---
title: Contrôler une LED externe à l'aide d'un Raspberry Pi et des broches GPIO
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-07T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/hello-gpio-blinking-led-using-raspberry-pi-zero-wh-65af81718c14
coverImage: https://cdn-media-1.freecodecamp.org/images/0*xch19X3RFpIZdFXw.png
tags:
- name: Electronics
  slug: electronics
- name: General Programming
  slug: programming
- name: Python
  slug: python
- name: Raspberry Pi
  slug: raspberry-pi
- name: 'tech '
  slug: tech
seo_title: Contrôler une LED externe à l'aide d'un Raspberry Pi et des broches GPIO
seo_desc: 'By Shahbaz Ahmed

  In this post we’ll explore Raspberry Pi GPIO pins by creating a “Hello World” GPIO
  program that results in a blinking red LED. We’ll be using the Python programming
  language. I am using a headless Raspberry Pi Zero WH (wireless with ...'
---

Par Shahbaz Ahmed

Dans cet article, nous explorerons les broches GPIO du Raspberry Pi en créant un programme GPIO "Hello World" qui fait clignoter une LED rouge. Nous utiliserons le langage de programmation Python. J'utilise un Raspberry Pi Zero WH sans tête (sans fil avec en-têtes soudés) avec Raspbian Stretch Lite (système d'exploitation Raspberry Pi avec une image minimale basée sur Debian Stretch).

Je communiquerai avec mon Pi sans tête en utilisant `ssh` et transférerai les fichiers nécessaires de mon Mac vers le Pi en utilisant les commandes `scp`. Je suppose que vous avez votre Raspberry Pi en marche avec le système d'exploitation Raspbian installé. Si ce n'est pas le cas, il existe de nombreux articles sur Internet décrivant comment configurer votre Pi et installer Raspbian, y compris la [documentation officielle de Raspberry Pi](https://www.raspberrypi.org/documentation/).

Ce dont vous aurez besoin :

* 1 x Raspberry Pi (j'utilise le modèle Pi Zero WH)
* 1 x plaque d'essai
* 1 x LED rouge
* 1 x résistance de 330 ohms
* 2 x câbles de cavaliers femelle à mâle

### Configuration des broches GPIO

**GPIO** signifie **General Purpose Input Output**. Avec l'aide des broches GPIO, un Raspberry Pi peut se connecter et interagir avec des composants électroniques externes. Les modèles récents de Raspberry Pi (Pi 3, Pi Zero, Pi W et Pi WH, etc.) contiennent 40 broches GPIO. Chaque broche peut s'allumer ou s'éteindre, ou passer à `HIGH` ou `LOW` en termes électroniques. Si la broche est à `HIGH`, elle fournit 3,3 volts ; si la broche est à `LOW`, elle est éteinte.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Zpa1YOQcMlvu-Sxs.png)

Dans notre exemple, nous utiliserons la `broche 6` (masse) et la `broche 25`. Pour en savoir plus sur les broches GPIO du Raspberry Pi, consultez [pinout.xyz](https://pinout.xyz/).

### Installation du circuit

Vous devez éteindre le Pi pendant la construction du circuit. Nous créerons un circuit comme illustré dans le diagramme ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/0*xch19X3RFpIZdFXw.png)

**Note** : La résistance dans l'image est de 220 Ohm, mais j'ai utilisé 330 Ohm dans mon circuit.

1. Utilisez un câble de cavalier femelle à mâle pour connecter la `broche 6` (masse) (câble noir dans l'image ci-dessus) à la rangée négative de la plaque d'essai.
2. Utilisez un autre cavalier femelle à mâle pour connecter la broche GPIO `25` au point représenté par la rangée `A` et la colonne `12` sur la plaque d'essai comme montré ci-dessus (câble bleu dans l'image ci-dessus).
3. Connectez une extrémité d'une résistance de 330 ohms à la rangée négative (la rangée mise en évidence en vert où le câble noir a été connecté précédemment) et connectez l'autre extrémité au point représenté par la rangée `C` et la colonne `11` sur la plaque d'essai comme montré ci-dessus.
4. L'extrémité la plus courte de la **LED** est l'extrémité négative et la plus longue est l'extrémité positive. L'extrémité la plus longue doit toujours être connectée au point du circuit avec une tension plus élevée (c'est-à-dire un potentiel plus élevé). L'extrémité la plus courte de la **LED** est connectée à une broche GPIO `25` (qui peut fournir 3,3 V) via le câble bleu et l'extrémité la plus longue est connectée à la masse `broche 6` (qui est à 0 V et agit comme la borne négative de la batterie) via le câble noir avec une résistance entre eux.

### Résistance

En gardant à l'esprit que j'ai suivi des cours d'introduction en génie électrique et électronique il y a quelque temps (environ 4 à 5 ans), j'avais deux questions auxquelles je devais trouver des réponses. Veuillez m'excuser pour mon ignorance dans ce contexte.

1. Pourquoi avons-nous besoin d'une résistance dans notre circuit ?
2. Comment déterminons-nous combien d'ohms (la mesure de la résistance électrique) la résistance doit avoir ?

Une résistance est nécessaire pour dissiper l'énergie électrique excédentaire (tension) du Raspberry Pi. Le Raspberry Pi est conçu pour fournir 50 mA à 3,3 V. Supposons que notre LED rouge peut avoir une tension directe (la tension directe est la "tension négative" utilisée par la LED lorsqu'elle est allumée) d'environ 2 V et consomme 4 mA de courant. Ainsi, les 1,3 V restants doivent être dissipés par la résistance.

En utilisant la loi d'Ohm, `V = IR`, `R` = `(3,3V - 2V) / (4/1000)` ce qui donne environ `325 ohms` — je recommande donc d'utiliser une **résistance de 330 ohms**.

J'ai découvert cela dans une [discussion sur le forum Raspberry Pi](https://www.raspberrypi.org/forums/viewtopic.php?t=84240).

### Faire clignoter la LED avec Python

Maintenant que nous avons un circuit complet, la prochaine étape est de programmer les ports GPIO pour faire clignoter la LED. Nous utiliserons la sortie de la broche GPIO `25` pour faire clignoter la LED.

Démarrez votre Pi et connectez-vous à celui-ci en utilisant ssh. Dans le terminal, utilisez la commande suivante pour installer la bibliothèque Python `gpiozero`. La bibliothèque `gpiozero` simplifie grandement le travail avec les broches GPIO et les composants externes connectés.

Pour installer la bibliothèque Python, tapez `sudo apt-get install python3-gpiozero`.

Maintenant, nous allons exécuter du code Python. Enregistrez le code ci-dessous sur le système de fichiers de votre Pi dans un fichier nommé `blink1.py`. Le script allume la LED connectée à la `broche 25`, attend 1 seconde, éteint la LED, puis attend à nouveau 1 seconde. Et cela est fait en continu dans une boucle jusqu'à ce que le programme soit terminé (en appuyant sur `ctrl` + `c`).

Maintenant, depuis le terminal, allez dans le répertoire où le script est enregistré et exécutez-le avec la commande : `python3 blink1.py`.

Vous verrez la LED rouge clignoter comme ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/0*5v09jlygdroPzBCF.gif)

Nous pouvons construire beaucoup de choses amusantes en utilisant `gpiozero` avec une configuration similaire. Consultez [la documentation](https://gpiozero.readthedocs.io/en/stable/recipes.html) pour `gpiozero` qui démontre quelques exemples intéressants. Essayez de construire un système de feux de circulation.

_Publié à l'origine sur [shahbaz.co](http://shahbaz.co) le 7 avril 2018._