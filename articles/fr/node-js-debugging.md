---
title: Comment déboguer une application Node.js avec VSCode, Docker et votre terminal
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-12T22:41:28.000Z'
originalURL: https://freecodecamp.org/news/node-js-debugging
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/hacking-coding-code-hack.jpg
tags:
- name: debugging
  slug: debugging
- name: Docker
  slug: docker
- name: node js
  slug: node-js
- name: terminal
  slug: terminal
- name: Visual Studio Code
  slug: vscode
seo_title: Comment déboguer une application Node.js avec VSCode, Docker et votre terminal
seo_desc: 'By Erick Wendel

  In this article, we''ll get into some powerful tools to help you find and fix bugs
  using VSCode, Docker, and your terminal. We''ll also learn (and put into practice)
  the 6 ways to debug a Node.js application.

  Can you guess what the 6 po...'
---

Par Erick Wendel

Dans cet article, nous allons explorer certains outils puissants pour vous aider à trouver et corriger des bugs en utilisant VSCode, Docker et votre terminal. Nous allons également apprendre (et mettre en pratique) les 6 façons de déboguer une application Node.js.

Pouvez-vous deviner quelles sont les 6 façons possibles de déboguer une application Node.js ? L'une des pratiques les plus courantes dans la vie de chaque développeur consiste à trouver rapidement des bugs et à comprendre ce qui se passe dans leurs applications.

La plupart des exemples présentés ici utiliseront Node.js, mais vous pouvez également les utiliser dans vos applications front-end JavaScript. Vous pouvez utiliser d'autres éditeurs ou IDE tels que Visual Studio ou Web Storm, mais dans cet article, j'utiliserai VSCode. Prenez simplement ce que vous apprenez ici et appliquez-le dans l'éditeur de votre choix.

À la fin de cet article, vous aurez appris à inspecter vos applications en utilisant les outils suivants :

* Boucle Read-Eval-Print (REPL) de Node.js
* Navigateur
* Docker
* VSCode & Environnement local
* VSCode & Docker
* VSCode & Environnement distant

## Prérequis

Dans les étapes suivantes, vous allez créer une API Web en utilisant Node.js et déboguer votre application en utilisant VSCode et Docker. Avant de commencer à coder, assurez-vous d'avoir les outils suivants installés sur votre machine :

