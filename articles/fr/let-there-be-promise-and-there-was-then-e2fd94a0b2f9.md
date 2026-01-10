---
title: Simplifiez-vous la vie avec les promesses JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-26T11:19:06.000Z'
originalURL: https://freecodecamp.org/news/let-there-be-promise-and-there-was-then-e2fd94a0b2f9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*04bMW0y0-DvpWPoks8GvlA.png
tags:
- name: ES6
  slug: es6
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Simplifiez-vous la vie avec les promesses JavaScript
seo_desc: 'By Ivan Orlov

  If you’re not using Promises in your JavaScript yet, you should give them a try.
  Today I’ll walk you through situations where promises are helpful, and show you
  how to apply them.


  The promise object is used for asynchronous computation...'
---

Par Ivan Orlov

Si vous n'utilisez pas encore les promesses en JavaScript, vous devriez les essayer. Aujourd'hui, je vais vous guider à travers des situations où les promesses sont utiles et vous montrer comment les appliquer.

> L'objet **promise** est utilisé pour les calculs asynchrones. Une promesse représente une opération qui n'est pas encore terminée, mais que vous attendez à compléter à l'avenir.

Qu'est-ce que cela signifie réellement ? Eh bien, si vous avez déjà commencé à utiliser NodeJS, vous avez peut-être déjà entendu parler des promesses. Mais il peut être un peu difficile de saisir le concept. Alors laissez-moi le décomposer pour vous.

