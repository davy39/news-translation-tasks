---
title: Comment créer un lecteur vidéo HTML5 personnalisé en utilisant TailwindCSS
  et JavaScript
subtitle: ''
author: Franklin Okolie
co_authors: []
series: null
date: '2024-02-13T15:14:21.000Z'
originalURL: https://freecodecamp.org/news/build-a-custom-video-player-using-javascript-and-tailwind-css
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/how-to-build-a-custom-video-player-using-tailwindcss-and-javascript.png
tags:
- name: JavaScript
  slug: javascript
- name: tailwind
  slug: tailwind
seo_title: Comment créer un lecteur vidéo HTML5 personnalisé en utilisant TailwindCSS
  et JavaScript
seo_desc: HTML5 comes equipped with a native video player. It's shipped with a simple
  user interface, functionality, and some basic controls in the browser. And while
  the functionality of the default video player via the browser works perfectly, the
  user inter...
---

HTML5 est équipé d'un lecteur vidéo natif. Il est livré avec une interface utilisateur simple, une fonctionnalité et quelques contrôles de base dans le navigateur. Et bien que la fonctionnalité du lecteur vidéo par défaut via le navigateur fonctionne parfaitement, l'interface utilisateur n'est pas si belle et élégante, et elle n'est tout simplement pas généralement esthétiquement agréable. 

Pour cette raison, la plupart des applications et plateformes web modernes comme Udemy, Netflix, YouTube et Amazon Prime ne livrent pas le lecteur vidéo HTML5 intégré par défaut à leurs utilisateurs. Au lieu de cela, ils construisent leurs propres versions personnalisées avec une interface utilisateur élégante pour rendre leurs plateformes plus attrayantes et conviviales.

Si vous avez déjà été curieux de savoir comment ces entreprises et plateformes web sont capables de réaliser un tel exploit, alors cet article est pour vous.

Vous obtiendrez une expérience pratique en suivant un guide étape par étape qui vous apprend comment vous pouvez construire et personnaliser votre propre lecteur vidéo HTML5. Vous apprendrez comment personnaliser l'interface utilisateur, étendre la fonctionnalité et construire vos propres contrôles et fonctionnalités personnalisés fantastiques.

Vous apprendrez également comment construire tout cela en utilisant rien d'autre que l'API Video native fournie par JavaScript dans le navigateur – aucune bibliothèque ou outil externe requis.

## Prérequis

* Connaissance fondamentale de HTML5 et CSS
* Connaissance fondamentale de Tailwind CSS
* Connaissance fondamentale de JavaScript (ES6)
* Un éditeur de code de votre choix
* Un navigateur qui supporte les fonctionnalités modernes de JavaScript (par exemple Chrome ou Mozilla Firefox)

## Voici ce que nous allons couvrir:

