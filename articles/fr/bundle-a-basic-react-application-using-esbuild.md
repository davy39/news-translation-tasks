---
title: Comment regrouper une application React simple en utilisant esbuild
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-08-22T20:56:13.000Z'
originalURL: https://freecodecamp.org/news/bundle-a-basic-react-application-using-esbuild
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Screenshot-from-2023-08-21-16-04-04.png
tags:
- name: Bundler
  slug: bundler
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: web performance
  slug: web-performance
seo_title: Comment regrouper une application React simple en utilisant esbuild
seo_desc: Bundling is an important phase in the web development process, particularly
  when dealing with JavaScript frameworks like React. It entails combining all the
  various JavaScript files and dependencies into a single file for faster browser
  loading and e...
---

Le regroupement est une phase importante dans le processus de développement web, en particulier lors de l'utilisation de frameworks JavaScript comme React. Cela implique de combiner tous les différents fichiers JavaScript et dépendances en un seul fichier pour un chargement et une exécution plus rapides dans le navigateur. 

esbuild est un bundler léger et efficace pour les applications React. Voici un aperçu de la manière d'utiliser esbuild pour regrouper une application React de base.

## Comment installer esbuild globalement

Nous allons commencer par installer esbuild globalement dans votre système en exécutant `npm install -g esbuild` dans la ligne de commande. Cela installera la dernière version d'esbuild globalement sur votre système. 

Après l'installation, vous pouvez accéder à esbuild depuis la ligne de commande en tapant `esbuild`.

## Comment créer un nouveau répertoire pour votre application React

Pour créer un nouveau répertoire pour votre application React, ouvrez le terminal et naviguez jusqu'au répertoire où vous souhaitez créer le nouveau répertoire. Ensuite, exécutez la commande suivante :

```bash
mkdir my-react-app
```

Cela créera un nouveau répertoire nommé `my-react-app`. Vous pouvez le remplacer par le nom que vous souhaitez donner à votre répertoire d'application React.

Après avoir créé le répertoire, naviguez dedans en exécutant :

```bash
cd my-react-app
```

Initialisez un nouveau projet `npm` en exécutant la commande suivante et en suivant les invites :

```bash
npm init -y
```

Installez React et React DOM en exécutant `npm install react react-dom` dans le terminal. Cela installera les dernières versions de React et React DOM dans votre projet, ainsi que toutes les dépendances requises.

## Comment créer les fichiers et dossiers nécessaires

Créons les fichiers et dossiers nécessaires. Voici une structure de base :

```
my-react-app
├── src
|   |
│   ├── index.js
├── index.html
│  
└── package.json

```

  
Ajoutez le code montré ci-dessous dans votre application, en suivant la structure ci-dessus :

**index.html** :

```html
<!DOCTYPE html>
<html>

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>Bonjour, esbuild !</title>
</head>

<body>
  <div id="root"></div>
  <script src="Bundle.js"></script>
</body>

</html
```

Le code ci-dessus décrit la structure fondamentale d'une page web HTML5. Il commence par une déclaration indiquant l'utilisation de HTML5. La structure principale se compose d'un élément racine `<html>` contenant une section `<head>` pour les métadonnées, y compris le codage des caractères et les paramètres de la fenêtre d'affichage pour la réactivité.

L'élément `<title>` définit le titre de l'onglet du navigateur, tandis que le contenu réel réside dans l'élément `<body>`. Dans le `<body>`, un élément `<div>` avec l'id "root" sert de placeholder pour un contenu dynamique potentiel. 

De plus, il y a une balise `<script>` pointant vers un fichier JavaScript externe nommé "Bundle.js", généré par esbuild, à exécuter par le navigateur. 

Cette structure pose les bases pour construire une page web avec des fonctionnalités HTML5, CSS et JavaScript.

**index.js**

```jsx
import React from "react";
import ReactDOM from "react-dom";

function App() {
  return (
    <div>Bonjour, esbuild ! </div>
  );
}

ReactDOM.render(<App />, document.getElementById("root"));
```

Notre code React configure une application React simple avec un seul composant App. Il rend un élément `<div>` avec le texte `Bonjour, esbuild !` et le monte dans le DOM, spécifiquement dans l'élément avec l'`id` de `root`.

## Comment créer la fonction de build

Ajoutons le script de build suivant en utilisant le bundler `esbuild` dans notre fichier `package.json` :

```json
"scripts": {
        "build": "esbuild src/index.js --bundle --outfile=Bundle.js --loader:.js=jsx --format=cjs"
},

```

Ce script de build commence avec le point d'entrée `src/index.js` et procède au regroupement de toutes les dépendances. Le code regroupé résultant est enregistré sous `Bundle.js`. 

Le script spécifie également que les fichiers avec l'extension `.js` doivent être traités comme des fichiers `jsx`, indiquant l'utilisation de la syntaxe JSX.

Enfin, le format de sortie est défini sur `CommonJS (cjs)` qui est le système de modules utilisé par Node.js. 

En exécutant ce script de build, le bundler `esbuild` traitera les fichiers, appliquera les transformations nécessaires et générera un seul fichier JavaScript regroupé prêt pour le déploiement ou une utilisation ultérieure.

### Aperçu de la fonction de build et de son objectif

Le script de build utilisant esbuild est un code JavaScript qui regroupe votre code JavaScript en un seul fichier. Cela est utile pour optimiser votre code pour les environnements de production, réduire le nombre de requêtes HTTP nécessaires pour charger votre application et améliorer les temps de chargement.

La méthode de build prend un objet `options` comme argument, ce qui vous permet de configurer la manière dont votre code est regroupé. L'objet options spécifie des propriétés telles que `entryPoints`, `outfile`, `format`, `bundle` et `loader`.

Une fois la méthode de build configurée avec les options souhaitées, la fonction de build est appelée, ce qui déclenche le processus de build. Cela générera un seul fichier regroupé contenant tout votre code JavaScript.

Enfin, le script de build est exécuté en exécutant le script en utilisant Node.js. Vous pouvez le faire en mettant à jour le fichier `package.json` pour inclure un script qui exécute le script de build, comme montré ci-dessus.

Construisez l'application React en utilisant la commande suivante :

```bash
npm run build
```

  
Ensuite, exécutez l'application en utilisant cette commande :

```bash
npx http-server
```

## Conclusion

En suivant ces étapes, vous pouvez regrouper votre application React de base en utilisant esbuild et la préparer pour le déploiement ou une utilisation ultérieure. Voici la [démo](https://github.com/gatwirival/esbuild-bundling-demo.git).

Bon codage !