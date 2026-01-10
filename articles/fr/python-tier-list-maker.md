---
title: Comment créer un générateur de listes hiérarchisées avec Python
subtitle: ''
author: Atharva Shah
co_authors: []
series: null
date: '2023-07-07T20:48:16.000Z'
originalURL: https://freecodecamp.org/news/python-tier-list-maker
coverImage: https://www.freecodecamp.org/news/content/images/2023/07/python-tier-list-1.png
tags:
- name: projects
  slug: projects
- name: Python
  slug: python
seo_title: Comment créer un générateur de listes hiérarchisées avec Python
seo_desc: 'Hello Pythonistas! Do you want to level up your Python and API skills while
  also building something really useful? Well, then you''re in the right place.

  This hands-on tutorial showcases how to leverage Python''s capabilities to code
  an interactive tie...'
---

Bonjour les Pythonistas ! Vous voulez améliorer vos compétences en Python et en API tout en construisant quelque chose de vraiment utile ? Alors vous êtes au bon endroit.

Ce tutoriel pratique montre comment exploiter les capacités de Python pour coder un générateur de listes hiérarchisées interactif directement dans votre terminal.

Nous utiliserons quelques bibliothèques Python utiles pour construire un outil pratique qui vous permet de classer et d'organiser vos albums préférés de manière engageante et efficace en quelques secondes.

## Aperçu du projet

Les listes hiérarchisées sont des outils de catégorisation utilisés pour classer des objets en fonction des préférences. Elles sont utilisées dans la musique, les films et d'autres domaines. La liste hiérarchisée des albums de ce projet attribue des enregistrements à différents niveaux en fonction de vos choix personnels.

