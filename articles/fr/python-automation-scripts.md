---
title: Scripts d'automatisation Python que vous devriez connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-02-03T18:36:39.000Z'
originalURL: https://freecodecamp.org/news/python-automation-scripts
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/Python-Automation-Scripts-You-Should-Know.png
tags:
- name: automation
  slug: automation
- name: Python
  slug: python
seo_title: Scripts d'automatisation Python que vous devriez connaître
seo_desc: 'By Shittu Olumide

  We all have those same old boring tasks that we do over and over again. Fortunately,
  we can automate some of these processes so that we can focus on doing other things
  that really need our energy and attention.

  In this article, we w...'
---

Par Shittu Olumide

Nous avons tous ces mêmes vieilles tâches ennuyeuses que nous faisons encore et encore. Heureusement, nous pouvons automatiser certains de ces processus afin de pouvoir nous concentrer sur d'autres choses qui nécessitent vraiment notre énergie et notre attention.

Dans cet article, nous allons parler de quelques scripts d'automatisation Python que vous pouvez facilement utiliser pour effectuer des tâches d'automatisation. Il est important de comprendre qu'ils sont tous des codes prêts à l'emploi qui peuvent nous aider à prendre en charge de nombreuses tâches répétitives quotidiennes.

Je vous recommande fortement d'avoir une certaine expérience préalable avec le langage de programmation Python avant de continuer avec cet article. 

Commençons-nous ?

