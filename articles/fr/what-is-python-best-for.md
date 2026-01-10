---
title: Cas d'utilisation de Python – Pour quoi Python est-il le meilleur ?
subtitle: ''
author: Juan Cruz Martinez
co_authors: []
series: null
date: '2023-12-05T21:22:56.000Z'
originalURL: https://freecodecamp.org/news/what-is-python-best-for
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/python-best-for.png
tags:
- name: Python
  slug: python
seo_title: Cas d'utilisation de Python – Pour quoi Python est-il le meilleur ?
seo_desc: "Developers are often very passionate about their tech stack, and they'll\
  \ likely recommend it for anything. \nIt is very common to see devs on social media\
  \ sharing how you can build anything with JavaScript or how Python is great for\
  \ data scientists.\nA..."
---

Les développeurs sont souvent très passionnés par leur stack technique et ils le recommanderont probablement pour tout.

Il est très courant de voir des devs sur les réseaux sociaux partager comment vous pouvez tout construire avec JavaScript ou comment Python est génial pour les data scientists.

En tant que fanatique de Python moi-même, je n'utilise pas toujours Python pour mes projets car Python ne se distingue pas dans tout. Alors aujourd'hui, je veux partager mes réflexions sur les principaux cas d'utilisation où Python excelle.

## Scripting et automatisation

Il n'a jamais été aussi facile de scripter et d'automatiser des tâches grâce à l'essor du no-code et à des outils comme l'application Shortcuts d'Apple. Mais même après avoir intégré ceux-ci dans ma routine quotidienne, il y a encore de nombreuses fois où je m'appuie sur Python pour accomplir des choses.

J'utilise Python en partie parce que je maîtrise déjà le langage. De plus, sa simplicité et son vaste écosystème de bibliothèques m'aident à obtenir des résultats plus rapidement qu'avec d'autres langages de programmation.

Voici quelques-unes des tâches que vous pouvez automatiser avec Python, ainsi que quelques exemples personnels :

### Gestion de fichiers

Vous pouvez automatiser des tâches comme l'organisation de fichiers, le renommage, la copie et la suppression en utilisant Python.

Personnellement, j'utilise Obsidian comme outil de prise de notes, où toutes mes notes atterrissent dans un dossier dédié "inbox" pour traitement. Un script Python lit ensuite les notes et déplace chacune d'elles vers le dossier approprié en fonction de leur contenu.

Le script semble sophistiqué, mais il est en réalité assez simple, car j'ai déjà un système en place.

Voici à quoi ressemble mon script pour organiser les notes :

```python
import shutil
import os
import frontmatter

# Liste des propriétés frontmatter avec les destinations de dossiers
frontmatter_to_dir = {
    'project': '1. Projects',
    'area': '2. Areas',
    'resource': '3. Resources',
}

def try_move_file(file, destination):
    print('- Déplacement du fichier', file, "vers", destination)
    try:
        shutil.move(file, destination)
    except Exception as err:
        print('-  - Projet non trouvé', err)


# Lire tous les fichiers à l'intérieur du répertoire "!inbox"
notes = os.listdir('!inbox')
for note in notes:
    note_path =  f"!inbox/{note}"
    # Lire le frontmatter du fichier
    note_metadata = frontmatter.load(note_path)
    
    # Vérifier si le fichier a une propriété pour catégoriser cette note,
    # par exemple : project, area, ou resource
    for group, group_destination in frontmatter_to_dir.items():
        if group in note_metadata:
            # Essayer de déplacer le fichier, il peut arriver que le projet soit
            # par exemple mal orthographié, dans ce cas, il ne fera rien avec la note
            try_move_file(note_path, f"{group_destination}/{note_metadata[group]}/{note}")
```

### Traitement de données

Python est dans une position unique lorsqu'il s'agit de traitement de données. Que vous essayiez de traiter du texte, des images, de grands ensembles de données ou d'effectuer des calculs complexes, il existe d'excellentes bibliothèques Python pour tous les cas d'utilisation.

Je crée généralement des scripts Python pour comprendre des informations. Par exemple, je dirige une entreprise avec plusieurs produits SaaS, et j'ai des scripts Python pour traiter les relevés et m'aider avec la comptabilité.

### Extraction de données à partir de fichiers texte ou de pages web