Ce guide étape par étape exploite la puissance des bibliothèques Python comme [**Rich**](https://github.com/Textualize/rich)**,** [**PyLast**](https://github.com/pylast/pylast)**,** [**Pillow**](https://github.com/python-pillow/Pillow)**, et** [**Pick**](https://github.com/wong2/pick) pour créer un générateur de listes hiérarchisées directement dans le terminal.

Imaginez facilement catégoriser vos albums dans différents niveaux, tels que "Niveau S" pour les favoris de tous les temps ou "Niveau B" pour ces pépites méconnues. Vous aurez un contrôle total sur la manière dont votre collection de musique est organisée selon vos préférences.

![Aperçu général de haut niveau du guide](https://www.freecodecamp.org/news/content/images/2023/07/image-8.png align="left")

*Aperçu général de haut niveau du guide*

À la fin de ce projet, vous pourrez exporter toutes vos listes hiérarchisées. Voici un exemple de ce à quoi cela pourrait ressembler. Cela peut être fait pour n'importe quel artiste de votre choix.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/MAC-DEMARCO-TIER-LIST.png align="left")

*Résultat final du projet*

## Obtenez votre clé API LastFM

[LastFM](https://www.last.fm/) est une base de données musicale et une plateforme en ligne qui offre un système sophistiqué de recommandation musicale ainsi qu'une API. Elle permet aux développeurs d'accéder et de télécharger des données depuis leur base de données.

C'est une étape nécessaire car l'application CLI demande les métadonnées des albums et les couvertures depuis l'API LastFM.

Tout d'abord, vous devrez créer un [compte développeur LastFM](https://www.last.fm/api/account/create).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-7.png align="left")

*Ne partagez jamais les informations d'identification de l'API. Utilisez des variables d'environnement pour les stocker.*

Ensuite, copiez la clé API et le secret partagé. Définissez-les comme variables d'environnement.

Sur Windows :

```javascript
setx LASTFM_API_KEY "votre_clé_api"
setx LASTFM_API_SECRET "votre_secret_api"
```

Sur Linux/MacOS :

```javascript
export LASTFM_API_KEY="votre_clé_api"
export LASTFM_API_SECRET="votre_secret_api"
```

## Importer les modules

Voici les modules que vous devez installer pour démarrer le projet :

* `json` : Encodage et décodage des réponses JSON des API.

* `os` : Opérations sur les fichiers et répertoires.

* `datetime` : Formatage et opérations mathématiques sur la date et l'heure.

* `io` : Interface de type flux pour les données binaires en mémoire.

* `typing` : Indication de type pour une meilleure lisibilité.

* `pylast` : Une bibliothèque Python qui enveloppe l'API LastFM.

* `requests` : Faire des requêtes HTTP avec des services et API en ligne.

* `pick` : Un menu de sélection interactif pour choisir dans une liste directement dans le terminal.

* `PIL` : Traitement et manipulation d'images (par exemple, dessin, redimensionnement et sauvegarde).

* `rich` : Formattage élégant du terminal.

Installez ces modules en utilisant pip (le gestionnaire de paquets Python).

```javascript
pip install pylast requests pick Pillow rich
```

Maintenant que la configuration est terminée, lancez votre éditeur de code et commençons à construire.

```py
import json
import os
from datetime import datetime
from io import BytesIO
from typing import List

import pylast
import requests
from pick import pick
from PIL import Image, ImageDraw, ImageFont
from rich import print
from rich.panel import Panel
from rich.table import Table
```

## Démarrer avec un menu interactif

Il s'agit d'une application basée sur CLI. Ainsi, tous les choix que vous faites seront effectués directement dans le terminal. Deux choix sont présentés à l'utilisateur sur l'écran de démarrage :

1. **Créer une liste hiérarchisée** : Entrez le nom de la liste et l'artiste. L'application récupérera les métadonnées et les couvertures d'albums depuis l'API LastFM et les enregistrera dans un fichier JSON.

2. **Exporter la liste hiérarchisée en image** : Utilisez Pandas pour exporter les données JSON collectées vers une belle image PNG/JPG. L'image aura des lignes et des colonnes pour indiquer les niveaux et les albums.

Pour commencer, présentons un menu interactif à l'utilisateur :

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-12.png align="left")

*Le module pick présente un menu de sélection de choix dans le terminal. Utilisez les touches fléchées pour naviguer et appuyez sur Entrée pour confirmer.*

Ignorez les quatre premières options, car elles sont hors du cadre de ce guide. Vous pouvez simplement utiliser l'instruction `pass` au lieu d'invoquer ces fonctions pour éviter toute erreur.

Pour y parvenir, vous devrez écrire le code pilote suivant à la fin de votre fichier.

```py
LASTFM_API_KEY = os.environ.get("LASTFM_API_KEY")
LASTFM_API_SECRET = os.environ.get("LASTFM_API_SECRET")
network = pylast.LastFMNetwork(api_key=LASTFM_API_KEY, api_secret=LASTFM_API_SECRET)

def start():
    global network
    startup_question = "Que voulez-vous faire ?"
    options = ["Noter par album", "Noter les chansons", "Voir les albums notés", "Voir les chansons notées", "Créer une liste hiérarchisée", "Voir les listes hiérarchisées créées", "QUITTER"]
    selected_option, index = pick(options, startup_question, indicator="→")
    
    if index == 0:
        rate_by_album()
    elif index == 1:
        rate_by_song()
    elif index == 2:
        see_albums_rated()
    elif index == 3:
        see_songs_rated()
    elif index == 4:
        create_tier_list()
    elif index == 5:
        see_tier_lists()
    elif index == 6:
        exit()
start()
```

Comme on peut le voir dans le code ci-dessus, la fonction `os.environ.get()` récupère la valeur d'une variable d'environnement que vous avez définie dans la section précédente.

`network` est probablement la variable la plus importante. Elle a beaucoup de méthodes attachées. Ces méthodes incluent :

* Récupération des albums d'un artiste

* Récupération des métadonnées sur un artiste

* Récupération des métadonnées sur un album

* Récupération des couvertures d'albums

* Validation des erreurs en vérifiant le statut de réponse 200 (OK).

Ensuite, `start()` initialise l'application, présente une question de démarrage en utilisant la fonction `pick`, stocke les choix de l'utilisateur et exécute diverses actions en fonction de l'option sélectionnée.

La méthode `pick` accepte les paramètres suivants :

* `**options**` : La liste des options parmi lesquelles choisir. Ce seront les albums de la liste.

* `**title**` : Le titre ou la question à afficher à l'utilisateur. Le nom de la liste hiérarchisée.

* `**multiselect**` : Un indicateur indiquant si plusieurs options peuvent être sélectionnées. Choix multiple ou choix unique.

* `**indicator**` : Le symbole ou le caractère utilisé pour indiquer l'option sélectionnée.

* `**min_selection_count**` : Le nombre minimum d'options qui doivent être sélectionnées. Ce choix ne permet qu'une seule sélection, la valeur par défaut.

Note : **Tout le code ci-dessous doit être placé au-dessus du code pilote**. Nous allons définir plusieurs fonctions, une pour chaque option.

## Comment sauvegarder l'état en JSON

Les fichiers JSON sont faciles à utiliser et à maintenir même lorsque le schéma de l'application change. C'est pourquoi vous allez stocker les données de la liste hiérarchisée au format JSON. C'est une méthode de stockage persistante qui vous permet de mettre à jour les notes des albums et des chansons, ainsi que les listes hiérarchisées, même lorsque le programme est relancé.

Bien sûr, vous ne voulez pas que les données de l'utilisateur soient perdues lorsque l'application redémarre ? Par conséquent, une sauvegarde de l'état est nécessaire. C'est une base de données la plupart du temps. Mais pour simplifier, stockons et récupérons les données de l'utilisateur en utilisant JSON.

```py
def load_or_create_json() -> None:
    if os.path.exists("albums.json"):
        with open("albums.json") as f:
            ratings = json.load(f)
    else:
        # créer un nouveau fichier json avec un dictionnaire vide
        with open("albums.json", "w") as f:
            ratings = {"album_ratings": [], "song_ratings": [], "tier_lists": []}
            json.dump(ratings, f)
```

Cette fonction personnalisée charge un fichier JSON existant ou en crée un s'il n'existe pas. Elle garantit que l'application dispose d'un fichier pour stocker et récupérer les notes des albums et des chansons, ainsi que les listes hiérarchisées.

Si le fichier n'existe pas, il crée un nouveau fichier nommé "albums.json" en mode écriture. Ensuite, initialise la variable `ratings` comme un dictionnaire contenant des listes vides. `json.dump()` écrit le contenu du dictionnaire `ratings` dans le fichier JSON.

## Comment écrire des fonctions utilitaires

Les fonctions utilitaires ou d'assistance en programmation pilotée par menu effectuent des tâches ou opérations courantes liées aux options de menu. Ces fonctions sont réutilisables et modulaires, rendant le code plus organisé et plus facile à maintenir. Exemples :

* Afficher le menu

* Validation des entrées

* Persistance des données

* Formatage et affichage

* Gestion des erreurs

* Opérations courantes.

Ces fonctions gèrent les tâches courantes requises par plusieurs options de menu, favorisant la réutilisabilité du code et réduisant la redondance. L'encapsulation de ces fonctions dans la logique du menu aide à maintenir le flux de code et facilite les tests, le débogage et les modifications futures.

Pensez à elles comme des ponts qui aident à connecter deux fonctions mieux et isolent la logique triviale qui peut être utilisée à la volée. Ce projet repose sur deux fonctions d'assistance.

### Supprimer l'album de la liste

Tout d'abord, nous allons écrire une fonction pour supprimer l'album sélectionné de la liste afin d'éviter les répétitions entre les différents niveaux. Voici à quoi cela ressemble :

```py
def create_tier_list_helper(albums_to_rank, tier_name):
    # si il n'y a plus d'albums à classer, retourner une liste vide
    if not albums_to_rank:
        return []
    
    question = f"Sélectionnez les albums que vous voulez classer dans {tier_name}"
    tier_picks = pick(options=albums_to_rank, title=question, multiselect=True, indicator="→", min_selection_count=0)
    tier_picks = [x[0] for x in tier_picks]
    
    for album in tier_picks:
        albums_to_rank.remove(album)

    return tier_picks
```

Cela permet aux utilisateurs de classer les albums dans certains niveaux et facilite la création de listes hiérarchisées.

Elle nécessite deux arguments : `albums_to_rank` et `tier_name`. Si il n'y a plus d'albums à classer, la fonction produit une liste vide. Les utilisateurs peuvent choisir des albums à noter parmi les albums à classer, les sauvegarder dans les choix de niveau, les supprimer et retourner la liste des choix de niveau.

La valeur retournée `tier_picks` est une liste Python.

### Retourner la couverture de l'album sélectionné

Ensuite, écrivez une fonction qui retourne la couverture d'un album que les utilisateurs sélectionnent. Voici à quoi cela ressemble :

```py
def get_album_cover(artist, album):
    album = network.get_album(artist, album)
    album_cover = album.get_cover_image()
    # vérifier si c'est une URL valide
    try:
        response = requests.get(album_cover)
        if response.status_code != 200:
            album_cover = "https://community.mp3tag.de/uploads/default/original/2X/a/acf3edeb055e7b77114f9e393d1edeeda37e50c9.png"
    except:
        album_cover = "https://community.mp3tag.de/uploads/default/original/2X/a/acf3edeb055e7b77114f9e393d1edeeda37e50c9.png"
    return album_cover
```

Cela récupère l'image de couverture de l'album pour un artiste et un nom d'album spécifiés via l'API LastFM. Il valide l'URL de l'image de couverture de la réponse de l'API avec une requête HTTP.

La couverture de l'album est retournée si l'URL est correcte. Sinon, une image de remplacement par défaut pour la couverture de l'album est fournie.

L'objet `network` que vous avez créé précédemment a plusieurs méthodes pratiques. La première ligne obtient l'objet album puis obtient l'image de couverture pour cet objet directement via LastFM.

## Comment ajouter les données de la liste hiérarchisée au JSON

Une fois que l'utilisateur choisit l'option "créer une liste hiérarchisée" dans le menu, le script lui présente les niveaux disponibles et lui demande d'entrer un artiste valide et un nom pour sa liste hiérarchisée afin qu'elle puisse être stockée dans le fichier JSON.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-16.png align="left")

*Après avoir choisi l'option "créer une liste hiérarchisée", le script valide l'artiste et retourne les métadonnées en utilisant l'API LastFM.*

Utilisez l'objet `network` pour valider si l'artiste existe. Si oui, demandez tous les albums de cet artiste. Remplissez une liste avec ces albums et définissez l'`option` sur cette liste pour qu'elle apparaisse dans les choix pour le niveau S.

Dans l'image ci-dessous, la marque (x) indique que l'utilisateur a sélectionné cet album particulier pour être dans le niveau S.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-33.png align="left")

