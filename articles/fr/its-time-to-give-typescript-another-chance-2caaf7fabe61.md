---
title: Il est temps de donner une autre chance à TypeScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-17T07:14:38.000Z'
originalURL: https://freecodecamp.org/news/its-time-to-give-typescript-another-chance-2caaf7fabe61
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i0qclSPNcjj8cWOPr3wLxg.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: TypeScript
  slug: typescript
seo_title: Il est temps de donner une autre chance à TypeScript
seo_desc: 'By Jason Dreyzehner

  Since 2012, TypeScript has been a popular choice for programmers coming to JavaScript
  from more structured languages (like C++ or Java). But it’s also been largely dismissed
  by those native to the JavaScript world.

  You may have he...'
---

Par Jason Dreyzehner

Depuis 2012, TypeScript est un choix populaire pour les programmeurs venant à JavaScript depuis des langages plus structurés (comme C++ ou Java). Mais il a également été largement rejeté par ceux qui sont natifs du monde JavaScript.

Vous avez peut-être entendu dire que l'équipe Angular a récemment [passé à TypeScript pour Angular 2](https://vsavkin.com/writing-angular-2-in-typescript-1fa77c78d8e8). Il en va de même pour les équipes derrière [RxJS](https://github.com/ReactiveX/rxjs), [Ionic](https://blog.ionic.io/announcing-ionic-2-0-0-final/), [Cycle.js](https://cycle.js.org/), [Blueprint](https://github.com/palantir/blueprint), [Dojo](https://dojotoolkit.org/community/roadmap/vision.html), [NativeScript](https://github.com/NativeScript/NativeScript), [Plottable](https://github.com/palantir/plottable), et d'autres.

Si vous êtes dans le monde JavaScript/Node.js depuis un certain temps, il est facile de supposer que les décideurs de ces projets ont perdu la tête. Ou peut-être qu'ils ont été payés par Microsoft. ?

