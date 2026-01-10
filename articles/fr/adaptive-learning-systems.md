---
title: Comment construire un système d'apprentissage adaptatif
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-22T20:51:53.000Z'
originalURL: https://freecodecamp.org/news/adaptive-learning-systems
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/adaptive-1.jpg
tags:
- name: Adaptive Learning
  slug: adaptive-learning
- name: algorithms
  slug: algorithms
- name: education
  slug: education
seo_title: Comment construire un système d'apprentissage adaptatif
seo_desc: 'By Kevin Heis

  Have you ever started a course, but thought it was too slow? Or too difficult? Wish
  you could make it go faster? Felt like you didn''t get enough practice to master
  the content? Adaptive learning systems seek to address these challenges....'
---

Par Kevin Heis

Avez-vous déjà commencé un cours, mais pensé qu'il était trop lent ? Ou trop difficile ? Souhaité pouvoir l'accélérer ? Avez-vous eu l'impression de ne pas avoir assez de pratique pour maîtriser le contenu ? Les systèmes d'apprentissage adaptatif cherchent à répondre à ces défis.

Dans cet article, je vais expliquer ce que sont les systèmes d'apprentissage adaptatif. Je couvre quelques notions de base sur pourquoi les systèmes d'apprentissage adaptatif ont la structure qu'ils ont. Je vais également présenter quelques systèmes d'apprentissage adaptatif. Ensuite, je parlerai des quatre éléments d'un système d'apprentissage adaptatif, et comment vous pouvez en architecturer un vous-même. Nous terminerons par une évaluation des avantages et des inconvénients de l'apprentissage adaptatif.

## Qu'est-ce qu'un système d'apprentissage adaptatif ?

Un système d'apprentissage adaptatif est un logiciel où des algorithmes optimisent le contenu pour s'adapter aux objectifs et à l'état actuel des connaissances de l'apprenant.

Dans un cours d'e-learning traditionnel, vous suivez linéairement le chemin créé par un instructeur. Vous regardez des vidéos, lisez des articles, passez des quiz et pratiquez des modules interactifs dans un ordre prédéterminé. Un système d'apprentissage adaptatif contiendra les mêmes types de matériaux. Mais l'ordre changera pour chaque apprenant. Le système décide quel contenu montrer à l'apprenant en fonction de deux choses :

* Si l'objectif de l'apprenant ne concerne qu'un sous-ensemble du contenu, le système peut limiter le contenu.
* Les connaissances préalables entrent également en jeu. Si le système détermine que le chemin actuel est trop facile, le système peut accélérer vers un matériel plus difficile. Si le système découvre que le chemin actuel est trop difficile, le système peut... intervenir et réviser le contenu préalable, réduire le défi ou ralentir le rythme.

Certains sujets connexes incluent les tuteurs intelligents, les tests adaptatifs, la psychométrie, l'apprentissage personnalisé et l'enseignement intelligent. Beaucoup de ces sujets partagent des algorithmes et des structures avec les systèmes d'apprentissage adaptatif.

## La connaissance est un graphe : neurosciences

Je vais commencer par un peu de contexte. Cela créera un cadre pour expliquer pourquoi les systèmes d'apprentissage adaptatif ont les quatre éléments ci-dessous. Le point ici est que la connaissance est un graphe.

Le cerveau humain compte 86 milliards de neurones. Chaque neurone a des dendrites, un soma et un axone.