*C'est une invite pour les utilisateurs de sélectionner les albums qu'ils veulent déplacer vers le niveau S. Naviguez avec les touches fléchées pour sélectionner zéro, un ou plusieurs albums de la liste.*

Après que l'utilisateur a sélectionné ces albums, vous souhaitez sérialiser cette liste et la mettre dans un fichier JSON qui sera utilisé pour générer l'image réelle plus tard. Ce fichier JSON doit avoir une définition de données.

Pensez à la manière dont les bases de données ont un schéma. Elles ont des tables et des colonnes et des lignes qui décrivent la nature et le format des données.

De même, nous allons définir le schéma du fichier JSON pour stocker tous ces choix de liste hiérarchisée. Chaque objet de liste hiérarchisée contient les propriétés suivantes :

* `tier_list_name` : Le nom donné à la liste hiérarchisée.

* `artist` : Le nom de l'artiste pour lequel la liste hiérarchisée est créée.

* `s_tier`, `a_tier`, `b_tier`, `c_tier`, `d_tier`, `e_tier` : Tableaux qui contiennent les albums et leurs couvertures correspondantes pour chaque niveau. Les albums sont représentés comme des objets avec les propriétés "album" et "cover_art".

* `time` : Horodatage de création.

* Chaque tableau de niveau contient un ou plusieurs objets d'album avec "album" représentant le nom de l'album et "cover_art"

