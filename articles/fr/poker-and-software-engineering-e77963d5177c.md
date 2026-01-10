---
title: Poker et Ingénierie Logicielle
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-03-19T18:14:16.000Z'
originalURL: https://freecodecamp.org/news/poker-and-software-engineering-e77963d5177c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cZLconGMB4cKdmnUF0rZBQ.jpeg
tags:
- name: business
  slug: business
- name: Machine Learning
  slug: machine-learning
- name: poker
  slug: poker
- name: software development
  slug: software-development
- name: startup
  slug: startup
seo_title: Poker et Ingénierie Logicielle
seo_desc: 'By Jeff Meyerson

  As a poker player becomes a software engineer, certain trends about human-computer
  interaction become apparent:


  human poker players will lose to computers in the near future

  every field is plagued by the madness of crowds

  emotional ...'
---

Par Jeff Meyerson

Alors qu'un joueur de poker devient ingénieur logiciel, certaines tendances concernant l'interaction homme-machine deviennent évidentes :

* les joueurs de poker humains perdront face aux ordinateurs dans un avenir proche
* chaque domaine est affecté par la folie des foules
* le travail émotionnel est un avantage concurrentiel
* la créativité et l'autonomie sont nécessaires pour réussir

Cet article explore chacune de ces tendances, expliquant pourquoi elles sont importantes pour les joueurs de poker, les ingénieurs logiciels et tout le monde.

**Jeux Automatisés**

