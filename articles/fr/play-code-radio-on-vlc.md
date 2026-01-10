---
title: Comment écouter Code Radio dans VLC Media Player en seulement 2 étapes simples
subtitle: ''
author: Akarsh Seggemu
co_authors: []
series: null
date: '2019-07-29T21:07:12.000Z'
originalURL: https://freecodecamp.org/news/play-code-radio-on-vlc
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca12d740569d1a4ca4d23.jpg
tags: []
seo_title: Comment écouter Code Radio dans VLC Media Player en seulement 2 étapes
  simples
seo_desc: "I enjoy listening to Code Radio while I'm working. The music helps me focus\
  \ and block out the noise of the surrounding office. \nBut when one of my co-workers\
  \ interrupts my flow to ask a question, I have to switch Code Radio off. \nIt's\
  \ kind of time co..."
---

J'aime écouter [Code Radio](https://coderadio.freecodecamp.org/) pendant que je travaille. La musique m'aide à me concentrer et à bloquer le bruit du bureau environnant. 

Mais quand un de mes collègues interrompt mon flux de travail pour poser une question, je dois éteindre Code Radio. 

C'est un peu chronophage de basculer vers le site de Code Radio pour mettre la musique en pause. Il faut trouver dans quel onglet Code Radio est en lecture pour pouvoir la mettre en pause.

Pour surmonter cette situation, j'ai commencé à ouvrir un navigateur séparé que j'utilisais uniquement pour écouter Code Radio. Cela m'a facilité la tâche puisque je pouvais simplement faire alt+tab vers l'icône de ce navigateur et appuyer sur la touche espace de Code Radio pour mettre la musique en pause.

Mais faire tourner un navigateur séparé uniquement pour écouter de la musique semblait drainer les ressources de mon ordinateur. Je pensais qu'il y aurait une meilleure solution, moins gourmande. 

Depuis que j'ai commencé à écouter [Code Radio](https://coderadio.freecodecamp.org/), j'avais largement abandonné Spotify et désinstallé l'application. Mais je me souvenais qu'à l'époque où j'utilisais Spotify, je pouvais utiliser les contrôles média de mon clavier pour mettre la musique en pause et la lire. Cela m'a donné une idée.

# Une solution plus élégante

Et si vous pouviez lire et mettre en pause Code Radio avec une seule touche de votre clavier - même si vous étiez dans votre terminal ou votre éditeur de code ?

Eh bien, vous ne pouvez pas faire cela avec une application de navigateur. Mais vous pouvez le faire avec une application native exécutée sur votre ordinateur. Et vous avez peut-être déjà cette application installée sur votre ordinateur. Elle s'appelle VLC, et c'est l'un des lecteurs multimédias les plus courants.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/IMG_20190726_173455644-1.jpg)
_boutons du lecteur multimédia sur mon clavier_

Pendant ma pause déjeuner, je continuais à réfléchir à la manière de faciliter l'écoute de la musique et d'avoir la possibilité de lire/mettre en pause la musique depuis mon clavier avec un seul clic, c'est-à-dire le bouton lecture/pause. J'ai donc recherché sur Internet et j'ai découvert que les lecteurs multimédias peuvent diffuser du contenu depuis n'importe quel réseau. 

[Cet article](https://www.vlchelp.com/access-media-upnp-dlna/) m'a aidé à comprendre comment diffuser du contenu depuis n'importe quel réseau dans VLC.

Afin d'avoir la flexibilité d'utiliser le bouton lecture/pause de mon clavier, je devais utiliser un lecteur multimédia. J'ai trouvé que le [lecteur multimédia VLC](https://www.videolan.org/vlc/index.html) est un lecteur multimédia fiable, disponible sur toutes les plateformes, open source et gratuit à télécharger.

Lors de ma première tentative, j'ai essayé d'ouvrir l'URL de la page web de Code Radio : _[https://radio.freecodecamp.org](https://radio.freecodecamp.org)_ dans le lecteur multimédia VLC.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.02.22.png)
_essayer d'ouvrir Code Radio depuis le lecteur multimédia VLC._

Et le lecteur multimédia VLC n'a pas pu le lire. J'ai essayé d'appuyer sur le bouton lecture plusieurs fois, mais cela n'a rien fait.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.02.40.png)
_impossible de lire sur le lecteur multimédia VLC_