Vous pouvez utiliser Python pour extraire des données de sites web, analyser le contenu web et recueillir des informations pour envoyer des résumés ou autres. Je l'ai utilisé jusqu'à très récemment pour télécharger des flux RSS de mes blogs et sites web préférés et créer un résumé par e-mail que j'utilisais ensuite pour lire les articles les plus intéressants. J'utilise maintenant Readwise Reader à cette fin.

Pour montrer comment extraire des données de pages web en utilisant Python, j'ai créé un petit script qui visiterait un site, analyserait son HTML et retournerait des informations à partir d'éléments dans le DOM. En particulier, il visiterait un journal, trouverait des informations sur le taux de change pour la paire ARS/USD du jour et l'afficherait à l'écran. Un excellent script pour ceux qui vivent en Argentine.

```python
import requests
from bs4 import BeautifulSoup

# Charger le site web du journal pour extraire des informations sur le taux de change actuel pour USD/ARS
URL = 'https://www.lanacion.com.ar/'
page = requests.get(URL)

# Analyser les données HTML
soup = BeautifulSoup(page.content, "html.parser")
# Utiliser select pour trouver un élément dans le DOM
# Dans notre cas, nous avons besoin d'un span à l'intérieur d'un lien avec un titre spécifique
span = soup.select('a[title="Dólar blue"] span')[0]
price = span.get_text()
# Dans un scénario réel, au lieu de simplement imprimer le prix,
# je m'enverrais par exemple les résultats par e-mail ou je ferais un autre traitement
print(price) # par exemple $930,00
```

### Envoi d'e-mails

C'est ainsi que ma newsletter a commencé : envoyer des e-mails aux abonnés via un script Python. Maintenant, cela ne se met pas très bien à l'échelle car je voulais des fonctionnalités plus sophistiquées, et je suis passé à ConvertKit – mais le script Python était bien pour être une solution gratuite et à plus petite échelle.

L'envoi d'e-mails nécessite l'accès à un serveur SMTP ou à un service similaire, dans mon cas, j'utilisais une API propriétaire pour les envoyer, Amazon SES, car lorsqu'il s'agit d'envoyer des e-mails en masse, il y a certaines mesures que vous souhaitez prendre pour ne pas endommager le score de votre domaine, sinon vos e-mails finiront dans le dossier spam.

Voici comment je faisais cela :

```python
import boto3
import json

# Toutes les adresses e-mail étaient stockées dans s3
s3_bucket = ''
# Fournir le chemin vers votre fichier dans le bucket S3
s3_key = 'mail_list/addresses.txt'

s3_client = boto3.client('s3')
# Récupérer les identifiants e-mail à partir du fichier
s3_object = s3_client.get_object(Bucket=s3_bucket, Key=s3_key)
email_ids = s3_object['Body'].read().decode('utf-8').split('\n')

# Envoyer un e-mail pour chaque identifiant e-mail
ses_client = boto3.client('ses')
for email_id in email_ids:
	email_id = email_id.strip() # Supprimer les espaces de début/fin
	
	# Effectuer les opérations d'envoi d'e-mail en utilisant le client SES
	response = ses_client.send_email(
		Source='<FromAddress>',
		Destination={'ToAddresses': [email_id]},
		Message={
			'Subject': {'Data': 'Your Subject'},
			'Body': {'Text': {'Data': 'Your Email Body'}}
		}
	)

print(f"Email envoyé à {email_id}. ID du message : {response['MessageId']}")
```

## Applications Web et APIs

C'est vrai – vous ne pouvez pas faire de développement web uniquement avec Python. Vous aurez toujours besoin de HTML, CSS et JavaScript. Mais lorsqu'il s'agit de construire des backends pour des applications web, Python est une option fantastique.

