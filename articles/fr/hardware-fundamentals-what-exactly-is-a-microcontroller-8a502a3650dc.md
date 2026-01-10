---
title: 'Fondamentaux du matériel : qu''est-ce qu''un microcontrôleur exactement ?'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-24T13:18:27.000Z'
originalURL: https://freecodecamp.org/news/hardware-fundamentals-what-exactly-is-a-microcontroller-8a502a3650dc
coverImage: https://cdn-media-1.freecodecamp.org/images/1*WKKNCMKqg6yEkowj28CHng.jpeg
tags:
- name: arduino
  slug: arduino
- name: hardware
  slug: hardware
- name: Internet of Things
  slug: internet-of-things
- name: Makers
  slug: makers
- name: technology
  slug: technology
seo_title: 'Fondamentaux du matériel : qu''est-ce qu''un microcontrôleur exactement
  ?'
seo_desc: 'By Taron Foxworth

  At the fundamental level, a microcontroller is a just tiny computer.

  Being a “tiny computer” doesn’t really tell us much, though. So let’s go deeper.
  Many people associate microcontrollers with Arduino. But it’s important to point
  o...'
---

Par Taron Foxworth

Au niveau fondamental, un microcontrôleur est simplement un petit ordinateur.

Être un « petit ordinateur » ne nous en dit pas vraiment beaucoup, cependant. Alors approfondissons. Beaucoup de gens associent les microcontrôleurs à Arduino. Mais il est important de souligner qu'**Arduino n'est pas un microcontrôleur**. Arduino est une plateforme complète qui s'étend à travers le logiciel et le matériel.

Arduino fabrique des appareils comme l'[Arduino Uno](https://www.arduino.cc/en/Main/arduinoBoardUno) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*GT8uC4hwFJfFb818C5g7LA.jpeg)
_Arduino Uno_

L'Arduino Uno n'est pas non plus un microcontrôleur. C'est une carte de développement basée sur le [microcontrôleur Atmel ATmega328P](http://www.microchip.com/wwwproducts/en/ATmega328P).

Voici à quoi ressemble le microcontrôleur Atmel :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dGZ5XWLj4osrGlUf79mW1w.png)

Si vous aviez seulement le microcontrôleur Atmel en main, en tant que débutant, il ne serait pas très utile. C'est là que la carte de développement entre en jeu.