![Image](https://upload.wikimedia.org/wikipedia/commons/thumb/1/10/Blausen_0657_MultipolarNeuron.png/1200px-Blausen_0657_MultipolarNeuron.png)

* Les dendrites sont l'entrée. Les extrémités des dendrites reçoivent des neurotransmetteurs de la synapse. La synapse est un espace entre deux neurones.
* Le soma est le débit. Le soma, qui contient le noyau cellulaire, achemine l'entrée des dendrites.
* L'axone est la sortie. L'axone transmet un potentiel d'action, un signal électrique, aux terminaux de l'axone. Une gaine de myéline couvre l'axone pour protéger le signal. Les terminaux de l'axone libèrent des neurotransmetteurs dans la synapse.

Les informations que votre cerveau reçoit et traite correspondent à un chemin neural. Votre cerveau myelinisera ce chemin, renforçant la myéline autour de l'axone pour soutenir les signaux électriques. Grâce à la myéline renforcée, ce chemin sera plus susceptible de s'activer à l'avenir. En d'autres termes, vous apprenez.

Même à la plus petite échelle, notre cerveau est un graphe massif de neurones connectés. Nous apprenons et optimisons en rendant certains chemins plus susceptibles de se connecter que d'autres.

## La connaissance est un graphe : sciences de l'apprentissage

Le prédicteur le plus fort de notre performance dans un environnement d'apprentissage est notre connaissance préalable. Ce que nous savons déjà avant de commencer l'expérience d'apprentissage. Un article notable de psychologie, "1999 Dochy, Segers, and Buehl", a révélé que la connaissance préalable représente 81 % des différences de résultats entre les apprenants. La révision des connaissances préalables avant de présenter de nouvelles informations a un impact sur les résultats d'apprentissage. Et connecter de nouvelles connaissances aux connaissances préalables pendant l'enseignement peut également avoir un grand impact. (Voir [Eight Ideas](https://heiskr.com/stories/eight-big-ideas-of-learning) pour les sources.)

L'article de psychologie le plus célèbre est "The Magical Number Seven, Plus or Minus Two" de George Miller, publié en 1956. L'article suggère que les humains ont une mémoire de travail limitée. Miller a découvert que pour des nombres simples, un humain pouvait travailler avec environ sept éléments à la fois. Des chercheurs ultérieurs ont découvert que pour des informations plus complexes, cette limite est plus proche de quatre.

Certains psychologues suggèrent que parmi ces "quatre emplacements", pour que nous apprenions, au moins un ou deux doivent être des connaissances préalables. La quantité de connaissances préalables que nous pouvons "charger" dans l'un des quatre emplacements dépend de la force des connexions dans le graphe. Lorsque nous avons à la fois des connaissances préalables et de nouvelles connaissances dans notre mémoire de travail, nous associons les informations. Et nous renforçons la connexion entre les deux. Essayer d'apprendre de nouvelles informations sans les connecter aux connaissances préalables limite la force de la mémoire.

En résumé, nous apprenons en connectant les connaissances préalables aux nouvelles informations. Et ces connexions forment un grand graphe infini de connaissances.

## Quelques systèmes d'apprentissage adaptatif importants

Cette section est plus contextuelle, mais optionnelle. Je n'écris pas un article approfondi sur l'histoire de ces systèmes, mais voici quelques points :

* L'une des premières implémentations était la [machine d'enseignement de Skinner](https://en.wikipedia.org/wiki/Teaching_machine).
* Dans les années 1960 et 1970, il y a eu plusieurs tentatives de systèmes d'instruction informatisés. Les coûts et les machines plus lentes ont limité le succès de ces systèmes.
* À la fin des années 70 et au début des années 80, la [Théorie de la réponse aux items](https://en.wikipedia.org/wiki/Item_response_theory) a permis aux concepteurs de tests de commencer à travailler sur des tests adaptatifs informatisés.
* Un système informatisé précoce et influent était le tuteur Lisp, également connu sous le nom de LISPITS (1983) à l'Université Carnegie Mellon.
* [SuperMemo](https://en.wikipedia.org/wiki/SuperMemo), sorti en 1985, a incorporé l'apprentissage espacé dans un système informatisé.
* En 1985 également, un article sur les [Espaces de connaissances](https://en.wikipedia.org/wiki/Knowledge_space) a été publié, formant les fondations de l'un des quatre éléments.
* Le [tuteur de mathématiques ALEKS](https://en.wikipedia.org/wiki/ALEKS) est sorti en 1994, promouvant fortement son utilisation des espaces de connaissances.
* En 1995, Corbett et Anderson ont publié "Knowledge tracing", formant la base des modèles de [Bayesian knowledge tracing](https://en.wikipedia.org/wiki/Bayesian_Knowledge_Tracing).
* Certains logiciels importants incluent [AutoTutor](https://en.wikipedia.org/wiki/AutoTutor), [ACT-R](https://en.wikipedia.org/wiki/ACT-R) et [Cognitive Tutor Authoring Tools](http://ctat.pact.cs.cmu.edu/).
* [Knewton](https://en.wikipedia.org/wiki/Knewton) est un exemple de systèmes d'apprentissage adaptatif contemporains. Kaplan et Pearson utilisent tous deux Knewton pour fournir des expériences d'apprentissage adaptatif.

## Les quatre éléments

La plupart des systèmes d'apprentissage adaptatif aujourd'hui ont ces quatre éléments. Les termes changent et leur portée aussi. Mais vous trouverez presque toujours les quatre éléments.

Ces éléments sont :

* L'**expert** -- un modèle graphique de l'état "idéal", de tout ce que la personne pourrait apprendre en utilisant ce système.
* L'**apprenant** -- un modèle de l'état actuel de l'apprenant, qui montre la probabilité que l'apprenant connaisse chacun des nœuds du graphe de l'expert.
* Le **tuteur** -- les algorithmes qui déterminent quel contenu montrer et quand. Le modèle de l'expert et le modèle de l'apprenant informent le tuteur. Le tuteur cherche à optimiser le contenu pour la pertinence, le défi et l'efficacité.
* L'**interface** -- qui est la manière d'afficher l'expérience d'apprentissage à l'apprenant. Dans de nombreuses expériences d'apprentissage adaptatif, l'interface change en fonction du modèle de l'apprenant et des objectifs du tuteur.

Examinons chaque élément.

### L'expert — le grand graphe de tout

Le modèle de l'expert est un grand graphe connecté de tout ce que vous voulez que les apprenants sachent. Comme le suggère le nom, vous avez un expert sur le sujet -- ou des experts sur des sujets -- pour créer le modèle. Ce modèle est statique. Le modèle de l'expert ne change que lorsque la portée des résultats d'apprentissage change. Ou lorsque des problèmes et des opportunités de perfectionner le système d'apprentissage adaptatif se présentent.

La plupart du travail du modèle de l'expert se fait au début de la création d'une nouvelle expérience d'apprentissage. Le système d'apprentissage adaptatif accédera au modèle de l'expert pour comparer l'état actuel de l'apprenant avec le modèle de l'expert. Le système accédera également au modèle de l'expert pour déterminer quelle expérience d'apprentissage se concentrer ensuite.

Généralement, une équipe d'experts définira la portée des résultats d'apprentissage. Chaque nœud dans le modèle de l'expert doit avoir les attributs suivants :

* Un nom
* Une courte description, qui indique quelles compétences sont testées et ce qui est hors de portée
* Une liste de nœuds préalables -- ceux-ci forment les "arêtes" du graphe. Ces préalables ne peuvent pas former un "cycle" -- une boucle de nœuds.

Les modèles d'experts fonctionnent mieux lorsque chaque nœud est petit et étroitement défini. Par exemple, chaque compétence dans la taxonomie de Bloom -- reconnaissance, compréhension, application, analyse, synthèse et évaluation -- pourrait être son propre nœud dans le modèle de l'expert. La combinaison de deux compétences sous-jacentes doit également être un nœud séparé.

Il existe un nombre infini de formats que vous pourriez utiliser pour créer un modèle d'expert, tels que XML, JSON, CSV ou YAML. Il peut être utile de pouvoir afficher graphiquement le modèle de l'expert pour révision.

Certains systèmes généreront automatiquement un modèle d'expert en interrogeant des experts dans une série de questions, comme un assistant. D'autres regrouperont le contenu d'apprentissage existant, en utilisant des algorithmes comme le regroupement k-means. Vous pouvez consulter l'[article Wikipedia sur les espaces de connaissances](https://en.wikipedia.org/wiki/Knowledge_space) pour une description plus mathématique.

### L'apprenant — où vous en êtes par rapport à où vous voulez être

L'élément de l'apprenant est un modèle de l'état actuel des compétences de l'apprenant. Ainsi, pour chaque nœud donné dans le graphe de l'expert, le modèle de l'apprenant a une probabilité qui lui est associée : 1-99 %. Le système met à jour ce graphe chaque fois que l'apprenant effectue une activité. Si un apprenant répond correctement à une question, la probabilité augmente. Si l'apprenant répond incorrectement, la probabilité diminue.

Chaque apprenant a son propre modèle d'apprenant. Ainsi, chaque fois qu'il y a un nouvel apprenant dans le système, il y a un nouveau modèle d'apprenant. Plus tard, le tuteur utilisera le modèle de l'apprenant pour décider comment ordonner le contenu d'apprentissage.

Il existe de nombreux algorithmes pour mettre à jour le modèle de l'apprenant. Les espaces de connaissances suggèrent que, à mesure qu'un apprenant développe une compétence, les probabilités pour les compétences connexes doivent également s'ajuster.

Certains systèmes d'apprentissage adaptatif utilisent des modèles heuristiques simples pour mettre à jour les probabilités des compétences. Dans la théorie de la réponse aux items, la probabilité est mise à jour le long d'une courbe sigmoïde. Dans le traçage bayésien des connaissances, cette courbe a une forme plus conservatrice. Chaque modèle tend à prendre en compte ces facteurs :

* Avant que l'apprenant ne fasse quoi que ce soit, quelle est notre estimation de la probabilité ?
* Quelle est la probabilité qu'un apprenant devine la bonne réponse s'il ne connaît pas la compétence ?
* Quelle est la probabilité qu'un apprenant fasse une erreur même s'il connaît la compétence ?
* Quelle est la probabilité que l'apprenant ait "appris" la compétence après avoir vu l'élément ?
* Quelle est la probabilité que cette activité classe l'apprenant comme compétent ou non compétent ?
* Quelle sera la difficulté de cet élément pour cet apprenant particulier ?

Pour la théorie de la réponse aux items et le traçage bayésien des connaissances, vous aurez besoin d'un moyen d'estimer ces paramètres. C'est l'un des domaines en développement le plus rapide dans les systèmes d'apprentissage adaptatif, donc je ne peux pas encore faire de recommandations spécifiques. Il y a aussi des chercheurs qui créent des modèles avec l'apprentissage automatique classique, comme les réseaux de neurones.

### Le tuteur — quoi montrer et quand

Le tuteur choisit dans quel ordre sélectionner les activités que l'apprenant effectuera. Après chaque mise à jour du modèle de l'apprenant, le tuteur mettra à jour le chemin qu'il empruntera pour optimiser pour cet apprenant.

Le but du tuteur est d'amener l'apprenant à un graphe d'expert complet dans le temps le plus court possible. Certains systèmes permettent aux apprenants de se concentrer uniquement sur certains domaines tout en ignorant le reste. Comme le modèle de l'apprenant est unique pour chaque apprenant, le chemin que le tuteur empruntera l'est également. Alors que les éléments expert et apprenant sont des données avec quelques algorithmes, le tuteur est des algorithmes avec quelques données.

Le tuteur peut décider à la fois des compétences sur lesquelles se concentrer et des activités que l'apprenant doit effectuer. Pour les compétences sur lesquelles se concentrer, le tuteur choisira souvent les compétences ayant le plus grand impact sur le graphe plus large. Cela signifie souvent se concentrer sur des compétences plus élémentaires avant des compétences plus avancées. Pour les activités :

* Le tuteur essaiera de choisir les activités les plus pertinentes pour l'apprenant
* Le tuteur choisira des activités qui sont stimulantes, mais pas trop difficiles pour l'apprenant.
* Le tuteur essaiera de choisir des activités de manière à réduire le temps total nécessaire pour maîtriser.

Les tuteurs simples d'apprentissage adaptatif peuvent choisir des activités au hasard dans une compétence. Les tuteurs basés sur la théorie de la réponse aux items insistent sur le choix d'activités stimulantes. Dans les modèles de traçage bayésien des connaissances, le marché propose de nombreux algorithmes de tuteur différents. Les chercheurs se sont davantage concentrés sur les éléments expert et apprenant. Nous ne savons donc pas ce qui produit les meilleurs résultats d'apprentissage pour l'élément tuteur.

### L'interface — comment l'afficher

Certains systèmes d'apprentissage adaptatif modifieront l'interface utilisateur. Lorsque l'apprenant est moins familier avec une compétence, l'interface se réduit et se concentre davantage sur la tâche à accomplir. À mesure que la capacité de l'apprenant grandit, plus de l'interface complète se rassemble. Certains appellent ce processus "échafaudage".

Dans certains systèmes, les apprenants peuvent demander et recevoir des indices. Le moment où offrir des indices et la profondeur de ces indices peuvent s'ajuster en fonction de la capacité de l'apprenant.

Il y a aussi d'autres questions comme :

* Affichez-vous le graphe de l'expert à l'apprenant ?
* Affichez-vous leur progression sur toutes les compétences ? Comment ?
* Affichez-vous leur progression sur des compétences spécifiques ? Comment ?
* L'apprenant a-t-il des choix dans le contenu d'apprentissage ? Ou le système décide-t-il de tout ?

Selon les besoins du système, certains de ces éléments peuvent avoir un impact sur les résultats d'apprentissage.

## Comment savoir si l'apprentissage adaptatif est efficace ?

Comme ces systèmes proviennent du milieu universitaire, nous disposons d'une quantité significative de données et d'historique pour chaque système.

Le tutorat individuel humain offre les meilleurs résultats d'apprentissage. C'est une conclusion courante dans la recherche en éducation. Jusqu'à présent, aucun système d'apprentissage adaptatif informatisé n'a surpassé le tutorat humain en tête-à-tête.

Les chercheurs ont étudié l'apprentissage en classe seul, l'apprentissage adaptatif informatisé seul, ainsi que l'apprentissage en classe combiné à l'apprentissage adaptatif. Un [article de 2016 "Effectiveness of Intelligent Tutoring Systems"](https://www.researchgate.net/publication/277636218_Effectiveness_of_Intelligent_Tutoring_Systems_A_Meta-Analytic_Review) fournit une méta-analyse de ces études. Les systèmes d'apprentissage adaptatif surpassent généralement l'apprentissage en classe traditionnel. Combinés à l'apprentissage en classe, les systèmes d'apprentissage adaptatif créent un effet positif, mais il y a certaines limitations.

Les systèmes adaptatifs se distinguent particulièrement par les commentaires instantanés et la maîtrise des compétences. Les enquêteurs notent quelques domaines à améliorer :

* Le coût de développement de contenu pour ces systèmes est élevé.
* Ces systèmes ne peuvent souvent pas contextualiser l'apprentissage de la manière dont un humain peut le faire.
* Les systèmes d'apprentissage adaptatif peuvent sembler plus difficiles, ce qui peut réduire la motivation de l'apprenant.

## Conclusion

Et bien, je me suis un peu laissé emporter. J'ai couvert ce que sont les systèmes d'apprentissage adaptatif. J'ai fourni un peu de contexte pour la conception de ces systèmes. Un peu d'histoire. J'ai couvert les quatre éléments principaux : l'expert, l'apprenant, le tuteur et l'interface. J'espère que ce n'était pas trop technique.

Appel à l'action obligatoire à la fin de l'article : [Découvrez Sagefy](https://sagefy.org), le système d'apprentissage adaptatif à contenu ouvert sur lequel je travaille.