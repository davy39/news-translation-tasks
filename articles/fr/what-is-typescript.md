---
title: Qu'est-ce que TypeScript ?
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-11T00:31:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-typescript
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/typescript.png
tags:
- name: toothbrush
  slug: toothbrush
- name: TypeScript
  slug: typescript
seo_title: Qu'est-ce que TypeScript ?
seo_desc: 'By Frances Coronel

  TypeScript Overview

  So as you are most likely aware, JavaScript is expanding its footprint everyday.
  It is both overwhelming and amazing what you can do with the language nowadays.

  However, as more large-scale projects start to use...'
---

Par Frances Coronel

## **Aperçu de TypeScript**

Comme vous le savez probablement, JavaScript étend son empreinte chaque jour. Il est à la fois impressionnant et incroyable ce que l'on peut faire avec ce langage de nos jours.

Cependant, à mesure que des projets de plus grande envergure commencent à utiliser JavaScript, le processus de rendre le code plus facile à écrire et plus maintenable devient de plus en plus difficile.

C'est un problème que Microsoft a reconnu tôt et ils ont trouvé une solution : TypeScript. La première version a été publiée le 1er octobre 2012.

## **JavaScript vs TypeScript**

![Où est Charlie](https://i.imgur.com/DznuAou.jpg)

Maintenant que nous avons une idée générale de ce qu'est TypeScript, jouons à un rapide jeu de **Où est Charlie**.

Dans la capture d'écran ci-dessus, vous pouvez repérer les différences entre `JavaScript` et `TypeScript` dans ce programme de multiplication très simple qui imprime simplement le produit de deux nombres que j'ai prédéfinis.

### **Quelles sont ces différences ? ?f60f**

Ce sont les **types** !

Ainsi, `JavaScript` a une typage dynamique, ce qui signifie qu'une variable déclarée comme un nombre peut être transformée en chaîne de caractères, alors que `TypeScript` a un typage statique, ce qui signifie que vous déclarez à l'avance quel type de valeur la variable contiendra et cela ne change pas.

Dans ce fichier `multiplication.ts`, je déclare toutes ces variables comme étant des nombres, donc elles ne peuvent pas être changées en autre chose.

En essence, TypeScript essaie d'aider JavaScript à atteindre de nouveaux sommets et à devenir très évolutif. Cela peut être mis en évidence par les caractéristiques suivantes :

* langage de programmation libre et open-source développé et maintenu par Microsoft
* sur-ensemble syntaxique strict de JavaScript qui compile en JavaScript simple
* facilite le développement d'applications à grande échelle écrites en JavaScript
* étend JavaScript en ajoutant des types statiques, des classes, des modules, des interfaces et des génériques

**? LE SAVIEZ-VOUS** TypeScript a eu 7 ans le 1er octobre 2019.

## Version

La dernière version stable disponible est [TypeScript 3.7](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-7.html) (début 2020).

## **Comment installer TypeScript**

![Installation](https://i.imgur.com/9ILjA1q.jpg)

Pour commencer, les deux choses dont vous aurez besoin sont le compilateur TypeScript et un éditeur qui supporte TypeScript.

Dans la capture d'écran ci-dessus, j'installe à la fois le compilateur et [TSLint](https://github.com/palantir/tslint) (qui est similaire à [ESLint](https://eslint.org/)) en utilisant `npm` dans le terminal intégré de [Visual Studio Code](https://code.visualstudio.com/).

### **Installation de TypeScript**

Cette commande installera le package TypeScript comme une dépendance dans votre projet en utilisant [`npm`](https://www.npmjs.com/), qui est un gestionnaire de packages populaire.

```bash
npm i typescript
```

_À noter_ Il existe [plusieurs options](https://docs.npmjs.com/cli/install) que `npm` propose selon l'endroit où vous souhaitez installer TypeScript.

* `npm i -g typescript` pour installer globalement le package TypeScript
* `npm i -D typescript` pour installer le package TypeScript comme une dépendance de développement

### **Compilation d'un seul fichier en JavaScript**

```bash
tsc multiplication.ts
```

_À noter_ Vous pouvez configurer ce processus de compilation TypeScript comme un script npm personnalisé dans votre `package.json`.

### **Options de configuration**

```bash
touch tsconfig.json
```

Il existe également l'option de créer un fichier [`tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html) qui spécifie les fichiers racines et les options du compilateur.

Dans votre fichier [`tsconfig.json`](https://www.typescriptlang.org/docs/handbook/tsconfig-json.html), par exemple, vous pourriez spécifier que vous voulez que TypeScript compile en ES5 au lieu de ES6.

### **Exemple rapide**

![Multiplication](https://i.imgur.com/V5nP3xj.jpg)

Dans la capture d'écran ci-dessus, vous pouvez voir deux fichiers - `multiplication.js` et `multiplication.ts`.

Ce programme imprime simplement le produit de deux nombres que j'ai prédéfinis.

`multiplication.ts`

```typescript
let a: number = 10;
let b: number = 2;

function showProduct(first: number, second: number): void {
  console.info("Mathématique ! Le résultat est " + first * second + ".");
}

showProduct(a, b);

// Mathématique ! Le résultat est 20.
```

Une fois que j'ai terminé de créer `multiplication.ts`, je peux le compiler en JavaScript en utilisant la commande `tsc` qui signifie TypeScript compile.

`multiplication.js`

```javascript
var a = 10;
var b = 2;

function showProduct(first, second) {
    console.info("Mathématique ! Le résultat est " + first * second + ".");
}

showProduct(a, b);

// Mathématique ! Le résultat est 20.
```

Bam - nous venons de compiler avec succès TypeScript en JavaScript !

## **TSLint**

![TSLint](https://2.bp.blogspot.com/-w7oeP1geosE/V82a740bTbI/AAAAAAAAAu4/-zJxZsmmH6garbdmUplX0n5Yz5zDsvcVQCLcB/s1600/tslint.png)

Un [linter](https://www.wikiwand.com/en/Lint_(software)) est un outil qui détecte et signale les erreurs dans les langages de programmation, y compris les erreurs de style.

Pour TypeScript, [TSLint](http://palantir.github.io/tslint) est l'option de linter la plus populaire.

TSLint est un outil d'analyse statique extensible qui vérifie le code TypeScript pour les erreurs de lisibilité, de maintenabilité et de fonctionnalité.

Il est largement supporté dans les éditeurs modernes et les systèmes de construction, et peut être personnalisé avec vos propres règles de lint, configurations et formateurs.

### **Installation de TSLint**

Cette commande installera globalement le package `TSLint` en utilisant `npm`, un gestionnaire de packages populaire.

```bash
npm i -g tslint
```

## Playground

![Playground](https://i.imgur.com/vlV7ZFr.png)

Si vous voulez essayer TypeScript sans l'installer, visitez le [TypeScript Playground](http://www.typescriptlang.org/play/index.html).

Le Playground dispose d'une complétion automatique intégrée et de la possibilité de voir directement le JavaScript émis.

### **Autres ressources**

Pour en savoir plus sur l'installation, consultez l'[Annexe d'installation](https://guide.freecodecamp.org/typescript/src/articles/typescript/appendix-installation/index.md).

Si vous avez besoin uniquement d'un vérificateur de type et ne souhaitez pas compiler votre programme, lisez à propos de [Flux](https://facebook.github.io/flux/).

* [Démarrage rapide](http://www.typescriptlang.org/samples/index.html)
* [Documentation](http://www.typescriptlang.org/docs/home.html)
* [Code source](https://github.com/Microsoft/TypeScript)