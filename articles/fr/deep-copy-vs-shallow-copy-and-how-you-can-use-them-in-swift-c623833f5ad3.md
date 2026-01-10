---
title: Copie profonde vs. copie superficielle — et comment les utiliser en Swift
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T23:42:32.000Z'
originalURL: https://freecodecamp.org/news/deep-copy-vs-shallow-copy-and-how-you-can-use-them-in-swift-c623833f5ad3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7s9oXXuSiTw_HDCwc0Mrqw.jpeg
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
seo_title: Copie profonde vs. copie superficielle — et comment les utiliser en Swift
seo_desc: 'By Payal Gupta

  Copying an object has always been an essential part in the coding paradigm. Be it
  in Swift, Objective-C, JAVA or any other language, we’ll always need to copy an
  object for use in different contexts.

  In this article, we’ll discuss in d...'
---

Par Payal Gupta

Copier un objet a toujours été une partie essentielle du paradigme de programmation. Que ce soit en Swift, Objective-C, JAVA ou tout autre langage, nous aurons toujours besoin de copier un objet pour l'utiliser dans différents contextes.

Dans cet article, nous discuterons en détail de la manière de copier différents types de données en Swift et de leur comportement dans différentes circonstances.

### Types de valeur et types de référence

Tous les types de données en Swift se divisent en deux catégories, à savoir les **types de valeur** et les **types de référence**.

* **Type de valeur** — chaque instance conserve une copie unique de ses données. Les types de données qui entrent dans cette catégorie incluent — `tous les types de données de base, struct, enum, array, tuples`.
* **Type de référence** — les instances partagent une seule copie des données, et le type est généralement défini comme une `class`.

La caractéristique la plus distinctive des deux types réside dans leur comportement de copie.

### Qu'est-ce qu'une copie profonde et une copie superficielle ?

Une instance, qu'il s'agisse d'un type de valeur ou d'un type de référence, peut être copiée de l'une des manières suivantes :

#### **Copie profonde** — Duplique tout

* Avec une copie profonde, tout objet pointé par la source est copié et la copie est pointée par la destination. Ainsi, deux objets complètement séparés seront créés.
* **Collections** — Une copie profonde d'une collection est deux collections avec tous les éléments de la collection originale dupliqués.
* **Moins sujette aux conditions de course** et performante dans un environnement multithread — les modifications dans un objet n'auront aucun effet sur un autre objet.
* **Les types de valeur** sont copiés profondément.

Dans le code ci-dessus,

* **Ligne 1** : `arr1` — tableau (un type de valeur) de Strings
* **Ligne 2** : `arr1` est assigné à `arr2`. Cela créera une copie profonde de `arr1` puis assignera cette copie à `arr2`
* **Lignes 7 à 11** : toute modification effectuée dans `arr2` ne se reflète pas dans `arr1`.

C'est ce qu'est une copie profonde — des instances complètement séparées. Le même concept fonctionne avec tous les types de valeur.

Dans certains scénarios, c'est-à-dire lorsqu'un type de valeur contient des types de référence imbriqués, la copie profonde révèle un comportement différent. Nous verrons cela dans les sections à venir.

#### **Copie superficielle** — Duplique le moins possible

* Avec une copie superficielle, tout objet pointé par la source est également pointé par la destination. Ainsi, un seul objet sera créé en mémoire.
* **Collections** — Une copie superficielle d'une collection est une copie de la structure de la collection, et non des éléments. Avec une copie superficielle, deux collections partagent désormais les éléments individuels.
* **Plus rapide** — seule la référence est copiée.
* La copie des **types de référence** crée une copie superficielle.

Dans le code ci-dessus,

* **Lignes 1 à 8** : type de classe `Address`
* **Ligne 10** : `a1` — une instance du type `Address`
* **Ligne 11** : `a1` est assigné à `a2`. Cela créera une copie superficielle de `a1` puis assignera cette copie à `a2`, c'est-à-dire que seule la référence est copiée dans `a2`.
* **Lignes 16 à 19** : toute modification effectuée dans `a2` se reflétera certainement dans `a1`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HCBKXip1e4ACmsDcDcGOrA.png)

Dans l'illustration ci-dessus, nous pouvons voir que `a1` et `a2` pointent vers la même adresse mémoire.

### Copie profonde des types de référence

Jusqu'à présent, nous savons que chaque fois que nous essayons de copier un type de référence, seule la référence à l'objet est copiée. Aucun nouvel objet n'est créé. Que faire si nous voulons créer un objet complètement séparé ?

Nous pouvons créer une copie profonde du type de référence en utilisant la méthode `[copy()](https://developer.apple.com/documentation/objectivec/nsobject/1418807-copy)`. Selon la [documentation](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy),

