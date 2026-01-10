---
title: Comment changer la couleur du texte en HTML – Tutoriel sur le style de police
subtitle: ''
author: Joel Olawanle
co_authors: []
series: null
date: '2022-09-12T20:45:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-change-text-color-in-html
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/cover-template--6-.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
seo_title: Comment changer la couleur du texte en HTML – Tutoriel sur le style de
  police
seo_desc: 'Text plays a significant role on our web pages. This is because it helps
  users learn what the web page is all about and what they can do there.

  When you add text to your web pages, this text defaults to a black color. But sometimes
  you will want to c...'
---

Le texte joue un rôle significatif sur nos pages web. Cela est dû au fait qu'il aide les utilisateurs à comprendre de quoi traite la page web et ce qu'ils peuvent y faire.

Lorsque vous ajoutez du texte à vos pages web, ce texte est par défaut de couleur noire. Mais parfois, vous voudrez changer la couleur du texte pour le personnaliser davantage.

Par exemple, supposons que vous avez une couleur plus foncée comme arrière-plan de votre site web. Dans ce cas, vous voudrez rendre la couleur du texte plus claire et plus brillante pour améliorer la lisibilité et l'accessibilité de votre site web.

Dans cet article, vous apprendrez comment changer la couleur de votre texte en HTML. Nous examinerons diverses méthodes et nous discuterons de la meilleure méthode.

## Comment changer la couleur du texte avant HTML5

Avant l'introduction de HTML5, vous utilisiez `<font>` pour ajouter du texte aux sites web. Cette balise prend l'attribut `color`, qui accepte la couleur sous forme de nom ou de valeur de code hexadécimal :

```html
<font color="#9900FF"> Bienvenue chez freeCodeCamp. </font>

// Ou

<font color="green"> Bienvenue chez freeCodeCamp. </font>
```

Cette balise a été dépréciée lors de l'introduction de HTML5. Cela a du sens car HTML est un langage de balisage, pas un langage de style. Lorsqu'il s'agit de tout type de style, il est préférable d'utiliser CSS, dont la fonction principale est le style.

Cela signifie que pour ajouter de la couleur à vos pages web, vous devez utiliser CSS.

Au cas où vous seriez pressé de voir comment vous pouvez changer la couleur de votre texte, alors le voici :

```html
// Utilisation de CSS en ligne
<h1 style="color: value;"> Bienvenue chez freeCodeCamp! </h1>

// Utilisation de CSS interne/externe
selector {
    color: value;
}
```

Supposons que vous n'êtes pas pressé. Plongeons-nous brièvement dans le sujet.

## Comment changer la couleur du texte en HTML

Vous pouvez utiliser la propriété CSS `color` pour changer la couleur du texte. Cette propriété accepte des valeurs de couleur comme les codes Hex, RGB, HSL ou les noms de couleur.

Par exemple, si vous voulez changer la couleur du texte en bleu ciel, vous pouvez utiliser le nom `skyblue`, le code hexadécimal `#87CEEB`, le code décimal RGB `rgb(135,206,235)`, ou la valeur HSL `hsl(197, 71%, 73%)`.

Il existe trois façons de changer la couleur de votre texte avec CSS. Il s'agit de l'utilisation de styles en ligne, internes ou externes.

### Comment changer la couleur du texte en HTML avec CSS en ligne

Le CSS en ligne vous permet d'appliquer des styles directement à vos éléments HTML. Cela signifie que vous mettez du CSS directement dans une balise HTML.

Vous pouvez utiliser l'attribut `style`, qui contient tous les styles que vous souhaitez appliquer à cette balise.

```html
<p style="...">Bienvenue chez freeCodeCamp!</p>
```

Vous utiliserez la propriété CSS `color` avec la valeur de couleur de votre choix :

