---
title: Comment créer un ballon de basket qui rebondit dans Unity avec des matériaux
  et des textures 🏀
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-05-27T15:16:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-a-basketball-in-unity-with-materials-and-textures
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/basketball-image.jpg
tags:
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: unity
  slug: unity
seo_title: Comment créer un ballon de basket qui rebondit dans Unity avec des matériaux
  et des textures 🏀
seo_desc: "By Rajat Kumar Gupta\nIn this article, I'll teach you how to make a basketball\
  \ using materials and textures in Unity. You can extend this micro-concept to create\
  \ any kind of ball like a football, tennis ball, or snooker balls. \nThat said,\
  \ these techni..."
---

Par Rajat Kumar Gupta

Dans cet article, je vais vous apprendre à créer un ballon de basket en utilisant des matériaux et des textures dans Unity. Vous pouvez étendre ce micro-concept pour créer tout type de balle comme un ballon de football, une balle de tennis ou des boules de snooker. 

Cela dit, ces techniques ne sont pas limitées à la création d'objets 3D ronds comme des balles. Vous devriez pouvoir utiliser ce concept pour personnaliser l'apparence de tout type de géométrie (ou de maillage).

Voici ce que vous allez créer👋🏻

![Un ballon de basket qui rebondit sur une surface plane](https://www.freecodecamp.org/news/content/images/2021/05/1.gif)
_Basketball🏀_

Imaginez le ballon de basket comme une sphère (c'est-à-dire un maillage) enveloppée dans un joli papier (c'est-à-dire une texture).

Commençons.

### Prérequis

Pour faire rebondir la balle, votre scène d'exemple doit contenir les éléments suivants :

1. Un plan
2. Une sphère avec un matériau personnalisé

Voyons d'abord comment faire cela.

## Étape 1 : Comment ajouter un plan et une sphère à la scène

Tout d'abord, allez dans le panneau Hiérarchie dans Unity. Faites un clic droit et sélectionnez "plane" pour ajouter un plan à votre scène. Faites de même pour ajouter une sphère.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/plane-and-sphere.gif)
_Ajoutez un plan et une sphère à la scène_

## Étape 2 : Comment créer un dossier contenant toutes les couleurs

Il est toujours bon de commencer par créer un dossier contenant toutes vos couleurs et matériaux. Cela vous aide à créer une palette (ou une collection de couleurs et de matériaux) et facilite l'application des actifs de votre palette aux Game Objects.

Allez simplement dans le panneau Projets. Ensuite, faites un clic droit dans le sous-panneau des actifs, cliquez sur créer, puis sélectionnez dossier. Nommez ce dossier "Materials".

![Image](https://www.freecodecamp.org/news/content/images/2021/05/ColorFolder-min.gif)
_Clic droit dans le panneau des actifs > Créer > Dossier > Nommez-le "Materials"_

## Étape 3 : Comment créer un matériau pour le plan

L'étape suivante consiste à créer des couleurs (ou des matériaux) pour le plan.

Allez dans le dossier des matériaux que vous avez créé à l'étape précédente en double-cliquant dessus. Faites un clic droit et sélectionnez créer. Ensuite, sélectionnez "Material" dans le menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_5PyYNjCGe3_lYB4LYwb5KA.gif)
_Allez dans le dossier Materials > Clic droit > Créer > Material > Nommez-le "MyColor" (ou ce que vous voulez)_

## Étape 4 : Comment changer la propriété Albedo du matériau

Ensuite, sélectionnez le matériau créé et consultez ses propriétés dans le panneau Inspecteur sur le côté droit. 

Notez que vous devez uniquement changer la propriété albedo du matériau du plan et **non** celle de la sphère. Nous créerons un matériau pour la sphère plus tard dans cet article.

Il est important que votre sphère ait un matériau personnalisé dans cette étape. Sinon, vous ne pourrez pas visualiser ou modifier les différentes propriétés du matériau.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/change-albedo-property.gif)
_Changez la propriété "albedo" pour la couleur que vous voulez._

Super ! Maintenant vous pouvez créer une collection de couleurs en utilisant la même technique.

Maintenant nous pouvons appliquer la couleur à n'importe quel Game Object comme ceci👋.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_n1b2BxGPRFe5hV6uiBMTCw.gif)
_Glissez-déposez le matériau dans le Game Object (dans notre cas, ce sera un plan au lieu d'un cube)_

## Étape 5 : Comment ajouter le composant Rigidbody à la balle

Puisque nous voulons que notre balle obéisse aux lois de la physique, nous devons lui attacher le composant Rigidbody.

Pour ce faire, sélectionnez la Sphère dans votre panneau Hiérarchie de la scène. Cliquez sur Ajouter un composant, puis assurez-vous que la case "Use Gravity" est cochée. Nous ne voulons pas que la balle s'envole dans l'espace 😅.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_i5YL1YYQ5zDSYM2X3TCLFg.gif)
_Sélectionnez la Sphère > Ajouter un composant > Rigid Body > Gardez la case "Use Gravity" cochée_

## Étape 6 : Comment créer un matériau "Rebondissant"

Allez dans le panneau des actifs. Faites un clic droit, puis cliquez sur créer. Assurez-vous de sélectionner "Physic Material" et **non** Material. Nommez le matériau comme vous le souhaitez. Je l'ai nommé "Bouncy" pour des raisons évidentes.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_b_3AtywJx2c4owi9uGamOg.gif)
_Clic droit dans le panneau des actifs > Créer > Physic Material > Nommez-le "Bouncy"_

## Étape 7 : Comment changer les propriétés du matériau rebondissant

Sélectionnez le matériau Bouncy. Vous devriez pouvoir voir les propriétés de ce matériau sur le côté droit dans le panneau Inspecteur. Changez maintenant les propriétés.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_D9khGemDSHYutFoTs08WzQ.gif)
_Définit la friction à 0 et le rebond à 1_

