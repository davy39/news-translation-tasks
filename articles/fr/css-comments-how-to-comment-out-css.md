---
title: Commentaires CSS – Comment commenter en CSS
subtitle: ''
author: Kolade Chris
co_authors: []
series: null
date: '2022-06-02T14:49:40.000Z'
originalURL: https://freecodecamp.org/news/css-comments-how-to-comment-out-css
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/CSSComment.png
tags:
- name: best practices
  slug: best-practices
- name: CSS
  slug: css
seo_title: Commentaires CSS – Comment commenter en CSS
seo_desc: 'Commenting is an integral part of any programming language, and CSS is
  no exception.

  If you have a very large project or you work in a team, then you''ll need to help
  others understand your CSS stylesheet better by adding comments to it.

  Since stylesh...'
---

Commenter est une partie intégrante de tout langage de programmation, et CSS ne fait pas exception.

Si vous avez un très grand projet ou si vous travaillez en équipe, vous devrez aider les autres à mieux comprendre votre feuille de style CSS en y ajoutant des commentaires.

Puisque les feuilles de style peuvent devenir compliquées et verbeuses avec le temps, ajouter des commentaires à votre code CSS est une convention utile que vous devriez suivre.

Cet article vous montrera comment ajouter des commentaires en ligne et multilingues en CSS.

## Comment commenter en CSS

Une barre oblique (`/`) et un astérisque (`*`) sont tout ce dont vous avez besoin pour commenter une ligne ou des lignes de CSS. Mais comment faire ?

Pour ajouter des commentaires en ligne et multilingues en CSS, vous commencez par une barre oblique et un astérisque (`/*`), et vous terminez le commentaire par un astérisque et une barre oblique (`*/`).

Voici à quoi ressemble un commentaire en ligne en CSS :
```css
/* Ceci est un commentaire en ligne en CSS */
```

Voici à quoi ressemble un commentaire multilingue :
```css
/* 
Ceci 
est
un 
commentaire
multilingue
en 
CSS
*/
```

Vous pouvez commenter une ligne ou des lignes de CSS que vous ne voulez pas exécuter :
```css
/* .email-sub {
  padding: 0.2rem;
  border: 1px solid var(--primary-color);
  border-radius: 4px;
}

.email-sub:focus {
  border: 1px solid var(--secondary-color);
  outline: none;
} */
```

Vous pouvez spécifier le début et la fin des styles pour une section de votre page web avec des commentaires :
```css
/* Section héroïque commence */
.hero {
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 1.9rem;
  max-width: 1100px;
  margin: 2rem auto -6rem;
}
/* Section héroïque se termine */
```
Vous pouvez également utiliser des commentaires pour ajouter des notes à votre CSS :
```css
/* 
Ne pas remplacer ce style si vous ne savez pas ce que vous faites. Sinon, CSS pourrait vous donner un coup de pied dans les fesses
*/
```

## Conclusion

À long terme, ajouter des commentaires à votre CSS peut vous aider à vous souvenir de ce que vous faisiez lorsque vous avez écrit le code.

De plus, lorsque vous ajoutez des commentaires de la bonne manière, cela facilite le début du travail sur un projet si cela fait longtemps que vous n'avez pas regardé le code.

Pour voir comment vous pouvez organiser votre CSS avec des commentaires, vous devriez lire [cet article](https://www.freecodecamp.org/news/comments-in-css/).