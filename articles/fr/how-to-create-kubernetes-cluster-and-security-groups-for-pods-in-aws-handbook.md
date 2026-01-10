---
title: Comment créer un cluster Kubernetes et des Security Groups pour les Pods dans
  AWS [Guide complet]
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2025-10-15T23:53:37.631Z'
originalURL: https://freecodecamp.org/news/how-to-create-kubernetes-cluster-and-security-groups-for-pods-in-aws-handbook
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1760572399710/e6ff9b5b-2fa5-4e61-9b89-9b68c81e6d46.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: AWS
  slug: aws
- name: Security
  slug: security
- name: handbook
  slug: handbook
seo_title: Comment créer un cluster Kubernetes et des Security Groups pour les Pods
  dans AWS [Guide complet]
seo_desc: Amazon Elastic Kubernetes Service (EKS) Security Groups for Pods is a powerful
  feature that enables fine-grained network security controls at the pod level. This
  guide walks you through implementing this feature, from initial cluster setup to
  testing...
---

Amazon Elastic Kubernetes Service (EKS) Security Groups for Pods est une fonctionnalité puissante qui permet un contrôle granulaire de la sécurité réseau au niveau du pod. Ce guide vous accompagne dans l'implémentation de cette fonctionnalité, de la configuration initiale du cluster aux tests d'assignation des Security Groups au niveau du pod.

Traditionnellement, les Security Groups ne pouvaient être assignés qu'au niveau de l'instance EC2 dans les clusters EKS. Cela signifiait que tous les pods s'exécutant sur un nœud partageaient les mêmes règles de sécurité réseau. Avec les Security Groups pour les Pods, vous pouvez désormais assigner des Security Groups spécifiques à des pods individuels, offrant un contrôle beaucoup plus fin sur l'accès réseau.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Comprendre l'architecture](#heading-comprendre-larchitecture)
    
