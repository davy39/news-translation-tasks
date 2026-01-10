---
title: Comment commencer à apprendre JavaScript
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2023-07-13T20:22:41.000Z'
originalURL: https://freecodecamp.org/news/getting-started-with-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/pexels-mikhail-nilov-6968122.jpg
tags:
- name: beginner
  slug: beginner
- name: JavaScript
  slug: javascript
seo_title: Comment commencer à apprendre JavaScript
seo_desc: 'Just in case you haven''t yet been properly introduced, JavaScript is a
  powerful programming language that provides significant value in web development.

  Its benefits include:


  Server-side development through Node.js

  Client-side interactivity where sc...'
---

Au cas où vous n'auriez pas encore été correctement introduit, JavaScript est un langage de programmation puissant qui apporte une valeur significative dans le développement web.

Ses avantages incluent :

* Développement côté serveur via Node.js
* Interactivité côté client où les scripts s'exécutent directement dans les navigateurs de vos utilisateurs
* Interfaces utilisateur réactives et interactives
* Intégration large d'API et de services tiers permettant des applications multi-niveaux
* Développement d'applications mobiles multiplateformes via des frameworks comme React Native et Ionic
* Support quasi-universel des navigateurs, et un vaste écosystème de bibliothèques, frameworks et outils

Si vous prévoyez d'ajouter de l'interactivité à l'un de vos sites web, vous devrez acquérir quelques compétences en JavaScript. Mais les bases sont en réalité assez simples.

Dans cet article, je vais vous montrer comment incorporer JavaScript dans votre code HTML, à quoi pourraient ressembler des opérations simples en utilisant JavaScript, comment créer et exécuter des fonctions en JavaScript, et comment vous pouvez tirer parti de la console de votre navigateur pour tester JavaScript dans un environnement vivant – mais sûr.

Au fait, il n'y a aucun lien technique entre JavaScript et le langage de programmation Java.

Quelque temps après que Brendan Eich ait créé son langage LiveScript chez Netscape en seulement 10 jours en 1995, la légende raconte qu'il a renommé son projet JavaScript pour tirer parti de la popularité de Java à l'époque.

Mais ce n'était plus qu'une stratégie marketing qu'une indication de quelque relation technique.

Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Si vous le souhaitez, vous pouvez suivre la version vidéo ici :

