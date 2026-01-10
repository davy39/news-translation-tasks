---
title: Comment rendre votre jeu de Morpion imbattable en utilisant l'algorithme minimax
subtitle: ''
author: Ahmad Abdolsaheb
co_authors: []
series: null
date: '2020-05-02T04:50:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-your-tic-tac-toe-game-unbeatable-by-using-the-minimax-algorithm-9d690bad4b37
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/1_y2B2auvIpUI0vSLtT2KWyg-1.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: gaming
  slug: gaming
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
seo_title: Comment rendre votre jeu de Morpion imbattable en utilisant l'algorithme
  minimax
seo_desc: I struggled for hours scrolling through tutorials, watching videos, and
  banging my head on the desk trying to build an unbeatable Tic Tac Toe game with
  a reliable Artificial Intelligence. So if you are going through a similar journey,
  I would like to...
---

J'ai passé des heures à faire défiler des tutoriels, à regarder des vidéos et à me taper la tête contre le bureau en essayant de construire un jeu de Morpion (Tic Tac Toe) imbattable avec une Intelligence Artificielle fiable. Si vous vivez un parcours similaire, j'aimerais vous présenter l'algorithme Minimax.

Comme un joueur d'échecs professionnel, cet algorithme voit quelques coups à l'avance et se met à la place de son adversaire. Il continue de simuler les coups jusqu'à ce qu'il atteigne une configuration finale du plateau (**état terminal**) se traduisant par un match nul, une victoire ou une défaite. Une fois dans un état terminal, l'IA attribuera un score positif arbitraire (+10) pour une victoire, un score négatif (-10) pour une défaite, ou un score neutre (0) pour un match nul.

En même temps, l'algorithme évalue les mouvements qui mènent à un état terminal en fonction du tour des joueurs. Il choisira le mouvement avec le score maximum quand c'est au tour de l'IA et choisira le mouvement avec le score minimum quand c'est au tour du joueur humain. En utilisant cette stratégie, Minimax évite de perdre contre le joueur humain.

Essayez-le par vous-même dans le jeu suivant, de préférence en utilisant un navigateur Chrome.

<iframe height="454" style="width: 100%;" scrolling="no" title="minimax 4 medium" src="https://codepen.io/abdolsa/embed/vgjoMb?height=454&theme-id=light&default-tab=js,result" frameborder="no" loading="lazy" allowtransparency="true" allowfullscreen="true">
  Voir le Pen <a href='https://codepen.io/abdolsa/pen/vgjoMb'>minimax 4 medium</a> par Ahmad Abdolsaheb
  (<a href='https://codepen.io/abdolsa'>@abdolsa</a>) sur <a href='https://codepen.io'>CodePen</a>.
</iframe>

Un algorithme Minimax peut être défini au mieux comme une fonction récursive qui effectue les opérations suivantes :

1. retourner une valeur si un état terminal est trouvé (+10, 0, -10)
2. parcourir les emplacements disponibles sur le plateau
3. appeler la fonction minimax sur chaque emplacement disponible (récursion)
4. évaluer les valeurs retournées par les appels de fonction
5. et retourner la meilleure valeur

