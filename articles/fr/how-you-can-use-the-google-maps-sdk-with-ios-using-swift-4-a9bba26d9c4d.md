---
title: Votre guide ultime pour le SDK Google Maps sur iOS, en utilisant Swift 4
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-26T03:16:01.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-use-the-google-maps-sdk-with-ios-using-swift-4-a9bba26d9c4d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*0ONsJHjgFTW1SF_amzDM6g.jpeg
tags:
- name: iOS
  slug: ios
- name: ios app development
  slug: ios-app-development
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
seo_title: Votre guide ultime pour le SDK Google Maps sur iOS, en utilisant Swift
  4
seo_desc: 'By Dejan Atanasov

  Many iOS apps use Google Maps. This is a very common feature, so I have decided
  to prepare an ultimate guide on the Google Maps SDK for iOS. This tutorial covers
  everything that you might need to know.

  I hope that my readers will re...'
---

Par Dejan Atanasov

De nombreuses applications iOS utilisent Google Maps. Il s'agit d'une fonctionnalité très courante, j'ai donc décidé de préparer un guide ultime sur le SDK Google Maps pour iOS. Ce tutoriel couvre tout ce que vous devez savoir.

J'espère que mes lecteurs demanderont des fonctionnalités, afin que je puisse développer cet article. Tout sera documenté dans ce post ! ?

### Installation

Avant de commencer à coder, nous devons d'abord installer le SDK Google Maps iOS. Vous préférerez peut-être un autre gestionnaire de dépendances, mais je recommande [CocoaPods](https://cocoapods.org/).

Créez un Podfile à l'intérieur du répertoire racine de votre projet et copiez le code suivant :

```
source 'https://github.com/CocoaPods/Specs.git'target 'NOM_DE_VOTRE_CIBLE' do  pod 'GoogleMaps'end
```

Tout ce que vous avez à faire est de remplacer la chaîne NOM_DE_VOTRE_CIBLE par une valeur réelle. Enregistrez le fichier et fermez-le. Ouvrez le terminal et accédez au répertoire racine du projet, puis tapez `pod install`. C'est tout ! ?

### Obtenir une clé API

Pour utiliser le SDK Google Maps iOS, vous aurez besoin d'une clé API. Pour générer la clé, vous devrez visiter la [Console Google API](https://console.developers.google.com/flows/enableapi?apiid=maps_ios_backend&reusekey=true).   
Créez un projet et accédez à « Identifiants ».

Ensuite, cliquez sur « Générer des identifiants » et choisissez Clé API. Vous devrez fournir l'identifiant de bundle de votre projet. La clé est générée par l'identifiant de bundle unique, donc si celui-ci est modifié, les services Google Maps **ne fonctionneront pas** !

Accédez à votre projet et, dans votre classe `AppDelegate.swift`, ajoutez `import GoogleMaps`. Ensuite, copiez le code suivant dans `application(_:didFinishLaunchingWithOptions:)`

```
GMSServices.provideAPIKey("VOTRE_CLE_API")
```

### `Étape 1 — Ajouter une carte`

Je vais commencer par vous montrer comment configurer la carte avec un marqueur de base. Le code que vous verrez ici est testé en parallèle pendant que j'écris.

Commençons ! ?

