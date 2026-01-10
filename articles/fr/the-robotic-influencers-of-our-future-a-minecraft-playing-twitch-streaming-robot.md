---
title: 'Les influenceurs robotiques de notre avenir : Expérimentation avec un robot
  jouant à Minecraft et diffusant sur Twitch'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T21:26:15.000Z'
originalURL: https://freecodecamp.org/news/the-robotic-influencers-of-our-future-a-minecraft-playing-twitch-streaming-robot
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/twitchrobot.png
tags:
- name: gaming
  slug: gaming
- name: minecraft
  slug: minecraft
- name: robotics
  slug: robotics
- name: streaming
  slug: streaming
- name: Twitch
  slug: twitch
seo_title: 'Les influenceurs robotiques de notre avenir : Expérimentation avec un
  robot jouant à Minecraft et diffusant sur Twitch'
seo_desc: 'By Minja Axelsson

  In this article, I''ll discuss how we reached young audiences by combining robotics
  with e-sports.

  What on Earth?

  Ever heard of anything like it before? Me neither. The robot was created as part
  of Futurice’s project with Yle, the na...'
---

Par Minja Axelsson

Dans cet article, je vais discuter de la manière dont nous avons atteint les jeunes publics en combinant la robotique avec les e-sports.

## Qu'est-ce que c'est ?

Vous en avez déjà entendu parler ? Moi non plus. Le robot a été créé dans le cadre du projet de [Futurice](https://www.futurice.com/) avec [Yle](https://yle.fi/), la société nationale de diffusion de la Finlande.

Yle produit du contenu pour la télévision, la radio et le web. Il atteint un large public d'auditeurs plus âgés, mais a eu du mal à atteindre les plus jeunes. L'objectif de ce projet était d'utiliser une nouvelle technologie pour atteindre les jeunes publics, spécifiquement les adolescents.

Le contenu de Yle a traditionnellement été non participatif : les artistes se produisent, et le public regarde. Cependant, les jeunes publics regardent généralement du contenu plus participatif, comme les vidéos YouTube ou les streams.

Nous voulions créer du contenu participatif, où l'artiste interagit avec son public. Les journalistes de Yle, spécialisés dans les audiences adolescentes, ont souligné que les jeux et les e-sports sont des contenus populaires. Nous avons réalisé que le gaming était le contexte parfait pour cela : le public pourrait jouer avec l'artiste. Nous voulions explorer à quoi pourrait ressembler un divertisseur, ou même un influenceur du futur. Alors pourquoi ne pas créer un robot streamer gamer ?

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_QW08nV9GgKS589PJ.png)
_Les journalistes de Yle et les roboticistes de Futurice développant l'idée d'un robot gamer_

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_XdFOgvs4DhZVaHnW.png)
_Premières ébauches_

## À quoi ressemblait ce robot ?

Nous avons choisi deux jeux pour le robot : Flappy Bird et Minecraft.

Flappy Bird était un jeu culte qui a connu une brève période de popularité extrême en 2014. Nous avons choisi Flappy Bird parce que les mécanismes du jeu sont simples et permettent de jouer avec l'apprentissage automatique. Nous voulions essayer un [algorithme de neuroévolution](https://xviniette.github.io/FlappyLearning/), qui fait évoluer de nouveaux oiseaux dans le jeu en fonction de ceux qui ont le mieux performé dans la génération précédente. Ainsi, nous pourrions voir comment le public réagissait lorsqu'un ordinateur jouait au jeu.

Nous avons choisi Minecraft pour ses fonctionnalités communautaires, qui permettent l'interaction entre les joueurs. Les joueurs peuvent coopérer ou se battre, échanger entre eux et discuter. Ils peuvent se "griefer" mutuellement, c'est-à-dire être une nuisance. Les joueurs peuvent également miner des matériaux et les transformer en objets, voire construire des villes. Ils peuvent stocker des choses précieuses, cultiver la terre, élever des animaux et combattre des monstres.

Minecraft possède également un matériau appelé redstone, que les joueurs peuvent utiliser pour construire des circuits logiques. En effet, les joueurs peuvent construire un ordinateur entier à l'intérieur de Minecraft. Poétique, n'est-ce pas ?

Pour jouer à Minecraft, nous avons décidé qu'un humain devrait contrôler le robot. Le jeu est compliqué, et avoir des interactions authentiques avec d'autres joueurs nécessiterait un humain à l'autre bout.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_zNxCX_zKJ3ikRM-y.png)
_Flappy Bird et le robot_

Notre équipe de journalistes de Yle et de roboticistes de Futurice a défini quelques avantages clairs à l'utilisation d'un robot dans ce contexte :

