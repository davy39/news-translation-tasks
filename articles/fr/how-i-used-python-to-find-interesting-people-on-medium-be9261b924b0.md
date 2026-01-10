---
title: Comment j'ai utilisé Python pour trouver des personnes intéressantes à suivre
  sur Medium
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-11T11:31:24.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9rLeOFD7rvImTlcXQUe-mw.png
tags:
- name: medium
  slug: medium
- name: Python
  slug: python
- name: startup
  slug: startup
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment j'ai utilisé Python pour trouver des personnes intéressantes à
  suivre sur Medium
seo_desc: 'By Radu Raicea

  Medium has a large amount of content, a large number of users, and an almost overwhelming
  number of posts. When you try to find interesting users to interact with, you’re
  flooded with visual noise.

  I define an interesting user as someo...'
---

Par Radu Raicea

Medium contient une grande quantité de contenu, un grand nombre d'utilisateurs et un nombre presque écrasant de publications. Lorsque vous essayez de trouver des utilisateurs intéressants avec lesquels interagir, vous êtes submergé de bruit visuel.

Je définis un utilisateur intéressant comme quelqu'un qui fait partie de votre réseau, qui est actif et qui écrit des réponses généralement appréciées par la communauté Medium.

Je parcourais les dernières publications des utilisateurs que je suis pour voir qui avait répondu à ces utilisateurs. Je me suis dit que si ils répondaient à quelqu'un que je suis, ils devaient avoir des intérêts similaires aux miens.

Le processus était fastidieux. Et c'est à ce moment-là que je me suis souvenu de la leçon la plus précieuse que j'ai apprise lors de mon dernier stage :

**Toute tâche fastidieuse peut et doit être automatisée.**

Je voulais que mon automatisation fasse les choses suivantes :

1. Obtenir tous les **utilisateurs** de ma liste "Abonnements"
2. Obtenir les dernières **publications** de chaque utilisateur
3. Obtenir toutes les **réponses** à chaque publication
4. Filtrer les réponses plus anciennes que 30 jours
5. Filtrer les réponses ayant moins d'un nombre minimum de recommandations
6. Obtenir le **nom d'utilisateur** de l'auteur de chaque réponse

### Commençons à explorer

J'ai d'abord regardé l'[API de Medium](https://github.com/Medium/medium-api-docs), mais je l'ai trouvée limitante. Elle ne me donnait pas grand-chose avec quoi travailler. Je ne pouvais obtenir des informations que sur mon compte, et non sur d'autres utilisateurs.

En plus de cela, le dernier changement apporté à l'API de Medium remonte à plus d'un an. Il n'y avait aucun signe de développement récent.

