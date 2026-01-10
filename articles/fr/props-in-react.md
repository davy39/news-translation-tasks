---
title: Comment utiliser les Props dans React
subtitle: ''
author: Tooba Jamal
co_authors: []
series: null
date: '2023-01-10T16:01:03.000Z'
originalURL: https://freecodecamp.org/news/props-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/all-about-props-in-react-1.png
tags:
- name: React
  slug: react
seo_title: Comment utiliser les Props dans React
seo_desc: 'When you''re first learning React, props are often one of the most difficult
  topics to understand – especially when it comes to passing props across components.
  And when you need similar props in more than one component, things can get really
  tricky.

  ...'
---

Lorsque vous commencez à apprendre React, les props sont souvent l'un des sujets les plus difficiles à comprendre – surtout lorsqu'il s'agit de passer des props entre les composants. Et lorsque vous avez besoin de props similaires dans plus d'un composant, les choses peuvent devenir vraiment compliquées.

Dans ce guide, nous commencerons par comprendre ce que sont les props et ce qu'elles font. Nous examinerons les différents types de props et comment utiliser des props similaires dans plusieurs composants.

Il est utile de [comprendre l'état de React](https://beta.reactjs.org/learn/state-a-components-memory) avant de plonger dans ce guide.

## Qu'est-ce que les Props dans React ?

Props signifie propriétés. Ce sont des valeurs en lecture seule qui peuvent être passées entre les composants afin d'afficher des données pertinentes dans vos applications React. 

Prenons l'exemple d'une fonction JavaScript simple. Dans celle-ci, nous passons deux paramètres, a et b, pour les manipuler à l'intérieur de la fonction et retourner la somme des deux paramètres.

```javascript
function add(a, b) {
	const sum = a + b
    return sum
}
```

Lorsque nous passons une prop à un composant, la même chose se produit à l'intérieur du composant. Nous prenons les props, les manipulons et retournons quelque chose. Voir l'exemple ci-dessous :

```react.js
export default function App() {
	return <DummyComponent name="Tooba" a={5} b={2} />
}

function DummyComponent(props) {
	const sum = props.a + props.b
    
    return (
    	<>
        	<p>Mon nom est {props.name}</p>
            <p>La somme des props numériques que j'ai reçues est {sum}</p>
        </>
    )
}
```

Dans le code React ci-dessus, nous avons un composant App qui retourne DummyComponent et nous avons passé trois props (propriétés) à ce composant : name, a et b. 

Dans DummyComponent, nous recevons ces props en tant que paramètres de fonction et effectuons une simple addition entre a et b. Les props sont reçues sous forme d'objet avec des propriétés égales à ce que nous passons dans notre composant. 

L'objet props pour notre exemple ressemblerait à {name: "Tooba", a: 5, b: 2}. Par conséquent, nous devons récupérer les propriétés dont nous avons besoin comme nous le faisons dans les objets JavaScript réguliers. 

`const sum = props.a + props.b` récupère les propriétés a et b de notre objet props et stocke leur somme dans la variable sum. Ensuite, nous retournons deux balises <p>, l'une affichant notre prop name et l'autre affichant la somme. Le résultat rendu à l'écran ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/reactss.png)
_Capture d'écran montrant le résultat rendu (« Mon nom est Tooba / La somme des props numériques que j'ai reçues est 7. »)_

Et si je console.log le DummyComponent, j'obtiens une fonction ayant les props passées en tant que paramètre exactement comme nous l'avons discuté ci-dessus. Voir le code ci-dessous :

```react.js
export default function App() {
	console.log(DummyComponent)
	return <DummyComponent name="Tooba" a={5} b={2} />
}

function DummyComponent(props) {
	const sum = props.a + props.b
    
    return (
    	<>
        	<p>Mon nom est {props.name}</p>
            <p>La somme des props numériques que j'ai reçues est {sum}</p>
        </>
    )
}
```

Le résultat rendu sur la console est :

