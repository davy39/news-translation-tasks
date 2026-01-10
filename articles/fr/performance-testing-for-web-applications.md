---
title: Comment effectuer des tests de performance sur vos applications Web
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-02-26T19:52:39.000Z'
originalURL: https://freecodecamp.org/news/performance-testing-for-web-applications
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/performance-test2.jpg
tags:
- name: Testing
  slug: testing
- name: Web Applications
  slug: web-applications
- name: web performance
  slug: web-performance
seo_title: Comment effectuer des tests de performance sur vos applications Web
seo_desc: "Performance testing is an important yet underrated field of software development.\
  \ And it’s a must-have skill that can help you prevent common software failures\
  \ that occur in production applications. \nPerformance testing is a routine software\
  \ practice..."
---

Les tests de performance sont un domaine important mais sous-estimé du développement logiciel. Et c'est une compétence indispensable qui peut vous aider à prévenir les pannes logicielles courantes qui se produisent dans les applications de production. 

Les tests de performance sont une pratique logicielle de routine qui est effectuée pour déterminer la stabilité d'un système en termes de scalabilité, de fiabilité et de gestion des données, parmi d'autres paramètres.

Dans ce tutoriel, je vais vous guider à travers ce que les tests de performance impliquent, et les outils courants utilisés pour les tests backend. Nous allons également parcourir ensemble un projet de démonstration de tests de performance. 

Le tutoriel est simplifié et adapté aux débutants, aux développeurs de niveau intermédiaire et aux développeurs professionnels. Être compétent en tests de performance est fondamental pour grandir en tant que développeur backend, et ce guide servira de bonne révision même si vous êtes plus avancé dans votre carrière. Cela dit, plongeons-nous dans le sujet.

### Prérequis :

* Connaissance intermédiaire de Node.js
* Connaissance de base des opérations JavaScript
* Connaissance du développement d'API

## Table des matières :

