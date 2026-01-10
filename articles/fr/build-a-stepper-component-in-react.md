---
title: Comment créer un composant Stepper dans React
subtitle: ''
author: Olabisi Olaoye
co_authors: []
series: null
date: '2024-01-10T15:28:54.000Z'
originalURL: https://freecodecamp.org/news/build-a-stepper-component-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Your-paragraph-text-3.png
tags:
- name: CSS
  slug: css
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment créer un composant Stepper dans React
seo_desc: I was working on a React project recently, and I realized that there were
  so many UI components that I had to build to get things done quickly. So I began
  to explore a lot of UI libraries like Material UI or Chakra UI. Then I started wondering
  why I ...
---

Je travaillais récemment sur un projet React et j'ai réalisé qu'il y avait tant de composants UI que je devais créer pour avancer rapidement. J'ai donc commencé à explorer de nombreuses bibliothèques UI comme [Material UI](https://mui.com) ou [Chakra UI](https://chakra-ui.com/). Ensuite, j'ai commencé à me demander pourquoi je n'avais pas tenté de construire certains de ces composants moi-même.

J'ai donc décidé de me lancer dans une aventure pour construire autant de composants que possible. Bien sûr, cela prendrait plus de temps, mais j'apprendrais comment ces composants sont construits.

Dans ce guide, vous apprendrez à construire un stepper, un composant UI qui guide un utilisateur à travers un processus en le divisant en plusieurs étapes. Nous allons réaliser cela avec React et Tailwind CSS, un framework CSS open-source, basé sur des utilitaires, qui vous permet de styliser votre HTML directement sans avoir à ouvrir un fichier `.css`.

Voici quelques prérequis dont vous avez besoin avant de pouvoir suivre efficacement ce guide :

* Connaissance de HTML, CSS et JavaScript
* Connaissance des fondamentaux de React

## Comment configurer le projet

Tout d'abord, vous devez créer un projet React. Dans le terminal de votre éditeur de texte et dans le répertoire de votre choix, tapez cette commande :

```bash
npx create-react-app my-stepper
```

Ensuite, installez Tailwind CSS dans votre projet avec cette commande :

```bash
npm install -D tailwindcss
```

Lorsque cela est fait, un fichier tailwind.config.js est automatiquement créé pour vous dans le répertoire racine du projet. Il ne contient initialement aucune configuration particulière, vous devrez donc ajouter les chemins vers vos fichiers de modèle comme ceci :

```javascript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```

## Comment construire la mise en page du Stepper

Ensuite, créez un composant Stepper dans le répertoire `src` de votre projet. Il doit pouvoir passer à l'étape suivante en montrant un changement de couleur visible ou un texte d'aide, ou les deux. Par exemple, une étape inactive peut être grise et une étape active peut être bleue.

Essentiellement, nous devons pouvoir nous déplacer en avant et en arrière entre les étapes. La mise en page ne comportera qu'un cercle et une ligne de connexion pour l'instant, mais plus tard, un peu de JavaScript aidera à répliquer les cercles et les lignes de connexion en fonction du nombre d'étapes dont le stepper sera composé.

```javascript
//Stepper.js
export default function Stepper () {
    return (
        <div className="flex items-center">
            <div className="rounded-full bg-blue-500 w-6 h-6"></div>
            <span className="h-1 w-8 bg-blue-500"></span>
        </div>
    )
}
```

Dans le bloc de code ci-dessus, j'ai stylisé l'apparence de base du stepper : un cercle arrondi avec un fond bleu, et une courte ligne juste à côté. Ils seront tous les deux répliqués, en fonction du nombre d'étapes que vous souhaitez afficher.

Pour les besoins de ce guide, vous pouvez ajouter deux boutons dans le composant `App` pour passer d'une étape à l'autre. Ensuite, le composant Stepper peut être rendu juste au-dessus d'eux comme ceci :

```javascript
//App.js
import { useState } from 'react';
import Stepper from './Stepper';

export default function App()  {
    return (
        <main>
            <Stepper />
            <div>
                <button>Étape précédente</button>
                <button>Étape suivante</button>
            </div>
        </main>
    )
}
```

