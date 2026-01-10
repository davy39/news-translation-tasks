---
title: 'Comment écrire moins de bugs : conseils pour les développeurs de jeux'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-27T00:47:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-fewer-bugs-tips-for-game-developers-82e3d742f6f7
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pHeuHrK2mkKIukWExHBCVA.jpeg
tags:
- name: Game Development
  slug: game-development
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: technology
  slug: technology
seo_title: 'Comment écrire moins de bugs : conseils pour les développeurs de jeux'
seo_desc: 'By Richard Taylor

  Preface

  I have made a lot of games. The end phase of game development is usually hard. The
  dreaded crunch, the extra mile to fix bugs and add polish can be very arduous for
  all involved.

  If you are lucky the crunch is driven by pass...'
---

Par Richard Taylor

### **Préface**

J'ai créé beaucoup de jeux. La phase finale du développement de jeux est généralement difficile. Le redoutable "crunch", les efforts supplémentaires pour corriger les bugs et ajouter des finitions peuvent être très ardus pour tous les participants.

Si vous avez de la chance, le crunch est motivé par la passion et le désir d'atteindre une vision collective. Si vous n'avez pas de chance, il est motivé par un surengagement et des délais impossibles. (_En réalité, la chance n'a rien à voir avec cela, mais c'est une discussion pour une autre fois._)

Le langage que nous, développeurs, utilisons lorsque nous parlons des bugs est très révélateur. Généralement quelque chose comme "QA a trouvé un bug dans mon code !" L'implication est que le bug et le code sont des entités séparées, un peu comme découvrir une chenille dans une laitue que vous alliez manger.

Cela est, bien sûr, loin de la vérité — sans le code, il n'y a pas de bug. La laitue peut être retirée pour laisser la chenille, le code ne peut pas être retiré pour laisser le bug. Sans le code, il n'y a pas de bug. La réalité est qu'il n'y a pas de bugs, juste du code qui satisfait les exigences nécessaires à un degré plus ou moins grand.

Ce langage de non-responsabilité peut être très peu utile lorsque l'on essaie de parler d'approches pour créer moins de bugs, "Que voulez-vous dire, les bugs arrivent simplement, le débogage fait partie du cycle logiciel."

Dans mon expérience, la plupart des projets de développement de jeux passent une quantité significative de ressources à corriger des bugs tout au long du projet et en masse à la fin d'un projet. Cela représente essentiellement du temps et des efforts gaspillés ; si ces ingénieurs ne corrigeaient pas de bugs, ils pourraient ajouter des finitions et améliorer la qualité.

**La réponse est claire : Écrivez moins de bugs !**

Étant donné que tous les bugs ne sont que du code, alors tous les bugs ont été ajoutés par l'équipe de développement. Peut-être devriez-vous demander à votre équipe de développement d'écrire moins de bugs ?

Si vous riez de cette suggestion, je ne suis pas surpris. Dans mon expérience, c'est une réaction typique des ingénieurs : personne n'écrit de bugs intentionnellement, n'est-ce pas ? Pourtant, du point de vue d'un projet, il s'agit d'une demande entièrement raisonnable. Imaginez l'augmentation de la qualité ou la réduction des heures supplémentaires si le temps passé à corriger des bugs pouvait simplement être supprimé de l'emploi du temps.

La partition entre code et bugs rend cette demande très difficile à prendre au sérieux. Nous sommes tellement habitués à cette façon de penser qu'elle semble être une question absurde. Alors, comment transformer écrire moins de bugs en une demande sensée à laquelle votre équipe d'ingénierie peut adhérer ?

### **Début d'un nouveau projet. Étape un, ne pas répéter les erreurs précédentes.**

Notre équipe a travaillé ensemble sur plusieurs projets AAA et nous venions de terminer Driveclub. Nous savions tous que nous ne voulions pas passer les derniers mois de notre prochain projet à courir après nos propres erreurs. C'était le moment de faire quelque chose à ce sujet. Nous voulions passer du temps à peaufiner le jeu, pas à corriger des bugs. En commençant un nouveau projet, nous nous sommes assis avec l'intention d'explorer l'idée d'écrire moins de bugs.

Nous devons développer un langage et un raisonnement qui permettront à l'équipe de s'approprier le problème. Il doit être clair que l'objectif est réalisable et que la responsabilité incombe aux individus spécifiques.

La première étape est de définir le pourquoi. Nous avons le pourquoi de haut niveau : réduire le temps passé à corriger des bugs et passer plus de temps à améliorer la qualité. Tout le monde peut adhérer à moins d'heures supplémentaires, mais pourquoi est-ce que je demande à vous de résoudre le problème ?

