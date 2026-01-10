---
title: Qu'est-ce que Tailwind CSS et comment l'ajouter à mon site web ou à mon application
  React ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-05-19T14:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-tailwind-css-and-how-can-i-add-it-to-my-website-or-react-app
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/tailwind-1.jpg
tags:
- name: CSS
  slug: css
- name: CSS Framework
  slug: css-framework
- name: CSS3
  slug: css3
- name: Developer Tools
  slug: developer-tools
- name: framework
  slug: framework
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: PostCSS
  slug: postcss
- name: tailwind
  slug: tailwind
- name: tools
  slug: tools
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que Tailwind CSS et comment l'ajouter à mon site web ou à mon
  application React ?
seo_desc: "CSS is a technology that can be your best or worst friend. While it's incredibly\
  \ flexible and can produce what seems like magic, without the proper care and attention,\
  \ it can become hard to manage like any other code. \nHow can Tailwind CSS help\
  \ us to..."
---

CSS est une technologie qui peut être votre meilleur ami ou votre pire ennemi. Bien qu'elle soit incroyablement flexible et puisse produire ce qui semble être de la magie, sans les soins et l'attention appropriés, elle peut devenir difficile à gérer comme tout autre code. 

Comment Tailwind CSS peut-il nous aider à prendre le contrôle de nos styles ?