1. [Getting Started](#heading-installation)
2. [Comment configurer l'environnement de développement](#heading-comment-configurer-lenvironnement-de-developpement)
3. [Comment construire une interface utilisateur personnalisée en utilisant Tailwind CSS](#heading-comment-construire-une-interface-utilisateur-personnalisee-en-utilisant-tailwind-css)
4. [Comment implémenter la fonctionnalité de lecture et de pause](#heading-comment-implementer-la-fonctionnalite-de-lecture-et-de-pause)
5. [Comment implémenter la fonctionnalité de rembobinage et d'avance rapide](#heading-comment-implementer-la-fonctionnalite-de-rembobinage-et-davance-rapide)
6. [Comment implémenter la fonctionnalité de muet et de son](#heading-comment-implementer-la-fonctionnalite-de-muet-et-de-son)
7. [Comment mettre à jour la barre de progression relative au temps de la vidéo](#heading-comment-mettre-a-jour-la-barre-de-progression-relative-au-temps-de-la-video)
8. [Comment implémenter la fonctionnalité de recherche](#heading-comment-implementer-la-fonctionnalite-de-recherche)
9. [Comment implémenter les navigations clavier pour l'accessibilité](#heading-comment-ajouter-la-navigation-clavier-pour-laccessibilite)
10. [Où aller à partir d'ici](#heading-ou-aller-a-partir-dici)
11. [Conclusion](#heading-conclusion)

## Getting Started

Dans cet article, nous utiliserons Tailwind CSS comme outil de style pour construire l'interface utilisateur du lecteur vidéo personnalisé. Nous utiliserons également JavaScript pour construire la fonctionnalité des contrôles.

Notez que l'utilisation de Tailwind CSS est facultative, car tout outil de style suffira ici comme SCSS, CSS, styled-components, etc. – c'est totalement à vous.

J'ai divisé ce tutoriel en différentes sections, chacune abordant un aspect spécifique de la fonctionnalité du lecteur vidéo personnalisé. Chaque nouvelle section s'appuiera sur les précédentes pour compléter le lecteur. À la fin de l'article, vous aurez un lecteur vidéo HTML5 personnalisé entièrement fonctionnel.

Dans ce tutoriel, nous nous concentrerons sur des fonctionnalités spécifiques du lecteur vidéo. Ces fonctionnalités offriront des opportunités et des idées pour construire des fonctionnalités supplémentaires. Les fonctionnalités que nous allons couvrir sont:

* Lecture et pause
* Rembobinage et avance rapide
* Muet et son
* Recherche vidéo
* Navigations clavier (utilisant la barre d'espace pour la lecture et la pause, et les touches fléchées pour le rembobinage et l'avance rapide).

Nous n'aborderons pas le design réactif ici, car nous ne nous concentrerons pas sur la rendre le lecteur vidéo réactif pour les mobiles. Cette omission devrait présenter un défi et une opportunité d'apprentissage pour vous.

Maintenant, plongeons dans la configuration de notre environnement de développement afin que nous puissions commencer à construire.

## Comment configurer l'environnement de développement

La première étape consiste à configurer un environnement de développement efficace pour garantir un flux de travail fluide. Nous utiliserons [Vite](https://vitejs.dev/) à cette fin. 

Avant de passer à la partie suivante de cette section, assurez-vous d'avoir [NodeJS](https://nodejs.org/en) et [NPM](https://www.npmjs.com/) ou [Yarn](https://yarnpkg.com/) installés sur votre ordinateur, car ils sont nécessaires pour installer des outils et configurer votre environnement de développement de manière transparente.

### Comment configurer le projet avec Vite

Pour créer un projet dans Vite, ouvrez votre terminal et tapez la commande suivante:

```bash
yarn create vite
```

Vite vous guidera dans la configuration et la sélection des outils appropriés pour votre environnement de développement. 

La première étape consiste à choisir un nom de projet – vous avez la liberté de choisir le nom que vous préférez. Dans cet article, j'utiliserai "html5-video-player" comme nom de projet.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-81.png)
_Sortie du terminal après avoir exécuté la commande 'yarn create vite'_

L'étape suivante consiste à sélectionner le framework du projet. Ce projet sera écrit en JavaScript pur, donc choisissez "Vanilla" puis sélectionnez "JavaScript" à l'invite suivante.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-82.png)
_Sortie du terminal après avoir saisi un nom de projet, demandant de sélectionner un framework pour le projet_

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-83.png)
_Sortie du terminal après avoir sélectionné le framework 'Vanilla'_

Maintenant, Vite a configuré avec succès votre environnement en utilisant les outils sélectionnés. Il est temps d'installer les dépendances nécessaires pour que Vite fonctionne correctement. Suivez les instructions fournies par Vite dans le CLI.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-84.png)
_Terminal affichant un message de succès sur la configuration de l'environnement_

Si vous avez nommé votre projet comme le mien, exécutez la commande ci-dessous exactement comme elle est. Si vous avez choisi un nom différent, substituez simplement mon nom de projet par le vôtre et procédez de la même manière.

```bash
cd html5-video-player
```

Cette commande vous amènera au répertoire du projet où se trouve votre environnement de développement. À partir de là, vous pouvez procéder à l'installation des dépendances.

```bash
yarn
```

Une fois les dépendances installées, passons à l'étape suivante, qui consiste à configurer Tailwind CSS comme notre outil de style. Ce processus est simple, similaire à la façon dont nous avons configuré Vite.

Ouvrez votre terminal et exécutez les commandes suivantes:

```bash
yarn add -D tailwindcss postcss autoprefixer
```

Cela installera Tailwind CSS, notre outil de style, ainsi que PostCSS et Autoprefixer. Ces outils aideront Tailwind CSS à fonctionner efficacement dans votre projet. 

La commande suivante consiste à configurer les fichiers de configuration pour Tailwind CSS et PostCSS.

Ouvrez votre terminal local une fois de plus et tapez la commande suivante:

```bash
npx tailwindcss init
```

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-85.png)
_Création du fichier de configuration Tailwind CSS._

Comme mentionné dans le message de la commande, un fichier nommé `tailwind.config.js` sera généré à la racine du dossier du projet. Ce fichier contiendra votre configuration pour le style, y compris les paramètres pour les polices, les couleurs, les plugins, et plus encore. Pour plus de détails, consultez la [documentation TailwindCSS](https://tailwindcss.com/).

Ouvrez le fichier de configuration Tailwind CSS qui a été généré dans votre éditeur de code et apportez les modifications suivantes:

```js
/** @type {import('tailwindcss').Config} */
export default {
  content: ['./index.html'],
  theme: {
    extend: {},
  },
  plugins: [],
}


```

Ici, nous avons simplement modifié la clé `content` pour spécifier le fichier où TailwindCSS doit lire les classes Tailwind CSS. Ce fichier est le fichier `index.html`, où notre travail principal aura lieu.

Ensuite, vous devrez configurer PostCSS, qui n'a pas de commande de configuration automatisée comme TailwindCSS. Vous créerez donc le fichier de configuration manuellement. Accédez au dossier racine du projet et créez un fichier nommé `postcss.config.js`.

Après avoir créé le fichier `postcss.config.js`, copiez et collez simplement le code fourni dans le fichier.

```js
export default {
  plugins: {
    tailwindcss: {},
    autoprefixer: {},
  },
};
```

Ensuite, configurez votre fichier `style.css` pour utiliser les valeurs par défaut de Tailwind CSS. Cela vous évite la tâche fastidieuse de configurer manuellement les valeurs par défaut de CSS. 

Ouvrez le fichier `style.css` dans votre éditeur de code, supprimez son contenu, puis collez le code suivant dans le fichier:

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

### Supprimer les fichiers et le code inutiles

Les fichiers générés par Vite servent principalement de guides pour ajouter vos propres fichiers et utiliser le bundler efficacement. Vous pouvez donc supprimer la plupart d'entre eux car ils sont inutiles pour ce projet.

Voici les fichiers à supprimer du projet:

1. `counter.js`
2. `javascript.svg`

Une fois que vous avez fait cela, vous pouvez passer à l'étape suivante de cette section, qui consiste à supprimer le code inutile.

Ouvrez le fichier `main.js` situé à la racine du projet, et supprimez tout le code qu'il contient.

Ensuite, accédez au fichier `index.html` et supprimez tout son contenu actuel. Ensuite, copiez et collez le code suivant dans le fichier:

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link rel="stylesheet" href="./style.css" />
    <title>HTML5 Custom Video Player</title>
  </head>
  <body>
    <h1 class="text-3xl font-bold underline text-red-800">Hello world!</h1>
    <script type="module" src="/main.js"></script>
  </body>
</html>


```

Et avec cela, vous avez terminé cette partie! Votre environnement de développement est maintenant configuré, prêt pour que vous commenciez à construire votre lecteur vidéo HTML5 personnalisé

Pour confirmer que votre environnement est configuré correctement, vérifiez les éléments suivants:

1. Les fichiers et dossiers du projet doivent ressembler à la structure suivante:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-108.png)
_Configuration du projet terminée: Visual Studio Code affichant la structure du projet._

2.  Ouvrez votre terminal et exécutez la commande suivante:

```bash
yarn dev
```

Cela créera un serveur de développement où votre page web sera hébergée. Ouvrez l'URL fournie par Vite.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-109.png)
_Lancement du serveur de développement Vite avec la commande 'yarn dev'._

En ouvrant le lien `http://localhost:5173/`, vous devriez voir ceci:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-110.png)
_L'interface utilisateur initiale affichée après l'exécution de la commande 'yarn dev'._

Félicitations! Vous avez réussi à compléter cette section sur la configuration de votre environnement de développement, ce qui nous permettra de travailler efficacement tout en construisant notre lecteur vidéo HTML5 personnalisé.

**Dépannage:** Si vous trouvez que votre configuration ne fonctionne pas comme prévu, ne vous inquiétez pas. Supprimez simplement le dossier du projet et répétez le processus. Vous avez peut-être manqué une étape ou certains outils n'ont peut-être pas été installés correctement. De plus, vérifiez vos fichiers de configuration Tailwind CSS et PostCSS pour vous assurer qu'ils contiennent le code correct comme montré ci-dessus.

## Comment construire une interface utilisateur personnalisée en utilisant Tailwind CSS

Cette section couvre tous les styles nécessaires pour construire l'interface utilisateur du lecteur vidéo HTML5 personnalisé. Nous allons suivre un guide étape par étape du processus.

Tout d'abord, copiez et collez la balise de lien suivante dans l'en-tête de votre HTML, au-dessus du lien vers la feuille de style:

```css
<link
  href="https://fonts.googleapis.com/icon?family=Material+Icons"
  rel="stylesheet"
/>
```

Cela nous permet d'utiliser les [icônes CSS Materialize](https://materializecss.com/icons.html), qui sont essentielles pour styliser nos boutons dans l'interface utilisateur. 

Ensuite, concentrons-nous sur le style de l'élément vidéo dans notre balisage. Remplacez simplement l'élément `body` par le code fourni ci-dessous:

```html
<body class="bg-indigo-950 p-10">
  <div
    id="container"
    class="w-4/5 h-4/5 mx-auto rounded-lg overflow-hidden relative group"
  >
    <!-- VIDEO -->
    <figure>
      <video class="w-full">
        <source src="/your-video.mp4" />
      </video>
    </figure>
  </div>
  <script type="module" src="/main.js"></script>
</body>


```

Le code fourni inclut le balisage et le style pour l'élément vidéo, ainsi qu'une div externe servant de conteneur pour toute l'interface utilisateur du lecteur vidéo. L'élément vidéo est imbriqué dans un élément figure.

Pour l'élément `source`, spécifiez le chemin vers la vidéo que vous souhaitez lire. Vous pouvez trouver des vidéos en ligne, les télécharger et les ajouter au répertoire "public" dans le dossier du projet. Ensuite, liez l'attribut `src` de l'élément `source` au fichier vidéo. Vous pouvez trouver des vidéos téléchargeables gratuites [ici](https://www.pexels.com/search/videos/online/).

Ensuite, stylisons les contrôles en utilisant les [icônes Materialize CSS](https://materializecss.com/icons.html) que vous avez liées dans votre HTML. Placez le code suivant sous l'élément `figure` à l'intérieur de l'élément body.

```html
<!-- CONTROLS -->
<div
  id="controls"
  class="opacity-0 p-5 absolute bottom-0 left-0 w-full transition-opacity duration-300 ease-linear group-hover:opacity-100"
>
  <!-- PROGRESS BAR -->
  <div id="progress-bar" class="h-1 w-full bg-white cursor-pointer mb-4">
    <div
      id="progress-indicator"
      class="h-full w-9 bg-indigo-800 transition-all duration-500 ease-in-out"
    ></div>
  </div>
  <div class="flex items-center justify-between">
    <div class="flex items-center justify-between">
      <!-- REWIND BUTTON -->
      <button
        id="rewind"
        class="transition-all duration-100 ease-linear hover:scale-125"
      >
        <i class="material-icons text-white text-3xl w-12">replay_10 </i>
      </button>

      <!-- PLAY BUTTON -->
      <button
        id="play-pause"
        class="transition-all duration-100 ease-linear hover:scale-125"
      >
        <i class="material-icons text-white text-5xl inline-block w-12"
          >play_arrow</i
        >
      </button>

      <!-- FAST FORWARD BUTTON -->
      <button
        id="fast-forward"
        class="transition-all duration-100 ease-linear hover:scale-125"
      >
        <i class="material-icons text-white text-3xl w-12">forward_10 </i>
      </button>
    </div>

    <div>
      <!-- VOLUME BUTTON -->
      <button
        id="volume"
        class="transition-all duration-100 ease-linear hover:scale-125"
      >
        <i class="material-icons text-white text-3xl">volume_up</i>
      </button>
    </div>
  </div>
</div>

```

Ce segment de code définit la disposition et le comportement des contrôles pour un lecteur vidéo. Il commence par configurer une div conteneur (`<div id="controls">`) qui contient tous les éléments de contrôle. Le conteneur est initialement invisible (`opacity-0`) et devient visible avec une transition fluide (`transition-opacity duration-300 ease-linear`) lorsque l'utilisateur passe la souris dessus (`group-hover:opacity-100`).

À l'intérieur du conteneur, il y a une barre de progression (`<div id="progress-bar">`) pour suivre la progression de la vidéo. Elle se compose d'une barre de fond blanche (`bg-white`) avec un indicateur mobile (`<div id="progress-indicator">`) coloré en indigo (`bg-indigo-800`). La barre de progression est réactive et permet aux utilisateurs de rechercher différentes parties de la vidéo.

Sous la barre de progression se trouvent les boutons de contrôle pour diverses fonctions. Les boutons de rembobinage, de lecture/pause et d'avance rapide sont regroupés dans un conteneur flex (`<div class="flex items-center justify-between">`). Chaque bouton (`<button>`) est stylisé pour s'agrandir légèrement (`hover:scale-125`) lorsque la souris passe dessus.

* Le bouton de rembobinage (`<button id="rewind">`) contient une icône (`<i class="material-icons text-white text-3xl w-12">replay_10</i>`) indiquant un rembobinage de dix secondes.
* Le bouton de lecture/pause (`<button id="play-pause">`) contient une icône (`<i class="material-icons text-white text-5xl w-12">play_arrow</i>`) basculant entre les états de lecture et de pause.
* Le bouton d'avance rapide (`<button id="fast-forward">`) contient une icône (`<i class="material-icons text-white text-3xl w-12">forward_10</i>`) indiquant une avance rapide de dix secondes.

Séparément, il y a un bouton de volume (`<button id="volume">`) situé à droite des boutons de contrôle. Il contient une icône de volume (`<i class="material-icons text-white text-3xl w-12">volume_up</i>`).

Dans l'ensemble, ce segment de code combine HTML et les classes Tailwind CSS pour créer un ensemble de contrôles fonctionnel et visuellement attrayant pour un lecteur vidéo.

La dernière pièce du puzzle consiste à désactiver la fonctionnalité par défaut du navigateur, et nous ne voudrions pas que notre lecteur vidéo HTML5 personnalisé entre en conflit avec ou soit remplacé par le style par défaut fourni par les navigateurs.

Copiez et collez le code suivant dans votre fichier `style.css`, directement sous les directives Tailwind CSS:

```css
@layer base {
  video::-webkit-media-controls {
    display: none;
  }

  video::-webkit-media-controls-play-button {
    display: none;
  }

  video::-webkit-media-controls-volume-slider {
    display: none;
  }

  video::-webkit-media-controls-mute-button {
    display: none;
  }

  video::-webkit-media-controls-timeline {
    display: none;
  }

  video::-webkit-media-controls-current-time-display {
    display: none;
  }
}
```

Ce morceau de code est utilisé pour personnaliser l'apparence et le comportement des contrôles multimédias par défaut fournis par le moteur de navigateur WebKit (communément utilisé dans des navigateurs comme Safari et certaines versions de Google Chrome) pour l'élément `<video>`.

Chaque règle CSS dans le bloc `@layer base` cible des parties spécifiques des contrôles multimédias par défaut et les masque en définissant leur propriété `display` sur `none`. Voici une ventilation de chaque règle:

1. `video::-webkit-media-controls`: Cette règle cible l'ensemble des contrôles multimédias pour l'élément `<video>` et les masque complètement. En masquant les contrôles, vous pouvez implémenter vos propres contrôles personnalisés en utilisant JavaScript et CSS, offrant une expérience utilisateur plus adaptée et cohérente sur différents navigateurs.
2. `video::-webkit-media-controls-play-button`: Cette règle cible le bouton de lecture dans les contrôles multimédias par défaut et le masque. Nous pourrions vouloir masquer le bouton de lecture si nous utilisons un design de bouton de lecture personnalisé ou si nous gérons le contrôle de la lecture de manière programmatique.
3. `video::-webkit-media-controls-volume-slider`: Cette règle cible le curseur de volume dans les contrôles multimédias par défaut et le masque. De manière similaire à masquer le bouton de lecture, vous pourriez choisir de masquer le curseur de volume si vous implémentez votre propre interface utilisateur de contrôle de volume.
4. `video::-webkit-media-controls-mute-button`: Cette règle cible le bouton de mise en sourdine dans les contrôles multimédias par défaut et le masque. Si vous avez un bouton de mise en sourdine/réactivation du son personnalisé ou si vous souhaitez gérer la mise en sourdine audio de manière programmatique, vous pouvez masquer le bouton de mise en sourdine par défaut.
5. `video::-webkit-media-controls-timeline`: Cette règle cible la timeline (barre de progression) dans les contrôles multimédias par défaut et la masque. En masquant la timeline, vous pouvez implémenter votre propre barre de progression avec un style personnalisé et des fonctionnalités supplémentaires.
6. `video::-webkit-media-controls-current-time-display`: Cette règle cible l'affichage du temps actuel dans les contrôles multimédias par défaut et le masque. Si vous implémentez une interface utilisateur personnalisée pour afficher le temps de lecture actuel, vous pouvez masquer l'affichage par défaut.

Dans l'ensemble, ce code permet une personnalisation complète des contrôles multimédias par défaut fournis par les navigateurs WebKit, vous permettant de créer une expérience utilisateur unique et adaptée pour la lecture vidéo sur vos sites web.

Vérifiez votre URL localhost pour voir une interface utilisateur personnalisée affichée comme ceci:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-114.png)
_Interface utilisateur du lecteur vidéo personnalisé sans survol de la souris, contrôles masqués._

Cependant, lors du survol, les contrôles s'estomperont et l'interface utilisateur sera affichée comme ceci:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/image-113.png)
_Interface utilisateur du lecteur vidéo personnalisé avec contrôles visibles lors du survol de la souris._

Et voilà! Vous avez réussi à construire un lecteur vidéo HTML5 personnalisé. Maintenant, il est temps de lui donner vie en utilisant JavaScript pour développer les contrôles et la fonctionnalité, que nous aborderons dans les sections à venir.

## Comment implémenter la fonctionnalité de lecture et de pause

Pour implémenter la fonctionnalité de lecture et de pause sur le lecteur vidéo HTML5 personnalisé, vous commençerez par sélectionner les boutons de lecture et de pause en utilisant leurs ID respectifs à partir du balisage. Vous pouvez également sélectionner l'élément vidéo. Ensuite, vous contrôlerez la lecture de manière programmatique en utilisant l'API Video fournie par JavaScript dans le navigateur. Commençons.

```js
"use strict";

const playNpauseBtn = document.querySelector("#play-pause");
const video = document.querySelector("video");
```

À partir du code ci-dessus:

* `"use strict";` garantit que JavaScript s'exécute en mode strict, capturant les erreurs de codage courantes.
* `const playNpauseBtn = document.querySelector("#play-pause");` sélectionne le bouton de lecture/pause à partir du HTML en utilisant son ID.
* `const video = document.querySelector("video");` sélectionne l'élément vidéo à partir du HTML.

Ensuite, créons deux fonctions:

1. `playNpauseFn`: Cette fonction gérera la lecture et la pause de la vidéo.
2. `updatePlayNPauseIcon`: Cette fonction mettra à jour les icônes de lecture et de pause en fonction de l'état actuel de la vidéo. Par exemple, si la vidéo est en lecture, elle affichera l'icône de pause, et vice versa.

Maintenant, examinons comment cela fonctionnera dans le code suivant.

```js
function playNpauseFn() {
  video.paused ? video.play() : video.pause();
}

function updatePlayNPauseIcon() {
  const icon = playNpauseBtn.querySelector("i");
  icon.textContent = "";

  icon.textContent = video.paused ? "play_arrow" : "paused";
}
```

Comprenons ce qui se passe. Commençons par la fonction `playNpauseFn`, lorsqu'elle est appelée, elle vérifie l'état actuel de la vidéo en utilisant la méthode `paused` disponible dans l'API Video. Si la vidéo est en pause, elle lit la vidéo. Sinon, elle met la vidéo en pause. Cela est accompli en utilisant l'opérateur ternaire en JavaScript.

Alternativement, vous pouvez réécrire cela en utilisant l'instruction if/else, comme montré ci-dessous:

```js
function playNpauseFn() {
  if (video.paused) {
    video.play();
  } else {
    video.paused();
  }
}
```

L'exemple de code ci-dessus accomplit la même tâche que la version précédente – l'une ou l'autre fonctionnera.

Maintenant, passons à la deuxième fonction, `updatePlayNPauseIcon`. Cette fonction met à jour les icônes de lecture et de pause en fonction de l'état actuel de la vidéo. Examinons comment elle est implémentée.

Consultez le style de l'icône ci-dessous:

```html
<button
  id="play-pause"
  class="transition-all duration-100 ease-linear hover:scale-125"
>
  <i class="material-icons text-white text-5xl inline-block w-12">play_arrow</i>
</button>

```

Ce code crée un bouton avec l'ID "play-pause" qui contient une icône spécifiée par la balise `<i>`. Materialize CSS utilise le texte "play_arrow" à l'intérieur de la balise `<i>` pour afficher l'icône correspondante. Si vous changez le texte à l'intérieur de `<i>`, Materialize CSS met à jour l'icône en conséquence.

Maintenant, concentrons-nous sur la fonction responsable de la mise à jour de l'icône. Regardez-la ci-dessous en isolation:

```js
function updatePlayNPauseIcon() {
  const icon = playNpauseBtn.querySelector("i");
  icon.textContent = "";

  icon.textContent = video.paused ? "play_arrow" : "paused";
}
```

Cette fonction, `updatePlayNPauseIcon()`, est responsable de la mise à jour de l'icône de lecture/pause en fonction de l'état actuel de la vidéo.

1. Elle sélectionne d'abord l'élément icône à l'intérieur du bouton de lecture/pause.
2. Ensuite, elle efface tout contenu textuel existant dans l'icône.
3. Enfin, elle définit le contenu textuel de l'icône sur "play_arrow" si la vidéo est en pause, ou "paused" si la vidéo est actuellement en lecture. Cela change dynamiquement l'icône affichée sur le bouton pour refléter l'état actuel de la lecture.

**Note:** La façon dont vous mettez à jour les icônes de manière programmatique peut varier en fonction du service d'icônes et de son API. Cette implémentation particulière est spécifique aux icônes Materialize CSS.

Ensuite, connectons ces fonctions aux événements qui les déclenchent. Voyons comment cela fonctionne ci-dessous:

```js
video.addEventListener("play", updatePlayNPauseIcon);
video.addEventListener('click', playNpauseFn)
video.addEventListener("pause", updatePlayNPauseIcon);
playNpauseBtn.addEventListener("click", playNpauseFn);
```

Dans ce code:

* `video.addEventListener("play", updatePlayNPauseIcon);`: Cette ligne ajoute un écouteur d'événement à l'élément vidéo, écoutant spécifiquement l'événement "play". Lorsque la vidéo commence à jouer, elle déclenche la fonction `updatePlayNPauseIcon`, mettant à jour l'icône de lecture/pause en conséquence.
* `video.addEventListener('click', playNpauseFn)`: Cette ligne ajoute un écouteur d'événement à l'élément vidéo pour l'événement "click". Lorsque la vidéo est cliquée, elle déclenche la fonction `playNpauseFn`, qui joue ou met en pause la vidéo.
* `video.addEventListener("pause", updatePlayNPauseIcon);`: Cette ligne ajoute un écouteur d'événement à l'élément vidéo, écoutant l'événement "pause". Lorsque la vidéo est mise en pause, elle déclenche la fonction `updatePlayNPauseIcon` pour mettre à jour l'icône de lecture/pause.
* `playNpauseBtn.addEventListener("click", playNpauseFn);`: Cette ligne ajoute un écouteur d'événement à l'élément bouton de lecture/pause. Lorsque le bouton est cliqué, il déclenche la fonction `playNpauseFn`, qui joue ou met en pause la vidéo.

Nous avons quatre écouteurs d'événements sur les deux éléments sélectionnés. Décomposons ce qui se passe:

* L'élément vidéo écoute l'événement "play". Lorsque la vidéo commence à jouer, il déclenche `updatePlayNPauseIcon`, mettant à jour l'icône en fonction de l'état actuel de la vidéo.
* L'élément vidéo écoute également un événement de clic. Lorsqu'il est cliqué, il déclenche `playNpauseFn`, qui bascule entre la lecture et la pause de la vidéo.
* De plus, l'élément vidéo écoute l'événement "pause". Lorsque la vidéo est mise en pause, il déclenche `playNpauseFn`, basculant l'état de lecture de la vidéo.
* L'élément bouton de lecture/pause écoute également un événement de clic. Lorsqu'il est cliqué, il déclenche `playNpauseFn`, basculant entre la lecture et la pause de la vidéo.

Cela conclut cette section. Vous pouvez maintenant essayer la fonctionnalité de lecture et de pause. La vidéo devrait mettre en pause et jouer efficacement, avec les icônes se mettant à jour correctement.

Pour l'instant, votre lecteur vidéo personnalisé devrait faire ceci:

![Image](https://www.freecodecamp.org/news/content/images/2024/02/play-pause.gif)
_Test de la fonctionnalité de lecture et de pause_

Dans la section suivante, nous implémenterons la fonctionnalité de rembobinage et d'avance rapide.

## Comment implémenter la fonctionnalité de rembobinage et d'avance rapide

Maintenant que nous avons implémenté la fonctionnalité de lecture et de pause, les prochaines fonctionnalités à ajouter sont le rembobinage et l'avance rapide. Ces fonctionnalités courantes permettent aux utilisateurs de sauter en avant ou en arrière dans la vidéo d'un nombre défini de secondes. 

Tout d'abord, commençons par sélectionner les boutons correspondants dans le document HTML en utilisant leurs ID et en les stockant dans des variables:

```js
const rewindBtn = document.querySelector("#rewind");
const fastForwardBtn = document.querySelector("#fast-forward");
```

Une fois cela terminé, vous devez construire la fonction responsable de l'implémentation de la fonctionnalité de rembobinage et d'avance rapide. Voici le code:

```js
function rewindNforwardFn(type) {
  video.currentTime += type === "rewind" ? -10 : 10;
}
```

Cette fonction, appelée `rewindNforward`, est responsable du rembobinage ou de l'avance rapide de la vidéo. Voici comment elle fonctionne:

* Elle prend un paramètre appelé `type`, qui indique si vous souhaitez rembobiner ou avancer rapidement.
* Si `type` est "rewind", elle soustrait 10 secondes du temps de lecture actuel de la vidéo (`video.currentTime`).
* Si `type` n'est pas "rewind" (indiquant que vous souhaitez avancer rapidement), elle ajoute 10 secondes au temps de lecture actuel de la vidéo. Cela permet aux utilisateurs de naviguer dans la vidéo en arrière ou en avant par intervalles de 10 secondes, selon la valeur de `type`.

Ensuite, vous devez connecter les écouteurs d'événements sur les boutons pour déclencher la fonction `rewindNforward`.

```js
rewindBtn.addEventListener("click", () => rewindNforwardFn("rewind"));
fastForwardBtn.addEventListener("click", () => rewindNforwardFn("forward"));
```

Ce code ajoute des écouteurs d'événements aux boutons de rembobinage et d'avance rapide. Lorsque le bouton de rembobinage est cliqué, il déclenche la fonction `rewindNforward` avec l'argument "rewind", indiquant que vous souhaitez rembobiner la vidéo. 

De même, lorsque le bouton d'avance rapide est cliqué, il déclenche la fonction `rewindNforward` avec l'argument "forward", indiquant que vous souhaitez avancer rapidement la vidéo.

N'hésitez pas à l'essayer et à observer comment il fonctionne sur l'interface utilisateur (UI).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/rewind-1.gif)
_Test de la fonctionnalité de rembobinage et d'avance rapide_

## Comment implémenter la fonctionnalité de muet et de son

Pour ajouter la fonctionnalité de muet et de son, vous suivrez le même processus que pour les fonctionnalités précédentes.

Vous commençerez par sélectionner le bouton de volume dans le document HTML en utilisant la méthode `querySelector`:

```js
const volumeBtn = document.querySelector("#volume");

```

Ensuite, créez les fonctions responsables de la mise en sourdine et de la réactivation du son de la vidéo, et mettez à jour l'icône en conséquence lorsque l'un de ces événements se produit.

```js
function muteNunmuteFn() {
  video.muted = video.muted ? false : true;
}

function updateVolumeIcon() {
  const icon = volumeBtn.querySelector("i");
  icon.textContent = "";
  icon.textContent = video.muted ? "volume_off" : "volume_up";
}
```

Ce code comprend deux fonctions:

1. `muteNunmuteFn()`: Cette fonction bascule l'état de sourdine de la vidéo. Si la vidéo est actuellement en sourdine, elle la réactive. Sinon, elle met la vidéo en sourdine.
2. `updateVolumeIcon()`: Cette fonction met à jour l'icône de volume affichée sur le bouton de volume. Elle efface tout contenu d'icône existant, puis définit le texte de l'icône sur "volume_off" si la vidéo est en sourdine, et "volume_up" si la vidéo n'est pas en sourdine.

La dernière étape consiste à connecter les fonctions avec des écouteurs d'événements afin qu'elles soient exécutées lorsque l'événement est déclenché. Voici les extraits de code pour cela:

```js
video.addEventListener("volumechange", updateVolumeIcon);
volumeBtn.addEventListener("click", muteNunmuteFn);
```

Ce code configure deux choses:

1. Il ajoute un écouteur d'événement à l'élément vidéo, écoutant l'événement "volumechange". Lorsque cet événement se produit (c'est-à-dire lorsque le volume est modifié), il déclenche la fonction `updateVolumeIcon` pour mettre à jour l'icône de volume en conséquence.
2. Il ajoute un écouteur d'événement au bouton de volume. Lorsque le bouton de volume est cliqué, il déclenche la fonction `muteNunmuteFn`, basculant entre la mise en sourdine et la réactivation du son de la vidéo.

Similaire aux événements `play` et `pause`, la vidéo a également un événement `volumechange` déclenché lorsque le volume ou l'état de sourdine change. Vous configurez la vidéo pour écouter cet événement, donc lorsqu'il se produit, l'écouteur d'événement exécute la fonction pour mettre à jour l'icône de volume en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/volume.gif)
_Test de la fonctionnalité de mise en sourdine et de réactivation du son_

## Comment mettre à jour la barre de progression par rapport au temps de la vidéo

Dans cette section, vous verrez comment mettre à jour la barre de progression à mesure que la vidéo est lue, permettant aux utilisateurs de suivre leur progression dans la vidéo.

La barre de progression ne bouge actuellement pas à mesure que la vidéo est lue et que le temps change. Nous allons corriger cela.

Pour commencer, vous supprimerez le style de largeur fixe pour la barre de progression. Initialement ajouté à des fins de style, il n'est plus nécessaire car vous ajusterez dynamiquement la largeur en utilisant JavaScript. Mettez à jour la classe de `w-9` à `w-0` dans l'élément div avec l'id "progress-indicator".

```html
<!-- PROGRESS BAR -->
<div id="progress-bar" class="h-1 w-full bg-white cursor-pointer mb-4">
  <div
    id="progress-indicator"
    class="h-full w-0 bg-indigo-800 transition-all duration-500 ease-in-out"
  ></div>
</div>

```

Passons à l'implémentation de la mise à jour de la barre de progression, la première étape consiste à sélectionner l'élément indicateur de la barre de progression. La largeur de cet élément augmentera à mesure que le temps de la vidéo progresse. Voici le code pour y parvenir:

```js
const progressIndicator = document.querySelector("#progress-indicator");

```

Une fois l'indicateur de progression sélectionné, votre prochaine tâche est d'implémenter la fonction responsable de sa mise à jour.

```js
function updateProgress() {
  const progressPercentage = (video.currentTime / video.duration) * 100;

  progressIndicator.style.width = `${progressPercentage}%`;
}
```

Dans l'extrait de code ci-dessus, la fonction appelée `updateProgress` calcule le pourcentage de progression de la vidéo en divisant le temps actuel de la vidéo par sa durée totale, puis en multipliant par 100. Ce pourcentage est utilisé pour définir la largeur de l'élément indicateur de progression, représentant visuellement la quantité de vidéo qui a été regardée.

Décomposons la fonction. Dans la première ligne de code, vous calculez le pourcentage du temps actuel de la vidéo par rapport à sa durée totale. Vous faites cela en divisant le temps actuel par la durée totale de la vidéo. Par exemple, si une vidéo dure 30 secondes et que le temps actuel est de 3 secondes, 3 divisé par 30 est égal à 0,1. 

Vous multipliez ensuite ce décimal par 100 pour obtenir le pourcentage. Donc, 0,1 multiplié par 100 est égal à 10. Cela signifie que vous êtes à 10% de la vidéo de 30 secondes. 

Enfin, vous utilisez ce pourcentage pour mettre à jour la largeur de l'indicateur de progression en conséquence.

Ensuite, ajoutons un écouteur d'événement qui déclenche cette fonction. Voir l'extrait de code ci-dessous:

```js
video.addEventListener('timeupdate', updateProgress);
```

Similaire à d'autres événements dans l'API Video, il y en a un autre appelé `timeupdate`. Cet événement est déclenché lorsque le `currentTime` de la vidéo change. Ainsi, à mesure que le temps est mis à jour, la fonction `updateProgress` est automatiquement exécutée chaque fois que l'événement est déclenché, provoquant la mise à jour de l'indicateur de progression en conséquence.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/progress.gif)
_Test de la fonctionnalité de progression du temps_

## Comment implémenter la fonctionnalité de recherche

La fonctionnalité de recherche est un aspect vital des lecteurs vidéo. Bien que le rembobinage et l'avance rapide soient efficaces pour les petits sauts, les utilisateurs souhaitent souvent faire des sauts plus importants vers des parties spécifiques de la vidéo. Cliquer sur rembobiner ou avancer rapidement, qui ne se déplace que par incréments fixes, peut être frustrant pour les utilisateurs. Ainsi, la fonctionnalité de recherche s'avère inestimable dans de tels scénarios.

Commençons par sélectionner l'élément de la barre de progression dans le Document Object Model (DOM).

```js
const progessBar = document.querySelector("#progress-bar");

```

Ayant obtenu la barre de progression à partir du DOM en utilisant son ID, votre prochaine étape consiste à construire la fonction de recherche. Vous pouvez trouver l'implémentation dans l'extrait de code suivant:

```js
function seekingFn(e) {
  const updatedTime = (e.offsetX / progessBar.offsetWidth) * video.duration;

  video.currentTime = updatedTime;
}
```

Décomposons la fonction et comprenons ce qui se passe.

La fonction, `seekingFn`, ajuste le temps de lecture actuel de la vidéo en fonction de la position où l'utilisateur clique sur la barre de progression. Elle calcule le temps mis à jour en divisant le décalage horizontal du clic par rapport à la largeur de la barre de progression par la largeur totale de la barre de progression. Ensuite, elle le multiplie par la durée totale de la vidéo. Enfin, elle définit le temps actuel de la vidéo sur le temps mis à jour calculé.

Ensuite, ajoutez l'écouteur d'événement:

```js
let mouseIsDown = false;

progessBar.addEventListener("mousedown", () => (mouseIsDown = true));
progessBar.addEventListener("mouseup", () => (mouseIsDown = false));
progessBar.addEventListener("click", seekingFn);
progessBar.addEventListener("mousemove", (e) => mouseIsDown && seekingFn);
```

Dans l'extrait de code ci-dessus, le code gère les événements de la souris sur la barre de progression pour la fonctionnalité de recherche:

* `mouseIsDown` est une variable qui suit si le bouton de la souris est enfoncé.
* Lorsque le bouton de la souris est enfoncé (événement `mousedown`), `mouseIsDown` est défini sur vrai.
* Lorsque le bouton de la souris est relâché (événement `mouseup`), `mouseIsDown` est défini sur faux.
* Lorsque la barre de progression est cliquée (événement `click`), la fonction `seekingFn` est déclenchée pour rechercher la position cliquée.
* Lorsque la souris se déplace sur la barre de progression (événement `mousemove`), si `mouseIsDown` est vrai, ce qui signifie que le bouton de la souris est enfoncé, alors la fonction `seekingFn` est déclenchée, permettant la recherche tout en faisant glisser la souris.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/seeking.gif)
_Test de la fonctionnalité de recherche_

## Comment ajouter la navigation clavier pour l'accessibilité

Notre lecteur vidéo prend actuellement en charge les appareils à pointeur comme les souris et les stylets. Mais nous visons à garantir l'accessibilité pour les utilisateurs qui peuvent ne pas avoir ou ne pas pouvoir utiliser de tels appareils. Nous nous efforçons donc de rendre notre lecteur vidéo HTML5 personnalisé utilisable sans avoir besoin d'un appareil à pointeur, en utilisant plutôt les claviers.

### Utilisation de la barre d'espace pour la lecture et la pause 

Commençons par améliorer la fonctionnalité de lecture et de pause. Dans la plupart des lecteurs vidéo, il est courant d'utiliser la barre d'espace du clavier pour basculer entre la lecture et la pause d'une vidéo. C'est la première fonctionnalité de navigation clavier que nous implémenterons.

Voici un extrait de code montrant comment y parvenir:

```js
window.addEventListener("keyup", (e) => {
  if (e.code === "Space") {
    playNpauseFn();
  }
});
```

Ce code écoute lorsque une touche de votre clavier est relâchée, connue sous le nom d'événement "keyup". Si la touche relâchée est la barre d'espace, il déclenche la fonction qui bascule entre la lecture et la pause de la vidéo. Vous allez simplement réutiliser la fonction que vous avez créée précédemment pour cela.

Voici une explication étape par étape du code:

1. **`window.addEventListener("keyup", (e) => { ... })`:**

* Vous ajoutez un écouteur d'événement à l'objet `window`.
* Cet écouteur est déclenché lorsqu'une touche est relâchée (événement `keyup`).

2.  **  `(e) => { ... }`:**

* Il s'agit d'une fonction fléchée qui est exécutée lorsque l'événement `keyup` se produit.
* Le paramètre `e` représente l'objet événement contenant des informations sur l'événement.

3.  **`if (e.code === "Space") { ... }`:**

* Cette condition vérifie si la touche qui a été relâchée est la barre d'espace.
* `e.code` fournit le code de la touche qui a déclenché l'événement.

4.  **`playNpauseFn();`:**

* Si la touche relâchée est la barre d'espace, cette fonction est appelée.
* La fonction `playNpauseFn` est responsable du basculement entre la lecture et la pause de la vidéo.

### Utilisation des touches fléchées pour le rembobinage et l'avance rapide

Vous pouvez utiliser la touche fléchée gauche pour le rembobinage et la touche fléchée droite pour l'avance rapide d'une vidéo, en plus de la barre d'espace pour la lecture et la pause.

En vous basant sur l'extrait de code précédent pour la fonctionnalité de lecture et de pause, vous pouvez incorporer les touches fléchées pour le rembobinage et l'avance rapide de la vidéo.

```js
window.addEventListener("keyup", (e) => {
  if (e.code === "Space") {
    playNpauseFn();
  } else if (e.code === "ArrowLeft") {
    rewindNforwardFn("rewind");
  } else if (e.code === "ArrowRight") {
    rewindNforwardFn("forward");
  } else {
    return;
  }
});
```

Cet extrait de code configure un écouteur d'événement sur l'objet window pour l'événement keyup. Lorsque n'importe quelle touche est relâchée, la fonction de rappel fournie est déclenchée avec un paramètre d'événement. À l'intérieur de la fonction de rappel, il y a des instructions conditionnelles pour vérifier quelle touche a été pressée:

* Si la touche pressée est la barre d'espace ("Space"), la fonction `playNpauseFn` est exécutée, basculant entre la lecture et la pause de la vidéo.
* Si la touche pressée est la touche fléchée gauche ("ArrowLeft"), la fonction `rewindNforwardFn` est appelée avec l'argument "rewind", indiquant que la vidéo doit être rembobinée.
* Si la touche pressée est la touche fléchée droite ("ArrowRight"), la fonction `rewindNforwardFn` est appelée avec l'argument "forward", indiquant que la vidéo doit être avancée rapidement.
* Si la touche pressée n'est pas la barre d'espace, la flèche gauche ou la flèche droite, la fonction retourne sans effectuer aucune action.

### À quoi devrait ressembler votre code maintenant

Nous avons maintenant terminé de construire notre lecteur vidéo HTML5 personnalisé. Félicitations à vous pour avoir appris cela.

Si vous avez rencontré des difficultés ou manqué des étapes en cours de route, ne vous inquiétez pas. Vous pouvez trouver les extraits de code pour chaque fichier principal ci-dessous:

**index.html**

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <link rel="icon" type="image/svg+xml" href="/vite.svg" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <link
      href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet"
    />
    <link rel="stylesheet" href="./style.css" />
    <title>HTML5 Custom Video Player</title>
  </head>
  <body class="bg-indigo-950 p-10">
    <div
      id="container"
      class="w-4/5 h-4/5 mx-auto rounded-lg overflow-hidden relative group"
    >
      <!-- VIDEO -->
      <figure>
        <video class="w-full">
          <source src="/oceans.mp4" />
        </video>
      </figure>

      <!-- CONTROLS -->
      <div
        id="controls"
        class="opacity-0 p-5 absolute bottom-0 left-0 w-full transition-opacity duration-300 ease-linear group-hover:opacity-100"
      >
        <!-- PROGRESS BAR -->
        <div id="progress-bar" class="h-1 w-full bg-white cursor-pointer mb-4">
          <div
            id="progress-indicator"
            class="h-full w-0 bg-indigo-800 transition-all duration-500 ease-in-out"
          ></div>
        </div>
        <div class="flex items-center justify-between">
          <div class="flex items-center justify-between">
            <!-- REWIND BUTTON -->
            <button
              id="rewind"
              class="transition-all duration-100 ease-linear hover:scale-125"
            >
              <i class="material-icons text-white text-3xl w-12">replay_10 </i>
            </button>

            <!-- PLAY BUTTON -->
            <button
              id="play-pause"
              class="transition-all duration-100 ease-linear hover:scale-125"
            >
              <i class="material-icons text-white text-5xl inline-block w-12"
                >play_arrow</i
              >
            </button>

            <!-- FAST FORWARD BUTTON -->
            <button
              id="fast-forward"
              class="transition-all duration-100 ease-linear hover:scale-125"
            >
              <i class="material-icons text-white text-3xl w-12">forward_10 </i>
            </button>
          </div>

          <div>
            <!-- VOLUME BUTTON -->
            <button
              id="volume"
              class="transition-all duration-100 ease-linear hover:scale-125"
            >
              <i class="material-icons text-white text-3xl">volume_up</i>
            </button>
          </div>
        </div>
      </div>
    </div>
    <script type="module" src="/main.js"></script>
  </body>
</html>

```

**style.css**

```css
@tailwind base;
@tailwind components;
@tailwind utilities;

@layer base {
  video::-webkit-media-controls {
    display: none;
  }

  video::-webkit-media-controls-play-button {
    display: none;
  }

  video::-webkit-media-controls-volume-slider {
    display: none;
  }

  video::-webkit-media-controls-mute-button {
    display: none;
  }

  video::-webkit-media-controls-timeline {
    display: none;
  }

  video::-webkit-media-controls-current-time-display {
    display: none;
  }
}

```

**main.js**

```js
"use strict";

const playNpauseBtn = document.querySelector("#play-pause");
const video = document.querySelector("video");
const rewindBtn = document.querySelector("#rewind");
const fastForwardBtn = document.querySelector("#fast-forward");
const volumeBtn = document.querySelector("#volume");
const progressIndicator = document.querySelector("#progress-indicator");
const progessBar = document.querySelector("#progress-bar");

function playNpauseFn() {
  video.paused ? video.play() : video.pause();
}

function updatePlayNPauseIcon() {
  const icon = playNpauseBtn.querySelector("i");
  icon.textContent = "";

  icon.textContent = video.paused ? "play_arrow" : "paused";
}

function rewindNforwardFn(type) {
  video.currentTime += type === "rewind" ? -10 : 10;
}

function muteNunmuteFn() {
  video.muted = video.muted ? false : true;
}

function updateVolumeIcon() {
  const icon = volumeBtn.querySelector("i");
  icon.textContent = "";
  icon.textContent = video.muted ? "volume_off" : "volume_up";
}

function updateProgress() {
  const progressPercentage = (video.currentTime / video.duration) * 100;

  progressIndicator.style.width = `${progressPercentage}%`;
}

function seekingFn(e) {
  const updatedTime = (e.offsetX / progessBar.offsetWidth) * video.duration;

  video.currentTime = updatedTime;
}

// PLAY AND PAUSE FUNCTIONALITY
video.addEventListener("play", updatePlayNPauseIcon);
video.addEventListener("click", playNpauseFn);
video.addEventListener("pause", updatePlayNPauseIcon);
playNpauseBtn.addEventListener("click", playNpauseFn);

// REWIND AND FAST FORWARD
rewindBtn.addEventListener("click", () => rewindNforwardFn("rewind"));
fastForwardBtn.addEventListener("click", () => rewindNforwardFn("forward"));

// MUTE AND UNMUTE
video.addEventListener("volumechange", updateVolumeIcon);
volumeBtn.addEventListener("click", muteNunmuteFn);

// PROGRESS
video.addEventListener("timeupdate", updateProgress);

// SEEKING
let mouseIsDown = false;

progessBar.addEventListener("mousedown", () => (mouseIsDown = true));
progessBar.addEventListener("mouseup", () => (mouseIsDown = false));
progessBar.addEventListener("click", seekingFn);
progessBar.addEventListener("mousemove", (e) => mouseIsDown && seekingFn);

// KEYBOARD NAVIGATIONS
window.addEventListener("keyup", (e) => {
  if (e.code === "Space") {
    playNpauseFn();
  } else if (e.code === "ArrowLeft") {
    rewindNforwardFn("rewind");
  } else if (e.code === "ArrowRight") {
    rewindNforwardFn("forward");
  } else {
    return;
  }
});

```

Alternativement, vous pouvez trouver tout le code sur le [dépôt GitHub](https://github.com/DeveloperAspire/custom-html5-video-player) que j'ai créé pour ce projet. Si vous le trouvez utile, envisagez de donner une étoile au dépôt – je l'apprécierais vraiment!

Vous pouvez accéder au site en direct en [visitant ici](https://custom-html5-video-player5.netlify.app/).

## Où aller à partir d'ici

Maintenant que vous avez terminé de lire cet article, rappelez-vous que votre voyage ne s'arrête pas ici. Il y a un monde entier de possibilités qui vous attend pour explorer et construire sur ce que vous avez appris.

L'API Video offre une large gamme de fonctionnalités que vous pouvez expérimenter, telles que l'ajout de contrôles de vitesse de lecture, le réglage du volume ou même des sous-titres. Vous pouvez également améliorer votre projet avec des animations, des interactions et vous assurer qu'il est réactif pour les mobiles, peut-être même en activant le mode paysage pour les appareils mobiles.

Pour plus d'inspiration et d'idées, n'hésitez pas à consulter ma version du projet [ici](https://aspire-video-player.netlify.app/) – bien qu'elle soit encore en cours de développement. Je suis excité de voir ce que vous allez créer! 

Si vous décidez de partager votre projet, n'oubliez pas de me taguer – j'adorerais le passer en revue et offrir tout feedback. Continuez à avancer, et bon codage!

## Conclusion

Félicitations! Vous avez atteint la fin de cet article et avez acquis une expérience pratique précieuse dans la construction de votre propre lecteur vidéo HTML5 personnalisé. En incorporant la navigation clavier et en optimisant pour l'accessibilité, vous avez garanti une expérience utilisateur fluide.

Je suis excité de voir ce que vous allez créer avec vos nouvelles connaissances, alors n'oubliez pas de partager vos projets avec moi.

 Merci d'avoir lu, et à la prochaine!

### Informations de contact

Souhaitez-vous entrer en contact avec moi? N'hésitez pas à me contacter via l'un des canaux suivants:

* Twitter / X: [@developeraspire](https://twitter.com/developeraspire)
* Email: developeraspire5@gmail.com