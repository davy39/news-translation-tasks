---
title: Comprendre les machines à états
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-11T23:02:53.000Z'
originalURL: https://freecodecamp.org/news/state-machines-basics-of-computer-science-d42855debc66
coverImage: https://cdn-media-1.freecodecamp.org/images/0*3QzqRMfRCh28-xe1.
tags:
- name: Computer Science
  slug: computer-science
- name: finite state machine
  slug: finite-state-machine
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
seo_title: Comprendre les machines à états
seo_desc: 'By Mark Shead

  An intro to Computer Science concepts

  Computer science enables us to program, but it is possible to do a lot of programming
  without understanding the underlying computer science concepts.

  This isn’t always a bad thing. When we program, ...'
---

Par Mark Shead

#### Une introduction aux concepts de l'informatique

L'informatique nous permet de programmer, mais il est possible de faire beaucoup de programmation sans comprendre les concepts sous-jacents de l'informatique.

Ce n'est pas toujours une mauvaise chose. Lorsque nous programmons, nous travaillons à un niveau d'abstraction beaucoup plus élevé.

Lorsque nous conduisons une voiture, nous ne nous préoccupons que de deux ou trois pédales, d'un levier de vitesses et d'un volant. Vous pouvez conduire une voiture en toute sécurité sans avoir la moindre idée de son fonctionnement.

Cependant, si vous voulez conduire une voiture aux limites de ses capacités, vous devez en savoir beaucoup plus sur les automobiles que simplement les trois pédales, le levier de vitesses et le volant.

Il en va de même pour la programmation. Beaucoup de travail quotidien peut être accompli avec peu ou pas de compréhension de l'informatique. Vous n'avez pas besoin de comprendre la théorie computationnelle pour créer un formulaire "Contactez-nous" en PHP.

Cependant, si vous prévoyez d'écrire du code qui nécessite un calcul sérieux, vous devrez comprendre un peu mieux comment le calcul fonctionne sous le capot.

Le but de cet article est de fournir quelques bases fondamentales pour le calcul. Si cela suscite de l'intérêt, je pourrais suivre avec des sujets plus avancés, mais pour l'instant, je veux examiner la logique derrière l'un des dispositifs computationnels abstraits les plus simples — une **machine à états finis**.

### Machines à états finis

Une machine à états finis est une abstraction mathématique utilisée pour concevoir des algorithmes.

En termes plus simples, une machine à états lira une série d'entrées. Lorsqu'elle lit une entrée, elle passera à un état différent. Chaque état spécifie à quel état passer, pour une entrée donnée. Cela semble compliqué, mais c'est en réalité assez simple.

Imaginez un dispositif qui lit une longue bande de papier. Pour chaque pouce de papier, il y a une seule lettre imprimée dessus — soit la lettre 'a', soit la lettre 'b'.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xO3Fuvo1mL-jczfC.)
_Une bande de papier, avec huit lettres imprimées dessus_

Alors que la machine à états lit chaque lettre, elle change d'état. Voici une machine à états très simple :

