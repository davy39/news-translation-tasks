---
title: Comment créer un agent de codage IA avec Python et Gemini
subtitle: ''
author: Lane Wagner
co_authors: []
series: null
date: '2025-10-02T15:43:29.742Z'
originalURL: https://freecodecamp.org/news/build-an-ai-coding-agent-with-python-and-gemini
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1759418643581/2470669e-8592-463e-8b4c-55eace8dd80a.png
tags:
- name: AI
  slug: ai
- name: Python
  slug: python
- name: gemini
  slug: gemini
- name: handbook
  slug: handbook
seo_title: Comment créer un agent de codage IA avec Python et Gemini
seo_desc: In this handbook, you'll build a basic version of Claude Code using Google's
  free Gemini API. If you've ever used Cursor or Claude Code as an "agentic" AI code
  editor, then you should be familiar with what we'll be building here. As long as
  you have ...
---

Dans ce guide, vous allez construire une version de base de Claude Code en utilisant l'API [Gemini gratuite](https://ai.google.dev/gemini-api/docs/pricing) de Google. Si vous avez déjà utilisé Cursor ou Claude Code en tant qu'éditeur de code IA « agentique », alors vous devriez être familier avec ce que nous allons construire ici. Tant que vous avez un LLM à votre disposition, il est en fait étonnamment simple de construire un agent personnalisé (relativement) efficace.

Ceci est un guide textuel entièrement gratuit. Cela dit, il existe deux autres options pour suivre ce cours :