En 2008, le poker était le sport parfait pour la symbiose homme-machine. Ce que [Tyler Cowen a dit](http://www.newyorker.com/business/currency/are-computers-making-society-more-unequal) à propos des [échecs en style libre](https://en.wikipedia.org/wiki/Advanced_Chess) s'appliquait également au poker :

> _Même les ordinateurs très puissants n'ont pas ce sens méta-rationnel de l'ambiguïté. Aujourd'hui, les équipes homme-plus-machine sont meilleures que les machines seules. Cela montre qu'il y aura toujours une place pour un élément humain._

Au poker, un humain avec un affichage "tête-à-tête" statistique peut prendre des décisions plus justifiées mathématiquement qu'un humain sans un tel outil.

Les affichages tête-à-tête créent la version poker des "équipes homme-plus-machine".

![Image](https://cdn-media-1.freecodecamp.org/images/0*IK2rBEc26WeCM1iL.)

Une thèse de [_Average is Over_](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=1&cad=rja&uact=8&ved=0ahUKEwiNzZmw68zLAhVW22MKHdV2CoUQFggdMAA&url=http%3A%2F%2Fwww.amazon.com%2FAverage-Is-Over-Powering-Stagnation%2Fdp%2F0525953736&usg=AFQjCNGMtd-c5RSRlSTubgz-uug-WZVEaA&sig2=2l0CeC5zCxIc5wBxIef-5w) est qu'un humain ne sera employable à l'avenir qu'en trouvant une carrière où le raisonnement humain apporte une valeur défendable au processus de résolution de problèmes d'un ordinateur.

Si les responsabilités de l'humain ne sont pas défendables, l'humain sera obsolète.

Dans [un article de blog ultérieur](http://marginalrevolution.com/marginalrevolution/2013/11/what-are-humans-still-good-for-the-turning-point-in-freestyle-chess-may-be-approaching.html), Cowen aborde le "basculement" qui peut se produire lorsqu'un problème computationnel n'a plus besoin d'assistance humaine :

> _Très bientôt, les programmes informatiques pourraient être suffisamment bons pour que l'ajout de l'humain à l'ordinateur n'apporte aucun avantage. (Cela a été le cas pour les dames depuis un certain temps, car ce jeu est entièrement résolu.)_

> _Pensez à pourquoi un tel basculement pourrait être en cours, même si les échecs sont loin d'être entièrement résolus._

Les joueurs de poker ont été [de plus en plus battus](https://en.wikipedia.org/wiki/Polaris_%28poker_bot%29) par des [machines](http://www.pokernews.com/news/2015/06/suspected-bots-on-pokerstars-under-investigation-21860.htm) au cours des [10 dernières années](http://poker.cs.ualberta.ca/). Il n'est pas surprenant que l'[AlphaGo](https://en.wikipedia.org/wiki/AlphaGo) de Google ait battu le champion humain Lee Sedol.

Si Google décidait de battre les humains au poker, ce serait [un exercice trivial](https://www.quora.com/Why-are-certain-games-so-difficult-for-computers/answer/Jeff-Meyerson?srid=po1Y&share=0c798983) pour les chercheurs.

Le poker semble différent du Go ou des échecs, car il y a du non-déterminisme. Vous commencez avec deux cartes, mais vous ne savez pas comment le tableau va se développer. Il semblerait que le destin soit aux commandes, contrairement au Go et aux échecs, qui n'ont pas d'éléments aléatoires.

Avec seulement 4 couleurs et 13 valeurs, un jeu de poker a un facteur de branchement trivial. Le non-déterminisme est si minimal pour un ordinateur qu'il est effectivement déterministe.

Imaginez si AlphaGo devait apprendre à jouer à une version de Go avec la règle suivante : au début de chaque tour, lancez une pièce. Si vous perdez le lancer, vous ne pouvez pas bouger. S'adapter à cette règle serait trivial. C'est l'ampleur du non-déterminisme dans le poker.

Le poker, les échecs et le Go ont de petits espaces de décision. Les règles ne changent jamais, les pièces de jeu ne changent jamais, il y a un non-déterminisme minimal.

Un ordinateur peut évaluer une main de poker comme il le ferait pour un modèle de Markov caché, mais il faudra un travail comparable à celui de l'équipe AlphaGo pour qu'un ordinateur soit formé à construire un modèle avec précision.

![Image](https://cdn-media-1.freecodecamp.org/images/0*8bpG1HYB6iUYhZNf.)

Le métier de joueur de poker professionnel a été un mauvais choix à long terme pour un humain depuis plus d'une décennie, car il est vulnérable à l'automatisation.

Des jeux comme le Go, le poker et les échecs peuvent être automatisés avec des techniques d'apprentissage automatique que nous comprenons aujourd'hui. Les règles, le schéma des pièces de jeu et les objectifs sont faciles à définir, donc ces jeux sont mûrs pour l'_apprentissage supervisé_ et l'_apprentissage par renforcement_.

[Yann LeCun](https://en.wikipedia.org/wiki/Yann_LeCun) a protesté contre le battage médiatique autour de la victoire d'AlphaGo :

> _Comme je l'ai dit dans des déclarations précédentes : la plupart de l'apprentissage humain et animal est de l'apprentissage non supervisé. Si l'intelligence était un gâteau, l'apprentissage non supervisé serait le gâteau, l'apprentissage supervisé serait le glaçage sur le gâteau, et l'apprentissage par renforcement serait la cerise sur le gâteau. Nous savons comment faire le glaçage et la cerise, mais nous ne savons pas comment faire le gâteau._

> _Nous devons résoudre le problème de l'apprentissage non supervisé avant même de penser à atteindre une véritable IA. Et ce n'est qu'un obstacle que nous connaissons. Qu'en est-il de tous ceux que nous ne connaissons pas ?_

Le poker est vulnérable aux mêmes techniques d'apprentissage supervisé et par renforcement qui ont permis à AlphaGo de battre Lee Sedol au Go.

L'[_apprentissage supervisé_](https://en.wikipedia.org/wiki/Supervised_learning) _est la tâche d'apprentissage automatique consistant à inférer une fonction à partir de données d'entraînement étiquetées._ Des milliards d'histoires de mains existent pour qu'un bot de poker s'entraîne. Ces histoires de mains sont courtes et bien schématisées, parfaites pour être consommées par un automate.

L'[_apprentissage par renforcement_](http://www.scholarpedia.org/article/Reinforcement_learning) _est l'apprentissage par interaction avec un environnement._ Les bots de poker peuvent tester et paralléliser leurs stratégies sur les milliers de jeux de poker gratuits ou bon marché sur Internet. Le [signal de récompense](http://www.scholarpedia.org/article/Reward_signals) d'une stratégie peut être défini comme le profit sur un horizon de temps donné.

Aujourd'hui, les professionnels humains survivants se cannibalisent. Avant longtemps, même les meilleurs de ces joueurs perdront leur argent face aux bots.

Les jeux qui ne peuvent pas être facilement résolus avec un simple apprentissage supervisé et par renforcement ne seront pas automatisés dans un avenir proche. Les exemples incluent Magic : l'Assemblée, Sim City, Minecraft et Donjons et Dragons.

Les caractéristiques de ces jeux incluent :

* de grands facteurs de branchement aux points de non-déterminisme
* un grand corpus de pièces de jeu avec un schéma de pièces de jeu difficile à normaliser
* une nature non-nulle
* des objectifs subjectifs des joueurs
* des états de fin de jeu et des conditions de victoire largement variés

Les règles, le succès et l'échec sont faciles à définir dans le Go, les échecs et le poker.

En revanche, il est difficile d'expliquer ce qui fait un joueur idéal de Minecraft. Différents joueurs de Minecraft ont des objectifs et des conditions de victoire différents. Nous n'avons aucun moyen de superviser un ordinateur pour réussir à Minecraft, ou de récompenser un ordinateur pour son comportement souhaitable dans Minecraft.

Le poker a 52 types de pièces de jeu, les échecs en ont 6, et le Go en a 1. Magic : l'Assemblée a 16 000+ cartes uniques. Nous ne savons pas comment enseigner à un ordinateur de comprendre les relations stratégiques complexes parmi ces 16 000 types de cartes différents.

![Image](https://cdn-media-1.freecodecamp.org/images/0*ftcDwdhGL71zoGn6.)

Donjons et Dragons est coopératif, à somme positive, hautement aléatoire et orienté autour d'objectifs subjectifs des joueurs. Un ordinateur ne rivalisera pas avec l'humanisme créatif et utilitaire d'un maître de donjon talentueux de sitôt, car nous n'avons pas de bonne façon de codifier les traits d'un jeu réussi de Donjons et Dragons.

En tant qu'humains, ce sont les jeux que nous devrions étudier et célébrer.

[Le Go, les échecs et le poker étaient d'excellents passe-temps avant la renaissance des jeux que nous avons eue au cours des 30 dernières années. Aujourd'hui, il existe de meilleurs jeux.](https://www.quora.com/Is-learning-to-play-poker-worth-it)

AlphaGo prouve que le Go est juste une autre routine qui peut être automatisée, comme la préparation de fast-food ou la conduite de camions.

Plutôt que de passer notre temps sur les échecs, le Go ou le poker, le temps humain est mieux dépensé à jouer à des jeux qui reflètent des activités qu'un ordinateur a du mal à accomplir.

Choisir une carrière de joueur de poker professionnel aujourd'hui, c'est comme choisir d'être un chauffeur Uber ou un employé d'entrepôt Amazon : vous attendez d'être automatisé.

**La folie des foules**

Dans le poker comme dans le logiciel, les participants au marché confondent l'[analyse technique](https://en.wikipedia.org/wiki/Technical_analysis) avec l'[analyse fondamentale](https://en.wikipedia.org/wiki/Fundamental_analysis).

> L'analyse technique _est une méthodologie d'analyse de sécurité pour prévoir la direction des [prix](https://en.wikipedia.org/wiki/Prices) à travers l'étude des données de marché passées, principalement le prix et le volume._

> _Contrastant avec l'analyse technique, il y a_ [l'analyse fondamentale](https://en.wikipedia.org/wiki/Fundamental_analysis)_, l'étude des [facteurs économiques](https://en.wikipedia.org/wiki/Economic) qui influencent la manière dont les investisseurs évaluent les marchés financiers. L'analyse technique soutient que les prix reflètent déjà tous les facteurs fondamentaux sous-jacents._

Les analystes techniques purs croient dogmatiquement en la sagesse des foules.

Les analystes techniques croient qu'il n'y a pas de secrets, et que toutes les connaissances humaines sur l'avenir sont intégrées dans l'évaluation de la foule du présent.

Raisonner sur les marchés en utilisant des premiers principes peut conduire à des décisions qui diffèrent de la sagesse des foules. C'est une forme d'analyse _fondamentale_.

En 2003, un comptable devenu joueur de poker amateur nommé Chris Moneymaker a remporté les World Series of Poker. Cela a coïncidé avec l'augmentation de la couverture vidéo de l'événement par ESPN. Les gens ont commencé à aller dans les restaurants pour regarder le poker comme si c'était le Super Bowl.

Alors que le poker devenait populaire dans le monde entier, de nombreux joueurs non qualifiés ont commencé à jouer au jeu.

En 2004, n'importe quel adolescent doué en informatique pouvait apprendre à jouer au poker et prendre de l'argent aux nombreux Américains non qualifiés qui essayaient de devenir le prochain Chris Moneymaker.

Il y avait une richesse d'informations sur la façon de gagner au poker en ligne, et cela ne nécessitait pas beaucoup d'efforts pour étudier suffisamment de ces informations pour réussir.

Pour les adolescents qui étaient doués pour les jeux en ligne, c'était une ruée vers l'or. Les adolescents qui avaient des compétences dans des jeux comme StarCraft et Magic Online ont rapidement appris le poker et ont commencé à écraser les amateurs non qualifiés.

En 2006, la bulle du poker en ligne a commencé à fuir avec le [passage de l'UIGEA](https://en.wikipedia.org/wiki/Unlawful_Internet_Gambling_Enforcement_Act_of_2006). La loi sur l'application des jeux d'argent illégaux sur Internet de 2006 a rendu difficile pour les joueurs amateurs de financer leurs comptes de poker en ligne avec des cartes de crédit.

En 2008, l'économie mondiale s'est effondrée, réduisant davantage le nombre de joueurs occasionnels sur Internet.

En 2011, le [Vendredi Noir](https://en.wikipedia.org/wiki/United_States_v._Scheinberg) s'est produit et il a été découvert que Full Tilt Poker était un schéma de Ponzi.

Depuis 2006, le poker en ligne est devenu de plus en plus difficile, et un nombre croissant de joueurs de poker se sont plaints de l'environnement macro du poker.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1ZNyIaAEhNCr7jCN.)

Google Trends indique que la popularité du poker a chuté de 80 % après le passage de l'UIGEA à la fin de 2006.

Depuis 2006, les joueurs de poker disent : "Il n'y a plus d'amateurs faibles. Nous nous battons tous les uns contre les autres, et parce que nous avons tous les mêmes stratégies, nous lançons essentiellement des pièces de monnaie les uns contre les autres. Le poker est devenu un jeu de variance complète."

Aucun de cela n'importe à [Dan Cates](https://en.wikipedia.org/wiki/Daniel_Cates), [Mike McDonald](https://en.wikipedia.org/wiki/Michael_McDonald_%28poker_player%29), et [Patrik Antonius](https://en.wikipedia.org/wiki/Patrik_Antonius). Leur stratégie est suffisamment meilleure que celle de leurs adversaires pour qu'ils aient une opportunité _fondamentale_. Ils ont continué à gagner malgré une augmentation brutale de la concurrence.

Les joueurs de poker moyens qui ne sont ni innovants ni résilients ont vu les événements de 2006-2011 comme des menaces _fondamentales_ pour leur viabilité en tant que joueurs de poker professionnels, alors qu'en fait ces problèmes étaient de nature _technique_.

Les détails du marché ont changé, mais l'opportunité _fondamentale_ est restée : les meilleurs joueurs ont toujours assez d'avantage pour bien gagner leur vie en jouant au poker.

Lorsque les investisseurs et les entrepreneurs parlent d'une "bulle" dans la Silicon Valley, ils parlent d'une bulle _technique_. Pas d'une bulle _fondamentale_.

L'informatique en nuage bon marché, les téléphones mobiles, les marchés émergents de la Chine et de l'Inde, les réseaux sociaux, Docker, Bitcoin, l'économie de la chaîne d'approvisionnement, les drones, la fintech, la réalité virtuelle : ce sont des opportunités _fondamentales_ avec un énorme potentiel de croissance.

Lorsque les investisseurs et les entrepreneurs parlent de la façon dont "[L'hiver arrive](http://recode.net/2015/08/20/bill-gurley-to-unicorns-winter-is-coming-you-ready/)", quelles sont les bases citées de leur panique ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*fdueSWl-wSGSaTPVN8yR8A.png)

L'analyse _technique_ qui a peu à voir avec la viabilité des technologies de rupture stimulant la croissance.

Les investisseurs institutionnels se retirent des marchés privés ? La Chine est une maison de cartes ? Le pétrole ? La Grèce ? Les modèles de graphiques _techniques_ de 1999 montrant une hausse qui reflète les marchés privés modernes ? Les startups de livraison de nourriture soutenues par d'autres startups ?

Il n'y a pas de signe plus sûr de la folie des foules que lorsque les investisseurs regardent les uns les autres plutôt que les fondamentaux en essayant de deviner la vraie nature des marchés privés.

Les investisseurs qui prétendent se fier à la pensée à long terme oublient souvent les fondamentaux technologiques qui déterminent la viabilité à long terme des entreprises.

De 2006 à 2011, des milliers de joueurs de poker professionnels ont quitté le jeu, convaincus qu'un certain récit populaire était vrai : le poker était finalement devenu un jeu de chance.

> _"Quand vous y pensez comme un billet de loterie, quand vous dites, 'Cela pourrait marcher, cela pourrait ne pas marcher, je ne sais pas', vous vous êtes déjà psyché pour perdre. Vous vous êtes convaincu de ne pas faire autant de travail. Là où nous avons le mieux réussi au fil des ans, c'est là où nous avions beaucoup de conviction, où nous étions prêts à mettre beaucoup d'argent dans les choses."_

> [_-Peter Thiel_](http://www.inc.com/jeff-bercovici/peter-thiel-startup-red-flags.html)

Les joueurs de poker faibles ont abandonné lorsque la bulle a éclaté parce qu'ils étaient convaincus que le poker était devenu si compétitif qu'il était impossible d'avoir une stratégie efficace et différenciée.

Les joueurs de poker qui ont foi en leur propre créativité continuent de gagner leur vie grâce au travail acharné et à l'étude.

Dans un avenir proche, les [anti-portfolios](https://www.bvp.com/portfolio/anti-portfolio) des investisseurs technologiques au comportement de troupeau gonfleront à des taux sans précédent, car les investisseurs chercheront par erreur des conseils les uns chez les autres, plutôt que de regarder les opportunités fondamentales offertes par notre boom technologique actuel.

**Travail Émotionnel**

En 2004 et 2005, les étudiants et les jeunes professionnels bien éduqués ont commencé à jouer au poker parce que c'était un moyen à faible risque et facile de gagner de l'argent. Les joueurs de poker amateurs américains riches perdaient de l'argent face à ces étudiants et jeunes professionnels.

Il y avait une énorme différence de compétence entre ces deux classes de joueurs.

Les étudiants et les jeunes professionnels bien éduqués lisaient des livres sur les statistiques, la psychologie et la stratégie de poker complexe. Les Américains amateurs riches regardaient le poker à la télévision et essayaient de copier ce qu'ils voyaient les professionnels faire à l'écran.

![Image](https://cdn-media-1.freecodecamp.org/images/1*AvGLra5EzfIqx_Cnh1CKUw.png)

Pour les étudiants et les jeunes professionnels bien éduqués, la seule exigence pour réussir au poker à haut risque était la patience.

La patience était importante parce que les Américains amateurs riches jouaient si mal qu'un étudiant pouvait s'asseoir et attendre des opportunités pour mettre de l'argent dans le pot avec un avantage de 10:1.

De 2006 à 2011, des circonstances législatives et économiques ont poussé de nombreux joueurs amateurs américains hors du jeu. Alors que les amateurs riches disparaissaient du poker, le champ des hauts risques est devenu à 95 % professionnel.

En 2005, une table de poker en ligne moyenne à 6 joueurs contenait 3 professionnels et 3 amateurs. En 2006, une table moyenne contenait 4 professionnels, 1 amateur compétent et 1 amateur faible. En 2008, la plupart des tables étaient entièrement remplies de professionnels et d'amateurs compétents.

Les adversaires faibles étaient introuvables.

Dans ce nouveau monde de joueurs de poker presque entièrement professionnels, la résilience émotionnelle était plus importante que la patience.

Les joueurs professionnels ne pouvaient plus attendre un avantage clair de 10:1 ou 5:1 sur leurs adversaires. Les étudiants et les jeunes professionnels timides qui maintenaient une stratégie patiente et non créative ont commencé à perdre de l'argent.

Des joueurs chaotiques et hyperagressifs ont commencé à forcer les jeux dans une direction avec une variance accrue, faisant douter leurs adversaires de leur risque présumé de ruine. L'exemple le plus extrême de cela était Viktor Blom, un joueur de haut risque dont la volonté de se ruiner semblait dépasser sa peur, menant à un style où il surenchérissait fréquemment le pot.

Un professionnel jouant contre Viktor Blom savait que plus d'argent serait [perdu](http://www.cardrunners.com/images/jun20%281%29.png) ou [gagné](http://www.pokernews.com/news/2009/12/pokernews-exclusive-isildur1-speaks-about-the-4-million-7714.htm) dans un court laps de temps que contre n'importe qui d'autre.

![Image](https://cdn-media-1.freecodecamp.org/images/0*K5TlUEK2n_OV5vPD.)

Pour Viktor Blom, le coût principal de l'utilisation de cette stratégie était que le contrôle émotionnel est plus difficile à maintenir lorsque vous gagnez et perdez des millions de dollars plus fréquemment que vos adversaires.

Le compromis en valait la peine. La stratégie brillante de Viktor Blom lui a donné à la fois un [avantage mathématique](http://andr3w321.com/overbet-math/) et un [avantage de réputation](https://www.highstakesdb.com/6676-the-effect-of-isildur1.aspx).

Pourquoi cela est-il pertinent pour l'ingénierie logicielle ?

> _Le travail émotionnel est disponible pour nous tous, mais il est rarement exploité comme un avantage concurrentiel._

> _-Seth Godin_

Viktor Blom a obtenu un énorme avantage concurrentiel en s'engageant dans un _travail émotionnel_.

Il a délibérément joué au poker de manière à mettre tout le monde à la table mal à l'aise, car il se jugeait plus capable de gérer ce malaise que tout le monde.

La plupart des ingénieurs logiciels évitent le travail émotionnel.

Lorsque les ingénieurs logiciels choisissent de travailler dans une grande entreprise parce que cela semble luxueux et sûr, ils font une erreur. Il n'y a jamais eu de meilleur moment pour les ingénieurs de prendre des risques extrêmes avec leur carrière.

Les ingénieurs logiciels sont incroyablement privilégiés. Nos emplois de 9 à 5 sont agréables et créatifs, et beaucoup d'entre nous ont un temps libre significatif pour faire ce que nous voulons. Pendant leur temps libre, les ingénieurs logiciels devraient se dépasser et exercer un travail émotionnel, et voir ce dont ils sont capables.

En 2005, les joueurs de poker professionnels avaient la possibilité de mener un style de vie insouciant. Nous supposions que la ruée vers l'or du poker en ligne ne se terminerait jamais. Beaucoup d'entre nous ont agi de manière irresponsable avec l'argent, comme si nous pouvions gagner 30 000 dollars par mois pour le reste de notre vie.

![Image](https://cdn-media-1.freecodecamp.org/images/0*lIZqZQ49UQmh6nJ4.)

Lorsque l'économie du poker s'est effondrée, la vie de nombreux joueurs de poker professionnels s'est effondrée avec elle. Nous nous étions habitués à la belle vie, mais nous n'avions pas travaillé assez dur pour capitaliser pleinement sur l'opportunité à portée de main.

Les joueurs de poker qui ont travaillé dur et intelligemment pendant les années fastes de 2003-2007 ont pu survivre à la crise.

La plupart des joueurs de poker n'ont pas travaillé dur et intelligemment pendant le boom.

La plupart des joueurs de poker n'ont pas pratiqué le _travail émotionnel_ en 2005, lorsque le jeu était facile. Lorsque le poker est devenu difficile en 2008, ces joueurs étaient fragiles. La plupart des joueurs de poker professionnels n'ont pas pu s'adapter au paysage nouvellement compétitif.

En revanche, [Viktor Blom s'est habitué aux activités à haut risque vers 2005, peu après avoir commencé à jouer au poker :](https://en.wikipedia.org/wiki/Viktor_Blom)

> _Après quelques semaines de jeu, Blom90 jouait régulièrement à des sit n gos de 530 $. Après quelques mois de jeu supplémentaires, le jeune Viktor Blom de 15 ans avait gagné plus de 275 000 $ au total sur divers sites. Il a ensuite collecté tout l'argent sur un site et s'est attaqué aux jeux de cash et aux sit n gos avec des buy-ins plus élevés. Cela a abouti à la perte de tout l'argent. Il a ensuite reconstitué une bankroll et déposé 3 000 $ sur le même site, il s'est attaqué aux sit'n gos avec des buy-ins élevés et a commencé à gagner de plus en plus d'argent. Après avoir reconstitué sa bankroll à 50 000 $, il s'est attaqué à un régulier de sit'n go de 310 $ et a une fois de plus tout perdu._

Viktor Blom a fait faillite deux fois en tant qu'adolescent.

Faire faillite n'est pas toujours vertueux. Pour certains joueurs de poker, être ruiné est une addiction. Ils feront une carrière du cycle maniaque-dépressif consistant à accumuler d'énormes sommes d'argent, pour tout perdre ensuite.

Viktor Blom est devenu [antifragile](https://en.wikipedia.org/wiki/Antifragile#Introduction) grâce à ses premières expériences de faillite.

Cela était bien avant sa série de victoires en 2009. Lorsque l'économie du poker s'est effondrée, cela n'a pas sévèrement affecté Viktor Blom car il s'était forcé à se challenger pendant des années auparavant.

Au début de sa carrière, Viktor a pris des risques sans relâche. La force de l'économie du poker en 2005 lui a permis de reconstruire sa bankroll chaque fois qu'il faisait faillite.

Les ingénieurs logiciels d'aujourd'hui devraient agir comme Viktor Blom en 2005.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oUJuS1o6X1m-YJcO.)
_Viktor Blom a compris le pouvoir de la faillite_

En 2005, Viktor pouvait perdre toute sa bankroll en jouant à haut risque, il était facile de la reconstruire en jouant à des jeux de mi-stakes. En augmentant le risque de ruine à court terme, il a diminué le risque de ruine à long terme.

En 2016, un ingénieur logiciel peut quitter un emploi d'entreprise et construire des projets secondaires pendant 6 mois. Si aucun des projets secondaires ne se transforme en un produit commercialisable, cet ingénieur peut toujours retourner à l'entreprise, et peut probablement demander un salaire plus élevé grâce aux nouvelles compétences apprises en travaillant sur ces projets secondaires.

Prendre des risques est un acte de _travail émotionnel_.

Les ingénieurs logiciels peuvent construire un produit, démarrer une entreprise, écrire un algorithme, lancer une fusée ou programmer une voiture autonome. Toutes ces activités nécessitent des risques. Mais de nombreux ingénieurs logiciels passent leur temps libre à faire des activités à très faible risque.

Si vous vous engagez à être un ingénieur logiciel prêt à prendre des risques et à vous engager dans un travail émotionnel, vous pouvez facilement vous démarquer des autres.

**Construisez Votre Propre Navire**

J'ai passé mes [années de fin d'adolescence à jouer au poker](https://www.quora.com/What-is-it-like-to-earn-a-living-through-poker/answer/Jeff-Meyerson?srid=po1Y&share=d4c57ed4) et je n'ai pas écrit une ligne de code avant le début de la vingtaine. La plupart des ingénieurs réussis que je connais codaient pendant leur adolescence.

Pour rattraper mon retard, j'ai dû tirer parti des compétences que j'ai apprises en jouant au poker.

De nombreux nouveaux ingénieurs d'aujourd'hui sont confrontés au même problème.

Vous apprenez à coder comme deuxième carrière, et cela peut sembler très difficile car cela donne l'impression de tout jeter du passé et de commencer à zéro.

Que vous soyez formé comme barista, commercial ou biologiste, vous devez trouver des compétences de votre passé que vous pouvez apporter dans votre carrière d'ingénieur logiciel.

Un barista est excellent pour séquencer des opérations moins triviales qu'elles n'en ont l'air. Un commercial comprend comment travailler avec des clients et répondre à leurs besoins dans des projets à enjeux élevés. Un biologiste comprend les abstractions et comment penser aux parties individuelles d'un système en isolation.

Être un outsider est un désavantage au début, mais avec le temps, cela a une valeur énorme.

Chaque emploi que vous avez eu dans le passé a des compétences transférables qui peuvent être appliquées à l'ingénierie logicielle. Identifier les avantages que vous avez développés à partir de vos expériences passées peut vous aider à vous sentir plus confiant.

Lorsque vous commencez en tant qu'ingénieur logiciel, de nombreux développeurs vous diront quoi faire et comment vous devez agir.

Ces personnes disent : Apprenez JavaScript. Allez dans un boot camp de codage. Écrivez des tests pour tout votre code. Apprenez à créer des applications mobiles. Utilisez StackOverflow. Apprenez la programmation fonctionnelle. Devenez un maître de la ligne de commande.

Chaque personne apprend l'ingénierie logicielle différemment.

L'ingénierie logicielle est un art. Pour réussir en tant qu'artistes, nous devons décider quels outils et méthodologies nous voulons utiliser. Nous devons décider _pour nous-mêmes_.

Le poker est aussi un art. Il n'y a pas de manière objectivement "meilleure" de jouer au poker. Les joueurs de poker développent leur forme d'art à travers des années d'expérience subjective.

![Image](https://cdn-media-1.freecodecamp.org/images/0*KGL-yykngEd2nmNL.)

Haseeb Qureshi a décrit cela dans "Poker as Shipbuilding", une section de son chef-d'œuvre [The Philosophy of Poker](http://www.amazon.com/How-Be-Poker-Player-Philosophy-ebook/dp/B00HFDJU6A/ref=sr_1_1?ie=UTF8&qid=1458343923&sr=8-1&keywords=philosophy+of+poker) :

> _Imaginez que votre jeu de poker est un navire, et vous, le joueur de poker, êtes le constructeur de navires._

> _Votre navire n'est pas une extension de vous-même. Ce n'est pas quelque chose d'interne, qui existe dans votre esprit. Nous voulons imaginer plutôt qu'un jeu de poker est un objet externe — votre objet, certainement, le produit de votre artisanat et de votre travail acharné, mais néanmoins quelque chose qui existe "là-bas", prêt à être analysé, démonté et remonté. En tant que constructeur de navires, vous avez beaucoup de choix à faire sur la façon de construire votre navire._

> _Quel type de jeu de poker voulez-vous construire ?_

> _Vous regardez la mer du poker et voyez des centaines de milliers de navires, tous construits différemment, avec des idées et des intentions apparemment variées derrière leur construction. Naturellement, vous ne voulez choisir que les meilleurs navires à imiter. Vous regardez donc des vidéos des grands joueurs, vous suivez les jeux à enjeux élevés, vous lisez des articles bien écrits — et vous essayez de façonner votre navire à leur image._

> _Mais il y a une faille fatale intégrée dans ce processus : peu importe le nombre de navires que vous regardez, qu'il s'agisse de centaines ou de milliers, même des navires de la meilleure qualité, aucune quantité d'étude de tels navires ne vous permettra de construire un navire pour vous-même. Parce que_ regarder _des navires est un processus très différent de celui de_ construire _réellement._

En tant que joueur de poker, j'ai échoué parce que j'ai copié ce que je voyais les autres faire sans comprendre le raisonnement derrière cela. Je n'ai pas construit mon propre navire en tant que joueur de poker.

Si votre stratégie est de copier les autres, vous ne pouvez pas vous différencier du pool de talents mondial. Vous ne pouvez pas vous différencier des machines qui deviennent plus intelligentes chaque jour.

En tant qu'ingénieur logiciel, j'essaie de ne pas faire l'erreur de copier aveuglément ce qui est à la mode. Il y a une décennie, j'ai perdu la plupart de mon argent parce que je suivais simplement ce que les autres faisaient.

Il est utile d'avoir un tel historique de douleur associé à la copie des autres.

Pour la plupart des gens, copier aveuglément les autres soulage la douleur. Lorsque je sens que je copie les autres sans comprendre pourquoi, ma réaction instinctive est d'avoir honte et peur de ma propre tendance à répliquer.

Si vous ne copiez pas le comportement des autres ingénieurs, votre manager ne peut pas vous traiter comme une marchandise hautement prévisible. Vous ne pouvez pas être mis en route et assigné à une tâche comme un cluster EC2.

Si vous n'êtes pas une marchandise hautement prévisible, vous serez probablement licencié ou promu.

Malheureusement, [la plupart des entreprises ne sont pas conçues pour soutenir ou encourager le comportement entrepreneurial](https://www.quora.com/Why-are-entrepreneurs-bad-employees/answer/Auren-Hoffman).

De nombreux ingénieurs logiciels se retrouvent coincés dans des emplois qui les rendent malheureux parce qu'ils se contentent de suivre les ordres et ne réfléchissent pas par eux-mêmes, en considérant toutes leurs options et en voyant le tableau d'ensemble.

[Les ingénieurs logiciels doivent construire leurs propres navires.](http://softwareengineeringdaily.com/2016/02/12/10-philosophies-for-developers/)

Si votre stratégie en tant qu'ingénieur logiciel est de ne copier que ce que vous avez déjà vu, vous suivrez les gens dans les anciennes technologies. Vous créerez des entreprises dans des marchés saturés. Vous vous retrouverez entouré d'autres personnes qui ont peur de créer leurs propres stratégies, technologies et produits.

Si vous construisez votre propre navire, le monde est plein d'opportunités.