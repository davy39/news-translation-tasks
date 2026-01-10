---
title: Programmation Fonctionnelle En JavaScript — Avec Des Exemples Pratiques (Partie
  2)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-16T18:13:04.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U1TQD4tsM3JLZ-MfBH-vJA.jpeg
tags:
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Programmation Fonctionnelle En JavaScript — Avec Des Exemples Pratiques
  (Partie 2)
seo_desc: 'By rajaraodv

  In Part 1, we talked through: Functional Programming basics, Currying, Pure Functions,
  “Fantasy-land” specs, “Functors”, “Monads”, “Maybe Monads” and “Either Monads” via
  couple of examples.

  In this part, we’ll cover: Applicative, curryN ...'
---

Par rajaraodv

[**Dans la Partie 1**](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.8dao66cag), nous avons parlé de : les bases de la programmation fonctionnelle, le Currying, les Fonctions Pures, les spécifications "Fantasy-land", les "Foncteurs", les "Monades", les "Monades Maybe" et les "Monades Either" via quelques exemples.

**Dans cette partie, nous couvrirons : Applicative, la fonction curryN et "Validation Applicative".**

> Merci aux gurus de la FP [Brian Lonsdorf](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined), [keithalexander](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined) et autres pour la révision _??_

### _Exemple 3 — Assigner des Valeurs à des Objets Potentiellement Nuls_

_**Concepts FP Utilisés : "Applicative"**_

_**Cas d'Utilisation :** Disons que nous voulons donner une réduction à l'utilisateur si l'utilisateur est connecté et si nous faisons une promotion (c'est-à-dire que la réduction existe)._

