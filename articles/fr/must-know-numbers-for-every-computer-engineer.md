---
title: Voici les chiffres que tout ingénieur informaticien devrait connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-14T17:32:57.000Z'
originalURL: https://freecodecamp.org/news/must-know-numbers-for-every-computer-engineer
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/numbers.jpg
tags:
- name: coding
  slug: coding
- name: Computer Science
  slug: computer-science
- name: Google
  slug: google
- name: internet
  slug: internet
- name: technology
  slug: technology
seo_title: Voici les chiffres que tout ingénieur informaticien devrait connaître
seo_desc: 'By Kousik Nath

  In 2010, Jeff Dean from Google gave a wonderful talk at Stanford that made him quite
  famous. In it, he discussed a few numbers that are relevant to computing systems.
  Then Peter Norvig published those numbers for the first time on the ...'
---

Par Kousik Nath

En 2010, [Jeff Dean](https://en.wikipedia.org/wiki/Jeff_Dean_(computer_scientist)) de Google a donné une conférence merveilleuse à Stanford qui l'a rendu assez célèbre. Il y a discuté de quelques chiffres pertinents pour les systèmes informatiques. Ensuite, Peter Norvig a [publié](http://norvig.com/21-days.html) ces chiffres pour la première fois sur Internet.

Le temps a passé, et les chiffres ont changé. Voici une très bonne [interface web interactive](https://people.eecs.berkeley.edu/~rcs/research/interactive_latency.html) de ces chiffres qui montre à peu près comment ils ont changé au fil des ans en fonction du temps.

Cet article n'est pas seulement une compilation des données estimées de Jeff Dean, mais il rassemble tous ces chiffres de différentes sources. Cela devrait vous aider en tant que concepteur et architecte de systèmes. Lors de la conception, vous pouvez utiliser ces chiffres pour estimer la quantité de ressources dont votre système a besoin.

## Estimation approximative des données de latence pour 2019 :

1. Référence au cache L1 : 1 nanoseconde.
2. Référence au cache L2 : 4 nanosecondes.
3. Verrouillage / Déverrouillage de Mutex : 17 nanosecondes.
4. Référence à la mémoire principale / RAM : 100 nanosecondes.
5. Compression de 1 Ko avec Zippy (actuellement appelé [Snappy](https://en.wikipedia.org/wiki/Snappy_(compression))) : 2000 nanosecondes ou 2 microsecondes.
6. Prédiction de branche CPU [erronée](https://en.wikipedia.org/wiki/Branch_predictor) : 3 nanosecondes.
7. Lecture aléatoire sur disque SSD : 16 microsecondes.
8. Recherche sur disque (disque dur / disque magnétique) : 3 millisecondes.
9. Lecture séquentielle de 1 000 000 octets depuis la mémoire principale : 4 microsecondes.
10. Lecture séquentielle de 1 000 000 octets depuis un SSD : 62 microsecondes.
11. Lecture séquentielle de 1 000 000 octets depuis un disque : 947 microsecondes.
12. Requête réseau aller-retour dans le même centre de données : 500 microsecondes.
13. Envoyer 2000 octets sur un réseau standard : 62 nanosecondes.

## Temps nécessaire pour que la charge utile voyage sur TCP :

Voici le temps nécessaire pour transmettre diverses charges utiles de données sur des réseaux cellulaires typiques dans le monde, en supposant aucune perte de données.

RTT — Round Trip Time — Temps total nécessaire pour qu'un paquet de données (un ensemble d'octets de données) voyage de l'expéditeur au destinataire et du destinataire à l'expéditeur sur le réseau. En bref, on l'appelle temps de Ping.

1. Le transfert de 1 octet à 13 000 octets (environ 13 Ko) de données prend 1 aller-retour ou 1 RTT. Temps approximatif — USA : 150 millisecondes, Inde : 1200 millisecondes, Brésil : 600 millisecondes.
2. 13 001 octets — 39 000 octets (13 Ko à 39 Ko) prend 2 RTT. Temps approximatif — USA : 300 millisecondes, Inde : 2400 millisecondes, Brésil : 1200 millisecondes.
3. 39 001 octets — 91 000 octets (39 Ko à 91 Ko) prend 3 RTT. Temps approximatif — USA : 450 millisecondes, Inde : 3600 millisecondes, Brésil : 1800 millisecondes.
4. 91 001 octets — 195 000 octets (91 Ko à 195 Ko) prend 4 RTT. Temps approximatif — USA : 600 millisecondes, Inde : 4800 millisecondes, Brésil : 2400 millisecondes.

Ainsi, plus la taille de la réponse est grande, plus il y a d'octets, un aller-retour plus long, une latence d'API plus élevée, et finalement une application moins conviviale.

Cet article sera mis à jour lorsque de nouveaux chiffres ou des chiffres mis à jour seront trouvés. Veuillez me faire savoir si vous connaissez de nouveaux chiffres.

Cet article a été initialement publié sur le [mur medium](https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c) de l'auteur. Si vous l'aimez, veuillez applaudir.

Références :

1. [https://colin-scott.github.io/blog/2012/12/24/latency-trends/](https://colin-scott.github.io/blog/2012/12/24/latency-trends/)
2. [https://blog.std.in/2015/05/23/http-response-sizes-and-tcp/](https://blog.std.in/2015/05/23/http-response-sizes-and-tcp/)
3. [https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c](https://medium.com/@kousiknath/must-know-numbers-for-every-computer-engineer-6338a12c292c)