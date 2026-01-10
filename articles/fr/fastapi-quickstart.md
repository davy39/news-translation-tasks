---
title: Manuel FastAPI – Comment développer, tester et déployer des API
date: '2023-07-25T20:54:10.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/fastapi-quickstart
posteditor: ''
proofreader: ''
author: Atharva Shah
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/FastAPI-Handbook-Cover.png
tags:
- name: FastAPI
  slug: fastapi
- name: handbook
  slug: handbook
- name: Python
  slug: python
seo_desc: 'Welcome to the world of FastAPI, a sleek and high-performance web framework
  for constructing Python APIs. Don''t worry if you''re new to API programming – we''ll
  start at the beginning.

  An API (Application Programming Interface) connects several softwar...'
---


Par Atharva Shah

<!-- more -->

Bienvenue dans le monde de FastAPI, un framework web élégant et performant pour construire des API Python. Ne vous inquiétez pas si vous êtes novice en programmation d'API – nous allons commencer par le début.

Une **API** (Application Programming Interface) connecte plusieurs programmes logiciels en leur permettant de converser et d'échanger des informations. Les API sont essentielles dans le développement logiciel moderne car elles constituent l'architecture backend d'une application.

Après avoir lu ce guide de démarrage rapide, vous serez capable de développer une API d'administration de cours en utilisant **[FastAPI][1]** et **[MongoDB][2]**. Le plus intéressant est que vous n'allez pas seulement écrire des API, mais aussi tester et conteneuriser l'application.

Dans ce projet guidé, nous allons créer un système backend Python utilisant FastAPI, un framework web rapide, et une base de données MongoDB pour le stockage et la récupération des informations sur les cours.

Le système permettra aux utilisateurs d'accéder aux détails des cours, de consulter les chapitres, de noter les chapitres individuels et d'agréger les évaluations.

Le projet est conçu pour les développeurs Python ayant des connaissances de base en programmation et quelques notions de NoSQL. La familiarité avec MongoDB, Docker et PyTest n'est pas requise puisque je vais mettre en évidence tout ce que vous devez savoir dans le cadre de ce projet.

## Ce que nous allons construire

Voici ce que nous allons construire :

**Backend FastAPI :** Il servira d'interface pour gérer les requêtes et les réponses de l'API. FastAPI a été choisi pour sa facilité d'utilisation, ses performances et sa conception intuitive.

**Base de données MongoDB :** Une base de données NoSQL pour stocker les informations sur les cours. Le schéma flexible de MongoDB nous permet de stocker des données dans des documents de type JSON, ce qui le rend adapté à ce projet.

**Informations sur les cours :** Les utilisateurs pourront consulter divers détails sur les cours, tels que le nom du cours, la description, l'instructeur, etc.

**Détails des chapitres :** Le système fournira des informations sur les chapitres d'un cours, y compris les noms des chapitres, les descriptions et toute autre donnée pertinente.

**Évaluation des chapitres :** Les utilisateurs auront la possibilité de noter des chapitres individuels. Nous implémenterons une fonctionnalité pour enregistrer et récupérer les évaluations des chapitres.

**Évaluation agrégée du cours :** Le système calculera et affichera l'évaluation agrégée pour chaque cours en fonction des notes de ses chapitres.

Ce tutoriel montre comment configurer un environnement de développement, construire un backend FastAPI, intégrer MongoDB, définir des points de terminaison API, ajouter une fonctionnalité d'évaluation des chapitres et calculer les évaluations agrégées des cours. Il couvre les concepts fondamentaux du projet ainsi que Python, MongoDB et les bases de données NoSQL.

À la fin, ce système backend utile gérera les détails des chapitres, les informations sur les cours et les évaluations des utilisateurs, servant de base à un projet complexe et gratifiant.

L'objectif est de créer un système qui traite les requêtes liées aux cours. Les informations sur les cours doivent ensuite être récupérées de MongoDB en fonction de la requête. Enfin, ces données de réponse doivent être renvoyées dans un format standard (JSON).

Nous commencerons par un script qui lit les informations sur les cours à partir de `courses.json`. Ces données seront stockées dans l'instance MongoDB. Une fois les données chargées, notre code API pourra se connecter à cette base de données pour permettre une récupération simple des données.

L'aspect intéressant est la création de plusieurs points de terminaison avec FastAPI. Notre API sera capable de :

-   Récupérer une liste de tous les cours
-   Afficher un aperçu complet d'un cours
-   Lister des informations détaillées sur certains chapitres
-   Enregistrer les scores des utilisateurs pour chaque chapitre.

De plus, pour chaque cours, nous agrégerons tous les avis, fournissant aux visiteurs des informations pertinentes concernant la popularité et la qualité du cours.

Ce tutoriel se concentre sur la construction d'une API évolutive, efficace et conviviale. Une fois que nous aurons tout testé, nous conteneuriserons l'application à l'aide de Docker. Cela simplifiera grandement le déploiement, la maintenance et l'installation.

## Table des matières

Voici les sections de ce tutoriel :