## Comment ajouter de la fonctionnalité au Stepper

Pour faire fonctionner un stepper de base, il y a deux choses à noter : combien d'étapes il y a au total, et quelle est l'étape actuelle.

Si vous traitez avec cinq étapes, par exemple, vous devez savoir quelle étape est l'étape active. Cela signifie que vous aurez besoin de ces deux informations dans le composant `Stepper` sous forme de props.

À partir du nombre total d'étapes passé dans le composant, vous pouvez générer un groupe de cercles et de lignes de connexion ce nombre de fois. Vous pouvez utiliser la fonction intégrée `Array.from()` de JavaScript pour créer un tableau d'étapes comme ceci :

```javascript
export default function Stepper ({currentStep, numberOfSteps}) {
    return (
        <div className="flex items-center">
        {Array.from({length: numberOfSteps}).map((_, index) => (
        	<React.Fragment key={index}>
          		<div className={`w-6 h-6 rounded-full`}></div>
				<div className={`w-12 h-1`}></div> 
        	</React.Fragment>
      	))}
        </div>
    )
}
```

Dans le bloc de code ci-dessus, j'ai utilisé `React.Fragment` pour ne pas avoir à envelopper le div du cercle et le div du connecteur dans un div redondant (les expressions JSX doivent avoir un seul élément parent).

De plus, lors du mappage du tableau, j'ai utilisé le symbole `_` comme premier paramètre dans la fonction `map` car nous n'en avons pas besoin. C'est plus un paramètre "jetable" que nous n'utilisons pas car nous avons juste besoin d'accéder au paramètre d'index du tableau.

Faisons un peu de style. Chaque étape active doit avoir une couleur distincte pour indiquer à l'utilisateur qu'il s'agit de l'étape actuelle dans le composant.

Pour implémenter cela, créez une fonction `activeColor` qui prend en argument l'index actuel du tableau généré à partir de `Array.from()`, et le compare avec la variable `currentStep`. Si l'index actuel correspond à l'étape actuelle, une couleur distincte est utilisée, sinon une couleur inactive est utilisée.

```javascript
const activeColor = (index) => currentStep === index ? "bg-blue-500" : "bg-gray-300"
```

La condition incorporée dans la fonction `activeColor` ci-dessus stipule, en termes simples, "à ce stade de notre tableau d'étapes, sommes-nous à l'étape actuelle ? Si oui, la couleur de l'étape est bleue. Sinon, elle est grise."

Maintenant, ajoutez cette ligne de code au composant `Stepper` et appelez la fonction dans le nom de la classe de chaque cercle et ligne de connexion.

```javascript
export default function Stepper ({currentStep, numberOfSteps}) {
  const activeColor = (index) => currentStep >= index ? 'bg-blue-500' : 'bg-gray-300'

  return (
    <div className="flex items-center">
      {Array.from({length: numberOfSteps}).map((_, index) => (
        <React.Fragment key={index}>
          <div className={`w-6 h-6 rounded-full ${activeColor(index)}`}>  
          </div>
		  <div className={`w-12 h-1 ${activeColor(index)}`}></div>
        </React.Fragment>
      ))}
    </div>
  )
}
```

Il y a un petit problème, cependant. Parce que le cercle et la ligne de connexion sont simplement répliqués en fonction du nombre d'étapes, voici le résultat actuel :


![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-167.png)
_Stepper montrant la ligne de connexion supplémentaire à la fin_

Il y a une ligne de connexion supplémentaire à la fin – mais nous pouvons facilement corriger cela en la rendant conditionnellement. La condition vérifiera simplement si l'index actuel dans le tableau est sur la dernière étape. Si c'est le cas, alors il n'est pas nécessaire de rendre une ligne de connexion. De cette façon, cette ligne de connexion solitaire disparaît à la dernière étape.

```javascript
const isFinalStep = (index) => index === numberOfSteps - 1
```

