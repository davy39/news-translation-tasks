---
title: Comment construire un système de prévision météorologique en Python avec Tkinter
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2023-04-04T16:01:03.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-geolocation-based-weather-forecasting-system-using-tkinter
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/weather-forecast.png
tags:
- name: api
  slug: api
- name: Python
  slug: python
seo_title: Comment construire un système de prévision météorologique en Python avec
  Tkinter
seo_desc: "Tkinter is a Python GUI (Graphical User Interface) toolkit that allows\
  \ developers to create desktop applications with Python. It provides a set of tools\
  \ and widgets for building graphical interfaces that are simple and intuitive to\
  \ use. \nTkinter is i..."
---

Tkinter est une boîte à outils GUI (Interface Graphique Utilisateur) Python qui permet aux développeurs de créer des applications de bureau avec Python. Il fournit un ensemble d'outils et de widgets pour construire des interfaces graphiques simples et intuitives à utiliser. 

Tkinter est inclus dans la distribution standard de Python et prend en charge le développement multiplateforme, ce qui en fait un choix idéal pour construire des applications de bureau.

Dans ce tutoriel, vous apprendrez à construire un système simple de prévision météorologique basé sur la géolocalisation IP en utilisant Python. Vous utiliserez l'API de géolocalisation de [ipbase.com](https://ipbase.com/) pour récupérer l'emplacement de l'utilisateur en fonction de son adresse IP, et l'API [OpenWeatherMap](https://openweathermap.org/) pour obtenir les conditions météorologiques actuelles pour cet emplacement. Commençons !

## Prérequis

Avant de commencer à construire le projet, vous devez vous assurer que vous avez les prérequis suivants :

* Python 3.8+ installé sur votre système
* Connaissance pratique de Python
* Connaissance de base de [comment interagir avec les services web en Python](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)
* Clé API de l'API de géolocalisation de [ipbase.com](https://ipbase.com) : Pour utiliser l'API de géolocalisation de ipbase.com, vous devrez vous inscrire pour obtenir une clé API. Vous pouvez vous inscrire pour un compte gratuit à l'adresse [https://app.ipbase.com/register](https://app.ipbase.com/register). Une fois inscrit, vous pouvez trouver votre clé API (surlignée en noir) sur la page du tableau de bord.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-082417.png)
_Obtenir votre clé API depuis ipbase.com_

* Clé API de [OpenWeatherMap](https://openweathermap.org/) : Pour utiliser l'API OpenWeatherMap, vous devrez vous inscrire pour obtenir une clé API. Vous pouvez vous inscrire pour un compte gratuit à l'adresse [https://home.openweathermap.org/users/sign_up](https://home.openweathermap.org/users/sign_up). Une fois inscrit, vous pouvez trouver votre clé API sur la page des clés API.

![Image](https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-01-090934.png)
_Obtenir votre clé API depuis OpenWeatherMap.com_

## Comment configurer votre environnement virtuel

Avant de commencer à coder, vous devrez vous assurer que vous avez tous les outils et bibliothèques nécessaires installés. Pour garantir que vous avez un environnement propre et isolé, vous allez créer un environnement virtuel en utilisant `venv`.

Créez un répertoire de projet et naviguez jusqu'à celui-ci dans le terminal :

```bash
mkdir weather-forecast
cd weather-forecast
```

Créez un environnement virtuel nommé `env` en utilisant la commande suivante :

```bash
python -m venv env
```

Python est maintenant livré avec la bibliothèque `venv` préinstallée pour créer des environnements virtuels.

Activez l'environnement virtuel comme ceci :

```bash
source env/bin/activate
```

Note : Si vous êtes sous Windows, vous devrez utiliser source env/Scripts/activate pour activer l'environnement.

Vous devriez voir `(env)` dans votre invite de terminal, indiquant que l'environnement virtuel a été activé.

## Comment installer les bibliothèques

Maintenant que vous avez créé l'environnement virtuel, vous pouvez installer les bibliothèques suivantes :

* `requests` : Cette bibliothèque vous aide à envoyer des requêtes sur les points de terminaison de l'API.
* `python-decouple` : Cette bibliothèque vous aide à lire les valeurs des variables d'environnement

Pour installer les bibliothèques, exécutez la commande suivante :

```bash
pip install requests python-decouple
```

## Comment utiliser l'API de géolocalisation pour obtenir les détails de localisation

Bien qu'il existe de nombreuses API de géolocalisation disponibles telles que [IP Lookup API](https://iplookupapi.com/), [ipapi](https://ipapi.com/), etc., vous allez utiliser l'API [ipbase.com](https://ipbase.com/) dans ce tutoriel. 

L'API fournit des données basées sur la localisation pour toute adresse IP et est très facile à intégrer avec Python en utilisant le module `requests`. Elle vous permet de récupérer des informations telles que l'adresse IP elle-même, le nom d'hôte, la localisation, l'organisation, et plus encore. L'API utilise un service web RESTful et fournit des réponses au format JSON.

Pour obtenir les détails de localisation en utilisant l'API de géolocalisation de ipbase.com, vous devez faire une requête HTTP au point de terminaison de l'API avec les paramètres de requête appropriés. Vous devez passer la clé API comme paramètre de requête obligatoire et l'adresse IP comme paramètre de requête facultatif. 

Si vous ne passez pas d'adresse IP, l'API renvoie des informations sur l'adresse IP à partir de laquelle la requête a été faite.

Vous pouvez utiliser la bibliothèque `requests` en Python pour faire la requête HTTP au point de terminaison de l'API. Voici un exemple de la façon dont vous pouvez faire une requête :

```python
import requests

api_key = '<YOUR_API_KEY>'
ip_address = '<IP_ADDRESS>'  # Facultatif

api_endpoint = 'https://api.ipbase.com/v2/info'
query_params = {'apiKey': api_key}
if ip_address:
    query_params['ip'] = ip_address

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Traiter les données de réponse
else:
    # Gérer les erreurs
    print(f'Erreur : {response.status_code} - {response.text}')

```

Le dictionnaire `query_params` stocke la clé API et éventuellement l'adresse IP à interroger. Comme mentionné, si `ip_address` est fourni, vous l'ajoutez au dictionnaire `query_params` comme valeur de la clé `'ip'`. 

La méthode `requests.get()` envoie une requête GET au point de terminaison de l'API, avec l'URL `api_endpoint` et le dictionnaire `query_params` passés comme arguments. La réponse de l'API est stockée dans la variable `response`. Si le code de statut de la réponse est `200`, indiquant une requête réussie, vous analysez le contenu de la réponse comme des données JSON en utilisant la méthode `.json()`, et la variable `data` peut être utilisée pour accéder aux détails de localisation pertinents.

Si le code de statut de la réponse n'est pas `200`, indiquant une erreur, le message d'erreur est imprimé sur la console en utilisant `print(f'Erreur : {response.status_code} - {response.text}')`.

Une réponse JSON réussie ressemble à ceci :

```json
{
  "data":{
    "ip":"171.76.86.246",
    "hostname":"None",
    "type":"v4",
    "range_type":{
      "type":"PUBLIC",
      "description":"Adresse publique"
    },
    "connection":{
      "asn":45609,
      "organization":"Bharti Airtel Limited",
      "isp":"Bharti Airtel Limited",
      "range":"171.76.64.0/18"
    },
    "location":{
      "geonames_id":1277333,
      "latitude":12.971940040588379,
      "longitude":77.59368896484375,
      "zip":"560001",
      "continent":{
        "code":"AS",
        "name":"Asia",
        "name_translated":"Asie"
      },
      "country":{
        "alpha2":"IN",
        "alpha3":"IND",
        "calling_codes":[
          "+91"
        ],
        "currencies":[
          {
            "symbol":"Rs",
            "name":"Indian Rupee",
            "symbol_native":"\u099f\u0995\u09be",
            "decimal_digits":2,
            "rounding":0,
            "code":"INR",
            "name_plural":"Indian rupees"
          }
        ],
        "emoji":"\ud83c\uddee\ud83c\uddf3",
        "ioc":"IND",
        "languages":[
          {
            "name":"English",
            "name_native":"English"
          },
          {
            "name":"Hindi",
            "name_native":"\u0939\u093f\u0902\u0926\u0940"
          }
        ],
        "name":"India",
        "name_translated":"Inde",
        "timezones":[
          "Asia/Kolkata"
        ],
        "is_in_european_union":false,
        "fips":"IN",
        "geonames_id":1269750,
        "hasc_id":"IN",
        "wikidata_id":"Q668"
      },
      "city":{
        "fips":"None",
        "alpha2":"None",
        "geonames_id":1277333,
        "hasc_id":"None",
        "wikidata_id":"Q1355",
        "name":"Bangalore",
        "name_translated":"Bangalore"
      },
      "region":{
        "fips":"IN19",
        "alpha2":"IN-KA",
        "geonames_id":1267701,
        "hasc_id":"IN.KA",
        "wikidata_id":"Q1185",
        "name":"Karnataka",
        "name_translated":"Karnataka"
      }
    },
    "tlds":[
      ".in"
    ],
    "timezone":{
      "id":"Asia/Kolkata",
      "current_time":"2023-03-30  0T08:45:00+05:30",
      "code":"IST",
      "is_daylight_saving":false,
      "gmt_offset":19800
    },
    "security":{
      "is_anonymous":"None",
      "is_bot":"None",
      "is_known_attacker":"None",
      "is_proxy":"None",
      "is_spam":"None",
      "is_tor":"None",
      "proxy_type":"None",
      "threat_score":"None"
    },
    "domains":{
      "count":"None",
      "domains":[
        
      ]
    }
  }
}
```

La réponse JSON obtenue de l'API de géolocalisation contient une grande quantité d'informations. Mais vous ne vous intéressez qu'à la clé `city`, qui est imbriquée dans la clé `location`, elle-même imbriquée dans la clé `data`. Vous pouvez extraire le nom de la ville en utilisant `city["name"]`.

Ainsi, une fois que vous avez analysé la réponse JSON dans un dictionnaire Python, vous pouvez extraire le nom de la ville comme suit :

```python
import requests

api_key = '<YOUR_API_KEY>'
ip_address = '<IP_ADDRESS>'  # Facultatif

api_endpoint = 'https://api.ipbase.com/v2/info'
query_params = {'apiKey': api_key}
if ip_address:
    query_params['ip'] = ip_address

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Traiter les données de réponse
    try:
        location_data = data['data']['location']
        city_name = location_data['city']['name']
        print(city_name)
    except KeyError as e:
        print(f'Erreur : {e}')
else:
    # Gérer les erreurs
    print(f'Erreur : {response.status_code} - {response.text}')

```

Note : Assurez-vous de remplacer la valeur de `api_key` par votre clé API correcte. Vous pouvez mettre une adresse IP dans la variable `ip_address` ou simplement la laisser comme une chaîne vide.

Sortie :

```bash
Gurugram
```

## Comment utiliser l'API OpenWeatherMap pour obtenir les détails météorologiques

L'API OpenWeatherMap est une API météorologique gratuite fournissant des données météorologiques actuelles, des prévisions horaires, sur 5 jours et 16 jours, des données historiques et des cartes météorologiques pour n'importe quel endroit dans le monde. Elle fournit l'accès à une grande quantité de données météorologiques, y compris la température, la vitesse du vent, l'humidité, les précipitations, et plus encore.

Pour faire des requêtes à l'API OpenWeatherMap, vous devez à nouveau utiliser la bibliothèque `requests` en Python. Vous devez faire une requête GET au point de terminaison de l'API avec les paramètres de requête appropriés, y compris votre clé API et le nom de la ville pour laquelle vous souhaitez obtenir les détails météorologiques.

Voici un exemple de code qui démontre comment faire une requête à l'API OpenWeatherMap :

```python
import requests

api_key = '<YOUR_API_KEY>'
city_name = '<CITY_NAME>'

api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
query_params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Traiter les données de réponse
else:
    # Gérer les erreurs
    print(f'Erreur : {response.status_code} - {response.text}')

```

La réponse de l'API OpenWeatherMap est au format JSON. Vous pouvez analyser la réponse et la convertir en un dictionnaire Python en utilisant la méthode `json()`.

Une réponse JSON réussie ressemble à ceci :

```json
{
  "coord":{
    "lon":77.6033,
    "lat":12.9762
  },
  "weather":[
    {
      "id":802,
      "main":"Clouds",
      "description":"nuages épars",
      "icon":"03d"
    }
  ],
  "base":"stations",
  "main":{
    "temp":27.8,
    "feels_like":29.26,
    "temp_min":26.9,
    "temp_max":27.8,
    "pressure":1018,
    "humidity":61
  },
  "visibility":6000,
  "wind":{
    "speed":3.09,
    "deg":250
  },
  "clouds":{
    "all":40
  },
  "dt":1680150474,
  "sys":{
    "type":1,
    "id":9205,
    "country":"IN",
    "sunrise":1680137244,
    "sunset":1680181248
  },
  "timezone":19800,
  "id":1277333,
  "name":"Bengaluru",
  "cod":200
}
```

À partir du dictionnaire de réponse, vous pouvez extraire divers détails météorologiques tels que la température, la vitesse du vent, l'humidité et les précipitations. Par exemple, pour extraire la température en Celsius, vous pouvez utiliser le code suivant :

```python
import requests

api_key = '<YOUR_API_KEY>'
city_name = '<CITY_NAME>'

api_endpoint = 'https://api.openweathermap.org/data/2.5/weather'
query_params = {'q': city_name, 'appid': api_key, 'units': 'metric'}

response = requests.get(api_endpoint, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Traiter les données de réponse
    temperature = data['main']['temp'] 
    print(temperature)
else:
    # Gérer les erreurs
    print(f'Erreur : {response.status_code} - {response.text}')

```

De même, vous pouvez extraire d'autres détails météorologiques selon vos besoins.

## Comment construire l'application GUI avec Tkinter

Dans l'application de prévision météorologique, vous utiliserez Tkinter pour créer une interface graphique permettant à l'utilisateur de saisir les détails de localisation et de récupérer les informations météorologiques. 

L'interface graphique aura un champ de saisie où les utilisateurs pourront entrer soit l'adresse IP, soit le nom de la ville. Elle inclura également un bouton pour récupérer les détails météorologiques et un autre bouton pour obtenir les détails météorologiques en utilisant la direction de l'emplacement actuel. 

Cette interface graphique sera un moyen simple et intuitif pour les utilisateurs d'interagir avec l'application et de récupérer les informations dont ils ont besoin.

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Screenshot-2023-03-30-101552.png)

### Comment créer la fenêtre principale et la disposition

Pour construire une application GUI avec Tkinter, vous devez d'abord créer la fenêtre principale et la disposition. Vous allez créer une fenêtre avec une largeur de 400 pixels et une hauteur de 200 pixels en utilisant la fonction `Tk()` du module Tkinter. Vous allez ensuite définir le titre de la fenêtre en utilisant la fonction `title()`.

Vous allez également ajouter les étiquettes, boutons et champs de saisie nécessaires à notre fenêtre en utilisant les fonctions `Label()`, `Button()` et `Entry()` du module Tkinter. Vous allez utiliser la fonction `pack()` pour afficher ces widgets dans notre fenêtre.

```python
import tkinter as tk

root = tk.Tk()
root.title("Application de prévision météorologique")
root.geometry("400x200")

input_label = tk.Label(root, text="Entrez la ville ou l'adresse IP :")
input_label.pack()

input_field = tk.Entry(root)
input_field.pack()

submit_button = tk.Button(root, text="Obtenir la météo", command=get_weather)
submit_button.pack()

location_button = tk.Button(root, text="Utiliser la localisation actuelle", command=get_location_weather)
location_button.pack()

weather_label = tk.Label(root, text="")
weather_label.pack()

root.mainloop()
```

Vous avez ajouté les étiquettes, boutons et champs de saisie nécessaires dans le code ci-dessus. Le `input_label` et `input_field` permettent à l'utilisateur d'entrer la ville ou l'adresse IP. Le `submit_button` récupère les informations météorologiques en utilisant la valeur saisie, et le `location_button` récupère les informations météorologiques pour la localisation actuelle. Le `weather_label` affiche les informations météorologiques récupérées.

### Comment récupérer et afficher les informations météorologiques

Pour récupérer et afficher les informations météorologiques, vous allez définir deux fonctions `get_weather()` et `get_location_weather()`. 

La fonction `get_weather()` récupère les détails météorologiques en fonction de la saisie de l'utilisateur. Si l'utilisateur saisit une adresse IP, la fonction récupère d'abord le nom de la ville en utilisant l'API ipbase.com, puis utilise le nom de la ville pour récupérer les détails météorologiques en utilisant l'API OpenWeatherMap. 

Si l'utilisateur saisit directement un nom de ville, la fonction utilise le nom de la ville pour récupérer les détails météorologiques en utilisant l'API OpenWeatherMap. La fonction met ensuite à jour l'étiquette météo pour afficher la température en Celsius pour l'emplacement spécifié.

La fonction `get_location_weather()` récupère la localisation actuelle en utilisant l'API ipbase.com, puis utilise le nom de la ville pour récupérer les détails météorologiques en utilisant l'API OpenWeatherMap. La fonction met à jour l'étiquette météo pour afficher la température en Celsius pour la localisation actuelle.

Voici le code complet pour les fonctions `get_weather()` et `get_location_weather()` :

```python
import requests
import tkinter as tk
import re
from decouple import config

OPEN_WEATHER_MAP_API_KEY = config("OPEN_WEATHER_MAP_API_KEY")
OPEN_WEATHER_MAP_API_ENDPOINT = 'https://api.openweathermap.org/data/2.5/weather'

IPBASE_API_KEY = config("IPBASE_API_KEY")
IPBASE_API_ENDPOINT = "https://api.ipbase.com/v2/info"

IP_ADDRESS_REGEX = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


def get_weather():
    input_value = input_field.get()

    if IP_ADDRESS_REGEX.match(input_value):
        ipbase_query_params = {
            "apiKey": IPBASE_API_KEY,
            "ip": input_value
        }
        response = requests.get(IPBASE_API_ENDPOINT,
                                params=ipbase_query_params)
        city_name = response.json()["data"]["location"]["city"]["name"]

        weather_query_params = {
            'q': city_name,
            'appid': OPEN_WEATHER_MAP_API_KEY,
            'units': 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()

    else:
        # Essayer d'obtenir les données météorologiques directement en utilisant le nom de la ville
        weather_query_params = {
            'q': input_value,
            'appid': OPEN_WEATHER_MAP_API_KEY,
            'units': 'metric'
        }
        response = requests.get(
            OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
        weather_data = response.json()

    # Afficher les données météorologiques
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']}\u00b0C")


def get_location_weather():
    query_params = {
        "apiKey": IPBASE_API_KEY
    }
    response = requests.get(IPBASE_API_ENDPOINT, params=query_params)
    city_name = response.json()["data"]["location"]["city"]["name"]

    weather_query_params = {
        'q': city_name,
        'appid': OPEN_WEATHER_MAP_API_KEY,
        'units': 'metric'
    }
    response = requests.get(
        OPEN_WEATHER_MAP_API_ENDPOINT, params=weather_query_params)
    weather_data = response.json()

    # Afficher les données météorologiques
    weather_label.config(
        text=f"{weather_data['name']}: {weather_data['main']['temp']}\u00b0C")
```

Au lieu de coder en dur les valeurs des clés API, vous définissez leurs valeurs dans les variables d'environnement. Créez un fichier `.env` et ajoutez le code suivant :

```
export OPEN_WEATHER_MAP_API_KEY='your-value-here'
export IPBASE_API_KEY='your-value-here'
```

Remplacez `your-value-here` par les valeurs correctes des clés API et exécutez la commande suivante pour définir les variables d'environnement :

```bash
source .env
```

Vous utilisez ensuite la bibliothèque `python-decouple` pour lire les valeurs des clés API dans le code Python. 

En plus de cela, le code importe le module `re` pour utiliser des expressions régulières pour la correspondance de motifs. Il est utilisé pour vérifier si un utilisateur a saisi une adresse IP.

Note : Assurez-vous d'ajouter les deux fonctions ci-dessus avant le code Tkinter, sinon vous obtiendrez une `NameError` pour les noms de fonction.

Si vous êtes confus, vous pouvez voir le code [dans ce dépôt](https://github.com/ashutoshkrris/weather-forecast-tkinter/blob/main/app.py).

![Image](https://www.freecodecamp.org/news/content/images/2023/03/Weather-Demo-Made-with-Clipchamp.gif)

## Conclusion

Dans ce tutoriel, vous avez appris à construire une application de prévision météorologique en utilisant Tkinter. Vous avez utilisé deux services d'API externes pour obtenir des données en temps réel. 

Il existe plusieurs façons d'étendre et d'améliorer ce projet. Par exemple, vous pouvez ajouter plus de fonctionnalités à l'application GUI, telles que la capacité de récupérer des prévisions météorologiques pour plusieurs jours ou d'afficher des données météorologiques pour plusieurs emplacements à la fois.

Si vous avez suivi ce tutoriel et construit votre propre application de prévision météorologique, je vous encourage à partager votre création avec le monde ! Prenez une capture d'écran ou enregistrez une vidéo de votre application en action, et partagez-la sur Twitter. N'oubliez pas de me taguer, [@ashutoshkrris](https://twitter.com/ashutoshkrris), afin que je puisse voir votre travail et le partager avec mes abonnés.

J'ai hâte de voir ce que vous avez créé ! Bon codage !

### Ressources supplémentaires

* [Dépôt Github](https://github.com/ashutoshkrris/weather-forecast-tkinter/blob/main/app.py) pour le tutoriel
* [Comment interagir avec les services web en utilisant Python](https://blog.ashutoshkrris.in/how-to-interact-with-web-services-using-python)
* [Documentation ipbase.com](https://ipbase.com/docs)
* [Documentation de l'API OpenWeatherMap](https://openweathermap.org/api)