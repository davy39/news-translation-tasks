---
title: 'Plongez dans JavaScript : Comment créer un convertisseur de couleurs Hex2RGB'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-22T22:17:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-hex2rgb-color-converter-ce32d32afd1f
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca62e740569d1a4ca6e7b.jpg
tags:
- name: CSS
  slug: css
- name: Design
  slug: design
- name: freeCodeCamp.org
  slug: freecodecamp
- name: JavaScript
  slug: javascript
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: 'Plongez dans JavaScript : Comment créer un convertisseur de couleurs Hex2RGB'
seo_desc: 'By Vaibhav Kandwal

  Update (23/07/2019): I have corrected a few grammatical errors and changed app.js
  code a bit by removing the checkBG function.

  In this article, we’ll be creating a web-app that converts color codes between Hexadecimal
  form and RGB ...'
---

Par Vaibhav Kandwal

_Mise à jour (23/07/2019) : J'ai corrigé quelques erreurs grammaticales et modifié un peu le code app.js en supprimant la fonction checkBG._

Dans cet article, nous allons créer une application web qui convertit les codes de couleurs entre la forme hexadécimale et la forme RGB.

Vous pouvez trouver une [démo ici](https://boxdox.github.io/hex2rgb/?source=post_page---------------------------) et le [code source ici](https://github.com/boxdox/hex2rgb?source=post_page---------------------------).

## Structure du projet :

La structure du projet est assez simple.

1. `index.html` : Contient la structure de l'application.
2. `style.css` : Style la page.
3. `app.js` : Contient tout le code magique.

## Idée :

Voici la liste des choses que je voulais que cette application fasse :

1. Chaque fois que quelque chose est tapé dans un champ de texte pour hex, l'application doit vérifier si la couleur est valide. Si c'est le cas, la convertir en RGB, la définir comme arrière-plan et ensuite placer la valeur RGB dans le champ de texte RGB et vice versa.
2. Si un code de couleur hex court est tapé dans le champ de texte, l'étendre lorsque le champ de texte perd le focus (l'utilisateur clique en dehors de la zone de texte).
3. Ajouter automatiquement le symbole '#' à l'entrée hex.

## Commençons !

## index.html

```html
<!DOCTYPE html>
<html lang="fr">

<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <title>Convertisseur Hex vers RGB</title>
  <link rel="stylesheet" href="style.css">
</head>

<body>
  <div class="head">
    HEX &lt;--&gt; RGB
  </div>
  <div id="content">
    <input type="text" id="hex" placeholder="hex">
    <img id="hexError" class="hidden" src="data:image/svg+xml;utf8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzYgNTEyIj48cGF0aCBkPSJNNTY5LjUxNyA0NDAuMDEzQzU4Ny45NzUgNDcyLjAwNyA1NjQuODA2IDUxMiA1MjcuOTQgNTEySDQ4LjA1NGMtMzYuOTM3IDAtNTkuOTk5LTQwLjA1NS00MS41NzctNzEuOTg3TDI0Ni40MjMgMjMuOTg1YzE4LjQ2Ny0zMi4wMDkgNjQuNzItMzEuOTUxIDgzLjE1NCAwbDIzOS45NCA0MTYuMDI4ek0yODggMzU0Yy0yNS40MDUgMC00NiAyMC41OTUtNDYgNDZzMjAuNTk1IDQ2IDQ2IDQ2IDQ2LTIwLjU5NSA0Ni00Ni0yMC41OTUtNDYtNDZ6bS00My42NzMtMTY1LjM0Nmw3LjQxOCAxMzZjLjM0NyA2LjM2NCA1LjYwOSAxMS4zNDYgMTEuOTgyIDExLjM0Nmg0OC41NDZjNi4zNzMgMCAxMS42MzUtNC45ODIgMTEuOTgyLTExLjM0Nmw3LjQxOC0xMzZjLjM3NS02Ljg3NC01LjA5OC0xMi42NTQtMTEuOTgyLTEyLjY1NGgtNjMuMzgzYy02Ljg4NCAwLTEyLjM1NiA1Ljc4LTExLjk4MSAxMi42NTR6Ii8+PC9zdmc+" />
    </br>
    <input type="text" id="rgb" placeholder="rgb">
    <img id="rgbError" class="hidden" src="data:image/svg+xml;utf8;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA1NzYgNTEyIj48cGF0aCBkPSJNNTY5LjUxNyA0NDAuMDEzQzU4Ny45NzUgNDcyLjAwNyA1NjQuODA2IDUxMiA1MjcuOTQgNTEySDQ4LjA1NGMtMzYuOTM3IDAtNTkuOTk5LTQwLjA1NS00MS41NzctNzEuOTg3TDI0Ni40MjMgMjMuOTg1YzE4LjQ2Ny0zMi4wMDkgNjQuNzItMzEuOTUxIDgzLjE1NCAwbDIzOS45NCA0MTYuMDI4ek0yODggMzU0Yy0yNS40MDUgMC00NiAyMC41OTUtNDYgNDZzMjAuNTk1IDQ2IDQ2IDQ2IDQ2LTIwLjU5NSA0Ni00Ni0yMC41OTUtNDYtNDYtNDZ6bS00My42NzMtMTY1LjM0Nmw3LjQxOCAxMzZjLjM0NyA2LjM2NCA1LjYwOSAxMS4zNDYgMTEuOTgyIDExLjM0Nmg0OC41NDZjNi4zNzMgMCAxMS42MzUtNC45ODIgMTEuOTgyLTExLjM0Nmw3LjQxOC0xMzZjLjM3NS02Ljg3NC01LjA5OC0xMi42NTQtMTEuOTgyLTEyLjY1NGgtNjMuMzgzYy02Ljg4NCAwLTEyLjM1NiA1Ljc4LTExLjk4MSAxMi42NTR6Ii8+PC9zdmc+" />
  </div>
  <script src="app.js"></script>
</body>

</html>
```

