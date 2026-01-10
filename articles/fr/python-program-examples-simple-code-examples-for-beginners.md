---
title: Exemples de programmes Python – Exemples de code simples pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-17T17:09:25.000Z'
originalURL: https://freecodecamp.org/news/python-program-examples-simple-code-examples-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/python-program-examples-image.png
tags:
- name: beginner
  slug: beginner
- name: beginners guide
  slug: beginners-guide
- name: Python
  slug: python
seo_title: Exemples de programmes Python – Exemples de code simples pour débutants
seo_desc: 'By Shittu Olumide

  Mark Twain said that the secret of getting ahead is getting started. Programming
  can seem daunting for beginners, but the best way to get started is to dive right
  in and start writing code.

  Simple code examples are a great way for b...'
---

Par Shittu Olumide

Mark Twain a dit que le secret pour prendre de l'avance est de commencer. La programmation peut sembler intimidante pour les débutants, mais la meilleure façon de se lancer est de plonger directement et de commencer à écrire du code.

Les exemples de code simples sont un excellent moyen pour les débutants de se familiariser et d'apprendre les bases de la programmation. Dans cet article, je vais fournir une série d'exemples de code simples qui sont parfaits pour les débutants en Python.

Ces exemples couvrent un éventail de concepts de programmation et vous aideront à développer une base solide. Que vous soyez nouveau dans la programmation ou que vous cherchiez simplement à rafraîchir vos compétences, ces exemples de code vous aideront à démarrer votre voyage dans le codage.

Si vous avez besoin d'apprendre quelques bases de Python, j'ai ajouté des ressources utiles à la fin de ce tutoriel.

## Comment créer un jeu de devinette de nombre en Python

Dans ce projet, vous allez créer un jeu simple de devinette de nombre qui permet à l'utilisateur de deviner un nombre aléatoire entre 1 et 100. Le programme donnera des indices à l'utilisateur après chaque tentative, indiquant si sa proposition était trop haute ou trop basse, jusqu'à ce que l'utilisateur devine le nombre correct.

**Code** :

```py
import random

secret_number = random.randint(1, 100)

while True:
    guess = int(input("Devinez le nombre entre 1 et 100 : "))
    
    if guess == secret_number:
        print("Félicitations ! Vous avez deviné le nombre !")
        break
    elif guess < secret_number:
        print("Trop bas ! Réessayez.")
    else:
        print("Trop haut ! Réessayez.")

```

**Explication** :

* Commencez par importer le module `random`, qui vous permettra de générer un nombre aléatoire.
* Générez un nombre aléatoire entre 1 et 100 à l'aide de la fonction `randint()` du module `random`, et affectez-le à une variable.
* Créez une boucle qui permet à l'utilisateur de deviner le nombre jusqu'à ce qu'il devine correctement. À l'intérieur de la boucle, invitez l'utilisateur à saisir sa proposition à l'aide de la fonction `input()`, et convertissez sa saisie en un entier à l'aide de la fonction `int()`.
* Ajoutez une instruction conditionnelle à l'intérieur de la boucle qui vérifie si la proposition de l'utilisateur est correcte, trop haute ou trop basse. Si la proposition est correcte, affichez un message de félicitations et sortez de la boucle. Si la proposition est trop haute ou trop basse, affichez un message d'indice pour aider l'utilisateur à deviner le nombre correctement.
* Lancez le programme et jouez au jeu de devinette de nombre !

## Comment créer un générateur de mots de passe simple en Python

Un générateur de mots de passe, comme son nom l'indique, génère un mot de passe aléatoire d'une longueur particulière en utilisant différentes combinaisons de caractères et de caractères spéciaux.

**Code** :

```py
import random
import string

def generate_password(length):
    """Cette fonction génère un mot de passe aléatoire
    d'une longueur donnée en utilisant une combinaison de
    lettres majuscules, de lettres minuscules,
    de chiffres et de caractères spéciaux"""
    
    # Définir une chaîne contenant tous les caractères possibles
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Générer un mot de passe à l'aide d'une sélection aléatoire de caractères
    password = "".join(random.choice(all_chars) for i in range(length))
    
    return password

# Tester la fonction en générant un mot de passe de longueur 10
password = generate_password(10)
print(password)

```

**Explication** :

