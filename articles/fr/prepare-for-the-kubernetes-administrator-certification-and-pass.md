---
title: Préparez-vous à la certification Certified Kubernetes Administrator (CKA) et
  réussissez l'examen
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2025-10-29T13:20:09.253Z'
originalURL: https://freecodecamp.org/news/prepare-for-the-kubernetes-administrator-certification-and-pass
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761739982392/f255a6af-6ec9-4136-b45f-6f14d4fb2c8c.jpeg
tags:
- name: Kubernetes
  slug: kubernetes
- name: youtube
  slug: youtube
seo_title: Préparez-vous à la certification Certified Kubernetes Administrator (CKA)
  et réussissez l'examen
seo_desc: We just posted a course on the freeCodeCamp.org YouTube channel to help
  prepare you for the Certified Kubernetes Administrator Certification. This course
  is designed to provide a deep, practical understanding of Kubernetes administration,
  from founda...
---

Nous venons de publier un cours sur la chaîne YouTube de freeCodeCamp.org pour vous aider à vous préparer à la certification Certified Kubernetes Administrator (CKA). Ce cours est conçu pour fournir une compréhension approfondie et pratique de l'administration Kubernetes, des concepts fondamentaux au troubleshooting avancé.

Vous pouvez regarder le cours sur [la chaîne YouTube de freeCodeCamp.org](https://youtu.be/Fr9GqFwl6NM) (2 heures de visionnage).

%[https://youtu.be/Fr9GqFwl6NM] 

Le cours contient de nombreuses démos utilisant Kubernetes. Vous trouverez ci-dessous toutes les commandes utilisées dans le cours afin qu'il soit plus facile pour vous de les suivre sur votre machine locale.

## Compagnon pratique CKA : Commandes et Demos

## Partie 1 : Fondamentaux de Kubernetes et Lab Setup

Cette section couvre la configuration d'un cluster à nœud unique à l'aide de `kubeadm` pour créer un environnement qui reflète l'examen CKA.

### Section 1.3 : Configuration de votre environnement de pratique CKA

#### **Étape 1 : Installer un Container Runtime (sur tous les nœuds)**

1. **Charger les modules kernel requis :**
    
    ```bash
    cat <<EOF | sudo tee /etc/modules-load.d/k8s.conf
    overlay
    br_netfilter
    EOF
    
    sudo modprobe overlay
    sudo modprobe br_netfilter
    ```
    
2. **Configurer sysctl pour le networking :**
    
    ```bash
    cat <<EOF | sudo tee /etc/sysctl.d/k8s.conf
    net.bridge.bridge-nf-call-iptables  = 1
    net.bridge.bridge-nf-call-ip6tables = 1
    net.ipv4.ip_forward               = 1
    EOF
    
    sudo sysctl --system
    ```
    
3. **Installer containerd :**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y containerd
    ```
    
4. **Configurer containerd pour le driver systemd cgroup :**
    
    ```bash
    sudo mkdir -p /etc/containerd
    sudo containerd config default | sudo tee /etc/containerd/config.toml
    sudo sed -i 's/SystemdCgroup = false/SystemdCgroup = true/' /etc/containerd/config.toml
    ```
    
5. **Redémarrer et activer containerd :**
    
    ```bash
    sudo systemctl restart containerd
    sudo systemctl enable containerd
    ```
    

#### **Étape 2 : Installer les binaires Kubernetes (sur tous les nœuds)**

1. **Désactiver la mémoire swap :**
    
    ```bash
    sudo swapoff -a
    # Commenter le swap dans fstab pour rendre le changement persistant :
    sudo sed -i '/ swap / s/^\(.*\)$/#\1/g' /etc/fstab
    ```
    
2. **Ajouter le dépôt apt Kubernetes :**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y apt-transport-https ca-certificates curl gpg
    sudo mkdir -p -m 755 /etc/apt/keyrings
    curl -fsSL https://pkgs.k8s.io/core:/stable:/v1.29/deb/Release.key | sudo gpg --dearmor -o /etc/apt/keyrings/kubernetes-apt-keyring.gpg
    echo 'deb [signed-by=/etc/apt/keyrings/kubernetes-apt-keyring.gpg] https://pkgs.k8s.io/core:/stable:/v1.29/deb/ /' | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```
    
3. **Installer et figer les binaires (ajuster la version si nécessaire) :**
    
    ```bash
    sudo apt-get update
    sudo apt-get install -y kubelet kubeadm kubectl
    sudo apt-mark hold kubelet kubeadm kubectl
    ```
    

#### **Étape 3 : Configurer un cluster à nœud unique (sur le Control Plane)**

1. **Initialiser le nœud du Control Plane :**
    
    ```bash
    sudo kubeadm init --pod-network-cidr=10.244.0.0/16
    ```
    
2. **Configurer kubectl pour l'utilisateur administrateur :**
    
    ```bash
    mkdir -p $HOME/.kube
    sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
    sudo chown $(id -u):$(id -g) $HOME/.kube/config
    ```
    
3. **Supprimer la Taint du Control Plane :**
    
    ```bash
    kubectl taint nodes --all node-role.kubernetes.io/control-plane-
    ```
    
4. **Installer le plugin CNI Flannel :**
    
    ```bash
    kubectl apply -f https://github.com/flannel-io/flannel/releases/latest/download/kube-flannel.yml
    ```
    
5. **Vérifier le cluster :**
    
    ```bash
    kubectl get nodes
    kubectl get pods -n kube-system
    ```
    

---

## Partie 2 : Architecture, Installation & Configuration du Cluster (25%)

### Section 2.1 : Bootstrapping d'un cluster multi-nœuds avec `kubeadm`

#### **Initialisation du Control Plane (Exécuter sur le nœud Control Plane)**

1. **Exécuter** `kubeadm init` (Remplacer `<control-plane-private-ip>`) :
    
    ```bash
    sudo kubeadm init --pod-network-cidr=192.168.0.0/16 --apiserver-advertise-address=<control-plane-private-ip>
    ```
    
    * **Note :** Sauvegardez la commande `kubeadm join` fournie en sortie.
        
2. **Installer le plugin CNI Calico :**
    
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.28.0/manifests/calico.yaml
    ```
    
3. **Vérifier l'installation du cluster et du CNI :**
    
    ```bash
    kubectl get pods -n kube-system
    kubectl get nodes
    ```
    

#### **Joindre les Worker Nodes (Exécuter sur chaque Worker Node)**

1. **Exécuter la commande join sauvegardée lors du** `kubeadm init` :
    
    ```bash
    # EXEMPLE - Utilisez la commande exacte de votre sortie kubeadm init
    sudo kubeadm join <control-plane-private-ip>:6443 --token <token> \
        --discovery-token-ca-cert-hash sha256:<hash>
    ```
    
2. **Vérifier le cluster complet (depuis le nœud Control Plane) :**
    
    ```bash
    kubectl get nodes -o wide
    ```
    

### Section 2.2 : Gestion du cycle de vie du cluster

#### **Mise à jour des clusters avec** `kubeadm` (Exemple : Mise à jour vers 1.29.1)

1. **Mise à jour du Control Plane : Mettre à jour le binaire** `kubeadm` :
    
    ```bash
    sudo apt-mark unhold kubeadm
    sudo apt-get update && sudo apt-get install -y kubeadm='1.29.1-1.1'
    sudo apt-mark hold kubeadm
    ```
    
2. **Planifier et appliquer la mise à jour (sur le nœud Control Plane) :**
    
    ```bash
    sudo kubeadm upgrade plan
    sudo kubeadm upgrade apply v1.29.1
    ```
    
3. **Mettre à jour** `kubelet` et `kubectl` (sur le nœud Control Plane) :
    
    ```bash
    sudo apt-mark unhold kubelet kubectl
    sudo apt-get update && sudo apt-get install -y kubelet='1.29.1-1.1' kubectl='1.29.1-1.1'
    sudo apt-mark hold kubelet kubectl
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
    
4. **Mise à jour du Worker Node : Drainer le nœud (depuis le nœud Control Plane) :**
    
    ```bash
    kubectl drain <node-to-upgrade> --ignore-daemonsets
    ```
    
5. **Mettre à jour les binaires (sur le Worker Node) :**
    
    ```bash
    # Sur le worker node
    sudo apt-mark unhold kubeadm kubelet
    sudo apt-get update
    sudo apt-get install -y kubeadm='1.29.1-1.1' kubelet='1.29.1-1.1'
    sudo apt-mark hold kubeadm kubelet
    ```
    
6. **Mettre à jour la configuration du nœud et redémarrer kubelet (sur le Worker Node) :**
    
    ```bash
    # Sur le worker node
    sudo kubeadm upgrade node
    sudo systemctl daemon-reload
    sudo systemctl restart kubelet
    ```
    
7. **Rétablir le nœud (Uncordon) (depuis le nœud Control Plane) :**
    
    ```bash
    kubectl uncordon <node-to-upgrade>
    ```
    

#### **Sauvegarde et restauration d'etcd (Exécuter sur le nœud Control Plane)**

1. **Effectuer une sauvegarde (en utilisant** `etcdctl` sur l'hôte) :
    
    ```bash
    # Créer d'abord le répertoire de sauvegarde
    sudo mkdir -p /var/lib/etcd-backup
    
    sudo ETCDCTL_API=3 etcdctl snapshot save /var/lib/etcd-backup/snapshot.db \
        --endpoints=https://127.0.0.1:2379 \
        --cacert=/etc/kubernetes/pki/etcd/ca.crt \
        --cert=/etc/kubernetes/pki/etcd/server.crt \
        --key=/etc/kubernetes/pki/etcd/server.key
    ```
    
2. **Effectuer une restauration (sur le nœud Control Plane) :**
    
    ```bash
    # Arrêter kubelet pour arrêter les pods statiques
    sudo systemctl stop kubelet
    
    # Restaurer le snapshot dans un nouveau répertoire de données
    sudo ETCDCTL_API=3 etcdctl snapshot restore /var/lib/etcd-backup/snapshot.db \
        --data-dir /var/lib/etcd-restored
    
    # !! IMPORTANT : Modifiez manuellement /etc/kubernetes/manifests/etcd.yaml pour pointer vers le nouveau data-dir /var/lib/etcd-restored !!
    
    # Redémarrer kubelet pour prendre en compte le changement de manifeste
    sudo systemctl start kubelet
    ```
    

### Section 2.3 : Mise en œuvre d'un Control Plane à Haute Disponibilité (HA)

1. **Initialiser le premier nœud du Control Plane (Remplacer** `<load-balancer-address:port>`) :
    
    ```bash
    sudo kubeadm init --control-plane-endpoint "load-balancer.example.com:6443" --upload-certs
    ```
    
    * **Note :** Sauvegardez la commande join spécifique à la HA et la `--certificate-key`.
        
2. **Joindre des nœuds de Control Plane supplémentaires (Exécuter sur les deuxième et troisième nœuds Control Plane) :**
    
    ```bash
    # EXEMPLE - Utilisez la commande exacte de votre sortie `kubeadm init`
    sudo kubeadm join load-balancer.example.com:6443 --token <token> \
        --discovery-token-ca-cert-hash sha256:<hash> \
        --control-plane --certificate-key <key>
    ```
    

### Section 2.4 : Gestion du Role-Based Access Control (RBAC)

#### **Démo : Accorder un accès en lecture seule**

1. **Créer un Namespace et un ServiceAccount :**
    
    ```bash
    kubectl create namespace rbac-test
    kubectl create serviceaccount dev-user -n rbac-test
    ```
    
2. **Créer le manifeste** `Role` (`role.yaml`) :
    
    ```yaml
    # role.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: Role
    metadata:
      namespace: rbac-test
      name: pod-reader
    rules:
    - apiGroups: [""] # "" indique le groupe d'API core
      resources: ["pods"]
      verbs: ["get", "list", "watch"]
    ```
    
    **Appliquer :** `kubectl apply -f role.yaml`
    
3. **Créer le manifeste** `RoleBinding` (`rolebinding.yaml`) :
    
    ```yaml
    # rolebinding.yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: read-pods
      namespace: rbac-test
    subjects:
    - kind: ServiceAccount
      name: dev-user
      namespace: rbac-test
    roleRef:
      kind: Role
      name: pod-reader
      apiGroup: rbac.authorization.k8s.io
    ```
    
    **Appliquer :** `kubectl apply -f rolebinding.yaml`
    
4. **Vérifier les permissions :**
    
    ```bash
    # Vérifier si le ServiceAccount peut lister les pods (Devrait être YES)
    kubectl auth can-i list pods --as=system:serviceaccount:rbac-test:dev-user -n rbac-test
    
    # Vérifier si le ServiceAccount peut supprimer les pods (Devrait être NO)
    kubectl auth can-i delete pods --as=system:serviceaccount:rbac-test:dev-user -n rbac-test
    ```
    

### Section 2.5 : Gestion des applications avec Helm et Kustomize

#### **Démo : Installer une application avec Helm**

1. **Ajouter un dépôt de Chart :**
    
    ```bash
    helm repo add bitnami https://charts.bitnami.com/bitnami
    helm repo update
    ```
    
2. **Installer un Chart avec une surcharge de valeur :**
    
    ```bash
    helm install my-nginx bitnami/nginx --set service.type=NodePort
    ```
    
3. **Gérer l'application :**
    
    ```bash
    helm upgrade my-nginx bitnami/nginx --set service.type=ClusterIP
    helm rollback my-nginx 1
    helm uninstall my-nginx
    ```
    

#### **Démo : Personnaliser un Deployment avec Kustomize**

1. **Créer le manifeste de base (**`my-app/base/deployment.yaml`) :
    
    ```bash
    mkdir -p my-app/base
    cat <<EOF > my-app/base/deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: my-app
      template:
        metadata:
          labels:
            app: my-app
        spec:
          containers:
          - name: nginx
            image: nginx:1.25.0
    EOF
    ```
    
2. **Créer le fichier Kustomization de base (**`my-app/base/kustomization.yaml`) :
    
    ```bash
    cat <<EOF > my-app/base/kustomization.yaml
    resources:
    - deployment.yaml
    EOF
    ```
    
3. **Créer l'overlay de production et le patch :**
    
    ```bash
    mkdir -p my-app/overlays/production
    cat <<EOF > my-app/overlays/production/patch.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: my-app
    spec:
      replicas: 3
    EOF
    cat <<EOF > my-app/overlays/production/kustomization.yaml
    bases:
    -../../base
    patches:
    - path: patch.yaml
    EOF
    ```
    
4. **Appliquer l'overlay (notez le flag** `-k` pour kustomize) :
    
    ```bash
    kubectl apply -k my-app/overlays/production
    ```
    
5. **Vérifier le changement :**
    
    ```bash
    kubectl get deployment my-app
    ```
    

---

## Partie 3 : Workloads & Scheduling (15%)

### Section 3.1 : Maîtriser les Deployments

#### **Démo : Effectuer une mise à jour progressive (Rolling Update)**

1. **Créer un manifeste de Deployment de base (**`deployment.yaml`) :
    
    ```yaml
    # deployment.yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: nginx-deployment
    spec:
      replicas: 3
      selector:
        matchLabels:
          app: nginx
      template:
        metadata:
          labels:
            app: nginx
        spec:
          containers:
          - name: nginx
            image: nginx:1.24.0
            ports:
            - containerPort: 80
    ```
    
    **Appliquer :** `kubectl apply -f deployment.yaml`
    
2. **Mettre à jour l'image du conteneur pour déclencher le rolling update :**
    
    ```bash
    kubectl set image deployment/nginx-deployment nginx=nginx:1.25.0
    ```
    
3. **Observer le déploiement :**
    
    ```bash
    kubectl rollout status deployment/nginx-deployment
    kubectl get pods -l app=nginx -w
    ```
    

#### **Exécuter et vérifier les retours en arrière (Rollbacks)**

1. **Voir l'historique des révisions :**
    
    ```bash
    kubectl rollout history deployment/nginx-deployment
    ```
    
2. **Revenir à la version précédente :**
    
    ```bash
    kubectl rollout undo deployment/nginx-deployment
    ```
    
3. **Revenir à une révision spécifique (ex: révision 1) :**
    
    ```bash
    kubectl rollout undo deployment/nginx-deployment --to-revision=1
    ```
    

### Section 3.2 : Configurer les applications avec ConfigMaps et Secrets

#### **Méthodes de création**

1. **ConfigMap : Création impérative :**
    
    ```bash
    # À partir de valeurs littérales
    kubectl create configmap app-config --from-literal=app.color=blue --from-literal=app.mode=production
    
    # À partir d'un fichier
    echo "retries = 3" > config.properties
    kubectl create configmap app-config-file --from-file=config.properties
    ```
    
2. **Secret : Création impérative :**
    
    ```bash
    # Kubernetes encodera automatiquement en base64
    kubectl create secret generic db-credentials --from-literal=username=admin --from-literal=password='s3cr3t'
    ```
    

#### **Démo : Consommer des ConfigMaps et des Secrets dans les Pods**

1. **Manifeste : Variables d'environnement (**`pod-config.yaml`) :
    
    ```yaml
    # pod-config.yaml (Suppose que le ConfigMap app-config-declarative et le Secret db-credentials existent)
    apiVersion: v1
    kind: Pod
    metadata:
      name: config-demo-pod
    spec:
      containers:
      - name: demo-container
        image: busybox
        command: ["/bin/sh", "-c", "env && sleep 3600"]
        env:
          - name: THEME
            valueFrom:
              configMapKeyRef:
                name: app-config-declarative
                key: ui.theme
          - name: DB_PASSWORD
            valueFrom:
              secretKeyRef:
                name: db-credentials
                key: password
      restartPolicy: Never
    ```
    
    **Appliquer :** `kubectl apply -f pod-config.yaml` **Vérifier :** `kubectl logs config-demo-pod`
    
2. **Manifeste : Volumes montés (**`pod-volume.yaml`) :
    
    ```yaml
    # pod-volume.yaml (Suppose que le ConfigMap app-config-file existe)
    apiVersion: v1
    kind: Pod
    metadata:
      name: volume-demo-pod
    spec:
      containers:
      - name: demo-container
        image: busybox
        command: ["/bin/sh", "-c", "cat /etc/config/config.properties && sleep 3600"]
        volumeMounts:
        - name: config-volume
          mountPath: /etc/config
      volumes:
      - name: config-volume
        configMap:
          name: app-config-file
      restartPolicy: Never
    ```
    
    **Appliquer :** `kubectl apply -f pod-volume.yaml` **Vérifier :** `kubectl logs volume-demo-pod`
    

### Section 3.3 : Mise en œuvre de l'Autoscaling des charges de travail

#### **Démo : Installer et vérifier le Metrics Server**

1. **Installer le Metrics Server :**
    
    ```bash
    kubectl apply -f https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
    ```
    
2. **Vérifier l'installation :**
    
    ```bash
    kubectl top nodes
    kubectl top pods -A
    ```
    

#### **Démo : Autoscaling d'un Deployment**

1. **Créer un Deployment avec des Resource Requests (nécessite le manifeste** `hpa-demo-deployment.yaml` non fourni, utilisez-en un simple) :
    
    ```bash
    kubectl create deployment php-apache --image=k8s.gcr.io/hpa-example --requests="cpu=200m"
    kubectl expose deployment php-apache --port=80
    ```
    
2. **Créer un HPA (cible 50% CPU, échelle 1-10 réplicas) :**
    
    ```bash
    kubectl autoscale deployment php-apache --cpu-percent=50 --min=1 --max=10
    ```
    
3. **Générer de la charge (s'exécutera en arrière-plan) :**
    
    ```bash
    kubectl run -it --rm load-generator --image=busybox -- /bin/sh -c "while true; do wget -q -O- http://php-apache; done"
    ```
    
4. **Observer le scaling :**
    
    ```bash
    kubectl get hpa -w
    ```
    
    *(Arrêtez le générateur de charge pour observer la réduction d'échelle)*
    

### Section 3.5 : Ordonnancement avancé

#### **Démo : Utiliser la Node Affinity**

1. **Étiqueter un nœud :**
    
    ```bash
    kubectl label node <votre-nom-de-worker-node> disktype=ssd
    ```
    
2. **Créer un Pod avec Node Affinity (nécessite le manifeste** `affinity-pod.yaml` non fourni, créez un pod factice pour le label du nœud) :
    
    ```bash
    # Créer le pod en utilisant les règles d'affinité
    kubectl apply -f affinity-pod.yaml # Ou manifeste équivalent avec node affinity
    ```
    

#### **Démo : Utiliser les Taints et Tolerations**

1. **Appliquer une Taint à un nœud (Effet :** `NoSchedule`) :
    
    ```bash
    kubectl taint node <un-autre-nom-de-worker-node> app=gpu:NoSchedule
    ```
    
2. **Créer un Pod avec une Toleration (nécessite le manifeste** `toleration-pod.yaml` non fourni, créez un pod factice pour la taint) :
    
    ```bash
    # Créer le pod en utilisant les règles de tolérance
    kubectl apply -f toleration-pod.yaml # Ou manifeste équivalent avec toleration
    ```
    
3. **Vérifier l'ordonnancement du Pod sur le nœud avec Taint :**
    
    ```bash
    kubectl get pod gpu-pod -o wide
    ```
    

---

## Partie 4 : Services & Networking (20%)

### Section 4.2 : Services Kubernetes

#### **Démo : Créer un service ClusterIP**

1. **Créer un Deployment :**
    
    ```bash
    kubectl create deployment my-app --image=nginx --replicas=2
    ```
    
2. **Exposer le Deployment avec un service ClusterIP (nécessite le manifeste** `clusterip-service.yaml` non fourni, utilisez une commande impérative) :
    
    ```bash
    kubectl expose deployment my-app --port=80 --target-port=80 --name=my-app-service --type=ClusterIP
    ```
    
3. **Vérifier l'accès (à l'intérieur d'un Pod temporaire) :**
    
    ```bash
    kubectl run tmp-shell --rm -it --image=busybox -- /bin/sh
    # À l'intérieur du shell :
    # wget -O- my-app-service
    ```
    

#### **Démo : Créer un service NodePort**

1. **Créer un service NodePort (nécessite le manifeste** `nodeport-service.yaml` non fourni, utilisez une commande impérative) :
    
    ```bash
    kubectl expose deployment my-app --port=80 --target-port=80 --name=my-app-nodeport --type=NodePort
    ```
    
2. **Vérifier les informations d'accès :**
    
    ```bash
    kubectl get service my-app-nodeport
    kubectl get nodes -o wide
    # Accès depuis l'extérieur via <NodeIP>:<NodePort>
    ```
    

### Section 4.3 : Ingress et l'API Gateway

#### **Démo : Routage basé sur le chemin avec NGINX Ingress**

1. **Installer le NGINX Ingress Controller :**
    
    ```bash
    kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/controller-v1.10.1/deploy/static/provider/cloud/deploy.yaml
    ```
    
2. **Déployer deux applications et services d'exemple :**
    
    ```bash
    kubectl create deployment app-one --image=k8s.gcr.io/echoserver:1.4
    kubectl expose deployment app-one --port=8080
    
    kubectl create deployment app-two --image=k8s.gcr.io/echoserver:1.4
    kubectl expose deployment app-two --port=8080
    ```
    
3. **Créer une ressource Ingress (nécessite le manifeste** `ingress.yaml` non fourni, utilisez la structure fournie pour créer le fichier) :
    
    ```bash
    # Appliquer ingress.yaml
    kubectl apply -f ingress.yaml
    ```
    
4. **Tester l'Ingress :**
    
    ```bash
    INGRESS_IP=$(kubectl get svc -n ingress-nginx ingress-nginx-controller -o jsonpath='{.status.loadBalancer.ingress.ip}')
    curl http://$INGRESS_IP/app1
    curl http://$INGRESS_IP/app2
    ```
    

### Section 4.4 : Network Policies

#### **Démo : Sécuriser une application avec des Network Policies**

1. **Créer une politique Ingress par défaut "Deny-All" (**`deny-all.yaml`) :
    
    ```yaml
    # deny-all.yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: default-deny-ingress
    spec:
      podSelector: {} # Correspond à tous les pods du namespace
      policyTypes:
      - Ingress
    ```
    
    **Appliquer :** `kubectl apply -f deny-all.yaml`
    
2. **Déployer un serveur Web et un service :**
    
    ```bash
    kubectl create deployment web-server --image=nginx
    kubectl expose deployment web-server --port=80
    ```
    
3. **Tenter une connexion (échouera) :**
    
    ```bash
    kubectl run tmp-shell --rm -it --image=busybox -- /bin/sh -c "wget -O- --timeout=2 web-server"
    ```
    
4. **Créer une politique "Allow" (**`allow-web-access.yaml`) :
    
    ```yaml
    # allow-web-access.yaml
    apiVersion: networking.k8s.io/v1
    kind: NetworkPolicy
    metadata:
      name: allow-web-access
    spec:
      podSelector:
        matchLabels:
          app: web-server
      policyTypes:
      - Ingress
      ingress:
      - from:
        - podSelector:
            matchLabels:
              access: "true"
        ports:
        - protocol: TCP
          port: 80
    ```
    
    **Appliquer :** `kubectl apply -f allow-web-access.yaml`
    
5. **Tester la politique "Allow" (la connexion réussira) :**
    
    ```bash
    kubectl run tmp-shell --rm -it --labels=access=true --image=busybox -- /bin/sh -c "wget -O- web-server"
    ```
    

### Section 4.5 : CoreDNS

#### **Démo : Personnaliser CoreDNS pour un domaine externe**

1. **Modifier le ConfigMap CoreDNS :**
    
    ```bash
    kubectl edit configmap coredns -n kube-system
    ```
    
2. **Ajouter un nouveau bloc serveur à l'intérieur de la structure de données** `Corefile` (ex: pour [`my-corp.com`](http://my-corp.com)) :
    
    ```yaml
    # ... à l'intérieur de la chaîne data.Corefile...
        my-corp.com:53 {
            errors
            cache 30
            forward . 10.10.0.53 # Transférer vers votre serveur DNS interne
        }
    # ...
    ```
    

---

## Partie 5 : Stockage (10%)

### Section 5.2 : Configuration des volumes

#### **Démo de provisionnement statique**

1. **Créer un PersistentVolume (**`pv.yaml`) :
    
    ```yaml
    # pv.yaml (Utilisation de hostPath pour les tests locaux)
    apiVersion: v1
    kind: PersistentVolume
    metadata:
      name: task-pv-volume
    spec:
      capacity:
        storage: 10Gi
      accessModes:
        - ReadWriteOnce
      persistentVolumeReclaimPolicy: Retain
      storageClassName: manual
      hostPath:
        path: "/mnt/data"
    ```
    
    **Appliquer :** `kubectl apply -f pv.yaml`
    
2. **Créer une PersistentVolumeClaim (**`pvc.yaml`) :
    
    ```yaml
    # pvc.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: task-pv-claim
    spec:
      storageClassName: manual
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 3Gi
    ```
    
    **Appliquer :** `kubectl apply -f pvc.yaml`
    
3. **Vérifier le Binding :**
    
    ```bash
    kubectl get pv,pvc
    ```
    
4. **Créer un Pod qui utilise la PVC (**`pod-storage.yaml`) :
    
    ```yaml
    # pod-storage.yaml
    apiVersion: v1
    kind: Pod
    metadata:
      name: storage-pod
    spec:
      containers:
        - name: nginx
          image: nginx
          volumeMounts:
          - mountPath: "/usr/share/nginx/html"
            name: my-storage
      volumes:
        - name: my-storage
          persistentVolumeClaim:
            claimName: task-pv-claim
    ```
    
    **Appliquer :** `kubectl apply -f pod-storage.yaml`
    

### Section 5.3 : StorageClasses et provisionnement dynamique

#### **Démo : Utiliser une StorageClass par défaut**

1. **Inspecter les StorageClasses disponibles :**
    
    ```bash
    kubectl get storageclass
    ```
    
2. **Créer une PVC sans PV (repose sur une StorageClass par défaut) :**
    
    ```yaml
    # dynamic-pvc.yaml
    apiVersion: v1
    kind: PersistentVolumeClaim
    metadata:
      name: my-dynamic-claim
    spec:
      accessModes:
        - ReadWriteOnce
      resources:
        requests:
          storage: 1Gi
    ```
    
    **Appliquer :** `kubectl apply -f dynamic-pvc.yaml`
    
3. **Observer le provisionnement dynamique :**
    
    ```bash
    kubectl get pv
    ```
    

---

## Partie 6 : Troubleshooting (30%)

### Section 6.2 : Troubleshooting des applications et des Pods

#### **Outils de débogage pour les plantages et les échecs**

1. **Obtenir des informations détaillées sur une ressource (la commande de débogage la plus critique) :**
    
    ```bash
    kubectl describe pod <pod-name>
    ```
    
2. **Vérifier les logs de l'application (pour le conteneur actuel) :**
    
    ```bash
    kubectl logs <pod-name>
    ```
    
3. **Vérifier les logs de l'application (pour l'instance de conteneur précédente ayant planté) :**
    
    ```bash
    kubectl logs <pod-name> --previous
    ```
    
4. **Obtenir un shell à l'intérieur d'un conteneur en cours d'exécution pour un débogage en direct :**
    
    ```bash
    kubectl exec -it <pod-name> -- /bin/sh
    ```
    

### Section 6.3 : Troubleshooting du cluster et des nœuds

1. **Vérifier le statut des nœuds :**
    
    ```bash
    kubectl get nodes
    ```
    
2. **Obtenir des informations détaillées sur un nœud :**
    
    ```bash
    kubectl describe node <node-name>
    ```
    
3. **Voir la capacité des ressources du nœud (pour les problèmes d'ordonnancement) :**
    
    ```bash
    kubectl describe node <node-name> | grep Allocatable
    ```
    
4. **Vérifier le statut du service** `kubelet` (sur le nœud affecté via SSH) :
    
    ```bash
    sudo systemctl status kubelet
    sudo journalctl -u kubelet -f
    ```
    
5. **Réactiver l'ordonnancement sur un nœud cordoned :**
    
    ```bash
    kubectl uncordon <node-name>
    ```
    

### Section 6.5 : Troubleshooting des services et du réseau

1. **Vérifier le Service et les Endpoints (pour les problèmes de connectivité) :**
    
    ```bash
    kubectl describe service <service-name>
    ```
    
2. **Vérifier la résolution DNS depuis un Pod client (depuis le shell du Pod client) :**
    
    ```bash
    kubectl exec -it client-pod -- nslookup <service-name>
    ```
    
3. **Vérifier les Network Policies (pour voir si le trafic est bloqué) :**
    
    ```bash
    kubectl get networkpolicy
    ```
    

### Section 6.6 : Surveillance de l'utilisation des ressources du cluster et des applications

1. **Obtenir l'utilisation des ressources des nœuds (nécessite Metrics Server) :**
    
    ```bash
    kubectl top nodes
    ```
    
2. **Obtenir l'utilisation des ressources des Pods (nécessite Metrics Server) :**
    
    ```bash
    kubectl top pods -n <namespace>
    ```