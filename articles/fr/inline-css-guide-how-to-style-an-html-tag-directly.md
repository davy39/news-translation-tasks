---
title: "Guide du CSS en ligne \x13 Comment styliser une balise HTML directement"
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-09T19:43:17.000Z'
originalURL: https://freecodecamp.org/news/inline-css-guide-how-to-style-an-html-tag-directly
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9c38740569d1a4ca30c1.jpg
tags:
- name: CSS
  slug: css
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: General Programming
  slug: programming
- name: Style Guide
  slug: style-guide
seo_title: "Guide du CSS en ligne \x13 Comment styliser une balise HTML directement"
seo_desc: 'By Amy Haddad

  You’ve written some HTML and now need to style it with CSS. One way is to use inline
  styles, which is what this article is about.

  <p style="color: red; font-size: 20px;">This is my first paragraph.</p>


  Before we jump into the nuances o...'
---

Par Amy Haddad

Vous avez écrit du HTML et vous devez maintenant le styliser avec du CSS. Une façon de le faire est d'utiliser des styles en ligne, ce qui est le sujet de cet article.

```html
<p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
```

Avant de plonger dans les nuances des styles en lignequand, pourquoi et comment les utiliseril est important de connaître les autres façons de styliser votre HTML. Ainsi, vous pourrez choisir la meilleure option pour votre code.

Voici un résumé de vos options.

### Feuille de style externe

Les développeurs stockent généralement tout leur CSS dans une feuille de style externe. Dans votre fichier HTML, utilisez l'élément **`<link>`** pour lier à votre feuille de style externe, qui contient votre CSS.

```html
<head>
    <link rel="stylesheet" href="./index.css">
</head>
```

À l'intérieur du fichier, index.css, nous avons nos règles CSS.

```css
p {
    color: red;
    font-size: 20px;
}
```

### Feuille de style interne

Une autre option pour styliser le CSS est d'utiliser une feuille de style interne. Cela signifie définir vos règles CSS à l'intérieur de l'élément **`<style>`** dans votre fichier HTML.

```html
<head>  
   <style>
       p {
           color: red;
           font-size: 20px;
       }
   </style>
 </head>
```

### Styles en ligne

Moins fréquemment, vous vous retrouverez à utiliser des styles en ligne. Mais ils sont toujours importants à connaître car il y a certaines occasions où ils sont pratiques.

Avec les styles en ligne, vous ajoutez l'attribut style à une balise HTML suivi de votre CSS pour styliser un élément.

```html
<p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
<p>Ceci est mon deuxième paragraphe.</p>
```

Dans notre cas, le texte du premier paragraphe est rouge avec une taille de police de 20px. Le deuxième, cependant, reste inchangé.

Examinons de plus près comment et quand utiliser les styles en ligne. Nous découvrirons également pourquoi un seul de nos paragraphes est stylisé.

# Qu'est-ce qu'une balise HTML ?

Avec les styles en ligne, vous appliquez du CSS à l'attribut `style` dans la balise HTML d'ouverture.

Exemples de balises HTML incluent :

* <body>...</body>
* <h1>...</h1>
* <p>...</p>

