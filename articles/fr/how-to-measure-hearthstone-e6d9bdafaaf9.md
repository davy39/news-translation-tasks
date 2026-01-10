---
title: J'ai visualisé les données de chaque partie de Hearthstone à laquelle j'ai
  joué. Toutes les 4 700.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-02-02T23:28:46.000Z'
originalURL: https://freecodecamp.org/news/how-to-measure-hearthstone-e6d9bdafaaf9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*xDEs78svOKwkhRxvo5fqJQ.png
tags:
- name: Data Science
  slug: data-science
- name: gaming
  slug: gaming
- name: life
  slug: life
- name: Life lessons
  slug: life-lessons
- name: 'tech '
  slug: tech
seo_title: J'ai visualisé les données de chaque partie de Hearthstone à laquelle j'ai
  joué. Toutes les 4 700.
seo_desc: 'By Alan Wilson

  I’ve been playing Hearthstone since the beta. I’m a fairly casual player, but I
  have aspirations of eventually reaching the prestigious “Legend” ranking.

  Back in March I started to track my games to see if I had a chance of making it.
  ...'
---

Par Alan Wilson

Je joue à Hearthstone depuis la bêta. Je suis un joueur plutôt occasionnel, mais j'ai l'ambition d'atteindre un jour le prestigieux rang "Légende".

En mars, j'ai commencé à suivre mes parties pour voir si j'avais une chance d'y parvenir. Je joue la plupart de mes parties sur un iPad, donc c'était un processus manuel dans Google Sheets.

