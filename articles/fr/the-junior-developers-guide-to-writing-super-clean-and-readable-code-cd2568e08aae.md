---
title: Le guide du développeur junior pour écrire du code super propre et lisible
subtitle: ''
author: Chris Blakely
co_authors: []
series: null
date: '2019-03-28T20:06:23.000Z'
originalURL: https://freecodecamp.org/news/the-junior-developers-guide-to-writing-super-clean-and-readable-code-cd2568e08aae
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BbAtAVDs9srxs33lkY9sbw.jpeg
tags:
- name: clean code
  slug: clean-code
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Le guide du développeur junior pour écrire du code super propre et lisible
seo_desc: 'Writing code is one thing, but writing clean, readable code is another
  thing. But what is “clean code?” I’ve created this short clean code for beginners
  guide to help you on your way to mastering and understanding the art of clean code.

  Imagine you a...'
---

Écrire du code est une chose, mais écrire du code propre et lisible en est une autre. Mais qu'est-ce que le "code propre" ? J'ai créé ce court _guide du code propre pour débutants_ pour vous aider à maîtriser et à comprendre l'art du code propre.

Imaginez que vous lisez un article. Il y a un paragraphe d'introduction, qui vous donne un bref aperçu de ce dont traite l'article. Il y a des titres, chacun avec une série de paragraphes. Les paragraphes sont structurés avec les informations pertinentes regroupées et ordonnées de manière à ce que l'article "coule" et se lise bien.

Maintenant, imaginez que l'article n'a aucun titre. Il y a des paragraphes, mais ils sont longs et dans un ordre confus. Vous ne pouvez pas parcourir l'article et devez vraiment plonger dans le contenu pour avoir une idée de ce dont il traite. Cela peut être assez frustrant !

Votre code devrait se lire comme un bon article. Considérez vos classes/fichiers comme des titres, et vos méthodes comme des paragraphes. Les phrases sont les instructions de votre code. Voici quelques caractéristiques du code propre :

1. Le code propre est focalisé — Chaque fonction, chaque classe et chaque module doit faire une chose et la faire bien.
2. Il doit être élégant — Le code propre doit être _simple_ à lire. Le lire devrait vous faire sourire. Il devrait vous laisser penser "Je sais exactement ce que fait ce code".
3. Le code propre est bien entretenu. Quelqu'un a pris le temps de le garder simple et ordonné. Il a prêté une attention appropriée aux détails. Il s'en est soucié.
4. Les tests doivent passer — Le code cassé n'est pas propre !

Passons à la grande question du jour — comment écrire réellement du code propre en tant que développeur junior ? Voici mes meilleurs conseils pour commencer.

### Utiliser une mise en forme et une indentation cohérentes

Les livres seraient difficiles à lire si l'espacement des lignes était incohérent, les tailles de police différentes et les sauts de ligne partout. Il en va de même pour votre code.

Pour rendre votre code clair et facile à lire, assurez-vous que l'indentation, les sauts de ligne et la mise en forme sont cohérents. Voici un bon et un mauvais exemple :

#### Le Bon

```js
function getStudents(id) { 
     if (id !== null) { 
        go_and_get_the_student(); 
     } else { 
        abort_mission(); 
     } 
}
```

* À première vue, vous pouvez voir qu'il y a une instruction `if/else` dans la fonction
* Les accolades et l'indentation cohérente rendent facile la visualisation du début et de la fin des blocs de code
* Les accolades sont cohérentes — Remarquez comment l'accolade ouvrante pour la `function` et pour le `if` sont sur la même ligne

#### Le Mauvais

```js
function getStudents(id) {
if (id !== null) {
go_and_get_the_student();} 
    else 
    {
        abort_mission();
    }
    }
```

Woah ! Tant d'erreurs ici.

* L'indentation est partout — vous ne pouvez pas dire où la fonction se termine, ou où le bloc `if/else` commence (oui, il y a un bloc if/else là-dedans !)
* Les accolades sont confuses et ne sont pas cohérentes
* L'espacement des lignes est incohérent

C'est un exemple un peu exagéré, mais il montre l'avantage d'utiliser une indentation et une mise en forme cohérentes. Je ne sais pas pour vous, mais l'exemple "bon" était beaucoup plus agréable à lire pour moi !

La bonne nouvelle est qu'il existe de nombreux plugins IDE que vous pouvez utiliser pour formater automatiquement le code pour vous. Alléluia !

