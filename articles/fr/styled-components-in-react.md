---
title: Comment utiliser les composants stylisés dans vos applications React
subtitle: ''
author: Kedar Makode
co_authors: []
series: null
date: '2023-05-04T14:19:57.000Z'
originalURL: https://freecodecamp.org/news/styled-components-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/Frame-390.png
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: styled-components
  slug: styled-components
seo_title: Comment utiliser les composants stylisés dans vos applications React
seo_desc: 'Styled-components is a library that allows you to write CSS in JS while
  building custom components in Reactjs.

  There are multiple options you can go with to style a React application. But the
  CSS in JS technique is good approach, where you write the ...'
---

Styled-components est une bibliothèque qui vous permet d'écrire du `CSS in JS` tout en créant des composants personnalisés dans `Reactjs`.

Il existe plusieurs options pour styliser une application React. Mais la technique `CSS in JS` est une bonne approche, où vous écrivez le code `CSS` directement dans le `fichier JavaScript`. Styled-components adopte cette approche.

Dans cet article, vous apprendrez à écrire du CSS en JS.

## Prérequis

Avant de commencer avec les composants stylisés, vous devez être familiarisé avec `React` et `CSS`.

## Comment créer une application React de base

Avant de commencer avec les composants stylisés, commençons par créer une application React en utilisant `create-react-app`.

```javascript
npx create-react-app NOM_DE_L_APPLICATION
```

Si vous n'êtes pas familiarisé avec create-react-app, vous pouvez [consulter ici](https://reactjs.org/docs/create-a-new-react-app.html) pour plus d'informations.

Une fois que votre modèle React est configuré, supprimez tous les fichiers du dossier `src` sauf `index.js` et `app.js`.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/ss1-2.png align="left")

Voici à quoi vos fichiers devraient ressembler une fois les étapes ci-dessus terminées. Il est maintenant temps de nettoyer `app.js` et `index.js`. `index.js` et `app.js` contiendront du code standard par défaut. Nous devons supprimer les éléments inutiles de ces fichiers. Après avoir supprimé les éléments inutiles, vos fichiers `app.js` et `index.js` devraient ressembler au code ci-dessous dans les fichiers respectifs.

`App.js`

```javascript
function App() {
    return(
    \t<div>
        \tComposants stylisés
        </div>
    )
}
```

`index.js`

```javascript
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'

const root = ReactDom.createRoot(document.getElementById('root'))
root.render(
\t<>
    \t<App />
    </>
)
```

Ouvrez maintenant la ligne de commande ou appuyez sur ctrl + `(backtick) pour l'ouvrir et tapez `npm start` pour démarrer votre application React.

Une fois que votre application fonctionne avec succès, arrêtez votre serveur en utilisant ctrl + c et installez styled-components. La commande pour installer styled-components est la suivante :

```javascript
npm install styled-components
```

## Stylisons notre premier composant

Nous allons créer une configuration de base pour vous aider à apprendre les composants stylisés. Dans app.js, créez un titre en utilisant une balise

# , un paragraphe en utilisant une balise et un bouton en utilisant la balise.`App.js function App() { return ( <div> <h1>Composants stylisés</h1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <button>Cliquez sur MOI !</button> </div> ); } export default App;`Avant de styliser notre composant, nous devons importer styled-components dans notre fichier `app.js` :`import styled from 'styled-components' function App() { return ( <div> <h1>Composants stylisés</h1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <button>Cliquez sur MOI !</button> </div> ); } export default App;`Nous allons maintenant créer notre **composant personnalisé** appelé H1 et l'utiliser à la place de la balise avec un style personnalisé.`` const H1 = styled.h1` color: red; font-size: 4rem; ` ``Tout d'abord, nous devons donner un nom personnalisé de notre choix. Ensuite, nous commençons par `styled.<NomDeLaBaliseHTML>` et enveloppons le style dans des backticks. Maintenant, lorsque nous utilisons ce composant personnalisé, il aura la propriété `<NomDeLaBaliseHTML>` avec le style.``import styled from 'styled-components' const H1 = styled.h1` color: red; font-size: 4rem; ` function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <button>Cliquez sur MOI !</button> </div> ); } export default App;``Voilà ! Voici notre premier composant stylisé personnalisé.**NOTE** : Utilisez toujours des lettres majuscules pour commencer le nom de votre composant personnalisé dans React, car c'est la convention React.

Si vous inspectez la page, vous verrez un nom de classe incompréhensible. Les composants stylisés font cela pour éviter les conflits de noms.

Maintenant, stylisons notre composant bouton :`` const DefaultButton = styled.button` background-color: #645cfc; border: none; padding: 10px; color: white; ` ``DefaultButton est notre nom de composant personnalisé. Après l'avoir stylisé, nous pouvons lui donner n'importe quelle balise HTML que nous désirons afin que ce composant personnalisé ait cette balise.

