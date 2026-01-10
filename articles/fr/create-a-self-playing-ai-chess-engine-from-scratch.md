---
title: Créer un moteur d'échecs IA auto-joueur à partir de zéro avec l'apprentissage
  par imitation
subtitle: ''
author: Eivind Kjosbakken
co_authors: []
series: null
date: '2023-09-21T08:11:38.000Z'
originalURL: https://freecodecamp.org/news/create-a-self-playing-ai-chess-engine-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/undraw_Programmer_re_owql.png
tags:
- name: AI
  slug: ai
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Python
  slug: python
seo_title: Créer un moteur d'échecs IA auto-joueur à partir de zéro avec l'apprentissage
  par imitation
seo_desc: "This is an article on how I created an AI chess engine, starting completely\
  \ from scratch to building my very own AI chess engine. \nBecause creating an AI\
  \ chess engine from scratch is a relatively complex task, this will be a long article,\
  \ but stay tu..."
---

Cet article explique comment j'ai créé un moteur d'échecs IA, en partant complètement de zéro pour construire mon propre moteur d'échecs IA.

Étant donné que la création d'un moteur d'échecs IA à partir de zéro est une tâche relativement complexe, cet article sera long, mais restez à l'écoute, car le produit final sera un projet intéressant à présenter !

## Prérequis

Cet article expliquera la plupart des concepts en détail. Cependant, il y a quelques prérequis recommandés pour suivre ce tutoriel. Vous devriez être familier avec les éléments suivants :

* Python
* Comment utiliser le terminal
* Jupyter Notebook
* Concepts fondamentaux de l'IA
* Règles des échecs

J'utiliserai également les outils suivants :

* Python
* Différents packages Python
* Stockfish

## Table des matières

