---
title: Programmation en binôme avec l'IA ChatGPT – GPT-3.5 comprend-il Bash ?
subtitle: ''
author: David Clinton
co_authors: []
series: null
date: '2022-12-16T17:51:07.000Z'
originalURL: https://freecodecamp.org/news/pair-programming-with-the-chatgpt-ai-how-well-does-gpt-3-5-understand-bash
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/pexels-pavel-danilyuk-8438951.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Bash
  slug: bash
- name: Chat
  slug: chat
seo_title: Programmation en binôme avec l'IA ChatGPT – GPT-3.5 comprend-il Bash ?
seo_desc: "We've been hearing a lot about artificial intelligence and natural language\
  \ processing – and in particular about the latest version of OpenAI's GPT – for\
  \ weeks. \nThe recent release of GPT 3.5, and specifically the very new ChatGPT\
  \ tool, is definitely..."
---

Nous entendons parler d'intelligence artificielle et de traitement du langage naturel – et en particulier de la dernière version de GPT d'OpenAI – depuis des semaines. 

La récente sortie de GPT 3.5, et plus spécifiquement du tout nouveau outil ChatGPT, est définitivement un énorme bond en avant.

Vous avez peut-être lu des articles sur des personnes demandant à l'IA de rédiger des contrats immobiliers et des testaments, et même de générer du code de programmation. Cet article aborde l'outil sous un angle légèrement différent. 

Vous pouvez regarder une version vidéo de cet article ici si vous souhaitez l'utiliser pour compléter votre apprentissage :