* [Qu'est-ce que Tailwind ?](#heading-quest-ce-que-tailwind)
* [Alors, qu'est-ce qui rend Tailwind génial ?](#heading-alors-quest-ce-qui-rend-tailwind-genial)
* [Partie 1 : Ajout de Tailwind CSS à une page HTML statique](#heading-partie-1-ajout-de-tailwind-css-a-une-page-html-statique)
* [Partie 2 : Ajout de Tailwind CSS à une application React](#heading-partie-2-ajout-de-tailwind-css-a-une-application-react)

%[https://www.youtube.com/watch?v=7KeZcRMltP0]

## Qu'est-ce que Tailwind ?

[Tailwind CSS](https://tailwindcss.com/) est un framework CSS "utility-first" qui fournit un catalogue approfondi de classes CSS et d'outils vous permettant de commencer facilement à styliser votre site web ou votre application.

L'objectif sous-jacent est que, lors de la construction de votre projet, vous n'ayez pas besoin de gérer les styles en cascade et de vous soucier de la manière de remplacer cet empilement de 10 sélecteurs qui hante votre application depuis les 2 dernières années.

## Alors, qu'est-ce qui rend Tailwind génial ?

La solution de Tailwind est de fournir une large variété de classes CSS, chacune ayant son propre usage ciblé. Au lieu d'une classe appelée `.btn` créée avec un ensemble d'attributs CSS directement, dans Tailwind, vous appliqueriez soit un ensemble de classes comme `bg-blue-500 py-2 px-4 rounded` à l'élément bouton, soit vous créeriez une classe `.btn` en [appliquant](https://tailwindcss.com/docs/functions-and-directives/#apply) ces classes utilitaires à ce sélecteur.

Bien que Tailwind ait beaucoup plus à offrir, nous allons nous concentrer sur ces bases pour ce tutoriel, alors commençons !

## Partie 1 : Ajout de Tailwind CSS à une page HTML statique

Nous allons commencer par appliquer Tailwind CSS directement à une page HTML statique. L'espoir est qu'en nous concentrant sur Tailwind et non sur l'application, nous puissions mieux comprendre ce qui se passe réellement avec le framework.

### Étape 1 : Création d'une nouvelle page

Vous pouvez commencer simplement en créant un nouveau fichier HTML. Pour le contenu, vous pouvez utiliser ce que vous voulez, mais je vais utiliser [fillerama.io](http://fillerama.io/) pour que le contenu de remplissage soit un peu plus amusant.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-with-content.jpg)
_Nouvelle page HTML avec contenu_

Si vous souhaitez simplifier cette étape, vous pouvez simplement [copier le fichier que j'ai créé](https://github.com/colbyfayock/my-tailwind-static/commit/c7db11899c9cd193cdd666fd228cfaefe75623f2#diff-eacf331f0ffc35d4b482f1d15a887d3b) pour commencer.

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-static/commit/c7db11899c9cd193cdd666fd228cfaefe75623f2)

### Étape 2 : Ajout de Tailwind CSS via CDN

Tailwind recommande généralement d'installer via [npm](https://www.npmjs.com/package/tailwindcss) pour obtenir toutes les fonctionnalités, mais encore une fois, nous essayons simplement de comprendre comment cela fonctionne d'abord.

Alors, ajoutons un lien vers le fichier CDN dans le `<head>` de notre document :

```html
<link href="https://unpkg.com/tailwindcss@^1.0/dist/tailwind.min.css" rel="stylesheet">
```

Une fois que vous avez sauvegardé et rechargé la page, la première chose que vous remarquerez est que tous les styles ont été supprimés !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-tailwind-base.jpg)
_Page HTML avec la base de Tailwind CSS_

C'est attendu. Tailwind inclut un ensemble de [styles de prévol](https://tailwindcss.com/docs/preflight) pour corriger les incohérences entre les navigateurs. Entre autres, ils incluent le populaire [normalize.css](https://github.com/necolas/normalize.css/) sur lequel ils construisent avec leurs propres styles.

Mais nous allons apprendre à utiliser Tailwind pour ajouter nos styles et configurer les choses comme nous le voulons !

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-static/commit/b431b75cee0a03154a70b194b6dfcf028bc65942)

### Étape 3 : Utilisation de Tailwind CSS pour ajouter des styles à votre page

Maintenant que nous avons installé Tailwind, nous avons ajouté la possibilité d'utiliser leur énorme bibliothèque de classes utilitaires que nous allons maintenant utiliser pour ajouter des styles à notre page.

Commençons par ajouter une marge à tous nos paragraphes (`<p>`) et à nos éléments de liste (`<ol>`, `<ul>`). Nous pouvons faire cela en ajoutant la classe `.my-5` à chaque élément comme suit :

```html
<p class="my-5">
  Bender, arrête de détruire l'univers ! Oui, je fais ça avec ma stupidité. Je ne t'ai jamais aimé. Continuons...
  Belliqueux et nombreux.
</p>

```

Le nom de la classe suit un modèle que vous remarquerez avec le reste des classes utilitaires — `.my-5` signifie marge (m) appliquée à l'axe y (y) avec une valeur de 5 qui, dans le cas de Tailwind, utilise [rem](https://developer.mozilla.org/en-US/docs/Learn/CSS/Building_blocks/Values_and_units), donc la valeur est de 5rem.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-paragraph-styles.jpg)
_Page HTML avec des styles de paragraphe de base_

Ensuite, faisons en sorte que nos en-têtes ressemblent à de vrais en-têtes. En commençant par notre balise `h1`, ajoutons :

```html
<h1 class="text-2xl font-bold mt-8 mb-5">

```

Voici ce qui se passe :

* `text-2xl` : définit la taille du texte (font-size) à 2xl. Dans Tailwind, ce 2xl équivaudra à 1,5rem
* `font-bold` : définit le poids du texte (font-weight) à bold
* `mt-8` : Similaire à `my-5`, cela définira la marge supérieure (t) à 8rem
* `mb-5` : Et cela définira la marge inférieure (b) à 5rem

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-header-styles.jpg)
_Page HTML avec H1 stylisé_

Avec ces classes ajoutées au `h1`, appliquons ces mêmes classes exactes au reste de nos éléments d'en-tête, mais en descendant dans la liste, réduisons la taille de la police, de sorte qu'elle ressemblera à :

* h2 : `text-xl`
* h3 : `text-lg`

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-all-headers-style.jpg)
_Page HTML avec tous les en-têtes stylisés_

Maintenant, faisons en sorte que nos éléments de liste ressemblent à des listes. En commençant par notre liste non ordonnée (`<ul>`), ajoutons ces classes :

```html
<ul class="list-disc list-inside my-5 pl-2">

```

Voici ce que nous ajoutons :

* `list-disc` : définit le style de liste à disc (les marqueurs sur chaque élément de ligne)
* `list-inside` : définit la position des marqueurs de liste en utilisant la position relative aux éléments de liste et à la liste elle-même avec list-style-position à inside
* `my-5` : définit la marge de l'axe y à 5rem
* `pl-2` : définit le remplissage gauche à 2rem

Ensuite, nous pouvons appliquer les mêmes classes exactes à notre liste ordonnée (`<ol>`), sauf qu'au lieu de `list-disc`, nous voulons changer notre type de style en `list-decimal`, afin que nous puissions voir les nombres étant donné qu'il s'agit d'une liste ordonnée.

```html
<ol class="list-decimal list-inside my-5 pl-2">

```

Et nous avons nos listes !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-styled-lists.jpg)
_Page HTML avec des listes stylisées_

Enfin, rendons notre contenu un peu plus facile à lire en définissant une largeur maximale et en centrant le contenu. Sur la balise `<body>`, ajoutez ce qui suit :

```html
<body class="max-w-4xl mx-auto">

```

/Note : Typiquement, vous ne voudriez pas appliquer ces classes au `<body>` lui-même, plutôt, vous pouvez envelopper tout votre contenu avec une balise `<main>`, mais puisque nous essayons simplement de comprendre comment cela fonctionne, nous allons nous en tenir à cela. N'hésitez pas à ajouter la balise `<main>` avec ces classes à la place si vous préférez !/

Et avec cela, nous avons notre page !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-content-centered.jpg)
_Page HTML avec contenu centré_

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-static/commit/06fd719c98d17e2242b61ec2ab7034436c1c2ba6)

