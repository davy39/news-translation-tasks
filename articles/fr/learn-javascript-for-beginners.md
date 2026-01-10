---
title: Apprendre JavaScript pour les débutants - Manuel des bases de JS
subtitle: ''
author: Nathan Sebhastian
co_authors: []
series: null
date: '2023-07-06T19:01:25.000Z'
originalURL: https://freecodecamp.org/news/learn-javascript-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/book-cover.jpg
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Apprendre JavaScript pour les débutants - Manuel des bases de JS
seo_desc: 'The goal of this handbook is to quickly introduce you to the basics of
  JavaScript so you can start programming applications.

  Instead of covering all the theories and concepts of JavaScript, I''ll be teaching
  you only the most important building blocks...'
---

L'objectif de ce manuel est de vous introduire rapidement aux bases de JavaScript afin que vous puissiez commencer à programmer des applications.

Au lieu de couvrir toutes les théories et concepts de JavaScript, je vais vous enseigner uniquement les éléments de base les plus importants du langage. Nous aborderons des sujets tels que les variables, les types de données, les fonctions, les objets, les tableaux et les classes. Vous apprendrez également à les combiner pour construire un petit mais solide programme.

Nous allons également laisser de côté HTML, CSS et l'utilisation de JavaScript dans le navigateur. Ce tutoriel se concentre uniquement sur JavaScript en tant que langage de programmation et utilise le terminal pour exécuter le code.

Ce tutoriel comprend également des exercices pour chaque section, ce qui vous donne le temps de pratiquer ce que vous avez appris et de "mémoriser" les connaissances dans votre cerveau.

