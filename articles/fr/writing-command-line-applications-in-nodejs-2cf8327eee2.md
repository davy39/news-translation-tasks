---
title: Écrire des applications en ligne de commande en NodeJS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2015-12-21T01:32:51.000Z'
originalURL: https://freecodecamp.org/news/writing-command-line-applications-in-nodejs-2cf8327eee2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*90gS34fsYQD1Up9L6KHwmw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: Linux
  slug: linux
- name: Node.js
  slug: nodejs
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Écrire des applications en ligne de commande en NodeJS
seo_desc: 'By Peter Benjamin

  With the right packages, writing command-line apps in NodeJS is a breeze.

  One package in particular makes it extremely easy: Commander.

  Let’s set the stage and walk-through how to write a command-line interface (CLI)
  app in NodeJS w...'
---

Par Peter Benjamin

Avec les bons packages, écrire des applications en ligne de commande en NodeJS est un jeu d'enfant.

Un package en particulier rend cela extrêmement facile : [_Commander_](https://www.npmjs.com/package/commander).

Préparons le terrain et parcourons comment écrire une application d'interface en ligne de commande (CLI) en NodeJS avec Commander. Notre objectif sera d'écrire une application CLI pour lister les fichiers et les répertoires.

#### Installation

**IDE**  
J'adore les IDE en ligne. Ils abstraient beaucoup de maux de tête lorsqu'il s'agit de configurer l'environnement de développement. J'utilise personnellement [Cloud9](http://c9.io) pour les raisons suivantes :

* La disposition est intuitive
* L'éditeur est beau et facile à utiliser
* Les ressources du niveau gratuit ont récemment été augmentées à 1 Go de RAM et 5 Go d'espace disque, ce qui est plus que suffisant pour une application NodeJS de taille décente.
* Nombre illimité de postes de travail
* C'est un environnement parfait pour tester ou expérimenter de nouveaux projets/idées sans craindre de casser votre environnement

**Version de Node/NPM**  
Au moment de la rédaction de cet article, Node est à la version 5.3.0 et NPM est à la version 3.3.12.

#### Initialisation

Nous commençons par initialiser notre projet, accepter toutes les valeurs par défaut de NPM et installer le package _commander_ :

```
npm init
npm i --save commander
```

Résultant en :

**Note :**

* Vous devrez ajouter **_bin_** manuellement, ce qui indique à NodeJS le nom de votre application CLI et le point d'entrée de votre application.
* Assurez-vous de ne pas utiliser un nom de commande qui existe déjà dans votre système.

#### Index.js

Maintenant que nous avons initialisé notre projet et indiqué que notre point d'entrée est index.js, créons index.js :

```
touch index.js
```

Maintenant, pour la partie codage proprement dite :

Typiquement, lors de l'exécution de fichiers NodeJS, nous indiquons au système d'utiliser l'interpréteur approprié en préfixant _node_ avant le fichier. Cependant, nous voulons pouvoir exécuter notre application CLI globalement depuis n'importe où dans le système, et sans avoir à spécifier l'interpréteur node à chaque fois.

Par conséquent, notre première ligne est l'expression [shebang](https://en.wikipedia.org/wiki/Shebang_(Unix)) :

```
#!/usr/bin/env node
```

Cela indique non seulement à notre système d'utiliser l'interpréteur approprié, mais aussi d'utiliser la version appropriée de l'interpréteur.

À partir de là, nous écrivons du code JavaScript pur.  
Puisque j'écrirai du code conforme à ES6, je commencerai par l'expression littérale :

```
'use strict';
```

Cela indique au compilateur d'utiliser une variante plus stricte de javascript [[1](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Strict_mode)] et nous permet d'écrire du code ES6 sur Cloud9.

Commençons par requérir le package _commander_ :

```
const program = require('commander');
```

Maintenant, écrire des applications CLI avec _commander_ est simple, et la documentation est excellente, mais j'ai eu du mal avec quelques concepts que je vais essayer de clarifier ici.

Il semble y avoir 2 designs pour les applications CLI. Prenons **_ls_** et **_git_** par exemple.

Avec **_ls_**, vous passez un ou plusieurs flags :

* **_ls -l_**
* **_ls -al_**

Avec **_git_**, vous passez des sous-commandes, mais vous avez aussi quelques flags :

* **_git commit -am <message>_**
* **_git remote add origin <repo-url>_**

Nous allons explorer la flexibilité que _Commander_ nous donne pour concevoir les deux types d'interfaces en ligne de commande.

#### API Commander

L'API _Commander_ est simple et la documentation est excellente.

Il y a 3 façons de base d'écrire notre programme :

**MÉTHODE #1 : Application en ligne de commande avec flags uniquement**

```
const program = require('commander');
```

```
program  .version('0.0.1')  .option('-o, --option','description de l'option')  .option('-m, --more','nous pouvons avoir autant d'options que nous voulons')  .option('-i, --input [optional]','entrée utilisateur optionnelle')  .option('-I, --another-input <required>','entrée utilisateur requise')  .parse(process.argv); // terminez par parse pour analyser l'entrée
```

**Note :**

* Les options en version courte et longue sont dans la même chaîne (voir le texte en gras dans l'image ci-dessus)
* **-o** et **-m** retourneront des valeurs **booléennes** lorsque les utilisateurs les passeront parce que nous n'avons pas spécifié d'entrée utilisateur _optionnelle_ ou _requise_.
* **-i** et **-I** captureront l'entrée utilisateur et passeront les valeurs à notre application CLI.
* Toute valeur enfermée dans des crochets (par exemple [ ]) est considérée comme optionnelle. L'utilisateur peut ou non fournir une valeur.
* Toute valeur enfermée dans des chevrons (par exemple < >) est considérée comme requise. L'utilisateur doit fournir une valeur.

L'exemple ci-dessus nous permet de mettre en œuvre une approche basée uniquement sur les flags pour notre application CLI. Les utilisateurs devront interagir avec notre application comme suit :

```
//Exemples :
$ cli-app -om -I hello
$ cli-app --option -i optionalValue -I requiredValue
```

**MÉTHODE #2 : Application en ligne de commande basée sur des sous-commandes et des flags**

```
const program = require('commander');
```

```
program  .version('0.0.1')  .command('command <req> [optional]')  .description('description de la commande')  .option('-o, --option','nous pouvons encore avoir des options supplémentaires')  .action(function(req,optional){    console.log('.action() nous permet de mettre en œuvre la commande');    console.log('L'utilisateur a passé %s', req);    if (optional) {      optional.forEach(function(opt){        console.log("L'utilisateur a passé des arguments optionnels : %s", opt);      });    }  });
```

```
program.parse(process.argv); // notez que nous devons analyser dans une nouvelle instruction.
```

**Note :**

* Si nous utilisons **.command('command…').description('description…')**, nous devons utiliser **.action()** pour passer une fonction et exécuter notre code en fonction de l'entrée de l'utilisateur. (Je souligne ce point car il existe une méthode alternative pour utiliser **.command()** que nous explorerons ensuite.)
* Si nous utilisons **.command('command…')**, nous ne pouvons plus simplement ajouter **.parse(process.argv)** à la fin comme nous l'avons fait dans l'exemple précédent. Nous devons passer **parse()** dans une nouvelle instruction.

Les utilisateurs sont censés interagir avec notre application CLI comme suit :

```
//Exemple : $ cli-app command requiredValue -o
```

**MÉTHODE #3 : Identique à la MÉTHODE #2 ci-dessus, mais permet un code modulaire**

Enfin, nous n'avons pas à alourdir notre fichier JavaScript avec toute la logique **.command().description().action()**. Nous pouvons modulariser notre projet CLI comme suit :

```
// fichier : ./cli-app/index.js
const program = require('commander');
```

```
program.version('0.0.1').command('command <req> [optional]','description de la commande').command('command2','description de la commande2').command('command3','description de la commande3').parse(process.argv);
```

**Note :**

* Si nous utilisons **.command('command', 'description')** pour passer la commande et la description, nous ne pouvons plus avoir **.action()**. _Commander_ impliquera que nous avons des fichiers séparés avec une convention de nommage spécifique où nous pouvons gérer chaque commande. La convention de nommage est **index-command.js**, **index-command2.js**, **index-command3.js**. [Voir des exemples de cela sur Github](https://github.com/tj/commander.js/tree/master/examples) (spécifiquement : les fichiers **pm**, **pm-install**, **pm-publish**).
* Si nous prenons cette route, nous pouvons simplement ajouter **.parse()** à la fin.

#### Retour à notre scénario de projet…

Maintenant que nous avons couvert les bases, c'est tout en descente à partir d'ici. Nous pouvons prendre une grande respiration.

*** SOUPIR ***

Très bien, maintenant le plaisir commence.

Si nous nous rappelons notre scénario de projet, nous voulons écrire une application CLI pour lister les fichiers et les répertoires. Alors commençons à écrire le code.

Nous voulons donner à l'utilisateur la possibilité de décider s'il veut voir « tous » les fichiers (y compris les fichiers cachés) et/ou s'il veut voir le format de liste long (y compris les droits/permissions des fichiers/dossiers).

Alors, nous commençons par écrire la structure de base de notre programme pour voir notre progression incrémentale (nous suivrons la signature de la **Méthode #2** pour la démonstration) :

```
#!/usr/bin/env node
'use strict';
```

```
const program = require('commander');
```

```
program  .version('')  .command('')  .description('')  .option('','')  .option('','')  .action('');
```

```
program.parse(process.argv);
```

Commençons à remplir les blancs :

```
#!/usr/bin/env node
'use strict';
```

```
const program = require('commander');
```

```
program  .version('0.0.1')  .command('list [directory]')  .description('Lister les fichiers et les dossiers')  .option('-a, --all','Lister tous les fichiers et dossiers')  .option('-l, --long','')  .action();
```

```
program.parse(process.argv);
```

**Note :**

* Nous avons décidé de nommer notre commande **_list_**.
* L'argument **directory** est optionnel, donc l'utilisateur peut simplement ignorer le passage d'un répertoire, auquel cas nous listerons les fichiers/dossiers dans le répertoire courant.

Donc, dans notre scénario, les appels suivants sont valides :

```
$ cli-app list
$ cli-app list -al
$ cli-app list --all
$ cli-app list --long
$ cli-app list /home/user -al
```

Maintenant, commençons à écrire le code pour notre **.action()**.

```
#!/usr/bin/env node
'use strict';
```

```
const program = require('commander');
```

```
let listFunction = (directory,options) => {  //du code ici}
```

```
program  .version('0.0.1')  ...  .action(listFunction);
```

```
program.parse(process.argv);
```

Nous allons tricher ici en utilisant la commande intégrée **_ls_** qui est disponible dans tous les systèmes d'exploitation de type unix.

```
#!/usr/bin/env node
'use strict';
```

```
const program = require('commander'),      exec = require('child_process').exec;
```

```
let listFunction = (directory,options) => {
const cmd = 'ls';
let params = [];
if (options.all) params.push('a');
if (options.long) params.push('l');
let fullCommand = params.length                   ? cmd + ' -' + params.join('')                  : cmd
if (directory) fullCommand += ' ' + directory;
```

```
};
```

```
program  .version('0.0.1')  ...  .action(listFunction);
```

```
program.parse(process.argv);
```

Parlons de la raison de ce code.

1. Tout d'abord, nous requérons la bibliothèque **_child_process_** pour exécuter des commandes shell***** (***_cela ouvre un grand risque de sécurité que je discuterai plus tard_**)
2. Nous déclarons une variable constante qui contient la racine de notre commande
3. Nous déclarons un tableau qui contiendra tous les paramètres passés par l'utilisateur (par exemple **_-a_**, **_-l_**)
4. Nous vérifions si l'utilisateur a passé des flags en version courte (**-a**) ou en version longue (  **all**). Si c'est le cas, alors **options.all** et/ou **options.long** évalueront à **_true_**, auquel cas nous pousserons le flag de commande respectif dans notre tableau. Notre objectif est de construire la commande shell que nous passerons plus tard à **child_process**.
5. Nous déclarons une nouvelle variable pour contenir la commande shell complète. Si le tableau de paramètres contient des flags, nous concaténons les flags les uns aux autres et à la commande racine. Sinon, si le tableau de paramètres est vide, alors nous utilisons la commande racine telle quelle.
6. Enfin, nous vérifions si l'utilisateur a passé des valeurs de **directory** optionnelles. Si c'est le cas, nous les concaténons à la commande entièrement construite.

Maintenant, nous voulons exécuter la commande entièrement construite dans le shell. **Child_Process.exec()** nous donne la possibilité de le faire et [NodeJS docs](https://nodejs.org/api/child_process.html#child_process_child_process_exec_command_options_callback) nous donnent la signature :

```
child_process.exec(command, callback(error, stdout, stderr){
  //"error" sera retourné si exec a rencontré une erreur.
  //"stdout" sera retourné si exec est réussi et que des données sont retournées.
  //"stderr" sera retourné si la commande shell a rencontré une erreur.
})
```

Alors, utilisons cela :

```
#!/usr/bin/env node
'use strict';
```

```
const program = require('commander'),      exec = require('child_process').exec;
```

```
let listFunction = (directory,options) => {
  const cmd = 'ls';
  let params = [];
  if (options.all) params.push('a');
  if (options.long) params.push('l');
  let fullCommand = params.length                   ? cmd + ' -' + params.join('')                  : cmd
  if (directory) fullCommand += ' ' + directory;
```

```
  let execCallback = (error, stdout, stderr) => {
    if (error) console.log("exec error: " + error);
    if (stdout) console.log("Result: " + stdout);
    if (stderr) console.log("shell error: " + stderr);
  };
```

```
  exec(fullCommand, execCallback);
```

```
};
```

```
program  .version('0.0.1')  ...  .action(listFunction);
```

```
program.parse(process.argv);
```

C'est tout !

[Voici le gist de mon application CLI d'exemple](https://gist.github.com/pmbenjamin/3a57f2e0195ae2404c0a#file-index-js).

Bien sûr, nous pouvons ajouter quelques améliorations, comme :

* Colorier la sortie (j'utilise la bibliothèque **_chalk_** ci-dessous)
* Les applications CLI modernes sont assez intelligentes pour afficher le texte d'aide lorsque l'utilisateur appelle le programme sans paramètres ou arguments (comme **_git_**), j'ai donc ajouté cette fonctionnalité tout en bas.

```
#!/usr/bin/env node
'use strict';

/**
 * Require dependencies
 * */
const program = require('commander'),
    chalk = require("chalk"),
    exec = require('child_process').exec,
    pkg = require('./package.json');

/**
 * list function definition
 * */
let list = (directory,options)
  => {
    const cmd = 'ls';
    let params = [];
        if (options.all) params.push("a");
    if (options.long) params.push("l");
    let parameterizedCommand = params.length
                                 ? cmd + ' -' + params.join('')
                                 : cmd ;
    if (directory) parameterizedCommand += ' ' + directory ;
        let output = (error, stdout, stderr) => {
        if (error) console.log(chalk.red.bold.underline("exec error:") + error);
        if (stdout) console.log(chalk.green.bold.underline("Result:") + stdout);
        if (stderr) console.log(chalk.red("Error: ") + stderr);
    };
        exec(parameterizedCommand,output);
    };

program
    .version(pkg.version)
    .command('list [directory]')
    .option('-a, --all', 'List all')
    .option('-l, --long','Long list format')
    .action(list);

program.parse(process.argv);

// if program was called with no arguments, show help.
if (program.args.length === 0) program.help();
```

Enfin, nous pouvons tirer parti de NPM pour créer un lien symbolique de notre application CLI afin de pouvoir l'utiliser globalement dans notre système. Il suffit, dans le terminal, de se déplacer à la racine de notre application CLI et de taper :

```
npm link
```

### Réflexions finales et considérations

Le code de ce projet est loin d'être le meilleur code. Je suis pleinement conscient qu'il y a toujours place à l'amélioration, donc les commentaires sont les bienvenus !

De plus, je veux souligner une faille de sécurité dans notre application. Notre code ne **_nettoie_** pas ou ne **_valide_** pas l'entrée des utilisateurs. Cela viole les meilleures pratiques de sécurité. Considérez les scénarios suivants où les utilisateurs peuvent passer une entrée non désirée :

```
$ cli-app -al ; rm -rf /
$ cli-app -al ; :(){ :|: & };:
```

Si vous voulez écrire du code qui gère ce problème, ou corrige d'autres problèmes potentiels, assurez-vous de nous montrer votre code en laissant un commentaire.