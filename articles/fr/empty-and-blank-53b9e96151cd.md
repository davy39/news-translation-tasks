---
title: Quand utiliser les pseudo-sélecteurs CSS :empty et :blank
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-09-18T22:12:41.000Z'
originalURL: https://freecodecamp.org/news/empty-and-blank-53b9e96151cd
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca9e4740569d1a4ca8771.jpg
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Quand utiliser les pseudo-sélecteurs CSS :empty et :blank
seo_desc: 'I made a terrible mistake when I tweeted about :empty and :blank a while
  ago. I said that :empty wasn’t useful, and :blank is much more useful than :empty.


  I was wrong!

  :empty is actually good enough. We don’t even need :blank!

  A quick introduction

  ...'
---

J'ai fait une terrible erreur lorsque j'ai tweeté à propos de `:empty` et `:blank` il y a quelque temps. J'ai dit que `:empty` n'était pas utile, et que `:blank` est beaucoup plus utile que `:empty`.

![Image](https://cdn-media-1.freecodecamp.org/images/vsw0KkV-ZfP8LtM29iCh0QOcEBaiV9Xy-F9C)

J'avais tort !

`:empty` est en fait suffisamment bon. Nous n'avons même pas besoin de `:blank` !

#### Une rapide introduction

D'abord, qu'est-ce que `:empty` et qu'est-ce que `:blank` ?

`:empty` est un pseudo-sélecteur. Il vous permet de sélectionner des éléments qui sont vides.

```
/* Ceci est du CSS */
```

```
:empty { /* faire quelque chose */}
```

Les éléments vides sont des éléments qui n'ont rien à l'intérieur. Ils ne peuvent même pas avoir un espace blanc.

```
<!-- Ceci est du HTML -->
```

```
<!-- Exemple d'un élément vide --><div></div>
```

Les éléments vides peuvent avoir des commentaires, tant que les commentaires remplissent entièrement l'élément.

```
<!-- Ceci est du HTML -->
```

```
<!-- Les éléments vides peuvent avoir des commentaires --><div><!-- ceci est un commentaire --></div>
```

`:blank` est une version améliorée de `:empty`. Il vous permet de sélectionner des éléments qui contiennent des espaces blancs :

```
<!-- Ceci est du HTML -->
```

```
<!-- Correspond à :blank mais pas à :empty --><div> </div>
```

`:empty` et `:blank` sont utiles si vous avez besoin de :

1. Styliser un élément vide
2. Créer des états vides

#### Un exemple

Supposons que vous avez une `<div>`. Vous ne remplirez cette `<div>` avec du contenu que lorsqu'une erreur se produit.

```
<!-- Ceci est du HTML -->
```

```
<!-- Sans erreurs --><div class="error"></div>
```

```
<!-- Avec erreurs --><div class="error">Oups ! Quelque chose s'est mal passé !</div>
```

Ici, vous devez styliser la div `.error`. Si vous n'utilisez pas `:empty`, vous devez vous appuyer sur une classe ou un attribut. Cela semble redondant.

```
<!-- Ceci est du HTML -->
```

```
<!-- Avec erreurs --><div class="error" data-state="error">Oups ! Quelque chose s'est mal passé !</div>
```

```
/* Ceci est du CSS */
```

```
.error { display: none; background-color: hsl(0, 20%, 50%); padding: 0.5em 0.75em;}
```

```
.error[data-state="error"] { display: block;}
```

Mais si vous utilisez `:empty`, vous n'avez pas besoin de la classe ou de l'attribut supplémentaire. Vous pouvez styliser directement la classe `.error`. Vous n'avez même pas besoin de `display: none;` !

```
/* Ceci est du CSS */
```

```
.error { background-color: hsl(0, 20%, 50%); padding: 0.5em 0.75em;}
```

```
.error:empty { padding: 0;}
```

Voici un codepen [Démonstration Empty](https://codepen.io/zellwk/pen/JaPgdN/) que j'ai créé pour que vous puissiez jouer avec (essayez de supprimer le `padding: 0;` de `.error:empty`, vous verrez un fond rouge ?).

Supposons que vous souhaitez créer une liste de tâches. Lorsque vos utilisateurs voient la liste de tâches pour la première fois, ils verront probablement zéro élément de tâche.

Que montrez-vous lorsqu'il n'y a aucune tâche ?

Cet état de zéro tâche est ce que nous appelons un état vide.

Si vous souhaitez créer un état vide pour votre liste de tâches, vous pouvez ajouter une `<div>` supplémentaire après votre `<ul>`. Lorsque vous le faites, vous pouvez utiliser une combinaison de `:empty` et du sélecteur + (frère adjacent) ou ~ (frère suivant) pour styliser l'état vide.

```
<!-- Ceci est du HTML -->
```

```
<ul> <li>Élément 1</li> <li>Élément 2</li> <li>Élément 3</li></ul><div class="empty-state"></div>
```

```
/* Ceci est du CSS */
```

```
.empty-state { display: none;}
```

```
ul:empty + .empty-state { display: block;}
```

J'ai appris à utiliser `:empty` de cette manière grâce à Heydon Pickering. Consultez [l'article de Heydon](https://inclusive-components.design/a-todo-list/) sur [Inclusive Components](https://inclusive-components.design/) si vous souhaitez voir l'exemple de la liste de tâches en action.

> Note : les états vides sont importants. Si vous avez besoin d'être convaincu, consultez [cet article](https://www.invisionapp.com/blog/why-empty-states-deserve-more-design-time/) sur Invision.

#### Décomposer mon raisonnement

`:empty` est souvent suffisant en pratique. J'ai pensé que `:empty` n'était pas assez bon pour deux raisons :

1. Mauvaise expérience développeur
2. Je devrais supprimer les espaces blancs manuellement avec JavaScript

La première raison est valable, mais ce n'est pas un gros problème.

**La deuxième raison n'est pas valable**. J'ai supposé que je devais supprimer les espaces blancs, mais ce n'est pas nécessaire.

Je vais vous expliquer les deux.

Revenons à l'exemple de la liste de tâches. Supposons que nous avons créé une liste de tâches et que nous avons ce balisage.

```
<!-- Ceci est du HTML -->
```

```
<ul> <li>Élément 1</li> <li>Élément 2</li> <li>Élément 3</li></ul><div class="empty-state"></div>
```

Comment vérifieriez-vous si `:empty` fonctionne ?

Eh bien, je supprimerais chaque `<li>` avec cmd + x. Cette commande coupe toute la ligne. Lorsque j'ai supprimé les trois `<li>`, je me retrouve avec ce balisage :

```
<!-- Ceci est du HTML -->
```

```
<ul></ul>
```

À ce stade, vous saurez que le HTML ci-dessus ne déclenchera pas `:empty`. `:empty` ne fonctionne que lorsqu'il n'y a pas d'espaces blancs dans l'élément.

J'ai dû supprimer les espaces blancs pour que `:empty` fonctionne, ce qui signifie quelques frappes supplémentaires. C'était une corvée que j'espérais ne pas avoir à faire.

Mais après tout, c'est un petit problème pour un grand bénéfice.

Je le répète. **Vous n'avez pas besoin de supprimer les espaces blancs manuellement en JavaScript** si vous utilisez `:empty`. J'ai fait une mauvaise supposition.

Prenons un exemple et vous verrez ce que je veux dire. Nous utiliserons à nouveau l'exemple de la liste de tâches.

Supposons que nous avons ce HTML pour l'instant :

```
<!-- Ceci est du HTML -->
```

```
<ul> <li>Élément 1</li></ul><div class="empty-state"></div>
```

Pour que l'état vide fonctionne, nous devons supprimer le dernier élément `<li>` de `<ul>`. Si vous utilisez du JavaScript simple, vous pouvez faire cela avec `removeChild`.

```
// Ceci est du JavaScript
```

```
const ul = document.querySelector('ul')const li = ul.children[0]
```

```
ul.removeChild(li)
```

Je croyais (à tort) que `removeChild` produirait ce HTML :

```
<!-- Ceci est du HTML -->
```

```
<ul></ul>
```

Si cela produisait ce HTML, je devrais supprimer tout espace blanc restant dans la liste (ce qui est du JavaScript supplémentaire).

```
// Ceci est du JavaScript
```

```
const ul = document.querySelector('ul')const li = ul.children[0]
```

```
ul.removeChild(li)
```

```
if (ul.children.length === 0) { ul.innerHTML = ''}
```

Comme je l'ai dit, j'avais tort. Cela n'a pas produit le HTML ci-dessus. Au lieu de cela, voici ce qu'il a produit :

```
<!-- Ceci est du HTML -->
```

```
<ul></ul>
```

Ce qui signifie que nous n'avions pas besoin du JavaScript supplémentaire pour supprimer les espaces blancs !

> Avertissement : J'ai vérifié la sortie sur Safari, Chrome et Firefox. Je n'ai pas encore vérifié Edge. Je serais très reconnaissant si vous pouviez m'aider à le tester !

Voici le code pour cet exemple :

Voir le stylo [Démonstration Empty avec todolist](https://codepen.io/zellwk/pen/ZMzgJp/) que j'ai créé ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

`:empty` est supporté sur tous les navigateurs, et `:blank` a un faible support navigateur. Cela vous donne de nombreuses raisons d'utiliser `:empty` plutôt que `:blank` aujourd'hui !

![Image](https://cdn-media-1.freecodecamp.org/images/0uAx8kJC7pr98VvkEYqphhJ3BD00BfPuNuJ2)

J'espère que le support navigateur pour `:blank` s'améliorera un jour.

#### Conclusion

`:empty` et `:blank` vous permettent de styliser des éléments vides et de produire des états vides facilement.

`:blank` est meilleur que `:empty` car il nous offre une meilleure expérience développeur. Mais nous ne pouvons pas utiliser `:blank` car `:blank` n'a pas assez de support navigateur.

`:empty` est souvent suffisamment bon. Vous pouvez déjà l'utiliser. Utilisez-le autant que vous le souhaitez ! ?

Essayez `:empty` et faites-moi savoir ce que vous en pensez !

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=%3Aempty%20and%20%3Ablank%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/empty-and-blank/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/empty-and-blank).

Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.