%[https://www.youtube.com/watch?v=GxJKuINwPSw]

## Expérimentation avec ChatGPT et la programmation Bash

J'ai décidé de voir comment ChatGPT gère la programmation Bash sous Linux. Mais (alerte spoiler !) alors que je travaillais sur les suggestions de l'outil – à la fois le bon et le mauvais code – j'ai commencé à réaliser qu'il y avait un avantage encore plus puissant qui me regardait en face : une opportunité de programmer en binôme avec un partenaire extrêmement utile.

L'IA n'a finalement pas réussi à résoudre mon problème, mais la *manière* dont elle a échoué était absolument fascinante. Et regarder l'IA chercher de nouvelles réponses était absolument fou.

### Première tentative – ChatGPT essaie de résoudre le problème

Alors, voyons comment tout cela s'est passé. Voici, plus ou moins, la première instruction que j'ai fournie à l'IA :

> Écrivez-moi un script Bash qui demande l'URL d'une vidéo YouTube et utilise ensuite le programme yt-dlp pour télécharger depuis cette URL. Le script doit ensuite changer le nom du fichier en "myvideo.mp4"

Après quelques secondes, ChatGPT m'a dit qu'un script était en cours de génération. Voici à quoi ressemblait ce code :

```
#!/bin/bash

# Demander à l'utilisateur l'URL de la vidéo YouTube
read -p "Entrez l'URL de la vidéo YouTube : " url

# Télécharger la vidéo depuis YouTube en utilisant yt-dlp
yt-dlp $url

# Obtenir le nom du fichier vidéo téléchargé
yt-dlp $url

# Changer le nom du fichier vidéo téléchargé en "myvideo.mkv"
mv video-filename.mp4 myvideo.mp4
```

L'IA connaît clairement les scripts Bash et comment présenter du code. Elle a même fait un excellent travail en commentant chaque ligne de code. L'IA sait comment demander correctement à l'utilisateur une entrée et ensuite comment importer la chaîne d'entrée dans une variable appelée `url`. 

Elle connaît également le programme yt-dlp et son fonctionnement, lui fournissant de manière appropriée l'URL fournie. Ensuite, elle a au moins tenté de renommer le fichier vidéo téléchargé en myvideo.mp4. Mais tout s'est un peu effondré lorsqu'elle a supposé que le nom du fichier téléchargé serait video-filename.mp4. Oups.

Dans tous les cas, l'IA m'a utilement montré comment créer le script à partir de son code et ensuite l'exécuter.

### Deuxième tentative – ChatGPT se corrige

Ma première instruction de suivi a pointé l'erreur évidente et, après quelques secondes, ChatGPT a admis qu'elle avait tort et a proposé une amélioration. 

> Vous avez raison, le script que j'ai fourni ne fonctionnerait pas comme prévu car il suppose que la vidéo téléchargée sera enregistrée dans un fichier nommé `video-filename.mp4`. Cependant, ce n'est pas garanti. Pour corriger cela...

C'est tout simplement incroyable comment l'IA est complètement engagée dans le processus ici. Elle se souvient de son premier code, écoute et comprend ma plainte, et réfléchit à une solution. Voici cette deuxième tentative :

```
#!/bin/bash

# Demander à l'utilisateur l'URL de la vidéo YouTube
read -p "Entrez l'URL de la vidéo YouTube : " url

# Télécharger la vidéo depuis YouTube en utilisant yt-dlp
yt-dlp $url

# Obtenir le nom du fichier vidéo téléchargé
filename=$(basename $url)

# Changer le nom du fichier vidéo téléchargé en "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

D'accord, donc je peux voir comment la solution semblait correcte. `basename` est un outil Linux qui peut supprimer les répertoires du système de fichiers et ne laisser que le nom de fichier réel.

Le problème est que la variable `url` ne contient pas un nom de fichier local, mais une adresse internet. Celui-ci ne fonctionnera définitivement pas.

### Troisième tentative – ChatGPT essaie à nouveau

J'ai donc essayé à nouveau, expliquant comment ce n'était pas le bon outil pour le travail. Et ChatGPT tente à nouveau. 

```
#!/bin/bash

# Demander à l'utilisateur l'URL de la vidéo YouTube
read -p "Entrez l'URL de la vidéo YouTube : " url

# Extraire le nom de fichier de l'URL
filename=$(basename $url)

# Télécharger la vidéo en utilisant l'outil yt-dlp et spécifier le nom de fichier
yt-dlp -o $filename $url

# Changer le nom du fichier vidéo téléchargé en "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

Cette fois, il montre qu'il s'est familiarisé avec la documentation de yt-dlp, suggérant que nous utilisions l'argument `-o` pour donner un nom à la vidéo en cours de téléchargement, contre lequel `basename` devrait maintenant fonctionner. À chaque itération, l'IA me donne ce code mis à jour pour mon plaisir de copier-coller.

Bien sûr, cela ne fonctionnerait pas non plus. Avec la tentative suivante, j'ai l'impression que l'IA est un peu désespérée. 

### Si au premier essai vous ne réussissez pas... Au moins vous apprendrez quelque chose

Je vais passer les prochaines tentatives, car nous avons rencontré un problème secondaire : les vidéos provenant de YouTube ne sont pas toujours des MP4, elles sont parfois des MKV ou même des WEBM. Cette incertitude pourrait perturber les noms de fichiers avec lesquels nous travaillons, alors j'ai demandé à ChatGPT de l'intégrer dans le code. 

```
#!/bin/bash

# Demander à l'utilisateur l'URL de la vidéo YouTube
read -p "Entrez l'URL de la vidéo YouTube : " url

# Extraire le nom de fichier de l'URL
filename=$(basename $url)

# Télécharger la vidéo en utilisant l'outil yt-dlp et spécifier le nom de fichier
yt-dlp -F mp4 -O $filename $url

# Changer le nom du fichier vidéo téléchargé en "myvideo.mkv"
mv $filename.mp4 myvideo.mp4
```

Lorsque j'ai signalé que cela ne fonctionnerait pas non plus, l'IA a commencé à se confondre. D'abord, elle m'a dit que l'option `-F` attendait un format vidéo valide, mais que "mp4" n'était pas valide. Ensuite, elle me donne des options valides, y compris "mp4".

Lorsque rien de ce que l'IA a suggéré n'a fonctionné, elle a abandonné, me conseillant de m'assurer que yt-dlp était réellement installé sur ma machine et me montrant comment faire cela. 

J'ai pensé que c'était un bon moment pour abandonner. C'était un effort surprenamment bon et, même si cela n'a pas résolu le problème, cela m'a montré une syntaxe utile et m'a fait réfléchir.

Au cas où vous seriez intéressé, voici à quoi ressemblerait un script fonctionnel réel. 

```
#!/bin/bash

# Demander à l'utilisateur l'URL de la vidéo YouTube
read -p "Entrez l'URL de la vidéo YouTube : " url

# Télécharger la vidéo depuis YouTube en utilisant yt-dlp
yt-dlp $url

# Obtenir le nom du fichier vidéo téléchargé
original_filename=$(ls | awk '/mp4/ || /webm/ || /mkv/')

# Changer le nom du fichier vidéo téléchargé en "myvideo.mkv"
mv "$original_filename" /home/ubuntu/vids/myvideo.mp4
```

Les deux premières lignes de code sont exactement comme ChatGPT l'a suggéré. Mais j'isole ensuite le nom de fichier en listant tous les fichiers dans le répertoire courant et en utilisant `awk` pour filtrer uniquement les noms de fichiers contenant mp4, webm ou mkv. (Cela suppose qu'il n'y aura jamais plus d'un fichier vidéo dans le répertoire à la fois.) 

Le nom de fichier sera ensuite écrit dans la variable `original_filename`. J'utiliserai ensuite cette variable dans le cadre d'une commande `move` pour renommer le fichier `myvideo.mp4`. Dans la mesure où je peux en juger, cela fonctionnera quelle que soit la forme réellement envoyée.

## Conclusion

L'intelligence artificielle n'est peut-être pas tout à fait prête pour les tâches de programmation du monde réel aujourd'hui, mais je ne voudrais pas parier contre elle pour y parvenir demain... ou quelque temps l'année prochaine. 

En attendant, je recommanderais absolument d'utiliser des outils comme ChatGPT chaque fois que vous êtes confronté à une tâche de programmation difficile. 

Deux têtes valent (presque) toujours mieux qu'une.

_En plus de [ma chaîne YouTube](https://www.youtube.com/@davidbclinton) (à laquelle vous pouvez vous abonner), [mon site web](https://bootstrap-it.com) propose des liens vers toutes sortes de ressources technologiques disponibles sous forme d'articles, de livres et de cours._