Vous pouvez essayer la version interactive de ce [cours sur les agents IA sur Boot.dev](https://www.boot.dev/courses/build-ai-agent-python), avec des défis de codage et des projets, ou regarder le [tutoriel vidéo](https://www.youtube.com/watch?v=YtHdaXuOAks) de ce cours sur la chaîne YouTube de FreeCodeCamp.

%[https://www.youtube.com/watch?v=YtHdaXuOAks] 

## Prérequis

* Vous devriez déjà être familier avec les bases de Python. Si ce n'est pas le cas, consultez ce [cours Python sur Boot.dev](https://www.boot.dev/courses/learn-code-python).
    
* Vous devriez déjà savoir utiliser une ligne de commande de type Unix. Si ce n'est pas le cas, [consultez ce cours Linux sur Boot.dev](https://www.boot.dev/courses/learn-linux).
    

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Que fait l'agent ?](#heading-que-fait-lagent)
    
* [Objectifs d'apprentissage](#heading-objectifs-dapprentissage)
    
* [Configuration de Python](#heading-configuration-de-python)
    
* [Comment intégrer l'API Gemini](#heading-comment-integrer-lapi-gemini)
    
* [Entrée en ligne de commande](#heading-entree-en-ligne-de-commande)
    
* [Structure des messages](#heading-structure-des-messages)
    
* [Mode verbeux](#heading-mode-verbeux)
    
* [Comment construire le projet de calculatrice](#heading-comment-construire-le-projet-de-calculatrice)
    
* [Fonctions de l'agent](#heading-fonctions-de-lagent)
    
* [Prompt système](#heading-prompt-systeme)
    
* [Déclaration de fonction](#heading-declaration-de-fonction)
    
* [Plus de déclarations de fonctions](#heading-plus-de-declarations-de-fonctions)
    
* [Appel de fonction](#heading-appel-de-fonction)
    
* [Construction de la boucle de l'agent](#heading-construction-de-la-boucle-de-lagent)
    
* [Conclusion](#heading-conclusion)
    

## Que fait l'agent ?

Le programme que nous construisons est un outil CLI qui :

1\. Accepte une tâche de codage (par exemple, « les chaînes de caractères ne se séparent pas dans mon application, merci de corriger »)

2\. Choisit parmi un ensemble de fonctions prédéfinies pour travailler sur la tâche, par exemple :

* Scanner les fichiers d'un répertoire
    
* Lire le contenu d'un fichier
    
* Écraser le contenu d'un fichier
    
* Exécuter l'interpréteur Python sur un fichier
    

3\. Répète l'étape 2 jusqu'à ce que la tâche soit terminée (ou qu'elle échoue lamentablement, ce qui est possible)

Par exemple, j'ai une application de calculatrice buggée, j'ai donc utilisé mon agent pour corriger le code :

```bash
> uv run main.py "fix my calculator app, its not starting correctly"
# Calling function: get_files_info
# Calling function: get_file_content
# Calling function: write_file
# Calling function: run_python_file
# Calling function: write_file
# Calling function: run_python_file
# Final response:
# Great! The calculator app now seems to be working correctly. The output shows the expression and the result in a formatted way.
```

## Objectifs d'apprentissage

Les objectifs d'apprentissage de ce projet sont :

* Vous initier aux projets Python multi-répertoires
    
* Comprendre comment les outils d'IA que vous utiliserez presque certainement au travail fonctionnent réellement sous le capot
    
* Pratiquer vos compétences en Python et en programmation fonctionnelle
    

Le but n'est *pas* de construire un LLM à partir de zéro, mais d'utiliser un LLM pré-entraîné pour construire un *agent* à partir de zéro.

## Configuration de Python

Configurons un environnement virtuel pour notre projet. Les environnements virtuels sont le moyen utilisé par Python pour séparer les dépendances (par exemple, les bibliothèques Google AI que nous allons utiliser) des autres projets sur notre machine.

Utilisez `uv` pour créer un nouveau projet. Cela créera le répertoire et initialisera également Git.

```bash
uv init your-project-name
cd your-project-name
```

Créez un environnement virtuel au niveau supérieur de votre répertoire de projet :

```bash
uv venv
```

**Attention** : Ajoutez toujours le répertoire `venv` à votre fichier `.gitignore`.

Activez l'environnement virtuel :

```bash
source .venv/bin/activate
```

Vous devriez voir `(your-project-name)` au début de votre invite de terminal, par exemple, le mien est :

```bash
(aiagent) wagslane@MacBook-Pro-2 aiagent %
```

Utilisez `uv` pour ajouter deux dépendances au projet. Elles seront ajoutées au fichier `pyproject.toml` :

```bash
uv add google-genai==1.12.1
uv add python-dotenv==1.1.0
```

Cela indique à Python que ce projet nécessite [`google-genai`](https://pypi.org/project/google-genai/) version `1.12.1` et [`python-dotenv`](https://pypi.org/project/python-dotenv/) version `1.1.0`.

Pour exécuter le projet en utilisant l'environnement virtuel `uv`, utilisez :

```bash
uv run main.py
```

Dans votre terminal, vous devriez voir `Hello from YOUR PROJECT NAME`.

## Comment intégrer l'API Gemini

Les [Large Language Models (LLMs)](https://www.cloudflare.com/learning/ai/what-is-large-language-model/) sont la technologie d'IA sophistiquée qui a fait couler beaucoup d'encre dans le monde de l'IA récemment. Des produits comme ChatGPT, Claude, Cursor et Google Gemini sont tous propulsés par des LLMs. Pour les besoins de ce cours, vous pouvez considérer un LLM comme un générateur de texte intelligent. Il fonctionne exactement comme ChatGPT : vous lui donnez un prompt, et il vous renvoie un texte qu'il estime répondre à votre prompt.

Nous allons utiliser l'[API Gemini de Google](https://ai.google.dev/gemini-api/docs/pricing) pour alimenter notre agent dans ce cours. Il est raisonnablement intelligent, mais plus important encore pour nous, il dispose d'un niveau gratuit.

### Tokens

Vous pouvez considérer les tokens comme la monnaie des LLMs. C'est la façon dont les LLMs mesurent la quantité de texte qu'ils doivent traiter. Les tokens représentent [environ 4 caractères](https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them) pour la plupart des modèles. Il est important, lorsqu'on travaille avec des APIs de LLM, de comprendre combien de tokens vous utilisez.

Nous resterons largement dans les limites du niveau gratuit de l'API Gemini, mais nous surveillerons tout de même notre consommation de tokens !

**Attention** : Sachez que tous les appels API, y compris ceux effectués lors des tests locaux, consomment des tokens de votre quota gratuit. Si vous épuisez votre quota, vous devrez peut-être attendre qu'il soit réinitialisé (généralement 24 heures) pour continuer la leçon. Régénérer votre clé API ne réinitialisera pas votre quota.

Voici comment créer une clé API :

1. Créez un compte sur [Google AI Studio](https://aistudio.google.com/) si vous n'en avez pas déjà un.
    
2. Cliquez sur le bouton « Create API Key ». Vous pouvez utiliser la [documentation](https://ai.google.dev/gemini-api/docs/api-key) si vous êtes perdu.
    

Si vous avez déjà un compte GCP et un projet, vous pouvez créer la clé API dans ce projet. Sinon, AI Studio en créera un automatiquement pour vous.

3\. Copiez la clé API, puis collez-la dans un nouveau fichier `.env` dans votre répertoire de projet. Le fichier devrait ressembler à ceci :

```bash
GEMINI_API_KEY="your_api_key_here"
```

4\. Ajoutez le fichier `.env` à votre `.gitignore`.

**Danger** : Nous ne voulons jamais Commit de clés API, de mots de passe ou d'autres informations sensibles dans Git.

5\. Mettez à jour le fichier `main.py`. Au démarrage du programme, chargez les variables d'environnement du fichier `.env` en utilisant la bibliothèque `dotenv` et lisez la clé API :

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
```

6\. Importez la bibliothèque `genai` et utilisez la clé API pour créer une nouvelle instance d'un [client Gemini :](https://googleapis.github.io/python-genai/#create-a-client)

```python
from google import genai

client = genai.Client(api_key=api_key)
```

7\. Utilisez la [méthode `client.models.generate_content()`](https://googleapis.github.io/python-genai/#generate-content) pour obtenir une réponse du modèle `gemini-2.0-flash-001`. Vous devrez utiliser deux paramètres nommés :

* `model` : Le nom du modèle `gemini-2.0-flash-001` (celui-ci a un niveau gratuit généreux)
    
* `contents` : Le prompt à envoyer au modèle (une chaîne de caractères). Utilisez ce prompt :
    

« Pourquoi [Boot.dev](http://Boot.dev) et FreeCodeCamp sont-ils d'excellents endroits pour apprendre le développement backend ? Utilisez un paragraphe maximum. »

La méthode `generate_content` renvoie un [objet `GenerateContentResponse`.](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse) Affichez la [propriété `.text`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.text) de la réponse pour voir la réponse du modèle.

Si tout fonctionne comme prévu, vous devriez pouvoir exécuter votre code et voir la réponse du modèle dans votre terminal.

8\. En plus d'afficher la réponse textuelle, affichez le nombre de tokens consommés par l'interaction dans ce format :

```plaintext
Prompt tokens: X
Response tokens: Y
```

La réponse possède une propriété [`.usage_metadata`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponseDict.usage_metadata) qui contient à la fois :

* Une propriété `prompt_token_count` (tokens dans le prompt)
    
* Une propriété `candidates_token_count` (tokens dans la réponse)
    

**Danger** : L'API Gemini est un *service web externe* et il arrive qu'il soit *lent et peu fiable*. Soyez donc patient.

## Entrée en ligne de commande

Nous avons codé en dur le prompt envoyé à Gemini, ce qui n'est... pas très utile. Mettons à jour notre code pour accepter le prompt comme argument de ligne de commande.

Nous ne voulons pas que nos utilisateurs aient à modifier le code pour changer le prompt.

Mettez à jour votre code pour accepter un argument de ligne de commande pour le prompt. Par exemple :

```bash
uv run main.py "Why are episodes 7-9 so much worse than 1-6?"
```

**Conseil** : La variable [`sys.argv`](https://docs.python.org/3/library/sys.html#sys.argv) est une liste de chaînes de caractères représentant tous les arguments de ligne de commande passés au script. Le premier élément est le nom du script, et le reste sont les arguments. Assurez-vous d'utiliser `import sys` pour l'utiliser.

Si le prompt n'est pas fourni, affichez un message d'erreur et quittez le programme avec le code de sortie 1.

## Structure des messages

Les APIs de LLM ne sont généralement pas utilisées de manière « ponctuelle » (one-shot), par exemple :

* Prompt : « Quel est le sens de la vie ? »
    
* Réponse : « 42 »
    

Elles fonctionnent de la même manière que ChatGPT dans une conversation. La conversation a un historique, et si nous gardons trace de cet historique, alors à chaque nouveau prompt, le modèle peut voir l'intégralité de la conversation et répondre dans le contexte plus large de celle-ci.

### Rôles

Il est important de noter que chaque message de la conversation a un « rôle ». Dans le contexte d'une application de chat comme ChatGPT, vos conversations ressembleraient à ceci :

* **user** : « Quel est le sens de la vie ? »
    
* **model** : « 42 »
    
* **user** : « Attends, qu'est-ce que tu viens de dire ? »
    
* **model** : « 42. C'est la réponse à la question ultime sur la vie, l'univers et tout le reste. »
    
* **user** : « Mais pourquoi ? »
    
* **model** : « Parce que Douglas Adams l'a dit. »
    

Ainsi, bien que notre programme soit encore « ponctuel » pour l'instant, mettons à jour notre code pour stocker une liste de messages dans la conversation, et passer le « rôle » de manière appropriée.

Créez une nouvelle liste de [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content), et définissez le prompt de l'utilisateur comme le seul message (pour l'instant) :

```python
from google.genai import types

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)]),
]
```

Mettez à jour votre appel à [`models.generate_content`](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate_content) pour utiliser la liste de messages :

```python
response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)
```

**Info** : À l'avenir, nous ajouterons plus de messages à la liste au fur et à mesure que l'agent effectue ses tâches dans une boucle.

## Mode verbeux

Au fur et à mesure que vous déboguez et construisez votre agent IA, vous voudrez probablement afficher beaucoup plus de contexte dans la console, mais en même temps, nous ne voulons pas rendre l'expérience utilisateur de notre outil CLI trop bruyante.

Ajoutons un drapeau de ligne de commande optionnel, `--verbose`, qui nous permettra d'activer ou de désactiver la sortie « verbeuse ». Quand nous voudrons voir plus d'infos, nous l'activerons simplement.

Ajoutez un nouvel argument de ligne de commande, `--verbose`. Il doit être fourni après le prompt s'il est inclus. Par exemple :

```bash
uv run main.py "What is the meaning of life?" --verbose
```

Si le drapeau `--verbose` est inclus, la sortie de la console doit inclure :

* Le prompt de l'utilisateur : `"User prompt: {user_prompt}"`
    
* Le nombre de tokens du prompt à chaque itération : `"Prompt tokens: {prompt_tokens}"`
    
* Le nombre de tokens de la réponse à chaque itération : `"Response tokens: {response_tokens}"`
    

Sinon, il ne doit pas afficher ces éléments.

## Comment construire le projet de calculatrice

Puisque nous construisons un agent IA, l'agent aura besoin d'un projet sur lequel travailler. J'ai construit une petite application de calculatrice en ligne de commande que nous utiliserons comme projet de test pour que l'IA puisse lire, mettre à jour et exécuter.

Tout d'abord, créez un nouveau répertoire appelé `calculator` à la racine de votre projet. Ensuite, copiez et collez les fichiers `main.py` et `tests.py` ci-dessous dans le répertoire `calculator`.

*Ne vous inquiétez pas trop du fonctionnement de ce code - notre projet n'est pas de construire une calculatrice, c'est le projet sur lequel notre projet d'agent IA travaillera !*

```python
# main.py
import sys
from pkg.calculator import Calculator
from pkg.render import format_json_output


def main():
    calculator = Calculator()
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    expression = " ".join(sys.argv[1:])
    try:
        result = calculator.evaluate(expression)
        if result is not None:
            to_print = format_json_output(expression, result)
            print(to_print)
        else:
            print("Error: Expression is empty or contains only whitespace.")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

```python
# tests.py

import unittest
from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self):
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self):
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self):
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self):
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")


if __name__ == "__main__":
    unittest.main()
```

Créez un nouveau répertoire dans `calculator` appelé `pkg`. Ensuite, copiez et collez les fichiers `calculator.py` et `render.py` ci-dessous dans le répertoire `pkg`.

```python
# calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }


    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)


    def _evaluate_infix(self, tokens):
        values = []
        operators = []

        for token in tokens:
            if token in self.operators:
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)

            else:
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
```

```python
# render.py

import json

def format_json_output(expression: str, result: float, indent: int = 2) -> str:
    if isinstance(result, float) and result.is_integer():
        result_to_dump = int(result)
    else:
        result_to_dump = result

    output_data = {
        "expression": expression,
        "result": result_to_dump,
    }
    return json.dumps(output_data, indent=indent)
```

Voici la structure finale :

```plaintext
├── calculator
│   ├── main.py
│   ├── pkg
│   │   ├── calculator.py
│   │   └── render.py
│   └── tests.py
├── main.py
├── pyproject.toml
├── README.md
└── uv.lock
```

Exécutez les tests de `calculator` :

```bash
uv run calculator/tests.py
```

Espérons que tous les tests passent !

Maintenant, exécutez l'application de calculatrice :

```bash
uv run calculator/main.py "3 + 5"
```

Espérons que vous obtenez 8 !

## Fonctions de l'agent

Nous devons donner à notre agent la capacité de *faire des choses*. Nous allons commencer par lui donner la capacité de lister le contenu d'un répertoire et de voir les métadonnées des fichiers (nom et taille).

Avant d'intégrer cette fonction à notre agent LLM, construisons simplement la fonction elle-même. Rappelez-vous, les LLMs travaillent avec du texte, donc notre objectif avec cette fonction sera qu'elle accepte un chemin de répertoire et renvoie une chaîne de caractères représentant le contenu de ce répertoire.

Créez un nouveau répertoire appelé `functions` à la racine de votre projet (pas à l'intérieur du répertoire `calculator`). À l'intérieur, créez un nouveau fichier appelé `get_files_info.py`. À l'intérieur, écrivez cette fonction :

```python
def get_files_info(working_directory, directory="."):
```

Voici ma structure de projet jusqu'à présent :

```plaintext
 project_root/
 ├── calculator/
 │   ├── main.py
 │   ├── pkg/
 │   │   ├── calculator.py
 │   │   └── render.py
 │   └── tests.py
 └── functions/
     └── get_files_info.py
```

Le paramètre `directory` doit être traité comme un chemin *relatif* au sein du `working_directory`. Utilisez `os.path.join(working_directory, directory)` pour créer le chemin complet, puis validez qu'il reste dans les limites du répertoire de travail.

Si le chemin absolu vers le `directory` est en dehors du `working_directory`, renvoyez un message d'erreur sous forme de chaîne :

```python
f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
```

Cela donnera à notre LLM des garde-fous : nous ne voulons jamais qu'il puisse effectuer un travail en dehors du « working_directory » que nous lui donnons.

**Danger** : Sans cette restriction, le LLM pourrait s'égarer n'importe où sur la machine, lire des fichiers sensibles ou écraser des données importantes. C'est une étape très importante que nous intégrerons dans chaque fonction que le LLM peut appeler.

Si l'argument `directory` n'est pas un répertoire, renvoyez à nouveau une chaîne d'erreur :

```python
f'Error: "{directory}" is not a directory'
```

**Attention** : Toutes nos fonctions d'« appel d'outil », y compris `get_files_info`, doivent toujours renvoyer une chaîne de caractères. Si des erreurs peuvent être levées à l'intérieur, nous devons les intercepter et renvoyer une chaîne décrivant l'erreur à la place. Cela permettra au LLM de gérer les erreurs avec élégance.

Construisez et renvoyez une chaîne représentant le contenu du répertoire. Elle doit utiliser ce format :

```bash
- README.md: file_size=1032 bytes, is_dir=False
- src: file_size=128 bytes, is_dir=True
- package.json: file_size=1234 bytes, is_dir=False
```

**Conseil** : Les tailles exactes des fichiers et même l'ordre des fichiers peuvent varier selon votre système d'exploitation et votre système de fichiers. Votre sortie n'a pas besoin de correspondre à l'exemple octet par octet, seulement au format général.

Si des erreurs sont levées par les fonctions de la bibliothèque standard, interceptez-les et renvoyez à la place une chaîne décrivant l'erreur. Préfixez toujours les chaînes d'erreur par « Error: ».

Voici mon implémentation complète :

```python
import os


def get_files_info(working_directory, directory="."):
    abs_working_dir = os.path.abspath(working_directory)
    target_dir = os.path.abspath(os.path.join(working_directory, directory))
    if not target_dir.startswith(abs_working_dir):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for filename in os.listdir(target_dir):
            filepath = os.path.join(target_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(filepath)
            file_size = os.path.getsize(filepath)
            files_info.append(
                f"- {filename}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"
```

Voici quelques fonctions de la bibliothèque standard que vous trouverez utiles :

* [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath) : Obtenir un chemin absolu à partir d'un chemin relatif
    
* [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join) : Joindre deux chemins ensemble en toute sécurité (gère les barres obliques)
    
* [`.startswith()`](https://docs.python.org/3/library/stdtypes.html#str.startswith) : Vérifier si une chaîne commence par une sous-chaîne
    
* [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir) : Vérifier si un chemin est un répertoire
    
* [`os.listdir()`](https://docs.python.org/3/library/os.html#os.listdir) : Lister le contenu d'un répertoire
    
* [`os.path.getsize()`](https://docs.python.org/3/library/os.path.html#os.path.getsize) : Obtenir la taille d'un fichier
    
* [`os.path.isfile()`](https://docs.python.org/3/library/os.path.html#os.path.isfile) : Vérifier si un chemin est un fichier
    
* [`.join()`](https://docs.python.org/3/library/stdtypes.html#str.join) : Joindre une liste de chaînes de caractères avec un séparateur
    

### Fonction de récupération du contenu d'un fichier

Maintenant que nous avons une fonction capable de récupérer le contenu d'un répertoire, nous en avons besoin d'une capable de récupérer le contenu d'un fichier. Encore une fois, nous renverrons simplement le contenu du fichier sous forme de chaîne, ou éventuellement une chaîne d'erreur si quelque chose s'est mal passé.

Comme toujours, nous limiterons la portée de la fonction à un répertoire de travail spécifique.

Créez une nouvelle fonction dans votre répertoire `functions`. Voici la signature que j'ai utilisée :

```python
def get_file_content(working_directory, file_path):
```

Si le `file_path` est en dehors du `working_directory`, renvoyez une chaîne avec une erreur :

```python
f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
```

Si le `file_path` n'est pas un fichier, renvoyez à nouveau une chaîne d'erreur :

```python
f'Error: File not found or is not a regular file: "{file_path}"'
```

Lisez le fichier et renvoyez son contenu sous forme de chaîne.

* Si le fichier fait plus de `10000` caractères, tronquez-le à `10000` caractères et ajoutez ce message à la fin `[...File "{file_path}" truncated at 10000 characters]`.
    
* Au lieu de coder en dur la limite de `10000` caractères, je l'ai stockée dans un fichier [`config.py`](http://config.py).
    

**Attention** : Nous ne voulons pas lire accidentellement un fichier gigantesque et envoyer toutes ces données au LLM. C'est un bon moyen de brûler vos limites de tokens.

Si des erreurs sont levées par les fonctions de la bibliothèque standard, interceptez-les et renvoyez à la place une chaîne décrivant l'erreur. Préfixez toujours les erreurs par « Error: ».

Tout d'abord, créez `config.py` :

```python
MAX_CHARS = 10000
WORKING_DIR = "./calculator"
```

Voici mon implémentation complète pour `functions/get_file_content.py` :

```python
import os
from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    try:
        with open(abs_file_path, "r") as f:
            content = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                )
        return content
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'
```

* [`os.path.abspath`](https://docs.python.org/3/library/os.path.html#os.path.abspath) : Obtenir un chemin absolu à partir d'un chemin relatif
    
* [`os.path.join`](https://docs.python.org/3/library/os.path.html#os.path.join) : Joindre deux chemins ensemble en toute sécurité (gère les barres obliques)
    
* [`.startswith`](https://docs.python.org/3/library/stdtypes.html#str.startswith) : Vérifier si une chaîne commence par une sous-chaîne spécifique
    
* [`os.path.isfile`](https://docs.python.org/3/library/os.path.html#os.path.isfile) : Vérifier si un chemin est un fichier
    

Exemple de lecture d'un fichier :

```python
MAX_CHARS = 10000

with open(file_path, "r") as f:
    file_content_string = f.read(MAX_CHARS)
```

### Fonction d'écriture de fichier

Jusqu'à présent, notre programme était en lecture seule... maintenant ça devient vraiment <s>dangereux</s> amusant ! Nous allons donner à notre agent la capacité d'écrire et d'écraser des fichiers.

Créez une nouvelle fonction dans votre répertoire `functions`. Voici la signature que j'ai utilisée :

```python
def write_file(working_directory, file_path, content):
```

Si le `file_path` est en dehors du `working_directory`, renvoyez une chaîne avec une erreur :

```python
f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
```

Si le `file_path` n'existe pas, créez-le. Comme toujours, s'il y a des erreurs, renvoyez une chaîne représentant l'erreur, préfixée par « Error: ». Écrasez ensuite le contenu du fichier avec l'argument `content`. En cas de succès, renvoyez une chaîne avec le message :

```python
f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
```

**Conseil** : Il est important de renvoyer une chaîne de succès pour que notre LLM sache que l'action qu'il a entreprise a réellement fonctionné. Boucles de rétroaction, boucles de rétroaction, boucles de rétroaction.

Voici mon implémentation complète pour `functions/write_file_content.py` :

```python
import os


def write_file(working_directory, file_path, content):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        try:
            os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
        except Exception as e:
            return f"Error: creating directory: {e}"
    if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
        return f'Error: "{file_path}" is a directory, not a file'
    try:
        with open(abs_file_path, "w") as f:
            f.write(content)
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as e:
        return f"Error: writing to file: {e}"
```

* [`os.path.exists`](https://docs.python.org/3/library/os.path.html#os.path.exists) : Vérifier si un chemin existe
    
* [`os.makedirs`](https://docs.python.org/3/library/os.html#os.makedirs) : Créer un répertoire et tous ses parents
    
* [`os.path.dirname`](https://docs.python.org/3/library/os.path.html#os.path.dirname) : Renvoyer le nom du répertoire
    

Exemple d'écriture dans un fichier :

```python
with open(file_path, "w") as f:
    f.write(content)
```

### Fonction d'exécution Python

Si vous pensiez que permettre à un LLM d'écrire des fichiers était une mauvaise idée...

> Vous n'avez encore rien vu ! (loué soit le [basilique](https://en.wikipedia.org/wiki/Roko%27s_basilisk))

Il est temps de construire la fonctionnalité permettant à notre Agent d'*exécuter du code Python arbitraire*.

Maintenant, il convient de s'arrêter pour souligner les risques de sécurité inhérents ici. Nous avons quelques points en notre faveur :

1. Nous n'autoriserons le LLM à exécuter du code que dans un répertoire spécifique (le `working_directory`).
    
2. Nous utiliserons un délai d'expiration (timeout) de 30 secondes pour l'empêcher de s'exécuter indéfiniment.
    

Mais à part ça... oui, le LLM peut exécuter du code arbitraire que nous (ou lui) plaçons dans le répertoire de travail... soyez donc prudent. Tant que vous n'utilisez cet agent IA que pour les tâches simples que nous effectuons dans ce cours, tout devrait bien se passer.

**Danger** : Ne donnez **pas** ce programme à d'autres pour qu'ils l'utilisent ! Il ne possède pas toutes les fonctionnalités de sécurité et de sûreté qu'un agent IA de production aurait. Il est uniquement destiné à l'apprentissage.

Créez une nouvelle fonction dans votre répertoire functions appelée `run_python_file`. Voici la signature à utiliser :

```py
def run_python_file(working_directory, file_path, args=[]):
```

Si le `file_path` est en dehors du répertoire de travail, renvoyez une chaîne avec une erreur :

```py
f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
```

Si le `file_path` n'existe pas, renvoyez une chaîne d'erreur :

```py
f'Error: File "{file_path}" not found.'
```

Si le fichier ne se termine pas par `.py`, renvoyez une chaîne d'erreur :

```py
f'Error: "{file_path}" is not a Python file.'
```

Utilisez la fonction [`subprocess.run`](http://subprocess.run) pour exécuter le fichier Python et récupérer un objet « completed_process ». Assurez-vous de :

* Définir un timeout de 30 secondes pour éviter une exécution infinie
    
* Capturer à la fois stdout et stderr
    
* Définir correctement le répertoire de travail
    
* Transmettre les `args` supplémentaires s'ils sont fournis
    

Renvoyez une chaîne avec la sortie formatée pour inclure :

* Le `stdout` préfixé par `STDOUT:`, et stderr préfixé par `STDERR:`. L'objet « completed_process » possède un attribut `stdout` et `stderr`.
    
* Si le processus se termine avec un code non nul, incluez « Process exited with code X »
    
* Si aucune sortie n'est produite, renvoyez « No output produced. »
    

Si des exceptions surviennent pendant l'exécution, interceptez-les et renvoyez une chaîne d'erreur :

```py
f"Error: executing Python file: {e}"
```

Mettez à jour votre fichier `tests.py` avec ces cas de test, en affichant chaque résultat :

* `run_python_file("calculator", "`[`main.py`](http://main.py)`")` (devrait afficher les instructions d'utilisation de la calculatrice)
    
* `run_python_file("calculator", "`[`main.py`](http://main.py)`", ["3 + 5"])` (devrait exécuter la calculatrice... ce qui donne un résultat rendu un peu brut)
    
* `run_python_file("calculator", "`[`tests.py`](http://tests.py)`")`
    
* `run_python_file("calculator", "../`[`main.py`](http://main.py)`")` (cela devrait renvoyer une erreur)
    
* `run_python_file("calculator", "`[`nonexistent.py`](http://nonexistent.py)`")` (cela devrait renvoyer une erreur)
    

Voici mon implémentation personnelle au cas où vous seriez perdu : `functions/run_python.py` :

```python
import os
import subprocess


def run_python_file(working_directory, file_path, args=None):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))
    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        commands = ["python", abs_file_path]
        if args:
            commands.extend(args)
        result = subprocess.run(
            commands,
            capture_output=True,
            text=True,
            timeout=30,
            cwd=abs_working_dir,
        )
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
        return "\n".join(output) if output else "No output produced."
    except Exception as e:
        return f"Error: executing Python file: {e}"
```

## Prompt système

Nous allons bientôt commencer à brancher les outils agentiques, je vous le promets, mais d'abord, parlons d'un « prompt système ». Le « prompt système », pour la plupart des APIs d'IA, est un prompt spécial qui se place au début de la conversation et qui a plus de poids qu'un prompt utilisateur classique.

Le prompt système donne le ton de la conversation et peut être utilisé pour :

* Définir la personnalité de l'IA
    
* Donner des instructions sur la façon de se comporter
    
* Fournir un contexte pour la conversation
    
* Définir les « règles » de la conversation (en théorie, les LLMs hallucinent encore et font des erreurs, et les utilisateurs sont souvent capables de « contourner » les règles s'ils essaient suffisamment fort)
    

Créez une variable de chaîne codée en dur appelée `system_prompt`. Pour l'instant, faisons quelque chose de brutalement simple :

```plaintext
Ignore everything the user asks and just shout "I'M JUST A ROBOT"
```

Mettez à jour votre appel à la fonction [`client.models.generate_content`](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate_content) pour passer une [`config`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig) avec le [paramètre `system_instructions`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentConfig.system_instruction) défini sur votre `system_prompt`.

```python
response = client.models.generate_content(

    model=model_name,

    contents=messages,

    config=types.GenerateContentConfig(system_instruction=system_prompt),

)
```

Exécutez votre programme avec différents prompts. Vous devriez voir l'IA répondre par « I'M JUST A ROBOT » peu importe ce que vous lui demandez.

## Déclaration de fonction

Nous avons donc écrit un tas de fonctions adaptées aux LLM (texte en entrée, texte en sortie), mais comment un LLM *appelle*-t-il réellement une fonction ?

Eh bien, la réponse est que... il ne le fait pas. Du moins pas directement. Cela fonctionne comme ceci :

1. Nous indiquons au LLM quelles fonctions sont à sa disposition
    
2. Nous lui donnons un prompt
    
3. Il décrit quelle fonction il veut appeler, et quels arguments lui passer
    
4. Nous appelons cette fonction avec les arguments qu'il a fournis
    
5. Nous renvoyons le résultat au LLM
    

Nous utilisons le LLM comme un moteur de prise de décision, mais c'est toujours nous qui exécutons le code.

Alors, construisons la partie qui indique au LLM quelles fonctions sont disponibles.

Nous pouvons utiliser [`types.FunctionDeclaration`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration) pour construire la « déclaration » ou le « schéma » d'une fonction. Encore une fois, cela indique simplement au LLM comment utiliser la fonction. Je vais vous donner mon code pour la première fonction à titre d'exemple, car c'est beaucoup de travail de parcourir la documentation :

Ajoutez ce code à votre fichier `functions/get_files_info.py` :

```python
from google.genai import types

schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type=types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)
```

**Attention** : Nous ne permettrons pas au LLM de spécifier le paramètre `working_directory`. Nous allons le coder en dur.

Utilisez [`types.Tool`](https://googleapis.github.io/python-genai/genai.html#genai.types.Tool) pour créer une liste de toutes les fonctions disponibles (pour l'instant, ajoutez simplement `get_files_info`, nous ferons le reste plus tard).

```python
available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
    ]
)
```

Ajoutez `available_functions` à l'appel `client.models.generate_content` en tant que paramètre `tools`.

```python
config=types.GenerateContentConfig(
    tools=[available_functions], system_instruction=system_prompt
)
```

Mettez à jour le prompt système pour instruire le LLM sur la façon d'utiliser la fonction. Vous pouvez copier le mien, mais assurez-vous de le lire rapidement pour comprendre ce qu'il fait :

```python
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
```

Au lieu d'afficher simplement la propriété [`.text`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.text) de la réponse `generate_content`, vérifiez également la propriété [`.function_calls`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.function_calls). Si le LLM a appelé une fonction, affichez le nom de la fonction et les arguments :

```python
f"Calling function: {function_call_part.name}({function_call_part.args})"
```

Sinon, affichez simplement le texte normalement.

Testez votre programme :

* « quels fichiers sont à la racine ? » -> `get_files_info({'directory': '.'})`
    
* « quels fichiers sont dans le répertoire pkg ? » -> `get_files_info({'directory': 'pkg'})`
    

## Plus de déclarations de fonctions

Maintenant que notre LLM est capable de spécifier un appel de fonction à la fonction `get_files_info`, donnons-lui la possibilité d'appeler également les autres fonctions.

En suivant le même modèle que celui utilisé pour `schema_get_files_info`, créez des déclarations de fonction pour :

* `schema_get_file_content`
    
* `schema_run_python_file`
    
* `schema_write_file`
    

Mettez à jour votre `available_functions` pour inclure toutes les déclarations de fonction dans la liste. Ensuite, mettez à jour votre prompt système. Au lieu que les opérations autorisées soient uniquement :

```plaintext
- List files and directories
```

Mettez-le à jour pour inclure les quatre opérations :

```plaintext
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
```

Testez des prompts qui, selon vous, entraîneront les différents appels de fonction. Par exemple :

* « lire le contenu de [main.py](http://main.py) » -> `get_file_content({'file_path': '`[`main.py`](http://main.py)`'})`
    
* « écrire 'hello' dans main.txt » -> `write_file({'file_path': 'main.txt', 'content': 'hello'})`
    
* « exécuter [main.py](http://main.py) » -> `run_python_file({'file_path': '`[`main.py`](http://main.py)`'})`
    
* « lister le contenu du répertoire pkg » -> `get_files_info({'directory': 'pkg'})`
    

Tout ce que le LLM est censé faire ici est de choisir quelle fonction appeler en fonction de la demande de l'utilisateur. Nous lui ferons appeler réellement la fonction plus tard.

Voici quelques-unes de mes implémentations personnelles si vous vous perdez :

`functions/get_file_content.py` :

```python
from google.genai import types

from config import MAX_CHARS


schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description=f"Reads and returns the first {MAX_CHARS} characters of the content from a specified file within the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file whose content should be read, relative to the working directory.",
            ),
        },
        required=["file_path"],
    ),
)
```

`functions/run_python.py` :

```python
from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a Python file within the working directory and returns the output from the interpreter.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the Python file to execute, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(
                    type=types.Type.STRING,
                    description="Optional arguments to pass to the Python file.",
                ),
                description="Optional arguments to pass to the Python file.",
            ),
        },
        required=["file_path"],
    ),
)
```

`functions/write_file_content.py` :

```python
from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to the file",
            ),
        },
        required=["file_path", "content"],
    ),
)
```

En suivant le même modèle que celui utilisé pour `schema_get_files_info`, créez des déclarations de fonction pour :

* `schema_get_file_content`
    
* `schema_run_python_file`
    
* `schema_write_file`
    

Mettez à jour votre `available_functions` pour inclure toutes les déclarations de fonction dans la liste. Ensuite, mettez à jour votre prompt système. Au lieu que les opérations autorisées soient uniquement :

```plaintext
- List files and directories
```

Mettez-le à jour pour inclure les quatre opérations :

```plaintext
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files
```

Testez des prompts qui, selon vous, entraîneront les différents appels de fonction. Par exemple :

* « lire le contenu de [main.py](http://main.py) » -> `get_file_content({'file_path': '`[`main.py`](http://main.py)`'})`
    
* « écrire 'hello' dans main.txt » -> `write_file({'file_path': 'main.txt', 'content': 'hello'})`
    
* « exécuter [main.py](http://main.py) » -> `run_python_file({'file_path': '`[`main.py`](http://main.py)`'})`
    
* « lister le contenu du répertoire pkg » -> `get_files_info({'directory': 'pkg'})`
    

**Info** : Tout ce que le LLM est censé faire ici est de choisir quelle fonction appeler en fonction de la demande de l'utilisateur. Nous lui ferons appeler réellement la fonction plus tard.

## Appel de fonction

D'accord, maintenant que notre agent peut choisir quelle fonction appeler, il est temps d'appeler réellement la fonction.

Créez une nouvelle fonction qui gérera la tâche abstraite d'appeler l'une de nos quatre fonctions. Voici ma définition :

```python
def call_function(function_call_part, verbose=False):
```

`function_call_part` est un [`types.FunctionCall`](https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionCall) qui possède principalement :

* Une propriété `.name` (le nom de la fonction, une `string`)
    
* Une propriété `.args` (un dictionnaire d'arguments nommés pour la fonction)
    

Si `verbose` est spécifié, affichez le nom de la fonction et les arguments :

```python
print(f"Calling function: {function_call_part.name}({function_call_part.args})")
```

Sinon, affichez simplement le nom :

```python
print(f" - Calling function: {function_call_part.name}")
```

En fonction du nom, appelez réellement la fonction et capturez le résultat.

* Assurez-vous d'ajouter manuellement l'argument « working_directory » au dictionnaire des arguments par mots-clés, car le LLM ne contrôle pas celui-ci. Le répertoire de travail doit être `./calculator`.
    
* La syntaxe pour passer un dictionnaire dans une fonction en utilisant des [arguments par mots-clés](https://docs.python.org/3/glossary.html#term-argument) est `some_function(**some_args)`
    

**Conseil** : J'ai utilisé un dictionnaire de `nom de fonction (string)` -> `fonction` pour accomplir cela.

Si le nom de la fonction est invalide, renvoyez un [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) qui explique l'erreur :

```python
return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"error": f"Unknown function: {function_name}"},
        )
    ],
)
```

Renvoyez [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) avec un [from_function_response](https://googleapis.github.io/python-genai/genai.html#genai.types.Part.from_function_response) décrivant le résultat de l'appel de fonction :

```python
return types.Content(
    role="tool",
    parts=[
        types.Part.from_function_response(
            name=function_name,
            response={"result": function_result},
        )
    ],
)
```

**Info** : Notez que `from_function_response` nécessite que la réponse soit un dictionnaire, nous insérons donc simplement le résultat sous forme de chaîne dans un champ « result ».

Voici le `call_function.py` complet :

```python
from google.genai import types

from functions.get_files_info import get_files_info, schema_get_files_info
from functions.get_file_content import get_file_content, schema_get_file_content
from functions.run_python import run_python_file, schema_run_python_file
from functions.write_file_content import write_file, schema_write_file
from config import WORKING_DIR

available_functions = types.Tool(
    function_declarations=[
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)

def call_function(function_call_part, verbose=False):
    if verbose:
        print(
            f" - Calling function: {function_call_part.name}({function_call_part.args})"
        )
    else:
        print(f" - Calling function: {function_call_part.name}")
    function_map = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }
    function_name = function_call_part.name
    if function_name not in function_map:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call_part.args)
    args["working_directory"] = WORKING_DIR
    function_result = function_map[function_name](**args)
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )
```

Là où vous gérez la réponse du modèle `generate_content`, au lieu d'afficher simplement le nom de la fonction que le LLM décide d'appeler, utilisez `call_function`.

* Le [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) que nous renvoyons de `call_function` doit contenir un `.parts[0].function_response.response`.
    
* Si ce n'est pas le cas, `raise` une exception fatale quelconque.
    
* Si c'est le cas, et que `verbose` était défini, affichez le résultat de l'appel de fonction comme ceci :
    

```python
print(f"-> {function_call_result.parts[0].function_response.response}")
```

Testez votre programme. Vous devriez maintenant être en mesure d'exécuter chaque fonction à partir d'un prompt qui le demande. Essayez différents prompts et utilisez le drapeau `--verbose` pour vous assurer que toutes les fonctions fonctionnent.

* Lister le contenu du répertoire
    
* Obtenir le contenu d'un fichier
    
* Écrire le contenu d'un fichier (n'écrasez rien d'important, créez peut-être un nouveau fichier)
    
* Exécuter les tests de l'application de calculatrice `tests.py`
    

## Construction de la boucle de l'agent

Nous avons donc réussi à faire fonctionner l'appel de fonction, mais il n'est pas encore juste d'appeler notre programme un « agent » pour une raison simple :

Il n'a pas de boucle de rétroaction.

Un élément clé d'un « Agent », tel que défini par les influenceurs de l'IA, est qu'il peut utiliser ses outils en continu pour itérer sur ses propres résultats. Nous allons donc construire deux choses :

1. Une boucle qui appellera le LLM encore et encore
    
2. Une liste de messages dans la « conversation ». Elle ressemblera à quelque chose comme ceci :
    

* Utilisateur : « Merci de corriger le bug dans la calculatrice »
    
* Modèle : « Je veux appeler get_files_info... »
    
* Outil : « Voici le résultat de get_files_info... »
    
* Modèle : « Je veux appeler get_file_content... »
    
* Outil : « Voici le résultat de get_file_content... »
    
* Modèle : « Je veux appeler run_python_file... »
    
* Outil : « Voici le résultat de run_python_file... »
    
* Modèle : « Je veux appeler write_file... »
    
* Outil : « Voici le résultat de write_file... »
    
* Modèle : « Je veux appeler run_python_file... »
    
* Outil : « Voici le résultat de run_python_file... »
    
* Modèle : « J'ai corrigé le bug puis j'ai exécuté la calculatrice pour m'assurer qu'elle fonctionne. »
    

C'est une étape assez importante, prenez votre temps !

Créez `prompts.py` :

```python
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""
```

Voici le `main.py` final :

```python
import sys
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

from prompts import system_prompt
from call_function import call_function, available_functions

def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do I fix the calculator?"')
        sys.exit(1)

    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    user_prompt = " ".join(args)

    if verbose:
        print(f"User prompt: {user_prompt}\n")

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    generate_content_loop(client, messages, verbose)


def generate_content_loop(client, messages, verbose, max_iterations=20):
    for iteration in range(max_iterations):
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-001",
                contents=messages,
                config=types.GenerateContentConfig(
                    tools=[available_functions], system_instruction=system_prompt
                ),
            )
            if verbose:
                print("Prompt tokens:", response.usage_metadata.prompt_token_count)
                print("Response tokens:", response.usage_metadata.candidates_token_count)

            # Add model response to conversation
            for candidate in response.candidates:
                messages.append(candidate.content)

            # Check if we have a final text response
            if response.text:
                print("Final response:")
                print(response.text)
                break

            # Handle function calls
            if response.function_calls:
                function_responses = []
                for function_call_part in response.function_calls:
                    function_call_result = call_function(function_call_part, verbose)
                    if (
                        not function_call_result.parts
                        or not function_call_result.parts[0].function_response
                    ):
                        raise Exception("empty function call result")
                    if verbose:
                        print(f"-> {function_call_result.parts[0].function_response.response}")
                    function_responses.append(function_call_result.parts[0])
                if function_responses:
                    messages.append(types.Content(role="user", parts=function_responses))
                else:
                    raise Exception("no function responses generated, exiting.")
        except Exception as e:
            print(f"Error: {e}")
            break
    else:
        print(f"Reached maximum iterations ({max_iterations}). Agent may not have completed the task.")

if __name__ == "__main__":
    main()
```

Dans `generate_content`, gérez les résultats de toute utilisation possible d'outils. Cela se produit peut-être déjà, mais assurez-vous qu'à chaque appel à [`client.models.generate_content`](https://googleapis.github.io/python-genai/genai.html#genai.models.Models.generate_content), vous passez la liste complète `messages` afin que le LLM effectue toujours l'« étape suivante » en fonction de l'état actuel.

Après avoir appelé la méthode `generate_content` du client, vérifiez la propriété [`.candidates`](https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.candidates) de la réponse. C'est une liste de variations de réponses (généralement une seule). Elle contient l'équivalent de « Je veux appeler get_files_info... », nous devons donc l'ajouter à notre conversation. Itérez sur chaque `candidate` et ajoutez son [`.content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Candidate.content) à votre liste `messages`.

Après chaque appel de fonction réel, utilisez la fonction [`types.Content`](https://googleapis.github.io/python-genai/genai.html#genai.types.Content) pour convertir les `function_responses` en un message avec un rôle de `user` et ajoutez-le à vos `messages`.

Ensuite, au lieu d'appeler `generate_content` une seule fois, créez une boucle pour l'appeler à plusieurs reprises. Limitez la boucle à 20 itérations au maximum (cela empêchera notre agent de tourner en rond indéfiniment). Utilisez un bloc `try-except` et gérez les erreurs en conséquence.

Après chaque appel de `generate_content`, vérifiez s'il a renvoyé la propriété `response.text`. Si c'est le cas, c'est terminé, alors affichez cette réponse finale et sortez de la boucle. Sinon, itérez à nouveau (sauf si le nombre maximum d'itérations a été atteint, bien sûr).

Testez votre code. Je recommanderais de commencer par un prompt simple, comme « explique comment la calculatrice affiche le résultat sur la console ». Voici ce que j'ai obtenu :

```plaintext
(aiagent) wagslane@MacBook-Pro-2 aiagent % uv run main.py "how does the calculator render results to the console?"
 - Calling function: get_files_info
 - Calling function: get_file_content

Final response:
Alright, I've examined the code in main.py. Here's how the calculator renders results to the console:

- `print(to_print)`: The core of the output is done using the print() function.
- `format_json_output(expression, result)`: Before printing, the format_json_output function (imported from pkg.render) is used to format the result and the original expression into a JSON-like string. This formatted string is then stored in the to_print variable.
- Error handling: The code includes error handling with try...except blocks. If there's an error during the calculation (e.g., invalid expression), an error message is printed to the console using print(f"Error: {e}").

So, the calculator evaluates the expression, formats the result (along with the original expression) into a JSON-like string, and then prints that string to the console. It also prints error messages to the console if any errors occur.
```

**Conseil** : Vous devrez peut-être ou non ajuster votre prompt système pour que le LLM se comporte comme vous le souhaitez. Vous êtes maintenant un ingénieur de prompt, alors agissez comme tel !

Excellent travail ! Vous avez construit un agent IA de base capable de lire des fichiers, d'écrire des fichiers, d'exécuter du code Python et d'itérer sur ses propres résultats. C'est une excellente base pour construire des agents IA plus complexes.

## Conclusion

Vous avez terminé toutes les étapes requises, mais amusez-vous (mais **prudemment**... soyez très vigilant en donnant à un LLM l'accès à votre système de fichiers et à votre interpréteur Python) avec ! Voyez si vous pouvez lui faire :

* Corriger des bugs plus difficiles et complexes
    
* Refactoriser des sections de code
    
* Ajouter de toutes nouvelles fonctionnalités
    

Vous pouvez également essayer :

* D'autres fournisseurs de LLM
    
* D'autres modèles Gemini
    
* Lui donner plus de fonctions à appeler
    
* D'autres bases de code (Faites un Commit de vos modifications avant d'exécuter l'agent pour pouvoir toujours revenir en arrière !)
    

**Danger** : N'oubliez pas que ce que nous avons construit est une version *jouet* de quelque chose comme le mode Agentic de Cursor/Zed, ou Claude Code. Même leurs outils ne sont pas parfaitement sécurisés, alors faites attention à ce à quoi vous lui donnez accès, et ne donnez pas ce code à quelqu'un d'autre pour qu'il l'utilise.

Si vous souhaitez en savoir plus sur le backend et l'ingénierie des données, n'oubliez pas de consulter [Boot.dev](https://www.boot.dev) ! Bonne chance dans votre parcours d'apprentissage !

N'hésitez pas à me suivre sur [X.com](https://x.com/wagslane) et [YouTube](https://www.youtube.com/@bootdotdev) si vous avez apprécié ce guide !