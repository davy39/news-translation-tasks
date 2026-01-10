---
title: Comment créer une application de chiffrement de photos en utilisant la stéganographie
subtitle: ''
author: Houssein Badra
co_authors: []
series: null
date: '2023-08-23T21:06:02.000Z'
originalURL: https://freecodecamp.org/news/build-a-photo-encryption-app
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--122-.png
tags:
- name: encryption
  slug: encryption
- name: information security
  slug: information-security
seo_title: Comment créer une application de chiffrement de photos en utilisant la
  stéganographie
seo_desc: "In this digital age, data flows freely across networks and devices. So\
  \ protecting sensitive information from unauthorized access is crucial. That's where\
  \ encryption comes in. \nEncryption involves converting plain, readable data into\
  \ an incomprehensib..."
---

À l'ère numérique, les données circulent librement à travers les réseaux et les appareils. Il est donc crucial de protéger les informations sensibles contre les accès non autorisés. C'est là que le chiffrement intervient. 

Le chiffrement consiste à convertir des données lisibles en une forme incompréhensible. Il est également essentiel d'avoir un moyen de convertir les données en une forme lisible, sinon tout le processus n'a pas de sens et n'est pas utile.

Il existe divers algorithmes de chiffrement populaires, chacun avec ses forces et ses faiblesses. Comprendre comment ces algorithmes fonctionnent est essentiel pour les programmeurs, car ils doivent choisir le plus approprié pour leurs applications. 

Dans cet article, nous allons créer une application où les utilisateurs peuvent chiffrer des images et également inverser le processus en utilisant HTML, CSS et JavaScript. 

Vous apprendrez à travailler avec des images et à les chiffrer. L'approche que nous allons utiliser consiste à cacher une image dans une autre, ce qui s'appelle la **stéganographie**. Vous pratiquerez également quelques compétences de base en développement web. Ce sera amusant, c'est sûr !

### Voici ce que nous allons couvrir :

* Comment les images sont représentées sur votre ordinateur
* Comment créer l'algorithme de chiffrement 
* Comment créer l'algorithme de déchiffrement
* Code de l'application de chiffrement de photos

## Comment les images sont représentées sur votre ordinateur

Comprendre la manière dont les images sont stockées est crucial avant de se lancer dans leur chiffrement. 

Les images sont représentées sur les ordinateurs à l'aide d'une combinaison de pixels. Un pixel est la plus petite unité d'une image et sert de bloc de construction pour afficher des visuels sur les écrans numériques. 

En mémoire, une image est un tableau de pixels. Mais maintenant, vous vous demandez probablement, qu'est-ce qu'un pixel ?

Un pixel se voit attribuer une valeur de couleur spécifique qui détermine son apparence. Les valeurs de couleur sont généralement représentées à l'aide d'une combinaison de trois couleurs primaires : rouge, vert et bleu, communément appelées RVB. 

Chaque canal de couleur est représenté par une valeur numérique, allant de 0 à 255, qui détermine l'intensité de cette couleur dans le pixel. 

Par exemple :

* (0, 0, 0) représente le noir (absence de toutes les couleurs)
* (255, 255, 255) représente le blanc (intensité maximale de toutes les couleurs)
* (255, 0, 0) représente le rouge pur (intensité maximale de rouge, absence de vert et de bleu)
* (0, 255, 0) représente le vert pur (intensité maximale de vert, absence de rouge et de bleu)
* (0, 0, 255) représente le bleu pur (intensité maximale de bleu, absence de rouge et de vert)

En combinant différentes intensités de rouge, de vert et de bleu, nous pouvons représenter une large gamme de couleurs. Ces informations de couleur pour chaque pixel sont stockées en mémoire, formant une image numérique. Par exemple, pour obtenir du jaune, nous pouvons combiner le rouge et le vert - (255, 255, 0) représente un pixel jaune.

## Comment utiliser l'algorithme de chiffrement

L'idée clé derrière l'algorithme que nous allons utiliser est qu'il utilise 2 images : l'image que nous voulons chiffrer et une image qui jouera le rôle de masque utilisé pour cacher l'image que nous voulons chiffrer. Nous allons donc combiner ces deux images de manière à cacher notre image principale et à permettre son extraction.

