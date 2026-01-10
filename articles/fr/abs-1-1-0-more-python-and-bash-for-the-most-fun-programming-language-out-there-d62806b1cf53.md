---
title: 'ABS 1.1.0 : plus de Python et de Bash pour le langage de programmation le
  plus amusant'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T22:39:34.000Z'
originalURL: https://freecodecamp.org/news/abs-1-1-0-more-python-and-bash-for-the-most-fun-programming-language-out-there-d62806b1cf53
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6mI3EvSE3oEnyo9i8g-HBw.png
tags:
- name: Bash
  slug: bash
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: Python
  slug: python
seo_title: 'ABS 1.1.0 : plus de Python et de Bash pour le langage de programmation
  le plus amusant'
seo_desc: 'By Alex Nadalin


  If you missed my previous post, ABS is a programming language that allows you to
  interact with the underlying system with a modern syntax. This is an example of
  it as a version of Bash built in 2019.


  In this article, I’ll discuss a ...'
---

Par Alex Nadalin

> Si vous avez manqué [mon précédent article](https://medium.freecodecamp.org/introducing-abs-a-programming-language-for-shell-scripting-dfbd737d621), ABS est un langage de programmation qui vous permet d'interagir avec le système sous-jacent avec une syntaxe moderne. Voici un exemple de celui-ci en tant que version de Bash construite en 2019.

Dans cet article, je vais discuter d'une toute nouvelle version du [langage de programmation ABS](https://www.abs-lang.org/), apportant plus de syntaxe que vous devriez connaître, inspirée à la fois par Bash et Python.

![Image](https://cdn-media-1.freecodecamp.org/images/5OAgXy5TO37WQneW-yytB9mfRRN5GgSTWQmg)

Cette version inclut 8 nouvelles fonctionnalités et 2 corrections de bugs, alors découvrons-les ensemble !

### Meilleure vérification d'appartenance

L'opérateur de vérification d'appartenance, `in`, prend désormais en charge la recherche pour savoir si un objet possède une clé particulière ainsi que la recherche de sous-chaînes dans les chaînes de caractères :

```
some in {"some": "thing"} # VRAIsome in {} # FAUX
```

```
"str" in "string" # VRAI"hello" in "string" # FAUX
```

Avec ces changements apportés à `in`, nous déprécions désormais la fonction `set.includes(member)` :

```
"string".contains("str")[1, 2, 3].contains(2)
```

La fonction continuera de fonctionner mais, encore une fois, elle est dépréciée. Nous ne la supprimerons probablement pas des futures versions (même majeures), mais... vous avez été prévenus !

### 1 ~ 1.1

L'opérateur de similarité, `~`, prend désormais en charge les nombres :

```
1 ~ 1.23 # VRAI1 ~ 0.99 # FAUX
```

Les nombres seront similaires si leur conversion en entier est la même. C'est un raccourci pour :

```
1.int() == 1.23.int() # VRAI1.int() ~ 0.99.int() # FAUX
```

### for .. in

Nous avons apporté quelques modifications à `for .. in` pour le rendre plus utile, car vous pouvez maintenant parcourir les hachages :

```
for k, v in {"some": "thing"} {    # k est some     # v est thing }
```

### Plus de déstructuration

Nous avons introduit la déstructuration [avant qu'ABS ne soit stable](https://github.com/abs-lang/abs/releases/tag/preview-2), [l'avons mise à jour juste avant la 1.0](https://github.com/abs-lang/abs/releases/tag/preview-3), et nous l'avons maintenant étendue pour pouvoir déstructurer les hachages :

```
some, thing = {"some": 1, "thing": 1}some + thing # 2
```

### Commandes avec backticks

Ma fonctionnalité _absolue_ préférée dans cette version est la possibilité d'exécuter des commandes avec la syntaxe shell des backticks :

```
`ls -la`
```

```
# auparavant, vous ne pouviez faire que$(ls -la)
```

Il y avait certaines limitations avec la syntaxe `$()` (à savoir, une commande doit être sur sa propre ligne) qui n'existent plus avec les backticks. Maintenant, vous pouvez faire des choses comme :

```
if `somecommand`.ok {    ...faire quelque chose...}
```

```
# Ceci n'est pas possible, $() a besoin de sa propre ligne$(somecommand).ok
```

Le même style d'interpolation disponible avec `$()` fonctionne avec les backticks :

```
arg = "-la"`ls $arg`
```

### sleep(ms)

Eh bien... tous les langages en ont un !

Vous pouvez maintenant mettre en pause l'exécution d'un script en dormant pendant un certain nombre de millisecondes :

```
echo("Ceci sera imprimé immédiatement")sleep(10000)echo("Ceci sera imprimé dans 10s")
```

### Fonctions intégrées pour les hachages

Avec cette version, nous avons ajouté un ensemble de nouvelles fonctionnalités intégrées pour les hachages :

```
hash = {"a": 1, "b": 2, "c": 3}
```

```
hash.keys() # ["a", "b", "c"]hash.values() # [1, 2, 3]hash.items() # [["a", 1], ["b", 2], ["c", 3]]hash.pop(a) # hash est maintenant {"b": 2, "c": 3}
```

### Comparaison NULL

Dans [ABS 1.0.0](https://github.com/abs-lang/abs/releases/tag/1.0.0), nous avons introduit un bug qui faisait échouer la comparaison NULL :

```
null == null # FAUX
```

Dans la version 1.2.0, nous l'avons corrigé (et rétroporté dans [1.0.2](https://github.com/abs-lang/abs/releases/tag/1.0.2)).

### Affectations d'index

L'affectation à l'index d'un hachage/tableau fonctionne désormais :

```
array = []array[0] = 1 # array est maintenant [1]array[5] = 1 # array est maintenant [1, null, null, null, null, 1]
```

```
hash = {}hash.x = 1 # hash est maintenant {"x": 1}
```

### Qu'attendez-vous ?

```
bash <(curl https://www.abs-lang.org/installer.sh)
```

... et commencez à scripter comme si c'était 2019 !

PS : Encore une fois, un grand merci à [Erich](https://github.com/ntwrick), qui m'a aidé tout au long du processus et est devenu un membre crucial de l'équipe au cours des dernières semaines. Je veux juste m'assurer que son nom est mentionné car la plupart de ces choses n'auraient pas été possibles sans lui !

PPS : [La version 1.2.0 est déjà bien avancée](https://github.com/abs-lang/abs/milestone/9) — attendez-vous à la voir dans les 2 à 3 prochaines semaines. Nous introduirons des fonctionnalités extrêmement intéressantes telles que les commandes en arrière-plan et l'historique REPL, donc ce sera une version passionnante !

_Publié à l'origine sur [odino.org](https://odino.org/abs-1-dot-1-0-released-a-bit-more-of-python-and-a-bit-more-of-bash-for-the-most-programming-language-out-there/)._
_Vous pouvez me suivre sur [Twitter](https://twitter.com/_odino_) — les rants sont les bienvenus !_ 💡