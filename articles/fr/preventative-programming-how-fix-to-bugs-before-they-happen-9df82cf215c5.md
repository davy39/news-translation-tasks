---
title: Programmation préventive — comment corriger les bugs avant qu'ils n'apparaissent
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-02-19T22:22:28.000Z'
originalURL: https://freecodecamp.org/news/preventative-programming-how-fix-to-bugs-before-they-happen-9df82cf215c5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*qoss_sK2XC5p-p90DfZxZw.jpeg
tags:
- name: coding
  slug: coding
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Programmation préventive — comment corriger les bugs avant qu'ils n'apparaissent
seo_desc: 'By Kurt

  Bugs are inevitable.

  It is quite normal to spend more time debugging than you spend writing actual code.
  If you are learning to program and you absolutely hate debugging your own code,
  stop now.

  Find a new hobby or trade that you enjoy. Other...'
---

Par Kurt

#### Les bugs sont inévitables.

Il est tout à fait normal de passer plus de temps à déboguer qu'à écrire du code. Si vous apprenez à programmer et que vous détestez absolument déboguer votre propre code, **arrêtez maintenant**.

Trouvez un nouveau passe-temps ou un métier qui vous plaît. Sinon, vous découvrirez bientôt la vraie définition de la folie : déboguer le code hérité d'un autre programmeur, en vous demandant ce qu'ils avaient en tête.

Alternativement, vous pourriez simplement changer votre état d'esprit et arrêter de détester les bugs.

#### Voici quelques-unes des raisons pour lesquelles j'aime déboguer...

1. **C'est un défi**. Pour moi, un bug est une énigme à résoudre. J'adore les énigmes, donc c'est comme si l'application me donnait une heure pour jouer à Sudoku.
2. **Cela fait de moi un meilleur programmeur**. Déboguer du code est sans aucun doute l'une des meilleures méthodes d'apprentissage.
3. **Parfois, cela me fait rire**. Pour être programmeur, il faut avoir un bon sens de l'humour. Il faut aussi pouvoir rire de sa propre stupidité ou de l'humour de la situation.
4. **C'est la meilleure idée que je puisse avoir des pensées de mes utilisateurs**. Au-delà de vos tests initiaux, _vous ne devriez jamais tester vos propres applications_ — ni un autre programmeur. Cela est dû au fait que vous ne casserez jamais votre application de la manière dont vos utilisateurs le feront. Le meilleur testeur que j'ai jamais eu était le fils de 5 ans de mon patron, qui testait toutes nos applications iPad. S'il ne pouvait pas utiliser l'application, nos utilisateurs ne le pourraient pas non plus. La question lors du débogage ne se limite pas à _"Comment l'utilisateur l'a-t-il fait ?"_ mais s'étend également à _"Pourquoi l'utilisateur l'a-t-il fait ?"_

J'ai trouvé ce graphique circulaire sur le [ProgrammerHumor subreddit](https://www.reddit.com/r/ProgrammerHumor/) qui résume parfaitement ma journée moyenne :