Ce manuel est entièrement gratuit ici sur cette page web. Si vous souhaitez la [version Kindle ou brochée de ce tutoriel](https://codewithnathan.com/beginning-modern-javascript), vous pouvez payer un petit montant pour cela. Cela m'aidera à créer un tutoriel JavaScript approfondi qui vous aidera à construire une application web complète.

## Table des matières

* [1 - Introduction à JavaScript](#heading-1-introduction-a-javascript)
    
    * [Pourquoi apprendre JavaScript](#heading-pourquoi-apprendre-javascript)
        
    * [JavaScript vs Java](#heading-javascript-vs-java)
        
* [2 - Comment configurer votre ordinateur](#heading-2-comment-configurer-votre-ordinateur)
    
    * [Comment installer VSCode](#heading-comment-installer-vscode)
        
    * [Comment installer Node.js](#heading-comment-installer-nodejs)
        
* [3 - Introduction rapide à la console](#heading-3-introduction-rapide-a-la-console)
    
* [4 - Il est temps de dire Bonjour le Monde !](#heading-4-il-est-temps-de-dire-bonjour-le-monde)
    
* [5 - Structure du code JavaScript](#heading-5-structure-du-code-javascript)
    
    * [Instructions](#heading-instructions)
        
    * [Commentaires](#heading-commentaires)
        
    * [Flux d'exécution](#heading-flux-dexecution)
        
    * [Exercice #1](#heading-exercice-1)
        
* [6 - Variables JavaScript](#heading-6-variables-javascript)
    
    * [Nom des variables](#heading-nom-des-variables)
        
    * [Variable constante](#heading-variable-constante)
        
    * [Le mot-clé var](#heading-le-mot-cle-var)
        
    * [Exercice #2](#heading-exercice-2)
        
    * [Résumé](#heading-resume)
        
* [7 - Types de données de base en JavaScript](#heading-7-types-de-donnees-de-base-en-javascript)
    
    * [Chaînes de caractères en JavaScript](#heading-chaines-de-caracteres-en-javascript)
        
    * [Nombres (entiers et flottants) en JavaScript](#heading-nombres-entiers-et-flottants-en-javascript)
        
    * [Booléens en JavaScript](#heading-booleens-en-javascript)
        
    * [Indéfini en JavaScript](#heading-indefini-en-javascript)
        
    * [Null en JavaScript](#heading-null-en-javascript)
        
* [8 - Conversion et coercition de type](#heading-8-conversion-et-coercition-de-type)
    
    * [Coercition de type](#heading-coercition-de-type)
        
    * [Règles de coercition de type](#heading-regles-de-coercition-de-type)
        
    * [Pourquoi vous devriez éviter la coercition de type](#heading-pourquoi-vous-devriez-eviter-la-coercition-de-type)
        
* [9 - Opérateurs en JavaScript](#heading-9-operateurs-en-javascript)
    
    * [Opérateurs arithmétiques](#heading-operateurs-arithmetiques)
        
    * [L'opérateur d'affectation](#heading-loperateur-daffectation)
        
    * [Les opérateurs de comparaison](#heading-les-operateurs-de-comparaison)
        
    * [Opérateurs logiques](#heading-operateurs-logiques)
        
    * [L'opérateur typeof](#heading-loperateur-typeof)
        
    * [Exercice #3](#heading-exercice-3)
        
* [10 - Tableaux JavaScript](#heading-10-tableaux-javascript)
    
    * [Position d'index du tableau](#heading-position-dindex-du-tableau)
        
    * [Méthodes spéciales pour la manipulation de tableaux](#heading-methodes-speciales-pour-la-manipulation-de-tableaux)
        
    * [Exercice #4](#heading-exercice-4)
        
* [11 - Flux de contrôle (Conditionnels) en JavaScript](#heading-11-flux-de-controle-conditionnels-en-javascript)
    
    * [L'instruction if...else](#heading-linstruction-ifelse)
        
    * [L'instruction switch...case](#heading-linstruction-switchcase)
        
    * [Le corps de l'instruction switch](#heading-le-corps-de-linstruction-switch)
        
    * [Cas d'utilisation de l'instruction switch](#heading-cas-dutilisation-de-linstruction-switch)
        
    * [Exercice #5](#heading-exercice-5)
        
* [12 - Flux de contrôle (Boucles) en JavaScript](#heading-12-flux-de-controle-boucles-en-javascript)
    
    * [L'instruction for](#heading-linstruction-for)
        
    * [Quand utiliser la boucle for ?](#heading-quand-utiliser-la-boucle-for)
        
    * [L'instruction while](#heading-linstruction-while)
        
    * [Quand utiliser la boucle while ?](#heading-quand-utiliser-la-boucle-while)
        
    * [Exercice #6](#heading-exercice-6)
        
* [13 - Fonctions en JavaScript](#heading-13-fonctions-en-javascript)
    
    * [Comment créer votre propre fonction](#heading-comment-creer-votre-propre-fonction)
        
    * [Paramètres et arguments de fonction](#heading-parametres-et-arguments-de-fonction)
        
    * [Paramètres par défaut](#heading-parametres-par-defaut)
        
    * [Paramètres par défaut et null](#heading-parametres-par-defaut-et-null)
        
    * [L'instruction return](#heading-linstruction-return)
        
    * [Portée des variables](#heading-portee-des-variables)
        
    * [Le paramètre rest](#heading-le-parametre-rest)
        
    * [Fonction fléchée](#heading-fonction-flechee)
        
    * [Fonctions fléchées à une et plusieurs lignes](#heading-fonctions-flechees-a-une-et-plusieurs-lignes)
        
    * [Fonction fléchée sans parenthèses](#heading-fonction-flechee-sans-parentheses)
        
    * [La fonction fléchée n'a pas de liaison d'arguments](#heading-la-fonction-flechee-na-pas-de-liaison-darguments)
        
    * [Comment convertir une fonction normale en une fonction fléchée facilement](#heading-comment-convertir-une-fonction-normale-en-une-fonction-flechee-facilement)
        
    * [Exercice #7](#heading-exercice-7)
        
* [14 - Objets en JavaScript](#heading-14-objets-en-javascript)
    
    * [Comment accéder aux valeurs des objets](#heading-comment-acceder-aux-valeurs-des-objets)
        
    * [Comment ajouter une nouvelle propriété à l'objet](#heading-comment-ajouter-une-nouvelle-propriete-a-lobjet)
        
    * [Comment modifier les propriétés des objets](#heading-comment-modifier-les-proprietes-des-objets)
        
    * [Comment supprimer les propriétés des objets](#heading-comment-supprimer-les-proprietes-des-objets)
        
    * [Comment vérifier si une propriété existe dans un objet](#heading-comment-verifier-si-une-propriete-existe-dans-un-objet)
        
    * [Exercice #8](#heading-exercice-8)
        
* [Exercice final : Construire une machine de caisse enregistreuse](#heading-exercice-final-construire-une-machine-de-caisse-enregistreuse)
    
* [Conclusion](#heading-conclusion)
    
* [Solutions](#heading-solutions)
    

## 1 - Introduction à JavaScript

JavaScript a été créé autour d'avril 1995 par Brendan Eich. À l'époque, il travaillait au développement d'un navigateur pour une entreprise appelée Netscape. On lui a dit qu'il n'avait que 10 jours pour concevoir et coder un prototype fonctionnel d'un langage de programmation qui pouvait s'exécuter sur le navigateur.

Il devait créer un langage qui plaisait aux programmeurs non professionnels comme Microsoft Visual Basic.

La raison pour laquelle il n'avait que 10 jours était que Netscape devait publier son navigateur, qui était à l'époque en compétition avec Microsoft.

Au début, JavaScript n'était pas aussi puissant qu'aujourd'hui, car il était initialement conçu pour ajouter de l'interaction et de l'animation aux pages web. Ce n'est qu'en 2005, lorsque jQuery et AJAX ont été publiés, que JavaScript a commencé à être utilisé dans tous les sites web.

Les gens n'avaient simplement pas d'alternative facile à jQuery et AJAX pour la manipulation du DOM et l'envoi de requêtes asynchrones. De plus, une communauté active de développeurs JavaScript continuait à ajouter de nouvelles fonctionnalités à la bibliothèque.

Ensuite, Google a lancé son navigateur Chrome moderne, et Facebook a commencé à mettre plus de gens en ligne. JavaScript a commencé à croître pour répondre aux ambitions de ces grandes entreprises internet.

Les navigateurs ont commencé à développer des API que vous pouviez utiliser en JavaScript. JS pouvait récupérer des informations telles que les adresses IP et les localisations géographiques à partir du navigateur, ajoutant plus de puissance aux entreprises internet pour localiser les fonctionnalités de leurs sites web.

Puis une autre innovation s'est produite pour rendre JavaScript encore plus puissant.

Un environnement côté serveur nommé Node.js a été publié en 2009, permettant à JavaScript de s'exécuter côté serveur comme PHP, Java, Python, Ruby, et bien d'autres. Il a également permis aux développeurs de développer des applications web full-stack en utilisant uniquement JavaScript.

Aujourd'hui, JavaScript est un langage qui peut alimenter le web, les applications de bureau et mobiles.

Voici une citation de Tim O'Reilly, le fondateur d'O'Reilly Media :

> Apprendre JavaScript signifiait autrefois que vous n'étiez pas un développeur sérieux. Aujourd'hui, ne pas apprendre JavaScript signifie la même chose.

Apprendre JavaScript est maintenant crucial pour les personnes qui veulent devenir développeurs web.

### Pourquoi apprendre JavaScript ?

Il y a 4 bonnes raisons pour lesquelles vous devez apprendre et comprendre profondément JavaScript :

1. JavaScript est le seul langage qui fonctionne dans le navigateur
    
2. Il est relativement facile à apprendre (mais difficile à maîtriser)
    
3. C'est un langage essentiel pour créer des applications web
    
4. Il y a de nombreuses opportunités de carrière pour les développeurs JavaScript
    

Apprendre JavaScript ouvre des opportunités considérables où vous pouvez être développeur frontend, backend ou mobile.

En gros, apprendre JavaScript est une porte d'entrée vers des améliorations de carrière dans la tech.

### JavaScript vs Java

Au début, JavaScript s'appelait en fait LiveScript. Il a été renommé JavaScript parce que Java était un langage de programmation très populaire.

Puisque la plupart des développeurs de logiciels étaient déjà familiers avec Java, le nom JavaScript était censé aider à commercialiser JavaScript comme un excellent langage de programmation et attirer l'intérêt des développeurs de l'époque.

Pour être clair, JavaScript et Java sont deux langages de programmation complètement différents. Vous n'avez pas besoin de connaître Java pour apprendre JavaScript (ou vice versa). :)

## 2 - Comment configurer votre ordinateur

Pour écrire un programme en utilisant JavaScript, vous devez installer 2 outils gratuits disponibles pour tous les systèmes d'exploitation.

Le premier outil à installer est Visual Studio Code.

### Comment installer VSCode

Visual Studio Code ou VSCode en abrégé est un programme éditeur de texte créé dans le but d'écrire du code. En plus d'être gratuit, VSCode est open source et disponible sur tous les principaux systèmes d'exploitation.

Vous pouvez utiliser VSCode sur Windows, macOS et Linux, donc si vous n'avez pas d'éditeur de texte sur votre ordinateur, je vous recommande d'installer VSCode ici.

Maintenant que vous avez un éditeur de texte pour écrire du code JavaScript, vous avez besoin d'un logiciel pour exécuter du code JavaScript. Installons Node.js ensuite.

### Comment installer Node.js

Pour exécuter JavaScript en dehors du navigateur, vous devez installer Node.js, qui est essentiellement un exécuteur JavaScript.

Rendez-vous simplement sur le site web de Node.js à l'adresse nodejs.org et téléchargez la dernière version LTS pour votre ordinateur. Une fois le téléchargement terminé, installez-le sur votre système.

Vous devez exécuter Node.js en utilisant la console, donc ouvrez votre application de ligne de commande ou de terminal et exécutez la commande suivante :

```sh
node -v
```

Cette commande affichera la version de votre Node.js fraîchement installé dans la console.

## 3 - Introduction rapide à la console

La console est une interface basée sur du texte que vous pouvez utiliser pour taper et exécuter des commandes sur votre ordinateur. Sur Windows, elle est appelée la ligne de commande. Sur macOS et Linux, elle est connue sous le nom de Terminal.

Vous n'allez pas utiliser toutes les commandes disponibles dans la console. En fait, vous n'avez besoin de connaître que 7 commandes de base pour vous aider à exécuter du code JavaScript.

Tout d'abord, ouvrez le programme de console sur votre ordinateur et tapez la commande `pwd` :

```sh
pwd
```

C'est la commande que vous utilisez pour savoir dans quel répertoire se trouve votre terminal. `pwd` est l'abréviation de print working directory.

Pour changer le répertoire de travail, vous devez exécuter la commande `cd`.

Voici un exemple pour vous déplacer dans un répertoire enfant :

```sh
cd directory_name/directory_name
```

Pour remonter à un répertoire parent, vous spécifiez `..` à côté de la commande :

```sh
cd ..
```

Pour remonter de plus d'un répertoire, utilisez `../..`

Pour effacer votre console des commandes et sorties précédentes, utilisez la commande `clear` :

```sh
clear
```

Pour imprimer la liste des fichiers et répertoires dans le répertoire courant, exécutez la commande `ls` :

```sh
ls
```

Pour créer un nouveau fichier, utilisez la commande `touch` suivie du nom de fichier et de l'extension :

```sh
touch index.js
```

La commande ci-dessus créera un nouveau fichier JavaScript nommé `index.js` dans le répertoire de travail courant.

Pour créer un nouveau répertoire, utilisez la commande `mkdir` suivie du nom du répertoire :

```sh
mkdir my_project
```

Pour exécuter JavaScript en utilisant Node.js, spécifiez `node` suivi du nom de fichier comme suit :

```sh
node index.js
```

Vous verrez toute sortie du code dans la même console.

Il y a beaucoup de choses que vous pouvez faire avec la console, mais ces 7 commandes suffiront car nous n'en avons besoin que pour exécuter du code JavaScript.

Ensuite, exécutons votre premier programme JavaScript !

## 4 - Il est temps de dire Bonjour le Monde !

Il est temps d'exécuter votre premier programme JavaScript en utilisant Node.

À partir de la console, créez un nouveau fichier JavaScript nommé `index.js` en utilisant la commande `touch`.

```sh
touch index.js
```

Ensuite, ouvrez le fichier en utilisant VSCode et écrivez la ligne de code suivante dans le fichier :

```js
console.log("Bonjour le Monde !");
```

De retour sur la console, exécutez ce script avec Node :

```sh
node index.js
```

La console devrait exécuter le fichier `index.js` et imprimer "Bonjour le Monde !".

Vous venez d'exécuter votre tout premier programme JavaScript en utilisant Node.js. Excellent !

Lorsque vous exécutez la commande `node index.js`, le programme Node.js commence à lire le script ligne par ligne de haut en bas.

Le programme `node` voit que vous avez écrit le mot `console.log` suivi de parenthèses `()`, donc il sait que vous lui donnez l'instruction d'imprimer quelque chose. Le programme lit ensuite ce que vous avez mis dans les parenthèses et l'imprime sur la console.

Dans votre VSCode ou autre programme éditeur de texte, vous devriez voir différentes parties de votre code mises en évidence avec différentes couleurs. Il s'agit d'une fonctionnalité de l'éditeur de texte appelée *coloration syntaxique*, et elle est vraiment utile pour vous aider à distinguer les différentes parties du code.

Le mot-clé `log` est une fonction, donc il est mis en évidence dans une couleur, tandis que les mots dans les parenthèses ont une autre couleur.

Une fonction est simplement un morceau de code utilisé pour effectuer une certaine tâche. La fonction `log()` est utilisée pour "imprimer" ce que vous mettez à l'intérieur des parenthèses.

D'autre part, le mot-clé `console` est un objet, qui est une propriété autonome qui donne accès à certaines fonctionnalités.

Nous en apprendrons plus sur les fonctions et les objets plus tard. Pour l'instant, rappelez-vous simplement que le mot-clé `console.log()` est utilisé pour imprimer des choses sur la console.

Ensuite, commençons par apprendre la structure du code JavaScript.

## 5 - Structure du code JavaScript

Un programme informatique est une série de morceaux de code écrits dans un fichier texte. Ces fichiers texte sont ensuite exécutés par un logiciel spécialement conçu pour exécuter le code. Le logiciel Node.js que vous avez téléchargé précédemment est l'outil qui traite le code JavaScript.

Avant d'aller plus loin, comprenons la structure du code.

### Instructions

Une instruction est une seule instruction que l'ordinateur doit exécuter. Pensez-y comme à une phrase, mais pour les ordinateurs. Nous pouvons terminer une instruction en utilisant un point-virgule `;` tout comme nous pouvons terminer une phrase en utilisant un point `.`

Vous pouvez écrire plusieurs instructions sur une seule ligne, mais la convention est d'écrire une instruction par ligne :

```js
// Cela est difficile à lire
console.log("Bonjour le Monde !"); console.log("J'apprends JavaScript");

// Maintenant c'est mieux
console.log("Bonjour le Monde !");
console.log("J'apprends JavaScript");
```

Chaque instruction est une expression d'une action qui doit être effectuée par le logiciel qui exécute le code.

### Commentaires

En programmation, les commentaires sont du texte que nous utilisons pour communiquer le contexte du code écrit dans le fichier.

Pour écrire un commentaire en JavaScript, vous devez ajouter deux barres obliques `//` avant le commentaire comme montré ci-dessous :

```js
// C'est un commentaire
// C'est aussi un commentaire

// Ci-dessous, imprime deux lignes d'instructions
console.log("Bonjour le Monde !");
console.log("J'apprends JavaScript");
```

Les commentaires sont ignorés par le processeur de langage, donc vous pouvez utiliser les commentaires pour désactiver du code sans avoir à le supprimer.

Le code ci-dessous montre comment désactiver la deuxième instruction d'impression :

```js
console.log("Bonjour le Monde !");
// console.log("J'apprends JavaScript");
```

### Flux d'exécution

Un processeur de langage tel que Node.js exécute les instructions dans une approche de haut en bas. L'instruction écrite dans la première ligne sera exécutée avant la deuxième ligne, puis continuera jusqu'à la dernière ligne :

```js
console.log("Bonjour le Monde !");
console.log("J'apprends JavaScript");

// Impression de nombres
console.log(1);
console.log(2);
console.log(3);
```

**Sortie :**

```txt
Bonjour le Monde !
J'apprends JavaScript
1
2
3
```

Si vous voulez imprimer les nombres avant le texte, alors vous devez déplacer les lignes `console.log()` correspondantes en haut.

### Exercice #1

Essayez d'imprimer votre nom, votre âge et votre profession sur la console.

La sortie devrait ressembler à ce qui suit :

```txt
John Doe
19
Étudiant
```

Maintenant que vous comprenez la structure de base du code JavaScript, continuons avec l'apprentissage des variables ensuite.

## 6 - Variables JavaScript

Avant d'expliquer ce qu'est une variable, je veux que vous modifiiez le code que vous avez écrit dans le fichier `index.js`.

Modifiez le code dans ce fichier comme suit :

```js
let message = "Bonjour le Monde !"
console.log(message)
```

Ensuite, exécutez le code en utilisant la commande `node index.js`. Vous verrez la même sortie que lorsque vous écrivez le message 'Bonjour le Monde !' directement à l'intérieur de la fonction `console.log()`. Comment cela peut-il être ?

C'est parce que le message écrit dans le code ci-dessus est une *variable*.

En programmation, une variable est simplement un nom que vous donnez à une valeur afin que vous puissiez accéder à cette valeur plus tard. Vous pouvez penser à une variable comme une étiquette qui peut être attachée à une certaine valeur, afin que vous puissiez vous référer à la valeur en utilisant l'étiquette.

Pour déclarer une variable, vous devez taper le mot-clé `let` suivi du nom de la variable.

La première ligne du code indique à JavaScript d'associer la variable `message` avec la valeur `Bonjour le Monde !` :

```js
let message = "Bonjour le Monde !"
```

Dans la deuxième ligne, JavaScript est instruit d'imprimer la valeur de `message`, et c'est exactement ce qu'il fait.

Vous pouvez changer la valeur de votre variable en réaffectant une autre valeur comme suit :

```js
message = "Bonjour le Monde !"
console.log(message)
message = "Quel beau temps !"
console.log(message)
```

Exécutez le fichier et vous verrez deux lignes imprimées en sortie :

```txt
Bonjour le Monde !
Quel beau temps !
```

Les variables sont utilisées pour référencer des données afin que vous puissiez utiliser les mêmes données plusieurs fois dans votre programme.

Ensuite, voyons quelques règles pour nommer les variables en JavaScript.

### Nom des variables

JavaScript a quelques règles de nommage que vous devez connaître pour éviter les erreurs de nommage.

Les noms de variables ne peuvent contenir que des lettres de l'alphabet, des chiffres et des traits de soulignement (`_`). Cela signifie que vous pouvez nommer votre variable `message`, `message_1`, `message_2`.

Le premier caractère du nom de la variable ne doit pas être un chiffre. `message_1` est correct. `1_message` ne l'est pas.

Vous ne pouvez pas utiliser de mots-clés réservés tels que `console` car ils sont utilisés par JavaScript pour faire certaines choses. Il y a beaucoup d'autres mots-clés utilisés par JavaScript que vous apprendrez dans les sections suivantes tels que `if`, `for` et `while`.

Les noms de variables sont sensibles à la casse, ce qui signifie que `Message`, `MESSAGE` et `message` peuvent être utilisés pour créer trois variables différentes. Mais bien sûr, je ne recommande pas d'utiliser des noms similaires car cela provoque de la confusion.

Parfois, vous avez besoin de plus d'un mot pour déclarer un nom de variable. JavaScript a deux conventions de nommage qui sont utilisées dans le monde entier :

1. `camelCase`
    
2. `snake_case`
    

La casse camel est une convention de nommage qui utilise une lettre majuscule pour le premier caractère des mots suivants. Voici un exemple :

```js
let myAwesomeVariable
```

La convention de nommage snake case utilise un trait de soulignement pour séparer les mots. Voici un exemple :

```js
let my_awesome_variable
```

Les deux sont des conventions de nommage acceptables, mais vous devriez vous en tenir à l'une d'entre elles dans votre code pour éviter la confusion.

### Variable constante

Il arrive que vous ayez besoin de stocker une valeur qui ne change jamais dans une variable.

Une variable constante est une variable qui ne change pas sa valeur tant que le programme est en cours d'exécution. Dans d'autres langages de programmation, changer la valeur d'une constante produira une erreur.

En JavaScript, une variable constante est déclarée en utilisant le mot-clé `const`.

Ce qui suit montre comment déclarer 2 constantes en JavaScript :

```js
const FILE_SIZE_LIMIT = 2000
const MAX_SPEED = 300
```

La convention de nommage pour une constante est d'utiliser toutes les lettres majuscules, bien que l'utilisation de lettres minuscules fonctionne également. Les majuscules sont simplement une norme pour faire ressortir davantage les constantes.

### Le mot-clé var

Le mot-clé `var` est utilisé pour déclarer des variables avec une portée globale. Ce mot-clé était le seul mot-clé que vous pouviez utiliser pour déclarer des variables avant que JavaScript ne publie les nouveaux mots-clés `let` et `const` en 2015.

À partir d'aujourd'hui, vous devriez éviter d'utiliser `var` si vous le pouvez, puisque `var` peut introduire des bugs que vous pouvez éviter en utilisant le mot-clé `let`.

Pour vous montrer ce que je veux dire, considérons l'exemple suivant :

```js
if(true) {
    var name = "Nathan";
}

console.log(name)
```

Le code ci-dessus imprimera la variable `name` sans problème, mais il ne devrait vraiment pas le faire car la variable `name` est déclarée à l'intérieur du bloc `if`.

C'est parce que toute variable déclarée en utilisant le mot-clé `var` est accessible de partout. La portée de cette variable est globale.

D'autre part, le mot-clé `let` a une portée de bloc, ce qui signifie que la variable n'est accessible que depuis le bloc et tous ses blocs enfants.

Mais pourquoi se soucier de la portée de la variable ? C'est parce que lorsque vous avez des centaines ou des milliers de lignes de code, il peut devenir frustrant de tracer une erreur qui se produit à cause des variables globales.

Il y a un principe en développement logiciel appelé "principes de moindre exposition", ce qui signifie que vous ne devez pas exposer une partie de votre programme qui est inutile.

La portée de bloc d'une variable garantit qu'une variable est exposée et accessible uniquement dans les parties de votre base de code qui nécessitent la variable.

Une variable déclarée en utilisant le mot-clé `let` est identique à une variable déclarée en utilisant `var` à l'exception du niveau de portée.

```js
if(true) {
    let name = "Nathan";
}

console.log(name)  // Erreur : name n'est pas défini
```

Cela signifie également que vous avez maintenant les mots-clés `var`, `let` et `const` pour déclarer une variable. Lequel utiliser ?

En général, vous pouvez déclarer une variable avec `const` en premier. Lorsque vous codez votre application et que vous réalisez que vous devez changer l'affectation de la variable, vous pouvez changer la déclaration en `let`.

Si vous savez dès le départ que la valeur de la variable changera, alors vous pouvez utiliser `let` immédiatement. Ne pas utiliser `var` aujourd'hui ou les gens pourraient se fâcher contre vous.

### Exercice #2

Écrivez un programme avec trois variables, chacune avec la valeur suivante :

1. La première variable contient votre nom
    
2. La deuxième variable contient votre âge
    
3. La troisième variable contient votre profession
    

Ensuite, imprimez les variables en utilisant la méthode `console.log()`. Voici un exemple de sortie :

```txt
John Doe
Étudiant
19
```

### Résumé

La manière dont vous utilisez les variables pour créer un programme qui fait ce que vous voulez qu'il fasse est l'une des compétences les plus importantes que vous pouvez avoir en tant que programmeur.

Mais avant d'en apprendre davantage sur la manière d'utiliser les variables, apprenons les types de données en JavaScript.

## 7 - Types de données de base en JavaScript

Les types de données sont simplement des définitions pour différents types de données connus d'un langage de programmation.

Un type de données contient des spécifications sur ce que vous pouvez et ne pouvez pas faire avec ces données.

Pour vous montrer un exemple facile à comprendre, je suis sûr que vous êtes d'accord avec le fait que `2 + 2 = 4` ?

Eh bien, JavaScript est également d'accord avec cela :

```js
console.log(2 + 2);

// Sortie : 4
```

Mais que se passe-t-il si vous essayez d'ajouter un nombre avec des lettres comme montré ci-dessous ?

```js
console.log(2 + "ABC");
```

**Sortie :**

```txt
2ABC
```

L'ajout d'un nombre et de lettres ensemble amènera JavaScript à concaténer ou joindre les valeurs ensemble.

Dans cette section, vous allez apprendre les types de données de base que JavaScript connaît :

* Chaînes de caractères
    
* Nombres
    
* Booléens
    
* Null
    
* Indéfini
    

Vous verrez également comment ces différents types réagissent aux opérateurs tels que `+` montré dans l'exemple ci-dessus.

Commençons d'abord par les chaînes de caractères.

### Chaînes de caractères en JavaScript

Les chaînes de caractères sont simplement des données définies comme une série de caractères.

Vous avez vu un exemple de données de chaîne de caractères précédemment lorsque vous appelez la fonction `console.log()` pour imprimer un message :

```js
let message = "Bonjour, Soleil !";
console.log(message); // Bonjour, Soleil !
```

Une chaîne de caractères doit être entourée de guillemets. Vous pouvez utiliser des guillemets doubles ou simples, mais ils doivent correspondre.

Vous obtiendrez une erreur lorsque vous utiliserez des marques de guillemets différentes comme ceci :

```js
// Jeton invalide ou inattendu
let message = "Bonjour';
```

Vous pouvez joindre deux chaînes de caractères ou plus en une seule avec le symbole plus `+`. N'oubliez pas d'ajouter un espace avant la chaîne suivante ou vous obtiendrez une chaîne sans espaces !

```js
let message = "Bonjour " + "et " + "Au revoir !";
console.log(message);

// Sortie : Bonjour et Au revoir !
```

Lorsque vous imprimez la valeur d'une variable, vous pouvez également ajouter des chaînes de caractères dans la fonction `console.log()` directement comme suit :

```js
let message = "Bonjour, Dave !";

console.log("Le message est : " + message);

// Sortie : Le message est : Bonjour, Dave !
```

Cela est particulièrement utile lorsque vous avez plusieurs chaînes de caractères à imprimer dans une seule phrase comme suit :

```js
let name = "John";
let topic = "JavaScript";

console.log(name + " apprend " + topic + " aujourd'hui");

// Sortie : John apprend JavaScript aujourd'hui
```

Ou vous pouvez également utiliser le format des chaînes de caractères de modèle, qui vous permet d'intégrer une variable directement à l'intérieur de la chaîne de caractères comme suit :

```js
let name = "John";
let topic = "JavaScript";

console.log(`${name} apprend ${topic} aujourd'hui`);

// Sortie : John apprend JavaScript aujourd'hui
```

Pour utiliser le format des chaînes de caractères de modèle, vous devez utiliser le caractère backtick ``(`)`` pour envelopper la chaîne de caractères au lieu des guillemets.

La variable est intégrée dans la chaîne de caractères en utilisant le symbole dollar et les accolades comme dans `${variable}`.

De cette façon, JavaScript sait que vous référencez une variable à l'intérieur de la chaîne de caractères.

Lorsque vous avez plusieurs chaînes de caractères à imprimer dans une seule ligne, alors le format des chaînes de caractères de modèle est plus pratique car vous n'avez pas eu à rompre la chaîne de caractères avec des guillemets et des concaténations.

Ensuite, les chaînes de caractères peuvent également représenter des nombres. Vous entourez les nombres de guillemets comme suit :

```js
let score = "10" + "30";
console.log(score);

// Sortie : 1030
```

Lorsque vous joignez deux nombres de chaîne de caractères avec un symbole `+`, JavaScript joindra les deux nombres au lieu d'effectuer une addition arithmétique.

C'est ainsi que fonctionnent les chaînes de caractères en JavaScript. Regardons les nombres ensuite.

### Nombres (entiers et flottants) en JavaScript

Les types de données numériques représentent différents types de nombres. Il existe deux types de nombres en JavaScript :

* Entiers
    
* Flottants
    

Un entier est un nombre entier sans décimales ni fractions. Ci-dessous, vous voyez des exemples de deux entiers `x` et `y` :

```js
let x = 1;
let y = 2;

console.log(x + y);

// Sortie : 3
```

D'autre part, les flottants font référence aux nombres avec des points décimaux comme ceci :

```js
let f = 1.2;
let z = 2.35;

console.log(f + z);

// Sortie : 3.55
```

Pour créer un flottant, vous devez écrire un nombre et utiliser `.` pour définir les valeurs décimales.

Avec les types numériques, vous pouvez effectuer des opérations arithmétiques telles que l'addition `+`, la soustraction `-`, la division `/` et la multiplication `*` tout comme vous utilisez une calculatrice.

### Booléens en JavaScript

Le booléen est un type qui représente les valeurs `true` et `false`.

Vous pouvez penser aux booléens comme à un interrupteur qui ne peut être que dans l'une des deux positions : allumé ou éteint.

Il en va de même pour les valeurs booléennes dans les langages de programmation. Elles sont utilisées lorsque JavaScript doit prendre une décision : Aller à gauche ou à droite ? Vrai ou faux ?

Voici comment vous créez des valeurs booléennes en JavaScript :

```js
let on = true;
let off = false;
```

Ce type de données est fréquemment utilisé lorsque vous devez prendre une décision en utilisant un flux de contrôle. Vous verrez pourquoi les valeurs booléennes sont très utiles dans le développement d'un programme plus tard dans la Section 9.

### Indéfini en JavaScript

Indéfini est un type de données en JavaScript utilisé pour représenter une variable à laquelle aucune valeur n'a encore été assignée.

Chaque fois que vous déclarez une variable sans assigner aucune valeur, la valeur `undefined` sera assignée à cette variable. Par exemple :

```js
let first_name;

console.log(first_name); // undefined
```

Vous pouvez également assigner `undefined` à une variable explicitement comme suit :

```js
let last_name = undefined;
```

Mais cela n'est généralement pas recommandé, car JavaScript a une autre valeur appelée `null` qui est utilisée pour marquer une variable comme vide.

### Null en JavaScript

La valeur `null` est un type de données spécial qui représente une valeur vide ou inconnue. Voici comment vous assignez une variable comme null :

```js
let first_name = null;
```

Le code ci-dessus signifie que la valeur de `first_name` est vide ou inconnue.

À ce stade, vous pourriez penser quelle est la différence entre `undefined` et `null` ? Ils semblent servir un but similaire.

Et vous avez raison. `undefined` et `null` sont tous deux des valeurs qui ne représentent rien, et les autres langages de programmation n'ont généralement qu'une seule, et c'est `null`.

En JavaScript, la valeur `undefined` est réservée comme valeur par défaut lorsqu'une variable est déclarée, tandis que `null` signifie que vous avez intentionnellement assigné une valeur "vide" à la variable.

Cette légère différence entrera en jeu plus tard lorsque vous apprendrez les fonctions dans le Chapitre 13.

Pour l'instant, gardez simplement à l'esprit que JavaScript traite `undefined` comme la valeur vide "par défaut" et `null` comme la valeur vide "intentionnelle".

## 8 - Conversion et coercition de type

Parfois, vous pourriez vouloir convertir un type de données en un autre afin que le programme s'exécute comme prévu.

Par exemple, supposons que vous devez convertir une chaîne de caractères en un entier afin de pouvoir effectuer une addition entre des nombres.

Si vous avez l'un des nombres sous forme de chaîne de caractères, JavaScript les joindra au lieu de les additionner :

```js
let x = "7";
let y = 5;

console.log(x + y); // 75
```

Pour additionner les deux nombres correctement, vous devez convertir la variable `x` en un entier.

Changer les données d'un type à un autre est également connu sous le nom de conversion de type ou de transtypage. Il existe 3 fonctions fréquemment utilisées pour effectuer une conversion de type :

* `Number()`
    
* `String()`
    
* `Boolean()`
    

Comme leur nom l'indique, ces fonctions de conversion de type tenteront de convertir toute valeur que vous spécifiez à l'intérieur des parenthèses en le type du même nom.

Pour convertir une chaîne de caractères en un entier, vous pouvez utiliser la fonction `int()` :

```js
let x = "7";
let y = 5;

// Convertir x en entier
x = Number(x);

console.log(x + y); // 12
```

D'autre part, la fonction `String()` convertit une valeur d'un autre type en une chaîne de caractères. Si vous tapez `String(true)`, alors vous obtiendrez 'true' en retour.

Passer une valeur du même type que la fonction n'a aucun effet. Elle renverra simplement la même valeur.

### Coercition de type

En JavaScript, la coercition de type est un processus où une valeur d'un type est implicitement convertie en un autre type.

Cela est automatiquement fait par JavaScript afin que votre code ne provoque pas d'erreur. Mais comme vous le verrez dans cette section, la coercition de type peut en fait causer un comportement indésirable dans le programme.

Considérons ce qui se passe lorsque vous effectuez une addition entre un `number` et une `string` en JavaScript :

```js
console.log(1 + "1");
```

Comme vous l'avez vu dans la section précédente, JavaScript considérera le nombre comme une chaîne de caractères et joindra les deux lettres comme `11` au lieu de les additionner (`1 + 1 = 2`)

Mais vous devez savoir que d'autres langages de programmation ne répondent pas de la même manière.

Des langages de programmation comme Ruby ou Python répondront en arrêtant votre programme et en donnant une erreur comme retour. Il répondra avec quelque chose du genre "Impossible d'effectuer une addition entre un nombre et une chaîne de caractères".

Mais JavaScript verra cela et dira : "Je ne peux pas faire l'opération que vous avez demandée **telle quelle**, mais je peux le faire si le nombre `1` est converti en une `chaîne de caractères`, **donc je vais faire exactement cela**."

Et c'est exactement ce qu'est la coercition de type. JavaScript remarque qu'il ne sait pas comment exécuter votre code, mais il n'arrête pas le programme et ne répond pas avec une erreur.

Au lieu de cela, il changera le type de données de l'une des valeurs sans vous le dire.

Bien que la coercition de type ne cause aucune erreur, la sortie est en fait quelque chose que vous ne voulez pas non plus.

### Règles de coercition de type

Les règles de coercition de type ne sont jamais énoncées clairement nulle part, mais j'ai trouvé quelques règles en essayant divers codes stupides moi-même.

Il semble que JavaScript convertira d'abord les types de données en `string` lorsqu'il trouvera différents types de données :

```js
1 + "1" // "11"
[1 ,2] + "1" // "1,21"
true + "1" // "true1"
```

Mais l'ordre des valeurs compte lorsque vous avez un objet. Écrire des objets en premier retourne toujours le nombre `1` :

```js
{ a: 1 } + "1" // 1
"1" + { a: 1 } // "1[object Object]"
true + { a: 1 } // "true[object Object]"
{ a: 1 } + 1 // 1
```

JavaScript peut calculer entre les types booléens et numériques, car les valeurs booléennes `true` et `false` ont implicitement la valeur numérique de `1` et `0` :

```js
true + 1 // 1+1 = 2
false + 1 // 0+1 = 1
[1,2] + 1 // "1,21"
```

La coercition de type est toujours effectuée **implicitement**. Lorsque vous attribuez la valeur en tant que variable, le type de variable ne changera jamais en dehors de l'opération :

```js
let myNumber = 1;
console.log(myNumber + "1"); // imprime 11
console.log(myNumber); // imprime toujours le nombre 1 et non la chaîne de caractères
```

Vous pouvez essayer d'en trouver d'autres par vous-même, mais vous comprenez maintenant ce qu'est la coercition de type et comment elle fonctionne.

### Pourquoi vous devriez éviter la coercition de type

Les développeurs JavaScript sont généralement divisés en deux camps lorsqu'ils parlent de coercition de type :

* Ceux qui pensent que c'est une fonctionnalité
    
* Ceux qui pensent que c'est un bug
    

Si vous me demandez, je vous recommande d'éviter d'utiliser la coercition de type dans votre code tout le temps.

La raison est que je n'ai jamais trouvé de problème où la coercition de type est nécessaire pour la solution, et lorsque j'ai besoin de convertir un type en un autre, il est toujours préférable de le faire explicitement :

```js
let price = "50";
let tax = 5;

let totalPrice = Number(price) + Number(tax);

console.log(totalPrice);
```

L'utilisation de fonctions de conversion de type explicites telles que `Number()` et `String()` rendra votre code clair et transparent. Vous n'avez pas besoin de deviner le type de données requis dans votre programme.

La coercition de type est l'une des fonctionnalités uniques de JavaScript qui peut confondre les débutants, il est donc bon de la clarifier tôt.

Ensuite, nous apprendrons les opérateurs JavaScript.

## 9 - Opérateurs en JavaScript

Comme leur nom l'indique, les opérateurs sont des symboles que vous pouvez utiliser pour effectuer des opérations sur vos données.

Vous avez vu quelques exemples d'utilisation de l'opérateur plus `+` pour joindre plusieurs chaînes de caractères et additionner deux nombres ensemble. Bien sûr, JavaScript a plus d'un opérateur comme vous le découvrirez dans cette section.

Puisque vous avez appris les types de données et la conversion précédemment, apprendre les opérateurs devrait être relativement facile.

### Opérateurs arithmétiques

Les opérateurs arithmétiques sont utilisés pour effectuer des opérations mathématiques comme les additions et les soustractions.

Ces opérateurs sont fréquemment utilisés avec les types de données numériques. Voici un exemple :

```js
console.log(10 - 3); // 7
console.log(2 + 4); // 6
```

Au total, il y a 8 opérateurs arithmétiques en JavaScript :

| Nom | Exemple d'opération | Signification |
| --- | --- | --- |
| Addition | `x + y` | Retourne la somme entre les deux opérandes |
| Soustraction | `x - y` | Retourne la différence entre les deux opérandes |
| Multiplication | `x * y` | Retourne la multiplication entre les deux opérandes |
| Exponentiation | `x ** y` | Retourne la valeur de l'opérande de gauche élevée à la puissance de l'opérande de droite |
| Division | `x / y` | Retourne la valeur de l'opérande de gauche divisée par l'opérande de droite |
| Reste | `x % y` | Retourne le reste de l'opérande de gauche après avoir été divisé par l'opérande de droite |
| Incrément | `x++` | Retourne l'opérande plus un |
| Décrément | `x--` | Retourne l'opérande moins un |

Ces opérateurs sont assez simples, donc vous pouvez les essayer par vous-même.

Comme vous l'avez vu dans la section précédente, l'opérateur `+` peut également être utilisé sur les données de type chaîne pour fusionner plusieurs chaînes en une seule :

```js
let message = "Bonjour " + "humain !";
console.log(message); // Bonjour humain !
```

Lorsque vous ajoutez un nombre et une chaîne, JavaScript effectuera une coercition de type et traitera la valeur numérique comme une valeur de chaîne :

```js
let sum = "Salut " + 89;
console.log(sum); // Salut 89
```

L'utilisation de tout autre opérateur arithmétique avec des chaînes amènera JavaScript à retourner une valeur `NaN`.

### L'opérateur d'affectation

Le prochain opérateur à apprendre est l'opérateur d'affectation, qui est représenté par le signe égal `=`.

En JavaScript, l'opérateur d'affectation est utilisé pour affecter des données ou une valeur à une variable.

Vous avez vu quelques exemples d'utilisation de l'opérateur d'affectation auparavant, donc voici un rappel :

```js
// Affecter la valeur de chaîne 'Bonjour' à la variable 'message'
let message = "Bonjour";

// Affecter la valeur booléenne true à la variable 'on'
let on = true;
```

Vous avez peut-être remarqué que le signe égal a une signification légèrement différente en programmation que en mathématiques, et vous avez raison !

L'opérateur d'affectation n'est pas utilisé pour comparer si un nombre est égal à un autre nombre en programmation.

Si vous voulez faire ce type de comparaison, alors vous devez utiliser l'opérateur égal à `==`.

Les opérateurs d'affectation peuvent également être combinés avec des opérateurs arithmétiques, afin que vous puissiez ajouter ou soustraire des valeurs de l'opérande de gauche.

Voir le tableau ci-dessous pour les types d'opérateurs d'affectation :

| Nom | Exemple d'opération | Signification |
| --- | --- | --- |
| Affectation | `x = y` | `x = y` |
| Affectation d'addition | `x += y` | `x = x + y` |
| Affectation de soustraction | `x -= y` | `x = x - y` |
| Affectation de multiplication | `x *= y` | `x = x * y` |
| Affectation de division | `x /= y` | `x = x / y` |
| Affectation de reste | `x %= y` | `x = x % y` |

Ensuite, regardons les opérateurs de comparaison.

### Les opérateurs de comparaison

Les opérateurs de comparaison sont utilisés pour comparer deux valeurs. Les opérateurs de cette catégorie retourneront des valeurs booléennes : soit `true` soit `false`.

Le tableau suivant montre tous les opérateurs de comparaison disponibles en JavaScript :

| Nom | Exemple d'opération | Signification |
| --- | --- | --- |
| Égal | `x == y` | Retourne `true` si les opérandes sont égaux |
| Non égal | `x != y` | Retourne `true` si les opérandes ne sont pas égaux |
| Strictement égal | `x === y` | Retourne `true` si les opérandes sont égaux et ont le même type |
| Strictement non égal | `x !== y` | Retourne `true` si les opérandes ne sont pas égaux, ou ont des types différents |
| Supérieur à | `x > y` | Retourne `true` si l'opérande de gauche est supérieur à l'opérande de droite |
| Supérieur ou égal à | `x >= y` | Retourne `true` si l'opérande de gauche est supérieur ou égal à l'opérande de droite |
| Inférieur à | `x < y` | Retourne `true` si l'opérande de gauche est inférieur à l'opérande de droite |
| Inférieur ou égal à | `x <= y` | Retourne `true` si l'opérande de gauche est inférieur ou égal à l'opérande de droite |

Voici quelques exemples d'utilisation de ces opérateurs :

```js
console.log(9 == 9); // true

console.log(9 != 20); // true

console.log(2 > 10); // false

console.log(2 < 10); // true

console.log(5 >= 10); // false

console.log(10 <= 10); // true
```

Les opérateurs de comparaison peuvent également être utilisés pour comparer des chaînes de caractères comme ceci :

```js
console.log("ABC" == "ABC"); // true

console.log("ABC" == "abc"); // false

console.log("Z" == "A"); // false
```

Les comparaisons de chaînes de caractères sont sensibles à la casse, comme le montre l'exemple ci-dessus.

JavaScript a également deux versions de chaque opérateur de comparaison : lâche et stricte.

En mode strict, JavaScript comparera les types sans effectuer de coercition de type.

Vous devez ajouter un symbole égal `=` supplémentaire à l'opérateur comme suit

```js
console.log("9" == 9); // true
console.log("9" === 9); // false

console.log(true == 1); // true
console.log(true === 1); // false
```

Vous devriez utiliser les opérateurs de comparaison stricts sauf si vous avez une raison spécifique de ne pas le faire.

### Opérateurs logiques

Les opérateurs logiques sont utilisés pour vérifier si une ou plusieurs expressions résultent en `True` ou `False`.

Il y a trois opérateurs logiques que JavaScript possède :

| Nom | Exemple d'opération | Signification | | ----------- | ----------------- | --------------------------------------------------------------- | --- | ---------------------------------------------------------------------- | | Logique ET | `x && y` | Retourne `true` si tous les opérandes sont `true`, sinon retourne `false` | | Logique OU | `x || y` | Retourne `true` si l'un des opérandes est `true`, sinon retourne `false` | | Logique NON | `!x` | Inverse le résultat : retourne `true` si `false` et vice versa |

Ces opérateurs ne peuvent retourner que des valeurs booléennes. Par exemple, vous pouvez déterminer si '7 est supérieur à 2' et '5 est supérieur à 4' :

```js
console.log(7 > 2 && 5 > 4); // true
```

Ces opérateurs logiques suivent les lois de la logique mathématique :

1. `&&` Opérateur ET - si une expression retourne `false`, le résultat est `false`
    
2. `||` Opérateur OU - si une expression retourne `true`, le résultat est `true`
    
3. `!` Opérateur NON - nie l'expression, retourne l'inverse.
    

Faisons un petit exercice. Essayez d'exécuter ces instructions sur votre ordinateur. Pouvez-vous deviner les résultats ?

```js
console.log(true && false);

console.log(false || false);

console.log(!true);
```

Ces opérateurs logiques seront utiles lorsque vous devrez affirmer qu'une exigence spécifique est remplie dans votre code.

### L'opérateur `typeof`

JavaScript vous permet de vérifier le type de données en utilisant l'opérateur `typeof`. Pour utiliser l'opérateur, vous devez l'appeler avant de spécifier les données :

```js
let x = 5;
console.log(typeof x) //  'number'

console.log(typeof "Nathan") // 'string'

console.log(typeof true) // 'boolean'
```

L'opérateur `typeof` retourne le type des données sous forme de chaîne de caractères. Le type 'number' représente à la fois les types entier et flottant, les types string et boolean représentent leurs types respectifs.

### Exercice #3

Devinez le résultat de ces opérateurs en action :

```js
console.log(19 % 3);
console.log(10 == 3);
console.log(10 !== "10");
console.log(2 < "10");
console.log("5" > 2);
console.log((false && true) || false);
```

## 10 - Tableaux JavaScript

Un tableau est un type de données objet qui peut être utilisé pour contenir plus d'une valeur. Un tableau peut être une liste de chaînes de caractères, de nombres, de booléens, d'objets, ou un mélange de tout cela.

Pour créer un tableau, vous devez utiliser les crochets `[]` et séparer les éléments en utilisant une virgule.

Voici comment créer une liste de chaînes de caractères :

```js
let birds = ['Hibou', 'Aigle', 'Perroquet', 'Faucon'];
```

Vous pouvez penser à un tableau comme une liste d'éléments, chacun stocké dans un compartiment de casier :

![Array as a locker illustration](https://www.freecodecamp.org/news/content/images/2023/07/10-array-as-a-locker-1.png align="left")

Vous pouvez également déclarer un tableau vide sans aucune valeur :

```js
let birds = [];
```

Un tableau peut également avoir un mélange de valeurs comme ceci :

```js
let mixedArray = ['Oiseau', true, 10, 5.17]
```

Le tableau ci-dessus contient une chaîne de caractères, un booléen, un entier et un flottant.

### Position d'index du tableau

JavaScript se souvient de la position des éléments dans un tableau. La position d'un élément est également appelée numéro d'index.

En revenant à l'exemple du casier, vous pouvez penser aux numéros d'index comme aux numéros de casier. Le numéro d'index commence à `0` comme suit :

![Array index numbers as locker numbers](https://www.freecodecamp.org/news/content/images/2023/07/10-array-index-analogy.png align="left")

Pour accéder ou changer la valeur d'un tableau, vous devez ajouter la notation des crochets `[x]` à côté du nom du tableau, où `x` est le numéro d'index de cet élément. Voici un exemple :

```js
// Accéder au premier élément du tableau
myArray[0];

// Accéder au deuxième élément du tableau
myArray[1];
```

Supposons que vous voulez imprimer la chaîne 'Hibou' du tableau `birds`. Voici comment vous pouvez le faire.

```js
let birds = ['Hibou', 'Aigle', 'Perroquet', 'Faucon'];

console.log(birds[0]); // Hibou
console.log(birds[1]); // Aigle
```

Voilà. Vous devez taper le nom du tableau, suivi du numéro d'index entouré de crochets.

Vous pouvez également assigner une nouvelle valeur à un index spécifique en utilisant l'opérateur d'affectation.

Remplaçons 'Perroquet' par 'Vautour' :

```js
let birds = ['Hibou', 'Aigle', 'Perroquet', 'Faucon'];
birds[2] = 'Vautour';

console.log(birds);
// ['Hibou', 'Aigle', 'Vautour', 'Faucon']
```

Parce que l'index du tableau commence à zéro, la valeur 'Perroquet' est stockée à l'index 2 et non 3.

### Méthodes spéciales pour la manipulation de tableaux

Puisque le tableau est un objet, vous pouvez appeler des méthodes qui sont fournies par JavaScript pour manipuler les valeurs du tableau.

Par exemple, vous pouvez utiliser la méthode `push()` pour ajouter un élément à la fin du tableau :

```js
let birds = ['Hibou', 'Aigle'];

birds.push('Moineau');

console.log(birds);
// ['Hibou', 'Aigle', 'Moineau']
```

Une autre méthode appelée `pop()` peut être utilisée pour supprimer un élément de la fin d'un tableau :

```js
let birds = ['Hibou', 'Aigle', 'Moineau'];

birds.pop();

console.log(birds);
// ['Hibou', 'Aigle']
```

La méthode `unshift()` peut être utilisée pour ajouter un élément à l'avant à l'index 0 :

```js
let fishes = ['Saumon', 'Poisson rouge', 'Thon'];

fishes.unshift('Sardine');

console.log(fishes);
// ['Sardine', 'Saumon', 'Poisson rouge', 'Thon']
```

D'autre part, la méthode `shift()` peut être utilisée pour supprimer un élément de l'index 0 :

```js
let fishes = ['Saumon', 'Poisson rouge', 'Thon'];

fishes.shift();

console.log(fishes);
// ['Poisson rouge', 'Thon']
```

La méthode `indexOf()` peut être utilisée pour trouver et retourner l'index d'un élément dans le tableau.

La méthode retournera `-1` lorsque l'élément n'est pas trouvé à l'intérieur du tableau :

```js
let fishes = ['Saumon', 'Poisson rouge', 'Thon'];

let pos = fishes.indexOf('Thon');

console.log(pos); // 2
```

Pour obtenir la taille d'un tableau, vous pouvez accéder à la propriété `length` :

```js
let fishes = ['Saumon', 'Poisson rouge', 'Thon'];

console.log(fishes.length); // 3
```

Notez que nous n'ajoutons pas de parenthèses à côté du mot-clé `length` ci-dessus. C'est parce que `length` est une propriété de l'objet tableau et non une méthode.

Nous en apprendrons plus sur les objets dans les tutoriels à venir.

### Exercice #4

Créez un tableau nommé `colors` qui inclut les couleurs 'red', 'green, et 'blue'.

Tout d'abord, ajoutez une couleur 'black' après le dernier index du tableau. Ensuite, imprimez le tableau.

Ensuite, supprimez la valeur 'red' et échangez la position de 'green' et 'blue'. Imprimez le tableau.

Enfin, ajoutez la couleur 'yellow' au premier index du tableau, puis imprimez le tableau.

Le résultat de la sortie est le suivant :

```txt
[ 'red', 'green', 'blue', 'black' ]
[ 'blue', 'green', 'black' ]
[ 'yellow', 'blue', 'green', 'black' ]
```

Vous devez modifier le tableau original en utilisant les méthodes expliquées dans cette section.

## 11 - Flux de contrôle (Conditionnels) en JavaScript

Jusqu'à présent, le code JavaScript que vous avez écrit est exécuté ligne par ligne de haut en bas. Mais que se passe-t-il si vous voulez exécuter certaines lignes de code uniquement lorsqu'une certaine condition est remplie ?

Un programme informatique a généralement besoin de prendre en compte de nombreuses conditions différentes qui peuvent survenir pendant l'exécution du programme.

Cela est similaire à la façon dont un humain prend des décisions dans sa vie. Par exemple, avez-vous assez d'argent pour couvrir les vacances au Japon ? Si oui, allez-y. Si non, alors économisez plus d'argent !

C'est là que le flux de contrôle intervient. **Le flux de contrôle** est une fonctionnalité dans un langage de programmation qui vous permet d'exécuter sélectivement un code spécifique en fonction des différentes conditions qui peuvent survenir.

L'utilisation de flux de contrôle vous permet de définir plusieurs chemins qu'un programme peut prendre en fonction des conditions présentes dans votre programme.

Il existe deux types de flux de contrôle couramment utilisés en JavaScript : les conditionnels et les boucles.

Cette section se concentrera sur les instructions conditionnelles telles que :

1. L'instruction `if...else`
    
2. L'instruction `switch...case`
    

Vous apprendrez les instructions de boucle dans la section suivante.

### L'instruction if...else

L'instruction `if` vous permet de créer un programme qui ne s'exécute que si une condition spécifique est remplie.

La syntaxe de l'instruction `if` est la suivante :

```js
if (condition) {
  // code à exécuter si la condition est vraie
}
```

Prenons un exemple. Supposons que vous voulez partir en vacances qui nécessitent 5000 dollars.

En utilisant l'instruction `if`, voici comment vous vérifiez si vous avez assez d'argent :

```js
let balance = 7000;

if (balance > 5000) {
  console.log("Vous avez l'argent pour ce voyage. Partons !");
}
```

Exécutez le code ci-dessus une fois, et vous verrez la chaîne de caractères imprimée sur le terminal.

Maintenant, changez la valeur de `balance` en `3000` et vous n'obtiendrez aucune réponse.

Cela se produit parce que le code à l'intérieur de l'instruction `if` n'est exécuté que lorsque la condition est `true`.

Après l'instruction `if`, vous pouvez écrire une autre ligne de code en dessous comme suit :

```js
let balance = 7000;

if (balance > 5000) {
  console.log("Vous avez l'argent pour ce voyage. Partons !");
}
console.log("La fin !");
```

Le deuxième appel `console.log()` ci-dessus sera exécuté quelle que soit la valeur que vous attribuez à la variable `balance`.

Si vous voulez qu'il s'exécute uniquement lorsque la condition `if` est remplie, alors mettez la ligne à l'intérieur des accolades également :

```js
let balance = 7000;

if (balance > 5000) {
  console.log("Vous avez l'argent pour ce voyage. Partons !");
  console.log("La fin !");
}
```

Ensuite, supposons que vous devez exécuter un code uniquement lorsque la condition de l'instruction `if` n'est pas remplie.

C'est là que l'instruction `else` intervient. L'instruction `else` est utilisée pour exécuter un code uniquement lorsque l'instruction `if` n'est pas remplie.

Voici un exemple :

```js
let balance = 7000;

if (balance > 5000) {
  console.log("Vous avez l'argent pour ce voyage. Partons !");
} else {
  console.log("Désolé, pas assez d'argent. Économisez plus !");
}
console.log("La fin !");
```

Maintenant, changez la valeur de `balance` pour qu'elle soit inférieure à `5000`, et vous déclencherez le bloc `else` dans l'exemple.

JavaScript dispose également de l'instruction `else if` qui vous permet d'écrire une autre condition à vérifier si la condition de l'instruction `if` n'est pas remplie.

Considérez l'exemple ci-dessous :

```js
let balance = 7000;

if (balance > 5000) {
  console.log("Vous avez l'argent pour ce voyage. Partons !");
} else if (balance > 3000) {
  console.log("Vous n'avez assez d'argent que pour une staycation");
} else {
  console.log("Désolé, pas assez d'argent. Économisez plus !");
}
console.log("La fin !");
```

Lorsque le montant `balance` est inférieur à `5000`, l'instruction `else if` vérifiera si le `balance` est supérieur à `3000`. Si c'est le cas, alors le programme recommandera de faire une staycation.

Vous pouvez écrire autant d'instructions `else if` que vous le souhaitez, et chacune d'entre elles ne sera exécutée que si l'instruction précédente n'est pas remplie.

Ensemble, les instructions `if..else..else if` vous permettent d'exécuter différents blocs de code en fonction de la condition à laquelle le programme est confronté.

### L'instruction switch...case

L'instruction `switch` fait partie de la syntaxe de base de JavaScript qui vous permet de contrôler le flux d'exécution de votre code.

Elle est souvent considérée comme une alternative à l'instruction `if..else` qui vous donne un code plus lisible, surtout lorsque vous avez de nombreuses conditions différentes à évaluer.

Voici un exemple d'une instruction `switch` fonctionnelle. Je vais expliquer le code ci-dessous :

```js
let age = 15;
switch (age) {
  case 10:
    console.log("L'âge est 10");
    break;
  case 20:
    console.log("L'âge est 20");
    break;
  default:
    console.log("L'âge n'est ni 10 ni 20");
}
```

Tout d'abord, vous devez passer une expression à évaluer par l'instruction `switch` entre les parenthèses. Dans l'exemple, la variable `age` est passée comme argument pour l'évaluation.

Ensuite, vous devez écrire les valeurs `case` que l'instruction `switch` essaiera de faire correspondre avec votre expression. La valeur `case` est immédiatement suivie d'un deux-points (`:`) pour marquer le début du bloc de cas :

```js
case "apple":
```

Gardez à l'esprit le type de données de la valeur `case` que vous voulez faire correspondre avec l'expression. Si vous voulez faire correspondre une `string`, alors vous devez mettre une `string`. Les instructions `switch` **ne effectueront pas de coercition de type** lorsque vous avez un `number` comme argument mais mettez une `string` pour le cas :

```js
switch (1) {
  case "1":
    console.log("Bonjour le Monde !");
    break;
}
```

L'expression numérique ne correspond pas à la valeur de cas de la chaîne, donc JavaScript ne journalisera rien dans la console.

Il en va de même pour les valeurs booléennes. Le nombre `1` ne sera pas coercé en `true` et le nombre `0` ne sera pas coercé en `false` :

```js
switch (0) {
  case true:
    console.log("Bonjour Vrai !");
    break;
  case false:
    console.log("Bonjour Faux !");
    break;
  default:
    console.log("Aucun cas correspondant");
}
```

### Le corps de l'instruction switch

Le corps de l'instruction `switch` est composé de trois mots-clés :

* Le mot-clé `case` pour démarrer un bloc de cas
    
* Le mot-clé `break` pour empêcher l'instruction `switch` d'exécuter le `case` suivant
    
* Le mot-clé `default` pour exécuter un morceau de code lorsqu'aucun `case` correspondant n'est trouvé.
    

Lorsque votre expression trouve un `case` correspondant, JavaScript exécutera le code suivant l'instruction `case` jusqu'à ce qu'il trouve le mot-clé `break`. Si vous omettez le mot-clé `break`, alors l'exécution du code continuera vers le bloc suivant.

Jetez un coup d'œil à l'exemple suivant :

```js
switch (0) {
  case 1:
    console.log("La valeur est un");
  case 0:
    console.log("La valeur est zéro");
  default:
    console.log("Aucun cas correspondant");
}
```

Lorsque vous exécutez le code ci-dessus, JavaScript imprimera le journal suivant :

```shell
> "La valeur est zéro"
> "Aucun cas correspondant"
```

C'est parce que sans le mot-clé `break`, `switch` continuera à évaluer l'expression par rapport aux cas restants même lorsqu'un cas correspondant est déjà trouvé.

Votre évaluation de switch peut correspondre à plus d'un cas, donc le mot-clé `break` est couramment utilisé pour quitter le processus une fois qu'une correspondance est trouvée.

Enfin, vous pouvez également mettre des expressions comme valeurs de `case` :

```js
switch (20) {
  case 10 + 10:
    console.log("la valeur est vingt");
    break;
}
```

Mais vous devez garder à l'esprit que la valeur pour un bloc `case` **doit correspondre exactement** à l'argument `switch`.

L'une des erreurs les plus courantes lors de l'utilisation de l'instruction `switch` est que les gens pensent que la valeur `case` est évaluée comme `true` ou `false`.

Les blocs `case` suivants ne fonctionneront pas dans les instructions `switch` :

```js
let age = 5;

switch (age) {
  case age < 10:
    console.log("La valeur est inférieure à dix");
    break;
  case age < 20:
    console.log("La valeur est inférieure à vingt");
    break;
  default:
    console.log("La valeur est vingt ou plus");
}
```

Vous devez vous rappeler les différences entre les évaluations `if` et `case` :

* Le bloc `if` sera exécuté lorsque la condition de test **est évaluée à** `true`
    
* Le bloc `case` sera exécuté lorsque la condition de test **correspond exactement** à l'argument `switch` donné
    

### Cas d'utilisation de l'instruction switch

La règle générale lorsque vous considérez entre `if` et `switch` est la suivante :

> Vous n'utilisez `switch` que lorsque le code est fastidieux à écrire en utilisant `if`

Par exemple, disons que vous voulez écrire un nom de jour de la semaine basé sur le numéro du jour de la semaine

Voici comment vous pouvez l'écrire :

```js
let weekdayNumber = 1;

if (weekdayNumber === 0) {
  console.log("Dimanche");
} else if (weekdayNumber === 1) {
  console.log("Lundi");
} else if (weekdayNumber === 2) {
  console.log("Mardi");
} else if (weekdayNumber === 3) {
  console.log("Mercredi");
} else if (weekdayNumber === 4) {
  console.log("Jeudi");
} else if (weekdayNumber === 5) {
  console.log("Vendredi");
} else if (weekdayNumber === 6) {
  console.log("Samedi");
} else {
  console.log("Le numéro du jour de la semaine est invalide");
}
```

Je ne sais pas pour vous, mais le code ci-dessus semble fastidieux pour moi ! Bien qu'il n'y ait rien de mal avec le code ci-dessus, vous pouvez le rendre plus joli avec `switch` :

```js
let weekdayNumber = 1;

switch (weekdayNumber) {
  case 0:
    console.log("Dimanche");
    break;
  case 1:
    console.log("Lundi");
    break;
  case 2:
    console.log("Mardi");
    break;
  case 3:
    console.log("Mercredi");
    break;
  case 4:
    console.log("Jeudi");
    break;
  case 5:
    console.log("Vendredi");
    break;
  case 6:
    console.log("Samedi");
    break;
  default:
    console.log("Le numéro du jour de la semaine est invalide");
}
```

Lorsque vous avez beaucoup de conditions à évaluer pour le même bloc, vous combinerez probablement plusieurs conditions `if` en utilisant l'opérateur logique **ET (**`&&`) ou **OU (**`||`) :

```js
let myFood = "Banane";

if (myFood === "Banane" || myFood === "Pomme") {
  console.log("Mangez des fruits tous les jours pour rester en bonne santé.");
}

if (myFood === "Gâteau au chocolat") {
  console.log("Profitez de la douceur.");
}
```

Vous pouvez remplacer le code ci-dessus en utilisant l'instruction switch. La clé est que vous devez empiler plusieurs `cases` comme un seul comme ceci :

```js
let myFood = "Banane";

switch (myFood) {
  case "Banane":
  case "Pomme":
    console.log("Mangez des fruits tous les jours pour rester en bonne santé.");
    break;
  case "Gâteau au chocolat":
    console.log("Profitez de la douceur.");
    break;
}
```

Malheureusement, `switch` ne peut pas remplacer plusieurs conditions `if` qui utilisent l'opérateur `&&` à cause de la manière dont l'évaluation `case` fonctionne. Vous devez utiliser l'instruction `if` pour cela.

### Exercice #5

Une école primaire donne différentes récompenses en fonction de la note de l'élève :

* Les élèves qui ont obtenu un A recevront un Chocolat
    
* Les élèves qui ont obtenu un B recevront un Cookie
    
* Les élèves qui ont obtenu un C recevront un Bonbon
    
* Pour toute autre valeur, imprimez "Pas de récompense à donner."
    

Créez une variable nommée `grade` qui stockera la note de l'élève.

Exemple de sortie :

```txt
Vous avez obtenu un A, alors voici un Chocolat pour vous !
Vous avez obtenu un B, voici un Cookie pour vous !
Vous avez obtenu un C, il y a de la place pour l'amélioration et voici votre Bonbon !
```

Vous pouvez utiliser soit l'instruction `if...else` soit l'instruction `switch...case`.

## 12 - Flux de contrôle (Boucles) en JavaScript

Lorsque vous programmez une application en JavaScript, vous devrez souvent écrire un morceau de code qui doit être exécuté plusieurs fois.

Disons que vous voulez écrire un programme qui imprime les nombres de 1 à 10 dans la console. Vous pouvez le faire en appelant `console.log` 10 fois comme ceci :

```js
console.log(1);
console.log(2);
console.log(3);
console.log(4);
console.log(5);

// et ainsi de suite..
```

Cela fonctionne, mais il y a une meilleure façon d'écrire ce type de tâche répétitive.

Une **instruction de boucle** est une autre catégorie d'instruction de flux de contrôle utilisée pour exécuter un bloc de code plusieurs fois jusqu'à ce qu'une certaine condition soit remplie.

Il existe deux instructions de boucle utilisées en JavaScript :

* L'instruction `for`
    
* L'instruction `while`
    

Apprenons comment utiliser ces instructions en pratique.

### L'instruction for

Au lieu de vous répéter 10 fois pour imprimer les nombres de 1 à 10, vous pouvez utiliser l'instruction `for` et écrire une seule ligne de code comme suit :

```js
for (let x = 0; x < 10; x++) {
  console.log(x);
}
```

Voilà ! L'instruction `for` est suivie de parenthèses (`()`) qui contiennent 3 expressions :

* L'expression `initialization`, où vous déclarez une variable à utiliser comme source de la condition de la boucle. Représentée par `x = 1` dans l'exemple.
    
* L'expression `condition`, où la variable dans l'initialisation sera évaluée pour une condition spécifique. Représentée par `x < 11` dans l'exemple.
    
* L'expression `arithmetic`, où la valeur de la variable est soit incrémentée soit décrémentée à la fin de chaque boucle.
    

Ces expressions sont séparées par un point-virgule (`;`)

Après les expressions, les accolades (`{}`) seront utilisées pour créer un bloc de code qui sera exécuté par JavaScript tant que l'expression `condition` retourne `true`.

Vous pouvez identifier quelle expression est laquelle en prêtant attention au point-virgule (`;`) qui termine l'instruction.

```js
for ( [initialization]; [condition]; [arithmetic expression]) {
  // Tant que la condition retourne true,
  // Ce bloc sera exécuté de manière répétée
}
```

L'expression arithmétique peut être une expression d'incrément (`++`) ou de décrément (`--`). Elle est exécutée une fois à chaque fois que l'exécution du code à l'intérieur des accolades se termine :

```js
for (let x = 10; x >= 1; x--) {
  console.log(x);
}
```

Ou vous pouvez également utiliser des opérateurs arithmétiques abrégés comme `+=` et `-=` comme montré ci-dessous :

```js
// instruction for avec expression arithmétique abrégée
for (let x = 1; x < 20; x += 3) {
  console.log(x);
}
```

Ici, x sera incrémenté de 3 à chaque fois que la boucle est exécutée.

Une fois la boucle terminée, JavaScript continuera à exécuter tout code que vous écrivez en dessous du corps de la boucle `for` :

```js
for (let x = 1; x < 2; x++) {
  console.log(x);
}
console.log("La boucle for est terminée");
console.log("Continuer l'exécution du code");
```

### Quand utiliser une boucle for

La boucle for est utile **lorsque vous savez combien de fois** vous devez exécuter une tâche répétitive.

Par exemple, disons que vous écrivez un programme pour lancer une pièce de monnaie. Vous devez trouver combien de fois la pièce atterrit sur pile lorsqu'elle est lancée 10 fois. Vous pouvez le faire en utilisant la méthode `Math.random` :

* Lorsque le nombre est inférieur à `0,5`, vous devez incrémenter le compteur `tails`
    
* Lorsque le nombre est `0,5` et plus, vous devez incrémenter le compteur `heads`
    

```js
let heads = 0;
let tails = 0;
for (x = 1; x <= 10; x++) {
  if (Math.random() < 0.5) {
    tails++;
  } else {
    heads++;
  }
}

console.log("La pièce a été lancée dix fois");
console.log(`Nombre de piles : ${heads}`);
console.log(`Nombre de faces : ${tails}`);
```

L'exemple ci-dessus montre où la boucle `for` offre l'approche la plus efficace.

Maintenant, voyons un exercice alternatif sur les lancers de pièces où la boucle `for` n'est pas efficace :

***Découvrez combien de fois vous devez lancer une pièce jusqu'à ce qu'elle atterrisse sur pile.***

Cette fois, vous ne savez pas **combien de fois** vous devez lancer la pièce. C'est là que vous devez utiliser l'instruction de boucle `while`, que vous allez apprendre ensuite.

### L'instruction while

L'instruction `while` ou la boucle `while` est utilisée pour exécuter un bloc de code tant que la condition est évaluée à `true`.

Vous pouvez définir la condition et l'instruction pour la boucle comme suit :

```js
while (condition) {
  statement;
}
```

Tout comme la boucle `for`, la boucle `while` est utilisée pour exécuter un morceau de code encore et encore jusqu'à ce qu'il atteigne la condition souhaitée.

Dans l'exemple ci-dessous, nous continuerons à exécuter le bloc *statement* jusqu'à ce que l'expression *condition* retourne `false` :

```js
let i = 0;

while (i < 6) {
  console.log(`La valeur de i = ${i}`);
  i++;
}
```

Ici, la boucle `while` imprimera de manière répétée la valeur de `i` tant que `i` est inférieur à `6`. À chaque itération, la valeur de `i` est incrémentée de 1 jusqu'à ce qu'elle atteigne 6 et que la boucle se termine.

Gardez à l'esprit que vous devez inclure un morceau de code qui finit par rendre la condition d'évaluation à `false` ou la boucle `while` sera exécutée pour toujours. L'exemple ci-dessous provoquera une boucle infinie :

```js
let i = 0;

while (i < 6) {
  console.log(`La valeur de i = ${i}`);
}
```

Parce que la valeur de `i` ne change jamais, la boucle while continuera indéfiniment !

### Quand utiliser une boucle while

Voyant que `while` et `for` peuvent tous deux être utilisés pour exécuter un morceau de code de manière répétée, quand devriez-vous utiliser une boucle `while` au lieu de `for` ?

Un moyen facile de savoir quand vous devriez utiliser `while` est lorsque **vous ne savez pas combien de fois** vous devez exécuter le code.

Revenons à l'exemple du lancer de pièce, il y a un cas qui est parfait pour une boucle `while` :

***Découvrez combien de fois vous devez lancer une pièce jusqu'à ce qu'elle atterrisse sur pile.***

Vous devez également **montrer combien de fois** vous lancez la pièce jusqu'à ce qu'elle atterrisse sur pile :

```js
let flips = 0;
let isHeads = false;

while (!isHeads) {
  flips++;
  isHeads = Math.random() < 0.5;
}

console.log(`Il a fallu ${flips} lancers pour atterrir sur pile.`);
```

Ici, la condition `isHead = Math.random() < 0.5` simule le lancer d'une pièce équitable. Lorsque le résultat est `true`, cela signifie que la pièce est tombée sur pile et que la boucle se terminera.

Parce que vous ne pouvez pas savoir combien de fois vous devez lancer la pièce jusqu'à obtenir pile, vous devez utiliser une boucle `while` au lieu d'une boucle `for`.

### Exercice #6

Écrivez un programme qui imprime une demi-pyramide en utilisant des astérisques `*` comme montré ci-dessous :

```txt
*
**
***
****
*****
```

Ensuite, imprimez une demi-pyramide inversée comme suit :

```txt
*****
****
***
**
*
```

## 13 - Fonctions en JavaScript

Une fonction est simplement une section (ou un bloc) de code écrite pour effectuer une tâche spécifique.

Par exemple, la fonction de transtypage `String()` est utilisée pour convertir des données d'un autre type en une chaîne de caractères.

Les méthodes `console.log()` et diverses méthodes de tableau que nous avons apprises dans les chapitres précédents sont également des fonctions. Mais parce que ces fonctions sont appelées à partir d'un objet, elles sont appelées méthodes.

Vous en apprendrez plus sur les méthodes plus tard dans le Chapitre 14. Pour l'instant, sachez simplement qu'une fonction et une méthode sont essentiellement les mêmes, sauf qu'une méthode est appelée à partir d'un objet.

En plus des fonctions intégrées fournies par JavaScript, vous pouvez également créer votre propre fonction.

### Comment créer votre propre fonction

La création d'une fonction commence par taper le mot-clé `function` suivi du nom de la fonction, d'une paire de parenthèses, puis d'une paire d'accolades.

Voici un exemple :

```js
function greet() {
  // corps de la fonction ici
  console.log("Bonjour !");
}
```

Pour appeler une fonction, vous devez spécifier le nom de la fonction suivi de parenthèses :

```js
greet(); // Bonjour !
```

Le code à l'intérieur de la fonction est exécuté lorsque vous appelez cette fonction.

### Paramètres et arguments de fonction

Les paramètres sont des variables utilisées pour accepter les entrées données lorsque la fonction est appelée.

Vous pouvez spécifier des paramètres dans l'en-tête de la fonction, à l'intérieur des parenthèses.

L'exemple suivant montre une fonction qui a un paramètre appelé `name` :

```js
function greet(name) {
  // corps de la fonction
}
```

La manière dont vous utilisez ce paramètre `name` à l'intérieur de la fonction dépend de vous.

Vous pouvez utiliser le paramètre à l'intérieur de la fonction `print()` comme suit :

```js
function greet(name) {
  console.log(`Bonjour, ${name} !`);
  console.log("Beau temps aujourd'hui, n'est-ce pas ?");
}
```

Maintenant, chaque fois que vous devez appeler la fonction `greet()`, vous devez passer une entrée pour remplir le paramètre `name`.

L'entrée que vous passez pour remplir un paramètre est appelée un argument, et voici comment le faire :

```js
greet("Peter");
```

La chaîne 'Peter' à l'intérieur des parenthèses lors de l'appel de la fonction `greet()` sera passée comme paramètre `name`.

Exécutez le code pour recevoir cette sortie :

```txt
Bonjour, Peter !
Beau temps aujourd'hui, n'est-ce pas ?
```

Vous pouvez avoir plus d'un paramètre lors de la définition de la fonction, mais vous devez séparer chaque paramètre par une virgule comme suit :

```js
function greet(name, weather) {
  console.log(`Bonjour, ${name} !`);
  console.log(`Il fait ${weather} aujourd'hui, n'est-ce pas ?`);
}

greet("Nathan", "pluvieux");
```

**Sortie :**

```txt
Bonjour, Nathan !
Il fait pluvieux aujourd'hui, n'est-ce pas ?
```

Lorsque vous spécifiez deux paramètres dans l'en-tête de la fonction, vous devez passer deux arguments. Si vous appelez la fonction sans passer les arguments, la valeur sera `undefined`.

Dans la section suivante, vous apprendrez à créer des paramètres avec des valeurs par défaut, ce qui vous permet d'appeler la fonction sans avoir à passer un argument.

Mais pour l'instant, j'espère que vous voyez la commodité d'avoir des paramètres. Ils rendent vos fonctions plus adaptables et réutilisables en prenant différentes valeurs d'entrée pour couvrir une variété de scénarios que la fonction pourrait avoir.

Comme montré dans l'exemple, les paramètres `name` et `weather` vous permettent de saluer de nombreuses personnes différentes dans différents temps.

Qu'il fasse ensoleillé, pluvieux ou nuageux, changez simplement les arguments `name` et `weather` lorsque vous voulez saluer une autre personne.

### Paramètres par défaut

Lors de la définition d'une fonction, vous pouvez définir une valeur par défaut pour tout paramètre de cette fonction.

Par exemple, le paramètre `name` dans la fonction ci-dessous est un paramètre par défaut :

```js
function greet(name = "Nathan") {
  console.log(`Bonjour, ${name} !`);
  console.log("Beau temps aujourd'hui, n'est-ce pas ?");
}
```

Ici, la valeur par défaut 'Nathan' sera utilisée lorsqu'aucune valeur ou `undefined` n'est passée pour le paramètre `name`.

Vous pouvez tester cela en appelant la fonction `greet()` sans argument comme suit :

```js
greet();
greet("Jack");
```

**Sortie :**

```txt
Bonjour, Nathan !
Beau temps aujourd'hui, n'est-ce pas ?

Bonjour, Jack !
Beau temps aujourd'hui, n'est-ce pas ?
```

Toute fonction que vous définissez peut avoir un mélange de paramètres par défaut et non par défaut.

Voici un autre exemple de fonction qui a un paramètre par défaut appelé `name` et un paramètre non par défaut appelé `weather` :

```js
function greet(weather, name = "Nathan") {
  console.log(`Bonjour, ${name} !`);
  console.log(`Il fait ${weather} aujourd'hui, n'est-ce pas ?`);
}

greet("sunny");
```

**Sortie :**

```txt
Bonjour, Nathan !
Il fait ensoleillé aujourd'hui, n'est-ce pas ?
```

Remarquez que le paramètre `weather` a été placé devant le paramètre `name`. Cela est pour la commodité afin que vous n'ayez pas besoin de spécifier le paramètre par défaut.

Si vous placez le paramètre non par défaut après le paramètre par défaut, alors vous devez passer une valeur au paramètre `name` pour accéder au paramètre `weather`.

Considérez l'exemple ci-dessous :

```js
function greet(name = "Nathan", weather) {
  console.log(`Bonjour, ${name} !`);
  console.log(`Il fait ${weather} aujourd'hui, n'est-ce pas ?`);
}

greet(undefined, "sunny");
```

Pour passer un argument au paramètre `weather`, nous devons passer `undefined` ou une valeur quelconque pour le paramètre `name` en premier.

C'est pourquoi il est préférable de spécifier les paramètres non par défaut devant les paramètres par défaut.

### Paramètres par défaut et null

Dans le Chapitre 7, rappelez-vous que nous avons brièvement exploré la différence entre `undefined` comme valeur vide "par défaut" et `null` comme valeur vide "intentionnelle".

Lorsque vous passez `undefined` à une fonction qui a un paramètre par défaut, le paramètre par défaut sera utilisé :

```js
function greet(name = "John"){
  console.log(name);
}

greet(undefined); // John
```

Comme vous pouvez le voir, JavaScript imprime la valeur du paramètre par défaut `John` lorsque vous passez `undefined` à la fonction.

Mais lorsque vous passez `null` à la fonction, le paramètre par défaut sera ignoré :

```js
function greet(name = "John"){
  console.log(name);
}

greet(null); // null
```

C'est l'une des erreurs courantes que font les débutants lorsqu'ils apprennent JavaScript. Lorsque vous utilisez la valeur `null`, JavaScript pensera que vous voulez que cette valeur soit vide, donc il ne remplace pas la valeur par le paramètre par défaut.

Lorsque vous utilisez `undefined`, alors JavaScript le remplacera par le paramètre par défaut. Vous pourriez rencontrer ce problème lorsque vous travaillez avec du code JavaScript dans votre carrière, alors gardez cela à l'esprit.

### L'instruction return

Une fonction peut également avoir une instruction `return` à l'intérieur du bloc de code. Une instruction `return` est utilisée pour retourner une valeur à l'appelant.

Par exemple, la fonction suivante retourne la somme de deux valeurs :

```js
function sum(a, b) {
  return a + b;
}

let result = sum(3, 2);
console.log(result); // 5
```

La valeur retournée par une fonction peut être assignée à une variable pour une opération ultérieure. Vous pouvez ajouter l'instruction `return` n'importe où à l'intérieur de la fonction.

Lorsque JavaScript atteint l'instruction `return`, il saute le code supplémentaire écrit à l'intérieur du bloc de fonction et revient à l'endroit où vous appelez la fonction.

La fonction suivante a deux instructions `return` :

```js
function checkAge(age) {
  if (age > 18) {
    return "Vous pouvez obtenir un permis de conduire";
  }
  return "Vous ne pouvez pas encore obtenir un permis de conduire";
}

console.log(checkAge(20));
console.log(checkAge(15));
```

**Sortie :**

```txt
Vous pouvez obtenir un permis de conduire
Vous ne pouvez pas encore obtenir un permis de conduire
```

Lorsque nous appelons la fonction `checkAge()` la première fois, la valeur de l'argument `age` est supérieure à 18, donc JavaScript exécute l'instruction `return` à l'intérieur du bloc `if`.

La deuxième fois que nous avons appelé la fonction, la condition `if` n'est pas remplie, donc JavaScript exécute l'instruction `return` sous le bloc `if` à la place.

Vous pouvez également arrêter l'exécution d'une fonction et revenir à l'appelant en spécifiant l'instruction `return` sans aucune valeur :

```js
function greet() {
  console.log("Bonjour !");
  return;
  console.log("Au revoir !");
}

greet()
```

Sortie :

```txt
Bonjour !
```

Ici, l'instruction `return` est appelée entre les appels `console.log()`.

JavaScript exécute le premier appel `console.log()`, puis saute le reste du code. La chaîne 'Au revoir !' n'est pas imprimée.

### Portée des variables

Maintenant que vous apprenez les fonctions, c'est un bon moment pour parler de la portée des variables.

Une variable déclarée à l'intérieur d'une fonction ne peut être accessible que depuis cette fonction. Cela est dû au fait que cette variable a une portée locale.

D'autre part, une variable déclarée en dehors de tout bloc est connue comme une variable globale en raison de sa portée globale.

Ces deux portées sont importantes car lorsque vous essayez d'accéder à une variable locale en dehors de sa portée, vous obtiendrez une erreur. Par exemple :

```js
function greet() {
  let myString = "Bonjour le Monde !";
}

greet();
console.log(myString);
```

Lorsque vous exécutez le code ci-dessus, JavaScript répond avec une erreur :

```txt
ReferenceError : myString n'est pas défini
```

C'est parce que la variable `myString` est déclarée à l'intérieur de la fonction `greet()`, donc vous ne pouvez pas accéder à cette variable en dehors de celle-ci. Cela n'a pas d'importance même si vous avez appelé cette fonction avant d'accéder à la variable.

Pendant ce temps, une variable globale peut être accessible de n'importe où, même à l'intérieur d'une fonction :

```js
let myString = "Bonjour le Monde !";

function greet() {
  console.log(myString);
}

greet(); // Bonjour le Monde !
```

Ici, la fonction `greet()` est capable d'accéder à la variable `myString` déclarée en dehors de celle-ci.

Gardez à l'esprit que cela s'applique uniquement aux variables déclarées en utilisant `let` et `const`.

Ensuite, vous pouvez également définir une variable locale avec le même nom que la variable globale sans l'écraser.

Voici un exemple :

```js
let myString = "Bonjour le Monde !";

function greet() {
  let myString = "Bonjour !";
  console.log(myString);
}

greet();  // Bonjour !
console.log(myString); // Bonjour le Monde !
```

Lorsque vous appelez la fonction `greet()`, une variable locale appelée `myString` a été assignée à la chaîne 'Bonjour !'.

En dehors de la fonction, la variable globale qui s'appelle également `myString` existe toujours, et la valeur n'est pas changée.

JavaScript considère la variable de portée locale comme une variable différente. Lorsque vous déclarez la même variable à l'intérieur d'une fonction, tout code à l'intérieur de la fonction fera toujours référence à la variable locale.

En pratique, vous avez rarement besoin de déclarer la même variable dans différentes portées :

1. Toute variable déclarée en dehors d'une fonction ne devrait pas être utilisée à l'intérieur d'une fonction sans les passer en tant que paramètres.
    
2. Une variable déclarée à l'intérieur d'une fonction ne devrait jamais être référencée en dehors de cette fonction
    

Gardez cela à l'esprit lorsque vous écrivez des fonctions JavaScript.

### Le paramètre rest

Le paramètre rest est un paramètre qui peut accepter n'importe quel nombre de données comme arguments. Les arguments seront stockés sous forme de tableau.

Vous pouvez définir un paramètre rest dans l'en-tête de la fonction en ajoutant trois points `...` avant le nom du paramètre.

Voici un exemple de création d'une fonction qui a un argument de longueur variable :

```js
function printArguments(...args){
    console.log(args);
}
```

Lorsque vous appelez la fonction `printArguments()` ci-dessus, vous pouvez spécifier autant d'arguments que vous le souhaitez :

```js
function printArguments(...args){
    console.log(args);
}

printArguments("A", "B", "C"); 
// [ 'A', 'B', 'C' ]
printArguments(1, 2, 3, 4, 5);
// [ 1, 2, 3, 4, 5 ]
```

Gardez à l'esprit qu'une fonction ne peut avoir qu'un seul paramètre rest, et que le paramètre rest doit être le dernier paramètre de la fonction.

Vous pouvez utiliser un paramètre rest lorsque votre fonction doit fonctionner avec un nombre indéfini d'arguments.

### Fonction fléchée

La **syntaxe des fonctions fléchées JavaScript** vous permet d'écrire une fonction JavaScript avec une syntaxe plus courte et plus concise.

Lorsque vous devez créer une fonction en JavaScript, la méthode principale consiste à utiliser le mot-clé `function` suivi du nom de la fonction comme montré ci-dessous :

```js
function greetings(name) {
  console.log(`Bonjour, ${name} !`);
}

greetings("John"); // Bonjour, John !
```

La syntaxe des fonctions fléchées vous permet de créer une expression de fonction qui produit le même résultat que le code ci-dessus.

Voici la fonction `greetings()` utilisant la syntaxe fléchée :

```js
const greetings = (name) => {
  console.log(`Bonjour, ${name} !`);
};

greetings("John"); // Bonjour, John !
```

Lorsque vous créez une fonction en utilisant la syntaxe des fonctions fléchées, vous devez assigner l'expression à une variable afin que la fonction ait un nom.

En gros, la syntaxe des fonctions fléchées est la suivante :

```js
const fun = (param1, param2, ...) => {
  // corps de la fonction
}
```

Dans le code ci-dessus,

* `fun` est la variable qui contient la fonction. Vous pouvez appeler la fonction comme `fun()` plus tard dans votre code.
    
* `(param1, param2, ...)` sont les paramètres de la fonction. Vous pouvez définir autant de paramètres que nécessaire pour la fonction.
    
* Ensuite, vous avez la flèche `=>` pour indiquer le début de la fonction.
    

Le code ci-dessus est égal au suivant :

```js
const fun = function(param1, param2, ...) {
  // corps de la fonction
}
```

La syntaxe des fonctions fléchées n'ajoute aucune nouvelle capacité au langage JavaScript.

Au lieu de cela, elle offre des améliorations à la manière dont vous écrivez une fonction en JavaScript.

Au début, cela peut sembler étrange car vous êtes habitué au mot-clé `function`.

Mais à mesure que vous commencez à utiliser la syntaxe fléchée, vous verrez qu'elle est très pratique et plus facile à écrire.

### Fonctions fléchées à une et plusieurs lignes

La fonction fléchée vous fournit un moyen d'écrire une fonction sur une seule ligne où le côté gauche de la flèche `=>` est retourné au côté droit.

Lorsque vous utilisez le mot-clé `function`, vous devez utiliser les accolades `{}` et le mot-clé `return` comme suit :

```js
function plusTwo(num) {
  return num + 2;
}
```

En utilisant la fonction fléchée, vous pouvez omettre à la fois les accolades et le mot-clé `return`, créant une fonction sur une seule ligne comme montré ci-dessous :

```js
const plusTwo = (num) => num + 2;
```

Sans les accolades, JavaScript évaluera l'expression du côté droit de la syntaxe fléchée et la retournera à l'appelant.

La syntaxe des fonctions fléchées fonctionne également pour une fonction qui ne `retourne` pas de valeur comme montré ci-dessous :

```js
const greetings = () => console.log("Bonjour le Monde !");
```

Lorsque vous utilisez la syntaxe des fonctions fléchées, les accolades sont requises uniquement lorsque vous avez un corps de fonction sur plusieurs lignes :

```js
const greetings = () => {
  console.log("Bonjour le Monde !");
  console.log("Comment allez-vous ?");
};
```

### Fonction fléchée sans parenthèses

Les parenthèses `()` sont utilisées dans les fonctions JavaScript pour indiquer les paramètres que la fonction peut recevoir.

Lorsque vous utilisez le mot-clé `function`, les parenthèses sont toujours requises :

```js
function plusThree(num) {
  return num + 3;
}
```

D'autre part, la fonction fléchée vous permet d'omettre les parenthèses lorsque vous avez **exactement un paramètre** pour la fonction :

L'exemple de code suivant est une expression de fonction fléchée valide :

```js
const plusThree = num => num + 3;
```

Comme vous pouvez le voir, vous pouvez supprimer les parenthèses et les accolades ainsi que le mot-clé `return`.

Mais vous avez toujours besoin des parenthèses pour deux conditions :

* Lorsque la fonction n'a pas de paramètre
    
* Lorsque la fonction a plus d'un paramètre
    

Lorsque vous n'avez pas de paramètre, alors vous avez besoin de parenthèses avant la flèche comme montré ci-dessous :

```js
const greetings = () => console.log("Bonjour le Monde !");
```

Il en va de même lorsque vous avez plus d'un paramètre.

La fonction ci-dessous a deux paramètres : `name` et `age`.

```js
const greetings = (name, age) => console.log("Bonjour le Monde !");
```

La syntaxe fléchée rend les parenthèses facultatives lorsque vous avez une fonction à paramètre unique.

### La fonction fléchée n'a pas de liaison d'arguments

Lorsque vous utilisez le mot-clé `function` pour définir une fonction, vous pouvez accéder aux arguments que vous passez à la fonction en utilisant le mot-clé `arguments` comme ceci :

```js
const printArgs = function () {
  console.log(arguments);
};

printArgs(1, 2, 3);
// [Arguments] { '0': 1, '1': 2, '2': 3 }
```

Le mot-clé `arguments` dans le code ci-dessus fait référence à l'objet qui stocke tous les arguments que vous avez passés dans la fonction.

En revanche, la fonction fléchée n'a pas l'objet `arguments` et lèvera une erreur lorsque vous essayez d'y accéder :

```js
const printArgs = () => console.log(arguments);

printArgs(1, 2, 3);
//Uncaught ReferenceError : arguments n'est pas défini
```

Vous pouvez utiliser la syntaxe de propagation JavaScript pour imiter la liaison `arguments` comme suit :

```js
const printArgs = (...arguments) => console.log(arguments);

printArgs(1, 2, 3);
// [1, 2, 3]
```

En utilisant la syntaxe de propagation, les arguments que vous passez à la fonction fléchée seront stockés dans un tableau.

**Notez** que vous avez besoin des parenthèses même si vous ne passez qu'un seul argument à la fonction.

Vous pouvez accéder aux `arguments` donnés avec la notation d'index de tableau comme `arguments[0]`, `arguments[1]`, et ainsi de suite.

### Comment convertir une fonction normale en une fonction fléchée facilement

Vous pouvez suivre les **trois étapes faciles** ci-dessous pour convertir une fonction normale en une fonction fléchée :

1. Remplacez le mot-clé `function` par le mot-clé de variable `let` ou `const`
    
2. Ajoutez le symbole `=` après le nom de la fonction et avant les parenthèses
    
3. Ajoutez le symbole `=>` après les parenthèses
    

Le code ci-dessous vous aidera à visualiser les étapes :

```js
function plusTwo(num) {
  return num + 2;
}

// étape 1 : remplacer function par let / const
const plusTwo(num) {
  return num + 2;
}

// étape 2 : ajouter = après le nom de la fonction
const plusTwo = (num) {
  return num + 2;
}

// étape 3 : ajouter => après les parenthèses
const plusTwo = (num) => {
  return num + 2;
}
```

Les trois étapes ci-dessus suffisent pour convertir toute ancienne syntaxe de fonction JavaScript en la nouvelle syntaxe de fonction fléchée.

Lorsque vous avez une fonction sur une seule ligne, il y a une quatrième étape facultative pour supprimer les accolades et le mot-clé `return` comme suit :

```js
// de ceci
const plusTwo = num => {
  return num + 2;
};

// à ceci
const plusTwo = num => num + 2;
```

Lorsque vous avez exactement un paramètre, vous pouvez également supprimer les parenthèses :

```js
// de ceci
const plusTwo = (num) => num + 2;

// à ceci
const plusTwo = num => num + 2;
```

Mais les deux dernières étapes sont facultatives. Seules les trois premières étapes sont requises pour convertir toute fonction JavaScript `function` et utiliser la syntaxe de fonction fléchée.

### Exercice #7

Écrivez une fonction nommée `calculateSquare()` qui est utilisée pour calculer l'aire et le périmètre d'une forme carrée.

La fonction accepte un paramètre : le `côté` du carré.

La formule pour calculer l'aire est `côté * côté`, et la formule pour calculer le périmètre est `4 * côté`.

La sortie montre la taille du côté, l'aire et le périmètre comme suit :

```txt
Le côté du carré est 8
L'aire du carré est 64
Le périmètre du carré est 32
```

## 14 - Objets en JavaScript

Un objet est un type de données spécial qui vous permet de stocker plus d'une valeur, tout comme un tableau.

La différence entre un objet et un tableau est qu'un tableau stocke les données sous forme de liste d'éléments, tandis qu'un objet stocke les données dans un format de paire `clé:valeur`.

Voyons un exemple illustrant cette différence. Supposons que vous voulez stocker des informations sur un livre dans votre programme.

Lorsque vous utilisez des variables régulières, cela ressemblerait à ceci :

```js
let bookTitle = "Introduction à JavaScript";
let bookAuthor = "Nathan Sebhastian";
```

Bien que cela fonctionne bien, ce n'est certainement pas la meilleure façon de stocker des valeurs liées.

Une autre façon de stocker la valeur serait d'utiliser un tableau :

```js
let myBook = ["Introduction à JavaScript", "Nathan Sebhastian"];
```

Cela est certainement mieux car vous pouvez regrouper les données liées au livre ensemble, mais vous n'avez aucun moyen d'ajouter du contexte à la valeur.

C'est là qu'un objet est utile. Vous pouvez déclarer un seul objet livre et stocker les données au format `clé:valeur` :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};
```

Un objet est déclaré en utilisant les accolades `{}`, et chaque élément à l'intérieur des accolades est écrit au format `clé:valeur`.

Un élément d'objet est également connu sous le nom de propriété, avec la *clé* comme nom de propriété et *valeur* comme valeur de propriété.

Comme un tableau, vous devez séparer chaque élément à l'intérieur d'un objet en utilisant une virgule.

Vous pouvez assigner une chaîne de caractères ou des nombres comme clé d'un élément, et vous pouvez assigner n'importe quel type de données comme valeur, y compris une fonction :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
  describe: function () {
    console.log(`Titre du livre : ${this.title}`);
    console.log(`Auteur du livre : ${this.author}`);
  },
};
```

Ici, la clé ou propriété `describe` est une fonction qui imprime les valeurs `title` et `author` de l'objet.

Le mot-clé `this` fait référence au contexte du code, qui est l'objet `myBook` dans ce cas.

Habituellement, une clé d'objet est quelque chose qui donne plus de contexte à la valeur qu'elle contient. Une clé doit également être unique, donc vous ne pouvez pas utiliser la même clé deux fois dans le même objet.

Par exemple, si vous avez des données sur un livre, vous pouvez utiliser des clés d'objet telles que `title`, `author` et `price` pour vous aider à comprendre le contexte de la valeur stockée dans chaque clé.

### Comment accéder aux valeurs des objets

Pour accéder à la valeur d'un objet, vous pouvez utiliser soit la notation par point `.` soit la notation par crochets `[]`.

Voici un exemple d'utilisation de la notation par point pour accéder aux propriétés de l'objet :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};

console.log(myBook.title);
console.log(myBook.author);
```

Et voici comment vous utilisez les crochets pour accéder aux mêmes propriétés :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};

console.log(myBook["title"]);
console.log(myBook["author"]);
```

Gardez à l'esprit que vous devez entourer le nom de la propriété de guillemets comme une chaîne de caractères, sinon JavaScript pensera que vous passez une variable à l'intérieur des crochets.

### Comment ajouter une nouvelle propriété à l'objet

Vous pouvez assigner une nouvelle propriété à l'objet en utilisant soit la notation par point soit les crochets comme ceci :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};

// ajouter la propriété de l'année de sortie
myBook.year = 2023;

// ajouter la propriété de l'éditeur
myBook["publisher"] = "CodeWithNathan";

console.log(myBook);
```

Lorsque vous imprimez l'objet, voici le résultat :

```txt
{
  title: 'Introduction à JavaScript',
  author: 'Nathan Sebhastian',
  year: 2023,
  publisher: 'CodeWithNathan'
}
```

Vous pouvez ajouter autant de propriétés que vous le souhaitez au même objet.

### Comment modifier les propriétés des objets

Pour modifier une propriété existante, vous devez spécifier une propriété d'objet existante en utilisant soit la notation par point soit les crochets suivie de l'opérateur d'affectation comme suit :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};

// changer la propriété de l'auteur
myBook.author = "John Doe";

console.log(myBook);
```

Sortie :

```txt
{
  title: 'Introduction à JavaScript',
  author: 'John Doe'
}
```

Comme vous pouvez le voir, la valeur de la propriété `author` a été modifiée.

### Comment supprimer les propriétés des objets

Pour supprimer une propriété de votre objet, vous devez utiliser l'opérateur `delete` comme suit :

```js
let myBook = {
  title: "Introduction à JavaScript",
  author: "Nathan Sebhastian",
};

delete myBook.author;

console.log(myBook);
```

**Sortie :**

```txt
{ title: 'Introduction à JavaScript' }
```

Lorsque vous essayez d'accéder à la propriété supprimée, vous obtiendrez la valeur `undefined`.

### Comment vérifier si une propriété existe dans un objet

Pour vérifier si une certaine propriété existe dans votre objet, vous pouvez utiliser l'opérateur `in` comme ceci :

```js
propertyName in myObject
```

L'opérateur `in` retourne `true` si le `propertyName` existe dans votre objet.

Voir l'exemple ci-dessous :

```js
let person = {
  firstName: "Nathan",
  lastName: "Sebhastian"
}

// vérifier si firstName existe
console.log('firstName' in person); // true

// vérifier si age existe
console.log('age' in person); // false
```

Maintenant, vous savez comment manipuler un objet JavaScript.

### Exercice #8

Créez un objet `person` avec les propriétés suivantes :

* `name` - le nom de la personne
    
* `age` - l'âge de la personne
    
* `greet()` - une fonction pour saluer une autre personne
    

À l'intérieur de la fonction `greet()`, présentez la personne, en spécifiant le nom et l'âge.

Voici un exemple de sortie :

```txt
person.greet();

Bonjour ! Je m'appelle Alex et j'ai 22 ans.
```

## Exercice final : Construire une machine de caisse enregistreuse

Construisons une machine de caisse enregistreuse qui peut ajouter des articles à un panier d'achat, calculer le prix total, calculer les remises et accepter le paiement en espèces.

La devise est supposée être en USD, donc vous n'avez pas besoin de l'ajouter au programme.

La caisse enregistreuse a 3 articles à vendre :

* Téléphone pour 300
    
* Smart TV pour 220
    
* Console de jeu pour 150
    

Il y a une remise de 10 % lorsque le prix total est supérieur à 400.

La caisse enregistreuse doit avoir un panier d'achat qui commence vide.

La caisse enregistreuse doit fournir une méthode appelée `addItem` qui prend le nom d'un article comme paramètre. Lorsqu'elle est appelée, elle doit vérifier si l'article est disponible à la vente. Si c'est le cas, l'article doit être ajouté au panier d'achat. Si ce n'est pas disponible, affichez un message indiquant que nous ne vendons pas cet article.

La caisse enregistreuse doit fournir une méthode appelée `calculateTotalPrice` qui calcule le prix total de tous les articles dans le panier d'achat. Elle doit parcourir les articles dans le panier d'achat et additionner leurs prix.

La caisse enregistreuse doit fournir une méthode appelée `pay` qui prend le montant du paiement comme paramètre.

Elle doit calculer le prix total des articles dans le panier d'achat en utilisant la méthode `calculateTotalPrice`. Si le prix total est supérieur à 400, une remise de 10 % doit être appliquée.

La méthode doit ensuite comparer le montant du paiement avec le prix total (après application de la remise) et afficher un message approprié :

* Si le montant du paiement est égal ou supérieur au prix total, elle doit afficher un message remerciant le client pour l'achat. Si un changement est dû, elle doit également afficher le montant du changement à donner.
    
* Si le montant du paiement est inférieur au prix total, elle doit afficher un message indiquant que le client n'a pas assez d'argent pour acheter les articles.
    
* Le programme doit inclure des instructions `console.log()` appropriées pour afficher des messages pour l'ajout d'articles au panier d'achat, l'affichage du prix total et le traitement du paiement.
    

Le programme doit gérer les scénarios où le montant du paiement du client est exactement égal au prix total, ainsi que les cas où le montant du paiement est supérieur ou inférieur au prix total.

Pour construire le programme, vous devez utiliser ce que vous avez appris sur les objets, les tableaux, les conditionnels et les boucles.

Je vous recommande d'essayer de construire le programme vous-même d'abord. Si vous êtes bloqué, alors consultez la solution fournie ci-dessous. Bonne chance !

## Conclusion

Félicitations pour avoir terminé ce manuel ! Nous avons parcouru beaucoup de concepts ensemble pour apprendre à coder en utilisant JavaScript.

J'espère que vous avez apprécié le processus autant que j'ai apprécié l'écrire. J'adorerais avoir votre retour, apprendre ce que vous avez aimé et ce que vous n'avez pas aimé afin que je puisse améliorer le tutoriel.

Si vous voulez en savoir plus sur JavaScript, je crée un cours qui vous aide à utiliser JavaScript pour construire des applications web. Il est actuellement en période de pré-commande afin que vous puissiez obtenir le cours à un prix inférieur et soutenir mon travail dans la création de plus de tutoriels. Vous pouvez [le consulter ici](https://codewithnathan.com/js-course).

[![The JavaScript Tutorial by Nathan Sebhastian](https://www.freecodecamp.org/news/content/images/2023/07/nathan-js-tutorial.jpg align="left")](https://codewithnathan.com/js-course)

## Solutions

### Exercice #1

```js
console.log("Votre nom ici");
console.log("Votre âge ici");
console.log("Votre profession ici");
```

### Exercice #2

```js
let name = "Votre nom ici";
let age = "Votre âge ici";
let occupation = "Votre profession ici";

console.log(name);
console.log(age);
console.log(occupation);
```

### Exercice #3

```txt
1
false
true
true
true
false
```

### Exercice #4

```js
let colors = ["red", "green", "blue"];

colors.push("black");
console.log(colors);

colors.shift();
colors[0] = "blue";
colors[1] = "green";
console.log(colors);

colors.unshift("yellow");
console.log(colors);
```

### Exercice #5

En utilisant l'instruction `if...else` :

```js
let grade = "A";

if (grade === "A") {
  console.log("Vous avez obtenu un A, alors voici un Chocolat pour vous !");
} else if (grade === "B") {
  console.log("Vous avez obtenu un B, voici un Cookie pour vous !");
} else if (grade === "C") {
  console.log(
    "Vous avez obtenu un C, il y a de la place pour l'amélioration et voici votre Bonbon !"
  );
} else {
  console.log("Pas de récompense à donner.");
}
```

```js
let grade = "A";
switch (grade) {
  case "A":
    console.log("Vous avez obtenu un A, alors voici un Chocolat pour vous !");
    break;
  case "B":
    console.log("Vous avez obtenu un B, voici un Cookie pour vous !");
    break;
  case "C":
    console.log(
      "Vous avez obtenu un C, il y a de la place pour l'amélioration et voici votre Bonbon !"
    );
    break;
  default:
    console.log("Pas de récompense à donner.");
}
```

En utilisant l'instruction `switch...case` :

### Exercice #6

Motif de demi-pyramide :

```js
let pattern;

for (let i = 1; i <= 5; i++) {
  pattern = "";
  for (let j = 1; j <= i; j++) {
    pattern += "*";
  }
  console.log(pattern);
}
```

Motif de demi-pyramide inversée :

```js
for (let i = 4; i >= 0; i--) {
  pattern = "";
  for (let j = 0; j <= i; j++) {
    pattern += "*";
  }
  console.log(pattern);
}
```

### Exercice #7

```js
function calculateSquare(side) {
  console.log(`Le côté du carré est ${side}`);
  console.log(`L'aire du carré est ${side * side}`);
  console.log(`Le périmètre du carré est ${4 * side}`);
}

calculateSquare(7);
```

### Exercice #8

```js
const person = {
  name: "Alex",
  age: 22,
  greet: function () {
    console.log(
      `Bonjour ! Je m'appelle ${this.name} et j'ai ${this.age} ans.`
    );
  },
};

person.greet();
```

### Exercice final

```js
const cashRegister = {
  itemsForSale: [
    { name: "Phone", price: 300 },
    { name: "Smart TV", price: 220 },
    { name: "Gaming Console", price: 150 },
  ],
  shoppingCart: [],
  addItem: function (name) {
    let foundItem = this.itemsForSale.find(function (item) {
      return item.name === name;
    });
    if (foundItem) {
      this.shoppingCart.push(foundItem);
      console.log(`Ajout de ${name} à votre panier d'achat`);
    } else {
      console.log(`Désolé, nous ne vendons pas ${name} ici !`);
    }
  },
  calculateTotalPrice: function () {
    let totalPriceAmount = 0;
    this.shoppingCart.forEach(function (purchasedItem) {
      totalPriceAmount += purchasedItem.price;
    });
    return totalPriceAmount;
  },
  pay: function (amount) {
    let totalPriceAmount = this.calculateTotalPrice();
    if (totalPriceAmount > 500) {
      totalPriceAmount -= totalPriceAmount * 0.1;
      console.log(
        `Vous obtenez une remise de 10% et votre prix total est ${totalPriceAmount}`
      );
    }
    if (amount >= totalPriceAmount) {
      if (amount - totalPriceAmount > 0) {
        console.log(`Voici votre monnaie de ${amount - totalPriceAmount}`);
      }
      console.log(`Merci pour votre achat ! Espérons que vous reviendrez`);
    } else {
      console.log(
        "Désolé, mais vous n'avez pas assez d'argent pour acheter vos articles"
      );
    }
  },
};
```

Pour tester l'objet, exécutez le code ci-dessous :

```js
cashRegister.addItem("Phone");
cashRegister.addItem("Smart TV");
console.log(cashRegister.calculateTotalPrice());
cashRegister.pay(700);
```

Sortie :

```txt
Ajout de Phone à votre panier d'achat
Ajout de Smart TV à votre panier d'achat
520
Vous obtenez une remise de 10% et votre prix total est 468
Voici votre monnaie de 232
Merci pour votre achat ! Espérons que vous reviendrez
```

Merci d'avoir lu !

Si vous avez aimé ce manuel et souhaitez faire passer vos compétences en JavaScript au niveau supérieur, je vous recommande de consulter mon nouveau livre *Beginning Modern JavaScript* [ici](https://www.amazon.com/dp/B0CQXHMF8G).

[![beginning-js-cover](https://www.freecodecamp.org/news/content/images/2024/01/beginning-js-cover.png align="left")](https://www.amazon.com/dp/B0CQXHMF8G)

Le livre est conçu pour être facile à comprendre et accessible à toute personne souhaitant apprendre JavaScript. Il fournit un guide progressif qui vous aidera à comprendre comment utiliser JavaScript pour créer une application dynamique.

Voici ma promesse : *Vous allez vraiment avoir l'impression de comprendre ce que vous faites avec JavaScript.*

Jusqu'à la prochaine fois !