---
title: 'Une histoire embarrassante : Pourquoi mon serveur ne pouvait gérer que 10
  joueurs'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-20T20:17:06.000Z'
originalURL: https://freecodecamp.org/news/an-embarrassing-tale-why-my-server-could-only-handle-10-players-3b83b6fa8136
coverImage: https://cdn-media-1.freecodecamp.org/images/1*HcpeaKYBaTboHEs654ICcQ.png
tags:
- name: Game Preview
  slug: game-preview
- name: '#Game Design'
  slug: game-design
- name: Game Development
  slug: game-development
- name: Games
  slug: games
- name: indie game
  slug: indie-game
seo_title: 'Une histoire embarrassante : Pourquoi mon serveur ne pouvait gérer que
  10 joueurs'
seo_desc: 'By Jason Chitla

  What might be even more embarrassing is that at one point I had convinced myself
  that 10 players per server was normal.

  It all started with an idea at the beginning of the summer. I was standing in my
  room trying to think of an io gam...'
---

Par Jason Chitla

Ce qui pourrait être encore plus embarrassant, c'est que à un moment donné, je m'étais convaincu que 10 joueurs par serveur était normal.

Tout a commencé avec une idée au début de l'été. J'étais debout dans ma chambre en essayant de penser à un jeu io à créer (j'ai décidé que si je devais faire un jeu, je me limiterais à faire un jeu io pour un potentiel viral maximum — c'est une chose, je vous assure).

J'ai donc commencé à analyser ce qui rendait certains jeux io (agar.io, slither.io, etc.) addictifs. Je trouvais des comparaisons et des similitudes entre ces jeux, comme on peut le voir dans l'image ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/rkAzNXqwIAcH2zfY9tDJ5G2rF1uc7T3G2nKb)
_« Joey aimerait-il ça ? » → Joey est mon petit frère au collège. Écrire cette question sur le tableau m'a forcé à toujours prendre une décision en gardant à l'esprit les utilisateurs finaux (les utilisateurs du type Joey). Malin, hein._

