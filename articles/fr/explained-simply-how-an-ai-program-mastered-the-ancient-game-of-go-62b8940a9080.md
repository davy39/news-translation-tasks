---
title: 'Expliqué simplement : Comment un programme d''IA a maîtrisé l''ancien jeu
  de Go'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-03-10T05:54:28.000Z'
originalURL: https://freecodecamp.org/news/explained-simply-how-an-ai-program-mastered-the-ancient-game-of-go-62b8940a9080
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Y9MhKgjWmKJ_iwT5.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Deep Learning
  slug: deep-learning
- name: 'Science '
  slug: science
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Expliqué simplement : Comment un programme d''IA a maîtrisé l''ancien
  jeu de Go'
seo_desc: 'By Aman Agarwal

  This is about AlphaGo, Google DeepMind’s Go playing AI that shook the technology
  world in 2016 by defeating one of the best players in the world, Lee Sedol.

  Go is an ancient board game which has so many possible moves at each step tha...'
---

Par Aman Agarwal

Cet article parle d'**AlphaGo**, l'IA de Google DeepMind qui joue au [_Go_](https://en.wikipedia.org/wiki/Go_(game)) et qui a secoué le monde de la technologie en 2016 en battant l'un des meilleurs joueurs du monde, [Lee Sedol](https://en.wikipedia.org/wiki/Lee_Sedol).

Le Go est un jeu de plateau ancien qui offre tant de coups possibles à chaque étape que les positions futures sont difficiles à prédire — et donc, il nécessite une forte intuition et une pensée abstraite pour être joué. Pour cette raison, on pensait que seuls les humains pouvaient être bons au Go. La plupart des chercheurs pensaient qu'il faudrait encore des décennies pour construire une IA capable de penser ainsi. En fait, je publie cet essai aujourd'hui parce que _cette semaine (8–15 mars) marque le deuxième anniversaire du match AlphaGo contre Sedol !_

Mais AlphaGo ne s'est pas arrêté là. 8 mois plus tard, il a joué 60 parties professionnelles sur un site de Go sous le pseudonyme de « Master », et a gagné _chaque partie_, contre _des dizaines_ de champions du monde, bien sûr sans se reposer entre les parties.

Naturellement, ce fut une énorme réalisation dans le domaine de l'IA et a suscité des discussions mondiales sur le fait de savoir si nous devrions être excités ou inquiets par l'intelligence artificielle.

Aujourd'hui, nous allons prendre l'article de recherche original publié par DeepMind dans la revue _Nature_, et le décomposer paragraphe par paragraphe en utilisant un anglais simple.

**_Après cet essai, vous saurez très clairement ce qu'est AlphaGo et comment il fonctionne. J'espère aussi qu'après avoir lu cela, vous ne croirez pas tous les titres de journaux faits par les journalistes pour vous faire peur de l'IA, et que vous vous sentirez plutôt excité à ce sujet._**

S'inquiéter des réalisations croissantes de l'IA, c'est comme s'inquiéter des capacités croissantes de Microsoft Powerpoint. Oui, il s'améliorera avec le temps avec de nouvelles fonctionnalités, mais il ne peut pas simplement _croître de manière incontrôlable_ pour devenir une sorte de monstre hollywoodien.

**Vous n'avez PAS besoin de savoir jouer au Go pour comprendre cet article.** En fait, je n'ai moi-même lu que les 3–4 premières lignes du paragraphe d'ouverture de Wikipedia à ce sujet. À la place, et c'est surprenant, j'utilise quelques exemples de base des échecs pour expliquer les algorithmes. Vous devez simplement savoir ce qu'est un jeu de plateau à deux joueurs, dans lequel chaque joueur joue à tour de rôle et il y a un gagnant à la fin. Au-delà de cela, vous n'avez pas besoin de connaître la physique ou les mathématiques avancées.

Cela le rendra plus accessible aux personnes qui commencent tout juste à apprendre le machine learning ou les réseaux de neurones. Et surtout pour ceux qui n'utilisent pas l'anglais comme première langue (ce qui peut rendre très difficile la lecture de tels articles).

_Si vous n'avez AUCUNE connaissance préalable de l'IA et des réseaux de neurones, vous pouvez lire la section « Deep Learning » de l'un de mes précédents essais [**ici**](https://medium.com/swlh/everything-about-self-driving-cars-explained-for-non-engineers-f73997dcb60c). Après avoir lu cela, vous serez en mesure de comprendre cet essai._

_Si vous souhaitez obtenir une compréhension superficielle du Reinforcement Learning également (lecture optionnelle), vous pouvez le trouver [**ici**](https://medium.freecodecamp.org/explained-simply-how-deepmind-taught-ai-to-play-video-games-9eb5f38c89ee)._

Voici l'article original si vous souhaitez essayer de le lire :

En ce qui me concerne : Bonjour, je suis [Aman](http://aman-agarwal.com), ingénieur en IA et robots autonomes. J'espère que mon travail vous fera gagner beaucoup de temps et d'efforts si vous deviez étudier cela par vous-même.

_Parlez-vous japonais ?_ [Ryohji Ikebe](https://www.freecodecamp.org/news/explained-simply-how-an-ai-program-mastered-the-ancient-game-of-go-62b8940a9080/undefined) a gentiment écrit un bref mémo sur cet essai en japonais, dans une [série de Tweets](https://twitter.com/ikb/status/976008433852866560).

### Commençons !

#### Résumé

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDDMR_HFoZ1o7Ry5K2s9lQ.png)

Comme vous le savez, l'objectif de cette recherche était d'entraîner un programme d'IA à jouer au Go au niveau des meilleurs joueurs humains professionnels.

Pour comprendre ce défi, laissez-moi d'abord parler de quelque chose de similaire fait pour les échecs. Au début des années 1990, IBM a sorti l'ordinateur Deep Blue qui a battu le grand champion [**Garry Kasparov**](https://en.wikipedia.org/wiki/Garry_Kasparov) aux échecs. (C'est aussi un gars très cool, assurez-vous de lire plus sur lui plus tard !) Comment Deep Blue jouait-il ?

Eh bien, il utilisait une méthode très brute. À chaque étape du jeu, il regardait tous les coups légaux possibles qui pouvaient être joués, et explorait chaque coup pour voir ce qui se passerait. Et il continuait à explorer coup après coup pendant un moment, formant une sorte d'énorme arbre de décision de milliers de coups. Ensuite, il revenait le long de cet arbre, observant quels coups semblaient les plus susceptibles d'apporter un bon résultat. Mais que voulons-nous dire par « bon résultat » ? Eh bien, Deep Blue avait de nombreuses stratégies d'échecs soigneusement conçues intégrées par des experts en échecs pour l'aider à prendre de meilleures décisions — par exemple, comment décider de protéger le roi ou d'obtenir un avantage ailleurs ? Ils ont fait un algorithme d'évaluation spécifique à cet effet, pour comparer à quel point différentes positions sur le plateau sont avantageuses ou désavantageuses (IBM a codé en dur des stratégies d'échecs d'experts dans cette fonction d'évaluation). Et enfin, il choisit un coup soigneusement calculé. Au tour suivant, il refait essentiellement tout le processus.

Comme vous pouvez le voir, cela signifie que Deep Blue a pensé à des millions de positions théoriques avant de jouer chaque coup. Cela n'était pas si impressionnant en termes de logiciel d'IA de Deep Blue, mais plutôt en termes de matériel — IBM l'a présenté comme l'un des ordinateurs les plus puissants disponibles sur le marché à cette époque. Il pouvait examiner 200 millions de positions de plateau par seconde.

Maintenant, nous en venons au Go. Croyez-moi simplement que ce jeu est beaucoup plus ouvert, et si vous essayiez la stratégie Deep Blue sur le Go, vous ne pourriez pas bien jouer. Il y aurait TELLEMENT de positions à examiner à chaque étape que ce serait simplement impraticable pour un ordinateur de passer par cet enfer. Par exemple, au coup d'ouverture aux échecs, il y a 20 coups possibles. Au Go, le premier joueur a 361 coups possibles, et cette étendue de choix reste large tout au long du jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/0*XimL5rBEve3cv2m9.jpg)

C'est ce qu'ils veulent dire par « espace de recherche énorme ». De plus, au Go, il n'est pas si facile de juger à quel point une position particulière sur le plateau est avantageuse ou désavantageuse à un moment spécifique du jeu — vous devez presque jouer toute la partie pendant un certain temps avant de pouvoir déterminer qui gagne. Mais disons que vous avez magiquement un moyen de faire les deux. Et c'est là que le deep learning entre en jeu !

Dans cette recherche, DeepMind a utilisé des réseaux de neurones pour effectuer ces deux tâches (si vous n'avez jamais lu sur les réseaux de neurones, [voici le lien à nouveau](https://medium.com/swlh/everything-about-self-driving-cars-explained-for-non-engineers-f73997dcb60c)). Ils ont entraîné un « réseau de neurones de politique » pour décider quels sont les coups les plus sensés dans une position particulière sur le plateau (c'est donc comme suivre une stratégie intuitive pour choisir des coups à partir de n'importe quelle position). Et ils ont entraîné un « réseau de neurones de valeur » pour estimer à quel point un arrangement particulier sur le plateau est avantageux pour le joueur (ou en d'autres termes, à quel point vous êtes susceptible de gagner la partie à partir de cette position). Ils ont d'abord entraîné ces réseaux de neurones avec des exemples de parties humaines (votre bon vieux apprentissage supervisé ordinaire). Après cela, l'IA était capable d'imiter le jeu humain dans une certaine mesure, donc elle agissait comme un joueur humain faible. Et ensuite, pour entraîner les réseaux encore plus, ils ont fait jouer l'IA contre elle-même des millions de fois (c'est la partie « apprentissage par renforcement »). Avec cela, l'IA s'est améliorée parce qu'elle avait plus de pratique.

Avec ces deux réseaux seuls, l'IA de DeepMind était capable de bien jouer contre des programmes de jeu de Go de pointe que d'autres chercheurs avaient construits auparavant. Ces autres programmes avaient utilisé un algorithme de jeu préexistant déjà populaire, appelé « Monte Carlo Tree Search » (MCTS). Plus à ce sujet plus tard.

Mais devinez quoi, nous n'avons toujours pas parlé du vrai problème. L'IA de DeepMind ne concerne pas seulement les réseaux de politique et de valeur. Elle n'utilise pas ces deux réseaux comme un _remplacement_ de la Monte Carlo Tree Search. Au lieu de cela, elle utilise les réseaux de neurones pour faire fonctionner l'algorithme MCTS _mieux_… et il est devenu si bon qu'il a atteint des niveaux surhumains. CETTE version améliorée de MCTS est « AlphaGo », l'IA qui a battu Lee Sedol et est entrée dans l'histoire de l'IA comme l'une des plus grandes percées de tous les temps. Donc, essentiellement, AlphaGo est simplement une _implémentation améliorée_ d'un algorithme très ordinaire en informatique. Comprenez-vous maintenant pourquoi l'IA dans sa forme actuelle n'est absolument **rien** à craindre ?

Wow, nous avons passé beaucoup de temps sur le Résumé seul.

![Image](https://cdn-media-1.freecodecamp.org/images/1*R5nRwdKMg9bw7epJgOf-jA.png)

D'accord — pour comprendre l'article à partir de ce point, nous allons d'abord parler d'une stratégie de jeu appelée algorithme Monte Carlo Tree Search. Pour l'instant, je vais simplement expliquer cet algorithme en profondeur pour donner un sens à cet essai. Mais si vous voulez en apprendre davantage, des gens intelligents ont également fait d'excellentes vidéos et articles de blog à ce sujet :

1. [Une courte série de vidéos de Udacity](https://www.youtube.com/watch?v=onBYsen2_eA)
2. [L'explication de Jeff Bradberry sur MCTS](https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/)
3. [Un tutoriel MCTS par Fullstack Academy](https://www.youtube.com/watch?v=Fbs4lnGLS8M)

La section suivante est longue, mais facile à comprendre (je vais faire de mon mieux) et TRÈS importante, alors restez avec moi ! Le reste de l'essai ira beaucoup plus vite.

Parlons du premier paragraphe de l'essai ci-dessus. Vous souvenez-vous de ce que j'ai dit à propos de Deep Blue créant un énorme arbre de millions de positions et de coups à chaque étape du jeu ? Vous deviez faire des simulations et regarder et comparer chaque coup possible. Comme je l'ai dit auparavant, c'était une approche simple et très directe — si l'ingénieur logiciel moyen devait concevoir une IA de jeu, et avait tous les ordinateurs les plus puissants du monde, il ou elle concevrait probablement une solution similaire.

Mais réfléchissons à la façon dont les humains jouent eux-mêmes aux échecs ? Supposons que vous êtes à une position particulière sur le plateau au milieu du jeu. Selon les règles du jeu, vous pouvez faire une douzaine de choses différentes — déplacer ce pion ici, déplacer la reine de deux cases ici ou trois cases là, et ainsi de suite. Mais faites-vous vraiment une liste de tous les coups possibles que vous pouvez faire avec toutes vos pièces, puis sélectionnez un coup dans cette longue liste ? Non — vous réduisez « intuitivement » à quelques coups clés (disons que vous trouvez 3 coups sensés) que vous pensez avoir du sens, puis vous vous demandez ce qui se passera dans le jeu si vous choisissez l'un de ces 3 coups. Vous pourriez passer 15–20 secondes à considérer chacun de ces 3 coups et leur futur — et notez que pendant ces 15 secondes, vous n'avez pas à planifier soigneusement le futur de chaque coup ; vous pouvez simplement « dérouler » quelques coups mentaux guidés par votre intuition sans TROP de réflexion minutieuse (eh bien, un bon joueur penserait plus loin et plus profondément qu'un joueur moyen). C'est parce que vous avez un temps limité, _et_ vous ne pouvez pas prédire avec précision ce que votre _adversaire_ fera à chaque étape dans ce bel avenir que vous cuisinez dans votre cerveau. Donc vous devrez simplement laisser votre sentiment vous guider. Je vais me référer à cette partie du processus de réflexion comme « dérouler », alors notez-le !

Donc après avoir « déroulé » vos quelques coups sensés, vous dites finalement « et puis c'est tout » et jouez simplement le coup que vous trouvez le meilleur.

Ensuite, l'adversaire fait un coup. Il pourrait s'agir d'un coup que vous aviez déjà bien anticipé, ce qui signifie que vous êtes maintenant assez confiant quant à ce que vous devez faire ensuite. Vous n'avez pas à passer trop de temps sur les déroulages à nouveau. OU, il pourrait s'agir que votre adversaire vous frappe avec un coup assez cool auquel vous ne vous attendiez pas, donc vous devez être encore plus prudent avec votre prochain coup.

C'est ainsi que le jeu se poursuit, et à mesure qu'il se rapproche du point final, il vous sera plus facile de prédire le résultat de vos coups — donc vos déroulages ne prennent pas autant de temps.

Le but de cette longue histoire est de décrire ce que l'algorithme MCTS fait à un niveau superficiel — il imite le processus de réflexion ci-dessus en construisant un « arbre de recherche » de coups et de positions à chaque fois. Encore une fois, pour plus de détails, vous devriez consulter les liens que j'ai mentionnés précédemment. L'innovation ici est qu'au lieu de passer par tous les coups possibles à chaque position (ce que Deep Blue a fait), il sélectionne intelligemment un petit ensemble de coups sensés et explore ceux-ci à la place. Pour les explorer, il « déroule » le futur de chacun de ces coups et les compare en fonction de leurs résultats _imaginés_.

(Sérieusement — c'est tout ce que je pense que vous devez comprendre pour cet essai)

Maintenant — revenons à la capture d'écran de l'article. Le Go est un jeu à « [information parfaite](https://jeffbradberry.com/posts/2015/09/intro-to-monte-carlo-tree-search/) » (veuillez lire la définition dans le lien, ne vous inquiétez pas, ce n'est pas effrayant). Et **théoriquement**, pour de tels jeux, peu importe **_quelle_** position particulière vous occupez dans le jeu (même si vous venez de jouer 1–2 coups), il est possible que vous puissiez deviner correctement qui va gagner ou perdre (en supposant que les deux joueurs jouent « parfaitement » à partir de ce point). _Je ne sais pas qui a inventé cette théorie, mais c'est une hypothèse fondamentale dans ce projet de recherche et ça marche._

Donc, cela signifie que, étant donné un état du jeu _s_, il existe une fonction v*(s) qui peut prédire le résultat, disons la probabilité que vous gagniez ce jeu, de 0 à 1. Ils l'appellent la « fonction de valeur optimale ». Parce que certaines positions sur le plateau sont plus susceptibles de vous faire gagner que d'autres positions sur le plateau, elles peuvent être considérées comme plus « précieuses » que les autres. Laissez-moi le redire : Valeur = Probabilité entre 0 et 1 que vous gagniez le jeu.

Mais attendez — disons qu'il y avait une fille nommée Foma assise à côté de vous pendant que vous jouez aux échecs, et qu'elle vous dit à chaque étape si vous gagnez ou perdez. « Vous gagnez… Vous perdez… Non, vous perdez toujours… » Je pense que cela ne vous aiderait pas beaucoup à choisir quel coup vous devez faire. Elle serait aussi assez ennuyeuse. Ce qui vous aiderait plutôt, c'est si vous dessiniez tout l'arbre de tous les coups possibles que vous pouvez faire, et les états auxquels ces coups mèneraient — et ensuite Foma vous dirait pour tout l'arbre quels états sont des états gagnants et quels états sont des états perdants. Ensuite, vous pouvez choisir des coups qui continueront à vous mener à des états gagnants. Tout à coup, Foma est votre partenaire dans le crime, pas une amie ennuyeuse. Ici, Foma se comporte comme votre fonction de valeur optimale v*(s). Auparavant, on pensait qu'il n'était pas possible d'avoir une fonction de valeur précise comme Foma pour le jeu de Go, parce que les jeux avaient trop d'incertitude.

MAIS — même si vous aviez la merveilleuse Foma, cette stratégie de wonderland de dessiner toutes les positions possibles pour que Foma les évalue ne fonctionnera pas très bien dans le monde réel. Dans un jeu comme les échecs ou le Go, comme nous l'avons dit auparavant, si vous essayez d'imaginer même 7–8 coups dans le futur, il peut y avoir tellement de positions possibles que vous n'avez pas assez de temps pour les vérifier toutes avec Foma.

Donc Foma ne suffit pas. Vous devez réduire la liste des coups à quelques coups sensés que vous pouvez dérouler dans le futur. Comment votre programme va-t-il faire cela ? Entrez Lusha. Lusha est une joueuse d'échecs expérimentée et une passionnée qui a passé des décennies à regarder des grands maîtres jouer aux échecs les uns contre les autres. Elle peut regarder votre position sur le plateau, regarder rapidement tous les coups disponibles que vous pouvez faire, et vous dire à quel point il est probable qu'un expert en échecs fasse l'un de ces coups s'il était assis à votre table. Donc, si vous avez 50 coups possibles à un moment donné, Lusha vous dira la probabilité que chaque coup soit choisi par un expert. Bien sûr, quelques coups sensés auront une probabilité beaucoup plus élevée et d'autres coups inutiles auront une probabilité très faible. Par exemple : aux échecs, disons que votre reine est en danger dans un coin du jeu, vous pourriez encore avoir l'option de déplacer un petit pion dans un autre coin du jeu. Elle est votre _fonction de politique_, p(a\s). Pour un état donné s, elle peut vous donner des probabilités pour tous les coups possibles qu'un expert ferait.

Wow — vous pouvez utiliser l'aide de Lusha pour vous guider dans la sélection de quelques coups sensés, et Foma vous dira la probabilité de gagner à partir de chacun de ces coups. Vous pouvez choisir le coup que Foma et Lusha approuvent toutes les deux. Ou, si vous voulez être extra prudent, vous pouvez dérouler les coups sélectionnés par Lusha, faire évaluer par Foma, en choisir quelques-uns pour les dérouler plus loin dans le futur, et continuer à laisser Foma et Lusha vous aider à prédire TRÈS loin dans le futur du jeu — beaucoup plus rapide et plus efficace que de passer par tous les coups à chaque étape dans le futur. C'EST ce qu'ils veulent dire par « réduire l'espace de recherche ». Utilisez une fonction de valeur (Foma) pour prédire les résultats, et utilisez une fonction de politique (Lusha) pour vous donner des probabilités de grand maître afin de vous aider à réduire les coups que vous déroulez. Ceux-ci sont appelés « déroulages de Monte Carlo ». Ensuite, pendant que vous revenez du futur au présent, vous pouvez prendre les valeurs moyennes de tous les différents coups que vous avez déroulés, et choisir l'action la plus appropriée. Jusqu'à présent, cela n'a fonctionné qu'à un niveau amateur faible dans le Go, car les fonctions de politique et de valeur qu'ils ont utilisées pour guider ces déroulages n'étaient pas si bonnes.

Ouf.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sonozS4bQD9Dd_-thQxKMg.png)

La première ligne est explicite. Dans MCTS, vous pouvez commencer avec une Foma non qualifiée et une Lusha non qualifiée. Plus vous jouez, mieux elles deviennent pour prédire des résultats et des coups solides. « Réduire la recherche à un faisceau d'actions à haute probabilité » est simplement une manière sophistiquée de dire : « Lusha vous aide à réduire les coups que vous devez dérouler en leur attribuant des probabilités qu'un expert les jouerait ». Les travaux antérieurs ont utilisé cette technique pour atteindre des joueurs d'IA de niveau amateur fort, même avec des fonctions de politique simples (ou « superficielles » comme ils l'appellent).

![Image](https://cdn-media-1.freecodecamp.org/images/1*LGYVFeJlh4eM9ecwSNjTIA.png)

Oui, les réseaux de neurones convolutifs sont excellents pour le traitement d'images. Et puisque un réseau de neurones prend une entrée particulière et donne une sortie, c'est essentiellement une fonction, n'est-ce pas ? Donc vous pouvez utiliser un réseau de neurones pour devenir une fonction complexe. Donc vous pouvez simplement passer une image de la position du plateau et laisser le réseau de neurones comprendre par lui-même ce qui se passe. Cela signifie qu'il est possible de créer des réseaux de neurones qui se comporteront comme des fonctions de politique et de valeur TRÈS précises. Le reste est assez explicite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*1eYuYipiPEX9rrUAXwuCeQ.png)

Ici, nous discutons de la façon dont Foma et Lusha ont été entraînées. Pour entraîner le réseau de politique (prédire pour une position donnée quels coups les experts choisiraient), vous utilisez simplement des exemples de parties humaines et les utilisez comme données pour le bon vieux apprentissage supervisé.

Et vous voulez entraîner une autre version légèrement différente de ce réseau de politique à utiliser pour les déroulages ; celle-ci sera plus petite et plus rapide. Disons simplement que puisque Lusha est si expérimentée, elle prend un certain temps pour traiter chaque position. Elle est bonne pour commencer le processus de réduction, mais si vous essayez de lui faire répéter le processus, elle prendra encore un peu trop de temps. Donc vous entraînez un *réseau de politique plus rapide* pour le processus de déroulage (je l'appellerai… le jeune frère de Lusha, Jerry ? Je sais, je sais, assez avec ces noms). Après cela, une fois que vous avez entraîné les réseaux de politique lents et rapides avec suffisamment de données de joueurs humains, vous pouvez essayer de faire jouer Lusha contre elle-même sur un plateau de Go pendant quelques jours, et obtenir plus de pratique. C'est la partie apprentissage par renforcement — faire une meilleure version du réseau de politique.

Ensuite, vous entraînez Foma pour la prédiction de valeur : déterminer la probabilité que vous gagniez. Vous laissez l'IA s'entraîner en jouant contre elle-même encore et encore dans un environnement simulé, observez le résultat final à chaque fois, et apprenez de ses erreurs pour devenir de mieux en mieux.

Je n'entrerai pas dans les détails de **_comment_** ces réseaux sont entraînés. Vous pouvez lire plus de détails techniques dans la section ultérieure de l'article (« Méthodes ») que je n'ai pas couverte ici. En fait, le vrai but de cet article particulier n'est pas de montrer **_comment_** ils ont utilisé l'apprentissage par renforcement sur ces réseaux de neurones. L'un des articles précédents de DeepMind, dans lequel ils ont appris à l'IA à jouer à des jeux ATARI, a déjà discuté de certaines techniques d'apprentissage par renforcement en profondeur (Et j'ai déjà écrit une explication de cet article [ici](https://medium.freecodecamp.org/explained-simply-how-deepmind-taught-ai-to-play-video-games-9eb5f38c89ee)). Pour cet article, comme je l'ai légèrement mentionné dans le Résumé et aussi souligné dans la capture d'écran ci-dessus, la plus grande innovation était **_le fait qu'ils ont utilisé l'apprentissage par renforcement avec des réseaux de neurones_** pour améliorer un algorithme de jeu déjà populaire, MCTS. L'apprentissage par renforcement est un outil cool dans une boîte à outils qu'ils ont utilisé pour affiner les réseaux de neurones de politique et de valeur après l'entraînement supervisé régulier. Cet article de recherche est sur la preuve de la polyvalence et de l'excellence de cet outil, pas sur l'apprentissage de son utilisation. **En termes de télévision, l'article Atari était une infopublicité sur l'apprentissage par renforcement et cet article AlphaGo est une publicité.**

#### D'accord, nous avons enfin terminé avec les parties « introduction ». À ce stade, vous avez déjà une très bonne idée de ce qu'était AlphaGo.

#### Ensuite, nous allons approfondir légèrement chaque chose que nous avons discutée ci-dessus. Vous pourriez voir quelques équations et expressions mathématiques laides et dangereuses, mais elles sont simples (je les explique toutes). Détendez-vous.

Une rapide note avant de continuer. Souhaitez-vous m'aider à écrire plus d'essais expliquant des articles de recherche intéressants ? Si vous êtes sérieux, je serais ravi de travailler avec vous. Laissez un commentaire et je vous contacterai.

![Image](https://cdn-media-1.freecodecamp.org/images/0*fVll6yCFC9UDeFR1.jpg)
_Une photo de deux femmes japonaises jouant au Go, placée ici au cas où vous seriez déjà fatigué de regarder de longs blocs de texte._

![Image](https://cdn-media-1.freecodecamp.org/images/1*_df8aEGWvtbPvUUIvr8fAA.png)

Donc, la première étape consiste à entraîner notre réseau de neurones de politique (Lusha), pour prédire quels coups sont susceptibles d'être joués par un expert. L'objectif de ce réseau de neurones est de permettre à l'IA de jouer de manière similaire à un expert humain. Il s'agit d'un réseau de neurones convolutif (comme je l'ai mentionné précédemment, c'est un type spécial de réseau de neurones très utile dans le traitement d'images) qui prend une image simplifiée d'un arrangement de plateau. Les « non-linéarités rectificatrices » sont des couches qui peuvent être ajoutées à l'architecture du réseau. Elles lui donnent la capacité d'apprendre des choses plus complexes. Si vous avez déjà entraîné des réseaux de neurones auparavant, vous avez peut-être utilisé la couche « ReLU ». C'est ce que sont ces couches.

Les données d'entraînement ici étaient sous la forme de paires aléatoires de positions de plateau, et les étiquettes étaient les actions choisies par les humains lorsqu'ils étaient dans ces positions. Juste un apprentissage supervisé régulier.

Ici, ils utilisent la « montée de gradient stochastique ». Eh bien, il s'agit d'un algorithme pour la rétropropagation. Ici, vous essayez de **maximiser** une fonction de récompense. Et la fonction de récompense est simplement la probabilité de l'action prédite par un expert humain ; vous voulez augmenter cette probabilité. Mais hé — vous n'avez pas vraiment besoin de trop réfléchir à cela. Normalement, vous entraînez le réseau pour qu'il **minimise** une fonction de perte, qui est essentiellement l'erreur/différence entre le résultat prédit et l'étiquette réelle. Cela s'appelle la descente de gradient. Dans la mise en œuvre réelle de cet article de recherche, ils ont effectivement utilisé la descente de gradient **régulière**. Vous pouvez facilement trouver une fonction de perte qui se comporte à l'opposé de la fonction de récompense de sorte que la minimisation de cette perte maximisera la récompense.

![Image](https://cdn-media-1.freecodecamp.org/images/1*pr-BLx7eZ90tAuTUNL_w6A.png)

Le réseau de politique a 13 couches, et est appelé réseau de politique « SL » (SL = apprentissage supervisé). Les données provenaient d'un… je vais simplement dire que c'est un site web populaire sur lequel des millions de personnes jouent au Go. À quel point ce réseau de politique SL a-t-il performé ?

Il était plus précis que ce que d'autres chercheurs avaient fait auparavant. Le reste du paragraphe est assez explicite. En ce qui concerne la « politique de déroulage », vous vous souvenez de quelques paragraphes plus tôt, comment Lusha le réseau de politique SL est lent donc il ne peut pas bien s'intégrer avec l'algorithme MCTS ? Et nous avons entraîné une autre version plus rapide de Lusha appelée Jerry qui était son jeune frère ? Eh bien, cela fait référence à Jerry juste ici. Comme vous pouvez le voir, Jerry est seulement moitié moins précis que Lusha MAIS il est des milliers de fois plus rapide ! Il aidera vraiment à accélérer les simulations déroulées du futur, lorsque nous appliquerons le MCTS.

Pour cette prochaine section, vous n'avez *pas* besoin de connaître déjà l'apprentissage par renforcement, mais alors vous devrez supposer que tout ce que je dis fonctionne. Si vous voulez vraiment creuser dans les détails et vous assurer de tout, vous pourriez vouloir lire un peu sur l'apprentissage par renforcement d'abord.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lZ4zT1qpm8wA4n18fjtv9Q.png)

Une fois que vous avez le réseau SL, entraîné de manière supervisée en utilisant les coups des joueurs humains avec les données des coups humains, comme je l'ai dit avant, vous devez la laisser pratiquer par elle-même et s'améliorer. C'est ce que nous faisons ici. Donc vous prenez simplement le réseau de politique SL, vous l'enregistrez dans un fichier, et vous en faites une autre copie.

Ensuite, vous utilisez l'apprentissage par renforcement pour l'affiner. Ici, vous faites jouer le réseau contre lui-même et apprendre des résultats.

Mais il y a un problème dans ce style d'entraînement.

Si vous ne pratiquez que contre UN seul adversaire, et que cet adversaire pratique aussi exclusivement avec vous, il n'y a pas beaucoup de nouvelles choses que vous pouvez apprendre. Vous allez simplement vous entraîner à pratiquer comment battre CE JOUEUR-LÀ. C'est, vous l'avez deviné, du surapprentissage : vos techniques jouent bien contre un adversaire, mais ne généralisent pas bien aux autres adversaires. Alors, comment corrigez-vous cela ?

Eh bien, chaque fois que vous affinez un réseau de neurones, il devient un type de joueur légèrement différent. Donc vous pouvez enregistrer cette version du réseau de neurones dans une liste de « joueurs », qui se comportent tous légèrement différemment, n'est-ce pas ? Super — maintenant, pendant l'entraînement du réseau de neurones, vous pouvez le faire jouer aléatoirement contre de nombreuses versions différentes, plus anciennes et plus récentes, de l'adversaire, choisies dans cette liste. Ce sont des versions du même joueur, mais ils jouent tous légèrement différemment. Et plus vous vous entraînez, plus vous avez de joueurs avec lesquels vous entraîner encore plus ! Bingo !

Dans cet entraînement, la seule chose qui guide le processus d'entraînement est l'objectif ultime, c'est-à-dire gagner ou perdre. Vous n'avez pas besoin d'entraîner spécialement le réseau à faire des choses comme capturer plus de territoire sur le plateau, etc. Vous lui donnez simplement tous les coups légaux possibles qu'il peut choisir, et vous dites : « vous devez gagner ». Et c'est pourquoi l'apprentissage par renforcement est si polyvalent ; il peut être utilisé pour entraîner des réseaux de politique ou de valeur pour n'importe quel jeu, pas seulement le Go.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jhOXPDOCwgzpjw9s9qZl_A.png)

Ici, ils ont testé la précision de ce réseau de politique RL, simplement par lui-même sans aucun algorithme MCTS. Comme vous vous en souvenez, ce réseau peut directement prendre une position de plateau et décider comment un expert la jouerait — donc vous pouvez l'utiliser pour jouer des parties en solo.

Eh bien, le résultat était que le réseau affiné par RL a battu le réseau SL qui n'était entraîné que sur les coups humains. Il a également battu d'autres programmes forts de jeu de Go.

Il faut noter ici que _même avant d'entraîner ce réseau de politique RL, le réseau de politique SL était déjà meilleur que l'état de l'art — et maintenant, il s'est encore amélioré !_ Et nous n'en sommes même pas encore aux autres parties du processus comme le réseau de valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*FK7eVx2Fzc9Vjo4Tkp6yeg.png)

Saviez-vous que les bébés manchots peuvent éternuer plus fort qu'un chien peut aboyer ? En fait, ce n'est pas vrai, mais j'ai pensé que vous aimeriez une petite blague ici pour vous distraire des équations effrayantes ci-dessus. Revenons à l'essai : nous avons terminé l'entraînement de Lusha ici. Maintenant, revenons à Foma — vous souvenez-vous de la « fonction de valeur optimale » : v*(s) -> cela ne vous dit que la probabilité que vous gagniez dans votre position actuelle sur le plateau si les deux joueurs jouent parfaitement à partir de ce point ?

Donc, évidemment, pour entraîner un réseau de neurones à devenir notre fonction de valeur, nous aurions besoin d'un joueur parfait… que nous n'avons pas. Donc nous utilisons simplement notre **_meilleur joueur_**, qui se trouve être notre réseau de politique RL.

Il prend l'état actuel du plateau s, et donne la probabilité que vous allez gagner la partie. Vous jouez une partie et vous connaissez le résultat (victoire ou défaite). Chacun des états de la partie agit comme un échantillon de données, et le résultat de cette partie agit comme l'étiquette. Donc en jouant une partie de 50 coups, vous avez 50 échantillons de données pour la prédiction de valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZumV81-2OpuPzmQzEFvOlA.png)

Lol, non. Cette approche est naïve. Vous ne pouvez pas utiliser tous les 50 coups de la partie et les ajouter à l'ensemble de données.

L'ensemble de données d'entraînement devait être choisi avec soin pour éviter le surapprentissage. Chaque coup dans la partie est très similaire au suivant, car vous ne déplacez qu'une seule fois et cela vous donne une nouvelle position, n'est-ce pas ? Si vous prenez les états à chacun de ces 50 coups et les ajoutez aux données d'entraînement avec la même étiquette, vous avez essentiellement beaucoup de données « en quelque sorte dupliquées », et cela provoque du surapprentissage. Pour éviter cela, vous choisissez uniquement des états de jeu très distincts. Donc, par exemple, au lieu de tous les 50 coups d'une partie, vous n'en choisissez que 5 et les ajoutez à l'ensemble d'entraînement. DeepMind a pris 30 millions de positions à partir de 30 millions de parties différentes, pour réduire toute chance qu'il y ait des données dupliquées. Et cela a fonctionné !

**_Maintenant, quelque chose de conceptuel ici_** : il y a deux façons d'évaluer la valeur d'une position sur le plateau. Une option est une fonction de valeur optimale magique (comme celle que vous avez entraînée ci-dessus). L'autre option est de simplement dérouler dans le futur en utilisant votre politique actuelle (Lusha) et de regarder le résultat final dans ce déroulage. Évidemment, la vraie partie suivrait rarement vos plans. Mais DeepMind a comparé comment ces deux options se comportent. Vous pouvez également faire un mélange de ces deux options. Nous apprendrons un peu plus tard sur ce « paramètre de mélange », alors notez mentalement ce concept !

Eh bien, votre réseau de neurones unique essayant d'approximer la fonction de valeur optimale est ENCORE MEILLEUR que de faire des milliers de simulations mentales en utilisant une politique de déroulage ! Foma a vraiment assuré ici. Lorsqu'ils ont remplacé la politique de déroulage rapide par la politique RL Lusha deux fois plus précise (mais lente), et ont fait des milliers de simulations avec _cela_, cela a mieux fonctionné que Foma. Mais seulement légèrement mieux, et trop lentement. Donc Foma est la gagnante de cette compétition, elle a prouvé qu'elle ne peut pas être remplacée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qZanMJBFb7GtqYmLEUerLw.png)

Maintenant que nous avons entraîné les fonctions de politique et de valeur, nous pouvons les combiner avec MCTS et donner naissance à notre ancien champion du monde, destructeur de grands maîtres, la percée d'une génération, pesant deux cent soixante-huit livres, le seul et unique _Alphaaaaa GO !_

Dans cette section, idéalement, vous devriez avoir une compréhension légèrement plus approfondie du fonctionnement interne de l'algorithme MCTS, mais ce que vous avez appris jusqu'à présent devrait suffire pour vous donner une bonne idée de ce qui se passe ici. La seule chose que vous devriez noter est **_comment_** nous utilisons les probabilités de politique et les estimations de valeur. Nous les combinons pendant les déroulages, pour réduire le nombre de coups que nous voulons dérouler à chaque étape. Q(s,a) représente la fonction de valeur, et u(s,a) est une probabilité stockée pour cette position. Je vais expliquer.

Souvenez-vous que le réseau de politique utilise l'apprentissage supervisé pour prédire les coups d'experts ? Et il ne vous donne pas seulement le coup le plus probable, mais plutôt des **_probabilités_** pour chaque coup possible qui indiquent à quel point il est probable qu'il s'agisse d'un coup d'expert. Cette probabilité peut être stockée pour chacune de ces actions. Ici, ils l'appellent « probabilité a priori », et ils l'utilisent évidemment lors de la sélection des actions à explorer. Donc, essentiellement, pour décider d'explorer ou non un coup particulier, vous considérez deux choses : Premièrement, en jouant ce coup, à quel point êtes-vous susceptible de gagner ? Oui, nous avons déjà notre « réseau de valeur » pour répondre à cette première question. Et la deuxième question est, à quel point est-il probable qu'un expert choisisse ce coup ? (Si un coup est très peu susceptible d'être choisi par un expert, pourquoi perdre du temps à le considérer. Cela, nous l'obtenons du réseau de politique)

Ensuite, parlons du « paramètre de mélange » (voir, nous y revenons !). Comme discuté précédemment, pour évaluer les positions, vous avez deux options : premièrement, utilisez simplement le réseau de valeur que vous avez utilisé pour évaluer les états tout au long. Et deuxièmement, vous pouvez essayer de jouer rapidement une partie de déroulage avec votre stratégie actuelle (en supposant que l'autre joueur jouera de manière similaire), et voir si vous gagnez ou perdez. Nous avons vu comment la fonction de valeur était meilleure que les déroulages en général. Ici, ils combinent les deux. Vous essayez de donner à chaque prédiction une importance de 50-50, ou 40-60, ou 0-100, et ainsi de suite. Si vous attachez un % de X à la première, vous devrez attacher 100-X à la seconde. C'est ce que signifie ce paramètre de mélange. Vous verrez ces résultats d'essais et d'erreurs plus tard dans l'article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7vZGbapsdnNVlkTvpzz_rA.png)

Après chaque déroulage, vous mettez à jour votre arbre de recherche avec les informations que vous avez obtenues pendant la simulation, afin que votre prochaine simulation soit plus intelligente. Et à la fin de toutes les simulations, vous choisissez simplement le meilleur coup.

![Image](https://cdn-media-1.freecodecamp.org/images/1*CGyyDnQjqYSTIwC1d2oNVg.png)

Une idée intéressante ici !

Vous vous souvenez comment le réseau de neurones de politique affiné par RL était meilleur que le réseau de politique entraîné par l'homme SL ? Mais lorsqu'ils les ont placés dans l'algorithme MCTS d'AlphaGo, utiliser le réseau entraîné par l'homme s'est avéré être un meilleur choix que le réseau affiné. Mais dans le cas de la fonction de valeur (dont vous vous souviendrez qu'elle utilise un joueur fort pour approximer un joueur parfait), entraîner Foma en utilisant la politique RL fonctionne mieux que de l'entraîner avec la politique SL.

![Image](https://cdn-media-1.freecodecamp.org/images/1*n_PiVVyVdvzg0NtET63jyQ.png)

« Faire toutes ces évaluations prend beaucoup de puissance de calcul. Nous avons vraiment dû sortir les gros canons pour pouvoir exécuter ces programmes. »

![Image](https://cdn-media-1.freecodecamp.org/images/0*8WFyFNZFCIaegHCy.)
_Une autre photo, de la première partie AlphaGo contre Lee Sedol._

![Image](https://cdn-media-1.freecodecamp.org/images/1*6T2huF9r4oKPJb9QSLUqBA.png)

Explicite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*o6k-P1HQzWCf9SaKDywVZQ.png)

« LOL, notre programme a littéralement soufflé les pantalons de tous les autres programmes qui nous ont précédés »

![Image](https://cdn-media-1.freecodecamp.org/images/1*4JF8kOfmkOb9gKGVZNCqqw.png)

Cela revient à ce « paramètre de mélange » à nouveau. Lors de l'évaluation des positions, donner une importance égale à la fois à la fonction de valeur et aux déroulages a mieux fonctionné que d'utiliser uniquement l'une d'entre elles. Le reste est explicite et révèle une idée intéressante !

![Image](https://cdn-media-1.freecodecamp.org/images/1*7ffhp9i2PXv9I56YwENz3A.png)

Explicite.

![Image](https://cdn-media-1.freecodecamp.org/images/1*DM09OIIgih_ALPwch3TT9A.png)

Explicite. Mais relisez cette phrase soulignée en rouge. J'espère que vous pouvez voir clairement maintenant que cette ligne ici est à peu près le résumé de tout ce que ce projet de recherche était.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mCqgpWNDdte7DCJNQTlFlg.png)

Paragraphe de conclusion. « Laissez-nous nous vanter un peu plus ici parce que nous le méritons ! » :)

**Oh et si vous êtes un scientifique ou une entreprise technologique, et avez besoin d'aide pour expliquer votre science à des non-techniciens pour le marketing, les relations publiques ou la formation, etc., je peux vous aider. Envoyez-moi un message sur Twitter : @mngrwl**