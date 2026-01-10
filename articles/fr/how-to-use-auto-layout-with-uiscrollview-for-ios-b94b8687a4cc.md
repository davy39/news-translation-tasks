---
title: Comment utiliser Auto Layout avec UIScrollView pour iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T16:16:06.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-auto-layout-with-uiscrollview-for-ios-b94b8687a4cc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rWN6HdC61ChO2dNs8W8wEQ.jpeg
tags:
- name: Design
  slug: design
- name: ios app development
  slug: ios-app-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Auto Layout avec UIScrollView pour iOS
seo_desc: 'By Sam Ollason

  I love building tools with software, and that is why I am currently the Lead Developer
  for Green 13 Solutions.

  Recently I have been having lots of fun using Swift and the Interface Builder in
  Xcode to create iOS apps.

  I ran into some c...'
---

Par Sam Ollason

J'adore construire des outils avec des logiciels, et c'est pourquoi je suis actuellement le Développeur Principal pour [Green 13 Solutions](http://irisd.green13solutions.com/).

Récemment, je me suis beaucoup amusé à utiliser Swift et l'Interface Builder dans Xcode pour créer des applications iOS.

J'ai rencontré quelques défis lorsque j'ai essayé de créer une **scène** où les utilisateurs peuvent **faire défiler** pour voir le contenu qui dépasse de la **vue de contenu** actuelle. Le contenu ne défilait pas correctement et le texte n'était pas automatiquement affiché correctement pour différentes tailles d'écran.

Voici quelques notes pour mon futur moi pour référence. J'espère que vous les trouverez utiles également !

Voici un [dépôt](https://github.com/SamOllason/autolayout-scrollview-example) pour le projet si vous souhaitez voir l'exemple complet.

### Ce que nous allons construire

Notre application aura une seule page. La page contiendra du texte et les utilisateurs pourront faire défiler vers le bas pour voir le texte qui dépasse de leur vue de contenu actuelle.

Nous utiliserons l'Interface Builder dans Xcode pour ajouter un objet UIScrollView, un objet UIView imbriqué et ensuite un objet UITextView imbriqué. Nous utiliserons l'Interface Builder pour ajouter des contraintes à ces éléments. Les contraintes permettront à Auto Layout d'activer le défilement correctement et la vue de texte apparaîtra automatiquement correctement sur différentes tailles d'écran.

### Un peu d'informations de fond rapide (jeu de mots intentionnel)

L'objet UIScrollView peut être utilisé comme un objet parent pour d'autres éléments UIKit tels que UIView et UITextView.

Faire cela signifie que tous les objets enfants peuvent **avoir leur origine déplacée collectivement** par rapport à la **vue de contenu** qui est montrée à l'utilisateur. Cela signifie que le comportement de 'défilement' fonctionne comme les utilisateurs s'y attendent. Un autre avantage est que Auto Layout dimensionnera correctement nos éléments sur différents écrans comme prévu.

Nous utilisons les termes 'UIScrollView' et 'Scroll View' de manière interchangeable ci-dessous, et de même pour View et Text View.

Voici les étapes à suivre.

### Ajout de la Vue

Créez un nouveau projet et sélectionnez 'Single View App'. Si vous cliquez sur Main.storyboard, vous verrez que nous avons une scène avec un élément View vide.

### Ajout de la Scroll View

Faites glisser un élément UI Scroll View de la bibliothèque d'objets dans la scène. Ensuite, ajoutez les contraintes montrées dans l'image ci-dessous pour ancrer l'élément Scroll View aux bords de sa zone sécurisée parente.

![Image](https://cdn-media-1.freecodecamp.org/images/Jhaxfl2emel8kPk8TwfmUSLlJSoPciBhfibi)

### Ajout d'un élément Vue

Utilisez la bibliothèque d'objets pour faire glisser un élément Vue dans la scène. La Vue sera le conteneur parent pour notre élément Text View.

Redimensionnez manuellement l'élément Vue avec votre curseur pour qu'il remplisse la largeur de l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/MKboKx-1Pr9cG-z5Po9jigJc6BK01-TororP)
_Élément Vue redimensionné manuellement pour s'adapter à la largeur_

### Ancrage de la Vue à la Scroll View

Cliquez sur l'élément Vue dans la hiérarchie des objets et faites glisser+relâchez votre curseur sur l'élément Scroll View au-dessus dans la hiérarchie. Cliquez sur les 4 options supérieures pour appliquer ces contraintes. Cliquez sur 'Equal Widths' pour appliquer également cette contrainte.

**Pourquoi ?** Contraindre la Vue de cette manière signifie qu'un élément Text View enfant que nous ajoutons fonctionne correctement avec Auto Layout. Cela se produit parce que nous contraignons la Text View au bas de la Vue (que nous avons correctement ancrée au bas de la Scroll View !) au lieu de directement au bas de la Scroll View.

Vous verrez que les guides de mise en page dans l'Interface Builder sont rouges car il y a une autre erreur. Nous allons corriger cela sous peu.

![Image](https://cdn-media-1.freecodecamp.org/images/cGgPMQiJhTMXXpSUXQYKFP9uiKqDNkonUiJw)
_Ajoutez ces contraintes à l'élément Vue_

### Ajout de la Text View en tant qu'enfant de la Vue

Ajoutez un élément Text View à l'intérieur de l'élément Vue dans la scène.

### Ajout de contraintes à la Text View

Ajoutez les contraintes de l'image ci-dessous à la Text View.

**Pourquoi ?** Cela contraindra la Text View par rapport à l'objet Vue qui l'entoure.

![Image](https://cdn-media-1.freecodecamp.org/images/NhKkvtmYB37I7gGULPDI-a7idl2KWN7mlcex)
_Ajout de contraintes à la Text View_

### Désactiver le comportement de défilement dans la Text View

Vous devriez avoir un écran similaire à celui ci-dessous. Vous pouvez voir qu'il y a encore beaucoup de rouge dans l'Interface Builder.

Vous pouvez supprimer ces avertissements en sélectionnant l'élément Text View et **en désélectionnant 'Scrolling Enabled' dans le panneau de l'éditeur** sur le côté droit.

![Image](https://cdn-media-1.freecodecamp.org/images/C2yKd3qiiQtqIVmO4A5FV7oCpMuB9KyFaevK)
_Désélectionnez 'Scrolling Enabled' à droite pour supprimer ces erreurs rouges_

Notez que nous aurons toujours un comportement de défilement avec cette approche, mais **ce sera la Scroll View parente qui sera réellement déplacée, et non l'élément Text View individuel**. C'est la même chose qu'une feuille qui ne bouge sur une rivière que parce que la rivière qui l'entoure bouge !

C'est légèrement subtil mais assez important à comprendre car cela sous-tend toute la solution.

![Image](https://cdn-media-1.freecodecamp.org/images/JjCnsnOxlF0Cp5akdGf9wDrOvWUexcPe9jXd)
_Notre approche signifie qu'une Text View ne défile que parce qu'une Scroll View la déplace — comme une feuille ne bouge que parce que la rivière qui l'entoure la déplace_

### Enfin

Ajoutez plus de contenu à la Text View. Vous devriez voir que le défilement fonctionne comme prévu et que la Text View apparaît correctement sur différentes tailles d'écran.

C'est la beauté d'Auto Layout !

![Image](https://cdn-media-1.freecodecamp.org/images/YuajWxyO9HnRMGpONlOhgGA7iXZ5wOajtCqL)
_Capture d'écran de la Text View défilée utilisant le simulateur Xcode_

Voici un [dépôt](https://github.com/SamOllason/autolayout-scrollview-example) pour le projet si vous souhaitez voir l'exemple complet.

Toutes les informations sur les rouges-gorges pour le contenu de la Text View proviennent directement de [Wikipedia](https://en.wikipedia.org/wiki/European_robin). Merci à la communauté pour cela.

_Pourquoi les rouges-gorges ?_ Parce que j'adore les oiseaux et les rouges-gorges sont des créatures particulièrement géniales !

Merci d'avoir lu, j'espère que vous avez trouvé cela utile. N'hésitez pas à me faire savoir si vous avez des commentaires ou des questions !