---
title: Comment implémenter la tokenisation en utilisant JWT et Django Rest Framework
subtitle: ''
author: Velda Kiara
co_authors: []
series: null
date: '2023-02-23T15:53:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-jwt-and-django-rest-framework-to-get-tokens
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/Purple-Colorful-Tech-22-YouTube-Channel-Art.png
tags:
- name: Django
  slug: django
- name: JSON Web Tokens
  slug: json-web-tokens
- name: JWT
  slug: jwt
- name: Tokenization
  slug: tokenization
seo_title: Comment implémenter la tokenisation en utilisant JWT et Django Rest Framework
seo_desc: "When I was a young girl, we used to have sports competitions like running\
  \ a hundred meters, relays, swimming, and basketball games. \nMy strengths were\
  \ swimming and basketball. I went home with many gifts or, as my school's game master\
  \ said, a token o..."
---

Quand j'étais une jeune fille, nous avions des compétitions sportives comme la course de cent mètres, les relais, la natation et les matchs de basketball. 

Mes points forts étaient la natation et le basketball. Je rentrais à la maison avec de nombreux cadeaux ou, comme le disait le maître de jeu de mon école, un **jeton de reconnaissance**.

Un jeton est une forme sécurisée utilisée pour transmettre des données entre deux parties. Les médailles que j'ai obtenues lors des compétitions ont beaucoup de valeur pour moi, et si je les donnais à quelqu'un d'autre, elles ne seraient que des babiole.

JavaScript Object Notation (JSON) est un format utilisé pour présenter des données structurées basées sur la syntaxe JavaScript. Nous l'utilisons pour transmettre des données dans les applications web en envoyant les données du serveur à l'affichage du client.

JWT (JSON Web Token) est une forme de transmission d'un objet JSON en tant qu'information entre les parties. Apprenons-en plus sur ce que sont les JWT et comment ils fonctionnent.

## L'importance des JWT

Les JWT sont importants pour deux raisons principales :

**Autorisation** : lors de nos compétitions, nous devions présenter nos cartes d'identification scolaire pour vérification avant de recevoir nos médailles. 

Nos cartes d'identité scolaire agissaient comme des demandes de connexion dans les applications. Ces demandes, dans les applications, contiennent un JWT qui permet aux utilisateurs d'obtenir la permission d'accéder à toute ressource accessible avec ce jeton.

**Échange d'informations** : mes médailles étaient un badge d'honneur et un moyen d'obtenir un certificat signé et tamponné par notre maître de jeu pour légitimité. 

Nous utilisons les JWT pour échanger des informations dans les cas où ils sont signés – par exemple en utilisant des paires de clés publiques-privées pour s'assurer que l'intégrité de l'information n'est pas compromise puisque la charge utile et l'en-tête sont utilisées pour calculer les signatures.

## Comment fonctionnent les JWT ?

Un JWT est un jeton d'autorisation qui est inclus dans les demandes. Voici un exemple de ce à quoi cela ressemble :

```python
eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjczNTI3ODMzLCJpYXQiOjE2NzM1Mjc0MzAsImp0aSI6IjNkMGRkMGZiZjA5ZjRmZWU4MTZmMGQyOTQ5OWU3ZmFmIiwidXNlcl9pZCI6IjFmYTBiMGJkLWY4MmMtNDQzNy1iMmViLTMwOTYzMGZkNzQ2NiJ9.-swqFh4MCecycmodQfO8ZmfsDJ3DqoZBsdNzEWhfzhA


```

Vous pouvez obtenir un JWT en vous connectant avec un nom d'utilisateur et un mot de passe. En échange, le serveur retourne un jeton d'accès et un jeton de rafraîchissement sous forme de JWT. Les jetons accèdent aux ressources sur le serveur.

Les durées de vie des jetons d'accès et de rafraîchissement varient puisque les jetons d'accès durent cinq minutes ou moins tandis que les jetons de rafraîchissement peuvent durer 24 heures. Mais vous pouvez personnaliser les chronologies des deux types de jetons.

Si le jeton d'accès expire, le client utilise le jeton de rafraîchissement pour obtenir un nouveau jeton d'accès du serveur. Une fois le jeton de rafraîchissement expiré, l'utilisateur doit se reconnecter avec son nom d'utilisateur et son mot de passe pour obtenir une nouvelle paire de jetons. 

