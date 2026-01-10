---
title: Périphériques réseau – Comment fonctionnent les concentrateurs et les commutateurs
  et comment les sécuriser
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2022-10-27T14:30:00.000Z'
originalURL: https://freecodecamp.org/news/how-hub-switch-work-and-how-to-protect-them
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/Computer-Networks-Hub-Switch.png
tags:
- name: computer network
  slug: computer-network
- name: computer networking
  slug: computer-networking
- name: Security
  slug: security
seo_title: Périphériques réseau – Comment fonctionnent les concentrateurs et les commutateurs
  et comment les sécuriser
seo_desc: 'In a previous post I described every bit and byte of the Ethernet protocol.
  In this post you will learn about two network devices, how they work, and how this
  knowledge may be used by hackers.

  How Classic Ethernet Works

  Before describing the network ...'
---

Dans [un article précédent](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), j'ai décrit chaque bit et octet du protocole Ethernet. Dans cet article, vous apprendrez à connaître deux périphériques réseau, leur fonctionnement et comment ces connaissances peuvent être utilisées par des pirates.

# Comment fonctionne l'Ethernet classique

Avant de décrire les périphériques réseau, considérons un réseau sans périphériques réseau spéciaux. C'est-à-dire, un réseau utilisant l'Ethernet classique où tous les ordinateurs sont attachés à un seul câble.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-168.png)
_Quatre appareils connectés utilisant l'Ethernet classique (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Dans ce cas, si l'ordinateur A envoie un message à un autre ordinateur, par exemple B, le message est envoyé sur le câble partagé, et tous les appareils le reçoivent.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-169.png)
_Avec l'Ethernet classique, si A envoie un message à B - tous les appareils (sauf A) reçoivent ce message (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Pouvez-vous penser à certains problèmes avec cette structure de réseau ?

Premièrement, **surcharge** – toutes les trames réseau sont reçues par tous les ordinateurs. Supposons que A veuille envoyer une trame à B. C voit également cette trame et doit réaliser qu'elle n'est pas destinée à son adresse, et donc la rejeter. Ce processus prend du temps et des ressources. Le même processus se produit sur la machine D, bien sûr.

Deuxièmement, **vie privée** – si C voit chaque message envoyé de A à B et vice versa, cela signifie que la vie privée est violée. Nous préférerions avoir un réseau où seuls A et B voient les messages envoyés entre eux.

Troisièmement, **extensibilité** – ce réseau n'est pas vraiment extensible. Supposons que jusqu'à 10 ordinateurs peuvent se connecter à ce câble. Que se passe-t-il lorsque vous devez ajouter un autre ordinateur ? Vous devriez remplacer l'ensemble du câble. Cela est coûteux et peu pratique.

Eh bien, la personne qui doit réellement remplacer le câble est probablement la personne de l'I.T. - vous savez, celle qui s'assure que tout fonctionne bien dans votre réseau et qui est rarement remarquée jusqu'à ce que quelque chose de mauvais se produise (au moins lorsque vous travaillez dans une organisation assez grande pour avoir des personnes de l'I.T.).

Pour être clair – nous ADORONS la personne de l'I.T. Nous voulons que sa vie soit bonne, nous ne voulons pas qu'elle passe son temps à acheter des câbles.

Quatrièmement, **collisions** – supposons que A veuille envoyer un message à B, et que C veuille envoyer un message à D. Au même moment, les deux pourraient commencer leur transmission, et les messages vont _entrer en collision_.

Dans ce cas, nous obtenons des erreurs – un peu comme le cas où deux personnes commencent à parler en même temps, et il est impossible de comprendre l'une ou l'autre.

