---
title: Les enseignements que j'ai tirés de la construction d'un robot à commande vocale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-05T17:40:58.000Z'
originalURL: https://freecodecamp.org/news/building-a-voice-activated-robot-for-an-advertising-agency-fedaa9f347d3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lbIDINee-izLUwkgIb581g.gif
tags: []
seo_title: Les enseignements que j'ai tirés de la construction d'un robot à commande
  vocale
seo_desc: 'By Mithi


  Insights I gained from building a voice-activated robot


  For almost a year, I worked at an advertising agency as a creative technologist.
  Based on the insight that innovation drives new businesses and that technology can
  be creatively appli...'
---

Par Mithi

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ao2FdjrlyNOlixjPtXD7Cg.jpeg)

# Les enseignements que j'ai tirés de la construction d'un robot à commande vocale

![Image](https://cdn-media-1.freecodecamp.org/images/1*lbIDINee-izLUwkgIb581g.gif)

Pendant près d'un an, j'ai travaillé dans une agence de publicité en tant que [technologue créatif](http://digit.gitlab.io/digit-x/). Basé sur l'idée que l'innovation stimule les nouvelles entreprises et que la technologie peut être appliquée de manière créative aux campagnes de marque, il y a quelques choses intéressantes que je fais dans mon travail. J'introduis de nouvelles technologies, je fais des vérifications de faisabilité des idées technologiques par des créatifs non techniciens, et je [prototype des choses](https://docs.google.com/presentation/d/18nTykqw-Evj0o0kAuIuKrMsknV8-LQz7Obmxvazd1wQ/edit?usp=sharing), entre autres.

Peut-être l'une des choses les plus excitantes que j'ai faites dans mon travail était de travailler avec des robots ! J'ai supervisé la création et programmé un robot de 45 pouces de haut pendant un peu plus de deux mois.

### Comment nous avons construit Robbie

Rencontrez Robbie — également connu sous le nom de [HelloBot](http://digit.gitlab.io/digit-x-robot/) — une expérience sur la façon dont les humains et la technologie interagissent en faisant en sorte que les gens se connectent avec un robot de la même manière que les gens se connectent avec d'autres personnes. L'idée derrière Robbie est que la technologie, comme un robot, peut renforcer votre marque avec chaque interaction agréable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EwOqyh2QmjSAI-ZsD8fgLg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*CfIj9YaFMg4zsJ1o_4OzMQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ASspWUHMXcbvs_25y15IoQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*IhER4KvG8sF8CpByaBNITw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*O1dMfn33Oj88-3gJ3TKm7w.jpeg)
_Quelques enseignements que j'ai tirés du processus créatif de construction de la version "produit minimum viable" du robot Robbie._

Il est plus facile que jamais de construire un robot sophistiqué avec des pièces toutes faites.

Tout cela grâce à la communauté du matériel open-source (OSHW). Construire un robot est possible parce que nous nous appuyons sur les épaules généreuses de géants.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ytlKHwxvDr0QxF57PGJGmQ.png)

Tous les composants électroniques utilisés pour construire Robbie peuvent être achetés chez [DFRobot](http://dfrobot.com), [Adafruit](http://adafruit.com) et [Hobby King](http://hobbyking.com). Tous sont open-source — les schémas, la liste des matériaux et la conception des cartes PCB sont libres à télécharger, reproduire ou modifier.

Chaque composant n'est pas une boîte noire où vous devez dépendre d'une petite équipe de support client pour résoudre vos problèmes. Lorsque quelque chose ne va pas, vous avez toute une communauté pour vous aider.

De plus, parce que beaucoup d'informations sont librement disponibles, vous gagnez une compréhension plus profonde de comment les choses fonctionnent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y8TWQZcSb8afA6YVwZOn3g.png)

Le cerveau de notre robot est un [Raspberry Pi 3](http://raspberrypi.org), un ordinateur de la taille d'une carte de crédit avec WiFi intégré. Il est connecté à une variété de périphériques pour que le robot puisse recevoir des entrées et produire des sorties vers le monde extérieur.

Certaines des entrées sont : un microphone pour que le robot puisse entendre vos mots, une caméra de 8 mégapixels pour que le robot puisse vous voir, et un capteur infrarouge passif (PIR) qui s'active lorsque le "niveau de radiation moyen change". Cela est utile pour détecter si des êtres humains entrent ou sortent du territoire du robot.

Certaines des sorties sont l'écran de 7 pouces où le robot montre ses expressions, et des haut-parleurs audio pour que vous puissiez entendre ce qu'il dit. Le Raspberry Pi 3 est connecté au WiFi et utilise la [bibliothèque de reconnaissance vocale de Google](https://cloud.google.com/speech/). Il utilise une bibliothèque de vision par ordinateur open-source ([OpenCV](http://opencv.org/)) pour reconnaître les visages.

![Image](https://cdn-media-1.freecodecamp.org/images/1*fs7Rac0WtXGOVXOc8QTKBw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Uby_FKtAS17bEQqoaCgcAA.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Go_98roPwBS-v29WreJonQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*j9ye4Fc-7IHgN1o3VvJrFw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*XPN79SUj4KgneTd__oVx7Q.png)

Le Raspberry Pi 3 communique avec un microcontrôleur [Arduino Mega](http://arduino.cc) pour déléguer des tâches de bas niveau que le Pi ne gère pas bien. L'Arduino Mega contrôle deux drivers de moteur (il a quatre roues que vous pouvez contrôler indépendamment) pour que le robot puisse se déplacer à gauche, à droite, en avant et en arrière.

Il a également deux servomoteurs (moteurs spéciaux qui peuvent être dirigés par angle grâce à un circuit de rétroaction intégré) pour déplacer ses bras.

Il y a aussi des périphériques de bas niveau connectés à l'Arduino, comme des LEDs RGB adressables et chaînables colorées "[Neopixels](https://www.adafruit.com/category/168)" pour indiquer l'état, et trois capteurs de distance infrarouges pour éviter les obstacles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*eRBynzsjCT4rBkWus6EQDQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*5AhcgK5hhx6I7Q8cnFXVFw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*d42GY-71f49-BO0qO2az3A.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UBpqeq23_NSHpTsq6Nr2Wg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*C54Waq3zARr3bQjZJdD5pw.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*kqkZnCZ03zp0rl7nKpP2VA.png)

L'ensemble du robot (y compris les moteurs) est alimenté par des batteries lithium-polymère de 14,8v 4500 mAh. Des convertisseurs DC-DC régulent la puissance pour la réduire à une tension plus faible nécessaire pour alimenter en toute sécurité le Raspberry Pi et l'Arduino.

![Image](https://cdn-media-1.freecodecamp.org/images/1*IOu2YTtIzPYhjKJyCOeOUQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*SlxuVaf8IMv3PfJNP52p_Q.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*meNEUTZBF699GTbpRIuZZw.png)

Nous n'aurions pas pu concevoir, et encore moins comprendre, tout cela sans les généreux tutoriels réalisés par la communauté du matériel open-source — en particulier par [Adafruit Industries](http://adafruit.com), pionnière grâce à [Limor "Lady Ada" Fried](https://en.wikipedia.org/wiki/Limor_Fried).

Voici quelques-unes des choses que j'ai apprises tout au long de ce processus.

### Concevoir un "code propre" est crucial

![Image](https://cdn-media-1.freecodecamp.org/images/1*7aqCLMcrRsC1z3XL3uqMgg.jpeg)

Essayer de concevoir un code "propre" est très important lorsque vous essayez de construire un robot que vous aimerez non seulement interagir mais aussi développer.

J'ai appris à être réfléchie lorsque j'écris du code pour ce robot, inspirée par les livres sur l'artisanat du code de [Robert Martin](https://www.amazon.com/Clean-Code-Handbook-Software-Craftsmanship/dp/0132350882) et [Sandi Metz](https://www.sandimetz.com/). Je ne suis pas une vétéran de l'écriture de code bien conçu, mais je fais de mon mieux.

Lorsque vous faites de la maintenance de code dans un robot, vous pouvez vraiment "adorer" ou "détester" une personne que vous ne connaissez même pas juste à cause du code qu'elle a écrit.

Le code désordonné va presque toujours de pair avec une productivité réduite, une motivation plus faible et un nombre plus élevé de bugs. D'innombrables heures et des ressources significatives sont perdues à cause d'un code mal écrit, mais cela n'a pas à être ainsi.

Le code propre est quelque chose qui me trotte dans la tête depuis un moment. Il y a un an, j'ai parlé à la [Python Conference Philippines](https://medium.com/nanica-talks/nanica-io-talk-a-raspberry-pi-hexy-transcript-d39257ac7cdc#.kq3lt4p7j) de la façon dont j'ai fait danser un robot hexapode dans l'effort de pratiquer l'écriture de code propre. J'ai parlé de mes principes directeurs pour un code écrit de manière réfléchie.

Encore plus tôt, j'ai écrit sur [les choses auxquelles je pense](https://medium.com/@mithi/review-sandi-metz-s-poodr-ch-1-4-wip-d4daac417665) lorsque je décide d'écrire mes propres classes. C'est partie de mon effort pour appliquer une philosophie de conception orientée objet pour rendre mon code propre.

J'ai toujours ces principes et ces pensées à l'esprit chaque fois que j'écris du code en général, et en particulier lorsque j'ai écrit [le code pour Robbie](https://github.com/mithi/hellobot-raspberry).

![Image](https://cdn-media-1.freecodecamp.org/images/1*UYF78LVNFkCJV4i9W_oavg.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*rCZipTusi6cIbhpGUUYyrQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*n6jAs6mFkdoz-a8RPYlqTA.png)

Le code résidant dans la section [Arduino](http://github.com/mithi/hellobot-arduino) est écrit dans une version simplifiée de C++ conçue pour la programmation embarquée. Il a deux classes évidentes, `Motors` et `DistanceSensors`.

La classe `Motors` est responsable de l'entraînement des roues pour faire tourner le robot à gauche, à droite, avancer ou reculer.

La classe `DistanceSensors` est responsable de la mesure de la distance et de la vérification de la présence d'obstacles autour.

Il y a d'autres classes que j'ai utilisées et qui ont été créées par d'autres personnes, comme `Serial` et `Neopixel`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qfWOpD6_uaTRLjZE5YWn4w.png)

Le code résidant dans la section [Raspberry Pi](http://github.com/mithi/hellobot) est écrit en Python. Certaines des classes que j'ai écrites pour lui sont `Listener`, `Responder`, `Directive`, `Relayer` et `FaceFinder`.

Une instance de `Listener` est nécessaire pour obtenir les phrases (au format chaîne) à partir des données du microphone, telles qu'interprétées par GoogleSpeech.

Le `Responder` lit des vidéos ou affiche des images sur l'écran.

Le `Directive` traite la phrase pour obtenir le mot après un **mot-clé** qui est utilisé pour donner des commandes au robot à exécuter.

Le `Relayer` communique avec l'Arduino.

Le `FaceFinder` est responsable de la détection des visages.

Pour un code plus propre, les classes doivent être responsables d'une seule chose et rien de plus. Les classes sont créées pour simplifier les choses, pas pour les compliquer. Vous savez qu'une classe est simple lorsque vous pouvez décrire ce qu'elle fait en une seule phrase comme je viens de le faire.

### Apprendre par l'expérience est la voie à suivre

Vous avez besoin d'itérations continues et de retours utilisateurs pour obtenir une bonne expérience utilisateur pour votre produit.

Robbie dans son état actuel n'est qu'un "produit minimum viable". Il y a encore beaucoup de choses qui peuvent être faites pour améliorer la fiabilité, l'expérience utilisateur et la conception globale de Robbie.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7GRlsGxGrXvTbaHS-YXGVg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*fFaQQ74ezmW2ttOiE64law.jpeg)

Au début, nous avons conçu Robbie pour avoir divers modes (**mode autonome**, **mode caméra**, **mode télécommande**, **mode conversation**), qui peuvent être activés en appuyant sur des boutons.

Mais lorsque les gens ont commencé à interagir avec lui, nous avons réalisé que Robbie serait un robot à commande vocale 90 % du temps. Chaque fois que les gens rencontrent Robbie, leur instinct est de se diriger vers le robot et de lui parler.

![Image](https://cdn-media-1.freecodecamp.org/images/1*XzoRTl4gL7B2lJZgRAcvzQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*UZ6ERqQ2UYzbicsO58xY2g.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*_XoTS1r9mOj3bpPux-u-Sw.png)

Nous avons réalisé à quel point il était important pour Robbie d'avoir un meilleur microphone et de meilleurs haut-parleurs audio, plutôt que d'ajouter plus de capteurs pour une meilleure détection d'obstacles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9uhWYeoYf-OdqeVvCfgrYA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*K_Iif14NoqYip9CN7QXCFw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*vEHZ4Sm_GLDkkRyagsDUgw.jpeg)

Nous avons décidé d'utiliser un microphone omnidirectionnel plus puissant. Actuellement, vous devez parler à quelques centimètres du microphone pour être compris par le robot. Maintenant, l'objectif est que le robot comprenne les commandes même si la personne parle à un mètre de distance.

Les gens se frustrent lorsque Robbie ne comprend pas. Cela dépend beaucoup des conditions sonores de la pièce.

Une conversation va dans les deux sens. Améliorer le système audio est également l'une des principales priorités. Selon l'ambiance de la pièce, même lorsque Robbie comprend la personne, l'interaction n'est pas amusante lorsque la personne ne comprend pas Robbie.

Nous avons également détruit des batteries parce que nous avons accidentellement laissé le robot allumé sans le vérificateur de batterie branché. Les batteries se sont déchargées au-delà du seuil. Ce fut une expérience d'apprentissage très coûteuse pour nous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rW1NRyRizYpMDe4a4zAyCw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*ABIUhvk1tQ7ZnngFWOeWrg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*nHtN7tWVVIsYpDrP51KiNQ.jpeg)

Les bras du robot sont également une source majeure de problèmes. Les bras n'ont pas été conçus mécaniquement correctement. Ils sont très fragiles, si fragiles que le simple transport du robot les use considérablement. Parfois, un bras tombait et c'était une corvée de le remettre en place.

Nous devons concevoir le bras non seulement pour qu'il soit plus robuste, mais aussi plus modulaire pour qu'il soit facile à remettre en place s'il tombe.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W8r5hxh0w1NFzbf9ZkrjiA.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*YmnvLYOmCgq8Ydf4g1GKlg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*4qO0oWAYqXCrrg-L0B2Wqw.jpeg)

En parlant de modularité et de problèmes, le dépannage de l'électronique du robot était le processus le plus douloureux de tous. Accéder à l'électronique n'était pas une tâche facile, car il n'y a pas de "porte d'accès facile" et les cartes étaient simplement percées partout.

Vous devez démonter la tête du robot de 20 kg juste pour y glisser un multimètre. C'était horrible. Je ne peux pas insister assez sur ce point. La prochaine fois que je construirai un robot, concevoir pour la modularité et la facilité de dépannage sera en tête de ma liste de priorités. S'il y a un "code propre", il y a aussi une "intégration et un assemblage électronique propres".

Une électronique mal intégrée peut fonctionner. Mais si les choses ne sont pas assemblées ou organisées de manière réfléchie, lorsque quelque chose ne va pas, personne ne voudra réparer votre robot.

![Image](https://cdn-media-1.freecodecamp.org/images/1*VLwI5e6qmptXA8gWGHsLSQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*jQBMRB3qKo8Y8IztKD8b8g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*GlbFsRr8XaA3iMrT_s8YaA.jpeg)

### Conclusion

Voilà, mes trois principaux enseignements.

Premièrement, il est plus facile que jamais de construire un robot sophistiqué avec des pièces toutes faites. Tout cela grâce à la communauté du matériel open-source (OSHW). Construire un robot est possible parce que nous nous appuyons sur les épaules généreuses de géants.

Deuxièmement, les idées de conception de "code propre" sont cruciales pour construire un robot que vous aimerez et sur lequel vous voudrez travailler.

Enfin, mais non des moindres, vous devez apprendre par l'expérience, les itérations continues et les retours utilisateurs pour obtenir une bonne expérience utilisateur pour vos produits.

Je remercie mon ancien employeur de m'avoir donné l'opportunité de grandir et de travailler sur des projets passionnants. Être technologue créatif dans une agence de publicité a vraiment été une grande expérience d'apprentissage.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sVa4kAS2dueSvy-OzbvtGA.jpeg)

Crédits

* Tel Castillo — Designs d'affiches
* Apol Sta Maria — Direction créative, design et animation du robot
* Beaucoup d'autres personnes, dont Dom De Leon, JR Ignacio, Axel Raymundo, Merlee Jayme, Alex Syfu, Owel Alvero, Jopy, Cyri, Cathy, Bonat...

![Image](https://cdn-media-1.freecodecamp.org/images/1*Oc4X-6kCJgUMCh63AeP9_g.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*yOUdk_ouqeS7agPeMJlz2Q.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*PtnqkSJsedi_Ye62rxUWdA.jpeg)