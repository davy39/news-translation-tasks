---
title: Comment ajouter des tests de bout en bout à votre projet avec Cypress
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-12-05T23:16:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-end-to-end-tests-to-your-project-with-cypress-a74437f6df6e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*LpbDW-kW6Jh85WFAFEKwlQ.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: software development
  slug: software-development
- name: Software Testing
  slug: software-testing
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment ajouter des tests de bout en bout à votre projet avec Cypress
seo_desc: 'By Austin Tackaberry

  In this post, I will walk through the process of adding Cypress end-to-end tests
  to an existing project.

  Why end to end testing?

  There are pros and cons to all testing methods. End to end testing is the closest
  to actual user tes...'
---

Par Austin Tackaberry

Dans cet article, je vais vous guider à travers le processus d'ajout de tests de bout en bout Cypress à un projet existant.

### Pourquoi les tests de bout en bout ?

Il y a des avantages et des inconvénients à toutes les méthodes de test. Les tests de bout en bout sont les plus proches des tests utilisateurs réels, ce qui est l'un de leurs principaux avantages. Plus le test est proche de la simulation de l'utilisateur, plus il est susceptible de détecter les problèmes que l'utilisateur pourrait rencontrer.

Si vous vouliez qu'un utilisateur teste l'envoi d'un tweet sur Twitter, vous pourriez lui dire quelque chose comme :

