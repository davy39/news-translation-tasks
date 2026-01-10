---
title: Vous pensez avoir besoin d'un tableau de bord ? Vous devriez plutôt créer un
  notebook.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-03T21:46:25.000Z'
originalURL: https://freecodecamp.org/news/think-you-need-a-dashboard-you-should-build-a-notebook-instead-33104d913f95
coverImage: https://cdn-media-1.freecodecamp.org/images/0*iOUCCgSxZ8pwih2L
tags:
- name: analytics
  slug: analytics
- name: big data
  slug: big-data
- name: Data Science
  slug: data-science
- name: Productivity
  slug: productivity
- name: 'tech '
  slug: tech
seo_title: Vous pensez avoir besoin d'un tableau de bord ? Vous devriez plutôt créer
  un notebook.
seo_desc: 'By Mahdi Karabiben

  After first establishing themselves as a key component of the standard Business
  Intelligence model during the first years of the millennium, dashboards were rapidly
  adopted by most companies as the go-to tool to present data-driven...'
---

Par Mahdi Karabiben

Après s'être d'abord établis comme un composant clé du modèle standard de Business Intelligence au cours des premières années du millénaire, les tableaux de bord ont été rapidement adoptés par la plupart des entreprises comme l'outil de référence pour présenter des insights et des indicateurs basés sur les données.

Lorsque Hadoop a été introduit en 2007, son lancement a été suivi par un ensemble de technologies Big Data qui ont radicalement changé la manière dont les choses sont faites en coulisses. Elles ont permis le parallélisme à une échelle auparavant inimaginable. Ces changements ont été, pendant une longue période, limités au stockage et au traitement des données. Changer la manière dont les utilisateurs finaux accédaient aux données semblait être une étape inutile, car les tableaux de bord faisaient toujours du bon travail.

Dans une ère du Big Data qui a complètement changé la manière dont les entreprises traitent leurs données, les tableaux de bord ont réussi à rester la norme *de facto* pour donner un sens aux quantités astronomiques de données produites quotidiennement. La plupart des entreprises proposant des solutions de tableaux de bord ont rapidement adapté leurs produits aux technologies Big Data. Elles ont également offert des connecteurs qui ont permis aux tableaux de bord de rester l'outil incontournable pour comprendre les données.

Mais avec les changements et les améliorations continus des technologies Big Data standard se produisant à un rythme effréné, peut-être est-il temps de mettre à jour l'*expérience utilisateur du Big Data* ?

### Le problème avec les tableaux de bord : vous êtes toujours à la traîne

Lorsqu'ils ont commencé à être intégrés dans les piles technologiques au tournant du siècle, les tableaux de bord répondaient à un besoin clair et cohérent : présenter des KPI et des insights basés sur les données qui offrent des réponses à des questions établies. Ils étaient le portail vers les données de l'entreprise et permettaient aux personnes ayant des rôles et des besoins multiples de comprendre ce que les données avaient à dire. En essence, les tableaux de bord ont d'abord été introduits pour démocratiser la **découverte de données**.

Mais au tournant du siècle, les flux de données étaient très structurés, les données n'avaient pas tant de choses à dire, et la gamme de questions à leur poser était limitée.

Ce n'est plus le cas. Avec la croissance exponentielle des données produites quotidiennement, la valeur de ce nouvel or noir atteint de nouveaux sommets chaque jour. Les volumes de données disponibles pour l'exploitation dans cette ère du Big Data n'offrent pas seulement des réponses à un ensemble spécifique de questions. Ils vous offrent des questions auxquelles vous n'avez pas encore pensé à demander. Cela a conduit à l'essor de l'**exploration de données**, avec des scientifiques des données cherchant à extraire autant de valeur des données que possible.

Compter sur les tableaux de bord pour visualiser et extraire de la valeur de vos données signifie que vous devez utiliser une autre technologie (généralement des **notebooks**) pour les explorer et décider ce qui sera accessible via vos tableaux de bord. Un tel mécanisme signifie que le tableau de bord arrive toujours dans une seconde phase d'extraction de valeur des données. Dans cette ère où les quantités de données disponibles permettent un nombre infini de possibilités en matière d'exploration de données, aucun tableau de bord ne pourrait suffire à extraire toute la valeur que vos données offrent.

Travailler avec ce mécanisme en deux étapes signifie que la collaboration entre différents rôles reste limitée. Cela est dû au fait que les architectures de données deviennent trop complexes en raison du nombre de technologies utilisées par les différents spécialistes des données.

