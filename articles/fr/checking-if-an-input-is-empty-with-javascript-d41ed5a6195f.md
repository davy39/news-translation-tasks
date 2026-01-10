---
title: Comment vérifier si une entrée est vide avec JavaScript
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-03-14T07:09:27.000Z'
originalURL: https://freecodecamp.org/news/checking-if-an-input-is-empty-with-javascript-d41ed5a6195f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*YK6dG3FqhIXZgD3x.gif
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment vérifier si une entrée est vide avec JavaScript
seo_desc: 'Last week, I shared how to check if an input is empty with CSS. Today,
  let’s talk about the same thing, but with JavaScript.

  It’s much simpler.

  Here’s what we’re building:


  Events to validate the input

  If you want to validate the input when a user ty...'
---

La semaine dernière, j'ai partagé comment [vérifier si une entrée est vide avec CSS](https://zellwk.com/blog/check-empty-input-css). Aujourd'hui, parlons de la même chose, mais avec JavaScript.

C'est beaucoup plus simple.

Voici ce que nous construisons :

![Image](https://cdn-media-1.freecodecamp.org/images/J-TSs6H2P10YzT6HqW1U29C6zTZlrIYDh2B0)

### Événements pour valider l'entrée

Si vous souhaitez valider l'entrée lorsque l'utilisateur tape dans le champ, vous pouvez utiliser l'événement `input`.

```
const input = document.querySelector('input')input.addEventListener('input', evt => {  // Valider l'entrée})
```

Si vous souhaitez valider l'entrée lorsque l'utilisateur soumet un formulaire, vous pouvez utiliser l'événement `submit`. Assurez-vous de prévenir le comportement par défaut avec `preventDefault`.

Si vous ne prévenez pas le comportement par défaut, les navigateurs redirigeront l'utilisateur vers l'URL indiquée dans l'attribut action.

```
const form = document.querySelector('form')form.addEventListener('submit', evt => {  evt.preventDefault()
```

```
// Valider l'entrée})
```

### Validation de l'entrée

Nous voulons savoir si une entrée est vide. Pour notre usage, vide signifie :

1. L'utilisateur n'a rien tapé dans le champ
2. L'utilisateur a tapé un ou plusieurs espaces vides, mais pas d'autres caractères

En JavaScript, les conditions de réussite/échec peuvent être représentées comme suit :

```
// Vide
''  ' '   '  '
```

```
// Rempli
'one-word'
'one-word '
' one-word'
' one-word '
'one phrase with whitespace'
'one phrase with whitespace '
' one phrase with whitespace'
' one phrase with whitespace '
```

Vérifier cela est facile. Nous devons simplement utiliser la méthode `trim`. `trim` supprime tout espace blanc au début et à la fin d'une chaîne.

```
const value = input.value.trim()
```

Si l'entrée est valide, vous pouvez définir `data-state` sur `valid`. Si l'entrée est invalide, vous pouvez définir `data-state` sur `invalid`.

```
// Ceci est du JavaScript 
```

```
input.addEventListener('input', evt => {  const value = input.value.trim()
```

```
if (value) {    input.dataset.state = 'valid'  } else {    input.dataset.state = 'invalid'  }})
```

```
/* Ceci est du CSS */
```

```
/* Afficher des bordures rouges lorsque rempli, mais invalide */input[data-state="invalid"] {  border-color: hsl(0, 76%, 50%);}
```

```
/* Afficher des bordures vertes lorsque valide */input[data-state="valid"] {  border-color: hsl(120, 76%, 50%);}Ce n'est pas encore la fin. Nous avons un problème.
```

Lorsque l'utilisateur entre du texte dans le champ, la validation de l'entrée commence. Cependant, si l'utilisateur supprime tout le texte du champ, l'entrée continue d'être invalide.

Nous ne voulons pas invalider l'entrée si l'utilisateur supprime tout le texte. Ils peuvent avoir besoin d'un moment pour réfléchir, mais l'état invalidé déclenche une alarme inutile.

![Image](https://cdn-media-1.freecodecamp.org/images/dsKKfAA91i2Uz5MVxMBJ531ya-j0s9bsQ5zo)

Pour corriger cela, nous pouvons vérifier si l'utilisateur a entré du texte dans l'entrée avant de le `trim`.

```
input.addEventListener('input', evt => {  const value = input.value
```

```
if (!value) {    input.dataset.state = ''    return  }
```

```
const trimmed = value.trim()
```

```
if (trimmed) {    input.dataset.state = 'valid'  } else {    input.dataset.state = 'invalid'  }})
```

Voici un Codepen pour vous amuser :

Voir le stylo [Validation vide avec JavaScript](https://codepen.io/zellwk/pen/EObQpr/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=Checking%20if%20an%20input%20is%20empty%20with%20JavaScript%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/check-empty-input-js/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/check-empty-input-js).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.