> Allez sur [https://twitter.com](https://twitter.com,) et connectez-vous. Cliquez sur la zone de texte avec le texte de remplissage « Qu'est-ce qui se passe ? », puis tapez « Ceci est un tweet de test ». Cliquez sur le bouton avec le texte « Tweeter ». Maintenant, allez sur votre page de profil et regardez le premier tweet. Le texte devrait être égal à « Ceci est un tweet de test ».

Idéalement, vous donnez des instructions similaires à votre exécutant de tests de bout en bout.

Vous pourriez également lui faire chercher des éléments par noms de classe ou identifiants, mais que se passe-t-il si les noms de classe ou les identifiants changent intentionnellement ? Ou si le texte change accidentellement ? Si vous avez dit à l'exécutant de test de cliquer sur le bouton par nom de classe, le test pourrait passer incorrectement. Vous pourriez argumenter :

> Et si vous voulez changer le texte intentionnellement ? Peut-être voulez-vous changer le texte du bouton pour qu'il lise « Envoyer » au lieu de « Tweeter » ?

C'est peut-être un argument valable, mais vous pourriez aussi argumenter que vous voulez réellement que le test échoue si le texte change. En fin de compte, vous devez vous demander : « Si ce texte change, est-ce que je veux que mes tests échouent ? » Dans le cas de « Envoyer » contre « Tweeter », peut-être que vous ne voulez pas que le test échoue, mais peut-être que si le texte était accidentellement supprimé ou mal orthographié, alors vous voudriez qu'ils échouent. Vous ne pouvez pas vraiment avoir les deux, alors vous devez prendre la meilleure décision pour vous et votre application.

Certains inconvénients des tests de bout en bout sont :

* Ils sont « coûteux », c'est-à-dire qu'ils prennent beaucoup de temps à s'exécuter. Chaque test nécessite qu'un navigateur complet soit instancié avec des événements de navigateur réels, ce qui prend plus de temps que les tests unitaires ou d'intégration.
* Il fait un bon travail pour trouver les problèmes, mais il ne fait pas un bon travail pour vous aider à résoudre ces problèmes. Votre test de bout en bout pourrait trouver que le système de paiement est cassé, mais il ne vous dira pas lequel de vos 10 microservices a causé le problème.

### Quel framework de test de bout en bout choisir

Il existe de nombreux frameworks de test de bout en bout, et il peut être difficile de choisir le « bon ». Je vais partager mes pensées très brièvement, bien que j'aie admis n'avoir utilisé que Cypress :

**Test Cafe** — C'est le dernier framework de test de bout en bout, et il semble être très bon. Il s'intègre avec Browser Stack, a un bon support de navigateur, prend en charge tous les frameworks front-end, supporte la syntaxe ES2015+ et aussi TypeScript. Il semble que vous devez avoir la version payante pour obtenir des tests enregistrés.

**Puppeteer** — C'est la solution open source de Google. Il semble léger et facile à démarrer. Il est open source et s'exécute sur Chromium (avec ou sans tête). Puppeteer est présenté comme un framework de test qui a une fonctionnalité riche, mieux que de ne pas avoir de tests de bout en bout, mais ce n'est pas une solution complète. Ils ont également récemment partagé qu'ils expérimentent avec Firefox.

**Cypress** — C'est un framework de test open source convivial pour les développeurs. Cypress enregistre des instantanés et des vidéos de vos tests, dispose d'une console d'exécution de test et est gratuit. Il est facile de commencer pour les développeurs et les ingénieurs QA. Il ne prend actuellement en charge que les variantes de Chrome, mais il a le support multi-navigateur sur la feuille de route. Il n'a pas de support natif pour les iframes, bien qu'il existe des solutions de contournement. Cypress a son propre système basé sur les promesses que vous devez utiliser (vous ne pouvez pas utiliser les promesses ES6).

Voici une bonne ressource pour une comparaison approfondie de Cypress et Test Cafe : [https://medium.com/yld-engineering-blog/evaluating-cypress-and-testcafe-for-end-to-end-testing-fcd0303d2103](https://medium.com/yld-engineering-blog/evaluating-cypress-and-testcafe-for-end-to-end-testing-fcd0303d2103)

![Image](https://cdn-media-1.freecodecamp.org/images/46bWXP9x94n3PNT4wmB0KC8H2-kJPmj8b37Z)
_Photo par [Unsplash](https://unsplash.com/photos/cY-SXZp6TUY?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">chuttersnap</a> sur <a href="https://unsplash.com/search/photos/options?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

### Mise en route

Le projet que je vais utiliser est [https://ydkjs-exercises.com](https://ydkjs-exercises.com). Il s'agit d'une application web monopage qui fournit des exercices conçus pour aider les utilisateurs à tester leurs connaissances tout en lisant [You Don't Know JavaScript](https://github.com/getify/You-Dont-Know-JS). Il utilise React, React Router et l'API de contexte React. Il y a des tests unitaires/d'intégration utilisant Jest et react-testing-library. Et maintenant, je vais ajouter des tests de bout en bout avec Cypress !

Je vais suivre les progrès via des tags, en commençant par `cypress-0`, et en incrémentant l'entier à chaque étape. [Voici le point de départ](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-0).

La première étape consiste à installer Cypress en tant que `devDependency` :

```
npm install cypress --save-dev
```

La version actuelle de Cypress est v3.1.1. La documentation mentionne que le package npm Cypress est un wrapper autour du binaire Cypress. Et qu'à partir de la version 3.0, le binaire est téléchargé dans un répertoire de cache global pour être utilisé dans plusieurs projets.

Maintenant, ouvrons Cypress. Si vous utilisez npm version > 5.2, vous pouvez l'ouvrir en utilisant :

```
npx cypress open
```

Cela ouvre Cypress avec un modal de bienvenue nous informant qu'ils ont ajouté un tas de fichiers à notre projet :

![Image](https://cdn-media-1.freecodecamp.org/images/M41bAYSYx5WSFzrEg8atyQNzd-mLK6-EtOiU)

Après avoir cliqué pour fermer le modal, nous voyons qu'il y a un tas de tests d'exemple, et nous voyons que nous pouvons les exécuter dans Chrome 70. Si vous cliquez sur « Runs », vous voyez que vous pouvez configurer un tableau de bord Cypress pour regarder les exécutions précédentes. Nous ne allons pas nous en soucier, mais vous pourriez certainement vérifier cette fonctionnalité.

J'ai choisi de suivre tous ces fichiers d'exemple dans git car je veux que les futurs contributeurs y aient accès lorsqu'ils forkent le projet.

[Voici l'avancement actuel jusqu'à ce point.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-1)

### Écrire un script Cypress

Nous sommes presque prêts à écrire notre premier test. Nous devons créer un répertoire pour stocker nos tests Cypress : `cypress/integration/ydkjs`

Maintenant, nous devons écrire le script qui démarrera notre serveur de développement, exécutera nos tests Cypress, puis arrêtera notre serveur de développement. Ce projet a été amorcé avec Create React App, ce qui signifie qu'il a un fichier `scripts/start.js` qui est utilisé pour démarrer le serveur. Je vais copier le code de là, le coller dans un nouveau fichier `scripts/cypress.js`, et faire quelques modifications.

L'extrait de code ci-dessous est le cœur de notre nouveau fichier `scripts/cypress.js`.

```js
return devServer.listen(port, HOST, err => {
    if (err) {
        return console.log(err);
    }
    if (isInteractive) {
        clearConsole();
    }
    console.log(chalk.cyan('Démarrage du serveur de développement...\n'));
    return cypress
        .run({
            spec: './cypress/integration/ydkjs/*.js',
        })
        .then(results => {
            devServer.close();
        });
});
```

Il fait exactement ce que nous avons dit qu'il ferait. Il démarre le serveur de développement, exécute tous les fichiers de test dans `cypress/integration/ydkjs`, puis arrête le serveur de développement.

Maintenant, dans `cypress.json`, nous pouvons ajouter notre `baseUrl` :

```js
{
    "baseUrl": "http://localhost:3000"
}
```

Maintenant, nous pouvons écrire notre premier test ! Appelons-le `cypress/integration/ydkjs/sidebar.js`, et nous l'utiliserons pour tester la fonctionnalité de la barre latérale. Pour l'instant, écrivons simplement un test factice :

```js
/* globals context cy */
/// <reference types="Cypress" />
context('Sidebar', () => {
    beforeEach(() => {
        cy.visit('/');
    });
    
    it('fait quelque chose', () => {
        cy.contains('YDKJS Exercises');
    });
});
```

Tout ce que nous faisons ici est de visiter l'URL de base et de trouver un élément qui contient « YDKJS Exercises ». Notez que j'ai seulement ajouté le commentaire sur la première ligne pour que `eslint` ne se plaigne pas des variables Cypress non définies.

J'ai également ajouté un nouveau script dans mon `package.json` :

```js
"scripts": {
    ...
    "cypress": "node scripts/cypress.js",
    ...
},
```

Ainsi, je peux maintenant appeler `npm run cypress` lorsque je veux exécuter mes tests de bout en bout Cypress. Maintenant, lorsque j'exécute cette commande dans le terminal, je vois que mon serveur démarre, le test s'exécute et réussit, puis le serveur s'arrête. Hourra !

[Voici le code jusqu'à ce point.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-2)

### Écrivons quelques vrais tests !

Maintenant que nous avons notre script Cypress configuré pour démarrer le serveur, exécuter les tests et arrêter le serveur, nous pouvons commencer à écrire quelques tests !

Nous avons déjà créé un fichier de test `sidebar.js`, alors écrivons quelques tests autour de notre fonctionnalité de barre latérale. Peut-être que notre premier test devrait vérifier que la barre latérale se ferme lorsque nous cliquons sur le bouton X et se rouvre lorsque nous cliquons sur le hamburger.

Avant de trouver le bouton X et de cliquer dessus, assurons-nous que la barre latérale est visible lors du chargement de la page d'accueil. Je peux mettre cela dans la méthode `beforeEach` juste après avoir navigué vers la page d'accueil, car je vais toujours vouloir m'assurer que la barre latérale est visible lorsque je vais pour la première fois sur la page d'accueil.

```js
beforeEach(() => {
    cy.visit('/');
    cy.contains('Progress').should('exist');
});
```

Maintenant, commençons à écrire le test. Comme le X est en fait un SVG, nous ne pouvons pas facilement dire à Cypress d'aller le trouver. Nous allons donc le trouver en utilisant un attribut `data-testid`, ou `cy.get("[data-testid=closeSidebar]").click()` . Je sais ce que vous pensez...

> Ok, je comprends que vous ne pouvez pas utiliser le texte dans ce cas. Mais pourquoi utiliser un attribut de données ? Pourquoi ne pas simplement utiliser un nom de classe ou un identifiant ?

La meilleure pratique est d'utiliser un attribut de données. Vous pourriez utiliser des noms de classe, mais ils sont sujets à changement et mieux optimisés pour le style.

En ce qui concerne les identifiants, le principal problème est que vous ne pouvez en avoir qu'un par page, ce qui pourrait être ennuyeux. Et si vous voulez obtenir tous les boutons X de la page et vérifier qu'il devrait y en avoir 2 ? Vous ne pouvez pas faire cela facilement en utilisant des identifiants.

Notre test terminé pourrait ressembler à ceci :

```js
it('se ferme lorsque X est cliqué et se rouvre lorsque le hamburger est cliqué', () => {
    cy.get('[data-testid=closeSidebar]').click();
    cy.contains('Progress').should('not.exist');
    cy.get('[data-testid=openSidebar]').click();
    cy.contains('Progress').should('exist');
});
```

Je vais sur la page d'accueil, je m'assure que la barre latérale est ouverte, puis je clique sur le bouton X et je m'assure qu'elle est fermée, puis je clique sur le hamburger et je m'assure que la barre latérale est rouverte. Lorsque nous l'exécutons, il réussit !

Et vous pouvez voir une vidéo du test dans `cypress/ydkjs/sidebar.js.mp4` ! Plutôt sympa. C'est super utile lorsque vos tests échouent et que vous ne savez pas pourquoi.

Une chose à laquelle vous devez faire attention est que Cypress est un système basé sur les promesses. Lorsque vous exécutez `cy.contains('Progress').should('not.exist')`, Cypress ne passera pas à la ligne de code suivante tant que cette ligne n'est pas vraie. S'il voit un élément DOM qui contient « Progress », il attendra qu'il disparaisse ou jusqu'à ce qu'il expire et que le test échoue.

Ce système est agréable car il rend l'écriture de ces tests très rapide et facile. Il peut parfois vous mordre, cependant, lorsque vous traitez avec des actions asynchrones. Peut-être voulez-vous vous assurer qu'un élément DOM n'apparaît pas à la suite d'un clic sur un bouton. Vous pourriez simplement cliquer sur le bouton et puis vérifier si cet élément DOM existe, non ? Mais que se passe-t-il si l'élément DOM est créé une seconde après avoir cliqué sur le bouton ? Votre test passerait alors qu'il aurait dû échouer.

Écrivons un autre test.

Lorsque nous cliquons sur un livre dans la barre latérale, nous voulons naviguer vers la page associée à ce livre.

```js
it('navigue vers /up-going lorsque Up & Going est sélectionné', () => {
    cy.contains(/Up & Going \(/).click({ force: true });
    cy.url().should('include', '/up-going');
    cy.contains('Chapter 1: Into Programming').should('exist'); 
    cy.contains('Chapter 2: Into JavaScript').should('exist');
});
```

Il y a quelques choses à noter concernant ce test. Sur la page d'accueil de ydkjs-exercises, le texte « Up & Going » est à deux endroits. Une fois dans la barre latérale et une fois au milieu de la page. Dans la barre latérale, le texte complet est « Up & Going (0/41) » ce qui signifie que l'utilisateur a répondu à 0 questions sur 41 possibles. Sur la page principale, le texte est simplement « Up & Going ». Donc, pour m'assurer que nous cliquons sur « Up & Going » depuis la barre latérale, j'utilise une regex pour cliquer sur l'élément qui contient « Up & Going (». Je ne veux pas qu'il inclue le 0 ou le 41 car ces nombres pourraient changer. Cela pourrait être l'un de ces cas où l'utilisation d'un attribut de données pourrait être meilleure que l'utilisation du texte comme je l'ai fait dans l'extrait de code ci-dessus.

Je dois forcer l'événement de clic car la balise d'ancrage a le texte mais elle est enveloppée par un élément de liste. Après cela, je teste pour m'assurer que l'URL est correcte et que le contenu de la page est correct.

[Voici l'état final du code.](https://github.com/austintackaberry/ydkjs-exercises/tree/cypress-4)

### Conclusion

Comme vous pouvez le voir, une fois que vous avez installé Cypress, que vous avez le script approprié configuré pour démarrer votre serveur de développement, et que vous commencez à écrire les tests, travailler avec Cypress est assez rapide et sans douleur.

Une fois que vous êtes à l'aise avec cela, vous pouvez même rendre votre code de test réutilisable en créant vos propres commandes Cypress personnalisées !

Vous pourriez exécuter ces tests avant le commit ou dans un environnement CI pour vous assurer qu'aucune régression ne se glisse dans la production.

Dans l'ensemble, Cypress est un choix parfaitement solide si vous voulez porter vos tests au niveau supérieur avec des tests de bout en bout !

Bon codage !