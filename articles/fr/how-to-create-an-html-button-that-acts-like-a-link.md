---
title: Comment créer un bouton HTML qui agit comme un lien
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-02T22:05:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-an-html-button-that-acts-like-a-link
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9e4f740569d1a4ca3c6e.jpg
tags:
- name: HTML
  slug: html
seo_title: Comment créer un bouton HTML qui agit comme un lien
seo_desc: 'Sometimes you may want to use a button to link to another page or website
  rather than to submit a form or something like that. This is fairly simple to do
  and can be achieved in several ways.

  How to Create an HTML Button Using the Button Tag in an A ...'
---

Parfois, vous pouvez vouloir utiliser un bouton pour lier à une autre page ou site web plutôt que pour soumettre un formulaire ou quelque chose de similaire. Cela est assez simple à faire et peut être réalisé de plusieurs manières.

## Comment créer un bouton HTML en utilisant la balise Button dans une balise A

Une façon est de simplement envelopper votre balise `<button>` dans une balise `<a>` :

```html
<a href='https://www.freecodecamp.org/'><button>Lien vers freeCodeCamp</button></a>
```

Cela transforme votre bouton entier en un lien.

## Comment transformer un lien en bouton avec CSS

Une deuxième option est de créer votre lien comme vous le feriez normalement avec votre balise `<a>` puis de le styliser via CSS :

```html
<a href='https://www.freecodecamp.org/'>Lien vers freeCodeCamp</a>
```

Une fois que vous avez créé votre lien, vous pouvez utiliser CSS pour lui donner l'apparence d'un bouton. Par exemple, vous pourriez ajouter une bordure, une couleur de fond, des styles pour lorsque l'utilisateur survole le lien.

Vous pouvez [lire plus sur le stylisme des liens avec CSS ici](https://www.freecodecamp.org/news/a-quick-guide-to-styling-buttons-using-css-f64d4f96337f/).

## Comment mettre un bouton à l'intérieur d'un formulaire en utilisant HTML

Une autre façon d'ajouter un bouton est d'envelopper un `input` à l'intérieur de balises `form`. Spécifiez l'URL cible souhaitée dans l'attribut d'action du formulaire.

```html
<form action="http://google.com">
    <input type="submit" value="Aller sur Google" />
</form>
```

J'espère que vous avez trouvé ce tutoriel utile. Bon codage.