---
title: Comment optimiser vos flux de travail bash avec GNU parallel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-12T22:31:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-supercharge-your-bash-workflows-with-gnu-parallel-53aab0aea141
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t40_MeHpD55L892RmAGa_g.jpeg
tags:
- name: Bash
  slug: bash
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment optimiser vos flux de travail bash avec GNU parallel
seo_desc: 'By Zach Caceres

  GNU parallel is a command line tool for running jobs in parallel.

  parallel is awesome and belongs in the toolbox of every programmer. But I found
  the docs a bit overwhelming at first. Fortunately, you can start being useful with
  paral...'
---

Par Zach Caceres

[GNU](https://www.gnu.org/software/parallel/) [`parallel`](https://www.gnu.org/software/parallel/) est un outil en ligne de commande pour exécuter des tâches en parallèle.

`parallel` est génial et devrait faire partie de la boîte à outils de chaque programmeur. Mais j'ai trouvé [la documentation](https://www.gnu.org/software/parallel/man.html) un peu écrasante au début. Heureusement, vous pouvez commencer à utiliser `parallel` de manière utile avec seulement quelques commandes de base.

#### Pourquoi `parallel` est-il si utile ?

Comparons l'exécution séquentielle et parallèle de la même tâche intensive en calcul.

Imaginez que vous avez un dossier de fichiers audio .wav à convertir en .flac :

![Image](https://cdn-media-1.freecodecamp.org/images/pwuETgAZqyFpphdmdLk0FWhPL7oTMEri0hh9)
_fichiers .wav_

Ce sont des fichiers assez volumineux, chacun faisant au moins un gigaoctet.

Nous utiliserons un autre excellent outil en ligne de commande, [ffmpeg](https://ffmpeg.org/), pour convertir les fichiers. Voici ce que nous devons exécuter pour chaque fichier.

```
ffmpeg -i audio1.wav audio1.flac
```

Écrivons un script pour convertir chaque fichier séquentiellement :

```sh
# convert.sh
ffmpeg -i audio1.wav audio1.flac
ffmpeg -i audio2.wav audio2.flac
ffmpeg -i audio3.wav audio3.flac
ffmpeg -i audio4.wav audio4.flac
ffmpeg -i audio5.wav audio5.flac
```

Nous pouvons mesurer le temps d'exécution d'une tâche en ajoutant `time` lors de l'appel du script depuis le terminal. `time` affichera le temps réel écoulé pendant l'exécution.

```
time ./convert.sh
```

Notre script se termine en un peu plus d'une minute.

![Image](https://cdn-media-1.freecodecamp.org/images/Ogv4D0s6iSZGXToI-iqHEtIRA8tnxNyQXJ2g)
_le temps d'exécution séquentielle_

Pas mal. Mais maintenant, exécutons-le en parallèle !

Nous n'avons pas besoin de changer quoi que ce soit dans notre script. Avec le flag `-a`, nous pouvons transmettre notre script directement à `parallel`. `parallel` exécutera chaque ligne comme une commande séparée.

```
parallel -a ./convert.sh
```

En utilisant `parallel`, notre conversion s'est exécutée en un peu plus de la moitié du temps. Bien !

![Image](https://cdn-media-1.freecodecamp.org/images/Ewm0aJAZhb-cuL65NVBvnOjb6Fvr9X2sWIqw)
_le temps d'exécution parallèle_

Avec seulement cinq fichiers, cette différence n'est pas si importante. Mais avec des listes plus longues et des tâches plus longues, nous pouvons économiser beaucoup de temps avec `parallel`.

J'ai rencontré `parallel` en travaillant sur une tâche de traitement de données qui aurait probablement pris une heure ou plus si elle avait été effectuée séquentiellement. Avec `parallel`, cela n'a pris que quelques minutes.

La puissance de `parallel` dépend également de votre ordinateur. Mon MacBook Pro avec un Intel i7 n'a que 4 cœurs. Même cette petite tâche les a tous poussés à leur limite :

![Image](https://cdn-media-1.freecodecamp.org/images/plEr7TOAAn9AbE2gtW7dDJiXcxKGRT2L2kf8)

Les ordinateurs plus puissants peuvent avoir des processeurs avec 8, 16, ou même 32 cœurs, offrant des économies de temps massives grâce à la parallélisation de vos tâches.

### Être utile avec `parallel`

L'autre grand avantage de `parallel` est sa brièveté et sa simplicité. Commençons par un script Python compliqué et convertissons-le en un appel propre à `parallel`.

Voici un script Python pour accomplir notre conversion de fichiers audio :

```py
import subprocess
path = Path.home()/'my-data-here'
for audio_file in list(path.glob('*.wav')):
    cmd = ['ffmpeg',
           '-i',
           str(audio_file),
           f'{audio_file.name.split(".")[0]}.flac']
    subprocess.run(cmd, stdout=subprocess.PIPE)
```

Aïe ! C'est en fait beaucoup de code à réfléchir juste pour convertir quelques fichiers. (Cela prend environ 1,2 minute à exécuter).

Convertissons notre Python en `parallel`.

### Appeler un script avec `parallel -a`

`parallel -a your-script-here.sh` est la belle commande en une ligne que nous avons utilisée ci-dessus pour transmettre notre script bash.

C'est génial mais cela nécessite que vous écriviez le script bash que vous souhaitez exécuter. Dans notre exemple, nous avons toujours écrit chaque appel individuel à `ffmpeg` dans `convert.sh`.

### Pipes et interpolation de chaînes avec `parallel`

Heureusement, `parallel` nous donne un moyen de supprimer entièrement `convert.sh`.

Voici tout ce que nous devons exécuter pour accomplir notre conversion :

```
ls *.wav | parallel ffmpeg -i {} {.}.flac
```

Décomposons cela.

Nous obtenons une liste de tous les fichiers .wav dans notre répertoire avec `ls *.wav`. Ensuite, nous transmettons (`|`) cette liste à `parallel`.

Parallel fournit des moyens utiles de faire de l'interpolation de chaînes, afin que nos chemins de fichiers soient saisis correctement.

Le premier est `{}`, que `parallel` remplace automatiquement par une ligne de notre entrée.

Le deuxième opérateur est `{.}`, qui saisira une ligne mais avec toute extension de fichier supprimée.

Si nous développons la commande exécutée par `parallel` pour notre première ligne d'entrée, nous verrions...

```
ffmpeg -i audio1.wav audio1.flac
```

### Args avec `Parallel`

Il s'avère que nous n'avons même pas besoin de transmettre depuis `ls` pour accomplir notre tâche. Nous pouvons aller encore plus simple :

```
parallel ffmpeg -i {} {.}.flac ::: *.wav
```

Les arguments passés à `parallel` se trouvent après la commande et sont séparés par `:::`. Dans ce cas, notre argument est `*.wav`, qui fournira la liste de tous les fichiers .wav dans notre répertoire. Ces fichiers deviennent l'entrée pour notre travail ultra-rapide `parallel`.

Fait amusant : `parallel` a été créé par [Ole Tange](http://ole.tange.dk/) et publié en 2011. Selon lui, vous pouvez utiliser l'outil pour la recherche sans citer l'article source pour la modeste somme de 10 000 euros !

![Image](https://cdn-media-1.freecodecamp.org/images/7MEg7-7ibkq3EurYW9xudzKLJRHuZvdTUbwW)

Merci d'avoir lu !