---
title: 'Explication des Hashmaps en Clojure : Comment Récupérer et Mettre à Jour des
  Valeurs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/clojure-hashmaps-explained-how-to-retrieve-values-from-and-update-hashmaps
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9cea740569d1a4ca34e0.jpg
tags:
- name: Clojure
  slug: clojure
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
seo_title: 'Explication des Hashmaps en Clojure : Comment Récupérer et Mettre à Jour
  des Valeurs'
seo_desc: 'A hashmap is a collection that maps keys to values. They have various names
  in other languages – Python refers to them as dictionaries, and JavaScript’s objects
  essentially work like hashmaps.

  A hashmap can, like many collections, be constructed in t...'
---

Une hashmap est une collection qui associe des clés à des valeurs. Elles portent différents noms dans d'autres langues - Python les appelle dictionnaires, et les objets JavaScript fonctionnent essentiellement comme des hashmaps.

Une hashmap peut, comme de nombreuses collections, être construite de deux manières. Il y a la fonction constructeur :

```text
;; Notez que chaque argument est *préfixé* à la hashmap, et non suffixé.
(def a-hashmap (hash-map :a 1 :b 2 :c 3))
a-hashmap
; => {:c 3, :b 2, :a 1}
```

Vous pouvez également les définir en utilisant un littéral de hashmap. Cela est souvent plus concis et clair. L'utilisation de virgules pour séparer les paires clé/valeur dans les hashmaps est recommandée, car cela peut rendre les limites plus claires.

```text
;; Cette hashmap est en fait dans le bon ordre, contrairement à celle ci-dessus.
(def another-hashmap {:a 1, :b 2, :c 3})
another-hashmap
; => {:a 1, :b 2, :c 3}
```

## **Quand utiliser une hashmap ?**

Une hashmap est utile lorsque vous souhaitez donner des noms à vos variables. Si vous vous surprenez à penser, _"Et si j'utilisais un objet..."_ avant de vous rappeler que vous utilisez Clojure, essayez d'utiliser une hashmap.

Elles sont également utiles si vous souhaitez associer deux valeurs différentes l'une à l'autre. Prenez, par exemple, un chiffre ROT13 - vous pourriez associer `\A` avec `\N`, `\B` avec `\M`, et ainsi de suite.

Cela serait long et ennuyeux à écrire dans la plupart des langues, mais Clojure dispose de certaines fonctions qui peuvent le générer pour vous et le rendre _amusant !_

## **Mots-clés et récupération de valeurs à partir de hashmaps**

Attendez. Qu'est-ce que c'est ? `:a` ? `:b` ? `:c` ? Cela semble étrange. Ce sont, vous le voyez, des mots-clés. Ils sont appelés _mots_-clés car ils sont souvent utilisés comme clés dans les hashmaps.

Pourquoi sont-ils souvent utilisés comme clés ? Eh bien, contrairement aux chaînes de caractères, les mots-clés peuvent être utilisés comme fonctions pour extraire des valeurs d'une hashmap ; pas besoin de `get` ou `nth` !

```text
(def string-hashmap {"a" 1, "b" 2, "c" 3})
("a" string-hashmap)
; => ClassCastException java.lang.String cannot be cast to clojure.lang.IFn

(def keyword-hashmap {:a 1, :b 2, :c 3})
(:a keyword-hashmap)
; => 1

;; Vous pouvez également passer un mot-clé avec une valeur par défaut au cas où il n'est pas trouvé, tout comme get.
(:not-in-the-hashmap keyword-hashmap "not found!")
; => "not found!"
```

## Mettre à jour une hashmap

Vous pouvez mettre à jour des valeurs à l'intérieur d'une hashmap en utilisant `assoc`. Cela vous permet d'ajouter de nouvelles paires clé/valeur ou de modifier les anciennes.

```text
(def outdated-hashmap {:a 1, :b 2, :c 3})

(def newer-hashmap (assoc outdated-hashmap :d 4))
newer-hashmap
; => {:a 1, :b 2, :c 3, :d 4}

(def newest-hashmap (assoc newer-hashmap :a 22))
newest-hashmap
; => {:a 22, :b 2, :c 3, :d 4}

;; Notez que outdated-hashmap n'a pas été mutée par tout cela.
;; Assoc est pur et fonctionnel.
outdated-hashmap
; => {:a 1, :b 2, :c 3}
```

## **Convertir d'autres collections en hashmaps**

La conversion en hashmap est délicate. Pour démontrer, essayons de l'utiliser comme `vec` ou `seq`.

```text
(hash-map [:a 1 :b 2 :c 3])
; => IllegalArgumentException No value supplied for key: [:a 1 :b 2 :c 3]
```

La fonction `hash-map` pense que nous essayons de créer une hashmap avec `[:a 1 :b 2 :c 3]` comme l'une des clés. Regardez ce qui se passe si nous lui donnons le bon nombre d'arguments :

```text
(hash-map [:a 1 :b 2 :c 3] "foo")
; => {[:a 1 :b 2 :c 3] "foo"}
```

Pour convertir une séquence en hashmap, vous devrez utiliser et comprendre `apply`. Heureusement, cela est assez simple : `apply` déstructure essentiellement une collection avant d'appliquer une fonction à celle-ci.

```text
;; Ces deux expressions sont exactement les mêmes.
(+ 1 2 3)
; => 6
(apply + [1 2 3])
; => 6
```

Voici comment vous convertiriez un vecteur en hashmap :

```text
(apply hash-map [:a 1 :b 2 :c 3])
; => {:c 3, :b 2, :a 1}

;; Cela est identique à :
(hash-map :a 1 :b 2 :c 3)
; => {:c 3, :b 2, :a 1}
```

Cela devrait être tout ce dont vous avez besoin pour commencer avec les hashmaps en Clojure. Maintenant, sortez et commencez à hacher avec les meilleurs.