### Étape 4 : Ajout d'un bouton et d'autres composants

Pour la dernière partie de notre exemple statique, ajoutons un bouton.

L'astuce avec Tailwind est qu'ils ne fournissent intentionnellement pas de classes de composants pré-cuits, l'idée étant que les gens devraient probablement remplacer ces composants de toute façon pour les faire ressembler à ce qu'ils veulent.

Cela signifie que nous allons devoir créer les nôtres en utilisant les classes utilitaires !

Tout d'abord, ajoutons un nouveau bouton. Quelque part sur la page, ajoutez le fragment suivant. Je vais l'ajouter juste en dessous de la première balise de paragraphe (`<p>`) :

```html
<button>Faire la fête avec Slurm !</button>

```

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-unstyled-button.jpg)
_Page HTML avec bouton non stylisé_

Vous remarquerez que, comme tous les autres éléments, il n'est pas stylisé, cependant, si vous essayez de cliquer dessus, vous remarquerez qu'il a toujours les actions de clic. Alors, faisons-le ressembler à un bouton.

Ajoutons les classes suivantes :

```html
<button class="text-white font-bold bg-purple-700 hover:bg-purple-800 py-2 px-4 rounded">
  Faire la fête avec Slurm !
</button>

```

Voici une ventilation de ce qui se passe :

* `text-white` : nous définissons notre couleur de texte en blanc
* `font-bold` : définit le poids du texte en gras (font-weight)
* `bg-purple-700` : définit la couleur de fond du bouton en violet avec une nuance de 700. Le 700 est relatif aux autres couleurs définies comme violettes, vous pouvez trouver ces valeurs sur leur [page de documentation de la palette](https://tailwindcss.com/docs/customizing-colors#default-color-palette)
* `hover:bg-purple-800` : lorsque quelqu'un survole le bouton, définit la couleur de fond en violet nuance 800. Tailwind fournit ces classes d'assistance qui nous permettent de définir facilement des styles interactifs avec des choses comme [hover, focus, et active modifiers](https://tailwindcss.com/course/hover-focus-and-active-styles/)
* `py-2` : définit le remplissage de l'axe y à 2rem
* `px-4` : définit le remplissage de l'axe x à 4rem
* `rounded` : arrondit les coins de l'élément en définissant le rayon de la bordure. Avec tailwind, il définit la valeur du rayon de la bordure à .25rem

Et avec tout cela, nous avons notre bouton !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/html-page-styled-button.jpg)
_Page HTML avec un bouton stylisé_

Vous pouvez appliquer cette méthodologie à tout autre composant que vous souhaitez construire. Bien que ce soit un processus manuel, nous découvrirons comment nous pouvons rendre ce processus plus facile lors de la construction de projets plus dynamiques comme ceux basés sur React.

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-static/commit/09312336dce316a75e8007d6c935133490f16c25)

## Partie 2 : Ajout de Tailwind CSS à une application React

Pour un cas d'utilisation plus réel, nous allons ajouter Tailwind CSS à une application créée avec [Create React App](https://reactjs.org/docs/create-a-new-react-app.html).

Tout d'abord, nous allons passer par les étapes nécessaires pour ajouter tailwind à votre projet en utilisant une nouvelle installation de Create React App, puis nous utiliserons notre contenu de notre dernier exemple pour le recréer dans React.

### Étape 1 : Lancement d'une nouvelle application React

Je ne vais pas détailler cette étape trop. L'essentiel est que nous allons démarrer une nouvelle application React en utilisant Create React App.