![Image](https://cdn-media-1.freecodecamp.org/images/1*qqkZuYVXrxIsyuJ5xTa_Yw.png)

_Disons que nous utilisons la méthode **applyDiscount** ci-dessous. Comme vous pouvez l'imaginer, applyDiscount pourrait lancer des erreurs null si soit l'utilisateur (le côté gauche) soit la réduction (le côté droit) est null._

_`//Ajoute une réduction à l'objet utilisateur si l'utilisateur et la réduction existent.`_  
_`//Lance des erreurs null si l'utilisateur ou la réduction est nullconst applyDiscount = (user, discount) => {    let userClone = clone(user);// utilise une bibliothèque pour faire une copie`_    
   _`    **userClone.discount = discount.code;**   return userClone;`_  
_`}`_

_Voyons comment nous pouvons résoudre cela en utilisant "applicative"._

_**Applicative :**_

_Toute Classe qui a une méthode "ap" et implémente la spécification Applicative est appelée un Applicative. Les Applicatives peuvent être utilisées dans des fonctions qui traitent des valeurs null des deux côtés de l'équation (utilisateur et réduction)._

_Il s'avère que les Monades "Maybe" (et toutes les Monades) implémentent également la spécification "ap" et sont donc également des "Applicatives" et pas seulement des Monades. Nous pouvons donc utiliser les Monades "Maybe" pour gérer les valeurs null au niveau de la fonction._

_Voyons comment nous pouvons faire fonctionner applyDiscount en utilisant Maybe utilisé comme un "applicative"._

#### _**Étape 1 :** envelopper nos valeurs potentiellement null dans des Monades Maybe_

_`const maybeUser = Maybe(user);`_  
_`const maybeDiscount = Maybe(discount);`_

#### _**Étape 2 :** Réécrire la fonction et la curry pour pouvoir passer un paramètre à la fois._

_`//Réécrire la fonction et la curry pour pouvoir`_   
_`//passer un paramètre à la fois`_  
_`var applyDiscount = curry(function(user, discount) {`_       
       _`user.discount = discount.code;`_       
       _`return user;`_   
_`});`_

#### _**Étape 3 :** passons le premier argument (maybeUser) à applyDiscount via "map"._

_`//passer le premier argument à applyDiscount via "map"`_  
_`**const maybeApplyDiscountFunc = maybeUser.map(applyDiscount);**//Note, puisque applyDiscount est "curried", et "map" ne passera qu'un seul paramètre, le résultat retourné (**maybeApplyDiscountFunc**) sera une fonction "applyDiscount" enveloppée dans un Maybe qui a maintenant maybeUser (1er param) dans sa fermeture.**En d'autres termes, nous avons maintenant une fonction enveloppée dans une Monade !**`_

#### _**Étape 4 : Traiter** maybeApplyDiscountFunc_

_À ce stade, maybeApplyDiscountFunc peut être :_  
_1. Si l'utilisateur existe réellement, alors maybeApplyDiscountFunc est une fonction enveloppée dans un Maybe._  
_2. Si l'utilisateur n'existe pas, alors maybeApplyDiscountFunc sera "Nothing" (sous-classe de Maybe)_

_Si l'utilisateur n'existe pas, alors "Nothing" est retourné et toute interaction supplémentaire avec celui-ci est ignorée complètement. Donc si nous passons un 2ème argument, rien ne se passe. Et aucune erreur Null n'est lancée._

_Mais dans le cas où l'utilisateur existe réellement, nous pouvons essayer de passer le 2ème argument à maybeApplyDiscountFunc via "map" pour exécuter la fonction comme ci-dessous :_

_`maybeDiscount.map(maybeApplyDiscountFunc)! // PROBLÈME !`_

_**Oh oh ! "map" ne sait pas comment exécuter la fonction (**maybeApplyDiscountFunc) **quand la fonction elle-même est à l'intérieur d'un Maybe !**_

_C'est pourquoi nous avons besoin d'une interface différente pour traiter ce scénario. Il s'avère que c'est "ap" !_

_**Étape 5 :** Récapitulons la fonction "ap". La méthode "ap" prend une autre Monade Maybe et passe/applique la fonction qu'elle stocke actuellement à ce Maybe._

_Nous pouvons simplement appliquer ("ap") maybeApplyDiscountFunc à maybeDiscount au lieu d'utiliser "map" comme ci-dessous et cela fonctionnera à merveille !_

_`maybeApplyDiscountFunc.**ap**(maybeDiscount)//En interne, cela fait ce qui suit parce que applyDiscount est stockée dans this.val de l'enveloppe maybeApplyDiscountFunc :`_  
_`maybeDiscount.map(applyDiscount)//Maintenant, si maybeDiscount a effectivement la réduction, alors la fonction est exécutée. Si maybeDiscount est Null, alors rien ne se passe.`_

> _FYI : Apparemment, il y a un changement dans la spécification FL, l'ancienne version a (par exemple) : `Just(f).ap(Just(x))` (où `f` est une fonction et `x` est une valeur) mais la nouvelle version vous ferait écrire `Just(x).ap(Just(f))`Mais les implémentations n'ont pas encore beaucoup changé. Merci [keithalexander](https://www.freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e/undefined)_

_Pour résumer, si vous avez une fonction qui traite plusieurs paramètres qui pourraient tous être null, vous la curry d'abord, puis vous la mettez dans un Maybe. De plus, mettez également tous les paramètres dans un Maybe et utilisez ensuite "ap" pour exécuter la fonction._

### _Fonction curryN_

_Nous sommes familiers avec "curry". Il convertit simplement une fonction qui prend plusieurs arguments pour les prendre un par un._

_`**//Exemple de Curry :**`_  
_`const add = (a, b) =>a+b;const curriedAdd = R.curry(add);const add10 = curriedAdd(10);//passe le 1er argument. Retourne une fonction qui prend le 2ème paramètre (b).//exécute la fonction en passant le 2ème argument`_  
_`add10(2) // -> 12 //exécute "add" avec 10 et 2 en interne.`_

_Mais au lieu d'additionner seulement deux nombres, que se passe-t-il si la fonction **add** peut additionner tous les nombres passés en argument ?_

_`const add = (...args) => R.sum(args); //additionne tous les nombres dans args`_

_Nous pouvons toujours la curry en limitant le nombre d'args en utilisant **curryN** comme ci-dessous :_

_`**//exemple de curryN**`_  
_`const add = (...args) => R.sum(args);//Exemple de CurryN :`_  
_`const add = (...args) => R.sum(args);const add3Numbers = R.**curryN**(3, add);`_  
_`const add5Numbers = R.**curryN**(5, add);`_  
_`const add10Numbers = R.**curryN**(10, add);add3Numbers(1,2,3) // 6`_  
_`add3Numbers(1) // retourne une fonction qui prend 2 paramètres de plus.`_  
_`add3Numbers(1, 2) // retourne une fonction qui prend 1 paramètre de plus.`_

#### _Utilisation de "curryN" pour attendre un nombre d'appels de fonction_

_Disons que nous voulons écrire une fonction qui ne log que si nous l'appelons 3 fois (et ignorer le 1er et le 2ème appel). Quelque chose comme ci-dessous :_

_`//impure`_  
_`let counter = 0;`_  
_`const logAfter3Calls = () => {`_  
 _`if(++counter == 3)`_  
   _`console.log('called me 3 times');`_  
_`}logAfter3Calls() // Rien ne se passe`_  
_`logAfter3Calls() // Rien ne se passe`_  
_`logAfter3Calls() // 'called me 3 times'`_

_Nous pouvons simuler cela en utilisant curryN comme ci-dessous._

_`//Pure`_  
_`const log = () => {`_  
   _`console.log('called me 3 times');`_  
_`}**const logAfter3Calls = R.curryN(3, log);**//appel`_  
_`**logAfter3Calls('')('')('')**//'called me 3 times'//Note : Nous passons '' pour satisfaire CurryN que nous passons un paramètre.`_

> _**Note : Nous utiliserons cette technique dans la validation Applicative.**_

### _Exemple 4 — Collecte et Affichage de Multiples Erreurs_

_Sujets couverts : **Validation (aka "Validation Functor", "Validation Applicative", "Validation Monad")**._

> _**Validations** sont communément appelées **Validation Applicative** car elles sont couramment utilisées pour la validation en utilisant leur fonction "ap" (apply)._

_**Validations** sont similaires aux **Either Monads** et utilisées pour travailler avec la composition de multiples fonctions générant des erreurs. Mais contrairement à la Monade Either, où nous utilisons typiquement sa méthode "chain" pour composer, dans les Monades Validation, nous utilisons typiquement la méthode "ap" pour composer. Et contrairement à la méthode "chain" de either, où nous ne collectons que la 1ère erreur, **la méthode "ap", surtout dans les Monades Validation, nous permet de collecter toutes les erreurs dans un tableau**._

_Elles sont typiquement utilisées dans la validation de formulaires où nous pouvons vouloir montrer toutes les erreurs en même temps._

_**Cas d'utilisation :** Nous avons un formulaire d'inscription qui valide le nom d'utilisateur, le mot de passe et l'email en utilisant 3 fonctions (isUsernameValid, isPwdLengthCorrect et ieEmailValid. Nous devons montrer toutes les 1, 2 ou 3 erreurs si elles se produisent en même temps._

![Image](https://cdn-media-1.freecodecamp.org/images/1*qru9EDCwqmj-o2FgtVqAQg.png)
_Pour montrer plusieurs erreurs, utilisez le "Validation" Functor_

_D'accord, voyons comment l'implémenter en utilisant "Validation Applicative"._

> _Nous utiliserons la bibliothèque data.validation de [folktalejs](https://github.com/folktale/data.validation) car ramda-fantasy ne l'implémente pas encore._

_Similaire à la Monade "Either", elle a deux constructeurs : **Success** et **Failure**. Ce sont comme des sous-classes qui implémentent chacune les spécifications de Either._

_**Étape 1 :** Pour utiliser Validation, tout ce que nous avons à faire est d'envelopper les valeurs valides et les erreurs dans les constructeurs **Success** et **Failure** (c'est-à-dire créer des instances de ces classes)._

_`const Validation = require('data.validation') //de [folktalejs](https://github.com/folktale/data.validation)`_  
_`const Success = Validation.Success`_  
_`const Failure = Validation.Failure`_  
_`const R = require('ramda');**//Au lieu de :**`_  
_`function isUsernameValid(a) {`_  
    _`return /^(0|[1-9][0-9]*)$/.test(a) ?`_   
           _`["Username can't be a number"] : a`_  
_`}**//Utilisez :**`_  
_`function isUsernameValid(a) {`_  
    _`return /^(0|[1-9][0-9]*)$/.test(a) ?`_   
         _`         **Failure**(["Username can't be a number"]) : **Success**(a)`_  
_`}`_

> _**Répétez le processus pour TOUTES les fonctions de validation générant des erreurs.**_

_**Étape 2 :** Créer une fonction factice pour contenir le succès de la validation._

_`const returnSuccess = () => 'success';//retourne simplement success`_

_**Étape 3 : Utiliser curryN pour appliquer "ap" de manière répétée**_

_Le problème avec "ap" est que le côté gauche doit être un foncteur (ou une monade) contenant une **fonction**._

_Par exemple, disons que nous voulons appliquer "ap" de manière répétée comme ci-dessous. Cela ne fonctionnera que si monad1 contient une fonction. Et le résultat de monad1.ap(monad2) c'est-à-dire **resultingMonad** est également une monade avec une fonction afin que nous puissions "ap" à monad3._

_`**let finalResult = monad1.ap(monad2).ap(monad3)**//Peut être réécrit comme :`_  
_`let resultingMonad = monad1.ap(monad2)`_  
_`let **finalResult** = resultingMonad.ap(monad3)**//ne fonctionnera que si : monad1 a une fonction et monad1.ap(monad2) résulte en une autre monade (resultingMonad) avec une fonction**`_

> _En général, nous avons besoin de 2 monades qui ont des fonctions afin d'appliquer "ap" deux fois._

_Dans notre cas, nous avons 3 fonctions que nous devons appliquer._

_Disons que nous avons fait quelque chose comme ci-dessous._

_`Success(returnSuccess)`_  
        _`.ap(isUsernameValid(username)) //fonctionne`_  
        _`.ap(isPwdLengthCorrect(pwd))//ne fonctionnera pas`_  
        _`.ap(ieEmailValid(email))//ne fonctionnera pas`_

_Ce qui précède ne fonctionnera pas car Success(returnSuccess).ap(isUsernameValid(username)) résultera en une valeur. Et nous ne pouvons plus continuer à faire "ap" sur les 2ème et 3ème fonctions._

_Entrez curryN._

_Nous pouvons utiliser curryN pour continuer à retourner une fonction jusqu'à ce qu'elle soit appelée "N" fois._

_Nous pouvons donc simplement faire :_

_`//3 car nous appelons "ap" 3 fois.`_  
_`let success = R.curryN(3, returnSuccess);`_

_Maintenant, le **success curried continue à retourner une fonction 3 fois.**_

_`function validateForm(username, pwd, email) {`_  
    _`//3 car nous appelons "ap" 3 fois.`_  
    _`let success = R.curryN(3, returnSuccess);    return Success(success)// par défaut ; utilisé pour 3 "ap"s`_  
        _`.ap(isUsernameValid(username))`_  
        _`.ap(isPwdLengthCorrect(pwd))`_  
        _`.ap(ieEmailValid(email))`_  
_`}`_

_Mettre le tout ensemble :_

_**Si vous avez aimé le post en cliquant sur le ? ci-dessous et en le partageant sur Twitter ! Merci pour la lecture !** ??_

### _Mes Autres Posts_

_**DERNIER :** [_Le Fonctionnement Interne du Navigateur — pour les Développeurs JavaScript & Web_](https://medium.com/@rajaraodv/the-inner-workings-of-the-browser-for-javascript-web-developers-course-d26f11270f41) _**Utilisez le code : INNER15 et obtenez 50% de réduction !**__

#### _Programmation Fonctionnelle_

1. _[JavaScript Est Turing Complete — Expliqué](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)_
2. _[Programmation Fonctionnelle En JS — Avec Des Exemples Pratiques (Partie 1)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)_
3. _[Programmation Fonctionnelle En JS — Avec Des Exemples Pratiques (Partie 2)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.mmpv20wsv)_

#### _ES6_

1. _[5 "Mauvais" Côtés de JavaScript Qui Sont Corrigés Dans ES6](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)_
2. _[Est-ce que "Class" Dans ES6 Est La Nouvelle "Mauvaise" Partie ?](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)_

#### _WebPack_

1. _[Webpack — Les Parties Confuses](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)_
2. _[Webpack & Hot Module Replacement [HMR]](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg)_ _(sous le capot)_
3. _[HMR de Webpack et React-Hot-Loader — Le Manuel Manquant](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)_

#### _Draft.js_

1. _[Pourquoi Draft.js Et Pourquoi Vous Devriez Contribuer](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)_
2. _[Comment Draft.js Représente les Données de Texte Riche](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)_

#### _React Et Redux :_

1. _[Guide Pas à Pas Pour Construire des Apps React Redux](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)_
2. _[Un Guide Pour Construire une App React Redux CRUD](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz)_ _(app de 3 pages)_
3. _[Utilisation des Middlewares Dans les Apps React Redux](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)_
4. _[Ajout d'une Validation de Formulaire Robuste aux Apps React Redux](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)_
5. _[Sécurisation des Apps React Redux Avec des Tokens JWT](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)_
6. _[Gestion des Emails Transactionnels Dans les Apps React Redux](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)_
7. _[L'Anatomie d'une App React Redux](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)_

#### _Salesforce_

1. _[Développement d'Applications React Redux Dans Visualforce de Salesforce](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)_