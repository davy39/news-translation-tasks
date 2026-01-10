---
title: 'Jour 23 : Comment construire une application avec ARKit et Unity mettant en
  vedette le PortKey de Harry Potter'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-18T15:22:37.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-app-with-arkit-and-unity-featuring-harry-potter-portkeys-7dd478b02735
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QvstEQ294-nyHY7mJnViLA.jpeg
tags:
- name: Augmented Reality
  slug: augmented-reality
- name: iOS
  slug: ios
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Virtual Reality
  slug: virtual-reality
seo_title: 'Jour 23 : Comment construire une application avec ARKit et Unity mettant
  en vedette le PortKey de Harry Potter'
seo_desc: 'By Harini Janakiraman

  Augmented Reality. The future screams of it. The present is full of it: filters,
  games, and AR apps are popping up daily. Imagine a world where everywhere you look
  there are visual data aids to augment your comprehension.

  Now, I...'
---

Par Harini Janakiraman

Réalité Augmentée. L'avenir en dépend. Le présent en est rempli : filtres, jeux et applications AR apparaissent quotidiennement. Imaginez un monde où, partout où vous regardez, il y a des aides visuelles pour augmenter votre compréhension.

Maintenant, je préférerais me lancer dans la VR, surtout après avoir vu Ready Player One. Oh, comme je souhaite être transportée à Oasis maintenant ! Cependant, la RA a plus de cas d'utilisation dans le monde réel, de l'achat de meubles à la construction d'usines industrielles — les possibilités sont infinies.

> La réalité augmentée fera partie essentielle de votre vie quotidienne. Elle changera tout.
— Tim Cook

Maintenant, ces affirmations doivent résister à l'épreuve du temps (cas d'utilisation puissants, visuels réalistes, vitesse de traitement du matériel, etc.). En attendant, la RA mobile est probablement le banc d'essai pour les développeurs, avant qu'un casque ou quelque chose de similaire ne fasse partie de votre technologie quotidienne, avec une communauté de développeurs RA et une multitude d'applications.

Aujourd'hui, nous allons utiliser ARKit d'Apple (qui a rendu le développement RA beaucoup plus facile à explorer) pour nous initier et expérimenter avec la RA. Nous allons construire une application de base de superposition d'objets en style RA "additif" à la vue de la caméra. Pour rendre les choses intéressantes, nous allons placer des PortKeys de Harry Potter comme nos objets RA, qui vous transporteront dans un monde fantastique (cette partie est laissée à votre imagination pour l'instant. Je vais construire une version plus complète de l'application dans la prochaine partie de cette série sur la RA, alors restez à l'écoute !).

