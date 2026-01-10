---
title: Comment coder votre propre générateur de donjon procédural en utilisant l'algorithme
  de marche aléatoire
subtitle: ''
author: Ahmad Abdolsaheb
co_authors: []
series: null
date: '2020-06-02T21:18:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-own-procedural-dungeon-map-generator-using-the-random-walk-algorithm-e0085c8aa9a
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/Screen-Shot-2020-09-12-at-11.30.55-PM.png
tags:
- name: AI
  slug: ai
- name: algorithms
  slug: algorithms
- name: Games
  slug: games
- name: JavaScript
  slug: javascript
- name: React
  slug: react
seo_title: Comment coder votre propre générateur de donjon procédural en utilisant
  l'algorithme de marche aléatoire
seo_desc: 'As technology evolves and game contents become more algorithmically generated,
  it’s not difficult to imagine the creation of a life-like simulation with unique
  experiences for each player.

  Technological breakthroughs, patience, and refined skills wil...'
---

Alors que la technologie évolue et que les contenus de jeux deviennent de plus en plus générés algorithmiquement, il n'est pas difficile d'imaginer la création d'une simulation réaliste avec des expériences uniques pour chaque joueur.

Les percées technologiques, la patience et les compétences affinées nous mèneront là, mais la première étape est de comprendre la **génération procédurale de contenu**.

Bien que de nombreuses solutions clés en main pour la génération de cartes existent, ce tutoriel vous apprendra à créer votre propre générateur de carte de donjon en deux dimensions à partir de zéro en utilisant JavaScript.

Il existe de nombreux types de cartes en deux dimensions, et toutes ont les caractéristiques suivantes :

1. Des zones accessibles et inaccessibles (tunnels et murs).

2. Un itinéraire connecté que le joueur peut naviguer.

