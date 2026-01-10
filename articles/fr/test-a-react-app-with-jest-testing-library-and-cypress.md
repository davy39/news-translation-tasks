---
title: Comment tester vos applications avec Jest, Testing Library, Cypress et Supertest
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-04-25T17:13:36.000Z'
originalURL: https://freecodecamp.org/news/test-a-react-app-with-jest-testing-library-and-cypress
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-rodolfo-clix-1366942.jpg
tags:
- name: Quality Assurance
  slug: quality-assurance
- name: React
  slug: react
- name: react testing library
  slug: react-testing-library
- name: Software Testing
  slug: software-testing
- name: Testing
  slug: testing
seo_title: Comment tester vos applications avec Jest, Testing Library, Cypress et
  Supertest
seo_desc: Hi everyone! In this article we're going to talk about testing. I'll give
  you a good overview of what testing is and an introduction of how you can implement
  it on your JavaScript projects. We'll use four very popular tools – Jest, Testing
  library, C...
---

Bonjour à tous ! Dans cet article, nous allons parler des tests. Je vais vous donner un bon aperçu de ce qu'est le testing et une introduction sur la façon dont vous pouvez l'implémenter dans vos projets JavaScript. Nous allons utiliser quatre outils très populaires – Jest, Testing Library, Cypress et Supertest.

Tout d'abord, nous allons parler de ce qu'est le testing, pourquoi c'est une bonne idée de tester notre code, et les différents types de tests qui peuvent être implémentés.

Ensuite, nous allons présenter chacun des outils que nous allons utiliser, et enfin nous donnerons des exemples pratiques pour du code vanilla JS, une application front-end React, et une application back-end Node.

C'est parti !

## Table des matières