Nous allons maintenant utiliser DefaultButton que nous avons créé ci-dessus comme notre composant personnalisé dans React.js – mais en coulisses, ce sera la balise bouton de HTML comme nous l'avons mentionné dans le style en utilisant les composants stylisés.``import styled from 'styled-components' const H1 = styled.h1` color: red; ` const DefaultButton = styled.button` background-color: #645cfc; border: none; padding: 10px; color: white; ` function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <DefaultButton>Cliquez sur MOI !</DefaultButton> </div> ); } export default App;``Nous pouvons également garder nos fichiers propres en créant un fichier différent pour chaque composant différent dans les composants stylisés. Oui ! Nous pouvons faire cela ici.

Nous allons créer un nouveau dossier appelé `components` dans `src` et créer les fichiers `Title.js` et `Buttons.js` pour séparer le style du titre et des boutons.

Nous allons copier le style H1 et le coller dans `Title.js` et copier le style DefaultButton et le coller dans `Buttons.js`.

Dans `Title.js`, nous allons l'exporter par défaut. Mais dans `Buttons.js`, nous allons nommer l'export car nous allons créer plusieurs styles de boutons ici.

Lorsque nous exportons un composant par défaut, son import est un import régulier comme montré ci-dessous :`import H1 from './components/Title'`

Mais lorsque l'export est un export nommé (vous pouvez voir l'export nommé dans Button.js dans l'image ci-dessus), alors lors de l'import de ce composant, nous devons envelopper le nom du composant dans des accolades ({}) comme montré ci-dessous :`import {DefaultButton} from './components/Buttons'`

Maintenant, notre `App.js` ressemble à ceci :`import H1 from './components/Title' import {DefaultButton} from './components/Buttons' function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <DefaultButton>Cliquez sur MOI !</DefaultButton> </div> ); } export default App;`

Props dans les composants stylisés

Pour ceux d'entre vous qui connaissent les props de React, vous avez de la chance – les props dans les composants stylisés fonctionnent de manière similaire. Si vous ne savez pas ce que sont les props, ne vous inquiétez pas – je vais les introduire ici.

Maintenant, nous avons appris à créer des composants personnalisés dans les composants stylisés. Ces composants personnalisés peuvent avoir des attributs auxquels nous pouvons accéder dans les composants. Cela peut être un peu confus pour les débutants, mais regardons cela dans le code :`import H1 from './components/Title' import {DefaultButton} from './components/Buttons' function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <DefaultButton>Cliquez sur MOI !</DefaultButton> <DefaultButton red>Cliquez sur MOI !</DefaultButton> </div> ); } export default App;`

Dans le code ci-dessus, j'ai créé un autre bouton Default. Mais pouvez-vous voir la différence entre ces 2 boutons. Oui ! Nous avons quelque chose d'écrit après DefaultButton, qui est `red`. C'est ce qu'on appelle un attribut.

En accédant à l'attribut dans DefaultButton, nous pouvons changer le style en fonction de ces attributs. Faisons-le !`` import styled from 'styled-components' export const DefaultButton = styled.button` background-color: ${(props) => (props.red && 'red') || '#645cfc'}; border: none; padding: 10px; color: white; ` ``Nous sommes déjà dans un [littéral de gabarit (backticks)](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Template_literals). Nous pouvons donc écrire du JavaScript à l'intérieur. Nous avons utilisé le signe dollar ($) et des accolades pour écrire le JavaScript. Dans ces accolades, nous avons déclaré une [fonction fléchée](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Functions/Arrow_functions) qui a un paramètre props qui peut accéder aux attributs des composants personnalisés.

Ainsi, la fonction fléchée dit que si l'attribut **red** est donné, alors la couleur de fond doit être rouge, sinon elle doit être d'une couleur bleu-bleuet.`App.jsimport H1 from './components/Title' import {DefaultButton} from './components/Buttons' function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <DefaultButton>Cliquez sur MOI !</DefaultButton> <DefaultButton red>Cliquez sur MOI !</DefaultButton> </div> ); } export default App;`

Nous pouvons également déstructurer les props par le nom de l'attribut. Ci-dessus, nous avons donné à DefaultButton un attribut de red et nous y avons accédé avec `props.red`.

