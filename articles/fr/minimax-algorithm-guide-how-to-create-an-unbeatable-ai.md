---
title: 'Guide de l''algorithme Minimax : Comment créer une IA invincible'
subtitle: ''
author: Oluwatobi Sofela
co_authors: []
series: null
date: '2020-12-09T16:16:23.000Z'
originalURL: https://freecodecamp.org/news/minimax-algorithm-guide-how-to-create-an-unbeatable-ai
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fc9fb8be6787e0983939c87.jpg
tags:
- name: algorithms
  slug: algorithms
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Game Development
  slug: game-development
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
seo_title: 'Guide de l''algorithme Minimax : Comment créer une IA invincible'
seo_desc: "Recently I wondered – how can I program the computer to be unbeatable in\
  \ a tic-tac-toe game? \nWell, I thought I could easily get an answer to this question.\
  \ But as I went back and forth from articles to videos to a series of coding meditations,\
  \ I onl..."
---

Récemment, je me suis demandé – comment puis-je programmer l'ordinateur pour qu'il soit invincible dans un jeu de morpion ?

Eh bien, j'ai pensé que je pourrais facilement obtenir une réponse à cette question. Mais alors que je passais d'articles en vidéos à une série de méditations codantes, je n'ai réussi qu'à devenir plus confus.

Cependant, mon moment « Aha ! » est arrivé lorsque j'ai pris le temps de comprendre comment fonctionne l'**algorithme minimax**.

Si vous êtes également sur un chemin similaire, laissez-moi vous guider à travers les étapes pour construire une IA invincible (Intelligence Artificielle).

## Étape 1 : Comprendre les bases de l'algorithme minimax

