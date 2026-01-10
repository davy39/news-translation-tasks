---
title: Comment commencer les tests unitaires de votre code JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-24T10:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-start-unit-testing-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/ferenc-almasi-EWLHA4T-mso-unsplash-1.jpg
tags:
- name: JavaScript
  slug: javascript
- name: Software Testing
  slug: software-testing
- name: unit testing
  slug: unit-testing
seo_title: Comment commencer les tests unitaires de votre code JavaScript
seo_desc: 'By Ondrej Polesny

  We all know we should write unit tests. But, it''s hard to know where to start and
  how much time to devote to tests compared to actual implementation. So, where to
  start? And is it just about testing code or do unit tests have other ...'
---

Par Ondrej Polesny

Nous savons tous que nous devrions écrire des tests unitaires. Mais il est difficile de savoir par où commencer et combien de temps consacrer aux tests par rapport à l'implémentation réelle. Alors, par où commencer ? Et s'agit-il uniquement de tester le code ou les tests unitaires ont-ils d'autres avantages ?

Dans cet article, je vais expliquer les différents types de tests et les avantages que les tests unitaires apportent aux équipes de développement. Je vais présenter Jest - un framework de test JavaScript.

## Différents types de tests

Avant de plonger dans les spécificités des tests unitaires, je souhaite faire un rapide tour d'horizon des différents types de tests. Il y a souvent une certaine confusion à leur sujet et je ne suis pas surpris. Parfois, la ligne entre eux est assez fine.

### Tests unitaires

Les tests unitaires ne testent qu'une seule partie de votre implémentation. Une unité. Aucune dépendance ou intégration, aucune spécificité de framework. Ils sont comme une méthode qui retourne un lien dans une langue spécifique :

```js
export function getAboutUsLink(language){
  switch (language.toLowerCase()){
    case englishCode.toLowerCase():
      return '/about-us';
    case spanishCode.toLowerCase():
      return '/acerca-de';
  }
  return '';
}
```

### Tests d'intégration

À un moment donné, votre code communique avec une base de données, un système de fichiers ou un autre tiers. Il pourrait même s'agir d'un autre module dans votre application.

Cette partie de l'implémentation doit être testée par des tests d'intégration. Ils ont généralement une configuration plus compliquée qui implique la préparation d'environnements de test, l'initialisation des dépendances, etc.

### Tests fonctionnels

Les tests unitaires et les tests d'intégration vous donnent confiance que votre application fonctionne. Les tests fonctionnels examinent l'application du point de vue de l'utilisateur et testent que le système fonctionne comme prévu.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/presentation.jpg)

Dans le diagramme ci-dessus, vous voyez que les tests unitaires forment la grande base de la suite de tests de votre application. Typiquement, ils sont petits, nombreux et exécutés automatiquement.

Alors maintenant, plongeons un peu plus dans les détails des tests unitaires.

## Pourquoi devrais-je me donner la peine d'écrire des tests unitaires ?

Chaque fois que je demande aux développeurs s'ils ont écrit des tests pour leur application, ils me répondent toujours : "Je n'ai pas eu le temps pour eux" ou "Je n'en ai pas besoin, je sais que ça marche."

Alors je souris poliment et je leur dis ce que je veux vous dire. Les tests unitaires ne concernent pas seulement les tests. Ils vous aident également de autres manières, afin que vous puissiez :

**Être confiant que votre code fonctionne.** Quand était la dernière fois que vous avez commis un changement de code, votre build a échoué et la moitié de votre application a cessé de fonctionner ? La mienne était la semaine dernière.

Mais ce n'est toujours pas grave. Le vrai problème est lorsque le build réussit, le changement est déployé et votre application commence à être instable.

Lorsque cela se produit, vous commencez à perdre confiance en votre code et finissez par simplement prier pour que l'application fonctionne. Les tests unitaires vous aideront à découvrir les problèmes beaucoup plus tôt et à gagner en confiance.

**Prendre de meilleures décisions architecturales.** Le code change, mais certaines décisions concernant la plateforme, les modules, la structure et autres doivent être prises dès les premières étapes d'un projet.

Lorsque vous commencez à réfléchir aux tests unitaires dès le début, cela vous aidera à mieux structurer votre code et à atteindre une séparation appropriée des préoccupations. Vous ne serez pas tenté d'assigner plusieurs responsabilités à des blocs de code uniques, car ceux-ci seraient un cauchemar à tester unitairement.

**Définir la fonctionnalité avant de coder.** Vous écrivez la signature de la méthode et commencez à l'implémenter immédiatement. Oh, mais que devrait-il se passer si un paramètre est nul ? Et si sa valeur est en dehors de la plage attendue ou contient trop de caractères ? Lancez-vous une exception ou retournez-vous nul ?

