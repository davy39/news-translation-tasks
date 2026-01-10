---
title: Une introduction au développement piloté par les tests
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2019-02-04T16:44:44.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-test-driven-development-c4de6dce5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*UILpgckM9QDwSXuy6l1WTg.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: TDD (Test-driven development)
  slug: tdd
- name: 'tech '
  slug: tech
- name: unit testing
  slug: unit-testing
seo_title: Une introduction au développement piloté par les tests
seo_desc: I’ve been programming for five years and, honestly, I have avoided test-driven
  development. I haven’t avoided it because I didn’t think it was important. In fact,
  it seemed very important–but rather because I was too comfortable not doing it.
  That’s ...
---

Je programme depuis cinq ans et, honnêtement, j'ai évité le développement piloté par les tests. Je ne l'ai pas évité parce que je ne pensais pas que c'était important. En fait, cela semblait très important, mais plutôt parce que j'étais trop à l'aise de ne pas le faire. Cela a changé.

### Qu'est-ce que le test ?

Le test est le processus qui consiste à s'assurer qu'un programme reçoit les entrées correctes et génère les sorties correctes et les effets secondaires prévus. Nous définissons ces entrées, sorties et effets secondaires corrects avec des *spécifications*. Vous avez peut-être vu des fichiers de test avec la convention de nommage `filename.spec.js`. Le `spec` signifie spécification. C'est le fichier où nous spécifions ou *affirmons* ce que notre code devrait faire et où nous le testons ensuite pour vérifier qu'il le fait.

Vous avez deux choix en matière de test : le test manuel et le test automatisé.

#### Test manuel

Le test manuel est le processus de vérification de votre application ou de votre code du point de vue de l'utilisateur. Ouvrir le navigateur ou le programme et naviguer pour tester la fonctionnalité et trouver des bugs.

#### Test automatisé

Le test automatisé, en revanche, consiste à écrire du code qui vérifie si d'autres codes fonctionnent. Contrairement au test manuel, les spécifications restent constantes d'un test à l'autre. Le plus grand avantage est de pouvoir tester *de nombreuses* choses beaucoup plus rapidement.

C'est la combinaison de ces deux techniques de test qui permettra de détecter le plus grand nombre de bugs et d'effets secondaires non intentionnels, et de s'assurer que votre programme fait ce que vous dites qu'il fera. L'accent de cet article est mis sur le test automatisé, et en particulier, le test unitaire.

> Il existe deux principaux types de tests automatisés : les tests unitaires et les tests de bout en bout (E2E). Les tests E2E testent une application dans son ensemble. Les tests unitaires testent les plus petites parties du code, ou unités. Qu'est-ce qu'une unité ? Eh bien, nous définissons ce qu'est une unité, mais en général, c'est une partie relativement petite de la fonctionnalité de l'application.

#### Récapitulatif :

1. Le test consiste à vérifier que notre application fait ce qu'elle devrait faire.

2. Il existe deux types de tests : manuel et automatisé.

3. Les tests *affirment* que votre programme se comportera d'une certaine manière. Ensuite, le test lui-même prouve ou réfute cette affirmation.

### Développement piloté par les tests

Le développement piloté par les tests est l'acte de décider d'abord ce que vous voulez que votre programme fasse (les spécifications), de formuler un test qui échoue, *puis* d'écrire le code pour faire passer ce test. Il est le plus souvent associé au test automatisé. Bien que vous puissiez appliquer les principes au test manuel également.

Prenons un exemple simple : construire une table en bois. Traditionnellement, nous fabriquerions une table, puis, une fois la table faite, nous la testerions pour nous assurer qu'elle fait, eh bien, ce qu'une table devrait faire. Le TDD, en revanche, nous ferait d'abord définir ce que la table devrait faire. Ensuite, lorsqu'elle ne fait pas ces choses, ajouter la quantité minimale de "table" pour faire fonctionner chaque unité.

Voici un exemple de TDD pour construire une table en bois :

```python
Je m'attends à ce que la table ait quatre pieds de diamètre.

Le test échoue parce que je n'ai pas de table.

Je coupe un morceau de bois circulaire de quatre pieds de diamètre.

Le test passe.

__________

Je m'attends à ce que la table ait trois pieds de haut.

Le test échoue parce qu'elle est posée sur le sol.

J'ajoute un pied au milieu de la table.

Le test passe.

__________

Je m'attends à ce que la table supporte un objet de 20 livres.

Le test échoue parce que lorsque je place l'objet sur le bord, il fait tomber la table puisque qu'il n'y a qu'un seul pied au milieu.

Je déplace le pied unique vers le bord extérieur de la table et j'ajoute deux autres pieds pour créer une structure en trépied.

Le test passe.
```

Cela continuerait ainsi jusqu'à ce que la table soit complète.

#### Récapitulatif

1. Avec le TDD, la logique de test précède la logique de l'application.

### Un exemple pratique

Imaginez que nous avons un programme qui gère les utilisateurs et leurs articles de blog. Nous avons besoin d'un moyen de suivre les articles qu'un utilisateur écrit dans notre base de données avec plus de précision. Actuellement, l'utilisateur est un objet avec une propriété de nom et d'email :

