---
title: Comment utiliser SnapKit pour écrire des contraintes de manière programmatique
  pour les applications iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-14T21:13:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-snapkit-to-write-constraints-programmatically-for-ios-apps-ce0a6d9e76cf
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mLxT0gEiltVrN8rS_zKLWg.jpeg
tags:
- name: iOS
  slug: ios
- name: iphone
  slug: iphone
- name: mobile app development
  slug: mobile-app-development
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
seo_title: Comment utiliser SnapKit pour écrire des contraintes de manière programmatique
  pour les applications iOS
seo_desc: 'By Jake Shelley

  When I first started building apps with Xcode, I thought Storyboards were magic.
  Dragging and dropping subviews into place was so simple, I never understood how
  people built views without them.

  Eventually, I decided that to become a “...'
---

Par Jake Shelley

Lorsque j'ai commencé à construire des applications avec Xcode, je pensais que les Storyboards étaient magiques. Glisser-déposer des sous-vues en place était si simple que je ne comprenais pas comment les gens construisaient des vues sans eux.

Finalement, j'ai décidé que pour devenir un « maître programmeur », je devrais apprendre à construire des vues de manière programmatique. Un problème : écrire des contraintes en code est une corvée.

```
let horizontalConstraint = NSLayoutConstraint(   item: newView,    attribute: NSLayoutAttribute.centerX,    relatedBy: NSLayoutRelation.equal,    toItem: view,    attribute: NSLayoutAttribute.centerX, multiplier: 1, constant: 0)
```

C'est une contrainte horizontale qui centrera une sous-vue sur l'axe X de sa supervue. Pas très facile à lire, et écrire cela pour chaque contrainte devient rapidement fastidieux. Pourtant, je voulais abandonner les storyboards, alors j'ai cherché une alternative. C'est alors que j'ai découvert [SnapKit](http://github.com/SnapKit/SnapKit).

SnapKit dispose d'une API claire et concise qui facilite l'écriture de contraintes en code. Je vais passer en revue quelques exemples très basiques de ce qui peut être fait avec SnapKit.

Je vais aborder :

1. **Disposer une sous-vue dans sa supervue**
2. **Disposer des sous-vues les unes par rapport aux autres**
3. **Mettre à jour et animer des contraintes**

#### Installation

Assurez-vous de télécharger SnapKit dans votre projet. J'utilise [Cocoapods](http://cocoapods.org/) pour les bibliothèques tierces.

Ajoutez `pod 'SnapKit'` à votre Podfile et exécutez `pod install`. Maintenant, écrivez `import SnapKit` en haut du fichier dans lequel vous souhaitez l'utiliser.

#### Disposer une sous-vue dans sa supervue

Tout d'abord, je vais épingler une sous-vue aux bords de sa supervue :

```
let subview = UIView()view.addSubview(subview)
```

```
subview.snp.makeConstraints { (make) in    make.top.equalTo(view)    make.bottom.equalTo(view)    make.left.equalTo(view)    make.right.equalTo(view)}
```

Cela définira des contraintes pour les bords supérieur, inférieur, gauche et droit de la sous-vue aux bords correspondants de sa supervue avec une constante de 0.