Nous avons créé deux champs de texte avec les identifiants 'hex' et 'rgb' respectivement. À côté de chaque entrée se trouve une icône SVG pour l'erreur, qui a une classe de hidden, par défaut.

## style.css

```css
:root {
     --color: rgba(255,255,255,0.9);
     --tweet: white;
}
 * {
     margin: 0;
     padding: 0;
     box-sizing: border-box;
}
 ::placeholder {
     color: var(--color)!important;
}
 body {
     padding: 50px;
     width: 100vw;
     height: 100vh;
     display: flex;
     align-items: center;
     justify-content: center;
     background-color: #28a745;
     font-family: -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Oxygen-Sans,Ubuntu,Cantarell,"Helvetica Neue",sans-serif;
}
 .head {
     position: absolute;
     top: 30px;
     text-align: center;
     color: var(--tweet);
     font-size: 3rem;
     border-bottom: 2px solid var(--tweet);
}
 #content {
     display: block;
}
 input {
     color: var(--color)!important;
     margin: 1rem 0;
     width: 400px;
     border: none;
     border-bottom: 1px solid var(--color);
     font-size: 2.5rem;
     background-color: transparent;
}
 input:focus {
     outline: none;
}
 img {
     width: 24px;
}
 .hidden {
     visibility: hidden;
     opacity: 0.8;
}
 .dark {
     --color: rgba(0,0,0,0.75);
     --tweet: rgba(0,0,0,0.95);
}
 @media only screen and (max-width: 560px){
     #content input {
         margin: 0.75rem 0;
         width: 90%;
         font-size: 1.875rem;
    }
     #content img {
         width: 16px;
    }
     .head {
         font-size: 2rem;
    }
}

```

Voici une mise en page de base pour rendre le balisage un peu meilleur. Nous avons défini deux classes ici, `.hidden` et `.dark`. `.hidden` est utilisé pour masquer/afficher l'icône SVG d'erreur et `.dark` est pour changer la couleur du texte en fonction de la couleur de l'arrière-plan. Par défaut, j'ai défini le texte en couleur foncée (pour les arrière-plans clairs).

## app.js

Voici la partie magique. Je vais décomposer le code en morceaux :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_vkFx7EZWK1gr8yecEb2UpQ.png)

Tout d'abord, nous avons défini des variables qui ciblent les entrées avec les identifiants 'hex' et 'rgb'. Ensuite, nous avons des fonctions pour vérifier si l'entrée Hex/RGB est valide ou non. Elles utilisent une configuration regex de base et retournent un booléen. Si vous êtes intimidé par elles, je vous recommande d'essayer ce [Tutoriel Regex](http://regextutorials.com/?source=post_page---------------------------).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_US53im4jHtPwS30i_VpSQA.png)

Ici, nous avons écrit une fonction d'analyse appelée `modifyHex` qui vérifie si l'entrée hex a une longueur de 4 caractères ; c'est-à-dire, contient '#' et est en notation abrégée (par exemple, #333) et remplace le '#' par un caractère vide. Ensuite, elle vérifie si la longueur est maintenant de 3 et l'étend à 6 caractères de long (par exemple, #123 = #112233).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_OkqZufTfvTtTH4wdXm44nw--2-.png)

Nous avons défini deux fonctions qui convertissent hex en rgb et vice versa. Voici une décomposition étape par étape pour `hexToRgb` (ce processus est écrit en forme développée pour une meilleure compréhension) :