Au lieu d'y accéder avec `props.red`, nous pourrions déstructurer la prop avec {} et le nom de l'attribut. Reportez-vous au code ci-dessous pour bien comprendre.`` import styled from 'styled-components' export const DefaultButton = styled.button` background-color: ${({red}) => (red && 'red') || '#645cfc'}; border: none; padding: 10px; color: white; ` ``Maintenant, nous pouvons accéder aux props directement en tant que `red` plutôt que `props.red`.

Comment étendre les styles dans les composants stylisés

Nous savons comment écrire des composants stylisés personnalisés. Mais que faire si nous voulons utiliser le style DefaultButtons qui a plutôt une largeur de 100% du bouton ? Nous pouvons le faire en utilisant des styles étendus dans les composants stylisés.

C'est simple : nous devons simplement créer un nouveau composant dans `Buttons.js`. Et nous utiliserons `styled.<html Tag>`, au lieu de `styled(DefaultButton)`. Notre nouveau composant aura maintenant les styles de DefaultButton et certains nouveaux styles qui lui sont propres.``export const ExtendedButton = styled(DefaultButton)` display: block; width: 100vw; `App.jsimport H1 from './components/Title' import {DefaultButton, ExtendedButton} from './components/Buttons' function App() { return ( <div> <H1>Composants stylisés</H1> <p>Cillum culpa deserunt enim et eiusmod quis proident consequat tempor ipsum sunt esse.</p> <DefaultButton>Cliquez sur MOI !</DefaultButton> <ExtendedButton red>Cliquez sur MOI !</ExtendedButton> </div> ); } export default App;``Comment imbriquer les styles dans les composants stylisés

Nous pouvons écrire des styles plus complexes dans React en utilisant un composant personnalisé. Cela vous aidera encore plus et rendra le style simple. Reportez-vous au code suivant :``import styled from 'styled-components' function App() { return ( <div> <Wrapper> <h1>Un autre titre</h1> <p>Un autre paragraphe</p> <button>Un autre bouton</button> </Wrapper> </div> ); } const Wrapper = styled.div` h1{ text-align: center; color: violet; } p{ font-size: 40px; } button{ background-color: pink; padding: 4px 8px; border: none; } ` export default App;``Lorsque nous implémentons le composant wrapper, toutes les balises de paragraphe à l'intérieur du wrapper auront une taille de police de 40px et le bouton aura une couleur de fond rose, un remplissage comme mentionné, et aucune bordure. Cela vous aidera énormément lors de l'écriture de votre code.

Comment étendre les composants React

Nous pouvons également étendre les composants React en utilisant les composants stylisés. C'est assez similaire à l'imbrication des styles. Voici un exemple :``import React from 'react' import styled from 'styled-components' const Newcom = () => { return ( <div> <h2>Titre 2</h2> <button>Cliquez sur moi !</button> </div> ) } const Wrapper = styled(Newcom)` h2{ color: green; text-align: center; } button{ padding: 4px 10px; background-color: violet; border: none; } ` export default Wrapper``Lorsque nous écrivons des styles en utilisant les composants stylisés, nous devons simplement étendre les composants React comme nous étendons les styles. Lorsque nous étendons les styles, nous écrivons le nom du style étendu. Ici, nous écrirons le nom du composant à étendre comme montré dans le code ci-dessus.

Mais cela ne fonctionne toujours pas. Si nous inspectons, nous verrons notre HTML mais sans classe. Dans les composants React, il n'y a pas de classe. Vous devez donc ajouter des props au composant React et console.log() ces props.

Vous verrez notre nom de classe incompréhensible avec la paire clé:valeur, comme className : nom-de-classe-incompréhensible. Maintenant, en utilisant cela, nous allons déstructurer les props et donner un className à la div de ce composant de className. Reportez-vous à l'exemple ci-dessous :``import React from 'react' import styled from 'styled-components' const Newcom = ({className}) => { return ( <div className={className}> <h2>Titre 2</h2> <button>Cliquez sur moi !</button> </div> ) } const Wrapper = styled(Newcom)` h2{ color: green; text-align: center; } button{ padding: 4px 10px; background-color: violet; border: none; } ` export default Wrapper``Même après avoir utilisé les composants stylisés pour le style, vous pouvez utiliser le style global.

Rappelez-vous simplement que si votre style global et le style des composants stylisés sont les mêmes, React choisira le style des composants stylisés.

Variables CSS

Répéter la même couleur est ennuyeux. Et si j'ai du rouge à de nombreux endroits et que je veux maintenant que tout ce rouge soit changé en bleu ? C'est une tâche chronophage à faire manuellement, un par un.