Cette chaîne de personnes utilisant différentes technologies pour différents besoins signifie que, pour ajouter certains insights à un tableau de bord, un analyste de données doit attendre qu'un scientifique des données travaille sur les données via un notebook. À son tour, le scientifique des données peut avoir besoin d'attendre qu'un ingénieur de données fournisse les données dans une certaine structure via un script. Et n'oubliez pas — tout au long de ce processus chronophage, la valeur des données continue de diminuer.

Plusieurs fournisseurs de tableaux de bord ont tenté d'intégrer des capacités d'exploration de données dans leurs plateformes, Tableau offrant notamment [un connecteur Spark impressionnant](https://onlinehelp.tableau.com/current/pro/desktop/en-us/examples_sparksql.htm) qui vous permet d'exécuter des jobs Spark SQL directement depuis votre tableau de bord. Néanmoins, les capacités restent limitées et l'interactivité n'est que partielle, ce qui laisse l'utilisateur final toujours à la traîne.

Que vous utilisiez Kibana, Tableau ou Qlikview, votre tableau de bord peut offrir des insights précieux concernant vos données. Le problème avec de telles technologies est qu'elles ont été conçues avec la découverte de données à l'esprit. Et à cause de cela, elles négligent un élément clé rendu possible à grande échelle dans cette ère du Big Data : l'**exploration de données**.

Alors que les flux de données continuent de croître de manière exponentielle, dédier le portail principal de vos données uniquement aux insights signifie que vous ne lisez que la première page d'un livre très intéressant.

### Les notebooks, et comment ils portent l'interactivité à un niveau complètement nouveau

Comme mentionné ci-dessus, les notebooks sont l'outil standard pour l'exploration de données depuis quelques années. Depuis la sortie de [projet Jupyter](https://jupyter.org/) en 2014, et grâce à l'ensemble des fonctionnalités qu'il offrait en plus de ce qui était déjà disponible via IPython, les notebooks ont attiré les scientifiques des données en tant qu'outil idéal pour l'exploration de données, grâce principalement à un concept clé : **l'interactivité**.

Grâce aux kernels (dans l'écosystème Jupyter) et aux interpréteurs (dans Apache Zeppelin), les notebooks vous permettent d'explorer vos données à travers une multitude de technologies de traitement Big Data. Ils offrent ensuite un accès immédiat aux données via des modules de visualisation intégrés et des mécanismes de sortie. Réunir ces deux capacités dans le même outil est la clé pour utiliser un tel outil à la fois pour la découverte et l'exploration de données.

Les notebooks ne sont pas seulement un outil qui permet un accès direct aux données, ils le font tout en maintenant une interactivité complète. Ils estompent complètement la ligne qui sépare les scientifiques des données et les analystes de données et permettent aux personnes ayant ces deux rôles de collaborer ensemble de manière transparente.

Cela fonctionne parfaitement grâce au protocole puissant sur lequel s'appuient les notebooks et à leur bloc de construction principal, les cellules (paragraphes dans Zeppelin). En offrant plusieurs types de cellules (pour le code et le texte), les notebooks permettent une collaboration efficace.

Pour montrer leur efficacité par rapport aux tableaux de bord, revenons au scénario dont nous avons parlé précédemment. Dans une architecture basée sur des notebooks, lorsqu'un analyste de données a besoin de certains insights dans un notebook, l'ingénieur de données peut ajouter une cellule de code dans laquelle il manipule les données via la technologie de traitement de données adéquate. Ensuite, le scientifique des données utilise ces données dans une autre cellule de code pour extraire les informations souhaitées et offrir le résultat à l'analyste de données. Tout cela se passe sans que l'un de ces trois spécialistes des données ne quitte le notebook.

Dans une ère où le Fast Data est la norme, extraire de la valeur de vos données via un pipeline structuré utilisant différents outils pour chaque étape n'est plus un modèle durable. Les données qui proviennent d'un flux de données en temps réel non structuré peuvent offrir des insights précieux lorsqu'elles sont utilisées pour des processus par lots. Mais elles offrent encore plus de valeur lorsqu'elles sont analysées progressivement via un traitement en temps quasi réel et des tableaux de bord interactifs (c'est-à-dire des notebooks) qui offrent un accès complet aux données brutes et des visualisations sophistiquées.