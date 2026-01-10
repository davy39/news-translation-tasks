---
title: Comment fonctionne la programmation modulaire dans Node.js
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-17T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/modular-programming-nodejs-npm-modules
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/alternateimg.png
tags:
- name: backend
  slug: backend
- name: JavaScript
  slug: javascript
- name: node
  slug: node
- name: node js
  slug: node-js
- name: npm
  slug: npm
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la programmation modulaire dans Node.js
seo_desc: 'By Sarvesh Kadam

  Modules are one of the fundamental features of Node.js.

  When you''re building an application, as the code becomes more and more complex
  you cannot put your entire code in one single file.

  As this becomes unmanageable, you can use Node...'
---

Par Sarvesh Kadam

Les modules sont l'une des fonctionnalités fondamentales de Node.js.

Lorsque vous construisez une application, à mesure que le code devient de plus en plus complexe, vous ne pouvez pas mettre tout votre code dans un seul fichier.

Comme cela devient ingérable, vous pouvez utiliser le modèle de module de Node pour écrire différents fichiers et les exporter (y compris les fonctions, les objets et les méthodes) vers le fichier principal.

Maintenant, vous pourriez demander – qu'est-ce qu'un `module` exactement ?

En termes simples, un `module` n'est rien d'autre qu'un fichier JavaScript. C'est tout.

Avec la fonctionnalité modulaire de Node, nous pouvons importer nos propres fichiers externes, les modules principaux (natifs) de Node et les modules NPM. Dans cet article, nous allons discuter de chacun d'eux en détail.

## **Comment importer vos propres fichiers**

Dans cet article, nous allons discuter de la manière dont nous pouvons exporter et importer nos propres fichiers.

En gros, il y a deux fichiers : `calculate.js`, d'où nous allons exporter, et `main.js` où nous allons importer ce fichier.

![mduleexport.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603082860893/xGgR903x4.png)

Nous avons les deux fichiers dans le même dossier pour garder cela simple.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603015526076/cwIgq_IuU.png)

### Comment importer une fonction

```js
//---- Fichier exporté [calculate.js] ----
const add = (a,b)=>{
    return a + b
}

module.exports = add

```

Ici, nous exportons une fonction appelée `add` en utilisant `module.exports`. Ensuite, cette fonction est importée dans un fichier différent en utilisant la méthode `require`.

Dans Node, chaque fichier est appelé un `module`, et `exports` est une propriété de l'objet module.

Nous pouvons maintenant invoquer la fonction dans le fichier différent, c'est-à-dire `main.js`, en passant les arguments comme montré ci-dessous.

```js
//------ Fichier principal [main.js] ----

const add = require('./calculate') //nom du fichier souhaité
const result = add(2,4)
console.log(result); //Sortie : 6


```

### Comment importer un objet

Nous pouvons également exporter un objet entier et accéder aux différentes méthodes qu'il contient.

```js
//---- Fichier exporté [calculate.js]  ----
const add = {
    result : (a,b)=>{
        return a + b
    }
}
module.exports = add


```

Nous avons exporté l'objet `add` et l'avons importé dans notre fichier principal en utilisant la méthode `require`.

Nous pouvons maintenant accéder à la méthode `result` de l'objet `add` en utilisant l'opérateur `.` point :

```javascript
//---- Fichier principal [main.js] ----
const add = require('./calculate')

const result = add.result(5,8)

console.log(result) //Sortie : 13


```

Une autre façon dont nous pouvons exporter l'objet ci-dessus est en exportant uniquement la méthode dont nous avons besoin plutôt que l'objet entier.

```js
//---- Fichier exporté [calculate.js]  ----
const add = {
    result : (a,b)=>{
        return a + b
    }
}

module.exports = add.result

```

Comme vous pouvez le voir, nous importons la méthode `result` dans l'objet `add`. Ainsi, cette méthode peut être directement invoquée dans le fichier principal.

C'est une bonne pratique si vous n'avez pas besoin de l'objet entier mais seulement de certaines méthodes/fonctions de celui-ci. Cela rend également notre code plus sécurisé.

```javascript
//---- Fichier principal [main.js] ----

const add = require('./calculate')
const result = add(5,8)
console.log(result) //Sortie : 13


```

### Comment importer un constructeur de fonction :

Un constructeur de fonction est principalement utilisé pour créer une nouvelle instance d'un objet qui possède les mêmes propriétés que l'objet/fonction principal.

