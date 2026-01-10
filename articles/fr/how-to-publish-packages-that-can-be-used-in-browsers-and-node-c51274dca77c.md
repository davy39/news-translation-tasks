---
title: Comment publier des packages utilisables dans les navigateurs et Node
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2019-05-02T15:49:27.000Z'
originalURL: https://freecodecamp.org/news/how-to-publish-packages-that-can-be-used-in-browsers-and-node-c51274dca77c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*bpaO04etYhqF8-OFxen63w.png
tags:
- name: JavaScript
  slug: javascript
- name: Node.js
  slug: nodejs
- name: npm
  slug: npm
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment publier des packages utilisables dans les navigateurs et Node
seo_desc: 'When you create a package for others to use, you have to consider where
  your user will use your package. Will they use it in a browser-based environment
  (or frontend JavaScript)? Will they use it in Node (or backend JavaScript)? Or both?

  If you want ...'
---

Lorsque vous créez un package pour que d'autres l'utilisent, vous devez considérer où votre utilisateur utilisera votre package. L'utilisera-t-il dans un environnement basé sur un navigateur (ou JavaScript frontend) ? L'utilisera-t-il dans Node (ou JavaScript backend) ? Ou les deux ?

Si vous souhaitez créer un package utilisable à la fois dans les navigateurs et Node, cet article est là pour vous aider.

Vous apprendrez :

1. Comment écrire des packages pour une utilisation dans les navigateurs

2. Comment écrire des packages pour une utilisation dans Node

3. Comment publier vos packages pour une utilisation dans les navigateurs et Node

### **Écrire un package pour une utilisation dans les navigateurs**

Si vous souhaitez inclure une bibliothèque dans JavaScript frontend, vous devez d'abord lier la bibliothèque avec une balise `script`. Vous pouvez utiliser la bibliothèque à tout moment après l'avoir liée.

```
<!-- Ceci est du html -->
```

```
<script src="lien-vers-jquery.js"></script>
```

```
<script>  // Vous pouvez utiliser jQuery à tout moment après l'avoir lié  console.log(jQuery)</script>
```

Cela fonctionne parce que JavaScript dans les navigateurs partage une portée globale unique. Peu importe combien de fichiers JavaScript vous liez. Ils se comportent comme s'ils étaient un seul grand fichier JavaScript.

Avec cette information, nous pouvons commencer à écrire une bibliothèque pour une utilisation dans le monde frontend.

Disons que vous souhaitez créer une bibliothèque appelée `peachBlossom`. `peachBlossom` a une fonction `bloom`. Vous écrivez cette fonction `bloom` dans un fichier JavaScript séparé, `peach-blossom.js`.

```
// Ceci est du js
```

```
// peach-blossom.jsfunction bloom () {  console.log('Bloom!')}
```

Vous pouvez inclure `peachBlossom` dans votre JavaScript frontend en liant le fichier `peach-blossom.js`. Une fois que vous avez fait cela, vous pouvez utiliser `bloom` n'importe où.

```
<!-- Ceci est du html -->
```

```
<script src="peach-blossom.js"></script><script src="main.js"></script>
```

```
// Ceci est du js
```

```
// main.jsbloom() // Bloom!
```

Les bibliothèques ont généralement plus d'un morceau de code. Nous ne voulons pas polluer la portée globale avec de petites variables. Ce que nous pouvons faire, c'est envelopper les fonctions que nous voulons exposer dans une expression de fonction immédiatement invoquée (IIFE).

Cela signifie :

1. Nous créons une fonction et l'exécutons immédiatement  
2. Nous retournons la bibliothèque depuis l'intérieur de la fonction pour pouvoir utiliser la bibliothèque plus tard.

En code, cela ressemble quelque peu à ceci :

```
// Ceci est du js
```

```
// peach-blossom.js const peachBlossom = (function () {  // Écrivez autant de code que vous voulez ici
```

```
// Retournez ce que les autres peuvent utiliser  return {    bloom: function () {      console.log('Bloom!')    }  }})()
```

Vous pouvez ensuite utiliser `bloom` n'importe où en écrivant `peachBlossom.bloom`.

```
// Ceci est du js
```

```
// main.jspeachBlossom.bloom() // Bloom!
```

Ce sont les bases de l'écriture d'une bibliothèque frontend.

Maintenant, parlons de l'écriture d'une bibliothèque pour Node.

### **Écrire un package pour Node**

Ajouter une bibliothèque à Node est différent de l'ajout d'une bibliothèque aux navigateurs. Cela est dû au fait que Node n'a pas de fichiers HTML et de balises `<script>`.

Assurons-nous que vous savez comment exécuter Node avant de commencer à écrire une bibliothèque pour Node.

#### Exécuter Node

Tout d'abord, vous devez vous assurer que Node est installé sur votre ordinateur. Vous pouvez installer Node depuis [le site web de Node](https://nodejs.org/en/) si vous ne l'avez pas déjà installé.