```js
user = { 
   name: 'John Smith', 
   email: 'js@somePretendEmail.com' 
}
```

Nous allons suivre les articles qu'un utilisateur crée dans le même objet utilisateur.

```js
user = { 
   name: 'John Smith', 
   email: 'js@someFakeEmailServer.com'
   posts: [Array Of Posts] // <-----
}
```

Chaque article a un titre et un contenu. Au lieu de stocker l'article entier avec chaque utilisateur, nous aimerions stocker quelque chose d'unique qui pourrait être utilisé pour référencer l'article. Nous avons d'abord pensé que nous stockerions le titre. Mais, si l'utilisateur change jamais le titre, ou si - bien que peu probable - deux titres sont exactement les mêmes, nous aurions quelques problèmes pour référencer cet article de blog. Au lieu de cela, nous allons créer un identifiant unique pour chaque article de blog que nous stockerons dans l'objet `user`.

```js
user = { 
   name: 'John Smith', 
   email: 'js@someFakeEmailServer.com'
   posts: [Array Of Post IDs]
}
```

#### Configurer notre environnement de test

Pour cet exemple, nous allons utiliser Jest. Jest est une suite de test. Souvent, vous aurez besoin d'une bibliothèque de test et d'une bibliothèque d'assertion séparée, mais Jest est une solution tout-en-un.

> Une bibliothèque d'assertion nous permet de faire des assertions sur notre code. Donc dans notre exemple de table en bois, notre assertion est : "Je m'attends à ce que la table supporte un objet de 20 livres." En d'autres termes, j'affirme quelque chose sur ce que la table devrait faire.

#### Configuration du projet

1. Créez un projet NPM : `npm init`.

2. Créez `id.js` et ajoutez-le à la racine du projet.

3. Installez Jest : `npm install jest --D`

4. Mettez à jour le script `test` du package.json

```json
// package.json

{
   ...other package.json stuff
   "scripts": {   
     "test": "jest" // cela exécutera jest avec "npm run test"
   }
}
```

C'est tout pour la configuration du projet ! Nous n'allons pas avoir de HTML ou de style. Nous abordons cela purement du point de vue des tests unitaires. Et, croyez-le ou non, nous avons assez pour exécuter Jest maintenant.

Dans la ligne de commande, exécutez notre script de test : `npm run test`.

Vous devriez avoir reçu une erreur :

```bash
No tests found
In /****/
  3 files checked.
  testMatch: **/__tests__/**/*.js?(x),**/?(*.)+(spec|test).js?(x) - 0 matches
  testPathIgnorePatterns: /node_modules/ - 3 matches
```

Jest recherche un nom de fichier avec certaines caractéristiques spécifiques telles que `.spec` ou `.test` contenu dans le nom de fichier.

Mettons à jour `id.js` pour qu'il soit `id.spec.js`.

Exécutez le test à nouveau

Vous devriez recevoir une autre erreur :

```bash
FAIL  ./id.spec.js
   25cf Test suite failed to run
  
Your test suite must contain at least one test.
```

Un peu mieux, il a trouvé le fichier, mais pas de test. Cela a du sens ; c'est un fichier vide.

#### Comment écrivons-nous un test ?

Les tests sont simplement des fonctions qui reçoivent quelques arguments. Nous pouvons appeler notre test avec soit `it()` ou `test()`.

> `it()` est un alias de `test()`.

Écrivons un test très basique juste pour nous assurer que Jest fonctionne.

```js
// id.spec.js

test('Jest fonctionne', () => {
   expect(1).toBe(1);
});
```

Exécutez le test à nouveau.

```bash
PASS  ./id.spec.js
   2713 Jest fonctionne (3ms)
  
Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
Snapshots:   0 total
Time:        1.254s
Ran all test suites.
```

Nous avons réussi notre premier test ! Analysons le test et les résultats de la sortie.

Nous passons un titre ou une description comme premier argument.

`test('Jest fonctionne')`

Le deuxième argument que nous passons est une fonction où nous affirmons réellement quelque chose sur notre code. Bien que, dans ce cas, nous n'affirmions pas quelque chose sur notre code, mais plutôt quelque chose de vrai en général qui passera, une sorte de vérification de santé.

`...() => { expect(1).toBe(1)` });

Cette affirmation est mathématiquement vraie, donc c'est un test simple pour s'assurer que nous avons correctement configuré Jest.

Les résultats nous indiquent si le test passe ou échoue. Il nous indique également le nombre de tests et de suites de tests.

#### Une note à propos de l'organisation de nos tests

Il y a une autre façon dont nous pourrions organiser notre code. Nous pourrions envelopper chaque test dans une fonction `describe`.

```js
describe('Premier groupe de tests', () => {
   test('Jest fonctionne', () => {
      expect(1).toBe(1);
   });
});

describe('Un autre groupe de tests', () => {
   // ...plus de tests ici
});
```

`describe()` nous permet de diviser nos tests en sections :

```bash
PASS  ./id.spec.js
  Premier groupe de tests
     2713 Jest fonctionne (4ms)
     2713 Un autre test (1ms)
  Un autre groupe de tests
     2713 Et un autre test
     2713 Encore un test (12ms)
     2713 Et oui, encore un test
```