Après plusieurs essais, j'ai découvert que le lecteur multimédia VLC nécessite un fichier au format musical (par exemple, mp3) et ne peut pas analyser le site web html :/. L'URL doit être l'emplacement du fichier au format musical.

Je suis donc retourné sur la page web de musique [Code Radio](https://coderadio.freecodecamp.org/) et j'ai inspecté la page web. J'ai recherché le mot-clé "_mp3_" et je n'ai rien trouvé. 

Ensuite, j'ai remarqué que je n'avais pas appuyé sur le bouton lecture pour que le site web demande la lecture du fichier mp3. Je l'ai simplement essayé (sur Firefox), et je n'ai pas eu à cliquer sur entrer pour trouver l'URL de ces mp3.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.01.05.png)
_emplacement du fichier mp3 via l'inspection de la page web de musique Code Radio_

Il y a deux options de [débit binaire](https://en.wikipedia.org/wiki/MP3#Bit_rate) disponibles sur la page web de musique [Code Radio](https://coderadio.freecodecamp.org/).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-29-at-22.05.28.png)
_plusieurs options de débit binaire mp3_

Les fichiers mp3 que j'ai vus dans l'inspection correspondent au bouton d'option de [débit binaire](https://www.freecodecamp.org/news/play-code-radio-on-vlc/Code%20Radio%20music%20website%20page).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-29-at-22.05.47.png)
_emplacements des fichiers mp3 avec leur débit binaire_

Les deux débits binaires et leurs noms de fichiers :

1. 64 kbps - low.mp3
2. 128 kbps - radio.mp3

Lors de ma deuxième tentative, j'ai utilisé l'URL de l'emplacement du fichier mp3 : [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326) que j'ai trouvé dans la page de musique Code Radio dans le lecteur multimédia VLC. Il a commencé à lire la musique :).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.03.35.png)
_lecteur multimédia VLC lisant le fichier mp3_

J'ai remarqué le numéro unique à la fin du fichier mp3 "[?1564340326](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3?1564340326)". Cela semble être des valeurs uniques créées par le serveur back-end. Lorsque j'ai ouvert le lecteur multimédia VLC le lendemain, il n'a pas pu lire la musique de Code Radio. J'ai essayé de supprimer les dernières valeurs à la fin du fichier mp3 et il a recommencé à lire :).

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.23.48.png)

## Étapes pour écouter la musique [Code Radio](https://coderadio.freecodecamp.org/) depuis [VLC media player](https://www.videolan.org/vlc/index.html)

**Étape 1.** Ouvrez le lecteur multimédia VLC. Ensuite, cliquez sur **Fichier**->**Ouvrir un réseau**

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-26-at-18.34.07.png)
_Ouvrir un réseau dans le lecteur multimédia VLC_

**Étape 2.** Dans le champ **URL**, collez cette URL : [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3). Ensuite, cliquez sur le bouton **Ouvrir**. 

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.25.43.png)
_ouverture de l'URL depuis le réseau dans le lecteur multimédia VLC_

Ensuite, le [lecteur multimédia VLC](https://www.videolan.org/vlc/index.html) ouvrira le réseau Code Radio et commencera à lire la musique.

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Screen-Shot-2019-07-28-at-21.23.48-1.png)

Remarque : Vous pouvez utiliser l'URL : [https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3](https://coderadio-admin.freecodecamp.org/radio/8010/radio.mp3) dans n'importe quel lecteur multimédia prenant en charge la diffusion via le réseau. J'ai essayé de lire avec Quick Time player et cela fonctionne !

### Autre option : Lecture via un fichier de liste de lecture,

Code Radio est alimenté par AzuraCast et son lecteur public dispose d'un lien "Download PLS" qui générera un fichier de liste de lecture PLS contenant tous les différents débits binaires. Le fichier de liste de lecture peut être lu dans le lecteur multimédia VLC et dans d'autres lecteurs. 

Vous pouvez ouvrir le fichier de liste de lecture - [https://coderadio-admin.freecodecamp.org/public/coderadio/playlist/pls](https://coderadio-admin.freecodecamp.org/public/coderadio/playlist/pls) dans le lecteur multimédia VLC et choisir le débit binaire pour commencer à lire la musique.

Profitez de l'écoute de la musique [Code Radio](https://coderadio.freecodecamp.org/).

Crédits : Je remercie [Quincy Larson](https://twitter.com/ossia), [Buster Neece](https://twitter.com/SlvrEagle23) et [Louis Tsai](https://twitter.com/louis993546) pour avoir relu cet article.