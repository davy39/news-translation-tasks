---
title: Programmeurs macho, mémoire à tambour et une analyse médico-légale du code
  machine des années 1960
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-02T11:40:08.000Z'
originalURL: https://freecodecamp.org/news/macho-programmers-drum-memory-and-a-forensic-analysis-of-1960s-machine-code-6c5da6a40244
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ch1IHMJg5qHV050mUiLjDw.jpeg
tags:
- name: history
  slug: history
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Programmeurs macho, mémoire à tambour et une analyse médico-légale du code
  machine des années 1960
seo_desc: 'By David Nugent

  Real programmers don’t use PASCAL

  Programmers today build distributed applications and artificial neural networks.
  They use functional reactive programming, open source web frameworks, and serverless
  environments. Yet, impostor syndro...'
---

Par David Nugent

### Les vrais programmeurs n'utilisent pas PASCAL

Les programmeurs d'aujourd'hui créent des applications distribuées et des réseaux de neurones artificiels. Ils utilisent la programmation réactive fonctionnelle, des frameworks web open source et des environnements serverless. Pourtant, le syndrome de l'imposteur est réel, et les programmeurs se critiquent encore mutuellement pour ne pas être des "vrais programmeurs".

J'ai travaillé comme docent pour le Computer History Museum pendant des années. Le trope du "vrai programmeur" existe depuis le début du logiciel. Et je peux le prouver avec une histoire.

L'histoire commence avec une lettre de 1983, [Real Programmers Don’t Use PASCAL](http://web.mit.edu/humor/Computers/real.programmers), écrite par Ed Post. La lettre a été publiée dans Datamation et discutait du côté "macho" de la programmation. Elle taquinait ceux qui méprisent les utilisateurs de langages de haut niveau comme **non** "vrais programmeurs".