Pour commencer, vous pouvez suivre [les instructions](https://reactjs.org/docs/create-a-new-react-app.html) de la documentation officielle de React :

[https://reactjs.org/docs/create-a-new-react-app.html](https://reactjs.org/docs/create-a-new-react-app.html)

Et une fois que vous avez démarré votre serveur de développement, vous devriez maintenant voir une application !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/create-react-app-starting-page.jpg)
_Page de démarrage de Create React App_

Enfin, migrons tout notre ancien contenu vers notre application. Pour ce faire, copiez tout ce qui se trouve à l'intérieur de la balise `<body>` de notre exemple statique et collez-le à l'intérieur de la balise d'enveloppe `<div className="App">` dans le nouveau projet React.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-migrating-content.jpg)
_Migration de code vers l'application React_

Ensuite, changez tous les attributs `class="` du contenu que nous avons collé en `className="` afin qu'il utilise les attributs React appropriés :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-fixing-class-attribute.jpg)
_Correction de l'attribut de classe dans le contenu_

Et enfin, remplacez le className `App` sur notre balise d'enveloppe `<div>` par les classes que nous avons utilisées sur notre `<body>` statique.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/code-wrapper-styles.jpg)
_Ajout de styles d'enveloppe à l'application_

Une fois que vous avez sauvegardé vos modifications et redémarré votre serveur, cela devrait sembler trompeusement correct.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-app-basic-content.jpg)
_Application React avec contenu de base_

React inclut certains styles de base lui-même, donc bien que cela semble correct, nous n'utilisons pas encore Tailwind. Alors, commençons par l'installer !

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-dynamic/commit/57993883c77739f71072bcc02ed2398543efc2fd)

### Étape 2 : Installation de Tailwind dans votre application React

Il y a quelques étapes que nous devons suivre pour faire fonctionner Tailwind sur notre application. Assurez-vous de suivre ces étapes attentivement pour garantir une configuration correcte.

Tout d'abord, ajoutons nos dépendances :

```
yarn add tailwindcss postcss-cli autoprefixer
# ou
npm install tailwindcss postcss-cli autoprefixer

```