copy() — Retourne l'objet retourné par `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)`.

Il s'agit d'une méthode de commodité pour les classes qui adoptent le protocole `[NSCopying](https://developer.apple.com/documentation/foundation/nscopying)`. Une exception est levée s'il n'y a pas d'implémentation pour `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)`.

Restructurons la `classe Address` que nous avons créée dans l'extrait de code 2 pour qu'elle se conforme au protocole `NSCopying`.

Dans le code ci-dessus,

* **Lignes 1 à 14** : le type de classe `Address` se conforme à `NSCopying` et implémente la méthode `[copy(with:)](https://developer.apple.com/documentation/foundation/nscopying/1410311-copy)`
* **Ligne 16** : `a1` — une instance du type `Address`
* **Ligne 17** : `a1` est assigné à `a2` en utilisant la méthode `copy()`. Cela créera une copie profonde de `a1` puis assignera cette copie à `a2`, c'est-à-dire qu'un objet complètement nouveau sera créé.
* **Lignes 22 à 25** : toute modification effectuée dans `a2` ne se reflétera pas dans `a1`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KRe3gHvPBmPeclvEctU4qA.png)

Comme le montre l'illustration ci-dessus, `a1` et `a2` pointent vers des emplacements mémoire différents.

Examinons un autre exemple. Cette fois, nous verrons comment cela fonctionne avec **les types de référence imbriqués — un type de référence contenant un autre type de référence**.

Dans le code ci-dessus,

* **Ligne 22** : une copie profonde de `p1` est assignée à `p2` en utilisant la méthode `copy()`. Cela implique que tout changement dans l'un d'eux ne doit avoir aucun effet sur l'autre.
* **Lignes 27 à 28** : les valeurs `name` et `city` de `p2` sont modifiées. Cela ne doit pas se refléter dans `p1`.
* **Ligne 30** : le `name` de `p1` est comme prévu, mais sa `city` ? Elle devrait être « Mumbai », non ? Mais nous ne pouvons pas voir cela se produire. « Bangalore » était seulement pour `p2`, non ? Oui... exactement. ?

_Copie profonde... !_ ? _Ce n'était pas attendu de vous. Vous avez dit que vous copieriez tout. Et maintenant vous vous comportez comme ça. Pourquoi oh pourquoi.. ?! Que faire maintenant ? ☠️_

Ne paniquez pas. Examinons ce que les adresses mémoire ont à dire à ce sujet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*6AbWa3I3gC4p-PsFCILOew.png)

D'après l'illustration ci-dessus, nous pouvons voir que

* `p1` et `p2` pointent vers des emplacements mémoire différents comme prévu.
* Mais leurs variables `address` pointent toujours vers le même emplacement. Cela signifie que même après les avoir copiés profondément, seules les références sont copiées — c'est-à-dire, une **copie superficielle** bien sûr.

**Veuillez noter :** chaque fois que nous copions un type de référence, une copie superficielle est créée par défaut jusqu'à ce que nous spécifions explicitement qu'elle doit être copiée profondément.

```
func copy(with zone: NSZone? = nil) -> Any{    let person = Person(self.name, self.address)    return person}
```

Dans la méthode ci-dessus que nous avons implémentée précédemment pour la classe `Person`, nous avons créé une nouvelle instance en copiant l'adresse avec `self.address`. Cela ne copiera que la référence à l'objet adresse. C'est la raison pour laquelle les `address` de `p1` et `p2` pointent vers le même emplacement.

Ainsi, copier l'objet en utilisant la méthode `copy()` ne créera pas une vraie copie profonde de l'objet**_.**

**Pour dupliquer complètement un objet de référence :** le type de référence ainsi que tous les types de référence imbriqués doivent être copiés avec la méthode `copy()`.

```
let person = Person(self.name, self.address.copy() as? Address)
```

L'utilisation du code ci-dessus dans la méthode `func copy(with zone: NSZone? = nil) ->` Any fera fonctionner tout correctement. Vous pouvez le voir à partir de l'illustration ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XdsZvbu6N5jYEDumL3PCUw.png)

### Vraie copie profonde — Types de référence et types de valeur

Nous avons déjà vu comment nous pouvons créer une copie profonde des types de référence. Bien sûr, nous pouvons le faire avec tous les types de référence imbriqués.

Mais qu'en est-il du type de référence imbriqué dans un type de valeur, c'est-à-dire un tableau d'objets, ou une variable de type de référence dans une struct ou peut-être un tuple ? Pouvez-vous résoudre cela en utilisant `copy()` également ? Non, nous ne pouvons pas, en fait. La méthode `copy()` nécessite l'implémentation du protocole `NSCopying` qui ne fonctionne que pour les sous-classes de `NSObject`. Les types de valeur ne supportent pas l'héritage, donc nous ne pouvons pas utiliser `copy()` avec eux.