Voici le schéma JSON d'exemple. Une fois que l'utilisateur fait les choix dans le terminal, un objet Python sérialisé similaire à celui-ci contenant les données de la liste hiérarchisée sera écrit dans le fichier JSON.

```json
{
  "tier_lists": [
        {
            "tier_list_name": "THE WEEKND RANKED",
            "artist": "the weeknd",
            "s_tier": [
                {
                    "album": "After Hours",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/7d957bd27dd562bee7aaa89eafa0bbe6.jpg"
                }
            ],
            "a_tier": [
                {
                    "album": "Kiss Land",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/01ad150445023de653c50dbbc3e10dbc.jpg"
                },
                {
                    "album": "Echoes of Silence",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/4f257619898b44b7a8f95431045e9ffe.png"
                }
            ],
            "b_tier": [],
            "c_tier": [],
            "d_tier": [],
            "e_tier": [
                {
                    "album": "I Feel It Coming",
                    "cover_art": "https://lastfm.freetls.fastly.net/i/u/300x300/974deeb8c348d0ad0c0fa10941dd67e8.jpg"
                }
            ],
            "time": "2023-04-23 23:56:14.652417"
        }
    ]
}
```

Vous voulez écrire dynamiquement dans ce fichier JSON à mesure que l'utilisateur continue à créer des listes hiérarchisées. C'est-à-dire qu'il doit continuer à croître et à s'étendre pour s'adapter à toutes les couvertures d'albums. Le code ci-dessous fait exactement cela :

