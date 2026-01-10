---
title: Comment configurer une politique de réseau Kubernetes et sécuriser votre cluster
subtitle: ''
author: Eti Ijeoma
co_authors: []
series: null
date: '2025-02-18T14:45:59.661Z'
originalURL: https://freecodecamp.org/news/set-up-kubernetes-network-policy-and-secure-your-cluster
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1739889943803/796d97e8-a1c9-41e4-a678-61477514c020.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: containers
  slug: containers
- name: clusters
  slug: clusters
- name: AWS
  slug: aws
seo_title: Comment configurer une politique de réseau Kubernetes et sécuriser votre
  cluster
seo_desc: In a Kubernetes environment, proper networking allows for seamless communication
  between various components within the cluster and the external environment. As your
  applications grow, networking becomes more and more important and helps ensure that
  t...
---

Dans un environnement Kubernetes, une configuration réseau appropriée permet une communication transparente entre les différents composants au sein du cluster et l'environnement externe. À mesure que vos applications se développent, le réseau devient de plus en plus important et aide à garantir que l'application est suffisamment scalable et sécurisée pour répondre aux demandes de vos utilisateurs.

Le réseau Kubernetes vous aide à gérer la manière dont les pods, les services et d'autres entités externes interagissent dans cet environnement pour assurer une connectivité, une isolation et une distribution de charge appropriées lorsque cela est nécessaire. Il offre un système de réseau flexible mais sophistiqué qui met en œuvre des contrôles de sécurité granulaires grâce aux politiques de réseau.

Une caractéristique unique de Kubernetes est qu'il vous permet de déployer et de gérer plusieurs applications à grande échelle au sein d'un seul cluster. Cela vous aide à gérer les ressources de manière efficace et optimise les coûts lorsque vos applications s'exécutent. Mais cela introduit également des défis liés à l'isolation des ressources et à la sécurité. C'est là que la configuration réseau appropriée de Kubernetes devient essentielle.

Dans cet article, nous discuterons des fondamentaux du réseau Kubernetes et de la manière dont il facilite les connexions sécurisées au sein d'un cluster. Nous explorerons également les politiques de réseau en tant que mécanisme pour définir des règles qui régulent la communication entre pods et entre pods et entités externes, assurant un contrôle granulaire sur le flux de trafic au sein du cluster.

### **Voici ce que nous allons couvrir :**

