---
title: Comment créer une interface graphique de convertisseur de devises avec Tkinter
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-04-10T16:44:45.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-currency-converter-gui-with-tkinter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/currency-converter.png
tags:
- name: Python
  slug: python
seo_title: Comment créer une interface graphique de convertisseur de devises avec
  Tkinter
seo_desc: "Tkinter is a built-in Python library for creating graphical user interfaces\
  \ (GUIs). It provides a set of tools for building windows, frames, buttons, textboxes,\
  \ and other GUI elements. \nIt is easy to use and widely available, making it a\
  \ popular choi..."
---

Tkinter est une bibliothèque Python intégrée pour créer des interfaces graphiques (GUI). Elle fournit un ensemble d'outils pour construire des fenêtres, des cadres, des boutons, des zones de texte et d'autres éléments d'interface graphique. 

Elle est facile à utiliser et largement disponible, ce qui en fait un choix populaire pour construire des applications GUI en Python. Elle est également hautement personnalisable, permettant aux développeurs de créer des interfaces utilisateur uniques et visuellement attrayantes.

Dans ce tutoriel, vous allez construire une application GUI de convertisseur de devises en utilisant Tkinter. Avant de plonger dans le tutoriel, il est bon de noter que ce n'est pas la première fois que nous construisons une application GUI avec Tkinter. Dans un tutoriel précédent, nous avons construit une [Application de Quiz GUI utilisant Tkinter](https://blog.ashutoshkrris.in/how-to-build-a-gui-quiz-application-using-tkinter-and-open-trivia-db), et dans une autre série de tutoriels, nous avons construit un [Gestionnaire de Mots de Passe](https://blog.ashutoshkrris.in/password-generator-using-python-and-tkinter-part-i). Je vous encourage à consulter ces tutoriels également.

Voici à quoi ressemblera votre résultat final :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Converter.gif)