## Étape 8 : Comment appliquer le matériau à la sphère

Maintenant, appliquez ce matériau à la sphère (c'est-à-dire la balle) dans notre scène en glissant-déposant simplement le matériau rebondissant sur la sphère.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_cCrIarAzTFKxQJ0tOciSyQ.gif)
_Glissez-déposez le matériau Bouncy dans la Sphère_

C'est tout ! 🎉 Cette étape confirme que la sphère rebondira sur le sol.

## Étape 9 : Appuyez sur le bouton Lecture

En haut du panneau Game, vous trouverez le bouton de lecture. Cliquez dessus et la balle commencera à rebondir. 

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_c0PLeoiv2A4LRUgu7s_zKw.gif)
_Notre balle rebondit maintenant. Youpi !_

Remarquez comment le rebond s'arrête après un certain temps. C'est un comportement attendu et nous allons le corriger à l'étape suivante.

## Étape 10 : Comment changer les propriétés du matériau "Bouncy"

Différentes balles rebondissent différemment. Vous pouvez contrôler le nombre de fois où la balle rebondit. Essayez d'expérimenter avec différentes propriétés du matériau "Bouncy". 

Sélectionnez le matériau "Bouncy" dans le dossier Materials et essayez de changer les valeurs des propriétés. Si vous voulez que la balle rebondisse pour toujours, définissez la valeur de Bounce Combine sur Maximum.

![Image](https://www.freecodecamp.org/news/content/images/2021/05/1_aH8Epn0bCvlrZEy-nn6WJQ.gif)
_Définit la valeur de Bounce Combine sur Maximum et notre balle ne s'arrêtera pas de rebondir_

D'accord. Maintenant, faisons en sorte que cette balle ressemble à un vrai ballon de basket. 

## Étape 11 : Comment créer un dossier qui contiendra toutes vos textures

Pour garder les choses organisées, créons un dossier qui contiendra toutes les textures.

Pour ce faire, allez dans le panneau des actifs et créez un nouveau dossier appelé "Textures". C'est ici que nous stockerons toutes nos textures.

![Clic droit dans le panneau des actifs. Ensuite, sélectionnez Créer. Ensuite, sélectionnez Dossier. Nommez-le "Textures"](https://www.freecodecamp.org/news/content/images/2021/05/2.gif)
_Clic droit dans le panneau des actifs > Créer > Dossier > Nommez-le "Textures"_

## Étape 12 : Comment télécharger une texture

Puisque nous avons besoin d'une texture pour un ballon de basket, téléchargez-en une simplement en ligne. Une texture est juste une image au format .png ou .jpg. Pour l'instant, vous pouvez télécharger la texture de ballon de basket ici :

%[https://www.robinwood.com/Catalog/FreeStuff/Textures/TexturePages/BallMaps.html]

Assurez-vous d'avoir la licence appropriée pour utiliser une texture que vous téléchargez. Les textures ci-dessus sont libres d'utilisation.

## Étape 13 : Comment déposer la texture dans votre projet Unity

Glissez-déposez simplement les textures dans le dossier Textures comme montré ci-dessous👋

![Image](https://www.freecodecamp.org/news/content/images/2021/05/3.gif)
_Glissez-déposez la texture téléchargée dans le dossier "Textures" que vous avez créé à l'étape 1 ci-dessus._

## Étape 14 : Comment appliquer la texture téléchargée à la sphère

Sélectionnez la sphère pour voir toutes ses propriétés dans le panneau Inspecteur. Ensuite, glissez-déposez la texture "BasketballColor" dans la boîte carrée sur le côté gauche de la propriété Albedo.

![Glissez-déposez la texture téléchargée dans la boîte à gauche de la propriété Albedo.](https://www.freecodecamp.org/news/content/images/2021/05/4.gif)
_Glissez-déposez la texture téléchargée dans la boîte à gauche de la propriété Albedo._

Vous avez réussi à utiliser des matériaux et des textures pour créer un ballon de basket. Maintenant, vous pouvez faire de même pour tous vos jeux ou expériences AR/VR que vous développez.

Différents types de balles se comportent différemment. Essayez d'expérimenter avec le rebond et d'ajuster les différents paramètres du composant Rigid Body attaché à la sphère pour créer une balle de golf, un ballon de football ou une balle de tennis.

Amusez-vous !👋🏻

%[https://buymeacoffee.com/knightcube]

### Vous pouvez me contacter sur les réseaux sociaux ici :

* Twitter id : [@knightcube](https://twitter.com/knightcube)
* [Abonnez-vous à ma chaîne YouTube pour en savoir plus sur la RA/RV](https://www.youtube.com/channel/UCvB2-KQUEwXSrzX4-lhEfPg?sub_confirmation=1)
* Lisez plus d'articles [sur mon profil Medium ici](https://knightcube.medium.com/)