1. [Décomposition des types de connectivité réseau](#heading-decomposition-des-types-de-connectivite-reseau)

2. [Qu'est-ce que les politiques de réseau Kubernetes ?](#heading-quest-ce-que-les-politiques-de-reseau-kubernetes)

   * [Comment fonctionnent les politiques de réseau Kubernetes](#heading-comment-fonctionnent-les-politiques-de-reseau-kubernetes)

   * [Comment implémenter les politiques de réseau](#heading-comment-implementer-les-politiques-de-reseau)

3. [Comment configurer une politique de réseau Kubernetes simple sur EKS](#heading-comment-configurer-une-politique-de-reseau-kubernetes-simple-sur-eks)

4. [Quand et pourquoi utiliser les politiques de réseau Kubernetes](#heading-quand-et-pourquoi-utiliser-les-politiques-de-reseau-kubernetes)

5. [Bonnes pratiques pour implémenter les politiques de réseau Kubernetes sur votre cluster](#heading-bonnes-pratiques-pour-implementer-les-politiques-de-reseau-kubernetes-sur-votre-cluster)

## **Décomposition des types de connectivité réseau**

Le réseau Kubernetes est conçu pour atteindre quatre objectifs importants au sein de l'environnement Kubernetes afin d'assurer le fonctionnement transparent d'un cluster Kubernetes. Ces objectifs sont définis pour garantir une communication appropriée entre les conteneurs, les pods et les entités externes, leur permettant de travailler ensemble efficacement au sein de l'infrastructure Kubernetes.

### **Communication entre conteneurs**

L'un des objectifs de la mise en œuvre d'un réseau Kubernetes approprié est de permettre aux conteneurs au sein du même pod de communiquer directement entre eux. Le partage du même espace de noms réseau permet à ces conteneurs d'interagir les uns avec les autres en utilisant localhost, résultant en une communication à faible latence qui aide les applications multi-conteneurs à fonctionner correctement.

La communication entre conteneurs est utile lorsque l'on travaille avec des charges de travail ayant des processus étroitement couplés et nécessitant une communication rapide sans latence au sein d'un seul pod.

### **Connectivité entre pods**

Au sein d'un environnement Kubernetes, les pods se voient attribuer des adresses IP uniques, rendant la communication entre pods simple et directe. Comprenant le réseau traditionnel entre serveurs, Kubernetes élimine la complexité de la traduction d'adresses réseau (NAT), permettant aux pods de communiquer avec facilité.

La communication entre pods est le fondement de l'architecture des microservices, permettant à chaque pod de fonctionner indépendamment tout en restant connecté aux autres.

### **Interaction entre pods et services**

Les services dans Kubernetes sont souvent décrits comme des points de terminaison stables qui aident les pods à accéder les uns aux autres. Ils garantissent que le trafic est acheminé vers le bon pod, indépendamment de la complexité de la configuration du pod. La communication entre services et pods est généralement fiable, en particulier dans les environnements où le trafic et les configurations des pods évoluent constamment.

### **Accès externe à interne**

L'un des objectifs du réseau Kubernetes est également de gérer le trafic provenant de l'extérieur du cluster. Il existe plusieurs outils, comme les contrôleurs d'entrée (Ingress Controllers) et les équilibreurs de charge (LoadBalancers), qui aident à gérer la communication externe à interne. Ces outils aident à garantir que la bonne application est exposée aux utilisateurs finaux, assurant la livraison appropriée des services.

Bien que le réseau Kubernetes réponde aux exigences de ces objectifs, la communication est généralement ouverte par défaut. Cela signifie que les pods au sein d'un cluster peuvent communiquer librement entre eux sans aucune restriction. Ce n'est pas idéal, en particulier dans un environnement de production où l'isolation et la sécurité sont importantes. C'est là que les politiques de réseau Kubernetes entrent en jeu.

## **Qu'est-ce que les politiques de réseau Kubernetes ?**

Les politiques de réseau Kubernetes vous donnent un moyen d'appliquer un contrôle granulaire sur le flux de trafic au sein de vos pods. Ces politiques vous permettent de définir quels pods peuvent communiquer entre eux ou avec d'autres appareils – elles agissent donc comme une couche de sécurité avec des règles qui restreignent ou autorisent certains types de trafic.

Par exemple, si certains pods gèrent des données ou des informations sensibles, les politiques de réseau peuvent garantir que seuls les pods ou systèmes externes autorisés peuvent y accéder.

La mise en œuvre de politiques de réseau aide également vos clusters Kubernetes à maintenir la sécurité et la conformité en restreignant les communications inutiles et en réduisant le flux de trafic qui pourrait causer une faille de sécurité.

### Comment fonctionnent les politiques de réseau Kubernetes

Les politiques de réseau Kubernetes fournissent un contrôle d'accès granulaire au sein du cluster Kubernetes pour gérer le trafic réseau au niveau des pods. Ici, vous pouvez définir des règles séparées pour l'entrée (ingress) et la sortie (egress) et restreindre le trafic à une plage de ports particulière.

Dans les politiques de réseau Kubernetes, plusieurs politiques peuvent cibler le même pod. Dans ce cas, vous pouvez créer des règles "autoriser" pour déterminer quel trafic est permis. Tout trafic qui ne correspond pas à la règle "autoriser" sera bloqué.

Les politiques de réseau utilisent des adresses IP et des numéros de port pour réguler le trafic. Cela fournit un contrôle sur les flux réseau pour se conformer à des exigences de sécurité spécifiques.

D'un autre côté, les politiques de réseau ne constituent pas une solution complète au sein d'un environnement en raison de certaines limitations. Elles ne peuvent pas journaliser les événements de trafic bloqué, ce qui signifie que vous ne pouvez pas observer ou déboguer pourquoi et quand la politique de réseau Kubernetes bloque un trafic spécifique. Pour y parvenir, vous devez utiliser des outils externes pris en charge par votre plugin CNI.

CNI signifie Container Network Interface, une interface standard utilisée par Kubernetes pour gérer les ressources réseau dans les conteneurs. Le plugin CNI est essentiel pour fournir des capacités de réseau de conteneurs telles que l'allocation d'adresses IP, le routage et l'application des politiques de réseau. Le plugin permet également au cluster de gérer le réseau des pods, y compris l'attribution de politiques de réseau aux pods et la gestion du flux de trafic entre eux.

Certains plugins réseau populaires incluent Calico, Cilium, Flannel et Weave Net, chacun offrant des fonctionnalités uniques et une prise en charge de l'intégration des politiques de réseau.

### **Comment implémenter les politiques de réseau**

La mise en œuvre correcte des politiques de réseau dépend du plugin CNI que vous utilisez dans le cluster Kubernetes. Pour que les politiques de réseau prennent effet, le plugin CNI configuré sur votre cluster doit les prendre en charge.

Les politiques de réseau sont généralement activées par défaut dans les services Kubernetes gérés fournis par les plateformes cloud telles qu'Amazon EKS, Microsoft Azure AKS ou Google Cloud GKE. Mais si vous gérez votre propre cluster, vous devez vous assurer que votre plugin CNI est compatible. Par exemple, le plugin CNI populaire Flannel ne prend pas en charge les politiques de réseau, alors que Calico le fait.

## **Comment configurer une politique de réseau Kubernetes simple sur EKS**

### **Prérequis**

Assurez-vous d'avoir installé les éléments suivants sur votre serveur Ubuntu :

* #### `AWS CLI` : Pour l'authentification et les interactions avec les ressources AWS

* #### `kubectl` : CLI Kubernetes

* #### `eksctl` : Il s'agit d'un CLI pour gérer les clusters EKS

### **Étapes**

Tout d'abord, créez votre cluster AWS EKS en utilisant les commandes CLI suivantes :

```bash
eksctl create cluster \

  --name my-eks-cluster \

  --region us-east-1 \

  --nodegroup-name ng-eks \

  --node-type t3.medium \

  --nodes 3 \

  --nodes-min 2 \

  --nodes-max 4 \

  --with-oidc \

  --version 1.31
```

Ensuite, activez le plugin Amazon VPC CNI pour votre cluster Kubernetes. Pour ce faire, au sein de votre cluster EKS, assurez-vous que le plugin Amazon VPC CNI est installé pour gérer le réseau des pods.

Vérifiez le statut comme suit :

```bash
kubectl get pods -n kube-system | grep aws-node
```

S'il ne s'exécute pas, déployez-le ou mettez-le à jour pour qu'il s'exécute sur le cluster

```bash
kubectl apply -f https://raw.githubusercontent.com/aws/amazon-vpc-cni-k8s/master/config/v1.12/aws-k8s-cni.yaml
```

Amazon VPC CNI ne prend pas en charge et n'applique pas les politiques de réseau. Nous devons donc installer Calico, qui est un CNI qui fonctionne avec le VPC CNI pour les politiques de réseau.

```bash
kubectl apply -f https://raw.githubusercontent.com/projectcalico/calico/v3.25.0/manifests/calico.yaml
```

Confirmez que Calico est installé et en cours d'exécution comme suit :

```bash
kubectl get pods -n kube-system | grep calico
```

Maintenant que nous avons configuré Calico sur notre cluster AWS EKS, examinons diverses politiques de réseau Kubernetes que nous pouvons lui appliquer.

### Autoriser tout le trafic vers un pod spécifique dans le cluster :

```bash
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: pod-network-policy

spec:

  podSelector:

    matchLabels:

      app: application-demo

  policyTypes:

    - Ingress

    - Egress

  ingress:

    - {}

  egress:

    - {}
```

Cette configuration définit une NetworkPolicy nommée `pod-network-policy` qui s'applique à tous les pods avec le label `app: application-demo`. Le `podSelector` garantit que seuls les pods avec ce label sont ciblés.

* Le champ `policyTypes` indique que cette politique contrôle à la fois **Ingress** (trafic entrant) et **Egress** (trafic sortant).

* Les règles `ingress` et `egress` sont définies avec des accolades vides `{}`, ce qui signifie qu'aucune restriction n'est appliquée—tout le trafic est autorisé, à la fois entrant et sortant.

### Refuser tout le trafic vers un pod dans le cluster :

```bash

apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: pod-network-policy
spec:
  podSelector:
    matchLabels:
      app: application-demo
  policyTypes:
    - Ingress
    - Egress
```

Cette configuration sélectionne également les pods étiquetés `app: application-demo` et applique la politique à la fois au trafic Ingress et Egress.

Puisqu'aucune règle spécifique n'est définie, Kubernetes refuse tout le trafic par défaut. Cela est également connu sous le nom de politique "refuser par défaut", utilisée pour imposer une isolation stricte, empêchant les pods de communiquer avec d'autres sauf si explicitement autorisé par des politiques supplémentaires.

### Refuser tout le trafic ingress vers les pods dans le cluster

```bash
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  name: pod-network-policy
spec:
  podSelector: {}
  policyTypes:
    - Ingress
```

Cette configuration applique une NetworkPolicy à tous les pods dans le namespace.

* Le `podSelector` est vide (`{}`), ce qui signifie qu'il s'applique à tous les pods dans le namespace, indépendamment de leurs labels.

* Le champ `policyTypes` spécifie que la politique ne s'applique qu'au trafic Ingress.

* Puisqu'aucune règle Ingress explicite n'est définie, Kubernetes bloque tout le trafic entrant par défaut.

### Refuser tout le trafic egress vers les pods dans le cluster

```bash
apiVersion: networking.k8s.io/v1

kind: NetworkPolicy

metadata:

  name: pod-network-policy

spec:

  podSelector: {}

  policyTypes:

    - Egress
```

Dans la configuration ci-dessus :

* Le `podSelector` est vide (`{}`), ce qui signifie que la politique s'applique à tous les pods dans le namespace.

* Le champ `policyTypes` spécifie que cette politique ne s'applique qu'au trafic Egress.

* Puisqu'aucune règle Egress explicite n'est définie, Kubernetes bloque tout le trafic sortant pour les pods cibles par défaut.

## Quand et pourquoi utiliser les politiques de réseau Kubernetes

Il existe divers cas d'utilisation pour la mise en œuvre de politiques de réseau Kubernetes afin d'améliorer la sécurité du cluster.

Par exemple, peut-être souhaitez-vous restreindre qui/quoi peut accéder à la base de données. Si vous avez une base de données déployée au sein du cluster, les politiques de réseau Kubernetes garantissent que seuls les pods autorisés peuvent communiquer avec elle, bloquant l'accès depuis des applications non autorisées au sein du cluster.

Ou peut-être souhaitez-vous isoler des pods sensibles. La mise en œuvre correcte des politiques de réseau aide à isoler les pods sensibles qui n'ont pas besoin d'accepter le trafic entrant depuis d'autres pods, renforçant la sécurité au sein de l'infrastructure.

## **Bonnes pratiques pour implémenter les politiques de réseau Kubernetes sur votre cluster**

Pour maximiser l'efficacité et les avantages de sécurité de vos politiques de réseau Kubernetes, gardez ces bonnes pratiques à l'esprit :

* **Assurez-vous que tous les pods sont couverts par une politique de réseau :** Dans un environnement de production idéal, tous les pods au sein du cluster doivent être couverts par une politique de réseau qui limite leur réseau aux seules cibles Ingress et Egress définies dans la configuration. Sans cette politique en place, tous les pods peuvent communiquer librement, posant un énorme risque de sécurité.

* **Complétez les politiques de réseau avec d'autres mesures de sécurité** : Bien que les politiques de réseau soient essentielles pour l'isolation du réseau, elles doivent faire partie d'une stratégie de sécurité et de réseau plus large pour votre cluster. Des sauvegardes supplémentaires doivent inclure le contrôle d'accès basé sur les rôles (RBAC), qui restreint l'accès ou la modification des configurations des pods par des utilisateurs non autorisés, et des contextes de sécurité avancés, qui limitent les capacités des conteneurs.

* **Testez toujours les politiques de réseau avant de les déployer en production.** Les politiques de réseau Kubernetes peuvent être un peu fastidieuses à valider, en particulier dans un environnement de production, car elles peuvent entraver de nombreux processus en cours au sein du cluster. Testez toujours les nouvelles politiques pour vous assurer qu'elles fonctionnent comme prévu au sein du cluster. Par exemple, si vous implémentez une nouvelle politique de test, utilisez des outils comme curl ou ping pour vérifier la connectivité bloquée au sein du cluster.

* **Revoyez toujours vos politiques de réseau à mesure que le cluster grandit.** À mesure que votre cluster grandit avec une base d'utilisateurs croissante et des besoins techniques, vos politiques de réseau doivent toujours refléter les nouvelles charges de travail, telles que les pods et les namespaces. Il est toujours préférable de revoir et de mettre à jour vos politiques de réseau pour rester pertinentes et garantir que votre environnement est sécurisé.

* **Utilisez des sélecteurs de cibles précis pour les configurations :** Soyez spécifique lorsque vous définissez les sélecteurs de pods, les namespaces et les plages ipBlock au sein de vos politiques de réseau. Par exemple, si vous travaillez avec des sélecteurs de namespace, assurez-vous que tous les pods au sein de ce namespace se conformen à ses objectifs de sécurité. Évitez d'utiliser des sélecteurs de namespace si vous devez déployer des pods qui doivent communiquer avec d'autres pods dans le namespace. Cela est idéal car l'implémentation vague de sélecteurs de namespace ou de pods aura un impact sur le serveur, conduisant à un accès non intentionnel.

## **Conclusion**

Dans cet article, vous avez appris les politiques de réseau Kubernetes comme moyen de gérer et de restreindre la communication entre les pods. Puisque les pods n'ont pas d'isolation réseau par défaut, la configuration des bonnes politiques est importante pour la sécurité.

Bien que les politiques de réseau jouent un rôle important, il est également important de protéger votre environnement cloud en vous assurant que votre infrastructure est renforcée – assurez-vous donc de mettre en œuvre le RBAC et des analyses régulières de vulnérabilités. Vous devez également allouer uniquement les ressources de pods nécessaires, construire des images de base minimales pour les pods et suivre les bonnes pratiques de sécurité Kubernetes en général.

En faisant cela, vous pouvez obtenir une protection de bout en bout pour vos charges de travail.