Puisqu'une image est composée de pixels, ce qui fonctionne pour un seul pixel fonctionne pour une image entière. Nous allons discuter de la manière dont nous allons combiner 2 pixels de manière à en cacher un et à permettre d'inverser le processus.

Maintenant, la partie intéressante : si nous regardons les nombres de 0 à 255, ils peuvent tous s'écrire comme suit : a * 16 + b. Par exemple, 241 peut s'écrire 15 * 16 + 1. Mais pourquoi faisons-nous cela ? 

Nous allons utiliser cela pour diviser chaque pixel en deux parties : premièrement la partie a * 16 et deuxièmement b. La première partie contient beaucoup plus d'informations que la seconde, puisque lorsque le degré de couleur augmente, son intensité augmente également. Par exemple, un pixel (245, 137, 200) peut être divisé en (240, 128, 192) et (5, 9, 8). 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--114-.png)
_Division de l'image_

Maintenant, en comparant le pixel de haute valeur et l'original, vous pouvez voir clairement que l'utilisation du pixel de haute valeur au lieu de l'original ne va pas changer beaucoup l'information que le pixel original contient.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--115-.png)
_Comparaison d'un pixel de haute valeur et des valeurs d'un pixel original_

Maintenant, nous allons utiliser deux pixels : un que nous allons chiffrer (le pixel cible), et un dans lequel nous allons cacher le pixel cible (le pixel de chiffrement), qui peut être aléatoire comme nous le verrons plus tard. 

Tout d'abord, nous allons obtenir le pixel de haute valeur de nos pixels cible et de chiffrement. Ensuite, pour le pixel que nous essayons de chiffrer, nous diviserons chaque degré de nombre par 16. 

Par exemple, si le pixel cible original était (245, 137, 200), alors le pixel de haute valeur sera (240, 128, 192) qui deviendra (15, 8, 12) après avoir appliqué une division par 16. 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--121-.png)
_Obtention des valeurs initiales et application de la division_

Maintenant, nous avons deux nouveaux pixels : le pixel de haute valeur du pixel de chiffrement, et notre pixel de haute valeur du pixel cible qui a été divisé par 16. 

Enfin, pour obtenir un pixel chiffré, nous allons additionner les valeurs de ces deux pixels pour obtenir ce que nous cherchons. 

Prenons, par exemple, (26, 98, 234) et (245, 137, 200) comme nos pixels de chiffrement et cible, respectivement. Obtenons d'abord les pixels de haute valeur. Nous aurons (16, 96, 224) et (240, 128, 192), respectivement. 

Maintenant, divisez le pixel de haute valeur du pixel cible par 16 et vous aurez (15, 8, 12). Maintenant, additionnez ces deux valeurs et vous obtiendrez (31, 104, 236). Et c'est notre pixel chiffré. 

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--118-.png)
_Image chiffrée_

Maintenant, vous savez comment chiffrer un pixel. En appliquant cela à tous les pixels d'une image, nous obtiendrons une image chiffrée. 

Pour rendre cela plus clair, nous allons cacher une image de Quincy Larson jouant de la guitare dans le logo de freeCodeCamp 😂.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--126-.png)
_Image montrant comment nous avons pu cacher l'image de Quincy Larson dans le logo de freeCodeCamp_

Pour que cela fonctionne, nous avons besoin de deux images : celle que nous devons chiffrer et une image aléatoire à utiliser comme image de chiffrement. De plus, les deux images doivent avoir les mêmes dimensions pour obtenir le même nombre de pixels. 

La raison pour laquelle nous utilisons une image aléatoire pour cacher notre image est de la faire ressembler à une image très aléatoire qui ne rendra personne suspect.

## Comment utiliser l'algorithme de déchiffrement

Maintenant, nous avons besoin d'un moyen d'inverser le processus, pour extraire le pixel cible d'un pixel chiffré. Ensuite, nous aurons accompli notre objectif.