1. [Qu'est-ce que les tests de performance ?](#heading-quest-ce-que-les-tests-de-performance)
2. [Exemples d'outils de tests de performance](#heading-exemples-doutils-de-tests-de-performance)
3. [Projet de démonstration](#heading-projet-de-demonstration)
4. [Conclusion](#heading-conclusion)

## Qu'est-ce que les tests de performance ?

Les tests de performance servent à de nombreuses fins – l'une des plus importantes étant de tester l'efficacité du système dans l'exécution et le maintien des tâches. Ils servent également de norme que vous pouvez utiliser pour comparer des systèmes d'efficacité et de builds variés et vous permettent de choisir le plus efficace.

Les tests de performance aident également à révéler les vulnérabilités. Les outils de test de pointe sont bien optimisés pour analyser efficacement le code afin de détecter toute erreur. Ils sont rapides à mettre en évidence les zones où ces erreurs se produisent.

Le but final des tests de performance dépend de la manière dont vous utilisez l'application. Il peut être orienté concurrence ou taux de transaction, selon que l'application implique des utilisateurs finaux ou non. 

Les tests de performance peuvent également impliquer des tests de charge, qui sont généralement effectués pour évaluer le comportement d'un service web sous une charge spécifique attendue. D'autres types de tests que vous pouvez effectuer incluent les tests d'intégration, les tests de pointe, les tests de trempage et les tests de stress.

## Exemples d'outils de tests de performance

Il existe de nombreux outils couramment utilisés pour tester l'efficacité et la latence des applications web. Dans cette section, je vais discuter de certains des outils populaires utilisés, et mettre en évidence leurs forces et leurs cas d'utilisation.

### Jest

[Jest](https://www.npmjs.com/package/jest) est un outil de test multiplateforme utilisé pour évaluer la justesse des applications basées sur JavaScript. C'est celui que nous allons utiliser dans cette démonstration. 

Jest a été initialement créé pour tester l'efficacité des applications React, mais a depuis été étendu pour tester l'efficacité des applications Node.js également. Il offre également une fonctionnalité de couverture de code.

### Mocha

[Mocha](https://www.npmjs.com/package/mocha) est un outil de test asynchrone concis basé sur JavaScript pour les applications Node.js. Il est également utilisé avec des bibliothèques d'assertion telles que `[Chai](https://www.npmjs.com/package/chai)` et `[should](https://www.npmjs.com/package/should)`.

### Pythagora

[Pythagora](https://github.com/Pythagora-io/pythagora) offre une fonctionnalité de test d'intégration unique pour aider à tester comment différentes parties de l'application fonctionnent ensemble. Il dispose également d'une fonctionnalité de couverture de code.

### Artillery

[Artillery](https://artillery.io) est un outil de test agnostique de la pile. Cela signifie qu'il peut être utilisé pour plusieurs applications web basées sur différents langages de programmation et produire toujours un résultat de test optimal. 

Cet outil fournit des fonctionnalités de test de charge efficaces qui aident à déterminer l'état optimal de l'application lorsqu'elle est exposée à une grande charge de trafic. Il vérifie également la vitesse à laquelle une application répond à une demande utilisateur sans planter. 

### Ava

[Ava](https://www.npmjs.com/package/ava) est un outil de test d'unités de performance basé sur JavaScript utilisé pour tester l'efficacité des applications Node.js. Il fonctionne de manière asynchrone, exécutant plusieurs tests simultanés pour déterminer l'adéquation de plusieurs unités de code.

### Loadtest

[Loadtest](https://www.npmjs.com/package/loadtest) est un package Node spécial qui est utilisé pour tester la charge des applications Node.js. Il évalue leur capacité à faire face à des demandes de volumes variés et il évalue l'efficacité et la concurrence.

### Apache J-meter

[Apache J-meter](https://jmeter.apache.org) offre des fonctionnalités de test de charge pour les applications web. Il dispose d'un IDE intégré pour permettre l'interaction avec l'utilisateur. Il est multithread, augmentant sa capacité à imiter plusieurs utilisateurs.

Il existe d'autres outils de test qui sont également utiles. Mais dans ce tutoriel, nous allons utiliser `Jest` pour tester notre application backend.

## Projet de démonstration

### Installer Jest

Nous allons maintenant effectuer un test unitaire sur notre code en utilisant l'outil de test `Jest`. Pour ce faire, vous devrez installer le package `Jest` dans votre dossier de code. Tapez `npm install jest` dans l'invite de commande. Un message de succès s'affichera lorsque l'installation sera terminée.

### Configurer `package.json`

Dans ce tutoriel, nous allons tester l'efficacité de certaines routes sélectionnées dans notre application Node.js. Cela nécessitera d'écrire différents tests unitaires pour chaque route et d'évaluer sa justesse. 

Optimisons maintenant notre structure de fichiers pour tester avec succès notre application. Accédez au fichier `package.json` et modifiez-le pour inclure le code suivant :

```javascript
"scripts": {
    "test": "jest",
    "start": "nodemon index.js"
  },
```

La modification du fichier package.json pour inclure ce code garantit que le serveur Node.js reconnaît Jest comme notre outil de test unitaire par défaut pour le projet. En faisant cela, chaque fois que nous entrons `npm test` dans l'invite de commande, Jest s'active.

### Configurer l'environnement de test

Créez un dossier dans le répertoire `root` nommé « tests ». Cela aide l'opérateur Jest à localiser les fichiers spécifiques contenant les routes à tester. 

Dans le dossier de test, créez un fichier de test. Le fichier peut être nommé comme vous le souhaitez, mais le suffixe `.test.js` doit être ajouté pour permettre à `Jest` de le reconnaître et de l'exécuter.

Après avoir terminé ces étapes, plongeons dans les détails principaux des tests unitaires dans notre projet.

### Exécuter les tests unitaires

Le projet de démonstration que nous allons tester dans ce tutoriel est une application de bibliothèque de livres électroniques qui contient certaines fonctions telles qu'une route `get all books`, une route `Get a single book`, une route `upload a book` et une route `delete a book`. Nous allons créer des tests unitaires pour la route `GetAllBooks` dans l'exemple ci-dessous, puis vous pourrez essayer de créer les vôtres pour les autres routes.

Tout d'abord, nous allons importer la base de données de livres dans le fichier test.js comme ceci :

```javascript
const Book = require('../models/Book')
```

Le code ci-dessus importe et initialise notre modèle de base de données MongoDB de livres par défaut.

Ensuite, nous allons importer les fonctions que nous allons tester dans chaque route :

```javascript
const Book = require("../models/Book")

async function GetAllBooks(req, res) {
    try {
        const allBooks = await Book.find();
        res.status(200)
        res.send(allBooks)
    }
    catch (err) {
        res.status(500)
        res.send(err)
    }
}
module.exports = {GetAllBooks};
```

```javascript
const {GetAllBooks} = require("../controllers/Books");
```

Le code ci-dessus importe la fonction getAllBooks depuis un dossier de contrôleur. 

Ayant importé la fonction, allons-y pour configurer notre fonction de test unitaire Jest.

```javascript
jest.mock("../models/Book");

const req = {};
const res = {
  status: jest.fn((x) => x),
  send: jest.fn((x) => x),
};

it("it should return all the books in the database", async () => {
 
Book.find.mockImplementationOnce(() => ({
    Title: "black is king",
    Author: "black",
    price: "$23",
    Summary: "Hello",
  }));
  
  await GetAllBooks(req, res);
  
 
expect(res.status).toHaveBeenCalledWith(200);
 
expect(res.send).toHaveBeenCalledTimes(1);
});
```

Tout d'abord, Jest vous offre la possibilité de créer une fausse base de données en copiant la structure de la base de données par défaut. Cela est connu sous le nom de mocking. Cela permet au test unitaire de fonctionner plus rapidement et d'éliminer le lag qui vient avec l'obtention de réponses de grandes bases de données. 

Les tests qui impliquent la base de données réelle sont appelés tests de bout en bout par opposition aux tests unitaires.

Voici comment vous pouvez faire cela dans Jest :

```javascript
jest.mock("../models/Book");
```

Le code ci-dessus illustre le mocking de la base de données. Afin d'obtenir un test unitaire plus rapide, nous devons mock la base de données Book existante que nous utilisons dans notre application.

```javascript
const req = {};
const res = {
  status: jest.fn((x) => x),
  send: jest.fn((x) => x),
};
```

Le code ci-dessus contient les objets de requête et de réponse d'échantillon par défaut. L'objet de réponse d'échantillon contient à la fois les fonctions status et send, qui retournent une sortie définie si elles sont exécutées avec succès ou non.

```javascript
it("it should return all the books in the database", async () => {
Book.find.mockImplementationOnce(() => ({
    Title: "black is king",
    Author: "black",
    price: "$23",
    Summary: "Hello",
  }));
  await GetAllBooks(req, res); 
expect(res.status).toHaveBeenCalledWith(200);
expect(res.send).toHaveBeenCalledTimes(1);
});

```

Maintenant, la fonction `It` contient une courte description de ce que le test devrait être. Cela est ensuite couplé à une fonction asynchrone anonyme qui contient une implémentation mock de la base de données avec quelques données factices.

Après cela, la requête getAllBooks est déclenchée et exécutée avec une requête nulle qui lui est passée et le format de l'objet de réponse est inclus.

L'instruction `expect` retourne `passed` si la fonction satisfait les exigences attendues. Pour ce code, les exigences sont que l'objet `response` doit retourner un code de statut de 200 et l'objet `response.send` doit être appelé au moins une fois avec l'objet de réponse inclus. Si cela échoue, un statut échoué sera retourné.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/test.JPG)
_Tests passing_

Vous connaissez maintenant les bases de la façon de tester les fonctions unitaires. Vous pouvez également essayer de tester la route `delete book`, la route `upload a book` et la route `find a specific book`.

## Conclusion

Dans ce tutoriel, vous avez pu exploiter l'utilité des outils de test pour optimiser vos applications web. 

Vous avez appris divers outils de test disponibles et leurs cas d'utilisation, et vous avez également implémenté un test unitaire dans une application web.  

En suivant les étapes mises en évidence dans ce tutoriel, vous serez en mesure d'effectuer des tests unitaires sur vos projets de codage.

J'espère sincèrement que vous avez appris quelque chose de nouveau et que vous avez apprécié ce tutoriel. Jusqu'à la prochaine fois, continuez à coder.