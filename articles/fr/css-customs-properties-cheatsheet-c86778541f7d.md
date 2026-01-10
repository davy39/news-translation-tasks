---
title: Un aide-mémoire pour vous aider à retenir les propriétés personnalisées CSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-20T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/css-customs-properties-cheatsheet-c86778541f7d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OkasBr8SDeRPWhLGIGlqnw.png
tags:
- name: CSS
  slug: css
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Un aide-mémoire pour vous aider à retenir les propriétés personnalisées
  CSS
seo_desc: 'By Vincent Humeau

  CSS custom properties, also known as CSS variables, represent custom properties
  that can be declared and be called in your CSS.

  Declare a custom property in CSS

  To declare a Custom property in your CSS, you need to use the -- syntax...'
---

Par Vincent Humeau

Les propriétés personnalisées CSS, également connues sous le nom de variables CSS, représentent des propriétés personnalisées qui peuvent être déclarées et appelées dans votre CSS.

### Déclarer une propriété personnalisée en CSS

Pour déclarer une propriété personnalisée dans votre CSS, vous devez utiliser la syntaxe `--` :

```css
:root { --colorPrimary: hsla(360, 100%, 74%, 0.6); }
```

Remarquez le sélecteur de pseudo-classe `:root` — nous pouvons déclarer nos variables globalement en l'utilisant. Nous pouvons également les déclarer en utilisant d'autres sélecteurs, et elles seront alors limitées à ces derniers.

```css
.theme-dark { --colorPrimary: hsla(360, 100%, 24%, 0.6); }
```

### Utiliser une propriété personnalisée en CSS

Pour utiliser une propriété personnalisée CSS dans votre CSS, vous pouvez utiliser la fonction `var()` :

```css
:root { --colorPrimary: tomato; } 
.theme-dark { --colorPrimary: lime; } body { background-color: var(--colorPrimary); }
```

Dans ce cas, `body` aura une couleur de fond `tomato`, mais un `body.theme-dark` de `lime`.

### Utiliser des propriétés personnalisées sans unités

Les propriétés personnalisées CSS peuvent être déclarées sans unités si elles sont utilisées avec la fonction `calc()`.

```css
:root { --spacing: 2; } 
.container { 
  padding: var(--spacing) px; /*Ne fonctionne pas ?*/ 
  padding: calc(var(--spacing) * 1rem); /*Donnera 2rem ?*/ 
}
```

## Utiliser des propriétés personnalisées avec JavaScript

Pour obtenir une propriété personnalisée, nous pouvons utiliser ce qui suit :

```js
getComputedStyle(element).getPropertyValue("--my-var"); 
// Ou si en ligne 
element.style.getPropertyValue("--my-var");
```

Pour mettre à jour la valeur de la propriété personnalisée :

```
element.style.setProperty("--my-var", newVal);
```

Exemple d'obtention et de remplacement de valeurs :

Dans l'exemple suivant, nous utilisons la [bibliothèque de contrôleurs dat.gui](https://workshop.chromeexperiments.com/examples/gui/) pour changer la valeur des propriétés personnalisées --scenePerspective, --cubeRotateY et --cubeRotateX. Cette méthode facilite l'application d'un nouveau style, car vous n'avez pas à appliquer de style en ligne sur chaque élément du DOM.

Merci d'avoir lu !

### Ressources

[Définir des propriétés personnalisées : la famille de propriétés --*](https://drafts.csswg.org/css-variables/#defining-variables)

[Propriétés personnalisées : variables CSS — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/--*)

[var() — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/var)

[Utiliser les propriétés personnalisées CSS (variables) — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Using_CSS_variables)

Vous pouvez lire plus de mes articles [sur mon blog](https://vinceumo.github.io/devNotes/css/2019/02/20/css-customs-properties.html).