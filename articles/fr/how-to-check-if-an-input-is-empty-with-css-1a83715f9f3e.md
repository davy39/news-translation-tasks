---
title: Comment vérifier si une entrée est vide avec CSS
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-12-28T23:32:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-check-if-an-input-is-empty-with-css-1a83715f9f3e
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1N9VIZ7wJ7Kq_iqQ.gif
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
- name: Web Development
  slug: web-development
seo_title: Comment vérifier si une entrée est vide avec CSS
seo_desc: 'Is it possible to know if an input is empty with only CSS?

  I had that question when I tried to make an autocomplete component for Learn JavaScript.
  Basically, I wanted to:


  Hide a drop-down if the input is empty

  Show the drop-down if the input is fil...'
---

Est-il possible de savoir si une entrée est vide avec seulement du CSS ?

J'ai eu cette question lorsque j'ai essayé de créer un composant d'autocomplétion pour Learn JavaScript. Basiquement, je voulais :

1. Masquer une liste déroulante si l'entrée est vide
2. Afficher la liste déroulante si l'entrée est remplie

![Image](https://cdn-media-1.freecodecamp.org/images/yyt7BfywizCAjffJaHpmuVSIGNarprZTgj87)

J'ai trouvé un moyen de le faire. Ce n'est pas parfait. Il y a quelques nuances impliquées, mais je veux le partager avec vous.

### Le formulaire

Tout d'abord, construisons un formulaire pour être sur la même page. Nous allons utiliser un formulaire simple avec une entrée.

```
<form>  <label for="input"> Entrée </label>  <input type="text" id="input" /></form>
```

Lorsque l'entrée est remplie, nous voulons changer sa `border-color` en vert. Voici un exemple de ce que nous créons :

![Image](https://cdn-media-1.freecodecamp.org/images/3Ta3zBaP2zckvzN9II60OJhn1EXzzNRfcwnd)

### Vérifier si l'entrée est vide

Je me suis appuyé sur la validation de formulaire HTML pour vérifier si l'entrée était vide. Cela signifiait que j'avais besoin d'un attribut `required`.

```
<form>  <label> Entrée </label>  <input type="text" name="input" id="input" required /></form>
```

À ce stade, cela fonctionnait bien lorsque l'entrée était remplie. Les bordures devenaient vertes.

![Image](https://cdn-media-1.freecodecamp.org/images/Fr40-RMCPUjeTD6Y3GJ3MK4VJUf-jqCHSw9e)

Mais il y avait un problème : si l'utilisateur entre un espace dans le champ, les bordures deviennent également vertes.

![Image](https://cdn-media-1.freecodecamp.org/images/y-kZqMJhxDWcisrzGnyqwMQNJ2BtCUVu1hB5)

Techniquement, c'est correct. L'entrée est remplie parce que l'utilisateur a tapé quelque chose dedans.

Mais je ne voulais pas que les espaces déclenchent un menu déroulant vide (pour le composant d'autocomplétion).

Ce n'était pas suffisant. J'avais besoin d'une vérification plus stricte.

### Vérifications supplémentaires

HTML vous donne la possibilité de valider les entrées avec des expressions régulières grâce à l'attribut `pattern`. J'ai décidé de le tester.

Puisque je ne voulais pas que les espaces soient reconnus, j'ai commencé avec le motif `\S+`. Ce motif signifiait : Un ou plusieurs caractères qui ne sont pas des espaces.

```
<form>  <label> Entrée </label>  <input type="text" name="input" id="input" required pattern="\S+"/></form>
```

En effet, cela a fonctionné. Si un utilisateur entre un espace dans le champ, l'entrée n'est pas validée.

![Image](https://cdn-media-1.freecodecamp.org/images/jWR2WuP91tUOox5ZmYcKvq6sYRFFGmh09C4g)

Mais lorsqu'un espace est entré (n'importe où) dans l'entrée, l'entrée est invalidée.

![Image](https://cdn-media-1.freecodecamp.org/images/JVKUWbAqxbWQZ2sDtV9XjMYKfEAmaaE46Sg7)

Malheureusement, ce motif ne fonctionnait pas dans mon cas d'utilisation.

Dans le composant d'autocomplétion de Learn JavaScript, j'enseignais aux étudiants comment compléter une liste de pays. Les noms de certains pays contenaient des espaces...

![Image](https://cdn-media-1.freecodecamp.org/images/G0iQiqeU5xFkv7AlHXj30Z8Bn5JQ9Kj2MfxY)

Je devais inclure les espaces dans le mélange.

La meilleure alternative suivante à laquelle j'ai pensé est `\S+.*`. Cela signifie 1 ou plusieurs caractères non-espace, suivis de zéro ou plusieurs (n'importe quels) caractères.

```
<form>  <label> Entrée </label>  <input type="text" name="input" id="input" required pattern="\S+.*"/></form>
```

Cela a fonctionné ! Je peux maintenant entrer des espaces dans le mélange !

![Image](https://cdn-media-1.freecodecamp.org/images/x2YDLSVq2CmaVUd1nlQCqo0IKCrwBOQqymwx)

Mais il y a un autre problème... l'entrée n'est pas validée si vous commencez par un espace...

![Image](https://cdn-media-1.freecodecamp.org/images/CT8NoxhJxCE8LM-5j9y6lMNstA3K0z37Okw8)

Et c'est le problème que je n'ai pas pu résoudre. Plus sur cela plus tard.

Lorsque j'ai travaillé sur cet article, je suis tombé sur une autre question intéressante : Est-il possible de styliser un état invalide lorsque l'entrée est remplie incorrectement ?

### Invalider l'entrée

Nous ne voulons pas utiliser `:invalid` car nous allons démarrer l'entrée avec un état invalide. (Lorsque l'entrée est vide, elle est déjà invalide).

C'est là que Chris Coyier est intervenu pour sauver la situation avec « [Form Validation UX in HTML and CSS](https://css-tricks.com/form-validation-ux-html-css/) ».

Dans l'article, Chris parle d'une pseudo-classe `:placeholder-shown`. Elle peut être utilisée pour vérifier si un placeholder est affiché.

L'idée est :

1. Vous ajoutez un placeholder à votre entrée
2. Si le placeholder est masqué, cela signifie que l'utilisateur a tapé quelque chose dans le champ
3. Procédez à la validation (ou à l'invalidation)

Voici le CSS (version simplifiée. Pour la version complète, consultez [l'article de Chris](https://css-tricks.com/form-validation-ux-html-css/).)

```
/* Afficher des bordures rouges lorsque rempli, mais invalide */input:not(:placeholder-shown) {  border-color: hsl(0, 76%, 50%);}
```

Puisque j'avais à la fois des styles de validation ET d'invalidation, je devais m'assurer que les styles valides venaient après les styles invalides.

```
/* Afficher des bordures rouges lorsque rempli, mais invalide */input:not(:placeholder-shown) {  border-color: hsl(0, 76%, 50%);;}
```

```
/* Afficher des bordures vertes lorsque valide */input:valid {  border-color: hsl(120, 76%, 50%);}
```

Voici une démo pour que vous puissiez jouer avec :

Voir le stylo [Pure CSS Empty validation](https://codepen.io/zellwk/pen/dgEKxX/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

Note : Edge ne supporte pas `:placeholder-shown`, donc ce n'est probablement pas une bonne idée de l'utiliser en production pour l'instant. Il n'y a pas de bon moyen de détecter cette fonctionnalité.

Maintenant, revenons au problème que je n'ai pas pu résoudre.

### Le problème avec pattern

L'attribut `pattern` est merveilleux car il vous permet d'accepter une expression régulière. Cette expression régulière vous permet de valider l'entrée avec tout ce à quoi vous pouvez penser.

Mais... **l'expression régulière doit correspondre complètement au texte**. Si le texte n'est pas complètement correspondant, l'entrée est invalidée.

Cela a créé le problème que j'ai mentionné ci-dessus. (Rappel du problème : Si un utilisateur entre un espace en premier, l'entrée devient invalide).

Je n'ai pas pu trouver une expression régulière qui fonctionnait pour tous les cas d'utilisation auxquels j'ai pensé. Si vous voulez essayer de créer une expression régulière dont j'ai besoin, je serais plus qu'heureux de recevoir de l'aide !

Voici les cas d'utilisation :

```
// Ne devrait pas correspondre''' ''  ''   '
```

```
// Devrait correspondre'one-word''one-word '' one-word'' one-word ''one phrase with whitespace''one phrase with whitespace '' one phrase with whitespace'' one phrase with whitespace '
```

(Encore une fois, je peux peut-être trop y penser... ?).

### Mise à jour : Problème résolu !

De nombreux lecteurs ont été assez généreux pour m'envoyer leurs solutions. Je veux remercier tout le monde qui a aidé. Merci beaucoup !

La solution la plus propre que j'ai reçue est : `.*\S.*` par [Daniel O'Connor](https://www.nvinteractive.com/). Cela signifie :

* `.*` : N'importe quel caractère
* `\S` : Suivi d'_un_ caractère non-espace
* `.*` : Suivi de n'importe quel caractère

D'autres expressions régulières que j'ai reçues incluent :

* `.*\S+.*` par [Matt Mink](https://twitter.com/matthewjmink)
* `\s*\S.*` par [Sungbin Jo](https://github.com/pcr910303)
* `^\s?(?=\S).` avec une assertion par [Konstantin](https://twitter.com/KonstantinRouda)

Et beaucoup d'autres !

Voici un [codepen](https://codepen.io/zellwk/pen/NeRaPw/) avec la solution mise à jour par Daniel.

### Conclusion

Oui, il est possible de valider un formulaire avec du CSS pur. Il y a des problèmes potentiels avec la validation lorsque des caractères d'espace sont impliqués.

Si vous ne vous souciez pas des espaces, cela fonctionne parfaitement. Amusez-vous à essayer ce motif ! (Désolé, je ne peux pas m'en empêcher).

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=Checking%20if%20an%20input%20is%20empty%20with%20CSS%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/check-empty-input-css/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/check-empty-input-css). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.