![Image](https://cdn-media-1.freecodecamp.org/images/0*msRB3BVpVkGVgEOd.)

Les cercles sont les "**états**" dans lesquels la machine peut se trouver. Les flèches sont les **transitions**. Donc, si vous êtes dans l'état _s_ et que vous lisez un 'a', vous passerez à l'état _q_. Si vous lisez un 'b', vous resterez dans l'état _s_.

Donc, si nous commençons par _s_ et que nous lisons la bande de papier ci-dessus de gauche à droite, nous lirons le 'a' et passerons à l'état _q_.

Ensuite, nous lirons 'b' et reviendrons à l'état _s_.

Un autre 'b' nous maintiendra sur _s_, suivi d'un 'a' — ce qui nous ramène à l'état _q_. Assez simple, mais quel est l'intérêt ?

Eh bien, il s'avère que vous pouvez faire passer une bande à travers la machine à états et en dire quelque chose sur la séquence de lettres, en examinant l'état dans lequel vous vous trouvez à la fin.

Dans notre machine à états simple ci-dessus, si nous finissons dans l'état _s_, la bande doit se terminer par une lettre 'b'. Si nous finissons dans l'état _q_, la bande se termine par la lettre 'a'.

Cela peut sembler inutile, mais il existe un _énorme nombre_ de problèmes qui peuvent être résolus avec ce type d'approche. Un exemple très simple serait de déterminer si une page HTML contient ces balises dans cet ordre :

```
<html>   <head> </head>   <body> </body> </html>
```

La machine à états peut passer à un état qui montre qu'elle a lu la balise html, boucler jusqu'à ce qu'elle atteigne la balise head, boucler jusqu'à ce qu'elle atteigne la balise de fermeture head, et ainsi de suite.

Si elle parvient avec succès à l'état final, alors vous avez ces balises particulières dans le bon ordre.

Les machines à états finis peuvent également être utilisées pour représenter de nombreux autres systèmes — tels que la mécanique d'un parcmètre, d'un distributeur automatique, d'une pompe à essence automatisée, et toutes sortes d'autres choses.

### Machines à états finis déterministes

Les machines à états que nous avons examinées jusqu'à présent sont toutes des machines à états **déterministes**. À partir de n'importe quel état, il n'y a qu'_une_ seule transition pour toute entrée autorisée. En d'autres termes, il ne peut pas y avoir deux chemins sortant d'un état lorsque vous lisez la lettre 'a'. À première vue, cela semble ridicule de faire cette distinction.

À quoi bon un ensemble de décisions si la même entrée peut entraîner le passage à plus d'un état ? Vous ne pouvez pas dire à un ordinateur, `si x == vrai` alors exécutez `doSomethingBig` ou exécutez `doSomethingSmall`, n'est-ce pas ?

Eh bien, vous pouvez en quelque sorte avec une machine à états.

La sortie d'une machine à états est son état final. Elle effectue tout son traitement, puis l'état final est lu, et **ensuite** une action est déclenchée. Une machine à états ne **fait** rien lorsqu'elle passe d'un état à un autre.

Elle traite, et lorsqu'elle arrive à la fin, l'état est lu et quelque chose d'externe déclenche l'action souhaitée (par exemple, distribuer une canette de soda). C'est un concept important lorsqu'il s'agit de machines à états finis **non déterministes**.

### Machines à états finis non déterministes

Les machines à états finis non déterministes sont des machines à états finis où une entrée donnée à partir d'un état particulier peut conduire à **plus d'un** état différent.

Par exemple, supposons que nous voulons construire une machine à états finis qui peut reconnaître des chaînes de lettres qui :

* Commencent par la lettre 'a'
* et sont suivies par zéro ou plusieurs occurrences de la lettre 'b'
* ou, zéro ou plusieurs occurrences de la lettre 'c'
* sont terminées par la lettre suivante de l'alphabet.

Les chaînes valides seraient :

* abbbbbbbbbc
* abbbc
* acccd
* acccccd
* ac (zéro occurrence de b)
* ad (zéro occurrence de c)

Elle reconnaîtra donc la lettre 'a' suivie de zéro ou plusieurs occurrences de la même lettre 'b' ou 'c', suivie de la lettre suivante de l'alphabet.

Une façon très simple de représenter cela est avec une machine à états qui ressemble à celle ci-dessous, où un état final de _t_ signifie que la chaîne a été acceptée et correspond au motif.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3QzqRMfRCh28-xe1.)
_Machine à états finis de reconnaissance de motifs_

Voyez-vous le problème ? À partir du point de départ _s_, nous ne savons pas quel chemin prendre. Si nous lisons la lettre 'a', nous ne savons pas si nous devons aller à l'état _q_ ou _r_.

Il existe plusieurs façons de résoudre ce problème. L'une d'elles est le retour en arrière. Vous prenez simplement tous les chemins possibles, et ignorez ou revenez en arrière sur ceux où vous êtes bloqué.

C'est essentiellement ainsi que fonctionnent la plupart des ordinateurs jouant aux échecs. Ils examinent toutes les possibilités — et toutes les possibilités de ces possibilités — et choisissent le chemin qui leur donne le plus grand nombre d'avantages sur leur adversaire.

L'autre option est de convertir la machine non déterministe en une machine déterministe.

L'un des attributs intéressants d'une machine non déterministe est qu'il existe un algorithme pour transformer toute machine non déterministe en une machine déterministe. Cependant, cela est souvent beaucoup plus compliqué.

Heureusement pour nous, l'exemple ci-dessus n'est que légèrement plus compliqué. En fait, celui-ci est suffisamment simple pour que nous puissions le transformer en une machine déterministe dans notre tête, sans l'aide d'un algorithme formel.

La machine ci-dessous est une version déterministe de la machine non déterministe ci-dessus. Dans la machine ci-dessous, un état final de _t_ ou _v_ est atteint par toute chaîne acceptée par la machine.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Sp_eR3qz6X2w-vPo.)
_Une machine à états finis déterministe_

Le modèle non déterministe a quatre états et six transitions. Le modèle déterministe a six états, dix transitions et deux états finaux possibles.

Ce n'est pas beaucoup plus, mais la complexité augmente généralement de manière exponentielle. Une machine non déterministe de taille modérée peut produire une machine déterministe absolument _énorme_.

### Expressions régulières

Si vous avez fait de la programmation, vous avez probablement rencontré des expressions régulières. Les expressions régulières et les machines à états finis sont fonctionnellement équivalentes. Tout ce que vous pouvez accepter ou faire correspondre avec une expression régulière peut être accepté ou fait correspondre avec une machine à états.

Par exemple, le motif décrit ci-dessus pourrait être fait correspondre avec l'expression régulière : `a(b*c|c*d)`

Les expressions régulières et les machines à états finis ont également les mêmes limitations. En particulier, elles ne peuvent toutes deux faire correspondre ou accepter que des motifs qui peuvent être gérés avec une mémoire finie.

Alors, quel type de motifs ne peuvent-elles pas faire correspondre ? Supposons que vous souhaitiez faire correspondre uniquement des chaînes de 'a' et 'b', où il y a un certain nombre de 'a' suivis d'un nombre égal de 'b'. Ou _n_ 'a' suivis de _n_ 'b', où _n_ est un nombre.

