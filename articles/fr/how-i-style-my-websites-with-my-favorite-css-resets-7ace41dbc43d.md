---
title: Comment je style mes sites web avec mes CSS resets préférés
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-03-25T18:05:27.000Z'
originalURL: https://freecodecamp.org/news/how-i-style-my-websites-with-my-favorite-css-resets-7ace41dbc43d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cHZLhJhJgiRK48Dzhem5-w.jpeg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment je style mes sites web avec mes CSS resets préférés
seo_desc: 'Many frontend developers begin styling their websites with Normalize. Some
  developers have personal preferences that they add on to Normalize.css. I have my
  preferences, too.

  In this article, I want to share these preferences with you, my personal CS...'
---

De nombreux développeurs frontend commencent à styliser leurs sites web avec Normalize. Certains développeurs ont des préférences personnelles qu'ils ajoutent à Normalize.css. J'ai aussi mes préférences.

Dans cet article, je souhaite partager ces préférences avec vous, mon reset CSS personnel (que j'utilise en plus de Normalize.css).

Je catégorise les resets en 8 catégories :

1. Dimensionnement de la boîte

2. Suppression des marges et des paddings

3. Listes

4. Formulaires et boutons

5. Images et intégrations

6. Tableaux

7. L'attribut hidden

8. Noscript

# Dimensionnement de la boîte

La propriété `box-sizing` change la façon dont le modèle de boîte CSS fonctionne. Elle change la façon dont les propriétés `width`, `height`, `padding`, `border` et `margin` sont calculées.

Le paramètre par défaut pour `box-sizing` est `content-box`. Je préfère le changer en `border-box` car il est plus facile pour moi de styliser `padding` et `width`.

Pour plus d'informations sur le dimensionnement de la boîte, vous pourriez être intéressé par « [Comprendre le dimensionnement de la boîte](https://zellwk.com/blog/understanding-css-box-sizing/) ».

```css
html {
  box-sizing: border-box;
}
*,
*::before,
*::after {
  box-sizing: inherit;
}
```

# Suppression des marges et des paddings

Les navigateurs définissent différentes marges et paddings pour différents éléments. Ces paramètres par défaut me déroutent lorsque je n'en suis pas conscient. Lorsque je code, je préfère définir toutes les marges et paddings moi-même.

```css
/* Réinitialise les marges et les paddings sur la plupart des éléments */
body,
h1,
h2,
h3,
h4,
h5,
h6,
ul,
ol,
li,
p,
pre,
blockquote,
figure,
hr {
  margin: 0;
  padding: 0;
}
```

# Listes

J'utilise des listes non ordonnées dans de nombreuses situations, et je n'ai pas besoin d'un style `disc` dans la plupart d'entre elles. Ici, je définis `list-style` sur none. Lorsque j'ai besoin du style `disc`, je le rétablis manuellement sur le `<ul>` spécifique.

```css
/* Supprime les disques des ul */
ul {
  list-style: none;
}
```

# Formulaires et boutons

Les navigateurs n'héritent pas de la typographie pour les formulaires et les boutons. Ils définissent `font` sur `400 11px system-ui`. Je trouve cela déconcertant et bizarre. Je dois toujours les faire hériter des éléments ancêtres manuellement.

```css
input,
textarea,
select,
button {
  color: inherit;
  font: inherit;
  letter-spacing: inherit;
}
```

Différents navigateurs ont stylisé les bordures des éléments de formulaire et des boutons différemment. Je n'aime pas ces styles par défaut et préfère les définir sur `1px solid gray`.

```css
button {
  border-radius: 0;
  padding: 0.75em 1em;
  background-color: transparent;
}
```

J'ai apporté quelques ajustements supplémentaires aux boutons :

1. Définir le padding des boutons sur `0.75em` et `1em` car ils semblent être des valeurs par défaut sensées d'après mon expérience.
2. Supprimer le `border-radius` par défaut appliqué aux boutons.
3. Forcer la couleur de fond à être transparente

```css
button {
  border-radius: 0;
  padding: 0.75em 1em;
  background-color: transparent;
}
```

Enfin, je définis `pointer-events: none` pour les éléments à l'intérieur d'un bouton. Cela est principalement utilisé pour les interactions JavaScript.

(Lorsque les utilisateurs cliquent sur quelque chose dans un bouton, `event.target` est la chose sur laquelle ils ont cliqué, et non le bouton. Ce style facilite le travail avec les événements `click` s'il y a des éléments HTML à l'intérieur d'un bouton).

```css
button * {
  pointer-events: none;
}
```

Les éléments multimédias incluent les images, les vidéos, les objets, les iframes et les intégrations. Je tends à laisser ces éléments se conformer à la largeur de leurs conteneurs.

Je définis également ces éléments sur `display: block` car `inline-block` crée un espace blanc indésirable en bas de l'élément.

```css
embed,
iframe,
img,
object,
video {
  display: block;
  max-width: 100%;
}
```

# Tableaux

J'utilise rarement des tableaux, mais ils peuvent être utiles parfois. Voici les styles par défaut avec lesquels je commence :

```css
table {
  table-layout: fixed;
  width: 100%;
}
```

Lorsque un élément a un attribut `hidden`, il doit être masqué à la vue. Normalize.css le fait déjà pour nous.

```css
[hidden] {
  display: none;
}
```

Le problème avec ce style est sa faible spécificité.

J'ajoute souvent `hidden` à d'autres éléments que je style avec une classe. La spécificité d'une classe est plus élevée que celle d'un attribut, et la propriété `display: none` ne fonctionne pas.

C'est pourquoi je choisis d'augmenter la spécificité de `[hidden]` avec `!important`.

```css
[hidden] {
  display: none !important;
}
```

# Noscript

Si un composant nécessite JavaScript pour fonctionner, j'ajoute une balise `<noscript>` pour informer les utilisateurs (s'ils ont désactivé JavaScript).

Cela crée des styles par défaut pour la balise `<noscript>`.

```css
/* styles noscript */
noscript {
  display: block;
  margin-bottom: 1em;
  margin-top: 1em;
}
```

# Conclusion

Chacun commence ses projets différemment. N'hésitez pas à utiliser l'un de ces styles que j'ai mentionnés. Voici un [dépôt Github](https://github.com/zellwk/css-reset) de mes resets CSS personnels.

Avez-vous des recommandations qui pourraient aider à améliorer ce fichier CSS Reset ? Si oui, n'hésitez pas à me contacter et à me le faire savoir !

Merci d'avoir lu. Cet article vous a-t-il aidé ? Si c'est le cas, j'espère que vous envisagerez de [le partager](https://twitter.com/share?text=My%20CSS%20reset%20by%20@zellwk%20%F0%9F%91%87%20&url=https://zellwk.com/blog/css-reset/). Vous pourriez aider quelqu'un d'autre. Merci beaucoup !

---

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/css-reset). Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.