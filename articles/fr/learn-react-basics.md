---
title: Tutoriel React – Apprendre les bases de la programmation React et JavaScript
  avec des exemples de code
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2021-03-01T23:52:36.000Z'
originalURL: https://freecodecamp.org/news/learn-react-basics
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/freeCodeCamp-Cover-2.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: components
  slug: components
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Tutoriel React – Apprendre les bases de la programmation React et JavaScript
  avec des exemples de code
seo_desc: "React is an open-source JavaScript library that helps you build user interfaces.\
  \ It's a component-based, declarative, \"learn once and write anywhere\" tool. \n\
  With 164K+ GitHub stars, 30K+ forks, and close to ~10 million weekly downloads,\
  \ React is undo..."
---

React est une bibliothèque JavaScript open-source qui vous aide à construire des interfaces utilisateur. C'est un outil basé sur les composants, déclaratif, "apprendre une fois et écrire partout".

Avec plus de 164K étoiles sur GitHub, 30K forks, et près de ~10 millions de téléchargements par semaine, React est sans aucun doute une excellente bibliothèque d'interface utilisateur à apprendre et à utiliser.

Si vous êtes un développeur qui commence avec React ou qui envisage de l'utiliser dans vos projets secondaires ou en entreprise, cet article est pour vous. Si vous avez commencé à apprendre React il y a quelque temps mais que vous avez du mal à saisir les bases, lisez cet article.

# TL;DR

Cet article est long mais devrait être une lecture amusante si vous voulez apprendre React ou si vous travaillez déjà avec. Il répond à ces questions :

* Comment la connaissance du JavaScript moderne fait de vous un développeur React efficace ?
* Quels types de changements devez-vous apporter à votre état d'esprit lorsque vous concevez et développez une application React ?
* Quels sont les écosystèmes dont vous devez être conscient et pourquoi ?

Détendez-vous, prenez votre boisson préférée et profitez de l'article.

# Pourquoi j'ai écrit cet article

Au début, lorsque j'apprenais React, j'ai fait l'erreur de ne pas me concentrer sur quelques fondamentaux essentiels. À mesure que mes connaissances grandissaient, j'ai commencé à apprendre ces concepts et je me suis senti plus à l'aise avec React.

Beaucoup de mes mentorés ont discuté des défis auxquels ils étaient confrontés lorsqu'ils travaillaient avec React, qui tournent également autour de ces fondamentaux. Cela m'a motivé à écrire cet article et à partager ce que j'ai appris.

# Concepts de JavaScript moderne que vous devez connaître pour React

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-179.png)
_Flexibilité avec le JavaScript moderne_

Le nom standardisé de JavaScript est ECMAScript. ECMAScript 2015 (qui est également la 6ème édition, et pourquoi il est appelé ES6) a apporté de nombreuses fonctionnalités et une nouvelle syntaxe au langage JavaScript.

React, et de nombreuses autres bibliothèques et frameworks d'interface utilisateur modernes, fonctionnent bien avec ES6. Il est essentiel de connaître sa syntaxe moderne et ses nouvelles fonctionnalités pour faciliter la programmation.

