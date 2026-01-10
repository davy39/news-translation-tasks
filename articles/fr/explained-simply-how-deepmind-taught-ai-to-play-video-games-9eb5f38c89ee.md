---
title: 'Expliqué simplement : Comment DeepMind a appris à l''IA à jouer à des jeux
  vidéo'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-27T12:58:05.000Z'
originalURL: https://freecodecamp.org/news/explained-simply-how-deepmind-taught-ai-to-play-video-games-9eb5f38c89ee
coverImage: https://cdn-media-1.freecodecamp.org/images/0*1yGJPwNHuhDZLyLq.jpg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: 'Expliqué simplement : Comment DeepMind a appris à l''IA à jouer à des
  jeux vidéo'
seo_desc: 'By Aman Agarwal

  Google’s DeepMind is one of the world’s foremost AI research teams. They’re most
  famous for creating the AlphaGo player that beat South Korean Go champion Lee Sedol
  in 2016.

  The key technology used to create the Go playing AI was Deep...'
---

Par Aman Agarwal

DeepMind de Google est l'une des équipes de recherche en IA les plus en vue au monde. Ils sont surtout célèbres pour avoir créé le joueur AlphaGo qui a battu le champion sud-coréen de Go, Lee Sedol, en 2016.

La technologie clé utilisée pour créer l'IA jouant à Go était l'apprentissage par renforcement profond.