```py
def create_tier_list():
    load_or_create_json()
    with open("albums.json") as f:
        album_file = json.load(f)

    print("NIVEAUX - S, A, B, C, D, E")

    question = "Pour quel artiste voulez-vous créer une liste hiérarchisée ?"
    artist = input(question).strip().lower()
    
    try:
        get_artist = network.get_artist(artist)
        artist = get_artist.get_name()
        albums_to_rank = get_album_list(artist)
        
        # garder uniquement le nom de l'album en divisant la chaîne au premier - et en supprimant le premier élément
        albums_to_rank = [x.split(" - ", 1)[1] for x in albums_to_rank[1:]]

        question = "Comment voulez-vous appeler cette liste hiérarchisée ?"
        tier_list_name = input(question).strip()

        # répéter jusqu'à ce que l'utilisateur entre au moins un caractère
        while not tier_list_name:
            print("Veuillez entrer au moins un caractère")
            tier_list_name = input(question).strip()

        # NIVEAU S
        question = "Sélectionnez les albums que vous voulez classer dans le niveau S :"
        s_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau S")
        s_tier_covers = [get_album_cover(artist, album) for album in s_tier_picks]
        s_tier = [{"album":album,"cover_art": cover} for album, cover in zip(s_tier_picks, s_tier_covers)]
        
        # NIVEAU A
        question = "Sélectionnez les albums que vous voulez classer dans le niveau A :"
        a_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau A")
        a_tier_covers = [get_album_cover(artist, album) for album in a_tier_picks]
        a_tier = [{"album":album,"cover_art": cover} for album, cover in zip(a_tier_picks, a_tier_covers)]
            
        # NIVEAU B
        question = "Sélectionnez les albums que vous voulez classer dans le niveau B :"
        b_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau B")
        b_tier_covers = [get_album_cover(artist, album) for album in b_tier_picks]
        b_tier = [{"album":album,"cover_art": cover} for album, cover in zip(b_tier_picks, b_tier_covers)]
        
        # NIVEAU C
        question = "Sélectionnez les albums que vous voulez classer dans le niveau C :"
        c_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau C")
        c_tier_covers = [get_album_cover(artist, album) for album in c_tier_picks]
        c_tier = [{"album":album,"cover_art": cover} for album, cover in zip(c_tier_picks, c_tier_covers)]
            
        # NIVEAU D
        question = "Sélectionnez les albums que vous voulez classer dans le niveau D :"
        d_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau D")
        d_tier_covers = [get_album_cover(artist, album) for album in d_tier_picks] 
        d_tier = [{"album":album,"cover_art": cover} for album, cover in zip(d_tier_picks, d_tier_covers)]
        # NIVEAU E
        question = "Sélectionnez les albums que vous voulez classer dans le niveau E :"
        e_tier_picks = create_tier_list_helper(albums_to_rank, "Niveau E")
        e_tier_covers = [get_album_cover(artist, album) for album in e_tier_picks]
        e_tier = [{"album":album,"cover_art": cover} for album, cover in zip(e_tier_picks, e_tier_covers)]
        
        # vérifier si tous les niveaux sont vides et si oui, quitter
        if not any([s_tier_picks, a_tier_picks, b_tier_picks, c_tier_picks, d_tier_picks, e_tier_picks]):
            print("Tous les niveaux sont vides. Quitter...")
            return
        
        
        # # ajouter les albums qui ont été sélectionnés à la liste hiérarchisée
        tier_list = {
            "tier_list_name": tier_list_name,
            "artist": artist,
            "s_tier": s_tier, 
            "a_tier": a_tier,
            "b_tier": b_tier,
            "c_tier": c_tier,
            "d_tier": d_tier,
            "e_tier": e_tier,
            "time": str(datetime.now())
        }
        
        # ajouter la liste hiérarchisée au fichier json
        album_file["tier_lists"].append(tier_list)
        
        # sauvegarder le fichier json
        with open("albums.json", "w") as f:
            json.dump(album_file, f, indent=4)
            
        return
    
    except pylast.PyLastError:
        print("\u274c[b red] Artiste non trouvé [/b red]")
```

