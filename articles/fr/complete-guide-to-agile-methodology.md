---
title: Guide complet de la méthodologie Agile
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-27T19:25:00.000Z'
originalURL: https://freecodecamp.org/news/complete-guide-to-agile-methodology
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d69740569d1a4ca37a0.jpg
tags:
- name: agile development
  slug: agile-development
- name: toothbrush
  slug: toothbrush
seo_title: Guide complet de la méthodologie Agile
seo_desc: 'Story Points and Complexity Points

  In Scrum/Agile, the functionality of a product in development is explored by way
  of stories a user might tell about what they want from a product. A team uses Story
  Points when they estimate the amount of effort req...'
---

## **Points de Story et Points de Complexité**

Dans Scrum/Agile, la fonctionnalité d'un produit en développement est explorée par le biais de **stories** qu'un utilisateur pourrait raconter sur ce qu'il veut d'un produit. Une équipe utilise les **Points de Story** lorsqu'elle estime la quantité d'effort nécessaire pour livrer une story utilisateur.

Les caractéristiques notables des points de story sont qu'ils :

* représentent les contributions de toute l'équipe
* ne correspondent pas directement au temps que la tâche pourrait prendre
* sont une mesure approximative à des fins de planification - similaire aux ordres de grandeur
* sont attribués dans une séquence de type Fibonacci : 0, 1, 2, 3, 5, 8, 13, 20, 40, 100
* estiment la "taille" des stories _les unes par rapport aux autres_

Le concept de points de story peut être assez insaisissable si vous êtes nouveau dans les méthodes Agile. Vous trouverez de nombreuses sources en ligne discutant des points de story de différentes manières, et il peut être difficile d'avoir une idée claire de ce qu'ils sont et de la manière dont ils sont utilisés.

À mesure que vous apprenez les principes et la terminologie des pratiques comme Scrum, les raisons de certaines de ces propriétés deviendront apparentes. L'utilisation des points de story, en particulier dans les "cérémonies" telles que le planning poker, est beaucoup plus facile à comprendre en observant ou en participant qu'à travers une explication écrite !

### **Plus d'informations :**