![Image](https://cdn-media-1.freecodecamp.org/images/VD0zelL6oRdE5C5mBEc8CV4sOTNNz3PdiNRa)

Et si vous n'avez pas suivi de près, vous avez peut-être manqué les incroyables progrès de TypeScript au cours de la dernière année (et même des derniers mois).

**Si vous pensez toujours « TypeScript est un peu comme CoffeeScript, non ? »—cet article est pour vous.**

Il existe des dizaines de ressources et d'articles excellents sur les avantages de l'utilisation de TypeScript. J'espère qu'après avoir lu ceci, vous y jetterez un autre coup d'œil.

### JavaScript — avec des types ?

Pour ceux qui sont nouveaux dans cette discussion, il est important de comprendre l'aversion qu'une grande partie du monde JavaScript a pour les types. Outre sa portabilité, une grande partie de la popularité de JavaScript pourrait être attribuée à sa simplicité.

> « Pour être attractif pour les hackers, un langage doit être bon pour écrire le genre de programmes qu'ils veulent écrire. Et cela signifie, peut-être de manière surprenante, qu'il doit être bon pour écrire des programmes jetables. » — Paul Graham, [Being Popular](http://paulgraham.com/popular.html)

Le genre de programmeurs qui font de JavaScript leur outil de choix le font souvent pour sa flexibilité. Il n'y a pas de bibliothèque standard, très peu de structure, et sans types, les utilisateurs de JavaScript n'ont pas besoin de passer beaucoup de temps à réfléchir aux détails lorsqu'ils travaillent sur une nouvelle idée.

Cela est probablement plus facile à opposer à un langage comme C++, où les programmes tendent à nécessiter beaucoup plus de structure et de surcharge. Beaucoup de programmeurs JavaScript (en particulier les hackers mentionnés ci-dessus) trouvent que la monotonie des classes traditionnelles, du code boilerplate, des types et du typecasting les ralentit.

> _« Donnez-moi vos fatigués, vos pauvres, vos masses entassées aspirant à respirer librement — des langages de programmation surprotecteurs. » — JavaScript_ ?	_(basiquement)_

Avec cette perspective, il est facile de voir pourquoi beaucoup d'utilisateurs de JavaScript sont si opposés à l'idée de JavaScript avec des types.

**Voici quelques idées qui pourraient aider à apaiser ces craintes.**

### TypeScript est JavaScript avec un meilleur linting

Probablement l'une des préoccupations les plus courantes avec l'idée d'utiliser TypeScript est qu'il n'est pas du JavaScript _pur_. Parce que TypeScript est son propre langage, on suppose que votre code sera transpilé en un globule désordonné que vous serez un jour obligé de déboguer.

![Image](https://cdn-media-1.freecodecamp.org/images/4KJABu71ToVztq9ECbZnIs6Jesry5geC5fq-)
_Trop de gens ont cette impression de TypeScript._

Outre le fait que TypeScript est extrêmement bien testé et largement utilisé, il est worth noter que, selon votre configuration, très peu de « transpilation » se produit réellement (si tant est qu'il y en ait). TypeScript est simplement du JavaScript avec des typages optionnels.

![Image](https://cdn-media-1.freecodecamp.org/images/Op0RURU0iG-XSOpaHcUcbNOhjdDzeAUTPC5f)
_Tapez un peu plus maintenant, obtenez un retour instantané lorsque « add » est utilisé incorrectement. Vous obtenez également une documentation à jour gratuitement (sans balises JSDoc à maintenir), et un excellent support d'éditeur et d'outils._

**TypeScript est comme un linter hautement avancé, capable de vérifier la documentation et d'avertir lorsque le code n'est pas utilisé comme prévu.**

Il fournit un retour immédiat et une meilleure expérience de développement pour tous les futurs utilisateurs de votre code. C'est aussi un bon test pour les nouveaux projets—si votre projet mérite un linting pour faire respecter les conventions de style de code, votre projet est probablement assez durable pour bénéficier de TypeScript.

L'équipe TypeScript s'est [engagée à suivre JavaScript](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Design-Goals) pour l'avenir prévisible. Donc, si/quand des fonctionnalités supplémentaires se stabilisent dans JavaScript, TypeScript les correspondra et s'adaptera.

### TypeScript élimine la surcharge d'exécution

Une autre idée fausse courante est que la vérification des types de TypeScript persiste d'une manière ou d'une autre dans l'environnement d'exécution, ajoutant de la complexité et de la surcharge.

En fait, TypeScript est un bon moyen d'éviter la surcharge de vérification des types d'exécution.

**TypeScript est un outil de développement/temps de compilation** — il prend en charge le JavaScript standard avec des indications de type optionnelles et produit du JavaScript avec ces indications supprimées. (Si activé, il peut également transpiler les fonctionnalités JavaScript ES6 et ES7 vers les normes actuelles.)

Les indications de type de TypeScript nous offrent tous les avantages des types, puis elles disparaissent.

Les seuls indices laissés à l'exécution du _type_ d'un objet sont les mêmes indices fournis par les fonctionnalités JavaScript standard. (Par exemple, lorsque vous créez un nouvel objet à partir d'un prototype, vous pouvez vérifier son type avec `instanceof`.)

Ironiquement, parce que JavaScript ne fournit pas de moyen standard de vérification des types au moment du développement, beaucoup des bibliothèques JavaScript les plus développées **réimplémentent leurs propres systèmes de vérification des types d'exécution**.

![Image](https://cdn-media-1.freecodecamp.org/images/DaV5pfLgbs5XVe8C2mUevmbcf8u8zZHYwJ3Q)
_Vérification des types d'exécution dans la bibliothèque [Snippet→](https://github.com/request/request" rel="noopener" target="_blank" title="">Request</a>. Cela fournit une bien meilleure expérience de débogage pour les utilisateurs qui utilisent la méthode incorrectement. Mais cela nécessite plus de code à l'exécution et plus de cas à tester en unité. <a href="https://github.com/request/request/blob/092e1e657326626da0b8ac4cfe8752751689313b/index.js#L43-L55" rel="noopener" target="_blank" title=")_

Ces bibliothèques n'ont pas l'intention de faire cela au départ, mais faire partie de la fourniture d'une bonne expérience de développement consiste à garantir que les développeurs voient des erreurs claires et exploitables lorsqu'ils ont fait une erreur.

Dans la poursuite de cet objectif, de nombreuses bibliothèques vérifient de manière extensive les types de paramètres passés aux méthodes à l'exécution, lançant des erreurs destinées uniquement aux yeux du développeur implémentant la méthode.

**C'est très certainement le pire des deux mondes.** Ces cascades de vérifications de types d'exécution ajoutent un gonflement significatif du code, rendent le code moins lisible et augmentent la difficulté de maintenir une couverture de test unitaire à 100 %.

À travers de grandes bases de code, ces tests d'exécution s'additionnent vraiment. Après un peu de refactorisation, de nombreuses grandes bases de code finissent par avoir des **systèmes de types entiers**.

![Image](https://cdn-media-1.freecodecamp.org/images/tSTFwJOfo1V4VmlZ8bMJPtQEElxV0fsRmcue)
_[Snippet→](https://github.com/bcoin-org/bcoin/" rel="noopener" target="_blank" title="">Bcoin</a> fournit une bonne expérience de développement en échouant rapidement (à l'exécution) et en émettant des erreurs utiles. Mais cela se fait au coût de la maintenance et des tests d'un système de vérification des types d'exécution extensif. Il serait plus utile et efficace de le faire avec TypeScript. <a href="https://github.com/bcoin-org/bcoin/blob/4e7df6ef875e5936bea5139d922871498b4d9586/lib/primitives/tx.js#L84-L123" rel="noopener" target="_blank" title=")_

Sans utiliser TypeScript, non seulement vous perdez la vérification des types au moment du développement—vous la déplacez souvent à l'exécution. (_J'espère que vous avez une couverture de test complète._)

Lorsque vous utilisez TypeScript, vous offrez à vos utilisateurs une expérience de développement encore meilleure, réduisez la vérification des types d'exécution aux seuls cas où elle est nécessaire (par exemple, l'assainissement de l'entrée de l'utilisateur final) et rendez votre code plus facile à tester complètement en unité.

### TypeScript a parcouru un long chemin

Peut-être pour les raisons mentionnées ci-dessus, lorsque j'ai entendu parler de TypeScript pour la première fois, je suis parti dans la direction opposée aussi vite que possible. Outre le fait qu'il était antithétique à la « meilleure chose à propos de JavaScript » (moins de structure), il était _fait par Microsoft_.

Mais ce n'est plus 2012. TypeScript n'est pas une [abstraction qui fuit](https://en.wikipedia.org/wiki/Leaky_abstraction) de JavaScript, et le projet TypeScript compte parmi les meilleurs hackers et ingénieurs dans ce domaine. (Et je suis impressionné par la façon dont Microsoft le gère.)

**Puisque TypeScript suit ECMAScript, l'utilisation de TypeScript ne verrouille pas votre projet dans un nouveau langage.** Beaucoup de gens ne réalisent toujours pas cela, il n'est donc pas rare d'entendre des sentiments comme :

> « Il est difficile de maintenir un projet TypeScript. »

Ce qui, pour moi, ressemble à :

> « Il est difficile de maintenir un projet avec linting. »

Si votre projet cesse somehow de bénéficier de TypeScript, vous pouvez exécuter votre projet à travers le compilateur (une dernière fois) pour supprimer tous les types de votre base de code.

Ensuite, vous revenez à JavaScript non typé.

### TL;DR

TypeScript s'est beaucoup amélioré récemment. Si vous avez entendu parler de TypeScript il y a des années, mais que vous ne l'avez pas vraiment suivi depuis, cela vaut la peine d'y jeter un autre coup d'œil.

### Quand utiliser TypeScript

#### [**Angular : Pourquoi TypeScript ?**](https://vsavkin.com/writing-angular-2-in-typescript-1fa77c78d8e8)

Une courte discussion technique sur les raisons exactes pour lesquelles l'équipe Angular a choisi TypeScript pour construire Angular 2.

#### [**Toutes les bibliothèques JS devraient être écrites en TypeScript**](http://staltz.com/all-js-libraries-should-be-authored-in-typescript.html)

Un résumé de pourquoi TypeScript est une bonne idée pour les bibliothèques JS, du créateur de Cycle.js et contributeur à RxJS.

#### [**TypeScript Deep Dive — Pourquoi TypeScript**](https://basarat.gitbooks.io/typescript/content/docs/why-typescript.html)

Un bon résumé des avantages de l'utilisation de TypeScript. ([TypeScript Deep Dive](https://basarat.gitbooks.io/typescript/) est une excellente référence générale.)

### En savoir plus sur TypeScript

#### [**Le tutoriel TypeScript**](https://www.typescriptlang.org/docs/tutorial.html)

Un court tutoriel maintenu par l'équipe TypeScript.

#### [**Objectifs de conception de TypeScript**](https://github.com/Microsoft/TypeScript/wiki/TypeScript-Design-Goals)

Un court wiki décrivant les principes généraux de conception de l'équipe TypeScript.

![Image](https://cdn-media-1.freecodecamp.org/images/v6Z91ppLcyGMvaboJMYIqUKa-n-kaubsaqxM)

### [**typescript-starter**](https://github.com/bitjson/typescript-starter)

Un projet de base pour construire des bibliothèques JavaScript. Inclut des tests unitaires appropriés, la génération de documentation, et des exports de modules CommonJS et ES6 (pour Node.js et le navigateur).

J'ai écrit cela dans l'espoir de changer les mentalités. Si vous avez des idées sur la façon dont je pourrais améliorer cet article, veuillez [me le faire savoir](https://twitter.com/bitjson).

Veuillez ❤ et [partager cet article](https://twitter.com/bitjson/status/832497164467183616) si vous l'avez trouvé intéressant. Merci pour la lecture !