---
title: Pourquoi j'apprécie maintenant les tests, et pourquoi vous devriez aussi.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-25T20:41:01.000Z'
originalURL: https://freecodecamp.org/news/why-i-now-appreciate-testing-and-why-you-should-too-74d48c67ab72
coverImage: https://cdn-media-1.freecodecamp.org/images/1*4zwBXAldsCYxTb9vySYwZw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Pourquoi j'apprécie maintenant les tests, et pourquoi vous devriez aussi.
seo_desc: 'By Evelyn Chan

  There’s a common misconception that writing tests slows down development speed.
  While the benefits of testing may not be immediately noticeable sometimes, it’s
  been my experience thus far that testing allows me to work faster in the lo...'
---

Par Evelyn Chan

Il existe une idée reçue selon laquelle l'écriture de tests ralentit la vitesse de développement. Bien que les avantages des tests ne soient pas toujours immédiatement visibles, mon expérience jusqu'à présent montre que les tests permettent de travailler plus rapidement à long terme, même au sein d'une petite équipe.

Après avoir implémenté des tests pour une application full-stack, j'ai appris à apprécier l'utilité de tester efficacement vos applications et comment cela influence votre capacité à coder.

### Brève introduction à ce à quoi ressemble une pile de tests

**Jest** est une bibliothèque de tests développée par Facebook qui est livrée avec une série de méthodes sympas pour faciliter les tests. Dans un projet récent, mon équipe et moi avons choisi Jest pour sa facilité d'utilisation et sa large gamme de fonctions intégrées qui aident à rationaliser vos tests. Il est très simple à configurer et utilise la bibliothèque Expect pour les assertions.

**Enzyme** est la méthode de facto pour tester votre application React. C'est assez magique dans le sens où il rend vos composants React au sein de Jest, vous permettant de tester votre code JSX front-end efficacement sans le transpiler manuellement. Vous rendez vos composants en utilisant l'une des trois méthodes : shallow, mount ou render.

**SuperTest** vous permet de faire des appels API sans réellement faire l'appel, en l'interceptant. Les appels API peuvent être coûteux et/ou lents pour les tests unitaires, vous ne voudrez donc pas faire l'appel et attendre la réponse. Sinon, cela ralentira vos tests et prendra une éternité à s'exécuter.

### Voici ce que j'ai appris

#### Les tests empêchent les régressions

L'ajout de nouvelles fonctionnalités casse fréquemment le code existant, et avoir des tests peut empêcher cela. Les tests aident à s'assurer que votre code fonctionne comme vous l'entendez. Aussi simple que cela puisse paraître, cela fait une différence énorme.

Il peut sembler ridicule d'entendre que tous les programmeurs ne peuvent pas articuler le code qu'ils écrivent, mais c'est en fait assez courant. Combien de fois vous a-t-on demandé d'expliquer quelque chose que vous avez écrit à la volée sous un délai strict et vous êtes retrouvé à bégayer pour répondre ? Écrire des tests vous force à penser clairement à ce que votre fonction prend exactement comme argument et retourne comme sortie.

Même si vous comprenez le but de chaque ligne de code, avec le temps, vous commencerez inévitablement à oublier. Les tests fournissent un complément important à la documentation qui vous aide à naviguer rapidement entre les bases de code. Prendre le temps d'écrire de bons tests efficaces vous permet de refactoriser votre code beaucoup plus facilement et de développer avec confiance.

#### Test unitaire avec des mocks et des stubs.

Dans un test unitaire, vous testez un morceau spécifique de code à la fois. Dans toute application, votre code fera probablement des appels à et dépendra d'autres classes ou modules. À mesure que ces relations entre classes augmentent en complexité, cela obscurcira la source des bugs.

Afin d'isoler et de déboguer efficacement, vous pouvez remplacer ces dépendances par un mock ou un stub pour contrôler le comportement ou la sortie que vous attendez.

Par exemple, supposons que vous voulez tester la méthode suivante :

```
import database from 'Database';
import cache from 'Cache';
```

```
const getData = (request) => {
  if (cache.check(request.id)) { 
    // vérifie si les données existent dans le cache
    return cache.get(request.id); 
    // obtient depuis le cache
  }
  return database.get(request.id); 
  // obtient depuis la base de données
};
```

Stub :

```
test('should get from cache on cache miss', (done) => {
  const request = { id: 10 };
  cache.check = jest.fn(() => false);
```

```
  getData(request);
  expect(database.get).toHaveBeenCalledWith(request.id);
  done();
});
```