Nous n'utiliserons pas `describe`, mais *il est* plus courant que non de voir une fonction `describe` qui enveloppe les tests. Ou même quelques `describes` - peut-être un pour chaque fichier que nous testons. Pour nos besoins, nous nous concentrerons simplement sur `test` et garderons les fichiers assez simples.

#### Test basé sur les spécifications

Aussi tentant que cela puisse être de simplement s'asseoir et commencer à taper la logique de l'application, un plan bien formulé rendra le développement plus facile. Nous devons définir ce que notre programme fera. Nous définissons ces objectifs avec des spécifications.

Notre spécification de haut niveau pour ce projet est de créer un identifiant unique, bien que nous devrions le décomposer en unités plus petites que nous testerons. Pour notre petit projet, nous utiliserons les spécifications suivantes :

1. Créer un nombre aléatoire

2. Le nombre est un entier.

3. Le nombre créé est dans une plage spécifiée.

4. Le nombre est unique.

#### Récapitulatif

1. Jest est une suite de test et dispose d'une bibliothèque d'assertion intégrée.

2. Un test est simplement une fonction dont les arguments définissent le test.

3. Les spécifications définissent ce que notre code devrait faire et sont finalement ce que nous testons.

### Spécification 1 : Créer un nombre aléatoire

JavaScript dispose d'une fonction intégrée pour créer des nombres aléatoires - `Math.random()`. Notre premier test unitaire vérifiera si un nombre aléatoire a été créé et retourné. Ce que nous voulons faire, c'est utiliser `math.random()` pour créer un nombre, puis nous assurer que c'est le nombre qui est retourné.

Vous pourriez donc penser que nous ferions quelque chose comme ceci :

`expect(our-functions-output).toBe(some-expected-value)`. Le problème avec notre valeur de retour étant aléatoire, c'est que nous n'avons aucun moyen de savoir à quoi nous attendre. Nous devons réassigner la fonction `Math.random()` à une valeur constante. Ainsi, lorsque notre fonction s'exécute, Jest remplace `Math.random()` par quelque chose de constant. Ce processus est appelé *mocking*. Donc, ce que nous testons vraiment, c'est que `Math.random()` est appelé et retourne une valeur attendue que nous pouvons planifier.

Maintenant, Jest fournit également un moyen de prouver qu'une fonction est appelée. Cependant, dans notre exemple, cette assertion seule ne nous assure que `Math.random()` a été appelé quelque part dans notre code. Elle ne nous dira pas que le résultat de `Math.random()` était également la valeur de retour.

> Pourquoi voudriez-vous mock une fonction ? N'est-ce pas le but de tester le vrai code ? Oui et non. De nombreuses fonctions contiennent des choses que nous ne pouvons pas contrôler, par exemple une requête HTTP. Nous n'essayons pas de tester ce code. Nous supposons que ces dépendances feront ce qu'elles sont censées faire ou créons des fonctions fictives qui simulent leur comportement. Et, dans le cas où ces dépendances sont des dépendances que nous avons écrites, nous écrivons probablement des tests séparés pour elles.

Ajoutez le test suivant à `id.spec.js`

```js
test('retourne un nombre aléatoire', () => {
   const mockMath = Object.create(global.Math);
   mockMath.random = jest.fn(() => 0.75);
   global.Math = mockMath;
   const id = getNewId();
   expect(id).toBe(0.75);
});
```

#### Décomposition du test ci-dessus

Tout d'abord, nous copions l'objet Math global. Ensuite, nous changeons la méthode `random` pour qu'elle retourne une valeur constante, quelque chose que nous pouvons *attendre*. Enfin, nous remplaçons l'objet `Math` global par notre objet `Math` mocké.

Nous devrions obtenir un ID d'une fonction (que nous n'avons pas encore créée - rappelez-vous que c'est du TDD). Ensuite, nous nous attendons à ce que cet ID soit égal à 0,75 - notre valeur de retour mockée.

> Remarquez que j'ai choisi d'utiliser une méthode intégrée que Jest fournit pour mock les fonctions : `jest.fn()`. Nous aurions également pu passer une fonction anonyme à la place. Cependant, je voulais vous montrer cette méthode, car il y aura des moments où une fonction mockée par Jest sera nécessaire pour que d'autres fonctionnalités de nos tests fonctionnent.

Exécutez le test : `npm run test`

```bash
FAIL  ./id.spec.js
 2715 retourne un nombre aléatoire (4ms)
 25cf retourne un nombre aléatoire
   ReferenceError: getNewId is not defined
```

Remarquez que nous obtenons une erreur de référence comme nous le devrions. Notre test ne peut pas trouver notre `getNewId()`.

Ajoutez le code suivant au-dessus du test.

```js
function getNewId() {
   Math.random()
}
```

> Je garde le code et les tests dans le même fichier pour simplifier. Normalement, le test serait écrit dans un fichier séparé, avec toutes les dépendances importées au fur et à mesure qu'elles sont nécessaires.