Ainsi, lorsque j'appelle cette fonction dans le JSX du composant `Stepper`, la ligne de connexion ne sera affichée que si cette étape n'est pas l'index actuel du tableau n'est pas égal au nombre d'étapes (moins un, puisque nous travaillons avec un tableau à index zéro). Le composant `Stepper`, entièrement terminé, ressemblera alors à ceci :

```javascript
import React from 'react';

export default function Stepper ({currentStep, numberOfSteps}) {
  const activeColor = (index) => currentStep >= index ? 'bg-blue-500' : 'bg-gray-300'
  const isFinalStep = (index) => index === numberOfSteps - 1

  return (
    <div className="flex items-center">
      {Array.from({length: numberOfSteps}).map((_, index) => (
        <React.Fragment key={index}>
          <div className={`w-6 h-6 rounded-full ${activeColor(index)}`}></div>
          {isFinalStep(index) ? null : <div className={`w-12 h-1 ${activeColor(index)}`}></div>}
        </React.Fragment>
      ))}
    </div>
  )
}
```

## Comment passer les props

Puisque le composant `Stepper` accepte `currentStep` et `numberOfSteps` comme props, ces deux éléments doivent être définis dans le composant `App`.

Rappelez-vous, l'étape actuelle change, donc elle doit être suivie. Vous pouvez utiliser le hook `useState` de React pour cela. L'état initial est défini à zéro, qui est la première étape. Pour les besoins de ce guide, j'utiliserai cinq étapes.

```javascript
//App.js

export default function App() {
    const [currentStep, setCurrentStep] = React.useState(0)
    const NUMBER_OF_STEPS = 5

    return (
        //...du code
        <Stepper currentStep={currentStep} numberOfSteps={NUMBER_OF_STEPS}/>
        //...du code
    )
}
```

## Comment se déplacer en avant et en arrière entre les étapes

La dernière chose à faire est d'ajouter une fonctionnalité à ces deux boutons dans le composant `App`.

Créez deux fonctions, `goToPreviousStep` et `goToNextStep`, qui vont simplement décrémenter ou incrémenter l'état de l'étape actuelle.

Pour empêcher le bouton précédent de décrémenter en dessous de zéro, puisque la première étape a un index de zéro, vous pouvez ajouter une condition pour vérifier si l'étape actuelle est supérieure ou égale à zéro. Ce sera la limite inférieure du stepper.

Pour le bouton suivant, l'étape actuelle ne doit pas dépasser le nombre d'étapes moins un, puisque nous traitons avec un tableau à [index zéro](https://en.wikipedia.org/wiki/Zero-based_numbering).

Voici le code final pour le composant `App` :

```javascript
import React from 'react';
import Stepper from './Stepper';

export default function App() {
  const [currentStep, setCurrentStep] = React.useState(0)
  const NUMBER_OF_STEPS = 5

  const goToNextStep = () => setCurrentStep(prev => prev === NUMBER_OF_STEPS - 1 ? prev : prev + 1)
  const goToPreviousStep = () => setCurrentStep(prev => prev <= 0 ? prev : prev - 1)

  return (
    <div>
      <h1 className="text-2xl">Voici le stepper en action !</h1>
      <br/>
      <Stepper currentStep={currentStep} numberOfSteps={NUMBER_OF_STEPS}/>
      <br/>
      <section className="flex gap-10">
        <button 
		  onClick={goToPreviousStep} 
		  className="bg-blue-600 text-white p-2 rounded-md"
		>
          Étape précédente
        </button>
        <button 
		  onClick={goToNextStep} 
		  className="bg-blue-600 text-white p-2 rounded-md"
		>
          Étape suivante
      	</button>
      </section>
    </div>
  );
}

```

Et c'est tout ! Vous avez réussi à construire un composant stepper dans un projet React. Vous pouvez jouer avec cette [démo fonctionnelle sur Stackblitz](https://stackblitz.com/edit/stackblitz-starters-ga6rgw?file=src%2FApp.js). Veuillez me faire part de vos pensées et suggestions concernant cet article.

Bonus : Vous pouvez améliorer ce code en ajoutant des libellés et des descriptions à chaque étape.

Merci d'avoir lu !