[The Story of Mel](http://www.catb.org/jargon/html/story-of-mel.html) est une réponse en ligne à cette lettre. Elle a été postée sur Usenet le 21 mai 1983 par [Ed Nather](https://en.wikipedia.org/wiki/Ed_Nather).

Mel et Ed étaient collègues dans une entreprise de machines à écrire qui s'était diversifiée dans la construction d'ordinateurs. Leur succès phare était le [LGP-30](http://www.computerhistory.org/revolution/early-computer-companies/5/116) : un [ordinateur à mémoire à tambour](https://en.wikipedia.org/wiki/Drum_memory) avec un clavier Flexowriter et un lecteur de bande papier. (L'image d'en-tête de cet article est le tableau de bord d'un LGP-30.) Mel a été chargé de réécrire un programme populaire pour l'ordinateur successeur, le RPC-4000.

> Port ? Qu'est-ce que cela signifie ?

Après le départ de Mel de l'entreprise, Ed a été chargé de réécrire une partie de ce programme. Dans l'histoire, il découvre une boucle infinie dans le code, qui, d'une manière ou d'une autre, n'empêche pas le programme de fonctionner :

> Peut-être que mon plus grand choc est venu lorsque j'ai trouvé une boucle innocente qui n'avait aucun test. 
> Aucun test. Aucun. 
> Le bon sens disait que cela devait être une boucle fermée, où le programme tournerait, pour toujours, sans fin. 
> Le contrôle du programme passait directement à travers, cependant, et sortait en toute sécurité de l'autre côté.

Ed a découvert que la boucle fermée provoquait un débordement, qui réécrivait le code d'instruction. Le résultat du débordement était une instruction de **saut**, déplaçant le contrôle du programme vers un autre emplacement mémoire.

C'est une grande histoire. Mais est-elle véridique ?

### Analyse médico-légale du code : L'histoire est-elle véridique ?

Notre première étape consiste à rechercher des détails techniques de la machine pour laquelle le programme a été écrit. Bien que l'histoire mentionne abondamment le LGP-30, le programme fonctionnait en réalité sur un RPC-4000. (Rappelez-vous, il devait être réécrit pour cette nouvelle machine.)

Les deux machines utilisaient la mémoire à tambour pour le stockage des programmes. (Fait amusant : l'équivalent approximatif de votre disque dur moderne était la mémoire à tambour, la bande papier, les cartes perforées ou la bande magnétique !) Une seule ligne de têtes électromagnétiques lisait/écrivait les données tandis que le tambour tournait à une vitesse constante en dessous. Voici une référence visuelle :

![Image](https://cdn-media-1.freecodecamp.org/images/zJIzg5uyEQoFMEUDYz9gmS1SWMgNoRgksyeg)
_Diagramme de la mémoire à tambour. Source : [Manuel RPC-4000](https://archive.org/details/bitsavers_royalPrecirogrammingManual_8537458" rel="noopener" target="_blank" title=")_

Les données étaient stockées et récupérées à partir des différents secteurs et pistes du tambour. Pour en savoir plus sur le format des données, nous pouvons consulter [le manuel de programmation du RPC-4000](https://archive.org/details/bitsavers_royalPrecirogrammingManual_8537458), que archive.org a numérisé et préservé en ligne.

À la page 20 du manuel, nous trouvons le diagramme suivant du format des mots de données :

![Image](https://cdn-media-1.freecodecamp.org/images/7vhFSaJoslnlHki9MxXaOymDWxKfin32mF7X)
_Diagrammes du format des mots du RPC-4000_

Le mot de commande se décompose en :

* 5 bits pour la commande
* 13 bits pour l'emplacement de la piste/secteur de l'opérande
* 13 bits pour la piste/secteur de l'adresse de la commande suivante

Le bit 31 est le **tag d'index** qui, lorsqu'il est activé, activait le registre d'index :

> [Le registre d'index] permettait au programmeur d'écrire une boucle de programme qui utilisait une instruction indexée à l'intérieur ; à chaque passage, le nombre dans le registre d'index était ajouté à l'adresse de cette instruction, de sorte qu'elle se référerait à la donnée suivante dans une série.

L'histoire mentionne que le "bit d'index" est "_le bit qui se trouvait entre l'adresse et le code d'opération dans le mot d'instruction_." Pourtant, le diagramme ci-dessus montre que le bit de tag d'index est en réalité au bit 31, après la commande et les adresses. Personnellement, je mets cela sur le compte d'un mauvais souvenir de l'auteur dans les années entre le moment où il a examiné le code et le moment où l'histoire a été enregistrée.

Heureusement, cela n'affecte pas l'aspect de débordement de l'histoire. Puisque le mot d'instruction était tiré en mémoire et incrémenté, le bit d'index devait encore être activé **on** pour que l'incrément provoque un débordement de l'**Adresse Suivante**.

Pour recréer les mots d'instruction dans la boucle, nous devons en savoir plus sur le fonctionnement du programme. Voici une citation de la partie critique de l'histoire :

> Il avait situé les données sur lesquelles il travaillait près du haut de la mémoire — 
> les plus grands emplacements que les instructions pouvaient adresser — 
> donc, après que la dernière donnée ait été traitée, l'incrémentation de l'adresse d'instruction la ferait déborder. 
> Le report ajouterait un au code d'opération, le changeant en suivant dans le jeu d'instructions : une instruction de saut. 
> En effet, la prochaine instruction du programme était à l'emplacement d'adresse zéro, et le programme continuait joyeusement son chemin.

### Implémentation hypothétique : "Montrez-moi les bits !"

Voici une instruction potentielle qui pourrait être l'**instruction de saut** mentionnée dans l'histoire :

![Image](https://cdn-media-1.freecodecamp.org/images/YTmPExJNbmY8-Kx2r3UTaJSJ311QxjRn2Fc4)

Nous pouvons voir que les bits de commande sont **10111**. Si **Branch Control** est désactivé, "la prochaine instruction est celle spécifiée dans le champ Next-address." Donc une situation hypothétique serait que, après le débordement, le registre (en utilisant des pipes pour dénoter les séparations entre les champs de bits) lisait :

**10111 | 0000000| 0000000 | 0**

En extrapolant en arrière, avant l'incrément et le débordement, le registre aurait lu :

**10110 | 1111111 | 1111111 | 1**

Un effet secondaire intéressant de travailler sur cette implémentation est que l'instruction utilisée n'a pas vraiment d'importance. Chaque instruction dans le RPC-4000 inclut l'adresse de l'instruction suivante. Un débordement dans le bit d'index vers le champ d'adresse suivante entraînera un saut à cette adresse indépendamment des bits de commande.

### Épilogue

![Image](https://cdn-media-1.freecodecamp.org/images/MiGjYka4199vjdbxDAskYWf9anRYPPUg72Ev)
_Photo de groupe de l'Août 1956 Librazette_

Mel Kaye (debout, à l'extrême droite) a continué à travailler et a finalement pris sa retraite. Un fan nommé Anthony Cuozzo a posté en 2014 qu'il avait essayé de prendre contact avec Mel :

> J'ai finalement réussi à prendre contact avec Mel, mais je l'ai malheureusement effrayé. C'est une histoire pour un autre jour... :-/ ([source](https://news.ycombinator.com/item?id=7869771))

Par respect pour la vie privée de Mel, je ne posterai aucune information personnelle et je m'en tiendrai au programme et à l'histoire. Si quelqu'un sait comment Mel ressent sa célébrité sur Internet, j'aimerais avoir de vos nouvelles.

> Je n'ai pas gardé contact avec Mel, donc je ne sais pas s'il a jamais cédé à la vague de changements qui a submergé les techniques de programmation depuis ces jours lointains. J'aime à penser qu'il ne l'a pas fait. — Ed Nather

_Sources supplémentaires :_

* [_Page Wikipedia sur l'histoire de Mel_](https://en.wikipedia.org/wiki/The_Story_of_Mel)
* [_Manuel de Mel pour le jeu de blackjack RPC-4000_](http://bitsavers.trailing-edge.com/pdf/royalPrecision/RPC-4000/programWriteups/W1-01.0_Blackjack_Game.pdf)
* [_La vérité ne se met jamais en travers d'une bonne histoire_](https://books.google.com/books?id=PhkINW48_J0C) _par Jan Howard Brunvand_

[Dave](https://twitter.com/drnugent) travaille dans les relations avec les développeurs chez IBM. Pour une raison quelconque, IBM n'a pas de SDK pour le RPC-4000.