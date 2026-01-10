---
title: Qu'est-ce que NodeJS ? Le moteur et l'environnement d'exécution JavaScript
  expliqués pour les débutants
subtitle: ''
author: Brandon Wozniewicz
co_authors: []
series: null
date: '2023-07-17T14:46:01.000Z'
originalURL: https://freecodecamp.org/news/what-is-node-js-explained
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-sevenstorm-juhaszimrus-443383--2-.jpg
tags:
- name: JavaScript
  slug: javascript
- name: node js
  slug: node-js
seo_title: Qu'est-ce que NodeJS ? Le moteur et l'environnement d'exécution JavaScript
  expliqués pour les débutants
seo_desc: Every year another something JS enters the development sphere. With names
  such as VueJS, NextJS, and AngularJS, you may be under the impression that NodeJS
  is a JavaScript framework. Or you've heard that NodeJS is a language. But neither
  of those sta...
---

Chaque année, un autre *quelque chose JS* entre dans la sphère du développement. Avec des noms tels que VueJS, NextJS et AngularJS, vous pourriez avoir l'impression que NodeJS est un framework JavaScript. Ou vous avez entendu dire que NodeJS est un langage. Mais aucune de ces affirmations n'est exacte.

Pour définir NodeJS, nous allons faire un pas en arrière et examiner comment fonctionne JavaScript et discuter de trois composants qui jouent un rôle significatif dans JavaScript :

1. Le langage lui-même
   
2. Le moteur JavaScript
   
3. L'environnement d'exécution JavaScript

## Le langage JavaScript lui-même

JavaScript est un langage de programmation basé sur ECMAScript. Vous pouvez également l'entendre désigner comme un dialecte ou une implémentation de la norme de langage ECMAScript.

Une norme de langage contient un ensemble de règles sur la manière dont un langage doit se comporter. Les dialectes, en revanche, sont des implémentations d'une norme de langage. Tout comme il existe des dialectes régionaux de la langue anglaise, JavaScript est un dialecte—le dialecte le plus populaire—de ECMAScript.

Avant 2008, les développeurs utilisaient uniquement JavaScript pour manipuler des pages web. Mais l'impossibilité d'utiliser JavaScript en dehors du navigateur n'était pas une limitation de JavaScript, le langage, mais une contrainte de l'endroit où ce code JavaScript était exécuté.

## Qu'est-ce que le moteur JavaScript ?

Avant d'aborder où JavaScript est exécuté, nous allons brièvement aborder comment il est exécuté.

Il existe des langages compilés et des langages interprétés. Un langage compilé est comme un repas préparé. Tous les ingrédients ont été mélangés, organisés et arrangés en quelque chose qui doit simplement être cuit. Ils ont été vérifiés au préalable pour s'assurer qu'ils répondent à la norme pour ce repas.

Un langage interprété, en revanche, est comme un chef hibachi qui exécute son art sur le grill pendant que vous regardez. Il prépare votre repas en temps réel, fait des ajustements à la volée et incorpore ses compétences et techniques uniques pour créer le plat final.

Dans le domaine de l'interprétation JavaScript, un moteur JavaScript prend le rôle du chef hibachi, exécutant le code et le faisant vivre sur le grill numérique.

Autant cela peut sembler un acte d'improvisation, le moteur JavaScript met toujours en œuvre des règles spécifiques, assurant la cohérence lors de l'exécution de votre code. (Rappelez-vous que beaucoup de ces règles proviennent de la norme de langage ECMAScript).

Mais il peut vous surprendre que beaucoup de ce qui est écrit par un développeur web ne se trouvera nulle part dans la norme ECMAScript.

Vous voyez, le DOM, par exemple, fait partie d'un "monde extérieur". Et ECMAScript n'a pas de spécifications sur la manière dont JavaScript doit interagir avec ce monde extérieur. Ces règles proviennent d'ailleurs—l'environnement d'exécution JavaScript.

## Qu'est-ce qu'un environnement d'exécution JavaScript ?

Un environnement d'exécution est un lieu ou un environnement où votre code s'exécute. Ce n'est *pas* la chose qui exécute le code elle-même (c'est le moteur) mais plutôt un environnement qui fournit l'accès à certaines parties du monde extérieur.

