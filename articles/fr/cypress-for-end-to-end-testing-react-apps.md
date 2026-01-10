---
title: Comment utiliser Cypress pour les tests end-to-end de vos applications React
subtitle: ''
author: Okosa Leonard
co_authors: []
series: null
date: '2023-11-01T22:45:46.000Z'
originalURL: https://freecodecamp.org/news/cypress-for-end-to-end-testing-react-apps
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/1_PfsGOHgjLPh3EFOkxCRmjw.png
tags:
- name: React
  slug: react
- name: Software Testing
  slug: software-testing
seo_title: Comment utiliser Cypress pour les tests end-to-end de vos applications
  React
seo_desc: 'React is a popular framework for building web applications. It''s is one
  of the best options for frontend engineering because of its declarative approach
  to user interface design and component-based architecture.

  But it can be difficult to make sure y...'
---

React est un framework populaire pour la construction d'applications web. C'est l'une des meilleures options pour l'ingénierie frontend grâce à son approche déclarative de la conception d'interface utilisateur et à son architecture basée sur les composants.

Mais il peut être difficile de s'assurer que votre application React fonctionne comme prévu dans divers scénarios différents.

Cypress est un framework de test end-to-end que vous pouvez utiliser pour tester vos applications React. Et dans ce tutoriel, j'expliquerai comment créer des tests end-to-end efficaces pour votre application web en utilisant Cypress et React.

## Table des matières

