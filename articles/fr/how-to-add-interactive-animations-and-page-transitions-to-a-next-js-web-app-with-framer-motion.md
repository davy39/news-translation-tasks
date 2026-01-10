---
title: Comment ajouter des animations interactives et des transitions de page à une
  application Web Next.js avec Framer Motion
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-14T00:35:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-interactive-animations-and-page-transitions-to-a-next-js-web-app-with-framer-motion
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/framer-motion.jpg
tags:
- name: animation
  slug: animation
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
seo_title: Comment ajouter des animations interactives et des transitions de page
  à une application Web Next.js avec Framer Motion
seo_desc: "The web is vast and it's full of static websites and apps. But just because\
  \ those apps are static, it doesn't mean they have to be boring. \nHow can we use\
  \ Framer Motion to add some animations to our web apps and provide a more interactive\
  \ experience?..."
---

Le web est vaste et il est rempli de sites web et d'applications statiques. Mais simplement parce que ces applications sont statiques, cela ne signifie pas qu'elles doivent être ennuyeuses. 

Comment pouvons-nous utiliser Framer Motion pour ajouter des animations à nos applications web et offrir une expérience plus interactive ?

* [Qu'est-ce que Framer Motion ?](#heading-qu-est-ce-que-framer-motion)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Installation de Framer Motion dans votre application Next.js](#heading-etape-0-installation-de-framer-motion-dans-votre-application-nextjs)
* [Étape 1 : Animation du titre de la page avec Framer Motion dans une application Next.js](#heading-etape-1-animation-du-titre-de-la-page-avec-framer-motion-dans-une-application-nextjs)
* [Étape 2 : Ajout d'effets de survol animés avec Framer Motion aux éléments dans une application Next.js](#heading-etape-2-ajout-d-effets-de-survol-animes-avec-framer-motion-aux-elements-dans-une-application-nextjs)
* [Étape 3 : Ajout de transitions de page avec Framer Motion à une application Next.js](#heading-etape-3-ajout-de-transitions-de-page-avec-framer-motion-a-une-application-nextjs)
* [Étape 4 : Utilisation des keyframes de Framer Motion pour des animations avancées](#heading-etape-4-utilisation-des-keyframes-de-framer-motion-pour-des-animations-avancees)
* [Étape bonus : Devenir un peu étrange avec les animations dans notre application Next.js Rick et Morty](#heading-etape-bonus-devenir-un-peu-etrange-avec-les-animations-dans-notre-application-nextjs-rick-et-morty)

%[https://www.youtube.com/watch?v=q9tpBtvTTz8]

## Qu'est-ce que Framer Motion ?

[Framer Motion](https://www.framer.com/api/motion/) est une API qui provient directement de l'API Framer. Elle fournit des animations prêtes à l'emploi et des contrôles de gestes qui facilitent la création d'effets dynamiques.

Qu'est-ce que [Framer](https://www.framer.com/) ? Framer lui-même est un outil de prototypage d'interface utilisateur qui permet de créer des interfaces interactives avec des animations que vous pouvez transmettre à votre équipe, tandis que l'[API Framer](https://www.framer.com/api/) est une bibliothèque Javascript qui permet de faire cela avec du code.

L'API Motion découle de ce travail, mais est commodément disponible en tant que package séparé que nous pouvons utiliser pour le contrôle des animations.

## Que allons-nous construire ?

Nous allons utiliser les concepts de Framer Motion pour ajouter des interactions et des effets de transition de page à notre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/framer-motion-nextjs-animation-demo.gif)
_Démonstration d'animation utilisant Framer Motion_

Nous commencerons par quelques animations de base qui se produisent lorsque la page se charge, nous apprendrons comment les déclencher au survol, et nous construirons un wrapper qui permet à nos pages de transiter gracieusement dans Next.js.

## Avant de commencer

Ceci est la deuxième partie d'une série d'articles détaillant la construction d'un wiki Rick et Morty. [La première partie](https://www.freecodecamp.org/news/how-to-create-a-dynamic-rick-and-morty-wiki-web-app-with-next-js/) se concentre sur la demande de données à l'API Rick et Morty et la création de pages dynamiques.

[Comment créer une application Web Wiki Rick et Morty dynamique avec Next.js](https://www.freecodecamp.org/news/how-to-create-a-dynamic-rick-and-morty-wiki-web-app-with-next-js/)

Bien que vous puissiez suivre sans avoir lu la première partie, il pourrait être utile d'avoir un point de départ. Sinon, vous devriez pouvoir suivre la plupart de cela avec n'importe quelle application React.

## Étape 0 : Installation de Framer Motion dans votre application Next.js

Puisque nous allons utiliser Framer Motion pour fournir nos fonctionnalités d'animation, la première chose que nous voulons faire est de l'installer !

Une fois que vous avez l'application en cours d'exécution localement, vous pouvez l'installer avec :

```
yarn add framer-motion
# ou
npm install framer-motion

```

Et à ce stade, vous pouvez redémarrer votre serveur de développement et nous serons prêts à partir !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-nextjs.jpg)
_Point de départ - Application wiki Rick et Morty dans Next.js_

[Suivez avec le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/d768a2cd70fa990b31f9becdd82f034a676b6a9f)

## Étape 1 : Animation du titre de la page avec Framer Motion dans une application Next.js

Pour commencer, nous allons animer le titre de la page dans notre application wiki. Plus particulièrement, nous allons configurer Framer Motion pour faire apparaître le titre et le faire grandir lorsque la page se charge pour la première fois.

Tout d'abord, nous devons importer Motion dans notre application.

Commencez par ajouter l'instruction d'importation suivante en haut de `pages/index.js` :

```js
import { motion } from 'framer-motion';

```

Et maintenant que nous sommes prêts à utiliser `motion`, nous pouvons commencer par envelopper notre titre `<h1>` avec un composant motion :

```react
<motion.div>
  <h1 className="title">
    Wubba Lubba Dub Dub!
  </h1>
</motion.div>

```

Envelopper notre élément est ce qui va nous permettre de nous connecter à l'[API Motion](https://www.framer.com/api/motion/).

Si nous rechargeons notre page, elle ne fera cependant rien pour l'instant. C'est parce que nous n'avons pas encore configuré notre animation, alors faisons cela !

Lorsque nous utilisons l'API Motion avec notre composant `<motion.x>`, nous avons deux concepts de base que nous devons utiliser :

* Cycle de vie de l'animation
* Variantes

Chacune des props du cycle de vie de l'animation telles que `initial` et `animate` nous permettent de définir le nom de notre animation en tant que variante.

Notre prop `variants` est l'endroit où nous configurons ces animations en définissant les noms des variantes ainsi que l'animation que nous souhaitons qu'elles exécutent.

Pour commencer, ajoutons deux définitions de cycle de vie à notre composant de titre en ajoutant deux props de cycle de vie :

```react
<motion.div initial="hidden" animate="visible">
  <h1 className="title">
    Wubba Lubba Dub Dub!
  </h1>
</motion.div>

```

Maintenant, nous voulons définir celles-ci :

```react
<motion.div initial="hidden" animate="visible" variants={{
  hidden: {},
  visible: {},
}}>
  <h1 className="title">
    Wubba Lubba Dub Dub!
  </h1>
</motion.div>

```

Nous définissons deux variantes — hidden et visible — que nous référençons ensuite dans les props de cycle de vie `initial` et `animate`.

Maintenant, si nous rechargeons la page, elle ne fera toujours rien puisque nous n'avons pas encore défini les animations elles-mêmes, alors faisons cela :

```react
<motion.div initial="hidden" animate="visible" variants={{
  hidden: {
    scale: .8,
    opacity: 0
  },
  visible: {
    scale: 1,
    opacity: 1,
    transition: {
      delay: .4
    }
  },
}}>
  <h1 className="title">
    Wubba Lubba Dub Dub!
  </h1>
</motion.div>

```

Voici ce qui se passe :

* Nous avons deux cycles de vie différents, un initial et un animate. L'initial est ce qui se charge "initialement" lorsque la page se charge, où animate est ce qui se passe après le chargement de la page
* Dans notre état initial, nous définissons l'élément pour qu'il soit légèrement réduit avec une opacité de 0
* Lorsque la page se charge et déclenche notre animation, nous rétablissons l'échelle à 1 et l'opacité à 1
* Nous définissons également un délai sur notre transition afin qu'elle attende .4s avant de déclencher l'animation. Cela aide simplement à laisser les choses se charger un peu avant de déclencher

Donc, dans ce qui précède, ce qui se passe réellement est que .4s après le chargement de la page, nous allons faire apparaître le titre et lui donner l'impression de grandir légèrement.

Et si nous enregistrons cela et rechargeons la page, nous pouvons voir l'effet de notre titre !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/animated-header-framer-motion.gif)
_Titre animé dans l'application Next.js avec Framer Motion_

[Suivez avec le commit](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/80eb7c3fb694577002feac063a613c421826e03c)

## Étape 2 : Ajout d'effets de survol animés avec Framer Motion aux éléments dans une application Next.js

Maintenant que nous avons une compréhension de base de la façon d'ajouter des animations lorsque la page se charge, commençons à ajouter une certaine interaction.

Nous allons ajouter des effets de survol à chaque carte de personnage. Ainsi, lorsque votre curseur passe sur l'une des cartes, nous déclencherons notre animation.

Tout d'abord, à l'intérieur de notre grille de liste non ordonnée `<ul className="grid">`, mettons à jour l'élément de liste `<li>` pour qu'il soit un élément `<motion.li>` :

```react
<motion.li key={id} className="card">
  ...
</motion.li>

```

Si vous enregistrez et rechargez la page, vous remarquerez que nous avons en fait un problème.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-missing-styles.jpg)
_Application avec des styles manquants pour les cartes de personnages_

En raison de l'intégration entre motion et l'intégration CSS de Next.js, notre application est perturbée par le nom de la classe.

Bien que cela ne le répare pas à son "cœur", nous pouvons le corriger pour notre démonstration en supprimant la prop `jsx` de notre bloc `<style>` supérieur où se trouve notre définition `.card`.

Changer :

```react
<style jsx>{`

```

En :

```react
<style>{`

```

Maintenant, si nous rechargeons notre page, nous sommes revenus à notre point de départ.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-nextjs.jpg)
_Application avec les styles corrects_

Pour ajouter notre effet de survol, nous allons créer une nouvelle prop sur notre composant `<motion.li>` appelée `whileHover` et la remplir avec quelques styles de base :

```react
<motion.li key={id} className="card" whileHover={{
  scale: 1.2,
  transition: {
    duration: .2
  }
}}>

```

Ci-dessus, nous disons à motion que lorsque quelqu'un survole notre élément, nous voulons qu'il grandisse en le mettant à l'échelle à 1.2 et nous voulons que cette animation dure .2s.

Et si nous rechargeons la page, nous pouvons voir notre animation !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-wiki-hover-framer-motion.gif)
_Effet de survol dans l'application Next.js utilisant Framer Motion_

Si vous regardez le bas de l'effet, lorsque la carte grandit, elle chevauche la carte en dessous et semble un peu cassée. Nous pouvons corriger cela en appliquant un z-indexing et une couleur de fond !

```react
<motion.li key={id} className="card" whileHover={{
  position: 'relative',
  zIndex: 1,
  background: 'white',
  scale: 1.2,
  transition: {
    duration: .2
  }
}}>

```

Et si nous rechargeons la page à nouveau, nous pouvons maintenant voir que lorsque notre carte grandit, elle apparaît au-dessus de la carte en dessous !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-framer-motion-animation-fixed-layer.gif)
_Correction du z-indexing et du fond sur l'effet de survol_

[Suivez avec le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/b5c79c245edd586ee0d5fa6392bc52ae43378e13)

## Étape 3 : Ajout de transitions de page avec Framer Motion à une application Next.js

Déclencher des animations lorsque la page se charge et les effets de survol est cool, mais c'est une belle touche lorsque votre application peut fournir des transitions gracieuses entre les pages. Cela peut faire partie de ce qui la fait ressentir comme une "application web" plutôt qu'un site web "statique".

Pour ce faire, nous devons [configurer notre application Next.js](https://nextjs.org/docs/advanced-features/custom-app) avec un wrapper autour des pages racines du site web. Cela nous permettra de nous connecter au cycle de vie de la navigation et d'animer correctement nos pages.

Pour commencer, nous devons créer un nouveau fichier sous le répertoire `pages` appelé `_app.js` :

```react
// Dans pages/_app.js
function App({ Component, pageProps }) {
  return (
    <Component {...pageProps} />
  )
}

export default App;

```

Bien que nous n'ayons pas nécessairement besoin de comprendre les spécificités de ce qui se passe, nous créons essentiellement un wrapper où nous pouvons ajouter des fonctionnalités supplémentaires.

Avec ce nouveau fichier, si vous rechargez la page, vous ne devriez pas encore voir de changements.

Ensuite, nous allons ajouter notre fondation qui nous permet de configurer nos transitions de page.

Tout d'abord, importons motion en haut de notre page :

```react
import { motion } from 'framer-motion';

```

Ensuite, similaire à nos autres animations, créons un nouveau composant `<motion.div>` qui enveloppe notre page.

```react
<motion.div initial="pageInitial" animate="pageAnimate" variants={{
  pageInitial: {
    opacity: 0
  },
  pageAnimate: {
    opacity: 1
  },
}}>
  <Component {...pageProps} />
</motion.div>

```

Ici, nous définissons un état initial avec une opacité de 0 et un état d'animation avec une opacité de 1, avec l'idée qu'il s'estompera.

Maintenant, si vous appuyez sur actualiser, vous remarquerez que la page s'estompe. Mais si vous cliquez sur l'un des personnages, lorsque la page du personnage se charge, elle ne s'estompe pas.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-app-no-page-transitions.gif)
_Changement de page sans effet de transition_

Le problème est que, actuellement, le composant motion ne comprend pas qu'il s'agit d'une nouvelle route, nous devons donc le forcer à reconnaître cela et à se mettre à jour.

Pour ce faire, nous allons déstructurer l'argument `router` dans nos props App :

```react
function App({ Component, pageProps, router }) {

```

Et sur notre composant motion, nous allons l'utiliser comme clé :

```react
<motion.div key={router.route} initial="pageInitial" animate="pageAnimate" variants={{

```

Maintenant, si nous rechargeons la page et naviguons entre notre page de personnage et notre page d'accueil, vous verrez qu'elle fait maintenant apparaître le contenu !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-app-fade-page-transitions-framer-motion.gif)
_Transition de page en fondu dans Next.js avec Framer Motion_

[Suivez avec le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/c558283e0ade4dcc300c9b35e71b87217dd0bd78)

## Étape 4 : Utilisation des keyframes de Framer Motion pour des animations avancées

Maintenant que nous avons les bases de la configuration des animations dans le cycle de vie de notre application, nous pouvons aller plus loin en utilisant des [keyframes](https://www.framer.com/api/motion/examples/#keyframes).

La façon dont les keyframes fonctionnent, c'est que lorsque nous définissons une animation, nous pouvons définir cette animation pour qu'elle passe par un ensemble de différentes valeurs pour notre propriété donnée, ce qui nous permet de créer des animations personnalisées à notre guise.

Par exemple, disons que nous voulons faire en sorte qu'un élément, au survol, grandisse à 2x la taille, le rendre un peu plus petit à 1,5x la taille, puis revenir à 2x la taille, le tout en une seule séquence d'animation. Nous pouvons faire cela avec des keyframes !

La syntaxe pour cela ressemblerait à ceci :

```js
scale: [1, 2, 1.5, 2]

```

Nous spécifions notre séquence en utilisant un tableau qui dit que nous voulons que notre élément commence à sa taille normale à 1x, puis dans le cadre suivant, il grandira à 2x, puis rétrécira un peu à 1,5x, puis enfin grandira à nouveau à 2x.

Pour tester cela, nous allons apporter quelques modifications à notre effet de survol que nous avons déjà configuré pour nos cartes de personnages.

Dans `pages/index.js`, mettez à jour la propriété `whileHover` sur nos éléments de liste motion à :

```react
<motion.li key={id} className="card" whileHover={{
  position: 'relative',
  zIndex: 1,
  background: 'white',
  scale: [1, 1.4, 1.2],
  rotate: [0, 10, -10, 0],
  transition: {
    duration: .2
  }
}}>

```

Nous spécifions 2 ensembles de keyframes, qui sont les suivants :

* Sa taille initiale est de 1x et il a une rotation de 0 (ou aucune rotation)
* Il passe ensuite à une échelle de 1,4x la taille et tourne de 10 degrés
* Il revient ensuite à une échelle de 1,2x la taille et tourne dans l'autre sens à -10 degrés
* À ce stade, les keyframes de l'échelle sont terminées, donc nous ne mettrions plus rien à l'échelle, mais nous avons une dernière rotation, où nous tournons à nouveau vers notre position initiale de 0 (ou aucune rotation)

Et si nous rechargeons la page et survolons nos éléments, nous pouvons voir nos effets en action !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-hover-effect-framer-motion.gif)
_Effet de survol Framer Motion avec rotation et mise à l'échelle_

Sans keyframes, nous ne pouvons faire des effets d'animation qu'à partir d'un seul état initial vers une autre valeur unique. Mais avec nos keyframes, nous pouvons ajouter des animations plus dynamiques en nous déplaçant vers différentes valeurs.

[Suivez avec le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/99c75a3674623f896e12d29fff1431ac609bd60a)

## Étape bonus : Devenir un peu étrange avec les animations dans notre application Next.js Rick et Morty

Pour ajouter une autre couche de plaisir à cela, nous pouvons jouer avec d'autres propriétés qui rendent nos animations encore plus dynamiques.

Pour commencer, nous allons améliorer nos effets de survol.

Dans notre fichier `pages/index.js` à l'intérieur de la prop `whileHover` de notre élément de carte `<motion.li>`, ajoutons la propriété suivante :

```js
filter: [
  'hue-rotate(0)',
  'hue-rotate(360deg)',
  'hue-rotate(45deg)',
  'hue-rotate(0)'
],

```

Ici, nous configurons un nouvel ensemble de keyframes qui va "tourner" la teinte de l'image en fonction de la [fonction CSS hue-rotate](https://developer.mozilla.org/en-US/docs/Web/CSS/filter-function/hue-rotate).

Et si nous enregistrons et rechargeons notre page, cela nous donne un joli petit effet de couleur.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-hover-effect-weird-framer-motion.gif)
_Changement de couleur de l'image au survol avec Framer Motion et les filtres CSS_

Mais c'est trop subtil pour moi — je veux que ce soit un peu plus étrange.

Mettons à jour notre propriété de filtre comme suit :

```js
filter: [
  'hue-rotate(0) contrast(100%)',
  'hue-rotate(360deg) contrast(200%)',
  'hue-rotate(45deg) contrast(300%)',
  'hue-rotate(0) contrast(100%)'
],

```

Maintenant, non seulement la couleur change, nous utilisons la [fonction CSS de contraste](https://developer.mozilla.org/en-US/docs/Web/CSS/filter-function/contrast) pour rendre les couleurs plus extrêmes, ce qui nous donne un effet encore plus étrange.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-framer-js-hover-effect-color.gif)
_Changement de contraste et de couleurs en utilisant des filtres CSS au survol avec Framer Motion_

Ensuite, nous pouvons faire quelque chose de similaire avec nos transitions de page !

Pour ce faire, nous allons utiliser une nouvelle partie du cycle de vie du composant Motion — la sortie. Pour ce faire, nous devons utiliser le composant [AnimatePresence](https://www.framer.com/api/motion/animate-presence/) de Motion qui nous permet d'animer les composants lorsqu'ils sont retirés de l'arbre React.

Pour commencer, ouvrons `pages/_app.js` et importons ce composant en haut :

```js
import { motion, AnimatePresence } from 'framer-motion';

```

Ensuite, nous voulons envelopper notre composant `<motion.div>` avec notre nouveau composant `AnimatePresence` :

```react
<AnimatePresence>
      <motion.div key={router.route} initial="pageInitial" animate="pageAnimate" variants={{

```

Avec notre composant enveloppé, nous pouvons maintenant définir notre nouvelle prop de cycle de vie `exit` ainsi que sa variante :

```react
<motion.div key={router.route} initial="pageInitial" animate="pageAnimate" exit="pageExit" variants={{
  pageInitial: {
    opacity: 0
  },
  pageAnimate: {
    opacity: 1
  },
  pageExit: {
    backgroundColor: 'white',
    filter: `invert()`,
    opacity: 0
  }
}}>

```

Dans ce qui précède, nous :

* Configurons une variante `pageExit`
* Définissons notre prop de cycle de vie `exit` sur `pageExit`
* À l'intérieur de notre variante `pageExit`, nous définissons la couleur de fond sur blanc et nous ajoutons un filtre pour inverser les couleurs

_Note : il est important de définir la couleur de fond sur blanc, sinon, le filtre d'inversion ne s'appliquera pas à l'arrière-plan._

Et si nous enregistrons et rechargeons la page, lorsque nous naviguons vers un autre élément, nous obtenons notre effet !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rick-and-morty-app-page-transitions.gif)
_Inversion des couleurs lors de la transition de page avec Framer Motion_

[Suivez avec le commit !](https://github.com/colbyfayock/my-rick-and-morty-wiki/commit/3c1455370f750ff86b75a3b3edc446ebe553bf5b)

## Que pouvons-nous faire d'autre ?

### Ajouter des animations pour échelonner les résultats de recherche

Si vous consultez ma démonstration originale sur laquelle j'ai basé ce tutoriel, j'ajoute une fonctionnalité qui fait flotter les résultats en les décalant légèrement vers le haut.

Nous pouvons faire cela avec la propriété de transition [staggerChildren](https://www.framer.com/api/motion/types/#orchestration.staggerchildren) et en définissant les [propriétés de position x et y](https://www.framer.com/api/motion/component/#transform) sur nos éléments de liste.

[https://github.com/colbyfayock/rick-and-morty-wiki/blob/master/pages/index.js#L11](https://github.com/colbyfayock/rick-and-morty-wiki/blob/master/pages/index.js#L11)

### Animer les boutons

Actuellement, les boutons sont simplement statiques. Ajoutez des effets de survol et de clic aux boutons comme "Load More" en bas.

### Ajouter plus d'effets étranges

C'est Rick et Morty après tout, rendez-le aussi étrange que possible ! Mais assurez-vous qu'il reste utilisable.

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>