1. Définir un tableau vide pour stocker le résultat.
2. Remplacer le symbole '#', s'il existe, et si la longueur n'est pas égale à 6 (c'est-à-dire, la version abrégée), appeler la fonction `modifyHex` ci-dessus et l'étendre.
3. De manière très basique, hex vers rgb fonctionne en convertissant le code hex (en base 16) en code rgb (en base 10). Chaque deux caractères dans le code hex représentent une valeur dans le code de couleur rgb. Par exemple dans #aabbcc, le rouge est (aa en base 10), le vert est (bb en base 10) et le bleu est (cc en base 10). Donc dans la fonction, nous découpons la valeur hex, la convertissons en base 10 en utilisant `parseInt`, puis la stockons dans le tableau défini.
4. Enfin, nous retournons la chaîne de sortie en joignant le tableau ci-dessus.

Pour la fonction `rgbToHex` (ceci est écrit avec une logique plus courte) :

1. Nous utilisons directement une regex pour extraire uniquement les valeurs numériques — c'est-à-dire, rgb(123,21,24) retournera 123,21,24.
2. Ensuite, nous utilisons une fonction map pour retourner un nouveau tableau, qui convertit le nombre en base 16, puis remplit la valeur.

La regex que nous avons utilisée ci-dessus retourne des données de type 'string'. Pour les convertir en Base 16, nous devons utiliser la méthode `toString()`, avec un paramètre de '16'.

Maintenant, la méthode `toString()` est applicable uniquement aux types de données numériques, donc nous utilisons `parseInt` pour d'abord convertir chaque élément du tableau en un nombre, puis utilisons `toString(16)` pour le convertir en forme hexadécimale et enfin ajoutons un remplissage pour le rendre exactement de 2 caractères de long. Le remplissage est nécessaire, si vous avez quelque chose comme '14', que vous voulez convertir en hexadécimal, il retournera 'e'. Mais le code de couleur hex a besoin de 2 caractères pour chaque partie, donc le remplissage est requis, ce qui le rend '0e'.

_Note :_ `_padStart` _est une fonctionnalité ES8, qui peut ne pas être supportée dans tous les navigateurs. Pour garder ce tutoriel simple, je ne l'ai pas transpilé en ES5._

3. Enfin, nous retournons le tableau résultant en le joignant et en le convertissant en majuscules.


![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_GS58ex_1iIswypXdZjaoHA.png)

La fonction `errorMark()` est utilisée pour afficher ou masquer l'icône SVG d'erreur. Elle transmet simplement le contenu de l'entrée (`hex.value` et `rgb.value`) à travers leurs fonctions de vérification respectives et utilise le booléen retourné pour ajouter/supprimer la classe `.hidden`.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_05piBJK1b3tsaEdxkjK8JA.png)

Maintenant, nous définissons une fonction qui prend la couleur de l'arrière-plan et détermine ensuite si elle est foncée ou claire (j'ai obtenu ce code de StackOverflow). Elle multiplie les valeurs de couleur individuelles avec des nombres calculés et retourne 'black' ou 'white'. J'utilise ensuite une autre fonction pour changer la couleur du texte en ajoutant/supprimant la classe `.dark`.

## Ajout d'écouteurs d'événements :

![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_wAKHCvq61Bw83rkTNqZcZw.png)

Enfin, nous connectons toutes les fonctions en ajoutant des écouteurs d'événements.

Tout d'abord, nous ajoutons un événement `keyup` à l'entrée `hex`. Cet événement est déclenché chaque fois qu'une touche est relâchée. Voici la décomposition du processus :

1. Vérifier si le code d'entrée est valide et l'étendre s'il est en notation abrégée.
2. Définir la couleur de l'arrière-plan du corps sur la valeur d'entrée.
3. Vérifier le contraste de la couleur et changer la couleur du texte en conséquence.
4. Appeler la fonction de conversion et placer la couleur convertie dans le champ d'entrée RGB.

L'autre écouteur d'événement que nous avons utilisé est `blur`. Il est déclenché chaque fois que l'entrée perd le 'focus', ou en termes profanes, chaque fois que vous cliquez/tapotez en dehors de l'élément d'entrée, `blur` est déclenché. Donc, c'est bien de modifier l'entrée hex !

Donc, nous vérifions si la couleur hex est valide ou non, puis nous l'étendons si elle est courte, et enfin nous ajoutons un '#' s'il n'existe pas. Notez que nous vérifions si les index 0 et 1 contiennent '#'. Cela est fait pour que la fonction n'ajoute pas '#' deux fois.