Ce n'est pas seulement moins de temps perdu, mais plus de temps que vous pouvez passer sur les tâches intéressantes qui vous font sortir du lit le matin. Plus de RnD, plus d'optimisation, plus de gameplay, plus de fidélité visuelle, plus d'excellence. **C'est une vision qui parle à pourquoi nous sommes tous développeurs de jeux. Plus de temps sur les trucs cool.**

Même avec une vision claire, écrire moins de bugs est une déclaration si générale qu'elle est effectivement inutile. C'est une déclaration d'intention, mais elle ne donne aucune indication sur la manière dont nous pourrions faire une telle chose. Et encore plus important, comment le temps investi dans écrire moins de bugs peut être transformé en un bénéfice net.

Transformer écrire moins de bugs en une sorte de direction technique que l'équipe d'ingénierie peut adopter va prendre du temps et des efforts significatifs. À ce stade, il est trop facile de regarder les délais du projet et de décider de maintenir le statu quo. Après tout, les bugs sont inévitables et nous avons un projet à livrer.

Pour découvrir le comment, nous suivons la méthode scientifique de base : **Observation, Hypothèse, Tests, Répéter.**

### **Observations**

#### **Catégorisation — Analyse forensique**

Ouvrez la base de données des bugs de votre dernier projet terminé et jetez un coup d'œil. Il existe de nombreux types de bugs différents, donc dire simplement moins de bugs est essentiellement sans signification.

Pour pouvoir discuter du problème, nous avons d'abord besoin de mieux définir les spécificités. Dans ce cas, nous étions particulièrement intéressés par les bugs qui absorbent des quantités significatives de temps d'ingénierie. Nous avons analysé la base de données des bugs et identifié 2 cohortes significatives que nous voulions aborder :

* Les bugs qui ont pris beaucoup de temps à corriger, et
* les bugs qui régressaient continuellement.

Essentiellement 2 valeurs KPI pour les bugs : jours pour corriger accepté et nombre de transitions d'état de bug.

Les bugs avec un long temps de correction sont généralement des bugs difficiles à reproduire ou à diagnostiquer. Les bugs avec de nombreuses transitions d'état rebondissent souvent autour de cannot repo ou de boucles fix / reopen.

En utilisant ces KPI, nous avons identifié un ensemble plus petit de bugs qui représentent une quantité disproportionnellement grande de temps d'ingénierie. Nous avons eu quelques faux positifs dans ces cohortes qui ont été écartés à l'étape suivante. Enfin, nous avions notre façon d'aborder le problème.

#### **Analyse**

Ayant identifié des cohortes spécifiques de bugs, l'étape suivante était d'essayer d'identifier les points communs et les causes profondes. Cela a nécessité une combinaison d'expérience en programmation et d'interprétation de la description des bugs. Par-dessus tout, cela a nécessité du temps et de la persévérance.

Nous avions une intégration entre notre base de données de bugs et SCM. Cela a permis une certaine corrélation directe avec le code source, bien que le rapport de bruit était élevé et nécessitait encore une interprétation expérimentée.

#### **Cause profonde**

Finalement, après suffisamment de temps, certains schémas ont émergé et nous avons pu voir qu'un sous-ensemble de bugs représentait effectivement une quantité significative de temps d'ingénierie. Étant donné ces bugs, nous étions déterminés à en trouver la cause profonde, jusqu'au code source.

En travaillant avec les ingénieurs, nous avons trouvé les modifications de correction. Nous avons ensuite compilé plus de listes de systèmes, de fichiers et de lignes de code liées aux problèmes significatifs. En fin de compte, nous avions une liste de modifications de code spécifiques à discuter avec l'équipe d'ingénierie.

#### **Je vous l'avais dit**

Ensuite, nous avons pu nous asseoir avec l'équipe d'ingénierie plus large pour discuter de nos conclusions (et ils étaient presque certainement conscients de tous les problèmes dans le code !!!). Donc, si l'équipe connaît déjà les problèmes dans le code, qu'avons-nous accompli ? La réponse est quelque chose de très important.

**Nous avons créé une cartographie entre temps de développement perdu et zones spécifiques du code. Cela nous donne un moyen de classer objectivement la valeur de toute refactorisation et maintenance proposée.**

Cela sert également à mettre en évidence les zones de code qui sont devenues acceptablement mauvaises. Ce fut notre plus grande surprise. Je me suis retrouvé à dire il est clair que nous devons refactoriser ce système lorsque l'équipe d'ingénierie l'avait déjà écarté comme trop gros travail ou simplement pas réalisable.

En effet, beaucoup des problèmes de cause profonde étaient systémiques. En particulier, beaucoup des problèmes invisibles impliquaient des modèles de programmation généralement acceptés. **Cela signifie que la correction de ces problèmes nécessiterait de défier les tendances, les modes et les mantras actuels de la programmation.**