Si vous découvrez le concept de récursion, je vous recommande de regarder cette [vidéo](https://www.youtube.com/watch?v=VrrnjYgDBEk) de CS50 de Harvard.

Pour bien saisir le processus de pensée de Minimax, implémentons-le en code et voyons-le en action dans les deux sections suivantes.

### Minimax dans le code

Pour ce tutoriel, vous travaillerez sur un état de fin de partie proche, illustré à la figure 2 ci-dessous. Étant donné que minimax évalue chaque état du jeu (des centaines de milliers), un état proche de la fin vous permet de suivre plus facilement les appels récursifs de minimax (9).

Pour la figure suivante, supposons que l'IA est X et que le joueur humain est O.

![Image](https://cdn-media-1.freecodecamp.org/images/iYDAcMcMvbr0lBISCQqM-mBbfhqDx2sPqcYl)
_figure 2 échantillon d'état de jeu_

Pour travailler plus facilement avec le plateau de Morpion, vous devriez le définir comme un tableau de 9 éléments. Chaque élément aura son indice comme valeur. Cela sera utile plus tard. Comme le plateau ci-dessus est déjà rempli de quelques coups X et O, définissons le plateau avec les coups X et O déjà présents (_origBoard_).

```javascript
var origBoard = ["O",1,"X","X",4,"X",6,"O","O"];
```

Ensuite, déclarez les variables _aiPlayer_ et _huPlayer_ et réglez-les respectivement sur "X" et "O".

De plus, vous avez besoin d'une fonction qui recherche les combinaisons gagnantes et retourne vrai si elle en trouve une, et d'une fonction qui liste les indices des cases disponibles sur le plateau.

```javascript
/* le plateau original
 O |   | X
 ---------
 X |   | X
 ---------
   | O | O
 */
var origBoard = [“O”,1 ,”X”,”X”,4 ,”X”, 6 ,”O”,”O”];

// humain
var huPlayer = “O”;

// ia
var aiPlayer = “X”;

// retourne la liste des indices des cases vides sur le plateau
function emptyIndexies(board){
  return  board.filter(s => s != "O" && s != "X");
}

// combinaisons gagnantes en utilisant les indices du plateau
function winning(board, player){
 if (
 (board[0] == player && board[1] == player && board[2] == player) ||
 (board[3] == player && board[4] == player && board[5] == player) ||
 (board[6] == player && board[7] == player && board[8] == player) ||
 (board[0] == player && board[3] == player && board[6] == player) ||
 (board[1] == player && board[4] == player && board[7] == player) ||
 (board[2] == player && board[5] == player && board[8] == player) ||
 (board[0] == player && board[4] == player && board[8] == player) ||
 (board[2] == player && board[4] == player && board[6] == player)
 ) {
 return true;
 } else {
 return false;
 }
}
```

Plongeons maintenant dans le vif du sujet en définissant la fonction Minimax avec deux arguments _newBoard_ et _player_. Ensuite, vous devez trouver les indices des cases disponibles sur le plateau et les affecter à une variable appelée _availSpots_.

```javascript
// la fonction minimax principale
function minimax(newBoard, player){
  
    // cases disponibles
    var availSpots = emptyIndexies(newBoard);
```

De plus, vous devez vérifier les états terminaux et retourner une valeur en conséquence. Si O gagne, vous devez retourner -10, si X gagne, vous devez retourner +10. De plus, si la longueur du tableau _availableSpots_ est nulle, cela signifie qu'il n'y a plus de place pour jouer, que le jeu s'est soldé par un match nul, et vous devez retourner zéro.

```javascript

  // vérifie les états terminaux tels que victoire, défaite et match nul 
  // et retourne une valeur en conséquence
  if (winning(newBoard, huPlayer)){
     return {score:-10};
  }
	else if (winning(newBoard, aiPlayer)){
    return {score:10};
	}
  else if (availSpots.length === 0){
  	return {score:0};
  }
```

Ensuite, vous devez collecter les scores de chacune des cases vides pour les évaluer plus tard. Par conséquent, créez un tableau appelé _moves_ et parcourez les cases vides tout en collectant l'indice et le score de chaque mouvement dans un objet appelé _move_.

Ensuite, réglez le numéro d'indice de la case vide qui était stocké sous forme de nombre dans _origBoard_ sur la propriété index de l'objet _move_. Ensuite, réglez la case vide sur le _newboard_ sur le joueur actuel et appelez la fonction _minimax_ avec l'autre joueur et le _newboard_ fraîchement modifié. Ensuite, vous devez stocker l'objet résultant de l'appel de la fonction _minimax_ qui inclut une propriété _score_ dans la propriété _score_ de l'objet _move_.

> _Si la fonction minimax ne trouve pas d'état terminal, elle continue de descendre récursivement niveau par niveau plus profondément dans le jeu. Cette récursion se produit jusqu'à ce qu'elle atteigne un état terminal et retourne un score au niveau supérieur._

Enfin, Minimax réinitialise _newBoard_ à ce qu'il était avant et ajoute l'objet _move_ au tableau _moves_.

```javascript
// un tableau pour collecter tous les objets
  var moves = [];

  // boucle à travers les cases disponibles
  for (var i = 0; i < availSpots.length; i++){
    // crée un objet pour chacune et stocke l'indice de cette case 
    var move = {};
  	move.index = newBoard[availSpots[i]];

    // définit la case vide pour le joueur actuel
    newBoard[availSpots[i]] = player;

    /* collecter le score résultant de l'appel de minimax 
      sur l'adversaire du joueur actuel */
    if (player == aiPlayer){
      var result = minimax(newBoard, huPlayer);
      move.score = result.score;
    }
    else{
      var result = minimax(newBoard, aiPlayer);
      move.score = result.score;
    }

    // réinitialise la case comme vide
    newBoard[availSpots[i]] = move.index;

    // ajoute l'objet au tableau
    moves.push(move);
  }
```

Ensuite, l'algorithme minimax doit évaluer le meilleur _move_ dans le tableau _moves_. Il doit choisir le _move_ avec le score le plus élevé lorsque l'IA joue et le _move_ avec le score le plus bas lorsque l'humain joue. Par conséquent, si le _player_ est _aiPlayer_, il définit une variable appelée _bestScore_ à un nombre très bas et parcourt le tableau _moves_ ; si un _move_ a un _score_ plus élevé que _bestScore_, l'algorithme stocke ce _move_. Dans le cas où il y a des mouvements avec un score similaire, seul le premier sera stocké.

Le même processus d'évaluation se produit lorsque _player_ est _huPlayer_, mais cette fois _bestScore_ serait réglé sur un nombre élevé et Minimax recherche un mouvement avec le score le plus bas à stocker.

À la fin, Minimax retourne l'objet stocké dans _bestMove_.

```javascript
// si c'est le tour de l'ordinateur, boucle sur les mouvements et choisit le mouvement avec le score le plus élevé
  var bestMove;
  if(player === aiPlayer){
    var bestScore = -10000;
    for(var i = 0; i < moves.length; i++){
      if(moves[i].score > bestScore){
        bestScore = moves[i].score;
        bestMove = i;
      }
    }
  }else{

// sinon boucle sur les mouvements et choisit le mouvement avec le score le plus bas
    var bestScore = 10000;
    for(var i = 0; i < moves.length; i++){
      if(moves[i].score < bestScore){
        bestScore = moves[i].score;
        bestMove = i;
      }
    }
  }

// retourne le mouvement choisi (objet) à partir du tableau moves
  return moves[bestMove];
}
```

> _C'est tout pour la fonction minimax. :) vous pouvez trouver l'algorithme ci-dessus sur [github](https://github.com/ahmadabdolsaheb/minimaxarticle) et [codepen](https://codepen.io/abdolsa/pen/mABGoz?editors=1011). Amusez-vous avec différents plateaux et vérifiez les résultats dans la console._

Dans la section suivante, passons en revue le code ligne par ligne pour mieux comprendre comment la fonction minimax se comporte avec le plateau illustré à la figure 2.

### Minimax en action

En utilisant la figure suivante, suivons les appels de fonction (**AF**) de l'algorithme un par un.

Note : Dans la figure 3, les grands nombres représentent chaque appel de fonction et les niveaux font référence au nombre de coups d'avance que l'algorithme simule.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1_VG79nxl-mJQrsp6p3q79qA--1-.png)
_Figure 3 Appel de fonction par appel de fonction de Minimax_

**_1._** _origBoard_ et _aiPlayer_ sont fournis à l'algorithme. L'algorithme dresse une liste des trois cases vides qu'il trouve, vérifie les états terminaux et boucle à travers chaque case vide en commençant par la première. Ensuite, il modifie le _newBoard_ en plaçant l' _aiPlayer_ dans la première case vide. Après cela, il s'appelle lui-même avec _newBoard_ et le _huPlayer_ et attend que l'AF retourne une valeur.

**2.** Alors que le premier AF est toujours en cours, le second commence par dresser une liste des deux cases vides qu'il trouve, vérifie les états terminaux et boucle à travers la case vide en commençant par la première. Ensuite, il modifie le _newBoard_ en plaçant le _huPlayer_ dans la première case vide. Après cela, il s'appelle lui-même avec _newBoard_ et l' _aiPlayer_ et attend que l'AF retourne une valeur.

**3.** Enfin, l'algorithme dresse une liste des cases vides et trouve une victoire pour le joueur humain après avoir vérifié les états terminaux. Par conséquent, il retourne un objet avec une propriété score et une valeur de -10.

> _Puisque le deuxième AF a listé deux cases vides, Minimax modifie le_ newBoard _en plaçant_ huPlayer _dans la deuxième case vide. Ensuite, il s'appelle lui-même avec le nouveau plateau et l'_ aiPlayer_._

**4.** L'algorithme dresse une liste des cases vides et trouve une victoire pour le joueur humain après avoir vérifié les états terminaux. Par conséquent, il retourne un objet avec une propriété score et une valeur de -10.

> _Lors du deuxième AF, l'algorithme collecte les valeurs provenant des niveaux inférieurs (3ème et 4ème AF). Puisque le tour de_ huPlayer _a abouti aux deux valeurs, l'algorithme choisit la plus basse des deux valeurs. Comme les deux valeurs sont identiques, il choisit la première et la renvoie au premier AF._

> _À ce stade, le premier AF a évalué le score du placement de_ aiPlayer _dans la première case vide. Ensuite, il modifie le_ newBoard _en plaçant_ aiPlayer _dans la deuxième case vide. Ensuite, il s'appelle lui-même avec le_ newBoard _et le_ huPlayer_._

**5.** Lors du cinquième AF, l'algorithme dresse une liste des cases vides et trouve une victoire pour le joueur humain après avoir vérifié les états terminaux. Par conséquent, il retourne un objet avec une propriété score et une valeur de +10.

> _Après cela, le premier AF continue en modifiant le_ newBoard _et en plaçant_ aiPlayer _dans la troisième case vide. Ensuite, il s'appelle lui-même avec le nouveau plateau et le_ huPlayer_._

**6.** Le 6ème AF commence par dresser une liste des deux cases vides qu'il trouve, vérifie les états terminaux et boucle à travers les deux cases vides en commençant par la première. Ensuite, il modifie le _newBoard_ en plaçant le _huPlayer_ dans la première case vide. Après cela, il s'appelle lui-même avec _newBoard_ et l' _aiPlayer_ et attend que l'AF retourne un score.

**7.** Maintenant, l'algorithme est à deux niveaux de profondeur dans la récursion. Il dresse une liste de la seule case vide qu'il trouve, vérifie les états terminaux et modifie le _newBoard_ en plaçant l' _aiPlayer_ dans la case vide. Après cela, il s'appelle lui-même avec _newBoard_ et le _huPlayer_ et attend que l'AF retourne un score afin de pouvoir l'évaluer.

**8.** Lors du 8ème AF, l'algorithme dresse une liste vide de cases vides et trouve une victoire pour l' _aiPlayer_ après avoir vérifié les états terminaux. Par conséquent, il retourne un objet avec une propriété score et une valeur de +10 au niveau supérieur (7ème AF).

> _Le 7ème AF n'a reçu qu'une seule valeur positive des niveaux inférieurs (8ème AF). Parce que le tour de_ aiPlayer _a abouti à cette valeur, l'algorithme doit retourner la valeur la plus élevée qu'il a reçue des niveaux inférieurs. Par conséquent, il retourne sa seule valeur positive (+10) au niveau supérieur (6ème AF)._

> _Puisque le 6ème AF a listé deux cases vides, Minimax modifie_ newBoard _en plaçant_ huPlayer _dans la deuxième case vide. Ensuite, il s'appelle lui-même avec le nouveau plateau et l'_ aiPlayer_._

**9.** Ensuite, l'algorithme dresse une liste des cases vides et trouve une victoire pour l' _aiPlayer_ après avoir vérifié les états terminaux. Par conséquent, il retourne un objet avec des propriétés score et une valeur de +10.

> _À ce stade, le 6ème AF doit choisir entre le score (+10) qui a été envoyé par le 7ème AF (retourné à l'origine par le 8ème AF) et le score (-10) retourné par le 9ème AF. Puisque le tour de_ huPlayer _a abouti à ces deux valeurs de retour, l'algorithme trouve le score minimum (-10) et le renvoie vers le haut sous la forme d'un objet contenant les propriétés score et index._

> _Enfin, les trois branches du premier AF ont été évaluées (-10, +10, -10). Mais parce que le tour de aiPlayer a abouti à ces valeurs, l'algorithme retourne un objet contenant le score le plus élevé (+10) et son indice (4)._

**Dans le scénario ci-dessus, Minimax conclut que déplacer le X au milieu du plateau donne le meilleur résultat. :)**

### La fin !

Vous devriez maintenant être en mesure de comprendre la logique derrière l'algorithme Minimax. En utilisant cette logique, essayez d'implémenter un algorithme Minimax vous-même ou trouvez l'échantillon ci-dessus sur [github](https://github.com/ahmadabdolsaheb/minimaxarticle) ou [codepen](https://codepen.io/abdolsa/pen/mABGoz?editors=1011) et optimisez-le.

_Merci pour votre lecture ! Si vous avez aimé cette histoire, n'oubliez pas de la partager sur les réseaux sociaux._

_Remerciements particuliers à Tuba Yilmaz, Rick McGavin et Javid Askerov pour la relecture de cet article._