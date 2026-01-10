---
title: Comment créer un formulaire réactif avec fonctionnalité de filtre en utilisant
  HTML, CSS et JavaScript
subtitle: ''
author: Kingsley Ubah
co_authors: []
series: null
date: '2021-10-13T20:54:46.000Z'
originalURL: https://freecodecamp.org/news/build-a-responsive-filterable-form-with-css-and-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2021/10/responsiveform.png
tags:
- name: CSS
  slug: css
- name: forms
  slug: forms
- name: HTML
  slug: html
- name: JavaScript
  slug: javascript
seo_title: Comment créer un formulaire réactif avec fonctionnalité de filtre en utilisant
  HTML, CSS et JavaScript
seo_desc: 'Most sites that display a list of data in a table typically have some kind
  of filter functionality implemented. This helps the user filter relevant items based
  on the text they type into the form input.

  In this quick tutorial, we are going to build a...'
---

La plupart des sites qui affichent une liste de données dans un tableau ont généralement une sorte de fonctionnalité de filtre implémentée. Cela aide l'utilisateur à filtrer les éléments pertinents en fonction du texte qu'il saisit dans le champ de formulaire.

Dans ce tutoriel rapide, nous allons créer un tableau filtrable et réactif qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ezgif.com-gif-maker--2-.gif align="left")

*Un tableau réactif filtré par langage de programmation*

Le tableau contiendra une liste de développeurs. Chaque ligne contient un nom, un âge et un langage de programmation. Lorsque l'utilisateur tape dans le champ de saisie, le tableau filtre et retourne les lignes qui correspondent à la valeur entrée.

Au cours de ce processus, vous apprendrez certaines propriétés CSS ainsi que l'accès et la manipulation du DOM avec JavaScript.

Vous pouvez obtenir le code exemple sur [CodePen](https://codepen.io/ubahthebuilder/pen/RwgdLoj).

## Installation

Vous devrez créer trois fichiers simples dans votre dossier de projet. Il s'agit de `index.html` pour le balisage HTML, `styles.css` pour le style et `index.js` pour le script.

```html
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Tableau filtrable</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  
  <script src="index.js" type="text/javascript"></script>
</body>
</html>
```

Assurez-vous de lier votre feuille de style et votre fichier de script comme je l'ai fait dans le HTML ci-dessus.

## Balisage HTML pour le tableau

Ajoutez le balisage suivant à l'intérieur des balises `body` :

```html
<div class="app">
    <input type="text" id="searchInput" placeholder="filtrer les développeurs...">

    <table>
      <thead>
        <tr>
          <th>Nom</th>
          <th>Âge</th>
          <th>Langage</th>
        </tr>
      </thead>
      <tbody id="names">
        <tr>
          <td>Kingsley</td>
          <td>32</td>
          <td>JavaScript</td>
        </tr>
        <tr>
          <td>Samuel</td>
          <td>22</td>
          <td>Python</td>
        </tr>
        <tr>
          <td>Joyce</td>
          <td>28</td>
          <td>Ruby</td>
        </tr>
        <tr>
          <td>Jake</td>
          <td>29</td>
          <td>Python</td>
        </tr>
        <tr>
          <td>Daniel</td>
          <td>40</td>
          <td>JavaScript</td>
        </tr>
        <tr>
          <td>Mary</td>
          <td>21</td>
          <td>C</td>
        </tr>
        <tr>
          <td>David</td>
          <td>26</td>
          <td>JavaScript</td>
        </tr>
        <tr>
          <td>Kelly</td>
          <td>31</td>
          <td>React</td>
        </tr>
        <tr>
          <td>Cleo</td>
          <td>43</td>
          <td>Java</td>
        </tr>
        <tr>
          <td>Peter</td>
          <td>19</td>
          <td>Vue</td>
        </tr>
        <tr>
          <td>George</td>
          <td>59</td>
          <td>Cobol</td>
        </tr>
        <tr>
          <td>James</td>
          <td>29</td>
          <td>JavaScript</td>
        </tr>
        <tr>
          <td>Ethan</td>
          <td>22</td>
          <td>PHP</td>
        </tr>
        <tr>
          <td>Sandra</td>
          <td>29</td>
          <td>R</td>
        </tr>
        <tr>
          <td>Pires</td>
          <td>34</td>
          <td>React Native</td>
        </tr>
        <tr>
          <td>Martha</td>
          <td>30</td>
          <td>React</td>
        </tr>
      </tbody>
    </table>
  </div>
```

Le premier élément est le champ de formulaire. Nous allons l'utiliser pour collecter les données de l'utilisateur.

Ensuite, nous avons le tableau. Le tableau se compose d'un en-tête (`thead`) et d'un corps (`tbody`). L'en-tête a une seule ligne (`tr`) de données, qui est l'en-tête. Le corps a 16 lignes de données, chacune d'entre elles se compose d'un nom, d'un âge et d'un langage de programmation.

Nous enveloppons ces deux éléments dans une balise `div` parente. Ils nous aideront avec l'alignement comme nous le verrons plus tard dans le CSS.

Enregistrez le fichier et ouvrez l'application dans un navigateur web.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/htmltable.png align="left")

*Tableau HTML*

## Comment styliser le tableau avec CSS

Nous allons maintenant appliquer un style au tableau. Tout d'abord, nous définissons les styles de base comme ceci :

```css
@import url("https://fonts.googleapis.com/css2?family=Lato:wght@300&display=swap");

/* Définir aucune marge et aucun remplissage autour du corps. Définir la hauteur pour prendre toute la hauteur de l'écran. Aligner tout au centre, à la fois horizontalement et verticalement */

body {
  margin: 0;
  height: 100vh;
  padding: 0;
  font-family: "lato", sans-serif;
  display: grid;
  justify-content: center;
  align-items: center;
  font-size: 20px;
}

/* Supprimer la bordure et le contour autour de la saisie. Définir la largeur pour prendre toute la largeur du parent et définir la marge en bas */

#searchInput {
  border: none;
  outline: none;
  width: 100%;
  margin-bottom: 20px;
}

/* Lorsque la saisie reçoit le focus, ajouter une bordure bleue en dessous */

#searchInput:focus {
  border-bottom: 2px solid #4575b6;
}
```

Le tableau sera aligné au centre.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/centertable.png align="left")

