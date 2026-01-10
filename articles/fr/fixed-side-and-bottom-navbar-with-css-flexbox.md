---
title: Tutoriel CSS Flexbox – Comment créer une barre latérale et une barre de navigation
  inférieure fixes
subtitle: ''
author: Spruce Emmanuel
co_authors: []
series: null
date: '2021-09-28T21:41:48.000Z'
originalURL: https://freecodecamp.org/news/fixed-side-and-bottom-navbar-with-css-flexbox
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/halacious-weRQAu9TA-A-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: flexbox
  slug: flexbox
seo_title: Tutoriel CSS Flexbox – Comment créer une barre latérale et une barre de
  navigation inférieure fixes
seo_desc: 'Flexbox can help you simplify the process of creating both basic and advanced
  layouts. And it''s pretty straightforward to create side and bottom navigation menus
  with CSS flexbox or Grid.

  These layouts are so popular that they appear almost everywher...'
---

Flexbox peut vous aider à simplifier le processus de création de mises en page à la fois basiques et avancées. Et il est assez simple de créer des menus de navigation latéraux et inférieurs avec CSS `flexbox` ou `Grid`.

Ces mises en page sont si populaires qu'elles apparaissent presque partout sur le web. Par exemple, consultez la barre latérale de Twitter, qui a inspiré cet article :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/Web-capture_25-9-2021_181148_twitter.com-1.jpeg align="left")

Normalement, pour créer un menu fixe avec CSS, vous devriez utiliser la propriété `position` avec une valeur soit `fixed` soit `sticky`.

Le problème avec cette approche est qu'elle sort l'élément entier du flux du document comme s'il n'avait jamais été là. C'est l'un de ces moments frustrants en CSS pour les débutants et parfois même pour les experts.

Dans ce tutoriel, vous apprendrez à créer une barre latérale fixe et un menu de navigation inférieur fixe avec CSS `flexbox` à la place. Je vais héberger tout le code et les démonstrations sur Codepen afin que vous puissiez voir un aperçu en direct de ce que nous allons construire.

## Installation

Pour créer un élément fixe avec Flexbox, vous devez d'abord désactiver le défilement sur l'élément parent de l'élément que vous souhaitez rendre fixe. Dans notre cas, l'élément parent est le `body` :

```css
body {
    overflow: hidden;
    height: 100vh;
}
```

## Le Balisage

Nous allons utiliser HTML pour créer une mise en page à deux colonnes enveloppée dans une `div` appelée `wrapper`.

```html
<body>
<div class="wrapper">
  <aside>
    <ul>
      <li>Item</li>
      ...
    </ul>
  </aside>
  <main>
    <div class="wrapper_inner">
      <p>
        ...  
       </p>
     </div>
   </main>
 </div>
</body>
```

## Le CSS

Pour rendre la barre latérale fixe, nous devons simplement désactiver le défilement sur le parent `body` et rendre l'élément `main` défilable.

```css
body {
  overflow: hidden;
  height: 100vh;
}
main {
  overflow-y: auto;
}
aside {
  flex: 1 0 10%;
}
.wrapper {
  display: flex;
  height: 100%;
}
```

Décomposons un peu ce code.

Tout d'abord, nous avons rendu le `body` non défilable et avons caché les barres de défilement avec ce code :

```css
body {
    overflow: hidden;
}
```

Ensuite, en utilisant `overflow: auto`, nous avons ajouté les barres de défilement à l'élément `main`.

Et enfin, nous avons créé un conteneur flex `wrapper` et lui avons donné une hauteur égale au parent en utilisant `height: 100%` :

```css
.wrapper {
    display: flex;
    height: 100%;
}
```

## Comment le rendre compatible mobile

Mais sur un écran mobile avec une largeur inférieure à `500px`, nous voudrons que la barre latérale soit fixe en bas ou en haut selon le cas. Pour cela, vous ajouterez le CSS suivant :

```css
@media (max-width: 500px) {
  .wrapper {
    flex-direction: column-reverse;
  }
  ul {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }
  
}
```

Ici, sur un écran mobile, nous changeons la direction de notre conteneur flex en colonne au lieu de ligne. Ensuite, pour le fixer en bas, nous ajoutons ce qui suit :

```css
.wrapper {
    flex-direction: column-reverse;
}
```

Pour le fixer en haut, en revanche, vous devez simplement supprimer le `column-reverse` et le changer en `column` comme suit :

```css
.wrapper {
    flex-direction: column;
}
```

Vous pouvez voir un aperçu en direct dans le pen créé avec Codepen ci-dessous. Vous pouvez redimensionner la fenêtre pour voir la barre de navigation inférieure fixe :

%[https://codepen.io/Spruce_khalifa/pen/XWgxabX] 

## Conclusion

Dans ce tutoriel, vous avez appris à créer une barre latérale fixe responsive avec `flexbox`. Voici quelques étapes importantes à retenir :

1. Pour rendre un élément fixe avec flexbox, vous devez désactiver le défilement sur l'élément parent avec `overflow: hidden`
    
2. Ensuite, vous devez créer un conteneur flex avec une hauteur égale au parent
    
3. Ajoutez `overflow: auto` à l'élément que vous ne voulez pas fixe
    

Et c'est tout !

Si vous avez trouvé ce tutoriel utile ou si vous avez des questions, n'hésitez pas à me contacter sur Twitter (n'oubliez pas de cliquer sur le bouton suivre) [@sprucekhalifa](https://twitter.com/iamspruce.dev/).

Oh et bon codage !