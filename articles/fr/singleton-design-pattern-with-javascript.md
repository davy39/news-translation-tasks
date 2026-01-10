---
title: Singleton Design Pattern – Comment cela fonctionne en JavaScript avec un exemple
  de code
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2022-07-18T19:26:56.000Z'
originalURL: https://freecodecamp.org/news/singleton-design-pattern-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/sven-mieke-fteR0e2BzKo-unsplash.jpg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: singleton
  slug: singleton
seo_title: Singleton Design Pattern – Comment cela fonctionne en JavaScript avec un
  exemple de code
seo_desc: 'At one point or another, you might need to use global state inside your
  React apps. This lets you have your data in one place and make sure the required
  components can access it.

  To help you do this, you''ll often use some sort of state management lib...'
---

À un moment ou à un autre, vous pourriez avoir besoin d'utiliser un état global dans vos applications React. Cela vous permet d'avoir vos données à un seul endroit et de vous assurer que les composants requis peuvent y accéder.

Pour vous aider à faire cela, vous utiliserez souvent une sorte de bibliothèque de gestion d'état comme Redux, React Context ou Recoil.

Mais dans cet article, nous allons apprendre à gérer l'état global à l'aide de design patterns.

Nous allons voir ce que sont les design patterns, et nous nous concentrerons particulièrement sur le design pattern singleton. Enfin, nous examinerons un exemple du design pattern singleton ainsi que ses avantages et ses inconvénients.

Alors sans plus attendre, commençons.

## Table des matières

