---
title: Bricoler le défi de la corde à sauter de Mario Odyssey
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T07:18:28.000Z'
originalURL: https://freecodecamp.org/news/mario-jump-rope-challenge-f7bb44faf6bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gch8CVKbhZiqMqD0ZgB6OA.jpeg
tags:
- name: arduino
  slug: arduino
- name: gaming
  slug: gaming
- name: nintendo
  slug: nintendo
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: Bricoler le défi de la corde à sauter de Mario Odyssey
seo_desc: 'By Antin Harasymiv

  Super Mario Odyssey is quite possibly my favorite Mario game. So much so that I
  went out of my way to complete every last challenge. But one of them gave me more
  trouble than all the others combined: Jump-Rope Genius in the Metro K...'
---

Par Antin Harasymiv

[Super Mario Odyssey](https://www.nintendo.com/games/detail/super-mario-odyssey-switch) est probablement mon jeu Mario préféré. Tellement que j'ai fait tout mon possible pour compléter chaque dernier défi. Mais l'un d'eux m'a donné plus de fil à retordre que tous les autres combinés : _Génie de la corde à sauter_ dans le Royaume Metro.

Vous n'avez même pas besoin de bouger. Vous devez simplement sauter avec succès 100 fois de suite. Mais le truc, c'est que tous les cinq sauts, ça accélère jusqu'à 50, jusqu'à ce que vous sautiez presque deux fois par seconde. Appuyez sur sauter trop tôt et vous échouez. Appuyez sur sauter trop tard et vous échouez. Appuyez sur sauter trop longtemps et... vous l'avez deviné, vous échouez.

Après quelques dizaines de tentatives infructueuses, j'ai commencé à plaisanter en disant que je construirais simplement quelque chose pour le battre à ma place... et au fil des jours, alors que je n'avais toujours pas terminé le défi, mes plaisanteries sont devenues plus sérieuses et j'ai commencé à me demander comment faire.

Ma première pensée était de simplement programmer un Arduino pour relier les connecteurs du bouton de saut sur une manette de Switch, mais heureusement, j'ai d'abord vérifié le [démontage iFixit](https://www.ifixit.com/Teardown/Nintendo+Switch+Teardown/78263#s156437) car les manettes Nintendo depuis la Wii utilisent des interrupteurs à dôme au lieu des plots en caoutchouc conducteurs, ce qui rend cela impossible (pour une lecture amusante, voir l'[évolution](https://www.fictiv.com/blog/posts/nintendo-controller-teardown-part-1) des manettes Nintendo au fil des ans).

![Image](https://cdn-media-1.freecodecamp.org/images/1*s7mqVpMJHtFRFflTAETHTQ.jpeg)
_Manette Joy-Con de la Switch_

Je réfléchissais à acheter une ancienne manette GameCube (avec adaptateur) qui serait facile à pirater, ou à utiliser un solénoïde pour appuyer physiquement sur un bouton d'une manette de Switch, les deux solutions semblaient viables, mais après avoir été surenchéri sur les premières manettes GameCube vendues sur eBay, j'ai opté pour la solution du solénoïde.

Après avoir complété 835 des 836 défis uniques de Mario, j'ai tourné toute mon attention vers la dernière lune. Pour programmer quelque chose pour le battre, je devrais d'abord mesurer le timing, donc mon intention était d'enregistrer l'écran puis de compter les images. Avant de mettre en place une caméra, j'ai fait quelques tours de pratique, et à ma grande horreur, j'ai réellement battu le truc légitimement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oIzx9GmxYY57vJfq0Ewwyw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*kgB2EcsqurjlAm4Ni9DmLQ.jpeg)

Ayant passé deux semaines à dire à tout le monde que je connaissais que j'allais programmer quelque chose pour le battre (et que la plupart d'entre eux se moquaient de moi), perdre l'excuse de le faire était assez décevant.

Cependant, en tant qu'adulte, j'ai réalisé que je n'avais pas vraiment besoin d'une excuse pour perdre mon temps et mon argent (c'est à peu près tout ce que nous faisons), donc j'ai commandé en express un Arduino et les composants nécessaires pour commencer mon projet.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0shSlQ9GLpAK7fVEDPt5Pw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*JFaR8nH_b25ZIcFEt7w0WA.jpeg)

La première étape était de comprendre comment utiliser un Arduino, ce qui... était en fait assez simple, l'éditeur en ligne et les tutoriels sont super faciles, et après avoir programmé quelques LEDs clignotantes, je me sentais prêt à partir. Le plus grand obstacle était en fait de trouver un câble USB-B car honnêtement, qui utilise encore ceux-là ?

La deuxième étape était de comprendre le timing, et je me suis rendu la tâche impressionnamment difficile. Je pensais être malin en enregistrant depuis la vue aérienne, et je pourrais utiliser le pied de la femme pour aligner les images, quand _sa main touchait son pied_, j'appellerais cela une révolution, et j'ai laborieusement passé en revue QuickTime en appuyant sur les touches fléchées pour avancer image par image et compter _un, deux, trois... soixante-huit, soixante-neuf, soixante-dix_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*78Sfthm-0pj58nvXBZwiIw.png)
_L'image du milieu montre sa main alignée avec son pied_