À la ligne 2, seule la structure de `arr1` est copiée profondément, mais les objets `Address` à l'intérieur sont toujours copiés superficiellement. Vous pouvez le voir à partir de la carte mémoire ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*P4qAq9o-mqCbhiHx0mfnYA.png)

Les éléments dans `arr1` et `arr2` pointent tous deux vers les mêmes emplacements mémoire. Cela est dû à la même raison — les types de référence sont copiés superficiellement par défaut.

**Sérialiser puis désérialiser** un objet crée toujours un objet entièrement nouveau. Cela est valable pour les types de valeur ainsi que pour les types de référence.

Voici quelques API que nous pouvons utiliser pour sérialiser et désérialiser des données :

1. [**NSCoding**](https://developer.apple.com/documentation/foundation/nscoding) — Un protocole qui permet à un objet d'être encodé et décodé pour l'archivage et la distribution. Il ne fonctionnera qu'avec les objets de type `class` car il nécessite d'hériter de `NSObject`.
2. [**Codable**](https://developer.apple.com/documentation/foundation/archives_and_serialization/encoding_and_decoding_custom_types) — Rendez vos types de données encodables et décodables pour la compatibilité avec des représentations externes telles que JSON. Il fonctionnera pour les types de valeur — `struct, array, tuple, basic data types` ainsi que pour les types de référence — `class`.

Restructurons un peu plus la classe `Address` pour qu'elle se conforme au protocole `Codable` et supprimons tout le code `NSCopying` que nous avons ajouté précédemment dans l'extrait de code 3.

Dans le code ci-dessus, les lignes 11–13 créeront une vraie copie profonde de `arr1`. Ci-dessous se trouve l'illustration qui donne une image claire des emplacements mémoire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*17lE3zZhorgMa6GFLNoOoA.png)

### Copie à l'écriture

La copie à l'écriture est une technique d'optimisation qui aide à améliorer les performances lors de la copie de types de valeur.

Supposons que nous copions une seule String ou Int ou peut-être tout autre type de valeur — nous ne rencontrerons aucun problème de performance crucial dans ce cas. Mais qu'en est-il lorsque nous copions un tableau de milliers d'éléments ? Cela ne créera-t-il toujours pas de problèmes de performance ? Et si nous le copions simplement et n'apportons aucune modification à cette copie ? Cette mémoire supplémentaire que nous avons utilisée n'est-elle pas simplement du gaspillage dans ce cas ?

Voici le concept de Copie à l'écriture — lors de la copie, chaque référence pointe vers la même adresse mémoire. Ce n'est que lorsqu'une des références modifie les données sous-jacentes que Swift copie réellement l'instance originale et effectue la modification.

C'est-à-dire, qu'il s'agisse d'une copie profonde ou superficielle, une nouvelle copie ne sera pas créée tant que nous n'aurons pas apporté de modification à l'un des objets.

Dans le code ci-dessus,

* **Ligne 2** : une copie profonde de `arr1` est assignée à `arr2`
* **Lignes 4 et 5** : `arr1` et `arr2` pointent toujours vers la même adresse mémoire
* **Ligne 7** : modifications apportées dans `arr2`
* **Lignes 9 et 10** : `arr1` et `arr2` pointent désormais vers des emplacements mémoire différents

Maintenant, vous en savez plus sur les copies profondes et superficielles et sur leur comportement dans différents scénarios avec différents types de données. Vous pouvez les essayer avec votre propre ensemble d'exemples et voir quels résultats vous obtenez.

### Lectures complémentaires

N'oubliez pas de lire mes autres articles :

1. [Tout sur Codable en Swift 4](https://hackernoon.com/everything-about-codable-in-swift-4-97d0e18a2999)
2. [Tout ce que vous avez toujours voulu savoir sur les notifications dans iOS](https://medium.freecodecamp.org/ios-10-notifications-inshorts-all-in-one-ad727e03983a)
3. [Coloriez-le avec des DÉGRADÉS — iOS](https://hackernoon.com/color-it-with-gradients-ios-a4b374c3c79f)
4. [Coder pour iOS 11 : Comment glisser-déposer dans les collections et les tables](https://hackernoon.com/drag-it-drop-it-in-collection-table-ios-11-6bd28795b313)
5. [Tout ce que vous devez savoir sur les Extensions Today (Widget) dans iOS 10](https://hackernoon.com/app-extensions-and-today-extensions-widget-in-ios-10-e2d9fd9957a8)
6. [Sélection de UICollectionViewCell simplifiée..!!](https://hackernoon.com/uicollectionviewcell-selection-made-easy-41dae148379d)

N'hésitez pas à laisser des commentaires si vous avez des questions.