Les exemples seraient :

* ab
* aabb
* aaaaaabbbbbb
* aaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbb

À première vue, cela semble être un travail facile pour une machine à états finis. Le problème est que vous allez rapidement manquer d'états, ou vous devrez supposer un nombre infini d'états — à ce moment-là, ce n'est plus une machine à états _finis_.

Supposons que vous créiez une machine à états finis qui peut accepter jusqu'à 20 'a' suivis de 20 'b'. Cela fonctionne bien, jusqu'à ce que vous obteniez une chaîne de 21 'a' suivis de 21 'b' — à ce moment-là, vous devrez réécrire votre machine pour gérer une chaîne plus longue.

Pour toute chaîne que vous pouvez reconnaître, il en existe une un peu plus longue que votre machine ne peut pas reconnaître parce qu'elle manque de mémoire.

C'est ce qu'on appelle le **Lemme de pompage** qui dit essentiellement : "si votre motif a une section qui peut être répétée (comme celle ci-dessus), alors le motif n'est pas régulier".

En d'autres termes, ni une expression régulière ni une machine à états finis ne peuvent être construites pour reconnaître toutes les chaînes qui _correspondent_ au motif.

Si vous regardez attentivement, vous remarquerez que ce type de motif où chaque 'a' a un 'b' correspondant ressemble beaucoup au HTML. Dans toute paire de balises, vous pouvez avoir n'importe quel nombre d'autres paires de balises correspondantes.

Ainsi, bien que vous puissiez utiliser une expression régulière ou une machine à états finis pour reconnaître si une page HTML contient les éléments `<html>`, `<head>` et `<body>` dans le bon ordre, vous ne pouvez pas utiliser une expression régulière pour dire si une page HTML entière est valide ou non — parce que le HTML n'est pas un motif régulier.

### Machines de Turing

Alors, comment reconnaître les **motifs non réguliers** ?

Il existe un dispositif théorique similaire à une machine à états, appelé Machine de Turing. Elle est similaire à une machine à états finis en ce sens qu'elle a une bande de papier qu'elle lit. Mais une Machine de Turing peut effacer et écrire sur la bande de papier.

Expliquer une Machine de Turing prendra plus d'espace que nous n'en avons ici, mais il y a quelques points importants pertinents pour notre discussion sur les machines à états finis et les expressions régulières.

Les Machines de Turing sont **computationnellement complètes** — ce qui signifie que tout ce qui peut être calculé peut être calculé sur une Machine de Turing.

Puisqu'une Machine de Turing peut écrire ainsi que lire sur la bande de papier, elle n'est pas limitée à un nombre fini d'états. La bande de papier peut être supposée infinie en longueur. Bien sûr, les ordinateurs réels n'ont pas une quantité infinie de mémoire. Mais ils contiennent généralement suffisamment de mémoire pour que vous n'atteigniez pas la limite pour le type de problèmes qu'ils traitent.

Les Machines de Turing nous donnent un dispositif mécanique imaginaire qui nous permet de visualiser et de comprendre comment fonctionne le processus computationnel. Il est particulièrement utile pour comprendre les limites du calcul. Si cela suscite de l'intérêt, je ferai un autre article sur les Machines de Turing à l'avenir.

### Pourquoi est-ce important ?

Alors, quel est l'intérêt ? Comment cela va-t-il vous aider à créer ce prochain formulaire PHP ?

Quelles que soient leurs limitations, les machines à états sont un concept très central en informatique. En particulier, il est significatif que pour toute machine à états non déterministe que vous pouvez concevoir, il existe une machine à états déterministe qui fait la même chose.

C'est un point clé, car cela signifie que vous pouvez concevoir votre algorithme de la manière la plus facile à penser. Une fois que vous avez un algorithme fonctionnel, vous pouvez le convertir dans la forme la plus efficace.

La compréhension que les machines à états finis et les expressions régulières sont fonctionnellement équivalentes ouvre des utilisations incroyablement intéressantes pour les moteurs d'expressions régulières — en particulier lorsqu'il s'agit de créer des règles métiers qui peuvent être modifiées sans recompiler un système.

Une base en informatique vous permet de prendre un problème que vous ne savez pas résoudre et de raisonner : "Je ne sais pas comment résoudre X, mais je sais comment résoudre Y. Et je sais comment convertir une solution pour Y en une solution pour X. Par conséquent, je sais maintenant comment résoudre X."

Si vous aimez cet article, vous pourriez apprécier ma [chaîne YouTube](https://www.youtube.com/markshead) où je crée occasionnellement une vidéo ou un dessin animé sur un aspect de la création de logiciels. J'ai également une [liste de diffusion](http://eepurl.com/uPj05) pour les personnes qui aimeraient recevoir un e-mail occasionnel lorsque je produis quelque chose de nouveau.

Publié à l'origine sur [blog.markshead.com](https://blog.markshead.com/869/state-machines-computer-science/) le 11 février 2018.