La deuxième étape et demie était de réaliser que le compteur de sauts était une mesure plus fiable, et que Final Cut Pro me montrerait le temps et le compteur d'images, me permettant de parcourir très rapidement la vidéo.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkMIRmBft5rUN-yusYEV4g.png)
_Final Cut Pro_

Faites cela 50 fois... et mettez tous les résultats dans une feuille de calcul et vous avez le secret du succès de la corde à sauter. Ces 50 derniers sauts ? Vous devez en faire un tous les 0,58 secondes.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PB9TdFtO9Ynh6KDxs479HA.png)
_Timings mesurés pour le défi de la corde à sauter de Mario_

Avec les timings terminés, j'ai tourné mon attention vers la moitié électronique du problème, et heureusement, quelqu'un qui comprend l'électronique (ce qui n'est définitivement pas mon cas) avait déjà [partagé](https://core-electronics.com.au/tutorials/solenoid-control-with-arduino.html) comment contrôler un solénoïde avec un Arduino.

Pour ceux qui ne savent pas, un solénoïde est vraiment juste une bobine cylindrique de fil qui, lorsque vous y faites passer un courant, produit un champ magnétique. Le nom est interchangeable avec quelques choses qui utilisent des solénoïdes (la partie bobine) pour faire quelque chose de plus complexe, dans ce cas, pousser une petite tige métallique. Allumez l'alimentation et la tige sort, éteignez-la et le ressort la ramène.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pr51iD0DzPoSdwbPF8OIJQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EjyP9Ed764JVtIijnU53Hw.png)
_Circuit terminé_

J'ai câblé un circuit avec un simple interrupteur et un solénoïde, et j'ai écrit un programme qui bouclerait et le déclencherait, réduisant progressivement le timing au fur et à mesure. Basculer l'interrupteur démarrerait la boucle, l'éteindre la réinitialiserait.

Cela me permettrait de faire courir Mario manuellement en position et de basculer l'interrupteur pour démarrer, et aussi de me donner un moyen facile de réessayer si je me trompais (ce que j'anticipais serait souvent). Après quelques heures (et quelques conseils de mon frère), j'avais un circuit fonctionnel !

