---
title: Comment simuler des requêtes pour les tests unitaires dans Node
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-31T00:03:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-mock-requests-for-unit-testing-in-node-bb5d7865814a
coverImage: https://cdn-media-1.freecodecamp.org/images/0*FDlur-dky_pPFMag.
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: technology
  slug: technology
- name: unit testing
  slug: unit-testing
- name: Web Development
  slug: web-development
seo_title: Comment simuler des requêtes pour les tests unitaires dans Node
seo_desc: 'By Edo Rivai

  Let’s say you’ve decided to test your codebase, and you’ve read that unit and integration
  tests shouldn’t perform I/O. You’ve figured you need to mock out the outbound HTTP
  requests that your app is making, but you’re not sure where to s...'
---

Par Edo Rivai

Supposons que vous avez [décidé de tester votre base de code](ttps://blog.kentcdodds.com/write-tests-not-too-many-mostly-integration-5e8c7fff591c), et que vous avez lu que [les tests unitaires et d'intégration ne devraient pas effectuer d'I/O](https://medium.com/@_ericelliott/yes-i-am-clearly-saying-dont-unit-test-i-o-but-not-just-in-js-in-any-language-ca8ce5016942). Vous avez compris que vous devez simuler les requêtes HTTP sortantes que votre application envoie, mais vous n'êtes pas sûr de par où commencer.

J'ai décidé de demander à Kent C. Dodds sur Twitter comment il aborde la simulation HTTP :

Juste, Kent ! Je suppose que ce sujet mérite une explication plus élaborée.

#### TL;DR

Lorsque vous devez tester du code qui envoie des requêtes HTTP, essayez ce qui suit.

1. Séparez les requêtes HTTP de la logique métier de traitement de la réponse. Très souvent, le code qui gère le protocole HTTP n'est pas très intéressant et, selon certains, ne nécessite pas de tests. Utilisez l'outil de simulation de votre choix pour simuler votre wrapper d'API.
2. Si vous devez vraiment tester du code spécifique à HTTP et que la réponse de l'API externe est relativement simple, utilisez Nock et simulez manuellement les requêtes.
3. Si la réponse que vous devez tester est assez complexe, utilisez `nock-record` pour enregistrer une réponse une fois et utilisez cet enregistrement pour les tests suivants.

Puisque la communauté des tests est obsédée par les pyramides, en voici une pour vous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*w3qPSBXV3ujMUrgT-rIBpQ.png)
_Pyramide de simulation HTTP. « API Wrappers + mocking régulier » à la base. « Nocks manuels » au milieu. « Enregistrements Nock » au sommet._

### Présentation de `Nock`

Je dirais que le consensus général dans le monde NodeJS est d'utiliser `[nock](https://github.com/node-nock/nock)`, qui fonctionne en patchant le module natif `http` de Node. Cela fonctionne très bien, car même si vous n'utilisez pas directement le module `http`, la plupart des bibliothèques utilisateur comme `axios`, `superagent` et `node-fetch` utilisent toujours `http` sous le capot.

Écrire et utiliser un `Nock` ressemble à ceci :

```
// Configurer un intercepteur
nock('http://www.example.com')
  .post('/login', 'username=pgte&password=123456')
  .reply(200, { id: '123ABC' });
```

```
// Exécuter votre code, qui envoie une requête
fetchUser('pgte', '123456');
```

Dans l'exemple ci-dessus, `fetchUser` envoie une requête POST à `example.com/login`. Nock intercepte la requête et répond immédiatement avec votre réponse prédéfinie, sans réellement toucher le réseau. Génial !

### Ce n'est pas si simple

Lorsque j'ai commencé avec Nock, je l'ai rapidement utilisé avec mes tests unitaires. Cependant, j'ai rapidement eu l'impression de passer plus de temps à écrire des Nocks qu'à tester la logique métier. Une solution à cela est de **séparer votre code de requête de votre logique métier**. Examinons du code.

```
async function getUser(id) {
  const response = await fetch(`/api/users/${id}`);
  // L'utilisateur n'existe pas
  if (response.status === 404) return null;
```

