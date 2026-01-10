---
title: Pourquoi vous devriez commencer à utiliser Chakra UI
subtitle: ''
author: Georgey V B
co_authors: []
series: null
date: '2021-05-11T15:22:27.000Z'
originalURL: https://freecodecamp.org/news/why-should-you-start-using-chakraui
coverImage: https://www.freecodecamp.org/news/content/images/2021/05/Why-should-you-start-using--5-.png
tags:
- name: Accessibility
  slug: accessibility
- name: Front-end Development
  slug: front-end-development
- name: Web Development
  slug: web-development
seo_title: Pourquoi vous devriez commencer à utiliser Chakra UI
seo_desc: "In this article, I'll talk about what ChakraUI is and why you should use\
  \ it.\nChakra UI is a component-based library. It's made up of basic building blocks\
  \ that can help you build the front-end of your web application. \nIt is customizable\
  \ and reusable..."
---

Dans cet article, je vais vous expliquer ce qu'est Chakra UI et pourquoi vous devriez l'utiliser.

Chakra UI est une bibliothèque basée sur des composants. Elle est composée de blocs de construction de base qui peuvent vous aider à construire le front-end de votre application web.

Elle est personnalisable et réutilisable, et surtout, elle prend en charge ReactJs, ainsi que d'autres bibliothèques.

Voici ce que nous allons aborder dans cet article :

1. Qu'est-ce que Chakra UI ?
2. Comment démarrer et installer Chakra UI
3. Personnalisation et fonctionnalités de Chakra UI
4. Comment Chakra UI affecte votre score Lighthouse
5. Comment utiliser le mode sombre dans Chakra UI
6. Conclusion

## Qu'est-ce que Chakra UI ?

Avez-vous déjà eu du mal à décider s'il fallait vous concentrer davantage sur le back-end ou le front-end de votre projet ? Croyez-moi, les deux sont tout aussi importants.

J'ai commencé à utiliser Chakra UI parce que je voulais me concentrer sur mon code back-end plutôt que de rester bloqué sur « Comment centrer un élément div ? ».

Chakra UI est extrêmement simple à utiliser, surtout si vous êtes familier avec l'utilisation des composants ReactJs.

## Comment démarrer et installer Chakra UI

Dans votre répertoire respectif, installez Chakra UI en utilisant Yarn ou NPM

`yarn add @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^4`

`npm i @chakra-ui/react @emotion/react@^11 @emotion/styled@^11 framer-motion@^4`

#### Pour React :
Pour que Chakra UI soit initialisé, vous devez d'abord ajouter `<ChakraProvider>` dans votre fichier `index.js`.
```js
import React from "react"

// 1. importer le composant `ChakraProvider` 
import { ChakraProvider } from "@chakra-ui/react"

function App({ Component }) {
 // 2. Utiliser à la racine de votre application
 return (
   <ChakraProvider>
     <Component />
   </ChakraProvider>
 )
}
```

