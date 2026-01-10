---
title: Comment ajouter des utilisateurs IAM à accès limité à un cluster EKS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-31T11:27:37.000Z'
originalURL: https://freecodecamp.org/news/adding-limited-access-iam-user-to-eks-cluster
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d3d740569d1a4ca36ad.jpg
tags:
- name: AWS
  slug: aws
- name: Cloud Services
  slug: cloud-services
- name: EKS
  slug: eks
- name: IAM
  slug: iam
- name: Kubernetes
  slug: kubernetes
seo_title: Comment ajouter des utilisateurs IAM à accès limité à un cluster EKS
seo_desc: 'By Faizan Bashir

  Introduction

  Elastic Kubernetes Service (EKS) is the fully managed Kubernetes service from AWS.
  It is deeply integrated with many AWS services, such as AWS Identity and Access
  Management (IAM) (for authentication to the cluster), Ama...'
---

Par Faizan Bashir

### **Introduction**

[Elastic Kubernetes Service (EKS)](https://aws.amazon.com/eks/) est le service Kubernetes entièrement géré par AWS. Il est profondément intégré à de nombreux services AWS, tels que AWS Identity and Access Management (IAM) (pour l'authentification au cluster), Amazon CloudWatch (pour la journalisation), Auto Scaling Groups (pour la mise à l'échelle des nœuds de travail) et Amazon Virtual Private Cloud (VPC) (pour la mise en réseau). De nombreuses entreprises font confiance à Amazon EKS pour exécuter leurs charges de travail conteneurisées.

![Authentification IAM EKS](https://faizanbashir.me/assets/images/posts/eks-iam.png)

EKS utilise IAM pour fournir une authentification à votre cluster Kubernetes (via la commande `aws eks get-token`, ou l'[AWS IAM Authenticator pour Kubernetes](https://github.com/kubernetes-sigs/aws-iam-authenticator)). Pour l'autorisation, il s'appuie sur le contrôle d'accès basé sur les rôles (RBAC) natif de [Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/rbac/). IAM est utilisé pour l'authentification à votre cluster EKS. Et vous pouvez gérer les permissions pour interagir avec l'API Kubernetes de votre cluster via le système RBAC natif de Kubernetes.

## Comment créer un utilisateur IAM

Rendez-vous sur votre [Console AWS](https://console.aws.amazon.com/) où vous trouverez le service [IAM](https://console.aws.amazon.com/iam/home) listé sous le groupe "Sécurité, Identité et Conformité". Dans le tableau de bord IAM, cliquez sur l'onglet Utilisateurs et cliquez sur le bouton "Ajouter un utilisateur".

![Onglet Utilisateurs du tableau de bord IAM AWS](https://faizanbashir.me/assets/images/posts/1*VtA7fGzE2a_h6yMTl69lBw.png)

Créez un nouvel utilisateur et autorisez l'accès **programmatique** en cochant la case "Accès programmatique". Vous n'avez besoin d'aucune permission particulière pour que votre utilisateur accède à EKS. Vous pouvez continuer sans sélectionner aucune permission.

![Clés d'accès](https://faizanbashir.me/assets/images/posts/1*7FqyvVFoRxZClqC16SevXw.png)

Après la création de l'utilisateur, vous aurez accès à l'**ID de la clé d'accès** et à la **Clé d'accès secrète** de l'utilisateur. Vous devrez utiliser ces clés dans l'étape suivante.

## Configurer l'AWS CLI

Configurer votre AWS CLI avec un nouvel utilisateur est aussi simple que d'exécuter la commande `aws configure` et de fournir l'`ID de la clé d'accès AWS` et la `Clé d'accès secrète AWS`. Le `Nom de la région par défaut` et le `Format de sortie par défaut` sont facultatifs, cependant.

```shell
$ aws configure --profile eks-user
AWS Access Key ID [None]: AKIAI44QH8DHBEXAMPLE
AWS Secret Access Key [None]: je7MtGbClwBF/2Zp9Utk/h3yCo8nvbEXAMPLEKEY
Default region name [None]: us-east-1
Default output format [None]: text
```

Une fois configuré, vous pouvez tester pour voir si l'utilisateur est correctement configuré en utilisant la commande `aws sts get-caller-identity` :

```shell
$ aws sts get-caller-identity --profile eks-user
```

Si l'utilisateur est correctement configuré avec l'utilitaire `aws` cli, vous devriez voir une réponse comme celle montrée ci-dessous :

```json
{
    "UserId": "AIDAX7JPBEM4A6FTJRTMB",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/eks-user"
}
```

## Créer un Rôle et un RoleBinding pour l'utilisateur

Avec votre utilisateur IAM correctement configuré, vous pouvez créer un rôle pour l'utilisateur. Ce snippet de code crée un rôle nommé `eks-user-role` avec une modeste permission `list` pour la ressource `pods` dans votre cluster.

```yaml
kind: Role
metadata:
  name: eks-user-role
rules:
- apiGroups: [""]
  resources: ["pods"]
  verbs: ["list"]
```

Enregistrez le snippet de code ci-dessus dans un fichier et appliquez le Rôle à votre cluster Kubernetes :

```shell
$ kubectl apply -f role.yaml
```

Avec le rôle configuré, vous devez créer un RoleBinding correspondant :

```yaml
apiVersion: rbac.authorization.k8s.io/v1
kind: RoleBinding
metadata:
  name: eks-user-role-binding
subjects:
- kind: User
  name: eks-user
  apiGroup: rbac.authorization.k8s.io
roleRef:
  kind: Role
  name: eks-user-role
  apiGroup: rbac.authorization.k8s.io
```

Enregistrez le snippet de code ci-dessus dans un fichier et appliquez le Role Binding à votre cluster Kubernetes :

```shell
$ kubectl apply -f role-binding.yaml
```

## Ajouter l'utilisateur à la configmap aws-auth

Si vous souhaitez accorder à des utilisateurs ou rôles AWS supplémentaires la possibilité d'interagir avec votre cluster EKS, vous devez ajouter les utilisateurs/rôles à la ConfigMap `aws-auth` dans Kubernetes dans l'espace de noms `kube-system`.

Vous pouvez le faire soit en l'éditant avec la commande `kubectl edit` :

```shell
$ kubectl edit configmap aws-auth -n kube-system
```

Soit en important la ConfigMap `aws-auth` et en appliquant les modifications :

```shell
$ kubectl get configmap aws-auth -n kube-system -o yaml > aws-auth.yaml
```

Ajoutez l'utilisateur sous `mapUsers` en tant qu'élément dans la ConfigMap `aws-auth` :

```yaml
data:
  mapUsers: |
    - userarn: arn:aws:iam::123456789012:user/eks-user
      username: eks-user
      groups:
      - eks-role
```

Si l'utilisateur est correctement configuré, vous devriez pouvoir lister les pods dans le Cluster :

```shell
$ kubectl get pods --as eks-user
```

Le drapeau `--as` simule la demande à Kubernetes en tant qu'utilisateur donné. Vous pouvez utiliser ce drapeau pour tester les permissions pour n'importe quel utilisateur.

## Configurer les permissions pour l'utilisateur

Le rôle que vous avez défini précédemment n'avait la permission que de lister les pods. L'`eks-user` ne peut pas accéder à d'autres ressources Kubernetes comme les Deployments, ConfigMaps, Events, Secrets, logs ou même accéder à un shell dans un pod donné.

Dans un scénario réel, vous devrez fournir des permissions à un utilisateur pour accéder aux ressources requises. Le snippet de code ci-dessous fournit l'accès aux ressources telles que `events`, `pods`, `deployments`, `configmaps` et `secrets`.

```yaml
rules:
- apiGroups: [""]
  resources: ["events"]
  verbs: ["get", "list", "watch"]
- apiGroups: [""]
  resources: ["pods", "pods/log", "pods/exec"]
  verbs: ["list", "get", "create", "update", "delete"]
- apiGroups: ["extensions", "apps"]
  resources: ["deployments"]
  verbs: ["list", "get", "create", "update", "delete"]
- apiGroups: [""]
  resources: ["configmaps"]
  verbs: ["list", "get", "create", "update", "delete"]
- apiGroups: [""]
  resources: ["secrets"]
  verbs: ["list", "get", "create", "update", "delete"]
```

Ajoutez les permissions ci-dessus au fichier `role.yaml` et appliquez les modifications, en utilisant `kubectl apply -f`.

## Testez, testez et testez !

Maintenant, testez pour voir si les permissions ont été correctement appliquées à l'`eks-user`. Vous pouvez tester la même chose en utilisant le drapeau `--as USERNAME` mentionné ci-dessus ou en définissant `eks-user` comme profil par défaut pour l'utilitaire `aws` cli.

```shell
$ export AWS_PROFILE=eks-user
```

Une fois configuré, vous pouvez tester pour voir si l'utilisateur est correctement configuré en utilisant la commande `aws sts get-caller-identity` :

```shell
$ aws sts get-caller-identity
```

Vous devriez voir une réponse comme celle ci-dessous, indiquant que l'utilisateur est correctement configuré avec votre utilitaire `aws` cli :

```json
{
    "UserId": "AIDAX7JPBEM4A6FTJRTMB",
    "Account": "123456789012",
    "Arn": "arn:aws:iam::123456789012:user/eks-user"
}
```

Testez les permissions de l'utilisateur avec les commandes mentionnées ci-dessous.

```shell
$ kubectl get pods
$ kubectl get secrets
$ kubectl get configmaps
$ kubectl get deployments
$ kubectl logs <pod-name>
$ kubectl exec -it <pod-name> sh
$ kubectl create configmap my-cm --from-literal=db_username=<USERNAME> --from-literal=db_host=<HOSTNAME>
$ kubectl create secret generic my-secret --from-literal=db_password=<SOME_STRONG_PASSWORD>
```

En résumé, l'utilisateur `eks-user` devrait être en mesure d'effectuer toutes les actions spécifiées dans le tableau des verbes pour `pods`, `secrets`, `configmaps`, `deployments` et `events`. Vous pouvez en lire plus ici [Aperçu de l'autorisation Kubernetes](https://kubernetes.io/docs/reference/access-authn-authz/authorization/).

## Puis-je ou non

Vous pouvez utiliser `auth can-i` pour vérifier si vous avez la permission pour une ressource. Pour voir si vous avez la permission de lister les pods, exécutez simplement :

```shell
$ kubectl auth can-i get pods
```

La réponse sera un simple `yes` ou `no`. Amazing, n'est-ce pas ?

Vous voulez vérifier si vous avez les permissions `cluster-admin` ? Lancez ceci :

```shell
$ kubectl auth can-i "*" "*"
```

## Conclusion

EKS fournit le plan de contrôle Kubernetes avec la couche de persistance backend. Le serveur API Kubernetes et les nœuds maîtres sont provisionnés et mis à l'échelle dans diverses zones de disponibilité, ce qui entraîne une haute disponibilité et élimine un point de défaillance unique. Un cluster Kubernetes géré par AWS peut résister à la perte d'une zone de disponibilité.

Les contrôles d'accès et d'autorisation sont essentiels pour tout système de sécurité. Kubernetes nous fournit un mécanisme de permission RBAC robuste et génial.

_Publié à l'origine sur_ [**faizanbashir.me**](https://faizanbashir.me/adding-limited-access-iam-user-to-eks-cluster)