L'algorithme de ce tutoriel provient de l'[Algorithme de Marche Aléatoire](https://en.wikipedia.org/wiki/Random_walker_algorithm), l'une des solutions les plus simples pour la génération de cartes.

Après avoir créé une carte en forme de grille de murs, cet algorithme commence à partir d'un endroit aléatoire sur la carte. Il continue à faire des tunnels et à prendre des virages aléatoires pour compléter son nombre souhaité de tunnels.

Pour voir une démonstration, ouvrez le projet CodePen ci-dessous, cliquez sur la carte pour créer une nouvelle carte, et changez les valeurs suivantes :

1. **Dimensions** : la largeur et la hauteur de la carte.
2. **MaxTunnels** : le plus grand nombre de virages que l'algorithme peut prendre lors de la création de la carte.
3. **MaxLength** : la plus grande longueur de chaque tunnel que l'algorithme choisira avant de faire un virage horizontal ou vertical.

<iframe height="700" style="width: 100%;" scrolling="no" title="CreatMap" src="https://codepen.io/abdolsa/embed/zEKdop?height=700&theme-id=light&default-tab=result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  See the Pen <a href='https://codepen.io/abdolsa/pen/zEKdop'>CreatMap</a> by Ahmad Abdolsaheb
  (<a href='https://codepen.io/abdolsa'>@abdolsa</a>) on <a href='https://codepen.io'>CodePen</a>.
</iframe>

**Note :** plus le _maxTurn_ est grand par rapport aux dimensions, plus la carte sera dense. Plus le _maxLength_ est grand par rapport aux dimensions, plus elle aura l'air "tunnelée".

Ensuite, passons en revue l'algorithme de génération de carte pour voir comment il :

1. Crée une carte en deux dimensions de murs
2. Choisit un point de départ aléatoire sur la carte
3. Tant que le nombre de tunnels n'est pas zéro
4. Choisit une longueur aléatoire à partir de la longueur maximale autorisée
5. Choisit une direction aléatoire pour tourner (droite, gauche, haut, bas)
6. Dessine un tunnel dans cette direction tout en évitant les bords de la carte
7. Décrémente le nombre de tunnels et répète la [boucle while](https://en.wikipedia.org/wiki/While_loop)
8. Retourne la carte avec les changements

Cette boucle continue jusqu'à ce que le nombre de tunnels soit zéro.

### L'Algorithme en Code

Puisque la carte se compose de cellules de tunnels et de murs, nous pourrions la décrire comme des zéros et des uns dans un tableau à deux dimensions comme suit :

```javascript
map = [[1,1,1,1,0],
       [1,0,0,0,0],
       [1,0,1,1,1],       
       [1,0,0,0,1],       
       [1,1,1,0,1]]
```

Puisque chaque cellule est dans un tableau à deux dimensions, nous pouvons accéder à sa valeur en connaissant sa ligne et sa colonne, comme map [ligne][colonne].

Avant d'écrire l'algorithme, vous avez besoin d'une fonction auxiliaire qui prend un caractère et une dimension comme arguments et retourne un tableau à deux dimensions.

```javascript
createArray(num, dimensions) {
    var array = [];    
    for (var i = 0; i < dimensions; i++) { 
      array.push([]);      
      for (var j = 0; j < dimensions; j++) {  
         array[i].push(num);      
      }    
    }    
    return array;  
}

```

Pour implémenter l'Algorithme de Marche Aléatoire, définissez les dimensions de la carte (largeur et hauteur), la variable `maxTunnels`, et la variable `maxLength`.

```javascript
createMap(){
 let dimensions = 5,     
 maxTunnels = 3, 
 maxLength = 3;

```

Ensuite, créez un tableau à deux dimensions en utilisant la fonction auxiliaire prédéfinie (tableau à deux dimensions de uns).

```javascript
let map = createArray(1, dimensions);
```

Définissez une colonne aléatoire et une ligne aléatoire pour créer un point de départ aléatoire pour le premier tunnel.

```javascript
let currentRow = Math.floor(Math.random() * dimensions),       
    currentColumn = Math.floor(Math.random() * dimensions);
```

Pour éviter la complexité des virages diagonaux, l'algorithme doit spécifier les directions horizontales et verticales. Chaque cellule se trouve dans un tableau à deux dimensions et pourrait être identifiée par sa ligne et sa colonne. Pour cette raison, les directions pourraient être définies comme des soustractions et/ou des additions aux numéros de colonne et de ligne.

Par exemple, pour aller à une cellule autour de la cellule [2][2], vous pourriez effectuer les opérations suivantes :

* pour aller **en haut**, soustrayez 1 de sa ligne [1][2]
* pour aller **en bas**, ajoutez 1 à sa ligne [3][2]
* pour aller **à droite**, ajoutez 1 à sa colonne [2][3]
* pour aller **à gauche**, soustrayez 1 de sa colonne [2][1]

La carte suivante illustre ces opérations :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1_P1AfxAKl6SAQMgn8SONUGQ.png)
_Grille des options opérationnelles_

Maintenant, définissez la variable `directions` aux valeurs suivantes que l'algorithme choisira avant de créer chaque tunnel :

```javascript
let directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];
```

Enfin, initialisez la variable `randomDirection` pour contenir une valeur aléatoire du tableau des directions, et définissez la variable `lastDirection` à un tableau vide qui contiendra l'ancienne valeur de `randomDirection`.

**Note :** le tableau `lastDirection` est vide lors de la première boucle car il n'y a pas d'ancienne valeur `randomDirection`.

```javascript
let lastDirection = [], 
    randomDirection;
```

Ensuite, assurez-vous que `maxTunnel` n'est pas zéro et que les valeurs des dimensions et `maxLength` ont été reçues. Continuez à trouver des directions aléatoires jusqu'à ce que vous en trouviez une qui n'est pas inverse ou identique à `lastDirection`. Cette [boucle do while](https://en.wikipedia.org/wiki/Do_while_loop) aide à prévenir l'écrasement du tunnel récemment dessiné ou le dessin de deux tunnels dos à dos.

Par exemple, si votre `lastTurn` est [0, 1], la boucle do while empêche la fonction de continuer jusqu'à ce que `randomDirection` soit défini à une valeur qui n'est pas [0, 1] ou l'opposé [0, -1].

```javascript
do {         
randomDirection = directions[Math.floor(Math.random() * directions.length)];      
} while ((randomDirection[0] === -lastDirection[0] &&    
          randomDirection[1] === -lastDirection[1]) || 
         (randomDirection[0] === lastDirection[0] &&  
          randomDirection[1] === lastDirection[1]));

```

Dans la boucle do while, il y a deux conditions principales qui sont divisées par un signe || (OU). La première partie de la condition se compose également de deux conditions. La première vérifie si le premier élément de `randomDirection` est l'inverse du premier élément de `lastDirection`. La seconde vérifie si le deuxième élément de `randomDirection` est l'inverse du deuxième élément de `lastTurn`.

Pour illustrer, si `lastDirection` est [0,1] et `randomDirection` est [0,-1], la première partie de la condition vérifie si `randomDirection`[0] === - `lastDirection`[0]), ce qui équivaut à 0 === - 0, et est vrai.