Grâce à des frameworks Python populaires comme [Django](https://www.notion.so/Draft-Script-1d2f649493b04a0f84acc9dcc91f0c7a?pvs=21), [Flask](https://flask.palletsprojects.com/en/3.0.x/), et [FastAPI](https://fastapi.tiangolo.com/), il est très facile de commencer à construire vos applications web et APIs.

Dans la plupart des produits et applications que je construis, j'utilise une combinaison de [NextJS](https://nextjs.org/) pour le frontend, alimenté par un backend Python utilisant FastAPI, et c'est une combinaison redoutable.

Mais je ne suis pas le seul à choisir Python pour construire des backends web. Des entreprises comme Microsoft, Instagram, Pinterest et le Washington Post utilisent Python pour servir des millions d'utilisateurs.

## Analyse de données / Data Science / IA

Python est le leader incontesté en science des données, intelligence artificielle et apprentissage automatique. Cela est en partie grâce à son vaste écosystème de bibliothèques open-source, comme [Pandas](https://pandas.pydata.org/), [Numpy](https://numpy.org/), [Tensorflow](https://www.tensorflow.org/), et [Python in Excel](https://techcommunity.microsoft.com/t5/excel-blog/announcing-python-in-excel-combining-the-power-of-python-and-the/ba-p/3893439) parmi d'autres. Cet ensemble d'outils complet vous permet de relever pratiquement n'importe quel défi dans ces domaines.

Effectuez-vous des analyses statistiques complexes ? Pas de problème, il existe une bibliothèque pour cela. Êtes-vous impatient de commencer à utiliser des modèles d'apprentissage automatique de pointe ? Python vous couvre ! Avez-vous besoin d'un réseau de neurones complexe ? Bien sûr, vous pouvez le faire !

Le vaste écosystème de bibliothèques de Python vous permet de construire rapidement ce dont vous avez besoin, avec des bibliothèques qui sont prêtes pour la production, rapides, efficaces et qui ont des APIs de haute qualité.

Voici quelques exemples d'applications liées de Python pour la science des données et l'IA :

* Analyse de séries temporelles
* Visualisation de données
* Prédictions de ventes
* Traitement du langage
* Analyse de sentiment
* Systèmes de recommandation (comme la musique, les vidéos, etc.)
* Classification
* Vision par ordinateur
* Voitures autonomes
* et bien plus encore...

## Test d'applications

La syntaxe conviviale de Python et sa lisibilité en font un excellent choix pour les testeurs QA de tous niveaux de compétence. Sa structure simple et son organisation claire du code facilitent le prototypage rapide et la mise en œuvre de scripts de test.

Encore une fois, c'est grâce à l'écosystème riche de Python avec des bibliothèques comme Playwright et Selenium que Python est une excellente option pour cette catégorie.

Pour les applications web, les ingénieurs QA écrivent des scripts de test qui chargent l'application dans un navigateur sans tête, généralement un environnement QA ou de test, et effectuent une série de validations pour déterminer que l'application fonctionne correctement.

Par exemple, si vous souhaitez tester la page de liste d'un utilisateur, vous pouvez charger la page et, en interrogeant les éléments du DOM, vous pouvez valider que l'application rend effectivement les résultats. De plus, vous pouvez simuler des frappes de clavier, des clics, remplir des formulaires et bien plus encore avec ces outils.

Voici un script qui charge le site web [python.org](http://python.org/), effectue une recherche et valide le résultat en comparant la page résultante avec le message `No results found`.

```python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

# Définir le pilote pour utiliser Firefox, peut aussi être Chrome, IE, et Remote
driver = webdriver.Firefox()
# Charger le site web cible
driver.get("http://www.python.org")
# Valider que la page est chargée en comparant le titre de la page
assert "Python" in driver.title
# Trouver l'élément d'entrée de recherche par nom
elem = driver.find_element(By.NAME, "q")
# Le vider
elem.clear()
# Taper `pycon`
elem.send_keys("pycon")
# Appuyer sur entrée pour déclencher le formulaire de recherche
elem.send_keys(Keys.RETURN)
# Valider que le texte `No results found.` n'est pas présent dans la page
assert "No results found." not in driver.page_source
# Fermer le navigateur
driver.close()
```

## Conclusion

La polyvalence de Python et son vaste écosystème de bibliothèques en font un excellent choix pour divers projets. Que vous ayez besoin d'automatiser des tâches, de traiter des données, de construire des applications web et des APIs, de réaliser des analyses de données et de l'IA, ou de mener des tests d'applications, Python vous couvre.

Sa simplicité, sa lisibilité et ses bibliothèques puissantes vous permettent d'obtenir des résultats rapidement et efficacement. Alors, la prochaine fois que vous envisagez un langage de programmation pour votre projet, considérez les forces de Python dans ces domaines.

Merci d'avoir lu !

Vous pouvez me suivre ([@bajcmartinez](https://twitter.com/bajcmartinez)) ainsi que [@jesstemporal](https://twitter.com/jesstemporal) sur Twitter/X pour en apprendre davantage sur Python et comment construire des applications Python sécurisées. Nous sommes des développeurs advocates chez [Auth0 by Okta](https://auth0.com/) et publions régulièrement du contenu et des lives streams sur Python.