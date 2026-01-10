---
title: 5 parties "problématiques" de JavaScript corrigées dans ES6
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-13T18:38:01.000Z'
originalURL: https://freecodecamp.org/news/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81
coverImage: https://cdn-media-1.freecodecamp.org/images/1*7wW5ARBnO9lewHr46Eff9A.jpeg
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 5 parties "problématiques" de JavaScript corrigées dans ES6
seo_desc: 'By rajaraodv

  ECMAScript 6 (ES6) features can be divided into features that are pure syntactic
  sugar (like: class), features that enhance JavaScript (like import) and features
  that fix some of JavaScript’s “bad” parts (like the let keyword). Most blog...'
---

Par rajaraodv

Les fonctionnalités d'ECMAScript 6 (ES6) peuvent être divisées en trois catégories : les fonctionnalités qui sont du sucre syntaxique pur (comme : **class**), les fonctionnalités qui améliorent JavaScript (comme **import**) et les fonctionnalités qui corrigent certaines parties "problématiques" de JavaScript (comme le mot-clé **let**). La plupart des blogs et articles combinent ces trois types, ce qui peut submerger les nouveaux venus. C'est pourquoi j'écris cet article qui se concentre uniquement sur les fonctionnalités clés d'ES6 qui corrigent les parties "problématiques".

> **J'espère qu'à la fin de cet article, vous réaliserez qu'en utilisant seulement quelques fonctionnalités d'ES6 comme let et les flèches grasses, vous obtiendrez des retours massifs.**

D'accord, commençons.

### 1. Portée de bloc

