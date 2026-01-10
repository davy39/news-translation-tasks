---
title: Comment construire une IA pour les jeux à deux joueurs en tour par tour
subtitle: ''
author: Houssein Badra
co_authors: []
series: null
date: '2022-12-15T18:24:15.000Z'
originalURL: https://freecodecamp.org/news/build-an-ai-for-two-player-turn-based-games
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/2825132-637490944552534550-16x9-1.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Games
  slug: games
seo_title: Comment construire une IA pour les jeux à deux joueurs en tour par tour
seo_desc: 'Two-player turn-based games are games where two players play against each
  other, turn after turn, until one of them wins. Examples of these types of games
  are Tic-Tac-Toe, Backgammon, Mancala, Chess, and Connect 4.

  In this tutorial we will learn abou...'
---

Les jeux à deux joueurs en tour par tour sont des jeux où deux joueurs jouent l'un contre l'autre, tour après tour, jusqu'à ce que l'un d'eux gagne. Des exemples de ces types de jeux sont le Tic-Tac-Toe, le Backgammon, le Mancala, les Échecs et le Connect 4.

Dans ce tutoriel, nous allons apprendre l'algorithme **Minimax**. C'est un algorithme de retour en arrière qui est utilisé dans la prise de décision et la théorie des jeux. Il trouve le meilleur coup pour un joueur, en supposant que son adversaire joue également de manière optimale. Il est largement utilisé dans les jeux à deux joueurs en tour par tour.

Vous apprendrez comment créer votre propre IA qui joue à l'un des jeux mentionnés ci-dessus ou à tout autre jeu similaire. De plus, pour rendre cela aussi compréhensible que possible, je vais appliquer l'algorithme à un jeu de **Tic-Tac-Toe**.

Nous ne couvrirons pas tout le processus de création du jeu, mais seulement la partie liée à l'IA puisque c'est notre sujet. Si vous êtes intéressé par le processus de création de jeux, vous pouvez consulter ce [**jeu de Tic-Tac-Toe qui utilise l'IA**](https://housseinbadra.github.io/BadraAI.github.io/) et son code source sur [**GitHub**](https://github.com/HousseinBadra/BadraAI.github.io.git). C'est un projet que j'ai construit il y a longtemps, mais il reste l'un de mes préférés.

### Table des matières

* Comment fonctionne l'algorithme minimax
* Limites de l'algorithme minimax
* Comment améliorer la complexité temporelle de l'algorithme
* Code de l'IA pour le Tic-Tac-Toe
* Conclusion

## Comment fonctionne l'algorithme Minimax

La méthodologie de l'algorithme minimax est assez simple. Tout d'abord, il vérifie toutes les combinaisons possibles à partir d'une position donnée. Ensuite, il choisit le meilleur coup possible qui maximise les chances de gagner, en supposant que les deux joueurs jouent parfaitement.

Pour illustrer cela, considérons un jeu de Tic-Tac-Toe pour rendre cela plus convaincant. Comme vous le savez peut-être, dans ce jeu, il y a 2 joueurs et 9 cases disponibles. Nous pouvons donc représenter un jeu en utilisant un tableau de longueur 9.

Prenons maintenant ce tableau comme exemple : comme vous pouvez le voir, un tableau de jeu est un tableau de longueur 9 dont les valeurs peuvent être soit **X**, **O**, soit une chaîne vide. Une chaîne vide signifie que cette position est encore disponible.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/new1.jpg)
_Tableau de jeu en tableau de jeu_

Maintenant, c'est au tour de **X**. L'algorithme minimax essaiera toutes les combinaisons de jeu à partir de cette position. Ensuite, il essaiera toutes les combinaisons de jeu à partir des positions enfants résultantes jusqu'à atteindre une position où le jeu se termine soit par une victoire de X, une victoire de O, soit par un match nul (qui se produit lorsque le tableau est plein et que personne ne gagne).

Cette image illustre comment cela fonctionne :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/new2.jpg)
_Démonstration de toutes les combinaisons de jeu_

Nous pouvons réaliser cela en utilisant la récursivité. Je montrerai le code à la fin, mais pour l'instant, concentrons-nous sur la compréhension de la manière dont nous pouvons traiter les combinaisons de jeu pour obtenir le meilleur coup. Nous considérerons ces cas :

* Le tableau qui a une position gagnante pour X est évalué à **1 point**
* Le tableau qui a une position gagnante pour O est évalué à -**1 point**
* Le tableau où la position est un match nul a **0 point**

Si nous cherchons le meilleur coup pour X, nous devrions trouver le tableau avec le plus de points. Mais que faire si un tableau n'est pas encore terminé ? Alors nous devrions choisir un tableau en fonction de ses tableaux enfants – mais lequel choisir ?