Imaginez que votre code est une personne à l'intérieur d'une maison. Différentes pièces auront différentes fenêtres qui permettent à cette personne de voir différentes parties de ce qui est à l'extérieur. L'extérieur ne change pas, mais la pièce dans laquelle se trouve la personne déterminera ce qu'elle peut voir. C'est l'essence de ce qu'est un environnement d'exécution JavaScript. C'est comme une pièce dans laquelle vous pouvez placer votre code. Et tout comme la personne à l'intérieur de la maison, la pièce dans laquelle se trouve votre code déterminera quelles parties du monde extérieur il peut accéder.

L'environnement d'exécution JavaScript le plus courant est le navigateur. Et pour le navigateur, les parties du monde extérieur qu'il vous permet de voir (interagir avec) sont l'objet Window et, par conséquent, l'objet document, ou DOM.

Ces objets sont cruciaux pour les développeurs web car ils fournissent les API nécessaires qui permettent à votre JavaScript d'interagir avec les pages web. Ajouter un

, mettre à jour un texte HTML interne ou écouter des événements basés sur la fenêtre sont tous grâce à l'API Web fournie par l'environnement d'exécution du navigateur.

## Alors, qu'est-ce que NodeJS ?

À ce stade, vous avez peut-être une idée de ce qu'est NodeJS. Node est un environnement d'exécution JavaScript. Ce n'est pas un langage ou un framework. C'est simplement un environnement qui vous permet d'écrire du JavaScript qui interagit avec différentes parties du monde extérieur autres que le navigateur.

Au lieu de fournir des choses comme l'API Web, il fournit des API pour interagir avec des composants tels que le système de fichiers, HTTP et le système d'exploitation.

## Comment fonctionne Node

Examinons un exemple de ce que Node peut faire. Vous devrez peut-être installer Node d'abord. La manière la plus simple de l'installer est de visiter NodeJS.org et de télécharger la version LTS (Long-Term Support).

*Écran d'accueil de Node JS org affichant les options de téléchargement*

Nous pouvons vérifier qu'il est installé correctement en ouvrant une invite de commande ou un terminal et en tapant `node -v`.

```js
node -v
> v18.16.0
```

Exécutons notre première commande dans Node. Dans une fenêtre de terminal, démarrez le REPL Node en tapant `node` et en appuyant sur entrée.

Une fois le REPL démarré, nous pouvons exécuter nos premières commandes JavaScript dans l'environnement d'exécution Node. Tapons `console.log(1 + 1)` :

```js
console.log(1+1)
> 2
```

Exécuter des commandes dans le REPL est idéal pour des démonstrations, mais Node ne serait pas bénéfique si c'était le seul endroit où vous pourriez interagir avec l'environnement d'exécution Node. Heureusement, nous pouvons également créer des fichiers JavaScript et les exécuter avec Node.

Créons un fichier JavaScript nommé *main.js.* Ajoutez une instruction console.log et affichez un message de votre choix. Voici ce que j'ai créé :

```js
const msg = 'Hello, World! Here is a message from main.js'

console.log(msg)
```

Depuis votre terminal (dans le même répertoire où vous avez sauvegardé le fichier), tapez `node main.js` et appuyez sur entrée. Vous devriez voir quelque chose de similaire à ce qui suit :

```js
node main.js
> Hello, World! Here is a message from main.js!
```

Faisons une chose de plus avec Node et construisons quelque chose de plus complexe.

Dans cet dernier exemple, nous allons utiliser certains modules intégrés de Node pour créer un fichier HTML et ensuite servir ce fichier, le tout avec JavaScript (dans l'environnement d'exécution Node, bien sûr !).

Tout d'abord, nous allons importer trois modules : FS, OS et HTTP. Ce sont des modules principaux fournis par Node JS.

```js
const fs = require('fs');
const http = require('http');
const os = require('os');
```

Ensuite, nous allons créer le contenu que nous ajouterons au fichier index.html que nous allons créer. Nous allons obtenir le type de système d'exploitation de notre machine et éventuellement remplir notre fichier HTML avec cette information.

```js
// Obtenir le type de système d'exploitation de notre machine
osType = os.type();

// Créer une chaîne de contenu HTML pour un fichier que nous allons créer
htmlContent = '<html><h3>Hello, World! Votre type de système d\'exploitation est ${osType}</h3></html>'
```

Maintenant que nous avons le contenu préparé pour notre fichier HTML, il est temps de créer le fichier. La plupart de ce que nous faisons avec Node JS sera de l'écriture de code asynchrone. Donc pour notre exemple, nous utiliserons des fonctions de rappel pour exécuter tout code que nous voulons nous assurer qu'il s'exécute *après* notre code asynchrone.

