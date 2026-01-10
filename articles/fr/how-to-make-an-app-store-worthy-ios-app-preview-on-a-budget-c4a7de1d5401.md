---
title: Comment créer une prévisualisation d'application iOS digne de l'App Store avec
  un budget limité
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-31T07:56:38.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-an-app-store-worthy-ios-app-preview-on-a-budget-c4a7de1d5401
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BkBLvnsaD7NaXFVj3quLGQ.jpeg
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment créer une prévisualisation d'application iOS digne de l'App Store
  avec un budget limité
seo_desc: 'By Jake Shelley

  Back in 2014, Apple made it possible to add an app preview to the the App Store.
  App previews are the best way to show potential users what your app has to offer
  before they download the app. In fact, users are 3x more likely to insta...'
---

Par Jake Shelley

En 2014, Apple a rendu possible l'ajout d'une prévisualisation d'application à l'App Store. Les prévisualisations d'applications sont le meilleur moyen de montrer aux utilisateurs potentiels ce que votre application a à offrir avant qu'ils ne la téléchargent. En fait, les utilisateurs sont 3 fois plus susceptibles d'installer une application avec une prévisualisation, selon [StoreMaven](https://www.storemaven.com/).

Malheureusement, de nombreux développeurs solo n'ont pas le budget pour engager un professionnel pour créer une prévisualisation d'application. Récemmement, je me suis retrouvé dans cette situation, et après quelques recherches, j'ai trouvé quelques outils gratuits pour créer une prévisualisation d'application de qualité.

Dans cet article, je vais aborder les points suivants :

1. Préparer le contenu
2. Enregistrer la vidéo
3. Monter la vidéo
4. Problèmes courants

Je suppose que vous utilisez un Mac, qui vient avec Xcode, Quicktime et iMovie gratuitement. Si vous n'utilisez pas un Mac, vous devrez peut-être acheter ces outils.

#### Préparer le contenu

Chaque développeur d'applications connaît les parties les plus engageantes et amusantes de son application. Assurez-vous de les mettre en avant dans votre prévisualisation. Déterminez où vous devez ajouter des superpositions de texte et assurez-vous que le texte contraste avec l'arrière-plan sur lequel il est affiché.

Depuis iOS 11, vous pouvez avoir jusqu'à trois prévisualisations pour montrer votre application. Il peut être tentant d'utiliser les 90 secondes qui vous sont accordées, mais je vous suggère de charger vos fonctionnalités les plus intéressantes dans la première. Si les utilisateurs ne sont pas intéressés par votre application après la première prévisualisation, il est peu probable qu'ils prennent le temps de regarder les deux autres.