Comme nous l'avons fait précédemment en combinant 2 pixels pour obtenir un pixel chiffré, nous allons diviser le pixel chiffré pour obtenir notre cible.

Chaque pixel peut être divisé en deux parties : la partie de haute valeur (a * 16) et la partie de basse valeur (b). Maintenant, nous nous intéressons à la partie b puisque elle provient de notre pixel cible. Nous devons donc extraire la partie b d'un pixel chiffré.

Nous pouvons faire cela facilement en mappant chaque nombre avec son reste correspondant de la division par 16. Nous pouvons faire cela en utilisant l'opérateur modulo **%** qui est un opérateur mathématique pour obtenir le reste de la division d'un nombre par un autre. Par exemple, 241 % 16 est 1 puisque 241 est égal à 15 * 16 + 1.

En prenant (31, 104, 236) et en appliquant le modulo, nous obtiendrons (15, 8, 12). Comme discuté précédemment, un pixel chiffré est la somme du pixel de haute valeur de notre pixel de chiffrement ou du pixel de masque et du pixel de haute valeur de notre cible divisé par 16. Après l'application du modulo, la valeur restante est le pixel de haute valeur de notre cible divisé par 16.

Maintenant, multipliez chaque nombre par 16 et vous obtiendrez exactement (240, 128, 192) qui est le pixel de haute valeur de notre pixel cible.

