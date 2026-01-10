---
title: Comment booster vos études avec Python, Anki et ChatGPT
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-25T20:35:46.000Z'
originalURL: https://freecodecamp.org/news/supercharged-studying-with-python-anki-chatgpt
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/pexels-pixabay-256302.jpg
tags:
- name: chatgpt
  slug: chatgpt
- name: learning to code
  slug: learning-to-code
- name: Python
  slug: python
seo_title: Comment booster vos études avec Python, Anki et ChatGPT
seo_desc: "By Otavio Ehrenberger\nYou may have heard how students can use ChatGPT\
  \ to cheat on assignments. But we should also talk about what a fantastic study\
  \ tool it can be. \nIn this article we'll discuss how you can use ChatGPT to help\
  \ you study and learn new..."
---

Par Otavio Ehrenberger

Vous avez peut-être entendu parler de la manière dont les étudiants peuvent utiliser [ChatGPT](https://chat.openai.com) pour tricherdans les devoirs. Mais nous devrions également parler de l'excellent outil d'étude qu'il peut être.

Dans cet article, nous discuterons de la manière dont vous pouvez utiliser ChatGPT pour vous aider à étudier et à apprendre de nouvelles compétences.

Vous verrez comment instruire ChatGPT pour qu'il vous donne une liste bien formatée d'informations que vous devez mémoriser. Vous verrez ensuite comment l'entrer dans un programme Python qui générera un package Anki. Enfin, vous chargerez le package dans Anki pour vous aider à retenir les concepts grâce à des déclencheurs de mémoire.

Je vais vous montrer comment créer des cartes Anki de manière programmatique en utilisant Python et la bibliothèque [Genanki](https://github.com/kerrickstaley/genanki). Nous allons créer un deck Anki pour apprendre les répertoires du système de fichiers Linux et leurs descriptions. Le deck contiendra des cartes de type basique et inversé pour chaque répertoire.

# Qu'est-ce qu'Anki ?

[Anki](https://apps.ankiweb.net/) est une puissante application open-source de cartes mémoire qui aide les utilisateurs à mémoriser des informations plus efficacement en utilisant la répétition espacée. Il est disponible sur plusieurs plateformes, y compris Windows, macOS, Linux, iOS et Android.

Anki permet aux utilisateurs de créer leurs propres decks de cartes mémoire contenant du texte, des images, de l'audio et même des équations LaTeX.

Apprendre à utiliser correctement Anki est une compétence en soi. [Voici une bonne vidéo pour commencer](https://www.youtube.com/watch?v=7K2StK7e3ww&t=6s). Dans ce programme, nous utiliserons les concepts de modèles Anki, de cartes, de notes, de decks et de packages pour créer notre ensemble de cartes. Mais d'abord, apprenons un peu plus sur le fonctionnement d'Anki.

### Modèles Anki

Un modèle Anki, également connu sous le nom de type de note, définit la structure et la mise en page d'un ensemble de cartes. Chaque modèle se compose d'un ensemble de champs, qui stockent les informations à apprendre, et d'un ensemble de templates de cartes, qui déterminent comment ces informations sont affichées sur les cartes.

Les modèles permettent aux utilisateurs de créer différents types de cartes et de mises en page pour divers besoins d'apprentissage, tels que les cartes de base, les cartes inversées et les cartes de suppression cloze.

### Cartes Anki

Une carte Anki est une carte mémoire numérique contenant des informations à apprendre. Chaque carte a un côté recto, qui contient généralement une question ou une invite, et un côté verso, qui contient la réponse ou des informations supplémentaires liées au côté recto.

Les cartes Anki peuvent contenir du texte, des images, de l'audio et même des équations LaTeX. Les cartes sont générées à partir de modèles et de leurs champs associés, qui déterminent le contenu et la mise en page des cartes.

### Notes Anki

Une note Anki est une seule pièce d'information qui est utilisée pour générer une ou plusieurs cartes mémoire ou cartes Anki.

Chaque note est basée sur un modèle spécifique (également connu sous le nom de type de note), qui définit la structure, la mise en page et les champs pour cette note. Les champs stockent le contenu réel de la note, tel que des questions, des réponses ou des invites, tandis que le modèle détermine comment ce contenu est affiché sur les cartes générées.

### Decks Anki

Un deck Anki est une collection de cartes sur un sujet ou un thème spécifique. Les decks sont utilisés pour organiser les cartes en groupes significatifs, ce qui facilite la concentration des utilisateurs sur un domaine d'étude particulier.

Anki permet aux utilisateurs de créer et de personnaliser leurs propres decks, qui peuvent être partagés avec d'autres, importés ou exportés. Les utilisateurs peuvent étudier un deck à la fois ou plusieurs decks simultanément, selon leurs objectifs et préférences d'apprentissage.

### Packages Anki

Un package Anki est un seul fichier contenant un ou plusieurs decks, ainsi que leurs cartes associées, modèles, fichiers multimédias et autres données connexes. Les packages Anki ont l'extension de fichier ".apkg" et peuvent être facilement partagés, importés ou exportés entre utilisateurs et appareils.

Les packages Anki sont un moyen pratique de distribuer des decks et du contenu associé, car ils regroupent toutes les informations nécessaires dans un seul fichier. Lors de l'importation d'un package Anki, les decks, cartes et modèles qu'il contient sont ajoutés à la collection existante de l'utilisateur.

# Comment utiliser ChatGPT comme aide à l'étude

Vous pouvez penser à ChatGPT comme un Google humanoïde. Il ne fera pas le travail à votre place et il ne pensera certainement pas à votre place. Mais si vous savez comment formuler vos questions, il peut vous donner des réponses assez bonnes, et dans le format que vous souhaitez. Cela facilite l'insertion de ces réponses dans un programme.

Dans cet exemple, je vais poser une question concernant le système de fichiers Linux. Je m'attends à ce que la réponse soit une liste des répertoires accessibles depuis le dossier racine, avec une explication de leur présence. Si vous n'obtenez pas la réponse souhaitée, n'oubliez pas d'être plus spécifique.

![Réponse de Chat GPT sur le système de fichiers Linux](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/rufulo3vzyby3ueost53.png)

Il s'agit d'une capture d'écran partielle – la réponse va jusqu'à 14, le répertoire `/var` utilisé pour stocker des fichiers de données fluides qui sont censés changer pendant une session d'utilisation du système, et le dernier dans l'ordre alphabétique.

Jusqu'à présent, tout va bien. Mais si nous voulons insérer ces informations dans un programme, nous devons les formater. C'est un domaine où Chat GPT excelle.

Si vous recevez, par exemple, un paragraphe comme réponse, vous pouvez simplement demander au robot de le reformuler sous forme de liste ordonnée. Ensuite, vous pouvez lui demander de renvoyer chaque élément sous forme de tableau de tuples, par exemple. Voici un exemple basé sur la dernière réponse :

![Description de l'image](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/5tosze6su9fq8ieswu56.png)

N'oubliez pas de toujours vérifier les réponses avant de les télécharger dans Anki, car vous allez marteler les informations retournées dans votre cerveau. Vous ne voulez pas saboter votre apprentissage pendant vos études.

Cela suffit pour l'instant, passons au codage.

# Comment installer Genanki

Pour commencer, vous devrez installer la bibliothèque `genanki`, qui est une bibliothèque Python pour créer des decks et des cartes Anki de manière programmatique. Vous pouvez l'installer en utilisant `pip` :

```bash
pip install genanki
```

# Comment créer des cartes et des decks Anki

Maintenant que nous avons installé la bibliothèque `genanki`, créons un script Python qui génère les cartes et le deck Anki pour les répertoires du système de fichiers Linux.

## Préparations

Ici, nous allons importer la bibliothèque et coller la réponse de ChatGPT. Elle sera utilisée comme paramètre pour les fonctions fournies par `genanki`.

```python
import genanki

# Liste des répertoires Linux et de leurs descriptions
linux_dirs = [
    ('/', 'Répertoire racine, point de départ de la hiérarchie du système de fichiers.'),
    ('/bin', 'Contient les exécutables des commandes système essentielles.'),
    ('/sbin', 'Contient les exécutables des commandes d\'administration système essentielles.'),
    ('/boot', 'Contient les fichiers nécessaires pour démarrer le processus de boot.'),
    ('/etc', "Contient les fichiers de configuration système et les scripts."),
    ('/dev', 'Contient les fichiers de périphériques représentant les dispositifs matériels.'),
    ('/home', 'Contient les répertoires personnels de chaque utilisateur.'),
    ('/lib', 'Contient les bibliothèques partagées et les modules du noyau.'),
    ('/opt', 'Répertoire optionnel pour stocker les logiciels tiers.'),
    ('/proc', 'Système de fichiers virtuel fournissant une interface aux structures de données internes du noyau.'),
    ('/sys', 'Système de fichiers virtuel fournissant une interface aux structures de données internes du noyau pour les dispositifs, les pilotes et autres composants.'),
    ('/tmp', 'Répertoire temporaire pour stocker les fichiers supprimés après un redémarrage du système.'),
    ('/usr', 'Contient les fichiers liés à l\'utilisateur, les bibliothèques partagées, les fichiers d\'en-tête, la documentation et les binaires de logiciels non essentiels.'),
    ('/var', 'Contient les fichiers de données variables, tels que les logs, les bases de données et les files d\'attente de courrier.'),
]
```

Ici, nous devons générer un identifiant de modèle pour les cartes que nous créons, qui doit être unique. Vous devrez également donner un nom à votre modèle, créer des champs à remplir avec du contenu, puis déclarer un template pour votre note en utilisant ces champs.

Rappelez-vous qu'une note est essentiellement un formulaire pour les cartes associées à cette note. Nous aurons deux cartes pour chaque note, puisque le nom du répertoire est un déclencheur de mémoire pour la description du répertoire et vice-versa.

```python
# Définir le modèle de note Anki
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Dossiers du système de fichiers Linux',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Carte 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Carte 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])
```

Nous allons enfin créer le deck et lui donner un identifiant (qui, vous l'aurez deviné, doit être unique) et également lui donner un nom. Nous allons ensuite parcourir notre liste de tuples et créer une note pour chaque tuple, en déclarant le modèle de la note et en entrant notre contenu en tant que champs ('Directory' et 'Description' respectivement).

Nous allons enfin écrire un package contenant notre deck unique. Si vous avez une installation d'Anki, il vous suffit de double-cliquer sur le fichier généré et il devrait s'ouvrir dans le programme, prêt pour l'étude.

```python
# Générer les cartes Anki et les ajouter à un deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Système de fichiers Linux')

for dir_name, description in linux_dirs:
    note = genanki.Note(model=model, fields=[dir_name, description])
    deck.add_note(note)

# Sauvegarder le deck dans un fichier de package Anki (*.apkg)
genanki.Package(deck).write_to_file('linux_filesystem.apkg')
```

# Script complet

```python
import genanki

# Liste des répertoires Linux et de leurs descriptions
linux_dirs = [
    ('/', 'Répertoire racine, point de départ de la hiérarchie du système de fichiers.'),
    ('/bin', 'Contient les exécutables des commandes système essentielles.'),
    ('/sbin', 'Contient les exécutables des commandes d\'administration système essentielles.'),
    ('/boot', 'Contient les fichiers nécessaires pour démarrer le processus de boot.'),
    ('/etc', "Contient les fichiers de configuration système et les scripts."),
    ('/dev', 'Contient les fichiers de périphériques représentant les dispositifs matériels.'),
    ('/home', 'Contient les répertoires personnels de chaque utilisateur.'),
    ('/lib', 'Contient les bibliothèques partagées et les modules du noyau.'),
    ('/opt', 'Répertoire optionnel pour stocker les logiciels tiers.'),
    ('/proc', 'Système de fichiers virtuel fournissant une interface aux structures de données internes du noyau.'),
    ('/sys', 'Système de fichiers virtuel fournissant une interface aux structures de données internes du noyau pour les dispositifs, les pilotes et autres composants.'),
    ('/tmp', 'Répertoire temporaire pour stocker les fichiers supprimés après un redémarrage du système.'),
    ('/usr', 'Contient les fichiers liés à l\'utilisateur, les bibliothèques partagées, les fichiers d\'en-tête, la documentation et les binaires de logiciels non essentiels.'),
    ('/var', 'Contient les fichiers de données variables, tels que les logs, les bases de données et les files d\'attente de courrier.'),
]

# Définir le modèle de note Anki
model_id = 1607392319
model = genanki.Model(
    model_id,
    'Modèle Simple',
    fields=[
        {'name': 'Directory'},
        {'name': 'Description'},
    ],
    templates=[
        {
            'name': 'Carte 1',
            'qfmt': '{{Directory}}',
            'afmt': '{{Description}}',
        },
        {
            'name': 'Carte 2',
            'qfmt': '{{Description}}',
            'afmt': '{{Directory}}',
        },
    ])

# Générer les cartes Anki et les ajouter à un deck
deck_id = 2059400110
deck = genanki.Deck(deck_id, 'Système de fichiers Linux')

for dir_name, description in linux_dirs:
    note = genanki.Note(model=model, fields=[dir_name, description])
    deck.add_note(note)

# Sauvegarder le deck dans un fichier de package Anki (*.apkg)
genanki.Package(deck).write_to_file('linux_filesystem.apkg')
```

# Limites de cette méthode

Ce script est assez bon, et je l'utilise très souvent – mais ne prétendez pas qu'il est parfait. Vous devrez générer le deck chaque fois que vous voudrez ajouter des éléments de manière programmatique.

Vous pouvez également obtenir l'identifiant du deck et générer plus de cartes pour un nouveau package avec le même identifiant et les ajouter, mais cela peut entraîner des erreurs si vous n'êtes pas prudent.

De plus, la méthode d'entrée est actuellement un tableau de tuples. Vous devrez modifier le script chaque fois pour mettre à jour le tableau avec un nouveau deck.

Vous pourriez également copier et coller le contenu dans un fichier texte et lire l'entrée à partir de là. Et vous pourriez également générer aléatoirement un identifiant de modèle afin de pouvoir simplement coller le contenu des cartes dans votre fichier texte et générer le package à partir d'une seule exécution de script. Cela est quelque peu subjectif, donc je l'ai laissé de côté intentionnellement.

# Conclusion

Anki propose plusieurs types de cartes, les principaux étant les cartes de base (déclencheur de mémoire + réponse) et les cartes cloze (un ou plusieurs déclencheurs de mémoire intégrés dans un plan). Cet exemple utilise les cartes de base et inversées, car à la fois la 'question' et la 'réponse' peuvent être un déclencheur de mémoire l'une pour l'autre. Si vous voulez une carte simple et basique, vous devriez consulter l'exemple dans le README de [Genanki](https://github.com/kerrickstaley/genanki).

J'espère que ce script sert au moins de point de départ pour vos propres applications d'Anki programmable. C'est probablement ma principale méthode d'étude de nos jours, et elle est devenue beaucoup plus puissante après ChatGPT. Amusez-vous bien avec votre codage.