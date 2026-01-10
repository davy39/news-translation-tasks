---
title: Comment créer une application JavaScript adaptée aux débutants
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2023-05-09T16:05:03.000Z'
originalURL: https://freecodecamp.org/news/build-a-beginner-friendly-javascript-application
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/freeCodeCamp-Cover.png
tags:
- name: beginner
  slug: beginner
- name: CSS
  slug: css
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer une application JavaScript adaptée aux débutants
seo_desc: "JavaScript is a popular programming language for building web, mobile,\
  \ and desktop applications. \nThere are many frameworks and libraries that have\
  \ been built around JavaScript, with more likely being developed even as you are\
  \ reading this article. I..."
---

JavaScript est un langage de programmation populaire pour créer des applications web, mobiles et de bureau. 

Il existe de nombreux frameworks et bibliothèques qui ont été construits autour de JavaScript, avec d'autres probablement en développement même pendant que vous lisez cet article. Si vous prévoyez de commencer à apprendre JavaScript, certains d'entre eux valent également la peine d'être appris.

Comme pour tout langage de programmation, la maîtrise de JavaScript comporte deux parties vitales : comprendre les concepts clés et pratiquer ce que vous avez appris. Vous devez vous familiariser avec les concepts principaux du langage, et en même temps, vous devez commencer à pratiquer des projets de codage en utilisant les concepts que vous avez appris. 