```bash
FAIL  ./id.spec.js
    2715 retourne un nombre aléatoire (4ms)
    25cf retourne un nombre aléatoire
   
   expect(received).toBe(expected) // Object.is equality
   Expected: 0.75
   Received: undefined
```

Nous avons échoué à nouveau avec ce qu'on appelle une *erreur d'assertion*. Notre première erreur était une erreur de référence. Cette deuxième erreur nous indique qu'elle a reçu `undefined`. Mais nous avons appelé `Math.random()` alors qu'est-ce qui s'est passé ? Rappelez-vous, les fonctions qui ne retournent pas explicitement quelque chose retourneront implicitement `undefined`. Cette erreur est un bon indice que quelque chose n'était pas défini comme une variable, ou, comme dans notre cas, notre fonction ne retourne rien.

Mettez à jour le code comme suit :

```js
function getNewId() {
   return Math.random()
}
```

Exécutez le test

```bash
PASS  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)

Test Suites: 1 passed, 1 total
Tests:       1 passed, 1 total
```

Félicitations ! Nous avons réussi notre premier test.

> Idéalement, nous voulons obtenir nos erreurs d'assertion aussi rapidement que possible. Les erreurs d'assertion - spécifiquement les *erreurs d'assertion de valeur* comme celle-ci, bien que nous aborderons les *erreurs d'assertion booléennes* dans un instant - nous donnent des indices sur ce qui ne va pas.

### Spécification 2 : Le nombre que nous retournons est un entier.

`Math.random()` génère un nombre entre 0 et 1 (non inclus). Le code que nous avons ne générera jamais un tel entier. Ce n'est pas grave, c'est du TDD. Nous vérifierons si c'est un entier, puis nous écrirons la logique pour transformer notre nombre en entier.

Alors, comment vérifions-nous si un nombre est un entier ? Nous avons quelques options. Rappelez-vous, nous avons mocké `Math.random()` ci-dessus, et nous retournons une valeur constante. En fait, nous créons également une valeur réelle puisque nous retournons un nombre entre 0 et 1 (non inclus). Si nous retournions une chaîne, par exemple, nous ne pourrions pas faire passer ce test. Ou, d'un autre côté, si nous retournions un entier pour notre valeur mockée, le test passerait toujours (faussement).

Un point clé à retenir est que si vous allez utiliser des valeurs de retour mockées, elles doivent être réalistes afin que nos tests retournent des informations significatives avec ces valeurs.

Une autre option serait d'utiliser `Number.isInteger()`, en passant notre ID comme argument et en voyant si cela retourne vrai.

Enfin, sans utiliser les valeurs mockées, nous pourrions comparer l'ID que nous obtenons avec sa version entière.

Regardons les options 2 et 3.

**Option 2 : Utilisation de Number.isInteger()**

```js
test('retourne un entier', () => {
   const id = getRandomId();
   expect(Number.isInteger(id)).toBe(true);
});
```

Le test échoue comme il se doit.

```bash
FAIL  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2715 retourne un entier (3ms)

 25cf retourne un entier
expect(received).toBe(expected) // Object.is equality

Expected: true
Received: false
```

Le test échoue avec une *erreur d'assertion booléenne*. Rappelez-vous, il y a plusieurs façons dont un test peut échouer. Nous voulons qu'ils échouent avec des erreurs d'assertion. En d'autres termes, notre assertion n'est pas ce que nous disons qu'elle est. Mais encore plus, nous voulons que notre test échoue avec des *erreurs d'assertion de valeur*.

Les erreurs d'assertion booléennes (erreurs vrai/faux) ne nous donnent pas beaucoup d'informations, mais une erreur d'assertion de valeur le fait.

Revenons à notre exemple de table en bois. Maintenant, restez avec moi, les deux déclarations suivantes peuvent sembler maladroites et difficiles à lire, mais elles sont là pour souligner un point :

Tout d'abord, vous pourriez affirmer que **la table est bleue [pour être] vraie**. Dans une autre affirmation, vous pourriez affirmer **la couleur de la table [pour être] bleue**. Je sais, ces affirmations sont maladroites à dire et peuvent même sembler identiques, mais elles ne le sont pas. Jetez un coup d'œil à ceci :

`expect(table.isBlue).toBe(true)`

vs

`expect(table.color).toBe(blue)`

En supposant que la table n'est pas bleue, l'erreur du premier exemple vous dira qu'elle s'attendait à vrai mais a reçu faux. Vous n'avez aucune idée de la couleur de la table. Nous avons très bien pu oublier de la peindre complètement. L'erreur du deuxième exemple, cependant, pourrait vous dire qu'elle s'attendait à bleu mais a reçu rouge. Le deuxième exemple est beaucoup plus informatif. Il pointe vers la racine du problème beaucoup plus rapidement.

Réécrivons le test, en utilisant l'option 2, pour recevoir une erreur d'assertion de valeur à la place.

```js
test('retourne un entier', () => {
   const id = getRandomId();
   expect(id).toBe(Math.floor(id));
});
```

Nous disons que nous nous attendons à ce que l'ID que nous obtenons de notre fonction soit égal au plancher de cet ID. En d'autres termes, si nous obtenons un entier, alors le plancher de cet entier est égal à l'entier lui-même.