-   [Méthodes API][3]
-   [Client et Serveur][4]
-   [Comment configurer la base de données MongoDB][5]
-   [Comment analyser et insérer les données de cours dans MongoDB][6]
-   [Comment concevoir les points de terminaison FastAPI][7]
-   [Tests automatisés des points de terminaison API avec PyTest][8]
-   [Comment conteneuriser l'application avec Docker][9]
-   [Conclusion][10]

## Méthodes API

Les méthodes HTTP (Hypertext Transfer Protocol) spécifient l'action à entreprendre sur une ressource. Voici les méthodes les plus souvent utilisées dans le développement d'API :

**GET** : Demande des informations à un serveur. Lorsqu'un client soumet une requête GET, il demande des données au serveur.

**POST** : Envoie des données au serveur pour traitement. Lorsqu'un client soumet une requête POST, il livre souvent des données au serveur pour créer ou mettre à jour une ressource.

**PUT** : Met à jour les données du serveur. Lorsqu'un client soumet une requête PUT, la ressource indiquée dans la requête est mise à jour.

**DELETE** : Un client envoyant une requête DELETE demande la suppression de la ressource spécifiée.

## Client et Serveur

Le **client** est souvent une application front-end qui envoie des requêtes au serveur, comme un navigateur web ou une application mobile. Le **serveur**, quant à lui, est l'application back-end chargée de traiter les requêtes des clients et de répondre de manière appropriée.

Une requête est une communication délivrée par le client au serveur qui spécifie l'action prévue et toutes les données requises. La méthode HTTP, l'URL (Uniform Resource Locator), les en-têtes et, dans le cas des requêtes POST ou PUT, la charge utile des données (payload) font tous partie d'une requête.

Après que le serveur a reçu la **requête**, il la traite et renvoie une **réponse**. La réponse est le message renvoyé au client par le serveur qui contient les données demandées ou le résultat de l'activité.

Une réponse comprend généralement un code de statut HTTP indiquant le succès ou l'échec de la requête, ainsi que toutes les données renvoyées au client par le serveur.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-131.png) _Schéma montrant le fonctionnement des API_

## Comment configurer la base de données MongoDB

MongoDB est un type de base de données NoSQL. Elle est non relationnelle et sauvegarde les informations sous forme de collections et de documents.

Installez MongoDB pour votre système d'exploitation à partir du [site officiel.][11]

Maintenant, lancez la commande `mongosh` dans votre terminal pour vérifier si l'installation a réussi.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-125.png) _L'exécution de la commande mongosh devrait donner ce résultat_

Connectez-vous au serveur MongoDB avec **MongoDB Compass**. Je vous recommande de configurer MongoDB en spécifiant des paramètres tels que le numéro de port, le moteur de stockage, l'authentification, etc.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-124.png) _Créer une nouvelle connexion MongoDB_

Maintenant que la connexion est établie, l'étape suivante consiste à créer une base de données ou un "document". Appelez cette base de données "courses". Elle sera vide pour le moment. Dans une minute, nous insérerons les documents à l'aide d'un script Python.

## Comment analyser et insérer les données de cours dans MongoDB

Vous pourriez insérer les enregistrements un par un, mais il est préférable d'utiliser un fichier JSON pour simplifier ce processus. Téléchargez ce fichier [**courses.json**][12] depuis GitHub. Toutes les informations sur les cours y sont présentes (sous forme de liste de cours).

Plus précisément, chaque cours a la structure suivante :

-   **name :** Le titre du cours.
-   **date :** Date de création sous forme de timestamp UNIX.
-   **description :** La description du cours.
-   **domain :** Liste du ou des domaines du cours.
-   **chapters :** Liste des chapitres du cours. Chaque chapitre a un titre et un texte de contenu.

Vous aurez besoin de quelques packages Python pour ce projet.

-   **`BSON`** - Format de sérialisation binaire utilisé dans MongoDB pour un stockage et une récupération efficaces des données. Il est inclus avec PyMongo.
-   **`FastAPI`** - Framework web pour créer des API Python offrant des performances élevées, une validation automatique, une documentation interactive et la prise en charge des opérations asynchrones.
-   **`PyMongo`** - Pilote MongoDB officiel pour Python. Il sert d'API de haut niveau pour intégrer MongoDB dans Python.
-   **`Uvicorn`** - Serveur ASGI principal qui améliore les performances des applications. Il est responsable du démarrage du serveur.
-   **`Starlette`** - Framework ASGI qui propulse FastAPI et permet un développement rapide de prototypes.
-   **`Pydantic`** - Bibliothèque intégrée de validation et d'analyse de données. Nous en avons besoin pour créer une documentation d'API interactive tout en validant automatiquement les données des requêtes entrantes et en appliquant des règles de type de données.

Installez-les via les commandes pip comme ceci :

```
pip install fastapi pymongo uvicorn starlette pydantic
```

Maintenant, écrivons un script Python pour insérer toutes ces données de cours dans la base de données afin de pouvoir commencer à construire les routes de l'API. Lancez votre IDE, créez un fichier nommé `script.py` et assurez-vous qu'il se trouve dans le même répertoire que le fichier `courses.json`.

```
""" 
Script to parse course information from courses.json, create the appropriate databases and
collection(s) on a local instance of MongoDB, create the appropriate indices (for efficient retrieval)
and finally add the course data on the collection(s).
"""

import pymongo
import json

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["courses"]
collection = db["courses"]

# Read courses from courses.json
with open("courses.json", "r") as f:
    courses = json.load(f)

# Create index for efficient retrieval
collection.create_index("name")

# add rating field to each course
for course in courses:
    course['rating'] = {'total': 0, 'count': 0}

# add rating field to each chapter
for course in courses:
    for chapter in course['chapters']:
        chapter['rating'] = {'total': 0, 'count': 0}

# Add courses to collection
for course in courses:
    collection.insert_one(course)

# Close MongoDB connection
client.close()
```

Ce script remplit une base de données MongoDB avec les informations sur les cours provenant du fichier JSON.

Il commence par se connecter à l'instance locale de MongoDB. Il lit les données des cours à partir d'un fichier nommé `courses.json` et crée un nouveau champ pour les évaluations des cours. Il développe ensuite un index pour accélérer la récupération des données. Enfin, les données des cours sont ajoutées à la collection MongoDB.

C'est un script simple pour gérer les données de cours dans une base de données. Lors de l'exécution du script, tous les enregistrements de `courses.json` devraient avoir été insérés dans la base de données "courses". Basculez vers MongoDB Compass pour le vérifier.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-116.png) _Vous devriez pouvoir voir les éléments JSON dans votre base de données courses après avoir exécuté le script python_

