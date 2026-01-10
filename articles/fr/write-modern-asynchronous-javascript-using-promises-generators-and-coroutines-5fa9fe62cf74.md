---
title: Écrire du JavaScript asynchrone moderne en utilisant les Promesses, les Générateurs
  et les Coroutines
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-11T23:07:07.000Z'
originalURL: https://freecodecamp.org/news/write-modern-asynchronous-javascript-using-promises-generators-and-coroutines-5fa9fe62cf74
coverImage: https://cdn-media-1.freecodecamp.org/images/1*SYxxUFJirsj3BH1-LCsFZw.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: Écrire du JavaScript asynchrone moderne en utilisant les Promesses, les
  Générateurs et les Coroutines
seo_desc: 'By William Gottschalk

  Over the years, “Callback Hell” is often cited as one of the most hated design patterns
  in Javascript for managing concurrency. Just in case you’ve forgotten what that
  looks like, here is an example of a varying and processing a...'
---

Par William Gottschalk

Au fil des ans, le "Callback Hell" est souvent cité comme l'un des motifs de conception les plus détestés en JavaScript pour gérer la concurrence. Au cas où vous auriez oublié à quoi cela ressemble, voici un exemple de variation et de traitement d'une transaction dans Express :

#### Les Promesses devaient nous sauver...

On m'a dit que les promesses permettraient aux développeurs JavaScript d'écrire du code asynchrone comme s'il était synchrone en enveloppant nos fonctions asynchrones dans un objet spécial. Pour accéder à la valeur de la Promesse, nous appelons soit **_.then_** soit **_.catch_** sur l'objet Promesse. Mais que se passe-t-il lorsque nous essayons de refactoriser l'exemple ci-dessus en utilisant les Promesses ?

Puisque chaque fonction à l'intérieur du callback est scopée, nous ne pouvons pas accéder à l'objet utilisateur à l'intérieur du second callback **_.then_**.

Après un peu de recherche, je n'ai pas trouvé de solution élégante, mais j'en ai trouvé une frustrante :

> Il suffit d'indenter vos promesses pour qu'elles aient un scoping approprié.

Indenter mes promesses !? Donc c'est le retour à la Pyramide de la Mort maintenant ?

Je soutiendrais que la version avec les callbacks imbriqués semble plus propre et plus facile à comprendre que la version avec les promesses imbriquées.

#### Async Await va nous sauver !

Les mots-clés **_async_** et **_await_** nous permettront d'écrire notre code JavaScript comme s'il était synchrone. Voici du code écrit avec ces mots-clés arrivant dans ES7 :

Malheureusement, la majorité des fonctionnalités de ES7, y compris **_async_**/**_await_**, n'ont pas été implémentées nativement et nécessitent donc l'utilisation d'un transpileur. Cependant, vous pouvez écrire du code qui ressemble exactement au code ci-dessus en utilisant les fonctionnalités de ES6 qui ont été implémentées dans la plupart des navigateurs modernes ainsi que dans Node version 4+.

#### Le Duo Dynamique : Générateurs et Coroutines

Les générateurs sont un excellent outil de métaprogrammation. Ils peuvent être utilisés pour des choses comme l'évaluation paresseuse, l'itération sur des ensembles de données intensifs en mémoire et le traitement de données à la demande à partir de plusieurs sources de données en utilisant une bibliothèque comme RxJs.

Cependant, nous ne voudrions pas utiliser les générateurs seuls dans le code de production car ils nous obligent à raisonner sur un processus dans le temps. Et chaque fois que nous appelons next, nous revenons à notre générateur comme une instruction GOTO.

Les coroutines comprennent cela et remédient à cette situation en enveloppant un générateur et en abstraisant toute la complexité.

#### La version ES6 utilisant Coroutine

Les coroutines nous permettent de **_yield_** nos fonctions asynchrones une ligne à la fois, rendant notre code synchrone.

Il est important de noter que j'utilise la bibliothèque Co. La coroutine de Co exécutera le générateur immédiatement, alors que la coroutine de Bluebird retournera une fonction que vous devez invoquer pour exécuter le générateur.

Établissons quelques règles de base pour utiliser les coroutines :

1. Toute fonction à droite d'un **_yield_** doit retourner une Promesse.
2. Si vous voulez exécuter votre code maintenant, utilisez **_co_**.
3. Si vous voulez exécuter votre code plus tard, utilisez **_co.wrap_**.
4. Assurez-vous de chaîner un **_.catch_** à la fin de votre coroutine pour gérer les erreurs. Sinon, vous devriez envelopper votre code dans un bloc try/catch.
5. **_Promise.coroutine_** de Bluebird est l'équivalent de **_co.wrap_** de Co et non de la fonction **_co_** seule.

#### Que faire si je veux exécuter plusieurs processus simultanément ?

Vous pouvez utiliser des objets ou des tableaux avec le mot-clé yield et ensuite déstructurer le résultat.

#### Bibliothèques que vous pouvez utiliser aujourd'hui :

[**Promise.coroutine | bluebird**](http://bluebirdjs.com/docs/api/promise.coroutine.html)
[_Bluebird est une bibliothèque de promesses JavaScript entièrement fonctionnelle avec des performances inégalées._bluebirdjs.com](http://bluebirdjs.com/docs/api/promise.coroutine.html)
[**co**](https://www.npmjs.com/package/co)
[_generator async control flow goodness_www.npmjs.com](https://www.npmjs.com/package/co)
[**Babel · _Le compilateur pour écrire la prochaine génération de JavaScript_**](https://babeljs.io/)
[Le compilateur pour écrire la prochaine génération de JavaScriptbabeljs.io](https://babeljs.io/)
[**asyncawait**](https://www.npmjs.com/package/asyncawait)
[_async/await pour node.js_www.npmjs.com](https://www.npmjs.com/package/asyncawait)