---
title: Apprendre React – Un Guide des Concepts Clés
subtitle: ''
author: Ankur Tyagi
co_authors: []
series: null
date: '2024-01-06T01:52:22.000Z'
originalURL: https://freecodecamp.org/news/learn-react-key-concepts
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/Orange
seo_title: Apprendre React – Un Guide des Concepts Clés
---

Yellow-Gradient-Make-Design-Blog-Banner--56-.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: null
seo_desc: 'Bienvenue dans ce guide complet pour apprendre React. Si vous cherchez une approche efficace et bien pensée pour comprendre les fondamentaux de React, vous avez trouvé la perle rare.

Ce guide suit la règle 80/20 – nous nous concentrerons sur quelques concepts clés de React que vous utiliserez dans la majorité de votre travail avec React.

J'ai créé cette ressource pour les développeurs débutants et intermédiaires. Dans ce guide, je couvrirai tous les concepts de base que vous devez connaître pour commencer avec React.

Êtes-vous prêt à construire votre première application React ? Commençons.

À la fin de ce guide, vous devriez avoir une compréhension solide des bases de React, y compris :

* **[Qu'est-ce que React ?](#heading-quest-ce-que-react)**
* **[Combien de JavaScript devez-vous connaître avant d'apprendre React ?](#heading-combien-de-javascript-devez-vous-connaître-avant-dapprendre-react)**
* **[Pourquoi](#heading-pourquoi-apprendre-react) **apprendre React ?****
* **[Comment installer React](#heading-comment-installer-react)**
* **[Concepts clés à comprendre dans React](#heading-concepts-clés-à-comprendre-dans-react)**
* **[Qu'est-ce que JSX ?](#heading-quest-ce-que-jsx)**
* **[Qu'est-ce que l'état React ?](#heading-quest-ce-que-letat-react)**
* **[Props dans React](#heading-props-dans-react)**
* **[Comment afficher des éléments de liste dans React](#heading-comment-afficher-des-éléments-de-liste-dans-react)**
* **[Gestionnaires d'événements React](#heading-gestionnaires-devenements-react)**
* **[Hooks React](#heading-hooks-react)**
* **[Flux de données dans React](#heading-flux-de-données-dans-react)**

Ces sujets formeront la base de tous les concepts avancés que vous apprendrez plus tard.

Ce guide est une excellente ressource pour les programmeurs JavaScript qui commencent à apprendre React.

## Qu'est-ce que React ?

React est une bibliothèque JavaScript pour construire des interfaces utilisateur d'applications web.

Elle est open-source et développée par Facebook. Avec React, vous pouvez créer une application web rapide et évolutive en décomposant l'UI en composants plus petits.

React adopte un style déclaratif, mais que signifie cela ? Vous avez peut-être rencontré les termes impératif et déclaratif dans les discussions sur le codage, alors décomposons cela.

Dans le codage impératif, vous instruisez l'ordinateur sur les étapes à suivre pour obtenir le résultat.

**Voici un exemple :**

```javascript
let num = [1,2,3,4];
let tripled  = [];
for(let i = 0; i < num.length; i++){
    let newNum = num[i] * 3;
    tripled.push(newNum)
}
console.log(tripled)   // [ 3, 6, 9, 12 ]
```

Dans le code ci-dessus, nous donnons des instructions étape par étape pour effectuer certaines tâches. Si nos instructions sont incorrectes, la machine pourrait ne pas donner le résultat attendu. Elle ne fait que ce que nous lui instruisons clairement de faire.

En revanche, dans la programmation déclarative, nous déclarons notre résultat souhaité, et l'ordinateur détermine les étapes pour l'atteindre.

**Voici un exemple :**

```javascript
let num = [1,2,3,4];
let tripled = num.map((n) =>  n * 3);
console.log(tripled)  // [ 3, 6, 9, 12 ]
```

À chaque cycle, le programme multiplie le num par trois et l'ajoute à un tableau.

Nous ne fournissons pas d'instructions étape par étape, pourtant les actions sont exécutées. Cette approche déclarative est ce qui fait que React fonctionne si efficacement, et c'est l'une de ses caractéristiques marquantes.

## Combien de JavaScript devez-vous connaître avant d'apprendre React ?

La question initiale est souvent, à quel point devez-vous connaître JavaScript avant de vous attaquer à React ? Je pense qu'il est important d'avoir une solide compréhension des concepts de base de JavaScript avant de plonger dans un framework ou une bibliothèque, car cela vous bénéficiera à long terme.

%[https://x.com/TheAnkurTyagi/status/1422558697302249480?s=20]

Disons que vous voulez devenir développeur web et que vous voulez utiliser React comme votre technologie principale.

Voici une feuille de route de haut niveau que vous pouvez utiliser pour vous assurer d'avoir les connaissances nécessaires :

* Apprenez les bases de [JavaScript](https://theankurtyagi.com/a-simple-and-effective-way-to-learn-practice-javascript/).
* Apprenez les pages web et les technologies de développement web comme [HTML et CSS](https://www.freecodecamp.org/news/learn-html-and-css-from-the-ceo-of-scrimba/).
* [Apprenez les bases de Node.js et Express](https://www.freecodecamp.org/news/free-8-hour-node-express-course/).
* Soyez capable d'écrire une sorte d'application web simple Node.js.
* Apprenez les différents frameworks (React) et technologies que les développeurs utilisent pour développer des applications Node.js.
* Apprenez une sorte de [base de données à utiliser avec Node.js](https://www.freecodecamp.org/news/full-stack-project-create-a-recipe-app-using-react-node-js/).
* Apprenez les bases de l'informatique, comme [les algorithmes et les structures de données](https://www.freecodecamp.org/news/learn-data-structures-and-algorithms/).
* Apprenez [les meilleures pratiques pour écrire du bon code](https://www.freecodecamp.org/news/how-to-write-clean-code/).
* Apprenez comment [concevoir l'architecture](https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/) d'une application React.js.

Avoir un plan en place est important. Vous pouvez toujours changer et adapter le plan, mais si vous n'avez pas de plan au départ, vous allez errer sans but et vous pourriez finir frustré et être plus susceptible d'abandonner.

Donc la réponse simple à cette question est, une fois que vous êtes confiant dans vos bases de JavaScript, allez-y et commencez à apprendre et à construire des projets avec React. Vous pouvez [lire cet article](https://www.freecodecamp.org/news/p/e2f91d79-f9c6-40a8-a53f-e61601faaeca/You%20can%20read%20more%20about%20the%20core%20JS%20concepts%20you%20should%20know%20in%20this%20guide.) pour vous assurer de comprendre ces concepts fondamentaux de JS.

Le domaine de la technologie évolue rapidement avec de nouveaux langages ou frameworks qui sortent souvent. Si vous vous concentrez sur la construction d'une base solide, vous serez prêt à plonger.

%[https://twitter.com/TheAnkurTyagi/status/1637061346708844545]

Voici quelques ressources utiles supplémentaires pour apprendre JavaScript :

* [Cours JS de freeCodeCamp](https://www.freecodecamp.org/learn/)
* [Le tutoriel moderne de JavaScript](https://javascript.info/)
* ['33 concepts JavaScript' sur GitHub](https://github.com/leonardomso/33-js-concepts)
* [Documentation officielle JS (MDN)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

## Pourquoi apprendre React ?

Il y a plusieurs raisons pour lesquelles apprendre cette bibliothèque JavaScript populaire est bénéfique.

En voici quelques-unes :

* React est bien aimé dans le développement frontend grâce à ses composants UI réutilisables, sa flexibilité et sa facilité de débogage. Cela aide les développeurs à construire des applications web plus efficacement.
* Il est probable que vous rencontriez un projet React dans votre travail actuel ou futur.
* Pour un programmeur JavaScript, il est courant de rencontrer des questions basées sur React lors des entretiens d'embauche.
* De nombreux frameworks ou bibliothèques, comme NextJs et Gatsby, sont construits sur React.
* React améliore vos compétences de développement car il encourage les bonnes pratiques. Il vous aide à considérer le flux de données et la gestion de l'état global dans vos applications, ainsi que ses modèles de conception qui vous incitent à penser à divers scénarios et cas limites.

Pour plus d'informations, vous pouvez lire mon article sur [Pourquoi vous devriez apprendre React](https://theankurtyagi.com/why-you-should-learn-reactjs/).

### Comment React se distingue des autres outils de l'écosystème JavaScript

Tout d'abord, React est rapide car il utilise le DOM virtuel pour afficher les données, mettant à jour uniquement les parties modifiées lorsque les données changent.

React encourage également la décomposition du code en petits morceaux réutilisables. Cela le rend gérable plutôt que de s'attaquer à une grande base de code d'un seul coup.

Au-delà de cela, React simplifie le débogage et accélère le développement à grande échelle.

Il est également compatible avec le SEO, ce qui est crucial pour la visibilité des entreprises sur les moteurs de recherche comme Google. Et étant open-source avec une grande communauté, React offre un soutien abondant et une variété d'outils et d'extensions pour faciliter son utilisation et son débogage.

Maintenant, avec une meilleure compréhension des avantages de React, passons à l'installation de React dans notre environnement de développement local.

## Comment installer React

Tout d'abord, vous devez installer Node.js. Il vous permet d'exécuter du code JavaScript et de faire tourner des applications React sur votre ordinateur.

Vous pouvez l'installer depuis le [site web](https://nodejs.org/en) et vérifier sa version actuelle en utilisant l'extrait de code ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/image-99.png)
_Configuration de l'environnement de développement local_

Assurez-vous d'avoir Node 14.0.0 ou supérieur sur votre machine pour installer la dernière version de React.

Ensuite, pour configurer rapidement une application React, il y a plusieurs façons de procéder. Si vous le souhaitez, vous pouvez utiliser l'outil officiel, create-react-app. Exécuter `npx create-react-app my-app` téléchargera la dernière version de React. Mais cette méthode n'est plus recommandée pour installer React.

Au lieu de cela, vous pouvez créer une application React en utilisant [Vite](https://vitejs.dev/), qui est un environnement de développement pour les applications modernes.

Exécutez l'extrait de code ci-dessous dans votre terminal, fournissez un nom pour votre projet, et sélectionnez React comme framework.

```bash
npm install
```

Démarrez le serveur de développement en exécutant `npm run dev` dans votre terminal.

L'application sera lancée sur votre port local `5173` par défaut.

Maintenant, nous sommes prêts à plonger dans les concepts de base de React.

## Concepts clés à comprendre dans React

### Composants React

Le navigateur retourne un ensemble d'éléments React, appelés composants, qui apparaissent sur l'écran de l'ordinateur.

Dans React, une page web peut être divisée en plusieurs composants qui constituent tous les éléments à l'écran. Cela nous aide à adhérer au principe DRY (Don't Repeat Yourself) et à écrire un code plus propre.

React divise l'UI en morceaux indépendants et réutilisables (composants). Chaque nom de composant doit commencer par une majuscule, ce qui le rend lisible. Ils ont leurs propres styles, API, logique et structures.

Il existe deux types de composants React :

* Composants de classe ou avec état
* Composants fonctionnels ou sans état

#### Composants de classe (avec état)

Cette méthode pour créer des composants React est considérée comme obsolète. Bien qu'elle soit toujours supportée par React, elle n'est pas recommandée car les nouvelles fonctionnalités de React sont basées sur les composants fonctionnels et les hooks.

Les composants de classe sont déclarés en utilisant le mot-clé class de JavaScript. Ils sont appelés `avec état` car les variables à l'intérieur des composants sont liées à eux en utilisant le mot-clé `this` de JavaScript.

Pour créer des composants de classe, vous devez étendre le composant React par défaut qui contient une fonction constructeur avec tous les états requis. Le composant de classe affiche ses éléments via une fonction render.

Considérons un composant Hello World en utilisant les composants de classe.

```javascript
import React, { Component } from 'react';

class HelloWorld extends Component {
  constructor(props) {
    super(props);
    // Initialiser l'état
    this.state = {
      greeting: 'Bonjour, le monde !'
    };
  }

  render() {
    return (
      <div>
        <h1>{this.state.greeting}</h1>
      </div>
    );
  }
}
```

L'extrait de code ci-dessus crée un composant de classe avec un état appelé greeting contenant une valeur "Bonjour, le monde !". L'état est déclaré en utilisant le mot-clé this.state et la méthode render affiche ensuite la valeur de l'état greeting dans un élément h1.

Rappel : vous devez généralement éviter d'utiliser les composants de classe dans vos applications, et utiliser plutôt les composants fonctionnels – que nous allons discuter maintenant.

#### Composants fonctionnels (sans état)

Les composants fonctionnels sont une manière moderne d'écrire React. Ils suivent la méthode ES6 de JavaScript pour écrire des fonctions. Un composant fonctionnel accepte un seul argument connu sous le nom de props (données d'objet), principalement retourné avec un élément JSX.

Les composants fonctionnels reçoivent des données sous forme de props provenant de différents composants. Vous apprendrez comment gérer l'état un peu plus tard dans ce guide.

Considérons l'exemple ci-dessous :

```javascript
import "useState" from "react"
function App() {
  const [name, addName] = useState('');
  function handleAddName(event) {
    addName(event.target.value);
  }
  return (
    <div>
      <form>
      <label>
        Nom :
        <input type="text" value={name} onChange={handleAddName} />
      </label>
      </form>
      <p>
        Bienvenue {name}, j'espère que vous apprendrez beaucoup dans ce manuel.
      </p>
    </div>
  );
}
```

Les composants fonctionnels sont déclarés de manière similaire aux fonctions JavaScript. La différence est que les composants acceptent les props et rendent les éléments JSX. Vous en apprendrez plus sur JSX ensuite.

## Qu'est-ce que JSX ?

Chaque composant que vous voyez utilise JSX. Le meilleur aspect de React est que vous pouvez facilement intégrer JavaScript dans JSX. Cela vous donne la flexibilité de construire des interfaces utilisateur rapides. Mais attendez, qu'est-ce que JSX ?

[JSX](https://legacy.reactjs.org/docs/introducing-jsx.html) signifie JavaScript Syntax Extension, et il vous permet d'utiliser une syntaxe similaire à HTML dans vos composants React.

Une fonction appelée `React.createElement()` nous permet de créer des éléments JSX dans React. Elle accepte trois arguments – l'élément HTML, un objet contenant les attributs de l'élément HTML, et le contenu de l'élément HTML.

Voyons quelques exemples : L'extrait de code ci-dessus crée un bouton qui affiche « Cliquez ici » avec des attributs de couleur de fond et de texte.

```javascript
React.createElement(
'button',
{ color : 'white', backgroundColor: 'blue'},
'Cliquez ici'
)
```

Mais les développeurs ne créent pas d'éléments JSX de cette manière. En fait, vous n'avez pas besoin d'utiliser la fonction `React.createElement()` car elle crée beaucoup de lignes de code inutiles et il sera difficile de créer des éléments JSX profondément imbriqués.

Au lieu de cela, React fournit une manière plus facile d'écrire des éléments JSX. Ils sont similaires aux éléments HTML et acceptent un attribut appelé `className` qui remplace l'attribut class en HTML.

Il y a deux règles concernant les éléments JSX :

* `class` est un mot-clé JavaScript. Par conséquent, utilisez `className` au lieu de class lorsque vous stylez vos éléments JSX.
* Un composant ne peut retourner qu'un seul élément JSX. Mais lorsque vous devez afficher plus d'un élément JSX, placez-les dans un seul élément conteneur.

Voyons quelques exemples :

```javascript
function Greeting() {
  return (
  <h1 className="heading">Bienvenue dans React</h1>
  );
}
```

L'extrait de code ci-dessus montre un composant Greeting qui retourne un seul élément JSX. Il affiche « Bienvenue dans React » en utilisant l'élément h1. L'attribut className ajoute le style « heading » à l'élément JSX.

Considérons un autre composant qui retourne plusieurs éléments JSX :

```javascript
function Greeting() {
  return (
<div>
  <h1 className="heading">Bienvenue dans React</h1>
 <p>Ce message est sponsorisé par FreeCodeCamp
</div>
  );
}
```

L'extrait de code ci-dessus retourne plus d'un élément JSX imbriqué dans un élément parent. Il est donc important de noter que tous les éléments JSX doivent être dans un conteneur parent.

### Quelle est la différence entre HTML et JSX ?

La syntaxe JSX ressemble à HTML. En HTML, nous utilisons les attributs de classe pour le style. En JavaScript, « Class » est un mot réservé. Nous ne pouvons donc pas utiliser le mot-clé class. Pour cela, React utilise `className` au lieu de Class comme valeur par défaut pour le style.

Considérons l'exemple ci-dessous :

```html
<!DOCTYPE html>
<html lang="en">
    <head>
        <style>
            .heading {
                color: #3498db;
            }

            .paragraph {
                font-size: 18px;
            }
        </style>
    </head>
    <body>
        <h1 class="heading">Bienvenue dans React</h1>
        <p class="paragraph">Bon apprentissage</p>
    </body>
</html>
```

L'extrait de code ci-dessus montre un document HTML qui affiche un élément de titre et de paragraphe sur la page web. Les éléments sont stylisés en utilisant le sélecteur de classe CSS (attribut de classe HTML).

Recréons cela avec des éléments JSX :

```javascript
'const App = () => {
    return (
        <div>
            <h1 className='heading'>Bienvenue dans React</h1>
            <p className='paragraph'>Bon apprentissage</p>
        </div>
    );
};
```

L'extrait de code ci-dessus affiche les éléments JSX de titre et de paragraphe et utilise l'attribut className pour styliser chacun d'eux. Vous pouvez ajouter un fichier CSS contenant vos styles dans votre projet.

## Qu'est-ce que l'état React ?

L'état est un concept clé dans les applications React. Vous pouvez penser à l'état comme une collection d'informations ou d'objets qui vous indiquent où vous pouvez accéder et stocker vos données. Tout ce qui est en dehors d'un composant, par exemple, ne peut pas accéder à ses données. Il est privé et contrôlé par le composant.

Chaque composant React a son propre état. Chaque fois qu'un état change, le composant est **re-rendu**. Cela se produit lorsqu'un utilisateur clique sur un bouton, répond ou interagit avec quelque chose sur la page.

Les composants enfants peuvent accéder à ces états via les props (que nous discuterons ci-dessous) passés par le composant parent.

Considérons quelques exemples d'état React :

```javascript
const [name, setName] = useState("")
const [age, setAge] = useState(0)
const [products, setProducts] = useState(["riz", "haricots"])
```

L'extrait de code ci-dessus montre quelques exemples d'états React. Un état peut être un tableau, une chaîne, un objet ou un nombre. Le hook useState accepte la valeur initiale de l'état comme paramètre, et le nom de l'état et la fonction d'état (pour modifier sa valeur) sont déstructurés du hook useState.

```javascript
const [stateName, stateFunction]= useState(<initial_value>)
```

Considérons un formulaire qui accepte le nom et l'âge d'un utilisateur et les affiche, comme ceci :

```javascript
function UserInfo() {
  const [name, setName] = useState('');
  const [age, setAge] = useState(0);

  function handleNameChange(event) {
    setName(event.target.value);
  }
  function handleAgeChange(event) {
    setAge(parseInt(event.target.value));
  }
  return (
    <div>
      <form>
      <label>
        Nom :
        <input type="text" value={name} onChange={handleNameChange} />
      </label>
      <label>
        Âge :
        <input type="number" value={age} onChange={handleAgeChange} />
      </label>
     </form>
      <p>
        Votre nom est {name} et votre âge est {age}.
      </p>
    </div>
  );
}
export default UserInfo;

```

L'extrait de code ci-dessus accepte le nom et l'âge de l'utilisateur et les stocke dans les états React. Les fonctions `handleNameChange` et `handleAgeChange` acceptent l'entrée de l'utilisateur et mettent à jour les valeurs de l'état.

### État global vs État local dans React

Les états globaux font référence aux valeurs d'état utilisées dans plusieurs composants au sein de l'application. Dans certains cas, ils peuvent être mis à jour n'importe où dans l'application.

Par exemple, lorsqu'un utilisateur passe du mode sombre au mode clair tout en utilisant votre application. Cet état affecte la vue globale de l'application pour s'assurer que tous les composants changent de couleur.

Pour cela, vous devrez peut-être déclarer un état comme ceci :

```javascript
const [darkmode, setDarkMode] = useState(false)
```

Cet état est mis à jour lorsqu'un utilisateur bascule un interrupteur dans l'application. Cet état est global car il est passé dans tous les composants de l'application pour s'assurer que leurs vues changent en fonction de la valeur de l'état.

Voyons un exemple :

```javascript
const App = () => {
  const [darkMode, setDarkMode] = useState(false);
  return (
    <div>
      <Home darkMode={darkMode} />
      <Profile darkMode={darkMode} setDarkMode={setDarkMode}>
    </div>
  );
};
```

Dans l'extrait de code ci-dessus, nous avons un composant App et un composant Profile. Le composant App est un composant d'ordre supérieur qui rend deux composants et contient un état appelé `darkMode` qui bascule l'humeur de l'application.

Les sous-composants (Home et Profile) acceptent les états et mettent à jour la couleur de leurs éléments en fonction de la valeur de l'état.

Dans le composant Profile, darkMode est un état global, et `name` est un état local car l'état name est déclaré et lié uniquement au composant Profile, et darkMode est disponible pour d'autres états en plus du composant App.

**Les états locaux** sont des variables d'état liées à un composant. Ils sont utilisés en dehors de ce composant, ce qui signifie qu'ils sont locaux à ce composant.

Par exemple, l'état name est local au composant Profile :

```javascript
const Profile = () => {
  const [name, setName] = useState("Ankur");
  const toggleName = () => setName("Tyagi");
  return (
    <div>
      <h1>Salut, je suis {name}</h1>
      <button onClick={toggleName}> Changer de nom </button>
    </div>
  );
};
```

L'extrait de code ci-dessus bascule l'état name entre "Ankur" et "Tyagi" lorsqu'un utilisateur clique sur le bouton, et l'état n'est utilisé nulle part en dehors du composant Profile.

## Props dans React

Les props sont des données transférées d'un parent à un composant enfant. Les props ne peuvent pas être modifiées, car elles sont en lecture seule. Un composant enfant ne peut pas changer les valeurs des props reçues du composant parent.

Le diagramme ci-dessous montre qu'un composant accepte les props d'un autre composant et les affiche sous forme d'éléments JSX dans le composant.

![Image](https://lh7-us.googleusercontent.com/5r8Vl6fru32HhsepLC-r1liB6d1czoCjJSavSB_6eennnn3R8btkofqNSyytEEopXOLDpLBcN986CqV3GOyAtnw-LZuH5jHuavMUCF5-E9YDhrX0O1lkah1dtka2WzJppeurGjcGs8dllIZ8zE1Mjwk)
_Diagramme montrant comment fonctionnent les props_

Par exemple, considérons une application qui permet aux utilisateurs de basculer le thème de l'application.

```javascript
const App = () => {
  const [darkMode, setDarkMode] = useState(false);
  return (
    <div>
      <Home darkMode={darkMode} />
      <Profile darkMode={darkMode} setDarkMode={setDarkMode}>
    </div>
  );
};
```

L'extrait de code ci-dessus montre que les composants Home et Profile acceptent l'état darkMode et sa fonction en tant que props. Le composant Home accepte la valeur darkMode et le composant Profile accepte la valeur de l'état et sa fonction.

Maintenant, comment accéder aux valeurs des props dans ces composants ? Vous pouvez le faire via une méthode appelée Destructuring.

### Destructuring des props dans React

La destructuration des props est un phénomène simple similaire à la manière dont nous obtenons les valeurs des objets en JavaScript. Voyons un exemple :

```javascript
const profile = {
 name: "Ankur Tyagi",
 age: 22,
 role: "Rédacteur Technique",
};
```

Dans l'extrait de code ci-dessus, l'objet contient une propriété name, age et role. En JavaScript, vous pouvez obtenir les valeurs de chaque propriété en utilisant objectName.<propertyName>

Par conséquent, vous pouvez accéder à chaque valeur comme montré ci-dessous :

```javascript
console.log(profile.name)  //"Ankur Tyagi"
console.log(profile.age) //22
console.log(profile.role) //"Rédacteur Technique"
```

Cependant, la destructuration fournit une meilleure et beaucoup plus propre manière d'obtenir les valeurs dans un objet ou un tableau.

```javascript
const profile = {
 name: "Ankur Tyagi",
 age: 22,
 role: "Rédacteur Technique",
};
//Destructuration de l'objet
const { name, age, role } = profile;
console.log(`Mon nom est ${name}. Je suis un ${role} et j'ai ${age} ans`);

const friends = ["Tejas", "Brad", "Ankit"]
//Destructuration du tableau
const [first, second, third] = friends

console.log(first)
```

Dans l'extrait de code ci-dessus, les propriétés de l'objet et les valeurs du tableau sont déstructurées du parent nous permettant de référencer chaque valeur en utilisant le nom de la propriété ou un nom de variable. La destructuration fournit une manière plus propre d'accéder aux valeurs dans un objet ou un tableau.

Mais React utilise cette syntaxe ES6 pour simplifier la manière dont vous accédez aux valeurs dans les objets et les tableaux et aux valeurs des props. Notez que lorsque vous passez des données dans les composants via les props, les données sont ajoutées en tant que propriété à l'objet props.

```javascript
const App = () => {
  const [darkMode, setDarkMode] = useState(false);
  return (
    <div>
      <Home darkMode={darkMode} />
      <Profile darkMode={darkMode} setDarkMode={setDarkMode}>
    </div>
  );
};
```

Le composant Profile déstructure les valeurs darkMode et setDarkMode de l'objet props, nous permettant ainsi d'interagir directement avec les données.

Chaque composant React a un objet props par défaut qui permet le partage de données entre les composants et vous pouvez accéder à la valeur des props en utilisant l'une des méthodes de destructuration ci-dessous :

```javascript
const Component = (props) => {
```

### État vs Props

L'état et les props sont utilisés pour contenir des données dans une application React. Mais ils servent à des fins différentes.

* Les états sont mutables, et les props sont immuables. Les données stockées dans un état peuvent être modifiées, tandis que les props ne peuvent pas être modifiées (lecture seule).

```javascript
const App = () => {
  //👇🏻 état
  const [name, setName] = useState("Ankur");
  ////👇🏻 modifier l'état
  const changeName = () => setName("Tyagi");

  return (
    <div>
      <Profile name={name} />
    </div>
  );
};

//👇🏻 accepte le nom en tant que props
const Profile = ({ name }) => {
  return (
    <div>
      <h1>Salut, je suis {name}</h1>
      <p>Bienvenue dans mon tutoriel</p>
    </div>
  );
};
```

L'extrait de code ci-dessus montre que lorsque vous déclarez un état, React vous permet de créer une fonction qui modifie la valeur de l'état. De plus, les états deviennent des props (lecture seule) lorsque vous les passez dans d'autres composants.

* L'état est local à un composant tandis que les props proviennent d'un composant parent. Dans l'extrait de code ci-dessus, l'état name est local au composant App mais devient une prop lorsqu'il est passé dans le composant Profile.

## Comment afficher des éléments de liste dans React

Jusqu'à présent, vous avez vu comment afficher les valeurs des états et des props dans les éléments JSX dans React. Mais dans certains cas, vous devrez peut-être afficher des éléments de liste sur une page web – par exemple, des données reçues d'un point de terminaison d'API. Comment rendre cela dans React ? Vous allez l'apprendre bientôt.

Considérons l'extrait de code suivant qui rend une liste de produits alimentaires :

```javascript
export default function App() {
  const products = ["Riz", "Haricots", "Ignames", "Œufs"]
  return (
    <div>
      <ul>
        {products.map((item) => (
          <li>{item}</li>
        ))}
      </ul>
    </div>
  )
}
```

Dans React, la fonction JavaScript [array.map](https://docs.google.com/document/d/1fGaC-08J_Seh0s7X5NAMX_lz5WiPed2QMifd91QsJqA/edit#heading=h.bvln7ojdubhk)() est utilisée pour rendre les éléments de liste. Mais l'extrait de code est incomplet. Chaque élément de liste doit avoir une prop clé unique pour permettre à React de suivre chaque élément dans la liste.

![Image](https://lh7-us.googleusercontent.com/fzpTXQsNDQV3_vxZ_wKEKQepkzbnvXBMqhvjvZN2i9sRi2wCTct0Ao0KnjxbRs_Jz_rOz6ttXuDDxNprT7q89Tiw08OzWx3EckLPS3g9yIOXXv60QIjegMiwFUUu3gmquFUgQPkeuGrnhvh2y947nJ4)
_Avertissement indiquant que chaque enfant dans la liste doit avoir une prop clé unique._

Pour corriger cela, mettez à jour l'extrait de code comme montré ci-dessous :

```javascript
export default function App() {
  const products = ["Riz", "Haricots", "Ignames", "Œufs"]
  return (
    <div>
      <ul>
        {products.map((item, index) => (
          <li key={index}>{item}</li>
        ))}
      </ul>
    </div>
  )
}
```

La fonction [array.map](https://docs.google.com/document/d/1fGaC-08J_Seh0s7X5NAMX_lz5WiPed2QMifd91QsJqA/edit#heading=h.bvln7ojdubhk)() accepte deux arguments : l'élément de la liste et sa position dans le tableau. Vous pouvez donc définir la prop key à l'index (position de l'élément) pour permettre à React de distinguer chaque élément des autres.

La prop key optimise les performances de React et est utile pour effectuer des opérations CRUD avec les éléments de la liste.

Considérons une liste de tâches qui permet aux utilisateurs de créer et de supprimer des éléments de tâches.

```javascript
import { useState } from "react";

export default function App() {
  const [todoList, setTodoList] = useState([]);
  const [todo, setTodo] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    setTodoList([...todoList, { todo, id: Math.random() * 1000 }]);
    setTodo("");
  };
  const handleDelete = (id) => {
    const newTodoList = todoList.filter((item) => item.id !== id);
    setTodoList(newTodoList);
  };

  return (
    <div>
      <h1>Liste de tâches</h1>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          name='todo'
          id='todo'
          value={todo}
          onChange={(e) => setTodo(e.target.value)}
          required
        />
        <button type='submit'>Ajouter une tâche</button>
      </form>

      <div>
        {todoList.map((item) => (
          <div key={item.id}>
            <p>{item.todo}</p>
            <button onClick={() => handleDelete(item.id)}>Supprimer</button>
          </div>
        ))}
      </div>
    </div>
  );
}
```

La fonction `handleSubmit` accepte l'entrée de l'utilisateur et l'ajoute à la liste de tâches, et la fonction `handleDelete` supprime la tâche sélectionnée de la liste de tâches en utilisant son id.

L'extrait de code ci-dessus affiche les éléments de la liste de tâches et utilise les ids des éléments pour identifier chaque tâche lors de l'ajout et de la suppression d'éléments de la liste.

![Image](https://lh7-us.googleusercontent.com/vRUhBY660BL-aIScb_jK2opXIJZq-xh-KJsl91-g-1TIR9CqH1Z-iuxgR0oRHSO_D900oWk7yYgR-eulo8iTRJJBaClsAdwzyf4XH5AHWT1TXClRqaBjps7TecBpDr9Y5j-l2mEri7POJYaGhNoufmE)
_Exemple de liste de tâches - ajout et suppression d'éléments_

## Gestionnaires d'événements React

Lorsque nous cliquons sur un bouton ou interagissons avec l'interface utilisateur, nous nous attendons à une réponse. Cela est rendu possible avec les gestionnaires d'événements. Ces gestionnaires d'événements déterminent quelle action est effectuée lorsque l'utilisateur interagit avec eux (c'est-à-dire lorsqu'un événement est déclenché).

Si vous savez comment gérer les événements en JavaScript, ce ne sera pas si difficile de comprendre comment le faire dans React. Il y a juste quelques différences.

Dans React, les gestionnaires d'événements sont écrits en camelCase comme ceci : onClick, onChange, etc.

Voici un exemple qui montre la différence entre l'écriture de gestionnaires d'événements en HTML et React. Les deux extraits de code exécutent une fonction appelée handleClick lorsqu'un utilisateur clique sur le bouton.

En HTML :

```html
<button onclick="handleClick()">
Vous avez cliqué sur un bouton
</button>
```

Dans React :

```javascript
<button onClick={handleClick}>
Vous avez cliqué sur un bouton
</button>
```

Dans React, vous devez utiliser des gestionnaires d'événements lors de la soumission d'un formulaire et de la modification de la valeur d'un état. Voyons quelques exemples :

```javascript
import { useState } from "react";

export default function App() {
  const [todo, setTodo] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log({ todo });
  };

  return (
    <div>
      <h1>Liste de tâches</h1>
      <form onSubmit={handleSubmit}>
        <input
          type='text'
          name='todo'
          id='todo'
          value={todo}
          onChange={(e) => setTodo(e.target.value)}
          required
        />
        <button type='submit'>Ajouter une tâche</button>
      </form>
    </div>
  );
}
```

Il y a deux gestionnaires d'événements dans l'extrait de code ci-dessus : les gestionnaires `onSubmit` et `onChange`.

Le gestionnaire d'événements `onChange` met à jour l'état todo avec l'entrée du formulaire lorsque l'utilisateur entre une valeur dans le champ du formulaire.

Le gestionnaire d'événements `onSubmit` gère la soumission du formulaire. Dans la plupart des formulaires React, vous rencontrerez la fonction `event.preventDefault()`. Elle empêche la page de se recharger (action par défaut) chaque fois qu'un utilisateur soumet le formulaire.

## Hooks React

Les hooks sont une fonctionnalité critique de React qui ont été introduits dans la version 16.8.

Dans les composants de classe, nous rencontrons certains problèmes :

* Nous devons gérer l'auto-liaison et « This »
* Le code devient plus long, et plusieurs méthodes de cycle de vie sont difficiles à suivre.
* Il est difficile de partager la logique et de réutiliser les composants

Pour résoudre tous ces problèmes liés aux classes, l'équipe React a créé les hooks. Ils vous aident à écrire un code plus propre, plus lisible et plus maintenable. Alors apprenons quelques-uns des hooks et comment les utiliser.

### Le hook useState

useState est utilisé pour créer des variables d'état. Il nous permet de créer et de modifier des variables d'état dans nos composants.

useState retourne une paire de valeurs. La première est l'état actuel et la seconde est la fonction qui le met à jour.

```javascript
const [value, setValue] = useState(<initial Value>)
```

Créons un compteur en utilisant le hook useState :

```javascript
function Counter = () => {
  const [count, setCount] = useState(0);
```

Nous initialisons un état count et le définissons à « 0 ». La fonction handleClick modifie l'état count en utilisant la fonction setCount pour augmenter la valeur du compteur de 1.

L'extrait de code ci-dessous modifie l'état count lorsque l'utilisateur clique sur les boutons d'incrémentation et de décrémentation.

```javascript
function Counter = () => {
  const [count, setCount] = useState(0);
  function handleClickInc(){
    setCount(counter => counter + 1)
  }
  function handleClickDec(){
```

### Le hook useEffect

Le hook useEffect est un hook essentiel qui nous permet d'effectuer des actions lorsque divers changements se produisent dans un composant React, tels que la récupération de données, lorsqu'un composant est réaffiché, etc.

Le hook useEffect accepte deux paramètres : une fonction et un tableau de dépendances. La fonction est exécutée en fonction des conditions dans le tableau de dépendances.

```javascript
useEffect(()=> {
```

Il y a trois façons d'utiliser le hook useEffect :

* Sans tableau de dépendances
* Avec un tableau de dépendances vide
* Avec un tableau de dépendances contenant des valeurs.

#### Sans tableau de dépendances

Un hook useEffect sans tableau de dépendances s'exécutera chaque fois que le composant est réaffiché en raison d'un événement ou d'un changement d'état. Vous ne devriez pas utiliser le hook useEffect de cette manière car cela entraîne des problèmes de performance.

Supposons qu'il y ait un hook useEffect dans le composant Counter, il retournera lorsque le composant est monté sur la page et chaque fois que le compteur change.

```javascript
import { useEffect, useState } from "react"

export default function Counter() {
  const [count, setCount] = useState(0);

  const increment = () => setCount( prev => prev + 1)
  const decrement = () => setCount( prev => prev - 1)

  useEffect(() => {
    console.log("S'exécute chaque fois que le compteur change");
  });

  return (
    <div>
      <h1>Compteur : {count}</h1>
      <div>
        <button onClick={increment}>Augmenter</button>
        <button onClick={decrement}>Diminuer</button>
      </div>
    </div>
  );
}
```

Notez que vous devez éviter d'utiliser useEffect sans son tableau de dépendances – cela causera des problèmes de performance dans votre application.

#### Avec un tableau de dépendances vide

Un hook useEffect peut également contenir un tableau de dépendances vide. Cela signifie que la fonction dans la fonction useEffect doit s'exécuter une seule fois – lorsque le composant est monté ou chargé sur la page web.

Cette méthode est principalement utilisée lorsque vous devez récupérer des données à partir d'un point de terminaison d'API et les afficher sur la page web lorsqu'elle se charge.

Voici un exemple, la fonction useEffect s'exécute une seule fois (lorsque la page est montée). Un tableau de dépendances vide indique à React que le useEffect s'exécute une fois – lorsque le composant est rendu sur la page web.

```javascript
import { useEffect, useState } from "react"

export default function App() {
  const [count, setCount] = useState(0);

  const increment = () => setCount( prev => prev + 1)
  const decrement = () => setCount( prev => prev - 1)

  useEffect(() => {
    console.log("S'exécute une seule fois lorsque le composant est monté");
  }, []);

  return (
    <div>
      <h1>Compteur : {count}</h1>
      <div>
        <button onClick={increment}>Augmenter</button>
        <button onClick={decrement}>Diminuer</button>
      </div>
    </div>
  );
}
```

#### Avec un tableau de dépendances contenant des valeurs

Dans la section précédente, vous avez appris que déclarer une fonction useEffect sans tableau de dépendances cause des problèmes de performance. Alors comment pouvons-nous exécuter une fonction qui s'exécute lorsque le compteur change ?

C'est là que le tableau de dépendances aide. Il contient les valeurs dont la fonction dépend. La fonction s'exécute lorsque le composant est rendu et lorsque la valeur des variables dans le tableau change.

Mettons à jour le hook useEffect pour qu'il s'exécute uniquement lorsque le compteur change.

```javascript
import { useEffect, useState } from "react"

export default function App() {
  const [count, setCount] = useState(0);

  const increment = () => setCount( prev => prev + 1)
  const decrement = () => setCount( prev => prev - 1)

  useEffect(() => {
    console.log("useEffect s'exécute lorsque le compteur change");
  }, [count]);

  return (
    <div>
      <h1>Compteur : {count}</h1>
      <div>
        <button onClick={increment}>Augmenter</button>
        <button onClick={decrement}>Diminuer</button>
      </div>
    </div>
  );
}
```

### Le hook useReducer

Le hook useReducer est couramment utilisé dans les composants qui ont un grand nombre d'états et plusieurs gestionnaires d'événements. Il vous permet de gérer des états complexes dans votre application.

Vous devriez utiliser le hook useState lorsqu'il y a quelques états dans vos composants. Utilisez le hook useReducer lorsque vous avez beaucoup d'états à gérer.

Le hook useReducer est divisé en quatre parties : l'état, la fonction de réduction, l'action et la fonction de dispatch.

L'état est un objet contenant tous les états déclarés dans l'application.

La fonction de réduction manipule directement l'état et retourne une copie du résultat, et la fonction de dispatch déclenche la fonction de réduction lorsqu'un événement se produit.

L'action est un objet contenant une propriété de type et une propriété de payload.

La propriété de type spécifie l'action exacte à exécuter par la fonction de réduction, et le payload peut accepter des données de l'utilisateur ou d'autres parties de l'application.

Voyons comment cela fonctionne en recréant le composant Counter en utilisant le hook useReducer :

```javascript
import { useReducer } from "react";
```

Le hook useReducer accepte deux arguments : la fonction de réduction et l'objet d'état. Il retourne les états et la fonction de dispatch.

```javascript
const [state, dispatch] = useReducer(reducerFunction, {states});
```

Dans le composant Counter, le hook useReducer accepte la fonction de réduction et l'état initial du compteur.

```javascript
import {useReducer} from "react"
//👇🏻 déclare le hook useReducer
const [state, dispatch] = useReducer(reducer, { counter: 0 }));
```

Après avoir déclaré le hook useReducer, vous devez créer la fonction de réduction qui gère la manipulation de l'état.

```javascript
//👇🏻 fonction de réduction
const reducer = (state, action) => {
  switch (action.type) {
    case "increase":
      return { counter: state.counter + 1 };
    case "decrease":
      return { counter: state.counter - 1 };
    default:
      return state;
  }
};
```

La fonction de réduction accepte un état et un paramètre d'action. L'objet d'action détermine l'action à effectuer par la fonction de réduction.

Enfin, nous avons la fonction de dispatch qui indique le type d'action et passe sa valeur dans la fonction de réduction pour lui permettre d'effectuer la tâche requise.

```javascript
const increaseCounter = () => {
  dispatch({ type: "increase" });
};

const decreaseCounter = () => {
  dispatch({ type: "decrease" });
};
```

Vous pouvez également passer des données dans la fonction de réduction via le dispatch. Par exemple, vous pouvez augmenter le compteur de 2 en passant les données en tant que payload via la fonction de dispatch.

```javascript
const increaseBy2 = () => {
  dispatch({type: "increaseBy2", payload: {number: 2}})
}
```

Ensuite, créez son action dans la fonction de réduction comme montré ci-dessous :

```javascript
const reducer = (state, action) => {
  switch (action.type) {
    case "increase":
      return { counter: state.counter + 1 };
    case "decrease":
      return { counter: state.counter - 1 };
    case "increaseBy2":
      return { counter: state.counter + action.payload.number };
    default:
      return state;
  }
};
```

Le hook useReducer est beaucoup plus utile dans les composants contenant de nombreux états et diverses modifications d'état, car il vous permet d'écrire le code de manière plus propre.

## Flux de données dans React

Les données circulent de haut en bas dans React, ce qui signifie que vous ne pouvez passer des données que d'un parent à un composant enfant. C'est là que les props sont utiles. Mais parfois, vous devrez peut-être passer des données d'un composant enfant à un composant parent. Comment y parvenir ?

Vous pouvez y parvenir en remontant l'état. Cela implique de déplacer l'état du composant enfant vers le composant parent où l'état est nécessaire. Gardez à l'esprit, cependant, que cette solution peut ne pas être efficace car elle peut entraîner un perçage de props.

### Qu'est-ce que le perçage de props ?

Le **perçage de props** se produit lorsque les composants parent et enfant ne sont pas directement liés, et vous devez passer les données via plusieurs composants avant qu'elles n'atteignent le composant enfant qui a besoin des données.

Prenons un exemple : supposons que nous avons un composant App qui rend diverses parties de l'application. Ensuite, un composant Products affiche la liste des produits disponibles, et nous devons montrer le nombre total de produits dans le composant Nav en haut de l'écran.

Pour résoudre cela, vous devrez peut-être déplacer les produits dans le composant App et les passer en tant que props dans tous les composants enfants jusqu'à ce qu'ils atteignent les composants Nav et Product. Ce processus est appelé perçage de props. Les données des produits devront passer par des composants qui n'en ont pas besoin.

![Image](https://lh7-us.googleusercontent.com/kdujx9yA0oVGx6DiXxszXCu6FzSOdWxJfxhmPWjQl4DrHKySGQzKh497-rS1w9AnaR8Apyc339xz4ekZGHI-ot3s4_EckbSI1bimkmdJ47zbWgV7R2CNIs0zkj4hc88_ZHftQ_riO4Ae4GtVWTvw5b4)
_Diagramme illustrant le fonctionnement du perçage de props_

Des bibliothèques de gestion d'état comme Redux Toolkit, React Context API et Zustand peuvent aider à résoudre ce problème. Elles vous permettent de créer un magasin dans votre application qui permet à tous les composants d'accéder au magasin indépendamment sans interagir avec un composant parent.

Tout changement apporté à un état dans le magasin se reflète dans tous les composants requis. N'hésitez pas à faire des recherches et à en apprendre davantage sur ce sujet.

![Image](https://lh7-us.googleusercontent.com/jT2wKxV-0aNiqh7KPc8kWkcrvFQAVF_FQr1jt07BU_ZKquHvHA-95rNB9xmQ135x40GkkfkXqbkwa40-GVI0q3H8KtayuTNqXRcnKfaNeZRMsxFI0i9S30-8tBs0uGkOqvzigDzWb0cKoXCzokTM2Y8)
_Diagramme montrant comment l'utilisation d'une bibliothèque de gestion d'état peut aider_

## Conclusion

C'est tout pour ce tutoriel. J'espère que vous avez trouvé la discussion éclairante et que vous êtes maintenant mieux équipé pour prendre des décisions éclairées dans votre parcours React.

Si vous êtes impatient d'approfondir React et d'élargir vos compétences, j'ai une mine de ressources sur mon blog. Des tutoriels pour débutants aux conseils et astuces avancés, il y en a pour tous ceux qui cherchent à maîtriser cette bibliothèque puissante.

Ne manquez pas mes derniers tutoriels React :

* **Comprendre les Hooks React : Un Guide pour Débutants** - [Lire Ici](https://theankurtyagi.com/react-hooks/)
* **Gestion d'État dans React : Redux vs Context API** - [Lire Ici](https://theankurtyagi.com/react-state-management-a-complete-in-depth-look-at-hooks-context-api-and-redux/)
* **Comment Utiliser et Valider les Formulaires dans React** - [Lire Ici](https://theankurtyagi.com/how-to-validate-forms-in-react/)

Si vous voulez apprendre React selon les normes de l'industrie, voici où j'ai partagé mon expérience : [Meilleures Pratiques pour Garder un Projet React Propre et Efficace.](https://dev.to/tyaga001/7-best-practices-for-keeping-a-react-project-clean-and-efficient-1ee3)

Vous pouvez me contacter si vous avez des questions ou des corrections. Je les attends.

Et si vous avez trouvé ce tutoriel utile, veuillez le partager avec vos amis et collègues qui pourraient en bénéficier également. Votre soutien me permet de continuer à produire du contenu utile pour la communauté tech.

Il est maintenant temps de passer à l'étape suivante en vous abonnant à ma [**newsletter**](https://theankurtyagi.substack.com/) et en me suivant sur [**Twitter**](https://twitter.com/theankurtyagi).

![Image](https://www.freecodecamp.org/news/content/images/2023/12/image-168.png)
_Une newsletter sur les conseils de carrière, d'affaires, d'écriture et de vie pour les ingénieurs_