## Comment concevoir les points de terminaison FastAPI

Ces points de terminaison API offrent un moyen efficace de gérer les informations sur les cours, de récupérer les détails des cours et de permettre les interactions des utilisateurs pour noter les chapitres.

Je recommande de concevoir d'abord les points de terminaison de l'API ainsi que le type de requête HTTP avant d'écrire le code. Cela sert de bonne référence et apporte de la clarté pendant le processus de codage.

| Point de terminaison | Type de requête | Description |
| --- | --- | --- |
| /courses | GET | Obtenir une liste de tous les cours disponibles avec des options de tri. <br><br>Options : Trier par titre (croissant), date (décroissant) ou évaluation totale du cours (décroissant). <br><br>Le filtrage optionnel basé sur le domaine est pris en charge. |
| /courses/{course\_id} | GET | Obtenir l'aperçu d'un cours spécifique identifié par course\_id. |
| /courses/{course\_id}/{chapter\_id} | GET | Obtenir des informations sur un chapitre spécifique au sein d'un cours. |
| /courses/{course\_id}/{chapter\_id} | POST | Noter un chapitre spécifique au sein d'un cours. <br><br>Options : Évaluation positive (1), évaluation négative (-1). <br><br>Les évaluations sont agrégées pour chaque cours. |

D'accord, il est temps de plonger dans le code de l'API. Créez un tout nouveau fichier Python et appelez-le `main.py` :

```
import contextlib
from fastapi import FastAPI, HTTPException, Query
from pymongo import MongoClient
from bson import ObjectId
from fastapi.encoders import jsonable_encoder

app = FastAPI()
client = MongoClient('mongodb://localhost:27017/')
db = client['courses']
```

Le code importe les modules essentiels et crée une instance active de la classe FastAPI nommée `app`. Il établit également une connexion à la base de données locale MongoDB en utilisant la bibliothèque PyMongo, et la variable `db` stocke maintenant la référence de connexion au document des cours.

Examinons maintenant chacun de ces points de terminaison plus en détail.

### Le point de terminaison de récupération de tous les cours (`/courses` – GET)

Ce point de terminaison vous permet de récupérer une liste de tous les cours disponibles. Vous pouvez trier les cours selon différents critères, tels que l'ordre alphabétique (basé sur le titre du cours par ordre croissant), la date (par ordre décroissant) ou l'évaluation totale du cours (par ordre décroissant). De plus, nous permettrons aux utilisateurs de filtrer les cours en fonction de leur domaine.

```
@app.get('/courses')
def get_courses(sort_by: str = 'date', domain: str = None):
    # set the rating.total and rating.count to all the courses based on the sum of the chapters rating
    for course in db.courses.find():
        total = 0
        count = 0
        for chapter in course['chapters']:
            with contextlib.suppress(KeyError):
                total += chapter['rating']['total']
                count += chapter['rating']['count']
        db.courses.update_one({'_id': course['_id']}, {'$set': {'rating': {'total': total, 'count': count}}})


    # sort_by == 'date' [DESCENDING]
    if sort_by == 'date':
        sort_field = 'date'
        sort_order = -1

    # sort_by == 'rating' [DESCENDING]
    elif sort_by == 'rating':
        sort_field = 'rating.total'
        sort_order = -1

    # sort_by == 'alphabetical' [ASCENDING]
    else:  
        sort_field = 'name'
        sort_order = 1

    query = {}
    if domain:
        query['domain'] = domain


    courses = db.courses.find(query, {'name': 1, 'date': 1, 'description': 1, 'domain':1,'rating':1,'_id': 0}).sort(sort_field, sort_order)
    return list(courses)
```

