---
title: Format de fichier WAV – Comment ouvrir un WAV et convertir des WAV en MP3
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-30T18:46:16.000Z'
originalURL: https://freecodecamp.org/news/wav-file-format-how-to-open-a-wav-and-convert-wavs-to-mp3
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/Untitled-design.jpg
tags:
- name: audio
  slug: audio
- name: how-to
  slug: how-to
seo_title: Format de fichier WAV – Comment ouvrir un WAV et convertir des WAV en MP3
seo_desc: 'By Vaibhav Kandwal

  Audio is a very important part of any digital media. Since audio or sound is a wave
  (a literal, continuous wave) it is analog in nature. This means that it cannot be
  stored and processed by the computer directly, as a computer only...'
---

Par Vaibhav Kandwal

L'audio est une partie très importante de tout média numérique. Puisque l'audio ou le son est une onde (une onde littérale et continue), il est de nature analogique. Cela signifie qu'il ne peut pas être stocké et traité directement par l'ordinateur, car un ordinateur ne comprend que les signaux numériques. 

Naturellement, les ingénieurs ont trouvé un moyen de convertir ces signaux analogiques en signaux numériques. Ils ont également développé une méthode pour les enregistrer au format numérique. Je parle des codecs audio.

Les codecs audio, en termes plus simples, sont simplement des encodeurs et des décodeurs (_co_ - codeurs, _dec_ - décodeurs, ou _co_ - compresseur, _dec_ - décompresseur). Ils peuvent être implémentés sous forme de codecs matériels, qui encodent l'audio analogique en audio numérique et vice versa. 

Un exemple de tels codecs sont les cartes son de votre ordinateur, qui disposent de circuits intégrés analogique-numérique (ADC) et numérique-analogique (DAC).

Le pendant logiciel est un algorithme qui compresse et décompresse l'audio numérique. Certains exemples de tels codecs sont MP3, FLAC, WAV et AAC.  
  
Aujourd'hui, nous allons examiner les encodeurs logiciels et nous allons nous concentrer sur le format WAV.

## Ce que signifie la compression dans les codecs audio

Les algorithmes de compression audio sont divisés en deux catégories : _Sans perte_ et _Avec perte_. Quelle est donc la différence entre ces deux types ?

### Algorithmes sans perte

Ces algorithmes peuvent effectuer une certaine compression sur l'audio, mais ils ne suppriment aucune donnée audio, ainsi rien n'est perdu. Le compromis est que vous avez des tailles de fichiers très grandes.

### Algorithmes avec perte

Dans ce type de compression, une partie de la fidélité audio, jugée inaudible/indistinguable pour l'oreille humaine, est supprimée ou sa fidélité (ou précision ou volume) est réduite. La compression est également effectuée après cette étape. [Vous pouvez en lire plus ici](https://en.wikipedia.org/wiki/Data_compression#Lossy_audio_compression).

Sauf si vous avez un très bon système HI-FI capable de reproduire ces sons de fidélité supplémentaires, vous devriez opter pour la compression avec perte. Cela économisera de l'espace et supprimera les données supplémentaires que vous ne pourriez jamais entendre.

Maintenant que vous comprenez la compression audio, passons au sujet principal de cet article.

## Qu'est-ce que le WAV ?

WAV (ou WAVE) signifie Waveform Audio File Format. Il a été développé par IBM et Microsoft. L'extension de fichier est `.wav` ou `.wave`. 

Le format WAV est largement utilisé lorsque vous souhaitez un audio non compressé. Par exemple, les ingénieurs du son l'utilisent beaucoup – et grâce à sa forme sans perte, il peut être utilisé pour les premiers échantillons de production. 

La grande taille du fichier signifie qu'il n'est généralement pas adapté à la transmission sur Internet. D'autres formats comme MP3 et AAC offrent des tailles de fichiers beaucoup plus petites, car ils sont avec perte.

### Limites du format WAV

Les fichiers WAV sont limités à 4 Go en taille car ils ont un en-tête de taille de fichier 32 bits. W64 est un successeur qui a un en-tête 64 bits, permettant des tailles de fichiers encore plus grandes.  
  
En outre, puisque l'audio n'est pas compressé, sa taille de fichier est grande. Donc, si l'audio est stocké sur un disque dur lent, cela peut causer des problèmes de mise en mémoire tampon (car l'audio doit être chargé du disque vers la RAM avant que le lecteur de musique ne puisse décoder et lire le fichier). 

Cela ne devrait pas être un problème, cependant, sur les ordinateurs modernes, car ils ont des disques durs beaucoup plus rapides.

## Comment ouvrir un fichier WAV

Puisque le WAV est un format assez populaire, presque tous les appareils aujourd'hui le supportent en utilisant des lecteurs multimédias intégrés. 

