---
title: Optimisez votre flux de travail avec des profils et des dispositions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-23T14:24:05.000Z'
originalURL: https://freecodecamp.org/news/supercharge-your-workflow-with-profiles-and-arrangements-99099da313b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PU7wwmX3JaTa6CcDKvSwpA.jpeg
tags:
- name: Front-end Development
  slug: front-end-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Optimisez votre flux de travail avec des profils et des dispositions
seo_desc: 'By Marcus Wood

  If you’ve ever had to manage multiple projects, keeping up with the command line
  can be cumbersome. Here are a couple of hot tips on how juggle multiple projects
  that will save you a ton of time.

  If you’re using the regular Mac Termina...'
---

Par Marcus Wood

Si vous avez déjà dû gérer plusieurs projets, suivre la ligne de commande peut être fastidieux. Voici quelques conseils pour jongler avec plusieurs projets qui vous feront gagner un temps précieux.

Si vous utilisez le Terminal Mac régulier, je vous recommande vivement de passer à [iTerm2](https://www.iterm2.com/) (c'est simplement mieux). Plus d'informations à ce sujet dans un instant.

#### Alias SSH

Parfois, vous devez vous connecter en SSH à un serveur quelque part. Parfois, vous avez vingt serveurs différents auxquels vous souhaitez vous connecter en SSH. Se souvenir de leur emplacement et de leur nom peut être fastidieux.

Pour gagner du temps, créez des alias pour chaque serveur en moins d'une minute. Voici comment faire :

```
// Ouvrir une fenêtre de terminalnano ~/.ssh/config
```

```
// Remplissez ce qui suit pour créer un aliasHost <Nom que vous souhaitez attribuer>  Hostname <Où vous souhaitez vous connecter en SSH>  User <Utilisateur avec lequel vous souhaitez vous connecter>  IdentityFile ~/.ssh/<fichier pem que vous souhaitez utiliser>
```

```
// Quitter et enregistrer le fichierctrl + xyenter
```

```
// Au lieu de faire cela pour vous connecterssh -i "<fichier pem>" <utilisateur>@<nom d'hôte>
```

```
// Vous pouvez faire celassh nom-que-vous-avez-attribué
```

#### Profils et dispositions iTerm2

Les profils sont géniaux et ont changé mon flux de travail quotidien. Parfois, votre terminal ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*doLyDCyaaDRpKmByae3DWA.png)
_Lequel voulais-je à nouveau ? ?_

Le problème est que vous ne savez pas quelle fenêtre vous voulez cliquer. Vous ne voulez pas non plus fermer les fenêtres, car alors vous devrez ouvrir une nouvelle fenêtre, revenir au bon répertoire et vous souvenir de la commande à exécuter.

Avec les profils et les dispositions de fenêtres, vous n'avez pas à vous soucier de tout cela.

Il y a une courte vidéo de démonstration ci-dessous si vous vous perdez à l'une de ces étapes.

Un profil vous permet d'ouvrir une nouvelle fenêtre de ligne de commande dans un certain répertoire et d'exécuter des commandes automatiquement. Créons-en un !

Tout d'abord, fermez toutes les fenêtres de ligne de commande ouvertes dans iTerm et commencez avec une nouvelle fenêtre de ligne de commande. Ensuite, vous voudrez naviguer vers « Profiles » dans la barre de menus et cliquer sur « Open Profiles… »

![Image](https://cdn-media-1.freecodecamp.org/images/1*dMLCZZID5N8XRNu2DGyrLw.png)
_Vous devriez voir quelque chose comme ceci_

Maintenant, cliquez sur « Edit Profiles… » ce qui devrait vous amener ici :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CBAfmdNNCcrQYrkZ_FLDlw.png)
_Gamebyrd et Mongod sont des profils que j'ai créés, ne vous inquiétez pas si vous ne les voyez pas_

Cliquez sur le signe + en bas à gauche pour créer un nouveau profil. Assurez-vous de lui donner un nom et de mettre à jour le répertoire pour qu'il soit à la racine de votre projet.

Si vous souhaitez exécuter des commandes lorsque ce profil est ouvert, ajoutez-les dans le champ « Send text at start: ». L'une de mes recettes préférées est d'ouvrir le projet dans mon éditeur de code et de le construire pour le développement.

```
// Séparer les commandes avec un point-virguleatom .; preact watch
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ht3-GXIzPXeGDxeF_IPRyA.png)
_Assurez-vous de cliquer sur le bouton radio Directory_

La sortie de la fenêtre enregistrera vos modifications (il n'y a pas de bouton pour cela).

Ensuite, nous devons le tester. Cliquez sur « Profiles » dans la barre de menus et sélectionnez le profil que vous avez créé pour vous assurer qu'il fonctionne. Si vous rencontrez des problèmes, assurez-vous que votre chemin de répertoire est correct et que vos commandes sont correctement séparées.

Une fois que tout cela fonctionne, il est temps de créer une disposition de fenêtre pour lancer facilement le profil nouvellement créé. **Assurez-vous de ne pas avoir de fenêtres de terminal ouvertes lorsque vous effectuez cette étape, sinon elles seront enregistrées dans la disposition.**

Dans une nouvelle fenêtre de terminal, cliquez sur le profil que vous venez de créer. Si elle s'ouvre dans un nouvel onglet, assurez-vous de fermer l'onglet « Default ». Naviguez vers l'onglet « Window » dans la barre de menus et sélectionnez « Save Window Arrangement ». Donnez-lui un nom et cliquez sur OK. Vous êtes prêt à partir !

Maintenant, toutes vos fenêtres de terminal seront nommées. Elles se souviendront automatiquement des commandes dont vous avez besoin pour démarrer chaque projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8y6dJLmDB93veUvHtBTc4w.png)
_??????_

#### Conclusion

Après la première fois que vous le faites, vous pourrez créer de nouveaux profils et dispositions avec facilité. Vous pouvez également combiner plusieurs profils dans une disposition, utiliser des fenêtres de terminal à onglets pour exécuter plusieurs parties d'un projet, et bien plus encore.

Cela vous a-t-il été utile ? Si oui, applaudissez l'histoire et faites-moi savoir ce que vous aimeriez savoir d'autre sur mon processus de développement ou des conseils pour maîtriser la ligne de commande.

_Je m'appelle Marcus Wood. Je suis le fondateur de Caldera, une agence numérique full-service spécialisée dans les applications web._