```
  // Une autre erreur s'est produite
  if (response.status > 400) {
    throw new Error(`Impossible de récupérer l'utilisateur #${id}`);
  }
  const { firstName, lastName } = await response.json();
  return {
    firstName,
    lastName,
    fullName: `${firstName} ${lastName}`
  };
}
```

Le code ci-dessus envoie une requête à `/api/users/<user id>`, et lorsqu'un utilisateur est trouvé, il reçoit un objet contenant un `firstName` et un `lastName`. Enfin, il construit un objet qui a un champ supplémentaire `fullName`, calculé à partir du prénom et du nom reçus de la requête.

Une suite de tests pour cette fonction pourrait ressembler à ceci :

```
it('devrait correctement décorer le fullName', async () => {
  nock('http://localhost')
    .get('/api/users/123')
    .reply(200, { firstName: 'John', lastName: 'Doe' });
  const user = await getUser(123);
  expect(user).toEqual({
    firstName: 'John',
    lastName: 'Doe',
    fullName: 'John Doe'
  });
});
```

```
it('devrait retourner null si l'utilisateur n'existe pas', async () => {
  nock('http://localhost')
    .get('/api/users/1337')
    .reply(404);
  const user = await getUser(1337);
  expect(user).toBe(null);
});
```

```
it('devrait retourner null lorsqu'une erreur se produit', async () => {
  nock('http://localhost')
    .get('/api/users/42')
    .reply(404);
  const userPromise = getUser(42);
  expect(userPromise).rejects.toThrow('Impossible de récupérer l'utilisateur #42');
});
```

Comme vous pouvez le voir, il se passe beaucoup de choses dans ces tests. Séparons la fonction en deux parties :

* le code qui envoie et gère la requête HTTP
* notre logique métier

Notre exemple est un peu artificiel, car la seule logique métier que nous avons est de « calculer » le `fullName`. Mais vous pouvez imaginer comment une application réelle aurait une logique métier plus complexe.

```
// api.js
export async function getUserFromApi(id) {
  const response = await fetch(`/api/users/${id}`);
  // L'utilisateur n'existe pas
  if (response.status === 404) return null;
```

```
  // Une autre erreur s'est produite
  if (response.status > 400) {
    throw new Error(`Impossible de récupérer l'utilisateur #${id}`);
  }
```

```
  return response.json();
}
```

```
// user.js
import { getUserFromApi } from './api';
```

```
async function getUserWithFullName(id) {
  const user = await getUserFromApi(id);
  if (!user) return user;
```

```
  const { firstName, lastName } = user;
  return {
    firstName,
    lastName,
    fullName: `${firstName} ${lastName}`
  };
}
```

Pour ne pas vous ennuyer à mort, je ne vais vous montrer que les tests pour notre logique métier. Au lieu d'utiliser Nock pour simuler la requête HTTP, vous pouvez maintenant utiliser votre bibliothèque de simulation préférée pour simuler notre propre wrapper d'API. Je préfère [Jest](https://facebook.github.io/jest/), mais ce modèle n'est pas lié à une bibliothèque de simulation spécifique.

```
// La fonction que nous testons
import { getUserWithFullName } from './user';
```

```
// Importé uniquement pour la simulation
import { getUserFromApi } from './api';
```

```
jest.mock('./api');
```

```
it('devrait correctement décorer le fullName', async () => {
  getUserFromApi.mockResolvedValueOnce(
    { firstName: 'John', lastName: 'Doe' }
  );
  const user = await getUserWithFullName(123);
  expect(user).toEqual({
    firstName: 'John',
    lastName: 'Doe',
    fullName: 'John Doe'
  });
});
```

```
it('devrait retourner null si l'utilisateur n'existe pas', async () => {
  getUserFromApi.mockResolvedValueOnce(null);
  const user = await getUserWithFullName(1337);
  expect(user).toBe(null);
});
```

Comme vous pouvez le voir, nos tests sont un peu plus propres. Toute la surcharge HTTP est maintenant contenue dans le module API. Ce que nous avons effectivement fait, c'est minimiser la surface de notre code qui connaît le transport HTTP. Et en faisant cela, nous minimisons le besoin d'utiliser Nock dans nos tests.

### Mais la logique HTTP est exactement ce que je veux tester !

Je vous entends. Parfois, la connexion à une API externe est exactement ce que vous voulez tester.

J'ai déjà montré comment vous pouvez utiliser Nock pour simuler une requête HTTP très basique. Écrire des Nocks explicites pour de telles paires requête/réponse simples est très efficace, et je recommande de s'y tenir autant que possible.

Cependant, parfois le contenu de la requête ou de la réponse peut devenir assez complexe. Écrire des Nocks manuels pour de tels cas devient rapidement fastidieux et aussi fragile !

Un exemple très clair d'un tel cas serait le test d'un scraper. La principale responsabilité d'un scraper est de convertir du HTML brut en données utiles. Cependant, lors du test de votre scraper, vous ne voulez pas construire manuellement une page HTML à alimenter dans Nock. De plus, le site que vous souhaitez scraper a déjà le HTML que vous voulez traiter, alors utilisons cela ! Pensez aux snapshots Jest, pour la simulation HTTP.

#### Extraction de sujets de Medium

Supposons que je veux connaître tous les sujets disponibles sur Medium.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GTktvsL1PGGUyaHfpObi6w.png)
_Capture d'écran de la page d'accueil de medium.com, montrant la liste des sujets disponibles_

Nous allons utiliser `scrape-it` pour demander la page d'accueil de Medium et extraire les textes de tous les éléments qui correspondent à `.ds-nav-item` :

```
import scrapeIt from "scrape-it";
```

```
export function getTopics() {
  return scrapeIt("https://medium.com", {
    topics: {
      listItem: ".ds-nav-item"
    }
  }).then(({ data }) => data.topics);
}
```

```
// Utilisation
getTopics().then(console.log);
// [ 'Home', 'Tech', 'Culture', 'Entrepreneurship', 'Self', 'Politics', 'Media', 'Design', 'Science', 'Work', 'Popular', 'More' ]
```

👌 Cela a l'air bien !

Maintenant, comment pourrions-nous simuler la requête réelle dans notre test ? Une façon d'y parvenir serait d'aller sur medium.com dans notre navigateur, de voir la source et de copier/coller cela dans un Nock manuellement. C'est fastidieux et sujet aux erreurs. Si nous voulons vraiment le document HTML entier, nous pourrions aussi bien laisser l'ordinateur s'en charger pour nous.

Il s'avère que [Nock a un mécanisme intégré](https://github.com/node-nock/nock#recording) appelé « Recording ». Cela vous permet d'utiliser les intercepteurs Nock pour intercepter le trafic HTTP réel, puis de stocker la paire requête/réponse dans un fichier et d'utiliser cet **enregistrement** pour les requêtes futures.

Personnellement, j'ai trouvé la fonctionnalité des enregistrements Nock très utile, mais l'ergonomie pourrait être améliorée. Alors voici mon [plug éhonté pour `nock-record`](https://github.com/edorivai/nock-record), une bibliothèque plus ergonomique pour exploiter les enregistrements :

![Image](https://cdn-media-1.freecodecamp.org/images/0*jojs7J_uR9k56M3C.)
_Capture d'écran de nock-record en action. Montrant comment une première exécution de test envoie des requêtes HTTP réelles, et les exécutions suivantes utiliseront les enregistrements de la première exécution pour prévenir les futures requêtes._

Voyons comment nous pourrions tester notre scraper en utilisant `nock-record` :

```
import { setupRecorder } from 'nock-record';
import { getTopics } from './index';
```

```
const record = setupRecorder();
```

```
describe('#getTopics', () => {
  it('devrait obtenir tous les sujets', async () => {
    // Démarrer l'enregistrement, spécifier le nom de la fixture
    const { completeRecording } = await record('medium-topics');
```

```
    // Notre fonction réelle sous test
    const result = await getTopics();
    // Compléter l'enregistrement, permettre à Nock d'écrire les fixtures
    completeRecording();
    expect(result).toEqual([
      'Home',
      'Tech',
      'Culture',
      'Entrepreneurship',
      'Self',
      'Politics',
      'Media',
      'Design',
      'Science',
      'Work',
      'Popular',
      'More'
    ]);
  });
});
```

La première fois que nous exécutons ce test, il envoie la requête réelle pour récupérer le HTML de la page d'accueil de Medium :

```
✓ devrait obtenir tous les sujets (1163ms)
```

Après cette première exécution, `nock-record` a sauvegardé l'enregistrement dans un fichier à 
`__nock-fixtures__/medium-topics.json`. Pour la deuxième exécution, `nock-record` chargera automatiquement l'enregistrement et configurera un Nock pour vous.

```
✓ devrait obtenir tous les sujets (116ms)
```

Si vous avez déjà utilisé les snapshots Jest, ce flux de travail vous sera très familier.

Nous avons maintenant obtenu 3 choses en exploitant les enregistrements :

1. Déterministes : votre test s'exécutera toujours contre le même document HTML
2. Rapide : les tests suivants ne toucheront pas le réseau
3. Ergonomique : pas besoin de jongler manuellement avec les fixtures de réponse

### Faites-moi savoir ce que vous en pensez

L'approche que j'ai décrite dans cet article a bien fonctionné pour moi. J'aimerais entendre parler de votre expérience dans les commentaires ou sur Twitter : [@EdoRivai](https://twitter.com/EdoRivai).

Même chose pour `nock-record` ; les [problèmes](https://github.com/edorivai/nock-record/issues) et les [PR](https://github.com/edorivai/nock-record/pulls) sont les bienvenus !