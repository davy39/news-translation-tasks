---
title: Quel est le meilleur moment pour diffuser en direct sur Facebook Live ? J'ai
  analysé 5 000 publications Facebook pour le découvrir.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-04T20:42:29.000Z'
originalURL: https://freecodecamp.org/news/the-best-time-to-stream-on-facebook-live-my-analysis-5-000-facebook-posts-c8346b732d0f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Mrg0GKl9ZPW_mQv2iy0DHw.png
tags:
- name: Data Science
  slug: data-science
- name: Entrepreneurship
  slug: entrepreneurship
- name: Facebook
  slug: facebook
- name: marketing
  slug: marketing
- name: startup
  slug: startup
seo_title: Quel est le meilleur moment pour diffuser en direct sur Facebook Live ?
  J'ai analysé 5 000 publications Facebook pour le découvrir.
seo_desc: 'By Ofir Chakon

  Streaming on Facebook Live can be a powerful marketing strategy for startups and
  businesses. They can share knowledge, provide value, get exposure and collect high-quality
  leads.

  Prepare your Facebook Live session upfront. Researching ...'
---

Par Ofir Chakon

Diffuser en direct sur Facebook Live peut être une stratégie marketing puissante pour les startups et les entreprises. Elles peuvent partager des connaissances, fournir de la valeur, obtenir de la visibilité et collecter des leads de haute qualité.

Préparez votre session Facebook Live à l'avance. Faites des recherches sur votre public cible et construisez un agenda détaillé. La session peut booster votre entreprise de manière spectaculaire.

J'étais Chef de Produit et Technologie dans ma précédente startup spécialisée dans la détection de fraudes. J'ai décidé d'essayer Facebook Live comme nouvelle stratégie marketing.

C'était encore relativement nouveau à l'époque. Une fois qu'une session Facebook Live était lancée, les personnes concernées recevaient des notifications Facebook pour rejoindre la session. Cela augmentait encore plus la visibilité.

Il existe de nombreux articles expliquant comment mieux construire votre session Facebook Live. Ils discutent des sujets à aborder, de la construction d'un agenda, des angles de caméra, de la durée de la session, et plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/ZHFfsew6XVks0GRiG80lhrRnI9MYiWckGZMD)

Mais il y a un élément du puzzle que les propriétaires d'entreprise et les marketeurs oublient souvent ou auquel ils ne prêtent pas attention : **Quel est le meilleur moment pour diffuser votre session Facebook Live ?**

Vous pouvez répondre à cette question en utilisant une supposition éclairée basée sur votre familiarité avec le public cible.

Par exemple :

* Les mamans enceintes sont prêtes à consommer votre session Live le lundi après-midi.
* Les adolescents âgés de 18 à 22 ans sont dans le bon état d'esprit le samedi matin.

Mais il y a tellement de données autour de nous que nous pouvons utiliser avec quelques clics de souris. Vous restez en arrière si vous ne faites pas un usage approprié de certaines des données disponibles.

Presque toutes les plateformes marketing ou réseaux sociaux ouvrent des services API. Vous, en tant qu'entrepreneur technologique, pouvez facilement les consommer. Ces données peuvent fournir des conclusions précieuses qui peuvent propulser vos objectifs commerciaux au-delà de vos concurrents.

Cette approche est souvent appelée **décisions basées sur les données**.

Une fois que vous commencez à justifier certaines ou au moins la plupart de vos décisions commerciales en utilisant des données que vous possédez ou des données que vous pouvez collecter à partir de différentes ressources, vous pouvez arrêter de deviner et commencer à prendre des décisions basées sur les données.

J'aime penser aux décisions basées sur les données comme du crowd-sourcing. Lior Zoref était dans [cette conférence TED](https://www.youtube.com/watch?v=din2UVvRnGU). Il a invité un bœuf sur scène et a demandé au public de deviner son poids. Si vous avez regardé cela, vous avez probablement été impressionné par la précision de la moyenne de la foule par rapport au poids réel du bœuf : 1 792 livres ou 1 795 livres !

