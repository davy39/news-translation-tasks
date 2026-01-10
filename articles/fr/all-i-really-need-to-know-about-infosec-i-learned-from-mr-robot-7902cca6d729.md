---
title: Tout ce que je dois vraiment savoir sur la cybersécurité, je l'ai appris grâce
  à Mr. Robot
subtitle: ''
author: Quincy Larson
co_authors: []
series: null
date: '2016-02-02T02:49:41.000Z'
originalURL: https://freecodecamp.org/news/all-i-really-need-to-know-about-infosec-i-learned-from-mr-robot-7902cca6d729
coverImage: https://cdn-media-1.freecodecamp.org/images/1*oTCgvrRHRzNApJxeh-JKJg.png
tags:
- name: Design
  slug: design
- name: education
  slug: education
- name: Security
  slug: security
- name: social media
  slug: social-media
- name: technology
  slug: technology
seo_title: Tout ce que je dois vraiment savoir sur la cybersécurité, je l'ai appris
  grâce à Mr. Robot
seo_desc: 'I was trapped on a beastly 14-hour flight to China — complete with a jet-lagged
  newborn on my lap. Fortunately, the in-flight entertainment included a new cybercrime
  drama called Mr. Robot.

  This show takes technical realism to levels unprecedented fo...'
---

J'étais coincé dans un vol épouvantable de 14 heures vers la Chine — avec un nouveau-né souffrant du décalage horaire sur mes genoux. Heureusement, les divertissements à bord incluaient une nouvelle série sur le cybercrime appelée Mr. Robot.

Cette série pousse le réalisme technique à des niveaux sans précédent pour Hollywood. Elle a réussi à me distraire de la gêne d'être "ce type" avec le bébé qui pleure. Et j'ai même appris quelques choses sur la sécurité de l'information.

Par respect pour les lecteurs qui n'ont pas encore regardé cette série primée aux Golden Globes, j'ai purgé cet article de toute référence aux personnages ou à l'intrigue de l'histoire. **Lisez en toute confiance — cet article est sans spoiler.**

Sans plus attendre, voici cinq leçons de sécurité de l'information tirées de la saison 1 de Mr. Robot.

#### 1. Un hacker peut compromettre votre téléphone en quelques secondes, et vous ne le saurez même jamais