Les tests unitaires vous aideront à découvrir tous ces cas. Regardez à nouveau les questions et vous trouverez que c'est exactement ce qui définit vos cas de test unitaires.

Je suis sûr qu'il y a beaucoup plus d'avantages à écrire des tests unitaires. Ce sont juste ceux dont je me souviens de mon expérience. Ceux que j'ai appris à la dure.

## Comment écrire votre premier test unitaire JavaScript

Mais revenons à JavaScript. Nous allons commencer avec [Jest](https://jestjs.io/), qui est un framework de test JavaScript. C'est un outil qui permet les tests unitaires automatiques, fournit une couverture de code et nous permet de simuler facilement des objets. Jest a également une extension pour Visual Studio Code [disponible ici](https://marketplace.visualstudio.com/items?itemName=Orta.vscode-jest).

Il existe également d'autres frameworks, si vous êtes intéressé, vous pouvez les vérifier dans [cet article](https://www.browserstack.com/guide/top-javascript-testing-frameworks).

```js
npm i jest --save-dev
```

Utilisons la méthode mentionnée précédemment `getAboutUsLink` comme implémentation que nous voulons tester :

```js
const englishCode = "en-US";
const spanishCode = "es-ES";
function getAboutUsLink(language){
    switch (language.toLowerCase()){
      case englishCode.toLowerCase():
        return '/about-us';
      case spanishCode.toLowerCase():
        return '/acerca-de';
    }
    return '';
}
module.exports = getAboutUsLink;
```

J'ai mis cela dans le fichier `index.js`. Nous pouvons écrire des tests dans le même fichier, mais une bonne pratique est de séparer les tests unitaires dans un fichier dédié.

Les modèles de nommage courants incluent `{filename}.test.js` et `{filename}.spec.js`. J'ai utilisé le premier, `index.test.js` :

```js
const getAboutUsLink = require("./index");
test("Retourne about-us pour la langue anglaise", () => {
    expect(getAboutUsLink("en-US")).toBe("/about-us");
});
```

Tout d'abord, nous devons importer la fonction que nous voulons tester. Chaque test est défini comme une invocation de la fonction `test`. Le premier paramètre est le nom du test pour votre référence. L'autre est une fonction fléchée où nous appelons la fonction que nous voulons tester et spécifions quel résultat nous attendons.

Dans ce cas, nous appelons la fonction `getAboutUsLink` avec `en-US` comme paramètre de langue. Nous attendons que le résultat soit `/about-us`.

Maintenant, nous pouvons installer l'interface de ligne de commande Jest globalement et exécuter le test :

```js
npm i jest-cli -g
jest
```

Si vous voyez une erreur liée à la configuration, assurez-vous que votre fichier `package.json` est présent. Dans le cas contraire, générez-en un en utilisant `npm init`.

Vous devriez voir quelque chose comme ceci :

```js
 PASS  ./index.test.js
  ✓ Retourne about-us pour la langue anglaise (4ms)
  console.log index.js:15
    /about-us
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        2.389s
```

Excellent travail ! C'était le premier test unitaire JavaScript simple du début à la fin. Si vous avez installé l'extension Visual Studio Code, elle exécutera les tests automatiquement dès que vous enregistrerez un fichier. Essayons-le en étendant le test avec cette ligne :

```js
expect(getAboutUsLink("cs-CZ")).toBe("/o-nas");
```

Dès que vous enregistrez le fichier, Jest vous informera que le test a échoué. Cela vous aide à découvrir les problèmes potentiels même avant de valider vos modifications.

## Tester des fonctionnalités avancées et simuler des services

Dans la vie réelle, les codes de langue pour la méthode getAboutUsLink ne seraient pas des constantes dans le même fichier. Leur valeur est généralement utilisée dans tout le projet, donc ils seraient définis dans leur propre module et importés dans toutes les fonctions qui les utilisent.

```js
import { englishCode, spanishCode } from './LanguageCodes'
```

Vous pouvez importer ces constantes dans le test de la même manière. Mais la situation se compliquera si vous travaillez avec des objets au lieu de simples constantes. Jetez un œil à cette méthode :

```js
import { UserStore } from './UserStore'
function getUserDisplayName(){
  const user = UserStore.getUser(userId);
  return `${user.LastName}, ${user.FirstName}`;
}
```

Cette méthode utilise l'importé `UserStore` :

```js
class User {
    getUser(userId){
        // logique pour obtenir des données d'une base de données
    }
    setUser(user){
        // logique pour stocker des données dans une base de données
    }
}
let UserStore = new User();
export { UserStore }
```

Afin de tester correctement cette méthode, nous devons simuler `UserStore`. Un mock est un substitut pour l'objet original. Il nous permet de séparer les dépendances et les données réelles de l'implémentation de la méthode testée, tout comme des mannequins aident aux crash tests de voitures au lieu de vraies personnes.

Si nous n'utilisions pas le mock, nous testerions à la fois cette fonction et le store. Cela serait un test d'intégration et nous devrions probablement simuler la base de données utilisée.

### Simuler un service

Pour simuler des objets, vous pouvez soit fournir une fonction de simulation ou un mock manuel. Je vais me concentrer sur ce dernier car j'ai un cas d'utilisation simple et clair. Mais n'hésitez pas à [découvrir d'autres possibilités de simulation que Jest propose](https://jestjs.io/docs/en/mock-functions.html).

```js
jest.mock('./UserStore', () => ({
  UserStore: ({
    getUser: jest.fn().mockImplementation(arg => ({
      FirstName: 'Ondrej',
      LastName: 'Polesny'
    })),
    setUser: jest.fn()
  })
}));
```

Tout d'abord, nous devons spécifier ce que nous simulons - le module `./UserStore`. Ensuite, nous devons retourner le mock qui contient tous les objets exportés de ce module.

Dans cet exemple, il s'agit uniquement de l'objet `User` nommé `UserStore` avec la fonction `getUser`. Mais avec des implémentations réelles, le mock peut être beaucoup plus long. Toutes les fonctions dont vous ne vous souciez pas vraiment dans le cadre des tests unitaires peuvent être facilement simulées avec `jest.fn()`.

Le test unitaire pour la fonction `getUserDisplayName` est similaire à celui que nous avons créé précédemment :

```js
test("Retourne le nom d'affichage", () => {
  expect(getUserDisplayName(1)).toBe("Polesny, Ondrej");
})
```

Dès que j'enregistre le fichier, Jest me dit que j'ai 2 tests qui passent. Si vous exécutez les tests manuellement, faites-le maintenant et assurez-vous de voir le même résultat.

### Rapport de couverture de code

Maintenant que nous savons comment tester le code JavaScript, il est bon de couvrir autant de code que possible avec des tests. Et cela est difficile à faire. Après tout, nous sommes juste des humains. Nous voulons accomplir nos tâches et les tests unitaires entraînent généralement une charge de travail indésirable que nous avons tendance à négliger. La couverture de code est un outil qui nous aide à lutter contre cela.

La couverture de code vous indiquera quelle partie de votre code est couverte par des tests unitaires. Prenons par exemple mon premier test unitaire vérifiant la fonction `getAboutUsLink` :

```js
test("Retourne about-us pour la langue anglaise", () => {
  expect(getAboutUsLink("en-US")).toBe("/about-us");
});
```

Il vérifie le lien anglais, mais la version espagnole reste non testée. La couverture de code est de 50 %. L'autre test unitaire vérifie minutieusement la fonction `getDisplayName` et sa couverture de code est de 100 %. Ensemble, la couverture totale de code est de 67 %. Nous avions 3 cas d'utilisation à tester, mais nos tests n'en couvrent que 2.

Pour voir le rapport de couverture de code, tapez la commande suivante dans le terminal :

```js
jest --coverage
```

Ou, si vous utilisez Visual Studio Code avec l'extension Jest, vous pouvez exécuter la commande (CTRL+SHIFT+P) _Jest: Toggle Coverage Overlay_. Elle vous montrera directement dans l'implémentation quelles lignes de code ne sont pas couvertes par des tests.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/code-coverage-inline.jpg)