C'est la fonction principale utilisée pour créer des listes hiérarchisées pour les albums et les stocker dans `albums.json`. Voici ce qui se passe dans cette fonction :

* L'utilisateur entre le nom de l'artiste et récupère les informations depuis l'API LastFM.

* Ensuite, il fournit un nom pour la liste hiérarchisée qu'il souhaite créer.

* Pour chaque niveau (S, A, B, C, D, E), il sélectionne les albums à classer dans ce niveau en utilisant une fonction d'assistance écrite précédemment.

* La récupération des couvertures d'albums pour chaque album sélectionné est effectuée via `get_album_cover()`, et les albums sélectionnés et leurs couvertures correspondantes sont stockés sous forme de dictionnaires dans la liste hiérarchisée respective.

* Si tous les niveaux sont vides, la fonction quitte. Rien n'est écrit dans le fichier JSON.

* Sinon, la liste hiérarchisée est ajoutée au fichier JSON qui est sauvegardé dans le répertoire de travail actuel (même chemin que le script Python).

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-15.png align="left")

*Maintenant, voici la sélection pour le niveau suivant (Niveau A). Les albums que nous avons sélectionnés dans les options précédentes n'apparaissent plus, ce qui signifie qu'ils ont déjà été sélectionnés.*

## Comment utiliser Pillow pour les transformations visuelles

Maintenant que vous avez toutes les données JSON pour vos listes hiérarchisées, vous souhaitez exporter tout cela vers une image afin de pouvoir la partager avec vos amis ou la publier sur le web. Mais comment devriez-vous procéder ? Décomposons cela :

Tout d'abord, vous voudrez déterminer le nombre de niveaux. Ensuite, déterminer la position et la taille de la grille de la liste hiérarchisée ainsi que des carrés de couverture des albums.

Ici, vous voudrez penser aux décalages de largeur et de hauteur dynamiques. Comment devriez-vous prévenir le débordement des images, ajouter de nouvelles lignes ou maintenir une hauteur minimale ?

Tout cela est lié au canevas de l'image. Pillow est un excellent choix pour cela. Vous pouvez redimensionner, ajuster et étendre les dimensions de toutes vos images ainsi que le canevas de fond à la volée en fonction de l'entrée et de la sélection de l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-34.png align="left")

*Modèle de liste hiérarchisée réalisé avec Pillow. Voir le code ci-dessous pour l'explication.*

La manière la plus logique de s'attaquer à cela est de passer l'objet de la liste hiérarchisée à une fonction et de la laisser parcourir tous les niveaux. À l'intérieur de chaque niveau, laissez-la parcourir tous les enregistrements et ajouter un élément. Si la couverture de l'album dépasse la largeur maximale, ajoutez une nouvelle ligne pour qu'elle ne déborde pas. Continuez ainsi jusqu'à ce que tous les albums de chaque niveau soient traités. Violà !