J'ai réalisé que je devrais me fier aux requêtes HTTP pour obtenir mes données, alors j'ai commencé à explorer en utilisant mes [**Chrome DevTools**](https://developer.chrome.com/devtools).

Le premier objectif était d'obtenir ma liste d'Abonnements.

J'ai ouvert mes DevTools et je suis allé dans l'onglet Réseau. J'ai filtré tout sauf [XHR](https://en.wikipedia.org/wiki/XMLHttpRequest) pour voir d'où Medium obtient ma liste d'Abonnements. J'ai cliqué sur le bouton de rechargement de ma page de profil et je n'ai rien obtenu d'intéressant.

Et si je cliquais sur le bouton Abonnements de mon profil ? Bingo.

![Image](https://cdn-media-1.freecodecamp.org/images/Ee6OOGBa5dG7hRyH4i7CzL7oMUumnReStC8-)
_Trouver le lien qui liste les abonnements d'un utilisateur_

À l'intérieur du lien, j'ai trouvé une très grande réponse [JSON](https://en.wikipedia.org/wiki/JSON). C'était un JSON bien formaté, à l'exception d'une chaîne de caractères au début de la réponse : `])}while(1);<`/x>

J'ai écrit une fonction pour nettoyer cela et transformer le JSON en un dictionnaire Python.

```
import json
```

```
def clean_json_response(response):    return json.loads(response.text.split('])}while(1);</x>')[1])
```

J'avais trouvé un point d'entrée. Que le codage commence.

### Obtenir tous les utilisateurs de ma liste d'Abonnements

Pour interroger ce point de terminaison, j'avais besoin de mon ID d'utilisateur (je sais que je l'avais déjà, mais c'est à des fins éducatives).

En cherchant un moyen d'obtenir l'ID d'un utilisateur, j'ai [découvert](https://medium.com/statuscode/building-a-basic-web-service-to-display-your-medium-blog-posts-on-your-website-using-aws-api-48597b1771c5) que vous pouvez ajouter `?format=json` à la plupart des URL de Medium pour obtenir une réponse JSON de cette page. J'ai essayé cela sur ma page de profil.

Oh, regardez, voici l'ID de l'utilisateur.

```
])}while(1);</x>{"success":true,"payload":{"user":{"userId":"d540942266d0","name":"Radu Raicea","username":"Radu_Raicea",...
```

J'ai écrit une fonction pour extraire l'ID de l'utilisateur à partir d'un nom d'utilisateur donné. Encore une fois, j'ai dû utiliser `clean_json_response` pour supprimer les caractères indésirables au début de la réponse.

J'ai également créé une constante appelée `MEDIUM` qui contient la base de toutes les URL de Medium.

```
import requests
```

```
MEDIUM = 'https://medium.com'
```

```
def get_user_id(username):
```

```
    print('Récupération de l\'ID de l\'utilisateur...')
```

```
    url = MEDIUM + '/@' + username + '?format=json'    response = requests.get(url)    response_dict = clean_json_response(response)    return response_dict['payload']['user']['userId']
```

Avec l'ID de l'utilisateur, j'ai interrogé le point de terminaison `/_/api/users/<user_id>/following` et j'ai obtenu la liste des noms d'utilisateur de ma liste d'Abonnements.

Lorsque je l'ai fait dans DevTools, j'ai remarqué que la réponse JSON ne contenait que huit noms d'utilisateur. Bizarre.

Après avoir cliqué sur "Afficher plus de personnes", j'ai vu ce qui manquait. Medium utilise la [**pagination**](https://developer.twitter.com/en/docs/ads/general/guides/pagination) pour la liste des Abonnements.

![Image](https://cdn-media-1.freecodecamp.org/images/3-eKbPasdKJvOhPQW7WT7xlHtVm38Rg3lvDB)
_Medium utilise la pagination pour la liste des Abonnements_

La pagination fonctionne en spécifiant une `limite` (éléments par page) et `to` (premier élément de la page suivante). Je devais trouver un moyen d'obtenir l'ID de cet élément suivant.

À la fin de la réponse JSON de `/_/api/users/<user_id>/following`, j'ai vu une clé intéressante.

```
..."paging":{"path":"/_/api/users/d540942266d0/followers","next":{"limit":8,"to":"49260b62a26c"}}},"v":3,"b":"31039-15ed0e5"}
```

À partir de là, écrire une boucle pour obtenir tous les noms d'utilisateur de ma liste d'Abonnements était facile.

```
def get_list_of_followings(user_id):
```

```
    print('Récupération des utilisateurs des Abonnements...')        next_id = False    followings = []
```

```
    while True:
```

```
        if next_id:            # Si ce n'est pas la première page de la liste des abonnements            url = MEDIUM + '/_/api/users/' + user_id                  + '/following?limit=8&to=' + next_id        else:            # Si c'est la première page de la liste des abonnements            url = MEDIUM + '/_/api/users/' + user_id + '/following'
```

```
        response = requests.get(url)        response_dict = clean_json_response(response)        payload = response_dict['payload']
```

```
        for user in payload['value']:            followings.append(user['username'])
```

```
        try:            # Si la clé "to" est manquante, nous avons atteint la fin            # de la liste et une exception est levée            next_id = payload['paging']['next']['to']        except:            break
```

```
    return followings
```

### Obtenir les dernières publications de chaque utilisateur

Une fois que j'ai eu la liste des utilisateurs que je suis, je voulais obtenir leurs dernières publications. Je pouvais le faire avec une requête à `[https://medium.com/@<username>/latest?forma](https://medium.com/@username/latest?format=json)`t=json

J'ai écrit une fonction qui prend une liste de noms d'utilisateur et retourne une liste d'ID de publications pour les dernières publications de tous les noms d'utilisateur de la liste d'entrée.

```
def get_list_of_latest_posts_ids(usernames):
```

```
    print('Récupération des dernières publications...')
```

```
    post_ids = []
```

```
    for username in usernames:        url = MEDIUM + '/@' + username + '/latest?format=json'        response = requests.get(url)        response_dict = clean_json_response(response)
```

```
        try:            posts = response_dict['payload']['references']['Post']        except:            posts = []
```

```
        if posts:            for key in posts.keys():                post_ids.append(posts[key]['id'])
```

```
    return post_ids
```

### Obtenir toutes les réponses de chaque publication

Avec la liste des publications, j'ai extrait toutes les réponses en utilisant `https://medium.com/_/api/posts/<post_id>/res`ponses

Cette fonction prend une liste d'ID de publications et retourne une liste de réponses.

```
def get_post_responses(posts):
```

```
    print('Récupération des réponses aux publications...')
```

```
    responses = []
```

```
    for post in posts:        url = MEDIUM + '/_/api/posts/' + post + '/responses'        response = requests.get(url)        response_dict = clean_json_response(response)        responses += response_dict['payload']['value']
```

```
    return responses
```

#### Filtrer les réponses

Au début, je voulais des réponses qui avaient obtenu un nombre minimum d'applaudissements. Mais j'ai réalisé que cela pourrait ne pas être une bonne représentation de l'appréciation de la communauté pour la réponse : un utilisateur peut donner plus d'un applaudissement pour le même article.

Au lieu de cela, j'ai filtré par le nombre de recommandations. Cela mesure la même chose que les applaudissements, mais cela ne prend pas en compte les doublons.

Je voulais que le minimum soit dynamique, alors j'ai passé une variable nommée `recommend_min` autour.

La fonction suivante prend une réponse et la variable `recommend_min`. Elle vérifie si la réponse atteint ce minimum.

```
def check_if_high_recommends(response, recommend_min):    if response['virtuals']['recommends'] >= recommend_min:        return True
```

Je voulais également des réponses récentes. J'ai filtré les réponses plus anciennes que 30 jours en utilisant cette fonction.

```
from datetime import datetime, timedelta
```

```
def check_if_recent(response):    limit_date = datetime.now() - timedelta(days=30)    creation_epoch_time = response['createdAt'] / 1000    creation_date = datetime.fromtimestamp(creation_epoch_time)
```

```
    if creation_date >= limit_date:        return True
```

### Obtenir le nom d'utilisateur de l'auteur de chaque réponse

Une fois que j'ai eu toutes les réponses filtrées, j'ai récupéré tous les ID des auteurs en utilisant la fonction suivante.

```
def get_user_ids_from_responses(responses, recommend_min):
```

```
    print('Récupération des ID d\'utilisateur des réponses...')
```

```
    user_ids = []
```

```
    for response in responses:        recent = check_if_recent(response)        high = check_if_high_recommends(response, recommend_min)
```

```
        if recent and high:            user_ids.append(response['creatorId'])
```

```
    return user_ids
```

Les ID d'utilisateur sont inutiles lorsque vous essayez d'accéder au profil de quelqu'un. J'ai fait en sorte que cette fonction suivante interroge le point de terminaison `/_/api/users/<user_id>` pour obtenir les noms d'utilisateur.

```
def get_usernames(user_ids):
```

```
    print('Récupération des noms d\'utilisateur des utilisateurs intéressants...')
```

```
    usernames = []
```

```
    for user_id in user_ids:        url = MEDIUM + '/_/api/users/' + user_id        response = requests.get(url)        response_dict = clean_json_response(response)        payload = response_dict['payload']
```

```
        usernames.append(payload['value']['username'])
```

```
    return usernames
```

### Mettre tout ensemble

Après avoir terminé toutes les fonctions, j'ai créé un [pipeline](https://en.wikipedia.org/wiki/Pipeline_(software)) pour obtenir ma liste d'utilisateurs recommandés.

```
def get_interesting_users(username, recommend_min):
```

```
    print('Recherche d\'utilisateurs intéressants pour %s...' % username)
```

```
    user_id = get_user_id(username)
```

```
    usernames = get_list_of_followings(user_id)
```

```
    posts = get_list_of_latest_posts_ids(usernames)
```

```
    responses = get_post_responses(posts)
```

```
    users = get_user_ids_from_responses(responses, recommend_min)
```

```
    return get_usernames(users)
```

Le script était enfin prêt ! Pour l'exécuter, vous devez appeler le pipeline.

```
interesting_users = get_interesting_users('Radu_Raicea', 10)print(interesting_users)
```

![Image](https://cdn-media-1.freecodecamp.org/images/1uACHW2JbTMIV-keNz8xATXsRCZRPlOPNpKL)
_Crédit image : [Know Your Meme](http://knowyourmeme.com/photos/185885-success-kid-i-hate-sandcastles" rel="noopener" target="_blank" title=")_

Enfin, j'ai ajouté une option pour ajouter les résultats à un CSV avec un horodatage.

```
import csv
```

```
def list_to_csv(interesting_users_list):    with open('recommended_users.csv', 'a') as file:        writer = csv.writer(file)
```

```
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')        interesting_users_list.insert(0, now)                writer.writerow(interesting_users_list)
```

```
interesting_users = get_interesting_users('Radu_Raicea', 10)list_to_csv(interesting_users)
```

Le code source du projet est sur [GitHub](https://github.com/Radu-Raicea/Interesting-People-On-Medium).

Si vous ne connaissez pas Python, allez lire [TK](https://www.freecodecamp.org/news/how-i-used-python-to-find-interesting-people-on-medium-be9261b924b0/undefined)'s [Learning Python: From Zero to Hero](https://medium.freecodecamp.org/learning-python-from-zero-to-hero-120ea540b567).

Si vous avez des suggestions sur d'autres critères qui rendent les utilisateurs intéressants, veuillez **les écrire ci-dessous !**

### En résumé...

* J'ai créé un [**script Python pour Medium**](https://github.com/Radu-Raicea/Interesting-People-On-Medium).
* Le script retourne une liste d'utilisateurs intéressants qui sont **actifs** et **postent des réponses intéressantes** sur les dernières publications des personnes que vous suivez.
* Vous pouvez prendre des utilisateurs de la liste et exécuter le script avec leur nom d'utilisateur au lieu du vôtre.

**Consultez mon [primer](https://medium.freecodecamp.org/how-open-source-licenses-work-and-how-to-add-them-to-your-projects-34310c3cf94) sur les licences open source et comment les ajouter à vos projets !**

Pour plus de mises à jour, suivez-moi sur [Twitter](https://twitter.com/radu_raicea).