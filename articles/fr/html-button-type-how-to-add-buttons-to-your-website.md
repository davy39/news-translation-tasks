---
title: Type de Bouton HTML – Comment Ajouter des Boutons à votre Site Web
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2021-09-24T18:06:24.000Z'
originalURL: https://freecodecamp.org/news/html-button-type-how-to-add-buttons-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/button.png
tags:
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Type de Bouton HTML – Comment Ajouter des Boutons à votre Site Web
seo_desc: 'Buttons are an essential part of websites. You need them for various functionalities,
  from submitting information and getting access to more content to linking to different
  parts of the web page and other websites.

  HTML gives you several ways to add ...'
---

Les boutons sont une partie essentielle des sites web. Vous en avez besoin pour diverses fonctionnalités, de la soumission d'informations et de l'accès à plus de contenu à la liaison avec différentes parties de la page web et d'autres sites web.

HTML vous offre plusieurs façons d'ajouter des boutons à votre site web – avec la balise button, le lien d'ancrage et les types d'input `button` et `submit`.

Dans cet article, je vais vous guider à travers 4 de ces méthodes, afin que vous puissiez commencer à ajouter des boutons à vos sites web en toute confiance.

## Comment Ajouter des Boutons à votre Site Web avec la Balise Button

La balise button est l'une des façons les plus simples d'ajouter des boutons à vos sites web. Pour l'utiliser, il vous suffit de placer le texte que vous voulez voir sur le bouton entre les balises d'ouverture et de fermeture, comme ceci :

```html
<button>Bouton Exemple</button>
```