Ensuite, elle vérifie si (`randomDirection`[1] === - `lastDirection`[1]) ce qui équivaut à (-1 === -1) et est également vrai. Puisque les deux conditions sont vraies, l'algorithme retourne pour trouver une autre `randomDirection`.

La deuxième partie de la condition vérifie si les première et deuxième valeurs des deux tableaux sont les mêmes.

Après avoir choisi une `randomDirection` qui satisfait les conditions, définissez une variable pour choisir aléatoirement une longueur à partir de `maxLength`. Définissez la variable `tunnelLength` à zéro pour servir d'itérateur.

```javascript
let randomLength = Math.ceil(Math.random() * maxLength),       
    tunnelLength = 0;
```

Créez un tunnel en transformant la valeur des cellules de un à zéro tant que `tunnelLength` est inférieur à `randomLength`. Si dans la boucle le tunnel atteint les bords de la carte, la boucle doit se rompre.

```javascript
while (tunnelLength < randomLength) { 
 if(((currentRow === 0) && (randomDirection[0] === -1))||  
    ((currentColumn === 0) && (randomDirection[1] === -1))|| 
    ((currentRow === dimensions — 1) && (randomDirection[0] ===1))||
 ((currentColumn === dimensions — 1) && (randomDirection[1] === 1)))   
 { break; }
```

Sinon, définissez la cellule actuelle de la carte à zéro en utilisant `currentRow` et `currentColumn`. Ajoutez les valeurs dans le tableau `randomDirection` en définissant `currentRow` et `currentColumn` là où ils doivent être dans l'itération à venir de la boucle. Maintenant, incrémentez l'itérateur `tunnelLength`.

```javascript
else{ 
  map[currentRow][currentColumn] = 0; 
  currentRow += randomDirection[0];
  currentColumn += randomDirection[1]; 
  tunnelLength++; 
 } 
}

```

Après que la boucle ait fait un tunnel ou se soit rompue en atteignant un bord de la carte, vérifiez si le tunnel fait au moins une cellule de long. Si c'est le cas, définissez `lastDirection` à `randomDirection` et décrémentez `maxTunnels` et retournez pour faire un autre tunnel avec une autre `randomDirection`.

```javascript
if (tunnelLength) { 
 lastDirection = randomDirection; 
 maxTunnels--; 
}

```

Cette instruction IF empêche la boucle for qui a atteint le bord de la carte et n'a pas fait un tunnel d'au moins une cellule de décrémenter `maxTunnel` et de changer `lastDirection`. Lorsque cela se produit, l'algorithme va trouver une autre `randomDirection` pour continuer.

Lorsque l'algorithme a fini de dessiner les tunnels et que `maxTunnels` est zéro, retournez la carte résultante avec tous ses virages et tunnels.

```javascript
}
 return map;
};
```

Vous pouvez voir l'algorithme complet dans l'extrait suivant :

Félicitations pour avoir lu ce tutoriel. Vous êtes maintenant bien équipé pour créer votre propre générateur de carte ou améliorer cette version. Consultez le projet sur [CodePen](https://codepen.io/anon/pen/aLpORx) et sur [GitHub](https://github.com/ahmadabdolsaheb/mapgen) en tant qu'application React.

_Merci d'avoir lu ! Si vous avez aimé cette histoire, n'oubliez pas de la partager sur les réseaux sociaux._

Un remerciement spécial à [Tom](https://github.com/moT01) pour la co-rédaction de cet article.