Visitez votre UIViewController (où vous devez ajouter la carte). Créez une UIView personnalisée avec la taille dont vous avez besoin. Assignez la classe `GMSMapView` en tant que **Classe personnalisée** à la UIView (voir la capture d'écran ci-dessous). N'oubliez pas non plus de connecter le délégué.

![Image](https://cdn-media-1.freecodecamp.org/images/1*zb3cuSmzcs1byI9_wNw6rA.png)

#### Enfin, du code !

Revenons au UIViewController et écrivons du code. 
Dans l'extrait ci-dessous, j'ai ajouté toute la classe pour que vous puissiez mieux comprendre ce qui se passe.

`GMSCameraPosition` indique à la carte quelles coordonnées prendre comme point central. Pour afficher un marqueur simple sur la carte, utilisez la fonction `showMarker()`.

À la fin du fichier, ajoutez une [extension](http://theappspace.com/i-%E2%9D%A4-swift-part-1-organize-uiviewcontroller-classes-by-using-extensions/) qui « stockera » les méthodes `GMSMapViewDelegate` dont nous avons besoin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PljEkFaSEt10AzemQsFlzg.png)

### Étape 2 — Méthodes du délégué

Je vais maintenant vous présenter certaines méthodes `GMSMapViewDelegate` et leurs fonctionnalités. 

#### InfoWindow GMSMarker

Dans Google Maps, une InfoWindow est une fenêtre contextuelle avec des informations supplémentaires sur un lieu donné. Elle s'affiche lorsque l'utilisateur appuie sur le marqueur que nous avons ajouté ci-dessus.

Notre InfoWindow est personnalisable. Vous pouvez attacher votre propre UIView avec les composants dont vous avez besoin.

J'ai écrit un exemple d'implémentation. Cela suppose que dans la plupart des cas, les gens utiliseront une InfoWindow personnalisée,

* `didTapInfoWindowOf()` détecte lorsque l'utilisateur appuie sur l'InfoWindow.
* `markerInfoWindow()` ajoute la UIView personnalisée que nous voulons afficher sur le marqueur.
* `didLongPressInfoWindowOf()` détecte lorsque l'InfoWindow a été pressée longtemps.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B1__Cl82zpZ2U4QJ0RsMkw.png)

#### Glisser le GMSMarker

Une autre fonctionnalité intéressante dans GMSMapViewDelegate est la possibilité de faire glisser le marqueur. Cela peut être réalisé avec une quantité minimale de code.

Tout ce que vous avez à faire est d'activer le « commutateur », en appelant `marker.isDragabble=true` sur le marqueur créé ci-dessus.

Pour faire glisser le marqueur, vous devrez utiliser une pression longue. Si vous devez être notifié lorsque l'utilisateur commence et termine le glissement, vous pouvez implémenter ces trois méthodes de délégué :

* `didBeginDragging` notifie une fois — lorsque le glissement a commencé.
* `didDrag` notifie pendant que le marqueur est en cours de glissement.
* `didEndDragging` notifie une fois — lorsque le glissement est terminé.

#### Position du GMSMarker

Et si vous devez changer la position du `GMSMarker` pendant que l'utilisateur appuie sur la carte ? Eh bien, `GMSMapViewDelegate` offre également une solution pour cela. Une seule méthode de délégué peut intercepter les coordonnées (latitude et longitude) de la zone appuyée. Elle attribuera ensuite leurs valeurs au marqueur.

* `didTapAt()` retourne la coordonnée de la zone appuyée sur la carte

### Étape 3 — Ajout de formes

Le SDK Google Maps iOS simplifie le dessin de formes. Je vais couvrir comment dessiner avec des polylignes, des polygones et des cercles.

#### Polylignes

Les formes peuvent être construites à l'aide de lignes. Nous pouvons dessiner des lignes dans Google Maps en utilisant des 'polylignes'. L'objet qui nous aidera à dessiner s'appelle `GMSPolyline`.

Pour créer une polyligne, vous devrez créer un chemin en utilisant `GMSMutablePath`. Il a besoin de deux points ou plus pour commencer à créer un chemin.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8QR6Xcs9Z9kG2L50hWMBsw.png)

Si vous avez utilisé l'exemple ci-dessus, vous obtiendrez une forme rectangulaire comme celle illustrée.

**Quelques autres conseils utiles :**

* Pour supprimer une polyligne de la carte, appelez `mapView.clear()`.
* Vous pouvez changer la couleur de la ligne en utilisant `polyline.strokeColor=.black`.
* Changez la largeur de la ligne en appelant `polyline.strokeWidth=3`.

#### Polygone

Le polygone est presque identique aux polylignes. Il fonctionne selon la même approche, avec quelques différences mineures.

Par exemple, `GMSPolygon` dessine une forme. Vous pouvez ensuite utiliser `fillColor` pour remplir la zone dessinée. Voici un exemple de ce à quoi cela ressemble.

![Image](https://cdn-media-1.freecodecamp.org/images/1*79iM1lo6ICzmy5DmJM43kA.png)

#### Rayon (cercle)

La dernière forme que nous allons examiner est un cercle. Il s'agit probablement de la forme la plus facile de toutes, car elle est toujours la même !

Pour y parvenir, nous devons utiliser la classe `GMSCircle`. Ici, nous ne passons pas de chemin. Au lieu de cela, nous utilisons une coordonnée pour spécifier le centre du cercle. Nous définissons également un rayon (mesuré en mètres).

![Image](https://cdn-media-1.freecodecamp.org/images/1*l41eb5zRtfO-1QWiYlKBWw.png)

La classe `GMSCircle` contient les mêmes propriétés que le polygone, y compris `fillColor`, `strokeColor` et `strokeWidth`.

### Étape 4 — Propriétés et paramètres

Cette partie couvrira quelques propriétés et paramètres souvent utilisés lors de l'utilisation de Google Maps dans votre application. Examinons-les.

#### Changer l'icône du marqueur

Le `GMSMarker` contient deux propriétés différentes pour changer l'icône du marqueur.

* `marker.icon=UIImage(named: "image.png")` dans cette approche, vous passez un nom de fichier d'image. Cela remplace celui par défaut.
* `marker.iconView=customView` Vous pouvez également ajouter une vue personnalisée au lieu d'une image. Cela peut être utilisé pour des marqueurs plus complexes. Par exemple, vous pouvez vouloir ajouter une animation ou plusieurs composants (au lieu d'une seule image). Notez que la propriété `icon` est écrasée lorsque `iconView` est appelée.

#### Ajouter le bouton 'Ma position'

Le bouton 'Ma position' apparaît dans le coin inférieur droit. Cliquer sur le bouton animera la carte pour montrer la position actuelle de l'utilisateur.

Pour ajouter cela, définissez `mapView.settings.myLocationButton = true`. Le bouton apparaîtra.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EgK9Q4dvn3-IuGOvOvvOtw.png)

#### Contrôles de zoom

Le SDK Google Maps pour iOS ne fournit pas de contrôles de zoom intégrés (mais le SDK Android le fait). Vous devrez écrire votre propre logique à la place.

Tout ce que vous avez à faire est d'ajouter deux boutons avec les icônes '+' et '-'. Lorsqu'ils sont appuyés, ceux-ci appelleront `mapView.animate(toZoom: zoom)`.

#### Contrôler les gestes

Vous pouvez activer ou désactiver n'importe quel geste que vous pouvez voir sur la carte. Par exemple, vous pouvez vouloir désactiver le zoom ou désactiver le défilement.

Il y a un total de quatre gestes disponibles pour vous :

```
mapView.settings.scrollGestures = falsemapView.settings.zoomGestures   = falsemapView.settings.tiltGestures   = falsemapView.settings.rotateGestures = false
```

J'espère que vous avez apprécié ce tutoriel. Si vous souhaitez en savoir plus sur le SDK Google Maps pour iOS, écrivez-moi un commentaire. Je serais très heureux de développer ce tutoriel avec vos demandes.

#### C'est tout pour ce tutoriel et s'il vous a aidé, veuillez ? ou partager cette histoire pour que d'autres comme vous puissent la trouver. Merci pour votre attention ! ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*5-oC2BqqizoRxIls08WMmA.png)

#### Découvrez mon dernier projet :

[**1x2 BET - Conseils et cotes de football**](https://apple.co/2EIiDpI)  
[_COTES CHAUDES Chaque jour, nous générons une liste des cotes les plus chaudes au monde. Ce sont des cotes qui ont le plus baisséapple.co](https://apple.co/2EIiDpI)

#### Lisez plus de mes écrits sur Medium :

[**Présentation de l'architecture Clean Swift (VIP)**](https://hackernoon.com/introducing-clean-swift-architecture-vip-770a639ad7bf)  
[_Oubliez MVC, maintenant !_hackernoon.com](https://hackernoon.com/introducing-clean-swift-architecture-vip-770a639ad7bf)[**Votre guide ultime pour le SDK Google Maps sur iOS, en utilisant Swift 4**](https://medium.freecodecamp.org/how-you-can-use-the-google-maps-sdk-with-ios-using-swift-4-a9bba26d9c4d)  
[_De nombreuses applications iOS utilisent Google Maps. Il s'agit d'une fonctionnalité très courante, j'ai donc décidé de préparer un guide ultime sur lemedium.freecodecamp.org](https://medium.freecodecamp.org/how-you-can-use-the-google-maps-sdk-with-ios-using-swift-4-a9bba26d9c4d)[**SWIFT — Custom UIView avec fichier XIB**](https://medium.com/theappspace/swift-custom-uiview-with-xib-file-211bb8bbd6eb)  
[_Custom UIView avec fichier XIB est une pratique très courante dans le développement iOS. Les classes Custom UIView ne contiennent pas de fichiers XIBmedium.com](https://medium.com/theappspace/swift-custom-uiview-with-xib-file-211bb8bbd6eb)[**Comment ajouter la prise en charge de Spotlight à votre application iOS**](https://hackernoon.com/how-to-add-spotlight-support-to-your-ios-app-4a89054aff89)  
[_Un tutoriel Swift qui rendra votre application disponible dans la recherche Spotlight_hackernoon.com](https://hackernoon.com/how-to-add-spotlight-support-to-your-ios-app-4a89054aff89)[**Relations Core Data**](https://hackernoon.com/core-data-relationships-d813ed66ba8c)  
[_Comprendre les relations un-à-un et un-à-plusieurs_hackernoon.com](https://hackernoon.com/core-data-relationships-d813ed66ba8c)[**Comprendre Auto Layout dans Xcode 9**](https://hackernoon.com/understanding-auto-layout-in-xcode-9-2719710f0706)  
[_Tout ce que vous devez savoir sur Auto Layout_hackernoon.com](https://hackernoon.com/understanding-auto-layout-in-xcode-9-2719710f0706)

#### Abonnez-vous à ma newsletter :