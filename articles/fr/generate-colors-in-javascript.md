---
title: Comment générer des couleurs en JavaScript
subtitle: ''
author: Rufai Mustapha
co_authors: []
series: null
date: '2023-03-07T22:11:32.000Z'
originalURL: https://freecodecamp.org/news/generate-colors-in-javascript
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/colotd--2-.jpg
tags:
- name: JavaScript
  slug: javascript
seo_title: Comment générer des couleurs en JavaScript
seo_desc: "In this article, we'll build a random color generator in JavaScript. Along\
  \ the way, we will explore general topics in programming like functions and randomization.\
  \ \nWe will build a project called Change The Background Color to illustrate these\
  \ concep..."
---

Dans cet article, nous allons créer un générateur de couleurs aléatoires en JavaScript. En cours de route, nous explorerons des sujets généraux en programmation comme les fonctions et la randomisation. 

Nous allons construire un projet appelé _Changer la couleur de fond_ pour illustrer ces concepts. Vous pouvez voir la démonstration [ici](http://rufai.github.io/buildingx/random_bg_color.html). 

Dans ce tutoriel, nous allons :

* apprendre comment les ordinateurs comprennent le concept de couleurs
* apprendre le système hexadécimal et son utilité pour les ordinateurs
* apprendre à séparer les préoccupations dans votre code
* explorer le monde des boucles, des tableaux et des fonctions tels qu'utilisés en JavaScript
* utiliser cette nouvelle connaissance pour générer des couleurs en hexadécimal
* introduire les événements en JavaScript
* cliquer sur un bouton dans notre code HTML pour appeler nos fonctions
* changer le style _background-color_ du body lorsque le bouton est cliqué

Cet article devrait être accessible à toute personne familiarisée avec les variables et leur création dans n'importe quel langage de programmation.  

## Ce que nous allons couvrir

1. Comment les ordinateurs comprennent les couleurs
2. Qu'est-ce que le système hexadécimal ?
3. Comment l'hexadécimal est utilisé dans les espaces colorimétriques
4. Comment générer des couleurs avec les hexadécimaux

## Comment les ordinateurs comprennent les couleurs

Les écrans d'ordinateur utilisent de minuscules points appelés pixels pour afficher des couleurs en mélangeant de la lumière rouge, verte et bleue. 

Pour interpréter et manipuler les couleurs, les ordinateurs utilisent des modèles mathématiques appelés espaces colorimétriques. En convertissant les couleurs dans un espace colorimétrique spécifique, les ordinateurs peuvent les modifier et les ajuster avant de les afficher à l'écran.   
  
Il existe de nombreux types différents d'espaces colorimétriques, chacun avec sa propre façon de représenter les couleurs. Voici quelques exemples :

1. RVB (Rouge, Vert, Bleu) : C'est l'espace colorimétrique le plus courant utilisé en infographie, et il représente les couleurs en mélangeant différentes quantités de composantes rouges, vertes et bleues.
2. CMJN (Cyan, Magenta, Jaune, Noir) : C'est un espace colorimétrique utilisé en impression, où les couleurs sont créées en superposant des points de différentes couleurs les uns sur les autres.
3. TSL (Teinte, Saturation, Luminosité) : Cet espace colorimétrique représente les couleurs en fonction de leur teinte (quelle couleur elles sont), de leur saturation (à quel point la couleur est intense) et de leur luminosité (à quel point la couleur est claire ou foncée).
4. LAB (Luminosité, A, B) : Cet espace colorimétrique est utilisé en imagerie numérique et représente les couleurs en fonction de leur luminosité, ainsi que de leur position sur deux axes de couleur : A (du vert au rouge) et B (du bleu au jaune).
5. XYZ : Cet espace colorimétrique représente les couleurs en fonction de la quantité de lumière qu'elles réfléchissent ou émettent, et est souvent utilisé dans les applications de correspondance des couleurs.

## Qu'est-ce que le système hexadécimal ?

L'hexadécimal (ou simplement "hex") est un système de numération en base 16 qui est couramment utilisé en informatique et en électronique numérique. 

Dans ce système, les nombres sont représentés à l'aide de 16 chiffres : les chiffres décimaux réguliers de 0 à 9, plus les lettres A à F qui représentent les valeurs de 10 à 15.

``` [0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F]```

L'hexadécimal est souvent utilisé en informatique car il fournit une manière compacte et facile à lire de représenter les nombres binaires. Chaque chiffre hexadécimal correspond à quatre chiffres binaires, ou bits, ce qui signifie que deux chiffres hexadécimaux peuvent représenter un octet de données (8 bits).

### Comment l'hexadécimal est utilisé dans les espaces colorimétriques

L'hexadécimal est couramment utilisé pour représenter les couleurs dans divers espaces colorimétriques, en particulier dans les médias numériques. 

Chaque composante en RVB peut avoir une valeur comprise entre 0 et 255, et ces valeurs peuvent être converties en notation hexadécimale à l'aide d'un [système de numération en base 16](https://www.colorhexa.com/11eb11).

En notation hexadécimale RVB, chaque composante est représentée par un nombre hexadécimal à deux chiffres, qui peut varier de 00 à FF.   
  
Par exemple, 

| Couleur      | RVB | Hexadécimal  | 
| ----------- | ----------- |  ----------- |
| Noir   | 0,0,0        | #000000        |
| Vert d'eau | 0,186,186 | #00BABA |
| Vert | 17,235,17 | #11EB11 |
| Jaune moutarde   | 250,194,134 | #FAC286 |
| Blanc     | 255,255,255       | #FFFFFF       |




![Image](https://lh4.googleusercontent.com/X4ES_ppBld_5qGeavLFSlvSwyXHREWoFaO9WBIp3mV4psy-FNbZV6hXD5_eES4gdzpAXIS8uv1qdFeAyKCwPMgXaZnmlTpBBpw4X2Z8_pyP426g_RSLtipKJsid-e4lNy8D9cmgqE3EtDo3wnVnhC68)
_Illustration du système de couleurs hexadécimal_

## Comment générer des couleurs avec les hexadécimaux

Notre objectif dans cette section est de construire le projet de démonstration. Le projet de démonstration est un bouton. En cliquant sur ce bouton, une couleur est générée qui change le fond de la page web HTML.

Il y a 6 étapes pour construire le projet. Nous les passerons en revue une par une.

### 1. Représenter les hexadécimaux à l'aide d'un tableau

```js

const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

```

La première étape consiste à stocker nos caractères dans une structure. J'ai choisi un tableau pour sa simplicité. La manière dont les tableaux fonctionnent en JavaScript nous permet de [sélectionner n'importe quel élément en fournissant son index](https://www.freecodecamp.org/news/the-javascript-array-handbook/).

### 2. Créer une fonction pour extraire des éléments de ce tableau

```js
const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]

function getCharacter(index) {
	return hexCharacters[index]
}
```

La fonction `getCharacter` prendra l'index et retournera le caractère hexadécimal stocké à cet endroit. Cela nous aide à choisir nos couleurs.

### 3. Représenter les couleurs en utilisant la valeur extraite

Une représentation hexadécimale du RVB commence par `#` suivi de 6 caractères sélectionnés dans notre tableau. Ainsi, la fonction `getCharacters` sera appelée 6 fois. Nous pouvons utiliser une [boucle for](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Statements/for) pour appeler notre fonction plus rapidement. 

```js

const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]


function getCharacter(index) {
	return hexCharacters[index]
}

function generateJustOneColor(){
    
	let hexColorRep = "#"

    for (let position = 0; position < 6; position++){
        hexColorRep += getCharacter( position )
    }
	
	return hexColorRep

}

console.log( generateJustOneColor() )
```

`generateJustOneColor()` génère un code de couleur hexadécimal aléatoire représenté sous forme de chaîne.

La fonction commence par déclarer une variable nommée _hexColorRep_ et l'initialise avec le caractère #. 

Ensuite, la fonction utilise une boucle for pour générer les six caractères suivants du code de couleur. La boucle s'exécute six fois car chaque code de couleur est représenté par six chiffres hexadécimaux.

Dans la boucle, la fonction appelle une autre fonction nommée `getCharacter()` pour générer un chiffre hexadécimal pour chaque position du code de couleur. Le paramètre `position` est passé à la fonction `getCharacter()` pour indiquer quel chiffre est en cours de génération.

Une fois que les six chiffres du code de couleur ont été générés, la fonction retourne le code de couleur complet sous forme de chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.56.42.png)
_Le même résultat est retourné à chaque fois._

Le code ci-dessus retournera toujours ce même résultat/couleur étant donné la même `position` pour notre boucle for. Nous devons donc introduire de l'aléatoire. Cela signifie que notre sélection des caractères doit comporter un élément de surprise. 

### 4. Améliorer notre code pour générer des couleurs aléatoires

En JavaScript, **[`Math.random()`](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Math/random)** est l'une des façons d'introduire de l'aléatoire. `Math.random()` donne un nouveau résultat à chaque fois qu'il est appelé dans la plage `0 à 1`_._ 

Bien que la fonction `Math.random()` génère un nombre décimal aléatoire entre 0 (inclus) et 1 (exclus), nous pouvons manipuler cette valeur pour obtenir un entier aléatoire entre 0 et 15.

Cela se fait en multipliant le nombre décimal aléatoire par la plage souhaitée d'entiers (dans ce cas, 16) puis en appliquant la méthode `Math.floor()` pour arrondir le résultat à l'entier le plus proche. Cela garantira que le résultat est dans la plage souhaitée d'entiers.

Par exemple, si `Math.random()` génère la valeur `0.435`, la multiplier par 16 donnerait `6.96`. Appliquer `Math.floor()` à ce résultat l'arrondirait alors à `6`, qui est un entier aléatoire dans la plage de 0 à 15.

`Math.floor()` joue 2 rôles ici : il nous aide à éviter une [RangeError](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Errors/Invalid_array_length) en arrondissant les extrêmes (le nombre maximum sera 15) et garantit que nous retournons toujours un entier. 

```js
const randomNumber = Math.floor ( Math.random() * hexCharacters.length ) 
```

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.34.10.png)
_Math.random() donne un nouveau résultat à chaque fois qu'il est appelé._

Nous avons tous les ingrédients nécessaires pour générer notre couleur, nous pouvons donc maintenant les combiner. Chaque couleur hexadécimale doit commencer par un "#" et être suivie de 6 caractères_._ 

```js


const hexCharacters = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]



function getCharacter(index) {
	return hexCharacters[index]
}

function generateNewColor() {
	let hexColorRep = "#"

	for (let index = 0; index < 6; index++){
		const randomPosition = Math.floor ( Math.random() * hexCharacters.length ) 
    	hexColorRep += getCharacter( randomPosition )
	}
	
	return hexColorRep
}

console.log( generateNewColor() ) 
```

La fonction `generateNewColor()` est la fonction principale du programme qui génère le code de couleur hexadécimal aléatoire. Elle commence par initialiser une variable de chaîne nommée "hexColorRep" avec le caractère "#", car tous les codes de couleur hexadécimaux commencent par ce caractère.

Ensuite, la fonction utilise une boucle for pour générer six caractères aléatoires pour le code de couleur. Dans la boucle, la fonction génère une position aléatoire dans la plage du tableau "hexCharacters" en utilisant la fonction `Math.random()` et la longueur du tableau `hexCharacters`. Cette position aléatoire est ensuite utilisée pour obtenir un caractère aléatoire du tableau `hexCharacters` en utilisant la fonction `getCharacter()`. Le caractère résultant est ajouté à la variable de chaîne `hexColorRep`.

Enfin, la fonction `generateNewColor()` retourne le code de couleur hexadécimal complet représenté sous forme de chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2023/02/Screenshot-2023-02-21-at-08.55.07.png)
_Le résultat est toujours une nouvelle représentation de couleur hexadécimale._

