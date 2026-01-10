---
title: 4 Approches du Traitement et de la Compréhension du Langage Naturel
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-03-21T17:23:33.000Z'
originalURL: https://freecodecamp.org/news/how-natural-language-processing-powers-chatbots-4-common-approaches-a077a4de04d4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DwKde6rZ8qMjtvJmmEzUjw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: '#chatbots'
  slug: chatbots
- name: Machine Learning
  slug: machine-learning
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: 4 Approches du Traitement et de la Compréhension du Langage Naturel
seo_desc: 'By Mariya Yao

  In 1971, Terry Winograd wrote the SHRDLU program while completing his PhD at MIT.

  SHRDLU features a world of toy blocks where the computer translates human commands
  into physical actions, such as “move the red pyramid next to the blue c...'
---

Par Mariya Yao

En 1971, Terry Winograd a écrit le programme [SHRDLU](http://hci.stanford.edu/winograd/shrdlu/) tout en complétant son doctorat au MIT.

SHRDLU présente un monde de blocs jouets où l'ordinateur traduit les commandes humaines en actions physiques, comme « déplace la pyramide rouge à côté du cube bleu ».

Pour réussir de telles tâches, l'ordinateur doit construire des connaissances sémantiques de manière itérative, un processus que Winograd a découvert comme fragile et limité.

![Image](https://cdn-media-1.freecodecamp.org/images/1*wlupOMZ-wUJj_4GWak53YQ.png)

L'essor des chatbots et des technologies activées par la voix a renouvelé l'enthousiasme pour les techniques de traitement du langage naturel (NLP) et de compréhension du langage naturel (NLU) qui peuvent produire des dialogues homme-machine satisfaisants.

Malheureusement, les percées académiques ne se sont pas encore traduites par une meilleure expérience utilisateur. Le journaliste de Gizmodo, Darren Orf, a déclaré les chatbots de Messenger « [frustrants et inutiles](http://gizmodo.com/facebook-messenger-chatbots-are-more-frustrating-than-h-1770732045) » et Facebook a admis un [taux d'échec de 70 %](https://www.theregister.co.uk/2017/02/22/facebook_ai_fail/) pour leur assistant conversationnel très attendu, « M ».

Néanmoins, les chercheurs avancent avec de nouveaux plans d'attaque, revisitant parfois les mêmes tactiques et principes que Winograd a essayés dans les années 70.

OpenAI a récemment utilisé l'apprentissage par renforcement pour [apprendre à des agents à concevoir leur propre langage](https://openai.com/blog/learning-to-communicate/) en « les plaçant dans un ensemble de mondes simples, en leur donnant la capacité de communiquer, puis en leur donnant des objectifs qui peuvent être mieux atteints en communiquant avec d'autres agents ». Les agents ont indépendamment développé un langage simple « ancré ».

Le MIT Media Lab [présente](https://www.media.mit.edu/projects/grounded-language-learning-and-understanding/overview/) cette clarification satisfaisante sur ce que signifie « ancré » dans le contexte du langage :

> _« Le langage est ancré dans l'expérience. Contrairement aux dictionnaires qui définissent les mots en termes d'autres mots, les humains comprennent de nombreux mots de base en termes d'associations avec des expériences sensori-motrices. Les gens doivent interagir physiquement avec leur monde pour saisir l'essence des mots comme « rouge », « lourd » et « au-dessus ». Les mots abstraits ne sont acquis qu'en relation avec des termes plus concrètement ancrés. L'ancrage est ainsi un aspect fondamental du langage parlé, qui permet aux humains d'acquérir et d'utiliser des mots et des phrases en contexte. »_

L'antithèse du langage ancré est le langage inféré. Le langage inféré tire sa signification des mots eux-mêmes plutôt que de ce qu'ils représentent.

Lorsqu'ils sont formés uniquement sur de grands corpus de texte — mais pas sur des représentations du monde réel — les méthodes statistiques pour le NLP et le NLU manquent de véritable compréhension de la signification des mots.

OpenAI souligne que de telles approches partagent les faiblesses révélées par la célèbre expérience de pensée de la [Chambre chinoise](https://plato.stanford.edu/entries/chinese-room/) de John Searle. Équipé d'un dictionnaire universel pour mapper toutes les phrases d'entrée chinoises possibles à des phrases de sortie chinoises, n'importe qui peut effectuer une recherche brute et produire des réponses conversationnellement acceptables sans comprendre ce qu'ils disent réellement.

### Pourquoi le Langage est-il si Complexe ?

Percy Liang, professeur en informatique à Stanford et expert en NLP, [décompose les diverses approches du NLP / NLU](https://www.youtube.com/watch?v=mhHfnhh-pB4) en quatre catégories distinctes :

1. Distributionnelle
2. Basée sur les cadres
3. Théorique des modèles
4. Apprentissage interactif

Tout d'abord, une brève leçon de linguistique avant de continuer à définir et décrire ces catégories.

Il existe trois niveaux d'analyse linguistique :

1. Syntaxe — qu'est-ce qui est grammaticalement correct ?
2. Sémantique — quel est le sens ?
3. Pragmatique — quel est le but ou l'objectif ?

En utilisant une analogie de programmation, Liang compare une syntaxe réussie à « aucune erreur de compilation », la sémantique à « aucun bug d'implémentation » et la pragmatique à « avoir implémenté le bon algorithme ».

Il [souligne](https://simons.berkeley.edu/sites/default/files/docs/5950/2017.02.01-21.15.12-simons-nlp-tutorial.pdf) que les phrases peuvent avoir la même sémantique, mais une syntaxe différente, comme « 3+2 » versus « 2+3 ». De même, elles peuvent avoir une syntaxe identique mais une sémantique différente, par exemple, 3/2 est interprété différemment en Python 2.7 vs Python 3.

En fin de compte, la pragmatique est clé, puisque le langage est créé par le besoin de motiver une action dans le monde. Si vous implémentez un réseau de neurones complexe pour modéliser un simple lancer de pièce, vous avez une excellente sémantique mais une mauvaise pragmatique puisque il existe une pléthore d'approches plus faciles et plus efficaces pour résoudre le même problème.

De nombreux autres termes linguistiques existent qui démontrent la complexité du langage. Les mots prennent des significations différentes lorsqu'ils sont combinés avec d'autres mots, comme « light » versus « light bulb » (c'est-à-dire, expressions multi-mots), ou utilisés dans diverses phrases comme « I stepped into the light » et « the suitcase was light » (polysémie).

L'hyponymie montre comment une instance spécifique est liée à un terme général (un chat est un mammifère) et la méronymie indique qu'un terme fait partie d'un autre (un chat a une queue). De telles relations doivent être comprises pour effectuer la tâche d'implication textuelle, reconnaissant lorsqu'une phrase est logiquement impliquée dans une autre. « Vous lisez cet article » implique la phrase « vous pouvez lire ».

Outre les relations lexicales complexes, vos phrases impliquent également des croyances, des implicatures conversationnelles et des présuppositions. Liang fournit d'excellents exemples de chacun. Superman et Clark Kent sont la même personne, mais Lois Lane croit que Superman est un héros tandis que Clark Kent ne l'est pas.

Si vous dites « Où est le rôti de bœuf ? » et que votre partenaire de conversation répond « Eh bien, le chien a l'air heureux », l'implicature conversationnelle est que le chien a mangé le rôti de bœuf.

Les présuppositions sont des hypothèses de fond qui sont vraies indépendamment de la valeur de vérité d'une phrase. « J'ai arrêté de manger de la viande » a la présupposition « J'ai déjà mangé de la viande » même si vous inversez la phrase en « Je n'ai pas arrêté de manger de la viande ».

S'ajoutant à la complexité, il y a le flou, l'ambiguïté et l'incertitude. L'incertitude est lorsque vous voyez un mot que vous ne connaissez pas et devez deviner le sens.

Si vous traquez un crush sur Facebook et que leur statut de relation dit « C'est compliqué », vous comprenez déjà le flou. Richard Socher, Scientifique en Chef chez Salesforce, a donné un excellent exemple d'ambiguïté lors d'une récente conférence sur l'IA : « La question 'puis-je vous couper ?' signifie des choses très différentes si je suis à côté de vous dans une file d'attente ou si je tiens un couteau. »

Maintenant que vous êtes plus éclairé sur les nombreux défis du langage, revenons aux quatre catégories de Liang des approches de l'analyse sémantique en NLP et NLU.

### #1 : Approches Distributionnelles

Les approches distributionnelles incluent les tactiques statistiques à grande échelle de l'apprentissage automatique et de l'apprentissage profond. Ces méthodes transforment généralement le contenu en vecteurs de mots pour l'analyse mathématique et performant assez bien pour des tâches telles que l'étiquetage des parties du discours (est-ce un nom ou un verbe ?), l'analyse des dépendances (cette partie d'une phrase modifie-t-elle une autre partie ?) et la parenté sémantique (ces différents mots sont-ils utilisés de manière similaire ?). Ces tâches de NLP ne reposent pas sur la compréhension du sens des mots, mais plutôt sur la relation entre les mots eux-mêmes.

De tels systèmes sont larges, flexibles et scalables. Ils peuvent être appliqués largement à différents types de texte sans avoir besoin de caractéristiques conçues à la main ou de connaissances de domaine encodées par des experts. L'inconvénient est qu'ils manquent de véritable compréhension de la sémantique et de la pragmatique du monde réel. Comparer des mots à d'autres mots, ou des mots à des phrases, ou des phrases à des phrases peut tous donner des résultats différents.

La similarité sémantique, par exemple, ne signifie pas synonymie. Un calcul de voisin le plus proche peut même considérer des antonymes comme liés :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Np3j6yCOzrYsuk4HBptluQ.png)

Les modèles avancés de réseaux de neurones modernes, tels que les [réseaux de mémoire attentionnels de bout en bout](https://arxiv.org/abs/1503.08895) pionniers de Facebook ou le [modèle multi-tâches conjoint](https://arxiv.org/abs/1611.01587) inventé par Salesforce, peuvent gérer des tâches simples de questions et réponses, mais sont encore en phase pilote pour les cas d'utilisation grand public et entreprise.

Jusqu'à présent, Facebook n'a montré publiquement qu'un [réseau de neurones](http://newsroom.fb.com/news/2015/03/f8-day-two-2015/) formé sur une version absurdement simplifiée du Seigneur des Anneaux peut déterminer où se trouve l'anneau unique insaisissable.

![Image](https://cdn-media-1.freecodecamp.org/images/1*W-PLNibnZcX_DVAApA6TAA.jpeg)

Bien que les méthodes distributionnelles atteignent une large couverture, elles ne peuvent pas gérer la profondeur. Les questions complexes et nuancées qui reposent sur la sophistication linguistique et les connaissances contextuelles du monde n'ont pas encore été répondus de manière satisfaisante.

### #2 : Approche Basée sur les Cadres

« Un cadre est une structure de données pour représenter une situation stéréotypée », explique Marvin Minsky dans son [article séminal de 1974](http://web.media.mit.edu/~minsky/papers/Frames/frames.html) intitulé « A Framework For Representing Knowledge ». Pensez aux cadres comme une représentation canonique pour laquelle des spécificités peuvent être échangées.

Liang fournit l'exemple d'une transaction commerciale comme cadre. Dans de telles situations, vous avez généralement un vendeur, un acheteur, des biens échangés et un prix d'échange.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZNOHTsow0HvJ5rHIYkG7Kw.png)

Les phrases qui sont syntaxiquement différentes mais sémantiquement identiques — comme « Cynthia a vendu le vélo à Bob pour 200 $ » et « Bob a acheté le vélo pour 200 $ de Cynthia » — peuvent être adaptées au même cadre. L'analyse consiste alors à identifier d'abord le cadre utilisé, puis à remplir les paramètres spécifiques du cadre — c'est-à-dire Cynthia, 200 $.

L'inconvénient évident des cadres est qu'ils nécessitent une supervision. Dans certains domaines, un expert doit les créer, ce qui limite la portée des approches basées sur les cadres. Les cadres sont également nécessairement incomplets. Les phrases telles que « Cynthia a visité le magasin de vélos hier » et « Cynthia a acheté le vélo le moins cher » ne peuvent pas être analysées de manière adéquate avec le cadre que nous avons défini ci-dessus.

### #3 : Approche Théorique des Modèles

La troisième catégorie d'analyse sémantique relève de l'approche théorique des modèles. Pour comprendre cette approche, nous introduirons deux concepts linguistiques importants : la « théorie des modèles » et la « compositionnalité ».

La théorie des modèles fait référence à l'idée que les phrases se réfèrent au monde, comme dans le cas du langage ancré (c'est-à-dire le bloc est bleu). Dans la compositionnalité, les significations des parties d'une phrase peuvent être combinées pour déduire la signification globale.

Liang compare cette approche à la transformation du langage en programmes informatiques. Pour déterminer la réponse à la requête « quelle est la plus grande ville d'Europe par population », vous devez d'abord identifier les concepts de « ville » et « Europe » et réduire votre espace de recherche aux villes contenues en Europe. Ensuite, vous devrez trier les nombres de population pour chaque ville que vous avez présélectionnée jusqu'à présent et retourner le maximum de cette valeur.

![Image](https://cdn-media-1.freecodecamp.org/images/1*py-XBjZHKyilrrRHO70q8w.png)

Pour exécuter la phrase « Rappelle-moi d'acheter du lait après ma dernière réunion lundi » nécessite une décomposition et une recombinaison similaires.

![Image](https://cdn-media-1.freecodecamp.org/images/1*y0KBbhJha-bi0LxE2-hJcw.png)

Les modèles varient du besoin d'une supervision lourde de la part d'experts à une supervision légère de la part de humains moyens sur Mechanical Turk. Les avantages des méthodes basées sur les modèles incluent la représentation du monde entier, une sémantique riche et un traitement de bout en bout, ce qui permet à de telles approches de répondre à des requêtes de recherche difficiles et nuancées.

Le principal inconvénient est que les applications sont fortement limitées en portée en raison du besoin de caractéristiques conçues à la main. Les applications des approches théoriques des modèles à la NLU commencent généralement par les cas d'utilisation les plus faciles et les plus contenus et avancent à partir de là.

Le Saint Graal de la NLU est à la fois la largeur et la profondeur, mais en pratique, vous devez faire un compromis entre les deux. Les méthodes distributionnelles ont de l'échelle et de la largeur, mais une compréhension superficielle. Les méthodes théoriques des modèles sont intensives en main-d'œuvre et étroites en portée. Les méthodes basées sur les cadres se situent entre les deux.

### #4 : Approches d'Apprentissage Interactif

Paul Grice, un philosophe britannique du langage, a décrit le langage comme un jeu coopératif entre le locuteur et l'auditeur. Liang est enclin à être d'accord. Il croit qu'une approche viable pour aborder à la fois la largeur et la profondeur dans l'apprentissage du langage est d'employer des environnements interactifs où les humains enseignent progressivement aux ordinateurs. Dans de telles approches, les besoins pragmatiques du langage informent le développement.

Pour tester cette théorie, Liang a développé [SHRDLRN](http://shrdlurn.sidaw.xyz/acl16) comme une version moderne du SHRDLU de Winograd. Dans ce jeu de langage interactif, un humain doit instruire un ordinateur de déplacer des blocs d'une orientation de départ à une orientation de fin. Le défi est que l'ordinateur commence sans concept de langage. Étape par étape, l'humain dit une phrase puis indique visuellement à l'ordinateur à quoi devrait ressembler le résultat de l'exécution.

![Image](https://cdn-media-1.freecodecamp.org/images/1*-WnP6w_TMdgT0tzgWlG5JQ.png)

Si un humain joue bien, il ou elle adopte un langage cohérent qui permet à l'ordinateur de construire rapidement un modèle de l'environnement de jeu et de mapper les mots aux couleurs ou aux positions. Le résultat surprenant est que n'importe quel langage fera l'affaire, même une notation abrégée inventée individuellement, tant que vous êtes cohérent.

![Image](https://cdn-media-1.freecodecamp.org/images/1*E2QiQdJsZDXl1aspB_AKSQ.png)

Les pires joueurs qui mettent le plus de temps à former l'ordinateur emploient souvent une terminologie incohérente ou des étapes illogiques.

![Image](https://cdn-media-1.freecodecamp.org/images/1*uYNWERS5qcdjIh35WP03QA.png)

Le pari de Liang est que de telles approches permettraient aux ordinateurs de résoudre les problèmes de NLP et de NLU de bout en bout sans modèles explicites. « Le langage est intrinsèquement interactif », ajoute-t-il. « Comment représentons-nous les connaissances, le contexte, la mémoire ? Peut-être ne devrions-nous pas nous concentrer sur la création de meilleurs modèles, mais plutôt sur de meilleurs environnements pour l'apprentissage interactif. »

Le langage est à la fois logique et émotionnel. Nous utilisons des mots pour décrire à la fois les mathématiques et la poésie. Accommoder la large gamme de nos expressions dans les applications de NLP et de NLU peut impliquer de combiner les approches décrites ci-dessus, allant des méthodes distributionnelles / axées sur la largeur aux systèmes basés sur les modèles aux environnements d'apprentissage interactif.

Nous devons peut-être aussi repenser entièrement nos approches, en utilisant un apprentissage coopératif basé sur l'interaction humain-ordinateur plutôt que des modèles pilotés par des chercheurs.

Si vous avez une heure et demie de libre, je vous recommande vivement de regarder l'intégralité de la conférence de Percy Liang sur laquelle cet article de synthèse était basé :

_Un remerciement spécial à [Melissa Fabros](https://www.linkedin.com/in/melissa-fabros-5a1b35b/) pour avoir recommandé la conférence de Percy, [Matthew Kleinsmith](https://www.linkedin.com/in/matthewkleinsmith/) pour avoir mis en avant la définition du MIT Media Lab du langage « ancré », et Jeremy Howard et Rachel Thomas de [fast.ai](http://www.fast.ai/) pour avoir facilité notre connexion et notre conversation._

**Si vous avez aimé mon article, rejoignez la communauté [TOPBOTS](http://www.topbots.com/bot-news-pro-newsletter/?utm_medium=article&utm_source=medium&utm_campaign=newsletter) et obtenez les meilleures nouvelles sur les bots et un contenu exclusif de l'industrie.**