1. [Qu'est-ce que Cypress ?](#heading-quest-ce-que-cypress)
    
2. [Comment configurer votre environnement](#heading-comment-configurer-votre-environnement)
    
3. [Comment écrire votre premier test Cypress](#heading-comment-ecrire-votre-premier-test-cypress)
    
4. [Comment interagir avec les composants React](#heading-comment-interagir-avec-les-composants-react)
    
5. [Requêtes Cypress](#heading-cypress-queries)
    
6. [Assertions Cypress](#heading-cypress-assertions)
    
7. [Actions Cypress](#heading-cypress-actions)
    
8. [Comment organiser et exécuter vos tests Cypress](#heading-comment-organiser-et-executer-vos-tests-cypress)
    
9. [Plugins](#heading-plugins)
    
10. [Blocs Describe](#heading-describe-blocks)
    
11. [Commandes personnalisées](#heading-custom-commands)
    
12. [Tableau de bord Cypress](#heading-cypress-dashboard)
    
13. [Comment déboguer votre code avec Cypress](#heading-comment-deboguer-votre-code-avec-cypress)
    
14. [Intégration continue](#heading-integration-continue)
    
15. [Conclusion](#heading-conclusion)
    

## Qu'est-ce que Cypress ?

Cypress est un framework de test end-to-end open-source et simple, conçu pour le développement web moderne. Il est basé sur JavaScript.

L'outil fonctionne dans le navigateur, ce qui le distingue des autres outils de test comme Selenium. L'API concise et simple que Cypress fournit pour interagir avec votre application facilite la création et la gestion des tests.

Vous pouvez créer et gérer des tests qui imitent les interactions des utilisateurs avec Cypress. Vous pouvez également examiner votre application web pour un comportement attendu et résoudre tout problème qui survient.

## Comment configurer votre environnement

Avant de commencer à écrire des tests, vous voudrez configurer votre environnement. Vous devez avoir Node.js et npm (Node Package Manager) installés pour utiliser Cypress avec votre application React.

Vous pouvez visiter [https://nodejs.org/en/](https://nodejs.org/en/) pour télécharger et installer Node.js sur votre ordinateur si ce n'est pas déjà fait. Pour commencer à utiliser Cypress après avoir installé Node, vous pouvez suivre ces étapes :

### 1) Créer une application React

Nous utiliserons Vite pour développer notre application React, car il nous aide à créer rapidement et efficacement des applications web.

Pour commencer, créez une application React sur Vite en entrant le code suivant dans votre console :

```js
npm create vite@latest
```

Vite vous demandera de donner un nom à votre projet. Choisissez le nom que vous souhaitez.

Ensuite, Vite vous donnera le choix du framework. Assurez-vous simplement de sélectionner React pour cette leçon.

Il vous demandera ensuite de choisir entre TypeScript et JavaScript lorsque vous sélectionnez React. Choisissez JavaScript.

Ensuite, allez dans votre répertoire de projet et choisissez votre projet.

Enfin, tapez `npm install` puis `npm start dev` pour lancer votre projet.

Votre projet sera hébergé par Vite à l'adresse `http://localhost:5173/`. Pour voir votre projet dans un navigateur, cliquez sur le lien fourni.

### 2) Installer Cypress

Vous pouvez installer Cypress dans votre projet en utilisant ce code `install cypress --save-dev` dans votre terminal. Ce code installe Cypress dans votre application React.

### 3) Initialiser Cypress

Exécutez `npx Cypress open` depuis le répertoire de votre projet React. Cette commande devrait lancer Cypress Test Runner, un outil graphique pour créer et gérer des tests. Vous aurez maintenant deux alternatives pour les tests automatisés :

* Test End-to-End : Le test end-to-end implique un navigateur utilisant un outil automatisé comme Cypress, vous pouvez donc créer des tests composés de fonctions comme appuyer sur des boutons, taper dans des champs de saisie, etc. Cela aide à s'assurer que tout fonctionne parfaitement.
    
* Test de composants : Cela implique de tester des composants individuels au lieu de l'ensemble de l'application React.
    

#### Qu'est-ce que le Cypress Test Runner ?

Le test runner s'ouvre une fois que vous passez `npx cypress open`. C'est un outil graphique pour créer et gérer des tests, il vous permet également d'écrire et d'exécuter vos cas de test dans Cypress.

Après avoir sélectionné le type de test que vous souhaitez effectuer, la section suivante du test runner vous aide à spécifier le script que vous souhaitez exécuter, et vous donne l'option de sélectionner le navigateur que vous souhaitez utiliser et de valider vos tests comme prévu.

### 4) Structure de dossier

Cypress enregistrera automatiquement ses fichiers de test et configurations à l'intérieur de votre projet dans un sous-dossier nommé `cypress`.

## Comment écrire votre premier test Cypress

Nous utiliserons JavaScript pour écrire nos tests Cypress qui sont exécutés dans le navigateur. Voici comment créer votre premier test pour votre application React.

Supposons que nous souhaitons vérifier si le Document Object Model (DOM) affiche notre élément h2. Pour accomplir cela en utilisant Cypress, prenez les actions suivantes :

**Étape 1** : Dans votre dossier Cypress, allez dans le fichier e2e et vous y verrez une ligne de code similaire à celle-ci :

```javascript
describe('template spec', () => {
    it('passes', () => {
        cy.visit('https://example.cypress.io')
    })
    })
```

**Étape 2** : Maintenant, dans `cy.visit`, mettez à jour l'adresse http par défaut par l'adresse de votre application React ([http://localhost:5173/](http://localhost:5173/), si vous vous souvenez).

**Étape 3** : Nous souhaitons vérifier si le DOM contient notre élément h2. Naviguez jusqu'à l'élément que vous souhaitez tester et ajoutez `data-testid` comme attribut pour accomplir cela. Ensuite, attribuez un nom à l'attribut. Exemple : `<h2 data-testid="cypress-h1"> Site Web de Leo </h2>`.

**Étape 4** : Faites un espace et ajoutez ce morceau de code à votre dossier cypress pour voir si l'attribut existe.

```js
cy.get('[data-testid="cypress-header"]').should('exists');
```

Puisque Cypress est configuré pour exécuter les tests à la sauvegarde, dès que vous sauvegardez quelque chose dans votre éditeur de code, le test devrait démarrer instantanément dans Cypress.

## Comment interagir avec les composants React

Vous voudrez être familier avec la vaste gamme de commandes utilisées pour imiter les interactions des utilisateurs afin d'écrire des tests plus perspicaces.

Avec son ensemble étendu de commandes pour interagir avec et tester les éléments en ligne, Cypress est conçu spécifiquement pour les pages web et les applications web.

Pour imiter les interactions des utilisateurs et affirmer certains comportements de l'application, les scripts de test emploient ces instructions. Parce que Cypress maintient une chaîne de promesses en votre nom, vous pouvez enchaîner les commandes ensemble. Jusqu'à ce que la chaîne se brise et qu'une erreur se produise, chaque commande produit un "sujet" pour la commande suivante.

Les commandes Cypress peuvent être classées dans les groupes suivants : requêtes, assertions, actions et autres.

### Requêtes Cypress

Ce sont des commandes Cypress qui récupèrent l'état actuel de votre application. Elles réessayent si nécessaire pour s'assurer que l'élément DOM ou d'autres données qu'elles fournissent sont constamment à jour. Elles retournent un sujet pour que d'autres commandes agissent ou affirment.

Voici quelques façons d'organiser et d'exécuter des tests :

#### Utilisation de la méthode `.children()`

Pour choisir et travailler avec les éléments enfants directs d'un élément parent dans Cypress, utilisez la méthode `.children()`. Elle vous permet d'accéder à des éléments enfants spécifiques d'un élément parent donné en naviguant dans l'arborescence DOM.

Voici quelques exemples de l'utilisation de `.children()` dans Cypress :

Exemple 1 : Supposons que vous avez cette structure HTML dans votre fichier `jsx` :

```html
<div class="parent-element">
  <div class="child">Enfant 1</div>
  <div class="child">Enfant 2</div>
  <div class="child">Enfant 3</div>
</div>
```

Pour choisir et travailler avec les éléments enfants à l'intérieur de l'élément `.parent`, utilisez la fonction `.children()` comme ceci :

```javascript
cy.get('.parent').children('.child').should('have.length', 3);

// Cliquez sur le deuxième élément enfant
cy.get('.parent').children('.child').eq(1).click();
```

Exemple 2 : vous pouvez effectuer toute une gamme de tâches en utilisant `.children()` combiné avec d'autres fonctions Cypress. Vous pouvez, par exemple, reconnaître certains objets enfants et définir leurs propriétés :

```javascript
// Assurez-vous que le premier élément enfant contient le texte "Enfant 1"
cy.get('.parent').children('.child').first().should('contain', 'Enfant 1');

// Vérifiez que tous les éléments enfants ont une classe spécifique
cy.get('.parent').children('.child').each(($child) => {
  cy.wrap($child).should('have.class', 'child');
});
```

Exemple 3 : De nombreuses instructions Cypress peuvent être enchaînées pour effectuer des interactions plus complexes. En utilisant `.children()`, vous pouvez sélectionner l'élément parent, sélectionner ses éléments enfants, puis opérer avec les éléments enfants comme le démontre cet exemple :

```javascript
cy.get('.parent')
  .children('.child')
  .first()
  .click()
  .next()
  .type("Je suis Leo");
```

Dans cet exemple, pour interagir avec l'élément enfant suivant, nous sélectionnons d'abord l'élément `.parent`, puis utilisons `.children('.child')` pour sélectionner ses éléments enfants, cliquons sur le premier élément enfant, puis enchaînons plus d'instructions pour taper "Je suis Leo".

Ces exemples vous montrent comment sélectionner et travailler avec des éléments enfants à l'intérieur d'un élément parent dans Cypress en utilisant la fonction `.children()`. Selon votre structure HTML unique, vous pouvez modifier le sélecteur CSS à l'intérieur de `.children()` pour correspondre aux éléments enfants que vous souhaitez cibler.

Maintenant, vous devriez avoir une idée de comment `.children()` fonctionne et comment vous pouvez utiliser les requêtes comme type de commande Cypress. Il existe d'autres commandes de requête, mais vous pouvez toujours vous référer à la documentation sur [cypress.io](https://www.freecodecamp.org/news/p/ee697448-b73d-43dd-85de-d31f1e1005c6/cypress.io) pour en apprendre plus sur elles.

#### Utilisation de la commande cy.get()

`cy.get()` est une commande fondamentale dans le framework Cypress. Vous l'utilisez pour choisir et effectuer des actions sur les éléments DOM à l'intérieur d'une application web, y compris ceux créés en utilisant React.

Pour choisir un ou plusieurs éléments DOM de votre application React pour les tester, utilisez la commande `cy.get()`. Elle vous permet de sélectionner des éléments avec des sélecteurs CSS ou d'autres méthodes compatibles avec Cypress.

La syntaxe fondamentale de `cy.get()` est `cy.get(selector)`.

`selector` est une instance d'un sélecteur CSS. Il existe des moyens alternatifs pour choisir des composants basés sur des attributs comme l'ID, le nom de classe ou les données.

Supposons que vous avez un composant React comme ceci :

```javascript
<button data-testid="Leo-button">Cliquez</button>
```

Vous pouvez utiliser `cy.get()` pour sélectionner l'élément bouton :

```javascript
cy.get('[data-testid="Leo-button"]');
```

`cy.get('#Leo-button')` dans ce cas choisit l'élément bouton avec l'ID "Leo-button".

### Assertions Cypress

Ce sont des commandes Cypress qui font des assertions sur l'état de votre application. Elles arrêtent votre test lorsqu'elles atteignent la limite de temps ou que la condition spécifiée est remplie.

Il n'existe que deux types de commandes d'assertion : `.and()` et `.should()`. Je vais discuter de `.should()` ici.

Dans Cypress, les déclarations concernant les états d'éléments particuliers sont faites en utilisant la commande `.should()`. Elle vous permet de spécifier des exigences que les composants doivent remplir. Dans le cas où les exigences ne sont pas satisfaites, le test échouera.

#### Utilisation fondamentale de `.should()`

La syntaxe de base de `.should()` est la suivante :

```javascript
cy.get('selector').should('condition', expectedValue);
```

* Les éléments DOM que vous souhaitez tester sont choisis par `cy.get('selector')`.
    
* `.should('condition', expectedValue)` indique les conditions et valeurs que les éléments choisis doivent satisfaire.
    

Vous pouvez également enchaîner les assertions `.should()`. Les déclarations `.should()` enchaînées sont utilisées pour vérifier différentes conditions sur le même élément :

```javascript
cy.get('input#username')
  .should('be.visible')
  .should('have.attr', 'placeholder', 'Entrez votre nom d\'utilisateur');
```

Dans cet exemple, nous vérifions que l'élément d'entrée du nom d'utilisateur est présent et que le contenu du placeholder est approprié.

`.should()` vous permet également d'utiliser des assertions personnalisées en passant une fonction de rappel comme valeur attendue :

```javascript
cy.get('.my-element').should(($element) => {
  expect($element).to.have.class('active');
  expect($element).to.have.css('color', 'rgb(255, 0, 0)');
});
```

Dans ce code, nous utilisons des assertions personnalisées dans `.should()` pour vérifier si l'élément a la classe "active" et si sa couleur de texte est rouge.

#### Nier les assertions avec .should()

`.should('not.condition', expectedValue)` peut être utilisé pour réfuter les affirmations suivantes :

```javascript
cy.get('#error-message').should('not.exist');
```

Ce code vérifie qu'il n'y a pas d'élément avec l'ID "error-message".

#### Combiner .should() avec d'autres commandes

Pour créer des scénarios de test plus complexes, vous pouvez combiner `.should()` avec d'autres commandes Cypress. Par exemple, vous pouvez l'utiliser pour affirmer l'état final de l'élément après une commande `.click()` ou `.type()`.

```javascript
cy.get('button').click().should('be.disabled');
cy.get('[data-testid="search-input"]').type('Leonard').should('have.value', 'Leonard');
```

Dans ces cas, nous interagissons d'abord avec les éléments (en cliquant sur un bouton ou en entrant du texte dans une boîte de saisie), puis nous utilisons les états résultants des éléments tels que déterminés par l'utilisation de `.should()`.

Lorsque vous construisez des assertions pertinentes pour confirmer le comportement et l'état des éléments dans votre application web pendant les tests end-to-end, la commande `.should()` de Cypress est un outil puissant.

### Actions Cypress

Les commandes Cypress qui interagissent avec votre programme comme le ferait un utilisateur sont appelées actions. Elles n'interagissent pas avec la page jusqu'à ce que les composants ou éléments soient actionnables. Il existe de nombreux exemples, mais pour l'instant, j'utiliserai la commande `.click()`.

Pour imiter un clic sur un élément DOM dans Cypress, utilisez la commande `.click()`. C'est l'une des choses les plus typiques et basiques que vous ferez dans vos tests end-to-end.

Examinons un exemple de code pour démontrer comment utiliser `.click()` :

#### Utilisation de base de `.Click()`

La syntaxe de `.click()` est la suivante :

```javascript
cy.get('selector').click();
```

Pour choisir l'élément DOM que vous souhaitez cliquer, utilisez `cy.get('selector')`. `.click()` réplique un événement de clic sur l'élément sélectionné.

#### Gestion des clics pendant l'interaction utilisateur

Parfois, vous devrez peut-être interagir avec des éléments avant de cliquer. Par exemple, vous pourriez vouloir remplir un champ de formulaire et appuyer sur le bouton de soumission ensuite. Vous pouvez utiliser `.type()` pour communiquer avec les champs de saisie avant de continuer sur le bouton de soumission, `.click()` :

```javascript
cy.get('[data-testid="username"]').type('okosaleo');
cy.get('[data-testid="password"]').type('password');
cy.get('[data-testid="Leo-button"]').click();
```

Tout d'abord, dans ce cas, nous utilisons `.type()` pour saisir des valeurs dans les champs de mot de passe et de nom d'utilisateur, puis nous cliquons sur `.click()` pour cliquer sur le bouton de connexion et soumettre le formulaire.

#### Gestion des éléments dynamiques

Vous pouvez utiliser `.click()` tout en travaillant avec des éléments dynamiques, ou des éléments qui apparaissent après une action. Afin de vous assurer que l'élément est présent et prêt pour l'interaction, vous pouvez utiliser `.click()` en combinaison avec d'autres commandes.

Par exemple, cliquer sur un élément dynamique. Supposons que vous avez une liste d'éléments et que vous souhaitez cliquer sur un certain élément qui apparaît après une certaine quantité d'interaction utilisateur :

```javascript
cy.get('[data-testid="Leo-button"]').click();
cy.get('.dynamic-item').should('have.length.gt', 5);
cy.get('.dynamic-item').eq(4).click();
```

Dans cet exemple, pour charger de nouvelles choses dynamiquement, nous cliquons d'abord sur le bouton `"Leo-button"`. Après nous être assurés qu'au moins six choses sont affichées en utilisant `.should('have.length.gt', 5)`, nous cliquons sur le cinquième élément en utilisant `.eq(4)`.

### Autres commandes

Cypress a de nombreuses autres commandes que nous n'avons pas discutées ici, mais que vous pouvez utiliser pour écrire d'autres tests. Vous pouvez les consulter dans la [documentation Cypress ici](https://docs.cypress.io/api/table-of-contents).

## Comment organiser et exécuter vos tests Cypress

Votre application peut accumuler un certain nombre de tests au fil du temps. Cypress offre plusieurs méthodes pour les configurer et les gérer efficacement.

### Plugins

Pour aider à des tâches telles que la création de rapports de couverture de code et la simulation d'API, Cypress offre un certain nombre d'extensions et de plugins.

Les plugins sont des modules JavaScript spécialement conçus qui vous permettent de modifier et d'ajouter de nouvelles fonctionnalités au framework de test Cypress. Avec l'utilisation de plugins, vous pouvez augmenter les capacités de Cypress et le personnaliser pour répondre à vos besoins uniques.

Les plugins Cypress incluent :

1. Intégrations : Cypress peut être intégré avec d'autres programmes, services et systèmes par la création de plugins. Des exemples de ceux-ci incluent les pipelines de déploiement, les systèmes de contrôle de version et les plateformes d'intégration continue (CI).
    
2. Commandes personnalisées : Pour encapsuler et réutiliser des procédures de test de routine ou des interactions utilisateur avec votre application, vous pouvez définir des commandes personnalisées en utilisant des plugins. Cela améliore l'organisation et la maintenabilité de votre code de test.
    

Il existe de nombreuses autres fonctionnalités de plugins que Cypress offre. Les plugins sont un moyen flexible de personnaliser votre framework de test selon les besoins spécifiques de votre projet, d'augmenter la puissance de votre test et d'organiser et maintenir votre code de test de manière plus efficace.

### Blocs Describe

Le framework de test Mocha, qui est intégré avec Cypress pour vous aider à organiser et structurer vos suites de test, inclut des blocs describe. Ces blocs describe donnent à vos tests une structure claire et vous aident à regrouper des cas de test liés.

Vous pouvez utiliser des blocs describe pour catégoriser et expliquer la fonctionnalité et le comportement du programme que vous évaluez.

#### Objectif des blocs Describe dans Cypress

* Organiser les cas de test : Vous pouvez organiser les cas de test pertinents ensemble en utilisant les blocs describe. Un bloc de description peut être créé pour une fonctionnalité, une partie ou une fonctionnalité spécifique de l'application.
    
* Améliorer le framework de test : Ils donnent à vos tests un cadre hiérarchique qui rend la suite de test plus facile à explorer et à comprendre. Les développeurs et les testeurs peuvent trouver certains tests plus rapidement avec l'aide de cette structure.
    
* Clarté et documentation : Vous pouvez donner des titres à vos tests qui sont à la fois lisibles par l'homme et descriptifs en utilisant des blocs describe. Cela fonctionne comme une forme de documentation de test.
    

Un bloc `describe` est structuré comme ceci :

```javascript
describe('Description de la suite de test ou de la fonctionnalité', function () {
  // Vos cas de test (blocs it) vont ici
});
```

* `"Description de la suite de test ou de la fonctionnalité"` : Il s'agit d'une chaîne qui contient une description de la suite de test ou de la fonctionnalité. Elle agit comme le titre du groupe de cas de test.
    
* `function () { /*... */ }` : Cette fonction contient les différents cas de test qui sont liés à ce bloc `describe` et sont écrits dans des blocs `it`.
    

#### Comment utiliser les blocs Describe avec des commandes personnalisées

Supposons que vous évaluez la fonctionnalité de connexion d'une application web. Voici comment vous pourriez structurer vos tests en utilisant des blocs describe :

```javascript
describe('Fonctionnalité de connexion', function () {
  // Il s'agit du bloc describe le plus externe pour la fonctionnalité de connexion

  it('devrait afficher le formulaire de connexion', function () {
    // Logique du cas de test pour vérifier si le formulaire de connexion est affiché
  });

  it('devrait afficher un message d\'erreur en cas de connexion invalide', function () {
    // Logique du cas de test pour vérifier l\'affichage du message d\'erreur
  });

  it('devrait se connecter avec succès avec des identifiants valides', function () {
    // Logique du cas de test pour vérifier la connexion réussie
  });

  describe('Réinitialisation du mot de passe', function () {
    // Bloc describe imbriqué pour la fonctionnalité de réinitialisation du mot de passe

    it('devrait permettre aux utilisateurs de demander une réinitialisation du mot de passe', function () {
      // Logique du cas de test pour la demande de réinitialisation du mot de passe
    });

    it('devrait réinitialiser le mot de passe avec un jeton de réinitialisation valide', function () {
      // Logique du cas de test pour la réinitialisation du mot de passe avec un jeton valide
    });
  });
});
```

Dans cet exemple :

1. Tous les cas de test pour la fonctionnalité de connexion sont regroupés dans le bloc describe le plus externe.
    
2. Les tests relatifs à la fonctionnalité de réinitialisation du mot de passe sont regroupés dans un bloc describe imbriqué.
    

Vous pouvez facilement identifier les tests liés grâce à cette structure hiérarchique, qui aide également à clarifier les objectifs de chaque ensemble de cas de test.

L'utilisation efficace des blocs `describe` dans Cypress vous permet d'écrire des suites de test bien structurées et facilement accessibles, ce qui facilitera la gestion et la maintenance des tests à mesure que votre projet se développe.

### Commandes personnalisées

Pour simplifier les tâches répétitives et améliorer la lisibilité de vos tests, vous pouvez créer des commandes Cypress personnalisées.

Pour encapsuler et réutiliser des procédures de test courantes ou des interactions avec l'application testée, vous pouvez développer et ajouter des commandes personnalisées—fonctions JavaScript définies par l'utilisateur—à votre suite de test Cypress. Celles-ci peuvent aider à augmenter les commandes intégrées de Cypress et améliorer la lisibilité, l'organisation et la maintenabilité de votre code de test.

Vous devez définir votre commande personnalisée dans l'un de vos fichiers de test, généralement le fichier `commands.js`. Souvent, vous pouvez trouver ce fichier dans le répertoire `cypress/support`.

D'autre part, vous pouvez organiser vos commandes personnalisées dans différents fichiers ou dossiers selon les fonctionnalités de votre programme.

Voici un exemple :

```javascript
Cypress.Commands.add('customCommandName', (arg0, arg1, ...) => {
  // Définissez la logique de la commande personnalisée ici
});
```

* `customCommandName` : Il s'agit du nom que vous utiliserez dans vos scripts de test pour identifier votre commande personnalisée.
    
* `(arg0, arg1,...)` : Ce sont les paramètres ou arguments que vous pouvez donner à la commande personnalisée afin de modifier le comportement du programme.
    
* `// Logique de la commande personnalisée }` : Ici, vous fournissez les opérations précises que vous souhaitez voir exécutées par votre commande personnalisée.
    

#### Comment utiliser les commandes personnalisées

Une fois votre commande personnalisée définie, vous pouvez l'utiliser dans vos scripts de test de la même manière que toute autre commande Cypress intégrée.

En utilisant la syntaxe suivante, vous pouvez invoquer une commande personnalisée :

```javascript
cy.customCommandName(arg0, arg1, ...);
```

#### Avantages des commandes personnalisées

Les commandes personnalisées de Cypress présentent un certain nombre d'avantages :

1. Réutilisabilité : Vous pouvez encapsuler des interactions complexes ou couramment utilisées avec votre application en utilisant des commandes personnalisées. Cela réduit la redondance dans vos scripts de test et encourage la réutilisation du code.
    
2. Lisibilité : Vos scripts de test deviennent plus accessibles et compréhensibles lorsque des tâches typiques sont abstraites en commandes personnalisées. Votre code de test sera plus auto-explicatif avec des commandes personnalisées.
    
3. Maintenance : Plutôt que de devoir rechercher et mettre à jour chaque instance d'une action dans plusieurs scripts de test, vous n'avez besoin de modifier la commande personnalisée qu'une seule fois lorsque vous devez mettre à jour une action ou une interaction courante.
    
4. Cohérence : L'utilisation de commandes personnalisées garantit que les interactions courantes de votre suite de test sont effectuées de manière cohérente. Cela maintient la cohérence du processus de test.
    

Voici une illustration basique d'une commande personnalisée qui permet à un utilisateur de se connecter en remplissant un formulaire de connexion avec son nom d'utilisateur et son mot de passe :

```javascript
Cypress.Commands.add('login', (username, password) => {
  cy.get('[username-input]').type(username);
  cy.get('[data-testid="password-input"]').type(password);
  cy.get('[data-testid="Leo-button"]').click();
});
```

### Tableau de bord Cypress

Cet outil vous permet de surveiller les films des exécuteurs de texte, d'organiser les exécutions de test et de discuter des résultats avec votre équipe. Vous pouvez trouver le tableau de bord Cypress dans la fenêtre du test runner.

Pour voir l'historique de vos exécutions de test, cliquez sur l'onglet "Runs". L'onglet Runs contiendra un lien "View Dashboard" en haut. Lorsque vous cliquez sur le lien "View Dashboard", votre navigateur web lancera le tableau de bord Cypress.

Cypress offre le tableau de bord comme un service basé sur le web. Le but du tableau de bord Cypress est d'améliorer et de rationaliser le processus de test et de gestion des tests des applications web. Il fournit une plateforme unique pour surveiller, analyser et gérer vos exécutions de test en utilisant Cypress.

Les principales caractéristiques et capacités du tableau de bord Cypress sont les suivantes :

1. Exécution de test en temps réel : Vous pouvez observer le processus d'exécution des tests en temps réel lorsque vous utilisez le service de tableau de bord Cypress pour exécuter les tests Cypress. Il offre une vue en temps réel de vos tests, y compris avec des vidéos et des captures d'écran en direct du navigateur. Cet outil est utile pour suivre la progression des tests et résoudre les problèmes.
    
2. Collaboration et partage : Le tableau de bord permet aux équipes de développement et d'assurance qualité de collaborer. Les résultats des tests peuvent être consultés et examinés par les développeurs, les testeurs et les autres parties prenantes avec facilité lorsque les exécutions de test sont partagées avec les membres de l'équipe.
    
3. Gestion centralisée des tests : Vous pouvez stocker et gérer vos résultats de test Cypress de manière centralisée en utilisant le tableau de bord Cypress. Les exécutions de test peuvent être consultées et organisées à partir d'un seul endroit.
    
4. Le tableau de bord Cypress facilite l'exécution simultanée des tests sur plusieurs ordinateurs et navigateurs web. Cela peut accélérer considérablement le processus d'exécution des tests et vous fournir les résultats dont vous avez besoin plus rapidement.
    
5. Insights et analyses des tests : En suivant les résultats des tests au fil du temps, vous pouvez en apprendre davantage sur vos exécutions de test. Des analyses complètes, y compris les temps d'exécution, les statuts de réussite/échec, et plus encore, sont disponibles dans le tableau de bord Cypress. Vous pouvez utiliser ces données pour trouver des tendances et des motifs dans vos résultats de test.
    
6. Automatisation et planification des tests : Vous pouvez automatiser le processus de test en planifiant des tests à exécuter à des moments ou intervalles prédéterminés. L'exécution de tests de régression et le maintien d'une couverture de test continue peuvent tous deux bénéficier de cela.
    

Ce sont quelques-unes des fonctions et caractéristiques que le tableau de bord Cypress offre.

![Image](https://www.freecodecamp.org/news/content/images/2023/11/dashboard-analytics-overview.png align="left")

*Voici un exemple de ce à quoi ressemble le tableau de bord Cypress*

## Comment déboguer votre code avec Cypress

Il est simple de déboguer vos tests avec Cypress. Pour arrêter l'exécution des tests et voir l'état d'une application dans le navigateur, ajoutez `cy.debug()`. Examinons un exemple de l'utilisation de `cy.debug` dans Cypress :

```javascript
describe('Exemple de débogage Cypress', () => {
  it('effectue une connexion et vérifie le profil utilisateur', () => {
    cy.visit('/login');
    cy.get('#username-input').type('testuser');
    
    // Pause l'exécution du test pour inspecter l'état de l'application
    cy.pause();

    cy.get('#password-input').type('password123');
    cy.get('#login-button').click();

    // Continuer avec les assertions
    cy.url().should('include', '/profile');
    cy.get('.user-info').should('contain', 'Bienvenue, testuser');
  });
});
```

Dans cet exemple, le test s'arrêtera lorsqu'il atteindra la commande `cy.pause()`, et le Cypress Test Runner vous invitera à consulter la console DevTools.

Après cela, vous pouvez interagir avec le programme, examiner le DOM, vérifier les variables et exécuter d'autres commandes Cypress de manière interactive à des fins de débogage via la console.

#### Débogage par voyage dans le temps

Cypress dispose également d'une fonctionnalité puissante appelée "Débogage par voyage dans le temps". Cette fonctionnalité vous permet de voir l'état actuel de votre application à tout moment pendant qu'elle est testée. Cela simplifie grandement le processus de diagnostic.

En utilisant cette fonctionnalité, vous pouvez enregistrer et rejouer les étapes d'exécution des tests pour résoudre les problèmes de vos tests Cypress. En vous fournissant une représentation visuelle du processus d'exécution des tests étape par étape, elle vous aide à identifier et à résoudre les problèmes de vos tests et de votre application. En utilisant le développement piloté par les tests (TTD), vous pouvez voir l'état de votre application de manière interactive à différentes étapes de l'exécution des tests.

Voici comment fonctionne le débogage par voyage dans le temps de Cypress :

Vous devez d'abord enregistrer une exécution de test afin d'utiliser TTD. Vous pouvez le faire en utilisant le service de tableau de bord Cypress ou en exécutant vos tests localement avec le paramètre `--record`.

Voici un exemple de la manière de mener des tests tout en enregistrant :

```bash
npx cypress run --record
```

Le test est lancé dans le navigateur Electron par défaut.

Ensuite, vous pouvez utiliser l'interface web du tableau de bord Cypress une fois que l'exécution du test est terminée et que les résultats sont soumis au tableau de bord Cypress.

Ensuite, trouvez l'exécution du test que vous souhaitez déboguer dans le tableau de bord Cypress et cliquez dessus. Cela vous dirigera vers la page avec les détails du test.

Sur la page des détails du test, vous pouvez voir une représentation chronologique de l'état de votre application à chaque exécution de commande Cypress.

Pour voir l'état de l'application à un moment donné, cliquez sur une capture instantanée dans la chronologie. Vous pouvez parcourir les journaux de la console, travailler avec le DOM et même exécuter des commandes Cypress dans le contexte de cette capture instantanée.

Pour examiner l'état de l'application à différentes phases de test, vous pouvez soit aller à des points spécifiques dans la chronologie, soit parcourir chaque commande dans la chronologie une par une.

Voici une illustration de la manière d'appliquer TTD dans un test Cypress :

```javascript
describe('Exemple de débogage par voyage dans le temps', () => {
  it('effectue une connexion et vérifie le profil utilisateur', () => {
    cy.visit('/login');
    cy.get('[username-input]').type('testuser');
    cy.get('[password-input]').type('password');
    cy.get('[login-input]').click();

    // À ce stade, nous pourrions vouloir effectuer TTD pour inspecter l'état de l'application
    // et nous assurer que l'utilisateur est renvoyé à la page de profil.
    
    cy.url().should('include', '/profile');
    cy.get('.user-info').should('contain', 'Bienvenue, testuser');
  });
});
```

Dans ce scénario, vous pourriez rencontrer un problème que vous souhaitez diagnostiquer après avoir saisi vos informations de connexion et cliqué sur le bouton de connexion.

Pour vous assurer que l'utilisateur est sur la page de profil et que son nom est affiché correctement, vous pouvez utiliser TTD pour faire une pause à l'assertion `cy.url()` et vérifier l'état de l'application.

Avec TTD, vous pouvez examiner l'état de l'application à différents moments pour déboguer et résoudre les problèmes de vos tests Cypress de manière interactive, ce qui vous aidera à trouver et à résoudre les problèmes plus efficacement.

## Intégration continue

Les tests Cypress peuvent être intégrés dans votre workflow d'intégration continue (CI) en utilisant des solutions comme Travis CI, GitHub Actions, Jenkins ou CircleCI. Parlons de l'intégration continue en utilisant GitHub Actions :

### Intégration continue Cypress en utilisant GitHub Actions

Vous pouvez automatiser le test de vos applications web avec Cypress dans le cadre de votre workflow de développement avec l'intégration continue (CI) en utilisant GitHub Actions.

Vous pouvez créer des workflows en utilisant GitHub Actions qui automatisent une variété de processus, tels que les exécutions de tests Cypress, chaque fois que des modifications sont apportées à votre source. Passons en revue comment le configurer.

**Prérequis :**

1. Dépôt GitHub : Le code de l'application et les tests Cypress doivent être situés dans un dépôt GitHub.
    
2. Configuration Cypress : Vérifiez que Cypress est installé dans votre projet et que vos configurations de test Cypress sont exactes. Cypress Open peut être utilisé pour configurer et exécuter vos tests localement.
    

#### Étape 1 : Établir une configuration de workflow :

Créez un fichier dans votre dépôt GitHub appelé configuration de workflow. Le workflow CI est défini dans ce fichier, qui est généralement nommé `.github/workflows/cypress.yml`. Il fournit également des instructions sur quand et comment exécuter les tests Cypress.

Voici un exemple de fichier de configuration simple :

```javascript
name: Cypress Tests

on:
  push:
    branches:
      - main # Alignez avec la branche par défaut de votre dépôt

jobs:
  cypress:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v2

    - name: Install dependencies
      run: npm install

    - name: Run Cypress tests
      run: npm run cypress:run
```

Chaque fois qu'un push est effectué sur la branche `main`, un processus pour exécuter les tests Cypress est établi par ce fichier de configuration. Cela peut être modifié pour répondre à vos besoins.

#### Étape 2 : Décrire les scripts `npm` :

Définissez les scripts `npm` dans votre fichier `package.json` afin que les tests Cypress puissent être exécutés. Par exemple :

```javascript
"scripts": {
  "cypress:run": "cypress run",
  "cypress:open": "cypress open"
}
```

Alors que `cypress:open` est utilisé pour exécuter les tests de manière interactive pendant le développement, `cypress:run` est utilisé pour exécuter les tests Cypress en mode headless.

#### Étape 3 : Ajouter au dépôt GitHub

Ajoutez votre code d'application et le fichier de configuration des actions GitHub (cypress.yml) à votre dépôt GitHub. Envoyez les modifications à GitHub.

#### Étape 4 : Activer les actions GitHub :

Si vous ne l'avez pas déjà fait, allez dans votre dépôt GitHub, choisissez l'onglet "Actions" et activez les actions GitHub pour votre dépôt.

#### Étape 5 : Gérer votre processus :

Les actions GitHub lanceront le processus spécifié, qui inclut vos tests Cypress, automatiquement chaque fois que vous publierez des modifications dans votre dépôt.

#### Étape 6 : Examiner les résultats :

La page "Actions" de votre dépôt GitHub est l'endroit où vous pouvez voir l'état et les résultats de vos tests Cypress. Les résultats des tests et les journaux vous seront affichés, vous permettant de diagnostiquer et de rechercher tout problème.

### Option Headless

Cypress offre une option headless pour les tests d'intégration continue (CI). Sans le test runner Cypress, vous pouvez toujours exécuter Cypress en mode headless. En utilisant la commande `npx cypress run`, cela signifie simplement qu'il n'y a pas d'interface graphique impliquée, donc le test runner n'est pas déployé, ici nous écrivons principalement des scripts pour utiliser Cypress.

Les navigateurs web qui fonctionnent sans interface graphique, ou navigateurs headless, sont adaptés aux tests automatisés dans des contextes de serveur tels que les systèmes d'intégration continue/livraison continue.

Lorsque vous exécutez des tests Cypress en mode headless, aucune fenêtre de navigateur visible n'est affichée pendant l'exécution des tests. Cela est très utile lorsque vous testez sans interface utilisateur dans un pipeline d'intégration et de livraison continue automatisé.

Pour utiliser cela, mettez la commande `npx cypress run` dans votre terminal.

1. Cypress lancera votre test dans un navigateur electron lorsque vous exécuterez cette commande.
    
2. Une fois terminé, Cypress fournira automatiquement une vidéo de l'exécution du test et des captures d'écran en cas d'échec d'un test, facilitant ainsi le débogage.
    
3. L'utilisateur peut ajuster les captures d'écran et les vidéos. Le dossier intitulé "screenshots and videos" contient à la fois les captures d'écran et les vidéos que Cypress produit.
    

Une autre façon d'exécuter des tests est d'ajouter des scripts à votre fichier `package.json`. Vous pouvez ajouter des scripts qui consistent en une paire `clé` et `valeur` qui fonctionnent comme des objets, avec `clé` étant le nom de la commande et `valeur` étant la commande qui est exécutée.

Exécutons un test en mode headless en utilisant une paire clé-valeur :

```javascript
"script": {
    "cypress:run": "cypress run",
    "cypress:open": "cypress open"
},
```

Dans ce code, `"cypress:run"` et `"cypress:open"` sont les `clés` et `"cypress open"` et `"cypress open"` sont les commandes. Pour exécuter la commande, nous avons besoin de `npm run` suivi de la clé utilisée, par exemple : `npm cypress:run`.

Espérons que vous comprenez maintenant comment exécuter des tests en mode headless dans Cypress.

## Conclusion

Cypress est un outil efficace que vous pouvez utiliser pour tester vos applications web. Vous pouvez l'utiliser pour écrire des tests end-to-end qui garantissent que vos projets React fonctionnent comme prévu et identifient tout problème.

Cypress est un ajout utile à votre boîte à outils de test grâce à son Test Runner interactif, son API facile à utiliser et ses fonctionnalités de débogage robustes. Alors, allez-y et utilisez Cypress pour tester vos applications React afin de garantir une expérience utilisateur fluide et sans erreur.

Si vous souhaitez en savoir plus sur Cypress en détail, vous pouvez consulter leur documentation à l'adresse [cypress.io](https://www.freecodecamp.org/news/p/ee697448-b73d-43dd-85de-d31f1e1005c6/CYPRESS.IO). Bonne chance pour vos tests !