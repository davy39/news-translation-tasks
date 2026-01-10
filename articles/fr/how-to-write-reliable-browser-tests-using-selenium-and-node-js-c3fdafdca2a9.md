---
title: Comment écrire des tests de navigateur fiables en utilisant Selenium et Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-09-23T20:45:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-reliable-browser-tests-using-selenium-and-node-js-c3fdafdca2a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*fCq0yqM563bKV4MFu8xufQ.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Testing
  slug: testing
seo_title: Comment écrire des tests de navigateur fiables en utilisant Selenium et
  Node.js
seo_desc: 'By Todd Chaffee

  There are many good articles on how to get started with automated browser testing
  using the NodeJS version of Selenium.

  Some wrap the tests in Mocha or Jasmine, and some automate everything with npm or
  Grunt or Gulp. All of them descr...'
---

Par Todd Chaffee

Il existe de nombreux bons articles sur la façon de commencer avec les tests de navigateur automatisés en utilisant la version NodeJS de Selenium.

Certains enveloppent les tests dans Mocha ou Jasmine, et d'autres automatisent tout avec npm ou Grunt ou Gulp. Tous décrivent comment installer ce dont vous avez besoin, ainsi qu'un exemple de code de base fonctionnel. Cela est très utile car faire fonctionner toutes les différentes pièces pour la première fois peut être un défi.

Mais ils ne creusent pas les détails des nombreux pièges et des meilleures pratiques de l'automatisation de vos tests de navigateur lors de l'utilisation de Selenium.

Cet article continue là où les autres articles s'arrêtent, et vous aidera à écrire des tests de navigateur automatisés qui sont beaucoup plus fiables et maintenables avec l'API Selenium NodeJS.

### Éviter les pauses

La méthode `driver.sleep` de Selenium est votre pire ennemi. Et tout le monde l'utilise. Cela peut être dû au fait que la documentation pour la version Node.js de [Selenium](http://seleniumhq.github.io/selenium/docs/api/javascript/) est succincte et ne couvre que la syntaxe de l'API. Elle manque d'exemples concrets.

Ou cela peut être dû au fait que de nombreux exemples de code dans des articles de blog et sur des sites de questions-réponses comme StackOverflow l'utilisent.

Supposons qu'un panneau s'anime d'une taille de zéro à une taille complète. Regardons.

