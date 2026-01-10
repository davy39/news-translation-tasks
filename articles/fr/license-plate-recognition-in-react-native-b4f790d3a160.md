---
title: Reconnaissance de plaques d'immatriculation dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-02T07:31:23.000Z'
originalURL: https://freecodecamp.org/news/license-plate-recognition-in-react-native-b4f790d3a160
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XU79Bvq2T-jmpoux2giVJQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: React Native
  slug: react-native
seo_title: Reconnaissance de plaques d'immatriculation dans React Native
seo_desc: 'By Sam Corcos

  Today, we at CarDash are releasing [react-native-openalpr](https://github.com/cardash/react-native-openalpr),
  an open-source React Native package for automatic license plate recognition using
  OpenALPR (iOS-only as of February 2017).

  Eno...'
---

Par Sam Corcos

Aujourd'hui, nous chez [CarDash](https://www.cardash.com) publions `[react-native-openalpr](https://github.com/cardash/react-native-openalpr)`, un package React Native open-source pour la reconnaissance automatique de plaques d'immatriculation utilisant [OpenALPR](https://github.com/openalpr/openalpr) (iOS uniquement en février 2017).

Assez parlé. Voici un GIF de l'[application exemple](https://github.com/cardash/react-native-openalpr/tree/master/Example) (incluse dans le dépôt) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*u1nTJMFc34aDLTPCIr0-cQ.gif)

### Comment utiliser cela dans votre application React Native

Pour installer, suivez les instructions dans la [documentation](https://github.com/cardash/react-native-openalpr). Une fois installé, importez `Camera` depuis `react-native-openalpr` et ajoutez-le à votre projet React Native.

Vous pouvez trouver une liste complète des options dans la [documentation](https://github.com/cardash/react-native-openalpr#options), mais l'option la plus importante est `onPlateRecognized`, qui retourne une `plate` et un pourcentage de `confidence`. Cette fonction est l'endroit où vous placerez la logique pour ce que vous voulez faire une fois que vous reconnaissez une plaque d'immatriculation.

Dans l'exemple ci-dessus, lorsque le `confidence` est supérieur à 90%, `this.state.plate` est défini sur la plaque entrante, qui est ensuite affichée à l'utilisateur. C'est ici que vous pourriez fermer la caméra et déclencher une action Redux si vous êtes satisfait du résultat.

### Comment nous avons construit ce package

Ce package est construit en utilisant [OpenALPR](https://github.com/openalpr/openalpr) et la [compilation iOS associée](https://github.com/twelve17/openalpr-ios). L'échafaudage pour la fonctionnalité de la caméra est basé sur le package populaire `[react-native-camera](https://github.com/lwansbrough/react-native-camera)`.

OpenALPR accepte soit une image statique, soit un flux d'images, et comme reconnaître des images à partir d'un flux est bien plus cool, nous avons décidé d'adopter cette approche. Malheureusement, aucune des bibliothèques de caméra React Native existantes ne donne un accès facile à un flux d'images, nous avons donc dû le construire nous-mêmes.

Puisque nous exécutons un flux d'images à travers un algorithme (OpenALPR), nous devons comprendre comment l'algorithme fonctionne à un niveau basique afin d'optimiser les images que nous lui fournissons.

L'algorithme peut prendre n'importe quelle image, mais lorsqu'il reçoit une image, il va effectuer un certain prétraitement. Donc, si vous voulez être performant, vous devez minimiser le nombre d'opérations que l'algorithme doit exécuter.

#### Qualité de l'image

Une des choses que les algorithmes dans OpenCV et OpenALPR font est de sous-échantillonner (réduire la qualité) de votre image. La détection de base des contours ne nécessite pas une haute résolution. En fait, la haute résolution est souvent l'ennemie de la détection de contours, car elle introduit du bruit. Le sous-échantillonnage agit comme un flou et supprime les détails inutiles.

Sachant que l'algorithme va déjà sous-échantillonner votre image, vous pouvez optimiser vos données d'entrée en passant des images qui sont déjà en basse résolution. Lorsque vous demandez des frames vidéo (tampons de frames), vous pouvez définir la résolution que vous souhaitez recevoir. Dans iOS, vous feriez cela en accédant à un préréglage. `AVSessionPreset` est un paramètre que vous donnez au framework `AVFoundation`, qui vous donne un accès de bas niveau à la caméra.

La plupart des gens utilisent par défaut des images haute résolution, mais puisque vous savez que l'algorithme sous-échantillonne de toute façon, vous pouvez laisser l'appareil photo de l'iPhone faire tout le travail sans coût de calcul plutôt que de traiter une conversion d'image intensive en mémoire après coup.

#### Pixels

Une autre chose que l'algorithme fait est de convertir l'image en niveaux de gris, car les algorithmes de détection de contours fonctionnent mieux dans un plan de couleur en niveaux de gris.

Si vous voulez être malin, vous pouvez choisir un format de pixel non standard. Ordinairement, vos images reviennent en `RGBA`, où R est rouge, G est vert, B est bleu, et A est alpha (opacité). Vous avez peut-être aussi vu `CMYK` (cyan, magenta, jaune et clé) si vous travaillez avec Illustrator ou des matériaux imprimés.

En utilisant `RGBA` comme exemple, chaque pixel est représenté par 0 à 4 octets. Afin d'obtenir une image en niveaux de gris à partir de `RGBA`, vous devriez prendre la moyenne des composants `RGB`, ce qui correspond à 3 lectures, 3 multiplications et 2 additions pour obtenir le niveau de gris.

Voici `Y'CbCr`, où `Y'` est la luminosité et `Cb` et `Cr` sont les couleurs.

> Y est le composant [luma](https://en.wikipedia.org/wiki/Luma_(video)) et CB et CR sont les composants de différence bleue et de différence rouge [chroma](https://en.wikipedia.org/wiki/Chrominance). -Wikipedia

Dans `Y'CbCr`, les données sont encodées différemment. Y prime (`Y'`) est effectivement le même que les informations en niveaux de gris que vous obtiendriez à partir du calcul `RGB` ci-dessus mais ne nécessite pas d'étape de calcul. Donc, si vous spécifiez ce type de pixel, vous économisez du temps de processeur.

C'est, autant que nous le sachions, la manière la plus efficace d'obtenir vos données d'entrée afin qu'elles n'aient pas besoin d'être prétraitées.

#### Orientation

Bien que vous puissiez prendre des images optimisées à ce stade, vous devez toujours gérer l'orientation. Tout algorithme OCR (reconnaissance optique de caractères) doit savoir quelle direction est vers le haut, car les lettres perdent leur sens lorsqu'elles sont à l'envers ou de côté.

La manière native dont l'iPhone prend des images est en mode paysage avec le bouton d'accueil à droite, donc pour faire fonctionner notre algorithme en mode portrait, vous devez reconnaître l'orientation et faire pivoter l'image. Heureusement, il existe une manière efficace de faire cela et OpenCV fournit une méthode efficace pour faire pivoter les images.

#### Mappage des coordonnées

La dernière pièce est de dessiner le rectangle autour d'une plaque d'immatriculation reconnue. Lorsque vous utilisez la caméra native en mode portrait, elle place une boîte aux lettres autour de la sortie de la caméra. Si vous essayez de rendre la caméra plein écran, elle va étirer l'image pour remplir l'espace disponible. Cela s'appelle le "video gravity".

Dans l'image ci-dessous, vous pouvez voir que le téléphone de gauche est en plein écran, ce qui fait que la boîte de WD-40 apparaît légèrement plus grande que sur la caméra de droite, qui est en mode boîte aux lettres.

![Image](https://cdn-media-1.freecodecamp.org/images/1*71BUUolW8CBdaGyJkGSJBw.jpeg)
_Caméra de gauche subissant le video gravity_

Alors, comment mappez-vous les coordonnées de la plaque de l'espace image (système de coordonnées) sur le système de coordonnées de l'écran, en tenant compte du rapport d'ouverture, du rapport d'aspect vidéo et du video gravity ?

La manière de faire cela est de d'abord mapper les coordonnées avec `0,0` en haut à gauche et `1,1` en bas à droite. Si l'orientation est autre que le mode paysage avec le bouton d'accueil à droite, vous devez le calculer légèrement différemment. Ensuite, vous mappez ces coordonnées sur le système de coordonnées de l'écran en utilisant la méthode magique donnée par iOS : `pointForCaptureDevicePointOfInterest`

Cette méthode prend la coordonnée normalisée dans l'espace de coordonnées de l'image et la mappe à une coordonnée dans l'espace de l'écran. Elle prend automatiquement en compte la gravité et tout le reste pour vous.

Et c'est tout.

### Contributeurs

* Evan Rosenfeld - Evan est le fondateur de Avocado Hills et conseiller technique de CarDash.
* [Votre nom ici] - Si vous souhaitez contribuer, envoyez-nous une pull request - surtout si vous êtes un développeur Java intéressé par la construction de notre fonctionnalité Android ?.

_Sam Corcos est le co-fondateur de [CarDash](https://www.cardash.com), un fournisseur de services automobiles complets qui élimine les tracas des services, soins et maintenance automobiles. Il est également l'auteur de [Learn Phoenix](http://learnphoenix.io), et développeur principal et fondateur de [Sightline Maps](http://sightlinemaps.com)._