Cinquièmement, cette structure de réseau peut conduire à la **famine** – supposons que A transmet une trame. Si les autres stations souhaitent éviter les collisions, elles s'abstiendront d'envoyer des données. Mais maintenant, la machine A peut continuer à transmettre indéfiniment, prenant ainsi toute la bande passante pour elle-même et ne laissant aucune autre station parler. Cela s'appelle la famine.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-181.png)
_Cinq problèmes majeurs avec les réseaux Ethernet classiques (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Eh bien, cela ne semble pas être le meilleur réseau, n'est-ce pas ?

Nous allons maintenant découvrir des périphériques réseau qui aident à résoudre ces problèmes.

# Comment les périphériques réseau résolvent ces problèmes

## Qu'est-ce qu'un concentrateur ?

Un périphérique qui résout uniquement le problème d'**extensibilité** est appelé un **concentrateur**. Un concentrateur est un périphérique avec plusieurs ports auxquels des câbles Ethernet individuels sont connectés :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-182.png)
_Un concentrateur Ethernet est un périphérique avec plusieurs ports, chacun connecté à un seul câble Ethernet (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Ainsi, au lieu d'avoir un câble avec plusieurs ports auxquels de nombreux ordinateurs sont attachés, nous avons plutôt un seul concentrateur, et chaque ordinateur est connecté à celui-ci via un seul câble. Cela rend la vie de la personne de l'I.T. beaucoup plus facile.

Le concentrateur prend simplement l'impulsion qu'il reçoit et la multiplie – c'est-à-dire, l'envoie à tous les autres ports. Par exemple, si A envoie une trame à B, le concentrateur enverra cette trame à B, C et D – tous les ports sauf le port de A.

Le concentrateur ne comprend pas Ethernet et ne connaît rien des adresses MAC. Pour le concentrateur, tous les bits sont simplement des bits transmis sur le fil, et ces bits doivent arriver à toutes les autres extrémités.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-183.png)
_Un concentrateur prend simplement un flux de bits et le multiplie à tous les ports sauf le port source (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Maintenant, si vous devez ajouter un nouvel ordinateur au réseau, vous pouvez simplement le connecter au concentrateur.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-199.png)
_Pour ajouter un nouvel appareil au réseau, nous le connectons simplement au concentrateur (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Que se passe-t-il si le concentrateur n'a plus de ports ? Pas de problème, nous le connecterons à un autre concentrateur, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-200.png)
_Au cas où vous n'auriez plus de ports, vous pouvez ajouter un autre concentrateur (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Super ! Cela est beaucoup plus facile à maintenir que l'Ethernet classique.

Pourtant, au moins avec les concentrateurs classiques, tous les autres problèmes subsistent. Puisque tous les ordinateurs reçoivent la trame envoyée de A à B, il n'y a pas de **vie privée**, le réseau est **surchargé**, des **collisions** peuvent se produire, et le réseau est sujet à la **famine**.

Ce que nous voulons vraiment, c'est un périphérique qui, lorsque A envoie une trame à B, transmet cette trame à B et **uniquement** à B. Ce périphérique est appelé un **commutateur**.

## Qu'est-ce qu'un commutateur ?

Si toutes les stations sont connectées via un **commutateur**, et que A envoie une trame à B, seul B la reçoit.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-201.png)
_Avec un commutateur, si A envoie un message à B - seul B le recevra (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Remarquez que cela signifie que tous les problèmes sont effectivement résolus. Les périphériques ne seront pas surchargés car chaque trame n'arrivera qu'aux destinataires concernés. Il n'y a pas de problèmes de vie privée puisque, à part le commutateur, seuls A et B voient la trame. Le réseau est facilement extensible en branchant des commutateurs supplémentaires si nécessaire.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-202.png)
_Similaire au travail avec des concentrateurs, le réseau est facilement extensible en ajoutant plusieurs commutateurs (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Le commutateur peut éviter les collisions car chaque connexion entre un commutateur et un point de terminaison est un seul **domaine de collision** – c'est-à-dire, le commutateur s'abstiendra d'envoyer plus d'une trame sur un seul fil en même temps.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-204.png)
_Chaque connexion entre le commutateur et un autre périphérique forme un domaine de collision indépendant (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

De même, il n'y aura pas de famine car B et C peuvent communiquer entre eux pendant que A envoie des données. Même si A continue à envoyer des trames destinées à l'ensemble du réseau, c'est-à-dire l'adresse de diffusion, le commutateur peut permettre aux messages envoyés par d'autres hôtes d'être transférés entre eux.

Mais, comment ce commutateur magique peut-il fonctionner ?

Supposons que nous venons d'acheter un tout nouveau commutateur et de le brancher sur le réseau. A envoie une trame destinée à B. Comment le commutateur sait-il où se trouve l'ordinateur B ?

Une option serait de configurer manuellement le commutateur. C'est-à-dire, avoir une table de mappage entre une adresse MAC et le port pertinent, et avoir quelqu'un configurer manuellement cette table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-205.png)
_Le commutateur peut contenir une table de mappage des adresses MAC aux ports physiques (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Lorsque nous disons _quelqu'un_, nous voulons généralement dire la personne de l'I.T. Et, eh bien, nous ADORONS les personnes de l'I.T. Nous ne voudrions pas leur faire faire ce travail fastidieux à chaque fois.

De plus, je ne sais pas pour vous, mais la plupart des gens n'ont généralement pas une personne de l'I.T. à la maison pour chaque fois qu'ils branchent un périphérique sur leur réseau.

Une autre option serait d'envoyer un message spécial du commutateur à chaque port, et ensuite les points de terminaison répondront avec leurs adresses MAC. Le principal inconvénient ici est que nous devons maintenant rendre tous les périphériques conscients du commutateur. Nous devons changer le comportement des périphériques pour qu'ils répondent à ce message spécial.

Il serait tellement mieux si le commutateur était simplement **transparent** – aucun point de terminaison n'aurait besoin de savoir qu'il est là, mais il ferait toujours le travail.

Apparemment, cela peut effectivement être réalisé !

Considérons ce réseau, avec un tout nouveau commutateur qui vient d'être ajouté au réseau. Le commutateur stocke une table, mappant une adresse MAC à un port physique. Cette table est vide.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-206.png)
_Quand un commutateur rejoint un nouveau réseau, la table de mappage des adresses MAC aux ports physiques est vide (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Maintenant, A envoie une trame à B.

Le commutateur comprend Ethernet et peut regarder l'en-tête de la trame et lire l'**adresse source**. Puisque cette adresse source correspond à « A », et puisque le message a été envoyé depuis le port physique numéro 2, le commutateur ajoute le mappage de l'adresse MAC de A et du numéro de port 2 à sa table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-207.png)
_Quand la machine A envoie une trame, le commutateur inspecte la trame, lit l'adresse source et la mappe avec le port physique correspondant (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Mais que fera le commutateur avec la trame ? Eh bien, pour l'instant, le commutateur ne sait pas où se trouve B, donc le commutateur multiplie simplement la trame et l'envoie à tous les ports, tout comme le ferait un concentrateur. Donc pour l'instant, B, C et D reçoivent tous la trame.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-208.png)
_Puisque la table du commutateur n'inclut pas d'enregistrement pour B, une trame destinée à B est en fait envoyée à tous les ports sauf le port source - de la même manière qu'un concentrateur le ferait (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Ensuite, A envoie un autre message à B. Le commutateur le regarde et sait déjà que l'adresse MAC de A est branchée sur le port numéro 2. Il ne sait toujours pas où se trouve B, donc cette trame est également envoyée à tous les autres ports.

Maintenant, C envoie une trame à A. Le commutateur regarde l'**adresse source** et ajoute le mappage entre l'adresse MAC de C et le port numéro 5 à sa table.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-209.png)
_À la réception d'une trame de C, le commutateur analyse son en-tête, extrait l'adresse source et l'associe au port physique correspondant - le port numéro 5 (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Cette fois, puisque la trame est destinée à l'adresse MAC de A, et puisque le commutateur connaît cette adresse – la trame peut être transmise au port numéro 2, et uniquement au port numéro 2. Hourra ! 👏🏻👏🏻👏🏻

Maintenant, B envoie un message à C. Le commutateur crée un mappage entre le port numéro 7 et l'adresse MAC de B, qui apparaît dans le champ **adresse source**.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-210.png)
_Le commutateur continue d'apprendre les adresses progressivement, en remplissant ses mappages internes (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Le commutateur peut également transmettre le message à C, car il connaît déjà l'adresse de C.

Ainsi, en général, le commutateur utilise le champ **adresse source** des trames Ethernet pour apprendre dynamiquement quelles adresses se trouvent derrière chaque port.

Maintenant, une question pour vous : Est-il possible que deux adresses différentes mappent à un seul port ? Par exemple, avoir l'adresse de l'ordinateur A mappée au port numéro 3, et aussi avoir l'adresse de l'ordinateur B mappée au port numéro 3 ? 🤔

Eh bien, la réponse est oui. Considérons le réseau suivant :

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-211.png)
_Un diagramme de réseau avec cinq points de terminaison et trois commutateurs (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

Maintenant, étant donné que les commutateurs connaissent le réseau, lorsque A envoie un message à D, il sera envoyé au commutateur 1, puis au commutateur 2, et finalement transmis par le commutateur 2 à D. Lorsque le commutateur 2 voit la trame, quelle adresse voit-il dans le champ **adresse source** ?

L'adresse de l'ordinateur A, bien sûr. Remarquez que les commutateurs sont transparents et ne modifient jamais les adresses MAC. Ainsi, le commutateur 2 apprend que l'adresse MAC de l'ordinateur A se trouve derrière le port numéro 3.

Ensuite, lorsque l'ordinateur B envoie une trame à l'ordinateur C, ce message sera également transféré via le commutateur 1 puis le commutateur 2. Ainsi, le commutateur 2 apprend que l'adresse MAC de l'ordinateur B se trouve également derrière le port numéro 3. Donc, dans ce cas, les adresses MAC de A et de B se trouvent toutes deux derrière le port numéro 3.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-213.png)
_Étant donné ce diagramme de réseau, le commutateur 2 enregistre à la fois l'adresse MAC de A ainsi que celle de B - avec le port numéro 3 (Source : [Brief](https://www.youtube.com/watch?v=Youk8eUjkgQ&ab_channel=Brief))_

REMARQUE qu'un commutateur n'est **pas** un _saut_ supplémentaire ! Nous ne parlons pas de routage ici. Comme nous l'avons dit précédemment, un commutateur est un périphérique **transparent**. Du point de vue des points de terminaison, il n'y a pas de commutateur – A « sent » comme s'il était directement connecté à B, C et D.

Tous les périphériques qui sont connectés via un **saut** sont considérés comme étant dans le même **segment de réseau**. Ici, tous les ordinateurs et commutateurs – A, B, C, D, le commutateur 1 et le commutateur 2 – résident tous dans le même segment.

Dans la section des ressources ci-dessous, j'ai ajouté un lien vers un exercice sur les concentrateurs et les commutateurs. Vous êtes les bienvenus pour le résoudre afin de vous assurer que tout est clair. Si vous avez des questions, n'hésitez pas à demander 😊

## Résumé intermédiaire

Jusqu'à présent, vous avez appris à connaître deux périphériques réseau. Premièrement, un concentrateur, qui est essentiellement un périphérique de première couche. C'est-à-dire, il transmet simplement des bits d'un port à d'autres ports, sans comprendre aucun protocole.

Deuxièmement, vous avez découvert un périphérique réseau de deuxième couche, à savoir un commutateur, qui « comprend » déjà le protocole Ethernet et les adresses MAC. Il utilise cette connaissance afin de transférer les trames uniquement aux ports pertinents, au moins une fois qu'il connaît le réseau.

# Sécurité 😈

Maintenant que vous comprenez comment fonctionnent les concentrateurs et les commutateurs, il est temps de considérer leurs implications en matière de sécurité.

Supposons que je sois connecté à un certain segment Ethernet, et que vous utilisiez l'ordinateur A. B envoie un message à C. Est-il possible pour vous de voir ce message ?

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-214.png)
_Quatre PC, B envoie une trame à C (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Dans le cas où les ordinateurs sont connectés via un concentrateur, vous verrez certainement le message, car le concentrateur transmet simplement la trame à tous les ports (sauf le port source) indépendamment de l'adresse de destination.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-215.png)
_Un concentrateur multiplierait simplement la trame et l'enverrait à A, C et D (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

De plus, si les ordinateurs sont connectés via un commutateur, mais que le commutateur n'a pas encore appris l'adresse de la destination, ce message sera également envoyé à votre port – et, en général, à tous les ports autres que le port source, tout comme un concentrateur agirait.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-216.png)
_Un nouveau commutateur agit exactement comme un concentrateur jusqu'à ce qu'il apprenne l'adresse de destination (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Ainsi, dans ces cas, votre carte réseau recevra les trames, mais les traitera-t-elle ?

