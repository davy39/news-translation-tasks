---
title: Comment télécharger et rogner des MP3 depuis YouTube avec Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-21T18:57:27.000Z'
originalURL: https://freecodecamp.org/news/download-trim-mp3-from-youtube-with-python
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-pixabay-164821.jpg
tags:
- name: music
  slug: music
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: Comment télécharger et rogner des MP3 depuis YouTube avec Python
seo_desc: 'By Otavio Ehrenberger

  Everybody''s different, but I believe that nearly all of us enjoy listening to music.

  If you want to keep a local version of audio streams you often listen to, you''ll
  need to download these files. Sometimes you''ll also want to cl...'
---

Par Otavio Ehrenberger

Chacun est différent, mais je crois que presque tous nous aimons écouter de la musique.

Si vous souhaitez conserver une version locale des flux audio que vous écoutez souvent, vous devrez télécharger ces fichiers. Parfois, vous voudrez également extraire une portion de ce fichier audio au lieu d'avoir uniquement le fichier complet disponible.

Vous pouvez développer un script Python pour faire exactement ces choses. Vous pouvez également l'étendre avec des fonctionnalités supplémentaires si vous le souhaitez. Et je vais vous montrer comment faire dans ce tutoriel.

## Une note sur les droits d'auteur

Si vous avez déjà utilisé Internet, vous êtes probablement conscient que les problèmes de droits d'auteur peuvent rendre beaucoup de gens mécontents des deux côtés d'un débat sur la gratuité du contenu.