J'ai récemment publié un article sur [Comment apprendre JavaScript efficacement avec des conseils et des stratégies d'apprentissage](https://www.freecodecamp.org/news/how-to-learn-javascript-effectively/). Vous devriez le consulter si vous ne l'avez pas déjà fait.

Dans cet article, nous nous concentrerons sur la partie pratique. Nous allons créer une application JavaScript adaptée aux débutants qui vous enseignera les bases de la création de structures HTML, du travail avec CSS, et enfin de l'ajout de comportements dynamiques en utilisant JavaScript.

Tout est prêt ? Commençons.

Si vous aimez également apprendre à partir de contenu vidéo, cet article est également disponible sous forme de tutoriel vidéo ici : 👂

%[https://www.youtube.com/watch?v=NkO4mVXnrtM]

## Que construisons-nous aujourd'hui ?

Nous allons créer un projet appelé `Colorify`. Il affiche un cercle coloré sur la page web et dispose de quelques boutons qui vous permettent de changer les couleurs en cliquant dessus. 

L'image ci-dessous montre un cercle rouge avec trois boutons étiquetés Rouge, Vert et Jaune. Lorsque vous cliquez sur Rouge, la couleur du cercle devient rouge – de même pour Vert et Jaune, respectivement.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-32.png)
_Le projet Colorify_

Nous utiliserons les concepts suivants de développement web lors de la création de cette application :

* Stylisation de base des DIV avec border-radius et centrage
* Disposition des boutons
* Utilisation des littéraux de gabarit
* Ajout de gestionnaires de clics
* Manipulation du DOM pour définir des valeurs

## Comment créer une structure de projet JavaScript

Tout d'abord, créons la structure du projet. Créez un dossier appelé `colorify` et créez ces fichiers vides à l'intérieur.

* **index.html** : Le fichier HTML qui contiendra le squelette et le balisage de l'application.
* **index.css** : Tout le code de style et d'embellissement de l'application va dans ce fichier CSS. Nous inclurons le fichier CSS dans le fichier HTML créé ci-dessus.
* **index.js** : Le code JavaScript va dans ce fichier. Nous créerons des fonctions pour fournir un comportement dynamique à l'application. Comme le fichier CSS, nous inclurons également ce fichier dans le fichier `index.html`.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/unnamed.png)
_La structure du projet_

## Comment construire la structure HTML 

Créons la structure de la page HTML. Nous avons besoin d'un cercle et de trois boutons dans le cadre des exigences du projet. Copiez le code suivant et collez-le à l'intérieur du fichier `index.html` :

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Colorify</title>
  <link rel="stylesheet" href="./index.css">
  <script src="./index.js" defer></script>
</head>
<body>
  <div class="container">
    <h1>Colorify</h1>
    <p class="subheading">
      Avec Colorify, nous voulons commencer
      à apprendre JavaScript.
    </p>
    <div class="circle" id="circleID"></div>
    <div class="action">
      <button onclick="paint('red')">Rouge</button>
      <button onclick="paint('green')">Vert</button>
      <button onclick="paint('yellow')">Jaune</button>
    </div>
  </div>
</body>
</html>
```

Le fichier HTML a deux sections principales :

### la section `<head>`

La section `<head>` inclut des informations méta comme le jeu de caractères supporté, la version d'Internet Explorer que la page doit utiliser pour le rendu avec la valeur X-UA-Compatible, et les informations de la fenêtre d'affichage. Nous avons également fourni un titre à la page web.

Nous avons inclus le fichier CSS en utilisant la balise link. Nous avons utilisé l'attribut `href` pour pointer vers le fichier `index.css`. Enfin, nous avons ajouté le fichier de script `index.js` en utilisant la balise script. 

Notez que nous avons utilisé l'attribut `defer` pour ajouter le script au HTML. Vous pouvez aborder les performances de chargement du script avec des attributs comme defer et async. 

Si vous êtes nouveau dans ce domaine, vous pouvez consulter cet article : [Performance JavaScript – Comment améliorer la vitesse de la page avec async et defer](https://www.freecodecamp.org/news/javascript-performance-async-defer/).

```html
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Colorify</title>
  <link rel="stylesheet" href="./index.css">
  <script src="./index.js" defer></script>
</head>
```

### La section `<body>`

La section <body> définit ce qui sera visible pour les utilisateurs grâce au processus de rendu du navigateur. Dans le code ci-dessous, nous avons d'abord créé une div de conteneur (une simple balise div avec une classe appelée `container`) qui enveloppe tous les éléments HTML que nous prévoyons de montrer sur la page web.

Tout d'abord, il y a un titre qui rend le nom de notre application. Ensuite, un paragraphe montre un texte sur l'application. Puis nous avons une div avec un id appelé `circleID`. Nous utiliserons cette div pour dessiner un cercle. Enfin, nous avons trois boutons enveloppés dans une autre div.

Remarquez également que chacun des boutons a un gestionnaire de clic associé en utilisant `onClick`.

```html
<div class="container">
    <h1>Colorify</h1>
    <p class="subheading">
      Avec Colorify, nous voulons commencer
      à apprendre JavaScript.
    </p>
    <div class="circle" id="circleID"></div>
    <div class="action">
      <button onclick="paint('red')">Rouge</button>
      <button onclick="paint('green')">Vert</button>
      <button onclick="paint('yellow')">Jaune</button>
    </div>
</div>
```

Exécutons l'application à ce stade et voyons le résultat.

Notez qu'il existe plusieurs façons d'exécuter l'application. La méthode la plus simple consiste à naviguer jusqu'au dossier du projet et à ouvrir le fichier `index.html` dans un navigateur web. Mais cette approche peut ne fonctionner que pour certains scripts. 

L'approche recommandée consiste à exécuter le projet dans le cadre d'un `serveur web`. Vous pouvez utiliser l'extension `Live Server` dans l'éditeur `Visual Studio Code` pour cela.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-35.png)
_L'application - Première étape_

Attendez ! Où est le cercle ? Nous ne voyons pas le cercle parce que nous avons simplement créé un conteneur pour lui mais n'avons pas fourni les éléments de style pour le faire ressembler à un cercle. 

De plus, nous pouvons faire un bien meilleur travail en alignant les éléments HTML sur la page web. Corrigons ces problèmes en utilisant CSS.

## Comment utiliser CSS pour styliser le code

Ouvrez le fichier `index.css` et ajoutez le contenu suivant :

```css
.container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.circle {
  border: 1px solid #000000;
  width: 200px;
  height: 200px;
  border-radius: 50%;
}

.action {
  margin: 10px;
}

button {
  cursor: pointer;
}
```

Nous avons fourni une disposition flex à la div de conteneur extérieure en spécifiant de centrer les éléments à l'intérieur en colonne. Nous avons fourni une hauteur et une largeur égales à la div du cercle pour la faire apparaître comme un carré. Maintenant, nous courbons tous les côtés de la bordure avec la propriété border-radius pour la faire ressembler à un cercle.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-37.png)
_L'application - Deuxième étape_

Maintenant, l'application a bien meilleure allure ! 

Cliquons sur les boutons. Oh ! Nous voyons qu'une erreur est enregistrée dans le panneau de la console. La raison est que nous avons ajouté les gestionnaires de clic aux boutons mais n'avons pas défini la fonction `paint()` à exécuter lorsque l'utilisateur clique sur ces boutons.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-38.png)
_L'application - Troisième étape montrant l'erreur_

Il est temps de définir la fonction `paint()` et de faire fonctionner les choses.

## Comment ajouter un comportement dynamique en utilisant JavaScript

Ouvrez maintenant le fichier `index.js` et copiez-collez le fragment de code suivant :

```js
function paint(color) {
  const circle = document.getElementById('circleID');
  circle.style = `background-color:${color}`;
}
```

Nous avons maintenant défini une fonction `paint()` que nous avons passée aux gestionnaires `onClick` des boutons. Vous avez peut-être remarqué (dans le fichier index.html), nous avons passé les couleurs respectives à la fonction `paint()` lorsque l'utilisateur clique sur un bouton. 

Plongeons dans la méthode `paint()` et comprenons les choses.

* Tout d'abord, nous accédons à l'élément div qui représente le cercle. Nous pouvons identifier l'élément en utilisant la valeur de l'attribut id qui lui est fourni, c'est-à-dire `circleID`. Nous utilisons la méthode DOM appelée `document.getElementById` pour l'obtenir.
* Une fois que nous avons l'élément, nous pouvons ajouter un style. Nous ajoutons un style de couleur de fond basé sur le nom de la couleur passé à la fonction. Notez que nous utilisons ici les expressions de littéraux de gabarit au lieu d'une concaténation de chaînes régulière. [Cet article](https://blog.greenroots.info/what-exactly-is-javascript-tagged-template-literal) vous aidera à comprendre les littéraux de gabarit si vous êtes nouveau dans ce domaine.

C'est tout. Maintenant, chaque fois qu'un utilisateur clique sur un bouton, la couleur respective est ajoutée comme couleur de fond au cercle. Cela fonctionne comme dans l'exemple suivant :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/Screen-Recording-2023-05-09-at-3.24.23-PM.gif)
_L'application - Étape finale_

## Tâche pour vous : Compléter le QUIZ

Très bien, vous avez appris comment créer un projet de changement de couleur en utilisant HTML, CSS et JavaScript pur. Portons cela à un niveau supérieur. Voici une tâche pour vous à compléter.

* Ajoutez un autre bouton appelé `Aléatoire` à côté des boutons existants.
* Lorsque l'utilisateur clique sur le bouton `Aléatoire`, vous devez ajouter une couleur de fond aléatoire au cercle.
* Vous devez réutiliser la fonction `random()` existante que nous avons vue dans le fichier `index.js`.

Si vous complétez cette tâche et souhaitez que je révise votre code, n'hésitez pas à créer un Tweet/un post LinkedIn en utilisant le lien vers votre code en me taguant. Je m'assurerai de le réviser et de commenter.

## Avant de terminer...

C'est tout pour l'instant. J'espère que vous avez trouvé cet article informatif et perspicace. Tout le code source utilisé dans cet article peut être trouvé sur [ce dépôt GitHub](https://github.com/atapas/youtube/tree/main/javascript/projects/colorify).

Restez en contact.

* [ABONNEZ-VOUS](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à ma chaîne YouTube si vous voulez apprendre JavaScript, ReactJS, Node.js, Git, et tout sur le développement web de manière pratique.
* [Suivez-moi sur Twitter](https://twitter.com/tapasadhikary) ou [LinkedIn](https://www.linkedin.com/in/tapasadhikary/) si vous ne voulez pas manquer la dose quotidienne de conseils en développement web et en programmation.
* Consultez mes travaux Open Source sur [GitHub](https://github.com/atapas).
* Suivez-moi sur [Showwcase](https://www.showwcase.com/atapas398) pour un apprentissage basé sur la communauté.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.