Ce code définit un point de terminaison dans l'application FastAPI pour récupérer une liste de tous les cours disponibles. Le point de terminaison est accessible via une requête HTTP GET sur l'URL '/courses'.

Le décorateur `@app.get()` est attaché à la fonction `get_courses` et s'en occupe.

Lorsqu'une requête est faite à ce point de terminaison, le code calcule d'abord l'évaluation totale du cours en additionnant les notes de tous les chapitres de chaque cours. Il met ensuite à jour le champ `rating` de chaque cours dans la base de données MongoDB avec le total calculé et le nombre d'évaluations.

Ensuite, le code détermine le mode de tri en fonction du paramètre de requête `sort_by`. Si `sort_by` est défini sur `date`, les cours seront triés par leur date de création par ordre décroissant. S'il est défini sur `rating`, les cours seront triés par leur évaluation totale par ordre décroissant. Sinon, les cours seront triés par ordre alphabétique de leurs noms par ordre croissant.

Si le paramètre de requête optionnel `domain` est fourni, le code filtrera les cours en fonction du domaine spécifié.

Enfin, le code interroge la base de données MongoDB pour récupérer les informations pertinentes sur les cours, notamment le nom du cours, la date de création, la description, le domaine et l'évaluation. Les cours sont triés selon le mode de tri sélectionné et renvoyés sous forme de liste.

C'était l'explication du code, mais qu'en est-il de la réponse réelle de l'API ? Exécutez la commande ci-dessous dans votre terminal depuis le répertoire de travail actuel :

```
uvicorn main:app --reload
```

Uvicorn est un serveur web ASGI. Vous pouvez interagir avec les points de terminaison de l'API directement sur votre machine locale sans aucun serveur externe. En exécutant la commande ci-dessus, vous devriez voir un message de succès indiquant que le serveur a démarré.

Lancez votre navigateur et entrez [`http://127.0.0.1:8000/courses`][13] dans la barre d'URL. Le résultat que vous verrez sera la réponse JSON directement du serveur.

Vérifiez que le premier objet contient les éléments suivants :

```
{
"name": "Introduction to Programming",
"date": 1659906000,
"description": "An introduction to programming using a language called Python. Learn how to read and write code as well as how to test and \"debug\" it. Designed for students with or without prior programming experience who'd like to learn Python specifically. Learn about functions, arguments, and return values (oh my!); variables and types; conditionals and Boolean expressions; and loops. Learn how to handle exceptions, find and fix bugs, and write unit tests; use third-party libraries; validate and extract data with regular expressions; model real-world entities with classes, objects, methods, and properties; and read and write files. Hands-on opportunities for lots of practice. Exercises inspired by real-world programming problems. No software required except for a web browser, or you can write code on your own PC or Mac.",
"domain": [
    "programming"
    ],
"rating": {
    "total": 6,
    "count": 12
    }
}
```

Devinez quoi ? C'est une liste de tous les cours que nous avons stockés dans notre base de données. Votre application front-end peut maintenant itérer sur tous ces éléments et les présenter de manière élégante à l'utilisateur. C'est là toute la puissance des API.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-117.png) _L'évaluation de l'ensemble du cours sera mise à jour selon la somme agrégée des chapitres comme mentionné dans le document de mission._

À ce stade, si vous souhaitez voir la documentation de votre API, faites-le en naviguant vers le point de terminaison [`http://127.0.0.1:8000/docs`][14]. Cette API navigable est pré-packagée avec FastAPI. N'est-ce pas génial ?

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-126.png) _Documentation FastAPI pour tous vos points de terminaison API_

Vous n'aimez pas l'aspect classique de la documentation ? Ne vous inquiétez pas, il existe également un point de terminaison `/redoc` avec une interface un peu plus sophistiquée. Naviguez simplement vers `http://127.0.0.1:8000/redoc` et vous serez accueilli par cet écran.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-127.png) _Interface alternative Redoc de FastAPI avec options de recherche et de téléchargement_

### Le point de terminaison d'aperçu d'un cours (`/courses/{course_id}` – GET)

Vous utiliserez ce point de terminaison pour obtenir un aperçu d'un cours spécifique. Fournissez simplement le `course_id` dans l'URL, et l'API renverra des informations détaillées sur ce cours particulier.

```
@app.get('/courses/{course_id}')
def get_course(course_id: str):
    course = db.courses.find_one({'_id': ObjectId(course_id)}, {'_id': 0, 'chapters': 0})
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    try:
        course['rating'] = course['rating']['total']
    except KeyError:
        course['rating'] = 'Not rated yet' 

    return course
```

Cet extrait de code recherche dans la base de données MongoDB le cours avec le `course_id` spécifié et extrait les informations du cours tout en omettant le champ `chapters`.

S'il ne trouve pas le cours, il lève une `HTTPException` avec le code de statut 404. S'il le trouve, il tente d'accéder au champ `rating` et le remplace par sa valeur 'total' pour afficher l'évaluation totale. Sinon, la case `rating` est définie sur `Not rated yet`.

Enfin, sans le champ `chapters`, il renvoie la réponse JSON des informations sur le cours, y compris l'évaluation totale.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-118.png) _Réponse du point de terminaison d'aperçu d'un seul cours_