![Image](https://cdn-media-1.freecodecamp.org/images/1*QvstEQ294-nyHY7mJnViLA.jpeg)
_Image [source](https://www.hp-lexicon.org/thing/portkey/" rel="noopener" target="_blank" title=")_

#### **Qu'est-ce qu'un PortKey ?**

_(Pour les Moldus, voici la définition *clin d'œil clin d'œil*) :_

Un PortKey, dans le monde de Harry Potter, est un objet enchanté qui, lorsqu'il est touché, transporte instantanément une personne du point A au point B. L'objet est généralement un morceau de pacotille sans valeur et est placé aléatoirement pour ne pas attirer l'attention.

### Projet (environ 3 heures)

Dans ce tutoriel, vous apprendrez à construire une application Unity avec ARKit. Nous ajouterons une couche de réalité augmentée mettant en vedette les PortKeys de Harry Potter. La plupart du temps que vous passerez sera consacré aux installations, alors prenez votre café et préparez-vous !

### Étape 1 : Installation

![Image](https://cdn-media-1.freecodecamp.org/images/1*eynlod-95BXqY5K-GKsveg.png)

Au cas où vous ne l'auriez pas déjà, téléchargez et installez la dernière version de [Xcode](https://developer.apple.com/develop/) pour votre Mac et [Unity](https://store.unity.com/).

Installez la version gratuite personnelle de Unity, mais assurez-vous que "Support de construction iOS" est coché.

Vous aurez également besoin d'un compte de développeur iOS et d'un iPhone, de préférence, pour tester l'application RA que vous construisez.

### Étape 2 : Configurer un projet Unity avec le plugin ARKit

![Image](https://cdn-media-1.freecodecamp.org/images/1*XuIjqaU1t5tnuY95fiTWjg.png)

Créez un nouveau projet 3D appelé "ARHarryPotterApp".

![Image](https://cdn-media-1.freecodecamp.org/images/1*PiyWLQ7TaZX6EyZJQ5PF9g.png)

Une fois le projet créé, à partir de l'onglet "Asset Store", téléchargez ARKit dans votre projet.

### Étape 3 : Créer la scène AR et ajouter des actifs

![Image](https://cdn-media-1.freecodecamp.org/images/1*-7JQn-VjoPPb9xSH5kqUpg.png)

Commençons par une scène d'exemple qui est fournie avec l'actif ARKit téléchargé. Naviguez vers la scène d'exemple dans le panneau de gauche et double-cliquez pour ouvrir "UnityARKitScene".

Cela ouvrira un actif de cube de base placé dans l'onglet "Scene", qui est votre champ de vision. L'actif "HitCube" ici peut facilement être remplacé par n'importe quel actif de votre choix pour créer votre propre scène de réalité augmentée unique.

Il y a plusieurs propriétés de chaque actif affichées dans le panneau Inspector à droite, telles que l'ombre/l'éclairage/le rendu, etc. Nous n'entrerons pas dans les détails de ces propriétés ici (mais je les discuterai plus en détail dans un prochain article).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iBqQWR1_N-syc-BHTq3-XQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rF93KoFWjh_24kC_IZMCdw.png)

Vous devez faire attention à deux choses ici dans l'exemple. Elles devront être répétées pour tout nouvel actif ajouté à la scène :

1. Dans le panneau de l'inspecteur, ajoutez le composant "Unity AR Hit Test Example" et attachez-le à un script.
2. Glissez-déposez "HitCubeParent" du panneau de gauche sur "Hit Transform" dans le panneau de l'inspecteur à droite dans le composant "Unity AR Hit Test Example".

Assurez-vous de compléter ces deux étapes pour tout nouvel actif ajouté à la scène, car cela aide à placer l'objet dans le plan horizontal.

Pour notre application, nous placerons des PortKeys de Harry Potter aléatoires dans la scène à partir du pack gratuit "Halloween Pack" téléchargé depuis l'asset store.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wE81t6xODD0Niv218kn5rA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*STFbCHC77lsFps4WU0LygA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZGis6PFJWX_Xss5iBCa7Vg.png)

Placez les actifs que vous aimez dans la scène et assurez-vous d'ajouter les composants "Unity AR Hit Test Example" et "Hit Transform" à chacun de ces actifs comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kNg_LCEkC3LkTtQHYTwRyw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SlEDCOP7yZpe6LcTu71R3A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*7a3lEN3Yb5AJ4iaYq_Tt_Q.png)

### Étape 4 : Construire l'application

Enfin, il est temps de construire l'application. Sélectionnez Fichier -> Paramètres de construction. Cochez "Unity ARKitScene" et sélectionnez la plateforme iOS, puis cliquez sur "Changer de plateforme". Cela importera les actifs et configurera la scène.

Vous pouvez ensuite cliquer sur les paramètres du joueur et vérifier l'inspecteur pour vous assurer que "Appareil cible", "Version minimale iOS cible" et "sdk" sont tous configurés comme vous le souhaitez via les paramètres de votre système.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q9LAj2ePvzMHVPQtDZging.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_-IVH0I3OGDKM7Y3RUxggw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nakY_b7Ovalv1O9Hp6fSwA.png)

À ce stade, vous êtes prêt à "Construire" l'application et sélectionner votre répertoire de destination... cela peut prendre un certain temps.

### Étape 5 : Exécutez votre toute première application AR

Une fois la construction terminée, ouvrez le xcodeproj à partir du dossier de destination de la construction. Connectez votre iPhone (avec des versions iOS et Xcode compatibles), signez le projet avec votre équipe (vous aurez besoin d'un compte de développeur iOS) et lancez l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LvM8Hk781OKOHtacf3xaHg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*lWfin4S-HbYGkWg3Y7fLRg.png)

Violà, votre toute première application AR est prête ! Regardez autour de vous dans le champ de vision, repérez les PortKeys de Harry Potter et laissez-vous transporter dans un monde magique ;)

_Si vous avez aimé cela, applaudissez **? s** pour que d'autres puissent le voir aussi ! Suivez-moi sur Twitter @[H**ariniLabs**](https://twitter.com/harinilabs) ou M[**edium**](https://medium.com/@harinilabs) pour obtenir les dernières mises à jour sur d'autres histoires ou simplement pour dire Bonjour :)_

_PS : Inscrivez-vous à ma newsletter [**ici**](http://harinilabs.com/womenintech.html) pour être le premier à recevoir du nouveau contenu et elle est remplie d'une dose d'inspiration du monde de #[**WomenInTech**](http://harinilabs.com/womenintech.html) et oui, les hommes peuvent aussi s'inscrire !_