```bash
FAIL  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2715 retourne un entier (4ms)
 25cf retourne un entier
expect(received).toBe(expected) // Object.is equality

Expected: 0
Received: 0.75
```

Wow, quelles sont les chances que cette fonction retourne juste la valeur mockée ! Eh bien, elles sont de 100 % en fait. Même si notre valeur mockée semble être limitée au premier test, nous réassignons en fait la valeur globale. Donc, peu importe à quel point cette réassignation est imbriquée, nous changeons l'objet `Math` global.

Si nous voulons changer quelque chose avant chaque test, il y a un meilleur endroit pour le mettre. Jest nous offre une méthode `beforeEach()`. Nous passons une fonction qui exécute tout code que nous voulons exécuter avant chacun de nos tests. Par exemple :

```js
beforeEach(() => {
   someVariable = someNewValue;
});

test(...)
```

Pour nos besoins, nous n'utiliserons pas cela. Mais changeons un peu notre code pour réinitialiser l'objet `Math` global à la valeur par défaut. Retournez dans le premier test et mettez à jour le code comme suit :

```js
test('retourne un nombre aléatoire', () => {
   const originalMath = Object.create(global.Math);
   const mockMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId();
   expect(id).toBe(0.75);
   global.Math = originalMath;
});
```

Ce que nous faisons ici, c'est sauvegarder l'objet `Math` par défaut avant de le réécrire, puis le réassigner après que notre test soit terminé.

Exécutons nos tests à nouveau, en nous concentrant spécifiquement sur notre deuxième test.

```bash
 2713 retourne un nombre aléatoire (1ms)
 2715 retourne un entier (3ms)
 25cf retourne un entier
expect(received).toBe(expected) // Object.is equality

Expected: 0
Received: 0.9080890805713182
```

Puisque nous avons mis à jour notre premier test pour revenir à l'objet `Math` par défaut, nous obtenons vraiment un nombre aléatoire maintenant. Et tout comme le test précédent, nous nous attendons à recevoir un entier, ou en d'autres termes, le plancher du nombre généré.

Mettons à jour notre logique d'application.

```js
function getRandomId() {
   return Math.floor(Math.random()); // convertir en entier
}

FAIL  ./id.spec.js
 2715 retourne un nombre aléatoire (5ms)
 2713 retourne un entier
 25cf retourne un nombre aléatoire
expect(received).toBe(expected) // Object.is equality
Expected: 0.75
Received: 0
```

Oh oh, notre premier test a échoué. Alors, qu'est-ce qui s'est passé ?

Eh bien, parce que nous mockons notre valeur de retour. Notre premier test retourne 0,75, peu importe quoi. Nous nous attendons, cependant, à obtenir 0 (le plancher de 0,75). Peut-être serait-il préférable de vérifier si `Math.random()` est appelé. Bien que cela soit quelque peu insignifiant, car nous pourrions appeler `Math.random()` n'importe où dans notre code, ne jamais l'utiliser, et le test passe toujours. Peut-être devrions-nous tester si notre fonction retourne un nombre. Après tout, notre ID doit être un nombre. Pourtant, nous testons déjà si nous recevons un entier. Et tous les entiers sont des nombres ; ce test serait redondant. Mais il y a un autre test que nous pourrions essayer.

Quand tout est dit et fait, nous nous attendons à obtenir un entier. Nous savons que nous utiliserons `Math.floor()` pour le faire. Donc peut-être pouvons-nous vérifier si `Math.floor()` est appelé avec `Math.random()` comme argument.

```js
test('retourne un nombre aléatoire', () => {
   jest.spyOn(Math, 'floor'); // <--------------------changed
   const mockMath = Object.create(global.Math); 
   const globalMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId();
   getNewId(); //<------------------------------------changed
   expect(Math.floor).toHaveBeenCalledWith(0.75); //<-changed
   global.Math = globalMath;
});
```

J'ai commenté les lignes que nous avons changées. Tout d'abord, portez votre attention vers la fin de l'extrait. Nous affirmons qu'une fonction a été appelée. Maintenant, revenez au premier changement : `jest.spyOn()`. Pour surveiller si une fonction a été appelée, jest nous demande soit de mock cette fonction, soit de l'espionner. Nous avons déjà vu comment mock une fonction, donc ici nous espionnons `Math.floor()`. Enfin, l'autre changement que nous avons fait était de simplement appeler `getNewId()` sans assigner sa valeur de retour à une variable. Nous n'utilisons pas l'ID, nous affirmons simplement qu'il appelle une fonction avec un argument.

Exécutons nos tests

```bash
PASS  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier

Test Suites: 1 passed, 1 total
Tests:       2 passed, 2 total
```

Félicitations pour un deuxième test réussi.

### Spécification 3 : Le nombre est dans une plage spécifiée.

Nous savons que `Math.random()` retourne un nombre aléatoire entre 0 et 1 (non inclus). Si le développeur veut retourner un nombre entre 3 et 10, que pourrait-elle faire ?

Voici la réponse :

`Math.floor(Math.random() * (max  2014 min + 1))) + min;`

