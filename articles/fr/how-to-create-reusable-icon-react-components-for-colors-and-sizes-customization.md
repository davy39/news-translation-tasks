---
title: Comment créer des composants React d'icônes SVG réutilisables
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-26T18:22:02.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-reusable-icon-react-components-for-colors-and-sizes-customization
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-chait-goli-2088233.jpg
tags:
- name: components
  slug: components
- name: Icons
  slug: icons
- name: React
  slug: react
- name: SVG
  slug: svg
seo_title: Comment créer des composants React d'icônes SVG réutilisables
seo_desc: 'By Dillion Megida

  We use icons when building frontend applications all the time – for indications,
  pointers, and so on. Here''s how to create a reusable React component for icons.

  When it comes to icons, you can use PNG or SVG images. PNGs come with a...'
---

Par Dillion Megida

Nous utilisons des icônes lors de la création d'applications frontend tout le temps – pour des indications, des pointeurs, etc. Voici comment créer un composant React réutilisable pour les icônes.

En ce qui concerne les icônes, vous pouvez utiliser des images PNG ou SVG. Les PNG viennent avec une couleur fixe mais permettent des changements de dimension (comme une image régulière). Dans certains cas, cela altère la qualité de l'image.

Les SVG, en revanche, ont une meilleure qualité quelle que soit la taille et les couleurs sont personnalisables même après le téléchargement.

Mais vous serez peut-être d'accord avec moi pour dire que les SVG peuvent être un casse-tête en matière de personnalisation.

Dans cet article, je vais vous montrer comment je procède actuellement pour créer des icônes SVG personnalisables en tant que composants React.

## Comment télécharger les icônes

Je télécharge généralement les icônes que j'utilise depuis [Remixicon](https://remixicon.com/). Je n'ai pas encore essayé d'autres bibliothèques d'icônes, donc les étapes de cet article peuvent ou non s'appliquer si vous utilisez une bibliothèque différente.

Cela dit, j'ai travaillé avec un client dans le passé qui a créé des icônes personnalisées sur Figma. J'ai appliqué la solution partagée dans cette étape, et cela a également fonctionné pour la plupart des icônes. Alors suivez le guide même si vous n'utilisez pas Remixicon :)

Sur Remixicon, je sélectionne une icône de mon choix, je sélectionne la taille **18px**, et je sélectionne **Copier SVG**.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-154.png)

Je laisse la couleur en noir. Si vous choisissez une couleur différente, cela peut entrer en conflit avec les couleurs spécifiées que vous fournissez plus tard. Il est donc préférable de la laisser en noir, qui est la couleur par défaut des SVG.

## Comment créer le composant React

Ensuite, je colle le SVG dans un fichier, par exemple, `home-line.js` avec le code suivant :

```js
import React from 'react'

export default function HomeLine() {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="18" height="18">
      <path fill="none" d="M0 0h24v24H0z"/>
      <path d="M21 20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.49a1 1 0 0 1 .386-.79l8-6.222a1 1 0 0 1 1.228 0l8 6.222a1 1 0 0 1 .386.79V20zm-2-1V9.978l-7-5.444-7 5.444V19h14z"/>
    </svg>
  )
}
```

Tel quel, il utilise la couleur et la taille par défaut qui proviennent de Remixicon. Je vais ajouter deux props pour modifier ce composant : `size` et `color`.

L'élément `svg` a quatre propriétés : `xmlns`, `viewBox`, `width` et `height`. Je vais utiliser la prop `size` pour modifier la valeur de `width` et `height`. Ensuite, je vais ajouter une propriété supplémentaire, `fill`, que je vais utiliser pour la prop `color`.

Voici le composant mis à jour :

```js
import React from 'react'

export default function HomeLine({
  size = 18, // ou toute taille par défaut de votre choix
  color = "black" // ou toute couleur de votre choix
}) {
  return (
    <svg
      xmlns="http://www.w3.org/2000/svg"
      viewBox="0 0 24 24"
      width={size} // ajouté size ici
      height={size} // ajouté size ici
      fill={color} // ajouté color ici
    >
      <path fill="none" d="M0 0h24v24H0z"/>
      <path d="M21 20a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V9.49a1 1 0 0 1 .386-.79l8-6.222a1 1 0 0 1 1.228 0l8 6.222a1 1 0 0 1 .386.79V20zm-2-1V9.978l-7-5.444-7 5.444V19h14z"/>
    </svg>
  )
}
```

Je laisse le `viewBox` tel quel. Et maintenant je peux utiliser le composant comme ceci :

```js
<HomeLine size={100} color="purple" />
<HomeLine size={50} color="red" />
<HomeLine size={30} color="green" />
```

![Image](https://www.freecodecamp.org/news/content/images/2022/04/image-155.png)

Si vous utilisez une icône qui n'est pas de forme carrée, vous devrez spécifiquement fournir les props `width` et `height` pour changer les deux attributs en conséquence.

## Conclusion

Je sais que Remixicon ne possède pas toutes les icônes dont vous pourriez avoir besoin, et lorsque vous travaillez avec un système de design, vous pourriez recevoir certaines icônes personnalisées.

Mais l'idée partagée ici est quelque chose que vous pouvez essayer avec n'importe quelle bibliothèque avec laquelle vous travaillez. Et si vous le faites, j'adorerais entendre votre expérience en essayant cela.

Si vous avez aimé cet article et l'avez trouvé utile, partagez-le :)