#### Pour Next.js
Allez dans `pages/_app.js` et ajoutez les lignes de code suivantes :
```js
import { ChakraProvider } from "@chakra-ui/react"
function MyApp({ Component, pageProps }) {
 return (
   <ChakraProvider>
     <Component {...pageProps} />
   </ChakraProvider>
 )
}
export default MyApp
```
(Source : [Chakra UI Docs](https://chakra-ui.com/docs/getting-started))

> Vous pouvez consulter la documentation pour vérifier la prise en charge de Chakra UI pour d'autres bibliothèques : https://chakra-ui.com/docs/getting-started

## Personnalisation et fonctionnalités de Chakra UI

### Props de style
Chakra UI prend en charge ReactJs, et chaque composant est personnalisable à l'aide des props de style. Elles correspondent à presque toutes les propriétés CSS nécessaires disponibles.

Par exemple, pour `margin-top` en CSS, vous l'écririez ainsi :
`<Text mt={8} >`. Cela définira une marge supérieure de `8px` sur l'élément sélectionné.

Chakra UI s'inspire de la palette de couleurs de TailwindCSS, vous y trouverez donc toutes vos couleurs préférées !

### Comment surcharger le thème par défaut de Chakra UI
Vous pouvez surcharger le thème par défaut de Chakra UI et créer votre propre thème avec les couleurs de votre choix. Vous pouvez le faire en utilisant les variables CSS de Chakra UI.

Tout ce que vous avez à faire est de créer un nouveau fichier `theme.js` ou de modifier le fichier `index.js` existant sur React ou le fichier `_app.js` sur Next.js.

```js
// 1. Importer `extendTheme`
import { extendTheme } from "@chakra-ui/react"

// 2. Appeler `extendTheme` et passer vos valeurs personnalisées
const theme = extendTheme({
 colors: {
   brand: {
     100: "#f7fafc",
     // ...
     900: "#1a202c",
   },
 },
})

// 4. Maintenant, vous pouvez utiliser ces couleurs dans vos composants
function Usage() {
 return <Box bg="brand.100">Welcome</Box>
}
```
(Source : [Chakra Ui Docs](https://chakra-ui.com/docs/theming/customize-theme))

> Pour plus d'informations sur la surcharge du thème par défaut de Chakra UI, visitez la documentation de Chakra UI à l'adresse https://chakra-ui.com/docs/theming/customize-theme

### Styles réactifs (responsive)
Qu'en est-il de la réactivité ? Le plus gros casse-tête, du moins pour moi. Je n'aime pas cette partie, mais avec Chakra UI, ce n'est plus une grande souffrance.

Par exemple, considérez la ligne de code ci-dessous :

```js
<Box m={[2, 3]} />
```
(Source : [Chakra UI Docs](https://chakra-ui.com/docs/features/style-props))

Ainsi, en définissant cette valeur dans un tableau, le composant Box fera `8px` sur tous les viewports, et `16px` à partir du premier point de rupture.

Nous pouvons maintenant surcharger cela de plusieurs manières, dont l'une est plus facile à comprendre – en utilisant la syntaxe d'objet.

```js
<Text fontSize={{ base: "24px", md: "40px", lg: "56px" }}>
 Ceci est un texte réactif
</Text>
```
(Source : [Chakra UI Docs](https://chakra-ui.com/docs/features/style-props))

Ainsi, sur les petits écrans, la taille de police (`fontSize`) est de `24px`, sur les écrans de taille moyenne elle est de `40px`, et sur les grands écrans elle est de `56px`.

Vous avez peut-être remarqué que Chakra UI suit strictement la syntaxe ReactJs pour définir les styles en ligne en mettant une majuscule au second mot (c'est-à-dire `fontSize`) comme pour la propriété CSS `font-size` pour ses props de style également.

> Pour plus d'informations sur les styles réactifs, visitez la documentation de Chakra UI à l'adresse https://chakra-ui.com/docs/features/responsive-styles

### Composant Stack
Une autre fonctionnalité couramment utilisée que je n'aimais pas en CSS est la propriété `flex`. C'est un peu déroutant de comprendre comment cette propriété fonctionne.

Eh bien, j'ai l'honneur de dire ici – « Chakra UI à la rescousse 🚀 ! »

J'aimerais vous présenter le composant Stack.

Stack est un composant de mise en page simple que vous pouvez utiliser pour empiler des éléments, verticalement et horizontalement.

Il existe Stack, HStack (raccourci pour Horizontal Stack) et VStack (raccourci pour Vertical Stack). Vous l'avez probablement déjà deviné, mais HStack empilera les éléments horizontalement et VStack fera de même verticalement – mais surtout avec zéro CSS.

> Pour plus d'informations sur le composant Stack, visitez la documentation de Chakra UI à l'adresse https://chakra-ui.com/docs/layout/stack.

## Comment Chakra UI affecte votre score Lighthouse
![score-2](https://www.freecodecamp.org/news/content/images/2021/05/score-2.JPG)

Lorsque vous êtes enfin prêt à déployer une application web, vous devriez d'abord la passer par Google Lighthouse.

Google Lighthouse est un outil d'automatisation intégré à vos outils de développement Chrome. Il vous aide à effectuer des audits sur vos applications web et détermine un score basé sur leurs performances, l'accessibilité, les applications web progressives (PWA), le SEO, et bien plus encore.

Le mot auquel nous voulons prêter attention ici est l'Accessibilité.

### Qu'est-ce que l'accessibilité web ?

En tant que développeur, il est de notre responsabilité de rendre le web accessible à tous, et Google prend cette question très au sérieux.

Lorsque les sites web sont correctement conçus, cela aide tout le monde. Une conception appropriée signifie que, par exemple, les lecteurs d'écran doivent être capables de lire correctement les éléments de votre page à un utilisateur. Ces principes sont reflétés dans l'Initiative pour l'Accessibilité du Web (WAI).

Une bonne accessibilité ne profite pas seulement aux personnes handicapées. Elle est également utile aux utilisateurs de smartphones, de télévisions connectées, d'écrans de toutes tailles, aux personnes âgées qui pourraient ne pas très bien voir leurs écrans, aux utilisateurs daltoniens et aux personnes utilisant des connexions internet lentes.

Pour plus d'informations sur la WAI, vous pouvez visiter leur site officiel à l'adresse https://www.w3.org/WAI/.

### Quel est le rapport entre Chakra UI et l'accessibilité ?

Chakra UI suit toutes les normes établies par la WAI pour tous ses composants. Tout ce que vous avez à faire est d'ajouter la propriété `Aria-label` au composant Chakra.

C'est précisément ce que Chakra fait en coulisses pour vous aider pendant le processus de développement.

### Mais pourquoi devons-nous suivre la WAI de toute façon ? Et si nous ne le faisons pas ?

Comme je l'ai dit, Google prend l'accessibilité très au sérieux. Par conséquent, le moteur de recherche classera votre page en partie en fonction de votre score d'accessibilité. C'est pourquoi Lighthouse propose des audits dédiés à l'accessibilité.

## Comment utiliser le mode sombre dans Chakra UI

Le mode sombre est de plus en plus populaire ces jours-ci, et Chakra UI facilite son utilisation.

Supposons que vous soyez dans un projet React avec le fichier `index.js` ci-dessous :

```js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './components/App'
import { ChakraProvider } from '@chakra-ui/react'
 
ReactDOM.render(
  <ChakraProvider>
    <App />
  </ChakraProvider>,
  document.getElementById('root')
)
```

Tout ce que vous avez à faire pour initialiser le mode sombre sur votre site est d'apporter quelques modifications au fichier `index.js` et de créer un composant Button pour basculer en mode sombre.

Initialisons d'abord le hook pour basculer entre le mode sombre et le mode clair.

Allez dans le fichier `index.js` et tapez les lignes de code suivantes :

```js
import React from 'react'
import ReactDOM from 'react-dom'
import App from './components/App'
import { ChakraProvider, ColorModeScript } from '@chakra-ui/react'
 
ReactDOM.render(
  <ChakraProvider>
    <ColorModeScript initialColorMode="light" />
    <App />
  </ChakraProvider>,
  document.getElementById('root')
)
```

Le hook `ColorModeScript` suivra le mode actuellement défini sur le site.

Réglez la prop `initialColorMode` sur « light », « dark » ou « system ».

Maintenant, allez dans votre fichier `App.js`.

Installez react-icons en utilisant npm comme ceci :
`npm i react-icons`

Importez deux icônes React :
```js
import { FaMoon, FaSun } from 'react-icons/fa'
```

Importez le composant Chakra UI suivant et le hook `useColorMode`, puis initialisez le hook.

```js
import {IconButton, useColorMode } from '@chakra-ui/react

const { colorMode, toggleColorMode } = useColorMode()
```

Le hook est similaire au hook `useState`, sauf que `toggleColorMode` définira le thème du site en mode sombre ou clair de manière globale, tandis que `colorMode` stockera la valeur « light » ou « dark ».

Maintenant, intégrons le bouton d'icône et donnons au composant les props suivantes :

```js
<IconButton
    icon={colorMode === 'light' ? <FaSun /> : <FaMoon />}
    isRound="true"
    size="lg"
    alignSelf="flex-end"
    onClick={toggleColorMode}
/>
```

Maintenant, lorsque vous cliquez sur le bouton, le site devrait passer en mode sombre et basculer entre les deux icônes.

C'était facile, n'est-ce pas ?

## Conclusion
Chakra UI m'a aidé à booster mon processus de développement à un autre niveau. C'est très flexible, la documentation est excellente et il existe de nombreux modèles pré-construits pour vous aider à accélérer le processus.

Deux des modèles que je tiens à souligner sont [Choc UI](https://choc-ui.tech/) et [Chakra-Templates](https://chakra-templates.dev/).

Chakra UI possède également une communauté très active sur [Discord](https://discord.com/invite/dQHfcWF).

## Merci d'avoir lu jusqu'ici 🎉
Si vous avez aimé cet article, partagez-le avec vos collègues.
Je tweete sur mon parcours de développement en tant que développeur autodidacte, alors contactez-moi sur [Twitter](https://twitter.com/BrodasGeo).

D'ici là, passez une excellente semaine !