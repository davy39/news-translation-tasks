---
title: Si vous êtes un développeur en transition vers la science des données, voici
  vos meilleures ressources
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-01T19:34:02.000Z'
originalURL: https://freecodecamp.org/news/if-youre-a-developer-transitioning-into-data-science-here-are-your-best-resources-c31928b53cd1
coverImage: https://cdn-media-1.freecodecamp.org/images/1*omoLHRzItrE69MC6Um6pIA.png
tags:
- name: Career
  slug: career
- name: Data Science
  slug: data-science
- name: Machine Learning
  slug: machine-learning
- name: Software Engineering
  slug: software-engineering
seo_title: Si vous êtes un développeur en transition vers la science des données,
  voici vos meilleures ressources
seo_desc: 'By Cecelia Shao

  It seems like everyone wants to be a data scientist these days — from PhD students
  to data analysts to your old college roommate who keeps Linkedin messaging you to
  ‘grab coffee’.

  Perhaps you’ve had the same inkling that you should at...'
---

Par Cecelia Shao

Il semble que tout le monde veuille devenir scientifique des données ces jours-ci — des étudiants en doctorat aux analystes de données en passant par votre ancien colocataire de l'université qui ne cesse de vous envoyer des messages LinkedIn pour "prendre un café".

Peut-être avez-vous eu la même intuition que vous devriez au moins explorer quelques postes en science des données et voir ce que tout ce battage médiatique a à offrir. Peut-être avez-vous vu des articles comme celui de Vicki Boykis [Data Science is different now](https://veekaybee.github.io/2019/02/13/data-science-is-different) qui déclare :

> **Ce qui devient clair, c'est qu'à un stade avancé du cycle de battage médiatique, la science des données se rapproche asymptotiquement de l'ingénierie, et les [compétences dont les scientifiques des données ont besoin](https://www.youtube.com/watch?v=frQeK8xo9Ls) à l'avenir sont moins basées sur la visualisation et les statistiques, et [plus en ligne avec l'informatique traditionnelle](https://tech.trivago.com/2018/12/03/teardown-rebuild-migrating-from-hive-to-pyspark/)...**

> Des concepts comme les tests unitaires et l'intégration continue ont rapidement trouvé leur place dans le jargon et l'ensemble d'outils couramment utilisés par les scientifiques des données et les scientifiques numériques travaillant sur l'ingénierie ML.

ou [tweets](https://twitter.com/tdhopper/status/730425632862044161) comme celui de Tim Hopper :

Ce qui n'est pas clair, c'est comment vous pouvez tirer parti de votre expérience en tant qu'ingénieur logiciel pour obtenir un poste en science des données. Certaines autres questions que vous pourriez vous poser sont :

_Que devrais-je prioriser dans mon apprentissage ?_

_Y a-t-il des meilleures pratiques ou des outils différents pour les scientifiques des données ?_

_Mon ensemble de compétences actuel sera-t-il transférable à un rôle en science des données ?_

Cet article fournira un contexte sur le rôle du scientifique des données et pourquoi votre formation pourrait être un bon choix pour la science des données, ainsi que des actions concrètes et progressives que vous, en tant que développeur, pouvez entreprendre pour vous lancer dans la science des données.

> Vous voulez voir les dernières offres d'emploi en science des données ? Abonnez-vous à la newsletter bihebdomadaire [ML Jobs Newsletter](https://www.getrevue.co/profile/mljobs) pour recevoir les nouvelles offres d'emploi en science des données directement dans votre boîte de réception.

### Scientifique des données versus Ingénieur des données

Tout d'abord, nous devons distinguer deux rôles complémentaires : Scientifique des données versus Ingénieur des données. Bien que ces deux rôles traitent des modèles d'apprentissage automatique, leur interaction avec ces modèles ainsi que les exigences et la nature du travail pour les scientifiques des données et les ingénieurs des données varient largement.

> Remarque : Le rôle d'Ingénieur des données spécialisé dans l'apprentissage automatique peut également apparaître dans les descriptions de poste sous le nom d'« Ingénieur logiciel, Apprentissage automatique » ou « Ingénieurs en Apprentissage automatique ».

Dans le cadre d'un [flux de travail d'apprentissage automatique](https://skymind.ai/wiki/machine-learning-workflow), le scientifique des données effectuera l'analyse statistique nécessaire pour déterminer quelle approche d'apprentissage automatique utiliser, puis commencera à prototyper et à construire ces modèles.

Les ingénieurs en apprentissage automatique collaborent souvent avec les scientifiques des données avant et après ce processus de modélisation : (1) en construisant des pipelines de données pour alimenter les données dans ces modèles et (2) en concevant un système d'ingénierie qui servira ces modèles pour assurer une santé continue des modèles.

Le diagramme ci-dessous est une façon de visualiser ce continuum de compétences :

![Image](https://cdn-media-1.freecodecamp.org/images/1*3u1RTgYVDpQHvLcbQVYT4g.png)

Il existe une multitude de ressources en ligne sur la différence entre les scientifiques des données et les ingénieurs des données — assurez-vous de consulter :

* [Panoply : Quelle est la différence entre un ingénieur des données et un scientifique des données ?](https://blog.panoply.io/what-is-the-difference-between-a-data-engineer-and-a-data-scientist)
* [Springboard : Ingénieur en Apprentissage automatique vs Scientifique des données](https://www.springboard.com/blog/machine-learning-engineer-vs-data-scientist/)
* [O'Reilly : Ingénieurs des données vs. scientifiques des données](https://www.oreilly.com/ideas/data-engineers-vs-data-scientists)

En guise de mise en garde, cet article couvre principalement le rôle de Scientifique des données avec quelques références au côté Ingénierie en Apprentissage automatique (particulièrement pertinent si vous cherchez un poste dans une petite entreprise où vous pourriez avoir à jouer les deux rôles). Si vous êtes intéressé à voir comment vous pouvez passer à un rôle d'Ingénieur des données ou d'Ingénieur en Apprentissage automatique, faites-le nous savoir dans les commentaires ci-dessous !

### Votre avantage en tant que développeur

Au détriment de tous, les cours sur l'apprentissage automatique comme "Introduction à la Science des données en Python" ou le cours Coursera d'Andrew Ng ne couvrent _pas_ les concepts et les meilleures pratiques de l'ingénierie logicielle comme les tests unitaires, l'écriture de code modulaire réutilisable, CI/CD, ou le contrôle de version. Même certaines des équipes d'apprentissage automatique les plus avancées n'utilisent toujours pas ces pratiques pour leur code d'apprentissage automatique, ce qui conduit à une tendance inquiétante...

Pete Warden a décrit cette tendance comme "[la Crise de Reproductibilité en Apprentissage automatique](https://petewarden.com/2018/03/19/the-machine-learning-reproducibility-crisis/)" :

> nous sommes encore dans les âges sombres en ce qui concerne le suivi des changements et la reconstruction des modèles à partir de zéro. **C'est si mauvais que parfois cela ressemble à un retour en arrière dans le temps lorsque nous codions sans contrôle de source.**

Bien que vous ne voyiez peut-être pas ces compétences "d'ingénierie logicielle" explicitement mentionnées dans les descriptions de poste pour les scientifiques des données, avoir une bonne maîtrise de ces compétences dans votre formation vous aidera à multiplier par 10 votre travail en tant que scientifique des données. De plus, elles vous seront utiles lorsque viendra le temps de répondre à ces questions de programmation lors de votre entretien pour un poste en science des données.

Pour une perspective intéressante de l'autre côté, consultez l'article de [Trey Causey](https://www.freecodecamp.org/news/if-youre-a-developer-transitioning-into-data-science-here-are-your-best-resources-c31928b53cd1/undefined) sur les "[Compétences en développement logiciel pour les scientifiques des données](http://treycausey.com/software_dev_skills.html)" sur les compétences qu'il recommande aux scientifiques des données d'apprendre pour "écrire un meilleur code, interagir mieux avec les développeurs de logiciels, et finalement vous faire gagner du temps et éviter des maux de tête".

### Se lancer dans la science des données

C'est formidable que vous ayez une bonne base avec votre formation en ingénierie logicielle, mais quelle est la prochaine étape pour devenir scientifique des données ? Le tweet ironique de Josh Will sur la définition d'un scientifique des données est surprenamment précis :

Il suggère l'un des sujets que vous devriez rattraper si vous êtes intéressé par un rôle ou une carrière de scientifique des données : les statistiques. Dans cette prochaine section, nous couvrirons d'excellentes ressources pour :

* **Acquérir des connaissances spécifiques au ML**
* **Acquérir des connaissances sectorielles**
* **Outils de la stack ML**
* **Compétences et qualifications**

#### **Acquérir des connaissances spécifiques au ML**

Il est plus efficace de construire une combinaison de connaissances théoriques autour de la probabilité et des statistiques ainsi que des compétences appliquées dans des domaines comme la manipulation de données ou l'entraînement de modèles sur des GPU/calcul distribué.

Une façon de structurer les connaissances que vous acquérez est de les référer au flux de travail de l'apprentissage automatique.

![Image](https://cdn-media-1.freecodecamp.org/images/1*omoLHRzItrE69MC6Um6pIA.png)
_Une vue simplifiée du flux de travail de l'apprentissage automatique_

> Voir [ce flux de travail détaillé](https://skymind.ai/wiki/machine-learning-workflow) de Skymind AI

Voici quelques-unes des meilleures ressources que vous pouvez trouver autour de l'apprentissage automatique. Il serait impossible d'avoir une liste exhaustive et pour économiser de l'espace (et du temps de lecture), nous n'avons pas mentionné des ressources très populaires comme le cours Coursera d'Andrew Ng ou Kaggle.

**Cours :**

* [Fast.ai MOOC](https://www.fast.ai/) (cours gratuits qui enseignent des compétences très appliquées dans le cadre de l'apprentissage profond pratique pour les codeurs, l'apprentissage profond de pointe pour les codeurs, l'algèbre linéaire computationnelle et l'introduction à l'apprentissage automatique pour les codeurs)
* Khan Academy
* Chaînes YouTube [3Blue1Brown](https://www.youtube.com/channel/UCYO_jab_esuFRV4b17AJtAw) et [mathematicalmonk](https://www.youtube.com/channel/UCcAtD_VYwcYwVbTdvArsm7w)
* Cours Udacity (y compris [Prétraitement pour l'apprentissage automatique en Python](https://www.datacamp.com/courses/preprocessing-for-machine-learning-in-python))
* Parcours spécifique à l'IA/ML de [Springboard](https://www.springboard.com/blog/ai-machine-learning-career-track/)

**Manuels :** *tentative de trouver des PDF gratuits en ligne pour la plupart de ceux-ci*

* [Programmation probabiliste et méthodes bayésiennes pour les hackers](http://camdavidsonpilon.github.io/Probabilistic-Programming-and-Bayesian-Methods-for-Hackers/)
* [Probabilité et processus aléatoires](https://www.amazon.com/Probability-Random-Processes-Geoffrey-Grimmett/dp/0198572220/)
* [Éléments de l'apprentissage statistique](https://web.stanford.edu/~hastie/Papers/ESLII.pdf)
* [Algèbre linéaire faite correctement](http://148.206.53.84/tesiuami/S_pdfs/Linear%20Algebra%20Done%20Right.pdf)
* [Introduction à l'algèbre linéaire](http://math.mit.edu/~gs/linearalgebra/)
* [Conception d'algorithmes](http://www.cs.sjtu.edu.cn/~jiangli/teaching/CS222/files/materials/Algorithm%20Design.pdf)

**Guides :**

* [Guide de développement machine learning de Google](https://developers.google.com/machine-learning/guides/rules-of-ml/)
* [Guides de maîtrise de l'apprentissage automatique](https://machinelearningmastery.com/start-here/) (pour un bon point de départ, voir [ce mini-cours sur l'apprentissage automatique Python](https://machinelearningmastery.com/python-machine-learning-mini-course/))
* [Pyimagesearch](https://www.pyimagesearch.com/) (pour la vision par ordinateur)

**Rencontres :** *principalement basées à NYC*

* [Papers We Love](https://paperswelove.org/)
* [NYC Intelligence Artificielle et Apprentissage Automatique](https://www.meetup.com/NYC-Artificial-Intelligence-Machine-Learning/)
* [DataCouncil.ai](https://www.meetup.com/DataCouncil-AI-NYC-Data-Engineering-Science/)
* [NY Intelligence Artificielle](https://www.meetup.com/NYAImeetup/)

> Pour un point de départ intéressant, consultez le "[Open-Source Machine Learning Masters](http://willwolf.io/2018/02/03/practical-guide-open-source-ml-masters/)" de Will Wolf sur la façon dont vous pouvez structurer votre temps entre l'étude de sujets spécifiques et le travail sur des projets pour montrer votre expertise dans un lieu distant à faible coût.

#### Acquérir des connaissances sectorielles

Si vous avez une intuition que vous aimeriez travailler dans un secteur spécifique comme la santé, les services financiers, les biens de consommation, le commerce de détail, etc..., il est inestimable de vous mettre à jour sur les points de douleur et les développements de ce secteur en relation avec les données et l'apprentissage automatique.

**Un conseil pro =** vous pouvez parcourir les sites web des startups d'IA spécifiques à un secteur et voir comment elles positionnent leur proposition de valeur et où l'apprentissage automatique entre en jeu. Cela vous donnera des idées pour des domaines spécifiques de l'apprentissage automatique à étudier et des sujets pour des projets afin de mettre en valeur votre travail.

**Nous pouvons passer par un exemple :** disons que je suis intéressé à travailler dans le domaine de la santé.

1. Grâce à une recherche rapide sur Google pour "_machine learning healthcare_", j'ai trouvé cette liste de Healthcareweekly.com sur les "[Meilleures startups de santé à surveiller en 2019](https://healthcareweekly.com/best-healthcare-startups-to-watch-for-in-2019/)".

> Vous pouvez également effectuer des recherches rapides sur [Crunchbase](https://www.crunchbase.com/hub/health-care-startups#section-leaderboard) ou [AngelList](https://angel.co/jobs#find/f!%7B%22keywords%22%3A%5B%22Healthcare%22%5D%7D) avec "santé" comme mot-clé.

2. Prenons l'une des entreprises présentées sur la liste, [BenevolentAI](https://benevolent.ai/), comme exemple.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PfrEeqvUlERnSvGVdoBDWg.png)

3. Le site web de BenevolentAI indique :

> Nous sommes une entreprise d'IA avec une capacité de bout en bout, de la découverte précoce de médicaments au développement clinique en phase avancée. BenevolentAI combine la puissance de la médecine computationnelle et de l'IA avancée avec les principes des systèmes ouverts et du cloud computing pour transformer la manière dont les médicaments sont conçus, développés, testés et mis sur le marché.

> Nous avons construit la plateforme Benevolent pour mieux comprendre les maladies et concevoir de nouveaux traitements, et améliorer les traitements existants, à partir de vastes quantités d'informations biomédicales. Nous croyons que notre technologie permet aux scientifiques de développer des médicaments plus rapidement et de manière plus rentable.

> Un nouvel article de recherche est publié toutes les 30 secondes, mais les scientifiques n'utilisent actuellement qu'une fraction des connaissances disponibles pour comprendre la cause des maladies et proposer de nouveaux traitements. Notre plateforme ingère, "lit" et contextualise de vastes quantités d'informations tirées de documents écrits, de bases de données et de résultats expérimentaux. Elle est capable de faire infiniment plus de déductions et d'inférences à travers ces sources de données disparates et complexes, identifiant et créant des relations, des tendances et des motifs, qui seraient impossibles pour un être humain à faire seul.

4. Vous pouvez immédiatement voir que BenevolentAI utilise le traitement du langage naturel (NLP) et travaille probablement avec certains graphes de connaissances s'ils identifient des relations entre les maladies et la recherche de traitements.

5. Si vous consultez la page carrière de BenevolentAI, vous pouvez voir qu'ils recrutent pour un [Chercheur principal en apprentissage automatique](https://benevolent.ai/career-open-positions/senior-machine-learning-researcher). Il s'agit d'un poste senior, donc ce n'est pas un exemple parfait, mais jetez un œil aux compétences et qualifications qu'ils demandent ci-dessous :

**Remarque :**

* traitement du langage naturel, inférence de graphe de connaissances, apprentissage actif et modélisation biochimique
* sources de données structurées et non structurées
* approches de modèles bayésiens
* connaissance des outils modernes pour le ML

![Image](https://cdn-media-1.freecodecamp.org/images/1*LXgNRqLT8u28wc86N1OSrw.png)

**Cela devrait vous donner quelques étapes pour savoir quoi aborder ensuite :**

* travailler avec des données structurées
* travailler avec des données non structurées
* classer les relations dans les graphes de connaissances (voir une bonne ressource [ici](https://medium.com/comet-ml/using-fasttext-and-comet-ml-to-classify-relationships-in-knowledge-graphs-e73d27b40d67))
* apprendre la probabilité bayésienne et les approches de modélisation
* travailler sur un projet de NLP (donc des données textuelles)

Nous ne recommandons pas que vous postuliez aux entreprises que vous trouvez par le biais de votre recherche, mais plutôt que vous voyiez comment elles décrivent les points de douleur de leurs clients, les propositions de valeur de leur entreprise, et quel type de compétences elles listent dans leurs descriptions de poste pour guider vos recherches.

#### Outils de la stack ML

Dans la description de poste de Chercheur principal en apprentissage automatique chez BenevolentAI, ils demandent une _"connaissance des outils modernes pour le ML, comme Tensorflow, PyTorch, etc..."_.

Apprendre ces outils modernes pour le ML peut sembler décourageant puisque l'espace est toujours en évolution. Pour diviser le processus d'apprentissage en morceaux gérables, rappelez-vous d'ancrer votre réflexion autour du flux de travail de l'apprentissage automatique ci-dessus — "Quel outil peut m'aider avec cette partie du flux de travail ?".

![Image](https://cdn-media-1.freecodecamp.org/images/1*omoLHRzItrE69MC6Um6pIA.png)

Pour voir quels outils accompagnent chaque étape de ce flux de travail d'apprentissage automatique, consultez l'article de [Roger Huang](https://www.freecodecamp.org/news/if-youre-a-developer-transitioning-into-data-science-here-are-your-best-resources-c31928b53cd1/undefined) intitulé "[Introduction à la stack de l'apprentissage automatique](https://hackernoon.com/introduction-to-the-machine-learning-stack-f5b64bba7602)" qui couvre des outils comme [Docker](https://www.docker.com/), [Comet.ml](http://www.comet.ml), et [dask-ml](https://dask-ml.readthedocs.io/en/latest/).

Sur le plan tactique, [Python](https://www.python.org/) et [R](https://www.r-project.org/about.html) sont les langages de programmation les plus courants que les scientifiques des données utilisent et vous rencontrerez des packages complémentaires conçus pour des applications de science des données, tels que [NumPy](http://www.numpy.org/) et [SciPy](http://www.scipy.org/), et matplotlib. Ces langages sont interprétés, plutôt que compilés, laissant le scientifique des données libre de se concentrer sur le problème plutôt que sur les nuances du langage. Il vaut la peine d'investir du temps pour apprendre la programmation orientée objet afin de comprendre la mise en œuvre des structures de données en tant que classes.

Pour vous mettre à jour sur les frameworks ML comme Tensorflow, Keras et PyTorch, assurez-vous d'aller sur leur documentation et d'essayer de mettre en œuvre leurs tutoriels de bout en bout.

À la fin de la journée, vous voulez vous assurer que vous construisez des projets qui mettent en valeur ces outils modernes pour la collecte et la manipulation de données, la gestion des expériences d'apprentissage automatique et la modélisation.

Pour quelques idées pour vos projets, consultez l'article d'[Edouard Harris](https://www.freecodecamp.org/news/if-youre-a-developer-transitioning-into-data-science-here-are-your-best-resources-c31928b53cd1/undefined) sur "[Le problème du démarrage à froid : comment construire votre portfolio d'apprentissage automatique](https://towardsdatascience.com/the-cold-start-problem-how-to-build-your-machine-learning-portfolio-6718b4ae83e9)".

#### **Compétences et qualifications**

Nous avons laissé cette section pour la fin car elle regroupe une grande partie des informations des sections précédentes, mais est spécifiquement orientée vers la préparation aux entretiens en science des données. Il y a six sujets principaux lors d'un entretien pour un poste de scientifique des données :

1. Codage
2. Produit
3. SQL
4. Tests A/B
5. Apprentissage automatique
6. Probabilité (voir une bonne définition vs. Statistiques [ici](https://www3.cs.stonybrook.edu/~skiena/jaialai/excerpts/node12.html))

Vous remarquerez que l'un de ces sujets n'est pas comme les autres (Produit). Pour les postes en science des données, [la communication sur les concepts techniques et les résultats](https://medium.com/comet-ml/a-data-scientists-guide-to-communicating-results-c79a5ef3e9f1) ainsi que les métriques commerciales et l'impact sont cruciaux.

> **Quelques agrégations utiles de questions d'entretien en science des données :**

> ?? ht[tps://github.com/kojino/120-Data-Science-Interview-Questions](https://github.com/kojino/120-Data-Science-Interview-Questions)

> [??ht](https://github.com/kojino/120-Data-Science-Interview-Questions)[tps://github.com/iamtodor/data-science-interview-questions-and-answers](https://github.com/iamtodor/data-science-interview-questions-and-answers)

> [???? http](https://github.com/iamtodor/data-science-interview-questions-and-answers)[s://hookedondata.org/red-flags-in-data-science-interviews/](https://hookedondata.org/red-flags-in-data-science-interviews/)

> [?? ht](https://hookedondata.org/red-flags-in-data-science-interviews/)[tps://medium.com/@XiaohanZeng/i-interviewed-at-five-top-companies-in-silicon-valley-in-five-days-and-luckily-got-five-job-offers-25178cf74e0f](https://medium.com/@XiaohanZeng/i-interviewed-at-five-top-companies-in-silicon-valley-in-five-days-and-luckily-got-five-job-offers-25178cf74e0f)

[Vous remarquerez que nous avons inclus l'article de Hooked on Data sur les "](https://medium.com/@XiaohanZeng/i-interviewed-at-five-top-companies-in-silicon-valley-in-five-days-and-luckily-got-five-job-offers-25178cf74e0f)[Drapeaux rouges dans les entretiens en science des données](https://hookedondata.org/red-flags-in-data-science-interviews/)" — au fur et à mesure que vous passez des entretiens pour des postes, vous rencontrerez des entreprises qui construisent encore leur infrastructure de données ou qui n'ont peut-être pas une compréhension solide de la manière dont leur équipe de science des données s'intègre dans la valeur globale de l'entreprise.

Ces entreprises peuvent encore gravir cette hiérarchie des besoins ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/1*7IMev5xslc9FLxr9hHhpFw.png)
_La populaire hiérarchie des besoins en IA de Monica Rogati_

Pour quelques attentes concernant les entretiens en science des données, je recommande de lire l'article de Tim Hopper sur "[Quelques réflexions sur le fait d'être refusé pour de nombreux emplois en science des données](https://tdhopper.com/blog/some-reflections-on-being-turned-down-for-a-lot-of-data-science-jobs/)".

#### Merci d'avoir lu ! Nous espérons que ce guide vous aide à comprendre si la science des données est une carrière que vous devriez envisager et comment commencer ce voyage !

_Vous voulez voir les dernières offres d'emploi en science des données ? Abonnez-vous à la newsletter bihebdomadaire [ML Jobs Newsletter](https://www.getrevue.co/profile/mljobs) pour recevoir les nouvelles offres d'emploi en science des données directement dans votre boîte de réception :_

[**ML Jobs Newsletter - Revue**](https://www.getrevue.co/profile/mljobs)
[_Inscrivez-vous pour recevoir cette liste bihebdomadaire d'offres d'emploi en science des données dans les meilleures entreprises du secteur. Rôles...www.getrevue.co](https://www.getrevue.co/profile/mljobs)