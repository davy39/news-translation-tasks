---
title: Comment utiliser Gource pour montrer la chronologie de votre projet
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T23:17:24.000Z'
originalURL: https://freecodecamp.org/news/using-gource-to-show-your-project-timeline
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/gource.jpg
tags:
- name: Git
  slug: git
- name: gource
  slug: gource
- name: terminal
  slug: terminal
seo_title: Comment utiliser Gource pour montrer la chronologie de votre projet
seo_desc: 'By Leonardo Faria

  The first time I heard about Gource was in 2013. At the time I watched this cool
  video showing Ruby on Rails source code evolution:

  https://www.youtube.com/watch?v=r0ji8FDNTj0&feature=emb_title

  At Thinkific we have (almost) monthly ...'
---

Par Leonardo Faria

La première fois que j'ai entendu parler de [Gource](https://github.com/acaudwell/Gource) était [en 2013](https://leonardofaria.net/2013/01/20/gource-uma-forma-estilosa-de-ver-logs-do-seu-controle-de-versao/). À l'époque, j'ai regardé cette vidéo cool montrant l'évolution du code source de Ruby on Rails :

%[https://www.youtube.com/watch?v=r0ji8FDNTj0&feature=emb_title]

Chez [Thinkific](https://www.thinkific.com/), nous avons (presque) chaque mois des réunions générales sur les produits, que nous utilisons pour communiquer les décisions concernant les produits et maintenir toutes les équipes produit (Designers, Ingénieurs, Chefs de produit et QA) sur la même longueur d'onde.

Nous aimons commencer la présentation avec une vidéo Gource de nos projets. Voici comment nous procédons :

`gource --hide dirnames,filenames --seconds-per-day 0.1 --auto-skip-seconds 1 -1280x720 -o - | ffmpeg -y -r 60 -f image2pipe -vcodec ppm -i - -vcodec libx264 -preset ultrafast -pix_fmt yuv420p -crf 1 -threads 0 -bf 0 gource.mp4`

Le [README](https://github.com/acaudwell/Gource/blob/master/README) de Gource contient toutes les options que vous pouvez personnaliser dans votre vidéo. Associé à [ffmpeg](https://www.ffmpeg.org/), nous créons un fichier mp4 qui peut être utilisé dans Google Slides ou YouTube. Voici le résultat de l'exemple ci-dessus :

%[https://youtu.be/hYvWaA5cCJg]

_Aussi publié sur [mon blog](http://bit.ly/2FWop4N). Si vous aimez ce contenu, suivez-moi sur [Twitter](https://twitter.com/leozera) et [GitHub](https://github.com/leonardofaria)._

Au fait, Thinkific [recrute](https://bit.ly/thnk-senior-front-end-eng) [pour](https://bit.ly/thnk-senior-full-stack-eng) [plusieurs postes](https://www.thinkific.com/careers/) si vous êtes intéressé.