Dans le cas ci-dessous, nous créons une nouvelle instance de l'objet 'Add' en utilisant le mot-clé `new`. Ce processus où nous créons une instance d'un objet est appelé 'instanciation'.

Ensuite, nous exportons cette instance en utilisant `module.exports` :

```js
//---- Fichier exporté [calculate.js]  ----

function Add (){
    this.result = (a,b)=>{
        return a + b
    }
}

module.exports = new Add()


```

Maintenant, nous pouvons l'importer dans notre fichier principal et accéder à la méthode 'result' à l'intérieur pour obtenir notre valeur calculée.

```js
//---- Fichier principal [main.js] ----

const add = require('./calculate2')
const result = add.result(1,3)
console.log(result); //Sortie : 4


```

De cette manière, nous pouvons exporter et importer un constructeur de fonction.

Il existe une autre façon de faire cela, qui consiste à créer notre nouvelle instance dans le fichier principal plutôt que dans le fichier exporté comme montré ci-dessus `module.exports = new Add()`.

Nous verrons comment cela fonctionne lorsque nous exporterons des classes ES6 qui fonctionnent de manière similaire aux constructeurs de fonctions.

### Comment importer des classes ES6

`class` est un type spécial de fonction où le mot-clé `class` aide à l'initialiser. Il utilise la méthode `constructor` pour stocker les propriétés.

Maintenant, nous allons exporter la classe `class` entière en utilisant `module.exports` :

```js
//---- Fichier exporté [calculate.js]  ----

const Add = class{
    constructor(a,b){
        this.a = a;
        this.b = b;
    }

    result(){
        return this.a + this.b
    }
}

module.exports = Add;


```

Maintenant, dans notre fichier principal, nous créons une nouvelle instance en utilisant le mot-clé `new` et accédons à la méthode `result` pour obtenir notre valeur calculée.

```js

//---- Fichier principal [main.js] ----

const add = require('./calculate')

const result = new add(2,5)

console.log(result.result()); //Sortie : 7


```

## Comment importer des modules principaux (natifs) de Node

Plutôt que de créer nos propres modules personnalisés à chaque fois, Node fournit un ensemble de modules pour faciliter notre vie.

Nous allons discuter de certains des modules, mais vous pouvez trouver la liste complète dans la documentation officielle de l'API Node [ici](https://nodejs.org/dist/latest-v15.x/docs/api/).

L'importation des modules Node est similaire à la façon dont vous importez vos propres modules. Vous utilisez la même fonction `require()` pour y accéder dans votre propre fichier.

Mais il y a certains modules que vous avez peut-être utilisés sans le savoir et qui n'ont pas besoin d'être importés. Par exemple, `console.log()` – nous avons utilisé le module `console` de nombreuses fois sans le récupérer dans notre propre fichier local, car ces méthodes sont disponibles **globalement**.

Regardons l'un des modules principaux natifs qui est le **système de fichiers** (`fs`).
Il y a un nombre n de opérations que nous pouvons effectuer avec le module du système de fichiers, telles que la lecture d'un fichier, l'écriture d'un fichier et sa mise à jour, pour n'en nommer que quelques-unes.

Nous allons utiliser le module `fs` pour lire un fichier. Même dans cette méthode, il y a deux façons dont nous pouvons effectuer cette action : l'une en utilisant la fonction synchrone `fs.readFileSync()`, et l'autre par la fonction asynchrone `fs.readFile()`.

Nous discuterons des fonctions Node synchrones-asynchrones dans de futurs articles.

Aujourd'hui, nous utiliserons la version asynchrone, c'est-à-dire `fs.readFile()`.

Pour cet exemple, nous avons créé deux fichiers : `main.js`, où nous allons effectuer l'opération de lecture de fichier, et `file.txt` qui est le fichier que nous allons lire.

![image.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603442034534/DRk8tK6B8.png)

Le fichier `file.txt` contient du texte.

```txt
Bonjour le monde !
```

Maintenant, nous utilisons le module `fs` pour lire le fichier, sans l'importer, comme montré ci-dessous :

```js
fs.readFile('./file.txt','utf-8',(err,data)=>{
    if (err) throw err
    console.log(data);
})
```

Il va lancer une erreur car `fs` n'est pas défini. C'est parce que le module du système de fichiers `fs` n'est pas disponible globalement comme le module `console`.