![Image](https://cdn-media-1.freecodecamp.org/images/h19NE8zY9w7JaC02Ba2219rQNg51CwVYlOJ1)
_J'ai suivi chaque partie classée depuis mars. Cela représente 4 700+ parties jusqu'à présent. J'aimerais vraiment qu'il y ait un moyen d'obtenir ces données plus facilement (ahem… [@playhearthstone](https://twitter.com/playhearthstone" rel="noopener" target="_blank" title=")?)._

#### Visualisation du classement en échelle

J'ai utilisé un simple formatage conditionnel pour rendre le tableau plus facile à lire, mais la plupart de mes analyses se font dans un outil gratuit appelé [Tableau Public](https://public.tableau.com/s/). Cela commence très basique—juste un graphique en ligne de mon classement—mais même cela est utile. Maintenant, je peux voir comment se passent mes tentatives pour atteindre Légende.

![Image](https://cdn-media-1.freecodecamp.org/images/A7camtQde7sz1YLeb9vrZyzsUn8lhIoAn91z)
_Je joue dans les deux formats classés : Standard et Wild._

Comme vous pouvez le voir, mon classement était assez volatile, alors j'ai fait évoluer la visualisation en utilisant des moyennes mobiles. Les chiffres bruts sont toujours là (dans les points), mais les lignes représentent maintenant une moyenne mobile sur 25 parties. Cela m'a permis de voir les vraies tendances de mon classement et de réduire les tendances à m'énerver lors des séries de défaites.

![Image](https://cdn-media-1.freecodecamp.org/images/DVkQF9KNciD1EiBDzXtAesLCxWmWbbe6J3Nv)
_Ces moyennes mobiles aident à calmer mon anxiété de l'échelle._

Ensuite, j'ai superposé les saisons les unes sur les autres pour pouvoir les comparer.

![Image](https://cdn-media-1.freecodecamp.org/images/PFlV7oIDdbgrrR37a9rjc3jtl17CcjNas1ds)
_Vous voyez correctement—j'étais **à une victoire** de Légende **7 fois différentes** lors de la saison 24. Soupir._

Maintenant, je peux voir à quel point ma progression chaque saison est efficace et comment elle se compare à la saison en cours. Mais je ne sais toujours pas combien de temps il reste dans la saison.

Est-ce que j'ai un jour ou une semaine de reste ? Suis-je mieux classé que d'habitude pour le 5ème jour de la saison ?

Pour répondre à ces questions, j'ai créé un graphique qui suit la progression par jour de la saison. Ici, j'ai des strip-plots pour chaque jour et une ligne reliant le classement maximum atteint chaque jour. C'est une meilleure façon d'évaluer mes chances d'atteindre Légende dans une saison donnée.

![Image](https://cdn-media-1.freecodecamp.org/images/HkSbNLXfTL9OXbGF8kDQmkOHzvSW4fnefKwU)

#### Visualisation de la performance des decks

Mais qu'en est-il des decks ? Évidemment, ils jouent un rôle énorme. En ce qui concerne les decks, tout est question de taux de victoire, donc je visualise chaque deck comme une ligne. C'est un peu encombré, mais je peux voir le taux de victoire, quand il se stabilise, et comment un deck se compare à un autre. La fonction de surbrillance de Tableau est _vraiment_ utile ici.

![Image](https://cdn-media-1.freecodecamp.org/images/26-Sygty2grNl532udKwhPrNA980IXW65100)
_Remarquez comment il faut environ 100 parties pour qu'un deck se stabilise. Souvenez-vous de cela la prochaine fois que vous lirez à propos du taux de victoire "incroyable" de 82,35 % de quelqu'un (après seulement 17 parties)._

Ensuite, j'ai créé une vue spécifique au deck de ce graphique pour voir comment il performe contre différentes classes. Je dois jouer _beaucoup_ de parties avant que des tendances n'émergent, mais une fois qu'elles le font, j'ai une idée de la fréquence de chaque classe et de ma performance contre elle. Selon le méta, j'obtiens également une compréhension des match-ups de decks.

![Image](https://cdn-media-1.freecodecamp.org/images/itX05eBsBzeAnkvKxHhYYloO1YQx-ys9qlQB)

Maintenant, il va sans dire que mon taux de victoire va souffrir à mesure que j'atteins des rangs plus élevés, alors j'ai créé un graphique à bulles pour m'aider à mieux comprendre la performance de mes decks à différents rangs et saisons.

![Image](https://cdn-media-1.freecodecamp.org/images/l9Hr6bJZfE8M6c8-jpS5PhJbAhnxlyodrJWV)
_Mon deck Zoo a très bien performé jusqu'à ce que j'atteigne le Rang 5._

### Comment fonctionne le système de classement de Hearthstone

Tout cela m'a fait réfléchir à la difficulté, aux saisons et au système de classement (soyez indulgent si vous maîtrisez bien le système de classement de Hearthstone). Tout d'abord, le système de classement n'est pas linéaire comme on pourrait le supposer. Les rangs (commencant à 25 et allant jusqu'à 1) ne sont pas espacés uniformément car le nombre d'étoiles entre chaque rang change à mesure que vous montez dans l'échelle. En tout, il y a 120 placements possibles.

![Image](https://cdn-media-1.freecodecamp.org/images/zzdTyoXk6rJen1TnVd5lbPrezK4fDNz7m4Fa)

Mais Blizzard n'a pas arrêté là. Ils ont créé une résistance supplémentaire à partir du rang 20, puis à nouveau au rang 5.

![Image](https://cdn-media-1.freecodecamp.org/images/SrGtzAgycCXKR85H6jFuO7EUUnKDpdH8FrA8)

Enfin, Hearthstone a des saisons très courtes—un seul mois. À la fin de chaque mois, tout le monde est renvoyé au bas de l'échelle.

![Image](https://cdn-media-1.freecodecamp.org/images/cevOooSmVRiswh8P6agOxbNP45pEXktKIw-A)

Maintenant, ce n'est pas une nouvelle pour quiconque joue beaucoup de parties classées. Mais cela me ramène à ma question initiale : comment mesurer la difficulté d'une partie donnée ?

### Modélisation de la difficulté du jeu

J'ai commencé avec quelques hypothèses simples :

1. La partie la plus difficile de la saison est au rang 1 avec 5 étoiles le premier jour du mois.
2. La partie la moins difficile de la saison est au rang 25 sans étoiles le dernier jour du mois.
3. Toute partie jouée plus tard dans le mois à un rang donné est plus facile qu'une partie jouée à ce même rang plus tôt dans le mois.

En utilisant ces hypothèses comme guide, j'ai créé un modèle de difficulté. Au début, il était très simple (et inexact).

![Image](https://cdn-media-1.freecodecamp.org/images/BSLkpvID6E-m4cEvHYxccoqRLAVjBmdNcsqp)
_Un modèle très approximatif._

Je l'ai affiné jusqu'à ce qu'il reflète ma _perception_ de la difficulté. Notez que cela n'est pas basé sur des données et je doute qu'il soit complètement précis, mais c'est mieux que le rang seul pour évaluer la difficulté.

![Image](https://cdn-media-1.freecodecamp.org/images/Xm1goAK3Jrr20cloCiHDcohFK6d3qEcDeNBR)
_Un meilleur modèle._

Maintenant, revisitons certains des graphiques précédents en utilisant cette nouvelle métrique de "difficulté" à la place du rang. Cela offre une perspective différente—espérons-le, plus précise.

![Image](https://cdn-media-1.freecodecamp.org/images/qKFBCPEHsM4OlQxaMp2ls7St14YbbUJpwAvY)

Et ce graphique à bulles ? J'ai mis la difficulté en catégories, comme je l'ai fait avec le rang, et je me sens déjà mieux avec la perspective que cela offre. C'est tout aussi précieux en début et en fin de saison.

![Image](https://cdn-media-1.freecodecamp.org/images/OSdS-KXr0jxUD8x3dFMlwlGJ2Kuf8ZUMDhSb)

#### Évaluation de la performance des decks

Ensuite, j'utilise la difficulté pour créer _une autre_ métrique. Celle-ci est assez simple. Je l'appelle "qualité". Si je gagne une partie, j'ajoute la difficulté de cette partie à la qualité. Si je perds une partie, je soustrais la difficulté de cette partie de la qualité.

> Si "victoire" alors + difficulté

> Sinon si "défaite" alors – difficulté

Cela me permet de récompenser davantage les victoires dans des parties difficiles que dans des parties faciles et donne des résultats très intéressants. Vous vous souvenez de ce graphique montrant les taux de victoire des decks ? Le voici à nouveau, mais avec notre nouvelle métrique de qualité sur l'axe des y (la couleur est toujours le taux de victoire).

![Image](https://cdn-media-1.freecodecamp.org/images/i2YHuYBLDQmwsOWpZ1OWGI0AHa-JkWtwo8Z4)

J'ai également résumé cela en un simple rang.

![Image](https://cdn-media-1.freecodecamp.org/images/OWqNZrWBdUCt-PHgOS2n1xGumaWp9Y0xcnsN)
_Même un taux de victoire de 53,9 % n'a pas pu sauver la performance de mon Démoniste Zoo de la saison 27._

#### Qu'est-ce qui suit ?

Il y a encore beaucoup de choses que je veux explorer davantage avec mon ensemble de données. Il serait également intéressant d'appliquer ces techniques aux joueurs professionnels et de les comparer les uns aux autres. Sont-ils Légende rang 1 parce qu'ils gagnent des parties difficiles ? Le taux de victoire seul est-il le meilleur prédicteur de compétence ? Quel rôle joue le volume de parties jouées dans l'avancement du rang ?

Au cas où vous ne l'auriez pas deviné d'après les données, je _n'ai toujours pas_ atteint Légende, mais je m'amuse honnêtement autant à analyser mes statistiques qu'à jouer au jeu.

### \_(ツ)_/