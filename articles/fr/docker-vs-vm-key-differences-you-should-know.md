---
title: Docker vs Machine Virtuelle (VM) – Les différences clés à connaître
subtitle: ''
author: Bala Priya C
co_authors: []
series: null
date: '2022-10-04T16:48:57.000Z'
originalURL: https://freecodecamp.org/news/docker-vs-vm-key-differences-you-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/docker-vs-vm-diff.png
tags:
- name: container
  slug: container
- name: containerization
  slug: containerization
- name: Docker
  slug: docker
- name: virtual machine
  slug: virtual-machine
seo_title: Docker vs Machine Virtuelle (VM) – Les différences clés à connaître
seo_desc: 'In this guide, you''ll learn the differences between a virtual machine
  and a Docker container.

  Both virtual machines and containers help replicate the development environment,
  and manage dependencies and configurations better. But there are certain di...'
---

Dans ce guide, vous découvrirez les différences entre une **machine virtuelle** (VM) et un conteneur **Docker**.

Les machines virtuelles et les conteneurs aident tous deux à répliquer l'environnement de développement et à mieux gérer les dépendances et les configurations. Mais il existe certaines différences que vous devez connaître pour vous aider à choisir entre une VM ou un conteneur Docker en fonction de l'application.

Au cours des prochaines minutes, nous verrons comment fonctionnent les machines virtuelles et les conteneurs Docker, puis nous résumerons les principales différences entre les deux.

Commençons !

## Les défis du développement et du déploiement d'applications

Lorsque vous travaillez au sein d'une équipe de développement, chaque application nécessite l'installation de plusieurs logiciels et packages tiers. Afin de collaborer et de travailler ensemble, chaque développeur de l'équipe doit configurer son environnement de développement local.

Cependant, la configuration de l'environnement de développement est un processus fastidieux. Les étapes d'installation peuvent être potentiellement différentes selon le système d'exploitation et la configuration du système. Même lors du déploiement, vous devez configurer le même environnement sur le serveur.

Différentes applications nécessitent également plusieurs versions d'un logiciel spécifique, par exemple PostgreSQL. Dans de tels cas, la gestion des dépendances entre les applications devient difficile.

Pour relever les défis ci-dessus, il est très utile que les applications s'exécutent dans des environnements isolés que vous pouvez répliquer facilement, indépendamment de la configuration du système. Les machines virtuelles (VM) et les conteneurs Docker vous aident à y parvenir. Voyons comment !

## Comment fonctionne une machine virtuelle ?