Le code ci-dessus produira un nombre aléatoire dans une plage. Regardons deux exemples pour montrer comment cela fonctionne. Je vais simuler deux nombres aléatoires créés puis appliquer le reste de la formule.

**Exemple :** Un nombre entre 3 et 10. Nos nombres aléatoires seront .001 et .999. J'ai choisi les valeurs extrêmes comme nombres aléatoires afin que vous puissiez voir que le résultat final reste dans la plage.

`0.001 * (10-3+1) + 3 = 3.008` le plancher de cela est `3`

`0.999 * (10-3+1) + 3 = 10.992` le plancher de cela est `10`

Écrivons un test

```js
test('génère un nombre dans une plage spécifiée', () => {
   const id = getRandomId(10, 100);
   expect(id).toBeLessThanOrEqual(100);
   expect(id).toBeGreaterThanOrEqual(10);
});

FAIL  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier (1ms)
 2715 génère un nombre dans une plage spécifiée (19ms)

 25cf génère un nombre dans une plage spécifiée
expect(received).toBeGreaterThanOrEqual(expected)

Expected: 10
Received: 0
```

Le plancher de `Math.random()` sera toujours 0 jusqu'à ce que nous mettons à jour notre code. Mettez à jour le code.

```js
function getRandomId(min, max) {
   return Math.floor(Math.random() * (max - min + 1) + min);
}

FAIL  ./id.spec.js
 2715 retourne un nombre aléatoire (5ms)
 2713 retourne un entier (1ms)
 2713 génère un nombre dans une plage spécifiée (1ms)

 25cf retourne un nombre aléatoire

expect(jest.fn()).toHaveBeenCalledWith(expected)

Expected mock function to have been called with:

0.75 as argument 1, but it was called with NaN.
```

Oh non, notre premier test a échoué à nouveau ! Qu'est-ce qui s'est passé ?

Simple, notre test affirme que nous appelons `Math.floor()` avec `0.75`. Cependant, nous l'appelons en réalité avec 0.75 plus et moins une valeur max et min qui n'est pas encore définie. Ici, nous allons réécrire le premier test pour inclure une partie de nos nouvelles connaissances.

```js
test('retourne un nombre aléatoire', () => {
   jest.spyOn(Math, 'floor');
   const mockMath = Object.create(global.Math);
   const originalMath = Object.create(global.Math);
   mockMath.random = () => 0.75;
   global.Math = mockMath;
   const id = getNewId(10, 100);
   expect(id).toBe(78);
   global.Math = originalMath;
});

PASS  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier
 2713 génère un nombre dans une plage spécifiée (1ms)

Test Suites: 1 passed, 1 total
Tests:       3 passed, 3 total
```

Nous avons apporté quelques changements assez importants. Nous avons passé quelques nombres d'exemple à notre fonction (10, et 100 comme valeurs minimale et maximale), et nous avons changé notre assertion une fois de plus pour vérifier une certaine valeur de retour. Nous pouvons faire cela parce que nous savons que si `Math.random()` est appelé, la valeur est définie à 0.75. Et, lorsque nous appliquons nos calculs min et max à `0.75`, nous obtiendrons le même nombre à chaque fois, qui dans notre cas est 78.

Maintenant, nous devons commencer à nous demander si c'est même un bon test. Nous avons dû revenir en arrière et adapter notre test à notre code. Cela va un peu à l'encontre de l'esprit du TDD. Le TDD dit de changer votre code pour faire passer le test, pas de changer le test pour faire passer le test. Si vous vous retrouvez à essayer de corriger les tests pour qu'ils passent, cela peut être le signe d'un mauvais test. Pourtant, j'aimerais laisser le test ici, car il y a quelques bons concepts. Cependant, je vous exhorte à considérer l'efficacité d'un test comme celui-ci, ainsi qu'une meilleure façon de l'écrire, ou s'il est même crucial de l'inclure.

Revenons à notre troisième test qui consistait à générer un nombre dans une plage.

Nous voyons qu'il a réussi, mais nous avons un problème. Pouvez-vous y penser ?

La question que je me pose est de savoir si nous avons simplement de la chance ? Nous n'avons généré qu'un seul nombre aléatoire. Quelles sont les chances que ce nombre se trouve dans la plage et passe le test ?

Heureusement ici, nous pouvons mathématiquement prouver que notre code fonctionne. Cependant, pour le plaisir (si vous pouvez appeler cela du plaisir), nous allons envelopper notre code dans une boucle `for` qui s'exécute 100 fois.

```js
test('génère un nombre dans une plage définie', () => {
   for (let i = 0; i < 100; i ++) {
      const id = getRandomId(10, 100);    
   
      expect(id).toBeLessThanOrEqual(100);
      expect(id).toBeGreaterThanOrEqual(10);
      expect(id).not.toBeLessThan(10);
      expect(id).not.toBeGreaterThan(100);
   }
});
```

J'ai ajouté quelques nouvelles assertions. J'utilise `.not` uniquement pour démontrer d'autres API Jest disponibles.

```bash
PASS  ./id.spec.js
   2713 fonctionne (2ms)
   2713 Math.random() est appelé dans la fonction (3ms)
   2713 reçoit un entier de notre fonction (1ms)
   2713 génère un nombre dans une plage définie (24ms)
  
Test Suites: 1 passed, 1 total
Tests:       4 passed, 4 total
Snapshots:   0 total
Time:        1.806s
```

