---
title: Comment écrire un CSS vraiment terrible
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-20T15:49:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-truly-terrible-css-214c26c6f729
coverImage: https://cdn-media-1.freecodecamp.org/images/1*O1a0MYPIXEao7xRij_O7AQ.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment écrire un CSS vraiment terrible
seo_desc: 'By Emmanuel Ohans

  Everyone talks about ‘tips’ and ‘pro-tips’ for writing great CSS.

  That’s fine, but maybe seeing what bad CSS looks like will give you a different
  perspective. Heck, it may even do you some good!

  Let me take you through a journey on ...'
---

Par Emmanuel Ohans

Tout le monde parle de "conseils" et de "conseils pro" pour écrire un excellent CSS.

C'est bien, mais peut-être que voir à quoi ressemble un mauvais CSS vous donnera une perspective différente. Après tout, cela pourrait même vous être bénéfique !

Laissez-moi vous guider à travers un voyage sur la façon d'écrire un très mauvais CSS.

Prêt ?

![Image](https://cdn-media-1.freecodecamp.org/images/w3bFCZdYDt-qHJf85m14wVykMZ2vXfwDaHil)

Note : même si vous jurez par le CSS-in-JS et n'aimez pas le CSS vanilla, nous sommes tous d'accord sur une chose : nous devons tous encore connaître un peu de CSS…

Donc, que vous écriviez du CSS, ou un sur-ensemble comme [SASS](https://sass-lang.com), ou simplement du [CSS-in-JS](https://hackernoon.com/all-you-need-to-know-about-css-in-js-984a72d48ebc), vous bénéficierez toujours de savoir exactement à quoi ressemble un mauvais CSS.

#### Qui écrit des commentaires ? Personne.

![Image](https://cdn-media-1.freecodecamp.org/images/FbkAby9gdFaRJyOXcXG9D3N2mrSloefCGdtB)
_Pas de commentaires ? Du code réel que j'ai écrit il y a quelque temps mais dont j'ai supprimé tous les commentaires ?_

Il est si facile de glisser ici que vous ne remarquerez pas très vite.

Nous le savons tous. Vous êtes si intelligent, personne d'autre ne s'en approche. Même si le CSS n'est pas le plus expressif des "langages", vous pouvez faire des hypothèses sur les particularités des navigateurs, les corriger, et supposer que vous comprendrez ce que vous avez fait quelques semaines plus tard.

Comme c'est intelligent, hein ?

Mettez votre fierté de côté, et épargnez-vous et à vos coéquipiers le stress.

Si vous utilisez une technique pas si évidente, ou avez corrigé une particularité de navigateur, ou quoi que ce soit d'autre que vous pensez n'être pas assez expressif, écrivez ce commentaire ! Cela ne fait pas de mal.

#### Le Pays des Sélecteurs Complexes

![Image](https://cdn-media-1.freecodecamp.org/images/RxyN6FyWgWoXqbvgn3-a7nC499Qf9ROvgE9j)

Oui ! Vous venez d'apprendre le CSS et vous vous sentez au sommet du monde. Alors, il est temps de montrer quelques muscles de sélecteurs.

Mauvais mouvement.

En faisant des sélections avec trop de sélecteurs CSS, vous avez peut-être réussi à rendre votre CSS extrêmement difficile à maintenir. Il est maintenant très dépendant de la structure HTML de votre application.

Si la structure du balisage change légèrement, vous devez également refactoriser votre CSS. Pas le workflow le plus facile.

Ajoutez simplement une classe à l'élément et continuez votre vie !

Même dans les scénarios où vous devez qualifier les sélecteurs avec plusieurs classes, privilégiez toujours la simplicité.

Simple est bien, presque toujours !

#### Performance ? Oubliez ça !

![Image](https://cdn-media-1.freecodecamp.org/images/eg1zeTeOEHbfMYn4FqghXZBXTvumo-7BBWEA)

Alors, je comprends. Vous ne vous souciez tout simplement pas de la performance. Vous ne vous souciez pas de l'entreprise, clairement. Si vous le faisiez, vous n'ennuieriez pas vos utilisateurs avec vos sélecteurs non performants.

Mais attendez…

Je comprends que les ordinateurs sont devenus plus rapides et que les navigateurs continuent d'être optimisés. Quoi qu'il en soit, les sélecteurs simples doivent toujours être préférés, et comprendre comment le navigateur parcourt le DOM pour trouver votre sélecteur est toujours d'actualité !

Il y a des chances que vous lisiez vos sélecteurs de gauche à droite.

Cependant, le navigateur fait correspondre les sélecteurs de droite à gauche, afin d'éliminer les éléments qui ne correspondent pas aussi rapidement que possible.

Si vous saviez cela, vous seriez probablement plus indulgent envers les navigateurs. Ils méritent votre amour.

En considérant l'exemple graphique ci-dessus, le navigateur fera correspondre tous les éléments (*) et vérifiera également s'ils sont des descendants de `body`.

```
body * {  ... } 
```

Mais pourquoi ? Presque tous les éléments visibles sont idéalement des descendants de l'élément `<body>`. Ce n'est qu'une vérification inefficace et inutile.

#### Je suis nul pour nommer les choses, alors je ne me donne même pas la peine.

> Il n'y a que 2 choses difficiles en informatique. Nommer les choses et …

Oui, je pense que vous avez déjà entendu cela quelque part. Nommer les choses peut être difficile, mais cela ne signifie pas que vous ne devriez pas y réfléchir, ou devenir complètement cryptique.

Je doute qu'il y ait une situation où il soit judicieux d'utiliser des lettres simples comme noms de classe.

```
.u {  font-size: 60rem;}
```

Et qu'en est-il des noms de classe super-spécifiques ?

```
.former-black-now-red-paragraph {  color: red;}
```

Ceux-ci ne font pas de bien non plus.

Bien que le nom puisse sembler transmettre un certain sens, vous avez très probablement brisé une grande partie de la réutilisabilité de la classe. Ce qui, soit dit en passant, est la raison principale d'avoir des classes.

Maintenant, si vous vouliez styliser un paragraphe `red` régulier, le nom précédent est si spécifique qu'il n'aurait pas de sens.

Utilisez des noms significatifs, mais ne les surchargez pas.

#### J'ai entendu dire que les classes étaient géniales. Abusez-en !

![Image](https://cdn-media-1.freecodecamp.org/images/Lf3jWnJxes3KHuGApVOUOjhq3dgc4TDOBOga)
_hmmm… Quand c'est possible, évitez les classes trop modulaires_

Les classes sont géniales, et tout le monde les aime. Mais, comme pour tout le reste, trop de quelque chose est généralement une mauvaise idée.

Vous voyez, si un groupe de classes sera principalement utilisé ensemble, regroupez-les simplement en une seule classe.

Quand vous choisissez de regrouper ces classes est peut-être subjectif. Si vous construisez une bibliothèque atomique de quelque sorte, vous pourriez tendre vers cela.

Si vous écrivez une grande application, vous êtes probablement mieux loti en regroupant les classes de manière significative, plutôt que d'avoir une tonne de classes sur un seul élément.

Quand c'est possible, évitez les classes trop modulaires.

#### Je suis un puriste du CSS. Je ne fais pas de SASS, LESS, etc.

Vous êtes un puriste du CSS, je suis un puriste du CSS, nous sommes tous les deux puristes. Mettons cela de côté.

Maintenant, au cœur du différend.

Il y a définitivement des cas d'utilisation où écrire simplement du CSS vanilla est génial ! Par exemple, si je n'utilise pas de solution [CSS-in-JS](https://hackernoon.com/all-you-need-to-know-about-css-in-js-984a72d48ebc) pour mes projets [React](http://reacts.org), je pourrais décider de prendre la route du CSS pur. Cela ne fait pas de mal.

Cependant, si vous écrivez une grande application avec une tonne de CSS vanilla qui traîne, je parie qu'introduire un préprocesseur CSS rendra votre développement plus intéressant et contribuera à une base de code CSS plus maintenable.

Encore une fois, je ne dis pas d'utiliser des préprocesseurs à chaque fois. Je dis simplement de ne pas fermer cette option. Cela pourrait vous sauver !

#### Vous avez beaucoup de style _Important_ là !

![Image](https://cdn-media-1.freecodecamp.org/images/N6QGbrfgLCAKgecAbfzrNyCfMxjXtcebzvHm)

Je déteste le CSS. Cela ne fonctionne jamais. Alors, quelle est la solution ?

Avoir une tonne de `!important` partout quand j'ai besoin de remplacer des déclarations. Haha !

Bien que cela semble être un plan décent pour votre moi paresseux, l'utilisation excessive de la règle `!important` ne résultera que dans un document CSS grossièrement difficile à maintenir.

La prochaine fois que vous aurez besoin d'utiliser `!important`, [assurez-vous](https://css-tricks.com/when-using-important-is-the-right-choice/) de ne pas le faire parce que vous êtes trop paresseux pour corriger vos problèmes de cascade.

[Le CSS n'est pas si mauvais. Embrassez-le.](https://medium.freecodecamp.org/the-most-important-css-concept-to-learn-8e929c944a19)

#### Vous voulez écrire un meilleur CSS ?

J'ai créé un guide CSS gratuit pour faire décoller vos compétences en CSS, immédiatement. [Obtenez l'ebook gratuit](https://pages.convertkit.com/0c2c62e04a/60e5d19f9b).

![Image](https://cdn-media-1.freecodecamp.org/images/qdjk1yXX4UbyuwxJGbKmQchX4aYmmJAN1VZ2)
_Sept secrets CSS que vous ne connaissiez pas_