![Image](https://www.freecodecamp.org/news/content/images/2019/07/1_TZODzwqCrGnQCARdrzarBw.png)

Le même écouteur d'événement `keyup` est ajouté à l'entrée RGB et il suit également la même série d'étapes que l'écouteur d'événement hex.

Enfin, nous avons ajouté un écouteur d'événement `keyup` à l'ensemble du document, c'est-à-dire qu'il sera déclenché pour l'un des deux éléments d'entrée. Dans celui-ci, nous appelons la fonction `errorMark`, qui ajoute l'icône d'erreur, en cas d'erreur, ou la supprime si tout est valide.

Voici le code final pour `app.js` :

```js
const hex = document.getElementById("hex");
const rgb = document.getElementById("rgb");

// Fonctions de vérification
function checkHex(hex) {
  const hexRegex = /^[#]*([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$/i
  if (hexRegex.test(hex)) {
    return true;
  }
}

function checkRgb(rgb) {
  const rgbRegex = /([R][G][B][A]?[(]\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\s*,\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\s*,\s*([01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(\s*,\s*((0\.[0-9]{1})|(1\.0)|(1)))?[)])/i
  if (rgbRegex.test(rgb)) {
    return true
  }
}
// Fonction d'analyse
function modifyHex(hex) {
  if (hex.length == 4) {
    hex = hex.replace('#', '');
  }
  if (hex.length == 3) {
    hex = hex[0] + hex[0] + hex[1] + hex[1] + hex[2] + hex[2];
  }
  return hex;
}

// Fonctions de conversion
function hexToRgb(hex) {
  let x = [];
  hex = hex.replace('#', '')
  if (hex.length != 6) {
    hex = modifyHex(hex)
  }
  x.push(parseInt(hex.slice(0, 2), 16))
  x.push(parseInt(hex.slice(2, 4), 16))
  x.push(parseInt(hex.slice(4, 6), 16))
  return "rgb(" + x.toString() + ")"
}

function rgbToHex(rgb) {
  let y = rgb.match(/\d+/g).map(function(x) {
    return parseInt(x).toString(16).padStart(2, '0')
  });
  return y.join('').toUpperCase()
}

// Fonctions d'aide
function addPound(x) {
  return '#' + x;
}

// Fonction pour ajouter une croix en cas d'erreur
function errorMark() {
  if (checkHex(hex.value)) {
    document.getElementById('hexError').classList.add('hidden');
  } else {
    document.getElementById('hexError').classList.remove('hidden');
  }
  if (checkRgb(rgb.value)) {
    document.getElementById('rgbError').classList.add('hidden');
  } else {
    document.getElementById('rgbError').classList.remove('hidden');
  }
}

// Trouver le ratio de contraste pour changer la couleur du texte. Merci https://stackoverflow.com/a/11868398/10796932
function getContrastYIQ(hexcolor) {
  if (checkHex(hexcolor)) {
    hexcolor = hexcolor.replace("#", '')
  } else {
    hexcolor = rgbToHex(hexcolor)
  }
  var r = parseInt(hexcolor.substr(0, 2), 16);
  var g = parseInt(hexcolor.substr(2, 2), 16);
  var b = parseInt(hexcolor.substr(4, 2), 16);
  var yiq = ((r * 299) + (g * 587) + (b * 114)) / 1000;
  return (yiq >= 128) ? document.body.classList.add('dark') : document.body.classList.remove('dark')
}

// Ajout d'écouteurs d'événements
hex.addEventListener('keyup', function() {
  let color = hex.value
  if (checkHex(color)) {
    color = modifyHex(color);
    document.body.style.backgroundColor = addPound(color);
    getContrastYIQ(color)
    rgb.value = hexToRgb(color);
  }
})
hex.addEventListener('blur', function() {
  if (checkHex(hex.value)) {
    hex.value = modifyHex(hex.value)
    if (hex.value[1] != '#') {
      if (hex.value[0] != '#') {
        hex.value = addPound(hex.value);
      }
    }
  }
})
rgb.addEventListener('keyup', function() {
  let color = rgb.value
  if (checkRgb(color)) {
    hex.value = color = addPound(rgbToHex(color))
    document.body.style.backgroundColor = color;
    getContrastYIQ(color)
  }
})
document.addEventListener('keyup', function() {
  errorMark();
})
```

# Conclusion

Voilà ! Je sais que le code n'est pas parfait et peut être refactorisé, mais bon, ce n'est qu'un début. Si vous voulez améliorer ce code, vous pouvez aller de l'avant et ouvrir une PR sur mon [dépôt github](https://github.com/boxdox/hex2rgb?source=post_page---------------------------).

Bon codage !