Le prochain code à écrire créera le fichier HTML. Nous utilisons le module `fs` et la méthode `writeFile` pour ce faire. Cette fonction accepte un rappel. Nous utiliserons ce rappel pour nous assurer que le fichier a été créé avant de lire le fichier et de créer éventuellement le serveur.

```js
// Créer un fichier index.html avec la variable htmlContent comme contenu.
// Puisque cela est asynchrone, nous fournirons un rappel comme troisième argument
// qui s'exécutera après la création du fichier. C'est dans ce rappel que
// nous lirons le fichier. Pour la clarté du code, nous ne gérerons pas les erreurs.

fs.writeFile('./index.html', htmlContent, (err) => {
    const server = http.createServer((req, res) => {
        fs.readFile('./index.html', (err, content) => {
            res.setHeader('Content-Type', 'text/html');
            res.end(content);
        });
    });
})
```

Nous avons créé le fichier et préparé le serveur jusqu'à ce stade. Mais pour servir le fichier, nous devons démarrer le serveur. Nous utilisons la méthode `listen` sur `createServer` pour démarrer le serveur. Cette fonction accepte plusieurs arguments. Nous allons passer un numéro de port de 3000. Donc, en mettant tout ensemble :

```js
const fs = require('fs');
const http = require('http');
const os = require('os');

// Obtenir le type de système d'exploitation de notre machine
osType = os.type();

// Créer une chaîne de contenu HTML pour un fichier que nous allons créer
htmlContent = '<html><h3>Hello, World! Votre type de système d\'exploitation est ${osType}</h3></html>'

// Créer un fichier index.html avec la variable htmlContent comme contenu.
// Puisque cela est asynchrone, nous fournirons un rappel comme troisième argument
// qui s'exécutera après la création du fichier. C'est dans ce rappel que
// nous lirons le fichier. Pour la clarté du code, nous ne gérerons pas les erreurs.

fs.writeFile('./index.html', htmlContent, (err) => {
    const server = http.createServer((req, res) => {
        fs.readFile('./index.html', (err, content) => {
            res.setHeader('Content-Type', 'text/html');
            res.end(content);
        });
    });
    server.listen(3000);
})
```

Maintenant, rappelez-vous, ce n'est qu'un fichier JavaScript. Le fichier contient le code pour faire tout ce que nous voulons faire, mais nous devons exécuter le script. Exécutons le script et voyons ce qui se passe :

```js
node main.js
>
```

Il peut sembler que le script est bloqué ou cassé. Rappelez-vous, cependant, que nous avons démarré un serveur. Jusqu'à ce que nous annulions le script, le script est en cours d'exécution, et il peut sembler que le script a expiré.

Annulons le serveur (appuyez sur *ctrl + c* deux fois), puis ajoutons un console.log à notre méthode `listen` pour aider à fournir un retour lorsque le serveur est en cours d'exécution. `listen` peut accepter un rappel comme deuxième argument. Nous allons passer une fonction de rappel pour logger une sortie.

```js
server.listen(3000, () => {
    console.log('Écoute sur le port 3000 !');
});
```

Maintenant, lorsque nous exécutons le script, nous devrions voir :

Pour exécuter ce fichier, changez de répertoire où se trouve le fichier et exécutez la commande suivante :

```bash
node main.js
> Écoute sur le port 3000 !
```

Le serveur est en cours d'exécution. Mais où est notre page web ?

Ouvrez un navigateur, entrez *localhost:3000* pour l'URL et appuyez sur entrée. Vous devriez voir quelque chose de similaire à ceci :

*Le contenu du fichier index.html que nous avons créé et servi avec Node !*

Vous l'avez fait ! Vous avez créé une application web simple et l'avez servie avec NodeJS.

## Conclusion

JavaScript, le langage, est une syntaxe écrite exécutée par un moteur JavaScript, qui adhère aux règles établies par la norme ECMAScript.

En plus de la norme de langage, le moteur incorpore des fonctionnalités supplémentaires pour interagir avec le monde extérieur. L'environnement d'exécution JavaScript fournit ces fonctionnalités. Les environnements d'exécution les plus courants sont le navigateur et Node, mais il en existe d'autres comme Deno (similaire à Node mais offrant des fonctionnalités supplémentaires comme la prise en charge native de TypeScript).