```powershell
ReferenceError: fs is not defined
    at Object.<anonymous> (C:\Users\Sarvesh Kadam\Desktop\Training\blog\code snippets\Node Modular Pattern\main.js:3:1)
    at Module._compile (internal/modules/cjs/loader.js:1256:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1277:10)
    at Module.load (internal/modules/cjs/loader.js:1105:32)
    at Function.Module._load (internal/modules/cjs/loader.js:967:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:60:12)
    at internal/main/run_main_module.js:17:47

```

Par conséquent, nous devons importer toutes les données du module du système de fichiers en utilisant la fonction `require()` et stocker toutes ces données dans une variable `fs`.

```js
const fs = require('fs')

fs.readFile('./file.txt','utf-8',(err,data)=>{
    if (err) throw err
    console.log(data);
})
```

Maintenant, vous pouvez nommer cette variable comme vous le souhaitez. Je l'ai nommée `fs` pour la lisibilité et c'est la norme que la plupart des développeurs suivent.

En utilisant la variable `fs`, nous pouvons accéder à la méthode `readFile()` où nous avons passé trois arguments. Ces arguments sont le chemin du fichier, l'encodage des caractères `utf-8`, et la fonction de rappel pour donner une sortie.

Vous pourriez demander pourquoi nous passons `utf-8` comme argument dans `readFile()` ?

Parce qu'il encode la valeur et donne le texte comme sortie plutôt que de donner un buffer comme montré ci-dessous :

`<Buffer 48 65 6c 6c 6f 20 57 6f 72 6c 64 21 21>`

La fonction de rappel, à son tour, a deux arguments : une erreur (`err`) et le contenu réel dans le fichier (`data`). Ensuite, nous imprimons ces `data` dans la console.

```powershell
//Sortie:
Bonjour le monde !


```

## **Comment importer des modules NPM**

Alors, qu'est-ce exactement que le gestionnaire de paquets Node ?

Le paquet est un morceau de code qui est géré par le gestionnaire de paquets. Ce n'est rien d'autre qu'un logiciel qui gère l'installation et la mise à jour des paquets.

