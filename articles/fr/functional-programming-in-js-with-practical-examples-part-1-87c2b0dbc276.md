---
title: Programmation Fonctionnelle en JavaScript — Avec des Exemples Pratiques (Partie
  1)
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-11-14T18:28:03.000Z'
originalURL: https://freecodecamp.org/news/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276
coverImage: https://cdn-media-1.freecodecamp.org/images/1*U1TQD4tsM3JLZ-MfBH-vJA.jpeg
tags:
- name: Angular
  slug: angularjs
- name: Functional Programming
  slug: functional-programming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
seo_title: Programmation Fonctionnelle en JavaScript — Avec des Exemples Pratiques
  (Partie 1)
seo_desc: 'By rajaraodv

  Functional Programming(FP) can change the way you program for the better. But it’s
  hard to learn and many posts and tutorials don’t go into details like Monads, Applicative
  and so on and don’t seem to use practical examples to help us us...'
---

Par rajaraodv

La Programmation Fonctionnelle (PF) peut changer la façon dont vous programmez pour le mieux. Mais elle est difficile à apprendre et de nombreux articles et tutoriels n'entrent pas dans les détails comme les Monades, Applicative et ainsi de suite et ne semblent pas utiliser des exemples pratiques pour nous aider à utiliser des techniques PF puissantes au quotidien. C'est pourquoi j'ai pensé à écrire un article pour faciliter l'utilisation des techniques PF.

> Veuillez noter : L'accent dans ce blog est mis sur **POURQUOI** la fonctionnalité xyz est nécessaire plutôt que simplement sur **QUOI** est la fonctionnalité xyz.

**Dans la Partie 1, vous apprendrez les bases de la Programmation Fonctionnelle, le Currying, les Fonctions Pures, les spécifications "Fantasy-land", les "Functors", les "Monads", les "Maybe Monads" et les "Either Monads" via quelques exemples.**

### Programmation Fonctionnelle

La Programmation Fonctionnelle est un style d'écriture de programmes en composant simplement un ensemble de fonctions.

Essentiellement, la PF nous demande d'envelopper virtuellement tout dans des fonctions, d'écrire beaucoup de petites fonctions réutilisables et de les appeler simplement les unes après les autres pour obtenir le résultat comme : (**func1.func2.func3**) ou de manière composée, comme : **func1(func2(func3()))**.

Mais pour écrire des programmes dans ce style, les fonctions doivent suivre certaines règles et surmonter certains défis comme ceux mentionnés ci-dessous :

#### Les Défis de la PF :

Si tout peut être fait en composant un ensemble de fonctions...

1. Comment pouvons-nous gérer les conditions si-sinon ? (**Indice : Monade "Either"**)
2. Comment pouvons-nous gérer les exceptions Null (**Indice : Monade "Maybe"**) ?
3. Comment s'assurer que les fonctions sont vraiment "réutilisables" et peuvent être réutilisées n'importe où, (**Indice :** **Fonctions pures,** **transparence référentielle**) ?
4. Comment s'assurer que les données que nous passons ne sont pas modifiées afin que nous puissions réutiliser les données ailleurs (**Indice :** **Fonctions pures, immutabilité**) ?
5. Si une fonction prend plusieurs valeurs mais que le chaînage ne peut passer qu'une seule valeur, comment pouvons-nous encore en faire partie d'une chaîne (**Indice :** "currying" et "fonctions d'ordre supérieur") ?
6. et plus...<ajoutez votre question ici>.

#### La Solution PF :

Pour faire face à tous ces défis, les langages de Programmation Fonctionnelle complets comme Haskell fournissent divers outils et concepts mathématiques comme les "Monades", les "Functors" et ainsi de suite, prêts à l'emploi.

Bien que JavaScript ne fournisse pas beaucoup de ces outils prêts à l'emploi, heureusement, il dispose de suffisamment de fonctionnalités PF qui permettent aux gens d'écrire des bibliothèques.

### Spécifications Fantasy-Land et Bibliothèques PF

Les bibliothèques qui souhaitent fournir des fonctionnalités comme les Functors, les Monades et ainsi de suite, doivent implémenter des fonctions/classes qui suivent certaines spécifications afin de fournir des fonctionnalités comme elles le sont dans des langages comme Haskell.

