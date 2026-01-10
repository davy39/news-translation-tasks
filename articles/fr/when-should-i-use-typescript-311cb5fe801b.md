---
title: Quand devrais-je utiliser TypeScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-24T08:56:23.000Z'
originalURL: https://freecodecamp.org/news/when-should-i-use-typescript-311cb5fe801b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IkUwv_lceATY-tP7Pf5TeQ.jpeg
tags:
- name: Angular
  slug: angularjs
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Quand devrais-je utiliser TypeScript ?
seo_desc: 'By Alex Ewerlöf

  Last summer we had to convert a huge code base (18,000+ lines of code) from JavaScript
  to TypeScript. I learned a lot about the strengths and weaknesses of each, and when
  it makes sense to use one over the other.

  This article is now a...'
---

Par Alex Ewerlöf

L'été dernier, nous avons dû convertir une énorme base de code (18 000+ lignes de code) de JavaScript à TypeScript. J'ai beaucoup appris sur les forces et les faiblesses de chacun, et quand il est judicieux d'utiliser l'un plutôt que l'autre.

_Cet article est maintenant disponible en [japonais](http://postd.cc/when-should-i-use-typescript/) et en [chinois](http://www.luxingyun.xyz/2016/08/17/%E4%BD%95%E6%97%B6%E5%BA%94%E8%AF%A5%E4%BD%BF%E7%94%A8typescript/)._

### Quand il est judicieux d'utiliser TypeScript

#### **Quand vous avez une grande base de code**

Quand votre base de code est énorme, et que plus d'une personne travaille sur le projet, un système de typage peut vous aider à éviter beaucoup d'erreurs courantes. Cela est particulièrement vrai pour les applications monopage.

À chaque fois qu'un développeur pourrait introduire des changements cassants, il est généralement bon d'avoir un mécanisme de sécurité.

Le [transpileur](https://www.stevefenton.co.uk/2012/11/compiling-vs-transpiling/) TypeScript révèle les erreurs les plus évidentes — bien qu'il n'élimine pas magiquement le besoin de débogage.

Si votre base de code n'est pas si grande, il ne fait probablement pas sens de l'agrandir en ajoutant des annotations de type. J'ai converti 180+ fichiers de JavaScript à TypeScript, et dans la plupart des cas, cela a ajouté environ 30 % à la taille totale du code.

#### **Quand les développeurs de votre équipe sont déjà habitués aux langages à typage statique**

Si vous ou la majorité de l'équipe venez d'un langage à typage fort comme C# ou Java, et que vous ne voulez pas vous engager complètement dans JavaScript, TypeScript est une bonne alternative.

Bien que je recommande d'apprendre JavaScript en profondeur, rien ne vous empêche d'utiliser TypeScript sans connaître JavaScript. En fait, TypeScript a été créé par le [même homme](https://en.wikipedia.org/wiki/Anders_Hejlsberg) qui a fait C#, donc les syntaxes sont similaires.

Dans mon entreprise, nous avions une équipe de développeurs C# qui codait une application desktop sophistiquée en C# et [WPF](https://en.wikipedia.org/wiki/Windows_Presentation_Foundation) (qui est essentiellement un outil de développement front-end pour le monde desktop). Ils ont ensuite été invités à rejoindre un projet web en tant que développeurs full stack. Ainsi, en peu de temps, ils ont pu apprendre TypeScript pour le front-end, puis utiliser leurs connaissances en C# pour le back-end.

#### **TypeScript peut servir de remplacement pour Babel**

L'ancienne Microsoft avait l'habitude de prendre des outils standard — Java par exemple — et d'y ajouter des fonctionnalités non standard propriétaires — résultant dans ce cas en J++. Ensuite, ils essayaient de forcer les développeurs à choisir entre les deux.

TypeScript est exactement la même approche — cette fois pour JavaScript. Au fait, ce n'est pas le premier fork de JavaScript par Microsoft. En 1996, ils ont forké JavaScript pour créer [JScript](https://en.wikipedia.org/wiki/JScript).

Bien que ce soit un cas d'utilisation moins courant, il est techniquement possible de transpiler du code ES6 en ES5 en utilisant le transpileur TypeScript. Cela est possible parce que ES6 est essentiellement un sous-ensemble de TypeScript, et le transpileur [TypeScript](https://www.stevefenton.co.uk/2012/11/compiling-vs-transpiling/) génère du code ES5.

Le transpileur de Typescript génère un code JavaScript (EcmaScript 5) assez lisible en sortie. C'était l'une des raisons pour lesquelles l'équipe Angular 2 a choisi TypeScript plutôt que le langage Dart de Google.

De plus, TypeScript a quelques fonctionnalités sympas qui ne sont pas dans ES6, comme les énumérations et la capacité d'initialiser des variables membres dans un constructeur. Je ne suis pas un grand fan de l'héritage, mais je trouve utile d'avoir les mots-clés _public, private, protected, et abstract_ dans les classes. TypeScript les a et ES6 ne les a pas.

Nos développeurs C# ont trouvé super génial de pouvoir écrire une fonction lambda comme corps d'une méthode — ce qui a éliminé les maux de tête associés au mot-clé _this_.

#### **Quand une bibliothèque ou un framework recommande TypeScript**

Si vous utilisez Angular 2 ou une autre bibliothèque qui recommande TypeScript, allez-y. Jetez un coup d'œil à [ce que ces développeurs ont à dire](http://m12.io/blog/we-launched-angular-2-project) après avoir utilisé Angular 2 pendant six mois.

Sachez simplement que — même si TypeScript peut utiliser toutes les bibliothèques JavaScript directement — si vous voulez de bonnes erreurs de syntaxe, vous devrez ajouter les définitions de type pour ces bibliothèques externement. Heureusement, les gentils gars de [DefinitelyTyped](http://definitelytyped.org/) ont construit un dépôt piloté par la communauté avec des outils pour faire exactement cela. Mais cela reste une étape supplémentaire lorsque vous configurez votre projet.

(En passant : pour tous les fans de JSX, consultez [TSX](http://www.typescriptlang.org/docs/handbook/jsx.html).)

#### **Quand vous ressentez vraiment le besoin de vitesse**

Cela peut vous choquer, mais le code TypeScript peut dans certaines situations performer mieux que JavaScript. Laissez-moi expliquer.

Dans notre code JavaScript, nous avions beaucoup de vérifications de type. C'était une application MedTech, donc même une petite erreur pouvait être littéralement fatale si elle n'était pas traitée correctement. Donc beaucoup de fonctions avaient des instructions comme :

```
if(typeof name !== 'string') throw 'Name should be string'
```

Avec TypeScript, nous avons pu éliminer beaucoup de ces vérifications de type.

Cela a particulièrement montré son effet dans les parties du code où nous avions auparavant un goulot d'étranglement de performance, car nous avons pu sauter beaucoup de vérifications de type inutiles à l'exécution.

### Donc quand est-il préférable de se passer de TypeScript ?

#### **Quand vous ne pouvez pas vous permettre une taxe de transpilation supplémentaire**

Il n'y a pas de plans pour supporter TypeScript nativement dans les navigateurs. Chrome [a fait une expérience](https://developers.google.com/v8/experiments#soundscript), mais a ensuite [annulé](https://groups.google.com/forum/embed/?place=forum/strengthen-js#!topic/strengthen-js/ojj3TDxbHpQ) le support. Je suspecte que cela a quelque chose à voir avec un surcoût inutile à l'exécution.

Si quelqu'un veut des roues d'entraînement, il peut les installer. Mais les vélos ne devraient pas venir avec des roues d'entraînement permanentes. Cela signifie que vous devrez toujours transpiler votre code TypeScript avant de l'exécuter dans un navigateur.

Pour l'ES6 standard, c'est une toute autre histoire. Quand [ES6 sera supporté par la plupart des navigateurs](https://kangax.github.io/compat-table/es6/), la transpilation actuelle de ES6 à ES5 deviendra inutile (mise à jour : [oui en effet](https://medium.freecodecamp.org/you-might-not-need-to-transpile-your-javascript-4d5e0a438ca)!).

ES6 est le plus grand changement pour le langage JavaScript, et je crois que la plupart des programmeurs s'en contenteront. Mais ces quelques courageux qui veulent essayer la prochaine version des fonctionnalités expérimentales de JavaScript, ou les fonctionnalités pas encore implémentées sur tous les navigateurs — ils devront transpiler de toute façon.

Sans transpilation, vous modifiez simplement le fichier et rafraîchissez votre navigateur. C'est tout. Pas besoin de _surveillance_, de _transpilation à la demande_, ou de _système de build_.

Si vous choisissez TypeScript, vous devrez faire un peu de paperasserie supplémentaire pour les définitions de type de vos bibliothèques et frameworks JavaScript (en utilisant DefinitelyTyped ou en écrivant vos propres annotations de type). C'est quelque chose que vous n'auriez pas besoin de faire pour un projet purement JavaScript.

#### **Quand vous voulez éviter des cas limites bizarres de débogage**

Les sourcemaps facilitent le débogage de TypeScript, mais le statu quo n'est pas parfait. Il y a des cas limites vraiment ennuyeux et déroutants.

De plus, il y a quelques problèmes de débogage du mot-clé "this" et des propriétés qui y sont attachées (indice : "this" fonctionne dans la plupart des cas). C'est parce que les sourcemaps n'ont actuellement pas un bon support pour les variables — bien que cela puisse changer dans le futur.

#### **Quand vous voulez éviter des pénalités de performance potentielles**

Dans notre projet, nous avions 9 000+ lignes de bon vieux JavaScript ES5 qui fournissait une puissance brute à un canvas 3D WebGL. Nous l'avons gardé ainsi.

Le transpileur TypeScript (comme Babel) a des fonctionnalités qui nécessitent de générer du code supplémentaire (héritage, enum, génériques, async/await, etc.). Peu importe à quel point votre transpileur est bon, il ne peut pas surpasser les optimisations d'un bon programmeur. Nous avons donc décidé de le garder en ES5 pur pour faciliter le débogage et le déploiement (aucune transpilation).

Cela dit, la pénalité de performance est probablement négligeable par rapport aux avantages d'un système de typage et d'une syntaxe plus moderne pour la plupart des projets. Mais il y a des cas où les millisecondes et même les microsecondes comptent, et dans ces cas, la transpilation de quelque sorte que ce soit n'est pas recommandée (même avec Babel, CoffeeScript, Dart, etc.).

Notez que TypeScript n'ajoute aucun code supplémentaire pour la vérification de type à l'exécution. Toutes les vérifications de type se font au moment de la transpilation et les annotations de type sont supprimées du code JavaScript généré.

#### **Quand vous voulez maximiser l'agilité de votre équipe**

Il est plus rapide de configurer quelque chose en JavaScript. L'absence de système de typage permet une agilité et une facilité de changement. Cela rend aussi plus facile de casser des choses, alors assurez-vous de savoir ce que vous faites.

JavaScript est plus flexible. Rappelez-vous qu'un des principaux cas d'utilisation d'un système de typage est de rendre difficile la casse des choses. Si TypeScript est Windows, JavaScript est Linux.

Dans le monde JavaScript, vous n'avez pas les roues d'entraînement d'un système de typage, et l'ordinateur suppose que vous savez ce que vous faites, mais vous permet de rouler beaucoup plus vite et de manœuvrer plus facilement.

Cela est particulièrement important à noter si vous êtes encore dans la phase de prototypage. Si c'est le cas, ne perdez pas votre temps avec TypeScript. JavaScript est tellement plus flexible.

Rappelez-vous que TypeScript est un sur-ensemble de JavaScript. Cela signifie que vous pouvez facilement convertir JavaScript en TypeScript plus tard si vous en avez besoin.

#### Ma préférence sur JavaScript VS TypeScript

Il n'y a pas une seule meilleure langue en général. Mais pour chaque projet individuel, il y a probablement un meilleur langage, une meilleure bibliothèque, un meilleur framework, une meilleure base de données et un meilleur système d'exploitation, etc.

Pour notre projet, il était judicieux d'utiliser TypeScript. J'ai essayé de refactoriser certains de mes projets personnels en TypeScript, mais cela n'en valait pas la peine.

J'aime personnellement 5 choses à propos de TypeScript :

1. Il est entièrement compatible avec ES6. C'est vraiment bien de voir Microsoft jouer franc jeu avec les autres navigateurs. Notre écosystème peut bénéficier d'un rival fort à Google, Mozilla et Apple. Microsoft y consacre une énergie sérieuse — comme écrire [Visual Studio Code](https://code.visualstudio.com/) à partir de zéro en utilisant TypeScript sur Google Chrome, de toutes les plateformes.
2. Le système de typage est optionnel. Venant d'un background C et Java, j'ai trouvé l'absence de système de typage dans JavaScript libératrice. Mais je détestais perdre du temps quand je rencontrais des bugs stupides pendant l'exécution. TypeScript me permet d'éviter beaucoup de bugs courants afin que je puisse concentrer mon temps à corriger les vrais problèmes délicats. C'est un bon équilibre. J'aime ça. C'est mon goût. J'utilise les types chaque fois que je peux parce que cela me donne la paix de l'esprit. Mais c'est moi. Si j'utilise TypeScript, je ne veux pas me limiter à ses fonctionnalités ES6.
3. Le code JavaScript qui sort du transpileur TypeScript est très lisible. Je ne suis pas un fan des sourcemaps, donc je fais la plupart de mon débogage sur le JavaScript généré. C'est absolument génial. Je peux totalement comprendre pourquoi Angular 2 [a choisi TypeScript plutôt que Dart](https://jaxenter.com/angular-typescript-dart-115426.html).
4. L'expérience de développement de TypeScript est fantastique. [VS Code](https://code.visualstudio.com/) est très intelligent lorsqu'il traite avec JavaScript (certains pourraient argumenter que c'est l'IDE JS le plus intelligent). Mais TypeScript pousse les limites à un tout nouveau niveau. Les fonctionnalités d'autocomplétion et de refactorisation dans VSCode fonctionnent beaucoup plus précisément, et ce n'est pas parce que l'IDE est super intelligent. C'est tout grâce à TypeScript.
5. Les annotations de type sont comme une documentation de base. Elles déclarent le type de données que chaque fonction attend, leurs résultats et divers autres indices comme les attributs `readonly`, `public` ou `private`. Dans mon expérience, en essayant de refactoriser un code JavaScript en TypeScript, j'ai généralement obtenu un code plus propre avec une meilleure structure. En fait, écrire du TypeScript a amélioré la façon dont j'écris du JavaScript pur.

TypeScript n'est pas la réponse à tout. Vous pouvez encore [écrire du code terrible](https://medium.com/@alexewerlof/what-is-shitty-code-handwriting-ae7c00708b) avec.

Les haters de TypeScript vont détester, soit par peur du changement, soit parce qu'ils connaissent quelqu'un qui connaît quelqu'un qui en a peur. La vie continue et TypeScript introduit [de nouvelles fonctionnalités](https://github.com/Microsoft/TypeScript/wiki/What%27s-new-in-TypeScript) à [sa communauté](https://github.com/Microsoft/TypeScript) de toute façon.

Mais comme React, TypeScript est l'une de ces technologies influentes qui pousse les limites de notre développement web.

Que vous utilisiez TypeScript ou non, cela ne fait pas de mal de l'essayer pour vous forger votre propre opinion. Il a une courbe d'apprentissage, mais si vous connaissez déjà JavaScript, elle sera douce.

Voici un [transpileur TS en ligne en temps réel](http://www.typescriptlang.org/Playground) avec quelques exemples qui vous permettent de comparer le code TypeScript avec son équivalent en JavaScript.

Voici un rapide [tutoriel](http://www.typescriptlang.org/Tutorial), et un [très bon guide](http://www.typescriptlang.org/Handbook), mais je suis plus un gars [référence de langage](https://github.com/Microsoft/TypeScript/blob/master/doc/spec.md). Si vous aimez les vidéos, voici [un cours d'Udemy](https://www.udemy.com/typescript/).

John Papa a un [court article](http://johnpapa.net/es5-es2015-typescript/) sur ES5 et TypeScript.

Il y a [une étude intéressante](http://ttendency.cs.ucl.ac.uk/projects/type_study) qui montre que toutes choses égales par ailleurs, un système de typage réduit les bugs de 15 %.

Oh, et si vous avez envie de partir dans une mission secondaire, lisez [pourquoi la programmation est le meilleur travail jamais](https://medium.com/@alexewerlof/what-s-cool-about-being-a-programmer-5a1e58efeee6).