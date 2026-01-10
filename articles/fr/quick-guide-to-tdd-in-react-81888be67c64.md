---
title: Un guide rapide pour le développement piloté par les tests dans React
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T19:42:31.000Z'
originalURL: https://freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64
coverImage: https://cdn-media-1.freecodecamp.org/images/0*be_rcBa_vhJE6cVD.
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
seo_title: Un guide rapide pour le développement piloté par les tests dans React
seo_desc: 'By Michał Baranowski

  Following the principles of Test-Driven Development (TDD) when writing a front-end
  React app might seem more difficult than doing the same on the back-end.

  First, we need to somehow render our component. Then we need to simulate ...'
---

Par Michał Baranowski

Suivre les principes du **développement piloté par les tests** (TDD) lors de l'écriture d'une application front-end React peut sembler plus difficile que de faire de même sur le back-end.

Tout d'abord, nous devons somehow **rendre** notre composant. Ensuite, nous devons **simuler** l'interaction de l'utilisateur avec un navigateur. Ensuite, nous répondons aux changements dans les **props** et l'**état**, et enfin, nous trouvons un moyen de tester les méthodes **asynchrones** déclenchées par le clic d'un bouton.

Essayer de couvrir tous ces cas dans nos tests aboutit souvent à des tests difficiles à lire. Ils dépendent également souvent les uns des autres. Nous faisons beaucoup de mocks, et en retour, nous avons des tests pleins d'anti-patterns.

### Ne perdez pas votre temps

D'après ce que j'ai vu, de nombreux programmeurs créent d'abord des composants React fonctionnels. Ensuite, ils essaient de les couvrir avec des tests, pour réaliser que les composants ne peuvent pas être testés dans leur implémentation actuelle. Ensuite, ils doivent refactoriser. À cause de cela, ils perdent patience, temps et l'argent de leur employeur.

### Solutions disponibles

