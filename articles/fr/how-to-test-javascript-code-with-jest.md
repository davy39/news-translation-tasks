---
title: Comment tester le code JavaScript avec Jest
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-12-14T13:54:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-javascript-code-with-jest
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/jest.png
tags:
- name: JavaScript
  slug: javascript
- name: youtube
  slug: youtube
seo_title: Comment tester le code JavaScript avec Jest
seo_desc: 'Testing code is crucial because it ensures the reliability, security, and
  proper functioning of products or systems, identifying potential issues before they
  become significant problems.

  We just published a course on the freeCodeCamp.org YouTube chan...'
---

Tester le code est crucial car cela garantit la fiabilité, la sécurité et le bon fonctionnement des produits ou des systèmes, en identifiant les problèmes potentiels avant qu'ils ne deviennent des problèmes majeurs.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous apprendra à tester le code JavaScript avec le framework de test Jest. Tomi Tokko a créé ce cours. Il est un enseignant expérimenté et membre de l'équipe freeCodeCamp.

### Qu'est-ce que Jest ?

Jest, développé par Facebook, est un framework de test JavaScript agréable avec un accent sur la simplicité. Il fonctionne de manière transparente avec des projets utilisant Babel, TypeScript, Node.js, React, Angular et Vue.js, ce qui en fait un choix polyvalent pour une large gamme de projets JavaScript.

### Fonctionnalités principales de Jest

* **Configuration zéro** : Jest est conçu pour fonctionner dès la sortie de la boîte, avec une configuration minimale requise.
* **Tests de snapshot** : Cette fonctionnalité garantit que votre interface utilisateur ne change pas de manière inattendue en capturant des snapshots de vos composants.
* **Test Runner intégré** : Jest est livré avec un test runner intégré, éliminant le besoin d'outils supplémentaires.
* **Support de Mocking** : Il fournit des capacités de mocking robustes, cruciales pour isoler les tests des dépendances externes.

### Exemples de base de Jest

**Test simple** : Écrire un test de base dans Jest est simple. Voici un exemple qui teste une fonction simple :

```javascript
function sum(a, b) {
  return a + b;
}

test('additionne 1 + 2 pour obtenir 3', () => {
  expect(sum(1, 2)).toBe(3);
});
```

Cet exemple définit une fonction `sum` et un test qui vérifie si la fonction retourne le résultat attendu.

**Test asynchrone** : Jest gère le code asynchrone sans effort. Voici un exemple :

```javascript
async function fetchData() {
  // Simuler la récupération de données depuis une API
  return 'freeCodeCamp';
}

test('les données sont freeCodeCamp', async () => {
  const data = await fetchData();
  expect(data).toBe('freeCodeCamp');
});
```

Ce test garantit que la fonction `fetchData` se résout avec la chaîne attendue.

**Fonctions Mock** : Pour tester les interactions dans votre code, vous pouvez utiliser les fonctionnalités de mocking de Jest :

```javascript
const myMockFunction = jest.fn(x => x + 42);

test('test de fonction mock', () => {
  expect(myMockFunction(0)).toBe(42);
});
```

Ce test vérifie que la fonction mock se comporte comme prévu lorsqu'elle est appelée avec un argument spécifique.

### Contenu du cours

Le cours de Tomi sur la chaîne YouTube de freeCodeCamp est structuré pour répondre aux besoins des débutants et des développeurs expérimentés. Il couvre les bases, aborde des sujets avancés comme le mocking et les tests de snapshot, et fournit des exemples concrets pour consolider la compréhension.

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://www.youtube.com/watch?v=IPiUDhwnZxA) (1 heure de visionnage).

%[https://www.youtube.com/watch?v=IPiUDhwnZxA]