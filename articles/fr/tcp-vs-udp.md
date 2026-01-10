---
title: "TCP vs. UDP \x13 Quelles sont les différences et quel protocole est le plus\
  \ rapide ?"
subtitle: ''
author: Kristofer Koishigawa
co_authors: []
series: null
date: '2021-06-28T12:06:00.000Z'
originalURL: https://freecodecamp.org/news/tcp-vs-udp
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/ian-battaglia-9drS5E_Rguc-unsplash.jpg
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: internet
  slug: internet
- name: network
  slug: network
- name: networking
  slug: networking
seo_title: "TCP vs. UDP \x13 Quelles sont les différences et quel protocole est le\
  \ plus rapide ?"
seo_desc: 'If you''re getting into computer networking, or if you''ve dug through
  the network settings of some applications, you''ve likely seen these terms: TCP
  and UDP.

  TCP, which stands for Transmission Control Protocol, and UDP, or User Datagram Protocol,
  are ...'
---

Si vous vous initiez aux réseaux informatiques, ou si vous avez exploré les paramètres réseau de certaines applications, vous avez probablement rencontré ces termes : TCP et UDP.

TCP, qui signifie Transmission Control Protocol, et UDP, ou User Datagram Protocol, font partie de la suite de protocoles internet. TCP et UDP sont deux méthodes différentes pour envoyer des informations sur internet.

Mais même en connaissant leur signification, il est difficile de savoir quel protocole utiliser, ou pourquoi utiliser l'un plutôt que l'autre.

Dans cet article, nous allons passer en revue les bases des réseaux informatiques, les différences entre TCP et UDP, quand chacun est utilisé, et plus encore.

## Bases des réseaux informatiques

Avant de plonger dans le fonctionnement de TCP et UDP, il est utile de connaître les bases du fonctionnement d'internet.

En général, internet est un réseau de dispositifs connectés. Chaque dispositif, qu'il s'agisse de votre smartphone ou d'un serveur, communique via la suite de protocoles internet.

La suite de protocoles internet est une collection de différents protocoles, ou méthodes, permettant aux dispositifs de communiquer entre eux. TCP et UDP sont des protocoles majeurs au sein de la suite de protocoles internet :

