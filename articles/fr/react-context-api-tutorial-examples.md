---
title: Comment utiliser l'API Context de React – Tutoriel avec exemples
date: '2024-07-22T15:25:40.000Z'
author: Danny
authorURL: https://www.freecodecamp.org/news/author/danny-adams/
originalURL: https://freecodecamp.org/news/react-context-api-tutorial-examples
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/React.png
tags:
- name: React
  slug: react
- name: React context
  slug: react-context
seo_desc: 'In React, data is typically passed down from parent to child via props.
  But this can lead to "prop drilling" – where we have to pass props down through
  lots of components to get them where they''re needed.

  Also, some props (for example, the current au...'
---


Dans React, les données sont généralement transmises du parent à l'enfant via des props. Mais cela peut mener au "prop drilling" – où nous devons faire passer des props à travers de nombreux composants pour les acheminer là où elles sont nécessaires.

<!-- more -->

De plus, certaines props (par exemple, l'utilisateur actuellement authentifié, le thème de l'interface utilisateur ou la langue préférée) seront requises par de nombreux composants au sein d'une application.

L'API Context de React fournit un moyen de partager des valeurs comme celles-ci entre les composants sans avoir à les transmettre explicitement comme une prop à chaque niveau de l'arborescence. Ainsi, Context est conçu pour partager des données qui peuvent être considérées comme "globales" pour un arbre de composants React.

## Ce que vous apprendrez dans cet article

-   [Qu'est-ce que l'API Context de React et quand l'utiliser ?][1]
-   [Exemple d'API Context React : comment basculer entre les thèmes d'interface clair et sombre][2]
-   [Comment créer plusieurs Contexts React (et pourquoi vous devriez le faire)][3]
-   [Comment prévenir le problème de re-rendu du Context React][4]
-   [API Context React vs Redux pour la gestion d'état global][5]

## Code source

Tous les exemples de cet article se trouvent dans ce dépôt : [https://github.com/DoableDanny/React-context-API-tutorial][6]

J'ai également réalisé une version vidéo de cet article pour vous permettre de suivre plus facilement les exemples : [React Context Tutorial with Examples  
][7]

## Qu'est-ce que l'API Context de React et quand l'utiliser ?

L'API Context est une fonctionnalité de React qui permet de partager des valeurs telles que des thèmes, des informations utilisateur ou des paramètres de configuration entre les composants sans avoir à passer explicitement des props à chaque niveau de l'arborescence des composants. Cela la rend particulièrement utile pour gérer l'état global, ou un état nécessaire à de nombreux composants à différents niveaux d'imbrication.

L'API Context fait partie de la bibliothèque React, ce qui signifie que vous n'avez pas besoin de l'installer en tant que package tiers dans une application React.

Ainsi, l'API Context peut être utilisée pour partager des variables globales entre les composants d'une application React, sans avoir à passer ces variables comme props le long de l'arborescence. C'est particulièrement utile s'il existe des composants profondément imbriqués qui ont besoin d'accéder à des variables provenant de composants situés plus haut.

Apprenons maintenant comment fonctionne l'API Context en examinant un exemple de cas d'utilisation courant...

## Exemple d'API Context React — Thème d'interface clair et sombre

Un cas d'utilisation réel très courant pour l'API Context de React est le stockage du thème préféré de l'utilisateur actuel – c'est-à-dire le "mode clair" ou le "mode sombre".

Pensez-y : de nombreux composants de l'interface utilisateur dans une application React devront connaître le thème actuel afin d'afficher les styles appropriés. Boutons, titres, barre de navigation, pied de page, menus déroulants – de nombreux composants vont devoir s'afficher différemment selon le thème actuel.

### La solution du passage de props

La manière la plus simple et la plus évidente de résoudre ce problème dans React serait de créer une variable `theme` dans le composant de haut niveau `App`, puis de continuer à la transmettre comme prop à tous les composants de l'arborescence. Mais cela conduit à un problème React connu sous le nom de "prop drilling".

Le "prop drilling" est un terme utilisé dans React pour décrire le processus de passage de données d'un composant parent à un composant enfant profondément imbriqué via plusieurs composants intermédiaires. Cela peut se produire lorsque vous devez transmettre un état ou des fonctions plusieurs niveaux plus bas dans l'arborescence des composants.

Exemple de prop drilling :

```jsx

function App() {
  const theme = 'dark';
  return <Parent theme={theme} />;
}

function Parent({ theme }) {
  return <Child theme={theme} />;
}

function Child({ theme }) {
  return <Button theme={theme} />;
}

function Button({ theme }) {
  return <button style={{ background: theme === 'dark' ? 'black' : 'white' }}>Click me</button>;
}

```

Comme vous pouvez le voir, chaque composant intermédiaire doit inclure la prop, même s'il ne l'utilise pas, juste pour la transmettre plus bas. Cela encombre le code et le rend plus difficile à comprendre.

De plus, les composants intermédiaires qui n'utilisent pas les props peuvent tout de même se re-rendre lorsque les props changent, ce qui entraîne des problèmes de performance. Cela peut être particulièrement problématique dans les grandes applications avec des arborescences de composants profondes.

### L'API Context à la rescousse

Nous pouvons résoudre ce problème de prop drilling en utilisant l'API Context.

#### Création d'un contexte

Tout d'abord, nous devons créer le contexte et passer le thème clair comme valeur par défaut :

```jsx
// src/contexts/ThemeContext.js

import { createContext } from "react";

export const themes = {
  light: {
    background: "white",
    text: "black",
  },
  dark: {
    background: "black",
    text: "white",
  },
};

export const ThemeContext = createContext(themes.light);
```

Ci-dessus, nous avons créé un dossier `contexts` à l'intérieur de notre dossier `src` pour stocker tous nos contextes. Il est considéré comme une bonne pratique de créer chaque contexte dans son propre fichier. Dans notre cas, nous avons juste besoin de créer un contexte pour stocker le thème actuel.

Notez que les contextes sont créés en appelant la fonction `createContext()` qui provient de la bibliothèque `React`. Nous passons à la fonction `createContext()` une valeur par défaut de `themes.light`.

#### Fournir un contexte

Ensuite, nous devons envelopper tous les composants qui ont besoin d'accéder au thème dans un fournisseur de contexte (Provider). Le fournisseur de contexte prend une prop `value`, où nous pouvons passer la valeur que nous voulons rendre globale.

Ci-dessous, `<Navbar />` et `<Button />` auront accès à l'état `theme`, même si nous ne l'avons pas explicitement transmis comme prop. C'est parce que nous avons enveloppé ces composants dans le fournisseur de contexte de thème, et lui avons passé la valeur (`theme`) qui doit être rendue globale.

```jsx
// src/App.js

import React, { useState } from "react"
import { ThemeContext, themes } from "./contexts/ThemeContext"
import Navbar from "./components/Navbar"
import Button from "./components/Button"

const App = () => {
  const [theme, setTheme] = useState(themes.light)

  const toggleTheme = () => {
    setTheme(state => (state === themes.light ? themes.dark : themes.light))
  }

  return (
    <div className="App">
      <ThemeContext.Provider value={theme}>
        <Navbar />
        <Button changeTheme={toggleTheme} />
      </ThemeContext.Provider>
    </div>
  )
}

export default App
```

Si nous voulions également rendre `setTheme()` disponible dans toute notre application via le contexte, nous pourrions passer l'objet suivant à la prop `value`. Nous serions alors capables de basculer le thème depuis n'importe quel composant au sein du Theme Context Provider :

```jsx
<ThemeContext.Provider value={{ theme, setTheme }}>
```

Créons maintenant les composants `Button` et `Navbar` qui consommeront le contexte de thème en utilisant le hook `useContext()`. Remarquez comment les styles CSS des composants changent en fonction des valeurs du thème actuel :

```jsx
// src/components/Button.js

import React, { useContext } from "react"
import { ThemeContext } from "../contexts/themeContext"

const Button = ({ changeTheme }) => {
  const theme = useContext(ThemeContext)

  return (
    <button
      style={{ backgroundColor: theme.background, color: theme.text }}
      onClick={changeTheme}
    >
      Toggle theme
    </button>
  )
}

export default Button
```

```jsx
// src/components/Navbar.js

import React, { useContext } from "react"
import { ThemeContext } from "../contexts/themeContext"

const Navbar = () => {
  const theme = useContext(ThemeContext)

  return (
    <nav style={{ backgroundColor: theme.background }}>
      <ul>
        <li style={{ color: theme.text }}>Home</li>
        <li style={{ color: theme.text }}>About</li>
      </ul>
    </nav>
  )
}

export default Navbar
```

**Voici les étapes impliquées dans l'utilisation d'un contexte** :

1.  Importez le contexte que vous souhaitez utiliser (`ThemeContext` dans cet exemple) dans le composant.
2.  Importez le hook `useContext` depuis `React`.
3.  À l'intérieur du composant qui a besoin d'accéder à la ou aux valeurs du contexte, appelez le hook `useContext` et passez le contexte que vous souhaitez utiliser. Assignez cela à une variable (`const theme = useContext(ThemeContext)` dans notre exemple).
4.  Le composant a maintenant accès à la variable globale, et le composant se re-rendra/sera mis à jour chaque fois qu'une valeur à l'intérieur du contexte est mise à jour.

D'accord, c'est tout ce dont nous avons besoin pour cet exemple. Lançons maintenant notre application en exécutant la commande suivante à la racine du projet :

`npm run start`

Testons maintenant les choses dans le navigateur.

Mode clair :

![light_mode](https://www.freecodecamp.org/news/content/images/2022/03/light_mode.JPG)

_\*\* Appuyez sur le bouton Toggle Theme \*\*_

Mode sombre :

![dark_mode](https://www.freecodecamp.org/news/content/images/2022/03/dark_mode.JPG)

Et voilà, nous avons utilisé l'API Context pour partager l'état du thème dans toute notre application – sans avoir à le transmettre comme une prop. Cool ! 👌

## Comment créer plusieurs Contexts React

Dans notre exemple ci-dessus, nous n'avons créé qu'un seul contexte, `ThemeContext`. Mais que se passerait-il si nous avions d'autres données devant être rendues globales, telles que le `username` et l' `age` de l'utilisateur actuellement connecté ?

Nous pourrions simplement créer un seul grand contexte pour stocker toutes les variables devant être consommées globalement :

```jsx
<OneBigContext.Provider value={{ theme, username, age }}>
  <Button changeTheme={toggleTheme} />
  <Navbar />
</OneBigContext.Provider>
```

Mais cela est considéré comme une mauvaise pratique, car chaque fois qu'une valeur de contexte est mise à jour, tous les composants consommant ce contexte seront re-rendus. Cela signifie que tous les composants qui n'ont besoin de connaître que le `theme`, et non les variables utilisateur, seront re-rendus chaque fois que l'une des variables utilisateur est mise à jour. Cela peut dégrader les performances d'une application, en particulier dans les applications plus grandes avec de nombreux composants complexes.

Nous pouvons résoudre ce problème en créant plusieurs contextes – un contexte pour le thème et un autre pour les données utilisateur – et en enveloppant notre application dans les deux fournisseurs, comme ceci :

```jsx
<ThemeContext.Provider value={theme}>
  <UserContext.Provider value={{ username, age }}>
    <Button changeTheme={toggleTheme} />
    <Navbar />
  </UserContext.Provider>
</ThemeContext.Provider>
```

En ne stockant que les données liées dans chaque contexte, nous aidons à prévenir les re-rendus inutiles de composants et améliorons les performances de notre application.

## Comment prévenir le problème de re-rendu du Context React

Comme nous l'avons discuté, chaque fois qu'une valeur de contexte est mise à jour, tous les composants consommant ce contexte seront re-rendus – même s'ils sont enveloppés dans `React.memo()`. (Si vous ne savez pas ce qu'est `React.memo()`, ne paniquez pas – nous en discuterons bientôt !) Cela peut dégrader les performances d'une application.

Mais nous pouvons atténuer ce problème avec les méthodes suivantes :

### 1\. Utiliser plusieurs Contexts React

C'est ce que nous avons discuté plus haut, et c'est la manière "préférée" de résoudre le problème de re-rendu ([voir cette réponse][8]).

### 2\. Diviser le composant et passer la valeur nécessaire

Vous pouvez également diviser le composant et transmettre (en tant que prop) la valeur nécessaire du contexte, avec les composants enfants enveloppés dans `React.memo()`. Exemple :

```jsx
const Card = () => {
  const appContextValue = useContext(AppContext);
  const theme = appContextValue.theme;

  return (
    <div>
      <CardTitle theme={theme} />
      <CardDescription theme={theme} />
    </div>
  );
};

const CardTitle = React.memo(({ theme }) => {
  return <h2 style={{ color: theme.text }}>This is the Title </h2>;
});

const CardDescription = React.memo(({ theme }) => {
  return <p style={{ color: theme.text }}>lorem ipsum dolor sit amet,</p>;
});
```

`React.memo()` est un composant d'ordre supérieur (HOC) dans React qui est utilisé pour optimiser les composants fonctionnels en empêchant les re-rendus inutiles. Il le fait en mémoïsant le composant, ce qui signifie qu'il ne se re-rendra que si ses props changent.

-   Sans `React.memo()` : Les composants `CardTitle` et `CardDescription` se re-rendraient chaque fois que leur parent, `Card`, se re-rend – même si leurs props n'ont pas changé. Cela peut entraîner des problèmes de performance dans les grandes applications ou avec des composants coûteux à rendre.
-   Avec `React.memo()` : `CardTitle` et `CardDescription` ne se re-rendent que si leurs props changent, réduisant ainsi les rendus inutiles et améliorant les performances.

Ainsi, en divisant le composant, en ne transmettant que les valeurs nécessaires sous forme de props et en enveloppant les composants dans `React.memo()`, `CardTitle` et `CardDescription` ne seront re-rendus que si `theme` est mis à jour, mais pas si `username` est mis à jour.

Cette solution est particulièrement utile si nous ne pouvons pas diviser le contexte pour une raison quelconque.

### 3\. Un seul composant avec `React.useMemo()` à l'intérieur

Ci-dessous, `theme` est une dépendance de `useMemo()`, donc nous n'obtiendrons un re-rendu des éléments retournés par la fonction de rappel que lorsque `theme` est modifié :

```jsx
const Card = () => {
  const appContextValue = useContext(AppContext);
  const theme = appContextValue.theme;

  return useMemo(
    () => (
      <div>
        <CardTitle theme={theme} />
        <CardDescription theme={theme} />
      </div>
    ),
    [theme]
  );
};

const CardTitle = ({ theme }) => {
  return <h2 style={{ color: theme.text }}>This is the Title </h2>;
};

const CardDescription = ({ theme }) => {
  return <p style={{ color: theme.text }}>lorem ipsum dolor sit amet,</p>;
};

```

Voici comment fonctionne `useMemo()` :

1.  Le premier paramètre de `useMemo()` est une fonction de rappel qui retourne une valeur mémoïsée. Dans ce cas, elle retourne un élément React, ou une arborescence d'éléments React.
2.  Le deuxième paramètre est un tableau de dépendances. Si l'une des valeurs de ce tableau de dépendances est mise à jour, alors la fonction de rappel fournie comme premier argument est appelée, et les éléments que la fonction de rappel retourne sont re-rendus.

Ainsi, `useMemo()` peut être utilisé pour ne re-rendre les éléments React que si certaines valeurs spécifiées dans le tableau de dépendances sont mises à jour.

En enveloppant ces éléments dans `useMemo()` et en spécifiant `theme` comme seule dépendance, les éléments ne sont re-rendus que si `theme` est mis à jour, mais ne seront pas re-rendus si une autre valeur de contexte est mise à jour.

Cette solution est également particulièrement utile si nous ne pouvons pas diviser le contexte.

## API Context React vs Redux

C'est un sujet très courant et très débattu au sein de la communauté React. L'API Context de React et Redux sont tous deux des outils pour gérer l'état dans une application React, mais ils ont des cas d'utilisation, des forces et des limites différents.

L'API Context est une fonctionnalité intégrée de React, dont l'objectif principal est de permettre le partage de l'état à travers une arborescence de composants React sans prop drilling.

L'API Context a une API simple : `React.createContext()`, `Provider`, et le hook `useContext()`. Elle est adaptée aux applications de petite à moyenne taille, car elle est simple à utiliser et nécessite peu de configuration et de code boilerplate.

D'un autre côté, Redux est une bibliothèque de gestion d'état qui doit être installée en tant que package tiers dans une application. Son objectif principal est de gérer l'état à l'échelle de l'application de manière prévisible, en particulier dans les applications volumineuses et complexes.

#### Pourquoi l'API Context est bonne pour les applications de petite à moyenne taille :

-   **Simplicité** : Elle est plus simple que Redux.
-   **Intégrée** : Elle fait partie de React, donc pas besoin d'installer des packages supplémentaires, ce qui facilite la maintenance du projet.
-   **Boilerplate minimal** : Nécessite moins de code répétitif et de configuration que Redux.

#### Pourquoi Redux est bon pour les applications plus grandes et plus complexes :

-   **Store unique** : Maintient un store unique pour l'état de toute l'application, ce qui facilite le débogage et les tests.
-   **Mises à jour d'état prévisibles** : Utilise des fonctions pures (reducers) pour gérer les mises à jour d'état, garantissant la prévisibilité et l'immuabilité.
-   **Support des middlewares** : Système de middleware puissant (comme redux-thunk ou redux-saga) pour gérer les actions asynchrones et les effets secondaires.
-   **Intégration DevTools** : Excellents outils de développement pour le débogage par voyage dans le temps (time-travel debugging) et l'inspection de l'état.
-   **Adapté aux grandes applications** : Conçu pour gérer une logique d'état complexe et des applications à grande échelle.

**Le mainteneur de Redux, [Mark Erikson][9], donne les raisons suivantes pour utiliser Redux** :

-   Modèles architecturaux cohérents
-   Capacités de débogage
-   Middleware
-   Extensions et extensibilité
-   Utilisation multiplateforme et multi-framework
-   Selon la configuration de votre application, de bien meilleures performances qu'en travaillant uniquement avec Context (nous n'avons pas à nous soucier du problème de re-rendu que nous rencontrons avec Context, mentionné ci-dessus – les composants ne se re-rendent que lorsque la valeur qu'ils utilisent est mise à jour)

#### En résumé :

-   Redux est un outil de gestion d'état plus complexe qui offre plus de fonctionnalités et d'outils. Il fournit un moyen cohérent de gérer l'état dans toute une application, ce qui est très utile sur les grands projets avec plusieurs développeurs (car ils n'implémenteront pas tous leurs propres styles de gestion d'état, rendant la base de code incohérente).
-   L'API Context de React est plus simple, nécessite moins de configuration et constitue une bonne solution pour les projets de petite à moyenne taille où la complexité et la surcharge liées à l'utilisation d'un outil comme Redux ne sont pas nécessaires.

## Merci pour votre lecture !

Si vous avez trouvé cet article utile, vous pouvez en apprendre davantage de ma part en :

-   [Vous abonnant à ma chaîne YouTube][10]. Je prévois d'en faire une chaîne axée sur React/NextJS/Node, avec des vidéos approfondies 😎.
-   [Me suivant sur Twitter][11] où je tweete sur mon parcours de freelance, mes projets personnels et mes apprentissages actuels.
-   [Consultant mon blog technique][12]

### Cours gratuit sur les Hooks React

Vous voulez apprendre tous les hooks de React ? J'ai créé une vidéo gratuite de 2 heures expliquant les 9 hooks principaux de React avec des exemples : [React Hooks Tutorial — All React Hooks Explained with Examples][13]. Si vous appréciez, n'hésitez pas à vous abonner à [ma chaîne][14].

Santé !

---

![Danny Adams](https://www.freecodecamp.org/news/content/images/size/w60/2022/01/prof-1.png)

Je suis un développeur web fullstack spécialisé dans React, NextJS, TypeScript, Node et PHP. Actuellement freelance à plein temps avec WordPress.

---

Si vous avez lu jusqu'ici, remerciez l'auteur pour lui montrer que vous appréciez son travail. Dites Merci

Apprenez à coder gratuitement. Le programme open source de freeCodeCamp a aidé plus de 40 000 personnes à obtenir des emplois de développeurs. [Commencer][15]

[1]: #heading-qu-est-ce-que-l-api-context-de-react-et-quand-l-utiliser
[2]: #heading-exemple-d-api-context-react-theme-d-interface-clair-et-sombre
[3]: #heading-comment-creer-plusieurs-contexts-react
[4]: #heading-comment-prevenir-le-probleme-de-re-rendu-du-context-react
[5]: #heading-api-context-react-vs-redux
[6]: https://github.com/DoableDanny/React-context-API-tutorial
[7]: https://www.youtube.com/watch?v=hkGiP6Ur-B4
[8]: https://github.com/facebook/react/issues/15156#issuecomment-474590693
[9]: https://x.com/acemarke?lang=en
[10]: https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA
[11]: https://twitter.com/doabledanny
[12]: https://www.doabledanny.com/blog/
[13]: https://www.youtube.com/watch?v=TXN6HYGLba4&ab_channel=DoableDanny
[14]: https://www.youtube.com/channel/UC0URylW_U4i26wN231yRqvA
[15]: https://www.freecodecamp.org/learn/