### 5. Créer une interface pour présenter notre code

Nous avons besoin d'une interface pour que les utilisateurs puissent interagir avec notre code et voir la magie que nous avons créée. 

Nous allons avoir une page HTML avec une liste d'instructions et un bouton. Les éléments bouton et span sont donnés avec l'attribut id pour qu'il soit plus facile de les trouver dans notre code JavaScript. Vous pouvez voir le code HTML [ici](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html). 

![Image](https://www.freecodecamp.org/news/content/images/2023/03/demo4.JPG)

### 6. Connecter le bouton à la fonction à l'aide d'un événement

Notre objectif est de changer le style _background-color_ de cette page HTML. 

```js
let btn = document.getElementById('b')
let bgColor = document.getElementById('s')

btn.addEventListener("click", (event) => {
		
	const newColor = generateNewColor()

	document.body.style.backgroundColor  = newColor
	bgColor.textContent = newColor 
		
})
```

Ce programme définit la couleur de fond d'une page web avec un code de couleur hexadécimal généré aléatoirement lorsqu'un bouton est cliqué.

Le programme commence par définir deux variables en utilisant la méthode `document.getElementById()`. La variable `btn` représente l'élément bouton sur la page web avec l'ID `b`, tandis que la variable `bgColor` représente un élément de texte sur la page web avec l'ID `s`.

Ensuite, le programme attache un écouteur d'événement à l'élément `btn` en utilisant la méthode `addEventListener()`. Cet écouteur écoute l'événement `click` sur le bouton. Lorsqu'il est déclenché, il exécute une fonction qui génère un nouveau code de couleur aléatoire en utilisant la fonction `generateNewColor()`.

Le code de couleur résultant est ensuite attribué à la couleur de fond de la page web en utilisant la propriété `style.backgroundColor` de l'élément `document.body`. Cela met à jour toute la page web avec la nouvelle couleur.

Enfin, le code de couleur est également affiché dans l'élément `bgColor` sur la page web en utilisant la propriété textContent.

Vous pouvez voir le code complet [ici](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html). 

![Image](https://www.freecodecamp.org/news/content/images/2023/02/ezgif.com-gif-maker-1.gif)
_Produit final_

## Résumé

Dans cet article, nous avons montré comment générer des couleurs aléatoires en JavaScript. Nous avons utilisé les méthodes _random_ et _floor_ de la [classe Math](https://developer.mozilla.org/fr/docs/Web/JavaScript/Reference/Global_Objects/Math) et montré l'utilisation de base d'une boucle for.  
  
Dans le [projet de démonstration](http://rufai.github.io/buildingx/random_bg_color.html), la couleur générée a été passée en fond à une page HTML. C'est pourquoi, en cliquant sur le bouton, une nouvelle couleur est générée et met à jour le style _background-color_ de la page. Consultez le code complet [ici](https://github.com/rufai/rufai.github.io/blob/master/buildingx/random_bg_color.html).   
  
Si vous souhaitez voir plus d'enseignements, consultez [Xutini](https://www.youtube.com/@xutini) - la manière amusante d'apprendre les compétences numériques.