En exécutant la vérification de la couverture, Jest créera également un rapport HTML. Trouvez-le dans votre dossier de projet sous `coverage/lcov-report/index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/code-coverage.jpg)

Maintenant, je n'ai pas besoin de mentionner que vous devriez vous efforcer d'atteindre une couverture de code de 100 %, n'est-ce pas ? :-)

## Résumé

Dans cet article, je vous ai montré comment commencer avec les tests unitaires en JavaScript. Bien qu'il soit agréable d'avoir votre couverture de code briller à 100 % dans le rapport, en réalité, il n'est pas toujours possible d'y parvenir (de manière significative). L'objectif est de laisser les tests unitaires vous aider à maintenir votre code et à garantir qu'il fonctionne toujours comme prévu. Ils vous permettent de :

* définir clairement les exigences d'implémentation,
* mieux concevoir votre code et séparer les préoccupations,
* découvrir les problèmes que vous pourriez introduire avec vos nouveaux commits,
* et vous donner confiance que votre code fonctionne.

Le meilleur endroit pour commencer est la page [Getting started](https://jestjs.io/docs/en/getting-started) dans la documentation de Jest afin que vous puissiez essayer ces pratiques par vous-même.

Avez-vous votre propre expérience avec les tests de code ? J'adorerais l'entendre, faites-le moi savoir sur [Twitter](https://twitter.com/ondrabus) ou rejoignez l'un de mes [streams Twitch](https://twitch.tv/ondrabus).