* VS Code : [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode)
* Atom : [Atom Beautify](https://atom.io/packages/atom-beautify)
* Sublime Text : [Prettify](https://packagecontrol.io/packages/HTML-CSS-JS%20Prettify)

### Utiliser des noms de variables et de méthodes clairs

Au début, j'ai parlé de l'importance de rendre votre code facile à lire. Un aspect important de cela est le nommage que vous choisissez (c'est l'une des [erreurs que j'ai faites lorsque j'étais développeur junior](https://www.chrisblakely.dev/7-mistakes-i-made-as-a-junior-developer/)). Examinons un exemple de bon nommage :

```
function changeStudentLabelText(studentId){                  
     const studentNameLabel = getStudentName(studentId); 
}
function getStudentName(studentId){ 
     const student = api.getStudentById(studentId); 
     return student.name; 
}
```

Ce snippet de code est bon pour plusieurs raisons :

* Les fonctions sont nommées clairement avec des arguments bien nommés. Lorsqu'un développeur lit cela, il est clair dans son esprit, "Si j'appelle la méthode `getStudentName()` avec un `studentId`, je vais obtenir un nom d'étudiant" — ils n'ont pas besoin de naviguer vers la méthode `getStudentName()` s'ils n'en ont pas besoin !
* Dans la méthode `getStudentName()`, les variables et les appels de méthodes sont à nouveau clairement nommés — il est facile de voir que la méthode appelle une `api`, obtient un objet `student`, et retourne la propriété `name`. Facile !

Choisir de bons noms lors de l'écriture de code propre pour débutants est plus difficile que vous ne le pensez. À mesure que votre application grandit, utilisez ces conventions pour vous assurer que votre code est facile à lire :

* Choisissez un style de nommage et soyez cohérent. Soit `camelCase` soit `under_scores` mais pas les deux !
* Nommez vos fonctions, méthodes et variables en fonction de ce que fait cette chose, ou de ce qu'est cette chose. Si votre méthode _obtient_ quelque chose, mettez `get` dans le nom. Si votre variable _stocke_ une couleur de voiture, appelez-la `carColour`, par exemple.

**CONSEIL BONUS** — si vous ne pouvez pas nommer votre fonction ou méthode, alors cette fonction fait trop de choses. Allez-y et divisez-la en fonctions plus petites ! Par exemple, si vous finissez par appeler votre fonction `updateCarAndSave()`, créez 2 méthodes `updateCar()` et `saveCar()`.

### Utiliser des commentaires lorsque nécessaire

Il y a un dicton, "le code devrait être auto-documenté", ce qui signifie essentiellement que, au lieu d'utiliser des commentaires, votre code devrait être suffisamment clair pour réduire le besoin de commentaires. C'est un point valide, et je suppose que cela a du sens dans un monde parfait. Pourtant, le monde de la programmation est loin d'être parfait, donc parfois les commentaires sont nécessaires.

Les commentaires de documentation sont des commentaires qui décrivent ce que fait une fonction ou une classe particulière. Si vous écrivez une bibliothèque, cela sera utile pour les développeurs qui utilisent votre bibliothèque. Voici un exemple de useJSDoc :

```js
/** * Résout les équations de la forme a * x = b 
* @example * 
// retourne 2 * globalNS.method1(5, 10); 
* @example * 
// retourne 3 * globalNS.method(5, 15); 
* @returns {Number} Retourne la valeur de x pour l'équation. */ globalNS.method1 = function (a, b) { return b / a; };
```

Les commentaires de clarification sont destinés à toute personne (y compris vous-même dans le futur) qui pourrait avoir besoin de maintenir, de refactoriser ou d'étendre votre code. Plus souvent qu'autrement, les commentaires de clarification pourraient être évités, en faveur du "code auto-documenté". Voici un exemple de commentaire de clarification :

```js
/* Cette fonction appelle une API tierce. En raison d'un problème avec le fournisseur de l'API, la réponse retourne "BAD REQUEST" parfois. Si c'est le cas, nous devons réessayer */ 
function getImageLinks(){ 
     const imageLinks = makeApiCall(); 
     if(imageLinks === null){ 
        retryApiCall(); 
     } else { 
        doSomeOtherStuff(); 
     } 
}
```

Voici quelques commentaires que vous devriez essayer d'éviter. Ils n'offrent pas beaucoup de valeur, peuvent être trompeurs et encombrent simplement le code.

Commentaires redondants qui n'ajoutent pas de valeur :

```js
// cela définit l'âge des étudiants 
function setStudentAge();
```

Commentaires trompeurs :

```js
// cela définit le nom complet de l'étudiant 
function setLastName();
```

Commentaires drôles ou insultants :

```js
// cette méthode fait 5000 lignes de long mais il est impossible de la refactoriser alors n'essayez pas 
function reallyLongFunction();
```

### Rappelez-vous le principe DRY (Don't Repeat Yourself)

Le principe DRY est énoncé comme suit :

> "Chaque morceau de connaissance doit avoir une représentation unique, non ambiguë et faisant autorité au sein d'un système."

À son niveau le plus simple, cela signifie essentiellement que vous devriez chercher à réduire la quantité de code dupliqué qui existe. (Notez que j'ai dit "réduire" et non "éliminer" — Il y a certaines instances où le code dupliqué n'est pas la fin du monde !)

Le code dupliqué peut être un cauchemar à maintenir et à modifier. Examinons un exemple :

```js
function addEmployee(){ 
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'Rory',
        lastName: 'Millar',
        role: 'Admin'
    }
    
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

function addManager(){  
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'James',
        lastName: 'Marley',
        role: 'Admin'
    }
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}

function addAdmin(){    
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'Gary',
        lastName: 'Judge',
        role: 'Admin'
    }
    
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    axios.post('/user', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log(error);
      });
}
```

Imaginez que vous créez une application web de ressources humaines pour un client. Cette application permet aux administrateurs d'ajouter des utilisateurs avec des rôles à une base de données via une API. Il y a 3 rôles : employé, manager et administrateur. Examinons quelques-unes des fonctions qui pourraient exister :

Cool ! Le code fonctionne et tout va bien dans le monde. Après un certain temps, notre client arrive et dit :

> _Hey ! Nous aimerions que le message d'erreur affiché contienne la phrase "il y a eu une erreur". Aussi, pour être extra énervant, nous voulons changer le point de terminaison de l'API de `/user` à `/users`. Merci !_

Alors, avant de nous lancer et de commencer à coder, faisons un pas en arrière. Souvenez-vous, au début de cet article sur le code propre pour débutants, lorsque j'ai dit "Le code propre devrait être focalisé". C'est-à-dire, faire une chose et la faire bien ? C'est là que notre code actuel a un petit problème. Le code qui fait l'appel API et gère l'erreur est répété — ce qui signifie que nous devons changer le code en 3 endroits pour répondre aux nouvelles exigences. Énervant !

Alors, que se passerait-il si nous refactorisions cela pour _être plus focalisé_ ? Jetez un coup d'œil à ce qui suit :

```js
function addEmployee(){ 
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'Rory',
        lastName: 'Millar',
        role: 'Admin'
    }
    
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    saveUserToDatabase(user);
}

function addManager(){  
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'James',
        lastName: 'Marley',
        role: 'Admin'
    }
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    saveUserToDatabase(user);
}

function addAdmin(){    
    // créer l'objet utilisateur et donner le rôle
    const user = {
        firstName: 'Gary',
        lastName: 'Judge',
        role: 'Admin'
    }
    
    // ajouter le nouvel utilisateur à la base de données - et logger la réponse ou l'erreur
    saveUserToDatabase(user);
}

function saveUserToDatabase(user){
    axios.post('/users', user)
      .then(function (response) {
        console.log(response);
      })
      .catch(function (error) {
        console.log("there was an error " + error);
  });
}
```

Nous avons déplacé la logique qui crée un appel API dans sa propre méthode `saveUserToDatabase(user)` (est-ce un bon nom ? À vous de décider !) que les autres méthodes _appelleront_ pour sauvegarder l'utilisateur. Maintenant, si nous devons changer la logique de l'API à nouveau, nous n'avons qu'à mettre à jour 1 méthode. De même, si nous devons ajouter une autre méthode qui crée des utilisateurs, la méthode pour sauvegarder l'utilisateur dans la base de données via l'API existe déjà. Hourra !

### Un exemple de refactorisation utilisant ce que nous avons appris jusqu'à présent

Fermons les yeux et imaginons très fort que nous créons une application de calculatrice. Il y a des fonctions qui sont utilisées et qui nous permettent d'additionner, de soustraire, de multiplier et de diviser respectivement. Le résultat est affiché dans la console.

Voici ce que nous avons jusqu'à présent. Voyez si vous pouvez repérer les problèmes avant de continuer :

```js
function addNumbers(number1, number2)
{
    const result = number1 + number2;
        const output = 'The result is ' + result;
        console.log(output);
}

// cette fonction soustrait 2 nombres
function substractNumbers(number1, number2){
    
    // stocke le résultat dans une variable appelée result
    const result = number1 - number2;
    const output = 'The result is ' + result;
    console.log(output);
}

function doStuffWithNumbers(number1, number2){
    const result = number1 * number2;
    const output = 'The result is ' + result;
    console.log(output);
}

function divideNumbers(x, y){
    const result = number1 / number2;
    const output = 'The result is ' + result;
    console.log(output);
}
```

Quels sont les problèmes ?

* L'indentation est incohérente — peu importe le format d'indentation que nous utilisons, tant qu'il est cohérent
* La 2ème fonction a des commentaires redondants — nous pouvons comprendre ce qui se passe en lisant le nom de la fonction et le code à l'intérieur de la fonction, donc avons-nous vraiment besoin d'un commentaire ici ?
* Les 3ème et 4ème fonctions n'utilisent pas de bons noms — `doStuffWithNumbers()` n'est pas le meilleur nom de fonction car il ne précise pas ce qu'il fait. `(x, y)` ne sont pas non plus des variables descriptives — sont `x & y` des fonctions ? des nombres ? des bananes ?
* Les méthodes _font plus d'une chose_ — effectuent le calcul, mais affichent également la sortie. Nous pouvons séparer la logique d'_affichage_ dans une méthode séparée — conformément au **principe DRY**

Maintenant, nous allons utiliser ce que nous avons appris dans ce guide du code propre pour débutants pour tout refactoriser afin que notre nouveau code ressemble à ceci :

```js
function addNumbers(number1, number2){
	const result = number1 + number2;
	displayOutput(result)
}

function substractNumbers(number1, number2){
	const result = number1 - number2;
	displayOutput(result)
}

function multiplyNumbers(number1, number2){
	const result = number1 * number2;
	displayOutput(result)
}

function divideNumbers(number1, number2){
	const result = number1 * number2;
	displayOutput(result)
}

function displayOutput(result){
	const output = 'The result is ' + result;
	console.log(output);
}
```

* Nous avons corrigé l'indentation pour qu'elle soit cohérente
* Ajusté le nommage des fonctions et des variables
* Supprimé les commentaires inutiles
* Déplacé la logique `displayOutput()` dans sa propre méthode — si la sortie doit changer, nous n'avons besoin de la changer qu'à un seul endroit

Félicitations ! Vous pouvez maintenant parler des principes du code propre lors de vos entretiens et lors de la [rédaction de votre CV percutant](https://www.chrisblakely.dev/how-to-write-an-awesome-junior-developer-resume-in-a-few-simple-steps/) !

### Ne "sur-nettoyez" pas votre code

Je vois souvent des développeurs en faire trop lorsqu'il s'agit de code propre. Faites attention à ne pas essayer de trop nettoyer votre code, car cela peut avoir l'effet inverse et rendre votre code _plus difficile à lire et à maintenir_. Cela peut également avoir un impact sur la productivité, si un développeur doit constamment sauter entre de nombreux fichiers/méthodes pour apporter une simple modification.

Soyez conscient du code propre, mais ne le suranalysez pas aux premiers stades de vos projets. Assurez-vous que votre code fonctionne et est bien testé. Lors de la phase de refactorisation, c'est là que vous devriez vraiment réfléchir à la manière de nettoyer votre code en utilisant le principe DRY, etc.

Dans ce guide du code propre pour débutants, nous avons appris à :

* Utiliser une mise en forme et une indentation cohérentes
* Utiliser des noms de variables et de méthodes clairs
* Utiliser des commentaires lorsque nécessaire
* Utiliser le principe DRY (Don't Repeat Yourself)

Si vous avez apprécié ce guide, assurez-vous de consulter [_Clean Code: A Handbook of Agile Software Craftsmanship_ par Robert C Martin](https://amzn.to/2U7JO4N). Si vous êtes sérieux au sujet de l'écriture de code propre et de la sortie du niveau de développeur junior, je recommande vivement ce livre.

Merci d'avoir lu !

Pour obtenir les derniers guides et cours pour développeurs juniors directement dans votre boîte de réception, assurez-vous de rejoindre la liste de diffusion sur [www.chrisblakely.dev](https://www.chrisblakely.dev/#sign-up) !