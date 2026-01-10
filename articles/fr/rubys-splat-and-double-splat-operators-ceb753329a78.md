---
title: Une introduction aux opérateurs *Splat et **Double Splat de Ruby
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-07T00:15:35.000Z'
originalURL: https://freecodecamp.org/news/rubys-splat-and-double-splat-operators-ceb753329a78
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4Cc4O2WsCRkCaFiy0u92QA.png
tags:
- name: coding
  slug: coding
- name: General Programming
  slug: programming
- name: Ruby
  slug: ruby
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Une introduction aux opérateurs *Splat et **Double Splat de Ruby
seo_desc: 'By Declan Meehan

  Have you ever wanted to define a method without knowing how many arguments it will
  take? Do you spend long restless nights wishing there was an easy way to separate
  a list into a hash? Well look no further than Ruby’s splat operators...'
---

Par Declan Meehan

Avez-vous déjà voulu définir une méthode sans savoir combien d'arguments elle prendra ? Passez-vous de longues nuits sans sommeil en souhaitant qu'il existe un moyen facile de séparer une liste en un hash ? Ne cherchez pas plus loin que les opérateurs splat de Ruby ! Il y a tant de choses géniales que vous pouvez faire avec ceux-ci, mais je vais simplement passer en revue les bases plus quelques astuces sympas que j'ai découvertes.

### Splat unique *

L'opérateur splat a presque des utilisations infinies. Mais l'idée principale est que chaque fois que vous ne voulez pas spécifier le nombre d'arguments que vous avez, vous utiliseriez un opérateur splat. L'exemple le plus simple serait quelque chose comme ceci :

Une autre chose utile est que l'opérateur splat peut transformer un tableau en plusieurs arguments :

```
arr = ["first", "second", "third"]
def threeargs(*arr)
  # crée trois arguments
```

Vous pouvez également utiliser l'opérateur splat pour capturer n'importe quel segment d'un tableau :

```
first, *rest, last  = ["a", "b", "c", "d"]
p first # "a"
p rest # ["b", "c"]
p last # "d"
```

Vous remarquerez que la variable rest est toujours un tableau, ce qui est super pratique. Et donc, en suivant le dernier exemple, vous pouvez toujours faire des choses comme ceci :

```
first, *rest, last  = ["a", "b", "c", "d"]
p rest[0] # "b"
```

Ce sont les bases de l'opérateur splat unique, mais je vous encourage à jouer davantage avec lui. Il peut faire des choses comme combiner des tableaux, transformer des hashs et des chaînes en tableaux, ou extraire des éléments d'un tableau !

### Double **Splat

L'opérateur double splat est sorti avec Ruby 2.0. Il est assez similaire au splat original avec une différence : il peut être utilisé pour les hashs ! Voici un exemple pour l'utilisation la plus basique d'un double splat.

```
def doublesplat(**nums)
  p **nums
end
doublesplat one: 1, two: 2 # {:one=>1, :two=>2}
```

### Mettre le tout ensemble

J'espère que vous pouvez voir que les possibilités sont presque infinies en utilisant ces deux ensemble. La chose principale à garder à l'esprit est que vous utilisez des splats comme paramètre dans une méthode lorsque vous n'êtes pas sûr du nombre d'arguments que cette méthode utilisera.

Enfin, j'ai fait une petite fonction qui montre comment vous pouvez filtrer tout argument qui n'est pas une paire clé-valeur en utilisant à la fois un splat unique et un double splat.

```
def dubSplat(a, *b, **c)
  p c
end
dubSplat(1,2,3, 4, a: 40, b: 50)
#{:a=>40, :b=>50}
```

Merci d'avoir lu, et maintenant essayez de jouer avec cela vous-même !