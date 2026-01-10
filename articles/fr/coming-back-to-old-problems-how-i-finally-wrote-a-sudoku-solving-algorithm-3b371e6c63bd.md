---
title: Comment je suis revenu à un vieux problème et j'ai finalement écrit un algorithme
  de résolution de Sudoku
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-27T13:45:12.000Z'
originalURL: https://freecodecamp.org/news/coming-back-to-old-problems-how-i-finally-wrote-a-sudoku-solving-algorithm-3b371e6c63bd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ERYVo0W3nlPCEQGOHul6Rw.jpeg
tags:
- name: algorithms
  slug: algorithms
- name: Computer Science
  slug: computer-science
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: sudoku
  slug: sudoku
seo_title: Comment je suis revenu à un vieux problème et j'ai finalement écrit un
  algorithme de résolution de Sudoku
seo_desc: 'By Ali Spittel

  This article will be part technical, part personal story, and part cultural critique.
  If you are just here for the code and explanation, jump to the The Initial Approach
  header!

  This story starts a few years ago in a college computer s...'
---

Par Ali Spittel

Cet article sera à la fois technique, une histoire personnelle et une critique culturelle. Si vous êtes ici uniquement pour le code et l'explication, passez directement à l'en-tête **L'approche initiale** !

Cette histoire commence il y a quelques années dans une salle de classe d'informatique à l'université. J'ai eu un parcours peu traditionnel pour écrire du code — je me suis inscrit par hasard à un cours d'informatique pendant ma deuxième année d'université, parce que j'avais une heure de crédit supplémentaire et que j'étais curieux de savoir de quoi il s'agissait. Je pensais que nous allions apprendre à utiliser Microsoft Word et Excel — je n'avais vraiment aucune idée de ce qu'était le code.

Mon lycée n'avait définitivement aucun cours de codage, ils avaient à peine des ordinateurs fonctionnels ! Je ne jouais pas aux jeux vidéo ni ne participais à des activités qui mènent traditionnellement les enfants à apprendre à coder. Donc, le codage était totalement nouveau pour moi lorsque j'ai suivi ce cours de Python à l'université.

Dès que je suis entré dans la salle de classe, ils nous ont fait taper du code Python dans Idle, un éditeur de texte qui vient avec le langage Python. Ils avaient imprimé le code et nous ont simplement fait le taper et l'exécuter — j'ai été immédiatement accro. Au cours de ce cours, j'ai construit un script de Tic Tac Toe avec une interface graphique pour entrer les pièces et un clone de Flappy Bird. Cela m'est venu assez facilement, et je me suis beaucoup amusé. J'ai rapidement décidé de faire une mineure en informatique, et je voulais simplement écrire plus de code.

Le semestre suivant, je me suis inscrit à un cours de Structures de données et d'algorithmes, qui était le suivant dans la séquence d'informatique. Le cours était enseigné en C++, ce que, sans le savoir, j'étais censé apprendre pendant l'été avant le cours. Il est rapidement devenu évident que les professeurs essayaient d'utiliser le cours pour éliminer les étudiants — environ 50 % des inscrits le premier jour ont réussi le semestre. Nous avons même changé de salles de classe, passant d'un amphithéâtre à une salle de travail. Ma fierté était la seule chose qui me maintenait dans le cours. Je me sentais complètement perdu dans presque chaque leçon. J'ai passé de nombreuses nuits blanches à travailler sur des projets et à étudier pour les examens.

Un problème en particulier m'a vraiment marqué — nous devions construire un programme en C++ qui résoudrait n'importe quel problème de Sudoku. Encore une fois, j'ai passé d'innombrables heures sur l'assignment en essayant de faire fonctionner le code. Au moment où le projet était dû, ma solution fonctionnait pour certains des cas de test mais pas pour tous. J'ai fini par obtenir un C+ pour mon assignment — l'une de mes pires notes de tout le collège.

Après ce semestre, j'ai abandonné mon idée de faire une mineure en informatique, j'ai complètement arrêté de coder et je me suis concentré sur ce que je pensais être mes points forts — l'écriture et la politique.