### Point de terminaison d'informations sur un chapitre spécifique (`/courses/{course_id}/{chapter_id}` – GET)

L'appel de ce point de terminaison renvoie des informations spécifiques sur un chapitre au sein d'un cours. En spécifiant à la fois le `course_id` et le `chapter_id` dans l'URL, vous pouvez accéder aux détails de ce chapitre particulier.

```
@app.get('/courses/{course_id}/{chapter_id}')
def get_chapter(course_id: str, chapter_id: str):    
    course = db.courses.find_one({'_id': ObjectId(course_id)}, {'_id': 0, })
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    chapters = course.get('chapters', [])
    try:
        chapter = chapters[int(chapter_id)]
    except (ValueError, IndexError) as e:
        raise HTTPException(status_code=404, detail='Chapter not found') from e
    return chapter
```

Comme vous pouvez vous y attendre, `course_id` est l'identité du cours, et `chapter_id` est l'identifiant du chapitre à l'intérieur de ce cours.

Lorsqu'une requête est faite à ce point de terminaison, le code recherche d'abord dans la base de données MongoDB le cours avec le `course_id` spécifié, en ignorant la colonne `_id` dans la réponse.

Si le cours avec le `course_id` fourni ne peut être trouvé dans la base de données, le code lève une HTTPException avec le code de statut 404, indiquant que le cours n'a pas pu être localisé.

Le code utilise ensuite la fonction `get` pour récupérer la liste des chapitres du cours, en définissant la valeur par défaut sur une liste vide si le champ 'chapters' n'existe pas.

En utilisant le `chapter_id` fourni dans la requête, le code tente ensuite de récupérer le chapitre exact dans la liste des chapitres. Si le `chapter_id` n'est pas un entier valide ou est hors de portée pour la liste des chapitres, le code lève une HTTPException avec le code de statut 404. Cela indique qu'il n'a pas pu localiser le chapitre.

S'il localise le chapitre, la réponse contient des informations sur le chapitre individuel au sein du cours.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-119.png) _Point de terminaison des détails du chapitre_

### Point de terminaison d'évaluation d'un chapitre (`/courses/{course_id}/{chapter_id}` – POST)

Ce point de terminaison permet aux utilisateurs de noter des chapitres individuels au sein d'un cours. Vous pouvez fournir une note de 1 pour un avis positif ou -1 pour un avis négatif. L'API agrège toutes les évaluations pour chaque cours, fournissant un retour précieux pour les améliorations futures.

Jusqu'à présent, nous avons principalement vu des requêtes GET. Mais voyons maintenant comment vous pouvez envoyer des données au serveur, les valider et les insérer dans la base de données de l'application.

```
@app.post('/courses/{course_id}/{chapter_id}')
def rate_chapter(course_id: str, chapter_id: str, rating: int = Query(..., gt=-2, lt=2)):
    course = db.courses.find_one({'_id': ObjectId(course_id)}, {'_id': 0, })
    if not course:
        raise HTTPException(status_code=404, detail='Course not found')
    chapters = course.get('chapters', [])
    try:
        chapter = chapters[int(chapter_id)]
    except (ValueError, IndexError) as e:
        raise HTTPException(status_code=404, detail='Chapter not found') from e
    try:
        chapter['rating']['total'] += rating
        chapter['rating']['count'] += 1
    except KeyError:
        chapter['rating'] = {'total': rating, 'count': 1}
    db.courses.update_one({'_id': ObjectId(course_id)}, {'$set': {'chapters': chapters}})
    return chapter
```

Nous avons mis en place un point de terminaison pour que les utilisateurs notent chaque chapitre d'un cours à l'aide d'une requête HTTP POST vers l'URL `/courses/course_id/chapter_id`. Les utilisateurs peuvent fournir une valeur de note de 1 pour une évaluation positive ou -1 pour une évaluation négative. Le code interroge la base de données MongoDB pour trouver le cours avec le `course_id` spécifié, en excluant le champ `_id`.

S'il ne trouve pas le cours, il lève une exception HTTP avec un code de statut de 404. Le code récupère la liste des chapitres, en définissant la valeur par défaut sur une liste vide.

Si le `chapter_id` n'est pas un entier valide ou est hors de portée, il lève une `HTTPException` avec un code de statut de 404. Si le chapitre est trouvé, le code met à jour sa note en incrémentant la valeur de la note `total` avec la note fournie et en incrémentant la valeur `count`.

Si le chapitre n'a pas de champ `rating` existant, il en crée un et l'initialise avec la note fournie et un compte de 1. La note mise à jour est ensuite enregistrée dans la base de données, et le chapitre mis à jour est renvoyé en réponse, fournissant un retour à l'utilisateur sur sa note pour ce chapitre.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-120.png) _Requête POST pour ajouter une évaluation à un chapitre_

Pour effectuer une requête POST, ouvrez la documentation et cliquez sur la requête mise en évidence dans l'image ci-dessus. Ensuite, cliquez sur "Try it out", remplissez les données du post et appuyez sur le bouton "Execute" juste en dessous. Cela envoie les données POST au serveur qui sont ensuite validées.