3. [Fondations de l'infrastructure](#heading-fondations-de-linfrastructure)
    
4. [Configuration du cluster EKS](#heading-configuration-du-cluster-eks)
    
5. [Configuration de l'instance de gestion](#heading-configuration-de-linstance-de-gestion)
    
6. [Configuration des Security Groups](#heading-configuration-des-security-groups)
    
7. [Configuration de la base de données](#heading-configuration-de-la-base-de-donnees)
    
8. [Configuration du plugin CNI](#heading-configuration-du-plugin-cni)
    
9. [Mise en œuvre des politiques de sécurité](#heading-mise-en-oeuvre-des-politiques-de-securite)
    
10. [Tests et validation](#heading-tests-et-validation)
    
11. [Nettoyage et maintenance](#heading-nettoyage-et-maintenance)
    
12. [Conclusion](#heading-conclusion)
    

## Prérequis

Avant de commencer ce guide, assurez-vous d'avoir :

* Un compte AWS avec les permissions appropriées
    
* L'AWS CLI configurée sur votre machine locale
    
* Une compréhension de base des concepts Kubernetes
    
* Une familiarité avec les concepts réseau AWS (VPCs, Security Groups, sous-réseaux)
    
* Une compréhension des fondamentaux d'Amazon EKS
    

## Comprendre l'architecture

Avant de passer à l'implémentation, comprenons comment les Security Groups pour les Pods modifient le modèle réseau d'EKS. Nous commencerons par l'approche traditionnelle, puis nous explorerons le modèle amélioré et enfin les composants qui permettent son fonctionnement.

### Réseautage EKS traditionnel

Dans la configuration réseau EKS standard, la sécurité s'opère au niveau du nœud plutôt qu'au niveau du pod. Lorsque vous créez un cluster EKS selon le modèle traditionnel, chaque nœud de travail (worker node) EC2 se voit assigner un Security Group. Tous les pods s'exécutant sur ce nœud héritent des mêmes paramètres de Security Group que leur nœud hôte. Cela signifie que si vous avez dix applications différentes sur le même nœud, elles partagent toutes des règles de sécurité réseau identiques.

Cette approche présente des limitations importantes. Par exemple, si un pod doit accéder à une base de données alors qu'un autre ne le devrait pas, vous ne pouvez pas appliquer cette distinction lorsque les deux pods partagent le Security Group du nœud. La frontière de sécurité se situe au niveau du nœud, créant un modèle de sécurité grossier.

![Architecture sans Security Groups pour les pods](https://cdn.hashnode.com/res/hashnode/image/upload/v1758251803143/fa7ac487-a847-4029-9543-839c428ec20c.png align="center")

### Architecture des Security Groups pour les Pods

Ce modèle réseau change complètement ce paradigme. Avec les Security Groups pour les Pods activés, vous pouvez assigner des Security Groups dédiés à des pods individuels en fonction de leurs besoins spécifiques. Au lieu que tous les pods héritent du Security Group du nœud, certains pods peuvent obtenir leur propre Elastic Network Interface (ENI) avec des assignations de Security Group personnalisées.

Une ENI (Elastic Network Interface) est essentiellement une carte réseau virtuelle dans AWS. Tout comme votre ordinateur physique possède une carte réseau pour se connecter à Internet, les instances EC2 et désormais les pods individuels peuvent avoir leurs propres interfaces réseau virtuelles. Chaque ENI peut avoir sa propre adresse IP, ses propres Security Groups et ses propres paramètres réseau. Lorsque nous assignons une ENI à un pod, ce pod obtient sa propre identité réseau dédiée, distincte du nœud sur lequel il s'exécute.

Cette architecture offre une véritable sécurité au niveau du pod. Par exemple, vous pourriez avoir un pod frontend et un pod d'accès à la base de données s'exécutant sur le même nœud. Le pod frontend utilise le Security Group du nœud et ne peut pas accéder à la base de données. Pendant ce temps, le pod d'accès à la base de données obtient sa propre ENI avec un Security Group qui autorise explicitement les connexions à la base de données. Même s'ils partagent le même nœud physique, ces pods ont des profils de sécurité réseau complètement différents.

![Architecture avec Security Groups pour les pods](https://cdn.hashnode.com/res/hashnode/image/upload/v1758252157480/fda41975-aabc-4e1c-a638-75a26c565bb0.png align="center")

### Comment ça marche :

L'implémentation des Security Groups pour les Pods repose sur plusieurs mécanismes interconnectés. Tout d'abord, lorsque vous marquez un pod pour un traitement spécial via une `SecurityGroupPolicy`, le système provisionne automatiquement une ENI dédiée pour ce pod. Cette assignation d'ENI se fait via la fonctionnalité de réseau par branche (branch networking) de l'[AWS VPC CNI](https://docs.aws.amazon.com/eks/latest/best-practices/vpc-cni.html), qui permet d'attacher plusieurs interfaces réseau à une seule instance EC2.

La capacité de branch networking est cruciale ici. Les instances EC2 ont des limites sur le nombre d'ENI qu'elles peuvent supporter. Par exemple, une instance t3.medium peut supporter jusqu'à trois ENI, tandis qu'une m5.large peut en supporter jusqu'à quatre. Le plugin VPC CNI utilise ces emplacements d'ENI supplémentaires pour créer des interfaces de branche pour les pods qui nécessitent des Security Groups personnalisés. Chaque interface de branche peut alors avoir sa propre configuration de Security Group indépendante de l'interface réseau principale du nœud.

Ce contrôle granulaire signifie que vous pouvez désormais appliquer des politiques réseau au niveau de l'application. Différents microservices dans votre cluster peuvent avoir des modèles d'accès réseau complètement différents, même s'ils s'exécutent sur la même infrastructure.

### Composants clés :

Plusieurs composants Kubernetes et AWS collaborent pour activer cette fonctionnalité.

#### CRD SecurityGroupPolicy

La Custom Resource Definition (CRD) SecurityGroupPolicy est un objet Kubernetes que vous créez pour indiquer au système quels pods doivent recevoir quels Security Groups. Vous utilisez des sélecteurs de labels Kubernetes standard pour identifier les pods, puis spécifiez un ou plusieurs ID de Security Group AWS. La création d'une SecurityGroupPolicy ne modifie rien immédiatement ; elle crée une règle qui s'appliquera aux futurs pods correspondant à ces labels.

#### Contrôleur de ressources VPC

Le contrôleur de ressources VPC est un composant AWS qui s'exécute dans le Control Plane de votre cluster. Ce contrôleur surveille en permanence les pods qui correspondent à vos définitions de SecurityGroupPolicy.

Lorsqu'un pod correspondant est créé, le contrôleur communique avec les API AWS EC2 pour provisionner l'ENI nécessaire, attacher les Security Groups spécifiés et configurer l'interface réseau. Il gère également le processus de nettoyage lorsque les pods sont supprimés.

#### AWS VPC CNI

Enfin, le plugin AWS VPC CNI est amélioré pour supporter cette fonctionnalité de branch networking. Lorsque le contrôleur de ressources VPC provisionne une ENI pour un pod, le plugin CNI sur le nœud de travail gère la configuration réseau de bas niveau. Il attache l'ENI à l'espace de noms réseau du pod, configure les règles de routage et s'assure que le trafic de ce pod passe par l'interface dédiée.

## Fondations de l'infrastructure

Nous allons maintenant construire l'infrastructure AWS sous-jacente. Cela inclut la configuration des rôles IAM, la création du VPC avec les sous-réseaux appropriés et la configuration des composants réseau.

### Configuration des rôles et politiques IAM

Avant de créer l'infrastructure, nous devons configurer les rôles IAM. Considérez les rôles IAM comme des cartes d'identité que les services présentent à AWS pour prouver qu'ils sont autorisés à effectuer certaines actions.

#### Rôle de service du cluster EKS :

Tout d'abord, nous créons le rôle IAM que le service EKS lui-même utilisera pour gérer votre cluster.

```bash
# Créer le rôle de service du cluster EKS
aws iam create-role \
  --role-name EKSClusterRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "eks.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'
```

**Explication :**

Cette commande crée un rôle IAM qui établit une confiance entre votre compte AWS et le service EKS :

* `assume-role-policy-document` : Définit quel service AWS peut assumer ce rôle.
* `"Service": "eks.amazonaws.com"` : Seul le service EKS peut utiliser ce rôle.

![Rôle IAM du cluster EKS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758420978401/1f7a7849-923b-4378-9ee5-1063cf4b2ffd.png align="center")

#### Politiques attachées au rôle du cluster EKS :

Nous devons attacher des politiques gérées qui accordent les permissions réelles dont EKS a besoin.

```bash
# Attacher les politiques requises
aws iam attach-role-policy \
  --role-name EKSClusterRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSClusterPolicy

aws iam attach-role-policy \
  --role-name EKSClusterRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSVPCResourceController
```

La politique **AmazonEKSClusterPolicy** permet à EKS de gérer les composants du Control Plane Kubernetes. La seconde, **AmazonEKSVPCResourceController**, est critique pour notre implémentation des Security Groups pour les Pods, car elle autorise la gestion des ENI et des ressources VPC au nom des pods.

![Politique du rôle du cluster EKS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758421026844/2ef6755d-1306-40f5-8048-04f3334a8308.png align="center")

#### Rôle du groupe de nœuds EKS :

Ensuite, nous créons le rôle IAM que les nœuds de travail EC2 utiliseront.

```bash
# Créer le rôle du groupe de nœuds
aws iam create-role \
  --role-name EKSNodeGroupRole \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'
```

![Rôle du groupe de nœuds EKS](https://cdn.hashnode.com/res/hashnode/image/upload/v1758417915291/f06a2ab3-d6be-4bfc-a489-fae3a0c22e8f.png align="center")

#### Politiques attachées au rôle du groupe de nœuds :

```bash
# Attacher les politiques requises pour les nœuds de travail
aws iam attach-role-policy \
  --role-name EKSNodeGroupRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy

aws iam attach-role-policy \
  --role-name EKSNodeGroupRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy

aws iam attach-role-policy \
  --role-name EKSNodeGroupRole \
  --policy-arn arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
```

1. **AmazonEKSWorkerNodePolicy** : Permet aux nœuds de se connecter au cluster EKS.
2. **AmazonEKS_CNI_Policy** : Permet au plugin CNI de gérer le réseau des pods.
3. **AmazonEC2ContainerRegistryReadOnly** : Permet de récupérer les images depuis ECR.

#### Rôle IAM pour l'instance de gestion :

Nous créons un rôle pour l'instance EC2 qui nous servira à gérer le cluster.

```bash
# Créer le rôle IAM pour l'instance de gestion
aws iam create-role \
  --role-name EKS-Management-Role \
  --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Principal": {
          "Service": "ec2.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
      }
    ]
  }'

# Créer le profil d'instance
aws iam create-instance-profile \
  --instance-profile-name EKS-Management-Profile

# Ajouter le rôle au profil d'instance
aws iam add-role-to-instance-profile \
  --instance-profile-name EKS-Management-Profile \
  --role-name EKS-Management-Role

# Créer et attacher une politique personnalisée pour la gestion EKS
cat > eks-management-policy.json << 'EOF'
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "eks:*",
                "ec2:DescribeInstances",
                "ec2:DescribeSecurityGroups",
                "ec2:DescribeVpcs",
                "ec2:DescribeSubnets",
                "ec2:DescribeNetworkInterfaces",
                "ec2:CreateSecurityGroup",
                "ec2:AuthorizeSecurityGroupIngress",
                "ec2:RevokeSecurityGroupIngress",
                "rds:DescribeDBInstances",
                "rds:CreateDBInstance",
                "rds:DeleteDBInstance",
                "iam:PassRole"
            ],
            "Resource": "*"
        }
    ]
}
EOF

aws iam create-policy \
  --policy-name EKS-Management-Policy \
  --policy-document file://eks-management-policy.json

aws iam attach-role-policy \
  --role-name EKS-Management-Role \
  --policy-arn arn:aws:iam::$(aws sts get-caller-identity --query Account --output text):policy/EKS-Management-Policy
```

### Infrastructure VPC et réseau

#### Création et configuration du VPC

```bash
# Créer le VPC
export VPC_ID=$(aws ec2 create-vpc \
  --cidr-block 10.0.0.0/16 \
  --name 'eks-security-demo'
  --query 'Vpc.VpcId' \
  --output text)

# Créer l'Internet Gateway
export IGW_ID=$(aws ec2 create-internet-gateway \
  --query 'InternetGateway.InternetGatewayId' \
  --output text)

# Attacher l'Internet Gateway au VPC
aws ec2 attach-internet-gateway \
  --internet-gateway-id $IGW_ID \
  --vpc-id $VPC_ID
```

#### Stratégie d'architecture des sous-réseaux

Nous créons quatre sous-réseaux (deux publics, deux privés) répartis sur deux zones de disponibilité.

```bash
# Sous-réseaux publics
export PUBLIC_SUBNET_1=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.1.0/24 \
  --availability-zone eu-west-1a \
  --query 'Subnet.SubnetId' \
  --output text)

export PUBLIC_SUBNET_2=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.2.0/24 \
  --availability-zone eu-west-1b \
  --query 'Subnet.SubnetId' \
  --output text)

# Activer l'assignation auto d'IP publique pour les sous-réseaux publics
aws ec2 modify-subnet-attribute --subnet-id $PUBLIC_SUBNET_1 --map-public-ip-on-launch
aws ec2 modify-subnet-attribute --subnet-id $PUBLIC_SUBNET_2 --map-public-ip-on-launch

# Sous-réseaux privés
export PRIVATE_SUBNET_1=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.3.0/24 \
  --availability-zone eu-west-1a \
  --query 'Subnet.SubnetId' \
  --output text)

export PRIVATE_SUBNET_2=$(aws ec2 create-subnet \
  --vpc-id $VPC_ID \
  --cidr-block 10.0.4.0/24 \
  --availability-zone eu-west-1b \
  --query 'Subnet.SubnetId' \
  --output text)
```

#### Marquage (Tagging) des sous-réseaux EKS

```bash
# Taguer les sous-réseaux pour l'auto-découverte EKS
aws ec2 create-tags \
  --resources $PUBLIC_SUBNET_1 $PUBLIC_SUBNET_2 \
  --tags Key=kubernetes.io/cluster/pod-security-cluster-demo,Value=shared \
         Key=kubernetes.io/role/elb,Value=1

aws ec2 create-tags \
  --resources $PRIVATE_SUBNET_1 $PRIVATE_SUBNET_2 \
  --tags Key=kubernetes.io/cluster/pod-security-cluster-demo,Value=shared \
         Key=kubernetes.io/role/internal-elb,Value=1
```

#### Routage et NAT Gateway

```bash
# Créer la table de routage publique
export PUBLIC_RT=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)

# Route vers l'Internet Gateway
aws ec2 create-route --route-table-id $PUBLIC_RT --destination-cidr-block 0.0.0.0/0 --gateway-id $IGW_ID

# Associer les sous-réseaux publics
aws ec2 associate-route-table --subnet-id $PUBLIC_SUBNET_1 --route-table-id $PUBLIC_RT
aws ec2 associate-route-table --subnet-id $PUBLIC_SUBNET_2 --route-table-id $PUBLIC_RT

# Créer la NAT Gateway
export EIP_ALLOC=$(aws ec2 allocate-address --domain vpc --query 'AllocationId' --output text)
export NAT_GW=$(aws ec2 create-nat-gateway --subnet-id $PUBLIC_SUBNET_1 --allocation-id $EIP_ALLOC --query 'NatGateway.NatGatewayId' --output text)

# Attendre que la NAT Gateway soit disponible
aws ec2 wait nat-gateway-available --nat-gateway-ids $NAT_GW

# Table de routage privée
export PRIVATE_RT=$(aws ec2 create-route-table --vpc-id $VPC_ID --query 'RouteTable.RouteTableId' --output text)
aws ec2 create-route --route-table-id $PRIVATE_RT --destination-cidr-block 0.0.0.0/0 --nat-gateway-id $NAT_GW

# Associer les sous-réseaux privés
aws ec2 associate-route-table --subnet-id $PRIVATE_SUBNET_1 --route-table-id $PRIVATE_RT
aws ec2 associate-route-table --subnet-id $PRIVATE_SUBNET_2 --route-table-id $PRIVATE_RT
```

## Configuration du cluster EKS

### Création du cluster EKS

```bash
export CLUSTER_ROLE_ARN=$(aws iam get-role --role-name EKSClusterRole --query 'Role.Arn' --output text)

# Créer le cluster EKS
aws eks create-cluster \
  --name pod-security-cluster-demo \
  --kubernetes-version 1.33 \
  --role-arn $CLUSTER_ROLE_ARN \
  --access-config authenticationMode=API_AND_CONFIG_MAP \
  --resources-vpc-config subnetIds=$PUBLIC_SUBNET_1,$PUBLIC_SUBNET_2,$PRIVATE_SUBNET_1,$PRIVATE_SUBNET_2

# Attendre que le cluster soit actif
aws eks wait cluster-active --name pod-security-cluster-demo
```

### Configuration du groupe de nœuds gérés

```bash
export NODE_ROLE_ARN=$(aws iam get-role --role-name EKSNodeGroupRole --query 'Role.Arn' --output text)

# Créer le groupe de nœuds gérés
aws eks create-nodegroup \
  --cluster-name pod-security-cluster-demo \
  --nodegroup-name workers \
  --subnets $PRIVATE_SUBNET_1 $PRIVATE_SUBNET_2 \
  --node-role $NODE_ROLE_ARN \
  --instance-types m5.large \
  --scaling-config minSize=1,maxSize=3,desiredSize=2 \
  --disk-size 20 \
  --capacity-type ON_DEMAND

# Attendre que le groupe de nœuds soit actif
aws eks wait nodegroup-active --cluster-name pod-security-cluster-demo --nodegroup-name workers
```

### Configuration de l'accès au cluster EKS

```bash
export MANAGEMENT_ROLE_ARN=$(aws iam get-role --role-name EKS-Management-Role --query 'Role.Arn' --output text)

# Créer l'entrée d'accès
aws eks create-access-entry --cluster-name pod-security-cluster-demo --principal-arn $MANAGEMENT_ROLE_ARN

# Associer la politique admin
aws eks associate-access-policy \
  --cluster-name pod-security-cluster-demo \
  --principal-arn $MANAGEMENT_ROLE_ARN \
  --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy \
  --access-scope type=cluster
```

## Configuration de l'instance de gestion

### Security Group pour l'accès à la gestion

```bash
export EC2_SG=$(aws ec2 create-security-group \
  --group-name EKS-Management-SG \
  --description "Security group for EKS management instance" \
  --vpc-id $VPC_ID --query 'GroupId' --output text)

# Autoriser SSH
aws ec2 authorize-security-group-ingress --group-id $EC2_SG --protocol tcp --port 22 --cidr 0.0.0.0/0
```

### Installation automatisée des outils

```bash
# Créer le script user-data
cat > user-data.sh << 'EOF'
#!/bin/bash
yum update -y
yum install -y unzip git
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
./aws/install
curl -O https://s3.us-west-2.amazonaws.com/amazon-eks/1.33.4/2025-08-20/bin/linux/amd64/kubectl
chmod +x ./kubectl
mkdir -p $HOME/bin && cp ./kubectl $HOME/bin/kubectl && export PATH=$HOME/bin:$PATH
curl --silent --location "https://github.com/weaveworks/eksctl/releases/latest/download/eksctl_$(uname -s)_amd64.tar.gz" | tar xz -C /tmp
cp /tmp/eksctl /usr/local/bin
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
sudo amazon-linux-extras install -y postgresql13
echo "Management tools installed successfully" > /var/log/setup-complete.log
EOF

# Lancer l'instance
export AMI_ID=$(aws ec2 describe-images --owners amazon --filters "Name=name,Values=amzn2-ami-hvm-*" --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' --output text)
export INSTANCE_ID=$(aws ec2 run-instances --image-id $AMI_ID --count 1 --instance-type t3.micro --subnet-id $PUBLIC_SUBNET_1 --security-group-ids $EC2_SG --iam-instance-profile Name=EKS-Management-Profile --user-data file://user-data.sh --query 'Instances[0].InstanceId' --output text)
```

## Configuration des Security Groups

### Récupération des informations réseau du cluster

```bash
aws eks update-kubeconfig --name pod-security-cluster-demo --region eu-west-1 
kubectl get nodes 
```

### Création du Security Group au niveau du pod

```bash
aws ec2 create-security-group --description 'Pod Security Group - Database Access' --group-name 'POD_SG' --vpc-id ${VPC_ID}
export POD_SG=$(aws ec2 describe-security-groups --filters Name=group-name,Values=POD_SG Name=vpc-id,Values=${VPC_ID} --query "SecurityGroups[0].GroupId" --output text)
```

### Règles de communication inter-services

```bash
# Autoriser le DNS
export NODE_GROUP_SG=$(aws ec2 describe-security-groups --filters Name=tag:Name,Values=eks-cluster-sg-pod-security-cluster-demo-* Name=vpc-id,Values=${VPC_ID} --query "SecurityGroups[0].GroupId" --output text)
aws ec2 authorize-security-group-ingress --group-id ${NODE_GROUP_SG} --protocol tcp --port 53 --source-group ${POD_SG}
aws ec2 authorize-security-group-ingress --group-id ${NODE_GROUP_SG} --protocol udp --port 53 --source-group ${POD_SG}
```

## Configuration de la base de données

### Création du groupe de sous-réseaux RDS

```bash
aws rds create-db-subnet-group --db-subnet-group-name rds-ekslab --db-subnet-group-description "Subnet group for EKS lab RDS instance" --subnet-ids ${PRIVATE_SUBNET_1} ${PRIVATE_SUBNET_2}
```

### Configuration de l'instance RDS

```bash
export RDS_PASSWORD=$(openssl rand -base64 32 | tr -d "=+/" | cut -c1-25)
aws rds create-db-instance \
   --db-instance-identifier rds-ekslab \
   --db-instance-class db.t3.micro \
   --engine postgres \
   --master-username postgres \
   --master-user-password ${RDS_PASSWORD} \
   --allocated-storage 20 \
   --vpc-security-group-ids ${RDS_SG} \
   --db-subnet-group-name rds-ekslab \
   --no-publicly-accessible
```

## Configuration du plugin CNI

### Activation du support ENI pour les Pods

```bash
kubectl -n kube-system set env daemonset aws-node ENABLE_POD_ENI=true
kubectl -n kube-system rollout restart daemonset aws-node
```

## Mise en œuvre des politiques de sécurité

### Création de la ressource SecurityGroupPolicy

```yaml
apiVersion: vpcresources.k8s.aws/v1beta1
kind: SecurityGroupPolicy
metadata:
  name: allow-rds-access
  namespace: networking
spec:
  podSelector:
    matchLabels:
      app: green-pod
  securityGroups:
    groupIds:
      - ${POD_SG}
```

## Tests et validation

Nous déployons deux pods : un "green-pod" (autorisé) et un "red-pod" (non autorisé). Le green-pod devrait pouvoir se connecter à la base de données grâce à son label correspondant à la `SecurityGroupPolicy`, tandis que le red-pod sera bloqué.

## Nettoyage et maintenance

### Suppression complète de l'infrastructure VPC

Il est crucial de supprimer les ressources dans l'ordre inverse de leur création : d'abord les pods et les politiques, puis le groupe de nœuds, le cluster EKS, la base de données RDS, et enfin le VPC et les rôles IAM.

## Conclusion

Ce guide complet a démontré comment implémenter les Security Groups pour les Pods dans Amazon EKS, offrant un contrôle de sécurité réseau granulaire.

J'espère que vous avez apprécié ce guide. Pour plus de projets DevOps pratiques, suivez-moi sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).