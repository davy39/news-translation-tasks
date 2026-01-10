---
title: ⚡ Comment ne plus jamais répéter les mêmes erreurs RxJs ⚡
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T13:14:28.000Z'
originalURL: https://freecodecamp.org/news/blitz-tips-rxjs-pipe-is-not-a-subscribe-125c89437a2c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8WNtSRqKD9vfik5zLqDRzw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: RxJS
  slug: rxjs
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: ⚡ Comment ne plus jamais répéter les mêmes erreurs RxJs ⚡
seo_desc: 'By Tomas Trajan

  Remember: .pipe() is not .subscribe()!


  _Look! A lightning tip! (Original ? by M[ax Bender)](https://unsplash.com/photos/iF5odYWB_nQ?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="blank" tit...'
---

Par Tomas Trajan

#### Rappel : .pipe() n'est pas .subscribe() !

![Image](https://cdn-media-1.freecodecamp.org/images/fNpm-kNhaYwgz2TVveT9Zs1BYKjC9I5G6wR0)
_Regardez ! Un conseil éclair ! (Original ? par M[ax Bender)](https://unsplash.com/photos/iF5odYWB_nQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Cet article s'adresse aux débutants cherchant à améliorer leurs connaissances en RxJs, mais peut également servir de rappel rapide ou de référence à montrer aux débutants pour les développeurs plus expérimentés !

Aujourd'hui, nous allons être concis et aller droit au but !

Actuellement, je travaille dans une organisation assez grande avec plusieurs équipes et projets (plus de 40 SPAs) qui sont en cours de migration vers Angular et donc aussi vers RxJs.

Cela représente une excellente opportunité de se familiariser avec les parties déroutantes de RxJs, qui peuvent être faciles à oublier une fois que l'on maîtrise les APIs et que l'on se concentre sur la mise en œuvre des fonctionnalités.

### La fonction "subscribe()"

Les observables RxJs représentent une "recette" de ce que nous voulons qu'il se passe. C'est déclaratif, ce qui signifie que toutes les opérations et transformations sont spécifiées dans leur intégralité dès le départ.

Un exemple de flux observable pourrait ressembler à ceci...

![Image](https://cdn-media-1.freecodecamp.org/images/RilFbbGg9L-sldm9tExd5KJeYZDpaI-tkDB6)
_Exemple de déclaration de flux observable RxJs_

Cet observable RxJs ne fera littéralement rien par lui-même. Pour l'exécuter, nous devons nous y abonner quelque part dans notre codebase !

![Image](https://cdn-media-1.freecodecamp.org/images/slCuDufj5NNymYAfjvD5ZjCk1ImU5j56Ydww)
_Cet abonnement enregistrera nos salutations toutes les minutes impaires_

Dans l'exemple ci-dessus, nous avons fourni un gestionnaire uniquement pour les valeurs émises par l'observable. La fonction subscribe elle-même accepte jusqu'à trois arguments différents pour gérer la valeur **next**, l'événement **error** ou **complete**.

En plus de cela, nous pourrions également passer un objet avec les propriétés listées ci-dessus. Un tel objet est une implémentation de l'interface `Observer`. L'avantage de l'observer est que nous n'avons pas à fournir d'implémentation ou au moins un espace réservé `null` pour les gestionnaires qui ne nous intéressent pas.

Considérons l'exemple suivant...

![Image](https://cdn-media-1.freecodecamp.org/images/o0QFSmaoJWlc3EB1EwioXq8y4feIBLr1JcS6)

Dans le code ci-dessus, nous passons un littéral d'objet qui ne contient que le gestionnaire complete, les valeurs normales seront ignorées et les erreurs remontent la pile.

![Image](https://cdn-media-1.freecodecamp.org/images/tdaiNzIWmElXpTcw-dBTX5XNtSEspNyyAu2S)

Et dans cet exemple, nous passons le gestionnaire de la prochaine erreur et le complétons en tant qu'arguments directs de la fonction subscribe. Tous les gestionnaires non implémentés doivent être passés comme null ou undefined jusqu'à ce que nous arrivions à l'argument qui nous intéresse.

Comme nous pouvons le voir, le style d'argument en ligne de l'implémentation d'un appel de fonction `.subscribe()` est positionnel.

> Selon mon expérience, le style d'arguments en ligne est celui qui est le plus courant dans divers projets et organisations.

Malheureusement, nous pouvons souvent rencontrer des implémentations comme la suivante...

![Image](https://cdn-media-1.freecodecamp.org/images/HzGX7f-wmb1vGY1r8A2aaKkUYhf5H74LbC9N)
_Exemple de gestionnaires redondants souvent rencontrés "dans la nature"_

L'exemple ci-dessus contient des gestionnaires redondants pour les gestionnaires `next` et `error` qui **ne font absolument rien** et auraient pu être remplacés par `null`.

> Encore mieux serait de passer l'objet observer avec l'implémentation du gestionnaire `complete`, en omettant complètement les autres gestionnaires !

### Le "pipe()" et les opérateurs

Comme les débutants sont habitués à fournir trois arguments à subscribe, ils essaient souvent de mettre en œuvre un modèle similaire lorsqu'ils utilisent des opérateurs similaires dans la chaîne de pipe.

Les opérateurs RxJs, qui sont souvent confondus avec les gestionnaires `.subscribe()`, sont `catchError` et `finalize`. Ils servent tous deux un but similaire également — la seule différence étant qu'ils sont utilisés dans le contexte du pipe au lieu de l'abonnement.

Dans le cas où nous souhaiterions réagir à l'événement complete de chaque abonnement du flux observable RxJs, nous pourrions implémenter l'opérateur `finalize` en tant que partie du flux observable lui-même.

> De cette façon, nous n'avons pas à dépendre des développeurs pour implémenter les gestionnaires complete dans chaque appel .subscribe(). Rappelez-vous, le flux observable peut être abonné plus d'une fois !

![Image](https://cdn-media-1.freecodecamp.org/images/KyNcUrKEuK-5ho4qMmrJH9rRsgUIYBFDx8kr)
_Utilisez l'opérateur finalize pour réagir à l'événement complete du flux indépendamment de l'abonnement. (Similaire à tap)_

Cela nous amène au dernier et probablement au modèle le plus problématique que nous pouvons rencontrer lors de l'exploration de diverses bases de code : les opérateurs redondants ajoutés lors de la tentative de suivre le modèle .subscribe() dans le contexte .pipe().

![Image](https://cdn-media-1.freecodecamp.org/images/VoSsjJj6f-9Tmlkpqn53d5LikSlKgaQVPMzg)

De plus, nous pourrions rencontrer son cousin encore plus verbeux...

![Image](https://cdn-media-1.freecodecamp.org/images/XZb1uYVdeTzKVx1YSpK5NY88CB6YrY0BMh85)
_Les choses peuvent devenir verbeuses...

Remarquez que nous sommes passés de la ligne unique originale à neuf lignes complètes de code que nous devons lire et comprendre lorsque nous voulons corriger un bug ou ajouter une nouvelle fonctionnalité.

> Les choses peuvent devenir encore plus complexes lorsqu'elles sont combinées avec des types Typescript génériques plus complexes, ce qui peut rendre le bloc de code entier encore plus mystérieux (et donc gaspiller plus de notre temps).

### Récapitulation

1. La méthode `.subscribe()` accepte à la fois l'objet observer et les gestionnaires en ligne.
2. L'objet observer représente le moyen le plus polyvalent et concis de s'abonner à un flux observable.
3. Dans le cas où nous souhaitons utiliser les arguments d'abonnement en ligne (`next`, `error`, `complete`), nous pouvons fournir `null` à la place d'un gestionnaire dont nous n'avons pas besoin.
4. Nous devons nous assurer de ne pas essayer de répéter le modèle `.subscribe()` lorsque nous traitons avec `.pipe()` et les opérateurs.
5. Efforcez-vous toujours de garder le code aussi simple que possible et de supprimer les redondances inutiles !

#### C'est tout ! ✨

> J'espère que vous avez apprécié cet article et que vous avez maintenant une meilleure compréhension de la manière de vous abonner aux observables RxJs avec une implémentation propre et concise !

Veuillez soutenir ce guide avec vos ??? en utilisant le bouton d'applaudissements et aidez-le à atteindre un public plus large ? De plus, n'hésitez pas à me contacter si vous avez des questions en utilisant les réponses de l'article ou les DM Twitter @tom[astrajan.](https://twitter.com/tomastrajan)

> [Et n'oubliez jamais, l'avenir est radieux](https://twitter.com/tomastrajan)

![Image](https://cdn-media-1.freecodecamp.org/images/HDE38gYVRZf0lweAmygW6hc5yW3sHdp3agm9)
_[avier Coiffic)](https://twitter.com/tomastrajan" rel="noopener" target="_blank" title="">Évidemment l'avenir radieux ! (? par X</a><a href="https://unsplash.com/photos/WV4B_aVj0aQ?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

> Vous commencez un projet Angular ? Consultez [Angular NgRx Material Starter](https://github.com/tomastrajan/angular-ngrx-material-starter) !

![Image](https://cdn-media-1.freecodecamp.org/images/mWKbDXFT-UMK-sCaFd9yMEVZstrY1roIHN7v)
_Angular NgRx Material Starter avec des meilleures pratiques intégrées, des thèmes et bien plus encore !_

Si vous êtes arrivé jusqu'ici, n'hésitez pas à consulter certains de mes autres articles sur Angular et le développement de logiciels frontend en général...

[**?‍?️ Les 7 conseils pro pour être productif avec Angular CLI & Schematics ?**](https://hackernoon.com/%EF%B8%8F-the-7-pro-tips-to-get-productive-with-angular-cli-schematics-b59783704c54)  
[**An**g_ular Schematics est un outil de workflow pour le web moderne — article d'introduction officielhac_kernoon.com](https://hackernoon.com/%EF%B8%8F-the-7-pro-tips-to-get-productive-with-angular-cli-schematics-b59783704c54)  [**La meilleure façon de se désabonner des observables RxJS dans les applications Angular !**](https://blog.angularindepth.com/the-best-way-to-unsubscribe-rxjs-observable-in-the-angular-applications-d8f9aa42f6a0)  
[_Il existe de nombreuses façons différentes de gérer les abonnements RxJS dans les applications Angular et nous allons explorer leurs..._blog.angularindepth.com](https://blog.angularindepth.com/the-best-way-to-unsubscribe-rxjs-observable-in-the-angular-applications-d8f9aa42f6a0)[**Guide complet de l'injection de dépendances Angular 6+ — providedIn vs providers:[ ] ?**](https://medium.com/@tomastrajan/total-guide-to-angular-6-dependency-injection-providedin-vs-providers-85b7a347b59f)  
[L_et’s learn when and how to use new better Angular 6+ dependency injection mechanism with new providedIn syntax to make...m_edium.com](https://medium.com/@tomastrajan/total-guide-to-angular-6-dependency-injection-providedin-vs-providers-85b7a347b59f) [**La réponse ultime à la question très courante sur Angular : subscribe() vs | async Pipe**](https://blog.angularindepth.com/angular-question-rxjs-subscribe-vs-async-pipe-in-component-templates-c956c8c0c794)  
[_La plupart des bibliothèques populaires de gestion d'état Angular comme NgRx exposent l'état de l'application sous forme de flux de..._blog.angularindepth.com](https://blog.angularindepth.com/angular-question-rxjs-subscribe-vs-async-pipe-in-component-templates-c956c8c0c794)