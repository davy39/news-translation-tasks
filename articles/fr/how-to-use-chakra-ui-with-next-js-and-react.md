---
title: Comment utiliser Chakra UI avec Next.js et React
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-10-21T00:16:01.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-chakra-ui-with-next-js-and-react
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/chakra.jpg
tags:
- name: components
  slug: components
- name: Libraries
  slug: libraries
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment utiliser Chakra UI avec Next.js et React
seo_desc: "Building websites and applications is hard. There are a lot of things to\
  \ consider to make sure our apps are usable and accessible including how our React\
  \ components work. \nHow can we take advantage of the power of Chakra UI to build\
  \ great web apps?\n\n..."
---

Construire des sites web et des applications est difficile. Il y a beaucoup de choses à considérer pour s'assurer que nos applications sont utilisables et accessibles, y compris le fonctionnement de nos composants React.

Comment pouvons-nous tirer parti de la puissance de Chakra UI pour construire de grandes applications web ?

* [Qu'est-ce que Chakra UI ?](#heading-qu-est-ce-que-chakra-ui)
* [Ce qui rend Chakra UI si génial](#heading-ce-qui-rend-chakra-ui-si-genial)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Créer un nouveau projet React avec Next.js](#heading-etape-0-creer-un-nouveau-projet-react-avec-nextjs)
* [Étape 1 : Installer et configurer Chakra UI dans Next.js](#heading-etape-1-installer-et-configurer-chakra-ui-dans-nextjs)
* [Étape 2 : Ajouter des composants Chakra UI à une application React](#heading-etape-2-ajouter-des-composants-chakra-ui-a-une-application-react)
* [Étape 3 : Créer des composants réactifs avec Chakra UI](#heading-etape-3-creer-des-composants-reactifs-avec-chakra-ui)
* [Étape 4 : Personnaliser le thème par défaut de Chakra UI](#heading-etape-4-personnaliser-le-theme-par-defaut-de-chakra-ui)

%[https://www.youtube.com/watch?v=ubB5l-HVPgY]

## Qu'est-ce que Chakra UI ?

[Chakra UI](https://chakra-ui.com/) est une bibliothèque de composants pour React qui facilite la création de l'interface utilisateur d'une application ou d'un site web.

Leur objectif est de fournir un ensemble de composants simple, modulaire et accessible pour démarrer rapidement.

## Ce qui rend Chakra UI si génial

Pour commencer, par défaut, Chakra s'efforce de rendre chaque composant accessible. C'est une partie critique du développement d'applications qui est souvent négligée, et les mainteneurs de Chakra ont fait de leur mieux pour s'assurer que les composants suivent les [directives WAI-ARIA](https://www.w3.org/WAI/standards-guidelines/aria/).

Chakra inclut également une API simple permettant aux développeurs d'être productifs. Elle permet aux personnes et aux équipes de créer des applications inclusives sans avoir à se soucier de construire un tas de composants eux-mêmes.

Pour le style et la personnalisation, Chakra utilise [Emotion](https://emotion.sh/) sous le capot pour fournir aux développeurs la capacité de styliser leurs composants directement dans leur JavaScript avec des props de style. Il vient avec un thème par défaut, mais permet de le remplacer facilement avec des paramètres personnalisés.

## Que allons-nous construire ?

Pour avoir une bonne idée de comment Chakra fonctionne, nous allons essentiellement reconstruire le modèle par défaut de Next.js avec des composants Chakra UI.

Cela nous aidera à comprendre quelques concepts importants, tels que comment utiliser Chakra UI avec Next.js, comment ajouter des styles personnalisés avec des props, et comment personnaliser le thème Chakra UI.

Les concepts ici peuvent s'appliquer à presque n'importe quelle application [React](https://reactjs.org/), bien que les exemples seront légèrement spécifiques à Next.js.

## Étape 0 : Créer un nouveau projet React avec Next.js

Pour commencer, nous avons besoin d'une application React. Nous allons utiliser Next.js comme notre framework, ce qui nous permettra de créer facilement une nouvelle application.

Une fois dans le répertoire où vous souhaitez créer votre projet, exécutez :

```
yarn create next-app my-chakra-app
# ou
npx create-next-app my-chakra-app

```

Note : n'hésitez pas à changer `my-chakra-app` par le nom que vous souhaitez donner au répertoire du projet.

Et une fois que c'est terminé, vous pouvez naviguer dans ce répertoire et démarrer le projet avec :

```
yarn dev
# ou
npm run dev

```

Cela devrait lancer votre serveur de développement à l'adresse [http://localhost:3000](http://localhost:3000) et nous devrions être prêts à partir !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-default-template.jpg)
_Modèle par défaut de Next.js_

[Suivez le commit !](https://github.com/colbyfayock/my-chakra-app/commit/01f6ec8d961eb197fe3e8a32e498d07bf0be269b)

## Étape 1 : Installer et configurer Chakra UI dans Next.js

Ensuite, installons Chakra UI.

À l'intérieur de votre répertoire de projet, exécutez :

```
yarn add @chakra-ui/core @emotion/core @emotion/styled emotion-theming
# ou 
npm install @chakra-ui/core @emotion/core @emotion/styled emotion-theming

```

Cela installera Chakra UI et ses dépendances, qui incluent Emotion, car il s'appuie sur celui-ci pour le style.

Pour faire fonctionner Chakra à l'intérieur de notre application, nous devons configurer un Provider à la racine de notre application. Cela permettra à tous les composants de Chakra de communiquer entre eux et d'utiliser la configuration pour maintenir des styles cohérents.

À l'intérieur de `pages/_app.js`, commençons par importer notre Provider en haut :

```
import { ThemeProvider, theme } from '@chakra-ui/core';

```

Ensuite, remplacez l'instruction return à l'intérieur du composant par :

```jsx
function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider theme={theme}>
      <Component {...pageProps} />
    </ThemeProvider>
  )
}

```

Comme vous le remarquerez, nous passons également une variable `theme` à notre provider. Nous importons le thème par défaut de Chakra UI directement depuis Chakra et le passons à notre `ThemeProvider` afin que tous nos composants puissent obtenir les styles et configurations par défaut.

Enfin, nous voulons ajouter un composant appelé `CSSReset` directement comme enfant de notre `ThemeProvider`.

Tout d'abord, ajoutez `CSSReset` comme import :

```
import { ThemeProvider, theme, CSSReset } from '@chakra-ui/core';

```

Ensuite, ajoutez le composant directement à l'intérieur de `ThemeProvider` :

```jsx
<ThemeProvider theme={theme}>
  <CSSReset />
  <Component {...pageProps} />
</ThemeProvider>

```

Et maintenant, si nous rechargeons la page, nous pouvons voir que les choses ont un peu changé !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-chakra-ui-css-reset.jpg)
_Next.js avec Chakra UI CSS Reset_

Le navigateur vient avec beaucoup de styles par défaut et par défaut, Chakra UI ne les remplace pas. Cela inclut des styles comme les bordures sur un élément de bouton.

Bien que nous n'ayons pas nécessairement besoin du CSS Reset ici, nous pourrions remplacer ces choses manuellement. Cela nous fournit une base où nous saurons que Chakra UI fonctionne comme prévu et nous pouvons commencer à ajouter nos composants.

[Suivez le commit !](https://github.com/colbyfayock/my-chakra-app/commit/8538b3609cfac71b6ece60e36314edf9a189941b)

## Étape 2 : Ajouter des composants Chakra UI à une application React

Maintenant, la partie amusante. Nous allons utiliser les composants Chakra UI pour essayer de reconstruire le modèle par défaut de Next.js. Cela ne ressemblera pas à 100 % exactement, mais cela en gardera l'esprit et nous pourrons le personnaliser comme nous le souhaitons.

### Construire le titre et la description

En commençant par le haut, mettons à jour notre titre et notre description.

En haut de la page, nous devons importer notre composant `Heading` :

```
import { Heading, Link } from "@chakra-ui/core";

```

Ensuite, remplaçons le `<h1>` par :

```jsx
<Heading as="h1" size="2xl" mb="2">
  Bienvenue dans Next.js !
</Heading>

```

Ici, nous utilisons le composant [Heading](https://chakra-ui.com/heading) que nous définissons ensuite comme un `h1`. Nous pouvons utiliser n'importe quel nom de balise d'élément de titre HTML, mais puisque nous remplaçons un h1, nous voulons utiliser celui-ci.

Nous définissons également un attribut `size`, qui nous permet de contrôler la taille de notre titre, ainsi que `mb`, qui signifie `margin-bottom`, nous permettant d'ajouter un peu d'espace en dessous.

Et nous pouvons déjà voir que notre page ressemble davantage au modèle par défaut.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-heading-component.jpg)
_Composant Heading de Chakra UI_

Nous voulons également ajouter notre lien.

Ajoutez `Link` à notre instruction d'import en haut, puis à l'intérieur de notre composant `<Heading>`, remplacez le texte Next.js par :

```jsx
<Link color="teal.500" href="https://nextjs.org">Next.js !</Link>

```

Le composant [Link](https://chakra-ui.com/link) de Chakra crée un lien comme prévu, mais permet ensuite d'utiliser les props de style pour le personnaliser. Ici, nous utilisons la variable de couleur `teal.500` que Chakra fournit pour changer notre lien en couleurs de Chakra.

Et nous pouvons voir que nous avons notre lien Next.js !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-heading-with-link.jpg)
_Composant Heading de Chakra UI avec le composant Link_

La dernière partie de l'en-tête est la description. Pour cela, nous voulons utiliser le composant Text.

Ajoutez `Text` et `Code` à l'instruction d'import et remplacez la description par :

```jsx
<Text fontSize="xl" mt="2">
  Commencez par modifier <Code>pages/index.js</Code>
</Text>

```

Nous utilisons le composant [Text](https://chakra-ui.com/text) pour recréer une balise `<p>` et le composant [Code](https://chakra-ui.com/code) pour créer notre balise `<code>`. Similaire à notre composant Heading, nous ajoutons une `fontSize` pour agrandir la police et `mt` qui signifie `margin-top` pour ajouter un peu d'espace au-dessus.

Et maintenant nous avons notre en-tête !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-text-with-code-component.jpg)
_Composant Text de Chakra UI avec Code_

### Remplacer les cartes d'information par des composants Chakra UI

Pour chacune de nos cartes, nous pouvons utiliser les mêmes concepts que nous avons utilisés avec l'en-tête pour recréer chacune de nos boîtes.

Pour commencer, ajoutez un import pour le composant `Flex` et remplacez la balise `<div className={styles.grid}>` par :

```jsx
<Flex flexWrap="wrap" alignItems="center" justifyContent="center" maxW="800px" mt="10">
  ...
</Flex>

```

Assurez-vous de laisser toutes les cartes à l'intérieur du composant Flex. Le composant [Flex](https://chakra-ui.com/flex) recréera notre grille en ajoutant Flexbox ainsi que les mêmes propriétés que celles de la grille précédente.

À ce stade, cela devrait être exactement le même qu'avant.

Ensuite, ajoutez `Box` à l'instruction d'import, puis remplacez la première carte par :

```jsx
<Box as="a" href="https://nextjs.org/docs" p="6" m="4" borderWidth="1px" rounded="lg" flexBasis="45%">
  <Heading as="h3" size="lg" mb="2">Documentation &rarr;</Heading>
  <Text fontSize="lg">Trouvez des informations détaillées sur les fonctionnalités et l'API de Next.js.</Text>
</Box>

```

Similaire à notre composant Heading, nous définissons notre composant [Box](https://chakra-ui.com/box) comme une balise `<a>` lui permettant de servir de lien. Nous configurons ensuite nos props de style pour répliquer nos cartes.

À l'intérieur de cela, nous utilisons le composant Heading et Text pour recréer le contenu réel des cartes.

Et après avoir changé seulement la première carte, nous pouvons maintenant voir les changements :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-box-component.jpg)
_Composant Box de Chakra UI_

Maintenant, nous pouvons revenir en arrière et remplacer les trois autres cartes avec les mêmes composants pour terminer la recréation de notre grille.

Pour le plaisir, nous pouvons ajouter une 5ème carte qui mène à Chakra UI :

```jsx
<Box as="a" href="https://chakra-ui.com/" p="6" m="4" borderWidth="1px" rounded="lg" flexBasis="45%">
  <Heading as="h3" size="lg" mb="2">Chakra UI &rarr;</Heading>
  <Text fontSize="lg">Construisez des applications et sites React accessibles rapidement.</Text>
</Box>

```

Et avec toutes nos modifications, nous pouvons maintenant voir notre modèle de départ Next.js recréé !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-nextjs-grid.jpg)
_Chakra UI recréant la grille Next.js_

[Suivez le commit !](https://github.com/colbyfayock/my-chakra-app/commit/a324f8cd1d4120027a7f4dbcb16f45980de5495a)

## Étape 3 : Créer des composants réactifs avec Chakra UI

Une partie de ce que la grille par défaut de Next.js était capable de fournir était la capacité pour les cartes de s'étendre à pleine largeur une fois que la taille du navigateur devient suffisamment petite. Cela est particulièrement pertinent à `600px`, ce qui signifie généralement que quelqu'un est sur un appareil mobile.

Si nous regardons notre page sur un appareil mobile, nous pouvons voir que nos cartes ne remplissent pas toute la largeur.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-not-responsive.jpg)
_Chakra UI par défaut sans réactivité_

Chakra nous permet de [définir des styles réactifs](https://chakra-ui.com/responsive-styles) avec sa mise en page intégrée, nous permettant de recréer facilement nos cartes de grille réactives.

Pour ce faire, au lieu de passer une seule valeur à nos props de style, nous pouvons passer un tableau.

Par exemple, sur chacun de nos composants Box, mettons à jour la prop `flexBasis` à :

```jsx
flexBasis={['auto', '45%']}

```

Ici, selon les [points d'arrêt réactifs par défaut de Chakra](https://chakra-ui.com/responsive-styles), nous disons que par défaut, nous voulons que notre `flexBasis` soit défini sur `auto`. Mais pour tout ce qui est `480px` et plus grand, ce qui est à nouveau le premier point d'arrêt par défaut de Chakra, nous le définissons sur `45%`.

Chakra considère son style réactif comme étant mobile d'abord, c'est pourquoi vous voyez le `480px` agir comme une taille minimale, et non une taille maximale.

Et avec ce changement, nous pouvons maintenant voir que sur un grand appareil, nous avons toujours notre grille.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-large-device.jpg)
_Composants Chakra UI sur un grand appareil_

Mais maintenant sur mobile, nos cartes occupent toute la largeur !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/chakra-ui-small-device.jpg)
_Composants Chakra UI sur un petit appareil_

L'utilisation du modèle de tableau fonctionne pour tous les points d'arrêt, donc si vous vouliez plus de contrôle sur vos styles, Chakra vous permet de le faire.

[Suivez le commit !](https://github.com/colbyfayock/my-chakra-app/commit/c08e80b60395aa738eaa8f8eb411ca7004ffac9d)

## Étape 4 : Personnaliser le thème par défaut de Chakra UI

Bien que Chakra fournisse un thème par défaut assez génial, nous avons également la possibilité de le personnaliser à notre guise pour correspondre à notre marque ou à notre goût personnel.

Par exemple, bien que le bleu-vert que nous avons utilisé pour notre lien Heading soit génial et utilise les styles de Chakra, que se passe-t-il si je voulais personnaliser tous les liens pour utiliser le violet que j'[utilise sur mon site web](https://colbyfayock.com/) ?

Pour commencer, Chakra vient avec un violet par défaut, donc nous pouvons mettre à jour notre lien pour utiliser ce violet :

```jsx
Bienvenue dans <Link color="purple.500" href="https://nextjs.org">Next.js !</Link>

```

Et nous voyons notre changement.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-purple-header.jpg)
_Rendre le lien de l'en-tête Next.js violet avec la prop de style de couleur_

Cela a l'air génial, mais mettons-le à jour avec le violet exact que j'utilise.

À l'intérieur de `pages/_app.js`, nous allons créer un nouvel objet en haut de la page, où nous étendons le thème par défaut en créant un nouvel objet de thème. Nous allons également remplacer la prop `theme` par notre nouvel objet :

```
const customTheme = {
  ...theme
}

function MyApp({ Component, pageProps }) {
  return (
    <ThemeProvider theme={customTheme}>

```

Si nous sauvegardons et rechargeons la page, elle aura exactement le même aspect.

Ensuite, nous voulons mettre à jour les couleurs, donc dans notre objet de thème personnalisé, ajoutons la propriété des couleurs, où nous pouvons ensuite définir notre violet personnalisé :

```jsx
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    purple: '#692ba8'
  }
}

```

Note : vous verrez ici que nous étendons également `theme.colors`. Si nous ne le faisons pas, nous remplacerons l'objet des couleurs par seulement la valeur violet, ce qui signifie que nous n'aurons aucune autre couleur.

Mais si nous rechargeons la page, notre lien n'est plus violet !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-link-no-color.jpg)
_Lien Next.js sans couleur_

Chakra utilise généralement des gammes de couleurs qui nous permettent d'utiliser différentes nuances de chacune des couleurs. Dans notre composant Link, nous spécifions `purple.500` que nous n'avons pas défini pour exister.

Pour corriger cela, nous pouvons utiliser un outil comme [Smart Swatch](https://smart-swatch.netlify.app/#692ba8) pour obtenir toutes les valeurs de couleur dont nous avons besoin et les définir dans notre objet de thème personnalisé :

```jsx
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    purple: {
      50: '#f5e9ff',
      100: '#dac1f3',
      200: '#c098e7',
      300: '#a571dc',
      400: '#8c48d0',
      500: '#722fb7',
      600: '#59238f',
      700: '#3f1968',
      800: '#260f40',
      900: '#10031a',
    }
  }
}

```

Astuce : Smart Swatch vous permet en fait de copier ces valeurs sous forme d'objet JavaScript, ce qui facilite le collage dans notre thème !

Et maintenant, si nous rechargeons la page, nous pouvons voir notre violet !

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-custom-purple.jpg)
_Next.js avec violet personnalisé_

Bien que nous ayons utilisé une valeur de gamme ici, nous pouvons également spécifier des variables de couleur sans gamme.

Supposons que je veux laisser le violet par défaut de Chakra "tel quel" mais fournir un moyen de référencer mon violet.

Pour ce faire, je pourrais supprimer ces valeurs violettes et ajouter une nouvelle variable personnalisée :

```
const customTheme = {
  ...theme,
  colors: {
    ...theme.colors,
    spacejelly: '#692ba8'
  }
}

```

Ensuite, mettez à jour mon Link pour utiliser cette couleur :

```jsx
Bienvenue dans <Link color="spacejelly" href="https://nextjs.org">Next.js !</Link>

```

Et nous pouvons voir que nous utilisons maintenant notre violet sans remplacer l'original :

![Image](https://www.freecodecamp.org/news/content/images/2020/10/nextjs-spacejelly-purple.jpg)
_Next.js avec une variable de couleur personnalisée_

Nous pouvons appliquer cela à la plupart des parties des styles de Chakra, y compris la typographie et la définition de points d'arrêt personnalisés. C'est une autre façon de rendre notre projet personnalisé tout en tirant parti de la puissance de Chakra !

[Suivez le commit !](https://github.com/colbyfayock/my-chakra-app/commit/b9d707ce3324207c25c2348934ca0c506402bd2f)

## Que pouvez-vous faire d'autre avec Chakra UI ?

Bien que nous ayons passé en revue quelques exemples plus simples, cela ouvre vraiment la porte à des changements et contrôles de style plus complexes que Chakra fournit avec ses API de composants.

Il existe également une multitude de composants géniaux que vous pouvez utiliser pour transformer votre site web ou votre application et rendre le développement rapide et facile !

Ils fournissent même des [recettes](https://chakra-ui.com/recipes) qui ont quelques exemples de la façon dont vous pouvez combiner les composants, ce qui donne des fonctionnalités puissantes. Cela inclut un en-tête réactif et même l'ajout d'animations avec Framer Motion.

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4e83fb Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsorisez-moi</a>
    </li>
  </ul>
</div>