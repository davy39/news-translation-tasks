---
title: Comment exécuter des tests de régression visuelle sur une application Next.js
  avec Cypress et Applitools
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-12-10T16:14:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-run-visual-regression-testing-on-a-next-js-app-with-cypress-and-applitools
coverImage: https://www.freecodecamp.org/news/content/images/2020/12/applitools.jpg
tags:
- name: Next.js
  slug: nextjs
- name: Testing
  slug: testing
- name: user testing
  slug: user-testing
seo_title: Comment exécuter des tests de régression visuelle sur une application Next.js
  avec Cypress et Applitools
seo_desc: "A critical component of any development project is the tests that make\
  \ sure that project is always doing exactly what it’s supposed to be doing. \nThere\
  \ are a ton of testing tools available to us, but not all of them test what someone\
  \ actually experie..."
---

Un composant critique de tout projet de développement est les tests qui garantissent que le projet fait toujours exactement ce qu'il est censé faire. 

Il existe une tonne d'outils de test disponibles, mais tous ne testent pas ce qu'une personne vit réellement. Comment pouvons-nous utiliser Applitools pour tester visuellement notre projet et nous assurer qu'il fonctionne correctement ?

* [Qu'est-ce que le test de régression visuelle ?](#heading-questce-que-le-test-de-regression-visuelle)
* [Qu'est-ce que Cypress ?](#heading-questce-que-cypress)
* [Qu'est-ce qu'Applitools ?](#heading-questce-quapplitools)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Étape 0 : Création d'une nouvelle application React avec Next.js](#heading-etape-0-creation-dune-nouvelle-application-react-avec-nextjs)
* [Étape 1 : Installation et configuration de Cypress dans une application Next.js](#heading-etape-1-installation-et-configuration-de-cypress-dans-une-application-nextjs)
* [Étape 2 : Création de votre premier test Cypress dans une application Next.js](#heading-etape-2-creation-de-votre-premier-test-cypress-dans-une-application-nextjs)
* [Étape 3 : Installation et configuration d'Applitools Eyes](#heading-etape-3-installation-et-configuration-dapplitools-eyes)
* [Étape 4 : Test de régression visuelle avec Applitools Eyes](#heading-etape-4-test-de-regression-visuelle-avec-applitools-eyes)

%[https://www.youtube.com/watch?v=3dF4t56LHhs]

Vous pouvez également consulter [mon live stream](https://www.youtube.com/watch?v=Bei0Cvu7D7I) depuis [ma chaîne Twitch](https://twitch.tv/colbyfayock) où j'ai parcouru l'ensemble du processus de configuration d'une nouvelle application et de son test avec Cypress et Applitools.

Et pour être tout à fait transparent, j'ai récemment accepté un poste de Developer Advocate chez Applitools. Mais vous pouvez suivre ce tutoriel en utilisant son niveau gratuit, sans carte de crédit requise.

## Qu'est-ce que le test de régression visuelle ?

Similaire à la plupart des tests, le test de régression visuelle est un type de test qui s'exécutera périodiquement et à diverses étapes du cycle de vie d'un projet, comme lors d'une demande de pull ou d'un déploiement en production, pour s'assurer que tout dans l'application fonctionne correctement.

Ce que fait différemment le test de régression visuelle, cependant, c'est qu'il compare directement des captures visuelles de votre projet. Il détecte tout changement de contenu, de mise en page ou de tout autre détail que vous souhaitez, soit en visitant statiquement une page, soit en interagissant avec elle pour prévisualiser le résultat de cette interaction.

## Qu'est-ce que Cypress ?

[Cypress](https://www.cypress.io/) est un framework de test basé sur JavaScript que nous utiliserons pour exécuter notre suite de tests. Il exécute les tests dans le navigateur, nous permettant de vérifier directement l'état de notre projet là où les gens l'utiliseront réellement.

L'avantage de Cypress est qu'il offre également la possibilité d'interagir avec la page. Par exemple, si nous voulons tester qu'un utilisateur de notre application peut se connecter, nous pouvons entrer des identifiants et soumettre le formulaire de connexion, puis vérifier que le processus d'authentification a fonctionné correctement.

## Qu'est-ce qu'Applitools ?

[Applitools](https://info.applitools.com/ucXr9) est un outil de test visuel et une plateforme d'automatisation qui nous permet de comparer visuellement notre application à différents moments, nous donnant la possibilité de vérifier si quelque chose a changé ou ne fonctionne pas correctement.

Bien qu'Applitools ait quelques fonctionnalités différentes que nous pouvons utiliser, nous allons nous concentrer sur l'utilisation de l'API Eyes, que nous utiliserons pour capturer notre capture d'écran et l'envoyer au tableau de bord Applitools.

## Que allons-nous construire ?

Bien que nous puissions vraiment exécuter Cypress et Applitools sur une [variété de types de projets](https://info.applitools.com/ucXsd), nous allons utiliser Next.js pour créer rapidement une nouvelle application [React](https://reactjs.org/). Cela nous permettra de nous concentrer sur les outils de test plutôt que sur l'application elle-même.

Une fois notre application configurée, nous installerons Cypress et Applitools afin de les utiliser pour exécuter nos tests de régression visuelle.

_Note : vous aurez besoin d'un compte Applitools pour configurer les tests de régression visuelle. Vous pouvez [vous inscrire pour un compte gratuit](https://info.applitools.com/ucXsg) sur applitools.com._

## Étape 0 : Création d'une nouvelle application React avec Next.js

Pour commencer, nous allons utiliser [Create Next App](https://nextjs.org/docs/api-reference/create-next-app) pour créer une nouvelle application Next.js.

Une fois que vous êtes dans le répertoire où vous souhaitez créer votre nouveau projet, exécutez dans votre terminal :

```
npx create-next-app my-testing-app

```

_Note : vous pouvez changer le nom du projet de `my-testing-app` à ce que vous souhaitez._

Cela clonera l'exemple par défaut de Next.js depuis GitHub, installera les dépendances et nous permettra immédiatement d'être productifs avec nos outils de test.

Une fois terminé, naviguez dans votre nouveau projet :

```
cd my-testing-app

```

Démarrez votre serveur de développement :

```
npm run dev

```

Et maintenant votre site devrait être disponible à l'adresse [http://localhost:3000](http://localhost:3000) !

![Image](https://www.freecodecamp.org/news/content/images/2020/12/new-nextjs-app.jpg)
_Nouvelle application Next.js_

## Étape 1 : Installation et configuration de Cypress dans une application Next.js

Maintenant que notre application est configurée, nous voulons installer Cypress afin de pouvoir l'utiliser pour exécuter nos tests.

De retour dans notre terminal, nous pouvons installer Cypress avec :

```
npm install cypress --save-dev

```

Ici, nous incluons le drapeau `--save-dev`, car nous n'avons pas besoin de Cypress pour fonctionner dans la version de production de notre application, nous l'installons donc comme une dépendance de développement.

Une fois cela terminé, nous avons besoin d'un moyen d'exécuter Cypress depuis la ligne de commande. Bien que nous puissions naviguer vers Cypress lui-même, nous pouvons plutôt ajouter une nouvelle commande de script, ce qui facilitera l'exécution de Cypress.

À l'intérieur de `package.json`, sous `scripts`, ajoutez ce qui suit :

```json
"cy:open": "cypress open"

```

Maintenant, dans notre terminal, nous pouvons exécuter ce script pour ouvrir Cypress :

```
npm run cy:open

```

Si c'est la première fois que vous exécutez Cypress, cela peut prendre une seconde supplémentaire et installer Cypress dans votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/opening-cypress-in-terminal.jpg)
_Ouverture de Cypress pour la première fois_

Une fois terminé, Cypress ouvrira un nouveau panneau de dialogue qui servira de tableau de bord pour exécuter les tests de votre projet.

Vous remarquerez également que Cypress vous informe qu'il a également ajouté un nouveau répertoire à votre projet sous `cypress`. Cela inclut des fichiers d'exemple qui vous permettent de voir comment Cypress fonctionne et de commencer immédiatement.

Pour essayer cela, sur le côté droit du panneau Cypress, cliquez sur **Exécuter 19 spécifications d'intégration**.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cypress-run-all-tests.jpg)

Cypress ouvrira alors un nouveau navigateur et exécutera tous les tests d'exemple.

Ensuite, nous ajouterons quelques-uns de nos propres tests.

[Suivez le commit !](https://github.com/colbyfayock/my-testing-app/commit/ba73974d4521443d64fa4bddbc07500c0bb7b74f)

## Étape 2 : Création de votre premier test Cypress dans une application Next.js

Maintenant que nous pouvons exécuter nos tests avec succès, essayons d'ajouter les nôtres.

Nous n'avons pas vraiment besoin des tests que Cypress a inclus dans les exemples, alors supprimons le répertoire entier `integration/examples`.

Ensuite, créez un nouveau fichier sous `integration` appelé `home.spec.js` et ajoutez ce qui suit à l'intérieur :

```javascript
/// <reference types="cypress" />

context('Home', () => {
  beforeEach(() => {
    cy.visit('http://localhost:3000');
  });

  it('should find the title of the homepage', () => {
    cy.get('h1').contains('Welcome');
  });
});

```

Dans le code ci-dessus, nous :

* Ajoutons d'abord Cypress comme type de référence, ce qui permet à Cypress de trouver le fichier et de savoir qu'il doit l'utiliser pour exécuter un test
* Créons un nouveau contexte pour notre test et le définissons comme Home
* Disons à Cypress que avant chaque test, nous voulons qu'il visite notre page d'accueil
* Définissons un test qui récupère le h1 et vérifie qu'il contient "Welcome"

Si nous regardons maintenant Cypress, nous verrons que nous n'avons qu'un seul test d'intégration. Si nous cliquons dessus et essayons d'exécuter le test, nous verrons que nous obtenons en fait une erreur, car nous n'avons jamais démarré notre serveur de développement, ce qui signifie qu'il n'est pas disponible.

Pour corriger cela, nous allons utiliser un outil appelé [start-server-and-test](https://www.npmjs.com/package/start-server-and-test).

Ce package fera ce que le nom implique, il va :

* Démarrer notre serveur en fonction de la commande que nous fournissons
* Exécuter les tests que nous fournissons
* Arrêter le serveur une fois terminé

Pour l'ajouter, dans notre terminal, exécutons :

```
npm install start-server-and-test --save-dev

```

Ensuite, dans notre fichier `package.json`, nous allons ajouter une autre nouvelle commande à l'objet `scripts` :

```json
"test": "start-server-and-test dev 3000 cy:open"

```

Ici, nous disons à start-server-and-test que nous voulons exécuter la commande `dev` pour démarrer notre serveur, qu'il sera disponible sur le port 3000, et que nous voulons exécuter la commande `cy:open` après pour exécuter nos tests.

Et si nous retournons dans notre terminal et exécutons :

```
npm run test

```

Nous verrons que Cypress s'ouvre comme avant. Mais si nous exécutons maintenant notre test, nous pouvons voir qu'il ouvre avec succès notre application Next.js et qu'il voit le mot "Welcome" à l'intérieur de notre `h1` !

![Image](https://www.freecodecamp.org/news/content/images/2020/12/successful-test-cypress.jpg)
_Exécution réussie d'un test dans Cypress_

[Suivez le commit](https://github.com/colbyfayock/my-testing-app/commit/b7fdcada3c6642521baa8c34949c4b9df3e56c18).

## Étape 3 : Installation et configuration d'Applitools Eyes

Avec Cypress exécutant nos tests avec succès, nous pouvons maintenant nous connecter à nos tests et utiliser Applitools pour exécuter des tests de régression visuelle sur notre projet.

Avant de plonger, assurez-vous d'avoir un [compte gratuit](https://info.applitools.com/ucXsg) configuré chez Applitools, dont nous aurons besoin pour configurer une clé API.

Pour commencer, nous allons devoir installer la bibliothèque Eyes à notre projet.

Dans notre terminal, nous pouvons exécuter :

```
npm install @applitools/eyes-cypress --save-dev

```

Ce qui installera le [SDK spécifique à Cypress pour Applitools Eyes](https://www.npmjs.com/package/@applitools/eyes-cypress).

Une fois l'installation terminée, nous pouvons exécuter le script de configuration d'Eyes.

```
npx eyes-setup

```

Cela parcourra le projet et ajoutera les configurations nécessaires à Cypress pour faire fonctionner Eyes correctement.

Enfin, nous devrons rendre notre clé API Applitools disponible chaque fois que nous exécuterons nos tests.

Pour commencer, nous devons trouver notre clé API dans notre compte Applitools.

Dans le tableau de bord Applitools, sélectionnez **My API Key** sous le menu déroulant du compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-finding-api-key.jpg)
_Trouver la clé API Applitools_

Cela ouvrira une boîte de dialogue où vous pouvez sélectionner et copier votre clé API.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-api-key.jpg)
_Copie de la clé API Applitools_

Vous voudrez enregistrer cette clé API pour plus tard lorsque nous exécuterons nos tests.

Ensuite, nous voudrons pouvoir définir notre clé API. Nous pouvons le faire de plusieurs manières :

* [Exporter la variable d'environnement](https://docs.cypress.io/guides/guides/environment-variables.html#Option-3-CYPRESS) dans notre shell avant d'exécuter les tests
* Préfixer la clé API à la commande de test
* Ajouter la clé API au fichier de configuration [applitools.config.js](https://www.npmjs.com/package/@applitools/eyes-cypress#advanced-configuration)
* Créer une variable d'environnement en utilisant dotenv et le package [cypress-dotenv](https://github.com/morficus/cypress-dotenv)

Pour cette démonstration, nous allons exécuter notre test en préfixant la clé API à notre commande. Cela nous permettra de tester cela rapidement.

Pour ce faire, chaque fois que nous exécutons une commande comme `npm run test`, nous allons inclure notre clé API devant elle comme ceci :

```
APPLITOOLS_API_KEY="abcd1234" npm run test

```

_Note : n'oubliez pas de remplacer la clé API par votre identifiant unique._

Et maintenant, nous devrions être prêts à ajouter notre premier test.

[Suivez le commit !](https://github.com/colbyfayock/my-testing-app/commit/0b11b0238270b320969ac9982b271a48981634f4)

## Étape 4 : Test de régression visuelle avec Applitools Eyes

Nous avons configuré Cypress et Applitools et ils sont prêts à être utilisés, ce qui signifie que nous pouvons maintenant ajouter Applitools Eyes pour tester visuellement notre application !

Notre application n'a pas encore beaucoup de fonctionnalités, nous pouvons donc commencer par une vérification de base qui s'assure que notre page d'accueil a l'apparence qu'elle devrait avoir à chaque fois que nos tests s'exécutent.

Pour commencer, à l'intérieur de notre fichier `cypress/integrations/home.spec.js`, ajoutons ce qui suit juste en dessous de notre instruction `it` existante :

```javascript
it('should verify the homepage looks as expected', () => {
  cy.eyesOpen({
    appName: 'My App',
    testName: 'Homepage Check',
  });

  cy.eyesCheckWindow({
    tag: 'App Window',
    target: 'window',
    fully: true
  });

  cy.eyesClose();
});

```

Voici ce que nous faisons ici :

* Tout d'abord, nous "ouvrons les yeux" d'Applitools, ce qui préparera la fonctionnalité Eyes à vérifier notre application
* Ensuite, nous exécutons une vérification sur la fenêtre de notre application, capturant essentiellement une capture d'écran de notre application et l'envoyant à Applitools
* Enfin, nous "fermons les yeux" d'Applitools, informant Eyes que nous exécutons nos vérifications

Maintenant, si nous exécutons notre commande de test et démarrons notre test :

```
APPLITOOLS_API_KEY="abcd1234" npm run test

```

Nous pouvons voir que Cypress exécute notre nouveau cas de test qui ne semble pas faire grand-chose à l'intérieur de notre navigateur, mais affiche un indicateur de réussite.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/successul-applitools-check.jpg)
_Exécution réussie d'une vérification Applitools Eyes dans Cypress_

Maintenant, si nous retournons à notre tableau de bord Applitools :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-first-snapshot.jpg)
_Premier instantané dans Applitools_

Nous pouvons voir que nous avons une nouvelle "exécution" intitulée Homepage Check (que nous avons spécifiée dans le code) qui montre qu'elle a réussi avec un instantané de notre application.

Maintenant, avoir cette capture d'écran seule n'est pas ce qui rend cela puissant. À partir de maintenant, chaque fois que nous exécuterons ce test, Applitools comparera notre application avec cet instantané original et nous informera si quelque chose a changé.

Pour tester cela, nous allons changer la couleur du titre de notre page. Cela peut sembler un changement simple, mais les changements de style peuvent être plus difficiles à détecter pour des outils comme Cypress seul, ce qui est là où Applitools Eyes brillera avec sa comparaison d'instantanés.

À l'intérieur du fichier `styles/Home.module.css`, ajoutons ce qui suit à la classe `.title` :

```css
color: #ddd;
```

![Image](https://www.freecodecamp.org/news/content/images/2020/12/nextjs-app-title-color-change.jpg)
_Application Next.js avec un titre gris clair_

Bien que nous n'ayons peut-être pas intentionnellement fait un changement comme celui-ci en pratique, cela pourrait arriver si nous changions des styles qui se propagent à notre titre. Cela rend notre titre difficile à lire, mais cela en fait un cas de test parfait.

Maintenant, exécutons nos tests à nouveau :

```
APPLITOOLS_API_KEY="abcd1234" npm run test
```

Mais cette fois, nous pouvons voir que notre test échoue !

![Image](https://www.freecodecamp.org/news/content/images/2020/12/cypress-failed-applitools-eyes-test-error.jpg)
_Cypress génère une erreur avec la vérification Applitools Eyes_

Notre test Applitools échoue car il indique que "Eyes-Cypress a détecté des différences ou des erreurs lors de l'exécution des tests visuels".

Si nous regardons à l'intérieur de notre tableau de bord Applitools :

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-text-change-detected.jpg)
_Changement détecté dans le texte du titre de l'application dans Applitools Eyes_

Nous pouvons voir que nous avons maintenant une "exécution non résolue" où Applitools nous montre les différences sur la page, qui dans notre cas, est la partie "Welcome to" de notre titre.

Cela est super utile lorsque l'on travaille sur des projets où il peut être difficile de tester chaque page ou type de page dans une application. Nous pouvons nous assurer que si quelque chose change ou se casse, cela sera immédiatement signalé dans Applitools.

À partir de là, si nous sommes satisfaits du changement de couleur, nous pouvons accepter la nouvelle version de notre application.

![Image](https://www.freecodecamp.org/news/content/images/2020/12/applitools-eyes-accept-reject-changes.jpg)
_Accepter ou rejeter les changements dans Applitools Eyes_

Sinon, nous pouvons le rejeter et informer notre équipe qu'il doit être corrigé.

[Suivez le commit !](https://github.com/colbyfayock/my-testing-app/commit/6c5f5655d0e15878e870a893652201979244e986)

## Qu'est-ce qui suit ?

Entre Cypress et Applitools, nous avons beaucoup de choses que nous pouvons faire pour nous assurer que notre application se comporte comme nous le voulons.

La plupart du temps, lorsque nous construisons une application, nous construisons cette application pour que les gens puissent interagir avec elle.

En utilisant Cypress, nous pouvons cliquer sur différentes parties de la page, changer l'état de la page, puis exécuter une vérification avec Applitools Eyes pour nous assurer qu'elle fonctionne comme nous l'attendons.

Nous pouvons également faire fonctionner Cypress sur différents navigateurs pour nous assurer que notre application fonctionne correctement partout où quelqu'un essaie de l'utiliser !

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">F426 Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">F3FA Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">F4EB Inscrivez-vous à ma newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">F49D Sponsorisez-moi</a>
    </li>
  </ul>
</div>