> Cela ne signifie pas que vous ne pouvez pas écrire une application React avec ES5. [Vous pouvez](https://reactjs.org/docs/react-without-es6.html) si vous devez, mais vous ferez les choses de manière plus difficile.

Voici quelques concepts que vous devez bien apprendre.

## 1. Comment utiliser Let et Const en JavaScript

Jusqu'à ES5, la seule façon de déclarer une variable était d'utiliser le mot-clé `var`. ES6 a introduit deux autres façons de déclarer des variables, en utilisant les mots-clés `let` et `const`. L'utilisation de ces mots-clés modernes nous donne plus de prévisibilité et moins de chances d'introduire des bugs dans le code.

### Le mot-clé `var`

Une variable déclarée avec `var` est limitée à la portée de la fonction. Cela signifie que nous obtiendrons une `ReferenceError` lorsque nous essaierons d'accéder à la variable en dehors de la fonction.

```js
var x = 10;
function someFunc(){
    var y = 10;
    console.log('inside someFunc', x, y);
}
```

Maintenant, si vous appelez `someFunc()`, il enregistrera ce qui suit dans la console du navigateur :

```shell
inside someFunc 10 10
```

Mais essayez d'accéder à la variable y en dehors de `sumFunc()` et vous obtiendrez l'erreur suivante :

```shell
Uncaught ReferenceError: y is not defined

```

### Le mot-clé `let`

`let` est limité à la portée du bloc. C'est la principale différence entre `let` et `var`. Prenons cette fonction où nous bouclons en utilisant une boucle `for` et accédons à la variable `i` à l'intérieur et à l'extérieur de la boucle.

```js
function letsLoop() {
 for (var i=0; i<5; i++) {
   console.log('i inside the loop: ', i);
 }
 
 console.log('i outside of loop', i);
}

```

Lorsque vous appelez la fonction `letsLoop()`, la sortie sera la suivante :

```shell
i inside the loop:  0
i inside the loop:  1
i inside the loop:  2
i inside the loop:  3
i inside the loop:  4
i outside of loop 5
```

Maintenant, changeons le mot-clé `var` en `let` lors de la déclaration et de l'assignation de la variable `i`.

```js
function letsLoop() {
 for (let i=0; i<5; i++) {
   console.log('i inside the loop: ', i);
 }
 
 console.log('i outside of loop', i);
}
```

Si vous exécutez la fonction `letsLoop()` maintenant, vous obtiendrez une `ReferenceError` lors de l'accès à la variable `i` en dehors de la boucle `for`. C'est parce que la visibilité et l'accessibilité (ou la portée) de la variable `i` sont limitées au bloc `for`.

```shell
i inside the loop:  0
i inside the loop:  1
i inside the loop:  2
i inside the loop:  3
i inside the loop:  4
Uncaught ReferenceError: i is not defined
    at letsLoop (<anonymous>:6:35)
    at <anonymous>:1:1
```

### Le mot-clé `const`

`const` est presque identique à `let`. La seule différence est que, une fois que vous avez assigné une valeur à une variable définie avec le mot-clé `const`, vous ne pouvez pas réassigner une nouvelle valeur à celle-ci.

```js
const name = 'freeCodeCamp';

name = 'My freeCodeCamp'; // Uncaught TypeError: Assignment to constant variable.
```

Cela s'applique à tous les types de variables que nous pouvons créer en JavaScript. Vous devez être prudent lorsque cela concerne une structure de données complexe comme `object`. Lorsqu'un objet est déclaré et que sa valeur est assignée avec `const`, vous pouvez toujours changer la valeur de ses propriétés. Mais vous ne pouvez pas réassigner la variable à un autre objet. Veuillez consulter cet exemple :

```js
const publication = {
 'name': 'freeCodeCamp'
}

publication.name= 'My freeCodeCamp'; // Autorisé

publication = {}; // Uncaught TypeError: Assignment to constant variable.
```

Et maintenant, pour comparer les trois mots-clés :

|               | var           | let   | const |
| ------------- |:-------------:| -----:| -----:|
|    Portée      | fonction      | bloc | bloc |
|    Réassigner une nouvelle valeur      | Autorisé      | Autorisé | Non Autorisé |
| Lorsque l'accès est avant la déclaration      | undefined       |   ReferenceError  | ReferenceError |

Voici quelques règles pour utiliser var, let et const :

* N'utilisez plus `var`. Utilisez `let` ou `const`.
* Utilisez `const` plus souvent. Utilisez `let` lorsque vous devez réassigner une autre valeur à une variable.

Dans une application React, vous verrez souvent du code utilisant `let` et `const`. Un composant React est généralement déclaré en utilisant `const`. Consultez l'exemple ci-dessous.

La variable `DifficultyLevels` est déclarée en utilisant `const` et se voit assigner une fonction comme valeur. Cette fonction définit un composant React. Il est logique d'utiliser `const` ici, car il ne sera pas réassigné avec une autre valeur.

Maintenant, remarquez les usages de la variable `level` à l'intérieur de `useEffect`. Nous devons réassigner les valeurs en fonction d'une condition. Il est donc logique d'utiliser le mot-clé `let` ici. Mais vous ne verrez aucun `var` nulle part !

```js
const DifficultyLevels = () => {
    
    const userDataLS = getFromLS(LS_KEY_USER_DATA);
    const [userData, setUserData] = useState(userDataLS || {
        'fullName': '',
        'age': '',
        'email': '',
        'gender': 'F',
        'difficultyLevel': BEGINNER
    });
    
    //... autre code
    
    useEffect(() => {
        let level = 'beginner';
        if (userData.age >=10 && userData.age <= 13) {
            level = 'intermediate';
        } else if (userData.age > 13) {
            level = 'advanced';
        }
        
        setUserData({
            ...userData,
            'difficultyLevel': level
        });
    }, [userData.age]);
    
    //... autre code
    
    return(
        <>
        	{/*...autre code */}
        
          	<span> { userData.level } </span>
        
		  	{/*...autre code */}
        </>
    )
    
}
```

## 2. Comment utiliser les littéraux de gabarit en JavaScript

Les jours où nous devions concaténer des chaînes de caractères comme ceci sont révolus :

```js
var name = 'Tapas';
var publication = 'freeCodeCamp';
var greeting = 'Hello'; // Ou Hola

// Cela produit une sortie comme "Hello Tapas, welcome to freeCodeCamp."
var message = greeting + ' ' + name + ', welcome to ' + publication + '.';
```

La manière ci-dessus de gérer la concaténation de chaînes et les valeurs dynamiques est trop fastidieuse, difficile à lire et sujette aux erreurs. Que diriez-vous d'obtenir la même sortie en écrivant du code naturellement sans se soucier des `+`, des espaces, etc. ?

Avec ES6, nous avons les `littéraux de gabarit`, qui sont des littéraux de chaîne permettant d'intégrer des expressions. Nous utilisons des backticks (` `) au lieu de guillemets simples ou doubles dans les littéraux de gabarit. Nous pouvons définir les valeurs dynamiques (ou expressions) comme des espaces réservés en utilisant le signe dollar ($) et des accolades (comme `${expression}`).

Écrivons l'exemple ci-dessus en utilisant des littéraux de gabarit.

```js
// Nous nous attendons à ce que les valeurs changent dynamiquement, d'où `let`
let name = 'Tapas';
let publication = 'freeCodeCamp';
let greeting = 'Hello'; // Ou Hola

// Une bien meilleure façon d'écrire comme une phrase en langage naturel
let message = `${greeting} ${name}, welcome to ${publication}.`;
```

Alors, l'utilisons-nous dans notre code React ? Oui, pourquoi pas ? Vous pourriez vouloir utiliser le message de salutation ci-dessus dans votre composant React et le rendre dans un élément d'interface utilisateur. [Voici un article](https://blog.greenroots.info/what-exactly-is-javascript-tagged-template-literal-ckg6hyekf000n8bs1hz9udvzc) pour vous aider à apprendre les littéraux de gabarit en détail.

Utilisez-vous [styled-components](https://styled-components.com/) dans votre projet React ? Dans ce cas, vous utilisez déjà des littéraux de gabarit !

## 3. Comment importer et exporter des modules en JavaScript

Pour coder efficacement dans React, vous devez `penser en React`. L'une des principales façons de penser est de diviser l'interface utilisateur en une hiérarchie de composants appropriée.

Nous apprendrons plus en détail ce que cela signifie ci-dessous. Mais à un niveau élevé, chaque composant dans React peut être un module JavaScript. Vous devez exporter ce module pour l'importer ailleurs dans le code pour une meilleure composition de composants. C'est pourquoi il est essentiel de bien maîtriser les concepts de modules et les fonctionnalités d'import/export.

Voici un exemple simple de la façon dont nous pouvons exporter un composant React et l'importer dans un autre composant.

```js

// under-construction.js sous le répertoire src/components/utility

import React from "react";

const UnderConstruction = () => {
    
    return(
        <div className="column">
            <p style={{marginTop:"10px"}}>
                Si vous voyez ceci, je suis probablement en train de travailler dessus ! 
                Veuillez lui donner quelques jours pour être construit.
            </p>
        </div>
    )
};

export default UnderConstruction;
```

Dans un autre composant :

```js
import UnderConstruction from './components/utility/under-construction'
```

Veuillez [lire cet article](https://blog.greenroots.info/javascript-modules-and-how-to-effectively-work-with-export-import-cka7t5z6s01irx9s16st6j51j) pour vous familiariser avec les modules JavaScript et les mots-clés import/export.

## 4. Comment utiliser les fonctions fléchées en JavaScript

Juste un petit rappel – vous pouvez écrire du code React sans les fonctions fléchées JavaScript.

C'est vrai. Alors, pourquoi en parlons-nous ? Une fonction fléchée est utile à bien des égards :

* Elle rend l'écriture de fonctions beaucoup plus facile. Vous tapez généralement moins de caractères lorsque vous utilisez des fonctions fléchées que avec des fonctions standard.

```js
const double = (num) => {return num * 2;};
```

* Contrairement aux fonctions standard, une fonction fléchée ne redéfinit pas la valeur de `this` dans sa définition. Ce comportement en fait un choix facile pour les développeurs d'utiliser des fonctions fléchées comme rappels. Qui veut plus de bugs à cause de `this` ?

Voici [un excellent article](https://www.freecodecamp.org/news/arrow-function-javascript-tutorial-how-to-declare-a-js-function-with-the-new-es6-syntax/) pour vous initier aux fonctions fléchées et à leurs usages.

## 5. Comment fonctionne la destructuration en JavaScript

La destructuration est la syntaxe JavaScript pour extraire des valeurs d'une propriété d'objet et les assigner à une variable. La destructuration est également possible pour les tableaux JavaScript.

Une fois que vous aurez bien appris la destructuration, cela aidera à simplifier les choses.

Vous pouvez utiliser la destructuration dans les boucles, comme ceci :

```js
for(let { name, age } of users) {
    console.log(`${name} a ${age} ans !`);
}
```

Avec la valeur de retour d'une fonction :

```js
const getUser = () => {
    return{ 
        'name': 'Alex',
        'address': '15th Park Avenue',
        'age': 43
    }
}

const { name, age } = getUser();

console.log(name, age); // Alex 43
```

Dans un paramètre de fonction :

```js
function logDetails({name, age}) {
    console.log(`${name} a ${age} an(s) !`)
}
```

Voici un exemple de destructuration de tableau :

```js
let emojis = ['🔥', '⏲️', '🏆', '🍉'];

let [fire, clock, , watermelon] = emojis;

console.log(fire, clock, watermelon); // 🔥 ⏲️ 🍉

```

Bien sûr, nous aurions pu faire emojis[0], emojis[1], etc. Mais c'est trop long à écrire et à assigner à des variables une par une.

Dans une application React, vous verrez une utilisation intensive de la destructuration d'objets et de tableaux. Un développeur React expérimenté qui pourrait examiner votre code s'attendrait à voir ces implémentations également.

[Voici un article approfondi](https://www.freecodecamp.org/news/javascript-object-destructuring-spread-operator-rest-parameter/) qui couvre la destructuration d'objets. Vous devez également connaître la destructuration de tableaux.

## 6. Comment fonctionnent l'opérateur de propagation et le paramètre Rest en JavaScript

La syntaxe de propagation (également connue sous le nom d'opérateur de propagation) est une autre excellente fonctionnalité d'ES6. Comme son nom l'indique, elle prend un itérable (comme un tableau) et l'étend (étale) en éléments individuels.

Nous pouvons également étendre des objets en utilisant la syntaxe de propagation et copier ses propriétés `énumérables` vers un nouvel objet.

La syntaxe de propagation nous aide à `cloner` un objet et un tableau avec la syntaxe la plus simple en utilisant les trois points `...`, comme ceci :

```js
const clone_some_object = {...some_object}
```

Cela est extrêmement utile dans React lorsque vous réinitialisez une variable d'état avec une nouvelle instance d'un objet et d'un tableau pour aider à réafficher le composant.

Le paramètre `Rest` est en quelque sorte l'opposé de la syntaxe de propagation. Alors que la syntaxe de propagation aide à étendre ou à propager des éléments et des propriétés, le paramètre Rest aide à les collecter ensemble.

[Consultez la deuxième moitié de cet article](https://www.freecodecamp.org/news/javascript-object-destructuring-spread-operator-rest-parameter/) pour en savoir plus sur l'opérateur de propagation et le paramètre Rest.

## 7. Comment utiliser les classes en JavaScript

La `classe` d'ES6 est une autre excellente inclusion qui vous aide à écrire de la programmation orientée objet en JavaScript.

```js
class Employee {
	constructor(name) {
		this.name = name;
	}

	greeting() {
		return `Hello, ${this.name}`;
	}
}


let emp = new Employee("Tapas");
emp.greeting(); // "Hello, Tapas"
```

Nous pouvons également créer une classe en l'étendant à partir d'une classe existante. Dans React, nous pouvons créer des composants de deux manières :

* En utilisant une classe
* En utilisant une fonction.

Voici un exemple de la façon dont nous pouvons créer un composant React en utilisant une classe ES6 :

```js
class Greeting extends React.Component {
	render() {
		return <span>Hello World!</span>;
	}
}
```

[Vous pouvez regarder cette vidéo](https://www.youtube.com/watch?v=2ZphE5HcQPQ) sur la chaîne YouTube freeCodeCamp pour en savoir plus sur les classes ES6.

En plus de ceux-ci, connaître la boucle `for-of`, `async-await`, l'`opérateur ternaire`, etc., serait très utile.

# Architecture des composants

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-177.png)
_Architecture des composants - Plusieurs valent mieux qu'un seul._

Bienvenue dans la deuxième section de l'article. Parlons des `composants`. Si nous parlons de React, nous devons parler des composants.

Un seul fichier de code source contient toutes les fonctionnalités d'une application. Mais cela crée certains des problèmes que vous voulez éviter en tant que développeur. En voici quelques-uns que j'ai rencontrés (et il pourrait y en avoir beaucoup d'autres) :

* Plusieurs développeurs travaillant sur l'application peuvent augmenter les problèmes de collaboration comme les conflits de fusion, le travail indépendant, etc.
* La réutilisabilité du code diminue et la répétition augmente.
* L'équipe finit par travailler dans un modèle monotâche et la livraison finale devient lente.
* Tester votre application en tant qu'unité n'est plus possible. Vous touchez toujours l'ensemble de l'application lorsque vous modifiez le fichier unique.
* Votre designer ne l'aimera pas.

Lorsque vous travaillez avec React, vous allez diviser votre application en autant d'unités petites que possible, appelées composants. Chacun des composants devrait idéalement ne faire qu'une seule chose.

Alors, comment mettre cela en pratique ? Apprenons comment avec un exemple.

## Comment visualiser une application React comme un ensemble de composants

Supposons que nous construisons une application web utilisant React qui liste les résultats de chaque étudiant par leurs notes. Notre designer a conçu une maquette, comme montré ci-dessous. Ce que nous voyons est le suivant :

* Une navigation supérieure avec un logo et le nom de l'application.
* Une répartition claire des résultats par notes.
* Il montre le résultat des trois meilleurs étudiants de chaque classe.
* Il y a une option `voir tout` pour voir tous les résultats d'une classe.
* Nous pouvons rechercher le résultat de n'importe quel étudiant en recherchant le nom de l'étudiant.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/e-results-1.png)
_Une application web imaginaire : e-results_

Maintenant, nous devons commencer à penser aux composants. Cela signifie comment diviser cette application en unités logiques qui prennent en charge une seule responsabilité.

Il n'y a pas nécessairement une seule réponse. C'est bien, mais nous devons nous assurer que nous faisons un meilleur travail de création de composants.

Voici comment nous pouvons le faire :

* Un composant racine appelé `App`.
* Un composant `Nav` pour la navigation supérieure.
* Un composant `Results` qui est toute la page sauf le `Nav`.
* Un composant `Search`.
* Un composant `Scores` qui peut inclure tous les scores.
* Un composant `Score` qui contient un en-tête, un tableau de scores et le lien voir tout.
* Un composant `ScoreHeading` qui contient un en-tête comme, `Grade 1`.
* Un composant `ScoreList` qui contient le tableau de scores.

L'image ci-dessous les montre en les marquant avec différentes couleurs.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/website-structure-1.png)
_Penser en composants_

Super, nous avons maintenant tous les composants. Nous devons donc commencer à penser à la composition des composants. Que signifie cela ?

Ces composants sont effectivement des unités isolées qui sont chacune censées faire une seule chose. Cependant, la plupart des composants dans une application React seront liés les uns aux autres par des données.

Nous devons également ajouter des composants les uns aux autres afin que ces unités construisent finalement l'ensemble de l'application.

À partir de l'image ci-dessous, vous pouvez comprendre comment ces composants peuvent être composés.

* Le composant `App` est un composant de niveau racine qui a deux autres composants, `Nav` et `Results`.
* Le composant `Nav` a un logo et un en-tête.
* Le composant `Results` a un composant `Search` et un composant `Scores`.
* Un composant `Scores` peut avoir plusieurs composants `Score`.
* Chacun des composants `Score` a un composant `ScoreHeading` et `ScoreList`.

L'image ci-dessous a-t-elle du sens pour vous ?

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Component-tree.png)
_L'arborescence des composants_

Voici une autre façon de le visualiser :

![Image](https://www.freecodecamp.org/news/content/images/2021/02/Component-hierarchy.png)
_La hiérarchie des composants_

Chacun de ces composants gère et utilise des données en utilisant deux concepts importants, qui sont `props` et `state`.

## Props vs State dans React

Dans React, `props` et `state` sont les moyens de base dont vous disposez pour gérer les données à l'intérieur et entre les composants.

* `Props` : sont les variables passées par un composant parent à ses enfants. En utilisant le composant props, nous pouvons passer les données requises à ses enfants dans la hiérarchie.
* `State` : De l'autre côté, `state` est la variable qu'un composant gère en interne. Dans de nombreux cas, une variable d'état d'un composant peut être initialisée par les données qui lui sont passées en utilisant props.

# L'écosystème NPM

![Image](https://www.freecodecamp.org/news/content/images/2021/02/image-180.png)
_Écosystème NPM - Construire, Tester et Publier_

Nous voici à la dernière section de l'article. Cette section expliquera pourquoi connaître l'écosystème NPM vous rend plus à l'aise avec React.

## Qu'est-ce que NPM ?

`NPM` est le gestionnaire de paquets pour la plateforme `Node.js`. Il se compose de modules que Node peut trouver et il aide Node à gérer les conflits de dépendances de manière intelligente. Le plus souvent, il est utilisé pour publier, découvrir, installer et développer des programmes.

Vous pouvez trouver plus d'informations sur `NPM` [ici](https://docs.npmjs.com/cli/npm).

## Pourquoi dois-je connaître NPM ?

React en lui-même est une petite bibliothèque qui vous permet de créer des composants et de construire des applications web complètes. Cependant, vous aurez souvent besoin d'utiliser quelque chose que React ne propose peut-être pas directement.

Par exemple, pour une gestion d'état extensive, vous pourriez vouloir utiliser `Redux`. Vous pourriez opter pour une bibliothèque externe qui aide avec cela, et cette bibliothèque est disponible sous la forme d'un paquet `NPM` que vous pouvez télécharger et installer.

De même, des paquets npm existent pour diverses utilités, bibliothèques de graphiques, externalisation de chaînes, routage – vous l'appelez, et il y a probablement un paquet pour cela.

## L'état d'esprit `Open-Source`

Que faire si vous ne trouvez pas une fonctionnalité spécifique que vous recherchez en tant que module npm existant ? Oui, cela peut arriver. De plus, elle peut être disponible en tant que paquet npm existant, mais elle ne répond pas à vos besoins tels quels. Que faites-vous alors ?

Il existe deux façons simples de gérer cette situation :

* Vous construisez cette fonctionnalité en tant que composant, vous la testez et vous la publiez en tant que paquet npm open-source.
* Vous contribuez à un paquet npm open-source existant et vous l'améliorez.

Il est tout à fait naturel d'avoir un état d'esprit open-source en tant que développeur React. Recherchez activement des opportunités pour créer quelque chose de nouveau ou contribuer à quelque chose qui existe déjà. C'est une excellente sensation lorsque votre travail est utilisé et apprécié par quelqu'un de la même manière que vous utilisez le travail de quelqu'un d'autre.

J'ai créé un [projet open-source](https://github.com/atapas/react-package-publisher) pour aider à publier rapidement des paquets npm en utilisant un script. N'hésitez pas à y jeter un coup d'œil, à le forker et à contribuer. Vous pourriez le trouver utile.

# Avant de terminer...

J'espère que vous avez trouvé cet article perspicace et qu'il vous aidera à commencer à utiliser ces concepts de manière plus efficace. Restons en contact. Vous me trouverez actif sur [Twitter (@tapasadhikary)](https://twitter.com/tapasadhikary). N'hésitez pas à me suivre.

Vous pourriez également aimer ces articles :

* [Comment apprendre quelque chose de nouveau chaque jour en tant que développeur de logiciels](https://www.freecodecamp.org/news/learn-something-new-every-day-as-a-software-developer/)
* [Comment créer un formulaire React avec un seul gestionnaire d'événements de changement ?](https://blog.greenroots.info/how-to-create-react-form-with-a-single-change-event-handler-ckizqh0yq00x7zks16wd1cxu1)
* [16 dépôts GitHub de projets secondaires que vous pourriez trouver utiles](https://blog.greenroots.info/16-side-project-github-repositories-you-may-find-useful-ckk50hic406quhls1dui2d6sd)
* [Comprendre les imports dynamiques, Lazy et Suspense en utilisant les hooks React](https://blog.greenroots.info/understanding-dynamic-imports-lazy-and-suspense-using-react-hooks-ckdfssktb01czpts12krebs1h)