Une **Machine Virtuelle** ou **VM** est l'émulation d'un ordinateur physique à l'intérieur d'une machine hôte.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/1.png)
_Comment fonctionne une VM (image de l'auteur)_

S'exécutant au-dessus du système d'exploitation hôte, un logiciel appelé hyperviseur contrôle les instances de VM. Chaque instance de VM possède son propre système d'exploitation invité. Les applications s'exécutent à l'intérieur de cet environnement isolé.

Vous pouvez avoir plusieurs VM, chacune exécutant une application différente sur un système d'exploitation différent.

## Comment fonctionne un conteneur Docker ?

Récemment, la technologie des conteneurs a révolutionné le processus de développement logiciel et la manière dont les équipes de développement et d'exploitation collaborent. Avec le temps, Docker est devenu le choix de référence pour la conteneurisation d'applications.

Les conteneurs Docker sont analogues aux conteneurs physiques que vous pouvez utiliser pour stocker, emballer et transporter des marchandises. Mais au lieu de biens tangibles, ce sont des conteneurs pour des applications logicielles. 🙂

Un conteneur Docker est une unité logicielle portable qui contient l'application, ainsi que les dépendances et la configuration associées.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/2.png)
_Comment fonctionnent les conteneurs (image de l'auteur)_

Contrairement à une VM, les conteneurs Docker _ne démarrent pas_ leur propre OS invité. Ils s'exécutent plutôt au-dessus du système d'exploitation hôte. Ceci est facilité par un moteur de conteneur (container engine).

## Docker vs VM – Une comparaison complète

### 1️⃣ Virtualisation

D'après ce que nous avons compris jusqu'à présent, les machines virtuelles et les conteneurs Docker fournissent tous deux des environnements isolés pour exécuter des applications. La principale différence entre les deux réside dans la _manière_ dont ils facilitent cette isolation.

Rappelez-vous qu'une VM démarre son propre OS invité. Par conséquent, elle virtualise à la fois le noyau du système d'exploitation et la couche applicative.

Un conteneur Docker virtualise _uniquement_ la couche applicative et s'exécute au-dessus du système d'exploitation hôte.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/3.png)
_Conteneur vs VM (image de l'auteur)_

### 2️⃣ Compatibilité

Une machine virtuelle utilise son propre système d'exploitation et est _indépendante_ du système d'exploitation hôte sur lequel elle s'exécute. Par conséquent, une VM est compatible avec tous les systèmes d'exploitation.

Un conteneur Docker, en revanche, est compatible avec _n'importe quelle_ distribution Linux. Vous pourriez rencontrer des problèmes en exécutant Docker sur une machine Windows ou un ancien Mac.

### 3️⃣ Taille

Une image Docker est légère et se mesure généralement en kilo-octets.

**💡 Note** : Une image Docker désigne l'artéfact contenant l'application, ses dépendances associées et sa configuration. Une instance en cours d'exécution de l'image Docker est appelée un conteneur.

Une instance de VM peut atteindre plusieurs gigaoctets, voire téraoctets.

### 4️⃣ Performance

En termes de performances, les conteneurs Docker offrent des performances quasi-natives. Parce qu'ils sont légers, vous pouvez les démarrer en quelques millisecondes.

Démarrer une VM équivaut à configurer une machine autonome à l'intérieur de votre ordinateur. Le démarrage d'une instance de VM peut prendre jusqu'à quelques minutes.

### 5️⃣ Sécurité

Les conteneurs Docker s'exécutent au-dessus du système d'exploitation hôte. Par conséquent, si l'OS hôte est sensible à des vulnérabilités de sécurité, les conteneurs Docker le sont aussi.

Les machines virtuelles, quant à elles, démarrent leur propre système d'exploitation et sont plus sécurisées. Rappel : chaque machine virtuelle est une machine complète s'exécutant à l'intérieur d'une autre. Si vous avez des contraintes de sécurité strictes à respecter pour des applications sensibles, vous devriez envisager d'utiliser une machine virtuelle à la place.

### 6️⃣ Réplicabilité

Le prochain facteur que nous allons considérer est la facilité avec laquelle vous pouvez répliquer les environnements isolés fournis par les VM et les conteneurs. Nous pouvons déduire la facilité de réplicabilité de nos discussions précédentes sur la **taille** et la **performance**.

Lorsqu'il y a plusieurs applications, chacune devant s'exécuter sur une instance de VM, l'utilisation de VM peut être **inefficace** et **gourmande en ressources**. Les conteneurs Docker, grâce à leur légèreté et à leurs performances, sont préférés lorsque vous devez exécuter plusieurs applications. ✅

## En résumé

J'espère que ce tutoriel vous a aidé à comprendre comment fonctionnent les conteneurs Docker et les VM, ainsi que les principales différences entre les deux.

Voici un résumé de ce que vous avez appris :

|Caractéristique|Docker| Machine Virtuelle (VM)|
|------|---------|------------|
|Compatibilité| Fonctionne mieux avec les distributions Linux|Tous les systèmes d'exploitation|
|Taille| Léger|Sensiblement plus volumineux – de l'ordre du gigaoctet ou plus|
|Virtualisation|Uniquement la couche applicative |À la fois le noyau de l'OS et les couches applicatives|
|Performance|Facile à démarrer (prend généralement quelques millisecondes)|Prend plus de temps pour démarrer une instance de VM|
|Sécurité|Moins sécurisé|Relativement plus sécurisé|
|Réplicabilité|Facile à répliquer. Vous pouvez récupérer (pull) des images Docker correspondant aux diverses applications|Difficile à répliquer, surtout avec l'augmentation du nombre d'instances de VM|


Merci d'avoir lu jusqu'ici. À bientôt dans un autre tutoriel ! 😄