![Image](https://www.freecodecamp.org/news/content/images/2023/08/Screenshot--117-.png)
_Déchiffrement_

Maintenant, comme vous pouvez le voir, la **stéganographie** implique une petite perte d'informations de chaque pixel cible, mais ce n'est pas grave car vous pouvez voir que cela n'a pas beaucoup d'importance dans l'apparence de l'image finale.

## Code de l'application de chiffrement de photos

Et maintenant, puisque notre boîte à outils est prête, codons cette application de chiffrement d'images. Tout le code est disponible dans ce [dépôt GitHub](https://github.com/HousseinBadra/image-Encryption.git). Le code lui-même est très simple. 

Tout d'abord, créez trois fichiers : un fichier HTML, un fichier CSS et un fichier JavaScript. 

Pour le fichier HTML, nous avons juste besoin d'un canevas où nous pouvons voir l'image résultante. Nous avons également besoin de deux entrées de type fichier pour pouvoir télécharger nos images cible et de chiffrement. Et enfin, nous avons besoin d'un bouton pour sauvegarder notre image chiffrée. 

Nous allons également utiliser une petite bibliothèque pour gérer les images créée par l'Université Duke, nous devons donc inclure une balise de script à la fin du corps pour cela.

```.html
<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Application de chiffrement d'images</title>
    <link rel="stylesheet" href="index.css">
</head>
<body>
    <div class="container">
       <canvas></canvas>
    </div>
    <div class="input-container">
        <label for="Target">Télécharger l'image cible</label>
        <input type="file" id="target" mltiple='false' accept='image/*'>
    </div>
    <div class="input-container">
        <label for="Encryption">Télécharger l'image de chiffrement</label>
        <input type="file" id="encryption" multiple='false' accept='image/*'>
    </div>
    <button>Sauvegarder l'image</button>
    <script src='https://www.dukelearntoprogram.com/course1/common/js/image/SimpleImage.js'></script>
    <script src="index.js" type="text/javascript"></script>
</body>
</html>
```

Le CSS est également simple. Nous allons donner à la div enveloppant le canevas une largeur et une hauteur de 300px, au canevas une largeur et une hauteur de 100%, et il aura une bordure noire. Maintenant, les balises div enveloppant nos entrées auront une légère marge de 10px en haut, et c'est tout.

```.css
.container{
  width:300px;
  height: 300px;
}

canvas{
  width:100%;
  height:100%;
  border:1px solid black;
}

.input-container{
    margin-top: 10px;
}
```

Maintenant, pour le fichier JavaScript. Nous allons d'abord sélectionner les deux entrées, le canevas et le bouton de sauvegarde, et les stocker dans quatre variables différentes. Ensuite, nous allons définir la largeur et la hauteur du canevas à 300px avec JavaScript pour éviter tout problème futur. Et enfin, nous allons définir deux variables, target et encryption, pour stocker nos images de chiffrement et cible.

```.js
const canvas = document.querySelector("canvas");
const targetInput = document.querySelector("#target");
const encryptionInput = document.querySelector("#encryption");
const saveButton = document.querySelector("button");
let target;
let encryption;

canvas.width = 300;
canvas.height = 300;
```

Maintenant, nous devons stocker les images de chiffrement et cible lors du téléchargement par l'utilisateur dans les deux variables que nous avons créées précédemment. Définissez également l'événement **onClick** de notre bouton de sauvegarde sur une fonction appelée **save** que nous allons créer ensuite. Enfin, nous allons créer une fonction qui prend un nombre comme argument et retourne sa valeur élevée comme discuté dans la section de l'algorithme de chiffrement.  

```.js
targetInput.onchange = (e) => {
  const img = new SimpleImage(targetInput);
  img.setSize(300, 300);
  target = img;
};

encryptionInput.onchange = (e) => {
  const img = new SimpleImage(encryptionInput);
  img.setSize(300, 300);
  encryption = img;
};

saveButton.onclick = save;

function getValue(x) {
  return x - (x % 16);
}
```

Il ne reste plus qu'à créer la fonction save. Tout d'abord, nous allons créer un nouvel objet image avec des dimensions de 300 * 300. Une image avec ces dimensions aura 90000 pixels. Tous ont des coordonnées x et y de 0-299, puisque l'indexation commence à 0 dans les tableaux. Boucler de 0 à 300 deux fois nous permettra d'obtenir toutes les coordonnées possibles, ce qui signifie tous les pixels.

Maintenant, pour chaque coordonnée, nous allons utiliser le pixel correspondant de notre chiffrement, de la cible et de la nouvelle image créée. Maintenant, nous pouvons définir chaque pixel de notre nouvelle image créée à la somme du pixel de haute valeur du pixel de chiffrement et du pixel de haute valeur de notre cible divisé par 16.

Maintenant, nous allons dessiner le nouveau pixel créé sur le canevas. Et nous aurons besoin d'obtenir l'URL de l'image dessinée dans le canevas. Nous allons appliquer une petite modification à l'URL, sinon cela ne fonctionnera pas car nous serons bloqués par le navigateur pour des raisons de sécurité.

Enfin, naviguez vers cette URL en définissant l'emplacement de la fenêtre sur cette URL. Ensuite, l'image chiffrée sera téléchargée.

```.js
function save() {
  const img = new SimpleImage(300, 300);
  for (let i = 0; i < 300; i++) {
    for (let j = 0; j < 300; j++) {
      const targetPixel = target.getPixel(i, j);
      const encryptionPixel = encryption.getPixel(i, j);
      const pixel = img.getPixel(i, j);
      pixel.setRed(
        getValue(targetPixel.getRed()) / 16 + getValue(encryptionPixel.getRed())
      );
      pixel.setGreen(
        getValue(targetPixel.getGreen()) / 16 +
          getValue(encryptionPixel.getGreen())
      );
      pixel.setBlue(
        getValue(targetPixel.getBlue()) / 16 +
          getValue(encryptionPixel.getBlue())
      );
    }
  }
  img.drawTo(canvas);
  let url = canvas
    .toDataURL("image/png")
    .replace("image/png", "image/octet-stream");
  window.location.href = url;
}
```

Et c'est tout pour le code 😇.

## Conclusion

Dans cet article, nous avons appris un algorithme simple pour le chiffrement d'images. Les algorithmes modernes sont beaucoup plus robustes, car ils utilisent des techniques comme la multiplication de matrices pour obtenir des algorithmes de hachage solides, mais ils sont très complexes et nécessitent beaucoup plus de temps et de connaissances mathématiques que celui-ci. 

Si vous trouvez ce contenu agréable, [suivez-moi sur LinkedIn](https://www.linkedin.com/in/houssein-badra-943879214/) car j'y poste du bon contenu 😉.