![Image](https://cdn-media-1.freecodecamp.org/images/fZM47S1qIQzKxR-vdoT7fHbgtFwiAThAfK3V)

Cela se produit si rapidement que vous ne remarquez peut-être pas que les boutons et les contrôles à l'intérieur du panneau changent constamment de taille et de position.

Voici une version ralentie. Faites attention au bouton vert de fermeture et vous pouvez voir la taille et la position changeantes du panneau.

![Image](https://cdn-media-1.freecodecamp.org/images/qNLqqY3CqTVwjMjvtfWCUIjzgCLzMxhp6aXS)

Cela pose rarement un problème pour les utilisateurs réels car l'animation se produit si rapidement. Si elle était suffisamment lente, comme dans la deuxième vidéo, et que vous essayiez de cliquer manuellement sur le bouton de fermeture pendant que cela se produit, vous pourriez cliquer sur le mauvais bouton, ou manquer le bouton complètement.

Mais ces animations se produisent généralement si rapidement que vous n'avez jamais la chance de le faire. Les humains attendent simplement que l'animation se termine. Ce n'est pas le cas avec Selenium. Il est si rapide qu'il peut essayer de cliquer sur des éléments qui sont encore en cours d'animation, et vous pourriez obtenir un message d'erreur comme :

```
System.InvalidOperationException : Element is not clickable at point (326, 792.5)
```

C'est à ce moment-là que de nombreux programmeurs diront « Aha ! Je dois attendre que l'animation se termine, donc je vais simplement utiliser `driver.sleep(1000)` pour attendre que le panneau soit utilisable. »

#### Quel est donc le problème ?

L'instruction `driver.sleep(1000)` fait ce qu'elle semble faire. Elle arrête l'exécution de votre programme pendant 1000 millisecondes, et permet au navigateur de continuer à travailler. Faire la mise en page, estomper ou animer des éléments, charger la page, ou autre chose.

En utilisant l'exemple ci-dessus, si le panneau s'estompait sur une période de 800 millisecondes, le `driver.sleep(1000)` **fonctionnerait généralement** comme vous le souhaitez. Alors pourquoi ne pas l'utiliser ?

La raison la plus importante est qu'il n'est pas [déterministe](https://en.wikipedia.org/wiki/Deterministic_algorithm#What_makes_algorithms_non-deterministic.3F). Cela signifie qu'il ne fonctionnera que certaines fois. Puisqu'il ne fonctionne que certaines fois, nous nous retrouvons avec des tests fragiles qui se cassent dans certaines conditions. Cela donne une mauvaise réputation aux tests de navigateur automatisés.

Pourquoi ne fonctionne-t-il que certaines fois ? En d'autres termes, pourquoi n'est-il pas déterministe ?

Ce que vous remarquez avec vos yeux n'est souvent pas la seule chose qui se passe sur un site web. Un fondu ou une animation d'élément en est un parfait exemple. Nous ne sommes pas censés remarquer ces choses si elles sont bien faites.

Si vous dites à Selenium de trouver d'abord un élément puis de cliquer dessus, il peut n'y avoir que quelques millisecondes entre ces deux opérations. Selenium peut être beaucoup plus rapide qu'un humain.

Lorsque qu'un humain utilise le site web, nous attendons que l'élément s'estompe avant de cliquer dessus. Et lorsque cet estompage prend moins d'une seconde, nous ne remarquons probablement même pas que nous faisons cette « attente ». Selenium n'est pas seulement plus rapide et moins indulgent, vos tests automatisés doivent gérer toutes sortes d'autres facteurs imprévisibles :

1. Le concepteur de votre page web pourrait changer le temps d'animation de 800 millisecondes à 1200 millisecondes. *Votre test vient de se casser.*
2. Les navigateurs ne font pas toujours exactement ce que vous demandez. En raison de la charge du système, l'animation pourrait effectivement s'arrêter et prendre plus de 800 millisecondes, peut-être même plus que votre pause de 1000 millisecondes. *Votre test vient de se casser.*
3. Différents navigateurs ont différents moteurs de mise en page et priorisent les opérations de mise en page différemment. Ajoutez un nouveau navigateur à votre suite de tests et *vos tests viennent de se casser.*
4. Les navigateurs et le JavaScript qui contrôle une page sont asynchrones par nature. Si l'animation dans notre exemple change de fonctionnalité qui a besoin d'informations du back-end, le programmeur pourrait ajouter un appel AJAX et attendre le résultat avant de déclencher l'animation. 
Nous traitons maintenant de la latence du réseau et de la garantie nulle du temps qu'il faudra pour que le panneau s'affiche. *Votre test vient de se casser.*
5. Il y a sûrement d'autres raisons que je ne connais pas. 
Même **un** navigateur à lui seul est une bête complexe et tous ont des bugs. Nous parlons donc d'essayer de faire fonctionner la même chose sur plusieurs navigateurs différents, plusieurs versions de navigateurs différentes, plusieurs systèmes d'exploitation différents, et plusieurs versions de systèmes d'exploitation différentes. 
À un moment donné, *vos tests se cassent* s'ils ne sont pas déterministes. Pas étonnant que les programmeurs abandonnent les tests de navigateur automatisés et se plaignent de la fragilité des tests.

Que font généralement les programmeurs pour corriger les choses lorsque l'un des cas ci-dessus se produit ? Ils retracent les choses aux problèmes de timing, donc la réponse évidente est d'augmenter le temps dans l'instruction driver.sleep. Ensuite, ils croisent les doigts pour que cela couvre tous les scénarios futurs possibles de charge du système, de différences de moteur de mise en page, et ainsi de suite. Ce n'est **pas déterministe** et **ça se casse**, donc ne faites pas ça !

Si vous n'êtes pas encore convaincu, voici une autre raison : vos tests s'exécuteront beaucoup plus rapidement. L'animation de notre exemple ne prend que 800 millisecondes, nous l'espérons. Pour traiter le « nous l'espérons » et faire fonctionner les tests dans toutes les conditions, vous verrez probablement quelque chose comme `driver.sleep(2000)` dans le monde réel.

C'est plus d'une seconde complète perdue **pour une seule étape** de vos tests automatisés. Sur de nombreuses étapes, cela s'additionne rapidement. Un test récemment refactorisé pour l'une de nos pages web qui prenait plusieurs minutes en raison de l'utilisation excessive de driver.sleep prend maintenant moins de quinze secondes.

La majeure partie du reste de cet article donne des exemples spécifiques sur la façon dont vous pouvez rendre vos tests entièrement déterministes, et éviter l'utilisation de `driver.sleep`.

### Une note sur les promesses

L'API JavaScript pour Selenium utilise largement les promesses, et elle fait également un bon travail pour cacher cela en utilisant un gestionnaire de promesses intégré. Cela change et [sera obsolète](https://github.com/SeleniumHQ/selenium/issues/2969).

À l'avenir, vous devrez soit apprendre à utiliser le chaînage de promesses vous-même, soit utiliser les nouvelles fonctions JavaScript asynchrones comme `await`.

Dans cet article, les exemples utilisent toujours le gestionnaire de promesses intégré traditionnel de Selenium et tirent parti du chaînage de promesses. Les exemples de code ici auront plus de sens si vous comprenez comment fonctionnent les promesses. Mais vous pouvez toujours tirer beaucoup de cet article si vous souhaitez sauter l'apprentissage des promesses pour le moment.

### Commençons

Continuant avec notre exemple d'un bouton sur lequel nous voulons cliquer sur un panneau qui s'anime, examinons plusieurs pièges spécifiques qui pourraient casser nos tests.

Que dire d'un élément qui est ajouté dynamiquement à la page et qui n'existe même pas encore après que la page a fini de charger ?

#### Attendre qu'un élément soit présent dans le DOM

Le code suivant ne fonctionnerait pas si un élément avec un identifiant CSS 'my-button' était ajouté au DOM après le chargement de la page :

```
// Code d'initialisation de Selenium omis pour plus de clarté
```

```
// Charger la page.driver.get('https:/foobar.baz');
```

```
// Trouver l'élément.const button = driver.findElement(By.id('my-button'));
```

```
button.click();
```

La méthode `driver.findElement` s'attend à ce que l'élément soit déjà présent dans le DOM. Elle générera une erreur si l'élément ne peut pas être trouvé immédiatement. Dans ce cas, immédiatement signifie « après le chargement complet de la page » en raison de l'instruction `driver.get` précédente.

Rappelez-vous que la version actuelle de JavaScript Selenium gère les promesses pour vous. Ainsi, chaque instruction se complétera entièrement avant de passer à l'instruction suivante.

**Note :** Le comportement ci-dessus n'est pas toujours indésirable. `driver.findElement` seul peut être utile si vous êtes sûr que l'élément devrait déjà être là.

D'abord, regardons la mauvaise façon de corriger cela. Ayant été informé qu'il pourrait falloir quelques secondes pour que l'élément soit ajouté au DOM :

```
driver.get('https:/foobar.baz');
```

```
// La page a été chargée, maintenant endormez-vous pendant quelques secondes.driver.sleep(3000);
```

```
// Priez que trois secondes suffisent et trouvez l'élément.const button = driver.findElement(By.id('my-button'));
```

```
button.click();
```

Pour toutes les raisons mentionnées précédemment, cela peut se casser, et probablement le fera. Nous devons apprendre à attendre qu'un élément soit localisé. Cela est assez facile, et vous verrez souvent cela dans des exemples sur le web. Dans l'exemple ci-dessous, nous utilisons la méthode [bien documentée](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/ie_exports_Driver.html#wait) `driver.wait` pour attendre jusqu'à vingt secondes que l'élément soit trouvé dans le DOM :

```
const button = driver.wait(  until.elementLocated(By.id('my-button')),   20000);
```

```
button.click();
```

Il y a des avantages immédiats à cela. Par exemple, si l'élément est ajouté au DOM en une seconde, la méthode driver.wait se complétera en une seconde. Elle n'attendra pas les vingt secondes complètes spécifiées.

En raison de ce comportement, nous pouvons mettre beaucoup de marge dans notre délai d'attente sans nous soucier du ralentissement de nos tests. Contrairement à `driver.sleep` qui attendra toujours tout le temps spécifié.

Cela fonctionne dans de nombreux cas. Mais un cas où cela ne fonctionne pas est d'essayer de cliquer sur un élément qui est présent dans le DOM, mais qui n'est pas encore visible.

Selenium est assez intelligent pour ne pas cliquer sur un élément qui n'est pas visible. C'est bien, car les utilisateurs ne peuvent pas cliquer sur des éléments invisibles, mais cela nous oblige à travailler plus dur pour créer des tests automatisés fiables.

#### Attendre qu'un élément soit visible

Nous allons nous appuyer sur l'exemple ci-dessus car il est logique d'attendre qu'un élément soit localisé avant qu'il ne devienne visible.

Vous trouverez également notre première utilisation du chaînage de promesses ci-dessous :

```
const button = driver.wait(  until.elementLocated(By.id('my-button')),   20000).then(element => {   return driver.wait(     until.elementIsVisible(element),     20000   );});
```

```
button.click();
```

Nous pourrions presque nous arrêter ici et vous seriez déjà beaucoup mieux lotis. Avec le code ci-dessus, vous éliminerez de nombreux cas de test qui se casseraient autrement parce qu'un élément n'est pas immédiatement présent dans le DOM. Ou parce qu'il n'est pas immédiatement visible en raison de choses comme l'animation. Ou même pour ces deux raisons.

Maintenant que vous comprenez la technique, il ne devrait plus y avoir de raison d'écrire du code Selenium qui n'est pas déterministe. Cela ne signifie pas que c'est toujours facile.

Lorsque les choses deviennent plus difficiles, les développeurs abandonnent souvent et reviennent à `driver.sleep`. J'espère qu'en donnant encore plus d'exemples, je peux vous encourager à rendre vos tests déterministes.

#### Écrire vos propres conditions

Grâce à la méthode `until`, l'API JavaScript Selenium dispose déjà d'une [poignée de méthodes de commodité](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/until.html) que vous pouvez utiliser avec `driver.wait`. Vous pouvez également attendre qu'un élément n'existe plus, pour un élément qui contient un texte spécifique, pour qu'une alerte soit présente, ou pour de nombreuses autres conditions.

Si vous ne trouvez pas ce dont vous avez besoin dans les méthodes de commodité fournies, vous devrez écrire vos propres conditions. Cela est en fait assez facile, mais il est difficile de trouver des exemples. Et il y a un piège — auquel nous arriverons.

[Selon la documentation](http://seleniumhq.github.io/selenium/docs/api/javascript/module/selenium-webdriver/lib/webdriver_exports_WebDriver.html#wait), vous pouvez fournir à `driver.wait` une fonction qui retourne `true` ou `false`.

Supposons que nous voulions attendre qu'un élément soit à pleine opacité :

```
// Obtenir l'élément.const element = driver.wait(  until.elementLocated(By.id('some-id')),  20000);
```

```
// driver.wait a juste besoin d'une fonction qui retourne vrai ou faux.driver.wait(() => {   return element.getCssValue('opacity')          .then(opacity => opacity === '1');});
```

Cela semble utile et réutilisable, alors mettons-le dans une fonction :

```
const waitForOpacity = function(element) {  return driver.wait(element => element.getCssValue('opacity')          .then(opacity => opacity === '1');  );};
```

Et ensuite nous pouvons utiliser notre fonction :

```
driver.wait(  until.elementLocated(By.id('some-id')),  20000).then(waitForOpacity);
```

Voici le piège. Que se passe-t-il si nous voulons cliquer sur l'élément après qu'il ait atteint une opacité totale ? Si nous essayons d'assigner la valeur retournée par ce qui précède, nous n'obtiendrions pas ce que nous voulons :

```
const element = driver.wait(  until.elementLocated(By.id('some-id')),  20000).then(waitForOpacity);
```

```
// Oups, element est vrai ou faux, pas un élément.element.click();
```

Nous ne pouvons pas non plus utiliser le chaînage de promesses, pour la même raison.

```
const element = driver.wait(  until.elementLocated(By.id('some-id')),  20000).then(waitForOpacity).then(element => {  // Non, element est un booléen ici aussi.  element.click();}); 
```

Cela est facile à corriger. Voici notre méthode améliorée :

```
const waitForOpacity = function(element) {  return driver.wait(element => element.getCssValue('opacity')          .then(opacity => {      if (opacity === '1') {        return element;      } else {        return false;    });  );};
```

Le modèle ci-dessus, qui **retourne l'élément lorsque la condition est vraie**, et retourne false sinon, est un modèle réutilisable que vous pouvez utiliser lorsque vous écrivez vos propres conditions.

Voici comment nous pouvons l'utiliser avec le chaînage de promesses :

```
driver.wait(  until.elementLocated(By.id('some-id')),  20000).then(waitForOpacity).then(element => element.click());
```

Ou même :

```
const element = driver.wait(  until.elementLocated(By.id('some-id')),  20000).then(waitForOpacity);
```

```
element.click();
```

En écrivant vos propres conditions simples, vous pouvez élargir vos options pour rendre vos tests déterministes. Mais cela n'est pas toujours suffisant.

### Allez négatif

C'est vrai, parfois vous devez être négatif au lieu de positif. Ce que je veux dire par là, c'est tester pour que quelque chose n'existe plus ou pour que quelque chose ne soit plus visible.

Supposons qu'un élément existe déjà dans le DOM, mais que vous ne devriez pas interagir avec lui tant que certaines données ne sont pas chargées via AJAX. L'élément pourrait être couvert par un panneau « chargement... ».

Si vous avez prêté une attention particulière aux conditions offertes par la méthode `until`, vous avez peut-être remarqué des méthodes comme `elementIsNotVisible` ou `elementIsDisabled` ou le moins évident `stalenessOfElement`.

Vous pourriez tester pour qu'un panneau « chargement... » ne soit plus visible :

```
// Déjà ajouté au DOM, donc cela retournera immédiatement.const desiredElement = driver.wait(  until.elementLocated(By.id('some-id')),  20000);
```

```
// Mais l'élément n'est vraiment prêt que lorsque le panneau de chargement// a disparu.driver.wait(  until.elementIsNotVisible(By.id('loading-panel')),  20000);
```

```
// Le panneau de chargement n'est plus visible, il est sûr d'interagir maintenant.desiredElement.click();
```

Je trouve que `stalenessOfElement` est particulièrement utile. Il attend qu'un élément soit supprimé du DOM, ce qui pourrait également se produire lors du rafraîchissement de la page.

Voici un exemple d'attente pour que le contenu d'un `iframe` se rafraîchisse avant de continuer :

```
let iframeElem = driver.wait(  until.elementLocated(By.className('result-iframe')),  20000  );
```

```
// Maintenant, nous faisons quelque chose qui provoque le rafraîchissement de l'iframe.someElement.click();
```

```
// Attendre que l'iframe précédent n'existe plus :driver.wait(  until.stalenessOf(iframeElem),  20000);
```

```
// Basculer vers le nouvel iframe. driver.wait(  until.ableToSwitchToFrame(By.className('result-iframe')),  20000);
```

```
// Tout code suivant sera relatif au nouvel iframe.
```

### Soyez toujours déterministe, et ne dormez pas

J'espère que ces exemples vous ont aidé à mieux comprendre comment rendre vos tests Selenium déterministes. Ne vous fiez pas à `driver.sleep` avec une supposition arbitraire.

Si vous avez des questions ou vos propres techniques pour rendre les tests Selenium déterministes, veuillez laisser un commentaire.