[Fantasyland specs](https://github.com/fantasyland/fantasy-land) est l'une des spécifications les plus importantes qui explique comment chaque fonction JS/classes doit se comporter.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwhU3xa-92GSWXCfUg2PKg.png)

L'image ci-dessus montre toutes les spécifications et leurs dépendances. Les spécifications sont essentiellement des lois et similaires aux "interfaces" en Java. Du point de vue JS, vous pouvez penser aux spécifications comme des "classes" ou des fonctions constructrices qui implémentent certaines méthodes comme (**map**, **of**, **chain** et ainsi de suite) selon la spécification.

Par exemple :

Une classe JS est un "Functor" si elle implémente une méthode "map". Et cette méthode map doit fonctionner selon la spécification (ps : ceci est une version simplifiée et il y a plus de règles).

De même, une classe JS est un "Apply Functor" si elle implémente les fonctions "map" et "ap" selon la spécification.

De même, une classe JS est une "Monad" (aka Monad Functor), si elle implémente les exigences de "Functor", "Apply", "Applicative", "Chain" et "Monad" elle-même (en raison de la chaîne de dépendance).

> Note : La dépendance peut sembler être de l'héritage mais pas nécessairement. Par exemple : Monad implémente à la fois les spécifications "Applicative" et "Chain" (en plus d'autres).

#### Bibliothèques conformes aux spécifications Fantasy-Land