Heureusement, les variables CSS viennent à notre secours. Créez maintenant un fichier `index.css` dans le dossier `src`. Importez-le dans `index.js`.`import './index.css';`

Nous allons maintenant écrire quelques variables CSS dans index.css qui sont des styles globaux accessibles de partout. La chose la plus intéressante est que nous pouvons avoir accès aux variables CSS dans les composants stylisés également.`index.css:root{ --primary-color: #8F00FF }`

Maintenant, `:root{}` est comme sélectionner `html{}` en CSS. Mais `:root{}` a plus de spécificité que `html{}`. Nous pouvons maintenant utiliser cette variable dans notre composant stylisé :`` const Wrapper = styled(Newcom)` h2{ color: green; text-align: center; } button{ padding: 4px 10px; background-color: var(--primary-color); border: none; } ` ``Comment ajouter un thème

De nos jours, les thèmes clairs et sombres sont très populaires. Nous pouvons le faire facilement dans les composants de style.

Tout d'abord, nous devons importer ThemeProvider des composants stylisés. Ensuite, nous envelopperons toute l'application dans ThemeProvider avec l'attribut theme dans lequel nous fournirons notre thème. Ensuite, nous pourrons le basculer avec React.`import styled, {ThemeProvider} from 'styled-components' import Sample from "./components/Sample"; const baseTheme = { background: '#fff', color: '#222', } const darkTheme = { background: '#222', color: '#fff', } function App() { return ( <ThemeProvider theme={darkTheme}> <p>Ceci est un paragraphe d'exemple</p> </ThemeProvider> ); }`

Nous n'avons toujours pas notre thème sombre. Pour cela, nous devons ajouter un nouveau composant stylisé personnalisé. Vous pouvez lui donner n'importe quel nom que vous voulez, mais je vais l'appeler `Container`.

Dans le conteneur, nous pouvons accéder au thème et à ses propriétés et aider l'utilisateur à changer la couleur de fond et la couleur du texte. Ce sont les seules choses majeures à changer entre le mode sombre et le mode clair.``import styled, {ThemeProvider} from 'styled-components' import Sample from "./components/Sample"; const baseTheme = { background: '#fff', color: '#222', } const darkTheme = { background: '#222', color: '#fff', } const Container = styled.div` color: ${(props) => props.theme.color}; background-color: ${(props) => props.theme.background}; ` function App() { return ( <ThemeProvider theme={darkTheme}> <Container> <p>Ceci est un paragraphe d'exemple</p> </Container> </ThemeProvider> ); }``Jetez un coup d'œil à notre `Container`. Nous accédons au thème et changeons la couleur et la couleur de fond lorsque le thème change. Et voici, une façon simple d'avoir des thèmes sur votre prochain projet.

Animation dans les composants stylisés

L'animation est importante dans le développement frontend. Nous allons apprendre à implémenter l'animation dans les composants stylisés avec un exemple.

Tout d'abord, nous devons importer keyframes de styled-components. Une fois cela fait, nous l'utiliserons pour créer des animations.``import styled, {keyframes} from 'styled-components' const spinner = keyframes` to{ transform: rotate(360deg); } ` const Loading = styled.div` width: 6rem; height: 6rem; border: 5px solid #ccc; border-radius: 50%; border-top-color: black; animation: ${spinner} 0.6s linear infinite; ` export default Loading``Dans le code ci-dessus, nous avons spinner dans lequel nous avons déclaré l'animation et spinner est le nom de l'animation. Dans loading, nous utilisons ce nom d'animation spinner afin que Loading utilise cette animation. Dans loading, j'ai utilisé une propriété raccourcie pour déclarer l'animation.

Comment utiliser `as` dans les composants stylisés

Si j'ai un bouton et que je lui donne un attribut `href` que nous utilisons pour lier à un autre site web, cela ne fonctionnera pas. Cela est dû au fait que l'attribut `href` appartient à la balise d'ancrage.`import React from 'react' import {DefaultButton} from './components/Buttons' const App = () => { return ( <div> <DefaultButton href="https://www.google.com">Cliquez</DefaultButton> </div> ) } export default App`

Mais dans les composants de style en utilisant `as`, nous pouvons faire en sorte que le composant donné agisse comme une balise HTML fournie comme valeur à `as`. Voyons cela en action.`import React from 'react' import {DefaultButton} from './components/Buttons' const App = () => { return ( <div> <DefaultButton as='a' href="https://www.google.com">Cliquez</DefaultButton> </div> ) } export default App`

