---
title: 'Tutoriel d''extension Chrome : Comment passer des messages depuis le contexte
  d''une page'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-02-24T02:14:59.000Z'
originalURL: https://freecodecamp.org/news/chrome-extension-message-passing-essentials
coverImage: https://www.freecodecamp.org/news/content/images/2021/02/DDF5E684-AEF5-45E6-9421-E5D4360E9A85-1.jpg
tags:
- name: Google Chrome
  slug: chrome
- name: chrome extension
  slug: chrome-extension
- name: JavaScript
  slug: javascript
- name: messaging
  slug: messaging
seo_title: 'Tutoriel d''extension Chrome : Comment passer des messages depuis le contexte
  d''une page'
seo_desc: "By Tarique Ejaz\nIn the world of web development, Chrome extensions are\
  \ a pretty handy set of tools to have around. \nWhether you use them to add headers\
  \ to simple requests or to scrape important data from the DOM, extensions help provide\
  \ extra functio..."
---

Par Tarique Ejaz

Dans le monde du développement web, les extensions Chrome sont un ensemble d'outils assez pratiques à avoir sous la main. 

Que vous les utilisiez pour ajouter des en-têtes à des requêtes simples ou pour extraire des données importantes du DOM, les extensions aident à fournir une fonctionnalité supplémentaire qui facilite la vie.

J'ai commencé à m'amuser à développer une extension Chrome pour un cas d'utilisation que j'avais en tête au travail. C'est alors que je suis tombé sur la manière dont nous passons certaines données d'une page web à une extension. Et le manque de guide simplifié m'a incité à écrire cet article. 

Nous avons bien la [documentation de l'API Chrome](https://developer.chrome.com/docs/extensions/reference/), et elle est effectivement très complète. Mais je me considère comme un apprenant plus visuel, et pouvoir visualiser comment nous passons des messages entre les scripts d'extension a aidé à simplifier le développement global.

> **Note :** Cet article utilise Manifest V2 au lieu de V3. La principale différence entre les deux est l'utilisation de service workers dans V3 au lieu de pages d'arrière-plan et d'actions associées. 

## Passage de messages : Interaction entre les scripts

Une extension, comme son nom l'indique, est comme une couche au-dessus de la page web existante que vous essayez d'accéder. Le navigateur agit comme le conteneur.

Elle comprend principalement les scripts suivants :

* **Script Popup** - Fichier JavaScript local pour le DOM de l'extension
* **Script d'arrière-plan** - Fournit la persistance et gère les événements d'arrière-plan
* **Script de contenu** - Scripts qui s'exécutent en isolation dans le contexte de la page web
* **Script injecté** - Scripts qui sont injectés par programmation dans la page web 

Normalement, si vous devez simplement traiter le contenu du DOM, alors la manière dont l'extension est développée est relativement simple. 

Le HTML brut est déjà disponible pour le script de contenu et tout ce que vous avez à faire est de le passer au script popup. 

Cependant, si vous devez accéder aux variables et fonctions de la page, le processus devient un peu plus compliqué.

Les variables et fonctions disponibles dans le contexte de la page, par exemple dans l'objet `window`, ne sont pas accessibles aux scripts de contenu puisqu'ils tendent à s'exécuter dans un environnement JavaScript spécial. Ils ont accès uniquement au DOM de la page mais pas aux variables et fonctions. 

Pour accéder aux variables et fonctions d'une page, nous injectons des scripts en les ajoutant au DOM. Cela fait que le navigateur suppose qu'il s'exécute dans le contexte de la page web. Cela fournit à son tour au script injecté l'accès aux variables et fonctions locales.

Puisque les extensions Chrome sont basées sur des événements en raison de leur architecture, une fois que les scripts injectés ont accès aux variables et fonctions de la page, ils peuvent les passer au script de contenu. 

Le script de contenu passe ensuite ces objets à la page d'arrière-plan. 

Et enfin, le script popup est capable d'appeler la page d'arrière-plan en utilisant l'API d'extension et de la passer au DOM de l'extension. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/flowchart.png)
_Aperçu du passage de messages_

Maintenant, nous allons construire une simple extension Performance Watcher qui lit les données de performance depuis l'objet window global d'une page et mappe les métriques essentielles pour que l'utilisateur puisse les voir. Passons au code alors.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/extn.PNG)

## Assez parlé, montrez-moi le code

Vous pouvez trouver le dépôt de code complet pour le projet [ici](https://github.com/tejazz/article-snippets/tree/master/chrome-extn-message-passing). Passons rapidement en revue les fichiers principaux et les fonctionnalités importantes qu'ils offrent.

### Le fichier Manifest

Chaque extension Chrome a besoin d'un fichier `manifest`. Il s'agit essentiellement d'un fichier au format JSON qui fournit un ensemble de métadonnées afin que le navigateur puisse reconnaître les permissions qui doivent être accordées et la portée opérationnelle probable de l'extension. 

Voici le manifest utilisé pour notre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/manifest.png)
_manifest.json : métadonnées pour votre extension_

Certaines des propriétés importantes sur lesquelles nous devons nous concentrer sont les suivantes :

* `background` - Prend un tableau de scripts qui seraient exécutés dans la page d'arrière-plan. 
* `content-scripts` - Inclut un tableau de scripts de contenu que nous souhaitons exécuter dans le contexte de la page web. 
* `web_accessible_resources` - Un tableau de ressources packagées destinées à être utilisées dans le contexte d'une page web. Par exemple, une image que nous avons l'intention d'intégrer dans une page ou un script personnalisé que nous voulons injecter.
* `permissions` - Permet à votre extension d'obtenir l'accès à certaines API Chrome comme [tabs](https://developer.chrome.com/docs/extensions/reference/tabs/#type-Tab) dans ce cas. 

### Le script de contenu

Les scripts de contenu ont un accès facile au DOM de la page web. Nous utilisons le script de contenu pour ajouter notre script personnalisé – `inject-script.js` – dans le DOM.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/content-inject.png)
_content-script.js : injecter un script personnalisé dans le DOM_

Le script de contenu continue également simultanément à écouter tout message envoyé en amont depuis le script personnalisé. 

Dès que nous recevons un message du script injecté, nous effectuons une vérification rapide des données reçues et vérifions si notre extension est installée. Une fois cela fait, nous utilisons simplement l'[API Runtime](https://developer.chrome.com/docs/extensions/reference/runtime/) de Chrome pour envoyer les données reçues vers la page d'arrière-plan. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/content-send.png)
_content-script.js : envoyer les données requises à la page d'arrière-plan_