J'ai besoin que vous vous concentriez sur cette partie, car c'est la plus importante. Lorsque j'ai introduit l'algorithme, j'ai dit qu'il trouve toutes les combinaisons de jeu en supposant que les deux joueurs jouent de manière optimale.

Après la première génération de tableaux enfants, ce sera au tour de O. Avec l'hypothèse que O joue de manière optimale, nous devrions choisir un tableau où O fait de son mieux, c'est-à-dire l'un des tableaux avec le moins de points (puisque lorsque O gagne, le tableau retourne -1).

Pourquoi choisissons-nous ainsi ? Imaginez si nous choisissons la valeur maximale lorsque c'est au tour de O, alors nous laissons X gagner. Cela rend l'algorithme inutile, puisque nous devons supposer que O joue de manière optimale.

Pour la 3ème génération, le joueur est X à nouveau et nous choisirons le tableau avec le plus de points une fois de plus.

Cette méthode alternée de choix des valeurs maximales et minimales est la raison pour laquelle cet algorithme est appelé l'algorithme Minimax. Consultez cette visualisation pour plus de clarté :

![Image](https://www.freecodecamp.org/news/content/images/2022/12/new3.jpg)
_Mécanisme Minimax_

C'est le même exemple donné ci-dessus. Les 2 tableaux en bas sont gagnants pour X, donc chacun retournera une valeur de 1. Ici, c'est au tour de X, donc nous choisirons la valeur optimale - il se trouve que les deux tableaux ont une valeur de 1 ici.

Comme je l'ai dit plus tôt, si un tableau ne satisfait pas les conditions de victoire ou de match nul, nous regarderons ses tableaux enfants. C'est pourquoi les parents des tableaux avec une valeur de 1 auront une valeur de 1.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/new4.jpg)
_Mécanisme de l'algorithme Minimax_

Ici, c'est au tour de O, donc nous choisirons la valeur la plus basse possible, qui se trouve être 1. J'ai choisi cet exemple spécifique pour simplifier les choses, mais cela fonctionne sur tous les tableaux.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/new5.jpg)
_Mécanisme Minimax_

Enfin, c'est à nouveau au tour de X et nous maximiserons la valeur du tableau choisi. C'est pourquoi nous pouvons choisir le tableau enfant à gauche ou celui à droite ou celui au milieu – cela n'a pas d'importance puisque leurs valeurs sont les mêmes.

En fin de compte, le meilleur coup pour X pour maximiser ses chances de gagner est aux positions 7, 8 ou 9. Si vous n'êtes toujours pas convaincu, prenez n'importe quelle combinaison de tableau et dessinez l'arbre de combinaison et vous obtiendrez un résultat satisfaisant – je recommande fortement de dessiner cela sur papier.

## Limites de l'algorithme Minimax

Comme vous l'avez vu, l'algorithme est récursif et le nombre d'exécutions peut devenir énorme.

Par exemple, pour un jeu de Tic-Tac-Toe, le nombre d'exécutions est d'environ **«9!» (9 factoriel)**. La raison en est que pour le premier coup, il y a 9 possibilités, puis pour chaque coup suivant, il y en a 8, et ainsi de suite.

Ce n'est pas un problème pour le tic-tac-toe, mais considérons un jeu d'échecs. Si nous devions écrire le nombre de combinaisons, l'univers entier ne suffirait pas. Donc le minimax est souvent utilisé comme partie d'un moteur, mais ce n'est pas suffisant pour répondre à nos besoins.

## Comment améliorer la complexité temporelle de l'algorithme

Vous avez peut-être remarqué que l'utilisation de cette approche peut entraîner des tableaux répétitifs et que nous devons calculer leur valeur plusieurs fois. Alors pourquoi ne pas stocker la valeur de chaque tableau une fois calculée ?

Donc maintenant, pour chaque itération, nous vérifierons si une position s'est déjà produite. Si c'est le cas, nous utiliserons sa valeur stockée. Sinon, nous pouvons calculer la valeur de la position et la stocker.

Pour stocker les valeurs, nous utiliserons un dictionnaire qui permet une recherche en O(1). En utilisant cette approche, nous pouvons réduire la complexité temporelle – mais elle ne serait toujours pas efficace dans certains cas.

J'ai construit un jeu de Connect 4 avec cet algorithme et il était horrible en termes de temps d'exécution. Donc, au lieu de chercher toutes les combinaisons, je me suis arrêté à une certaine profondeur, ce qui a conduit à une IA capable de voir n coups à l'avance.

