---
title: Comment utiliser du CSS pur pour créer une belle animation de chargement pour
  votre application
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-05T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-css-to-create-a-beautiful-loading-animation-for-your-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/loading-animation.jpg
tags:
- name: animation
  slug: animation
- name: animations
  slug: animations
- name: CSS
  slug: css
- name: CSS3
  slug: css3
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: HTML5
  slug: html5
- name: Inspiration
  slug: inspiration
- name: Pure CSS
  slug: pure-css
- name: Web Applications
  slug: web-applications
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment utiliser du CSS pur pour créer une belle animation de chargement
  pour votre application
seo_desc: "If you've been around the internet lately, you've most likely seen a nice\
  \ subtle loading animation that fills page content before gracefully loading in.\
  \ \nSome of the social giants like Facebook even use this approach to give page\
  \ loading a better exp..."
---

Si vous avez navigué sur Internet récemment, vous avez très probablement vu une animation de chargement subtile qui remplit le contenu de la page avant de s'afficher gracieusement.

Certains géants des réseaux sociaux comme Facebook utilisent même cette approche pour offrir une meilleure expérience de chargement de page. Comment pouvons-nous faire cela avec juste un peu de CSS simple ?

* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Vous voulez juste le snippet ?](#heading-vous-voulez-juste-le-snippet)
* [Partie 1 : Créer notre animation de chargement](#heading-partie-1-creer-notre-animation-de-chargement)
* [Partie 2 : Utiliser notre animation de chargement dans une application dynamique](#heading-partie-2-utiliser-notre-animation-de-chargement-dans-une-application-dynamique)

%[https://www.youtube.com/watch?v=auyZWWjXJCo]

## Que allons-nous construire ?

Nous allons créer une animation de chargement en utilisant une classe CSS que vous pouvez appliquer à peu près à n'importe quel élément (dans la limite du raisonnable).

![Image](https://www.freecodecamp.org/news/content/images/2020/05/loading-animation.gif)
_Aperçu de l'animation de chargement_

Cela vous donne une grande flexibilité d'utilisation et rend la solution simple et élégante avec seulement du CSS.

Bien que le snippet soit assez court et que vous puissiez simplement le copier-coller, je vais vous expliquer ce qui se passe et vous montrer un exemple d'utilisation dynamique lors du chargement de données.

## Vous voulez juste le snippet ?

Vous pouvez le récupérer ici !

%[https://gist.github.com/colbyfayock/d155418975d1e0e04b2805e285296033]

## Dois-je savoir comment animer avant ce tutoriel ?

Non ! Nous allons détailler exactement ce que vous devez faire. En fait, l'animation dans ce tutoriel est relativement simple, alors plongeons-nous dedans !

## Partie 1 : Créer notre animation de chargement

Cette première partie va se concentrer sur la mise en place de l'animation de chargement et son observation sur un site HTML statique. L'objectif est de passer par la création réelle du snippet. Nous n'utiliserons que du HTML et du CSS pour cette partie.

### Étape 1 : Créer du contenu d'exemple

Pour commencer, nous allons avoir besoin d'un peu de contenu d'exemple. Il n'y a vraiment aucune restriction ici, vous pouvez créer cela avec du HTML et CSS de base ou l'ajouter à votre Create React App !

Pour cette démonstration, je vais utiliser du HTML et du CSS avec quelques exemples de contenu qui nous permettront de voir l'effet.

Pour commencer, créez un nouveau fichier HTML. À l'intérieur de ce fichier HTML, remplissez-le avec du contenu qui nous donnera la possibilité de jouer avec notre animation. Je vais utiliser [fillerama](http://fillerama.io/) qui utilise des répliques de ma série télévisée préférée [Futurama](https://en.wikipedia.org/wiki/Futurama) !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-website-fillerama.jpg)
_Page web HTML & CSS statique avec du contenu provenant de fillerama.io_

Si vous suivez avec moi, voici à quoi ressemble mon projet :

```
my-css-loading-animation-static
- index.html
- main.css

```

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-static/commit/9aa7925f7048fa1b73fef74d0d56380c29fc5d73)

### Étape 2 : Commencer avec une classe de chargement de base

Pour notre base, créons une nouvelle classe CSS. Dans notre fichier CSS, ajoutons :

```css
.loading {
  background: #eceff1;
}

```

Avec cette classe, ajoutons-la à quelques-uns ou à tous nos éléments. Je l'ai ajoutée à quelques paragraphes, titres et listes.

```html
<p class="loading">Par exemple...

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-gray-background.jpg)
_Page web HTML & CSS statique avec un fond gris pour le contenu_

Cela nous donne un arrière-plan de base, mais nous voudrions probablement masquer ce texte. Lors du chargement, nous n'aurons pas encore ce texte, donc nous voudrons très probablement utiliser du texte de remplissage ou une hauteur fixe. Quoi qu'il en soit, nous pouvons définir la couleur sur transparent :

```css
.loading {
  color: transparent;
  background: #eceff1;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-gray-background-hidden-text.jpg)
_Page web HTML & CSS statique avec un fond gris et une couleur transparente pour le contenu_

Si vous remarquez avec les éléments de liste, que vous appliquiez la classe à l'élément de liste de niveau supérieur (`<ol>` ou `<ul>`) par rapport à l'élément de liste lui-même (`<li>`), cela ressemble à un gros bloc. Si nous ajoutons une petite marge au bas de tous les éléments de liste, nous pouvons voir une différence dans leur affichage :

```css
li {
  margin-bottom: .5em;
}

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-gray-background-different-lists.jpg)
_Différence de style entre l'application à la liste de niveau supérieur ou aux éléments de liste_

Et maintenant, cela commence à prendre forme, mais cela ressemble un peu à de simples espaces réservés. Animons donc cela pour que cela donne l'impression d'être réellement en train de charger.

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-static/commit/f68cdef36be11311a5cc11a1d39e52ea7e7bb48d)

### Étape 3 : Styler et animer notre classe de chargement

Avant d'animer réellement notre classe, nous avons besoin de quelque chose à animer, alors ajoutons un dégradé à notre classe `.loading` :

```css
.loading {
  color: transparent;
  background: linear-gradient(100deg, #eceff1 30%, #f6f7f8 50%, #eceff1 70%);
}

```

Cela signifie que nous voulons un [linear-gradient](https://developer.mozilla.org/en-US/docs/Web/CSS/linear-gradient) incliné à 100 degrés, où nous commençons avec `#eceff1`, passons à `#f6f7f8` à 30% et revenons à `#eceff1` à 70% ;

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-gray-background-subtle-gradient.jpg)
_Arrière-plan en dégradé subtil qui pourrait ressembler à un reflet_

C'est difficile à voir au début quand c'est statique, cela pourrait juste ressembler à un reflet sur votre ordinateur ! Si vous souhaitez le voir avant de continuer, n'hésitez pas à jouer avec les couleurs ci-dessus pour voir le dégradé.

Maintenant que nous avons quelque chose à animer, nous allons d'abord devoir créer une règle [keyframes](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes) :

```css
@keyframes loading {
  0% {
    background-position: 100% 50%;
  }
  100% {
    background-position: 0 50%;
  }
}

```

Cette règle, lorsqu'elle est appliquée, changera la position de l'arrière-plan en partant de 100% de l'axe x vers 0% de l'axe x.

Avec cette règle, nous pouvons ajouter notre propriété [animation](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Animations/Using_CSS_animations) à notre classe `.loading` :

```css
.loading {
  color: transparent;
  background: linear-gradient(100deg, #eceff1 30%, #f6f7f8 50%, #eceff1 70%);
  animation: loading 1.2s ease-in-out infinite;
}

```

Notre ligne d'animation définit l'image clé sur `loading`, lui dit de durer 1,2 seconde, définit la [timing function](https://developer.mozilla.org/en-US/docs/Web/CSS/animation-timing-function) sur `ease-in-out` pour la rendre fluide, et lui dit de boucler éternellement avec `infinite`.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-gray-background-subtle-gradient.jpg)
_Aucun changement – cela ne s'anime pas_

Si vous remarquez pourtant après avoir enregistré cela, il ne se passe toujours rien. La raison en est que nous définissons notre dégradé d'une extrémité de l'élément DOM à l'autre, donc il n'y a nulle part où bouger !

Essayons donc de définir également un `background-size` sur notre classe `.loading`.

```css
.loading {
  color: transparent;
  background: linear-gradient(100deg, #eceff1 30%, #f6f7f8 50%, #eceff1 70%);
  background-size: 400%;
  animation: loading 1.2s ease-in-out infinite;
}

```

Maintenant, puisque notre arrière-plan s'étend au-delà de notre élément DOM (vous ne pouvez pas voir cette partie), il a de l'espace pour s'animer et nous obtenons notre animation !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/static-html-css-loading-animation.gif)
_Notre animation de chargement !_

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-static/commit/bc4b5ec955a0906fea032edbbaf90f037f76c91b)

## Partie 2 : Utiliser notre animation de chargement dans une application dynamique

Maintenant que nous avons notre animation de chargement, mettons-la en action avec un exemple basique où nous simulons un état de chargement.

L'astuce pour l'utiliser réellement est que, généralement, nous n'avons pas le contenu réel disponible, donc dans la plupart des cas, nous devons le simuler.

Pour vous montrer comment nous pouvons faire cela, nous allons construire une application [React](https://reactjs.org/) simple avec [Next.js](https://nextjs.org/).

### Étape 1 : Créer un exemple d'application React avec Next.js

Naviguez vers le répertoire dans lequel vous souhaitez créer votre nouveau projet et lancez :

```shell
yarn create next-app
# ou
npm init next-app

```

Il vous demandera quelques options, notamment un nom qui déterminera le répertoire dans lequel le projet est créé et le type de projet. J'utilise `my-css-loading-animation-dynamic` et l'application "Default Starter App".

![Image](https://www.freecodecamp.org/news/content/images/2020/05/nextjs-new-project.jpg)
_Création d'un nouveau projet avec Next.js_

Une fois installé, naviguez dans votre nouveau répertoire et lancez votre serveur de développement :

```
cd [directory]
yarn dev
# ou 
npm run dev

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/nextjs-starting-dev-server.jpg)
_Démarrage du serveur de développement avec Next.js_

Ensuite, remplaçons le contenu de notre fichier `pages/index.js`. Je vais dériver le contenu de l'exemple précédent, mais nous allons le créer de la même manière que ce que nous pourrions attendre d'une API. Tout d'abord, ajoutons notre contenu sous forme d'objet au-dessus de notre instruction return :

```javascript
const content = {
  header: `Alors, quoi de neuf avec les Knicks ?`,
  intro: `Comment s'appellent-ils ? Je suis le Père Noël ! Cet opéra est aussi minable qu'il est brillant ! Vos paroles manquent de subtilité. Vous ne pouvez pas simplement faire annoncer à vos personnages ce qu'ils ressentent. Ça me met en colère ! Bonne nouvelle, tout le monde ! J'ai appris au grille-pain à ressentir l'amour !`,
  list: [
    `Oui ! Dans ta face, Gandhi !`,
    `Donc je suis vraiment important ? Ce que je ressens quand je suis ivre est correct ?`,
    `Qui sont ces horribles hommes oranges ?`
  ]
}
```

Pour afficher ce contenu, à l'intérieur de `<main>`, remplaçons le contenu par :

```jsx
<main>
  <h1>{ content.header }</h1>
  <p>{ content.intro }</p>
  <ul>
    { content.list.map((item, i) => {
      return (
        <li key={i}>{ item }</li>
      )
    })}
  </ul>
</main>

```

Et pour les styles, vous pouvez copier et coller tout ce qui se trouve dans notre fichier `main.css` de la Partie 1 dans les balises `<style>` en bas de notre page d'index. Cela nous donnera :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/basic-content-with-nextjs.jpg)
_Contenu de base avec Next.js_

Avec cela, nous devrions être revenus à un point similaire à celui où nous nous sommes arrêtés dans la Partie 1, sauf que nous n'utilisons pas encore activement les animations de chargement.

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-dynamic/commit/365e081522ec07b1754bf360a95b0bc373476c95)

### Étape 2 : Simuler le chargement de données depuis une API

L'exemple sur lequel nous travaillons est assez simple. Vous verriez probablement cela arriver pré-généré de manière statique, mais cela nous aide à créer une démo réaliste avec laquelle nous pouvons tester notre animation de chargement.

Pour simuler notre état de chargement, nous allons utiliser `useState`, `useEffect` de React, et un bon vieux `setTimeout` pour précharger du contenu de "chargement", et après la fin du `setTimeout`, mettre à jour ce contenu avec nos données réelles. En attendant, nous saurons que nous sommes dans un état de chargement avec une instance séparée de `useState`.

Tout d'abord, nous devons importer nos dépendances. En haut de notre fichier `pages/index.js`, ajoutez :

```jsx
import { useState, useEffect } from 'react';

```

Au-dessus de notre objet `content`, ajoutons un peu d'état :

```jsx
const [loadingState, updateLoadingState] = useState(true);
const [contentState, updateContentState] = useState({})

```

Et dans notre contenu, nous pouvons mettre à jour les instances pour utiliser cet état :

```jsx
<h1>{ contentState.header }</h1>
<p>{ contentState.intro }</p>
<ul>
  { contentState.list.map((item, i) => {
    return (
      <li key={i}>{ item }</li>
    )
  })}
</ul>

```

Une fois que vous aurez enregistré et chargé cela, vous remarquerez d'abord que nous obtenons une erreur parce que notre propriété `list` n'existe pas sur notre `contentState`, nous pouvons donc d'abord corriger cela :

```jsx
{ Array.isArray(contentState.list) && contentState.list.map((item, i) => {
  return (
    <li key={i}>{ item }</li>
  )
})}

```

Et une fois que c'est prêt, ajoutons notre `setTimeout` à l'intérieur d'un hook `useEffect` pour simuler le chargement de nos données. Ajoutez ceci sous notre objet `content` :

```jsx
useEffect(() => {
  setTimeout(() => {
    updateContentState(content);
    updateLoadingState(false)
  }, 2000);
}, [])

```

Une fois que vous aurez enregistré et ouvert votre navigateur, vous remarquerez que pendant 2 secondes vous n'avez aucun contenu, puis il se charge, simulant ainsi le chargement asynchrone de ces données.

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-dynamic/commit/f0cada8d696ffe3e983f5efc03dc9d75a2245fe1)

### Étape 3 : Ajouter notre animation de chargement

Maintenant, nous pouvons enfin ajouter notre animation de chargement. Pour ce faire, nous allons utiliser notre état de chargement que nous avons configuré avec `useState` et si le contenu est en cours de chargement, ajouter notre classe `.loading` à nos éléments.

Avant de faire cela, au lieu d'ajouter individuellement cette classe à chaque élément du DOM, il pourrait être plus judicieux de le faire via CSS en ajoutant la classe au parent, alors faisons cela d'abord.

Tout d'abord, mettez à jour la classe `.loading` pour cibler nos éléments :

```css
.loading h1,
.loading p,
.loading li {
  color: transparent;
  background: linear-gradient(100deg, #eceff1 30%, #f6f7f8 50%, #eceff1 70%);
  background-size: 400%;
  animation: loading 1.2s ease-in-out infinite;
}

```

Ensuite, nous pouvons ajouter dynamiquement notre classe à notre balise `<main>` :

```jsx
<main className={loadingState ? 'loading' : ''}>

```

_Note : si vous utilisez [Sass](https://sass-lang.com/), vous pouvez gérer vos styles de chargement en [étendant](https://sass-lang.com/documentation/at-rules/extend) la classe `.loading` dans les instances où vous souhaitez l'utiliser ou créer un [placeholder](https://sass-lang.com/documentation/style-rules/placeholder-selectors) et l'étendre !_

Et si vous rafraîchissez la page, vous remarquerez que c'est toujours une page blanche pendant 2 secondes !

Le problème est que lorsque nous chargeons notre contenu, rien n'existe à l'intérieur de nos balises qui permettrait à la hauteur de ligne des éléments de lui donner une hauteur.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-css-collapsed-content.jpg)
_Aucune hauteur lorsqu'il n'y a pas de contenu_

Mais nous pouvons corriger cela ! Parce que notre classe `.loading` rend notre texte transparent, nous pouvons simplement ajouter le mot `Chargement` pour chaque élément de contenu :

```jsx
const [contentState, updateContentState] = useState({
  header: 'Chargement',
  intro: 'Chargement',
  list: [
    'Chargement',
    'Chargement',
    'Chargement'
  ]
})

```

_Note : Nous ne pouvons pas utiliser un espace vide ici car cela seul ne nous fournira pas de hauteur lors du rendu dans le DOM._

Et une fois que vous aurez enregistré et rechargé la page, nos 2 premières secondes auront un état de chargement qui reflète notre contenu !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-css-loading-animation-1.gif)
_Animation de chargement HTML & CSS_

[Suivez avec le commit !](https://github.com/colbyfayock/my-css-loading-animation-dynamic/commit/5b7b1c40d1eebf97f65c966bb771a5f6787073ea)

## Quelques réflexions supplémentaires

Cette technique peut être utilisée assez largement. Le fait d'être une classe CSS la rend facile à ajouter partout où vous le souhaitez.

Si vous n'aimez pas l'idée de définir le texte `Chargement` pour l'état de chargement, une autre option consiste à définir une hauteur fixe. Le seul problème est que cela nécessite plus de maintenance pour ajuster le CSS afin qu'il corresponde à ce à quoi ressemblera le contenu chargé.

De plus, ce ne sera pas parfait. Le plus souvent, vous ne saurez pas exactement quelle quantité de texte vous avez sur une page. L'objectif est de simuler et de suggérer qu'il y aura du contenu et qu'il est actuellement en cours de chargement.

## Quelle est votre animation de chargement préférée ?

Faites-le moi savoir sur [Twitter](https://twitter.com/colbyfayock) !

## Rejoignez la conversation !

%[https://twitter.com/freeCodeCamp/status/1264557769547493376]

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?️ Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">✉️ Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>