[Selon la documentation de Tailwind](https://tailwindcss.com/docs/installation#4-process-your-css-with-tailwind), nous devons être en mesure de traiter nos styles afin qu'ils puissent être correctement ajoutés à notre pipeline. Donc, dans ce qui précède, nous ajoutons :

* [tailwindcss](https://tailwindcss.com/) : le package principal de Tailwind
* [postcss-cli](https://github.com/postcss/postcss) : Create React App utilise déjà postcss, mais nous devons configurer Tailwind pour qu'il fasse partie de ce processus de construction et exécute son propre traitement
* [autoprefixer](https://github.com/postcss/autoprefixer) : Tailwind n'inclut pas les préfixes de fournisseurs, donc nous voulons ajouter autoprefixer pour gérer cela pour nous. Cela s'exécute dans le cadre de notre configuration postcss

Nous allons également ajouter deux dépendances de développement qui facilitent le travail avec notre code :

```
yarn add concurrently chokidar-cli -D
# ou
npm install concurrently chokidar-cli --save-dev

```

* [concurrently](https://github.com/kimmobrunfeldt/concurrently) : un package qui nous permet de configurer la possibilité d'exécuter plusieurs commandes à la fois. Cela est utile puisque nous devons surveiller à la fois les styles et l'application React elle-même.
* [chokidar-cli](https://github.com/kimmobrunfeldt/chokidar-cli) : nous permet de surveiller les fichiers et d'exécuter une commande lorsqu'ils sont modifiés. Nous utiliserons cela pour surveiller notre fichier CSS et exécuter le processus de construction du CSS lors des modifications

Ensuite, configurons postcss, alors créez un nouveau fichier à la racine de votre projet appelé `postcss.config.js` et incluez ce qui suit :

```js
// À l'intérieur de postcss.config.js
module.exports = {
    plugins: [
        require('tailwindcss'),
        require('autoprefixer')
    ],
};

```

Cela ajoutera les plugins Tailwindcss et Autoprefixer à notre configuration postcss.

Avec notre configuration, nous devons l'inclure dans le cadre des processus de construction et de surveillance. À l'intérieur de `package.json`, ajoutez les définitions suivantes à votre propriété `scripts` :

```json
"build:css": "tailwind build src/App.css -o src/index.css",
"watch:css": "chokidar 'src/App.css' -c 'npm run build:css'",

```

De plus, modifiez les scripts `start` et `build` pour inclure désormais ces commandes :

```json
"start": "concurrently -n Tailwind,React 'npm run watch:css' 'react-scripts start'",
"build": "npm run build:css && react-scripts build",

```

Avec notre configuration prête à l'emploi, essayons de restaurer nos styles là où ils étaient lorsque nous avons quitté l'exemple statique.

À l'intérieur du fichier `App.css`, remplacez tout le contenu par :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

```

Cela va importer les styles de base de Tailwind, les composants et les classes utilitaires qui permettent à Tailwind de fonctionner comme vous vous y attendez.

Nous pouvons également supprimer l'importation `App.css` de notre fichier `App.js` car il est maintenant injecté directement dans notre fichier `index.css`. Alors, supprimez cette ligne :

```js
import './App.css';

```

Une fois que vous avez terminé, vous pouvez redémarrer votre serveur de développement ! Si celui-ci était déjà démarré, assurez-vous de le redémarrer pour que toutes les modifications de configuration prennent effet.

Et maintenant, la page devrait avoir exactement le même aspect que dans notre exemple statique !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-app-with-styled-content.jpg)
_Application React avec contenu stylisé_

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-dynamic/commit/5f50cc218ef58f469dad7f09bdad31f36b58a896)

### Étape 3 : Création d'une nouvelle classe de composant bouton avec Tailwind

Tailwind ne fournit pas de classes de composants pré-cuits, mais il facilite leur création !

Nous allons utiliser notre bouton que nous avons déjà créé comme exemple pour créer un nouveau composant. Nous allons créer une nouvelle classe `btn` ainsi qu'un modificateur de couleur `btn-purple` pour y parvenir.

La première chose que nous allons vouloir faire est d'ouvrir notre fichier App.css où nous allons créer notre nouvelle classe. À l'intérieur de ce fichier, ajoutons :

```css
.btn {
  @apply font-bold py-2 px-4 rounded;
}

```

Si vous vous souvenez de notre HTML, nous incluons déjà ces mêmes classes à notre élément `<button>`. Tailwind nous permet d'"appliquer" ou d'inclure les styles qui composent ces classes utilitaires à une autre classe, dans ce cas, la classe `.btn`.

Et maintenant que nous créons cette classe, appliquons-la à notre bouton :

```html
<button className="btn text-white bg-purple-700 hover:bg-purple-800">
  Faire la fête avec Slurm !
</button>

```

Et si nous ouvrons notre page, nous pouvons voir que notre bouton a toujours le même aspect. Si nous inspectons l'élément, nous pouvons voir notre nouvelle classe `.btn` générée avec ces styles.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-tailwind-button-class.jpg)
_Classe .btn dans une application React avec Tailwind_

Ensuite, créons un modificateur de couleur. Similaire à ce que nous venons de faire, nous allons ajouter les règles suivantes :

```css
.btn-purple {
  @apply bg-purple-700 text-white;
}

.btn-purple:hover {
  @apply bg-purple-800;
}

```

Ici, nous ajoutons notre couleur de fond et notre couleur de texte à notre classe de bouton. Nous appliquons également une couleur de bouton plus foncée lorsque quelqu'un survole le bouton.

Nous voudrons également mettre à jour notre bouton HTML pour inclure notre nouvelle classe et supprimer celles que nous venons d'appliquer :

```html
<button className="btn btn-purple">
  Faire la fête avec Slurm !
</button>

```

Et avec ce changement, nous pouvons toujours voir que rien n'a changé et nous avons notre nouvelle classe de bouton !

![Image](https://www.freecodecamp.org/news/content/images/2020/05/react-tailwind-styled-button.jpg)
_Bouton stylisé dans React avec Tailwind_

[Suivez le commit !](https://github.com/colbyfayock/my-tailwind-dynamic/commit/7a76e8a4583b0a4c523ea902d73e889c7b86f437)

## Application de ces concepts à plus de composants

À travers ce guide, nous avons appris comment créer une nouvelle classe de composant en utilisant la directive apply de Tailwind. Cela nous a permis de créer des classes réutilisables qui représentent un composant comme un bouton.

Nous pouvons appliquer cela à n'importe quel nombre de composants dans notre système de design. Par exemple, si nous voulions toujours afficher nos listes de la manière dont nous les avons configurées ici, nous pourrions créer une classe `.list-ul` qui représenterait une liste non ordonnée avec les utilitaires Tailwind `list-disc list-inside my-5 pl-2` appliqués.

## Quels conseils et astuces aimez-vous utiliser avec Tailwind ?

Partagez-les avec moi sur [Twitter](https://twitter.com/colbyfayock) !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f3fb Inscription à ma newsletter</a>
    </li>
  </ul>
</div>