---
title: Formats vidéo pour le web, un guide court pour vous aider à choisir
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T08:45:55.000Z'
originalURL: https://freecodecamp.org/news/video-formats-for-the-web
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/photo-1440404653325-ab127d49abc1-1.jpg
tags:
- name: 'tech '
  slug: tech
- name: video
  slug: video
- name: Web Development
  slug: web-development
seo_title: Formats vidéo pour le web, un guide court pour vous aider à choisir
seo_desc: 'By Anton Garcia Diaz

  Video in the web will be on the rise for long. While embedding Instagram and Youtube
  videos is simple, there are more and more situations -like many ecommerce use cases-
  demanding a custom approach to video delivery.

  When it come...'
---

Par Anton Garcia Diaz

La vidéo sur le web sera en hausse pendant longtemps. Bien que l'intégration de vidéos Instagram et YouTube soit simple, il existe de plus en plus de situations - comme de nombreux cas d'utilisation dans le e-commerce - nécessitant une approche personnalisée pour la diffusion de vidéos.

Lorsqu'il s'agit de mettre en place un pipeline de traitement et de diffusion vidéo, la première décision à prendre concerne les formats vidéo à servir. Des aspects comme l'UX, le support (navigateurs et systèmes), l'efficacité de la compression ou la vitesse de codage sont susceptibles d'être pertinents pour ce choix.

