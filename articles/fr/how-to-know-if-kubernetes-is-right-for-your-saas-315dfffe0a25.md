---
title: Comment savoir si Kubernetes est adapté à votre SaaS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-03T11:29:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-know-if-kubernetes-is-right-for-your-saas-315dfffe0a25
coverImage: https://cdn-media-1.freecodecamp.org/images/1*tJXXWOYkuMF3RkqZxMmvFw.png
tags:
- name: Cloud Computing
  slug: cloud-computing
- name: Devops
  slug: devops
- name: Docker
  slug: docker
- name: SaaS
  slug: saas
- name: 'tech '
  slug: tech
seo_title: Comment savoir si Kubernetes est adapté à votre SaaS
seo_desc: 'By Ben Sears

  Kubernetes is an awesome technology, and I personally have seen great gains in my
  ability to scale, deploy, and manage my own SaaS because of it. But, not everyone
  would immediately benefit from adopting it for a number of reasons:


  Lack...'
---

Par Ben Sears

Kubernetes est une technologie géniale, et personnellement, j'ai vu de grands gains dans ma capacité à mettre à l'échelle, déployer et gérer mon propre SaaS grâce à elle. Mais, tout le monde ne bénéficierait pas immédiatement de son adoption pour un certain nombre de raisons :

* Manque de familiarité avec la technologie des conteneurs
* Architecture de l'application non propice à l'utilisation des avantages de Kubernetes
* Augmentation de la quantité d'efforts par rapport au temps passé

Si vous êtes intéressé par Kubernetes mais que vous n'êtes pas sûr d'investir le temps/les ressources nécessaires, cet article est pour vous.

### Quelle est votre expérience avec les conteneurs ? ?

Afin de comprendre ce que Kubernetes peut faire pour vous, vous devez d'abord connaître les avantages que les conteneurs fournissent. Avant de passer du temps sur Kubernetes, vous devez d'abord :

#### Conteneuriser votre application

