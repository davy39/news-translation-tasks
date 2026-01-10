---
title: L'essor de l'ingénieur de données
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-01-20T23:44:03.000Z'
originalURL: https://freecodecamp.org/news/the-rise-of-the-data-engineer-91be18f1e603
coverImage: https://cdn-media-1.freecodecamp.org/images/1*j0fTLcAR6HhXmWkcii469Q.jpeg
tags:
- name: big data
  slug: big-data
- name: data
  slug: data
- name: data-engineering
  slug: data-engineering
- name: Data Science
  slug: data-science
- name: 'tech '
  slug: tech
seo_title: L'essor de l'ingénieur de données
seo_desc: 'By Maxime Beauchemin

  I joined Facebook in 2011 as a business intelligence engineer. By the time I left
  in 2013, I was a data engineer.

  I wasn’t promoted or assigned to this new role. Instead, Facebook came to realize
  that the work we were doing trans...'
---

Par Maxime Beauchemin

J'ai rejoint Facebook en 2011 en tant qu'**ingénieur en intelligence économique**. Au moment où je suis parti en 2013, j'étais un **ingénieur de données**.

Je n'ai pas été promu ou affecté à ce nouveau rôle. Au lieu de cela, Facebook a réalisé que le travail que nous faisions transcendait l'intelligence économique classique. Le rôle que nous avions créé pour nous-mêmes était une nouvelle discipline à part entière.

Mon équipe était à l'avant-garde de cette transformation. Nous développions de nouvelles compétences, de nouvelles façons de faire les choses, de nouveaux outils, et — plus souvent qu'autrement — tournions le dos aux méthodes traditionnelles.

Nous étions des pionniers. Nous étions des ingénieurs de données !

### L'ingénierie des données ?

La **science des données** en tant que discipline traversait son adolescence d'affirmation et de définition de soi. En même temps, l'**ingénierie des données** était le frère légèrement plus jeune, mais elle traversait quelque chose de similaire. La discipline de l'ingénierie des données s'inspirait de sa sœur, tout en se définissant en opposition et en trouvant sa propre identité.

Comme les scientifiques des données, les ingénieurs de données écrivent du code. Ils sont hautement analytiques et s'intéressent à la visualisation des données.

Contrairement aux scientifiques des données — et inspirés par notre parent plus mature, le **génie logiciel** — les ingénieurs de données construisent des outils, des infrastructures, des frameworks et des services. En fait, il est soutenable que l'ingénierie des données est beaucoup plus proche du génie logiciel que de la science des données.

En relation avec les **rôles précédemment existants**, le domaine de l'ingénierie des données pourrait être considéré comme un sur-ensemble de l'**intelligence économique** et de l'**entreposage de données** qui apporte plus d'éléments du **génie logiciel**. Cette discipline intègre également une spécialisation autour de l'exploitation des systèmes distribués dits de « big data », ainsi que des concepts autour de l'écosystème étendu de Hadoop, du traitement en flux, et du calcul à grande échelle.

Dans les petites entreprises — où aucune équipe d'**infrastructure de données** n'a encore été formalisée — le rôle de l'ingénieur de données peut également couvrir la charge de travail autour de la mise en place et de l'exploitation de l'infrastructure de données de l'organisation. Cela inclut des tâches comme la mise en place et l'exploitation de plateformes comme Hadoop/Hive/HBase, Spark, et autres.

Dans les petits environnements, les gens tendent à utiliser des services hébergés offerts par Amazon ou Databricks, ou à obtenir du soutien de sociétés comme Cloudera ou Hortonworks — ce qui sous-traite essentiellement le rôle de l'ingénieur de données à d'autres entreprises.

Dans les grands environnements, il tend à y avoir une spécialisation et la création d'un rôle formel pour gérer cette charge de travail, à mesure que le besoin d'une équipe d'infrastructure de données grandit. Dans ces organisations, le rôle d'automatiser certains des processus d'ingénierie des données incombe à la fois aux équipes d'ingénierie des données et d'infrastructure de données, et il est courant que ces équipes collaborent pour résoudre des problèmes de niveau supérieur.

Alors que l'aspect ingénierie du rôle prend de l'ampleur, d'autres aspects du rôle initial de l'ingénierie économique deviennent secondaires. Des domaines comme la création et la maintenance de portefeuilles de rapports et de tableaux de bord ne sont pas le focus principal d'un ingénieur de données.