* User Stories : [freeCodeCamp](https://guide.freecodecamp.org/agile/user-stories)

## **Développement Parallèle**

Le Développement Parallèle représente le processus de développement séparé en plusieurs branches, afin de fournir un produit polyvalent avec des versions stables et de nouvelles fonctionnalités. Dans un processus de développement logiciel plus commun et direct, vous n'avez qu'une seule branche avec des corrections de bugs et des améliorations, ainsi que de nouvelles fonctionnalités. Dans le développement parallèle, plusieurs branches peuvent coexister.

Généralement, le développement parallèle contient une branche principale, "master", qui est la plus stable et contient des corrections importantes pour le code existant. À partir de la branche principale, d'autres branches sont créées pour ajouter de nouveaux "chemins" au code existant. Ces branches fournissent de nouvelles fonctionnalités, mais n'incluent pas les corrections appliquées entre-temps à partir de la branche master. Les clients connaissent ces versions et disposent d'équipements spéciaux ou de machines de test pour pouvoir tester les nouvelles fonctionnalités. Lorsque les tests QA sont réussis, la branche latérale peut être fusionnée avec la branche principale pour introduire de nouvelles fonctionnalités dans la version de release.

## **Graphiques de Burndown et Burnup**

Les graphiques de burndown et burnup sont utilisés pour mesurer la progression d'un projet — généralement un sprint de développement sous la méthodologie Agile. Les deux graphiques représentent visuellement le travail par rapport au temps.

Les graphiques de burndown montrent combien de travail reste à faire par rapport au temps restant. L'axe Y représente le travail restant à faire — généralement en relation avec une estimation de temps attribuée à chaque tâche, par exemple les points de story — et l'axe X représente le temps restant. Deux lignes sont utilisées ; la première — "Ligne de Travail Restant Idéal" — représente un burndown idéal, où chaque jour une quantité de travail proportionnelle au temps total est accomplie, résultant en une ligne droite. La deuxième "Ligne de Travail Restant Réel" est utilisée pour tracer la progression réelle à mesure que les tâches passent par le développement jusqu'à un état terminé. Un exemple de graphique de burndown est montré ci-dessous.

![texte alternatif](https://upload.wikimedia.org/wikipedia/commons/8/8c/Burn_down_chart.png)

De nombreuses équipes Scrum utilisent des graphiques de burndown afin de voir comment elles avancent pendant le sprint. Avoir un burndown régulier et constant peut être un indicateur que les stories sont petites et gérables. Si une équipe remarque au milieu d'un sprint que la "Ligne de Travail Restant Réel" est au-dessus de la "Ligne de Travail Restant Idéal", elles peuvent faire des ajustements à la portée : des stories peuvent être retirées du sprint ou la portée des stories peut être réduite. Regarder le burndown pendant la rétrospective à la fin du sprint peut susciter des discussions intéressantes et entraîner des améliorations de processus.

Les graphiques de burnup sont très similaires, mais ils montrent le travail qui a été accompli par rapport à la quantité totale de travail et au temps restant. Trois lignes sont utilisées — une ligne idéale, une ligne de travail accompli, et une ligne de travail total. Dans ce graphique, la ligne de travail total doit être quelque peu stable en haut du graphique, et est une bonne représentation du changement de portée. La ligne de travail accompli doit monter régulièrement vers la ligne de travail total pour la durée du projet — sa trajectoire idéale est montrée par la ligne idéale. Un exemple est montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/ReleaseBurnup.png)

_Image courtesy of [Effective PMC](https://sites.google.com/a/effectivepmc.com/www/blog/agile/information-radiators/burn-up-chart?overridemobile=true)_

## **Design Patterns**

Un design pattern est une solution de conception courante à un problème de conception courant. Une collection de design patterns pour un domaine ou un champ d'application est appelée un langage de patterns. Notez qu'il existe également des patterns à d'autres niveaux : code, concurrency, architecture, interaction design...

En ingénierie logicielle, un design pattern est une solution générale réutilisable à un problème courant dans un contexte donné en conception logicielle. Ce n'est pas une conception finale qui peut être transformée directement en code source ou machine. C'est une description ou un modèle pour résoudre un problème qui peut être utilisé dans de nombreuses situations différentes. Les design patterns sont des meilleures pratiques formalisées que le programmeur peut utiliser pour résoudre des problèmes courants lors de la conception d'une application ou d'un système.

Les design patterns orientés objet montrent généralement des relations et des interactions entre classes ou objets, sans spécifier les classes ou objets d'application finaux impliqués. Les patterns qui impliquent un état mutable peuvent ne pas convenir aux langages de programmation fonctionnelle, certains patterns peuvent devenir inutiles dans les langages qui ont un support intégré pour résoudre le problème qu'ils tentent de résoudre, et les patterns orientés objet ne sont pas nécessairement adaptés aux langages non orientés objet.

Les design patterns peuvent être considérés comme une approche structurée de la programmation informatique intermédiaire entre les niveaux d'un paradigme de programmation et d'un algorithme concret.

Le livre qui a popularisé le domaine est celui du Gang of Four (GoF) **Design Patterns: Elements of Reusable Object-Oriented Software** (1994). Il présente une série (23) de patterns pour un langage OO conventionnel (C++) classés en trois types :

* **Création** (pour créer des objets) : abstract factory, builder, factory method, prototype, singleton.
* **Structurel** (pour composer des objets) : adapter, bridge, composite, decorator, facade, flyweight, proxy.
* **Comportemental** (pour communiquer entre objets) : chain of responsibility, command, interpreter, iterator, mediator, memento, observer, state, strategy, template method, visitor.

Les patterns peuvent être utilisés pour plusieurs objectifs (apprentissage, communication, amélioration de votre outil) mais dans l'agile, ils doivent être refactorisés à partir du code avec une dette technique et non simplement ajoutés au début (design/architecture émergent) car initialement vous n'avez pas assez de connaissances sur le (futur) système qui va évoluer. Notez que ce qui nécessite un pattern dans un langage ou un outil peut ne pas être nécessaire ou déjà faire partie d'un autre langage ou outil. Un framework est un ensemble de classes coopérantes qui constituent un design réutilisable pour un type spécifique de logiciel et sont généralement riches en patterns.

## **Tableaux de Tâches et Kanban**

Kanban est une excellente méthode à la fois pour les équipes effectuant du développement logiciel et pour les individus suivant leurs tâches personnelles.

Dérivé du terme japonais pour "panneau d'affichage" ou "panneau publicitaire" pour représenter un signal, le principe clé est de limiter votre travail en cours (WIP) à un nombre fini de tâches à un moment donné. La quantité qui peut être En Cours est déterminée par la capacité contrainte de l'équipe (ou de l'individu). Lorsqu'une tâche est terminée, c'est le signal pour vous de faire avancer une autre tâche à sa place.

Vos tâches Kanban sont affichées sur le Tableau de Tâches dans une série de colonnes qui montrent l'état des tâches. Sous sa forme la plus simple, trois colonnes sont utilisées

* À Faire
* En Cours
* Terminé

![Exemple de Tableau Kanban](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Simple-kanban-board-.jpg/600px-Simple-kanban-board-.jpg)

_Image courtesy of [Wikipedia](https://en.wikipedia.org/wiki/Kanban_board)_

Mais de nombreuses autres colonnes, ou états, peuvent être ajoutées. Une équipe logicielle peut également inclure En Attente de Test, Complet, ou Accepté, par exemple.

![Image](https://www.freecodecamp.org/news/content/images/2020/04/LeanKit-Program-Board_Drive-Agility-c-1000x547.jpg)
_Un exemple plus compliqué._

_Image courtesy of [leankit](https://leankit.com/learn/kanban/kanban-board-examples-for-development-and-operations/)_

## **Enfer de l'Intégration**

L'Enfer de l'Intégration est un terme argotique pour désigner le moment où tous les membres d'une équipe de développement passent par le processus de mise en œuvre de leur code à des moments aléatoires sans moyen d'incorporer les différents morceaux de code en une seule chaîne de code fluide. L'équipe de développement devra passer plusieurs heures ou jours à tester et à ajuster le code pour que tout fonctionne.

En pratique, plus les composants sont développés en isolation, plus les interfaces tendent à diverger de ce qui est attendu. Lorsque les composants sont enfin intégrés à la fin du projet, cela prendrait beaucoup plus de temps que prévu, conduisant souvent à des pressions de délais et à une intégration difficile. Ce travail d'intégration douloureux à la fin du projet est l'enfer éponyme.

L'Intégration Continue, l'idée qu'une équipe de développement devrait utiliser des outils spécifiques pour "intégrer continuellement" les parties du code sur lesquelles ils travaillent plusieurs fois par jour afin que les outils puissent assembler les différents "morceaux" de code pour une intégration beaucoup plus fluide qu'auparavant.

Les dépôts de code, comme Git (et son interface open source que nous connaissons et aimons tous, GitHub) permettent aux équipes de développement d'organiser leurs efforts afin que plus de temps puisse être consacré au codage et moins de temps à s'inquiéter si les différentes parties du code s'intégreront toutes.

[L'Intégration Continue](https://guide.freecodecamp.org/agile/continuous-integration/) est l'antidote Agile à ce problème. L'intégration est toujours douloureuse, mais la faire au moins quotidiennement empêche les interfaces de diverger trop.

## **User Stories**

Selon [Mountain Goat Software](https://www.mountaingoatsoftware.com/agile/user-stories), les user stories sont :

> ...une partie d'une approche agile qui aide à déplacer le focus de l'écriture sur les exigences à la discussion sur celles-ci. Toutes les user stories agiles incluent une ou deux phrases écrites et, plus important encore, une série de conversations sur la fonctionnalité souhaitée.

Les user stories sont généralement écrites en utilisant le modèle suivant :

**En tant que [type d'utilisateur], je veux [un objectif] afin que [une raison ou un besoin]**

Les user stories doivent être écrites en termes non techniques du point de vue de l'utilisateur. La story doit souligner le besoin de l'utilisateur, et non le comment. Il ne doit y avoir aucune solution fournie dans la user story.

Une erreur courante commise lors de l'écriture de user stories est d'écrire du point de vue du développeur ou de la solution. Assurez-vous de préciser l'objectif et le besoin, et les exigences fonctionnelles viendront plus tard.

#### **Dimensionnement d'une User Story : Épics et Stories Plus Petites**

Un epic est comme le titre ou le placeholder pour les user stories. Les épics servent généralement de grands traits larges et sont ensuite décomposés en plusieurs user stories.

En commençant par un epic, vous pouvez planifier la fonctionnalité du produit sans vous engager sur des détails exacts. Prendre cette approche vous donne le temps d'en apprendre davantage sur vos utilisateurs et sur la manière de répondre à leurs besoins.

Lors de la réflexion sur les stories possibles, il est également important de considérer les "mis-user cases" et les "unhappy path" stories. Comment les exceptions seront-elles gérées par le système ? Quel type de messagerie fournirez-vous à l'utilisateur ? Comment un utilisateur malveillant abuserait-il de cette fonction de l'application ? Ces mal-stories peuvent éviter des retravaux et devenir des cas de test utiles en QA.

## **Planning Poker**

### **Introduction**

Le planning poker est une technique d'estimation et de planification dans le modèle de développement Agile. Il est utilisé pour estimer l'effort de développement requis pour une [user story](https://en.wikipedia.org/wiki/User_story) ou une fonctionnalité.

### **Processus**

Le planning poker est effectué pour une user story à la fois.

Chaque estimateur tient un jeu de cartes de poker identique composé de cartes avec diverses valeurs. Les valeurs des cartes sont généralement de la séquence de Fibonacci. L'unité utilisée pour les valeurs peut être le nombre de jours, les points de story, ou toute autre unité d'estimation convenue par l'équipe.

Le propriétaire du produit (PO) ou la partie prenante explique la story qui doit être estimée.

L'équipe discute de la story, posant toutes les questions de clarification qu'ils pourraient avoir. Cela aide l'équipe à mieux comprendre _ce que_ le PO veut.

À la fin de la discussion, chaque personne sélectionne d'abord une carte (représentant leur estimation pour la story) sans la montrer aux autres. Ensuite, ils révèlent leurs cartes en même temps.

Si toutes les cartes ont la même valeur, la valeur devient l'estimation pour la story. S'il y a des différences, l'équipe discute des raisons des valeurs qu'ils ont choisies. Il est de grande valeur que les membres de l'équipe qui ont donné les estimations les plus basses et les plus hautes fournissent des justifications pour leurs estimations.

Après cette discussion, le processus de choix d'une carte en privé puis de sa révélation en même temps est répété. Cela est fait jusqu'à ce qu'il y ait un consensus sur l'estimation.

Parce que le planning poker est un outil pour modérer une estimation _conjointe_ d'experts, il conduit à une meilleure compréhension commune et peut-être même à un affinement de la demande de fonctionnalité. Il est de grande valeur même lorsque l'équipe fonctionne en mode No-Estimates.

Un modérateur devrait essayer d'éviter le biais de confirmation.

Choses à mentionner :

* Les estimations ne sont pas comparables entre les équipes, car chaque équipe a sa propre échelle.
* Les estimations doivent inclure tout ce qui doit être fait pour qu'un travail soit terminé : conception, codage, test, communication, revues de code (+ tous les risques possibles)
* La valeur de l'utilisation du planning poker réside dans les discussions résultantes, car elles révèlent différentes vues sur une possible implémentation

## **Behavior Driven Development**

Le Behavior Driven Development (BDD) est un processus de développement logiciel qui a émergé du [Test Driven Development (TDD)](https://www.freecodecamp.org/news/an-introduction-to-test-driven-development-c4de6dce5c/). Le Behavior Driven Development combine les techniques et principes généraux du TDD avec des idées de la conception pilotée par le domaine et de l'analyse et la conception orientées objet pour fournir aux équipes de développement et de gestion logicielle des outils partagés et un processus partagé pour collaborer sur le développement logiciel. C'est une méthodologie de développement logiciel dans laquelle une application est spécifiée et conçue en décrivant comment son comportement devrait apparaître à un observateur extérieur.

Bien que le BDD soit principalement une idée sur la manière dont le développement logiciel devrait être géré par les intérêts commerciaux et l'insight technique, la pratique du BDD suppose l'utilisation d'outils logiciels spécialisés pour soutenir le processus de développement.

Bien que ces outils soient souvent développés spécifiquement pour une utilisation dans les projets BDD, ils peuvent être vus comme des formes spécialisées de l'outillage qui soutient le développement piloté par les tests. Les outils servent à ajouter de l'automatisation au langage ubiquitaire qui est un thème central du BDD.

Le BDD se concentre sur :

* Par où commencer dans le processus
* Ce qu'il faut tester et ce qu'il ne faut pas tester
* Combien tester en une seule fois
* Comment nommer les tests
* Comment comprendre pourquoi un test échoue

Au cœur du BDD se trouve une révision de l'approche des tests unitaires et des tests d'acceptation qui apparaissent naturellement avec ces problèmes. Par exemple, le BDD suggère que les noms des tests unitaires soient des phrases complètes commençant par un verbe conditionnel ("should" en anglais par exemple) et doivent être écrits dans l'ordre de la valeur commerciale. Les tests d'acceptation doivent être écrits en utilisant le cadre agile standard d'une user story : "En tant que _rôle_ je veux _fonctionnalité_ afin que _bénéfice_". Les critères d'acceptation doivent être écrits en termes de scénarios et implémentés en tant que classes : Étant donné _contexte initial_, lorsque _événement se produit_, alors _assurer certains résultats_.

Exemple

```text
Story : Les retours vont en stock

En tant que propriétaire de magasin
Afin de garder une trace du stock
Je veux ajouter des articles au stock lorsqu'ils sont retournés.

Scénario 1 : Les articles remboursés doivent être retournés en stock
Étant donné qu'un client a précédemment acheté un pull noir chez moi
Et j'ai trois pulls noirs en stock.
Lorsque qu'il retourne le pull noir pour un remboursement
Alors je devrais avoir quatre pulls noirs en stock.

Scénario 2 : Les articles remplacés doivent être retournés en stock
Étant donné qu'un client a précédemment acheté un vêtement bleu chez moi
Et j'ai deux vêtements bleus en stock
Et trois vêtements noirs en stock.
Lorsque qu'il retourne le vêtement bleu pour un remplacement en noir
Alors je devrais avoir trois vêtements bleus en stock
Et deux vêtements noirs en stock.
```

Avec cela viennent quelques avantages :

1. Tous les travaux de développement peuvent être directement liés aux objectifs commerciaux.
2. Le développement logiciel répond aux besoins des utilisateurs. Des utilisateurs satisfaits = bonne entreprise.
3. Priorisation efficace - les fonctionnalités critiques pour l'entreprise sont livrées en premier.
4. Toutes les parties ont une compréhension commune du projet et peuvent être impliquées dans la communication.
5. Un langage commun garantit que tout le monde (technique ou non) a une visibilité complète sur la progression du projet.
6. Conception logicielle résultante qui correspond aux besoins existants et soutient les besoins commerciaux à venir.
7. Code de meilleure qualité réduisant les coûts de maintenance et minimisant les risques du projet.

## **Scrum**

Scrum est l'une des méthodologies sous l'égide Agile. Le nom est dérivé d'une méthode de reprise de jeu dans le sport du rugby, dans laquelle toute l'équipe avance ensemble pour gagner du terrain. De même, un scrum en Agile implique toutes les parties de l'équipe travaillant sur le même ensemble d'objectifs. Dans la méthode scrum, une liste priorisée de tâches est présentée à l'équipe, et au cours d'un "sprint" (généralement deux semaines), ces tâches sont accomplies, dans l'ordre, par l'équipe. Cela garantit que les tâches ou livrables de la plus haute priorité sont accomplis avant que le temps ou les fonds ne s'épuisent.

### **Composants d'un Scrum**

Scrum est l'une des méthodologies sous l'égide Agile. Il provient de "scrummage" qui est un terme utilisé en rugby pour désigner les joueurs se regroupant pour obtenir la possession du ballon. La pratique tourne autour de

* Un ensemble de rôles (équipe de livraison, propriétaire du produit et scrum master)
* Cérémonies (planification de sprint, daily standup, revue de sprint, rétrospective de sprint et toilettage du backlog)
* Artéfacts (backlog de produit, backlog de sprint, incrément de produit, et radiateurs d'informations et rapports).
* L'objectif principal est de maintenir l'équipe alignée sur la progression du projet pour faciliter l'itération rapide.
* De nombreuses organisations ont opté pour Scrum, car contrairement au modèle Waterfall, il garantit un livrable à la fin de chaque Sprint.

### **Artéfacts**

* Sprint : Il s'agit de la durée, généralement en semaines, pendant laquelle une équipe travaille pour atteindre ou créer un livrable. Un livrable peut être défini comme un morceau de code ou un fragment du Produit Final que l'équipe souhaite atteindre. Scrum conseille de maintenir la durée d'un Sprint entre 2 et 4 semaines.
* Product Backlog : Il s'agit de la liste des tâches qu'une équipe doit terminer dans le Sprint actuel. Il est décidé par le Product Owner, en accord avec la Direction ainsi que l'Équipe de Livraison.

### **Rôles**

* Product Owner (PO) : La SEULE personne responsable devant la Direction. Le PO décide de ce qui entre ou sort du Product Backlog.
* Équipe de Livraison : Ils sont tenus de travailler conformément aux tâches fixées par leur PO dans le backlog de produit et de livrer le livrable requis à la fin du sprint.
* Scrum Masters : - Les Scrum Masters doivent strictement adhérer au Scrum Guide et faire comprendre à l'équipe la nécessité d'adhérer au Scrum guide lorsqu'ils suivent Scrum. C'est le travail d'un Scrum Master de s'assurer que toutes les cérémonies Scrum sont menées à temps et participées par toutes les personnes requises selon le scrum guide. Le SM doit s'assurer que le Daily Scrum est mené régulièrement et activement participé par l'équipe.

## **Daily Stand-Up et Daily Scrum**

Le Daily Stand-Up (DSU) ou la réunion Daily Scrum est l'une des parties intégrales de la méthodologie scrum.

Comme le nom l'indique, vous tenez la réunion quotidiennement, à la même heure et, pour une équipe co-localisée, au même endroit. La réunion doit être brève, terminée en moins de 15 minutes.

Seuls les membres de l'équipe de développement sont tenus d'assister au Daily Stand-up. Typiquement, le Scrum Master et les Product Owners assisteront également, mais ils ne sont pas tenus de le faire.

L'ordre du jour standard pour chaque personne est :

* Ce que vous avez fait depuis le dernier DSU
* Ce que vous allez faire après ce DSU
* Quels sont les principaux obstacles qui stoppent votre progression, et où avez-vous besoin d'aide

Les membres de l'équipe doivent écouter attentivement les contributions des autres et tenter d'identifier les domaines où ils peuvent aider à la progression des autres. La réunion stand-up fera également émerger des sujets de discussion plus longs qui doivent avoir lieu entre différents membres de l'équipe. Ces discussions plus longues qui émergent doivent alors être interrompues et prises en dehors du stand-up, impliquant uniquement les participants concernés, et non toute l'équipe.

### **Exemple de Réunion Stand-up**

[https://www.youtube.com/watch?v=_3VIC8u1UV8](https://www.youtube.com/watch?v=_3VIC8u1UV8)

## **Pirate Metrics**

Dave McClure a identifié cinq catégories de métriques de haut niveau critiques pour le succès d'une startup : Acquisition, Activation, Rétention, Revenus, Référencement.

Il a inventé le terme "Pirate Metrics" à partir de l'acronyme de ces cinq catégories de métriques (AARRR).

Dans leur livre Lean Analytics, Croll et Yoskovitz interprètent ces métriques visuellement comme un entonnoir :

![Lean Analytics Figure 5.1](https://github.com/yunChigewan/storage/blob/master/figure_5_1.jpg?raw=true)

Lean Analytics, 2013

Et avec des explications plus pointues sous forme de tableau :

![Lean Analytics Table 5.1](https://github.com/yunChigewan/storage/blob/master/table_5_1.jpg?raw=true)

Lean Analytics, 2013

## **Exigences Non Fonctionnelles**

Une exigence non fonctionnelle (NFR) est une exigence qui spécifie des critères qui peuvent être utilisés pour juger le fonctionnement d'un système, plutôt que des comportements spécifiques (une exigence fonctionnelle). Les exigences non fonctionnelles sont souvent appelées "attributs de qualité", "contraintes" ou "exigences non comportementales".

De manière informelle, celles-ci sont parfois appelées les "utilités", à partir d'attributs comme la stabilité et la portabilité. Les NFR peuvent être divisés en deux catégories principales :

* **Qualités d'exécution**, telles que la sécurité, la sûreté et l'utilisabilité, qui sont observables pendant le fonctionnement (au moment de l'exécution).
* **Qualités d'évolution**, telles que la testabilité, la maintenabilité, l'extensibilité et la scalabilité, qui sont incarnées dans la structure statique du système

Généralement, vous pouvez affiner une exigence non fonctionnelle en un ensemble d'exigences fonctionnelles comme moyen de détailler et de permettre (partiellement) des tests et une validation.

### **Exemples :**

* L'imprimante doit imprimer 5 secondes après que le bouton est pressé
* Le code doit être écrit en Java
* L'UI doit être facilement navigable

## **Planification Basée sur les Fonctionnalités**

La **Planification Basée sur les Fonctionnalités** est une méthodologie de planification qui peut être utilisée pour décider quand publier un logiciel en fonction des fonctionnalités qui seront livrées aux clients, plutôt qu'une publication basée sur une date limite arbitraire.

Dans cette méthode de planification de publication, les équipes décident quelles fonctionnalités doivent être priorisées. En fonction de la portée de ces fonctionnalités, l'équipe peut ensuite prédire quand la prochaine publication peut être déployée.

## **Managers Fonctionnels**

Un manager fonctionnel est une personne qui a une autorité de gestion sur un groupe de personnes. Cette autorité provient de la position formelle de cette personne dans l'organisation (par exemple, directeur du département, manager du département qualité, manager de l'équipe de développement). Le rôle des managers fonctionnels est différent de celui des chefs de projet ou des ScrumMasters et n'est pas basé sur un projet.
Dans les organisations plus agiles, différents modèles existent. Les managers fonctionnels sont souvent responsables du développement des personnes dans leurs groupes, de la sécurisation des budgets et du temps pour les personnes. Cependant, il existe également certains modèles d'entreprises Agile où les fonctions habituellement attribuées aux managers fonctionnels sont distribuées à d'autres rôles au sein de l'organisation (par exemple, le modèle Spotify avec Tribes, Guilds, Chapters, Squads).

Dans le monde traditionnel du travail, les entreprises organisent les personnes dans une hiérarchie. Les personnes ayant des rôles de travail similaires sont regroupées dans des domaines fonctionnels et dirigées par un manager fonctionnel. Le manager fonctionnel est généralement responsable de la guidance et du bien-être des employés qui lui rendent directement compte.

Les équipes de projet agiles travailleront souvent avec des managers fonctionnels qui contrôlent les ressources dont l'équipe a besoin pour accomplir le travail. Un exemple serait de travailler avec un manager fonctionnel en approvisionnement pour assigner une personne à travailler avec l'équipe pour obtenir des licences logicielles.

## **Build Measure Learn**

La boucle Build-Measure-Learn est une méthode utilisée pour construire le bon produit. Inventée dans le livre "Lean Startup" par Eric Reis, la boucle permet des expérimentations rapides, dans le seul but d'atteindre l'adéquation au marché. En d'autres termes, c'est un système puissant pour valider les hypothèses concernant un produit que vous vous proposez de livrer. En décomposant la boucle, elle se compose des parties suivantes :

![boucle build-measure-learn](https://steveblank.files.wordpress.com/2015/05/ideas-build-code-measure.jpg)

### **Idée**

Chaque boucle commence par une idée qui fournira une valeur commerciale à certains utilisateurs. Une telle idée doit consister en une vision pour un produit - qui vous dirigera sur ce qu'il faut construire, et une métrique qui indiquera si vos hypothèses sur la valeur commerciale étaient correctes.

### **Build**

Pour valider votre idée, vous vous lancez dans la construction d'un Produit Minimum Viable (MVP), combiné avec des métriques prédéfinies (une est préférée), dont le but est de valider votre théorie, et de vous aider à décider si vous devez préserver ou pivoter.

### **Measure**

Cette étape est axée sur la collecte de données et de métriques à partir du MVP.

### **Learn**

Ensuite, en utilisant les données collectées, une décision doit être prise, que votre produit soit utilisé par les utilisateurs et que vous devez donc préserver, ou que les utilisateurs ne soient pas intéressés par le produit, et que vous devez donc pivoter. La phase d'apprentissage se termine donc par une idée (soit comment développer le produit, soit comment pivoter par rapport au produit original), applicable pour la prochaine boucle Build Measure Learn.

## **Réunion de Planification de Sprint**

La Planification de Sprint est facilitée par le Scrum Master de l'équipe et se compose de l'Équipe Scrum : Équipe de Développement, Product Owner (PO) et Scrum Master (SM). Elle vise à planifier un sous-ensemble d'éléments du Backlog de Produit dans un Backlog de Sprint. Le Sprint Scrum est normalement lancé après la réunion de Planification de Sprint.

### **Partie Principale**

Il est de grande valeur pour l'équipe de diviser la réunion en deux parties en posant ces deux questions :

* **Quoi** l'équipe devrait-elle planifier pour le prochain Sprint ?
* **Comment** l'équipe devrait-elle (grossièrement) aborder les éléments planifiés ?

#### **Quoi**

Dans la phase Quoi, l'équipe commence par le haut du Backlog de Produit ordonné. L'équipe estime au moins implicitement les éléments en prévisionnant ce qu'ils pourraient prendre dans le Backlog de Sprint. Si nécessaire, ils pourraient demander/discuter des éléments avec le PO, qui doit être présent pour cette réunion.

#### **Comment**

Dans la phase Comment, l'équipe discute brièvement de chaque élément du Backlog de Sprint sélectionné en se concentrant sur la manière dont ils vont l'aborder. Le SM aide l'équipe à ne pas approfondir la discussion et les détails d'implémentation. Il est très probable et bon que davantage de questions soient posées au PO ou que des affînements des éléments, ou du backlog, soient effectués par l'équipe.

### **Objectif de Sprint / Clôture**

L'équipe devrait proposer un Objectif de Sprint partagé pour le Sprint afin de maintenir le focus dans la boîte de temps du Sprint. À la fin de la Planification de Sprint, l'équipe prévoit qu'elle peut atteindre l'Objectif de Sprint et compléter très probablement tous les éléments du Backlog de Sprint. Le SM devrait empêcher l'équipe de surestimer en fournissant des insights ou des statistiques utiles.

## **Développement Logiciel Lean**

### **Introduction**

Le Développement Logiciel Lean est le processus de construction de logiciels en se concentrant sur l'utilisation de techniques qui minimisent le travail supplémentaire et l'effort gaspillé. Ces techniques sont empruntées au mouvement de fabrication Lean et appliquées au contexte du développement logiciel.

### **Concepts Clés**

Il existe sept principes au sein de la méthodologie qui incluent :

1. Éliminer le gaspillage
2. Amplifier l'apprentissage
3. Décider le plus tard possible
4. Livrer le plus rapidement possible
5. Autonomiser l'équipe
6. Construire l'intégrité
7. Voir le tout

### **Métaphores**

L'acte de programmation est considéré comme une chaîne de montage, où chaque fonctionnalité ou correction de bug est appelée une "demande de changement". Cette chaîne de montage de "demandes de changement" peut alors être considérée comme un "flux de valeur" avec pour objectif de minimiser le temps que chaque "demande de changement" passe sur la ligne avant d'être livrée.

Le logiciel qui n'est pas encore livré est considéré comme un "stock" puisqu'il n'a pas encore fourni de valeur à l'entreprise ou au client. Cela inclut tout logiciel partiellement complet. Par conséquent, pour maximiser le débit, il est important de livrer de nombreuses petites pièces de logiciel complètes et fonctionnelles.

Afin de minimiser le "stock", il est important de céder le contrôle aux "travailleurs" qui seraient les développeurs de logiciels, car ils seraient les mieux équipés pour créer des processus automatisés afin de "sécuriser contre les erreurs" les différentes parties de la chaîne de montage.

### **Références**

La source originale de la documentation écrite sur les techniques Lean est le livre Lean Software Development, An Agile Toolkit de Mary et Tom Poppendieck.

D'autres livres des auteurs incluent :

* Implementing Lean Software Development: From Concept to Cash par Mary Poppendieck
* Leading Lean Software Development: Results Are not the Point par Mary Poppendieck

## **Collocation Vs Distribué**

* Co-localisé fait référence à une équipe qui travaille ensemble ; même bureau. Idéalement, tout le monde travaille ensemble dans des bureaux adjacents ou un espace de travail ouvert.
* Les membres de l'équipe distribuée sont dispersés géographiquement ; différents bâtiments, villes, ou même pays. En cas d'équipe distribuée, l'infrastructure doit faciliter les processus afin de résoudre les différences de fuseaux horaires et de distance entre les membres de l'équipe, offrant ainsi un moyen efficace de travailler ensemble.

## **Intégration Continue**

À sa base, l'intégration continue (CI) est une méthodologie de développement agile dans laquelle les développeurs fusionnent régulièrement leur code directement dans la source principale, généralement une branche `master` distante. Afin de s'assurer qu'aucun changement cassant n'est introduit, une suite de tests complète est exécutée sur chaque build potentiel pour tester la régression du nouveau code, c'est-à-dire tester que le nouveau code ne casse pas les fonctionnalités existantes et fonctionnelles.

Cette approche nécessite une bonne couverture de tests de la base de code, ce qui signifie qu'une majorité, sinon la totalité, du code a des tests qui garantissent que ses fonctionnalités sont pleinement fonctionnelles. Idéalement, l'intégration continue serait pratiquée conjointement avec le développement piloté par les tests (TDD) complet.

### **Étapes Principales**

Les étapes de base suivantes sont nécessaires pour faire l'approche la plus standard actuelle de l'intégration continue.

1. Maintenir un dépôt central et une branche `master` active.

Il doit y avoir un dépôt de code pour que tout le monde puisse fusionner et tirer les changements. Cela peut être sur Github ou sur l'un des nombreux services de stockage de code.

1. Automatiser la construction.

En utilisant des scripts NPM ou des outils de construction plus complexes comme Yarn, Grunt, Webpack, ou [Gulp](https://guide.freecodecamp.org/developer-tools/gulp), automatiser la construction afin qu'une seule commande puisse construire une version entièrement fonctionnelle du produit, prête à être déployée dans un environnement de production. Mieux encore, inclure le déploiement comme partie de la construction automatisée !

1. Faire en sorte que la construction exécute tous les tests.

Afin de vérifier que rien dans le nouveau code ne casse la fonctionnalité existante, la suite de tests complète doit être exécutée et la construction doit échouer si l'un des tests échoue.

1. Tout le monde doit fusionner les changements dans `master` chaque jour.
2. Chaque fusion dans `master` doit être construite et entièrement testée.

### **Meilleures Pratiques**

Il existe d'autres meilleures pratiques qui tirent le meilleur parti de ce que la CI a à offrir et des défis qu'elle présente, telles que :

1. Garder la construction rapide, afin que beaucoup de temps de développeur ne soit pas gaspillé en attendant une construction.
2. Tester la construction dans un clone complet de l'environnement de production.

Si vous avez, par exemple, une application déployée sur quelque chose comme Heroku ou Digital Ocean, avez un déploiement de test séparé là où vous pouvez déployer des constructions de test, pour vous assurer qu'elles fonctionnent non seulement dans les tests mais dans un environnement de production réel. Cet environnement de test doit être fonctionnellement identique à l'environnement de production réel, afin de garantir que le test est précis.

1. Faciliter la mise à jour.

Les codeurs doivent régulièrement tirer de la branche `master` pour continuer à intégrer leur code avec les changements de leur équipe. Le dépôt doit également être mis à la disposition des parties prenantes comme les chefs de produit, les dirigeants de l'entreprise, ou parfois des clients clés, afin que tout le monde puisse facilement voir les progrès.

1. Conserver des enregistrements des constructions, afin que tout le monde puisse voir les résultats de toute construction donnée, qu'elle ait réussi ou échoué, et qui ou quoi a introduit de nouveaux changements.
2. Automatiser le déploiement.

Gardez votre application entièrement à jour avec tout nouveau changement en automatisant le déploiement dans l'environnement de production comme étape finale du processus de construction, une fois que tous les tests ont réussi et que le déploiement de test dans le clone de l'environnement de production a réussi.

### **Services CI**

De nombreux services existent pour gérer le processus d'intégration continue pour vous, ce qui peut faciliter l'établissement d'un pipeline CI solide, ou d'un processus de construction. Lors de l'évaluation de ceux-ci, prenez en compte des facteurs comme le budget, la vitesse de construction, et le type de projet sur lequel vous travaillez. Certains services, comme [Travis CI](https://travis-ci.org/), offrent des services gratuits pour les projets open-source, ce qui peut en faire un choix facile pour des projets comme celui-ci, mais ils peuvent avoir des constructions plus lentes que d'autres services, comme [Circle CI](https://circleci.com/) ou [Codeship](https://codeship.com/), pour n'en nommer que quelques-uns.

## **Critères d'Acceptation**

La User Story, en tant qu'élément de votre backlog, est un placeholder pour une conversation. Dans cette conversation, le Product Owner et l'Équipe de Livraison parviennent à une compréhension de l'issue souhaitée.

Les Critères d'Acceptation indiquent à l'Équipe de Livraison comment le code doit se comporter. Évitez d'écrire le **"Comment"** de la User Story ; restez sur le **"Quoi"**. Si l'équipe suit le Test Driven Development (TDD), cela peut fournir le cadre pour les tests automatisés. Les Critères d'Acceptation seront les débuts du plan de test pour l'équipe QA.

Plus important encore, si la story ne répond pas à chacun des Critères d'Acceptation, alors le Product Owner ne devrait pas accepter la story à la fin de l'itération.

Les critères d'acceptation peuvent être considérés comme un instrument pour protéger l'Équipe de Livraison. Lorsque l'Équipe de Livraison s'engage sur un ensemble fixe de stories lors de la planification du Sprint, elle s'engage également sur un ensemble fixe de critères d'acceptation. Cela aide à éviter le glissement de portée.

Considérez la situation suivante : lors de l'acceptation de la user story, le Product Owner suggère d'ajouter quelque chose qui n'était pas dans la portée de la User story. Dans ce cas, l'Équipe de Livraison est en position de rejeter cette demande (aussi petite soit-elle) et de demander au Product Owner de créer une nouvelle User story qui pourra être prise en charge dans un autre Sprint.

## **Code Smells**

Un Code Smell en programmation informatique est une indication de surface qu'il pourrait y avoir un problème concernant votre système et la qualité de votre code. Ce problème pourrait nécessiter un refactoring pour être corrigé.

Il est important de comprendre que le code qui sent mauvais fonctionne, mais n'est pas de bonne qualité.

#### **Exemples**

1. Code dupliqué - Blocs de code qui ont été répliqués dans la base de code. Cela peut indiquer que vous devez généraliser le code dans une fonction et l'appeler à deux endroits, ou il peut être que la manière dont le code fonctionne à un endroit est complètement sans rapport avec la manière dont il fonctionne à un autre endroit, malgré avoir été copié.
2. Grandes classes - Classes ayant trop de lignes de code. Cela peut indiquer que la classe essaie de faire trop de choses, et doit être divisée en classes plus petites.

## Plus d'informations sur le Développement Agile :

* [Comment s'assurer que votre processus de développement est vraiment Agile](https://www.freecodecamp.org/news/signs-that-your-development-process-is-agile-only-on-paper-and-how-to-fix-it-f6c05b24337f/)
* [Comment corriger la dette technique](https://www.freecodecamp.org/news/give-the-gift-of-a-tech-debt-sprint-this-agile-holiday-season/)
* [Agile signifie-t-il vraiment ce que vous pensez ?](https://www.freecodecamp.org/news/you-say-your-team-is-agile-but-that-word-may-not-mean-what-you-think-6dd26eaf9b21/)