Bien sûr, des choses amusantes arrivent dans la vie et j'ai évidemment recommencé à coder, mais il m'a fallu beaucoup de temps pour me sentir comme un programmeur compétent.

Tout cela étant dit, quelques années plus tard dans mon parcours de programmation, j'ai décidé de réessayer d'implémenter l'algorithme de résolution de Sudoku pour me prouver que je pouvais l'implémenter maintenant. Le code n'est pas parfait, mais il résoudra presque n'importe quelle énigme de Sudoku. Passons en revue l'algorithme puis l'implémentation.

### Énigmes de Sudoku

![Image](https://cdn-media-1.freecodecamp.org/images/NGyo6kOiNfPdOzeV5RfN8K4SUw0Jxw0LOraz)

Au cas où vous n'auriez jamais joué aux énigmes de Sudoku, ce sont des énigmes de nombres dans lesquelles chaque ligne, colonne et carré de 3x3 de l'énigme doit contenir les nombres 1–9 représentés exactement une fois. Il existe de nombreuses approches pour résoudre ces énigmes, dont beaucoup peuvent être reproduites par un ordinateur plutôt que par une personne. Habituellement, lorsque nous les résolvons à l'aide d'un ordinateur, nous utiliserons des tableaux imbriqués pour représenter le plateau de Sudoku comme suit :

```
puzzle = [[5, 3, 0, 0, 7, 0, 0, 0, 0],          [6, 0, 0, 1, 9, 5, 0, 0, 0],          [0, 9, 8, 0, 0, 0, 0, 6, 0],          [8, 0, 0, 0, 6, 0, 0, 0, 3],          [4, 0, 0, 8, 0, 3, 0, 0, 1],          [7, 0, 0, 0, 2, 0, 0, 0, 6],          [0, 6, 0, 0, 0, 0, 2, 8, 0],          [0, 0, 0, 4, 1, 9, 0, 0, 5],          [0, 0, 0, 0, 8, 0, 0, 7, 9]]
```

Une fois résolu, les zéros seront remplis avec des nombres réels :

```
solution = [[5, 3, 4, 6, 7, 8, 9, 1, 2],            [6, 7, 2, 1, 9, 5, 3, 4, 8],            [1, 9, 8, 3, 4, 2, 5, 6, 7],            [8, 5, 9, 7, 6, 1, 4, 2, 3],            [4, 2, 6, 8, 5, 3, 7, 9, 1],            [7, 1, 3, 9, 2, 4, 8, 5, 6],            [9, 6, 1, 5, 3, 7, 2, 8, 4],            [2, 8, 7, 4, 1, 9, 6, 3, 5],            [3, 4, 5, 2, 8, 6, 1, 7, 9]]
```

### L'approche initiale

Comme je n'avais pas envie d'écrire une suite de tests complète avec différents puzzles, j'ai utilisé les défis sur [CodeWars](https://www.codewars.com/) pour me tester. Le premier problème que j'ai essayé était [celui-ci](https://www.codewars.com/kata/sudoku-solver) — où tous les puzzles étaient des Sudokus « faciles » qui pouvaient être résolus sans un algorithme plus complexe.

J'ai décidé d'essayer de résoudre les Sudokus de la manière dont je le fais personnellement — où je trouverais les nombres possibles pour un espace, les garderais en mémoire, et si un seul nombre est possible, je le placerais à cet endroit. Comme ces Sudokus étaient plus faciles, cette approche a bien fonctionné pour ce Kata, et j'ai réussi.

Voici mon code (non nettoyé) !

```
class SudokuSolver:    def __init__(self, puzzle):        self.puzzle = puzzle        self.box_size = 3
```

```
    def find_possibilities(self, row_number, column_number):        possibilities = set(range(1, 10))        row = self.get_row(row_number)        column = self.get_column(column_number)        box = self.get_box(row_number, column_number)        for item in row + column + box:            if not isinstance(item, list)and item in possibilities:                possibilities.remove(item)        return possibilities
```

```
    def get_row(self, row_number):        return self.puzzle[row_number]
```

```
    def get_column(self, column_number):        return [row[column_number] for row in self.puzzle]
```

```
    def get_box(self, row_number, column_number):        start_y = column_number // 3 * 3        start_x = row_number // 3 * 3        if start_x < 0:            start_x = 0        if start_y < 0:            start_y = 0        box = []        for i in range(start_x, self.box_size + start_x):            box.extend(self.puzzle[i][start_y:start_y+self.box_size])        return box
```

```
    def find_spot(self):        unsolved = True        while unsolved:            unsolved = False            for row_number, row in enumerate(self.puzzle):                for column_number, item in enumerate(row):                    if item == 0:                        unsolved = True                        possibilities = self.find_possibilities(                            row_number, column_number)                        if len(possibilities) == 1:                            self.puzzle[row_number][column_number] = list(possibilities)[                                0]        return self.puzzle
```

```
def sudoku(puzzle):    sudoku = SudokuSolver(puzzle)    return sudoku.find_spot()
```

Bien sûr, je voulais aussi résoudre des puzzles de Sudoku plus difficiles, alors j'ai décidé d'implémenter un algorithme plus complexe afin de résoudre ces puzzles.

### L'algorithme

Un algorithme pour résoudre les puzzles de Sudoku est l'algorithme de retour en arrière. Essentiellement, vous continuez à essayer des nombres dans des cases vides jusqu'à ce qu'il n'y en ait plus de possibles, puis vous revenez en arrière et essayez différents nombres dans les cases précédentes.

![Image](https://cdn-media-1.freecodecamp.org/images/XHVFcJhCX-mRMxvSBvuWMQuEw1eipOCxKWBS)
_Merci à Wikipedia pour cette superbe visualisation !_

La première chose que j'ai faite a été de continuer l'approche de mon solveur de Sudoku « facile » en trouvant les valeurs possibles pour chaque case en fonction des valeurs déjà présentes dans la ligne, la colonne et la boîte de cette case. J'ai stocké toutes ces valeurs dans une liste afin de pouvoir m'y référer rapidement lors du retour en arrière ou pour trouver quelle valeur utiliser dans cette case.

Ensuite, j'ai dû implémenter l'avancement et le retour en arrière pour placer des éléments dans chaque espace. J'ai placé des marqueurs sur chaque espace non donné (ceux qui étaient des zéros au début du jeu) afin que ces espaces soient inclus dans le retour en arrière et que les espaces donnés ne le soient pas. J'ai ensuite itéré à travers ces espaces non résolus. J'ai placé le premier élément de la liste des valeurs possibles dans cet espace, puis je suis passé à l'espace non résolu suivant. J'ai ensuite placé la première valeur possible de cet espace à sa place. Si elle entrait en conflit avec la valeur de l'espace précédent, je passais alors au deuxième élément de la liste des valeurs possibles, puis je passais à l'espace suivant.

Ce processus se poursuivait jusqu'à ce qu'il n'y ait plus de mouvement possible pour un espace donné — c'est-à-dire que la fin de la liste des valeurs possibles était atteinte et qu'aucune des valeurs ne fonctionnait dans cette ligne, colonne ou boîte. Ensuite, l'algorithme de retour en arrière se déclenchait.

Dans l'implémentation du retour en arrière, le code revenait à la dernière case remplie et passait à la valeur possible suivante, puis recommençait à avancer. Si la dernière des valeurs possibles était atteinte à cet endroit également, l'algorithme de retour en arrière continuait à reculer jusqu'à ce qu'il y ait une case qui pouvait être incrémentée.

Une fois la fin du puzzle atteinte avec des valeurs correctes dans chaque case, le puzzle était résolu !

### Mon approche

J'aime les approches orientées objet, donc j'ai deux classes différentes dans ma solution : une pour la cellule et une pour le plateau de Sudoku. Mon code très imparfait ressemble à ceci :

```
class Cell:    """Une cellule individuelle sur le plateau de Sudoku"""
```

```
    def __init__(self, column_number, row_number, number, game):        # Si inclure la cellule dans le retour en arrière        self.solved = True if number > 0 else False        self.number = number  # la valeur actuelle de la cellule        # Les nombres que la cellule pourrait potentiellement être        self.possibilities = set(range(1, 10)) if not self.solved else []        self.row = row_number  # l'index de la ligne où se trouve la cellule        self.column = column_number  # l'index de la colonne où se trouve la cellule        self.current_index = 0  # l'index de la possibilité actuelle        self.game = game  # le jeu de sudoku auquel appartient la cellule        if not self.solved:  # exécute le vérificateur de possibilités            self.find_possibilities()
```

```
    def check_area(self, area):        """Vérifie si la valeur actuelle de la cellule est un mouvement valide de sudoku"""        values = [item for item in area if item != 0]        return len(values) == len(set(values))
```

```
    def set_number(self):        """modifie l'attribut number et change également la valeur de la cellule dans le puzzle plus grand"""        if not self.solved:            self.number = self.possibilities[self.current_index]            self.game.puzzle[self.row][self.column] = self.possibilities[self.current_index]
```

```
    def handle_one_possibility(self):        """Si la cellule n'a qu'une seule possibilité, définit la cellule à cette valeur et la marque comme résolue"""        if len(self.possibilities) == 1:            self.solved = True            self.set_number()
```

```
    def find_possibilities(self):        """filtre les valeurs possibles pour la cellule"""        for item in self.game.get_row(self.row) + self.game.get_column(self.column) + self.game.get_box(self.row, self.column):            if not isinstance(item, list) and item in self.possibilities:                self.possibilities.remove(item)        self.possibilities = list(self.possibilities)        self.handle_one_possibility()
```

```
    def is_valid(self):        """vérifie si le nombre actuel est valide dans sa ligne, colonne et boîte"""        for unit in [self.game.get_row(self.row), self.game.get_column(self.column), self.game.get_box(self.row, self.column)]:            if not self.check_area(unit):                return False        return True
```

```
    def increment_value(self):        """déplace le nombre vers la possibilité suivante tant que le nombre actuel est invalide et qu'il reste des possibilités"""        while not self.is_valid() and self.current_index < len(self.possibilities) - 1:            self.current_index += 1            self.set_number()
```

```
class SudokuSolver:    """contient la logique pour résoudre un puzzle de sudoku -- même les plus difficiles en utilisant un algorithme de retour en arrière"""
```

```
    def __init__(self, puzzle):        self.puzzle = puzzle  # la liste 2d des cases sur le plateau        self.solve_puzzle = []  # liste 1d des objets Cell        # la taille des boîtes dans le puzzle -- 3 pour un puzzle typique        self.box_size = int(len(self.puzzle) ** .5)        self.backtrack_coord = 0  # l'index actuel du retour en arrière
```

```
    def get_row(self, row_number):        """Obtient la ligne complète du puzzle en fonction de l'index de la ligne"""        return self.puzzle[row_number]
```

```
    def get_column(self, column_number):        """Obtient la colonne complète"""        return [row[column_number] for row in self.puzzle]
```

```
    def find_box_start(self, coordinate):        """Obtient la coordonnée de départ pour la petite boîte de sudoku"""        return coordinate // self.box_size * self.box_size
```

```
    def get_box_coordinates(self, row_number, column_number):        """Obtient les nombres de la petite boîte de sudoku"""        return self.find_box_start(column_number), self.find_box_start(row_number)
```

```
    def get_box(self, row_number, column_number):        """Obtient la petite boîte de sudoku pour une coordonnée x et y"""        start_y, start_x = self.get_box_coordinates(row_number, column_number)        box = []        for i in range(start_x, self.box_size + start_x):            box.extend(self.puzzle[i][start_y:start_y+self.box_size])        return box
```

```
    def initialize_board(self):        """crée les Cells pour chaque élément du puzzle et obtient ses possibilités"""        for row_number, row in enumerate(self.puzzle):            for column_number, item in enumerate(row):                self.solve_puzzle.append(                    Cell(column_number, row_number, item, self))
```

```
    def move_forward(self):        """Avance vers la cellule suivante"""        while self.backtrack_coord < len(self.solve_puzzle) - 1 and self.solve_puzzle[self.backtrack_coord].solved:            self.backtrack_coord += 1
```

```
    def backtrack(self):        """Recule vers la cellule précédente"""        self.backtrack_coord -= 1        while self.solve_puzzle[self.backtrack_coord].solved:            self.backtrack_coord -= 1
```

```
    def set_cell(self):        """Définir la cellule actuelle sur laquelle travailler"""        cell = self.solve_puzzle[self.backtrack_coord]        cell.set_number()        return cell
```

```
    def reset_cell(self, cell):        """réinitialise une cellule à zéro"""        cell.current_index = 0        cell.number = 0        self.puzzle[cell.row][cell.column] = 0
```

```
    def decrement_cell(self, cell):        """exécute l'algorithme de retour en arrière"""        while cell.current_index == len(cell.possibilities) - 1:            self.reset_cell(cell)            self.backtrack()            cell = self.solve_puzzle[self.backtrack_coord]        cell.current_index += 1
```

```
    def change_cells(self, cell):        """avance ou recule en fonction de la validité d'une cellule"""        if cell.is_valid():            self.backtrack_coord += 1        else:            self.decrement_cell(cell)
```

```
    def solve(self):        """exécute les autres fonctions nécessaires pour résoudre le puzzle de sudoku"""        self.move_forward()        cell = self.set_cell()        cell.increment_value()        self.change_cells(cell)
```

```
    def run_solve(self):        """exécute le solveur jusqu'à ce que nous soyons à la fin du puzzle"""        while self.backtrack_coord <= len(self.solve_puzzle) - 1:            self.solve()
```

```
def solve(puzzle):    solver = SudokuSolver(puzzle)    solver.initialize_board()    solver.run_solve()    return solver.puzzle
```

[Solveur de Sudoku difficile](https://www.codewars.com/kata/hard-sudoku-solver)

### Mes conclusions

Parfois, il suffit de temps et de pratique. Le solveur de Sudoku sur lequel j'ai passé d'innombrables heures à l'université m'a pris moins d'une heure quelques années plus tard.

Je dirai que les programmes d'informatique ne tendent pas à commencer de manière à permettre aux personnes qui n'ont pas écrit de code plus tôt dans leur vie de participer. Dans quelques années, les politiques d'éducation en informatique pourraient changer. Mais pour l'instant, cela élimine les personnes qui ont grandi dans de petites villes, qui n'étaient pas intéressées par le codage en grandissant, ou qui sont allées dans des lycées moins performants.

En partie, cela contribue définitivement au succès des bootcamps de codage qui commencent par les fondamentaux et enseignent les compétences de développement web moins conceptuelles plutôt que les algorithmes lourds.

Je peux maintenant écrire l'algorithme de résolution de Sudoku, mais je ne pense pas que ce soit une compétence nécessaire pour les développeurs — je suis devenu un ingénieur logiciel prospère peu de temps après cette période où je ne pouvais pas implémenter le solveur de Sudoku.

Je pense que certains fondamentaux de l'informatique peuvent être très utiles, même pour les nouveaux développeurs. Par exemple, les concepts derrière la notation Big-O peuvent être vraiment utiles pour décider entre différentes approches. Cela dit, la plupart des structures de données et des algorithmes ne sont pas utilisés au quotidien, alors pourquoi sont-ils la base des entretiens et des cours d'informatique au lieu des choses plus importantes utilisées chaque jour ?

Je suis heureux de voir ma propre croissance personnelle en matière de codage ; cependant, j'ai hâte du jour où les développeurs ne devront plus sauter à travers des cerceaux imaginaires pour se prouver, et où les environnements d'apprentissage seront beaucoup plus constructifs.

*Si vous avez aimé cet article, veuillez vous [abonner](https://tinyletter.com/ali_writes_code) à ma newsletter hebdomadaire où vous recevrez mes liens préférés de la semaine et mes derniers articles.*