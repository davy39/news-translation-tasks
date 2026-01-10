---
title: Let’s Enhance ! Comment nous avons trouvé la clé privée obfusquée du portefeuille
  de 1 000 $ de @rogerkver
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-10-23T14:33:09.000Z'
originalURL: https://freecodecamp.org/news/lets-enhance-how-we-found-rogerkver-s-1000-wallet-obfuscated-private-key-8514e74a5433
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8kWT7sPCk3qu-fimhbLxAg.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Cryptocurrency
  slug: cryptocurrency
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Let’s Enhance ! Comment nous avons trouvé la clé privée obfusquée du portefeuille
  de 1 000 $ de @rogerkver
seo_desc: 'By Michel Sassano

  Before we even start: We do not know the journalists who recorded the interview
  and we do not know Roger Ver. Anyone who had access to this video could have retrieved
  the private key.

  We could have simply named this post “How great ...'
---

Par Michel Sassano

**Avant même de commencer : Nous ne connaissons pas les journalistes qui ont enregistré l'interview et nous ne connaissons pas Roger Ver. Quiconque ayant eu accès à cette vidéo aurait pu récupérer la clé privée.**

Nous aurions pu simplement intituler cet article « À quel point les QR codes sont géniaux et comment nous en avons récupéré un à partir de presque rien ». Mais c'est beaucoup plus intéressant quand le QR code est la clé d'un portefeuille Bitcoin Cash de 1 000 $.

Bitcoin, Ethereum, Litecoin, Dash, Neo… Les cryptomonnaies sont partout et évoluent rapidement. Je suis le Bitcoin depuis 2013 (suivre ne signifie pas acheter), et j'ai dû lire [Mastering Bitcoin](https://www.amazon.com/Mastering-Bitcoin-Programming-Open-Blockchain/dp/1491954388/ref=sr_1_1?ie=UTF8&qid=1508344325&sr=8-1&keywords=Mastering+Bitcoin) trois fois pour comprendre comment chaque partie fonctionne réellement et être capable de l'expliquer à quelqu'un d'autre. Pourtant, je n'arrive pas à suivre le marché, les nouvelles cryptomonnaies, les nouveaux forks, les nouvelles ICO partout, chaque jour.

Il est facile de commencer à utiliser des cryptomonnaies en suivant un tutoriel en ligne. Téléchargez une application de portefeuille au hasard, générez une paire de clés aléatoire et achetez des cryptos sur une plateforme d'échange quelconque, mais la courbe d'apprentissage des cryptomonnaies est difficile.

Si vous ne comprenez pas parfaitement comment toutes les parties fonctionnent, vous devriez éviter les cryptomonnaies. Sinon, vous risquez de perdre votre argent en tombant dans l'un des nombreux pièges. L'un d'eux, la sécurisation de votre clé privée, est le sujet de cet article.

> La première règle du Crypto Club est : vous ne partagez pas votre clé privée.

La chose la plus précieuse que vous possédez lorsque vous détenez des cryptomonnaies est votre clé privée. Si vous perdez votre clé privée, vous perdez votre argent. Si quelqu'un accède à votre clé privée, vous perdez votre argent. C'est simple.

