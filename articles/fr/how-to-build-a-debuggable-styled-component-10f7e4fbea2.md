---
title: Comment Construire un Composant Stylisé Débogable
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-09-13T14:39:55.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-debuggable-styled-component-10f7e4fbea2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*OArsqiCwxTb78iN27XtVdg.jpeg
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: styled-components
  slug: styled-components
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment Construire un Composant Stylisé Débogable
seo_desc: 'By ChunLin Wu

  Styled-components is a CSS-In-JavaScript library. It allows you to write CSS code
  inside your React JSX files. Life is good when your component’s CSS properties can
  be dynamically changed with styled-components.

  However, there are some ...'
---

Par ChunLin Wu

Styled-components est une bibliothèque CSS-In-JavaScript. Elle permet d'écrire du code CSS directement dans vos fichiers React JSX. La vie est belle lorsque les propriétés CSS de vos composants peuvent être modifiées dynamiquement avec styled-components.

Cependant, il y a quelques inconvénients lorsque vous essayez de déboguer vos composants stylisés. Dans cet article, je vais vous présenter les avantages et les inconvénients de la construction de composants avec le CSS traditionnel et styled-components. Ensuite, je vous montrerai une méthode simple pour surmonter les défauts de la construction d'un composant stylisé. Restez à l'écoute !

### Installation

Tout d'abord, créons un composant avec un fichier CSS conventionnel.

Pour l'instant, le composant ressemble à l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bMJr4IzslE0CGmTvCcT_jg.png)

Plutôt mignon, n'est-ce pas ?

### Rendre le titre "Cute Puppy" d'une autre couleur

Donnons une prop à `Content.jsx`. Pour simplifier, donnons-lui une prop appelée **skyblue**.

Maintenant, nous pouvons changer les propriétés CSS de `Content.jsx` en fonction de `skyblue`. Je veux vous présenter deux méthodes pour ajouter de nouvelles propriétés CSS via le CSS général.

#### **Style Inline**

Comme vous pouvez le voir, nous utilisons `skyblue` comme condition pour ajouter des propriétés CSS à l'objet style. Nous injectons ensuite l'objet style comme un style inline. Maintenant, le résultat ressemblera à ceci...

![Image](https://cdn-media-1.freecodecamp.org/images/1*heUmDWYNGBJjKDM7nc2kAA.png)

La couleur du titre est maintenant bleu ciel ! Passons maintenant à la deuxième méthode.

#### **Ajouter de Nouvelles Classes CSS**

Comme vous le savez, nous avons créé une classe CSS appelée `content--skyblue`. C'est simple pour rendre la couleur bleu ciel. Nous voulons ajouter cette classe au titre "Cute Puppy". Ce que nous faisons, c'est créer un tableau pour stocker les classes CSS, puis utiliser la méthode `join` pour séparer les classes avec un espace. Ainsi, le className serait comme `<div className="content__title content--skyblue">Cute Puppy</div>`. Le résultat sera également le même que la méthode inline-style.

Vous pouvez voir qu'il n'est pas pratique de modifier les styles avec les deux méthodes ci-dessus, surtout pour les composants UI complexes. Vous ne voulez pas écrire beaucoup d'instructions conditionnelles pour styliser vos composants, n'est-ce pas ?

Alors, quels sont les avantages et les inconvénients des méthodes **inline-style** et **ajout de nouvelles classes CSS** ?

#### Avantages

1. C'est du CSS général et du JS vanilla — vous n'avez pas besoin d'apprendre une nouvelle syntaxe et API.
2. Facile à déboguer en utilisant les outils de développement des navigateurs.

#### Inconvénients

1. Il n'est pas flexible de modifier le style inline à cause de la [spécificité CSS](http://muki.tw/wordpress/wp-content/uploads/2015/07/CSS-Specificity-full-710x1024.png). Vous ne pouvez pas simplement ajouter une classe pour remplacer le style inline car le style inline a une spécificité plus élevée.
2. Ce n'est pas clair de voir quelles classes sont incluses dans `className` via la méthode d'ajout de nouvelles classes CSS. Lorsque vous voyez ce genre de code `<div className={titleStyles.join(' ')}>Cute Puppy</div>`, vous devez revenir en arrière pour voir la logique que vous avez ajoutée aux classes. Cela sera un inconvénient majeur lorsque vous avez beaucoup de className à modifier.

C'est pourquoi je veux vous présenter [styled-components](https://www.styled-components.com/).

### Styled-components

> Utilisez les meilleurs éléments de ES6 et CSS pour styliser vos applications sans stress ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*WI_n7M5OYeUh0SrkXZVGyw.png)
_styled-components_

Styled-components est une bibliothèque qui facilite la modification des propriétés CSS. Vous pouvez simplement l'installer via `npm install styled-components --save` ou `yarn add styled-components`. Ensuite, vous pouvez utiliser styled-components pour styliser vos composants. Prenons l'exemple du Cute Puppy.

Tout d'abord, nous devons importer styled-components dans notre composant. Nous l'importons sous le nom `styled`. Ensuite, nous pouvons définir quel élément HTML doit être utilisé pour chaque styled-component. Par exemple,

`const Button = styled.button` /* Propriétés CSS */ ``

signifie que ce composant Button représente le styled-component qui rend un `<button />`. Ensuite, nous pouvons simplement déplacer les propriétés CSS vers chaque styled-component. C'est tout ! Juste aussi simple ! Maintenant, vous pouvez voir la version originale de Cute Puppy.