### Le script injecté

Le script personnalisé peut accéder aux variables et fonctions globales comme l'objet `window`. Nous mappons uniquement les propriétés dont nous avons besoin. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/inject-action.png)
_inject-script.js : obtenir l'objet requis depuis le contexte JS de la page_

Le message du script personnalisé est communiqué en toute sécurité au script de contenu en utilisant la fonction `[window.postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage)`. Dans ce cas, une fonction `setInterval` est utilisée pour mettre à jour dynamiquement les propriétés que nous observons.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/inject-send.png)
_inject-script.js : envoyer les données collectées au script de contenu_

### Le script d'arrière-plan

Le script d'arrière-plan écoute tout message transmis par le script de contenu en utilisant l'API Runtime. L'objet `window` de la page d'arrière-plan est ensuite mis à jour avec `tab.id` agissant comme identifiant. 

![Image](https://www.freecodecamp.org/news/content/images/2021/02/background.png)
_background.js : écouter le message entrant du script de contenu_

### Le script Popup

Le script popup est l'endroit où nous lisons enfin les données que nous avons obtenues de notre script personnalisé. C'est aussi l'endroit où nous codons les opérations JavaScript nécessaires.

La page d'arrière-plan est récupérée en utilisant la méthode `getBackgroundPage` de l'API d'extension. L'ID de l'onglet actif est interrogé en utilisant la méthode `tabs.query` de l'API Tabs afin d'extraire correctement les données pertinentes.

![Image](https://www.freecodecamp.org/news/content/images/2021/02/popup.png)
_popup.js : lecture de l'objet global stocké dans le contexte de la page d'arrière-plan_

De cette manière, nous sommes enfin en mesure de recevoir et de mapper les données dont nous avons besoin – `performance` dans notre cas – efficacement dans notre extension.

Le code de style de l'interface utilisateur et autres codes cosmétiques sont disponibles dans le dépôt, pour référence supplémentaire.

## Réflexions finales

Le passage de messages est un concept essentiel lorsqu'il s'agit de développer une extension Chrome. Ce n'est qu'une des multiples façons dont vous pouvez communiquer entre les scripts. 

J'ai passé quelques heures pour comprendre comment cela fonctionnerait pour mon cas d'utilisation. Espérons que ce simple guide et la représentation visuelle vous fassent gagner du temps. 

Je vous suggère de jouer un peu avec le code. Si vous avez des questions, n'hésitez pas à me contacter sur `[LinkedIn](https://www.linkedin.com/in/tarique-ejaz/)`.

En attendant, continuez à coder.