NPM selon la documentation officielle [documentation](https://docs.npmjs.com/) :

> NPM est le plus grand registre de logiciels au monde. Les développeurs open-source de tous les continents utilisent npm pour partager et emprunter des paquets, et de nombreuses organisations utilisent npm pour gérer le développement privé également.

Ainsi, dans NPM, nous utilisons le code open-source de quelqu'un d'autre géré par NPM en l'important dans notre projet.

NPM vient généralement avec Node JS lorsque vous le téléchargez. Vous pouvez vérifier si NPM est installé sur votre machine en exécutant simplement la commande `npm -v` sur votre invite de commande. Si elle retourne un numéro de version, cela signifie que NPM est installé avec succès.

NPM a son registre à [npmjs.com](https://docs.npmjs.com/) où vous pouvez découvrir des paquets que vous pouvez utiliser.

Regardons l'un des paquets appelés [chalk](https://www.npmjs.com/package/chalk) qui est principalement utilisé pour le style du terminal.

![chalknpm2.jpg](https://cdn.hashnode.com/res/hashnode/image/upload/v1603909979665/T6w4cd8qR.jpeg)

Dans la figure ci-dessus, nous pouvons voir les téléchargements hebdomadaires du paquet, ce qui suggère sa popularité.

De plus, vous pouvez voir que ce paquet a des dépendances. Ainsi, ce module qui servira de dépendance à notre projet dépend lui-même d'autres modules.
Ce processus de gestion entier est pris en charge par le gestionnaire de paquets.

Même le code source qui est présent sur GitHub nous est donné. Nous pouvons y naviguer et vérifier s'il y a des problèmes ouverts présents.

Une chose de plus avant de continuer : les paquets NPM viennent dans différentes versions. Le modèle que la version suit est la version sémantique.

Comme vous pouvez le voir, la dernière version du module [chalk](https://www.npmjs.com/package/chalk) lorsque j'ai écrit cet article est **4.1.0.**

Il suit le modèle de version sémantique `Major_changes`**.**`Minor_changes`**.**`Patch`.

`Major_changes`, comme le nom l'indique, sont les changements significatifs apportés au module qui pourraient affecter votre code existant.

`Minor_changes` sont de nouvelles améliorations ou fonctionnalités ainsi que des corrections de défauts qui ont été ajoutées et qui ne devraient pas affecter votre code existant.

`Patch` est le petit correctif qui ne fera pas planter votre code existant.

Vous pouvez en savoir plus sur la version sémantique sur [semver.org](https://semver.org/).

#### Comment installer NPM

Maintenant, pour importer un paquet de NPM, vous devez d'abord initialiser NPM sur votre dossier de projet local en exécutant la commande sur l'invite de commande :

```powershell
npm init

```

Une fois que vous avez exécuté la commande ci-dessus, elle vous demandera certaines données comme montré ci-dessous, telles que le nom du paquet, la version, etc.

La plupart de ces données peuvent être gardées par défaut comme mentionné dans les parenthèses **()**.
De plus, les champs tels que `author` et `license` sont pour les personnes qui ont créé ces paquets NPM.

D'autre part, nous importons simplement et les utilisons pour créer notre propre application.

```powershell
package name: (code_npm) code_npm
version: (1.0.0) 1.0.0
description: npm demo
entry point: (index.js) index.js
test command: test
git repository:
keywords: npm test
author: Sarvesh
license: (ISC)


```

Une fois que vous avez entré tous les champs, il créera un fichier JSON avec des valeurs qui ont les propriétés ci-dessus, et il vous demandera confirmation comme ceci :

```powershell
Is this OK? (yes) yes

```

Une fois que vous avez confirmé `yes`, il créera un fichier `package.json` avec toutes les données que vous avez entrées comme illustré ci-dessous :

```json
{
  "name": "code_npm",
  "version": "1.0.0",
  "description": "npm demo",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [
    "npm",
    "test"
  ],
  "author": "Sarvesh",
  "license": "ISC"
}


```

De plus, vous pouvez voir un objet `script` qui a une propriété `test` ajoutée. Vous pouvez l'exécuter en utilisant la commande `npm test` et il donnera la sortie souhaitée comme ceci :

```powershell
"Error: no test specified"

```

Maintenant, au lieu de faire cette méthode allongée d'initialisation de NPM et d'entrer les valeurs des propriétés personnalisées, vous pouvez simplement exécuter la commande :

```powershell
npm init -y

```

Une fois que vous avez exécuté cette commande, elle créera directement un fichier `package.json` avec les valeurs par défaut.

![pkgjson.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1603968825440/3fcyAhRJG.png)

Maintenant, pour installer la dernière version du paquet **chalk** dans votre projet, vous devez exécuter la commande :

```powershell
npm install chalk

```

Vous pouvez également installer n'importe quelle version spécifique dont vous avez besoin de chalk en ajoutant simplement `@version number` comme montré ci-dessous. De plus, au lieu de `install`, vous pouvez simplement mettre le raccourci `i` qui signifie installation :

```
npm i chalk@4.0.0

```

Cela installera deux choses, un dossier `node_modules` et un fichier `package-lock.json`.

![folderdir.PNG](https://cdn.hashnode.com/res/hashnode/image/upload/v1603968346848/EAws9k06a.png)

De plus, il ajoutera une nouvelle propriété appelée `dependencies` à notre fichier `package.json` qui contient le nom du paquet installé et sa version.

```json
"dependencies": {
    "chalk": "^4.0.0"
  }

```

Le dossier `node_module` contient le dossier des paquets et les dossiers de ses dépendances. Il est modifié au fur et à mesure que le paquet npm est installé.

Le fichier `package-lock.json` contient le code qui rend NPM plus rapide et plus sécurisé.

```json
"chalk": {
      "version": "4.0.0",
      "resolved": "https://registry.npmjs.org/chalk/-/chalk-4.0.0.tgz",
      "integrity": "sha512-N9oWFcegS0sFr9oh1oz2d7Npos6vNoWW9HvtCg5N1KRFpUhaAhvTv5Y58g880fZaEYSNm3qDz8SU1UrGvp+n7A==",
      "requires": {
        "ansi-styles": "^4.1.0",
        "supports-color": "^7.1.0"
      }

```

Il contient principalement des propriétés telles que `version`, qui est le numéro de version sémantique.

La propriété `resolved` est le répertoire ou l'emplacement à partir duquel le paquet a été récupéré. Dans ce cas, il a été récupéré depuis [chalk](https://www.npmjs.com/package/chalk).

La propriété `integrity` est pour s'assurer que nous obtenons le même code si nous installons à nouveau la dépendance.

La propriété de l'objet `requires` représente la dépendance du paquet `chalk`.

**Note** : Ne faites aucune modification à ces deux fichiers `node_modules` et `package-lock.json`

#### Comment utiliser NPM

Maintenant, une fois que nous avons installé chalk dans notre projet, nous pouvons l'importer dans notre fichier de projet racine en utilisant la méthode `require()`. Ensuite, nous pouvons stocker ce module dans une variable appelée `chalk`.

```js
const chalk = require('chalk')

console.log(chalk.red("Hello World"))
```

En utilisant la méthode `red()` du paquet `chalk`, nous avons stylisé la couleur du texte "Hello World" en rouge.

En exécutant la commande `node index.js`, nous obtenons la sortie suivante :

![chalkop.png](https://cdn.hashnode.com/res/hashnode/image/upload/v1603966334203/3ulfhvZnz.png)

Maintenant, il y a de nombreuses façons dont vous pouvez styliser la sortie de votre ligne de commande en utilisant le paquet chalk. Pour plus d'informations, vous pouvez vous référer à la [documentation officielle de Chalk](https://www.npmjs.com/package/chalk) sur NPM.

De plus, vous pouvez installer les paquets NPM globalement (c'est-à-dire sur notre système d'exploitation) plutôt que de les installer dans votre projet local en ajoutant le drapeau `-g` sur la ligne de commande (qui signifie global, comme mentionné ci-dessous) :

```powershell
npm i nodemon -g

```

Ce paquet global n'affectera pas notre `package.json` de quelque manière que ce soit puisqu'il n'est pas installé localement.

Nous avons installé le paquet `nodemon` globalement qui est utilisé pour le redémarrage automatique d'une application Node lorsque des changements de fichiers dans le répertoire sont observés.
Vous pouvez vous référer à [nodemon](https://www.npmjs.com/package/nodemon) pour plus d'informations.

Nous pouvons utiliser le paquet nodemon en exécutant l'application en utilisant cette commande :

```powershell
nodemon index.js

```

Il fonctionne de manière similaire à `node index.js`, sauf qu'il surveille les changements de fichiers et redémarre l'application une fois que des changements sont détectés.

```powershell
[nodemon] 2.0.6
[nodemon] to restart at any time, enter `rs`
[nodemon] watching path(s): *.*
[nodemon] watching extensions: js,mjs,json
[nodemon] starting `node index.js`
Hello World

```

**Note** : Le style `chalk` ne fonctionnera probablement pas lorsque vous utiliserez `nodemon`.

Enfin, nous allons passer en revue les `dev dependencies`. Il y a certains paquets ou modules NPM dont nous n'aurons pas besoin dans l'environnement de production de notre projet, mais seulement pour nos besoins de développement.

Nous pouvons installer ces modules dans notre projet en utilisant le drapeau `dev` comme montré ci-dessous :

```powershell
 npm i nodemon --save-dev

```

Il crée ensuite une nouvelle propriété dans le `package.json` appelée `devDependencies` :

```json
"devDependencies": {
    "nodemon": "^2.0.6"
  }

```

## Conclusion

En utilisant le modèle de module de Node, nous pouvons importer depuis nos propres fichiers en les exportant sous forme de fonctions, d'objets, de constructeurs de fonctions et de classes ES6.

Et Node a son propre ensemble de modules principaux (natifs) que nous pouvons utiliser. Certains d'entre eux sont disponibles globalement, tandis que d'autres doivent être importés localement dans votre projet/dossier.

NPM est un gestionnaire de paquets qui gère le code open source tiers que nous pouvons utiliser dans notre projet. Avant d'utiliser les modules NPM, vous devez initialiser NPM localement en utilisant `npm init` sur votre ligne de commande à la racine de votre dossier de projet.

Vous pouvez installer n'importe quel paquet NPM en utilisant la commande `npm i <nom du paquet>`. Et vous pouvez installer le paquet NPM globalement en utilisant le drapeau `-g`. De plus, le paquet peut être rendu dépendant du développement en utilisant le drapeau `--save-dev`.

Merci d'avoir lu ! Si vous aimez cet article, n'hésitez pas à me contacter sur [Twitter](https://twitter.com/kadamsarvesh10) alors que je continue à documenter mon apprentissage.