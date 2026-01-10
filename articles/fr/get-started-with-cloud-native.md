---
title: Qu'est-ce que le Cloud Native ? Le modèle de livraison du cloud computing expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-19T18:12:13.000Z'
originalURL: https://freecodecamp.org/news/get-started-with-cloud-native
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/GettingStartedWithCloudNative.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Cloud Services
  slug: cloud-services
- name: Kubernetes
  slug: kubernetes
seo_title: Qu'est-ce que le Cloud Native ? Le modèle de livraison du cloud computing
  expliqué
seo_desc: "By Edidiong Asikpo\nWhenever I heard of the term “Cloud native”, my thoughts\
  \ would usually go to Kubernetes. I used to think “Cloud native” was a phrase used\
  \ for describing just Kubernetes. \nBut as I delved more into it, I realized my\
  \ assumption was w..."
---

Par Edidiong Asikpo

Chaque fois que j'entendais le terme « Cloud native », mes pensées se tournaient généralement vers Kubernetes. Je pensais que « Cloud native » était une phrase utilisée pour décrire uniquement Kubernetes.

Mais en approfondissant le sujet, j'ai réalisé que mon hypothèse était fausse. Le Cloud native ne se limite pas à Kubernetes – c'est bien plus que cela !

Dans cet article, je vais vous aider à comprendre ce que signifie Cloud native, comment fonctionne le modèle de livraison du cloud computing, ses avantages, les principes architecturaux, et plus encore. Commençons.

## Qu'est-ce que le Cloud Native ?

Le Cloud native est une approche pour construire et exécuter des applications qui utilisent le *modèle de livraison du cloud computing*.

Le « cloud » n'est en réalité que l'internet, aussi cliché que cela puisse paraître. C'est un réseau de serveurs où sont hébergées et accessibles des informations, des logiciels, des applications et des services.

Alors, qu'est-ce que le *modèle de livraison du cloud computing* ?

## Qu'est-ce que le modèle de livraison du cloud computing ?

Bien que la définition ci-dessus du Cloud native soit excellente, vous devez comprendre ce que signifient tous les termes – comme « modèle de livraison du cloud computing ». Je me suis certainement demandé ce que c'était lorsque je l'ai vu sur presque toutes les définitions du Cloud native sur internet.

Tout d'abord, il est utile de savoir ce que signifie le cloud computing pour mieux comprendre le modèle de livraison du cloud computing.

### Qu'est-ce que le cloud computing ?

Selon Techopedia,

> **L'informatique** est le processus d'utilisation des ressources informatiques (stockage, réseau et puissance de calcul) pour accomplir une tâche donnée et orientée vers un objectif.
>
> **Le cloud computing** offre une disponibilité à la demande de ces ressources informatiques (mentionnées ci-dessus) sans gestion active directe par l'utilisateur.
>
> Le **modèle de livraison du cloud computing** représente une combinaison spécifique et préemballée de ressources informatiques offerte par un fournisseur de cloud.

Il existe plusieurs modèles de livraison de cloud, mais IaaS, PaaS et SaaS sont les modèles de livraison de cloud les plus populaires et largement utilisés.

### Qu'est-ce que l'Infrastructure en tant que Service (IaaS) ?

Ce modèle de livraison du cloud computing se concentre sur la fourniture d'infrastructures telles que des serveurs, des technologies de réseau, du stockage et de l'espace de centre de données en tant que service aux utilisateurs.

Cela donne aux utilisateurs l'autonomie de décider quelle infrastructure est provisionnée en fonction des différents besoins de leur application. Des exemples populaires de fournisseurs d'IaaS sont Microsoft Azure et AWS.

### Qu'est-ce que la Plateforme en tant que Service (PaaS) ?

Cela est plus axé sur le côté développement en fournissant une *plateforme* aux développeurs pour déployer leurs applications dans le cloud.

Quelques exemples bien connus de fournisseurs de PaaS sont Netlify et Heroku.

PaaS s'appuie sur IaaS, mais contrairement à IaaS, il gère déjà la configuration et la mise en place de l'infrastructure dont votre application a besoin.

Dans les cas où les utilisateurs souhaitent plus de contrôle sur les configurations de leur infrastructure, IaaS est un bon choix.

### Qu'est-ce que le Logiciel en tant que Service (SaaS) ?

Il s'agit du produit logiciel complet fourni en tant que service aux utilisateurs, leur permettant d'effectuer différentes activités.

Par exemple, Gmail est une excellente application SaaS native cloud utilisée par des millions de personnes dans le monde. En tant qu'utilisateur de Gmail, vous ne vous souciez probablement pas de la manière dont il a été construit ou de l'infrastructure sous-jacente, mais vous savez avec certitude que vous pouvez utiliser ce logiciel pour envoyer et recevoir des e-mails.

## Quelle est la différence entre les applications Cloud Native, les technologies Cloud Native et le Cloud Native Computing ?

En apprenant le « Cloud Native », j'ai eu du mal à comprendre les différences entre Cloud native, les applications Cloud native, les technologies Cloud native et le Cloud native computing. J'avais l'impression qu'ils utilisaient tous le préfixe Cloud native mais signifiaient la même chose.

