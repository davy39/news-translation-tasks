---
title: Le guide React pour débutants – JSX, Hooks et le rendu expliqués
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2025-10-22T21:56:41.189Z'
originalURL: https://freecodecamp.org/news/react-handbook-for-beginners-learn-jsx-hooks-rendering
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1761170169453/445fd0f5-54f9-4be5-bacf-2e6c6acd1f21.png
tags:
- name: React
  slug: reactjs
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
- name: Programming Blogs
  slug: programming-blogs
- name: coding
  slug: coding
seo_title: Le guide React pour débutants – JSX, Hooks et le rendu expliqués
seo_desc: React is one of the most powerful and widely used libraries for building
  user interfaces with JavaScript. From small components to large-scale front-end
  and full-stack applications, React gives you the flexibility to create interactive,
  efficient, an...
---

React est l'une des bibliothèques les plus puissantes et les plus largement utilisées pour construire des interfaces utilisateur avec JavaScript. Des petits composants aux applications front-end et full-stack à grande échelle, React vous offre la flexibilité nécessaire pour créer des fonctionnalités interactives, efficaces et modernes.

Mais apprendre React peut sembler décourageant. Avec autant de nouveaux termes, de modèles et de Frameworks comme Next.js dans l'équation, il est facile de se sentir perdu.

C'est pourquoi ce guide se concentre sur React lui-même, sans distractions inutiles. Une fois que vous aurez maîtrisé le cœur de React, vous aurez la confiance nécessaire pour l'utiliser avec ou sans Framework pour construire tout ce que vous pouvez imaginer.

## Table des matières