Implémentons une [chaîne d'attente](https://tonicdev.com/nchanged/579b31586ee527120007dd57).

![Image](https://cdn-media-1.freecodecamp.org/images/uP5UkvVabNJfwnPqG2oVJyJHiljjbI9VsNYy)

**Wait3** attend **wait2**, et **wait2** attend **wait1**.

Si vous imaginez comment cela pourrait être utile dans une application réelle, pensez aux requêtes de base de données ou aux appels d'API : **Autoriser** -> **accéder** -> **Créer** un post

Toutes ces méthodes sont asynchrones. Nous devons donc avoir un moyen de les synchroniser, puisque JavaScript est asynchrone.

Passer des callbacks est une façon de l'atteindre.

Mais la plupart des développeurs JavaScript sont d'accord : plus vous avez de callbacks imbriqués, plus votre code est mauvais. De plus, comment géreriez-vous les erreurs ?

```
function(e, res){   if (e) { console.log(e) }}
```

Vous devez avoir vu cela souvent. Supposons que vous injectez quelques-unes de ces fonctions dans votre pile de callbacks, mais ensuite vous réalisez que vous devez toutes les attraper et afficher une erreur, par exemple. Et puis vous commencez à danser autour, et rendez votre code encore plus illisible dans le processus.

Voici l'un des extraits que j'ai découverts dans notre ancienne base de code, qui a failli me faire étouffer.

![Image](https://cdn-media-1.freecodecamp.org/images/uLwBVU1PLAkjwBagpoO7qEQUswEEn4CJdcJv)
_La fonction complète — et tous ses callbacks imbriqués — est bien trop grande pour que je puisse la montrer ici._

Après avoir vu assez de ces "pyramides de l'enfer" de callbacks, vous aussi déciderez inévitablement qu'il est temps d'essayer les promesses. Voici à quoi elles ressemblent :

![Image](https://cdn-media-1.freecodecamp.org/images/H9hrCRRfujQxMnD9r-jPw7OYLIQ9Ms9jf2jf)

Cela peut [paraître](https://tonicdev.com/nchanged/579b36a56ee527120007df2c) déroutant au premier abord, mais ne vous inquiétez pas, vous allez comprendre.

J'ai modifié ce code, donc au lieu de passer des callbacks, chaque procédure retourne maintenant une **instance de Promise**. Chaque instance a des méthodes **then** et **catch**, et doit être soit **résolue** soit **rejetée**.

Pourquoi ne pas essayer un exemple primitif d'[authentification](https://tonicdev.com/nchanged/579b3a226ee527120007e086) ?

![Image](https://cdn-media-1.freecodecamp.org/images/BvOclPoZkkJxZunoBmORf-DOTK9A-rJzJCQO)

#### Pourquoi est-ce mieux que d'utiliser des callbacks ?

1. La promotion de l'utilisateur ne sera pas exécutée s'il y a une erreur. Vous pouvez donc totalement compter sur la validité de l'objet utilisateur. Aucune validation supplémentaire n'est requise.
2. Vous pouvez gérer toutes les erreurs au même endroit. Vous n'avez besoin que d'un seul gestionnaire **catch**.
3. Vous pouvez **verticalement** organiser votre code. Vous voulez avoir une fonctionnalité supplémentaire ? Créez une autre promesse et injectez-la dans votre flux en utilisant "**then**"

Mais parfois, ce n'est pas aussi simple que cela en a l'air :

```
flow.procedureC().then(flow.procedureB).then((res) => (   flow.procedureD(res)));
```

Quels inconvénients pouvez-vous repérer [ici](https://tonicdev.com/nchanged/579b17c049cba51300e8f5ab) ? Essayons de les souligner.

### Contexte JavaScript

Lorsque vous passez une fonction dans "then", elle perd son contexte, sauf si elle est liée. Donc, supposons que vous dépendez d'une référence "this" spécifique.

Vous pouvez voir le problème [ici](https://tonicdev.com/nchanged/579b17c049cba51300e8f5ab). (Cela s'exécute automatiquement et vous pouvez lire la sortie presque immédiatement.)

```
flow.procedureC().then(flow.procedureB)
```

Passer "flow.procedureB" dans une promesse sans lier explicitement la référence changera "this" en un objet complètement différent.

Vous obtiendrez une erreur : **flow.procedureB** a perdu son "this".

Et ce n'est pas la faute des promesses. C'est juste comme ça que JavaScript fonctionne.

Heureusement, il existe des solutions de contournement :

#### Liaison

```
flow.procedureC().then(flow.procedureB.bind(flow));
```

> La méthode **bind()** crée une nouvelle fonction qui, lorsqu'elle est appelée, a son mot-clé this défini sur la valeur fournie, avec une séquence donnée d'arguments précédant ceux fournis lorsque la nouvelle fonction est appelée.

Dans notre cas, "this" doit être référencé à l'instance "**flow**".

#### **Utilisation des fermetures** :

```
flow.procedureC().then(() => {    return flow.procedureB()});
```

> Les fermetures sont des fonctions qui font référence à des variables indépendantes (libres) (variables qui sont utilisées localement, mais définies dans une portée englobante). En d'autres termes, ces fonctions "se souviennent" de l'environnement dans lequel elles ont été créées.

Comme prévu, notre fonction de fermeture "s'est souvenue" de l'environnement de "procedureB" qui est "**flow**" et a résolu le problème.

### Partage des résultats

Vous rencontrerez ce problème une fois que vous commencerez à implémenter des tâches non triviales. Lorsque votre application nécessite de passer par de nombreuses étapes, vérifications, modifications, stockage — vous rencontrerez des obstacles avec le **partage** et le **stockage** des résultats dans votre flux.

```
let res_a, res_b, res_c;a().then((res) => {   res_a = res}).then((res) => {   return b();}).then((res) => {   res_b = res;}).then(c).then(() => {   res_a.callSomething()})
```

Pas très beau, n'est-ce pas ? Après avoir résolu **a** et **b**, vous devez toujours continuer à travailler avec les objets résolus, ce qui signifie des étapes redondantes.

> Une promesse retourne un objet à la fois.

![Image](https://cdn-media-1.freecodecamp.org/images/yISReNLja-oPZWohbf1AdcDAr9NDJwpn5ERH)

```
.then((res) => {      res_b = res // Sauvegarde pour réutilisation ultérieure})
```

Vous pouvez consulter cette [discussion](http://stackoverflow.com/questions/28250680/how-do-i-access-previous-promise-results-in-a-then-chain). Attendre, céder — tout cela semble extrêmement attrayant à première vue. Mais la syntaxe ECMAScript 8 n'est pas encore approuvée, et elle est très compliquée pour les débutants.

### Solutions

Avez-vous entendu parler des cascades ou des chaînes ? Une solution serait d'utiliser celles-ci.

[Realm-js](https://github.com/realm-js/realm-js) fournit une solution très puissante et élégante pour partager les portées et organiser les flux de promesses.

![Image](https://cdn-media-1.freecodecamp.org/images/RTon6GrO18yNoBtJtgocO29TrKcS3pYhXHfH)

[Essayez-le en direct !](https://tonicdev.com/57973bc56ee527120006cebd/57973bc56ee527120006cebe)

Les propriétés d'une classe sont exécutées consécutivement. Si vous préfixez votre méthode avec "set", elle stockera le résultat dans la portée. Ainsi, le résultat de "setFoo()" deviendra disponible dans la portée ou la classe (appelons-la "**this**") sous le nom "foo".

**Alors, comment bénéficions-nous d'avoir une classe ?**

* Nous n'avons plus besoin de "then". La chaîne est résolue si elle est promise
* Nous pouvons nommer nos procédures. C'est facile à suivre et à trouver une référence nécessaire
* Nous pouvons partager les résultats prometteurs sans douleur
* Nous pouvons [formater](https://github.com/realm-js/realm-js/blob/master/README.md#formatting-the-output) la sortie si nécessaire

**Vous avez un contrôle total de votre flux :**

* Vous pouvez rompre les chaînes en utilisant [this.$break()](https://github.com/realm-js/realm-js/blob/master/README.md#breaking-chains). C'est pratique. Une fois que vous décidez que vous n'avez pas besoin de continuer avec le flux, appelez la fonction magique et résolvez l'état actuel. (Vous pouvez remplacer la sortie en passant un objet.)
* Vous pouvez également tuer les chaînes en utilisant [_this.$kill()_](https://github.com/realm-js/realm-js/blob/master/README.md#killing-chains-and-ignoring-the-output)_._

En résumé, le chaînage remplace la pratique du "then", convertissant votre flux de promesses en une classe bien structurée. Plus de problèmes de liaison. Juste du code clair. Gagné.

Merci d'avoir lu !

J'espère vraiment que cette approche vous aidera à écrire un meilleur JavaScript. Si vous avez quelque chose à dire, n'hésitez pas à commenter. Discutons de votre code et ensemble nous pouvons résoudre plus de problèmes !