Nous avons maintenant de meilleurs outils en libre-service où les analystes, les scientifiques des données et le général « travailleur de l'information » deviennent plus compétents en données et peuvent prendre en charge la consommation de données de manière autonome.

#### L'ETL est en train de changer

Nous avons également observé un changement général loin des outils de glisser-déposer [ETL (Extract Transform and Load)](https://en.wikipedia.org/wiki/Extract,_transform,_load) vers une approche plus programmatique. La connaissance des produits sur des plateformes comme Informatica, IBM Datastage, Cognos, AbInitio ou Microsoft SSIS n'est pas courante parmi les ingénieurs de données modernes, et est remplacée par des compétences plus génériques en génie logiciel ainsi que par la compréhension de plateformes programmatiques ou pilotées par configuration comme Airflow, Oozie, Azkabhan ou Luigi. Il est également assez courant pour les ingénieurs de développer et de gérer leur propre orchestrateur/planificateur de tâches.

Il y a une multitude de raisons pour lesquelles des morceaux complexes de logiciels ne sont pas développés en utilisant des outils de glisser-déposer : c'est que finalement le **code** est la meilleure abstraction qui soit pour le logiciel. Bien qu'il soit hors de portée de cet article d'argumenter sur ce sujet, il est facile de déduire que ces mêmes raisons s'appliquent à l'écriture d'ETL comme à tout autre logiciel. Le code permet des niveaux arbitraires d'abstractions, permet toutes les opérations logiques de manière familière, s'intègre bien avec le contrôle de source, est facile à versionner et à collaborer. Le fait que les outils ETL aient évolué pour exposer des interfaces graphiques semble être un détour dans l'histoire du traitement des données, et ferait certainement l'objet d'un article de blog intéressant en soi.

Soulignons le fait que les abstractions exposées par les outils ETL traditionnels sont hors cible. Certes, il y a un besoin d'abstraire la complexité du traitement des données, du calcul et du stockage. Mais je soutiendrais que la solution n'est pas d'exposer des primitives ETL (comme source/cible, agrégations, filtrage) dans un format glisser-déposer. Les abstractions nécessaires sont d'un niveau supérieur.

Par exemple, un exemple d'abstraction nécessaire dans un environnement de données moderne est la configuration des expériences dans un framework de test A/B : *quelles sont toutes les expériences ? quels sont les traitements associés ? quel pourcentage d'utilisateurs devrait être exposé ? quelles sont les métriques que chaque expérience s'attend à affecter ? quand l'expérience prend-elle effet ?* Dans cet exemple, nous avons un framework qui reçoit des entrées précises et de haut niveau, effectue des calculs statistiques complexes et livre des résultats calculés. Nous nous attendons à ce que l'ajout d'une entrée pour une nouvelle expérience entraîne des calculs supplémentaires et des résultats livrés. Ce qui est important à noter dans cet exemple, c'est que les paramètres d'entrée de cette abstraction ne sont pas ceux offerts par un outil ETL traditionnel, et que la construction d'une telle abstraction dans une interface glisser-déposer ne serait pas gérable.

Pour un ingénieur de données moderne, les outils ETL traditionnels sont largement **obsolètes** parce que la logique ne peut pas être exprimée en utilisant du code. Par conséquent, les abstractions nécessaires ne peuvent pas être exprimées de manière intuitive dans ces outils. Sachant maintenant que le rôle de l'ingénieur de données consiste largement à définir l'ETL, et sachant qu'un ensemble complètement nouveau d'outils et de méthodologies est nécessaire, on peut soutenir que cela force la discipline à se reconstruire à partir de zéro. Nouvelle pile, nouveaux outils, un nouvel ensemble de contraintes, et dans de nombreux cas, une nouvelle génération d'individus.

#### La modélisation des données est en train de changer

Les techniques typiques de modélisation des données — comme le [schéma en étoile](https://en.wikipedia.org/wiki/Star_schema) — qui définissaient notre approche de la modélisation des données pour les charges de travail analytiques typiquement associées aux entrepôts de données, sont moins pertinentes qu'elles ne l'étaient. Les meilleures pratiques traditionnelles de l'entreposage de données perdent du terrain sur une pile en mutation. Le stockage et le calcul sont moins chers que jamais, et avec l'avènement des bases de données distribuées qui s'adaptent linéairement, la ressource la plus rare est le temps d'ingénierie.

Voici quelques changements observés dans les techniques de modélisation des données :

* **dénormalisation** supplémentaire : maintenir des [clés de substitution](http://www.kimballgroup.com/1998/05/surrogate-keys/) dans les dimensions peut être délicat, et cela rend les tables de faits moins lisibles. L'utilisation de clés naturelles, lisibles par l'homme, et d'attributs de dimension dans les tables de faits devient plus courante, réduisant le besoin de jointures coûteuses qui peuvent être lourdes sur les bases de données distribuées. Notez également que le support de l'encodage et de la compression dans les formats de sérialisation comme Parquet ou ORC, ou dans les moteurs de base de données comme Vertica, adresse la plupart des pertes de performance qui seraient normalement associées à la dénormalisation. Ces systèmes ont été conçus pour normaliser les données pour le stockage par eux-mêmes.
* **blobs** : les bases de données modernes ont un support croissant pour les blobs grâce à des types et fonctions natifs. Cela ouvre de nouvelles possibilités dans le manuel du modélisateur de données, et peut permettre aux tables de faits de stocker plusieurs grains à la fois lorsque cela est nécessaire.
* **schémas dynamiques** : depuis l'avènement de map reduce, avec la popularité croissante des magasins de documents et avec le support des blobs dans les bases de données, il devient plus facile de faire évoluer les schémas de base de données sans exécuter de [DML](https://en.wikipedia.org/wiki/Data_definition_language). Cela facilite une approche itérative de l'entreposage de données et supprime le besoin d'obtenir un consensus complet et une adhésion préalable au développement.
* **snapshotting** systématiquement les dimensions (stocker une copie complète de la dimension pour chaque cycle de planification ETL, généralement dans des partitions de table distinctes) en tant que moyen générique de gérer les [dimensions à changement lent](https://en.wikipedia.org/wiki/Slowly_changing_dimension) (SCD) est une approche générique simple qui nécessite peu d'efforts d'ingénierie, et qui, contrairement à l'approche classique, est facile à comprendre lors de l'écriture d'ETL et de requêtes. Il est également facile et relativement peu coûteux de dénormaliser les attributs de la dimension dans la table de faits pour suivre sa valeur au moment de la transaction. En rétrospective, les techniques de modélisation SCD complexes ne sont pas intuitives et réduisent l'accessibilité.
* **conformité**, comme dans les [dimensions conformes](http://www.kimballgroup.com/data-warehouse-business-intelligence-resources/kimball-techniques/dimensional-modeling-techniques/conformed-dimension/) et les métriques, est toujours extrêmement importante dans un environnement de données moderne, mais avec le besoin pour les entrepôts de données de se déplacer rapidement, et avec plus d'équipes et de rôles invités à contribuer à cet effort, c'est moins impératif et plus un compromis. Le consensus et la convergence peuvent se produire en tant que processus de fond dans les domaines où le point de douleur de la divergence devient ingérable.

De plus, plus généralement, il est soutenable de dire qu'avec la marchandisation des cycles de calcul et avec plus de personnes compétentes en données qu'avant, il y a moins besoin de précalculer et de stocker les résultats dans l'entrepôt. Par exemple, vous pouvez avoir un travail Spark complexe qui peut calculer des analyses complexes à la demande uniquement, et ne pas être planifié pour faire partie de l'entrepôt.

### Rôles et responsabilités

#### L'entrepôt de données

*Un entrepôt de données est une copie des données transactionnelles spécifiquement structurées pour la requête et l'analyse.* — Ralph Kimball

*Un entrepôt de données est une collection de données orientée sujet, intégrée, variante dans le temps et non volatile en soutien au processus de prise de décision de la direction.* — Bill Inmon

L'entrepôt de données est tout aussi pertinent qu'il ne l'a jamais été, et les ingénieurs de données sont responsables de nombreux aspects de sa construction et de son exploitation. Le point focal de l'ingénieur de données est l'entrepôt de données et gravite autour de celui-ci.

L'entrepôt de données moderne est une institution plus publique qu'historiquement, accueillant les scientifiques des données, les analystes et les ingénieurs logiciels pour participer à sa construction et à son exploitation. Les données sont simplement trop centrales pour l'activité de l'entreprise pour avoir des limitations autour des rôles qui peuvent gérer son flux. Bien que cela permette de s'adapter aux besoins de données de l'organisation, cela entraîne souvent une infrastructure beaucoup plus chaotique, en constante évolution et imparfaite.

L'équipe d'ingénierie des données possédera souvent des zones certifiées et de haute qualité dans l'entrepôt de données. Chez Airbnb, par exemple, il existe un ensemble de schémas « core » qui sont gérés par l'équipe d'ingénierie des données, où les accords de niveau de service (SLA) sont clairement définis et mesurés, les conventions de nommage sont strictement suivies, les métadonnées commerciales et la documentation sont de la plus haute qualité, et le code de pipeline associé suit un ensemble de meilleures pratiques bien définies.

Il devient également le rôle de l'équipe d'ingénierie des données d'être un « centre d'excellence » par le biais de la définition de normes, de meilleures pratiques et de processus de certification pour les objets de données. L'équipe peut évoluer pour participer ou diriger un programme d'éducation partageant ses compétences clés pour aider les autres équipes à devenir de meilleurs citoyens de l'entrepôt de données. Par exemple, Facebook dispose d'un programme d'éducation « data camp » et Airbnb développe un programme similaire « Data University » où les ingénieurs de données dirigent des sessions qui enseignent aux gens comment être compétents avec les données.

Les ingénieurs de données sont également les « bibliothécaires » de l'entrepôt de données, cataloguant et organisant les métadonnées, définissant les processus par lesquels on dépose ou extrait des données de l'entrepôt. Dans un écosystème de données en croissance rapide, en évolution rapide et légèrement chaotique, la gestion des métadonnées et les outils deviennent un composant vital d'une plateforme de données moderne.

#### Optimisation et réglage des performances

Avec les données devenant plus stratégiques que jamais, les entreprises développent des budgets impressionnants pour leur infrastructure de données. Cela rend de plus en plus rationnel pour les ingénieurs de données de consacrer des cycles à l'optimisation et au réglage des performances du traitement et du stockage des données. Comme les budgets ne diminuent que rarement dans ce domaine, l'optimisation provient souvent de la perspective d'accomplir plus avec la même quantité de ressources ou d'essayer de linéariser la croissance exponentielle de l'utilisation des ressources et des coûts.

Sachant que la complexité de la pile d'ingénierie des données explose, nous pouvons supposer que la complexité de l'optimisation de cette pile et des processus peut être tout aussi difficile. Là où il peut être facile d'obtenir des gains énormes avec peu d'efforts, les lois des rendements décroissants s'appliquent généralement.

Il est définitivement dans l'intérêt de l'ingénieur de données de construire une infrastructure qui s'adapte à l'entreprise, et d'être conscient des ressources à tout moment.

#### Intégration des données

L'intégration des données, la pratique derrière l'intégration des entreprises et des systèmes par l'échange de données, est aussi importante et aussi difficile qu'elle ne l'a jamais été. Alors que le [Logiciel en tant que Service (SaaS)](https://en.wikipedia.org/wiki/Software_as_a_service) devient la nouvelle norme pour les entreprises, le besoin de synchroniser les données de référence à travers ces systèmes devient de plus en plus critique. Non seulement le SaaS a besoin de données à jour pour fonctionner, mais nous voulons souvent ramener les données générées de leur côté dans notre entrepôt de données afin qu'elles puissent être analysées avec le reste de nos données. Bien sûr, le SaaS a souvent ses propres offres d'analyse, mais manque systématiquement de la perspective que le reste des données de votre entreprise offre, donc plus souvent qu'autrement, il est nécessaire de récupérer une partie de ces données.

Laisser ces offres SaaS redéfinir les données de référence sans intégration et partage d'une clé primaire commune est un désastre qui doit être évité à tout prix. Personne ne veut maintenir manuellement deux listes d'employés ou de clients dans 2 systèmes différents, et pire encore : devoir faire de la correspondance floue lors du retour de leurs données RH dans leur entrepôt.

Pire encore, les dirigeants d'entreprise signent souvent des accords avec des fournisseurs de SaaS sans vraiment considérer les défis de l'intégration des données. La charge de travail d'intégration est systématiquement minimisée par les vendeurs pour faciliter leurs ventes, et laisse les ingénieurs de données coincés à faire un travail non comptabilisé et sous-estimé. Sans parler du fait que les API SaaS typiques sont souvent mal conçues, mal documentées et « agiles » : ce qui signifie que vous pouvez vous attendre à ce qu'elles changent sans préavis.

#### Services

Les ingénieurs de données opèrent à un niveau d'abstraction plus élevé et, dans certains cas, cela signifie fournir des services et des outils pour automatiser le type de travail que les ingénieurs de données, les scientifiques des données ou les analystes peuvent faire manuellement.

Voici quelques exemples de services que les ingénieurs de données et les ingénieurs d'infrastructure de données peuvent construire et exploiter.

* ingestion de données : services et outils autour du « scraping » de bases de données, chargement de logs, récupération de données depuis des magasins ou API externes, …
* calcul de métriques : frameworks pour calculer et résumer les métriques liées à l'engagement, la croissance ou la segmentation
* détection d'anomalies : automatisation de la consommation de données pour alerter les personnes lorsque des événements anormaux se produisent ou lorsque les tendances changent de manière significative
* gestion des métadonnées : outils permettant la génération et la consommation de métadonnées, facilitant la recherche d'informations dans et autour de l'entrepôt de données
* expérimentation : les frameworks de test A/B et d'expérimentation sont souvent une pièce critique de l'analyse des entreprises avec une composante significative d'ingénierie des données
* instrumentation : l'analyse commence par la journalisation des événements et des attributs liés à ces événements, les ingénieurs de données ont un intérêt à s'assurer que des données de haute qualité sont capturées en amont
* sessionisation : pipelines spécialisés dans la compréhension des séries d'actions dans le temps, permettant aux analystes de comprendre les comportements des utilisateurs

Tout comme les ingénieurs logiciels, les ingénieurs de données devraient constamment chercher à automatiser leurs charges de travail et à construire des abstractions qui leur permettent de gravir l'échelle de la complexité. Bien que la nature des flux de travail qui peuvent être automatisés diffère en fonction de l'environnement, le besoin de les automatiser est commun à tous.

### Compétences requises

**Maîtrise de SQL** : si l'anglais est la langue des affaires, SQL est la langue des données. À quel point pouvez-vous être un homme d'affaires réussi si vous ne parlez pas bien anglais ? Alors que les générations de technologies vieillissent et s'estompent, SQL reste solidement la lingua franca des données. Un ingénieur de données devrait être capable d'exprimer tout degré de complexité en SQL en utilisant des techniques comme les « sous-requêtes corrélées » et les fonctions de fenêtre. Les primitives SQL/DML/DDL sont suffisamment simples pour ne pas avoir de secrets pour un ingénieur de données. Au-delà de la nature déclarative de SQL, il/elle devrait être capable de lire et de comprendre les plans d'exécution de la base de données, et avoir une compréhension de ce que sont toutes les étapes, comment les indices fonctionnent, les différents algorithmes de jointure et la dimension distribuée dans le plan.

**Techniques de modélisation des données** : pour un ingénieur de données, la modélisation entité-relation devrait être un réflexe cognitif, ainsi qu'une compréhension claire de la normalisation, et avoir une intuition aiguë autour des compromis de dénormalisation. L'ingénieur de données devrait être familier avec la [modélisation dimensionnelle](https://en.wikipedia.org/wiki/Dimensional_modeling) et les concepts et le champ lexical associés.

**Conception ETL** : écrire des ETL efficaces, résilients et « évolutifs » est essentiel. Je prévois d'approfondir ce sujet dans un prochain article de blog.

**Projections architecturales** : comme tout professionnel dans un domaine d'expertise donné, l'ingénieur de données a besoin d'avoir une compréhension de haut niveau de la plupart des outils, plateformes, bibliothèques et autres ressources à sa disposition. Les propriétés, cas d'utilisation et subtilités derrière les différentes saveurs de bases de données, moteurs de calcul, processeurs de flux, files de messages, orchestrateurs de flux de travail, formats de sérialisation et autres technologies connexes. Lors de la conception de solutions, il/elle devrait être capable de faire de bons choix quant aux technologies à utiliser et avoir une vision de la manière de les faire fonctionner ensemble.

### En résumé

Au cours des 5 dernières années à travailler dans la Silicon Valley chez Airbnb, Facebook et Yahoo!, et ayant interagi abondamment avec des équipes de données de tous types travaillant pour des entreprises comme Google, Netflix, Amazon, Uber, Lyft et des dizaines d'entreprises de toutes tailles, j'observe un consensus croissant sur ce que l'« ingénierie des données » évolue, et j'ai ressenti le besoin de partager certaines de mes découvertes.

J'espère que cet article pourra servir de sorte de manifeste pour l'ingénierie des données, et j'espère susciter des réactions de la communauté opérant dans les domaines connexes !