Avec cet exemple concret, nous allons vous montrer étape par étape comment nous avons récupéré la clé privée du portefeuille Bitcoin de 1 000 $ créé par [@rogerkver](http://twitter.com/rogerkver) pour l'émission de télévision française « Complément d'enquête », même si elle était obfusquée.

### L'intro

La semaine dernière, France 2 a diffusé un documentaire sur le Bitcoin. [Ils ont interviewé @rogerkver](https://twitter.com/rogerkver/status/913705294546341888) qui a décidé d'offrir 1 000 $ en Bitcoin au téléspectateur le plus rapide. Malheureusement, le QR code et la clé privée ont été obfusqués par France 2.

![Image](https://cdn-media-1.freecodecamp.org/images/1*8kWT7sPCk3qu-fimhbLxAg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*8C1zHKPwxu0B3n8ztrR5_w.png)
_n°1 — QR code et clé privée obfusqués._

J'ai vu plusieurs personnes s'en plaindre sur Twitter, certains tweetant même que France 2 avait décidé de garder les Bitcoins pour eux. C'est faux, France 2 a dû obfusquer la clé, non pas parce qu'ils voulaient garder les Bitcoins, mais parce qu'ils y étaient légalement obligés.

Vous pouvez essayer de scanner le QR code avec autant d'applications différentes que possible, vous ne pourrez pas le décoder car il y a trop de flou.

L'histoire aurait pu s'arrêter là, les 1 000 $ perdus à jamais car je ne pense pas que Roger Ver ait gardé une copie de la clé privée. Seuls les journalistes qui ont enregistré l'interview auraient pu récupérer les Bitcoins.

**Mais**, vers la toute fin de l'interview, ils ont montré une petite partie claire du QR code. Ont-ils fait cela exprès, sachant que les 1 000 $ seraient perdus si personne n'était capable de trouver la clé privée ? Ou était-ce juste l'une de ces erreurs que l'on peut commettre quand on commence à utiliser des cryptomonnaies ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*TCSPcJvw2VXRIIkZyFBs8A.png)
_n°2 — Partie claire du QR code. Chaîne de la clé privée obfusquée en dessous._

J'étais sur le point d'envoyer un mail à mon ami [@clementstorck](https://twitter.com/clementstorck) quand j'ai reçu une capture d'écran du QR code qu'il avait prise. Nous avons décidé de travailler dessus pour voir si nous pouvions trouver la clé privée à partir d'une si petite quantité d'informations.

**Soyons clairs, les chances de trouver la clé privée uniquement par force brute étaient proches de zéro. Nous connaissions les propriétés des QR codes et leur résilience aux dommages. Notre objectif était de rassembler autant d'informations que possible pour réduire au maximum les paramètres inconnus. Nous savions que nous devrions utiliser la force brute à un moment donné. Après toutes les étapes ci-dessous, nous n'avions plus qu'à tester 2 097 152 combinaisons par force brute.**

Alors, par où commencer ? Voici toutes les étapes que nous avons suivies pour récupérer la clé privée :

1. Collecte d'informations
2. Let’s enhance ! Analyse d'image
3. Standard du QR code, partie 1
4. Reconstruction du QR code
5. Standard du QR code, partie 2
6. Décodage du QR code
7. Code de correction d'erreur (ECC)
8. Python & Force brute

### 1 — Collecte d'informations

La première étape consistait à rassembler autant d'informations que possible à partir de l'interview. Nous avons regardé le replay image par image et pris plusieurs captures d'écran telles que :

* La clé publique, qui nous mène à un [portefeuille BTC (presque) vide](https://www.blocktrail.com/BTC/address/17Qgadvc7pm51mV9r9zUAs4xU1XXwDRr8o). Roger Ver a-t-il menti ? Beaucoup de gens sur Twitter l'ont dit. Il n'a pas menti, il a tweeté à propos du giveaway [ici](https://twitter.com/rogerkver/status/913705294546341888). Nous devions chercher un [portefeuille BCH](https://cashexplorer.bitcoin.com/address/17Qgadvc7pm51mV9r9zUAs4xU1XXwDRr8o).

![Image](https://cdn-media-1.freecodecamp.org/images/1*23bONvo6gR_g-iLRnGBIpA.png)
_n°3 — La chaîne de la clé publique et le QR code : 17Qgadvc7pm51mV9r9zUAs4xU1XXwDRr8o_

* Une partie floue de la chaîne de la clé privée. Nous exploiterons cela lors de l'étape d'analyse d'image pour obtenir les 6 premières lettres. L'étape du code de correction d'erreur nous donnera les 7 lettres suivantes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XWS_QXIlh5BN3CwN13tyuA.png)
_n°4 — Partie floue de la chaîne de la clé privée. On peut lire quelques lettres mais ce n'est pas très clair._

* La dernière lettre de la clé privée, cela sera également très utile pour débloquer les 8 dernières lettres de la clé privée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*dHGbjqm_h7k1K1r00ibDpw.jpeg)
_n°5 — La dernière lettre de la clé privée. Un joli « V »_

* Des captures d'écran de mauvaise qualité du haut et de la gauche du QR code. Elles seront également utiles pour obtenir (un peu) plus de données et compléter le QR code pendant la phase de reconstruction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FN2B9gBWQZ46MzHdwSFsEA.png)
_n°6 — Le haut du QR code, la première ligne peut être exploitée._

![Image](https://cdn-media-1.freecodecamp.org/images/1*3Sd57yD9EodvKmVoF1QtTA.png)
_n°7 — Sérieusement ?? Le côté gauche du QR code, les deux premières colonnes peuvent être (partiellement) exploitées._

* L'outil qu'il a utilisé pour créer la clé publique et la clé privée est l'outil [Single Wallet sur Bitcoin.com](https://tools.bitcoin.com/paper-wallet/). Cela nous a donné des informations sur les données à l'intérieur du QR code : une clé privée Bitcoin au format Wallet Import Format de 52 caractères similaire à celle-ci :

> KwjiU4CVAmdyxyDbvkbx2XbSoU1nxZgyXz7usqAemvsd4RdGHoPF

La prochaine étape est de recréer le QR code.

### 2 — Let’s Enhance ! Analyse d'image

Ok, nous avons moins d'un tiers d'un QR code, nous sommes encore loin de la clé privée. Que pouvons-nous apprendre des captures d'écran que nous avons prises ?

Nous avons décidé de nous concentrer sur 2 captures d'écran, la première est le QR code flou de la clé privée, nous voulions savoir si des applications de QR code seraient capables de le lire après traitement.

La deuxième capture d'écran sur laquelle nous voulions travailler était celle avec la chaîne de la clé privée. Nous savions que nous devions avoir au moins une petite quantité de données si nous voulions que l'étape ECC (Error Correction Code) fonctionne.

Nous avons décidé d'envoyer les captures d'écran à nos experts. Avec beaucoup de résultats :)

Voici ce que nous avons obtenu après un certain défloutage.

* Une version défloutée du QR code, aucune des applications de QR code n'a pu le décoder. Nous voulions essayer car [ce gars a fait des crash tests](http://datagenetics.com/blog/november12013/index.html) sur les QR codes et d'après les commentaires, ils étaient tous scannables.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m88f_zFFk2r6RafkBpBO4w.png)
_n°8 — Nous n'avons rien tiré de cette image. Seulement une confirmation de la dernière lettre._

* Deux versions de la chaîne de la clé privée défloutées. La première nous donne les quatre premières lettres (on ne voit pas clairement le « K ») et la seconde les six premières lettres (on ne voit pas clairement le « z »).

![Image](https://cdn-media-1.freecodecamp.org/images/1*1uM8Z46GqwazwU4721Ep7Q.png)
_n°9 — C'est flou mais on peut lire « ?yUz »_

![Image](https://cdn-media-1.freecodecamp.org/images/1*v5IUaCFiapRZfcwMcHGVQw.png)
_n°10 — Un peu plus clair. On peut lire jusqu'à la 6ème lettre « KyU?sR »._

Gardons ces informations pour plus tard. Elles nous aideront à remplir certains bits en cours de route.

### 3 — Standard du QR code, partie 1

Il était important de comprendre comment fonctionnent les QR codes et les limites de leurs capacités ECC pour restaurer un QR code endommagé.

[Wikipedia](https://en.wikipedia.org/wiki/QR_code) est un bon début mais tout ce dont nous avions besoin se trouvait dans la [norme ISO/IEC 18004](https://www.iso.org/standard/62021.html) (Il existe une version gratuite de la première édition sur [Swisseduc](http://www.swisseduc.ch)). Nous avons également trouvé [cette pépite](http://www.thonky.com/qr-code-tutorial/introduction) en ligne.

![Image](https://cdn-media-1.freecodecamp.org/images/1*aZkpY6cHfEo692eN156AxA.png)
_n°11 — Le niveau de correction d'erreur et le masque du QR code peuvent être extraits de cette capture d'écran._

Avant de commencer à reconstruire le QR code, voyons ce que nous pouvons apprendre de cette image en utilisant la norme ISO et la structure d'un QR code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_CStncD18C9-OdxY-Bf2hQ.png)
_n°12 — Par Wtuvell sur Wikipedia anglais (Travail personnel) [Domaine public], via Wikimedia Commons_

La partie intéressante pour nous était la colonne bleue (x:8, y:22–28).

C'est une partie de la chaîne d'information de format (séquence de 15 bits. 5 bits de données et 10 bits de correction d'erreur [BCH](https://en.wikipedia.org/wiki/BCH_code)). Les bits situés à (x:8, y:22–28) sont les bits 8 à 14 de la chaîne. Nous n'avions que 7 bits sur 15 mais c'était suffisant pour trouver les informations dont nous avions besoin.

La chaîne d'information de format encode le niveau de correction d'erreur (EC) et le motif de masque appliqué au QR code. Il existe 4 niveaux d'EC possibles (L, M, Q, H) et 8 motifs de masque possibles => 32 chaînes d'information de format possibles.

Les détails sur la façon de créer la chaîne d'information se trouvent à la page 76 de la norme (Annexe C — Information de format). La liste des 32 possibilités peut être consultée [ici](http://www.thonky.com/qr-code-tutorial/format-version-tables).

Utilisons à nouveau la norme pour trouver quel bit correspond à quoi.

![Image](https://cdn-media-1.freecodecamp.org/images/1*3YyyARGrdOalBcAsYmM91A.png)
_n°13 — Par Wtuvell sur Wikipedia anglais (Travail personnel) [Domaine public], via Wikimedia Commons_

De haut en bas, nous avons les bits 8 à 14 de la chaîne d'information. Le bit 14 est le bit le plus significatif. À partir de la capture d'écran n°11, nous pouvons alors lire :

> 0011001XXXXXXXX

Une recherche rapide dans la [table des chaînes d'information de format](http://www.thonky.com/qr-code-tutorial/format-version-tables). La seule combinaison qui correspond est celle pour le niveau ECC : H et le motif de masque : 3.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7JaUXvLcvCMUMSO_oCoV1w.png)
_n°14 — Par Bobmath (Travail personnel) [CC0], via Wikimedia Commons_

Nous devions également trouver le format d'encodage du QR code. Il existe cinq formats d'encodage (chacun utilise une méthode différente pour convertir le texte en bits) :

* Numérique (0–9)
* Alphanumérique (0–9 ; A-Z ; neuf autres caractères : espace $ % * +- . / : )
* Octet 8 bits (jeu de caractères JIS 8 bits. [JIS X 0201](https://en.wikipedia.org/wiki/JIS_X_0201) version japonaise de l'[ISO 646](https://en.wikipedia.org/wiki/ISO/IEC_646))
* Kanji (caractère Shift JIS, peut encoder chaque caractère Kanji sur 2 octets)
* ECI (Extended Channel Interpretation, lorsque vous avez besoin d'un encodage spécial/personnalisé)

Le **format d'encodage pour le QR code est l'octet 8 bits**, les formats Numérique et Alphanumérique ne supportent pas l'alphabet de la clé privée (pas de lettres minuscules), le Kanji encode sur 2 octets (nous n'en avons besoin que d'un) et l'ECI est superflu.

Nous étions presque prêts à commencer la reconstruction du QR code, la dernière chose dont nous avions besoin était de connaître la taille du QR code.

Il existe 40 tailles de QR code (appelées versions). Elles vont de 21x21 pixels (version 1) à 177x177 pixels (version 40). Elles augmentent de 4x4 pixels à chaque fois que leur numéro de version augmente. Chaque version a une capacité maximale, basée sur le format d'encodage et le niveau de correction d'erreur.

La capacité de chaque QR code dépend de sa version et de son niveau de correction d'erreur. Les détails se trouvent à la page 28 de la norme ISO.

Nous savions que le QR code devait stocker 52 caractères (416 bits) avec un niveau de correction d'erreur H.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AnZ3_XUj8MLauKzb3XZV3w.png)
_n°15 — La V6 est la plus petite taille pouvant contenir la clé de 416 bits avec un niveau EC de H. La V5 est trop petite, la V7 trop grande._

La taille d'un QR code de version 6 est de 41x41 pixels.

Nous avions maintenant toutes les informations nécessaires pour commencer la reconstruction du QR code.

### 4 — Reconstruction du QR code

Nous savions que nous devions reconstruire un QR code de 41x41 pixels. Nous avons décidé de travailler sur un tableur Google (facile pour dessiner, colorer et appliquer des fonctions telles que le masquage sur le QR code).

Nous sommes passés par les étapes suivantes :

1. Dessiner chaque motif faisant partie de la norme (le motif de positionnement, le motif d'alignement (un seul dans un QR code de version 6), le motif de synchronisation et les séparateurs comme on le voit sur l'image n°12).
2. Ajouter les bits de la chaîne d'information de format que nous avons trouvés à l'étape précédente.
3. Remplir le reste du QR code en se basant sur la capture d'écran (n°11) que nous avons prise.

Exploitons également les captures d'écran des côtés haut et gauche du QR code. Cela ne semble pas beaucoup, mais à ce stade, chaque bit compte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BFKdguNS7Rvc0w8NhqOjdw.png)
_n°16 — Comment nous avons collecté quelques bits supplémentaires sur les lignes du haut_

![Image](https://cdn-media-1.freecodecamp.org/images/1*gDioTuWq6Lydyv8m_awGyQ.png)
_n°17 — Même processus pour le côté gauche du QR code (pivoté de 90°)_

Ci-dessous, le QR code que nous avons pu reconstruire. L'étape suivante consiste à définir la séquence de bits pour extraire les mots de code (Codewords) et les mots de code de correction d'erreur (ECC Codewords).

![Image](https://cdn-media-1.freecodecamp.org/images/1*OWeV8Qlp269sohVAQokaZg.gif)
_n°18 — Reconstruction étape par étape du QR code._

### 5 — Standard du QR code, partie 2

Nous devions comprendre comment lire le QR code si nous voulions en extraire plus de bits.

Un QR code est composé de blocs de **mots de code de données** et de **mots de code EC**. Chaque bloc fait 8 bits de long et chaque bit est représenté par un module (carré noir ou blanc). On ne peut pas dire en regardant simplement un QR code si un carré blanc spécifique est un « 0 » ou un « 1 » car, comme nous le verrons plus tard, un masque est appliqué au QR code avant son rendu.

Les **mots de code de données** portent le message/données encapsulés dans un protocole simple illustré ci-dessous (les détails se trouvent à la page 17 de la norme ISO) :

* Indicateur de mode : identifiant de 4 bits indiquant le mode d'encodage de la séquence de message/données.
* Indicateur de nombre de caractères : séquence de bits qui indique la longueur du message. Varie selon le mode d'encodage et la version du QR code.
* Flux de bits du message/données (clé privée). (8 bits par caractère)
* Terminateur : 4 bits utilisés pour terminer la chaîne de bits représentant le message.
* Bits de remplissage : utilisés pour remplir les positions vides du flux de bits.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Dxv1kOi84T8BOsgfqfCQoA.png)
_n°19 — Le flux de bits contenu dans les mots de code de données._

Les **mots de code ECC** sont ajoutés à la séquence de mots de code de données afin de détecter et de corriger les données en cas d'erreur(s) ou d'effacement(s). Ce sont des codes [Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction) générés à partir des mots de code de données. Nous en reparlerons un peu plus à l'étape n°7.

Le nombre de mots de code de données et ECC varie selon la version et le niveau de correction d'erreur. Ils sont divisés en groupes (1 ou 2) et en blocs (1 à 67) selon la version et le niveau EC.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oZfJUlEyZ-OQuGZtp80Fcw.png)
_n°20 — Caractéristiques de correction d'erreur pour la version 6 (page 35 de la norme ISO)_

Dans notre cas (Version 6, niveau EC H), nous aurons 15 mots de code de données et 28 mots de code ECC par bloc. Le QR code contiendra 1 groupe de 4 blocs pour un total de 172 mots de code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RFZkI2LKz-D5ki4_JFgJAQ.png)
_n°21 — Blocs de mots de code de données. Chaque mot de code fait 8 bits de long. Ils portent une partie du flux de bits du n°19_

![Image](https://cdn-media-1.freecodecamp.org/images/1*YSgSsKwSXqMUqy4GQbnQ1Q.png)
_n° 22 — Blocs de mots de code ECC. Ce sont des codes Reed-Solomon de 8 bits dérivés des blocs de données._

### 6 — Décodage du QR code

L'étape suivante consistait à lire le QR code et à remplir autant que possible le tableau des mots de code de données et ECC de l'étape 5.

La première étape consistait à démasquer le QR code. Nous avons utilisé un tableur Google pour créer le masque et utilisé la fonction BITXOR pour l'appliquer.

![Image](https://cdn-media-1.freecodecamp.org/images/1*_j_kq3wbIvFTYgS86mITXw.png)
_n°23 — Lorsqu'il est appliqué au QR code, chaque module vert du masque inverse la couleur du module._

Le résultat du processus de masquage est le QR code lisible. Comment lire le QR code et par où commencer ? La norme ISO explique comment les mots de code sont mappés sur le QR code et comment les lire (page 46 : Placement des mots de code dans la matrice).

Mappons les mots de code sur le QR code.

![Image](https://cdn-media-1.freecodecamp.org/images/1*UU8CD-pljWuwM7UHFlbh8w.png)
_n°24 — Position des mots de code de données et de correction d'erreur. On peut voir des symboles réguliers et irréguliers._

Maintenant, lisons chacun d'entre eux. Chaque symbole doit être lu d'une manière différente selon sa forme et sa direction de lecture comme on le voit ci-dessous et comme expliqué à la page 47 de la norme ISO.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MsJ7J0ErT6vNj6ZZJ7J5nQ.png)
_n°25 — Par Bobmath (Travail personnel) [CC0], via Wikimedia Commons_

Ci-dessous, le QR code lisible bit par bit. Chaque « X » est un bit inconnu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*MKpvQy_E46YjqUaeQRVeYw.png)
_n°26 — Décodage d'un QR code à la main, un bit à la fois. Ça a l'air amusant, n'est-ce pas ?_

Nous avons ensuite lu et rempli les tableaux de données et ECC de l'étape 4.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LzV9j1XOAy5mlzkje4XSPA.png)
_n°27 — Mots de code de données après lecture du QR code, remplissage des bits du protocole et de ceux obtenus via l'analyse d'image._

Les mots de code #1 et #2 sont connus car ils font partie du protocole (Indicateur de mode + Indicateur de nombre de caractères).

Les mots de code #3, #4, #6 et #7 sont connus grâce à l'analyse d'image effectuée à l'étape 2 (« KyUzsR »).

Les mots de code #54 à #60 sont également connus car ils font partie du protocole (Terminateur + Bits de remplissage).

Chaque « X » résolu augmente nos chances de réussir la phase ECC et divise par 2 le nombre de possibilités que nous devrons tester par force brute plus tard.

Vous vous demandez peut-être pourquoi le 5ème bit de tous les mots de code portant le message/données est réglé sur « 0 ». C'est parce que nous connaissons l'alphabet de la clé privée ([Base58Check](https://en.bitcoin.it/wiki/Base58Check_encoding)) et tous les caractères de cet alphabet commencent par un « 0 » lorsqu'ils sont encodés sur 8 bits. (Le 5ème bit de chaque mot de code est le premier bit de chaque lettre du message en raison du décalage introduit par les 12 premiers bits du protocole).

![Image](https://cdn-media-1.freecodecamp.org/images/1*JmVaA1O9sPyzPgM1t7sWiA.png)
_n°28 — Tableau des mots de code ECC après lecture du QR code. Rien à faire ici car ils sont tous définis par l'encodeur Reed-Solomon._

Utilisons maintenant la magie du code de correction d'erreur pour restaurer autant de données que possible.

### 7 — Code de correction d'erreur (ECC)

À ce stade, nous étions encore loin de la clé privée complète, mais nous allions bientôt savoir si nous avions collecté assez de données pour récupérer la clé en exploitant l'ECC.

L'[ECC](https://en.wikipedia.org/wiki/Error_detection_and_correction) regroupe des techniques qui permettent une communication fiable sur des canaux non fiables. Elles ont le pouvoir de reconstruire les données originales en détectant et en corrigeant les erreurs et les effacements.

Les QR codes implémentent des [codes Reed-Solomon](https://en.wikipedia.org/wiki/Reed%E2%80%93Solomon_error_correction) (un sous-type des codes BCH que nous avons vus lors du décodage de la chaîne d'information de format à l'étape 3).

Nous n'allons pas expliquer en détail comment encoder ou décoder les codes Reed-Solomon. Il existe de nombreuses bonnes ressources sur le web, mais rapidement :

* L'encodeur Reed-Solomon produit les mots de code ECC. Ils sont le reste d'une division entre le polynôme représentant le message et un polynôme générateur irréductible.

![Image](https://cdn-media-1.freecodecamp.org/images/1*V06l-51_noE5_n_Q7mDpXw.png)
_n°29 — Le polynôme générateur irréductible pour 28 mots de code EC._

* Le décodeur Reed-Solomon est un peu plus complexe car il existe de nombreuses façons différentes de décoder le message. Différents algorithmes de décodage existent pour cette tâche, [cette page](https://en.wikiversity.org/wiki/Reed%E2%80%93Solomon_codes_for_coders) est très utile pour comprendre le processus de décodage.

Un décodeur Reed-Solomon est capable de décoder les effacements et les erreurs en même temps. Malheureusement, il y a une limite, appelée la [borne de Singleton](https://en.wikipedia.org/wiki/Singleton_bound).

Le risque que nous avions était d'être au-dessus de cette limite. Reed-Solomon est un [FEC](https://en.wikipedia.org/wiki/Forward_error_correction) (Forward Error Correction) optimal et est « vulnérable » à l'[effet de falaise](https://en.wikipedia.org/wiki/Cliff_effect). Cela signifie que si vous dépassez la limite, vous ne pouvez rien tirer des codes EC et c'est là que nous avons dû utiliser la force brute.

La limite (nombre d'effacements et d'erreurs corrigeables) est définie par la formule ci-dessous, telle que définie à la page 33 de la norme ISO :

e + 2*t ≤ d - p

Où :

* e : nombre d'effacements
* t : nombre d'erreurs
* d : nombre de mots de code de correction d'erreur
* p : nombre de mots de code de protection contre le mauvais décodage (0 dans notre cas : 6-H)

Ce que cette formule signifie, c'est que vous pouvez corriger jusqu'à 14 erreurs ou 28 effacements par bloc (ou un mélange des deux si la somme n'est pas supérieure à 28). Nous avons profité du fait que nous savions où se trouvaient les effacements sur le QR code pour avoir le niveau de correction d'erreur le plus élevé possible (28 mots de code par bloc).

Vérifions pour chaque bloc si nous sommes en dessous ou au-dessus de la limite :

* Bloc 1 : Les données contiennent 6 effacements, l'ECC contient 22 effacements
* Bloc 2 : Les données contiennent 12 effacements, l'ECC contient 21 effacements
* Bloc 3 : Les données contiennent 10 effacements, l'ECC contient 18 effacements
* Bloc 4 : Les données contiennent 6 effacements, l'ECC contient 21 effacements

Avec 28 effacements, le bloc 3 et le bloc 1 sont juste à la limite et nous pourrons les récupérer à 100 %. Idem pour le bloc 4 avec un total de 27 effacements.

Avec 33 effacements, le bloc 2 est au-dessus de la limite et nous devrons utiliser la force brute. Heureusement, la force brute se fera sur un petit nombre de combinaisons.

### 8 — Python & Force brute

Nous avons décidé d'utiliser [ce codec Python Reed-Solomon](https://github.com/tomerfiliba/reedsolomon) pour décoder le message.

Nous utiliserons un mélange de code Python et de pseudo-code pour décrire les étapes que nous avons suivies pour trouver le résultat final.

Commençons par le meilleur scénario, lorsque nous sommes en dessous de la limite et décodons les blocs 3, 4 et 1.

![Image](https://cdn-media-1.freecodecamp.org/images/1*5Pj3LmfOlg3GN0BD-vrI9Q.png)
_n°30 — Décodage du bloc 3 à l'aide du décodeur Reed-Solomon._

Le résultat du décodeur pour le **bloc 3** est :

> [115, 22, 181, 6, 151, 103, 118, 229, 22, 133, 167, 39, 101, 164, 87]

Même processus pour le **bloc 4**, il suffit de modifier la valeur des variables mess, ecc et error_pos. Le résultat est :

> [118, 132, 183, 38, 36, 99, 116, 53, 96, 236, 17, 236, 17, 236, 17]

Le résultat du décodeur pour le **bloc 1** est :

> [67, 68, 183, 149, 87, 167, 53, 39, 86, 71, 4, 230, 180, 196, 182]

Jusqu'ici tout va bien. Malheureusement, si nous essayons la même chose avec le bloc 2, le décodeur échouera car nous sommes au-dessus de la limite.

La seule solution que nous avions était la force brute. Nous avions une marge négative de 5 (33 effacements au lieu de 28), l'objectif était donc de restaurer (tester par force brute) 5 mots de code et de voir quel résultat le décodeur nous donnait.

Pour réduire le nombre de possibilités, nous avons cherché dans les tableaux n°27 et n°28 les octets avec le moins de bits inconnus. Les mots de code de données #17, #19, #20, #27 et le mot de code EC #50 étaient intéressants.

21 bits inconnus au total, 2²¹ combinaisons (2 097 152), ce n'est pas si énorme. Ci-dessous le pseudo-code de la force brute.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AL9Zlrlca-8av1SmSqC1Rw.png)
_n°31 — Force brute sur le bloc 2, nous donnant les derniers bits dont nous avions besoin._

Mon processeur i5–6600K a pu calculer environ 30 000 clés par minute sur un seul cœur. Il a fallu 30 minutes et 838 849 essais pour trouver la première solution qui était la bonne pour reconstruire la clé privée (il n'y avait que 2 solutions sur ces 2 097 152 combinaisons qui correspondaient aux filtres).

![Image](https://cdn-media-1.freecodecamp.org/images/1*CntIoCDJsqx-GocGSl5Lxg.png)
_n°32 — Force brute sur le bloc 2_

Le résultat pour le bloc 2 :

> [85, 99, 35, 131, 19, 84, 181, 99, 148, 87, 165, 38, 99, 116, 84]

Nous avons maintenant tous les mots de code, la dernière étape consiste à convertir tous ces mots de code en binaire, remplir le tableau n°27, supprimer les 12 premiers bits, les 52 derniers bits, décoder et voilà !

Le résultat final est la clé privée :

> **KyUzsRudpNkLKeV2815KV9EzRf7EG1kPivwnQhZrvZEwhKrbF7CV**

#### Il va sans dire que vous ne devriez pas utiliser cette clé privée car elle n'est plus vraiment privée !

![Image](https://cdn-media-1.freecodecamp.org/images/1*phWxhx7nkfVY9ALaZmowGQ.png)
_QR code de la clé privée restauré !_

Roger, merci pour le giveaway. Le processus pour récupérer les BCH n'était pas aussi facile que de scanner le QR code à la télé, mais c'était stimulant et amusant.

#### Si vous avez apprécié cet article, n'hésitez pas à cliquer sur le bouton 👏 et à le partager pour aider les autres à le trouver. N'hésitez pas à laisser des commentaires ou des questions ci-dessous.