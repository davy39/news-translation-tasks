---
title: Comment rendre les vues de collection de hauteur dynamique dans vos applications
  iOS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-26T17:45:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-height-collection-views-dynamic-in-your-ios-apps-7d6ca94d2212
coverImage: https://cdn-media-1.freecodecamp.org/images/1*58RjgkbswK_v3ofUG4z_qA.jpeg
tags:
- name: data
  slug: data
- name: General Programming
  slug: programming
- name: Swift
  slug: swift
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment rendre les vues de collection de hauteur dynamique dans vos applications
  iOS
seo_desc: 'By Payal Gupta

  Be dynamic, just like life…


  Table views and collection views have always been an integral part of iOS app development.
  We all might have came across various issues related to them. In this article, we’ll
  discuss one such problem state...'
---

Par Payal Gupta

#### Soyez dynamique, tout comme la vie…

![Image](https://cdn-media-1.freecodecamp.org/images/1*58RjgkbswK_v3ofUG4z_qA.jpeg)

Les vues de tableau et les vues de collection ont toujours été une partie intégrante du développement d'applications iOS. Nous avons tous pu rencontrer divers problèmes liés à celles-ci. Dans cet article, nous discuterons d'un tel problème lié aux vues de collection.

### Énoncé du problème

Supposons que nous avons un `UICollectionView` dans une `UITableViewCell` et environ 20 `UICollectionViewCells` que nous devons rendre verticalement. Nous pouvons définitivement implémenter cela en un clin d'œil avec la source de données donnée.

Voici le véritable énoncé du problème — nous avons besoin que la `UITableViewCell` ajuste sa hauteur dynamiquement selon son contenu. De plus, le `UICollectionView` doit être tel que toutes les cellules soient affichées en une seule fois, c'est-à-dire sans défilement autorisé.

En bref : _rendre tout dynamique…_

![Image](https://cdn-media-1.freecodecamp.org/images/1*QxfoBsPpGFM707gho3k0eA.gif)
_**Vue de collection de hauteur fixe et dynamique**_

### Commençons à coder

Une vue dans iOS calcule sa hauteur à partir de son contenu, à condition qu'aucune contrainte de hauteur ne soit fournie. Il en va de même pour `UITableViewCell`.

Pour l'instant, nous garderons un seul `collectionView` à l'intérieur de notre `tableViewCell` avec ses contraintes `leading, top, trailing et bottom` définies à 0.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KOtsApDTjYA4J2oo-1mRYA.png)
_**Hiérarchie des vues**_

Puisque nous n'avons pas fourni de contrainte de hauteur au `collectionView` et que nous ne connaissons pas non plus sa taille de contenu à l'avance, comment la `tableViewCell` calculera-t-elle sa hauteur ?

#### **Solution**

Le calcul dynamique de la hauteur du `collectionView` en fonction de sa `contentSize` est simplement un processus en 3 étapes.

**1.** Sous-classez `UICollectionView` et remplacez ses méthodes `layoutSubviews()` et `intrinsicContentSize`, c'est-à-dire

Le code ci-dessus invalidera la `intrinsicContentSize` et utilisera la `contentSize` réelle du `collectionView`. Le code ci-dessus prend également en considération la `mise en page personnalisée`.

**2.** Maintenant, définissez `DynamicHeightCollectionView` comme classe du `collectionView` dans le `storyboard`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*w3eFLkfu3BvAg04hj__pPQ.png)

**3.** Une dernière chose, pour que les changements prennent effet : vous devez appeler `layoutIfNeeded()` sur le `collectionView`, après avoir rechargé les données du `collectionView`, c'est-à-dire

```
func configure(with arr: [String]) {   self.arr = arr   self.collectionView.reloadData()   self.collectionView.layoutIfNeeded() //Ici..!!!}
```

Et voilà !

### Projet exemple

Vous pouvez télécharger le projet exemple [ici](https://github.com/pgpt10/DynamicHeightCollectionView).

### Lectures complémentaires

N'oubliez pas de lire mes autres articles :

1. [Tout sur Codable dans Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
2. [Tout ce que vous avez toujours voulu savoir sur les notifications dans iOS](https://medium.freecodecamp.org/ios-10-notifications-inshorts-all-in-one-ad727e03983a)
3. [Copie profonde vs. copie superficielle — et comment vous pouvez les utiliser dans Swift](https://medium.freecodecamp.org/deep-copy-vs-shallow-copy-and-how-you-can-use-them-in-swift-c623833f5ad3)
4. [Coder pour iOS 11 : Comment glisser et déposer dans les collections et les tableaux](https://hackernoon.com/drag-it-drop-it-in-collection-table-ios-11-6bd28795b313)
5. [Tout ce que vous devez savoir sur les extensions Today (Widget) dans iOS 10](https://hackernoon.com/app-extensions-and-today-extensions-widget-in-ios-10-e2d9fd9957a8)
6. [Sélection de UICollectionViewCell simplifiée..!!](https://hackernoon.com/uicollectionviewcell-selection-made-easy-41dae148379d)

N'hésitez pas à laisser des commentaires si vous avez des questions.