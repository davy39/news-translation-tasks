---
title: Apprenez React avec ce cours massif de 48 parties créé par une école de technologie
  de premier plan
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-28T15:58:24.000Z'
originalURL: https://freecodecamp.org/news/want-to-become-a-react-developer-947c9a6dbb76
coverImage: https://cdn-media-1.freecodecamp.org/images/1*B9uqLg7-TM2-bAIwa7Zxuw.png
tags:
- name: Front-end Development
  slug: front-end-development
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Apprenez React avec ce cours massif de 48 parties créé par une école de
  technologie de premier plan
seo_desc: 'By Per Harald Borgen


  _Click here to get to the course._

  Ever since we started creating courses on Scrimba, our users have asked us for a
  proper intro course on React. So when we finally got to it, we decided to make it
  our most comprehensive course ...'
---

Par Per Harald Borgen

![Image](https://cdn-media-1.freecodecamp.org/images/1*kI7-rNRdWKKPa22BQ6jytQ.png)
_[Cliquez ici pour accéder au cours.](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=glearnreact_launch_article)_

Depuis que nous avons commencé à créer des cours sur Scrimba, nos utilisateurs nous ont demandé un cours d'introduction propre sur React. Alors quand nous nous y sommes enfin mis, nous avons décidé d'en faire notre [cours le plus complet jamais créé.](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

Il s'appelle [Learn React](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) et il contient 48 chapitres au total — un mélange de cours et d'exercices interactifs.

%[https://twitter.com/perborgen/status/1067832208889651202]

C'est le cours d'introduction le plus complet jamais créé sur Scrimba. Il contient 48 chapitres au total — un mélange de cours et d'exercices interactifs.

L'homme derrière le cours est l'enseignant éminent Bob Ziroll. Bob est le Directeur de l'Éducation à [V School](https://vschool.io/), une école de technologie qui enseigne des cours complets sur JavaScript et l'UX.

V School est l'une des meilleures écoles de codage selon [Course Report](https://www.coursereport.com/best-coding-bootcamps), donc nous sommes super excités de nous associer avec eux.

Alors si vous aimez ce cours, assurez-vous de vérifier le programme immersif [full-stack](https://vschool.io/fullstack/) de V School. Maintenant, jetons un coup d'œil à la structure du cours !

### Partie 1. Introduction & Philosophie

Bob enseigne dans des bootcamps depuis 2014 et a développé sa propre philosophie d'apprentissage. Donc dans le premier screencast, nous nous familiariserons avec cette philosophie. Dans l'image ci-dessous, vous verrez l'essentiel.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2S7jU91WeeVGAA__NQth8g.png)

### Partie 2. Ce que nous allons construire

Dans la vidéo suivante, Bob donne un aperçu du cours, où il nous donne un rapide aperçu de deux projets que nous allons construire : une application simple de liste de tâches, qui couvre de nombreux sujets principaux de React ; et un projet final, qui sera une application de générateur de memes.

### Partie 3. Pourquoi React ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*kI7-rNRdWKKPa22BQ6jytQ.png)

Tout d'abord, Bob nous explique pourquoi nous devrions envisager d'utiliser quelque chose comme React au lieu d'écrire simplement en JavaScript pur et pourquoi tant de développeurs ont déjà choisi d'utiliser React.

### Partie 4. ReactDOM & JSX

Dans ce screencast, nous plongeons directement dans le code et écrivons notre Hello World en utilisant JSX — une extension JavaScript spécifique à React, afin que nous puissions écrire du HTML et du JavaScript en même temps !

```jsx
import React from "react"  
import ReactDOM from "react-dom"

ReactDOM.render(<h1>Hello world!</h1>, document.getElementById("root"))

```

Bob couvre également rapidement quelques pièges, comme les imports React corrects et le fait que JSX n'aime pas lorsque vous essayez de rendre deux éléments adjacents.

```jsx
// Hmm, je ne suis pas sûr de quel élément je devrais rendre ici...  
   ReactDOM.render(  
     <h1>Hello world!</h1>  
     <p>Je suis un paragraphe</p>,   
   document.getElementById("root"))

// C'est beaucoup mieux !  
   ReactDOM.render(  
     <div>  
       <h1>Hello world!</h1>  
       <p>Je suis un paragraphe</p>  
     </div>,   
   document.getElementById("root"))

```

### Partie 5. Pratique de ReactDOM & JSX

C'est notre première pratique de ce cours. Dans les screencasts de pratique, Bob nous donne un objectif et nous donne quelques indices.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rfsPYSNkwMA-ttqGH6u5Ag.png)

Bob nous encourage à passer du temps à réfléchir et à travailler sur ce défi et les suivants, car plus nous mettons d'efforts, plus nous pouvons nous souvenir de React.

À la fin, Bob montre et nous guide à travers la solution, mais ce blog ne donnera aucun spoiler ?, alors n'hésitez pas à le vérifier dans [le screencast réel](https://scrimba.com/p/p7P5Hd/cM7K3Hk?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article).

### Partie 6. Composants Fonctionnels

Dans ce cast, Bob nous donne un rapide aperçu des composants fonctionnels.

```jsx
import React from "react"  
import ReactDOM from "react-dom"

function MyApp() {  
  return (  
    <ul>  
       <li>1</li>  
       <li>2</li>  
       <li>3</li>  
    </ul>  
)}

ReactDOM.render(  
   <MyApp />,  
   document.getElementById("root")  
)

```

Nous définissons `MyApp()` comme une simple fonction JS qui retourne un élément de liste HTML très simple, mais c'est là que React se distingue car plus tard nous utilisons cette fonction comme élément HTML `<MyApp />` !

### Partie 7. Pratique des Composants Fonctionnels

Il est temps de pratiquer un peu plus.

![Image](https://cdn-media-1.freecodecamp.org/images/1*h1rFdXDsaD_3N3nKh_3BNA.png)

Comme dans le précédent cast de pratique, il n'y aura pas de spoilers ici, mais n'hésitez pas à [plonger directement dans le code](https://scrimba.com/p/p7P5Hd/cPLv2cZ?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) et à trouver votre propre solution. À la fin, Bob nous guide à travers comme avant.

### Partie 8. Déplacer les Composants dans des Fichiers Séparés

Dans ce chapitre, Bob nous donne quelques bonnes pratiques React courantes pour organiser le code, par exemple, nommer les fichiers avec des composants `MyInfo.js` de la même manière que le composant lui-même `<MyInfo />`.

Nous apprenons ensuite comment extraire les composants dans leurs propres fichiers séparés et comment les exporter pour les utiliser plus tard dans notre application.

```jsx
// MyInfo.js

import React from "react"  
function MyInfo() {  
  return (  
   // code du composant  
  )  
}

export default MyInfo

```

Nous pouvons ensuite simplement placer notre composant dans le dossier `components` et importer `<MyInfo />` dans `index.js`

```jsx
// index.js

import React from "react"  
import ReactDOM from "react-dom"

import MyInfo from "./components/MyInfo"

ReactDOM.render(  
   <MyInfo />,   
   document.getElementById("root")  
)

```

### Partie 9. Composants Parent/Enfant

Dans ce screencast, Bob parle des composants Parent et Enfant. Les applications régulières sont beaucoup plus complexes qu'un seul composant rendu dans le DOM. Au lieu de cela, nous avons généralement une hiérarchie complexe de composants.

Nous commençons par écrire notre composant fonctionnel `<App />` qui sera au sommet de la hiérarchie des composants

```jsx
// index.js

import React from "react"  
import ReactDOM from "react-dom"

import App from "./App"

ReactDOM.render(<App />, document.getElementById("root"))

```

Et dans le fichier `App.js` lui-même :

```jsx
// App.js

import React from "react"

function App() {  
  return (  
    <div>  
      <nav>  
        <h1>Bonjour une troisième fois !</h1>  
        <ul>  
          <li>Chose 1</li>  
          <li>Chose 2</li>  
          <li>Chose 3</li>  
        </ul>  
      </nav>  
      <main>  
        <p>C'est là que la plupart de mon contenu ira...</p>  
      </main>  
    </div>  
  )  
}

export default App

```

Comme vous pouvez le voir, nous pouvons écrire nos pages dans `<App />` mais cela va à l'encontre du but de React. Nous pouvons prendre chaque morceau de HTML et le mettre dans un composant séparé.

Voici à quoi pourrait ressembler notre `<App />` :

![Image](https://cdn-media-1.freecodecamp.org/images/1*CTJ4NU3XVU53licZiFurCw.png)

Dans React, les éléments HTML qui commencent par une majuscule indiquent un composant que nous avons créé

En utilisant ce concept, notre composant `<App />` ressemblerait à ceci :

```jsx
import React from "react"  
import MainContent from "./MainContent"  
import Footer from "./Footer"

function App() {  
  return (  
    <div>  
      <Header />  
      <MainContent />  
      <Footer />  
    </div>  
  )  
}

export default App

```

C'est beaucoup mieux et c'est une manière très propre d'organiser le code.

### Partie 10. Pratique des Composants Parent/Enfant

Il est temps de pratiquer. Voici la tâche que nous recevons de Bob, alors commençons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NxkmipjNqprMwLkEckeBMQ.png)

Comme d'habitude, pas de spoilers dans ce blog, alors n'hésitez pas à plonger dans la solution [dans le screencast de Bob.](https://scrimba.com/p/p7P5Hd/caQwRHM?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

Si vous n'êtes pas très sûr de par où commencer, Bob recommande de revoir les chapitres précédents d'abord et d'essayer de trouver une solution, même si elle n'est pas parfaite à ce stade. Ce serait la meilleure façon d'apprendre.

### Partie 11. Application Todo — Phase 1

Très bien ! Félicitations, nous avons maîtrisé les bases de React et cette fondation est suffisante pour commencer à construire notre première application réelle.

Tout d'abord, nous devons créer une structure pour notre application, et c'est une opportunité parfaite pour pratiquer ce que nous avons appris dans les screencasts précédents. Voici la tâche et [commençons.](https://scrimba.com/p/p7P5Hd/cVwzpCp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

![Image](https://cdn-media-1.freecodecamp.org/images/1*50Gm9c-XRI67WtKVGJBOkQ.png)

À ce stade, cela devrait être assez simple et Bob nous guide à travers la solution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Sj_r9rbQb0Ha4oFtc8OHfw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*2XfHnrp5DVQYnbNF5H3uoQ.png)

### Partie 12. Stylisation de React avec des Classes CSS

Dans ce cast, Bob nous introduit à la stylisation dans React. Il existe plusieurs façons de styliser les composants dans React, et nous commencerons par les classes CSS, car c'est celle avec laquelle la plupart d'entre nous devraient être vraiment familiers.

Commençons par un exemple simple. La structure de cet exemple est la même que dans le chapitre précédent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R8e7YRgaN8rVvK8YKnQJ4w.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*hZoSleZmE-c3EvKIcmdrBw.png)

Dans React, c'est très similaire au HTML pur, mais au lieu de `class`, nous devons utiliser `className` :

```jsx
function Header() {  
  return (  
    <header className="navbar">Ceci est l'en-tête</header>  
  )  
}

```

Beaucoup d'endroits vous diront que nous devons écrire `className` parce que `class` est un mot réservé en JS, mais la vérité est que sous le capot, JSX utilise l'API DOM JS vanilla.

```jsx
document.getElementById("something").className += "new-class-name"

```

Maintenant, nous pouvons simplement écrire du CSS pur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*bwANslPGNxTwPDUV5iP5RQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*RDIboVLpeoLSUKVG4tDigA.png)

### Partie 13. Quelques Mises en Garde

En aparté, Bob nous informe simplement de certains choix de style qu'il préfère personnellement, afin que nous soyons conscients qu'il existe une autre façon de faire les choses. Si vous souhaitez écrire du code légèrement différemment, vous êtes plus que bienvenu de le faire.

```jsx
// Bob aime éviter les points-virgules, lorsque c'est possible  
import React from 'react'

// mais il n'y a pas moyen de les éviter ici  
for (let i = 0; i < 10; i++) {}

// Bob préfère les fonctions régulières  
function App() {  
  return (  
    <h1>Bonjour le monde !</h1>  
  )  
}

// Bien que vous puissiez écrire des fonctions fléchées ES6 si vous le souhaitez  
const App = () => <h1>Bonjour le monde !</h1>

```

### Partie 14. JSX vers JavaScript et Retour

Avant d'aller plus loin, nous devons vraiment examiner comment JSX et JS interagissent. Nous voyons comment, à l'intérieur de nos fonctions JS, nous retournons quelque chose qui ressemble à du HTML, mais qui est du JSX.

Maintenant, que se passe-t-il si nous voulions utiliser une variable ? Nous pouvons le faire en utilisant `{}` :

```jsx
function App() {  
  const firstName = "Bob"  
  const lastName = "Ziroll"  
    
  return (  
    <h1>Bonjour {\`${firstName} ${lastName}\`} !</h1>  
  )  
}

```

`{}` est un moyen d'utiliser du JS pur dans JSX. En langage clair, cela ressemblerait à `<h1>Ceci est du JSX {maintenant nous écrivons du JS} et nous sommes de retour à JSX</h1>`

### Partie 15. Styles Inline avec la Propriété Style

Un truc très rapide pour appliquer des styles dans React est d'utiliser des styles inline.

```jsx
<h1 style={{color: "#FF8C00"}}>Bonjour le monde !</h1>

```

Remarquez comment nous utilisons deux ensembles d'accolades `{{}}`. Cela est dû au fait que React attend que les styles soient passés sous forme d'objet, mais nous devons également indiquer à JSX que nous utilisons des objets JS.

Il y a cependant un piège.

```jsx
// Cela va générer une erreur  
<h1 style={{background-color: "#FF8C00"}}>Bonjour le monde !</h1>

// Voici ce que nous devons faire, car JS n'aime pas les tirets au milieu de nos noms de propriétés  
<h1 style={{backgroundColor: "#FF8C00"}}>Bonjour le monde !</h1>

```

### Partie 16. Application Todo — Phase 2.

Dans ce screencast, nous allons reprendre là où nous nous sommes arrêtés avec la liste de tâches. Pour commencer, Bob nous demande de créer un composant `<TodoItem />` en extrayant le code suivant.

```jsx
<input type="checkbox" />  
<p>Texte de remplissage ici</p>

```

Et maintenant nous pouvons ajouter un peu de style et avoir une belle liste de tâches. Bientôt nous allons apprendre comment personnaliser le texte à l'intérieur de la balise `<p>`, mais avant cela, nous devons apprendre les props.

### Partie 17. Props Partie 1 — Comprendre le Concept

Regardons un peu de HTML pur et réfléchissons à ce qui ne va pas avec les éléments.

```jsx
<a>Ceci est un lien</a>  
<input />  
<img />

```

Aucun d'entre eux ne fait vraiment quelque chose d'important. Nous devons vraiment ajouter ces attributs à nos éléments.

```jsx
<a href="https://google.com">Ceci est un lien</a>  
<input placeholder="Prénom" name="firstName" type="text"/>  
<img src="https://goo.gl/dKwBew"/>

```

Très souvent, ces attributs sont appelés `properties` et si ce concept HTML a du sens pour vous, alors vous comprenez `props` dans React. Puisque nous créons nos propres composants, nous pouvons permettre aux `props` de modifier le comportement de nos propres composants.

### Partie 18. Props Partie 2 — Composants Réutilisables

Dans ce cast, Bob nous emmène sur YouTube pour illustrer le concept de composants réutilisables sur une simple vignette vidéo. Si elle était créée en React, nous ne ferions pas simplement un copier-coller d'une vignette sur toute la page, mais au lieu de cela, nous pourrions créer une seule vignette et nous assurer qu'elle peut changer en fonction des différentes propriétés telles que l'URL de l'image ou le titre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8dHohoFeUT49gFnZPxqypw.png)

### Partie 19. Props dans React

Dans ce screencast, Bob nous montrera comment combiner les concepts de props des parties 17 et 18 de ce cours et il a créé une application de liste de cartes de contact de base pour nous entraîner.

Pour commencer, ce serait vraiment bien de créer un composant pour une carte de contact et d'apprendre comment la rendre dynamique afin que nous puissions réutiliser un seul composant pour toutes les cartes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_WsaHhdMlb4LF5MZj0HZUA.png)

Une manière très React d'utiliser la carte de contact serait :

```jsx
// App.js  
...  
<ContactCard  
  name="Mr. Whiskerson"  
  imgUrl="http://placekitten.com/300/200"  
  phone="(212) 555-1234"  
  email="mr.whiskaz@catnap.meow"  
/>  
...

// au lieu de   
<div className="contact-card">  
  <img src="http://placekitten.com/300/200"/>  
  <h3>Mr. Whiskerson</h3>  
  <p>Téléphone : (212) 555-1234</p>  
  <p>Email : mr.whiskaz@catnap.meow</p>  
</div>

```

Créons `ContactCard` et utilisons `props` pour afficher dynamiquement les données.

```jsx
import React from "react"

function ContactCard(props) {  
  return (  
    <div className="contact-card">  
      <img src={props.imgUrl}/>  
      <h3>{props.name}</h3>  
      <p>Téléphone : {props.phone}</p>  
      <p>Email : {props.email}</p>  
    </div>  
  )  
}

export default ContactCard

```

### Partie 20. Pratique des Props et du Style

D'accord, pratiquons ! Comme dans les précédents casts de pratique, voici votre tâche :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_NfbLfH-KN4CutXNyppVcg.png)

Et comme c'est maintenant notre tradition, pour éviter tout spoiler et vraiment apprendre React, [plongez dans le guide de Bob.](https://scrimba.com/p/p7P5Hd/cbykBfa?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

Comme toujours, essayez de résoudre cette tâche par vous-même, et n'hésitez pas à vous référer aux chapitres précédents car ils contiennent tout ce dont vous avez besoin.

### Partie 21. Mapping des Composants

Donc, à partir de la session de pratique, vous avez peut-être remarqué que nous répétons quelques composants `<Joke />` et vous vous êtes peut-être demandé s'il existe un moyen de l'écrire une seule fois. Bien sûr ! Nous pouvons utiliser la méthode `.map` de JavaScript pour nous aider à atteindre cet objectif.

```jsx
function App() {

const jokeComponents = jokesData.map(joke => <Joke key={joke.id} question={joke.question} punchLine={joke.punchLine} />)

return (  
    <div>  
      {jokeComponents}  
    </div>  
  )  
}

```

Décomposons rapidement quelques éléments ici.

Très souvent, nos données proviennent d'une API, donc pour l'imiter, nous utilisons `jokesData` pour prétendre qu'il contient toutes les données dont nous avons besoin.

```jsx
const jokesData = [  
  {  
    id: 1,  
    punchLine: "Il est difficile d'expliquer les jeux de mots aux kleptomanes car ils prennent toujours les choses au pied de la lettre."  
  },  
  {  
    id: 2,  
    question: "Qu'est-ce qu'il y a de mieux en Suisse ?",  
    punchLine: "Je ne sais pas, mais le drapeau est un gros plus !"  
  },  
  ...  
]

```

Vous avez peut-être également remarqué dans `<Joke key={joke.id} ... />` la prop `key`. Il s'agit en réalité d'une exigence de React, selon laquelle chaque fois que vous créez un composant à plusieurs reprises, vous devez passer une prop `key` avec un paramètre unique. La plupart du temps, il s'agit d'un `id` que vous obtenez de votre API.

### Partie 22. Pratique du Mapping des Composants

Il est temps pour un autre cast de pratique. Voici votre tâche, et Bob a également eu la gentillesse de créer un peu de code de base pour nous, afin que nous n'ayons pas à tout créer à partir de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*95xsFlvFIj_m4upfWxpisA.png)

Comme toujours, n'hésitez pas à [parcourir la solution avec Bob](https://scrimba.com/p/p7P5Hd/c6b6Lfm?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article), mais essayez de le faire vous-même d'abord.

### Partie 23. Application Todo — Phase 3

Appliquons maintenant ce que nous avons appris sur le mapping et les props et rendons notre liste de tâches plus dynamique. Nous pouvons maintenant mapper les données des éléments et rendre `<TodoItem />` pour chaque élément de données que nous avons.

![Image](https://cdn-media-1.freecodecamp.org/images/1*HX3eHJ9nBQgrGkp8qn4hoA.png)

Et également utiliser les données comme props pour `<TodoItem />` et les placer où nous le souhaitons dans le composant lui-même.

![Image](https://cdn-media-1.freecodecamp.org/images/1*874VqCbV-r0L62uLDizjnQ.png)

Si à ce stade vous remarquez l'erreur suivante, `Warning: Failed prop type: You provided a `checked` prop to a form field...`, ne vous alarmez pas — nous avons tout fait correctement. Bob nous montrera ce que cela signifie et comment le résoudre dans la partie 31 de ce cours.

### Partie 24. Composants Basés sur les Classes

Dans ce chapitre, Bob nous présente les composants de classe dans React. Parfois, les composants fonctionnels que nous avons utilisés jusqu'à présent ne suffisent pas et leur fonctionnalité doit être étendue.

Nous en apprendrons davantage sur les différences sous-jacentes plus tard, mais pour l'instant, regardez comment ils diffèrent syntaxiquement et essayez de convertir notre `<App />` d'une fonction à un composant de classe.

```jsx
class App extends React.Component {  
  render() {  
    return (  
      <div>  
        <h1>Le code va ici</h1>  
      </div>  
    )  
  }  
}

```

### Partie 25. Pratique des Composants Basés sur les Classes

Encore un peu de pratique. Cette fois, nous avons du code écrit pour nous et nous devons pratiquer la conversion de composants fonctionnels en composants de classe. Dans cette pratique, nous avons également un petit bug caché dans le code, alors trouvons-le.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MidvJPKv95YO1xWPlvjh2Q.png)

Comme toujours, essayez de terminer cette pratique par vous-même d'abord, puis [suivez le guide de Bob.](https://scrimba.com/p/p7P5Hd/crV6eSv?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) À la prochaine partie !

### Partie 26. État

L'état est l'une des parties les plus importantes de React. Ce sont les données que le composant lui-même maintient. Les `props` ne peuvent pas être modifiées par un composant recevant les props, mais l'`état` peut ! Nous pourrions donc vouloir utiliser l'état lorsqu'un composant lui-même doit changer certaines données. Par exemple, lorsque nous cliquons sur un bouton, un texte dans notre composant change de couleur.

Un composant doit être un composant de classe pour avoir un état et nous devons avoir une méthode de constructeur.

```jsx
constructor() {  
  super()  
  this.state = {  
    answer: "Oui"  
  }  
}

```

Et ensuite nous pouvons utiliser ces données dans notre `return` et afficher nos données à l'intérieur de JSX.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EiRinOLwWN5iufS7Nvvp9g.png)

### Partie 27. Pratique de l'État

Dans cette session de pratique, nous avons un peu de débogage à faire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CSwTYIareIPUxqveYQAKMA.png)

Très souvent, nous devons corriger certains problèmes dans notre code, donc c'est une compétence très utile à pratiquer. Si vous êtes bloqué, n'hésitez pas à revoir certains des chapitres précédents avant de [suivre la solution de Bob](https://scrimba.com/p/p7P5Hd/c2NmZsa?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article).

### Partie 28. Pratique de l'État 2

L'état, comme nous l'avons mentionné précédemment, est un concept super important, donc Bob a inclus deux leçons de pratique pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DjUVqX9PLguNzmS4bG0lUQ.png)

Celle-ci peut être assez délicate, mais donnez-lui le meilleur de vous-même et ensuite regardez [comment Bob le fait.](https://scrimba.com/p/p7P5Hd/cewRpUQ?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

### Partie 29. Application Todo — Phase 4

Dans ce court cast, Bob nous montre comment utiliser l'état dans notre application Todo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*67X5Jm2RKxY3H-diZCIFYw.png)

### Partie 30. Gestion des Événements dans React

La gestion des événements consiste essentiellement à permettre à un utilisateur d'interagir avec votre page web et à faire quelque chose de spécifique lorsqu'un événement comme un clic sur un bouton ou un survol se produit.

Regardons un exemple simple d'exécution de cette fonction simple.

```jsx
function handleClick() {  
  console.log("J'ai été cliqué")  
}

```

Vous êtes peut-être déjà familier avec la façon dont cela se fait en HTML régulier :

```jsx
<button onclick="handleClick()">Cliquez-moi</button>

```

React est très similaire.

```jsx
<button onClick={handleClick}>Cliquez-moi</button>

```

La différence serait que le nom de l'événement `onClick` est en camelCase et `handleClick` est du JS passé à l'intérieur de notre JSX comme nous l'avons mentionné dans la leçon 14 sur les styles inline.

### Partie 31. Application Todo — Phase 5

Dans ce cast, Bob nous donne un défi. Vous vous souvenez de l'avertissement que nous recevons dans la console concernant la prop 'checked' ? Pour le résoudre, nous devons fournir un gestionnaire `onChange`. À ce stade, laissez-le simplement `console.log` ce que vous voulez.

Comme pour tous les défis habituels — [sautez dans le cast pour voir la solution.](https://scrimba.com/p/p7P5Hd/c9yP6uM?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

### Partie 32. Changement d'État

Nous pouvons mettre à jour l'état dans un composant en utilisant la méthode `setState()` de React.

Regardons comment nous pourrions l'utiliser sur un exemple très populaire — un compteur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XqL8-0haXmMN9pmycC3NAw.png)

Pour l'instant, lorsque vous cliquez sur le bouton « Changez ! », rien ne se passerait. Implémentons notre méthode `handleClick()`. Nous commençons par essayer d'afficher un nombre différent :

```jsx
handleClick() {  
  this.setState({ count: 1 })  
}

```

et le passons à notre `<button>`.

```jsx
<button onClick={this.handleClick}>Changez !</button>

```

Si nous exécutons cela, nous obtiendrons `Uncaught TypeError: Cannot read property 'setState' of undefined`. C'est une erreur très courante, et l'une des façons de faire fonctionner notre gestionnaire est de le lier.

```jsx
constructor() {  
  super()  
  this.state = {  
    count: 0  
  }  
  this.handleClick = this.handleClick.bind(this)  
}

```

Maintenant, nous voulons que notre méthode `handleClick()` soit dynamique et ajoute réellement 1 à notre état actuel. Heureusement, React nous fournit `prevState` afin que nous puissions comparer les états.

```jsx
handleClick() {  
  this.setState(prevState => {  
    return {  
      count: prevState.count + 1  
    }  
  })  
}

```

### Partie 33. Application Todo — Phase 6

Dans cette partie, nous allons faire en sorte que lorsque nous cliquons sur la case à cocher, elle change notre état et coche/décoche la case à cocher lorsque cela est nécessaire. Bob nous avertit que c'est une partie délicate de l'application et semble trompeusement simple. En tant que défi, essayons de l'implémenter nous-mêmes d'abord, mais pas besoin de s'inquiéter si quelque chose ne fonctionne pas tout à fait — [Bob nous soutient avec un guide.](https://scrimba.com/p/p7P5Hd/cgDqBHP?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article).

### Partie 34. Méthodes de Cycle de Vie Partie 1

L'une des choses agréables à propos de React est la façon dont nous écrivons essentiellement du JS vanilla et React s'occupe de beaucoup de choses en coulisses. Il existe un certain nombre de ces événements « en coulisses » qui se produisent pour un composant. C'est plus comme un ensemble de jalons dans la vie d'un composant, donc ils sont appelés **méthodes de cycle de vie**. Bob va couvrir les plus populaires et les plus importantes dans ce chapitre et les suivants.

La première que vous connaissez déjà est `render()`. Son travail est de déterminer ce qui est rendu à l'écran et React appelle `render()` lorsque quelque chose change comme `state` ou `props`.

La suivante est `componentDidMount()` qui est essentiellement comme « le composant est né ». Cette méthode est appelée lorsque le composant apparaît à l'écran. C'est un bon moment pour faire des appels API.

Une troisième méthode très intéressante est `shouldComponentUpdate()`. Parfois, React mettrait à jour un composant même si rien ne semblait changer. Cela pourrait devenir très coûteux dans certains cas et cette méthode nous donne, en tant que développeurs, une chance d'optimiser notre application.

Et la dernière méthode de ce chapitre est `componentWillUnmount()` et est un endroit pour nettoyer juste avant que votre composant ne disparaisse de l'écran de l'utilisateur. Vous pouvez supprimer des écouteurs d'événements ou annuler des appels API.

### Partie 35. Méthodes de Cycle de Vie Partie 2

Dans ce chapitre, [Bob couvre très rapidement](https://scrimba.com/p/p7P5Hd/cEkyPH2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) certaines des méthodes de cycle de vie obsolètes, que vous pourriez voir dans certaines applications React héritées, et il couvre également certaines méthodes vraiment rares, comme `getDerivedStateFromProps()` et `getSnapshotBeforeUpdate()`. Mais nous ne les couvrirons pas en profondeur car elles ne sont pas essentielles à ce cours.

### Partie 36. Rendu Conditionnel

Parfois, vous voulez afficher certaines données ou rendre du JSX uniquement à une certaine condition. C'est là que nous utilisons le rendu conditionnel.

L'un des points forts de React est qu'en utilisant du JS vanilla, nous pouvons préserver sa flexibilité pour écrire notre propre code. L'inconvénient est que lorsque vous apprenez React, il peut y avoir trop de façons différentes de faire la même chose. Le rendu conditionnel en est un exemple. Bob nous montrera quelques façons de le faire, mais soyez assuré, il y a autant de façons que de développeurs React.

Créons un composant `<Conditional />` qui rend « Chargement... » lorsqu'une page est en cours de chargement. Nous pouvons l'utiliser dans notre application dans la méthode `render`.

```jsx
render() {  
  return (  
    <div>  
      <Conditional isLoading={this.state.isLoading}/>  
    </div>  
  )  
}

```

Nous pouvons atteindre notre objectif en utilisant un simple if-else de JS :

![Image](https://cdn-media-1.freecodecamp.org/images/1*LHBYGxAoFeVzq5jeqaD_uQ.png)

Ou nous pouvons l'améliorer avec le dernier opérateur ternaire ES6.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hyG6iF2dQyQhlS0PrSJ-rg.png)

### Partie 37. Rendu Conditionnel — Pratique

Pratiquons maintenant. Le rendu conditionnel est l'un des outils essentiels dans la boîte à outils de tout développeur React.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2xr35TZVbIHPcCiiAKnQWw.png)

Essayez de donner le meilleur de vous-même avant de [parcourir la solution avec Bob.](https://scrimba.com/p/p7P5Hd/c893vh2?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

### Partie 39. Application Todo — Phase 7

Nous avons donc atteint la partie finale de notre application Todo et nous devons simplement terminer la partie finale du style et nous avons terminé ! Le défi pour cette partie serait de faire en sorte qu'un `<TodoItem />` terminé ait un aspect différent. Par exemple, avec un texte et/ou un arrière-plan grisés, en mettant le texte en italique. En tant que l'une des solutions, [Bob nous montrera comment le faire](https://scrimba.com/p/p7P5Hd/cKe27SD?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article), mais en fin de compte, cela dépend vraiment de nous.

### Partie 40. Récupération de données depuis une API

Dans ce cast, Bob nous a fourni un composant nu pour en apprendre davantage sur la récupération.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IPpXkcNjTxy5QDJ80JyuIA.png)

Dans le chapitre 24, nous avons appris que l'un des cas d'utilisation les plus courants pour la méthode de cycle de vie `componentDidMount()` est d'obtenir des données de quelque part afin que notre composant puisse effectuer la tâche qu'il est censé faire.

Dans cet exemple, nous utiliserons une API Star Wars gratuite pour récupérer certains noms de personnages. Écrivons notre méthode `componentDidMount()`, où nous allons récupérer certaines données et simplement les `console.log`.

```jsx
componentDidMount() {  
  fetch("https://swapi.co/api/people/1")  
    .then(response => response.json())  
    .then(data => console.log(data))  
}

```

![Données que nous avons obtenues de l'appel API](https://cdn-media-1.freecodecamp.org/images/1*sTxncw1bXhUbysRRFMCTZA.png)

Données que nous avons obtenues de l'appel API

D'accord ! Nous devons simplement extraire `name` de ces données et les stocker dans notre état pour ensuite les afficher dans le composant. À la fin, notre `<App />` devrait être :

![Image](https://cdn-media-1.freecodecamp.org/images/1*_ITXJuvSNEcdyfXLVqVraw.png)

Il y a quelques astuces intéressantes que nous pouvons apprendre de Bob.

Il est bon de créer un booléen `loading` dans l'état. Au cas où notre requête prendrait beaucoup de temps, nous pouvons simplement informer l'utilisateur que la requête est en cours de traitement et que ses données seront avec lui sous peu.

Nous créons une variable séparée `text` dans `render()` où nous faisons toute notre logique et nous avons un `return()` très propre, afin qu'il soit plus facile à comprendre pour le prochain développeur qui maintient notre code.

### Partie 41. Formulaires Partie 1

Dans ce cast, nous allons explorer comment les formulaires sont créés dans React. Les formulaires sont en réalité une partie très délicate de React. Tout d'abord, si vous n'avez pas terminé les défis des parties sur l'état dans React, ce serait le meilleur moment pour vous mettre à jour. Et en tant que préparation aux formulaires, Bob recommande de lire [la documentation officielle de React à leur sujet](https://reactjs.org/docs/forms.html).

Dans l'API DOM JS vanilla, vous créez un formulaire HTML. Une fois que l'utilisateur décide de le soumettre, vous rassemblez toutes les données de vos formulaires, presque à la dernière seconde, et vous les validez avant de les envoyer.

React préconise que vous gardiez une trace de vos données de formulaire au fur et à mesure, en les enregistrant dans l'état. À chaque frappe, vous avez la version la plus à jour du formulaire enregistrée dans l'état de votre composant de formulaire.

Il y a 3 parties clés aux formulaires dans React :

* Input — lorsque l'utilisateur met à jour l'input, nous déclenchons un gestionnaire d'événement (ligne 20)
* Gestionnaire d'événement — met à jour l'état avec les données de l'utilisateur (lignes 11–15)
* État — stockage pour vos données (lignes 6–8)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XlTMXOibXDD5sYJqipFDiA.png)

Pour un exemple plus complexe, où Bob montre quelques astuces pour rendre les formulaires très réutilisables et le code très lisible, [plongez dans le screencast.](https://scrimba.com/p/p7P5Hd/cW8Jdfy?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

### Partie 42. Formulaires Partie 2

Dans cette partie, Bob développe davantage nos connaissances sur les formulaires. Les formulaires peuvent gérer plus que simplement `<input />` ! Mais les choses peuvent devenir délicates. Nous apprenons comment gérer `<textarea />`, `<select />` et `<option />` pour les menus déroulants et nous développons davantage sur `<input />` pour en apprendre plus sur les cases à cocher et les boutons radio.

### Partie 43. Pratique des Formulaires

Super, maintenant il est temps de pratiquer.

Bob nous propose un nouveau défi et comme d'habitude, il est préférable d'essayer de le résoudre par nous-mêmes d'abord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ID_-WFwmHC9TwH5c8D3KwQ.png)

Si quelque chose ne fonctionne pas tout à fait, [Bob a toujours notre dos avec un excellent guide.](https://scrimba.com/p/p7P5Hd/ceLWEsp?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article)

### Partie 44. Architecture Conteneur/Composant

Dans ce cast, Bob introduit un modèle d'architecture React très populaire.

Très souvent, lorsque nous écrivons des composants complexes, nous finissons par avoir beaucoup de lignes de code dans un seul fichier. Nous commençons alors à faire défiler vers le haut et vers le bas pour ajouter des fonctionnalités supplémentaires et de la logique d'affichage. C'est là que la division Conteneur/Composant devient utile. Nous séparons nos préoccupations d'interface utilisateur et de logique métier en différents composants dans React. Il existe de nombreux termes différents : smart/dumb, container/presentational, tous ces termes font référence à la même idée de séparer les éléments rendus de la fonctionnalité de flux de données.

Dans notre exemple spécifique, nous pouvons implémenter le modèle conteneur/composant si nous extrayons notre HTML de la méthode `render()` dans un composant fonctionnel séparé `<FormComponent />` et notre `Form.tsx` devient `FormContainer.tsx`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QxlEv99mqSx0OXnZqzpl5Q.png)

Comme vous pouvez le voir, nous transmettons toujours nos gestionnaires et nos données en tant que props dans notre composant fonctionnel `<FormComponent />` et à l'intérieur du composant, nous appelons maintenant les gestionnaires et les données via les props.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-1kuN9m9FZJsoQem61w1Pw.png)

### Partie 45. Projet Final : Générateur de Mèmes

Vous l'avez fait ! Félicitations pour avoir atteint le projet final. Dans ce cast, Bob nous lance le défi ultime. Nous pouvons maintenant créer notre propre application, à partir de zéro.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PftHO0wbwiscfO9nmp7VcQ.png)

Si compléter tout le projet en une seule fois semble intimidant, Bob propose des mini-défis de guide [dans le screencast](https://scrimba.com/p/p7P5Hd/c6K77um?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) pour nous guider tout au long de la réalisation.

Bonne chance et bon codage !

### Partie 46. Écrire des Applications React Modernes

Bien joué ! Votre projet est maintenant prêt et vous pouvez le montrer à vos amis et à votre famille ! C'est vraiment quelque chose dont on peut être fier. Excellent travail !

Dans ce cast, Bob nous donne quelques conseils sur la façon de rester à jour avec tous les changements dans l'écosystème React et nous donne quelques astuces sur la façon dont les choses que nous avons apprises jusqu'à présent pourraient être faites légèrement différemment, comme l'utilisation de fonctions fléchées ES6 ou l'extraction de code dans de nouveaux composants pour améliorer la lisibilité.

### Partie 47. Idées de Projets pour Pratiquer

Dans ce cast, Bob discute de la suite à donner, là où le cours se termine. Il y a quelques idées et de bons articles à lire sur la façon de pratiquer ce que nous avons appris.

### Partie 48. Conclusion

Félicitations, nous l'avons fait ! Dans ce cast, nous faisons rapidement le bilan de ce que nous avons fait dans ce cours et nous esquissons ce que nous pouvons apprendre à l'avenir.

Merci beaucoup pour [le cours](https://scrimba.com/g/glearnreact?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article), Bob !

---

Merci d'avoir lu ! Je m'appelle Per Borgen, je suis le co-fondateur de [Scrimba](https://scrimba.com) — la manière la plus facile d'apprendre à coder. Vous devriez consulter notre [bootcamp de design web réactif](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&utm_medium=referral&utm_campaign=glearnreact_launch_article) si vous voulez apprendre à construire des sites web modernes à un niveau professionnel.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/bootcamp-banner.png)
_[Cliquez ici pour accéder au bootcamp avancé.](https://scrimba.com/g/gresponsive?utm_source=freecodecamp.org&amp;utm_medium=referral&amp;utm_campaign=glearnreact_launch_article)_