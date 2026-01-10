---
title: Comment détecter le schéma de couleurs préféré d'un utilisateur en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-18T16:54:59.000Z'
originalURL: https://freecodecamp.org/news/how-to-detect-a-users-preferred-color-scheme-in-javascript-ec8ee514f1ef
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QPIhIZte1bW0DKQoLoXwxw.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: Neo4j
  slug: neo4j
- name: General Programming
  slug: programming
- name: UX
  slug: ux
seo_title: Comment détecter le schéma de couleurs préféré d'un utilisateur en JavaScript
seo_desc: 'By Oskar Hane

  In recent versions of macOS (Mojave) and Windows 10, users have been able to enable
  a system level dark mode. This works well and is easy to detect for native applications.

  Websites have been the odd apps where it’s up to the website pu...'
---

Par Oskar Hane

Dans les versions récentes de macOS (Mojave) et Windows 10, les utilisateurs peuvent activer un mode sombre au niveau du système. Cela fonctionne bien et est facile à détecter pour les applications natives.

Les sites web ont été les applications étranges où c'est à l'éditeur du site web de décider quel schéma de couleurs les utilisateurs doivent utiliser. Certains sites web offrent un support de thème. Pour que les utilisateurs changent, ils doivent trouver la configuration et mettre à jour manuellement les paramètres pour chaque site web individuel.

Serait-il possible d'avoir cette détection faite automatiquement et d'avoir des sites web présentant un thème qui respecte la préférence de l'utilisateur ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*QPIhIZte1bW0DKQoLoXwxw.png)
_Thème Clair vs Sombre dans Neo4j Browser_

### Ébauche de la requête média CSS `prefers-color-scheme`