![ss-1](https://www.freecodecamp.org/news/content/images/2021/09/ss-1.png)

J'ai placé le bouton au centre horizontalement et verticalement en utilisant flexbox, les marges et les propriétés de hauteur :

```css
body {
        background-color: #8d8d8d;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 0 auto;
        height: 100vh;
      }
```

Tout sur la page sera centré avec ce CSS au fur et à mesure que nous avancons.

Pour rendre ce type de bouton actif, vous devez ajouter un peu de JavaScript. Dans l'extrait de code ci-dessous, avec un peu de JavaScript en ligne, je fais en sorte que le bouton affiche une boîte d'alerte dans le navigateur chaque fois qu'il est cliqué :

```html
<button onclick="alert('Hello Campers')">Bouton Exemple</button>
```

![ss-2](https://www.freecodecamp.org/news/content/images/2021/09/ss-2.png)

## Comment Ajouter des Boutons à vos Sites Web avec une Balise d'Ancre

Vous pouvez également ajouter des boutons à vos sites web avec la balise d'ancrage. La balise d'ancrage est principalement utilisée pour ajouter des liens à vos sites web, mais vous pouvez la styliser avec CSS pour qu'elle ressemble à un bouton réel.

L'avantage de cette approche est que vous pouvez lier à une page sans aucun JavaScript.

Dans l'exemple ci-dessous, je crée un bouton avec la balise d'ancrage et je le lie au site officiel de freeCodeCamp :

```html
<a href="https://freecodecamp.org">Apprendre à Coder Gratuitement</a>
```

Cela ressemble à un lien dans le navigateur :
![ss-3](https://www.freecodecamp.org/news/content/images/2021/09/ss-3.png)

Vous pouvez le faire ressembler à un bouton avec un peu de CSS en supprimant le soulignement par défaut et la couleur du texte, en définissant une couleur de fond et une couleur de premier plan avec les propriétés de couleur, et en ajoutant un remplissage et un rayon de bordure :

```css
 a {
        text-decoration: none;
        border: 0.2px solid #000;
        color: #000;
        background: #e6e4e4;
        padding: 5px;
        border-radius: 1px;
      }
```

Tout ce que j'ai fait dans le CSS, c'est essayer d'imiter l'apparence par défaut donnée aux boutons en HTML.

La balise d'ancrage ressemble maintenant à ceci :
![ss-4](https://www.freecodecamp.org/news/content/images/2021/09/ss-4.png)

## Comment Ajouter des Boutons à vos Sites Web avec le Type d'Input `Button`

Vous pouvez également ajouter des boutons à votre site web avec le type d'input button. Il se comporte exactement comme la balise button.

La balise input est un élément vide, ce qui signifie qu'elle n'a pas de balise de fermeture. Alors, comment affichez-vous du texte dans le bouton ? Vous le faites avec l'attribut value !

```html
<input type="button" value="Bouton Exemple" />
```

![ss-5](https://www.freecodecamp.org/news/content/images/2021/09/ss-5.png)

## Comment Ajouter des Boutons à vos Sites Web avec le Type d'Input `Submit`

Vous utilisez généralement le type d'input submit à l'intérieur d'un élément de formulaire afin que les données remplies par l'utilisateur soient soumises lorsque le bouton est cliqué.

Tout comme le type d'input button, c'est un élément vide, donc vous avez besoin d'un attribut value pour communiquer à l'utilisateur de quoi il s'agit.

```html
<input type="submit" value="Un Autre Bouton" />
```

![ss-6](https://www.freecodecamp.org/news/content/images/2021/09/ss-6.png)

La différence entre le type d'input button et le type d'input submit est que lorsque vous utilisez le type de bouton submit dans un formulaire, les données sont soumises sans aucune manipulation avec JavaScript.

Mais le type d'input button, en revanche, nécessite une manipulation avec JavaScript pour fonctionner. Donc, lorsque vous utilisez un type d'input button à l'intérieur d'un élément de formulaire, les données ne sont pas soumises automatiquement lorsqu'il est cliqué.

## Mini Projet : Comment Créer un Bouton Lumière Néon avec HTML et CSS

Le bouton lumière néon est une tendance de design qui fait des vagues parce qu'il est magnifique. Avec ce que vous avez appris dans cet article, vous pouvez en créer un avec une balise button et un peu de CSS.

Tout d'abord, vous devez changer les styles par défaut du bouton :

```html
<button>Lumière Néon</button>
```

```css
  button {
        background-color: #000;
        border: .5px solid crimson;
        border-radius: 10px;
        color: #fff;
        padding: 8px;
      }
```

Jusqu'à présent, le bouton ressemble à ceci :
![neon](https://www.freecodecamp.org/news/content/images/2021/09/neon.png)

Pour implémenter l'effet de lumière néon, vous pouvez utiliser la propriété `box-shadow`. Elle permet plusieurs valeurs, ce qui sera instrumental pour créer l'effet de lumière néon.

```css
button {
        background-color: #000;
        border: .5px solid crimson;
        border-radius: 10px;
        color: #fff;
        padding: 8px;
        box-shadow: 0 0 30px 0 crimson,
                    0 0 30px 0 crimson,
                    0 0 10px 0 crimson inset;
      }
```

Dans la propriété `box-shadow` :

- la première valeur représente le décalage sur l'axe x
- la deuxième valeur représente le décalage sur l'axe y
- la troisième valeur représente le rayon de flou
- la quatrième valeur représente le rayon de propagation
- la cinquième valeur est la couleur à appliquer à l'ombre

Je ne voulais que le rayon de propagation et la couleur, donc j'ai mis les autres valeurs à zéro. Ensuite, j'ai fait en sorte que la dernière des valeurs de box-shadow s'applique à l'intérieur du bouton en y attachant `inset`.

Il y a maintenant un effet de lumière néon sur le bouton :

![neon-light](https://www.freecodecamp.org/news/content/images/2021/09/neon-light.png)

## Conclusion

Cet article vous a montré plusieurs façons d'ajouter des boutons à un site web.
En HTML et CSS, il y a toujours plusieurs façons de faire la même chose – c'est l'une des raisons pour lesquelles vous pouvez ajouter des boutons à un site web même avec une balise d'ancrage.

Vous pouvez même faire en sorte qu'un bouton se comporte comme un lien en enveloppant une balise d'ancrage autour d'un bouton.

Vous pouvez également ajouter des boutons avec presque n'importe quelle autre balise, comme div, span, et même la balise p. Mais vous devriez éviter de le faire pour des raisons d'accessibilité et pour ne pas nuire au référencement de votre site web. Après tout, vous devez aussi faciliter la vie des robots d'indexation.

Merci d'avoir lu, et continuez à coder.