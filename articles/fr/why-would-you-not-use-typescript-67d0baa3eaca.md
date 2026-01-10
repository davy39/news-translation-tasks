---
title: Pourquoi ne pas utiliser TypeScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T00:22:26.000Z'
originalURL: https://freecodecamp.org/news/why-would-you-not-use-typescript-67d0baa3eaca
coverImage: https://cdn-media-1.freecodecamp.org/images/0*p8qXhijgzkr7h2wT.jpg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: TypeScript
  slug: typescript
- name: Web Development
  slug: web-development
seo_title: Pourquoi ne pas utiliser TypeScript ?
seo_desc: 'By Jonathan Creamer

  In a world where JavaScript is arguably the most popular tool for building software
  these days, it seems like it’s everywhere now. With Node.js, it’s on the backend,
  with Electron it’s native on your machine, with React Native, it...'
---

Par Jonathan Creamer

Dans un monde où JavaScript est sans doute l'outil le [plus populaire](https://insights.stackoverflow.com/survey/2017#technology) pour construire des logiciels de nos jours, il semble qu'il soit partout maintenant. Avec Node.js, il est sur le backend, avec Electron, il est natif sur votre machine, avec React Native, il est natif sur votre téléphone. Il ne fait aucun doute que JavaScript est au moins omniprésent dans tant d'écosystèmes.

Donc, la question suivante que je me pose est, si JavaScript est si populaire, alors TypeScript, par nature de ce qu'il est, devrait également être populaire. Après tout, au cas où vous ne l'auriez pas réalisé...

> _Tout JavaScript que vous pouvez écrire qui est au moins ECMA stage 3 est du TypeScript valide._

![Image](https://cdn-media-1.freecodecamp.org/images/0*TsjAfKA-gbrLIXeu.gif)

### VSCode

Tout d'abord, si vous n'utilisez pas Visual Studio Code pour écrire du JavaScript, vous devriez, alors [allez le télécharger](https://code.visualstudio.com/), et aussi allez chercher [tout ce matériel](http://vscodecandothat.com/) de [Burke Holland](https://twitter.com/burkeholland).

Sous le capot, le compilateur TypeScript fera beaucoup de choses incroyables pour vous sans que vous ayez à y penser à deux fois. La raison pour laquelle il peut faire cela est que VS Code exécute votre JavaScript à travers le compilateur TypeScript, que vous le réalisiez ou non.

[**Microsoft/TypeScript**](https://github.com/Microsoft/TypeScript/wiki/JavaScript-Language-Service-in-Visual-Studio)
[_TypeScript est un sur-ensemble de JavaScript qui compile en un code JavaScript propre._github.com](https://github.com/Microsoft/TypeScript/wiki/JavaScript-Language-Service-in-Visual-Studio)

En plus de cela, il utilise également quelque chose appelé Définitions de Types Automatiques en utilisant la bibliothèque phénoménale [Definitely Typed](https://github.com/DefinitelyTyped/DefinitelyTyped) de définitions de types pour télécharger automatiquement les types pour des milliers de bibliothèques JavaScript populaires.

### De JS à TS, TypeScript vous couvre

Dans l'exemple suivant, nous formatons simplement une chaîne de prix.

Il pourrait être facile d'oublier que si vous passez une chaîne ici, cette fonction explosera parce que `toFixed` n'existe pas sur une chaîne.

Simplement ajouter des types peut vous éviter des bugs à l'exécution...

Mais, il y a encore mieux...

![Image](https://cdn-media-1.freecodecamp.org/images/0*p8qXhijgzkr7h2wT.jpg)

Vous êtes peut-être déjà un grand utilisateur de JSDoc, mais si c'est le cas, vous serez ravi d'apprendre que, depuis une version récente de TypeScript, vous pouvez ajouter `// @ts-check` en haut d'un fichier JavaScript, et obtenir une vérification de type dedans !

![Image](https://cdn-media-1.freecodecamp.org/images/0*nJs9Zs2Uib62uz7_.png)

Voici plus d'informations sur ce que vous pouvez faire avec JSDoc... [https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript](https://github.com/Microsoft/TypeScript/wiki/JSDoc-support-in-JavaScript)

Avec VSCode, vous pouvez activer la vérification complète des types avec l'option de paramètres utilisateur suivante...

```
"javascript.implicitProjectConfig.checkJs": true
```

Vous pouvez ajouter un fichier globals.d.ts et déclarer des choses sous l'espace de noms global si vous avez des interfaces que vous voulez définir dans tout le projet.

```
declare global {  interface IFormatPrice {}}
```

### React

La bonne nouvelle est que TypeScript supporte également React dès la sortie de la boîte en ajoutant ce qui suit à votre tsconfig...

```
{ "jsx": "react" }
```

Maintenant, le vrai plaisir...

![Image](https://cdn-media-1.freecodecamp.org/images/0*5jBFBOXnVAi_A9JB.jpeg)

Les PropTypes sont un excellent moyen de capturer les bugs React à l'exécution. Mais le problème frustrant avec eux est que vous ne savez pas si quelque chose est cassé généralement jusqu'à ce que votre application se construise, que le navigateur ou le rechargement à chaud se recharge, et que vous voyez un message d'erreur rouge cryptique dans la console.

Ne serait-il pas agréable de simplement capturer ce bug en travaillant sur le composant ?

Maintenant, regardez cela...

![Image](https://cdn-media-1.freecodecamp.org/images/0*iI_CtUfjUjoLqTZ1.gif)

Il est incroyable de pouvoir obtenir l'intellisense sur les props. Vous pouvez commencer à taper, ou dans VSCode appuyer sur Control + Space pour ouvrir le menu Intellisense.

Vous pouvez même obtenir l'intellisense sur les classes React également...

![Image](https://cdn-media-1.freecodecamp.org/images/0*4aH83IUb9UbmjI8D.png)

### Conclusion

Que vous décidiez ou non de passer complètement à TypeScript, il est clair que vous pouvez voir de nombreux avantages même si vous restez avec du JavaScript pur.

_Publié à l'origine sur [jonathancreamer.com](http://jonathancreamer.com/why-would-you-not-use-typescript/) le 2 février 2018._