[La bibliothèque même que nous allons utiliser a eu sa part de problèmes de droits d'auteur](https://github.blog/2020-11-16-standing-up-for-developers-youtube-dl-is-back/).

Heureusement, il existe du matériel libre de droits disponible pour que nous puissions en profiter et l'utiliser dans nos programmes. Nous utiliserons donc l'audio libre de droits [4ème mouvement de la 9ème symphonie de Beethoven](https://www.youtube.com/watch?v=8OAPLk20epo) dans ce tutoriel.

Ce guide suppose que vous utiliserez les méthodes suivantes pour télécharger du matériel libre de droits également. N'utilisez pas ces informations pour enfreindre des droits d'auteur !

## Ce que nous allons faire dans ce tutoriel

Tout d'abord, nous allons installer la dépendance de base, FFMPEG. Ensuite, nous installerons la bibliothèque `youtube-dl` (qui fonctionne également avec Vimeo et de nombreuses autres plateformes) pour télécharger l'audio depuis une URL YouTube et l'utiliser dans du code Python.

Ensuite, nous téléchargerons la bibliothèque `pydub` pour rogner les fichiers audio et implémenter cette fonctionnalité dans notre code.

Enfin, nous créerons une interface utilisateur conviviale afin de pouvoir réutiliser ce script plus tard sans avoir à modifier le code.

Tout cela sera exécuté à l'intérieur d'une fonction `main()` afin de séparer la fonctionnalité, l'implémentation et l'utilisation.

## Comment installer le paquet FFMPEG

Ce paquet est au cœur de nombreux programmes multimédias (et de tous les logiciels open-source que j'ai utilisés jusqu'à présent). Nous en aurons besoin pour les deux bibliothèques Python que nous installerons très bientôt.

### Comment installer sur Linux

Si vous êtes sur une machine basée sur Debian (comme Ubuntu ou Kali), voici la commande pour installer FFMPEG :

```
sudo apt-get install ffmpeg
```

Si vous utilisez d'autres types de distributions, les instructions d'installation sont [ici](https://ffmpeg.org/download.html).

### Comment installer sur Windows

Tout d'abord, installez le [Chocolatey Package Manager](https://chocolatey.org/how-chocolatey-works). Les instructions d'installation sont [ici](https://chocolatey.org/install), je vous attends.

Une fois que vous avez correctement installé Chocolatey (si vous ne l'aviez pas déjà), téléchargez le paquet depuis une **instance administrative de Powershell** :

```powershell
choco install ffmpeg

```

### Comment installer sur Mac

Si vous ne l'avez pas déjà, [installez Homebrew](https://brew.sh/). Ensuite, dans un terminal :

```
brew install ffmpeg
```

## Comment télécharger programmatiquement de l'audio depuis des URL YouTube

Tout d'abord, téléchargez le paquet youtube-dl depuis pip. C'est [l'un des plus étoilés sur GitHub](https://github.com/ytdl-org/youtube-dl).

`pip install youtube-dl`

Nous allons importer ce module et ensuite déclarer une fonction qui télécharge l'audio au format mp3 avec une qualité raisonnable depuis une URL YouTube.

```python
import youtube_dl # client pour de nombreux portails multimédias

# télécharge yt_url dans le même répertoire à partir duquel le script s'exécute
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def main():
    yt_url = "https://www.youtube.com/watch?v=8OAPLk20epo"
    download_audio(yt_url)

main()

```

La méthode `.download()` va télécharger progressivement le flux audio sous forme de fichier `.webm`. Une fois qu'il détecte que le fichier complet est disponible, il utilisera `ffmpeg` pour le convertir en fichier audio MP3. Cela signifie que si quelque chose se produit, par exemple si la connexion Internet est coupée lorsque le fichier est téléchargé à 90 %, il reprendra le téléchargement à 90 % au lieu de recommencer depuis le début, ce qui est plutôt pratique.

Notez que si vous avez déjà le fichier mp3 téléchargé, le téléchargement redémarrera et écrasera le fichier.

Exécutez votre script Python. Le téléchargement audio de cette interprétation du 4ème mouvement de la 9ème symphonie de Beethoven devrait donner un fichier MP3 d'environ 33 Mo avec le titre de la vidéo disponible localement. Cela sera probablement un peu lent, alors allez vous préparer une tasse de thé.

Comme vous pouvez le voir, il est possible de passer des paramètres optionnels à youtube-dl (qui sera également disponible en tant que programme CLI autonome en dehors du script). L'une de ses capacités est de [télécharger une série de vidéos à partir d'une URL de playlist](https://github.com/ytdl-org/youtube-dl#video-selection). Si vous êtes plus intéressé, vous pouvez lire leur documentation. Je garderai l'utilisation plus triviale tout au long de ce tutoriel.

## Comment rogner le fichier téléchargé

Avec le fichier téléchargé, nous allons maintenant le découper arbitrairement localement (vous avez peut-être envisagé s'il est possible de simplement télécharger un clip depuis YouTube. Toutes les méthodes fiables que j'ai trouvées se résumeront essentiellement à télécharger le fichier complet puis à l'éditer localement). Pour cela, nous utiliserons la [bibliothèque pydub](https://github.com/jiaaro/pydub). Vous pouvez l'installer comme ceci :

```python
pip install pydub
```

C'est une bibliothèque assez agréable qui vous permet de manipuler complètement l'audio, en réduisant ou en augmentant le volume à certains intervalles, en répétant des clips, et ainsi de suite. Pour l'instant, nous nous intéressons uniquement au rognage.

Pour rogner notre fichier téléchargé, nous devrons obtenir le nom de fichier de notre MP3 nouvellement téléchargé, convertir les points de début et de fin de notre intervalle audio souhaité de 'heures:minutes:secondes' en millisecondes, et enfin utiliser `pydub` pour découper notre fichier audio.

### Comment obtenir le nom du fichier

Malheureusement, la méthode `.download()` ne retournera pas notre nom de fichier généré, auquel nous n'aurons pas non plus accès puisque nous passons simplement l'URL en tant que paramètre. Mais nous avons Python et c'est un outil fantastique.

Nous savons que nous cherchons un fichier `.mp3` qui a été généré juste avant notre opération de recherche de nom de fichier (Python est mono-thread et exécutera le code de manière synchrone par défaut). Nous obtiendrons le nom de notre MP3 le plus récent dans le répertoire du script, et ce sera notre fichier.

Nous pouvons effectuer cette opération en listant tous les fichiers `.mp3` dans le répertoire local, en collectant leurs timestamps sous forme d'entiers (ce qui signifie le temps en millisecondes compté à partir d'une date donnée dans le passé. Cela signifie que plus la valeur est élevée, plus le fichier a été créé récemment.), et en obtenant le fichier avec la valeur la plus élevée.

Pour cela, nous aurons besoin des modules `glob` pour naviguer dans le répertoire et `os` pour obtenir les informations de timestamp, tous deux disponibles nativement.

```python
import glob
import os

def newest_mp3_filename():
    # liste tous les mp3 dans le répertoire local
    list_of_mp3s = glob.glob('./*.mp3')
    # retourne le mp3 avec la valeur de timestamp la plus élevée
    return max(list_of_mp3s, key = os.path.getctime)

```

### Comment obtenir HH:MM:SS en millisecondes

Une fois que nous avons découpé notre fichier, `pydub` s'attendra à ce que les intervalles de temps soient exprimés en millisecondes. Mais pour nous, humains, calculer le moment exact en millisecondes chaque fois que nous voulons rogner une vidéo serait assez ennuyeux, alors nous demanderons respectueusement à l'ordinateur de le faire pour nous.

Notre entrée sera une chaîne de caractères au format **HH:MM:SS**. Cela fonctionne bien si nous voulons rogner une vidéo de plus d'une heure, mais la plupart du temps, nous voudrons simplement obtenir l'intervalle de temps d'un intervalle minute:seconde à un autre. Nous devons donc en tenir compte également.

Une milliseconde est 1/1000 de seconde, une minute est 60 secondes, et une heure est 60 minutes. Nous devons donc obtenir la valeur pour les heures, puis pour les minutes, puis pour les secondes, effectuer la conversion en millisecondes sur chacune, puis additionner les parties pour obtenir le résultat.

```python
def get_video_time_in_ms(video_timestamp):
    vt_split = video_timestamp.split(":")
    if (len(vt_split) == 3): # si au format HH:MM:SS
        hours = int(vt_split[0]) * 60 * 60 * 1000
        minutes = int(vt_split[1]) * 60 * 1000
        seconds = int(vt_split[2]) * 1000
    else: # format MM:SS
        hours = 0
        minutes = int(vt_split[0]) * 60 * 1000
        seconds = int(vt_split[1]) * 1000
    # point dans le temps en millisecondes
    return hours + minutes + seconds

```

### Comment obtenir l'audio rogné

Nous allons maintenant lire notre MP3 en tant qu'objet `pydub` et découper notre intervalle souhaité. La syntaxe est exactement la même que les opérations de découpage sur les chaînes de caractères et les tableaux, mais au lieu d'un index pour un élément, nous utiliserons des millisecondes pour des instants spécifiques dans l'audio.

```python
def get_trimmed(mp3_filename, initial, final = ""):
    if (not mp3_filename):
        # lever une erreur pour arrêter immédiatement l'exécution du programme
        raise Exception("Aucun MP3 trouvé dans le répertoire local.")
    # lit le mp3 en tant qu'objet PyDub
    sound = AudioSegment.from_mp3(mp3_filename)
    t0 = get_video_time_in_ms(initial)
    print("Début du processus de rognage pour le fichier ", mp3_filename, ".\n")
    print("Début à ", initial, "...")
    if (len(final) > 0):
        print("...jusqu'à ", final, ".\n")
        t1 = get_video_time_in_ms(final)
        return sound[t0:t1] # t0 jusqu'à t1
    return sound[t0:] # t0 jusqu'à la fin

```

## Comment tout mettre ensemble

> Alle Menschen werden Brüder,  
> Wo dein sanfter Flügel weilt.  
> -- Friedrich Schiller

Au cas où vous vous poseriez la question, le fragment précédent se traduit par "Tous les hommes deviendront frères, partout où tes ailes douces planent". C'est un fragment de l'_Ode à la Joie_, un poème de Friedrich Schiller, qui sert de paroles à la plupart des parties chorales du 4ème Mouvement. 

C'est le fragment le plus célèbre du mouvement le plus célèbre de la symphonie la plus célèbre de Beethoven. Qui que vous soyez, quand et comment vous avez été élevé, vous êtes très susceptible de reconnaître ce morceau.

Nous allons maintenant rassembler ce que nous avons fait. Nous allons télécharger l'audio depuis YouTube, découper le choral _Ode à la Joie_ (de `9:51` à `14:04`), et l'enregistrer sous `<nomdefichier> - TRIM.mp3`.

Si vous avez suivi le tutoriel correctement, mettez à jour votre fonction `main()` pour exécuter chaque étape de manière à ce que vous ayez le MP3 complet et la version rognée de celui-ci disponibles en tant que fichiers dans le répertoire à partir duquel vous exécuterez le script. N'oubliez pas d'exécuter la fonction `main()` à la fin du script.

```python
def main():
    yt_url = "https://www.youtube.com/watch?v=8OAPLk20epo"
    download_audio(yt_url)
    initial = "9:51"
    final = "14:04"
    filename = newest_mp3_filename()
    trimmed_file = get_trimmed(filename, initial, final)
    trimmed_filename = "".join([filename.split(".mp3")[0], "- TRIM.mp3"])
    print("Processus conclu avec succès. Enregistrement du fichier rogné sous ", trimmed_filename)
    # enregistre le fichier avec le nouveau nom de fichier
    trimmed_file.export(trimmed_filename, format="mp3")

```

## Comment ajouter une interaction utilisateur directement depuis la CLI

Pour cette partie, nous aurons besoin du module `sys` de Python, qui lit les entrées passées depuis la ligne de commande (entre autres). Nous allons simplement mettre à jour les variables dans la fonction `main()` pour lire les entrées depuis la CLI au lieu des données actuellement codées en dur. 

ARGV lit les entrées séquentiellement sous forme de tableau, en commençant par l'index 1 (0 représente le nom du script Python en cours d'exécution). Nous allons le configurer pour lire une URL en tant que premier argument, puis (optionnellement) les instants de début et de fin du rognage.

```python
import sys

def main():
    if (not len(sys.argv) > 1):
        print("Veuillez insérer une URL de plateforme multimédia supportée par youtube-dl en tant que premier argument.")
        return
    yt_url = sys.argv[1]
    download_audio(yt_url)
    if (not len(sys.argv > 2)): # quitter si aucun instant en tant qu'args
        return
    initial = sys.argv[2]
    final = ""
    if (sys.argv[3]):
        final = sys.argv[3]
    filename = newest_mp3_filename()
    trimmed_file = get_trimmed(filename, initial, final)
    trimmed_filename = "".join([filename.split(".mp3")[0], "- TRIM.mp3"])
    print("Processus conclu avec succès. Enregistrement du fichier rogné sous ", trimmed_filename)
    # enregistre le fichier avec le nouveau nom de fichier
    trimmed_file.export(trimmed_filename, format="mp3")

```

Exécutez le fichier pour le tester. N'oubliez pas de mettre à jour le nom du script avec celui qui est sur votre machine.

```bash
python ytauddown.py https://www.youtube.com/watch?v=8OAPLk20epo 9:51 14:04

```

## Script final

Voici la version finale avec tout rassemblé. Notez que les commentaires sur les modules sont liés uniquement à ce que nous les utilisons et que la fonction `main()` est invoquée à la dernière ligne.

```python
import youtube_dl # client pour télécharger depuis de nombreux portails multimédias
import glob # opérations de répertoire
import os # interface vers les informations fournies par le système d'exploitation sur les fichiers
import sys # interface vers la ligne de commande
from pydub import AudioSegment # uniquement les opérations audio

def newest_mp3_filename():
    # liste tous les mp3 dans le répertoire local
    list_of_mp3s = glob.glob('./*.mp3')
    # retourne le mp3 avec la valeur de timestamp la plus élevée
    return max(list_of_mp3s, key = os.path.getctime)

def get_video_time_in_ms(video_timestamp):
    vt_split = video_timestamp.split(":")
    if (len(vt_split) == 3): # si au format HH:MM:SS
        hours = int(vt_split[0]) * 60 * 60 * 1000
        minutes = int(vt_split[1]) * 60 * 1000
        seconds = int(vt_split[2]) * 1000
    else: # format MM:SS
        hours = 0
        minutes = int(vt_split[0]) * 60 * 1000
        seconds = int(vt_split[1]) * 1000
    # point dans le temps en millisecondes
    return hours + minutes + seconds

def get_trimmed(mp3_filename, initial, final = ""):
    if (not mp3_filename):
        # lever une erreur pour arrêter immédiatement l'exécution du programme
        raise Exception("Aucun MP3 trouvé dans le répertoire local.")
    # lit le mp3 en tant qu'objet PyDub
    sound = AudioSegment.from_mp3(mp3_filename)
    t0 = get_video_time_in_ms(initial)
    print("Début du processus de rognage pour le fichier ", mp3_filename, ".\n")
    print("Début à ", initial, "...")
    if (len(final) > 0):
        print("...jusqu'à ", final, ".\n")
        t1 = get_video_time_in_ms(final)
        return sound[t0:t1] # t0 jusqu'à t1
    return sound[t0:] # t0 jusqu'à la fin



# télécharge yt_url dans le même répertoire à partir duquel le script s'exécute
def download_audio(yt_url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([yt_url])

def main():
    if (not len(sys.argv) > 1):
        print("Veuillez insérer une URL de plateforme multimédia supportée par youtube-dl en tant que premier argument.")
        return
    yt_url = sys.argv[1]
    download_audio(yt_url)
    if (not len(sys.argv > 2)): # quitter si aucun instant en tant qu'args
        return
    initial = sys.argv[2]
    final = ""
    if (sys.argv[3]):
        final = sys.argv[3]
    filename = newest_mp3_filename()
    trimmed_file = get_trimmed(filename, initial, final)
    trimmed_filename = "".join([filename.split(".mp3")[0], "- TRIM.mp3"])
    print("Processus conclu avec succès. Enregistrement du fichier rogné sous ", trimmed_filename)
    # enregistre le fichier avec le nouveau nom de fichier
    trimmed_file.export(trimmed_filename, format="mp3")

# exemple d'utilisation :
# python ytauddown.py https://www.youtube.com/watch?v=8OAPLk20epo 9:51 14:04
main()

```

## Exercices suggérés

1. Détecter si la première entrée est une URL valide ou non. Jetez un coup d'œil à Python RegEx si vous ne savez pas par où commencer.
2. Détecter si les deuxième et troisième entrées sont au format valide (heures:minutes:secondes **OU** minutes:secondes).
3. Ajouter une option pour renommer le fichier MP3 directement depuis la CLI. N'oubliez pas que les arguments ARGV sont exécutés dans l'ordre.
4. Refactoriser ce script afin d'interagir avec ses fonctionnalités en utilisant une interface graphique. Cela peut être une application web ou locale, à votre choix.

## Considérations finales

J'espère que vous vous amuserez avec ce projet et que vous l'utiliserez à bon escient. 

N'oubliez pas que gagner sa vie en tant qu'artiste est assez difficile, surtout pour la majorité sans soutien corporatif. N'oubliez pas de soutenir les artistes dont vous appréciez le travail chaque fois que vous le pouvez et n'oubliez pas non plus de soutenir les logiciels open-source.