Une fois que vous avez Node installé, vous voudrez créer un dossier pour stocker votre projet Node. Dans ce cas, appelons-le « node-project ».

La commande pour créer un dossier est la suivante :

```
# Ceci est du bash
```

```
mkdir node-project
```

Ensuite, vous devez naviguer vers le répertoire `node-project`. Vous pouvez le faire avec `cd` :

```
# Ceci est du bashcd node-project
```

Si vous avez des problèmes avec la ligne de commande, vous pouvez utiliser [ce guide](https://zellwk.com/blog/fear-of-command-line/) pour vous aider.

Ensuite, nous voulons créer un fichier. Ce sera un fichier JavaScript. (Nous exécuterons Node sur ce fichier). Appelons-le `index.js`.

```
# Ceci est du bash
```

```
touch index.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/f0BgtmtrZh4oc2U58UuNiCxOVxx-ibcLd4nE)

Dans `index.js`, nous allons écrire une instruction `console.log`. Cela nous permettra de savoir si nous exécutons le fichier.

```
// Ceci est du js
```

```
// index.jsconsole.log('Exécution de index.js !')
```

Enfin, vous pouvez utiliser `node` pour exécuter `index.js`. Voici la commande :

```
# Ceci est du bash
```

```
node index.js
```

Une fois que vous avez exécuté `index.js`, vous devriez voir le `console.log` dans le terminal. C'est ainsi que nous savons que le fichier a été exécuté.

![Image](https://cdn-media-1.freecodecamp.org/images/b-KuiWqcDHmAGXKBJ6uVsJPwU6bdeRYTCow9)

#### Ajouter des bibliothèques à Node

Pour ajouter des bibliothèques à Node, vous devez utiliser l'instruction `require`. Une fois que vous avez ajouté une bibliothèque, vous pouvez l'utiliser n'importe où dans le même fichier JavaScript.

Voici un exemple :

```
// Ceci est du js
```

```
const fs = require('fs')console.log(fs)
```

![Image](https://cdn-media-1.freecodecamp.org/images/tuH9M9aEGONU-7bU7OlXhK4knqSm0h7WLmN3)

Lorsque vous utilisez `require`, Node recherche la bibliothèque que vous avez spécifiée dans trois endroits :

Tout d'abord, il vérifie si la bibliothèque est intégrée à Node. Dans cet exemple, `fs` est intégré directement à Node. Vous pouvez utiliser `fs` à tout moment si vous utilisez Node.

Ensuite, il vérifie si la bibliothèque existe dans le dossier `node_modules`. Ce sont des bibliothèques installées par l'utilisateur. Vous pouvez ajouter une bibliothèque au dossier `node_modules` en exécutant `npm install`.

Voici un exemple où nous installons `express`, puis nous l'utilisons dans Node :

```
# Ceci est du bash
```

```
# Exécutez ceci dans la ligne de commande
npm install express
```

```
// Ceci est du js 
```

```
// Index.js const express = require('express')console.log(express)
```

![Image](https://cdn-media-1.freecodecamp.org/images/bcyHIXmeoXF45Sr4heQfBSnhFRiTMscQ1iIr)

Troisièmement, si vous ajoutez `./` à `require`, Node recherchera un fichier situé dans le répertoire courant. C'est là que nous pouvons commencer à écrire la bibliothèque `peach-blossom`.

#### Écrire votre première bibliothèque pour Node

Commençons par créer un fichier `peach-blossom.js`. Ce fichier doit être dans le même répertoire que `index.js`.

```
// Ceci est du js
```

```
touch peach-blossom.js
```

![Image](https://cdn-media-1.freecodecamp.org/images/vHap18-jDq8MyfYna0XkLMbHFqeVF7EPQmXP)

Nous pouvons ajouter `peach-blossom.js` à `index.js` en utilisant `require`. Voici à quoi cela ressemble :

```
// Ceci est du js 
```

```
const peachBlossom = require('./peach-blossom')
```

Dans Node, il n'y a pas de concept de portée globale partagée. Chaque fichier a sa propre portée. Donc, si vous écrivez `peach-blossom.js` comme s'il était utilisé pour JavaScript frontend, vous ne pourrez pas l'utiliser. Vous obtiendrez une erreur.

```
// Ceci est du js
```

```
// peach-blossom.js const peachBlossom = (function () { // Écrivez autant de code que vous voulez ici
```

```
// Retournez ce que les autres peuvent utiliser return { bloom: function () { console.log('Bloom!') } }})()
```

```
// Ceci est du js
```

```
// index.js const peachBlossom = require('peach-blossom')
```

![Image](https://cdn-media-1.freecodecamp.org/images/DeVVpx8tTDzGn56qpevFYrfJnDX1RzQTIBcy)

Pour passer des variables d'un fichier à un autre dans Node, vous devez écrire `module.exports`. Les variables passées à `module.exports` peuvent être récupérées depuis un autre fichier.

Cela signifie que nous devons écrire `module.exports` dans `peach-blossom.js`.

```
// Ceci est du js 
```

```
// Écrivez autant de code que vous voulez ici const peachBlossom = { bloom () { console.log('Bloom!') }}
```

```
// Exporte peachBlossom pour une utilisation dans d'autres fichiers
module.exports = peachBlossom
```

Une fois que nous avons exporté `peachBlossom`, nous pouvons l'utiliser dans d'autres fichiers :

```
// Ceci est du js
```

```
// index.js const peachBlossom = require('./peach-blossom')
peachBlossom.bloom() // Bloom!
```

Ce format de passage de variables dans Node avec `require` et `module.exports` est appelé **CommonJS**.

#### Publier votre bibliothèque en tant que package npm

En bref, pour faire fonctionner votre module dans Node, vous devez exporter une variable avec `module.exports`. D'autres personnes peuvent ensuite `require` ce module dans leur code.

À ce stade, vous pouvez déplacer `peach-blossom` dans un dossier de projet séparé et le publier en tant que package npm. Vous pouvez utiliser [ce guide](https://zellwk.com/blog/publish-to-npm/) pour en savoir plus sur le processus de publication.

### Écrire des modules utilisables à la fois en frontend et backend JavaScript

Prenons un moment pour réconcilier ce que nous savons.

Pour écrire une bibliothèque pour le frontend, nous devons la déclarer en tant que variable. Dans la mesure du possible, nous voulons exposer une seule variable.

```
// Ceci est du js
```

```
const peachBlossom = (function () {  // Écrivez autant de code que vous voulez ici
```

```
// Retournez ce que les autres peuvent utiliser  return {    bloom: function () {      console.log('Bloom!')    }  }})()
```

Pour écrire une bibliothèque pour Node, nous devons exporter la variable avec `module.exports`. Ici, nous n'exposons qu'une seule variable.

```
// Ceci est du js
// Écrivez autant de code que vous voulez ici
const peachBlossom = {  bloom () {    console.log('Bloom!')  }}
```

```
// Exporte peachBlossom pour une utilisation dans d'autres fichiers
module.exports = peachBlossom
```

Mais ce sont deux formats complètement différents ! Comment pouvons-nous écrire une bibliothèque une fois et l'utiliser dans les deux contextes ?

Entrez UMD.

#### UMD

[UMD (Universal Module Definition)](https://github.com/umdjs/umd) est un bloc de code que nous pouvons utiliser pour envelopper notre bibliothèque. Ce bloc de code permet d'utiliser une bibliothèque à la fois en frontend et dans Node.

Cela ressemble un peu à ceci :

```
// Ceci est du js
```

```
(function (root, factory) {    if (typeof define === 'function' && define.amd) {        // AMD. Enregistrer en tant que module anonyme.        define(['b'], factory);    } else if (typeof module === 'object' && module.exports) {        // Node.        module.exports = factory(require('b'));    } else {        // Globales du navigateur (root est window)        root.returnExports = factory(root.b);    }}(typeof self !== 'undefined' ? self : this, function (b) {    // Utilisez b de quelque manière.
```

```
// Retournez simplement une valeur pour définir l'exportation du module.    // Cet exemple retourne un objet, mais le module    // peut retourner une fonction en tant que valeur exportée.    return {};}));
```

Whoa ! C'est confus ! Attendez !

En pratique, nous n'avons pas besoin de savoir comment UMD-ifier notre code nous-mêmes. De nombreux outils, comme Webpack et Parcel, nous donnent la possibilité de UMD-ifier notre code à travers eux.

Voici quelques exemples (et leurs instructions de configuration pertinentes) :

1. [Gulp-umd](https://github.com/eduardolundgren/gulp-umd)  
2. [Webpack](https://webpack.js.org/guides/author-libraries/)  
3. [Parcel](https://parceljs.org/cli.html#expose-modules-as-umd)  
4. [Rollup](https://rollupjs.org/guide/en)

Cela signifie que vous devez configurer ces outils si vous souhaitez écrire des packages qui peuvent être utilisés à la fois pour JavaScript Frontend et dans Node. Oui, cela complique le processus d'écriture, mais il n'y a pas grand-chose que nous puissions faire à ce sujet pour le moment.

### Conclusion

Si vous souhaitez que votre bibliothèque fonctionne à la fois sur JavaScript Frontend et dans Node, vous devez envelopper votre module avec UMD (Universal Module Definition).

Si vous souhaitez UMD-ifier votre code, vous devez utiliser un outil de construction lorsque vous écrivez votre package. Cela rend le processus d'écriture plus compliqué. Mais le compromis peut en valoir la peine pour offrir aux utilisateurs une option d'utiliser votre bibliothèque n'importe où.

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/publishing-npm-packages-that-can-be-used-in-browsers-and-node).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.