---
title: Comment concevoir visuellement l'état en JavaScript
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-20T15:39:10.000Z'
originalURL: https://freecodecamp.org/news/how-to-visually-design-state-in-javascript-3a6a1aadab2b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*yZWunekTH1rb4DgIGwoPXw.jpeg
tags:
- name: Statecharts
  slug: statecharts
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: technology
  slug: technology
seo_title: Comment concevoir visuellement l'état en JavaScript
seo_desc: 'By Shawn McKay

  A roadmap for developing applications with state machines & statecharts


  _Photo by [Unsplash](https://unsplash.com/photos/lRssALOk1fU?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText"
  rel="noopener" target="_blank" ti...'
---

Par Shawn McKay

#### _Une feuille de route pour développer des applications avec des machines à états et des statecharts_

![Image](https://cdn-media-1.freecodecamp.org/images/Aok0bLw6goCsqIi-E0awku8Os9f6qvl969AH)
_Photo par [Unsplash](https://unsplash.com/photos/lRssALOk1fU?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel</a> sur <a href="https://unsplash.com/search/photos/map?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Pourquoi la gestion d'état semble-t-elle particulièrement délicate en JavaScript ? Est-ce la complexité inhérente des applications modernes, ou simplement les outils ? Comment d'autres domaines de l'ingénierie développent-ils des systèmes fiables et prévisibles ? Est-il possible de dessiner un système et de le transformer en code, et vice versa ?

Explorons un changement de paradigme dans la gestion d'état vers la conception visuelle de systèmes avec des **machines à états** et des **statecharts**.

### Concepts > Libs

La gestion d'état me préoccupe depuis un certain temps. J'ai expérimenté diverses bibliothèques de gestion d'état : Flux, Reflux, Redux, Dva, Vuex, Mobx, et aussi [la mienne](https://github.com/rematch/rematch).

![Image](https://cdn-media-1.freecodecamp.org/images/QgmolkLumTmVxfq7iqvnfE61r7hf4cElnIKG)

Il est inutile de discuter pour savoir laquelle est la solution 10x. Les bibliothèques d'état sont différentes saveurs avec les mêmes ingrédients. Elles font partie du puzzle—elles facilitent la synchronisation et la connexion des données.

Les solutions qui nécessitent notre attention concernent le tableau plus large :

Nous devons nous améliorer dans la **planification et la conception des systèmes**.

### Casser toutes les choses

Pensez à une interface utilisateur que vous considéreriez comme **élégante**. Quelque chose de construit pour résister à une rafale d'interactions utilisateur aléatoires—vous savez, le genre d'imprévisibilité qui se produit lorsqu'un utilisateur appuie sur un bouton plus de fois que prévu, interagit avec des entrées dans un ordre inattendu ou vous amène à remettre en question votre foi en l'humanité. La vie réelle est dure pour les systèmes.

Je vais deviner le projet auquel vous pensez.

Eh bien… vous ne pensez probablement pas à quelque chose de construit pour le web, où la philosophie semble être « avancer vite et casser des choses ».

À en juger par la fréquence des mises à jour, vous ne pensez probablement pas non plus au mobile.

Vous ne pensez probablement même pas à quelque chose de construit récemment. Nous ne semblons pas nécessairement nous améliorer dans la construction de produits fiables.

Je pense savoir à quoi vous pensez…

![Image](https://cdn-media-1.freecodecamp.org/images/t8w6rHEwXZ-55I0XjfhIHQhs55ZDjuJV7Flj)

Ai-je raison ? …Non ?

Vous ne reconnaissez peut-être même pas ceci comme le Walkman Sony des années 1980.

Enfant, j'ai reçu un lecteur de cassettes comme celui-ci d'un ami qui était passé à un lecteur CD portable. Je comprends que certains jeunes lecteurs peuvent trouver la mention de ces deux appareils peu familière—considérez le Walkman comme un iPhone, mais avec des boutons plus grands et un potentiel destructeur plus élevé. Ma mission principale : le casser.

J'essayais toutes les combinaisons de boutons pour voir ce qui pourrait se passer :

* Essayer d'éjecter pendant que la cassette était en avance rapide
* Maintenir l'avance rapide et le rembobinage en même temps

Essayez comme je pourrais, le Walkman Sony a tenu mieux que la plupart des sites web aujourd'hui.

### Ingénierie des interfaces

Les appareils électroniques comme le Walkman ont résisté au gauntlet des tests utilisateurs sans aucune capacité à cacher ou désactiver des éléments de l'interface utilisateur. N'importe quel bouton pouvait être pressé à n'importe quel moment, n'importe quoi pouvait arriver. Et pourtant, il semblait **incassable**.

Cela m'a amené à me demander :

**Peut-être que l'électronique offre un meilleur paradigme pour la façon dont nous pouvons construire des interfaces sur le web.**

Que pouvons-nous apprendre du processus de conception **ancien** de l'électronique ? Comment pouvons-nous mieux **concevoir** des applications ? Marty, nous devons retourner vers le futur !

### Électronique & Le Web

L'électronique peut-elle nous enseigner une meilleure façon de créer des applications dans le navigateur ?

Considérez que les **composants** ont produit l'un des changements les plus significatifs dans le développement web au cours des cinq dernières années. Peut-être y a-t-il d'autres concepts que nous pouvons emprunter à l'ingénierie électronique ?

En tant que développeurs web, nous avons eu de la chance. Vraiment de la chance. Trouvé un bug ? Déployez une mise à jour sur votre serveur dans l'heure.

D'autres domaines de l'ingénierie ne sont pas aussi indulgents. Un problème matériel entraîne souvent la mise au rebut d'un appareil. Les développeurs embarqués doivent veiller à ce qu'une mise à jour du micrologiciel ne vide pas la batterie ou ne fasse pas planter tous les appareils existants.

**Les développeurs web ont le luxe d'être imprudents.**

Sans parler du fait que les développeurs d'applications ont rarement été confrontés aux mêmes limitations de ressources que les créateurs de dispositifs électroniques. Quand était la dernière fois que votre préoccupation principale était la **performance** et l'**utilisation de la mémoire**, plutôt que de simplement faire fonctionner le truc ? Un seuil de 60 images par seconde est une barre basse. Mais la barre monte à mesure que nous commençons à construire des applications de plus en plus complexes pour fonctionner sur des appareils mobiles et IoT moins puissants. Nous frôlons un problème d'ingénierie que les ingénieurs de bas niveau ont rencontré depuis des décennies.

**Les contraintes stimulent la créativité**. Les limitations mènent à un meilleur design.

Pour voir comment l'acceptation des limitations peut mener à un meilleur design, nous devons revenir aux principes fondamentaux de la gestion d'état.

### Les anciens/nouveaux principes fondamentaux de la gestion d'état

La direction des conversations dans la communauté web tend à pencher vers les packages NPM plutôt que vers les principes fondamentaux de l'informatique.

**Les ingénieurs ne demandent pas tant « quelle bibliothèque est meilleure ? » que « comment concevoir un meilleur système ».**

Nous pouvons commencer par quelques principes de base d'un bon design :

* distinguer entre les **données** indéterminées et les **états** finis
* limiter les transitions possibles d'un état à un autre
* concevoir visuellement

Je vais travailler sur ces points ainsi que sur mon propre chemin, et les 8 réalisations qui ont suivi.

### 1. État !== Données

Dans les systèmes programmatiques, la différence entre **état** et **données** est floue. Ils vivent tous deux en mémoire, et sont donc traités de la même manière.

Dans React, **état** et **données** partagent le même nom et les mêmes mécanismes :

* obtenir : `this.state`
* stocker : `this.state = {}`
* mettre à jour : `this.setState(nextState)`

En électronique, il y a moins de confusion sur la distinction entre **état** et **données**.

**État** représente un nombre fini de modes dans lesquels le système peut se trouver—souvent défini par le circuit lui-même. Pour notre Walkman, pensez à « Lecture », « Arrêt », « Éjection ». Comme un « mode » ou une « configuration », l'état est dénombrable.

**Données**, en revanche, sont stockées en mémoire avec un ensemble presque infini de paramètres possibles. Pour notre Walkman, pensez à la piste qui est en lecture, « Chanson 2 ». Les données, comme la musique, peuvent avoir des possibilités infinies.

Quoi que fasse ce composant `DataLoader` ci-dessous, l'état ne peut générer qu'un ensemble limité de vues : « chargement », « chargé », ou « erreur ».

![Image](https://cdn-media-1.freecodecamp.org/images/1qn8vO-gCRq04nCZLSuPHRXBb7O8csOWr7bc)

Séparer l'état et les données peut réduire la confusion et nous permet de construire des applications basées sur des **machines à états finis**.

### 2. L'état est fini

Les développeurs en électronique savent depuis longtemps qu'une interface prévisible est une interface avec un nombre limité et contrôlé d'états. Sans un nombre contrôlé d'états, les systèmes deviennent difficiles à déboguer et impossibles à tester de manière exhaustive.

Dans une machine à états finis, les états sont explicitement définis. Les **transitions** sont l'ensemble des **événements** possibles que vous pouvez déclencher pour passer d'un état à un autre.

![Image](https://cdn-media-1.freecodecamp.org/images/GzMSdQyOzGH82UmnnebDYD4gjx56cInsCWww)

Par exemple, déclencher une transition avec l'événement « STOP » déplacera l'état vers « Arrêté ».

Dans React, nous pourrions définir un Walkman de base comme ayant au moins deux états : « Arrêté » ou « Lecture ».

![Image](https://cdn-media-1.freecodecamp.org/images/w9GtPNNc0Qkk7-BLfkNclkArMmbkLlEX0niP)

Consultez ce [CodeSandbox](https://codesandbox.io/s/2v55q3j5q0).

Dans une machine à états finis, le système est toujours dans l'une des configurations possibles. La vue n'a aucune possibilité d'être autre chose que « Lecture » ou « Arrêté ». Tester les deux peut nous donner confiance que le système fonctionne comme il devrait.

### 3. Gérer la complexité dans les machines à états

Regardons ce qui se passe lorsque nous commençons à ajouter deux nouveaux états à l'exemple de la machine à états : « Rembobinage » et « Avance rapide ».

![Image](https://cdn-media-1.freecodecamp.org/images/eRuPPcRGv7MOZrJ0Jch9H0HUErUksz8iwSQb)

Lorsque les états sont équivalents, ils sont trompeusement faciles à ajouter. Chaque état est comme son module qui peut être développé et testé en isolation. Mais attention, les transitions d'état ne doivent pas toujours être possibles.

Nous devons nous soucier des **transitions non contrôlées** entre les états.

Peut-être l'avez-vous remarqué. Nous avons introduit un bug ci-dessus. Prenez une minute et voyez si vous pouvez découvrir ce qui n'allait pas.

### 4. Protéger les transitions

Il semble que la cassette soit toute emmêlée car nous avons permis aux utilisateurs de sauter entre `rembobinage` et `avanceRapide` sans arrêter la cassette entre les deux.

En solution, nous pouvons ajouter des **gardes** à nos transitions d'état. Les gardes sont des conditions qui doivent être remplies pour qu'une transition se produise. Par exemple, nous pouvons nous assurer que les événements `AVANCERAPIDE`, `REBOBINER` et `LECTURE` ne peuvent être déclenchés que lorsque l'état est « Arrêté ».

![Image](https://cdn-media-1.freecodecamp.org/images/-KBLie7LReY9irWrdfGqQrgeDVQUmPTZ12um)

Les transitions d'état inattendues sont vouées à se produire à moins que nous ne repensions la façon dont nous planifions et concevons notre gestion d'état.

Lorsque nous ajoutons des états supplémentaires comme `éjecté`, nous devons réfléchir à quelles transitions d'état peuvent être autorisées et sous quelles conditions. Avec un Walkman, vous pouvez éjecter la cassette en appuyant sur stop lorsque la cassette est en mode arrêt. Pour ajouter cette fonctionnalité, nous devons ajouter encore plus de gardes et déterminer quelles transitions sont possibles.

![Image](https://cdn-media-1.freecodecamp.org/images/TNd2gmZ6olbEgYRznbzFd-ULawTF-Px6ceFG)

La probabilité de **combinations d'états non gérées** se multiplie à mesure que des états supplémentaires sont ajoutés. Ce n'est pas une solution évolutive. Chaque état supplémentaire entraîne une vérification de tous les gardes de transition.

On commence à avoir l'impression que c'est l'état qui vous gère.

Le problème de la gestion des gardes vient de la façon dont l'état est représenté : « Arrêté », « Lecture », « Rembobinage ».

La structure de données idéale pour l'état n'est pas une chaîne ou un objet.

Mais alors, qu'est-ce que c'est ?

### 5. L'état est un graphe

La structure de données idéale pour représenter l'état est souvent un graphe. Les **graphes d'état**, communément appelés **diagrammes d'état**, offrent un moyen intuitif de concevoir, visualiser et contrôler les transitions d'état à chaque nœud.

![Image](https://cdn-media-1.freecodecamp.org/images/OzKS67LoGJGc4l8Iux99Zp-8mKS9Z7OLEyES)

Ce n'est pas une nouvelle—les ingénieurs en électronique utilisent des diagrammes d'état pour décrire des systèmes complexes depuis des décennies.

Regardons un exemple sur le web. AWS Step Functions fournit une interface visuelle pour graphiquer le flux de travail d'une application. Chaque nœud contrôle une lambda—une fonction distante appelée dans le cloud—avec la sortie de chaque fonction déclenchant l'entrée de la suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/w7YWq3WEbXndpgpj8N0aihnKvIlsA26CVD8m)
_AWS Step Functions_

Dans l'exemple ci-dessus, il est clair de voir comment les actions d'un utilisateur passent par chaque étape, y compris les erreurs possibles et comment les gérer. L'ajout d'étapes supplémentaires n'entraîne pas d'augmentations exponentielles de la complexité.

Un ingénieur pourrait remarquer à quel point Step Functions ont en commun avec les **diagrammes de blocs PLC (Programmatic Logic Controller)**. Un designer pourrait remarquer à quel point ils ont en commun avec les diagrammes de **flux de travail**. La façon dont nous concevons l'état ne devrait-elle pas avoir plus en commun avec la façon dont nous planifions les applications ?

### 6. Échafaudage sur les graphes d'état

Les graphes d'état deviennent l'échafaudage de votre application.

Par exemple, un graphe d'état de notre Walkman pourrait produire une représentation plus visuellement compréhensible et accessible.

![Image](https://cdn-media-1.freecodecamp.org/images/2zAjA1aOXrHbugxcUeQN3WNJjz0W64g5AkNP)
_Graphe d'état du Walkman_

Sans entrer dans le code concernant les gardes, nous pouvons dire qu'il ne devrait y avoir aucune possibilité de sauter de « Rembobinage » à un autre état que « Arrêté ». Plutôt que de décrire toutes les transitions que votre interface ne devrait pas faire, vous exposez ce qu'elle peut faire. Le développement passe d'une approche de codage **bottom-up** défensive à une approche de conception **top-down**. Ce changement seul est 10x.

Les graphes d'état sont plus intuitifs, plus accessibles pour le débogage et plus capables d'absorber les changements de exigences. Aux côtés des machines à états, les changements dans chaque état peuvent être isolés de leurs états voisins. Sans parler du fait que beaucoup de la logique complexe de transition « garde » peut être englobée dans un format visuellement compréhensible.

**Malheureusement, les graphes d'état peuvent être une bombe à retardement.**

Les graphes densément connectés ne sont pas évolutifs. Considérez ce qui se passerait si nous ajoutions 4 états supplémentaires au graphe ci-dessus. La lisibilité diminue et la répétition augmente, avec des flèches emmêlées pointant dans toutes les directions en compétition pour l'espace. Cette **spaghettification** d'un graphe d'état est connue sous le nom d'**explosion d'état**.

Heureusement, il existe un moyen de réduire la complexité visuelle de la conception de graphes d'état complexes en utilisant une méthode formalisée de description des systèmes : explorons les **statecharts**.

### 7. Maîtriser les statecharts

J'ai d'abord appris les statecharts grâce à [la présentation de Luca Matteis sur la modélisation du comportement des applications Redux en utilisant des statecharts](https://medium.freecodecamp.org/how-to-model-the-behavior-of-redux-apps-using-statecharts-5e342aad8f66) lors de la rencontre React de Vancouver. Le lendemain au travail, j'ai abordé ce paradigme « nouveau » pour la gestion d'état, pour découvrir que beaucoup de mes collègues ingénieurs étaient déjà familiers avec le concept. Je travaille dans une [entreprise basée sur l'IoT](http://semios.com) aux côtés de nombreux développeurs matériel et embarqués. Nous recrutons ;)

Le concept de statechart remonte à 1987 lorsque le mathématicien David Harel a publié [un article](http://www.inf.ed.ac.uk/teaching/courses/seoc/2005_2006/resources/statecharts.pdf) sur la description visuelle de systèmes complexes, comme l'exemple ci-dessous d'une montre à quartz.

![Image](https://cdn-media-1.freecodecamp.org/images/f-quhmLt3aFmT5fJzios3yvARyEjubamkyV6)

Les statecharts sont à la fois intuitifs et faciles à maîtriser une fois que vous comprenez le langage.

![Image](https://cdn-media-1.freecodecamp.org/images/zSumkSO2cqGP-rYYmCoLmvfpErtW6GDCVxRz)

Les statecharts introduisent une variété de nouveaux types d'états :

* **état initial** — l'état de départ marqué par un point avec une flèche.
* **états imbriqués** — états qui ont accès aux transitions de leur parent.
* **états parallèles** — deux états non adjacents représentés par des lignes pointillées.
* **état historique** — un état qui **se souvient** et peut revenir à sa valeur précédente.

![Image](https://cdn-media-1.freecodecamp.org/images/oOZGxYZfej-hZFJR1ABU3NAF4YJAnW-EyyuY)

De plus, les statecharts peuvent englober comment et quand les **transitions** et **actions** sont déclenchées :

* **transition** — une fonction qui déclenche un changement d'état basé sur un **événement** nommé. « Arrêté » → transition('Play') → « Lecture »
* **garde** — une condition qui doit être remplie pour qu'une transition se produise. Par exemple, « play » ne peut pas être déclenché si aucune cassette n'est présente, ou si la cassette est à sa fin. « Arrêté » → transition('Play') **[hasTape]** → « Lecture ». Plusieurs transitions peuvent être possibles, selon un ordre.
* **action** — déclencheurs qui se produisent en fonction d'un changement d'état. Par exemple, déclencher une cassette pour commencer à jouer lorsque l'état entre en « lecture ». Les actions peuvent se produire `onEntry` et/ou `onExit`.

Réécrire l'exemple du Walkman en tant que statechart élimine la redondance trouvée dans le graphe d'état. Remarquez comment il n'y a plus besoin de répétition avec les événements « STOP ». Les statecharts sont évolutifs—il n'est pas difficile d'ajouter des états parallèles supplémentaires tels que « Enregistrement » et « Volume ».

![Image](https://cdn-media-1.freecodecamp.org/images/dG-3oXwGlHH8n-mGMvCh8oKUBtVUd7mRiXD0)

Les statecharts sont plus qu'un simple concept pour décrire visuellement les applications.

**Les statecharts peuvent générer les machines à états qui sous-tendent une application.**

Vous pouvez convertir des visuels en code, et vice versa. Visualisez la logique de votre application sous forme de graphique, ou dessinez-la.

### 8. Outils de statecharts

Les statecharts offrent un avenir prometteur pour concevoir véritablement des systèmes—et pas seulement sur papier. Bien que des outils existent pour d'autres langages de programmation, JavaScript commence tout juste à montrer un essor dans les outils de statecharts.

Les développeurs C & Java disposent d'outils pour coder avec et aux côtés des statecharts. Par exemple, [Yakindu Statechart Tools](https://www.itemis.com/en/yakindu/state-machine/) réunit les mondes de la conception visuelle et du code. J'ai récemment appris que Yakindu inclut également un [générateur de code TypeScript](https://blogs.itemis.com/en/typescript-code-generation-with-yakindu-statechart-tools).

![Image](https://cdn-media-1.freecodecamp.org/images/-zcZ55mMe5L0lysnKeFPXJlGaa7SPR2cIbqz)

Les mêmes outils deviennent enfin disponibles pour JavaScript également.

[Sketch Systems](http://sketch.systems/) fournit un moyen de concevoir des systèmes en markdown qui peuvent ensuite être utilisés pour prototyper en JavaScript. Bien que Sketch Systems ne prenne pas encore en charge les **actions** ou les **gardes**, je l'ai trouvé très utile pour prototyper et tester des statecharts.

![Image](https://cdn-media-1.freecodecamp.org/images/YUfyjSO1Fkv-eO2LH6Nf15i--zzzPnY9adkF)
_[https://bit.ly/2lZhqOB](https://bit.ly/2lZhqOB" rel="noopener" target="_blank" title=")_

Sketch Systems vous permet d'exporter vos graphiques vers [XState](https://github.com/davidkpiano/xstate), une bibliothèque JavaScript basée sur les statecharts avec son outil de visualisation et de prototypage d'états cliquables.

![Image](https://cdn-media-1.freecodecamp.org/images/CorF8tAeQ5g4qd3c4F1TkTflhcuUspsI6mi3)
_[https://bit.ly/2uJydt9](https://bit.ly/2uJydt9" rel="noopener" target="_blank" title=")_

Imaginez des outils plus avancés dans votre éditeur. Imaginez votre flux de travail alors que vous basculez entre la conception visuelle et le codage manuel de la logique de votre application. Cela vaut le travail que nous devrons fournir en tant que communauté pour faire avancer les outils, les bibliothèques et les plugins d'éditeur que nous voulons pour mieux supporter l'utilisation des statecharts.

### Conclusion

La complexité s'est glissée dans la communauté JavaScript. Je ne pense pas que nous étions prêts pour cela. J'admets qu'il m'a fallu beaucoup de temps pour devenir bon dans la **planification** des applications. Je dessinais un arbre de composants et une forme d'état. Je regardais les prototypes évoluer en production. Mais comment pourrais-je être bon dans la planification des applications sans un langage visuel formalisé pour concevoir des diagrammes d'état ?

Pendant longtemps, j'avouerai que j'ai abordé la gestion d'état plus comme un art mystifiant. Je ne savais pas qu'il y avait beaucoup à apprendre d'autres domaines de l'informatique avec une longue histoire de construction et de gestion de systèmes complexes. J'ai fini par comprendre qu'il y a de la valeur à regarder le passé, ainsi qu'à regarder de côté les domaines de l'ingénierie autour de nous.

Nous pouvons apprendre des ingénieurs qui ont pionné et développé des solutions vieilles de plusieurs décennies pour créer des systèmes complexes—mais prévisibles. Nous pouvons construire sur des outils et des bibliothèques en tant qu'écosystème pour soutenir la conception visuelle de la logique des applications. Et nous le ferons parce que JavaScript en a besoin.

L'avenir de la conception d'applications en JavaScript semble plus prometteur que jamais. Cet article a été très général et a probablement laissé plus de questions que de réponses. Dans la [**partie 2**](https://medium.freecodecamp.org/patterns-for-using-react-with-statechart-based-state-machines-33e6ab754605), j'aimerais examiner plus en détail les modèles d'utilisation des statecharts avec des composants.