Si toutes les données soumises sont conformes aux attentes, le serveur les accepte et affiche le code de statut 200, ce qui signifie que l'opération a réussi. Les données soumises sont maintenant dans le document MongoDB.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-121.png) _Succès de la requête POST_

C'est tout pour la partie développement de l'API.

## Tests automatisés des points de terminaison API avec PyTest

À mesure que la complexité des applications web modernes augmente, le nombre de points de terminaison d'API et leurs interactions augmentent également.

Dans une application web d'e-commerce dynamique, il pourrait y avoir des centaines de points de terminaison, chacun prenant en charge plusieurs méthodes de requête HTTP. Et ces points de terminaison pourraient être étroitement interconnectés.

Garantir le bon fonctionnement de tous ces points de terminaison après chaque itération de développement devient une tâche colossale pour les développeurs et les équipes QA. C'est là que les tests automatisés viennent à la rescousse.

Créez un fichier `test_app.py` dans le même répertoire que `courses.json` et `main.py` :

```
from fastapi.testclient import TestClient
from pymongo import MongoClient
from bson import ObjectId
import pytest
from main import app

client = TestClient(app)
mongo_client = MongoClient('mongodb://localhost:27017/')
db = mongo_client['courses']
```

Cela configure un environnement de test automatisé.

Le **TestClient de FastAPI** simule des requêtes HTTP vers l'application web. Avec cela, vous pouvez prétendre être un utilisateur, envoyer des requêtes à votre application et recevoir des réponses, tout comme le ferait un utilisateur réel.

Nous utilisons une **connexion MongoDB** pour le stockage des données de cours, avec `MongoClient` permettant l'interaction et la mise à jour des données pendant les tests.

La **base de données de test** est une base de données distincte pour les tests. Elle n'affectera pas les documents de cours réels.

Avec cette configuration, vous pouvez maintenant créer des fonctions de test qui envoient des requêtes à votre application FastAPI en utilisant le `TestClient`. Vous interagirez avec votre base de données MongoDB pendant ces tests, mais ne vous inquiétez pas — c'est juste la base de données de test, donc rien d'important ne sera endommagé.

### Comment tester le point de terminaison "Get Courses List"

Ces fonctions de test utilisent `TestClient` pour interagir avec le point de terminaison "/courses" de l'application FastAPI. Elles vérifient si le point de terminaison se comporte comme prévu lorsque différents paramètres, tels que le tri et le filtrage par domaine, sont fournis.

Les tests vérifient les codes de statut, la présence de données, l'ordre de tri et le filtrage par domaine dans les réponses de l'API, garantissant que la fonctionnalité du point de terminaison des cours est correcte et fiable.

```
def test_get_courses_no_params():
    response = client.get("/courses")
    assert response.status_code == 200

def test_get_courses_sort_by_alphabetical():
    response = client.get("/courses?sort_by=alphabetical")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['name']) == courses


def test_get_courses_sort_by_date():
    response = client.get("/courses?sort_by=date")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['date'], reverse=True) == courses

def test_get_courses_sort_by_rating():
    response = client.get("/courses?sort_by=rating")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert sorted(courses, key=lambda x: x['rating']['total'], reverse=True) == courses

def test_get_courses_filter_by_domain():
    response = client.get("/courses?domain=mathematics")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])

def test_get_courses_filter_by_domain_and_sort_by_alphabetical():
    response = client.get("/courses?domain=mathematics&sort_by=alphabetical")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])
    assert sorted(courses, key=lambda x: x['name']) == courses

def test_get_courses_filter_by_domain_and_sort_by_date():
    response = client.get("/courses?domain=mathematics&sort_by=date")
    assert response.status_code == 200
    courses = response.json()
    assert len(courses) > 0
    assert all([c['domain'][0] == 'mathematics' for c in courses])
    assert sorted(courses, key=lambda x: x['date'], reverse=True) == courses
```

Prêtez attention aux instructions `assert`. Les résultats attendus sont vérifiés par rapport aux résultats réels et renvoient un booléen `True` ou `False` basé sur cette comparaison. L'objectif est de faire passer tous les tests en égalisant ces valeurs.

### Comment tester le point de terminaison "Get Single Course Info"

Les tests utilisent `TestClient` pour envoyer des requêtes au point de terminaison "/courses/course_id" de FastAPI, récupérant les données du cours depuis la base de données MongoDB à l'aide de la fonction `db.courses.find_one`. Comparer les données de réponse de l'API aux données de la base de données peut vous aider à déterminer si le point de terminaison gère correctement les ID de cours existants et inexistants.

```
def test_get_course_by_id_exists():
    response = client.get("/courses/6431137ab5da949e5978a281")
    assert response.status_code == 200
    course = response.json()
    # get the course from the database
    course_db = db.courses.find_one({'_id': ObjectId('6431137ab5da949e5978a281')})
    # get the name of the course from the database
    name_db = course_db['name']
    # get the name of the course from the response
    name_response = course['name']
    # compare the two
    assert name_db == name_response


def test_get_course_by_id_not_exists():
    response = client.get("/courses/6431137ab5da949e5978a280")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Course not found'}
```