Les balises d'ouverture et de fermeture font souvent partie de l'[élément](https://developer.mozilla.org/en-US/docs/Glossary/element) HTML, qui peut contenir du texte, des données, une image, ou rien du tout.

Ici, nous avons un élément de texte.

```html
<p>Ceci est mon premier paragraphe.</p>
```

Nous pouvons utiliser des styles en ligne pour styliser cet élément en ajoutant l'attribut style à la balise d'ouverture, suivi de paires propriété-valeur CSS.


```html
<body>
   <p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
   <p>Ceci est mon deuxième paragraphe.</p>
</body>
```

Passons en revue comment nous avons utilisé les styles en ligne.

# Comment utiliser les styles en ligne

Ajoutez l'attribut style à la balise que vous souhaitez styliser, suivi d'un signe égal. Commencez et terminez votre CSS avec des guillemets doubles.

```html
<p style="....">
```

Ajoutez des paires propriété-valeur à l'attribut style. Ajoutez un point-virgule après chaque paire propriété-valeur.

```css
color: red; font-size: 20px;
```

Ainsi, lorsque nous mettons tout ensemble, cela ressemble à ceci :

```html
<p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
```

## Points clés à connaître

Contrairement aux feuilles de style internes et externes, les styles en ligne ne contiennent pas d'accolades ni de sauts de ligne. C'est-à-dire, écrivez votre CSS tout sur la même ligne lorsque vous utilisez des styles en ligne.

De plus, gardez à l'esprit que les styles en ligne n'affectent _que_ l'élément spécifique auquel vous ajoutez l'attribut style avec les paires propriété-valeur CSS.

Par exemple, dans le code ci-dessous, _seul_ le premier paragraphe est stylisé en rouge avec une taille de police de 20px.

```html
<body>
   <p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
   <p>Ceci est mon deuxième paragraphe.</p>
</body>
```

Si nous voulons styliser le texte des _deux_ paragraphes avec des styles en ligne, alors nous devons ajouter du CSS à l'attribut style du deuxième `<p>` également.

```html
<body>
  <p style="color: red; font-size: 20px;">Ceci est mon premier paragraphe.</p>
  <p style="color: red; font-size: 20px;">Ceci est mon deuxième paragraphe.</p>
</body>
```

Cependant, si nous utilisions une feuille de style externe, par exemple, nous pourrions facilement styliser les _deux_ paragraphes sans dupliquer notre code en utilisant un seul sélecteur CSS.

```css
p {
    color: red;
    font-size: 20px;
}
```

Cela nous amène à un sujet important : quand utiliser et quand ne pas utiliser les styles en ligne.

# Quand utiliser (et quand NE PAS utiliser) les styles en ligne

Disons que vous avez un fichier HTML avec dix balises de paragraphe ou plus. Pouvez-vous imaginer styliser chacune individuellement avec des styles en ligne ?

Faire cela encombrera rapidement votre code, le rendant difficile à lire et à maintenir.

De plus, les styles en ligne peuvent introduire des problèmes de spécificité si vous utilisez également des feuilles de style internes ou externes.

C'est parce que les styles en ligne ont une [spécificité élevée](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance#Understanding_the_cascade). Cela signifie qu'ils remplaceront la plupart des autres règles dans les feuilles de style internes et externes, sauf pour la déclaration `!important`.

Par exemple, nous avons ajouté des styles en ligne à deux éléments de paragraphe. Nous avons également ajouté une feuille de style interne.

```html
<html>
  <head>
      <title>Ma Nouvelle Page Web</title>
      <style>
       p {
           color: pink;
       }
   </style>
  </head>
 
<body>
   <p style="color: blue;">Un paragraphe bleu.</p>
   <p style="color: blue;">Un autre paragraphe bleu.</p>
</body>
</html>
```

Le CSS de nos styles en ligne remplace le CSS dans la feuille de style interne. Nous obtenons donc deux paragraphes bleus.

Les feuilles de style externes sont également beaucoup plus faciles à maintenir lorsque vous ou quelqu'un d'autre devez apporter une modification. Cela est dû au fait qu'un style d'une feuille de style externe ou interne peut s'appliquer à plusieurs éléments, tandis qu'un style en ligne doit être appliqué à chaque élément individuellement.

Par exemple, disons que vous devez mettre à jour un style pour dix éléments. Il est plus facile d'apporter la modification une fois dans une feuille de style externe, plutôt que dix fois différentes dans votre fichier HTML.

En général, il est souvent préférable de mettre votre CSS dans un fichier séparé. Ainsi, votre fichier HTML contient la structure et le contenu de votre site web, et votre fichier CSS contient vos styles. Cela rend votre code plus facile à lire et à gérer.

Cependant, il y a des moments où il peut être judicieux d'utiliser des styles en ligne :

* Ajoutez un style et voyez le changement rapidement, ce qui peut être utile pour les [tests](https://developer.mozilla.org/en-US/docs/Web/HTML/Global_attributes/style).
* Utilisez l'attribut style en JavaScript pour appliquer un style.

La plupart du temps, vous voudrez utiliser des feuilles de style externes. Mais vous vous retrouverez occasionnellement à utiliser des styles en ligne, le plus souvent dans les situations ci-dessus.

_Je parle de l'apprentissage de la programmation et des meilleures façons de s'y prendre sur mon blog à [amymhaddad.com](https://amymhaddad.com/)._