![Image](https://cdn-media-1.freecodecamp.org/images/1*3ZRrdaO_VDGPdRK7AG8kXQ.jpeg)

Les hackers n'ont pas besoin de voler votre téléphone — ce serait trop évident, et ne leur donnerait accès qu'à vos données passées.

À la place, ils peuvent prendre le contrôle de votre téléphone en utilisant un logiciel espion. Ils peuvent le faire en quelques minutes, et vous ne le saurez même jamais.

Dans Mr. Robot, l'un des personnages installe un rootkit sur le téléphone de quelqu'un en moins de temps qu'il n'en faut pour prendre une douche. En utilisant Flexispy — un outil de logiciel espion largement utilisé pour Android —, le personnage "root" le téléphone — le mettant en mode superutilisateur — puis cache l'icône normale du superutilisateur pour dissimuler le fait que le téléphone a été manipulé.

![Image](https://cdn-media-1.freecodecamp.org/images/1*GL3Ko4MvNmtR-UbDDhFBxQ.jpeg)
_FlexSpy — un logiciel espion menaçant avec la page d'accueil SaaS la plus banale qui soit._

Désormais, le personnage est capable de surveiller toutes les communications numériques et audio de ce téléphone.

Un conseil avisé — utiliser le scanner d'empreintes digitales de votre téléphone ou définir un mot de passe pour l'écran de verrouillage rendra beaucoup plus difficile pour un hacker de vous faire cela.

#### 2. N'acceptez pas de CDs ou de clés USB de la part d'inconnus

![Image](https://cdn-media-1.freecodecamp.org/images/1*-KtCOR3_KbFMhxBffIQX-Q.jpeg)

En sortant du métro, un rappeur diffusant sa musique à partir d'un boombox vous offre une copie gratuite de son dernier album.

Maintenant, vous n'accepteriez pas un bonbon d'un type en jeans à pattes d'éléphant pour le mettre dans votre bouche. N'acceptez pas un CD d'un type avec une casquette à visière plate pour le mettre dans votre ordinateur !

Pour être juste, vous devriez tout de même exécuter un fichier. Dans Mr. Robot, les hackers utilisent un nom de fichier alléant comme "Free iTunes Gift Card.exe" pour tromper la victime et la faire double-cliquer dessus. Cela installe un cheval de Troie d'accès à distance (RAT), donnant effectivement à l'attaquant l'accès aux fichiers et même aux webcams. Flippant.

#### 3. Cachez les choses en pleine vue

Parfois, le meilleur endroit pour cacher des choses est bien en évidence. Qui se soucierait de ce classeur de vieux albums de rock par terre ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*VO-eM007x-XwNFFtN8qXEg.jpeg)

Ce qui ressemble à un CD normal — qui joue même leur album griffonné dessus avec un marqueur — contient en réalité une couche supplémentaire de données cachées.

Retirés de tout accès réseau, la seule façon de lire les données sur ces CDs serait d'entrer physiquement dans les locaux et de les récupérer. Vous devriez ensuite avoir au moins assez de temps pour lancer un lecteur optique et en extraire le contenu.

#### Si vous n'utilisez pas le Bluetooth, éteignez-le.

![Image](https://cdn-media-1.freecodecamp.org/images/1*m16AZPqfMfQO8SMhPbtrHw.jpeg)

Si un attaquant découvre une connexion Bluetooth ouverte sur votre appareil, il pourrait y connecter son propre clavier et commencer à entrer des commandes.

Oui, il est possible d'ouvrir un terminal avec une série de raccourcis clavier sous Windows et OSX, et à partir de là, taper des commandes malveillantes.

En bonus, éteindre le Bluetooth lorsque vous êtes dehors réduira votre consommation de batterie, vous donnant plus de temps pour lire des articles Medium comme celui-ci (et suivre des auteurs Medium comme moi).

#### Vous êtes votre propre plus grande vulnérabilité

Tout au long de Mr. Robot, l'exploit le plus courant est le bon vieux social engineering — manipuler les gens pour qu'ils fassent ce que vous voulez.

Voici quelques signes avant-coureurs à surveiller lors d'interactions avec des inconnus :

* un appel téléphonique qui passe directement à "Je dois d'abord vous poser quelques questions de sécurité" — de nombreux services utilisent les mêmes questions de sécurité, et celles-ci pourraient également être utilisées pour accélérer une tentative de force brute pour deviner votre mot de passe.
* un inconnu vous aborde avec une histoire trop plausible et demande à utiliser votre téléphone — c'est un moyen facile d'obtenir votre numéro de téléphone ou d'autres informations d'identification
* Votre propre vanité, paresse, amour de la famille ou peur des germes — ce sont toutes des vulnérabilités qu'un attaquant peut exploiter. Si un inconnu semble vous monter émotionnellement pour aucune raison, il peut être plus qu'une simple personne méchante. Il peut être un attaquant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*U3z6k5J0bPgAMc0WNgerrQ.jpeg)

Si vous avez aimé cet article, vous aimerez probablement Mr. Robot. Vous pouvez [regarder toute la première saison ici](http://www.amazon.com/gp/product/B00YBX8QEO/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B00YBX8QEO&linkCode=as2&tag=out0b4b-20&linkId=7XIGZAKLZUHAOINS).

Vous pouvez également en apprendre davantage sur la cybersécurité grâce à [le plus célèbre hacker black hat lui-même](http://www.amazon.com/gp/product/B0047Y0F0K/ref=as_li_tl?ie=UTF8&camp=1789&creative=9325&creativeASIN=B0047Y0F0K&linkCode=as2&tag=out0b4b-20&linkId=YAU7HTXFLAUZKFPA).

Restez en sécurité !

**Je n'écris que sur la programmation et la technologie. Si vous [me suivez sur Twitter](https://twitter.com/ossia), je ne perdrai pas votre temps. ?**