* Sur Windows, le Lecteur Windows Media est capable de lire les fichiers WAV.
* Sur MacOS, iTunes ou QuickTime peuvent lire les fichiers WAV.
* Sur Linux, votre système ALSA de base peut lire ces fichiers.

D'autres solutions existent également qui peuvent vous aider à lire les fichiers WAV, comme le lecteur multimédia VLC ou tout autre lecteur de musique.

### Comment lire un fichier WAV sur Windows avec le Lecteur Windows Media

1. Ouvrez le Lecteur Windows Media en utilisant la recherche

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-140.png)
_étape 1 : recherche Windows_

2. Glissez-déposez votre fichier audio WAV de l'explorateur vers le Lecteur Windows Media

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc.gif)
_étape 2 : glissez-déposez votre audio_

3. Cliquez sur Lecture !

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-1.jpg)
_étape 3 : cliquez sur lecture_

### Comment lire un fichier WAV sur n'importe quel système d'exploitation avec VLC Media Player

VLC media player est un lecteur multimédia open-source qui peut lire la plupart de vos formats de fichiers sans avoir besoin de télécharger des codecs externes. Il est multiplateforme, donc vous obtiendrez les mêmes fonctionnalités et interface sur tous les systèmes d'exploitation, que vous utilisiez Linux, Windows ou MacOS (supporte également Android et iOS). 

Voici les étapes pour lire un fichier WAV avec VLC sur votre PC.

1. Téléchargez VLC depuis le site officiel [ici](https://www.videolan.org/)
2. Ouvrez VLC
3. Cliquez sur Médias, puis sélectionnez Ouvrir un fichier

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-2-1.jpg)
_étape 3 : cliquez sur 'médias', puis cliquez sur 'ouvrir un fichier'_

4. Dans la boîte de dialogue de sélection de fichier, choisissez votre audio, cliquez sur `Ouvrir` et le fichier WAV devrait commencer à jouer automatiquement !

![Image](https://www.freecodecamp.org/news/content/images/2021/03/Untitled-3.jpg)
_étape 4 : sélectionnez votre fichier et cliquez sur 'ouvrir'_

Ou si vous préférez un GIF :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc2.gif)
_Etapes 1-4 pour VLC :D_

## Comment convertir des fichiers WAV en MP3

Selon le périphérique final, vous pourriez vouloir convertir le WAV en d'autres formats, par exemple pour économiser de l'espace disque ou si vous écoutez sur un périphérique bas de gamme.

Le MP3 est un format assez bon pour stocker l'audio. Il vous donne des tailles de fichiers 50-75 % plus petites, tout en conservant presque la même expérience d'écoute. Voyons comment vous pouvez convertir ces fichiers.

### Convertisseurs en ligne

Si vous ne convertissez l'audio que rarement, je vous suggère d'utiliser un convertisseur en ligne tel que [CloudConvert](https://cloudconvert.com/wav-converter). Et Google est votre ami ici. 

Gardez à l'esprit que ces convertisseurs en ligne peuvent stocker vos fichiers pendant un certain temps (même pour toujours), alors lisez leur politique si vous voulez convertir quelque chose de critique.

### Convertisseurs hors ligne

Une autre option est de convertir ces fichiers localement. Cela vous aidera si vous voulez convertir fréquemment ou si vous avez quelque chose que vous ne voulez pas exposer sur Internet.  
  
Il y a deux façons de faire cela :

**[Audacity](https://www.audacityteam.org/)** : Audacity est une application gratuite, open-source et multiplateforme qui vous permet d'éditer et de convertir l'audio. 

Le seul inconvénient est que vous devez faire une configuration initiale (installation de LAME). De plus, vous devez convertir les fichiers un par un. 

**[FFmpeg](https://ffmpeg.org/)** : FFmpeg est un outil en ligne de commande multiplateforme pour convertir des fichiers audio et vidéo. Vous pouvez exécuter la commande suivante pour convertir un fichier wav en mp3 :  
`ffmpeg -i input.wav output.mp3`

Vous pouvez explorer la documentation de FFmpeg pour comprendre comment personnaliser certains paramètres et passer une liste de fichiers pour des conversions par lots.

Le principal inconvénient est que FFmpeg n'est pas convivial. Vous devez savoir comment utiliser les outils en ligne de commande. Bien que des choses comme une interface graphique pour FFmpeg existent, cela dépasse le cadre de notre discussion ici.

### Merci d'avoir lu !

J'espère que cet article vous a donné quelques informations sur la compression audio, ainsi que sur la façon de manipuler et de convertir des fichiers WAV. 

Pour toute question ou commentaire, vous pouvez me trouver sur Twitter [@vaibhav_kandwal](https://twitter.com/vaibhav_kandwal). Merci d'avoir lu.