![Image](https://cdn-media-1.freecodecamp.org/images/AZhfT1f8jS0KnbLrYz7QXj1LYdXd9pADqp2r)

Tout d'abord, votre application doit être conteneurisée. Cela signifie définir les étapes nécessaires pour prendre une image de base du système d'exploitation et installer votre application dessus dans un fichier (généralement un Dockerfile).

Passer par ce processus ainsi que définir les variables d'environnement nécessaires pour configurer votre application (telles que l'URL, le nom d'utilisateur et le mot de passe de la base de données que votre application utilise) sera crucial pour rendre votre image de conteneur utilisable par Kubernetes.

Notez également les dépendances dont votre application a besoin pour fonctionner et apprenez à utiliser les versions conteneurisées de celles-ci.

#### [Comprendre comment fonctionne le stockage](https://docs.docker.com/engine/admin/volumes/)

Les conteneurs sont conçus pour contenir uniquement le code nécessaire à l'exécution d'une application. Toutes les données persistantes doivent être stockées ailleurs, car le processus de suppression et de création de conteneurs (très courant lors de la gestion de conteneurs) détruit également toutes les données stockées dans le système de fichiers de ce conteneur.

Savoir comment le stockage des conteneurs est censé fonctionner et comment gérer des choses comme la sauvegarde des données, le déplacement de ces données entre les conteneurs et l'accès aux données depuis l'extérieur du conteneur est très précieux lorsque l'on considère Kubernetes.

Kubernetes facilite la gestion du stockage avec des fonctionnalités telles que l'approvisionnement automatique. Cela permet à votre fournisseur de stockage (tel que AWS EBS) de créer de nouveaux volumes à la volée lorsque de nouveaux conteneurs sont créés, en les montant automatiquement.

#### [Comprendre comment fonctionne la mise en réseau](https://docs.docker.com/engine/userguide/networking/)

La manière dont vous implémentez la mise en réseau peut jouer un rôle important dans la façon dont vous utilisez Kubernetes. Savoir comment ouvrir des systèmes spécifiques à l'internet public et en cacher d'autres, tels que les bases de données, tout en maintenant la communication entre les services est important à comprendre pour commencer. Certaines opérations plus compliquées que j'ai dû apprendre étaient comment intégrer l'équilibrage de charge ainsi que donner à chaque instance de client un nom d'hôte personnalisé (choses que Kubernetes rend beaucoup plus faciles).

### Kubernetes résout-il les problèmes que vous rencontrez actuellement ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/zqFzeEAsKrXpWWtkZBdh-ju7DgxgV4-RvEcz)

Si vous n'utilisez pas de conteneurs pour déployer votre application, vous ne devriez probablement pas encore utiliser Kubernetes. Les problèmes que Kubernetes vise à résoudre sont ceux qui surviennent lorsque vous essayez de mettre à l'échelle une infrastructure basée sur des conteneurs.

Voici quelques-uns des problèmes que je pense que Kubernetes résout bien lorsque l'on essaie de gérer des conteneurs à grande échelle.

#### Mise à l'échelle des ressources

Kubernetes est essentiellement un cluster de nœuds qui fournissent des ressources de calcul pouvant être consommées par des charges de travail de conteneurs. Cette architecture en cluster permet une mise à l'échelle ou une réduction très facile des ressources. Vous ajoutez ou retirez simplement des nœuds du cluster, et Kubernetes utilisera automatiquement ces ressources ou réaffectera les charges de travail sur vos ressources existantes.

Cela a résolu un problème majeur auquel j'étais confronté, car je suis passé d'un seul serveur que je devais continuer à mettre à l'échelle (un processus manuel ennuyeux) à la capacité de mettre à l'échelle ou de réduire mon infrastructure avec une seule commande en utilisant le CLI.

#### Effectuer des mises à jour massives

Un autre problème que Kubernetes résout est la capacité de mettre à jour tous vos conteneurs. Auparavant, j'écrivais des scripts shell qui sélectionnaient chaque conteneur pertinent et le recréaient en utilisant une nouvelle balise d'image. Le processus prenait plus d'une heure, et je n'avais aucun moyen de valider que la mise à jour avait réussi. Avec Kubernetes, j'ai pu effectuer une mise à jour avec une seule commande comme dans l'exemple ci-dessous :

```bash
// Mettre à jour tous les pods de frontend avec une nouvelle balise d'image
$ kubectl rolling-update frontend --image=image:v2
```

Kubernetes vous permet également de mettre à jour n'importe quelle partie de Kubernetes (réseaux, stockage, etc.) avec des commandes basées sur n'importe quel critère. C'est un énorme progrès par rapport à l'écriture de vos propres scripts pour apporter des modifications à votre infrastructure.

#### Auto-réparation

Le dernier et l'un des éléments les plus importants de Kubernetes dont je voudrais parler est la capacité d'auto-réparation. Si Kubernetes détecte quelque chose de mal avec une partie de son infrastructure, comme un nœud qui ne répond pas ou un conteneur qui ne passe pas son contrôle de santé, il effectuera des étapes pour recréer ces parties de lui-même jusqu'à ce que les choses recommencent à fonctionner.

Cela est extrêmement utile car si une partie du cluster tombe en panne pour une raison quelconque, la charge de travail sera réaffectée et vous pouvez même faire en sorte que Kubernetes recrée des serveurs entiers pour résoudre le problème.

### Votre architecture d'application devra-t-elle changer ? ?

![Image](https://cdn-media-1.freecodecamp.org/images/I0-fuTV0uXQR1xoGvWjcyCI-eDJLgJlkrxHZ)
_Parfois, adapter votre application à Kubernetes revient à mettre un carré dans un trou rond_

Lorsque j'ai migré vers Kubernetes, il n'y avait pas tant de changements que j'ai dû apporter car il était à l'origine conçu pour être une plateforme multi-instances déployée via des conteneurs.

Voici quelques-unes des choses que j'ai apprises en migrant ma propre charge de travail vers Kubernetes.

#### Le temps de démarrage de votre application est important

Lorsque vous créez un nouveau déploiement, vous devez attendre que votre application démarre avant qu'elle ne soit disponible pour l'utilisateur final. Cela devient un problème si votre processus de déploiement implique la création de nouvelles instances lorsque l'utilisateur final appuie sur un bouton ou si vous effectuez des mises à jour sur toutes les instances de vos clients, car cela nécessite une reconstruction des pods.

Lorsque vous passez à Kubernetes, vous devrez peut-être apporter quelques modifications à votre base de code pour rendre le processus de démarrage plus efficace afin que l'utilisateur final n'ait pas une expérience dégradée en utilisant votre produit.

#### L'adaptation des architectures multi-locataires est difficile

Une architecture multi-locataire signifie que vous avez une seule instance de votre application qui gère tous vos utilisateurs finaux dans des locataires partitionnés, généralement avec une seule base de données partagée entre tout le monde.

Si votre application n'est pas conçue pour utiliser le clustering (plusieurs serveurs agissant comme une seule instance), vous ne devriez pas encore utiliser Kubernetes.

Généralement, je vois deux types d'architectures lors de l'utilisation de Kubernetes :

* Multi-instances avec une instance de l'application pour chaque client
* Architecture multi-locataire avec des capacités de clustering car elles peuvent utiliser la mise à l'échelle des ressources

Je préfère personnellement les multi-instances car elles sont beaucoup plus faciles à implémenter par rapport à une architecture multi-locataire en cluster. De plus, le travail nécessaire pour passer d'une architecture multi-locataire à une architecture multi-instances n'est pas trop mauvais par rapport à l'ajout de capacités de clustering à une architecture multi-instances.

#### Passer à une application sans état représente un effort important

L'une des grandes fonctionnalités de Kubernetes est la capacité de mettre à l'échelle le nombre de pods dans un déploiement. Mais, si votre application n'est pas en cluster ou sans état, cette fonctionnalité est gaspillée car les pods supplémentaires dans un déploiement ne seront pas configurés correctement et ne pourront pas être utilisés.

Le processus d'utilisation de l'absence d'état dans Kubernetes est souvent plus problématique que cela n'en vaut la peine, car la plupart du temps, vous devrez complètement réorganiser la façon dont vous gérez les configurations dans votre application.

Ne vous découragez pas si vous ne voulez pas passer du temps à rendre votre application sans état ou en cluster, car il existe de nombreuses façons d'adapter les déploiements avec état pour utiliser Kubernetes. Mais celles-ci ont leurs propres problèmes que je n'aborderai pas dans cet article.

### Devez-vous adopter Kubernetes ? ?

Après vous être posé ces questions, vous devriez avoir une assez bonne idée si Kubernetes sera adapté à vos besoins actuels. La plupart des startups en phase précoce n'en auront probablement pas besoin, et les plus matures peuvent avoir beaucoup investi dans d'autres technologies, ce qui rendrait le passage à Kubernetes peu réaliste.

Je pense que le meilleur cas pour quelqu'un passant à Kubernetes est une startup cherchant à passer d'une infrastructure cloud viable minimale utilisant des conteneurs pour alimenter les charges de travail de production à quelque chose de plus stable. C'était mon cas, et je peux dire que je suis passé d'avoir des temps d'arrêt périodiques dus à une mauvaise gestion des ressources et à des serveurs surchargés à ne plus du tout m'inquiéter de mon infrastructure grâce à la puissance de Kubernetes.

Vous cherchez à connecter Kubernetes à votre SaaS ? Parlons-en - [ben@servicebot.io](mailto:ben@servicebot.io)

![Image](https://cdn-media-1.freecodecamp.org/images/Doj-pHbdszxakMEVRnRFpJmZdW8nkJmsKoXo)