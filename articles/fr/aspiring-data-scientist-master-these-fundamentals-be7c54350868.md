---
title: Vous aspirez à devenir data scientist ? Maîtrisez ces fondamentaux.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T18:55:48.000Z'
originalURL: https://freecodecamp.org/news/aspiring-data-scientist-master-these-fundamentals-be7c54350868
coverImage: https://cdn-media-1.freecodecamp.org/images/1*XHVhBv7qx1RYrJ1Iyl_Sew.jpeg
tags:
- name: Data Science
  slug: data-science
- name: Life lessons
  slug: life-lessons
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Vous aspirez à devenir data scientist ? Maîtrisez ces fondamentaux.
seo_desc: 'By Peter Gleeson

  Data science is an exciting, fast-moving field to become involved in. There’s no
  shortage of demand for talented, analytically-minded individuals. Companies of all
  sizes are hiring data scientists, and the role provides real value ac...'
---

Par Peter Gleeson

La science des données est un domaine passionnant et en constante évolution. Il n'y a pas de pénurie de demande pour des individus talentueux et analytiques. Les entreprises de toutes tailles recrutent des data scientists, et ce rôle apporte une réelle valeur dans un large éventail d'industries et d'applications.

Souvent, les premières rencontres des gens avec ce domaine se font par la lecture de [titres de science-fiction](https://www.nature.com/articles/nature24270) générés par de grandes organisations de recherche. Les progrès récents ont soulevé la possibilité que l'apprentissage automatique transforme le monde tel que nous le connaissons en une génération.

Cependant, en dehors du milieu universitaire et de la recherche, la science des données englobe bien plus que les sujets à la une tels que le [deep learning](https://www.technologyreview.com/s/513696/deep-learning/) et le [NLP](https://www.wired.com/insights/2014/02/growing-importance-natural-language-processing/).

Une grande partie de la valeur commerciale d'un data scientist provient de la clarté et des insights que de vastes quantités de données peuvent apporter. Le rôle peut englober tout, de l'ingénierie des données à l'analyse et au reporting, avec peut-être un peu de machine learning pour faire bonne mesure.

C'est particulièrement le cas dans une startup. Les besoins en données des entreprises en phase de démarrage et de croissance sont généralement très éloignés du domaine des réseaux de neurones et de la vision par ordinateur. (Sauf, bien sûr, si ces éléments sont des caractéristiques principales de leur produit/service).

Plutôt, elles ont besoin d'analyses précises, de processus fiables et de la capacité à évoluer rapidement.

Par conséquent, les compétences requises pour de nombreux postes de data scientist sont larges et variées. Comme pour toute poursuite dans la vie, une grande partie de la valeur provient de la maîtrise des bases. La célèbre [règle 80:20](https://betterexplained.com/articles/understanding-the-pareto-principle-the-8020-rule/) s'applique — environ 80 % de la valeur provient de 20 % des compétences.

Voici un aperçu de certaines des compétences fondamentales que tout aspirant data scientist devrait maîtriser.

### Commencez par les statistiques

L'attribut principal qu'un data scientist apporte à son entreprise est la capacité à distiller des insights à partir de la complexité. La clé pour y parvenir est de comprendre comment découvrir du sens à partir de données bruyantes.

L'analyse statistique est donc une compétence importante à maîtriser. Les statistiques vous permettent de :

* Décrire les données, pour fournir une image détaillée aux parties prenantes
* Comparer les données et tester des hypothèses, pour éclairer les décisions commerciales
* Identifier les tendances et les relations qui offrent une réelle valeur prédictive

Les statistiques fournissent un ensemble puissant d'outils pour donner un sens aux données commerciales et opérationnelles.

Mais attention ! La seule chose pire que des insights limités sont des insights trompeurs. C'est pourquoi il est vital de comprendre les fondamentaux de l'analyse statistique.

Heureusement, il existe quelques principes directeurs que vous pouvez suivre.

#### Évaluez vos hypothèses

Il est très important d'être conscient des hypothèses que vous faites sur vos données.

Soyez toujours critique quant à la provenance et sceptique quant aux résultats. Pourrait-il y avoir une explication « peu intéressante » pour toute tendance observée dans vos données ? À quel point votre test statistique ou méthodologie choisi est-il valide ? Vos données répondent-elles à toutes les hypothèses sous-jacentes ?

Savoir quelles conclusions sont « intéressantes » et valent la peine d'être rapportées dépend également de vos hypothèses. Un cas élémentaire en est de juger s'il est plus approprié de rapporter la moyenne ou la médiane d'un ensemble de données.

Souvent, il est plus important de savoir quelle approche ne pas prendre que de savoir laquelle prendre. Il existe généralement plusieurs façons d'analyser un ensemble de données donné, mais assurez-vous d'éviter les pièges courants.

Par exemple, les [comparaisons multiples](https://www.stat.berkeley.edu/~mgoldman/Section0402.pdf) doivent toujours être corrigées. En aucun cas, vous ne devez chercher à confirmer une hypothèse en utilisant les mêmes données utilisées pour la générer ! Vous seriez surpris de la facilité avec laquelle cela peut être fait.

#### Distribution > Localisation

Chaque fois que je parle de statistiques introductives, je m'assure toujours de souligner un point particulier : la distribution d'une variable est généralement *au moins* aussi intéressante/informative que sa localisation. En fait, elle l'est souvent plus.

![Image](https://cdn-media-1.freecodecamp.org/images/rik8jxwiorgEeOcSoTlX527aPx4Y2OZ0-hj7)
_La tendance centrale est utile à connaître, mais la distribution est souvent plus intéressante à comprendre !_

C'est parce que la distribution d'une variable contient généralement des informations sur les processus génératifs (ou d'échantillonnage) sous-jacents.

Par exemple, les données de comptage suivent souvent une [distribution de Poisson](https://brilliant.org/wiki/poisson-distribution/), tandis qu'un système présentant un retour positif (« renforcement ») tendra à surfacer une [distribution de loi de puissance](https://www.theguardian.com/commentisfree/2011/nov/11/occupy-movement-wealth-power-law-distribution). Ne vous fiez jamais à une distribution normale des données sans avoir d'abord vérifié soigneusement.

Deuxièmement, comprendre la distribution des données est essentiel pour savoir comment travailler avec elles ! De nombreux tests et méthodes statistiques reposent sur des hypothèses concernant la distribution de vos données.

Par exemple, assurez-vous toujours de traiter les données unimodales et bimodales différemment. Elles peuvent avoir la même moyenne, mais vous perdriez une tonne d'informations importantes si vous ignoriez leurs distributions.

Pour un exemple plus intéressant qui illustre pourquoi vous devriez toujours vérifier vos données avant de rapporter des statistiques sommaires, regardez le [quartet d'Anscombe](https://en.wikipedia.org/wiki/Anscombe%27s_quartet) :

![Image](https://cdn-media-1.freecodecamp.org/images/sUOmUXDvexLRATldgB3ve07oyr72lmiWiNrp)
_Différentes données ; mais des moyennes, variances et corrélations presque identiques_

Chaque graphique semble très distinctif, n'est-ce pas ? Pourtant, chacun a des statistiques sommaires identiques — y compris leurs moyennes, variances et coefficients de corrélation. Tracer certaines des distributions révèle qu'elles sont plutôt différentes.

![Image](https://cdn-media-1.freecodecamp.org/images/WY3C1lBh5ZxbwERNiU7McZyJ24jPVI8HQoaa)

Enfin, la distribution d'une variable détermine la certitude que vous avez sur sa vraie valeur. Une distribution « étroite » permet une plus grande certitude, tandis qu'une distribution « large » permet moins de certitude.

La variance autour d'une moyenne est cruciale pour fournir un contexte. Trop souvent, des moyennes avec des intervalles de confiance très larges sont rapportées aux côtés de moyennes avec des intervalles de confiance très étroits. Cela peut être trompeur.

#### Échantillonnage approprié

La réalité est que l'échantillonnage peut être un point de douleur pour les data scientists orientés commercialement, en particulier pour ceux ayant un passé dans la recherche ou l'ingénierie.

Dans un cadre de recherche, vous pouvez ajuster précisément des expériences conçues avec de nombreux facteurs et niveaux différents et des traitements de contrôle. Cependant, les conditions commerciales « en direct » sont souvent sous-optimales du point de vue de la collecte de données. Chaque décision doit être soigneusement pesée contre le risque d'interrompre le « business-as-usual ».

Cela nécessite que les data scientists soient inventifs, mais réalistes, dans leur approche de la résolution de problèmes.

Les [tests A/B sont un exemple canonique](https://www.theguardian.com/technology/2014/feb/05/why-google-engineers-designers) d'une approche qui illustre comment les produits et plateformes peuvent être optimisés à un niveau granulaire sans causer de perturbation majeure au business-as-usual.

![Image](https://cdn-media-1.freecodecamp.org/images/z18nGPqOGUaZTqZMmP8dyKlxMzrjokk7LjTJ)
_Les tests A/B sont une norme industrielle pour comparer différentes versions de produits, afin de les optimiser_

Les [méthodes bayésiennes](http://mathworld.wolfram.com/BayesianAnalysis.html) peuvent être utiles pour travailler avec des ensembles de données plus petits, si vous avez un ensemble raisonnablement [informatif de priors](http://www.stats.org.uk/priors/Bayes6.pdf) à partir duquel travailler.

Avec toute donnée que vous collectez, assurez-vous de reconnaître ses limitations.

Les données d'enquête sont sujettes au biais d'échantillonnage (souvent, ce sont les répondants ayant les opinions les plus fortes qui prennent le temps de compléter l'enquête). Les séries temporelles et les données spatiales peuvent être affectées par l'[autocorrélation](https://www.investopedia.com/terms/a/autocorrelation.asp). Et enfin, méfiez-vous toujours de la [multicolinéarité](http://www.statisticshowto.com/multicollinearity/) lors de l'analyse de données provenant de sources connexes.

### Ingénierie des données

C'est un peu un cliché de la science des données, mais la réalité est que beaucoup du flux de travail des données est consacré à la recherche, au nettoyage et au stockage des données brutes nécessaires pour l'analyse en amont plus perspicace.

Comparativement peu de temps est réellement consacré à la mise en œuvre d'algorithmes à partir de zéro. En effet, la plupart des outils statistiques viennent avec leurs mécanismes internes enveloppés dans des packages R et des modules Python bien organisés.

Le processus [extract-transform-load](https://medium.freecodecamp.org/sqlalchemy-makes-etl-magically-easy-ab2bd0df928) (ETL) est crucial pour le succès de toute équipe de science des données. Les grandes organisations auront des ingénieurs de données dédiés pour répondre à leurs besoins complexes en infrastructure de données, mais les jeunes entreprises dépendront souvent de leurs data scientists pour posséder de solides compétences en ingénierie des données.

![Image](https://cdn-media-1.freecodecamp.org/images/JuAo5-Pczab04lxNo7GwvYmtOKK3FZmBXwHb)

#### Programmation en pratique

La science des données est hautement interdisciplinaire. En plus des compétences analytiques avancées et des connaissances spécifiques au domaine, le rôle nécessite également de solides compétences en programmation.

Il n'y a pas de réponse parfaite à la question de [quels langages de programmation](https://medium.freecodecamp.org/which-languages-should-you-learn-for-data-science-e806ba55a81f) un aspirant data scientist devrait apprendre à utiliser. Cela dit, au moins l'un des langages [Python](https://www.python.org/) et/ou [R](https://www.r-project.org/) vous servira très bien.

![Image](https://cdn-media-1.freecodecamp.org/images/BOncv7QP5YTJhE-A0NF3l79W7S7FieIr9znU)
_L'un ou l'autre (ou les deux) de ces langages constituent un excellent point de départ si vous souhaitez travailler avec des données_

Quel que soit le langage que vous choisissez, visez à devenir familier avec toutes ses fonctionnalités et l'écosystème environnant. Parcourez les différents packages et modules disponibles, et configurez votre IDE parfait. Apprenez les API que vous devrez utiliser pour accéder aux plateformes et services principaux de votre entreprise.

Les bases de données sont une pièce intégrale du puzzle de tout flux de travail de données. Assurez-vous de maîtriser un dialecte de SQL. Le choix exact n'est pas trop important, car le passage de l'un à l'autre est un processus gérable lorsque nécessaire.

Les bases de données NoSQL (comme [MongoDB](https://www.mongodb.com/)) peuvent également valoir la peine d'être apprises, si votre entreprise les utilise.

Devenir un utilisateur confiant de la ligne de commande contribuera grandement à augmenter votre productivité au quotidien. Même une familiarité passagère avec les scripts bash simples vous donnera un bon départ en matière d'automatisation des tâches répétitives.

#### Codage efficace

Une compétence très importante pour les aspirants data scientists à maîtriser est le codage efficace. La réutilisabilité est la clé. Il vaut la peine de prendre le temps (quand il est disponible) pour écrire du code à un niveau d'abstraction qui permet de l'utiliser plus d'une fois.

Cependant, il y a un équilibre à trouver entre les priorités à court et à long terme.

Il n'y a pas de raison de prendre deux fois plus de temps pour écrire un script ad hoc réutilisable s'il n'y a aucune chance qu'il soit jamais pertinent à nouveau. Pourtant, chaque minute passée à refactoriser l'ancien code pour le réexécuter est une minute qui aurait pu être économisée précédemment.

Les meilleures pratiques de l'ingénierie logicielle valent la peine d'être développées afin d'écrire un code de production vraiment performant.

Les outils de gestion de version tels que Git rendent le déploiement et la maintenance du code beaucoup plus fluides. Les planificateurs de tâches vous permettent d'automatiser les processus de routine. Les revues de code régulières et les normes de documentation convenues faciliteront grandement la vie des futurs membres de votre équipe.

Dans tout domaine de spécialisation technologique, il n'est généralement pas nécessaire de réinventer la roue. L'ingénierie des données ne fait pas exception. Des frameworks tels que [Airflow](https://airflow.apache.org/) facilitent et rendent plus robustes la planification et la surveillance des processus ETL. Pour le stockage et le traitement distribués des données, il y a [Apache Spark](https://spark.apache.org/) et [Hadoop](http://hadoop.apache.org/).

![Image](https://cdn-media-1.freecodecamp.org/images/Ev4qhnVU4ozvlxs6U8YjhNVPq-D5L7HaIM-W)

Il n'est pas essentiel pour un débutant d'apprendre ces outils en profondeur. Pourtant, avoir une conscience de l'écosystème environnant et des outils disponibles est toujours un avantage.

### Communiquez clairement

La science des données est une discipline full stack, avec une partie frontale importante orientée vers les parties prenantes : la couche de reporting.

Le fait est simple — une communication efficace apporte avec elle une valeur commerciale significative. Avec la science des données, il y a quatre aspects à un reporting efficace.

* **Précision**   
Cela est crucial, pour des raisons évidentes. La compétence ici est de savoir comment interpréter vos résultats, tout en étant clair sur les limitations ou les mises en garde qui peuvent s'appliquer. Il est important de ne pas surestimer ou sous-estimer la pertinence de tout résultat particulier.
* **Précision**   
Cela compte, car toute ambiguïté dans votre rapport pourrait conduire à une mauvaise interprétation des résultats. Cela pourrait avoir des conséquences négatives plus tard.
* **Concis**  
Gardez votre rapport aussi court que possible, mais pas plus court. Un bon format pourrait fournir un contexte pour la question principale, inclure une brève description des données disponibles, et donner un aperçu des résultats et graphiques « principaux ». Des détails supplémentaires peuvent (et doivent) être inclus dans une annexe.
* **Accessible**  
Il y a un besoin constant d'équilibrer la précision technique d'un rapport avec la réalité que la plupart de ses lecteurs seront des experts dans leurs propres domaines respectifs, et pas nécessairement en science des données. Il n'y a pas de réponse facile et universelle ici. Une communication fréquente et des retours aideront à établir un équilibre approprié.

#### Le jeu des graphiques

Des visualisations de données puissantes vous aideront à communiquer des résultats complexes aux parties prenantes de manière efficace. Un graphique ou un tableau bien conçu peut révéler en un coup d'œil ce que plusieurs paragraphes de texte seraient nécessaires pour expliquer.

Il existe une large gamme d'outils de visualisation et de construction de tableaux de bord gratuits et payants, notamment Plotly, Tableau, Chartio, d3.js et [beaucoup d'autres](https://www.creativebloq.com/design-tools/data-visualization-712402).

Pour des maquettes rapides, parfois vous ne pouvez pas battre les bons vieux logiciels de tableur comme Excel ou Google Sheets. Ceux-ci feront le travail comme requis, bien qu'ils manquent de la fonctionnalité des logiciels de visualisation spécialisés.

Lors de la construction de tableaux de bord et de graphiques, il y a un certain nombre de principes directeurs à considérer. Le défi sous-jacent est de maximiser la valeur informative de la visualisation, sans sacrifier la « lisibilité ».

![Image](https://cdn-media-1.freecodecamp.org/images/ROM8HBlVkLC8vq-pq-BR0FAFzoAoR9J35Vlj)
_Comment ne pas présenter les données — en général, gardez cela simple (pour plus d'informations sur cet exemple, lisez [ce blog post intéressant](http://glengilchrist.co.uk/post/the-3d-challenge-can-you-read-this-chart" rel="noopener" target="_blank" title="))_

Une visualisation efficace révèle un aperçu de haut niveau en un coup d'œil. Les graphiques plus complexes peuvent prendre un peu plus de temps pour être assimilés par le spectateur, et doivent donc offrir un contenu informatif beaucoup plus grand.

Si vous ne lisez qu'un seul livre sur la visualisation des données, alors le classique d'Edward Tufte [_The Visual Display of Quantitative Information_](https://www.goodreads.com/book/show/17744.The_Visual_Display_of_Quantitative_Information) est le choix exceptionnel.

Tufte a popularisé et inventé une grande partie du domaine de la visualisation des données. Des termes largement utilisés tels que [chartjunk](http://www.businessinsider.com/the-27-worst-charts-of-all-time-2013-6?op=1&IR=T) et data density doivent leurs origines au travail de Tufte. Son concept du [data-ink ratio](http://www-personal.umich.edu/~jpboyd/eng403_chap2_tuftegospel.pdf) reste influent plus de trente ans plus tard.

L'utilisation de la couleur, de la mise en page et de l'interactivité fera souvent la différence entre une bonne visualisation et une visualisation de haute qualité et professionnelle.

![Image](https://cdn-media-1.freecodecamp.org/images/M4erTx4iXd9tA9sl5QsJSf-whYhOGt9977oD)
_Visualisation de données mieux faite [[Source](https://www.wsj.com/articles/SB10001424052748703786804576137932801470052" rel="noopener" target="_blank" title=")]_

En fin de compte, la création d'une grande visualisation de données touche à des compétences plus souvent associées à l'UX et au design graphique qu'à la science des données. Lire sur ces sujets pendant votre temps libre est un excellent moyen de développer une conscience de ce qui fonctionne et de ce qui ne fonctionne pas.

Assurez-vous de consulter des sites comme [bl.ocks.org](https://bl.ocks.org/) pour vous inspirer !

### La science des données nécessite un ensemble de compétences diversifié

Il y a quatre domaines de compétences principaux sur lesquels vous, en tant qu'aspirant data scientist, devriez vous concentrer pour vous développer. Ils sont :

* Les statistiques, y compris la théorie sous-jacente et l'application dans le monde réel.
* La programmation, dans au moins l'un des langages Python ou R, ainsi que SQL et l'utilisation de la ligne de commande
* Les meilleures pratiques en ingénierie des données
* La communication efficace de votre travail

#### Bonus ! Apprenez constamment

Si vous avez lu jusqu'ici et que vous vous sentez un peu découragé — rassurez-vous. La compétence principale dans un domaine en évolution aussi rapide est d'apprendre à apprendre et à réapprendre. Sans aucun doute, de nouveaux frameworks, outils et méthodes émergeront dans les années à venir.

L'ensemble de compétences exact que vous apprenez maintenant pourrait devoir être entièrement mis à jour dans cinq à dix ans. Attendez-vous à cela. En faisant cela et en étant préparé, vous pouvez rester en tête du jeu grâce à un réapprentissage continu.

Vous ne pouvez jamais tout savoir, et la vérité est — personne ne le fait jamais. Mais, si vous maîtrisez les fondamentaux, vous serez en position de vous approprier tout le reste sur une base de besoin de savoir.

Et c'est probablement la clé du succès dans toute discipline en développement rapide.