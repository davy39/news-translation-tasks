---
title: Vous voulez que vos tests soient plus efficaces ? Rédigez vos spécifications
  comme ceci.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-29T16:13:06.000Z'
originalURL: https://freecodecamp.org/news/want-your-tests-to-be-more-effective-write-your-specifications-like-this-5d701a961e35
coverImage: https://cdn-media-1.freecodecamp.org/images/1*eDyt0mtmMAYoUOF0SaA0eA.jpeg
tags:
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Vous voulez que vos tests soient plus efficaces ? Rédigez vos spécifications
  comme ceci.
seo_desc: 'By Edd Yerburgh

  Writing test specifications is tricky. If you get it right, your tests are easy
  to understand and debug. But get it wrong, and your tests will be confuse people
  more than they’ll help them.

  In this article, I’ll show you how to write ...'
---

Par Edd Yerburgh

Rédiger des spécifications de test est délicat. Si vous faites bien les choses, vos tests seront faciles à comprendre et à déboguer. Mais si vous vous trompez, vos tests risquent de confondre les gens plus qu'ils ne les aideront.

Dans cet article, je vais vous montrer comment rédiger des spécifications de test expressives.

### Qu'est-ce que les spécifications de test ?

Les spécifications de test (specs) sont les chaînes utilisées pour identifier les tests lorsqu'ils sont exécutés par un test runner.

Ci-dessous, vous pouvez voir un exemple de sortie d'un test échoué. Vous pouvez voir où la spécification et l'erreur d'assertion sont utilisées pour décrire comment un test a échoué.