ES5 n'avait que la "portée au niveau de la fonction" (c'est-à-dire que vous enveloppez le code dans des fonctions pour créer une portée) et cela a causé beaucoup de problèmes. ES6 fournit une portée au niveau du "bloc" (c'est-à-dire des accolades pour la portée) lorsque nous utilisons "**let**" ou "**const**" au lieu de "**var**".

#### Empêcher le hissing des variables en dehors de la portée

L'image ci-dessous montre que la variable "bonus" n'est pas hissée en dehors du bloc "if", ce qui la fait fonctionner comme dans la plupart des langages de programmation.

> Remarque : Vous pouvez cliquer sur les images pour zoomer et lire

![Image](https://cdn-media-1.freecodecamp.org/images/9FJydx6UlmUycsw0InaURd9mceYbaBOoplVc)

#### Empêcher la déclaration en double de variables

ES6 n'autorise pas la déclaration en double de variables lorsque nous les déclarons en utilisant **"let" ou "const" dans la même portée**. Cela est très utile pour éviter les expressions de fonction en double provenant de différentes bibliothèques (comme l'expression de fonction "add" ci-dessous).

![Image](https://cdn-media-1.freecodecamp.org/images/LYXvvQvqzpsq4lIZDi9np-I371PgBWjk1M28)

#### Élimine le besoin d'IIFE

Dans ES5, dans des cas comme celui ci-dessous, nous devions utiliser une expression de fonction immédiatement invoquée (IIFE) pour nous assurer de ne pas polluer ou écraser la portée globale. Dans ES6, nous pouvons simplement utiliser des accolades ({}) et utiliser **const** ou **let** pour obtenir le même effet.

![Image](https://cdn-media-1.freecodecamp.org/images/p9vja10g1seIjyLnc3QYucY4VCZ11xg1dJaN)

#### Babel — Un outil pour convertir ES6 en ES5

> Nous devons finalement exécuter ES6 dans un navigateur classique. [Babel](http://babeljs.io/) est l'outil le plus populaire utilisé pour convertir ES6 en ES5. Il dispose de diverses interfaces comme une CLI, un module Node et également un convertisseur en ligne. J'utilise le module node pour mes applications et la [version en ligne](http://babeljs.io/repl/) pour voir rapidement les différences.

> L'image ci-dessous montre comment Babel renomme les variables pour simuler "let" et "const" !

![Image](https://cdn-media-1.freecodecamp.org/images/7dFctBbozGKRW2ivDmX3zpc5od6PEiQwAxXJ)
_BabelJS.io renomme les variables pour simuler let et const_

#### Rend trivial l'utilisation de fonctions dans les boucles

Dans ES5, si vous aviez une fonction à l'intérieur d'une boucle (comme for(var i = 0; i < 3; i++) {...}), et si cette fonction essayait d'accéder à la variable de boucle "i", nous aurions des problèmes à cause du hissing. Dans ES6, si vous utilisez **"let"**, vous pouvez utiliser des fonctions sans aucun problème.

![Image](https://cdn-media-1.freecodecamp.org/images/SoAkDH4c6Z9CYxs8X7dTM52a3JefjhLGYTbB)

> Remarque : Vous ne pouvez pas utiliser **const** car il est **constant** sauf si vous utilisez la nouvelle boucle for..of.

### 2. "this" lexical (via les fonctions fléchées)

Dans ES5, "this" peut varier en fonction de "où" il est appelé et même "comment" il est appelé, ce qui a causé toutes sortes de problèmes pour les développeurs JS. ES6 élimine ce problème majeur en utilisant "this" lexical.

> "this" lexical est une fonctionnalité qui force la variable "this" à toujours pointer vers l'objet où elle est **physiquement** située.

#### Le problème et deux solutions de contournement dans ES5 :

Dans l'image ci-dessous, nous essayons d'imprimer le prénom et le salaire d'un utilisateur. Mais nous obtenons le salaire du serveur (simulé). Remarquez que lorsque la réponse revient, "this" est "window" au lieu de l'objet "person".

![Image](https://cdn-media-1.freecodecamp.org/images/l7TGRBGNkWr-gXZhGl24gIuXuGvg6-F59NSt)
_ES5 — le problème et deux solutions de contournement_

#### La solution dans ES6

**Il suffit d'utiliser la fonction fléchée => et vous obtenez automatiquement le "this" lexical.**

![Image](https://cdn-media-1.freecodecamp.org/images/fwFpXGvPX0o4fjxH3ar5Q0KoPysTif17sp5U)
_La ligne 16 montre comment utiliser la fonction =&gt; dans ES6_

> L'image ci-dessous montre comment Babel convertit la fonction fléchée en fonction ES5 régulière avec une solution de contournement pour qu'elle fonctionne dans les navigateurs actuels.

![Image](https://cdn-media-1.freecodecamp.org/images/LJfIVFoY6SUill6l32oESh1zLtPthI6nVDCr)
_Babel convertit la fonction fléchée en fonction ES5 régulière avec la solution de contournement #2_

### 3. Gestion des "arguments"

Dans ES5, "arguments" se comporte comme un tableau (c'est-à-dire que nous pouvons boucler dessus), mais ce n'est pas un tableau. Ainsi, toutes les fonctions de tableau comme sort, slice, etc., ne sont pas disponibles.

Dans ES6, nous pouvons utiliser une nouvelle fonctionnalité appelée paramètres "Rest". Elle est représentée par 3 points et un nom comme **...args**. Les paramètres Rest est un tableau et nous pouvons donc utiliser toutes les fonctions de tableau.

![Image](https://cdn-media-1.freecodecamp.org/images/Hlk7i7KXhBGbyBPt2R0YVlfbxqj0DwNmzf9B)
_L'image montre les paramètres "Rest" d'ES6_

### 4. Classes

Conceptuellement, il n'y a pas de "Classe" (c'est-à-dire un plan) en JS comme dans d'autres langages OO comme Java. Mais depuis longtemps, les gens ont traité la "fonction" (aka "constructeurs de fonctions") qui crée des objets lorsque nous utilisons le mot-clé "new" comme des Classes.

Et puisque JS ne supporte pas les "Classes" et les simule simplement via des "prototypes", sa syntaxe a été très confuse pour les développeurs JS existants et les nouveaux venus qui veulent l'utiliser de manière OO traditionnelle. **Cela est particulièrement vrai pour des choses comme : la création de sous-classes, l'appel de fonctions dans la classe parente, etc.**

ES6 apporte une nouvelle syntaxe courante dans divers langages de programmation et simplifie tout. L'image ci-dessous montre une comparaison côte à côte des classes ES5 et ES6.

> Remarque : Vous pouvez cliquer sur l'image pour zoomer et lire

![Image](https://cdn-media-1.freecodecamp.org/images/b4odOVjDfpH6zTop1QLUFswTJCPudtFOY2Gw)
_ES5 Vs ES6 (es6-features.org)_

> **MISE À JOUR : Assurez-vous de lire : [_La "Classe" dans ES6 est-elle la nouvelle partie "problématique" ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv) _(après cela)_**

### 5. Mode strict

Le [Mode Strict](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode) ("use strict") aide à identifier les problèmes courants (ou les parties "problématiques") et aide également à ["sécuriser" JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode#Securing_JavaScript). Dans ES5, le Mode Strict est optionnel, mais dans ES6, il est nécessaire pour de nombreuses [fonctionnalités ES6](http://www.ecma-international.org/ecma-262/6.0/#sec-strict-mode-code). Ainsi, la plupart des gens et des outils comme Babel ajoutent automatiquement "use strict" en haut du fichier, mettant tout le code JS en mode strict et nous forçant à écrire un meilleur JavaScript.

C'est tout ! ?

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissement ? ci-dessous plusieurs fois pour montrer votre soutien !  ??

### Mes autres articles

[_https://medium.com/@rajaraodv/latest_](https://medium.com/@rajaraodv/latest)

#### ECMAScript 2015+

1. [_Découvrez ces conseils et astuces utiles pour ECMAScript 2015 (ES6)_](https://medium.freecodecamp.org/check-out-these-useful-ecmascript-2015-es6-tips-and-tricks-6db105590377)
2. [_5 parties "problématiques" de JavaScript corrigées dans ES6_](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)
3. [_La "Classe" dans ES6 est-elle la nouvelle partie "problématique" ?_](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)

#### Améliorations du terminal

1. [_Comment personnaliser votre terminal Bash — Un guide étape par étape avec des images_](https://medium.freecodecamp.org/jazz-up-your-bash-terminal-a-step-by-step-guide-with-pictures-80267554cb22)
2. [_Personnalisez votre terminal "ZSH" en sept étapes — Un guide visuel_](https://medium.freecodecamp.org/jazz-up-your-zsh-terminal-in-seven-steps-a-visual-guide-e81a8fd59a38)

#### WWW

1. [_Une histoire fascinante et désordonnée du Web et de JavaScript_](https://medium.freecodecamp.org/a-fascinating-and-messy-history-of-the-web-and-javascript-video-8978dc7bda75)

#### Virtual DOM

1. [_Le fonctionnement interne du Virtual DOM_](https://medium.com/@rajaraodv/the-inner-workings-of-virtual-dom-666ee7ad47cf)

#### Performance de React

1. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)
2. [_Utiliser Preact au lieu de React_](https://medium.com/@rajaraodv/using-preact-instead-of-react-70f40f53107c#.7fzp0lyo3)

#### Programmation fonctionnelle

1. [_JavaScript est Turing Complete — Expliqué_](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)
2. [_Programmation fonctionnelle en JS — Avec des exemples pratiques (Partie 1)_](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)
3. [_Programmation fonctionnelle en JS — Avec des exemples pratiques (Partie 2)_](https://medium.freecodecamp.org/functional-programming-in-js-with-practical-examples-part-2-429d2e8ccc9e)
4. [_Pourquoi Redux a besoin que les réducteurs soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)

#### WebPack

1. [_Webpack — Les parties confuses_](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)
2. [_Webpack & Hot Module Replacement [HMR]_](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg) _(sous le capot)_
3. [_Webpack's HMR et React-Hot-Loader — Le manuel manquant_](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)

#### Draft.js

1. [_Pourquoi Draft.js et pourquoi vous devriez contribuer_](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)
2. [_Comment Draft.js représente les données de texte riche_](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)

#### React et Redux :

1. [_Guide étape par étape pour construire des applications React Redux_](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)
2. [_Un guide pour construire une application React Redux CRUD_](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz) _(application de 3 pages)_
3. [_Utilisation des middlewares dans les applications React Redux_](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)
4. [_Ajout d'une validation de formulaire robuste aux applications React Redux_](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)
5. [_Sécurisation des applications React Redux avec des jetons JWT_](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)
6. [_Gestion des e-mails transactionnels dans les applications React Redux_](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)
7. [_L'anatomie d'une application React Redux_](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)
8. [_Pourquoi Redux a besoin que les réducteurs soient des "fonctions pures"_](https://medium.com/@rajaraodv/why-redux-needs-reducers-to-be-pure-functions-d438c58ae468#.bntrywxrf)
9. [_Deux moyens rapides pour réduire la taille des applications React en production_](https://medium.com/@rajaraodv/two-quick-ways-to-reduce-react-apps-size-in-production-82226605771a#.6lepbl7ae)

#### Si cela vous a été utile, veuillez cliquer sur le bouton d'applaudissement ? ci-dessous plusieurs fois pour montrer votre soutien !  ??