(En fin de compte, ces causes profondes étaient si systémiques dans l'architecture du code qu'elles nous ont conduit à tout recommencer entièrement à partir de zéro. Mais c'est un sujet pour un autre article de blog.)

Enfin, nous avions assez d'observations pour faire des hypothèses et toute l'équipe a été impliquée dans le voyage.

### **Hypothèse**

> **Hypothèse 1** — Certains modèles de programmation seront statistiquement plus susceptibles de causer des bugs dans un grand projet logiciel.

> **Hypothèse 2** — Le temps passé à corriger des bugs tout au long du projet sera réduit si nous évitons l'utilisation des modèles de programmation identifiés par (1).

Aux fins de cet article, définissons un grand projet comme 25+ programmeurs et 12+ mois de développement. Un projet suffisamment grand pour que les points suivants soient vrais :

a) Tout code vivra suffisamment longtemps pour que le coût de maintenance l'emporte sur le coût de développement.

b) La complexité découlant de la colle entre les systèmes est plus grande que la complexité de tout système unique.

Pourquoi est-ce significatif ? Dans les petits projets logiciels, vous pouvez vous en sortir avec n'importe quoi, l'ingénierie logicielle n'a essentiellement pas d'importance. Le code est entièrement à vous.

Dans un grand projet, le code n'est PAS à vous. Vous travaillerez avec du code que vous ne comprenez pas et prendrez des décisions d'ingénierie basées sur des connaissances et des hypothèses imparfaites. Maintenant, lorsque nous parlons au reste de l'équipe, le message est très différent.

Ayant analysé nos projets précédents, nous avons fait l'hypothèse suivante...

Les données montrent que ces modèles de programmation spécifiques étaient un facteur commun impliqué dans les problèmes. Nous croyons qu'éviter ces modèles réduira le temps passé à corriger des bugs et améliorera la qualité.

Ensuite, nous devons transformer les hypothèses en quelque chose d'utilisable.

### **Test**

Une partie importante de la direction technique et de l'architecture des systèmes pour le prochain projet serait basée sur l'évitement des modèles de code à haut risque identifiés.

* Couplage de la durée de vie de l'allocation mémoire avec la construction et la durée de vie des objets.
* Surcharge des opérateurs et conventions de nommage dénormalisées.
* auto, fonctions polymorphes et suppression de la sécurité des types.([https://medium.freecodecamp.org/why-the-compiler-is-your-best-friend-f165329cb20a](https://medium.freecodecamp.org/why-the-compiler-is-your-best-friend-f165329cb20a))
* Pousser la complexité vers le haut par injection de dépendances, rappels, lambdas,
* Utilisation de mutex, sémaphores et autres primitives de threading dans le code de haut niveau.

Chacun de ces points mérite une discussion technique sur la manière dont il a changé notre approche des systèmes et de la conception des API. Comme cette discussion technique serait pour un public légèrement différent, je les aborderai dans des articles techniques de suivi séparés.

#### **Qu'est-il arrivé ensuite ?**

Comme je l'ai mentionné ci-dessus, nous avons eu beaucoup de chance et avons eu l'opportunité de commencer un nouveau jeu avec une nouvelle approche. Nous avons pu construire un nouveau moteur de jeu à partir de zéro en 24 mois et livrer le jeu à temps avec une petite équipe de programmation. Même si le code n'avait jamais été livré auparavant, nous avons atteint un niveau élevé de finition avec relativement peu de bugs et très peu de bugs coûteux. Cela a été confirmé de manière indépendante par le département QA qui a documenté la facilité avec laquelle le jeu a traversé le processus QA.

Demander à l'équipe d'éviter les modèles ci-dessus n'était pas suffisant. Les directives de codage sont faciles à oublier et l'équipe aurait pu rapidement retomber dans de vieilles habitudes. Une décision clé a été de concevoir le code, les systèmes et les interfaces de manière à ce que les modèles ci-dessus ne puissent pas être utilisés. Cela s'est rapidement transformé en un mantra rendre difficile de faire la mauvaise chose qui a guidé l'équipe tout au long du projet.

Importamment, l'équipe était plus heureuse. Nous avions défini une approche qui a abouti à plus de code fonctionnant du premier coup. L'équipe savait que la manière évidente et facile d'utiliser un système était probablement correcte et que l'API empêcherait les mauvais modèles. Il y avait moins de bugs et plus de temps passé sur les fonctionnalités, les finitions et les itérations.

### Lectures complémentaires.

Vous pouvez consulter ces diapositives annotées contenant des directives techniques spécifiques dérivées de l'approche Écrire moins de bugs.

[https://www.slideshare.net/RichardTaylor172/c-restrictions-for-game-programming](https://www.slideshare.net/RichardTaylor172/c-restrictions-for-game-programming)

![Image](https://cdn-media-1.freecodecamp.org/images/PEiGLDLWyj93R8M4ot-OpdUjsmbjxjTwmD1o)