![Image](https://cdn-media-1.freecodecamp.org/images/1*bMJr4IzslE0CGmTvCcT_jg.png)

Et si nous changions la couleur du titre en utilisant styled-components ? Styled-components tire parti des [littéraux de gabarit](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals) JavaScript ES6. Vous pouvez passer une fonction aux littéraux de gabarit. Cela sera utile lorsque vous voulez modifier les propriétés CSS en fonction des props. Plongeons plus profondément dans le sujet via Cute Puppy.

Nous passons la prop `skyblue` au composant `Title` qui a été construit avec styled-components. Ensuite, nous pouvons simplement passer une fonction aux propriétés CSS que nous voulons modifier via les littéraux de gabarit. Comme vous pouvez le voir, nous passons une fonction fléchée `props => (props.skyblue ? 'skyblue' : 'black')` pour déterminer dans quelles conditions la couleur de Title doit être bleu ciel, et nous venons de terminer le changement de couleur de Title !

![Image](https://cdn-media-1.freecodecamp.org/images/1*heUmDWYNGBJjKDM7nc2kAA.png)

### Et le Débogage ?

Ouvrons Chrome Devtools pour voir ce qui se passe lorsque nous construisons un composant avec styled-components.

![Image](https://cdn-media-1.freecodecamp.org/images/1*McKlxIMuHFOWXY_tswRzDg.png)
_Ce qui se passe sur Chrome Devtools_

Styled-components dispose d'un système de modules CSS intégré. C'est génial pour résoudre le problème des conflits de noms de classes. Cependant, nous ne savons définitivement pas quelles classes nous utilisons lorsque nous essayons de déboguer sur Chrome Devtools. De plus, lorsque nous vérifions la fonction de rendu dans `Content.jsx` :

Savez-vous quel élément HTML nous utilisons ? Absolument pas, n'est-ce pas ? Vous devez revenir en arrière sur chaque styled-component pour vérifier quel élément HTML il utilise. C'est assez ennuyeux. De plus, lorsque vous construisez des styled-components de cette manière, vous abandonnez essentiellement les fonctionnalités puissantes des sélecteurs CSS.

En tenant compte des problèmes ci-dessus, je veux vous présenter une méthode simple pour construire un styled-component débogable, qui combine le CSS général avec styled-components.

### Combiner les Sélecteurs CSS avec Styled-components

Au début de cette partie, je veux que vous sachiez comment [styliser des composants existants avec styled-components](https://www.styled-components.com/docs/basics#styling-any-components).

> La méthode styled fonctionne parfaitement sur tous vos propres composants ou ceux de tiers. Tant qu'ils passent la prop className à leurs sous-composants rendus, qui doivent également la passer, et ainsi de suite. En fin de compte, le className doit être passé le long de la ligne à un nœud DOM réel pour que le style ait un effet.

Nous devons ajouter **className** aux composants généraux et nous pouvons les styliser facilement avec styled-components. Voyons comment en tirer parti pour construire un styled-component débogable.

Nous devons envelopper `Content.jsx` via la prop **className** et nous pouvons le styliser avec ce modèle :

`const StyledContent = styled(Content)` /* Propriétés CSS */ ``

Ensuite, nous pouvons envelopper n'importe quel composant dans le styled-component. De plus, nous pouvons également utiliser la puissance des sélecteurs CSS à l'intérieur du styled-component. Encore mieux, la syntaxe SCSS est disponible dans styled-components ! Voyons ce qui se passe lorsque nous ouvrons la console dans Chrome Devtools.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aUt6gsRAGgRr_ewJ6c_E8w.png)

Maintenant, les classes sont significatives, n'est-ce pas ? Et nous bénéficions toujours du système de modules CSS intégré grâce à la prop className. En résumé, vous devez simplement prendre soin des noms de classes CSS à l'intérieur du composant, puis tout ira bien ?. Vous vous souvenez comment nous modifions les propriétés CSS en passant une fonction à styled-components ? Cela fonctionne toujours avec cette méthode ! Bien sûr, le résultat ressemblera toujours à...

![Image](https://cdn-media-1.freecodecamp.org/images/1*heUmDWYNGBJjKDM7nc2kAA.png)

La vie n'a jamais été aussi belle !

### Conclusion

Nous avons passé en revue deux méthodes pour styliser un composant via le CSS traditionnel. Ensuite, nous avons appris comment styliser facilement des composants avec styled-components. Enfin, nous avons combiné les sélecteurs CSS avec styled-components. Maintenant, les composants peuvent être facilement stylisés et sont également débogables.

Si vous voulez essayer styled-components pour styliser vos composants, mais que vous ressentez la douleur lors du débogage, je vous recommande d'essayer cette méthode.

### [DÉMO](https://chun-lin.github.io/Debuggable-Styled-Components-Example/)

### Code Source

Vous pouvez consulter le code source de chaque méthode sur mon dépôt Github

1. [Style Inline](https://github.com/Chun-Lin/Debuggable-Styled-Components-Example/tree/general-css-version)

2. [Ajouter une Nouvelle Classe](https://github.com/Chun-Lin/Debuggable-Styled-Components-Example/tree/general-css-version)

3. [Styled-components](https://github.com/Chun-Lin/Debuggable-Styled-Components-Example/tree/styled-components-version)

4. [Combiner les Sélecteurs CSS avec styled-components](https://github.com/Chun-Lin/Debuggable-Styled-Components-Example/tree/styled-components-css-selectors)

Merci d'avoir lu mon article. J'espère qu'il n'a pas perdu votre temps. Si vous aimez cet article, n'hésitez pas à m'applaudir ???. Vos applaudissements me motiveront à écrire plus d'articles de haute qualité .

Suivez-moi sur [Twitter](https://twitter.com/wulin40063)

Suivez-moi sur [Github](https://github.com/Chun-Lin)

Connectez-vous avec moi sur [LinkedIn](https://www.linkedin.com/in/chunlin-wu-4114809b/)