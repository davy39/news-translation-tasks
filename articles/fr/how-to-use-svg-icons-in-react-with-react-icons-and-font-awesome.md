---
title: Comment utiliser les icônes SVG dans React avec React Icons et Font Awesome
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-09-24T16:07:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-svg-icons-in-react-with-react-icons-and-font-awesome
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/react-icons.jpg
tags:
- name: Icons
  slug: icons
- name: React
  slug: react
- name: SVG
  slug: svg
seo_title: Comment utiliser les icônes SVG dans React avec React Icons et Font Awesome
seo_desc: "Icons are a way to visually communicate concepts and meaning without the\
  \ use of words. This could be for categorization, an action, or even a warning.\
  \ \nHow can we add icons using SVG to our React apps to improve our visual communication?\n\
  \nWhat is SVG..."
---

Les icônes sont un moyen de communiquer visuellement des concepts et des significations sans utiliser de mots. Cela peut être pour la catégorisation, une action, ou même un avertissement. 

Comment pouvons-nous ajouter des icônes utilisant SVG à nos applications React pour améliorer notre communication visuelle ?

* [Qu'est-ce que SVG ?](#heading-quest-ce-que-svg)
* [Pourquoi SVG est-il idéal pour le web ?](#heading-pourquoi-svg-est-il-ideal-pour-le-web)
* [Partie 0 : Créer une application React](#heading-partie-0-creer-une-application-react)
* [Partie 1 : Ajouter des icônes SVG avec react-icons](#heading-partie-1-ajouter-des-iconessvg-avec-react-icons)
* [Partie 2 : Ajouter manuellement des fichiers SVG à un composant React](#heading-partie-2-ajouter-manuellement-des-fichiers-svg-a-un-composant-react)

%[https://www.youtube.com/watch?v=OtcA2EAlldo]

## Qu'est-ce que SVG ?

[SVG](https://www.w3.org/Graphics/SVG/) signifie Scalable Vector Graphics. C'est un format de fichier basé sur un langage de balisage similaire à XML qui permet aux développeurs et designers de créer des images vectorielles en utilisant des définitions de chemins.

## Pourquoi SVG est-il idéal pour le web ?

SVG a été conçu pour le web. C'est un standard ouvert créé par le W3C pour offrir une meilleure façon d'ajouter des images au web. Si vous ouvrez un fichier SVG sur votre ordinateur, vous pourriez être surpris de constater qu'il s'agit entièrement de code !

Cela contribue à la petite taille des fichiers. Typiquement, lorsque vous utilisez SVG, vous pouvez profiter de sa taille réduite par rapport aux fichiers image plus volumineux qui pourraient être nécessaires pour offrir la même haute résolution.

De plus, puisque nous définissons SVG comme des chemins, ils peuvent être redimensionnés aussi grands ou aussi petits que nous le souhaitons. Cela les rend particulièrement flexibles pour une utilisation sur le web, surtout lorsque vous créez des expériences responsives.

## Que allons-nous créer ?

Nous allons d'abord parcourir l'utilisation d'un package appelé [react-icons](https://react-icons.github.io/react-icons/) qui nous permettra d'importer facilement des icônes depuis des ensembles d'icônes populaires comme [Font Awesome](https://fontawesome.com/) directement dans notre application.

Nous allons également voir comment nous pouvons ajouter manuellement des fichiers SVG directement dans notre application en copiant le code d'un fichier SVG dans un nouveau composant.

## Partie 0 : Créer une application React

Pour ce guide, vous pouvez utiliser n'importe quel framework React que vous souhaitez, que ce soit [Create React App](https://create-react-app.dev/) ou [Next.js](https://nextjs.org/). Vous pouvez même utiliser un projet existant.

Puisque nous n'avons pas besoin de quoi que ce soit de spécial pour ajouter nos icônes, je vais utiliser create-react-app.

Pour commencer avec create-react-app, vous pouvez créer un nouveau projet en utilisant la commande suivante dans votre terminal :

```
yarn create react-app [nom-du-projet]
# ou
npx create-react-app [nom-du-projet]

```

_Note : remplacez `[nom-du-projet]` par le nom que vous souhaitez utiliser pour votre projet. Je vais utiliser `mes-icones-svg`._

Une fois que vous avez votre nouvelle application ou votre application existante, nous devrions être prêts à commencer !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/new-create-react-app.jpg)
_Nouvelle application Create React App_

## Partie 1 : Ajouter des icônes SVG avec react-icons

### Ajouter react-icons à votre projet

Pour commencer avec react-icons, nous voulons l'installer dans notre projet.

À l'intérieur de votre projet, exécutez la commande suivante :

```
yarn add react-icons
# ou
npm install react-icons --save

```

Une fois l'installation terminée, nous devrions être prêts à l'utiliser dans notre projet.

### Sélectionner des icônes pour un projet

L'une des choses intéressantes à propos de react-icons est la bibliothèque extensive qu'ils mettent à disposition dans un seul package.

Non seulement avons-nous Font Awesome immédiatement disponible, mais nous avons également [les Octicons de GitHub](https://primer.style/octicons), [Heroicons](https://heroicons.com/), [les icônes Material Design](https://google.github.io/material-design-icons/), et [beaucoup d'autres](https://react-icons.github.io/).

![Image](https://www.freecodecamp.org/news/content/images/2020/09/react-icons-heroicons.jpg)
_react-icons Heroicons_

Lors du choix des icônes, vous avez pratiquement la possibilité d'utiliser n'importe quelle icône à tout moment. Cela dit, je recommanderais d'essayer de garder une apparence et une sensation cohérentes avec vos icônes.

Si vous utilisez principalement Font Awesome pour votre site web, cela pourrait sembler un peu étrange et incohérent si vous commenciez à ajouter [des icônes de couleurs plates](https://react-icons.github.io/icons?name=fc) au mélange. Vous voulez finalement offrir une expérience que les gens pourront facilement identifier les motifs que vous créez.

### Utiliser react-icons dans votre projet

Une fois que vous avez trouvé les icônes que vous souhaitez utiliser, nous pouvons maintenant les ajouter à notre projet.

Le site web de react-icons facilite la recherche du nom de l'icône que nous voulons utiliser pour l'importer dans notre projet.

Si nous voulions utiliser l'icône de fusée Font Awesome, nous pouvons naviguer vers Font Awesome dans la barre latérale, rechercher la page pour "rocket" (CMD+F ou CTRL+F), puis cliquer sur l'icône qui copiera son nom dans votre presse-papiers.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/font-awesome-rocket.jpg)
_Icône de fusée Font Awesome_

Nous pourrions également rechercher "rocket" dans le formulaire de recherche en haut à gauche de la page, ce qui nous montre le résultat "rocket" dans tous les ensembles d'icônes.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/react-icons-rocket.jpg)
_Icônes de fusée dans react-icons_

À l'intérieur de notre projet, nous pouvons maintenant importer cette icône. Similaire aux instructions en haut de la page react-icons, nous voulons importer cette icône spécifique depuis `react-icons/fa`, qui fait référence au module Font Awesome de react-icons.

Ajoutez ce qui suit en haut du fichier dans lequel vous souhaitez importer l'icône. Si vous utilisez un nouveau projet create-react-app, vous pouvez l'ajouter en haut de `src/App.js`.

```js
import { FaRocket } from 'react-icons/fa';

```

Pour tester cela, remplaçons le logo React par notre icône.

Supprimez le composant `<img` et ajoutez plutôt :

```jsx
<FaRocket />

```

Et si nous rechargeons la page, nous pouvons voir notre fusée !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/create-react-app-rocket-icon.jpg)
_Icône de fusée dans l'application React_

Notre fusée ne tourne pas comme le logo React, alors corrigeons cela.

Ajoutez la classe `.App-logo` au composant `FaRocket` :

```jsx
<FaRocket className="App-logo" />

```

Et la fusée devrait maintenant tourner !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/create-react-app-rocket-spin.gif)
_Icône de fusée tournante dans l'application React_

Mais elle est aussi un peu petite. Si nous regardons dans `src/App.css`, nous définissons la hauteur de `.App-logo` à `40vmin`. Bien que cela fonctionne, pour que notre icône remplisse l'espace, nous devons également fournir une largeur pour qu'elle le remplisse.

Ajoutez ce qui suit à la classe `.App-logo` pour ajouter une largeur :

```css
width: 40vmin;

```

Et bien qu'elle soit probablement un peu trop grande maintenant, nous avons une taille plus appropriée et nous avons notre icône !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/create-react-app-icon-rocket-spin-large.gif)
_Taille augmentée de l'icône de fusée tournante dans l'application React_

[Suivez avec le commit](https://github.com/colbyfayock/my-svg-icons/commit/036112c3e2ffc5f42a53c68e8025fe70a87e3b13).

## Partie 2 : Ajouter manuellement des fichiers SVG à un composant React

Parfois, vous ne voulez pas ajouter une nouvelle bibliothèque juste pour obtenir une icône. Parfois, il s'agit d'une icône personnalisée qui n'est pas disponible dans une bibliothèque publique.

Heureusement avec React, nous pouvons créer un nouveau composant SVG assez facilement qui nous permet d'ajouter nos icônes SVG personnalisées n'importe où nous le souhaitons.

Tout d'abord, trouvons une icône.

Bien que toutes les Heroicons soient disponibles dans react-icons, utilisons-la comme exemple puisque c'est facile de trouver et de copier du code SVG.

Allez sur heroicons.com et recherchez une icône que vous aimeriez utiliser pour cet exemple. Je vais utiliser "globe".

Après avoir trouvé l'icône que vous voulez, survolez cette icône, où vous verrez des options pour copier cette icône en tant que SVG ou JSX, et copiez-la en tant que JSX.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/heroicons-copy-svg.gif)
_Copier en tant que JSX dans Heroicons_

Avec cette icône copiée, créez un nouveau fichier sous `src` appelé `Globe.js`.

À l'intérieur de ce fichier, nous allons créer un nouveau composant appelé Globe et coller notre SVG dans ce composant.

```jsx
import React from 'react';

const Globe = () => {
  return (
    <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3.055 11H5a2 2 0 012 2v1a2 2 0 002 2 2 2 0 012 2v2.945M8 3.935V5.5A2.5 2.5 0 0010.5 8h.5a2 2 0 012 2 2 2 0 104 0 2 2 0 012-2h1.064M15 20.488V18a2 2 0 012-2h3.064M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
    </svg>
  )
}

export default Globe;

```

_Note : lors de la copie d'un SVG normal dans un composant React, cela pourrait ne pas fonctionner "tel quel". Parfois, les fichiers SVG incluent des classes CSS ou des attributs d'éléments qui ne sont pas valides avec JSX._

_Si vous rencontrez des erreurs, essayez de corriger les attributs et regardez la console web pour voir les avertissements et erreurs que React génère. Parce que nous avons copié en tant que JSX, nous avons pu le faire fonctionner immédiatement._

Maintenant, retournez à `src/App.js` et importez notre nouveau composant :

```js
import Globe from './Globe';

```

Ensuite, nous pouvons remplacer notre icône de fusée par notre nouveau composant :

```jsx
<Globe />

```

Et si nous ouvrons notre navigateur, nous pouvons voir notre globe !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/create-react-app-globe-large.jpg)
_Grand globe icône dans l'application React_

Bien qu'il soit un peu grand.

Nous voulons appliquer notre classe `.App-logo` à notre composant Globe, donc nous devons mettre à jour ce composant pour accepter une prop `className`.

Retournez à `src/Globe.js`, ajoutez un argument de prop `className` :

```
const Globe = ({ className }) => {

```

Ensuite, ajoutez une nouvelle prop avec ce `className` au composant `<svg` :

```jsx
<svg className={className}

```

Maintenant, nous pouvons mettre à jour notre composant Globe dans `src/App.js` pour inclure cette classe :

```jsx
<Globe className="App-logo" />

```

Et si nous rechargeons la page, nous pouvons voir que notre logo est revenu à la bonne taille et qu'il tourne à nouveau !

![Image](https://www.freecodecamp.org/news/content/images/2020/09/create-react-app-globe-icon-spinning.gif)
_Icône de globe de taille normale et tournante dans l'application React_

[Suivez avec le commit](https://github.com/colbyfayock/my-svg-icons/commit/87b00748fc9b38d80336ddb5f6f823388c2edead).

## Pourquoi ne pas l'inclure en tant que fichier img ?

Bien que nous puissions l'inclure en tant que fichier image comme le fait React dans le code par défaut de create-react-app, nous obtenons quelques avantages à ajouter nos fichiers SVG "en ligne".

Tout d'abord, lorsque nous ajoutons SVG en ligne, nous pouvons accéder aux différents chemins avec des propriétés CSS. Cela nous donne plus de flexibilité pour le personnaliser dynamiquement.

Cela va également réduire le nombre de requêtes HTTP. Le navigateur saura comment charger ce SVG, donc nous n'avons pas besoin de déranger le navigateur pour demander ce fichier à inclure dans la page.

Cela dit, c'est toujours une option valable pour ajouter un fichier SVG à la page.

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4e73fb Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsor Me</a>
    </li>
  </ul>
</div>