Revenons 4 ans en arrière, lorsque [DeepMind a construit pour la première fois une IA capable de jouer à des jeux Atari](https://deepmind.com/research/publications/playing-atari-deep-reinforcement-learning/) des années 70. Des jeux comme _Breakout, Pong_ et _Space Invaders_. C'est cette recherche qui a conduit à AlphaGo, et à l'acquisition de DeepMind par Google.

![Image](https://cdn-media-1.freecodecamp.org/images/1*04OeIRzClXSYqHrfIro39w.jpeg)
_Space Invaders !_

Aujourd'hui, nous allons prendre cet article de recherche original et le décomposer paragraphe par paragraphe. Cela le rendra plus accessible pour les personnes qui commencent tout juste à apprendre l'apprentissage par renforcement. Et pour ceux qui n'utilisent pas l'anglais comme première langue (ce qui rend très difficile la lecture de tels articles).

Voici l'article original si vous souhaitez essayer de le lire :

#### Quelques notes rapides (au cas où vous n'iriez pas jusqu'au bout de cet article de 20 minutes)

Les explications ici sont faites par deux personnes :

1. [Moi](http://aman-agarwal.com), un ingénieur en voitures autonomes
2. [Qiang Lu](https://www.linkedin.com/in/luqiang21/), un candidat au doctorat et chercheur à l'Université de Denver

Nous espérons que notre travail vous fera gagner beaucoup de temps et d'efforts si vous deviez étudier cela par vous-même.

#### Et si vous êtes plus à l'aise pour lire le chinois, voici une traduction *non officielle* [de cet essai](https://kknews.cc/sports/b48mjln.html).

1. Nous aimons vos applaudissements, mais nous aimons encore plus vos commentaires. Déchargez tout ce qui vous passe par la tête — sentiments, suggestions, corrections ou critiques — dans la boîte à commentaires !
2. J'ai l'intention d'écrire beaucoup plus d'articles comme celui-ci, et je cherche plus de collaborateurs. Si vous souhaitez vraiment contribuer, laissez un commentaire.

### Commençons

![Image](https://cdn-media-1.freecodecamp.org/images/1*9tQ-BWYI2et8HFJ29-1Q9w.png)

Nous voulons faire apprendre à un robot comment jouer à un jeu Atari par lui-même, en utilisant l'apprentissage par renforcement.

Le robot dans notre cas est un réseau de neurones convolutionnel.

C'est presque de l'apprentissage profond de bout en bout, car notre robot reçoit des entrées de la même manière qu'un joueur humain — il voit directement l'image à l'écran et la récompense/le changement de points après chaque mouvement, et c'est toute l'information dont il a besoin pour prendre une décision.

Et que produit le robot ? Eh bien, idéalement, nous voulons que le robot choisisse l'action qui, selon lui, promet la plus grande récompense à l'avenir. Mais au lieu de choisir directement l'action, nous lui permettons d'assigner des « valeurs » à chacune des 18 actions possibles du joystick. Donc, pour faire simple, la valeur V pour toute action A représente l'attente du robot de la récompense future qu'il obtiendra s'il effectue cette action A.

En essence, ce réseau de neurones est une fonction de valeur. Il prend en entrée l'état de l'écran et le changement de récompense, et il produit les différentes valeurs associées à chaque action possible. Ainsi, vous pouvez choisir l'action avec la valeur la plus élevée, ou choisir toute autre action en fonction de la manière dont vous programmez le joueur global.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BT6UkJ1iSN8tmjNRQH-42g.png)

Disons que vous avez l'écran de jeu, et que vous voulez dire à un réseau de neurones ce qu'il y a à l'écran. Une façon serait de donner directement l'image au réseau de neurones ; nous ne traitons pas les entrées de quelque autre manière. L'autre serait de créer un résumé de ce qui se passe à l'écran dans un format numérique, puis de le donner au réseau de neurones. La première est appelée ici « entrées sensorielles de haute dimension » et la seconde est « représentations de caractéristiques artisanales ».

![Image](https://cdn-media-1.freecodecamp.org/images/1*jvu34f_gONIqCN09nnh1ow.png)

Lisez l'explication abstraite. Ensuite, ce paragraphe est auto-explicatif.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9lApLHIoQbsTDNdHvGdlPw.png)

Les méthodes de Deep Learning ne fonctionnent pas facilement avec l'apprentissage par renforcement comme elles le font dans l'apprentissage supervisé/non supervisé. La plupart des applications de DL ont impliqué d'énormes ensembles de données d'entraînement avec des échantillons et des étiquettes précis. Ou dans l'apprentissage non supervisé, la fonction de coût cible est encore assez pratique à utiliser.

Mais dans l'apprentissage par renforcement, il y a un piège — comme vous le savez, l'apprentissage par renforcement implique des récompenses qui pourraient être retardées de nombreuses étapes dans le futur (par exemple, il faut plusieurs mouvements pour éliminer la reine de l'adversaire aux échecs, et chacun de ces mouvements ne retourne pas la même récompense immédiate que le mouvement final, MÊME SI l'un de ces mouvements pourrait être plus important que le mouvement final).

Les récompenses pourraient également être bruyantes — par exemple, parfois les points pour un mouvement particulier sont légèrement aléatoires et non facilement prévisibles !

De plus, dans le DL, on suppose généralement que les échantillons d'entrée ne sont pas liés les uns aux autres. Par exemple, dans un réseau de reconnaissance d'images, les données d'entraînement auront un grand nombre d'images organisées de manière aléatoire et non liées. Mais en apprenant à jouer à un jeu, généralement la stratégie des mouvements ne dépend pas seulement de l'état actuel de l'écran mais aussi de certains états et mouvements précédents. Il n'est pas simple de supposer qu'il n'y a pas de corrélation.

Maintenant, attendez une seconde. Pourquoi est-il important que nos échantillons de données d'entraînement ne soient pas corrélés les uns aux autres ? Supposons que vous avez 5 échantillons d'images d'animaux, et que vous voulez apprendre à les classer en « chat » et « pas chat ». Si l'une de ces images est celle d'un chat, cela affecte-t-il la probabilité qu'une autre image soit aussi un chat ? Non. Mais dans un jeu vidéo, une image de l'écran est définitivement liée à l'image suivante. Et à l'image suivante. Et ainsi de suite. Si cela prend 10 images pour qu'un faisceau laser détruise votre vaisseau spatial, je suis assez sûr que la 9ème image est une assez bonne indication que la 10ème image va être douloureuse. Vous ne voulez pas traiter les deux images à quelques millisecondes d'intervalle comme des expériences totalement séparées lors de l'apprentissage, car elles portent évidemment des informations précieuses l'une sur l'autre. Elles font partie de la même expérience — celle d'un faisceau laser frappant votre vaisseau spatial.

Même les données d'entraînement elles-mêmes changent de nature à mesure que le robot apprend de nouvelles stratégies, ce qui rend l'entraînement plus difficile. Que signifie cela ? Par exemple, supposons que vous êtes un joueur d'échecs débutant. Vous commencez avec quelques stratégies de débutant lorsque vous jouez votre premier jeu d'échecs, c'est-à-dire continuez à avancer, tuez le pion à la première occasion, etc. Ainsi, à mesure que vous apprenez ces comportements et que vous êtes heureux de prendre des pions, ces mouvements agissent comme votre ensemble d'entraînement actuel.

Maintenant, un jour, vous essayez une stratégie différente — sacrifier l'un de vos propres fous pour sauver votre reine et prendre la tour de l'autre. Bam, vous réalisez que c'est si génial. Vous avez ajouté ce nouveau truc à votre ensemble d'entraînement, que vous n'auriez jamais appris si vous aviez continué à pratiquer votre stratégie de débutant précédente.

C'est ce que signifie avoir une distribution de données non stationnaire, ce qui ne se produit pas vraiment dans l'apprentissage supervisé/non supervisé.

Alors, étant donné ces défis, comment entraînez-vous même le réseau de neurones dans une telle situation ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*SqRBUitD7ETrDZDavseTbA.png)

Dans cet article, nous montrons comment nous avons surmonté les problèmes mentionnés ci-dessus ET nous avons directement utilisé des données vidéo/images brutes. Ce qui signifie que nous sommes géniaux.   
Un truc spécifique qui mérite d'être mentionné : « Experience Replay ». Cela résout le défi de la « corrélation des données » et des « distributions de données non stationnaires » (voir le paragraphe précédent pour comprendre ce que cela signifie).

Nous enregistrons toutes nos expériences — en utilisant à nouveau l'analogie des échecs, chaque expérience ressemble à [état actuel du plateau, mouvement que j'ai essayé, récompense que j'ai obtenue, nouvel état du plateau] — dans une mémoire. Ensuite, lors de l'entraînement, nous prélevons des lots d'expériences distribuées aléatoirement qui ne sont pas liées les unes aux autres. Dans chaque lot, différentes expériences pourraient être associées à différentes stratégies également — car toutes les expériences et stratégies précédentes sont maintenant mélangées ensemble ! Cela a du sens ?

Cela rend les échantillons de données d'entraînement plus aléatoires et non corrélés, et cela donne également l'impression d'être plus stationnaire pour le réseau de neurones car chaque nouveau lot est déjà rempli d'expériences de stratégies aléatoires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yMhzL1J1JMDzRr7aJjl_dw.png)

La plupart de cela est auto-explicatif. La clé ici est que la même architecture de réseau de neurones et les mêmes hyperparamètres (taux d'apprentissage, etc.) ont été utilisés pour chaque jeu différent. Ce n'est pas comme si nous avions utilisé un réseau plus grand pour Space Invaders et un réseau plus petit pour le ping-pong. Nous avons entraîné les réseaux à partir de zéro pour chaque nouveau jeu, mais la conception du réseau était la même. C'est assez génial, non ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*B8rW56tn65Z3r2ah_HZPKQ.png)

Les premières phrases sont auto-explicatives. En disant que « E » est stochastique, cela signifie que l'environnement n'est pas toujours prévisible (ce qui est vrai dans les jeux, non ? n'importe quoi peut arriver à n'importe quel moment).

Il répète également que le réseau de neurones ne reçoit aucune information sur l'état interne du jeu. Par exemple, nous ne lui disons pas des choses comme « il y a un monstre à cette position qui tire sur vous et se déplace dans cette direction, votre vaisseau spatial est présent ici et se déplace là, etc. ». Nous lui donnons simplement l'image et laissons le réseau convolutionnel déterminer par lui-même où se trouve le monstre, et où se trouve le joueur, et qui tire où, etc. Cela permet au robot de s'entraîner de manière plus humaine.

![Image](https://cdn-media-1.freecodecamp.org/images/1*JUTMKOB7E8zmhiqXj4A5nA.png)

Aliasing perceptuel : Cela signifie que deux états/endroits différents peuvent être perçus comme identiques. Par exemple, dans un bâtiment, il est presque impossible de déterminer un emplacement uniquement avec l'information visuelle, car tous les couloirs peuvent se ressembler.

L'aliasing perceptuel est un problème. Dans les jeux Atari, l'état du jeu ne change pas tant à chaque milliseconde, ni un être humain n'est capable de prendre des décisions à chaque milliseconde. Donc, lorsque nous prenons une entrée vidéo à 60 images par seconde, et que nous traitons chaque image comme un état séparé, alors la plupart des états dans nos données d'entraînement se ressembleront exactement ! Il est préférable de garder un horizon plus long pour ce à quoi ressemble un « état », qui a, disons, au moins 4 à 5 images (disons). Plusieurs images consécutives contiennent également des informations précieuses les unes sur les autres — par exemple, une photographie immobile de deux voitures à un pied l'une de l'autre est très ambiguë — est-ce qu'une voiture est sur le point d'entrer en collision avec l'autre ? Ou vont-elles s'éloigner l'une de l'autre après être venues si près ? Vous ne savez pas. Mais si vous prenez 4 images de la vidéo et que vous les regardez les unes après les autres, maintenant vous savez comment les voitures se déplacent et pouvez deviner si elles vont entrer en collision ou non. Nous appelons cela une séquence d'images consécutives, et utilisons une séquence comme un état.

De plus, lorsqu'un humain déplace le joystick, il reste généralement dans la même position pendant plusieurs millisecondes, ce qui est incorporé dans cet état. La même action est continuée dans chacune des images. Chaque séquence (qui inclut plusieurs images et la même action entre elles) est un état individuel, et cet état remplit toujours un processus de décision de Markov (MDP).

Si vous avez lu sur l'apprentissage par renforcement, vous savez ce que sont les MDPs et ce qu'ils signifient ! Les MDPs sont l'hypothèse centrale dans l'apprentissage par renforcement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Lae10a_oikDRMehSOlOe7g.png)

Maintenant, pour comprendre cette partie, vous devriez vraiment faire quelques études de fond sur l'apprentissage par renforcement et le Q-Learning d'abord. C'est très important. Vous devriez comprendre ce que fait l'équation de Bellman, ce que sont les récompenses futures actualisées, etc. Mais laissez-moi essayer de donner un aperçu vraiment simple du Q-learning.

Vous souvenez-vous de ce que j'ai dit à propos de la « fonction de valeur » plus tôt ? Faites défiler jusqu'à l'Abstract et lisez-le.

Maintenant, disons que vous aviez un tableau qui avait une ligne pour TOUS les états possibles (s) du jeu, et les colonnes représentaient toutes les actions possibles du joystick (a). Chaque cellule de la ligne représente la valeur totale future maximale possible si vous prenez cette action particulière et jouez au mieux à partir de ce moment-là. Cela signifie que vous avez maintenant une « feuille de triche » de ce à quoi vous attendre de n'importe quelle action à n'importe quel état ! Les valeurs de ces cellules sont appelées la valeur Q-star. (Q*(s,a)). Pour n'importe quel état s, si vous prenez l'action a, la valeur totale future maximale est Q*(s,a) comme vu dans ce tableau.

Dans la dernière ligne, pi est la « politique ». La politique est simplement la stratégie sur quelle action choisir lorsque vous êtes dans un état particulier.

![Image](https://cdn-media-1.freecodecamp.org/images/1*BMqZZKHHDmRJFXg92fTGDg.png)

Maintenant, si vous y réfléchissez, disons que vous êtes dans l'état S1. Vous voyez la valeur Q* pour toutes les actions possibles dans le tableau (expliqué dans le paragraphe 3), et vous choisissez A1 parce que sa valeur Q est la plus élevée. Vous obtenez une récompense immédiate R1, et le jeu passe à un état différent S2. Pour S2, la récompense future maximale sera si elle prend (disons) l'action A2 dans le tableau.

Maintenant, la valeur Q initiale Q*(S1,A1) est la valeur maximale que vous pourriez obtenir si vous jouiez de manière optimale à partir de ce moment-là, n'est-ce pas ? Cela signifie que Q*(S1, A1) devrait être égal à la somme de la récompense R1 ET de la valeur future maximale de l'état suivant Q*(S2,A2) ! Cela a-t-il du sens ? Mais hé, nous voulons réduire l'influence de l'état suivant, alors nous le multiplions par un nombre gamma qui est compris entre 0 et 1. Cela s'appelle l'actualisation de Q*(S2,A2).

Par conséquent, Q*(S1,A1) = R1 + [gamma x Q*(S2,A2)]

![Image](https://cdn-media-1.freecodecamp.org/images/1*cNiT8MoOSpzlXHUBJNCy4w.png)
_Je dois admettre que celui-ci ne sera pas facile à saisir juste en lisant mon explication. Prenez un peu de temps ici._

Regardez à nouveau l'équation précédente. Nous supposons que pour tout état, et pour toute action future, nous *connaissons* déjà la fonction de valeur optimale, et pouvons l'utiliser pour choisir la meilleure action à l'état actuel (parce qu'en itérant sur toutes les valeurs Q possibles, nous pouvons littéralement regarder vers l'avenir). Mais bien sûr, une telle fonction Q n'existe pas vraiment dans le monde réel ! Le mieux que nous puissions faire est d'*approximer* la fonction Q par une autre fonction, et de mettre à jour cette fonction d'approximation peu à peu en la testant dans le monde réel encore et encore. Cette fonction d'approximation peut être un simple polynôme linéaire, mais nous pouvons même utiliser des fonctions non linéaires. Nous choisissons donc d'utiliser un réseau de neurones comme notre « fonction Q approximative ».

Maintenant, vous savez pourquoi nous lisons cet article en premier lieu — DeepMind utilise un réseau de neurones pour approximer une fonction Q, puis ils laissent l'ordinateur jouer à des jeux ATARI en utilisant le réseau pour aider à prédire les meilleurs mouvements. Avec le temps, à mesure que l'ordinateur se fait une meilleure idée de comment fonctionnent les récompenses, il peut ajuster son réseau de neurones (en ajustant les poids), de sorte qu'il devienne une meilleure approximation de cette fonction Q « réelle » ! Et au moment où cette approximation est suffisamment bonne, voilà, nous réalisons qu'il peut en fait faire de meilleures prédictions que les humains.

![Image](https://cdn-media-1.freecodecamp.org/images/1*yGHZtLf1EkxeB3R3GzPLtQ.png)

Maintenant, en laissant de côté certains des charabia mathématiques ci-dessus (c'est difficile pour moi aussi !). Sachez que le Q-learning est une approche *sans modèle*. Lorsque vous dites que l'apprentissage par renforcement est « sans modèle », cela signifie que votre agent n'a pas besoin d'apprendre explicitement les règles ou la physique du jeu. Dans l'apprentissage par renforcement basé sur un modèle, ces règles et cette physique sont définies en termes de « Matrice de Transition » qui calcule l'état suivant étant donné un état actuel et une action, et une « Fonction de Récompense » qui calcule la récompense étant donné un état actuel et une action. Dans notre cas, ces deux choses sont trop complexes à calculer, et si vous y réfléchissez, nous n'en avons pas vraiment besoin ! Dans notre approche « sans modèle », nous nous soucions simplement d'apprendre la fonction de valeur Q par essai et erreur, car nous supposons qu'une bonne fonction Q devra nécessairement suivre les règles et la physique du jeu.

Notre approche est également *hors politique*, et non *sur politique*. La différence ici est plus subtile car dans cet article, ils ont suivi une sorte d'hybride. Supposons que vous êtes à l'état s et que vous avez plusieurs actions parmi lesquelles choisir. Nous avons une fonction de valeur Q approximative, donc nous calculons quelle sera la valeur Q pour chacune de ces actions. Maintenant, lors du choix de l'action, vous avez deux options. L'option « sens commun » est de simplement choisir l'action qui a la valeur Q la plus élevée, n'est-ce pas ? Oui, et c'est ce qu'on appelle une stratégie « gloutonne ». Vous choisissez toujours l'action qui vous semble la meilleure *maintenant, étant donné votre compréhension actuelle du jeu* — en d'autres termes, étant donné votre approximation actuelle de la fonction Q — ce qui signifie, étant donné votre stratégie actuelle. Mais voilà le problème — lorsque vous commencez, vous n'avez pas vraiment une bonne fonction d'approximation Q, n'est-ce pas ? Et même si vous avez une stratégie quelque peu bonne, vous voulez toujours que votre IA explore d'autres stratégies possibles et voie où elles mènent. C'est pourquoi une stratégie « gloutonne » n'est pas toujours la meilleure lorsque vous apprenez. En apprenant, vous ne voulez pas simplement continuer à essayer ce que vous croyez qui fonctionnera — vous voulez essayer d'autres choses qui semblent moins probables, juste pour acquérir de l'expérience. Et c'est la différence entre l'apprentissage sur politique (glouton) et hors politique (non glouton).

Pourquoi ai-je dit que nous utilisons une sorte d'hybride ? Parce que nous varions l'approche en fonction de ce que nous avons appris. Nous varions la probabilité avec laquelle l'agent choisira l'action gloutonne. Comment varions-nous cela ? Nous choisissons des actions gloutonnes avec une probabilité de (1-e), où e est une variable qui représente à quel point le choix est aléatoire. Donc e=1 signifie que le choix est complètement aléatoire, et e=0 signifie que nous choisissons toujours l'action gloutonne. Cela a-t-il du sens ? Au début, lorsque le réseau commence tout juste à apprendre, nous choisissons e très proche de 1, car nous voulons que l'IA explore autant de stratégies que possible. Au fil du temps et à mesure que l'IA apprend de plus en plus, nous réduisons la valeur de e vers 0 afin que l'IA reste sur une stratégie particulière.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Vqn4ETGqTAEwq0YVtIm4XA.png)

Qiang : Le jeu de backgammon est le jeu le plus populaire pour les scientifiques afin de tester leurs divers algorithmes d'intelligence artificielle et d'apprentissage automatique. La référence [24] a utilisé un algorithme sans modèle pour atteindre un niveau de jeu surhumain. Sans modèle signifie qu'il n'y a pas d'équation explicite entre l'entrée de l'algorithme (images de l'écran) et la sortie (meilleure stratégie de jeu trouvée).

Q-learning, où « Q » signifie « qualité », utilise une fonction Q qui représente la récompense future maximale actualisée lorsque nous effectuons une certaine action dans un certain état. Ensuite, la politique optimale (stratégie de jeu) est continuellement trouvée à partir de ce point. La différence dans la référence [24] est qu'ils utilisent une approximation pour la valeur q en utilisant un perceptron multicouche (MLP). Dans leur MLP, une couche cachée existe entre la couche de sortie et la couche d'entrée.

![Image](https://cdn-media-1.freecodecamp.org/images/1*C97Rt7MqfCHfnFMPegf8qw.png)

Qiang : Les applications infructueuses suivantes de méthodes similaires sur d'autres jeux ont fait que les gens ne croyaient plus à l'approche TD-gammon. Ils attribuent le succès de TD-gammon sur le backgammon à la stochasticité des lancers de dés.

![Image](https://cdn-media-1.freecodecamp.org/images/1*rSdh7CUWilXhDogwDbBFbg.png)

Remontez de quelques paragraphes, où nous avons vu quels types de fonctions peuvent être utilisés pour approximer notre fonction Q théoriquement parfaite. Apparemment, les fonctions linéaires sont mieux adaptées à la tâche que les fonctions non linéaires comme les réseaux de neurones, car elles rendent le réseau plus facile à « converger » (c'est-à-dire que les poids s'ajustent de manière à ce que le réseau soit plus précis, au lieu de devenir plus aléatoire).

![Image](https://cdn-media-1.freecodecamp.org/images/1*BUFUyDKx_mV3KVwB0YJqlg.png)

Qiang : Récemmment, combiner l'apprentissage profond avec le renforcement est redevenu un intérêt de recherche. L'environnement, la fonction de valeur et la politique ont été estimés par des algorithmes d'apprentissage profond. Dans le même temps, la divergence a été partiellement résolue par des méthodes de différence temporelle de gradient. Cependant, comme mentionné dans l'article, ces méthodes ne peuvent fonctionner qu'avec un approximateur de fonction non linéaire, pas directement avec une fonction non linéaire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZdMJCNXDs7tV0xClTvzQuQ.png)

Qiang : NFQ est le travail antérieur le plus similaire à l'approche de cet article. L'idée principale de NFQ est d'utiliser RPROP (rétropropagation résiliente) pour mettre à jour les paramètres du réseau Q afin d'optimiser la séquence de fonctions de perte dans l'équation 2. Les inconvénients de NFQ sont qu'il introduit un coût de calcul proportionnel à la taille de l'ensemble de données en raison de la mise à jour par lots.

Cet article utilise des mises à jour de gradient stochastique qui sont efficaces sur le plan computationnel. NFQ a été appliqué à des tâches simples mais pas à des entrées visuelles, l'algorithme de cet article apprend de bout en bout. Un autre article sur le Q-learning a également utilisé un état de faible dimension au lieu d'entrées visuelles brutes, ce qui est l'avantage de cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mICRjpbAYlwPurGrEihRHQ.png)

Qiang : Ce paragraphe présente plusieurs applications de l'émulateur Atari 2600. Le premier article qui a utilisé l'émulateur Atari 2600 comme plateforme d'apprentissage par renforcement a appliqué des algorithmes d'apprentissage par renforcement standard avec approximation de fonction linéaire et caractéristiques visuelles génériques. Un plus grand nombre de caractéristiques et la projection de caractéristiques dans un espace de dimension inférieure ont amélioré les résultats. Et l'architecture évolutive HyperNEAT a fait évoluer respectivement un réseau de neurones pour chaque jeu. Et le réseau de neurones représente la stratégie de jeu, qui a pu être entraîné et exploiter certains défauts de conception dans certains jeux.

Mais comme mentionné dans l'article, l'algorithme de cet article apprend la stratégie pour sept jeux Atari 2600 sans ajustement de l'architecture. C'est le grand avantage de l'algorithme de cet article.

![Image](https://cdn-media-1.freecodecamp.org/images/1*qhW9gE_B8g0BEOq8dXRvbA.png)

Auto-explicatif ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*1VRgehbSIrMO1UXsp7aDpw.png)

TD Gammon était une approche sur politique, et il utilisait directement les expériences (s1, a1, r, s2, a2) pour entraîner le réseau (sans relecture d'expérience, etc.).

![Image](https://cdn-media-1.freecodecamp.org/images/1*OEuRz0yamVqS64dTenWa4Q.png)

Nous arrivons maintenant aux améliorations spécifiques apportées à TD Gammon. La première de celles-ci est la relecture d'expérience, dont il a déjà été question précédemment. La fonction « phi » effectue le prétraitement d'images, etc., de sorte que l'état du jeu est stocké sous la forme finale prétraitée (plus d'informations à ce sujet dans la section suivante).

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gx4XeJAPhUvs-sFcJ78voQ.png)

![Image](https://cdn-media-1.freecodecamp.org/images/1*zAaWZZ8yJYSdfHu8k5wb_g.png)

Ce sont les avantages concrets de l'utilisation de la relecture d'expérience (ce paragraphe se poursuit sur la page suivante). Premièrement, tout comme dans l'apprentissage profond régulier, où chaque échantillon de données peut être réutilisé plusieurs fois pour mettre à jour les poids, nous pouvons utiliser la même expérience plusieurs fois lors de l'entraînement. Cela permet une utilisation plus efficace des données.

Deuxièmement et troisièmement sont très liés. Parce que chaque état est très étroitement lié à l'état suivant (comme c'est le cas lors de la lecture d'un jeu vidéo), l'entraînement des poids avec chaque état consécutif conduira le programme à ne suivre qu'une seule façon de jouer au jeu. Vous prédisez un mouvement basé sur la fonction Q, vous faites ce mouvement, et vous mettez à jour les poids de sorte que la prochaine fois vous bougerez à nouveau probablement à gauche. Mais en brisant ce schéma et en tirant aléatoirement des expériences passées, vous pouvez éviter ces boucles de rétroaction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*RgxQ8X-9wWAqkxYyyYstaw.png)

Maintenant, il est bon de tirer des échantillons aléatoires de la relecture d'expérience, mais parfois dans un jeu, il y a des transitions importantes que vous aimeriez que l'agent apprenne. C'est une limitation de l'approche actuelle dans cet article. Une suggestion donnée est de choisir des transitions importantes avec une probabilité plus grande lors de l'utilisation de la relecture d'expérience. Ou quelque chose comme ça.

**(Au-delà de ce point, tout est basé sur la théorie couverte dans les sections précédentes, donc beaucoup de cela est juste des détails techniques)**

![Image](https://cdn-media-1.freecodecamp.org/images/1*14-ARLnQC5pu9TR8-UY-2A.png)

La plupart de cela est auto-explicatif. L'état S est prétraité pour inclure 4 images consécutives, toutes prétraitées en niveaux de gris et redimensionnées et recadrées en carrés de 84x84. Je pense que c'est parce que, étant donné que le jeu fonctionne à plus de 24 images par seconde, et que les humains ne peuvent pas réagir si rapidement pour faire un mouvement à chaque image, il est logique de considérer 4 images consécutives comme étant dans le même état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*06IQIrsGZN1TTmZVwE65gA.png)

Lors de la création de l'architecture du réseau, vous pouvez soit en faire une fonction Q qui prend à la fois S1 et A1 et produit la valeur Q pour cette combinaison. Mais cela signifie que vous devriez exécuter ce réseau pour chacune des 18 actions possibles du joystick à chaque étape, et comparer la sortie des 18 exécutions. Au lieu de cela, vous pouvez simplement avoir une architecture où vous utilisez S1 comme entrée et avez 18 sorties, chacune correspondant à la valeur Q pour une action donnée du joystick. C'est beaucoup plus efficace de comparer les valeurs Q de cette manière !

![Image](https://cdn-media-1.freecodecamp.org/images/1*Q1p6xgnJ-vHnnq6mKx4W-Q.png)

Auto-explicatif :)

![Image](https://cdn-media-1.freecodecamp.org/images/1*4hKetidzX3ki7Q9oAiRBrA.png)

Oooh. La première moitié est auto-explicative. La seconde moitié parle d'une chose très importante à propos de cette expérience : la nature des récompenses étant entrées dans l'agent a été modifiée. Donc, *toute* récompense positive était entrée comme +1, les récompenses négatives étaient entrées comme -1, et aucun changement était entré comme 0. Cela est bien sûr très différent de la manière dont les vrais jeux fonctionnent — les récompenses changent toujours, et certains accomplissements ont des récompenses plus élevées que d'autres. Mais c'est impressionnant que, malgré cela, l'agent ait performé mieux que les humains dans certains jeux !

![Image](https://cdn-media-1.freecodecamp.org/images/1*mpk23nQcunY7rxCiwLv6tg.png)

Nous avons déjà parlé de e-greedy (dans la section 2), et de la relecture d'expérience. Cela concerne les détails spécifiques de leur mise en œuvre.

![Image](https://cdn-media-1.freecodecamp.org/images/1*EkY_9oWcLk_qN0rO4pgXLw.png)

Plus de détails sur pourquoi ils utilisent une pile de 4 images vidéo au lieu d'utiliser une seule image pour chaque état.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Ho7tdFNanegjaqg6hfrYrQ.png)

Cela concerne la métrique d'évaluation que vous utilisez lors de l'entraînement. Habituellement, en apprentissage supervisé, vous avez quelque chose comme la précision de validation, mais ici vous n'avez aucun ensemble de validation, etc., à comparer. Donc, quelles autres choses pouvons-nous utiliser pour vérifier si notre réseau s'entraîne vers un point ou si les poids dansent simplement autour ? Hmm, réfléchissons à cela. Le but de cet article est de créer un agent IA qui obtient un score élevé dans le jeu, alors pourquoi ne pas simplement utiliser le score total comme notre métrique d'évaluation ? Et nous pouvons jouer plusieurs jeux et obtenir le score global moyen. Eh bien, il s'avère que l'utilisation de cette métrique ne fonctionne pas bien en pratique, car elle s'avère très bruyante.

Réfléchissons à une autre métrique ? Eh bien, une autre chose que nous faisons dans cette expérience est de trouver une « politique » que l'IA suivra pour assurer le score le plus élevé (c'est un apprentissage hors politique, comme expliqué précédemment). Et la valeur Q à n'importe quel moment représente la récompense totale attendue par l'IA à l'avenir. Donc, si l'IA trouve une excellente politique, alors la valeur Q pour cette politique sera plus élevée, n'est-ce pas ? Voyons si nous pouvons utiliser la valeur Q elle-même comme notre métrique d'évaluation. Et voilà, elle semble être plus stable que la simple récompense totale moyenne. Maintenant, comme vous pouvez le voir, il n'y a pas d'explication théorique pour cela, et ce n'était qu'une idée qui a fonctionné. (En fait, c'est ce qui se passe tout le temps en apprentissage profond. Certaines choses fonctionnent simplement, et d'autres choses qui semblent être du bon sens ne fonctionnent pas. Un autre exemple de cela est le Dropout, qui est une technique folle mais qui fonctionne incroyablement bien).

![Image](https://cdn-media-1.freecodecamp.org/images/1*XGgbzwNENCaQ3WGfFkVwLg.png)

Cela devrait être auto-explicatif. Il montre comment la fonction de valeur change dans différents mouvements du jeu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*NdRZkv19SmwuCizTN2sAxA.png)

Ici, nous comparons les résultats de l'article avec les travaux antérieurs dans ce domaine. « Sarsa » fait référence à [s1,a1,r,s2,a2]. C'est un algorithme d'apprentissage sur politique (par opposition à notre approche hors politique). Il n'est pas facile de comprendre la différence si facilement, [en voici une bonne](https://studywolf.wordpress.com/2013/07/01/reinforcement-learning-sarsa-vs-q-learning/).

Et [une autre](https://stackoverflow.com/a/41420616).

Le reste de ce paragraphe est assez facile à lire.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oboK_by9a85Yv_MZcICqVw.png)

Pour ce paragraphe et tout ce qui suit… « Regardez et émerveillez-vous de la performance de leur approche ! »

**Oh et si vous êtes quelqu'un qui a besoin d'aide pour expliquer votre travail scientifique ou technologique à des non-techniciens pour une raison quelconque (que ce soit pour le marketing ou l'éducation), je pourrais vraiment vous aider. Envoyez-moi un message sur Twitter : @mngrwl**