Il existe plusieurs bibliothèques qui implémentent la spécification FL. Par exemple : [**monet.js,**](https://cwmyers.github.io/monet.js/) [barely-functional](https://github.com/cullophid/barely-functional), [folktalejs](http://folktalejs.org/), [ramda-fantasy](https://github.com/ramda/ramda-fantasy) (basé sur Ramda), [immutable-ext](https://github.com/DrBoolean/immutable-ext) (basé sur ImmutableJS), [Fluture](https://github.com/Avaq/Fluture) et plus.

### Quelles bibliothèques dois-je utiliser ?

Les bibliothèques comme [**lodash-fp**](https://github.com/lodash/lodash/wiki/FP-Guide)**, [ramdajs](http://ramdajs.com/)**, vous permettent uniquement de commencer à écrire dans le style PF. Mais elles ne fournissent pas de fonctions pour utiliser des concepts mathématiques clés comme les Monades, les Functors, les Foldables pour résoudre réellement des problèmes du monde réel.

Donc, en plus de celles-ci, vous devrez utiliser l'une des bibliothèques qui suivent la spécification fantasy-land. Certaines de ces bibliothèques sont : [monet.js,](https://cwmyers.github.io/monet.js/) **barely-functional, [folktalejs](http://folktalejs.org/), [ramda-fantasy](https://github.com/ramda/ramda-fantasy) (basé sur Ramda), [immutable-ext](https://github.com/DrBoolean/immutable-ext) (basé sur ImmutableJS), [Fluture](https://github.com/Avaq/Fluture) et plus.**

> Note : J'utilise [**ramdajs**](http://ramdajs.com/) et [**ramda-fantasy**](https://github.com/ramda/ramda-fantasy)

OK, maintenant que nous connaissons les bases, voyons quelques exemples pratiques et apprenons diverses fonctionnalités et techniques PF à travers ces exemples.

### Exemple 1 — Gestion des vérifications Null

**Sujets abordés : Functors, Monads, Maybe Monad, Currying.**

**Cas d'utilisation :** Nous voulons afficher différentes pages d'accueil en fonction de la langue "primaire" de l'utilisateur (dans les préférences de l'utilisateur, voir ci-dessous). Et nous devons écrire **getUrlForUser** qui retourne l'URL appropriée à partir de la liste des URL (**indexURLs**) pour la langue **primaire** de l'utilisateur (**joeUser**) (**"espagnol"**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*6jUKhJlc2LK1aGAYilmtNw.png)

**Le problème est :** la langue principale pourrait être nulle. L'utilisateur lui-même pourrait être nul (non connecté). La langue principale pourrait ne pas être disponible dans notre liste d'indexURLs. Nous devrons donc prendre en charge de nombreux "nulls" ou "undefined".

#### Solution (Impératif Vs PF) :

> PS : Ne vous inquiétez pas si la version PF semble difficile à comprendre, je les couvrirai étape par étape plus tard dans cet article.

OK, comprenons d'abord plusieurs concepts et techniques PF utilisés dans cette solution.

#### Functors

Toute classe (ou fonction de construction) ou un type de données qui stocke une valeur et implémente la méthode "map" est appelé un "Functor".

Par exemple : Un Array est un "Functor". Parce qu'un Array peut stocker des valeurs et dispose de la méthode "map" qui nous permet de mapper une fonction aux valeurs qu'il stocke.

```
const add1 = (a) => a+1;
```

```
let myArray = new Array(1, 2, 3, 4); //stocke des valeurs
```

```
myArray.map(add1) // -> [2,3,4,5] //applique des fonctions
```

Écrivons notre propre Functor "MyFunctor". Il s'agit simplement d'une classe JS (fonction constructrice) qui stocke une valeur et implémente une méthode "map". Cette méthode "map" applique la fonction à la valeur stockée puis crée un nouveau Myfunctor à partir du résultat et retourne ce nouveau MyFunctor.

> PS : Les Functors doivent également implémenter d'autres spécifications (voir [Fantasyland specs](https://github.com/fantasyland/fantasy-land)) en plus de "map" mais je ne vais pas les couvrir ici.

#### Monads

Les Monads sont également des Functors, c'est-à-dire qu'ils ont la méthode "map" mais implémentent plus de méthodes que simplement "map". Si vous regardez à nouveau le graphe de dépendance des spécifications, vous verrez qu'ils doivent également implémenter diverses autres fonctionnalités dans différentes spécifications comme : "[Apply](https://github.com/fantasyland/fantasy-land#apply)" (méthode **ap**), "[Applicative](https://github.com/fantasyland/fantasy-land#applicative)" (méthode **ap** et **of**), et "[Chain](https://github.com/fantasyland/fantasy-land#chain)" (méthode **chain**).

![Image](https://cdn-media-1.freecodecamp.org/images/1*fwhU3xa-92GSWXCfUg2PKg.png)

**_Explication simplifiée :_** _En JS, les Monads sont des classes ou des fonctions constructrices qui stockent des données et implémentent les méthodes "map", "ap", "of" et "chain" qui font quelque chose avec les données stockées selon la spécification._

Voici une implémentation d'exemple pour que vous ayez une idée des internes de la Monad.

Maintenant, les Monads génériques ne sont généralement pas utilisées mais des Monads plus spécifiques et plus utiles comme "Maybe Monad" ou "Either Monad" sont souvent utilisées en programmation PF. Alors, jetons un coup d'œil à "Maybe Monad".

**Monade "Maybe"**

Une Monade "Maybe" est une classe qui implémente la spécification Monad. Mais la chose spéciale à propos de Monad est qu'elle prend en charge les valeurs "null" ou "undefined".

**Plus précisément, si les données stockées sont nulles ou non définies, alors sa fonction "map" n'exécute pas du tout la fonction donnée et évite ainsi tout problème de null ou undefined. Elle est utilisée dans les situations où nous traitons des valeurs Null.**

> Le code ci-dessous montre l'implémentation de la Monade Maybe de ramda-fantasy. Elle crée une instance de l'une des deux sous-classes différentes, **Just** ou **Nothing**, selon la valeur (c'est-à-dire une valeur utile V/s null/undefined respectivement).

> Bien que **Just** et **Nothing** aient des méthodes similaires (map, orElse, etc), Just fait réellement quelque chose mais Nothing ne fait rien.

> **Accordez une attention particulière aux méthodes "map" et "orElse" ci-dessous**

Voyons comment utiliser la monade Maybe pour gérer les vérifications "null".

Suivez ces étapes :

1. Si un objet peut être null ou avoir des propriétés nulles, créez un objet Monad à partir de celui-ci.
2. Utilisez certaines bibliothèques comme ramdajs, qui sont "Maybe-aware" pour accéder à la valeur depuis l'intérieur de la Monad et travailler dessus.
3. Fournissez une valeur par défaut si la valeur réelle s'avère être nulle (c'est-à-dire gérez les erreurs Null dès le début).

### Currying — (Aide à la gestion des données globales et des fonctions multi-paramètres)

Sujets abordés : **Fonctions pures** et **Composition**

Si nous voulons enchaîner une série de fonctions ensemble comme : func1.func2.func3 ou (func1(func2(func3())), toutes ces fonctions ne peuvent recevoir qu'un seul paramètre d'entrée chacune. Par exemple, si func2 prend deux paramètres func2(param1, param2), alors nous ne pouvons pas l'enchaîner !

Mais en pratique, de nombreuses fonctions prennent plusieurs paramètres. Alors comment les utiliser dans la composition ? Solution : "Currying".

Le Currying convertit une fonction qui prend plusieurs paramètres en une fonction qui prend un seul paramètre à la fois. Elle n'exécute pas la fonction jusqu'à ce que tous les paramètres soient passés.

#### De plus, le Currying peut également être utilisé dans des situations où nous accédons à des valeurs globales. c'est-à-dire la rendre "pure".

Regardons à nouveau notre solution :

### Exemple 2— Gestion des fonctions de levée d'erreurs et sortie immédiate après une erreur

**Sujets abordés : Monade "Either"**

La Monade Maybe est géniale si nous avons des valeurs "par défaut" pour remplacer les erreurs Null. Mais qu'en est-il des fonctions qui doivent réellement lever des erreurs ? Et comment savoir quelle fonction a levé l'erreur lorsque nous enchaînons plusieurs fonctions de levée d'erreurs (c'est-à-dire que nous voulons une défaillance rapide) ?

Par exemple : Si nous avons **func1.func2.func3…** et si **func2** lève une erreur, nous devons sauter **func3** et les autres fonctions futures et afficher correctement l'erreur de **func2** afin de pouvoir la gérer.

### **Monade Either**

Les Monades Either sont géniales pour gérer plusieurs fonctions lorsqu'elles peuvent toutes potentiellement lever des erreurs et vouloir quitter immédiatement après une erreur afin que nous puissions pointer où l'erreur s'est produite.

**Cas d'utilisation :** Par exemple, dans l'extrait impératif ci-dessous, nous calculons la "taxe" et la "remise" pour les "articles" et affichons finalement le "showTotalPrice".

Notez que la fonction "taxe" lèvera une erreur si le prix n'est pas numérique. De même, la fonction "remise" lèvera une erreur si le prix n'est pas numérique et lèvera également une erreur si le prix de l'article est inférieur à 10.

> Donc **showTotalPrice** a plusieurs vérifications d'erreurs.

Voyons comment **showTotalPrice** peut être amélioré en utilisant la Monade Either et réécrivons tout dans le style PF.

La Monade Either fournit deux constructeurs : "Either.Left" et "Either.Right". Considérez-les comme des sous-classes de Either. **Les deux "Left" et "Right" sont des Monades !** **L'idée est de stocker les erreurs/exceptions dans Left et les valeurs utiles dans Right**.

c'est-à-dire créer une instance de Either.Left ou Either.Right selon la valeur. **Une fois que nous avons fait cela, nous pouvons exécuter map, chain et ainsi de suite sur ces valeurs pour les composer.**

> Bien que **Left** et **Right** fournissent "map", "chain" et ainsi de suite, le constructeur **Left** ne fait rien car il stocke des Erreurs. Alors que le constructeur **Right** implémente toutes les fonctions car il contient le résultat réel.

**OK, voyons comment changer notre exemple impératif en PF**

**Étape 1 :** Envelopper les valeurs de retour avec Left et Right

> Note : "Envelopper" signifie créer une instance de quelque Classe. Ces fonctions appellent interne "new" donc nous n'avons pas à le faire.

**Étape 2 :** Envelopper la valeur initiale dans **Right** car c'est une valeur valide et donc nous pouvons la composer.

```
const getItemPrice = (item) => Right(item.price);
```

**Étape 3 :** Créer deux fonctions, une pour gérer l'erreur éventuelle et une autre pour gérer le résultat. Et les envelopper dans **Either.either** (ceci provient de [ramda-fantasy.js api](https://github.com/ramda/ramda-fantasy/blob/master/src/Either.js#L33)).

> **Either.either** prend 3 paramètres. un gestionnaire de succès, un gestionnaire d'erreurs et une Monade "Either". Either est curryfiée. Donc nous pouvons simplement passer les gestionnaires pour l'instant et passer l'Either (3ème paramètre) plus tard.

> Une fois que Either.either reçoit les 3 paramètres, il passe le 3ème paramètre "Either" au gestionnaire de succès ou au gestionnaire d'erreurs selon que l'Either est "Right" ou "Left" respectivement.

```
const displayTotal = (total) => { console.log('Prix Total : ' + total) };
```

```
const logError = (error) => { console.log('Erreur : ' + error.message); };
```

```
const eitherLogOrShow = Either.either(logError, displayTotal);
```

**Étape 4 :** Utiliser la méthode "chain" pour composer plusieurs fonctions de levée d'erreurs. Passer leur résultat à Either.either (eitherLogOrShow) qui se chargera de passer le résultat au gestionnaire de succès ou au gestionnaire d'échec.

```
const showTotalPrice = (item) => eitherLogOrShow(getItemPrice(item).chain(apply25PercDisc).chain(addCaliTax));
```

En mettant tout ensemble :

Merci d'avoir lu ! Si vous avez aimé l'article, veuillez ? et le partager sur Twitter !?

**DERNIER :** [_Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)

### Mes Autres Articles

#### Programmation Fonctionnelle

1. [_JavaScript Est Turing Complete — Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 2)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e#.r2mglxozr)

#### ES6

1. [_5 "Mauvaises" Parties de JavaScript Qui Sont Corrigées En ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
2. [_"Class" En ES6 Est-Elle La Nouvelle "Mauvaise" Partie ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### WebPack

1. [_Webpack — Les Parties Confuses_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_HMR de Webpack et React-Hot-Loader — Le Manuel Manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js Et Pourquoi Vous Devriez Contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js Représente les Données de Texte Riche_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide Étape par Étape Pour Construire des Apps React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un Guide Pour Construire une App React Redux CRUD_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(app de 3 pages)_
3. [_Utilisation des Middlewares Dans les Apps React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajout d'une Validation de Formulaire Robuste aux Apps React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécurisation des Apps React Redux Avec des Tokens JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gestion des Emails Transactionnels Dans les Apps React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'Anatomie d'une App React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)

#### Salesforce

1. [_Développement d'Apps React Redux Dans Visualforce de Salesforce_](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)