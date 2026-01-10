---
title: Projet Python – Comment créer un clone de Wordle en utilisant Python et Rich
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2022-04-04T20:21:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-wordle-clone-using-python-and-rich
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/wordle_ar8gck.png
tags:
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: Projet Python – Comment créer un clone de Wordle en utilisant Python et
  Rich
seo_desc: "Wordle is a popular game where you guess a five-letter word in six tries.\
  \ After each guess, the color of the tiles will change to show how close your guess\
  \ was to the word. \nIt is similar to the Hangman game which I've already shown\
  \ you how to build ..."
---

Wordle est un jeu populaire où vous devez deviner un mot de cinq lettres en six essais. Après chaque tentative, la couleur des tuiles change pour indiquer à quel point votre proposition était proche du mot.

Cela ressemble au [jeu du pendu](https://ireadblog.com/posts/124/hangman-game-using-python) dont je vous ai déjà montré comment le construire en utilisant Python.

Dans ce tutoriel, nous allons créer notre propre version terminal du jeu populaire Wordle en utilisant Python et Rich, une bibliothèque pour le formatage de texte enrichi.

Si vous êtes nouveau avec Rich, consultez [ce tutoriel](https://ireadblog.com/posts/108/getting-rich-with-python) pour commencer. Assurez-vous d'avoir installé Rich avant de commencer à suivre ce guide.

## Démonstration du projet

Voyons à quoi ressemblera notre jeu final :

[Contenu intégré](https://www.youtube.com/embed/-Mzsvg7IrME?rel=0)

## Codons notre jeu Wordle

Comme dans le vrai jeu Wordle, un mot de cinq lettres est choisi aléatoirement chaque jour. Pour cela, nous sélectionnerons un mot aléatoire dans une liste de mots de cinq lettres.

Donc, définissons d'abord la liste de mots appelée `word_list` dans un fichier séparé `words.py` :

```python
word_list = ['ABOUT', 'ABOVE', 'ABUSE', 'ACTOR', 'ACUTE', 'ADMIT', 'ADOPT', 'ADULT', 'AFTER', 'AGAIN', 'AGENT', 'AGREE', 'AHEAD', 'ALARM', 'ALBUM', 'ALERT', 'ALIKE', 'ALIVE', 'ALLOW', 'ALONE', 'ALONG', 'ALTER', 'AMONG', 'ANGER', 'ANGLE', 'ANGRY', 'APART', 'APPLE', 'APPLY', 'ARENA', 'ARGUE', 'ARISE', 'ARRAY', 'ASIDE', 'ASSET', 'AUDIO', 'AUDIT', 'AVOID', 'AWARD', 'AWARE', 'BADLY', 'BAKER', 'BASES', 'BASIC', 'BASIS', 'BEACH', 'BEGAN', 'BEGIN', 'BEGUN', 'BEING', 'BELOW', 'BENCH', 'BILLY', 'BIRTH', 'BLACK', 'BLAME', 'BLIND', 'BLOCK', 'BLOOD', 'BOARD', 'BOOST', 'BOOTH', 'BOUND', 'BRAIN', 'BRAND', 'BREAD', 'BREAK', 'BREED', 'BRIEF', 'BRING', 'BROAD', 'BROKE', 'BROWN', 'BUILD', 'BUILT', 'BUYER', 'CABLE', 'CALIF', 'CARRY', 'CATCH', 'CAUSE', 'CHAIN', 'CHAIR', 'CHART', 'CHASE', 'CHEAP', 'CHECK', 'CHEST', 'CHIEF', 'CHILD', 'CHINA', 'CHOSE', 'CIVIL', 'CLAIM', 'CLASS', 'CLEAN', 'CLEAR', 'CLICK', 'CLOCK', 'CLOSE', 'COACH', 'COAST', 'COULD', 'COUNT', 'COURT', 'COVER', 'CRAFT', 'CRASH', 'CREAM', 'CRIME', 'CROSS', 'CROWD', 'CROWN', 'CURVE', 'CYCLE', 'DAILY', 'DANCE', 'DATED', 'DEALT', 'DEATH', 'DEBUT', 'DELAY', 'DEPTH', 'DOING', 'DOUBT', 'DOZEN', 'DRAFT', 'DRAMA', 'DRAWN', 'DREAM', 'DRESS', 'DRILL', 'DRINK', 'DRIVE', 'DROVE', 'DYING', 'EAGER', 'EARLY', 'EARTH', 'EIGHT', 'ELITE', 'EMPTY', 'ENEMY', 'ENJOY', 'ENTER', 'ENTRY', 'EQUAL', 'ERROR', 'EVENT', 'EVERY', 'EXACT', 'EXIST', 'EXTRA', 'FAITH', 'FALSE', 'FAULT', 'FIBER', 'FIELD', 'FIFTH', 'FIFTY', 'FIGHT', 'FINAL', 'FIRST', 'FIXED', 'FLASH', 'FLEET', 'FLOOR', 'FLUID', 'FOCUS', 'FORCE', 'FORTH', 'FORTY', 'FORUM', 'FOUND', 'FRAME', 'FRANK', 'FRAUD', 'FRESH', 'FRONT', 'FRUIT', 'FULLY', 'FUNNY', 'GIANT', 'GIVEN', 'GLASS', 'GLOBE', 'GOING', 'GRACE', 'GRADE', 'GRAND', 'GRANT', 'GRASS', 'GREAT', 'GREEN', 'GROSS', 'GROUP', 'GROWN', 'GUARD', 'GUESS', 'GUEST', 'GUIDE', 'HAPPY', 'HARRY', 'HEART', 'HEAVY', 'HENCE', 'HENRY', 'HORSE', 'HOTEL', 'HOUSE', 'HUMAN', 'IDEAL', 'IMAGE', 'INDEX', 'INNER', 'INPUT', 'ISSUE', 'JAPAN', 'JIMMY', 'JOINT', 'JONES', 'JUDGE', 'KNOWN', 'LABEL', 'LARGE', 'LASER', 'LATER', 'LAUGH', 'LAYER', 'LEARN', 'LEASE', 'LEAST', 'LEAVE', 'LEGAL', 'LEVEL', 'LEWIS', 'LIGHT', 'LIMIT', 'LINKS', 'LIVES', 'LOCAL', 'LOGIC', 'LOOSE', 'LOWER', 'LUCKY', 'LUNCH', 'LYING', 'MAGIC', 'MAJOR', 'MAKER', 'MARCH', 'MARIA', 'MATCH', 'MAYBE', 'MAYOR', 'MEANT', 'MEDIA', 'METAL', 'MIGHT', 'MINOR', 'MINUS', 'MIXED', 'MODEL', 'MONEY', 'MONTH', 'MORAL', 'MOTOR', 'MOUNT', 'MOUSE', 'MOUTH', 'MOVIE', 'MUSIC', 'NEEDS', 'NEVER', 'NEWLY', 'NIGHT', 'NOISE', 'NORTH', 'NOTED', 'NOVEL', 'NURSE', 'OCCUR', 'OCEAN', 'OFFER', 'OFTEN', 'ORDER', 'OTHER', 'OUGHT', 'PAINT', 'PANEL', 'PAPER', 'PARTY', 'PEACE', 'PETER', 'PHASE', 'PHONE', 'PHOTO', 'PIECE', 'PILOT', 'PITCH', 'PLACE', 'PLAIN', 'PLANE', 'PLANT', 'PLATE', 'POINT', 'POUND', 'POWER', 'PRESS', 'PRICE', 'PRIDE', 'PRIME', 'PRINT', 'PRIOR', 'PRIZE', 'PROOF', 'PROUD', 'PROVE', 'QUEEN', 'QUICK', 'QUIET', 'QUITE', 'RADIO', 'RAISE', 'RANGE', 'RAPID', 'RATIO', 'REACH', 'READY', 'REFER', 'RIGHT', 'RIVAL', 'RIVER', 'ROBIN', 'ROGER', 'ROMAN', 'ROUGH', 'ROUND', 'ROUTE', 'ROYAL', 'RURAL', 'SCALE', 'SCENE', 'SCOPE', 'SCORE', 'SENSE', 'SERVE', 'SEVEN', 'SHALL', 'SHAPE', 'SHARE', 'SHARP', 'SHEET', 'SHELF', 'SHELL', 'SHIFT', 'SHIRT', 'SHOCK', 'SHOOT', 'SHORT', 'SHOWN', 'SIGHT', 'SINCE', 'SIXTH', 'SIXTY', 'SIZED', 'SKILL', 'SLEEP', 'SLIDE', 'SMALL', 'SMART', 'SMILE', 'SMITH', 'SMOKE', 'SOLID', 'SOLVE', 'SORRY', 'SOUND', 'SOUTH', 'SPACE', 'SPARE', 'SPEAK', 'SPEED', 'SPEND', 'SPENT', 'SPLIT', 'SPOKE', 'SPORT', 'STAFF', 'STAGE', 'STAKE', 'STAND', 'START', 'STATE', 'STEAM', 'STEEL', 'STICK', 'STILL', 'STOCK', 'STONE', 'STOOD', 'STORE', 'STORM', 'STORY', 'STRIP', 'STUCK', 'STUDY', 'STUFF', 'STYLE', 'SUGAR', 'SUITE', 'SUPER', 'SWEET', 'TABLE', 'TAKEN', 'TASTE', 'TAXES', 'TEACH', 'TEETH', 'TERRY', 'TEXAS', 'THANK', 'THEFT', 'THEIR', 'THEME', 'THERE', 'THESE', 'THICK', 'THING', 'THINK', 'THIRD', 'THOSE', 'THREE', 'THREW', 'THROW', 'TIGHT', 'TIMES', 'TIRED', 'TITLE', 'TODAY', 'TOPIC', 'TOTAL', 'TOUCH', 'TOUGH', 'TOWER', 'TRACK', 'TRADE', 'TRAIN', 'TREAT', 'TREND', 'TRIAL', 'TRIED', 'TRIES', 'TRUCK', 'TRULY', 'TRUST', 'TRUTH', 'TWICE', 'UNDER', 'UNDUE', 'UNION', 'UNITY', 'UNTIL', 'UPPER', 'UPSET', 'URBAN', 'USAGE', 'USUAL', 'VALID', 'VALUE', 'VIDEO', 'VIRUS', 'VISIT', 'VITAL', 'VOICE', 'WASTE', 'WATCH', 'WATER', 'WHEEL', 'WHERE', 'WHICH', 'WHILE', 'WHITE', 'WHOLE', 'WHOSE', 'WOMAN', 'WOMEN', 'WORLD', 'WORRY', 'WORSE', 'WORST', 'WORTH', 'WOULD', 'WOUND', 'WRITE', 'WRONG', 'WROTE', 'YIELD', 'YOUNG', 'YOUTH']

```

## Fonctions utilitaires

Nous allons définir quelques fonctions utilitaires pour nous aider à imprimer du texte coloré sur la console. Nous utiliserons des paramètres similaires à ceux par défaut de Wordle :

* Vert = lettre correcte à la bonne position
* Jaune = lettre correcte, mais à la mauvaise position
* Gris = lettre incorrecte

Pour cela, nous utiliserons Rich. Il est assez facile d'imprimer du texte coloré en utilisant ce code :

```python
from rich.console import Console
from random import choice
from words import word_list


WELCOME_MESSAGE = f'\n[white on blue] BIENVENUE DANS WORDLE [/]\n'
PLAYER_INSTRUCTIONS = "Vous pouvez commencer à deviner\n"
ALLOWED_GUESSES = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
```

Dans le code ci-dessus, nous avons défini trois fonctions pour imprimer du texte coloré en utilisant Rich. Nous avons également ajouté un message de bienvenue et des instructions pour le joueur, qui seront utilisés dans la fonction principale.

Le nombre de tentatives autorisées est fixé à 6. Dans la fonction principale, nous créons d'abord une instance de la classe `Console` de `rich.console`. Nous choisissons ensuite un mot aléatoire dans la `word_list` définie dans `words.py`.

Dans la dernière ligne, nous imprimons simplement le message de bienvenue et les instructions du joueur en utilisant `console.print`.

## Boucle de jeu

Nous allons exécuter une boucle while jusqu'à ce que toutes les tentatives aient été utilisées. Regardons le code puis expliquons-le.

```python
GUESS_STATEMENT = "\nEntrez votre proposition"

SQUARES = {
    'correct_place': '\ud83d\udfe9',
    'correct_letter': '\ud83d\udfe8',
    'incorrect_letter': '\u2b1b'
}

def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]Vous avez déjà proposé ce mot!!\n[/]")
            else:
                console.print('[red]Veuillez entrer un mot de 5 lettres!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Mot correct : {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")
```

La fonction `game()` accepte deux arguments – `console` et `chosen_word` (réponse correcte). Nous avons une variable booléenne `end_of_game` qui contrôle essentiellement la boucle while. La boucle while s'exécutera jusqu'à ce que `end_of_game` devienne True.

`already_guessed` est une liste qui contiendra les mots que l'utilisateur a déjà proposés. La liste `full_wordle_pattern` contiendra le motif Wordle (composé de carrés colorés). La liste `all_words_guessed` contiendra les mots avec leurs couleurs.

Ensuite, nous exécutons une boucle while jusqu'à `end_of_game` et demandons à l'utilisateur de deviner le mot. Nous vérifions également en continu si le mot proposé par l'utilisateur contient cinq lettres ou non, ainsi que si l'utilisateur a déjà proposé ce mot.

Dans l'un ou l'autre des cas, nous imprimons une erreur et demandons à l'utilisateur de deviner à nouveau.

Si l'utilisateur a proposé un mot, nous mettons le mot dans la liste `already_guessed`. Ensuite, nous utilisons une fonction appelée `check_guess()` pour vérifier si l'utilisateur a deviné le mot correctement ou non.

## Fonction `check_guess()`

Cette fonction accepte deux arguments – le mot proposé par l'utilisateur et la réponse correcte. Elle les compare lettre par lettre, puis utilise les fonctions d'assistance que nous avons définies précédemment pour créer la chaîne de formatage Rich pour chaque lettre. Ensuite, elle les joint toutes ensemble en une seule chaîne.

Cette fonction retourne deux chaînes – le mot proposé formaté avec Rich et les carrés colorés pour ce mot proposé.

Les chaînes retournées sont stockées dans deux variables, `guessed` et `pattern`, qui sont ensuite ajoutées à leurs listes respectives, `all_words_guessed` et `full_wordle_pattern`.

Dans chaque boucle, nous imprimons les éléments de la liste `all_words_guessed` séparés par un caractère de nouvelle ligne (`\n`). Si l'utilisateur a deviné le mot correctement ou si le nombre autorisé de tentatives a été épuisé, nous définissons `end_of_game` sur `True` et la boucle se termine.

En dehors de la boucle, nous vérifions si le nombre autorisé de tentatives a été épuisé et si l'utilisateur n'a pas pu deviner le mot correctement. Si c'est le cas, nous imprimons le mot correct et WORDLE X/6. Mais dans l'autre cas, nous imprimons WORDLE `n`/6 où n est le nombre de tentatives que l'utilisateur a prises pour deviner le mot correctement.

À la toute fin, nous imprimons la liste des motifs Wordle séparés par un caractère de nouvelle ligne (`\n`).

Dans la fonction principale, nous appelons la fonction `game()` avec `console` et `chosen_word` comme arguments.

## Code complet du projet

Voici le code complet pour le clone de Wordle :

```python
from rich.prompt import Prompt
from rich.console import Console
from random import choice
from words import word_list

SQUARES = {
    'correct_place': '\ud83d\udfe9',
    'correct_letter': '\ud83d\udfe8',
    'incorrect_letter': '\u2b1b'
}

WELCOME_MESSAGE = f'\n[white on blue] BIENVENUE DANS WORDLE [/]\n'
PLAYER_INSTRUCTIONS = "Vous pouvez commencer à deviner\n"
GUESS_STATEMENT = "\nEntrez votre proposition"
ALLOWED_GUESSES = 6

def correct_place(letter):
    return f'[black on green]{letter}[/]'


def correct_letter(letter):
    return f'[black on yellow]{letter}[/]'


def incorrect_letter(letter):
    return f'[black on white]{letter}[/]'


def check_guess(guess, answer):
    guessed = []
    wordle_pattern = []
    for i, letter in enumerate(guess):
        if answer[i] == guess[i]:
            guessed += correct_place(letter)
            wordle_pattern.append(SQUARES['correct_place'])
        elif letter in answer:
            guessed += correct_letter(letter)
            wordle_pattern.append(SQUARES['correct_letter'])
        else:
            guessed += incorrect_letter(letter)
            wordle_pattern.append(SQUARES['incorrect_letter'])
    return ''.join(guessed), ''.join(wordle_pattern)


def game(console, chosen_word):
    end_of_game = False
    already_guessed = []
    full_wordle_pattern = []
    all_words_guessed = []

    while not end_of_game:
        guess = Prompt.ask(GUESS_STATEMENT).upper()
        while len(guess) != 5 or guess in already_guessed:
            if guess in already_guessed:
                console.print("[red]Vous avez déjà proposé ce mot!!\n[/]")
            else:
                console.print('[red]Veuillez entrer un mot de 5 lettres!!\n[/]')
            guess = Prompt.ask(GUESS_STATEMENT).upper()
        already_guessed.append(guess)
        guessed, pattern = check_guess(guess, chosen_word)
        all_words_guessed.append(guessed)
        full_wordle_pattern.append(pattern)

        console.print(*all_words_guessed, sep="\n")
        if guess == chosen_word or len(already_guessed) == ALLOWED_GUESSES:
            end_of_game = True
    if len(already_guessed) == ALLOWED_GUESSES and guess != chosen_word:
        console.print(f"\n[red]WORDLE X/{ALLOWED_GUESSES}[/]")
        console.print(f'\n[green]Mot correct : {chosen_word}[/]')
    else:
        console.print(f"\n[green]WORDLE {len(already_guessed)}/{ALLOWED_GUESSES}[/]\n")
    console.print(*full_wordle_pattern, sep="\n")


if __name__ == '__main__':
    console = Console()
    chosen_word = choice(word_list)
    console.print(WELCOME_MESSAGE)
    console.print(PLAYER_INSTRUCTIONS)
    game(console, chosen_word)

```

## Conclusion

Dans cet article, nous avons créé notre propre version terminal de Wordle. Mais il y a encore beaucoup de choses que vous pouvez construire à partir de là. Similaire au vrai Wordle, vous pouvez créer une version web de ce projet.

Faites-moi savoir si vous avez des questions ! Partagez avec vos amis.

Dépôt de code : [https://github.com/ashutoshkrris/Terminal-Wordle](https://github.com/ashutoshkrris/Terminal-Wordle)

Vous pouvez lire cet article et mes autres articles [sur mon blog ici](https://ireadblog.com/posts/156/build-a-wordle-clone-using-python-and-rich).