![Image](https://cdn-media-1.freecodecamp.org/images/PAT9zMtLMXDy-Pphm43EbKfAVIIYX6d7uJLL)
_Sortie de la console d'un test échoué utilisant la spécification et l'erreur d'assertion_

### Pourquoi les spécifications de test sont-elles importantes ?

Lorsque un test échoue, la manière de l'identifier est avec la spécification de test.

Si la spécification est bien écrite, vous saurez immédiatement pourquoi le test a échoué en utilisant la spécification de test et l'[assertion de test](https://medium.freecodecamp.org/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088).

```
calls showModal when button is clickedError: Expected spy to have been called but it was not. 
```

Nous pouvons deviner que le test a échoué parce que showModal n'a pas été appelé lorsque le bouton a été cliqué. Cette facilité de débogage est ce que vous devriez viser dans les tests.

Regardons quelques règles pour aider à écrire des spécifications de test spectaculaires.

### La règle de Boucle d'Or

Vous devriez suivre la règle de Boucle d'Or pour les spécifications de test — ni trop générales ni trop spécifiques.

Par exemple, `does what I expect` est trop général. Vous ne saurez pas pourquoi le test a échoué ou ce que le test vérifiait.

En même temps, vous devez éviter d'être trop spécifique. Au lieu d'utiliser `adds cache-control none header and vary Lang header`, utilisez une spécification moins étroite, comme `adds correct headers`.

Un test échoué a deux parties. La spécification de test, et le message d'erreur.

```
adds correct headers Error: Expected something to equal none
```

Le nom de votre test devrait nous dire ce qui se passe. Mais il n'a pas besoin de nous donner tous les détails. L'[erreur d'assertion](https://medium.freecodecamp.org/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088) devrait inclure une valeur qui complète la spécification de test.

### Gardez-les courtes

Les spécifications doivent être courtes.

Ma règle générale est qu'elles ne doivent pas dépasser 150 caractères.

Si vos tests font plus de 150 caractères, il y a des chances que vos unités soient trop complexes. Soit réécrivez la spécification pour qu'elle soit plus courte, soit divisez la fonctionnalité de vos unités en morceaux plus petits.

### Écrivez au présent

Vos spécifications de test doivent être au présent.

Par exemple, `calls toggleModal when button is clicked`, et non `will call toggleModal when button is clicked`.

Les spécifications sont des déclarations sur le comportement de votre unité : `returns sum of input`.

Écrire au présent rend vos spécifications plus courtes et plus faciles à lire.

### Concentrez-vous sur la sortie et l'entrée

Les tests doivent déclencher une entrée et attendre une sortie.

Vos spécifications doivent suivre ce modèle — **sortie lorsque entrée**. Par exemple, `calls toggleModal when button is clicked`, ou `returns true when called with string`.

Respecter cette norme garantit que vos tests se concentrent sur la sortie et l'entrée.

### Soyez concis

Vous n'avez pas beaucoup d'espace dans les spécifications de test, alors évitez les mots inutiles.

Par exemple, n'ajoutez pas de mots de remplissage comme should ou will.

`should call showmodal when clicked` ❌

`will call show modal when clicked` ❌

`calls show modal when clicked` ✅

### N'utilisez pas de blocs describe imbriqués

De nombreuses bibliothèques de test JavaScript incluent une fonctionnalité appelée blocs `describe`.

Les blocs `describe` définissent des sections dans vos tests.

Un bloc describe comme celui ci-dessous :

```
describe('sum', () => {  test('returns sum of input', () => {    expect(sum(1,2)).toBe(3)  })})
```

Il crée la sortie de console suivante :

![Image](https://cdn-media-1.freecodecamp.org/images/NO0xZZRWjaU9ERatYHwHtWvfVGi89wVmNKR9)
_La sortie utilisant un bloc describe sum_

Vous devriez utiliser les blocs describe pour définir une suite de tests dans un fichier.

Certains développeurs imbriquent les blocs describe les uns dans les autres pour organiser leurs tests. Ne faites jamais cela.

Au lieu d'écrire des tests comme ceci :

```
describe('API', () => {  describe('/books', () => {    describe('/id', () => {      describe('not found', () => {        test('returns 404', () => {          expect(4).toBe(4)        })      })    })  })})
```

Écrivez des tests comme ceci :

```
describe('API', () => {  test('returns 404 when /books/id is not found', () => {    expect(4).toBe(4)  })})
```

**Ne jamais imbriquer les blocs describe**. Maintenir vingt ou trente tests dans des fichiers avec des blocs describe imbriqués est vraiment confus. Vous perdez du temps à décider dans quel bloc un nouveau test doit aller, et il est facile de supprimer accidentellement une accolade fermante.

Les blocs describe imbriqués ajoutent une charge cognitive inutile.

### Écrivez différentes spécifications pour différents types de tests

Il existe deux types de spécifications de test que vous écriverez — **spécifications de haut niveau**, et **spécifications de niveau développeur**. 

Les tests de bout en bout nécessitent des spécifications de haut niveau. Les actions que les tests de bout en bout effectuent sont de haut niveau, et la spécification doit correspondre à cela.

Les spécifications de haut niveau sont le genre de spécifications que votre manager pourrait vous donner — `the modal opens when the user clicks a button`. Vous pourriez montrer vos spécifications à votre manager, et il comprendrait à quoi sert le test.

D'autre part, les tests unitaires nécessitent des spécifications de niveau développeur.

Les tests unitaires vérifient comment les fonctions de notre code fonctionnent. Ils sont de bas niveau, donc les spécifications doivent refléter cela.

Les spécifications de niveau développeur n'ont de sens que pour les autres développeurs, comme `button should trigger action with displayModal true when clicked`. Elles peuvent mentionner des concepts qui n'ont pas de sens pour les non-développeurs. Elles peuvent utiliser des termes comme `Boolean`, et `throws error`.

Considérez les tests unitaires comme de la documentation pour les futurs développeurs, considérez les tests de bout en bout comme de la documentation pour les futurs chefs de projet. Et assurez-vous que vos spécifications reflètent cela.

### Appel à l'action

Maintenant que vous savez comment écrire des spécifications de test de haute qualité, allez-y et écrivez quelques tests ! Si vous ne savez pas comment écrire des tests, le [guide de démarrage de Jest](https://facebook.github.io/jest/docs/en/getting-started.html) est un excellent point de départ.