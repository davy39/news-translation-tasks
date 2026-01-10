---
title: Bases de données de graphes VS Bases de données relationnelles – Découvrez
  comment fonctionne une base de données de graphes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-09-09T17:16:35.000Z'
originalURL: https://freecodecamp.org/news/graph-database-vs-relational-database
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/f2fb45ed-48ce-4469-927f-d295b82d9f98.png
tags:
- name: database
  slug: database
- name: graph database
  slug: graph-database
seo_title: Bases de données de graphes VS Bases de données relationnelles – Découvrez
  comment fonctionne une base de données de graphes
seo_desc: "By Ljubica Lazarevic\nIf you're curious about graph databases and how they\
  \ compare with relational database management systems, then this beginner-friendly\
  \ guide is for you. \nIn this article, you'll discover of the power of graphs by\
  \ working with a sm..."
---

Par Ljubica Lazarevic

Si vous êtes curieux au sujet des bases de données de graphes et de leur comparaison avec les systèmes de gestion de bases de données relationnelles, alors ce guide pour débutants est fait pour vous. 

Dans cet article, vous découvrirez la puissance des graphes en travaillant avec un petit ensemble de données de films. Il est basé sur le [jeu de données intégré et le guide](https://neo4j.com/developer/example-data/) disponibles sur le [Neo4j Sandbox](https://dev.neo4j.com/try).

Vous voulez vous lancer directement et essayer par vous-même ? Allez-y ! Vous trouverez des instructions sur la façon de [commencer ici](https://lju.medium.com/getting-started-with-play-movies-251228c12f2c).

![Image](https://www.freecodecamp.org/news/content/images/2021/09/movie-image.png)

## Ce que nous allons couvrir dans cet article

Les bases de données de graphes gagnent en popularité et en adoption. Avec des quantités de données toujours plus importantes provenant de nombreuses sources différentes, il est crucial de pouvoir comprendre les données et de voir comment elles sont toutes connectées. 

Si vous souhaitez en savoir plus sur les types de problèmes que les bases de données de graphes aident à résoudre, et comment vous pourriez repérer une bonne application pour l'une d'entre elles, voici un [article de blog introductif](https://medium.com/geekculture/spotting-a-graph-shaped-problem-b1f126bf8c03). 

Certains d'entre vous qui lisent cet article ont peut-être entendu parler des bases de données de graphes (GDB), d'autres peut-être pas. Dans cet article, nous allons couvrir exactement ce qu'elles sont, et comment elles se comparent aux systèmes de gestion de bases de données relationnelles (RDBMS), plus traditionnels, qui ont été l'application logicielle phare des 40 dernières années. 

Inspiré par un petit ensemble de données de films utilisé par Neo4j comme introduction guidée à l'interrogation de graphes, nous allons examiner des exemples et des équivalents côte à côte de ce à quoi ressemblerait un modèle de données ou une requête dans une base de données de graphes et une base de données relationnelle.

Dans cet article, nous allons :

* Présenter les bases de données de graphes, en couvrant brièvement les deux modèles qui existent
* Jeter un regard conceptuel sur les différences entre les paradigmes relationnels et de graphes
* Examiner l'ensemble de données de films, et comparer et contraster les modèles de données d'un point de vue GDB et RDBMS
* Comparer et contraster certaines requêtes, basées soit sur Cypher (pour GDB), soit sur SQL
* Parler des requêtes les plus intéressantes qui apparaissent dans l'exemple de film, et décomposer exactement ce qui se passe

Si vous souhaitez essayer l'exemple de parcours de l'ensemble de données de films avant de lire l'article (ou pendant !), vous êtes plus que bienvenu de le faire. Vous pouvez en savoir plus [ici](https://medium.com/neo4j/getting-started-with-play-movies-251228c12f2c).

## Qu'est-ce qu'une base de données de graphes ?

Tout d'abord, avant de plonger dans ce qu'est une base de données de graphes, définissons le terme. Les bases de données de graphes sont un type de magasin de données "Not only SQL" (NoSQL). Elles sont conçues pour stocker et récupérer des données dans une structure de graphe. 

Le mécanisme de stockage utilisé peut varier d'une base de données à l'autre. Certaines GDB peuvent utiliser des constructions de base de données plus traditionnelles, telles que basées sur des tables, et avoir ensuite une couche d'API de graphe par-dessus. 

D'autres seront des GDB "natives" – où toute la construction de la base de données, du stockage à la gestion et à la requête, maintient la structure de graphe des données. De nombreuses bases de données de graphes actuellement disponibles le font en traitant les relations entre entités comme des citoyens de première classe.

### Différents types de bases de données de graphes

Il existe deux types de GDB : les bases de données de graphes RDF/triple stores/sémantiques et les bases de données de graphes de propriétés. 

Une GDB RDF utilise le concept de triple, qui est une déclaration composée de trois éléments : sujet-prédicat-objet. 

Le sujet sera une ressource ou des nœuds dans le graphe, l'objet sera un autre nœud ou une valeur littérale, et le prédicat représente la relation entre le sujet et l'objet. Il n'y a pas de structures internes sur les nœuds ou les relations, et tout est identifié par un identifiant unique, sous la forme d'un URI. 

La motivation derrière cette structure est l'échange et la publication de données. Pour en savoir plus sur cette structure, je vous renvoie au travail de [Jesus Barrasa](https://jbarrasa.com/2016/11/17/neo4j-is-your-rdf-store-part-1/) dans ce domaine. 

Une GDB de propriétés se concentre sur le concept de stockage de données proches du modèle logique. Cela sera basé sur les questions posées aux données elles-mêmes, et se concentre sur la représentation la plus efficace possible pour le stockage et l'interrogation. 

Contrairement à un graphe basé sur RDF, il existe des structures internes sur les nœuds et les relations, ce qui permet une représentation riche des données ainsi que des métadonnées associées. 

Les deux diagrammes suivants fournissent une comparaison côte à côte de données d'exemple représentées dans une base de données de graphes de propriétés et sous forme de graphe RDF – tous deux représentant la personne Tom Hanks, jouant le rôle de Jim Lovell, dans le film Apollo 13.

![Image](https://lh3.googleusercontent.com/v4SPvkCESPh7JmNx1ibALZTHEb0ILjPjN2xR7Y_62TTaHkM8lMuErmqzRMcdAUIkL3nz1lqYlrlQl24J_B_-Oa9K-dk7yy1GsRRXPpW5tVCMzcQ6tgMwf0sgE-XGbCfnf8Wlaqs0=s0)
_Exemple RDF de Tom Hanks dans Apollo 13_

![Image](https://lh5.googleusercontent.com/EW8G0eS4Luh9jykxFBvFA3CvFr9ivvbUDaspOwSL7gxuGx-N-eswCoZJjJiAdgo1x2k0eYTa55YeOaFXbfSYKywPW4mI_Di_NB-nTOwnHztaYVBBPVaecrG83es3DlT_PLskbf1b=s0)
_Exemple de graphe de propriétés de Tom Hanks dans Apollo 13_

##   
Anatomie d'une base de données de graphes de propriétés

Pour le reste de cet article, nous allons nous concentrer sur les bases de données de graphes de propriétés natives, spécifiquement Neo4j. Examinons les principaux composants. 

Les principaux composants d'une base de données de graphes de propriétés sont les suivants :

* Nœud : également connu sous le nom de sommet en théorie des graphes – l'élément de données principal à partir duquel les graphes sont construits
* Relation : également connue sous le nom d'arête en théorie des graphes – un lien entre deux nœuds. Elle aura une **direction** et un **type**. Un nœud sans relations est autorisé, une relation sans deux nœuds ne l'est pas

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-40.png)
_Nœud et Relation_

* Étiquette : Définit une catégorie de nœud, un nœud peut en avoir plusieurs
* Propriété : Enrichit un nœud ou une relation, pas besoin de valeurs nulles !

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-39.png)
_Étiquette, Type et Propriété_

## Bases de données de graphes vs Bases de données relationnelles

### Récapitulatif des bases de données relationnelles

De nombreux développeurs sont familiers avec la base de données relationnelle traditionnelle, où les données sont stockées dans des tables au sein d'un schéma bien défini. 

Chaque ligne dans la table est une entité discrète de données. L'un de ces éléments dans la ligne est généralement utilisé pour définir son unicité : la clé primaire. Il pourrait s'agir d'un identifiant unique ou peut-être d'un numéro de sécurité sociale pour une personne.

Nous passons ensuite par un processus appelé normalisation pour réduire la répétition des données. Dans la normalisation, nous déplaçons les références, comme une adresse pour une personne, dans une autre table. Ainsi, nous obtenons une référence de la ligne représentant l'entité à la ligne représentant l'adresse de cette personne.

Si, par exemple, quelqu'un change d'adresse, vous ne voudriez pas avoir plusieurs versions des adresses de cette personne partout et devoir essayer de vous souvenir de toutes les différentes instances où les adresses de cette personne existent. La normalisation garantit que vous avez une seule version des données, afin que vous puissiez effectuer les mises à jour en un seul endroit.

Ensuite, lorsque nous interrogeons, nous voulons reconstituer ces données normalisées. Nous faisons ce qu'on appelle une opération de JOIN. 

Dans notre ligne d'entité principale, nous avons la clé primaire qui identifie l'ID de l'entité, disons la personne. Nous avons également ce qu'on appelle une clé étrangère qui représente une ligne dans notre table d'adresses. Nous joignons les deux tables par leurs clés primaires et étrangères, et utilisons cela pour rechercher l'adresse dans la table d'adresses. Cela s'appelle un JOIN et ces JOINs sont effectués au moment de la requête et au moment de la lecture.

Lorsque nous effectuons un JOIN dans une base de données relationnelle, il s'agit d'une opération de comparaison d'ensembles où nous cherchons à voir où nos deux ensembles de données se chevauchent (dans ce cas, les ensembles sont la table des personnes et la table des adresses). À un niveau élevé, c'est ainsi que fonctionnent les bases de données relationnelles traditionnelles.

![Image](https://lh5.googleusercontent.com/VTc6WHaERtCGkdAxZOgAuN74-isXFuHQjAQL7cxXFZCntCHD3q86FBCkuUCOoRhfq_wwxRR4yd0y2XYrM3dG7CPyG0s7HukFfme1k-gU2il3HiQVlkTz9w3hzYJZhaD9Lzeow3M4=s0)
_Un exemple des tables trouvées et de leur correspondance dans une base de données relationnelle pour une base de données d'assurance_



![Image](https://lh4.googleusercontent.com/fRaKUVtGKp9TABKWcNfyy1CkZohxeC-5mf5FxbHF00xxh-_SsRdDqyVJ31ViXib8WdVvtWS7W2sZi4XS3SzcavlFvTW3-c8SEovdSWP3s4n6--pCRJ-w6FoQ53lgxAT455HWY29R=s0)
_L'équivalent de la base de données d'assurance dans une base de données de graphes de propriétés_

### Comment fonctionnent les bases de données de graphes natives : Connexions et Adjacence sans index

Jetons un rapide coup d'œil à une base de données de graphes native et à son fonctionnement. 

Nous avons parlé de l'entité discrète dans une base de données relationnelle étant une ligne au sein d'une table. Dans une base de données de graphes native, cette ligne serait l'équivalent d'un nœud. C'est toujours une entité discrète, donc nous avons toujours cet élément de normalisation.

Un nœud serait une entité. Si nous avions des nœuds de personnes, nous aurions un nœud pour une personne. Et nous aurions un certain degré d'unicité, disons le numéro de sécurité sociale. 

La différence clé, cependant, est lorsque nous connectons ce nœud de personne à une autre entité discrète – par exemple, une adresse – nous créons une connexion physique (aka relation) entre ces deux points.

L'adresse aurait un pointeur qui indique, quelle est la partie sortante de la relation qui se connecte au nœud ? Nous avons ensuite un autre pointeur pour la partie entrante de la relation pointant vers l'autre nœud. 

Ainsi, effectivement, nous collectons un ensemble de pointeurs, et c'est une manifestation de la connexion physique entre ces deux entités. C'est la grande différence.

Dans une base de données relationnelle, vous reconstitueriez les données avec des jointures à la lecture, ce qui signifie qu'au moment de la requête, elle irait essayer de comprendre comment les choses se cartographient ensemble.

Dans une base de données de graphes, puisque nous savons déjà que ces deux éléments sont connectés, nous n'avons pas besoin de rechercher la cartographie au moment de la requête. Tout ce que nous faisons est de suivre les relations stockées vers les autres nœuds. 

C'est ce que nous appelons l'adjacence sans index. Ce concept d'adjacence sans index est clé pour comprendre les optimisations de performance d'une base de données de graphes native par rapport à d'autres systèmes de bases de données.

L'adjacence sans index signifie que lors d'un parcours local de graphe, en suivant ces pointeurs (relations) qui connectent les nœuds dans mon graphe, la performance de l'opération ne dépend pas de la taille globale du graphe. Elle dépend du nombre de relations connectées aux nœuds que vous parcourez.

Lorsque nous parlons d'un JOIN comme une opération d'ensemble (intersection), nous utilisons un index dans une base de données relationnelle pour voir où ces deux ensembles se chevauchent. Cela signifie que la performance de l'opération de JOIN commence à ralentir à mesure que les tables deviennent plus grandes. 

En termes de notation Big O, cela ressemble à une croissance logarithmique utilisant un index – quelque chose comme O(log n) et croît également de manière exponentielle avec le nombre de JOINs dans votre requête.

D'autre part, le parcours des relations dans le graphe est plus une croissance linéaire basée sur le nombre de relations dans les nœuds que nous parcourons réellement, et non sur la taille globale du graphe.

C'est l'optimisation fondamentale du temps de requête que les bases de données de graphes réalisent pour nous donner l'adjacence sans index. D'un point de vue performance, c'est vraiment la chose la plus importante à considérer lorsque nous pensons à une base de données de graphes native.

## Une brève introduction au graphe de films

Nous avons parlé des différences théoriques entre une base de données de graphes et une base de données relationnelle. Maintenant, commençons à regarder quelques comparaisons côte à côte.

Le graphe de films se compose d'un ensemble de données comprenant des acteurs, des réalisateurs, des producteurs, des scénaristes, des critiques et des films, ainsi que des informations sur la manière dont ils sont tous connectés les uns aux autres.  

Cet ensemble de données est disponible dans Neo4j Browser et peut être facilement déclenché en utilisant la commande `:PLAY movies`. Pour rappel, voici un blog pour vous montrer [comment commencer](https://medium.com/neo4j/getting-started-with-play-movies-251228c12f2c). 

L'ensemble de données Movies se compose de :

* 133 nœuds/entités Person
* 38 nœuds/entités Movie
* 253 relations/connexions entre les entités ci-dessus, décrivant des connexions telles que :
* Personne(s) qui a réalisé un Film
* Personne(s) qui a joué dans un Film et rôle(s) joué(s)
* Personne(s) qui a écrit un Film
* Personne(s) qui a produit un Film
* Personne(s) qui a critiqué un Film et note et résumé donnés
* Personne(s) qui suit une autre Personne

Bien qu'il s'agisse d'un ensemble de données relativement petit, il décrit de manière exhaustive la puissance des graphes.

### Comparaison des modèles de données

Tout d'abord, jetons un coup d'œil aux modèles de données de nos bases de données respectives. Comme pour tous les modèles de données, leur apparence dépendra finalement des types de questions que vous posez. Supposons donc que nous allons poser les types de questions suivants :

* Quels films une personne a-t-elle joués ?
* Quels films une personne a-t-elle en relation ?
* Qui sont tous les co-acteurs avec lesquels une personne a déjà travaillé ?

Sur la base de ces questions, voici les modèles de données potentiels associés :

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-37.png)
_Modèle de données Entity Relationship pour le graphe de films_

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-41.png)
_Modèle de données Property Graph pour le graphe de films_

Vous remarquerez immédiatement quelque chose – ces identifiants ont disparu ! Comme nous connectons les données dès que nous savons qu'il y a une connexion, nous n'avons plus besoin d'eux, ni de ces tables de mappage pour nous indiquer comment différentes lignes de données se connectent.

### Comparaison des requêtes

Passons maintenant à la comparaison de certaines requêtes. En prenant quelques-unes des premières requêtes de l'exemple `:PLAY movies`, examinons quelques comparaisons côte à côte de la requête Cypher et de ce à quoi ressemblerait la requête SQL équivalente.

Qu'est-ce que Cypher, me demanderez-vous ? [Cypher est un langage de requête de graphes](https://neo4j.com/developer/cypher/) qui est utilisé pour interroger la base de données de graphes Neo4j. Il existe également une version [OpenCypher](https://opencypher.org/), qui est utilisée par un certain nombre d'autres fournisseurs.

Alors que nous passons en revue les requêtes, cela devrait devenir plus clair comment une base de données de graphes, accompagnée d'un langage de requête pour aider à explorer les relations, commence vraiment à se démarquer. Commençons à chercher Tom Hanks !

#### Comment trouver Tom Hanks

```cypher
MATCH (p:Person {name: "Tom Hanks"})
RETURN p
```

```sql
SELECT * FROM person 
WHERE person.name = "Tom Hanks"
```

#### Comment trouver les films de Tom Hanks

```cypher
MATCH (:Person {name: "Tom Hanks"})-->(m:Movie)
RETURN m.title
```

```sql
SELECT movie.title FROM movie
INNER JOIN movie_person ON movie.movie_id = person_movie.movie_id
INNER JOIN person ON person_movie.person_id = person.person_id
WHERE person.name = "Tom Hanks"
```

#### Comment trouver les films réalisés par Tom Hanks

```cypher
MATCH (:Person {name: "Tom Hanks"})-[:DIRECTED]->(m:Movie)
RETURN m.title
```

```sql
SELECT movie.title FROM movie
INNER JOIN person_movie ON movie.movie_id = person_movie.movie_id
INNER JOIN person ON person_movie.person_id = person.person_id
INNER JOIN involvement ON person_movie.involve_id = involvement.involve_id
WHERE person.name = "Tom Hanks" AND involvement.title = "Director"
```

#### Comment trouver les co-acteurs de Tom Hanks

```cypher
MATCH (:Person {name: "Tom Hanks"})-->(:Movie)<-[:ACTED_IN]-(coActor:Person)
RETURN coActor.name
```

```sql
WITH tom_movies AS (
    SELECT movie.movie_id FROM movie
    INNER JOIN person_movie ON movie.movie_id = person_movie.movie_id
    INNER JOIN person ON person_movie.person_id = person.person_id
    WHERE person.name = "Tom Hanks")
SELECT person.name FROM person
INNER JOIN person_movie ON tom_movies = person_movie.movie_id
INNER JOIN person ON person_movie.person_id = person.person_id
INNER JOIN involvement ON person_movie.involve_id = involvement.involve_id
WHERE involvement.title = "Actor"
```

## Plus de requêtes avec Cypher

Espérons que vous aurez compris l'idée des différences entre les requêtes Cypher et SQL. Peut-être êtes-vous excité à l'idée d'en apprendre plus sur elles aussi ! Nous aurons quelques références plus loin dans l'article de blog. 

Pour l'instant, jetons un coup d'œil à certaines des autres requêtes Cypher que vous pouvez trouver dans l'exemple de graphe `:PLAY movies`, et expliquons ce qui se passe.

Aucun graphe de films ne serait complet sans la question quintessentielle du [nombre de Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon), et notre graphe de films ne fait pas exception ! 

Jusqu'à présent, les exemples que nous avons examinés n'ont toujours parcouru qu'une seule relation à la fois. Nous pouvons facilement tirer parti de ces "jointures à l'écriture" pour parcourir de nombreuses relations afin de répondre à des questions intéressantes. 

Alors, revenons au nombre de Kevin Bacon. La requête suivante commencerà au nœud de la personne Kevin Bacon, puis ira jusqu'à 4 sauts à partir de ce point de départ, pour ramener tous les films et personnes connectés.

```cypher
MATCH (bacon:Person {name:"Kevin Bacon"})-[*1..4]-(hollywood)
RETURN DISTINCT hollywood
```

Nous pouvons faire cela en utilisant la syntaxe `*1..4` dans la partie relation du motif de requête :

* `*` indique tout
* `1..4` indique la plage - 1 dit à partir de 1 saut, 4 dit jusqu'à 4 sauts

Une autre chose graphique que nous pourrions faire sur cet ensemble de données de films est le chemin le plus court entre deux nœuds. 

Dans cet exemple, découvrons le [chemin le plus court](https://neo4j.com/docs/cypher-manual/4.3/clauses/match/#query-shortest-path) entre Kevin Bacon et Meg Ryan. Vous remarquerez que nous utilisons à nouveau la syntaxe `*` pour le motif de relation – indiquant tout. 

Ce qui peut être nouveau pour vous, c'est le `p=`. Vous avez vu comment nous utilisons des références pour les nœuds (par exemple, `bacon` ou `meg` dans notre requête actuelle), et nous pouvons faire de même pour les relations. 

Nous pouvons également avoir des références pour le chemin entier (c'est-à-dire tous les nœuds et relations impliqués). La syntaxe que nous utilisons pour cela est `refName =`, qui dans cet exemple est `p=`. 

Nous utilisons également la fonction Cypher `shortestPath()` – il s'agit d'une fonction simple de chemin le plus court qui retournera le premier chemin le plus court entre deux nœuds spécifiés. Soyez conscient qu'il peut y avoir un autre chemin, tout aussi court, mais cette fonction simple ne retournera que le premier rencontré. 

Pour ceux d'entre vous intéressés par d'autres fonctions liées aux chemins, consultez celles disponibles dans APOC et GDS. 

```
MATCH p=shortestPath(
(bacon:Person {name:"Kevin Bacon"})-[*]-(meg:Person {name:"Meg Ryan"}))
RETURN p
```

Un mot d'avertissement à vous tous : vous pouvez voir ce `[*]` et être tenté d'exécuter votre graphe sans la contrainte de la fonction `shortestPath()` ou de la plage `1..4`. Mais cela peut bien entraîner quelque chose d'inattendu. 

Dans notre exemple avec Kevin Bacon et Meg Ryan, même s'il n'y a que 253 relations dans cet ensemble de données très petit, toutes les combinaisons possibles de chemins entre nœuds et relations pourraient facilement atteindre des millions de chemins différents entre Bacon et Ryan. 

Lorsque vous utilisez `*` dans vos relations dans le cadre d'une requête, utilisez-le avec une extrême prudence ! Ce problème ne se pose pas avec le chemin le plus court car, dès qu'un chemin potentiel plus long que le plus court actuellement identifié est rencontré, il est immédiatement abandonné. 

### Une requête de recommandations simple

Voici deux requêtes qui montrent vraiment la puissance des bases de données de graphes et nous pouvons facilement utiliser les connexions dans nos données pour faire quelques recommandations.

Dans notre première requête, nous cherchons de nouveaux co-acteurs pour Tom Hanks avec lesquels travailler et qu'il n'a pas encore rencontrés. La requête fait cela en :

* Tout d'abord, en trouvant tous les co-acteurs avec lesquels il a déjà travaillé
* Ensuite, en trouvant tous les co-acteurs des co-acteurs (appelés co-co-acteurs)
* Ensuite, nous voulons exclure ces co-co-acteurs qui ont déjà travaillé avec Tom, ainsi que nous assurer que le co-co-acteur n'est pas Tom lui-même
* Enfin, nous retournons les noms des co-co-acteurs suggérés, et nous allons les trier par le nombre de co-acteurs qui ont travaillé avec eux – plus il y a de co-acteurs qui ont travaillé avec ce co-co-acteur, meilleure est la recommandation.

```cypher
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors),
(coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cocoActors)
WHERE NOT (tom)-[:ACTED_IN]->()<-[:ACTED_IN]-(cocoActors) 
    AND tom <> cocoActors
RETURN cocoActors.name AS Recommended, count(*) AS Strength 
    ORDER BY Strength DESC
```

Excellent, nous avons donc trouvé quelques co-co-acteurs potentiels. Dans cette prochaine requête, nous voulons suggérer Tom Cruise comme un potentiel nouveau co-acteur pour Tom Hanks. Mais, qui va présenter ces Toms l'un à l'autre ? Retour au graphe de films.

Dans cette requête, nous :

* Trouvons les co-acteurs de Tom Hanks, puis trouvons lesquels de ces co-acteurs ont également joué avec Tom Cruise
* Ensuite, nous retournerons le co-acteur et les films dans lesquels ils étaient avec Tom Hanks et Tom Cruise

```cypher
MATCH (tom:Person {name:"Tom Hanks"})-[:ACTED_IN]->(m)<-[:ACTED_IN]-(coActors),
(coActors)-[:ACTED_IN]->(m2)<-[:ACTED_IN]-(cruise:Person {name:"Tom Cruise"})
RETURN tom, m, coActors, m2, cruise
```

## Derniers mots

Nous sommes arrivés à la fin de notre parcours de l'exemple de base de données de films. Espérons que ceux d'entre vous ayant un background en bases de données relationnelles ont une meilleure idée des similitudes et des différences entre les bases de données relationnelles et de graphes, ainsi qu'un aperçu du langage de requête Cypher.

Si vous êtes désireux d'en apprendre plus sur la modélisation et l'interrogation de Neo4j, consultez la [Graph Academy](https://dev.neo4j.com/learn) gratuite.