* [Qu'est-ce que le testing et pourquoi est-ce précieux](#heading-questce-que-le-testing-et-pourquoi-estce-precieux)
    
* [Différents types de tests](#heading-differents-types-de-tests)
    
    * [Tests manuels vs automatisés](#heading-tests-manuels-vs-automatises)
        
    * [Tests fonctionnels vs non-fonctionnels](#heading-tests-fonctionnels-vs-non-fonctionnels)
        
    * [Tests unitaires vs d'intégration vs de bout en bout](#heading-tests-unitaires-vs-dintegration-vs-de-bout-en-bout)
        
    * [Tests boîte blanche vs boîte noire vs boîte grise](#heading-tests-boite-blanche-vs-boite-noire-vs-boite-grise)
        
* [Quand tester](#heading-quand-tester)
    
* [Notre boîte à outils](#heading-notre-boite-a-outils)
    
    * [Qu'est-ce que Jest](#heading-questce-que-jest)
        
    * [Qu'est-ce que Testing Library](#heading-questce-que-testing-library)
        
    * [Qu'est-ce que Cypress](#heading-questce-que-cypress)
        
    * [Qu'est-ce que Supertest](#heading-questce-que-supertest)
        
    * [Résumé des outils](#heading-resume-des-outils)
        
* [Comment tester du code vanilla JS](#heading-comment-tester-du-code-vanilla-js)
    
* [Comment tester une application front-end React avec Jest et React Testing Library](#heading-comment-tester-une-application-frontend-react-avec-jest-et-react-testing-library)
    
* [Comment tester une application front-end React avec Cypress](#heading-comment-tester-une-application-frontend-react-avec-cypress)
    
* [Comment tester une application back-end Node](#heading-comment-tester-une-application-backend-node)
    
* [Conclusion](#heading-conclusion)
    

# Qu'est-ce que le Testing et Pourquoi est-ce Précieux

Le testing est la pratique de vérifier si un morceau de logiciel fonctionne comme prévu. Cela est souvent reconnu comme QA ou assurance qualité, et vise à réduire au minimum le nombre de bugs qui atteignent la production.

Nous testons le logiciel pour identifier les erreurs, les lacunes ou les exigences manquantes et corriger ces choses avant de livrer le code en production.

Tester notre code de manière approfondie améliore la fiabilité de notre projet, nous fait gagner du temps de correction de bugs plus tard et réduit donc les coûts, et améliore les chances que notre client soit pleinement satisfait de notre produit.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/BvIJ1M5-1.gif align="left")

[Voici une courte vidéo sympa de Fireship](https://www.youtube.com/watch?v=u6QfIXgjwGQ&t=6s) introduisant certains des concepts dont nous parlerons plus tard.

# Différents Types de Tests

Les pratiques de test peuvent être classées en différents types selon de nombreux facteurs. Personnellement, je pense qu'il y a beaucoup de charabia à ce sujet, avec des centaines de termes qui font souvent référence à des choses très similaires. Alors gardons cela simple et passons en revue uniquement les termes les plus populaires et ce qu'ils signifient.

Cela aidera à clarifier les nombreuses façons dont un logiciel peut être testé et à mieux comprendre les outils que nous allons présenter plus tard.

### Tests manuels vs automatisés

Selon les outils que nous utilisons pour tester notre logiciel, nous pouvons classer les tests en **manuels** ou **automatisés**.

Les **tests manuels** consistent à "cliquer autour" et à vérifier manuellement toutes les fonctionnalités de notre produit, en simulant ce qu'un utilisateur réel ferait.

Les **tests automatisés** sont effectués via du code, en écrivant des programmes qui vérifient comment notre application fonctionne.

Il existe de nombreux frameworks et bibliothèques de test que nous pouvons utiliser pour cela. En ce qui concerne les tests fonctionnels (nous allons voir ce que cela signifie dans un instant), la plupart des bibliothèques fonctionnent de manière similaire :

* D'abord, nous **définissons** quel morceau de code nous voulons tester.
    
* Ensuite, nous fournissons à ce morceau de code une sorte d'**entrée** ou exécutons une **action** sur celui-ci.
    
* Ensuite, nous définissons ce que ce morceau de code **devrait faire** étant donné l'entrée/action que nous avons effectuée.
    
* Et enfin, nous allons **comparer** ce que ce morceau de code a réellement fait par rapport à ce que nous avons dit qu'il devrait faire.
    

S'il a fait ce que nous avons dit qu'il devrait faire, le test a réussi. Sinon, il a échoué.

### Tests fonctionnels vs non-fonctionnels

Les tests **fonctionnels** font référence aux **fonctionnalités réelles de notre produit**. Par exemple, si nous avons une plateforme de blog, les tests fonctionnels doivent assurer que les utilisateurs peuvent créer de nouveaux articles, modifier ces articles, parcourir les articles écrits par d'autres personnes, et ainsi de suite.

Les tests **non-fonctionnels** font référence à tout ce qui n'est **pas strictement lié aux fonctionnalités principales** de notre produit. Et cela peut être classé en différentes catégories, par exemple :

* Les **tests de stress** vérifient comment l'infrastructure répond à une utilisation intensive.
    
* Les **tests de sécurité** vérifient si une application est vulnérable aux attaques de piratage courantes.
    
* Les **tests d'accessibilité** vérifient si une application est codée de manière à être accessible aux personnes ayant différents handicaps.
    

### Tests unitaires vs d'intégration vs de bout en bout

Une autre façon de classer les tests est de savoir à quel point ils sont larges ou complets.

Les **tests unitaires** visent à tester des fonctions individuelles, des méthodes ou de petits morceaux de code de manière indépendante. Dans les tests unitaires, de petits morceaux de code sont vérifiés de manière isolée.

Les **tests d'intégration** vérifient comment les morceaux individuels de code interagissent les uns avec les autres et fonctionnent ensemble. Dans les tests d'intégration, nous mettons les morceaux ensemble et voyons s'ils interagissent correctement.

Les **tests de bout en bout**, également connus sous le nom de E2E, exécutent des programmes dans un environnement simulé qui émule le comportement réel de l'utilisateur. Prenons un site web comme exemple, notre code s'ouvrirait dans un navigateur réel et toutes les fonctionnalités seraient exécutées de la même manière qu'un utilisateur les utiliserait. Les tests E2E ressemblent beaucoup aux tests manuels à cet égard, mais sont entièrement automatisés.

Les tests E2E sont le type le plus large ou le plus complet de ces trois, car ils évaluent des fonctionnalités et des comportements entiers, et non des parties spécifiques de notre code.

### Tests boîte blanche vs boîte noire vs boîte grise

La dernière classification que nous allons voir dépend de la mesure dans laquelle nos tests se concentrent sur les détails d'implémentation ou l'expérience utilisateur.

Disons que nous avons un site web simple avec un bouton qui, lorsqu'il est cliqué, ouvre une modale. Dans notre code, le bouton a un écouteur d'événement de clic qui exécute une fonction. Cette fonction change la classe CSS de notre élément HTML modal, et cela fait que la modale est rendue à l'écran.

Nous parlons de tests "**boîte blanche**" lorsque nous testons les **détails d'implémentation**. En suivant l'exemple, sous ce paradigme, nous pourrions tester que le clic sur le bouton exécute la fonction correspondante, et qu'après l'exécution de la fonction, la classe CSS de notre élément modal est changée en conséquence.

Une autre façon de faire cela est d'oublier complètement l'implémentation et de simplement vérifier si la modale est rendue après le clic sur le bouton. Nous ne nous soucions pas de savoir quelle est la classe CSS, ou si la fonction correspondante est exécutée ou non. Nous nous concentrons uniquement sur le test de **ce que l'utilisateur devrait percevoir**. C'est ce qu'on appelle le test "**boîte noire**".

Et, comme vous l'avez peut-être deviné, le test "boîte grise" est simplement une combinaison des deux précédents.

Une dernière chose à mentionner ici est que ces différents types de tests ne sont pas nécessairement mutuellement exclusifs. Je veux dire, ils peuvent et sont souvent implémentés en même temps sur les mêmes projets.

Il est très courant d'avoir à la fois des tests manuels et automatisés, des tests fonctionnels et non-fonctionnels, des tests unitaires et E2E... L'idée sera toujours d'essayer d'anticiper et de résoudre le plus grand nombre possible de problèmes en un temps et un effort raisonnables.

# Quand Tester

Cela peut sembler une question simple au premier abord, mais il existe en réalité différentes approches à ce sujet, également.

Certaines personnes aiment tester leur application une fois qu'elle a été entièrement développée. D'autres aiment écrire des tests en même temps qu'ils codent l'application, et tester chaque fonctionnalité au fur et à mesure de son développement.

D'autres aiment écrire des tests d'abord avant toute autre chose, définissant de cette manière les exigences minimales pour que le programme les accomplisse. Ensuite, ils codent l'application de manière à ce qu'elle passe ces tests le plus rapidement possible (c'est ce qu'on appelle le [développement piloté par les tests ou TDD](https://en.wikipedia.org/wiki/Test-driven_development)).

Une fois que vous avez une application ou une fonctionnalité entière développée, et que vous avez une suite de tests en place (une suite de tests est un groupe de tests qui vérifient une fonctionnalité particulière ou une application entière), une autre pratique courante consiste à exécuter vos tests chaque fois que vous apportez une modification quelconque à la base de code, afin de vérifier que rien ne se casse.

Enfin, si vous avez un système [CI/CD](https://en.wikipedia.org/wiki/CI/CD) en place, il est courant d'automatiser l'exécution des tests avant tout déploiement. Ainsi, si un test échoue, le déploiement est arrêté et une sorte d'alerte est envoyée (ce qui est bien sûr toujours mieux que de voir votre application prendre feu en production 🔥😱).

Comme pour les types de tests, il est courant de tester les applications à différents moments. Chaque entreprise a généralement son propre calendrier ou pratique de test à suivre, adapté à ses besoins.

# Notre Boîte à Outils

D'accord, maintenant que nous avons une idée plus claire de ce qu'est le testing et des types de tests que nous pouvons effectuer, passons en revue les outils que nous allons utiliser dans nos exemples.

Comme mentionné précédemment, il existe de nombreuses bibliothèques différentes à choisir pour exécuter nos tests. J'ai choisi ces quatre parce qu'elles sont parmi les plus populaires lorsqu'il s'agit d'applications JavaScript, mais sachez qu'il existe d'autres options. Je mentionnerai des alternatives pour la plupart des outils que nous utiliserons au cas où vous souhaiteriez en savoir plus. 😉

## Qu'est-ce que Jest

[Jest](https://jestjs.io/) est un test-runner JavaScript. Un test-runner est un morceau de logiciel qui vous permet d'exécuter des tests pour évaluer votre application. C'est un projet open-source maintenu par Meta (anciennement Facebook), et a été open-sourcé pour la première fois en 2014.

Commentaire de côté : Chaque fois que je dis "test runner", je m'imagine cela. Suis-je le seul ? 🤔

![Image](https://www.freecodecamp.org/news/content/images/2022/04/8gTI-1.gif align="left")

*Test runner, pas Blade runner !*

En tout cas... vous pouvez utiliser Jest dans des projets qui utilisent [Babel](https://babeljs.io/), [TypeScript](https://www.typescriptlang.org/), [Node.js](https://nodejs.org/en/), [React](https://reactjs.org/), [Angular](https://angular.io/), [Vue.js](https://vuejs.org/), [Svelte](https://svelte.dev/) et d'autres technologies également. Vous pouvez installer Jest via NPM comme n'importe quelle bibliothèque et il nécessite très peu de configuration pour commencer.

Jest est installé par défaut lors de la configuration des applications React avec [create-react-app](https://create-react-app.dev/).

Jest est souvent également appelé un framework de test, car il vient avec de nombreuses autres fonctionnalités intégrées en plus de simplement exécuter des tests (ce qui n'est pas le cas avec tous les test runners). Certaines de ces fonctionnalités sont :

* **Bibliothèque d'assertion :** Jest vient avec beaucoup de fonctions et méthodes intégrées que vous pouvez utiliser pour assert votre code (assert signifie essentiellement vérifier si un morceau de code se comporte comme prévu).
    
* **Tests de snapshot :** Jest vous permet d'utiliser des snapshots, qui sont un moyen de capturer un grand objet et de le stocker en mémoire afin que vous puissiez ensuite le comparer avec autre chose.
    
* **Couverture de code :** Jest vous permet d'obtenir des rapports de couverture de code de vos tests. Ces rapports montrent quel pourcentage de votre code est actuellement testé, et vous pouvez même voir les lignes exactes de code qui ne sont pas actuellement couvertes.
    
* **Bibliothèque de mocking :** Jest fonctionne également comme une bibliothèque de mocking dans le sens où il vous permet de mock des données (comme une fonction ou un module) et de les utiliser dans vos tests.
    

Quelques alternatives bien connues à Jest sont [Mocha](https://mochajs.org/), [Jasmine](https://jasmine.github.io/), et [Karma](https://karma-runner.github.io/latest/index.html).

Voici [une petite vidéo sympa](https://www.youtube.com/watch?v=SyHzgcFefBk) expliquant ce qu'est Jest.

## Qu'est-ce que Testing Library ?

Testing Library n'est pas un test runner, mais un ensemble d'utilitaires qui fonctionneront avec un test runner comme Jest ou Mocha. Ces utilitaires sont des outils que nous pouvons utiliser pour tester notre code facilement et avec un accent plus marqué sur l'expérience utilisateur (tests boîte noire).

Testing Library a été développé par [Kent C Dodds](https://kentcdodds.com/) (qui est également l'un des meilleurs enseignants JS sur terre, donc je vous recommande de le suivre).

En citant [la documentation officielle :](https://testing-library.com/)

> *"La famille de bibliothèques Testing Library est une solution très légère pour tester sans tous les détails d'implémentation.*
> 
> *Les principales utilités qu'elle fournit impliquent des requêtes pour des nœuds de manière similaire à la façon dont les utilisateurs les trouveraient. De cette manière, testing-library aide à garantir que vos tests vous donnent confiance dans votre code UI."*

En anglais simple, avec la bibliothèque de test, nous pouvons tester des éléments UI (comme un paragraphe, un bouton, une div...) au lieu de tester le code responsable du rendu de l'UI.

Le principe derrière la bibliothèque est :

> *"Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils peuvent vous donner confiance."*

... et c'est exactement ce que nous entendons par "tests boîte noire". 😉

La bibliothèque de test est en fait un **ensemble de bibliothèques**, chacune créée pour atteindre le même objectif mais adaptée pour fonctionner avec différentes technologies telles que React, Angular, Vue, Svelte, React Native et plus... C'est pourquoi vous pourriez entendre "React-testing-library" ou "Vue-testing-library". C'est la même chose mais adaptée pour fonctionner avec différentes technologies.

React-testing-library est installé par défaut lors de la configuration des applications React avec [create-react-app](https://create-react-app.dev/).

Une alternative à testing library est [Enzyme](https://enzymejs.github.io/enzyme/) (un ensemble d'utilitaires de test UI développé par Airbnb).

## Qu'est-ce que Cypress ?

Cypress est un test-runner open source qui vous permet d'exécuter vos projets dans un navigateur automatisé, de la même manière qu'un utilisateur le ferait.

Avec Cypress, nous pouvons programmer ce que le navigateur fera (comme visiter une URL, cliquer sur un bouton, remplir et soumettre un formulaire...) et vérifier que chaque action est associée à la réponse correspondante.

Ce qui est génial avec cela, c'est que le test ressemble BEAUCOUP à ce que l'utilisateur expérimentera. Et puisque le but de créer un logiciel est l'utilisateur, plus nous sommes proches de leur perspective, plus nous devrions être proches de capturer les bugs les plus significatifs dans notre code. (En plus, c'est vraiment cool de voir un navigateur automatisé parcourir toute votre application en quelques secondes... 🤓)

Une autre fonctionnalité sympa de Cypress est le "time travel". Dans le navigateur automatisé de Cypress, nous pouvons voir tous les tests que nous avons écrits, et simplement survoler pour voir un snapshot graphique de son résultat. C'est une chose très utile pour mieux comprendre ce qui casse et quand.

Bien qu'il puisse être utilisé pour les tests unitaires et d'intégration, Cypress est principalement utilisé pour les tests de bout en bout car il peut facilement évaluer des fonctionnalités complètes en quelques secondes.

Vous pouvez utiliser Cypress pour tester tout ce qui s'exécute dans un navigateur, donc vous pouvez facilement l'implémenter sur React, Angular, Vue, et ainsi de suite.

Contrairement à Jest et React-Testing-Library, Cypress n'est pas préinstallé avec create-react-app. Mais nous pouvons facilement l'installer avec NPM ou votre gestionnaire de paquets de choix.

Quelques alternatives à Cypress sont [Selenium](https://www.selenium.dev/) et [Puppeteer](https://pptr.dev/).

[Voici une vidéo sympa de Fireship expliquant ce qu'est Cypress et comment il fonctionne.](https://www.youtube.com/watch?v=BQqzfHQkREo)

Commentaire de côté : ... et chaque fois que je parle de Cypress [cela joue dans mon esprit](https://www.youtube.com/watch?v=BV3CYz34ziE). 😎

## Qu'est-ce que Supertest ?

[Supertest](https://github.com/visionmedia/supertest) est une bibliothèque qui simule les requêtes HTTP. C'est super pratique pour tester les applications back-end Node avec Jest (comme nous allons le voir dans les exemples à venir).

### Résumé des outils

En résumé sur ce sujet :

* Jest est la bibliothèque que nous utiliserons pour écrire et exécuter des tests pour JavaScript.
    
* Testing Library fonctionne avec Jest et nous fournit des fonctions et méthodes pour tester l'UI directement, en oubliant le code derrière.
    
* Cypress exécute votre application dans un navigateur simulé et vérifie si les actions effectuées dans l'UI répondent comme prévu.
    
* Supertest est une bibliothèque qui simule les requêtes HTTP et peut être utilisée avec Jest pour tester les applications back-end.
    

Maintenant, commençons avec la partie amusante...

![Image](https://www.freecodecamp.org/news/content/images/2022/04/giphy-2.gif align="left")

*Que les tests commencent !*

# Comment Tester du Code Vanilla JS

D'accord, commençons par tester un peu de code vanilla JS simple. L'idée ici est de voir comment nous pouvons implémenter Jest dans notre projet et apprendre les bases de son fonctionnement.

Commençons par créer un nouveau répertoire sur notre machine et créer une application Node avec `npm init -y`. Ensuite, installez Jest en exécutant `npm i -D jest` (`-D` l'enregistre comme une dépendance de développement).

Maintenant, vous devriez voir quelque chose comme ceci dans votre fichier `package.json` : `"devDependencies": { "jest": "^27.5.1" }` .

Et en parlant de cela, dans votre `package.json`, remplacez votre script `test` par `"test": "jest"`. Cela nous permettra d'exécuter nos tests plus tard en exécutant `npm test`. ;)

Votre fichier `package.json` complet devrait ressembler à ceci :

```plaintext
{
  "name": "vanillatesting",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "jest"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "jest": "^27.5.1"
  }
}
```

Cool, nous sommes prêts à écrire un peu de JS que nous pouvons réellement tester ! Créez un fichier `index.js` et mettez ce code dedans :

```plaintext
// index.js
function isPalindrome(string) {
    // O(n)
    // Placez un pointeur à chaque extrémité du mot et itérez "vers l'intérieur"
    // À chaque itération, vérifiez si les pointeurs représentent des valeurs égales
    // Si cette condition n'est pas remplie, le mot n'est pas un palindrome
    let left = 0
    let right = string.length-1
  
    while (left < right) {
        if (string[left] === string[right]) {
            left += 1
            right -= 1
        }
        else return false
    }
  
    return true
}
```

Cette fonction est un vérificateur de [palindrome](https://en.wikipedia.org/wiki/Palindrome). Elle reçoit une chaîne comme paramètre et retourne `true` si la chaîne est un palindrome et `false` si ce n'est pas le cas. (C'est une question classique d'entretien technique d'ailleurs, mais c'est un sujet pour un autre article.🤛)

Voyez que nous exportons également la fonction. Commentaire de côté : Si vous souhaitez en savoir plus sur cela et sur le fonctionnement des modules JS, j'ai récemment écrit [un article](https://www.freecodecamp.org/news/modules-in-javascript) à ce sujet.

Super, alors maintenant testons cette fonction et voyons si elle fonctionne comme prévu. Créons un fichier appelé `index.test.js`.

Ce fichier est celui où nous allons écrire nos tests. Le suffixe que nous utilisons (`.test.js`) est important ici, car Jest identifiera automatiquement les fichiers `.test` et les exécutera lorsque nous demanderons à Jest de tester notre projet.

Jest identifie également les fichiers avec le suffixe `.spec`, comme `index.spec.js` (pour "specification", qui fait référence aux exigences de votre projet). Personnellement, je préfère `.test` car cela me semble plus explicite, mais les deux fonctionnent de la même manière.

Maintenant, écrivons nos premiers tests ! Mettez ceci dans votre fichier `index.test.js`.

```plaintext
// index.test.js
isPalindrome = require('./index.js')

test('neuquen est un palindrome', () => {
    expect(isPalindrome("neuquen")).toBe(true)
})

test('bariloche nest pas un palindrome', () => {
    expect(isPalindrome("bariloche")).toBe(false)
})
```

Récapitulons ce que nous faisons réellement :

1. Requérir la fonction que nous voulons tester : `isPalindrome = require('./index.js')`
    
2. La fonction `test()` est fournie par Jest et dans celle-ci nous mettrons le code que nous voulons que Jest exécute.
    
3. `test()` prend deux paramètres. Le premier est une description de test, qui est un nom distinctif qui s'affichera sur notre console lorsque le test sera exécuté. Nous verrons un exemple dans un instant.
    
4. Le deuxième paramètre est un callback, qui contient le code de test réel.
    
5. Dans ce callback, nous appelons la fonction `expect()` (également fournie par Jest). `expect()` prend notre fonction comme paramètre, qui elle-même reçoit un paramètre que nous avons inventé.
    
6. Enfin, nous enchaînons la fonction `.toBe()` (fournie par Jest également) et comme paramètre, nous lui passons la valeur que nous attendons de `isPalindrome()` pour chaque cas. ("neuquen" est un palindrome donc notre fonction devrait retourner `true`, et "bariloche" ne l'est pas, donc elle devrait retourner `false`.)
    

L'une des choses que j'aime le plus chez Jest est la facilité avec laquelle il peut être configuré. Une autre chose que j'aime beaucoup est la clarté de sa syntaxe. Remarquez que nous pouvons facilement comprendre ce que nos tests vont évaluer simplement en les lisant.👍

Maintenant, essayons cela ! Si nous exécutons `npm test` dans notre console, nous devrions obtenir ce qui suit :

```plaintext
// console
> jest PASS 
./index.test.js
✓ neuquen est un palindrome (1 ms)
✓ bariloche nest pas un palindrome

Test Suites: 1 passed, 1
total Tests:       2 passed, 2
total Snapshots:   0
total Time:        0.244 s
Ran all test suites.
```

Félicitations, vous venez de réussir votre premier test Jest.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/mr-miyagi-nod-1.gif align="left")

![Image](https://www.freecodecamp.org/news/content/images/2022/04/lets-get-this-party-started-yeah-1.gif align="left")

Pour voir à quoi ressemble également un test échoué, modifions notre fonction en éditant les lignes `return`.

```plaintext
// index.js
function isPalindrome(string) {
    // O(n)
    // Placez un pointeur à chaque extrémité du mot et itérez "vers l'intérieur"
    // À chaque itération, vérifiez si les pointeurs représentent des valeurs égales
    // Si cette condition n'est pas remplie, le mot n'est pas un palindrome
    let left = 0
    let right = string.length-1
  
    while (left < right) {
        if (string[left] === string[right]) {
            left += 1
            right -= 1
        }
        else return 1
    }
  
    return 2
}
```

Maintenant, vous devriez obtenir quelque chose comme ceci :

```plaintext
// console
> vanillatesting@1.0.0 test
> jest

 FAIL  ./index.test.js
  ✕ neuquen est un palindrome (4 ms)
  ✕ bariloche nest pas un palindrome

  ● neuquen est un palindrome

    expect(received).toBe(expected) // Object.is equality

    Expected: true
    Received: 2

      3 | // describe('isPalindrome function', () => {
      4 |   test('neuquen est un palindrome', () => {
    > 5 |     expect(isPalindrome("neuquen")).toBe(true)
        |                                     ^
      6 |   })
      7 |
      8 |   test('bariloche nest pas un palindrome', () => {

      at Object.<anonymous> (index.test.js:5:37)

  ● bariloche nest pas un palindrome

    expect(received).toBe(expected) // Object.is equality

    Expected: false
    Received: 1

       7 |
       8 |   test('bariloche nest pas un palindrome', () => {
    >  9 |     expect(isPalindrome("bariloche")).toBe(false)
         |                                       ^
      10 |   })
      11 | // })
      12 |

      at Object.<anonymous> (index.test.js:9:39)

Test Suites: 1 failed, 1 total
Tests:       2 failed, 2 total
Snapshots:   0 total
Time:        0.28 s, estimated 1 s
Ran all test suites.
```

Voyez que vous obtenez une description agréable de ce qui a échoué et à quel point cela a échoué. Dans notre cas, ils ont échoué lorsque nous avons asserté (vérifié) les valeurs de retour.

C'est très utile et nous devrions toujours prêter attention à ces descriptions, car parfois nos tests peuvent échouer parce qu'ils ne sont pas écrits correctement. Et nous n'écrivons pas normalement de tests pour nos tests, pas encore... 😅 Donc lorsque vous voyez un test échouer, vérifiez d'abord qu'il fonctionne comme prévu, puis allez revoir votre code réel.

Maintenant, ajoutons et testons une autre fonction pour montrer quelques fonctionnalités supplémentaires de Jest :

```plaintext
// index.js
function twoSum(nums, target) {
    // O(n)
    // Parcourez le tableau une fois
    // À chaque itération, calculez la valeur nécessaire pour atteindre la cible, qui est target - currentValue
    // Si la neededValue existe dans le tableau, retournez [currentValue, neededValue], sinon continuez l'itération
	for (let i = 0; i < nums.length; i++) {
		const neededNum = target - nums[i]
		if (nums.indexOf(neededNum) !== -1 && nums.indexOf(neededNum) !== i) return [nums[i], nums[nums.indexOf(neededNum)]]
	}
    return false
}

module.exports = { isPalindrome, twoSum }
```

C'est une autre question classique d'entretien. La fonction prend deux paramètres, un tableau de nombres et une valeur cible. Ce qu'elle fait, c'est identifier s'il y a deux nombres dans le tableau qui additionnés donnent la valeur du deuxième paramètre. Si les deux valeurs existent dans le tableau, elle les retourne dans un tableau, et si ce n'est pas le cas, elle retourne false.

Maintenant, écrivons quelques tests pour cela :

```plaintext
({ isPalindrome, twoSum } = require('./index.js'))

...

test('[2,7,11,15] et 9 retourne [2, 7]', () => {
    expect(twoSum([2,7,11,15], 9)).toEqual([2,7])
})

test('[3,2,4] et 6 retourne [2, 4]', () => {
    expect(twoSum([3,2,4], 6)).toEqual([2,4])
})

test('[3,2,4] et 10 retourne false', () => {
    expect(twoSum([3,2,4], 10)).toBe(false)
})
```

Voyez que la structure est presque la même, sauf que nous utilisons un **matcher** différent dans deux des tests, `toEqual()`.

Les **Matchers** sont les fonctions que Jest nous fournit pour évaluer les valeurs. Il existe de nombreux types de matchers qui peuvent être utilisés pour de nombreuses occasions différentes.

Par exemple, `.toBe()` est utilisé pour évaluer les primitives comme les chaînes, les nombres ou les booléens. `toEqual()` est utilisé pour évaluer les objets (ce qui couvre à peu près tout le reste en Javascript).

Si vous devez comparer la valeur de retour avec un nombre, vous pourriez utiliser `.toBeGreaterThan()` ou `toBeGreaterThanOrEqual()` et ainsi de suite...

Pour voir une liste complète des matchers disponibles, [consultez la documentation](https://jestjs.io/docs/using-matchers).

Si nous exécutons nos tests maintenant, nous obtiendrons ce qui suit :

```plaintext
> vanillatesting@1.0.0 test
> jest

 PASS  ./index.test.js
  ✓ neuquen est un palindrome (2 ms)
  ✓ bariloche nest pas un palindrome
  ✓ [2,7,11,15] et 9 retourne [2, 7] (1 ms)
  ✓ [3,2,4] et 6 retourne [2, 4]
  ✓ [3,2,4] et 10 retourne false (1 ms)

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        0.256 s, estimated 1 s
Ran all test suites.
```

C'est cool, mais nos résultats de tests semblent un peu désordonnés. Et à mesure que notre suite de tests grandit, il sera probablement plus difficile d'identifier chaque résultat séparé.

Pour nous aider avec cela, Jest nous fournit une fonction `describe()`, que nous pouvons utiliser pour regrouper les tests ensemble et afficher les résultats de manière plus schématique. Nous pouvons l'utiliser comme ceci :

```plaintext
({ isPalindrome, twoSum } = require('./index.js'))

describe('fonction isPalindrome', () => {
  test('neuquen est un palindrome', () => {
    expect(isPalindrome("neuquen")).toBe(true)
  })

  test('bariloche nest pas un palindrome', () => {
    expect(isPalindrome("bariloche")).toBe(false)
  })
})

describe('fonction twoSum', () => {
  test('[2,7,11,15] et 9 retourne [2, 7]', () => {
    expect(twoSum([2,7,11,15], 9)).toEqual([2,7])
  })

  test('[3,2,4] et 6 retourne [2, 4]', () => {
    expect(twoSum([3,2,4], 6)).toEqual([2,4])
  })

  test('[3,2,4] et 10 retourne false', () => {
    expect(twoSum([3,2,4], 10)).toBe(false)
  })
})
```

Le premier paramètre est la description que nous voulons afficher pour le groupe de tests donné, et le second est un callback qui contient nos tests. Maintenant, si nous exécutons `npm test` à nouveau, nous obtenons ceci 😎:

```plaintext
// console
> vanillatesting@1.0.0 test
> jest

 PASS  ./index.test.js
  fonction isPalindrome
    ✓ neuquen est un palindrome (2 ms)
    ✓ bariloche nest pas un palindrome
  fonction twoSum
    ✓ [2,7,11,15] et 9 retourne [2, 7] (1 ms)
    ✓ [3,2,4] et 6 retourne [2, 4]
    ✓ [3,2,4] et 10 retourne false

Test Suites: 1 passed, 1 total
Tests:       5 passed, 5 total
Snapshots:   0 total
Time:        0.216 s, estimated 1 s
Ran all test suites.
```

# Comment Tester une Application Front-end React avec Jest et React Testing Library

Maintenant que nous connaissons les bases de Jest, passons à la façon dont nous pouvons le combiner avec Testing Library pour tester une application React.

Pour cela, nous allons utiliser un exemple très simple. Juste une page avec du texte aléatoire, un bouton qui bascule un autre morceau de texte, une entrée de texte, et un bouton qui bascule le rendu de l'entrée.

![Image](https://www.freecodecamp.org/news/content/images/2022/04/Recording-2022-04-23-at-21.11.24.gif align="left")

Prenez en compte que nous utiliserons [create-react-app](https://create-react-app.dev/) pour créer cette application (qui a Jest et Testing Library installés par défaut). Si vous n'utilisez pas create-react-app, vous devrez peut-être installer les deux bibliothèques et ajouter une configuration supplémentaire.

Nous ne allons pas voir de code React ici, nous allons simplement nous concentrer sur les tests.

La structure des dossiers de notre projet est la suivante :

```plaintext
> src
    > components
        - About.jsx
    - App.jsx
    - Index.js
    - setupTests.js
```

Le fichier `setupTests.js` est important ici. Il est créé par défaut avec create-react-app avec ce contenu :

```plaintext
// jest-dom ajoute des matchers jest personnalisés pour assert sur les nœuds DOM.
// permet de faire des choses comme :
// expect(element).toHaveTextContent(/react/i)
// en savoir plus : https://github.com/testing-library/jest-dom
import '@testing-library/jest-dom';
```

Il importe globalement la bibliothèque `jest-dom` fournie par Testing Library, qui nous donne des matchers Jest supplémentaires que nous pouvons utiliser pour tester le DOM (comme `toHaveTextContent(), toBeInTheDocument()`, etc).

Nous allons voir des exemples dans un instant, mais sachez que certaines des fonctions et matchers que nous utiliserons viennent de là.

En ce qui concerne nos fichiers de tests, la pratique courante est d'avoir un fichier de test différent pour chaque composant que nous testons.

En ce qui concerne l'endroit où les placer, deux pratiques courantes consistent à les avoir tous ensemble dans un seul dossier, comme `__tests__` ou similaire, ou à avoir chaque fichier de test dans le même dossier que le composant qu'il teste.

Je préfère cette dernière option car je passe souvent du code du composant au code de test, et il est agréable de les avoir à proximité. Mais en vérité, cela n'a pas d'importance. Tant que nous utilisons les suffixes `.test` ou `.spec`, Jest identifiera et exécutera les fichiers de toute façon.

Ayant créé nos fichiers de tests, notre structure de dossiers devrait ressembler à ceci :

```plaintext
> src
    > components
        - About.jsx
        - About.test.jsx
    - App.jsx
    - Index.js
    - setupTests.js
```

Super ! Commençons par tester notre composant `About`.

Tout d'abord, testons qu'il se rend correctement, comme ceci :

```plaintext
// About.test.jsx
import { render, screen } from '@testing-library/react'
import About from './About'

describe('About', () => {

  test('About se rend correctement', () => {
    render( <About/> )
    expect(screen.getByText("Je suis la page à propos !")).toBeInTheDocument()
  })

})
```

* Voyez que nous commençons par importer deux choses de Testing Library : `import { render, screen } from '@testing-library/react'`.
    

La fonction `render` prend un composant React comme paramètre et le rendra afin que nous puissions le tester.

`screen` est un objet qui contient de nombreuses requêtes que nous pouvons utiliser pour tester l'UI directement, en sautant les détails d'implémentation et en nous concentrant sur ce que l'utilisateur verra réellement.

* Ensuite, nous importons notre composant `About` : `import About from './About'`
    
* Nous utilisons les fonctions `describe` et `test` de Jest mentionnées précédemment.
    
* Nous rendons le composant `About` : `render( <About/> )`
    
* Nous utilisons la fonction `expect` de Jest, et comme paramètre, nous utilisons l'objet `screen` fourni par Testing Library. Nous utilisons sa requête `getByText`, qui scanne le composant React pour le texte que nous passons comme paramètre.
    
* Pour finir, nous utilisons le matcher `.toBeInTheDocument()` de Testing Library, qui vérifie simplement si le résultat de la requête précédente est rendu.
    

Ensuite, nous pouvons tester que le bouton bascule "Switch state" fonctionne correctement, comme ceci :

```plaintext
// About.test.jsx
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import About from './About'

describe('About', () => {

  ...

  test('Switch state fonctionne correctement', async () => {
    render( <About/> )

    expect(screen.getByText("C'est allumé !")).toBeInTheDocument()
    userEvent.click(screen.getByText('Changer d'état'))
    expect(screen.getByText("C'est en cours !")).toBeInTheDocument()
    userEvent.click(screen.getByText('Changer d'état'))
    expect(screen.getByText("C'est allumé !")).toBeInTheDocument()
  })

})
```

Voyez que nous importons une utilité supplémentaire appelée `userEvent`. Il s'agit d'un objet qui contient de nombreuses méthodes que nous pouvons utiliser pour simuler des événements déclenchés par l'utilisateur, comme des clics, des survols, l'écriture dans une entrée, et ainsi de suite.

* Nous vérifions d'abord que la chaîne par défaut est rendue : `expect(screen.getByText("C'est allumé !")).toBeInTheDocument()`
    
* Ensuite, nous simulons un clic et vérifions que la chaîne change à l'écran :
    

```plaintext
userEvent.click(screen.getByText('Changer d'état'))
expect(screen.getByText("C'est en cours !")).toBeInTheDocument()
```

* Et enfin, nous simulons un autre clic et vérifions que la chaîne revient à la valeur par défaut :
    

```plaintext
userEvent.click(screen.getByText('Changer d'état'))
expect(screen.getByText("C'est allumé !")).toBeInTheDocument()
```

Pour terminer, nous allons écrire un autre test pour vérifier que l'entrée de texte et son basculement fonctionnent correctement.

```plaintext
import { render, screen } from '@testing-library/react'
import userEvent from '@testing-library/user-event'
import About from './About'

describe('About', () => {

  ...

  test('Input fonctionne correctement', async () => {
    render( <About/> )

    userEvent.type(screen.getByTestId("testInput"), "Testing the test")
    userEvent.click(screen.getByText("Print input"))

    expect(screen.getByText("Testing the test")).toBeInTheDocument()

    userEvent.click(screen.getByText("Print input"))
    expect(screen.queryByText("Testing the test")).not.toBeInTheDocument()
  })


})
```

* Encore une fois, nous utilisons `userEvent` pour simuler du texte écrit dans notre élément d'entrée : `userEvent.type(screen.getByTestId("testInput"), "Testing the test")`
    
* Ensuite, nous simulons un clic sur le bouton bascule, et vérifions que le texte d'entrée est dans le document :
    

```plaintext
userEvent.click(screen.getByText("Print input"))
expect(screen.getByText("Testing the test")).toBeInTheDocument()
```

* Et nous terminons en simulant un autre clic et en vérifiant que le test n'est plus présent :
    

```plaintext
userEvent.click(screen.getByText("Print input"))
expect(screen.getByText("Testing the test")).toBeInTheDocument()
```

Vous pouvez voir à quel point les utilitaires fournis par les bibliothèques de test sont pratiques, et à quel point il est facile de les combiner avec Jest. 🤓

Nous pouvons exécuter ce fichier de test spécifique en exécutant `npm test -- About.test.jsx` et voici le résultat que nous obtenons :

```plaintext
// console
PASS  src/components/About.test.jsx
  About
    ✓ About se rend correctement (34 ms)
    ✓ Switch state fonctionne correctement (66 ms)
    ✓ Input fonctionne correctement (67 ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
Snapshots:   0 total
Time:        0.997 s, estimated 1 s
Ran all test suites matching /About.test.jsx/i.
```

La dernière fonctionnalité de Jest que je souhaite vous montrer est la **couverture de test**. Vous pouvez obtenir un rapport de couverture en exécutant `npm test -- --coverage`.

Cela exécutera vos tests normalement et à la fin du rapport de résultats, vous devriez voir quelque chose comme ceci :

```plaintext
// console
...

----------------|---------|----------|---------|---------|-------------------
File            | % Stmts | % Branch | % Funcs | % Lines | Uncovered Line #s 
----------------|---------|----------|---------|---------|-------------------
All files       |      75 |      100 |   85.71 |      70 |                   
 src            |       0 |      100 |       0 |       0 |                   
  App.jsx       |       0 |      100 |       0 |       0 | 7                 
  App.t.js      |       0 |        0 |       0 |       0 |                   
  index.js      |       0 |      100 |     100 |       0 | 5-6               
 src/components |     100 |      100 |     100 |     100 |                   
  About.jsx     |     100 |      100 |     100 |     100 |                   
----------------|---------|----------|---------|---------|-------------------
```

Dans le rapport, nous pouvons voir que notre composant `About.jsx` est complètement couvert, mais nos fichiers `App.jsx` et `index.js` ne sont pas testés.

Cette fonctionnalité est très pratique lorsque vous travaillez sur de grands projets et que vous souhaitez savoir rapidement si la plupart de votre code est testé correctement.

# Comment Tester une Application Front-end React avec Cypress

Nous avons beaucoup parlé de Jest, alors maintenant, voyons comment nous pouvons tester notre application en utilisant Cypress.

Nous allons commencer par installer Cypress en exécutant `npm i -D cypress`.

Cela devrait ajouter ceci à notre `package.json` :

```plaintext
"devDependencies": {
    "cypress": "^9.5.4"
}
```

Ensuite, nous allons exécuter `npx cypress open`. Cela ouvrira le navigateur Cypress et créera un répertoire `cypress` dans notre projet. Dans ce répertoire, vous trouverez des exemples, de la documentation et des options de configuration.

Vous trouverez également un dossier "integration", dans lequel nous devons mettre nos tests. Alors créons notre fichier `About.test.js` dans ce dossier et répliquons les mêmes exemples de test que nous avons vus avec Jest :

```plaintext
// About.test.js
describe('AboutPage', () => {
    it('Se rend correctement', () => {
        cy.visit('http://localhost:3000/about')
        cy.contains("Je suis la page à propos !")
    })

    it('bouton switch bascule le texte', () => {
        cy.contains("C'est allumé !")
        cy.get('.switchBtn').click()
        cy.contains("C'est en cours !")
        cy.get('.switchBtn').click()
        cy.contains("C'est allumé !")
    })

    it('Input fonctionne correctement', () => {
        cy.get(".testInput").type("Testing the test")
        cy.get('.printInputBtn').click()
        cy.contains("Testing the test")

        cy.get('.printInputBtn').click()
        cy.contains("Testing the test").should('not.exist')
    })
})
```

* La fonction `describe` fonctionne de la même manière que dans Jest.
    
* `it()` est la même que la fonction `test()` que nous avons vue précédemment.
    
* Dans le premier test, nous disons au navigateur de visiter l'URL de notre application et de vérifier que le texte correspondant est rendu :
    

```plaintext
cy.visit('http://localhost:3000/about')
cy.contains("Je suis la page à propos !")
```

* Ensuite, nous vérifions que le texte de basculement par défaut est rendu, simulons un clic et vérifions qu'il change en conséquence :
    

```plaintext
cy.contains("C'est allumé !")
cy.get('.switchBtn').click()
cy.contains("C'est en cours !")
cy.get('.switchBtn').click()
cy.contains("C'est allumé !")
```

* Et pour finir, nous simulons une entrée de texte, simulons un clic et vérifions que le texte d'entrée est rendu :
    

```plaintext
cy.get(".testInput").type("Testing the test")
cy.get('.printInputBtn').click()
cy.contains("Testing the test")

cy.get('.printInputBtn').click()
cy.contains("Testing the test").should('not.exist')
```

La syntaxe est légèrement différente de Jest, mais l'idée et la structure sont à peu près les mêmes.🤩

Maintenant, si nous exécutons `npx cypress open` à nouveau, une fenêtre devrait s'ouvrir avec ce contenu :

![2022-04-23_22-30](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-23_22-30.png align="left")

Nous pouvons cliquer sur "Run integration spec" et notre test s'exécutera automatiquement dans le navigateur simulé. Après l'exécution des tests, dans le panneau de gauche, nous verrons les résultats :

![2022-04-23_22-31](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-23_22-31.png align="left")

Nous pouvons ouvrir ces résultats pour voir chaque étape que le test a exécutée. Si nous survolons chaque étape, nous la verrons s'exécuter dans le navigateur en temps réel. Une fonctionnalité vraiment géniale de Cypress.👍👍

![2022-04-23_22-34](https://www.freecodecamp.org/news/content/images/2022/04/2022-04-23_22-34.png align="left")

Comme vous pouvez le voir, il est très facile de configurer des tests avec Cypress. Et si vous êtes déjà familier avec Jest, vous pouvez rapidement le prendre en main car la syntaxe n'est pas si différente.

Si vous vous demandez s'il est judicieux d'utiliser à la fois Jest et Cypress comme test runners dans le même projet, [je pense que cette réponse de stack-overflow](https://stackoverflow.com/questions/66217682/should-i-use-both-cypress-and-jest-together) résume assez bien la situation.

# Comment Tester une Application Back-end Node

Maintenant que nous avons une compréhension de base des façons dont nous pouvons tester une application front-end, traversons la rivière et voyons comment nous pouvons utiliser des outils similaires pour tester une application back-end.

Pour cela, nous allons utiliser une API Node et Express simple avec seulement 3 endpoints.

Créez un répertoire et exécutez `npm init -y` pour créer une application Node. Exécutez `npm i express` pour installer Express, puis exécutez `npm i -D jest supertest` pour installer Jest et Supertest comme dépendances de développement.

Dans votre `package.json`, ajoutez `"scripts": { "test": "jest" }`. Votre fichier `package.json` complet devrait ressembler à ceci :

```plaintext
{
  "dependencies": {
    "express": "^4.17.3"
  },
  "devDependencies": {
    "jest": "^27.5.1",
    "supertest": "^6.2.2"
  },
    "scripts": {
    "test": "jest"
  }
}
```

Ensuite, créez un fichier `app.js` et mettez ce code dedans :

```plaintext
// app.js
/* Import et initialisation d'express */
const express = require('express')
const app = express()
const server = require('http').Server(app)
/* Middlewares globaux */
app.use(express.json())

/* Endpoint 1 */
app.get('/', async (req, res) => {

    try {
        res.status(200).json({ greeting: "Bonjour !" })
    } catch (err) {
        res.status(500).send(err)
    }
})

/* Endpoint 2 */
app.get('/isPalindrome', async (req, res) => {

    try {
        const string = req.body.string
        let result = true        
        let left = 0
        let right = string.length-1
        
        while (left < right && result) {
            if (string[left] === string[right]) {
                left += 1
                right -= 1
            }
            else result = false
        }
        
        res.status(200).json({ result: result })
        
    } catch (err) {
        res.status(500).send(err)
    }
})

/* Endpoint 3 */
app.get('/twoSum', async (req, res) => {
    
    try {
        const nums = JSON.parse(req.body.nums)
        const target = JSON.parse(req.body.target)

        let result = false
        
        for (let i = 0; i < nums.length; i++) {
            const neededNum = target - nums[i]
            if (nums.indexOf(neededNum) !== -1 && nums.indexOf(neededNum) !== i) result = [nums[i], nums[nums.indexOf(neededNum)]]
        }
        
        res.status(200).json({ result: result })
        
    } catch (err) {
        res.status(500).send(err)
    }
})

/* Export de l'objet server */
module.exports = server

/* Initialisation du server */
server.listen(3001, () => console.log('Le serveur écoute.') )
server.on('error', error => console.error(error) )
```

Comme vous pouvez le voir, l'endpoint 1 retourne simplement un message de salutation. Les endpoints 2 et 3 sont des adaptations des fonctions que nous avons vues dans nos exemples vanilla JS. Ils reçoivent maintenant les paramètres dans la requête et les valeurs de retour vont dans la réponse. 😉

Maintenant, les tests ! Créez un fichier `app.test.js` et mettez ce code dedans :

```plaintext
// app.test.js
const supertest = require('supertest') // Import supertest
const server = require("./app") // Import l'objet server
const requestWithSupertest = supertest(server) // Nous utiliserons cette fonction pour simuler les requêtes HTTP

afterEach(done => { // La fonction afterEach est fournie par Jest et s'exécute une fois que tous les tests sont terminés
    server.close() // Nous fermons la connexion du serveur une fois que tous les tests sont terminés
    done()
})

test('GET "/" retourne une salutation', async () => {
    const res = await requestWithSupertest.get('/')
    expect(res.status).toEqual(200)
    expect(res.type).toEqual(expect.stringContaining('json'))
    expect(res.body).toEqual({ greeting: "Bonjour !" })
})

describe("/isPalindrome", () => {
    test('GET "/isPalindrome" neuquen retourne true', async () => {
        const res = await requestWithSupertest.get('/isPalindrome').set('Content-type', 'application/json').send({ "string":"neuquen" })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({ result: true })
    })

    test('GET "/isPalindrome" bariloche retourne true', async () => {
        const res = await requestWithSupertest.get('/isPalindrome').set('Content-type', 'application/json').send({ "string":"bariloche" })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({ result: false })
    })
})

describe("/twoSum", () => {
    test('GET "/twoSum" [2,7,11,15] et 9 retourne [7, 2]', async () => {
        const res = await requestWithSupertest.get('/twoSum').set('Content-type', 'application/json').send({ "nums":"[2,7,11,15]", "target": "9" })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({ result: [7, 2] })
    })

    test('GET "/twoSum" [3,2,4] et 6 retourne [4, 2]', async () => {
        const res = await requestWithSupertest.get('/twoSum').set('Content-type', 'application/json').send({ "nums":"[3,2,4]", "target": "6" })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({ result: [4, 2] })
    })

    test('GET "/twoSum" [3,2,4] et 10 retourne false', async () => {
        const res = await requestWithSupertest.get('/twoSum').set('Content-type', 'application/json').send({ "nums":"[3,2,4]", "target": "10" })
        expect(res.status).toEqual(200)
        expect(res.type).toEqual(expect.stringContaining('json'))
        expect(res.body).toEqual({ result: false })
    })
})
```

Analysons ce que nous faisons :

* Nous simulons la requête avec `requestWithSupertest.get('/')`
    
* Ensuite, nous "cassons" l'objet `res` en morceaux et assertons chaque partie de celui-ci :
    
    * Vérifiez le statut de la réponse : `expect(res.status).toEqual(200)`
        
    * Vérifiez le format de la réponse : `expect(res.type).toEqual(expect.stringContaining('json'))`
        
    * Vérifiez le contenu du corps de la réponse : `expect(res.body).toEqual({ greeting: "Bonjour !" })`
        

Les autres tests sont vraiment similaires, sauf que nous envoyons des données dans les corps des requêtes simulées, comme ceci :

```plaintext
const res = await requestWithSupertest.get('/isPalindrome').set('Content-type', 'application/json').send({ "string":"bariloche" })
```

Comme vous pouvez le voir, tester de cette manière est vraiment simple une fois que vous êtes familier avec Jest. Nous avons juste besoin d'un peu d'aide de Supertest pour simuler la requête HTTP et le reste n'est que l'assertion de la réponse. 👏👏

Nous pouvons exécuter nos tests avec `npm test` et nous devrions obtenir la réponse suivante :

```plaintext
// console
 PASS  ./app.test.js
  ✓ GET "/" retourne une salutation (46 ms)
  /isPalindrome
    ✓ GET "/isPalindrome" neuquen retourne true (18 ms)
    ✓ GET "/isPalindrome" bariloche retourne true (3 ms)
  /twoSum
    ✓ GET "/twoSum" [2,7,11,15] et 9 retourne [7, 2] (4 ms)
    ✓ GET "/twoSum" [3,2,4] et 6 retourne [4, 2] (3 ms)
    ✓ GET "/twoSum" [3,2,4] et 10 retourne false (2 ms)

Test Suites: 1 passed, 1 total
Tests:       6 passed, 6 total
Snapshots:   0 total
Time:        0.552 s, estimated 1 s
Ran all test suites.
```

# Conclusion

Et voilà ! Nous avons couvert les bases de quatre outils très populaires qui vous permettront de tester à la fois le front-end et le back-end de vos applications JS.

Bien sûr, il y a beaucoup plus à dire sur tous les outils que nous avons vus et de nombreuses fonctionnalités que nous n'avons pas couvertes. Mais l'idée était de vous donner une introduction afin que vous puissiez faire vos premiers pas dans le monde des tests.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [linkedin](https://www.linkedin.com/in/germancocca/) ou [twitter](https://twitter.com/CoccaGerman).

À bientôt et à la prochaine ! =D

![Image](https://www.freecodecamp.org/news/content/images/2022/04/goodbye-bye--1-.gif align="left")