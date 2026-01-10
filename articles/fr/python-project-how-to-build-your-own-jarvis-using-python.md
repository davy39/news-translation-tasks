---
title: Projet Python – Comment créer le JARVIS de Tony Stark avec Python
subtitle: ''
author: Ashutosh Krishna
co_authors: []
series: null
date: '2021-12-09T17:19:31.000Z'
originalURL: https://freecodecamp.org/news/python-project-how-to-build-your-own-jarvis-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/png_20211209_232339_0000.png
tags:
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: Projet Python – Comment créer le JARVIS de Tony Stark avec Python
seo_desc: 'Do you remember J.A.R.V.I.S., Tony Stark''s virtual personal assistant?
  If you''ve seen any of the Ironman or Avengers movies, I''m sure you do.

  Have you ever wondered whether you could create your own personal assistant? Yes?
  Tony Stark can help us wit...'
---

Vous souvenez-vous de J.A.R.V.I.S., l'assistant personnel virtuel de Tony Stark ? Si vous avez vu l'un des films Iron Man ou Avengers, je suis sûr que oui.

Vous êtes-vous déjà demandé si vous pouviez créer votre propre assistant personnel ? Oui ? Tony Stark peut nous aider avec ça !

![Image](https://www.freecodecamp.org/news/content/images/2021/12/tony-snap2_rv5gmh.jpg)

Oups, aviez-vous oublié qu'il n'est plus là ? C'est triste qu'il ne puisse plus nous sauver. Mais hé, votre langage de programmation préféré, Python, peut vous aider pour cela.

Oui, vous avez bien entendu. Nous pouvons créer notre propre J.A.R.V.I.S. en utilisant Python. Plongeons-nous dedans !

## Configuration du projet

Pendant que vous coderez ce projet, vous rencontrerez divers modules et bibliothèques externes. Apprenons à les connaître et à les installer. Mais avant de les installer, créons un environnement virtuel et activons-le.

Nous allons créer un environnement virtuel en utilisant `virtualenv`. Python est désormais livré avec une bibliothèque `virtualenv` pré-installée. Ainsi, pour créer un environnement virtuel, vous pouvez utiliser la commande ci-dessous :

```bash
$ python -m venv env
```

La commande ci-dessus créera un environnement virtuel nommé `env`. Maintenant, nous devons activer l'environnement en utilisant la commande :

```bash
$ . env/Scripts/activate
```

Pour vérifier si l'environnement a été activé ou non, vous pouvez voir `(env)` dans votre terminal. Maintenant, nous pouvons installer les bibliothèques.

<ol>
	<li>
	<p><u><strong>pyttsx3</strong></u> :&nbsp;pyttsx est une bibliothèque de synthèse vocale multiplateforme qui est indépendante de la plateforme. Le principal avantage de l'utilisation de cette bibliothèque pour la conversion texte-parole est qu'elle fonctionne hors ligne. Pour installer ce module, tapez la commande ci-dessous dans le terminal :</p>

	<pre>
<code class="language-bash">$ pip install pyttsx3</code></pre>
	</li>
	<li><strong><u>SpeechRecognition</u></strong> :<strong>&nbsp;</strong>Cela nous permet de convertir l'audio en texte pour un traitement ultérieur. Pour installer ce module, tapez la commande ci-dessous dans le terminal :
	<pre>
<code class="language-bash">$ pip install SpeechRecognition</code></pre>
	</li>
	<li><u><strong>pywhatkit</strong></u> : Il s'agit d'une bibliothèque facile à utiliser qui nous aidera à interagir très facilement avec le navigateur. Pour installer le module, exécutez la commande suivante dans le terminal :
	<pre>
<code class="language-bash">$ pip install pywhatkit</code></pre>
	</li>
	<li><u><strong>wikipedia</strong></u> :&nbsp;Nous l'utiliserons pour récupérer diverses informations sur le site Web de Wikipédia. Pour installer ce module, tapez la commande ci-dessous dans le terminal :
	<pre>
<code class="language-bash">$ pip install wikipedia</code></pre>
	</li>
	<li><u><strong>requests</strong></u> : Il s'agit d'une bibliothèque HTTP élégante et simple pour Python qui&nbsp;vous permet d'envoyer des requêtes HTTP/1.1 extrêmement facilement. Pour installer le module, exécutez la commande suivante dans le terminal :
	<pre>
<code class="language-bash">$ pip install requests</code></pre>
	</li>
</ol>

### Fichier .env

Nous avons besoin de ce fichier pour stocker certaines données privées telles que les clés API, les mots de passe, etc., qui sont liées au projet. Pour l'instant, stockons le nom de l'utilisateur et du bot.

Créez un fichier nommé `.env` et ajoutez-y le contenu suivant :

```
USER=Ashutosh
BOTNAME=JARVIS
```

Pour utiliser le contenu du fichier `.env`, nous allons installer un autre module appelé **python-decouple** comme suit :

```bash
$ pip install python-decouple
```

En savoir plus sur les variables d'environnement en Python [ici](https://iread.ga/posts/49/do-you-really-need-environment-variables-in-python).

## Comment configurer JARVIS avec Python

Avant de commencer à définir quelques fonctions importantes, créons d'abord un moteur de parole.

```python
import pyttsx3
from decouple import config

USERNAME = config('USER')
BOTNAME = config('BOTNAME')


engine = pyttsx3.init('sapi5')

# Définir la vitesse
engine.setProperty('rate', 190)

# Définir le volume
engine.setProperty('volume', 1.0)

# Définir la voix (Féminine)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
```

Analysons le script ci-dessus. Tout d'abord, nous avons initialisé un moteur `engine` en utilisant le module `pyttsx3`. `sapi5` est une API de parole Microsoft qui nous aide à utiliser les voix. En savoir plus à ce sujet [ici](https://docs.microsoft.com/en-us/previous-versions/windows/desktop/ee125663(v=vs.85)). 

Ensuite, nous définissons les propriétés `rate` (vitesse) et `volume` du moteur de parole à l'aide de la méthode `setProperty`. 

Maintenant, nous pouvons obtenir les voix du moteur à l'aide de la méthode `getProperty`. `voices` sera une liste de voix disponibles dans notre système. Si nous l'affichons, nous pouvons voir ce qui suit :

```bash
[<pyttsx3.voice.Voice object at 0x000001AB9FB834F0>, <pyttsx3.voice.Voice object at 0x000001AB9FB83490>]
```

La première est une voix masculine et l'autre est une voix féminine. JARVIS était un assistant masculin dans les films, mais j'ai choisi de définir la propriété `voice` sur la voix féminine pour ce tutoriel en utilisant la méthode `setProperty`.

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">
<p><span style="color:#e74c3c">Note : Si vous obtenez une erreur liée à PyAudio, téléchargez le wheel PyAudio depuis </span><a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio"><span style="color:blue">ici</span></a>&nbsp;<span style="color:#e74c3c">et installez-le dans l'environnement virtuel.</span></p>
</div>

De plus, en utilisant la méthode `config` de _decouple_, nous récupérons la valeur de `USER` et `BOTNAME` à partir des variables d'environnement.

### Activer la fonction Speak

La fonction speak sera responsable de la lecture de tout texte qui lui est transmis. Voyons le code :

```python
# Conversion texte-parole
def speak(text):
    """Utilisé pour prononcer tout texte qui lui est transmis"""
    
    engine.say(text)
    engine.runAndWait()

```

Dans la méthode `speak()`, le moteur prononce le texte qui lui est transmis à l'aide de la méthode `say()`. En utilisant la méthode `runAndWait()`, il bloque pendant la boucle d'événements et revient lorsque la file d'attente des commandes est vidée.

### Activer la fonction Greet

Cette fonction sera utilisée pour saluer l'utilisateur chaque fois que le programme est exécuté. Selon l'heure actuelle, elle salue l'utilisateur par un _Bonjour_ (Good Morning), _Bon après-midi_ (Good Afternoon) ou _Bonsoir_ (Good Evening).

```python
from datetime import datetime


def greet_user():
    """Salue l'utilisateur selon l'heure"""
    
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Bonjour {USERNAME}")
    elif (hour >= 12) and (hour < 16):
        speak(f"Bon après-midi {USERNAME}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Bonsoir {USERNAME}")
    speak(f"Je suis {BOTNAME}. Comment puis-je vous aider ?")

```

Tout d'abord, nous obtenons l'heure actuelle, c'est-à-dire que si l'heure actuelle est 11h15, l'heure sera 11. Si la valeur de l'heure est comprise entre 6 et 12, on souhaite un Bonjour à l'utilisateur. Si la valeur est comprise entre 12 et 16, on souhaite un Bon après-midi et de même, si la valeur est comprise entre 16 et 19, on souhaite un Bonsoir. Nous utilisons la méthode speak pour parler à l'utilisateur.

### Comment prendre l'entrée de l'utilisateur

Nous utilisons cette fonction pour prendre les commandes de l'utilisateur et reconnaître la commande à l'aide du module `speech_recognition`.

```python
import speech_recognition as sr
from random import choice
from utils import opening_text


def take_user_input():
    """Prend l'entrée de l'utilisateur, la reconnaît à l'aide du module Speech Recognition et la convertit en texte"""

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Écoute....')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Reconnaissance...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Bonne nuit monsieur, prenez soin de vous !")
            else:
                speak('Passez une bonne journée monsieur !')
            exit()
    except Exception:
        speak('Désolé, je n\'ai pas compris. Pourriez-vous répéter s\'il vous plaît ?')
        query = 'None'
    return query
```

Nous avons importé le module `speech_recognition` sous le nom `sr`. La classe _Recognizer_ au sein du module `speech_recognition` nous aide à reconnaître l'audio. Le même module possède une classe _Microphone_ qui nous donne accès au microphone de l'appareil. Ainsi, avec le microphone comme `source`, nous essayons d'écouter l'audio en utilisant la méthode `listen()` de la classe _Recognizer_. 

Nous avons également défini le `pause_threshold` à 1, ce qui signifie qu'il ne se plaindra pas même si nous faisons une pause d'une seconde pendant que nous parlons.

Ensuite, en utilisant la méthode `recognize_google()` de la classe _Recognizer_, nous essayons de reconnaître l'audio. La méthode `recognize_google()` effectue la reconnaissance vocale sur l'audio qui lui est transmis, en utilisant l'**API Google Speech Recognition**. 

Nous avons défini la langue sur `en-in`, qui est l'anglais de l'Inde. Elle renvoie la transcription de l'audio qui n'est rien d'autre qu'une chaîne de caractères. Nous l'avons stockée dans une variable appelée `query`.

Si la requête contient les mots **exit** ou **stop**, cela signifie que nous demandons à l'assistant de s'arrêter immédiatement. Donc, avant de s'arrêter, nous saluons à nouveau l'utilisateur selon l'heure actuelle. Si l'heure est comprise entre 21h et 6h, on souhaite une _Bonne nuit_ à l'utilisateur, sinon, un autre message. 

Nous créons un fichier `utils.py` qui contient juste une liste avec quelques phrases comme celle-ci :

```python
opening_text = [
    "Cool, je m'en occupe monsieur.",
    "D'accord monsieur, j'y travaille.",
    "Juste une seconde monsieur.",
]
```

Si la requête ne contient pas ces deux mots (exit ou stop), nous disons quelque chose pour indiquer à l'utilisateur que nous l'avons entendu. Pour cela, nous utiliserons la méthode choice du module random pour sélectionner au hasard n'importe quelle phrase de la liste `opening_text`. Après avoir parlé, nous quittons le programme.

Pendant tout ce processus, si nous rencontrons une exception, nous nous excusons auprès de l'utilisateur et définissons la `query` sur None. À la fin, nous retournons la `query`.

## Comment configurer les fonctions hors ligne

À l'intérieur du dossier `functions`, créez un fichier Python appelé `os_ops.py`. Dans ce fichier, nous allons créer diverses fonctions pour interagir avec le système d'exploitation.

```python
import os
import subprocess as sp

paths = {
    'notepad': "C:\\Program Files\\Notepad++\\notepad++.exe",
    'discord': "C:\\Users\\ashut\\AppData\\Local\\Discord\\app-1.0.9003\\Discord.exe",
    'calculator': "C:\\Windows\\System32\\calc.exe"
}

```

Dans le script ci-dessus, nous avons créé un dictionnaire appelé `paths` qui contient le nom d'un logiciel comme clé et son chemin comme valeur. Vous pouvez modifier les chemins en fonction de votre système et ajouter d'autres chemins de logiciels si nécessaire.

### Comment ouvrir la caméra

Nous utiliserons cette fonction pour ouvrir la caméra de notre système. Nous utiliserons le module `subprocess` pour exécuter la commande.

```python
def open_camera():
    sp.run('start microsoft.windows.camera:', shell=True)
```

### Comment ouvrir le Bloc-notes et Discord

Nous utiliserons ces fonctions pour ouvrir Notepad++ et Discord dans le système.

```python
def open_notepad():
    os.startfile(paths['notepad'])


def open_discord():
    os.startfile(paths['discord'])
```

### Comment ouvrir l'invite de commande

Nous utiliserons cette fonction pour ouvrir l'invite de commande dans notre système.

```python
def open_cmd():
    os.system('start cmd')
```

### Comment ouvrir la calculatrice

Nous utiliserons cette fonction pour ouvrir la calculatrice sur notre système.

```python
def open_calculator():
    sp.Popen(paths['calculator'])
```

## Comment configurer les fonctions en ligne

Nous allons ajouter plusieurs fonctions en ligne. Elles sont :

1. Trouver mon adresse IP
2. Rechercher sur Wikipédia
3. Lire des vidéos sur YouTube
4. Rechercher sur Google
5. Envoyer un message WhatsApp
6. Envoyer un e-mail
7. Obtenir les dernières manchettes
8. Obtenir le rapport météo
9. Obtenir les films du moment
10. Obtenir des blagues aléatoires
11. Obtenir des conseils aléatoires

Créons un fichier appelé `online_ops.py` dans le répertoire `functions`, et commençons à créer ces fonctions les unes après les autres. Pour l'instant, ajoutez le code suivant dans le fichier :

```python
import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
```

Avant de commencer à travailler avec les API, si vous n'êtes pas familier avec les API et comment interagir avec elles en utilisant Python, consultez [ce tutoriel](https://iread.ga/posts/26/python-api-tutorial).

### Comment ajouter la fonction Trouver mon adresse IP

[ipify](https://www.ipify.org/) fournit une API d'adresse IP publique simple. Nous avons juste besoin de faire une requête GET sur cette URL : [https://api64.ipify.org/?format=json](https://api64.ipify.org/?format=json). Elle renvoie des données JSON comme suit :

```json
{
  "ip": "117.214.111.199"
}
```

Nous pouvons alors simplement renvoyer l'`ip` à partir des données JSON. Alors, créons cette méthode :

```python
def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]
```

### Comment ajouter la fonction Recherche sur Wikipédia

Pour effectuer une recherche sur Wikipédia, nous utiliserons le module `wikipedia` que nous avons installé plus tôt dans ce tutoriel.

```python
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results
```

À l'intérieur du module `wikipedia`, nous avons une méthode `summary()` qui accepte une requête comme argument. De plus, nous pouvons également passer le nombre de phrases requises. Ensuite, nous retournons simplement le résultat.

### Comment ajouter la fonction Lire des vidéos sur YouTube

Pour lire des vidéos sur YouTube, nous utilisons _PyWhatKit_. Nous l'avons déjà importé sous le nom `kit`.

```python
def play_on_youtube(video):
    kit.playonyt(video)
```

_PyWhatKit_ possède une méthode `playonyt()` qui accepte un sujet comme argument. Elle recherche ensuite le sujet sur YouTube et lit la vidéo la plus appropriée. Elle utilise [PyAutoGUI](https://pyautogui.readthedocs.io/en/latest/) en coulisses.

### Comment ajouter la fonction Recherche sur Google

Encore une fois, nous utiliserons _PyWhatKit_ pour effectuer des recherches sur Google.

```python
def search_on_google(query):
    kit.search(query)
```

Il possède une méthode `search()` qui nous aide à effectuer des recherches sur Google instantanément.

### Comment ajouter la fonction Envoyer un message WhatsApp

Nous utiliserons _PyWhatKit_ une fois de plus pour envoyer des messages WhatsApp.

```python
def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)
```

Notre méthode accepte deux arguments – le numéro de téléphone `number` et le `message`. Elle appelle ensuite la méthode `sendwhatmsg_instantly()` pour envoyer un message WhatsApp. Assurez-vous d'être déjà connecté à votre compte WhatsApp sur WhatsApp for Web.

### Comment ajouter la fonction Envoyer un e-mail

Pour envoyer des e-mails, nous utiliserons le module intégré `smtplib` de Python.

```python
EMAIL = config("EMAIL")
PASSWORD = config("PASSWORD")


def send_email(receiver_address, subject, message):
    try:
        email = EmailMessage()
        email['To'] = receiver_address
        email["Subject"] = subject
        email['From'] = EMAIL
        email.set_content(message)
        s = smtplib.SMTP("smtp.gmail.com", 587)
        s.starttls()
        s.login(EMAIL, PASSWORD)
        s.send_message(email)
        s.close()
        return True
    except Exception as e:
        print(e)
        return False
```

La méthode accepte `receiver_address`, `subject` et `message` comme arguments. Nous créons un objet de la classe _SMTP_ à partir du module `smtplib`. Il prend l'**hôte** et le **numéro de port** comme paramètres. 

Nous démarrons ensuite une session, nous nous connectons avec l'adresse e-mail et le mot de passe et nous envoyons l'e-mail. Assurez-vous d'ajouter **EMAIL** et **PASSWORD** dans le fichier `.env`.

### Comment ajouter la fonction Obtenir les dernières manchettes

Pour récupérer les dernières manchettes de l'actualité, nous utiliserons [NewsAPI](https://newsapi.org/). Inscrivez-vous pour un compte gratuit sur NewsAPI et obtenez la clé API. Ajoutez la **NEWS_API_KEY** dans le fichier `.env`.

```python
NEWS_API_KEY = config("NEWS_API_KEY")


def get_latest_news():
    news_headlines = []
    res = requests.get(
        f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}&category=general").json()
    articles = res["articles"]
    for article in articles:
        news_headlines.append(article["title"])
    return news_headlines[:5]
```

Dans la méthode ci-dessus, nous créons d'abord une liste vide appelée `news_headlines`. Nous effectuons ensuite une requête GET sur l'URL de l'API spécifiée dans la [Documentation NewsAPI](https://newsapi.org/docs). Un exemple de réponse JSON de la requête ressemble à ceci :

```json
{
  "status": "ok",
  "totalResults": 38,
  "articles": [
    {
      "source": {
        "id": null,
        "name": "Sportskeeda"
      },
      "author": "Aniket Thakkar",
      "title": "Latest Free Fire redeem code to get Weapon loot crate today (14 October 2021) - Sportskeeda",
      "description": "Gun crates are one of the ways that players in Free Fire can obtain impressive and appealing gun skins.",
      "url": "https://www.sportskeeda.com/free-fire/latest-free-fire-redeem-code-get-weapon-loot-crate-today-14-october-2021",
      "urlToImage": "https://staticg.sportskeeda.com/editor/2021/10/d0b83-16341799119781-1920.jpg",
      "publishedAt": "2021-10-14T03:51:50Z",
      "content": null
    },
    {
      "source": {
        "id": null,
        "name": "NDTV News"
      },
      "author": null,
      "title": "BSF Gets Increased Powers In 3 Border States: What It Means - NDTV",
      "description": "Border Security Force (BSF) officers will now have the power toarrest, search, and of seizure to the extent of 50 km inside three newstates sharing international boundaries with Pakistan and Bangladesh.",
      "url": "https://www.ndtv.com/india-news/bsf-gets-increased-powers-in-3-border-states-what-it-means-2574644",
      "urlToImage": "https://c.ndtvimg.com/2021-08/eglno7qk_-bsf-recruitment-2021_625x300_10_August_21.jpg",
      "publishedAt": "2021-10-14T03:44:00Z",
      "content": "This move is quickly snowballing into a debate on state autonomy. New Delhi: Border Security Force (BSF) officers will now have the power to arrest, search, and of seizure to the extent of 50 km ins… [+4143 chars]"
    },
    {
      "source": {
        "id": "the-times-of-india",
        "name": "The Times of India"
      },
      "author": "TIMESOFINDIA.COM",
      "title": "5 health conditions that can make your joints hurt - Times of India",
      "description": "Joint pain caused by these everyday issues generally goes away on its own when you stretch yourself a little and flex your muscles.",
      "url": "https://timesofindia.indiatimes.com/life-style/health-fitness/health-news/5-health-conditions-that-can-make-your-joints-hurt/photostory/86994969.cms",
      "urlToImage": "https://static.toiimg.com/photo/86995017.cms",
      "publishedAt": "2021-10-14T03:30:00Z",
      "content": "Depression is a mental health condition, but the symptoms may manifest even on your physical health. Unexpected aches and pain in the joints that you may experience when suffering from chronic depres… [+373 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "The Indian Express"
      },
      "author": "Devendra Pandey",
      "title": "Rahul Dravid likely to be interim coach for New Zealand series - The Indian Express",
      "description": "It’s learnt that a few Australian coaches expressed interest in the job, but the BCCI isn’t keen as they are focussing on an Indian for the role, before they look elsewhere.",
      "url": "https://indianexpress.com/article/sports/cricket/rahul-dravid-likely-to-be-interim-coach-for-new-zealand-series-7570990/",
      "urlToImage": "https://images.indianexpress.com/2021/05/rahul-dravid.jpg",
      "publishedAt": "2021-10-14T03:26:09Z",
      "content": "Rahul Dravid is likely to be approached by the Indian cricket board to be the interim coach for Indias home series against New Zealand. Head coach Ravi Shastri and the core of the support staff will … [+1972 chars]"
    },
    {
      "source": {
        "id": null,
        "name": "CNBCTV18"
      },
      "author": null,
      "title": "Thursday's top brokerage calls: Infosys, Wipro and more - CNBCTV18",
      "description": "Goldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:",
      "url": "https://www.cnbctv18.com/market/stocks/thursdays-top-brokerage-calls-infosys-wipro-and-more-11101072.htm",
      "urlToImage": "https://images.cnbctv18.com/wp-content/uploads/2019/03/buy-sell.jpg",
      "publishedAt": "2021-10-14T03:26:03Z",
      "content": "MiniGoldman Sachs has maintained its 'sell' rating on Mindtree largely due to expensive valuations, while UBS expects a muted reaction from Wipro's stock. Here are the top brokerage calls for the day:"
    }
  ]
}

```

Comme les actualités sont contenues dans une liste appelée `articles`, nous créons une variable `articles` avec la valeur `res['articles']`. Maintenant, nous itérons sur cette liste `articles` et ajoutons le `article["title"]` à la liste `news_headlines`. Nous retournons ensuite les cinq premières manchettes de cette liste.

### Comment ajouter la fonction Obtenir le rapport météo

Pour obtenir le rapport météo, nous utilisons l'[API OpenWeatherMap](https://openweathermap.org/). Inscrivez-vous pour un compte gratuit et obtenez l'APP ID. Assurez-vous d'ajouter l'**OPENWEATHER_APP_ID** dans le fichier `.env`.

```python
OPENWEATHER_APP_ID = config("OPENWEATHER_APP_ID")


def get_weather_report(city):
    res = requests.get(
        f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={OPENWEATHER_APP_ID}&units=metric").json()
    weather = res["weather"][0]["main"]
    temperature = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temperature}℃", f"{feels_like}℃"
```

Conformément à l'[API OpenWeatherMap](https://openweathermap.org/current), nous devons effectuer une requête GET sur l'URL mentionnée ci-dessus avec le nom de la ville. Nous obtiendrons une réponse JSON comme suit :

```json
{
    "coord": {
        "lon": 85,
        "lat": 24.7833
    },
    "weather": [
        {
            "id": 721,
            "main": "Haze",
            "description": "haze",
            "icon": "50d"
        }
    ],
    "base": "stations",
    "main": {
        "temp": 26.95,
        "feels_like": 26.64,
        "temp_min": 26.95,
        "temp_max": 26.95,
        "pressure": 1011,
        "humidity": 36
    },
    "visibility": 3000,
    "wind": {
        "speed": 2.57,
        "deg": 310
    },
    "clouds": {
        "all": 57
    },
    "dt": 1637227634,
    "sys": {
        "type": 1,
        "id": 9115,
        "country": "IN",
        "sunrise": 1637195904,
        "sunset": 1637235130
    },
    "timezone": 19800,
    "id": 1271439,
    "name": "Gaya",
    "cod": 200
}
```

Nous n'aurons besoin que de `weather`, `temperature` et `feels_like` de la réponse ci-dessus.

### Comment ajouter la fonction Obtenir les films du moment

Pour obtenir les films du moment, nous utiliserons l'API de [The Movie Database (TMDB)](https://www.themoviedb.org/). Inscrivez-vous pour un compte gratuit et obtenez la clé API. Ajoutez la **TMDB_API_KEY** dans le fichier `.env`.

```python
TMDB_API_KEY = config("TMDB_API_KEY")


def get_trending_movies():
    trending_movies = []
    res = requests.get(
        f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
    results = res["results"]
    for r in results:
        trending_movies.append(r["original_title"])
    return trending_movies[:5]
```

Tout comme nous l'avons fait pour les dernières manchettes, nous créons la liste `trending_movies`. Ensuite, conformément à l'API TMDB, nous effectuons une requête GET. Un exemple de réponse JSON ressemble à ceci :

```json
{
  "page": 1,
  "results": [
    {
      "video": false,
      "vote_average": 7.9,
      "overview": "Shang-Chi must confront the past he thought he left behind when he is drawn into the web of the mysterious Ten Rings organization.",
      "release_date": "2021-09-01",
      "title": "Shang-Chi and the Legend of the Ten Rings",
      "adult": false,
      "backdrop_path": "/cinER0ESG0eJ49kXlExM0MEWGxW.jpg",
      "vote_count": 2917,
      "genre_ids": [28, 12, 14],
      "id": 566525,
      "original_language": "en",
      "original_title": "Shang-Chi and the Legend of the Ten Rings",
      "poster_path": "/1BIoJGKbXjdFDAqUEiA2VHqkK1Z.jpg",
      "popularity": 9559.446,
      "media_type": "movie"
    },
    {
      "adult": false,
      "backdrop_path": "/dK12GIdhGP6NPGFssK2Fh265jyr.jpg",
      "genre_ids": [28, 35, 80, 53],
      "id": 512195,
      "original_language": "en",
      "original_title": "Red Notice",
      "overview": "An Interpol-issued Red Notice is a global alert to hunt and capture the world's most wanted. But when a daring heist brings together the FBI's top profiler and two rival criminals, there's no telling what will happen.",
      "poster_path": "/wdE6ewaKZHr62bLqCn7A2DiGShm.jpg",
      "release_date": "2021-11-04",
      "title": "Red Notice",
      "video": false,
      "vote_average": 6.9,
      "vote_count": 832,
      "popularity": 1990.503,
      "media_type": "movie"
    },
    {
      "genre_ids": [12, 28, 53],
      "original_language": "en",
      "original_title": "No Time to Die",
      "poster_path": "/iUgygt3fscRoKWCV1d0C7FbM9TP.jpg",
      "video": false,
      "vote_average": 7.6,
      "overview": "Bond has left active service and is enjoying a tranquil life in Jamaica. His peace is short-lived when his old friend Felix Leiter from the CIA turns up asking for help. The mission to rescue a kidnapped scientist turns out to be far more treacherous than expected, leading Bond onto the trail of a mysterious villain armed with dangerous new technology.",
      "id": 370172,
      "vote_count": 1804,
      "title": "No Time to Die",
      "adult": false,
      "backdrop_path": "/1953j0QEbtN17WFFTnJHIm6bn6I.jpg",
      "release_date": "2021-09-29",
      "popularity": 4639.439,
      "media_type": "movie"
    },
    {
      "poster_path": "/5pVJ9SuuO72IgN6i9kMwQwnhGHG.jpg",
      "video": false,
      "vote_average": 0,
      "overview": "Peter Parker is unmasked and no longer able to separate his normal life from the high-stakes of being a Super Hero. When he asks for help from Doctor Strange the stakes become even more dangerous, forcing him to discover what it truly means to be Spider-Man.",
      "release_date": "2021-12-15",
      "id": 634649,
      "adult": false,
      "backdrop_path": "/vK18znei8Uha2z7ZhZtBa40HIrm.jpg",
      "vote_count": 0,
      "genre_ids": [28, 12, 878],
      "title": "Spider-Man: No Way Home",
      "original_language": "en",
      "original_title": "Spider-Man: No Way Home",
      "popularity": 1084.815,
      "media_type": "movie"
    },
    {
      "video": false,
      "vote_average": 6.8,
      "overview": "After finding a host body in investigative reporter Eddie Brock, the alien symbiote must face a new enemy, Carnage, the alter ego of serial killer Cletus Kasady.",
      "release_date": "2021-09-30",
      "adult": false,
      "backdrop_path": "/70nxSw3mFBsGmtkvcs91PbjerwD.jpg",
      "vote_count": 1950,
      "genre_ids": [878, 28, 12],
      "id": 580489,
      "original_language": "en",
      "original_title": "Venom: Let There Be Carnage",
      "poster_path": "/rjkmN1dniUHVYAtwuV3Tji7FsDO.jpg",
      "title": "Venom: Let There Be Carnage",
      "popularity": 4527.568,
      "media_type": "movie"
    }
  ],
  "total_pages": 1000,
  "total_results": 20000
}

```

À partir de la réponse ci-dessus, nous avons juste besoin du titre du film. Nous obtenons les `results` qui sont une liste, puis nous itérons dessus pour obtenir le titre du film et l'ajouter à la liste `trending_movies`. À la fin, nous retournons les cinq premiers éléments de la liste.

### Comment ajouter la fonction Obtenir des blagues aléatoires

Pour obtenir une blague aléatoire, nous avons juste besoin de faire une requête GET sur cette URL : [https://icanhazdadjoke.com/](https://icanhazdadjoke.com/).

```python
def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]
```

### Comment ajouter la fonction Obtenir des conseils aléatoires

Pour obtenir un conseil aléatoire, nous utilisons l'[API Advice Slip](https://api.adviceslip.com/).

```python
def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']

```

## Comment créer la méthode principale

Pour exécuter le projet, nous devrons créer une méthode principale. Créez un fichier `main.py` et ajoutez le code suivant :

```python
import requests
from functions.online_ops import find_my_ip, get_latest_news, get_random_advice, get_random_joke, get_trending_movies, get_weather_report, play_on_youtube, search_on_google, search_on_wikipedia, send_email, send_whatsapp_message
from functions.os_ops import open_calculator, open_camera, open_cmd, open_notepad, open_discord
from pprint import pprint


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'ouvrir le bloc-notes' in query:
            open_notepad()

        elif 'ouvrir discord' in query:
            open_discord()

        elif 'ouvrir l\'invite de commande' in query or 'ouvrir cmd' in query:
            open_cmd()

        elif 'ouvrir la caméra' in query:
            open_camera()

        elif 'ouvrir la calculatrice' in query:
            open_calculator()

        elif 'adresse ip' in query:
            ip_address = find_my_ip()
            speak(f'Votre adresse IP est {ip_address}.\n Pour votre commodité, je l\'affiche sur l\'écran monsieur.')
            print(f'Votre adresse IP est {ip_address}')

        elif 'wikipedia' in query:
            speak('Que voulez-vous rechercher sur Wikipédia, monsieur ?')
            search_query = take_user_input().lower()
            results = search_on_wikipedia(search_query)
            speak(f"Selon Wikipédia, {results}")
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            print(results)

        elif 'youtube' in query:
            speak('Que voulez-vous lire sur Youtube, monsieur ?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'rechercher sur google' in query:
            speak('Que voulez-vous rechercher sur Google, monsieur ?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "envoyer un message whatsapp" in query:
            speak('À quel numéro dois-je envoyer le message monsieur ? Veuillez l\'entrer dans la console : ')
            number = input("Entrez le numéro : ")
            speak("Quel est le message monsieur ?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("J\'ai envoyé le message monsieur.")

        elif "envoyer un e-mail" in query:
            speak("À quelle adresse e-mail dois-je l\'envoyer monsieur ? Veuillez l\'entrer dans la console : ")
            receiver_address = input("Entrez l\'adresse e-mail : ")
            speak("Quel devrait être l\'objet monsieur ?")
            subject = take_user_input().capitalize()
            speak("Quel est le message monsieur ?")
            message = take_user_input().capitalize()
            if send_email(receiver_address, subject, message):
                speak("J\'ai envoyé l\'e-mail monsieur.")
            else:
                speak("Quelque chose s\'est mal passé pendant que j\'envoyais le mail. Veuillez vérifier les journaux d\'erreurs monsieur.")

        elif 'blague' in query:
            speak(f"J\'espère que vous aimerez celle-ci monsieur")
            joke = get_random_joke()
            speak(joke)
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            pprint(joke)

        elif "conseil" in query:
            speak(f"Voici un conseil pour vous, monsieur")
            advice = get_random_advice()
            speak(advice)
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            pprint(advice)

        elif "films du moment" in query:
            speak(f"Certains des films du moment sont : {get_trending_movies()}")
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            print(*get_trending_movies(), sep='\n')

        elif 'actualités' in query:
            speak(f"Je lis les dernières manchettes de l\'actualité, monsieur")
            speak(get_latest_news())
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            print(*get_latest_news(), sep='\n')

        elif 'météo' in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Obtention du rapport météo pour votre ville {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"La température actuelle est de {temperature}, mais on dirait qu\'il fait {feels_like}")
            speak(f"De plus, le rapport météo parle de {weather}")
            speak("Pour votre commodité, je l\'affiche sur l\'écran monsieur.")
            print(f"Description : {weather}\nTempérature : {temperature}\nRessenti : {feels_like}")
```

Bien que le script ci-dessus semble assez long, il est très simple et facile à comprendre.

Si vous regardez de plus près, tout ce que nous avons fait est d'importer les modules requis et les fonctions en ligne et hors ligne. Ensuite, à l'intérieur de la méthode principale, la première chose que nous faisons est de saluer l'utilisateur à l'aide de la fonction `greet_user()`.

Ensuite, nous lançons une boucle while pour prendre continuellement les entrées de l'utilisateur à l'aide de la fonction `take_user_input()`. Puisque nous avons notre chaîne de requête ici, nous pouvons ajouter une structure if-else pour vérifier les différentes conditions sur la chaîne `query`.

<div style="background:#eeeeee; border:1px solid #cccccc; padding:5px 10px">Note : Pour Python 3.10, vous pouvez utiliser <a href="https://www.python.org/dev/peps/pep-0636/" style="color:blue;">Python Match Case</a>&nbsp;au lieu de la structure if-else.</div>

Pour exécuter le programme, vous pouvez utiliser la commande suivante :

```bash
$ python main.py
```

## Conclusion

Nous venons de créer notre propre assistant personnel virtuel à l'aide de Python. Vous pouvez ajouter plus de fonctionnalités à l'application si vous le souhaitez. Vous pouvez ajouter ce projet à votre CV ou simplement le faire pour le plaisir !

Regardez la vidéo de démonstration pour le voir en action :

%[https://player.vimeo.com/video/650156113?h=9adb36534c]

Pour le code complet, consultez ce dépôt GitHub : [https://github.com/ashutoshkrris/Virtual-Personal-Assistant-using-Python](https://github.com/ashutoshkrris/Virtual-Personal-Assistant-using-Python)