* Nous importons les modules `random` et `string` que nous utilisons respectivement pour générer des valeurs aléatoires et travailler avec des chaînes de caractères.
* Ensuite, nous définissons une fonction appelée `generate_password` qui prend un seul paramètre `length`, lequel spécifie la longueur du mot de passe à générer.
* À l'intérieur de la fonction, nous définissons une chaîne appelée `all_chars` qui contient tous les caractères possibles pouvant être utilisés pour générer le mot de passe. Nous utilisons les constantes `string.ascii_letters`, `string.digits` et `string.punctuation` pour créer cette chaîne.
* Nous utilisons ensuite une compréhension de liste pour générer une liste de `length` caractères aléatoires à partir de la chaîne `all_chars` en utilisant la fonction `random.choice()`. Enfin, nous joignons ces caractères ensemble en une seule chaîne à l'aide de la fonction `"".join()` et renvoyons le résultat.
* Pour tester la fonction, nous l'appelons avec un argument de 10 pour générer un mot de passe de longueur 10 et affichons le résultat.

Notez qu'il s'agit d'un générateur de mots de passe très simple qui peut ne pas convenir à une utilisation dans des scénarios réels où la sécurité est une préoccupation.

## Comment créer un vérificateur de mot de passe en Python

Nous allons construire un vérificateur de mot de passe dans cette section. Son rôle est de vérifier si un mot de passe est assez fort en fonction de certains critères que nous avons définis. Il affichera une erreur si l'un des critères du mot de passe n'est pas rempli.

**Code** :

```py
# Définir une fonction pour vérifier si le mot de passe est assez fort
def password_checker(password):
    # Définir les critères pour un mot de passe fort
    min_length = 8
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special_char = False
    special_chars = "!@#$%^&*()-_=+[{]}\\|;:',<.>/?"
    
    # Vérifier la longueur du mot de passe
    if len(password) < min_length:
        print("Le mot de passe est trop court !")
        return False
    
    # Vérifier si le mot de passe contient une majuscule, une minuscule, un chiffre et un caractère spécial
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        elif char in special_chars:
            has_special_char = True
    
    # Afficher un message d'erreur pour chaque critère manquant
    if not has_uppercase:
        print("Le mot de passe doit contenir au moins une lettre majuscule !")
        return False
    if not has_lowercase:
        print("Le mot de passe doit contenir au moins une lettre minuscule !")
        return False
    if not has_digit:
        print("Le mot de passe doit contenir au moins un chiffre !")
        return False
    if not has_special_char:
        print("Le mot de passe doit contenir au moins un caractère spécial !")
        return False
    
    # Si tous les critères sont remplis, afficher un message de succès
    print("Le mot de passe est fort !")
    return True

# Inviter l'utilisateur à saisir un mot de passe et vérifier s'il répond aux critères
password = input("Entrez un mot de passe : ")
password_checker(password)

```

**Explication** :

* Dans ce code, nous définissons une fonction appelée `password_checker()` qui prend un mot de passe en argument et vérifie s'il répond à certains critères de force.
* Nous définissons d'abord les critères d'un mot de passe fort – une longueur minimale de 8 caractères, au moins une lettre majuscule, une lettre minuscule, un chiffre et un caractère spécial.
* Nous vérifions ensuite la longueur du mot de passe et s'il contient les types de caractères requis à l'aide d'une boucle for qui parcourt chaque caractère du mot de passe.
* Si le mot de passe ne répond à aucun des critères, nous affichons un message d'erreur et renvoyons `False` pour indiquer que le mot de passe n'est pas assez fort. Sinon, nous affichons un message de succès et renvoyons `True`.
* Enfin, nous invitons l'utilisateur à saisir un mot de passe à l'aide de la fonction `input()` et le passons à la fonction `password_checker()` pour vérifier s'il répond aux critères.

## Comment créer un web scraper en Python

Un web scraper extrait/récupère des données de pages web et les sauvegarde dans le format de notre choix, soit .csv soit .txt. Nous allons construire un web scraper simple dans cette section en utilisant une bibliothèque Python appelée Beautiful Soup.

**Code** :

```py
import requests
from bs4 import BeautifulSoup

# Définir l'URL de la page web que vous souhaitez scraper
url = 'https://www.example.com'

# Envoyer une requête HTTP à l'URL et récupérer le contenu HTML
response = requests.get(url)

# Créer un objet BeautifulSoup qui analyse le contenu HTML
soup = BeautifulSoup(response.content, 'html.parser')

# Trouver tous les liens sur la page web
links = soup.find_all('a')

# Afficher le texte et l'attribut href de chaque lien
for link in links:
    print(link.get('href'), link.text)

```

**Explication** :

