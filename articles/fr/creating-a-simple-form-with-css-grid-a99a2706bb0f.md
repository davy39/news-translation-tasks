---
title: Comment créer un formulaire simple avec CSS Grid
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-11-08T04:51:59.000Z'
originalURL: https://freecodecamp.org/news/creating-a-simple-form-with-css-grid-a99a2706bb0f
coverImage: https://cdn-media-1.freecodecamp.org/images/0*ZwG-auUyjJiPLU3P.png
tags:
- name: CSS
  slug: css
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: UI
  slug: ui
- name: UX
  slug: ux
seo_title: Comment créer un formulaire simple avec CSS Grid
seo_desc: 'You learned to create a simple form with Flexbox in the previous article.
  Today, you’ll understand how to create the same thing with CSS Grid.

  Here’s what we’re building:


  Building the form with CSS Grid

  From the picture above, we know the form conta...'
---

Vous avez appris à créer un formulaire simple avec Flexbox dans [l'article précédent](https://zellwk.com/blog/simple-form-with-flexbox). Aujourd'hui, vous allez comprendre comment créer la même chose avec CSS Grid.

Voici ce que nous allons construire :

![Image](https://cdn-media-1.freecodecamp.org/images/h4IM1DtbqMnvHdQDWjbAjyTB8HFHB8hBc3KV)

### Construire le formulaire avec CSS Grid

D'après l'image ci-dessus, nous savons que le formulaire contient deux éléments :

1. Un champ email
2. Un bouton de soumission

Voici le HTML :

```
<form>   <input type="email" name="email">   <button type="submit">Envoyer</button> </form>
```

Pour construire le formulaire avec CSS Grid, vous devez définir la propriété `display` du parent sur `grid`.

```
form {   display: grid; }
```

Voici ce que vous obtenez :

![Image](https://cdn-media-1.freecodecamp.org/images/wWF5gknxOICW0uVNJULglsbw9Tq8HjUXy7CS)

Pourquoi avons-nous obtenu deux lignes ?

Nous obtenons deux lignes parce que nous n'avons pas spécifié le nombre de colonnes pour la grille. Les navigateurs utiliseront toujours une colonne par défaut.

Pour ce formulaire, nous devons définir deux colonnes.

1. La première colonne doit s'étendre pour remplir tout espace disponible
2. La deuxième colonne doit être dimensionnée selon son contenu

Pour la première colonne, nous pouvons utiliser l'unité `fr`. Pour la deuxième colonne, nous pouvons utiliser `auto`.

```
form {   display: grid;   grid-template-columns: 1fr auto; }
```

Avec cela, vous avez terminé la mise en page du formulaire. Voici un Codepen pour vous amuser :

[Formulaire simple avec CSS Grid](https://codepen.io/zellwk/pen/qMLErJ/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Lorsque les éléments sont de hauteur inégale

Nous allons simuler des éléments de hauteur inégale en remplaçant le texte du `button` par un SVG. [C'est la même chose que ce que nous avons fait dans l'article précédent](https://zellwk.com/blog/simple-form-with-flexbox).

```
<form action="#">   <input type="email" placeholder="Entrez votre email">   <button type="button"><svg> <!-- une icône smiley --> </svg></button> </form>
```

![Image](https://cdn-media-1.freecodecamp.org/images/2fkg2F6SaWOZfNDsonfP1joVRlDl-eIlHjCs)

Remarquez que la hauteur de l'`input` augmente également pour s'adapter à la grande icône SVG ! Une fois de plus, nous n'avons pas besoin d'écrire de code supplémentaire. Cela se produit parce que les éléments de la grille sont étirés verticalement pour remplir tout espace disponible.

Si vous souhaitez changer ce comportement, vous pouvez modifier la propriété `align-items` en `start`, `end`, ou `center`.

![Image](https://cdn-media-1.freecodecamp.org/images/TZFrmkspxaoTilvhtb7K2CqB9qhDZLiwSgaM)

Voici un Codepen pour vous amuser :

[Formulaire simple avec CSS Grid (avec bouton SVG)](https://codepen.io/zellwk/pen/jvXEzm/) par Zell Liew ([@zellwk](https://codepen.io/zellwk)) sur [CodePen](https://codepen.io/).

### Conclusion

CSS Grid facilite la création de mises en page. Il n'a pas besoin d'être utilisé uniquement pour les macro-mises en page. Il peut également être utilisé pour des micro-mises en page comme l'exemple de formulaire que vous avez vu ici.

Amusez-vous avec CSS Grid !

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Creating%20a%20simple%20form%20with%20CSS%20Grid%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/simple-form-with-css-grid/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/simple-form-with-css-grid).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.