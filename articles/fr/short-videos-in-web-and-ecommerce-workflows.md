---
title: Comment déployer un pipeline complet de publication vidéo pour le web et l'ecommerce
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-13T08:00:00.000Z'
originalURL: https://freecodecamp.org/news/short-videos-in-web-and-ecommerce-workflows
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Video-Publishing-Demo.png
tags:
- name: ecommerce
  slug: ecommerce
- name: hls
  slug: hls
- name: publishing
  slug: publishing
- name: technology
  slug: technology
- name: Transcoding
  slug: transcoding
- name: video
  slug: video
- name: Video.js
  slug: video-js
- name: VideoJS
  slug: videojs
seo_title: Comment déployer un pipeline complet de publication vidéo pour le web et
  l'ecommerce
seo_desc: 'By Anton Garcia Diaz

  From ffmpeg and cloud video transcoding to HLS, delivery, players, Video.js, and
  analytics.

  After the conquest of social networks, video is spreading through web businesses.
  As a media consultant working for several of the larges...'
---

Par Anton Garcia Diaz

_De ffmpeg et du transcodage vidéo cloud à HLS, livraison, lecteurs, Video.js et analytique._

Après la conquête des réseaux sociaux, la vidéo se répand à travers les entreprises web. En tant que consultant média travaillant pour plusieurs des [plus grands sites d'ecommerce de mode](https://www.similarweb.com/top-websites/category/lifestyle/fashion-and-apparel) au monde, je peux affirmer sans risque que la tendance de la vidéo partout est pratiquement inarrêtable. 

Dans cet article, je passe en revue les principaux aspects à considérer lors de la publication de vidéos au format court dans un flux de travail web. Je commente les ressources open source qui rendent possible une solution interne pour chaque étape, comme ffmpeg ou Video.js. De plus, j'utilise un exemple avec [la démonstration d'optimisation et de publication vidéo d'Abraia](https://abraia.me/video/) - spécialement conçue pour les vidéos courtes destinées à l'ecommerce de mode. 

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Workflow/index.html]

Cela donne un accès complet aux ressources créées : chunks, playlists et code html pour le lecteur vidéo. Cela apporte des informations rapides sur le fonctionnement interne d'un pipeline complet. 

Le contenu devrait être utile soit pour poursuivre un pipeline de traitement et de publication interne, soit pour trouver la meilleure combinaison de services. 

## Qualité de l'expérience (QoE) et autres préoccupations liées aux affaires.

Il existe deux préoccupations principales qui sont étroitement liées. La crainte de surcharger la bande passante des utilisateurs, ce qui nuit à l'UX et à l'engagement, et la crainte de fournir une mauvaise qualité visuelle, ce qui pourrait potentiellement nuire à l'image de la marque. 

L'équilibre entre ces deux facteurs antagonistes est ce qui détermine la QoE. Maintenir une **QoE élevée** nécessite de fournir presque la **meilleure qualité possible, sans effets de rebuffering ou de blocage** ou des baisses notables de la vitesse de la page. 

Bien sûr, il y a d'autres problèmes qui comptent

* la personnalisation de l'expérience de visualisation pour correspondre à la marque de l'entreprise
* l'augmentation des coûts de livraison de contenu à bande passante plus élevée 
* et le fardeau supplémentaire en termes de devops

...pour n'en nommer que quelques-uns.

## Un premier choix : progressif vs débit binaire adaptatif (ABR).