![Image](https://cdn-media-1.freecodecamp.org/images/IvzzdOZzotoMqgIQ33aA3O9Rr9XGA5vWCg5C)

Lorsque vous faites des suppositions sur vos objectifs commerciaux en tant qu'individus, vous n'êtes pas différent de toute personne assise dans la foule et essayant d'évaluer le poids du bœuf. Vous pouvez même être celui qui a deviné 300 livres ou 8 000 livres, ce qui peut coûter à votre entreprise beaucoup de dépenses inutiles.

Mais, si vous utilisez la sagesse de la foule pour prendre des décisions basées sur les données, vous serez probablement en avance sur tous les autres individus. En termes commerciaux, vous serez en avance sur vos concurrents.

Je ne suis pas un marketeur pur. Mais avec des compétences de base en analyse de données, je peux faire avancer mon entreprise dans tous les aspects, y compris le marketing.

Je vais vous guider à travers un guide pratique étape par étape sur la façon d'accéder aux données de Facebook. Ensuite, comment les analyser en fonction de nos besoins concernant le moment optimal pour diffuser sur Facebook Live.

Pour suivre ce guide, vous avez besoin de :

* Un compte Facebook
* Un groupe Facebook que vous souhaitez analyser
Si c'est un groupe privé, vous devez en être membre
* Python 2.7 installé
* Jupyter notebook installé
* La bibliothèque Python de l'API Graph de Facebook installée

Un notebook Jupyter est un outil recommandé pour l'analyse de données en Python. Il a de nombreux avantages. Il vous permet d'exécuter des extraits de code et de sauvegarder les résultats en mémoire. Ainsi, vous n'exécuterez pas tous vos scripts encore et encore chaque fois que vous implémentez un changement mineur. Cela est crucial lors de l'analyse de données car certaines tâches peuvent prendre beaucoup de temps d'exécution.

Bien que ce ne soit pas essentiel, je recommande de travailler dans un environnement virtuel Python. [Voici un article que j'ai écrit](https://codingstartups.com/3-best-practices-better-setting-django-project/) sur les avantages d'un environnement virtuel lors de l'utilisation de Python.

Je recommande de travailler dans un [environnement Ubuntu](https://codingstartups.com/moved-windows-linux-lessons-learned/) lors de l'analyse de données en utilisant des notebooks Jupyter.

### Étape 1 — Obtenir l'ID du groupe Facebook

Pour obtenir des données de l'API Facebook, nous devons spécifier l'ID de l'entité dont nous voulons obtenir des données, dans notre cas, un groupe Facebook.

[Lookup-id.com](https://lookup-id.com/#) est un outil pratique que vous pouvez utiliser pour trouver l'ID d'un groupe basé sur son URL. Copiez l'URL de votre groupe et collez-la dans la barre de recherche.

![Image](https://cdn-media-1.freecodecamp.org/images/tKkbNLOW2TP-L-N7xNrf0w4lca-mj5EKrYv9)

Dans cet article, nous utiliserons le groupe : [Web Design and Development](https://www.facebook.com/groups/websworld/).

ID : **319479604815804**

### Étape 2 — Découvrir l'Explorateur d'API Graph

Pour tirer le meilleur parti de l'API Facebook en plus de la [documentation](https://developers.facebook.com/docs/), Facebook a développé un terrain de jeu pour les développeurs appelé [Graph API Explorer](https://developers.facebook.com/tools/explorer/).

L'Explorateur d'API Graph nous permet d'obtenir un jeton d'accès temporaire et de commencer à examiner les capacités que l'API Facebook a à offrir.

Cliquez sur **Get Token**. Ne sélectionnez aucune permission. Cliquez sur **Get Access Token**.

![Image](https://cdn-media-1.freecodecamp.org/images/EfF4faazp7CJE5KaNA0Zj8uz3hBc3DC5EujD)

L'API Facebook a de nombreux points de terminaison que vous pouvez utiliser. Dans ce guide, nous allons utiliser deux points de terminaison principaux :

* Le [point de terminaison du groupe](https://developers.facebook.com/docs/graph-api/reference/v2.10/group/)
* Le [point de terminaison des réactions](https://developers.facebook.com/docs/graph-api/reference/v2.10/object/reactions)

Pour déterminer la structure de la réponse que vous attendez, spécifiez l'URL du point de terminaison et cliquez sur **Submit**.

Examinons l'URL du point de terminaison pour récupérer les dernières publications du fil du groupe. Tapez cette URL dans l'Explorateur d'API Graph :

```
319479604815804/feed
```

et cliquez sur **Submit**.

![Image](https://cdn-media-1.freecodecamp.org/images/LDY1c5rCL0iwi6UCuQHoLTW8qjeqR3PGj5IL)

Vous devriez maintenant voir les dernières publications du fil du groupe dans une structure JSON. Il contient le contenu de la publication, son ID et l'heure de mise à jour. En cliquant sur l'un des ID et en ajoutant à la fin de l'URL :

```
319479604815804_1468216989942054/reactions?summary=total_count
```

Vous devriez voir une liste des réactions pour la publication spécifique, et un résumé du nombre total de réactions.

De cette manière, vous pouvez explorer toutes les fonctionnalités que l'API Facebook a à offrir.

Un autre outil pour examiner les points de terminaison des API qui n'offrent pas de terrain de jeu est [Postman](https://codingstartups.com/8-top-must-use-tools-boost-web-development-workflow/). Vous pouvez en savoir plus sur cet outil et les outils essentiels pour les [développeurs web](https://codingstartups.com/8-top-must-use-tools-boost-web-development-workflow/).

### Étape 3 — Notre plan et nos hypothèses

Notre objectif est de trouver le meilleur moment pour avoir une session Facebook Live dans le groupe qui contient notre public cible. Pour cela, nous supposons que plus il y a d'activité dans le groupe à un moment spécifique, plus il est probable que notre session Facebook Live obtiendra plus de traction.

Notre objectif maintenant est de déterminer quand il y a un pic dans l'activité du groupe au fil du temps. Et par quand, je veux dire un jour de la semaine et une heure spécifiques.

Pour cela, nous allons récupérer les 5 000 dernières publications du fil du groupe. Ensuite, nous tracerons la distribution des heures auxquelles elles ont été mises à jour.

Nous supposons que les publications plus longues indiquent plus d'activité dans le groupe car les membres passent plus de temps dans le groupe à les écrire. Ainsi, notre prochaine étape sera de prendre en compte la longueur de chaque publication dans la distribution.

Les réactions sur Facebook sont probablement une excellente indication de l'engagement des personnes avec une publication spécifique. Ainsi, notre dernière étape sera de collecter le nombre total de `réactions` pour chaque publication. Ensuite, prendre cela en compte dans la distribution de l'activité sur les jours de la semaine et les heures.

Parce que les `réactions` peuvent venir après la publication, nous devons être prudents en utilisant cette approche d'analyse de données.

### Étape 4 — Analysons quelques données !

Pour démarrer un notebook Jupyter, vous devez exécuter :

```
ipython notebook
```

et ensuite choisir New → Python 2.

![Image](https://cdn-media-1.freecodecamp.org/images/iMVyAqCTKHImyZgiNl0r9qDh4fHtENLef2af)

Pour analyser et tracer les données, nous allons utiliser les bibliothèques `numpy` et `matplotlib`. Ce sont des bibliothèques Python très populaires que vous devriez utiliser pour mieux analyser vos données.

Importons toutes les bibliothèques dont nous avons besoin :

```
import matplotlib.pyplot as plt
import numpy as np
import facebook
import urlparse
import datetime
import requests
```

et spécifions notre jeton d'accès et l'ID du groupe :

```
ACCESS_TOKEN = 'INSERT_ACCESS_TOKEN_HERE'
GROUP_ID = '319479604815804' # Groupe Web Design and Development
```

Ensuite, initialisons l'objet API avec notre jeton d'accès :

```
graph = facebook.GraphAPI(ACCESS_TOKEN)
```

Maintenant, nous voulons récupérer les publications du fil du groupe. Pour éviter les erreurs pendant les appels API, nous allons limiter chaque appel API à 50 publications et itérer sur 100 appels API :

```
posts = []
url = "{}/feed?limit=50".format(GROUP_ID)
until = None
for i in xrange(100):
    if until is not None:
        url += "&until={}".format(until)
    response = graph.request(url)
    data = response.get('data')
    if not data:
        break
    posts = posts + data
    next_url = response.get("paging").get("next")
    parsed_url = urlparse.urlparse(next_url)
    until = urlparse.parse_qs(parsed_url.query)["until"][0]
```

```
Dans chaque appel API, nous spécifions le paramètre until pour obtenir des publications plus anciennes.
```

```
Maintenant, organisons les publications en jours de la semaine et heures de la journée :
```

```
weekdays = {i: 0 for i in xrange(7)}
```

```
hours_of_day = {i: 0 for i in xrange(24)}
```

```
hours_of_week = np.zeros((7,24), dtype=np.int)
for post in posts:
    updated = datetime.datetime.strptime(post.get("updated_time"), "%Y-%m-%dT%H:%M:%S+0000")
    weekday = updated.weekday()
    hour_of_day = updated.hour
    weekdays[weekday] += 1
    hours_of_day[hour_of_day] += 1
    hours_of_week[weekday][hour_of_day] += 1
```

et ensuite, traçons les résultats en utilisant les graphiques à barres `matplotlib` :

```
plt.bar(weekdays.keys(), weekdays.values(), color='g')
plt.show()
```

![Image](https://cdn-media-1.freecodecamp.org/images/MKsXvKQmZNzAN3t2AaHWkbICk55C-UQHQDUt)
_0 représente le lundi_

```
plt.bar(hours_of_day.keys(), hours_of_day.values(), color='r')
plt.show()
```

![Image](https://cdn-media-1.freecodecamp.org/images/Wg7MdsofTo5ejs2dAkxn02OzqJfNyqghO41j)
_Tous les horaires sont spécifiés en IST_

Avec cette analyse de base seulement, nous pouvons déjà apprendre beaucoup sur les meilleurs ou pires créneaux horaires pour diffuser vers ce groupe. Mais cela ne semble pas assez informatif. Peut-être parce que les données sont divisées en 2 graphiques et manquent certaines informations critiques.

Essayons de présenter une carte thermique des données, qui nous permet de voir des informations en 3D :

```
plt.imshow(hours_of_week, cmap='hot')
plt.show()
```

![Image](https://cdn-media-1.freecodecamp.org/images/eEL4Zx2R8ur2sBc1ym9AkxAcG4RDg7c9wAAT)

Eh bien, c'est beaucoup mieux ! Nous pouvons voir que le groupe est très actif du lundi au vendredi entre 6h00 et 10h00.

Maintenant, prenons en compte la longueur des publications et voyons comment cela affecte les résultats :

```
weekdays_content = {i: 0 for i in xrange(7)}
hours_of_day_content = {i: 0 for i in xrange(24)}
hours_of_week_content = np.zeros((7,24), dtype=np.int)
for post in posts:
    updated = datetime.datetime.strptime(post.get("updated_time"), "%Y-%m-%dT%H:%M:%S+0000")
    weekday = updated.weekday()
    hour_of_day = updated.hour
    content_length = len(post["message"]) if "message" in post else 1
    weekdays_content[weekday] += content_length
    hours_of_day_content[hour_of_day] += content_length
    hours_of_week_content[weekday][hour_of_day] += content_length
```

La carte thermique que nous obtenons :

![Image](https://cdn-media-1.freecodecamp.org/images/A1B6SxDiXiJIs6Ak-Moe5DH1-msmRJ0B531N)

C'est bien mais doit être traité avec prudence. D'une part, nous pouvons voir un moment très spécifique qui est le créneau horaire optimisé pour avoir notre session Facebook Live. Mais, il pourrait s'agir d'un cas aberrant d'une publication super longue.

Je vous laisse le soin de le découvrir dans votre prochain projet d'analyse de données. Prenez une plus grande quantité de publications ou récupérez un lot plus ancien de 5000 publications du fil du groupe.

Pour prendre en compte les `réactions` lors de l'analyse des données, nous devons faire un autre appel API pour chaque publication.

C'est parce que c'est un point de terminaison API différent :

```
weekdays_reactions = {i: 0 for i in xrange(7)}
hours_of_day_reactions = {i: 0 for i in xrange(24)}
hours_of_week_reactions = np.zeros((7,24), dtype=np.int)
for i, post in enumerate(posts):
    url = "https://graph.facebook.com/v2.10/{id}/reactions?access_token={token}&summary=total_count".format(
    id=post["id"],
        token=ACCESS_TOKEN
    )
```

```
headers = {
        "Host": "graph.facebook.com"
    }
```

```
response = requests.get(url, headers=headers)
```

```
try:
        total_reactions = 1 + response.json().get("summary").get("total_count")
    except:
        total_reactions = 1
```

```
updated = datetime.datetime.strptime(post.get("updated_time"), "%Y-%m-%dT%H:%M:%S+0000")
    weekday = updated.weekday()
    hour_of_day = updated.hour
    weekdays_reactions[weekday] += total_reactions
    hours_of_day_reactions[hour_of_day] += total_reactions
    hours_of_week_reactions[weekday][hour_of_day] += total_reactions
```

Nous avons utilisé une approche de bas niveau en spécifiant la requête HTTP exacte et n'avons pas utilisé la bibliothèque Python de Facebook. Cela est dû au fait que cette bibliothèque ne supporte pas la dernière version de l'API Facebook requise lors de l'interrogation du point de terminaison `reactions`.

La carte thermique générée à partir de ces données :

![Image](https://cdn-media-1.freecodecamp.org/images/GLEHAw3lkvcmSTDOvMMPkVAmoiJrTCzo6PVB)

Nous pouvons conclure que les trois approches que nous avons utilisées s'accordent sur le lundi et le mercredi, de 6h00 à 7h00.

### Conclusions

L'analyse de données peut être difficile et nécessite souvent de la créativité. Mais elle est aussi passionnante et très gratifiante.

Après avoir choisi notre moment pour diffuser sur Facebook Live en nous basant sur l'analyse présentée ici, nous avons eu un énorme succès et beaucoup de traction pendant notre session Live.

Je vous encourage à essayer et à utiliser l'analyse de données pour prendre des décisions basées sur les données dans votre prochain mouvement commercial. Et commencez à penser en termes de décisions basées sur les données.

Vous pouvez trouver le dépôt Github [ici](https://github.com/CodingStartups/facebook-live-data).

J'ai initialement publié cela sur [CodingStartups](https://codingstartups.com/).