Avec 100 itérations, nous pouvons être assez confiants que notre code maintient notre ID dans la plage spécifiée. Vous pourriez également essayer de faire échouer le test intentionnellement pour une confirmation supplémentaire. Par exemple, vous pourriez changer l'une des assertions pour *ne pas* attendre une valeur supérieure à 50 mais toujours passer 100 comme argument maximum.

#### Est-il acceptable d'utiliser plusieurs assertions dans un seul test ?

Oui. Cela ne signifie pas que vous ne devriez pas essayer de réduire ces multiples assertions à une seule assertion plus robuste. Par exemple, nous pourrions réécrire notre test pour qu'il soit plus robuste et réduire nos assertions à une seule.

```js
test('génère un nombre dans une plage définie', () => {
   const min = 10;
   const max = 100;
   const range = [];
   for (let i = min; i < max+1; i ++) {
     range.push(i);
   }
   for (let i = 0; i < 100; i ++) {
      const id = getRandomId(min, max);
      expect(range).toContain(id);
   }
});
```

Ici, nous avons créé un tableau qui contient tous les nombres de notre plage. Nous vérifions ensuite si l'ID est dans le tableau.

### Spécification 4 : Le nombre est unique

Comment pouvons-nous vérifier si un nombre est unique ? Tout d'abord, nous devons définir ce que signifie unique pour nous. Très probablement, quelque part dans notre application, nous aurions accès à tous les identifiants déjà utilisés. Notre test devrait affirmer que le nombre généré n'est pas dans la liste des identifiants actuels. Il existe plusieurs façons de résoudre ce problème. Nous pourrions utiliser le `.not.toContain()` que nous avons vu précédemment, ou nous pourrions utiliser quelque chose avec `index`.

#### **indexOf()**

```js
test('génère un nombre unique', () => {
   const id = getRandomId();
   const index = currentIds.indexOf(id);
   expect(index).toBe(-1);
});
```

`array.indexOf()` retourne la position dans le tableau de l'élément que vous passez. Il retourne `-1` si le tableau ne contient pas l'élément.

```bash
FAIL  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier
 2713 génère un nombre dans une plage définie (25ms)
 2715 génère un nombre unique (10ms)

 25cf génère un nombre unique

ReferenceError: currentIds is not defined
```

Le test échoue avec une erreur de référence. `currentIds` n'est pas défini. Ajoutons un tableau pour simuler certains identifiants qui pourraient déjà exister.

```js
const currentIds = [1, 3, 2, 4];
```

Réexécutez le test.

```bash
PASS  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier
 2713 génère un nombre dans une plage définie (27ms)
 2713 génère un nombre unique

Test Suites: 1 passed, 1 total

Tests:       4 passed, 4 total
```

Bien que le test passe, cela devrait à nouveau soulever un drapeau rouge. Nous n'avons absolument *rien* qui garantit que le nombre est unique. Alors, qu'est-ce qui s'est passé ?

Encore une fois, nous avons de la chance. En fait, *votre* test a peut-être échoué. Bien que si vous l'exécutiez encore et encore, vous obtiendriez probablement un mélange des deux avec beaucoup plus de réussites que d'échecs en raison de la taille de `currentIds`.

Une chose que nous pourrions essayer est d'envelopper cela dans une boucle `for`. Une boucle `for` suffisamment grande causerait probablement notre échec, bien qu'il soit possible qu'elles passent toutes. Ce que nous pourrions faire, c'est vérifier si notre fonction `getNewId()` pourrait d'une manière ou d'une autre être consciente d'elle-même lorsqu'un nombre est ou n'est pas unique.

Par exemple, nous pourrions définir `currentIds = [1, 2, 3, 4, 5]`. Ensuite, appeler `getRandomId(1, 5)`. Notre fonction devrait réaliser qu'il n'y a aucune valeur qu'elle peut générer en raison des contraintes et renvoyer un message d'erreur. Nous pourrions tester ce message d'erreur.

```js
test('génère un nombre unique', () => {
   mockIds = [1, 2, 3, 4, 5];
   let id = getRandomId(1, 5, mockIds);
   expect(id).toBe('failed');
    
   id = getRandomId(1, 6, mockIds);
   expect(id).toBe(6);
});
```

Il y a quelques choses à remarquer. Il y a deux assertions. Dans la première assertion, nous nous attendons à ce que notre fonction échoue puisque nous la contraignons de manière à ce qu'elle ne doive pas retourner de nombre. Dans le deuxième exemple, nous la contraignons de manière à ce qu'elle ne doive pouvoir retourner que `6`.

```bash
FAIL  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier (1ms)
 2713 génère un nombre dans une plage définie (24ms)
 2715 génère un nombre unique (6ms)

 25cf génère un nombre unique

expect(received).toBe(expected) // Object.is equality

Expected: "failed"
Received: 1
```

Notre test échoue. Puisque notre code ne vérifie rien et ne retourne pas 'failed', cela est attendu. Bien que, il est possible que votre code ait reçu un nombre entre 2 et 6.