%[https://youtu.be/TrARdpmfD7c]

## Comment incorporer JavaScript dans votre code HTML

Vous pouvez inclure du code JavaScript dans vos pages web HTML de plusieurs manières. Tout d'abord, vous pouvez le faire en référençant un fichier `.js` externe en tant qu'attribut d'une balise `<script>` – comme vous le voyez ici :

```
<script src="script.js"></script>
```

Ou vous pouvez insérer votre code entre les balises `<script>` dans la section head de votre HTML comme ceci :

```
<head>
  <title>Exemple d'application JavaScript</title>
  <script>
    function greet() {
      var name = prompt("Quel est votre nom ?");
      alert("Bonjour, " + name + " !");
    }
  </script>
</head>
```

Les deux méthodes fonctionnent bien. Depuis l'adoption de HTML5, cependant, vous n'avez plus besoin d'ajouter `text/javascript` en tant qu'attribut de la balise `<script>`. À ce stade, JavaScript est le langage de script par défaut pour HTML.

## Comment exécuter du JavaScript simple

Voici un script simple de type hello-world qui fonctionnera pour nous lancer :

```
<!DOCTYPE html>
<html>
<head>
  <title>Exemple d'application JavaScript</title>
  <script>
    // Code JavaScript
    function greet() {
      var name = prompt("Quel est votre nom ?");
      alert("Bonjour, " + name + " !");
    }
  </script>
</head>
<body>
  <h1>Exemple d'application JavaScript</h1>
  <button onclick="greet()">Dire Bonjour</button>
</body>
</html>
```

Analysons ce code section par section.

Vous pouvez voir que le JavaScript est tout entre ces deux balises `<script>` et contient sa propre ligne de commentaire.

```
  <script>
    // Code JavaScript
    function greet() {
      var name = prompt("Quel est votre nom ?");
      alert("Bonjour, " + name + " !");
    }
  </script>
```

Je ne sais vraiment pas pourquoi cela doit être ainsi, mais les codes d'échappement de commentaire pour un langage ne semblent jamais fonctionner pour un autre. Dans le monde JavaScript, vous aurez besoin de deux barres obliques : `//`.

La première ligne de code réel introduit une nouvelle fonction nommée `greet`.

```
    function greet() {
      var name = prompt("Quel est votre nom ?");
      alert("Bonjour, " + name + " !");
    }
```

Les parenthèses sont nécessaires et, je vous assure, vous en ferez bon usage plus tard. Le code de la fonction doit tout se trouver entre deux accolades comme vous le voyez ici.

Cette fonction n'a que deux lignes. La première utilise `var` pour déclarer une variable qui s'appellera `name`. `name` prendra la valeur entrée par les utilisateurs lorsqu'ils seront invités avec la question "Quel est votre nom ?".

NOTE : bien que déclarer une variable comme `var` ait encore ses cas d'utilisation, pour la plupart des développements JavaScript modernes, [utiliser `let` et `const` est considéré comme une meilleure pratique](https://www.freecodecamp.org/news/differences-between-var-let-const-javascript/) en raison de leurs règles de portée améliorées et de leur comportement d'assignation de variables plus strict. J'ai utilisé `var` ici pour simplifier.

Une fois qu'une valeur a été entrée, `alert` générera une fenêtre pop-up avec le texte `Bonjour`, une virgule et un espace, la valeur actuelle de la variable `name`, et un point d'exclamation. Le caractère `+` sert à concaténer toutes ces valeurs en une phrase.

Mais attendez : vous ne voyez aucun champ de saisie de nom sur cette page, n'est-ce pas ? Et comment exactement la fonction est-elle exécutée ?

Excellentes questions. Cela se passera dans la section HTML. Il s'agit essentiellement d'une balise `<button>` qui a une étiquette de texte `Dire Bonjour`. Mais c'est l'attribut de la balise qui nous intéresse vraiment.

`onclick` appelle notre fonction `greet`. En d'autres termes, `onclick` indique au navigateur d'exécuter la fonction `greet` chaque fois que le bouton est cliqué.

```
<body>
  <h1>Exemple d'application JavaScript</h1>
  <button onclick="greet()">Dire Bonjour</button>
</body>
</html>

```

Collez le code dans un fichier `.html` et chargez-le dans un navigateur. Lorsque vous cliquez sur le bouton, une nouvelle boîte de dialogue s'ouvre avec un champ de saisie de données demandant votre nom. Lorsque vous tapez votre nom et cliquez sur `OK`, vous verrez une phrase bien concaténée, parfaitement arrangée.

## Comment travailler avec JavaScript dans une console de navigateur

Mais avant de continuer, je devrais vous rappeler que JavaScript a été conçu pour les navigateurs. Nous pouvons donc nous attendre à certaines intégrations utiles. Eh bien, peut-être la plus utile de toutes est la console.

Vous pouvez ouvrir la console en cliquant avec le bouton droit sur n'importe quel endroit vide d'une page de navigateur et en sélectionnant `Inspecter`. Cela devrait fonctionner quel que soit le navigateur que vous utilisez. Appuyer sur `F12` est une autre façon d'accéder au même endroit.

Dans mon navigateur Brave, la console apparaît sur le côté droit :

![Image](https://www.freecodecamp.org/news/content/images/2023/06/console1.png)
_Ouvrir la console_

Ceci est connu sous le nom de console du développeur, car il y a toutes sortes de fonctionnalités utiles de débogage et d'analyse de code intégrées.

Dans l'onglet `Éléments`, vous verrez une représentation du code de la page. Vous pouvez développer les sections `<head>` et `<script>` pour voir avec quoi vous travaillez. En passant à l'onglet `Console`, vous trouvez un environnement JavaScript en direct.

Dans cet exemple, j'ai collé trois opérations JavaScript dans la console que nous pouvons réellement tester.

![Image](https://www.freecodecamp.org/news/content/images/2023/06/webdev-s4-01-f011630.png)

Voici ce code révolutionnaire au format copier-coller :

```
console.log(2 + 2);
console.log("Bonjour" + " " + "Monde");
var fruits = ["Pomme", "Banane", "Orange"];
console.log(fruits.length);
```

Essayez-le vous-même.

Maintenant, vous devez être conscient que `console.log()` est une fonction JavaScript intégrée qui vous permet d'afficher des messages ou des valeurs dans la console. Elle est couramment utilisée pour le débogage et l'affichage d'informations pendant le processus de développement. Donc, en règle générale, vous ne voudrez utiliser la fonction `console.log` que ici.

Ce serait une excellente opportunité de vous présenter à la syntaxe JavaScript. La fonction accepte un ou plusieurs arguments entre parenthèses et les imprime dans la console.

La première exécution est la somme de 2 + 2.

```
console.log(2+2);
```

À partir de là, nous pouvons voir que vous pouvez utiliser n'importe lequel des opérateurs arithmétiques (comme plus, moins, l'astérisque pour la multiplication, la barre oblique pour la division, l'angle droit pour supérieur à, l'angle gauche pour inférieur à, et le signe égal) tels quels dans votre code JavaScript.

La seule autre chose à propos de cela qui pourrait attirer votre attention est le point-virgule qui suit. En JavaScript, les points-virgules sont des terminateurs d'instruction qui vous aident à éviter l'ambiguïté et, parfois, un comportement inattendu. Utilisez-les tôt, utilisez-les souvent.

La deuxième ligne contient un autre exemple de concaténation.

```
console.log("Bonjour" + " " + "Monde");
```

Celui-ci imprimera le mot "Bonjour" suivi d'un espace, puis le mot "Monde".

Avant d'exécuter la commande suivante, nous allons déclarer une variable appelée `fruits`, qui contiendra un tableau de trois mots : "Pomme", "Banane" et "Orange".

```
var fruits = ["Pomme", "Banane", "Orange"];
console.log(fruits.length);
```

Le code qui suit prendra la variable `fruits` et affichera sa longueur.

Lorsque j'appuie sur `Entrée`, les trois commandes s'exécuteront en une seule fois. Il y a trois lignes de sortie : "4", "Bonjour Monde" et "3" – ce qui est exactement ce à quoi nous nous attendions.

C'était bien et tout, mais cela n'utilise guère toutes les ressources de votre navigateur. Alors maintenant, essayez d'exécuter une commande qui générera une erreur. Vous pourriez, par exemple, ajouter quelques caractères illégaux à une opération comme ces astérisques :

```
console.log("Bonjour" + " " + "Monde")**;
```

Voici ce qui se passe :

```
VM30:1 Uncaught SyntaxError: Unexpected token ';'
```

Vous devriez voir une erreur de syntaxe non capturée. Le test `VM30:1` nous montre même quelle ligne de notre code contenait le problème – `1` dans ce cas. Si cela était du code réel, nous serions un pas plus près de résoudre un bug.

## Conclusion

Vous êtes maintenant correctement introduit aux bases de JavaScript et, en particulier, à la manière d'intégrer JavaScript avec votre HTML et à la manière d'utiliser l'environnement de la console de votre navigateur. Maintenant, allez voir ce que vous pouvez construire !

_Cet article provient de [mon cours complet LPI Web Development Essentials Study Guide](https://www.udemy.com/course/complete-lpi-web-development-essentials-exam-study-guide/?referralCode=C92570BCBB38302A9257). Et il y a beaucoup plus de bonnes choses technologiques disponibles sur [bootstrap-it.com](https://bootstrap-it.com/)_