* [Docker](https://docs.docker.com/desktop/)
* [Node.js v14](https://nodejs.org/en/download/current/)
* [VSCode](https://code.visualstudio.com/download)

## Introduction

Si vous travaillez comme développeur depuis un certain temps, vous savez peut-être que ce n'est pas comme dans les films. En fait, les développeurs devraient passer 80 % de leur temps à réfléchir et seulement 20 % à écrire du code.

Mais en réalité, la plupart de ces 80 % sont consacrés à la résolution de problèmes, à la correction de bugs et à la tentative de comprendre comment éviter de futurs problèmes. Les vendredis soirs peuvent ressembler au gif ci-dessous :

![développeur codant quand tout va mal](https://media.giphy.com/media/13HgwGsXF0aiGY/giphy.gif)

Quand je réalise que quelque chose d'étrange s'est produit dans mon travail, j'essaie de poser quelques questions, comme vous le verrez dans les sections suivantes.

### Était-ce une erreur de frappe ?

Dans ce cas, le problème pourrait provenir d'une fonction ou d'une variable que j'essaie d'appeler. La console me montrera où se trouve l'erreur et une brève raison possible de l'erreur, comme le montre l'impression ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-05-at-17.32.06.png)
_Image montrant une faute de frappe dans le code en appelant getPhoane au lieu de getPhone._

### Ce comportement devrait-il fonctionner avec l'implémentation actuelle ?

Il pourrait s'agir d'une instruction _if_ qui n'a pas évalué mes conditions ou même d'une _boucle_ qui devrait s'arrêter après certaines interactions mais ne s'arrête pas.

### Que se passe-t-il ici ?

Dans ce cas, il pourrait s'agir d'une erreur interne ou de quelque chose que je n'ai jamais vu auparavant. Je le google donc pour comprendre ce qui s'est passé dans mon application.

Par exemple, l'image ci-dessous montre une erreur interne de flux Node.js qui ne montre pas ce que j'ai fait de mal dans mon programme.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/Screen-Shot-2020-06-05-at-17.31.21-1.png)
_Erreur de flux Node.js avec le message "error: write after end" comme exemple d'erreurs internes._

## Débogage des langages basés sur des scripts

Habituellement, les développeurs de langages basés sur des scripts tels que Ruby, Python ou JavaScript n'ont pas besoin d'utiliser des IDE tels que Visual Studio, WebStorm, etc.

Au lieu de cela, ils optent souvent pour des éditeurs légers tels que Sublime Text, VSCode, VIM, et autres. L'image ci-dessous montre une pratique courante pour inspecter et "déboguer" les applications. Ils impriment des instructions pour vérifier les états et les valeurs de l'application.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/node-console-debug-1.gif)
_La console montrant le programme imprimant des valeurs telles que 'here1', 'here2', etc._

## Pour commencer

La pratique que nous avons vue dans la section précédente n'est pas aussi productive qu'elle pourrait l'être. Nous pouvons confondre des noms de texte avec des valeurs, imprimer des variables incorrectes et perdre du temps sur des bugs simples ou des erreurs de frappe. Mais dans les sections suivantes, je vais vous montrer d'autres façons d'améliorer votre recherche de bugs et de validations d'instructions.

L'objectif principal ici est de montrer à quel point il peut être simple de déboguer une application. En utilisant les outils les plus courants, vous serez en mesure d'inspecter le code à partir de commandes de terminal simples jusqu'à des machines distantes du monde entier.

### Création du projet d'exemple

Avant de plonger dans les concepts de débogage, vous devez créer une application à inspecter. Créez donc une API Web en utilisant le module HTTP natif de Node.js. L'API doit obtenir tous les champs de la requête, additionner toutes les valeurs de celle-ci, puis répondre au demandeur avec les résultats calculés.

Choisissez un dossier vide sur votre machine et commençons avec l'API Web.

Tout d'abord, créez un fichier `Math.js` qui sera responsable de l'addition de tous les champs d'un objet JavaScript :

```javascript
//Math.js
module.exports = {
    sum(...args) {
        return args.reduce(
            (prev, next) => 
                Number(prev) + Number(next), 0
        )
    }
}

```

Deuxièmement, créez un fichier serveur Node.js en utilisant le code ci-dessous. Copiez la valeur et créez votre fichier puis collez-la là. Je vais expliquer ce qui se passe là plus tard.

Remarquez que cette API est une API pilotée par événements et qu'elle gérera les requêtes en utilisant l'approche des flux Node.js.

```javascript
//server.js
const Http = require('http')
const PORT = 3000
const { promisify } = require('util')
const { pipeline } = require('stream')
const pipelineAsync = promisify(pipeline)
const { sum } = require('./Math')

let counter = 0
Http.createServer(async (req, res) => {
    try {
        await pipelineAsync(
            req,
            async function * (source) {
                source.setEncoding('utf8')
                for await (const body of source) {
                    console.log(`[${++counter}] - request!`, body)
                    const item = JSON.parse(body)

                    const result = sum(...Object.values(item))
                    yield `Result: ${result}`
                }
            },
            res
        )
    } catch (error) {
        console.log('Error!!', error)
    }
})
.listen(PORT, () => console.log('server running at', PORT))

```

D'accord, cela peut sembler un code inhabituel pour une API Web simple. Laissez-moi expliquer ce qui se passe.

En alternative, cette API est basée sur les _[Flux Node.js](https://nodejs.org/api/stream.html)_. Vous lirez donc les données à la demande à partir des **requêtes** entrantes, les traiterez et y répondrez en utilisant l'objet **response**.

À la ligne `(11)`, il y a une fonction pipeline qui gérera le flux d'événements. Si quelque chose ne va pas dans une fonction de flux, elle lancera une exception et nous gérerons les erreurs dans l'instruction _catch_ de _try/catch_.

À la ligne `(6)`, nous importons la fonction _sum_ du module _Math_ puis traitons les données entrantes à la ligne `(19)`. Remarquez qu'à la ligne `(19)`, il y a une fonction _Object.values_ qui étendra toutes les valeurs de l'objet et les retournera sous forme de tableau. Par exemple, un objet `{v1: 10, v2: 20}` sera analysé en `[10, 20]`.

### Exécution

Si vous avez un système basé sur Unix, vous pouvez utiliser la commande `cURL`, qui est une commande native pour faire des requêtes Web. Si vous travaillez sur le système d'exploitation Windows, vous pouvez utiliser [Windows Subsystem for Linux](https://docs.microsoft.com/en-us/windows/wsl/install-win10) ou [Git bash](https://git-scm.com/downloads) pour exécuter des instructions Unix.

Créez un fichier `run.sh` avec le code suivant. Vous créerez du code pour demander à votre API. Si vous êtes familier avec [Postman](https://www.postman.com/), vous pouvez sauter ce fichier et exécuter à partir de là.

```shell
curl -i \
    -X POST \
    -d '{"valor1": "120", "valor2": "10"}' \
    http://localhost:3000
```

Notez que vous devez installer Node.js version `14` ou supérieure.

Vous devrez ouvrir deux sessions de terminal. Sur la mienne, j'ai divisé deux terminaux dans mon instance VSCode. À gauche, exécutez `node server.js` et à droite, exécutez `bash run.sh` comme suit :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/02-server.gif)
_Le terminal en cours d'exécution et demandant server.js en utilisant le fichier run.sh._

## Débogage en utilisant la boucle Read-Eval-Print (REPL) de Node.js

Node.js peut vous aider à créer la meilleure application possible. REPL est un mécanisme pour déboguer et inspecter les applications Node.js à partir du terminal. Lorsque vous ajoutez le drapeau `inspect` après la commande `node`, le programme s'arrêtera dès la première ligne de code comme montré ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/03-inspect.gif)
_Utilisation de la commande node inspect pour arrêter le programme avant le démarrage_

Tout d'abord, vous écrirez le mot-clé `debugger` juste après le `console.log` du compteur à la ligne `(17)` puis exécuterez à nouveau `node inspect server.js`.

Notez que vous pouvez interagir avec l'API REPL en utilisant les commandes listées dans la [documentation officielle](https://nodejs.org/api/repl.html#repl_repl).

Dans l'image suivante, vous verrez un exemple pratique de fonctionnement de REPL en utilisant certaines des commandes suivantes :

1. `list(100)` : montre les 100 premières lignes de code
2. `setBreakpoint(17)` : définit un point d'arrêt à la 17ème ligne
3. `clearBreakpoint(17)` : supprime un point d'arrêt à la 17ème ligne
4. `exec body` : évalue la variable `body` et imprime son résultat
5. `cont` : continue l'exécution du programme

L'image ci-dessous montre en pratique comment cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/04-repl.gif)

Je vous recommande vivement d'essayer l'instruction `watch`. Comme dans le navigateur, vous pouvez surveiller les instructions à la demande. Dans votre session REPL, écrivez `watch(counter)` puis `cont`.

Pour tester le watch, vous devez choisir un point d'arrêt – utilisez `setBreakpoint(line)` pour cela. Lorsque vous exécutez `run.sh`, le programme s'arrêtera à votre point d'arrêt et affichera les observateurs. Vous pourrez voir le résultat suivant sur votre console :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/05-repl-watch-2.gif)

## Débogage en utilisant les navigateurs basés sur Chromium

Le débogage dans le navigateur est plus courant que le débogage à partir de sessions de terminal. Au lieu d'arrêter le code à la première ligne, le programme continuera son exécution juste avant son initialisation.

Exécutez `node --inspect server.js` puis allez dans le navigateur. Ouvrez le menu _DevTools_ (en appuyant sur **F12**, vous ouvrez les DevTools sur la plupart des navigateurs). Ensuite, l'icône Node.js apparaîtra. Cliquez dessus. Ensuite, dans la section _Sources_, vous pouvez sélectionner le fichier que vous souhaitez déboguer comme montré dans l'image ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/05-debug-browser-2.gif)

## Débogage dans VSCode

Aller et venir vers le navigateur n'est pas vraiment très amusant tant que vous écrivez du code dans un éditeur. La meilleure expérience est d'exécuter et de déboguer le code au même endroit.

Mais ce n'est pas magique. Vous configurez et spécifiez quel est le fichier principal. Configurons-le en suivant les étapes ci-dessous :

1. Vous devrez ouvrir le fichier `launch.json`. Vous pouvez l'ouvrir en appuyant sur `Ctrl` + `Shift` + `P` ou `Command` + `Shift` + `P` sur macOS, puis en écrivant _launch_. Choisissez l'option _Debug: Open launch.json_. De plus, vous pouvez appuyer sur **F5** et cela pourrait ouvrir le fichier également.
2. Dans l'étape suivante de l'assistant, cliquez sur l'option _Node.js_.
3. Vous avez peut-être vu un fichier JSON dans l'éditeur avec la pré-configuration pour le débogage. Remplissez le champ **program** avec votre nom de fichier – cela indique à VSCode quel est le fichier principal. Remarquez qu'il y a un symbole `${workspaceFolder}`. Je l'ai écrit pour spécifier que le fichier est dans le dossier actuel dans lequel je travaille :

```json
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "launch",
            "name": "Lancer le programme",
            "skipFiles": [
                "<node_internals>/**"
            ],
            "program": "${workspaceFolder}/server.js"
        }
    ]
}
```

Presque terminé ! Allez dans le code source de `server.js` et définissez un point d'arrêt à la 16ème ligne en cliquant sur le côté gauche de l'indicateur de ligne de code. Exécutez-le en appuyant sur **F5** et déclenchez le _server.js_ en utilisant le _run.sh_, ce qui affichera la sortie suivante :

![Image](https://www.freecodecamp.org/news/content/images/2020/06/07-debug-vscode.gif)

## Débogage des applications basées sur Docker

J'adore personnellement utiliser Docker. Cela nous aide à rester aussi proche que possible de l'environnement de production tout en isolant les dépendances dans un fichier de réception.

Si vous souhaitez utiliser Docker, vous devez le configurer dans un fichier de configuration Docker. Copiez le code ci-dessous et créez un nouveau fichier à côté de `server.js` et collez-le.

```dockerfile
FROM node:14-alpine

ADD . .

CMD node --inspect=0.0.0.0 server.js
```

Tout d'abord, vous devrez exécuter la commande de construction _Docker_ dans votre dossier pour construire l'application en exécutant `docker build -t app .`. Ensuite, vous devrez exposer le port de _debug_ (9229) et le port du _serveur_ (3000) afin que le navigateur ou VSCode puisse le surveiller et attacher une instruction de débogage.

```shell
docker run \
    -p 3000:3000 \
    -p 9229:9229 \
    app
```

Si vous exécutez à nouveau le fichier _run.sh_, il devrait demander le serveur qui s'exécute sur Docker.

Le débogage des applications Docker sur VSCode n'est pas une tâche difficile. Vous devez changer la configuration pour attacher un débogueur sur une racine distante. Remplacez votre fichier _launch.json_ par le code ci-dessous :

```json
{
    "configurations": [
        {
            "type": "node",
            "request": "attach",
            "name": "Docker : Attacher à Node",
            "remoteRoot": "${workspaceFolder}",
            "localRoot": "${workspaceFolder}"
        }
    ]
}
```

Tant que votre application s'exécute sur Docker et expose le port de _debug_ par défaut (9229), la configuration ci-dessus liera l'application au répertoire actuel. L'exécution de **F5** et le déclenchement de l'application auront le même résultat que l'exécution en local.

## Débogage de code distant en utilisant VSCode

Le débogage à distance est passionnant ! Vous devez garder à l'esprit quelques concepts avant de commencer à coder :

1. Quelle est l'adresse IP de la cible ?
2. Comment est configuré le répertoire de travail distant ?

Je vais modifier mon fichier _launch.json_ et ajouter l'adresse distante. J'ai un autre PC à la maison qui est connecté au même réseau. Son adresse IP est **192.168.15.12**.

De plus, j'ai le répertoire de travail de la machine Windows ici : _c://Users/Ana/Desktop/remote-vscode/._

Le macOS est basé sur les systèmes Unix, donc la structure des dossiers est différente de celle de ma machine Windows. La cartographie de la structure des répertoires doit changer pour _/Users/Ana/Desktop/remote-vscode/_.

```
{
    "version": "0.2.0",
    "configurations": [
        {
            "type": "node",
            "request": "attach",
            "name": "Attacher au distant",
            "address": "192.168.15.12",
            "port": 9229,
            "localRoot": "${workspaceFolder}",
            "remoteRoot": "/Users/Ana/Desktop/remote-vscode/",
            "trace": true,
            "sourceMaps": true,
            "skipFiles": [
                "<node_internals>/**"
            ]
        }
    ]
}
```

Dans ce cas particulier, vous aurez besoin d'au moins deux machines différentes pour le tester. J'ai fait une courte vidéo montrant comment cela fonctionne en pratique ci-dessous :

<iframe width="560" height="315" src="https://www.youtube.com/embed/s6ggU9grLNo" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Arrêtez d'utiliser console.log pour le débogage !

Mon conseil pour vous aujourd'hui est d'être paresseux pour les choses manuelles. Apprenez un nouveau raccourci ou outil par jour pour améliorer la productivité. Apprenez-en plus sur les outils avec lesquels vous travaillez tous les jours et cela vous aidera à passer plus de temps à réfléchir qu'à coder.

Dans cet article, vous avez vu comment VSCode peut être un outil utile pour déboguer des applications. Et VSCode n'était qu'un exemple. Utilisez ce qui vous convient le mieux. Si vous suivez ces conseils, le ciel est la limite.

## Merci d'avoir lu

J'apprécie vraiment le temps que nous avons passé ensemble. J'espère que ce contenu sera plus que du simple texte. J'espère qu'il vous aura rendu meilleur penseur et aussi meilleur programmeur. Suivez-moi sur [Twitter](https://twitter.com/erickwendel_) et consultez mon [blog personnel](https://erickwendel.com) où je partage tout mon contenu précieux.

À bientôt ! 🚀