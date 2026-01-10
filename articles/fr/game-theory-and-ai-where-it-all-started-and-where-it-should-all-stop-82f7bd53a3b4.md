---
title: 'Besoin d''évolution : théorie des jeux et IA'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-12T21:07:00.000Z'
originalURL: https://freecodecamp.org/news/game-theory-and-ai-where-it-all-started-and-where-it-should-all-stop-82f7bd53a3b4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ddulq7MNPa7NPjVf5xCuEw.jpeg
tags:
- name: Artificial Intelligence
  slug: artificial-intelligence
- name: Game Theory
  slug: game-theory
- name: Machine Learning
  slug: machine-learning
- name: Reinforcement Learning
  slug: reinforcement-learning
- name: technology
  slug: technology
seo_title: 'Besoin d''évolution : théorie des jeux et IA'
seo_desc: 'By Elena Nisioti

  Artificial Intelligence (AI) is full of questions that cannot be answered and answers
  that cannot be assigned to the correct questions. In the past, it paid for its persistence
  to wrong practices with periods of stagnation, known as ...'
---

Par Elena Nisioti

L'intelligence artificielle (IA) est pleine de questions sans réponse et de réponses sans question. Par le passé, elle a payé sa persistance à de mauvaises pratiques par des périodes de stagnation, connues sous le nom d'hivers de l'IA. Le calendrier de l'IA, cependant, vient tout juste d'atteindre le printemps, et les applications fleurissent.

Pourtant, il existe une branche de l'IA qui a longtemps été négligée. Il s'agit de l'apprentissage par renforcement, qui a récemment montré des résultats impressionnants sur des jeux comme [AlphaGo](https://www.deepmind.com/research/highlighted-research/alphago) et [Atari](https://www.deepmind.com/publications/playing-atari-with-deep-reinforcement-learning). Mais soyons honnêtes : ce n'étaient pas des victoires de l'apprentissage par renforcement. Ce qui est devenu plus profond dans ces cas, ce sont les réseaux de neurones profonds, et non notre compréhension de l'apprentissage par renforcement, qui conserve la profondeur qu'il a atteinte il y a des décennies.

Encore pire est le cas de l'apprentissage par renforcement lorsqu'il est appliqué à des problèmes réels. Si entraîner un robot à marcher sur une corde semble difficile, essayez d'entraîner une équipe de robots à gagner un match de football, ou une équipe de drones à surveiller une cible en mouvement.

Avant de perdre la branche, ou même l'arbre, nous devons affiner notre compréhension de ces applications. La théorie des jeux est l'approche la plus courante pour étudier des équipes de joueurs partageant un objectif commun. Elle peut nous fournir des outils pour guider les algorithmes d'apprentissage dans ces contextes.

Mais voyons pourquoi l'approche commune n'est pas une approche de bon sens.

> Tuer une erreur est un service aussi bon, et parfois même meilleur, que l'établissement d'une nouvelle vérité ou d'un nouveau fait. — Charles Darwin

Tout d'abord, salissons-nous les mains avec un peu de terminologie et de bases de ces domaines.

### Théorie des jeux

#### **Quelques termes utiles**

* **Jeu :** comme les jeux dans la compréhension populaire, il peut s'agir de tout contexte où les joueurs prennent des actions et dont le résultat dépendra d'eux.
* **Joueur :** un décideur stratégique au sein d'un jeu.
* **Stratégie :** un plan complet d'actions qu'un joueur entreprendra, étant donné l'ensemble des circonstances qui pourraient survenir au sein du jeu.
* **Gain :** le bénéfice qu'un joueur reçoit en arrivant à un résultat particulier d'un jeu.
* **Équilibre :** le point dans un jeu où les deux joueurs ont pris leurs décisions et un résultat est atteint.
* **Équilibre de Nash :** un équilibre dans lequel aucun joueur ne peut gagner en changeant sa propre stratégie si les stratégies des autres joueurs restent inchangées.
* **Stratégie dominante :** se produit lorsqu'une stratégie est meilleure qu'une autre stratégie pour un joueur, peu importe comment les adversaires de ce joueur peuvent jouer.

#### **Dilemme du prisonnier**

Il s'agit probablement du jeu le plus célèbre de la littérature. La figure ci-dessous présente sa matrice de gains. Maintenant, une matrice de gains vaut mille mots. Elle est suffisante, pour un œil expérimenté, pour fournir toutes les informations nécessaires pour décrire un jeu. Mais soyons un peu moins laconiques.

