---
title: Les tableaux et objets JavaScript sont comme des livres et des journaux
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-29T18:56:01.000Z'
originalURL: https://freecodecamp.org/news/javascript-arrays-and-objects-are-just-like-books-and-newspapers-6e1cbd8a1746
coverImage: https://cdn-media-1.freecodecamp.org/images/1*weFuKf53lfxyJLOK_hJa7A.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: learning to code
  slug: learning-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Les tableaux et objets JavaScript sont comme des livres et des journaux
seo_desc: 'By Kevin Kononenko

  If you have read books and newspapers, then you can understand the difference between
  arrays and objects in JavaScript.

  When you’re just getting started with JavaScript, it is easy to get confused on
  the best way to organize and st...'
---

Par Kevin Kononenko

#### Si vous avez lu des livres et des journaux, alors vous pouvez comprendre la différence entre les tableaux et les objets en JavaScript.

Lorsque vous commencez avec JavaScript, il est facile de se confondre sur la meilleure façon d'organiser et de stocker des données.

D'une part, vous êtes probablement familier avec les tableaux grâce à l'apprentissage des boucles "for". Mais, une fois que vous commencez à entasser autant de données que possible dans des tableaux, vous allez créer un désordre non scalable qui sera impossible à comprendre lorsque vous relirez votre code.

Choisir entre un objet et un tableau devient beaucoup plus facile lorsque vous pouvez rapidement déterminer le but de chaque structure. Les tableaux correspondent étroitement à la manière dont les livres stockent l'information. Et les objets correspondent à la manière dont les journaux stockent l'information.

Plongeons-nous dans le sujet !

#### Tableaux : L'ordre des données est le plus important

Voici les sections d'un livre super court, sous forme de tableau.