Cela fonctionne ainsi pour prévenir les dommages qui peuvent survenir lorsqu'un jeton est compromis et pour prévenir l'accès non autorisé.

### Différentes parties d'un JWT

Les JWT contiennent des informations en trois parties, comme vous pouvez le voir dans les blocs de code suivants :

```python
header.payload.signature

```

```python
header = eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9F5
payload = eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTQzODI4NDMxLCJqdGkiOiI3ZjU5OTdiNzE1MGQ0NjU3OWRjMmI0OTE2NzA5N2U3YiIsInVsztZXJfaWQiOjF9
signature = Ju70kdcaHKn1Qaz8H42zrOYk0Jx9kIciuhkTn9Xx7vhikY


```

Le JWT ci-dessus est encodé en utilisant [Base64](https://en.wikipedia.org/wiki/Base64). Une fois décodé, les informations incluront quelque chose de similaire aux parties suivantes :

#### En-tête

L'en-tête contient :

* type : la spécification que le jeton est un JWT
* algorithme : l'algorithme de signature utilisé pour signer ledit jeton

Les algorithmes utilisés pour signer incluent [RSA](https://www.geeksforgeeks.org/rsa-algorithm-cryptography/), [HMAC](https://www.geeksforgeeks.org/hmac-algorithm-in-computer-network/), ou [SHA256](https://www.n-able.com/blog/sha-256-encryption#:~:text=The%20SHA%2D256%20algorithm%20is,that%20is%20256%20bits%20long.). Les signatures pour les jetons servent deux objectifs – intégrité et authenticité.

Un exemple d'en-tête avec l'algorithme et le type est comme indiqué ci-dessous :

```python
{
  "alg": "HS256",
  "typ": "JWT"
}

```

#### Charge utile

La charge utile contient les messages prévus qui sont communément appelés revendications et métadonnées, ainsi que toute autre information.

Il existe trois types de revendications :

1. Revendications enregistrées : elles incluent exp (temps d'expiration), iss (émetteur), sub (sujet) et aud (public). Elles sont fortement recommandées car elles fournissent des informations sur l'utilisation et la condition d'utilisation du jeton.
2. Revendications publiques : ce sont des revendications qui sont uniques pour éviter les collisions avec d'autres services utilisant JWT. 
3. Revendications privées : ce sont des revendications qui sont utilisées spécifiquement entre deux parties qui comprennent la signification et l'utilisation. Comme l'exemple de mes médailles, mon maître de jeu et moi comprenions la valeur.

Ci-dessous se trouve un exemple de ce à quoi ressemble une charge utile.

```python
{
  "token_type": "access",
  "exp": 1543828431,
  "jti": "7f5997b7150d46579dc2b49167097e7b",
  "user_id": 4
}

```

* `token_type` est une étiquette qui montre quel type de jeton c'est. En l'occurrence, c'est un `jeton d'accès`.
* `exp` signifie expiration. C'est le moment où le jeton cessera de fonctionner – dans ce cas, le nombre représente la date et l'heure en temps Unix.
* `jti` signifie `ID JWT`. C'est un identifiant unique pour ce jeton spécifique. L'ID est utilisé pour suivre quels jetons ont été utilisés, pour éviter l'utilisation du même jeton plus d'une fois.
* `user_id` : est un identifiant de l'utilisateur auquel ce jeton appartient. Dans ce cas, le nombre 4 est l'identification de l'utilisateur.

#### Signature

La signature vérifie que les informations ne sont accessibles que par des personnes autorisées. Elle est émise par le backend JWT en utilisant base64 + charge utile + SECRET_KEY. 

La signature est vérifiée pour chaque demande. Pour valider la signature, vous utilisez la SECRET_KEY. N'oubliez pas que le but de l'appeler SECRET_KEY est qu'elle soit secrète. 

Maintenant, voyons comment les JWT fonctionnent en pratique avec un exemple.

## Installation du projet

Pour illustrer comment fonctionnent les JWT, j'utiliserai [simple JWT](https://django-rest-framework-simplejwt.readthedocs.io/en/latest/), qui est un plugin d'authentification JSON Web Token pour Django Rest Framework (DRF). 

### Prérequis

Pour suivre, vous devriez avoir quelques connaissances préalables des fichiers HTML et de la configuration d'un projet Django. Vous devriez également être familiarisé avec ce qu'est une API (Interface de Programmation d'Applications). 

Vous devrez également avoir un projet Django déjà configuré. Vous pourriez le nommer `tokenization` et ajouter une application appelée `access`. 

Une fois votre application et votre projet configurés, vous êtes prêt à partir. 

### Installation de Simple JWT

Comme mentionné, j'utiliserai `simple JWT` qui fournit une authentification JWT pour le Django Rest Framework (DRF).  

DRF est un package tiers pour Django utilisé comme boîte à outils pour construire des API Web. Il offre une expérience fluide pendant que vous construisez, testez, déboguez et maintenez des API RESTful en utilisant Django.

Les API RESTful (Representational State Transfer APIs) sont un type d'API web qui permettent la communication entre différentes applications sur Internet de manière rapide, fiable et évolutive.

Les API RESTful sont sans état. Cela signifie que les demandes contiennent des informations pour finaliser la demande, et le serveur n'a pas besoin de se souvenir de l'historique des demandes précédentes.

Pour installer `simple JWT`, utilisez la commande suivante dans votre terminal :

```python
pip install djangorestframework_simplejwt

```

### Comment définir l'authentification à Simple JWT

Allez dans votre projet (tokenization), et dans le fichier `settings.py`, ajoutez le code suivant pour configurer le framework REST pour utiliser simple JWT pour l'authentification :

```python
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
}


```

Le code ci-dessus spécifie la classe d'authentification par défaut à utiliser pour toutes les vues d'API dans l'application.

`DEFAULT_AUTHENTICATION_CLASSES': [ 'rest_framework_simplejwt.authentication.JWTAuthentication', ]` définit la classe d'authentification par défaut comme étant `JWTAuthentication` du package `rest_framework_simplejwt`. Cela signifie que toutes les vues d'API dans le projet utiliseront l'authentification JWT par défaut.

### Comment définir les motifs d'URL

Dans votre projet (tokenization), créez un fichier (si vous n'en avez pas encore créé un) nommé 
`urls.py`. Ensuite, ajoutez le code suivant :

```python
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]

```

La fonction `path` crée un nouveau motif d'URL et le mappe à la vue spécifiée.

Le chemin d'URL (Uniform Resource Locator) `/api/token/` est mappé à la vue `jwt_views.TokenObtainPairView.as_view()`. La méthode `as_view()` convertit la vue basée sur une classe en une vue basée sur une fonction utilisée dans le routage. Le paramètre `name` facilite la référence au motif d'URL dans d'autres parties de votre code. 

Nous avons maintenant créé un point de terminaison pour obtenir des jetons JWT. Si une demande est faite au point de terminaison, `TokenObtainPairView`, la vue gère la demande et retourne un jeton JWT dans la réponse pour l'authentification.

### Comment personnaliser les chronologies des jetons

Pour personnaliser la chronologie des jetons, ajoutez d'abord `rest_framework_simplejwt` dans la section des applications installées dans le projet (tokenization) sous le fichier `settings.py`. Le but d'ajouter `rest_framework_simplejwt` est pour la configuration. 

Pour ajouter la chronologie que nous voulons, nous créerons d'abord un dictionnaire appelé `SIMPLE_JWT`. Ensuite, nous créerons des variables pour contenir les chronologies des jetons d'accès et de rafraîchissement. 

L'extrait de code ci-dessous montre comment configurer les chronologies des jetons :

```python
INSTALLED_APPS = [
    # autres fichiers
    'rest_framework_simplejwt',
]

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=5),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}

```

Avant d'utiliser `timedelta`, vous devrez l'importer comme ceci : `python from datetime import timedelta`.

### Interaction visuelle avec l'API 

Dans cette section, nous utiliserons l'interface web de Django Rest Framework pour accéder aux points de terminaison.

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-13-at-10.55.14.png)
_Test de tokenisation_

Les jetons d'accès et de rafraîchissement sont mis en évidence en rouge, comme montré ci-dessus. Pour obtenir les jetons pour un utilisateur, vous devez entrer le mot de passe et le nom d'utilisateur corrects pour un utilisateur existant.

Utilisez un jeton de rafraîchissement via ce point de terminaison pour un jeton d'accès : `/api/token/refresh/` 

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-13-at-10.55.53.png)
_Jeton de rafraîchissement_

Un jeton de rafraîchissement obtient un jeton d'accès sans que l'utilisateur utilise ses identifiants de connexion pour prolonger la session de l'utilisateur. Cela fournit une expérience utilisateur fluide et améliore la sécurité en réduisant le nombre de fois où un utilisateur doit saisir ses identifiants.

### Comment ajouter une page d'accueil

Si vous souhaitez créer une interface visuellement attrayante, vous pouvez construire une page d'accueil personnalisée pour remplacer l'affichage actuel des points de terminaison de l'API et des messages d'erreur.

Pour ajouter une page d'accueil à votre projet Django, suivez ces étapes :

1. Créez un dossier `templates` dans votre application (access). Ensuite, ajoutez un fichier `index.html` à l'intérieur.
2. Créez un dossier `static` dans votre application (access) et ajoutez un dossier `img` à l'intérieur.
3. Dans ce cas, je voulais afficher une image, alors j'ai ajouté `me.png` dans le dossier img.
4. Ajoutez le code ci-dessous à votre fichier `html` :

```html
{% load static %}
<!DOCTYPE html>
<html>
<head>
    <title>Accueil</title>
    <style>
        body {
            background-image: url("{% static 'img/me.png' %}");
            background-size: cover;
        }
    </style>
</head>
</html>

```

Vous remarquerez que nous avons dû ajouter `{% load static %}` en haut du fichier pour un style et un fonctionnement appropriés du site. `{% load static %}` sert des fichiers comme des feuilles de style (CSS), des scripts (JS) et des images à vos modèles HTML pour offrir à l'utilisateur une expérience fluide lors de la visualisation de votre site.

### Comment définir les motifs d'URL pour votre page d'accueil

Dans le fichier `urls.py` de votre application (access) (créez-en un si vous n'en avez pas), ajoutez ceci :

```python
from django.urls import path
from django.views.generic import TemplateView

app_name='access'

urlpatterns=[
path('', TemplateView.as_view(template_name='home.html'), name='home'),

]
```

Dans le fichier `settings.py` de votre projet (tokenization), ajoutez le code suivant pour que les fichiers statiques soient servis :

```python
# Paramètres des fichiers statiques
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'access/static')]

```

Une fois que vous exécutez le serveur, votre page d'accueil devrait ressembler à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/Screenshot-2023-01-13-at-10.54.54.png)
_page d'accueil_

## Bugs et solutions

À un moment donné, j'ai peut-être supprimé le fichier `migrations` qui a supprimé certaines des données que j'avais. Cela a provoqué l'erreur suivante `django.db.utils.OperationalError: no such table: customUser`. 

J'ai pu résoudre cela en exécutant la commande `python manage.py migrate --run-syncdb`. La commande synchronise les tables en recherchant les tables non créées et en les créant.

J'ai également eu un problème d'utilisation d'un port qui était déjà utilisé par un programme que j'avais laissé en cours d'exécution et oublié.

Pour fermer un port, vous devez identifier le processus qui l'utilise en exécutant la commande `lsof -i :<port_number>`. Cela vous montrera l'utilisateur qui l'utilise et le PID. Pour arrêter le processus, utilisez `kill <PID>`. De plus, vous pouvez utiliser `sudo kill -9 -u <username> <pid>`.

Il est bon de savoir que pour tuer le port, vous aurez besoin de permissions d'administrateur. De plus, l'arrêt d'un processus peut provoquer une perte de données ou un comportement inhabituel, alors assurez-vous que vos données sont sauvegardées avant de faire cela.

## Conclusion

Dans ce tutoriel, vous avez appris comment fonctionnent les JWT, la structure des différents jetons, comment utiliser JWT et DRF pour obtenir des jetons, comment créer et servir des fichiers statiques dans Django, et comment gérer la suppression des fichiers de migration et tuer un port.

Il y a tant de choses que vous pouvez apprendre sur [Django](https://www.djangoproject.com/) et le [Django Rest Framework.](https://www.django-rest-framework.org/)

Le code de cet article peut être trouvé [ici](https://github.com/VeldaKiara/tokenization).

Puisse votre clavier être rapide, vos bugs peu nombreux, et votre compteur de plaisir être hors des graphiques pendant que vous codez !

Merci d'avoir lu mon article sur comment implémenter la tokenisation en utilisant JWT et Django Rest Framework. Je suis toujours partante pour une bonne discussion sur le codage et la technologie, alors suivez-moi sur [Twitter](https://twitter.com/VeldaKiara) et continuons la conversation là-bas.