Il existe une ébauche de requêtes média CSS de niveau 5 où [prefers-color-scheme](https://drafts.csswg.org/mediaqueries-5/#descdef-media-prefers-color-scheme) est spécifiée. Elle est destinée à détecter si l'utilisateur a demandé au système d'utiliser un thème de couleur clair ou sombre.

Cela semble être quelque chose avec lequel nous pouvons travailler ! Nous devons rester à jour avec tout changement apporté à l'ébauche, cependant, car elle pourrait changer à tout moment puisque ce n'est qu'une... ébauche. La requête `prefers-color-scheme` peut avoir trois valeurs différentes : `light`, `dark`, et `no-preference`.

### Support des navigateurs web en mars 2019

Le support actuel des navigateurs est très limité et n'est pas disponible dans aucune des versions stables de quelque fournisseur que ce soit. Nous pouvons seulement en profiter dans [Safari Technology Preview de la version 12.1](https://developer.apple.com/safari/technology-preview/) et dans [Firefox 67.0a1](https://www.mozilla.org/en-US/firefox/67.0a1/releasenotes/). Ce qui est génial, c'est qu'il existe des binaires qui le supportent, donc nous pouvons travailler avec et l'essayer dans les navigateurs web. Pour le support actuel des navigateurs, consultez [https://caniuse.com/#search=prefers-color-scheme](https://caniuse.com/#search=prefers-color-scheme).

### Pourquoi la détection CSS seule n'est pas suffisante

L'approche courante que j'ai vue jusqu'à présent est d'utiliser une approche CSS uniquement et de remplacer les règles CSS pour certaines classes lorsqu'une requête média est correspondante. 

Quelque chose comme ceci :

```css
/* global.css */

.themed {
  display: block;
  width: 10em;
  height: 10em;
  background: black;
  color: white;
}

@media (prefers-color-scheme: light) {
  .themed {
    background: white;
    color: black;
  }
}

```

Bien que cela fonctionne bien pour de nombreux cas d'utilisation, il existe des techniques de stylisation qui n'utilisent pas CSS de cette manière. Si [styled-components](https://www.styled-components.com) est utilisé pour le thème, par exemple, alors un objet JS est remplacé lorsque le thème est changé.

Avoir accès au schéma préféré est également utile pour l'analyse et des remplacements CSS plus prévisibles ainsi qu'un contrôle plus fin sur les éléments qui doivent être thématiques ou non.

### Approche JS initiale

J'ai appris dans le passé que vous pouvez faire de la détection de requêtes média en définissant le CSS `content` d'un élément à une valeur si une requête média est correspondante. C'est définitivement un hack, mais ça marche !

Quelque chose comme ceci :

```css
/* global.css */

html {
  content: "";
}

@media (prefers-color-scheme: light) {
  html {
    content: "light";
  }
}

@media (prefers-color-scheme: dark) {
  html {
    content: "dark";
  }
}

```

Ainsi, lorsqu'un utilisateur charge le CSS et que la requête média correspond à l'un des schémas de couleurs ci-dessus, la valeur de la propriété `content` de l'élément `html` est définie sur 'light' ou 'dark'.

La question est alors, comment lire la valeur `content` de l'élément `html` ?

Nous pouvons utiliser [window.getComputedStyle](https://developer.mozilla.org/en-US/docs/Web/API/Window/getComputedStyle), comme ceci :

```js
const value = window
  .getComputedStyle(document.documentElement)
  .getPropertyValue('content')
  .replace(/\"/g, '')

// value est maintenant "dark", "light" ou une chaîne vide

```

Et cela fonctionne bien ! Cette approche est bien pour une **lecture unique**, mais elle n'est pas réactive et ne se met pas à jour automatiquement lorsque l'utilisateur change le schéma de couleurs du système. Pour être mis à jour, un rechargement de la page est nécessaire (ou avoir la lecture ci-dessus faite à intervalles réguliers).

### Approche JS réactive

Comment pouvons-nous savoir lorsque l'utilisateur change le schéma de couleurs du système ? Y a-t-il des événements auxquels nous pouvons écouter ?

Oui, il y en a !

Il existe [window.matchMedia](https://developer.mozilla.org/en-US/docs/Web/API/Window/matchMedia) disponible dans les [navigateurs web modernes](https://caniuse.com/#feat=matchmedia).

Ce qui est génial avec `matchMedia`, c'est que nous pouvons attacher un écouteur qui sera appelé chaque fois que la correspondance change.

L'écouteur sera appelé avec un objet contenant l'information si la requête média a commencé à correspondre ou si elle a cessé de correspondre. Avec cette info, nous pouvons sauter le CSS et travailler uniquement avec JS.

```js
const DARK = '(prefers-color-scheme: dark)'
const LIGHT = '(prefers-color-scheme: light)'

function changeWebsiteTheme(scheme) {
  // la chaîne 'dark' ou 'light' est dans scheme ici
  // donc le thème du site web peut être mis à jour
}

function detectColorScheme() {
  if (!window.matchMedia) {
    return
  }

  function listener({ matches, media }) {
    if (!matches) {
      // Ne correspond plus = pas intéressant
      return
    }

    if (media === DARK) {
      changeWebsiteTheme('dark')
    } else if (media === LIGHT) {
      changeWebsiteTheme('light')
    }
  }

  const mqDark = window.matchMedia(DARK)
  mqDark.addListener(listener)

  const mqLight = window.matchMedia(LIGHT)
  mqLight.addListener(listener)
}

```

Cette approche fonctionne très bien dans les navigateurs web supportés et se désactive simplement si `window.matchMedia` n'est pas supporté.

### Hook React

Puisque nous utilisons React dans [neo4j-browser](https://github.com/neo4j/neo4j-browser), j'ai écrit cela comme un hook React personnalisé pour faciliter la réutilisation dans toutes nos applications et s'intégrer dans le système React.

```js
// useDetectColorScheme.js
import { useState, useEffect } from 'react'

// Définir les thèmes disponibles
export const colorSchemes = {
  DARK: '(prefers-color-scheme: dark)',
  LIGHT: '(prefers-color-scheme: light)',
}

export default function useDetectColorScheme(defaultScheme = 'light') {
  // État du hook
  const [scheme, setScheme] = useState(defaultScheme)

  useEffect(() => {
    // Pas de support pour la détection
    if (!window.matchMedia) {
      return
    }

    // L'écouteur
    const listener = (e) => {
      // Pas de correspondance = pas intéressant
      if (!e || !e.matches) {
        return
      }

      // Rechercher le schéma de couleurs correspondant
      // et mettre à jour l'état du hook
      const schemeNames = Object.keys(colorSchemes)
      for (let i = 0; i < schemeNames.length; i++) {
        const schemeName = schemeNames[i]

        if (e.media === colorSchemes[schemeName]) {
          setScheme(schemeName.toLowerCase())
          break
        }
      }
    }

    // Boucler et configurer les écouteurs pour les
    // requêtes média que nous voulons surveiller
    let activeMatches = []
    Object.keys(colorSchemes).forEach((schemeName) => {
      const mq = window.matchMedia(colorSchemes[schemeName])

      mq.addListener(listener)
      activeMatches.push(mq)
      listener(mq)
    })

    // Supprimer les écouteurs, pas de fuites de mémoire
    return () => {
      activeMatches.forEach((mq) => mq.removeListener(listener))
      activeMatches = []
    }
    // Exécuter uniquement au premier chargement du hook
  }, [])

  // Retourner le schéma actuel depuis l'état
  return scheme
}

```

C'est un peu plus de code que dans la première preuve de concept courte. Nous avons une meilleure détection des erreurs et nous supprimons également les écouteurs d'événements lorsque le hook est démonté.

Dans notre cas d'utilisation, les utilisateurs peuvent choisir de remplacer le schéma détecté automatiquement par autre chose (nous offrons un thème en contour par exemple, souvent utilisé lors de présentations).

Et l'utiliser comme ceci dans la couche application :

```jsx
// App.jsx
import React from 'react'
import ThemeProvider from './ThemeProvider'
import useDetectColorScheme from './useDetectColorScheme'
export default function App({ configuredTheme, themeData, children }) {
  // Détecter le schéma et avoir 'light' comme défaut
  const autoScheme = useDetectColorScheme('light')

  // Vérifier si l'utilisateur veut remplacer le schéma détecté automatiquement
  const scheme = configuredTheme === 'auto' ? autoScheme : configuredTheme

  // Passer les données de thème à un composant fournisseur de thème
  return <ThemeProvider theme={themeData[scheme]}>{children}</ThemeProvider>
}

```

La dernière partie dépend de la manière dont le thème est créé dans votre application. Dans l'exemple ci-dessus, l'objet de données de thème est passé dans un fournisseur de contexte qui rend cet objet disponible dans toute l'application React.

### Résultat final

Voici un gif avec le résultat final, et comme vous pouvez le voir, c'est instantané.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dp2Nj97f12YMhEXuUiybTA.gif)

### Réflexions finales

C'était une expérience amusante réalisée lors d'une soi-disant « Journée de Labo » que nous avons dans l'équipe UX chez [Neo4j](https://neo4j.com). Les premiers stades de la spécification et (par conséquent) le manque de support des navigateurs ne justifient pas encore de l'intégrer dans un produit. Mais le support pourrait arriver plus tôt que prévu.

Et en plus, nous livrons certains produits basés sur Electron et il y a un `[electron.systemPreferences.isDarkMode()](https://github.com/electron/electron/blob/master/docs/api/system-preferences.md#systempreferencesisdarkmode-macos)` disponible là-bas...

### À propos de l'auteur

[Oskar Hane](https://twitter.com/oskarhane) est un chef d'équipe / ingénieur senior chez [Neo4j](https://neo4j.com). 
Il travaille sur plusieurs des applications et bibliothèques de code de Neo4j pour les utilisateurs finaux et a écrit deux livres techniques.

Suivez Oskar sur twitter : [@oskarhane](https://twitter.com/oskarhane)