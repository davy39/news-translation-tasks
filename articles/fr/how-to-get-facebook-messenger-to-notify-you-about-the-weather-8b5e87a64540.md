---
title: Comment faire pour que Facebook Messenger vous envoie des notifications sur
  la météo
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-24T18:22:42.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-facebook-messenger-to-notify-you-about-the-weather-8b5e87a64540
coverImage: https://cdn-media-1.freecodecamp.org/images/1*RBHbkOfMOzl7o_crT4Rg7g.jpeg
tags:
- name: Facebook Messenger
  slug: facebook-messenger
- name: bots
  slug: bots
- name: how-to
  slug: how-to
- name: Python
  slug: python
- name: weather
  slug: weather
seo_title: Comment faire pour que Facebook Messenger vous envoie des notifications
  sur la météo
seo_desc: 'By Ekapope Viriyakovithya

  A complete DIY guide to build your own weather alert bot.

  The morning routine is always stressful. Wouldn’t it be wonderful if you had one
  less thing to worry about in the morning?

  What if you had a customizable weather aler...'
---

Par Ekapope Viriyakovithya

### Un guide DIY complet pour créer votre propre bot d'alerte météo.

La routine du matin est toujours stressante. Ne serait-ce pas merveilleux si vous aviez une chose de moins à vous soucier le matin ?

Et si vous aviez un bot d'alerte météo personnalisable qui vous envoyait un message court UNIQUEMENT lorsqu'il y avait une chance de pluie au-dessus de votre seuil prédéfinie ?

Ne perdez pas votre temps à vérifier la météo dans une application séparée. Elle peut être en direct dans votre boîte de chat Facebook Messenger !

### De quoi avez-vous besoin ?

