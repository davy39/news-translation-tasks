---
title: Comment écrire des tests unitaires plus puissants en utilisant des assertions
  de valeur
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-05T11:26:29.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-powerful-unit-tests-using-value-assertions-3de5146c0088
coverImage: https://cdn-media-1.freecodecamp.org/images/1*kmxDhQcCfG3cuel6qBz2Iw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment écrire des tests unitaires plus puissants en utilisant des assertions
  de valeur
seo_desc: 'By Edd Yerburgh

  Unit tests are awesome. Writing unit tests reduces bugs by 40–80%.

  But you need to do them right. Poorly written unit tests can suffocate a codebase,
  and cause more problems than they solve.

  One way to improve your unit tests is to us...'
---

Par Edd Yerburgh

Les tests unitaires sont géniaux. Écrire des tests unitaires [réduit les bugs de 4080 %](https://www.computer.org/csdl/mags/so/2007/03/s3024.pdf).

Mais il faut les faire correctement. Des tests unitaires mal écrits peuvent étouffer une base de code et causer plus de problèmes qu'ils n'en résolvent.

Une façon d'améliorer vos tests unitaires est d'utiliser des **assertions de valeur**.

Dans cet article, nous allons voir ce que sont les assertions de valeur et comment les utiliser pour améliorer vos tests.

### Comprendre les assertions

Les assertions sont des fonctions qui vérifient que le code s'est comporté comme nous l'attendions.

Différents langages ont différentes conventions. En JavaScript, il est courant de suivre le modèle `expect`. C'est là où vous `expect` une condition pour correspondre à une valeur.

Nous combinons la fonction `expect` avec une autre fonction appelée un **matcher**.

Dans l'exemple ci-dessous, nous `expect` que le résultat de `sum(1,1)` soit égal à `2`. Le matcher `toBe` vérifie que la valeur attendue est égale à `2`.

```
expect(sum(1,1)).toBe(2)
```

Si le résultat de `sum(1,1)` est égal à `2`, la fonction ne fera rien et le test passera. Si `sum(1,1)` n'est pas égal à `2`, la fonction lance une **erreur d'assertion** et le test échoue.

### Débogage des erreurs d'assertion

Dans les frameworks de test, les erreurs d'assertion sont formatées pour rendre le message plus facile à lire. Les erreurs d'assertion vous permettent de comprendre rapidement ce qui a mal tourné dans le test.

Vous pouvez voir une erreur d'assertion [Jest](https://facebook.github.io/jest/) échouée ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/-2e06m0DKQjtjvDUzRoGmkv60nm0HE8YiHFU)
_Une erreur d'assertion Jest_

Pour une raison quelconque, `sum(1,1)` a retourné `3`.

Si nous vérifions le code, nous trouverons que quelqu'un a accidentellement ajouté `b` deux fois :

```
function sum(a,b) {  return a + b + b}
```

Nous pouvons corriger l'erreur rapidement et faire fonctionner à nouveau la fonction `sum`. L'erreur d'assertion nous a aidés à comprendre ce qui a mal tourné et où.

### Qu'est-ce qu'une assertion de valeur ?

Une assertion de valeur est **une assertion qui compare deux valeurs**.

Nous venons d'écrire une assertion de valeur :

```
expect(sum(1,1)).toBe(2)
```

Et cela a généré l'erreur d'assertion :

```
Expected value to be (using ===): 2 Received: 3
```

### Quelles autres assertions existent ?

Une autre assertion courante est une **assertion booléenne**.

Une assertion booléenne est **une assertion qui compare deux booléens**.

```
expect(add(1,1) === 2).toBe(true)
```

Cela génère une erreur d'assertion booléenne :

```
Expected value to be (using ===): true Received: false
```

### Débogage d'une assertion de valeur

Les assertions de valeur lancent des erreurs d'assertion descriptives.

Lorsque un test échoue avec une assertion de valeur, vous pouvez voir pourquoi le test échoue. Cela nous donne un indice sur ce qui se passe dans le code :

```
warning: expected 'somevalue' to equal 'some value'
```

Vous savez quoi chercher dans le code lorsque vous voyez une erreur comme celle-ci. Oh, il semble que quelqu'un ait supprimé un espace par accident.

Les assertions de valeur améliorent la débogabilité (oui, c'est un mot) des tests unitaires. En lisant l'erreur d'assertion, vous pouvez voir ce qui a mal tourné dans le test.

Regardons une erreur d'assertion provenant d'une assertion booléenne :

![Image](https://cdn-media-1.freecodecamp.org/images/fyKQxgYRoihV-B-hRLYOIVVzYhAromkgOkAn)
_Une erreur d'assertion booléenne Jest_

Qu'est-ce qui a mal tourné ?

Il faut plus de temps pour déboguer un test avec une assertion booléenne, car vous ne savez pas quelle valeur a été retournée par le code testé.

Cela rend les erreurs d'assertion booléenne assez inutiles dans les tests unitaires.

### Écrire des assertions de valeur

Nous voulons donc écrire des assertions de valeur.

La plupart des bibliothèques de test JavaScript fournissent des fonctions pour écrire des assertions de valeur.

Jest contient des tonnes de [matchers utiles](https://facebook.github.io/jest/docs/en/expect.html) pour créer des assertions de valeur :

```
.toBeGreaterThan(number).toContain(item).toHaveBeenCalled().toHaveProperty(keyPath, value)
```

### Appel à l'action

Maintenant que vous comprenez la puissance des assertions de valeur, vos tests s'amélioreront.

Allez-y et écrivez des tests unitaires débogables !

Si vous avez aimé cet article, donnez-moi quelques applaudissements pour que plus de gens le voient. Merci !