Un **algorithme minimax** est un programme [récursif](https://www.codesweetly.com/recursion/) écrit pour trouver le meilleur gameplay qui minimise toute tendance à perdre un jeu tout en maximisant toute opportunité de gagner le jeu.

Graphiquement, nous pouvons représenter le minimax comme une exploration des [nœuds](https://en.wikipedia.org/wiki/Node_(computer_science)) d'un [arbre de jeu](https://en.wikipedia.org/wiki/Game_tree) pour découvrir le meilleur coup à faire. Dans un tel cas, la racine de l'arbre est l'état actuel du jeu — où l'algorithme minimax a été invoqué.

![Arbre de jeu du morpion](https://www.freecodecamp.org/news/content/images/2020/12/game-tree-for-tic-tac-toe-minimax-codesweetly.png)
_Figure 1 : L'arbre de jeu d'une partie de morpion en cours de conclusion_

Notre objectif dans ce guide est d'utiliser le minimax pour créer une IA invincible pour un jeu de morpion. Cependant, [vous pouvez également l'utiliser pour des jeux complexes](https://en.wikipedia.org/wiki/Minimax), comme les échecs, et pour la prise de décision générale afin de résoudre toute incertitude.

Dans la plupart des cas, le joueur qui invoque initialement le minimax est appelé le _joueur maximisant_. En d'autres termes, l'invocateur original du minimax est le joueur qui veut maximiser toute opportunité de gagner le jeu.

En revanche, l'opposant du joueur maximisant est appelé le _joueur minimisant_. Ainsi, le joueur minimisant est le joueur dont les chances de gagner doivent être minimisées.

En bref, un algorithme minimax est une fonction récursive créée pour aider un joueur (le maximiseur) à décider du gameplay qui _minimise_ la possibilité _maximale_ de perdre un jeu.

## Étape 2 : Familiarisez-vous avec le nœud racine de ce tutoriel

Pour rendre ce tutoriel précis, le nœud racine (l'état actuel du jeu de morpion) que nous utiliserons sera un plateau de jeu proche de la fin — comme illustré dans la figure 2 ci-dessous.

De plus, la marque **X** représentera la marque de l'IA, tandis que la marque **O** sera celle du joueur humain.

![L'état initial du plateau de morpion de ce tutoriel](https://www.freecodecamp.org/news/content/images/2020/12/root-node-for-tic-tac-toe-minimax-tutorial-codesweetly.png)
_Figure 2 : Le nœud racine de ce tutoriel_

À l'étape actuelle du jeu de morpion (comme illustré dans la figure 2 ci-dessus), c'est au tour de **X** de jouer (c'est-à-dire le tour de l'IA). Et comme il y a trois cellules vides sur le plateau, cela implique que **X** a trois choix de jeu possibles — milieu-haut, centre ou bas-droite.

Mais quel est le meilleur choix ? Quel mouvement aidera le mieux **X** à minimiser la possibilité maximale de perdre le jeu ?

![Mouvements possibles du joueur IA](https://www.freecodecamp.org/news/content/images/2020/12/ai-player-first-possible-moves-minimax-tic-tac-toe-codesweetly.png)
_Figure 3 : Choix de jeu possibles du joueur IA_

Pour prendre la meilleure décision, l'IA doit faire ce qui suit :

1. Stocker l'état actuel (valeurs) du plateau de morpion dans un tableau. (Pour toute cellule vide, l'index de la cellule sera stocké comme son contenu actuel).
2. Obtenir une liste de tableau _uniquement des index des cellules vides_.
3. Vérifier et confirmer si un joueur spécifique a gagné le jeu.
4. Invoquer [récursivement](https://www.codesweetly.com/recursion/) _minimax_ sur chacune des cellules vides du plateau.
5. Retourner un score pour chaque mouvement possible pour les joueurs **X** et **O**.
6. Parmi tous les scores retournés, choisir le meilleur (le plus élevé) qui est garanti pour minimiser les possibilités de gain du joueur humain.

Par conséquent, dans les étapes suivantes ci-dessous, nous allons configurer l'IA pour accomplir la liste ci-dessus. Alors, commençons par stocker l'état actuel du plateau dans un tableau.

## Étape 3 : Stocker l'état actuel du plateau dans un tableau

Notre prochaine étape est de stocker le contenu actuel de chacune des cellules du plateau dans un tableau comme suit :

```js
const currentBoardState = ["X", 1, "O", "X", 4, "X", "O", "O", 8];
```

**Note :**

* L'état actuel de notre plateau de morpion est toujours tel qu'illustré dans la figure 2.
* Les valeurs `1`, `4` et `8` dans le tableau `currentBoardState` sont les numéros d'index des cellules vides du plateau. En d'autres termes, au lieu d'utiliser des chaînes vides, nous avons choisi de stocker le contenu actuel des cellules vides comme leurs index respectifs.

Importamment, avant de passer à l'étape suivante, définissons explicitement à qui appartient la marque « X » et qui possède « O ».

```js
const aiMark = "X";
const humanMark = "O";
```

Les deux déclarations ci-dessus indiquent que la marque de l'IA est **X** tandis que celle du joueur humain est **O**.

## Étape 4 : Créer une fonction pour obtenir les index de toutes les cellules vides

La fonction ci-dessous filtrera le tableau `currentBoardState` — qui sera passé en tant qu'argument du paramètre de la fonction. Elle retournera ensuite un nouveau tableau contenant tous les éléments du tableau `currentBoardState` qui ne sont ni « X » ni « O ».

```js
function getAllEmptyCellsIndexes(currBdSt) {
    return currBdSt.filter(i => i != "X" && i != "O");
}
```

**Note :** Rappelez-vous que le tableau `currentBoardState` que nous avons créé à l'étape 3 contient uniquement les valeurs « X », « O » et _les index des cellules vides du plateau_. Par conséquent, la fonction `getAllEmptyCellsIndexes()` ci-dessus filtre toute occurrence d'un index dans le tableau `currentBoardState`.

## Étape 5 : Créer une fonction de détermination du gagnant

Le but principal de la _fonction de détermination du gagnant_ ci-dessous est de recevoir un tableau `currentBoardState` et la marque d'un joueur spécifique (soit la marque « X » ou « O ») en tant qu'arguments de ses paramètres.

Ensuite, elle vérifie si la marque reçue forme une combinaison gagnante sur le plateau de morpion. Si c'est le cas, la valeur booléenne `true` est retournée — sinon, `false` est retournée.

```js
function checkIfWinnerFound(currBdSt, currMark) {
    if (
        (currBdSt[0] === currMark && currBdSt[1] === currMark && currBdSt[2] === currMark) ||
        (currBdSt[3] === currMark && currBdSt[4] === currMark && currBdSt[5] === currMark) ||
        (currBdSt[6] === currMark && currBdSt[7] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[3] === currMark && currBdSt[6] === currMark) ||
        (currBdSt[1] === currMark && currBdSt[4] === currMark && currBdSt[7] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[5] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[4] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[4] === currMark && currBdSt[6] === currMark)
    ) {
        return true;
    } else {
        return false;
    }
}
```

## Étape 6 : Créer l'algorithme minimax

Un **algorithme minimax** est simplement une fonction ordinaire qui contient des instructions à exécuter une fois la fonction invoquée. Par conséquent, le processus de création de l'algorithme est le même que celui de création de toute autre fonction. Alors, créons-en une maintenant.

```js
function minimax(currBdSt, currMark) {
    
    // Espace pour les instructions du minimax 
    
}
```

C'est tout ! Nous avons créé une fonction **minimax** — bien qu'elle soit vide. Notre prochaine étape est de remplir la fonction avec des instructions qui seront exécutées une fois la fonction invoquée — ce que nous ferons ci-dessous.

**Note :** La fonction minimax créée ci-dessus est conçue pour accepter _deux arguments_. Le premier est _un tableau_ de liste du contenu actuel du plateau — c'est-à-dire, la valeur actuelle du tableau `currentBoardState`. Alors que le deuxième argument est _la marque_ du joueur qui exécute actuellement l'algorithme minimax — c'est-à-dire, la marque « X » ou la marque « O ».

## Étape 7 : Première invocation de minimax

Pour éviter toute confusion plus tard dans ce tutoriel, invoquons notre fonction minimax pour la première fois — tout en passant le tableau `currentBoardState` et la `aiMark` en tant qu'arguments de la fonction.

```js
const bestPlayInfo = minimax(currentBoardState, aiMark);
```

## Étape 8 : Stocker les index de toutes les cellules vides

Dans cette étape, nous allons invoquer la fonction `getAllEmptyCellsIndexes` que nous avons créée à l'étape 4 — tout en passant le tableau `currentBoardState` en tant qu'argument de la fonction.

Ensuite, nous stockerons la liste de tableau _retournée_ des index à l'intérieur d'une variable nommée `availCellsIndexes`.

```js
const availCellsIndexes = getAllEmptyCellsIndexes(currBdSt);
```

## Étape 9 : Vérifier s'il y a un état terminal

À ce stade, nous devons vérifier s'il y a un état terminal (c'est-à-dire un état de perte, un état de victoire ou un état de match nul) sur le plateau de morpion. Nous accomplirons cette vérification en invoquant la _fonction de détermination du gagnant_ (créée à l'étape 5) pour chacun des joueurs.

Si la fonction trouve un état de victoire pour le joueur humain (le minimiseur), elle retournera `-1` (ce qui signifie que le joueur humain a gagné, et que l'IA a perdu). Mais si elle trouve un état de victoire pour le joueur IA (le maximiseur), elle retournera `+1` (ce qui indique que l'IA a gagné, et que le joueur humain a perdu).

Cependant, supposons que la fonction de détermination du gagnant ne trouve aucune cellule vide sur le plateau ou aucun état de victoire pour l'un ou l'autre joueur. Dans ce cas, elle retournera `0` (zéro) — ce qui signifie que le jeu s'est terminé par un match nul.

**Note :** Les scores (`-1`, `+1` et `0`) indiqués ci-dessus sont des valeurs [heuristiques](https://www.vocabulary.com/dictionary/heuristic) — ce qui signifie que nous obtiendrons toujours le même résultat si nous préférons utiliser -25, +25 et 0.

Procéderons maintenant à la mise en œuvre de la vérification de l'état terminal en utilisant une _instruction if_ comme suit :

```js
if (checkIfWinnerFound(currBdSt, humanMark)) {
    return {score: -1};
} else if (checkIfWinnerFound(currBdSt, aiMark)) {
    return {score: 1};
} else if (availCellsIndexes.length === 0) {
    return {score: 0};
}
```

Lorsque qu'il y a un état terminal (perte, victoire ou match nul), la fonction minimax active retournera le score d'état terminal approprié (`-1`, `+1` ou `0`) et mettra fin à son invocation.

Si le minimax actif met fin à son invocation ici, l'algorithme passera à l'étape 12.

Cependant, lorsqu'il n'y a _pas_ d'état terminal, la fonction minimax active exécutera l'instruction suivante (étape 10, ci-dessous).

## Étape 10 : Préparez-vous à tester le résultat du placement de la marque du joueur actuel sur chaque cellule vide

Comme l'étape 9 n'a trouvé aucun état terminal, nous devons trouver un moyen de tester ce qui se passera si le joueur actuel (qui doit faire le prochain mouvement du jeu) joue sur chaque cellule vide.

En d'autres termes, si le joueur actuel joue sur la première cellule disponible, et que l'opposant joue sur la deuxième cellule vide, le joueur actuel gagnera-t-il, perdra-t-il ou fera-t-il match nul ? Ou n'y aura-t-il toujours aucun état terminal trouvé ?

Alternativement, que se passera-t-il si le joueur actuel joue sur la deuxième cellule disponible, et que l'opposant joue sur la première cellule vide ?

Ou peut-être, la troisième cellule disponible sera-t-elle le meilleur endroit pour que le joueur actuel joue ?

C'est ce test que nous devons faire maintenant. Mais avant de commencer, nous avons besoin d'un endroit pour enregistrer le résultat de chaque test — alors créons d'abord un tableau nommé `allTestPlayInfos`.

```js
const allTestPlayInfos = [];
```

Maintenant que nous avons sécurisé un endroit pour stocker le résultat de chaque essai, commençons les essais en créant une _instruction de boucle for_ qui parcourra chacune des cellules vides en commençant par la première.

```js
for (let i = 0; i < availCellsIndexes.length; i++) {
    
    // Espace pour les codes de la boucle for
    
}
```

Dans les deux étapes suivantes, nous remplirons la boucle for avec le code qu'elle doit exécuter pour chaque cellule vide.

## Étape 11 : Tester le placement de la marque du joueur actuel sur la cellule vide que la boucle for traite actuellement

Avant de faire quoi que ce soit dans cette étape, examinons l'état actuel de notre plateau.

![Plateau de morpion actuel](https://www.freecodecamp.org/news/content/images/2020/12/current-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 4 : L'état actuel du plateau de morpion_

Remarquez que le plateau ci-dessus est toujours le même que celui de la figure 2, sauf que nous avons mis en surbrillance — en rouge — la cellule que la boucle for traite actuellement.

Ensuite, il sera utile d'avoir un endroit pour stocker le score terminal de ce test — alors créons un objet comme suit :

```js
const currentTestPlayInfo = {};
```

De plus, avant de tester le placement de la marque du joueur actuel sur la cellule rouge, sauvegardons le numéro d'index de la cellule — afin qu'il soit facile de réinitialiser les informations de la cellule après ce test.

```js
currentTestPlayInfo.index = currBdSt[availCellsIndexes[i]];
```

Placons maintenant la marque du joueur actuel sur la cellule rouge (c'est-à-dire, la cellule actuellement traitée par la boucle for).

```js
currBdSt[availCellsIndexes[i]] = currMark;
```

Sur la base du gameplay du joueur actuel, l'état du plateau changera pour refléter son dernier mouvement.

![Nouveau plateau de morpion](https://www.freecodecamp.org/news/content/images/2020/12/ai-latest-move-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 5 : Le nouveau plateau — qui reflète le dernier mouvement du joueur actuel_

Par conséquent, puisque l'état du plateau a changé, nous devons exécuter récursivement minimax sur le nouveau plateau — tout en passant l'état du nouveau plateau et la marque du joueur suivant.

```js
if (currMark === aiMark) {
    const result = minimax(currBdSt, humanMark);
    currentTestPlayInfo.score = result.score;
} else {
    const result = minimax(currBdSt, aiMark);
    currentTestPlayInfo.score = result.score;
}
```

**Note :**

* L'invocation récursive de minimax à ce point précis sera la _____ fois que nous invoquons la fonction. La première invocation a eu lieu à l'étape 7.
* Cette invocation récursive provoquera la réitération des étapes 8 à 11.
* Supposons qu'il y ait un état terminal à l'étape 9. Dans ce cas, l'invocation actuelle de minimax cessera de s'exécuter — et stockera l'objet terminal retourné (par exemple, `{score: 1}`) dans la variable `result`.
* Une fois qu'il y a un état terminal, l'étape 12 sera l'étape suivante.
* Si _aucun_ état terminal n'existe, une **deuxième boucle for** commencera pour le nouveau plateau à l'étape 10.
* Si l'étape 10 est répétée, veuillez remplacer le plateau de la figure 4 par le nouveau plateau de la figure 5. Cependant, la cellule mise en surbrillance en rouge sera maintenant la cellule que la boucle for traite actuellement. Veuillez donc refléter les changements en conséquence.

## Étape 12 : Enregistrer le dernier score terminal

Après que l'invocation minimax récemment conclue a retourné la valeur de son état terminal, la boucle for active enregistrera le score de la variable `result` dans l'objet `currentTestPlayInfo` comme suit :

```js
currentTestPlayInfo.score = result.score;
```

Ensuite, puisque le score retourné met officiellement fin au test actuel, il est préférable de réinitialiser le plateau actuel à l'état où il était avant que le joueur actuel ne fasse son mouvement.

```js
currBdSt[availCellsIndexes[i]] = currentTestPlayInfo.index;
```

De plus, nous devons enregistrer le résultat du test du joueur actuel pour une utilisation future. Alors, faisons cela en poussant l'objet `currentTestPlayInfo` dans le tableau `allTestPlayInfos` comme suit :

```js
allTestPlayInfos.push(currentTestPlayInfo);
```

**Note :**

* Si vous êtes arrivé à cette étape depuis l'étape 17, veuillez continuer ce tutoriel à l'_étape 18_. Sinon, considérons le point suivant.
* Si la boucle for active a terminé de parcourir toutes les cellules vides du plateau actuel, la boucle se terminera à ce point, et l'_étape 14_ sera la suivante. Sinon, la boucle procédera au traitement de la cellule disponible suivante (étape 13).

## Étape 13 : Exécuter la boucle for active sur la cellule vide suivante

Rappelez-vous que la boucle for actuellement active (qui a commencé à l'étape 10) n'a terminé son travail que pour la ou les cellules vides précédentes. Par conséquent, la boucle procédera au test du placement de la marque du joueur actuel sur la cellule libre suivante.

En d'autres termes, la fonction minimax en cours d'exécution répétera les étapes **11** et **12**. Mais, essentiellement, notez ce qui suit :

* La cellule rouge mise en surbrillance dans la figure 4 changera pour la cellule que la boucle for traite actuellement.
* Veuillez noter que la figure 5 changera également. En d'autres termes, le mouvement du joueur actuel sera maintenant sur la cellule que la boucle for traite actuellement.
* Après que la boucle for active a terminé son travail, le tableau `allTestPlayInfos` contiendra des objets spécifiques pour chaque cellule vide que la boucle for a traitée.
* Chacun des objets dans le tableau `allTestPlayInfos` contiendra une propriété `index` et une propriété `score` (par exemple : `{index: 8, score: -1}`).
* Si vous êtes arrivé à cette étape depuis l'étape 20, alors, _après avoir terminé l'étape 12_, veuillez continuer ce tutoriel à l'_étape 18_.

## Étape 14 : Planifier comment obtenir l'objet avec le meilleur score de test pour le joueur actuel

Immédiatement après que la boucle for a terminé son travail de parcours de toutes les cellules vides du plateau actuel, minimax :

1. **Créera un espace** pour stocker le numéro de référence qui aidera plus tard à obtenir le meilleur objet de test.
2. **Obtiendra le numéro de référence** du meilleur test du joueur actuel.
3. **Utilisera le numéro de référence acquis** pour obtenir l'objet avec le meilleur test pour le joueur actuel.

Sans plus tarder, mettons en œuvre ce plan dans les prochaines étapes.

## Étape 15 : Créer un stockage pour la référence du meilleur test

La variable ci-dessous est l'endroit où nous stockerons plus tard la référence à l'objet du meilleur test. (Notez que la valeur `null` indique que nous avons délibérément laissé la variable vide).

```js
let bestTestPlay = null;
```

## Étape 16 : Obtenir la référence au meilleur test du joueur actuel

Maintenant qu'il y a un stockage `bestTestPlay`, la fonction minimax active peut procéder à l'obtention de la référence au meilleur test du joueur actuel comme suit :

```js
if (currMark === aiMark) {
    let bestScore = -Infinity;
    for (let i = 0; i < allTestPlayInfos.length; i++) {
        if (allTestPlayInfos[i].score > bestScore) {
            bestScore = allTestPlayInfos[i].score;
            bestTestPlay = i;
        }
    }
} else {
    let bestScore = Infinity;
    for (let i = 0; i < allTestPlayInfos.length; i++) {
        if (allTestPlayInfos[i].score < bestScore) {
            bestScore = allTestPlayInfos[i].score;
            bestTestPlay = i;
        }
    }
}
```

Le code ci-dessus signifie que si la marque actuelle est égale à la marque du joueur IA :

1. Créez une variable `bestScore` avec la valeur `-Infinity`. (Notez que cette valeur est simplement une valeur de remplissage qui doit être _inférieure à_ tous les scores dans le tableau `allTestPlayInfos`. Par conséquent, utiliser `-700` fera le même travail).
2. Ensuite, pour chaque objet de test dans le tableau `allTestPlayInfos`, vérifiez si le test que la boucle traite actuellement a un score _plus élevé_ que le `bestScore` actuel. Si c'est le cas, enregistrez les détails de ce test à l'intérieur des variables `bestScore` et `bestTestPlay`.

Sinon, si la marque actuelle est celle du joueur humain :

1. Créez une variable `bestScore` avec la valeur `+Infinity`. (Encore une fois, notez que nous obtiendrions le même résultat si nous avions préféré utiliser `+300`. C'est simplement une valeur de remplissage qui doit être _supérieure à_ tous les scores dans le tableau `allTestPlayInfos`).
2. Ensuite, pour chaque objet de test dans le tableau `allTestPlayInfos`, vérifiez si le test que la boucle traite actuellement a un score _inférieur_ au `bestScore` actuel. Si c'est le cas, enregistrez les détails de ce test à l'intérieur des variables `bestScore` et `bestTestPlay`.

## Étape 17 : Obtenir l'objet avec le meilleur score de test pour le joueur actuel

Enfin, l'invocation minimax actuellement en cours peut maintenant terminer son travail en retournant l'objet avec le meilleur test pour le joueur actuel comme suit :

```js
return allTestPlayInfos[bestTestPlay];
```

Notez que minimax stockera l'objet retourné à l'intérieur de la variable `result` de la première boucle for qui a commencé à l'étape 11. Il répétera ensuite l'étape 12. Veuillez revisiter uniquement l'étape 12. Ensuite, continuez ce tutoriel ci-dessous.

## Étape 18 : Faisons une révision

Cette étape est un excellent moment pour réviser ce que nous avons fait jusqu'à présent de manière picturale.

**Note :**

* Si c'est votre première fois à cette étape, veuillez utiliser le diagramme de l'_étape 19_.
* Est-ce votre deuxième fois à cette étape ? Si oui, le diagramme de l'_étape 21_ est le vôtre.
* Êtes-vous ici pour la troisième fois ? Bien joué ! Consultez le diagramme de l'_étape 23_.

## Étape 19 : Traçage de nos étapes avec un diagramme

Le diagramme ci-dessous montre le _premier test_ de l'IA et du joueur humain pour la première invocation de la boucle for initiée par le joueur IA.

![Premier test de morpion](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-first-test-play-codesweetly-1.png)
_Figure 6 : Premier test qui prédit un état de perte pour l'IA (maximiseur)_

## Étape 20 : La première boucle for avance pour traiter la cellule vide suivante

En concluant que jouer sur la première cellule vide se terminera par un état de perte, l'IA avance pour tester le résultat de jouer sur la _deuxième cellule libre_ en répétant l'étape 13.

## Étape 21 : Traçage de nos étapes avec un diagramme

Le diagramme ci-dessous montre le _deuxième test_ de l'IA et du joueur humain pour la première invocation de la boucle for initiée par le joueur IA.

![Deuxième test de morpion](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-second-test-play-codesweetly-1.png)
_Figure 7 : Deuxième test qui prédit un état de victoire pour l'IA (maximiseur)_

## Étape 22 : La première boucle for avance pour traiter la cellule vide suivante

Maintenant que l'IA a confirmé que jouer sur la deuxième cellule vide entraînera un état de victoire, elle vérifie davantage le résultat de jouer sur la _troisième cellule libre_ en répétant l'étape 13.

## Étape 23 : Traçage de nos étapes avec un diagramme

Le diagramme ci-dessous montre le _troisième test_ de l'IA et du joueur humain pour la première invocation de la boucle for initiée par le joueur IA.

![Troisième test de morpion](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-third-test-play-codesweetly-1.png)
_Figure 8 : Troisième test qui prédit un état de perte pour l'IA (maximiseur)_

## Étape 24 : Obtenir l'objet avec le meilleur score de test pour le joueur IA

À ce stade (après le troisième test), la première boucle for aurait traité les trois cellules vides du premier plateau (passé à minimax à l'étape 7).

Par conséquent, minimax avancera pour obtenir l'objet avec le meilleur test pour le joueur IA — en répétant les étapes 15 à 17. Cependant, _lors de l'étape 17_, veuillez noter ce qui suit :

* L'objet retourné sera maintenant stocké dans la variable `bestPlayInfo` que nous avons créée à l'étape 7.
* Minimax ne répétera pas l'étape 12 car l'instruction de la boucle for n'est plus active.

![Aperçu de tous les tests et scores de morpion](https://www.freecodecamp.org/news/content/images/2020/12/tic-tac-toe-minimax-view-of-all-test-plays-codesweetly-1.png)
_Figure 9 : Aperçu de tous les tests et scores_

## Étape 25 : Utiliser les données à l'intérieur de bestPlayInfo

En considérant le plateau de ce tutoriel (un plateau de jeu proche de la fin — comme illustré dans la figure 2 de l'étape 2), l'objet dans la variable `bestPlayInfo` sera `{index: 4, score: 1}`. Par conséquent, l'IA peut maintenant utiliser sa valeur d'index pour choisir la meilleure cellule sur laquelle jouer.

### Exemple

```js
// Obtenir toutes les cellules du plateau :
const gameCells = document.querySelectorAll(".cell");

// Voici la variable que nous avons créée à l'étape 3 :
const aiMark = "X";

// Voici le bestPlayInfo que nous avons créé à l'étape 7 pour contenir le meilleur objet de test pour le joueur IA :
const bestPlayInfo = minimax(currentBoardState, aiMark);

// Jouer la marque de l'IA sur la cellule qui lui est la plus favorable :
gameCells[bestPlayInfo.index].innerText = aiMark;
```

Par conséquent, le joueur IA gagnera le jeu, et le nouveau plateau ressemblera maintenant à ceci :

![Coup gagnant de l'IA](https://www.freecodecamp.org/news/content/images/2020/12/ai-winning-move-tic-tac-toe-minimax-board-codesweetly.png)
_Figure 10 : Plateau de jeu final montrant que l'IA (joueur X) a gagné le jeu_

## Étape 26 : Vue d'ensemble de l'algorithme de ce tutoriel

Voici l'algorithme minimax de ce tutoriel en un seul morceau. N'hésitez pas à l'insérer dans votre éditeur. Jouez avec pour divers scénarios de jeu, et utilisez la console pour le tester, le tester et le tester à nouveau jusqu'à ce que vous soyez à l'aise de construire une IA invincible.

Et rappelez-vous, la programmation est meilleure seulement lorsque vous [codez avec douceur](https://www.codesweetly.com/) — alors amusez-vous bien avec !

```js
// Étape 3 - Stocker l'état actuel du plateau dans un tableau et définir le propriétaire de chaque marque :
const currentBoardState = ["X", 1, "O", "X", 4, "X", "O", "O", 8];
const aiMark = "X";
const humanMark = "O";

// Étape 4 - Créer une fonction pour obtenir les index de toutes les cellules vides :
function getAllEmptyCellsIndexes(currBdSt) {
    return currBdSt.filter(i => i != "O" && i != "X");
}

// Étape 5 - Créer une fonction de détermination du gagnant :
function checkIfWinnerFound(currBdSt, currMark) {
    if (
        (currBdSt[0] === currMark && currBdSt[1] === currMark && currBdSt[2] === currMark) ||
        (currBdSt[3] === currMark && currBdSt[4] === currMark && currBdSt[5] === currMark) ||
        (currBdSt[6] === currMark && currBdSt[7] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[3] === currMark && currBdSt[6] === currMark) ||
        (currBdSt[1] === currMark && currBdSt[4] === currMark && currBdSt[7] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[5] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[0] === currMark && currBdSt[4] === currMark && currBdSt[8] === currMark) ||
        (currBdSt[2] === currMark && currBdSt[4] === currMark && currBdSt[6] === currMark)
) {
        return true;
    } else {
        return false;
    }
}

// Étape 6 - Créer l'algorithme minimax :
function minimax(currBdSt, currMark) {
    // Étape 8 - Stocker les index de toutes les cellules vides :
    const availCellsIndexes = getAllEmptyCellsIndexes(currBdSt);
    
    // Étape 9 - Vérifier s'il y a un état terminal :
    if (checkIfWinnerFound(currBdSt, humanMark)) {
        return {score: -1};
    } else if (checkIfWinnerFound(currBdSt, aiMark)) {
        return {score: 1};
    } else if (availCellsIndexes.length === 0) {
        return {score: 0};
    }
    
    // Étape 10 - Créer un espace pour enregistrer le résultat de chaque essai :
    const allTestPlayInfos = [];
    
    // Étape 10 - Créer une instruction de boucle for qui parcourra chacune des cellules vides :
    for (let i = 0; i < availCellsIndexes.length; i++) {
        // Étape 11 - Créer un espace pour stocker le score terminal de cet essai :
        const currentTestPlayInfo = {};
        
        // Étape 11 - Enregistrer le numéro d'index de la cellule que cette boucle for traite actuellement :
        currentTestPlayInfo.index = currBdSt[availCellsIndexes[i]];
        
        // Étape 11 - Placer la marque du joueur actuel sur la cellule que la boucle for traite actuellement :
        currBdSt[availCellsIndexes[i]] = currMark;
        
        if (currMark === aiMark) {
            // Étape 11 - Exécuter récursivement la fonction minimax pour le nouveau plateau :
            const result = minimax(currBdSt, humanMark);
            
            // Étape 12 - Enregistrer le score de la variable result dans l'objet currentTestPlayInfo :
            currentTestPlayInfo.score = result.score;
        } else {
            // Étape 11 - Exécuter récursivement la fonction minimax pour le nouveau plateau :
            const result = minimax(currBdSt, aiMark);
            
            // Étape 12 - Enregistrer le score de la variable result dans l'objet currentTestPlayInfo :
            currentTestPlayInfo.score = result.score;
        }
        
        // Étape 12 - Réinitialiser le plateau actuel à l'état où il était avant que le joueur actuel ne fasse son mouvement :
        currBdSt[availCellsIndexes[i]] = currentTestPlayInfo.index;
        
        // Étape 12 - Enregistrer le résultat du test du joueur actuel pour une utilisation future :
        allTestPlayInfos.push(currentTestPlayInfo);
    }
    
    // Étape 15 - Créer un stockage pour la référence du meilleur test :
    let bestTestPlay = null;
    
    // Étape 16 - Obtenir la référence au meilleur test du joueur actuel :
    if (currMark === aiMark) {
        let bestScore = -Infinity;
        for (let i = 0; i < allTestPlayInfos.length; i++) {
            if (allTestPlayInfos[i].score > bestScore) {
                bestScore = allTestPlayInfos[i].score;
                bestTestPlay = i;
            }
        }
    } else {
        let bestScore = Infinity;
        for (let i = 0; i < allTestPlayInfos.length; i++) {
            if (allTestPlayInfos[i].score < bestScore) {
                bestScore = allTestPlayInfos[i].score;
                bestTestPlay = i;
            }
        }
    }
    
    // Étape 17 - Obtenir l'objet avec le meilleur score de test pour le joueur actuel :
    return allTestPlayInfos[bestTestPlay];
} 

// Étape 7 - Première invocation de minimax :
const bestPlayInfo = minimax(currentBoardState, aiMark);
```

## Ressource utile

* [Récursivité : Ce que vous devez savoir sur la récursivité](https://www.codesweetly.com/recursion/)