En fait, si vous recherchez « Qu'est-ce que le Cloud native » sur Google, vous verrez plus de dix ressources sur la page de résultats de recherche. Et parmi ces dix ressources, 4 d'entre elles définissent ou parlent du Cloud native. Les 4 autres concernent soit les applications Cloud native, les technologies Cloud native, soit le Cloud native computing.

Et à ma grande surprise, ces ressources avaient toutes des définitions interchangeables de ce que signifiait Cloud native, ce qui m'a rendu confus. Y avait-il une différence ? Ces terminologies signifiaient-elles toutes la même chose ?

J'ai posé la question à plusieurs personnes et j'ai finalement compris les différences. Voici donc mes conclusions. 👍🏽

* **Cloud native** est une approche pour construire et exécuter des applications qui exploitent les avantages du modèle de livraison du cloud computing.
* **Les applications Cloud native** sont des services indépendants, conditionnés sous forme de conteneurs autonomes et légers, portables et pouvant être mis à l'échelle rapidement en fonction de la demande. Elles vous permettent de tirer parti des capacités uniques du cloud.
* **Les technologies Cloud native** sont les technologies utilisées pour construire et mettre à l'échelle des applications Cloud native, comme Kubernetes, Helm, Docker, et d'autres.
* **Le Cloud native computing** et le Cloud native signifient la même chose. Vous pouvez lire la définition de « Cloud native » ci-dessus pour mieux comprendre.

## Architecture Cloud Native

Le Cloud native suit quatre principes architecturaux qui aident les entreprises à livrer des produits plus rapidement, à mettre en œuvre les besoins de leurs clients rapidement, à créer de la valeur plus rapidement et à favoriser la collaboration entre les développeurs et les spécialistes informatiques.

Voici les quatre principes principaux qui font fonctionner l'architecture Cloud native :

### Microservices

Dans les microservices, vous décomposez le code en modules indépendants. Chaque fonctionnalité est un service autonome, et les ressources sont attribuées aux services uniquement lorsque vous en avez besoin. Les applications Cloud native sont construites en suivant cette architecture.

### Conteneurs

Les applications Cloud native sont conditionnées dans des conteneurs. Les conteneurs fournissent un contexte d'isolation pour les microservices, les rendant hautement accessibles et plus faciles à construire, mettre à jour et mettre à l'échelle.

### CI/CD

Les applications Cloud native fonctionnent selon un modèle de livraison continue. Cela favorise la collaboration entre les développeurs et l'équipe des opérations pour leur permettre de construire, déployer et publier des logiciels plus rapidement sans affecter les utilisateurs finaux ou les développeurs d'autres équipes.

### DevOps

Le Cloud native adopte DevOps comme pratique pour rendre possible la livraison continue et l'intégration continue (CI/CD).

## Avantages de la construction d'applications Cloud native

Il y a de nombreux avantages à construire des applications Cloud native :

* **Indépendance** : Parce que les applications Cloud native utilisent l'architecture des microservices, il est possible de construire des applications Cloud native indépendamment les unes des autres. Cela vous donne l'opportunité de construire, gérer et déployer les différents composants d'une application indépendamment sans affecter les autres composants.
* **Automatisation** : Les applications Cloud native fonctionnent selon un modèle de livraison continue, ce qui permet de livrer les mises à jour logicielles immédiatement.
* **Aucun temps d'arrêt** : Grâce aux orchestrateurs de conteneurs tels que Kubernetes, vous pouvez déployer une mise à jour logicielle avec essentiellement zéro temps d'arrêt. Si une instance de l'application tombe en panne, Kubernetes en démarrera automatiquement une autre pour vous immédiatement.
* **Évolutivité** : Les applications Cloud native permettent des options de déploiement flexibles à travers le réseau, ce qui facilite le développement, le déploiement et l'itération sur l'application.
* **Basé sur des normes** : La plupart des services Cloud native suivent un ensemble de normes promues par l'organisation Open Source [CNCF](https://www.cncf.io/). Ces normes ont été vérifiées et approuvées par la communauté et sont utilisées par certaines des plus grandes entreprises technologiques du monde. Cela aide à réduire le verrouillage par les fournisseurs et garantit que les applications sont construites de la bonne manière.

## Résumé

J'espère que vous avez apprécié la lecture de cet article. Si vous souhaitez en savoir plus sur le Cloud native, voici quelques ressources utiles pour approfondir le sujet :

* [Cloud Native 101](https://www.youtube.com/watch?v=9Ik96SBaIvs), VMware.
* [Comment commencer votre voyage Cloud native Kubernetes](https://blog.getambassador.io/how-to-start-your-cloud-native-kubernetes-journey-ee88585d9ff3), Ambassador Labs.
* [Comprendre les applications Cloud native](https://www.redhat.com/en/topics/cloud-native-apps), Red Hat.
* [Applications basées sur le cloud, Cloud native et applications activées par le cloud – Quelle est la différence ?](https://www.papertrail.com/solution/tips/cloud-based-cloud-native-and-cloud-enabled-applications-whats-the-difference/), PaperTrail.
* [Qu'est-ce que le Cloud Native ?](https://www.oracle.com/cloud/cloud-native/what-is-cloud-native/), Oracle.
* [Quelles sont les applications Cloud Native ?](https://tanzu.vmware.com/cloud-native), VMware.

Si vous avez des questions, vous pouvez me les poser sur [Twitter](https://twitter.com/Didicodes).