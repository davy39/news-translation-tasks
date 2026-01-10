---
title: Comment créer une application de quiz GUI en utilisant Tkinter et Open Trivia
  DB
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-10T21:29:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-gui-quiz-application-using-tkinter-and-open-trivia-db
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/python-GUI-QUiz-application.png
tags:
- name: Python
  slug: python
- name: tkinter
  slug: tkinter
seo_title: Comment créer une application de quiz GUI en utilisant Tkinter et Open
  Trivia DB
seo_desc: "In this article, we'll learn to build a Graphical User Interface (GUI)\
  \ Quiz Application using the Tkinter Python built-in module. \nThe task is to ask\
  \ multiple-choice questions, collect user answers, and finally display the results.\
  \ \nBefore coding the..."
---

Dans cet article, nous allons apprendre à créer une application de quiz avec une **interface graphique** (GUI) en utilisant le module intégré de Python [Tkinter](https://docs.python.org/3/library/tkinter.html).

La tâche consiste à poser des questions à choix multiples, à collecter les réponses des utilisateurs et enfin à afficher les résultats.

Avant de coder l'interface graphique, nous verrons d'abord comment récupérer des questions à choix multiples, leurs réponses correctes et les choix possibles à partir de l'API [Open Trivia DB](https://opentdb.com/).

La **base de données Open Trivia** fournit une API JSON complètement gratuite que vous pouvez utiliser dans vos projets de programmation. L'utilisation de cette API **ne nécessite pas** de clé API. Pour rendre la tâche plus intéressante, nous allons également randomiser l'ordre des choix.

Regardez cette vidéo pour voir ce que nous allons construire :

%[https://www.youtube.com/watch?v=2hYci86bmjs]

Nous allons utiliser les modules et concepts suivants dans ce projet :

* [tkinter](https://docs.python.org/3/library/tkinter.html) est une bibliothèque GUI standard pour Python avec laquelle nous pouvons construire des applications de bureau. C'est la base de notre projet et nous l'utiliserons pour créer l'interface utilisateur de l'application.
* Le [module random](https://docs.python.org/3/library/random.html) implémente des générateurs de nombres pseudo-aléatoires pour diverses distributions. Ce module nous aidera à mélanger les options pour les questions.
* La [bibliothèque requests](https://pypi.org/project/requests/) nous permet d'envoyer des requêtes HTTP/1.1 extrêmement facilement. Nous aurons besoin de cette bibliothèque pour récupérer des questions de la base de données Open Trivia.
* Les [classes Python](https://docs.python.org/3/tutorial/classes.html) sont un plan pour créer des objets. Les objets sont des entités du monde réel. Pendant tout le développement du projet, nous séparerons nos différentes fonctionnalités en différentes classes et méthodes.

## Flux de travail du projet

Le flux de travail de base de l'application se déroulera comme suit :

1. Nous allons récupérer des questions de l'API Open Trivia DB.
2. Pour chaque question récupérée, nous allons créer un objet différent en utilisant une classe _Question_. Tous ces objets _Question_ seront ajoutés à une liste `question_bank`.
3. Cette liste `question_bank` sera passée au cerveau de l'application, _QuizBrain_, et un objet `quiz` sera créé. Cette classe sera responsable de vérifier s'il y a plus de questions, d'obtenir la question suivante, de calculer le score, etc.
4. Enfin, cet objet `quiz` sera passé à la classe _QuizInterface_, et l'utilisateur pourra interagir avec lui.

Très bien, commençons !

## Comment récupérer des questions de l'API Open Trivia DB

Comme nous l'avons discuté ci-dessus, nous allons utiliser l'API Open Trivia DB pour obtenir les questions. Rendez-vous sur [leur API](https://opentdb.com/api_config.php), sélectionnez le nombre de questions que vous souhaitez, ainsi que les catégories et la difficulté.

Le type de question doit être _Multiple Choice_ et l'encodage doit être _Default Encoding_. Cliquez sur Generate API URL et vous obtiendrez une URL d'API.

Voici un exemple d'URL d'API : `https://opentdb.com/api.php?amount=10&type=multiple`

Pour récupérer les questions, nous allons utiliser le module `requests`. Vous pouvez l'installer comme ceci :

```bash
$ pip install requests
```

Créons un fichier Python `quiz_data.py` pour récupérer les questions et réponses du quiz en utilisant l'URL d'API générée ci-dessus.

```python
import requests

parameters = {
    "amount": 10,
    "type": "multiple"
}

response = requests.get(url="https://opentdb.com/api.php", params=parameters)
question_data = response.json()["results"]
```

Dans le script ci-dessus, au lieu d'ajouter directement les paramètres `amount` et `type` dans l'URL, nous avons créé un dictionnaire `parameters` et ajouté les valeurs respectives.

Après cela, nous faisons une requête **GET** en utilisant la bibliothèque _requests_ sur l'URL de l'API Open Trivia DB. Un exemple de réponse JSON ressemble à ceci :

```json
{
  "response_code": 0,
  "results": [
    {
      "category": "Entertainment: Video Games",
      "type": "multiple",
      "difficulty": "hard",
      "question": "What was the name of the hero in the 80s animated video game &#039;Dragon&#039;s Lair&#039;?",
      "correct_answer": "Dirk the Daring",
      "incorrect_answers": ["Arthur", "Sir Toby Belch", "Guy of Gisbourne"]
    },
    {
      "category": "Entertainment: Video Games",
      "type": "multiple",
      "difficulty": "medium",
      "question": "Which of these game franchises were made by Namco?",
      "correct_answer": "Tekken",
      "incorrect_answers": ["Street Fighter", "Mortal Kombat", "Dragon Quest"]
    }
  ]
}
```

Les données JSON contiennent un dictionnaire avec deux clés : `response_code` et `results`. Le `response_code` indique aux développeurs ce que fait l'API. Le `results` est une liste qui nous intéresse. Nous avons donc stocké la valeur des résultats dans une variable appelée `question_data`.

## Comment créer le modèle de question

Le modèle de question n'est rien d'autre qu'une classe Python avec trois attributs : `question_text`, `correct_answer` et `choices`.

_question_text_ est la question, _correct_answer_ est la réponse correcte pour cette question, et _choices_ est une liste d'options pour cette question.

Créons un fichier `question_model.py` et créons la classe dedans :

```python
class Question:
    def __init__(self, question: str, correct_answer: str, choices: list):
        self.question_text = question
        self.correct_answer = correct_answer
        self.choices = choices
```

## Comment créer le cerveau du quiz

Le _QuizBrain_, comme son nom l'indique, est le cerveau de l'application. Créons un fichier `quiz_brain.py` et ajoutons le code suivant :

```python
class QuizBrain:

    def __init__(self, questions):
        self.question_no = 0
        self.score = 0
        self.questions = questions
        self.current_question = None

    def has_more_questions(self):
        """Pour vérifier si le quiz a plus de questions"""
        
        return self.question_no < len(self.questions)

    def next_question(self):
        """Obtenir la question suivante en incrémentant le numéro de question"""
        
        self.current_question = self.questions[self.question_no]
        self.question_no += 1
        q_text = self.current_question.question_text
        return f"Q.{self.question_no}: {q_text}"

    def check_answer(self, user_answer):
        """Vérifier la réponse de l'utilisateur par rapport à la réponse correcte et maintenir le score"""
        
        correct_answer = self.current_question.correct_answer
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            return True
        else:
            return False

    def get_score(self):
        """Obtenir le nombre de réponses correctes, de réponses incorrectes et le pourcentage de score."""
        
        wrong = self.question_no - self.score
        score_percent = int(self.score / self.question_no * 100)
        return (self.score, wrong, score_percent)
```

La classe `QuizBrain` prend `questions`, une liste de questions. En outre, les attributs `question_no` et `score` sont initialisés avec `0` et `current_question` est défini sur `None` initialement.

La première méthode `has_more_questions()` vérifie si le quiz a plus de questions ou non.

La méthode suivante `next_question()` obtient la question de la liste `questions` à l'index `question_no`, puis incrémente l'attribut `question_no` et retourne une question formatée.

La méthode `check_answer()` prend `user_answer` comme argument et vérifie si la réponse de l'utilisateur est correcte ou non. Elle maintient également le _score_ et retourne des valeurs booléennes.

La dernière méthode `get_score()` retourne le nombre de _réponses correctes_, _réponses incorrectes_ et le _pourcentage de score_.

## Comment construire l'interface utilisateur du quiz

Passons à la partie suivante où nous allons créer l'interface utilisateur de l'application. Créez un fichier `quiz_ui.py` pour cette section et ajoutez le code suivant.

```python
class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        # Afficher le titre
        self.display_title()

        # Créer un canevas pour le texte de la question et afficher la question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question ici",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Déclarer une StringVar pour stocker la réponse de l'utilisateur
        self.user_answer = StringVar()

        # Afficher quatre options (boutons radio)
        self.opts = self.radio_buttons()
        self.display_options()

        # Pour montrer si la réponse est correcte ou incorrecte
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Boutons Suivant et Quitter
        self.buttons()

        # Boucle principale
        self.window.mainloop()
```

Dans le code ci-dessus, nous avons créé une classe _QuizInterface_ avec un constructeur. En Python, la méthode `__init__()` est appelée constructeur et est appelée automatiquement chaque fois qu'un objet de cette classe est créé.

Comme discuté dans le flux de travail, la classe _QuizInterface_ prend un argument de type _QuizBrain_. Donc, dans le constructeur, nous avons passé cela comme `quiz_brain`.

La première chose que nous faisons dans Tkinter est de créer une fenêtre en utilisant la classe _Tk_. Vous pouvez définir le titre et la géométrie en utilisant les méthodes `title()` et `geometry()` respectivement.

Ensuite, nous avons appelé quelques méthodes que nous allons créer ensuite. En plus de cela, nous avons créé un canevas en utilisant la classe _Canvas_ où nos questions seront placées. Le canevas est une zone rectangulaire où nous pouvons placer du texte, des graphiques, des widgets, etc.

À l'intérieur du canevas, nous avons ajouté un texte d'exemple pour l'instant en utilisant la méthode `create_text()`. Nous avons ensuite déclaré une variable StringVar appelée `user_answer` pour stocker la réponse de l'utilisateur en type String.

Ensuite, nous avons créé une étiquette `feedback` pour montrer si la réponse est correcte ou incorrecte en utilisant le widget _Label_. Ce widget implémente une boîte d'affichage où nous pouvons placer du texte ou des images. Vous pouvez mettre à jour le texte affiché par ce widget à tout moment.

À la toute fin, nous entrons dans la boucle d'événements principale pour prendre des mesures contre chaque événement déclenché par l'utilisateur en utilisant la méthode `mainloop()`. Maintenant, créons les autres méthodes que nous allons utiliser dans ce constructeur.

### Pour afficher le titre

```python
def display_title(self):
    """Pour afficher le titre"""

    title = Label(self.window, text="Application iQuiz",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))
    title.place(x=0, y=2)
```

Pour afficher un titre, nous avons créé un widget _Label_ sur la fenêtre principale. Nous avons défini ses propriétés `width`, `bg`, `fg` et `font` et cela ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-11-011507.png)

### Pour afficher une question

Comme nous le savons, nous avons déjà créé un canevas pour le texte de la question. Puisque le `question_no` est initialisé avec 0 dans la classe _QuizBrain_, nous pouvons obtenir les questions en utilisant la méthode `next_question()` :

```python
def display_question(self):
    """Pour afficher la question"""

    q_text = self.quiz.next_question()
    self.canvas.itemconfig(self.question_text, text=q_text)
```

En utilisant la méthode `itemconfig()` dans la classe _Canvas_, nous pouvons ajouter du texte de question dynamiquement.

### Pour créer les boutons radio

Puisque les options seront quatre boutons radio, nous allons utiliser la classe _RadioButton_ du module Tkinter.

```python
def radio_buttons(self):
        """Pour créer quatre options (boutons radio)"""
	# initialiser la liste avec une liste vide d'options
    choice_list = []

    # position de la première option
    y_pos = 220

    # ajouter les options à la liste
    while len(choice_list) < 4:

        # définir les propriétés du bouton radio
        radio_btn = Radiobutton(self.window, text="", variable=self.user_answer, value='', font=("ariel", 14))

        # ajouter le bouton à la liste
        choice_list.append(radio_btn)

        # placer le bouton
        radio_btn.place(x=200, y=y_pos)

        # incrémenter la position de l'axe y de 40
        y_pos += 40

    # retourner les boutons radio
    return choice_list
```

Tout d'abord, nous avons créé une liste `choice_list`. Nous avons défini la position y de la première option à 220. En utilisant une boucle while, nous avons créé quatre instances de la classe RadioButton sur la fenêtre principale. Remarquez l'attribut variable défini comme `user_answer` que nous avons créé précédemment.

Nous allons ajouter ces boutons radio dans la `choice_list` et les placer à une distance de 40 unités sur l'axe y. Nous retournons ensuite la `choice_list`.

### Pour afficher les options

Nous allons utiliser cette méthode pour définir l'attribut `text` et `value` de chaque bouton radio.

```python
def display_options(self):
    """Pour afficher quatre options"""

    val = 0

    # désélectionner les options
    self.user_answer.set(None)

    # boucler sur les options à afficher pour le
    # texte des boutons radio.
    for option in self.quiz.current_question.choices:
        self.opts[val]['text'] = option
        self.opts[val]['value'] = option
        val += 1
```

Nous avons d'abord défini `user_answer` sur None. Ensuite, nous itérons sur les `choices` pour la `current_question` et définissons les deux propriétés l'une après l'autre pour chaque option.

### Pour afficher les boutons

Comme vous pouvez le voir, nous avons deux boutons : Suivant et Quitter.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-11-013502.png)

Nous allons utiliser le bouton Suivant pour passer à la question suivante (si elle existe). Et nous allons utiliser le bouton Quitter pour quitter le quiz et détruire la fenêtre immédiatement.

Nous utilisons la classe _Button_ du module Tkinter pour les créer. La fonctionnalité de ces boutons est ajoutée dans l'attribut `command`.

Pour le bouton Suivant, nous allons créer une méthode séparée juste après cette section. Pour le bouton Quitter, nous détruisons simplement la fenêtre principale.

### Fonctionnalité du bouton Suivant

```python
def next_btn(self):
    """Pour montrer le feedback pour chaque réponse et continuer à vérifier s'il y a plus de questions"""

    # Vérifier si la réponse est correcte
    if self.quiz.check_answer(self.user_answer.get()):
        self.feedback["fg"] = "green"
        self.feedback["text"] = 'Bonne réponse ! \U0001F44D'
    else:
        self.feedback['fg'] = 'red'
        self.feedback['text'] = ('\u274E Oups ! \n'
                                     f'La bonne réponse est : {self.quiz.current_question.correct_answer}')

    if self.quiz.has_more_questions():
        # Passe à la question suivante pour afficher la question suivante et ses options
        self.display_question()
        self.display_options()
    else:
        # s'il n'y a plus de questions, alors il affiche le score
        self.display_result()

        # détruit la fenêtre
        self.window.destroy()
```

Le bouton suivant a beaucoup de choses à faire.

Tout d'abord, il vérifie si la réponse sélectionnée par l'utilisateur est correcte ou non en utilisant la méthode `check_answer`. Il montre le feedback en conséquence.

Ensuite, il vérifie si le quiz a plus de questions ou non. S'il y a plus de questions, il appelle les méthodes `display_question` et `display_options` à nouveau. S'il n'y a plus de questions, il appelle la méthode `display_result` pour montrer le résultat et détruit ensuite la fenêtre principale.

### Pour afficher les résultats

À la fin du quiz, nous devons montrer les résultats à l'utilisateur comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-11-014531.png)

Ici, comme vous pouvez le voir, nous affichons le pourcentage de score basé sur les réponses correctes et incorrectes.

```python
def display_result(self):
    """Pour afficher le résultat en utilisant messagebox"""
    correct, wrong, score_percent = self.quiz.get_score()

    correct = f"Correct : {correct}"
    wrong = f"Incorrect : {wrong}"

    # calcule le pourcentage de réponses correctes
    result = f"Score : {score_percent}%"

    # Affiche une boîte de message pour afficher le résultat
    messagebox.showinfo("Résultat", f"{result}\n{correct}\n{wrong}")
```

Nous utilisons la méthode `get_score` pour obtenir les calculs, puis nous utilisons la méthode `showinfo` de la classe `messagebox` pour afficher un message popup.

### Code complet pour `quiz_ui.py`

```python
from tkinter import Tk, Canvas, StringVar, Label, Radiobutton, Button, messagebox
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("iQuiz App")
        self.window.geometry("850x530")

        # Afficher le titre
        self.display_title()

        # Créer un canevas pour le texte de la question et afficher la question
        self.canvas = Canvas(width=800, height=250)
        self.question_text = self.canvas.create_text(400, 125,
                                                     text="Question ici",
                                                     width=680,
                                                     fill=THEME_COLOR,
                                                     font=(
                                                         'Ariel', 15, 'italic')
                                                     )
        self.canvas.grid(row=2, column=0, columnspan=2, pady=50)
        self.display_question()

        # Déclarer une StringVar pour stocker la réponse de l'utilisateur
        self.user_answer = StringVar()

        # Afficher quatre options (boutons radio)
        self.opts = self.radio_buttons()
        self.display_options()

        # Pour montrer si la réponse est correcte ou incorrecte
        self.feedback = Label(self.window, pady=10, font=("ariel", 15, "bold"))
        self.feedback.place(x=300, y=380)

        # Boutons Suivant et Quitter
        self.buttons()

        # Boucle principale
        self.window.mainloop()

    def display_title(self):
        """Pour afficher le titre"""

        # Titre
        title = Label(self.window, text="Application iQuiz",
                      width=50, bg="green", fg="white", font=("ariel", 20, "bold"))

        # place du titre
        title.place(x=0, y=2)

    def display_question(self):
        """Pour afficher la question"""

        q_text = self.quiz.next_question()
        self.canvas.itemconfig(self.question_text, text=q_text)

    def radio_buttons(self):
        """Pour créer quatre options (boutons radio)"""

        # initialiser la liste avec une liste vide d'options
        choice_list = []

        # position de la première option
        y_pos = 220

        # ajouter les options à la liste
        while len(choice_list) < 4:

            # définir les propriétés du bouton radio
            radio_btn = Radiobutton(self.window, text="", variable=self.user_answer,
                                    value='', font=("ariel", 14))

            # ajouter le bouton à la liste
            choice_list.append(radio_btn)

            # placer le bouton
            radio_btn.place(x=200, y=y_pos)

            # incrémenter la position de l'axe y de 40
            y_pos += 40

        # retourner les boutons radio
        return choice_list

    def display_options(self):
        """Pour afficher quatre options"""

        val = 0

        # désélectionner les options
        self.user_answer.set(None)

        # boucler sur les options à afficher pour le
        # texte des boutons radio.
        for option in self.quiz.current_question.choices:
            self.opts[val]['text'] = option
            self.opts[val]['value'] = option
            val += 1

    def next_btn(self):
        """Pour montrer le feedback pour chaque réponse et continuer à vérifier s'il y a plus de questions"""

        # Vérifier si la réponse est correcte
        if self.quiz.check_answer(self.user_answer.get()):
            self.feedback["fg"] = "green"
            self.feedback["text"] = 'Bonne réponse ! \U0001F44D'
        else:
            self.feedback['fg'] = 'red'
            self.feedback['text'] = ('\u274E Oups ! \n'
                                     f'La bonne réponse est : {self.quiz.current_question.correct_answer}')

        if self.quiz.has_more_questions():
            # Passe à la question suivante pour afficher la question suivante et ses options
            self.display_question()
            self.display_options()
        else:
            # s'il n'y a plus de questions, alors il affiche le score
            self.display_result()

            # détruit la fenêtre
            self.window.destroy()

    def buttons(self):
        """Pour afficher le bouton suivant et le bouton quitter"""

        # Le premier bouton est le bouton Suivant pour passer à la
        # question suivante
        next_button = Button(self.window, text="Suivant", command=self.next_btn,
                             width=10, bg="green", fg="white", font=("ariel", 16, "bold"))

        # placer le bouton sur l'écran
        next_button.place(x=350, y=460)

        # C'est le deuxième bouton qui est utilisé pour quitter la fenêtre
        quit_button = Button(self.window, text="Quitter", command=self.window.destroy,
                             width=5, bg="red", fg="white", font=("ariel", 16, " bold"))

        # placer le bouton Quitter sur l'écran
        quit_button.place(x=700, y=50)

    def display_result(self):
        """Pour afficher le résultat en utilisant messagebox"""
        correct, wrong, score_percent = self.quiz.get_score()

        correct = f"Correct : {correct}"
        wrong = f"Incorrect : {wrong}"

        # calcule le pourcentage de réponses correctes
        result = f"Score : {score_percent}%"

        # Affiche une boîte de message pour afficher le résultat
        messagebox.showinfo("Résultat", f"{result}\n{correct}\n{wrong}")
```

## Comment tout assembler

Puisque tous les composants sont prêts à être intégrés ensemble, créons un fichier `main.py` et ajoutons le contenu suivant :

```python
from question_model import Question
from quiz_data import question_data
from quiz_brain import QuizBrain
from quiz_ui import QuizInterface
from random import shuffle
import html

question_bank = []
for question in question_data:
    choices = []
    question_text = html.unescape(question["question"])
    correct_answer = html.unescape(question["correct_answer"])
    incorrect_answers = question["incorrect_answers"]
    for ans in incorrect_answers:
        choices.append(html.unescape(ans))
    choices.append(correct_answer)
    shuffle(choices)
    new_question = Question(question_text, correct_answer, choices)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

quiz_ui = QuizInterface(quiz)


print("Vous avez terminé le quiz")
print(f"Votre score final était : {quiz.score}/{quiz.question_no}")
```

Nous avons d'abord importé toutes les classes des différents fichiers que nous avons créés ci-dessus. En plus de cela, nous avons également besoin de la méthode `shuffle` du module `random` et du module `html`.

Nous avons une liste appelée `question_bank`. Nous itérons sur `question_data` que nous recevons du fichier `quiz_data.py`. Si vous regardez la réponse d'exemple, vous trouverez du texte comme `&#039;Dragon&#039`. Ceux-ci doivent être déséchappés en utilisant la méthode `html.unescape`.

Nous avons une liste `choices` qui contiendra la bonne réponse ainsi que les mauvaises réponses. La liste sera mélangée en utilisant la méthode `shuffle` du module `random`.

Après avoir mélangé, nous créons une question en utilisant le modèle `Question` du fichier `quiz_model.py` et l'ajoutons à la liste `question_bank`.

Ensuite, nous créons un objet appelé `quiz` de la classe _QuizBrain_ qui nécessite une liste de questions. Nous lui passons donc la liste `question_bank`.

Après cela, nous créons un objet `quiz_ui` de la classe _QuizInterface_ qui nécessite un objet de la classe QuizBrain, nous avons donc passé le nouvel objet `quiz` créé.

Maintenant que tout est prêt, nous sommes prêts à exécuter l'application.

```bash
$ python main.py
```

## Conclusion

Félicitations pour être arrivé à la fin ! C'était un tutoriel de base sur la façon dont vous pouvez construire une application de quiz GUI en utilisant Tkinter. Vous pouvez ajouter plus de fonctionnalités et rendre l'interface utilisateur plus attrayante si vous le souhaitez.

Voici le dépôt de code : [https://github.com/ashutoshkrris/GUI-Quiz-Tkinter](https://github.com/ashutoshkrris/GUI-Quiz-Tkinter)

Pour Windows, vous pouvez télécharger l'application exécutable depuis [ici](https://github.com/ashutoshkrris/GUI-Quiz-Tkinter/raw/master/quiz.exe).