* [Prérequis](#heading-prérequis)
    
* [Qu'est-ce qu'un design pattern](#heading-qu-est-ce-qu-un-design-pattern) ?
    
* [Qu'est-ce que le design pattern singleton](#heading-qu-est-ce-que-le-design-pattern-singleton) ?
    
* [Avantages et inconvénients du design pattern singleton](#heading-avantages-et-inconvénients-du-design-pattern-singleton)
    
* [Résumé](#heading-résumé)
    

## Prérequis

Avant de lire cet article, je vous recommande vivement de vous familiariser avec le contenu des articles suivants :

* [Qu'est-ce que les classes en JavaScript](https://www.freecodecamp.org/news/javascript-classes-how-they-work-with-use-case/) ?
    
* [Comment accéder aux éléments du DOM](https://developer.mozilla.org/en-US/docs/Web/API/Document_Object_Model/Introduction#accessing_the_dom)
    
* [Comment fonctionne Object.freeze](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Object/freeze)
    

## Qu'est-ce qu'un Design Pattern ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/ezgif.com-gif-maker--9-.gif align="left")

*Les design patterns fournissent des solutions conceptuelles à des problèmes courants*

Un design pattern est un ensemble d'instructions généralisées qui fournissent une solution à des problèmes courants dans la conception de logiciels.

Vous pouvez penser aux design patterns comme à un site web qui consiste en plusieurs modèles de conception que vous pouvez utiliser pour construire un site en fonction de vos besoins spécifiques.

Alors, maintenant la question est – pourquoi est-il important de connaître les design patterns ? Eh bien, l'utilisation de design patterns présente plusieurs avantages, tels que :

* Ces patterns sont éprouvés – c'est-à-dire que ces instructions sont testées et éprouvées, et elles reflètent l'expérience et les connaissances de nombreux développeurs.
    
* Ce sont des patterns que vous pouvez réutiliser facilement.
    
* Ils sont très expressifs.
    

Notez que les design patterns fournissent uniquement une solution conceptuelle à un problème récurrent de manière optimisée. Ils ne fournissent pas un morceau de code que vous pouvez utiliser dans votre projet.

Maintenant que nous savons ce que sont les design patterns, plongeons dans notre tout premier design pattern.

## Qu'est-ce que le Design Pattern Singleton ?

![Image](https://www.freecodecamp.org/news/content/images/2022/07/singleton-def-gif.gif align="left")

*Le design pattern singleton expose une seule instance qui peut être utilisée par plusieurs composants*

Singleton est un design pattern qui nous indique que nous ne pouvons créer qu'une seule instance d'une classe et que cette instance peut être accessible globalement.

C'est l'un des types de base de design pattern. Il garantit que la classe agit comme une seule source d'entrée pour tous les composants consommateurs qui souhaitent accéder à cet état. En d'autres termes, il fournit un point d'entrée commun pour utiliser l'état global.

Ainsi, une classe singleton doit être une classe qui :

* Garantit qu'elle ne crée qu'une seule instance de la classe
    
* Fournit un point d'accès global à l'état.
    
* S'assure que l'instance n'est créée que la première fois.
    

### Exemple du Design Pattern Singleton

Pour mieux comprendre ce concept, examinons un exemple. Cet exemple est une simple application React qui démontre comment la valeur de l'état global est utilisée dans les composants, comment elle est modifiée et comment la même valeur est mise à jour dans tous les composants. Commençons.

Avant de commencer avec l'implémentation réelle, jetons un coup d'œil à la structure des dossiers :

```yaml
.
├── index.html
├── package.json
└── src
    ├── componentA.js
    ├── componentB.js
    ├── globalStyles.js
    ├── index.js
    ├── styles.css
    └── utilities.js
```

Voici les détails de chaque fichier :

* `componentA.js` est un composant consommateur qui utilise la classe singleton pour accéder à l'objet d'état global et le manipuler.
    
* `componentB.js` est similaire au composant ci-dessus, car il doit accéder à l'objet d'état global et peut le manipuler.
    
* `globalStyles.js` est un module qui contient la classe singleton et exporte l'instance de cette classe.
    
* `index.js` gère les opérations JS globales, c'est-à-dire les changements JavaScript nécessaires pour d'autres éléments du DOM.
    
* `styles.css` gère le style de l'application. Contient du CSS de base.
    
* `utilities.js` est un module qui exporte certaines fonctions utilitaires.
    
* `index.html` contient le code HTML pour les composants nécessaires dans le projet.
    
* `package.json` est une configuration de base émise par la commande `npm init`.
    

Maintenant que nous savons ce que fait chaque fichier, nous pouvons commencer à les implémenter un par un.

Mais avant de plonger dans cet exemple, nous devons comprendre le flux de code. Le but de notre exemple est de construire une application JavaScript qui démontre comment le style global `color` est consommé par chacun des composants et comment chaque composant le modifie.

Chaque composant contient un `color-picker`. Lorsque vous changez la propriété de style global `color` via le sélecteur de couleur présent dans chaque composant, il apparaît automatiquement dans les autres composants et dans l'état global.

Tout d'abord, créons un fichier : `index.html`. Ensuite, collez le code ci-dessous dans ce fichier :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Parcel Sandbox</title>
    <meta charset="UTF-8" />
    <link rel="stylesheet" href="./src/styles.css" />
  </head>

  <body>
    <div class="global-state">
      <h3>Global State</h3>
      <h4>Color</h4>
      <span id="selected-color"></span>
    </div>
    <div class="contents">
      <div class="component-a">
        <strong>Component A</strong>
        <div>Pick color</div>
        <span id="selected-color">black</span>
        <input type="color" id="color-picker-a" />
      </div>
      <div class="component-b">
        <strong>Component B</strong>
        <div>Pick color</div>
        <span id="selected-color">black</span>
        <input type="color" id="color-picker-b" />
      </div>
    </div>
    <script src="src/index.js"></script>
    <script src="src/componentA.js"></script>
    <script src="src/componentB.js"></script>
  </body>
</html>
```

Ici, en haut, nous chargeons notre CSS via `<link rel="stylesheet" href="./src/styles.css" />`.

Ensuite, nous avons divisé notre application en deux parties via deux classes :

* `.global-state` : Cela représentera le code HTML pour montrer l'état global actuel de l'application.
    
* `.contents` : Cela représentera le code HTML qui représente les deux composants.
    

Chacun des composants (`component-a` et `component-b`) a un élément d'entrée de sélecteur de couleur.

Ces deux composants ont un `span` avec un élément de classe `selected-color` qui aidera à afficher la valeur actuelle de la variable d'état global `color`.

Comme vous pouvez le voir, lors d'un changement du sélecteur de couleur dans `componentA`, les valeurs suivantes changent également :

* Valeur à l'intérieur de l'élément span `.selected-color` dans `componentB` et l'état global.
    
* Valeur du sélecteur de couleur de `componentA` et `componentB`.
    

Nous verrons plus tard comment toutes ces valeurs changent. Mais pour l'instant, il est important pour nous de comprendre que si nous changeons la valeur de l'état global à partir d'un composant, alors les classes singleton s'assurent que la valeur de l'instance est mise à jour et que tous les composants qui consomment cette instance obtiennent la même valeur puisqu'ils se réfèrent à la même instance.

Ensuite, nous créons un fichier nommé `globalStyles.js`. Copiez-collez le code ci-dessous :

```javascript
let instance;
let globalState = {
  color: ""
};

class StateUtility {
  constructor() {
    if (instance) {
      throw new Error("New instance cannot be created!!");
    }

    instance = this;
  }

  getPropertyByName(propertyName) {
    return globalState[propertyName];
  }

  setPropertyValue(propertyName, propertyValue) {
    globalState[propertyName] = propertyValue;
  }
}

let stateUtilityInstance = Object.freeze(new StateUtility());

export default stateUtilityInstance;
```

Le code ci-dessus est un module qui contient une classe singleton `StateUtility` et exporte par défaut l'instance de cette classe.

Plongeons plus profondément dans la classe `StateUtility` pour comprendre comment elle devient une classe singleton :

* Elle contient un `constructor` et deux méthodes de classe appelées `getPropertyByName` et `setPropertyValue`. Ces deux méthodes de classe sont assez explicites : l'une obtient la valeur de la propriété et l'autre définit sa valeur.
    
* Ensuite, nous avons la fonction `constructor`. C'est une fonction qui est appelée chaque fois que nous créons un nouvel objet de cette classe.
    
* Mais voici un piège : pour qu'une classe soit un singleton, nous devons nous assurer qu'elle ne crée qu'une seule instance, et c'est tout.
    
* Pour nous assurer que cela se produit, nous créons simplement une variable globale appelée `instance`. Nous la définissons en haut du module. Cette variable agit comme un vérificateur. Nous ajoutons une condition dans la fonction `constructor` telle que si la variable `instance` a une valeur (c'est-à-dire l'objet de la classe `StateUtility`), alors une erreur est lancée, sinon nous attribuons `instance` à l'instance de classe actuelle (l'objet `this`).
    
* Dans cet exemple, nous avons implémenté la classe `StateUtility` de manière à ce qu'elle puisse exposer et modifier la variable `globalState`.
    
* Nous nous assurons de ne pas exposer `globalState`. Nous les exposons en utilisant les méthodes de classe de `StateUtility`. De cette manière, nous protégeons l'état global d'être modifié directement.
    
* Enfin, nous créons l'instance de la classe comme suit : `let stateUtilityInstance = Object.freeze(new StateUtility());`.
    
* Nous avons utilisé `Object.freeze` pour qu'aucune autre classe/composant/module ne puisse modifier l'instance `stateUtilityInstance` exposée.
    

Ensuite, créons un fichier appelé `componentA.js` dans le dossier `src`. Copiez-collez le code ci-dessous dans ce fichier :

```javascript
import {
    setAllSelectedColor
} from "./utilities";
import globalStyle from "./globalStyles";

// Get respective dom elements
const selectedColor = document.querySelectorAll("#selected-color");
const colorPickerA = document.getElementById("color-picker-a");
const colorPickerB = document.getElementById("color-picker-b");

// Event handler whenever a change event occurs
colorPickerA.onchange = (event) => {
    // set the color property of the global state with current color picker's value;
    globalStyle.setPropertyValue("color", event.target.value);
    const color = globalStyle.getPropertyByName("color");

    // A function thats sets the value of all the #selection-color dom elements;
    setValueOfSimilarElements(selectedColor, color);

    // make sure to set the component B's color picker value is set to color picker A;
    // this is done to make sure that both of the color picker have same value on change;
    colorPickerB.value = color;
};
```

Voici la décomposition du code ci-dessus :

* Le but de ce code est de s'assurer que nous attachons le gestionnaire `onChange` pour le sélecteur de couleur qui est présent dans `component-a`. Dans ce cas, le sélecteur de couleur du composant A est identifié par l'id : `#color-picker-a`.
    
* Nous devons nous assurer que ce gestionnaire :
    
    1. Définit la valeur de la propriété color de globalState.
        
    2. Récupère la même propriété à nouveau.
        
    3. Applique la même valeur à différentes zones du DOM.
        
    4. S'assure également que nous définissons la valeur de l'autre sélecteur de couleur à l'état global.
        

Maintenant, examinons toutes ces étapes une par une :

* Tout d'abord, récupérons tous les éléments DOM requis.
    
* Ce que nous prévoyons ici est de mettre à jour tous les sélecteurs de couleur et les éléments span avec l'id `#selected-color` avec la valeur de la propriété color de globalState actuelle chaque fois que l'événement on change se produit.
    
* Dans le cas de `componentA`, une fois que nous changeons la couleur via le sélecteur de couleur, nous devons mettre à jour la même valeur dans 2 éléments span (`#selected-color`) – c'est-à-dire un élément span de `componentB` et un élément span présent dans le conteneur div `.global-state`.
    
* Nous faisons cela parce que nous voulons garder tous les composants synchronisés et démontrer que la valeur de l'état global reste la même dans tous les composants.
    
* Nous mettons ensuite à jour la propriété `color` de l'état global en utilisant la méthode de classe `setPropertyValue` de `StateUtility`. Nous lui passons `event.target.value` car cela contient la valeur actuelle présente dans le sélecteur de couleur d'entrée `#color-picker-a`.
    
* Une fois la valeur définie, nous récupérons la même propriété à nouveau en utilisant `getPropertyByName`. Nous faisons cela pour démontrer que la propriété `color` de l'état global a été mise à jour et est prête à être utilisée.
    
* Ensuite, nous utilisons la fonction utilitaire `setValueOfSimilarElements` pour mettre à jour tous les éléments qui ont le même nom de classe/id avec une certaine valeur. Dans ce cas, nous mettons à jour tous les éléments `#selected-color` avec la valeur `color`.
    
* Enfin, nous mettons à jour la valeur de l'autre sélecteur de couleur, c'est-à-dire le sélecteur de couleur du composant B `#color-picker-b`.
    

Nous faisons la même chose pour `componentB`. Nous créons un fichier appelé `componentB.js` et le mettons à jour avec le code suivant :

```javascript
import {
    setValueOfSimilarElements
} from "./utilities";
import globalStyle from "./globalStyles";

// Get respective dom elements
const selectedColor = document.querySelectorAll("#selected-color");
const colorPickerA = document.getElementById("color-picker-a");
const colorPickerB = document.getElementById("color-picker-b");

/**
 * Event handler whenever a change event occurs
 */
colorPickerB.onchange = (event) => {
    // set the color property of the global state with current color picker's value;
    globalStyle.setPropertyValue("color", event.target.value);

    const color = globalStyle.getPropertyByName("color");

    // A function thats sets the value of all the #selection-color dom elements
    setValueOfSimilarElements(selectedColor, color);

    // make sure to set the component A's color picker value is set to color picker B;
    // this is done to make sure that both of the color picker have same value on change;
    colorPickerA.value = color;
};
```

Nous faisons la même chose que ce que nous avons fait dans le fichier `componentA`, mais dans ce cas, nous mettons à jour la valeur du sélecteur de couleur présent dans `componentA` (c'est-à-dire que nous mettons à jour la valeur de l'élément `#color-picker-a`).

Voici à quoi ressemblera notre application :

[Voici le lien vers le code](https://zqbo69.csb.app/) :

%[https://codesandbox.io/embed/zqbo69?view=editor+%2B+preview] 

## Avantages et inconvénients du Design Pattern Singleton

Voici quelques-uns des avantages de l'utilisation du design pattern singleton :

* Il garantit qu'une seule instance de la classe est créée.
    
* Nous obtenons un seul point d'accès à l'instance qui peut être accessible globalement.
    

Voici quelques inconvénients du design pattern singleton :

* Il viole le principe de responsabilité unique. C'est-à-dire qu'il essaie de résoudre deux problèmes en même temps. Il essaie de résoudre les problèmes suivants : *Garantir qu'une classe n'aura qu'une seule instance*, et *attribuer un point d'accès global à l'instance de la classe singleton.*
    
* Il est difficile d'écrire des cas de test unitaires pour les classes singleton. Cela est dû au fait que l'ordre d'exécution peut changer la valeur présente dans l'état global, donc l'ordre d'exécution est important.
    
* Lors de l'écriture de tests unitaires, il existe un risque qu'un autre composant ou module modifie la valeur/instance de l'état global. Dans de tels scénarios, il devient difficile de déboguer l'erreur.
    

## Résumé

Le design pattern singleton peut être utile pour créer un état global accessible par n'importe quel composant.

Pour parler brièvement du pattern singleton :

* C'est un pattern qui restreint la classe à ne créer qu'une seule instance.
    
* Le pattern singleton peut être considéré comme les bases des bibliothèques de gestion d'état global telles que Redux ou React Context.
    
* Ils peuvent être accessibles globalement et agissent comme un seul point d'accès pour accéder à l'état global.
    

C'est tout.

Merci d'avoir lu !

Suivez-moi sur [Twitter](https://twitter.com/keurplkar), [GitHub](https://github.com/keyurparalkar) et [LinkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).