* Python 3.6 (ou une version antérieure) avec les packages pandas et [fbchat](https://github.com/carpedm20/fbchat) installés

```bash
pip install fbchat
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uy6HxLRFNAOcpu40NDfXSw.png)
_Compte AccuWeather gratuit_

* [Compte développeur AccuWeather](https://developer.accuweather.com/packages), le package gratuit devrait suffire. Il offre 50 appels/jour avec 1 clé/compte développeur.

### Commençons !

À la fin de ce guide, vous aurez 3 fichiers dans le dossier scripts :

[keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/tree/master/scripts) : pour stocker votre email Facebook, votre mot de passe et votre clé API AccuWeather

[params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) : pour stocker le seuil et l'identifiant de l'emplacement de la prévision météo

[main.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/main.py) : c'est le script principal, il appellera keys.py et params.py

#### 1. Configuration du compte Facebook et de la clé API AccuWeather

Tout d'abord, mettons les détails de votre compte dans le fichier [keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/keys.py).

```py
# Votre nom d'utilisateur Facebook (email)
FB_USERNAME= "" 

# Votre mot de passe Facebook
FB_PASSWORD= "" 

# Votre clé API AccuWeather
ACCUWEATHER_API_KEY= ""
```

#### **2. Configuration des paramètres**

Dans cette étape, nous allons définir le seuil de probabilité de pluie ou de neige, le temps de délai entre chaque demande et message, ainsi que l'emplacement.

Actuellement, nous fixons le seuil à 25 % pour la pluie et la neige. Nous recevrons le message d'alerte uniquement si les données AccuWeather montrent une probabilité ≥ 25 %.

Les scripts ci-dessous demanderont des données à AccuWeather toutes les 1 heure (UPDATE_INTERVAL_HR= 1) et enverront un message toutes les 4 heures (DELAY_TIME_HR= 4).

Ces paramètres seront stockés dans le fichier [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py).

```py
# Définir le seuil de % pour la probabilité de pluie et de neige. 
# Le message sera envoyé si le % de chance dépasse la valeur
RAIN_THRESHOLD = 25
SNOW_THRESHOLD = 25

# temps entre les demandes Accuweather (en heures)
UPDATE_INTERVAL_HR = 1 

# temps de délai entre les messages (en heures)
DELAY_TIME_HR = 4 

# identifiant de l'emplacement
# par exemple, https://www.accuweather.com/en/fr/lille/135564/weather-forecast/135564
# l'identifiant de l'emplacement est 135564
LOCATION_ID = "135564" 
```

#### 3. Récupérer les données d'AccuWeather

Maintenant, voici la partie amusante. Nous allons maintenant travailler sur le script principal.

Si vous prévoyez de l'exécuter localement, configurez votre répertoire et importez les clés et les paramètres. Assurez-vous de mettre [keys.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/keys.py) et [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) dans le même dossier que ce script [main.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/main.py).

```py
# définir le répertoire courant
import os
os.chdir(r".\YOUR_PATH")
###############################################################################
# importer les clés et les paramètres des autres scripts dans le même dossier
from keys import FB_USERNAME,FB_PASSWORD,ACCUWEATHER_API_KEY
from params import RAIN_THRESHOLD,SNOW_THRESHOLD,UPDATE_INTERVAL_HR,DELAY_TIME_HR,LOCATION_ID

```

Importer les modules requis.

```py
# importer les modules requis
import urllib
import urllib.parse
import json
import time
import requests
import pandas as pd
import logging
import sys
from fbchat import Client
from fbchat.models import *
from datetime import datetime
```

Définir l'URL de la page à demander, dans cet exemple, nous allons récupérer les prévisions horaires sur 12 heures. Convertir notre temps de mise à jour/délai en secondes.

```py
url_page = "http://dataservice.accuweather.com/forecasts/v1/hourly/12hour/"+str(LOCATION_ID)+"?apikey="+ACCUWEATHER_API_KEY+"&details=true&metric=true"
# convertir les heures en secondes
update_interval_sec = 60*60*UPDATE_INTERVAL_HR 
delay_time_sec = 60*60*DELAY_TIME_HR 
```

Ensuite, demander les données et les mettre dans un DataFrame pandas appelé 'json_df'.

À ce stade, nous pouvons inspecter la table récupérée. Extraire et renommer les éléments dont nous avons besoin. Dans cet exemple, nous aurons besoin du lien AccuWeather, du % de pluie, du % de neige, de la date et de l'heure au format souhaité.

```py
    json_page = urllib.request.urlopen(url_page)
    json_data = json.loads(json_page.read().decode())
    json_df = pd.DataFrame(json_data)
    
    # définir la largeur maximale, afin que les liens soient entièrement affichés et cliquables
    pd.set_option('display.max_colwidth', -1)
    json_df['Links'] = json_df['MobileLink'].apply(lambda x: '<a href='+x+'>Link</a>')
    
    json_df['Real Feel (degC)'] = json_df['RealFeelTemperature'].apply(lambda x: x.get('Value'))
    json_df['Weather'] = json_df['IconPhrase'] 
    json_df['Percent_Rain'] = json_df['RainProbability'] 
    json_df['Percent_Snow'] = json_df['SnowProbability'] 
```

Si nous regardons de plus près, la colonne 'DateTime' est un peu délicate à extraire et nécessite un peu de travail. Après le nettoyage, sauvegardez-la dans la variable 'current_retrieved_datetime'.

```py
json_df[['Date','Time']] = json_df['DateTime'].str.split('T', expand=True)
# rogner l'heure au format hh:mm, changer en str
json_df[['Time']] = json_df['Time'].str.split('+', expand=True)[0].astype(str).str[:5]

current_retrieved_datetime = str(json_df['Date'][0])+' '+str(json_df['Time'][0])
```

Ensuite, écrivez une condition if-else pour personnaliser le message d'alerte. La table récupérée nous fournit une prévision sur 12 heures. Nous allons vérifier chaque élément des colonnes de pluie et de neige et retourner un message si la probabilité est supérieure au seuil.

Tout d'abord, initialisez le message d'alerte pour chaque cas.

```py
rain_msg=""
snow_msg=""
```

Vérifiez les colonnes 'Percent_Rain' et 'Percent_Snow', marquez avec 1 si le % de probabilité est supérieur au seuil (ou 0 sinon).

Faites la somme des colonnes et modifiez 'rain_msg' et 'snow_msg'.

```py
    # vérifier la colonne % Rain, retourner rain_msg
    json_df.loc[json_df['Percent_Rain'] >= RAIN_THRESHOLD, 'Rain_Alert'] = 1  
    json_df.loc[json_df['Percent_Rain'] < RAIN_THRESHOLD, 'Rain_Alert'] = 0
    if (sum(json_df['Rain_Alert']) > 0):
        rain_msg = 'Il y a ' \
                    +str(json_df['Percent_Rain'][json_df['Rain_Alert']==1][0]) \
                    +' % de chance de pluie' \
                    +' à ' \
                    +str(json_df['Time'][json_df['Rain_Alert']==1][0])
    
    # vérifier la colonne % Snow
    json_df.loc[json_df['Percent_Snow'] >= SNOW_THRESHOLD, 'Snow_Alert'] = 1  
    json_df.loc[json_df['Percent_Snow'] < SNOW_THRESHOLD, 'Snow_Alert'] = 0
    if (sum(json_df['Snow_Alert']) > 0):
        snow_msg = 'Il y a ' \
                    +str(json_df['Percent_Snow'][json_df['Percent_Snow']==1][0]) \
                    +' % de chance de neige' \
                    +' à ' \
                    +str(json_df['Time'][json_df['Percent_Snow']==1][0])
```

Initialisez 'alert_msg', modifiez les messages s'il y a un 'rain_msg' ou un 'snow_msg'.

```py
alert_msg =""
if(len(rain_msg)|len(snow_msg)!=0):
     alert_msg = rain_msg +" "+snow_msg
```

Ajoutez le lien à la variable 'link_for_click', celui-ci sera joint au message lorsque nous l'enverrons plus tard.

```py
link_for_click = json_df['MobileLink'][0]
```

Jusqu'à ce point, nous pouvons maintenant les envelopper dans une fonction. Ne vous inquiétez pas si vous êtes perdu, je les ai rassemblés ci-dessous.

```py
def func_get_weather(url_page):

    json_page = urllib.request.urlopen(url_page)
    json_data = json.loads(json_page.read().decode())
    json_df = pd.DataFrame(json_data)
    
    # définir la largeur maximale, afin que les liens soient entièrement affichés et cliquables
    pd.set_option('display.max_colwidth', -1)
    json_df['Links'] = json_df['MobileLink'].apply(lambda x: '<a href='+x+'>Link</a>')
    
    json_df['Real Feel (degC)'] = json_df['RealFeelTemperature'].apply(lambda x: x.get('Value'))
    json_df['Weather'] = json_df['IconPhrase'] 
    json_df['Percent_Rain'] = json_df['RainProbability'] 
    json_df['Percent_Snow'] = json_df['SnowProbability'] 
    json_df[['Date','Time']] = json_df['DateTime'].str.split('T', expand=True)
    # rogner l'heure au format hh:mm, changer en str
    json_df[['Time']] = json_df['Time'].str.split('+', expand=True)[0].astype(str).str[:5]
    
    current_retrieved_datetime = str(json_df['Date'][0])+' '+str(json_df['Time'][0])
    
    rain_msg=""
    snow_msg=""
    
    # vérifier la colonne % Rain, retourner rain_msg
    json_df.loc[json_df['Percent_Rain'] >= RAIN_THRESHOLD, 'Rain_Alert'] = 1  
    json_df.loc[json_df['Percent_Rain'] < RAIN_THRESHOLD, 'Rain_Alert'] = 0
    if (sum(json_df['Rain_Alert']) > 0):
        rain_msg = 'Il y a ' \
                    +str(json_df['Percent_Rain'][json_df['Rain_Alert']==1][0]) \
                    +' % de chance de pluie' \
                    +' à ' \
                    +str(json_df['Time'][json_df['Rain_Alert']==1][0])
    
    # vérifier la colonne % Snow
    json_df.loc[json_df['Percent_Snow'] >= SNOW_THRESHOLD, 'Snow_Alert'] = 1  
    json_df.loc[json_df['Percent_Snow'] < SNOW_THRESHOLD, 'Snow_Alert'] = 0
    if (sum(json_df['Snow_Alert']) > 0):
        snow_msg = 'Il y a ' \
                    +str(json_df['Percent_Snow'][json_df['Percent_Snow']==1][0]) \
                    +' % de chance de neige' \
                    +' à ' \
                    +str(json_df['Time'][json_df['Percent_Snow']==1][0])

    alert_msg =""
    if(len(rain_msg)|len(snow_msg)!=0):
         alert_msg = rain_msg +" "+snow_msg
    
    link_for_click = json_df['MobileLink'][0]
    
    return(current_retrieved_datetime,alert_msg,link_for_click)
```

#### 4. Boucle automatisée

Enfin, pour la dernière partie, nous allons automatiser le processus en utilisant des boucles. Les scripts ci-dessous mettent le nombre de boucles à 'num_repeat = 999'.

```py
num_repeat = 999 # nombre de boucles à répéter
previous_alert_msg = "" # initialiser le message d'alerte
```

Utilisez try et except pour surmonter les erreurs (au cas où quelque chose ne va pas avec les connexions). Appelez la fonction 'func_get_weather' et attribuez-la à des variables.

```py
for i in range(num_repeat):
    try:
        current_retrieved_datetime,alert_msg,link_for_click = func_get_weather(url_page)
    except (RuntimeError, TypeError, NameError, ValueError, urllib.error.URLError):
        print('erreur attrapée')
```

Ensuite, vérifiez s'il y a des changements dans la météo. Si rien n'a changé, affichez le message à l'écran. Aucun message de chat ne sera envoyé.

```py
    # si la prévision météo n'a pas changé, aucun message d'alerte ne sera envoyé
    if len(alert_msg) > 0 and previous_alert_msg == alert_msg:
        print(i, current_retrieved_datetime, 'aucun changement dans la prévision météo')
```

Le message ne sera envoyé que s'il y a un changement dans la météo.

Nous pouvons finaliser notre message à ce stade. Récupérez l'identifiant de l'utilisateur de vos amis et stockez-le dans 'friend_list'. Bouclez pour envoyer le message à chaque ami un par un. Nous mettons le temps de sommeil = 2 secondes entre chaque message et nous nous déconnectons après avoir terminé.

```py
    if len(alert_msg) > 0 and previous_alert_msg != alert_msg:    
        # connexion et envoi du message Facebook 
        client = Client(FB_USERNAME,FB_PASSWORD)
        users = client.fetchAllUsers()
        friend_list=[user.uid for user in users if user.uid!="0"]
        # boucle à travers tous les amis
        for id in friend_list: 
            client.send(Message(text=current_retrieved_datetime+' '+'Prévisions météo sur 12 heures' +' '+ alert_msg +' '+link_for_click),thread_id=id, thread_type=ThreadType.USER)
            # sommeil de 2 secondes entre chaque message
            time.sleep(2) 
        # déconnexion après l'envoi
        client.logout()   
```

Exécutez le temps de délai pour le prochain message. Déjà défini dans le fichier [params.py](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat/blob/master/scripts/params.py) — dans ce cas, il est de 4 heures. Et un autre pour le délai de demande AccuWeather est de 1 heure.

```py
    time.sleep(delay_time_sec)                         
time.sleep(update_interval_sec)
```

Encore une fois, ne vous inquiétez pas si vous êtes perdu. J'ai mis la boucle complète ci-dessous.

```py
# Exécuter les fonctions, récupérer les données et envoyer le message Facebook
num_repeat = 999 # nombre de boucles à répéter
previous_alert_msg = "" # initialiser le message d'alerte
for i in range(num_repeat):
    
    try:
        current_retrieved_datetime,alert_msg,link_for_click = func_get_weather(url_page)
    except (RuntimeError, TypeError, NameError, ValueError, urllib.error.URLError):
        print('erreur attrapée')

    # si la prévision météo n'a pas changé, aucun message d'alerte ne sera envoyé
    if len(alert_msg) > 0 and previous_alert_msg == alert_msg:
        print(i, current_retrieved_datetime, 'aucun changement dans la prévision météo')
    # s'il y a des changements dans la météo       
    if len(alert_msg) > 0 and previous_alert_msg != alert_msg:    
        # connexion et envoi du message Facebook 
        client = Client(FB_USERNAME,FB_PASSWORD)
        users = client.fetchAllUsers()
        friend_list=[user.uid for user in users if user.uid!="0"]
        # boucle à travers tous les amis
        for id in friend_list: 
            client.send(Message(text=current_retrieved_datetime+' '+'Prévisions météo sur 12 heures' +' '+ alert_msg +' '+link_for_click),thread_id=id, thread_type=ThreadType.USER)
            # sommeil de 2 secondes entre chaque message
            time.sleep(2) 
        # déconnexion après l'envoi
        client.logout()    
        time.sleep(delay_time_sec)                         
    time.sleep(update_interval_sec)
print(current_retrieved_datetime,'Exécution terminée')
```

Ta-da ! Après tout notre travail acharné, voici un aperçu du message que nous allons recevoir.

![Image](https://cdn-media-1.freecodecamp.org/images/1*34jxVzSyVzO86-OKGlzVHw.png)
_Message de la boîte de chat Facebook. L'identifiant de l'emplacement dans cet exemple est 135564._

Au cas où nous aurions besoin de plus de détails, nous pouvons cliquer directement sur le lien. Il nous redirigera vers le site mobile AccuWeather.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sZ6uWgjnGDF1rVBoKy44Ng.png)
_Lien AccuWeather_

Le script complet pour ce guide est également [documenté sur GitHub](https://github.com/ekapope/Weather_Alert_Notification_Facebook_Chat).

Merci d'avoir lu. Essayez-le, amusez-vous et faites-moi savoir vos commentaires !

Si vous aimez ce que j'ai fait, envisagez de me suivre sur [GitHub](https://ekapope.github.io/), [Medium](https://medium.com/@ekapope.v), et [Twitter](https://twitter.com/EkapopeV). Assurez-vous de [l'étoiler sur GitHub](https://github.com/Ekapope) :D