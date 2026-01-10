---
title: Comment créer une application web en utilisant Flask de Python et Google App
  Engine
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-05T21:58:56.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-web-app-using-pythons-flask-and-google-app-engine-52b1bb82b221
coverImage: https://cdn-media-1.freecodecamp.org/images/1*PBKcxaxtTHltv4ML4xpo3g.png
tags:
- name: Flask Framework
  slug: flask
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment créer une application web en utilisant Flask de Python et Google
  App Engine
seo_desc: 'By Tristan Ganry

  This is a small tutorial project for learning Flask, APIs, and Google App Engine
  for beginners.


  If you want to build web apps in a very short amount of time using Python, then
  Flask is a fantastic option.

  Flask is a small and powerf...'
---

Par Tristan Ganry

#### Ce projet est un petit tutoriel pour apprendre Flask, les APIs et Google App Engine pour les débutants.

![Image](https://cdn-media-1.freecodecamp.org/images/tnQx3nzC79uTpvzB3Y3NS-S9ox7vcvlwALnN)

Si vous souhaitez créer des applications web en très peu de temps avec Python, alors [Flask](http://flask.pocoo.org/) est une option fantastique.

Flask est un framework web petit et puissant (également connu sous le nom de "[microframework](https://en.wikipedia.org/wiki/Microframework)"). Il est également très facile à apprendre et simple à coder. D'après mon expérience personnelle, il était facile de commencer en tant que débutant.

Avant ce projet, mes connaissances en Python étaient principalement limitées à la Data Science. Pourtant, j'ai pu créer cette application et rédiger ce tutoriel en seulement quelques heures.

Dans ce tutoriel, je vais vous montrer comment créer une simple application météo avec du contenu dynamique en utilisant une API. Ce tutoriel est un excellent point de départ pour les débutants. Vous apprendrez à créer du contenu dynamique à partir d'APIs et à le déployer sur Google Cloud.

Le produit final peut être consulté [ici](http://weatherv2-220201.appspot.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/C1sPGVUOkyzQOv31MGaJVqmCcEvcJyJySYJn)

![Image](https://cdn-media-1.freecodecamp.org/images/Shef35vcxtGaPKwRseaHe77mkUwaUuFWegLp)

Pour créer une application météo, nous aurons besoin de demander une clé API à [Open Weather Map](https://openweathermap.org/api). La version gratuite permet jusqu'à 60 appels par minute, ce qui est largement suffisant pour cette application. Les icônes de conditions météo d'Open Weather Map ne sont pas très jolies. Nous les remplacerons par certaines des 200+ icônes météo d'[Erik Flowers](https://erikflowers.github.io/weather-icons/).

![Image](https://cdn-media-1.freecodecamp.org/images/dQsaxxMDaGMLeiJ8P08b868zi9dIh3yGv9bs)

Ce tutoriel couvrira également : (1) la conception CSS de base, (2) le HTML de base avec Jinja, et (3) le déploiement d'une application Flask sur Google Cloud.

Les étapes que nous allons suivre sont listées ci-dessous :

* **Étape 0 :** Installation de Flask (ce tutoriel ne couvre pas l'installation de Python et PIP)
* **Étape 1 :** Construction de la structure de l'application
* **Étape 2 :** Création du code principal de l'application avec la requête API
* **Étape 3 :** Création des 2 pages pour l'application (Principale et Résultat) avec [Jinja](http://jinja.pocoo.org/), HTML et CSS
* **Étape 4 :** Déploiement et test sur votre ordinateur local
* **Étape 5 :** Déploiement sur Google Cloud.

#### **Étape 0 — Installation de Flask et des bibliothèques que nous allons utiliser dans un environnement virtuel.**

Nous allons construire ce projet en utilisant un environnement virtuel. Mais pourquoi en avons-nous besoin ?

Avec les environnements virtuels, vous créez un environnement local spécifique pour chaque projet. Vous pouvez choisir les bibliothèques que vous souhaitez utiliser sans impacter l'environnement de votre ordinateur. À mesure que vous codez plus de projets sur votre ordinateur, chaque projet aura besoin de bibliothèques différentes. Avec un environnement virtuel différent pour chaque projet, vous n'aurez pas de conflits entre votre système et vos projets ou entre les projets.

* Exécutez l'invite de commande (cmd.exe) avec des privilèges d'administrateur. Ne pas utiliser les privilèges d'administrateur vous empêchera d'utiliser pip.

![Image](https://cdn-media-1.freecodecamp.org/images/BWMVZ22h-2kLpmz8ERJwYcrVG0nZDpyGFVP4)

* (Optionnel) Installez virtualenv et virtualenvwrapper-win avec PIP. Si vous avez déjà ces bibliothèques système, passez à l'étape suivante.

```
#Optionnelpip install virtualenvwrapper-winpip install virtualenv
```

![Image](https://cdn-media-1.freecodecamp.org/images/W3miohvJFMX5AGoi376capkdSL8SIU9InS1b)

* Créez votre dossier avec le nom "WeatherApp" et créez un environnement virtuel avec le nom "venv" (cela peut prendre un peu de temps)

```
#Obligatoirmkdir WeatherAppcd WeatherAppvirtualenv venv
```

![Image](https://cdn-media-1.freecodecamp.org/images/1MdAaLRsZYhosvwmrdmmPOgJhAloAnuSrGda)

* Activez votre environnement virtuel avec "call" sur Windows (identique à "source" pour Linux). Cette étape change votre environnement du système vers l'environnement local du projet.

```
call venv\Scripts\activate.bat
```

![Image](https://cdn-media-1.freecodecamp.org/images/e62vzScJTaWHcacPBJ7o4FeYc7qBBjuhgG5I)

* Créez un fichier requirements.txt qui inclut Flask et les autres bibliothèques dont nous aurons besoin dans votre dossier WeatherApp, puis sauvegardez le fichier. Le fichier requirements est un excellent outil pour suivre les bibliothèques que vous utilisez dans votre projet.

```
Flask==0.12.3click==6.7gunicorn==19.7.1itsdangerous==0.24Jinja2==2.9.6MarkupSafe==1.0pytz==2017.2requests==2.13.0Werkzeug==0.12.1
```

![Image](https://cdn-media-1.freecodecamp.org/images/vi12evCt5VXwf7iZhhG3xmsmde-eCMrpjjJa)

* Installez les requirements et leurs dépendances. Vous êtes maintenant prêt à créer votre WeatherApp. C'est l'étape finale pour créer votre environnement local.

```
pip install -r requirements.txt
```

![Image](https://cdn-media-1.freecodecamp.org/images/0YVd79Lu1AZ7Bjk7XsgfvKl8AeKquOhd0MHd)

#### **Étape 1 — Construction de la structure de l'application**

Vous avez pris soin de l'environnement local. Vous pouvez maintenant vous concentrer sur le développement de votre application. Cette étape consiste à s'assurer que la structure de dossiers et de fichiers appropriée est en place. L'étape suivante prendra en charge le code backend.

* Créez deux fichiers Python (main.py, weather.py) et deux dossiers (static avec un sous-dossier img, templates).

![Image](https://cdn-media-1.freecodecamp.org/images/9g3DNt-aM1MWaDzM3vApwbw53UlEJVUTD38B)

#### **Étape 2 — Création du code principal de l'application avec la requête API (Backend)**

Avec la structure mise en place, vous pouvez commencer à coder le backend de votre application. L'exemple "Hello world" de Flask n'utilise qu'un seul fichier Python. Ce tutoriel utilise deux fichiers pour vous familiariser avec l'importation de fonctions dans votre application principale.

Le fichier main.py est le serveur qui dirige l'utilisateur vers la page d'accueil et vers la page de résultats. Le fichier weather.py crée une fonction avec une API qui récupère les données météo en fonction de la ville sélectionnée. La fonction remplit la page de résultats.

* Modifiez main.py avec le code suivant et sauvegardez

```
#!/usr/bin/env pythonfrom pprint import pprint as ppfrom flask import Flask, flash, redirect, render_template, request, url_forfrom weather import query_api
```

```
app = Flask(__name__)
```

```
@app.route('/')def index():    return render_template(        'weather.html',        data=[{'name':'Toronto'}, {'name':'Montreal'}, {'name':'Calgary'},        {'name':'Ottawa'}, {'name':'Edmonton'}, {'name':'Mississauga'},        {'name':'Winnipeg'}, {'name':'Vancouver'}, {'name':'Brampton'},         {'name':'Quebec'}])
```

```
@app.route("/result" , methods=['GET', 'POST'])def result():    data = []    error = None    select = request.form.get('comp_select')    resp = query_api(select)    pp(resp)    if resp:       data.append(resp)    if len(data) != 2:        error = 'Bad Response from Weather API'    return render_template(        'result.html',        data=data,        error=error)
```

```
if __name__=='__main__':    app.run(debug=True)
```

* Demandez une clé API gratuite sur Open Weather Map

![Image](https://cdn-media-1.freecodecamp.org/images/mgz3Hi9i5MytohrBFAwI5YjayYUlY94IMf6v)

* Modifiez weather.py avec le code suivant (en mettant à jour la clé API) et sauvegardez

```
from datetime import datetimeimport osimport pytzimport requestsimport mathAPI_KEY = 'XXXXXXXXXXXXXXXXXXXXXXXXXXX'API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')
```

```
def query_api(city):    try:        print(API_URL.format(city, API_KEY))        data = requests.get(API_URL.format(city, API_KEY)).json()    except Exception as exc:        print(exc)        data = None    return data
```

#### **Étape 3 — Création des pages avec [Jinja](http://jinja.pocoo.org/), HTML et CSS (Frontend)**

Cette étape consiste à créer ce que l'utilisateur verra.

Les pages HTML weather et result sont celles vers lesquelles le backend main.py dirigera et donnera la structure visuelle. Le fichier CSS apportera la touche finale. Il n'y a pas de JavaScript dans ce tutoriel (le frontend est en HTML et CSS pur).

C'était ma première fois en utilisant la bibliothèque de modèles [Jinja2](http://jinja.pocoo.org/) pour remplir le fichier HTML. J'ai été surpris de la facilité avec laquelle il était possible d'ajouter des images dynamiques ou d'utiliser des fonctions (par exemple, arrondir la météo). Définitivement un moteur de modèles fantastique.

* Créez le premier fichier HTML dans le dossier templates (weather.html)

```
<!doctype html><link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

```
<div class="center-on-page">  <h1>Météo dans une ville</h1>
```

```
<form class="form-inline" method="POST" action="{{ url_for('result') }}">   <div class="select">    <select name="comp_select" class="selectpicker form-control">    {% for o in data %}     <option value="{{ o.name }}">{{ o.name }}</option>    {% endfor %}    </select>   </div>    <button type="submit" class="btn">Aller</button></form>
```

* Créez le deuxième fichier HTML dans le dossier templates (result.html)

```
<!doctype html>
```

```
<link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
```

```
<div class="center-on-page">
```

```
{% for d in data %} {% set my_string = "static/img/" + d['weather'][0]['icon']+ ".svg" %}    <h1>  <img src="{{ my_string }}" class="svg" fill="white" height="100" vertical-align="middle" width="100"> </h1>  <h1>Météo</h1> <h1>{{ d['name'] }}, {{ d['sys']['country'] }}</h1>    <h1>{{ d['main']['temp']|round|int}} °C</h1>{% endfor %}
```

![Image](https://cdn-media-1.freecodecamp.org/images/nAw74NRrD1iOkBctyY5kfCj05C7T7waNHmPE)

* Ajoutez un fichier CSS dans le dossier static (style.css)

```
body {  color: #161616;  font-family: 'Roboto', sans-serif;  text-align: center;  background-color: currentColor;}.center-on-page {  position: absolute;  top:50%;  left: 50%;  transform: translate(-50%,-50%);}h1 {  text-align: center;  color:#FFFFFF;}img {  vertical-align: middle; }/* Reset Select */select {  -webkit-appearance: none;  -moz-appearance: none;  -ms-appearance: none;  appearance: none;  outline: 0;  box-shadow: none;  border: 0 !important;  background: #2c3e50;  background-image: none;}/* Custom Select */.select {  position: relative;  display: block;  width: 20em;  height: 3em;  line-height: 3;  background: #2c3e50;  overflow: hidden;  border-radius: .25em;}select {  width: 100%;  height: 100%;  margin: 0;  padding: 0 0 0 .5em;  color: #fff;  cursor: pointer;}select::-ms-expand {  display: none;}/* Arrow */.select::after {  content: '\25BC';  position: absolute;  top: 0;  right: 0;  bottom: 0;  padding: 0 1em;  background: #34495e;  pointer-events: none;}/* Transition */.select:hover::after {  color: #f39c12;}.select::after {  -webkit-transition: .25s all ease;  -o-transition: .25s all ease;  transition: .25s all ease;}
```

```
button{  -webkit-appearance: none;  -moz-appearance: none;  -ms-appearance: none;  appearance: none;  outline: 0;  box-shadow: none;  border: 0 !important;  background: #2c3e50;  background-image: none;  width: 100%;  height: 40px;  margin: 0;  margin-top: 20px;  color: #fff;  cursor: pointer;  border-radius: .25em;}.button:hover{  color: #f39c12;}
```

* Téléchargez les images dans le sous-dossier img dans static

Lien avec les images sur [Github](https://github.com/tristanga/WeatherApp_Image):

![Image](https://cdn-media-1.freecodecamp.org/images/eLqWEnRgPc5Zpx31oZrswupEvYNZkbqPpHPT)

![Image](https://cdn-media-1.freecodecamp.org/images/l70xGTIfD1z--a5EL2alZonpnSf9exoPciXI)

#### **Étape 4 — Déploiement et test en local**

À ce stade, vous avez configuré l'environnement, la structure, le backend et le frontend. La seule chose restante est de lancer votre application et de la tester sur votre localhost.

* Lancez simplement main.py avec Python

```
python main.py
```

* Allez sur le lien localhost proposé sur cmd avec votre navigateur web (Chrome, Mozilla, etc.). Vous devriez voir votre nouvelle application météo en direct sur votre ordinateur local :)

![Image](https://cdn-media-1.freecodecamp.org/images/oxAp6U8i0QKF0zi9iu25GWDJflH4R-b3DYxl)

![Image](https://cdn-media-1.freecodecamp.org/images/vlmbbRQPLuHa3EdSWrhlWFi0QlR1LvSklARt)

#### **Étape 5 — Déploiement sur Google Cloud**

Cette dernière étape consiste à partager votre application avec le monde. Il est important de noter qu'il existe de nombreux fournisseurs pour les applications web construites avec Flask. Google Cloud n'est qu'un parmi tant d'autres. Cet article ne couvre pas certains des autres comme AWS, Azure, Heroku...

Si la communauté est intéressée, je peux fournir les étapes pour les autres fournisseurs de cloud dans un autre article ainsi qu'une comparaison (tarifs, limitations, etc.).

Pour déployer votre application sur Google Cloud, vous devrez 1) Installer le SDK, 2) Créer un nouveau projet, 3) Créer 3 fichiers locaux, 4) Déployer et tester en ligne.

* Installez le SDK en suivant [les instructions de Google](https://cloud.google.com/sdk/install)
* Connectez-vous à votre compte Google Cloud (utilisez [un coupon de 300 $](https://cloud.google.com/free/) si vous ne l'avez pas déjà fait)
* Créez un nouveau projet et sauvegardez l'identifiant du projet (attendez un peu jusqu'à ce que le nouveau projet soit provisionné)

![Image](https://cdn-media-1.freecodecamp.org/images/KVrPVIYRVEWg6sHYA8ZHnkv91MnOjTO5Lu12)

![Image](https://cdn-media-1.freecodecamp.org/images/sgjnSYa-O3LobwJXb--UE0yXNAcS6IqJliNR)

* Créez un fichier app.yaml dans votre dossier principal avec le code suivant :

```
runtime: python27api_version: 1threadsafe: true
```

```
handlers:- url: /static  static_dir: static- url: /.*  script: main.app  libraries:  - name: ssl    version: latest
```

* Créez un fichier appengine_config.py dans votre dossier principal avec le code suivant :

```
from google.appengine.ext import vendor
```

```
# Add any libraries installed in the "lib" folder.vendor.add('lib')
```

* Répliquez les dépendances des bibliothèques dans le dossier lib

```
pip install -t lib -r requirements.txt
```

* Déployez sur Google Cloud en utilisant votre identifiant de projet sauvegardé (cela peut prendre 10 minutes). Utilisez les étapes suivantes :

```
gcloud auth application-default logingcloud config set project <PROJECT_ID>gcloud initgcloud app deploy app.yaml
```

* Profitez de votre application web en direct gratuitement. La mienne est [ici](https://weatherv2-220201.appspot.com/).

Le code complet est disponible sur [Github](https://github.com/tristanga/WeatherApp_FullCode). Merci d'avoir lu mon article. C'était ma première application web utilisant Flask et mon premier tutoriel sur [freeCodeCamp](https://medium.freecodecamp.org/). Si vous avez trouvé cet article utile, donnez-moi quelques applaudissements ?. C'était beaucoup plus facile que je ne le pensais, venant d'un milieu de Data Science avec Python et R.

N'hésitez pas à [me contacter](https://www.linkedin.com/in/tristanganry/) si vous souhaitez créer une application Flask simple ou plus complexe.