### Comment tester le point de terminaison "Get Course Chapter Info"

Les tests prévoient que le point de terminaison "/courses/course_id/chapter_number" de l'application FastAPI fournisse des informations sur le chapitre pour un certain ID de cours et numéro lorsqu'ils utilisent le `TestClient` pour effectuer la requête.

Nous utilisons des assertions pour déterminer si la réponse inclut les données prévues ou donne une réponse "Not Found" pour un chapitre inexistant. Cela valide que le bon chapitre de l'API a été récupéré et gère les chapitres existants et inexistants.

```
def test_get_chapter_info():
    response = client.get("/courses/6431137ab5da949e5978a281/1")
    assert response.status_code == 200
    chapter = response.json()
    assert chapter['name'] == 'Big Picture of Calculus'
    assert chapter['text'] == 'Highlights of Calculus'


def test_get_chapter_info_not_exists():
    response = client.get("/courses/6431137ab5da949e5978a281/990")
    assert response.status_code == 404
    assert response.json() == {'detail': 'Chapter not found'}
```

### Comment tester le point de terminaison "Post Course Rating"

Pour tester la capacité d'évaluation, la fonction de test spécifie l'ID du cours, l'ID du chapitre et les variables de note. Elle utilise la méthode `post` du `TestClient` pour soumettre une requête POST à l'API "/courses/course_id/chapter_id", en fournissant l'ID du cours et le numéro du chapitre dans l'URL et en passant la variable de note comme paramètre de requête.

FastAPI imite l'activité d'un utilisateur pour noter un certain chapitre d'un cours. La réponse est réussie avec un code de statut 200. Le contenu JSON est validé pour les clés "name" et "rating", ainsi que les clés "total" et "count". L'évaluation totale et le nombre d'évaluations sont supérieurs à 0, indiquant que des utilisateurs ont noté le chapitre.

```
def test_rate_chapter():
    course_id = "6431137ab5da949e5978a281"
    chapter_id = "1"
    rating = 1

    response = client.post(f"/courses/{course_id}/{chapter_id}?rating={rating}")

    assert response.status_code == 200

    # Check if the response body has the expected structure
    assert "name" in response.json()
    assert "rating" in response.json()
    assert "total" in response.json()["rating"]
    assert "count" in response.json()["rating"]

    assert response.json()["rating"]["total"] > 0
    assert response.json()["rating"]["count"] > 0

def test_rate_chapter_not_exists():
    response = client.post("/courses/6431137ab5da949e5978a281/990/rate", json={"rating": 1})
    assert response.status_code == 404
    assert response.json() == {'detail': 'Not Found'}
```

Cette vérification s'assure que le point de terminaison d'ajout d'évaluation fonctionne comme prévu, l'API renvoyant le bon code de succès et les informations attendues sur le chapitre, y compris son nom et les détails de l'évaluation mise à jour.

En exécutant la commande `pytest`, toutes les fonctions de test du fichier `test_app.py` seront exécutées, et vous obtiendrez un retour sur le fonctionnement des points de terminaison ou sur d'éventuelles erreurs ou régressions. Cela permet aux développeurs et aux équipes QA de détecter les problèmes tôt dans le cycle de développement et de maintenir la fiabilité et la stabilité de l'application.

Comme vous pouvez le voir dans l'image ci-dessous, tous les tests passent. Beau travail ! À mesure que vous continuez à ajouter des fonctionnalités et des points de terminaison à l'application, continuez à ajouter les tests associés afin de valider l'exactitude. C'est ce qu'on appelle le [Développement piloté par les tests (TDD)][15].

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-122.png) _Exécution des tests d'API avec Pytest_

L'exécution de la commande Pytest affiche le résultat illustré dans l'image ci-dessus. Elle indique que 13 tests ont réussi. Cela signifie que tous nos points de terminaison sont fonctionnels et renvoient les réponses attendues.

En détectant les régressions, en intégrant les composants, en résolvant les erreurs, en effectuant des tests de charge et de performance, et en testant la sécurité, le test des points de terminaison vérifie que les opérations essentielles d'une application sont correctes. Toutes les faiblesses et vulnérabilités potentielles sont notées et marquées pour inspection.

Pytest vous aide à vous assurer que les points de terminaison de l'API fonctionnent bien ensemble, et vous aide également à gérer les échecs et les cas limites. Il peut gérer de nombreuses requêtes volumineuses simultanées dans des situations réelles.

## Comment conteneuriser l'application avec Docker

Vous pouvez regrouper votre application et toutes ses dépendances dans une seule unité appelée conteneur. C'est ce qu'on appelle la **conteneurisation**. Elle sépare l'application du système sous-jacent, ce qui maintient la cohérence sur différents systèmes d'exploitation.

**Docker** est une technologie de conteneurisation moderne qui facilite la création, la distribution et l'exécution de conteneurs. Il permet aux développeurs de construire, d'expédier et d'exécuter des applications de manière cohérente et reproductible sans avoir à les compiler à partir des sources.

Installez Docker à partir d'ici : [https://www.docker.com/get-started][16].