Vous pouvez trouver le code du tutoriel dans [ce dépôt](https://github.com/ashutoshkrris/currency-converter-gui).

## Prérequis

Pour suivre ce tutoriel et construire l'application, vous devez avoir les éléments suivants :

* Connaissance de base du langage de programmation Python
* Python 3.8+ installé sur votre système
* Familiarité avec les bibliothèques [Tkinter](https://docs.python.org/3/library/tkinter.html) et [Requests](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)

## Comment configurer votre environnement virtuel

Avant de commencer à coder, vous devez vous assurer que vous avez tous les outils et bibliothèques nécessaires installés. Pour garantir que vous avez un environnement propre et isolé, vous allez créer un environnement virtuel en utilisant `venv`.

Créez un répertoire de projet et naviguez jusqu'à celui-ci dans le terminal :

```bash
mkdir currency-converter
cd currency-converter
```

Créez un environnement virtuel nommé `env` en utilisant la commande suivante :

```bash
python -m venv env
```

Python est maintenant livré avec la bibliothèque `venv` préinstallée pour créer des environnements virtuels.

Activez l'environnement virtuel comme suit :

```bash
source env/bin/activate
```

Note : si vous êtes sur Windows, vous devrez utiliser `source env/Scripts/activate` pour activer l'environnement.

Vous devriez voir `(env)` dans votre prompt de terminal, indiquant que l'environnement virtuel a été activé.

### Comment installer les bibliothèques

Maintenant que vous avez créé l'environnement virtuel, vous pouvez installer les bibliothèques suivantes :

* `requests` : La bibliothèque vous aide à envoyer des requêtes sur les points de terminaison de l'API.
* `python-decouple` : La bibliothèque vous aide à lire les valeurs des variables d'environnement.
* `pillow` : La bibliothèque ajoute des capacités de traitement d'image à votre interpréteur Python.

Pour installer les bibliothèques, exécutez la commande suivante :

```bash
pip install requests python-decouple pillow
```

## Comment construire les fonctions utilitaires du convertisseur de devises

Dans cette section, vous allez commencer à construire la fonctionnalité principale de notre interface graphique de convertisseur de devises. Vous allez créer deux fonctions utilitaires qui seront utilisées pour convertir les devises et récupérer les codes de devises à partir d'un fichier JSON.

Pour définir les fonctions utilitaires, vous allez créer un nouveau fichier appelé `utils.py` dans le projet. Ce fichier contiendra toutes vos fonctions utilitaires pour l'interface graphique du convertisseur de devises.

### Fonction utilitaire pour obtenir les codes de devises à partir du fichier JSON

Cette fonction utilitaire récupérera les codes de devises à partir d'un fichier JSON. Cette fonction vous permettra de remplir l'interface graphique avec une liste de devises disponibles que l'utilisateur peut sélectionner.

Créez un fichier `currency.json` qui inclut le code de devise et le nom de diverses devises. Le fichier JSON a la structure suivante :

```json
[
  { "AED": "Dirham des Émirats arabes unis" },
  { "AFN": "Afghani afghan" },
  { "ALL": "Lek albanais" },
  ...
]
```

Vous pouvez obtenir le contenu du fichier `currency.json` à partir de [ce lien](https://github.com/ashutoshkrris/currency-converter-gui/blob/main/currency.json) et le copier dans le fichier `currency.json` de votre projet.

Ajoutez le code suivant pour définir la première fonction utilitaire :

```python
import json

def get_currencies() -> list:
    currency_codes = []
    with open('currency.json') as f:
        currency_data = json.load(f)
        for currency in currency_data:
            code, _ = list(currency.items())[0]
            currency_codes.append(code)
    return sorted(currency_codes)
```

Dans le code ci-dessus, vous définissez une fonction `get_currencies()` qui retourne une liste de codes de devises. À l'intérieur de la fonction, vous créez une liste vide appelée `currency_codes` que vous utiliserez pour stocker les codes de devises. Ensuite, vous ouvrez le fichier `currency.json` en mode lecture et utilisez la méthode `json.load()` pour charger le contenu du fichier dans un dictionnaire Python appelé `currency_data`.

Ensuite, vous parcourez chaque élément du dictionnaire `currency_data` en utilisant une boucle `for`. Chaque élément du dictionnaire `currency_data` est lui-même un dictionnaire, avec une seule paire clé-valeur représentant un code de devise et son nom. À l'intérieur de la boucle `for`, vous utilisez la fonction `list()` pour convertir la paire clé-valeur de chaque devise en une liste. 

Puisque chaque dictionnaire ne contient qu'une seule paire clé-valeur, nous pouvons utiliser la méthode `items()` pour convertir le dictionnaire en une liste de tuples contenant les paires clé-valeur.

Vous utilisez ensuite le [déballage de tuple](https://blog.ashutoshkrris.in/mastering-list-destructuring-and-packing-in-python-a-comprehensive-guide) pour assigner le premier élément de la liste à la variable `code` et ignorer le deuxième élément en utilisant `_`. 

Enfin, vous ajoutez la variable `code`, représentant le code de devise, à la liste `currency_codes`. Après avoir parcouru toutes les devises dans `currency_data`, vous triez la liste `currency_codes` par ordre croissant en utilisant la fonction `sorted()` et la retournez depuis la fonction.

Si vous appelez la fonction et affichez son résultat, vous obtiendrez la sortie suivante :

```bash
['ADA', 'AED', 'AFN', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AVAX', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BHD', 'BIF', 'BMD', 'BNB', 'BND', 'BOB', 'BRL', 'BSD', 'BTC', 'BTN', 'BWP', 'BYN', 'BYR', 'BZD', 'CAD', 'CDF', 'CHF', 'CLF', 'CLP', 'CNY', 'COP', 'CRC', 'CUC', 'CUP', 'CVE', 'CZK', 'DJF', 'DKK', 'DOP', 'DOT', 'DZD', 'EGP', 'ERN', 'ETB', 'ETH', 'EUR', 'FJD', 'FKP', 'GBP', 'GEL', 'GGP', 'GHS', 'GIP', 'GMD', 'GNF', 'GTQ', 'GYD', 'HKD', 'HNL', 'HRK', 'HTG', 'HUF', 'IDR', 'ILS', 'IMP', 'INR', 'IQD', 'IRR', 'ISK', 'JEP', 'JMD', 'JOD', 'JPY', 'KES', 'KGS', 'KHR', 'KMF', 'KPW', 'KRW', 'KWD', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'LTC', 'LTL', 'LVL', 'LYD', 'MAD', 'MATIC', 'MDL', 'MGA', 'MKD', 'MMK', 'MNT', 'MOP', 'MRO', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NOK', 'NPR', 'NZD', 'OMR', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'PYG', 'QAR', 'RON', 'RSD', 'RUB', 'RWF', 'SAR', 'SBD', 'SCR', 'SDG', 'SEK', 'SGD', 'SHP', 'SLL', 'SOL', 'SOS', 'SRD', 'STD', 'SVC', 'SYP', 'SZL', 'THB', 'TJS', 'TMT', 'TND', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UGX', 'USD', 'UYU', 'UZS', 'VEF', 'VND', 'VUV', 'WST', 'XAF', 'XAG', 'XAU', 'XCD', 'XDR', 'XOF', 'XPF', 'XRP', 'YER', 'ZAR', 'ZMK', 'ZMW', 'ZWL']
```

### Fonction utilitaire pour convertir les devises

Pour construire le convertisseur de devises, vous avez besoin d'une fonction utilitaire qui peut convertir une devise en une autre. À cette fin, vous allez utiliser une API externe pour récupérer la dernière valeur de change de devises. Bien qu'il existe de nombreuses API de change de devises disponibles telles que [API Forex](https://api.forex/), [Forex API](https://fxapi.com/), etc., vous allez utiliser l'[API de Conversion de Devises](https://currencyapi.com/). 

Vous pouvez intégrer l'API dans votre code soit en utilisant le module `requests`, soit sa propre bibliothèque `[currencyapi-python](https://github.com/everapihq/currencyapi-python)`. Comme déjà mentionné, vous allez utiliser le module `requests` dans ce tutoriel.

Pour utiliser l'API, vous devrez vous inscrire pour obtenir une clé API. Vous pouvez vous inscrire pour un compte gratuit à l'adresse [https://app.currencyapi.com/register](https://app.currencyapi.com/register). Une fois inscrit, vous pouvez trouver votre clé API (surlignée en noir) sur la page du tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-140705.png)

Créez un fichier `.env` et ajoutez le code suivant pour définir la variable d'environnement :

```
export API_KEY='votre-cle-api-ici'
```

Copiez votre clé API depuis le tableau de bord et remplacez `votre-cle-api-ici` dans le fichier ci-dessus. Ensuite, exécutez la commande suivante pour définir les variables d'environnement :

```bash
source .env
```

Vous utilisez ensuite la bibliothèque `python-decouple` pour lire les valeurs de la clé API dans le code Python. 

Ensuite, dans le même fichier `utils.py`, ajoutez le code suivant :

```python
import requests
from decouple import config


API_KEY = config('API_KEY')
API_ENDPOINT = 'https://api.currencyapi.com/v3/latest'

def convert_currency(from_currency: str, to_currency: str, amount: float) -> float:
    query_params = {
        'apikey': API_KEY,
        'base_currency': from_currency,
        'currencies': to_currency
    }
    response = requests.get(API_ENDPOINT, params=query_params)
    currency_data = response.json()
    exchange_rate = currency_data['data'][to_currency]['value']
    exchanged_value = exchange_rate * amount
    return exchanged_value
```

La fonction `convert_currency` prend trois arguments : `from_currency`, `to_currency`, et `amount`. `from_currency` et `to_currency` sont les codes de devise ISO pour les devises à convertir et `amount` est le montant de la devise `from_currency` que vous souhaitez convertir.

La fonction envoie une requête GET à l'URL `API_ENDPOINT` avec la `API_KEY`, `from_currency`, et `to_currency` comme paramètres de requête. La fonction `requests.get()` du module `requests` est utilisée pour envoyer la requête et l'argument `params` est utilisé pour passer les paramètres de requête.

Une fois la réponse reçue, nous la convertissons en un dictionnaire Python en utilisant la méthode `json()` de l'objet `response`. Une réponse réussie ressemble à ceci :

```json
{
  "meta":{
    "last_updated_at":"2023-03-30T23:59:59Z"
  },
  "data":{
    "INR":{
      "code":"INR",
      "value":82.100841
    }
  }
}
```

Vous extrayez ensuite le taux de change du dictionnaire de réponse et calculez la valeur échangée en utilisant le `amount` et le `exchange_rate`. Enfin, vous retournez la valeur échangée.

## Comment concevoir l'interface graphique du convertisseur de devises avec Tkinter

Maintenant que vous avez les fonctions utilitaires prêtes, vous pouvez concevoir l'interface graphique en utilisant Tkinter. Voici à quoi ressemblera l'application :

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-31-203154.png)

La conception inclut une fenêtre de 300 X 320 pixels avec un cadre supérieur et un cadre principal. Le cadre supérieur contient l'icône et le titre de l'application. Le cadre principal inclut des étiquettes, des boîtes de combinaison, un widget d'entrée et un bouton pour la conversion de devises.

Construisons l'application étape par étape. Créez un fichier `main.py` dans le répertoire du projet. Tout d'abord, importez les modules et fonctions nécessaires, ainsi que définissez quelques constantes de couleur.

```python
from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

from utils import convert_currency, get_currencies

# Couleurs
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#333333"
BLUE_COLOR = "#0000FF"
```

### Comment créer la fenêtre

Lors de la création d'une application GUI avec Tkinter, la première étape consiste à créer une fenêtre avec une taille et un titre spécifiques. Dans ce cas, la taille de la fenêtre doit être définie sur 300x320 et le titre doit être "Convertisseur de devises". Par défaut, la couleur de fond de la fenêtre est blanche et elle ne doit pas être redimensionnable. Voici le code :

```python
# Configuration de la fenêtre
window = Tk()
window.geometry("300x320")
window.title("Convertisseur de devises")
window.configure(bg=WHITE_COLOR)
window.resizable(height=FALSE, width=FALSE)
```

### Comment créer les cadres

Comme mentionné précédemment, vous devez créer deux cadres - un cadre supérieur et un cadre principal. Le cadre supérieur contiendra l'icône et le titre de l'application, tandis que le cadre principal inclura des widgets essentiels tels que des étiquettes, des widgets d'entrée, des boîtes de combinaison et le bouton de conversion. Le code suivant accomplit cela :

```python
# Créer les cadres supérieur et principal
top_frame = Frame(window, width=300, height=60, bg=BLUE_COLOR)
top_frame.grid(row=0, column=0)

main_frame = Frame(window, width=300, height=260, bg=WHITE_COLOR)
main_frame.grid(row=1, column=0)

```

Ici, la fonction `Frame()` est utilisée pour créer les deux cadres. Le premier argument est la fenêtre parente (qui est `window` dans ce cas), suivi de la largeur, de la hauteur et de la couleur de fond des cadres. Vous pouvez ensuite utiliser la méthode `grid()` pour placer les cadres dans la fenêtre en spécifiant leurs positions de ligne et de colonne.

Vous placez le widget `top_frame` dans la première ligne et la première colonne de la grille, tandis que le widget `main_frame` dans la deuxième ligne et la première colonne de la grille.

### Comment ajouter des widgets dans le cadre supérieur

Ensuite, vous pouvez créer les widgets qui appartiennent au cadre supérieur. Le cadre supérieur doit avoir une icône d'application et un titre d'application, comme mentionné précédemment. Vous pouvez obtenir une icône à partir de [Icons8](https://icons8.com/icons/set/exchange) (ou à partir de [ici](https://github.com/ashutoshkrris/currency-converter-gui/blob/main/icon.png)) et l'enregistrer dans votre répertoire de projet sous le nom `icon.png`.

```python
# Widgets du cadre supérieur
icon_image = Image.open('icon.png')
icon_image = icon_image.resize((40, 40))
icon_image = ImageTk.PhotoImage(icon_image)
app_name_label = Label(top_frame, image=icon_image, compound=LEFT, text="Convertisseur de devises", height=3, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=BLUE_COLOR, fg=WHITE_COLOR)
app_name_label.place(x=0, y=0)
```

Le code ouvre d'abord le fichier image `icon.png` en utilisant la classe `Image` du module PIL (Python Imaging Library). Il redimensionne ensuite l'image à une taille de 40x40 en utilisant la méthode `resize()`. Ensuite, il convertit l'image en un format qui peut être affiché dans l'interface graphique en utilisant la classe `PhotoImage` du module `ImageTk`.

La ligne suivante crée un widget `Label` qui affiche l'icône de l'application et le titre. Vous créez le widget à l'intérieur du cadre supérieur. Le widget prend plusieurs paramètres pour configurer son apparence.

Les paramètres incluent les éléments suivants :

* l'`image` de l'icône de l'application
* le `texte` à afficher ("Convertisseur de devises")
* la `hauteur` de l'étiquette (définie à 3)
* le remplissage sur les côtés gauche et supérieur (définis à 13 et 30, respectivement)
* le point d'ancrage de l'étiquette (définie au centre) 
* le style de police (`Arial 16 bold`)
* la couleur de fond (définie à `BLUE_COLOR`)
* la couleur de premier plan (définie à `WHITE_COLOR`)

Enfin, nous utilisons la méthode `place()` pour définir la position de l'étiquette dans le cadre supérieur. 

### Comment ajouter des widgets dans le cadre principal

Comme mentionné, le cadre principal contiendra les widgets essentiels. Créons-les étape par étape.

Le code suivant crée un widget `Label` nommé `result_label` à l'intérieur du cadre `main_frame`. Cette étiquette affichera le résultat de la conversion de devises. 

```python
result_label = Label(main_frame, text=" ", width=15, height=2, pady=7, padx=0, anchor=CENTER, font=('Ivy 16 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=SOLID)
result_label.place(x=50, y=10)
```

L'étiquette a un texte défini sur une chaîne vide (" "), une largeur de 15, une hauteur de 2 lignes et un remplissage de 7 pixels sur l'axe y et 0 pixel sur l'axe x. Le texte sera centré en utilisant l'option `anchor=CENTER`, et la police utilisée est `Ivy 16 bold`. La couleur de fond de l'étiquette est définie sur blanc (`bg=WHITE_COLOR`), et la couleur du texte est noire (`fg=BLACK_COLOR`). L'option `relief` est définie sur SOLID pour donner à l'étiquette une bordure. Enfin, l'étiquette est placée aux coordonnées (50, 10) en utilisant la méthode `place()`.

Ensuite, dans la conception de l'application, il y a deux étiquettes - "De" et "Vers", chacune suivie d'une `ComboBox` en dessous.

```python
from_label = Label(main_frame, text="De", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
from_label.place(x=48, y=90)
from_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
from_combo['values'] = (get_currencies())
from_combo.current(0)
from_combo.place(x=50, y=115)


to_label = Label(main_frame, text="Vers", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
to_label.place(x=158, y=90)
to_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
to_combo['values'] = (get_currencies())
to_combo.current(1)
to_combo.place(x=160, y=115)
```

La première `Label` et `ComboBox` sont pour la devise à convertir. Vous créez l'étiquette en utilisant la fonction `Label()` avec le texte, la largeur, la hauteur, le remplissage, la police et les paramètres de couleur spécifiés. L'étiquette est ensuite placée dans le cadre principal aux coordonnées spécifiées en utilisant la fonction place(). 

Vous créez ensuite une `ComboBox` en utilisant la fonction `ttk.Combobox()` avec la largeur, la police et les paramètres de justification spécifiés. Les valeurs disponibles pour la `ComboBox` sont définies en utilisant la fonction `get_currencies()` (importée de `utils.py`), et la valeur par défaut est définie sur le premier élément de la liste en utilisant la fonction `current()`. La `ComboBox` est également placée dans le cadre principal aux coordonnées spécifiées en utilisant la fonction `place()`.

La deuxième étiquette et la deuxième ComboBox sont pour la devise à convertir. L'étiquette et la ComboBox sont créées et placées de manière similaire à la première étiquette et à la première ComboBox, la seule différence étant le texte et les coordonnées de placement.

Les deux derniers widgets dans la conception de l'application sont le champ de saisie et le bouton de conversion. Vous pouvez utiliser la méthode `Entry()` pour créer le champ de saisie. Elle prend plusieurs paramètres, y compris `width`, `justify`, `font`, et `relief`. Le widget créé est ensuite placé en utilisant la méthode `place()` avec des coordonnées spécifiques sur le cadre principal.

De même, le bouton de conversion est créé en utilisant la méthode `Button()`. Il prend plusieurs paramètres tels que `text`, `width`, `height`, `bg`, `fg`, `font`, et `command`. Le bouton créé est ensuite placé en utilisant la méthode `place()` avec des coordonnées spécifiques sur le cadre principal.

Voici le code pour créer le champ de saisie et le bouton de conversion :

```python
amount_entry = Entry(main_frame, width=22, justify=CENTER,
                    font=('Ivy 12 bold'), relief=SOLID)
amount_entry.place(x=50, y=155)

convert_button = Button(main_frame, text="Convertir", width=19, padx=5,
                        height=1, bg=BLUE_COLOR, fg=WHITE_COLOR, font=('Ivy 12 bold'), command=convert)
convert_button.place(x=50, y=210)
```

Le paramètre `command` dans le widget `convert_button` prend un nom de fonction. Dans ce cas, il est défini sur `convert`. Mais la fonction `convert` n'a pas encore été définie. Pour la définir, vous pouvez ajouter le code suivant juste avant que la fenêtre ne soit définie :

```python
def convert():
    amount = float(amount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    converted_amount = convert_currency(from_currency, to_currency, amount)

    result_label['text'] = f'{to_currency} {converted_amount:.2f}'
```

La fonction `convert` prend l'entrée de l'utilisateur à partir du widget `amount_entry` et les devises sélectionnées à partir des widgets `from_combo` et `to_combo`, et les passe à la fonction `convert_currency` (importée de `utils.py`) pour obtenir le montant converti. Elle définit ensuite la valeur de `text` sur la valeur échangée dans le widget `result_label`.

Enfin, vous appelez la méthode `mainloop()` à la fin du fichier. La méthode est responsable de l'exécution de l'application et de la vérification continue des événements utilisateur, tels que les clics de souris, les entrées clavier et le redimensionnement de la fenêtre, et de la mise à jour de la fenêtre si nécessaire. 

Une fois la méthode `mainloop()` appelée, le programme entre dans la boucle d'événements et commence à attendre les événements utilisateur. La fenêtre restera ouverte et active jusqu'à ce que l'utilisateur ferme la fenêtre ou que le programme soit terminé.

```python
# Mainloop
window.mainloop()
```

## Code final

Voici le code final pour l'application GUI du convertisseur de devises que vous avez construite. Ce code intègre tous les différents composants que nous avons discutés jusqu'à présent, y compris la création de cadres, d'étiquettes, de boîtes de combinaison, de champs de saisie et de boutons.

```python
from tkinter import *
from tkinter import Tk, ttk

from PIL import Image, ImageTk

from utils import convert_currency, get_currencies

# Couleurs
WHITE_COLOR = "#FFFFFF"
BLACK_COLOR = "#333333"
BLUE_COLOR = "#0000FF"


def convert():
    amount = float(amount_entry.get())
    from_currency = from_combo.get()
    to_currency = to_combo.get()
    converted_amount = convert_currency(from_currency, to_currency, amount)

    result_label['text'] = f'{to_currency} {converted_amount:.2f}'


# Configuration de la fenêtre
window = Tk()
window.geometry("300x320")
window.title("Convertisseur de devises")
window.configure(bg=WHITE_COLOR)
window.resizable(height=FALSE, width=FALSE)


# Cadres
top_frame = Frame(window, width=300, height=60, bg=BLUE_COLOR)
top_frame.grid(row=0, column=0)

main_frame = Frame(window, width=300, height=260, bg=WHITE_COLOR)
main_frame.grid(row=1, column=0)


# Widgets du cadre supérieur
icon_image = Image.open('icon.png')
icon_image = icon_image.resize((40, 40))
icon_image = ImageTk.PhotoImage(icon_image)
app_name_label = Label(top_frame, image=icon_image, compound=LEFT, text="Convertisseur de devises", height=3, padx=13, pady=30, anchor=CENTER, font=('Arial 16 bold'), bg=BLUE_COLOR, fg=WHITE_COLOR)
app_name_label.place(x=0, y=0)

# Widgets du cadre principal
result_label = Label(main_frame, text=" ", width=15, height=2, pady=7, padx=0, anchor=CENTER, font=('Ivy 16 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=SOLID)
result_label.place(x=50, y=10)

from_label = Label(main_frame, text="De", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
from_label.place(x=48, y=90)
from_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
from_combo['values'] = (get_currencies())
from_combo.current(0)
from_combo.place(x=50, y=115)

to_label = Label(main_frame, text="Vers", width=8, height=1, pady=0, padx=0, anchor=NW, font=('Ivy 10 bold'), bg=WHITE_COLOR, fg=BLACK_COLOR, relief=FLAT)
to_label.place(x=158, y=90)
to_combo = ttk.Combobox(main_frame, width=8, justify=CENTER, font=('Ivy 12 bold'),)
to_combo['values'] = (get_currencies())
to_combo.current(1)
to_combo.place(x=160, y=115)

amount_entry = Entry(main_frame, width=22, justify=CENTER,
                    font=('Ivy 12 bold'), relief=SOLID)
amount_entry.place(x=50, y=155)

convert_button = Button(main_frame, text="Convertir", width=19, padx=5,
                        height=1, bg=BLUE_COLOR, fg=WHITE_COLOR, font=('Ivy 12 bold'), command=convert)
convert_button.place(x=50, y=210)

# Mainloop
window.mainloop()

```

Vous pouvez enfin exécuter l'application et commencer à convertir des devises !

## Conclusion

Dans ce tutoriel, vous avez appris à créer une application simple de convertisseur de devises en utilisant Python et Tkinter. Nous avons couvert des sujets tels que la création de cadres, d'étiquettes, de widgets d'entrée, de boîtes de combinaison et de boutons. Vous avez également créé une fonction pour convertir des devises en fonction de l'entrée de l'utilisateur. 

Il existe plusieurs façons d'améliorer cette application. Vous pouvez améliorer l'interface utilisateur pour la rendre plus attrayante, ajouter une fonctionnalité pour enregistrer l'historique des conversions, et bien plus encore.

Si vous avez suivi ce tutoriel et construit votre propre application de convertisseur de devises, je vous encourage à partager votre création avec le monde ! Prenez une capture d'écran ou enregistrez une vidéo de votre application en action, et partagez-la sur Twitter. N'oubliez pas de me taguer, [@ashutoshkrris](https://twitter.com/ashutoshkrris), afin que je puisse voir votre travail et le partager avec mes abonnés.

J'ai hâte de voir ce que vous avez créé ! Bon codage !

### Ressources supplémentaires

* [Dépôt Github](https://github.com/ashutoshkrris/currency-converter-gui) pour le tutoriel
* [Créer des interfaces graphiques en Python Tutoriel](https://www.youtube.com/watch?v=YXPyB4XeYLA)
* [Comment interagir avec les services web en Python](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)
* [Documentation de l'API de conversion de devises](https://currencyapi.com/docs)