* Un robot est infatigable, il peut jouer indéfiniment et fournir du contenu 24h/24 et 7j/7. C'est un streamer idéal.
* Un robot peut être neutre en termes de genre. Les gamers et les audiences de gaming sont typiquement masculines, mais un robot neutre pourrait potentiellement attirer des audiences plus diverses.
* Un robot peut refléter le comportement des gamers, suscitant des émotions. La culture du gaming est souvent agressive. Le robot pourrait être agressif à son tour, faisant réfléchir les gamers sur leur propre comportement.
* Un robot peut interagir dans le jeu et discuter simultanément. Les humains sont limités à une seule sortie, un robot peut en avoir plusieurs.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_-eTZqndK5kdFckQ5-lXpMg.jpeg)
_Test de notre équipement de streaming et problèmes d'interférence avec l'écran facial du robot._

Nous avons décidé d'une session de gaming de six heures, alternant entre Minecraft et Flappy Bird. Pour définir l'expérience utilisateur de la session, nous avons établi des directives pour la conception de notre robot :

* Expérience utilisateur expérimentale : l'utilisateur devrait pouvoir explorer dans l'interaction avec le robot.
* Les streamers sont généralement des personnages forts. Le robot est un personnage avec une forte personnalité.
* Le robot peut provoquer des réactions "WTF ?" chez les joueurs. Nous voulions que l'expérience soit mémorable, plutôt que fade.
* La culture et l'espace du gaming en ligne sont uniques et doivent être conçus pour cela.