Mock :

```
test('should check cache and return database data if cache data is not there', (done) => {
  let request = { id: 10 };
  let dummyData = { id: 10, name: 'Foo' }
  let cache = jest.mock('Cache');
  let database = jest.mock('Database');
  cache.check = jest.fn(() => false);
  database.get = jest.fn(() => dummyData);
```

```
  expect(getData(request)).toBe(dummyData);
  expect(cache.check).toHaveBeenCalledWith(request.id);
  expect(database.get).toHaveBeenCalledWith(request.id);
  done();
});
```

La principale différence entre les deux réside dans la manipulation de l'état par rapport au comportement.

Lorsque vous utilisez des mocks, vous remplacez le module entier par un objet mock. Un stub est une sortie forcée d'une fonction peu importe l'entrée donnée. Les mocks sont utilisés pour tester si une fonction est appelée avec les bons arguments, et les stubs sont utilisés pour tester comment une fonction opère sur une réponse donnée. Les stubs sont utilisés pour valider l'état d'une méthode, tandis que les mocks sont utilisés pour évaluer le comportement.

Jest fournit `jest.fn`, qui a à la fois des fonctionnalités de mocking et de stubbing de base. Un mock Jest peut également stub les sorties de méthode, et dans ce cas être à la fois un mock et un stub.

Le concept de mocks dans les tests et comment ils diffèrent des stubs peut devenir assez complexe, alors pour une plongée plus profonde, consultez les liens à la fin !

#### Sachez ce que vous n'avez pas besoin de tester.

Vous voudrez tester chaque méthode que vous écrivez. Mais gardez à l'esprit que selon votre base de code, une couverture de test à 100 % est peu probable et la plupart du temps pas même nécessaire.

Avec Jest, vous pouvez facilement suivre votre couverture de test en ajoutant une balise `--coverage` à votre script de test sur votre CLI. Bien que ce soit une mesure utile, prenez cela avec des pincettes — la façon dont Jest mesure la couverture de test est en traçant la pile d'appels, donc une couverture de test plus élevée ne signifie pas nécessairement que vos tests sont efficaces.

Par exemple, dans un projet précédent, j'ai utilisé une bibliothèque pour implémenter un composant carousel. Dans le composant, il y avait une fonction pour rendre une liste basée sur un tableau. Pour augmenter la couverture de test, j'ai écrit un test pour compter et comparer le nombre d'éléments rendus au tableau. Le composant carousel modifiait le nombre d'éléments rendus sur le DOM pour être plus qu'une sortie 1:1, même si l'implémentation affichait visuellement le bon nombre d'éléments dans le navigateur. J'ai choisi de renoncer à la couverture de test car elle testait essentiellement la bibliothèque carousel au lieu de mon code.

Supposons un composant `Listings` avec une méthode `renderCarousel` qui rend un carousel à partir d'une bibliothèque externe :

**Test inefficace :**

```
test('should return the same number of elements as the array', (done) => {
    // Render complet du DOM
    let mountWrapper = mount(<Listings />);
```

```
    // Changement d'état pour déclencher un re-render
    mountWrapper.instance().setState({ listings: [listing, listing, listing] });
```

```
    // Met à jour le wrapper basé sur le nouvel état
    mountWrapper.update();
```

```
    expect(mountWrapper.find('li').length).toBe(3);
    done();
  })
```

**Test efficace :**

```
test('should call renderCarousel method when state is updated', (done) => {
    // Fonction mock à l'intérieur du composant pour suivre les appels
    wrapper.instance().renderCarousel = jest.fn();
```

```
    // Changement d'état pour déclencher un re-render
    wrapper.instance().setState({ listings: [listing, listing, listing] });
```

```
    expect(wrapper.instance().renderCarousel).toHaveBeenCalled();
    done();
  });
```

La différence entre les deux réside dans ce que les tests testent réellement.

Le premier exemple évalue la fonction renderCarousel, qui appelle la bibliothèque externe. Le deuxième test évalue si renderCarousel est simplement appelé. Puisque les bibliothèques externes sont quelque peu similaires à une boîte noire de magie et sont testées par leurs propres développeurs, il n'est pas nécessaire d'écrire un test qui vérifie qu'elle fonctionne correctement.

Dans ce scénario, nous devons seulement tester que la bibliothèque est appelée et avoir confiance que les développeurs de la bibliothèque gèrent les tests.

Comprendre ce que vous devez et ne devez pas tester vous permet de maximiser votre temps pour éliminer les redondances.