1. [Ce que vous devriez déjà savoir](#heading-ce-que-vous-devriez-deja-savoir)
    
2. [Qu'est-ce que React exactement ?](#heading-qu-est-ce-que-react-exactement)
    
    * [Pourquoi le nom « React » ?](#heading-pourquoi-le-nom-react)
        
    * [React est-il un Framework ?](#heading-react-est-il-un-framework)
        
    * [React est-il uniquement destiné au développement web ?](#heading-react-est-il-uniquement-destine-au-developpement-web)
        
    * [Quel est l'objectif principal de React ?](#heading-quel-est-l-objectif-principal-de-react)
        
3. [Comment ajouter un composant React à un site web](#heading-comment-ajouter-un-composant-react-a-un-site-web)
    
    * [Créer un nouveau répertoire de projet](#heading-creer-un-nouveau-repertoire-de-projet)
        
    * [Créer un conteneur DOM](#heading-creer-un-conteneur-dom)
        
    * [Importer React, Babel et votre composant](#heading-importer-react-babel-et-votre-composant)
        
    * [Créer votre composant](#heading-creer-votre-composant)
        
    * [Configurer un serveur local](#heading-configurer-un-serveur-local)
        
4. [Qu'est-ce que JSX ?](#heading-qu-est-ce-que-jsx)
    
    * [React peut-il fonctionner sans JSX ?](#heading-react-peut-il-fonctionner-sans-jsx)
        
    * [Exemple 1 : Créer un élément React avec JSX](#heading-exemple-1-creer-un-element-react-avec-jsx)
        
    * [Exemple 2 : Créer un élément React avec du JavaScript classique](#heading-exemple-2-creer-un-element-react-avec-du-javascript-classique)
        
5. [Qu'est-ce que React.createElement() ?](#heading-qu-est-ce-que-reactcreateelement)
    
6. [Comment utiliser JSX](#heading-comment-utiliser-jsx)
    
    * [Utiliser JSX comme n'importe quelle expression JavaScript](#heading-utiliser-jsx-comme-n-importe-quelle-expression-javascript)
        
    * [Envelopper le JSX multi-ligne dans des parenthèses](#heading-envelopper-le-jsx-multi-ligne-dans-des-parentheses)
        
    * [Envelopper les expressions dans des accolades](#heading-envelopper-les-expressions-dans-des-accolades)
        
    * [Utiliser le camelCase pour nommer les attributs](#heading-utiliser-le-camelcase-pour-nommer-les-attributs)
        
    * [Fermer correctement les balises JSX vides](#heading-fermer-correctement-les-balises-jsx-vides)
        
    * [Un composant React ne peut retourner qu'un seul élément](#heading-un-composant-react-ne-peut-retourner-qu-un-seul-element)
        
7. [C'est l'heure de pratiquer avec JSX 🤸‍♂️🏋️‍♀️🏊‍♀️](#heading-c-est-l-heure-de-pratiquer-avec-jsx)
    
    * [La solution](#heading-la-solution)
        
8. [Qu'est-ce qu'un composant React ?](#heading-qu-est-ce-qu-un-composant-react)
    
    * [Syntaxe d'un composant React](#heading-syntaxe-d-un-composant-react)
        
    * [Exemple d'un composant React](#heading-exemple-d-un-composant-react)
        
    * [Bonnes pratiques pour les composants React](#heading-bonnes-pratiques-pour-les-composants-react)
        
9. [Comment rendre des listes d'éléments à partir d'un tableau](#heading-comment-rendre-des-listes-d-elements-a-partis-d-un-tableau)
    
    * [Chaque élément React dans un tableau a besoin d'une clé unique](#heading-chaque-element-react-dans-un-tableau-a-besoin-d-une-cle-unique)
        
    * [Comment ajouter des clés uniques à chaque élément React dans un tableau](#heading-comment-ajouter-des-cles-uniques-a-chaque-element-react-dans-un-tableau)
        
    * [Choses essentielles à savoir sur l'attribution des clés](#heading-choses-essentielles-a-savoir-sur-l-attribution-des-cles)
        
10. [Comment gérer les événements dans React](#heading-comment-gerer-les-evenements-dans-react)
    
    * [Types de gestionnaires d'événements](#heading-types-de-gestionnaires-d-evenements)
        
    * [Exemple : Gestionnaire d'événement en ligne](#heading-exemple-gestionnaire-d-evenement-en-ligne)
        
    * [Exemple : Gestionnaire d'événement référencé](#heading-exemple-gestionnaire-d-evenement-reference)
        
11. [Qu'est-ce que le State React ?](#heading-qu-est-ce-que-le-state-react)
    
    * [Syntaxe du State React](#heading-syntaxe-du-state-react)
        
    * [Exemple du State React](#heading-exemple-du-state-react)
        
    * [React trigger vs render vs Commit vs paint](#heading-react-trigger-vs-render-vs-commit-vs-paint)
        
    * [Que signifie déclencher (trigger) un rendu dans React ?](#heading-que-signifie-declencher-un-rendu-dans-react)
        
    * [Que signifie rendre des composants React ?](#heading-que-signifie-rendre-des-composants-react)
        
    * [Que signifie Commit une UI React vers le DOM du navigateur ?](#heading-que-signifie-commit-une-ui-react-vers-le-dom-du-navigateur)
        
    * [Que signifie peindre (paint) les nœuds DOM sur l'écran ?](#heading-que-signifie-peindre-les-noeuds-dom-sur-l-ecran)
        
12. [Qu'est-ce que le Hook Ref de React ?](#heading-qu-est-ce-que-le-hook-ref-de-react)
    
    * [Syntaxe du Hook ref de React](#heading-syntaxe-du-hook-ref-de-react)
        
    * [Exemple du Hook ref de React](#heading-exemple-du-hook-ref-de-react)
        
    * [Bonnes pratiques du Hook ref de React](#heading-bonnes-pratiques-du-hook-ref-de-react)
        
13. [Variables vs Refs vs States dans React](#heading-variables-vs-refs-vs-states-dans-react)
    
    * [Comment fonctionnent les variables dans React ?](#heading-comment-fonctionnent-les-variables-dans-react)
        
    * [Comment fonctionnent les refs dans React ?](#heading-comment-fonctionnent-les-refs-dans-react)
        
    * [Comment fonctionnent les states dans React ?](#heading-comment-fonctionnent-les-states-dans-react)
        
    * [Conseils sur l'utilisation des variables, des refs et des states dans React](#heading-conseils-sur-l-utilisation-des-variables-des-refs-et-des-states-dans-react)
        
14. [Qu'est-ce que le Hook useEffect ?](#heading-qu-est-ce-que-le-hook-useeffect)
    
    * [Syntaxe du Hook useEffect](#heading-syntaxe-du-hook-useeffect)
        
    * [Exemple du Hook useEffect](#heading-exemple-du-hook-useeffect)
        
    * [Bonnes pratiques du Hook useEffect](#heading-bonnes-pratiques-du-hook-useeffect)
        
15. [Comment styliser les composants React](#heading-comment-styliser-les-composants-react)
    
    * [Comment utiliser les feuilles de style CSS pour styliser les éléments React](#heading-comment-utiliser-les-feuilles-de-style-css-pour-styliser-les-elements-react)
        
    * [Comment utiliser l'attribut style en ligne pour styliser les éléments React](#heading-comment-utiliser-l-attribut-style-en-ligne-pour-styliser-les-elements-react)
        
    * [Comment utiliser les CSS Modules pour styliser les éléments React](#heading-comment-utiliser-les-css-modules-pour-styliser-les-elements-react)
        
    * [Comment utiliser une bibliothèque CSS-in-JS pour styliser les éléments React](#heading-comment-utiliser-une-bibliotheque-css-in-js-pour-styliser-les-elements-react)
        
16. [Aperçu](#heading-apercu)
    
    * [Approfondir React](#heading-approfondir-react)
        

## Ce que vous devriez déjà savoir

Vous tirerez le meilleur parti de ce guide si vous êtes familier avec :

* Les fondamentaux de JavaScript (variables, fonctions, tableaux, objets)
    
* Le CSS de base pour le stylisme
    
* Les bases du HTML pour la structure
    

Si vous avez déjà écrit un petit fichier JavaScript ou construit un site web simple « Hello World », vous êtes prêt !

Commençons par les bases.

## Qu'est-ce que React exactement ?

React est une bibliothèque JavaScript basée sur des composants pour construire efficacement des interfaces utilisateur (UI).

Peu importe l'ampleur de votre projet, React est parfaitement adapté pour vous aider à développer n'importe quelle application web de manière efficace.

Les développeurs utilisent principalement React pour construire des composants indépendants et réutilisables qui peuvent être combinés avec d'autres interfaces utilisateur isolées pour créer des applications hautement évolutives. Par exemple, l'image ci-dessous illustre les composants individuels de la page du lecteur vidéo de YouTube.

![Une illustration des composants React. La page du lecteur vidéo YouTube est illustrée comme une combinaison de composants indépendants.](https://cdn.hashnode.com/res/hashnode/image/upload/v1760577491945/1b0f8c61-b42e-4e3c-afdc-5804fdfa0d42.webp align="center")

En d'autres termes, React vous aide à construire des UI complexes à partir de petits composants isolés qui peuvent facilement être réutilisés dans plusieurs applications. Chaque composant indépendant indique à React l'élément exact que vous souhaitez afficher à l'écran.

![React expliqué : La bibliothèque JavaScript super flexible pour le développement d'applications frontend et full-stack modernes](https://cdn.hashnode.com/res/hashnode/image/upload/v1760577104799/4592a7d2-e75b-4ae6-b1f4-65cfd8e94033.webp align="center")

L'image ci-dessus illustre React comme une bibliothèque hautement adaptable qui utilise des fonctions JavaScript pour construire des interfaces utilisateur pour les applications mobiles et web. Discutons des points mis en évidence dans l'image.

### Pourquoi le nom « React » ?

Le nom vient de l'idée que React effectue le rendu de votre UI et réagit (reacts) aux événements dans l'interface utilisateur qu'il a affichée à l'écran.

### React est-il un Framework ?

Non, React est une [bibliothèque — pas un Framework](https://codesweetly.com/framework-vs-library/). React sert uniquement de fonctionnalité supplémentaire à votre application. Il n'est pas conçu pour être utilisé comme système de support principal d'une application.

### React est-il uniquement destiné au développement web ?

Non, vous n'utilisez pas React uniquement sur le web. Par exemple, ReactDOM aide à construire des applications web, et React Native aide à construire des applications mobiles.

### React peut-il être utilisé pour des applications full-stack ?

Absolument. React est super flexible. Vous pouvez l'utiliser dans des projets HTML simples, l'intégrer dans du code existant ou construire des applications full-stack complexes. Son adaptabilité le rend approprié pour une grande variété de scénarios de développement.

### Quel est l'objectif principal de React ?

L'objectif principal de React est de vous permettre d'utiliser des fonctions JavaScript pour retourner et gérer l'UI (élément HTML) que vous souhaitez rendre (afficher) à l'écran. Par exemple, considérez ce qui suit :

```javascript
function DonationUserInterface() {
  return <button>☕ Buy me a coffee</button>;
}
```

La fonction JavaScript ci-dessus est un composant React qui retourne l'UI (élément bouton HTML) que nous voulons afficher à l'écran et gérer avec React. En fait, implémentons le composant `DonationUserInterface` sur un site web en direct en utilisant uniquement HTML et JavaScript – sans Framework.

## Comment ajouter un composant React à un site web

Suivez les étapes ci-dessous pour ajouter un composant d'UI de don à un site web HTML en direct.

### Créer un nouveau répertoire de projet

```bash
mkdir codesweetly-donation-ui-001
```

**Note :** Vous pouvez utiliser le nom que vous préférez. Dans ce guide, nous utiliserons `codesweetly-donation-ui-001` pour la démonstration.

Ensuite, naviguez vers votre répertoire de projet en utilisant la ligne de commande.

```bash
cd path/to/codesweetly-donation-ui-001
```

### Créer un conteneur DOM

Pour ajouter un composant React à une page web, vous devez d'abord spécifier la section de la page où vous souhaitez insérer l'UI. Créez donc une page HTML :

```bash
touch index.html
```

Ensuite, ouvrez le nouveau fichier et ajoutez le code suivant :

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>CodeSweetly Donation UI</title>
  </head>
  <body>
    <!-- Un conteneur div (le nœud DOM) créé pour que React le gère -->
    <div id="donation-ui"></div>
  </body>
</html>
```

L'extrait ci-dessus a créé un nœud DOM (élément `<div>`), à l'intérieur duquel nous voulons que React affiche et gère une interface utilisateur de don. En d'autres termes, le `<div>` représente la section du site web que vous voulez que React gère.

Quelques notes :

* L'attribut `id` du `div` est la référence que nous utiliserons plus tard dans un fichier JavaScript pour trouver le conteneur et dire à React d'insérer une UI de don.
    
* Bien que la plupart des développeurs utilisent une balise `<div>` comme conteneur DOM, vous pouvez utiliser d'autres éléments HTML comme la balise `<main>`.
    
* Vous pouvez avoir plusieurs conteneurs DOM n'importe où à l'intérieur de l'élément `<body>`.
    
* Un conteneur DOM est généralement laissé vide, car React écrasera son contenu.
    

### Importer React, Babel et votre composant

Utilisez des balises script pour charger React, Babel et votre composant dans la page HTML de votre projet.

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>CodeSweetly Donation UI</title>
    <!-- Charger la bibliothèque React -->
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <!-- Charger l'API ReactDOM -->
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <!-- Charger le compilateur Babel -->
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="donation-ui"></div>
    <!-- Charger votre composant React -->
    <script type="text/babel" src="DonationUserInterface.js"></script>
  </body>
</html>
```

L'extrait ci-dessus utilise les trois premières balises script pour charger React, ReactDOM et Babel depuis unpkg.com.

En même temps, nous utilisons la quatrième balise script pour importer notre composant de don (que nous créerons dans la section suivante).

Quelques notes :

* Le package `react` est une bibliothèque contenant les fonctionnalités de base de React pour créer des composants React.
    
* L'API ReactDOM fournit les méthodes requises pour utiliser React avec le DOM.
    
* Babel est un compilateur qui transforme le code React en JavaScript pur, car les navigateurs ne comprennent pas la syntaxe React par défaut.
    
* L'attribut `type="text/babel"` indique à Babel d'exécuter et de convertir automatiquement le script `DonationUserInterface.js` du code React en JavaScript pur.
    
* La configuration ci-dessus est recommandée uniquement pour apprendre React. Ne l'utilisez pas pour des projets publics (environnement de production). Vous pouvez apprendre à configurer React pour la production dans mon livre [Code React Sweetly](https://www.amazon.com/dp/B0FRC4R8T3?tag=codesweetly00-20).
    
* Les scripts ne fonctionneront pas si votre connexion internet ou le serveur d'`unpkg.com` est en panne. Donc, si rien ne s'affiche à l'écran, entrez l'URL `src` de chaque script dans votre navigateur pour confirmer si le serveur répond avec succès.
    

### Créer votre composant

Créez un fichier JavaScript `DonationUserInterface.js` dans le même dossier que celui où se trouve votre fichier HTML.

```bash
touch DonationUserInterface.js
```

Ensuite, collez le code suivant à l'intérieur du fichier JavaScript que vous venez de créer :

```javascript
function DonationUserInterface() {
  const [donate, setDonate] = React.useState(false);

  function createUserInterface() {
    if (donate) {
      return (
        <p>
          <a href="https://www.buymeacoffee.com/codesweetly">Support page</a>.
          Thank you so much! 🎉
        </p>
      );
    }
    return <button onClick={() => setDonate(true)}>☕ Buy me a coffee</button>;
  }
  return createUserInterface();
}

const root = ReactDOM.createRoot(document.getElementById("donation-ui"));
root.render(<DonationUserInterface />);
```

L'extrait ci-dessus fait ce qui suit :

1. Définit un composant nommé `DonationUserInterface`.
    
2. Initialise le state du composant (objet intégré) avec la valeur booléenne `false`.
    
3. Programme le composant pour retourner un élément de paragraphe si la variable `donate` du state est `true`. Sinon, il doit retourner un élément bouton.
    
4. Crée une instance d'objet `ReactDOMRoot` pour l'élément HTML `donation-ui` que vous voulez que React gère. Ensuite, il assigne l'instance nouvellement créée à la variable `root`.
    
5. Utilise la méthode `render()` de l'instance d'objet pour afficher le composant `DonationUserInterface` à l'intérieur de la racine `donation-ui`.
    

### Configurer un serveur local

Les fichiers HTML contenant des [ES modules](https://codesweetly.com/javascript-modules-tutorial/) ne fonctionnent que via des URL `http://` et `https://`, pas localement via une URL `file://`.

Comme nous avons précédemment utilisé l'attribut `type="text/babel"` pour convertir le fichier JavaScript `DonationUserInterface.js` en un ES module, nous avons besoin d'un serveur local, comme « Live Server » ou « Servor », pour charger le document HTML via un schéma `http://`. Installons Servor afin de pouvoir l'utiliser pour ce projet.

#### Installer le serveur local Servor

```bash
npm install servor@4.0.2 --save-dev
```

#### Lancer votre application

Après avoir installé Servor, utilisez-le pour démarrer votre application depuis votre terminal :

```bash
npx servor --browse --reload
```

Quelques notes :

* Fermez le serveur en utilisant <kbd>Ctrl</kbd> + <kbd>C</kbd> sur Windows ou <kbd>Cmd</kbd> + <kbd>C</kbd> sur Mac.
    
* `--browse` : Ouvre le navigateur une fois que le serveur démarre.
    
* `--reload` : Recharge le navigateur chaque fois que vous mettez à jour les fichiers du projet.
    
* Vous pouvez également ajouter la commande `servor` au champ `"scripts"` du fichier `package.json` de votre projet :
    

```json
{
  "scripts": {
    "start": "servor --browse --reload"
  },
  "devDependencies": {
    "servor": "^4.0.2"
  }
}
```

Ce faisant, vous pouvez lancer votre application depuis votre terminal comme ceci :

```bash
npm run start
```

Et voilà ! Vous avez ajouté avec succès un composant React à un site web en direct en utilisant une fonction JavaScript pour rendre une UI de don à l'écran ! 🎉

Vous demandez-vous pourquoi nous écrivons du HTML à l'intérieur de JavaScript ? Eh bien, ce code ressemblant à du HTML s'appelle JSX. Apprenons-en plus à son sujet.

## Qu'est-ce que JSX ?

JSX est une extension de syntaxe JavaScript qui vous permet de construire des éléments React avec une syntaxe de type HTML directement dans votre code JavaScript.

**Conseils :**

* JSX est parfois appelé JavaScript XML ou JavaScript Syntax eXtension.
    
* Bien que JSX ressemble beaucoup au HTML, ce n'est pas du HTML. Au lieu de cela, il vous permet d'utiliser une syntaxe de type HTML avec toutes les forces de JavaScript.
    

### React peut-il fonctionner sans JSX ?

Oui. React peut fonctionner indépendamment de JSX. Mais JSX facilite la création d'interfaces utilisateur (UI).

En d'autres termes, tout ce que vous pouvez faire avec JSX, vous pouvez le faire de la même manière avec du JavaScript pur. Par exemple, considérez les deux exemples ci-dessous. Le premier inclut la syntaxe JSX, tandis que le second utilise la syntaxe JavaScript classique.

#### Exemple 1 : Créer un élément React avec JSX

`MyBio.js`

```javascript
function MyBio() {
  return <h1>My name is Oluwatobi.</h1>;
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<MyBio />);
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>MyBio App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/babel" src="MyBio.js"></script>
  </body>
</html>
```

Dans l'extrait React ci-dessus, `<h1>My name is Oluwatobi.</h1>` et `<MyBio />` sont du JSX.

**Conseil :** React prend en charge l'extension de fichier `.jsx` pour les fichiers contenant du code JSX. Donc, si vous préférez différencier vos fichiers JSX du JavaScript, vous pouvez renommer `MyBio.js` en `MyBio.jsx`. Notez simplement que le choix entre l'utilisation de `.js` ou `.jsx` pour les fichiers avec JSX dépend entièrement de vous. (Votre code JSX est simplement un sucre syntaxique pour l'appel JavaScript `React.createElement()`.)

#### Exemple 2 : Créer un élément React avec du JavaScript classique

`MyBio.js`

```javascript
function MyBio() {
  return React.createElement("h1", null, "My name is Oluwatobi.");
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(React.createElement(MyBio));
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>MyBio App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/babel" src="MyBio.js"></script>
  </body>
</html>
```

Tout dans l'extrait React ci-dessus est du code JavaScript pur.

## Qu'est-ce que React.createElement() ?

`React.createElement()` est l'alternative JavaScript au JSX. C'est une méthode pour créer des éléments React en JavaScript classique.

Les navigateurs ne peuvent pas lire la syntaxe JSX. C'est pourquoi nous utilisons généralement des outils comme Babel, TypeScript et Parcel pour compiler le JSX en un appel JavaScript `React.createElement(component, props, ...children)`.

Par exemple, `<button className="support-btn">Buy me a coffee</button>` se transformera en `React.createElement("button", { className: "support-btn" }, "Buy me a coffee ")` au moment de l'exécution.

Sous le capot, la méthode `React.createElement()` crée un objet JavaScript conventionnellement appelé « élément React ».

**Conseil :** Un élément React est un objet JavaScript qui définit l'interface utilisateur (UI) que vous souhaitez rendre à l'écran.

Une version simplifiée d'un élément React ressemble à ceci :

```javascript
const myBioReactElement = {
  type: "h1",
  props: {
    className: null,
    children: "My name is Oluwatobi.",
  },
};
```

`React.createElement()` est idéal pour les projets qui veulent éviter les outils de compilation comme Babel. Tandis que le JSX est un sucre syntaxique qui rend le code React plus facile à lire. Vous êtes donc libre de choisir la syntaxe qui vous convient le mieux (mais la plupart des projets React utilisent JSX pour sa simplicité).

## Comment utiliser JSX

Les conseils suivants vous aideront à démarrer avec JSX afin que vous puissiez l'utiliser dans vos projets React.

### Utiliser JSX comme n'importe quelle expression JavaScript

Vous pouvez utiliser JSX comme n'importe quelle autre expression JavaScript car, au [moment de l'exécution](https://codesweetly.com/web-tech-terms-e/#execution-time), le JSX est transpilé en JavaScript classique.

En d'autres termes, vous pouvez stocker des expressions JSX dans des variables, les utiliser dans des instructions `if` ou en faire la valeur de retour de fonctions.

**Exemple :**

`DisplayMyName.js`

```javascript
const firstName = false;
const myFirstName = <h1>My first name is Oluwatobi.</h1>;
const mylastName = <h1>My last name is Sofela.</h1>;
function DisplayMyName() {
  if (firstName) {
    return myFirstName;
  } else {
    return mylastName;
  }
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<DisplayMyName />);
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>DisplayMyName App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/babel" src="DisplayMyName.js"></script>
  </body>
</html>
```

L'extrait React ci-dessus stocke le code JSX dans des variables. Nous en avons également fait la valeur de retour de l'instruction `if...else` d'une fonction.

### Envelopper le JSX multi-ligne dans des parenthèses

Envelopper votre code JSX dans des parenthèses est préférable lorsqu'il s'étend sur plusieurs lignes. Cela rendra votre code lisible et évitera les [pièges de l'insertion automatique de points-virgules](https://stackoverflow.com/questions/2846283/what-are-the-rules-for-javascripts-automatic-semicolon-insertion-asi).

```javascript
const myName = (
  <div>
    <h1>My name is Oluwatobi.</h1>
  </div>
);
```

L'extrait ci-dessus enveloppe le `div` dans des parenthèses car il s'étend sur plusieurs lignes.

### Envelopper les expressions dans des accolades

Supposons que vous souhaitiez écrire des expressions JavaScript dans votre code JSX. Dans ce cas, enveloppez l'expression dans des accolades comme ceci :

`ExpressionInJSX.js`

```javascript
function ExpressionInJSX() {
  return <h2>JSX makes it {10 * 3} times faster to build React UIs.</h2>;
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<ExpressionInJSX />);
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>ExpressionInJSX App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/babel" src="ExpressionInJSX.js"></script>
  </body>
</html>
```

**Conseils :**

* React lit les accolades (`{...}`) dans le code JSX comme une expression JavaScript.
    
* L'utilisation d'accolades pour intégrer une expression JavaScript ne fonctionne que si vous l'utilisez de l'une des deux manières suivantes :
    
    1. Directement entre les balises JSX d'ouverture et de fermeture :
        
        ```xml
        <openingTag>I have a {javaScriptExpression} content.</closingTag>
        ```
        
    2. Comme valeur de l'attribut d'un élément JSX :
        
        ```xml
        <openingTag attribute={javaScriptExpression}>I have a content</openingTag>
        ```
        

### Utiliser le camelCase pour nommer les attributs

React utilise le [camelCase](https://codesweetly.com/naming-convention-explained/#what-is-camelcase) pour les clés d'attribut JSX plutôt que la convention de nommage des attributs HTML en minuscules. C'est parce que, sous le capot, le JSX est compilé en JavaScript pur et, par conséquent, utilise les API Web JavaScript.

En d'autres termes, au lieu d'écrire `readonly`, utilisez `readOnly`. De même, au lieu d'utiliser `maxlength`, écrivez `maxLength`. Ce faisant, React aura accès aux API Web JavaScript `readOnly` et `maxLength`.

**Exemple :**

```javascript
const myName = (
  <div>
    <h1 className="about-me">My name is Oluwatobi.</h1>
  </div>
);
```

### Fermer correctement les balises JSX vides

React exige de fermer explicitement tous les éléments JSX avec `/>`, y compris les balises vides. Par exemple, vous devrez écrire un élément HTML `<img>` comme `<img />`.

**Exemple :**

```javascript
const emptyJSXElement = <input type="button" value="Click me" />;
```

### Un composant React ne peut retourner qu'un seul élément

La création de deux éléments JSX ou plus à partir d'un composant nécessite de les envelopper dans un seul élément parent. Sinon, React renverra une erreur. C'est parce que les composants React ne retournent qu'un seul élément.

**Exemple :**

`TwoInnerUIs.js`

```javascript
function TwoInnerUIs() {
  return (
    <div>
      <h1>My name is Oluwatobi.</h1>
      <button>Buy me a coffee</button>
    </div>
  );
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<TwoInnerUIs />);
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>TwoInnerUIs App</title>
    <script src="https://unpkg.com/react@18/umd/react.development.js"></script>
    <script src="https://unpkg.com/react-dom@18/umd/react-dom.development.js"></script>
    <script src="https://unpkg.com/@babel/standalone/babel.min.js"></script>
  </head>
  <body>
    <div id="root"></div>
    <script type="text/babel" src="TwoInnerUIs.js"></script>
  </body>
</html>
```

Dans l'expression ci-dessus, le `<div>` est un élément parent contenant deux (2) balises internes.

**Conseil :** React permet d'utiliser un [fragment](https://react.dev/reference/react/Fragment) (balise vide) pour grouper des éléments. Voici un exemple :

```javascript
function TwoInnerUIs() {
  return (
    <>
      <h1>My name is Oluwatobi.</h1>
      <button>Buy me a coffee</button>
    </>
  );
}
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<TwoInnerUIs />);
```

Les fragments sont un excellent moyen de retourner plusieurs éléments sans créer de balises inutiles dans le DOM HTML.

## C'est l'heure de pratiquer avec JSX 🤸‍♂️🏋️‍♀️🏊‍♀️

C'est le moment de mettre en pratique les concepts JSX que vous avez appris.

Dans cet exercice, vous allez convertir le code JavaScript classique ci-dessous en son équivalent JSX :

```javascript
function SupportCodeSweetly() {
  return React.createElement(
    "div",
    { className: "support-ui" },
    React.createElement(
      "a",
      {
        id: "support-link",
        className: "support-link",
        target: "_blank",
        href: "https://www.buymeacoffee.com/codesweetly",
      },
      "Buy me a coffee"
    ),
    ". Thank you!"
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(React.createElement(SupportCodeSweetly));
```

Prenez un moment pour essayer par vous-même avant de regarder la solution ci-dessous. Même si vous devez essayer plusieurs fois, revenir lire les conseils ci-dessus ou chercher quelques trucs sur Google, cela vous aidera à mieux apprendre les concepts.

Ok, maintenant que vous avez essayé...

### La solution :

```javascript
function SupportCodeSweetly() {
  return (
    <div className="support-ui">
      <a
        id="support-link"
        className="support-link"
        target="_blank"
        href="https://www.buymeacoffee.com/codesweetly"
      >
        Buy me a coffee
      </a>
      . Thank you!
    </div>
  );
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<SupportCodeSweetly />);
```

Le composant `SupportCodeSweetly` retourne l'UI que nous voulons afficher à l'écran et gérer avec React. Mais qu'est-ce qu'un composant React exactement ?

## Qu'est-ce qu'un composant React ?

Un composant dans React est une classe ou une fonction qui accepte un seul argument appelé `props` et retourne un élément (UI).

### Syntaxe d'un composant React

![Syntaxe d'un composant React](https://cdn.hashnode.com/res/hashnode/image/upload/v1760626118056/8fb5818f-b39a-42c7-9399-1acc476604ee.webp align="center")

L'image ci-dessus illustre les parties constitutives d'un composant React :

1. Une fonction JavaScript avec une convention de nommage PascalCase.
    
2. Un paramètre props, qui est le seul argument que les composants React acceptent. (Conseil : props est l'abréviation de propriétés.)
    
3. Le corps du composant, où vous placez une séquence d'instructions comme des variables, des Hooks et des conditions.
    
4. Une instruction return, qui est utilisée pour sortir l'interface utilisateur (UI) que vous voulez que React affiche à l'écran. Cela peut être n'importe quel élément HTML valide.
    
5. Un invocateur qui exécute le composant pour récupérer son interface utilisateur. L'invocateur peut également passer des arguments (props) au composant.
    

### Exemple d'un composant React

```javascript
function MyBio(props) {
  return <h1>My name is {props.firstName}.</h1>;
}
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/jlj9lg?file=%2Fsrc%2Findex.js)

Le code dans l'extrait ci-dessus est un composant fonctionnel qui accepte un seul argument (props) et retourne un élément React.

### Bonnes pratiques pour les composants React

Lorsque vous travaillez avec des composants dans React, il y a quelques bonnes pratiques à suivre :

* Mettez une majuscule à la première lettre du nom de votre composant.
    
* N'utilisez pas d'expressions avec la notation entre crochets dans les balises de composants React.
    
* Les composants React fonctionnent mieux en tant que fonctions pures.
    
* Créez des composants au niveau supérieur de votre fichier.
    
* Divisez les composants longs en morceaux plus petits.
    

Comme il est courant d'utiliser des composants pour rendre une liste d'éléments, discutons maintenant de la manière d'implémenter cela de manière optimale.

## Comment rendre des listes d'éléments à partir d'un tableau

Supposons que vous souhaitiez créer une liste d'éléments React à partir d'un tableau de données. Vous pouvez utiliser la méthode JavaScript [`map()`](https://codesweetly.com/javascript-map-method/).

**Exemple :**

```javascript
import ReactDOM from "react-dom/client";

// Définir le tableau bestColors :
const bestColors = ["Blue", "White", "Pink"];

// Utiliser le tableau bestColors pour créer une liste d'éléments React :
const bestColorsLiElements = bestColors.map((color) => <li>{color}</li>);

// Rendre le tableau d'éléments <li> dans le DOM racine :
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<ul>{bestColorsLiElements}</ul>);
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/dcwwqr?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus a utilisé `map()` pour créer une nouvelle liste d'éléments React en convertissant chacun des éléments de `bestColors` en éléments `<li>`.

Remarquez que nous avons rendu la liste d'éléments directement dans la méthode `root.render()`. Typiquement, vous utiliseriez un composant pour effectuer un tel rendu. Faisons donc un peu de refactorisation en déplaçant la variable `bestColorsLiElements` et l'élément `<ul>` dans un composant :

```javascript
import ReactDOM from "react-dom/client";

function BestColor() {
  // Définir le tableau bestColors :
  const bestColors = ["Blue", "White", "Pink"];
  // Utiliser le tableau bestColors pour créer une liste d'éléments React :
  const bestColorsLiElements = bestColors.map((color) => <li>{color}</li>);
  return <ul>{bestColorsLiElements}</ul>;
}

// Rendre le tableau d'éléments <li> dans le DOM racine :
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/pj62c3?file=%2Fsrc%2Findex.js)

Bien que l'extrait ci-dessus affiche le bon contenu à l'écran, il n'est pas efficace. React renvoie donc une erreur dans la console. Discutons du problème.

### Chaque élément React dans un tableau a besoin d'une clé unique

Si vous vérifiez votre console, vous verrez un message d'avertissement qui dit : `Each child in a list should have a unique "key" prop.`

Ce message signifie que chaque fois que vous créez un tableau d'éléments, React a besoin que vous spécifiiez une identité unique pour chaque élément de la liste.

Les clés d'identité uniques aident React à identifier les changements apportés au tableau.

Refactorisons l'extrait précédent pour que chaque élément de `bestColorsLiElements` ait une prop `key` unique.

### Comment ajouter des clés uniques à chaque élément React dans un tableau

Il existe deux manières courantes d'attribuer des clés uniques à chaque élément d'un tableau. La première est la méthode non recommandée. Bien que la seconde soit la meilleure technique, il vaut la peine de noter les deux.

#### Manière non recommandée d'attribuer des clés à un tableau d'éléments React

Une façon d'ajouter des clés uniques est d'utiliser l'index de chaque élément comme prop `key`.

**Conseil :** Par défaut, si vous ne fournissez pas de prop `key`, React utilise la position d'index de chaque élément dans le tableau pour les identifier (`key=0`, `key=1`, etc.).

**Exemple :**

```javascript
import ReactDOM from "react-dom/client";

function BestColor() {
  const bestColors = ["Blue", "White", "Pink"];
  // Utiliser l'index de chaque élément comme prop key :
  const bestColorsLiElements = bestColors.map((color, index) => (
    <li key={index}>{color}</li>
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/yxp4sz?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus spécifie une prop `key` sur chaque élément `<li>`. Il utilise ensuite l'index (`index`) de chaque élément comme valeur de la prop.

Mais notez qu'il est préférable d'éviter d'utiliser les index comme prop `key` d'un élément React. Vous ne devriez l'utiliser qu'en dernier recours lorsque vous n'avez pas d'identifiants stables.

Chaque fois que vous utilisez un index comme prop `key`, assurez-vous que l'ordre des éléments dans le tableau ne change jamais. Sinon, vous pourriez avoir de graves problèmes de performance et d'état du composant.

#### Meilleure façon d'attribuer des clés à un tableau d'éléments React

La meilleure façon d'ajouter des clés uniques à chaque élément React dans un tableau est d'utiliser des identifiants stables provenant de l'une des sources suivantes :

* **Base de données :** Utilisez les identifiants générés par la base de données comme props `key` si vos données proviennent d'une base de données, car ils sont uniques par défaut.
    
* `crypto.randomUUID()` **compteur incrémentiel :** Utilisez la méthode `randomUUID()` pour générer des identifiants universellement uniques (UUID) si vous créez et stockez vos données localement. (Note : Cette méthode est une API web. Elle n'est donc disponible que dans les contextes HTTPS des navigateurs compatibles.)
    
* `uuid` : Un package NPM pour générer des identifiants universellement uniques si vous créez et persistez vos données localement. C'est une bonne alternative à la méthode `randomUUID()` pour la compatibilité multiplateforme.
    

**Exemple :**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function BestColor() {
  // Utiliser l'id de chaque élément comme prop key :
  const bestColorsLiElements = bestColors.map((color) => (
    <li key={color.id}>{color.name}</li>
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
export const bestColors = [
  { id: crypto.randomUUID(), name: "Blue" },
  { id: crypto.randomUUID(), name: "White" },
  { id: crypto.randomUUID(), name: "Pink" },
];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/n56z6x?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus spécifie une prop `key` sur chaque élément `<li>`. Il utilise ensuite l'identifiant (`id`) de chaque élément comme valeur de la prop.

**Note :** Chaque prop `key` doit être unique parmi ses frères et sœurs – pas globalement. Il est acceptable d'utiliser la même `key` pour un élément dans un tableau différent.

### Choses essentielles à savoir sur l'attribution des clés

Voici des faits essentiels à retenir chaque fois que vous attribuez des clés à un tableau d'éléments React.

#### 1. Définir la clé de chaque élément du tableau lors de la création du tableau

Le bon endroit pour spécifier la clé unique de chaque élément du tableau est directement à l'intérieur de la méthode `map()` *pendant la création de la liste d'éléments*.

En d'autres termes, supposons que vous extrayiez votre élément de modèle dans un composant séparé. Définissez la prop `key` sur la balise d'invocation du composant — pas sur l'élément de modèle extrait.

**Exemple 1 : Mauvais placement de la prop key**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function ColorListElement({ color }) {
  // FAUX : Ne placez pas la clé en dehors de la méthode map().
  return <li key={color.id}>{color.name}</li>;
}

function BestColor() {
  const bestColorsLiElements = bestColors.map((color) => (
    // L'attribut key ci-dessus aurait dû être défini ici.
    <ColorListElement color={color} />
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
export const bestColors = [
  { id: crypto.randomUUID(), name: "Blue" },
  { id: crypto.randomUUID(), name: "White" },
  { id: crypto.randomUUID(), name: "Pink" },
];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/frcspn?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus définit incorrectement la clé de chaque élément en dehors de la méthode `map()`. Vous devriez éviter une telle erreur !

Définissez toujours la prop `key` *pendant la création du tableau d'éléments*. Ainsi, l'extrait ci-dessus aurait dû définir la `key` sur la balise d'invocation du composant – dans la méthode `map()`.

**Exemple 2 : Placement correct de la prop key**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function ColorListElement({ color }) {
  return <li>{color.name}</li>;
}

function BestColor() {
  const bestColorsLiElements = bestColors.map((color) => (
    // CORRECT : Définissez toujours la clé directement dans la méthode map().
    <ColorListElement key={color.id} color={color} />
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
export const bestColors = [
  { id: crypto.randomUUID(), name: "Blue" },
  { id: crypto.randomUUID(), name: "White" },
  { id: crypto.randomUUID(), name: "Pink" },
];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/n9m7w2?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus définit correctement la clé de chaque élément à l'intérieur de la méthode `map()`. Cela permet à React d'accéder à la valeur `key` pour chaque élément du tableau retourné par la méthode `map()`.

**Conseil :** L'algorithme de réconciliation (diffing) de React est programmé pour accéder à la `key` de chaque élément de niveau supérieur du tableau. Il ne cherche jamais la `key` dans les éléments enfants ou descendants.

#### 2. React ne transmet pas les clés aux composants

React ne transfère pas la prop `key` aux composants et ne l'inclut pas non plus comme attribut d'un élément rendu.

React utilise les clés uniquement pour connaître l'état des éléments du tableau. Elles aident React à identifier les changements apportés au tableau.

Donc, si vous avez besoin d'utiliser la valeur d'une clé spécifique dans votre composant ou sur votre élément DOM, vous devez la passer explicitement comme valeur d'un attribut différent.

**Exemple :**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function ColorListElement(props) {
  return (
    <li>
      {props.color.name} (ID: {props.id})
    </li>
  );
}

function BestColor() {
  // Utiliser `color.id` comme valeur des props `key` et `id`.
  const bestColorsLiElements = bestColors.map((color) => (
    <ColorListElement key={color.id} id={color.id} color={color} />
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
export const bestColors = [
  { id: crypto.randomUUID(), name: "Blue" },
  { id: crypto.randomUUID(), name: "White" },
  { id: crypto.randomUUID(), name: "Pink" },
];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/v7yflr?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus initialise l'attribut `id` de chaque élément de la liste avec la même valeur que la prop `key`. Ce faisant, le composant `ColorListElement` peut accéder à `props.id` mais pas à `props.key`.

#### 3. Générez toujours les clés en dehors de vos composants

Ne générez jamais de clés à la volée (pendant le [rendu](https://codesweetly.com/web-tech-terms-r/#react-render) de vos composants). Au lieu de cela, créez-les dans vos données en dehors de vos composants. Sinon, React recréera les éléments à chaque cycle de rendu car la valeur de la `key` sera toujours différente.

**Exemple 1 : Mauvais endroit pour générer la prop key**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function BestColor() {
  // FAUX : Ne générez jamais de clés à la volée.
  const bestColorsLiElements = bestColors.map((color) => (
    <li key={crypto.randomUUID()}>{color}</li>
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
// Les valeurs des clés auraient dû être définies ici (en dehors du composant lors de la création de vos données).
export const bestColors = ["Blue", "White", "Pink"];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/lhwknv?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus a généré incorrectement la clé de chaque élément pendant le rendu du composant `BestColor`. Vous devriez éviter une telle erreur pour prévenir les bugs subtils causés par la recréation des éléments à chaque rendu.

Créez toujours la valeur de chaque `key` dans vos données en dehors du composant.

**Exemple 2 : Endroit correct pour générer la prop key**

`index.js`

```javascript
import { createRoot } from "react-dom/client";
import { bestColors } from "./bestColors.js";

function BestColor() {
  const bestColorsLiElements = bestColors.map((color) => (
    <li key={color.id}>{color.name}</li>
  ));
  return <ul>{bestColorsLiElements}</ul>;
}

const root = createRoot(document.getElementById("root"));
root.render(<BestColor />);
```

`bestColors.js`

```javascript
// CORRECT : Générez toujours la clé dans vos données en dehors du composant.
export const bestColors = [
  { id: crypto.randomUUID(), name: "Blue" },
  { id: crypto.randomUUID(), name: "White" },
  { id: crypto.randomUUID(), name: "Pink" },
];
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/n56z6x?file=%2Fsrc%2Findex.js)

L'extrait ci-dessus a correctement généré la clé de chaque élément dans les données du tableau en dehors du composant.

## Comment gérer les événements dans React

La gestion des événements dans React consiste à configurer vos éléments JSX pour qu'ils répondent aux interactions des utilisateurs sur ceux-ci (telles que les clics de souris, la soumission de formulaires et le focus sur un élément).

```xml
<jsxTag onEvent={handleEvent}>UI Content</jsxTag>
```

Voici ce qui se passe :

* `jsxTag` : Éléments React comme `<div>`, `<button>` et `<input>`.
    
* `onEvent` : L'écouteur d'événement que vous souhaitez ajouter à l'élément React. Quelques exemples sont `onClick`, `onBlur` et `onHover`.
    
* `handleEvent` : La fonction de gestionnaire d'événement que vous souhaitez utiliser pour gérer (répondre à) le type `onEvent` spécifié.
    

**Conseil :** Bien que vous puissiez nommer le gestionnaire d'événement comme vous le souhaitez, la convention de nommage typique consiste à préfixer le nom de l'événement par « handle ». Par exemple, si le nom de l'événement est `focus`, le nom du gestionnaire sera `handleFocus`.

### Types de gestionnaires d'événements

Il existe deux manières typiques de définir la fonction de gestionnaire d'événement dans React :

* **Gestionnaire d'événement en ligne :** Une fonction définie directement sur la balise d'ouverture d'un élément JSX comme valeur de la prop de l'écouteur d'événement (`onEvent`).
    
* **Gestionnaire d'événement référencé :** Une fonction définie comme une logique séparée (indépendante) et liée à un attribut d'écouteur d'événement (`onEvent`) par référence de nom.
    

#### Exemple : Gestionnaire d'événement en ligne

```javascript
export default function App() {
  return (
    <h1 onClick={() => alert("You clicked the heading!")}>
      Oluwatobi is my name.
    </h1>
  );
}
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/7tx7l5?file=%2Fsrc%2Fcomponents%2FApp.js)

#### Exemple : Gestionnaire d'événement référencé

```javascript
export default function App() {
  return <h1 onClick={handleClick}>Oluwatobi is my name.</h1>;
}

const handleClick = () => alert("You clicked the heading!");
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/msfszz?file=%2Fsrc%2Fcomponents%2FApp.js)

Les composants React ont une mémoire unique qui leur permet de se souvenir de choses entre les rendus. Cette mémoire est appelée « state ».

## Qu'est-ce que le State React ?

Le state React est la *mémoire d'un composant* pour stocker des données dont React doit se souvenir pendant le re-rendu d'un composant et dont la mise à jour doit déclencher un nouveau rendu.

### Syntaxe du State React :

```javascript
import { useState } from "react";

function App() {
  const [state, setState] = useState(initialState);

  // ...
}
```

* `state` : La variable contenant la valeur du state du composant.
    
* `setState` : Une fonction pour mettre à jour la valeur du state.
    
* `useState` : Le Hook de state pour initialiser et récupérer le state du composant.
    

### Exemple du State React :

```javascript
import { useState } from "react";

function AboutCompany() {
  const [age, setAge] = useState(5);

  function updateAge() {
    setAge(age + 1);
  }

  return (
    <div>
      <h3>CodeSweetly is {age} years old!</h3>
      <button type="button" onClick={updateAge}>
        Click to update age
      </button>
    </div>
  );
}

export default AboutCompany;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/9mlsl7?file=%2Fsrc%2FAboutCompany.js)

Lorsqu'un utilisateur clique sur le bouton de l'UI, l'événement `onClick` déclenche le gestionnaire d'événement `updateAge`, qui utilise la fonction setter `setAge` pour mettre à jour le state `age` du composant.

**Conseil :** React déclenchera un re-rendu de votre composant chaque fois que vous utiliserez la fonction setter de `useState` pour mettre à jour votre state. Mais que signifient exactement les termes « trigger » et « render » ?

### React trigger vs render vs Commit vs paint

Le déclenchement (triggering), le rendu (rendering), le Commit et la peinture (painting) sont les étapes impliquées dans l'affichage des UI React à l'écran. Voici les différences entre ces quatre étapes :

![Cycle de vie d'un composant React](https://cdn.hashnode.com/res/hashnode/image/upload/v1760637870319/ed8ae7a7-67c1-468a-ba5f-dbbafed8deb0.webp align="center")

La diapositive ci-dessus illustre les quatre phases du cycle de vie de l'UI d'un composant :

* **Trigger :** Spécifie le composant dont vous souhaitez afficher l'UI à l'écran.
    
* **Render :** Appelle le composant que vous avez déclenché.
    
* **Commit :** Met à jour le DOM avec l'UI du composant rendu.
    
* **Paint :** Convertit le code DOM que vous avez Commit en éléments conviviaux avec lesquels les utilisateurs peuvent interagir dans leurs navigateurs.
    

Discutons de ces différences en détail.

### Que signifie déclencher (trigger) un rendu dans React ?

L'événement trigger est la première étape de l'affichage d'une interface utilisateur (UI) React à l'écran. Il spécifie le composant dont vous souhaitez afficher l'UI à l'écran. Cet événement se produit à deux occasions :

1. Lorsque l'application commence à s'exécuter. L'application React utilise la méthode `createRoot` pour spécifier le composant dont vous souhaitez rendre l'UI dans un nœud DOM.
    

```javascript
import ReactDOM from "react-dom/client";
import DonationUI from "./components/DonationUI.js";

// Lorsque l'application commence à s'exécuter, vous devez utiliser createRoot et sa méthode render pour déclencher un rendu initial du composant racine de l'application.
const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<DonationUI />);
```

L'extrait ci-dessus fait ce qui suit :

* Utilise la méthode `ReactDOM.createRoot()` pour créer une instance d'objet `ReactDOMRoot` pour l'argument de l'élément `root`.
    
* Utilise la méthode `render()` de l'instance d'objet pour déclencher un rendu initial du composant `DonationUI`.
    

En d'autres termes, la méthode `createRoot().render()` spécifie `DonationUI` comme le composant dont React doit afficher l'UI dans l'élément HTML `root`.

2. La deuxième raison pour laquelle un événement trigger peut se produire est lorsqu'un state d'un composant (ou de ses ancêtres) est mis à jour avec une fonction setter.
    

`DonationUI.js`

```javascript
import React from "react";

function DonationUI() {
  const [donate, setDonate] = React.useState(false);
  function createUserInterface() {
    if (donate) {
      return (
        <p>
          <a href="https://www.buymeacoffee.com/codesweetly">Support page</a>.
          Thank you so much!
        </p>
      );
    }
    // La fonction setDonate déclenchera un re-rendu du composant DonationUI.
    return <button onClick={() => setDonate(true)}>Buy me a coffee</button>;
  }
  return createUserInterface();
}

export default DonationUI;
```

L'extrait ci-dessus fait ce qui suit :

1. Définit un composant nommé `DonationUI`.
    
2. Initialise le state du composant avec la valeur booléenne `false`.
    
3. Programme le composant pour retourner un élément de paragraphe si la variable `donate` du state est `true`. Sinon, il doit retourner un élément bouton.
    

Lorsque les utilisateurs cliquent sur l'élément bouton, la fonction setter `setDonate` déclenchera un re-rendu du composant `DonationUI`. Vous trouverez ci-dessous le script d'entrée et le code HTML pour que vous puissiez l'essayer vous-même localement.

`index.js`

```javascript
import ReactDOM from "react-dom/client";
import DonationUI from "./components/DonationUI";

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<DonationUI />);
```

`index.html`

```xml
<!DOCTYPE html>
<html lang="en-US">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>CodeSweetly DonationUI</title>
  </head>
  <body>
    <main id="root"></main>
    <script type="module" src="index.js"></script>
  </body>
</html>
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/95nvmr?file=%2Fsrc%2Fcomponents%2FDonationUI.js)

### Que signifie rendre des composants React ?

L'étape de rendu (rendering) est le moment où React [invoque (appelle)](https://codesweetly.com/invoke-vs-call/) le composant que vous avez déclenché avec la méthode `createRoot` ou une fonction setter. Le rendu amène React à invoquer un composant pour produire l'UI que vous souhaitez afficher à l'écran. Le composant que React rendra dépend du moment où l'événement trigger s'est produit :

* **Pour un trigger initial (au démarrage de l'application),** React invoquera le composant racine de l'application.
    
* **Pour les triggers de mise à jour (chaque fois que le state d'un composant est mis à jour),** React appellera le composant fonctionnel dont la mise à jour du state a initié l'événement trigger.
    

**Conseil :** Rendre un composant signifie « appeler un composant » pour récupérer son interface utilisateur (UI).

### Que signifie Commit une UI React vers le DOM du navigateur ?

L'étape de Commit est le moment où React met à jour le DOM avec l'UI du composant rendu.

Il y a des choses importantes à noter à propos de ce processus :

* **Pour un rendu initial (au démarrage de l'application),** React initialisera le DOM racine avec l'UI du composant racine. Il utilisera l'API JavaScript `appendChild()` pour ajouter les nœuds DOM (UI) récupérés du composant dans l'élément HTML racine de l'application.
    
* **Pour les re-rendus ultérieurs (après le Commit initial),** React ne mettra à jour les nœuds DOM que s'il y a une différence entre la sortie du rendu précédent et la plus récente. Aucun changement ne se produira si la dernière sortie du composant est la même que celle précédemment Commit.
    

### Que signifie peindre (paint) les nœuds DOM sur l'écran ?

L'étape de peinture (rendu du navigateur) est le moment où le navigateur repeint l'écran pour convertir le code DOM en éléments conviviaux. Il s'agit d'un processus au niveau du navigateur qui commence une fois que React a fini de mettre à jour (Commit) les nœuds DOM.

Parfois, les composants ont besoin de stocker des informations qui ne devraient pas déclencher un rendu lors de leur mise à jour. Dans ces situations, vous pouvez utiliser une ref.

## Qu'est-ce que le Hook Ref de React ?

Le Hook Ref de React vous permet de stocker des valeurs qui ne déclenchent pas de re-rendus lorsqu'elles sont modifiées.

### Syntaxe du Hook ref de React

Le Hook `useRef` n'accepte qu'un seul argument optionnel. Voici la syntaxe :

```javascript
useRef(initialValue);
```

* `initialValue` : La valeur à stocker dans la mémoire ref du composant. N'importe quel type de données JavaScript est autorisé.
    
* `useRef()` : Retourne un objet (`{ current: initialValue }`).
    

### Exemple du Hook ref de React :

```javascript
import { useRef } from "react";

function App() {
  const myNameRef = useRef("Oluwatobi");

  function handleClick() {
    console.log(myNameRef.current); // Affiche : "Oluwatobi"
  }

  return <button onClick={handleClick}>Click me</button>;
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/mgsxyq?file=%2Fsrc%2FApp.js)

L'extrait ci-dessus a utilisé le Hook `useRef` pour stocker une valeur (`"Oluwatobi"`) dont la mise à jour ne devrait pas déclencher de re-rendus.

### Bonnes pratiques du Hook ref de React

Lorsque vous travaillez avec le Hook ref de React, il y a quelques bonnes pratiques à suivre :

* Utilisez la syntaxe par point pour accéder et mettre à jour la valeur d'un objet ref au lieu de la notation entre crochets.
    
* Évitez d'accéder ou de mettre à jour la propriété `current` pendant le rendu pour maintenir la pureté de vos composants.
    
* N'utilisez pas une instance de fonction comme `initialValue`. Passez la fonction elle-même, pas son résultat.
    
* Vous pouvez utiliser le Hook ref de React pour gérer vos nœuds DOM HTML.
    

Mais quelle est la différence entre les refs, les states et les variables, me demanderez-vous ? Découvrons-le ci-dessous.

## Variables vs Refs vs States dans React

Dans React, les variables, les refs et les states vous permettent de stocker et de muter des données. Mais ils fonctionnent de manières différentes. Voici les principales distinctions entre eux :

1. Sa valeur persiste-t-elle pendant le re-rendu ?
    
    * React Ref : Oui
        
    * React State : Oui
        
    * Variable JavaScript : Non
        
2. La mise à jour de sa valeur déclencherait-elle un re-rendu du composant ?
    
    * React Ref : Non
        
    * React State : Oui
        
    * Variable JavaScript : Non
        
3. Est-ce du JavaScript pur ?
    
    * React Ref : Oui
        
    * React State : Non
        
    * Variable JavaScript : Oui
        
4. Pouvez-vous le déclarer en dehors d'un composant ?
    
    * React Ref : Non
        
    * React State : Non
        
    * Variable JavaScript : Oui
        
5. Est-il utilisable dans des instructions conditionnelles, des boucles ou des fonctions imbriquées ?
    
    * React Ref : Non
        
    * React State : Non
        
    * Variable JavaScript : Oui
        

### Comment fonctionnent les variables dans React ?

La valeur d'une [variable](https://codesweetly.com/javascript-variable/) ne persiste pas pendant le re-rendu. Sa valeur se réinitialise au début d'un nouveau rendu.

**Exemple :**

```javascript
import { useState } from "react";

function App() {
  let myVar = 0;
  const [myState, setMyState] = useState(0);

  function updateVar() {
    myVar = myVar + 1;
    console.log("myVar =", myVar);
  }

  function updateState() {
    setMyState(myState + 1);
  }

  return (
    <div>
      <h2>Variable: {myVar}</h2>
      <h2>State: {myState}</h2>
      <button onClick={updateVar}>Update Variable</button>
      <button onClick={updateState}>Update State</button>
    </div>
  );
}

export default App;
```

[**Essayer de l'éditer**](https://codesweetly.com/variables-vs-refs-vs-states-in-react/try-it-sdk-vitejs-vite-u6yjihmv)

L'extrait ci-dessus va :

* Incrémenter la valeur de la variable lorsque vous cliquez sur le bouton « Update Variable ». Cette modification ne déclenche pas de re-rendu du composant car React ne suit pas les changements d'une variable.
    
* Incrémenter la valeur du state lorsque vous cliquez sur le bouton « Update State ». Cette modification déclenche un re-rendu du composant car React demande un re-rendu chaque fois que vous modifiez le state.
    
* Réinitialiser la valeur de la variable à zéro (0) lors de chaque re-rendu du composant App. Par conséquent, la valeur de la variable affichée sera toujours zéro (0).
    

### Comment fonctionnent les refs dans React ?

La valeur d'une ref persiste pendant le re-rendu, mais sa modification ne provoque pas de re-rendu du composant par React. En d'autres termes, une ref est un simple [objet JavaScript](https://codesweetly.com/javascript-properties-object/) dont React se souvient pendant le re-rendu de votre composant. Mais React ne suit pas les changements de la valeur de la ref. Ainsi, ses modifications ne déclenchent pas de nouveau rendu.

**Exemple :**

```javascript
import { useState, useRef } from "react";

function App() {
  const myRef = useRef(0);
  const [myState, setMyState] = useState(0);

  function updateRef() {
    myRef.current = myRef.current + 1;
    console.log("myRef =", myRef);
  }

  function updateState() {
    setMyState(myState + 1);
  }

  return (
    <div>
      <h2>Ref: {myRef.current}</h2>
      <h2>State: {myState}</h2>
      <button onClick={updateRef}>Update Ref</button>
      <button onClick={updateState}>Update State</button>
    </div>
  );
}

export default App;
```

[**Essayer de l'éditer**](https://codesweetly.com/variables-vs-refs-vs-states-in-react/try-it-sdk-vitejs-vite-xyjh2fev)

L'extrait ci-dessus va :

* Incrémenter la valeur de la ref lorsque vous cliquez sur le bouton « Update Ref ». Cette modification ne déclenche pas de re-rendu du composant car React ne surveille pas les changements de la ref.
    
* Incrémenter la valeur du state lorsque vous cliquez sur le bouton « Update State ». Cette modification déclenche un re-rendu du composant car React demande un re-rendu chaque fois que vous modifiez le state.
    
* Conserver la valeur de la ref et du state lors de chaque re-rendu du composant App.
    

### Comment fonctionnent les states dans React ?

La valeur d'un state persiste pendant le re-rendu. Sa modification provoque également le re-rendu du composant par React.

**Exemple :**

```javascript
import { useState, useRef } from "react";

function App() {
  let myVar = 0;
  const myRef = useRef(0);
  const [myState, setMyState] = useState(0);

  function updateVarAndRef() {
    myVar = myVar + 1;
    myRef.current = myRef.current + 1;
    console.log("myVar =", myVar);
    console.log("myRef =", myRef);
  }

  function updateState() {
    setMyState(myState + 1);
  }

  return (
    <div>
      <h2>Variable: {myVar}</h2>
      <h2>Ref: {myRef.current}</h2>
      <h2>State: {myState}</h2>
      <button onClick={updateVarAndRef}>Update Variable and Ref</button>
      <button onClick={updateState}>Update State</button>
    </div>
  );
}

export default App;
```

[**Essayer de l'éditer**](https://codesweetly.com/variables-vs-refs-vs-states-in-react/try-it-sdk-vitejs-vite-gklkzfps)

L'extrait ci-dessus va :

* Incrémenter la valeur de la variable et de la ref lorsque vous cliquez sur le bouton « Update Variable and Ref ». Cette modification ne déclenche pas de re-rendu du composant car React ne surveille pas les changements de la variable ou de la ref.
    
* Incrémenter la valeur du state lorsque vous cliquez sur le bouton « Update State ». Cette modification déclenche un re-rendu du composant car React demande un re-rendu chaque fois que vous modifiez le state.
    
* Réinitialiser la valeur de la variable lors de chaque re-rendu du composant App, tout en conservant les données de la ref et du state.
    

### Conseils sur l'utilisation des variables, des refs et des states dans React

* Utilisez des variables pour les valeurs qui doivent se réinitialiser à chaque rendu du composant.
    
* Utilisez le Hook Ref pour stocker des valeurs que les utilisateurs n'ont pas besoin de voir à l'écran, car les changements apportés à la ref ne déclencheront pas de re-rendu du composant.
    
* Le state React est idéal pour stocker des valeurs que vous souhaitez afficher à l'écran, car les changements de state déclenchent un re-rendu du composant.
    

Les composants React ont parfois besoin de récupérer des données ou de modifier le DOM pendant différentes phases du cycle de vie : trigger, render, Commit et paint. Le Hook d'effet peut aider à accomplir ces tâches.

## Qu'est-ce que le Hook useEffect ?

Le Hook `useEffect` permet aux composants fonctionnels d'effectuer des effets de bord en dehors de React.

### Syntaxe du Hook useEffect

Le Hook `useEffect` accepte deux arguments. Voici la syntaxe :

```javascript
useEffect(callback, array);
```

* `callback` : La fonction de configuration requise pour le Hook useEffect.
    
* `array` : (Optionnel) La liste des dépendances réactives qui indique quand React exécute le callback.
    

**Conseil :** React exécute la fonction de configuration après le montage du composant ou lorsque les dépendances changent.

### Exemple du Hook useEffect :

```javascript
import { useState, useEffect } from "react";

function AboutCompany() {
  const [age, setAge] = useState(5);

  useEffect(() => {
    document.title = `🥳🎁🎉 It's CodeSweetly's birthday! 🎉🎁🥳`;
  });

  return (
    <div>
      <h3>CodeSweetly is {age} years old!</h3>
      <button type="button" onClick={() => setAge(age + 1)}>
        Click to update age
      </button>
    </div>
  );
}

export default AboutCompany;
```

Le code `useEffect` met à jour le titre du navigateur une fois que l'UI a fini de s'afficher.

### Bonnes pratiques du Hook useEffect

Comme toujours, il existe quelques bonnes pratiques pour utiliser ce Hook le plus efficacement possible :

* Utilisez `useEffect` pour vous connecter à des éléments extérieurs à votre application React, tels que des API ou des minuteurs. Si votre code n'a pas d'effets de bord, vous n'en avez probablement pas besoin.
    
* Évitez d'ajouter des valeurs au tableau de dépendances à moins que votre effet ne les utilise. Incluez uniquement le state et les props nécessaires pour éviter les réexécutions inutiles.
    
* Déclarez les objets et fonctions statiques en dehors des composants. Placez les éléments dynamiques à l'intérieur de votre Hook d'effet.
    
* Lorsque vous dépendez de props d'objet, listez chaque valeur primitive utilisée dans votre effet au lieu de l'objet entier.
    
* Utilisez `StrictMode` pour aider à détecter les problèmes courants du Hook useEffect pendant le développement.
    

Les bases de React étant couvertes, discutons du stylisme.

## Comment styliser les composants React

Les quatre principales façons de styliser les éléments React sont :

* Les feuilles de style CSS
    
* Les attributs de style en ligne
    
* Les CSS Modules
    
* Les bibliothèques CSS-in-JS
    

Discutons de ces quatre techniques de stylisme.

### Comment utiliser les feuilles de style CSS pour styliser les éléments React

Voici les étapes pour styliser les éléments JSX avec des feuilles de style CSS classiques.

#### 1. Créer une feuille de style CSS

Tout d'abord, créez une feuille de style CSS dans vos projets React.

```console
touch styles.css
```

**Conseil :** Vous pouvez créer la feuille de style n'importe où dans le répertoire de votre projet.

#### 2. Définir votre règle de style

Ouvrez le fichier CSS nouvellement créé et déclarez vos styles.

**Exemple :**

`styles.css`

```css
.text {
  color: seagreen;
  font-weight: bold;
}
```

L'extrait CSS ci-dessus indique aux navigateurs d'appliquer une couleur `seagreen` et un poids de police `bold` aux éléments ayant un nom de classe `text`.

#### 3. Appliquer la règle de la feuille de style à votre élément

Importez votre feuille de style dans le fichier du composant contenant l'élément que vous souhaitez styliser. Ensuite, appliquez-lui la règle de la feuille de style.

**Exemple :**

`App.js`

```javascript
// Importez votre feuille de style (le chemin vers votre feuille de style peut être différent).
import "../styles.css";

function App() {
  return <div className="text">Oluwatobi is my name.</div>;
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/mq5xzp?file=%2Fsrc%2FApp.js)

L'extrait ci-dessus indique à React d'appliquer la règle `"text"` sur l'élément avec un attribut `className="text"`.

### Comment utiliser l'attribut style en ligne pour styliser les éléments React

React vous permet d'appliquer des styles en ligne aux éléments JSX de la même manière que le CSS en ligne fonctionne en HTML. Mais il y a quelques différences à garder à l'esprit.

Premièrement, le HTML applique les styles en ligne sous forme de valeur de chaîne de caractères :

```xml
<div style="color:seagreen; font-weight:bold;">Oluwatobi is my name.</div>
```

Mais dans React, vous devez définir les styles en ligne comme des objets, pas des chaînes :

```javascript
<div style={{ color: "seagreen", fontWeight: "bold" }}>
  Oluwatobi is my name.
</div>
```

L'extrait ci-dessus utilise deux jeux d'accolades car en JSX (comme je l'ai mentionné plus haut), vous enveloppez les [expressions JavaScript](https://codesweetly.com/javascript-statement/#what-is-a-javascript-expression-statement) à l'intérieur d'accolades : par exemple, `<div>{myNameVariable}</div>`.

Donc, supposons que l'expression soit un objet littéral JavaScript. Dans ce cas, vous aurez besoin de deux jeux d'accolades : par exemple, `<div>{{ name: "Oluwatobi" }}</div>`.

Par conséquent, dans `style={{ color: seagreen, fontWeight: bold }}`, le premier jeu d'accolades (`{...}`) indique à React que vous voulez écrire une expression JavaScript. Le deuxième jeu d'accolades (`{ color: seagreen, fontWeight: bold }`) est l'expression JavaScript (un objet) que vous assignez comme valeur de l'attribut `style`.

**Exemple :**

`App.js`

```javascript
function App() {
  return (
    <div style={{ color: "seagreen", fontWeight: "bold" }}>
      Oluwatobi is my name.
    </div>
  );
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/84cmjf?file=%2Fsrc%2FApp.js)

L'extrait React ci-dessus indique à l'ordinateur d'appliquer un style en ligne à l'élément `div`.

Vous pouvez voir que nous avons écrit `fontWeight` en [camelCase](https://codesweetly.com/naming-convention-explained/#what-is-camelcase). C'est parce que, sous le capot, le JSX est compilé en JavaScript pur. Il utilise donc la convention de nommage des attributs des API Web JavaScript.

Pour rendre votre code plus facile à lire, envisagez de stocker votre objet de style en ligne dans une variable séparée comme ceci :

`App.js`

```javascript
function App() {
  // Stocker votre objet de style en ligne dans une variable :
  const textStyles = { color: "seagreen", fontWeight: "bold" };
  return <div style={textStyles}>Oluwatobi is my name.</div>;
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/2llmwy?file=%2Fsrc%2FApp.js)

**Conseil :** Le Framework Tailwind CSS est un outil de stylisme en ligne qui fournit des classes utilitaires que vous pouvez appliquer directement à un élément. Il offre des fonctionnalités supplémentaires qui manquent souvent au stylisme en ligne classique. Par exemple, Tailwind vous permet de configurer des media queries et des états d'événements (tels que `hover`, `focus` et `active`) dans les styles en ligne.

### Comment utiliser les CSS modules pour styliser les éléments React

Comme défini dans la [documentation officielle](https://github.com/css-modules/css-modules), un CSS Module est un fichier CSS dans lequel tous les noms de classes et noms d'animations sont portés localement par défaut.

Les CSS Modules partagent de nombreuses similitudes avec une feuille de style CSS classique. Mais il existe quelques différences essentielles.

#### 1. Convention de nom de fichier

La syntaxe pour nommer une feuille de style CSS classique est `[nom].css` : par exemple, `codesweetly-styles.css`.

Mais la convention de nommage de fichier d'un CSS module est `[nom].module.css` : par exemple, `codesweetly-styles.module.css`.

#### 2. Portée des styles

L'importation d'une feuille de style CSS dans votre fichier de script rend ses règles de style disponibles *globalement* pour tous les composants (et composants enfants) de ce script.

Mais l'importation d'un CSS module dans votre fichier de script ne rend ses règles de style disponibles que *localement* pour le composant qui invoque la règle du module. De plus, ce composant doit se trouver dans le script qui importe le CSS module.

**Exemple :**

Créez une feuille de style CSS classique dans votre projet React et ajoutez-y quelques règles :

`styles.css`

```css
.imageInfo {
  text-align: center;
  color: #442109;
}
```

Créez également un CSS module dans le même projet et ajoutez-y quelques règles :

`styles.module.css`

```css
.imageInfo {
  border: 8px ridge #71380f;
  background-color: #ffe5b4;
  padding: 20px 0 7px;
}
```

Importez à la fois la feuille de style CSS et le CSS module que vous venez de créer dans votre fichier de script :

`App.js`

```javascript
import "../styles.css";
import codesweetlyStyles from "../styles.module.css";

function App() {
  return (
    <div className="imageInfo">
      <h1>Random Image</h1>
      <img src="https://picsum.photos/400/400" alt="Random Image" />
      <p>Get a new image each time you refresh your browser.</p>
    </div>
  );
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/3t3nwt?file=%2Fsrc%2FApp.js)

Allez-y, lancez votre application et vérifiez son résultat dans votre navigateur.

Après avoir lancé votre application, vous remarquerez que React n'a appliqué que la règle de la feuille de style CSS, et non celle du CSS module.

React a fait cela parce que la règle de la feuille de style est disponible globalement pour tous les éléments (et composants enfants) de la page où vous avez importé la feuille.

Mais la règle dans le module n'est disponible localement que pour le composant qui invoque explicitement la règle.

Ainsi, pour utiliser le style de votre CSS module dans votre composant, vous devez l'exécuter explicitement comme ceci :

`App.js`

```javascript
import "../styles.css";
import codesweetlyStyles from "../styles.module.css";

function App() {
  return (
    <div className={`imageInfo ${codesweetlyStyles.imageInfo}`}>
      <h1>Random Image</h1>
      <img src="https://picsum.photos/400/400" alt="Random Image" />
      <p>Get a new image each time you refresh your browser.</p>
    </div>
  );
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/45lkpf?file=%2Fsrc%2FApp.js)

L'extrait ci-dessus utilise le code `codesweetlyStyles.imageInfo` pour indiquer à React d'appliquer la règle `imageInfo` du CSS module à l'élément `div`.

#### 3. Composition

Pour composer des styles ensemble tout en utilisant une feuille de style CSS classique, vous devez appliquer plusieurs classes à votre élément.

**Exemple : Composer des règles avec des feuilles de style CSS classiques**

`styles.css`

```css
.container {
  border: 4px solid blueviolet;
  padding: 30px 15px;
}

.text {
  color: seagreen;
  font-weight: bold;
}
```

`App.js`

```javascript
import "../styles.css";

function App() {
  return <div className="container text">Oluwatobi is my name.</div>;
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/w6h74d?file=%2Fsrc%2FApp.js)

L'utilisation de plusieurs classes sur un élément pour implémenter la composition de styles n'est pas la meilleure pratique car le CSS utilisera l'ordre des définitions de style dans la feuille de style pour déterminer l'ordre de priorité basé sur les règles de cascade CSS.

Mais les CSS modules fournissent une déclaration `composes` qui offre une plus grande flexibilité dans la composition de vos styles pour répondre aux besoins de votre projet.

**Exemple : Composer des règles avec des CSS modules**

`styles.module.css`

```css
.container {
  border: 4px solid blueviolet;
  padding: 30px 15px;
}

.text {
  composes: container;
  color: seagreen;
  font-weight: bold;
}
```

`App.js`

```javascript
import styles from "../styles.module.css";

function App() {
  return <div className={styles.text}>Oluwatobi is my name.</div>;
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/j6yl9z?file=%2Fsrc%2FApp.js)

Bien que vous puissiez définir plusieurs déclarations `composes` dans une règle, elles doivent précéder les autres règles.

**Exemple : Toutes les déclarations** `composes` **doivent venir avant les autres règles**

`styles.module.css`

```css
.container {
  border: 4px solid blueviolet;
  padding: 30px 15px;
}

.curved {
  border-radius: 20px;
}

.text {
  composes: container;
  composes: curved;
  color: seagreen;
  font-weight: bold;
}
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/3lqshk?file=%2Fsrc%2Fstyles.module.css)

Vous pouvez simplifier la règle `.text` en utilisant une seule déclaration `composes` pour plusieurs classes.

**Exemple : Composer des classes avec une seule déclaration** `composes` 

`styles.module.css`

```css
.container {
  border: 4px solid blueviolet;
  padding: 30px 15px;
}

.curved {
  border-radius: 20px;
}

.text {
  composes: container curved;
  color: seagreen;
  font-weight: bold;
}
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/x4zfyn?file=%2Fsrc%2Fstyles.module.css)

### Comment utiliser une bibliothèque CSS-in-JS pour styliser les éléments React

Une bibliothèque CSS-in-JS vous permet d'utiliser toutes les fonctionnalités du CSS directement dans votre fichier JavaScript.

Certaines des bibliothèques CSS-in-JS les plus populaires sont Linaria, Emotion, Pigment CSS et Panda CSS.

N'hésitez pas à essayer la bibliothèque CSS-in-JS que vous préférez. Ici, nous utiliserons Emotion pour illustrer comment une telle technique de stylisme fonctionne dans une application React.

Alors, allez-y et installez la bibliothèque dans n'importe lequel de vos projets React en exécutant :

```console
npm i @emotion/react@11.14.0
```

Après avoir installé Emotion, importez-la et utilisez-la dans votre fichier de composant comme ceci :

`App.js`

```javascript
// Le commentaire ci-dessous est essentiel. Emotion ne fonctionnera pas sans lui.
/** @jsxImportSource @emotion/react */

// Définissez vos styles en utilisant la syntaxe d'objet JavaScript.
const codesweetlyStyles = {
  border: "8px ridge #71380f",
  backgroundColor: "#ffe5b4",
  padding: "20px 0 7px",
  textAlign: "center",
  color: "maroon",
  "@media(min-width: 768px)": {
    color: "darkslategray",
  },
};

// Appliquez les styles à votre élément.
function App() {
  return (
    <div css={codesweetlyStyles}>
      <h1>Random Image</h1>
      <img src="https://picsum.photos/400/400" alt="Random Image" />
      <p>Get a new image each time you refresh your browser.</p>
    </div>
  );
}

export default App;
```

[**Essayer sur CodeSandbox**](https://codesandbox.io/p/sandbox/t4ttkx?file=%2Fsrc%2FApp.js)

L'extrait ci-dessus fait ce qui suit :

1. Utilise le commentaire `/** @jsxImportSource @emotion/react */` (JSX Pragma) pour indiquer au plugin Babel JSX de convertir les appels JSX du script en une fonction Emotion appelée `jsx` au lieu de `React.createElement`. Assurez-vous de placer la directive pragma au-dessus de vos instructions d'importation. Sinon, la bibliothèque Emotion ne fonctionnera pas.
    
2. Définit les styles dans un objet JavaScript.
    
3. Utilise la fonctionnalité de prop `css` d'Emotion pour appliquer les styles à l'élément JSX.
    

Remarquez que la prop `css` est comme l'attribut `style` en ligne. La principale différence est que les props `css` prennent en charge davantage de fonctionnalités CSS telles que les sélecteurs imbriqués, le préfixage automatique des fournisseurs, les media queries et les états d'événements (tels que `hover`, `focus` et `active`). Ainsi, l'utilisation de bibliothèques CSS-in-JS comme Emotion vous permet d'écrire des styles hautement flexibles et réactifs directement dans vos fichiers JavaScript.

**Conseil :** La prop `css` fonctionne sur n'importe quel élément qui prend en charge l'attribut `className`.

Maintenant, allez-y, lancez votre application et vérifiez son résultat dans votre navigateur.

Et voilà ! Vous savez maintenant comment utiliser une bibliothèque CSS-in-JS pour styliser vos éléments React.

J'ai utilisé Emotion dans cet article parce que j'aime la clarté de sa syntaxe. N'hésitez pas à tester d'autres bibliothèques CSS-in-JS, telles que Pigment CSS. Vous en trouverez peut-être une qui vous convient mieux.

## Aperçu

Dans ce guide, nous avons discuté des concepts fondamentaux que vous devez connaître pour commencer à construire des applications avec React. Nous avons également utilisé des exemples pour nous entraîner à créer et à styliser des composants.

Que vous envisagiez un petit projet personnel ou une application full-stack pour une base d'utilisateurs plus large, vous avez maintenant les bases pour construire ces projets en utilisant React.

Merci de m'avoir lu !

### Approfondir React

Ce guide vous a donné un aperçu de mon livre [Code React Sweetly](https://www.amazon.com/dp/B0FRC4R8T3?tag=codesweetly00-20). Que vous débutiez ou que vous souhaitiez affiner vos fondamentaux, le livre vous guide à travers tout, des concepts essentiels au déploiement d'applications réelles utilisant JavaScript et TypeScript. Il est pratique, adapté aux débutants et conçu pour vous aider à coder React avec plaisir !

[![Un guide du débutant pour React : Apprenez JSX, les Hooks et le développement d'applications réelles](https://cdn.hashnode.com/res/hashnode/image/upload/v1760698961658/f3f297da-1cd2-4777-b440-19b94daaa26f.jpeg align="center")](https://www.amazon.com/dp/B0FRC4R8T3?tag=codesweetly00-20)