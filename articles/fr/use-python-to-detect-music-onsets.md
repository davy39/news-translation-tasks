---
title: Comment utiliser Python pour détecter les attaques musicales
subtitle: ''
author: Lynn Zheng
co_authors: []
series: null
date: '2021-07-22T16:56:17.000Z'
originalURL: https://freecodecamp.org/news/use-python-to-detect-music-onsets
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Python-Music-Onset-Detection.png
tags:
- name: music
  slug: music
- name: Python
  slug: python
seo_title: Comment utiliser Python pour détecter les attaques musicales
seo_desc: 'In music terminology, an onset refers to the beginning of a musical note
  or other sound. In this post, we will look at how to detect music onsets with Python''s
  audio signal processing libraries, Aubio and librosa.

  This tutorial is relevant even if yo...'
---

En terminologie musicale, une **attaque** fait référence au **début d'une note musicale ou d'un autre son**. Dans cet article, nous allons voir comment détecter les attaques musicales avec les bibliothèques de traitement de signal audio de Python, [Aubio](https://aubio.org/) et [librosa](https://librosa.org/doc/latest/index.html).

Ce tutoriel est pertinent même si votre application n'utilise pas Python - par exemple, vous construisez un jeu dans Unity et C# qui n'a pas de bibliothèques robustes pour la détection d'attaques.

Si c'est le cas, vous pouvez exporter les timestamps des attaques détectées vers un fichier texte à lire dans votre moteur de choix.

Si vous préférez un tutoriel vidéo à un article, voici la version vidéo de ce tutoriel.

%[https://youtu.be/aMMI0nAKgI0] 

## Applications de la détection d'attaques musicales

J'ai découvert cette technique de détection d'attaques musicales lorsque je construisais **un jeu de rythme** et que je voulais un moyen de **générer automatiquement** des cartes de rythme pour n'importe quelle chanson.

Consultez la fin de cet article pour mon [jeu de rythme open-source](https://github.com/RuolinZheng08/renpy-rhythm) et [mon cours étape par étape sur la façon dont je l'ai construit.](https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973)

![Image d'un jeu de rythme similaire à Guitar Hero](https://www.freecodecamp.org/news/content/images/2021/07/ezgif.com-gif-maker.gif align="left")

*Ma vitrine de jeu de rythme*

Outre la construction d'un jeu de rythme, cette technique a de nombreuses autres applications.

Par exemple, la détection des attaques est généralement la première étape dans **l'extraction et l'analyse d'informations musicales**.

Un autre exemple pourrait être que nous construisons un jeu dans lequel il y a des scènes de combat. Nous pouvons détecter les attaques dans la musique de fond et faire apparaître un ennemi à chaque attaque. Cela peut créer un rythme unique dans notre jeu.

Je vais démontrer comment détecter les attaques musicales en utilisant deux packages Python différents pour le **traitement de signal audio**, [Aubio](https://aubio.org/) et [librosa](https://librosa.org/doc/latest/index.html). Les deux packages détectent les attaques avec une précision assez bonne. La petite différence est que librosa fonctionne pour le format **OGG** tandis qu'Aubio ne le fait pas.

## Comment configurer l'environnement de développement

Nous allons installer nos packages dans un environnement virtuel.

Dans la ligne de commande, nous créons un environnement virtuel nommé `python-aubio-librosa` comme suit. `-m` signifie `module`.

```pgsql
$ python3 -m venv python-aubio-librosa
```

Ensuite, nous activons l'environnement virtuel :

```pgsql
$ . python-aubio-librosa/bin/activate
```

Notez que si vous essayez d'activer l'environnement en utilisant la commande suivante, vous obtiendrez une erreur :

```pgsql
$ ./python-aubio-librosa/bin/activate
-bash: ./python-aubio-librosa/bin/activate: Permission denied
```

Une fois votre environnement activé, le nom de l'environnement s'affichera entre parenthèses :

```pgsql
(python-aubio-librosa) $ ...
```

Nous pouvons vérifier que si nous invoquons `python` ou `pip`, les programmes invoqués seront ceux de notre environnement virtuel au lieu de ceux du système.

Si nous n'avons pas activé notre environnement, la sortie pointera vers les programmes du système.

```pgsql
$ which python
/usr/bin/python
$ which pip
/usr/local/bin/pip
```

Une fois que nous avons activé notre environnement, la sortie pointera vers les programmes locaux.

```pgsql
(python-aubio-librosa) $ which python
/Users/USERNAME/Desktop/python-aubio-librosa/bin/python
(python-aubio-librosa) $ which pip
/Users/USERNAME/Desktop/python-aubio-librosa/bin/pip
```

## Comment installer et utiliser Aubio

Nous allons installer Aubio via `pip` :

```pgsql
(python-aubio-librosa) $ pip install aubio
```

La fonction que nous allons utiliser pour générer une liste de timestamps d'attaques sous forme de nombres à virgule flottante en secondes est la suivante. Cette fonction provient des [documentations officielles d'Aubio](https://github.com/aubio/aubio/blob/master/python/demos/demo_onset.py), nous pouvons donc simplement l'utiliser sans apprendre les détails techniques (comme FFT, Fast-Fourier Transformations) du traitement de signal audio.

```python
from aubio import source, onset

def get_onset_times(file_path):
    window_size = 1024 # Taille de la FFT
    hop_size = window_size // 4

    sample_rate = 0
    src_func = source(file_path, sample_rate, hop_size)
    sample_rate = src_func.samplerate
    onset_func = onset('default', window_size, hop_size)
    
    duration = float(src_func.duration) / src_func.samplerate

    onset_times = [] # secondes
    while True: # lire les frames
        samples, num_frames_read = src_func()
        if onset_func(samples):
            onset_time = onset_func.get_last_s()
            if onset_time < duration:
                onset_times.append(onset_time)
            else:
                break
        if num_frames_read < hop_size:
            break
    
    return onset_times
```

Ensuite, nous écrivons une fonction `main` qui prend le chemin vers un fichier audio et sortie les timestamps des attaques vers un fichier, en gardant les quatre premières décimales de chaque float, un float par ligne.

```python
def main():
    file_path = '../game/audio/my-music.mp3'
    onset_times = get_onset_times(file_path)
    # supprimer l'extension, .mp3, .wav etc.
    file_name_no_extension, _ = os.path.splitext(file_path)
    output_name = file_name_no_extension + '.beatmap.txt'
    with open(output_name, 'wt') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
```

Invoquons le script depuis la ligne de commande. Aubio peut lever un avertissement sur la précision, mais mes expérimentations montrent qu'Aubio est toujours assez précis.

```pgsql
(python-aubio-librosa) $ python generate_beatmap_aubio.py 
[mp3 @ 0x7fe671031e00] Estimating duration from bitrate, this may be inaccurate
```

Un exemple de fichier de sortie ressemblerait à ceci. Pour un court extrait musical de 15 secondes, Aubio a détecté 26 attaques. Ce sont les timestamps que nous pouvons utiliser pour notre application.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-20-at-13.54.18.png align="left")

*Un exemple de fichier de sortie contenant des timestamps d'attaques*

Et c'est tout pour Aubio.

## Comment installer et utiliser Librosa

Similaire à Aubio, nous allons installer librosa également via `pip` :

```pgsql
(python-aubio-librosa) $ pip install librosa
```

Comparé à Aubio, les méthodes de la bibliothèque librosa sont plus faciles à utiliser. `librosa.load` retourne un tableau NumPy `x` et un taux d'échantillonnage `sr`, que nous passons à `librosa.onset.onset_detect` pour obtenir une liste de frames d'attaques.

Enfin, nous convertissons les frames d'attaques en timestamps d'attaques, et écrivons chaque timestamp dans un fichier de sortie comme nous l'avons fait pour Aubio.

```python
import librosa

def main():
    file_path = '../game/audio/my-music.ogg'
    x, sr = librosa.load(file_path)
    onset_frames = librosa.onset.onset_detect(x, sr=sr, wait=1, pre_avg=1, post_avg=1, pre_max=1, post_max=1)
    onset_times = librosa.frames_to_time(onset_frames)
    # supprimer l'extension, .mp3, .wav etc.
    file_name_no_extension, _ = os.path.splitext(file_path)
    output_name = file_name_no_extension + '.beatmap.txt'
    with open(output_name, 'wt') as f:
        f.write('\n'.join(['%.4f' % onset_time for onset_time in onset_times]))
```

Le fichier de sortie sera dans le même format que celui montré ci-dessus pour Aubio.

## Conclusion

Merci d'avoir lu et j'espère que vous êtes prêt à appliquer cette technique de détection d'attaques à votre prochain projet. 🎶

Pour résumer les différences entre Aubio et Librosa, les deux détectent les attaques avec une précision assez bonne selon mes expérimentations.

Aubio est plus restreint en termes de formats de fichiers audio : il lève un avertissement sur la précision pour les fichiers MP3 et ne gère pas les fichiers OGG.

En revanche, Librosa est capable de gérer la plupart des formats de fichiers audio courants : MP3, OGG, FLAC et M4A. L'interface de la bibliothèque Librosa est également plus facile à utiliser que celle d'Aubio, surtout pour ceux d'entre nous qui ne sont pas des professionnels du traitement de signal.

Consultez les ressources ci-dessous si vous souhaitez en savoir plus ou vous inspirer pour votre prochain projet !

## Ressources

Vous pouvez consulter le code utilisé dans ce tutoriel [sur mon GitHub](https://github.com/RuolinZheng08/renpy-minigames101/tree/master/generate_beatmap) ou [regarder la version vidéo de ce tutoriel sur YouTube.](https://youtu.be/aMMI0nAKgI0)

Si vous êtes intéressé par la construction d'un jeu de rythme, consultez [mon jeu open-source construit en Python sur GitHub](https://github.com/RuolinZheng08/renpy-rhythm) et mon cours Udemy dans lequel nous construirons le jeu à partir de zéro.

%[https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973] 

Si vous souhaitez savoir si le cours est fait pour vous, consultez ma vidéo promotionnelle du cours sur YouTube et [des leçons d'exemple gratuites sur Udemy.](https://www.udemy.com/course/renpy-minigames/?referralCode=46F88E557D14A0FDD973)

%[https://youtu.be/_AaUKSjTNY8] 

Ma chaîne YouTube propose également d'autres tutoriels de projets amusants comme [la construction d'un chatbot IA Discord](https://youtu.be/UBwvFuTC1ZE), et [une série de cours intensifs sur les entretiens de codage](https://youtu.be/H2gnD7Ixeao) que je développe. J'espère vous y voir !

%[https://www.youtube.com/channel/UCZ2MeG5jTIqgzEMiByrIzsw]