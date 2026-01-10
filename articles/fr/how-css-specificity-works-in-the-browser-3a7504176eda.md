---
title: Comment fonctionne la spécificité CSS dans le navigateur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-09T23:39:14.000Z'
originalURL: https://freecodecamp.org/news/how-css-specificity-works-in-the-browser-3a7504176eda
coverImage: https://cdn-media-1.freecodecamp.org/images/1*wH2JSH_fw4oiAH2eqTg4qA.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la spécificité CSS dans le navigateur
seo_desc: 'By Michael Ozoemena

  A lot of people find CSS really difficult. They blame that on a number of reasons
  like they aren’t wired to understand CSS or CSS is bad or any number of other reasons.
  But most people find CSS difficult because they haven’t taken...'
---

Par Michael Ozoemena

Beaucoup de gens trouvent CSS vraiment difficile. Ils blâment cela pour un certain nombre de raisons comme ils ne sont pas faits pour comprendre CSS ou CSS est mauvais ou toute autre raison. Mais la plupart des gens trouvent CSS difficile parce qu'ils n'ont pas pris le temps de vraiment l'apprendre. Si vous lisez ceci, c'est probablement parce que vous êtes intéressé à devenir meilleur en CSS, et c'est génial !

#### Qu'est-ce que la spécificité CSS ?

Avez-vous déjà écrit un style et il ne fonctionnait tout simplement pas, alors vous ajoutez `!important` (ou ne l'ajoutez pas) et il ne fonctionne toujours pas ? Alors vous regardez les Devtools pour trouver qu'un autre style quelque part est en train de remplacer votre style ?

Eh bien, c'est la spécificité CSS qui entre en jeu ! C'est ainsi que le navigateur choisit lequel de vos sélecteurs en compétition appliquer à un élément. Lorsque votre navigateur voit que deux ou plusieurs de vos sélecteurs correspondent au même élément et que les sélecteurs ont des règles conflictuelles, il a besoin d'un moyen de déterminer laquelle des règles appliquer à cet élément. La façon dont il fait cela est à travers ce qu'on appelle la "valeur de spécificité CSS".

Avant d'approfondir la spécificité CSS, vous devez **noter** ces points :

1. La spécificité CSS n'est importante que lorsque plusieurs sélecteurs affectent le même élément. Le navigateur a besoin d'un moyen de déterminer quel style appliquer à un élément correspondant lorsqu'il y a des valeurs de propriété conflictuelles, et la spécificité CSS est la façon dont il le fait.
2. Lorsque deux ou plusieurs sélecteurs correspondants ont la même valeur de spécificité, le navigateur choisit le sélecteur "le plus récent" correspondant — le sélecteur qui apparaît plus près du bas de la liste des sélecteurs correspondants. Le point suivant explique ce qu'est la "liste des sélecteurs correspondants".
3. Le navigateur forme la "liste des sélecteurs correspondants" en combinant tous les styles d'une page web et en filtrant tous les styles qui ne correspondent pas à l'élément "en cours de stylisation". Les premiers sélecteurs dans la feuille de style sont en haut de la liste et les derniers sélecteurs sont en bas de la liste.
4. La propriété `style` sur un élément a une valeur de spécificité plus grande que les sélecteurs dans les feuilles de style, sauf lorsqu'il y a `!important` dans le sélecteur de la feuille de style.
5. L'utilisation de `!important` (qui est considérée comme une mauvaise pratique dans certains cas) modifie la spécificité d'un sélecteur. Lorsque deux sélecteurs ont la même spécificité, le sélecteur avec `!important` gagne. Et lorsqu'ils ont tous les deux `!important`, le sélecteur "le plus récent" gagne.

#### La valeur de spécificité.

Maintenant que nous avons éclairci ces points, nous pouvons maintenant aborder comment le navigateur détermine les valeurs de spécificité d'un sélecteur.

La spécificité d'un sélecteur peut être représentée comme une chaîne de 3 chiffres, délimitée par un trait d'union (ou ce que vous voulez) : "2-4-1". Le premier chiffre est le nombre de sélecteurs `ID` présents, le deuxième est le nombre de sélecteurs de classe, de sélecteurs d'attributs et de pseudo-classes présents, et le troisième est le nombre de sélecteurs de type et de pseudo-éléments présents. Par exemple :

```
#red.blue // 1-1-0
```

```
#green // 1-0-0
```

```
div.yellow#red // 1-1-1
```

```
.red.blue.yellow // 0-3-0
```

#### Déterminer le plus "spécifique"

Pour déterminer quel sélecteur a plus de spécificité, vous pouvez comparer chacune des trois valeurs.

Supposons que vous avez `1 - 1 - 1` et `0 - 3 - 0`, comme dans les deux derniers exemples, et que vous devez déterminer lequel a plus de spécificité. Vous comparez d'abord les dernières valeurs `1` et `0`, et dans ce cas, `1` gagne. Cela signifie qu'à ce stade, `div.yellow#red` a une valeur de spécificité plus grande... mais nous n'avons pas fini de comparer les valeurs.

Ensuite, vous comparez les deuxièmes valeurs `1` et `3`, et `3` gagne à nouveau. À ce stade, `.red.blue.yellow` a une valeur de spécificité plus grande, mais nous n'avons toujours pas fini.

Enfin, nous comparons les premières valeurs, `1` et `0`, et `1` gagne, donc `div.yellow#red` a plus de spécificité que `.red.blue.yellow`.

C'est ainsi que le navigateur détermine la spécificité CSS d'un sélecteur et cela donne une bonne explication de pourquoi aucun nombre de sélecteurs de classe ne peut remplacer un sélecteur `ID`.

#### Petits avertissements

Il y a trois "pièges" dont je voudrais parler :

1. Plus tôt, j'ai mentionné que le deuxième nombre dans la séquence de trois nombres de la valeur de spécificité _"est le nombre de sélecteurs de classe, de sélecteurs d'attributs et de pseudo-classes présents"_ et c'est vrai dans tous les cas sauf lorsqu'il s'agit de la pseudo-classe `:not()`. Lorsque c'est la pseudo-classe `:not()`, nous ne la comptons pas, nous l'ignorons simplement. Mais les sélecteurs à l'intérieur ne sont pas non plus ignorés, ils sont comptés normalement.
2. La spécificité CSS comprend la "forme" d'un sélecteur. Cela signifie que lorsque vous avez `*[id="yellow"]` et `#yellow`, le premier est traité comme un sélecteur d'attribut (et c'en est un) même s'ils sélectionnent tous les deux essentiellement la même chose.
3. Le sélecteur universel `*` seul n'est pas compté dans la valeur de spécificité d'un sélecteur. Dans le point ci-dessus, la partie `[id="yellow"]` du sélecteur est ce qui compte réellement.

#### Conclusion

J'espère que cet article était facile à comprendre et vous a aidé à mieux comprendre comment fonctionne la spécificité CSS. Maintenant, vous pouvez examiner les styles et simplement dire à quel point un style est "spécifique".

Si ce n'est pas le cas et que vous avez des questions ou des commentaires, je suis heureux d'avoir une discussion avec vous dans la section des commentaires ou sur Twitter [@theozmic](https://twitter.com/theozmic).

N'oubliez pas de laisser un ou deux ou cinquante applaudissements si vous avez aimé cet article.