D'accord, je l'admets, ce sont les trois premiers chapitres du [premier livre Harry Potter](http://harrypotter.wikia.com/wiki/Harry_Potter_and_the_Philosopher%27s_Stone). Voici ce tableau sous forme visuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FQ6CJaawGTIB_oa8M-Z7GQ.png)

Vous voulez utiliser des tableaux lorsque **l'ordre est le facteur le plus important pour organiser l'information**. Personne (je l'espère) ne regarde les titres des chapitres d'un livre Harry Potter et ne dit : "Hmmm, celui-ci a l'air intéressant, laissez-moi sauter à celui-là !" L'ordre des chapitres vous indique lequel lire ensuite.

Lorsque vous récupérez des informations depuis le tableau, vous utilisez l'**index** de chaque élément. Les tableaux sont [indexés à partir de 0](https://en.wikipedia.org/wiki/Zero-based_numbering), ce qui signifie qu'ils commencent à compter à partir de 0 plutôt que de 1.

Cela signifie que si vous vouliez accéder à l'index 0 du tableau des livres, vous utiliseriez :

```
books[0]
```

Et vous obtiendriez :

```
'foreword'
```

Si vous vouliez connaître le nom de la troisième section du livre, vous utiliseriez :

```
books[2]
```

Vous choisissez quelles sections lire ensuite en fonction de l'ordre dans le livre, et non en fonction du titre du chapitre.

#### Objets : L'étiquette des données est la plus importante

Voici à quoi pourrait ressembler un journal, sous forme d'objet.

Voici les mêmes données sous forme visuelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0C2W6JHq_TKG6anfblBiqg.png)

Les objets sont les meilleurs lorsque vous voulez **organiser en fonction des étiquettes de données**. Lorsque vous lisez un journal, vous ne le lisez probablement pas de la première à la dernière page, page par page. Vous allez à une certaine section en fonction du nom de la section. Peu importe où cette section se trouve dans le journal, vous pouvez y accéder immédiatement et avoir le contexte approprié. Cela diffère d'un livre, où l'ordre des chapitres/sections compte.

Les objets organisent ces informations via des **paires clé/valeur**. Cela ressemble à ceci :

```
key: value
```

Si vous vouliez accéder à la section Business de ce journal, vous utiliseriez la **clé** comme suit :

```
newspaper['business']
```

ou :

```
newspaper.business
```

Cela retournerait la **valeur** *'GE Stock Dips Again'*. Donc, lorsque c'est plus facile d'accéder aux données en fonction d'une étiquette (la **clé**), vous voulez les stocker dans un objet.

#### Combiner les objets et les tableaux

Jusqu'à présent, nous avons simplement stocké des chaînes de caractères dans nos tableaux et objets. Vous pouvez également stocker d'autres types de données de base comme des nombres et des booléens, ainsi que :

1. Des tableaux dans des objets
2. Des objets dans des tableaux.
3. Des tableaux dans des tableaux
4. Des objets dans des objets

C'est là que cela commence à devenir complexe. Mais, vous aurez presque toujours besoin d'une combinaison des deux pour stocker vos données de manière scalable. Vous voulez comprendre le code une semaine plus tard lorsque vous devrez le réviser.

Reprenons l'exemple du livre. Et si nous voulions également stocker le nombre de pages dans chaque chapitre ? Il serait peut-être préférable de remplir notre tableau avec des objets. Comme ceci :

```
var book =[  ['foreword', 14],  ['boywholived', 18]]
```

Nous avons maintenu l'ordre de nos chapitres, et maintenant nous avons la possibilité de nommer des propriétés spécifiques de chaque chapitre. Donc, si nous voulions connaître le nombre de pages de la deuxième section, nous utiliserions :

```
book[1]['pageCount']
```

Cela donnerait une **valeur** de 18.

Maintenant, disons que vous voulez voir un classement des meilleurs écrivains pour chaque section de votre journal local, basé sur l'ancienneté. Vous pourriez exprimer cela dans un tableau à l'intérieur de l'objet journal, comme ceci :

Un tableau convient bien pour stocker les écrivains car l'ordre compte. Vous savez que les écrivains précédents sont mieux classés que les écrivains suivants dans chaque tableau. L'écrivain à l'index 0 est l'écrivain le mieux classé.

Vous pourriez probablement optimiser cet objet en créant simplement des objets à l'intérieur de l'objet journal. Par exemple, un objet _sports_ avec un titre et une liste d'écrivains. Mais je vous laisse essayer cela !

#### Quelques défis rapides pour vous

1. Disons que votre application web a une partie quiz, où les utilisateurs répondent à un certain nombre de questions et obtiennent un score à la fin. Vous voulez stocker la réponse d'un utilisateur à chaque question, puis les vérifier efficacement à la fin. Quelle structure utiliseriez-vous pour stocker toutes les réponses de l'utilisateur avant de les vérifier ? Pourquoi ?
2. Disons que vous permettez aux utilisateurs de créer un nouveau profil sur votre site, avec un prénom, un nom, un email et un mot de passe. Vous voulez stocker ces données avant de les envoyer au back-end. Quelle structure utiliseriez-vous pour stocker toutes les informations du nouvel utilisateur ? Pourquoi ?
3. Disons que vous construisez un site de forum, où vous devez classer les commentaires en fonction du nombre de votes. Quelle structure pourrait avoir le plus de sens, lorsque vous devez suivre à la fois le texte du commentaire lui-même ET le nombre de votes ? Indice : une combinaison des deux d'une certaine sorte.

Si vous avez aimé cet article, vous aimerez peut-être aussi mes [autres explications](http://www.rtfmanual.io) de sujets CSS, JavaScript et SQL difficiles, tels que le positionnement, le Modèle-Vue-Contrôleur et les callbacks.

Et si vous pensez que cela pourrait aider d'autres personnes dans la même situation que vous, donnez-lui un "heart" !

[_Cet article est initialement paru sur le blog CodeAnalogies._](https://blog.codeanalogies.com/2017/04/29/javascript-arrays-and-objects-are-just-like-books-and-newspapers/)