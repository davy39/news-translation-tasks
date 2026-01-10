---
title: Comment commencer avec React — Un guide moderne basé sur des projets pour débutants
  (incluant les Hooks)
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2020-05-16T13:18:32.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-react-a-modern-project-based-guide-for-beginners-including-hooks-2
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/getting-started-with-react.png
tags:
- name: React
  slug: react
- name: react hooks
  slug: react-hooks
seo_title: Comment commencer avec React — Un guide moderne basé sur des projets pour
  débutants (incluant les Hooks)
seo_desc: "So you want to start learning React, eh? Then you've come to the right\
  \ place. This guide will walk you through everything you need to know when getting\
  \ started with React. \nWe'll get set up, explain the \"hows and whys\" behind the\
  \ basic concepts, and ..."
---

Vous voulez commencer à apprendre React, hein ? Alors vous êtes au bon endroit. Ce guide vous expliquera tout ce que vous devez savoir pour commencer avec React.

Nous allons nous installer, expliquer les "comment et pourquoi" derrière les concepts de base, et construire un petit projet qui récupère des données d'une API afin que nous puissions voir tout cela en action.

Ce sera un long guide, alors sautez/relisez les sections dont vous avez besoin en utilisant les liens "Aller à la section" ci-dessous. Cela étant dit, prenez une boisson, attachez votre ceinture et commençons.

#### Vous préférez les tutoriels vidéo ?

