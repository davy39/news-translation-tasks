---
title: Comment tester une application Socket.io-client en utilisant Jest et la react-testing-library
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-13T12:33:33.000Z'
originalURL: https://freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3
coverImage: https://cdn-media-1.freecodecamp.org/images/0*hO-7lLXvx8RG6CAQ
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: Testing
  slug: testing
seo_title: Comment tester une application Socket.io-client en utilisant Jest et la
  react-testing-library
seo_desc: 'By Justice Mba

  Testing the quality of real-time Socket.io-client integration seems to have sunk
  into oblivion, maybe because the UIs had a long history of testability issues. Let’s
  fix this!

  Quickly google “testing socket.io app”.

  The first two resul...'
---

Par Justice Mba

Tester la qualité de l'intégration en temps réel de Socket.io-client semble avoir sombré dans l'oubli, peut-être parce que les interfaces utilisateur avaient une longue histoire de problèmes de testabilité. Réparons cela !

Faites rapidement une recherche Google pour "testing socket.io app".

Les deux premières pages de résultats (ne vous donnez pas la peine d'ouvrir le reste des pages) sont toutes des exemples et des tutoriels axés sur le test de l'intégration côté serveur de socket.io. Personne ne parle de la qualité de l'intégration de socket.io-client sur le front-end, de l'apparence de l'interface utilisateur lorsqu'elle reçoit certains événements, et si le code front-end émet réellement les bons événements.

Mais pourquoi ? Cela signifie-t-il que les gens ne se soucient pas vraiment de la qualité de leurs applications en temps réel sur le front-end — le cœur du logiciel ? Je ne le pense pas. Mon hypothèse est : Tester les interfaces utilisateur **était** **simplement trop difficile !**

Les interfaces utilisateur ont une longue histoire de problèmes de testabilité. Les interfaces utilisateur ne sont jamais stables. Les outils de test que nous avons eus à notre disposition nous ont facilement conduit à écrire des tests d'interface utilisateur très fragiles. Ainsi, les gens tendent à concentrer leur temps et leur énergie sur le test de leurs applications socket.io uniquement côté serveur.

Mais cela ne semble pas correct. C'est **seulement** l'interface utilisateur qui donne confiance à notre utilisateur qu'il accomplit réellement le but de l'utilisation de notre application. Mais alors, un outil de test d'interface utilisateur nous a été donné !

### react-testing-library

Cela fait quelques mois, mon ami et mentor [Kent C. Dodds](https://www.freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3/undefined) [a publié cet outil magnifique](https://blog.kentcdodds.com/introducing-the-react-testing-library-e3a274307e65) pour tester les applications React. Depuis lors, je n'aime plus seulement l'**idée** de tester les interfaces utilisateur, mais j'aime réellement les tester. J'ai littéralement déterré et testé tout le code d'interface utilisateur que j'avais abandonné à cause de sa complexité :).

Selon mon opinion basée sur l'expérience, la react-testing-library est la panacée pour tous les problèmes de test d'interface utilisateur. Ce n'est pas seulement un outil de test, c'est une approche de test.

Note : Si vous n'êtes pas une personne React, il existe [vue-testing-library](https://www.npmjs.com/package/vue-testing-library), [ng-testing-library](https://www.npmjs.com/package/ng-testing-library) et [d'autres](https://www.npmjs.com/browse/depended/dom-testing-library), tous construits sur la [dom-testing-library](https://www.npmjs.com/package/dom-testing-library).

La meilleure fonctionnalité de la react-testing-library est probablement son support du TDD pour les interfaces utilisateur. Selon la documentation, son [principe directeur principal](https://twitter.com/kentcdodds/status/977018512689455106) est :

> _Plus vos tests ressemblent à la manière dont votre logiciel est utilisé, plus ils peuvent vous donner confiance._

C'est l'« approche » dont je parle. Testez vos interfaces utilisateur comme le ferait votre ami non-technicien. Votre utilisateur ne connaît probablement pas et ne se soucie pas de l'apparence de votre code. Et il en va de même pour votre test. Cela nous donne le pouvoir d'utiliser le TDD sur nos interfaces utilisateur.

C'est ainsi que nous allons écrire notre test socket.io-client — tester tout sans penser au code. Maintenant, faisons-le !

### Tester l'application Telegram

De notre très talentueux designer d'interface utilisateur Telegram, voici les designs de l'application Telegram que nous allons tester.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-DkSudIVU8WGeLQTWeZf8g@2x.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5s82AK1rmhshHVic0XCpXA@2x.jpeg)
_captures d'écran de chat telegram_

En regardant le design, je vois plusieurs fonctionnalités en temps réel que notre utilisateur voudrait s'assurer que l'application performe, sinon ils fermeront l'onglet. En voici quelques-unes :

* L'application devrait recevoir des messages
* L'application devrait indiquer quand/un message est envoyé ou non
* L'application devrait indiquer quand/un message est livré ou non
* L'application devrait indiquer quand un ami se connecte/se déconnecte
* L'application devrait indiquer quand un ami est en train d'écrire

D'accord, la liste continue... mais travaillons d'abord sur celles-ci.

#### Réception de messages

Regardons comment un utilisateur saurait s'il a reçu un message comme exemple. Tout d'abord, créez un fichier de test, puis importez le fichier chat.js et ses dépendances mockées. Si vous êtes nouveau dans le mocking ou des choses comme ça, alors [Kent C. Dodds](https://www.freecodecamp.org/news/testing-socket-io-client-app-using-jest-and-react-testing-library-9cae93c070a3/undefined) devrait vraiment être votre ami. Il a tout couvert sur les tests JavaScript, alors suivez-le ici, sur Twitter, et partout ailleurs.

Maintenant, alors que j'écrivais cette ligne, je pensais qu'il devrait simplement écrire un livre sur les tests JS, alors j'ai tweeté :

Et espérons qu'il le fera éventuellement :)

Retour à notre fichier de test :

```
// chat.test.jsimport React from 'react';import io from 'socket.io-client';
```

```
import Chat from './chat';
```

Parce que nous ne faisons que des tests d'intégration ici, nous ne voulons pas vraiment émettre des événements socket.io vers le serveur. Nous devons donc mock socket.io-client. Pour plus d'informations sur le mocking, voir l'article de Kent « [Mais vraiment, qu'est-ce qu'un mock JavaScript ?](https://blog.kentcdodds.com/but-really-what-is-a-javascript-mock-10d060966f7d) » ainsi que cette section de la documentation Jest sur [les fonctions de mock de Jest](https://facebook.github.io/jest/docs/en/mock-functions.html#using-a-mock-function).

Une fois que vous comprenez comment mock, la prochaine chose est de comprendre ce que votre module fait, puis de simuler l'implémentation.

```
// socket.io-client.js
```

```
let EVENTS = {};
```

```
function emit(event, ...args) { EVENTS[event].forEach(func => func(...args));}
```

```
const socket = { on(event, func) {  if (EVENTS[event]) {   return EVENTS[event].push(func);  }  EVENTS[event] = [func]; }, emit};
```

```
export const io = { connect() {  return socket; }};
```

```
// Aides supplémentaires, non incluses dans le vrai socket.io-client, juste pour notre test.
```

```
// pour émuler l'émission du serveur.export const serverSocket = { emit }; // aide de nettoyageexport function cleanup() { EVENTS = {}}
```

```
export default io;
```

Avec cela, nous avons un mock socket.io-client suffisamment bon pour notre test. Utilisons-le.

```
// chat.test.jsimport React from 'react';import mockio, {serverSocket, cleanUp } from 'socket.io-client';
```

```
import Chat from './chat';
```

Maintenant, écrivons notre premier test. L'approche traditionnelle du TDD dit que nous allons écrire un test pour une fonctionnalité, voir qu'il échoue, puis aller implémenter la fonctionnalité pour satisfaire notre test. Pour plus de concision, nous n'allons pas faire _exactement_ cela, car cet article se concentre sur les tests.

En suivant l'approche de la react-testing-library, la première chose que vous faites avant d'écrire un test est de vous demander : « Comment un utilisateur testerait-il cette fonctionnalité ? » Pour le premier test de notre liste ci-dessus, vous vous demandez : « Comment un utilisateur saura-t-il qu'il reçoit les messages que son ami envoie ? ». Pour le tester, il dira probablement à la personne à côté de lui de lui envoyer un message.

Habituellement, cela fonctionnera de manière à ce que l'ami de l'utilisateur envoie un message au serveur, avec l'adresse de l'utilisateur, puis le serveur émet le message à l'utilisateur. Maintenant, puisque nous ne testons pas si l'utilisateur peut envoyer un message à ce moment-là, mais si l'utilisateur peut **recevoir** un message, faisons en sorte que le `socket.io server` envoie directement un message à l'utilisateur.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
test('App should get messages', () => {  // first render the app  const utils = render(<Chat />)    // then send a message  serverSocket.emit('message', 'Hey Wizy!');})
```

Ci-dessus, nous avons importé la méthode `render` de la react-testing-library, qui est simplement un wrapper autour de `ReactDom.render`. Dans notre texte, nous l'utilisons pour rendre notre application Chat. La méthode render retourne un objet utilitaire de test qui contient des méthodes de requête que nous pouvons utiliser pour interroger le `container` de notre application — le nœud DOM dans lequel `render` a rendu notre application — pour les nœuds DOM qui intéressent notre test. Ensuite, dans le texte, utilisez notre serveur socket.io mock pour envoyer un message à l'utilisateur.

Maintenant que nous avons envoyé un message à l'utilisateur, réfléchissez à nouveau : comment l'utilisateur saura-t-il qu'il a reçu le message ? D'après le design ci-dessus, il devra définitivement regarder l'écran pour voir le message apparaître. Pour tester cela, nous devons interroger le conteneur de notre application pour voir s'il contient un nœud contenant le message que nous avons envoyé, 'Hey Wizy!'. Pour cela, l'objet utilitaire retourné par `render` a une méthode de requête appelée `getByText`, donc nous pourrions simplement faire :

`expect(utils.getByText('Hey Wizy!')).toBeTruthy();`

Bien que cela puisse fonctionner, malheureusement, nous ne pouvons pas faire cela. Voici pourquoi : Toutes les méthodes de requête retournées par `render` rechercheront dans l'ensemble du conteneur la requête spécifiée. Cela signifie que `getByText`, tel qu'utilisé ci-dessus, recherchera dans l'ensemble du conteneur le texte 'Hey Wizy!', puis retournera le premier nœud contenant ce texte.

Mais ce n'est pas ainsi que notre utilisateur recherchera le texte. Au lieu de cela, notre utilisateur ne regardera que **dans** la 'section des messages', la section qui contient tous les messages. Ce n'est que si les messages apparaissent dans cette section qu'ils sauront qu'ils ont reçu un message. Donc, pour nous assurer que notre test ressemble à la manière dont l'utilisateur utilise notre application, nous devrons rechercher le texte 'Hey Wizy!' **uniquement dans** la section des messages, tout comme l'utilisateur le ferait.

Pour cela, la react-testing-library nous fournit une méthode de requête unique appelée `within`, qui nous aide à concentrer notre requête **dans** une section particulière du document rendu. Utilisons-la !

Note : `within` est une nouvelle API qui a été inspirée par cet article, alors assurez-vous d'avoir la toute dernière version de la react-testing-library.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, within} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
test('App should get messages', () => {  // first render the app  const utils = render(<Chat />)    // then send a message  serverSocket.emit('message', 'Hey Wizy!');    // the message must appear in the message-section  const messageSection = utils.getByTestId('message-section');  // check withing messageSection to find the received message  const message = within(messageSection).getByText('Hey Wizy!');})
```

Tout d'abord, nous avons récupéré la section des messages avec une méthode de requête `getByTestId`. Pour utiliser `getByTestId` dans votre test, vous devez le coder en dur dans le DOM. Comme ceci :

`<div data-testid="message-section"` />

Parce que `getByTestId` ne ressemble pas de près à la manière dont les utilisateurs localisent les sections de votre application, vous ne devriez l'utiliser que dans des cas spéciaux et seulement lorsque vous êtes certain qu'il n'y a pas de meilleure alternative.

Néanmoins, notre test ne dépend pas de la structure du DOM. Même si quelqu'un change le `div` en une balise `section` ou l'enveloppe 10 niveaux plus profond dans le DOM, notre test ne se soucie pas du code — il ne se soucie que de l'ID de test.

Enfin, nous utilisons la méthode `within` comme décrit précédemment pour obtenir le message reçu. Si le texte n'est pas trouvé, `getByText` lancera une erreur et fera échouer notre test.

Et c'est ainsi que nous affirmons que l'application peut recevoir des messages.

#### Écriture de plus de tests

Regardons quelques autres méthodes de requête que la react-test-library nous offre. Nous verrons comment nous pouvons combiner davantage les API que nous avons déjà apprises pour effectuer des requêtes plus complexes sans dépendre du code de l'interface utilisateur.

Alors maintenant, écrivons le deuxième test : l'application devrait indiquer à l'utilisateur quand/un message a été envoyé ou non. De plus, je pense que ce test fait essentiellement la même chose que le suivant dans la liste, alors fusionnons les deux en un seul exemple.

Encore une fois, la première question que nous posons est... ? Je sais que vous l'avez : « Comment notre utilisateur testerait-il cette fonctionnalité ? » D'accord, la manière dont vous formulez votre question peut être différente, mais vous comprenez l'idée :). Donc, pour tester la fonctionnalité d'envoi de message, les étapes ressembleront à ceci :

* L'utilisateur localise l'entrée pour saisir son message. Ensuite, il saisit son message. Enfin, il clique sur le bouton d'envoi.
* Le message devrait apparaître dans la section des messages
* Le serveur indiquera si le message est arrivé au serveur, ce qui signifie envoyé
* L'interface utilisateur devrait marquer le message comme envoyé
* Le serveur indique ensuite quand le message est livré
* L'interface utilisateur devrait, à son tour, mettre à jour le message comme livré

Comment l'utilisateur localise-t-il l'entrée pour saisir son message ? D'après le design de l'interface utilisateur sur lequel nous travaillons, ils doivent chercher et trouver l'entrée avec le placeholder 'message'. (Eh bien, c'est en fait la seule entrée à l'écran, mais même s'il y en a plus, l'utilisateur identifiera l'entrée pour saisir son message par le placeholder ou l'étiquette.)

La react-testing-library nous couvre à nouveau avec une méthode de requête appelée `getByPlaceholderText`

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, renderIntoDocument, within, cleanup} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
afterEach(cleanup);
```

```
test('App should get messages', () => {  // ...})
```

```
test('App should tell when message is sent and delivered', () => {  // first render the app  const utils= renderIntoDocument(<Chat />)    // enter and send a message  utils.getByPlaceholderText('message').value = 'Hello';  utils.getByTestId('send-btn').click()})
```

Nous avons donc introduit quelques nouvelles API ici. La première est la méthode `renderIntoDocument`. Nous devons déclencher de vrais événements DOM, pas les simuler, dans notre test, car cela ressemble plus à la manière dont les utilisateurs utilisent notre application.

L'inconvénient est que la méthode `render` crée et rend notre application dans un nœud DOM arbitraire, appelé `container`, à la volée. Mais React gère les événements via la délégation d'événements — attachant un seul événement pour tous les types d'événements sur le `document`, puis déléguant l'événement au nœud DOM approprié qui a déclenché l'événement.

Donc, pour déclencher de vrais événements DOM, nous devons réellement rendre notre application dans `document.body`. C'est ce que `renderIntoDocument` fait pour nous.

Parce que nous rendons dans le document, nous voulons toujours nous assurer que le document est nettoyé après chaque test. Vous avez deviné juste, la fonction d'aide **cleanup** le fait pour nous.

Dans le test, après avoir saisi la valeur, nous cliquons sur le bouton d'envoi pour envoyer notre message. Si vous avez remarqué, en regardant le design, il n'y a pas de bouton d'envoi. Mais si vous sortez votre Telegram ou WhatsApp maintenant, vous remarquerez que le bouton d'envoi n'apparaît que lorsque vous avez réellement saisi du texte dans l'entrée de message. Notre test vient de couvrir accidentellement cette fonctionnalité. :)

Maintenant que nous avons cliqué sur le bouton d'envoi, faisons quelques assertions.

```
// chat.test.jsimport React from 'react';import mock-io, {serverSocket, cleanUp } from 'socket.io-client';import {render, renderIntoDocument, within, cleanup} from 'react-testing-library';
```

```
import Chat from './chat';
```

```
afterEach(cleanup);
```

```
test('App should get messages', () => {  // ...})
```

```
test('App should tell when message is sent/delivered', () => {  // first render the app  const utils = renderIntoDocument(<Chat />)    // enter and send a message  utils.getByPlaceholderText('message').value = 'Hello';  utils.getByTestId('send-btn').click();    // the message should appear on the message section  const messageSection = uitils.getByTestId('message-section');  expect(within(messageSection).getByText('Hello')).toBeTruthy();    // server tells us message is sent  serverSocket.emit('message-sent');
```

```
  // Now the UI should mark the message as sent  const message = within(messageSection).getByText('Hello');  expect(within(message).getByTestId('sentIcon')).toBeTruthy();
```

```
  // server tells us it's delivered  serverSocket.emit('message-delivered');
```

```
  // UI should mark the message as delivered  expect(within(message).getByTestId('deliveredIcon')).toBeTruthy();})
```

Et c'est tout. Tout comme l'utilisateur s'y attendrait, notre test s'attend à voir l'icône envoyé/livré apparaître à côté du message lorsqu'il est envoyé/livré.

Jusqu'à présent, nous avons vu à quel point il est facile de tester une application socket.io-client en temps réel avec la react-testing-library. Peu importe ce que vous testez, lorsque vous suivez cette approche, vous gagnez plus de confiance que votre application fonctionne comme elle le devrait. Et ce qui est plus, nous n'avons **aucune idée** de ce à quoi ressemblera l'implémentation de l'application. Tout comme l'utilisateur, **notre test ne se soucie pas de l'implémentation !**

### Finalisation

Enfin, je vous laisse réfléchir à la manière d'écrire les deux derniers tests restants de notre liste :

* L'application devrait indiquer quand un ami se connecte/se déconnecte
* L'application devrait indiquer quand un ami est en train d'écrire

Conseil : Vous devriez faire en sorte que le serveur socket.io émette l'événement, puis vous affirmez ce à quoi l'interface utilisateur ressemblera. Réfléchissez à la manière **exacte** dont l'utilisateur saura quand un ami est en train d'écrire, en ligne, hors ligne.

Si vous pensez que j'ai fait un bon travail et que d'autres méritent une chance de voir cela, applaudissez cet article pour aider à diffuser une meilleure approche de test des applications socket.io-client en temps réel.

Si vous avez une question qui n'a pas été répondue ou si vous avez un avis différent sur certains des points ici, n'hésitez pas à laisser des commentaires ici ou via [Twitter](https://twitter.com/Daajust).

Vous pourriez aussi vouloir me suivre ici et/ou sur Twitter pour plus d'articles géniaux à venir. Et vous pourriez aimer vérifier mes articles précédents :

* [Vous voulez une meilleure compréhension de Buffer dans Node.js ? Jetez un coup d'œil à cela](https://medium.freecodecamp.org/do-you-want-a-better-understanding-of-buffer-in-node-js-check-this-out-2e29de2968e8?source=user_profile---------2-------------------)
* [setState fonctionnel est l'avenir de React](https://medium.freecodecamp.org/functional-setstate-is-the-future-of-react-374f30401b6b)