![Sortie du code journalisant DummyComponent sur la console](https://www.freecodecamp.org/news/content/images/2023/01/FunctionalComponent.png)
_Sortie du code journalisant DummyComponent sur la console_

## Comment les Props sont partagées entre les composants dans React

Les props sont généralement passées d'un composant parent à un composant enfant. Un composant parent est un composant dans lequel vous importez un autre composant et passez des props à l'intérieur.

Dans l'exemple ci-dessus, App est notre composant parent. Donc, pour passer des props au composant enfant, nous devons d'abord l'importer dans App.js. C'est pourquoi nous avons importé DummyComponent dans App.js et ensuite passé les props dont nous avions besoin à l'intérieur `<DummyComponent name="Tooba" a=5 b=2/>`.

Mais l'application n'est pas toujours le seul composant parent de tous les autres composants.

Supposons que nous avons un autre composant où nous voulons maintenir un état et l'utiliser dans un autre composant. Dans une telle situation, le composant où nous maintenons l'état pour le passer à un autre composant devient le parent de ce dernier composant et le composant d'application devient le grand-parent.

Voir l'exemple ci-dessous pour comprendre ce que je veux dire :

```react.js
import React from "react"

export default function App() {
	return <DummyComponent name="Tooba" a={5} b={2}>
}

function DummyComponent(props) {
	const sum = props.a + props.b
    
    return (
    	<>
        	<p>Mon nom est {props.name}</p>
            <p>La somme des props numériques que j'ai reçues est {sum}</p>
        </>
    )
}

function Parent() {
  const [isParent, setIsParent] = React.useState(true)

  return (
    <>
      <Child isParent={isParent}/>
    </>
  )
}

function Child(props) {
  return (
    <>
      <h3>{props.isParent 
      ? "Je suis le composant enfant de Parent.js" 
      : "Il pourrait y avoir un bug"}</h3>
    </>
  )
}


```

Dans le code ci-dessus, nous avons ajouté deux nouveaux composants. `Parent.js` maintient l'état `isParent`. Il indique si c'est un composant parent ou non. Si l'état est vrai, nous affichons "Je suis le composant enfant de Parent.js" dans le fichier Child.js. Sinon, nous affichons "Il pourrait y avoir un bug".

Mais pour afficher cela dans le navigateur, nous devons importer Parent.js dans App.js et le retourner à l'intérieur de la fonction App. Le code est affiché dans le navigateur comme ceci :

![Sortie affichée dans le navigateur basée sur la prop isParent passée du parent au composant enfant](https://www.freecodecamp.org/news/content/images/2023/01/parent-component.png)
_Sortie affichée dans le navigateur basée sur la prop isParent passée du parent au composant enfant_

Peu importe la taille de votre application React, les composants enfants doivent toujours être importés dans le composant parent et le composant parent dans le composant grand-parent (s'il existe).

## Qu'est-ce que PropTypes dans React ?

Il existe une bibliothèque dans React appelée "prop-types" qui nous permet d'éviter les erreurs causées par des problèmes de type de données invalides.

Supposons que vous voulez qu'une variable soit de type Number, mais lorsque vous essayez de la manipuler mathématiquement, elle génère des erreurs. Vous avez peut-être rencontré ce problème de nombreuses fois dans votre parcours de codage.

Mais avec propTypes dans React, nous pouvons nous assurer que chaque prop est d'un certain type de données et rien d'autre.

Considérons le DummyComponent de l'exemple ci-dessus :

```react.js
import { PropTypes } from "prop-types"

function DummyComponent(props) {
	const sum = props.a + props.b
    
    return (
    	<>
        	<p>Mon nom est {props.name}</p>
        	<p>La somme des props numériques que j'ai reçues est {sum}</p>
        </>
    )
}

DummyComponent.propTypes = {
		a: PropTypes.number,
    	b: PropTypes.number
}
```

Pour utiliser propTypes, nous l'importons d'abord et définissons `propTypes` avec le nom égal à notre composant. Les propTypes sont des objets avec des clés égales à nos noms de props et des valeurs égales au type de données que nous voulons pour cette prop.

Nous pouvons également chaîner `propTypes` avec `isRequired` qui génère une erreur si la prop requise n'est pas fournie au composant.

```react.js
DummyComponent.propTypes = {
		a: PropTypes.number,
    	b: PropTypes.number.isRequired
}
```

Les types de données disponibles pour propTypes sont String, Number, Boolean, Object, Function et Symbol.

## Comment mettre à jour les Props à partir d'un composant enfant

Même si les props sont généralement passées aux composants enfants et sont des éléments de données en lecture seule, nous avons un moyen de mettre à jour une prop à partir du composant enfant. Et ce n'est pas aussi compliqué que cela peut paraître. Passons en revue cela étape par étape :

1. Passer `setState` en tant que prop au composant enfant
2. Ajouter un événement dans le composant enfant qui déclenche la fonction `setState`

Regardons le code qui fait fonctionner cela :

```react.js
function Parent() {
  const [isParent, setIsParent] = React.useState(true)

  return (
    <>
      <Child isParent={isParent} 
      changeIsParent={isParent => 
      setIsParent(isParent => !isParent)}/>
    </>
  )
}

function Child(props) {
  return (
    <>
      <h3>{props.isParent 
      ? "Je suis le composant enfant de Parent.js" 
      : "Il pourrait y avoir un bug"}</h3>
      <button onClick={() => props.changeIsParent()}>Cliquez-moi</button>
    </>
  )
}
```

Dans le code ci-dessus, nous avons passé une prop nommée `changeIsParent` qui met à jour l'état `isParent` en utilisant la fonction `setIsParent`.

Dans le composant enfant, nous avons ajouté un bouton et passé un événement onClick qui exécute la fonction `changeIsParent` à chaque clic. Puisque l'état de `isParent` change continuellement à chaque clic, le texte à l'intérieur de la balise <h3> change en conséquence.

## Comment utiliser le Hook useContext à la place

Lorsque vous commencez à construire des applications React plus grandes, il devient frustrant de passer des props dans la hiérarchie des composants React, surtout lorsque des composants avec différents parents ont besoin des mêmes props. Regardons le diagramme ci-dessous pour comprendre cela :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/prop-hierarchy.png)
_Exemple de hiérarchie d'application React_

Supposons que le composant enfant central dans le diagramme a besoin de certaines props de son parent. Nous pouvons répondre à ce besoin en maintenant un état dans son composant parent et en le passant à l'enfant en tant que prop.

Mais, que se passe-t-il si le composant parent le plus à gauche a besoin de la même prop ? Nous pouvons définir le même état dans son parent (grand-parent dans le diagramme) et le passer en tant que prop.

Encore, le composant grand-parent le plus à droite a également besoin de la même prop. Nous pouvons résoudre ce problème en maintenant l'état dans le composant App et en le passant à travers ses enfants.

Cette approche peut sembler fonctionner. Mais nous devons passer des props inutilement à chaque composant enfant, qu'ils en aient besoin ou non.

Le terme "prop drilling" décrit ce problème de passage de données à travers tous les enfants, qu'ils en aient besoin ou non. Heureusement, vous pouvez utiliser le hook useContext dans React pour résoudre ce problème en maintenant un état globalement et en le passant aux composants qui en ont besoin.

Comprenons comment faire cela avec useContext à travers une approche étape par étape :

1. Créer un fichier Context.js et créer le contexte dedans
2. Maintenir un état global dans le composant Context nouvellement créé
3. Passer cet état en tant que valeur au fournisseur de Contexte
4. Envelopper le composant App ou le parent commun le plus bas à l'intérieur du fournisseur de Contexte
5. Accéder à l'état global à travers les composants qui en ont besoin

Maintenant, supposons que nous construisons un jeu dans React et que nous devons basculer l'affichage du score de l'utilisateur dans plusieurs composants. Pour cela, nous maintenons un état `showScore` dans le composant Context.js comme ci-dessous

```react.js
import {useState, createContext} from "react"
const Context = createContext()

function ContextProvider(props) {
    const [showScore, setShowScore] = useState(false)

    function toggleScore() {
        setShowScore(!showScore)
    }

    return (
        <Context.Provider value={{showScore, toggleScore}}>
            {props.children}
        </Context.Provider>
    )
}

export {ContextProvider, Context}
```

Dans la première ligne, nous importons l'état et le contexte de React. Dans la ligne 2, nous créons un contexte nommé Context. Dans la ligne 4, nous créons une fonction nommée `ContextProvider`. Dans la ligne 5, nous initialisons l'état `showScore` et dans la ligne 7, nous définissons une fonction qui bascule l'état `showScore`. Dans la ligne 12, cette fonction retourne le fournisseur de contexte qui permet aux enfants d'accéder à son état et de lui passer une valeur.

La valeur peut être une seule valeur ou un objet ayant plusieurs valeurs. Puisque nous avons un état et une fonction à passer aux enfants, nous utilisons un objet pour définir notre valeur ayant à la fois l'état et la fonction qui bascule l'état `showScore`.

Enfin, nous exportons la fonction `ContextProvider` et Context en tant qu'exportations nommées.

Vous vous demandez peut-être, pourquoi notre composant de contexte reçoit-il des props et pourquoi les passons-nous à notre fournisseur de contexte ? Nous y reviendrons dans un instant – voyons d'abord quelle serait notre prochaine étape

Pour rendre notre contexte accessible dans toute notre application, nous devons envelopper le composant App à l'intérieur du composant `ContextProvider` dans le fichier `main.js`/ `index.js` :

```react.js
import React from 'react'
import App from './App'
import { ContextProvider } from './Context'

ReactDOM.createRoot(document.getElementById('root')).render(
  <ContextProvider>
     <App />
  </ContextProvider>
)
```

Dans le code ci-dessus, nous importons ContextProvider du composant Context et enveloppons `<App />` à l'intérieur. Chaque enfant du composant qui est enveloppé à l'intérieur du Context Provider peut accéder au contexte global. Nous avons passé `<App />` à l'intérieur de `<ContextProvider>` afin que chaque composant enfant de notre application puisse accéder à `showScore` et `toggleScore`.

Maintenant que le contexte est disponible pour être utilisé dans toute l'application, voyons comment nous pouvons l'utiliser :

```react.js
import { Context } from './Context'
import {useContext} from 'react'

function ScoreDisplay(props) {
	const {showScore} = useContext(Context)
    return (
    	{showScore && <h3>Votre score est {props.score}</h3>}
    )
}

function ScoreToggle() {
	const {toggleScore} = useContext(Context)
    	return (
    	<button onClick={displayScore}>Afficher les scores</button>
    )
}

```

Voyez comment nous devons simplement importer Context du composant Context et accéder à la valeur dont nous avons besoin pour l'utiliser dans n'importe quel composant.

Dans le composant ScoreDisplay, nous déstructurons `showScore` de Context et affichons le score en conséquence. Dans la fonction `ScoreToggle`, nous déstructurons `toggleScore` et le passons au gestionnaire d'événements onClick.

Pour résumer, nous avons créé un composant de contexte séparé et créé un contexte en utilisant le hook `createContext`. À l'intérieur du composant, nous définissons les états et les fonctions que nous voulons maintenir globalement et retournons `Context.Provider` à partir du Contexte que nous avons créé. Ensuite, nous exportons le composant de contexte et le Contexte que nous avons créé en utilisant le hook `createContext`.

`Context.Provider` prend une valeur qui peut être un objet ayant plusieurs paires clé-valeur. Nous avons passé à la fois notre état et la fonction de basculement à la valeur. Nous avons ensuite enveloppé le composant App à l'intérieur de `ContextProvider` dans le fichier `main.js`/ `index.js`.

Ensuite, nous devons importer le composant Context et le hook useContext partout où nous avons besoin de l'état global et déstructurer l'objet de valeur selon nos besoins.

Maintenant, revenons aux props que notre composant de contexte reçoit. Voyez comment dans le deuxième exemple de code nous passons `<App />` à l'intérieur du composant `<ContextProvider />` en tant que son enfant ? Dans React, lorsque nous écrivons un composant avec une balise de fermeture correspondante, tous les composants passés en tant qu'enfants deviennent ses props.

```react.js
<Context.Provider value={{showScore, toggleScore}}>	
	{props.children}
</Context.Provider>
```

Donc, lorsque nous passons `props.children` à l'intérieur de `<Context.Provider/>` dans le fichier Context.js, nous passons essentiellement le composant App à l'intérieur. Cela garantit que notre composant App a accès au contexte et qu'il est rendu correctement.

L'API Context nous aide à nous débarrasser complètement du problème de prop drilling. Mais nous devons éviter de l'utiliser lorsque les props doivent être passées à travers certains niveaux. La raison est que chaque fois que l'état du contexte est mis à jour, React ré-affiche chaque composant qui utilise l'état et cela peut causer des problèmes de performance.

Dans les situations où vous souhaitez éviter le prop drilling à travers certains niveaux, la documentation React a fourni une solution raisonnable appelée composition de composants. Vous pouvez en lire plus à ce sujet [ici](https://reactjs.org/docs/composition-vs-inheritance.html).

## Conclusion

Props est l'abréviation de propriétés qui sont des éléments de données en lecture seule qui sont passés à travers les composants pour être manipulés et affichés dans le navigateur.

Les props sont partagées dans la hiérarchie, c'est-à-dire des composants parents aux composants enfants. Vous pouvez utiliser la bibliothèque propTypes pour spécifier le type de données de chaque prop afin d'éviter les problèmes liés aux types de données.

Bien que les props ne puissent être passées que du composant parent au composant enfant, nous avons un moyen de mettre à jour les props à partir d'un composant enfant en utilisant un gestionnaire d'événements qui met à jour un état dans le composant parent.

Pour éviter le problème de prop drilling, nous pouvons utiliser l'API Context dans React qui nous aide à nous débarrasser complètement du problème.

Intéressé à se connecter sur LinkedIn ? Contactez-moi sur [Tooba Jamal](https://www.linkedin.com/in/tooba-jamal/).