À ce stade, j'avais essentiellement supposé le succès, puis la réalité a frappé (ou plutôt, m'a frappé). Dans ma naïveté, j'avais supposé que le solénoïde serait capable de presser trivialement un bouton de la Switch, celui que j'ai [acheté](https://www.adafruit.com/product/2776) était un solénoïde 5V capable de déplacer 3mm et d'appliquer 80 grammes de force, ce qui semblait beaucoup (c'est en fait moins d'un newton).

Je l'ai tenu contre la manette et... rien. Aucun mouvement, le bouton refusait de bouger. Googler pour savoir combien de force est nécessaire pour presser un bouton de manette de Switch n'a donné aucun résultat, et autour de ma maison, je n'avais aucun bon outil pour le mesurer.

Alors, sans bons outils, je suis parti à la recherche de quelques mauvais.

Et les mesures de cuisine ? J'ai rempli 1/3 de tasse d'eau et j'ai équilibré cela au-dessus d'un bouton, aucun mouvement. J'ai rempli 1/2 tasse d'eau et cela a pressé. Donc voilà votre réponse, un bouton Joy-Con a besoin de quelque part entre un tiers et une demi-tasse d'eau.

En les reconvertissant en unités réelles, 1 tasse = 250 ml et la chose facile à propos du système métrique est que le poids est dérivé du volume d'eau. 250 ml est 250 grammes, donc mon Joy-Con avait besoin de quelque part entre 83 grammes et 125 grammes pour presser.

Soudain, mon solénoïde de 80 grammes ne semblait plus si sous-alimenté, et si je... le suralimentais ? Je lui donnais les 5 volts qu'il demandait, mais j'avais une alimentation de 9 volts. La force magnétique d'un solénoïde augmente avec la tension (en fait, elle augmente avec le carré de la tension) donc à 9 volts, mon solénoïde devrait appliquer plus près de 250 grammes, ou comme j'aime à y penser, 1 tasse d'eau !

La quatrième étape impliquait de fixer le solénoïde à la manette. Étant donné le peu de réflexion que j'avais mis dans la planification de cette partie, ce n'était pas une surprise de voir à quel point la solution s'est avérée inefficace. Quelques morceaux de bois l'ont surélevé au-dessus des autres boutons, quelques morceaux de ruban électrique ont maintenu le bois en place, et un élastique a gardé le solénoïde en position.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mLSWqLee2C3Zc0Y8X6nwtg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*L854swGhbWdtOrJPuTAXog.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gch8CVKbhZiqMqD0ZgB6OA.jpeg)

J'étais enfin prêt à tout mettre à l'épreuve, je me suis téléporté dans le Royaume Metro, j'ai couru jusqu'au défi, et je me suis préparé à me délecter de la douce gloire de mon succès suffisant.

Et j'ai presque immédiatement échoué... Mon timing était faux. J'ai manuellement ajusté quelques-uns des timings dans mon code et j'ai rapproché Mario, encore plus près, et encore plus près, jusqu'à ce qu'il puisse atteindre 86 de manière assez fiable.