*Tableau aligné au centre*

Pour rendre le tableau plus beau, nous pouvons utiliser les règles de style suivantes :

```css

/* Définit la largeur du conteneur de tableau (div) à 80 % de la largeur de la fenêtre du navigateur et la hauteur à 100 % de la hauteur de la fenêtre. `vh` et `vw` rendent le tableau réactif car il s'adapte à la taille de l'écran. Définir également une marge de 20px en haut et en bas */

.app {
  width: 80vw;
  height: 100vh;
  margin: 20px 0;
}

/* Fusionner toutes les bordures séparant chaque cellule. Le tableau prend toute la largeur de .app. Définir une ombre grise autour du tableau */
table {
  border-collapse: collapse;
  width: 100%;
  box-shadow: 0 5px 7px gray;
}

/* Définir l'ombre uniquement sur l'en-tête du tableau */
thead {
  box-shadow: 0px 0px 10px gray;
}

/* Ajouter un peu d'espace autour de l'en-tête du tableau. Aligner le texte à gauche et transformer en majuscules */

th {
  padding: 1rem 3rem;
  text-transform: uppercase;
  letter-spacing: 1px;
  text-align: left;
}

/* Ajouter un remplissage sur chaque cellule */
td {
  padding: 0.5rem 3rem;
  font-size: 1rem;
}

/* Créer une couleur alternée (bleue) sur les lignes. Définir le bleu sur toutes les lignes paires (2, 4, 6 ...) */

tr:nth-child(even) {
  background-color: #dee8f5;
}
```

Notre tableau a maintenant un meilleur aspect et il est également réactif.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ezgif.com-gif-maker--3-.gif align="left")

*Le tableau est maintenant réactif*

## Comment implémenter la fonctionnalité de filtre avec JavaScript

Le tableau est pratiquement statique à ce stade. En utilisant JavaScript, nous allons implémenter la logique pour filtrer les noms en fonction de ce que l'utilisateur tape dans le champ de formulaire.

Dans votre fichier de script, définissez une fonction appelée `filter`. Dans les trois premières lignes, nous accédons à la valeur de saisie de l'utilisateur, passons le corps du tableau `<tbody>` dans la variable `names`, et enfin accédons à toutes les lignes du tableau `<tr>` à l'intérieur du `<tbody>`.

Nous convertissons également la valeur en majuscules pour nous assurer que tout est cohérent (l'utilisateur pourrait taper 'j' au lieu de 'J').

```js
  /* Cette fonction vérifiera la saisie de l'utilisateur et, en fonction de celle-ci, masquera ou affichera une ligne particulière */

  function filter() {
    // Accéder à la valeur du texte et aux éléments du DOM 
    let value = document.getElementById("searchInput").value.toUpperCase();
    let names = document.getElementById("names");
    let rows = names.getElementsByTagName("tr");

   // Le code continue
```

Ensuite, nous parcourons chaque tableau. Pour chaque ligne, nous accédons à la dernière colonne (colonne du langage) et obtenons son contenu textuel (valeur réelle).

```js
for (i = 0; i < rows.length; i++) {
    let column = rows[i].getElementsByTagName("td")[2];
    let language = column.textContent;

    rows[i].style.display =
      language.toUpperCase().indexOf(value) > -1 ? "" : "none";
  }
}

document.getElementById("searchInput").addEventListener("keyup", filter);
```

Si la valeur de la chaîne réelle du tableau contient une des valeurs de l'utilisateur à partir de leur saisie, nous affichons cette ligne. Sinon, nous la masquons. Nous avons également utilisé l'opérateur ternaire pour raccourcir l'instruction conditionnelle.

Enfin, nous ajoutons un écouteur d'événement sur la saisie. Chaque fois que la touche est relâchée, le filtre sera invoqué.

Voici le code complet pour cela :

```js
function filter() {
  let value = document.getElementById("searchInput").value.toUpperCase();
  var names = document.getElementById("names");
  var rows = names.getElementsByTagName("tr");

  for (i = 0; i < rows.length; i++) {
    let column = rows[i].getElementsByTagName("td")[2];
    let language = column.textContent;

    rows[i].style.display =
      language.toUpperCase().indexOf(value) > -1 ? "" : "none";
  }
}

document.getElementById("searchInput").addEventListener("keyup", filter);
```

Votre tableau devrait ressembler à ceci à la fin :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/ezgif.com-gif-maker--2--1.gif align="left")

## Conclusion

Avec seulement HTML, CSS et JavaScript, vous pouvez créer des éléments vraiment stylisés avec des fonctionnalités avancées.

J'espère que vous avez appris une ou deux choses de ce tutoriel. Une fois de plus, vous pouvez consulter le code sur CodePen et le modifier comme vous le souhaitez.

Merci d'avoir suivi ce tutoriel.