```py
def image_generator(file_name, data):

    # retourner si le fichier existe déjà
    if os.path.exists(file_name):
        return
    
    # Définir la taille de l'image et la police
    image_width = 1920
    image_height = 5000
    font = ImageFont.truetype("arial.ttf", 15)
    tier_font = ImageFont.truetype("arial.ttf", 30)
    
    # Créer une nouvelle image avec la taille et la couleur de fond noire
    image = Image.new("RGB", (image_width, image_height), "black")
    text_cutoff_value = 20

    # Initialiser les variables pour les positions des lignes et des colonnes
    row_pos = 0
    col_pos = 0
    increment_size = 200
    
    """NIVEAU S"""
    # côté le plus à gauche - faire un carré avec du texte à l'intérieur du carré et une couleur de remplissage
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="red")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau S", font=tier_font, fill="white")
        col_pos += increment_size
        
    for album in data["s_tier"]:
        # Obtenir la couverture
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
    
    	# Redimensionner la couverture
        cover_art = cover_art.resize((increment_size, increment_size))
        
        # Coller la couverture sur l'image de base
        image.paste(cover_art, (col_pos, row_pos))
        
        # Dessiner le nom de l'album sur l'image avec une taille de police de 10 et une couleur de fond blanche
        draw = ImageDraw.Draw(image)

        # Obtenir le nom de l'album
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        # Incrémenter la position de la colonne
        col_pos += 200
        # vérifier si la position de la colonne est supérieure à la largeur de l'image
        if col_pos > image_width - increment_size:
            # ajouter une nouvelle ligne
            row_pos += increment_size + 50
            col_pos = 0 

    # ajouter une nouvelle ligne pour séparer les niveaux
    row_pos += increment_size + 50
    col_pos = 0

    """NIVEAU A"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="orange")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau A", font=tier_font, fill="white")
        col_pos += increment_size
        
    for album in data["a_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0 

    row_pos += increment_size + 50
    col_pos = 0
    
    """NIVEAU B"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="yellow")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau B", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["b_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")
        col_pos += 200
        if col_pos > image_width - increment_size:
            # ajouter une nouvelle ligne
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0
    
    """NIVEAU C"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="green")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau C", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["c_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))       
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)

        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0
   

    """NIVEAU D"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="blue")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau D", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["d_tier"]:
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))
        image.paste(cover_art, (col_pos, row_pos))        
        draw = ImageDraw.Draw(image)
        
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")

        col_pos += 200
        if col_pos > image_width - increment_size:
            # ajouter une nouvelle ligne
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0


    """NIVEAU E"""
    if col_pos == 0:
        draw = ImageDraw.Draw(image)
        draw.rectangle((col_pos, row_pos, col_pos + increment_size, row_pos + increment_size), fill="pink")
        draw.text((col_pos + (increment_size//3), row_pos+(increment_size//3)), "Niveau E", font=tier_font, fill="black")
        col_pos += increment_size
        
    for album in data["e_tier"]:
        
        response = requests.get(album["cover_art"])
        cover_art = Image.open(BytesIO(response.content))
        cover_art = cover_art.resize((increment_size, increment_size))    
        image.paste(cover_art, (col_pos, row_pos))
        draw = ImageDraw.Draw(image)
        name = album["album"]
        if len(name) > text_cutoff_value:
            name = f"{name[:text_cutoff_value]}..."

        draw.text((col_pos, row_pos + increment_size), name, font=font, fill="white")
        col_pos += 200
        if col_pos > image_width - increment_size:
            row_pos += increment_size + 50
            col_pos = 0
    
    row_pos += increment_size + 50
    col_pos = 0

	image = image.crop((0, 0, image_width, row_pos))

    image.save(f"{file_name}")
```

Tout d'abord, avec deux paramètres (`nom de fichier` et `data`), cette fonction personnalisée est responsable de la conversion de toutes les données JSON que nous avons stockées en une image de liste hiérarchisée bien organisée.

Elle détermine si le fichier avec le `nom de fichier` spécifié existe et retourne vrai s'il existe. Cela économise du calcul si vous avez déjà créé la liste hiérarchisée avec ce nom.

Vous pouvez voir qu'elle spécifie la taille de l'image et la police pour construire le visuel de la liste hiérarchisée, génère une nouvelle image avec un fond noir, définit des variables pour les positions des lignes et des colonnes, et définit une taille d'incrément.

La fonction génère la partie Niveau S de la liste hiérarchisée, générant un carré avec du texte à l'intérieur qui est rempli de couleur rouge.

