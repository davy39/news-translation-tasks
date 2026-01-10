---
title: JavaScript est Turing Complete — Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-05-19T07:35:59.000Z'
originalURL: https://freecodecamp.org/news/javascript-is-turing-complete-explained-41a34287d263
coverImage: https://cdn-media-1.freecodecamp.org/images/1*u__iwCIORZT5-m_zdiucgA.png
tags:
- name: Computer Science
  slug: computer-science
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: JavaScript est Turing Complete — Expliqué
seo_desc: 'By rajaraodv

  If you start learning functional programming in JavaScript, you’ll probably hear
  about lambda calculus, Turing machine, Turing complete and somehow “JavaScript is
  Turing complete”.

  But, no one seem to explain, in simple terms, what it ac...'
---

Par rajaraodv

Si vous commencez à apprendre la programmation fonctionnelle en JavaScript, vous entendrez probablement parler du [lambda calcul](https://en.wikipedia.org/wiki/Lambda_calculus), de la [machine de Turing](https://en.wikipedia.org/wiki/Turing_machine), de la [complétude de Turing](https://en.wikipedia.org/wiki/Turing_completeness) et, d'une manière ou d'une autre, que « JavaScript est Turing complete ».

Mais personne ne semble expliquer, en termes simples, ce que cela signifie réellement. Quel est le rapport entre une machine de Turing et le langage JavaScript ? De plus, la plupart des gens utilisent du jargon pour expliquer le jargon, comme ceci :

> En [théorie de la calculabilité](https://en.wikipedia.org/wiki/Computability_theory), un système de règles de manipulation de données (comme un [jeu d'instructions](https://en.wikipedia.org/wiki/Instruction_set) d'ordinateur, un [langage de programmation](https://en.wikipedia.org/wiki/Programming_language) ou un [automate cellulaire](https://en.wikipedia.org/wiki/Cellular_automaton)) est dit **Turing complet** ou **universel en calcul** s'il peut être utilisé pour simuler n'importe quelle [machine de Turing](https://en.wikipedia.org/wiki/Turing_machine) à une seule bande. Le concept est nommé d'après le mathématicien anglais [Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing). Un exemple classique est le [lambda calcul](https://en.wikipedia.org/wiki/Lambda_calculus).

Voici donc ma tentative d'expliquer ces concepts simplement.

### Machines de Turing

À l'époque, les gens voulaient savoir comment créer une machine capable d'effectuer tous les calculs qu'ils faisaient à la main. Ils voulaient savoir comment construire une telle machine et comment elle pourrait fonctionner.

[Alan Turing](https://en.wikipedia.org/wiki/Alan_Turing) a imaginé une machine hypothétique capable de prendre n'importe quel programme, quelle que soit sa complexité, et de l'exécuter. Elle pouvait être implémentée en utilisant une simple bande, une tête qui se déplace à gauche et à droite, pouvait stocker des données en lisant, écrivant et effaçant le contenu de cellules carrées. Étant donné une bande suffisamment longue et assez de temps, elle pouvait calculer n'importe quel programme.

En d'autres termes, il a expliqué comment quelqu'un pouvait construire un ordinateur. Et il a appelé cet ordinateur une « machine de Turing ».

> **Anecdote :** À l'époque d'Alan Turing, le mot « ordinateur » désignait la personne qui effectuait manuellement les calculs des programmes (et non les machines) :)

#### Si puissante et pourtant si simple

Les machines de Turing sont rapidement devenues très populaires et ont finalement établi une norme, car bien qu'elles offraient un mécanisme puissant pour calculer n'importe quoi, elles étaient également faciles à comprendre. Comme décrit dans la vidéo ci-dessous, les machines de Turing utilisent une bande pour suivre les états et exécuter des calculs.

#### Machines de Turing à « une » ou « plusieurs » bandes

Un autre jargon que vous entendrez à propos des machines de Turing est le concept de bande « unique ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*YcmJ5nJ_XNXK5PoIjFULTQ.jpeg)

La version initiale de la machine de Turing n'avait qu'une seule longue bande. Plus tard, les gens ont eu l'idée de machines de Turing à « plusieurs » bandes utilisant deux à cinq bandes. **Les machines de Turing à plusieurs bandes n'étaient pas plus puissantes que celles à une seule bande, mais elles aidaient à simplifier les programmes.**

**Il n'est donc pas nécessaire de préciser explicitement « une » bande.**

### Turing Complete

Si une machine physique (comme un ordinateur) ou une machine virtuelle, qui est un logiciel (comme JavaVM), peut prendre **n'importe quel** programme et l'exécuter comme une machine de Turing, alors cette machine est appelée « Turing Complete ». PS : C'est une sorte de certification.

#### Exemples : Machine Turing complete vs Turing incomplete

![Image](https://cdn-media-1.freecodecamp.org/images/1*5KRGqyU6zKHJ7CUIpZ8QRA.jpeg)
_Pas Turing Complete_

Une calculatrice est un bon exemple de **machine Turing incomplete** car elle ne peut effectuer qu'un petit sous-ensemble prédéfini de calculs.

Cependant, un ordinateur personnel (Mac ou PC) est une machine Turing complete car il peut effectuer n'importe quel calcul qu'une machine de Turing peut faire si on lui donne suffisamment de mémoire et de temps.

### « JavaScript est Turing Complete »

Si vous y réfléchissez, une machine de Turing n'est qu'un concept — cela signifie que n'importe quelle « chose » (physique ou virtuelle) qui prend n'importe quel programme et l'exécute est essentiellement une machine de Turing. Et si cette « chose » peut exécuter tous les programmes qu'une « machine de Turing » peut exécuter, alors elle est appelée « Turing Complete ».

Maintenant, si vous pensez à n'importe quel langage de programmation moderne, ils prennent également des programmes (écrits par nous) en entrée et les exécutent. De plus, tout programme qui peut être théoriquement écrit pour être exécuté par une machine de Turing peut également être écrit en JavaScript. **Ainsi, JavaScript est Turing complete.**

**C'est tout !**

_??? Si **vous aimez cet article, veuillez 1. F49AF49AF49A** le **ci-dessous sur Medium et 2. le partager sur Twitter. Vous pouvez retweeter la carte ci-dessous ???_

### _Mes autres articles_

_**DERNIER :** [Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 1)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)_

#### _Programmation Fonctionnelle_

1. _[JavaScript est Turing Complete — Expliqué](https://medium.com/@rajaraodv/javascript-is-turing-complete-explained-41a34287d263#.6t0b2w66p)_
2. _[Programmation Fonctionnelle en JS — Avec des Exemples Pratiques (Partie 1)](https://medium.com/@rajaraodv/functional-programming-in-js-with-practical-examples-part-1-87c2b0dbc276#.fbgrmoa7g)_

#### _ES6_

1. _[5 « Mauvais » Côtés de JavaScript Qui Sont Corrigés Dans ES6](https://medium.com/@rajaraodv/5-javascript-bad-parts-that-are-fixed-in-es6-c7c45d44fd81#.7e2s6cghy)_
2. _[Est-ce que « Class » Dans ES6 Est Le Nouveau « Mauvais » Côté ?](https://medium.com/@rajaraodv/is-class-in-es6-the-new-bad-part-6c4e6fe1ee65#.4hqgpj2uv)_

#### _WebPack_

1. _[Webpack — Les Parties Confuses](https://medium.com/@rajaraodv/webpack-the-confusing-parts-58712f8fcad9#.6ot6deo2b)_
2. _[Webpack & Hot Module Replacement [HMR]](https://medium.com/@rajaraodv/webpack-hot-module-replacement-hmr-e756a726a07#.y667mx4lg)_ _(sous le capot)_
3. _[HMR de Webpack et React-Hot-Loader — Le Manuel Manquant](https://medium.com/@rajaraodv/webpacks-hmr-react-hot-loader-the-missing-manual-232336dc0d96#.fbb1e7ehl)_

#### _Draft.js_

1. _[Pourquoi Draft.js et Pourquoi Vous Devriez Contribuer](https://medium.com/@rajaraodv/why-draft-js-and-why-you-should-contribute-460c4a69e6c8#.jp1tsvsqc)_
2. _[Comment Draft.js Représente les Données de Texte Riche](https://medium.com/@rajaraodv/how-draft-js-represents-rich-text-data-eeabb5f25cf2#.hh0ue85lo)_

#### _React et Redux :_

1. _[Guide Pas à Pas Pour Construire des Applications React Redux](https://medium.com/@rajaraodv/step-by-step-guide-to-building-react-redux-apps-using-mocks-48ca0f47f9a#.s7zsgq3u1)_
2. _[Un Guide Pour Construire une Application React Redux CRUD](https://medium.com/@rajaraodv/a-guide-for-building-a-react-redux-crud-app-7fe0b8943d0f#.g99gruhdz)_ _(application de 3 pages)_
3. _[Utilisation des Middlewares Dans les Applications React Redux](https://medium.com/@rajaraodv/using-middlewares-in-react-redux-apps-f7c9652610c6#.oentrjqpj)_
4. _[Ajout d'une Validation de Formulaire Robuste aux Applications React Redux](https://medium.com/@rajaraodv/adding-a-robust-form-validation-to-react-redux-apps-616ca240c124#.jq013tkr1)_
5. _[Sécurisation des Applications React Redux Avec des Tokens JWT](https://medium.com/@rajaraodv/securing-react-redux-apps-with-jwt-tokens-fcfe81356ea0#.xci6o9s6w)_
6. _[Gestion des E-mails Transactionnels Dans les Applications React Redux](https://medium.com/@rajaraodv/handling-transactional-emails-in-react-redux-apps-8b1134748f76#.a24nenmnt)_
7. _[L'Anatomie d'une Application React Redux](https://medium.com/@rajaraodv/the-anatomy-of-a-react-redux-app-759282368c5a#.7wwjs8eqo)_

#### _Salesforce_

1. _[Développement d'Applications React Redux Dans Visualforce de Salesforce](https://medium.com/@rajaraodv/developing-react-redux-apps-in-salesforce-s-visualforce-3ad7be560d1c#.f6bao6mtu)_

_**Merci d'avoir lu !**_