Si vous êtes intéressé, consultez ce [dépôt GitHub](https://github.com/HousseinBadra/badraconnect4AI.github.io.git) pour le code du jeu Connect 4. Je l'ai écrit il y a longtemps, mais c'est cool à voir.

## Code de l'IA pour le Tic-Tac-Toe

Maintenant, implémentons d'abord quelques fonctions auxiliaires. Nous vérifierons d'abord s'il y a 3 valeurs de chaîne non vides horizontales, verticales ou diagonales dans le tableau de jeu.

```javascript
// Tableau de jeu
let xo=['','','',
        '','','',
        '','','']

// En écrivant cette fonction, nous devons nous assurer que les valeurs égales ne sont pas des chaînes vides

// Avant cela, je vais écrire une fonction auxiliaire pour m'assurer que 3 index n'ont pas de chaînes vides

function helper(index1,index2,index3){
  return xo[index1] !='' && xo[index2] !='' && xo[index3]!=''
}



function checkwin(){
  
   return (xo[0]==xo[1] && xo[1] ==xo[2] && helper(0,1,2)) ||
          (xo[3]==xo[4] && xo[4] ==xo[5] && helper(3,4,5)) ||
          (xo[6]==xo[7] && xo[7] ==xo[8] && helper(6,7,8)) ||
          (xo[0]==xo[3] && xo[3] ==xo[6] && helper(0,3,6)) ||
          (xo[1]==xo[4] && xo[4] ==xo[7] && helper(1,4,7)) || 
          (xo[2]==xo[5] && xo[5] ==xo[8] && helper(2,5,8)) ||
          (xo[0]==xo[4] && xo[4] ==xo[8] && helper(0,4,8)) ||
          (xo[2]==xo[4] && xo[4] ==xo[6] && helper(2,4,6))
   
}

//Et enfin une fonction pour vérifier s'il y a un match nul, qui vérifiera si toutes les valeurs du tableau ne sont pas des chaînes vides. Cela ne fonctionne qu'après avoir vérifié qu'il n'y a pas de conditions de victoire d'abord

function boardfull(){
  return xo.every((elem)=>{
   return elem !=''
  })
}
```

Maintenant, nous avons la fonction pour vérifier si un état gagnant est présent et nous pouvons enfin écrire le Minimax comme ceci (j'ai ajouté des commentaires dans le code pour aider à l'expliquer) :

```javascript
// Comme je l'ai dit plus tôt, l'algorithme prendra le tableau, le paramètre ismax pour vérifier si nous voulons maximiser ou minimiser pour un certain tour

function minimax(board,depth,ismax){
    
    // C'est une fonction récursive, donc nous devons d'abord définir les cas de base qui seront obtenir un match nul, une victoire ou atteindre la profondeur
    
    // Comme vous l'avez vu dans les visualisations, lorsqu'il y a un match nul ou des conditions de victoire, plus de tableaux enfants ne sont générés. Donc si une condition de victoire s'est produite lorsque c'est au tour de X. C'est X qui a gagné, c'est pourquoi j'ai retourné 1, et la même logique s'applique lorsque Y a gagné et j'ai retourné -1 lorsque nous minimisions.
    
    if (checkwin()) return ismax ? 1 : -1
    if (boardfull()) return 0
      
    if(ismax){
        
        // Lorsque nous maximisons, nous allons définir un compteur à -Infinity et chaque fois que nous rencontrons une valeur de tableau supérieure au compteur, nous la considérerons comme le meilleur coup
        
     let best=-Infinity
     board.forEach((elem,index)=>{
         
         //Maintenant, pour vérifier toutes les positions résultantes, nous allons itérer sur le tableau et chaque fois qu'il y a une case disponible, nous la définirons à X et exécuterons minimax sur cette position. Regardez comment j'ai incrémenté la profondeur
         
     if(elem ==''){
       board[index]='X'
       let  localscores=minimax(test,depth+1,false)
       
       // Ici, je réinitialise le tableau à la même position 
       
       board[index]=''
       best=max(best,localscores)
     }})
     return best
     }
    
 // Ce else ici signifie que nous minimisons
    
 else{
 
     // Ici, nous allons définir notre compteur à + Infinity car nous voulons trouver la valeur la plus basse possible
     
    let best=Infinity
    board.forEach((elem,index)=>{
    if(elem ==''){
     board[index]=humanicon
     let localscores=minimax(test,depth+1,true)
     board[index]=''
     best=min(best,localscores)
    }})
    return best
  }
}
```

Et maintenant, nous avons terminé !

## Conclusion

Dans cet article, nous avons appris l'algorithme minimax, son mécanisme, ses limites et comment l'améliorer. Maintenant, vous pouvez aller et personnaliser cela pour travailler sur divers jeux afin de créer des bots de jeu cool.

En fin de compte, j'espère que vous avez appris quelque chose de nouveau dans cet article.

Si vous avez trouvé cela utile et que vous souhaitez obtenir plus de contenu génial, [suivez-moi sur LinkedIn](https://www.linkedin.com/in/houssein-badra-943879214). Cela aidera beaucoup.