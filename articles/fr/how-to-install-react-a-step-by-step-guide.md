---
title: Comment installer React – Un guide étape par étape
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2024-02-05T12:43:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-install-react-a-step-by-step-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/solid-navy-blue-concrete-textured-wall.png
tags:
- name: beginners guide
  slug: beginners-guide
- name: React
  slug: react
seo_title: Comment installer React – Un guide étape par étape
seo_desc: 'React is an open-source JavaScript library that helps you build dynamic
  user interfaces (UIs). You can use it to build components that represent logically
  reusable parts of the UI.

  Because React is open source, anyone can access its source code, insp...'
---

React est une bibliothèque JavaScript open-source qui vous aide à construire des interfaces utilisateur (UI) dynamiques. Vous pouvez l'utiliser pour construire des composants qui représentent des parties logiquement réutilisables de l'UI.

Parce que React est open-source, n'importe qui peut accéder à son code source, l'inspecter, le modifier et l'améliorer pour ses besoins personnels ou les exigences de développement d'applications.

Dans ce tutoriel, vous apprendrez comment installer React dans votre projet.

## Comment installer React

Maintenant que vous savez ce qu'est React et pourquoi il est utile, vous apprendrez comment utiliser cette bibliothèque dans votre projet.

### Étape 1 : Installer Node.js

Avant de commencer le processus d'installation de React, vous devez avoir Node.js installé sur votre ordinateur. Si vous ne savez pas ce qu'est Node.js, vous pouvez en lire plus [ici](https://www.freecodecamp.org/news/what-is-node-js/).

Vous devez d'abord installer Node car React.js est une bibliothèque JavaScript, et Node.js est un environnement d'exécution JavaScript qui vous permet d'exécuter JavaScript côté serveur. Ainsi, lorsque vous écrivez du React, vous incluez des fonctions JavaScript dans votre projet React, et Node.js aide à exécuter ce code JavaScript sur la page web.

Node.js a diverses versions. La version recommandée est la dernière version stable, car elle contient des changements majeurs et significatifs. Ces changements incluent des corrections de bugs et des mises à jour de sécurité, la compatibilité avec les dépendances de votre projet, et ainsi de suite.

Pour installer Node, rendez-vous sur le [site web de Node.js](https://nodejs.org/en/). Sur leur page web, vous avez la possibilité de télécharger soit la version recommandée, soit la version actuelle, comme le montre l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Node.js.png align="left")

*Interface de la page web de Node.js*

Après avoir téléchargé la version de votre choix, installez-la sur votre ordinateur.

Une fois l'installation terminée, ouvrez votre invite de commande pour confirmer que Node a été installé avec succès. Tapez `node -v` dans votre invite de commande, puis cliquez sur le bouton Entrée. Cette commande doit afficher la version actuelle de Node installée sur votre ordinateur.

Voici à quoi cela ressemble :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/node-version-1.png align="left")

*Version de Node affichée dans l'invite de commande*

Si la version de votre Node est affichée comme ci-dessus, félicitations ! Vous avez installé Node.js avec succès sur votre ordinateur.

### Étape 2 : Installer React

Maintenant, vous pouvez procéder à l'installation de React dans votre projet. Passons ensemble par les étapes.

Tout d'abord, nous allons voir la méthode "traditionnelle" d'installation de React, en utilisant create-react-app (CRA), afin que vous soyez conscient de ce processus. Ensuite, nous verrons comment l'installer en utilisant l'outil de construction moderne Vite.

#### Utilisation de CRA

Toujours dans votre fenêtre d'invite de commande, naviguez jusqu'au répertoire que vous souhaitez utiliser pour créer votre projet React. Pour ce faire, tapez `cd [nom du répertoire]` puis cliquez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Screenshot-1_30_2024-9_53_23-AM.png align="left")

Commande `cd documents` pour aller dans le répertoire `documents`

Comme vous pouvez le voir dans l'image ci-dessus, je navigue vers le répertoire `documents`, qui est l'endroit où je souhaite créer mon projet React.

Dans le répertoire `documents` (ou là où vous créez votre projet), créez un dossier que vous utiliserez pour créer votre application React. Tapez `mkdir [nom du dossier]` puis naviguez jusqu'au répertoire nouvellement créé en utilisant `cd [nom du dossier nouvellement créé]`.

Dans le répertoire du dossier nouvellement créé, tapez `npx create-react-app [nom de projet de votre choix]`, puis attendez que votre projet React soit complètement créé. La dernière section doit avoir le texte de l'image ci-dessous affiché :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/React-project-2-1.png align="left")

*Installation complète de React dans le terminal*

Enfin, ouvrez le projet React dans votre éditeur de code en tapant `code .`. Votre éditeur de code (si vous utilisez VS code) devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/01/Welcome---reactproject---Visual-Studio-Code-1_30_2024-8_39_40-PM.png align="left")