* [Partie 1 : Comment générer un ensemble de données](#heading-partie-1-comment-generer-un-ensemble-de-donnees)
* [Partie 2 : Comment encoder les données](#heading-partie-2-comment-encoder-les-donnees)
* [Partie 3 : Comment entraîner le modèle IA](#heading-partie-3-comment-entrainer-le-modele-ia)
* [Conclusion](#heading-conclusion)

## Partie 1 : Comment générer un ensemble de données

Dans cette partie, j'utiliserai Stockfish pour générer un grand ensemble de données de coups à partir de différentes positions. Ces données pourront ensuite être utilisées pour entraîner l'IA d'échecs.

### Comment télécharger Stockfish

Le composant le plus important de mon moteur d'échecs est Stockfish, je vais donc vous montrer comment l'installer.

Rendez-vous sur la [page de téléchargement du site Stockfish](https://stockfishchess.org/download/) et téléchargez la version qui vous convient. J'utilise moi-même Windows, donc j'ai choisi la version Windows (plus rapide) :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_GxqQ42GNX21JB1GN.png)
_Appuyez sur le bouton de téléchargement marqué en rouge si vous avez un PC Windows_

Après le téléchargement, extrayez le fichier zip à l'emplacement de votre choix sur votre PC où vous souhaitez que votre moteur d'échecs soit. N'oubliez pas où vous le placez car vous aurez besoin du chemin pour l'étape suivante.

### Comment incorporer Stockfish avec Python

Maintenant, vous devez également incorporer le moteur dans Python. Vous pourriez le faire manuellement, mais j'ai trouvé plus facile d'utiliser le [package Python Stockfish](https://pypi.org/project/stockfish/) car il contient toutes les fonctions dont vous avez besoin.

Tout d'abord, installez le package à partir de `pip` (de préférence dans votre environnement virtuel) :

```bash
pip install stockfish

```

Vous pouvez ensuite l'importer en utilisant la commande suivante :

```py
from stockfish import Stockfish
stockfish = Stockfish(path=r"C:\Users\eivin\Documents\ownProgrammingProjects18062023\ChessEngine\stockfish\stockfish\stockfish-windows-2022-x86-64-avx2")
```

Notez que vous devez fournir votre propre chemin vers le fichier exécutable de Stockfish :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_MSlKl_UJHCvdpje6.png)
_Le fichier exécutable de stockfish est le deuxième fichier à partir du bas_

Vous pouvez copier le chemin du fichier à partir de la structure des dossiers, ou si vous êtes sur Windows 11, vous pouvez appuyer sur ctrl + shift + c pour copier automatiquement le chemin du fichier.

Super ! Vous avez maintenant Stockfish disponible dans Python !

### Comment générer un ensemble de données

Maintenant, vous avez besoin d'un ensemble de données pour pouvoir entraîner le moteur d'échecs IA ! Vous pouvez le faire en faisant jouer Stockfish et en mémorisant chaque position et les coups que vous pourriez faire à partir de là.

Ces coups seront parmi les meilleurs coups possibles, étant donné que Stockfish est un moteur d'échecs puissant.

Tout d'abord, installez un [package d'échecs](https://pypi.org/project/chess/) et NumPy (il y en a beaucoup à choisir, mais j'utiliserai celui ci-dessous).

Entrez chaque ligne (individuellement) dans le terminal :

```bash
pip install chess
pip install numpy

```

Ensuite, importez les packages (n'oubliez pas d'importer également Stockfish comme montré précédemment dans cet article) :

```py
import chess
import random
from pprint import pprint
import numpy as np
import os
import glob
import time

```

Vous avez également besoin de quelques fonctions d'assistance ici :

```py
#fonctions d'assistance :
def checkEndCondition(board):
 if (board.is_checkmate() or board.is_stalemate() or board.is_insufficient_material() or board.can_claim_threefold_repetition() or board.can_claim_fifty_moves() or board.can_claim_draw()):
  return True
 return False

#sauvegarde
def findNextIdx():
 files = (glob.glob(r"C:\Users\eivin\Documents\ownProgrammingProjects18062023\ChessEngine\data\*.npy"))
 if (len(files) == 0):
  return 1 #si aucun fichier, retourne 1
 highestIdx = 0
 for f in files:
  file = f
  currIdx = file.split("movesAndPositions")[-1].split(".npy")[0]
  highestIdx = max(highestIdx, int(currIdx))

 return int(highestIdx)+1

def saveData(moves, positions):
 moves = np.array(moves).reshape(-1, 1)
 positions = np.array(positions).reshape(-1,1)
 movesAndPositions = np.concatenate((moves, positions), axis = 1)
 nextIdx = findNextIdx()
 np.save(f"data/movesAndPositions{nextIdx}.npy", movesAndPositions)
 print("Sauvegardé avec succès")

def runGame(numMoves, filename = "movesAndPositions1.npy"):
 """exécute une partie que vous avez stockée"""
 testing = np.load(f"data/{filename}")
 moves = testing[:, 0]
 if (numMoves > len(moves)):
  print("Vous devez entrer un nombre de coups inférieur à la longueur maximale de la partie. La longueur de la partie ici est : ", len(moves))
  return

 testBoard = chess.Board()

 for i in range(numMoves):
  move = moves[i]
  testBoard.push_san(move)
 return testBoard
```

N'oubliez pas de changer le chemin du fichier dans la fonction `findNextIdx`, car celui-ci est personnel pour votre ordinateur.

Créez un dossier de données dans le dossier où vous codez, et copiez le chemin (mais gardez toujours le `*.npy` à la fin)

La fonction `checkEndCondition` utilise les fonctions du [package pip Chess](https://pypi.org/project/chess/) pour vérifier si la partie doit être terminée.

La fonction `saveData` sauvegarde une partie dans des fichiers npy qui est une méthode hautement optimisée pour stocker des tableaux.

La fonction utilise la fonction `findNextIdx` pour sauvegarder dans un nouveau fichier (n'oubliez pas de créer un nouveau dossier appelé data pour stocker toutes les données).

Enfin, la fonction `runGame` permet d'exécuter une partie que vous avez sauvegardée pour vérifier les positions après un nombre de coups `numMoves`.

Vous pouvez enfin accéder à la fonction qui extrait les parties d'échecs :

```py
def mineGames(numGames : int):
 """extrait numGames parties de coups"""
 MAX_MOVES = 500 #ne pas continuer les parties après ce nombre

 for i in range(numGames):
  currentGameMoves = []
  currentGamePositions = []
  board = chess.Board()
  stockfish.set_position([])

  for i in range(MAX_MOVES):
   #choisir aléatoirement parmi ces 3 coups
   moves = stockfish.get_top_moves(3)
   #si moins de 3 coups disponibles, choisir le premier, si aucun disponible, sortir
   if (len(moves) == 0):
    print("la partie est terminée")
    break
   elif (len(moves) == 1):
    move = moves[0]["Move"]
   elif (len(moves) == 2):
    move = random.choices(moves, weights=(80, 20), k=1)[0]["Move"]
   else:
    move = random.choices(moves, weights=(80, 15, 5), k=1)[0]["Move"]

   currentGamePositions.append(stockfish.get_fen_position())
   board.push_san(move)
   currentGameMoves.append(move)
   stockfish.set_position(currentGameMoves)
   if (checkEndCondition(board)):
    print("la partie est terminée")
    break
  saveData(currentGameMoves, currentGamePositions)
```

Ici, vous définissez d'abord une limite maximale pour qu'une partie ne dure pas indéfiniment.

Ensuite, vous exécutez le nombre de parties que vous souhaitez et assurez-vous que Stockfish et le package Chess pip sont réinitialisés à la position de départ.

Ensuite, vous obtenez les 3 meilleurs coups suggérés par Stockfish et choisissez l'un d'eux à jouer (80 % de chance pour le meilleur coup, 15 % de chance pour le deuxième meilleur coup, 5 % de chance pour le troisième meilleur coup). La raison pour laquelle vous ne choisissez pas toujours le meilleur coup est pour que la sélection des coups soit plus stochastique.

Ensuite, vous choisissez un coup (en vous assurant qu'aucune erreur ne se produit même s'il y a moins de trois coups possibles), sauvegardez la position du plateau en utilisant [FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation#:~:text=Forsyth%E2%80%93Edwards%20Notation%20%28FEN%29,Scottish%20newspaper%20journalist%20David%20Forsyth.) (une manière d'encoder une position d'échecs), ainsi que le coup effectué à partir de cette position.

Si la partie est terminée, vous sortez de la boucle et stockez toutes les positions et les coups effectués à partir de ces positions. Si la partie n'est pas terminée, vous continuez à faire des coups jusqu'à ce que la partie soit terminée.

Vous pouvez ensuite extraire une partie avec :

```py
mineGames(1)

```

N'oubliez pas de créer un dossier de données ici, car c'est là que je stocke les parties !

### Comment examiner une partie extraite

Exécutez la fonction `mineGames` pour extraire une partie en utilisant la commande suivante :

```py
mineGames(1)

```

Vous pouvez accéder à cette partie avec une fonction d'assistance montrée précédemment en utilisant la commande suivante :

```py
testBoard = runGame(12, "movesAndPositions1.npy")
testBoard

```

En supposant qu'il y a eu 12 coups dans la partie, vous verrez alors quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_pjARgYsCMqZjj8lK.png)
_Sortie de l'impression de la position du plateau après 12 coups. (Notez que la dernière ligne avec juste testBoard est imprimée, puisque dans un notebook Jupyter, une variable est imprimée si elle est écrite seule en bas d'une cellule)._

Et c'est tout, vous pouvez maintenant extraire autant de parties que vous le souhaitez.

Cela va prendre un certain temps, et il y a des possibilités d'optimiser ce processus d'extraction, comme la parallélisation des simulations de parties (puisque chaque partie est complètement séparée des autres).

Pour le code complet de la partie 1, vous pouvez consulter le code complet sur [mon GitHub](https://github.com/EivindKjosbakken/ChessEngine/blob/main/part1RetrievingDataset.ipynb).

## Partie 2 : Comment encoder les données

Dans cette partie, vous allez encoder les coups et les positions d'échecs de la même manière que DeepMind l'a fait avec AlphaZero !

J'utiliserai les données que vous avez collectées dans la partie 1 de cette série.

Pour rappel, vous avez installé Stockfish et vous avez assuré de pouvoir y accéder sur l'ordinateur. Vous l'avez ensuite fait jouer contre lui-même, tout en stockant tous les coups et positions.

Vous avez maintenant un problème d'apprentissage supervisé, puisque l'entrée est la position actuelle, et l'étiquette (le coup correct à partir des positions) est le coup que Stockfish a décidé être le meilleur.

### Comment installer et importer les packages

Tout d'abord, vous devez installer et importer tous les packages requis, dont certains sont peut-être déjà installés si vous avez suivi la partie 1 de cette série.

Toutes les importations sont ci-dessous – n'oubliez pas de n'entrer qu'une ligne à la fois lors de l'installation via `pip` :

```bash
pip install numpy
pip install gym-chess
pip install chess

```

De plus, vous devez apporter une petite modification à l'un des fichiers du package gym-chess puisque `np.int` était utilisé, ce qui est maintenant obsolète.

Dans le fichier avec le chemin relatif (à partir de l'environnement virtuel) `venv\Lib\site-packages\gym_chess\alphazero\board_encoding.py` où `venv` est le nom de mon environnement virtuel, vous devez rechercher "np.int" et les remplacer par "int".

Si vous ne le faites pas, vous verrez un message d'erreur indiquant que np.int est obsolète.

J'ai également dû redémarrer VS Code après avoir remplacé "np.int" par "int", pour que cela fonctionne.

Toutes les importations dont vous avez besoin sont ci-dessous :

```py
import numpy as np
import gym
import chess
import os
import gym.spaces
from gym_chess.alphazero.move_encoding import utils, queenmoves, knightmoves, underpromotions
from typing import List

```

Et vous devez également créer l'environnement gym pour encoder et décoder les coups :

```py
env = gym.make('ChessAlphaZero-v0')

```

### Comment encoder les positions et les coups du plateau

L'encodage est un élément important dans l'IA, car il nous permet de représenter les problèmes de manière lisible pour l'IA.

Au lieu d'une image d'un plateau d'échecs, ou d'une chaîne représentant un coup d'échecs comme "d2d4", vous représentez cela en utilisant des tableaux (listes de nombres).

Découvrir comment faire cela manuellement est assez difficile, mais heureusement pour nous, le [package Python gym-chess](https://pypi.org/project/gym-chess/) a déjà résolu ce problème pour nous.

Je ne vais pas entrer dans plus de détails sur la manière dont ils l'ont encodé, mais vous pouvez voir en utilisant le code ci-dessous qu'une position est représentée avec un tableau de forme (8,8,119), et tous les coups possibles sont donnés avec un tableau (4672) (1 colonne avec 4672 valeurs).

Si vous voulez en savoir plus à ce sujet, vous pouvez consulter l'article [AlphaZero](https://arxiv.org/abs/1712.01815v1), bien que ce soit un article assez compliqué à comprendre pleinement.

```py
#code pour imprimer l'action et l'espace d'état
env = gym.make('ChessAlphaZero-v0')
env.reset()
print(env.observation_space)
print(env.action_space)

```

Ce qui donne :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_yDTpZm519oQl-fJm.png)
_Sortie de l'impression de l'état (première ligne) et de l'espace d'action (deuxième ligne)_

Vous pouvez également vérifier l'encodage d'un coup. De la notation en chaîne à la notation encodée. Assurez-vous de réinitialiser l'environnement car cela peut donner une erreur si vous ne le faites pas :

```py
#d'abord définir l'environnement et s'assurer de réinitialiser les positions
env = gym.make('ChessAlphaZero-v0')
env.reset()

#encoder le coup e2 à e4
move = chess.Move.from_uci('e2e4')
print(env.encode(move))
# -> sortie : 877

#décoder le coup encodé 877
print(env.decode(877))
# -> sortie : Move.from_uci('e2e4')

```

Avec cela, vous pouvez maintenant avoir des fonctions pour encoder les coups et les positions que vous avez stockés dans la partie 1 où vous avez généré un ensemble de données.

### Comment créer des fonctions pour encoder les coups

Ces fonctions sont copiées du [package Gym-Chess](https://pypi.org/project/gym-chess/), mais avec de petites modifications pour qu'elles ne dépendent pas d'une classe.

J'ai manuellement modifié ces fonctions pour qu'elles soient plus faciles à encoder. Je ne m'inquiéterais pas trop de comprendre pleinement ces fonctions, car elles sont assez compliquées.

Sachez simplement qu'elles sont un moyen de s'assurer que les coups que les humains comprennent sont convertis en une forme que les ordinateurs peuvent comprendre.

```py
#correction des fonctions d'encodage d'openai

def encodeKnight(move: chess.Move):
    _NUM_TYPES: int = 8

    #: Point de départ des coups de cavalier dans la dernière dimension du tableau d'action 8 x 8 x 73.
    _TYPE_OFFSET: int = 56

    #: Ensemble des directions possibles pour un coup de cavalier, encodées comme
    #: (delta rang, delta case).
    _DIRECTIONS = utils.IndexedTuple(
        (+2, +1),
        (+1, +2),
        (-1, +2),
        (-2, +1),
        (-2, -1),
        (-1, -2),
        (+1, -2),
        (+2, -1),
    )

    from_rank, from_file, to_rank, to_file = utils.unpack(move)

    delta = (to_rank - from_rank, to_file - from_file)
    is_knight_move = delta in _DIRECTIONS
    
    if not is_knight_move:
        return None

    knight_move_type = _DIRECTIONS.index(delta)
    move_type = _TYPE_OFFSET + knight_move_type

    action = np.ravel_multi_index(
        multi_index=((from_rank, from_file, move_type)),
        dims=(8, 8, 73)
    )

    return action

def encodeQueen(move: chess.Move):
    _NUM_TYPES: int = 56 # = 8 directions * 7 cases max. distance
    _DIRECTIONS = utils.IndexedTuple(
        (+1,  0),
        (+1, +1),
        ( 0, +1),
        (-1, +1),
        (-1,  0),
        (-1, -1),
        ( 0, -1),
        (+1, -1),
    )

    from_rank, from_file, to_rank, to_file = utils.unpack(move)

    delta = (to_rank - from_rank, to_file - from_file)

    is_horizontal = delta[0] == 0
    is_vertical = delta[1] == 0
    is_diagonal = abs(delta[0]) == abs(delta[1])
    is_queen_move_promotion = move.promotion in (chess.QUEEN, None)

    is_queen_move = (
        (is_horizontal or is_vertical or is_diagonal) 
            and is_queen_move_promotion
    )

    if not is_queen_move:
        return None

    direction = tuple(np.sign(delta))
    distance = np.max(np.abs(delta))

    direction_idx = _DIRECTIONS.index(direction)
    distance_idx = distance - 1

    move_type = np.ravel_multi_index(
        multi_index=([direction_idx, distance_idx]),
        dims=(8,7)
    )

    action = np.ravel_multi_index(
        multi_index=((from_rank, from_file, move_type)),
        dims=(8, 8, 73)
    )

    return action

def encodeUnder(move):
    _NUM_TYPES: int = 9 # = 3 directions * 3 types de pièces (voir ci-dessous)
    _TYPE_OFFSET: int = 64
    _DIRECTIONS = utils.IndexedTuple(
        -1,
        0,
        +1,
    )
    _PROMOTIONS = utils.IndexedTuple(
        chess.KNIGHT,
        chess.BISHOP,
        chess.ROOK,
    )

    from_rank, from_file, to_rank, to_file = utils.unpack(move)

    is_underpromotion = (
        move.promotion in _PROMOTIONS 
        and from_rank == 6 
        and to_rank == 7
    )

    if not is_underpromotion:
        return None

    delta_file = to_file - from_file

    direction_idx = _DIRECTIONS.index(delta_file)
    promotion_idx = _PROMOTIONS.index(move.promotion)

    underpromotion_type = np.ravel_multi_index(
        multi_index=([direction_idx, promotion_idx]),
        dims=(3,3)
    )

    move_type = _TYPE_OFFSET + underpromotion_type

    action = np.ravel_multi_index(
        multi_index=((from_rank, from_file, move_type)),
        dims=(8, 8, 73)
    )

    return action

def encodeMove(move: str, board) -> int:
    move = chess.Move.from_uci(move)
    if board.turn == chess.BLACK:
        move = utils.rotate(move)

    action = encodeQueen(move)

    if action is None:
        action = encodeKnight(move)

    if action is None:
        action = encodeUnder(move)

    if action is None:
        raise ValueError(f"{move} n'est pas un coup valide")

    return action

```

Ainsi, vous pouvez maintenant donner un coup sous forme de chaîne (par exemple : "e2e4" pour le coup de e2 à e4), et il produit un nombre (la version encodée du coup).

### Comment créer une fonction pour encoder les positions

L'encodage des positions est un peu plus difficile. J'ai pris une fonction du package gym-chess ("encodeBoard") car j'ai eu quelques problèmes à utiliser directement le package. La fonction que j'ai copiée est ci-dessous :

```py
def encodeBoard(board: chess.Board) -> np.array:
 """Convertit un plateau en représentation de tableau numpy."""

 array = np.zeros((8, 8, 14), dtype=int)

 for square, piece in board.piece_map().items():
  rank, file = chess.square_rank(square), chess.square_file(square)
  piece_type, color = piece.piece_type, piece.color
 
  # Les six premiers plans encodent les pièces du joueur actif,
  # les six suivants celles de l'adversaire du joueur actif. Puisque
  # cette classe stocke toujours les plateaux orientés vers le joueur blanc,
  # Blanc est considéré comme le joueur actif ici.
  offset = 0 if color == chess.WHITE else 6
  
  # Chess énumère les types de pièces en commençant par un, ce que vous devez
  # prendre en compte
  idx = piece_type - 1
 
  array[rank, file, idx + offset] = 1

 # Compteurs de répétition
 array[:, :, 12] = board.is_repetition(2)
 array[:, :, 13] = board.is_repetition(3)

 return array

def encodeBoardFromFen(fen: str) -> np.array:
 board = chess.Board(fen)
 return encodeBoard(board)
```

J'ai également ajouté la fonction `encodeBoardFromFen`, car la fonction copiée nécessitait un plateau d'échecs représenté en utilisant le [package Python Chess](https://python-chess.readthedocs.io/en/latest/), donc je convertis d'abord à partir de la [notation FEN](https://en.wikipedia.org/wiki/Forsyth%E2%80%93Edwards_Notation) (une manière d'encoder les positions d'échecs en une chaîne – vous ne pouvez pas utiliser cela car vous avez besoin que l'encodage soit en nombres) en un plateau d'échecs donné dans ce package.

Vous avez maintenant tout ce dont vous avez besoin pour encoder tous vos fichiers.

### Comment automatiser l'encodage pour tous les fichiers de données brutes

Maintenant que vous pouvez encoder les coups et les positions, vous allez automatiser ce processus pour tous les fichiers dans votre dossier que vous avez générés à partir de la partie 1 de cette série. Cela implique de trouver tous les fichiers dans lesquels vous devez encoder les données et de sauvegarder ceux-ci dans de nouveaux fichiers.

Notez que j'ai légèrement modifié la structure des dossiers depuis la partie 1.

J'ai maintenant un dossier parent `Data`, et dans ce dossier, j'ai le `rawData`, qui contient les coups au format chaîne et les positions au format FEN (de la partie 1).

J'ai également le dossier `preparedData` sous le dossier de données, où les coups et les positions encodés seront stockés.

Notez que les coups et les positions encodés seront stockés dans des fichiers séparés puisque les encodages ont des dimensions différentes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_oiZbBdWwveJNMCPe.png)
_Structure des dossiers pour les données. Assurez-vous d'avoir deux dossiers appelés preparedData et rawData dans le dossier Data. Le dossier Data est au même niveau que vos fichiers de notebook._

```py
#fonction pour encoder tous les coups et positions du dossier rawData
def encodeAllMovesAndPositions():
    board = chess.Board() #ceci est utilisé pour changer le tour afin que l'encodage fonctionne
    board.turn = False #définir le tour à noir d'abord, changé au premier passage

    #trouver tous les fichiers dans le dossier:
    files = os.listdir('data/rawData')
    for idx, f in enumerate(files):
        movesAndPositions = np.load(f'data/rawData/{f}', allow_pickle=True)
        moves = movesAndPositions[:,0]
        positions = movesAndPositions[:,1]
        encodedMoves = []
        encodedPositions = []

        for i in range(len(moves)):
            board.turn = (not board.turn) #échanger les tours
            try:
                encodedMoves.append(encodeMove(moves[i], board)) 
                encodedPositions.append(encodeBoardFromFen(positions[i]))
            except:
                try:
                    board.turn = (not board.turn) #changer de tour, puisque vous sautez parfois des coups, vous pourriez avoir besoin de changer de tour
                    encodedMoves.append(encodeMove(moves[i], board)) 
                    encodedPositions.append(encodeBoardFromFen(positions[i]))
                except:
                    print(f'erreur dans le fichier : {f}')
                    print("Tour : ", board.turn)
                    print(moves[i])
                    print(positions[i])
                    print(i)
                    break
            
        np.save(f'data/preparedData/moves{idx}', np.array(encodedMoves))
        np.save(f'data/preparedData/positions{idx}', np.array(encodedPositions))
    
encodeAllMovesAndPositions()

#NOTE: forme des fichiers:
#moves: (nombre de coups dans la partie)
#positions: (nombre de coups dans la partie, 8, 8, 14) (nombre de coups dans la partie inclut les coups des noirs et des blancs)

```

Je commence par créer l'environnement et le réinitialiser.

Ensuite, j'ouvre tous les fichiers de données brutes créés à partir de la partie 1 et les encode. Je le fais également dans une instruction `try/catch`, car je vois parfois des erreurs avec les encodages de coups.

La première instruction except est pour le cas où un coup est sauté (donc le programme pense qu'il est au mauvais tour). Si cela se produit, l'encodage ne fonctionnera pas, donc l'instruction except change le tour et réessaie. Ce n'est pas le code le plus optimal, mais l'encodage est une partie mineure du temps d'exécution total pour créer un moteur d'échecs IA, et il est donc acceptable.

Assurez-vous d'avoir la structure de dossier correcte et d'avoir créé tous les différents dossiers. Sinon, vous recevrez une erreur.

Vous avez maintenant encodé votre plateau d'échecs et vos coups. Si vous le souhaitez, vous pouvez consulter le code complet de cette partie sur [mon GitHub](https://github.com/EivindKjosbakken/ChessEngine/blob/main/part2Encoding.ipynb).

## Partie 3 : Comment entraîner le modèle IA

Ceci est la troisième et dernière partie de la création de votre propre moteur d'échecs IA !

Dans la partie 1, vous avez appris à créer un ensemble de données, et dans la partie 2, vous avez examiné l'encodage de l'ensemble de données afin qu'il puisse être utilisé pour une IA.

Vous allez maintenant utiliser cet ensemble de données encodé pour entraîner votre propre IA en utilisant PyTorch !

### Comment importer les packages

Comme toujours, vous avez toutes les importations qui seront utilisées dans le tutoriel. La plupart sont simples, mais vous devez installer PyTorch, que je recommande d'installer en utilisant [ce site web](https://pytorch.org/).

Ici, vous pouvez faire défiler un peu vers le bas, où vous voyez quelques options pour le build et le système d'exploitation que vous utilisez.

Après avoir sélectionné les options qui vous concernent, vous obtiendrez un code que vous pouvez coller dans le terminal pour installer PyTorch.

Vous pouvez voir les options que j'ai choisies dans l'image ci-dessous, mais en général, je recommande d'utiliser le build stable et de choisir votre propre système d'exploitation.

Ensuite, sélectionnez le package auquel vous êtes le plus habitué (Conda ou `pip` est probablement le plus facile car vous pouvez simplement le coller dans le terminal).

Sélectionnez CUDA 11.7/11.8 (peu importe lequel), et installez en utilisant la commande donnée en bas.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_UJVBkAt40X6-FXuV.png)
_Mes sélections lors de l'installation de PyTorch._

Vous pouvez ensuite importer tous vos packages avec le code ci-dessous :

```py
import numpy as np
import torch
import torch.nn as nn
import torch.functional as F
import torchvision
import torchvision.transforms as transforms
from torch.utils.tensorboard import SummaryWriter
from datetime import datetime
import gym
import gym_chess
import os
import chess
from tqdm import tqdm
from gym_chess.alphazero.move_encoding import utils
from pathlib import Path
from typing import Optional

```

### Comment installer CUDA

Ceci est une étape optionnelle, qui vous permet d'utiliser votre GPU pour entraîner votre modèle beaucoup plus rapidement. Ce n'est pas obligatoire, mais cela vous fera gagner du temps lors de l'entraînement de votre IA.

La manière dont vous installez CUDA varie en fonction de votre système d'exploitation, mais j'utilise Windows et j'ai suivi [ce tutoriel](https://docs.nvidia.com/cuda/cuda-installation-guide-microsoft-windows/index.html).

Si vous êtes sur MacOS ou Linux, vous pouvez trouver un tutoriel en recherchant sur Google : "installer CUDA Mac/Linux".

Pour vérifier si vous avez CUDA disponible (votre GPU est disponible), vous pouvez utiliser ce code :

```py
#vérifier si cuda est disponible
torch.cuda.is_available()

```

Ce qui renvoie `True` si votre GPU est disponible. Si vous n'avez pas de GPU disponible, ne vous inquiétez pas, le seul inconvénient ici est que l'entraînement du modèle prend plus de temps, ce qui n'est pas si grave lorsque vous faites des projets de loisir comme celui-ci.

### Comment créer des méthodes d'encodage

J'ai ensuite défini quelques méthodes d'assistance pour l'encodage et le décodage à partir du [package Python Gym-Chess](https://pypi.org/project/gym-chess/).

J'ai dû apporter quelques modifications au package pour qu'il fonctionne. La plupart du code est copié du package, avec quelques petites modifications rendant le code indépendant d'une classe et ainsi de suite.

Notez que vous n'avez pas besoin de comprendre tout le code ci-dessous, car la manière dont Deepmind encode tous les coups aux échecs est compliquée.

```py
#méthodes d'assistance :

#décodage des coups de idx à la notation uci
def _decodeKnight(action: int) -> Optional[chess.Move]:
    _NUM_TYPES: int = 8

    #: Point de départ des coups de cavalier dans la dernière dimension du tableau d'action 8 x 8 x 73.
    _TYPE_OFFSET: int = 56

    #: Ensemble des directions possibles pour un coup de cavalier, encodées comme
    #: (delta rang, delta case).
    _DIRECTIONS = utils.IndexedTuple(
        (+2, +1),
        (+1, +2),
        (-1, +2),
        (-2, +1),
        (-2, -1),
        (-1, -2),
        (+1, -2),
        (+2, -1),
    )

    from_rank, from_file, move_type = np.unravel_index(action, (8, 8, 73))

    is_knight_move = (
        _TYPE_OFFSET <= move_type
        and move_type < _TYPE_OFFSET + _NUM_TYPES
    )

    if not is_knight_move:
        return None

    knight_move_type = move_type - _TYPE_OFFSET

    delta_rank, delta_file = _DIRECTIONS[knight_move_type]

    to_rank = from_rank + delta_rank
    to_file = from_file + delta_file

    move = utils.pack(from_rank, from_file, to_rank, to_file)
    return move

def _decodeQueen(action: int) -> Optional[chess.Move]:

    _NUM_TYPES: int = 56 # = 8 directions * 7 cases max. distance

    #: Ensemble des directions possibles pour un coup de dame, encodées comme
    #: (delta rang, delta case).
    _DIRECTIONS = utils.IndexedTuple(
        (+1,  0),
        (+1, +1),
        ( 0, +1),
        (-1, +1),
        (-1,  0),
        (-1, -1),
        ( 0, -1),
        (+1, -1),
    )
    from_rank, from_file, move_type = np.unravel_index(action, (8, 8, 73))
    
    is_queen_move = move_type < _NUM_TYPES

    if not is_queen_move:
        return None

    direction_idx, distance_idx = np.unravel_index(
        indices=move_type,
        shape=(8,7)
    )

    direction = _DIRECTIONS[direction_idx]
    distance = distance_idx + 1

    delta_rank = direction[0] * distance
    delta_file = direction[1] * distance

    to_rank = from_rank + delta_rank
    to_file = from_file + delta_file

    move = utils.pack(from_rank, from_file, to_rank, to_file)
    return move

def _decodeUnderPromotion(action):
    _NUM_TYPES: int = 9 # = 3 directions * 3 types de pièces (voir ci-dessous)

    #: Point de départ des sous-promotions dans la dernière dimension du tableau d'action
    #: 8 x 8 x 73.
    _TYPE_OFFSET: int = 64

    #: Ensemble des directions possibles pour une sous-promotion, encodées comme delta de fichier.
    _DIRECTIONS = utils.IndexedTuple(
        -1,
        0,
        +1,
    )

    #: Ensemble des types de pièces possibles pour une sous-promotion (promouvoir en dame
    #: est implicitement encodé par le coup de dame correspondant).
    _PROMOTIONS = utils.IndexedTuple(
        chess.KNIGHT,
        chess.BISHOP,
        chess.ROOK,
    )

    from_rank, from_file, move_type = np.unravel_index(action, (8, 8, 73))

    is_underpromotion = (
        _TYPE_OFFSET <= move_type
        and move_type < _TYPE_OFFSET + _NUM_TYPES
    )

    if not is_underpromotion:
        return None

    underpromotion_type = move_type - _TYPE_OFFSET

    direction_idx, promotion_idx = np.unravel_index(
        indices=underpromotion_type,
        shape=(3,3)
    )

    direction = _DIRECTIONS[direction_idx]
    promotion = _PROMOTIONS[promotion_idx]

    to_rank = from_rank + 1
    to_file = from_file + direction

    move = utils.pack(from_rank, from_file, to_rank, to_file)
    move.promotion = promotion

    return move

#fonction de décodage principale, celles ci-dessus sont juste des fonctions d'assistance
def decodeMove(action: int, board) -> chess.Move:
        move = _decodeQueen(action)
        is_queen_move = move is not None

        if not move:
            move = _decodeKnight(action)

        if not move:
            move = _decodeUnderPromotion(action)

        if not move:
            raise ValueError(f"{action} n'est pas une action valide")

        # Les actions encodent les coups du point de vue du joueur actuel. Si
        # c'est le joueur noir, le coup doit être réorienté.
        turn = board.turn
        
        if turn == False: #noir doit jouer
            move = utils.rotate(move)

        # Déplacer un pion vers la rangée de départ de l'adversaire avec un coup de dame
        # est automatiquement supposé être une sous-promotion en dame. Cependant,
        # puisque queenmoves n'a pas de référence au plateau et ne peut donc pas
        # déterminer si la pièce déplacée est un pion, vous devez ajouter cette
        # information manuellement ici
        if is_queen_move:
            to_rank = chess.square_rank(move.to_square)
            is_promoting_move = (
                (to_rank == 7 and turn == True) or 
                (to_rank == 0 and turn == False)
            )

            piece = board.piece_at(move.from_square)
            if piece is None: #NOTE J'ai ajouté ceci, pas entièrement sûr si c'est correct
                return None
            is_pawn = piece.piece_type == chess.PAWN

            if is_pawn and is_promoting_move:
                move.promotion = chess.QUEEN

        return move

def encodeBoard(board: chess.Board) -> np.array:
 """Convertit un plateau en représentation de tableau numpy."""

 array = np.zeros((8, 8, 14), dtype=int)

 for square, piece in board.piece_map().items():
  rank, file = chess.square_rank(square), chess.square_file(square)
  piece_type, color = piece.piece_type, piece.color
 
  # Les six premiers plans encodent les pièces du joueur actif,
  # les six suivants celles de l'adversaire du joueur actif. Puisque
  # cette classe stocke toujours les plateaux orientés vers le joueur blanc,
  # Blanc est considéré comme le joueur actif ici.
  offset = 0 if color == chess.WHITE else 6
  
  # Chess énumère les types de pièces en commençant par un, ce que vous devez
  # prendre en compte
  idx = piece_type - 1
 
  array[rank, file, idx + offset] = 1

 # Compteurs de répétition
 array[:, :, 12] = board.is_repetition(2)
 array[:, :, 13] = board.is_repetition(3)

 return array
 
```

### Comment charger les données

Dans la partie 1, vous avez extrait quelques parties d'échecs, puis dans la partie 2, vous les avez encodées afin qu'elles puissent être utilisées pour entraîner un modèle.

Vous chargez maintenant ces données dans des objets chargeurs de données PyTorch, afin qu'elles soient disponibles pour que le modèle s'entraîne. Au cas où vous n'auriez pas fait la partie 1 ou 2 de ce tutoriel, vous pouvez trouver quelques fichiers d'entraînement prêts à l'emploi dans [ce dossier Google Drive](https://drive.google.com/drive/folders/16QLJL2LQcz5hiONJnvuJwtUJqz6v-sN5?usp=sharing).

Tout d'abord, définissez quelques hyperparamètres :

```py
FRACTION_OF_DATA = 1
BATCH_SIZE = 4

```

La variable `FRACTION_OF_DATA` est là au cas où vous souhaitez entraîner le modèle rapidement et ne pas vouloir l'entraîner sur l'ensemble complet de données. Assurez-vous que cette valeur est > 0 et ≤ 1.

La variable `BATCH_SIZE` décide de la taille du lot sur lequel le modèle s'entraîne. En général, une taille de lot plus élevée signifie que le modèle peut s'entraîner plus rapidement, mais votre taille de lot est limitée par la puissance de votre GPU.

Je recommande de tester avec une petite taille de lot de 4, puis d'essayer de l'augmenter et de voir si l'entraînement fonctionne toujours comme il se doit. Si vous obtenez une erreur de mémoire de quelque sorte, essayez de diminuer à nouveau la taille du lot.

Vous chargez ensuite les données avec le code ci-dessous. Assurez-vous que votre structure de dossiers et le nom des fichiers sont corrects ici. Vous devriez avoir un dossier de données initial au même endroit où se trouve votre code.

Ensuite, à l'intérieur de ce dossier de données, vous devriez avoir un dossier `preparedData`, qui contient les fichiers sur lesquels vous souhaitez vous entraîner. Ces fichiers doivent être nommés `moves{i}.npy` et `positions{i}.npy`, où i est l'index du fichier. Si vous avez encodé les fichiers comme je l'ai fait précédemment, tout devrait être correct.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_3LT9odIm09DPFS59.png)
_La structure des dossiers. Jaune sont des dossiers, et turquoise sont des fichiers._

```py
#ensemble de données

#chargement des données d'entraînement

allMoves = []
allBoards = []

files = os.listdir('data/preparedData')
numOfEach = len(files) // 2 # moitié sont des coups, l'autre moitié sont des positions

for i in range(numOfEach):
    try:
        moves = np.load(f"data/preparedData/moves{i}.npy", allow_pickle=True)
        boards = np.load(f"data/preparedData/positions{i}.npy", allow_pickle=True)
        if (len(moves) != len(boards)):
            print("ERREUR SUR i = ", i, len(moves), len(boards))
        allMoves.extend(moves)
        allBoards.extend(boards)
    except:
        print("erreur : impossible de charger ", i, ", mais continue")

allMoves = np.array(allMoves)[:(int(len(allMoves) * FRACTION_OF_DATA))]
allBoards = np.array(allBoards)[:(int(len(allBoards) * FRACTION_OF_DATA))]
assert len(allMoves) == len(allBoards), "DOIT ÊTRE DE LA MÊME LONGUEUR"

#aplatir les plateaux
# allBoards = allBoards.reshape(allBoards.shape[0], -1)

trainDataIdx = int(len(allMoves) * 0.8)

#NOTE transférer toutes les données sur le GPU si disponible
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
allBoards = torch.from_numpy(np.asarray(allBoards)).to(device)
allMoves = torch.from_numpy(np.asarray(allMoves)).to(device)

training_set = torch.utils.data.TensorDataset(allBoards[:trainDataIdx], allMoves[:trainDataIdx])
test_set = torch.utils.data.TensorDataset(allBoards[trainDataIdx:], allMoves[trainDataIdx:])
# Créer des chargeurs de données pour vos ensembles de données ; mélanger pour l'entraînement, pas pour la validation

training_loader = torch.utils.data.DataLoader(training_set, batch_size=BATCH_SIZE, shuffle=True)
validation_loader = torch.utils.data.DataLoader(test_set, batch_size=BATCH_SIZE, shuffle=False)

```

### Comment définir le modèle de deep learning

Vous pouvez ensuite définir l'architecture du modèle :

```py
class Model(torch.nn.Module):

    def __init__(self):
        super(Model, self).__init__()
        self.INPUT_SIZE = 896 
        # self.INPUT_SIZE = 7*7*13 #NOTE changer la taille d'entrée pour utiliser les cnns
        self.OUTPUT_SIZE = 4672 # = nombre de coups uniques (espace d'action)
        
        #peut essayer d'ajouter CNN et pooling ici (calculs prenant en compte les caractéristiques spatiales)

        #forme d'entrée pour l'échantillon est (8,8,14), aplatie en tableau 1d de taille 896
        # self.cnn1 = nn.Conv3d(4,4,(2,2,4), padding=(0,0,1))
        self.activation = torch.nn.ReLU()
        self.linear1 = torch.nn.Linear(self.INPUT_SIZE, 1000)
        self.linear2 = torch.nn.Linear(1000, 1000)
        self.linear3 = torch.nn.Linear(1000, 1000)
        self.linear4 = torch.nn.Linear(1000, 200)
        self.linear5 = torch.nn.Linear(200, self.OUTPUT_SIZE)
        self.softmax = torch.nn.Softmax(1) #utiliser softmax comme prob pour chaque coup, dim 1 comme dim 0 est la dimension du lot
 
    def forward(self, x): #x.shape = (taille du lot, 896)
        x = x.to(torch.float32)
        # x = self.cnn1(x) #pour utiliser les cnns
        x = x.reshape(x.shape[0], -1)
        x = self.linear1(x)
        x = self.activation(x)
        x = self.linear2(x)
        x = self.activation(x)
        x = self.linear3(x)
        x = self.activation(x)
        x = self.linear4(x)
        x = self.activation(x)
        x = self.linear5(x)
        # x = self.softmax(x) #ne pas utiliser softmax puisque vous utilisez cross entropy loss
        return x

    def predict(self, board : chess.Board):
        """prend un plateau d'échecs et retourne un objet chess.move. NOTE : cette fonction devrait définitivement être mieux écrite, mais elle fonctionne pour l'instant"""
        with torch.no_grad():
            encodedBoard = encodeBoard(board)
            encodedBoard = encodedBoard.reshape(1, -1)
            encodedBoard = torch.from_numpy(encodedBoard)
            res = self.forward(encodedBoard)
            probs = self.softmax(res)

            probs = probs.numpy()[0] #ne veut plus de tenseur, 0 puisque c'est un tableau 2d avec 1 ligne

            #vérifier que le coup est légal et peut être décodé avant de retourner
            while len(probs) > 0: #essayer max 100 fois, sinon lever une erreur
                moveIdx = probs.argmax()
                try: #TODO ne devrait pas avoir try ici, mais il y avait un bug avec l'idx 499 si c'est aux noirs de jouer
                    uciMove = decodeMove(moveIdx, board)
                    if (uciMove is None): #n'a pas pu décoder
                        probs = np.delete(probs, moveIdx)
                        continue
                    move = chess.Move.from_uci(str(uciMove))
                    if (move in board.legal_moves): #si légal, retourner, sinon : la boucle continue après avoir supprimé le coup
                        return move 
                except:
                    pass
                probs = np.delete(probs, moveIdx) #TODO probablement une meilleure façon de faire cela, mais ce n'est pas trop critique en termes de temps car c'est seulement pour les prédictions
                                             #supprimer le coup pour qu'il ne soit pas choisi à nouveau à la prochaine itération
            
            #TODO peut retourner un coup aléatoire ici aussi !
            return None #si aucun coup légal trouvé, retourner None
```

Vous êtes libre de changer l'architecture comme vous le souhaitez.

Ici, j'ai simplement choisi quelques paramètres simples qui fonctionnent décemment, bien qu'il y ait de la place pour des améliorations. Voici quelques exemples de modifications que vous pouvez apporter :

1. Ajoutez des [modules CNN PyTorch](https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html) (n'oubliez pas de ne pas aplatir le tableau avant d'ajouter ceux-ci)
2. Changez les fonctions d'activation dans les couches cachées. J'utilise actuellement [ReLU](https://pytorch.org/docs/stable/generated/torch.nn.ReLU.html), mais cela pourrait être changé par exemple en Sigmoid ou Tanh, que vous pouvez lire plus en détail [ici](https://machinelearningmastery.com/choose-an-activation-function-for-deep-learning/).
3. Changez le nombre de couches cachées. Lorsque vous changez cela, vous devez vous souvenir d'ajouter une fonction d'activation entre chaque couche dans la fonction `forward()`.
4. Changez le nombre de neurones dans chaque couche cachée. Si vous allez changer le nombre de neurones, vous devez vous souvenir de la règle selon laquelle le nombre de neurones en sortie dans la couche n doit être le nombre de neurones en entrée dans la couche n+1. Par exemple, linear1 prend en entrée 1000 neurones et produit 2000 neurones. Ensuite, linear2 doit prendre en entrée 2000 neurones. Vous pouvez alors choisir librement le nombre de neurones de sortie sur linear2, mais la quantité doit correspondre au nombre de neurones d'entrée dans linear 3, et ainsi de suite. L'entrée de la couche 1 et la sortie de la dernière couche sont cependant définies avec les paramètres `INPUT_SIZE` et `OUTPUT_SIZE`.

En plus de l'architecture du modèle et des fonctions forward, qui sont obligatoires lors de la création d'un modèle profond, j'ai également défini une fonction `predict()`, pour faciliter la fourniture d'une position d'échecs au modèle, qui renvoie ensuite le coup qu'il recommande.

### Comment entraîner le modèle

Lorsque vous avez toutes les données requises et que le modèle est défini, vous pouvez commencer à entraîner le modèle. Tout d'abord, vous définissez une fonction pour entraîner une époque et sauvegarder le meilleur modèle :

```py
#fonctions d'assistance pour l'entraînement
def train_one_epoch(model, optimizer, loss_fn, epoch_index, tb_writer):
    running_loss = 0.
    last_loss = 0.

    # Ici, vous utilisez enumerate(training_loader) au lieu de
    # iter(training_loader) afin que vous puissiez suivre l'index du lot
    # et faire un rapport intra-époque
    for i, data in enumerate(training_loader):

        # Chaque instance de données est une paire entrée + étiquette
        inputs, labels = data

        # Mettez vos gradients à zéro pour chaque lot !
        optimizer.zero_grad()

        # Faites des prédictions pour ce lot
        outputs = model(inputs)

        # Calculez la perte et ses gradients
        loss = loss_fn(outputs, labels)
        loss.backward()

        # Ajustez les poids d'apprentissage
        optimizer.step()

        # Rassemblez les données et faites un rapport
        running_loss += loss.item()
        if i % 1000 == 999:
            last_loss = running_loss / 1000 # perte par lot
            # print('  lot {} perte: {}'.format(i + 1, last_loss))
            tb_x = epoch_index * len(training_loader) + i + 1
            tb_writer.add_scalar('Perte/entraînement', last_loss, tb_x)
            running_loss = 0.

    return last_loss

#les 3 fonctions ci-dessous aident à stocker le meilleur modèle que vous avez créé jusqu'à présent
def createBestModelFile():
    #d'abord trouver le meilleur modèle s'il existe :
    folderPath = Path('./savedModels')
    if (not folderPath.exists()):
        os.mkdir(folderPath)

    path = Path('./savedModels/bestModel.txt')

    if (not path.exists()):
        #créer les fichiers
        f = open(path, "w")
        f.write("10000000") #définir à un nombre élevé pour qu'il soit écrasé avec une meilleure perte
        f.write("\ntestPath")
        f.close()

def saveBestModel(vloss, pathToBestModel):
    f = open("./savedModels/bestModel.txt", "w")
    f.write(str(vloss.item()))
    f.write("\n")
    f.write(pathToBestModel)
    print("NOUVEL MEILLEUR MODÈLE TROUVÉ AVEC PERTE :", vloss)

def retrieveBestModelInfo():
    f = open('./savedModels/bestModel.txt', "r")
    bestLoss = float(f.readline())
    bestModelPath = f.readline()
    f.close()
    return bestLoss, bestModelPath

```

Notez que cette fonction est essentiellement copiée de la [documentation PyTorch](https://pytorch.org/tutorials/beginner/introyt/trainingyt.html), avec une légère modification en important le modèle, l'optimiseur et la fonction de perte en tant que paramètres de fonction.

Vous définissez ensuite les hyperparamètres comme ci-dessous. Notez que c'est quelque chose que vous pouvez ajuster pour améliorer davantage votre modèle.

```py
#hyperparamètres
EPOCHS = 60
LEARNING_RATE = 0.001
MOMENTUM = 0.9

```

Exécutez l'entraînement avec le code ci-dessous :

```py
#exécuter l'entraînement

createBestModelFile()

bestLoss, bestModelPath = retrieveBestModelInfo()

timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
writer = SummaryWriter('runs/fashion_trainer_{}'.format(timestamp))
epoch_number = 0

model = Model()
loss_fn = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.SGD(model.parameters(), lr=LEARNING_RATE, momentum=MOMENTUM)
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
model.to(device)

best_vloss = 1_000_000.

for epoch in tqdm(range(EPOCHS)):
    if (epoch_number % 5 == 0):
        print('ÉPOQUE {}:'.format(epoch_number + 1))

    # Assurez-vous que le suivi des gradients est activé, et faites un passage sur les données
    model.train(True)
    avg_loss = train_one_epoch(model, optimizer, loss_fn, epoch_number, writer)

    running_vloss = 0.0
    # Définissez le modèle en mode évaluation, désactivant le dropout et utilisant les statistiques de population
    # pour la normalisation par lot.

    model.eval()

    # Désactivez le calcul des gradients et réduisez la consommation de mémoire.
    with torch.no_grad():
        for i, vdata in enumerate(validation_loader):
            vinputs, vlabels = vdata
            voutputs = model(vinputs)

            vloss = loss_fn(voutputs, vlabels)
            running_vloss += vloss

    avg_vloss = running_vloss / (i + 1)

    #n'imprimer que toutes les 5 époques
    if epoch_number % 5 == 0:
        print('PERTE entraînement {} validation {}'.format(avg_loss, avg_vloss))

    # Journalisez la perte en cours moyennée par lot
    # pour l'entraînement et la validation
    writer.add_scalars('Perte d'entraînement vs. Perte de validation',
                    { 'Entraînement' : avg_loss, 'Validation' : avg_vloss },
                    epoch_number + 1)
    writer.flush()

    # Suivez les meilleures performances et sauvegardez l'état du modèle
    if avg_vloss < best_vloss:
        best_vloss = avg_vloss

        if (bestLoss > best_vloss): #si meilleure que la meilleure perte précédente de tous les modèles créés, sauvegardez-la
            model_path = 'savedModels/model_{}_{}'.format(timestamp, epoch_number)
            torch.save(model.state_dict(), model_path)
            saveBestModel(best_vloss, model_path)

    epoch_number += 1

print("\n\nMEILLEURE PERTE DE VALIDATION POUR TOUS LES MODÈLES : ", bestLoss)

```

Ce code est également fortement inspiré de la [documentation PyTorch](https://pytorch.org/tutorials/beginner/introyt/trainingyt.html).

Selon le nombre de couches dans votre modèle, le nombre de neurones dans les couches, le nombre d'époques, si vous utilisez un GPU ou non, et plusieurs autres facteurs, le temps nécessaire pour entraîner le modèle peut prendre de quelques secondes à plusieurs heures.

Comme vous pouvez le voir ci-dessous, le temps estimé pour entraîner mon modèle ici était d'environ 2 minutes.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_-JEKRkXNUxXy4CYh.gif)
_Vidéo de l'entraînement du modèle. Enregistrée en utilisant [LICEcap](https://www.cockos.com/licecap/" rel="noopener ugc nofollow noopener noopener)_

### Comment tester votre modèle

Tester votre modèle est une partie vitale pour vérifier si ce que vous avez créé fonctionne. J'ai implémenté deux façons de vérifier le modèle :

#### Vous contre l'IA

La première façon est de jouer contre l'IA. Ici, vous décidez d'un coup, puis vous laissez l'IA décider du coup, et ainsi de suite. Je recommande de faire cela dans un notebook, afin que vous puissiez exécuter différentes cellules pour différentes actions.

Tout d'abord, chargez un modèle qui a été sauvegardé à partir de l'entraînement. Ici, j'obtiens le chemin vers le fichier à partir du fichier créé lors de l'exécution de l'entraînement, qui stocke le chemin vers votre meilleur modèle. Vous pouvez bien sûr également changer manuellement le chemin vers le modèle que vous préférez utiliser.

```py
saved_model = Model()

#charger le chemin du meilleur modèle à partir de votre fichier
f = open("./savedModels/bestModel.txt", "r")
bestLoss = float(f.readline())
model_path = f.readline()
f.close()

model.load_state_dict(torch.load(model_path))

```

Ensuite, définissez le plateau d'échecs :

```py
#jouez votre propre partie
board = chess.Board()

```

Ensuite, vous pouvez faire un coup en exécutant le code dans la cellule ci-dessous en changeant la chaîne dans la première ligne. Assurez-vous qu'il s'agit d'un coup légal :

```py
moveStr = "e2e4"
move = chess.Move.from_uci(moveStr)
board.push(move)

```

Ensuite, vous pouvez laisser l'IA décider du coup suivant avec la cellule ci-dessous :

```py
#faire un coup d'IA :
aiMove = saved_model.predict(board)
board.push(aiMove)
board

```

Cela imprimera également l'état du plateau pour que vous puissiez décider de votre propre coup plus facilement :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_mkYWyk2zoU01fyEj.png)
_Imppression de l'état du plateau après que l'IA a fait un coup_

Continuez à faire un coup sur deux, laissez l'IA jouer un coup sur deux, et voyez qui gagne !

Si vous voulez annuler un coup, vous pouvez utiliser :

```py
#annuler un coup :
board.pop()

```

#### Stockfish contre votre IA

Vous pouvez également automatiser le processus de test, en définissant Stockfish à un ELO spécifique, et en laissant votre IA jouer contre lui :

Tout d'abord, chargez votre modèle (assurez-vous de changer le `model_path` vers votre propre modèle) :

```py
saved_model = Model()
model_path = "savedModels/model_20230702_150228_46" #TODO CHANGER CE CHEMIN
model.load_state_dict(torch.load(model_path))

```

Ensuite, importez Stockfish, et définissez-le à un ELO spécifique. N'oubliez pas de changer le chemin vers le moteur Stockfish vers votre propre chemin où vous avez le programme Stockfish) :

```py
# test elo contre stockfish
ELO_RATING = 500
from stockfish import Stockfish
#TODO CHANGER LE CHEMIN CI-DESSOUS
stockfish = Stockfish(path=r"C:\Users\eivin\Documents\ownProgrammingProjects18062023\ChessEngine\stockfish\stockfish\stockfish-windows-2022-x86-64-avx2")
stockfish.set_elo_rating(ELO_RATING)

```

Un classement ELO de 100 est assez mauvais, et quelque chose que votre moteur devrait espérons battre.

Ensuite, jouez la partie avec ce script, qui s'exécutera :

```py
board = chess.Board()
allMoves = [] #liste de chaînes pour sauvegarder les coups pour définir la position pour stockfish

MAX_NUMBER_OF_MOVES = 150
for i in range(MAX_NUMBER_OF_MOVES): #définir une limite pour la partie

 #d'abord mon coup d'IA
 try:
  move = saved_model.predict(board)
  board.push(move)
  allMoves.append(str(move)) #ajouter pour que stockfish puisse voir
 except:
  print("partie terminée. Vous avez perdu")
  break

 # #ensuite obtenir le coup de stockfish
 stockfish.set_position(allMoves)
 stockfishMove = stockfish.get_best_move_time(3)
 allMoves.append(stockfishMove)
 stockfishMove = chess.Move.from_uci(stockfishMove)
 board.push(stockfishMove)

stockfish.reset_engine_parameters() #réinitialiser le classement elo

board

```

Ce qui imprimera la position du plateau après la fin de la partie.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/0_TmLzgIp2R5_bNyy7.png)
_Position après que votre moteur d'échecs a perdu une partie contre Stockfish_

### Réflexion sur la performance du moteur d'échecs

J'ai essayé d'entraîner le modèle sur environ 100k positions et coups et j'ai découvert que la performance du modèle n'est toujours pas suffisante pour battre un bot d'échecs de bas niveau (500 ELO).

Il pourrait y avoir plusieurs raisons à cela. Les échecs sont un jeu hautement compliqué, qui nécessite probablement beaucoup plus de coups et de positions pour qu'un bot décent soit développé.

De plus, il y a plusieurs éléments du bot que vous pouvez potentiellement changer pour l'améliorer. L'architecture peut être améliorée, par exemple en ajoutant un CNN au début de la fonction forward, afin que le bot prenne en compte les informations spatiales.

Vous pouvez également changer le nombre de couches cachées dans les couches entièrement connectées, ou la quantité de neurones dans chaque couche.

Une manière sûre d'améliorer davantage le modèle est de lui fournir plus de données, car vous avez accès à une quantité infinie de données en utilisant le code d'extraction dans [cet article](https://medium.com/dev-genius/creating-an-ai-chess-engine-using-imitation-learning-part-1-generating-dataset-8033d9e7f7dc).

De plus, je pense que cela montre qu'un moteur d'échecs utilisant l'apprentissage par imitation nécessite soit beaucoup de données, soit que l'entraînement d'un moteur d'échecs uniquement par l'apprentissage par imitation n'est peut-être pas une idée optimale.

Néanmoins, l'apprentissage par imitation peut être utilisé comme partie d'un moteur d'échecs, par exemple, si vous implémentez également des méthodes de recherche traditionnelles et ajoutez l'apprentissage par imitation par-dessus.

## Conclusion

Félicitations ! Vous avez maintenant créé votre propre moteur d'échecs IA à partir de zéro, et j'espère que vous avez appris quelque chose en cours de route. Vous pouvez constamment améliorer ce moteur si vous souhaitez l'améliorer et vous assurer qu'il bat une compétition de plus en plus forte.

Si vous voulez le code complet, consultez [mon GitHub](https://github.com/EivindKjosbakken/ChessEngine/blob/main/part3Training.ipynb).

Ce tutoriel a été écrit à l'origine partie par partie sur mon Medium, vous pouvez consulter chaque partie ici :

* [Partie 1 : Générer l'ensemble de données](https://blog.devgenius.io/creating-an-ai-chess-engine-using-imitation-learning-part-1-generating-dataset-8033d9e7f7dc)
* [Partie 2 : Encodage avec la méthode AlphaZero](https://medium.com/dev-genius/creating-an-ai-chess-engine-part-2-encoding-using-the-alphazero-method-63c3c3c3a960)
* [Partie 3](https://python.plainenglish.io/learn-how-to-train-your-awesome-self-playing-ai-chess-engine-77a46633a949) : Entraîner le modèle

Si vous êtes intéressé et souhaitez en apprendre davantage sur des sujets similaires, vous pouvez me trouver sur :

* ✅ [Medium](https://medium.com/@oieivind)
* ✅ [Twitter](https://x.com/Ravenspike21)
* ✅ [LinkedIn](https://www.linkedin.com/in/eivind-kjosbakken/)