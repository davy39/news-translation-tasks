---
title: Bots Slack non financés
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-01T16:32:06.000Z'
originalURL: https://freecodecamp.org/news/unfundable-slack-bots-9369a75fdd
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KUlXltNVajILJHiucE6sHg.png
tags:
- name: bots
  slug: bots
- name: Design
  slug: design
- name: humor
  slug: humor
- name: slack
  slug: slack
- name: star wars
  slug: star-wars
seo_title: Bots Slack non financés
seo_desc: 'By Bertrand Fan

  In December, Slack announced a $80 million fund to invest in software projects that
  complement its technology. As an early adopter of the Slack API, here are some “bets”
  that I’ve made on the Slack platform:

  A bot that plays all of St...'
---

Par Bertrand Fan

En décembre, Slack a annoncé un fonds de 80 millions de dollars pour investir dans des projets logiciels qui complètent sa technologie. En tant qu'adoptant précoce de l'API Slack, voici quelques "paris" que j'ai faits sur la plateforme Slack :

#### Un bot qui joue toute l'édition déspecialisée de Star Wars (Han tire en premier !) une image toutes les dix secondes. Il faut environ 20 heures pour parcourir tout le film.

![Image](https://cdn-media-1.freecodecamp.org/images/1*KUlXltNVajILJHiucE6sHg.png)

#### Un bot qui héberge des jeux de The Resistance (optionnellement avec le Module Assassin de l'extension Hidden Agenda). Le vote secret est effectué via DM avec le bot, tandis que les actions publiques sont faites dans le canal.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mrfae1_an3lG1l9BxOBoyA.png)

#### Un bot qui vous permet de jouer à Wolfenstein 3D en émettant des commandes (gauche, droite, haut, bas, ouvrir et tirer). Vous pouvez optionnellement spécifier combien de degrés tourner à gauche et à droite, mais par défaut vous tournez de 45 degrés. Je n'ai jamais réussi à compléter le premier niveau, mais j'ai réussi à tuer plusieurs gardes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZZSwPJsD1p3xiyHJzP9HMQ.gif)

Je suis heureux d'annoncer que j'ai terminé mon dernier bot, [Vandelay Industries](https://vandelayindustries.online/). Vandelay Industries est un plagiat éhonté de [Frinkiac](https://frinkiac.com/) qui vous permet de rechercher des gifs animés de chaque épisode de Seinfeld dans Slack. Il contient chaque ligne de dialogue jamais prononcée dans Seinfeld.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dF_ekpm0NzefyQJBIw07ww.gif)

Si vous souhaitez l'essayer dans votre équipe Slack, rendez-vous simplement sur [Vandelay Industries](https://vandelayindustries.online) et cliquez sur **Ajouter à Slack**. Il vous demandera la permission d'ajouter une nouvelle commande slash, /vandelay, et une fois autorisé, il devrait être prêt à être utilisé immédiatement dans Slack.

Si vous êtes intéressé par les détails techniques de son fonctionnement, continuez à lire ! Sinon, vous avez réussi à battre le temps de lecture estimé pour cet article. Félicitations !

![Image](https://cdn-media-1.freecodecamp.org/images/1*UHa3mQHcgfao8vYc7MThUw.gif)

#### Traitement

J'ai initialement commencé avec 91 Go des neuf saisons de Seinfeld en qualité surprenante 720p. J'ai finalement obtenu 111 Go de GIFs animés, ce qui vous en dit long sur l'efficacité de ce format de fichier. Cette section explique comment je suis passé de l'un à l'autre.

Les fichiers étaient dans des conteneurs MKV, donc j'ai pu utiliser [MKVToolNix](https://mkvtoolnix.download/) pour extraire les sous-titres. Vous pouvez utiliser mkvinfo pour lister les différentes pistes de segments :

```
mkvinfo Seinfeld.S01E01.The.Seinfeld.Chronicles.mkv
```

C'est un peu difficile à lire, mais la piste qui nous intéresse est la piste numéro 3, la première piste de sous-titres. Après avoir noté l'ID de la piste (2), nous pouvons extraire les sous-titres dans un fichier SRT comme ceci :

```
mkvextract tracks Seinfeld.S01E01.The.Seinfeld.Chronicles.mkv 2:S01E01.srt
```

Le format SRT est assez simple. Il contient un compteur, l'heure de début, l'heure de fin et le texte du sous-titre. En utilisant un analyseur comme [subtitles-parser](https://www.npmjs.com/package/subtitles-parser), nous pouvons facilement itérer sur les sous-titres.

L'étape suivante consiste à parcourir chaque sous-titre et à extraire cette plage de temps du MKV dans un GIF animé. Il y a un [excellent article sur l'utilisation de ffmpeg pour encoder des GIF de haute qualité](http://blog.pkh.me/p/21-high-quality-gif-with-ffmpeg.html), mais si vous ne voulez pas le lire maintenant, le truc est d'extraire une palette spécialisée de la section de la vidéo qui vous intéresse, puis d'utiliser celle-ci pour encoder le GIF.

Voici un script que j'ai adapté pour les besoins de cette étape de traitement :

320 fait référence au nombre de pixels de large que le GIF résultant aura. Vous remarquerez que, au lieu de spécifier une heure de début et une heure de fin, je spécifie une durée. Bien que ffmpeg prétende supporter les heures de fin, quelle que soit la version que j'ai essayée, je n'ai pas réussi à ce qu'il extraie correctement la bonne plage, donc j'ai fini par calculer la durée en soustrayant l'heure de début de l'heure de fin et en utilisant l'époque unix comme ceci :

Après avoir appliqué le script gifenc.sh, nous obtenons un joli GIF animé de la plage extraite correcte comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*1rukLpm7GTaNxkunKTjiSg.gif)

Mais je voulais afficher le texte du sous-titre en bas du GIF et après avoir fouillé dans la documentation d'ImageMagick, j'ai trouvé ceci :

Ce n'est pas la solution la plus élégante, mais elle fait le travail. Notre gif final ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZTBtKosGpleB6sf_VVpvxA.gif)

Maintenant, il suffit de faire cela environ 104 782 fois de plus et vous avez terminé. Le traitement d'un épisode entier avec ffmpeg et ImageMagick a pris environ 30 minutes sur mon Macbook Pro haut de gamme en 2011. C'est la partie de l'histoire où j'aimerais vous dire que j'ai réussi à utiliser Amazon Elastic Transcoder ou que j'ai fait un travail hadoop pour distribuer la charge à tous les ordinateurs de ma maison, mais en réalité, ce que j'ai fait, c'est mettre tout cela sur mon [serveur OVH budget reconditionné](https://www.soyoustart.com/) et le laisser tourner pendant 5 jours tout en continuant à vivre ma vie.

Une fois qu'il a terminé l'encodage de tous les GIF, j'ai simplement laissé Apache les servir statiquement avec un long en-tête Expires et mis Cloudflare devant tout le domaine. Seul le temps nous dira si cela résistera réellement aux demandes de trafic.

#### Recherche

J'ai installé Elasticsearch et indexé le contenu des fichiers SRT. C'est là que j'ai rencontré quelques obstacles non techniques : Dans la saison 6, les épisodes 14 et 15 sont un épisode d'une heure appelé Highlights of a Hundred où Jerry Seinfeld vous montre un tas de vieux clips des épisodes précédents. Et dans le dernier épisode de Seinfeld, Saison 9, Épisode 23, ils font un tas de flashbacks aux épisodes précédents. Ces deux épisodes étaient régulièrement retournés dans les résultats de recherche, donc je les ai simplement exclus de la requête de recherche. Il y a probablement une meilleure façon de simplement baisser la qualité des scores de ces épisodes, mais la documentation pour le faire dans Elasticsearch est aussi facile à lire que la documentation ImageMagick mentionnée ci-dessus. Et à la fin de la journée, personne ne veut voir des clips de l'un ou l'autre de ces deux épisodes. Désolé, Larry David, le dernier épisode était terrible.

#### Commande Slash

La dernière étape consistait simplement à tout regrouper avec une commande slash Slack, qui est juste une simple application Express qui agit comme un client pour l'instance Elasticsearch. Il y a un peu d'OAuth pour empaqueter la commande en tant qu'application Slack et gérer le bouton Ajouter à Slack, mais je n'ai pas vraiment besoin de vérifier l'authentification lorsque les requêtes arrivent, donc je ne sauvegarde pas les jetons d'autorisation. Le code du serveur est disponible ici : [vandelayindustries-slack-server](https://github.com/bertrandom/vandelayindustries-slack-server).

C'est tout ! J'espère que ce compte rendu technique aidera la prochaine personne qui souhaite extraire des GIF d'une série télévisée entière pour peu ou pas de raison réelle.

![Image](https://cdn-media-1.freecodecamp.org/images/1*gQJzoNu5gkQxG9EOBDiF3w.gif)