En ce qui concerne la [sélection du format vidéo](https://www.freecodecamp.org/news/video-formats-for-the-web/), il existe deux options principales avec des implications importantes : la vidéo progressive et l'ABR.

Les vidéos progressives peuvent être livrées et consommées comme des images, en utilisant un simple code HTML5. De plus, les vidéos mp4 progressives avec un encodage H264 bénéficient d'un support universel sur les navigateurs et les systèmes. Elles sont donc l'approche la plus simple.

Cependant, dans l'éventualité probable où la QoE est une préoccupation majeure, nous devrions opter pour l'ABR. Plus spécifiquement pour HLS - à nouveau avec un encodage H264 - qui est une option largement supportée. 

Avec **HLS**, nous pourrons, dans la plupart des cas, maintenir les **bits par seconde - le débit binaire - de la vidéo dans les limites de la capacité de connexion**. Cela évite le rebuffering, le blocage ou le blocage d'autres contenus. Dans HLS, la vidéo est disponible à différents débits binaires et est divisée en morceaux. Cela permet au client de demander la meilleure qualité abordable, en fonction de la vitesse du réseau à tout moment. Le seul inconvénient est que nous devrons utiliser un lecteur dans notre front-end (basiquement un morceau de JavaScript). Dans les applications, c'est plus facile car iOS et Android disposent d'un support natif pour le protocole. 

## Le pipeline et le flux de travail

Cela dit, voyons ce qu'implique un pipeline d'optimisation et de livraison vidéo pour le web. Le pipeline est censé traiter une vidéo maître ou vierge de haute qualité et la rendre adaptée au web. Il est également censé répondre aux exigences de la marque en matière de visualisation et intégrer les événements vidéo dans l'analytique du site. 

En somme, notre pipeline devrait aborder les problèmes suivants :

* Gestion de contenu
* Transcodage et optimisation
* Livraison
* Visualisation
* Analytique

En fin de compte, le pipeline devrait permettre un flux de travail similaire à celui des plateformes de vidéo sociales - où vous téléchargez une vidéo et obtenez un [lien comme celui-ci](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Video-Freecodecamp/index.html) pour l'intégrer ou le partager ailleurs - mais sous toutes les exigences personnalisées de notre entreprise.

Pour garder cet article court et ciblé, je vais sauter la question de la gestion de contenu, qui est essentiellement la manière dont nous gérons toutes les ressources, y compris les flux de travail collaboratifs d'édition et d'approbation des médias. Ensuite, je passe en revue les principaux ingrédients d'optimisation et de livraison trouvés dans un pipeline de publication vidéo.

## Transcodage et optimisation

Pour que les vidéos progressives soient réactives, nous pouvons créer des versions avec différentes résolutions et qualités à consommer en fonction des points de rupture, similaires aux images. 

Dans un schéma interne, cette opération peut être [facilement accomplie avec ffmpeg](https://medium.com/abraia/video-transcoding-and-optimization-for-web-with-ffmpeg-made-easy-511635214df0). C'est un outil open source qui effectue le redimensionnement, la compression et de nombreuses autres opérations très efficacement. Par exemple, pour mettre à l'échelle une vidéo 4K en fullHD avec une bonne qualité visuelle, vous pouvez simplement utiliser :

```
ffmpeg -y -i input.mp4 -vf scale=1920:-2 -c:v libx264 -crf 22 -profile:v high -pix_fmt yuv420p -color_primaries 1 -color_trc 1 -colorspace 1 -movflags +faststart -an output.mp4
```

Alternativement, avec une plateforme cloud, l'opération devrait être un jeu d'enfant, bien que dans de nombreux cas nous perdions le contrôle effectif des paramètres de qualité et des points de rupture possibles.

L'encodage pour **HLS** est un peu plus délicat. Tout d'abord, **nous devons définir une échelle de codage**. Chaque étape de l'échelle présentera un débit binaire différent, d'un maximum à un minimum. Ils définissent respectivement la qualité maximale et minimale. 

Pour chaque débit binaire dans l'échelle, nous devons également définir la résolution, à nouveau d'un maximum à un minimum. Idéalement, nous devrions utiliser des débits binaires spécifiquement ajustés au contenu vidéo pour optimiser l'utilisation de la bande passante. Lorsque cela est fait automatiquement, **sur une base par vidéo**, cela s'appelle **l'encodage par titre**. 

Nous devons coder la vidéo avec les résolutions et les débits binaires définis, puis couper chaque rendu en morceaux. Nous devons également décider de la durée du morceau. C'est-à-dire, à quelle fréquence HLS renégocie la qualité à demander, en fonction de la vitesse actuelle du réseau. Nous pouvons effectuer tout l'encodage avec ffmpeg ou avec un service cloud.

Regardons les fichiers générés pour notre exemple. Nous avons un dossier contenant tous les morceaux (extension .ts), et les playlists (extension .m3u8). 

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-7.png)

Les playlists contiennent toutes les informations sur les rendus disponibles. Ensuite, nous pouvons voir le contenu de la playlist maître : l'échelle - débits binaires et résolutions - et le chemin relatif vers les rendus.

```
#EXTM3U
#EXT-X-VERSION:3
#EXT-X-STREAM-INF:BANDWIDTH=3374012,RESOLUTION=1920x1080
1080p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1836580,RESOLUTION=1280x720
720p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=1002050,RESOLUTION=856x480
480p.m3u8
#EXT-X-STREAM-INF:BANDWIDTH=649329,RESOLUTION=640x360
360p.m3u8
```

C'est-à-dire, pour chaque rendu, nous avons une playlist supplémentaire contenant les informations sur la durée et le chemin vers les morceaux correspondants. Nous avons également besoin d'une affiche à utiliser comme miniature et à couvrir en cas de connexion très lente ou de problèmes de compatibilité HLS. Dans notre exemple, toutes les ressources sont dans le même dossier, donc le chemin vers chaque ressource est simplement le nom.

## Livraison

**Les vidéos doivent être livrées via un CDN**. Si vous faites un mauvais transcodage, de nombreux utilisateurs peuvent souffrir de chargements de pages lents. Mais au moins, si vous utilisez un CDN, vous ne ferez pas tomber votre site parce que le serveur est incapable de gérer la charge. J'ai vu de grands sites qui ont plus que doublé leur trafic de pointe le jour où ils ont décidé d'utiliser des vidéos sur leur page d'accueil. Donc, les vidéos, qu'elles soient progressives ou HLS, doivent être livrées en tant que fichiers statiques mis en cache et livrés par un CDN.

Si vous utilisez une plateforme cloud pour la publication vidéo, vous devriez être couvert. Toute plateforme décente offre la livraison vidéo via au moins un CDN. Si vous avez besoin d'une couverture dans certains pays comme la Chine, vous devez examiner chaque plateforme spécifique et le CDN utilisé, car certains d'entre eux ne fonctionnent pas là-bas.

## Visualisation

Alors que pour les vidéos progressives, HTML5 suffit pour garantir la visualisation, dans le cas de HLS, nous avons besoin d'un **lecteur JavaScript avec support HLS**. 

Il existe de nombreuses options commerciales, mais il existe également des alternatives open source de très haute qualité. Un bon exemple est **Video.js**. Il bénéficie d'un large support parmi les navigateurs, limité uniquement par la dépendance à l'API [Media Source Extensions](https://caniuse.com/#search=media%20source). Il offre un haut degré de personnalisation en utilisant des skins et une configuration flexible, permettant par exemple d'utiliser la lecture automatique ou différents contrôles vidéo.

Le lecteur peut être inséré dans le code de la page, ou il peut être dans un fichier html statique qui est intégré en tant qu'iframe. 

Revenons à notre exemple, lorsque nous publions la vidéo, nous créons une [ressource html](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Tests/PexelsVideos2795392/index.html) qui contient un lecteur Video.js avec les paramètres par défaut. L'URL du contenu doit pointer vers la playlist maître et la miniature vers l'image de l'affiche extraite de la vidéo.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-3.png)

Dans ce cas, la ressource html ajoute également **la compatibilité oembed**. En plus d'un accès direct dans le navigateur à cet html - ou à un autre dans lequel nous copions/collons le code du lecteur - pour lire [la vidéo](https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Tests/PexelsVideos2795392/index.html), nous pouvons l'intégrer dans un système de gestion de contenu (CMS). Par exemple, lors de la rédaction de cet article pour freeCodeCamp.

%[https://store.abraia.me/05bf471cbb3f9fa9ed785718e6f60e28/Short-Video-Publishing-Demo/Embedding/index.html]

## Analytique

Dans les vidéos courtes, les analyses typiques d'intérêt sont le **ratio d'utilisateurs qui jouent la vidéo, le ratio de ceux qui la regardent en entier, ou le ratio d'échecs de lecture**. 

Encore une fois, il existe de nombreuses options commerciales disponibles. Cependant, dans de nombreux cas, une option gratuite largement répandue comme Google Analytics (GA) peut suffire. Si nous utilisons Video.js, nous devons simplement instrumenter la ressource html avec GA, comme pour toute autre page web. Revenons à notre exemple, nous pouvons le voir dans le HTML éditable créé.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-5.png)

Pour suivre l'utilisation de la vidéo dans GA, nous devons simplement suivre les événements vidéo dans le lecteur. Par exemple :

```
    player.analytics({
      defaultVideoCategory: 'Video',
      events: [{
        name: 'play',
        label: 'Video-Freecodecamp',
        action: 'play',
      }, {
        name: 'pause',
        label: 'Video-Freecodecamp',
        action: 'pause',
      }, {
        name: 'ended',
        label: 'Video-Freecodecamp',
        action: 'ended',
      }, {
        name: 'error',
        label: 'Video-Freecodecamp',
        action: 'error',
      }]
    });
```

Ensuite, dans GA, nous pouvons voir les événements qui se produisent. Cette capture d'écran montre ma propre activité en temps réel - avec deux appareils et navigateurs - sur l'exemple vidéo créé pour cet article.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/imaxe-4.png)

## Résumé

J'ai passé en revue les principaux aspects impliqués dans un pipeline de publication vidéo, du transcodage à la livraison, la visualisation et l'analytique. J'ai fait référence à l'utilisation potentielle de différentes ressources, y compris deux initiatives open source majeures comme ffmpeg et Video.js.

J'ai soutenu l'explication avec un exemple simple utilisant notre [démonstration de publication vidéo](https://abraia.me/video/). Cela donne un accès complet aux ressources créées. Vous pourrez télécharger, modifier et utiliser les ressources dans vos tests. Vous pouvez l'utiliser librement pour répéter le processus avec une vidéo courte de votre choix. 

N'oubliez pas de commencer avec une vidéo de haute qualité. L'exemple ici est basé sur une vidéo 4k de 9 secondes de [@cottonbro](https://www.pexels.com/@cottonbro). Dans l'ensemble, je m'attends à ce que l'article apporte une vue d'ensemble de ce qu'implique un déploiement personnalisé pour la publication vidéo.