Comment pouvons-nous vérifier si notre fonction *ne peut pas* trouver un nombre unique ?

Tout d'abord, nous devons faire une sorte de boucle qui continuera à créer des nombres jusqu'à ce qu'elle en trouve un qui soit valide. À un moment donné, cependant, s'il n'y a pas de nombres valides, nous devons sortir de la boucle pour éviter une situation de boucle infinie.

Ce que nous allons faire, c'est garder une trace de chaque nombre que nous avons créé, et lorsque nous avons créé tous les nombres que nous pouvons, et qu'aucun de ces nombres ne passe notre vérification d'unicité, nous sortirons de la boucle et fournirons un retour.

```js
function getNewId(min = 0, max = 100, ids =[]) {
   let id;
   do {
      id = Math.floor(Math.random() * (max - min + 1)) + min;
   } while (ids.indexOf(id) > -1);
   return id;
}
```

Tout d'abord, nous avons refactorisé `getNewId()` pour inclure un paramètre qui est une liste des identifiants actuels. De plus, nous avons mis à jour nos paramètres pour fournir des valeurs par défaut dans le cas où ils ne sont pas spécifiés.

Deuxièmement, nous utilisons une boucle `do-while` puisque nous ne savons pas combien de fois il faudra pour créer un nombre aléatoire qui est unique. Par exemple, nous pourrions spécifier un nombre de 1 à 1000 avec le *seul* nombre indisponible étant 7. En d'autres termes, nos identifiants actuels ne contiennent qu'un seul 7. Bien que notre fonction ait 999 autres nombres à choisir, elle pourrait théoriquement produire le nombre 7 encore et encore. Bien que cela soit très improbable, nous utilisons une boucle `do-while` puisque nous ne sommes pas sûrs du nombre de fois où elle s'exécutera.

De plus, remarquez que nous sortons de la boucle lorsque notre identifiant *est* unique. Nous déterminons cela avec `indexOf()`.

Nous avons toujours un problème, avec le code tel qu'il est actuellement, s'il n'y a pas de nombres disponibles, la boucle continuera à s'exécuter et nous serons dans une boucle infinie. Nous devons garder une trace de tous les nombres que nous créons, afin de savoir quand nous avons épuisé les nombres.

```js
function getRandomId(min = 0, max = 0, ids =[]) {
   let id;
   let a = [];
   do {
      id = Math.floor(Math.random() * (max - min + 1)) + min;
      if (a.indexOf(id) === -1) {
         a.push(id);
      }
      if (a.length === max - min + 1) {
         if (ids.indexOf(id) > -1) {
            return 'failed';
         }
      }
   } while (ids.indexOf(id) > -1);
   return id;
}
```

Voici ce que nous avons fait. Nous résolvons ce problème en créant un tableau. Et chaque fois que nous créons un nombre, nous l'ajoutons au tableau (sauf s'il y est déjà). Nous savons que nous avons essayé chaque nombre au moins une fois lorsque la longueur de ce tableau est égale à la plage que nous avons choisie plus un. Si nous arrivons à ce point, nous avons créé le dernier nombre. Cependant, nous voulons toujours nous assurer que le dernier nombre que nous avons créé ne passe pas le test d'unicité. Parce que si c'est le cas, bien que nous voulions que la boucle soit terminée, nous voulons toujours retourner ce nombre. Sinon, nous retournons "failed".

```bash
PASS  ./id.spec.js
 2713 retourne un nombre aléatoire (1ms)
 2713 retourne un entier (1ms)
 2713 génère un nombre dans une plage définie (24ms)
 2713 génère un nombre unique (1ms)

Test Suites: 1 passed, 1 total

Tests:       4 passed, 4 total
```

Félicitations, nous pouvons livrer notre générateur d'ID et faire nos millions !

### Conclusion

Certaines des choses que nous avons faites étaient à des fins de démonstration. Tester si notre nombre était dans une plage spécifiée est amusant, mais cette formule peut être mathématiquement prouvée. Donc un meilleur test pourrait être de s'assurer que la formule est appelée.

De plus, vous pourriez être plus créatif avec le générateur d'ID aléatoire. Par exemple, s'il ne peut pas trouver un nombre unique, la fonction pourrait automatiquement augmenter la plage de un.

Une autre chose que nous avons vue est comment nos tests et même les spécifications pourraient se cristalliser un peu au fur et à mesure que nous testons et refactorisons. En d'autres termes, il serait stupide de penser que rien ne changera tout au long du processus.

En fin de compte, le développement piloté par les tests nous fournit un cadre pour penser à notre code à un niveau plus granulaire. C'est à vous, le développeur, de déterminer à quel point vos tests et assertions doivent être granulaires. Gardez à l'esprit que plus vous avez de tests et plus vos tests sont étroitement ciblés, plus ils deviennent étroitement couplés à votre code. Cela pourrait causer une réticence à refactoriser car vous devez maintenant également mettre à jour vos tests. Il y a certainement un équilibre dans le nombre et la granularité de vos tests. L'équilibre est à vous, le développeur, de le déterminer.

Merci d'avoir lu !

woz