La carte de développement « déporte » les broches du microcontrôleur vers un appareil plus grand (comme l'Arduino Uno). Cet appareil plus grand rend le microcontrôleur plus facile à utiliser.

Pour l'Arduino Uno, la carte de développement vous donne la possibilité d'insérer un câble USB, de l'alimenter, de programmer l'appareil, et plus encore.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jmPJwZqvF1QqNR0Xr_rmCw.jpeg)
_[Crédit image](https://www.hackster.io/hmkim/remote-controlled-8x8-led-matrix-e2b79a?ref=part&ref_id=8233&offset=18" rel="noopener" target="_blank" title=")_

Sans la carte de développement, pour un débutant, ce serait une tâche décourageante. Ce problème est la raison même pour laquelle Arduino existe — pour rendre super facile l'apprentissage du matériel.

### Ah, c'est comme le Raspberry Pi ?

Pas tout à fait. L'Arduino et le Raspberry Pi sont toujours des ordinateurs par définition. Mais le Raspberry Pi est considéré comme un [ordinateur monocarte](http://maxembedded.com/2013/07/introduction-to-single-board-computing/). Un ordinateur monocarte est [un ordinateur complet construit sur une seule carte de circuit imprimé](https://en.wikipedia.org/wiki/Single-board_computer).

![Image](https://cdn-media-1.freecodecamp.org/images/1*iK9lfwT4cpJsY4lWQ2ul0Q.jpeg)
_Un Raspberry Pi_

Votre ordinateur portable est également techniquement un ordinateur monocarte — simplement un puissant. Le Raspberry Pi est une version simplifiée du même matériel que votre ordinateur portable. Tout comme votre ordinateur portable exécute un système d'exploitation (Windows, Mac ou Linux), le Raspberry Pi exécute un système d'exploitation Linux.

Maintenant, revenons aux microcontrôleurs. Les microcontrôleurs ne peuvent pas exécuter un système d'exploitation. Les microcontrôleurs n'ont pas non plus la même puissance de calcul ou les mêmes ressources que la plupart des ordinateurs monocartes.

Un microcontrôleur exécutera un seul programme de manière répétée — pas un système d'exploitation complet. Nous pouvons voir cela dans les programmes Arduino car ils n'ont besoin que de deux fonctions : `Setup` et `loop`. `Setup` s'exécutera une fois et `loop` s'exécutera indéfiniment.

![Image](https://cdn-media-1.freecodecamp.org/images/1*2zfsMFC_vB9OMA81Hl5ITA.png)
_Setup et Loop_

### Alors, qu'est-ce qu'un microcontrôleur ?

Un microcontrôleur est un petit ordinateur avec une faible mémoire et des périphériques d'entrée/sortie programmables.

#### Entrées/Sorties

Comme vous le savez probablement, tout avec un ordinateur finit par être binaire (0 ou 1).

![Image](https://cdn-media-1.freecodecamp.org/images/1*GFnxrpbOLyCUBuhnwxIHNA.png)

Une entrée signifie que le microcontrôleur lira le binaire. Un exemple d'entrée serait un capteur.

Une sortie signifie que le microcontrôleur enverra du binaire. Un exemple de sortie serait de contrôler un moteur ou une LED.

### Pourquoi avons-nous besoin de microcontrôleurs ?

Eh bien, ce sont des « ordinateurs » avant que nous arrivions à l'idée des ordinateurs que vous connaissez aujourd'hui. Les microcontrôleurs sont restés parce que certaines tâches informatiques sont incroyablement triviales et nécessitent une logique simple. Par exemple, actionner un interrupteur ou contrôler de petits composants — comme une lumière LED — ne nécessite pas les mêmes ressources que celles dont nous avons besoin pour les tâches quotidiennes comme envoyer un email.

Nous les utilisons aujourd'hui parce que leur faible puissance et leur faible mémoire les rendent peu coûteux. Les microcontrôleurs font partie des raisons pour lesquelles l'[Internet des objets](https://en.wikipedia.org/wiki/Internet_of_things) est possible et réussi aujourd'hui.

### Comment en obtenir un ?

Le microcontrôleur que vous voudrez obtenir dépend du problème que vous souhaitez résoudre. Si vous faites quelque chose de simple — allumer et éteindre des choses, ou lire un capteur — presque n'importe quel microcontrôleur fera l'affaire.

Si vous voulez jouer à des jeux ou avoir des idées plus complexes, vous aurez besoin de plus de puissance de calcul, donc vous devrez passer aux ordinateurs monocartes, comme le Raspberry Pi.

[Adafruit](https://www.adafruit.com/) et [Sparkfun](https://www.sparkfun.com/) ont tous deux des TONNES de kits et de matériel qui sont tous incroyables. Vous pouvez également utiliser leurs tutoriels.

[Losant](https://losant.com) a également quelques kits sympas disponibles. Vous pourriez construire votre propre [capteur de porte](https://docs.losant.com/getting-started/losant-iot-dev-kits/door-sensor-kit/)
—
pour être averti lorsqu'une porte est laissée ouverte trop longtemps.

Si vous n'avez pas de problème spécifique que vous voulez résoudre, procurez-vous simplement du matériel et amusez-vous avec.

Voici quelques choses que vous pouvez acheter pour commencer :

#### 1. Une carte appelée [NodeMCU](http://amzn.to/2oyalUf).

![Image](https://cdn-media-1.freecodecamp.org/images/1*lVu30df4maR8KAoG1vKDlg.jpeg)
_Node MCU_

Le [NodeMCU](http://amzn.to/2p3YDEu) est une carte basée sur le microcontrôleur ESP8266. Cette carte est spéciale car elle est bon marché et équipée du WiFi. Elle ne vous coûtera que environ 8,79 $ sur Amazon et encore moins sur Ebay.

Tous les microcontrôleurs ne sont pas équipés du WiFi. Le fait que celui-ci le soit ouvre la porte à un certain nombre de projets que vous pouvez construire avec cet appareil. Par exemple, vous pouvez collecter des données et les envoyer dans le cloud ☁️.

#### 2. Vous aurez besoin de quelques [Capteurs](http://amzn.to/2ocLN7O)

![Image](https://cdn-media-1.freecodecamp.org/images/1*tJrDBAK3Gi1gd3EucYqsnw.jpeg)
_Platine d'expérimentation_

Vous ne pouvez pas avoir de matériel sans capteurs. Les capteurs vous donnent la capacité de détecter l'environnement et le monde qui vous entoure. Ils sont également un excellent outil pour apprendre.

#### 3. Vous aurez besoin d'une [Platine d'expérimentation](http://amzn.to/2oul4zW) et de [Fils de connexion](http://amzn.to/2p0stYM) :

![Image](https://cdn-media-1.freecodecamp.org/images/1*hzlbvjGieO28VE7VKbFFZw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*-Ts_mndGd90p9JEImUouDQ.jpeg)

Pour connecter un capteur et le microcontrôleur ensemble, vous devrez les brancher sur la platine d'expérimentation et utiliser les fils de connexion pour les relier.

Rappelez-vous : tout est moins cher sur [eBay](http://ebay.com/) et [AliExpress](https://www.aliexpress.com/). Vous devrez simplement attendre quelques semaines pour la livraison.

### Que devrais-je construire ?

Encore une fois — et je ne peux pas insister assez sur ce point — il est beaucoup plus facile de commencer avec un projet en tête. Maintenant que vous comprenez ce qu'est un microcontrôleur et comment en obtenir un, jetez un regard différent sur le monde qui vous entoure. Que pouvez-vous contrôler ? Que pouvez-vous automatiser ? Une fois que vous commencerez à répondre à ces questions, vous trouverez un projet.

En pensant à des projets, [Hackster](https://www.hackster.io/) est votre meilleur ami. Hackster a une tonne de [projets ESP8266](https://www.hackster.io/esp) et quelques projets Arduino sympas :

Par exemple, vous pouvez réaliser un rêve d'enfance.

Vous pouvez même construire des robots.

Le point est, vous avez juste besoin d'une idée.

Parfois, programmer le monde réel est plus amusant que de programmer des mondes virtuels.

### Qu'est-ce qui suit ?

Les microcontrôleurs ne sont que le début. Vous avez un monde de matériel à explorer. Bon bidouillage 😊

#### Lectures complémentaires :

[**Le Guide Absolu du Débutant pour Arduino**](http://forefront.io/a/beginners-guide-to-arduino/)  
[_Pendant les vacances de Noël au travail, je voulais apprendre quelque chose de nouveau. J'ai eu Arduino à l'œil depuis un certain temps maintenant, et
…_forefront.io](http://forefront.io/a/beginners-guide-to-arduino/)

[_Taron Foxworth_](https://twitter.com/anaptfox) _est un bidouilleur de matériel et l'Évangéliste Développeur chez [Losant](https://www.losant.com). Son objectif est de traduire la technologie pour que les gens puissent apprendre, aimer et être inspirés._