* Dans ce code, nous importons d'abord les modules `requests` et `BeautifulSoup` qui sont utilisés respectivement pour effectuer des requêtes HTTP et analyser le contenu HTML.
* Ensuite, nous définissons l'URL de la page web que nous voulons scraper dans une variable appelée `url`.
* Nous utilisons ensuite la fonction `requests.get()` pour envoyer une requête HTTP GET à l'URL et récupérer le contenu HTML de la page web en tant que réponse.
* Nous créons un objet `BeautifulSoup` appelé `soup` qui analyse le contenu HTML de la réponse à l'aide de l'analyseur `html.parser`.
* Nous utilisons ensuite la méthode `soup.find_all()` pour trouver tous les liens sur la page web et les stocker dans une variable appelée `links`.
* Enfin, nous utilisons une boucle for pour parcourir chaque lien dans `links` et afficher le texte et l'attribut href de chaque lien à l'aide de la méthode `link.get()`.

## Comment créer un convertisseur de devises en Python

Un convertisseur de devises est un programme qui aide les utilisateurs à convertir la valeur d'une devise dans une autre devise. Vous pouvez l'utiliser à diverses fins, telles que le calcul du coût d'achats internationaux, l'estimation des frais de voyage ou l'analyse de données financières.

Note : nous utiliserons l'ExchangeRate-API pour obtenir les données de taux de change, qui est une API gratuite et open-source pour les taux de change. Mais il existe d'autres API disponibles qui peuvent avoir des limites d'utilisation ou des exigences différentes.

**Code** :

```py
# Importer les modules nécessaires
import requests

# Définir une fonction pour convertir les devises
def currency_converter(amount, from_currency, to_currency):
    # Définir le point de terminaison de l'API pour la conversion de devises
    api_endpoint = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
    
    # Envoyer une requête GET au point de terminaison de l'API
    response = requests.get(api_endpoint)
    
    # Récupérer les données JSON de la réponse
    data = response.json()
    
    # Extraire le taux de change pour la devise cible
    exchange_rate = data["rates"][to_currency]
    
    # Calculer le montant converti
    converted_amount = amount * exchange_rate
    
    # Renvoyer le montant converti
    return converted_amount

# Inviter l'utilisateur à saisir le montant, la devise source et la devise cible
amount = float(input("Entrez le montant : "))
from_currency = input("Entrez le code de la devise source : ").upper()
to_currency = input("Entrez le code de la devise cible : ").upper()

# Convertir la devise et afficher le résultat
result = currency_converter(amount, from_currency, to_currency)
print(f"{amount} {from_currency} est égal à {result} {to_currency}")

```

**Explication** :

* Dans ce code, nous définissons une fonction appelée `currency_converter()` qui prend un montant, un code de devise source et un code de devise cible comme arguments et renvoie le montant converti.
* Nous définissons d'abord le point de terminaison de l'API pour la conversion de devises en utilisant le paramètre `from_currency` et le module `requests` pour envoyer une requête GET au point de terminaison.
* Nous extrayons ensuite le taux de change pour la devise cible à partir des données JSON renvoyées par l'API à l'aide du paramètre `to_currency` et calculons le montant converti en multipliant le taux de change par le paramètre `amount`.
* Enfin, nous invitons l'utilisateur à saisir le `amount`, la `from_currency` et la `to_currency` à l'aide de la fonction `input()` et les passons à la fonction `currency_converter()` pour convertir la devise. Le montant converti est ensuite affiché en utilisant le formatage de chaîne.

## Conclusion

Tous ces projets sont très simples et faciles à réaliser. Si vous voulez vraiment améliorer vos compétences en Python, je vous conseille de prendre le code, de le modifier, de l'éditer et de construire à partir de celui-ci. Vous pouvez transformer bon nombre de ces projets simples en applications beaucoup plus complexes si vous le souhaitez.

Si vous avez besoin d'apprendre quelques bases de Python, consultez ces ressources utiles :

* [Comment construire votre premier projet Python – cours YouTube](https://www.youtube.com/watch?v=_ZqAVck-WeM)
* [Python pour tout le monde – cours universitaire complet du Dr. Chuck](https://www.youtube.com/watch?v=8DvywoWv6fI)
* [Apprendre Python pour les débutants – cours gratuits](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/)
* Les certifications de freeCodeCamp [Informatique scientifique avec Python](https://www.freecodecamp.org/learn/scientific-computing-with-python/) et [Analyse de données avec Python](https://www.freecodecamp.org/learn/data-analysis-with-python/)

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.linkedin.com/in/olumide-shittu). Vous pouvez également vous abonner à ma chaîne [YouTube](https://www.youtube.com/channel/UCNhFxpk6hGt5uMCKXq0Jl8A).

Bon codage !