Sur la base de ces directives, nous avons créé le personnage IQ_201. IQ_201 est basé sur des gamers en ligne agressifs qui sont convaincus de leur propre intelligence supérieure (voir [ce meme sur avoir un QI supérieur à 200](https://knowyourmeme.com/memes/200-iq)). Le robot serait grossier et réactif, destiné à provoquer une réaction chez les adolescents interagissant avec lui.

Avant la mise en œuvre, l'équipe voulait également prendre en compte certaines considérations éthiques :

* La transparence sur la manière dont le robot est opéré est nécessaire. Si ce robot devait être mis en production, les utilisateurs devraient pouvoir trouver des informations sur son fonctionnement.
* Le robot devrait traiter tous les joueurs de la même manière. Cela faisait également partie de la décision de rendre le robot neutre en termes de genre. Et en raison de la culture parfois enragée, haineuse, voire raciste ou sexiste du gaming, nous devions concevoir soigneusement la personnalité du robot. Il pouvait être excentrique, voire grossier, mais jamais haineux. Nous ne voulions aucun moment de gaming tendu.
* Le robot devrait être grossier, mais pas trop exagéré.
* Le chat devait être modéré. Comme mentionné, la culture du gaming peut être toxique. Nous voulions surveiller attentivement les chats de Minecraft et Twitch pour nous assurer qu'aucun méfait ne se produise.

Pour répondre à toutes ces exigences, nous avons sélectionné le [robot Furhat](https://www.furhatrobotics.com/). Le robot Furhat disposait d'une interface de téléopération relativement facile à utiliser, qui permettait à l'utilisateur de saisir du texte à convertir en parole du robot, ainsi que d'effectuer des gestes d'un simple clic sur un bouton.

## Fleurs et Violence

Nous avions un stream de 6 heures, commençant à 14h et se terminant à 20h. Nous avons alterné entre les jeux : 14h-15h était Flappy Bird, 15h-17h Minecraft, 17h-18h Flappy Bird, puis 18h-20h Minecraft à nouveau. Cet horaire permettait aux opérateurs du robot jouant à Minecraft de faire une pause bien nécessaire au milieu.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/twitchrobot-1.png)
_Notre robot_

Au début, quelques personnes ont rejoint. Graduellement, nous avons gagné de plus en plus de monde. Nous avons atteint notre pic à 16h20 avec 49 spectateurs simultanés sur Twitch. Au total, nous avons eu 431 spectateurs uniques. Dans Minecraft, il y avait environ 30 joueurs actifs. Considérant à quel point notre publicité était minimale (un post sur un forum et quelques tweets), nous avons été agréablement surpris par l'affluence.

Les sessions Minecraft étaient dirigées par deux opérateurs de robot (moi-même et une autre Minja). L'autre Minja jouait à Minecraft, et je contrôlais la voix et les gestes du robot. Une troisième personne répondait aux messages sur le chat.

%[https://www.youtube.com/watch?v=8kKPoYx7rMs]

Minecraft était écrasant. Le caractère provocateur du robot a provoqué les adolescents à le tuer à plusieurs reprises. Après s'être réfugié dans les montagnes avec les lamas à plusieurs reprises et avoir été tué encore une fois, nous avons modifié le comportement du robot pour le rendre plus amical. Nous voulions créer des interactions plus constructives.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_pMMw-X8ZYwIOH_cU.png)
_Deux Minjas en tant qu'opérateurs de robot_

Vers la fin du deuxième stream Minecraft, les adolescents coopéraient avec le robot. Ils le protégeaient des quelques joueurs agressifs qui restaient et lui offraient des cadeaux comme des fleurs. Certains l'ont même complimenté directement pour le rendre heureux. Les joueurs ont commencé à suivre le robot, acceptant de coopérer lorsqu'il a initié la construction d'un phare. Ils ont également construit une maison et capturé et nommé un lama : IQ_201 Junior.

Il y avait deux factions claires dans le jeu : certains étaient déterminés à tuer le robot tout au long du jeu, et d'autres le protégeaient tout au long. Certains se sont sentis plus à l'aise avec le robot au fur et à mesure du stream, changeant de camp. Dans tous les cas, le robot a suscité de fortes émotions. Les adolescents ont cherché une interaction authentique avec lui. Personne n'a ignoré le robot, ou s'est ennuyé.

Des discussions sur le fonctionnement du robot ont eu lieu tout au long du stream. Personne n'a demandé au robot lui-même, peut-être par respect ou par crainte de l'énerver. Les discussions se sont concentrées sur le fait de savoir si le robot était "réel", c'est-à-dire s'il était vraiment automatique, ou si un humain le contrôlait. Tapait-il avec de vraies mains physiques ? Ou avait-il "piraté" le jeu et jouait-il via du code ?

## "Je vais te manquer, robot !"

16 personnes ont répondu à notre enquête par la suite. 80 % des joueurs avaient moins de 18 ans, la plupart avaient entre 13 et 15 ans. 80 % des joueurs ont interagi avec le robot. C'était extrêmement positif, nous avons réussi à créer un robot qui était captivant pour les utilisateurs. 75 % des joueurs ont noté le robot 3 ou plus, sur 5.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_7k1TlGnl986zyBKQ.png)
_Spectateurs au fil du temps_

Nous avons recueilli des commentaires des joueurs à partir de l'enquête, ainsi que du chat du jeu Minecraft. Ils sont traduits du finnois et reflètent certaines des pensées de nos joueurs sur le robot.

#### D'abord les critiques :

**"C'était assez amusant et cool. Mais ça semblait un peu monté." [Faisant référence au robot ayant éventuellement un opérateur humain]**

Beaucoup de joueurs se demandaient comment le robot fonctionnait réellement. Ce commentaire nous ramène à la considération éthique dont nous avons parlé plus tôt : la transparence sur le fonctionnement du robot.

Bien que nous avions l'intention d'être transparents au début, nous avons décidé de ne pas informer les utilisateurs de la nature téléopérée du robot pour ce premier pilote. Nous avons fait ce choix parce que nous voulions maintenir la "suspension d'incrédulité" de l'utilisateur active, ce qui signifie que nous voulions que les participants jouent le jeu en croyant qu'ils parlaient à un "vrai robot" (un robot autonome) (Duffy & Zawieska, 2012).

La réponse négative que nous avons reçue concernant le manque de clarté sur le fonctionnement du robot nous a clairement indiqué que si ce pilote était étendu, il est hautement important d'être plus transparent. Il est possible de maintenir la suspension d'incrédulité et d'être honnête sur le fonctionnement du robot simultanément (nous savons tous que les émissions de télévision ne sont pas la réalité, après tout).

**"Le robot était un peu simple dans certaines choses, et parfois parlait méchamment aux gens, et était condescendant. C'était un peu anxiogène... Était-ce intentionnel ?"**

Certains joueurs ont estimé que le comportement grossier du robot franchissait la limite de la condescendance. Ils souhaitaient que le robot soit plus attentionné à l'avenir. Cela indique que même un robot peut blesser des sentiments. Dans les versions futures, rendre IQ_201 plus empathique et moins axé sur la supériorité des robots sur les humains pourrait avoir des résultats positifs.

**"Le robot avait un peu le visage bleu, et sa voix était un peu bizarre."**

Deux adolescents n'ont pas apprécié l'apparence et la voix du robot. L'un a particulièrement remarqué son visage bleu, demandant pourquoi nous ne l'avions pas rendu "de couleur normale".

Cela pourrait être dû au fait que le robot tombait dans la "vallée de l'étrange" pour ces joueurs. La vallée de l'étrange est une théorie développée par le chercheur en robotique Masahiro Mori (Mori et al., 2012). Sa théorie postule que lorsque l'apparence d'un robot approche celle d'un humain, il y a un creux lorsque l'apparence devient très proche. Les zombies et les cadavres tombent dans cette vallée.

Pour éliminer cet effet avec notre robot, il pourrait être judicieux de modifier l'apparence et la voix du robot dans les solutions futures.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_g5B15D6hFSmG0bbi.png)
_La Vallée de l'Étrange par Masahiro Mori. Wikimedia commons._

#### Et ensuite les positifs :

**"C'était vraiment intéressant de jouer avec le robot. :) J'espère qu'à l'avenir nous pourrons avoir ce type d'événement à nouveau. :)"**

La majorité des adolescents ont apprécié jouer avec le robot et regarder le stream. Leurs retours ont complimenté le sens de l'humour du robot et ses compétences de jeu. Une continuation du pilote trouverait sûrement un public intéressé.

**[au robot] "Certaines personnes ont du mal avec les nouvelles choses. Dans ce cas, ces joueurs ont du mal avec un robot, puisque tu es nouveau."**

Ce joueur a consolé le robot dans le jeu, alors que d'autres joueurs lui donnaient du fil à retordre en le tuant continuellement. Ce commentaire était touchant : le joueur se sentait mal pour le robot et pensait que le robot pouvait se sentir mal aussi, essayant de changer cela. C'est une réponse empathique claire envers le robot.

**[au robot] "Tu vas me manquer, robot !"**

Quelques joueurs ont dit au revoir au robot avec émotion lorsqu'il a quitté Minecraft. Ces joueurs ont trouvé le robot abordable et ont même formé un lien émotionnel avec lui. Cela signifie que nous avons réussi à créer un personnage captivant, même lors d'un stream de seulement 6 heures.

Pour les futures versions du robot, les joueurs devraient être informés de son fonctionnement. Cela pourrait les aider à calibrer un niveau approprié de lien émotionnel avec le robot.

## Les influenceurs robotiques sont-ils notre avenir ?

Les joueurs ont manifesté un intérêt actif pour le robot. Ils l'ont approché, interagi avec lui et formé des opinions à son sujet. Le robot a également provoqué des réactions émotionnelles, positives et négatives. Certains participants ont vraiment aimé le robot et souhaité plus d'interactions à l'avenir, tandis que d'autres étaient très critiques.

Cela indique que les influenceurs robotiques ont la capacité d'affecter nos émotions. Si cette capacité atteindra un jour le niveau des divertisseurs humains, je ne sais pas. Si cela est souhaitable, je ne sais pas non plus.

Ce qui m'a positivement surpris, c'est que la jeune base d'utilisateurs du robot était alphabétisée en matière de médias : ils ont examiné de manière critique le mode de fonctionnement du robot. Les joueurs avaient une bonne idée de ce qui est possible avec l'IA aujourd'hui, et de ce qui ne l'est pas. Ils n'étaient pas facilement dupés.

Cela me donne de l'espoir pour notre avenir, qu'il contienne ou non des divertisseurs robotiques. Lorsque les spectateurs restent critiques, ils peuvent comprendre que les robots sont des machines sans réelle capacité émotionnelle, même si les spectateurs choisissent de suspendre leur incrédulité.

Interagir avec le robot peut être considéré comme une forme d'[interaction parasociale](https://fr.wikipedia.org/wiki/Interaction_parasociale) pour le spectateur, où le spectateur peut sentir que sa relation avec le robot est proche, même si elle n'est pas vraiment réciproque. Cela n'est pas nécessairement nuisible, tant que nous sommes honnêtes sur ce qu'est vraiment la relation. Nous devrions comprendre que les robots jouent un rôle pour susciter des émotions en nous, comme le font les divertisseurs humains.

[**Une vidéo sur le projet.**](https://areena.yle.fi/1-50168989?source=post_page-----702735f678a8----------------------)

Publié pour la première fois sur [Towards Data Science.](https://towardsdatascience.com/the-robotic-influencers-of-our-future-a-minecraft-playing-twitch-streaming-robot-702735f678a8)

---

_Duffy, B. R., & Zawieska, K. (2012, septembre). Suspension of disbelief in social robotics. Dans 2012 IEEE RO-MAN : The 21st IEEE International Symposium on Robot and Human Interactive Communication (pp. 484–489). IEEE._

_Mori, M., MacDorman, K. F., & Kageki, N. (2012). The uncanny valley: The original essay by Masahiro Mori. IEEE Spectrum, 98–100._