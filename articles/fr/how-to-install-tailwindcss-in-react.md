---
title: Comment installer React et Tailwind CSS avec Vite dans un projet
subtitle: ''
author: Segun Ajibola
co_authors: []
series: null
date: '2023-01-09T18:49:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-tailwindcss-in-react
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Parameters-vs-Arguments--1-.png
tags:
- name: CSS
  slug: css
- name: React
  slug: react
- name: tailwind
  slug: tailwind
- name: vite
  slug: vite
seo_title: Comment installer React et Tailwind CSS avec Vite dans un projet
seo_desc: 'Tailwind CSS is a popular CSS framework, and React is one of the most popular
  JavaScript libraries.

  And Tailwind CSS and React are a great combo to use if you''re building a frontend
  project.

  In this article, you will learn how to setup your coding en...'
---

Tailwind CSS est un framework CSS populaire, et React est l'une des bibliothèques JavaScript les plus populaires.

Et Tailwind CSS et React sont une excellente combinaison à utiliser si vous construisez un projet frontend.

Dans cet article, vous apprendrez comment configurer votre environnement de codage avec Vite, installer React et Tailwind CSS avec leurs dernières versions, et commencer à construire vos projets immédiatement.

Nous utiliserons ces outils :

* [VSCode](https://code.visualstudio.com/download) pour notre éditeur de code
* [Node.js](https://nodejs.org/en/download/) pour notre gestionnaire de paquets
* [Vite](https://vitejs.dev/) pour notre environnement de développement

Si vous n'avez pas ces outils installés, vous pouvez le faire en cliquant sur les liens pour chacun d'eux ci-dessus.

Après avoir configuré Node.js pour votre VSCode, vous pouvez maintenant utiliser Node.js pour installer Vite pour votre projet en utilisant le terminal.

## Étape 1 – Créer votre dossier de projet

Ouvrez votre terminal et naviguez vers le dossier où vous souhaitez construire votre projet – par exemple, le Bureau. Saisissez la commande ci-dessous dans le terminal et cliquez sur `entrée` :

```node.js
npm create vite@latest votre-nom-de-projet -- --template react
```

La commande ci-dessus créera votre dossier de projet.

![Mon nom de projet est "food-app", le dossier food-app sera créé dans le dossier Programming sur mon Bureau](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-03-000708.png)
_Mon nom de projet est "food-app", le dossier food-app sera créé dans le dossier Programming sur mon Bureau_

Notez que nous avons utilisé `-- --template react` pour spécifier que nous construisons une application React avec Vite.

## Étape 2 – Naviguer vers votre dossier de projet

Saisissez la commande ci-dessous dans votre terminal et cliquez sur `entrée` :

```shell
cd food-app
```

Cette commande vous amènera à votre dossier de projet. Vous devriez avoir ceci :

![Saisie de "cd food-app" dans le terminal pour naviguer vers le dossier "food-app"](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-03-001414.png)
_Saisie de "cd food-app" dans le terminal pour naviguer vers le dossier "food-app"_

## **Étape 3 – Installer Tailwind CSS et autres dépendances**

Saisissez la commande ci-dessous dans votre terminal et cliquez sur `entrée` :

```node
npm install -D tailwindcss postcss autoprefixer
```

Cette commande installera les éléments suivants :

* Le framework Tailwind CSS
* Post CSS, qui fournit des plugins pour effectuer différentes fonctionnalités comme les préfixes en CSS Vanilla
* Autoprefixer, qui est un plugin PostCSS pour analyser le CSS et ajouter des préfixes de fournisseurs aux règles CSS.

Votre dossier devrait ressembler à ceci dans votre VSCode :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-03-004354.png)

Confirmez que vous avez le texte suivant dans votre `package.json` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-03-004416.png)
_<div id="ember183" class="miw-100 tc bn form-text bg-transparent pr8 pl8 ember-view" data-kg-has-link-toolbar="true" data-koenig-dnd-disabled="true" style="box-sizing: border-box; padding-right: 3.2rem; padding-left: 3.2rem; border-style: none; border-width: 0px; transition: border-color 0.15s linear 0s; appearance: none; outline: none; min-width: 100%; background-color: transparent !important; text-align: center;"><div class="koenig-basic-html-input__editor-wrappper" style="box-sizing: border-box; cursor: text;"><div class="koenig-basic-html-input__editor __mobiledoc-editor" data-gramm="false" data-kg="editor" data-kg-allow-clickthrough="" data-placeholder="Type caption for image (optional)" spellcheck="true" contenteditable="true" style="box-sizing: border-box; position: relative; resize: none; min-height: 1em;"><p style="box-sizing: border-box; margin: 0px; position: relative; min-width: 100%; max-width: 100%; font-family: inherit; font-weight: inherit; line-height: inherit; font-size: inherit; letter-spacing: inherit;">Remarquez les dépendances autoprefixer, postcss et tailwindcss des lignes 19 à 21. Le numéro de version peut avoir changé lorsque vous lisez ceci.</p></div></div></div>_

## Étape 4 – Générer les fichiers de configuration

Saisissez la commande ci-dessous dans votre terminal et cliquez sur `entrée` :

```node
npx tailwindcss init -p
```

Cette commande génère les fichiers de configuration `tailwind.config.cjs` et `postcss.config.cjs`, également connus sous le nom de fichiers config. Ils vous aident à interagir avec votre projet et à tout personnaliser.

## Étape 5 – Configurer les chemins sources

Ajoutez les chemins vers tous vos fichiers de modèle dans votre fichier `tailwind.config.cjs`. Les fichiers de modèle incluent les modèles HTML, les composants JavaScript et autres fichiers sources qui contiennent des noms de classes Tailwind. Cela permet de s'assurer que le CSS vanilla est généré pour les éléments correspondants.

Votre fichier `tailwind.config.cjs` ressemble à ceci pour l'instant :

![Fichier de configuration actuel nommé tailwind.config.cjs, il contient l'objet module.export pour personnaliser tailwind avec des propriétés comme content, theme et plugins](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-03-235907.png)
_Fichier de configuration actuel nommé tailwind.config.cjs, il contient l'objet module.export pour personnaliser tailwind avec des propriétés comme content, theme et plugins_

Ajoutez ceci dans votre section content.

```json
"./index.html",


"./src/**/*.{js,ts,jsx,tsx}",
```

Votre fichier devrait maintenant ressembler à ceci :

![Fichier de configuration après la mise à jour de la propriété content](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-000648.png)
_Fichier de configuration après la mise à jour de la propriété content_

## **Étape 6 – Ajouter les directives Tailwind à votre CSS**

Les directives Tailwind sont des instructions spécifiques à Tailwind qui indiquent au CSS comment se comporter. Vous devrez ajouter des directives pour trois des couches de Tailwind.

`@tailwind base` injecte les styles de base de Tailwind et les styles de base enregistrés par les plugins, `@tailwind components` injecte les classes de composants de Tailwind et les classes de composants enregistrées par les plugins, tandis que `@tailwind utilities` injecte les classes utilitaires de Tailwind et les classes utilitaires enregistrées par les plugins.

Ajoutez les instructions ci-dessous à votre fichier `./src/index.css` :

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```

Votre fichier `index.css` contient certains styles par défaut. Vous pouvez tout effacer et coller les trois lignes de directives ci-dessus.

## Étape 7 – Démarrer votre serveur Vite

Exécutez votre processus de construction avec la commande `npm run dev` dans le terminal. Vous devriez obtenir le message ci-dessous dans votre terminal :

![Le message que vous obtenez après avoir exécuté votre serveur Vite qui fournit le lien localhost, le réseau et l'aide.](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-005534.png)
_Le message que vous obtenez après avoir exécuté votre serveur Vite qui fournit le lien localhost, le réseau et l'aide._

Maintenez la touche `ctrl` enfoncée et cliquez sur le lien Local – ici, c'est http://127.0.0.1:5174. Cela ouvrira un nouvel onglet dans votre navigateur si vous le faites.

![Capture d'écran de la page web au premier lancement](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-005850.png)
_Capture d'écran de la page web au premier lancement_

Nos styles sont cassés car nous avons effacé le CSS par défaut dans le fichier `index.css` pour y insérer nos directives.

## Étape 8 – Commencer à écrire du Tailwind CSS

Vous pouvez commencer à utiliser les classes utilitaires de Tailwind pour styliser votre contenu. Naviguez vers votre fichier `App.jsx`, où vous devriez voir ceci :

![Capture d'écran du fichier App.jsx](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-184158.png)
_Capture d'écran du fichier App.jsx_

Effacez l'élément return à partir de la ligne 9 et remplacez-le par le texte ci-dessous pour tester votre Tailwind et savoir s'il fonctionne. Saisissez ceci :

```jsx
<h1 className="text-3xl font-bold underline text-center">Bonjour le monde !</h1> 
```

Maintenant, vous avez ceci :

![Ajout de l'élément h1 au fichier App.jsx avec les styles tailwindcss appliqués](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-184804.png)
_Ajout de l'élément h1 au fichier App.jsx_

Selon l'image ci-dessus, `text-3xl font-bold text-red-500 underline text-center` a été ajouté en tant que className à l'élément `div`. C'est la norme pour écrire le style Tailwind CSS.

Vous pouvez en apprendre plus sur les noms de classes Tailwind [ici](https://tailwindcss.com/docs/). Votre navigateur devrait se mettre à jour automatiquement.

![Capture d'écran de la page web après l'ajout de l'élément h1, montrant Bonjour le monde avec les styles CSS tailwind appliqués.](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-04-184720.png)
_Capture d'écran de la page web après l'ajout de l'élément h1_

Vous pouvez maintenant commencer à construire vos projets React et les styliser avec Tailwind CSS.

## **Conclusion**

Vous avez maintenant créé une application React et Tailwind CSS en utilisant Vite, un outil de construction frontend. Vous avez appris ce qu'est Vite et comment créer une application Vite avec un modèle React, ainsi que comment installer Tailwind et autres dépendances.

Merci d'avoir lu cet article. Si vous l'avez apprécié, envisagez de le partager pour aider d'autres développeurs.

Vous pouvez me joindre sur [Twitter](https://twitter.com/iamsegunajibola), [LinkedIn](https://www.linkedin.com/in/segunajibola/) et [GitHub](https://github.com/segunajibola).

Bon apprentissage.