![Image](https://cdn-media-1.freecodecamp.org/images/1*FwxngU46SX61NLTTjcb2CQ.jpeg)

Notez que la majorité du temps est consacrée à la mise en place de garde-fous. C'est la définition de la programmation préventive.

Si votre graphique est le même, c'est génial. Peut-être pouvons-nous échanger des conseils. Mais si vous êtes comme la plupart d'entre nous et passez la majorité de votre temps à vous demander ce que votre utilisateur a bien pu faire pour rendre une variable fixe [_undefined_](https://developer.mozilla.org/en-US/docs/Glossary/Undefined) ou transformer une _string_ en _integer_, alors cet article pourrait vous être particulièrement utile.

#### Pourquoi Sherlock Holmes aurait été un excellent programmeur

Le premier livre de Sherlock Holmes a été écrit en 1887, bien avant l'invention des ordinateurs. Tous ces livres regorgent de leçons que vous pouvez appliquer à la programmation.

Si cela vous surprend, rappelez-vous que les données existent depuis aussi longtemps que le mot écrit, et que la raison pour laquelle les ordinateurs ont été inventés était de gérer les données.

Sherlock Holmes est surtout célèbre pour utiliser sa _"méthode de déduction"_ :

> Lorsque vous avez éliminé l'impossible, ce qui reste, aussi improbable soit-il, doit être la vérité. — Sherlock Holmes dans _Le Signe des Quatre_

Si je devais appliquer cette pensée à une fonction, ce serait quelque chose comme...

> Lorsque vous avez empêché tout ce qu'une fonction ne devrait pas faire, elle ne peut faire que ce qu'elle devrait.

Plongeons dans quelques habitudes simples qui peuvent vous aider à économiser d'innombrables heures de débogage en appliquant cette théorie.

### Comment corriger les bugs avant qu'ils n'apparaissent

Jetez un coup d'œil à la fonction ci-dessous qui recherche dans un tableau et retourne la valeur si elle est trouvée soit _telle quelle_ soit _comme résultat d'une fonction de rappel_ :

```
function arraySearch(value, array, callback) {  callback = callback || false;  for (var i = 0; i < array.length; i++) {    if (array[i] == value) {      if (callback) {        return callback(value);      } else {        return value;      }    }  }}
var result = arraySearch(4,[1,2,3,4],function(val){return val+val;});
```

À première vue, cela semble parfaitement correct.

Mais faisons un pas en arrière et utilisons une _approche préventive_ en nous concentrant plutôt sur _ce que la fonction ne devrait pas faire_.

#### **Il y a quatre points que nous voulons aborder dans cet exercice**

1. **Elle ne devrait pas se casser facilement**. Si possible, nous voulons l'empêcher de s'arrêter sur une _erreur_. Au lieu de cela, elle devrait _retourner_.

2. **Elle ne devrait jamais retourner [undefined](https://developer.mozilla.org/en-US/docs/Glossary/Undefined).** Nous voulons qu'elle retourne _false_ à la place.

3. **Elle ne doit jamais faire de correspondance implicite ou "lâche".**

4. **Lorsque nous devons [lancer](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw) une erreur, elle ne doit pas être une erreur générique**. Nous voulons quelque chose de lisible pour nous-mêmes et pour le pauvre programmeur qui devra travailler sur ce code après nous.

#### Pour commencer

Le point 1 semble demander beaucoup, mais en essence, nous voulons simplement qu'elle échoue gracieusement et _retourne une valeur prévisible_ comme **_false_** au lieu d'arrêter le bus.

Tout d'abord, elle doit absolument avoir une _valeur d'entrée_ et un _tableau_ pour fonctionner. Modifions donc la fonction en gardant cela à l'esprit.

```
function arraySearch(value, array, callback) {  if (value === undefined || array === undefined) {    return false;  }  callback = callback || false;  for (var i = 0; i < array.length; i++) {    if (array[i] == value) {      if (callback) {        return callback(value);      }      else {        return value;      }    }  }}
```

Super, c'est réglé. En vérifiant si les arguments sont [_undefined_](https://developer.mozilla.org/en-US/docs/Glossary/Undefined), nous nous assurons que des valeurs leur ont été passées.

Notre callback a déjà une valeur _par défaut_, donc c'est pris en charge. Mais que se passe-t-il si notre _tableau n'est pas un tableau_ ? Ou dans le même ordre d'idées, que se passe-t-il si notre _callback n'est pas une fonction_ ?

Occupons-nous de cela ensuite...

```
function arraySearch(value, array, callback) {  if (value === undefined || array === undefined || (array instanceof Array) === false) {    return false;  }  callback = callback || false;  if (callback !== false && typeof callback !== 'function') {    throw 'Callback to arraySearch is not a function';    return false;  }  for (var i = 0; i < array.length; i++) {    if (array[i] == value) {      if (callback) {        return callback(value);      }      else {        return value;      }    }  }}
```

Génial. Maintenant, en vérifiant le [**_typeof_**](https://developer.mozilla.org/en-US/docs/Glossary/Null) du _callback_, nous sommes sûrs que le callback est une fonction valide et en vérifiant que le tableau est une [**_instanceof_**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/instanceof) de l'objet _Array_, nous sommes également sûrs que le tableau est un _Array_.

Passons donc au point 2 — "Elle ne devrait jamais retourner undefined".

Pour commencer, notre _fonction_ n'a pas de _valeur de retour par défaut_ en cas de non-correspondance. Tout aussi important, nous n'avons aucun moyen de savoir ce que la fonction de rappel retournera.

Nous pouvons corriger cela en faisant en sorte que la fonction _retourne une variable_ afin que nous n'ayons besoin de vérifier qu'une seule fois si elle est [_undefined_](https://developer.mozilla.org/en-US/docs/Glossary/Undefined) ou [_null_](https://developer.mozilla.org/en-US/docs/Glossary/Null).

```
function arraySearch(value, array, callback) {  if (value === undefined || array === undefined || (array instanceof Array) === false) {    return false;  }  callback = callback || false;  var result = null;  if (callback !== false && typeof callback !== 'function') {    throw 'Callback to arraySearch is not a function';    return false;  }  for (var i = 0; i < array.length; i++) {    if (array[i] == value) {      if (callback) {        result = callback(value);      }      else {        result = value;      }    }  }  return result || false;}
```

Résolu. En définissant la valeur de _result_ soit à la _correspondance_ soit au résultat de la _fonction de rappel_, nous pouvons retourner soit le _result_ soit false, si le _result_ est [_undefined_](https://developer.mozilla.org/en-US/docs/Glossary/Undefined) ou [_null_](https://developer.mozilla.org/en-US/docs/Glossary/Null).

Point 3. Une correspondance _implicite_ ou _lâche_ peut être décrite comme étant _relativement égale_, c'est-à-dire false == 0 ou '4' == 4, etc.

Nous voulons éviter cela. Et si nous cherchons _false_ dans un tableau contenant Zero ?

Nous pouvons corriger cela en changeant la ligne ci-dessous :

```
  if (array[i] == value) {//doit changer pour  if (array[i] === value) {
```

["**===**"](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Comparison_Operators) signifie **exactement égal à**. Faites toujours une correspondance explicite lors de la vérification des valeurs. Cette habitude vous fera économiser d'innombrables heures de temps à long terme car _vous n'essaierez pas de déboguer une instruction qui est évaluée comme vraie_.

Passons au dernier point.

Lors du lancement d'une erreur, nous voulons qu'elle soit conviviale. Cette fonctionnalité est déjà démontrée lors du passage d'une _fonction de rappel invalide_, mais _que se passe-t-il si une fonction de rappel valide lance une erreur_ ?

Les [fonctions anonymes](https://developer.mozilla.org/en-US/docs/Glossary/Function) peuvent être pénibles à déboguer, alors essayons de rendre le débogage un peu moins douloureux :

```
function arraySearch(value, array, callback) {  if (value === undefined || array === undefined || (array instanceof Array) === false) {    return false;  }  callback = callback || false;  var result = null;  if (callback !== false && typeof callback !== 'function') {    throw 'Callback to arraySearch is not a function';    return false;  }  for (var i = 0; i < array.length; i++) {    if (array[i] === value) {      if (callback) {        try{          result = callback(value);        }catch(e){          throw 'Callback function in arraySearch threw the error : '+e.message;        }      }      else {        result = value;      }    }  }  return result || false;}
```

Voilà.

Pour résoudre le problème, nous utilisons une simple instruction [**_try / catch_**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/try...catch) puis [relançons](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw) l'erreur avec un _message personnalisé_. Maintenant, si une fonction de rappel échoue, nous saurons immédiatement que c'est la _fonction de rappel_ qui a échoué et non notre fonction _arraySearch_.

#### Résumé

Dans l'ensemble, nous avons maintenant une fonction qui devrait nous donner un minimum de tracas à l'avenir. Et si elle a un problème, il devrait être rapide et facile à corriger.

Les bases de mes conseils sur la programmation préventive peuvent être résumés en 6 points...

1. **Vérifiez que vos valeurs d'entrée existent** et définissez des valeurs par défaut si nécessaire.
2. Assurez-vous toujours que **votre entrée est du même type que ce que vous recherchez**. Ne supposez jamais qu'un _Array_ sera un _Array_ ou qu'un _Integer_ sera un _Integer_.
3. **Faites toujours une correspondance explicite** lors de la comparaison des valeurs (**===**).
4. **Écrivez des fonctions qui retournent des valeurs prévisibles**, c'est-à-dire retournez _false_ en cas d'échec ou _false_ ou retournez le résultat attendu lorsque _true_.
5. **Essayez d'écrire des fonctions pures**. Une fonction pure est une fonction qui retourne toujours une valeur attendue et ne modifie pas les variables originales qui lui sont passées.
6. [**Lancez**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/throw) **des erreurs personnalisées si nécessaire, surtout lors de l'exécution de callbacks et de fonctions anonymes**. Vous ne vous souviendrez pas exactement de ce que fait votre code dans 8 mois, alors faites-vous une faveur et lancez un message d'erreur clair tant que vous savez encore ce que fait votre code.

### Je vous laisse avec quelques grandes citations de Sherlock Holmes

#### Morale : Ne faites pas de suppositions avant de collecter des données

> C'est une erreur capitale de théoriser avant d'avoir toutes les preuves. Cela biaise le jugement. — Une Étude en Rouge

> C'est une erreur capitale de théoriser avant d'avoir des données. Insensiblement, on commence à tordre les faits pour les adapter aux théories, au lieu d'adapter les théories aux faits. -Un Scandale en Bohême

> Pourtant, c'est une erreur de discuter devant ses données. On peut se retrouver à les tordre insensiblement pour les adapter à ses théories. -L'Aventure du Pavillon Wisteria

> Laissez-moi passer en revue les principales étapes. Nous avons abordé l'affaire, vous vous souvenez, avec un esprit absolument vide, ce qui est toujours un avantage. Nous n'avions formé aucune théorie. Nous étions simplement là pour observer et tirer des inferences de nos observations. -L'Aventure de la Boîte en Carton

> "Données ! Données ! Données !" s'exclama-t-il avec impatience. "Je ne peux pas faire de briques sans argile. -L'Aventure des Hêtres de Cuivre

#### Morale : Ne laissez pas vos émotions prendre le pas sur la logique

> La détection est, ou devrait être, une science exacte, et devrait être traitée de la même manière froide et sans émotion. -Le Signe des Quatre

> Les qualités émotionnelles sont antagonistes à un raisonnement clair. -Le Signe des Quatre

#### Morale : Concentrez-vous sur les fonctionnalités principales et les cas d'utilisation

> Il est de la plus haute importance dans l'art de la détection de pouvoir reconnaître, parmi un certain nombre de faits, lesquels sont incidentels et lesquels sont vitaux. Sinon, votre énergie et votre attention doivent être dissipées au lieu d'être concentrées. -Le Mystère de Reigate

#### Et quelques autres dont vous pouvez tirer votre propre leçon

> Rien ne clarifie une affaire autant que de l'exposer à une autre personne. -Silver Blaze

> Je vous ai déjà expliqué que ce qui est hors du commun est généralement un guide plutôt qu'un obstacle. -Une Étude en Rouge

> 'Plus un incident est étrange et grotesque, plus il mérite d'être examiné avec soin, et le point même qui semble compliquer une affaire est, lorsqu'il est dûment considéré et traité scientifiquement, celui qui est le plus susceptible de l'élucider. -Le Chien des Baskerville

> Toute vérité est meilleure qu'un doute indéfini. -La Figure Jaune

> Je ne devine jamais. C'est une habitude choquante — destructive pour la faculté logique -Le Signe des Quatre

C'est tout ce que j'ai pour cet article. Si vous avez aimé le lire et que vous souhaitez lire un autre article technique, consultez :

[**Comment écrire une bibliothèque similaire à jQuery en 71 lignes de code — Apprenez à connaître le DOM**](https://medium.com/p/e9fb99dbc8d2)  
[_Les frameworks JavaScript sont à la mode. Il est probable que tout flux d'actualités lié à JavaScript que vous ouvrez sera rempli..._medium.com](https://medium.com/p/e9fb99dbc8d2)

Alternativement, si le code vous a fait mal à la tête et vous a fatigué, voici quelques articles non techniques que j'ai écrits...

[**5 Choses à Retenir Lorsque Vous Apprenez à Programmer**](https://medium.com/p/1ed8e734b04f)  
[_Apprendre à programmer est un défi. En plus de choisir un langage ou de configurer un environnement de développement que vous..._medium.com](https://medium.com/p/1ed8e734b04f)[**Transformer le code en argent — Comment gagner de l'argent en tant que Développeur Web et vivre pour en parler.**](https://medium.com/p/f5eedc557b3e)  
[_Vous venez d'apprendre à coder. Vous êtes enthousiaste et quiconque ne sait pas coder pense que vous êtes un génie, la nouvelle se répand et tout..._medium.com](https://medium.com/p/f5eedc557b3e)[**Comment Je Suis Devenu Programmeur. Et Quand J'ai Commencé à M'Appeler Un**](https://medium.com/p/54a0533c4335)  
[_J'ai voulu commencer à bloguer sur la programmation depuis des mois maintenant et comme tant d'autres avant moi, je me suis lancé plein de..._medium.com](https://medium.com/p/54a0533c4335)[**Faire pleuvoir du code — Style Matrix**](https://medium.com/p/ec6e1386084e)  
[_Une introduction aux animations HTML 5 canvas_medium.com](https://medium.com/p/ec6e1386084e)