Comme je l'ai couvert dans [un tutoriel précédent](https://www.freecodecamp.org/news/the-complete-guide-to-the-ethernet-protocol/), le premier champ d'une trame Ethernet est l'adresse de destination. Par défaut, la carte réseau rejettera les trames qui ne sont pas destinées à son adresse, ou à un groupe auquel son système appartient, comme l'adresse de diffusion.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-217.png)
_Structure de la trame Ethernet - les périphériques considèrent d'abord l'adresse de destination (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Ainsi, par défaut, si votre carte réseau reçoit une trame qui ne lui était pas destinée, la trame sera rejetée. C'est exactement là que le **mode promiscuous** entre en jeu. Lorsque la carte réseau est en mode promiscuous, elle ne rejettera pas les trames en fonction de leurs adresses MAC de destination.

Maintenant, considérons un réseau avec un commutateur, et que ce commutateur a déjà appris toutes les adresses du réseau, réalisant ainsi la confidentialité.

Supposons qu'une personne malveillante travaille depuis l'ordinateur C et souhaite voir la communication envoyée à l'ordinateur B, même si le commutateur transmet ces trames uniquement à B.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-218.png)
_Un réseau avec un commutateur qui a déjà appris les adresses MAC et leurs ports correspondants. Une personne malveillante peut-elle voir la communication privée ? (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

La personne malveillante peut-elle faire quelque chose pour voler les données ?

Eh bien, la personne malveillante peut prétendre qu'elle a l'adresse de B. C'est-à-dire, la personne malveillante enverra une trame avec l'adresse source de B. Peu importe vraiment quelle serait l'adresse de destination de cette trame.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-219.png)
_La personne malveillante envoie une trame et usurpe l'identité de B en spécifiant l'adresse MAC de B comme adresse source de la trame (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Maintenant, le commutateur voit une trame envoyée depuis l'adresse de B et depuis le port de C, dans notre diagramme, le port 5, et change le mappage de l'adresse de B vers le port 5.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-220.png)
_En conséquence, le commutateur change le port associé à l'adresse de B (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Comme je l'ai mentionné précédemment, il est effectivement possible d'avoir deux adresses MAC différentes mappées au même numéro de port (par exemple, dans le cas d'un commutateur supplémentaire qui connecte les périphériques ayant ces adresses). Mais il n'est pas possible d'avoir l'adresse de B mappée à deux ports différents.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-221.png)
_En ce qui concerne le commutateur, B et C peuvent effectivement être tous deux attachés à celui-ci via le port 5, peut-être par l'intermédiaire d'un autre commutateur (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Maintenant, si A envoie un message à B, il arrivera en fait à C, mais pas à B ! 😨

Cette technique est appelée **USURPATION D'ADRESSE MAC**. L'entité malveillante est dite **usurper** l'adresse MAC de B.

Cette technique est-elle très utile pour l'attaquant ? 🤔

Eh bien, pas vraiment. Une fois que B envoie _n'importe quelle_ trame au réseau, le commutateur remplacera l'entrée pour l'adresse MAC de B par celle du numéro de port correct. Ainsi, pour que l'attaquant continue à recevoir des données, il devra continuer à envoyer plus de trames au nom de B, provoquant ainsi le commutateur à réécrire l'entrée de la table encore et encore.

De cette manière, C enverra une trame en utilisant l'adresse de B, et le commutateur mappera l'adresse MAC de B au port de C. Ensuite, B enverra une trame, et le commutateur mappera l'adresse MAC de B au port de B à nouveau.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-223.png)
_Une fois que B envoie une trame, le commutateur écrasera son entrée et la valeur originale sera restaurée (Source : [Brief](https://www.youtube.com/watch?v=YVcBShtWFmo&t=3s&ab_channel=Brief))_

Par conséquent, B recevra une partie du trafic, et cette attaque est facilement noticeable.

Il existe de nombreuses façons de défendre un commutateur contre de telles attaques. L'une d'elles serait de définir le port avec un nombre maximum d'adresses MAC qui y sont attachées. Par exemple, si aucun autre commutateur ne doit être connecté à un certain port, le nombre maximum d'adresses MAC liées peut être défini à un.

N'est-ce pas génial ? En comprenant comment fonctionne un commutateur, nous sommes en mesure d'estimer les problèmes de sécurité qui découlent de son mode de fonctionnement, ainsi que les contre-mesures pertinentes. 🤯

# Conclusion

Dans cet article, vous avez appris à connaître deux périphériques réseau importants, un concentrateur et un commutateur.

Vous avez appris qu'un concentrateur multiplie simplement le flux de bits qu'il reçoit à tous les ports autres que le port qui a reçu le flux de bits, tandis qu'un commutateur transmet la trame uniquement au bon port (une fois qu'il a appris le réseau). Vous avez également appris comment les commutateurs sont capables d'acquérir cette capacité automatiquement.

Enfin, vous avez appris à connaître un problème de sécurité qui découle du fonctionnement des commutateurs, et comment il peut être atténué.

## À propos de l'auteur

[Omer Rosenbaum](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/) est le Chief Technology Officer de [Swimm](https://swimm.io/). Il est l'auteur de la chaîne Brief [YouTube Channel](https://youtube.com/@BriefVid). Il est également un expert en formation cybernétique et fondateur de Checkpoint Security Academy. Il est l'auteur de [Computer Networks (en hébreu)](https://data.cyber.org.il/networks/networks.pdf). Vous pouvez le trouver sur [Twitter](https://twitter.com/Omer_Ros).

## Ressources supplémentaires

* [Liste de lecture sur les réseaux informatiques - sur ma chaîne Brief](https://www.youtube.com/playlist?list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg)
* [Un exercice DIY sur les concentrateurs et les commutateurs](https://drive.google.com/file/d/1WeHTbRNph7mevNLwGeIkys1aP6_Z-Fbk/view)