À ce stade, au lieu d'ajuster les choses au hasard, je l'ai enregistré en train de jouer et je suis retourné à Final Cut Pro pour recompter les images (cette fois en me concentrant sur le nombre d'images plus proches/plus éloignées que la corde obtenait par segment de 5 sauts), et bien que j'étais un peu décalé à quelques endroits, comme Mario atteignait toujours 50, la seule chose nécessitant un changement était le timing 50+. Je l'ai réduit à un saut toutes les 35,2 images et j'ai réessayé.

Succès ! 261 sauts. Cela semblait être une énorme victoire, vous pouvez voir dans la vidéo qu'il a facilement écrasé mon maigre effort humain de 102 sauts. Je suis immédiatement allé réveiller ma femme et j'ai essayé de lui expliquer à quel point c'était cool, et quand cela n'a pas réussi à me valoir beaucoup d'adulation, j'ai eu recours à le dire à mon frère qui a été beaucoup plus impressionné de manière appropriée.

Cependant, c'est un robot, pourquoi 261 devrait-il être une limite ? Pourquoi ne peut-il pas être parfait ? J'ai analysé les images à nouveau et j'ai remarqué que la corde rattrapait Mario très lentement, il devait aller plus vite !

![Image](https://cdn-media-1.freecodecamp.org/images/1*sFulRlhZB9oPR4iLwzD8vQ.png)
_Timings de saut, la moyenne a été mesurée, l'actuel est ce qui est dans le code_

Réduire le timing d'un saut toutes les 35,2 images à un toutes les 35,15 images (un changement de seulement 0,14%) a résulté en un Mario beaucoup plus réussi.

Si réussi qu'il a pu jouer au défi infuriant de la corde à sauter de Mario pendant 35 minutes et 21 secondes avant d'échouer... établissant un nouveau record (pour moi) de 3613.

Au début, j'ai supposé qu'il avait échoué parce que mon timing était encore imperceptiblement faux, mais en inspectant de plus près la vidéo, il est resté parfaitement synchronisé jusqu'à ce qu'il... appuie longtemps ! Quelle erreur humaine pour un ordinateur de faire, au lieu de faire un saut court et rapide, il a maintenu le bouton trop longtemps et a envoyé Mario trop haut, il a sauté au bon moment mais a atterri en retard.

En réalité, je pense que c'est que le pauvre solénoïde surchauffait, plus tôt dans la soirée alors que je jouais avec les timings, il avait cessé de fonctionner aussi bien, je pense que le faire fonctionner à presque deux fois la tension était problématique. Dans la vidéo, vous pouvez même voir qu'il a appuyer une deuxième fois pendant le saut au bon timing.

Quant au code ? C'était la partie la plus simple. Un simple 76 lignes de code peuvent jouer à Mario mieux que moi

![Image](https://cdn-media-1.freecodecamp.org/images/1*qxpqBkhYlTgMUgbiAkDihg.png)

Pour simplifier, j'ai mesuré tous les timings en nombre d'images entre les sauts, je pouvais compter les images facilement dans la vidéo, puis il suffisait de diviser par 60 pour transformer cela en secondes.

Le code calcule tout en utilisant la navigation à l'estime à partir du moment où le défi a commencé, j'ai supposé que les imprécisions dans le déclenchement de n'importe quel saut s'équilibreraient. À chaque boucle, le code calcule combien de millisecondes devraient s'être écoulées avant le saut suivant et si ce seuil est atteint, il active le solénoïde ; il y a une courte durée pendant laquelle il garde le solénoïde activé avant de le réinitialiser (peut-être devait-il être plus court pour éviter l'appui long).

Et c'est tout... presque stupidement simple, de manière appropriée, étant donné la nature du défi de saut.

Je pourrais réessayer mais à presque 40 minutes par tentative, je ne suis tout simplement pas assez intéressé. De plus, j'ai depuis découvert que [quelqu'un](https://www.youtube.com/watch?v=hu3HEwc6Pwk) est allé un pas plus loin que moi, bien que dans une direction légèrement différente.

Au lieu d'appuyer physiquement sur un bouton de leur manette, ils utilisent une bibliothèque pour simuler être une manette, ce qui leur permet d'envoyer des signaux de manière triviale. Lorsqu'ils ont rencontré le même défi de timing que moi (en n'obtenant que quelques centaines de sauts avant d'échouer — ils utilisaient le 35,18 constant pour leurs derniers sauts), ils l'ont résolu en surveillant de manière programmatique le signal vidéo, en vérifiant la zone de score et en faisant un autre saut lorsqu'il change. Avec cette méthode, ils peuvent atteindre le score maximum de 99 999 !

Vous penseriez qu'avec tout cela, j'aurais l'un des scores les plus élevés du jeu... vous auriez tort ! Il y a seulement une semaine, j'aurais probablement été dans le top 100, mais un bug a été découvert dans le jeu qui permet à n'importe qui de tricher ce défi, avec presque aucun effort, vous pouvez obtenir des sauts illimités et plus de 10 000 personnes l'ont maintenant fait. Peut-être que si Nintendo corrige cela et réinitialise le tableau des scores, je dépoussiérerai mon solénoïde à nouveau, je pense que si vous pouvez construire quelque chose pour jouer au jeu en utilisant uniquement la manette elle-même, alors c'est un peu légitime.