Après avoir récupéré les graphiques de couverture pour chaque album dans le niveau S, le titre de l'album est dessiné sur l'image en utilisant une police donnée une fois que l'art de la couverture est mis à l'échelle et placé dessus. Si la position de la colonne est supérieure à la largeur de l'image, une nouvelle ligne est ajoutée.

Ce processus est répété pour les niveaux A, B, C, D et E, chaque niveau ayant sa propre couleur. Si le fichier image n'existe pas déjà, l'image résultante est sauvegardée.

En résumé, cela place toutes les couvertures d'albums en lignes et colonnes à l'intérieur de chaque niveau, et de nouvelles lignes sont introduites si nécessaire pour accommoder la largeur de l'image. Des décalages de largeur et de hauteur dynamiques sont définis pour la croissance naturelle de la largeur et de la hauteur.

![Image](https://www.freecodecamp.org/news/content/images/2023/07/GRIMES-TIER-LIST---FAVORITE-ALBUMS.png align="left")

*Cette image entière est générée avec la bibliothèque Pillow en traitant les données du fichier JSON. Tout d'abord, les niveaux sont définis sur le bord gauche du canevas et séquentiellement, les albums sélectionnés sont placés sur le canevas. Tout débordement est pris en charge en ajoutant une ligne sous la liste hiérarchisée.*

## Comment exporter l'image créée

Vous y êtes presque. Cette fonction finale transmet les données de l'objet de la liste hiérarchisée à la fonction définie précédemment pour rendre une image en utilisant pillow.

Pensez à cela comme un lien de connexion entre deux fonctions. Elle imprime simplement le message de succès ou d'échec dans le CLI pour informer les utilisateurs du statut de la génération de l'image.

```py
def see_tier_lists():
    load_or_create_json()
    with open("albums.json", "r") as f:
        data = json.load(f)

    if not data["tier_lists"]:
        print("\u274c [b red]Aucune liste hiérarchisée n'a encore été créée ![/b red]")
        return
    
    for key in data["tier_lists"]:
        image_generator(f"{key['tier_list_name']}.png", key)
        print(f"\u2705 [b green]CRÉÉ[/b green] {key['tier_list_name']} liste hiérarchisée.")
        
    print("\u2705 [b green]TERMINÉ[/b green]. Vérifiez le répertoire pour les listes hiérarchisées.")    
    return
```

![Image](https://www.freecodecamp.org/news/content/images/2023/07/image-17.png align="left")

*Informer l'utilisateur que l'image est rendue dans le répertoire actuel.*

## Points clés à retenir

Ce tutoriel a démontré des moyens de transformer des données JSON en graphiques de listes hiérarchisées interactives en utilisant Python et la bibliothèque Pillow. En combinant la manipulation d'images et la récupération de données API, des représentations attrayantes des classements d'albums sont générées.

Pour résumer, vous avez appris :

* Comment récupérer les données des albums en utilisant l'API LastFM.

* Comment générer des listes hiérarchisées basées sur les entrées de l'utilisateur et les notes des albums.

* Comment utiliser la bibliothèque Pillow pour créer et manipuler des images.

* Comment redimensionner et coller les couvertures d'albums sur l'image de base.

* Comment ajouter du texte et des étiquettes de niveau à l'image.

* Comment écrire dynamiquement dans des fichiers JSON.

Vous voulez récupérer le code de ce tutoriel ? Obtenez-le depuis mon [Dépôt Github](https://github.com/HighnessAtharva/musicli). Il inclut d'autres fonctions CRUD comme la révision, la notation et la visualisation de tous vos albums et artistes directement dans le terminal.

Cela est également publié en tant que package Python pour faciliter l'utilisation. Référez-vous à cette [page de publication](https://pypi.org/project/musicli/) sur PyPi.

Ce projet utilise Python et des bibliothèques de manipulation d'images pour créer des listes hiérarchisées visuellement engageantes pour les communautés de jeux, les classements musicaux et les évaluations de contenu. Les utilisateurs peuvent noter les albums de manière interactive directement dans leur terminal et intégrer d'autres API ou sources de données pour améliorer le processus créatif. Cette application pratique explore de nouvelles possibilités en visualisation de données.