Maintenant, DefaultButton est une balise d'ancrage (). Il aura text-decoration car dans la balise d'ancrage par défaut, il a text-decoration. Mais je suis sûr que maintenant vous pouvez résoudre cela. Lorsque nous cliquons sur notre DefaultButton, il ouvrira Google.

CSS et styled-components

Maintenant, nous pouvons donner directement des styles aux composants en utilisant CSS comme un objet du composant appelé `css props`.``import React from 'react' import styled from 'styled-components' const App = () => { return ( <div> <h2 css={`color: green`}>Bonjour le monde !!!</h2> </div> ) } export default App``

Mais le code ci-dessus ne fonctionnera pas. Parce que nous devons importer styled-components/macro pour activer la méthode de style qui utilise Babel. Consultez le code complet ci-dessous :``import React from 'react' import styled from 'styled-components/macro' const App = () => { return ( <div> <h2 css={`color: green`}>Bonjour le monde !!!</h2> </div> ) } export default App``

Fonctions d'assistance CSS dans les composants stylisés

Nous avons beaucoup appris sur les composants stylisés. Mais il existe des moyens plus efficaces de résoudre certains problèmes – et l'un d'eux est d'utiliser une fonction d'assistance CSS.

Supposons que vous vouliez un DefaultButton et un grand DefaultButton. D'après ce que nous avons appris jusqu'à présent, nous dirions que nous devrions donner large comme une prop et changer le style en fonction de cette prop.

Mais réfléchissez-y – nous devons apporter des modifications à plusieurs propriétés. Une fonction d'assistance CSS vient donc à notre secours.`` App.jsimport React from 'react' import styled from 'styled-components/macro' import {DefaultButton} from './components/Buttons' const App = () => { return ( <div> <DefaultButton>Bonjour</DefaultButton> <DefaultButton large>Bonjour</DefaultButton> </div> ) } export default AppButtons.jsimport styled, {css} from 'styled-components/macro' export const DefaultButton = styled.button` background-color: ${({red}) => (red && 'red') || '#645cfc'}; border: none; color: white; display: block; margin: 10px; ${({large}) => large? css` padding: 15px; font-weight: 800; ` : css` padding: 10px; font-weight: 400; `} ` ``Jetez un coup d'œil au code ci-dessus. Tout d'abord, nous avons passé une prop comme large depuis app.js dans le composant DefaultButton. Ensuite, en utilisant l'opérateur ternaire dans Button.js, nous avons stylisé le composant. Il dit que si `large` est donné comme prop, implémentez le premier style, sinon implémentez le second style. Cela suit le principe DRY (Don't Repeat Yourself).

Attributs par défaut (attrs) dans les composants stylisés

Nous avons des attributs sur certains éléments en HTML. Par exemple, sur un bouton, nous avons type="submit" ou type="button". Mais chaque fois, nous devons les définir manuellement.``import React from 'react' import styled from 'styled-components' const Button = styled.button` border: none; padding: 5px 10px; background-color: #87CD11; margin: 10px; ` const App = () => { return ( <div> <Button type="button">Cliquez !</Button> <Button type="submit">Soumettre</Button> </div> ) } export default App``

Ici, les attributs par défaut sont pratiques. Nous pouvons leur passer un objet ou une fonction. Mais si nous passons des objets aux attributs, ils seront alors statiques. Pour avoir un contrôle dynamique, nous passerons une fonction à l'attribut.``import React from 'react' import styled from 'styled-components' const Button = styled.button.attrs((props) => { return {type: props.type || "button"} })` border: none; padding: 5px 10px; background-color: #87CD11; margin: 10px; ` const App = () => { return ( <div> <Button>Cliquez !</Button> <Button type="submit">Soumettre</Button> </div> ) } export default App``

Dans le code ci-dessus, nous avons défini les attributs pour `button`. Cela dit que si le type est donné, il définira ce type aux props données – ou si aucune props n'est donnée, il le définira par défaut à button.

En tant que défi, vous pouvez aller de l'avant et utiliser une fonction d'assistance CSS pour définir un style différent en fonction du type de bouton.

**Conclusion**

J'espère que vous comprenez maintenant comment utiliser les composants stylisés dans vos projets. Faites-moi savoir ce que vous en pensez. Merci d'avoir lu !

Vous pouvez me suivre sur :

[Twitter](https://twitter.com/Kedar__98)

[LinkedIn](https://www.linkedin.com/in/kedar-makode-9833321ab/?originalSubdomain=in)

[Instagram](https://www.instagram.com/kedar_98/)