*Affichage de l'installation complète de React en utilisant CRA*

Dans l'image ci-dessus, passons en revue certains des éléments que vous y verrez.

* Le dossier `node module` est un dossier de stockage qui contient votre package React ainsi que d'autres packages qui peuvent être installés lorsque vous travaillez sur votre projet React. Le `node module` aide à configurer le système de design de votre projet React.

* Le dossier `src` stocke tous les fichiers et composants utilisés dans votre application React, allant de `App.js`, `index.js`, `App.css` comme on le voit dans l'image ci-dessus.

* Le fichier `package-lock.json` verrouille les versions des dépendances que votre projet React utilise, et cela aide à gérer les dépendances dans votre projet React.

Récemment, create-react-app est devenu obsolète et l'équipe React ne recommande plus de l'utiliser. D'autres outils modernes offrent une expérience de développement front-end plus rapide, et vous pouvez les utiliser pour créer des applications React sans stress. De tels outils incluent Vite, Snowpack, Gatsby, Next.js, Percel, et ainsi de suite.

Dans cette section, vous apprendrez comment utiliser l'outil Vite pour installer React dans votre projet.

#### Utilisation de Vite

Vite est un outil moderne très rapide et personnalisable qui vise à fournir une expérience de développement linéaire pour les projets web modernes. Vous pouvez l'utiliser pour créer vos applications React de manière rapide et fiable. Il possède également les mêmes fonctionnalités que create-react-app (CRA).

Tout comme nous l'avons fait lors de l'installation de React en utilisant CRA, la première étape consiste à s'assurer que vous avez Node installé sur votre ordinateur. Après cela, naviguez jusqu'au répertoire que vous souhaitez utiliser et créez un nouveau dossier (avec le nom de votre choix).

Ouvrez le dossier nouvellement créé dans votre éditeur de code (VS code).

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-8_10_22-AM.png align="left")

*Vite_React*

L'image ci-dessus est ce à quoi la vôtre devrait ressembler. Dans mon cas, j'ai nommé le dossier que j'ai créé `Vite_React`.

L'étape suivante consiste à ouvrir le terminal (situé entre Exécuter et Aide), comme le montre l'image ci-dessus.

Une fois dans le terminal, exécutez `npm create vite@latest [nom de votre projet]`. Dans mon cas, le nom du projet que j'ai utilisé est `new-react-vite`. La commande ci-dessus devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-8_30_00-AM.png align="left")

*Sélectionner le Framework (React)*

À ce stade, on vous demande de sélectionner le framework que vous souhaitez installer, alors puisque vous travaillez sur React, utilisez les touches fléchées pour naviguer jusqu'à React, puis cliquez sur Entrée.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-8_36_40-AM.png align="left")

*Sélectionner le langage (JavaScript)*

D'après l'image ci-dessus, l'étape suivante consiste à sélectionner le langage que vous souhaitez pour votre projet. Vous pouvez choisir n'importe quel langage de votre choix, mais pour les besoins de ce tutoriel, j'ai choisi JavaScript.

L'étape suivante consiste à naviguer jusqu'au répertoire du projet où vous avez créé le projet React. Pour ce faire, tapez `cd [nom du répertoire]`. Le vôtre devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-8_44_16-AM.png align="left")

*Installation complète de React en utilisant Vite*

Une fois que vous avez fait cela, vous devriez voir que vos fichiers React ont été créés et affichés à l'écran comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-8_49_58-AM.png align="left")

*Affichage de l'installation de React*

Enfin, mais non des moindres, installez le dossier du module Node en tapant `npm install` dans le terminal. Cela prend un peu de temps pour se terminer, mais une fois l'installation terminée, vous devriez voir le dossier `node_module` en haut, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite_React---Visual-Studio-Code-2_2_2024-9_02_48-AM.png align="left")

*Dossier Node Modules*

Enfin, tapez `npm run dev` pour exécuter votre projet et l'afficher sur la page web. Si vous avez suivi les étapes d'installation correctement, vous devriez voir votre hôte local :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/vite.config.js---Vite_React---Visual-Studio-Code-2_2_2024-9_11_55-AM.png align="left")

*Hôte local*

Maintenez votre bouton de contrôle enfoncé et cliquez sur votre hôte local. Cela vous amène à la page web. À ce stade, si votre page web est affichée comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Vite---React---Google-Chrome-2_2_2024-9_16_47-AM.png align="left")

*Affichage final de React sur la page web*

Félicitations pour avoir installé React sur votre projet !

## Conclusion

La bibliothèque React est un outil JavaScript open-source puissant que vous pouvez utiliser pour créer des applications dynamiques et attrayantes. C'est en fait un framework amusant à utiliser, donc je vous recommande de l'essayer.

Je crois qu'à ce stade, vous pouvez installer complètement React dans votre projet avec l'outil moderne (comme Vite). Si vous l'avez fait, félicitations encore une fois !

Bon codage !