Enfin, vous pouvez vouloir montrer aux utilisateurs comment ils interagiront avec votre application. Pour montrer les touches et les gestes, utilisez [GSTouchesShowingWindow](https://github.com/LukasCZ/GSTouchesShowingWindow-Swift). C'est super facile à installer et cela montrera comment les utilisateurs interagiront avec votre application.

#### Enregistrer la vidéo

Une fois que vous avez décidé du contenu que vous voulez montrer, vous pouvez commencer à enregistrer votre vidéo. La manière la plus simple de le faire est d'utiliser **Quicktime** pour enregistrer l'écran d'un iPhone connecté.

Branchez votre iPhone, puis ouvrez Quicktime et cliquez sur `Fichier > Nouveau film`. Cela ouvrira une fenêtre d'enregistrement. À partir du menu déroulant à côté du bouton d'enregistrement, vous pouvez sélectionner le périphérique que vous avez connecté.

L'utilisation d'un périphérique connecté signifie que vous êtes limité aux périphériques que vous possédez. Heureusement, vous pouvez utiliser **Xcode CLI** pour enregistrer vos actions dans le simulateur.

Pour enregistrer avec Xcode CLI, commencez par exécuter votre simulateur dans Xcode. Ensuite, ouvrez votre terminal et entrez la commande suivante :

```
$ xcrun simctl io booted recordVideo example.mp4
```

Effectuez les actions que vous souhaitez enregistrer dans le simulateur, puis appuyez sur `ctrl-C` dans votre terminal pour terminer la session d'enregistrement. La commande ci-dessus ajoutera la vidéo `example.mp4` au répertoire actuel de votre terminal.

#### Monter la vidéo

Il y a deux objectifs que vous essayez d'atteindre lors du montage de votre prévisualisation :

1. Montrer votre application sous son meilleur jour
2. Réduire la prévisualisation à une durée comprise entre 15 et 30 secondes

Le meilleur outil pour monter une prévisualisation d'application est **iMovie**. Ouvrez iMovie et cliquez sur `Fichier > Nouvelle prévisualisation d'application`. Glissez-déposez votre vidéo dans la zone de médias pour l'ajouter à votre projet.

Je ne vais pas entrer dans les détails de la façon de monter une application dans iMovie, mais l'interface est assez intuitive. Il suffit de glisser-déposer les scènes que vous souhaitez dans la zone inférieure pour les ajouter à votre clip. `command+B` vous permettra de diviser votre clip afin que vous puissiez ajouter des transitions sympas et mieux suivre le rythme. Vous pouvez ajouter des transitions entre les clips divisés, de l'audio et des écrans de titre.

![Image](https://cdn-media-1.freecodecamp.org/images/OR3RzAsbdE1jvl6TmgArn3wRGgzwkkelV1ME)
_Vous pouvez ajouter des superpositions de texte et de l'audio à votre prévisualisation d'application dans iMovie avant de l'exporter_

Une fois que vous avez terminé le montage, cliquez sur `Fichier > Partager > Prévisualisation d'application` (si vous ne voyez pas `Prévisualisation d'application`, vous pouvez également cliquer sur `Fichier`). Ensuite, sélectionnez la destination où vous souhaitez l'enregistrer et appuyez sur Entrée. Après quelques secondes, votre vidéo sera disponible.

#### Problèmes courants

À ce stade, il est probable que vous ayez déjà tout prêt, mais lorsque vous essayez de télécharger votre prévisualisation sur iTunes Connect, vous obtenez une erreur. Il est probable que vos problèmes soient causés par l'une de ces deux exigences de prévisualisation d'application :

1. La résolution de votre prévisualisation doit correspondre aux exigences pour le type de périphérique
2. Votre prévisualisation doit fonctionner à 30 fps

La probabilité que la résolution de votre prévisualisation ne réponde pas aux exigences est assez faible, mais j'ai effectivement rencontré des problèmes **même lorsque j'ai enregistré directement depuis mon iPhone**. Pour une raison quelconque, Quicktime a capturé tout avec un pixel de décalage, donc iTunes Connect a refusé de me laisser télécharger la vidéo.

Après quelques recherches, j'ai trouvé un outil gratuit qui vous permet de recadrer votre fichier `.mov` (ou tout type de vidéo) dans la résolution correcte. Allez sur [ezgif.com](https://ezgif.com/) et cliquez sur `Video to GIF` dans la barre de navigation. Cela ouvre une autre barre de navigation en dessous de la première, où vous verrez `Crop video`. Cliquez dessus, puis vous pouvez télécharger votre fichier `.mov` Quicktime. Recadrez la vidéo à la taille dont vous avez besoin et téléchargez le nouveau fichier.

Si vous rencontrez des problèmes liés au fait que votre prévisualisation ne fonctionne pas à 30 fps, c'est un problème facile à résoudre (gratuitement) avec [ffmpeg](https://www.ffmpeg.org/). Ouvrez votre terminal, assurez-vous d'avoir installé [homebrew](https://brew.sh/) et entrez :

```
$ brew install ffmpeg
```

Maintenant, avec ffmpeg installé, `cd` dans le répertoire qui contient votre vidéo et entrez :

```
$ ffmpeg -i "original.mov" -r 30 "converted_30fps_video.mov"
```

Cela générera votre vidéo convertie en 30 fps.

#### Conclusion

Vous devriez maintenant avoir une prévisualisation d'application qui répond à toutes les exigences d'Apple. Avoir une prévisualisation d'application est important pour que votre application se distingue parmi les millions d'applications sur l'App Store. J'ai trouvé que les outils utilisés dans ce guide m'ont permis d'obtenir une prévisualisation d'application de haute qualité qui, selon moi, a bien commercialisé mon application, et cela n'a pas coûté un sou !

J'espère que ce guide vous a fait économiser du temps et de l'argent. Bonne chance sur l'App Store !

_Merci beaucoup d'avoir lu ! Si vous avez aimé cette histoire, suivez-moi sur [Twitter](https://twitter.com/JakeShelley3) où je publie des articles sur la gestion de produit, l'ingénierie et le design._