![Image](https://cdn-media-1.freecodecamp.org/images/6yjMwrwbqTmK5U3NaVcIAByRqmnbomeAXIqO)
_La sous-vue épinglée aux bords de sa supervue avec une constante de 0_

Remarquez que j'ajoute la sous-vue à la supervue avant de définir les contraintes de la sous-vue. Si vous écrivez des contraintes pour des vues qui ne sont pas déjà ajoutées à la supervue, cela provoquera une erreur fatale à l'exécution lorsque la vue se chargera.

La syntaxe de SnapKit est déjà beaucoup plus lisible que celle de la bibliothèque standard, mais elle peut être raccourcie. SnapKit offre une manière encore plus concise de contraindre une vue aux bords de sa supervue :

```
let subview = UIView()view.addSubview(subview)
```

```
subview.snp.makeConstraints { (make) in    make.top.bottom.left.right.equalTo(view)}
```

Cela disposera ma sous-vue de la même manière que le code ci-dessus, mais avec une ligne au lieu de quatre.

Je peux également contraindre la taille de ma sous-vue. Ci-dessous, je vais définir la hauteur et la largeur de la sous-vue et la centrer dans sa supervue :

```
subview.snp.makeConstraints { (make) in    make.width.equalTo(200)    make.height.equalTo(200)    make.centerX.equalTo(view)    make.centerY.equalTo(view)}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1iMgmnVQPYYYmiv9mn7NWSe8sxRWAmsmuuMp)

Cet exemple est assez simple, mais je me suis répété beaucoup. Lorsque je définis des contraintes qui ont les mêmes valeurs, SnapKit me permet de chaîner les contraintes ensemble comme ceci :

```
subview.snp.makeConstraints { (make) in    make.width.height.equalTo(200)    make.centerX.centerY.equalTo(view)}
```

Ce bloc résultera en les mêmes contraintes que celui ci-dessus. Juste une autre façon dont SnapKit aide à écrire un code plus propre.

#### Disposer des sous-vues les unes par rapport aux autres

Lorsque vous ajoutez plusieurs sous-vues à une seule vue, il est probable que vous souhaitiez disposer les sous-vues les unes par rapport aux autres. Dans cet exemple, je vais :

1. Ajouter `subview1` et la contraindre au bord gauche de sa supervue
2. Ajouter `subview2` et la contraindre au bord droit de `subview1`

```
let subview1 = UIView()let subview2 = UIView()view.addSubview(subview1)view.addSubview(subview2)
```

```
subview1.snp.makeConstraints { (make) in    make.width.height.equalTo(100)    make.left.equalTo(view)}
```

```
subview2.snp.makeConstraints { (make) in    make.width.height.equalTo(subview1)    make.left.equalTo(subview1.snp.right)}
```

Jusqu'à présent, je voulais que mes contraintes soient égales à la contrainte correspondante pour la vue relative. Par exemple, dans `make.left.equalTo(view)`, SnapKit définit le `left` de `subview1` sur le `left` de `view`. SnapKit correspondra automatiquement à la contrainte que je définis si je ne précise pas autrement.

Pour la contrainte `left` de `subview2`, je veux la définir sur le bord `right` de `subview1`. Si j'écrivais `make.left.equalTo(subview1)`, SnapKit définirait le bord `left` de `subview2` sur le bord `left` de `subview1`. Au lieu de cela, j'utilise le bord `right` de `subview1` que je récupère en écrivant `subview1.snp.right`.

Je peux accéder à n'importe quelle contrainte de la disposition d'une vue en ajoutant `snp` comme vu ci-dessus.

![Image](https://cdn-media-1.freecodecamp.org/images/-eQjim0SnilZW2c4hsPgWQomS2TOoC44bzkt)
_subview 2 est contrainte à droite de subview 1 avec une constante de 0_

Maintenant que j'ai `subview2` à droite de `subview1`, je vais créer un espace entre elles en ajoutant un **décalage** à `subview2`.

```
subview2.snp.makeConstraints { (make) in    make.width.height.equalTo(subview1)    make.left.equalTo(subview1.snp.right).offset(50)}
```

Un décalage peut être ajouté à la fin de n'importe quel `equalTo()` pour changer la constante de cette contrainte. Maintenant, `subview2` aura une constante de 50 sur sa contrainte `left`.

![Image](https://cdn-media-1.freecodecamp.org/images/12PDwNisgHOscWhDRBx45lwmW5ysGD-6D7Am)
_subview 2 est maintenant contrainte à subview 1 avec une constante de 50_

#### Mettre à jour et animer des contraintes

Si vous voulez que votre application soit la #ProchaineGrosseChose, tout le monde sait que vous devrez ajouter un peu de panache ! SnapKit offre un moyen de mettre à jour facilement les contraintes pour créer des vues dynamiques.

Mettre à jour une contrainte avec SnapKit est presque identique à en ajouter une nouvelle. Ici, je vais mettre à jour la contrainte pour `subview1` de l'exemple précédent en changeant la constante de la contrainte du bord `left` de 0 à 50 :

```
subview1.snp.updateConstraints { (make) in   make.left.equalTo(50)}
```

Et c'est tout ! Ma sous-vue sera mise à jour avec les nouvelles contraintes lorsque le bloc de code sera exécuté.

![Image](https://cdn-media-1.freecodecamp.org/images/iY07Gepf4N4TE7b3iRQ-FEy-S8CZgoPklpMO)
_Cliquer sur le bouton met à jour les contraintes de subview1_

Vous avez probablement remarqué que `subview2` a bougé lorsque j'ai mis à jour `subview1` même si je n'ai pas mis à jour ses contraintes. `subview2` est contrainte au bord droit de `subview1`. Lorsque `subview1` est déplacée, `subview2` continuera à honorer la contrainte gauche qu'elle a avec `subview1`.

Maintenant, je vais ajouter une animation pour fluidifier la transition. Si vous avez déjà animé une vue auparavant, cette syntaxe vous sera familière :

```
UIView.animate(withDuration: 0.3) {    subview1.snp.updateConstraints { (make) in        make.left.equalTo(50)    }        self.view.layoutIfNeeded()}
```

Lorsque j'anime des mises à jour sur mes contraintes, je dois appeler `layoutIfNeeded()` sur le parent de la sous-vue. Si j'anime plus d'une vue à la fois, je devrai appeler `layoutIfNeeded()` sur la supervue commune la plus proche des sous-vues.

![Image](https://cdn-media-1.freecodecamp.org/images/sYlCU5J2zYlN5if4W5au2V8RMVkrWwj6Hj4Z)

`updateConstraints()` ne peut mettre à jour que les contraintes existantes. Tentative de mise à jour d'une contrainte qui n'est pas déjà en place entraînera une erreur fatale à l'exécution.

Si vous souhaitez ajouter de nouvelles contraintes à votre sous-vue, utilisez `remakeConstraints()`. `**remakeConstraints()**` **supprimera toutes les contraintes existantes que vous avez définies sur cette sous-vue** et vous permettra d'en ajouter de nouvelles.

Vous pouvez également utiliser `deactivate()` pour supprimer une contrainte. Ci-dessous, je crée, définis et supprime une contrainte en utilisant `deactivate()` :

```
var constraint: Constraint!let subview = UIView()
```

```
subview.snp.makeConstraints { (make) in    constraint = make.height.equalTo(100).constraint}
```

```
constraint.deactivate()
```

Vous pouvez également animer la suppression d'une contrainte en la désactivant à l'intérieur d'un bloc d'animation.

Vous êtes maintenant un maître de l'écriture de contraintes de manière programmatique. Les storyboards semblent être une blague maintenant et il n'y a aucune raison de revenir à eux, n'est-ce pas ?

![Image](https://cdn-media-1.freecodecamp.org/images/RrxxmZ0RENDVaxHMS4-fBOJoeB7xGJF1OIQ8)
_Comment on se sent en construisant des storyboards après avoir lu ce guide_

Pas vraiment. Les storyboards et les nibs sont toujours le moyen le plus rapide de mettre en place un contrôleur de vue, et, si vous travaillez avec des non-développeurs, ils sont le meilleur moyen de montrer à quoi ressemblera l'application sans envoyer une version bêta.

Personnellement, j'utilise les deux. Dans [la dernière application que j'ai construite](https://github.com/JakeShelley1/Todo-List-App-Swift/), j'ai ajouté des contraintes à la fois en code avec SnapKit et en utilisant Auto Layout sur les storyboards et les nibs, parfois sur la même vue. En fin de compte, vous devrez décider ce qui fonctionne le mieux pour la vue que vous construisez.

_Merci beaucoup d'avoir lu ! Si vous avez aimé cet article, suivez-moi sur [Twitter](https://twitter.com/JakeShelley3) où je poste des articles sur la gestion de produit, l'ingénierie et le design._