Vous pouvez consulter le [tutoriel YouTube pour cet article ici.](https://youtu.be/bZXjHauDNcg)


## Aller à la section

* [Prérequis](#heading-prerequisites)
  * [JavaScript de base](#heading-javascript-de-base)
  * [HTML de base](#heading-html-de-base)
* [Environnement de développement](#heading-environnement-de-developpement)
  * [Node.js](#heading-nodejs)
  * [VS Code](#heading-visual-studio-code)
* [Création d'une application React](#heading-creation-dune-application-react)
* [Exploration de Create React App](#heading-exploration-de-create-react-app)
  * [Modules Node](#heading-modules-node)
  * [Dossier Public](#heading-dossier-public)
  * [Index.html](#heading-indexhtml)
* [Notre premier composant](#heading-notre-premier-composant)
* [JSX](#heading-jsx)
  * [Rendre les choses dynamiques](#heading-rendre-les-choses-dynamiques)
  * [Gestion des événements](#heading-gestion-des-evenements)
  * [Appel de fonctions](#heading-appel-de-fonctions)
* [Comment un composant est rendu](#heading-comment-un-composant-est-rendu)
* [Construisons une liste de contacts !](#heading-construisons-une-liste-de-contacts)
  * [Obtenir les styles](#heading-obtenir-les-styles)
  * [Création de la carte de contact](#heading-creation-de-la-carte-de-contact)
  * [Rendre notre carte de contact réutilisable](#heading-rendre-notre-carte-de-contact-reutilisable)
  * [Parlons de l'état](#heading-parlons-de-letat-le-hook-usestate)
  * [Mise à jour de l'état](#heading-mise-a-jour-de-letat)
  * [Introduction aux Props](#heading-introduction-aux-props)
  * [Utilisation des Props dans un composant](#heading-utilisation-des-props-dans-un-composant)
  * [Rendu des composants à partir d'une liste](#heading-rendu-des-composants-a-partir-dune-liste)
  * [Récupération de données depuis une API](#heading-recuperation-de-donnees-depuis-une-api)
  * [Introduction à useEffect](#heading-introduction-a-useeffect)
* [Conclusion](#heading-conclusion)


## Prérequis

Vous n'avez pas besoin de connaître React avant de lire ce guide. Mais il y a quelques choses que vous devrez connaître si vous voulez tirer le meilleur parti de ce guide React :

### JavaScript de base

React est une bibliothèque JavaScript, donc il est logique de connaître JavaScript avant d'apprendre React, non ? Ne vous inquiétez pas, vous n'aurez pas besoin de connaître JavaScript sur le bout des doigts — vous n'avez besoin de connaître que les bases :

- Variables, fonctions, types de données
- Tableaux et objets
- Syntaxe ES6 (utilisation de let & const, fonctions fléchées, affectation par décomposition, classes, importation/exportation, etc.)
- Comment JavaScript est utilisé pour manipuler le DOM

### HTML de base

Dans React, nous utilisons ce qu'on appelle **JSX** pour créer le HTML de nos pages web. Nous expliquerons JSX en profondeur plus tard, mais pour l'instant, assurez-vous d'avoir une bonne base en HTML :

- Comment structurer le HTML (comment imbriquer les éléments, etc.)
- Attributs HTML (comme "id", "class", "onclick", etc.)


> [Besoin d'une révision de JavaScript ? Abonnez-vous pour obtenir mon dernier livre "JavaScript prêt pour React" qui vous aidera à vous mettre à niveau sur le JavaScript dont vous avez besoin avant de commencer avec React !](https://subscribe.jschris.com)


## Environnement de développement

La première chose que nous allons faire est de configurer un environnement de développement. Si vous avez déjà configuré **Node.js** et installé **Visual Studio Code** (ou votre IDE préféré), vous pouvez passer à la section suivante.

### Node.js

[Allez ici et téléchargez](https://nodejs.org/en/download/) le bon package pour votre système d'exploitation (Mac/windows etc.)

Lorsque l'installation est terminée, ouvrez un terminal et tapez cette commande :

```js
node -v
```

Cela devrait afficher la version de Node que vous venez d'installer :

![](https://jschris.com/static/75f85dfa0c07e6b38092fb8eb832a189/b5cea/node.png)

Cela signifie que la commande `node` fonctionne et que Node est installé avec succès — hourra ! Si vous voyez des erreurs, essayez de réinstaller Node à partir du package que vous avez téléchargé et réessayez la commande.

### Visual Studio Code

Visual Studio Code est un IDE open-source populaire qui fonctionne bien pour le développement frontend. Il y en a beaucoup d'autres que vous pouvez essayer — voyez lequel est votre préféré et téléchargez-le si vous préférez. Pour l'instant, nous allons utiliser VS Code.

[Cliquez ici et téléchargez](https://code.visualstudio.com/download) la version pour votre plateforme :

Suivez les étapes d'installation, et vous devriez être prêt à partir. Allez-y et lancez Visual Studio Code.

Cela suffit pour la configuration de l'environnement pour l'instant. Il y a d'autres choses sympas que vous pouvez installer (extensions VS Code, etc.), mais nous n'en avons pas besoin pour l'instant — nous sommes ici pour apprendre React !

## Création d'une application React

L'étape suivante est de créer un projet React. Heureusement pour nous, les gens formidables de Facebook ont rendu cela très simple. Tout ce que nous avons à faire est d'exécuter une commande dans notre terminal :

```jsx
npx create-react-app my-app
```

Cela crée un projet pour nous appelé "my-app" et configure tout automatiquement. Plutôt cool.

Allez-y et ouvrez un terminal dans le répertoire où vous voulez créer votre application, par exemple un dossier "projects", et exécutez la commande. Laissez le terminal faire son travail, et après un moment, cela sera terminé et vous montrera quelques commandes :

![](https://jschris.com/static/9d651a0597f10abac0a8687011b437f1/78363/cra-install.png)

Remarquez que la sortie de **create-react-app** nous a dit ce que nous devons faire pour démarrer l'application. Allez-y et exécutez les commandes dans votre terminal :

```
cd my-app
yarn start
```

Cela démarrera un serveur de développement et ouvrira un navigateur web pour vous :

![](https://jschris.com/static/a1a4aeb3c265e6753ce67bb5e9c66fe0/cb922/cra-start.png)

Vous venez de configurer votre première application React ! Si vous voulez en savoir plus sur ce qui se passe, (consultez le GitHub "create-react-app" :)[https://github.com/facebook/create-react-app]

## Exploration de Create React App

Ouvrez Visual Studio Code (ou l'IDE que vous avez installé) et sélectionnez **Fichier > Ouvrir...** et sélectionnez le dossier **my-app** qui vient d'être créé pour nous en utilisant *create-react-app*. Cela ouvrira notre nouvelle application React dans l'IDE, afin que nous puissions écrire du code !

Vous devriez voir la structure du projet à droite :

![](https://jschris.com/static/64e7647ba04867a1c923bd3d1bac51d9/fdaf8/project-tree.png)


Regardez toutes ces choses ! Ne vous inquiétez pas trop de la plupart d'entre elles, c'est surtout du code et de la configuration de base que nous ne toucherons pas trop dans ce tutoriel — ouf ! Cependant, comme vous êtes un développeur curieux, examinons l'**arbre du projet** et voyons ce que nous avons :

### Modules Node

C'est là que nos packages vont, que nous installons via NPM (Node Package Manager). Si vous n'êtes pas familier avec NPM, c'est un endroit glorieux où nous pouvons partager du code (généralement open source) que d'autres développeurs peuvent utiliser au lieu d'écrire le leur.

Au lieu d'utiliser des **balises de script** comme nous le faisons dans le HTML traditionnel, nous installons ces modules dans le cadre de l'application. Ensuite, nous utilisons une **déclaration d'importation** pour accéder au code de ce module. Nous verrons cela en action plus tard.

### Dossier Public

C'est là que notre code regroupé va. Lorsque nous sommes prêts à déployer notre application, nous exécutons un **script de build** et les fichiers finaux vont ici. Cela sera typiquement notre HTML, JavaScript et CSS. C'est le dossier que nous mettons sur un serveur web quelque part, afin que nous puissions laisser les utilisateurs voir notre application via une URL.

### Index.html

Le **index.html** est le point d'entrée, ou la première chose que le navigateur web charge lorsqu'un utilisateur navigue vers l'URL hébergeant notre application.

Si nous regardons le fichier, c'est juste un fichier HTML normal avec des éléments HTML normaux que vous connaissez probablement. Si nous regardons le corps — il est vide. React convertira dynamiquement notre code React en HTML et le chargera ici, dans la div "root".

Cela étant dit, examinons les parties intéressantes — le code.

## Notre premier composant

Ouvrez **App.js** depuis l'arbre du projet. C'est le composant principal de notre application. C'est le premier composant à être rendu. C'est le "grand fromage" des composants.

La première chose que nous allons faire dans notre grand composant fromage est de tout supprimer et de construire notre propre composant à partir de zéro, pour mieux comprendre ce qui se passe.

Maintenant que nous avons une belle ardoise vierge avec laquelle jouer, nous allons commencer par importer **react**. Cela apporte la bibliothèque React dans le _scope_ et nous donne accès à toutes les fonctionnalités :

```jsx
import React from "react";
```

Ensuite, nous allons déclarer une fonction. Nous utiliserons ici les fonctions fléchées ES6. C'est plus ou moins ce qu'est un "composant" — une fonction avec une logique et un balisage. Nous allons également exporter cette fonction afin de pouvoir l'utiliser ailleurs :

```JSX
const App = () => {

}

export default App;

```

Dans notre fonction, nous voulons écrire `return()`. C'est ce qui est _retourné_ par ce composant et contient notre balisage qui est converti et rendu en HTML.

Enfin, ajoutons une `<div>` avec une balise de titre `<h1>`. Notre composant final ressemble à ceci :

```jsx
import React from "react";

const App = () => {
  return (
    <div>
       <h1>Bonjour le monde React</h1>
       <h2>
             C'est notre première application React - n'est-ce pas merveilleux ?!
       </h2>
    </div>
  );
}

export default App;
```


Maintenant, vous vous dites probablement : "Woah ! Du HTML dans une fonction ? Qu'est-ce que ce délire ?" Même si cela ressemble à du HTML, c'est en fait ce qu'on appelle **JSX (JavaScript XML)**. Cela nous permet essentiellement de mélanger JavaScript et HTML ensemble.

Cela peut sembler un peu étrange. Nous avons initialement appris le développement frontend en séparant notre HTML et JavaScript (et même CSS). Pourtant, JavaScript et la façon dont nous concevons les applications ont évolué, et garder tout ensemble dans le même "composant" facilite la maintenance et la réutilisation de notre code.

Voyons cela en action. Ouvrez votre terminal et exécutez

```
npm start
```

Cela devrait ouvrir le navigateur et vous devriez voir l'application en cours d'exécution.


Félicitations ! Vous venez de créer votre premier composant !

## JSX

Vous avez probablement des points d'interrogation qui flottent au-dessus de votre tête en pensant à cette chose JSX. Approfondissons cela.

```jsx
  return (
    <div>
      <h1>Bonjour le monde React</h1>
      <h2>
          C'est notre première application React - n'est-ce pas merveilleux ?!
      </h2>
    </div>
  );
```


Cela ressemble à du HTML, mais ce n'en est pas. C'est **JSX** ! Même si cela ressemble à du HTML normal, ce qui se passe en coulisses est que React **crée l'arbre d'éléments**, en utilisant cette syntaxe :


```jsx
React.createElement(component, props, ...children)
```

- component : L'**élément HTML** que vous souhaitez créer, par exemple `h1`, `div`, etc.
- props : tous les `props` que vous souhaitez passer à ce composant (nous parlerons des props plus tard)
- children : Un **tableau d'éléments HTML** qui sont imbriqués dans cet élément

Ainsi, le même composant que nous venons de créer peut être écrit comme suit :

```jsx
const App = () => {
  return (
    React.createElement(
      "div",
      null,
      React.createElement("h1", null, "Bonjour le monde React"),
      React.createElement(
        "h2",
        null,
        "C'est notre première application React - n'est-ce pas merveilleux ?!"
      )
    )
  );
}
```


Ce qui semble un peu désagréable (c'était encore plus désagréable d'essayer de le taper). Si vous le tracez soigneusement, vous pouvez voir que nous créons un élément `div`, qui n'a pas de props (indiqué en passant `null` comme deuxième argument). Enfin, nous créons 2 autres éléments en utilisant la syntaxe `createElement` — nos éléments `H1` et `H2`.

Si vous avez joué avec JavaScript pendant un certain temps, vous avez peut-être remarqué que cela ressemble à `document.createElement`. Et c'est le cas ! C'est après tout une bibliothèque JavaScript !

C'est l'avantage de JSX dans React — il nous permet d'écrire une syntaxe de type HTML, sans le désordre de `React.createElement()`.

Dans le monde réel, les développeurs React utilisent presque exclusivement JSX pour écrire leur code. Non, cette section n'était pas une perte de temps — il est toujours bon de comprendre ce qui se passe sous le capot. La connaissance, c'est le pouvoir (et moins de questions dans ma boîte de réception) !


### Rendre les choses dynamiques

Nous avons donc vu JSX et surmonté notre peur (espérons-le). Mais quel est l'intérêt ? Pourquoi utiliser cette chose JSX, alors que nous pourrions simplement utiliser HTML ? Ils se ressemblent ? N'est-ce pas ?

Bonne question mon ami ! Eh bien, si nous nous souvenons de ce que signifie JSX — JavaScript XML. Cela signifie que nous pouvons utiliser JavaScript pour rendre les choses dynamiques. Notre exemple précédent ressemble à ceci :


```jsx
const App = () => {
  return (
    <div>
      <h1>Bonjour le monde React</h1>
      <h2>C'est notre première application React - n'est-ce pas merveilleux ?!</h2>
    </div>
  );
}
```


Maintenant, disons que nous voulons rendre notre texte plus dynamique. Tout d'abord, ajoutons une variable pour contenir notre message :

`cont message = "C'est ma première variable rendue dans JSX !"`

Maintenant, pour ajouter JavaScript à cela, nous utilisons **des accolades** :

```jsx
const App = () => {
  const message = "C'est ma première variable rendue dans JSX !";

  return (
    <div>
      <h1>Bonjour le monde React</h1>
      <h2>{message}</h2>
    </div>
  );
}
```

Si vous exécutez cela dans le navigateur, vous remarquerez que le texte de notre variable de message apparaît. Allez-y et changez le texte de la variable de message en autre chose et regardez la magie se produire.

Nous utilisons **des accolades** pour dire au compilateur "**exécutez ce code en tant que JavaScript**". Si nous n'avions pas d'accolades, la variable **message** ne serait pas exécutée en tant que JavaScript et au lieu de cela, le texte "message" apparaîtrait à l'écran. Essayez cela et voyez !


### Gestion des événements

La même approche peut être prise avec la gestion des événements. Lorsque vous utilisez JSX, React nous donne accès aux **écouteurs d'événements** que vous connaissez peut-être déjà : **onClick**, **onPress**, **onSubmit**, etc.

Disons que nous voulons afficher une alerte lorsque le message est cliqué. Tout d'abord, nous ajoutons la propriété **onClick** à notre balise **h2**.

La propriété **onClick** accepte une fonction (en d'autres termes, nous passons une fonction comme argument. Cette fonction appellera l'alerte comme suit :

```jsx
const App = () => {
  const message = "C'est ma première variable rendue dans JSX !";

  return (
    <div>
      <h1>Bonjour le monde React</h1>
      <h2 onClick={()=> alert("vous avez cliqué sur le message !")}>{message}</h2>
    </div>
  );
}
```

Remarquez comment nous utilisons une fonction **fléchée** ici pour créer une fonction concise en ligne. Si vous n'êtes pas familier avec cette syntaxe, assurez-vous de [consulter mon livre où je couvre cela et plus ici](https://subscribe.jschris.com).

Encore une fois, remarquez comment nous avons mis ce code dans **des accolades**, pour nous assurer que la fonction est exécutée en tant que JavaScript.

### Appel de fonctions

Nous avons donc vu les fonctions en ligne dans le dernier exemple. Puisque JSX est JavaScript, nous pouvons créer et référencer des fonctions **en dehors du bloc return**. Notre dernier exemple pourrait ressembler à ceci :

```jsx
const App = () => {
  const message = "C'est ma première variable rendue dans JSX !";

  const handleClick = () =>{
	alert("vous avez cliqué sur le message !");
  }

  return (
    <div>
      <h1>Bonjour le monde React</h1>
      <h2 onClick={handleClick}>{message}</h2>
    </div>
  );
}
```

Remarquez comment nous avons créé une fonction appelée **handleClick** qui alerte le message. Au lieu d'utiliser une fonction en ligne, nous référençons cette fonction dans notre propriété **onClick**. Essayez cela et voyez ce qui se passe.

Ce ne sont que quelques exemples de la manière dont nous pouvons utiliser JavaScript pour rendre les choses dynamiques, et cela montre, je l'espère, la puissance de JSX. Nous approfondirons nos compréhensions plus tard en construisant un exemple, alors ne vous inquiétez pas si certaines choses ne sont pas encore claires !

## Comment un composant est rendu

J'espère avoir clarifié certaines des questions que vous pourriez avoir sur JSX. La prochaine chose à laquelle vous pourriez penser est — comment un composant est-il rendu ? Où ? Quand ?

Commençons par le début. Si vous regardez notre structure de fichiers, nous avons un fichier **index.js**. C'est le premier fichier à s'exécuter (nous appelons souvent cela un "Point d'entrée"). C'est généralement par convention — vous pouvez changer le point d'entrée si vous le souhaitez, mais pour l'instant, nous allons le laisser tel quel.

Si nous creusons dans le fichier, vous remarquerez que nous avons cette ligne :

```jsx
ReactDOM.render(<App />, document.getElementById("root"));
```

Remarquez que nous avons `document.getElementById("root")` — enfin du JavaScript qui a l'air normal ! Cela obtient l'élément **root** du DOM en utilisant le bon vieux JavaScript, et rend notre composant App à l'intérieur. Notre composant App est importé comme suit :

```jsx
import App from "./App"
```

Souvenez-vous que nous avons _exporté_ notre composant d'application dans App.js. Cela permet à d'autres fichiers/composants d'importer et d'utiliser notre composant App.

Alors, d'où vient l'élément **root** ? Eh bien, souvenez-vous de notre fichier *index.html* dans le dossier public ? Ce fichier index.html est le premier fichier HTML à être chargé lorsque le site web se charge.

À l'intérieur, nous avons une `div` avec un ID de `root`, qui est vide. C'est là que React charge nos composants. Regardons cela dans les outils de développement.

Ouvrez Chrome (ou le navigateur que vous utilisez) et inspectez les outils de développement. Vous verrez quelque part dans l'arbre une **div avec id="root"**, ainsi que le **HTML rendu à partir de notre composant App**. Plutôt cool !

![](https://jschris.com/static/48936a3669e8feaa26c72f9908400f73/fbdcb/id-root-dev-tools.png)

## Résumé rapide

Avant de continuer, résumons rapidement ce que nous avons appris jusqu'à présent :

- Nous avons un fichier *index.html*, qui est le squelette de notre application web
- Lorsque l'application démarre, *index.html* se charge et importe notre composant App
- Le JSX dans le composant App est converti en HTML, qui est ensuite rendu dans le **fichier index.html au niveau de la div root**

## Construisons une liste de contacts !

Maintenant que nous avons les pieds mouillés avec React et que nous avons une meilleure compréhension de la façon dont les choses s'emboîtent, construisons une application d'exemple en utilisant ce que nous avons appris jusqu'à présent. Nous apprendrons également quelques fonctionnalités courantes de React qui vous aideront bien sur la route pour commencer avec React. C'est parti !

Notre liste de contacts affichera un certain nombre de contacts, y compris leur nom, email, âge et avatar (ou image de profil).
Nous allons construire cela progressivement, en récupérant finalement des données d'une API. Quelle excitation !

![](https://jschris.com/static/093da2b0c6947b52d83b42183d172718/6569d/contacts-list-intro.png)

## Obtenir les styles

Puisque ceci est un tutoriel React, nous allons nous concentrer sur le fonctionnement interne de React et ne pas nous soucier de créer de beaux styles. Dans votre dossier source, créez un nouveau fichier `styles.css` et collez le code suivant :

```css
.contact-card {
  display: flex;
  padding: 10px;
  color: #ffffff;
  background-color: rgb(42, 84, 104);
  font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif;
  box-shadow: 10px 10px 25px -16px rgba(0, 0, 0, 0.75);
  border-radius: 10px;
  max-width: 500px;
  max-height: 125px;
  margin-bottom: 10px;
}

.contact-card p {
  margin-left: 10px;
  margin-top: 0;
}

button {
  margin-left: 10px;
  margin-bottom: 10px;
}
```

Ensuite, allez dans **App.js** et importez la feuille de style comme suit :

```jsx
import "./styles.css";
```

## Création de la carte de contact

Tandis que nous sommes encore dans **App.js**, ajoutons le JSX de base pour obtenir notre mise en page pour la carte de contact. Supprimez tout de l'instruction **return** et ajoutez ce qui suit :

```jsx
<div className="contact-card">
	<img src="https://via.placeholder.com/150" alt="profile" />
	<div className="user-details">
		<p>Nom : Jenny Han</p>
		<p>Email : Jenny.Han@notreal.com</p>
		<p>Âge : 25</p>
	</div>
</div>
```

Tout ce que nous faisons ici est de créer une **div** pour "envelopper" les détails de la carte de contact, d'ajouter une image (l'image utilisera un espace réservé pris sur le web pour l'instant), et d'ajouter quelques balises **p** pour contenir les détails dont nous avons besoin dans la carte de contact. Enfin, nous ajoutons quelques **classes CSS** prises de `styles.css` ;

> NOTE : pour référencer les classes CSS, nous devons utiliser le mot-clé **className**. Cela est dû au fait que nous écrivons du JSX, et "class" est un mot réservé en JavaScript.

Voici ce que nous avons jusqu'à présent dans notre fichier **App.js** :

```jsx
import React from "react";
import "./styles.css";

const App = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Nom : Jenny Han</p>
        <p>Email : Jenny.Han@notreal.com</p>
        <p>Âge : 25</p>
      </div>
    </div>
  );
}
```

Si vous exécutez cela dans le navigateur, vous devriez voir quelque chose de similaire à ce qui suit :

![](https://jschris.com/static/adff13952d09891bcb6c1d1c7a694bb9/89048/contac-card-template.png)

## Rendre notre carte de contact réutilisable

D'accord, nous avons donc notre carte de contact ! Cependant, elle n'est pas très réutilisable. Nous savons que nous allons devoir **réutiliser ce code** si nous voulons rendre plus d'une carte, donc il est logique de le diviser **en son propre composant**

> NOTE — Pour faciliter le suivi, je vais mettre tous les composants que nous créons dans **App.js**. Dans le monde réel, il serait préférable de diviser ces différents composants dans leurs propres fichiers, et de les importer/exporter là où c'est approprié.

Juste en dessous de la fonction **App**, créez une nouvelle fonction appelée **ContactCard**, et copiez le JSX de **App** vers **ContactCard** comme suit :

```jsx
const ContactCard = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Nom : Jenny Han</p>
        <p>Email : Jenny.Han@notreal.com</p>
        <p>Âge : 25</p>
      </div>
    </div>
  );
};
```

Encore une fois, un composant dans React est juste une **fonction qui retourne du JSX**. Maintenant que nous avons déplacé notre JSX vers **ContactCard**, nous pouvons utiliser ce composant dans notre composant principal **App** :

```jsx
const App = () => {
  return (
    <>
      <ContactCard />
    </>
  );
}
```

Nous utilisons nos propres composants comme n'importe quelle vieille balise HTML/JSX. Nous mettons simplement le **nom de notre composant entre chevrons**. Notre fichier **App.js** devrait ressembler à ceci :

```jsx
// App.js
import React from "react";
import "./styles.css";

const App = () => {
  return (
    <>
      <ContactCard />
    </>
  );
};

const ContactCard = () => {
  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Nom : Jenny Han</p>
        <p>Email : Jenny.Han@notreal.com</p>
        <p>Âge : 25</p>
      </div>
    </div>
  );
};
```

Maintenant, si vous exécutez cela dans le navigateur, les choses auront l'air comme avant — ce que nous voulons. Nous avons maintenant un composant **ContactCard** que nous pouvons utiliser autant de fois que nous le souhaitons :

```jsx
const App = () => {
  return (
    <>
      <ContactCard />
      <ContactCard />
      <ContactCard />
    </>
  );
};
```

Mettez à jour le composant **App** pour inclure deux autres composants **ContactCard**. L'exemple ci-dessus rendra 3 cartes de contact dans le navigateur. Allez vérifier !

> Considérez cela comme un "tampon" sur la page. Chaque composant **ContactCard** que nous ajoutons est un autre "tampon" et rend le même balisage sur la page.

## Parlons de l'état — le hook useState

Si vous avez déjà commencé avec React, vous avez peut-être entendu le terme **state**. L'état est assez important dans React. Alors, qu'est-ce que c'est ?

> L'état est essentiellement un objet qui représente une partie d'une application qui peut changer, à laquelle l'interface utilisateur "réagit". L'état peut être n'importe quoi ; objets, booléens, tableaux, chaînes ou entiers.

Prenons un exemple.

Certaines personnes qui apparaissent dans notre liste de contacts sont timides et ne veulent pas que leur âge soit affiché jusqu'à ce qu'un bouton soit cliqué. Nous pouvons stocker **si l'âge doit être affiché ou non** dans l'état en utilisant le **hook useState dans le composant**. Ce qui ressemble à ceci :

```jsx
const [showAge, setShowAge] = useState(false);
```

"Qu'est-ce qui se passe ici ?" Laissez-moi expliquer.

L'**objet useState** nous donne une variable avec la **valeur actuelle**, et une fonction qui **nous permet de changer cette valeur**. Lorsque nous appelons **useState**, nous pouvons définir une **valeur initiale** (dans ce cas, **false**).

Nous utilisons **l'affectation par décomposition** sur le **hook useState** pour obtenir ceux-ci. Vous n'avez pas à vous soucier de l'affectation par décomposition pour l'instant, rappelez-vous simplement que la première variable nous permet d'accéder à la valeur de l'état, la seconde nous permet de la changer.

Allez-y et ajoutez l'extrait de code ci-dessus au composant **ContactCard** comme suit :

```jsx
const ContactCard = () => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Nom : Jenny Han</p>
        <p>Email : Jenny.Han@notreal.com</p>
        <p>Âge : 25</p>
      </div>
    </div>
  );
};
```

Maintenant que nous avons un objet d'état, comment l'utilisons-nous ? Eh bien, nous pouvons référencer la variable `showAge` comme n'importe quelle autre variable. Dans ce cas, nous voulons _afficher l'âge uniquement si la variable `showAge` est `true`_.

Nous pouvons faire cela en utilisant l'_opérateur ternaire_ :

```jsx
{showAge === true ? <p>Âge : 25</p> : null}
```

Cet exemple se lit comme suit : _si la variable showAge est vraie, rendre l'âge, sinon, ne rien rendre_.

Allez-y et ajoutez cela au composant **ContactCard**, comme suit :

```jsx
const ContactCard = () => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src="https://via.placeholder.com/150" alt="profile" />
      <div className="user-details">
        <p>Nom : Jenny Han</p>
        <p>Email : Jenny.Han@notreal.com</p>
        {showAge === true ? <p>Âge : 25</p> : null}
      </div>
    </div>
  );
};
```

Maintenant, si vous exécutez l'application dans le navigateur, vous verrez que l'**âge** disparaît — c'est parce que notre variable `showAge` a été initialisée avec `false`. Si nous initialisons notre variable `showAge` avec `true` :

```js
const [showAge, setShowAge] = useState(true);
```

L'âge apparaîtra sur la carte de contact. Bien ! Bien que ce ne soit pas génial — nous ne voulons pas changer le code chaque fois que nous voulons afficher l'âge sur la carte de contact !

Avant de voir comment changer dynamiquement notre variable `showAge`, nettoyons un peu le code. Allez-y et remplacez cette ligne :

```js
{showAge === true ? <p>Âge : 25</p> : null}
```

Par :

```js
{showAge && <p>Âge : 25</p> }
```

Cela donne le même résultat, mais de manière plus concise.

> ASTUCE : Raccourcissez le code lorsque cela a du sens, ne vous sentez pas obligé de raccourcir chaque ligne de code que vous écrivez ! La lisibilité doit passer en premier.

## Mise à jour de l'état

D'accord, revenons à la mise à jour de l'état. Si nous nous souvenons, le hook `useState()` nous donne une **fonction pour mettre à jour l'état**. Connectons cela à un bouton, qui, lorsqu'il est cliqué, basculera l'affichage de l'âge sur la carte de contact.

Nous pouvons faire cela avec ce qui suit :

```jsx
<button onClick={() => setShowAge(!showAge)}>
	Basculer l'âge
</button>
```

Ce que cela fait, c'est appeler la **fonction setShowAge** (que nous obtenons du hook useState) pour changer la **valeur de show age à l'opposé de ce qu'elle est actuellement**.

> NOTE : J'utilise ici la syntaxe de la **fonction fléchée** pour passer une fonction à la propriété `onClick`. Si vous n'êtes pas familier avec cela, un rappel rapide que vous pouvez obtenir mon [livre où je discute des parties importantes de JavaScript à connaître avant React ici].

Lorsque l'état est mis à jour, React **re-rend le composant** et puisque la valeur de `showAge` est vraie, l'âge sera affiché.

Si l'utilisateur clique à nouveau sur le bouton, cela définira `showAge` à `false`, React re-rendra le composant, et l'âge sera masqué :

![](https://jschris.com/46201add1931d222dde4782768435378/age-toggle.gif)

Regardez notre basculement élégant en action !

> ASTUCE : Chaque fois que l'état du composant change, React re-rendra le composant avec le nouvel état.

Remarquez comment, même si nous avons 3 composants **ContactCard** rendus, lorsque nous cliquons sur le bouton, l'âge n'est affiché que pour **une** des cartes, et non pour toutes. Cela est dû au fait que **l'état appartient au composant individuel**. En d'autres termes, chaque composant **ContactCard** rendu est une **copie**, et a son propre état/données.


## Introduction aux Props

Nous avons donc maintenant un tout nouveau composant **ContactCard** que nous réutilisons quelques fois. Bien qu'il ne soit pas vraiment réutilisable, puisque le nom, l'email, l'âge et l'avatar sont les mêmes pour chacun de nos composants. Oh là là ! Nous pouvons rendre ces données plus dynamiques avec ce qu'on appelle **props**.

Puisque vous commencez tout juste avec React, vous pouvez penser aux **Props** comme des données qui sont passées à un composant, que le composant peut ensuite utiliser. Par exemple, nous pouvons passer notre **avatar**, **email**, **nom** et **âge** en tant que props à notre composant **ContactCard** comme suit :

```jsx
<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jenny Han"
  email="jenny.han@notreal.com"
  age={25}
/>
```

Comme vous pouvez le voir, nous définissons une prop en lui donnant un nom. Par exemple, *name* et en utilisant l'**égal** pour assigner une valeur à cette prop, par exemple **Jenny Han**. 

Nous pouvons avoir autant de props que nous voulons, et nous pouvons nommer ces props comme nous le voulons, donc elles sont assez flexibles.

Les props peuvent contenir différents types de données, c'est-à-dire des chaînes de caractères, des nombres, des booléens, des objets, des tableaux, etc.

> NOTE : Les props doivent être définies en utilisant du texte entre guillemets (par exemple, name="Jenny Han") ou entre accolades (par exemple, `age={25}`. Si nous omettons les accolades pour autre chose que des chaînes de caractères, les choses commencent à se casser — `age=25`);

Allez-y et remplacez les composants **ContactCard** actuels dans notre composant **App** par ce qui suit :

```jsx
<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jenny Han"
  email="jenny.han@notreal.com"
  age={25}
/>

<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Jason Long"
  email="jason.long@notreal.com"
  age={45}
/>

<ContactCard
  avatar="https://via.placeholder.com/150"
  name="Peter Pan"
  email="peter.pan@neverland.com"
  age={100}
/>
```


Tout ce que nous faisons ici est de passer **les données dont le composant a besoin** à chaque composant en tant que props. Remarquez comment les données sont différentes pour chaque composant.

## Utilisation des Props dans un composant

Nous avons envoyé un tas de props au composant **ContactCard**, alors apprenons au **ContactCard** comment les utiliser.

Jusqu'à présent, notre fonction **ContactCard** n'accepte aucun _paramètre_. React, étant la chose magique qu'il est, met automatiquement toutes nos props dans un bel **objet props**, qui est passé dans le composant :

```jsx
const ContactCard = props => {
	//...autre code
};
```

Remarquez la variable **props**. Il s'agit d'un objet contenant les props que nous avons définies précédemment. Nous pouvons _accéder à nos props définies_ en utilisant la _notation par points_ comme suit :

```jsx
const ContactCard = props => {
	console.log(props.avatar);
	console.log(props.name);
	console.log(props.email);
	console.log(props.age);

	//...autre code
};
```

Enfin, nous voulons remplacer les valeurs codées en dur dans notre JSX par les valeurs que nous recevons des props :

```jsx
return (
  <div className="contact-card">
    <img src={props.avatar} alt="profile" />
    <div className="user-details">
      <p>Nom : {props.name}</p>
      <p>Email : {props.email}</p>
      <button onClick={() => setShowAge(!showAge)}>Basculer l'âge</button>
      {showAge && <p>Âge : {props.age}</p>}
    </div>
  </div>
);
```

Remarquez comment nous avons défini la **source de l'image** en utilisant la valeur que nous avons reçue des props. Nous avons fait de même pour **name**, **email** et **age**. Remarquez également comment nous enveloppons ce code dans **des accolades**, afin qu'il soit exécuté en tant que JavaScript.

Notre fichier **App.js** final ressemble à ceci :

```jsx
// App.js
const App = () => {
  return (
    <>
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Jenny Han"
        email="jenny.han@notreal.com"
        age={25}
      />
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Jason Long"
        email="jason.long@notreal.com"
        age={45}
      />
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name="Peter Pan"
        email="peter.pan@neverland.com"
        age={100}
      />
    </>
  );
};

const ContactCard = props => {
  const [showAge, setShowAge] = useState(false);

  return (
    <div className="contact-card">
      <img src={props.avatar} alt="profile" />
      <div className="user-details">
        <p>Nom : {props.name}</p>
        <p>Email : {props.email}</p>
        <button onClick={() => setShowAge(!showAge)}>
			Basculer l'âge
		</button>
        {showAge && <p>Âge : {props.age}</p>}
      </div>
    </div>
  );
};
```

Si vous exécutez cela dans le navigateur, vous devriez voir quelque chose de similaire à ceci :

![](https://jschris.com/static/a01167e9d19e96ec4689edbe74bfbdcc/d56e1/contact-lists-3-components.png)

Hourra ! Notre composant fonctionne comme avant, mais il est maintenant plus dynamique. Nous pouvons réutiliser le même **ContactCard** en passant différentes données — tout en gardant la mise en page, les styles et les objets d'état identiques.

## Rendu des composants à partir d'une liste

Notre liste de contacts avance bien, nous avons un code bien conçu et réutilisable, donc il est temps de le laisser tranquille, n'est-ce pas ? Faux ! Allons un peu plus loin.

Dans une application réelle, les données arrivent généralement sous la forme d'un tableau de données, par exemple, après un appel d'API. Faisons semblant d'avoir fait un appel d'API pour **récupérer certains utilisateurs d'une base de données** et avoir reçu les données suivantes :

```js
const contacts = [
    { name: "Jenny Han", email: "jenny.han@notreal.com", age: 25 },
    { name: "Jason Long", email: "jason.long@notreal.com", age: 45 },
    { name: "Peter Pan", email: "peter.pan@neverland.com", age: 100 }
];
```

Collez cela dans le composant **App()** en haut de la fonction. Les plus observateurs d'entre vous remarqueront que ces données sont similaires à ce que nous avons déjà. Mais comment transformer ces données en composants **ContactCard** ? Eh bien, souvenez-vous de tous ces jours que vous avez passés à apprendre à parcourir un tableau en utilisant **.map()** ? Aujourd'hui est le jour où nous mettons cela en action !

Pour afficher une liste de composants, nous :

1) Parcourons le tableau en utilisant **.map()**
2) Pour chaque élément du tableau, créons un nouveau **composant ContactCard**
3) Passons les données de chaque objet du tableau au **composant ContactCard** en tant que props

Voyons comment cela fonctionne. Dans notre composant **App()**, remplacez l'instruction **return** par ceci :

```jsx
return (
  <>
    {contacts.map(contact => (
      <ContactCard
        avatar="https://via.placeholder.com/150"
        name={contact.name}
        email={contact.email}
        age={contact.age}
      />
    ))}
  </>
);
```

Comme vous pouvez le voir, nous **parcourons le tableau**. Pour chaque objet du tableau, nous voulons créer un nouveau **composant ContactCard**. Pour les props, nous voulons prendre le **name**, **email** et **age** de l'**objet actuel sur lequel la fonction map est**. En d'autres termes, de la variable **contact**.

> NOTE : J'ai laissé la prop "avatar" telle quelle, car elle est la même pour l'instant — elle changera plus tard dans le tutoriel.

Et c'est tout ! Notre fichier **App.js** ressemble à ceci :

```jsx
//App.js
const App = () => {
  const contacts = [
    { name: "Jenny Han", email: "jenny.han@notreal.com", age: 25 },
    { name: "Jason Long", email: "jason.long@notreal.com", age: 45 },
    { name: "Peter Pan", email: "peter.pan@neverland.com", age: 100 },
    { name: "Amy McDonald", email: "amy@email.com", age: 33 }
  ];

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar="https://via.placeholder.com/150"
          name={contact.name}
          email={contact.email}
          age={contact.age}
        />
      ))}
    </>
  );
};
```

Exécutez cela dans le navigateur et les choses devraient avoir l'air identiques. Nous n'avons pas changé notre **ContactCard**, nous avons simplement changé d'où nous obtenions les données. Le truc cool à propos de cela est que si vous ajoutez une autre ligne au tableau **contacts**, le composant supplémentaire sera rendu automatiquement — vous n'avez rien d'autre à faire ! Essayez cela vous-même et voyez.

## Récupération de données depuis une API

Nous avons maintenant une belle application React. Elle est dynamique et les choses fonctionnent bien. Ce qui est une bonne position puisque nous commençons tout juste avec React ! Mais il y a quelques nettoyages que nous devons faire. Dans une application réelle, **les données seront récupérées depuis une API**.

Pour la prochaine partie du tutoriel, nous allons obtenir de vrais contacts (quand je dis de vrais contacts, je veux dire de faux contacts — vous voyez ce que je veux dire) depuis une vraie API : [https://randomuser.me/](https://randomuser.me/). N'hésitez pas à parcourir le site web et à regarder la réponse que nous allons obtenir — c'est de là que nous obtiendrons nos données pour remplir nos composants.

Tout d'abord, créons une **variable d'état** pour contenir les données que nous obtenons de l'API. Souvenez-vous, l'état est bon pour contenir ce qui peut changer. Notre liste de contacts peut définitivement changer !

Dans **App.js**, supprimez le tableau **contacts** et ajoutez ce qui suit :

```js
const [contacts, setContacts] = useState([]);
```

Ici, nous créons un objet d'état et l'initialisons à un tableau vide. Lorsque nous faisons l'appel à l'API, nous mettrons à jour l'état pour contenir une liste de contacts. Puisque nous avons nommé cet objet d'état **contacts**, notre logique de rendu dans le JSX recherchera ce tableau à la place (par opposition à l'ancien tableau **contacts** que nous venons de supprimer).

Ensuite, récupérons les données de l'API. Nous utiliserons l'API **Fetch** standard. Pour l'instant, nous allons journaliser les données dans la console. Ajoutez ce qui suit en dessous de l'objet d'état que nous venons de créer :

```js
fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
  });
```

Tout ce que nous faisons ici est :

- Faire une requête GET à l'API **randomuser**, en demandant **trois** résultats
- Convertir la réponse en **JSON**
- Journaliser le **JSON** dans la console.

Si vous exécutez cela dans le navigateur, vous remarquerez que les composants **ContactCard** ne sont plus rendus — c'est normal, nous n'avons pas encore enregistré de nouvelles données dans l'état, et notre variable d'état est actuellement vide. Si vous regardez la console (dans les outils de développement de votre navigateur), vous remarquerez que l'objet de réponse est journalisé. Ce qui ressemblera à quelque chose comme ceci :

![](https://jschris.com/static/2327d21e950dd2b2d3a0c7c51fac655d/587b0/response_object.png)

Vous verrez que nous avons un tableau **results**, qui contient 3 objets. Chacun de ces objets contient les détails d'un utilisateur (ou d'un "Contact" dans notre cas). Cela est similaire au tableau **contacts** que nous avons créé manuellement dans la section précédente — juste un tableau rempli d'objets.

Mettons à jour le JSX de nos composants **App** pour sélectionner les données de cet objet. Mettez à jour le JSX comme suit :

```jsx
return (
  <>
    {contacts.map(contact => (
      <ContactCard
        avatar={contact.picture.large}
        name={contact.name.first + " " + contact.name.last}
        email={contact.email}
        age={contact.dob.age}
      />
    ))}
  </>
);
```

Cela fonctionne de manière similaire à ce que nous avions avant :

- Nous parcourons la variable **contacts** (qui, pour le moment, est un tableau vide)
- Lorsque nous enregistrons finalement la réponse dans l'état (l'étape suivante), nous cherchons dans chaque objet du tableau les choses appropriées dont nous avons besoin : dans ce cas, les objets **picture**, **name**, **email** et **dob**.

Ensuite, nous voulons stocker le tableau **results** dans l'état, afin que notre JSX puisse le parcourir (en utilisant la fonction **map()** que nous avons vue précédemment) et rendre de jolies **ContactCards**. Dans notre fonction **fetch**, ajoutez l'appel à **setContacts(data.results)** comme suit :

```jsx
fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
    setContacts(data.results);
  });
```

Notre composant **App** ressemble maintenant à ceci :

```jsx
//App.js
const App = () => {
  const [contacts, setContacts] = useState([]);

fetch("https://randomuser.me/api/?results=3")
  .then(response => response.json())
  .then(data => {
    console.log(data);
    setContacts(data.results);
  });

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar={contact.picture.large}
          name={contact.name.first + " " + contact.name.last}
          email={contact.email}
          age={contact.dob.age}
        />
      ))}
    </>
  );
};
```

Si vous enregistrez cela et l'exécutez dans le navigateur, vous verrez quelque chose comme ceci :

![](https://jschris.com/4bd02a07f80d45810780b5db77db42b3/multiple-calls-to-api.gif)

Vous pourriez penser : "WTF se passe-t-il ? Tout est cassé !"

Ne paniquez pas encore. (Si vous êtes sur une machine plus lente ou si vous commencez à vous sentir un peu paniqué, vous pouvez commenter la ligne **setContacts(data.results)** dans la fonction **fetch** pour l'instant).

Ce qui se passe ici, c'est que nous sommes coincés dans une sorte de boucle :

1) Nous faisons un appel à **fetch** et obtenons des données en retour
2) Nous **enregistrons ensuite ces données dans l'état**
3) Souvenez-vous, React effectue un **re-rendu lorsque l'état change**
4) Lorsque le composant est re-rendu, l'appel à l'API **fetch** se produit à nouveau et définit l'état
5) Puisque l'état a été mis à jour, le composant est re-rendu à nouveau
6) Après que le composant soit re-rendu, fetch est appelé à nouveau...
7) Vous voyez l'idée

Alors, comment arrêtons-nous cela ? Nous devons tout supprimer et recommencer. Non, je plaisante, ne partez pas encore. Nous pouvons corriger cela avec un autre hook React intégré — **useEffect**.

## Introduction à useEffect

Le hook **useEffect** est un hook spécial qui exécute une fonction. Par défaut, le hook useEffect s'exécute à chaque re-rendu. Cependant, nous pouvons le configurer pour qu'il ne s'exécute que **dans certaines conditions**, par exemple, lorsqu'un **composant est monté**, ou **si une variable change**. Le hook useEffect ressemble à ceci :

```js
useEffect(() => {
	// code à exécuter
});
```

Cela s'exécutera à chaque fois. Si nous voulons spécifier "**exécuter une seule fois**", nous passons un **tableau vide** comme deuxième argument comme suit.

```js
useEffect(() => {
	// code à exécuter
},[]); //<-- remarquez le tableau vide
```

Cela s'appelle un **tableau de dépendances**. Lorsque le tableau de dépendances est vide, cela signifie que la fonction useEffect ne s'exécutera que lorsque le composant se charge pour la première fois. Pour les re-rendus supplémentaires, la fonction useEffect est ignorée.

C'est un endroit parfait pour placer notre appel d'API, car nous voulons obtenir les données une seule fois, lorsque le composant se charge. Allez-y et placez une fonction **useEffect()** dans notre composant **App**, et déplacez l'appel à l'API **fetch** dans la fonction useEffect. Notre composant **App** ressemble maintenant à ceci :

```jsx
//App.js
const App = () => {
  const [contacts, setContacts] = useState([]);

  useEffect(() => {
    fetch("https://randomuser.me/api/?results=3")
      .then(response => response.json())
      .then(data => {
        setContacts(data.results);
      });
  }, []);

  return (
    <>
      {contacts.map(contact => (
        <ContactCard
          avatar={contact.picture.large}
          name={contact.name.first + " " + contact.name.last}
          email={contact.email}
          age={contact.dob.age}
        />
      ))}
    </>
  );
};
```

Maintenant, si vous exécutez le code dans votre navigateur, vous devriez voir 3 cartes de contact apparaître ! Rafraîchissez la page pour voir une autre liste aléatoire de contacts :

![](https://jschris.com/static/093da2b0c6947b52d83b42183d172718/6569d/contacts-list-intro.png)

## Conclusion

Félicitations ! Vous venez de terminer votre première application réelle et avez posé les bases pour passer à des sujets plus avancés.

[Assurez-vous de vous abonner ici pour rester à jour avec mon dernier contenu React, des réductions sur les cours et un accès anticipé, ainsi que des trucs gratuits !](https://subscribe.jschris.com)


[N'oubliez pas non plus de consulter mon nouveau blog - www.jschris.com - où je publierai des articles et tutoriels liés à JavaScript/React !](https://www.jschris.com)