Heureusement pour nous, il existe de nombreuses bibliothèques de test qui peuvent nous aider à résoudre ces problèmes. Nous pouvons essayer de rendre les composants React avec [**Enzyme**](https://github.com/airbnb/enzyme) et simuler les réponses de l'API en utilisant [**MockAxios**](https://github.com/ctimmerm/axios-mock-adapter). Cependant, ces bibliothèques ont généralement tellement de méthodes et d'options qu'il peut devenir confus, surtout pour les personnes qui viennent de commencer à écrire des tests.

Prenons **Enzyme** par exemple — quelle est la différence entre les méthodes **Shallow**, **Mount** et **Render** ? Et laquelle devriez-vous utiliser ? Ce n'est pas ce dont vous devriez vous soucier lorsque vous écrivez vos tests, à mon avis. Cela devrait être aussi simple que possible.

### Notre projet

Pour les besoins de notre guide rapide, nous allons créer une petite application React. Après avoir cliqué sur un bouton, une blague aléatoire sur [Chuck Norris](https://pl.wikipedia.org/wiki/Chuck_Norris) sera récupérée et affichée.

> Personne n'a jamais programmé en binôme avec Chuck Norris et vécu pour en parler.

Alors, commençons.

Lancez-vous en créant un projet React dans [**CodeSandbox**](https://codesandbox.io/s/new)**,** puis installez les dépendances suivantes (J**est** est déjà préinstallé si vous avez commencé à partir du lien ci-dessus) :

* [**axios**](https://github.com/axios/axios) — utilisé pour récupérer des données depuis une API externe
* [**axios-mock-adapter**](https://github.com/ctimmerm/axios-mock-adapter) — utilisé pour simuler les réponses du serveur
* [**react-testing-library**](https://github.com/kentcdodds/react-testing-library) — bibliothèque de test légère et facile à utiliser pour le rendu, la simulation d'actions et la gestion des méthodes asynchrones — créée par [Kent C. Dodds](https://www.freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64/undefined)
* [**jest**](https://facebook.github.io/jest/) — pour exécuter les tests et créer des assertions

#### Structure des dossiers/fichiers

* **src/index.js** — point d'entrée de notre application React
* **src/jokeGenerator.js** — notre composant [conteneur](https://medium.com/@dan_abramov/smart-and-dumb-components-7ca2f9a7c7d0) qui récupère, contrôle et fournit les données
* **src/joke.js** — simple composant de présentation
* **src/__tests__/jokeGenerator.test.js** — contient nos tests

#### Votre premier test

Chaque fois avant de créer un composant, **nous allons d'abord écrire un test qui échoue, puis essayer de le faire passer**. Commençons par écrire un test pour notre composant factice **<Joke />** qui affichera un texte à partir des props.

![Image](https://cdn-media-1.freecodecamp.org/images/Hex65Vqu6mUtqCS1F1-5mJDDes-ua5BSTSNK)
_jokeGenerator.test.js_

En lisant de haut en bas : nous utilisons une méthode [render](https://github.com/kentcdodds/react-testing-library#render) de la **react-testing-library** et passons le composant **<Joke />** (qui n'existe pas encore à ce stade) dedans. Elle retourne un objet contenant quelques méthodes très utiles (trouvez la liste complète des méthodes disponibles [ici](https://github.com/kentcdodds/react-testing-library#render)) — par exemple **getByTestId**. Elle retourne ensuite un élément HTML basé sur **data-testid** en tant qu'argument.

Ensuite, nous écrivons une **expectation** en utilisant la méthode ci-dessus et **data-testid**, et vérifions si l'élément contient le texte des props. Après avoir exécuté les tests, nous obtenons :

> Joke is not defined

Oui, nous voulons qu'il échoue ! **<Joke />** n'existe pas encore, vous vous souvenez ? Nous avons seulement créé un fichier _joke.js_ vide jusqu'à présent. Nous avons écrit un test dans lequel nous pouvons clairement voir ce que nous attendons du composant. Maintenant, notre travail est de faire **passer le test sans modifier le code de test**. Faisons cela alors :

![Image](https://cdn-media-1.freecodecamp.org/images/lCi4BrSPyRaCkptSkuZQO3d7UaBoJ7CZa9ue)
_joke.js_

Maintenant, si vous avez tout fait comme moi, le test devrait passer :)

#### Deuxième composant

Notre deuxième composant sera responsable de la récupération d'une blague aléatoire après qu'un utilisateur ait cliqué sur un bouton. Nous la sauvegarderons dans l'état du composant et la passerons à notre composant **<Joke />**. Nous aimerions également afficher un message par défaut lorsqu'aucune blague n'a encore été chargée.

Bien sûr, nous commençons par le test d'abord. C'est un composant plus grand, donc nous allons écrire le test étape par étape. Nous allons également nous assurer qu'il passe aussi souvent que possible.

![Image](https://cdn-media-1.freecodecamp.org/images/wZoc7qf8aDj-omViRiELm9UNsZ89RgibccoP)
_jokeGenerator.test.js_

Nous sommes déjà familiers avec la méthode **render**, mais cette fois nous utilisons **getByText** à partir de l'objet retourné. Comme vous l'avez peut-être deviné, la méthode retourne un élément HTML s'il existe dans le DOM.

Exécutez les tests et...

> JokeGenerator is not defined

Vous savez quoi en faire :

![Image](https://cdn-media-1.freecodecamp.org/images/Q5hr0EZ7poKO-fuA2kfkuSAo-nBiWpLSZPx5)
_jokeGenerator.js_

Le test échoue toujours, mais cette fois il affiche une erreur différente :

> Unable to find an element with the text.

**Vous n'avez pas encore chargé de blagues**. Cela pourrait être dû au fait que le texte est divisé par plusieurs éléments. Dans ce cas, vous pouvez fournir une fonction pour votre matcher de texte afin de rendre votre matcher plus flexible.

Corrigeons rapidement cela en introduisant un **état** dans notre composant et en affichant un message par défaut lorsqu'il n'y a pas de **blague** dans l'**état**.

![Image](https://cdn-media-1.freecodecamp.org/images/5RfACQ6NeneEtE4Fz9XHpysVjaBO4zO7a1A8)
_jokeGenerator.js_

Les tests passent maintenant, donc nous pouvons passer à l'ajout de nouvelles fonctionnalités. Imaginez que lorsque nous cliquons sur un bouton, le texte par défaut dans le composant disparaît pour laisser place à un message "_Chargement..._ ". Cela semble assez simple, n'est-ce pas ? Nous pouvons tester ce scénario avec seulement **trois** lignes de code !

Commençons par importer la méthode **Simulate**, car nous allons en avoir besoin :

> import { render, Simulate } from "react-testing-library"

![Image](https://cdn-media-1.freecodecamp.org/images/gGK6Sfw3gmdLpdjyQqgZFRWYJe5kYXU88HlD)
_Ajoutez-le à notre deuxième test — jokeGenerator.test.js_

La différence entre **queryByText** et **getByText** réside dans ce que chacune retourne lorsque l'élément n'est pas trouvé. La première retourne **null** et la seconde lance un **message d'erreur**. En relançant les tests :

> Unable to find an element with the text: **Load a random joke**...

Nous devons créer un bouton et définir la méthode **onClick** qui définira l'état **loading** à **true**.

![Image](https://cdn-media-1.freecodecamp.org/images/uoGJiY5bC4-yyK5HpLuREFgnlSdavInme7rV)
_jokeGenerator.js_

Comme ça, le test passe à nouveau. Maintenant, il est temps de récupérer notre blague aléatoire ! Eh bien... elle ne sera pas aléatoire dans nos tests. Nous allons la simuler en utilisant **MockAxios**.

> import * as axios from "axios"  
> import MockAxios from "axios-mock-adapter"

Au-dessus de nos tests dans **jokeGenerator.test.js**, insérez ces deux lignes de code :

![Image](https://cdn-media-1.freecodecamp.org/images/VA9ve3xfI5JUv-vznDWIHRIs7QEkl3ooEcJC)
_Insérez au-dessus de tous les tests — jokeGenerator.test.js_

La première ligne crée une nouvelle instance de **MockAxios** avec un délai aléatoire. La deuxième ligne prend et exécute une fonction de rappel après avoir exécuté tous les tests dans ce fichier, et supprime l'état simulé de **axios**.

En haut de notre deuxième test où nous testons le composant **<JokeGenerator />**, ajoutez :

![Image](https://cdn-media-1.freecodecamp.org/images/nSEIfJmjCd5aaTwFb0mEK9SrNp6zRwXvuzXV)
_Haut du deuxième test — jokeGenerator.test.js_

Cela simule la réponse de tout appel **GET** effectué via **axios**. À la fin du même test :

![Image](https://cdn-media-1.freecodecamp.org/images/Ssf6gSyjvVaJ4G1MtujRqjSq7whZIksqXnG3)
_jokeGenerator.test.js_

N'oubliez pas d'importer **wait** :

> import { render, Simulate, wait } from "react-testing-library"

La méthode **wait** attend (4500 ms par défaut) jusqu'à ce qu'une fonction de rappel cesse de lancer une erreur. Elle est vérifiée à des intervalles de 50 ms. En gros, nous attendons simplement que le message de chargement disparaisse du DOM.

[**wait**](https://github.com/TheBrainFamily/wait-for-expect) est également disponible en tant que package [npm](https://github.com/TheBrainFamily/wait-for-expect) séparé (**react-testing-library** l'utilise comme dépendance). Il a été créé par [Łukasz Gozda Gandecki](https://www.freecodecamp.org/news/quick-guide-to-tdd-in-react-81888be67c64/undefined).

Après avoir apporté toutes les modifications de code et exécuté les tests, nous devrions obtenir le message d'échec suivant :

> Expected the element **not** to be present  
> Received : <div>Loading…</div>

Qu'en pensez-vous ? Selon notre test, nous nous attendons à ce que le message de chargement ait disparu. De plus, nous voulons récupérer notre blague depuis l'API et la sauvegarder dans l'**état** afin que la prochaine **expectation** passe.

![Image](https://cdn-media-1.freecodecamp.org/images/RiBFROcMESY6up039OAXvaOtUb3vsReZWCM8)
_jokeGenerator.js_

![Image](https://cdn-media-1.freecodecamp.org/images/ZEaKt3f6itVBQb5lzlg2Vq0G2nMZd-48mLGv)
_Insérez dans la méthode render() — jokeGenerator.js_

Les tests devraient à nouveau passer. Nous sommes sûrs que tout fonctionne comme prévu... n'est-ce pas ? Remarquez que nous **n'avons jamais ouvert notre navigateur et vérifié manuellement si notre application fonctionne**... Cependant, grâce à la manière dont nous avons écrit nos tests ([de sorte que nos tests ressemblent à la manière dont l'utilisateur utiliserait l'application](https://twitter.com/kentcdodds/status/977018512689455106)), nous pouvons être presque sûrs à 100 % que notre petite application fonctionne simplement.

En tant que dernier morceau de code, ajoutons ceci à index.js et ouvrons le navigateur :)

![Image](https://cdn-media-1.freecodecamp.org/images/PzjDJRbEJAjgV6qTqIzxIC8FRfXptZI2HnWO)
_index.js_

### Bonus

Grâce à la manière dont nous avons écrit nos tests, nous pouvons les utiliser comme tests **e2e sans ajouter une seule ligne de code !** Tout ce que nous devons faire est de supprimer toutes les lignes liées à **MockAxios** et relancer les tests ! Ils utiliseront maintenant une vraie API externe. Cool, n'est-ce pas ? :)

### Résumé

Tout le code est disponible sur le projet [**CodeSandbox**](https://codesandbox.io/s/6yq6v1xk3)**.** Je vous encourage vraiment à vous familiariser avec la documentation complète de [**react-testing-library**](https://github.com/kentcdodds/react-testing-library). Vous y trouverez de nombreux autres exemples et cas d'utilisation.

J'espère que vous avez apprécié mon **Guide rapide du TDD dans React**, et que vous avez appris quelque chose de nouveau aujourd'hui.