Enfin, après un peu plus de brainstorming, je suis tombé sur [knckout.io](http://knckout.io). C'est le nom du jeu. Essayez de rester sur la carte et faites tomber les autres. J'ai adoré. Des contrôles simples, un objectif clair et une mécanique de jeu magnifique.

Après avoir défini comment je voulais que le jeu ait l'air et se sente, je me suis mis au travail. Je rentrais de mon stage d'été tous les jours, je faisais de l'exercice, puis je codais.

J'ai d'abord fait bouger le joueur comme je le voulais. Ensuite, j'ai géré le boost. Puis les collisions. Enfin, le jeu était terminé et prêt à être testé par le public. Ou du moins, c'est ce que je pensais...

Le week-end dernier (il y a environ une semaine), j'étais super motivé et prêt à montrer au monde ce que j'avais fait. Je me suis donc rendu sur le web et j'ai trouvé un petit subreddit appelé « playmygame ». J'ai écrit un court résumé et je l'ai [posté](https://www.reddit.com/r/playmygame/comments/6tr4o2/knckoutio/) (p.s. dans les commentaires du post, vous pouvez clairement voir que je stressais à propos de la capacité de mon serveur). J'ai attendu patiemment, puis HUZZAH ! Un joueur avait rejoint.

Nous allions et venions l'un contre l'autre dans le jeu. Pendant ce temps, je stressais et m'inquiétais de ce que ce joueur pouvait penser. Après que ce joueur ait perdu toutes ses vies et ait été éjecté de la partie, j'ai attendu pour voir s'il reviendrait. Et il l'a fait ! Mais encore mieux : le joueur a mis son nom à « ilikethisgame ». Mes yeux se sont agrandis et j'ai eu une montée d'adrénaline ! J'étais le garçon le plus heureux du monde.

Bientôt, d'autres joueurs ont rejoint et certains ont laissé des commentaires sur le post Reddit. Plus de joueurs ont dit qu'ils avaient aimé le jeu ! J'étais aux anges. Puis j'ai vérifié comment mon serveur tenait le coup (le 15/08)...

![Image](https://cdn-media-1.freecodecamp.org/images/QMRyiXB8dpEPTICQBm4PSy1w0kUrJfnJmai4)
_D'un serveur Digital Ocean NYC de 1 Go, 1 vCPU exécutant Ubuntu NodeJS 6.9.5 sur 14.04_

J'ai eu l'impression que quelqu'un m'avait coupé le souffle. Était-ce réel ? Cela devait être faux, me suis-je dit. Juste deux jeux et le serveur a du mal à les traiter.

J'ai commencé à réfléchir à ce que j'avais fait de travers dans mon code. Je pensais que la détection des collisions devait être le goulot d'étranglement. Mais j'utilisais déjà des quadtrees pour aider à réduire le nombre de passes de détection des collisions.

J'ai dû faire un peu de travail salissant, alors j'ai lancé un nouveau serveur Digital Ocean pour l'utiliser comme serveur de développement. J'ai ensuite temporairement désactivé complètement la détection des collisions et j'ai vu que le problème était toujours là.

OK — si la détection des collisions n'était pas le problème, alors quoi d'autre pouvait-ce être ?

J'ai pensé à la quantité d'informations que j'envoyais du serveur à chaque client chaque seconde. J'avais cette fonction de diffusion qui envoyait l'état du jeu toutes les 22 millisecondes à chaque client. Dans cette fonction, je filtrais inutilement le joueur local du client donné dans une propriété `allPlayers`, juste pour mettre le joueur local dans sa propre propriété. Donc, non seulement je mettais une boucle for (le filtrage) dans une autre boucle for (la diffusion pour chaque client), mais je personnalisais également les données à envoyer par cette fonction de diffusion pour chaque client.

Cette personnalisation n'était pas nécessaire. Je devrais simplement pouvoir envoyer l'état du jeu à tout le monde sans personnalisation. Tout le monde devrait recevoir les mêmes données (et les données ne devraient pas être adaptées à un client spécifique). C'est là que le CPU devait être mangé. J'ai donc optimisé cette fonction, je l'ai poussée sur le serveur de développement et j'ai vérifié le graphique du CPU. Pas de correction.

Avec mon ignorance, j'ai commencé à me convaincre que ~10–20 joueurs par serveur 1 cœur était bien. Maintenant, comment en suis-je arrivé à une telle conclusion ? Eh bien, ma confiance extrême en mes capacités techniques m'aveuglait clairement sur la réalité. Je suis tombé sur un [post](https://news.ycombinator.com/item?id=13266692) où le créateur de agar.io a dit que son serveur 1 cœur peut gérer environ 190 joueurs. Je me suis rapidement ressaisi.

Le prochain coupable que j'avais en ligne était : socket.io. J'utilisais socket.io pour gérer la communication en temps réel entre le client et le serveur. J'avais entendu dire auparavant que socket.io n'était pas aussi léger que d'autres alternatives.

À l'époque, si vous vouliez envoyer un message de manière asynchrone, vous deviez implémenter une sorte de hack : le polling long ou les sockets flash. C'était parce que tous les navigateurs web ne supportaient pas les websockets. Mais la plupart des navigateurs offrent maintenant un support natif. Mais pour que socket.io établisse une connexion, il le fait d'abord en utilisant l'un des hacks disponibles mentionnés, puis met à niveau la connexion si le client supporte une meilleure méthode. Même si les websockets sont déjà largement supportés. Cette approche se fait au détriment du CPU et de la mémoire. Mais pas autant que je le pensais...

Je suis allé en ligne et j'ai naïvement tapé « socket io cpu problem » dans Google. Les premiers résultats étaient intitulés « [Node.js — Comment déboguer les problèmes de CPU Node + Socket.io — Server Fault](https://serverfault.com/questions/498707/how-to-debug-node-socket-io-cpu-issues) » et « [Node.js — Serveur node socket.io utilisant un CPU élevé — Stack Overflow](https://stackoverflow.com/questions/8687434/socket-io-node-server-using-high-cpu?rq=1) ». Mes yeux se sont illuminés. J'ai été rassuré que c'était le coupable de mon problème. Mais j'ai cliqué sur le premier article et l'auteur a mentionné qu'il traitait ~1 500 connexions de socket simultanées. Je ne suis pas un major en maths, mais 20 joueurs est significativement moins que 1 500 joueurs.

Juste pour le plaisir, j'ai basculé mon application Node côté serveur pour utiliser [tiny websockets](https://github.com/uNetworking/uWebSockets), puis j'ai basculé l'application Node côté client pour utiliser le support natif des websockets, directement dans le navigateur. J'ai poussé les changements sur le serveur de développement et j'ai vérifié le graphique du CPU. Pas de correction.

Mon moral était au plus bas. J'ai commencé à grimacer chaque fois que je devais vérifier ce graphique de CPU. Je pensais que je n'allais jamais faire en sorte que cette ligne bleue arrête de s'éloigner de moi. C'était la seule fois où je me suis senti complètement incapable de gérer une tâche technique. Mais puis cela s'est produit...

J'étais assis devant le graphique du CPU, me morfondant dans ma misère, quand j'ai remarqué quelque chose. Peu importait combien de jeux complets étaient en cours ou à quel point ils étaient tous proches les uns des autres. Le CPU augmentait régulièrement à un rythme constant. Je n'étais jamais resté assez longtemps pour observer cela. Fuite de mémoire !

J'ai scanné mon code, ligne par ligne, à la recherche du bug (ce que j'aurais dû faire dès le début). Le voilà.

Dans mon jeu, un événement est un objet qui capture des informations sur des choses comme les morts de joueurs, les boosts et les collisions. Donc un événement est créé chaque fois que l'une de ces choses se produit.

J'ai cette boucle qui parcourt chaque événement et le met à jour. Elle est appelée toutes les 16 ms. Après qu'un événement ait rempli son devoir, il est censé être supprimé. Mots clés : « censé être ».

Bingo. J'avais un tas de mémoire qui s'accumulait ainsi qu'une quantité croissante de passes de boucle for inutiles. J'ai inséré une ligne de code et voilà !

![Image](https://cdn-media-1.freecodecamp.org/images/L8CFMJtioPQcWPBaK12MQcUO8ytlQIs3N1Rx)
_bien, je vais être_

Grand soupir de soulagement.

Ma prochaine tâche est de voir combien de jeux (4 joueurs par jeu) un serveur peut maintenant supporter en douceur. (Je sais qu'il peut en supporter au moins 12, mais je n'ai pas encore essayé plus). Maintenant que je sais que le nombre d'événements a un énorme impact sur le CPU... que se passera-t-il en production lorsque tous les joueurs déclencheront des événements de boost, de collision et de mort chaque seconde ? Mes tests n'ont pas tenu compte de cela.

De plus, après que ce post devienne viral, et que mon jeu suive le mouvement, je devrai rapidement augmenter le nombre de serveurs disponibles. Je ferai de cela le sujet d'un futur post ainsi que : « Comment [knckout.io](http://knckout.io) est passé à des millions de joueurs. » Suivez-moi ici pour les mises à jour. 😊