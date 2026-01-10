---
title: Comment créer une police personnalisée cohérente dans une application iOS avec
  seulement quelques lignes de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T22:00:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-consistent-custom-font-in-an-ios-app-e07b1ddb7a7c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*VaQCLYc6J3qmNdEPHmhIOA.png
tags:
- name: fonts
  slug: fonts
- name: iOS
  slug: ios
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Comment créer une police personnalisée cohérente dans une application iOS
  avec seulement quelques lignes de code
seo_desc: 'By Yuichi Fujiki

  In this article, you''ll learn how to create a unified custom look throughout your
  app with these simple tricks.

  What we want to do

  In iOS, there is a mechanism called UIAppearance to define an app’s global configuration.
  For example,...'
---

Par Yuichi Fujiki

Dans cet article, vous apprendrez comment créer une apparence personnalisée unifiée dans toute votre application avec ces astuces simples.

## Ce que nous voulons faire

Dans iOS, il existe un mécanisme appelé `UIAppearance` pour définir une configuration globale de l'application. Par exemple, vous pouvez définir une couleur de fond cohérente pour la barre de navigation avec une seule ligne :

```
UINavigationBar.appearance().barTintColor = UIColor.blue
```

Cependant, si vous appliquez la même approche à la police comme ceci :

```
UILabel.appearance().font = UIFont(named: "Gills Sans", size: 14)
```

toutes les instances de `UILabel` auront effectivement "Gills Sans", **mais avec une taille de 14 pt également**. Je ne pense pas qu'une application souhaite avoir **uniquement** des polices de 14 pt dans toute l'application. Puisque `UIFont` a toujours besoin des informations de taille pour être initialisé, il n'existe **aucun moyen standard** dans `UIKit` pour changer uniquement la famille de police sans affecter la taille.

Mais, ne souhaitez-vous pas changer la famille de police sans devoir parcourir tous les fichiers Swift et les fichiers Interface Builder ? Imaginez que vous avez une application avec des dizaines d'écrans et que le propriétaire du produit décide de changer la police pour toute l'application. Ou votre application veut couvrir une autre langue, et vous souhaitez utiliser une autre police pour cette langue car elle serait plus adaptée.

Cet article court explique comment vous pouvez faire cela avec seulement quelques lignes de code.

## Extension UIView

Lorsque vous créez une extension `UIView` et déclarez une propriété avec le modificateur `@objc`, vous pouvez définir cette propriété via `UIAppearance`.

Par exemple, si vous déclarez une propriété d'extension `UILabel` `substituteFontName` comme ceci :

Vous pouvez l'appeler dans `AppDelegate.application(:didFinishLaunching...)`

```
UILabel.appearance().substituteFontName = "Gills Sans"
```

Et voilà, toutes les `UILabel` seront dans la police "Gills Sans" avec des tailles appropriées. 🎉

## Mais vous voulez aussi utiliser une police en gras, n'est-ce pas ?

Jusqu'à présent, tout va bien, mais que faire si vous souhaitez spécifier deux variations différentes de la même police, comme une police en gras ? Vous pourriez penser que vous pouvez simplement ajouter une autre propriété d'extension `substituteBoldFontName` et l'appeler comme ceci, n'est-ce pas ?

```
UILabel.appearance().substituteFontName = fontNameUILabel.appearance().substituteBoldFontName = boldFontName
```

Ce n'est pas si simple. Si vous faites cela, alors **toutes** les instances de `UILabel` s'affichent en police gras. Je vais expliquer pourquoi.

Il semble que `UIAppearance` appelle simplement toutes les méthodes de définition des propriétés enregistrées dans l'ordre où elles ont été enregistrées.

Ainsi, si nous avons implémenté l'extension `UILabel` comme ceci :

alors la définition des deux propriétés via `UIAppearance` entraîne une séquence de code similaire à ce qui suit à chaque initialisation de `UILabel` en arrière-plan.

```
font = UIFont(name: substituteFontName, size: font.pointSize)font = UIFont(name: substituteBoldFontName, size: font.pointSize)
```

Ainsi, la première ligne est écrasée par la deuxième ligne et vous allez avoir des polices en gras partout. 😢

### Que pouvez-vous faire à ce sujet ?

Pour résoudre ce problème, nous pouvons attribuer un style de police approprié en fonction du style de police d'origine nous-mêmes.

Nous pouvons modifier notre extension `UILabel` comme suit :

Maintenant, la séquence de code qui est appelée à l'initialisation de `UILabel` sera comme suit, et seulement une des deux affectations de `font` sera appelée dans une condition.

```
if font.fontName.range(of: "Medium") == nil {   font = UIFont(name: newValue, size: font.pointSize)}if font.fontName.range(of: "Medium") != nil {   font = UIFont(name: newValue, size: font.pointSize)}
```

En conséquence, vous aurez une application avec un style de texte magnifiquement unifié tout en ayant des polices régulières et en gras qui coexistent, hourra ! 🎉

Vous devriez pouvoir utiliser la même logique pour ajouter plus de styles comme les polices italiques. De plus, vous devriez pouvoir appliquer la même approche à un autre contrôle comme `UITextField`.

J'espère que cela aide les développeurs iOS, bon codage !!