---
title: Span HTML – Comment utiliser la balise Span avec CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-08T01:18:28.000Z'
originalURL: https://freecodecamp.org/news/span-html-how-to-use-the-span-tag-with-css
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/span-tag.png
tags:
- name: JavaScript
  slug: javascript
seo_title: Span HTML – Comment utiliser la balise Span avec CSS
seo_desc: "You can use the HTML span tag as a container to group inline elements together\
  \ so you can style or manipulate them with JavaScript. \nIn this article, I will\
  \ show you how to use the span tag to make a certain part of your content distinct\
  \ from the res..."
---

Vous pouvez utiliser la balise HTML `span` comme conteneur pour regrouper des éléments en ligne afin de les styliser ou de les manipuler avec JavaScript. 

Dans cet article, je vais vous montrer comment utiliser la balise span pour rendre une partie spécifique de votre contenu distincte du reste. Ensuite, vous pourrez commencer à l'utiliser dans vos projets de codage.

## À quoi sert la balise `span` ?

La balise `span` est similaire à une div, utilisée pour regrouper du contenu similaire afin qu'il puisse être stylisé ensemble. 

Mais `span` est différente car c'est un élément en ligne, contrairement à `div`, qui est un élément de bloc.

De plus, gardez à l'esprit que `span` n'a aucun effet sur son contenu à moins de le styliser.

Il y a deux utilisations majeures de la balise `span` – le style et la manipulation d'un texte particulier avec JavaScript.

### Comment styliser du texte avec la balise `span`

Si vous souhaitez rendre un texte particulier ou tout autre contenu différent du reste, vous pouvez l'envelopper dans une balise `span`, lui donner un attribut de classe, puis le sélectionner avec la valeur de l'attribut pour le styliser.

Dans les exemples ci-dessous, je change la `couleur`, la `couleur de fond` et le `style de police` de certains textes en les enveloppant dans une balise `span`. 

#### Comment changer la couleur du texte

```html
<p>This a <span class="crimson-text">crimson text</span> within others.</p>
```

```css
.crimson-text {
      color: crimson;
   }
```


J'ai ajouté un peu de CSS de base pour centrer tout sur la page :

```css
body {
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        height: 100vh;
      }
```

![text-color-span](https://www.freecodecamp.org/news/content/images/2021/09/text-color-span.png)

#### Comment changer la couleur de fond

```html
<p>
      A <span class="green-background">green background color</span> perfectly
      implies the beauty of nature.
</p>
```

```css
 .green-background {
        background-color: #2ecc71;
      }
```

![background-color-span](https://www.freecodecamp.org/news/content/images/2021/09/background-color-span.png)

#### Comment changer le style de police

```html
<p>
   An <span class="font-style">italic</span> font style could be instrumental
   in laying emphasis on a text.
</p>
```

```
.font-style {
     font-style: italic;
   }
```

 ![font-style-span](https://www.freecodecamp.org/news/content/images/2021/09/font-style-span.png)
 
### Comment manipuler JavaScript avec la balise `span` 

Tout comme il est possible de styliser du contenu en enveloppant une balise `span` autour, vous pouvez également manipuler votre contenu en l'enveloppant dans une balise `span`. Vous lui donnez un attribut `id` puis vous le sélectionnez par son id avec JavaScript afin de le manipuler.

Dans l'exemple ci-dessous, j'ai changé un texte en majuscules avec JavaScript :

```html
<p>
   The text, <span id="uppercase"> freecodecamp</span>, was turned to
   upperase with JavaScript
</p>
```

```js
const uppercase = document.querySelector("#uppercase");

uppercase.style.textTransform = "uppercase";
```

![javascript-span](https://www.freecodecamp.org/news/content/images/2021/09/javascript-span.png)

## Conclusion 

Dans ce tutoriel, vous avez appris comment manipuler une partie spécifique de texte avec CSS et JavaScript en l'enveloppant dans une balise `span` et en lui donnant un attribut `class` ou `id` unique. 

Veuillez noter que dans des cas comme celui-ci, vous devriez utiliser des classes pour le style et des ids pour la manipulation avec JavaScript afin d'éviter toute confusion. 

Merci d'avoir lu, et continuez à coder.