```html
// Valeur du nom de couleur
<p style="color: skyblue">Bienvenue chez freeCodeCamp!</p>

// Valeur Hex
<p style="color: #87CEEB">Bienvenue chez freeCodeCamp!</p>

// Valeur RGB
<p style="color: rgb(135,206,235)">Bienvenue chez freeCodeCamp!</p>

// Valeur HSL
<p style="color: hsl(197, 71%, 73%)">Bienvenue chez freeCodeCamp!</p>
```

Mais le style en ligne n'est pas la meilleure option si vos applications deviennent plus grandes et plus complexes. Alors, voyons ce que vous pouvez faire à la place.

### Comment changer la couleur du texte en HTML avec CSS interne ou externe

Une autre méthode préférée pour changer la couleur de votre texte est d'utiliser soit le style interne soit le style externe. Ces deux méthodes sont assez similaires puisque toutes deux utilisent un sélecteur.

Pour le style interne, vous le faites dans la balise `<head>` de votre fichier HTML. Dans la balise `<head>`, vous ajouterez la balise `<style>` et placerez tous vos styles CSS là, comme vu ci-dessous :

```html
<!DOCTYPE html>
<html>
  <head>
    <style>
      selector {
        color: value;
      }
    </style>
  </head>

  // ...

</html>
```

Alors que pour le style externe, tout ce que vous avez à faire est d'ajouter le style CSS à votre fichier CSS en utilisant la syntaxe générale :

```css
selector {
  color: value;
}
```

Le sélecteur peut être soit votre balise HTML, soit une `class` ou un `ID`. Par exemple :

```html
// HTML
<p> Bienvenue chez freeCodeCamp! </p>

// CSS
p {
  color: skyblue;
}
```

Ou vous pourriez utiliser une `class` :

```html
// HTML
<p class="my-paragraph"> Bienvenue chez freeCodeCamp! </p>

// CSS
.my-paragraph {
   color: skyblue;
}
```

Ou vous pourriez utiliser un `id` :

```html
// HTML
<p id="my-paragraph"> Bienvenue chez freeCodeCamp! </p>

// CSS
#my-paragraph {
   color: skyblue;
}
```

**Note :** Comme vous l'avez vu précédemment, avec le CSS en ligne, vous pouvez utiliser le nom de couleur, le code Hex, la valeur RGB et la valeur HSL avec le style interne ou externe.

## Conclusion

Dans cet article, vous avez appris comment changer la couleur de la police/du texte d'un élément HTML en utilisant CSS. Vous avez également appris comment les développeurs le faisaient avant l'introduction de HTML5 avec la balise `<font>` et les attributs de couleur.

Gardez également à l'esprit que le style de vos éléments HTML avec des styles internes ou externes est toujours préférable au style en ligne. Cela est dû au fait que cela offre plus de flexibilité.

Par exemple, au lieu d'ajouter des styles en ligne similaires à tous vos éléments de balise `<p>`, vous pouvez utiliser une seule `class` CSS pour tous.

Les styles en ligne ne sont pas considérés comme des meilleures pratiques car ils entraînent beaucoup de répétition - vous ne pouvez pas réutiliser les styles ailleurs. Pour en savoir plus, vous pouvez lire [mon article sur le style en ligne en HTML](https://www.freecodecamp.org/news/inline-style-in-html/). Vous pouvez également apprendre comment changer la [taille du texte](https://www.freecodecamp.org/news/how-to-change-text-size-in-html/) dans cet article et la [couleur de fond](https://www.freecodecamp.org/news/html-background-color-change-bg-color-tutorial/) dans cet article.

J'espère que ce tutoriel vous donne les connaissances pour changer la couleur de votre texte HTML afin de le rendre plus beau.

Amusez-vous bien à coder !

Embarquez pour un voyage d'apprentissage ! [Parcourez plus de 200 articles d'experts sur le développement web](https://joelolawanle.com/contents). Consultez [mon blog](https://joelolawanle.com/posts) pour plus de contenu captivant de ma part.