![Image](https://cdn-media-1.freecodecamp.org/images/3C9rRuM6lrhidno7Ihm5g82g2CLkNPSMrD0R)
_Matrice de gains du dilemme du prisonnier_

La police arrête deux criminels, le criminel A et le criminel B. Bien que assez notoires, les criminels ne peuvent pas être emprisonnés pour le crime sous enquête en raison du manque de preuves. Mais ils peuvent être détenus pour des chefs d'accusation mineurs.

La durée de leur emprisonnement dépendra de ce qu'ils diront dans la salle d'interrogatoire, ce qui donne lieu au jeu. Chaque criminel (joueur) a la chance de soit rester silencieux, soit dénoncer l'autre criminel (joueur). La matrice de gains décrit combien d'années chaque joueur sera emprisonné en fonction du résultat. Par exemple, si le joueur A reste silencieux et que le joueur B le dénonce, le joueur A purgera 3 ans (-3) et le joueur B ne purgera rien (0).

Si vous examinez attentivement la matrice de gains, vous découvrirez que l'action logique d'un joueur est de trahir l'autre personne ou, en termes de théorie des jeux, trahir est la stratégie dominante. Cela conduira à l'équilibre de Nash du jeu, où chaque joueur a un gain de -2.

Quelque chose semble-t-il étrange ? Oui, ou du moins cela devrait être le cas. Si les deux joueurs s'étaient somehow mis d'accord pour rester silencieux, ils auraient tous deux obtenu une récompense plus élevée de -1. Le dilemme du prisonnier est un exemple de jeu où la rationalité conduit à un résultat pire que la coopération.

#### **Quelques remarques historiques**

La théorie des jeux trouve son origine en économie, mais est aujourd'hui un domaine d'étude interdisciplinaire. Son père, John von Neumann (vous remarquerez que les Johns ont de sérieuses perspectives de carrière dans ce domaine), a été le premier à donner une formulation stricte à la notion commune de jeu. Il a restreint ses études aux jeux de deux joueurs, car ils étaient plus faciles à analyser.

Il a ensuite co-écrit un livre avec Oskar Morgenstern, qui a posé les fondations de la théorie de l'utilité espérée et façonné le cours de la théorie des jeux. À cette époque, John Nash a introduit le concept d'équilibres de Nash, qui aide à décrire le résultat d'un jeu.

### Apprentissage par renforcement

Il n'a pas fallu longtemps pour réaliser à quel point les applications de la théorie des jeux peuvent être vastes. Des jeux à la biologie, la philosophie et, attendez-le, l'intelligence artificielle. La théorie des jeux est aujourd'hui étroitement liée aux contextes où plusieurs joueurs apprennent par renforcement, un domaine appelé apprentissage par renforcement multi-agents. Des exemples d'applications dans ce cas sont des équipes de robots, où chaque joueur doit apprendre à se comporter en faveur de son équipe.

#### **Quelques termes utiles**

* **Agent :** équivalent à un joueur.
* **Récompense :** équivalente à un gain.
* **État :** toutes les informations nécessaires pour décrire la situation dans laquelle se trouve un agent.
* **Action :** équivalent d'un mouvement dans un jeu.
* **Politique :** similaire à une stratégie, elle définit l'action qu'un agent entreprendra lorsqu'il se trouvera dans des états particuliers.
* **Environnement :** tout ce avec quoi l'agent interagit pendant l'apprentissage.

#### Applications

Imaginez le scénario suivant : une équipe de drones est lâchée dans une forêt afin de prédire et de localiser les incendies suffisamment tôt pour que les pompiers puissent intervenir. Les drones sont autonomes et doivent explorer la forêt, apprendre quelles conditions sont susceptibles de provoquer un incendie, et coopérer entre eux, afin qu'ils couvrent de vastes zones de la forêt en utilisant peu de batterie et de communication.

Cette application appartient au domaine de la surveillance environnementale, où l'IA peut prêter ses compétences prédictives à l'intervention humaine. Dans un monde technologique qui devient de plus en plus complexe et un monde physique sous menace, nous pouvons paraphraser [la citation de Kipling](https://www.brainyquote.com/quotes/rudyard_kipling_118509) en « L'homme ne peut pas être partout, et c'est pourquoi il a fait des drones. »

Les architectures décentralisées sont un autre domaine d'application intéressant. Des technologies comme l'[Internet des objets](https://en.wikipedia.org/wiki/Internet_of_things) et la Blockchain créent des réseaux immenses. L'information et le traitement sont distribués dans différentes entités physiques, une caractéristique qui a été reconnue pour offrir confidentialité, efficacité et démocratisation.

Qu'il s'agisse d'utiliser des capteurs pour minimiser la consommation d'énergie dans les foyers d'un pays, ou de remplacer le système bancaire, le décentralisé est le nouveau sexy.

Rendre ces réseaux intelligents, cependant, est un défi, car la plupart des algorithmes d'IA dont nous sommes fiers sont gourmands en données et en calculs. Les algorithmes d'apprentissage par renforcement peuvent être utilisés pour un traitement efficace des données et rendre le réseau adaptatif aux changements de son environnement. Dans ce cas, il est intéressant, et bénéfique pour l'efficacité globale, d'étudier comment les algorithmes individuels coopéreront.

![Image](https://cdn-media-1.freecodecamp.org/images/RcvtMhf4sDKByN00Jncb2s9aMCNZ5cB39fmv)
_Apprentissage profond ou collectif ? La recherche en IA a basé sa récolte sur des réseaux de plus en plus profonds, mais il se pourrait que les réponses aux problèmes difficiles proviennent de la connaissance collective, et non d'individus profondément enracinés. Avons-nous manqué la forêt ?_

### Pas seulement un jeu

Traduire les problèmes d'IA en jeux simples comme le dilemme du prisonnier est tentant. C'est une pratique courante lors du test de nouvelles techniques, car elle offre un banc d'essai intuitif et peu coûteux en calcul. Néanmoins, il est important de ne pas ignorer l'effet que les caractéristiques pratiques du problème, telles que le bruit, les retards et la mémoire finie, ont sur l'algorithme.

Peut-être l'hypothèse la plus trompeuse dans la recherche en IA est celle de représenter l'interaction avec des jeux statiques itérés. Par exemple, un algorithme peut appliquer le jeu du dilemme du prisonnier chaque fois qu'il veut prendre une décision, une formulation qui suppose que l'agent n'a pas appris, ou changé, en cours de route. Mais quel effet l'apprentissage aura-t-il sur le comportement de l'agent ? L'interaction avec les autres n'affectera-t-elle pas sa stratégie ?

La recherche dans ce domaine s'est concentrée sur [l'évolution de la coopération](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation) et Robert Axelrod a étudié les stratégies optimales qui émergent dans la version itérée du dilemme du prisonnier. Les [tournnois](https://en.wikipedia.org/wiki/The_Evolution_of_Cooperation#Axelrod%27s_tournaments) qu'Axelrod a organisés ont révélé que les stratégies qui s'adaptent avec le temps et l'interaction, même aussi simples que Tit-for-Tat, sont très efficaces. La communauté de l'IA a [récemment](https://arxiv.org/abs/1803.00162) étudié l'apprentissage sous le **dilemme du prisonnier séquentiel**_,_ mais la recherche dans ce domaine est encore à un stade prématuré.

Ce qui différencie l'apprentissage multi-agents de l'apprentissage mono-agent est la complexité accrue. Entraîner un seul réseau de neurones profond est déjà suffisamment douloureux, tandis que l'ajout de nouveaux réseaux, en tant que parties des agents, rend le problème exponentiellement plus difficile.

Une préoccupation moins évidente, mais plus importante, est le manque de propriétés théoriques pour ce type de problème. L'apprentissage par renforcement mono-agent est un domaine bien compris, car Richard Bellman et Christopher Watkins ont fourni les algorithmes et les preuves nécessaires pour apprendre. Dans le cas multi-agents, cependant, les preuves perdent leur validité.

Pour illustrer certaines des difficultés déconcertantes qui surgissent : un agent exécute un algorithme d'apprentissage pour apprendre à réagir de manière optimale à son environnement. Dans notre cas, l'environnement inclut les autres agents, qui exécutent également l'algorithme d'apprentissage. Ainsi, l'algorithme doit considérer l'effet de son action avant d'agir.

### **Les premières préoccupations**

Les préoccupations commencent là où la théorie des jeux a commencé : en économie. Commençons par quelques hypothèses faites lors de l'étude d'un système sous la théorie des jeux classique.

**Rationalité :** généralement en théorie des jeux, et afin de dériver les équilibres de Nash, une rationalité parfaite est supposée. Cela signifie grossièrement que les agents agissent toujours pour leur propre bien.

**Information complète :** chaque agent connaît tout sur le jeu, y compris les règles, ce que les autres joueurs savent, et quelles sont leurs stratégies.

**Connaissance commune :** il y a une connaissance commune d'un fait **p** dans un groupe d'agents lorsque : tous les agents connaissent **p**, ils savent tous que tous les agents connaissent **p**, ils savent tous qu'ils savent tous que tous les agents connaissent **p**, et ainsi de suite **ad infinitum**_._ Il existe des énigmes intéressantes, comme celle des [insulaires aux yeux bleus](http://mesosyn.com/mental1-2.html), qui décrivent l'effet de la connaissance commune sur un problème.

En 1986, Kenn Arrow a exprimé ses réserves envers la théorie des jeux classique.

> Dans [cet article](http://dieoff.org/_Economics/RationalityOfSelfAndOthersArrow.pdf), je veux démêler certains des sens dans lesquels l'hypothèse de rationalité est utilisée en théorie économique. En particulier, je veux souligner que la rationalité n'est pas une propriété de l'individu seul, bien qu'elle soit généralement présentée de cette manière. Plutôt, elle rassemble non seulement sa force mais aussi son sens même du contexte social dans lequel elle est intégrée. Elle est la plus plausible dans des conditions très idéales. Lorsque ces conditions cessent de s'appliquer, les hypothèses de rationalité deviennent tendues et éventuellement même auto-contradictoires.

Si vous trouvez qu'Arrow est un peu dur avec la théorie des jeux classique, à quel point diriez-vous que vos derniers achats ont été rationnels ? Ou, combien de conscience et d'effort avez-vous mis dans votre repas aujourd'hui ?

Mais Arrow n'est pas tant inquiet de l'hypothèse de rationalité. Il est inquiet des implications de celle-ci. Pour qu'un agent soit rationnel, vous devez lui fournir toutes les informations nécessaires pour prendre ses décisions. Cela nécessite des joueurs omniscients, ce qui est mauvais à deux égards : premièrement, cela crée des exigences irréalistes pour le stockage et le traitement de l'information des joueurs. Deuxièmement, la théorie des jeux n'est plus une **théorie des jeux**, car vous pouvez remplacer tous les joueurs par un dirigeant central (et où est le plaisir dans cela ?).

La valeur de l'information dans cette perspective est un autre point d'intérêt. Nous avons déjà discuté du fait que posséder toutes les informations est irréalisable. Mais qu'en est-il de supposer des joueurs avec des connaissances limitées ? Cela aiderait-il ?

Vous pouvez demander à quiconque impliqué dans ce domaine, mais il suffit de dire que l'optimisation sous incertitude est difficile. Oui, il y a encore les bons vieux équilibres de Nash. Le problème est qu'ils sont infinis. La théorie des jeux ne vous fournit pas d'arguments pour les évaluer. Donc, même si vous en atteignez un, vous ne devriez pas en faire tout un plat.

### **Préoccupations en matière d'apprentissage par renforcement**

À ce stade, vous devriez suspecter que les applications d'IA sont beaucoup plus compliquées que les exemples auxquels la théorie des jeux classique s'intéresse. Juste pour mentionner quelques obstacles sur le chemin de l'application de l'approche de l'équilibre de Nash dans une application robotique : imaginez être le capitaine d'une équipe de robots jouant au football dans la RoboCup. À quel point vos joueurs et vos adversaires sont-ils rapides, forts et intelligents ? Quelles stratégies l'équipe adverse utilise-t-elle ? Comment devriez-vous récompenser vos joueurs ? Un but est-il la seule raison de féliciter, ou applaudir une bonne passe améliorera-t-il également le comportement de l'équipe ? Clairement, connaître les règles du football ne vous fera pas gagner le match.

Si la théorie des jeux a suscité des débats pendant des décennies, si elle a été fondée sur des hypothèses irréalistes et, pour des tâches réalistes, si elle offre des solutions compliquées et peu comprises, pourquoi continuons-nous à l'utiliser ? Eh bien, tout simplement, c'est la seule chose que nous ayons lorsqu'il s'agit de raisonnement de groupe. Si nous comprenions réellement comment les groupes interagissent et coopèrent pour atteindre leurs objectifs, la psychologie et la politique seraient beaucoup plus claires.

Les chercheurs dans le domaine de l'apprentissage par renforcement multi-agents omettent soit complètement une discussion sur les propriétés théoriques de leurs algorithmes (et exhibent néanmoins souvent de bons résultats), soit étudient traditionnellement l'existence d'équilibres de Nash. Cette dernière approche semble, aux yeux d'un jeune chercheur dans le domaine, comme une lutte pour prouver, sous des hypothèses sévères et irréalistes, l'existence théorique de solutions qui — étant infinies et de valeur douteuse — ne seront jamais exploitées en pratique.

### **Théorie des jeux évolutionnistes**

L'émergence de la théorie des jeux évolutionnistes n'est pas récente, mais ses applications de grande portée dans le domaine de l'IA ont mis du temps à être reconnues. Originaire de la biologie, elle a été introduite en 1973 par John M. Smith et George R. Price, comme une alternative à la théorie des jeux classique. Les modifications sont si profondes que nous pouvons parler d'une toute nouvelle approche.

Le sujet du raisonnement n'est plus le joueur lui-même, mais la population de joueurs. Ainsi, les stratégies probabilistes sont définies comme le pourcentage de joueurs qui font un choix, et non la probabilité qu'un joueur choisisse une action comme dans la théorie des jeux classique. Cela élimine la nécessité d'agents rationnels et omniscients, car les stratégies évoluent comme des modèles de comportement. Le processus d'évolution ressemble à la théorie darwinienne. Les joueurs se reproduisent selon les principes de la survie du plus apte et des mutations aléatoires, et peuvent être élégamment décrits par un ensemble d'équations différentielles, appelées **dynamique des réplicateurs**.

Nous pouvons voir les trois parties importantes de ce système dans l'illustration ci-dessous. Une population représente l'équipe d'agents et est caractérisée par un mélange de stratégies. Les règles du jeu déterminent les gains de la population, qui peuvent également être vus comme les valeurs de fitness d'un algorithme évolutionniste. Enfin, les règles des réplicateurs décrivent comment la population évoluera en fonction des valeurs de fitness et des propriétés mathématiques du processus d'évolution.

![Image](https://cdn-media-1.freecodecamp.org/images/pcZhSDCQhuD1w4AMlmVxdNV-M0cymDbheIM8)
_Crédit image : Par HowieKor [CC BY-SA 3.0 ([https://creativecommons.org/licenses/by-sa/3.0](https://creativecommons.org/licenses/by-sa/3.0" rel="noopener" target="_blank" title="))], de Wikimedia Commons_

La notion et la poursuite des équilibres de Nash sont remplacées par des **stratégies stables évolutionnistes**_._ Une stratégie peut porter cette caractérisation si elle est immunisée contre une invasion par une population d'agents qui suivent une autre stratégie, à condition que la population envahissante soit petite. Ainsi, le comportement de l'équipe peut être étudié sous le domaine bien compris de la stabilité des systèmes dynamiques, tels que la [stabilité de Lyapunov](https://en.wikipedia.org/wiki/Lyapunov_stability).

> L'atteinte de l'équilibre nécessite un processus de déséquilibre. Que signifie le comportement rationnel en présence de déséquilibre ? Les individus spéculent-ils sur le processus d'équilibrage ? Si c'est le cas, le déséquilibre peut-il être considéré, en quelque sorte, comme un processus d'équilibre d'ordre supérieur ?

Dans le passage ci-dessus, Arrow semble lutter pour identifier les propriétés dynamiques d'un jeu. La théorie des jeux évolutionnistes pourrait-elle être une réponse à ses questions ?

Tout récemment, des algorithmes célèbres d'apprentissage par renforcement, tels que [Q-learning](https://link.springer.com/chapter/10.1007/978-3-540-39857-8_38), ont été étudiés sous cette nouvelle approche et des conclusions significatives ont été tirées. La manière dont cet nouvel outil est utilisé dépend finalement de l'application.

Nous pouvons suivre l'approche directe, pour dériver le modèle dynamique d'un algorithme d'apprentissage. Ou l'inverse, où nous partons de certaines propriétés dynamiques souhaitées et concevons un algorithme d'apprentissage qui les exhibe.

Nous pouvons utiliser la dynamique des réplicateurs de manière descriptive, pour visualiser la convergence. Ou de manière prescriptive, pour ajuster l'algorithme afin de converger vers des solutions optimales. Cette dernière peut considérablement réduire la complexité impliquée dans l'entraînement de réseaux profonds pour les tâches difficiles auxquelles nous sommes confrontés aujourd'hui, en éliminant le besoin d'ajustement aveugle.

### Conclusion

Il n'est pas difficile de retracer quand et pourquoi les chemins de la théorie des jeux et de l'IA sont devenus compliqués. Ce qui est plus difficile, cependant, est de négliger les restrictions que l'IA, et en particulier l'apprentissage par renforcement multi-agents, doit affronter lorsqu'elle suit les approches théoriques classiques des jeux.

La théorie des jeux évolutionnistes semble prometteuse, offrant à la fois des outils théoriques et des avantages pratiques, mais nous ne saurons vraiment que lorsque nous l'aurons essayée. Dans ce cas, l'évolution ne surgira pas naturellement, mais d'une lutte consciente de la communauté de recherche pour l'amélioration. Mais n'est-ce pas l'essence de l'évolution ?

Il faut un certain effort pour s'écarter de là où l'inertie vous pousse, mais l'apprentissage par renforcement, malgré les succès généraux de l'IA, a sérieusement besoin d'un coup de pouce.