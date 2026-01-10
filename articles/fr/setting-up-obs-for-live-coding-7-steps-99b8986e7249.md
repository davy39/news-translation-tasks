---
title: Configurer OBS pour le codage en direct en 7 étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-01T08:28:01.000Z'
originalURL: https://freecodecamp.org/news/setting-up-obs-for-live-coding-7-steps-99b8986e7249
coverImage: https://cdn-media-1.freecodecamp.org/images/1*aIrejV0NE5wBP8fd27Kmgw.jpeg
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: live streaming
  slug: live-streaming
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Configurer OBS pour le codage en direct en 7 étapes
seo_desc: 'By Wesley McCann

  Twitch TV is a popular live-streaming service. You traditionally used Twitch to
  stream yourself playing video games, but recently Twitch has started encouraging
  people to stream themselves coding.

  While typical video game live stream...'
---

Par Wesley McCann

Twitch TV est un service populaire de diffusion en direct. Traditionnellement, vous utilisiez Twitch pour diffuser vos parties de jeux vidéo, mais récemment, Twitch a commencé à encourager les gens à diffuser leurs sessions de codage.

Bien que les configurations typiques de diffusion en direct de jeux vidéo fonctionnent pour le codage en direct, elles sont excessives. Lors de la diffusion de codage en direct, vous pouvez vous en sortir avec des paramètres significativement plus bas, ce qui facilite grandement la tâche des personnes avec une connexion plus lente pour regarder votre diffusion en direct.

Cet article vous montrera comment configurer le populaire OBS (Open Broadcast Software) pour maintenir la qualité de votre diffusion tout en minimisant les exigences de bande passante pour vos spectateurs.

**Note : Afin de garder cet article raisonnablement court, nous ne montrerons que des captures d'écran de la version Windows d'OBS. Notez que la plupart des étapes devraient être presque identiques sur Mac et Linux.**

#### Premières étapes

1. Vous devrez télécharger et installer OBS pour votre plateforme. Le site web d'OBS se trouve [ici](https://obsproject.com/). Je préfère OBS Studio (qui est la seule option pour les utilisateurs non-Windows), car c'est la version la plus récente actuellement en développement et elle semble mieux utiliser la bande passante.
2. Une fois installé, vous voudrez commencer par configurer la scène. Tout d'abord, vous voudrez vous assurer qu'il y a une scène dans la boîte la plus à gauche. Cela devrait être là par défaut, cependant, si ce n'est pas le cas, faites un clic droit dans la boîte et sélectionnez « Add -> Scene ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*V1PhVwV1fbGCUVv4HWqqTg.gif)
_Ajout d'une nouvelle scène_

3. Ensuite, vous voudrez capturer tout votre écran ou juste une fenêtre. Le choix vous appartient. Personnellement, j'aime capturer tout mon écran, mais je vais vous montrer les deux options ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XuZv5YQVXXMG0Dt_abCW0Q.gif)
_Ajout d'une capture d'affichage_

4. Une fois cela configuré, vous voudrez faire fonctionner votre microphone pour pouvoir communiquer avec votre audience. Sur Windows, vous voudrez cliquer sur le bouton des paramètres > onglet audio. Une fois là, vous voudrez trouver « Mic/Auxiliary Audio Device » et utiliser le menu déroulant pour sélectionner votre périphérique d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*53JeBiTY7JVxgziTiCue3g.gif)
_Ajout d'un périphérique de capture d'entrée_

5. Maintenant que vous avez configuré la scène pour capturer votre affichage et votre microphone, vous devez configurer un service de diffusion. Pour ce faire, ouvrez votre **paramètres > Stream**. Une fois là, sélectionnez :  
**Type de Stream** : Services de diffusion  
**Service** : Twitch  
**Serveur** : Choisissez le serveur le plus proche de vous  
**Clé de Stream** : La clé de stream fournie par Twitch

![Image](https://cdn-media-1.freecodecamp.org/images/1*YTlL2Qff7PsgRjRdbf2SmA.gif)
_Configuration de votre service de diffusion_

6. Ensuite, vous voudrez changer les paramètres de sortie. Vous pouvez le faire en allant dans **paramètres > sortie**. À partir de là, vous voudrez sélectionner :  
**Mode de sortie** : Avancé  
Être sur l'onglet « Streaming »  
**Bitrate** : Pas plus haut que 1200. Essayez de correspondre à votre vitesse de téléchargement. Par exemple, ma vitesse de téléchargement est généralement entre 800 Kbps et 900 Kbps. J'ai réglé mon bitrate à 700.  
**Intervalle de Keyframe** : 2 secondes  
**Utilisateur** CBR : Cocher  
**Utilisation du CPU** : Veryfast. C'est la valeur recommandée si vous n'êtes pas sûr de votre matériel.  
_Tous les autres paramètres, laissez-les par défaut._

![Image](https://cdn-media-1.freecodecamp.org/images/1*f9LKSFdPtYDre9ldW_BufQ.gif)
_Configuration de vos paramètres de sortie_

7. Enfin, vous voudrez vérifier les images par seconde (FPS) de votre diffusion. Ne pas configurer correctement vos FPS est probablement la plus grande façon de gaspiller de la bande passante lors du codage en direct. Naviguez vers paramètres > vidéo. Une fois là, vous voudrez cliquer sur le menu déroulant « Common FPS Values » et sélectionner « Integer FPS Values ». Dans la boîte d'entrée qui apparaît, changez le 30 en 15. 15 FPS devraient suffire pour le codage en direct.

![Image](https://cdn-media-1.freecodecamp.org/images/1*hP9mN29TanVa4JGvMnpVwg.gif)
_Réglage de vos FPS_

Cela devrait être tout ce que vous devez faire pour configurer OBS et commencer le codage en direct !

Il y a quelques autres choses que vous pourriez vouloir faire, comme capturer l'audio de sortie pour jouer de la musique en diffusion. Je vais écrire un autre article à ce sujet très bientôt avec des GIF spécifiques à Windows et Mac.

Si vous avez des questions, n'hésitez pas à [me contacter sur Gitter](http://gitter.im/septimus) ou à tweeter à [@septimus98](https://twitter.com/septimus98).