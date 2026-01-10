---
title: 'Tutoriel sur le réseau Kubernetes : Un guide pour les développeurs'
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2025-06-23T17:31:40.976Z'
originalURL: https://freecodecamp.org/news/kubernetes-networking-tutorial-for-developers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1750697209688/e55bb451-1278-4004-ae3d-fd8bdbae47da.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: networking
  slug: networking
- name: Cloud Computing
  slug: cloud-computing
seo_title: 'Tutoriel sur le réseau Kubernetes : Un guide pour les développeurs'
seo_desc: 'Kubernetes networking is one of the most critical and complex parts of
  running containerized workloads in production. It’s what allows different parts
  of a Kubernetes system – like containers and services – to talk to each other.

  This tutorial will w...'
---

Le réseau Kubernetes est l'une des parties les plus critiques et complexes de l'exécution de charges de travail conteneurisées en production. C'est ce qui permet aux différentes parties d'un système Kubernetes - comme les conteneurs et les services - de communiquer entre elles.

Ce tutoriel vous guidera à travers la théorie ainsi que des exemples pratiques et des meilleures pratiques pour maîtriser le réseau Kubernetes.

## **Prérequis**

* Avoir une compréhension de base des conteneurs et [Docker installé](https://docs.docker.com/engine/install/) sur votre système.

* Compréhension de base des termes généraux de réseau.

* [Installer kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/) pour exécuter des commandes Kubernetes.

* Cluster Kubernetes ([Kind](https://kind.sigs.k8s.io/), [Minikube](https://kubernetes.io/docs/tutorials/kubernetes-basics/create-cluster/cluster-intro/), etc.).

* [Helm installé](https://helm.sh/docs/intro/install/) pour la gestion des packages Kubernetes.

## Table des matières

1. [Introduction au réseau Kubernetes](#heading-introduction-au-reseau-kubernetes)

2. [Concepts de base du réseau Kubernetes](#heading-concepts-de-base-du-reseau-kubernetes)

3. [Composants du réseau de cluster](#heading-composants-du-reseau-de-cluster)

4. [DNS et découverte de service](#heading-dns-et-decouverte-de-service)

5. [Plongée approfondie dans le réseau de pod](#heading-plongee-approfondie-dans-le-reseau-de-pod)

6. [Services et équilibrage de charge](#heading-services-et-equilibrage-de-charge)

7. [Politiques de réseau et sécurité](#heading-politiques-de-reseau-et-securite)

8. [Pièges courants et dépannage](#heading-pieges-courants-et-depannage)

9. [Résumé et prochaines étapes](#heading-resume-et-prochaines-etapes)

## Qu'est-ce que le réseau Kubernetes ?

Alors, qu'est-ce que le réseau dans Kubernetes ? Eh bien, en termes simples, il aide à s'assurer que chaque conteneur peut communiquer avec les autres, même s'ils sont sur des machines différentes. Il garantit également que le trafic externe peut atteindre les bons conteneurs lorsqu'il en a besoin.

Kubernetes abstrait une grande partie de la complexité impliquée dans le réseau, mais comprendre son fonctionnement interne vous aide à optimiser et à dépanner les applications.

Un facteur clé est que chaque pod obtient une adresse IP unique et peut communiquer avec tous les autres pods sans traduction d'adresse réseau (NAT). Ce modèle simple mais puissant supporte des systèmes distribués complexes.

**NAT (Network Address Translation)** fait référence au processus de réécriture de l'adresse IP source ou de destination (et éventuellement du port) des paquets lorsqu'ils passent par un routeur ou une passerelle.

Parce que NAT modifie les en-têtes de paquets, il rompt la transparence "end-to-end" du réseau :

1. L'hôte récepteur voit l'adresse du dispositif NAT au lieu de celle de l'expéditeur d'origine.

2. Les captures de paquets (par exemple, via tcpdump) ne montrent que les adresses traduites, obscurcissant quel point de terminaison interne a réellement envoyé le trafic.

### **Exemple : NAT du routeur Wi-Fi domestique**

Imaginez votre réseau domestique : vous avez un ordinateur portable, un téléphone et une smart TV tous connectés au même Wi-Fi. Votre fournisseur d'accès Internet vous attribue **une adresse IP publique** (par exemple, 203.0.113.5). En interne, votre routeur donne à chaque appareil une **IP privée** (par exemple, 192.168.1.10 pour votre ordinateur portable, 192.168.1.11 pour votre téléphone, etc.).

* **Trafic sortant :** Lorsque votre ordinateur portable (192.168.1.10) demande une page web, le routeur réécrit l'IP source du paquet de 192.168.1.10 → 203.0.113.5 (et suit quel port interne correspond à quel appareil).

* **Trafic entrant :** Lorsque la page web répond, elle arrive à 203.0.113.5, et le routeur utilise sa table NAT pour transmettre ce paquet à 192.168.1.10.

En raison de cette traduction :

1. Les serveurs externes **ne voient que** l'IP du routeur (203.0.113.5), pas celle de votre ordinateur portable.

2. Les paquets sont "masqués" de sorte que plusieurs appareils peuvent partager une seule adresse publique.

En revanche, les pods Kubernetes communiquent **sans** cette couche de traduction supplémentaire - chaque IP de pod est "réelle" au sein du cluster, donc aucune étape de type routeur n'obscurcit qui a parlé à qui.

### Exemple : Microservices de commerce électronique

Considérez une boutique en ligne construite comme des microservices séparés, chacun s'exécutant dans son propre pod avec une IP unique :

* **Service de catalogue de produits :** 10.244.1.2

* **Service de panier d'achat :** 10.244.2.3

* **Service d'authentification des utilisateurs :** 10.244.1.4

* **Service de traitement des paiements :** 10.244.3.5

Lorsque qu'un acheteur ajoute un article à son panier, le pod du panier d'achat contacte directement le pod du catalogue de produits à l'adresse 10.244.1.2. Comme il n'y a pas de NAT ou de proxy externe dans le chemin de données, cette communication est rapide et fiable - ce qui est crucial pour offrir une expérience utilisateur réactive et en temps réel.

**Astuce :** Pour une implémentation complète et pratique de ce scénario (et d'autres), consultez la section "networking-concepts-practice" de mon projet : [Learn-DevOps-by-building | networking-concepts-practice](https://github.com/Caesarsage/Learn-DevOps-by-building/blob/main/intermediate/k8/networking-concepts-practice/README.md)

### Importance dans les systèmes distribués

Le réseau dans les systèmes distribués facilite l'interaction de plusieurs services, permettant aux architectures de microservices de fonctionner efficacement. Un réseau fiable supporte la redondance, la scalabilité et la tolérance aux pannes.

### Principes du modèle de réseau Kubernetes

Le réseau Kubernetes fonctionne sur trois piliers fondamentaux qui créent un environnement réseau cohérent et haute performance :

#### 1. IP unique par pod

Chaque pod reçoit sa propre adresse IP routable, éliminant les conflits de ports et simplifiant la découverte de services. Cette conception traite les pods comme des VM traditionnelles ou des hôtes physiques : chacun peut se lier à des ports standard (par exemple, 80/443) sans remappage.

Cela aide les développeurs à éviter la complexité de la gestion des ports, et les outils (comme la surveillance, le traçage) fonctionnent de manière transparente, puisque les pods apparaissent comme des points de terminaison réseau de premier ordre.

#### 2. Communication entre pods sans NAT :

Les pods communiquent directement sans traduction d'adresse réseau (NAT). Les paquets conservent leurs adresses IP source/destination d'origine, assurant une visibilité de bout en bout. Cela simplifie le débogage (par exemple, `tcpdump` montre les vraies IP des pods) et permet des politiques réseau précises. L'absence de couche de traduction signifie également une latence plus faible et aucun goulot d'étranglement étatique caché.

#### 3. Routage direct entre nœuds et pods :

Les nœuds routent le trafic vers les pods sans passerelles centralisées. Chaque nœud gère les décisions de transfert localement (via les plugins CNI), créant un réseau L3 plat. Cela évite les points de défaillance uniques et optimise les performances - le trafic inter-nœuds circule directement entre les nœuds, sans passer par des proxys. La scalabilité est inhérente, et l'ajout de nœuds étend la capacité de manière linéaire.

### Défis dans le réseau de conteneurs

Les défis courants incluent la gestion des adresses IP dynamiques, la sécurisation des communications et la mise à l'échelle des réseaux sans dégradation des performances. Bien que Kubernetes abstraie les complexités du réseau, les déploiements dans le monde réel font face à des obstacles, comme :

#### Gestion dynamique des IP :

Les pods sont éphémères - les IP changent constamment lors de la mise à l'échelle, des pannes ou des mises à jour. Les IP codées en dur se cassent, et la mise en cache DNS (avec des TTL mal configurés) risque de router vers des points de terminaison obsolètes. Des solutions comme CoreDNS suivent dynamiquement les IP des pods via l'API Kubernetes, tandis que les sondes de disponibilité garantissent que seuls les pods actifs sont annoncés.

#### Communication sécurisée :

La connectivité par défaut des pods à l'échelle du cluster expose des menaces "est-ouest". Les charges de travail compromises peuvent scanner les services internes, et le chiffrement du trafic (par exemple, mTLS) ajoute une surcharge CPU. Les politiques de réseau imposent la segmentation (par exemple, isolant les services conformes PCI), et les maillages de service automatisent le chiffrement sans modifications d'application.

#### Performance à l'échelle :

Les grands clusters sollicitent les outils hérités. Les règles `iptables` explosent avec des milliers de services, ralentissant le traitement des paquets. Les réseaux superposés (par exemple, VXLAN) fragmentent les paquets, et les équilibreurs de charge centralisés créent des goulots d'étranglement. Les CNI modernes (Cilium/eBPF, Calico/BGP) contournent les goulots d'étranglement du noyau, tandis que IPVS remplace `iptables` pour des recherches O(1).

## Concepts de base du réseau Kubernetes

### Qu'est-ce que les pods et les nœuds ?

Les pods sont les plus petites unités déployables. Chaque pod s'exécute sur un nœud, qui peut être une machine virtuelle ou physique.

#### Exemple de scénario : Déploiement d'une application web

Une application web typique pourrait avoir :

* Trois pods frontend exécutant NGINX (distribués sur deux nœuds)

* Cinq pods backend API exécutant Node.js (distribués sur trois nœuds)

* Deux pods de base de données exécutant PostgreSQL (sur des nœuds dédiés avec stockage SSD)

```bash
# Voir les pods distribués sur les nœuds
kubectl get pods -o wide

NAME                        READY   STATUS    NODE
frontend-6f4d85b5c9-1p4z2   1/1     Running   worker-node-1
frontend-6f4d85b5c9-2m5x3   1/1     Running   worker-node-1
frontend-6f4d85b5c9-3n6c4   1/1     Running   worker-node-2
backend-7c8d96b6b8-4q7d5    1/1     Running   worker-node-2
backend-7c8d96b6b8-5r8e6    1/1     Running   worker-node-3
...
```

### Qu'est-ce que les services ?

Les services exposent les pods en utilisant des sélecteurs. Ils fournissent une identité réseau stable même lorsque les IP des pods changent.

```bash
kubectl expose pod nginx-pod --port=80 --target-port=80 --name=nginx-service
```

#### Exemple de scénario : Migration du service de base de données

Une équipe doit migrer sa base de données de MySQL à PostgreSQL sans perturber la fonctionnalité de l'application :

1. Déployer les pods PostgreSQL aux côtés des pods MySQL existants

2. Créer un service de base de données qui sélectionne initialement uniquement les pods MySQL :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: database-service
spec:
  selector:
    app: mysql
  ports:
  - port: 3306
    targetPort: 3306
```

3. Mettre à jour l'application pour qu'elle soit compatible avec les deux bases de données

4. Mettre à jour le sélecteur de service pour inclure à la fois les pods MySQL et PostgreSQL :

```yaml
selector:
  app: database  # Nouveau label appliqué aux pods MySQL et PostgreSQL
```

5. Supprimer progressivement les pods MySQL tandis que le service route le trafic vers les pods PostgreSQL disponibles

L'abstraction de service permet une migration sans temps d'arrêt en fournissant un point de terminaison cohérent tout au long de la transition.

### Chemins de communication

Un **chemin de communication** est simplement l'itinéraire que le trafic réseau emprunte de sa source à sa destination au sein (ou dans/sortant) du cluster. Dans Kubernetes, les trois principaux chemins sont :

* **Pod-à-Pod :** Trafic direct entre deux pods (éventuellement sur différents nœuds).

* **Pod-à-Service :** Trafic d'un pod destiné à un service Kubernetes (qui équilibre ensuite la charge vers l'un de ses pods backend).

* **Externe-à-Service :** Trafic provenant de l'extérieur du cluster (par exemple, d'un utilisateur final ou d'un système externe) dirigé vers un service (souvent via un LoadBalancer ou Ingress).

#### Communication Pod-à-Pod

Les pods communiquent directement entre eux en utilisant leurs adresses IP sans NAT. Par exemple :

```bash
kubectl exec -it pod-a -- ping pod-b
```

#### Exemple de scénario : Journalisation Sidecar

Dans une configuration d'agrégation de logs, chaque pod d'application a un conteneur sidecar qui traite et transfère les logs :

1. Le conteneur d'application écrit les logs dans un volume partagé

2. Le conteneur sidecar lit à partir du volume et transfère vers un service de journalisation central

```bash
# Vérifier la communication entre l'application et le sidecar
kubectl exec -it app-pod -c app -- ls -la /var/log/app
kubectl exec -it app-pod -c log-forwarder -- tail -f /var/log/app/application.log
```

Parce que les deux conteneurs sont dans le même pod, ils peuvent communiquer via [localhost](http://localhost) et des volumes partagés sans aucune configuration réseau.

#### Communication Pod-à-Service

Les pods communiquent avec les services en utilisant des noms DNS, permettant un accès équilibré en charge à plusieurs pods :

```bash
kubectl exec -it pod-a -- curl http://my-service.default.svc.cluster.local
```

#### Exemple de scénario : Modèle de passerelle API

Une architecture de microservices utilise un modèle de passerelle API :

1. Les pods frontend doivent accéder à quinze microservices backend ou plus

2. Au lieu de suivre les IP de pods individuelles, le frontend se connecte aux noms de service :

```javascript
// Code frontend
const authService = 'http://auth-service.default.svc.cluster.local';
const userService = 'http://user-service.default.svc.cluster.local';
const productService = 'http://product-service.default.svc.cluster.local';

async function getUserProducts(userId) {
  const authResponse = await fetch(`${authService}/validate`);
  if (authResponse.ok) {
    const user = await fetch(`${userService}/users/${userId}`);
    const products = await fetch(`${productService}/products?user=${userId}`);
    return { user, products };
  }
}
```

Chaque nom de service se résout en un point de terminaison stable, même lorsque les pods sous-jacents sont mis à l'échelle, remplacés ou reprogrammés.

#### Communication Externe-à-Service

La communication externe est facilitée par des types de service comme NodePort ou LoadBalancer. Un exemple d'utilisation de NodePort :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-nodeport-service
spec:
  type: NodePort
  ports:
  - port: 80
    targetPort: 80
    nodePort: 30080
  selector:
    app: my-app
```

Maintenant, ce service peut être accessible externement via :

```bash
curl http://<NodeIP>:30080
```

#### Exemple de scénario : Application web publique

Une entreprise exécute une application web publique qui nécessite un accès externe :

1. Déployer les pods d'application avec trois répliques

2. Créer un service LoadBalancer pour exposer l'application :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: web-app
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-type: nlb  # Annotation spécifique au cloud
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8080
  selector:
    app: web-app
```

3. Lorsqu'il est déployé sur AWS, cela provisionne automatiquement un Network Load Balancer avec une IP publique

4. Les utilisateurs externes accèdent à l'application via le load balancer, qui distribue le trafic sur les trois pods

```bash
# Vérifier l'IP externe attribuée au service
kubectl get service web-app

NAME     TYPE          CLUSTER-IP     EXTERNAL-IP        PORT(S)
web-app  LoadBalancer  10.100.41.213  a1b2c3.amazonaws.com  80:32456/TCP
```

## Composants du réseau de cluster

Le réseau Kubernetes transforme les principes abstraits en réalité grâce à des composants étroitement orchestrés. Au cœur de cela se trouve le **Container Network Interface (CNI)**, une spécification standardisée qui régit la manière dont la connectivité réseau est établie pour les conteneurs.

### Qu'est-ce qu'une interface réseau de conteneur (CNI) ?

À sa base, CNI agit comme le framework de plugin de réseau de Kubernetes. Il est responsable de l'attribution dynamique des adresses IP aux pods, de la création d'interfaces réseau virtuelles (comme des paires Ethernet virtuelles), et de la configuration des routes chaque fois qu'un pod démarre ou s'arrête.

De manière cruciale, Kubernetes délègue ces opérations de réseau de bas niveau aux plugins CNI, vous permettant de choisir des implémentations alignées sur les besoins de votre environnement : qu'il s'agisse des réseaux superposés simples de Flannel pour la portabilité, du routage BGP haute performance de Calico pour l'efficacité bare-metal, ou du plan de données eBPF de Cilium pour la sécurité avancée et l'observabilité.

Travaillant aux côtés de CNI, kube-proxy fonctionne sur chaque nœud, traduisant les abstractions de Service en règles de routage concrètes au sein du noyau du nœud (en utilisant `iptables` ou `IPVS`). Pendant ce temps, CoreDNS fournit une découverte de service transparente en mappant dynamiquement les noms lisibles par l'homme (par exemple, `cart-service.production.svc.cluster.local`) aux IP de Service stables. Ensemble, ces composants forment un tissu cohésif, garantissant que les pods peuvent communiquer de manière fiable, qu'ils soient sur le même nœud ou distribués sur des clusters globaux.

### **Différences de haut niveau entre les plugins CNI :**

* **Flannel :** Superposition simple (VXLAN, host-gw) pour le réseau multi-hôte de base.

* **Calico :** Routage pur L3 utilisant BGP ou IP-in-IP, plus des politiques réseau riches.

* **Cilium :** Plan de données basé sur eBPF pour un traitement ultra-rapide des paquets et des fonctionnalités avancées comme les politiques sensibles à l'API.

Ces plugins de haut niveau implémentent la norme CNI pour la gestion des IP de pods et le routage.

```bash
kubectl get pods -n kube-system
```

#### Exemple de scénario : Déploiement multi-cloud avec Calico

Une entreprise exploite un déploiement hybride sur AWS et Azure :

1. Choisir Calico comme plugin CNI pour un réseau cohérent entre les clouds :

```bash
# Installer Calico sur les deux clusters
kubectl apply -f https://docs.projectcalico.org/manifests/calico.yaml

# Vérifier que les pods Calico sont en cours d'exécution
kubectl get pods -n kube-system -l k8s-app=calico-node
```

Calico fournit :

* IPAM (gestion des adresses IP) cohérente entre les deux clouds

* Application des politiques réseau dans les deux environnements

* Routage BGP pour un trafic optimisé entre les nœuds

2. Lors de la migration des charges de travail entre les clouds, la couche réseau se comporte de manière cohérente malgré les infrastructures sous-jacentes différentes.

### Qu'est-ce que kube-proxy ?

kube-proxy est un composant réseau qui s'exécute sur chaque nœud et implémente l'abstraction **Service** de Kubernetes. Ses responsabilités incluent :

* **Surveiller le serveur API** pour les changements de Service et d'Endpoints.

* **Programmer la couche de filtrage de paquets du nœud** (iptables ou IPVS) afin que le trafic vers un ClusterIP de Service:port soit équilibré en charge vers l'un de ses pods backend sains.

* **Gérer l'affinité de session**, si configurée (de sorte que les requêtes répétées du même client aillent au même pod).

En faisant cela par nœud, `kube-proxy` garantit que tout pod sur ce nœud peut atteindre n'importe quelle IP de Service sans avoir besoin d'une passerelle centrale.

### Qu'est-ce que iptables et IPVS ?

iptables et IPVS sont tous deux des sous-systèmes du noyau Linux que `kube-proxy` peut utiliser pour gérer le trafic de Service :

#### Mode iptables

`kube-proxy` génère un ensemble de règles NAT (dans la table `nat`) de sorte que lorsqu'un paquet arrive pour une IP de Service, le noyau réécrit sa destination vers l'une des IP de pods backend.

#### Mode IPVS

IPVS (IP Virtual Server) fonctionne comme partie du framework Netfilter du noyau. Au lieu de dizaines ou de centaines de règles iptables, il maintient une table de hachage haute performance de services virtuels et de serveurs réels.

Voici la comparaison des modes `iptables` et `IPVS` dans un format de tableau clair :

| **Mode** | **Avantages** | **Inconvénients** |
| --- | --- | --- |
| **iptables** |  Simple et universellement disponible sur les systèmes Linux |  |
|  Testé en bataille et facile à déboguer |  La complexité des règles croît linéairement avec les Services/Endpoints |  |
|  Le traitement des paquets ralentit à l'échelle en raison des vérifications séquentielles des règles |  |  |
|  Les mises à jour de service déclenchent des rechargements complets des règles |  |  |
| **IPVS** |  Temps de recherche O(1) indépendamment de la taille du cluster |  |
|  Algorithmes d'équilibrage de charge intégrés (RR, LC, SH) |  |  |
|  Mises à jour incrémentielles sans recalcul complet des règles |  |  |
|  Faible surcharge CPU pour les grands clusters |  Nécessite un noyau Linux 4.4 et les modules IPVS chargés |  |
|  Configuration initiale plus complexe |  |  |
|  Visibilité limitée avec les outils traditionnels |  |  |

#### Exemple de scénario : Débogage de la connectivité de service

Lors du dépannage des problèmes de connectivité de service dans un cluster de production :

1. Tout d'abord, vérifier si kube-proxy fonctionne :

```bash
# Vérifier les pods kube-proxy
kubectl get pods -n kube-system -l k8s-app=kube-proxy

# Examiner les logs de kube-proxy
kubectl logs -n kube-system kube-proxy-a1b2c
```

2. Inspecter les règles iptables créées par kube-proxy sur un nœud :

```bash
# Se connecter à un nœud
ssh worker-node-1

# Voir les règles iptables pour un service spécifique
sudo iptables-save | grep my-service
```

3. La sortie révèle comment le trafic vers ClusterIP 10.96.45.10 est équilibré en charge sur plusieurs IP de pods backend :

```bash
-A KUBE-SVC-XYZAB12345 -m comment --comment "default/my-service" -m statistic --mode random --probability 0.33332 -j KUBE-SEP-POD1
-A KUBE-SVC-XYZAB12345 -m comment --comment "default/my-service" -m statistic --mode random --probability 0.50000 -j KUBE-SEP-POD2
-A KUBE-SVC-XYZAB12345 -m comment --comment "default/my-service" -j KUBE-SEP-POD3
```

Comprendre ces règles aide à diagnostiquer pourquoi le trafic pourrait ne pas atteindre certains pods.

## DNS et découverte de service

Chaque service dans Kubernetes repose sur le DNS pour mapper un nom convivial (par exemple, `my-svc.default.svc.cluster.local`) à son ClusterIP. Lorsque les pods apparaissent et disparaissent, les enregistrements DNS doivent être mis à jour rapidement afin que les clients ne rencontrent jamais d'adresses obsolètes.

Kubernetes utilise **CoreDNS** comme serveur DNS de cluster. Lorsque vous créez un Service, un enregistrement A est ajouté pointant vers son ClusterIP. Les Endpoints (les IP des pods) sont publiés comme enregistrements SRV (Service). Si un pod plante ou est reprogrammé, CoreDNS surveille l'API Endpoints et met à jour ses enregistrements en temps quasi réel.

**Mécanismes clés :**

1. **Enregistrement A du Service →** ClusterIP

2. **Enregistrements SRV des Endpoints →** IP et ports des pods backend

3. **Réglage du TTL →** durée pendant laquelle les clients mettent en cache les entrées

**Pourquoi la récupération est importante :**

* Un TTL DNS trop long peut laisser les clients réessayer une ancienne IP.

* Un TTL trop court augmente la charge DNS.

* Les sondes de disponibilité doivent signaler "non prêt" avant que CoreDNS ne supprime l'enregistrement d'un pod.

### CoreDNS

CoreDNS fournit la résolution DNS pour les services à l'intérieur du cluster.

```bash
kubectl exec -it busybox -- nslookup nginx-service
```

La découverte de service est automatique, utilisant :

```bash
<service>.<namespace>.svc.cluster.local
```

#### Exemple de scénario : Variables d'environnement de microservices vs. DNS

Une équipe migre des variables d'environnement codées en dur vers le DNS Kubernetes :

**Avant :** Configuration via variables d'environnement

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: order-service
spec:
  containers:
  - name: order-app
    image: order-service:v1
    env:
    - name: PAYMENT_SERVICE_HOST
      value: "10.100.45.12"
    - name: INVENTORY_SERVICE_HOST
      value: "10.100.67.34"
    - name: USER_SERVICE_HOST
      value: "10.100.23.78"
```

**Après :** Utilisation de la découverte de service DNS Kubernetes

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: order-service
spec:
  containers:
  - name: order-app
    image: order-service:v2
    env:
    - name: PAYMENT_SERVICE_HOST
      value: "payment-service.default.svc.cluster.local"
    - name: INVENTORY_SERVICE_HOST
      value: "inventory-service.default.svc.cluster.local"
    - name: USER_SERVICE_HOST
      value: "user-service.default.svc.cluster.local"
```

Lorsque l'équipe doit déplacer le service de paiement dans un espace de noms dédié pour la conformité PCI :

1. Déplacer le service de paiement vers l'espace de noms "finance"

2. Mettre à jour une seule variable d'environnement :

```yaml
- name: PAYMENT_SERVICE_HOST
  value: "payment-service.finance.svc.cluster.local"
```

3. L'application continue de fonctionner sans reconstruire les images de conteneur ou mettre à jour d'autres services

## Plongée approfondie dans le réseau de pod

Sous le capot, chaque pod a son propre espace de noms réseau, une paire Ethernet virtuelle (`veth`), et une interface comme `eth0`. Le plugin CNI relie ces éléments au tissu du cluster.

Lorsque le kubelet crée un pod, il appelle votre plugin CNI :

* 1. **Alloue une IP** à partir d'un pool.

* 2. **Crée une** paire `veth` et déplace une extrémité dans le netns du pod.

* 3. **Programme les routes** sur l'hôte afin que les autres nœuds sachent comment atteindre cette IP.

### Espaces de noms et Ethernet virtuel

Chaque pod obtient un espace de noms réseau Linux et se connecte à l'hôte via une paire Ethernet virtuelle.

```bash
kubectl exec -it nginx-pod -- ip addr
```

#### Exemple de scénario : Débogage de la connectivité réseau

Lors du dépannage des problèmes de connectivité entre les pods :

1. Examiner les interfaces réseau à l'intérieur d'un pod :

```bash
kubectl exec -it web-frontend-pod -- ip addr

1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN group default qlen 1000
    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
    inet 127.0.0.1/8 scope host lo
    inet6 ::1/128 scope host
2: eth0@if18: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1450 qdisc noqueue state UP group default
    link/ether 82:cf:d8:e9:7a:12 brd ff:ff:ff:ff:ff:ff link-netnsid 0
    inet 10.244.2.45/24 scope global eth0
    inet6 fe80::80cf:d8ff:fee9:7a12/64 scope link
```

2. Tracer le chemin du pod au nœud :

```bash
# Sur le nœud hébergeant le pod
sudo ip netns list
# Affiche l'espace de noms comme : cni-1a2b3c4d-e5f6-7890-a1b2-c3d4e5f6g7h8

# Examiner les connexions sur le nœud
sudo ip link | grep veth
# Affiche les paires Ethernet virtuelles comme : veth123456@if2: ...

# Vérifier les routes sur le nœud
sudo ip route | grep 10.244.2.45
# Affiche comment le trafic atteint le pod
```

Cette investigation révèle comment le trafic circule du pod à travers son espace de noms, via des paires Ethernet virtuelles, puis à travers la table de routage du nœud pour atteindre d'autres pods.

### Réseau partagé dans les pods multi-conteneurs

Les pods multi-conteneurs partagent le même espace de noms réseau. Utilisez cela pour les conteneurs sidecar et helpers.

#### Exemple de scénario : Sidecar de service mesh

Lors de l'implémentation d'Istio service mesh avec injection automatique de sidecar :

1. Déployer une application avec l'injection de sidecar Istio activée :

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: api-service
  annotations:
    sidecar.istio.io/inject: "true"
spec:
  containers:
  - name: api-app
    image: api-service:v1
    ports:
    - containerPort: 8080
```

2. Après le déploiement, le pod a deux conteneurs partageant le même espace de noms réseau :

```bash
kubectl describe pod api-service

Name:         api-service
...
Containers:
  api-app:
    ...
    Ports:          8080/TCP
    ...
  istio-proxy:
    ...
    Ports:          15000/TCP, 15001/TCP, 15006/TCP, 15008/TCP
    ...
```

3. Le conteneur sidecar intercepte tout le trafic réseau :

```bash
kubectl exec -it api-service -c istio-proxy -- netstat -tulpn

Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address     Foreign Address     State       PID/Program name
tcp        0      0 0.0.0.0:15001     0.0.0.0:*           LISTEN      1/envoy
tcp        0      0 0.0.0.0:15006     0.0.0.0:*           LISTEN      1/envoy
```

4. Le trafic vers le conteneur d'application est intercepté de manière transparente sans nécessiter de modifications de l'application :

```bash
kubectl exec -it api-service -c api-app -- curl localhost:8080
# Passe en réalité par le proxy même si cela semble direct pour l'application
```

Cet espace de noms réseau partagé permet au service mesh d'implémenter des fonctionnalités comme le chiffrement du trafic, le routage et la collecte de métriques sans modifications de l'application.

## Services et équilibrage de charge

Les services Kubernetes abstraient un ensemble de pods derrière une seule IP virtuelle. Cette IP virtuelle peut être exposée de plusieurs manières :

Un objet Service définit une IP stable (ClusterIP), une entrée DNS et un sélecteur. kube-proxy programme ensuite le nœud pour intercepter le trafic vers cette IP et le transmettre à l'un des pods.

### **Types de services :**

* **ClusterIP (par défaut) :** interne uniquement

* **NodePort :** ouvre le Service sur le port de chaque nœud (par exemple, `30080`)

* **LoadBalancer :** demande à votre fournisseur de cloud un LB externe

* **ExternalName :** CNAME vers un nom DNS externe

### **Mécanismes d'équilibrage de charge :**

* **kube-proxy + iptables/IPVS** (round-robin, least-conn)

* **Ingress externe** (NGINX, Traefik) pour HTTP/S avec routage hôte/chemin

###  Types de services

| Type | Description |
| --- | --- |
| ClusterIP | Par défaut, interne uniquement |
| NodePort | Expose le service sur l'IP du nœud |
| LoadBalancer | Utilise le LB du fournisseur de cloud |
| ExternalName | Alias DNS pour un service externe |

#### Exemple de scénario : Exposition d'une application multi-niveaux

Une entreprise exécute une application web à trois niveaux avec différentes exigences d'exposition :

1. Niveau web frontend (public) :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: frontend-service
  annotations:
    service.beta.kubernetes.io/aws-load-balancer-ssl-cert: "arn:aws:acm:region:account:certificate/cert-id"
spec:
  type: LoadBalancer
  ports:
  - port: 443
    targetPort: 8080
  selector:
    app: frontend
```

2. Niveau API (interne au frontend uniquement) :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: api-service
spec:
  type: ClusterIP  # Interne uniquement
  ports:
  - port: 80
    targetPort: 8000
  selector:
    app: api
```

3. Niveau de base de données (interne à l'API uniquement) :

```yaml
apiVersion: v1
kind: Service
metadata:
  name: db-service
spec:
  type: ClusterIP
  ports:
  - port: 5432
    targetPort: 5432
  selector:
    app: database
```

Cette configuration crée une architecture sécurisée où :

* Seul le frontend est exposé à Internet (avec TLS)

* L'API est uniquement accessible depuis les pods frontend au sein du cluster

* La base de données est uniquement accessible depuis les pods API au sein du cluster

### Contrôleurs d'ingress

Ingress fournit le routage HTTP(S) et la terminaison TLS.

```bash
helm install my-ingress ingress-nginx/ingress-nginx
```

#### Exemple de scénario : Hébergement de plusieurs applications sur un seul domaine

Une entreprise héberge plusieurs applications de microservices sous le même domaine avec différents chemins :

1. Déployer le contrôleur nginx-ingress :

```bash
helm install nginx-ingress ingress-nginx/ingress-nginx --set controller.publishService.enabled=true
```

2. Configurer le routage pour plusieurs services :

```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: company-apps
  annotations:
    kubernetes.io/ingress.class: nginx
    cert-manager.io/cluster-issuer: letsencrypt-prod
spec:
  tls:
  - hosts:
    - services.company.com
    secretName: company-tls
  rules:
  - host: services.company.com
    http:
      paths:
      - path: /dashboard
        pathType: Prefix
        backend:
          service:
            name: dashboard-service
            port:
              number: 80
      - path: /api
        pathType: Prefix
        backend:
          service:
            name: api-gateway
            port:
              number: 80
      - path: /docs
        pathType: Prefix
        backend:
          service:
            name: documentation-service
            port:
              number: 80
```

3. Flux de trafic utilisateur :

* L'utilisateur visite [https://services.company.com/dashboard](https://services.company.com/dashboard)

* Le trafic atteint le service LoadBalancer pour le contrôleur d'ingress

* Le contrôleur d'ingress route vers le dashboard-service en fonction du chemin

* Le service dashboard équilibre la charge sur les pods dashboard

Cela permet d'héberger plusieurs applications derrière un seul domaine et un certificat TLS.

## Politiques de réseau et sécurité

Les politiques de réseau restreignent la communication en fonction des sélecteurs de pods et des espaces de noms.

```yaml
policyTypes:
- Ingress

matchLabels:
  app: frontend
```

### Cas d'utilisation

* Isoler les environnements (par exemple, dev vs prod)

* Contrôler l'egress vers Internet

* Imposer un réseau zero-trust

#### Exemple de scénario : Conformité PCI pour le traitement des paiements

Une application financière traite les paiements par carte de crédit et doit se conformer aux exigences PCI DSS :

1. Créer un espace de noms dédié avec une isolation stricte :

```bash
kubectl create namespace payment-processing
```

2. Déployer les pods de paiement dans l'espace de noms isolé :

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: payment-processor
  namespace: payment-processing
spec:
  replicas: 3
  selector:
    matchLabels:
      app: payment
  template:
    metadata:
      labels:
        app: payment
        pci: "true"
    spec:
      containers:
      - name: payment-app
        image: payment-processor:v1
        ports:
        - containerPort: 8080
```

3. Définir une politique de réseau qui :

* N'autorise le trafic que depuis les services autorisés

* Bloque tout egress sauf vers des API spécifiques

* Surveille et journalise toutes les tentatives de connexion

```yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: pci-payment-policy
  namespace: payment-processing
spec:
  podSelector:
    matchLabels:
      pci: "true"
  policyTypes:
  - Ingress
  - Egress
  ingress:
  - from:
    - namespaceSelector:
        matchLabels:
          environment: production
    - podSelector:
        matchLabels:
          role: checkout
    ports:
    - protocol: TCP
      port: 8080
  egress:
  - to:
    - ipBlock:
        cidr: 192.168.5.0/24  # API de la passerelle de paiement
    ports:
    - protocol: TCP
      port: 443
  - to:
    - namespaceSelector:
        matchLabels:
          name: logging
    ports:
    - protocol: TCP
      port: 8125  # Port des métriques
```

4. Valider la politique avec des tests de connectivité :

```bash
# Test depuis un pod autorisé (devrait réussir)
kubectl exec -it -n production checkout-pod -- curl payment-processor.payment-processing.svc.cluster.local:8080

# Test depuis un pod non autorisé (devrait échouer)
kubectl exec -it -n default test-pod -- curl payment-processor.payment-processing.svc.cluster.local:8080
```

Cette politique de réseau complète garantit que les données de paiement sensibles sont isolées et ne peuvent être accessibles que par des services autorisés.

## Pièges courants et dépannage

### Pod non accessible

* **Symptôme :** `ping` ou le trafic de l'application expire.

* **Étapes pour le dépannage :**

1. **Vérifier l'état et les logs du pod :**

```bash
kubectl get pod myapp-abc123 -o wide
kubectl logs myapp-abc123
```

2. **Inspecter les logs du plugin CNI :**

```bash
# par exemple, pour Calico sur kube-system :
kubectl -n kube-system logs ds/calico-node
```

3. **Exécuter un conteneur de débogage réseau (netshoot) :**

```bash
kubectl run -it --rm netshoot --image=nicolaka/netshoot -- bash
# à l'intérieur de netshoot :
ping <pod-IP>
ip link show
ip route show
```

* **Pourquoi les pods peuvent être inaccessibles :** Échecs d'allocation d'IP, configuration incorrecte de `veth`, incompatibilité MTU, erreurs d'initialisation CNI.

### Service inaccessible

* **Symptôme :** Les clients ne peuvent pas atteindre l'IP du Service, ou `curl` vers `ClusterIP:port` échoue.

* **Étapes pour le dépannage :**

1. **Vérifier le Service et les Endpoints :**

```bash
kubectl get svc my-svc -o yaml
kubectl get endpoints my-svc -o wide
```

2. **Inspecter les règles kube-proxy :**

```bash
# mode iptables :
sudo iptables-save | grep <ClusterIP>
# mode IPVS :
sudo ipvsadm -Ln
```

3. **Tester la connectivité depuis un pod :**

```bash
kubectl exec -it netshoot -- curl -v http://<ClusterIP>:<port>
```

* **Pourquoi les services échouent :** Endpoints manquants (incompatibilité de sélecteur), règles kube-proxy obsolètes, entrées DNS pointant vers la mauvaise IP.

### Trafic bloqué par la politique

* **Symptôme :** Les connexions sont activement refusées ou immédiatement réinitialisées.

* **Étapes pour le dépannage :**

1. **Lister les NetworkPolicies dans l'espace de noms :**

```bash
kubectl get netpol
```

2. **Décrire la logique de la politique :**

```bash
kubectl describe netpol allow-frontend
```

3. **Simuler les flux autorisés vs. bloqués :**

```bash
# Depuis un pod de débogage :
kubectl exec -it netshoot -- \
  curl --connect-timeout 2 http://<target-pod-IP>:<port>
```

* **Pourquoi les politiques vous posent problème :** Comportement "deny" par défaut dans certains plugins CNI, sélecteur de pod ou namespaceSelector trop strict, règles egress manquantes.

###  Outils que vous pouvez utiliser :

* **kubectl exec :** Exécuter des commandes arbitraires **à l'intérieur de n'importe quel pod**. C'est idéal pour exécuter `ping`, `curl`, `ip`, ou `tcpdump` depuis l'espace de noms réseau du pod.

* **tcpdump :** Capturer des paquets bruts sur une interface. Utilisez-le (à l'intérieur de netshoot ou via `kubectl exec`) pour voir si le trafic quitte/arrive réellement à un pod.

* **Netshoot :** Une image de pod utilitaire remplie d'outils réseau (`ping`, `traceroute`, `dig`, `curl`, `tcpdump`, etc.) afin que vous n'ayez pas à construire le vôtre.

* **Cilium Hubble :** Une interface utilisateur/API d'observabilité pour **Cilium** qui montre les flux par connexion, les métadonnées L4/L7 et les verdicts de politique en temps réel.

* **Calico Flow Logs :** Journalisation basée sur **eBPF** de Calico des décisions d'autorisation/refus et des métadonnées de paquets. C'est idéal pour auditer exactement quelle règle de politique a correspondu à un paquet donné.

#### Exemple de scénario : Dépannage des problèmes de connexion de service

Une équipe rencontre des échecs de connexion intermittents à un service de base de données :

1. Vérifier si le service existe et a des endpoints :

```bash
kubectl get service postgres-db
NAME         TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
postgres-db  ClusterIP   10.96.145.232   <none>        5432/TCP   3d

kubectl get endpoints postgres-db
NAME         ENDPOINTS                                   AGE
postgres-db  <none>                                      3d
```

2. Le service existe mais n'a pas d'endpoints. Vérifier les sélecteurs de pod :

```bash
kubectl describe service postgres-db
Name:              postgres-db
Namespace:         default
Selector:          app=postgres,tier=db
...

kubectl get pods --selector=app=postgres,tier=db
No resources found in default namespace.
```

3. Inspecter les pods de base de données :

```bash
kubectl get pods -l app=postgres
NAME                        READY   STATUS    RESTARTS   AGE
postgres-6b4f87b5c9-8p7x2   1/1     Running   0          3d

kubectl describe pod postgres-6b4f87b5c9-8p7x2
...
Labels:       app=postgres
              pod-template-hash=6b4f87b5c9
...
```

4. Problème trouvé : Le pod a l'étiquette `app=postgres` mais manque l'étiquette `tier=db` requise par le sélecteur de service.

5. Corriger en mettant à jour le sélecteur de service :

```bash
kubectl patch service postgres-db -p '{"spec":{"selector":{"app":"postgres"}}}'
```

6. Vérifier que les endpoints sont maintenant peuplés :

```bash
kubectl get endpoints postgres-db
NAME         ENDPOINTS             AGE
postgres-db  10.244.2.45:5432      3d
```

Cette approche de débogage systématique a rapidement identifié une incompatibilité d'étiquette causant les problèmes de connexion.

## Résumé

Dans ce tutoriel, vous avez exploré :

* La communication entre pods et services

* Le routage et la découverte à l'échelle du cluster

* L'équilibrage de charge et l'ingress

* La configuration des politiques de réseau

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).

Pour plus de projets pratiques, suivez et étoilez ce dépôt : [Learn-DevOps-by-building | networking-concepts-practice](https://github.com/Caesarsage/Learn-DevOps-by-building/blob/main/intermediate/k8/networking-concepts-practice/README.md)