Basé sur mon [expérience en optimisation des médias pour les entreprises web](https://abraia.me/), j'essaie de mettre en évidence ici les principaux aspects à considérer. Si vous cherchez une option simple de transcodage et d'optimisation utilisant ffmpeg, vous pouvez également consulter [cet article](https://medium.com/abraia/video-transcoding-and-optimization-for-web-with-ffmpeg-made-easy-511635214df0).

## Conteneurs et codecs

Contrairement aux [formats d'image](https://www.freecodecamp.org/news/best-image-format-for-web-in-2019-jpeg-webp-heic-avif-41ba0c1b2789/) habituels, il est vraiment important de connaître la différence entre le conteneur et la norme de codage. L'extension du fichier nous indique quel conteneur est utilisé, mais pas quel codec est utilisé. Et la norme suivie pour encoder le clip déterminera si elle est supportée par le navigateur ou le système.

Par exemple, bien que le format vidéo universellement supporté pour le web utilise un conteneur mp4 et la norme H264 pour l'encodage, tous les fichiers mp4 ne sont pas universellement supportés puisqu'ils peuvent être codés sous une norme différente, comme H265.

Cela devient même un peu plus complexe avec le débit binaire adaptatif (ABR), qui offre la meilleure façon d'être réactif aux capacités du réseau et de l'appareil de l'utilisateur.

Examinons les principales combinaisons de conteneurs et de normes de codage et de diffusion, ainsi que les différences entre elles en termes de support, d'efficacité de compression, de vitesse d'encodage et d'expérience utilisateur.

## Vidéo progressive

### H264/AVC

Le format roi pour la vidéo présente un conteneur mp4 avec un encodage H264/AVC. Parfois, vous le trouverez dans un conteneur m4v (format par défaut dans Handbrake), un dérivé mp4 développé par Apple pour les vidéos H264 avec protection DRM.

Tous les navigateurs et systèmes - ainsi que les applications natives sur iOS et Android - supportent ce format. C'est le choix sûr pour éviter les problèmes de compatibilité.

De plus, presque tous les appareils, des ordinateurs de bureau aux mobiles, disposent d'un support pour l'accélération matérielle pour H264. Il est rapide à encoder et à décoder.

En somme, l'encodage et la diffusion de ce format sont vraiment faciles. Comme pour les images, vous pouvez simplement insérer le lien vers la vidéo en utilisant HTML5 et cela fonctionnera avec n'importe quel navigateur.

Les problèmes peuvent apparaître pour des résolutions supérieures à VGA, une bonne qualité visuelle - débits binaires d'environ 2000 kbps et plus - et une durée de plusieurs secondes. Lorsqu'elle est visionnée via un réseau mobile - dans de nombreuses régions également dans les connexions domestiques pendant les heures de pointe - elle peut subir des interruptions et des rebuffers. L'alternative de réduire la qualité produira des artefacts comme le flou, le moustiquage ou le blocage.

### H265/HEVC

En utilisant le même conteneur et l'encodage H265/HEVC, nous trouvons un format vidéo puissant qui offre une efficacité de compression beaucoup plus élevée ([environ 50% plus léger](https://www.bbc.co.uk/rd/blog/2016-01-h-dot-265-slash-hevc-vs-h-dot-264-slash-avc-50-percent-bit-rate-savings-verified)) et beaucoup moins de risques d'artefacts autres que le flou. Le problème de ce format est que le support est limité aux appareils Apple, qui incluent les royalties dans leur prix. Presque seulement Safari et les applications iOS pourront l'utiliser. Si vous avez beaucoup d'utilisateurs d'iPhone ou de Mac, vous pouvez l'inclure avec un fallback vers H264. L'expérience pour eux sera meilleure.

Même avec l'accélération matérielle - disponible presque uniquement sur les appareils Apple - la complexité plus élevée de ce format signifie que l'encodage est significativement plus lent, donc la production des variantes pour la diffusion prend plus de calcul et plus de temps.

### VP9

Il s'agit de la réponse open source et sans royalties de Google. Au lieu de mp4, il utilise des conteneurs webm, essentiellement un conteneur mkv mais définissant la norme de codage à VP8 ou VP9. Il [apporte des bénéfices similaires à H265](https://medium.com/netflix-techblog/a-large-scale-comparison-of-x264-x265-and-libvpx-a-sneak-peek-2e81e88f8b0f), peut-être un peu moins efficace mais toujours beaucoup plus comparé à H264. Encore une fois, il permet de réduire le poids avec beaucoup moins de risques d'artefacts autres que le flou. La vitesse d'encodage est similaire à H265, qui est lente. La vitesse d'encodage peut être quelque chose à garder à l'esprit, surtout dans un pipeline de transcodage interne.

Remarquez que bien qu'une version précédente (VP8) existe avec le même support, nous ne la recommandons pas du tout, car elle n'ajoute aucun bénéfice à H264, qui est déjà universellement supporté. L'utilisation de webm n'est justifiée qu'avec l'encodage VP9.

Bien sûr, le support pour webm est limité au monde Google. Cela signifie Chrome et Android. Encore une fois, nous aurons besoin d'un fallback vers H264.

### AV1

Une première version stable de cette norme a été publiée en mars 2018, avec des mappages pour les conteneurs MP4 et MKV. Elle offre des gains similaires ou légèrement supérieurs en efficacité de compression par rapport à H265, tout en étant libre de licence. Les [dernières implémentations ont également amélioré la vitesse de décodage par rapport à H265](https://www.bbc.co.uk/rd/blog/2019-05-av1-codec-streaming-processing-hevc-vvc), faisant des vidéos AV1 une alternative convaincante pour la diffusion web.

Les partenaires impliqués dans l'Alliance for Open Media qui a créé le format font valoir un support généralisé dans un avenir proche. Il promet de balayer tous les autres formats existants.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/imaxe.png)
_Partenaires de l'Alliance for Open Media derrière AV1_

Cependant, l'implémentation actuellement disponible doit encore être considérée comme expérimentale et son goulot d'étranglement est toujours la vitesse d'encodage. Le manque d'accélération matérielle pour cette opération est clairement un problème, avec les premières solutions attendues pour la fin de l'année.

### VVC

Le comité responsable de H264 AVC et H265 HEVC a accéléré une nouvelle norme, avec une sortie prévue pour 2020. Des tests préliminaires sur les approches actuellement considérées ont montré des gains remarquables par rapport à H265 et AV1. Je l'inclus ici comme une notice futuriste, juste pour montrer que la course au codage vidéo semble loin d'être terminée.

## Débit binaire adaptatif (ABR)

Il s'agit d'une alternative très intéressante à tout format progressif. Il repose sur un protocole de communication de streaming média basé sur HTTP. Dans cette approche, les vidéos sont diffusées sous forme de liste de lecture principale. La liste de lecture offre une représentation ou une échelle, avec différentes options de résolution et de débit binaire qui s'adaptent à différentes tailles de viewport, bandes passantes du réseau et capacités des appareils.

De plus, les vidéos sont divisées en morceaux ou _chunks_ afin que le client puisse passer d'un niveau de qualité à un autre. Il est capable de s'adapter aux conditions de l'utilisateur, notamment à la vitesse du réseau mais aussi à la taille du viewport - comme le passage en plein écran.

L'ABR apporte un grand avantage pour optimiser l'UX pour les appareils mobiles, évitant les interruptions ou les événements de rebuffering sous les réseaux mobiles. Si vous cherchez un comportement vraiment réactif, c'est clairement l'approche à adopter. Il existe deux normes principales, HLS et MPEG-DASH.

Bien qu'il existe une croyance répandue que l'ABR n'a de sens que pour des vidéos assez longues, selon mon expérience, de nombreuses situations avec des clips assez courts peuvent également bénéficier de cette approche.

### HLS

Développé par Apple, ce protocole ABR repose sur différentes renditions divisées en chunks au format mp4. À l'origine avec H264, il supporte également H265 maintenant. Cependant, en tant que compromis, nous recommanderions de rester avec l'encodage H264 avec HLS car il offre une bien meilleure compatibilité avec une variété de cas clients.

Un grand point de cette norme est le support dans les appareils Apple récents. Pour les clients autres que Safari ou les applications natives iOS, vous aurez besoin d'un lecteur. Mais ce n'est pas un gros problème puisque de bonnes options open source comme videojs sont disponibles. Bien sûr, vous aurez besoin de quelques efforts pour le personnaliser et le faire fonctionner dans votre front-end. Il existe également d'excellents services de transcodage et de diffusion faisant tout ce travail pour vous.

Puisque chaque rendition doit être encodée à un débit binaire constant, je recommande de combiner HLS avec un encodage par titre. C'est-à-dire, sélectionner le débit binaire de la rendition en fonction du contenu de la vidéo.

### MPEG-DASH

Il s'agit d'un protocole ABR agnostique en termes de codec, capable de fonctionner également avec l'encodage VP9 en plus de H264 et H265, ou même de nouvelles alternatives comme AV1. L'inconvénient est sa relative jeunesse, ce qui signifie qu'il bénéficie de beaucoup moins de support que HLS. C'est pourquoi nous ne le recommandons pas encore pour la plupart des entreprises web - même les grandes boutiques de e-commerce.

## Résumé

Après des années de prédominance de la compression H264 AVC, de nouvelles approches animent la scène. La course aux tailles et résolutions d'affichage alimente le développement de nouveaux formats capables de diffuser un contenu plus important dans la même bande passante.

VP9 dans webm offre un gain significatif en efficacité de compression (environ 30%), est libre de royalties et est supporté par les solutions Google (Chrome, Android). Allant beaucoup plus loin, H265/HEVC a atteint une qualité subjective comparable ou meilleure à la moitié du débit binaire par rapport à H264. Puisque aucun d'entre eux ne dispose d'un support universel, H264 sera encore nécessaire, au moins comme solution de repli.

Le débit binaire adaptatif est une alternative convaincante, offrant une expérience utilisateur inégalée. À cet égard, HLS bénéficie d'un large support grâce à des lecteurs open source. C'est probablement la meilleure option pour un web de taille moyenne. La complexité ajoutée par la nécessité d'un lecteur est assez atténuée par la disponibilité d'initiatives open source comme videojs pour les solutions internes, mais aussi par des services tiers pour faire le travail à des prix compétitifs. Si vous passez par cette dernière voie, assurez-vous de demander un [encodage par titre](https://abraia.me/docs/video-optimization/#per-title-encoding).