%[https://tenor.com/bTCas.gif]

## Comment automatiser la relecture Python

Le premier de la liste est la relecture. Chaque fois que vous souhaitez éliminer les erreurs de grammaire et d'orthographe de votre écriture, vous pouvez essayer ce projet qui utilise le module `Lmproof`.

```python
# Relecture Python
# pip install lmproof
import lmproof
def proofread(text):
    proofread = lmproof.load("en")
    correction = proofread.proofread(text)
    print("Original: {}".format(text))
    print("Correction: {}".format(correction))
    
proofread("Votre texte")
```

Tout d'abord, vous devrez installer la bibliothèque `lmproof` pour cette automatisation. Ensuite, vous pouvez utiliser la fonction `proofread()` qui prend `text` comme paramètre. La fonction s'exécute et imprime le texte original qui a été passé dans la fonction ainsi que le texte corrigé. Vous pouvez l'utiliser pour relire rapidement un essai ou un court article.

## Comment automatiser la lecture de musique aléatoire

Pendant le travail, de nombreux développeurs aiment écouter de la musique. Donc pour les amateurs de musique (comme moi), ce script choisit aléatoirement une chanson dans un dossier contenant des chansons et la joue avec l'aide des modules `OS` et `random` en Python.

```python
import random, os
music_dir = 'E:\\music diretory'
songs = os.listdir(music_dir)

song = random.randint(0,len(songs))

# Imprime le nom de la chanson
print(songs[song])  

os.startfile(os.path.join(music_dir, songs[0])) 
```

Le code va dans le répertoire de musique contenant toutes les chansons que vous voulez jouer, et les met toutes dans une liste. Ensuite, il joue aléatoirement chaque chanson l'une après l'autre. La fonction `os.startfile` joue la chanson. 

## Convertisseur automatique de PDF en CSV

Parfois, vous devrez convertir des données `pdf` en données `CSV` (valeurs séparées par des virgules) afin de pouvoir les utiliser pour une analyse plus approfondie. Dans ces cas, ce script peut être utile.

```python
import tabula

filename = input("Entrez le chemin du fichier: ")
df = tabula.read_pdf(filename, encoding='utf-8', spreadsheet=True, pages='1')

df.to_csv('output.csv')
```

Vous devrez installer la bibliothèque `tabula` en utilisant `pip` afin d'exécuter ce code. Après l'installation, vous pouvez passer le fichier dans votre projet. 

La bibliothèque vient avec une fonction `read_pdf()` qui prend le fichier et le lit. Vous terminez l'automatisation en utilisant la fonction `to_csv()` pour convertir la sortie en CSV.

## Compresseur de photos automatique

Vous pouvez également réduire la taille d'une image en la compressant tout en conservant sa qualité. 

```python
import PIL
from PIL import Image
from tkinter.filedialog import *

fl=askopenfilenames()
img = Image.open(fl[0])
img.save("output.jpg", "JPEG", optimize = True, quality = 10)
```

Vous pouvez utiliser la bibliothèque PIL (Python Imaging Library) pour manipuler des images, ajouter des filtres, flouter, accentuer, lisser, détecter les bords, compresser des images et faire beaucoup de choses aux images.

## Téléchargeur automatique de vidéos YouTube

Voici un script automatisé facile pour télécharger des vidéos YouTube. Il suffit d'utiliser le code ci-dessous pour télécharger n'importe quelle vidéo sans avoir besoin de sites web ou d'applications.

```python
import pytube

link = input('URL de la vidéo YouTube')
video_download = pytube.Youtube(link)
video_download.streams.first().download()
print('Vidéo téléchargée', link)
```

La bibliothèque pytube est une bibliothèque très facile et simple que vous pouvez utiliser pour télécharger des vidéos YouTube sur votre ordinateur local. Tout ce que vous avez à faire est de saisir le lien vers la vidéo, puis la méthode `download()` la télécharge sur votre ordinateur.

## Conversion automatique de texte en parole

Nous allons utiliser l'API Google Text to Speech pour ce script. L'API est à jour et fonctionne avec de nombreuses langues, tons et voix, que vous pouvez sélectionner.

```python
from pygame import mixer
from gtts import gTTS

def main():
   tts = gTTS('Like This Article')
   tts.save('output.mp3')
   mixer.init()
   mixer.music.load('output.mp3')
   mixer.music.play()
   
if __name__ == "__main__":
   main()
```

## Comment convertir automatiquement des images en PDF

Il s'agit d'une tâche très courante que vous pouvez effectuer souvent. Vous pouvez vouloir convertir une seule image ou plusieurs images en un PDF. 

Comment convertir une seule image en PDF :

```python
import os
import img2pdf
with open("output.pdf", "wb") as file:
   file.write(img2pdf.convert([i for i in os.listdir('path to image') if i.endswith(".jpg")]))
```

Comment convertir plusieurs images en PDF :

```python
from fpdf import FPDF
Pdf = FPDF()

list_of_images = ["wall.jpg", "nature.jpg","cat.jpg"]
for i in list_of_images:
   Pdf.add_page()
   Pdf.image(i,x,y,w,h)
   Pdf.output("result.pdf", "F")
```

Ici, nous utilisons la bibliothèque `image2pdf` en Python pour convertir notre image en PDF. Nous pouvons également convertir plusieurs images en PDF avec seulement quelques lignes de code.

## Vérificateur automatique de plagiat

Le plagiat est l'acte de présenter les mots ou les idées d'une autre personne comme les vôtres, avec ou sans la permission de cette personne, en les intégrant dans votre travail sans donner à l'auteur original le crédit qui lui est dû. 

Ce script peut être assez utile lorsque vous souhaitez vérifier le plagiat entre deux fichiers.

```python
from difflib import SequenceMatcher
def plagiarism_checker(f1,f2):
    with open(f1,errors="ignore") as file1,open(f2,errors="ignore") as file2:
        f1_data=file1.read()
        f2_data=file2.read()
        res=SequenceMatcher(None, f1_data, f2_data).ratio()
        
print(f"Ces fichiers sont {res*100} % similaires")
f1=input("Entrez le chemin du fichier_1: ")
f2=input("Entrez le chemin du fichier_2: ")
plagiarism_checker(f1, f2)
```

## Comment raccourcir les URL

Les grandes URL peuvent être assez ennuyeuses à lire et à partager. Pour raccourcir les URL, ce script utilise une API tierce.

```python
from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	from urllib2 import urlopen
import sys

def make_tiny(url):
	request_url = ('http://tinyurl.com/app-index.php?' + 
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def main():
	for tinyurl in map(make_tiny, sys.argv[1:]):
		print(tinyurl)

if __name__ == '__main__':
	main()
    

'''

-----------------------------SORTIE------------------------
python url_shortener.py https://www.wikipedia.org/
https://tinyurl.com/bif4t9

'''
    
```

## Testeur de vitesse Internet

L'API de test de vitesse OOKLA vous permet de vérifier le ping et la vitesse Internet. En plus de mesurer le ping, ce petit projet automatisé mesurera les vitesses de téléchargement et de téléversement.

```python
# Testeur de vitesse Internet
# pip install speedtest-cli
import speedtest as st

# Définir le meilleur serveur
server = st.Speedtest()
server.get_best_server()

# Tester la vitesse de téléchargement
down = server.download()
down = down / 1000000
print(f"Vitesse de téléchargement: {down} Mb/s")

# Tester la vitesse de téléversement
up = server.upload()
up = up / 1000000
print(f"Vitesse de téléversement: {up} Mb/s")

# Tester le ping
ping = server.results.ping
print(f"Vitesse de ping: {ping}")

```

Bien qu'il existe des alternatives comme [fast.com](https://www.freecodecamp.org/news/p/596c046e-0ba5-4a99-bf4d-eb3e0bebe75c/www.fast.com), avec ce script, vous pouvez rapidement vérifier la vitesse Internet en utilisant un script Python.

## Conclusion

Nous avons parlé de dix scripts d'automatisation Python dans cet article, et j'espère que vous l'avez trouvé utile. Vous pouvez également aller plus loin pour vérifier les bibliothèques utilisées et élargir vos connaissances.

Connectons-nous sur [Twitter](https://www.twitter.com/Shittu_Olumide_) et sur [LinkedIn](https://www.freecodecamp.org/news/p/596c046e-0ba5-4a99-bf4d-eb3e0bebe75c/linkedin.com/in/olumide-shittu).

Bon codage !