![Diagramme de base de la suite de protocoles internet.](https://www.freecodecamp.org/news/content/images/2021/07/internet-protocol-suite-diagram.gif)
_[Source](https://www.sciencedirect.com/topics/computer-science/internet-protocol-suite)_

Chaque dispositif connecté à internet possède une adresse IP unique. Et chaque fois que deux dispositifs communiquent via internet, ils utilisent probablement soit TCP, soit UDP pour le faire.

Voici une brève comparaison entre les deux :

![Diagramme comparant TCP et UDP](https://www.freecodecamp.org/news/content/images/2021/07/tcp-vs-udp-diagram.png)
_[Source](https://www.wowza.com/blog/udp-vs-tcp)_

Pour une vue d'ensemble encore plus générale du fonctionnement d'internet, regardez cette vidéo de cinq minutes :

%[https://www.youtube.com/watch?v=7_LPdttKXPc]

## Qu'est-ce que TCP ?

TCP, ou Transmission Control Protocol, est le protocole de réseau le plus courant en ligne. TCP est extrêmement fiable et est utilisé pour tout, de la navigation sur le web (HTTP), à l'envoi d'e-mails (SMTP), en passant par le transfert de fichiers (FTP).

TCP est utilisé dans des situations où il est nécessaire que toutes les données envoyées par un dispositif soient reçues intactes par un autre.

Par exemple, lorsque vous visitez un site web, TCP est utilisé pour garantir que tout, du texte, des images et du code nécessaire pour afficher la page, arrive. Sans TCP, des images ou du texte pourraient manquer, ou arriver dans le mauvais ordre, ce qui casserait la page.

TCP est un protocole orienté connexion, ce qui signifie qu'il établit une connexion entre deux dispositifs avant de transférer des données, et maintient cette connexion tout au long du processus de transfert.

Pour établir une connexion entre deux dispositifs, TCP utilise une méthode appelée "three-way handshake" :

![Image](https://www.freecodecamp.org/news/content/images/2021/07/tcp-three-way-handshake-simple.png)
_[Source](https://www.techopedia.com/definition/10339/three-way-handshake)_

Par exemple, pour lire cet article sur votre dispositif, votre dispositif a d'abord envoyé un message au serveur de freeCodeCamp News appelé SYN (Synchronize Sequence Number).

Ensuite, le serveur de freeCodeCamp News envoie un message d'accusé de réception appelé SYN-ACK.

Lorsque votre dispositif reçoit le SYN-ACK du serveur, il envoie un message d'accusé de réception ACK, ce qui établit la connexion.

Une fois qu'une connexion TCP est établie entre deux dispositifs, le protocole garantit que toutes les données sont transmises.

Revenons à l'exemple de votre dispositif et de freeCodeCamp News : une fois le three-way handshake terminé, le serveur News peut commencer à envoyer toutes les données dont le navigateur web de votre dispositif a besoin pour afficher cet article.

Tous les dispositifs divisent les données en petits paquets avant de les envoyer sur internet. Ces paquets doivent ensuite être réassemblés à l'autre extrémité.

Ainsi, lorsque le serveur de freeCodeCamp News envoie le HTML, le CSS, les images et le reste du code pour cet article, il divise tout en petits paquets de données avant de les envoyer à votre dispositif. Votre dispositif réassemble ensuite ces paquets dans les fichiers et images nécessaires pour afficher cet article.

TCP garantit que ces paquets arrivent tous sur votre dispositif. Si des paquets sont perdus en cours de route, TCP permet à votre dispositif de signaler au serveur qu'il manque des données, et au serveur de renvoyer ces paquets.

Une fois que votre dispositif a reçu toutes les données nécessaires pour afficher l'article, TCP termine automatiquement la connexion entre les deux dispositifs avec une méthode similaire au three-way handshake, en utilisant cette fois des paquets FIN et ACK.

## Qu'est-ce que UDP ?

UDP, ou User Datagram Protocol, est un autre des principaux protocoles qui composent la suite de protocoles internet. UDP est moins fiable que TCP, mais il est beaucoup plus simple.

UDP est utilisé dans des situations où une certaine perte de données est acceptable, comme pour la vidéo/audio en direct, ou où la vitesse est un facteur critique comme dans les jeux en ligne.

Bien que UDP soit similaire à TCP en ce sens qu'il est utilisé pour envoyer et recevoir des données en ligne, il existe quelques différences clés.

Tout d'abord, UDP est un protocole sans connexion, ce qui signifie qu'il n'établit pas de connexion préalable comme le fait TCP avec son three-way handshake.

Ensuite, UDP ne garantit pas que toutes les données sont transférées avec succès. Avec UDP, les données sont envoyées à tout dispositif qui se trouve à l'écoute, mais il ne se soucie pas si une partie est perdue en cours de route. C'est l'une des raisons pour lesquelles UDP est également connu sous le nom de protocole "fire-and-forget".

Une bonne façon de penser à ces différences est que TCP est comme une conversation entre deux personnes. La personne A demande à la personne B de parler. La personne B dit oui, c'est bien. La personne A est d'accord et elles commencent toutes les deux à parler.

UDP est plus comme un manifestant à l'extérieur avec un mégaphone. Tout le monde qui prête attention au manifestant devrait entendre la plupart de ce qu'il dit. Mais il n'y a aucune garantie que tout le monde dans la zone entende ce que le manifestant dit, ou qu'ils écoutent même.

![Un diagramme comparant les connexions UDP et TCP](https://www.freecodecamp.org/news/content/images/2021/07/udp-and-tcp-comparison.jpg)
_UDP vs TCP  [Source](https://www.dpstele.com/snmp/transport-requirements-udp-tcp.php)_

## Lequel est le plus rapide  TCP ou UDP ?

En général, UDP est le protocole le plus rapide.

UDP est beaucoup plus simple et n'essaie pas d'établir une connexion entre les dispositifs avant d'envoyer des données, ou de vérifier que toutes les données sont même arrivées. Il envoie simplement des données à tout dispositif qui les demande, et continue à le faire jusqu'à ce que l'autre dispositif se déconnecte ou qu'il n'y ait plus de données à envoyer.

Imaginez boire à partir d'un tuyau plutôt que de siroter à partir d'une bouteille. Vous étancherez votre soif dans les deux cas, mais vous finirez probablement avec une chemise mouillée en utilisant la première méthode.

![Un mème montrant une personne buvant à partir d'une bouteille d'eau pour représenter TCP, et une autre personne versant de l'eau d'une bouteille sur son visage pour représenter UDP.](https://www.freecodecamp.org/news/content/images/2021/07/tcp-vs-udp-meme.png)
_Pas un tuyau, mais toujours assez précis. Imaginez également que la bouteille TCP continue à demander si vous avez reçu de l'eau pendant que vous buvez. [Source](https://www.reddit.com/r/ProgrammerHumor/comments/9gcwgw/tcp_vs_udp/e63axmd/)_

Mais être plus rapide ne signifie pas que UDP est le meilleur protocole globalement. Cela signifie simplement qu'il est meilleur dans certaines situations.

Comme mentionné précédemment, TCP est nécessaire dans des situations où il est vital que tous les paquets de données soient envoyés dans l'ordre, et que tous les paquets arrivent. Le web ne fonctionnerait tout simplement pas sans TCP.

Et bien que TCP soit plus lent en raison de la manière dont il établit les connexions, et des vérifications des paquets manquants, il peut toujours être extrêmement rapide. Parce qu'ils sont sur le web et utilisent HTTP, des sites comme YouTube ou Netflix utilisent tous TCP pour envoyer des données à vos dispositifs.

TCP permet également la mise en mémoire tampon, de sorte que votre navigateur peut demander et charger plus de données pendant que vous regardez, permettant une lecture fluide et de sauter à d'autres parties de la vidéo.

UDP est le meilleur choix pour la vidéo et l'audio en direct ou les jeux en ligne où la vitesse est plus importante que la perte potentielle de données.

Lorsque vous passez un appel via Google Meet ou Zoom, votre vidéo et votre audio sont transmis via UDP. Si certains paquets sont perdus en cours de route, cela apparaîtra simplement comme un peu de latence ou une vidéo/audio coupée.

Si vous jouez à des jeux vidéo, vous pourriez penser que la manière dont TCP garantit que tous les paquets de données arrivent à l'autre dispositif en ferait le choix idéal. Mais en réalité, toutes les vérifications et les renvois de données que TCP effectue ajoutent simplement de la latence.

Les développeurs de jeux ont trouvé d'autres moyens astucieux pour s'assurer que les entrées et l'état des joueurs sont aussi précis que possible. Si vous êtes intéressé à en savoir plus sur pourquoi UDP est préféré pour les jeux en ligne, consultez [cet article](https://gafferongames.com/post/udp_vs_tcp/).

## FIN

J'espère que cet article vous a aidé à comprendre certaines des nuances entre TCP et UDP. Et si quelqu'un vous demande lequel est le plus rapide, dites-lui ce que vous avez lu ici : "UDP est plus rapide, _mais_..."

Et si vous avez aimé ce que vous avez lu, faites-le moi savoir sur [Twitter](https://twitter.com/kriskoishigawa).