Dockeriser des programmes Python vous aide à vous assurer qu'ils s'exécutent de manière cohérente sur plusieurs ordinateurs, éliminant les problèmes de compatibilité. Cela conteneurise le logiciel, ses dépendances et ses personnalisations, le rendant portable.

Dans le même répertoire que les autres fichiers, créez un nouveau fichier nommé `Dockerfile`. Notez qu'il ne nécessite aucune extension.

```
# Use an official Python runtime as a parent image
FROM python:3.9-slim-buster

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /code
WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app

# Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]
```

En commençant par l'image officielle Python 3.9 slim, le Dockerfile définit le plan de l'image.

Il change le répertoire de travail en `/app`, où le code de l'application sera stocké. Les exigences de ce projet sont listées dans le fichier `requirements.txt`, qui a été placé dans le conteneur.

La commande `RUN` utilise pip pour installer les dépendances Python. `COPY` déplace le code de l'application de l'hôte vers le répertoire `/app` du conteneur. `CMD` fournit la commande qui sera exécutée au démarrage du conteneur.

Dans ce cas, il exécute `uvicorn main:app` (l'application FastAPI `main.py`) avec l'hôte défini sur `0.0.0.0` et le port `80`.

### Comment exécuter le conteneur Docker

Construisez l'image Docker dans le même répertoire que le Dockerfile en utilisant : `**docker build -t my_python_app .**`

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-123.png) _Conteneurisation de l'application FastAPI avec Docker_

Exécutez le conteneur en mode détaché à l'aide de la commande `**docker run -d -p 80:80 my_python_app**`.

Une fois cela fait, vous pouvez voir l'état des conteneurs et de l'image depuis Docker Desktop.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-128.png) _Docker Desktop montre que notre image de conteneur est maintenant en état d'exécution sur le port 80_

### Comment arrêter le conteneur Docker

Trouvez l'ID ou le nom du conteneur avec `**docker ps**`. Arrêtez le conteneur en utilisant son ID ou son nom : `**docker stop <id_ou_nom_du_conteneur>**`

Ce tutoriel n'a abordé que le développement, les tests et la conteneurisation. Notez simplement qu'après le déploiement, la sécurité des conteneurs, si elle est négligée, introduit des risques tels que des vulnérabilités, des mauvaises configurations et des attaques. Vous devriez idéalement profiter d'une [CNAPP][17] (Cloud Native Application Protection Platform) pour scanner les images, respecter les meilleures pratiques et surveiller les conteneurs en cours d'exécution pour les protéger.

Ce qu'il faut retenir, c'est que la conteneurisation Docker permet de regrouper des scripts Python avec leurs dépendances, les rendant cohérents et portables. Le Dockerfile décrit comment l'image doit être créée.

Exécuter le conteneur après sa construction est aussi simple que de lancer une seule commande. Il est tout aussi simple de l'arrêter. Docker facilite la gestion de la distribution des applications Python.

## Conclusion

Ce tutoriel était un guide de démarrage rapide pour vous aider à exploiter la puissance de FastAPI. Nous avons construit une API d'administration de cours qui gère efficacement les requêtes liées aux cours.

Nous y sommes parvenus en important des données de cours d'un fichier JSON vers MongoDB, puis en créant plusieurs points de terminaison pour que les utilisateurs accèdent aux listes de cours, aux aperçus, aux informations sur les chapitres et aux scores des utilisateurs. Nous avons également ajouté une fonction d'agrégation d'avis pour démontrer l'utilisation des méthodes HTTP POST et HTTP GET afin que vous puissiez récupérer des données ainsi qu'en envoyer au serveur.

PyTest nous a aidés à gérer les tests automatisés, garantissant fiabilité et stabilité. Nous avons ensuite conteneurisé l'application avec Docker, ce qui simplifie le déploiement et la maintenance.

Mon [dépôt Github][18] contient le code complet couvert dans ce tutoriel de démarrage rapide. Abonnez-vous à mon [blog technique][19] pour des fiches mémo techniques et des ressources.

[1]: https://fastapi.tiangolo.com/
[2]: https://www.mongodb.com/
[3]: #heading-methodes-api
[4]: #heading-client-et-serveur
[5]: #heading-comment-configurer-la-base-de-donnees-mongodb
[6]: #heading-comment-analyser-et-inserer-les-donnees-de-cours-dans-mongodb
[7]: #heading-comment-concevoir-les-points-de-terminaison-fastapi
[8]: #heading-tests-automatises-des-points-de-terminaison-api-avec-pytest
[9]: #heading-comment-conteneuriser-l-application-avec-docker
[10]: #heading-conclusion
[11]: https://www.mongodb.com/try/download/community
[12]: https://github.com/HighnessAtharva/fastapi-kimo/blob/master/courses.json
[13]: http://127.0.0.1:8000/courses
[14]: http://127.0.0.1:8000/docs
[15]: https://www.freecodecamp.org/news/an-introduction-to-test-driven-development-c4de6dce5c/
[16]: https://www.docker.com/get-started
[17]: https://www.accuknox.com/blog/cnapp-buyers-guide
[18]: https://github.com/HighnessAtharva/fastapi-kimo/
[19]: https://atharvashah.netlify.app/