#### Des tests bien conçus mènent à un code bien conçu.

Concevoir votre code en sachant que vous devrez écrire des tests pour celui-ci améliore votre code. Cela est connu sous le nom de développement piloté par les tests, qui est soutenu par une grande majorité de la communauté de codage.

Afin de tester correctement les fonctions unitaires, vous devez éliminer la logique et tester une méthode à la fois. Cette structure vous force à écrire un code modulaire et à abstraire la logique de vos composants.

À mesure que vous pensez à votre code en termes d'écriture de tests, vous commencerez à développer l'habitude de découpler votre code. J'ai découvert que l'écriture de votre code de cette manière semble produire une structure de type histoire qui est à la fois plus facile à écrire et plus facile à suivre.

Considérons un scénario où nous appelons un endpoint pour récupérer des données d'une base de données et formater ces données avant de les retourner.

**Trop de logique :**

```
// Définir l'endpoint
app.get('/project', (request, response) => {
  let { id } = request.params;
  let query = `SELECT * FROM database WHERE id = ${id}`;
    database.query(query)
    .then((result) => {
      const results = [];
      for (let index = 0; index < data.length; index++) {
        let result = {};
        result.newKey = data[index].oldKey;
        results.push(result);
      }
      response.send(results);
    })
    .catch((error) => {
      response.send(error);
    })
  })
```

**Plus facile à tester :**

```
// Faire un appel à la base de données pour les données
const getData = (request) => {
  return new Promise((resolve, reject) => {
    let { id } = request.params;
    let query = `SELECT * FROM database WHERE id = ${id}`;
    database.query(query)
      .then(results => resolve(results))
      .catch(error => reject(error));
    };
}
```

```
// Formater les données à renvoyer
const formatData = (data) => {
  const results = [];
  for (let index = 0; index < data.length; index++) {
    let result = {};
    result.newKey = data[index].oldKey;
    results.push(result);
  }
  return results;
}
```

```
// Envoyer les données
const handleRequest = (request, response) => {
  getData(request)
  .then((result) => {
    let formattedResults = formatData(result)
    response.send(formattedResults);
  .catch((error) => {
    response.send(error);
}
```

```
// Définir l'endpoint
app.get('/project', handleRequest);
```

Bien que le deuxième exemple soit plus long, il est beaucoup plus facile à suivre. La logique est clairement abstraite et isolée, ce qui la rend beaucoup plus facile à tester.

Si vous débutez avec les tests/codage, il peut être difficile de discerner ce qui fait un test bien conçu. Vous ne pouvez pas écrire des tests efficaces si votre code n'est pas bien conçu, mais vous ne pouvez pas déterminer ce qui rend le code adapté aux tests que vous ne pouvez pas écrire ! Heureusement, cela mène à mon dernier conseil...

#### Écrivez des tests au fur et à mesure que vous codez

La meilleure façon d'incorporer les tests est de les écrire en même temps que votre code. Sinon, cela semblera accablant lorsque vous les écrirez tous à la fois et devrez aller et venir entre tous vos fichiers de tests et de méthodes.

De nombreux débutants font l'erreur de traiter les tests comme quelque chose que vous faites après que tout votre code est écrit. Si vous le traitez comme une tâche que vous faites en même temps que votre code, cela améliore non seulement votre code mais rend également leur écriture plus réalisable.

Dans un système avec des API clairement abstraites, vous pouvez tester chaque classe avant de passer à la suivante afin de savoir quelle partie de la logique est cassée. Par exemple, mon endpoint 'get' appelle getData pour interagir avec la base de données. J'écrirais d'abord des tests pour getData et m'assurerais qu'ils sont au vert. De cette façon, je sais que si l'un de mes tests de contrôleur échoue, cela a probablement à voir avec la manière dont j'appelle getData.

J'espère que cet article vous a aidé à comprendre pourquoi les tests sont si utiles et vous a équipé de quelques conseils pour commencer. Cela ne fait qu'effleurer la surface des tests, cependant ! Voici quelques ressources si vous voulez en savoir plus :

[https://martinfowler.com/articles/mocksArentStubs.html](https://martinfowler.com/articles/mocksArentStubs.html)

[https://medium.com/@rickhanlonii/understanding-jest-mocks-f0046c68e53c](https://medium.com/@rickhanlonii/understanding-jest-mocks-f0046c68e53c)

Si vous avez aimé cet article, veuillez cliquer sur le ?? et partager pour aider les autres à le trouver. Merci d'avoir lu !