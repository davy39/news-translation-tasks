---
title: Comment concevoir des systèmes de bases de données structurées avec SQL [Livre complet]
subtitle: ''
author: Daniel García Solla
co_authors: []
series: null
date: '2025-08-13T18:03:10.495Z'
originalURL: https://freecodecamp.org/news/how-to-design-structured-database-systems-using-sql-full-book
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1755095979245/dfd39c26-3456-4e79-a01c-0b2a82f7a034.png
tags:
- name: SQL
  slug: sql
- name: Databases
  slug: databases
- name: database design
  slug: database-design
- name: book
  slug: book
seo_title: null
seo_desc: 'Ce livre vous guidera pas à pas dans la conception d''une base de données relationnelle avec SQL. SQL est l''un des langages relationnels les plus reconnus pour la gestion et l''interrogation de données...'
---

Ce livre vous guidera, étape par étape, dans la conception d'une base de données relationnelle à l'aide de SQL. SQL est l'un des langages relationnels les plus reconnus pour la gestion et l'interrogation de données dans les bases de données.

Vous apprendrez les concepts fondamentaux liés à la fois aux données et aux bases de données où elles sont stockées et gérées – de la transformation des données en informations puis en connaissances, jusqu'à l'architecture d'un système de gestion de base de données (SGBD ou DBMS en anglais). Nous aborderons également les différentes étapes du processus de conception de base de données, ainsi que ses principes clés, en nous concentrant spécifiquement sur la conception de bases de données relationnelles.

À la fin de ce livre, vous aurez une solide compréhension de la manière de concevoir et de maintenir des bases de données efficaces et sécurisées, capables de supporter des applications complexes pilotées par les données, le tout visant à répondre à une série d'exigences imposées par les utilisateurs finaux ou les clients. Vous apprendrez également les bases du SQL nécessaires pour implémenter cette conception sur un SGBD, puis pour maintenir et interroger les données qu'il contient.

Ainsi, que vous soyez débutant ou que vous cherchiez à perfectionner vos compétences, ce livre vous fournira les connaissances et les outils nécessaires pour réussir dans le monde de la gestion des données.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Le rôle des données dans le monde numérique d'aujourd'hui](#heading-le-role-des-donnees-dans-le-monde-numerique-daujourdhui)
    
3. [Chapitre 1 : Qu'est-ce qu'une donnée ?](#heading-chapitre-1-quest-ce-quune-donnee)
    
    * [La pyramide DIKW](#heading-la-pyramide-dikw)
        
4. [Chapitre 2 : Qu'est-ce qu'une base de données ?](#heading-chapitre-2-quest-ce-quune-base-de-donnees)
    
    * [SGBD (Systèmes de Gestion de Bases de Données)](#heading-sgbd-systemes-de-gestion-de-bases-de-donnees)
        
    * [Propriétés ACID et SGBD transactionnels](#heading-proprietes-acid-et-sgbd-transactionnels)
        
    * [Architecture d'un système de gestion de base de données](#heading-architecture-dun-systeme-de-gestion-de-base-de-donnee)
        
5. [Chapitre 3 : Modèles et technologies de gestion de données](#heading-chapitre-3-modeles-et-technologies-de-gestion-de-donnees)
    
    * [Types de données selon leur structure](#heading-types-de-donnees-selon-leur-structure)
        
    * [Big Data](#heading-big-data)
        
    * [Bases de données NoSQL](#heading-bases-de-donnees-nosql)
        
    * [Data Warehousing](#heading-data-warehousing)
        
    * [Data Lakes](#heading-data-lakes)
        
    * [Web Sémantique](#heading-web-semantique)
        
6. [Chapitre 4 : Conception de base de données](#heading-chapitre-4-conception-de-base-de-donnees)
    
    * [Niveaux de conception de base de données](#heading-niveaux-de-conception-de-base-de-donnees)
        
7. [Chapitre 5 : Modèle relationnel (Données structurées)](#heading-chapitre-5-modele-relationnel-donnees-structurees)
    
    * [Table (Relation)](#heading-table-relation)
        
    * [Schéma](#heading-schema)
        
    * [uplet (Tuple)](#heading-uplet-tuple)
        
    * [Domaine d'attribut](#heading-domaine-dattribut)
        
    * [Attribut dérivé](#heading-attribut-derive)
        
    * [Représentation conceptuelle](#heading-representation-conceptuelle)
        
    * [Groupe répétitif](#heading-groupe-repetitif)
        
    * [Incohérence des données](#heading-incoherence-des-donnees)
        
    * [Associations d'entités](#heading-associations-dentites)
        
    * [Généralisation et Spécialisation](#heading-generalisation-et-specialisation)
        
    * [Pièges des associations d'entités](#heading-pieges-des-associations-dentites)
        
    * [Clés](#heading-cles)
        
    * [Entités faibles](#heading-entites-faibles)
        
    * [Navigabilité](#heading-navigabilite)
        
    * [Contraintes](#heading-contraintes)
        
    * [Intégrité des données](#heading-integrite-des-donnees)
        
    * [Contraintes d'intégrité](#heading-contraintes-dintegrite)
        
8. [Chapitre 6 : Diagramme de schéma relationnel](#heading-chapitre-6-diagramme-de-schema-relationnel)
    
    * [Association 1-1](#heading-association-1-1)
        
    * [Association 1-M](#heading-association-1-m)
        
    * [Problèmes de cardinalité minimale](#heading-problemes-de-cardinalite-minimale)
        
    * [Association N-M](#heading-association-n-m)
        
    * [Hiérarchie IS-A](#heading-hierarchie-is-a)
        
9. [Chapitre 7 : Normalisation](#heading-chapitre-7-normalisation)
    
    * [Décomposition](#heading-decomposition)
        
    * [Dépendance fonctionnelle](#heading-dependance-fonctionnelle)
        
    * [Formes normales](#heading-formes-normales)
        
    * [BCNF](#heading-bcnf)
        
    * [Autres formes normales](#heading-autres-formes-normales)
        
10. [Chapitre 8 : Langages de requête](#heading-chapitre-8-langages-de-requete)
    
    * [Langages formels vs pratiques](#heading-langages-formels-vs-pratiques)
        
11. [Chapitre 9 : SQL (Structured Query Language)](#heading-chapitre-9-sql-structured-query-language)
    
    * [DDL](#heading-ddl)
        
    * [DCL](#heading-dcl)
        
    * [DML](#heading-dml)
        
    * [Vues](#heading-vues)
        
    * [Administration de base de données](#heading-administration-de-base-de-donnees)
        
12. [Chapitre 10 : Exemple de processus de conception](#heading-chapitre-10-exemple-de-processus-de-conception)
    
    * [Du modèle entité-relation au modèle logique](#heading-du-modele-entite-relation-au-modele-logique)
        
    * [Comment créer la base de données](#heading-comment-creer-la-base-de-donnees)
        
13. [Chapitre 11 : Exemples de requêtes](#heading-chapitre-11-exemples-de-requetes)
    
    * [Filtrage d'uplets](#heading-filtrage-duplets)
        
    * [Sous-requêtes](#heading-sous-requetes)
        
    * [Expressions de table communes (CTE)](#heading-expressions-de-table-communes-cte)
        
    * [Opérations sur les ensembles](#heading-operations-sur-les-ensembles)
        
    * [Requêtes d'agrégation](#heading-requetes-dagregation)
        
    * [Requêtes de division](#heading-requetes-de-division)
        
    * [Requêtes de classement (Ranking)](#heading-requetes-de-classement-ranking)
        
14. [Conclusion](#heading-conclusion)
    

## Prérequis :

Avant de parcourir ce livre, voici quelques prérequis utiles :

### Fondamentaux :

1. Connaissances de base en programmation : variables, types de données (chaîne/nombre/booléen), et structures de contrôle (conditions/boucles).
    
2. Familiarité avec les termes de tableur (lignes, colonnes, tri/filtrage), car cela facilitera la correspondance avec les tables/uplets/attributs.
    
3. Bases de la ligne de commande : savoir ouvrir un terminal, exécuter une commande, configurer le PATH (vous utiliserez occasionnellement des outils CLI ici), etc.
    

### Environnement à configurer

1. Un SGBD relationnel comme PostgreSQL (recommandé, car c'est celui que nous utiliserons ici).
    
2. Un client SQL comme psql, pgAdmin, TablePlus ou DBeaver (choisissez-en un).
    
3. Un outil de diagramme Entité-Relation (ERD) comme [draw.io/diagrams.net](http://draw.io/diagrams.net), Lucidchart ou [dbdiagram.io](http://dbdiagram.io).
    
4. Un éditeur de code comme VS Code (avec des extensions SQL et ERD, c'est parfait).
    

### Connaissances utiles

1. Familiarité avec certaines bases de mathématiques/logique : ensembles/sous-ensembles, relations, fonctions, ainsi que la logique propositionnelle de base (ET/OU/NON, implication).
    
2. Connaissance de base des termes de modélisation de données (entité, attribut, relation, cardinalité, etc.).
    
3. Bases du contrôle de version (Git).
    

Une fois cela réglé, plongeons dans le vif du sujet.

## Le rôle des données dans le monde numérique d'aujourd'hui

De nos jours, chaque action que nous effectuons sur Internet laisse derrière elle une trace d'informations ou de données – qu'il s'agisse d'effectuer une transaction bancaire ou de faire des achats en ligne.

Mais vous vous demandez peut-être parfois s'il est réellement logique que ces actions numériques soient enregistrées. Avons-nous besoin d'enregistrer les frappes au clavier lors de l'utilisation d'une application de clavier, les images enregistrées dans une application de galerie, les fichiers dans un programme de gestion de fichiers, les notes enregistrées dans une application de prise de notes, ou même les itinéraires de véhicules avec la technologie Android Auto intégrée ?

Certaines de ces actions peuvent ne pas sembler particulièrement utiles au premier abord, mais elles aident les développeurs et les concepteurs à fournir des services meilleurs, plus avancés et plus efficaces aux utilisateurs.

Par exemple, comprendre comment un utilisateur tape sur une application de clavier peut améliorer l'expérience de frappe en temps réel en adaptant le dictionnaire interne au style de frappe de l'utilisateur et en corrigeant les erreurs plus efficacement. Cela améliore également la saisie gestuelle, une fonctionnalité basée sur des techniques d'intelligence artificielle qui nécessite un grand nombre d'exemples pour être déployée avec succès sur un produit.

De même, de simples images enregistrées dans une galerie peuvent ne pas sembler assez importantes pour être enregistrées sur des sites externes, ou même enregistrées tout court.

Les fichiers image, par exemple, peuvent contenir des [**métadonnées EXIF**](https://fr.wikipedia.org/wiki/Exif) avec des informations sur l'image, telles que le lieu où elle a été capturée, la date de création, sa résolution, son orientation et le modèle d'appareil photo utilisé – entre autres données. Bien qu'un utilisateur puisse ne pas être intéressé par ces données, elles servent de base à divers services d'application, notamment la classification des images dans des albums en fonction du lieu, la création de chronologies visuelles et la génération de "souvenirs". Ces fonctionnalités améliorent considérablement l'expérience utilisateur.

Outre les métadonnées, le contenu des images crée également une "trace numérique" sur des serveurs tiers, ce qui peut initialement sembler intrusif et non bénéfique pour l'utilisateur. Cependant, cela peut conduire à des services améliorés. Étant donné que ces tiers disposent des ressources nécessaires pour entraîner de grands modèles d'apprentissage automatique (machine learning), ils peuvent reconnaître des objets et des visages dans les images. Cela améliore la classification des albums et permet aux utilisateurs de rechercher des images à l'aide de texte. Les tiers peuvent également identifier quelles personnes ou quels articles figurent sur une photo et lier leurs données à d'autres services.

En ce qui concerne les données générées par les véhicules intelligents ou les [**appareils IoT**](https://www.ibm.com/think/insights/how-modern-enterprises-are-using-iot-data-to-spur-innovation) en général, l'objectif est fondamentalement le même : fournir aux utilisateurs de meilleurs services, tels que l'optimisation des itinéraires, la prédiction de la maintenance, la prévention des pannes possibles, l'aide à la conduite et l'intégration avec d'autres appareils intelligents de l'environnement.

Ces fonctionnalités sont implémentées à l'aide de techniques d'intelligence artificielle qui apprennent à partir d'exemples. En règle générale, plus il y a de données disponibles, mieux les modèles sous-jacents "apprennent", ce qui conduit à de meilleurs résultats.

En fin de compte, indépendamment des questions juridiques et de confidentialité liées à ces pratiques, l'enregistrement de ce que nous faisons n'est pas une fin en soi. C'est plutôt un moyen de transformer des informations éparses en connaissances utiles, qui peuvent ensuite être utilisées pour créer des services qui améliorent notre productivité ou notre expérience utilisateur.

Un exemple clair de cela se trouve dans cet article même sur la [**plateforme Hashnode**](https://hashnode.com/changelog/free-ai-for-all-users-blogging?source=changelogs). Elle fournit aux rédacteurs des services de traduction, de réécriture et d'optimisation de mots-clés pour les [**recherches SEO**](https://developers.google.com/search/docs/fundamentals/seo-starter-guide?hl=fr), tous basés sur des modèles d'intelligence artificielle qui ont été entraînés à l'aide de grandes quantités de texte – c'est-à-dire des données.

Pour s'assurer que tout cela est techniquement réalisable, nous avons dû développer des techniques spécifiques pour collecter, stocker et gérer les informations de manière sécurisée, efficace et cohérente.

* La collecte implique la capture d'informations provenant de diverses sources, telles que les capteurs IoT, les appareils mobiles et les interactions sociales, manuellement ou automatiquement.
    
* Ces informations peuvent ensuite être stockées et consultées à nouveau lorsque nous devons les transformer ou appliquer des processus qui améliorent l'efficacité des requêtes ou réduisent l'espace de stockage. C'est précisément pourquoi la compression des données est un aspect critique du stockage des données.
    
* Enfin, la gestion des données implique des tâches d'organisation, de protection, de gouvernance et d'analyse.
    

Dans ce livre, nous nous concentrerons sur le stockage, qui est l'aspect clé géré par les bases de données. Mais les bases de données servent à bien plus qu'au simple stockage et à l'accès aux données, comme nous le verrons plus tard. Elles fournissent également un ensemble de fonctionnalités qui nous permettent d'organiser, de protéger et d'assurer l'intégrité des données, ainsi que de les interroger de manière efficace et concurrente.

Cela fait des bases de données un composant fondamental de l'infrastructure de ces services, qui sont souvent proposés à un grand nombre d'utilisateurs.

Plus précisément, nous nous attacherons à expliquer tous les concepts théoriques nécessaires que vous devez connaître pour concevoir et maintenir une base de données. Il existe de nombreuses façons de stocker des données, selon leur nature ou les besoins du client, mais nous nous concentrerons sur une structure spécifique.

Pour saisir les fondamentaux du stockage et de la gestion des données, nous devrions commencer par les cas les plus simples, qui impliquent les structures de données les plus simples possibles. Vous apprendrez également le langage **SQL** et sa pertinence pour la maintenance des bases de données à travers des exemples.

## Chapitre 1 : Qu'est-ce qu'une donnée ?

Avant de commencer à travailler avec des bases de données, il est utile d'avoir une compréhension claire de ce qu'est une donnée. Plus précisément, nous devons comprendre ce que signifie une donnée dans le contexte du travail avec les bases de données et SQL.

La [**définition officielle de la donnée**](https://fr.wikipedia.org/wiki/Donn%C3%A9e) couvre le niveau le plus basique, stipulant qu'une donnée est une représentation symbolique d'un attribut ou d'une variable quantitative ou qualitative qui décrit un fait empirique, un événement ou une entité.

Il est important de noter qu'une donnée n'a pas de signification intrinsèque. En d'autres termes, une donnée n'est qu'une valeur représentant quelque chose d'observable ou de mesurable – elle ne fournit aucune signification interprétable par elle-même.

Par exemple, le nombre 27 est une donnée à laquelle nous ne pouvons initialement donner aucun sens, bien que nous puissions la stocker, la transformer, la compresser et la chiffrer, etc. Plus tard, si nous découvrons que cette valeur provient d'une variable représentant des températures, alors nous avons plus qu'une simple donnée – nous avons une sémantique, ou une signification.

Dans cet exemple, le nombre 27 est considéré comme une donnée brute. Les [**données brutes**](https://www.lenovo.com/ca/en/glossary/raw-data/) sont des données qui ont été collectées à partir d'une source, mais qui manquent de signification ou de [**sémantique**](https://fr.wikipedia.org/wiki/Mod%C3%A8le_de_donn%C3%A9es_s%C3%A9mantique) et n'ont pas été traitées ou organisées.

Dans le contexte des bases de données, le terme **variable** est occasionnellement utilisé pour désigner l'origine de la donnée. Mais le terme **attribut** est plus courant, comme nous le verrons plus tard. En résumé, un attribut peut être vu comme une variable en programmation. Il représente une caractéristique d'une entité, comme l'âge d'une personne. Il est caractérisé par un type de données et un domaine qui définissent respectivement ce que les valeurs peuvent être et quelles sont ses valeurs possibles.

Les [types de données](https://fr.wikipedia.org/wiki/Type_de_donn%C3%A9e) sont les formats internes et les opérations supportés par les données d'un attribut. Ils peuvent inclure :

* les entiers (**ints**), qui sont généralement encodés en informatique sous forme de séquences de 32 bits
    
* les chaînes de texte encodées au format [**UTF-8**](https://developer.mozilla.org/fr/docs/Glossary/UTF-8)
    
* les nombres décimaux (floats ou doubles, entre autres), représentés à l'aide de la norme de virgule flottante [**IEEE-754**](https://learn.microsoft.com/fr-fr/cpp/build/ieee-floating-point-representation?view=msvc-170), et
    
* les valeurs booléennes qui peuvent être vraies ou fausses et sont encodées avec des bits comme 0 ou 1.
    

Comme vous pouvez le voir, le **type de données** définit la forme que peuvent prendre les valeurs d'un attribut, tandis que le [**domaine**](https://fr.wikipedia.org/wiki/Domaine_\(base_de_donn%C3%A9es\)) est un ensemble contenant toutes les valeurs d'attribut acceptables. Un domaine se compose d'un type de données qui limite la forme de la donnée et d'une série de contraintes qui restreignent les valeurs possibles qui peuvent être instanciées au sein de ce type de données de base.

Par exemple, si un attribut est étiqueté comme un entier et représente l'âge d'une personne, il est évident que le domaine ne peut pas contenir de nombres négatifs, bien que le type de données int les autorise. Par conséquent, le domaine peut être défini comme toutes les valeurs entières possibles avec des contraintes supplémentaires garantissant que les valeurs inférieures à zéro ne sont pas prises en compte, ne laissant que les entiers positifs nécessaires.

Grâce à ces concepts, nous pouvons comprendre la donnée dans sa forme la plus basique. Si nous prenons un nombre décimal comme 3.24, il peut indiquer une mesure à des fins scientifiques. Une chaîne de texte comme "Juan", en revanche, peut représenter le nom d'une personne. En d'autres termes, la sémantique d'une séquence de caractères définit sa signification. Seule, la séquence de caractères ne représente rien – mais ensemble, ils peuvent représenter un texte avec un sens, comme le nom de quelqu'un.

Au-delà des données atomiques, qui sont les éléments les plus basiques pouvant contenir des informations, il existe également des données beaucoup plus complexes. Cela inclut les données documentaires, les données spatiales et géographiques, les données de réseau ou de graphe, et les données multidimensionnelles. La seule différence entre les données "atomiques" que nous avons vues plus tôt et ces formes complexes de données est que ces dernières sont composées de relations ou d'**associations** entre des données plus simples.

Par exemple, un document se compose de séquences de caractères (chaînes) liées les unes aux autres, où une chaîne peut représenter le titre et une autre un paragraphe. Dans un réseau informatique modélisé sous forme de graphe, il pourrait y avoir des adresses IP aux nœuds, que nous pouvons considérer comme des chaînes encodées, et des références à d'autres nœuds, qui sont également des adresses IP.

Nous n'approfondirons pas la nature complexe de ces données ici car elles sont gérées par des bases de données spécialisées plus difficiles à appréhender, et où SQL n'est pas toujours présent.

### La pyramide DIKW

Jusqu'à présent, nous avons vu que les données elles-mêmes ne sont que des "symboles" qui peuvent être stockés, sans signification intrinsèque à moins que leur origine ou leur interprétation ne soit connue.

Mais il est également possible d'entraîner des modèles d'apprentissage automatique pour fournir des services qui paraissent beaucoup plus complexes par rapport aux données avec lesquelles ils ont été construits. En d'autres termes, nous pouvons construire des systèmes d'information complexes à partir de données brutes qui contiennent des connaissances de **plus haut niveau** que les données dont nous avons discuté.

La [**pyramide DIKW (Data, Information, Knowledge, Wisdom)**](https://www.datacamp.com/cheat-sheet/the-data-information-knowledge-wisdom-pyramid) modélise cette transformation de la donnée vers la sagesse, établissant une hiérarchie à travers laquelle nous pouvons acquérir des connaissances sur un aspect de la réalité à partir de données. Pour comprendre cela, examinons les quatre niveaux d'organisation des connaissances.

1. **Données (Data) :** À ce niveau, notre connaissance du monde – ou plutôt ce que nous en savons – est représentée sous forme de données brutes. Comme mentionné précédemment, les données brutes sont dépourvues de sémantique. Les seules options ici sont de stocker et d'analyser les données. Bien qu'elles ne fournissent pas explicitement de connaissances de haut niveau, nous pouvons nettoyer les données pour éviter les valeurs manquantes ou corrompues et calculer des mesures statistiques.
    
    **Exemple :** Comme précédemment, une valeur brute, telle que l'entier 27, est une donnée à partir de laquelle nous ne pouvons calculer que certaines métriques statistiques. Nous ne pouvons pas l'interpréter car nous ne connaissons pas sa signification tant que nous n'avons pas plus de contexte.
    
2. **Information :** Après être passé du niveau précédent, la donnée brute est dotée d'une sémantique, ce qui donne un sens aux valeurs stockées et analysées. Désormais, la donnée est mieux organisée car elle est contextualisée par rapport à sa sémantique.
    
    C'est la caractéristique principale de ce niveau, bien que certaines relations entre les données permettent également de calculer des statistiques plus complexes et de répondre à des questions plus précieuses sur les données. La connaissance à ce niveau est plus abstraite et précieuse que la précédente.
    
    **Exemple :** En reprenant l'exemple précédent, le nombre 27 pourrait représenter l'âge d'une personne. Ainsi, ici nous pouvons l'interpréter et l'organiser avec une compréhension plus profonde et l'analyser plus précisément.
    
3. **Connaissance (Knowledge) :** À ce stade, la connaissance réside dans des modèles qui capturent les schémas (patterns) des données analysées et organisées selon leur sémantique. C'est-à-dire que les données suivent des schémas cachés qui ne sont pas facilement discernables, mais qui peuvent être révélés par des techniques statistiques avancées ou l'apprentissage automatique.
    
    Ainsi, à ce niveau, l'information est compressée et résumée, ou plutôt, une compréhension de celle-ci est générée à travers un modèle, permettant de la synthétiser.
    
    Ce niveau est supérieur au précédent car il extrait des connaissances encore plus abstraites de l'information. Ces connaissances décrivent les données elles-mêmes, servent à faire des prédictions et à obtenir certains résultats en exploitant les relations de plus haut niveau entre les données.
    
    **Exemple :** Une fois que nous avons des données significatives, nous pouvons construire des modèles pour les décrire ou les résumer afin de faire des prédictions sur des données invisibles ou de tirer des conclusions.
    
    Par exemple, nous pouvons utiliser une métrique statistique, telle que la moyenne, comme modèle pour déterminer l'âge moyen d'un ensemble de données donné. Plus tard, en comparant cette moyenne avec l'âge d'autres personnes, nous pouvons déterminer si elles sont au-dessus ou en dessous de la moyenne. Mais les modèles utilisés pour décrire les données à ce stade sont généralement plus complexes et pratiques.
    
4. **Sagesse (Wisdom) :** En s'appuyant sur les connaissances du niveau précédent, nous atteignons un point où il n'est plus possible d'extraire des relations de plus haut niveau à partir des données. Cela signifie qu'aucune abstraction supplémentaire n'est possible. La seule tâche restante est de combiner notre description des données du niveau précédent avec un contexte social et éthique, ainsi que l'expérience professionnelle des personnes qui ont l'intention d'utiliser ces connaissances pour guider la prise de décision stratégique et évaluer ses conséquences au fil du temps.
    
    **Exemple :** À ce niveau final, nous pouvons utiliser l'âge d'une personne, pour lequel nous avons des modèles les décrivant, et le combiner avec des informations sur le contexte dans lequel ces informations ont été collectées pour éclairer des décisions stratégiques.
    
    Notez que les données peuvent provenir d'une organisation, qui est le contexte dans lequel les décisions stratégiques sont prises. Le point clé ici est que le but de posséder une telle connaissance de haut niveau est d'éclairer les décisions stratégiques.
    

En étudiant cette hiérarchie, nous pouvons voir que l'interprétation des données brutes conduit à l'acquisition de connaissances, ce qui nous permet de prendre des décisions éclairées. Les bases de données aident dans ce processus principalement en stockant les données, ce qui est l'un de leurs objectifs principaux. Mais elles nous assistent également dans le processus d'analyse en adaptant les méthodes de stockage et d'organisation des données.

À ce stade, vous pourriez poser la question : **Comment voulons-nous que la base de données stocke et analyse ces données ?** Tout d'abord, nous devons stocker les données de manière [persistante](https://fr.wikipedia.org/wiki/Persistance_\(informatique\)) en [mémoire secondaire](https://www.geeksforgeeks.org/computer-science-fundamentals/secondary-memory/) afin qu'elles puissent être récupérées à tout moment, plutôt qu'en **mémoire volatile** telle que la **RAM**.

D'autre part, l'**analyse** des données implique une grande variété d'opérations, allant de simples recherches et filtrages à des agrégations complexes, la détection de schémas, des calculs statistiques, l'exécution de requêtes SQL élaborées et le traitement de texte ou d'images. Chaque type de données et chaque besoin opérationnel nécessite des algorithmes et des structures de données différents pour être efficace.

Cela signifie que puisqu'une base de données doit fournir des fonctionnalités aux couches de stockage et d'analyse, vous pourriez vous demander s'il existe un système de base de données "général" capable de stocker et d'analyser des données de toute nature, quels que soient leur complexité ou les besoins de l'utilisateur. Comme nous le verrons ci-dessous, un tel système général ne peut pas exister. Mais il existe des systèmes conçus pour gérer tout type de problème lié aux données, **tant que les données ont une "forme" spécifique**.

## Chapitre 2 : Qu'est-ce qu'une base de données ?

Une fois que vous avez découvert les principales fonctions qu'une base de données doit fournir, vous pouvez comprendre ses avantages et pourquoi elle existe – surtout par rapport à une tentative d'implémentation de ces fonctions sans base de données. Pour illustrer cela, nous allons commencer par analyser un cas où nous essayons de résoudre un problème impliquant des données sans base de données. Cela montrera les problèmes qui peuvent survenir et comment ils sont résolus.

### Stocker des données sans base de données

En termes de **stockage** de données, les données brutes pourraient être stockées directement dans des fichiers binaires en mémoire secondaire. Pour l'**analyse**, nous pouvons implémenter une "couche" logicielle que nous pouvons appeler "couche de traitement". Elle contient des programmes qui manipulent les données stockées en y accédant et en effectuant des transformations basées sur une logique implémentée. Et pour faciliter la manipulation des données par les utilisateurs, il peut y avoir un composant d'**interface graphique** qui simplifie l'utilisation de ces programmes.

Un exemple pratique illustrera mieux cela. Supposons que nous travaillions avec un domaine qui contient des données sur des personnes et leurs informations financières. Notre objectif est d'analyser ces données et de faire des prédictions économiques. Ces données peuvent provenir de sources gouvernementales, d'enquêtes ou d'autres systèmes d'information. Nous devrons donc les stocker dans notre système sous forme de fichiers binaires.

Mais nous sommes confrontés à quelques problèmes : d'abord, nous devons choisir le type de fichier optimal. Ensuite, nous devons choisir la meilleure façon de représenter les données dans le fichier pour minimiser les problèmes lors des étapes futures de conception des programmes d'accès et d'analyse.

Par exemple, stocker les données dans un **fichier séquentiel**, où les données sont stockées de manière contiguë, est différent de les stocker dans un **fichier indexé**, où les informations sont organisées par un [**index**](https://www.geeksforgeeks.org/dbms/indexing-in-databases-set-1/). En d'autres termes, il existe un index qui organise les données par nom, de sorte que toutes les personnes dont le nom (ou une caractéristique similaire) commence par la même lettre sont stockées de manière contiguë dans le même bloc, séparées des lettres restantes. Ce principe récursif continue pour les lettres suivantes du nom. C'est comme si les données étaient triées par ordre alphabétique, bien qu'en général, un seul niveau de récursion suffise.

**Regardons un exemple :** Dans un fichier séquentiel, les noms des personnes sont stockés de manière "désorganisée", ce qui nous oblige à parcourir tout le fichier pour récupérer l'enregistrement d'une personne spécifique. En revanche, un fichier indexé trie les personnes par ordre alphabétique de nom. En consultant l'index, nous pouvons déterminer où commencent les noms commençant par une certaine lettre, évitant ainsi d'avoir à parcourir tout le fichier. En d'autres termes, l'index est similaire à la table des matières d'un livre, qui nous indique à quelle page commence chaque chapitre.

Ce type de décision affecte l'efficacité des recherches et des requêtes sur les données, ainsi que leur traitement. Chaque type de fichier a ses propres avantages et inconvénients, comme on peut s'y attendre.

De même, il existe une grande variété de décisions que nous pouvons envisager lors de la conception de programmes pour accéder aux données et les manipuler. Celles-ci sont directement influencées par les décisions précédentes. Par exemple, si nous changeons le type de fichier, le logiciel de ces programmes devra très probablement être reprogrammé. Vous pouvez considérer ces programmes comme des scripts Python qui automatisent certains processus d'analyse.

De plus, lors de l'implémentation de ces programmes, nous devons tenir compte de détails tels que l'accès **concurrent** aux données, qui est difficile à implémenter à partir de zéro, ainsi que d'autres fonctionnalités de sécurité, telles que le chiffrement des données, la compression et la détection de données erronées ou incomplètes. Ces fonctionnalités sont essentielles pour fournir un bon service d'analyse, mais elles sont difficiles à programmer et à maintenir.

En résumé, sans base de données, il est possible de résoudre le problème du stockage et de l'analyse des données – mais l'implémentation de tout le logiciel est potentiellement assez compliquée, surtout si nous visons à le faire à partir de zéro. Si nous avons les bonnes ressources, il peut être possible de mener à bien ce processus et d'aboutir à un système suffisamment efficace. Mais dans la plupart des cas, l'utilisation d'une base de données est plus pratique.

### Stocker des données à l'aide d'une base de données

Une façon de simplifier ces processus est d'utiliser une base de données, qui est une **collection organisée** de données modélisant un **domaine** et fournissant un support de stockage et d'analyse pour les processus que nous devons appliquer aux données. Sans base de données, les données devaient être stockées dans des "fichiers uniques" – mais en utilisant une base de données, elles sont stockées selon un modèle qui définit le type d'information et ses relations internes. C'est pourquoi la définition utilise le terme "organisée".

Quant au terme "collection", il fait référence à l'idée qu'une base de données est un ensemble de données provenant du même [**domaine**](https://fr.wikipedia.org/wiki/Domaine_\(g%C3%A9nie_logiciel\)). Ici, par "domaine", nous entendons le problème que nous traitons, pour lequel nous devons stocker et analyser des données. Dans notre exemple ci-dessus, le domaine serait l'"univers" des personnes et tous les concepts fiscaux qui leur sont associés – c'est-à-dire l'ensemble des concepts et des informations de l'environnement réel qui peuvent être pertinents pour résoudre un problème à l'aide de ces données.

Les avantages d'une base de données vont au-delà du simple stockage. Ils incluent également la **normalisation** du stockage et de l'organisation, permettant des **requêtes** efficaces sur les données stockées. Ces requêtes constituent les opérations de base de tout processus d'analyse (interrogation). Elles sont également le support fondamental d'autres tâches telles que la maintenance technique du système d'information, la gestion des données ou même des fonctionnalités telles que l'évolutivité (scalability) du système.

### SGBD (Systèmes de Gestion de Bases de Données)

La gestion des données implique une série de fonctionnalités supplémentaires qui sont fournies par un composant sur lequel repose la grande majorité des bases de données actuelles : le [**SGBD (Système de Gestion de Base de Données)**](https://www.ibm.com/fr-fr/topics/dbms). Comme son nom l'indique, ce composant est un élément logiciel responsable de la gestion centralisée et efficace de tout le cycle de vie des données stockées.

Dans ce contexte, la gestion se réfère principalement au stockage, à l'extraction, à la modification, à la suppression et à la recherche de données. Ce sont les opérations fondamentales nécessaires pour qu'une base de données soit considérée comme opérationnelle.

Mais la gestion implique également des fonctionnalités supplémentaires utiles dans une base de données :

* **Centralisation :** Le stockage de toutes les données dans un seul système évite d'avoir des informations dispersées dans de nombreux fichiers, ce qui peut entraîner une duplication inutile d'informations, telles que des références de données ou les données elles-mêmes. Si le système d'information n'est pas conçu et implémenté correctement, cela peut entraîner des incohérences et des erreurs. Mais ce n'est pas un problème si nous utilisons une base de données.
    
* **Intégrité et sécurité des données :** Le système de gestion contrôle qui peut accéder aux données grâce à des contrôles d'accès et des autorisations pour différents utilisateurs de la base de données. Il assure également l'intégrité des données, un sujet dont nous discuterons plus tard.
    
* **Accès concurrent et partage :** Les systèmes d'information supportent généralement des applications utilisées par de nombreux utilisateurs simultanément, ce qui provoque des problèmes de synchronisation gérés automatiquement par le SGBD. Heureusement, cela signifie que nous n'avons pas à implémenter de logique spécifique dans notre base de données pour assurer l'accès concurrent aux données par de nombreux utilisateurs.
    

Enfin, une autre caractéristique des SGBD est qu'ils rationalisent le développement et la maintenance des systèmes d'information construits à l'aide de bases de données, en particulier ceux qui reposent sur un SGBD. Il existe de nombreux logiciels de SGBD différents, tels que MySQL, MariaDB, PostgreSQL, MongoDB et Neo4j, entre autres. Ici, nous nous concentrerons sur PostgreSQL.

### Propriétés ACID et SGBD transactionnels

Au-delà des opérations de base dont nous avons discuté, il est important de souligner l'importance du support transactionnel dans les SGBD modernes pour des applications telles que la banque, la facturation en ligne et la santé.

Dans ces domaines, il est généralement essentiel que toute modification ou requête des données suive un mécanisme de [**transaction**](https://cloud.google.com/learn/what-are-transactional-databases?hl=fr). En d'autres termes, les opérations effectuées sur la base de données doivent être composées d'un bloc d'instructions de bas niveau (lectures et écritures), et le gestionnaire doit s'assurer que ces opérations sont exécutées dans leur ensemble ou pas du tout. C'est ce qu'on appelle souvent une opération atomique.

Cela permet d'éviter que des défaillances techniques ne causent des incohérences dans les bases de données (ou des problèmes similaires). Par exemple, si un utilisateur envoie de l'argent via Internet et qu'une erreur se produit, toute la transaction est annulée, comme si elle n'avait jamais eu lieu. Cela protège la base de données contre le maintien dans un état **incohérent**, par exemple lorsqu'une partie a envoyé de l'argent, mais que l'autre ne l'a pas reçu. Le SGBD est donc responsable d'assurer cette atomicité dans les opérations de base de données, ce qui l'oblige à respecter les [**propriétés ACID**](https://www.freecodecamp.org/news/acid-databases-explained/). Elles sont :

**1. Atomicité :** Une transaction fonctionne selon le principe du "tout ou rien", ce qui signifie que soit toutes ses instructions de bas niveau sont terminées, soit aucune d'entre elles n'est exécutée.

Exemple : Une transaction bancaire doit être complétée entièrement, et non laissée dans un état intermédiaire où une partie envoie l'argent et l'autre ne le reçoit pas.

**2. Cohérence (Consistency) :** Chaque transaction met à jour la base de données, garantissant qu'elle reste dans un état valide et préserve l'intégrité des données.

Exemple : Si une transaction modifie l'âge d'une personne, l'âge final ne peut pas être négatif.

**3. Isolation :** Les transactions concurrentes ne doivent pas interférer les unes avec les autres d'une manière qui produit des résultats incohérents.

Exemple : Deux personnes essaient de réserver le dernier siège sur un vol en même temps. L'isolation garantit qu'une seule réservation réussit et que le siège n'est pas réservé deux fois.

**4. Durabilité :** Une fois qu'une transaction a été terminée, ses effets sont permanents. Même si le système tombe en panne, il faut s'assurer que les modifications subsistent en les écrivant sur un stockage persistant.

Exemple : Si vous transférez de l'argent entre des comptes bancaires et que le système plante juste après, le transfert doit toujours être reflété lorsque le système revient en ligne.

Enfin, il est important de comprendre que **tous** les systèmes de gestion de bases de données *(SGBD)* n'ont pas besoin d'être transactionnels, bien que beaucoup d'entre eux supportent de telles fonctionnalités.

### Architecture d'un système de gestion de base de données

Après avoir vu ce qu'est un SGBD à haut niveau, nous pouvons examiner comment ses fonctionnalités sont implémentées plus en détail. Nous ne regarderons pas le niveau le plus bas possible, mais plutôt le niveau architectural.

Pour mieux comprendre comment un SGBD fonctionne, nous pouvons nous concentrer sur le rôle de chacun de ses composants lors de la réception d'une demande d'utilisateur, qu'il s'agisse d'une modification de données, d'une opération de gestion ou d'une requête de récupération de données.

%[ 

Dans l'ensemble, chaque SGBD est unique, avec des composants spécifiques à sa conception et à ses besoins. D'une manière générale, cependant, ils partagent tous les composants suivants :

* **Précompilateur** : Ce composant extrait et sépare les instructions de langage individuelles intégrées dans les applications basées sur la requête de l'utilisateur, qui est généralement dans un langage comme SQL, avant de les transmettre à l'analyseur (parser).
    
* **Analyseur (Parser)** : Traite et valide la syntaxe de la requête de l'utilisateur, générant un arbre d'analyse intermédiaire.
    
* **Contrôle d'autorisation** : Vérifie les autorisations de l'utilisateur pour s'assurer que seules les actions autorisées sont effectuées.
    
* **Processeur de requête** : Convertit la requête de l'utilisateur en un plan d'exécution logique avant de l'optimiser.
    
* **Vérificateur d'intégrité** : Valide que les données répondent à toutes les contraintes définies sur la base de données pendant que la requête exécute ses instructions.
    
* **Optimiseur** : Analyse et réécrit le plan d'exécution pour choisir la stratégie d'exécution la plus efficace.
    
* **Génération de code exécutable** : Transforme le plan d'exécution optimisé en appels spécifiques à l'API du moteur de stockage.
    
* **Gestionnaire de transactions** : Coordonne le début, la validation (commit) ou l'annulation (rollback) des opérations de transaction pour assurer l'atomicité et l'isolation.
    
* **Journal (Log de transaction)** : Enregistre séquentiellement toutes les modifications pour assurer la durabilité et le support de la récupération.
    
* **Gestionnaire de récupération** : Utilise le journal pour restaurer la base de données dans un état cohérent après des pannes.
    
* **Gestionnaire de dictionnaire (Catalogue)** : Maintient et interroge les métadonnées *(schémas, statistiques, autorisations)* de la base de données.
    
* **Gestionnaire de données** : Implémente les structures de données de stockage physique et les opérations d'accès aux données.
    
* **Processeur d'E/S (I/O)** : Gère la lecture et l'écriture des données sur le disque, c'est-à-dire la mémoire persistante.
    
* **Générateur de résultats** : Formate et envoie les ensembles de résultats (données interrogées) à l'utilisateur ou à la couche applicative.
    

Enfin, bien que la plupart des bases de données reposent sur un SGBD, ce n'est pas toujours le cas. Pour des raisons techniques ou de performance, l'implémentation d'une base de données personnalisée à partir de zéro peut mieux fonctionner pour certaines équipes que l'utilisation d'une solution basée sur un SGBD commun. Un SGBD n'est donc pas nécessaire pour qu'une base de données existe, bien qu'il soit présent dans la vaste majorité des bases de données en raison de ses avantages intrinsèques.

## Chapitre 3 : Modèles et technologies de gestion de données

Comme vous l'avez appris, les applications qui reposent sur des bases de données impliquent généralement de grandes quantités de données diverses et complexes. Pour cette raison, il n'existe pas de modèle de base de données unique qui réponde efficacement à tous les scénarios. Il existe plutôt différentes familles, chacune se spécialisant dans des tâches ou des ensembles de tâches spécifiques.

Nous allons donc explorer ici une gamme d'options qui peuvent vous aider à sélectionner une base de données à utiliser dans un projet, en fonction des données et des exigences du système. Plus précisément, nous examinerons certains modèles ou approches sur lesquels une base de données peut être basée. Mais gardez à l'esprit qu'il en existe beaucoup d'autres en dehors de ceux dont nous discuterons ici.

### Types de données selon leur structure

Tout d'abord, le facteur le plus pertinent pour déterminer le paradigme d'une base de données dans un projet est la donnée elle-même – en particulier sa complexité. La complexité des données est définie par leur structure, leur variabilité et leurs relations internes. Cela détermine principalement comment les données sont stockées et traitées.

Ainsi, avant d'analyser les différents paradigmes ou approches disponibles, vous devez comprendre la signification de la [**complexité des données**](https://www.acceldata.io/blog/data-complexity).

La complexité est un concept que nous pouvons comprendre informellement comme le degré auquel une donnée est "compliquée". Par exemple, une liste d'entiers est différente d'un graphe avec des entiers à chaque nœud ou d'une liste de nombres encodés en binaire, chiffrés ou compressés.

Ainsi, la [**complexité**](https://www.aimspress.com/article/doi/10.3934/bdia.2016002?viewType=HTML) a plusieurs dimensions.

* **Volume :** Clairement, plus nous avons de données, plus elles seront difficiles à gérer. Il est probable qu'elles ne tiennent pas toutes sur une seule machine, ce qui entraîne des temps de traitement ou de latence de requête plus longs.
    
* **Hétérogénéité :** Cela fait allusion à la vaste variété de formats, de structures et d'origines que les données peuvent présenter au sein d'un écosystème d'information donné. Chacune de ces caractéristiques constitue un type spécifique d'[hétérogénéité](https://www.dremio.com/wiki/heterogeneous-data/). Ce concept est plus lié au monde de l'intégration de données qu'aux bases de données elles-mêmes, car c'est le principal problème auquel nous sommes confrontés lors de l'intégration de données dans un système, qu'il comprenne ou non une base de données.
    
    * **Exemple :** Si nous allons construire une base de données de villes et la remplir avec des données de différentes sources, il est probable que les noms des villes soient écrits légèrement différemment dans chaque source. C'est ce qu'on appelle l'hétérogénéité syntaxique.
        
* **Structure :** Dans notre cas, c'est la dimension clé, car elle nous permet de classer les données dans différentes catégories, chacune étant associée à un paradigme de base de données spécifique. Essentiellement, la structure des données se réfère à la mesure dans laquelle elles adhèrent à un **schéma** prédéfini.
    

Pour l'instant, nous pouvons comprendre le **schéma** comme une définition formelle qui détermine **comment** les données sont organisées, ainsi que les caractéristiques de cette organisation en fonction de la nature des données et de la base de données. Plus tard, nous nous concentrerons sur le concept de schéma dans une base de données **structurée** (relationnelle).

Ainsi, la complexité des données dépend principalement de deux dimensions : la **flexibilité** du schéma et le **volume** ou l'**hétérogénéité** des données. Plus le schéma est flexible et plus le volume ou l'hétérogénéité des données est important, plus il sera compliqué de les traiter, ce qui nécessitera un modèle de base de données approprié.

Cela signifie que, concernant la dimension structurelle de la complexité, nous pouvons catégoriser les données selon leur degré de "rigidité".

Tout d'abord, nous avons les **données non structurées**. Ce sont des données qui ne suivent pas un schéma fixe ou un ensemble de règles pour une interprétation ou un étiquetage automatique sans traitement préalable. Elles sont généralement les **plus complexes** car elles ne sont pas structurées et manquent de métadonnées, ou d'informations supplémentaires qui les décrivent ou les organisent. Cette catégorie comprend les images, les vidéos, l'audio et toutes sortes de multimédias, tels que les données spatiales.

Ensuite, nous avons les **données semi-structurées**. Contrairement aux données non structurées, celles-ci utilisent des balises (tags) comme métadonnées pour les organiser. Cela permet aux données d'être regroupées autour de ces balises, ce qui les rend plus faciles à interpréter, à interroger et à traiter. Mais elles peuvent également être auto-organisées à l'aide de paires clé-valeur ou de hiérarchies internes.

Essentiellement, ces données contiennent des **méta-informations** qui permettent leur auto-organisation, bien qu'elles n'adhèrent pas au schéma strict des données structurées. Par exemple, nous pouvons avoir des données au format **XML** ou **JSON** où les données sont présentées sous forme de paires clé-valeur, avec une clé associée à une ou plusieurs données. En tant que tel, le schéma de paire clé-valeur n'est pas assez rigide pour caractériser parfaitement la structure des données car il ne limite pas explicitement la quantité de données pouvant être associées à une balise.

Enfin, nous avons les **données structurées**. Ces données sont organisées par un schéma strict qui les restreint à une **forme tabulaire**. En d'autres termes, l'organisation est adaptée à un schéma et suit une série de règles. Chaque point de données est composé d'une séquence de valeurs qu'il prend sur un nombre fini d'attributs, où chacun de ces attributs est monovalué (univalued).

Nous pouvons considérer le schéma comme l'en-tête de la table qui détermine les attributs pour lesquels chaque point de données prend des valeurs. De cette façon, un point de données est un uplet (tuple) ou une ligne de la table dans laquelle il est stocké.

Il existe une restriction supplémentaire : chaque attribut ne peut avoir qu'une seule valeur, ce qui signifie qu'un attribut ou une cellule de la table ne peut pas contenir plus d'une valeur.

Chacune de ces catégories conduit à un ou plusieurs paradigmes de base de données adaptés à leur nature. Les plus faciles à traiter sont les structurées, car leur rigidité ne permet pas une variation suffisante pour que les techniques analytiques utilisées sur elles soient considérées comme "*complexes*". En revanche, les plus difficiles à traiter sont les non structurées, en raison de leur variété et de leur grande flexibilité.

#### Limitations des données structurées

Pour rester simple, nous nous concentrerons sur les données structurées et les bases de données qui les supportent. Ces bases de données sont construites à l'aide du **modèle relationnel**, dont nous discuterons plus tard.

Étant donné que les données structurées sont organisées en tables, les manipuler est plus simple car les tables ont des propriétés qui les rendent plus faciles à parcourir et à traiter. Par exemple, savoir que chaque cellule ne contient qu'une seule valeur nous permet de parcourir par programmation toutes les données de la table en parcourant toutes ses lignes, quel que soit le contenu de chaque cellule. De cette façon, nous évitons d'explorer un nombre indéterminé de valeurs par cellule, ce qui serait beaucoup moins efficace.

Cette simplicité permet également aux tables d'être implémentées à l'aide de structures de données orientées enregistrements ou champs. Celles-ci fournissent l'efficacité nécessaire pour structurer les données au sein du modèle relationnel conçu pour ce type de données. Ce modèle est un "paradigme" de base de données qui, lorsqu'il est utilisé avec un langage de requête tel que SQL, nous permet de stocker et de traiter la plupart des données structurées, c'est pourquoi il est si important.

Gardez à l'esprit, cependant, que son statut de paradigme "général" qui répond à presque tous les problèmes impliquant des données structurées introduit certaines limitations :

#### 1. Évolutivité (Scalability)

La plupart des implémentations de bases de données relationnelles ou structurées utilisent une architecture monolithique. Cela signifie que la base de données s'exécute sur une seule machine et ne peut être mise à l'échelle que **verticalement** en allouant plus de ressources à la machine.

Heureusement, les implémentations distribuées utilisent des réseaux de plusieurs machines pour exécuter la base de données. Cette approche permet une mise à l'échelle **horizontale** en ajoutant plus de machines au système distribué, offrant une plus grande évolutivité. Une telle évolutivité est critique pour des produits comme les réseaux sociaux, garantissant la disponibilité du système.

#### 2. Flexibilité du schéma

Avec un schéma aussi rigide, si nous devons stocker des données non structurées (comme du JSON ou des données d'image), cela nécessite une transformation ou une alternative aux bases de données structurées, telles que les bases de données **NoSQL**. Nous en discuterons plus tard. Ces bases de données permettent une plus grande flexibilité dans les schémas de données et supportent des données hétérogènes.

#### 3. Types de données complexes

En plus d'avoir un schéma flexible, le type de données que nous traitons peut être complexe, ce qui rend l'interrogation insuffisante. Les opérations sur les données structurées sont généralement conçues pour des données simples qui seront souvent interrogées. Mais lors du stockage d'images, de graphes ou d'autres entités complexes, nous pouvons avoir besoin d'effectuer des opérations complexes sur celles-ci.

Par exemple, nous pourrions avoir besoin d'effectuer une détection d'objets dans des images ou de calculer des métriques de voisinage et de centralité dans des graphes. Cela conduit au développement de modèles de bases de données spécifiques (que nous aborderons plus tard) qui supportent ces opérations et le stockage de telles données, qui sont généralement conservées dans des [BLOBs](https://developer.mozilla.org/fr/docs/Web/API/Blob).

#### 4. Volume de données (Big Data)

Comme mentionné précédemment, le volume de données a un impact sur presque tous les modèles de base de données, car le stockage d'une grande quantité de données ralentit les processus. Mais les modèles de **Warehousing** (entrepôt de données) et de **Data Lake** (lac de données) peuvent atténuer cet effet en exploitant leur capacité à évoluer horizontalement et à accélérer le calcul pour traiter plus rapidement des quantités massives de données. Ceci est réalisé grâce à des techniques telles que les [pipelines de données](https://aws.amazon.com/fr/what-is/data-pipeline/) ou le [cluster computing](https://www.ibm.com/think/topics/cluster-computing) (similaire au [calcul distribué](https://aws.amazon.com/fr/what-is/distributed-computing/)).

#### 5. Exigences en temps réel

Enfin, on attend des bases de données qu'elles aient une faible [latence](https://aws.amazon.com/fr/what-is/latency/) lors de l'exécution des opérations, car la vitesse à laquelle les utilisateurs sont servis est souvent déterminée par la latence de ces opérations. De plus, comme le nombre d'utilisateurs est généralement important, la base de données doit supporter la concurrence.

Mais les opérations de stockage persistant effectuées pendant ces processus – plus les verrous d'exclusion mutuelle qui assurent la [concurrence](https://www.geeksforgeeks.org/dbms/concurrency-control-in-dbms/) (et le respect des principes ACID) – ralentissent le traitement des données. En conséquence, les implémentations de [bases de données en mémoire](https://aws.amazon.com/fr/nosql/in-memory/) sont fréquemment préférées pour atténuer ce problème. En plus de sauvegarder les données dans un stockage persistant, ces implémentations utilisent la **mémoire RAM** comme cache pour stocker une partie des données et répondre plus rapidement aux requêtes, atteignant une latence proche du temps réel.

Ainsi, bien qu'elles soient les plus simples et les plus efficaces pour modéliser les problèmes quotidiens, les bases de données structurées présentent certains inconvénients. Ceux-ci ont conduit au développement de modèles et d'approches de bases de données alternatifs. Chacun de ces modèles tente de répondre à un problème spécifique des bases de données structurées, en fournissant un support pour des données plus complexes et des exigences techniques plus difficiles.

### Big Data

Avant d'examiner des modèles de bases de données spécifiques, nous devrions considérer un problème qui les affecte tous : le volume de données. Lorsque nous avons un problème avec une quantité suffisante de données, le terme "[Big Data](https://cloud.google.com/learn/what-is-big-data?hl=fr)" est généralement appliqué. Ce n'est pas un modèle ou un ensemble de modèles, mais plutôt un concept désignant des ensembles de données massifs et complexes.

Et étant donné la quantité de données actuellement produite chaque jour, il est de plus en plus courant de rencontrer des problèmes où le volume massif devient une limitation.

Dans un projet Big Data, nous pouvons diviser son cycle de vie en plusieurs étapes.

1. Tout d'abord, les données sont capturées à partir de multiples sources et intégrées dans des formats communs.
    
2. Ensuite, elles sont [nettoyées](https://aws.amazon.com/fr/what-is/data-cleansing/) pour assurer une intégration correcte et, si nécessaire, annotées ou étiquetées manuellement pour alimenter des modèles d'apprentissage automatique.
    
3. Les données sont ensuite stockées dans des infrastructures évolutives ou directement dans des bases de données, garantissant la disponibilité et un accès rapide.
    

Ces tâches de "[prétraitement](https://fr.wikipedia.org/wiki/Pr%C3%A9traitement_des_donn%C3%A9es)" peuvent représenter une part importante du travail nécessaire avant que les données ne soient prêtes à l'emploi.

Une fois traitées, nous utilisons principalement les données pour créer des modèles de connaissance afin de comprendre la nature des données. Cela nous permet également de générer des prédictions et des décisions éclairées dans des environnements professionnels. Ce processus est généralement appelé informatique décisionnelle (business intelligence) ou prise de décision basée sur les données.

Ces processus d'informatique décisionnelle peuvent également aider à d'autres tâches, telles que l'analyse statistique et la visualisation. Certaines de ces tâches, notamment la [visualisation](https://www.ibm.com/think/topics/data-visualization) et l'analyse statistique, sont considérées comme faisant partie de l'écosystème du Big Data et sont fondamentales pour le traitement des données. Elles accompagnent les tâches précédentes telles que la gestion des bases de données et des systèmes d'information. Il est donc essentiel de définir correctement dès le départ **quelles données** sont nécessaires pour un projet, **comment** elles seront traitées et **quels résultats** sont attendus.

#### Qu'est-ce qui constitue le "Big Data" ?

Il convient de noter que, pour qu'un projet soit considéré comme du Big Data, il n'y a pas de conditions strictes pour déterminer s'il appartient à cette catégorie. Néanmoins, un certain nombre de facteurs contribuent à cette désignation :

Le premier est le volume. Comme nous en avons déjà discuté, le volume de données se réfère à la quantité de données générées et stockées au sein d'un projet donné. Plus il y a de données générées et stockées, plus le projet est susceptible d'être classé comme Big Data. Pourtant, il n'y a pas de montant spécifique qui définit cette distinction, car elle dépend également d'autres facteurs, notamment la disponibilité et la complexité des données.

Le suivant est la vélocité. C'est la vitesse à laquelle les données sont générées et doivent être traitées. Par exemple, dans un projet consistant en un réseau social ou un réseau d'appareils IoT, les données peuvent être générées à une vélocité très élevée – c'est-à-dire une grande quantité de données par unité de temps. Ces données doivent être traitées le plus rapidement possible. Cela signifie que plus les données sont générées rapidement, plus elles sont susceptibles d'être considérées comme faisant partie de l'écosystème Big Data.

Le dernier facteur principal est la variété, également appelée hétérogénéité des données. Cela signifie que plus les données sont hétérogènes, plus elles sont difficiles à traiter. Cela nécessite une plus grande puissance de calcul, ce qui rend le projet plus susceptible d'être considéré comme du Big Data.

Par exemple, l'intégration de données provenant de sources utilisant les mêmes formats est plus facile que l'intégration de données provenant de sources utilisant des formats différents.

L'hétérogénéité est affectée non seulement par les formats, mais aussi par la façon dont ils sont encodés, transmis, etc. Nous devons également considérer le niveau de structuration des données car les données non structurées ou non étiquetées nécessitent probablement des techniques d'apprentissage automatique (telles que le [clustering](https://www.freecodecamp.org/news/8-clustering-algorithms-in-machine-learning-that-all-data-scientists-should-know/)) pour en extraire des informations.

Ce sont les facteurs principaux, bien que d'autres aient été ajoutés au fil du temps grâce aux progrès technologiques dans ces processus. Parmi eux :

* **Véracité** : Degré de fiabilité des informations reçues en termes de qualité et d'exactitude des données, afin d'éviter des décisions basées sur des informations incorrectes ou biaisées.
    
* **Viabilité :** Le degré auquel les données peuvent être utilisées efficacement dans le projet, car parfois leur volume ou d'autres facteurs rendent leur traitement techniquement irréalisable.
    
* **Visualisation :** C'est la facilité avec laquelle les données peuvent être transformées en tableaux de bord compréhensibles pour les utilisateurs, leur permettant de les explorer intuitivement.
    
* **Valeur :** La valeur attendue à obtenir du traitement des données. Généralement, c'est une valeur économique, bien qu'elle n'ait pas besoin d'être économique – elle dépend principalement du domaine d'application.
    
* **Viscosité :** C'est l'importance que les données ont dans la prise de décision. Non pas la valeur ajoutée par leur traitement, mais la pertinence qu'elles ont lors de la prise d'une décision.
    

En résumé, bien que le volume soit l'un des facteurs clés déterminant si un problème ou un projet est considéré comme du Big Data, ce n'est pas le seul. La vitesse à laquelle les données sont générées et l'hétérogénéité des données nécessitent une grande quantité de calcul pour les traiter, ce qui est le problème principal qui a conduit au concept de Big Data.

### Bases de données NoSQL

Le premier modèle ou approche de base de données que nous examinerons est [**NoSQL**](https://cloud.google.com/discover/what-is-nosql?hl=fr). Son nom indique que ces bases de données ne sont pas seulement structurées, mais aussi que les données peuvent varier en structure.

La caractéristique principale de cette approche de base de données est sa **flexibilité** dans le stockage des données – elle ne force pas les données à adhérer à un schéma fixe, tel qu'un schéma tabulaire. Elles se concentrent également sur l'offre d'une **évolutivité horizontale** facile, ce qui permet d'étendre la capacité de calcul de la base de données en augmentant le nombre de machines. Cela les rend efficaces pour traiter des données complexes et de grand volume et ainsi supporter les problèmes de Big Data.

Pour comprendre ce qu'elles impliquent en pratique, nous pourrions envisager un cas d'utilisation impliquant une base de données pour un système de location de vélos, qui permet aux utilisateurs de louer des vélos via un abonnement.

Pour implémenter ce système, nous pouvons choisir parmi une grande variété de bases de données ou de systèmes d'information. Par exemple, dans une **base de données relationnelle**, les informations sont organisées en tables, tandis que les bases de données **NoSQL** utilisent différents types de structures pour organiser les données. Chaque structure donne un type spécifique de base de données NoSQL.

Sans entrer dans les détails du cas d'utilisation, nous pouvons voir que l'utilisation d'une base de données relationnelle pour un tel projet peut poser des défis dans les domaines suivants :

* **Volume :** Si le système est déployé à l'échelle nationale ou continentale, un grand nombre d'utilisateurs effectueront des transactions dans notre système, soit en utilisant ou en rendant des vélos, soit en contractant ou en annulant leur abonnement au service. Surtout, la mise à l'échelle d'une base de données relationnelle a le plus grand impact sur le système. Pour gérer un tel nombre d'utilisateurs, le système nécessite une puissance de calcul puissante pour répondre aux besoins. Cela signifie que la base de données doit pouvoir évoluer horizontalement pour atteindre une capacité optimale. Dans les bases de données relationnelles, la mise à l'échelle verticale est généralement appliquée, mais il devient coûteux d'ajouter plus de capacités de calcul au-delà d'un certain seuil.
    
* **Vélocité :** Le système doit répondre rapidement aux demandes des utilisateurs, comme l'affichage des vélos disponibles dans une certaine zone ou la gestion des abonnements. Si le système utilise une base de données relationnelle, assurer la concurrence est coûteux en calcul, ce qui provoque une latence élevée lorsque de nombreux utilisateurs interrogent ou modifient les mêmes informations simultanément.
    
* **Schéma rigide :** Dans une base de données relationnelle, le schéma ne change pas fréquemment. Ainsi, si notre système nécessite des mises à jour régulières (comme des mises à jour de modèles de vélos, l'ajout de nouveaux capteurs de vélos ou des modifications importantes du service d'abonnement, en particulier l'ajout de fonctionnalités ou de nouvelles caractéristiques), ces changements nécessiteront la mise à jour du schéma de la base de données en ajoutant ou en supprimant des colonnes. Ce processus est coûteux et compliqué une fois que le système est en production et que ses tables contiennent une grande quantité de données.
    
* **Analyse temporelle :** Étant donné que les bases de données structurées sont composées de tables, comme nous l'apprendrons plus tard, si nous devons effectuer une analyse de séries chronologiques ou analyser des données s'étendant sur une longue période avec un grand nombre d'enregistrements tout au long de cette période, la latence de réponse de la base de données sera élevée. Par exemple, considérez le calcul de métriques sur l'utilisation des vélos au cours des 10 dernières années, période pendant laquelle il peut y avoir eu un nombre massif de transactions entre les utilisateurs et les vélos. Ces types de requêtes sont souvent appelés requêtes analytiques.
    

Les bases de données NoSQL offrent différentes solutions à ces problèmes, selon la façon dont les données doivent être structurées. Ainsi, pour chacune de ces façons d'organiser et de stocker les données, il existe un certain type de base de données NoSQL avec une série d'avantages et d'inconvénients selon la nature du projet et les données impliquées. Regardons-les maintenant.

#### Modèle Clé-Valeur

L'option la plus simple consiste à stocker toutes les données dans un dictionnaire de [**paires clé-valeur**](https://www.mongodb.com/resources/basics/databases/key-value-database), où chaque clé est un identifiant unique qui agit comme une balise liée à une seule valeur. Le type de contenu de chaque valeur dépend de la façon dont nous devons organiser les données.

Ici, nous utilisons le terme "[dictionnaire](https://en.wikibooks.org/wiki/A-level_Computing/AQA/Paper_1/Fundamentals_of_data_structures/Dictionaries)" pour désigner la structure de données utilisée dans des langages tels que Python et Java, ainsi que dans des langages où la structure de dictionnaire est la seule méthode de représentation de l'information, comme en JSON. Dans notre cas d'utilisation, si nous voulons stocker des informations sur l'utilisateur, chaque utilisateur pourrait être représenté comme un dictionnaire avec les paires [**clé-valeur**](https://aws.amazon.com/fr/nosql/key-value/) suivantes :

```json
{
  "id": 27,
  "name": "Juan",
  "email": "juan@juan.com",
  "birth": "1984-01-05"
}
```

Comme vous pouvez le voir, les clés servent de noms qui identifient la valeur que nous stockons dans une paire donnée. Dans ce cas, la clé est le nom de l'utilisateur, bien que nous puissions également enregistrer du contenu binaire ou une valeur booléenne comme clé.

Parmi les caractéristiques de ce modèle, on trouve :

* sa simplicité, qui permet aux humains de le comprendre facilement
    
* sa faible latence, qui bénéficie de structures de données telles que les tables de hachage avec des temps d'accès très bas, et
    
* sa facilité de distribution sur plusieurs machines, car un dictionnaire peut être partitionné de manière transparente par ses clés. En pratique, [**Redis**](https://redis.io/) est le SGBD le plus courant utilisé pour ce genre de base de données.
    

#### Modèle Documentaire

Dans ce modèle, l'unité de gestion de l'information n'est pas une paire clé-valeur, mais plutôt un ensemble de celles-ci, connu sous le nom de "document".

La différence principale avec le modèle **clé-valeur** précédent est que les valeurs ne sont plus "opaques". Ici, un document contient ses informations dans une structure hiérarchique imbriquée. Cela signifie qu'une valeur peut être un dictionnaire contenant des paires clé-valeur, dont certaines peuvent également être des dictionnaires. Ainsi, une hiérarchie est établie au sein des informations stockées, plutôt que de permettre aux valeurs d'être de n'importe quel type comme dans le modèle clé-valeur.

Certaines caractéristiques du modèle documentaire sont son **schéma flexible** et le **stockage hiérarchique** de données hétérogènes. Par exemple, dans notre cas d'utilisation, nous pouvons stocker les informations sur les vélos comme suit :

```json
bike1 = {
  "id": 1,
  "model": "model1",
  "status": "available"
}

bike2 = {
  "id": 2,
  "model": "model2",
  "status": "in_use",
  "sensors": {
    "cadence": 85,
    "speed": 24.5
  }
}

bike3 = {
  "id": 3,
  "model": "model3",
  "status": "maintenance",
  "sensors": {
    "gps": {
      "latitude": 40.4168,
      "longitude": -3.7038
    },
    "camera": "front_hd"
  },
  "acquisitionDate": "2024-11-15"
}
```

Ici, vous pouvez voir que tous les dictionnaires représentent des vélos. Mais certains contiennent plus de champs que d'autres selon les informations que le modèle de vélo spécifique produit. Cela évite d'avoir à créer plusieurs tables pour chaque modèle ou type de vélo. Vous pouvez également voir que certains champs ont un dictionnaire comme valeur, ce qui hiérarchise les données. De plus, tous les champs n'ont pas besoin d'être structurés de la même manière car le modèle permet une certaine **hétérogénéité** à cet égard.

Enfin, il est important de souligner que, dans ce modèle, les documents sont auto-descriptifs, car les noms des clés ou des balises identifient l'information stockée. [**MongoDB**](https://www.mongodb.com/fr-fr) est l'un des principaux SGBD pour implémenter ce modèle.

#### Modèle orienté colonnes

Ce modèle est similaire au modèle **structuré** (celui utilisé dans les bases de données relationnelles) où les informations sont stockées dans des tables – mais au lieu que chaque point de données soit conservé dans une ligne, il est stocké dans une [**colonne**](https://www.geeksforgeeks.org/dbms/columnar-data-model-of-nosql/). Par exemple, dans notre cas d'utilisation, nous pourrions avoir :

| **Attribut** | bike1 | bike2 | bike3 |
| --- | --- | --- | --- |
| **model** | model1 | model2 | model3 |
| **status** | available | in\_use | maintenance |
| **sensor\_cadence** | – | 85 | – |
| **sensor\_speed** | – | 24.5 | – |

Dans ce type de base de données, les points sont toujours des lignes dans une table. Mais les éléments que le système de gestion considère comme composant la table ne sont pas les lignes, mais les colonnes.

Dans une base de données relationnelle, un ensemble de lignes compose une table, où chaque ligne est un point de données contenant des valeurs prises pour certains attributs, qui sont les colonnes. De même, dans le [**modèle orienté colonnes**](https://fr.wikipedia.org/wiki/SGBD_orient%C3%A9_colonnes), le système de gestion traite une colonne comme un "point de données" sur lequel des opérations sont effectuées.

Comme illustré ci-dessus, une table du modèle relationnel est transposée de sorte que chaque colonne devienne un vélo au lieu d'un attribut. Dans le modèle orienté colonnes, chaque point de données est une colonne, ce qui permet d'exécuter rapidement des requêtes analytiques puisque toutes les valeurs d'une colonne sont considérées comme un seul "point de données", ce qui accélère considérablement les opérations d'**agrégation**.

De plus, une meilleure compression des données est généralement obtenue car toutes les données d'une colonne sont du même type. Une évolutivité horizontale simple est également possible grâce à des techniques telles que le sharding de colonnes. L'un des SGBD les plus populaires pour ce modèle est [**Hadoop**](https://hadoop.apache.org/).

#### Modèle de graphe

Alternativement, il existe le [**modèle de graphe**](https://aws.amazon.com/fr/nosql/graph/), qui repose sur des [**graphes**](https://www.w3schools.com/dsa/dsa_theory_graphs.php) comme structures de données fondamentales pour stocker des informations et des relations entre les données.

Dans notre cas d'utilisation, par exemple, chaque nœud peut représenter des entités allant des personnes aux vélos, reliées par des arêtes représentant des relations entre elles, telles que des abonnements ou des locations. Les nœuds et les arêtes peuvent contenir des attributs, ce qui nous permet d'organiser davantage l'information.

Ce modèle se caractérise par son support pour l'analyse et les projets de Big Data car les problèmes qui ont tendance à être modélisés avec des graphes impliquent souvent de grands volumes d'informations, comme les réseaux sociaux. De plus, les graphes en tant que structures de données permettent de modéliser des informations et des relations complexes. [**Neo4j**](https://neo4j.com/) est une option populaire ici, mais il existe une variété d'autres SGBD orientés vers des utilisations spécifiques au sein de ce modèle.

### Data Warehousing

Outre les différentes options offertes par le modèle NoSQL, vous pouvez avoir d'autres besoins qui nécessitent différents types de modèles. NoSQL se concentre actuellement principalement sur le stockage et l'interrogation efficaces des données. Il est particulièrement utile dans les projets où la génération de données est le goulot d'étranglement – c'est-à-dire qu'un système spécialisé dans le stockage des données est nécessaire.

Inversement, d'autres projets, en particulier ceux liés aux organisations, nécessitent un système qui non seulement stocke les données efficacement, mais gère également la difficulté d'extraire des informations stratégiques, car les données manquent de valeur par elles-mêmes. Le [**modèle de Warehousing**](https://www.geeksforgeeks.org/dbms/data-warehousing/) offre un support pour la centralisation, l'organisation et la transformation ultérieure des données en connaissances qui guident la prise de décision.

#### Qu'est-ce qu'un Data Warehouse ?

Un [**Data Warehouse**](https://cloud.google.com/learn/what-is-a-data-warehouse?hl=fr) (entrepôt de données) est essentiellement une base de données spécialisée pour stocker de manière centralisée de grands volumes de données provenant de multiples sources. En plus de stocker toutes les données dans "un seul système" de manière centralisée, son objectif principal consiste à optimiser les requêtes analytiques sur les données et à générer des tableaux de bord ou des rapports à partir de l'analyse elle-même. Tout cela vise à soutenir l'analyse et le stockage efficaces des données.

Par "[requêtes analytiques](https://docs.vertica.com/23.4.x/en/data-analysis/sql-analytics/analytic-query-examples/)", j'entends des requêtes qui nécessitent des informations sur une certaine période de temps (ou une dimension différente) pour calculer une métrique sur les données, telle que la magnitude moyenne sur une période de 10 ans.

En revenant à l'exemple précédent du système de location de vélos, le modèle de Warehousing offre des avantages en termes d'efficacité dans le stockage des vélos et des transactions des utilisateurs, telles que les locations ou les abonnements. Il supporte également des requêtes analytiques complexes sur les données qui contribuent à la prise de décision stratégique concernant le système. Ces requêtes visent à prédire la demande et les revenus, à détecter quelles zones de stationnement sont utilisées plus ou moins fréquemment, et ainsi de suite.

#### Principales caractéristiques des Data Warehouses

Examinons maintenant certaines des principales caractéristiques d'un Data Warehouse afin que vous compreniez comment ils fonctionnent.

#### Ils sont intégrés

Un entrepôt de données est généralement une base de données qui stocke des informations provenant de diverses sources. Il intègre ces informations à l'aide de transformations et de processus qui traitent l'hétérogénéité des données, en les adaptant au schéma commun de l'entrepôt.

Dans notre exemple, les données peuvent provenir de divers systèmes, notamment le positionnement GPS des vélos, les capteurs d'occupation des parkings, les systèmes de paiement et d'abonnement et les applications mobiles. L'entrepôt intègre ensuite toutes ces données, en les normalisant dans un format commun pour faciliter leur analyse collective. Notez que ces **sources** peuvent varier considérablement en nature, certaines étant structurées et d'autres non.

#### Ils ont une dimension historique

Au fil du temps, l'entrepôt accumule des informations provenant de différentes sources pour permettre des requêtes analytiques. Dans notre exemple, cela correspondrait à l'analyse des données elles-mêmes, comme l'examen du comportement et de l'utilisation des utilisateurs et des vélos, l'analyse de la demande ou des revenus, entre autres possibilités.

#### Ils sont optimisés pour la lecture

Compte tenu des objectifs que nous voulons atteindre avec un entrepôt, il est optimisé principalement pour les requêtes qui accèdent uniquement aux données sans les modifier, ce qui est précisément ce que les requêtes analytiques exigent.

Dans notre exemple, il ne serait pas très efficace d'implémenter l'ensemble du système d'information dans un entrepôt en raison de la nécessité d'optimiser les opérations d'écriture. Une solution possible serait d'utiliser l'entrepôt uniquement pour stocker les données réservées à l'analyse, tout en fournissant le service réel aux utilisateurs avec un système plus approprié.

En d'autres termes, même si nous utilisons une base de données différente pour implémenter le service de location de vélos, nous pouvons également avoir un entrepôt dans lequel nous insérons périodiquement les informations qui doivent être analysées.

#### Différents schémas de Data Warehousing

En plus de ces caractéristiques, un entrepôt de données est principalement une base de données composée de tables. Ainsi, si les données sont très complexes ou ont trop de dimensions, nous pouvons les organiser en différents modèles de données.

#### 1. [Schéma en étoile](https://fr.wikipedia.org/wiki/Sch%C3%A9ma_en_%C3%A9toile) (Star Schema)

Ici, les données ou les mesures sont principalement stockées dans une table centrale appelée table de faits, qui est liée à d'autres tables représentant les dimensions possibles pour l'analyse des données de la table de faits. La caractéristique principale de ce modèle est que les tables dimensionnelles ne sont généralement pas subdivisées en dimensions plus spécifiques, car l'objectif ici est de trouver un moyen simple de stocker les données pour accélérer au maximum les requêtes analytiques.

Dans notre exemple, si vous avez seulement besoin de construire des tableaux de bord pour l'utilisation, la facturation ou des fins similaires, en privilégiant la vitesse de requête, vous pourriez opter pour un schéma en étoile avec une grande table de locations contenant des champs comme l'utilisateur, le vélo, la station d'origine/destination, la date et le coût, et des tables environnantes pour chacune de ces entités qui peuvent être considérées comme des "*dimensions*" lors de l'analyse de ces données.

![Exemple de schéma en étoile, avec une table de faits centrale connectée à plusieurs tables de dimensions autour d'elle. De https://en.wikipedia.org/wiki/Star_schema](https://upload.wikimedia.org/wikipedia/commons/b/bb/Star-schema.png align="center")

#### 2. [Schéma en flocon de neige](https://fr.wikipedia.org/wiki/Sch%C3%A9ma_en_flocon_de_neige) (Snowflake schema)

Contrairement au modèle de données en étoile, avec un schéma en flocon de neige, chaque table environnante peut être subdivisée en sous-dimensions spécifiques, c'est-à-dire des tables plus petites liées les unes aux autres. Cela permet souvent d'économiser de l'espace et d'améliorer la qualité des données en réduisant la redondance, car il existe des tables spécifiques stockant des informations spécifiques et les reliant au reste des tables, évitant ainsi la duplication d'informations dans trop de tables. Cela rationalise la gestion d'ensembles de données plus volumineux et plus complexes.

![Exemple de schéma en flocon de neige, avec une table de faits centrale connectée à plusieurs tables de dimensions subdivisées en plus de dimensions autour d'elle. https://en.wikipedia.org/wiki/Snowflake_schema](https://upload.wikimedia.org/wikipedia/commons/b/b2/Snowflake-schema.png align="center")

#### ETL (Extraction, Transformation, and Load)

Comme vous l'avez appris, un Data Warehouse est alimenté par des données provenant de multiples sources, toutes potentiellement de nature différente. Les Data Warehouses doivent donc disposer d'un composant responsable de l'extraction des données des sources, de leur traitement et de leur insertion dans l'entrepôt de données. Ce composant est l'[**ETL**](https://cloud.google.com/learn/what-is-etl?hl=fr), qui est une pièce logicielle spécifique pour chaque source de données qui gère :

* **Extraction :** Obtient les données de la source dans le format fourni.
    
* **Transformation :** Elle applique une série de transformations pour les nettoyer, éliminer l'hétérogénéité et les adapter au schéma défini dans notre entrepôt. La complexité et le détail de ces transformations dépendent principalement du problème traité, allant même jusqu'à la dérivation ou la prédiction de nouvelles données à partir d'enregistrements existants.
    
* **Chargement (Load) :** Il les insère dans l'entrepôt.
    

Les processus ETL sont généralement exécutés périodiquement pour alimenter le Data Warehouse ou mettre à jour les données qu'il contient.

![Diagramme d'un processus ETL. Il extrait les données des sources, les transforme et les charge dans un système d'information. De https://en.wikipedia.org/wiki/Extract,_transform,_load](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c7/Extract%2C_Transform%2C_Load_Data_Flow_Diagram.svg/1280px-Extract%2C_Transform%2C_Load_Data_Flow_Diagram.svg.png align="center")

#### OLAP

Comme vous l'avez déjà vu, le Data Warehousing est conçu pour supporter les requêtes analytiques, communément appelées [**OLAP (Online Analytical Processing)**](https://aws.amazon.com/fr/what-is/olap/). Contrairement à l'[**OLTP (Online Transactional Processing)**](https://www.oracle.com/fr/database/what-is-oltp/), qui se concentre sur la lecture ou la modification d'enregistrements individuellement, l'OLAP permet d'analyser les données selon diverses dimensions pour découvrir des tendances ou des schémas qui soutiennent la prise de décision stratégique.

Pour comprendre cela, il est très courant de penser aux requêtes sur la dimension temporelle, qui est la plus facile à voir, comme le calcul d'une moyenne sur les données d'une période de temps ou toute métrique similaire.

Plus précisément, dans un [**environnement OLAP**](https://www.geeksforgeeks.org/dbms/olap-operations-in-dbms/), les données sont organisées en **cubes** multidimensionnels, où chaque dimension représente une perspective d'analyse comme le temps, le produit, la région, etc., et les données ou **mesures** sont les valeurs quantitatives qui sont **agrégées** selon les dimensions qui nous intéressent.

Certaines [**opérations**](https://www.ibm.com/think/topics/olap) de navigation et d'agrégation de base sont définies sur ces cubes :

* **Drill-Down (Forage vers le bas) :** Cela consiste à passer d'un niveau d'agrégation élevé à un niveau plus détaillé. Par exemple, après avoir examiné le total des locations de vélos trimestrielles, nous appliquons un drill-down pour voir celles qui ont eu lieu par mois, et de là par jour ou même par place de stationnement, ce qui nous permet de détecter rapidement les variations d'utilisation sur des périodes spécifiques.
    
* **Roll-Up (Synthèse) :** C'est l'opération inverse du drill-down : elle regroupe les données dans des niveaux de détail plus élevés. À partir des locations quotidiennes, avec un roll-up, nous pouvons obtenir les locations mensuelles, par région, ou le total annuel, ce qui aide à résumer de grands volumes de données et à fournir une vue d'ensemble du domaine modélisé.
    
* **Slice (Tranche) :** Ici, un sous-ensemble de données est sélectionné en fixant une valeur dans une dimension. Par exemple, une "tranche" dans le cube de location de vélos en fixant la dimension **"région = Espagne"** affichera toutes les locations de vélos qui ont eu lieu en Espagne, tout en gardant fixes d'autres dimensions comme le temps ou d'autres services (abonnement au service).
    
* **Dice (Dés) :** Similaire au slicing, un **"filtre"** est appliqué au cube sur plusieurs dimensions simultanément. Par exemple, interroger les locations de vélos dans une région géographique spécifique et pendant une certaine période de temps. La différence principale est qu'une plage est définie dans plusieurs dimensions à la fois, créant un sous-cube avec des résultats plus spécifiques.
    
* [**Pivot**](https://www.numberanalytics.com/blog/mastering-data-pivoting-data-warehousing) (Pivotement) **:** Cela consiste à réorganiser les dimensions du cube pour changer la perspective d'analyse sans modifier les données. Par exemple, permuter les lignes et les colonnes dans un rapport pour afficher les régions en colonnes et les périodes en lignes, ce qui facilite la comparaison de différentes dimensions et la découverte de corrélations entre elles.
    

### Data Lakes

En plus du modèle de Warehousing, nous avons les [**Data Lakes**](https://cloud.google.com/learn/what-is-a-data-lake?hl=fr) (lacs de données), qui sont comme des entrepôts où les données ne sont pas stockées selon un schéma commun mais sont conservées telles qu'elles proviennent de leurs sources respectives. C'est-à-dire que pour alimenter un entrepôt avec des données, des composants ETL sont nécessaires pour les transformer et les adapter à un **schéma**. Mais avec un lac de données, de tels composants n'existent pas car il n'y a pas de schéma que les données doivent suivre – au lieu de cela, elles sont simplement stockées dans leur format et leur structure d'origine.

La raison principale est qu'un lac de données vise à analyser les données, tandis qu'un entrepôt vise à intégrer les données par des transformations pour les transformer en connaissances qui soutiennent l'[**analyse de décision commerciale**](https://www.revealbi.io/blog/data-warehousing) de haut niveau.

Normalement, les données sont stockées sous leur forme brute dans un lac de données sans aucun traitement, bien qu'elles puissent être organisées selon les besoins du projet. Cela implique que les coûts associés sont généralement inférieurs à ceux d'un entrepôt, car cela économise toutes les ressources de calcul liées à leur transformation, qui peut parfois être complexe et coûteuse en calcul.

Étant donné que les lacs de données se concentrent sur le **stockage** des données plutôt que sur leur **intégration**, ils conviennent aux **tâches d'apprentissage automatique** et à l'[**analyse exploratoire**](https://www.ibm.com/think/topics/exploratory-data-analysis). Il est facile d'appliquer des algorithmes pour trouver des schémas dans les données brutes. Mais ne confondez pas données non intégrées et données non étiquetées. Les [**données étiquetées**](https://www.freecodecamp.org/news/supervised-vs-unsupervised-learning/) peuvent être stockées dans un lac de données et utilisées pour entraîner des modèles d'apprentissage automatique supervisés. Tout dépend des besoins du projet et du niveau d'abstraction avec lequel vous souhaitez travailler.

### Web Sémantique

En plus des modèles de bases de données précédents, il existe d'autres types de technologies et d'outils qui peuvent organiser les données et leur sémantique. L'une de ces technologies est le [**Web Sémantique**](https://fr.wikipedia.org/wiki/Web_s%C3%A9mantique), qui naît du besoin de donner un sens aux termes utilisés sur le web traditionnel.

Par exemple, dans un document HTML, le mot "user1" peut apparaître, ce qui en soi n'est qu'une donnée sans aucune signification. Ainsi, pour intégrer la sémantique, le Web Sémantique est utilisé comme une "couche" logicielle qui associe une signification aux termes qui apparaissent sur le web.

Alors qu'un simple document HTML sert à structurer une série de données au niveau de la **mise en page** (layout), le Web Sémantique fournit une signification, généralement par le biais de balises ou d'annotations, afin qu'elles puissent être interprétées par les humains et les machines. De cette façon, la donnée "user1" peut être associée à une balise comme "nom", indiquant que la donnée est un nom d'utilisateur.

Cette technologie repose sur une série de composants :

* **RDF (Resource Description Framework) :** Un [**standard**](https://fr.wikipedia.org/wiki/Resource_Description_Framework) où l'information est représentée par des triplets [**Sujet – Prédicat – Objet**](https://stackoverflow.com/questions/273218/whats-a-rdf-triple), où le sujet est généralement une ressource ou une entité au sein du domaine, le prédicat est un attribut ou une relation que l'entité a avec une valeur, qui est l'objet du triplet. Cette façon de représenter l'information est facilement compréhensible par les personnes et facilement traitée par les machines, étant indépendante du langage utilisé pour gérer les triplets (tels que **XML** ou **Turtle**).
    
    ```xml
    <http://example.org/users/user1> domain:name "Juan"
    ```
    
* **Vocabulaires :** Un ensemble de termes utilisés pour décrire les données dans un domaine spécifique. Nous pouvons voir cela comme un langage ou un dictionnaire de concepts avec leurs significations associées, appartenant tous à un domaine commun. Plus précisément, il peut avoir des significations associées à des classes (ensembles d'entités), des propriétés de ces entités ou des relations entre elles.
    
    * **Exemple :** [https://fr.wikipedia.org/wiki/Dublin_Core](https://fr.wikipedia.org/wiki/Dublin_Core)
        
* **Ontologies :** Une conceptualisation formelle d'un domaine, où les significations des entités qu'il contient sont définies, ainsi que leurs propriétés, leurs relations avec d'autres entités, les hiérarchies qu'elles forment entre elles et leurs contraintes. En résumé, elles fournissent une sémantique plus riche que les vocabulaires en raison de la complexité avec laquelle elles peuvent modéliser la sémantique.
    
    * **Exemple :** [http://musicontology.com/docs/getting-started.html](http://musicontology.com/docs/getting-started.html)
        

En ce qui concerne le web, il existe de multiples façons de stocker nos données, que ce soit sur notre propre [infrastructure](https://www.hpe.com/fr/fr/what-is/on-premises-vs-cloud.html) ou sur celle de quelqu'un d'autre. D'une part, nous pouvons choisir d'avoir une infrastructure complète en propre où toutes les données sont gérées localement **(on-premise)**, ce qui offre des avantages comme le fait d'avoir un contrôle total sur celles-ci ou un accès plus rapide. Mais cela présente également des inconvénients tels que des coûts élevés car nous devons maintenir toute l'infrastructure nous-mêmes, assurer une bonne évolutivité et minimiser le risque de pannes qui pourraient réduire la disponibilité du service.

D'autre part, vous pouvez choisir d'utiliser l'infrastructure de quelqu'un d'autre, généralement en la louant. Ici, les données sont dans le **cloud** (nuage), ce qui offre une plus grande évolutivité, des coûts réduits puisque vous ne payez que pour l'infrastructure que vous utilisez, un large accès géographique avec des services comme GCP ou AWS, et des services de sauvegarde qui minimisent le risque de perte de données, ce qui serait potentiellement très coûteux à réaliser en utilisant une infrastructure locale.

Pourtant, cette approche présente également des inconvénients, tels que la dépendance à une connexion Internet pour utiliser l'infrastructure en tant que service, ou des problèmes de sécurité et de confidentialité puisque les données se trouvent dans un endroit que nous ne connaissons pas bien.

Enfin, gardez à l'esprit que ces deux types de solutions ne s'excluent pas mutuellement. Vous pouvez les utiliser simultanément dans des [solutions hybrides](https://www.shakudo.io/blog/cloud-vs-on-premise-vs-hybrid) où les données les plus sensibles ou les plus précieuses sont conservées localement et le reste sur une infrastructure externe, bien que cela dépende fortement des exigences du projet.

## Chapitre 4 : Conception de base de données

Maintenant que vous avez découvert certains modèles de bases de données existants et les technologies qui les supportent, il est important de comprendre ce que signifie la conception de base de données.

En résumé, la [**conception de base de données**](https://guides.visual-paradigm.com/navigating-the-three-levels-of-database-design-conceptual-logical-and-physical/) se réfère à la création d'une base de données. Lorsque vous avez un projet impliquant des données, la première chose à faire est de déterminer si vous avez réellement besoin d'une base de données. Cela dépend généralement de facteurs tels que les exigences fournies par un client.

Si vous avez besoin d'une base de données, sa [conception](https://www.geeksforgeeks.org/dbms/database-design-in-dbms/) suit généralement une série d'étapes. Ces étapes commencent par les exigences du client, qui déterminent ce qui doit être stocké et comment cela doit être stocké. Ensuite, le schéma ou la structure que les données doivent suivre une fois le stockage planifié. Cela vous permet d'explorer plus avant comment stocker et traiter les données de manière informatique à bas niveau pour optimiser les opérations les plus critiques.

Par exemple, dans des projets tels que les plateformes de vente de produits, il peut être plus important d'optimiser les opérations liées aux recherches de produits, tandis que dans d'autres tels que les réseaux sociaux, l'optimisation de l'écriture de nouveaux messages peut être plus significative.

En plus de décider de la **structure** des données, les exigences des utilisateurs aident également à déterminer quelles données doivent être stockées, car il n'est pas toujours nécessaire de conserver toutes les données disponibles dans une base de données. Généralement, seules les données susceptibles d'être récupérées ou utilisées dans une opération sont stockées, bien que cela dépende fortement des exigences et de la nature du projet.

### Niveaux de conception de base de données

Lorsque vous développez un projet de données et que vous travaillez sur la conception de la base de données, vous pouvez la diviser en une série d'étapes ou de **niveaux de conception**. Ceux-ci sont liés au niveau d'abstraction avec lequel vous pouvez visualiser l'implémentation de la base de données. Considérez-les comme des étapes à suivre pour parvenir à une base de données fonctionnelle qui répond aux exigences des utilisateurs, lesquelles sont également considérées comme faisant partie de la conception de la base de données.

En dehors de ces niveaux de conception, il existe une distinction basée sur le domaine du développement auquel ils sont orientés, distinguant généralement trois domaines dans lesquels les différents niveaux de conception sont classés.

* D'une part, il y a l'**analyse** des besoins et des exigences du client, qui détermine ce que notre système d'information doit faire.
    
* Ensuite, nous avons la **conception** de la base de données elle-même, qui fournit une description de la solution, son implémentation pratique et les composants logiciels/matériels qui la forment.
    
* Enfin, nous avons la **technologie** utilisée pour cette implémentation, où les outils, les programmes et les modules spécifiques impliqués dans le développement sont décidés.
    

Voyons maintenant les différents niveaux de conception.

#### 1. Analyse (Exigences fonctionnelles et de données)

Ce niveau est considéré comme faisant partie de la conception de la base de données en raison de son influence sur les autres étapes ou niveaux. Ici, les informations sur le domaine sont d'abord recueillies, lesquelles peuvent provenir de clients, d'utilisateurs ou de toute partie prenante ayant une connaissance du domaine. L'objectif principal est d'obtenir autant d'informations que possible pour en extraire ensuite les [**exigences des utilisateurs**](https://qat.com/guide-writing-data-requirements/). Ce sont une série d'axiomes qui déterminent ce que le système doit faire pour fonctionner selon les besoins du client.

Ces exigences peuvent être de plusieurs types, tous [étudiés en profondeur](https://www.geeksforgeeks.org/software-engineering/software-engineering-classification-of-software-requirements/) dans le domaine du génie logiciel. Une caractéristique importante à leur sujet est qu'elles déterminent **ce que** le système doit faire, et non **comment** il doit le faire, bien que dans certains systèmes, il existe des exigences de correction ou de sécurité qui pourraient restreindre la façon dont le système doit effectuer certaines actions.

Par exemple, si nous concevons une base de données pour un [système critique](https://fr.wikipedia.org/wiki/Syst%C3%A8me_critique) comme une centrale nucléaire, il est très probable que certaines de ces exigences obligent le système à répondre à certaines requêtes critiques dans un délai court pour des raisons de sécurité.

#### 2. Conception conceptuelle (ERD/UML de haut niveau)

Une fois que les exigences auxquelles le système ou la base de données doit répondre sont claires, la [conception conceptuelle](https://www.tutorialspoint.com/conceptual-database-design) est chargée de décrire comment les données seront organisées au sein de la base de données. Cela se fait toujours selon le modèle de base de données que vous avez sélectionné pour le projet, car l'utilisation de NoSQL est différente de l'utilisation d'une base de données structurée.

Pour bien comprendre ce niveau, considérons un cas où la base de données utilisée est relationnelle/structurée. À ce niveau, les données sont d'abord décrites, ainsi que leurs éventuelles contraintes associées, telles que les types de données, les domaines d'attributs, etc. Ensuite, des outils de génie logiciel tels qu'un [diagramme entité-relation](https://www.lucidchart.com/pages/fr/diagramme-entite-relation) sont utilisés pour décrire les tables qui composent la base de données et leurs relations. Cela nous aide à formaliser la structure dans laquelle les données seront organisées une fois le système en production.

Il est important de se rappeler que quel que soit l'outil utilisé pour ce processus (qu'il s'agisse d'un diagramme ou de toute autre méthode de représentation), l'organisation représentée dans le diagramme doit ensuite être traduite en une implémentation logicielle, qui dépend fortement du SGBD. La conception d'une base de données **structurée** diffère de la conception d'une base de données **orientée graphe**, vous devrez donc sélectionner un outil approprié à ce niveau pour représenter l'organisation des données.

Ainsi, l'objectif principal à ce niveau, au-delà de la compréhension des exigences, est d'organiser la façon dont l'information est stockée en fonction des opérations que le système supportera. Vous devrez également documenter correctement les descriptions fournies, que ce soit avec des diagrammes ou d'autres outils, afin qu'elles soient compréhensibles plus tard et puissent être implémentées sur un SGBD spécifique.

#### 3. Conception logique (Schéma relationnel)

En supposant que la base de données soit **structurée**, à ce niveau, vous utiliserez le diagramme que vous avez créé au niveau précédent pour implémenter le schéma de la base de données sur un SGBD. Cela signifie que vous définissez les tables que la base de données aura sur le SGBD.

Si vous n'avez pas utilisé de diagramme au niveau précédent ou si la base de données n'est pas structurée, vous suivrez le même processus – bien qu'au lieu de tables, vous utiliserez les structures appropriées, telles que des graphes. En fin de compte, ici le diagramme **entité-relation** est traduit en un schéma **relationnel**, comme nous le verrons plus tard, qui est chargé de représenter les tables qui existent dans la base de données au niveau de la couche SGBD.

Lorsqu'on traite des tables (ou de la structure correspondante selon le modèle de base de données que vous utilisez), il est facile de comprendre comment la base de données organise l'information. Mais ce n'est que la vue de **haut niveau**, dans la mesure où les SGBD nous montrent comment les données sont organisées, car finalement tout doit être converti en structures de données de **bas niveau** et en algorithmes sur des fichiers qui travaillent avec des informations encodées en binaire. En d'autres termes, bien que nous voyions des tables, le SGBD opère en interne avec d'autres types d'outils informatiques à un niveau inférieur, plus proche du matériel, qui ne ressemblent pas nécessairement à des tables, des graphes, des paires clé-valeur, etc.

Cela offre un avantage : lors de la gestion de la base de données, vous pouvez le faire en vous concentrant sur les tables qu'elle contient, sans avoir à vous soucier de la façon dont les données sont réellement stockées en mémoire (ou de la façon dont les structures de données et les algorithmes utilisés pour implémenter les opérations de base de données fonctionnent).

En d'autres termes, la base de données, plus précisément le SGBD, traduit automatiquement la gestion au [niveau des tables]( en gestion au niveau le plus bas, plus proche du matériel, ce qu'on appelle l'[indépendance logique-physique](https://www.geeksforgeeks.org/dbms/physical-and-logical-data-independence/). Cela nous permet de manipuler la base de données en travaillant directement avec les tables, et non avec le contenu au niveau matériel, ce qui compliquerait les choses.

Enfin, à ce niveau, vous effectuerez souvent un [affinement du schéma](https://enter77.ius.edu/cjkimmer/schema-refinement/) (schema refinement). Cela consiste à restructurer le schéma avec des tables pour rendre certaines opérations plus efficaces, ou pour améliorer certains aspects de l'implémentation selon les exigences. Nous faisons cela parce que, lors de la traduction du niveau précédent vers le niveau [logique](, vous pouvez modifier certains modèles de conception pour mieux utiliser les outils fournis par le SGBD, qu'ils soient orientés table ou non.

#### 4. Conception physique (Index logiques, Clustering, Partitions)

À ce niveau, le SGBD implémente automatiquement le schéma que nous avons précédemment défini au niveau le plus proche du [matériel](https://www.ibm.com/docs/fr/db2-for-zos/12.0.0?topic=relationships-physical-database-design). Il traduit l'ensemble des tables et des associations que nous avons définies en [structures de données](https://docs.oracle.com/cd/A84870_01/doc/server.816/a76994/physical.htm) spécifiques comme des B-arbres (B-trees), des index et des algorithmes qui supportent leurs opérations. En substance, ce niveau est l'implémentation informatique du SGBD, qui gère la mémoire disque ou appelle le système d'exploitation, entre autres détails.

Cette implémentation de notre schéma par le SGBD est automatique. Nous devons simplement fournir une définition basée sur le schéma relationnel que nous avons créé précédemment, incluant les tables, les associations entre elles et les données que nous voulons insérer ou supprimer.

Grâce à cela, le SGBD traduit ces opérations "relationnelles" en opérations de bas niveau comme des instructions d'assemblage. Cela nous aide à maintenir l'[indépendance logique-physique](, car l'implémentation du SGBD peut être modifiée à tout moment sans affecter notre **schéma relationnel** ou sa fonctionnalité. Cela nous permet d'optimiser le code du SGBD sans avoir à réécrire tous les programmes "relationnels" qui définissent les bases de données.

#### 5. Niveau de stockage (Formats de blocs, structures de disque et accès)

Vous pouvez considérer ce niveau comme un sous-ensemble du précédent, car il est responsable du [stockage](https://www.geeksforgeeks.org/system-design/file-and-database-storage-systems-in-system-design/) des données en mémoire secondaire selon le schéma relationnel géré par le SGBD. Il effectue les requêtes nécessaires au système d'exploitation pour allouer de la mémoire et gère généralement les informations sur le disque au niveau de l'octet.

À cette fin, il emploie des techniques de bas niveau qui déterminent comment la mémoire disque disponible sera utilisée, y compris l'implémentation de structures de disque et le formatage des blocs de mémoire, entre autres.

%[ 

#### 6. Implémentation des applications et sécurité (Vues, Autorisations, Procédures)

Enfin, une fois la base de données construite, vous pouvez concevoir de nouvelles couches par-dessus sur lesquelles vous pouvez installer des applications et des services qui facilitent l'interaction avec la base de données. C'est-à-dire que vous pouvez simplifier son fonctionnement pour l'utilisateur final, par exemple en développant une application web en HTML, CSS et JavaScript pour obtenir les données de manière conviviale, au lieu d'utiliser du code SQL.

Certaines de ces couches sont également orientées vers la garantie de la [sécurité](https://www.ibm.com/fr-fr/topics/data-security) des données, en établissant des contrôles d'accès de plus haut niveau que le SGBD où l'utilisateur doit s'authentifier pour accéder aux données. Vous pouvez également chiffrer les données en utilisant certaines des fonctionnalités de ces couches.

## Chapitre 5 : Modèle relationnel (Données structurées)

Maintenant que vous comprenez certains des processus que nous utilisons pour concevoir des bases de données, nous allons nous concentrer sur les bases de données les plus simples, qui sont celles qui opèrent avec des données structurées. Ces bases de données sont généralement appelées **relationnelles** ou **structurées**. Elles sont formellement conçues à l'aide du modèle relationnel, qui est la formalisation du niveau conceptuel utilisé pour concevoir ce type de base de données.

La raison pour laquelle les bases de données relationnelles sont les plus simples réside dans la nature des données qu'elles stockent habituellement et les contraintes qui leur sont imposées, comme nous allons le voir maintenant. Nous discuterons simultanément des niveaux de conception conceptuelle et logique, où les éléments fondamentaux de ce type de système sont principalement représentés.

Il est important de différencier la façon dont ces éléments sont vus du niveau conceptuel et du niveau logique, car ils se réfèrent essentiellement à des concepts très similaires, et parfois équivalents – mais formellement ce sont des concepts différents. Dans une base de données relationnelle, l'information est structurée en entités liées les unes aux autres et composées d'une série d'attributs, ce qui est la vue conceptuelle du modèle.

### Table (Relation)

Comme mentionné précédemment, les données structurées sont celles qui suivent un schéma rigide et sont organisées sous forme de tables. Le composant fondamental pour stocker des informations dans une base de données relationnelle est donc la table, qui est parfois aussi appelée relation. Ce composant fait partie de la conception logique, puisque nous le définissons dans le SGBD. Ainsi, chaque fois que nous traitons des tables, nous nous référons au niveau de conception logique.

Voici un exemple :

| **CityID** | **Nom** | **Pays** | **Population** | **Superficie** |
| --- | --- | --- | --- | --- |
| 1 | Madrid | Espagne | 3 223 000 | 604,3 |
| 2 | Athènes | Grèce | 664 046 | 38,96 |
| 3 | New York | USA | 8 398 748 | 783,8 |
| 4 | Tokyo | Japon | 13 929 286 | 2 191,1 |
| 5 | Paris | France | 2 140 526 | 105,4 |

### Schéma

La table d'exemple **City** ci-dessus stocke des données sur différentes villes. La table a un schéma, qui est une série de données réservées pour décrire la structure de la table. C'est-à-dire que le schéma se compose du nom de la table, qui est ici **City**, ainsi que du nom et du type de tous les attributs qu'elle possède, correspondant aux colonnes.

Par exemple, si nous stockons des villes dans cette table, la colonne Nom correspond à l'attribut Nom de chaque ville, qui est une propriété que possèdent les entités villes, en plus des **associations** entre entités, qui dans certains contextes sont également appelées **propriétés**. Cet attribut doit avoir un type, comme string (chaîne de caractères) dans ce cas, pour déterminer quel genre de données il contiendra.

Ainsi, le nom de la table ainsi que les noms et types des attributs forment le schéma d'une table, lequel est principalement déterminé par les exigences des utilisateurs. Mais ce sont les concepteurs de bases de données qui décident comment modéliser les entités du domaine, quels attributs il est nécessaire d'inclure et les types de chacun.

### uplet (Tuple)

En plus d'un schéma, une table a également une instance, qui est l'ensemble des uplets qu'elle contient à un moment donné. Ici, par uplet, nous entendons une ligne de la table, car nous pouvons la voir mathématiquement comme un uplet **(valeur1, valeur2, valeur3...)** où toutes les valeurs pour une certaine ville sont présentes pour tous les attributs de la table.

Une particularité de l'instance est qu'il ne peut jamais y avoir plusieurs uplets identiques. Cela signifie, dans ce cas, qu'il ne peut pas y avoir deux villes ou plus ayant les mêmes valeurs pour tous les attributs en même temps. Cette restriction est imposée dans le modèle relationnel pur, bien que nous verrons en pratique que cette restriction peut ne pas être suivie pour faciliter certaines tâches.

C'est le cas parce que, dans le modèle relationnel pur, l'instance est considérée comme un ensemble d'uplets, et mathématiquement, un ensemble ne peut pas avoir d'éléments répétés. Mais dans l'implémentation pratique que nous verrons, l'instance est formellement modélisée avec un multiensemble (multiset) qui autorise les doublons, car chaque uplet est associé en interne à une valeur indiquant combien de fois il est répété dans le multiensemble.

### Domaine d'attribut

Précédemment, nous avons mentionné que chaque attribut a un domaine, ce qui permet au SGBD de déterminer comment les données de cette colonne seront stockées. Mais nous pourrions avoir un attribut comme **Population** où il n'est pas logique de stocker des nombres négatifs, tout comme pour la Superficie.

Pour éviter ces situations, le domaine de l'attribut peut être restreint. Par exemple, si nous définissons Population comme ayant uniquement le type de données INTEGER par défaut, il peut prendre n'importe quelle valeur de l'ensemble/domaine des entiers. Mais si nous voulons qu'il ne prenne que des valeurs positives, nous devons ajouter une contrainte (dont nous discuterons plus tard) afin que les valeurs possibles pour cet attribut, c'est-à-dire son domaine, ne soient que tous les entiers positifs nécessaires.

### Attribut dérivé

Un cas particulier d'attributs est celui des attributs dérivés. Leur valeur n'est pas stockée, mais est plutôt calculée à partir de la valeur d'autres attributs.

En reprenant l'exemple de la table **City**, supposons que nous ayons un attribut **Densité** qui doit indiquer la densité de population d'une ville. Dans ce cas, nous pouvons le définir comme un attribut dérivé, au lieu de calculer les valeurs au préalable et de les insérer dans la base de données. Ainsi, chaque fois que la **Densité** est interrogée, l'opération **Population/Superficie** sera effectuée, renvoyant la valeur à l'utilisateur dans l'uplet correspondant.

Nous pouvons voir un exemple plus clair si nous avons un attribut DateNaissance et que nous voulons calculer la valeur d'un autre attribut comme **Âge**. Ici, nous pouvons calculer l'attribut **Âge** directement à partir de **DateNaissance** comme s'il s'agissait d'une **"vue"** sur cet attribut. C'est-à-dire que nous pouvons voir une date de naissance comme s'il s'agissait d'un âge, à partir duquel nous pouvons dériver la valeur de l'attribut **Âge**. Nous discuterons du concept de vue plus tard plus en détail au niveau de l'implémentation.

Avant de passer à la représentation au niveau de la conception conceptuelle d'une table, il est important de comprendre pourquoi une table est parfois appelée une [relation](https://fr.wikipedia.org/wiki/Relation_\(base_de_donn%C3%A9es\)). Une relation est un sous-ensemble du [produit cartésien](https://fr.wikipedia.org/wiki/Produit_cart%C3%A9sien) des domaines que possèdent les attributs, mais vous pouvez le comprendre plus simplement comme un ensemble d'uplets qui respectent un schéma défini. Par exemple :

| **Lettre** | **Nombre** |
| --- | --- |
| A | 1 |
| A | 2 |
| B | 1 |
| B | 2 |

Dans cette table, nous pouvons supposer que les attributs **Lettre** et **Nombre** ont respectivement les domaines **{A, B}** et **{1, 2}**, de sorte que tout l'ensemble des uplets possibles que nous pouvons former avec ces domaines sont les uplets affichés dans la table elle-même.

Ces uplets proviennent du **produit cartésien** des deux domaines. Ainsi, si nous avions des domaines plus vastes, nous obtiendrions un produit cartésien beaucoup plus large. Un sous-ensemble de ses uplets est appelé une relation, et nous pouvons l'associer à l'instance d'une table, c'est pourquoi le terme relation est parfois utilisé pour désigner ce qui est en fait une table.

### Représentation conceptuelle

En mettant cela de côté, il n'est pas aussi important de se concentrer sur des détails formels comme le nom **relation**, mais plutôt de comprendre la structure d'une table et comment les données y sont stockées. Jusqu'à présent, tout ce que nous avons vu sur les tables se réfère au niveau de conception logique, qui est celui où nous travaillons réellement avec des tables. Mais au niveau conceptuel, il existe un élément très similaire à une table appelé une **entité**.

Selon le niveau conceptuel, une base de données relationnelle est un ensemble d'entités, où chacune peut être assimilée à une table. Chaque entité possède une série d'**attributs**, chacun avec un **domaine**, où au lieu d'attribut, on l'appelle généralement une propriété au niveau conceptuel.

![Entité City représentée dans un diagramme entité-relation. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751733945183/6d737d7b-f6f3-42af-ae91-3fae993524a0.png align="center")

En suivant l'exemple de la table City de tout à l'heure, au niveau conceptuel, il existe une entité appelée City, illustrée ci-dessus dans un [diagramme entité-relation **UML (Unified Modeling Language)**](https://www.freecodecamp.org/news/uml-diagrams-full-course/), qui est la manière la plus courante de représenter formellement ce type d'informations.

Parfois, nous pouvons utiliser la notation [**"Pattes de corbeau" (Crow's foot)**](https://www.freecodecamp.org/news/crows-foot-notation-relationship-symbols-and-how-to-read-diagrams/) pour le diagramme, mais ici nous utiliserons la même notation qu'un diagramme de classes en génie logiciel par souci de simplicité. C'est équivalent, c'est pourquoi les entités sont parfois appelées classes.

Pour bien comprendre ce qu'est une entité, considérez-la comme s'il s'agissait du schéma de la table, ou plutôt d'une classe en programmation orientée objet qui sert de modèle pour instancier des uplets. Gardez simplement à l'esprit qu'au niveau conceptuel, ils ne sont pas appelés uplets mais plutôt instances ou occurrences d'une entité.

Intuitivement, nous pouvons le voir comme si les attributs représentés dans l'entité étaient les valeurs réelles de la première ligne de la table équivalente – c'est-à-dire son schéma. De cette façon, si nous avons un schéma (c'est-à-dire un modèle), nous pouvons créer des instances de cette entité/schéma/modèle simplement en attribuant des valeurs à ces attributs. Ainsi, lorsque nous attribuons des valeurs aux propriétés d'une entité, nous avons une occurrence d'entité, qu'au niveau logique nous pouvons voir comme un uplet.

Par exemple, l'entité **City** peut être "instanciée" dans un "uplet" comme **[5, Paris, France, 2140526, 105.4]**. Mais au niveau conceptuel, nous devrions l'appeler une **occurrence** au lieu d'un uplet, car "instance" pourrait prêter à confusion avec le concept d'instance dont nous avons discuté précédemment au niveau logique.

```markdown
Entité : [CityID, Nom, Pays, Population, Superficie]    --->    uplet = Occurrence : [5, Paris, France, 2140526, 105.4]
```

Ainsi, chaque fois que nous voyons une boîte avec un nom et des propriétés dans un diagramme entité-relation, cela fait référence à une entité qui est logiquement équivalente à une table.

En ce qui concerne le concept d'instance que nous avons vu précédemment, ici il est appelé un **ensemble d'entités**, et il contient toutes les occurrences existantes de cette entité à un moment donné. Dans le diagramme, nous ne voyons que le modèle, pas l'ensemble avec les occurrences de cette entité (pensez aux uplets d'une table). En d'autres termes, le diagramme au niveau conceptuel sert à voir comment la base de données est structurée, et non à voir ses instances ou occurrences spécifiques, qui sont plus liées au niveau logique.

En ce qui concerne la notation, dans le diagramme entité-relation, l'entité est représentée dans une boîte où toutes ses propriétés (attributs) sont listées par nom et par type. Ici, le type ne doit pas correspondre exactement au type proposé par le SGBD dans la conception logique, car une traduction du niveau conceptuel au niveau logique est effectuée plus tard, comme nous l'avons vu précédemment.

À gauche de chaque attribut, un `-` est généralement placé pour indiquer qu'il s'agit d'un attribut privé. Mais ce concept n'est pas pertinent dans ce contexte de base de données, car il provient des utilisations données en génie logiciel à la notation de diagramme de classes que nous utilisons ici.

Enfin, les noms d'attributs sont généralement tous en minuscules, bien que selon le guide de style que vous suivez, cela puisse varier – comme ici, où nous autorisons les majuscules pour minimiser les changements de noms d'attributs lors de la traduction vers la conception logique.

### Groupe répétitif

Une fois que vous savez ce qu'est une entité, ou une table, et que la base de données est un ensemble d'entités liées les unes aux autres, vous devrez tenir compte d'une restriction importante concernant la table elle-même en tant que structure de stockage.

| **CityID** | **Nom** | **Pays** | **Température** |
| --- | --- | --- | --- |
| 5 | Paris | France | 7,44,20,90,1 |

Par exemple, si nous avons une table City similaire à celle ci-dessus où nous voulons seulement enregistrer les températures de la ville à différents moments, la première option que nous pourrions envisager est de stocker toutes les températures que chaque ville a ou a eues dans un seul attribut Température, toutes ensemble.

Mais cela n'est pas autorisé dans les bases de données structurées pour des raisons d'efficacité (ainsi que formellement, comme vous le verrez plus tard). Plus précisément, cette situation est connue sous le nom de groupe répétitif, et elle se produit lorsque nous devons stocker un nombre indéterminé de valeurs dans un attribut.

Par exemple, si nous n'avons besoin de stocker qu'un maximum de 5 températures qu'une ville peut avoir, nous pourrions faire du type de données de Température un tableau d'entiers d'une longueur de 5, qui serait rempli au fur et à mesure que nous obtenons des mesures de température. Mais si nous ne savons pas combien de températures nous allons mesurer, nous ne pouvons pas fixer de limite supérieure à la taille de la valeur que nous allons stocker, nous ne pouvons donc pas définir de taille spécifique pour la longueur du type de données de cet attribut. Cela crée un groupe répétitif.

Quoi qu'il en soit, même si nous pouvions fixer une taille pour des structures de données comme un tableau, elles ne sont généralement pas autorisées en raison de l'incertitude de la taille que le développeur pourrait fixer pour ce tableau (également considéré comme un groupe répétitif).

Dans le même temps, cette incertitude est la raison pour laquelle les **groupes répétitifs** posent un problème pour l'implémentation physique de la base de données. Comme nous ne savons pas de quel espace nous aurons besoin pour les représenter, nous pourrions finir par gaspiller beaucoup de mémoire en essayant de gérer cette incertitude, ainsi qu'à la [fragmenter](https://stackoverflow.com/questions/3770457/what-is-memory-fragmentation), ou à compliquer la logique d'implémentation pour tenter de minimiser l'impact de ce gaspillage et de cette fragmentation de la mémoire.

#### Comment éviter un groupe répétitif

Une façon de résoudre le problème des groupes répétitifs est de stocker chaque mesure de température dans un uplet séparé. Si toutes les mesures ne peuvent pas être stockées dans une seule valeur d'attribut, une option consiste à dupliquer les informations des autres attributs pour créer plusieurs uplets, chacun stockant une mesure de température spécifique.

| **CityID** | **Nom** | **Pays** | **Température** |
| --- | --- | --- | --- |
| 5 | Paris | France | 7 |
| 5 | Paris | France | 44 |
| 5 | Paris | France | 20 |
| 5 | Paris | France | 90 |
| 5 | Paris | France | 1 |

Comme vous pouvez le voir, nous avons dupliqué les informations pour stocker chaque mesure de température dans un uplet, ce qui évite de les accumuler toutes dans une seule valeur du même uplet. Mais la répétition des données crée une redondance (inutile) dans la base de données, ce qui est un problème.

La redondance n'est pas un problème dans toutes les situations, car elle peut parfois être utile pour assurer la disponibilité des données. Mais dans ce cas, nous pouvons voir qu'elle est complètement inutile. D'abord, parce qu'elle augmente considérablement l'espace nécessaire pour stocker les données de la ville en répétant les informations de la ville. Ensuite, parce que le fait d'avoir les données de la ville répétées tant de fois signifie que chaque fois que ces données doivent être modifiées, vous devrez apporter des modifications à tous les uplets enregistrant les températures, ce qui rend les opérations trop longues. Et si le schéma est modifié pour ajouter ou supprimer des attributs, toutes les données de leurs colonnes respectives doivent être supprimées – donc s'il y a beaucoup de données répétées, ces opérations auront également une latence élevée.

### Incohérence des données

D'un autre côté, si dans l'exemple précédent nous insérons une mesure de température et que, pour une raison quelconque, une erreur se produit pendant l'opération, nous pourrions nous retrouver dans une situation comme celle-ci :

| **CityID** | **Nom** | **Pays** | **Température** |
| --- | --- | --- | --- |
| 5 | Paris | France | 7 |
| 5 | Paris | Chine | 44 |

Ici, vous pouvez voir que lors de l'insertion de la mesure avec une température de **44**, une erreur s'est produite et l'uplet a été enregistré avec une valeur de **Pays** incorrecte. Ce n'est pas courant, mais si nous choisissons de résoudre le problème du groupe répétitif de cette manière, nous insérerons des valeurs en double plus souvent que nécessaire, ce qui rendra plus probable l'apparition de ce type d'erreurs.

Le fait d'avoir les mêmes informations dupliquées mais avec des valeurs contradictoires indique que notre base de données présente une incohérence. Cela se produit lorsque la même information est dupliquée à divers endroits de la base de données et que les valeurs sont contradictoires, comme dans cet exemple où nous avons plusieurs mesures de température pour ce qui semble être la même ville mais avec une valeur de pays incorrecte.

Pour s'assurer qu'il s'agit d'une incohérence, nous devrions examiner les valeurs de clé qui identifient de manière unique chaque uplet, ce dont nous discuterons plus tard. Mais intuitivement, nous devons nous concentrer sur les valeurs d'attribut qui nous permettent d'identifier de manière unique un uplet. Si ces valeurs se répètent dans plusieurs uplets et qu'il y a une incohérence dans les autres attributs, alors nous avons une incohérence.

D'un autre côté, si dans le dernier exemple la valeur de **Pays** du deuxième uplet était **"France"**, nous n'aurions aucune incohérence, même si les valeurs de température ne correspondent pas. Il est donc important de comprendre que l'incohérence dépend principalement de la sémantique du schéma, c'est-à-dire de ce que chaque attribut signifie.

Enfin, pour résoudre le problème des groupes répétitifs, vous devrez généralement affiner le schéma – c'est-à-dire le transformer. Dans ce cas précis, nous allons effectuer une opération de normalisation, que nous verrons comment faire plus tard. Cela consiste à séparer une table comme celle que nous avions auparavant avec des informations dupliquées en plusieurs tables :

| **CityID** | **Nom** | **Pays** |
| --- | --- | --- |
| 5 | Paris | France |

| **ReadingID** | **CityID** | **Température** |
| --- | --- | --- |
| 1 | 5 | 7 |
| 2 | 5 | 44 |
| 3 | 5 | 20 |
| 4 | 5 | 90 |
| 5 | 5 | 1 |

Il existe maintenant une table **City** très similaire à l'originale, mais avec la différence qu'elle ne stocke qu'un enregistrement des villes existantes, et non les températures enregistrées dans celles-ci.

De plus, il existe une autre table que nous pouvons appeler Readings, qui contient les mesures de température pour chaque ville. Dans cette table, chaque uplet contient une mesure et un identifiant qui détermine la ville où la mesure a été prise, qui est dans ce cas **CityID**.

Par exemple, si la mesure a été prise à Paris et que cette ville a une valeur CityID de 5, alors le CityID dans la table **Readings** sera 5 pour les mesures de cette ville. Cela évite de dupliquer toutes les informations de la ville comme c'était le cas auparavant.

En faisant cela, nous évitons les problèmes d'incohérence potentiels qui se posaient auparavant, et nous économisons également de l'espace disque en ne dupliquant pas d'informations inutiles. Plus important encore, cela empêche l'apparition du groupe répétitif.

Pour cela, nous avons dû "compliquer" ou plutôt enrichir le schéma de la base de données dans une certaine mesure, c'est-à-dire les tables qui la composent et les schémas qui les forment. Mais la complexité dans les bases de données structurées ne vient pas du fait d'être structuré, mais du domaine modélisé et de ses opérations. En d'autres termes, le modèle relationnel de données structurées n'est pas complexe en soi, car il s'agit simplement d'un modèle. Ce qui cause réellement la complexité, c'est la façon dont nous utilisons ce modèle pour refléter les exigences du domaine.

### Associations d'entités

Dans le contexte de la conception conceptuelle, une base de données relationnelle n'est pas seulement composée d'entités (tables), car cela ne nous permet que de modéliser l'existence d'"objets" dans le domaine. La plupart du temps, ces objets auront des associations entre eux, ce qui signifie qu'ils seront liés.

Ainsi, dans la conception conceptuelle, nous avons le concept d'**association d'entités**, qui décrit comment les "objets" sont liés les uns aux autres. C'est essentiel pour refléter la structure réelle de l'information.

![Diagramme entité-relation montrant les entités City et Person, où chaque ville peut avoir une ou plusieurs personnes y résidant. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751783067882/835a4c1c-1913-4847-9649-f2082d19d410.png align="center")

Par exemple, dans un domaine, nous pouvons avoir des entités comme celles ci-dessus, **City** et **Person**. Celles-ci modélisent l'existence de personnes et de villes dans le domaine. Mais outre l'existence des entités elles-mêmes, il est possible qu'elles aient des relations entre elles que nous pouvons modéliser dans notre diagramme – comme une personne vivant dans une certaine ville.

Dans ce cas, nous utilisons une association pour permettre à une personne dans notre système de vivre dans une ville, ce qui signifie que nous utilisons une association pour modéliser cette relation entre les deux entités.

À première vue, nous pouvons voir que l'association est représentée dans le diagramme entité-relation comme une relation établie entre entités – mais il est important de se rappeler que les entités sont des "modèles" à partir desquels des occurrences d'entités sont générées lors de l'implémentation du système (c'est-à-dire des uplets spécifiques). Ainsi, lorsque nous introduisons une association au niveau conceptuel, nous devons la voir en termes d'uplets qui seront générés plus tard à partir des entités liées.

Par exemple, ici la relation peut se produire entre une occurrence (uplet) d'une ville et de nombreuses occurrences d'une personne, puisque de nombreuses personnes peuvent vivre dans une ville. Mais l'inverse peut ne pas être vrai selon les exigences du domaine, qui peuvent déterminer qu'une personne (occurrence de l'entité **Person**, ou uplet de la table **Person**) ne peut vivre que dans une seule ville, comme nous le supposons dans ce cas.

#### Rôle de l'association

Dans un diagramme entité-relation, la notation de l'association est généralement représentée par une ligne reliant deux entités, connue sous le nom d'association binaire. Mais il existe des associations de degré supérieur (que nous n'aborderons pas ici par souci de simplicité) qui relient un nombre arbitraire d'entités dans une seule association.

Un rôle et une direction sont généralement ajoutés à cette ligne pour clarifier la sémantique de la relation. Le rôle est un mot ou une phrase écrit au-dessus de la ligne d'association et désigne le rôle qu'une entité a dans la relation représentée par rapport à la direction définie à côté du rôle.

Par exemple, dans le diagramme ci-dessous, nous avons une association entre une personne et une ville. Ainsi, dans l'association, le rôle donné à la personne est "vit" dans la ville avec laquelle elle est associée, car la direction a été définie de la personne vers la ville avec la flèche à côté du rôle. En d'autres termes, dans cette relation entre les deux entités, la fonction que remplit la personne est de "vivre" dans la ville avec laquelle elle est associée.

![Diagramme entité-relation montrant City et Person, où chaque ville a un ou plusieurs résidents. Image de l'auteur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751789958682/1f5aa10e-3120-49a1-a7f0-9791a3f2e25e.png align="center")

Ce rôle n'a pas besoin d'être inclus dans toutes les associations, et il n'est pas non plus nécessaire d'établir une direction. Mais dans certains cas, cela nous aide à comprendre le diagramme et le domaine, ce qui est le but du diagramme lui-même.

De plus, le rôle n'est pas rigide et peut être modélisé de plusieurs façons. Par exemple, dans ce cas, nous pouvons inverser la direction de l'association et dire que la ville a le rôle d'"avoir des résidents", qui sont les personnes avec lesquelles elle est associée. Cela modéliserait l'existence de personnes vivant dans la ville.

#### Cardinalité

En continuant avec les différents éléments d'une association, nous avons la **cardinalité**, qui décrit combien d'**occurrences** (uplets) d'une entité peuvent ou doivent être associées à combien d'occurrences d'une autre entité. Nous représentons cela avec des nombres des deux côtés de la ligne d'association qui désignent respectivement la cardinalité **minimale** et **maximale**.

Pour comprendre cela en utilisant l'exemple précédent, nous savons qu'une personne ne peut vivre que dans une seule ville, donc une entité personne sera associée à au plus une ville. À son tour, nous pouvons également supposer que chaque personne doit vivre dans une ville, ce qui signifie qu'il n'y a pas de personnes vivant dans les bois en dehors de la société. Ainsi, puisque chaque personne doit être associée à exactement une ville, la multiplicité que nous mettons du côté de l'entité ville est 1...1, ce qui s'écrit simplement 1.

Ici, le premier 1 est la cardinalité minimale, indiquant que chaque personne doit être associée à au moins une ville, tandis que l'autre 1 est la cardinalité maximale, indiquant que chaque personne peut être associée à au plus une ville. Par souci de simplicité dans le diagramme, le chiffre 1 est généralement utilisé pour désigner les deux cardinalités à la fois. De plus, lorsque nous parlons de personnes et de villes ici, nous nous référons aux occurrences réelles des entités, qui au niveau logique sont des uplets.

Si nous regardons l'autre côté de l'association, nous voyons qu'elle a une multiplicité (parfois appelée [Le rôle des données dans le monde numérique d'aujourd'hui](#heading-le-role-des-donnees-dans-le-monde-numerique-daujourdhui)) 1...*, où 1 est la cardinalité minimale, indiquant qu'une ville doit être liée à au moins une personne. Cela signifie que dans toutes les villes de notre domaine, il doit y avoir **au moins** un habitant.

D'un autre côté, l'astérisque * dans la **cardinalité maximale** est une façon de noter qu'il n'y a pas de valeur spécifique à donner à cette cardinalité – cela peut être n'importe quelle quantité. Cela signifie qu'une ville peut être associée à un nombre arbitraire de personnes, indiquant que les villes de notre domaine peuvent avoir n'importe quel nombre d'habitants.

Comme l'astérisque désigne une quantité quelconque et non bornée, nous n'avons pas à nous soucier de sa cohérence avec la cardinalité minimale. C'est-à-dire que même si nous fixons la cardinalité minimale à 1, en utilisant un astérisque pour le maximum, nous indiquons que le maximum peut être n'importe quel nombre de 1 à l'infini. Cela signifie que les villes auront au moins un habitant et au plus un nombre infini.

À partir de la **cardinalité minimale**, nous pouvons introduire les concepts d'**optionnalité** et d'**obligation**. Par exemple, nous avions auparavant des cardinalités minimales supérieures à 0, ce qui indique qu'une personne doit toujours être associée à une ville, ou qu'une ville doit toujours être associée à au moins une personne. Cela signifie que lorsque des occurrences de ces entités sont créées, elles doivent respecter la restriction imposée par la cardinalité minimale d'être associées à une occurrence de l'autre entité. Ainsi, lors de la création, elle doit être directement associée à l'autre entité qu'indique l'association, pour respecter la cardinalité minimale.

Pour voir cela au niveau de la conception logique, nous devons d'abord introduire les outils de ce niveau avec lesquels les associations sont implémentées – bien que pour l'instant, nous puissions le visualiser en pensant au paradigme orienté objet, où si nous instancions un objet personne, il doit avoir une **référence** vers un autre objet ville, et vice versa.

![Diagramme entité-relation montrant les entités City et Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751792178992/276f82ef-6895-487c-b7a0-7f1d01d9525f.png align="center")

En ce qui concerne l'optionnalité, considérons un autre cas possible où une ville peut avoir un nombre arbitraire de résidents, y compris être inhabitée, c'est-à-dire vide, puisque nous avons fixé la cardinalité minimale à 0 et la maximale à *. Cela peut également être représenté plus simplement en utilisant uniquement l'astérisque, indiquant une quantité arbitraire incluant 0.

Maintenant, supposons également qu'une personne puisse vivre dans une ou deux villes, sa multiplicité correspondante est donc modifiée en 1..2, indiquant qu'une personne doit être associée à au moins une ville et au plus deux villes simultanément à n'importe quel moment de son cycle de vie.

Cela se produit car le diagramme entité-relation est **instantané**, et non **historique**, ce qui signifie que ce que nous voyons dans le diagramme est une représentation instantanée de notre domaine, et non une représentation de son cycle de vie ou de son évolution dans le temps.

Ainsi, lorsque nous voyons qu'une association a une multiplicité de 1..2 comme dans ce cas, nous devons penser qu'à n'importe quel moment donné, une personne doit être associée à au moins une ville et au plus deux villes. Nous ne devrions pas penser qu'une personne doit avoir été liée à au moins une ville et au plus deux villes tout au long de sa vie entière.

Ici, nous pouvons voir qu'une ville peut n'avoir aucun résident en raison de la cardinalité minimale de 0 que nous avons placée du côté de la personne, indiquant qu'une ville peut ne pas être associée à une personne. Grâce à cela, nous pouvons modéliser l'optionnalité, qui consiste à permettre à une association de ne pas se produire. C'est-à-dire que lorsque nous créons une ville à partir de son entité (modèle), nous n'avons pas à l'associer à une personne, puisqu'elle peut être associée à 0 personne au minimum. Cela signifie qu'il n'est pas nécessaire d'ajouter une référence à une personne car une ville peut être abandonnée et n'avoir aucun résident.

![Diagramme entité-relation montrant les entités City et Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751792219256/f668bb15-db83-492b-ac95-c788ee6c8c19.png align="center")

Pour bien comprendre l'optionnalité, nous pouvons modifier à nouveau l'exemple de sorte qu'une personne puisse être associée soit à aucune ville, soit à une ville, indiquant que la personne peut ne vivre dans aucune ville ou peut vivre dans une seule. De plus, de l'autre côté de l'association, nous changeons également la cardinalité maximale à 500, indiquant qu'une ville peut avoir un nombre arbitraire de résidents entre 0 et 500, ce qui signifie qu'elle peut être associée à n'importe quel nombre de personnes de 0 à 500, inclus. Cela signifie que le fait d'avoir des résidents est optionnel.

Grâce à cela, il devrait être clair que nous pouvons fixer les cardinalités comme nous le souhaitons en fonction du domaine et des exigences – mais nous devons toujours nous assurer qu'elles sont correctes et logiques. Par exemple, vous ne pouvez pas fixer une cardinalité maximale strictement inférieure à la cardinalité minimale.

Dans ce cas, quelque chose de particulier se produit : des deux côtés, nous avons une cardinalité minimale de 0, ce qui signifie que nous avons une optionnalité. Ainsi, lorsque nous créons de nouvelles instances des entités, elles n'ont pas à être associées à des instances d'entités de l'autre côté de l'association. Nous pouvons voir cela comme si l'association que nous avons modélisée était entièrement optionnelle.

Pour conclure, bien que nous puissions fixer n'importe quel nombre pour les cardinalités minimales et maximales en fonction du domaine modélisé, les plus courantes sont 1..1, 1..M ou M..N, où N et M peuvent être des nombres arbitraires, y compris 0 dans le cas de N..M, tant qu'ils ne sont pas tous les deux 0 en même temps (car dans ce cas, l'association ne pourrait pas exister).

#### Associations récursives

D'un autre côté, une association ne doit pas nécessairement relier plusieurs entités. Nous pouvons l'utiliser pour modéliser une relation entre des occurrences de la **même entité**. Par exemple, si nous voulons modéliser la relation d'amitié entre les personnes de notre domaine, nous pouvons utiliser une **association récursive** dans l'entité Person :

![Diagramme entité-relation où Person a une relation d'amitié avec elle-même. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751795267979/91b3c5e3-5642-40eb-a270-721ceb8cd93a.png align="center")

Tout d'abord, il est très pratique d'établir un rôle dans les associations récursives, car c'est le moyen le plus simple de représenter leur sémantique afin que nous puissions les comprendre facilement en regardant le diagramme.

Mais dans ce cas, il n'est pas aussi utile de spécifier la direction de l'association puisque la relation d'amitié peut être considérée comme symétrique. Ici, nous avons modélisé la relation d'amitié de sorte qu'une occurrence de Person puisse être associée à n'importe quel nombre d'autres occurrences de **Person**, y compris aucune, ce qui indique que dans notre domaine, une personne (occurrence de l'entité Person) peut avoir un nombre arbitraire d'amis, y compris 0.

En ce qui concerne la notation, cela ne fait aucune différence d'utiliser 0..* ou *, car ils indiquent la même chose – mais nous devrions toujours utiliser la notation la plus courte et la plus simple à comprendre.

En résumé, une association récursive est simplement une association où les deux entités liées sont les mêmes. Dans ce cas, l'association d'amitié relie nécessairement des personnes à des personnes, ce qui signifie qu'elle établit quelles personnes sont amies entre elles.

#### Entité associative

Maintenant que nous savons ce que sont les associations, découvrons le concept d'**entité associative**. Dans certains cas, on l'appelle aussi une **propriété**, tout comme les **associations** elles-mêmes. Dans l'exemple suivant, il existe des villes dans un domaine qui peuvent accueillir de 1 à 500 habitants, tant que la restriction implicite d'avoir au moins un résident est respectée. De plus, une personne peut vivre dans un nombre arbitraire de villes entre 0 et 3.

![Diagramme entité-relation montrant les entités City et Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751797687686/758c9f22-ceb2-4c01-a0be-34219c1ee592.png align="center")

Le diagramme conceptuel ci-dessus modéliserait cette situation. En l'état, nous ne pouvons stocker aucune information sur le séjour de la personne dans la ville, ce qui signifie que nous ne pouvons pas enregistrer d'informations telles que les dates auxquelles elle a commencé à vivre dans cette ville ou a déménagé dans une autre. Si nous essayons de le faire, nous aurons plusieurs options qui mènent à certains problèmes dans la base de données.

D'une part, nous pourrions choisir d'ajouter des attributs tels que **DateDébut** et **DateFin** à l'entité **Person** pour déterminer les dates respectives auxquelles une personne a commencé à vivre dans une ville ou a déménagé dans une autre. Mais cela ne fonctionnerait même pas si la multiplicité 0..3 de la ville était 1..1, car au cours de la vie de la personne, même si elle ne peut vivre que dans une seule maison à la fois dans le cas 1..1, il est possible que la personne déménage plusieurs fois au cours de sa vie. Cela nécessiterait l'enregistrement de plusieurs paires **(DateDébut, DateFin)**. Ainsi, comme nous devons stocker plusieurs paires de ces dates, un groupe répétitif serait généré dans les propriétés (attributs) respectives, nous obligeant à affiner le schéma.

D'autre part, nous pourrions stocker ces attributs dans l'entité **City**, mais nous rencontrerions un problème très similaire ici. Nous devrions enregistrer plusieurs paires de valeurs **(DateDébut, DateFin)** pour chaque personne, avec la complexité supplémentaire qu'une ville peut avoir de nombreux résidents. Cela créerait également un groupe répétitif, ainsi que le problème de l'association de chaque paire **(DateDébut, DateFin)** avec la bonne personne.

![Diagramme entité-relation où City et Person sont liées via Residence. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751797354936/4c721372-a21c-4aa3-8ddb-29d81ecbc830.png align="center")

Pour remédier à cette situation, l'idéal serait de pouvoir stocker ces attributs au sein de l'association elle-même. De cette façon, lorsqu'une personne commence à vivre dans une ville, son association contiendrait ces attributs, et elle pourrait enregistrer la date à laquelle la personne a commencé à vivre dans la ville ainsi que la date à laquelle elle s'arrête. Cette valeur (quand elle cesse de vivre dans la ville) peut être laissée vide ou fixée à "**NULL**" jusqu'à ce qu'elle parte réellement et que l'association ne soit plus valide.

Pour y parvenir, au niveau conceptuel, on utilise des entités associatives. Ce sont des entités dont l'objectif principal est de permettre à notre base de données de stocker des informations sur les associations entre entités.

Comme vous pouvez le voir, les classes associatives sont **"liées"** aux associations entre entités, et non directement avec d'autres entités, et elles n'ont pas de multiplicité ou de rôles. C'est parce qu'elles n'existent que lorsque l'association entre plusieurs entités est réellement établie. Par exemple, lorsqu'une personne commence à vivre dans une ville, elle s'associe à une ville, et cette association se rapporte à une occurrence de la classe associative où les attributs respectifs comme DateDébut et DateFin sont stockés.

Ainsi, pour chaque association personne-ville que nous avons, il y aura également une occurrence de l'entité **Residence** avec les valeurs de ses propriétés correspondantes. Gardez également à l'esprit que cette association n'existe pas tout le temps, car la personne peut cesser de vivre dans cette ville – l'association elle-même peut donc cesser d'être valide ou, plutôt, cesser d'exister conceptuellement.

Mais selon la façon dont nous traduisons le diagramme relationnel vers la conception logique de la base de données, nous pourrions vouloir enregistrer les valeurs DateDébut et DateFin qu'avait l'occurrence de l'entité associative respective.

Si nous voulons cela, nous devrons le spécifier dans le modèle logique de la base de données ou dans le modèle conceptuel avec une note dans la marge du diagramme. C'est parce qu'au niveau conceptuel, il n'y a pas d'outils spécifiques au-delà des notes pour spécifier ce genre de détails, qui sont plus liés à la conception logique.

#### Agrégation et Composition

Puisqu'un **diagramme entité-relation UML** est utilisé au niveau conceptuel, il existe des modificateurs que nous pouvons utiliser dans les associations pour leur donner une signification particulière. Mais cela n'a aucun effet au niveau logique – ce qui signifie que l'introduction de ces modificateurs dans le diagramme conceptuel n'implique aucun type de changement au niveau logique. Ils sont simplement utilisés pour clarifier les détails du domaine modélisé.

![Diagramme entité-relation où City est composée d'instances de Person et chaque personne est composée d'un seul Brain. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751810875604/7b9044be-8d9b-43f2-8d80-61a190c23b6b.png align="center")

D'une part, une association peut être de type agrégation, comme entre Person et City, où l'agrégation est désignée par un losange vide et signifie qu'une ville peut être composée de personnes. Cela signifie que l'entité avec le losange est composée d'entités de l'autre côté de l'association.

De plus, dans le cas spécifique où nous créons et détruisons des occurrences d'entités en même temps, l'agrégation devient une composition, désignée par un losange plein. Elle fonctionne alors de la même manière que l'agrégation – la seule différence étant la signification qu'elle véhicule.

Par exemple, dans le diagramme ci-dessus, nous avons modélisé qu'une personne est composée d'un seul cerveau. Comme le cerveau d'une personne ne peut pas exister indépendamment de la personne, l'association est désignée comme une composition. C'est parce que l'agrégation permettrait au cerveau d'exister indépendamment, ce qui n'est pas possible.

Si nous regardons cela à l'inverse, la composition n'empêche pas la personne d'exister sans être liée à un cerveau, bien que la cardinalité 1..1 que nous avons placée des deux côtés modélise cette situation, exigeant que toutes les personnes aient exactement un cerveau.

La chose importante à comprendre est que l'agrégation et la composition ne sont que des associations avec une signification supplémentaire. Cela signifie qu'elles n'influencent pas la conception logique de la base de données elle-même, et encore moins au niveau de l'implémentation.

### Généralisation et Spécialisation

Une autre caractéristique du modèle relationnel est que, outre la modélisation des associations entre entités comme nous l'avons vu, il peut également modéliser d'autres types de relations entre entités. Cela peut être utile dans de nombreuses situations.

Par exemple, si nous avons un domaine où il y a des personnes qui peuvent être des clients ou des employés, nous pouvons utiliser une relation de généralisation et de spécialisation comme celle-ci :

![Diagramme entité-relation avec héritage où Client et Employee sont des sous-classes de Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751812519420/7e7fe801-22df-4411-862d-e74a1b56e263.png align="center")

Les relations de généralisation-spécialisation fonctionnent de la même manière qu'en orientation objet. Nous avons une classe comme **Person** avec un ensemble d'attributs, permettant des spécialisations de cette classe comme **Client** ou **Employee**, où toutes les instances sont également des personnes mais avec des attributs plus spécifiques.

Dans le cas de Client, il s'agit d'une entité spécialisée dérivée de l'entité Person, elle hérite donc de tous les attributs de son entité parente puisqu'un client est aussi une personne. En plus de ces attributs hérités, elle en possède d'autres spécifiques au fait d'être un client. Ainsi, lorsqu'une instance de l'entité Client est créée, considérez-la comme ayant tous les attributs de Client et de Person en même temps. La même chose se produit avec Employee mais avec ses attributs respectifs.

![Diagramme de Venn où Client et Employee sont des sous-ensembles de Person, avec un chevauchement possible. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751814124946/fa1daef2-46b0-47a8-8f62-c32642d5a165.png align="center")

Si nous regardons cela du point de vue de la [théorie des ensembles](https://fr.wikipedia.org/wiki/Th%C3%A9orie_des_ensembles), nous avons d'abord l'entité Person, qui donne naissance à un ensemble d'entités qui sont des personnes, c'est-à-dire les occurrences de cette entité. Au sein de tout cet ensemble, il est possible que, outre les occurrences de Person, il y ait des occurrences de Client, puisque chaque client est une personne. Ainsi, dans l'ensemble des personnes, il y en aura qui sont des clients. Cela se produit également avec Employee, où dans l'ensemble des personnes, il y aura également des employés, tous étant des personnes.

De plus, rien n'empêche une personne d'être à la fois client et employé, il y aura donc également des éléments dans l'ensemble qui sont à la fois client et employé. Mais ce détail est plus proche de la conception logique de la base de données que de la représentation conceptuelle de la généralisation et de la spécialisation présentée ici. Dans ce cas, ces noms indiquent que des classes comme Person sont plus générales que Client, qui sont leurs spécialisations respectives.

### Pièges des associations d'entités

Lorsque nous sommes à l'étape de la conception conceptuelle et que nous créons le diagramme entité-relation, il est courant de rencontrer des structures d'association qui semblent initialement correctes mais qui, lorsqu'elles sont implémentées dans un SGBD, entraînent des ambiguïtés ou des problèmes inattendus qui nous obligent à affiner la conception conceptuelle. L'une de ces structures est le **Piège en éventail (Fan Trap)** :

![Exemple de piège en éventail. Image de l'auteur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751814711606/798ec2c1-20dc-47d0-905b-acdc8becc39f.png align="center")

Le piège en éventail apparaît lorsque nous avons une classe "centrale" comme **City** qui est associée en forme d'"éventail" à deux autres, Person et Pool, où chacune a une cardinalité maximale de son côté. Cela signifie qu'une ville peut être associée à de nombreuses personnes et à de nombreuses piscines en même temps.

Cette situation est initialement correcte, mais le problème survient lorsque nous voulons savoir quelles personnes d'une certaine ville vont à quelle piscine. Cela devient compliqué car si on nous donne une certaine personne, nous pouvons connaître sa ville, car nous avons défini qu'une personne ne peut vivre que dans une seule ville. Mais la ville peut avoir de nombreuses piscines, nous ne savons donc pas à quelle piscine spécifique la personne se rend. Nous pouvons seulement savoir quelles piscines possède la ville où elle vit. De plus, la ville pourrait n'avoir aucune piscine, étant donné la cardinalité minimale de 0 du côté de la piscine.

D'un autre côté, si on nous donne une piscine, nous pouvons déterminer à quelle ville elle appartient. Ensuite, avec cette ville, nous pouvons trouver le groupe de personnes qui y vivent, ce que nous pouvons utiliser pour résoudre la question précédente – mais d'une manière beaucoup plus complexe.

Pour résoudre ce problème, il existe de nombreuses alternatives, bien que la plus simple dans ce cas consiste à ajouter une association explicite entre **Person** et **Pool** pour modéliser le fait qu'une personne se rend dans une piscine. Mais si nous n'allons pas effectuer ce type de requêtes fréquemment, il n'est peut-être pas utile de compliquer le diagramme.

![Exemple de piège en gouffre. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751818303502/70eecb3e-f2f1-4989-9348-afb81fb71346.png align="center")

Il existe également le **Piège en gouffre (Chasm Trap)**, qui est similaire à un piège en éventail mais avec des différences importantes. Par exemple, dans le diagramme ci-dessus, vous pouvez voir un piège en gouffre. Il se produit lorsqu'on nous donne une ville et qu'on nous demande de trouver les piscines qui s'y trouvent. La seule chose que nous puissions faire est d'obtenir le groupe de personnes vivant dans cette ville et, à partir de ce groupe, d'identifier certaines des piscines que possède la ville.

En d'autres termes, chaque piscine peut avoir ou non une association avec une personne, puisque toutes les personnes ne vont pas à la piscine. Ainsi, si nous essayons de trouver toutes les piscines d'une ville en regardant simplement les piscines où se rendent les résidents de la ville, nous pourrions rencontrer des situations où aucun résident de la ville ne se rend à la piscine. Ainsi, toutes les piscines profiteront de la cardinalité 0..30 du côté de Person pour n'avoir aucune personne associée, ce qui signifie que personne ne se rend dans ces piscines.

Donc, s'il y a des piscines que personne ne visite, nous ne pourrons pas les trouver via un groupe de personnes. Cela signifie que, pour une ville donnée, nous pourrions ne pas connaître toutes les piscines qu'elle possède, car si nous résolvons la requête de cette manière, nous ne pouvons être sûrs de connaître que les piscines que les résidents de la ville visitent. Mais s'il y a une piscine que personne ne visite, alors cette piscine ne sera pas accessible via une personne. En d'autres termes, les personnes ne verront pas ces piscines, puisque la relation 1..* les oblige à visiter une piscine – mais il peut toujours arriver que personne ne visite une certaine piscine.

La solution à ce problème est pratiquement la même que pour le piège en éventail, bien qu'il existe de nombreuses alternatives selon le domaine et les exigences. Il existe également d'autres situations pouvant mener à ces problèmes ou ambiguïtés que vous pouvez [approfondir ici](https://koushik-dutta.medium.com/avoiding-pitfalls-a-guide-to-sql-traps-and-how-to-solve-them-acdc3a95c74f).

### Clés

Jusqu'à présent, nous avons parlé d'entités et d'associations au niveau conceptuel, ainsi que de tables au niveau logique. En continuant avec le niveau logique, nous n'avons pas encore introduit de mécanisme pour identifier de manière unique les uplets contenus dans une table. Cela peut être très utile puisque les uplets sont des points de données – c'est-à-dire des occurrences d'une entité, comme des personnes, des villes, etc.

Les **identifier de manière unique** facilite l'exécution d'opérations ou de requêtes sur la table. Cela nous permet également d'implémenter des associations entre entités au niveau logique grâce à des références entre tables.

Les clés sont des ensembles d'attributs utilisés pour identifier de manière unique chaque uplet d'une table. La combinaison de valeurs de ces attributs doit être différente pour chaque uplet, de sorte qu'aucun uplet ne soit identique.

Pour comprendre ce concept, commençons par examiner les différents types de clés et leur utilité principale.

#### Superclés

Les superclés sont des ensembles d'attributs qui identifient de manière unique chaque uplet d'une table. C'est le type de clé le plus général. Tant que la combinaison de valeurs pour ces attributs est unique pour chaque uplet, l'ensemble d'attributs est qualifié de superclé.

Voici un exemple :

| **ID** | **SSN** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- | --- |
| 30 | 74 | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 22 | 59 | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 95 | 10 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 21 | 32 | David Brown | 2001-01-30 | david.brown@example.com |
| 47 | 61 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Dans ce cas, nous avons une table appelée **Person** où chaque ligne stocke les données d'une personne. Chaque personne possède un numéro d'**ID** gouvernemental, ainsi qu'un **numéro de sécurité sociale (SSN)**, un nom et d'autres détails.

Une superclé possible serait les attributs **{ID, Nom}**, car parmi toutes les personnes qui existent, deux personnes ne peuvent pas avoir le même nom et le même numéro d'ID gouvernemental. Mais si nous choisissons uniquement **{ID}** comme **superclé** et essayons d'identifier de manière unique toutes les lignes de la table, selon les données des lignes, nous pourrions rencontrer une situation où deux personnes ont exactement le même nom, avec des prénoms et noms identiques. Dans ce cas, nous ne pourrions pas les identifier de manière unique par leur seul nom.

Ainsi, en incluant l'ID dans la superclé, nous pouvons différencier les deux personnes/lignes, car elles ne peuvent pas avoir le même ID gouvernemental. Nous aurions également pu choisir **{ID, SSN}** ou même **{SSN, Nom}** comme superclé, car les combinaisons de valeurs dans ces attributs sont très peu susceptibles de se répéter entre différentes personnes. Il est impossible, par exemple, que plusieurs personnes aient le même nom et le même numéro de sécurité sociale.

Voici une autre façon de voir les choses : si nous choisissons **{ID, Nom}** comme superclé, alors il ne peut pas y avoir plusieurs lignes dans la table avec les mêmes valeurs d'ID et de Nom. En d'autres termes, si nous choisissons cette superclé, c'est parce que nous sommes sûrs que cette situation ne se produira pas, garantissant que toutes les lignes ont une combinaison unique de valeurs pour les attributs ID et Nom.

Cela dépend principalement du domaine, car identifier formellement une superclé n'est pas simple. Cela implique de connaître en détail tous les domaines et les contraintes associées des attributs, ainsi que les dépendances fonctionnelles entre eux (dont nous discuterons plus tard).

En résumé, bien que vous puissiez identifier une superclé par des méthodes formelles, nous n'entrerons pas dans les détails ici. Elles ne sont généralement pas simples, car elles combinent des techniques comme la fermeture ou le backtracking, qu'il n'est pas utile d'expliquer pour bien comprendre le concept de superclé. Pour l'instant, il suffit donc de se concentrer sur la sémantique de chaque attribut et de s'en tenir aux attributs que nous savons ne pas pouvoir être répétés dans plusieurs lignes, comme les codes d'identification des entités, les noms ou les propriétés spécifiques qu'elles pourraient avoir, etc.

Enfin, concernant la table ci-dessus, nous avons vu certaines des superclés possibles qui peuvent exister. Mais si nous voulons toutes les trouver, nous supposerons d'abord que les attributs avec des valeurs répétées dans plusieurs uplets sont **Nom**, **Naissance** et **Email**, puisque plusieurs personnes peuvent avoir le même nom, le même email ou la même date de naissance. Étant donné que l'**ID** et le **SSN** ne se répètent pas car ce sont des identifiants gouvernementaux, nous aurions les ensembles suivants comme superclés, ordonnés par leur taille ou cardinalité :

* **Cardinalité 1 :** {ID}, {SSN}
    
* **Cardinalité 2 :** {ID, SSN}, {ID, Nom}, {ID, Naissance}, {ID, Email}, {SSN, Nom}, {SSN, Naissance}, {SSN, Email}
    
* **Cardinalité 3 :** {ID, SSN, Nom}, {ID, SSN, Naissance}, {ID, SSN, Email}, {ID, Nom, Naissance}, {ID, Nom, Email}, {ID, Naissance, Email}, {SSN, Nom, Naissance}, {SSN, Nom, Email}, {SSN, Naissance, Email}
    
* **Cardinalité 4 :** {ID, SSN, Nom, Naissance}, {ID, SSN, Nom, Email}, {ID, SSN, Naissance, Email}, {ID, Nom, Naissance, Email}, {SSN, Nom, Naissance, Email}
    
* **Cardinalité 5 :** {ID, SSN, Nom, Naissance, Email}
    

#### Clés candidates

Ensuite, nous avons les clés candidates. Leur objectif principal est le même que celui des superclés, à la seule différence que dans ce cas, elles utilisent le nombre minimum d'attributs possible pour l'identification.

Par exemple, auparavant, comme superclé, nous pouvions choisir **{ID, Nom}**, entre autres options. Mais cette superclé contient l'attribut ID, qui représente l'identifiant gouvernemental de chaque personne, et nous avons l'assurance légale qu'il est unique pour chaque personne.

Ainsi, puisque nous savons que l'ID de chaque personne est unique, tout comme son numéro de sécurité sociale car il s'agit également d'un numéro lié aux procédures gouvernementales, nous pouvons réduire le nombre d'attributs nécessaires pour identifier de manière unique chaque uplet et choisir une clé candidate comme **{ID}** ou **{SSN}**. Nous pourrions également considérer **{Email}** comme une clé candidate, bien que nous supposions que plusieurs personnes pourraient avoir le même email, nous ne le comptons donc pas comme une clé candidate.

Comme vous pouvez le voir, conceptuellement, les clés candidates jouent le même rôle que les superclés, mais ici l'objectif est de parvenir à l'identification avec moins d'attributs, spécifiquement avec le nombre minimum possible. Dans cet exemple, en considérant des clés candidates avec un seul attribut comme **{ID}**, nous avons réussi à identifier de manière unique les uplets avec le plus petit nombre d'attributs possible, puisqu'on ne peut former aucun type de clé avec moins d'un attribut.

De plus, pour vérifier qu'une clé est candidate et non une superclé, vous pouvez vérifier qu'il n'y a aucun sous-ensemble d'attributs de la clé qui forme à lui seul une clé.

Par exemple, si nous avons une clé comme **{ID, Nom}** et que nous voulons vérifier s'il s'agit d'une clé candidate, nous devons simplement vérifier tous les sous-ensembles d'attributs possibles qu'elle possède, qui sont {ID} et {Nom} (bien qu'il puisse y avoir des sous-ensembles avec plus d'attributs). Et rappelez-vous que plusieurs personnes peuvent avoir le même nom, mais si nous regardons le sous-ensemble {ID}, nous verrons qu'aucune personne n'a le même ID qu'une autre.

Ainsi, puisqu'il existe un sous-ensemble capable d'identifier de manière unique les uplets, il remplit la propriété fondamentale de toute clé. Cela signifie que le **{ID, Nom}** que nous vérifiions n'est pas une superclé, car il existe un sous-ensemble de ses attributs qui est une clé.

Si nous répétons ce processus de manière exhaustive, nous sommes assurés de trouver une clé candidate, c'est-à-dire un ensemble minimal d'attributs qui sert de clé pour identifier les uplets.

Fondamentalement, une clé candidate n'est qu'une superclé minimale : elle identifie de manière unique chaque uplet, et si nous en retirons une colonne, elle n'identifie plus les uplets de manière unique.

En pratique, nous énumérons rarement chaque superclé ou ne nous soucions pas des étiquettes. Nous cherchons simplement un ensemble d'attributs qui identifie de manière unique chaque uplet, de préférence avec le moins d'attributs possible. Dans la conception, au niveau logique, nous pourrions définir plusieurs clés candidates (et, implicitement, de nombreuses superclés), mais l'étape importante consiste à choisir une clé candidate comme **clé primaire** pour identifier les uplets de manière unique.

#### Clés primaires

Une fois que nous avons toutes les clés candidates qui existent (puisqu'il peut y en avoir plusieurs selon le domaine et les tables que nous traitons), nous devons en sélectionner une comme **clé primaire** à implémenter dans le SGBD. De cette façon, nous pouvons avoir une clé qui identifie de manière unique les uplets. En d'autres termes, une table peut avoir de nombreuses clés candidates, mais ces clés sont des sous-ensembles d'attributs que nous analysons théoriquement.

Pour les rendre pratiques et identifier réellement les uplets d'une table, nous devons en implémenter une dans le modèle logique. Fondamentalement, nous devons dire au SGBD laquelle de toutes les clés candidates est la clé primaire que nous avons sélectionnée pour l'identification.

Grâce à cela, nous pouvons en déduire que le nom "clé candidate" vient du fait qu'il peut y avoir de nombreux sous-ensembles minimaux d'attributs avec lesquels nous pouvons identifier les uplets. Mais en pratique, nous n'en utilisons qu'un seul, qui est celui que nous indiquons au SGBD, c'est-à-dire la clé primaire.

Dans l'exemple précédent, de toutes les superclés **{ID, Nom}**, **{SSN, Nom}**, **{ID, Email}**, etc., nous pouvons dériver les candidates **{ID}** et **{SSN}**, parmi lesquelles nous pouvons choisir **{ID}** comme primaire. Vous ne devriez pas toujours faire ce choix arbitrairement, même si vous en avez techniquement la possibilité. Vous devriez plutôt tenir compte des détails techniques de l'implémentation, ainsi que de la sémantique des attributs qui forment la clé pour qu'elle reste facile à comprendre, entre autres facteurs.

![Diagramme entité-relation avec l'entité Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751882614007/17c082cf-4d82-48ec-8595-bae0e7497236.png align="center")

Même si la clé primaire est sélectionnée pour être utilisée au niveau logique, elle peut également être représentée dans le diagramme entité-relation au niveau conceptuel. Si elle se compose d'un seul attribut, elle est marquée par **{id}** à côté de son type de données. Mais si la clé primaire est **composite** (c'est-à-dire qu'elle est composée de plusieurs attributs où chacun n'est pas suffisant pour identifier de manière unique les uplets, mais l'est avec les autres attributs marqués), alors ils sont tous marqués par **{ID}**. Quant aux clés candidates ou superclés, elles ne sont pas spécialement marquées dans le diagramme car il peut y en avoir beaucoup.

#### Clés alternatives

De toutes les clés candidates que nous avons, nous n'en choisissons qu'une comme primaire, laissant toutes les autres de côté. Ces clés qui ne sont pas sélectionnées comme primaires sont appelées clés alternatives, et leur utilité principale est la même que celle d'une clé primaire : identifier de manière unique les uplets au cas où la clé primaire ne serait pas accessible ou s'il n'était pas pratique de l'utiliser.

Vous pouvez également utiliser des clés alternatives pour améliorer l'efficacité de certaines opérations ou requêtes sur la table, car des index peuvent être définis sur celles-ci. Mais nous n'entrerons pas dans les détails de ce type de technique d'optimisation ici.

Dans notre exemple, si les clés candidates étaient **{ID}** et **{SSN}** et que nous choisissons **{ID}** comme primaire, alors **{SSN}** sera la seule clé alternative que nous aurons.

#### Clés composites

Un autre type de clé est la clé composite, qui est définie comme une clé candidate composée strictement de plus d'un attribut car chaque attribut seul ne suffit pas à identifier de manière unique les uplets de la table.

| **NomVille** | **Pays** | **Population** | **Superficie** |
| --- | --- | --- | --- |
| Madrid | Espagne | 3 223 000 | 604,3 |
| Athènes | Grèce | 664 046 | 38,96 |
| Nantes | **France** | 320 732 | 65,19 |
| Tokyo | Japon | 13 929 286 | 2 191,1 |
| Paris | **France** | 2 140 526 | 105,4 |
| **San José** | Costa Rica | 333 980 | 44,6 |
| **San José** | USA | 1 013 240 | 469,7 |

Par exemple, nous avons ici une table **City** avec des informations sur des villes du monde entier. Comme vous pouvez le voir, les attributs **NomVille** et **Pays** seuls ne peuvent pas identifier de manière unique chaque ville, car il existe des villes dans le monde qui partagent un pays, comme **Nantes** et **Paris**, et il existe également des villes portant le même nom qui sont situées dans des pays différents.

Cela signifie que nous ne pouvons utiliser aucun de ces attributs séparément dans une clé candidate, car il existe plusieurs villes ayant la même valeur dans ces attributs lorsqu'ils sont considérés individuellement.

Mais si nous les regardons ensemble et considérons la clé composite **{NomVille, Pays}**, nous voyons qu'aucune ville de notre liste située dans le même pays ne porte le même nom, elle répond donc aux exigences pour être une clé candidate. C'est aussi une superclé, puisque toutes les clés candidates sont des superclés.

De cette façon, nous nous assurons qu'il s'agit bien d'une clé composite, que nous pouvons ensuite sélectionner comme clé primaire. C'est pourquoi, parfois, dans la définition d'une clé composite, le terme clé primaire est utilisé à la place de clé candidate.

#### Clés substitutives (Surrogate Keys)

Jusqu'à présent, nous avons vu des clés formées en choisissant un ensemble d'attributs d'une table capable d'identifier de manière unique les uplets. Mais parfois, cela peut ne pas être possible.

| **Nom** | **Date de naissance** | **Email** |
| --- | --- | --- |
| Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| Bob Smith | 1990-03-05 | bob.smith@example.org |
| Carol Davis | 1978-11-23 | carol.davis@example.net |
| David Brown | 2001-01-30 | david.brown@example.com |
| Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Par exemple, dans cette table Person, nous avons les mêmes attributs qu'auparavant, à l'exception de l'**ID** et du **SSN**, qui étaient les seuls identifiants gouvernementaux que nous pouvions utiliser pour distinguer de manière unique les personnes ou les uplets de la table.

Désormais, quel que soit le sous-ensemble d'attributs que nous choisissons, il ne peut pas servir de clé, car nous supposons qu'il pourrait y avoir plusieurs personnes portant le même nom, nées à la même date exacte et utilisant la même adresse e-mail (c'est une hypothèse ici et cela peut ne pas être vrai selon le domaine modélisé).

Comme nous ne pouvons pas choisir de clé avec les attributs dont nous disposons, nous devons générer artificiellement un attribut capable de servir de clé. Cet attribut est connu sous le nom de clé substitutive (surrogate key), et il consiste en un attribut qui contient des valeurs numériques séquentielles pour tous les uplets. Cela signifie que pour garantir que chacun possède une valeur unique dans cet attribut, ils sont numérotés de 1 à l'infini avec des entiers, garantissant la propriété de clé.

| **SurrogateKey** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- |
| 1 | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 2 | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 3 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 4 | David Brown | 2001-01-30 | david.brown@example.com |
| 5 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

En plus de cette approche auto-incrémentielle, où nous pouvons voir que la clé substitutive est une valeur entière qui augmente au fur et à mesure que les uplets sont insérés dans la table, il existe également la possibilité que l'attribut attribue à chaque uplet un **UUID (Universally Unique Identifier)**, qui est un type de données binaire de **128 bits** généralement représenté sous forme de chaîne de caractères permettant d'attribuer une valeur unique à chaque uplet.

| **SurrogateKey** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- |
| e9e5a22b-d90c-4e5a-8d49-bbc24ff9335e | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 374d6cbe-fc29-4db0-91db-d21a1e2fef3c | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 57f182c5-47e2-4b71-b82c-63dc1795f9f5 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| a979dd61-daa4-4d88-a9f3-9a60c23d5b16 | David Brown | 2001-01-30 | david.brown@example.com |
| 179f4e15-0124-4a80-a25d-80e94a8e4ed9 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Enfin, il est important de noter que la clé substitutive est simplement un mécanisme pour identifier les uplets, elle n'a donc aucune sémantique dans notre domaine. En d'autres termes, les valeurs prises par l'attribut artificiel que nous avons généré ne signifient rien concernant les uplets ou le domaine dans lequel ils sont représentés.

#### Clés secondaires

Les types de clés précédents aident généralement à résoudre le problème de l'identification unique des uplets. Mais outre leur identification, il est important d'opérer sur eux et de les interroger efficacement.

Pour ce faire, des index sont généralement définis sur des attributs qui n'identifient pas nécessairement les tables, tels que le nom ou la date de naissance de la table Person précédente. En définissant un [**index**](https://www.freecodecamp.org/news/database-indexing-at-a-glance-bb50809d48bd/) sur l'un de ces attributs, nous pouvons effectuer efficacement certaines opérations sur les uplets de la table, le tout basé sur les valeurs prises par les attributs sur lesquels nous avons défini un index. Ces attributs sont appelés clés secondaires, bien que nous n'entrerons pas dans les détails de ce qu'est un index ici.

#### Clé étrangère (Foreign key)

Pour en finir avec les types de clés, celles que nous avons vues précédemment se concentrent principalement sur la résolution du problème de l'identification unique des uplets, ce qui est le but des clés, ainsi que sur la contribution à l'optimisation des opérations et des requêtes sur les tables.

Mais les clés aident également à implémenter certains éléments de la conception conceptuelle sur la conception logique du SGBD. Plus précisément, avec le type de clé qu'il nous reste à voir, la **clé étrangère**, nous pouvons implémenter des associations entre entités au niveau logique, ce qui peut se produire dans des situations comme celle-ci :

![Diagramme entité-relation où une City est associée à de nombreuses Person. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751879685769/0d55f4c4-ce27-4aaf-8fc4-59a9717cdb77.png align="center")

Ici, nous revenons à l'exemple où nous modélisons conceptuellement un domaine avec des villes et des personnes, où une personne vit dans exactement une ville, et une ville peut avoir n'importe quel nombre de personnes y vivant, de 0 à l'infini. Étant donné la multiplicité 1..1 du côté de **City**, chaque personne doit vivre dans une ville, mais la multiplicité 0..* de l'autre côté signifie que les villes peuvent n'avoir aucun habitant.

Le diagramme ci-dessous représente la conception conceptuelle de notre base de données, capturant certains détails du domaine que nous devons ensuite transférer au niveau logique. D'une part, nous transférons les entités elles-mêmes au niveau logique en créant une table pour chaque entité directement :

| **ID** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- |
| 1 | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 2 | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 3 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 4 | David Brown | 2001-01-30 | david.brown@example.com |
| 5 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

| **CityID** | **Nom** | **Pays** | **Population** | **Superficie** |
| --- | --- | --- | --- | --- |
| 1 | Madrid | Espagne | 3 223 000 | 604,3 |
| 2 | Athènes | Grèce | 664 046 | 38,96 |
| 3 | New York | USA | 8 398 748 | 783,8 |
| 4 | Tokyo | Japon | 13 929 286 | 2 191,1 |
| 5 | Paris | France | 2 140 526 | 105,4 |

Étant donné les tables pour les deux entités, nous devons maintenant implémenter au niveau logique l'association que nous avons définie au niveau conceptuel. Cela signifie utiliser un mécanisme qui nous permet de savoir dans quelle ville chaque personne vit ou les personnes qui vivent dans une certaine ville.

Si nous réfléchissons à ce problème en termes de tables, nous verrons que la seule façon de le faire est d'ajouter un attribut supplémentaire dans l'une des deux tables afin que cet attribut prenne comme valeurs la ville où une personne vit ou les personnes qui vivent dans une certaine ville.

Pour bien comprendre cela, supposons d'abord que la clé primaire de la table **Person** est **{PersonID}**, qui pourrait être son ID gouvernemental ou une clé substitutive auto-incrémentée. De plus, la clé primaire de la table **City** est l'attribut **{CityID}**. De cette façon, nous pouvons identifier de manière unique les uplets de City et Person à l'aide de leurs clés primaires, qui prennent des valeurs uniques pour chacun de leurs uplets.

| **ID** | **CityID (FK)** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- | --- |
| 1 | 5 | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 2 | 5 | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 3 | 4 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 4 | 2 | David Brown | 2001-01-30 | david.brown@example.com |
| 5 | 3 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Si nous voulons connaître la ville où vit une personne, nous pourrions ajouter un attribut à la table **Person** de sorte que les valeurs qu'il prend appartiennent à l'attribut **CityID** comme indiqué ci-dessus. C'est-à-dire que si la personne **"Alice Johnson"** vit dans la ville **"Paris"**, alors dans cette ligne, la valeur du nouvel attribut **CityID (FK)** que nous avons ajouté est 5, ce qui correspond au CityID de la ville "Paris" dans sa table respective. De même, si la personne **"Carol Davis"** vit dans la ville de **"Tokyo"**, alors le nouvel attribut prendra la valeur 4, qui correspond au CityID de cette ville dans sa table respective.

Comme vous pouvez le voir, le nouvel attribut que nous avons ajouté nous indique dans quelle ville vit la personne représentée dans chaque ligne, car il prend la clé primaire de la table City comme valeur. Ainsi, en connaissant la valeur CityID, nous pouvons identifier de quelle ville il s'agit parmi toutes celles stockées dans cette table.

Cet attribut supplémentaire que nous ajoutons pour représenter l'association est la clé étrangère. Elle sert principalement à implémenter des associations entre entités au niveau conceptuel, par le biais d'attributs qui servent de références ou de pointeurs vers d'autres tables. C'est pourquoi on l'appelle parfois un pointeur d'association.

Avant de continuer, il convient de se demander ce qui se passerait si, au lieu de placer la clé étrangère CityID **(FK)** dans la table Person, une clé étrangère **PersonID (FK)** était placée dans la table City. Si nous faisons cela dans l'intention de référencer toutes les personnes qui sont résidentes d'une certaine ville, nous rencontrerions un problème important. C'est-à-dire que si nous faisons cela, nous devons garder à l'esprit qu'une ville peut avoir un nombre arbitraire de résidents, donc dans la valeur de sa clé étrangère, nous devrions stocker tous les **PersonID** de ses résidents les uns après les autres dans la même cellule. Cela entraînerait un groupe répétitif qui est interdit dans le modèle relationnel.

Ainsi, pour éviter l'apparition de ce groupe répétitif, nous pourrions affiner ou normaliser notre diagramme, en le laissant là où nous l'avions initialement placé, c'est-à-dire l'attribut **CityID (FK)** dans la table Person. Ce serait plus compliqué que de simplement changer la table où se trouve la clé étrangère.

Maintenant que nous comprenons la base de ce qu'est une clé étrangère, il est important de noter que, pour qu'un attribut serve réellement de clé étrangère, il doit référencer un attribut dans une autre table qui est une clé primaire à lui seul.

Dans ce cas, la clé étrangère est composée d'un seul attribut, CityID (FK), qui référence CityID dans la table City. S'il référençait l'attribut Nom à la place, il pourrait y avoir plusieurs villes différentes portant le même nom. Cela signifierait que si nous disons qu'une personne vit dans une certaine ville et utilisons son nom pour l'identifier, nous ne pourrions pas savoir exactement dans quelle ville elle vit s'il existe plusieurs villes portant le même nom.

C'est pourquoi la clé étrangère référence CityID, dont nous pouvons garantir qu'il identifie de manière unique les villes à lui seul, car c'est la clé primaire de City.

#### Clé étrangère composite

Pourtant, nous n'avons pas toujours des domaines et des schémas aussi simples que ceux-ci, où les clés primaires sont un attribut unique.

Par exemple, nous pourrions avoir un diagramme comme le suivant, où il y a des personnes qui possèdent des piscines. Chaque personne doit posséder exactement une piscine, mais il est possible que plusieurs personnes s'entendent ou s'associent pour posséder ensemble une piscine. Cela signifie que chaque personne possédera un petit pourcentage de la piscine, ce qui dans ce domaine n'est pas pertinent. Ainsi, une piscine peut appartenir à un nombre arbitraire de personnes, y compris aucune, car il y aura des piscines qui n'appartiennent encore à personne.

![Diagramme entité-relation où chaque Pool appartient à une personne, et une personne peut avoir plusieurs piscines. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751883961923/4b86fca3-7a3a-43fe-9fc8-f24a98d405cf.png align="center")

Étant donné les attributs de chaque entité, nous pouvons facilement voir que la clé primaire de Person est son **{ID}**, tandis que pour identifier de manière unique une piscine, utiliser uniquement **NomPiscine** ou **NomVille** ne suffit pas, car il pourrait y avoir plusieurs piscines situées dans la même ville ou portant le même nom.

Mais si nous supposons qu'il ne peut pas y avoir plusieurs piscines portant le même nom dans la même ville, nous pouvons établir une clé primaire composite comme **{NomPiscine, NomVille}**, où ces attributs identifieront de manière unique chaque piscine. En essayant de traduire cela au niveau logique, nous créons d'abord les tables correspondant aux deux entités.

| **ID** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- |
| 1 | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 2 | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 3 | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 4 | David Brown | 2001-01-30 | david.brown@example.com |
| 5 | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

| **NomPiscine** | **NomVille** | **Longueur** | **Largeur** |
| --- | --- | --- | --- |
| Olympic Stadium Pool | Los Angeles | 50,0 | 25,0 |
| Community Center Pool | Chicago | 25,0 | 12,5 |
| Lakeside Aquatic Center | Seattle | 33,3 | 15,0 |
| Riverside Neighborhood Pool | Austin | 30,0 | 10,0 |
| Sunset Community Pool | Miami | 25,0 | 10,0 |

Plus tard, si nous voulons modéliser l'association entre les deux entités avec une clé étrangère, nous devons d'abord considérer la cardinalité de l'association. D'une part, du côté de **Person**, nous avons une cardinalité de 0..*, indiquant qu'une piscine peut appartenir à de nombreuses personnes. De l'autre côté de l'association, nous avons une multiplicité de 1..1, indiquant qu'une personne ne peut avoir qu'une seule piscine.

Grâce à cela, nous pouvons en déduire que si nous plaçons la clé étrangère dans la table **Pool**, nous devrions référencer toutes les personnes qui possèdent chaque piscine, ce qui entraînerait des groupes répétitifs dans les cas où il y a plusieurs propriétaires pour la même piscine (car nous devrions référencer chaque propriétaire à partir de la même piscine). C'est-à-dire que la piscine aurait un attribut dont la valeur serait des références à tous ses propriétaires, et comme il peut y en avoir un nombre arbitraire, un groupe répétitif se forme.

Pour éviter ce problème, chaque fois que nous avons une association avec une **cardinalité** 1 d'un côté et * de l'autre, ou équivalents, nous avons besoin d'une **clé étrangère** pour la modéliser au **niveau logique**. De plus, elle doit généralement être placée dans la table dont la cardinalité contient **\*** comme **cardinalité maximale**, indiquant une quantité arbitraire. Ici, par équivalents, nous entendons des cardinalités comme 0..1, que nous pouvons traiter de la même manière que 1..1, ou 5..*, qui est équivalent à 0..* car la cardinalité maximale est toujours une quantité arbitraire.

| **ID** | **NomPiscine (FK)** | **NomVille (FK)** | **Nom** | **Naissance** | **Email** |
| --- | --- | --- | --- | --- | --- |
| 1 | Olympic Stadium Pool | Los Angeles | Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| 2 | Riverside Neighborhood Pool | Austin | Bob Smith | 1990-03-05 | bob.smith@example.org |
| 3 | Sunset Community Pool | Miami | Carol Davis | 1978-11-23 | carol.davis@example.net |
| 4 | Sunset Community Pool | Miami | David Brown | 2001-01-30 | david.brown@example.com |
| 5 | Olympic Stadium Pool | Los Angeles | Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Comme vous pouvez le voir, dans ce cas, la clé étrangère est placée dans la table Person, qui est celle avec le * dans sa cardinalité sur le diagramme, puisque chaque personne ne peut posséder qu'une seule piscine. Cela évite que la clé étrangère n'ait à stocker un nombre arbitraire de références.

Dans ce cas spécifique, au lieu d'un seul attribut, nous devons ajouter **NomPiscine (FK)** et **NomVille (FK)** car la clé primaire de Pool n'est pas un attribut unique mais deux. La clé étrangère dans Person sera donc une **clé étrangère composite** – ce qui signifie qu'au lieu d'un attribut référençant un autre dans une table différente, il y en a deux qui référencent simultanément deux attributs dans une autre table.

Pour que cela soit valide, chaque attribut de la clé étrangère doit référencer un attribut de la clé primaire dans la table Pool, de sorte qu'ensemble NomPiscine (FK) se réfère à **NomPiscine**, et NomVille (FK) se réfère à l'attribut **NomVille** de Pool. Ainsi, ensemble, ils référencent l'intégralité de la clé primaire de Pool.

Enfin, comme nous venons de le voir, les clés étrangères sont un outil de conception logique que nous utilisons pour implémenter des associations à partir du modèle conceptuel. C'est pourquoi, dans le modèle conceptuel (dans le diagramme entité-relation), **nous n'écrivons pas les attributs qui forment les clés étrangères**. C'est parce qu'au niveau conceptuel, les associations elles-mêmes indiquent les relations entre entités. Ainsi, même si les tables ont plus d'attributs que ce que nous voyons dans le diagramme en raison des clés étrangères, **ces attributs supplémentaires ne sont jamais écrits au niveau conceptuel**.

Quant à leur dénomination, il existe de nombreux guides de style à suivre. Ici, nous avons ajouté un (FK) aux noms d'attributs pour indiquer clairement qu'il s'agit de clés étrangères ou d'une partie de l'une d'entre elles, bien qu'elles puissent être nommées de toute autre manière.

### Entités faibles

Maintenant que nous avons défini comment les clés étrangères nous permettent d'implémenter des associations entre entités, nous allons poursuivre en analysant un cas où l'une des entités associées ne peut pas être identifiée seule avec ses attributs. Au lieu de cela, elle a besoin d'une clé étrangère qui référence une autre entité pour être correctement identifiée – cela signifie que l'entité est considérée comme faible en identification.

#### Faiblesse d'existence

Avant de continuer, sachez qu'il existe plusieurs types de faiblesses dans ce contexte. L'une est la **faiblesse d'existence**, ce qui signifie qu'une entité appelée **faible** ne peut pas exister s'il n'y a pas une autre entité appelée **propriétaire** avec laquelle elle est associée.

![Diagramme entité-relation où chaque personne est composée d'un cerveau. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751893494662/a3f06614-4314-48f5-8a0d-091515af9e1d.png align="center")

Nous pouvons comprendre cela avec l'exemple précédent, où une personne est composée d'un cerveau, et un cerveau doit toujours faire partie d'une personne. Ainsi, lorsqu'une instance de l'entité **Brain** est créée, c'est-à-dire qu'un uplet représentant un cerveau est créé, une personne doit également être créée pour être associée à cette personne.

En résumé, un cerveau ne peut pas exister sans l'entité **Person** à laquelle il est lié. Cela conduit à une faiblesse d'existence où nous disons que l'entité Brain est faible et que l'entité Person est le propriétaire ou forte. La composition permet à Person d'exister sans Brain, même si nous l'empêchons ici avec la cardinalité.

En dehors de cela, lorsque nous avons une association où toutes ses cardinalités sont 1..1, il est très probable que nous puissions combiner ces deux entités en une seule, comme Person, en ajoutant des attributs comme **Neurones**, au lieu d'avoir deux entités. Mais cela ne doit pas toujours être fait de cette façon, car cela dépend de la façon dont nous voulons modéliser le domaine et les exigences.

#### Faiblesse d'identification

En plus de la faiblesse d'existence, nous pouvons avoir une **faiblesse d'identification**. Ici, par identification, nous entendons le mécanisme par lequel chaque uplet d'une table est distingué de manière unique de tous les autres, comme nous l'avons vu précédemment avec les clés.

Pour comprendre ce type de faiblesse, quand elle se produit et comment elle est gérée, nous pouvons examiner le cas suivant :

![Diagramme entité-relation où Residence est une entité faible qui relie City et Person avec des dates de début et de fin. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751898026686/2cdc320d-f665-4977-95de-d606a86a9ab2.png align="center")

Ici, nous avons quelques entités :

* **City**, qui modélise les villes du domaine
    
* **Person**, qui fait de même pour les personnes, et
    
* **Residence**, qui modélise le séjour d'une personne dans une ville spécifique.
    

Cela signifie que les gens peuvent vivre dans une ville pendant un certain temps puis déménager dans une autre. Ainsi, selon ce diagramme, ils laisseraient derrière eux une occurrence ou un uplet de **Residence** avec la date à laquelle ils ont commencé à vivre dans la ville et la date à laquelle ils ont déménagé dans une autre.

En ce qui concerne les cardinalités, nous pouvons voir qu'une ville peut être liée à de nombreuses résidences, car elle peut avoir ou avoir eu de nombreux habitants, tandis qu'une résidence n'est liée qu'à une seule personne car la résidence se concentre sur l'enregistrement du fait qu'une certaine personne a vécu dans une certaine ville. Ainsi, les multiplicités 1..1 obligent une résidence à lier une personne à une ville, car introduire l'optionnalité ici impliquerait qu'une résidence puisse lier une ville ou une personne à "rien", ce qui n'a pas de sens.

Pendant ce temps, du côté de Residence, nous avons des multiplicités 0..* avec optionnalité car une personne peut ne vivre dans aucune ville, ou inversement, une ville peut n'avoir ou n'avoir jamais eu d'habitants, elle peut donc ne pas être liée à une occurrence de Residence.

Ensuite, lorsque nous traduisons ce diagramme au niveau logique, nous essayons d'abord de définir les clés primaires pour toutes les entités ou tables. Dans ce cas, pour City et Person, c'est simple, car nous supposons que CityID est un identifiant unique pour chaque ville, et ID est un identifiant gouvernemental unique pour chaque personne (uplet).

Mais lorsque nous définissons la clé primaire pour Residence, nous avons plusieurs options. D'une part, nous pourrions choisir **{DateDébut}** ou **{DateFin}** comme clé primaire, mais ce n'est pas faisable car plusieurs personnes pourraient commencer à vivre dans la même ville ou dans des villes différentes à la même date de début, date de fin, ou les deux. Nous ne pouvons donc même pas choisir **{DateDébut, DateFin}** comme clé primaire, car, dans le pire des cas, plusieurs personnes pourraient commencer et cesser de vivre dans une ville en même temps.

Cela signifie que l'entité Residence a besoin des autres entités auxquelles elle est associée pour avoir une clé primaire et être identifiable. Il est important de noter qu'au niveau logique, nous aurions deux clés étrangères dans Residence en raison de ses deux associations avec City et Person. Plus précisément, elle possède une clé étrangère **CityID (FK)** et une autre **ID (FK)** qui modélisent respectivement ces associations.

Nous pouvons le déduire d'un coup d'œil sans "voir" le modèle logique car nous avons des associations avec des cardinalités 1..1 et 0..*. Donc du côté 0..*, il doit y avoir une clé étrangère pour implémenter cette association comme nous l'avons vu précédemment.

Étant donné ces clés étrangères, nous pourrions envisager de choisir **{CityID (FK)}** ou **{ID (FK)}** comme clés primaires, mais cela ne garantirait pas l'identification de tous les uplets car plusieurs personnes peuvent vivre dans une ou plusieurs villes en même temps. De plus, une ville peut avoir plusieurs résidents simultanément, ce qui entraîne des valeurs répétées dans les attributs de clé étrangère pour des uplets qui devraient être considérés comme distincts.

Nous ne pouvons pas non plus choisir **{CityID (FK), ID (FK)}** comme clé car une personne peut avoir déménagé dans une ville plusieurs fois au cours de différentes périodes, même si elle a vécu dans d'autres villes entre-temps. Cela donnerait plusieurs uplets avec les mêmes valeurs dans les deux clés étrangères mais des valeurs différentes dans les dates.

Compte tenu de cette situation, la seule option restante est d'envisager une clé qui inclut l'un des attributs de date de Residence et les clés étrangères **{CityID (FK)}** ou **{ID (FK)}**, puisque rien n'empêche une personne d'avoir plusieurs résidences en même temps (où chaque résidence indique qu'elle vit dans une ville). C'est normal car nous n'avons restreint cette situation d'aucune manière dans le diagramme conceptuel.

Ainsi, puisqu'une personne peut vivre dans plusieurs villes à la fois, pour identifier un uplet Residence, nous devons savoir quelle personne vit dans quelle ville, plus à quel moment elle le fait. Cela, nous pouvons le déterminer avec **DateDébut** ou **DateFin**. L'une des dates suffit ici, car une personne ne peut vivre dans une ville qu'une seule fois au même moment, ce qui signifie qu'une personne ne peut pas commencer ou cesser de vivre dans la même ville plusieurs fois au même moment.

En résumé, si nous voulons identifier de manière unique l'entité Residence, nous devons sélectionner **{DateDébut, CityID (FK), ID (FK)}** comme clé primaire, bien que nous puissions également sélectionner **{DateFin, CityID (FK), ID (FK)}** tant que nous sommes sûrs que DateFin existe toujours. Si la date de fin n'est pas définie tant que la personne n'a pas quitté la ville, nous ne pourrions pas considérer DateFin pour identifier Residence.

Nous voyons donc ici que nous ne pouvons pas identifier l'entité sans utiliser les clés étrangères respectives. Cela signifie que l'entité est considérée comme faible en identification, car elle dépend des deux entités City et Person, qui dans ce contexte sont considérées comme les propriétaires de l'entité faible. En d'autres termes, les entités propriétaires peuvent être identifiées par elles-mêmes, tandis que l'entité faible dépend d'autres entités pour son identification.

Pour noter cela dans le diagramme entité-relation, nous pouvons utiliser un rôle **«weak»** (faible) sur les côtés de l'entité faible pour indiquer que les clés étrangères de ces associations sont nécessaires pour identifier l'**entité faible**.

Pour bien comprendre ce que signifie la faiblesse d'identification, nous pouvons maintenant considérer le même diagramme qu'auparavant. Mais maintenant, supposons qu'une personne ne puisse vivre que dans une seule ville à un moment donné, contrairement à avant où elle pouvait vivre dans plusieurs villes à la fois. Cette restriction ne peut pas être modélisée avec des éléments UML, il suffit donc d'ajouter une note textuelle dans le diagramme pour refléter la restriction.

![Diagramme entité-relation où Residence est une entité faible qui relie City et Person avec des dates de début et de fin. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751895973100/a7783ee8-ac34-4b92-9bb3-3bb1b425fa7a.png align="center")

Dans ce cas, puisqu'une personne ne peut vivre que dans une seule ville à la fois, nous n'avons pas besoin d'inclure la clé étrangère **CityID (FK)** dans la clé primaire de Residence. Si une personne vit dans une ville à un moment donné, elle ne peut pas vivre dans une autre, il n'y aura donc pas d'autres uplets dans la table avec cette personne et cette date de début et de fin de résidence.

Par conséquent, la clé primaire de Residence devient **{DateDébut, ID (FK)}**, par exemple. La seule chose qui change en dehors de cette clé primaire est le diagramme conceptuel lui-même, où désormais la seule entité propriétaire de Residence est Person car la clé étrangère vers City n'est plus strictement nécessaire pour son identification. Ainsi, même si Residence reste faible, sa seule entité propriétaire est Person. C'est pourquoi le rôle "weak" n'est écrit que dans l'association qui donne naissance à la clé étrangère **ID (FK)**, laquelle se trouve effectivement dans la clé primaire de Residence (contrairement au scénario précédent où nous avions placé le rôle dans les deux associations).

Comme vous pouvez l'imaginer, avec les rôles "weak", nous pouvons non seulement savoir quelles entités sont faibles mais aussi quelles entités les possèdent. Le rôle est toujours du côté de l'association où se trouve l'entité faible – c'est-à-dire là où se trouve la clé étrangère référençant l'entité propriétaire, ce qui correspond à la cardinalité * vue précédemment. Ensuite, de l'autre côté de l'association avec le rôle "weak", nous trouvons l'entité propriétaire.

![Diagramme entité-relation où Residence relie City et Person avec des dates de résidence. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751895191612/68997989-56ee-4a31-bd47-18bb12d9cb60.png align="center")

Si nous voulons convertir Residence en une entité qui n'est pas faible, nous devons ajouter suffisamment d'attributs pour l'identifier sans dépendre d'autres entités. Par exemple, si nous ajoutons une clé substitutive **ResidenceID** qui fonctionne par **auto-incrément** ou **UUID**, alors nous pouvons identifier automatiquement chaque uplet de Residence de manière unique, la clé primaire de **Residence** deviendrait donc **{ResidenceID}**, et l'entité ne serait plus faible.

Enfin, si nous considérons le domaine que nous avons initialement proposé et ses exigences, nous voyons que Residence est faible en identification, ayant besoin des deux clés étrangères pour être identifiée. Ainsi, en plus d'être représentée avec les rôles "weak" dans les deux associations, il convient de noter la possibilité de la représenter à l'aide d'une entité associative comme celle-ci :

![Diagramme entité-relation où Residence relie les villes et les personnes, permettant des relations multiples des deux côtés. Image de l'auteur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1751911354847/f2fb30d9-dcd6-4c0e-8931-40d8ae2f8a76.png align="center")

Nous pouvons faire le diagramme de cette façon dans cette situation car Residence a Person et City comme entités propriétaires. Puisqu'elle est liée à l'association entre les deux entités et qu'elle a besoin des deux pour être identifiée, elle peut être désignée comme une entité associative.

Mais une entité associative et une entité faible sont des concepts complètement différents, car la faiblesse d'identification est une propriété des entités, tandis qu'une entité associative est une façon de représenter les entités en UML au niveau conceptuel.

Par exemple, si Residence n'avait que Person comme entité propriétaire, alors il ne serait plus logique de la représenter comme une entité associative au niveau conceptuel. C'est parce qu'elle n'est une entité faible en identification que par rapport à une seule entité propriétaire, Person, et non deux entités propriétaires pouvant avoir une association N:M entre elles.

En plus de la représentation en tant qu'entité associative, les cardinalités des deux côtés de l'association doivent être 0..*, puisqu'il a été précédemment déclaré qu'une ville pouvait avoir un nombre arbitraire de résidences, où chacune n'avait qu'une seule personne, nécessairement. Ainsi, si nous représentons Residence comme une entité associative, l'association entre City et Person doit avoir un 0..* sur Person. Cela indique qu'une ville peut être liée à un nombre arbitraire de personnes via l'entité Residence, la même chose se produisant dans le sens inverse.

### Navigabilité

En relation avec l'exemple précédent et le concept d'association ou de clé étrangère, il est parfois important d'analyser la **navigabilité** de notre diagramme entité-relation avant d'implémenter la conception logique de la base de données. En effet, des problèmes d'efficacité, des ambiguïtés, voire l'impossibilité d'effectuer certaines opérations ou requêtes peuvent survenir.

Pour commencer, la navigabilité se réfère à la capacité que nous avons de **"naviguer"** sur le **diagramme entité-relation** à travers les associations entre entités, ou en d'autres termes, si nous sommes situés sur une certaine entité, elle se réfère à la capacité offerte par les associations qui affectent cette entité de parcourir ces associations et de récupérer des informations d'autres entités.

![Diagramme entité-relation où Residence relie City et Person avec des dates de résidence. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751895191612/68997989-56ee-4a31-bd47-18bb12d9cb60.png align="center")

Pour comprendre cela avec un exemple, nous pouvons nous référer au dernier diagramme de la section précédente où nous introduisons une clé substitutive à Residence. Dans ce diagramme, nous avons une entité Residence avec deux clés étrangères pointant vers City et Person. Ainsi, si on nous donne un uplet de Residence, nous pouvons utiliser ses clés étrangères pour déterminer quel uplet de City ou de Person est associé à l'occurrence de l'entité Residence. Cela nous permet de naviguer dans ces associations vers les classes correspondantes.

C'est utile, par exemple, lorsque nous interrogeons la base de données pour trouver la personne qui a vécu dans la ville correspondant à cette Residence. Pour cela, nous pouvons regarder la valeur de la clé étrangère **ID (FK)**, qui correspond à un identifiant d'une personne enregistrée dans la table Person. Cela nous permet de naviguer de l'entité Residence vers l'entité Person, ce qui signifie que nous avons obtenu des informations de l'entité Person en partant de Residence.

Nous pouvons répéter cette étape plusieurs fois, en naviguant d'entité en entité à travers le diagramme. Mais l'important est de savoir quelles associations sont navigables dans une certaine direction.

Par exemple, si on nous donne une personne, cet uplet n'a pas de clés étrangères, donc avec un uplet représentant une personne, nous ne pouvons obtenir d'informations sur aucune autre entité de notre diagramme – pas même Residence. Si nous ne regardons que les valeurs de l'uplet Person, nous ne saurons pas quels uplets Residence sont associés, car nous devrions interroger et parcourir toute la table Residence pour le savoir.

En résumé, l'association Residence-Person n'est pas navigable dans les deux sens – nous ne pouvons aller que de Residence vers Person, mais pas l'inverse. Il en va de même pour City.

La navigabilité est importante, car il est utile de connaître la direction dans laquelle les associations du diagramme peuvent être parcourues avant d'implémenter quoi que ce soit. Si notre système doit supporter une requête telle que l'obtention de la ville où une personne vit actuellement, il pourrait être plus efficace d'ajouter une association directement de Person vers City au lieu de devoir passer par tous les uplets Residence pour résoudre la requête, ce qui serait plus efficace.

![Diagramme entité-relation où Residence relie City et Person, avec une relation directe supplémentaire entre elles. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751904973527/7d253452-3cdd-4d17-bbfe-cdce7e064f89.png align="center")

Bien que cette association puisse sembler redondante, si nous devons nous concentrer fortement sur l'optimisation de la requête que nous avons mentionnée plus tôt, il peut être utile de "compliquer" le diagramme de cette manière afin que certaines requêtes critiques de notre système s'exécutent plus rapidement.

Il est également important de noter qu'une personne peut ne vivre dans aucune ville, c'est pourquoi la cardinalité minimale de la nouvelle association du côté de City est 0..1. C'est parce que la clé étrangère résultant de cette association peut "ne pas exister", comme nous le verrons plus tard, représentant le fait qu'une certaine personne ne vit dans aucune ville.

Enfin, tout ce qui concerne la navigabilité n'est pas lié à l'efficacité, comme lors de la détection de cycles de navigation. Si plusieurs existent, nous devrons nous assurer dans l'implémentation que l'optimiseur du SGBD choisit le plus court dans les requêtes correspondantes.

La navigabilité nous aide également à voir si certaines requêtes peuvent être résolues, c'est-à-dire si certaines données peuvent être obtenues du système à partir d'une certaine entrée. Et gardez à l'esprit que ce concept de navigabilité que nous avons introduit se réfère à la navigabilité sur le **diagramme conceptuel** lui-même, et non à la possibilité d'obtenir des informations sur d'autres entités au niveau logique, comme nous le verrons plus tard.

### Contraintes

En continuant avec les éléments du modèle relationnel, la seule chose qu'il nous reste à discuter sont les contraintes. Ce sont des conditions imposées aux données pour modéliser correctement le domaine et répondre à ses exigences. Il s'agit d'un ensemble de règles qui doivent toujours être suivies afin que les données stockées soient correctes, cohérentes, intègres et s'alignent sur la sémantique donnée par le domaine.

Nous pouvons définir des contraintes tant au niveau conceptuel qu'au niveau logique. D'une part, dans le modèle conceptuel, les contraintes sont principalement modélisées à l'aide des outils fournis par UML lors de la création du diagramme entité-relation.

Par exemple, disons que dans notre domaine, nous avons une règle métier ou une condition stipulant qu'une ville peut avoir un maximum de 500 habitants. Alors, si nous modélisons le domaine avec un diagramme similaire à ceux créés précédemment, nous aurons une association entre personne, habitant et ville, où nous utilisons la cardinalité de cette association (spécifiquement la cardinalité maximale) pour représenter la contrainte du nombre maximum d'habitants.

Mais toutes les contraintes ne peuvent pas être modélisées au niveau conceptuel avec les outils UML. Par exemple, considérons le cas où nous avons un réseau social avec des personnes qui peuvent en suivre d'autres. Nous pouvons modéliser cela avec une entité Person et une relation récursive où une personne peut suivre un nombre illimité de personnes, y compris le cas où elle ne suit personne.

![Diagramme entité-relation où Person a une relation de suivi avec elle-même. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1751796543335/1224219f-98b8-459b-ae74-e704d06e797a.png align="center")

Mais rien n'empêche une personne de se suivre elle-même, ce qui n'a pas beaucoup de sens dans un réseau social. Nous pourrions donc le laisser tel quel si le client ne spécifie pas le contraire. Mais si le domaine lui-même ou une exigence indique qu'une personne ne peut pas se suivre elle-même, nous devrons ajouter cette restriction au diagramme.

Malheureusement, nous ne pouvons pas le faire avec les outils fournis par UML, car il n'existe aucun mécanisme pour indiquer que cette association ne peut pas se produire entre la même occurrence (uplet) de l'entité **Person**.

Dans ce cas, nous avons plusieurs options pour refléter la restriction dans la conception conceptuelle. La première et la plus simple consiste à ajouter une note textuelle dans la marge du diagramme où nous expliquons brièvement la situation et indiquons la règle qui constitue la restriction. Les notes en UML sont des éléments standards consistant en une boîte avec du texte où sont spécifiées des choses qui ne peuvent pas être correctement modélisées avec les propres éléments du diagramme.

D'un autre côté, au lieu d'utiliser une note textuelle, qui est moins formelle et plus sujette à des interprétations erronées ou à la confusion, nous pouvons utiliser un langage spécifique pour représenter les contraintes comme **OCL (Object Constraint Language)**, où nous définissons la restriction en utilisant le propre code du langage.

```markdown
context Person
inv noSelfFollow:
    self.follows->forAll( p | p <> self )
```

Ici, nous n'entrerons pas dans les détails de la modélisation des contraintes en OCL. L'important est de savoir qu'il existe des contraintes que nous ne pouvons pas représenter directement avec les éléments du diagramme, elles doivent donc être reflétées dans la conception conceptuelle à l'aide de notes ou de code de langage spécialisé.

### Intégrité des données

Comme nous l'avons mentionné, les contraintes sont des **conditions de validité** imposées aux données. Elles permettent de s'assurer que, lorsqu'elles sont stockées dans notre base de données, leur exactitude, leur cohérence et leur intégrité peuvent être vérifiées, le tout vérifié automatiquement par le SGBD. En effet, les contraintes elles-mêmes sont généralement implémentées au niveau logique dans le SGBD, qui possède des fonctionnalités spécifiques pour vérifier les contraintes et assurer l'exactitude et l'intégrité des données.

Jusqu'à présent, nous avons supposé que les données sont stockées correctement dans leurs tables respectives. Nous avons également supposé qu'elles respectent les domaines d'attributs, ainsi que de nombreux autres détails pouvant affecter la validité de ce qui est stocké.

Ainsi, pour éviter les problèmes, la base de données vérifie automatiquement la **validité** des données, ce qui diffère de l'**exactitude** des données. Pour comprendre la différence entre ces concepts, considérez l'exemple suivant :

| **CityID** | **Nom** | **Pays** | **Température *(Kelvin)*** |
| --- | --- | --- | --- |
| 5 | Paris | France | 280 |
| 1 | Madrid | Espagne | \-3 |

Nous avons ici une table Temperature qui stocke des uplets avec les températures d'une ville à différents moments. Comme vous pouvez le deviner, l'attribut température est de type entier, ce qui signifie qu'il peut contenir n'importe quel entier, y compris des négatifs. Mais les températures ne peuvent pas être négatives si elles sont mesurées en Kelvin, donc si nous mesurons les températures en Kelvin ici, nous devons ajouter une contrainte de domaine comme **Température >= 0** pour empêcher l'attribut Température de prendre des valeurs négatives. C'est ce qu'on appelle une contrainte de domaine.

Les **contraintes de domaine**, comme vous venez de le voir, servent à définir les domaines des attributs de table, en restreignant les valeurs possibles qu'ils peuvent prendre et en garantissant que les données stockées sont du type approprié.

Compte tenu de cette restriction, nous pouvons voir que le premier uplet respecte toutes les contraintes, il pourrait donc être considéré comme une donnée valide. Mais avec les informations dont nous disposons, nous ne pouvons pas garantir que cette donnée est exacte. C'est-à-dire que nous n'avons pas pris de thermomètre pour mesurer la température à Paris, nous ne savons donc pas si ce 280 est la température réelle à Paris ou s'il s'agit d'une donnée inexacte. Ainsi, même si les données respectent les contraintes, nous devons nous assurer qu'elles sont exactes.

C'est une tâche très compliquée sur laquelle nous n'entrerons pas dans les détails ici. Nous pouvons implémenter des mécanismes de détection et de correction d'erreurs dans les données, ou nous pouvons mener des audits pour vérifier que les données correspondent à la réalité – c'est-à-dire au domaine. Ou des tiers peuvent superviser les données, car si la personne qui a pris cette mesure nous dit que le 280 n'est pas ce qu'elle a enregistré avec le thermomètre, alors nous savons que cette donnée est inexacte. Sinon, nous n'aurions aucun moyen de garantir son exactitude.

D'un autre côté, dans le deuxième uplet, la température prend une valeur négative, nous pouvons donc conclure que cette donnée est non seulement inexacte mais aussi invalide. Elle est invalide car aucune température Kelvin ne peut être négative, violant la contrainte de domaine imposée précédemment. Elle est inexacte car si elle est invalide, alors cette valeur doit nécessairement être différente de la température réelle de la ville.

Vous savez donc maintenant ce que signifie une donnée erronée ou inexacte. Vous comprenez également les contraintes de domaine qui peuvent assurer l'intégrité des données en termes de type de données et de valeurs possibles que l'attribut peut prendre.

Mais l'intégrité des données va au-delà de la simple vérification que les données sont au bon format et dans le domaine d'un attribut. Par exemple, les données doivent être **fiables et précises**, ce que nous vérifions par leur exactitude. Elles doivent également être **cohérentes**, ce qui signifie qu'il ne peut pas y avoir d'uplets en double avec des informations menant à des contradictions comme vu précédemment. Elles doivent également posséder d'autres caractéristiques de haut niveau telles que la disponibilité, la durabilité, l'actualité des données, la sécurité, etc., que nous n'approfondirons pas car elles ne sont pas essentielles ici.

### Contraintes d'intégrité

En plus des caractéristiques précédentes, il en existe une autre qui est essentielle pour maintenir l'intégrité des données : la complétude (completeness). Dans ce contexte, la complétude peut avoir plusieurs significations, la plus simple étant que tous les points de données sont présents dans la base de données sous forme d'uplets. Cela signifie que tous les "individus" du domaine sont représentés dans la base de données.

Par exemple, si nous stockons un domaine avec 10 personnes et que nous ne voyons que 9 uplets dans une table comme Person, nous savons que les données ne sont pas complètes car l'ensemble du domaine n'est pas représenté par les 9 uplets. D'un autre côté, la complétude signifie également que chaque point de données doit nécessairement avoir une valeur pour chaque attribut de la table qui le définit.

| **CityID** | **Nom** | **Pays** | **Population** |
| --- | --- | --- | --- |
| 1 | Madrid | Espagne | 3 223 000 |
| 2 | Athènes | **NULL** | 664 046 |
| 3 | New York | USA | 8 398 748 |
| 4 | Tokyo | Japon | 13 929 286 |
| 5 | Paris | France | **NULL** |

Par exemple, si nous avons un domaine avec des villes, et que dans notre base de données nous incluons une table **City** avec ces attributs, alors chaque ville (point de données) que nous représentons avec un uplet doit avoir une valeur pour chacun de ces attributs. Cela signifie que pour que les données soient complètes, aucune cellule de la table ne peut être vide.

Dans la table ci-dessus, vous pouvez voir que les villes nommées **"Athènes"** et **"Paris"** empêchent les données d'être complètes, car l'une n'a pas de valeur dans l'attribut **Pays** et l'autre dans Population, respectivement. Au lieu de laisser les cellules correspondantes vides, la valeur spéciale **NULL** y est stockée pour représenter qu'elles ne contiennent rien.

Pour garantir la propriété de complétude des données stockées, les valeurs NULL devraient être évitées dans les tables. Mais nous verrons plus tard que par défaut, les SGBD n'imposent généralement pas la restriction selon laquelle les valeurs de table ne peuvent pas être NULL. En d'autres termes, lorsque nous créons une table par défaut, les valeurs des uplets peuvent être NULL à moins que nous n'en définissions autrement par une restriction.

Nous définissons généralement cette restriction au niveau de l'attribut, où nous spécifions que les valeurs de la colonne correspondant à cet attribut ne peuvent pas être NULL. Ainsi, tous les uplets que nous enregistrons dans la table doivent avoir une valeur autre que NULL pour cet attribut.

Cela affecte le domaine de l'attribut, car par défaut, la valeur spéciale NULL est incluse dans l'ensemble de toutes les valeurs qu'un attribut peut prendre. Mais nous pouvons exclure cette valeur de l'ensemble à l'aide d'une restriction.

À la lumière de tout cela, et après avoir introduit le concept de NULL, nous pouvons définir l'intégrité comme une propriété qui garantit que tout au long de son cycle de vie, la donnée stockée est valide, exacte, cohérente, complète et fiable.

Pour s'assurer que toutes ces caractéristiques sont respectées (à l'exception de la dernière, qui est d'un niveau supérieur), nous utilisons des types spéciaux de contraintes dans la base de données, appelées contraintes d'intégrité. En d'autres termes, nous pouvons catégoriser les contraintes de base de données en fonction de leur objectif.

Certaines contraintes sont dédiées à la modélisation des exigences et des règles du domaine métier, tandis que d'autres sont des contraintes d'intégrité spécifiquement visant à appliquer les caractéristiques d'intégrité susmentionnées (mais certaines d'entre elles peuvent également modéliser indirectement une partie des règles métier).

Ces dernières contraintes sont des conditions de validité vérifiées automatiquement par le SGBD chaque fois qu'une opération est effectuée sur l'entité (table) ou les entités affectées par ces contraintes, le tout dans le but d'assurer l'intégrité des données à tout moment.

Ces conditions de validité, comme nous l'avons vu, doivent être respectées pour tous les uplets stockés, garantissant qu'aucun d'entre eux ne peut avoir une cellule vide ou une valeur interdite. En d'autres termes, des conditions peuvent être définies au niveau de l'attribut (colonne), bien que les uplets stockés doivent adhérer à ces contraintes. C'est pourquoi elles sont vérifiées pour chacun d'eux. Ainsi, lorsque tous les uplets stockés dans une table respectent toutes les contraintes d'intégrité définies, l'instance de cette table est dite **légale**.

Les contraintes d'intégrité, selon leur objectif logique, peuvent être classées en plusieurs types :

**Premièrement, nous avons les contraintes de domaine.** Ce sont celles dont nous venons de discuter, et elles servent principalement à définir le type de données des attributs et leur domaine.

D'une part, les contraintes de domaine implicites incluent celles qui définissent le type de données des attributs, car c'est quelque chose que nous devons faire lors de la création d'une table, et non quelque chose que nous ajoutons plus tard pour limiter le domaine de l'attribut.

D'autre part, il existe des contraintes de domaine explicites, que nous ajoutons en plus de la définition du type de données pour limiter les valeurs que les attributs peuvent prendre, comme les empêcher de contenir la valeur spéciale NULL, ou empêcher un attribut qui stocke des températures en Kelvin de prendre des valeurs négatives, comme nous l'avons vu. Nous pouvons également considérer comme implicite le fait que le SGBD autorise les cellules à prendre des valeurs NULL, ce que nous pouvons empêcher en fixant une contrainte explicite.

**Ensuite, nous avons les contraintes d'identification.** Concernant l'identification des uplets, nous avons vu précédemment qu'une clé primaire est choisie pour chaque table afin que ses attributs puissent identifier de manière unique tous les uplets qui y sont stockés. La définition explicite d'une clé primaire est une contrainte d'intégrité que nous définissons sur la table.

Mais en faisant cela, le SGBD applique en interne plusieurs sous-contraintes d'intégrité, dont l'une garantit que les combinaisons de valeurs prises par les attributs de la clé primaire sont toutes différentes (c'est-à-dire uniques). C'est ce qui caractérise une clé. De plus, aucun des attributs ne peut prendre NULL comme valeur, car s'ils le pouvaient, il y aurait plusieurs uplets avec la même valeur pour la clé primaire.

| **ID** | **Nom** | **Naissance** |
| --- | --- | --- |
| 1 | Alice Johnson | 1985-07-12 |
| **NULL** | Bob Smith | 1990-03-05 |
| 3 | Carol Davis | 1978-11-23 |
| 4 | David Brown | 2001-01-30 |
| **NULL** | Emily Wilson | 1995-09-14 |

Par exemple, si notre clé primaire est un attribut unique **{ID}**, alors il ne peut pas prendre NULL comme valeur, car dans ce cas, nous pourrions avoir plusieurs uplets avec NULL dans cet attribut comme vu ci-dessus, empêchant leur identification unique.

**Enfin, nous avons les contraintes référentielles.** Liées aux contraintes précédentes, les contraintes d'intégrité référentielle garantissent que les relations entre les tables sont cohérentes à tout moment. Ces contraintes sont implicites, ce qui signifie que le SGBD s'assure automatiquement qu'elles sont remplies. Néanmoins, nous devons définir explicitement quels attributs sont des clés étrangères pour qu'il le fasse.

![Diagramme entité-relation où Pool est une entité faible dépendant de City. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752060524956/e7efb90c-04f2-4581-b12d-cb443a028f25.png align="center")

Ici, par cohérent, nous ne nous référons pas au même concept que la cohérence des données. Nous voulons plutôt dire qu'une clé étrangère doit référencer un uplet valide dans la table vers laquelle elle pointe.

Par exemple, si nous avons une entité faible Pool dont la table logique possède un attribut de clé étrangère comme **CityID (FK)**, alors chaque fois que cet attribut référence une ville, il doit contenir une valeur CityID valide. Cela signifie qu'elle doit exister dans la table City. Si la valeur n'existe pas, alors elle ne référencerait aucune ville.

Notez également que l'attribut de clé étrangère lui-même peut être NULL par défaut, à moins que nous n'en spécifiions autrement, car la contrainte de clé étrangère ne se comporte pas comme la contrainte de clé primaire, qui empêche implicitement les valeurs NULL. Au lieu de cela, la contrainte de clé étrangère se concentre uniquement sur la garantie de la cohérence des références, et non sur la prévention des valeurs NULL.

Pour comprendre cela, nous devons regarder la multiplicité 1..1 du côté de City, qui exige que toutes les piscines appartiennent à exactement une ville, garantissant qu'aucune piscine n'est "volante" ou en dehors d'une ville. Cela signifie que toutes les piscines doivent avoir une valeur dans leur clé étrangère **CityID (FK)**, car elles doivent appartenir à une seule et unique ville.

Pour que cette restriction (que nous avons modélisée conceptuellement avec une cardinalité minimale) soit traduite au niveau logique, nous devons indiquer explicitement une **contrainte d'intégrité de domaine** sur l'attribut **CityID (FK)** afin qu'il ne puisse pas contenir de valeurs NULL. Cela signifie qu'il doit toujours se référer à une ville. Ceci, à son tour, permet à l'entité Pool d'être identifiée par le nom de la piscine et la ville où elle se trouve, car le nom peut être répété dans plusieurs uplets/piscines. Mais on suppose que la combinaison du nom et de la ville où elles se trouvent ne se répète jamais dans notre domaine. En d'autres termes, dans une même ville, il n'y a pas plusieurs piscines portant le même nom.

En supposant cela, si dans notre base de données nous avons une série d'uplets dans les deux tables et que nous voulons supprimer une ville de l'enregistrement, nous devons alors vérifier s'il existe une piscine référençant cette ville. Cela empêcherait la suppression de l'enregistrement de la ville pour maintenir l'intégrité et garantir que la clé étrangère respective de la piscine continue de référencer une ville existante.

Pour résoudre cette situation, il existe de nombreuses politiques que nous verrons plus tard, bien que la plus courante consiste à empêcher l'exécution de l'opération de suppression ou à supprimer également l'enregistrement de la piscine qui référence la ville que nous voulons supprimer. Cela pourrait entraîner d'autres suppressions récursives s'il existe des clés étrangères pointant vers Pool.

![Diagramme entité-relation où une City peut avoir zéro ou une Pool, et une piscine peut appartenir à zéro ou une ville. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752061005445/a3dab918-7ccc-42b8-b0da-2956bebe1e79.png align="center")

D'un autre côté, si la cardinalité minimale du côté de **City** est 0, cela signifie qu'au niveau logique, la clé étrangère de Pool peut ne pas exister – ce qui signifie que la piscine pourrait ne se trouver dans aucune ville. Ainsi, sa clé étrangère peut prendre la valeur NULL car c'est le seul moyen simple d'implémenter le fait que la clé étrangère elle-même "n'existe pas".

Si nous faisons cela, nous n'aurons pas à définir la contrainte explicite selon laquelle l'attribut de clé étrangère est non nul, et lors de la suppression d'un enregistrement de ville, nous pouvons définir la politique de suppression de sorte que la clé étrangère dans Pool soit mise à NULL.

Quant à la faiblesse d'identification de **Pool**, elle disparaît ici car elle ne peut pas utiliser sa clé étrangère pour l'identification puisqu'elle peut prendre la valeur NULL et que le nom de la piscine peut être répété. Pour cette raison, nous décidons d'ajouter une clé substitutive **PoolID** pour identifier l'entité Pool.

Enfin, rien n'empêche une clé étrangère de modéliser une relation récursive, ce qui signifie que le SGBD l'autorise implicitement par défaut. Donc, si nous voulons éviter les situations où un uplet se référence lui-même, nous devons ajouter des contraintes explicites, que nous pouvons classer comme intégrité référentielle.

## Chapitre 6 : Diagramme de schéma relationnel

Après avoir introduit le modèle relationnel au niveau conceptuel, nous devons nous rappeler qu'il s'agit du premier niveau de conception de base de données. Maintenant, sur la base du diagramme entité-relation, nous devons déterminer les tables qui composeront la base de données, ainsi que les clés qu'elles posséderont pour s'identifier et se référencer mutuellement. Nous devons également définir les contraintes qui garantissent la validité et l'intégrité des données.

Ainsi, même si nous avons déjà introduit certains concepts de conception logique, nous allons formaliser ici la conception logique elle-même à travers des diagrammes de schéma relationnel, parfois appelés diagrammes relationnels par souci de simplicité.

![Diagramme de schéma relationnel où Pool référence City via une clé étrangère. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752067358857/9f4bba9e-330a-44d3-b162-32681c5e5196.png align="center")

Comme vous pouvez le voir, nous avons ici un diagramme relationnel représentant la conception logique associée au dernier diagramme entité-relation de la section précédente.

Tout d'abord, au lieu d'entités, nous avons ici des tables, chacune avec une série d'attributs. Si un attribut est utilisé dans une clé primaire, il est souligné comme PoolID ou CityID, tous les autres attributs étant des attributs de table "normaux". De plus, les clés étrangères sont représentées directement par des flèches. Dans ce cas, CityFK est une clé étrangère qui référence l'attribut CityID de la table City car il s'agit d'une clé primaire, c'est pourquoi elle est désignée par une flèche pointant de l'attribut de clé étrangère vers l'attribut correspondant dans l'autre table.

En ce qui concerne la clé étrangère, gardez à l'esprit qu'un attribut ne peut pointer que vers un seul autre attribut – ce qui signifie que CityFK ne peut avoir qu'une seule flèche pointant vers un attribut, et non plusieurs, car la clé étrangère référence un attribut unique dans une autre table. Si on nous demandait de convertir ce diagramme relationnel en un diagramme entité-relation, la clé étrangère elle-même déterminerait les cardinalités de l'association (au moins les cardinalités maximales, puisque, pour que cette clé étrangère ait un sens, au niveau conceptuel, cela se traduirait par une piscine se trouvant dans une seule ville au plus, tandis qu'une ville peut avoir un nombre arbitraire de piscines).

Ces types de diagrammes ne sont pas standardisés comme UML. Ils doivent seulement répondre aux caractéristiques mentionnées précédemment. C'est pourquoi, dans de nombreux cas, les tables sont représentées par des carrés similaires aux entités UML au lieu d'être affichées au format textuel avec Datalog.

Mais contrairement aux diagrammes UML, il y a très peu de restrictions implicites ici. La plupart des restrictions doivent être ajoutées avec des notes dans les marges. Par exemple, pour indiquer qu'un attribut ne peut pas avoir de valeur NULL, nous ne pouvons pas le faire avec des éléments de diagramme – il doit être représenté par d'autres moyens, comme une note ou un morceau de code en **OCL**.

### Association 1-1

Compte tenu de la nature des diagrammes relationnels, nous pouvons en déduire que les entités sont directement transférées au modèle logique avec des tables, où chaque entité correspond à une table. Mais en plus des tables, nous devons implémenter les associations entre entités au niveau logique.

Pour ce faire, nous commençons par le cas le plus simple, qui est une association où la cardinalité maximale des deux côtés est 1, comme dans l'exemple que nous avons vu précédemment où nous avions une entité Person composée d'une entité Brain, dont la traduction en diagramme relationnel serait la suivante.

![Diagramme de schéma relationnel où Person et Brain se référencent mutuellement via des clés étrangères. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752069584062/a369d85c-5287-48e8-8822-18f503c0ae9e.png align="center")

Comme vous pouvez le voir, les deux entités sont représentées par des tables, où les attributs de leurs clés primaires sont soulignés. De plus, même s'ils n'apparaissent pas dans le diagramme conceptuel, nous devons refléter l'existence d'attributs de clé étrangère utilisés pour implémenter l'association elle-même.

Nous avons donc ajouté des attributs avec des noms qui indiquent au mieux qu'il s'agit de clés étrangères. Dans ce cas, le nom se termine par FK, bien que vous puissiez utiliser n'importe quel nom. Ainsi, pour qu'un cerveau soit associé à une personne, sa clé étrangère correspondante se réfère à la clé primaire de la table qui stocke les personnes. Comme l'autre sens de l'association est symétrique, nous faisons de même avec la clé étrangère de Person (qui se réfère à la clé primaire de Brain afin qu'une personne puisse être associée à son cerveau correspondant). Nous faisons cela avec des clés étrangères par souci de simplicité et parce que c'est le seul moyen de déterminer quel cerveau possède chaque personne et à qui appartient chaque cerveau.

En raison de l'association 1-1, vous ne devriez généralement pas laisser ce type d'association en raison de la surcharge causée par l'utilisation de plusieurs clés étrangères référençant dans les deux sens, et de la redondance au niveau conceptuel. Si chaque personne a un cerveau et un seul, et vice versa, il est probable que les deux puissent être "fusionnés" et modélisés comme un concept unique, en déplaçant tous les attributs qui caractérisent Brain vers l'entité Person, par exemple. Mais il existe d'autres façons d'affiner le schéma, ou il arrive que le domaine ou les exigences nous obligent à maintenir ce type de relation, auquel cas elle serait parfaitement valide.

### Association 1-M

Un autre type d'association que nous devons traduire au niveau logique est appelé 1-M (ou 1-N), qui se réfère aux associations où les cardinalités maximales des deux côtés sont respectivement 1 et *, où M signifie une quantité arbitraire.

![Diagramme entité-relation où chaque House appartient à une seule Person, qui peut avoir plusieurs maisons. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752069775099/caf1b28f-a301-451a-942f-a6a381f10ca5.png align="center")

Par exemple, nous avons ici une relation 1-M entre les entités House et Person, où une maison doit appartenir à une personne, et une personne peut avoir un nombre arbitraire de maisons, y compris aucune. Au niveau logique, nous pouvons représenter cela comme suit :

![Diagramme de schéma relationnel où House référence Person via une clé étrangère. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752074660667/ba64c7d8-7315-4f00-b3ff-0915af14d5d4.png align="center")

Tout comme auparavant, nous implémentons les deux entités avec des tables, et l'association 1-M entre elles avec une clé étrangère dans l'entité du côté où la cardinalité maximale est *. Plus précisément, pour éviter les groupes répétitifs, nous plaçons la clé étrangère dans house, puisqu'une maison ne peut avoir qu'une seule personne comme propriétaire. Cela signifie qu'il ne sera pas nécessaire de stocker un nombre arbitraire de références dans l'attribut de sa clé étrangère – une seule suffit.

Et comme toujours, la clé étrangère se réfère à la clé primaire de Person, afin qu'elle puisse référencer une valeur d'un attribut capable d'identifier de manière unique une personne, et ainsi déterminer le propriétaire d'une maison.

### Problèmes de cardinalité minimale

En ce qui concerne le diagramme entité-relation précédent, nous pouvons voir que le côté 1..1 indique qu'au minimum, une maison doit toujours être associée à une personne qui en sera le propriétaire. Cela signifie qu'une maison doit toujours avoir un propriétaire. Mais ce n'est pas réaliste, car lorsqu'une maison est construite, elle peut rester sans propriétaire pendant un certain temps, ce qui fait passer la cardinalité de ce côté de l'association à 0..1.

À son tour, la cardinalité minimale de 0 signifie qu'une maison peut ne pas avoir de propriétaire – sa clé étrangère ne devrait donc pas exister tant que la maison n'a pas de propriétaire. Pour modéliser cela, les attributs, y compris les clés étrangères, sont autorisés à prendre NULL comme valeur par défaut (comme nous l'avons vu précédemment). De cette façon, pour représenter que la clé étrangère ne pointe nulle part, nous choisissons simplement de ne pas restreindre la possibilité qu'elle prenne cette valeur NULL. Ainsi, lorsqu'une maison n'a pas de propriétaire, son attribut de clé étrangère sera NULL jusqu'à ce qu'il référence une personne – c'est-à-dire un uplet dans la table Person.

Cette situation, où une clé étrangère est autorisée à prendre la valeur NULL, n'est pas explicitement indiquée dans le diagramme relationnel. Au contraire, elle est indiquée lorsque la situation inverse se produit – où si la clé étrangère ne peut pas être NULL, nous devons ajouter une note l'indiquant clairement (comme c'est le cas dans le diagramme entité-relation original que nous venons de voir).

D'un autre côté, l'association dans le diagramme a une multiplicité de 0..* du côté de House, indiquant qu'une personne n'a pas à posséder de maison. Mais si nous avions une cardinalité minimale supérieure à 0, alors cette restriction devrait être définie avec une note dans le diagramme relationnel, ainsi qu'avec des outils SQL spécifiques (puisqu'il n'existe pas d'éléments standards pour modéliser ce type d'exigence causée par des cardinalités minimales dans une telle situation).

### Association N-M

Pour en finir avec les types d'associations selon leur cardinalité, la seule qu'il reste à traduire est N-M. Dans ce cas, N et M désignent des quantités arbitraires, c'est-à-dire des associations dont les cardinalités maximales sont toutes deux * en même temps.

![Diagramme entité-relation où House et Person ont une relation plusieurs-à-plusieurs. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752077406305/f54614f5-082a-4541-bc82-7146ffc640db.png align="center")

À titre d'exemple, nous pourrions avoir un domaine où une personne peut posséder de nombreuses maisons, et une maison peut appartenir à de nombreuses personnes en même temps. Pour modéliser cette situation au niveau conceptuel, la première chose à laquelle nous pourrions penser est de créer un diagramme comme celui-ci, où nous mettons seulement une association avec une cardinalité 0..* des deux côtés.

Conceptuellement, cela serait cohérent, mais logiquement, cela ne peut être traduit d'aucune manière. C'est-à-dire que si nous avons une association avec une cardinalité maximale de * des deux côtés et que nous essayons de l'implémenter logiquement à l'aide de clés étrangères comme nous l'avons fait jusqu'à présent, nous constaterons que même si nous mettons une clé étrangère dans les deux entités référençant l'entité de l'autre côté de l'association, le problème du groupe répétitif apparaîtra toujours dans les deux entités, quoi que nous fassions d'autre.

Pour comprendre cela, nous pouvons le regarder conceptuellement. Si une personne possède un nombre indéterminé de maisons et que nous mettons une clé étrangère dans Person référençant House, alors cette clé étrangère devrait contenir des références à chacune des maisons possibles que la personne pourrait avoir. Comme il ne s'agit pas d'un nombre fixe, un groupe répétitif apparaît dans la clé étrangère.

La même chose se produit à l'inverse : si une maison peut avoir un nombre arbitraire de propriétaires, alors l'inclusion d'une clé étrangère dans House référençant Person provoquerait un groupe répétitif dans la clé étrangère. Ce type d'association n'a donc pas d'implémentation directe au niveau logique.

Mais en réalité, ces situations ne se produisent généralement pas de cette manière. Au contraire, il est courant qu'il y ait une classe intermédiaire dans l'association qui permette son implémentation au niveau logique, comme dans l'exemple suivant :

![Diagramme entité-relation où Property relie les maisons et les personnes avec les dates de vente et les prix. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752070941510/823b8d0c-c00f-4115-92bb-59b31f8fc1a1.png align="center")

Ici, nous avons une situation similaire à la précédente, où une personne peut posséder un nombre arbitraire de maisons, et une maison peut appartenir à un nombre arbitraire de personnes. La différence ici est que nous supposons que l'une des exigences du domaine est d'enregistrer quand une personne achète et vend une maison, ainsi que le prix auquel elle a été achetée. Nous n'avons pas besoin du prix de vente car il s'agira du prix d'achat pour une autre occurrence de Property.

Pour cela, nous utilisons une entité intermédiaire Property qui stocke ces données, où nous devons garder à l'esprit que DateVente ne doit pas "exister" tant que la maison n'est pas réellement vendue, si elle est vendue. Ainsi, pour traduire cela au niveau logique, l'approche la plus simple consiste à autoriser DateVente à être NULL jusqu'à ce que la maison soit vendue.

![Diagramme de schéma relationnel où Property référence House et Person via des clés étrangères. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752071179227/4dd3de56-2a14-4cbc-ab56-944445b7de91.png align="center")

Comme nous pouvons le voir, cette situation peut maintenant être traduite en un diagramme relationnel, c'est-à-dire au niveau logique. En effet, toutes les entités peuvent être représentées sous forme de tables. Et comme les associations sont de type 1-M, nous savons déjà comment les implémenter à l'aide de clés étrangères, spécifiquement dans l'entité Property référençant les clés primaires des deux autres entités, respectivement.

Cela ne signifie pas que chaque fois que nous avons une relation N-M, nous devons introduire une entité intermédiaire pour l'implémenter. Parfois, nous avons besoin d'une classe intermédiaire pour stocker des informations, comme dans ce cas, et dans d'autres situations, nous pourrions avoir besoin d'affiner le schéma parce que la relation N-M ne représente pas au mieux le domaine.

Mais si nous avons réellement besoin d'implémenter une relation N-M et que nous sommes sûrs que cette relation est conceptuellement correcte, nous pouvons toujours ajouter une entité intermédiaire artificielle qui n'a pas d'autres attributs que les clés étrangères des deux associations (les deux étant la clé primaire), ce qui en fait une entité faible en identification.

![Diagramme entité-relation où Property est une entité faible qui relie House et Person avec des données de vente. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752070430749/a6f7f0cc-7fcb-4fce-ac0f-6d41fc1e7610.png align="center")

Par exemple, en considérant la situation où nous devons stocker des informations dans une classe intermédiaire, nous avons vu précédemment que Property avait sa propre clé primaire, **PropertyID**, probablement dérivée d'une clé substitutive. Mais s'il n'y a pas de clé substitutive, nous devons essayer d'identifier les uplets de Property à travers leurs attributs. Dans ce cas, ce n'est pas possible compte tenu de leur sémantique – c'est-à-dire de la signification de ce qu'ils stockent – car il pourrait y avoir plusieurs uplets avec les mêmes dates, prix, etc.

Ainsi, sachant que deux clés étrangères apparaîtront dans Property référençant House et **Person** lors de la traduction au niveau logique, nous pouvons les utiliser pour définir la clé primaire de Property en utilisant **DateAchat** et les attributs de clé étrangère eux-mêmes.

Nous faisons cela parce que si nous faisons seulement en sorte que la clé primaire soit constituée des clés étrangères, alors Property ne peut pas être identifiée de manière unique si une personne achète et vend la même maison au cours de plusieurs périodes différentes. Nous ajoutons donc DateAchat à la clé primaire pour distinguer également par date d'achat, car **DateVente** peut être **NULL** (ce qui viole la contrainte d'intégrité fondamentale des clés primaires selon laquelle aucun de leurs attributs ne peut être NULL). Grâce à cela, l'entité **Property** devient faible en identification, c'est pourquoi nous avons ajouté **«weak»** des deux côtés, indiquant que nous avons besoin des deux clés étrangères pour l'identification.

![Diagramme entité-relation où Property lie les maisons et les personnes avec des informations d'achat et de vente. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752070636272/b40fe320-933b-46c3-98b0-7d0838c59de1.png align="center")

De même, dans ce cas, puisque la faiblesse d'identification affecte les entités des deux côtés (ce qui signifie que nous avons besoin des clés étrangères référençant les entités des deux côtés de Property), elle peut être représentée conceptuellement avec une entité associative liée à l'association M-N entre House et Person. Cela reste équivalent au diagramme précédent, à la seule différence que la classe intermédiaire est représentée différemment.

De plus, il est important de noter que si Property avait une clé substitutive et n'avait pas besoin de clés étrangères pour son identification, cette représentation à l'aide d'une entité associative ne serait pas valide. En fin de compte, l'entité associative n'est valide à utiliser dans ce contexte que lorsque l'entité intermédiaire **dépend** des deux entités liées pour son identification, celles-ci étant ses entités propriétaires.

![Diagramme de schéma relationnel où Property référence House et Person via des clés étrangères. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752071302075/d712f40f-1b86-4a5c-bc84-0f5f33851215.png align="center")

En ce qui concerne la traduction au niveau logique de ce dernier cas, nous le faisons de la même manière – la différence étant que nous n'avons plus l'attribut PropertyID dans Property. De plus, sa clé primaire est désormais **{DateAchat, HouseFK, PersonFK}**, nous soulignons donc tous ces attributs.

En règle générale, lorsqu'une clé étrangère est soulignée dans un diagramme relationnel, cela indique que l'entité de niveau conceptuel correspondant à la table est faible en identification. Cela nous permet de savoir de combien d'entités elle dépend – c'est-à-dire ses entités propriétaires.

### Hiérarchie IS-A

Après avoir vu comment les entités et les associations du modèle relationnel sont traduites au niveau logique, comprenons maintenant comment les relations spéciales de généralisation et de spécialisation entre les entités elles-mêmes sont traduites.

Pour ce faire, nous allons commencer par un exemple de hiérarchie IS-A. Cela signifie fondamentalement qu'une ou plusieurs entités, comme CityPool, sont une spécialisation d'une autre entité plus générale, Pool. C'est très similaire à ce qui se passe en programmation orientée objet avec l'héritage.

La hiérarchie d'héritage est appelée IS-A (est un) car si CityPool hérite de Pool, alors elle est plus spécifique que Pool. Cela signifie que chaque piscine municipale est une piscine, mais elle possède des attributs spécifiques qui caractérisent les piscines municipales, tels que leur capacité maximale d'utilisateurs ou le prix du billet.

![Diagramme entité-relation avec héritage où CityPool et OlympicPool sont des sous-classes de Pool. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752081799527/5f6d4146-0884-4ba5-8125-3ae064748ff6.png align="center")

Avant de voir comment elles sont traduites au niveau logique, il est important de savoir que les hiérarchies IS-A possèdent une série de contraintes de spécialisation qui déterminent la "relation" que l'entité parente (Pool ici, parfois appelée superclasse) entretient avec les entités spécifiques. En d'autres termes, si nous considérons que les entités sont en réalité des ensembles contenant toutes leurs occurrences (uplets) (que nous appellerons ici individus pour garder un concept plus "général"), loin des détails du modèle conceptuel et logique, alors nous pouvons établir des contraintes telles que la **complétude** ou la **disjonction** d'une hiérarchie.

Pour comprendre la complétude en utilisant cet exemple, nous pouvons d'abord avoir des hiérarchies complètes, où tous les individus de l'entité Pool doivent nécessairement appartenir aux ensembles d'individus de l'une des entités spécifiques qui héritent de la superclasse Pool.

Dans ce cas, la superclasse **Pool** est une entité qui contient toutes les piscines existantes. Ainsi, certaines d'entre elles pourraient être des piscines municipales, appartenant à l'ensemble des individus généré par l'entité héritière **CityPool**. D'autres pourraient être des piscines olympiques, qui appartiennent à l'ensemble des individus de **OlympicPool**.

Dans notre modèle, nous n'avons spécifié que ces deux types de piscines, alors qu'en réalité, il existe de nombreux autres types de piscines. Dans cette hiérarchie, elles seraient représentées par des individus dans l'ensemble généré par Pool, car elles n'ont aucune classe héritière à laquelle appartenir. Ainsi, dans ce cas, notre hiérarchie ne serait pas complète, mais **partielle**, puisqu'il existe des piscines qui n'appartiennent à aucune entité héritière.

D'un autre côté, la **disjonction** se réfère à la possibilité pour les individus d'appartenir à plus d'une entité héritière en même temps. Par exemple, dans notre cas, une piscine est soit une piscine municipale, soit une piscine olympique, soit elle n'est aucun de ces types – nous ne trouverons donc jamais de piscine qui soit à la fois municipale et olympique en même temps.

Si nous considérons les ensembles d'individus des entités héritières, la hiérarchie est considérée comme **disjointe** lorsque ces ensembles sont disjoints, comme dans ce cas où les piscines sont soit d'un type, soit de l'autre, mais pas les deux en même temps. Inversement, dans les cas où ce dernier se produit, la hiérarchie est dite avec chevauchement (overlapping).

#### 1 table

Sachant maintenant que la hiérarchie de notre exemple est incomplète (appelée partielle) et disjointe, nous devons implémenter ce qui est représenté dans le diagramme entité-relation au niveau logique.

Nous avons plusieurs options pour cela. Une option consiste à implémenter toute la hiérarchie IS-A avec une seule table, Pool, qui rassemble tous les attributs des tables de la hiérarchie.

![Image de l'auteur. Schéma relationnel où Pool inclut des attributs pour la capacité, le prix et les caractéristiques de compétition.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752083879943/097a29cd-6b8d-41ca-ad49-6bed9562026a.png align="center")

Comme vous pouvez le voir, dans cette option, nous implémentons une table qui contient tous les attributs des trois tables, où PoolID fonctionne comme la clé primaire de toute la table Pool, puisque dans la conception conceptuelle, des identifiants spécifiques ne sont généralement pas attribués aux entités héritières, sauf si nécessaire. C'est pourquoi PoolID apparaît souligné. Quant au reste, ils fonctionnent de la même manière que s'ils étaient dans leurs entités respectives.

D'une part, cette option présente l'avantage de n'utiliser qu'une seule table pour toute la hiérarchie, ce qui la rend plus facile à comprendre et à maintenir. Elle évite également l'éventuelle redondance consistant à stocker les mêmes informations dans plusieurs tables.

Mais d'un autre côté, elle présente des problèmes importants. Tout d'abord, nous n'avons aucun moyen simple de distinguer une piscine d'une piscine municipale ou d'une piscine olympique, ce qui signifie que la seule façon de connaître le type spécifique de piscine qu'un uplet de la table Pool représente est d'avoir certains attributs à NULL.

Par exemple, si un uplet représente une piscine de l'entité Pool, alors tous les attributs de CityPool et OlympicPool doivent être NULL afin que l'uplet correspondant ne prenne des valeurs que dans les attributs de l'entité Pool. Cela nous permet de déterminer que l'uplet représente un "individu" de l'ensemble des occurrences de l'entité Pool.

La même chose se produit lorsque nous essayons de distinguer les piscines municipales, où tous les attributs de OlympicPool doivent être NULL, puisque CityPool hérite de tous les attributs de l'entité Pool. Ainsi, tous ces attributs plus ceux spécifiques à CityPool auront des valeurs, tandis que ceux de OlympicPool seront NULL pour indiquer que la piscine est une piscine municipale. Cela se produit également lorsque nous voulons savoir si un uplet représente une piscine olympique, où les attributs de CityPool seront NULL.

Ainsi, si nous implémentons la hiérarchie IS-A avec une seule table, nous aurons le problème de distinguer les types de piscines – c'est-à-dire de savoir si un uplet représente une occurrence de l'entité superclasse ou de l'une des entités héritières. Cela pourrait conduire à un nombre potentiellement important de valeurs NULL occupant un espace inutile dans la table, même si travailler avec une telle table peut être facile à comprendre.

De plus, nous pouvons également considérer la facilité avec laquelle le schéma peut être étendu ou modifié comme un avantage. En effet, si une clé étrangère est ajoutée plus tard dans notre domaine dans l'une des 3 tables de la hiérarchie référençant une autre entité, il suffirait simplement d'ajouter un attribut de clé étrangère à la table Pool. De même, si une clé étrangère externe pointe vers l'une des entités de la hiérarchie, elle n'aurait qu'à référencer PoolID.

#### 2 tables

Pour remédier au problème de distinction précédent, une autre option dont nous disposons pour implémenter la hiérarchie consiste à utiliser deux tables, ou autant qu'il y a d'entités héritières. La base de cela est que toutes les entités héritières possèdent les mêmes attributs que la superclasse dont elles héritent, plus une série d'attributs spécifiques qui les caractérisent.

Ainsi, pour distinguer logiquement les entités héritières, nous pouvons implémenter des tables spécifiques pour chacune, où elles possèdent les mêmes attributs que la superclasse plus les leurs.

![Schéma relationnel où CityPool et OlympicPool héritent des attributs communs et ajoutent des champs spécifiques. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752084244540/f47a6034-0fa1-43e4-8040-ad5177e1976d.png align="center")

Comme vous pouvez le voir, dans cette option, nous implémentons les tables CityPool et OlympicPool, qui sont chargées de stocker les uplets représentant respectivement les piscines municipales et les piscines olympiques. Comme chacune contient les mêmes attributs que la sous-classe, même s'ils ne sont pas explicitement copiés dans les entités héritières dans le diagramme conceptuel, les deux ont la même clé primaire, PoolID.

Cette implémentation offre divers avantages : tout d'abord, nous éliminons les valeurs NULL inutiles utilisées pour distinguer les types de piscines, du moins celles modélisées via les entités héritières. De plus, le schéma reste simple, étant facilement compréhensible et maintenable en raison de la sémantique de chaque table.

Mais il y a aussi un problème de distinction ici, car notre hiérarchie n'est pas complète. Cela signifie qu'il y aura des piscines qui ne sont ni municipales ni olympiques, elles ne peuvent donc pas être représentées par des uplets de CityPool ou OlympicPool. En d'autres termes, cette option ne fonctionne pas pour représenter des hiérarchies incomplètes, car la seule façon de représenter une piscine qui n'est d'aucun de ces types serait d'insérer un uplet identique dans CityPool et OlympicPool avec tous les attributs n'appartenant pas à la superclasse mis à NULL. Mais cela serait très contre-productif en termes d'utilisation de la mémoire, et serait également compliqué à gérer.

D'un autre côté, même si la hiérarchie était complète, un inconvénient possible à considérer est la répétition des attributs de la superclasse dans toutes les tables, où cette répétition gaspille de l'espace dans notre base de données.

Mais même si nous avons de l'espace supplémentaire et que nous pouvons nous permettre de répéter tous ces attributs, si nous voulons rassembler toutes les données sur toutes les piscines *(ou individus)* qui existent, nous devrions collecter les données présentes dans toutes les tables, ce qui peut ne pas être tout à fait efficace.

Enfin, si notre modèle conceptuel possède une clé étrangère référençant l'entité superclasse Pool, nous devons considérer que la clé primaire de Pool a maintenant été transférée aux deux tables. Cela signifie que cette clé étrangère devrait référencer les deux tables à la fois, ce qui n'est pas possible. Ainsi, au lieu de référencer un attribut d'une table, elle devrait référencer PoolID à la fois de CityPool et de OlympicPool. Cela compliquerait, voire rendrait impossible, l'implémentation au niveau logique.

En ce qui concerne les clés étrangères, cette option permettrait effectivement d'implémenter facilement une clé étrangère dans l'une des entités, CityPool ou OlympicPool, qui référence une autre entité (ou même des clés étrangères qui référencent ces entités de manière simple).

![Schéma relationnel où OlympicPool hérite de Pool, ajoutant des attributs de compétition et de certification. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752084458598/f27a5174-8f88-4ed1-8459-1dd1cb15c8dc.png align="center")

Mais, si nous insistons pour utiliser deux tables pour implémenter la hiérarchie, nous pourrions affiner le schéma logique pour résoudre le problème d'une clé étrangère référençant la superclasse de cette manière.

Comme vous pouvez le voir ci-dessus, nous avons deux tables où l'une est exclusivement dédiée au stockage des uplets contenant les attributs caractérisant une piscine olympique. L'autre entité englobe toutes les piscines, y compris les piscines municipales et les piscines olympiques. C'est parce qu'une piscine olympique hérite également des attributs de la superclasse, donc pour la représenter dans ce schéma, nous créons deux uplets : un dans Pool qui stocke les valeurs des attributs de la superclasse, laissant le reste à NULL, et un autre uplet dans OlympicPool qui stocke les attributs restants, avec sa clé étrangère (qui est aussi la clé primaire), référençant l'uplet correspondant dans Pool avec les valeurs d'attribut de la superclasse.

L'avantage principal de cette option est qu'elle résout le problème d'avoir une clé étrangère externe référençant Pool – car dans ce cas, elle n'aurait qu'à pointer vers la clé primaire {PoolID} de Pool, au lieu de plusieurs attributs à la fois comme c'était le cas auparavant.

Mais cela nous laisse avec un schéma nettement plus complexe à comprendre et à manipuler, car la façon de stocker une piscine municipale est totalement différente du stockage d'une piscine olympique. Cela complique certaines opérations comme l'insertion d'une piscine olympique, où nous devrions créer deux uplets dans Pool et OlympicPool afin que la clé primaire/étrangère de OlympicPool pointe vers l'uplet créé dans Pool. Cela complique également le comptage des piscines qui ne sont ni olympiques ni municipales dans le système, où tous ces uplets dans Pool avec NULL dans les attributs caractérisant les piscines municipales doivent être trouvés.

Enfin, bien que nous voyions que la clé primaire de OlympicPool est également étrangère dans cette implémentation, cela n'implique pas que conceptuellement il s'agisse d'une entité faible en identification. Il existe de nombreuses façons d'implémenter la hiérarchie, et celle-ci n'est pas nécessairement celle qui doit être réalisée.

#### 3 tables

Ainsi, si nous avons une hiérarchie incomplète et que nous voulons vraiment nous assurer que l'implémentation nous permet de distinguer les différents types de piscines et d'identifier les piscines qui n'appartiennent à aucune entité héritière, nous pouvons utiliser trois tables – une pour chaque entité, respectivement.

![Schéma relationnel où CityPool et OlympicPool héritent de Pool, ajoutant des attributs spécifiques. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752084637220/69491535-2a0c-4080-bf09-10967addced1.png align="center")

La particularité de ce schéma est que puisque toutes les piscines contiennent les attributs de la superclasse Pool, chaque fois qu'il y a une piscine dans notre base de données, elle sera représentée par un uplet dans la table Pool qui ne contient que les valeurs des attributs de la superclasse. Et, si une piscine est d'un type spécifique, elle sera représentée non seulement par l'uplet Pool mais aussi par un uplet dans l'une des tables réservées aux entités héritières, où chacune possède une clé étrangère pointant vers la clé primaire {PoolID} de Pool.

Par exemple, une piscine municipale peut être représentée par un uplet dans CityPool (qui ne possède que les attributs spécifiques qui la caractérisent comme piscine municipale) plus une clé étrangère pointant vers un uplet spécifique dans Pool qui détient les valeurs des autres attributs hérités.

L'avantage de ce schéma est qu'il minimise l'espace gaspillé par les informations dupliquées ou l'apparition de valeurs NULL (car la seule chose qui est "dupliquée" ici est l'attribut PoolID en tant que clés étrangères dans les entités héritières). Il est également facile à comprendre car chaque entité est représentée par une table spécifique au niveau logique.

De plus, le schéma est facile à modifier dans les cas où nous devons ajouter des clés étrangères aux entités, où il suffirait simplement d'ajouter un attribut de clé étrangère supplémentaire ou d'implémenter des clés étrangères externes pointant vers les entités elles-mêmes, ce que nous pouvons faire en référençant leurs propres clés primaires et étrangères {PoolID}.

Si nous ajoutons un nouveau type de piscine au domaine plus tard, il est facile d'ajouter une table très similaire à celles que nous avons déjà. Contrairement aux options précédentes que nous avons vues où l'ajout d'un nouveau type de piscine serait plus coûteux en raison des éléments nécessitant une modification. De plus, le fait d'avoir trois tables facilite la modélisation des contraintes liées à la complétude et à la disjonction de la hiérarchie.

Mais ce schéma présente également certains problèmes. D'une part, si nous avons une piscine municipale et que nous voulons connaître son nom, nous devrons accéder à la table Pool pour trouver son nom, en plus de la table CityPool. Cela complique la requête et affecte son efficacité et sa latence.

En dehors de cela, si nous avons un uplet de Pool et que nous voulons savoir s'il s'agit d'une piscine municipale, d'une piscine olympique ou d'aucune des deux, nous devrons parcourir tous les uplets de CityPool et OlympicPool pour voir si la clé étrangère de l'un d'eux pointe vers l'uplet Pool que nous essayons d'identifier.

De plus, la présence de trois tables est plus complexe que d'en avoir seulement une ou deux, ce qui rend le modèle logique un peu plus compliqué à manipuler car il y a plus de tables et plus de relations entre elles.


#### Quand modéliser chaque entité comme une table

Ces alternatives ne sont pas les seules options pour implémenter une hiérarchie IS-A au niveau logique. Selon les besoins et les exigences du domaine, nous pouvons choisir d'autres schémas plus appropriés qui sont similaires à ceux dont nous avons déjà discuté.

Pour résumer quel est le meilleur schéma que nous pouvons implémenter pour modéliser une hiérarchie IS-A au niveau logique, nous devons savoir quand il est approprié d'introduire une table pour chaque entité.

Tout d'abord, nous avons la **super-classe**. Il est utile de la modéliser avec une table spécifique dans les cas où la hiérarchie est incomplète, comme dans la hiérarchie d'exemple. Nous avons vu que sans une table Pool dédiée pour représenter les occurrences de l'entité super-classe, il est difficile de distinguer quand une piscine est du type générique de la super-classe ou est au contraire d'un type spécifique (comme celui des entités héritières). Il est également utile d'implémenter une table pour la super-classe lorsqu'une clé étrangère pointe vers l'entité super-classe elle-même. Sinon, il est très probable que nous ayons du mal à savoir quel attribut la clé étrangère doit référencer, comme nous l'avons vu précédemment.

Et pour en finir avec la super-classe, nous devrions également implémenter une table pour elle lorsque la hiérarchie est **non disjointe** ou **avec chevauchement (overlapping)**. Par exemple, si une piscine pouvait être de plusieurs types à la fois et que nous n'avions pas la table Pool, nous serions obligés de dupliquer les informations dans des tables spécifiques pour les entités héritières. Cela compliquerait grandement les opérations de base de données.

Ainsi, avec notre table Pool, nous pouvons avoir des uplets dans les tables respectives des entités héritières, tous avec leurs clés étrangères pointant vers le même uplet Pool, ce qui simplifie les requêtes.

Si nous avons une table Pool où toutes les piscines existantes sont stockées, il est probable que nous voudrions savoir efficacement le type d'une piscine à partir d'un uplet Pool. Au lieu de devoir parcourir tous les uplets des tables des entités héritières, nous pouvons ajouter un attribut dans Pool qui détermine son type (s'il en a un), ou qui sera NULL si la hiérarchie est incomplète et qu'elle n'appartient à aucun type.

C'est ce qu'on appelle un discriminateur explicite. S'il n'y en a pas, nous disons généralement qu'il existe un discriminateur implicite. Ce sont les clés étrangères des autres tables que nous devrions parcourir pour trouver le type.

En ce qui concerne les entités héritières, nous devrions créer une table pour chacune d'elles lorsqu'elles possèdent de nombreux attributs, ce qui entraînerait de nombreuses valeurs NULL si nous devions implémenter cela avec seulement une ou deux tables. Outre les attributs, les entités héritières elles-mêmes peuvent avoir des contraintes de domaine spécifiques qui sont grandement simplifiées au niveau logique si nous implémentons des tables pour chacune d'elles. Cela éviterait d'avoir à appliquer des contraintes sur seulement une ou deux tables, ce qui compliquerait la sémantique des contraintes.

En résumé, plus nous combinons d'entités dans une seule table, plus nous rencontrerons de valeurs NULL, car pour les **distinguer**, les attributs de la table qui ne correspondent pas au concept ou à l'entité que nous voulons représenter doivent être NULL, comme s'ils n'existaient pas.

Cela compliquerait également les opérations de base de données, car les opérations devraient tenir compte des attributs qui doivent ou ne doivent pas être NULL – tout comme les contraintes – qui doivent prendre en compte la présence de valeurs NULL pour être vérifiées.

D'un autre côté, si nous savons que la hiérarchie est complète, alors au lieu d'implémenter une table pour la super-classe, nous pouvons décider d'implémenter des tables pour chaque entité héritière, où chacune possède les attributs de la super-classe. Mais cette option perd de son intérêt lorsque nous avons une super-classe avec trop d'attributs, qui seraient répétés dans plusieurs tables, potentiellement nombreuses.

## Chapitre 7 : Normalisation

Lorsqu'on essaie de traduire une hiérarchie IS-A au niveau logique, il est très probable que l'on aboutisse à une conception qui présente de la **redondance**. En effet, la même information, comme celle de la super-classe, peut finir par être stockée à plusieurs endroits. Cela pose de multiples problèmes dans une base de données. Pour le comprendre, considérons l'exemple suivant :

| **PersonID** | **PersonName** | **CityID** | **CityName** |
| --- | --- | --- | --- |
| 1 | Alice Johnson | 1 | Madrid |
| 2 | Bob Smith | 5 | Paris |
| 3 | Carol Davis | 3 | New York |
| 4 | David Brown | 1 | Madrid |
| 5 | Emily Wilson | 5 | Paris |

Ici, nous avons une table Person qui stocke des données sur les personnes – spécifiquement leur ID, leur nom et la ville où elles vivent. Mais pour représenter la ville, tous les attributs que notre base de données stocke sur les villes sont inclus dans la table Person elle-même. Cela fait qu'en une seule ligne, nous pouvons connaître les informations sur la personne ainsi que les informations sur la ville respective.

À première vue, cela peut sembler pratique, car si nous avons une ligne Person, nous avons non seulement toutes les informations sur la personne mais aussi toutes les informations sur la ville correspondante. Cela nous permet d'éviter d'avoir à chercher ces informations dans d'autres tables. Mais cela crée un problème de redondance important.

Selon la définition, la redondance signifie que la même information est stockée à plusieurs endroits, c'est-à-dire répétée inutilement. Et cela ne signifie pas que l'information doit être dans des tables différentes. Par exemple, dans cet exemple, nous avons de la redondance car les mêmes informations de ville peuvent être stockées plusieurs fois dans la même table Person (comme c'est le cas pour la ville "Paris" ou "Madrid").

Cela entraîne en fait des problèmes lors de l'insertion de nouvelles villes dans la base de données. Si nous ne les stockons que dans cette table mais que nous n'avons aucune personne vivant dans la ville que nous voulons insérer, nous ne pourrons pas l'insérer à moins de le faire dans une ligne de la table Person avec le reste des attributs qui ne caractérisent pas une ville mis à NULL. Et cela compliquera grandement les opérations de base de données.

La **redondance pose également** un problème de consommation de mémoire, car le fait de dupliquer toutes les informations d'une ville pour chaque personne qui y vit utilise un espace inutile. De même, si nous voulons supprimer une ville ou mettre à jour ses informations, nous devons le faire pour chaque instance où cette information est répétée. Cela complique les opérations et les rend beaucoup moins efficaces.

Par exemple, si nous stockons un attribut Population dans cette table pour représenter la population de chaque ville, chaque fois que nous mettons à jour la population d'une certaine ville, nous devons le faire pour tous les uplets Person. Cela devient inefficace si de nombreuses personnes vivent dans cette ville, car nous devons changer la donnée de population dans tous les uplets représentant ces personnes.

Tout comme elle affecte l'efficacité, la redondance augmente également les chances d'incohérence des données. Si nous oublions de changer une valeur lors de la mise à jour des données de Population, ou s'il y a une erreur et qu'une certaine valeur dans un uplet ne se met pas à jour, alors cette valeur contredira le reste des valeurs de Population dans les uplets répétés pour cette ville, provoquant une **incohérence**.

Pour résoudre ce genre de situations, il est préférable de planifier à l'avance en créant une bonne conception au niveau conceptuel. Nous pouvons essayer de séparer les concepts en entités suffisamment distinctes pour éviter de stocker des informations sur des idées sémantiquement différentes dans la même entité (car cela pourrait causer de la redondance lors du passage au niveau logique).

Mais si nous atteignons le niveau logique avec un certain diagramme que nous n'avons pas pu affiner davantage au niveau conceptuel et que nous devons le raffiner, l'une des transformations que nous pouvons appliquer ici est appelée décomposition.

### Décomposition

| **PersonID** | **PersonName** | **CityID (FK)** |
| --- | --- | --- |
| 1 | Alice Johnson | 1 |
| 2 | Bob Smith | 5 |
| 3 | Carol Davis | 3 |
| 4 | David Brown | 1 |
| 5 | Emily Wilson | 5 |

| **CityID** | **Name** |
| --- | --- |
| 1 | Madrid |
| 3 | New York |
| 5 | Paris |

Avant d'examiner ce qu'implique la décomposition, il est utile d'examiner les problèmes spécifiques liés à la combinaison d'informations sur les personnes et les villes dans une seule entité.

Par exemple, si nous stockons de nombreux attributs d'une ville, beaucoup d'espace sera gaspillé si nous avons de nombreuses personnes vivant dans cette ville. En effet, toutes les valeurs des attributs de la ville sont répétées inutilement dans tous les uplets des personnes qui y vivent.

Un autre problème potentiel lié au gaspillage de mémoire pourrait survenir si nous devions insérer une personne dans la base de données et que nous ne connaissions pas la ville où elle vit. Cela nous obligerait à laisser tous les attributs de la ville à NULL, gaspillant tout l'espace occupé par ces NULL.

De même, si nous supprimons toutes les personnes vivant à "Madrid", par exemple, notre base de données ne contiendra plus aucune information sur cette ville, car personne n'y vit. Cela signifie qu'elle n'est pas explicitement stockée dans la table. Enfin, nous avons vu précédemment les problèmes qui survenaient lors de la mise à jour des informations d'une certaine ville.

Comme solution à ces problèmes, nous pouvons appliquer la décomposition. Si vous considérez l'exemple ci-dessus, vous pouvez voir que cela consiste à diviser la table Person en plusieurs tables. D'un côté, nous gardons la table Person dédiée au stockage des informations sur les personnes. De l'autre, pour les villes, nous stockons toutes leurs informations dans une table City spécifique.

Une fois les informations séparées en plusieurs tables, nous pouvons conserver l'attribut **CityID (FK)** dans la table Person, où il est maintenant converti en une clé étrangère qui référence le **CityID** de la nouvelle table **City**, indiquant la ville où vit la personne.

Comme vous pouvez le voir dans l'exemple, la décomposition consiste à remplacer une table par deux ou plusieurs tables, chacune contenant un sous-ensemble des attributs de l'originale. En les combinant, nous pouvons récupérer les attributs d'origine.

Par exemple, ici nous avons divisé une table en deux, l'une conservant tous les attributs liés aux personnes et l'autre les attributs liés aux villes. Ensemble, ces attributs forment la table originale que nous avions. Nous faisons cela principalement pour résoudre les problèmes causés par la redondance. Désormais, dans la table Person, nous ne stockons qu'un identifiant pour la ville où vit la personne, et dans la table City, nous ne stockons les informations de la ville qu'une seule fois, ce qui permet de les utiliser pour plus de tables dans la base de données.

Mais pour effectuer une décomposition correctement, nous devons nous assurer que certaines conditions sont remplies. L'une d'elles est que la décomposition soit **sans perte (lossless)**. Cela signifie que si nous prenons maintenant les deux tables générées par la décomposition et que nous combinons à nouveau toutes leurs informations en une seule table, nous devrions obtenir les informations que nous avions dans la table Person originale avant la décomposition.

Ainsi, si nous prenons maintenant la table Person résultante et que nous ajoutons à chaque uplet les informations fournies par l'uplet de la table City identifié par la clé étrangère définie lors de la décomposition, nous devrions obtenir les mêmes informations que celles que nous avions dans la table Person originale avant la décomposition – sans perdre d'uplets ni en créer de nouveaux.

Cette opération de jointure montre facilement qu'elle renvoie les données que nous avions initialement avant la décomposition. Et cela indique que la décomposition a été faite sans perte. Mais cela ne garantit pas qu'elle sera sans perte pour n'importe quel uplet possible. Pour s'en assurer, nous devons analyser les **dépendances fonctionnelles** présentes parmi les attributs de la table, qui doivent également être préservées après la décomposition.

Enfin, lors de l'exécution de la décomposition, nous pourrions recevoir des requêtes dans la base de données telles que, pour une personne donnée, obtenir des informations sur la ville où elle vit. Pour implémenter cette requête, nous effectuons généralement des opérations similaires à la jointure que nous avons décrite précédemment, ce qui peut être coûteux en termes de calcul. Ainsi, si cela devient si coûteux que c'est impraticable, nous pourrions envisager de ne pas faire la décomposition, ou même d'en faire une partielle, où nous gardons les attributs de la ville qui sont interrogés le plus fréquemment dans la table Person pour rendre certaines requêtes plus efficaces, même si une certaine redondance subsiste.

### Dépendance fonctionnelle

En continuant avec ces conditions, pour les comprendre correctement, vous devrez savoir ce que sont les dépendances fonctionnelles.

Pour introduire ce concept, nous pouvons regarder le cas le plus simple, qui sont les attributs PersonID et PersonName de la table Person. Ceux-ci stockent respectivement le numéro d'identification gouvernemental d'une personne et son nom. Ainsi, si nous trouvons plusieurs uplets dans la table Person avec la même valeur PersonID, nous nous attendons à ce que leurs valeurs PersonName respectives soient également les mêmes. En effet, si plusieurs uplets stockent des informations sur des personnes ayant le même ID, alors il doit nécessairement s'agir de la même personne (car nous supposons que le numéro d'identification gouvernemental est unique pour chaque personne).

Ainsi, chaque fois qu'il y a plusieurs uplets avec le même ID, nous pouvons dire que les noms des personnes représentées par ces uplets doivent également être les mêmes.

Mais l'inverse n'est pas forcément vrai, car si plusieurs personnes différentes ont le même nom, elles auront le même nom mais des ID différents. Donc, si plusieurs uplets ont le même PersonName, leurs PersonID respectifs ne correspondent pas forcément.

Cette situation que nous venons de voir est un cas de dépendance fonctionnelle entre **PersonID** et **PersonName**, spécifiquement notée **PersonID→PersonName**, car c'est l'attribut PersonID qui détermine de manière unique le nom de la personne.

| **PersonID** | **PersonName** | **CityID** | **CityName** |
| --- | --- | --- | --- |
| 1 | Alice Johnson | 1 | Madrid |
| 2 | Bob Smith | 5 | Paris |
| 3 | Carol Davis | 3 | New York |
| 4 | David Brown | 1 | Madrid |
| 5 | Emily Wilson | 5 | Paris |

Formellement, nous pouvons définir une dépendance fonctionnelle comme une contrainte ou une relation qui existe entre deux ensembles d'attributs, telle que les valeurs prises par un ensemble d'attributs déterminent de manière unique les valeurs que l'autre ensemble d'attributs doit prendre.

Par exemple, en utilisant le même exemple sans décomposition, nous pouvons voir qu'il existe une dépendance fonctionnelle entre l'ensemble d'attributs **X={PersonID}** et l'ensemble **Y={PersonName}**, notée **X→Y.** Cela signifie que pour toute paire d'uplets dans la table, si ces uplets ont les mêmes valeurs dans l'ensemble d'attributs X, alors ils doivent nécessairement avoir les mêmes valeurs dans l'ensemble d'attributs Y.

Mais nous ne découvrons pas cela par simple observation. Ces dépendances sont principalement données par les caractéristiques des attributs et le domaine que nous modélisons, ainsi que par les exigences. C'est-à-dire que pour découvrir ces dépendances, nous devons nous concentrer sur la sémantique des attributs.

La définition formelle de ce concept stipule qu'une dépendance fonctionnelle est une relation entre des ensembles d'attributs, ils n'ont donc pas besoin d'être des ensembles à attribut unique – ils peuvent en contenir n'importe quel nombre, selon la complexité de la dépendance.

Par exemple, si nous supposons qu'une personne vit toujours dans la même maison et ne déménage jamais, alors nous pouvons dire qu'il existe une dépendance fonctionnelle **{PersonID}→{CityID}**, ainsi que **{PersonID}→{CityName}**. Cela entraîne des dépendances fonctionnelles pour toutes les combinaisons possibles d'attributs sur le côté droit, qui doivent prendre la même valeur pour plusieurs uplets s'ils ont la même valeur pour les attributs sur le côté gauche.

Plus précisément, cela signifie qu'étant donné les dépendances que nous savons exister, les suivantes existent également :

* **{PersonID}→{PersonName, CityID}**
    
* **{PersonID}→{PersonName, CityName}**
    
* **{PersonID}→{CityID, CityName}**
    
* **{PersonID}→{CityID, CityName, PersonName}**
    

Cela se produit en raison de la propriété d'union des dépendances fonctionnelles, où si nous avons des dépendances **X→Y** et **X→Z**, alors la dépendance **X→(Y U Z)** existe également, où les lettres majuscules désignent des ensembles d'attributs.

Sans entrer plus dans les détails de ces propriétés, il convient de souligner qu'il s'agit de l'une des règles d'inférence d'Armstrong, dont l'objectif principal est d'**inférer toutes les dépendances fonctionnelles** qui existent dans une table. Plus précisément, ces règles d'inférence garantissent que, à partir d'une série de dépendances fonctionnelles initiales, **toutes** les dépendances qui existent réellement dans une table peuvent être inférées.

Grâce à cela, l'important est de savoir que les dépendances fonctionnelles peuvent avoir plusieurs attributs dans leurs ensembles. Cela conduit à son tour à une classification des dépendances basée sur le nombre d'attributs qu'elles possèdent dans chaque ensemble.

L'une des utilisations principales des dépendances fonctionnelles est de déterminer si une décomposition est valide, c'est-à-dire si toutes les dépendances fonctionnelles sont préservées.

Par exemple, dans la table originale, il existe les dépendances fonctionnelles **{PersonID}→{PersonName}** et **{PersonID}→{CityID}**, principalement, ou **{CityID}→{CityName}** car l'identifiant d'une ville détermine de manière unique le nom de la ville elle-même. Ainsi, en considérant ces dépendances comme base, nous pouvons en inférer d'autres comme **{PersonID}→{CityName}** par transitivité en utilisant **{PersonID}→{CityID}** et **{CityID}→{CityName}**.

Celles que nous avons considérées comme base sont celles générées directement par la sémantique du domaine. Cela signifie que si une ville est identifiée de manière unique par son **CityID**, alors il n'est pas logique de considérer **{PersonID}→{CityName}** comme une base, puisque nous avons les autres dépendances qui relient l'identifiant de la personne à son nom et à l'identifiant de la ville, à partir desquels nous pouvons l'inférer.

En résumé, les dépendances de base sont les plus fondamentales à partir desquelles toutes les autres peuvent être inférées. Il n'existe pas d'algorithme unique pour les trouver toutes. Il s'agit plutôt d'un processus plus ouvert que nous devons suivre en fonction de notre domaine, de nos exigences et de la sémantique des attributs.

Une fois que nous avons trouvé les dépendances de base, l'important est de s'assurer qu'elles sont préservées après la décomposition d'une table. Nous pouvons le voir dans les tables résultantes, où **{PersonID}→{PersonName}** reste dans Person, tout comme **{PersonID}→{CityID}**, avec la seule particularité que maintenant CityID dans Person est une clé étrangère, et **{CityID}→{CityName}**, qui est préservée dans la nouvelle table City après décomposition.

Ainsi, en préservant toutes les dépendances fonctionnelles de base, nous sommes assurés que la décomposition de Person en Person et City est correcte.

Enfin, les dépendances fonctionnelles peuvent avoir de nombreuses autres classifications en plus d'être de base ou non. Par exemple, dans certaines des définitions formelles des formes normales suivantes que nous verrons, nous vérifions souvent si une dépendance fonctionnelle est triviale. Il s'agit des dépendances X→Y où tous les attributs de l'ensemble Y sont présents dans l'ensemble X.

Par exemple, **{A, B} → {A}** est triviale car {A} ⊆ {A, B}, et **{A, B} → {B, A}** est également triviale car {B, A} ⊆ {A, B}. Mais **{A} → {B}** n'est **pas** triviale car {B} ⊄ {A}, ce qui signifie qu'il y a un attribut dans l'ensemble {B} qui n'est pas présent dans l'ensemble {A}.

### Formes normales

Après avoir compris ce que sont les dépendances fonctionnelles, il est important de noter qu'il existe de nombreux autres types de dépendances, telles que les dépendances multivaluées, d'union ou d'inclusion. Toutes visent également à éliminer ou à minimiser les problèmes associés à la redondance des données que nous avons vus précédemment grâce aux formes normales.

Il s'agit d'une série de niveaux de raffinement d'un schéma relationnel définis par des conditions de plus en plus strictes destinées à éliminer ou à minimiser progressivement les problèmes causés par la redondance dans un schéma. Parmi tous les niveaux, nous ne regarderons que ceux qui utilisent les dépendances fonctionnelles entre attributs comme critères pour leurs conditions. Mais il en existe d'autres que nous n'aborderons pas ici et dont les critères incluent des dépendances multivaluées ou d'union.

#### 1NF (Première Forme Normale)

Tout d'abord, nous avons la **première forme normale (1NF)**, dont la condition principale est que chaque attribut soit **atomique**. Cela signifie que les cellules de la table ne contiennent pas un nombre arbitraire de valeurs, ce que nous pouvons également appeler la non-existence de groupes répétitifs. Mais elle impose également des conditions de base telles que l'exigence d'une clé primaire dans la table afin que chaque uplet puisse être identifié de manière unique. Elle interdit les uplets en double, ainsi que les attributs avec des noms en double, ce qui signifie qu'il ne peut pas y avoir de colonnes avec des noms identiques.

Ces conditions doivent être remplies pour que toutes les tables d'un schéma de base de données soient en 1NF. Dans ce cas, nous pouvons facilement les vérifier en nous assurant que chaque cellule contient exactement une valeur, qu'il n'y a pas de doublons dans les lignes ou les colonnes, et qu'il existe une clé primaire.

Ces trois dernières conditions sont autorisées par un SGBD, ce qui signifie que lors de l'implémentation d'une table au niveau logique, nous pouvons avoir des doublons ou même ne définir aucune clé – et bien que la base de données puisse fonctionner, son schéma ne sera pas en 1NF. Ainsi, si nous trouvons une table qui ne répond pas aux conditions de la forme normale, nous pouvons appliquer certaines transformations pour la normaliser et l'amener en 1NF.

#### 2NF (Deuxième Forme Normale)

La première forme normale se concentre principalement sur l'interdiction des groupes répétitifs, ce qui élimine la possibilité de redondances au niveau de la cellule – mais n'élimine pas les redondances causées par les dépendances fonctionnelles.

Malgré l'interdiction de l'existence d'uplets en double, nous avons vu dans un exemple précédent que les informations de ville dans une table pouvaient être inutilement dupliquées dans plusieurs uplets différents parce que les personnes vivant dans cette ville étaient différentes. Cela respecte la 1NF mais présente des problèmes de redondance.

Pour traiter ces cas de redondance, nous utilisons la **deuxième forme normale (2NF)**. Elle inclut toutes les conditions de la 1NF plus une condition supplémentaire plus stricte : tous les attributs qui ne sont pas la clé primaire d'une table doivent dépendre de l'**intégralité de la clé primaire** sélectionnée pour la table – c'est-à-dire de tous ses attributs, et pas seulement d'un seul. Cela empêche la dépendance partielle par rapport à la clé primaire.

| **BikeID** | **Modèle** | **Marque** | **PaysMarque** | **PrixAchat** | **NomPropriétaire** | **EmailPropriétaire** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Roadster | SpeedX | USA | 1200 | John Doe | john@example.com |
| 2 | TrailBlazer | MountainCo | Canada | 1500 | Alice Smith | alice@example.com |
| 3 | Roadster | SpeedX | USA | 1150 | Bob Lee | bob@example.org |
| 4 | CityCruiser | UrbanRide | USA | 800 | John Doe | john@example.com |
| 5 | EcoCruiser | GreenMotion | Allemagne | 1300 | Carol Johnson | carol@example.com |

Par exemple, nous avons ici une table Bike dont la clé primaire est {BikeID}, et les dépendances fonctionnelles de base sont {BikeID}→{Modèle}, {BikeID}→{PrixAchat}, {BikeID}→{NomPropriétaire}, {BikeID}→{EmailPropriétaire} car si BikeID identifie de manière unique chaque vélo, alors les informations sur le modèle, le prix et le propriétaire dépendront directement de cet attribut.

Nous avons également les dépendances {Modèle}→{Marque}, {Modèle}→{PaysMarque}, et {EmailPropriétaire}→{NomPropriétaire}, car connaître le modèle du vélo peut déterminer de manière unique sa marque. Nous pouvons également déterminer le nom du propriétaire à partir de son e-mail, ce que nous ne pouvons pas faire à l'inverse car plusieurs personnes peuvent avoir le même nom et des adresses e-mail différentes.

Étant donné ces dépendances, puisque la clé primaire n'a qu'un seul attribut, nous voyons que tous les autres ont une dépendance sur l'intégralité de la clé primaire. Cela signifie que la clé primaire elle-même détermine de manière unique le reste des attributs de la table. Nous pouvons donc noter formellement que, pour tous les attributs A qui ne sont pas la clé primaire, il existe la dépendance fonctionnelle **{Clé Primaire}→A**.

Dans ce cas, même si certaines dépendances sont transitives, nous pouvons voir qu'en fin de compte, tous les attributs finissent par dépendre de la clé primaire. Par exemple, avec {BikeID}→{Modèle} et {Modèle}→{Marque}, nous inférons la dépendance {BikeID}→{Marque}, qui n'est pas basique.

Lorsque cette condition est remplie, la table est en 2NF, ce qui évite les redondances causées par des attributs qui ne dépendent que d'une partie de la clé primaire, et non de la clé entière.

Cela n'est peut-être pas aussi clair ici car la clé primaire de l'exemple n'a qu'un seul attribut, mais nous avons parfois des clés primaires avec plus d'attributs. Dans de tels cas, le reste des attributs de la table doit dépendre de tous les attributs de la clé primaire pour être en 2NF (en plus de remplir les conditions de la 1NF).

S'ils ne dépendent que d'une partie de la clé, il pourrait y avoir des valeurs répétées dans ces attributs. Cela causerait des problèmes de redondance car c'est l'intégralité de la clé primaire (tous ses attributs) qui peut identifier de manière unique chaque uplet.

#### 3NF (Troisième Forme Normale)

En continuant avec les formes normales, la [**3NF**](https://cse.hkust.edu.hk/~dimitris/5311/L08.pdf) est définie de manière similaire. Tout d'abord, pour qu'un schéma soit en 3NF, il doit remplir toutes les conditions de la 2NF plus une condition spécifique qui stipule qu'il ne peut pas y avoir de dépendances fonctionnelles entre attributs non-clés (non-prime).

Les attributs clés (prime) sont ceux qui appartiennent à n'importe quelle clé candidate de la table. Nous pouvons donc reformuler la condition précédente de la 3NF en disant qu'aucun attribut n'appartenant à aucune clé candidate ne peut dépendre fonctionnellement d'un autre attribut n'appartenant à aucune clé candidate.

Par exemple, dans la table Bike que nous avions précédemment, nous supposons que la seule clé candidate qui existe est **{BikeID}**, car aucun autre ensemble d'attributs ne peut identifier de manière unique les uplets de la table. Nous pouvons le vérifier en regardant la sémantique des attributs. Ainsi, en voyant qu'il existe des dépendances fonctionnelles comme **{Modèle}→{PaysMarque}** entre des attributs non-clés, c'est-à-dire qu'ils n'appartiennent à aucune clé candidate, nous concluons que la table n'est pas en 3NF, et nous devrons la normaliser.

| **BikeID** | **Modèle (FK)** | **PrixAchat** | **EmailPropriétaire (FK)** |
| --- | --- | --- | --- |
| 1 | Roadster | 1200 | john@example.com |
| 2 | TrailBlazer | 1500 | alice@example.com |
| 3 | Roadster | 1150 | bob@example.org |
| 4 | CityCruiser | 800 | john@example.com |
| 5 | EcoCruiser | 1300 | carol@example.com |

| **Modèle** | **Marque** | **PaysMarque** |
| --- | --- | --- |
| Roadster | SpeedX | USA |
| TrailBlazer | MountainCo | Canada |
| Roadster | SpeedX | USA |
| CityCruiser | UrbanRide | USA |
| EcoCruiser | GreenMotion | Allemagne |

| **EmailPropriétaire** | **NomPropriétaire** |
| --- | --- |
| john@example.com | John Doe |
| alice@example.com | Alice Smith |
| bob@example.org | Bob Lee |
| john@example.com | John Doe |
| carol@example.com | Carol Johnson |

Pour normaliser la table, nous devrons appliquer un algorithme aux tables pour convertir le schéma en 3NF, en veillant à ce qu'il n'y ait pas de dépendances fonctionnelles entre attributs non-clés.

Pour comprendre cet algorithme, nous allons partir de la table Bike originale que nous avions auparavant. Nous nous concentrerons sur les dépendances fonctionnelles entre attributs clés qui brisent la 3NF, qui ne sont pas dérivées de manière transitive de dépendances plus simples, et dont l'ensemble d'attributs sur le côté gauche ne forme pas une superclé.

Par exemple, si nous avons {A}→{B}, {B}→{C}, et {A}→{C}, nous ne considérons pas {A}→{C} car elle peut être dérivée de manière transitive des deux autres. Plus précisément, les dépendances problématiques dans notre exemple, qui ne sont pas dérivées de manière transitive et dont le côté gauche n'est pas une superclé, sont {Modèle}→{Marque}, {Modèle}→{PaysMarque}, et {EmailPropriétaire}→{NomPropriétaire}, qui sont les dépendances fonctionnelles de base.

Maintenant, nous devons décomposer la table guidés par ces dépendances fonctionnelles. Mais comme vous pouvez le voir, nous pouvons appliquer la propriété d'union des dépendances fonctionnelles pour savoir que la **dépendance fonctionnelle** **{Modèle}→{Marque, PaysMarque}** existe également. Nous l'avons dérivée des précédentes problématiques pour simplifier l'application de l'algorithme.

En résumé, pour faciliter l'application de l'algorithme, chaque fois que nous voyons plusieurs dépendances fonctionnelles avec le même déterminant (ensemble d'attributs sur le côté gauche), il est utile d'appliquer la propriété d'union mentionnée précédemment pour les simplifier en une seule.

Nous avons donc maintenant que les dépendances fonctionnelles problématiques sont **{Modèle}→{Marque, PaysMarque}** et **{EmailPropriétaire}→{NomPropriétaire}**. Nous pouvons créer une table spécifique pour chacune d'elles où son schéma est composé de tous les attributs de la dépendance – c'est-à-dire tous les attributs des deux côtés. Nous pouvons noter cela formellement comme l'union des deux ensembles d'attributs.

Comme vous pouvez le deviner, en faisant cela, les clés primaires dans les nouvelles tables seront les attributs des déterminants de ces dépendances (qui dans ce cas sont **{Modèle}** et **{EmailPropriétaire}**, respectivement).

Nous devons également supprimer ces attributs que nous avons séparés dans des tables supplémentaires de la table Bike originale, en ne laissant que les attributs des déterminants de ces dépendances et en les convertissant en clés étrangères pour référencer les clés primaires correspondantes des nouvelles tables. Par convention, les attributs qui composent la clé primaire d'une table sont généralement placés en premier à gauche, comme **Modèle** et **EmailPropriétaire** ici.

Après ce processus, nous pouvons voir que toutes les dépendances fonctionnelles qui étaient auparavant problématiques sont maintenant dans de nouvelles tables où leurs déterminants sont désormais des clés primaires. Cela évite de violer la condition imposée par la 3NF.

Notez qu'après avoir appliqué cet algorithme, nous n'avons pas besoin de l'appliquer de manière récursive aux tables générées par la décomposition, car il est garanti que le schéma résultant est déjà en 3NF après avoir appliqué ce processus. En résumé, en appliquant cette forme normale à notre schéma à l'aide de l'algorithme décrit, connu sous le nom d'[**algorithme de synthèse relationnelle**](https://www.cs.emory.edu/~cheung/Courses/377/Syllabus/9-NormalForms/FD-preserve-howto.html), nous parvenons à éviter ou à minimiser l'apparition de redondances causées par des dépendances fonctionnelles transitives.

### BCNF (Forme Normale de Boyce-Codd)

Les trois formes normales précédentes sont les plus basiques que nous puissions appliquer à un schéma pour éliminer la plupart des problèmes causés par les redondances. Mais il existe une autre forme normale en plus de la 3NF qui est plus restrictive et assure un meilleur résultat à cet égard, c'est la **BCNF**.

Comme nous l'avons vu, les formes normales deviennent de plus en plus restrictives dans les conditions qu'elles appliquent. Dans ce cas, [**BCNF** signifie **Boyce-Codd Normal Form**](https://cs.stackexchange.com/questions/116901/database-theory-does-the-dependency-preservation-and-lossless-join-properties), et elle se caractérise par le fait de n'autoriser que les dépendances fonctionnelles **X→Y** dans les tables où il est vrai que soit la dépendance est **triviale**, soit X est une **superclé** de la table.

Si ces conditions sont remplies, nous pouvons démontrer formellement que toutes les conditions de la 3NF doivent également être automatiquement remplies (et donc aussi la 2NF et la 1NF). Nous n'effectuerons pas cette démonstration ici, car l'important est de savoir comment normaliser un schéma pour qu'il adhère à la BCNF. Ainsi, si nous partons d'un schéma comme celui que nous avions initialement pour la table Bike non normalisée, nous pouvons appliquer un algorithme spécifique pour le transformer en BCNF.

| **BikeID** | **Modèle** | **Marque** | **PaysMarque** | **PrixAchat** | **NomPropriétaire** | **EmailPropriétaire** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Roadster | SpeedX | USA | 1200 | John Doe | john@example.com |
| 2 | TrailBlazer | MountainCo | Canada | 1500 | Alice Smith | alice@example.com |
| 3 | Roadster | SpeedX | USA | 1150 | Bob Lee | bob@example.org |
| 4 | CityCruiser | UrbanRide | USA | 800 | John Doe | john@example.com |
| 5 | EcoCruiser | GreenMotion | Allemagne | 1300 | Carol Johnson | carol@example.com |

L'algorithme pour convertir en BCNF est très similaire à celui que nous avons examiné pour la 3NF. La différence est qu'ici, la décomposition se fait en plus d'étapes.

Tout d'abord, nous devons identifier les dépendances fonctionnelles qui empêchent le respect de la BCNF, qui sont exactement {Modèle}→{Marque}, {Modèle}→{PaysMarque}, et {EmailPropriétaire}→{NomPropriétaire}. Nous choisissons celles-ci car, comme vous pouvez le voir, {Modèle} ne peut pas être une superclé, pas plus que {EmailPropriétaire} seul. Mais dans d'autres dépendances fonctionnelles comme {BikeID}→{PrixAchat}, nous voyons que {BikeID} est bien une superclé, car c'est en fait la clé primaire de la table. Nous ne les incluons donc pas lors de l'application de l'algorithme.

Gardez également à l'esprit qu'une dépendance fonctionnelle X→Y peut être triviale et répondre à la définition de la BCNF même si X n'est pas une superclé, ce qui signifie que l'ensemble d'attributs Y est un sous-ensemble de l'ensemble d'attributs X.

Maintenant, pour simplifier l'application de l'algorithme, nous pouvons nous concentrer sur le déterminant des dépendances qui brisent la forme normale – c'est-à-dire sur l'ensemble d'attributs sur le côté gauche, en cherchant plusieurs qui ont le même déterminant. S'il y en a plusieurs avec le même déterminant, comme c'est le cas pour celles qui ont **{Modèle}** sur leur côté gauche, alors nous pouvons utiliser la propriété d'union des règles d'inférence d'Armstrong pour les simplifier toutes en une seule comme **{Modèle}→{Marque, PaysMarque}**. Ici, sur le côté droit, nous avons rassemblé tous les attributs des côtés droits des dépendances que nous avions.

De cette façon, nous réduisons le nombre de dépendances à prendre en compte dans l'algorithme, ce qui simplifie son exécution. C'est le cas puisque cette étape n'est pas obligatoire dans cet algorithme (ni dans la conversion en 3NF), car elle ne fait pas partie de la définition de l'algorithme lui-même, mais est plutôt quelque chose de supplémentaire que nous faisons pour le simplifier sans affecter sa justesse.

Ensuite, nous nous retrouvons avec les dépendances **{Modèle}→{Marque, PaysMarque}** et **{EmailPropriétaire}→{NomPropriétaire}**, qui guident la décomposition que nous allons effectuer sur la table, de manière similaire à l'algorithme de conversion en 3NF. Mais la différence principale est que maintenant nous sélectionnons les dépendances une par une et effectuons une décomposition pour chacune, et non toutes à la fois. Chaque fois que la table est décomposée, les dépendances et les clés changent, nous devons donc le faire une par une pour garantir que la recombinaison des tables décomposées reste sans perte.

Bien que nous n'entrerons pas dans les détails de la raison pour laquelle cela se produit, l'important est de se rappeler que nous utilisons cette méthode car cet algorithme ne garantit pas la préservation de toutes les dépendances fonctionnelles en raison des conditions qui définissent cette forme normale. Ces conditions sont suffisamment restrictives pour que, dans certaines situations, certaines dépendances puissent ne pas être préservées après la décomposition.

En sélectionnant l'une des dépendances comme **{Modèle}→{Marque, PaysMarque}** (nous pouvons en fait choisir n'importe laquelle), nous décomposons la table Bike guidés par cette dépendance fonctionnelle. Nous supprimons tous les attributs du côté droit de la dépendance de la table originale et faisons des attributs du déterminant (côté gauche) des clés étrangères. Ces clés étrangères pointent vers les attributs correspondants d'une nouvelle table où nous stockons tous les attributs impliqués dans la dépendance (c'est-à-dire des deux côtés).

| **BikeID** | **Modèle (FK)** | **PrixAchat** | **NomPropriétaire** | **EmailPropriétaire** |
| --- | --- | --- | --- | --- |
| 1 | Roadster | 1200 | John Doe | john@example.com |
| 2 | TrailBlazer | 1500 | Alice Smith | alice@example.com |
| 3 | Roadster | 1150 | Bob Lee | bob@example.org |
| 4 | CityCruiser | 800 | John Doe | john@example.com |
| 5 | EcoCruiser | 1300 | Carol Johnson | carol@example.com |

| **Modèle** | **Marque** | **PaysMarque** |
| --- | --- | --- |
| Roadster | SpeedX | USA |
| TrailBlazer | MountainCo | Canada |
| Roadster | SpeedX | USA |
| CityCruiser | UrbanRide | USA |
| EcoCruiser | GreenMotion | Allemagne |

Formellement, si notre table originale est l'ensemble d'attributs **R**, alors nous gardons **R-{Marque, PaysMarque}**, convertissons **{Modèle}** en la clé étrangère **{Modèle (FK)}** référençant l'ensemble d'attributs {Modèle} de la nouvelle table générée par la décomposition, dont les attributs sont donnés par **{Modèle}U{Marque, PaysMarque}**, et dont la clé primaire est l'ensemble **{Modèle}** qui était auparavant dans le **déterminant** de la dépendance.

Maintenant, nous répétons ce processus de manière récursive sur les tables résultantes, car cette décomposition a résolu le problème causé par la dépendance {Modèle}→{Marque, PaysMarque}. Mais nous avons toujours la dépendance {EmailPropriétaire}→{NomPropriétaire} dans la table Bike. Nous appliquons donc une autre étape de décomposition guidée par la seule dépendance restante qui viole les conditions de la BCNF.

En faisant cela, nous supprimons l'ensemble d'attributs {NomPropriétaire} de la table Bike et convertissons {EmailPropriétaire} en une clé étrangère qui référence le même ensemble {EmailPropriétaire} mais de la nouvelle table générée par la décomposition. Dans ce cas, elle est formée par les attributs **{EmailPropriétaire}U{NomPropriétaire}={EmailPropriétaire, NomPropriétaire}**.

| **BikeID** | **Modèle (FK)** | **PrixAchat** | **EmailPropriétaire (FK)** |
| --- | --- | --- | --- |
| 1 | Roadster | 1200 | john@example.com |
| 2 | TrailBlazer | 1500 | alice@example.com |
| 3 | Roadster | 1150 | bob@example.org |
| 4 | CityCruiser | 800 | john@example.com |
| 5 | EcoCruiser | 1300 | carol@example.com |

| **Modèle** | **Marque** | **PaysMarque** |
| --- | --- | --- |
| Roadster | SpeedX | USA |
| TrailBlazer | MountainCo | Canada |
| Roadster | SpeedX | USA |
| CityCruiser | UrbanRide | USA |
| EcoCruiser | GreenMotion | Allemagne |

| **EmailPropriétaire** | **NomPropriétaire** |
| --- | --- |
| john@example.com | John Doe |
| alice@example.com | Alice Smith |
| bob@example.org | Bob Lee |
| john@example.com | John Doe |
| carol@example.com | Carol Johnson |

Comme vous pouvez le voir, après ces étapes, le schéma ne présente aucune dépendance fonctionnelle **X→Y** où X n'est pas une superclé ou la dépendance elle-même est triviale. En effet, lors de la décomposition en tables, nous définissons leurs clés primaires comme les déterminants des dépendances qui ne respectaient pas initialement la forme normale.

Ainsi, après avoir effectué ces étapes pour toutes les dépendances qui empêchent le schéma d'adhérer à la BCNF, nous aboutissons à un schéma normalisé qui respecte la BCNF. Au cours du processus, il est possible que certaines des tables générées présentent encore des dépendances fonctionnelles violant la BCNF, c'est pourquoi ces étapes sont appliquées de manière récursive. Cela signifie que la décomposition ne se fait pas seulement à partir de la table originale, mais qu'il peut également être nécessaire de décomposer une table générée par les étapes précédentes, en particulier dans les schémas plus complexes.

Dans l'exemple que nous avons, le schéma final qui répond aux conditions de la BCNF est exactement le même que celui que nous avons obtenu lors de la transformation en 3NF. Mais c'est une coïncidence – dans la plupart des cas pratiques, les schémas ont tendance à être plus complexes, et après les avoir convertis en 3NF, ils peuvent ne pas respecter la BCNF, ou il peut même être impossible de les convertir en BCNF. C'est-à-dire que la conversion d'un schéma en 3NF est toujours garantie d'être possible, alors qu'il n'y a pas de telle garantie pour la BCNF.

En résumé, la BCNF est plus restrictive que la 3NF, ce qui évite les redondances causées par des dépendances fonctionnelles où un ensemble d'attributs qui n'identifient pas de manière unique les uplets d'une table déterminent les valeurs d'un autre ensemble d'attributs. Cela rend les informations des attributs déterminants redondantes, de la même manière que ce qui se passe en 3NF avec les dépendances transitives.

De plus, étant plus restrictive, elle peut ne pas être réalisable si une table possède plusieurs superclés qui se chevauchent, car l'application de l'**algorithme de décomposition BCNF** briserait les dépendances fonctionnelles entre les attributs de différentes superclés. Ainsi, en assouplissant les conditions de la BCNF, on obtient la 3NF, qui gère correctement les situations où des superclés se chevauchent, c'est-à-dire qu'elles partagent un attribut.

### Autres formes normales

Outre les formes normales basées sur les dépendances fonctionnelles, que nous venons de voir, il en existe d'autres qui éliminent les redondances causées par différents types de relations entre attributs ou caractéristiques.

Par exemple, la **4NF** traite des **dépendances multivaluées**, la 5NF des dépendances de jointure, la **6NF** représente le niveau le plus élevé de normalisation d'un schéma relationnel, et la **DKNF (Domain–Key Normal Form)** impose également la condition que toutes les contraintes du schéma doivent résulter uniquement des définitions de domaine et de clé, ce qui signifie qu'elle n'autorise que les contraintes de domaine et de clé.

### Quand vérifier la conformité à chaque forme normale ?

Enfin, nous avons vu que chaque forme normale établit une série de caractéristiques qu'un **schéma de base de données** doit suivre et les problèmes qu'elle vise à résoudre.

D'un point de vue pratique, les formes normales les plus importantes que nous devons assurer pour presque tout schéma sont la **1NF** et la **2NF**. Dans le cas de la 1NF, la plupart des SGBD la garantissent automatiquement – mais nous devons concevoir le modèle conceptuel de manière à éviter l'apparition de groupes répétitifs qui ne répondent pas aux conditions de la 1NF. D'un autre côté, la 2NF est essentielle pour identifier les uplets dans les tables, nous devrions donc nous assurer qu'elle est respectée dans une base de données de projet réel.

Au-delà de celles-ci, si nous travaillons avec un système qui effectue des requêtes analytiques comme dans l'**OLTP**, le schéma de la base de données devrait également répondre aux conditions de la 3NF, en particulier lorsque le schéma doit gérer des requêtes ou subir des mises à jour fréquemment. Cela aide à résoudre ces requêtes et mises à jour aussi efficacement que possible.

Au-delà de la 3NF, nous voudrons respecter la BCNF lorsque les règles métier sont très complexes. C'est-à-dire que lorsque les données doivent répondre à des contraintes complexes, nous pouvons aider à minimiser l'impact des problèmes de redondance grâce aux conditions de la BCNF, car elles sont plus restrictives que celles de la 3NF. Ensuite, si notre schéma autorise des **attributs multivalués** ou des associations de **degré** supérieur à 2, il peut être utile de vérifier d'autres types de formes normales comme la 4NF, la 5NF, etc.

## Chapitre 8 : Langages de requête

À ce stade, vous avez découvert tous les éléments avec lesquels nous pouvons organiser ou structurer les données stockées dans les bases de données relationnelles à l'aide du modèle relationnel. Mais en pratique, nous ne voulons pas seulement stocker des données, car nous pourrions le faire avec de simples fichiers. Nous avons également besoin d'outils pour manipuler et interroger ces données. Cela signifie que nous devons utiliser un langage de requête.

En termes simples, les **langages de requête** sont conçus pour manipuler et interroger (ou accéder) aux données stockées dans une base de données à travers un ensemble d'opérations. L'interrogation est l'opération la plus fondamentale de toutes, car si nous réfléchissons au fonctionnement de certaines des autres opérations (comme la mise à jour ou la suppression de données, par exemple), nous devons être capables de sélectionner ou d'interroger les données afin d'effectuer toute opération sur elles. Ainsi, fondamentalement, presque toute modification commence par l'identification préalable des enregistrements qui seront affectés par l'opération.

Les langages de requête que nous apprendrons ici sont **relationnels**, ce qui signifie qu'ils sont créés pour manipuler et interroger des données dans des bases de données relationnelles. Fondamentalement, la plupart d'entre eux basent la logique des opérations sur des manipulations de tables qui aboutissent à une autre table. Ensuite, nous pouvons continuer à appliquer des opérations à cette table résultante. Ainsi, lorsque nous opérons sur une base de données relationnelle, nous transformons des tables en d'autres tables jusqu'à atteindre une table contenant les données qui nous intéressent.

### Langages formels vs pratiques

Il existe certains langages de requête connus sous le nom de langages formels, qui consistent en des définitions théoriques où les opérateurs ou les transformations pouvant être appliqués aux tables sont formellement définis. Cela aide également à optimiser considérablement les opérations sur celles-ci, car ces outils formels nous permettent de vérifier les équivalences entre les opérations ou les requêtes, nous permettant de choisir celle ayant le coût de calcul le plus bas parmi plusieurs équivalentes.

D'un autre côté, pour appliquer cela à une base de données, il existe des langages de requête pratiques comme [**SQL**](https://www.freecodecamp.org/news/an-animated-introduction-to-sql-learn-to-query-relational-databases/), qui sont des implémentations de langages de requête formels adaptés pour être utilisés sur des systèmes réels.

Bien que nous les appelions langages, il est important de ne pas les confondre avec des langages à usage général. Les langages de requête, comme leur nom l'indique, sont dédiés à la manipulation et à l'interrogation de données, et non à l'exécution de tout type de calcul. Voici des exemples de langages de requête formels :

#### Algèbre relationnelle

Il s'agit d'un langage impératif formel, ce qui signifie que lorsque nous programmons avec lui, nous devons réfléchir à la manière d'obtenir le résultat souhaité. En d'autres termes, nous définissons une séquence d'opérations à l'aide des opérateurs du langage qui transforment progressivement les tables jusqu'à atteindre une ou plusieurs tables finales contenant les données dont nous avons besoin.

Cette idée de séquence d'opérations est très similaire à la façon dont nous planifions et exécutons réellement une requête dans un langage de requête pratique comme SQL. Ceci, ajouté à la similitude des opérateurs formels avec les instructions proposées par ces langages pratiques, aide l'utilisateur final à optimiser la requête, à vérifier formellement sa justesse ou à démontrer son équivalence avec une autre requête nécessitant moins de ressources de calcul, entre autres utilisations.

* **Exemple :** Si nous voulons obtenir tous les âges d'une table Person qui sont supérieurs à 50, nous pouvons appliquer les opérateurs de l'algèbre relationnelle **π Age ( σ (Age > 50) (Person) )** que nous verrons plus tard. Tout d'abord, nous filtrons tous les uplets qui remplissent la condition d'avoir un âge > 50 à l'aide de l'opérateur correspondant, puis nous appliquons un autre opérateur à la table résultante avec ces uplets pour ne conserver que les âges de ces uplets.

#### Calcul relationnel

Contrairement à l'algèbre relationnelle, le calcul relationnel est un langage déclaratif. Cela signifie que nous programmons en pensant aux propriétés que le résultat doit avoir, et non aux opérateurs à appliquer à certaines tables pour y parvenir. En d'autres termes, nous ne définissons pas quelque chose de similaire à un plan d'exécution ou à une séquence d'opérateurs pour obtenir le résultat. Au lieu de cela, nous déclarons simplement les propriétés qu'il doit avoir pour répondre à nos besoins, et le système lui-même trouve un plan d'exécution qui produit exactement ce que nous recherchons.

Il existe plusieurs façons de poser une requête ou une modification sur les données. L'une est basée sur le **Calcul Relationnel de n-uplets (TRC - Tuple Relational Calculus)**, où nous déclarons les conditions que les attributs des uplets doivent remplir pour être inclus dans notre résultat. L'autre est le **Calcul Relationnel de Domaines (DRC - Domain Relational Calculus)**, qui consiste à utiliser des variables sur les domaines des attributs pour fixer des conditions sur ceux-ci en utilisant une méthodologie similaire à la logique du premier ordre.

* **Exemple :** En suivant le même exemple que précédemment, en **TRC**, nous aurions quelque chose comme **{ t.Age | Person(t) ∧ t.Age > 50 }**, où nous déclarons que les uplets **t** que nous voulons obtenir doivent appartenir à la table Person et avoir une valeur supérieure à 50 dans l'attribut Age. Pendant ce temps, en **DRC**, nous aurions **{ ⟨a⟩ | ∃id ( Person(id, a) ∧ a > 50) }**, où nous supposons que la table ne stocke qu'un attribut ID et un attribut Age, car si plus d'attributs étaient stockés, nous devrions utiliser plus de variables de domaine. En résumé, ici les conditions sont imposées sur les variables de domaine, qui représentent les valeurs que les uplets prennent dans leurs attributs respectifs.

Enfin, quel que soit le langage formel utilisé, les deux ont la même capacité expressive, ce qui peut être démontré formellement, car les deux sont construits à l'aide de la logique du premier ordre.

## Chapitre 9 : SQL (Structured Query Language)

En plus des langages formels, il existe des implémentations comme le Structured Query Language (SQL) qui sont basées sur les opérations de ces langages formels. Elles nous permettent de manipuler et d'interroger des données via des systèmes de gestion de bases de données relationnelles (SGBD).

Plus précisément, SQL est un langage utilisé commercialement avec diverses normes, auxquelles diverses fonctionnalités ont été ajoutées au fil du temps. La plupart des systèmes ont des versions installées plus récentes que SQL-92. Mais cette version inclut déjà toutes les fonctions nécessaires pour effectuer la grande majorité des opérations nécessaires sur une base de données, c'est donc la norme sur laquelle nous nous concentrerons ici. Et bien que nous visions un SQL portable, plusieurs exemples utilisent des fonctionnalités introduites après SQL-92 ou des extensions spécifiques à PostgreSQL (comme `BOOLEAN`, `XML/JSON`, `UUID`, et les méta-commandes psql).

SQL est un langage déclaratif, où nous définissons les données que nous voulons obtenir, et non la séquence exacte d'opérations pour les obtenir. Le SGBD fait cela en interne en traduisant les instructions que nous écrivons en opérations d'algèbre relationnelle, qui transforment les tables via un plan d'exécution jusqu'à atteindre une table finale avec les résultats que nous avons demandés.

Avant de poursuivre avec les éléments qui composent le langage SQL lui-même, nous devrions distinguer ces éléments ou instructions en fonction de leur objectif ou de leur domaine d'application.

D'une part, nous avons les instructions qui forment le Data Definition Language (DDL - Langage de Définition de Données), qui est un ensemble d'instructions dédiées à la gestion des tables de la base de données (telles que leur création, suppression, modification, etc.).

Ensuite, nous avons le Data Control Language (DCL - Langage de Contrôle de Données), qui est un autre ensemble d'instructions de langage dédié au contrôle des autorisations des utilisateurs dans la base de données, gérant qui peut lire ou modifier les tables.

D'autre part, nous avons le Data Manipulation Language (DML - Langage de Manipulation de Données). Ses instructions sont orientées vers la gestion des données contenues dans les tables, telles que l'insertion, la suppression, la transformation ou l'interrogation.

En dehors de ces ensembles d'instructions, nous pouvons également considérer le [**Transaction Control Language (TCL)**](https://www.geeksforgeeks.org/sql/tcl-full-form/), qui sont une série d'instructions nous permettant de gérer les transactions qui se produisent dans la base de données. Ici, nous nous concentrerons uniquement sur les trois premiers ensembles, qui contiennent les instructions les plus fondamentales.

### DDL

Pour commencer avec SQL, la chose la plus basique que nous puissions faire est de créer, modifier et supprimer des tables dans la base de données. Cela signifie que nous utilisons des instructions qui nous permettent de définir notre conception logique dans le SGBD.

Ici, nous utiliserons **PostgreSQL** comme SGBD, bien que ces exemples puissent être appliqués à tout SGBD supportant la norme **SQL-92**, sur laquelle nous allons nous concentrer.

![Diagramme entité-relation où Rental est une entité faible qui relie Person et Bike avec des données de location. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752248008262/339c85d9-14a2-4d63-9453-c0f1a36e90f0.png align="center")

Pour ces exemples, supposons un domaine où des personnes louent des vélos. Nous avons une entité faible appelée **Rental** qui modélise le moment où une personne a loué un certain vélo, et l'attribut **Duration** représente le nombre de jours de location.

Comme nous l'avons vu dans les exemples précédents, la clé primaire de Rental est composée de la date de location et des clés étrangères qui identifient la personne ayant loué un certain vélo. Cela rend Rental faible en identification car les deux clés étrangères sont nécessaires pour identifier de manière unique les uplets de cette table.

De plus, dans notre domaine, nous interdisons à une personne de louer un vélo lorsqu'il est déjà loué par quelqu'un d'autre. Cela signifie que bien que tout le monde puisse louer autant de vélos qu'il le souhaite, on ne peut pas en louer un qui est déjà utilisé par une autre personne ou par soi-même.

![Diagramme de schéma relationnel où Rental référence Bike et Person via des clés étrangères. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752248300505/daa2d932-d838-4ba4-8f4b-1abaa5f31f98.png align="center")

Lors de la traduction au niveau logique, nous soulignons simplement les attributs qui sont des clés et ajoutons les attributs de clé étrangère dans Rental, car ils ne sont pas représentés au niveau conceptuel. Ceux-ci sont soulignés car l'entité Rental est faible en identification, comme nous venons d'en discuter.

Ainsi, si nous voulons implémenter cette conception logique dans un SGBD comme PostgreSQL, nous devons d'abord l'**installer** et le **configurer** sur une machine. Ensuite, une fois ouvert dans un terminal, nous pouvons y naviguer avec différentes commandes (gardez à l'esprit que, à l'exception de `SQL CODE;`, ce sont des méta-commandes psql (raccourcis client), pas du SQL) :

* `\?` Affiche l'aide sur les commandes du SGBD.
    
* `\! [commande]` Exécute une commande du terminal du système d'exploitation.
    
* `\h [commande]` Affiche l'aide sur la syntaxe SQL, c'est-à-dire ses instructions comme `\h CREATE TABLE`.
    
* `\q` Ferme le SGBD, ce qui peut également être fait avec `exit`.
    
* `\l` ou `\list` Liste toutes les bases de données disponibles.
    
* `\c <nomBaseDeDonnees>` ou `\connect <nomBaseDeDonnees>` Connecte à la base de données du nom donné.
    
* `\conninfo` Affiche des informations sur la connexion actuelle à la base de données (hôte, port, utilisateur, base de données).
    
* `\dn` Liste tous les schémas, qui sont des regroupements d'éléments tels que des tables, des vues, des types, etc.
    
* `\dt` Affiche les tables de la base de données à laquelle nous sommes connectés.
    
* `\dv` Similaire à la commande précédente, celle-ci affiche les vues.
    
* `\di` Liste les index.
    
* `\df` Liste les fonctions.
    
* `\d[+] objet` Décrit l'objet dont nous fournissons le nom en argument d'entrée (table, vue, fonction, etc.). Avec `+`, cela inclut des détails supplémentaires.
    
* `SQL CODE;` Dans le terminal, nous pouvons exécuter du code SQL, se terminant généralement par un point-virgule.
    
* `\timing` Utilisé pour activer/désactiver la mesure du temps d'exécution des requêtes.
    
* `\copy table TO 'fichier.csv' CSV HEADER;` Exporte `table` vers un fichier CSV.
    
* `\copy table FROM 'fichier.csv' CSV HEADER;` Importe des données d'un fichier CSV dans une table sans la vider au préalable.
    
* `\i chemin/fichier.sql` Exécute un script SQL enregistré dans un fichier avec une extension .sql pour éviter d'avoir à copier et coller du code SQL fastidieux dans le terminal.
    

Lorsque vous utilisez un SGBD, vous devriez consulter sa documentation pour voir s'il est sensible à la casse (case sensitive) ou non. Dans ce cas, [PostgreSQL](https://stackoverflow.com/questions/21796446/postgres-case-sensitivity) convertit les identifiants non cités en minuscules. Les identifiants cités (entre guillemets) préservent la casse et doivent correspondre exactement. Les mots-clés SQL ne sont pas sensibles à la casse.

#### CREATE

Une fois entré dans le SGBD, la première chose que nous pouvons faire est de créer des éléments à l'aide de l'instruction CREATE. Il existe de nombreux éléments que nous pouvons créer, mais le plus important pour l'instant est DATABASE, qui nous permet de créer une nouvelle base de données.

```pgsql
CREATE DATABASE sampledb;
```

Si nous entrons cette commande directement dans le terminal, nous créerons une base de données vide à laquelle nous pourrons nous connecter à l'aide des commandes PostgreSQL précédentes. Une fois dans la base de données, nous pouvons créer les tables de notre conception logique avec ce qui suit :

```pgsql
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE,
    Email VARCHAR(255)
);
CREATE TABLE Bike (
    BikeID INT,
    Model VARCHAR(255),
    Weight DOUBLE PRECISION
);
CREATE TABLE Rental (
    PersonFK INT,
    BikeFK INT,
    RentalDate DATE,
    Duration INT,
    Price DOUBLE PRECISION
); --Important, n'oubliez pas le ; après chaque instruction--
```

Comme vous pouvez le voir, lors de la création de tables, vous devez spécifier le schéma de chacune. Ne confondez pas cela avec ce que PostgreSQL appelle un schéma au niveau du SGBD. Dans PostgreSQL, un **schéma** est un **espace de noms (namespace)** au sein de la base de données qui regroupe et isole des éléments tels que des **tables**, des vues, des fonctions, etc. Cela facilite l'organisation, la gestion et le contrôle des autorisations, et évite les conflits de noms.

Ici, le **schéma de table** se réfère aux **attributs** qui la définissent, c'est pourquoi nous déclarons leurs noms ainsi que leurs types de données, notamment :

| **Type de données** | **Catégorie** | **Description** |
| --- | --- | --- |
| `BIT` | Chaîne de bits | Chaîne de bits de taille fixe (par exemple, `BIT(1)` stocke un seul 0 ou 1). |
| `SMALLINT` | Numérique exact | Entier généralement de –32 768 à 32 767 (2 octets). |
| `INTEGER` / `INT` | Numérique exact | Entier généralement de –2 147 483 648 à 2 147 483 647 (4 octets). |
| `BIGINT` | Numérique exact | Entier généralement de –9 223 372 036 854 775 808 à 9 223 372 036 854 775 807 (8 octets). |
| `DECIMAL(p, s)` | Numérique exact | Nombre à virgule fixe avec précision `p` et échelle `s` (par exemple, monnaie). |
| `NUMERIC(p, s)` | Numérique exact | Synonyme de `DECIMAL`, même comportement à virgule fixe. |
| `FLOAT(p)` | Numérique approximatif | Virgule flottante avec une précision d'au moins `p` bits. |
| `REAL` | Numérique approximatif | Virgule flottante simple précision (généralement 24 bits). |
| `DOUBLE PRECISION` | Numérique approximatif | Virgule flottante double précision (généralement 53 bits). |
| `CHAR(n)` | Chaîne de caractères | Texte de longueur fixe d'exactement `n` caractères (complété par des espaces si plus court). |
| `VARCHAR(n)` | Chaîne de caractères | Texte de longueur variable jusqu'à `n` caractères (pas de complément). |
| `CLOB` | Chaîne de caractères | Character Large Object pour du texte très long (par exemple, des articles). |
| `BINARY(n)` | Chaîne binaire | Données binaires de longueur fixe d'exactement `n` octets. |
| `VARBINARY(n)` | Chaîne binaire | Données binaires de longueur variable. |
| `BLOB` | Chaîne binaire | Binary Large Object pour de grandes données binaires (par exemple, des images). |
| `DATE` | Date/Heure | Date du calendrier au format `AAAA-MM-JJ`. |
| `TIME(p)` | Date/Heure | Heure de la journée `HH:MM:SS[.fraction]` avec une précision de `p` secondes fractionnaires. |
| `TIMESTAMP(p)` | Date/Heure | Date et heure combinées avec une précision de secondes fractionnaires `p`. |
| `INTERVAL` | Date/Heure | Période de temps (par exemple, `INTERVAL '1-2' YEAR TO MONTH`). |
| `BOOLEAN` | Booléen | Valeur logique `TRUE`, `FALSE` ou `UNKNOWN` (NULL). |
| `XML` | Autre standard | Stocke un document ou un fragment XML. |
| `JSON` | Autre standard | Stocke du texte au format JSON pour des données semi-structurées. |
| `UUID` | Autre standard | Identifiant unique universel de 128 bits (par exemple, `550e8400-e29b-41d4-a716-446655440000`). |

Dans cette liste, nous pouvons en voir certains comme **BLOB** qui, à première vue, permettent de stocker une quantité arbitraire de données dans une seule cellule, car le BLOB peut être aussi grand que nous le souhaitons. Cela pourrait sembler poser un problème de groupe répétitif. Mais lorsqu'une colonne stocke des données BLOB, elle ne stocke pas plusieurs BLOB dans la même cellule, mais un seul. Cela rend le SGBD responsable de la gestion efficace du stockage sur disque de ce type de données.

En d'autres termes, nous pouvons voir cela comme si le BLOB lui-même n'était pas stocké dans une cellule de table, mais plutôt qu'un pointeur mémoire était stocké pointant vers une autre zone mémoire où l'intégralité du BLOB est stockée (bien que la technique exacte utilisée dépende fortement du SGBD).

De plus, si nous regardons d'autres types de données comme **VARCHAR** pour stocker du texte, dans PostgreSQL, vous pouvez utiliser VARCHAR avec ou sans longueur (ou TEXT). En SQL standard, VARCHAR(n) nécessite une longueur.

Outre la création de bases de données et de tables, nous pourrions vouloir créer un type de données personnalisé comme **ageDataType** ou **colorDataType**, ce que nous pouvons faire en utilisant **CREATE DOMAIN**.

```pgsql
CREATE DOMAIN ageDataType AS INTEGER CHECK (VALUE >= 0 AND VALUE <= 150);
CREATE DOMAIN colorDataType AS VARCHAR(8) CHECK (VALUE IN ('red', 'green', 'BlUe'));
```

Ici, nous venons de créer de nouveaux types de données appelés ageDataType et colorDataType, où le premier est utilisé pour représenter des âges et l'autre des couleurs. Nous pourrions le faire en imposant des contraintes sur les valeurs que les colonnes peuvent prendre, plutôt qu'en définissant un nouveau type de données, ou plutôt un domaine. Mais s'il y a de nombreux attributs avec les mêmes contraintes sur leur domaine, c'est-à-dire qu'ils ont le même domaine comme la couleur ou l'âge, alors il est logique d'en définir un personnalisé.

Nous faisons cela principalement à l'aide de l'instruction CHECK qui, comme nous le verrons, est utilisée pour définir des contraintes (dans ce cas sur les valeurs du type de données que nous définissons comme base lors de la création d'un nouveau domaine. Ci-dessus, nous avons utilisé respectivement INTEGER et VARCHAR(8)).

#### ALTER

En plus de créer des éléments tels que des tables ou des bases de données, nous pouvons également les modifier à l'aide de l'instruction **ALTER**. Par exemple, si nous avons oublié d'ajouter la colonne **AuxEmail** à la table **Person**, nous pouvons utiliser l'instruction suivante pour l'ajouter après la création de la table.

```pgsql
ALTER TABLE Person
  ADD COLUMN AuxEmail VARCHAR(255);
```

Comme vous pouvez le voir, nous spécifions d'abord la table où nous voulons ajouter la nouvelle colonne, puis nous spécifions le nom et le type de cet attribut. Mais il est important de considérer la valeur attribuée à ses cellules lorsque cette extension de table se produit.

Par défaut, SQL **autorise les valeurs NULL** dans la table, il remplira donc ces valeurs avec **NULL** s'il y a du contenu dans la table. Mais si nous voulons attribuer une valeur par défaut personnalisée aux cellules de la nouvelle colonne au lieu de NULL lorsqu'il y a déjà des données insérées dans la table, nous pouvons ajouter la propriété de valeur par défaut à la colonne que nous ajoutons :

```pgsql
ALTER TABLE Person
  ADD COLUMN AuxEmail VARCHAR(255) DEFAULT 'noEmail@gmail.com';
```

De cette façon, lorsque nous insérons un uplet et laissons la valeur **AuxEmail** non définie, le SGBD remplira automatiquement la cellule de cet attribut avec sa valeur par défaut. Cela s'applique également lors de l'ajout de la colonne elle-même lorsqu'il y a déjà des données dans la table. Nous pouvons également supprimer cette propriété de valeur par défaut en utilisant :

```pgsql
ALTER TABLE Person
  ALTER COLUMN Email DROP DEFAULT;
```

De même, ALTER nous permet également de supprimer un attribut :

```pgsql
ALTER TABLE Person
  DROP COLUMN Email;
```

Changer le type de données d'un attribut dans Postgres :

```pgsql
ALTER TABLE Person
  ALTER COLUMN Name TYPE CHAR(25);
```

Et renommer des éléments, parmi de nombreuses autres actions :

```pgsql
ALTER TABLE Person
  RENAME COLUMN Birth TO BirthDate; --Renomme la colonne Birth de la table Person--
ALTER TABLE Person
  RENAME TO People; --Renomme la table Person--
ALTER DATABASE sampledb
  RENAME TO otherName; --Renomme la base de données sampledb--
```

En résumé, ALTER nous permet de modifier des éléments qui ont déjà été créés dans la base de données sans avoir à les supprimer et à les recréer avec les changements. Sinon, nous devrions exporter les données stockées dans ces éléments et les réinsérer dans les nouveaux schémas, ce qui serait inefficace.

#### DROP

Nous pouvons supprimer des éléments avec l'instruction DROP. Son fonctionnement est très simple, car il suffit de spécifier le nom de l'élément à supprimer, comme la base de données que nous venons de créer :

```pgsql
DROP DATABASE sampledb;
```

Lors de l'exécution de cette instruction, SQL tente de supprimer la base de données, bien que nous puissions obtenir une erreur si nous y sommes connectés. En plus de simplement la supprimer, nous pouvons vérifier si elle existe avant d'essayer de la supprimer avec :

```pgsql
DROP DATABASE IF EXISTS sampledb;
```

De même, nous pouvons avoir un schéma comme cet exemple où il y a des clés étrangères dans Rental qui référencent ou pointent vers d'autres tables comme Bike et Person.

Si nous supprimons Rental, rien ne se passerait puisqu'aucune clé étrangère ne pointe vers Rental. Mais si nous voulons supprimer l'une des deux autres tables, un problème d'intégrité référentielle se posera. Par exemple, la suppression de Bike laisserait la référence de clé étrangère dans Rental qui pointe vers Bike orpheline. Ainsi, pour supprimer Bike et tous les outils SQL qui dépendent de Bike, c'est-à-dire ceux qui le référencent, nous pouvons utiliser CASCADE :

```pgsql
DROP TABLE Bike CASCADE;
```

En faisant cela, non seulement Bike serait supprimée, mais aussi la contrainte de clé étrangère dans Rental que nous n'avons pas encore introduite, ainsi que toutes les autres qui pointent vers Bike.

Il est important de noter que le CASCADE dans une instruction DROP n'est pas lié au CASCADE que nous pouvons définir dans une instruction CREATE pour définir des politiques de suppression ou d'insertion. Si, au lieu de supprimer une table entière, nous ne supprimons que certains uplets, nous pourrions nous retrouver avec une situation où un uplet a une valeur de clé étrangère qui ne correspond à aucun uplet dans la table référencée parce que nous l'avons supprimé. Nous pouvons établir des politiques de suppression où les uplets pointant vers celui supprimé sont également retirés, ou des actions similaires.

#### INSERT

Pour insérer des uplets dans les tables, nous utilisons l'instruction INSERT, où nous spécifions le nom de la table où nous voulons insérer, ainsi que les attributs de son schéma et les valeurs à insérer dans le nouvel uplet.

```pgsql
INSERT INTO Person (PersonID, Name, Birth, Email)
VALUES (5, 'Carol Johnson', '1985-07-15', 'carol@example.com');

INSERT INTO Bike (BikeID, Model, Weight)
VALUES (5, 'EcoCruiser', 14.2);

INSERT INTO Rental (PersonFK, BikeFK, RentalDate, Duration, Price)
VALUES (5, 5, '2025-07-10', 3, 25.50);
```

Mais, si nous n'avons pas certaines des valeurs pour l'uplet, nous pouvons les omettre en insérant des valeurs uniquement pour les attributs que nous avons. Nous pouvons même insérer un uplet avec des valeurs DEFAULT pour certains attributs. Mais cela ne fonctionne que si une valeur par défaut a été définie lors de la création de la table ou ajoutée avec une instruction ALTER.

```pgsql
INSERT INTO Bike (BikeID, Model)
VALUES (6, 'Speedster');
INSERT INTO Bike (BikeID, Model, Weight)
VALUES (7, 'Commuter', DEFAULT);
```

#### DELETE

Pour supprimer des uplets, vous pouvez utiliser DELETE, qui au niveau logique est très similaire à la clause SELECT que nous verrons plus tard (utilisée pour récupérer des données en réponse aux requêtes de base de données).

Pour utiliser DELETE, nous imposons un ensemble de conditions que les uplets de la table doivent remplir pour être sélectionnés. Les uplets qui remplissent les conditions sont ensuite supprimés par DELETE.

```pgsql
DELETE FROM Rental
WHERE PersonFK = 5
  AND BikeFK   = 5
  AND RentalDate = '2025-07-10';
```

Par exemple, ici tous les uplets ayant une valeur de 5 dans PersonFK et BikeFK et une date de location du 2025-07-10 seront supprimés.

#### UPDATE

De même, nous pouvons mettre à jour les valeurs des uplets à l'aide de UPDATE. Nous sélectionnons d'abord les uplets qui seront affectés par le changement que nous voulons effectuer en leur imposant des conditions, puis nous utilisons SET pour changer l'une de leurs valeurs d'attribut ou appliquer une transformation.

```pgsql
UPDATE Bike
SET Weight = 13.8
WHERE BikeID = 5;

UPDATE Person
SET Email = 'carol.johnson@example.com'
WHERE PersonID = 5;
```

#### Implémentation des contraintes

Grâce à ces instructions **DDL**, nous pouvons créer différents éléments où les données sont stockées. Mais comme nous l'avons vu, dans la plupart des domaines que nous modélisons, nous devons implémenter une série de contraintes pour nous assurer que les données adhèrent aux exigences de notre problème. (Ceci s'ajoute aux contraintes d'intégrité inhérentes au modèle relationnel, telles que l'existence de clés.)

Bien que cette distinction ne soit pas aussi forte en SQL, la plupart des contraintes que nous imposons aident à assurer l'intégrité des données, qu'elles se réfèrent aux propres règles du modèle relationnel ou aux règles métier de notre problème.

Pour implémenter des contraintes en SQL, nous pouvons commencer par les plus simples : les contraintes qui affectent une seule table. Celles-ci sont généralement implémentées à l'aide de l'instruction **CHECK** au sein d'une autre instruction comme **CREATE TABLE**, où une condition est spécifiée et que tous les uplets d'une table doivent remplir chaque fois que nous la modifions en insérant, modifiant ou supprimant ses uplets.

```pgsql
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE,
    Email VARCHAR(255),
    CHECK (Birth <= CURRENT_DATE)
);
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE,
    Email VARCHAR(255),
    CONSTRAINT BirthConstraint CHECK (Birth <= CURRENT_DATE)
);
```

Par exemple, nous pouvons supposer que la date de naissance d'une personne est toujours validée avant d'être enregistrée dans la base de données. Si un utilisateur saisit une date invalide dans la couche applicative, l'application elle-même générera une erreur et empêchera l'enregistrement d'une date invalide dans la base de données. Mais c'est toujours une bonne idée d'ajouter ce type de contrainte pour assurer l'intégrité des données.

Dans ce cas, une personne ne peut pas être née à une date postérieure à la date actuelle, que nous pouvons obtenir en SQL avec **CURRENT\_DATE**. Nous définissons donc une contrainte où l'attribut **Birth** doit être inférieur ou égal à la date actuelle pour toutes les lignes de la table Person.

Ces contraintes sont généralement définies sous la déclaration de l'attribut, et nous pouvons également leur donner un nom spécifique à l'aide de **CONSTRAINT**. Cela déclare la contrainte et lui attribue un nom que nous pouvons utiliser pour l'identifier. Nous pouvons ajouter ce nom non seulement à une contrainte CHECK mais aussi à toute déclaration similaire, telle que **PRIMARY KEY**, **FOREIGN KEY** ou **UNIQUE**, entre autres.

En continuant avec les contraintes sur une table spécifique, si nous devons nous assurer qu'un attribut ne peut pas prendre de valeurs NULL, nous pouvons utiliser soit un CHECK, soit un NOT NULL lors de la déclaration de l'attribut correspondant (auquel nous pouvons également donner un nom spécifique à l'aide de CONSTRAINT).

```pgsql
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE NOT NULL,
    Email VARCHAR(255)
);
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE CONSTRAINT BirthNotNull NOT NULL,
    Email VARCHAR(255)
);
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255),
    Birth DATE,
    Email VARCHAR(255),
    CONSTRAINT BirthNotNull CHECK (Birth IS NOT NULL)
);
```

Ces trois manières sont équivalentes si nous voulons obliger les personnes à enregistrer leur date de naissance dans la base de données, empêchant les valeurs NULL dans la colonne correspondante.

La différence principale entre l'utilisation de CHECK et le placement de NOT NULL à côté de la déclaration de l'attribut est que si nous utilisons CHECK, nous devons écrire une condition entre parenthèses similaire à la façon dont nous le faisons dans une requête SQL qui décrit la condition que nous voulons imposer, tant que cette requête n'affecte que les attributs de la table sur laquelle nous travaillons.

En revanche, NOT NULL à côté d'un attribut est une manière implicite d'indiquer cette restriction. Notez que les contraintes CHECK sont des expressions booléennes par ligne – elles ne peuvent pas contenir de sous-requêtes, d'agrégats ou de fonctions de fenêtrage (window functions) en SQL standard et dans la plupart des SGBD. Pour les conditions inter-tables, utilisez des **déclencheurs (triggers)** (portables) plutôt que CHECK.

Après avoir compris ce qu'implique CHECK, nous pouvons voir comment presque toute restriction de domaine sur les attributs peut être spécifiée dans l'une de ces instructions. Cependant, SQL nous offre plus de fonctionnalités, comme la définition d'une valeur par défaut pour les attributs avec **DEFAULT**.

```pgsql
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255) DEFAULT 'No name',
    Birth DATE,
    Email VARCHAR(255)
);
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255) CONSTRAINT NameDefaultValue DEFAULT 'No name', --On peut aussi nommer la valeur par défaut--
    Birth DATE,
    Email VARCHAR(255)
);
```

Comme nous l'avons vu précédemment, nous utilisons **DEFAULT** pour que lorsqu'un uplet est inséré avec une valeur manquante pour un certain attribut, si cet attribut a une valeur par défaut définie, l'uplet sera inséré avec cette valeur par défaut dans l'attribut correspondant au lieu de **NULL**.

C'est important car si nous incluons la restriction NOT NULL et ne définissons pas de valeur par défaut pour un attribut, le SGBD peut générer une erreur ici. Cela s'applique également lorsqu'un nouvel attribut est ajouté à la table à l'aide de ALTER, où nous pouvons définir une valeur par défaut en même temps.

```pgsql
CREATE TABLE Bike (
    BikeID INT,
    Model VARCHAR(255),
    Weight DOUBLE PRECISION,
    CONSTRAINT ModelValues CHECK (Model IN ('Model1', 'Model2', 'Model3'))
);
```

Par curiosité, si nous voulons définir explicitement les valeurs possibles qu'un attribut peut prendre, nous pouvons utiliser un CHECK comme celui ci-dessus. C'est la même expression que nous utilisons lors de la création d'un nouveau domaine avec **CREATE DOMAIN**. Nous pouvons ensuite l'affecter comme type de données à l'attribut Model. Nous avons donc la possibilité de créer un domaine personnalisé pour un attribut ou de définir une contrainte avec CHECK pour modéliser son domaine (bien que dans la plupart des cas, il soit préférable d'utiliser **CREATE DOMAIN** pour une meilleure maintenabilité).

En continuant avec les contraintes qui affectent une seule table, nous avons également celles plus liées à l'intégrité des données concernant le modèle relationnel. Par exemple, pour identifier de manière unique les uplets d'une table, nous avons des clés candidates dans le modèle relationnel, que nous pouvons déclarer en SQL à l'aide de **UNIQUE** en combinaison avec NOT NULL.

```pgsql
CREATE TABLE Bike (
    BikeID INT,
    Model VARCHAR(255),
    Weight DOUBLE PRECISION,
    UNIQUE (Model)
);
```

Par exemple, si nous supposons que dans notre problème il n'y a pas plusieurs vélos différents avec le même nom de modèle, alors nous pouvons utiliser Model comme clé candidate pour identifier de manière unique tous les uplets de la table.

Ainsi, pour déclarer explicitement que Model peut servir à l'identification des uplets, nous utilisons UNIQUE. Cela indique que toutes les valeurs que cet attribut prend dans (tous les uplets de la table) doivent être différentes.

Nous pouvons également appliquer cela à plus d'un attribut, où UNIQUE déterminerait que la combinaison de valeurs de tous ces attributs inclus dans la contrainte doit être différente dans tous les uplets de la table.

L'utilité principale de UNIQUE est qu'elle garantit que certains attributs répondent à la définition d'une clé candidate. Ainsi, si nous insérons plusieurs uplets avec les mêmes valeurs répétées dans des attributs qui forment une clé candidate définie avec UNIQUE, le SGBD générera une erreur. Mais au-delà de cela, nous n'avons pas à définir toutes les clés candidates qui existent à moins que le domaine ou les exigences du problème ne nous y obligent.

Habituellement, nous définissons simplement la clé primaire d'une table avec PRIMARY KEY, sans qu'il soit nécessaire qu'elle soit une clé candidate sélectionnée.

```sql
CREATE TABLE Person (
    PersonID INT,
    Name VARCHAR(255) DEFAULT 'No name',
    Birth DATE,
    Email VARCHAR(255),
    CONSTRAINT PersonPK PRIMARY KEY (PersonID) --La contrainte est nommée PersonPK--
);
```

Lorsque nous introduisons la contrainte de clé primaire sur un ensemble d'attributs, nous déclarons implicitement que ces attributs ne peuvent pas contenir de valeurs NULL, et que les combinaisons de valeurs qu'ils prennent doivent toutes être uniques dans les uplets de la table (tout comme avec UNIQUE).

C'est comme si nous définissions implicitement UNIQUE et NOT NULL sur les attributs qui forment la clé primaire, en nous assurant qu'ils remplissent toutes les conditions nécessaires pour former réellement une clé primaire (qui peut également être référencée par une clé étrangère).

Pour déclarer l'existence de clés étrangères, nous utilisons FOREIGN KEY sur les attributs qui la constituent.

```pgsql
CREATE TABLE Rental (
    PersonFK INT,
    BikeFK INT,
    RentalDate DATE,
    Duration INT,
    Price DOUBLE PRECISION,
    CONSTRAINT RentalPK PRIMARY KEY (PersonFK, BikeFK, RentalDate),
    CONSTRAINT FK_Rental_Person FOREIGN KEY (PersonFK) REFERENCES Person(PersonID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FK_Rental_Bike FOREIGN KEY (BikeFK) REFERENCES Bike(BikeID) ON DELETE
    SET NULL ON UPDATE CASCADE
);
```

Comme vous pouvez le voir, la déclaration des clés étrangères est très similaire aux clés primaires, sauf que nous utilisons l'instruction FOREIGN KEY. Mais pour que le SGBD assure l'intégrité référentielle dans la base de données, nous devons définir ce qui se passe lors de l'insertion, de la mise à jour ou de la suppression d'uplets dans les tables référencées par des clés étrangères.

Pour comprendre cela, le cas le plus simple est celui de l'insertion d'un uplet dans une table comme Rental, où des valeurs doivent être fournies pour ses clés étrangères. Par défaut (NO ACTION), SQL autorise une clé étrangère à prendre des valeurs NULL, ce qui signifie que NULL satisfait la contrainte de clé étrangère. Mais dans ce cas, nous devrions ajouter une contrainte NOT NULL sur ces attributs car, dans le modèle conceptuel, une entité Rental était liée à au moins une entité Bike et une entité Person, comme l'indique la cardinalité minimale.

Ainsi, si nous insérons un uplet avec une valeur NULL dans l'attribut de clé étrangère et que nous avions la contrainte NOT NULL, nous recevrions une erreur. D'un autre côté, si nous insérons une valeur qui n'est pas NULL mais qui n'existe pas dans l'attribut de la table que nous référençons, alors le SGBD n'autorisera pas non plus cette insertion – car cette clé étrangère ne référencera aucun uplet existant dans la table vers laquelle elle pointe.

Pour indiquer où elle pointe, nous utilisons REFERENCES dans la contrainte FOREIGN KEY elle-même, où la table et l'attribut vers lesquels la clé étrangère doit pointer sont spécifiés. Une clé étrangère doit référencer une clé candidate dans la table parente — soit la clé primaire, soit une autre colonne (ou ensemble de colonnes) déclarée UNIQUE et NOT NULL. Les colonnes référençantes et référencées doivent correspondre en nombre, en ordre et avoir des types de données compatibles.

Ensuite, si nous essayons de supprimer un uplet de la table Bike ou Person qui est référencé par un uplet dans la table Rental, nous pouvons définir plusieurs politiques de suppression.

Tout d'abord, en supprimant l'uplet de Bike ou Person, nous aurions un uplet dans Rental qui ne référence aucun uplet valide d'une autre table, créant un problème d'intégrité référentielle dû à une référence orpheline.

Une option pour résoudre ce problème consiste à supprimer également l'uplet dans la table Rental et à supprimer récursivement les uplets qui pointent vers les uplets retirés par ce processus. Nous déclarons cela avec ON DELETE CASCADE. Mais si nous voulons conserver l'uplet dans Rental, au lieu de le supprimer, nous pouvons attribuer une valeur particulière à la clé étrangère qui ne pointe plus vers aucun uplet valide (comme NULL ou la valeur par défaut DEFAULT). Nous déclarons cela avec **ON DELETE SET [valeur]**, où [valeur] peut être SET NULL ou SET DEFAULT.

Mais nous devons être prudents avec NULL, car si l'attribut de clé étrangère fait également partie de la clé primaire, comme dans cet exemple, il entrera en conflit avec la contrainte PRIMARY KEY implicite qui l'empêche d'être NULL.

Nous ne sommes pas obligés de déclarer ON DELETE dans ces contraintes, donc si nous ne le faisons pas, l'action par défaut (appelée NO ACTION) sera exécutée. Cela signifie rejeter la suppression de l'uplet dans Bike ou Person, et afficher une erreur à l'utilisateur.

De même, ce problème peut également survenir lors de la mise à jour d'un uplet, de sorte que le même mécanisme ON DELETE s'applique aux modifications d'uplets, que nous pouvons définir avec ON UPDATE.

Enfin, une clé étrangère peut référencer la table dans laquelle elle se trouve, et l'utilisation de la politique CASCADE est tout à fait valide. En effet, elle supprime récursivement les uplets qui causent des problèmes d'intégrité référentielle, et non des tables entières. Même s'il y a des uplets qui se référencent eux-mêmes, cela ne pose aucun problème, car le SGBD peut gérer ces cas limites.

Ce sont les contraintes de base que nous pouvons appliquer à une seule table, bien qu'il existe des outils plus avancés qui aident à assurer l'intégrité des données ou même à optimiser leur manipulation et leur interrogation.

Mais il existe certaines contraintes qui n'affectent pas seulement une table du schéma mais peuvent impliquer des conditions sur plusieurs tables. Pour les implémentations, nous avons plusieurs options, telles que les assertions, qui sont des conditions très similaires à CHECK qui sont vérifiées chaque fois que l'une des tables impliquées dans la condition est modifiée.

```pgsql
CREATE ASSERTION RentalEmailConstraint CHECK (
    NOT EXISTS (
        SELECT 1
        FROM Rental r
            JOIN Person p ON r.PersonFK = p.PersonID
        WHERE p.Email IS NULL
    )
);
```

Par exemple, ici nous créons une assertion qui vérifie que nous n'avons loué un vélo à aucune personne n'ayant pas d'Email défini. Pour ce type de contrainte, nous utilisons généralement des requêtes SQL complètes au sein du CHECK, car elles sont plus complexes à modéliser que les contraintes CHECK que nous plaçons sur une seule table.

Nous pourrions également le faire dans les contraintes CHECK de table au lieu d'utiliser des assertions, bien que ce soit souvent plus complexe à modéliser.

Enfin, outre les assertions, nous pouvons implémenter des contraintes sur plusieurs tables avec des déclencheurs (triggers), qui sont des instructions composées d'un événement, d'une condition et d'une action. Lorsque l'événement défini se produit, la condition qui constitue la contrainte est vérifiée, et selon qu'elle est vraie ou fausse, une certaine action est exécutée ou non sur la base de données.

Maintenant que nous savons comment fixer des contraintes sur un schéma relationnel, nous pouvons affiner l'implémentation logique de notre exemple en ajoutant les contraintes nécessaires, ce qui donne le code suivant :

```pgsql
DROP TABLE IF EXISTS Rental;
DROP TABLE IF EXISTS Bike;
DROP TABLE IF EXISTS Person;
CREATE TABLE Person (
    PersonID INT NOT NULL,
    Name VARCHAR(50) NOT NULL DEFAULT 'No name',
    Birth DATE NOT NULL,
    Email VARCHAR(50) NOT NULL UNIQUE,
    CONSTRAINT PersonPK PRIMARY KEY (PersonID),
    CONSTRAINT ConstraintPersonBirth CHECK (Birth <= CURRENT_DATE)
);
CREATE TABLE Bike (
    BikeID INT NOT NULL,
    Model VARCHAR(50) NOT NULL,
    Weight DOUBLE PRECISION NOT NULL,
    --Cette contrainte est redondante en raison de la définition de la contrainte PRIMARY KEY--
    UNIQUE (BikeID),
    CONSTRAINT BikePK PRIMARY KEY (BikeID),
    CONSTRAINT ConstraintBikeWeight CHECK (Weight > 0) --Le poids doit être positif--
);
CREATE TABLE Rental (
    PersonFK INT NOT NULL,
    BikeFK INT NOT NULL,
    RentalDate DATE NOT NULL,
    Duration INT NOT NULL,
    Price DOUBLE PRECISION NOT NULL,
    CONSTRAINT RentalPK PRIMARY KEY (PersonFK, BikeFK, RentalDate),
    CONSTRAINT FKRentalPerson FOREIGN KEY (PersonFK) REFERENCES Person(PersonID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT FKRentalBike FOREIGN KEY (BikeFK) REFERENCES Bike(BikeID) ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT ConstraintRentalDuration CHECK (Duration > 0),
    CONSTRAINT ConstraintRentalPrice CHECK (Price >= 0),
    CONSTRAINT ConstraintRentalDate CHECK (RentalDate <= CURRENT_DATE)
);
```

Comme vous pouvez le voir, dans le script de création, nous avons ajouté des instructions DROP pour supprimer les tables avant de créer les tables finales avec toutes les contraintes correctes. Nous faisons généralement cela lorsqu'il n'y a pas de données dans les tables, car un DROP supprimerait tout ce qui y est stocké. De plus, lorsque nous supprimons plusieurs tables liées par des clés étrangères, nous voulons éviter que le SGBD ne génère des erreurs d'intégrité référentielle. Pour cette raison, il est courant de supprimer d'abord les tables vers lesquelles aucune clé étrangère ne pointe, puis de continuer avec le reste.

### DCL

Maintenant que vous avez vu comment définir les éléments de base du modèle relationnel dans un SGBD avec SQL, nous devrions considérer la sécurité avec laquelle ces opérations sont effectuées (ainsi que celles que nous verrons en DML). Après tout, tous les utilisateurs de la base de données n'ont pas forcément de bonnes intentions lorsqu'ils opèrent sur le SGBD.

Ainsi, en DCL, nous pouvons définir une série d'instructions pour gérer les utilisateurs, les rôles et les autorisations, qui établissent qui peut faire quoi sur la base de données.

#### Rôles d'utilisateur

La première chose que nous pouvons faire est de créer des **rôles**, qui, comme leur nom l'indique, sont des rôles attribués à un utilisateur de la base de données et qui déterminent ce qu'il peut ou ne peut pas faire avec la base de données. Fondamentalement, le rôle fonctionne comme un **ensemble d'autorisations**.

Par défaut, un rôle PostgreSQL ne peut pas se connecter à moins qu'il ne soit créé WITH LOGIN (ou via CREATE USER). Pour simplifier cette section, nous pouvons supposer que lorsqu'un utilisateur veut accéder à la base de données, il suffit de lui donner un rôle avec l'autorisation de connexion (bien que ces mécanismes puissent dépendre du SGBD que nous utilisons).

```pgsql
CREATE ROLE user1 WITH LOGIN PASSWORD 'userPassword';
DROP ROLE user1; --Si nous voulons supprimer le rôle--
```

Il peut donc s'authentifier auprès du SGBD à l'aide du mot de passe que nous définissons ici. Dans PostgreSQL, les rôles peuvent généralement se connecter par défaut car CONNECT est accordé à PUBLIC. Pour restreindre l'accès, vous devez d'abord faire un REVOKE CONNECT ON DATABASE ... FROM PUBLIC, puis faire un GRANT CONNECT de manière sélective. Ainsi, mise à jour des autorisations avec GRANT :

```pgsql
GRANT CONNECT ON DATABASE sampledb TO user1;
```

Par défaut, l'utilisateur ne pourra rien faire d'autre que se connecter. Ainsi, en utilisant GRANT de la manière suivante, nous pouvons donner les autorisations nécessaires pour exécuter toutes les instructions nécessaires sur certains éléments de la base de données.

```pgsql
GRANT SELECT, UPDATE
ON TABLE Rental
TO user1;
```

Par exemple, ici nous donnons l'autorisation d'exécuter les instructions SELECT et UPDATE sur la table Rental.

Ou si nous voulons donner toutes les autorisations possibles pour faire n'importe quoi sur un élément, nous pouvons utiliser ALL, comme ceci :

```pgsql
GRANT ALL PRIVILEGES
ON TABLE Bike
TO user1;
```

Ou, si nous voulons être plus précis, nous pouvons même contrôler sur quelles colonnes d'une table certaines instructions peuvent être exécutées :

```pgsql
GRANT SELECT (PersonID, Name)
ON TABLE Person
TO user1;
```

De même, si au lieu d'utiliser GRANT nous utilisons REVOKE, nous supprimons certaines autorisations que possède le rôle :

```pgsql
REVOKE ALL PRIVILEGES
ON TABLE Bike
FROM user1;
```

Ce n'est qu'une partie de ce qui peut être contrôlé pour un rôle dans une base de données à l'aide des instructions DCL, car la sécurité est un aspect critique.

### DML

Après avoir configuré les autorisations des utilisateurs pour contrôler ce qu'un utilisateur peut faire dans la base de données, nous avons suffisamment d'éléments pour commencer à manipuler et interroger les données. Il est donc temps d'introduire l'ensemble des instructions qui composent le DML de SQL, qui gère principalement la gestion des données stockées.

#### CRUD

Pour comprendre la gestion des données, vous devriez réfléchir à la manière dont vous allez opérer sur elles. Cela est guidé par les besoins de l'utilisateur ou du client final. De là découle le **modèle CRUD (Create, Retrieve, Update, and Delete)**, qui définit les opérations fondamentales effectuées sur les données d'un projet réel et que la base de données doit supporter.

Comme vous pouvez le voir par son acronyme, au niveau le plus fondamental de notre base de données, de nouvelles données peuvent être insérées (Create), interrogées une fois stockées (Retrieve), et peuvent également être modifiées (Update) ou supprimées (Delete) lorsqu'elles ne sont plus utiles pour le domaine.

De toutes ces opérations, la plus importante est l'interrogation des données. Si nous y réfléchissons, tout service fourni à l'utilisateur final peut être réduit à une requête sur les données stockées.

Par exemple, le simple fait de visualiser des informations sauvegardées signifie qu'elles doivent être récupérées via une requête. En réalité, toute métrique devant être calculée sur les données implique également une interrogation puis un calcul sur celles-ci. Ainsi, même si le DML implique une grande variété d'instructions aux objectifs divers, nous nous concentrerons ici sur celles qui constituent les blocs fondamentaux pour effectuer des requêtes – CRUD.

Lorsqu'on travaille avec des bases de données relationnelles, il existe un certain mécanisme que les requêtes suivent pour obtenir les données que nous demandons au SGBD.

Tout d'abord, nous avons une série de tables où les informations sont stockées dans des uplets. Celles-ci, nous les appellerons tables de base, c'est-à-dire celles que nous créons initialement avec CREATE TABLE. Nous ne modifions pas ces tables de base directement – au lieu de cela, nous leur appliquons une série d'opérations, dont beaucoup proviennent de l'algèbre relationnelle, ce qui donne des tables intermédiaires. Ces tables intermédiaires passent par la séquence d'opérateurs jusqu'à atteindre une table finale avec les résultats que nous avons demandés.

En d'autres termes, une requête consiste à obtenir une table résultante avec des données provenant d'un ensemble de tables de base.

D'un point de vue formel, cela est parfois interprété en algèbre relationnelle comme si la requête était un [**arbre relationnel**](https://www.cs.emory.edu/~cheung/Courses/554/Syllabus/5-query-opt/intro.html) où les nœuds feuilles sont les tables de base. Au fur et à mesure que les opérateurs, qui peuvent être unaires ou binaires, sont appliqués, de nouvelles tables intermédiaires sont générées, représentant les nœuds intermédiaires de l'arbre jusqu'à atteindre le **nœud racine**, qui est la table finale, ou le **résultat de la requête**.

Grâce à cela, nous pouvons voir chaque opérateur comme s'il s'agissait d'une fonction mathématique qui prend une ou plusieurs tables en entrée, effectue une certaine opération sur elles et renvoie une autre table en sortie.

En revanche, lorsque nous programmons en SQL, nous n'utilisons pas directement ces opérateurs relationnels, car ce sont des outils formels qui supportent l'interrogation de données. Au lieu de cela, nous utilisons une série d'instructions DML, dont certaines ressemblent à des opérateurs relationnels mais sont en réalité destinées à être combinées avec d'autres instructions pour former une requête.

SQL n'est pas un langage formel comme l'algèbre relationnelle – c'est une implémentation basée sur ce langage formel, ainsi que sur le calcul relationnel, qui nous permet d'abstraire certains détails formels. Ainsi, lorsque nous exécutons une requête SQL, le SGBD la transformera d'une séquence d'instructions SQL en un plan d'exécution plus proche d'une séquence d'opérateurs d'algèbre relationnelle. Ensuite, elle est résolue en interne avec des techniques avancées qui travaillent sur les opérateurs formels eux-mêmes.

Il est également important de noter que la majeure partie de l'optimisation est effectuée par le SGBD lors de l'analyse de la structure de la requête. Malgré cela, nous devrions toujours essayer d'"aider" l'optimiseur du SGBD en écrivant des requêtes SQL visant à minimiser sa charge de travail. Pour cela, il existe certaines [**techniques**](https://www.geeksforgeeks.org/sql/best-practices-for-sql-query-optimizations/) que vous devriez suivre (mais que nous ne couvrirons pas en détail ici).

Avant d'introduire les instructions DML, il est conseillé d'avoir le [**schéma**](https://gist.github.com/cardstdani/587e515368c9755ab6bc9b78a119292f) chargé avec les tables Person, Bike et Rental, ainsi que quelques données d'exemple. En plus de créer les tables, pour s'assurer que les requêtes renvoient des données et que nous puissions vérifier qu'elles fonctionnent réellement, vous devrez y insérer des données à l'aide de INSERT.

#### SELECT et FROM

Les premières instructions que nous verrons pour construire une requête sont les plus basiques : SELECT et FROM. Vous avez souvent besoin d'un FROM pour construire une requête SQL, car il est utilisé pour déterminer de quelle table les données seront extraites. (Selon le SGBD, vous pouvez exécuter des requêtes sans FROM (par exemple, `SELECT 1;`), bien que certains systèmes utilisent des alternatives comme `VALUES` ou `FROM DUAL`). Voici comment cela fonctionne :

```pgsql
SELECT *
FROM Bike;
```

Par exemple, si nous exécutons cette requête, elle renverra tous les uplets stockés dans la table Bike. En effet, nous avons fourni une table à FROM, dans ce cas, Bike, à partir de laquelle les données seront obtenues. (FROM peut référencer une ou plusieurs tables (y compris des jointures, des sous-requêtes ou des CTE)). Ensuite, après avoir obtenu les données de cette table, SELECT \* est utilisé pour sélectionner les données de toutes ses colonnes, ce que nous renverrons à l'utilisateur.

Bien que nous ne puissions utiliser qu'une seule table dans le FROM, nous pouvons en fait effectuer une série d'opérations sur plusieurs tables de base et utiliser ce résultat comme table dans le FROM. En d'autres termes, nous pouvons faire en sorte que le résultat d'une requête SQL, qui est lui-même une table, soit la table utilisée dans le FROM, comme illustré ici :

```pgsql
SELECT *
FROM (SELECT * FROM Bike);
```

Il n'est pas courant de faire cela avec un exemple aussi simple, mais il est utile de montrer que nous pouvons fournir tout ce que nous pouvons construire avec une requête SQL comme table au FROM (puisque le résultat de toutes les requêtes que nous pouvons construire est en fait une table).

En essayant de transférer la fonctionnalité de ces instructions aux opérateurs de l'algèbre relationnelle, nous verrons qu'il n'y a pas d'opérateur spécifique pour FROM qui fasse quelque chose de similaire.

Mais pour SELECT, il existe un opérateur qui fait presque la même chose. Plus précisément, en algèbre relationnelle, il existe l'opérateur de projection **π(Table, ListeAttributs)**. Il prend en entrée une table avec des données et une liste de certains de ses attributs, et renvoie une autre table construite à partir de l'entrée où seuls les attributs de la liste sont conservés – avec toutes les données de leurs colonnes – en écartant le reste des attributs ne figurant pas dans la liste.

C'est exactement ce que fait SELECT : nous avons une table d'entrée donnée par la clause FROM, puis nous définissons une série d'attributs que nous voulons que la table résultante possède, en écartant les autres.

```pgsql
SELECT Name, Birth
FROM Person;
```

Par exemple, lorsque FROM obtient les données de la table Person, il les fournit en entrée à SELECT. Celui-ci renvoie alors une table où seuls les attributs Name et Birth que nous avons listés sont présents, avec toutes les données de leurs colonnes. Si nous avons besoin d'obtenir tous les attributs, nous pouvons utiliser SELECT \*, et nous obtiendrons la table d'entrée avec tous ses attributs et données tels qu'ils ont été reçus.

#### Alias

Un autre opérateur que nous avons en SQL sous une forme presque équivalente est l'**opérateur de renommage**. Comme son nom l'indique, nous l'utilisons pour fournir des noms alternatifs aux tables ou aux attributs que nous utilisons, afin d'éviter les problèmes d'ambiguïté ou de raccourcir les noms longs.

```pgsql
SELECT P.Name, Birth AS B
FROM Person P;
```

En algèbre relationnelle, l'opérateur est noté **ρ(Objet, Alias)**, et sa fonction est d'attribuer un alias à un objet, qui peut être soit une table, soit un attribut.

En SQL, il existe plusieurs façons de l'utiliser. D'une part, dans la clause FROM, nous pouvons utiliser AS [alias] ou placer directement le nom de l'alias après la ou les tables impliquées dans la requête. Cela nous permet de les désigner par leur alias au lieu de leur nom complet, surtout si nous utilisons le même plusieurs fois.

De plus, dans la clause SELECT, nous devrions utiliser AS pour éviter les ambiguïtés lors de l'attribution d'alias aux attributs que nous allons renvoyer. L'utilité principale ici est de renommer les attributs renvoyés pour avoir des noms plus descriptifs ou appropriés au contexte.

Par exemple, au lieu de renvoyer l'attribut Birth, ses données sont renvoyées sous le nom B, qui est plus court, tandis que l'attribut Name de la table P est renvoyé avec le même nom qu'il a au moment de l'exécution du SELECT.

#### DISTINCT

Une autre instruction importante est DISTINCT, que nous utilisons pour supprimer les uplets en double du résultat de la requête. Pour comprendre cela, il est important de noter que SQL n'utilise pas d'ensembles pour représenter les uplets d'une table. Au lieu de cela, les uplets sont représentés dans un multiensemble, ce qui permet des uplets identiques, en particulier dans les tables intermédiaires où les contraintes de clé primaire et autres ne s'appliquent pas. Ainsi, si nous voulons que le résultat n'ait pas d'uplets en double, nous devons ajouter DISTINCT au début de la liste des attributs dans l'instruction SELECT.

```pgsql
SELECT DISTINCT P.Name 
FROM Person P;
```

Lors de l'exécution de cette requête, nous devrions voir moins de noms car certaines personnes ont le même nom. De plus, DISTINCT n'est pas seulement utilisé au début de la liste des attributs. Nous pouvons également l'utiliser pour compter ou effectuer des opérations d'agrégation qui n'affectent que les valeurs non répétées, comme nous le verrons plus tard.

Cette instruction n'a pas d'équivalent direct avec un opérateur d'algèbre relationnelle, car l'algèbre relationnelle travaille formellement avec des ensembles où les uplets en double n'existent pas, éliminant ainsi le besoin d'un opérateur spécifique pour supprimer les doublons.

#### WHERE

Avec ce que nous avons vu jusqu'à présent, nous pouvons récupérer des données à partir de tables, même en supprimant les doublons ou les attributs inutiles pour le résultat – mais nous n'avons pas introduit de moyen de ne conserver que les uplets qui remplissent certaines conditions.

C'est précisément ce que fait la clause WHERE en SQL, qui possède un opérateur d'algèbre relationnelle très similaire appelé **opérateur de sélection** (ne pas confondre avec SELECT) et noté **σ(Table, Condition)**. Cet opérateur prend une table avec des données et une condition appliquée aux uplets stockés dans la table, de sorte que seuls les uplets qui remplissent la condition sont pris en compte dans la table de sortie fournie par l'opérateur.

En d'autres termes, tous les opérateurs produisent une table résultante, qui dans ce cas a exactement le même schéma que la table d'entrée, à la différence que la table de sortie ne contient que les uplets qui remplissent la condition que nous avons donnée à l'opérateur. Cela nous permet d'effectuer un filtrage plus complexe sur les données stockées, comme la récupération des locations ayant un prix supérieur à un certain montant.

Par exemple, en exécutant la requête suivante, nous obtiendrons tous les uplets de Rental ayant un prix supérieur à 10. Plus précisément, nous obtiendrons tous leurs attributs, puisque nous avons utilisé \* dans l'instruction SELECT.

```pgsql
SELECT * 
FROM Rental AS R 
WHERE R.Price > 10;
```

Il existe de nombreuses conditions possibles que nous pouvons utiliser dans la clause WHERE. Tout d'abord, nous pouvons comparer des attributs numériques et des chaînes avec des opérateurs tels que >, <, <= ou <>. Ces derniers vérifient quand deux choses sont différentes.

```pgsql
SELECT * 
FROM Rental 
WHERE Price > 50 AND Duration <> 7;
--L'opérateur <> signifie les valeurs de l'attribut Duration qui diffèrent de 7--

SELECT Name 
FROM Person 
WHERE Name > 'M';

SELECT * 
FROM Person 
WHERE Name = 'Carol King';
```

Comme vous pouvez le voir, les opérateurs fonctionnent de la même manière avec les nombres qu'avec le texte. Mais en les utilisant avec du texte, comme dans la comparaison Name > 'M', nous obtenons tous les uplets ayant une valeur Name qui est lexicographiquement après 'M'.

Il existe de nombreuses options que nous pouvons définir pour les conditions concernant les valeurs de texte. Par exemple, il existe des fonctions comme LOWER() et UPPER() qui convertissent le texte respectivement en minuscules et en majuscules. Nous pouvons également utiliser LIKE pour comparer du texte avec un motif similaire à une expression régulière, où nous avons des **caractères génériques** **%** et **\_** (% désigne un nombre arbitraire de caractères et **\_** un seul caractère).

Nous pouvons également utiliser l'opérateur **BETWEEN** pour vérifier si un texte est lexicographiquement entre deux autres, mais nous pouvons l'utiliser pour comparer d'autres types de données également.

```pgsql
SELECT * 
FROM Person 
WHERE Email LIKE '%@example.com';

SELECT * 
FROM Person 
WHERE LOWER(Name) = 'carol king';

SELECT * 
FROM Person 
WHERE Name BETWEEN 'A' AND 'M';

SELECT * 
FROM Rental 
WHERE RentalDate BETWEEN '2025-06-01' AND '2025-06-30';
```

En continuant avec les opérations sur le texte, nous avons également l'opérateur SIMILAR de la norme SQL-99, qui permet de comparer du texte avec des expressions régulières, en utilisant les mêmes caractères génériques que dans LIKE. Mais ces expressions régulières ne sont pas celles que l'on trouve dans POSIX ou Perl – ce sont simplement des expressions formées par les caractères génériques de LIKE avec une série d'opérateurs logiques similaires à ceux des expressions régulières conventionnelles.

```pgsql
SELECT * 
FROM Person 
WHERE Name SIMILAR TO '(John|Jane)%'; --Correspond aux noms commençant par John ou Jane--

SELECT * 
FROM Bike 
WHERE Model SIMILAR TO '%[0-9]'; --Modèles de vélos se terminant par un chiffre entre 0 et 9--
```

En plus de ces opérateurs, il existe également les opérateurs logiques AND, OR et NOT, qui nous permettent de décrire des conditions plus complexes.

```pgsql
SELECT * 
FROM Rental 
WHERE (RentalDate BETWEEN '2025-07-01' AND '2025-07-31') AND (Price > 50);

SELECT * 
FROM Bike 
WHERE Weight < 9.0 OR Model LIKE '%Trek%';
--Les parenthèses ne sont pas obligatoires, mais fortement recommandées--

SELECT 1 AS ColumnOfOnes
FROM Bike 
WHERE NOT (Weight > 10.0);
```

Ici, nous pouvons voir comment dans la clause SELECT de la dernière requête, au lieu de renvoyer un attribut, nous renvoyons un littéral, qui est une valeur numérique de 1. Si nous regardons le résultat, nous obtiendrons une table avec un seul attribut, ColumnOfOnes, qui est ce que nous voulons obtenir en le mettant dans la liste SELECT.

Quant aux uplets, elle en renvoie autant qu'il y en a dans Bike qui remplissent la condition WHERE, bien que nous ne verrons pas leurs valeurs. Au lieu de cela, chaque uplet n'aura que la valeur 1 pour l'attribut ColumnOfOnes, qui est le nom que nous avons donné à ces valeurs 1.

```pgsql
SELECT *, (Price / Duration) AS Ratio 
FROM Rental 
WHERE (Price / Duration) > 5;

SELECT *, (Price*1.0 / Duration) AS Ratio 
FROM Rental 
WHERE (Price*1.0 / Duration) > 5;
```

Lorsque nous utilisons des opérateurs arithmétiques, il est important de prendre en compte les types de données utilisés. Nous avons tous les opérateurs arithmétiques habituels +, -, \*, et /. Mais lors de l'utilisation de la division, si nous n'effectuons pas de transtypage (casting) explicite, la division peut être effectuée comme une division entière, fournissant un résultat arrondi qui peut être éloigné de ce dont nous avons besoin.

Pour obtenir une division exacte avec toutes les décimales, nous pouvons multiplier l'un des opérandes par 1.0 pour forcer le SGBD à le traiter comme une valeur décimale. Mais nous avons toujours la possibilité de multiplier l'opération par une certaine quantité comme 100 pour que le résultat final soit un entier au lieu d'une décimale, en particulier lors du calcul de ratios.

Bien entendu, en plus des opérations arithmétiques, SQL propose une série de fonctions qui nous permettent d'effectuer des opérations mathématiques plus avancées comme les suivantes :

```pgsql
SELECT
  ABS(-3.5)      AS abs,
  CEIL(2.1)      AS ceil,
  FLOOR(2.9)     AS floor,
  ROUND(2.345,2) AS round,
  TRUNC(2.345,1) AS trunc,
  SQRT(16)       AS sqrt,
  POWER(3,4)     AS power,
  MOD(17,5)      AS mod;

SELECT 
  EXP(1)       AS e_to_1, --Le nombre e à la puissance 1--
  LN(10)       AS ln10,
  LOG(10,100)  AS logBase10Of100; --Logarithme en base 10 du nombre 100--

SELECT
  SIN(PI()/2)   AS sin90deg,
  COS(0)        AS cos0deg,
  TAN(PI()/4)   AS tan45deg;
```

D'autre part, SQL permet d'effectuer des opérations logiques au niveau du bit, comme un ET au niveau du bit de la représentation binaire de deux nombres, ou un décalage de leurs bits, entre autres.

```pgsql
SELECT
  9  & 5   AS bitwiseAnd,
  9  | 5   AS bitwiseOr,
  9  # 5   AS bitwiseXor,
  1 << 3   AS shiftLeft,
  16 >> 2  AS shiftRight;
```

Enfin, si nous voulons vérifier si un attribut contient la valeur NULL ou non, nous ne pouvons pas utiliser l'opérateur =. Au lieu de cela, nous devons utiliser un opérateur spécifique appelé IS pour cette comparaison :

```pgsql
SELECT * 
FROM Person 
WHERE Email IS NOT NULL; --NULL ne peut pas être comparé avec l'opérateur =, mais avec IS --
```

#### UNION, INTERSECT et EXCEPT

Il existe d'autres opérateurs d'algèbre relationnelle qui sont utiles et ont des instructions SQL équivalentes, comme ceux qui opèrent sur des ensembles d'uplets. Jusqu'à présent, nous avons traité les tables comme s'il s'agissait de multiensembles car SQL autorise les uplets en double par défaut. Mais il y a des situations où il est plus clair d'utiliser des opérations sur les tables en les traitant comme s'il s'agissait d'ensembles d'uplets.

```pgsql
SELECT BikeFK AS BikeID 
FROM Rental 
WHERE Duration > 3 
UNION 
SELECT BikeFK 
FROM Rental 
WHERE Price <= 15;
```

Par exemple, lorsque nous effectuons une requête, elle renvoie une table avec des uplets, que nous pouvons voir comme un ensemble d'uplets. Ainsi, si nous avons plusieurs requêtes qui renvoient des tables avec le même nombre de colonnes et que toutes ont des types de données compatibles (ce qui signifie qu'ils sont soit les mêmes, soit convertibles par le SGBD), alors nous pouvons effectuer une opération d'ensemble entre elles, comme une union des deux ensembles d'uplets. Cela donne à son tour un autre ensemble d'uplets contenant tous ceux des deux ensembles initiaux.

Nous faisons cela à l'aide de l'opérateur UNION qui, par défaut, supprime les uplets en double puisqu'il traite les tables comme des ensembles d'uplets. Dans cet exemple spécifique, nous effectuons une union entre un ensemble d'uplets avec le schéma (BikeID) et un autre (BikeFK). Comme les deux schémas ont le même nombre d'attributs avec les mêmes types de données, quels que soient leurs noms, nous pouvons effectuer leur union, ce qui donne une table finale contenant tous les uplets des deux, en supprimant les doublons.

```pgsql
SELECT PersonFK, RentalDate AS DateName 
FROM Rental 
WHERE RentalDate < '2025-01-01' 
INTERSECT 
SELECT PersonFK, RentalDate AS DateName2 /*Ce nom n'est pas conservé, celui du dessus l'est*/ 
FROM Rental 
WHERE RentalDate > '2024-01-01';
```

En plus d'effectuer une union, nous pouvons également réaliser d'autres opérations d'ensemble courantes comme l'intersection ou la différence. Par exemple, avec INTERSECT, nous ne conservons que les uplets qui sont dans les deux ensembles d'uplets, en supprimant les doublons, tant que nous nous sommes assurés que les deux ensembles sont valides pour effectuer une opération d'ensemble entre eux.

Cela signifie que pour appliquer INTERSECT, nous devons nous assurer que le schéma des deux ensembles est compatible, tant au niveau du nombre de colonnes, dans ce cas 2, que de leurs types de données respectifs. Quant aux noms, nous voyons ici que le nom des attributs n'a pas d'importance, puisque le résultat conservera toujours le nom du schéma du premier ensemble de l'opération.

```pgsql
SELECT PersonFK, RentalDate 
FROM Rental 
WHERE RentalDate < '2025-01-01' 
EXCEPT ALL
SELECT PersonFK, RentalDate 
FROM Rental 
WHERE RentalDate > '2024-01-01';
```

Enfin, nous pouvons également calculer la différence entre plusieurs ensembles avec EXCEPT, qui dans certains SGBD est appelé MINUS. C'est le seul opérateur où l'ordre des ensembles compte, ce qui signifie que celui du haut écarte les uplets qui existent dans l'ensemble du bas, de sorte qu'il nous reste tous les uplets qui sont dans le premier ensemble mais pas dans le second. Comme les précédents, cet opérateur supprime également les uplets en double, donc si nous devons les conserver, nous devons ajouter ALL après l'opérateur d'ensemble.

#### Requête imbriquée (Nested query)

Nous avons parlé des requêtes imbriquées au début comme d'un moyen d'utiliser le résultat d'une requête à l'intérieur d'une autre requête. Essentiellement, c'est ce que c'est, mais SQL fournit une série d'opérateurs spécifiques qui sont utiles lors du travail avec des requêtes imbriquées dans une clause WHERE par exemple, car elles ne peuvent pas seulement être placées dans la clause FROM.

```pgsql
SELECT *
FROM (
    SELECT PersonFK,
      RentalDate
    FROM Rental
    WHERE RentalDate > '2024-01-01'
  ) AS T
WHERE T.RentalDate <= '2024-06-06';
```

Pour commencer, les requêtes imbriquées profitent du fait qu'une requête renvoie toujours une table, ce qui nous permet d'utiliser ce résultat comme une table intermédiaire dans le calcul d'une autre requête.

Par exemple, ici nous obtenons d'abord les uplets de Rental avec une date postérieure à 2024 dans la sous-requête de la clause FROM. Ensuite, dans la requête "externe", nous attribuons l'alias T au résultat de cette sous-requête, à partir duquel nous obtenons tous ses uplets avec une date antérieure au '2024-06-06'.

```pgsql
SELECT *
FROM Rental R
WHERE R.RentalDate > '2024-01-01'AND R.RentalDate <= '2024-06-06';
```

Comme vous pouvez le deviner, en faisant cela, SQL résout d'abord en interne la sous-requête dans la clause FROM. Cela signifie qu'il récupère tous les uplets que la sous-requête doit renvoyer, puis applique le filtre défini dans la clause WHERE à tous ces uplets. Ainsi, une condition est d'abord évaluée sur tous les uplets de Rental, puis une autre condition est appliquée à tous les uplets résultant de la requête. Cela crée un travail supplémentaire (calcul) pour d'abord obtenir et potentiellement stocker en mémoire les uplets de la sous-requête, puis les filtrer à nouveau.

Notez simplement que conceptuellement, une table dérivée est évaluée en premier, mais les optimiseurs peuvent réécrire/aplatir la requête – ne vous fiez donc pas à un ordre d'évaluation spécifique.

D'un autre côté, cette requête aurait pu être résolue plus simplement, comme illustré ci-dessus. Ici, la table Rental est utilisée directement dans la clause FROM, et le filtrage est appliqué avec les deux conditions sur **RentalDate** "ensemble" dans une seule clause WHERE. Cela signifie qu'il suffit de parcourir les uplets de Rental, au lieu de les parcourir puis de devoir filtrer à nouveau les uplets d'une sous-requête. Cela économise un calcul inutile ainsi que la mémoire éventuelle que le SGBD pourrait utiliser pour stocker les uplets résultant de la sous-requête en mémoire.

Avec cet exemple, nous avons vu qu'une même requête peut être résolue de manière plus ou moins efficace sur le plan informatique selon la façon dont nous prévoyons de l'implémenter. Bien que, généralement, tous les SGBD modernes disposent du composant **Optimiseur** dans leur architecture, qui applique automatiquement certaines [techniques d'optimisation](https://www.geeksforgeeks.org/dbms/advanced-query-optimization-in-dbms/) à la requête sans que nous ayons à nous en soucier. Nous n'entrerons pas dans le détail de ces techniques ici.

À son tour, l'imbrication de ces requêtes nous permet de résoudre des problèmes plus complexes à l'aide d'opérateurs tels que EXISTS. Plus précisément, nous utilisons principalement EXISTS dans une instruction WHERE avant une requête imbriquée pour vérifier si la requête imbriquée contient des uplets ou non. En d'autres termes, si nous la considérons comme un multiensemble d'uplets, EXISTS nous indique si ce multiensemble est vide ou non.

```pgsql
SELECT B.*
FROM Bike AS B
WHERE EXISTS (
    SELECT *
    FROM Rental AS R
    WHERE R.BikeFK = B.BikeID
  );
```

Par exemple, pour savoir quels vélos de Bike ont été loués au moins une fois, nous sélectionnons tous les uplets de Bike qui ont un uplet dans Rental associé au vélo que nous vérifions.

Pour comprendre cela, vous devez garder à l'esprit qu'une requête SQL est généralement exécutée en scannant les uplets des tables de haut en bas. Ainsi, la clause WHERE de la requête externe est en fait exécutée pour chaque vélo de Bike, qui est la table que nous parcourons dans la clause FROM.

Ainsi, pour chaque vélo, nous exécutons une requête imbriquée qui renvoie toutes les locations de ce vélo, car elle conserve les uplets de Rental dont la clé étrangère BikeFK pointe vers l'attribut BikeID de la table avec l'alias B. C'est ce qu'on appelle une **imbrication corrélée** car nous utilisons la table de la requête externe dans la requête imbriquée. Cela signifie que nous pourrions forcer SQL à la recalculer chaque fois que la condition WHERE est vérifiée sur un uplet de Bike (mais les moteurs la réécrivent couramment sous forme de semi-jointure, évitant une réexécution par ligne).

Grâce à cela, si la requête imbriquée contient un uplet, cela implique que le vélo a été loué au moins une fois. Et nous pouvons le détecter avec EXISTS, qui vérifie si la table résultante de la requête imbriquée renvoie un uplet.

Comme nous sommes simplement intéressés par le fait de savoir si elle contient un uplet, nous n'avons pas besoin de renvoyer d'attribut spécifique dans la requête imbriquée, bien qu'il soit généralement considéré comme une bonne pratique de renvoyer \*, ou une constante comme 1.

Une autre façon de résoudre la requête précédente avec un opérateur différent consiste à utiliser IN. Cet opérateur vérifie si une certaine valeur ou un uplet est contenu dans une colonne ou une table.

```pgsql
SELECT B.*
FROM Bike AS B
WHERE B.BikeID IN (
    SELECT Rental.BikeFK
    FROM Rental
  );
```

Par exemple, dans ce cas, nous construisons une requête imbriquée dans la clause WHERE qui contient uniquement la clé étrangère BikeFK de la table Rental, où se trouvent toutes les valeurs BikeID référencées par les uplets de location. Dans la requête externe, tous les uplets de Bike sont parcourus. Elle vérifie une condition selon laquelle le BikeID de la table Bike doit appartenir à la table résultante de la requête imbriquée pour être considéré comme un vélo ayant été loué au moins une fois.

Ainsi, pour résoudre cette requête, nous devons savoir, pour chaque vélo, si sa clé primaire BikeID est référencée par la clé étrangère correspondante de n'importe quel uplet dans Rental.

Pour cela, nous pouvons utiliser EXISTS comme auparavant pour vérifier s'il existe un uplet dans Rental qui référence la valeur de clé primaire spécifique de Bike, ou nous pouvons utiliser IN pour vérifier directement si la valeur de clé primaire BikeID du vélo que nous parcourons dans la requête externe est présente dans la colonne de clé étrangère de Rental que nous obtenons avec la requête imbriquée.

En continuant avec les manières équivalentes de résoudre la requête précédente, nous pouvons également remplacer l'opérateur IN par **=ANY**. Intuitivement, nous pouvons comprendre cela comme la vérification que la valeur B.BikeID est égale à l'une des valeurs de la colonne que nous avons obtenue avec la requête imbriquée (ce qui est équivalent à ce que fait l'opérateur IN).

```pgsql
SELECT B.*
FROM Bike AS B
WHERE B.BikeID = ANY (
    SELECT Rental.BikeFK
    FROM Rental
  );
```

En d'autres termes, conceptuellement, vérifier si quelque chose appartient à un ensemble équivaut à vérifier s'il est égal à l'un des éléments contenus dans l'ensemble. En fin de compte, l'opérateur ANY nous permet de vérifier si une certaine valeur remplit une condition par rapport à l'une des valeurs stockées dans une requête imbriquée – c'est-à-dire dans un multiensemble, puisque nous pouvons le faire avec des uplets aussi bien qu'avec des valeurs.

```pgsql
SELECT B.*
FROM Bike AS B
WHERE (1, B.BikeID) = ANY (
    SELECT R.PersonFK, R.BikeFK
    FROM Rental R
  );
```

Par exemple, au lieu de vérifier si une valeur spécifique d'un attribut unique se trouve dans la colonne de la requête imbriquée, nous pouvons effectuer la vérification avec un uplet complet.

Ici, la requête imbriquée renvoie les valeurs de clé étrangère des uplets de **Rental**, donc dans la requête externe, nous pouvons vérifier quels vélos ont été loués au moins une fois par la personne ayant la clé primaire **PersonID=1**. Ou dit autrement, pour chaque uplet de **Bike**, nous vérifions s'il existe un uplet dans la table de requête imbriquée sous la forme **(1, B.BikeID)**. Cela indiquerait que la personne ayant la clé primaire **PersonID=1** a loué le vélo au moins une fois.

Enfin, l'opérateur IN est également équivalent à l'opération **NOT <> ALL**, qui est plus compliquée à comprendre. Essentiellement, nous voulons vérifier si l'uplet (1, B.BikeID) est contenu dans le résultat de la requête imbriquée.

```pgsql
SELECT B.*
FROM Bike AS B
WHERE NOT (1, B.BikeID) <> ALL (
    SELECT R.PersonFK, R.BikeFK
    FROM Rental R
  );
```

Avec **<> ALL**, nous vérifions si l'uplet est différent de chaque uplet stocké dans la requête imbriquée. Ensuite, en niant ce résultat avec NOT, nous pouvons déterminer si cette condition n'est pas remplie (c'est-à-dire que l'uplet n'est pas différent de chaque uplet de la requête imbriquée). Cela signifierait qu'il est égal à au moins l'un d'entre eux, ou en d'autres termes, qu'il est contenu dans le multiensemble renvoyé par la requête imbriquée.

Pour comprendre l'opérateur ALL, nous pouvons essayer d'obtenir le vélo ayant le poids le plus bas dans toute la table Bike. Pour ce faire, avec une requête imbriquée, nous pouvons obtenir tous les poids de la table Bike. Ensuite, dans la requête externe, nous pouvons parcourir tous les uplets de Bike et vérifier si le poids de chacun B.Weight est inférieur ou égal à chaque poids obtenu avec la requête imbriquée à l'aide de **<= ALL**.

```pgsql
SELECT *
FROM   Bike B
WHERE  B.Weight <= ALL (
    SELECT Weight
    FROM   Bike
);
```

Si cela est vrai, alors ce poids correspondra au plus bas de toute la table, la condition WHERE sera donc TRUE, et l'uplet correspondant de Bike sera renvoyé dans notre requête externe.

En SQL, les conditions renvoient généralement des valeurs TRUE ou FALSE selon qu'elles sont remplies ou non. Mais lors de la comparaison avec des valeurs NULL, UNKNOWN est renvoyé, car il arrive qu'une requête imbriquée renvoie de manière inattendue des valeurs NULL. Cela fait que les conditions qui comparent avec ces valeurs ne donnent pas de valeurs de vérité logique, mais la valeur spéciale **UNKNOWN**.

#### JOIN (Jointure)

Les opérateurs JOIN ont également un équivalent en algèbre relationnelle. Leur objectif principal est de rassembler des informations réparties sur plusieurs tables afin que toutes les données puissent être manipulées dans une seule table intermédiaire.

Par exemple, lorsque nous regardons les informations de la table Rental, nous voyons qu'elle possède des clés étrangères référençant Bike et Person, mais la table Rental elle-même ne contient pas toutes les informations dont nous pourrions avoir besoin sur les vélos ou les personnes. Ainsi, si nous voulons interroger les locations et les noms des personnes impliquées dans ces locations, nous devrons appliquer une opération JOIN sur les deux tables.

```pgsql
SELECT *
FROM Rental, Person;
```

Il existe plusieurs types de JOIN, qui ont tous une équivalence presque directe dans les opérateurs de l'algèbre relationnelle. Le plus simple est le JOIN implicite illustré ci-dessus, qui est désigné par l'utilisation de plusieurs tables dans une instruction FROM séparées par des virgules. Nous pouvons utiliser autant de tables que nous le souhaitons ici, tant qu'il n'y a pas d'ambiguïtés dans leurs noms.

Notez que si nous effectuons un JOIN implicite d'une table avec elle-même, nous devrons attribuer des alias différents aux différentes utilisations que nous en faisons.

Avant de voir ce que fait la requête, il est utile de comprendre l'opération de produit cartésien en détail, car elle est le fondement de tous les opérateurs JOIN de SQL.

Le **produit cartésien** est une opération mathématique qui prend deux ensembles en entrée, qui en SQL sont des tables ou des multiensembles avec des uplets, tels que la table **A** avec les uplets **{{a},{b},{c}}**, et la table **B** avec les uplets **{{1},{2},{3}}**. En sortie, l'opération génère un nouveau multiensemble d'uplets où chaque ligne de A est **combinée** avec chaque ligne de B, ce qui donne la table ou le multiensemble **A×B={{a,1},{a,2},{a,3},{b,1},{b,2},{b,3},{c,1},{c,2},{c,3}}**.

Comme vous pouvez le voir, si la table **A** a **n** uplets et la table **B** a **m** uplets, le produit cartésien générera **n\*m** uplets, où chacun prend des valeurs de tous les attributs de la table **A** et de la table **B** (puisque le résultat de l'opération inclut tous les **"couplages"** possibles que nous pouvons faire entre les uplets des deux tables).

Ainsi, pour en revenir à notre requête, comme vous pouvez le voir dans le résultat, le JOIN implicite effectue le produit cartésien des deux tables. Peu importe si leurs noms se répètent, car chaque répétition peut être accédée via un alias différent.

En ce qui concerne les uplets qu'il contient, nous voyons que le produit cartésien renvoie des uplets où chaque uplet possible de Rental est combiné avec chaque uplet possible de Person. Cela forme des uplets avec des valeurs dans tous les attributs de la table **JOIN** résultante.

Le jointure implicite n'a pas de critères de filtrage ou de fonctionnalité supplémentaire – elle renvoie simplement le produit cartésien complet des tables impliquées dans l'opération.

Son nom, implicite, vient du fait que l'opérateur JOIN et le type de JOIN que nous voulons effectuer ne sont pas explicitement écrits. Au lieu de cela, il suffit de lister plusieurs tables séparées par une virgule dans la clause FROM.

En plus du JOIN implicite, nous avons également le JOIN explicite. Il peut être de plusieurs types selon le filtrage ou les conditions appliqués au produit cartésien.

Par exemple, au lieu d'effectuer un produit cartésien entre les deux tables avec une jointure implicite, nous pouvons également le faire explicitement avec un **CROSS JOIN**. Cela fait exactement la même chose mais avec une syntaxe explicite : nous spécifions l'opération JOIN à effectuer et son type, CROSS. Cela indique l'exécution d'un produit cartésien comme le précédent.

```sql
SELECT *
FROM Rental CROSS JOIN Person;
```

Outre le type CROSS, il existe d'autres types qui fournissent des fonctionnalités supplémentaires au JOIN, nous permettant de filtrer les uplets que nous obtenons d'un produit cartésien.

Par exemple, jusqu'à présent avec le produit cartésien, nous avons obtenu toutes les combinaisons d'uplets de Rental et Person. S'il y a N uplets dans Rental et M uplets dans Person, alors le produit cartésien renverra N\*M uplets – c'est-à-dire toutes les combinaisons possibles d'uplets des deux tables avec lesquelles nous travaillons.

Si nous regardons la table résultante de cette opération, nous verrons que certaines valeurs d'attributs différents comme PersonPK et PersonID correspondent dans le même uplet. Cela signifie qu'un uplet de Rental a été combiné avec un uplet de Person de sorte qu'il s'agit de la personne référencée par la clé étrangère dans Rental. En d'autres termes, nous avons un uplet qui contient non seulement les informations de Rental mais possède également les informations de l'uplet Person représentant la personne qui a effectué cette location – et il a été "concaténé" ou combiné avec lui.

Ainsi, si nous voulons ne conserver que les uplets du produit cartésien où PersonFK correspond à PersonID de la table Person, nous pourrions appliquer une condition dans une clause WHERE pour filtrer ces uplets. Mais en faisant cela, conceptuellement, il s'agit d'un produit cartésien suivi d'un filtre, mais l'optimiseur le réécrit généralement en une jointure interne équivalente sans matérialiser le produit complet.

Il existe des types spécifiques de JOIN qui peuvent nous aider à effectuer ce filtrage plus efficacement :

```pgsql
SELECT *
FROM Rental AS R CROSS JOIN Person AS P
WHERE R.PersonFK=P.PersonID;

SELECT *
FROM Rental R INNER JOIN Person AS P ON R.PersonFK=P.PersonID;
```

Pour implémenter cette requête, nous pouvons utiliser une condition dans une clause WHERE, ou nous pouvons utiliser un INNER JOIN, qui nous permet de fixer une condition dans la clause ON.

Si nous utilisons une clause WHERE, nous filtrerons tous les uplets obtenus à partir du produit cartésien complet résultant du CROSS JOIN à l'aide d'une condition. Mais pour éviter de créer l'intégralité du produit cartésien (ce qui n'est pas efficace), nous pouvons utiliser un INNER JOIN explicite. Ici, nous pouvons fournir une condition dans la clause ON afin que seuls les uplets du produit cartésien qui remplissent cette condition soient réellement construits.

Dans la clause ON d'un INNER JOIN, nous pouvons mettre n'importe quel type de condition sur les uplets que nous voulons obtenir. Mais il arrive que ces conditions soient simples et n'impliquent que l'égalité entre des attributs, qui peuvent même avoir le même nom.

```pgsql
SELECT *
FROM Person P1 CROSS JOIN Person P2
WHERE P1.PersonID=P2.PersonID;

SELECT *
FROM Person P1 INNER JOIN Person P2 ON P1.PersonID=P2.PersonID;
```

Par exemple, si nous effectuons le produit cartésien entre la table Person et elle-même, et que nous voulons ne conserver que les uplets où les attributs PersonID des deux tables correspondent, nous pouvons utiliser un INNER JOIN avec la condition que les PersonID des deux tables combinées soient égaux. De cette façon, seuls les uplets qui remplissent cette condition seront construits (contrairement à la requête précédente où l'utilisation d'un CROSS JOIN implique la construction de tous les uplets du produit cartésien, ce qui nécessite plus de calcul).

Dans ces types de situations, au lieu d'utiliser un INNER JOIN, nous pouvons profiter d'un autre type de JOIN comme le NATURAL JOIN. Celui-ci ne renvoie que les uplets où les valeurs de tous les attributs ayant le même nom correspondent.

```pgsql
SELECT *
FROM Person P1 NATURAL JOIN Person P2;

SELECT *
FROM Person P1
  NATURAL JOIN (
    SELECT PersonID,
      Name AS Name2,
      Birth AS Birth2,
      Email AS Email2
    FROM Person
) AS P2;
```

Pour comprendre cela, nous pouvons effectuer un NATURAL JOIN entre la table Person et elle-même. Tout d'abord, si nous ne renommons aucun attribut, alors tous auront le même nom dans les deux tables – le NATURAL JOIN imposera donc une condition d'égalité pour chaque attribut. Cela signifie qu'il ne renverra que les uplets qui satisfont **P1.PersonID=P2.PersonID**, **P1.Name=P2.Name**, etc. pour le reste des attributs, puisqu'ils ont le même nom bien qu'ils soient dans des tables avec des alias différents. Cela donnera la même table Person, car le NATURAL JOIN, en plus d'imposer ces conditions, "fusionne" les attributs qui remplissent ces conditions. Ainsi, s'ils ont le même nom, il n'en laisse qu'une seule occurrence, et non les deux (comme cela se produit dans d'autres types de JOIN).

Mais si nous renommons les attributs de l'une des tables à l'exception de PersonID, nous verrons que NATURAL JOIN impose uniquement la condition d'égalité **P1.PersonID=Person.PersonID**, puisque PersonID est le seul attribut qui est exactement le même dans les deux tables.

Dans la table résultante, nous obtiendrons la même chose qu'auparavant mais avec les attributs renommés inclus, car ils ne sont pas écartés ou soumis à une condition qui les rend inutiles. Même si nous renommons également PersonID, nous obtiendrons le produit cartésien de Person avec elle-même – car si aucun des attributs n'a le même nom dans les deux tables, alors NATURAL JOIN n'impose aucune condition d'égalité.

Une autre option que nous avons pour imposer des conditions d'égalité sur des attributs ayant le même nom dans les deux tables consiste à utiliser un INNER JOIN. Au lieu de déclarer des conditions dans une clause ON, nous utilisons une clause USING où nous définissons les attributs sur lesquels les conditions d'égalité sont imposées. Ceux-ci doivent avoir exactement le même nom dans les deux tables. Sinon, le SGBD pourrait générer une erreur.

```pgsql
SELECT *
FROM Person P1 INNER JOIN Person P2 USING (PersonID);
```

Par exemple, dans la requête ci-dessus, nous obtenons les uplets du produit cartésien de Person avec elle-même qui satisfont **P1.PersonID=P2.PersonID**.

La différence principale avec NATURAL JOIN est que NATURAL JOIN tente d'imposer cette condition d'égalité sur tous les attributs possibles ayant le même nom. Mais avec un INNER JOIN et USING, nous décidons quelles conditions d'égalité sont imposées sur quels attributs (tant qu'ils ont le même nom dans les deux tables).

De plus, lorsque nous utilisons USING en combinaison avec un INNER JOIN, une seule occurrence des attributs ayant le même nom apparaît dans la table résultante, tout comme avec NATURAL JOIN.

Enfin, il est important de noter que lors de l'utilisation de ON pour déclarer une condition, aucun attribut n'est supprimé de la table résultante de l'**opération JOIN**, car la condition peut être **très diverse** par nature. Cela signifie qu'elle ne doit pas nécessairement être une égalité entre plusieurs attributs.

Mais lorsque vous utilisez USING en combinaison avec un INNER JOIN (et imposez une condition d'égalité sur les attributs déclarés dans la clause USING), toutes les répétitions de ces attributs seront supprimées de la table résultante. Ainsi, si nous imposons une condition d'égalité sur plusieurs attributs ayant le même nom, toutes leurs occurrences sauf une seront supprimées.

Par exemple, dans une table avec deux attributs appelés PersonID mais provenant de tables différentes ou d'éléments avec des alias différents (même table Person mais alias différent), USING supprimerait l'une de leurs occurrences. Cela ne laisserait qu'un seul attribut PersonID dans la table JOIN résultante, alors que ON ne supprimerait aucune des occurrences. Et cela ferait en sorte que la table finale contienne les deux attributs PersonID originaux.

```pgsql
SELECT *
FROM Person P LEFT JOIN Rental R ON R.PersonFK = P.PersonID;
```

En continuant avec les types de JOIN, il pourrait y avoir un cas où une personne n'a jamais loué de vélo, il n'y aura donc aucun uplet dans la table Rental référençant cette personne. C'est possible en raison des multiplicités minimales du côté de Rental dans le diagramme entité-relation (qui n'exigent pas qu'une personne ait loué un vélo).

Ainsi, si nous voulons construire une table qui affiche des informations sur toutes les personnes ainsi que des informations sur toutes les locations qu'elles ont effectuées, la première chose à laquelle nous pourrions penser est d'effectuer un INNER JOIN entre elles. Et nous ajouterions une certaine condition d'égalité sur l'attribut de clé étrangère de Rental qui référence la clé primaire de la table Person.

Mais il peut y avoir des personnes qui n'ont jamais loué de vélo, donc si nous faisons un INNER JOIN, les informations sur ces personnes n'apparaîtront pas dans la table. Pour s'assurer qu'elles apparaissent, nous devons utiliser un OUTER JOIN au lieu d'un INNER JOIN. Nous devons également spécifier quelle table nous voulons forcer à faire apparaître ses données en mettant LEFT ou RIGHT avant le type de **OUTER JOIN** (ou nous pouvons simplement utiliser **LEFT JOIN**, par exemple).

De cette façon, si nous utilisons LEFT JOIN, nous forçons les données de la table à gauche du JOIN à apparaître dans la table résultante. Si elles n'ont pas de correspondance dans la table de droite (ce qui signifie qu'elles n'ont pas de location), alors les autres attributs seront remplis avec des valeurs NULL, comme nous l'avons vu dans le résultat de la requête précédente.

```pgsql
SELECT *
FROM Rental R RIGHT OUTER JOIN Person P ON R.PersonFK = P.PersonID;
```

De la même manière, si nous utilisons RIGHT JOIN et inversons l'ordre des tables, nous ferons la même chose mais forcerons les données de la table de droite à apparaître dans la table résultante, en remplissant les attributs de la table de gauche avec NULL au cas où il n'y aurait pas de correspondance.

Avec Rental RIGHT JOIN Person, toutes les personnes apparaissent – pour les personnes sans location, le côté Rental sera NULL.

Enfin, si nous voulons utiliser à la fois RIGHT et LEFT dans une jointure et forcer les données des deux tables à apparaître (ce qui remplirait NULL du côté correspondant à chaque uplet), nous pouvons utiliser un FULL JOIN.

```pgsql
SELECT *
FROM Person P JOIN Rental R ON R.PersonFK = P.PersonID;
```

Dans ce dernier type de JOIN, nous avons vu que spécifier OUTER est facultatif lors de l'utilisation de RIGHT, LEFT ou FULL. Mais par défaut, si rien n'est spécifié, l'opérateur JOIN est traité comme un type INNER, nécessitant une condition avec ON ou USING par la suite.

#### Agrégation

Avec les jointures, nous pouvons maintenant combiner plusieurs tables et rassembler leurs informations en une seule. Mais il y a encore certaines opérations que nous ne pouvons pas faire facilement, comme compter les lignes d'une table, additionner les valeurs d'une colonne, calculer leur moyenne, etc.

Toutes les opérations de cette nature qui impliquent des valeurs d'un multiensemble (table) d'uplets sont appelées opérations d'agrégation. Leur but est d'effectuer un calcul sur une série d'uplets et elles constituent la base des requêtes analytiques.

```pgsql
SELECT COUNT(*) AS rentalCount,
  SUM(Price) AS income,
  AVG(Price) AS averageRentalPrice,
  MAX(Price) AS maxRentalPrice,
  MIN(Price) AS minRentalPrice
FROM Rental;
```

SQL en propose un certain nombre (qui n'ont pas d'équivalent direct avec les opérateurs de l'algèbre relationnelle) : COUNT(), SUM(), AVG(), MIN() et MAX().

#### COUNT()

Nous pouvons utiliser COUNT() pour compter le nombre de lignes dans une table, y compris les uplets où toutes les valeurs sont NULL. Ainsi, en déclarant COUNT(\*) dans la clause SELECT, nous obtiendrons le nombre d'uplets dans la table spécifiée dans la clause FROM.

```pgsql
SELECT COUNT(*), COUNT(Price), COUNT(DISTINCT Price)
FROM Rental;
```

Mais la fonction peut également effectuer une agrégation sur une colonne spécifique. Ainsi, au lieu de compter les uplets, elle compte le nombre de valeurs existantes dans un certain attribut, y compris les valeurs en double et en ignorant les NULL.

Donc, si nous voulons compter uniquement le nombre de valeurs distinctes dans Price, nous pouvons utiliser DISTINCT comme illustré ci-dessus.

Quant aux noms de colonnes que nous obtenons de ces opérations, il n'est pas obligatoire de leur attribuer un alias et de les renommer, mais c'est très pratique pour identifier quel calcul est stocké dans chaque colonne de la table résultante.

```pgsql
SELECT COUNT(*) 
FROM (SELECT DISTINCT PersonFK, BikeFK FROM Rental) AS t;
```

En plus d'un attribut unique, COUNT() peut compter le nombre de combinaisons de valeurs d'un certain ensemble d'attributs présentes dans la table. Plus précisément, dans cet exemple, nous comptons combien de valeurs **(PersonFK, BikeFK)** se trouvent dans la table. Cela peut ne pas correspondre au nombre total d'uplets puisque les NULL sont ignorés ici, contrairement à l'opération **COUNT(\*)** où ils sont également pris en compte. Nous pouvons également utiliser DISTINCT ici, tant que les attributs dont nous voulons compter les combinaisons de valeurs sont entre parenthèses.

```pgsql
SELECT SUM(2*Price), AVG(Price)
FROM Rental;
```

#### SUM()

**SUM()** calcule la somme d'un certain attribut numérique d'une table, ou d'un attribut pouvant être converti en numérique. Elle prend en entrée l'attribut dont nous voulons obtenir la somme de toutes les valeurs présentes dans la table. Notez que, outre l'attribut, SUM() accepte des expressions qui aboutissent à un attribut unique. C'est-à-dire que si au lieu de **Price** nous fournissons **2\*Price, ou Price+Price**, alors ces opérations additionneront une série d'attributs dont le résultat sera stocké dans un attribut unique. Celui-ci est donné en entrée à SUM().

Si toutes les valeurs de l'attribut sont NULL, SUM() renvoie 0. Contrairement à COUNT(), dans ce cas, nous ne pouvons pas additionner plusieurs attributs à la fois, ce qui signifie que SUM() ne prend qu'un seul attribut en entrée, que nous l'obtenions ou non via une expression arithmétique.

#### AVG()

De même, AVG() calcule la moyenne des valeurs prises par un attribut unique, en ignorant les NULL. Contrairement à SUM(), cette fonction renvoie NULL lorsque toutes les valeurs de l'attribut d'entrée sont NULL, car elle peut être calculée en interne comme **SUM()/COUNT()**.

Ainsi, si SUM() renvoie 0 lors du comptage d'un attribut rempli de NULL et que COUNT() ignore ces valeurs NULL, la moyenne sera 0/0, ce qui est indéfini – ce qui fait que AVG() renvoie NULL. Il est également important de noter que si nous utilisons DISTINCT, la somme et la moyenne seront toutes deux différentes.

```pgsql
SELECT MIN(Price), MAX(Price)
FROM Rental;
```

#### MIN() et MAX()

Enfin, les opérations MIN() et MAX() prennent un attribut en entrée et renvoient respectivement la valeur minimale ou maximale trouvée dans les uplets stockés dans la table. Si toutes les valeurs de cet attribut sont NULL, elles renvoient également NULL, car une valeur minimale ou maximale cohérente ne peut pas être établie puisque les NULL sont ignorés.

#### GROUP BY

Si nous essayons d'utiliser des fonctions d'agrégation dans la clause SELECT avec d'autres attributs, le SGBD nous donnera une erreur car ces types de fonctions sont généralement utilisés avec l'instruction GROUP BY (celle-ci n'a pas non plus d'équivalent direct en algèbre relationnelle).

Pour comprendre le fonctionnement de GROUP BY, nous pouvons calculer la somme de tous les prix de location qu'une certaine personne a effectués dans le système.

```pgsql
SELECT SUM(Price)
FROM Rental R
WHERE R.PersonFK=5;
```

Pour ce faire, nous accédons à la table Rental et utilisons une clause WHERE pour filtrer tous les uplets de location d'une certaine personne à l'aide de sa clé étrangère qui référence la personne effectuant la location. Ensuite, avec SUM, nous obtenons la somme de l'attribut Price de la table finale, qui contient les prix de toutes les locations effectuées par cette personne.

Si nous voulions le faire par nom au lieu de PersonID, nous devrions faire un JOIN avec la table Person et filtrer par l'attribut Name de Person (bien que cela ne soit pas important pour comprendre GROUP BY).

```pgsql
SELECT SUM(Price) AS PriceSum
FROM Rental R INNER JOIN Person P ON R.PersonFK=P.PersonID
WHERE P.Name='Carol King';
```

Maintenant, si nous voulons calculer cette valeur pour le reste des personnes de la base de données qui ont déjà loué un vélo au moins une fois, nous devrions exécuter cette requête plusieurs fois pour chaque personne du système, ce qui n'est pas pratique. Au lieu de cela, nous pouvons profiter du fait que la table Rental elle-même possède la clé étrangère PersonFK pour les personnes ayant loué des vélos – et nous pouvons l'utiliser pour calculer cette somme pour toutes ces personnes plus simplement à l'aide de GROUP BY.

```pgsql
SELECT R.PersonFK, SUM(Price) AS PriceSum 
FROM Rental R 
GROUP BY R.PersonFK;
```

Comme vous pouvez le voir, cette requête renvoie toutes les personnes qui ont déjà loué un vélo – c'est-à-dire celles référencées dans la table Rental. Pour chacune d'elles, elle calcule la somme des prix de leurs locations. Cela est possible grâce à GROUP BY, qui regroupe tous les uplets de la table Rental par l'attribut PersonFK.

Comme chaque personne peut avoir plusieurs locations dans la table Rental, nous devons obtenir tous les uplets qui référencent chaque personne et les regrouper afin de pouvoir effectuer une opération d'agrégation comme SUM() sur l'un des attributs.

Dans ce cas, nous effectuons le regroupement avec l'attribut PersonFK, qui identifie la personne ayant effectué la location. Ainsi, puisque tous les uplets de Rental ayant la même valeur dans cet attribut appartiennent à la même personne, ils sont regroupés par cet attribut pour former des groupes d'uplets, un pour chaque personne.

Grâce à cela, nous pouvons ensuite renvoyer l'attribut qui a été regroupé (qui doit être inclus dans le SELECT lors de l'utilisation de GROUP BY) ainsi que les résultats des opérations d'agrégation calculés sur ces groupes.

```pgsql
SELECT DISTINCT Price
FROM Rental;

SELECT Price
FROM Rental
GROUP BY Price;
```

Lorsque nous utilisons GROUP BY et partitionnons les uplets de la table en groupes, chaque groupe est "identifié" ou représenté par une valeur de l'attribut par lequel nous regroupons. Cela signifie que lorsque nous renvoyons un résultat à l'utilisateur, pour **chaque groupe**, il reçoit un seul **uplet** où l'attribut utilisé pour le regroupement prend la valeur du "représentant" de ce groupe, au lieu de recevoir plusieurs uplets par groupe.

Par exemple, pour obtenir tous les prix distincts de la table Rental, nous pouvons utiliser directement DISTINCT, ou nous pouvons également regrouper par cet attribut, ce qui aboutit à la formation de différents groupes d'uplets, un pour chaque prix distinct. Enfin, lors du renvoi de Price après le regroupement, les valeurs distinctes de Price qui forment les différents groupes d'uplets sont renvoyées, ce qui signifie que seules les valeurs de Price distinctes sont obtenues.

Il convient également de noter que nous pouvons regrouper par plusieurs attributs à la fois, et pas seulement un seul. Dans ce cas, nous générerions des groupes d'uplets basés sur les combinaisons uniques de valeurs que ces attributs prennent dans la table.

Enfin, lorsque nous utilisons l'instruction GROUP BY dans une requête, nous pourrions vouloir filtrer et ne conserver que les uplets dont les résultats des opérations d'agrégation remplissent une certaine condition. Par exemple, pour obtenir uniquement les personnes dont la somme totale des prix de location est supérieure à 100, nous pourrions penser à utiliser une clause WHERE avec la condition suivante :

```pgsql
SELECT R.PersonFK, SUM(Price) AS PriceSum
FROM Rental R
WHERE PriceSum > 100
GROUP BY R.PersonFK;

SELECT R.PersonFK, SUM(Price) AS PriceSum
FROM Rental R
GROUP BY R.PersonFK
HAVING SUM(Price) > 100;
```

Mais si nous utilisons cette condition dans la clause WHERE, le SGBD nous donnera une erreur car nous ne pouvons pas imposer de conditions sur les calculs d'agrégation dans les groupes dans une clause WHERE. Nous ne pouvons pas non plus les désigner par l'alias que nous leur donnons, puisque l'alias est appliqué à la fin de la requête lorsque le résultat est fourni à l'utilisateur.

Ainsi, au lieu d'utiliser WHERE, lorsque nous voulons implémenter ce type de condition, nous utilisons HAVING. Au lieu de l'alias, nous utilisons l'expression SUM(Price) elle-même pour désigner la somme de Price dans chaque groupe. L'utilisation de WHERE n'est pas interdite, car avant d'effectuer le regroupement, nous pouvons filtrer les données qui apparaissent dans la table FROM, regroupant ainsi moins d'uplets.

#### ORDER BY

Enfin, si nous voulons trier les uplets d'une table, nous pouvons utiliser la clause ORDER BY. Elle nous permet de spécifier un ou plusieurs attributs sur lesquels le tri est effectué ainsi qu'une direction (qui peut être ASC ou DESC pour l'ordre croissant ou décroissant, respectivement).

```pgsql
SELECT *
FROM Person
ORDER BY Name ASC;

SELECT *
FROM Person
ORDER BY (PersonID, Name) ASC;
```

Dans le tri, certains attributs ont une priorité plus élevée. Ceux que nous plaçons plus à gauche sont triés en premier, comme dans cette dernière requête qui trie les uplets de Person par leurs valeurs PersonID puis par nom.

Ainsi, en utilisant toutes ces clauses, nous pouvons commencer à faire des requêtes SQL pour obtenir presque n'importe quel type de résultat dont nous avons besoin. Comme nous l'avons vu, les requêtes sont composées d'une série d'instructions ou de clauses où chacune effectue une certaine action sur les uplets d'une table.

Ces instructions suivent généralement un **ordre d'apparition dans la requête** qu'il est important de respecter pour éviter les erreurs du SGBD. L'ordre est le suivant :

1. `SELECT`
2. `FROM`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `ORDER BY`

Mais à bas niveau, l'exécution de ces instructions ou des opérateurs d'algèbre relationnelle équivalents suit un ordre différent de celui que nous utilisons lors de l'écriture de la requête. Il est le suivant :

1. `FROM`
2. `JOIN … ON`
3. `WHERE`
4. `GROUP BY`
5. `HAVING`
6. `SELECT`
7. `ORDER BY`

Tout d'abord, les données sont récupérées d'une table avec la clause FROM, qui peut nécessiter d'effectuer certaines opérations JOIN entre plusieurs tables pour que les données soient prêtes. Ensuite, les données sont filtrées à l'aide des conditions que nous avons fixées dans la clause WHERE, si nous l'utilisons. Après cela, les uplets sont regroupés et filtrés à nouveau si nous utilisons GROUP BY. Enfin, la clause SELECT est appliquée pour extraire les attributs qui nous intéressent de la table finale, que nous renommons et trions si nécessaire.

Ainsi, comme vous pouvez le voir, lorsque nous écrivons une requête SQL, nous devons utiliser les clauses dans un ordre spécifique. Mais nous devons garder à l'esprit que le SGBD, au niveau physique et du stockage, n'exécute pas ces instructions dans le même ordre que celui où nous les écrivons. En fait, nous n'avons pas à trop nous soucier de cet ordre interne car il est [transparent](https://stackoverflow.com/questions/17384020/what-do-transparent-and-opaque-mean-when-applied-to-programming-concepts) (c'est-à-dire géré automatiquement et caché) pour l'utilisateur. Cela signifie que nous n'avons pas de contrôle direct et que nous ne "voyons" pas comment l'exécution des clauses est effectuée en interne par le SGBD, sauf à inspecter le plan avec `EXPLAIN/EXPLAIN ANALYZE`.

En ce qui concerne l'ordre d'exécution interne, le SGBD réordonne, combine ou transforme généralement les clauses en d'autres, tout en construisant un plan d'exécution physique pour la requête. Cela implique de générer un plan pour les opérations et les ressources internes nécessaires pour l'exécuter de manière optimale (d'où le réordonnancement).

Il est important de le savoir lors de la construction d'une requête, car la façon dont vous la programmez peut affecter l'efficacité de la requête, même si le SGBD peut aider en automatisant une grande partie du processus d'optimisation. Vous n'êtes pas obligé d'utiliser toutes ces instructions dans une requête, bien sûr. Mais celles que vous utilisez doivent respecter l'ordre dans lequel elles doivent être écrites, sinon le SGBD finira probablement par renvoyer une erreur.

### Vues

Pour en finir avec le DML, examinons une application possible des requêtes lors de la définition d'éléments DDL en SQL. À l'origine, nous avons vu que les instructions DDL nous permettaient de créer des bases de données, des tables et des éléments similaires. L'un d'entre eux mérite d'être souligné : les **vues**, qui sont des tables virtuelles nous permettant d'abstraire les informations des tables d'une base de données.

Notre base de données est composée d'un schéma ou d'un ensemble de tables où les informations sont stockées, mais nous pourrions avoir besoin de "voir" ces informations différemment de la façon dont elles sont définies dans le schéma lui-même. Pour cela, nous définissons une vue qui nous permet d'interroger ces informations à partir de la base de données en utilisant une structure différente de celle utilisée pour les stocker.

```pgsql
CREATE VIEW RentalOverview AS
SELECT P.PersonID AS PersonID,
  P.Name AS ClientName,
  CURRENT_DATE - P.Birth AS ClientAge,
  B.BikeID AS BikeID,
  B.Model AS BikeModel,
  R.RentalDate AS RentalDate,
  R.Duration AS RentalDurationDays,
  R.Price AS RentalTotalPrice
FROM Rental R
  JOIN Person P ON R.PersonFK = P.PersonID
  JOIN Bike B ON R.BikeFK = B.BikeID;
SELECT *
FROM RentalOverview;
```

Par exemple, dans notre base de données, nous avons les tables Rental, Bike et Person, mais pour des raisons de commodité ou d'exigences, nous pourrions avoir besoin de voir toutes ces informations des tables intégrées dans une seule table avec les attributs **(PersonID, ClientName, ClientAge, BikeID, BikeModel, RentalDate, RentalDurationDays, RentalTotalPrice)**.

Par défaut, chaque fois que nous voudrions voir ces informations intégrées, nous devrions exécuter manuellement une requête (ou plusieurs, selon les circonstances) pour obtenir et intégrer ces informations dans une table.

Mais pour simplifier ce processus, il existe des vues qui nous permettent de définir une **table "virtuelle"** contenant les informations intégrées. Ainsi, chaque fois que nous avons besoin de ces informations intégrées, nous pouvons nous référer à la table virtuelle (et celle-ci est construite à l'aide de la requête que nous aurions dû exécuter manuellement pour la construire). Cette requête est la **définition** avec laquelle nous déclarons une **vue**, et la vue elle-même nous évite d'avoir à l'exécuter manuellement pour obtenir les informations intégrées.

C'est pourquoi nous créons une nouvelle vue dans la base de données qui agit comme une **table virtuelle** (ce qui signifie qu'elle ne stocke pas réellement d'informations). En effet, une vue est une table qui reçoit les requêtes des utilisateurs, mais pour les résoudre, elle doit aller chercher les informations dans différentes tables de la base de données.

Ainsi, comme vous pouvez le voir dans la vue ci-dessus, la table virtuelle RentalOverview est définie avec une requête SQL sur les tables qui stockent réellement les informations. Ainsi, lorsque nous interrogeons RentalOverview, le SGBD transforme en fait notre requête en utilisant la définition de la vue pour obtenir l'attribut ClientName, par exemple, qui est défini comme le nom de la personne ayant loué un vélo.

Dans ce cas précis, notre vue rassemble toutes les informations des trois tables en une seule, de sorte que lorsque nous l'interrogeons, nous avons les informations complètes sur la personne, le vélo et la location qui a eu lieu. Nous n'avons pas à effectuer les JOIN nous-mêmes, car ils font partie de la définition de la vue.

```pgsql
SELECT *
FROM RentalOverview;
```

En interrogeant la table virtuelle, nous obtiendrons des informations dérivées des tables de base, qui nous sont présentées selon le schéma que nous avons défini dans la vue. Par exemple, dans la base de données, la date de naissance des personnes est stockée dans l'attribut Birth. Mais la vue affiche cette donnée différemment, affichant l'âge au lieu de la date de naissance. Les deux se réfèrent à la même information mais sont vues de manières différentes.

### Administration de base de données

Au niveau logique où nous implémentons la base de données avec SQL, nous devons effectuer une maintenance continue de la base de données (en plus de la modélisation, de la modification et de l'interrogation des données). Cela garantit que nos données et services sont disponibles, optimise les performances des requêtes et fournit certaines garanties de sécurité et d'intégrité. Ce processus fait partie de ce qui est considéré comme l'**administration de base de données**, qui est une tâche effectuée par des experts.

#### Utilisateurs de la base de données

Avant d'introduire le concept d'administration, parlons des différents types d'utilisateurs qui pourraient utiliser une base de données. Chacun d'eux a un certain objectif, des responsabilités et des compétences.

Pour commencer, nous avons l'**utilisateur client**, qui utilise les services fournis par la base de données. Nous pouvons voir ce type d'utilisateur comme un utilisateur moyen d'applications mobiles ou web, ou sur n'importe quelle plateforme, utilisant une série de services qui impliquent une base de données.

Ensuite, nous avons l'**utilisateur développeur**, qui se consacre à l'implémentation technique de l'infrastructure, tant logicielle que matérielle, qui supporte les applications et les services. Les utilisateurs développeurs sont également responsables de la définition de la logique métier de la base de données, de sa structure, de ses exigences, etc. En résumé, ils suivent les différentes étapes de conception que nous avons vues au début, en particulier la conception conceptuelle et logique, bien qu'ils n'interagissent pas avec le SGBD. Ils proposent simplement le schéma que les données doivent suivre pour qu'un spécialiste l'implémente sur un SGBD.

Ce spécialiste est l'**utilisateur administrateur de base de données**, qui est responsable de l'implémentation de la conception logique de la base de données sur un SGBD. Pour ce faire, il effectue des tâches telles que le choix du SGBD approprié pour le projet en question, son installation et sa mise à jour. Il crée la base de données, les tables et les autres éléments logiques, gère la sécurité du SGBD en définissant des rôles, des autorisations et des politiques de sécurité, et surveille les performances de la base de données pour assurer sa disponibilité. Il fournit également un support technique aux autres types d'utilisateurs et définit des protocoles de sauvegarde des données.

Ainsi, fondamentalement, l'administrateur est en charge de l'implémentation pendant l'étape de conception logique, ainsi que des étapes ultérieures de conception physique et de stockage éventuelles. Il est également responsable de la maintenance du SGBD. Parmi toutes ces tâches, l'une des plus critiques est l'optimisation des requêtes que les utilisateurs pourraient faire au système et l'affinement des schémas si nécessaire pour améliorer les performances.

#### Métadonnées de la base de données

Jusqu'à présent, nous avons seulement considéré que la base de données est responsable du stockage des informations (données). Celles-ci sont finalement générées par le projet ou l'application que la base de données supporte, comme les uplets des tables.

Mais en plus de ces données, la base de données contient une série de métadonnées utilisées pour gérer les données. Essentiellement, les métadonnées servent principalement à décrire une autre donnée ou à fournir des informations supplémentaires qui aident à l'organiser au sein de la base de données. Voici un exemple :

| **Nom** | **Naissance** | **Email** |
| --- | --- | --- |
| Alice Johnson | 1985-07-12 | alice.johnson@example.com |
| Bob Smith | 1990-03-05 | bob.smith@example.org |
| Carol Davis | 1978-11-23 | carol.davis@example.net |
| David Brown | 2001-01-30 | david.brown@example.com |
| Emily Wilson | 1995-09-14 | emily.wilson@example.co.uk |

Pour comprendre l'idée de métadonnées, nous pouvons introduire le concept de schéma en tant que métadonnées. Dans une table, nous avons un nom de table, qui est une métadonnée décrivant la table. Cela nous permet de savoir à quelle table nous nous référons lors de l'utilisation de ce nom dans une requête ou d'autres situations.

Outre le nom, toutes les tables ont un en-tête composé des noms des attributs situés dans la première ligne, qui constituent le schéma de la table. Ces noms sont utilisés pour désigner les attributs ou les colonnes, tout comme le nom de la table est utilisé pour désigner la table elle-même en tant qu'objet. Le schéma fait donc partie des métadonnées, car il donne un sens aux données stockées dans les colonnes, permettant de les organiser.

En d'autres termes, si nous n'avions pas la première ligne avec les noms d'attributs, nous n'aurions aucune information sur les données stockées, car nous manquerions de leur sémantique. C'est précisément ce que le schéma fournit en tant que métadonnées, ce qui nous permet de les gérer.

En dehors des noms de tables et d'attributs, les tables ont généralement des métadonnées techniques associées provenant du SGBD. Ces métadonnées indiquent les utilisateurs qui possèdent la table ou ont certaines autorisations pour effectuer des actions sur celle-ci. Elles contiennent également les dates de création et de dernière modification de la table pour assurer la sécurité des données, les connexions existantes ou des informations sur les événements ou les verrous pour la gestion de la concurrence.

La table en tant qu'objet ne stocke pas son nom et toutes ses métadonnées en elle-même, mais plutôt dans des endroits spécifiques au sein du SGBD. Ces endroits spécifiques sont des tables réservées au SGBD appelées dictionnaires, ou parfois catalogues. Ils utilisent la nature structurée du SGBD pour stocker ces métadonnées de manière simple, similaire au stockage des données réelles.

Comme ces endroits sont des tables, ils ont également un nom, un schéma et des métadonnées, stockés dans le SGBD dans des structures de données physiques, et non dans d'autres tables. Quant à leurs schémas, ils sont spécifiquement appelés méta-schémas.

Les métadonnées dans un SGBD varient considérablement selon le SGBD spécifique que nous utilisons. Mais dans tous, nous trouverons toujours des informations fondamentales sur la base de données que nous avons implémentée, comme son nom, les noms des tables, les schémas, les contraintes, etc.

Plus précisément, dans PostgreSQL, nous pouvons les trouver dans les "schémas" **pg\_catalog** et **information\_schema**. Ici, PostgreSQL désigne par "schéma" un conteneur logique qui contient certaines tables, vues et éléments similaires d'une base de données, dont beaucoup sont responsables du stockage des métadonnées. Un conteneur logique n'est donc rien de plus qu'un dossier utilisé pour grouper des éléments afin de les rendre plus hiérarchisés et organisés.

D'une part, **pg\_catalog** est le catalogue interne de PostgreSQL, ce qui signifie qu'il contient toutes les informations nécessaires pour gérer le fonctionnement du SGBD. Mais ce catalogue est très technique et dense, car il vise à gérer l'intégralité du fonctionnement du système, impliquant de nombreux détails qui ne sont pas toujours nécessaires pour un administrateur.

C'est pourquoi il existe une abstraction standard de ce conteneur logique appelée **information\_schema**, introduite avec la norme SQL-92, qui sert principalement à abstraire les détails spécifiques liés au fonctionnement du SGBD et à fournir à l'administrateur de la base de données une série de vues pour mieux visualiser et gérer les métadonnées.

Pour savoir ce que contient pg\_catalog, vous pouvez utiliser des commandes comme **\dt pg\_catalog.\*** pour voir les tables, les vues ou généralement les éléments qu'il contient. Parmi tous, les plus importants sont :

* **pg\_catalog.pg\_class :** Stocke les métadonnées des objets de la base de données, tels que les tables ou les vues, entre autres.
    
* **pg\_catalog.pg\_namespace :** Stocke les noms des schémas (conteneurs logiques) du SGBD.
    
* **pg\_catalog.pg\_attribute :** Stocke les noms des attributs des tables ou des vues, c'est-à-dire leurs schémas, ainsi que leurs types de données ou les domaines définis par l'utilisateur.
    
* **pg\_catalog.pg\_type :** Stocke les types de données par défaut et les types définis par l'utilisateur.
    
* **pg\_catalog.pg\_attrdef :** Stocke les valeurs par défaut définies pour les attributs.
    
* **pg\_catalog.pg\_constraint :** Stocke les définitions des contraintes sur les tables, telles que PRIMARY KEY, UNIQUE, FOREIGN KEY, CHECK et EXCLUSION, incluant des informations sur la table à laquelle elles s'appliquent (conrelid), les colonnes impliquées (conkey), les actions de mise à jour et de suppression sur les clés étrangères (confupdtype, confdeltype), et le nom de la contrainte (conname), entre autres.
    
* **pg\_catalog.pg\_stat\_activity :** Fournit des informations en temps réel sur les sessions actives sur le serveur PostgreSQL.
    

Comme vous pouvez le voir, si nous explorons le contenu de pg\_catalog, nous constaterons qu'il est très dense et détaillé. C'est pourquoi nous avons l'alternative standard **information\_schema**, qui simplifie la gestion des métadonnées. Il fonctionne de manière similaire à pg\_catalog, servant de conteneur logique qui fournit des vues des tables du SGBD que nous avons vues auparavant pour abstraire leur fonctionnalité.

Les plus significatives sont :

* **information\_schema.tables :** Stocke une liste de toutes les tables et vues de la base de données.
    
* **information\_schema.columns :** Stocke les métadonnées de toutes les colonnes de toutes les tables et vues.
    
* **information\_schema.table\_constraints :** Stocke une liste de toutes les contraintes au niveau de la table (clé primaire, unique, étrangère, check...).
    
* **information\_schema.key\_column_usage :** Stocke une liste des colonnes impliquées dans les contraintes de clé (primaire, unique ou étrangère).
    
* **information\_schema.referential\_constraints :** Stocke les métadonnées sur les contraintes FOREIGN KEY, telles que les actions déclenchées après une suppression ou une mise à jour, entre autres.
    

Pour interroger les informations contenues dans toutes ces tables ou vues, vous pouvez simplement utiliser des requêtes comme si vous récupériez des données de n'importe quelle autre table utilisateur. Mais gardez à l'esprit que beaucoup d'entre elles contiennent également des métadonnées sur les tables du dictionnaire ou du catalogue du SGBD elles-mêmes, ce qui peut compliquer la compréhension des résultats.

```pgsql
SELECT *
FROM information_schema.tables
WHERE table_name='rental';

SELECT *
FROM pg_catalog.pg_class
WHERE relname = 'bike';

SELECT *
FROM pg_catalog.pg_stat_activity;

/*Obtenir les métadonnées des contraintes PRIMARY KEY que nous avons nommées avec "PK"*/
SELECT*
FROM pg_catalog.pg_constraint
WHERE conname LIKE '%pk%';

SELECT*
FROM pg_catalog.pg_constraint
WHERE conname LIKE '%pk%';

SELECT *
FROM information_schema.table_constraints
WHERE constraint_name LIKE '%pk%';
```

## Chapitre 10 : Exemple de processus de conception

Jusqu'à présent, vous avez découvert l'intégralité du modèle relationnel et quelques bases de SQL. Vous pouvez maintenant créer une base de données relationnelle sur le SGBD PostgreSQL, la gérer et y effectuer des requêtes. Appliquons donc toutes ces connaissances à un cas d'utilisation réel.

### Niveaux de base de données

Pour ce faire, nous devons nous rappeler certains des différents niveaux du processus de conception de base de données. Tout d'abord, nous avons la phase d'**analyse** où nous recueillons les exigences du projet auprès de l'utilisateur final ou du client. Ensuite, nous créons une conception **conceptuelle**, que nous transformons par la suite en une conception **logique** que nous pouvons implémenter sur un SGBD.

Ce sont les principaux niveaux dont nous devons nous soucier ici. Mais en plus de ceux-ci, nous avons le niveau **physique**, qui se concentre sur la représentation interne de l'implémentation du modèle logique de la base de données dans le SGBD à l'aide d'objets SGBD comme les index. Nous avons également le niveau de **stockage**, qui est le plus proche du matériel, et qui est principalement dédié à l'organisation des fichiers disque qui implémentent la fonctionnalité de la base de données sur le SGBD. Enfin, nous avons également le niveau de conception de l'**application** qui vise à fournir la base de données en tant que service à l'utilisateur.

Nous ne couvrirons pas ces niveaux supplémentaires dans cet exemple en raison de leur complexité et parce qu'ils ne sont pas aussi étroitement liés à la conception réelle de la base de données.

### Le processus de conception de base de données

Face à un problème réel nécessitant la conception d'une base de données, la première chose à faire est de recueillir autant d'informations que possible auprès de l'utilisateur ou du client. Nous faisons cela pour formaliser les exigences du système que nous allons construire.

Nous pouvons interviewer le client, sonder les utilisateurs potentiels du service ou utiliser d'autres méthodes similaires. Dans ce cas, nous n'effectuerons aucune de ces tâches directement. Au lieu de cela, nous supposerons que nous avons certaines exigences, et qu'à partir d'elles, nous avons pu construire un diagramme **entité-relation** qui les capture et modélise correctement le domaine de notre système. Disons qu'il ressemble à ceci :

![Diagramme entité-relation sur lequel nous travaillerons dans ce chapitre. Il représente diverses entités et relations, où les entités incluent "Vehicle," "Person," "Car," "Pool," "City," et d'autres. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1754234568579/a4165e66-85f1-4a81-b85d-a2be8ea19db3.jpeg align="center")

Comme vous pouvez le voir sur le diagramme ci-dessus (vous pouvez l'agrandir en l'ouvrant dans un nouvel onglet), le projet sur lequel nous travaillerons dans cet exemple est une extension du domaine de location de vélos que nous avons utilisé jusqu'à présent.

En plus d'un service de location de vélos, nous inclurons d'autres éléments pouvant être présents dans un modèle de base de données réel, tels que des véhicules, des lieux, des villes, etc. Nous inclurons également des actions pouvant être effectuées entre ces éléments, comme posséder une voiture, résider dans une ville, réserver une croisière ou obtenir un abonnement de bus, entre autres.

Lorsque nous construisons ce diagramme, nos décisions les plus importantes concernent les concepts modélisés avec des entités, ceux représentés par des relations et ceux qui ne valent pas la peine d'être inclus dans notre système.

Dans l'ensemble du domaine, il est courant de rencontrer beaucoup d'informations fournies par le client ou les utilisateurs qui ne nous aident pas directement à modéliser le système, car ils ne s'attendent pas à ce qu'elles soient stockées dans la base de données. Ainsi, tous les concepts liés à des informations qui ne sont pas destinées à être stockées de manière **persistante** ne sont généralement pas inclus dans la conception.

Quant aux autres questions, elles sont très subjectives, et il n'y a pas d'ensemble de règles à suivre pour savoir sans équivoque quels concepts modéliser avec des **entités** ou des **relations** – ou même pour déterminer le **degré** de ces relations (que nous supposerons ici être toujours de 2 pour éviter de compliquer la conception avec des relations impliquant plus de deux classes).

### Du modèle entité-relation au modèle logique

Mais pour comprendre comment nous pouvons et devons prendre ces décisions de conception, il est utile de comprendre le **but** de chaque entité dans ce diagramme entité-relation, ainsi que la signification des éléments qu'elle comprend ou auxquels elle se rapporte. Nous devons également comprendre comment elle a été traduite au niveau de la conception logique.

Avant d'expliquer chacune des entités, voici le diagramme relationnel que nous avons après toute la phase de conception logique :

![Diagramme relationnel dérivé du précédent diagramme entité-relation. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1753355497082/c7f6079b-a88b-4651-a92b-36761151aa80.png align="center")

Ce diagramme est ce que nous allons construire progressivement au fur et à mesure que nous transformons les entités en tables. Assurez-vous d'avoir ce diagramme et le diagramme entité-relation ouverts dans des fenêtres séparées afin de pouvoir vous y référer au cours des chapitres suivants. Cela rendra tout ce dont nous discutons plus facile à comprendre.

Comme vous pouvez le voir dans le diagramme ci-dessus, il inclut certaines modifications comme des clés étrangères pointant vers des attributs "libres" tels que **Sanction.SanctionID**, au lieu du même attribut dans la table du diagramme. Cela vise à éviter que les flèches de clé étrangère ne se croisent excessivement. Bien que ce ne soit pas une manière standard de représenter le modèle logique relationnel, tant que sa signification est spécifiée, c'est tout à fait valide.

Certaines contraintes ne sont pas modélisées dans le système en raison de leur complexité, ce que nous verrons au fur et à mesure que nous expliquerons toutes les entités. C'est pourquoi aucune note n'est incluse dans le diagramme relationnel, et nous n'indiquons pas les attributs qui peuvent ou ne peuvent pas être NULL. Il est utile de les montrer dans le diagramme, mais ce n'est pas obligatoire.

Enfin, au cours des explications, nous montrerons le code SQL utilisé pour créer chaque table. Vous trouverez le script SQL pour la création de l'intégralité de la base de données tout à la fin, après avoir expliqué toutes les entités. En effet, nous n'allons pas en discuter dans l'ordre où elles doivent être créées, afin de respecter les contraintes d'intégrité référentielle qui causeraient des erreurs dans le SGBD si les tables étaient créées dans un ordre différent.

#### Entité Person

Tout d'abord, nous avons l'entité Person, dont l'objectif principal est de modéliser l'existence de personnes dans notre système. Il est important de noter que dans notre domaine, il existe des personnes physiques, où chacune est une entité physique que nous pouvons abstraire à travers le concept de personne, qui possède un ensemble de caractéristiques associées. En d'autres termes, même s'il existe de nombreuses personnes différentes, elles partagent toutes un ensemble de caractéristiques qui les définissent en tant que personnes.

Ces caractéristiques sont ce que nous modéliserons comme les attributs de l'entité **Person**. Celles-ci peuvent ensuite être "instanciées", comme nous l'avons vu précédemment, ce qui donne un ensemble d'occurrences d'entités – ou en d'autres termes, des personnes spécifiques définies par les valeurs de leurs caractéristiques ou attributs.

Pour mieux comprendre cela, nous pouvons traduire cette entité au niveau de la conception logique où, s'agissant d'une entité unique, nous la modélisons avec une seule table nommée Person avec les attributs et types de données correspondants qui correspondent aux caractéristiques des personnes. De cette façon, le schéma de la table sera la structure qui définit "toutes les personnes", comme un modèle, tandis que les personnes spécifiques dont nous voulons stocker les informations dans le système correspondent aux uplets de la table, qui seront insérés au fur et à mesure que nous enregistrons des personnes dans le système.

Pour les attributs de l'entité, nous inclurons ceux qui doivent être stockés de manière persistante, tels que le nom, la date de naissance, l'e-mail, etc. Parmi tous, nous choisissons **PersonID** comme **clé primaire**, dont nous supposons qu'elle contient l'ID gouvernemental de la personne. Mais pour illustrer le concept de **clé substitutive** en SQL, dans l'implémentation sur le SGBD, nous implémenterons l'attribut PersonID comme une clé substitutive au lieu de l'ID réel de la personne (puisque les deux peuvent identifier de manière unique chaque personne). Ainsi, chaque uplet de Person aura une valeur unique et distincte dans cet attribut, servant de super-clé, de clé candidate et étant finalement sélectionné comme clé primaire.

En plus des attributs représentés dans le diagramme entité-relation, la table que nous utilisons pour modéliser l'entité Person possède d'autres attributs qui aident à implémenter les associations avec d'autres entités, spécifiquement des clés étrangères.

Si nous regardons uniquement le diagramme entité-relation, nous verrons une série d'associations qui "quittent" ou "entrent" dans l'entité Person. En d'autres termes, toutes les relations que possède cette entité sont de type 1-*, ce qui signifie que les cardinalités maximales des deux côtés sont respectivement 1 et *. Ces cardinalités maximales nous indiquent combien d'occurrences des entités peuvent être liées les unes aux autres. Ainsi, avec ces informations, nous pouvons déterminer où placer les clés étrangères et quels attributs elles doivent référencer à partir d'entités spécifiques.

Dans le cas de Person, nous avons 12 associations avec de telles multiplicités, dont une seule est une relation où le côté **"plusieurs"** (le côté avec la cardinalité maximale *) se trouve dans l'entité Person elle-même. Cela signifie que pour implémenter l'association entre Person et **CruiseLine**, par exemple, au niveau logique, il devrait y avoir une clé étrangère du côté "plusieurs" pointant vers l'entité du côté 1. Sinon, si nous plaçons la clé étrangère dans CruiseLine et la faisons référencer Person, son attribut pourrait contenir un nombre arbitraire de références à des personnes, entraînant l'apparition d'un groupe répétitif.

D'un autre côté, les 11 autres associations ont le **"côté 1"** dans Person, ce qui indique qu'il y a 11 entités qui doivent avoir une **clé étrangère** pointant vers Person.

Ainsi, nous savons que Person possède une clé étrangère pointant vers CruiseLine, même si les attributs qui la composent n'apparaissent pas explicitement dans le diagramme conceptuel. Et, puisque la clé étrangère doit référencer des uplets de CruiseLine, elle sera composée d'autant d'attributs que la clé primaire de CruiseLine, avec les mêmes types de données, respectivement.

Cela se produit car la clé étrangère doit référencer les uplets de manière unique. Ainsi, les valeurs des attributs de la clé étrangère devraient nous permettre d'aller dans la table CruiseLine, de regarder les colonnes de ses attributs de clé primaire et de trouver facilement l'uplet référencé. La clé étrangère dans Person aura donc 2 attributs, et pas seulement un.

```pgsql
CREATE TABLE Person (
    PersonID SERIAL PRIMARY KEY,
    Name VARCHAR(32) NOT NULL,
    Birth DATE NOT NULL CHECK (Birth < CURRENT_DATE),
    Email VARCHAR(32) NOT NULL,
    Phone BIGINT NOT NULL CHECK (Phone > 0),
    Nationality VARCHAR(32) NOT NULL,
    NameFK VARCHAR(32),
    FoundationDateFK DATE,
    FOREIGN KEY (NameFK, FoundationDateFK) REFERENCES CruiseLine(Name, FoundationDate)
);
```

De plus, comme vous pouvez le voir dans son DDL, les attributs **(NameFK, FoundationDateFK)** qui composent la clé étrangère n'ont pas la contrainte NOT NULL. En effet, la clé étrangère dans Person peut ne référencer aucun uplet de CruiseLine en raison de la multiplicité minimale de l'association du côté de CruiseLine (qui, étant 0, implique qu'une personne peut ne pas être cliente d'une ligne de croisière).

Sémantiquement, cette association, implémentée avec la clé étrangère, représente la possibilité qu'une personne puisse être cliente d'une certaine ligne de croisière, où si elle n'est cliente d'aucune, sa clé étrangère sera NULL.

Dans le même temps, une ligne de croisière ne doit pas nécessairement avoir de clients, car elle peut être liée à zéro personne au minimum, selon la multiplicité minimale de l'autre côté. Ainsi, avec les deux multiplicités minimales à 0, l'association dans son ensemble devient facultative, ce qui signifie qu'elle peut ne pas exister du tout, car rien n'oblige son existence.

Si nous regardons le diagramme relationnel, pour représenter cette entité ou table, il suffit de l'écrire en notation [**Datalog**](https://fr.wikipedia.org/wiki/Datalog), avec son nom et ses attributs. La seule chose à garder à l'esprit est que les attributs qui composent la clé primaire sont soulignés, et ceux qui représentent des clés étrangères ont chacun une flèche provenant d'eux pointant vers l'attribut correspondant de la clé primaire de l'entité ou de la table qu'ils référencent.

Dans des cas comme celui-ci où la clé étrangère est composite, chacun de ses attributs possède une flèche pointant vers l'attribut correspondant de l'entité référencée. Mais l'ordre dans lequel les attributs sont écrits dans ce diagramme n'est pas tout à fait pertinent – ce qui signifie que nous pouvons les écrire dans n'importe quel ordre tant que nous représentons correctement lesquels sont des clés primaires ou étrangères.

En ce qui concerne le DDL, puisque nous considérerons **PersonID** comme une **clé substitutive**, nous le déclarons comme [SERIAL](https://www.geeksforgeeks.org/postgresql/postgresql-serial/) afin que la colonne stocke des valeurs **auto-incrémentées**. De cette façon, pour identifier de manière unique chaque uplet, l'attribut utilisera une valeur entière qui augmente de un au fur et à mesure que les uplets sont insérés. Cela nous permet de les différencier tous par ce numéro.

Nous spécifierons la clé primaire avec **PRIMARY KEY**, que nous pouvons placer directement dans la déclaration de l'attribut s'il n'est pas composite. Nous spécifierons la clé étrangère avec **FOREIGN KEY**, en indiquant quels attributs référencent la clé primaire de CruiseLine.

La seule chose à laquelle il faut faire attention est l'ordre des attributs. Bien que vous puissiez disposer la clé étrangère dans n'importe quel ordre dans FOREIGN KEY, dans **REFERENCES**, nous devons nous assurer que les attributs de la clé primaire de CruiseLine sont dans le même ordre que ceux de la clé étrangère afin d'être référencés correctement.

Par exemple, si **NameFK** doit référencer **Name**, alors ces attributs occuperont la même position dans les uplets où nous déclarons la clé étrangère et la clé primaire vers laquelle elle pointe, sans avoir besoin d'apparaître dans une position spécifique, tant que la correspondance est maintenue.

Voyons maintenant ce qu'une Person peut faire.

#### Entité Rental

Dans notre domaine, les gens peuvent louer des vélos, et pour chaque location de vélo, nous voulons stocker certaines informations comme l'heure à laquelle la location a eu lieu, la durée en heures, le prix par heure, etc. Ainsi, si nous modélisions cela comme une association M-N entre **Bike** et **Person**, nous ne pourrions pas stocker toutes ces informations à moins d'utiliser une entité associative (qui n'est valide que lorsque l'entité elle-même est faible en identification). Mais ici, nous préférons utiliser une clé substitutive pour identifier de manière unique les locations, ce qui évite de rendre l'entité qui les représente faible en identification.

Ceci est nécessaire car chaque location nécessite le stockage d'informations associées, en plus de la personne et du vélo impliqués. Nous allons donc introduire une entité qui se rapporte à la fois à Bike et à Person par le biais d'**associations 1-*** (chaque **Rental** associe un vélo à une personne), stockant des informations sur cet "événement". Ensuite, comme elle possède deux associations avec le côté "plusieurs" dans Rental, cette entité aura deux clés étrangères – une pour implémenter chaque association. L'une référencera la clé primaire de l'entité Bike et l'autre la clé primaire de l'entité Person.

Ici, nous devons distinguer les deux clés étrangères, car chacune est composée d'un attribut, contrairement au cas précédent où Person n'avait qu'une seule clé étrangère composée de plusieurs attributs. C'est-à-dire que quels que soient les attributs qui composent chaque clé étrangère, il est important de distinguer que l'une vise à identifier de manière unique un vélo tandis que l'autre identifie de manière unique une personne.

```pgsql
CREATE TABLE Rental (
    RentalID SERIAL PRIMARY KEY,
    StartTimestamp TIMESTAMP NOT NULL,
    Duration INT NOT NULL CHECK (Duration >= 0), /*Durée de la période de location en heures*/
    HourPrice DOUBLE PRECISION NOT NULL CHECK (HourPrice >= 0),
    BikeFK INT NOT NULL,
    PersonFK INT NOT NULL,
    FOREIGN KEY (BikeFK) REFERENCES Bike(BikeID),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID)
);
```

Lors de l'écriture de votre DDL, les attributs sont déclarés de la même manière qu'auparavant – la différence principale ici étant que chaque clé étrangère possède sa propre contrainte FOREIGN KEY, qui référence l'attribut de clé primaire de la table correspondante. C'est le cas car ici, Bike et Person ont toutes deux des clés primaires avec un seul attribut.

Un autre détail important à considérer est la multiplicité minimale du côté de Person et Bike dans les associations du diagramme conceptuel, où le côté 1 des associations a une multiplicité minimale de 1. Cela signifie qu'un Rental doit toujours être associé à une personne et à un vélo, leurs clés étrangères ne peuvent donc jamais être NULL. C'est pourquoi la contrainte NOT NULL est utilisée dans les attributs.

Comme auparavant, au niveau conceptuel, nous ne montrons pas les attributs qui forment les clés étrangères, car les associations elles-mêmes et leurs cardinalités indiquent implicitement l'existence de clés étrangères. Mais dans le diagramme relationnel, nous montrons ces attributs, où des flèches indiquent les attributs de clé primaire d'autres entités vers lesquels ils pointent. Et, puisque l'entité n'est pas faible en identification, aucun des attributs de clé étrangère ne doit être souligné.

En ce qui concerne les autres contraintes, nous n'autorisons aucun attribut à être NULL, car il n'est pas logique qu'un horodatage (timestamp) soit nul, par exemple, alors que c'est précisément l'information précieuse sur une location que nous voulons stocker dans la base de données. Les autres attributs ont également des contraintes telles que la non-négativité, car la durée ou le tarif horaire ne peuvent pas être des montants négatifs.

De cette façon, si quelqu'un essaie d'insérer des valeurs négatives pour ces attributs, le SGBD saura automatiquement que la donnée insérée n'est pas valide ou exacte, puisque les nombres réels pour la durée et le prix ne peuvent jamais être négatifs. Cela implique que les valeurs de ces attributs doivent être positives pour être exactes.

#### Entité CarOwnership

Une autre entité liée à Person dans le diagramme – c'est-à-dire représentant autre chose qu'une Person peut faire – est **CarOwnership**. Celle-ci vise à modéliser le fait que les gens peuvent posséder des voitures, qu'elles soient achetées, louées ou en leasing. Pour cela, nous utilisons la même structure conceptuelle que pour Rental, où une personne peut avoir plusieurs voitures et une voiture peut appartenir à de nombreuses personnes.

Comme auparavant, cette association **N-M** implicite entre **Car** et **Person** doit stocker des informations sur la propriété, telles que son type, sa date de début, son prix, etc. Nous utiliserons donc une entité intermédiaire avec des associations 1-* vers les deux entités, avec le côté 1 sur celles-ci.

```pgsql
CREATE TYPE CarOwnershipType AS ENUM('buy', 'rental', 'lease');
CREATE TABLE CarOwnership (
    InsuranceID SERIAL PRIMARY KEY,
    BuyDate TIMESTAMP NOT NULL, /*Date de début de la propriété*/
    BuyPrice DOUBLE PRECISION NOT NULL CHECK (BuyPrice >= 0), /*Prix de la propriété, s'il s'agit d'une location ou d'un leasing, ce prix représente un montant mensuel*/
    WarrantyEndDate DATE NOT NULL CHECK (WarrantyEndDate >= DATE(BuyDate)),
    OwnershipType CarOwnershipType NOT NULL,
    PlateFK VARCHAR(32) NOT NULL,
    PersonFK INT NOT NULL,
    FOREIGN KEY (PlateFK) REFERENCES Car(Plate),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID)
);
```

La table implémentée au niveau logique est très similaire à Rental, car nous avons une clé substitutive qui identifie de manière unique les uplets, empêchant ainsi l'entité d'être faible en identification. Vous pouvez le voir directement dans le diagramme conceptuel. Là, nous avons un attribut marqué par **{id}** auquel nous donnons une sémantique équivalente à celle d'une clé substitutive. Cela signifie que nous n'avons pas besoin que son identification dépende d'une autre entité.

En d'autres termes, au niveau conceptuel, InsuranceID est un identifiant unique fourni par une compagnie d'assurance. Pour le générer, ils ont probablement utilisé une technique similaire au SERIAL auto-incrémenté de SQL, bien qu'il ne s'agisse pas nécessairement de cela, car il en existe [beaucoup d'autres](https://www.freecodecamp.org/news/how-to-effectively-manage-unique-identifiers-at-scale/) avec des applications très spécifiques.

La valeur de InsuranceID pourrait nous être fournie lors de l'insertion d'uplets dans notre système, où cette valeur devrait respecter la contrainte de clé primaire et ne pas se répéter pour n'importe quelle paire d'uplets possible. Mais nous avons tout de même décidé de l'implémenter avec un SERIAL pour simplifier la génération de données synthétiques pour cette base de données.

Gardez simplement à l'esprit que, dans une situation réelle, si cette valeur nous est fournie, nous devrions éviter d'utiliser SERIAL et enregistrer l'identifiant que possède chaque uplet. Comme InsuranceID est la clé primaire, aucune paire d'uplets ne peut avoir la même valeur dans cet attribut, mais ils peuvent avoir la même date de début, le même prix, etc.

Dans cette table, pour restreindre les valeurs que l'attribut OwnershipType peut prendre, au lieu d'utiliser un CHECK, nous allons créer un nouveau type de données. Nous aurions pu le faire parfaitement en utilisant un CREATE DOMAIN. Mais à la place, nous utiliserons un [TYPE ENUM](https://www.postgresql.org/message-id/49DCDA27.4090901@megafon.hr) pour montrer une autre façon de définir l'ensemble des valeurs qu'un attribut peut prendre. Il définit les valeurs possibles pour l'attribut, représentant une propriété où une personne achète, loue ou prend en leasing une voiture. Enfin, ce TYPE ENUM est affecté comme type de données de l'attribut.

Nous avons implémenté ici les contraintes de domaine les plus basiques et les exigences du problème, qui ne concernent que la table **CarOwnership** elle-même. Par exemple, nous avons celles exigeant que le prix soit positif ou que la date de fin de garantie soit postérieure à la date de début de la propriété.

D'un autre côté, nous pouvons voir que l'attribut **BuyDate** s'est vu attribuer un type de données **TIMESTAMP**, ce qui ne correspond pas exactement au nom de l'attribut. Dans cet exemple, de tels détails ne sont pas aussi importants, car le TIMESTAMP a été déclaré de cette manière pour fournir une heure en plus de la date d'achat. Mais dans un projet réel, vous devriez être plus strict sur le nommage des attributs en fonction de leurs caractéristiques. Cela aidera à améliorer la clarté du schéma et facilitera la gestion de la base de données.

#### Entité Residence

Une personne peut également résider dans une ville, notre base de données doit donc pouvoir stocker des informations sur le séjour d'une personne dans une certaine ville. Nous le ferons à l'aide de l'entité Residence, qui fonctionne de manière similaire aux entités précédentes Rental et CarOwnership, mais avec quelques différences.

Tout d'abord, les attributs qu'elle stocke sont :

* la date de début du séjour d'une personne dans une ville (qui ne peut pas être nulle car si le séjour existe, il doit avoir commencé à une date),
    
* la date de fin du séjour (qui peut être NULL car la personne peut résider dans la ville pendant une durée indéterminée), et
    
* l'adresse où elle réside au sein de la ville.
    

Lorsque l'attribut EndDate est NULL, cela signifie que la personne réside toujours dans la ville, car la date de fin du séjour n'est pas définie. De plus, si cette date existe et est postérieure à la date actuelle, nous pouvons également savoir que la personne vit toujours dans la ville jusqu'à la date spécifiée.

Cela a des implications pour l'identification de l'entité Residence, car il n'y a pas d'ensemble d'attributs au sein de l'entité elle-même qui identifie de manière unique les uplets de Residence. Au contraire, c'est la date de début, ainsi que les références à la personne et à la ville, qui l'identifient de manière unique ensemble. Ainsi, puisque l'identification de l'entité dépend d'autres entités, Residence est une entité faible en termes d'identification.

Ces références fonctionnent de manière similaire à ce que nous avons vu précédemment dans Rental, par exemple, où nous avions plusieurs associations 1-* avec le côté "plusieurs" dans l'entité Residence. Cela implique que pour chaque association, la clé étrangère est située dans l'entité Residence, pointant vers l'entité de l'autre côté de l'association.

Comme il y a deux associations de ce type au total, il y a deux clés étrangères, chacune formée par un attribut, car les clés primaires des entités vers lesquelles elles pointent sont également formées par un attribut unique.

```pgsql
CREATE TABLE Residence (
    StartDate DATE NOT NULL,
    EndDate DATE CHECK (
        EndDate IS NULL
        OR EndDate >= StartDate
    ),
    Address VARCHAR(32) NOT NULL,
    PersonFK INT NOT NULL,
    CityFK INT NOT NULL,
    PRIMARY KEY (StartDate, PersonFK, CityFK),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID),
    FOREIGN KEY (CityFK) REFERENCES City(CityID)
);
```

Si nous regardons le diagramme relationnel, nous verrons que la table implémentant cette entité a ses clés étrangères soulignées car elles font partie de la clé primaire. Cela nous aide à identifier que l'entité conceptuelle correspondante est **faible en identification**, certains de ses attributs de clé primaire étant des clés étrangères.

De plus, si nous voulions reconstruire l'entité conceptuelle à partir du diagramme relationnel, il suffirait de regarder les clés étrangères de la table, les autres entités qu'elles référencent, si leurs attributs sont soulignés ou non, et les éventuelles contraintes indiquées dans le diagramme relationnel.

Grâce à cela, si l'une des clés étrangères est soulignée, l'entité est nécessairement **faible** en identification, et le rôle **«weak»** serait spécifiquement placé sur l'association modélisée par cette clé étrangère. Le côté **"plusieurs"** de cette association serait placé du côté de l'entité d'où provient la clé étrangère. Et nous n'inclurions pas ses attributs de clé étrangère dans l'entité du diagramme conceptuel.

Dans son DDL, nous pouvons voir que la clé primaire est composée de StartDate ainsi que des attributs de clé étrangère, où chacun représente une clé étrangère différente pointant vers une certaine entité comme Person ou City – d'où l'ajout de deux contraintes FOREIGN KEY. Nous avons également ajouté la contrainte NOT NULL aux deux clés étrangères en raison de la multiplicité minimale du côté 1 des associations, qui exige qu'un uplet Residence lie une personne à une ville. Si nous avions 0..1 au lieu de 1..1 sur ces côtés des associations, alors chaque clé étrangère de Residence pourrait ne référencer aucune personne ou ville, ce qui signifie qu'elle pourrait être NULL.

En ce qui concerne les contraintes restantes, aucun attribut ne peut être nul sauf **EndDate**. S'il n'est pas NULL, alors la date qu'il stocke doit être postérieure à la date à laquelle la résidence a commencé, car il ne serait pas logique qu'elle soit antérieure à la date de début.

#### Entité ShipAssignment

Une autre entité qui est pratiquement la même que la précédente est ShipAssignment, chargée de modéliser l'affectation de certains navires de croisière à des lignes de croisière. C'est-à-dire qu'une croisière peut appartenir ou être affectée à une ligne de croisière qui l'exploite sous sa marque pendant une certaine période, tout comme une personne peut résider dans une ville pendant une certaine période.

S'agissant d'une entité faible en identification, comme nous pouvons le voir dans son diagramme conceptuel, nous aurions pu la représenter avec une entité associative et une association N-M entre CruiseShip et CruiseLine. Mais pour être cohérent avec la notation que nous avons utilisée dans Residence, nous n'utiliserons pas d'entité associative. Au lieu de cela, nous ferons en sorte que l'entité s'interpose dans l'association N-M, ce qui donne deux associations 1-* avec le côté **"plusieurs"** dans ShipAssignment.

Cela indique implicitement qu'il existe deux clés étrangères pointant respectivement vers CruiseShip et CruiseLine.

Notez également que le simple fait de se concentrer sur le côté **"plusieurs"** (qui est une règle facile à appliquer pour déterminer où placer les clés étrangères en regardant simplement le diagramme conceptuel) n'est pas en soi une bonne pratique sans réflexion supplémentaire. Lorsque vous avez un diagramme conceptuel, vous devriez regarder tous les éléments de l'entité pour prendre des décisions éclairées et raisonnées sur sa conception logique.

```pgsql
CREATE TABLE ShipAssignment (
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL CHECK (EndDate >= StartDate),
    NameFK VARCHAR(32) NOT NULL,
    FoundationDateFK DATE NOT NULL,
    ShipFK INT NOT NULL,
    PRIMARY KEY (StartDate, NameFK, FoundationDateFK, ShipFK),
    FOREIGN KEY (NameFK, FoundationDateFK) REFERENCES CruiseLine(Name, FoundationDate),
    FOREIGN KEY (ShipFK) REFERENCES CruiseShip(ShipID)
);
```

Ici, nous supposons que la date de fin de l'affectation est toujours définie, ce qui signifie que les navires sont affectés aux lignes de croisière par des "contrats" qui commencent et se terminent toujours à des dates spécifiques, et que les affectations ne durent pas indéfiniment. Cela implique que EndDate ne peut jamais être NULL. Ainsi, dans le DDL, nous incluons la contrainte NOT NULL et un CHECK pour nous assurer que EndDate est postérieure à la date de début, garantissant que seuls des uplets valides sont insérés dans la base de données.

Les clés étrangères sont formées uniquement par l'attribut ShipFK, qui se réfère à l'entité CruiseShip. Nous l'utilisons pour référencer le navire affecté à une certaine ligne de croisière. Mais l'autre clé étrangère, qui est utilisée pour implémenter l'autre association 1-*, est composée des attributs **(NameFK, FoundationDateFK)**, qui se réfèrent à la clé primaire de CruiseLine – et celle-ci, à son tour, est composite et contient deux attributs **(Name, FoundationDate)**.

Si nous regardons uniquement le diagramme relationnel, nous verrons que trois attributs font partie de clés étrangères car des flèches en proviennent. Plus précisément, la flèche de l'un d'eux (ShipFK) pointera vers un attribut dans une certaine table. Nous savons donc que cet attribut forme une clé étrangère à lui seul, tandis que les deux autres ont des flèches pointant vers des attributs d'une autre entité différente (mais les deux référençant la même).

Ainsi, ensemble, ils forment une autre clé étrangère car l'entité ou la table qu'ils référencent est **différente** de celle référencée par l'autre attribut **ShipFK**.

Ces attributs servent à leur tour à identifier de manière unique chaque uplet dans ShipAssignment – car, avec seulement les dates de début et de fin, nous ne pouvons pas distinguer n'importe quelle paire d'uplets possible.

Par exemple, si plusieurs navires sont affectés à la même ligne de croisière au cours de la même période, les dates de début et de fin correspondront dans les deux uplets, mais ils représenteront des affectations différentes même si les dates sont les mêmes. Ainsi, la clé primaire de la table inclut les attributs des clés étrangères, afin que leurs valeurs puissent distinguer n'importe quelle paire d'uplets que nous pourrions avoir dans la table. Plus précisément, nous incluons les clés étrangères car un navire peut être ou avoir été affecté à plusieurs lignes de croisière, tout comme une ligne de croisière peut avoir eu plusieurs navires qui lui ont été affectés.

Les valeurs des deux clés étrangères sont nécessaires pour identifier de manière unique cet "événement" entre un navire et une ligne de croisière, car selon le domaine, le même navire ne peut pas être affecté plusieurs fois à la même ligne de croisière à la même date.

```pgsql
CREATE ASSERTION EveryCruiseLineHasAssignment CHECK (
    NOT EXISTS (
        SELECT *
        FROM CruiseLine cl
        WHERE NOT EXISTS (
                SELECT *
                FROM ShipAssignment sa
                WHERE sa.NameFK = cl.Name
                    AND sa.FoundationDateFK = cl.FoundationDate
            )
    ) 
);
```

Enfin, étant donné la multiplicité minimale de 1..* du côté de ShipAssignment, nous devons implémenter une contrainte pour nous assurer que toutes les lignes de croisière ont au moins une affectation de navire, qui est toujours associée à un navire.

Pour ce faire, nous pouvons utiliser soit une ASSERTION, soit un TRIGGER, car il s'agit d'une contrainte impliquant plusieurs tables. Mais par souci de simplicité, nous supposerons que les données insérées respectent toujours cette contrainte. Cela signifie que nous n'avons pas besoin d'inclure d'assertions et de déclencheurs dans le DDL.

Abordons maintenant d'autres entités importantes de notre système.

#### Entité City

Cette entité est similaire à Person et est utilisée pour stocker des informations sur les villes du système. Plus précisément, pour chaque ville, elle stocke son nom, le pays où elle se trouve, sa population, sa superficie et ses coordonnées en latitude et longitude. Chaque ville physique de notre domaine au sein du système sera représentée par un uplet dans la table City, c'est ainsi que nous implémentons cette entité au niveau logique.

De toutes les associations que possède cette entité, aucune n'est de type 1-* avec le **côté "plusieurs"** dans City. Au contraire, elles ont toutes leur côté 1 dans City. Cela signifie qu'il y aura exactement 4 clés étrangères provenant d'autres entités pointant vers City, mais la table City elle-même n'aura aucune clé étrangère pointant vers une autre entité.

Cela peut ne pas être simple à voir au niveau conceptuel, car nous devons regarder les cardinalités maximales des associations pour savoir lesquelles donnent lieu à des clés étrangères dans l'entité que nous implémentons.

En revanche, dans le diagramme relationnel, c'est plus direct. Les références implémentées avec des clés étrangères sont des flèches, nous pouvons donc savoir directement combien de flèches se réfèrent à la clé primaire d'une certaine table ou combien pointent vers d'autres tables, en indiquant également clairement de quels attributs et tables elles proviennent.

```pgsql
CREATE TABLE City (
    CityID SERIAL PRIMARY KEY,
    Name VARCHAR(32) NOT NULL,
    Country VARCHAR(32) NOT NULL,
    Population INT NOT NULL CHECK (Population >= 0),
    Area DOUBLE PRECISION NOT NULL CHECK (Area >= 0),
    Latitude DOUBLE PRECISION NOT NULL CHECK (
        Latitude BETWEEN -90 AND 90
    ),
    Longitude DOUBLE PRECISION NOT NULL CHECK (
        Longitude BETWEEN -180 AND 180
    )
);
```

En ce qui concerne le DDL, nous implémentons l'identifiant CityID avec une clé substitutive **SERIAL**, car au niveau conceptuel, nous avons défini que l'attribut **CityID** est la clé primaire de **City**.

Il est important de noter que lors de la modélisation d'un domaine ou de la résolution d'un problème pour un client, nous pourrions être tenus d'utiliser des identifiants spécifiques au domaine que nous modélisons, ce qui signifierait que CityID serait du même type que l'identifiant à stocker. Mais par souci de simplicité, supposons que nous construisons nous-mêmes les identifiants de ville à l'aide d'une clé substitutive.

En plus des contraintes NOT NULL qui empêchent tous les attributs d'être NULL, puisqu'il n'est pas logique qu'une ville n'ait pas de nom ou de nombre de population défini, nous imposons une restriction sur la plage de valeurs que Latitude et Longitude peuvent prendre. Il s'agit de s'assurer que les valeurs sont valides, même si nous ne pouvons pas vérifier si elles sont exactes, car cela dépend principalement de la source de données.

Pour ce faire, nous pouvons utiliser l'opérateur **BETWEEN**, qui effectue la même vérification que **Latitude >= -90 AND Latitude <= 90** mais de manière plus lisible.

#### Entité Port

En plus des villes, notre domaine comprend également des ports, qui sont représentés par l'entité Port. Comme précédemment, chaque port sera un uplet dans la table, avec sa clé primaire composée du nom du port stocké dans l'attribut **Name** et d'une clé étrangère qui référence **City**, modélisant la ville où se trouve le port.

Nous pouvons déduire l'existence de cette clé étrangère en regardant les associations de l'entité, où toutes sont de type 1-*, et une seule a le **côté "plusieurs"** dans Port. Celle-ci modélise précisément cette relation entre Port et City. Les autres ont leur **côté 1** dans Port, ce qui indique qu'elles pointent vers Port, c'est-à-dire qu'elles référencent un uplet dans la table Port.

Dans le même temps, la clé étrangère de Port fait également partie de sa clé primaire car un port ne peut pas être identifié par son seul nom – nous devons également connaître la ville où il se trouve.

Par exemple, dans ce domaine, nous supposons qu'il peut y avoir plusieurs ports avec le même nom, mais pas situés dans la même ville. Ainsi, si deux ports se trouvent dans la même ville, selon le domaine, nous avons la garantie que leurs noms ne peuvent pas être les mêmes. Cela nous permet de définir la clé primaire comme la combinaison **(Name, CityFK)**.

Nous faisons ces suppositions ici à titre d'exemple, mais dans un projet réel, elles devraient être confirmées auprès des experts du domaine et des exigences du client pour s'assurer qu'elles sont respectées. Cela nous permettrait de prendre des décisions de conception telles que l'établissement des clés d'une entité. Ainsi, une fois que nous savons que Port possède une clé étrangère qui fait partie de sa clé primaire, nous savons que l'entité est faible en identification. Dans le diagramme relationnel, nous devrons souligner non seulement **Name** mais aussi l'attribut **CityFK**.

```pgsql
CREATE TABLE Port (
    Name VARCHAR(32),
    TerminalCount INT NOT NULL CHECK (TerminalCount >= 0),
    MaxShipLength INT NOT NULL CHECK (MaxShipLength >= 0),
    Area DOUBLE PRECISION NOT NULL CHECK (Area >= 0),
    CityFK INT NOT NULL,
    PRIMARY KEY(Name, CityFK),
    FOREIGN KEY (CityFK) REFERENCES City(CityID)
);
```

Le DDL est similaire aux précédents : nous avons la déclaration des attributs et des contraintes comme **PRIMARY KEY**, où l'ensemble d'attributs **(Name, CityFK)** est défini comme ceux qui identifient de manière unique les uplets de **Port**. Nous avons également la **FOREIGN KEY** correspondante qui référence l'attribut **CityID**, la clé primaire de la table **City**.

Une particularité de cette instruction CREATE TABLE est que nous n'ajoutons pas de contrainte NOT NULL à l'attribut Name car nous n'avons pas besoin de la déclarer explicitement dans ce cas. En effet, puisque Name fait partie de la clé primaire, et qu'une clé primaire n'autorise jamais de valeurs NULL dans ses attributs, nous pouvons nous dispenser de déclarer NOT NULL, car PRIMARY KEY le fait implicitement pour assurer la [**contrainte d'intégrité de clé primaire**](https://www.ibm.com/docs/fr/db2/11.5.x?topic=concepts-primary-key-referential-integrity-check-unique-constraints).

Cela s'applique également à l'attribut de clé étrangère, qui ne peut pas être NULL en raison de la multiplicité minimale (multiplicité minimale 1 dans 1..1) du côté de l'entité City, qui exige que tous les ports soient associés à une ville. Mais pour refléter plus clairement cette multiplicité minimale, nous ajoutons explicitement NOT NULL à l'attribut CityFK, même si ce n'est pas strictement nécessaire.

Enfin, si nous voulons nous assurer que la conception logique représentée dans le diagramme relationnel est correcte par rapport au diagramme conceptuel, nous pouvons essayer de reconstruire l'entité conceptuelle à partir de la table du diagramme relationnel.

Pour ce faire, après avoir créé l'entité avec son nom et ses attributs (à l'exception de ceux qui sont des clés étrangères), nous devons inférer les associations implémentées par ces clés étrangères. Ainsi, pour chacune d'elles, nous introduisons une association qui relie Port à l'entité vers laquelle pointe la clé étrangère, où le côté "plusieurs" est sur Port et le 1 est du côté de l'autre entité.

En plus des cardinalités maximales 1 et *, nous devons également définir les minimales, que nous pouvons déterminer grâce aux contraintes indiquées dans le diagramme relationnel.

Par exemple, si l'une des clés étrangères peut être NULL, alors sa multiplicité minimale du côté 1 de l'association sera 0, ce qui fait que ce côté aura une cardinalité de 0..1.

D'un autre côté, si elle ne peut pas être NULL, la cardinalité minimale est 1. De l'autre côté de l'association, nous mettrons par défaut une cardinalité minimale de 0, à moins qu'il n'y ait des contraintes exigeant que les villes aient au moins un port, par exemple. Cela signifierait que la cardinalité minimale serait 1, ce qui ferait que le côté Port de l'association aurait une cardinalité de 1..*.

Enfin, nous pouvons répéter ce processus avec les clés étrangères qui pointent vers la clé primaire de Port, ce qui donne lieu à davantage d'associations avec d'autres entités.

Par exemple, si nous reconstruisons l'entité conceptuelle **City** à partir du diagramme relationnel, nous verrons qu'il existe une clé étrangère de **Port** pointant vers **CityID** de City. City aura donc une association **1-*** avec **Port**, où le côté "plusieurs" se trouve du côté de Port car la clé étrangère provient de Port.

De cette façon, lorsque nous aurons entièrement reconstruit l'entité conceptuelle, nous déterminerons si elle est faible en identification en vérifiant si l'une de ses clés étrangères est soulignée. Cela signifie qu'elle fait également partie de la clé primaire. Dans ce cas, nous ajouterons le rôle **«weak»** aux associations issues de ces clés étrangères, toujours du côté d'où provient la clé étrangère.

#### Entité CruiseLine

Cette entité est chargée de représenter les lignes de croisière dans notre système, qui peuvent avoir des clients et des navires affectés. Conceptuellement, cette entité est très similaire à celles que nous avons déjà vues, car elle possède une clé primaire composée de deux attributs de l'entité elle-même, et aucune clé étrangère pointant vers d'autres entités. Mais il existe des clés étrangères dans d'autres entités qui **pointent** vers **CruiseLine**, ce que nous pouvons voir grâce aux associations de type 1-*.

```pgsql
CREATE TABLE CruiseLine (
    Name VARCHAR(32) NOT NULL,
    FoundationDate DATE NOT NULL,
    ContactPhone BIGINT NOT NULL CHECK (ContactPhone > 0),
    Rating DOUBLE PRECISION NOT NULL CHECK (Rating >= 0),
    PRIMARY KEY (Name, FoundationDate)
);
```

Plus précisément, la clé primaire de cette entité est composée du nom de la compagnie et de la date de fondation. Cette combinaison de valeurs peut sembler unique parmi les uplets que nous pouvons stocker dans la table, car il est très peu probable que plusieurs lignes de croisière portant le même nom soient fondées à la même date. Mais nous ne devrions pas faire ces suppositions nous-mêmes – nous devons au contraire nous assurer que ces conditions sont remplies auprès du client, de l'utilisateur cible ou des experts du domaine de notre système.

Ici, par souci de simplicité, nous supposons directement qu'aucune ligne de croisière n'a le même nom qu'une autre fondée à la même date, mais vous devriez toujours vérifier si cela est vrai dans le domaine.

Nous fixons donc **(Name, FoundationDate)** comme clé primaire, ce qui impose à son tour la contrainte NOT NULL implicite sur les deux attributs (ce qui signifie que nous n'avons pas besoin de la déclarer explicitement). Dans le DDL, nous pouvons également voir que l'attribut **ContactPhone** n'est pas de type INTEGER, mais **BIGINT**. En effet, les numéros de téléphone sont généralement des nombres longs représentant de grandes quantités numériques qui dépasseraient la plage représentable par un type plus basique comme INTEGER. Pour les attributs de type texte, une longueur maximale fixe de 32 caractères est utilisée pour toutes les chaînes, ce qui est suffisant pour accueillir n'importe quel nom de ligne de croisière ou information similaire.

Nous pourrions également représenter le numéro de téléphone par une chaîne de caractères, ce qui permettrait de stocker l'indicatif du pays au format texte, mais cela peut compliquer le traitement puisque le numéro devrait être analysé à partir du texte.

#### Entité Vehicle

Dans notre domaine, il peut y avoir certains types de véhicules, tels que des voitures, des navires de croisière, des vélos ou des bus urbains. Ils partagent tous une série de **caractéristiques communes** comme le modèle, le poids, la couleur ou la lecture de l'odomètre pour savoir quelle distance ils ont parcourue depuis leur fabrication.

Ces attributs sont communs à tous les véhicules de notre domaine, car ils auront toujours un nom de modèle ou un poids, entre autres, quel que soit le type de véhicule qu'ils sont. C'est pourquoi nous avons décidé d'abstraire ces caractéristiques communes dans la conception conceptuelle en une **super-classe** appelée **Vehicle**. Et de celle-ci, toutes les entités représentant des types spécifiques de véhicules doivent hériter.

En d'autres termes, au niveau conceptuel, nous avons une **hiérarchie IS-A** où l'**entité parente** est **Vehicle**, qui contient toutes les caractéristiques définissant tous les véhicules. D'elle héritent une série d'entités représentant des types spécifiques de véhicules (chacune ayant des caractéristiques plus spécifiques au type de véhicule correspondant).

En résumé, nous utilisons une hiérarchie IS-A car nous devons modéliser une situation où une série d'"individus" de notre domaine partagent un ensemble de **caractéristiques communes**. Formellement, une hiérarchie IS-A peut être définie comme une relation de [spécialisation/généralisation](https://jcsites.juniata.edu/faculty/rhodes/dbms/eermodel.htm) entre une **entité super-classe** et des **entités héritières**. Les entités héritières sont composées de toutes les caractéristiques ou attributs de la super-classe plus certains de leurs propres attributs.

Mais, concrètement, ce qui nous importe, c'est qu'une hiérarchie nous permet d'avoir une super-classe (l'entité Vehicle dans ce cas) où nous avons des attributs correspondant à ces caractéristiques communes, puis une série d'entités qui en héritent et représentent des types spécifiques d'individus (chacune ayant des caractéristiques spécifiques selon son type).

Grâce à cela, nous gagnons en clarté et en maintenabilité dans le diagramme, car l'ajout d'une nouvelle caractéristique commune à tous les véhicules ne nécessite que son ajout à Vehicle – et non à chacune des entités héritières. De même, si un nouveau type de véhicule doit être ajouté au système, nous n'aurons pas besoin d'inclure tous les attributs communs des véhicules dans cette entité.

#### Comment cette hiérarchie IS-A est-elle implémentée avec des tables ?

À ce stade, nous devons décider comment implémenter la hiérarchie à l'aide de tables dans le modèle logique. Plus précisément, nous devons déterminer le nombre de tables à utiliser et les clés que chacune possédera concernant l'implémentation de la hiérarchie elle-même.

Tout d'abord, il est important de voir que Vehicle possède VehicleID comme clé primaire, dont nous supposons qu'il s'agit d'une clé substitutive. Grâce à cela, nous savons que si nous devions implémenter une table pour les entités héritières, elles devraient avoir une clé étrangère pointant vers VehicleID, car c'est la clé primaire qui peut identifier de manière unique les uplets de Vehicle.

Nous voyons que la hiérarchie ici est **complète** et **disjointe**. Elle est complète car tous les "individus" de la hiérarchie doivent toujours être représentés par les entités héritières. En d'autres termes, nous ne trouverons jamais de véhicule qui ne possède que les attributs de Vehicle – au contraire, tous les véhicules de notre domaine sont nécessairement de l'un des types définis dans les entités héritières (du moins nous le supposons). Elle est **disjointe** car un véhicule ne peut pas être de plusieurs types à la fois, ce qui signifie qu'il ne peut pas être à la fois une voiture et un navire de croisière, ce qui est logique.

Tout cela signifie que chacune d'elles sera implémentée avec une table spécifique. Notre système stocke de nombreux types de véhicules et devra probablement s'étendre avec encore plus de types de véhicules. Pour simplifier ce processus d'ajout de nouveaux types de véhicules et pour éviter l'apparition de trop de valeurs NULL dans les tables, nous implémenterons une table pour chaque entité héritière de la hiérarchie.

Pour la super-classe, nous implémenterons également une table spécifique, car chaque véhicule existant dans notre système sera représenté dans l'une des tables des entités héritières – mais il devra prendre des valeurs dans les caractéristiques (attributs) de la super-classe.

Ici, nous avons plusieurs options. Une option consiste à ne pas implémenter de table pour la super-classe, en dupliquant tous ses attributs dans chacune des tables des types de véhicules spécifiques. C'est facile à comprendre et semble initialement pratique, mais cela présente des inconvénients importants.

Une autre option consiste à implémenter une table pour la super-classe et à inclure une clé étrangère dans toutes les entités héritières qui pointent vers la clé primaire de Vehicle.

Nous pouvons facilement écarter la première option car la duplication d'attributs dans toutes les tables pour différents types de véhicules entraîne beaucoup de [redondance au niveau des métadonnées](https://softwareengineering.stackexchange.com/questions/227832/single-table-w-extra-columns-vs-multiple-tables-which-duplicate-schema?utm_source=chatgpt.com) ou du **schéma**, c'est-à-dire des attributs dupliqués dans plusieurs tables sans besoin clair de duplication.

Au-delà du problème de redondance, la duplication des mêmes attributs dans plusieurs tables rend certaines modifications de schéma plus compliquées. Par exemple, l'ajout d'une caractéristique commune supplémentaire dans Vehicle nécessiterait l'ajout d'un attribut dans chaque table. Ou nous pourrions changer la façon dont les attributs communs comme la **couleur** sont représentés, comme le passage des noms de couleur de majuscules en minuscules (ou tout changement dans leur représentation). Nous devrions effectuer ces changements dans toutes les tables de types de véhicules.

Avec l'autre option, nous implémentons une table spécifique pour la super-classe, évitant ces problèmes en centralisant le stockage des caractéristiques communes dans une seule table. Cela facilite l'exécution des opérations mentionnées précédemment, ou même d'opérations supplémentaires comme le comptage du nombre de véhicules dans notre système.

Nous pouvons facilement le faire en comptant les uplets de la table Vehicle, au lieu d'additionner les nombres d'uplets de chacune des tables des différents types de véhicules. Nous pouvons résoudre la requête de cette manière car tous les véhicules auront un **uplet dans Vehicle** qui stocke les caractéristiques communes, ainsi qu'un uplet dans leur table de type de véhicule spécifique qui stocke le reste des caractéristiques le définissant comme voiture, croisière, vélo, etc.

Dans cet uplet, il y a une **clé étrangère** qui référence l'uplet dans la table super-classe, associant ainsi les informations des deux uplets afin qu'elles puissent être interrogées et connaître toutes les informations sur un véhicule – à la fois ses caractéristiques **communes** à tous les véhicules et celles **spécifiques** à son type.

```pgsql
CREATE TYPE ColorType AS ENUM ( 'red', 'green', 'blue', 'yellow', 'black', 'white' ); 
CREATE TABLE Vehicle (
    VehicleID SERIAL PRIMARY KEY,
    Model VARCHAR(32) NOT NULL,
    Weight DOUBLE PRECISION NOT NULL CHECK (Weight >= 0),
    Color ColorType NOT NULL,
    Odometer DOUBLE PRECISION NOT NULL CHECK (Odometer >= 0)
);
```

Enfin, nous décidons d'implémenter une table pour toutes les entités de la hiérarchie, en utilisant des **clés étrangères** dans les tables des entités héritières pour référencer les uplets de Vehicle qui stockent les caractéristiques communes des véhicules.

Dans son DDL, nous pouvons voir que la clé primaire est implémentée avec un attribut de type **SERIAL** car il s'agit d'une **clé substitutive**. Pour l'attribut **Color**, nous créons un **TYPE ENUM** avec les couleurs possibles dans notre système. C'est une bonne pratique car si nous avons besoin d'un attribut de couleur dans d'autres zones du système, nous aurons son domaine (ou type de données) défini dans **ColorType**. Et cela nous permet de le réutiliser et de s'assurer que tous les attributs de couleur peuvent prendre des valeurs provenant exactement du même ensemble de données.

Mais si nous essayons de reconstruire la hiérarchie IS-A à partir du diagramme entité-relation en regardant simplement l'implémentation représentée dans le diagramme relationnel, nous nous rendrons compte qu'elle est un peu plus complexe que ce que nous avons vu auparavant.

En effet, il n'y a pas qu'une seule façon de traduire une hiérarchie IS-A en un diagramme relationnel. Selon la sémantique des caractéristiques et des entités, plus les exigences du système, il peut être préférable d'utiliser plus ou moins de tables pour l'implémenter. Mais dans des cas comme celui-ci où nous avons une table pour chaque entité de la hiérarchie, nous pouvons clairement voir qu'il existe une table Vehicle avec une clé primaire VehicleID (qui est référencée par plusieurs tables, chacune ayant exactement la même clé étrangère référençant Vehicle).

Si nous ne regardons que cela, nous pourrions penser que Vehicle est une entité qui possède des associations 1-* avec d'autres entités – et c'est tout à fait possible en ne regardant que le diagramme relationnel.

Mais pour dériver la conception conceptuelle de la conception logique et inférer l'existence d'une hiérarchie IS-A, nous devons nous concentrer sur la sémantique des tables et des attributs. C'est là que nous verrons que Vehicle contient des attributs communs à tous les types de véhicules qui ont des clés étrangères pointant vers Vehicle. Cela nous donne des indices sur le fait que Vehicle pourrait être la super-classe d'une hiérarchie, et que le reste des tables avec des clés étrangères pointant vers Vehicle pourraient être des entités héritières.

Mais inférer l'existence d'une hiérarchie IS-A dans la conception conceptuelle simplement en observant l'implémentation logique n'est pas toujours sans équivoque. En effet, par exemple, ici nous pourrions parfaitement considérer que Vehicle est une entité associée aux autres entités héritières par des associations de type 1-*. Cela serait également correct d'un point de vue conceptuel et logique.

Pourtant, même si conceptuellement nous pouvons transformer la hiérarchie en une série d'associations 1-* entre Vehicle et les autres entités, cela n'est vrai pour l'implémentation que si nous implémentons une table par entité. Sinon, nous ne refléterions pas correctement dans la conception conceptuelle ce qui est réellement implémenté dans la conception logique.

En résumé, lorsque nous voyons une hiérarchie IS-A, cela ne signifie pas nécessairement qu'il existe des clés étrangères entre les entités héritières et la super-classe, car on n'utilise pas toujours autant de tables que d'entités pour implémenter la hiérarchie. Ainsi, pour reconstruire une hiérarchie au niveau conceptuel à partir du niveau logique, le plus fiable est de se concentrer sur les contraintes, les notes ou les indications laissées dans le diagramme relationnel expliquant pourquoi certaines tables ont été implémentées – c'est-à-dire d'où elles proviennent.

L'implémentation d'une hiérarchie au niveau logique implique généralement une série de décisions de conception qui doivent être correctement justifiées, que nous pouvons ensuite utiliser pour inférer l'existence de la hiérarchie au niveau conceptuel.

Cet exercice consistant à essayer de reconstruire le niveau conceptuel est important à aborder clairement, car la compréhension de ce processus inverse est essentielle pour appréhender les éléments des différents niveaux de conception et la manière dont ils se traduisent de l'un à l'autre.

#### Entité CruiseShip

Pour illustrer comment nous avons implémenté la hiérarchie IS-A de Vehicle, examinons les différentes entités héritières qui la composent.

![Partie du diagramme entité-relation où la hiérarchie IS-A des véhicules est représentée selon leur type. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1754729845339/090a3c2f-0833-4f14-8a58-52fb1a1606ea.png align="center")

Tout d'abord, nous avons CruiseShip, qui modélise l'existence de véhicules de type navire de croisière dans notre système, où chaque navire de croisière est un uplet dans la table. En ce qui concerne les caractéristiques spécifiques du navire de croisière qui en font un véhicule de type navire de croisière, nous avons sa longueur, sa capacité de passagers ou même la vitesse à laquelle il voyage. Il possède également des caractéristiques que tous les véhicules doivent avoir dans la table Vehicle, telles que le modèle, la couleur, etc., spécifiquement dans les uplets qui stockent les valeurs des caractéristiques de chaque croisière.

Pour relier ces informations des deux tables, il existe une clé étrangère dans CruiseShip qui pointe vers Vehicle, ce qui signifie qu'elle référence l'uplet dans Vehicle où ces valeurs de caractéristiques sont stockées, pour chaque navire de croisière (uplet de CruiseShip).

De cette façon, nous nous assurons que les attributs répétés dans tous les types de véhicules sont centralisés dans une table où ils peuvent être facilement modifiés ou consultés, bien mieux que de les avoir tous dupliqués dans les différentes tables de types de véhicules.

```pgsql
CREATE TYPE ClassType AS ENUM('first', 'second', 'third', 'economy');
CREATE TABLE CruiseShip (
    ShipID SERIAL PRIMARY KEY,
    Speed DOUBLE PRECISION NOT NULL CHECK (Speed >= 0),
    Length DOUBLE PRECISION NOT NULL CHECK (Length >= 0),
    PassengerCapacity INT NOT NULL CHECK (PassengerCapacity >= 0),
    Class ClassType NOT NULL,
    VehicleID INT UNIQUE NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);
```

Dans le DDL, nous voyons que les attributs et leurs types sont déclarés, où ShipID est défini comme une clé substitutive à l'aide du type de données SERIAL. Cela nous permet d'identifier de manière unique chaque navire de croisière. Mais comme chaque navire de croisière est aussi un véhicule, nous pourrions également l'identifier en faisant de sa clé primaire **{VehicleID}**, car cet attribut, même s'il s'agit d'une clé étrangère, ne sera jamais NULL puisqu'un navire de croisière doit avoir les caractéristiques qui le classent comme véhicule.

Ainsi, la clé étrangère doit référencer un uplet valide dans Vehicle où les valeurs des caractéristiques communes à tous les véhicules sont stockées. Par conséquent, VehicleID est une clé alternative déclarée avec la contrainte UNIQUE, bien que nous ne soyons pas obligés d'ajouter cette contrainte puisque la clé substitutive ShipID est suffisante pour l'identifier.

L'important concernant cet attribut est de définir correctement les contraintes NOT NULL et FOREIGN KEY, en s'assurant qu'il référence correctement la clé primaire VehicleID de la table Vehicle.

Dans la conception conceptuelle, nous voyons que cette entité possède plusieurs associations 1-*, qui indiquent qu'il existe trois clés étrangères provenant d'autres entités pointant vers CruiseShip. Mais si nous n'avons que la conception conceptuelle, nous ne pouvons rien dire sur l'éventuelle clé étrangère générée par la hiérarchie IS-A. C'est-à-dire que si nous n'avons que le diagramme conceptuel, nous ne pouvons pas "deviner" combien de tables ont été utilisées pour implémenter la hiérarchie – nous ne le savons qu'après avoir créé la conception logique. Tout au plus, nous pourrions envisager toutes les options possibles pour implémenter la hiérarchie et, pour chacune d'elles, analyser s'il existe une clé étrangère provenant de CruiseShip.

Mais si en plus du diagramme entité-relation nous savons qu'il existe une clé étrangère provenant de CruiseShip et pointant vers une autre entité, alors l'entité vers laquelle elle pointe doit nécessairement être Vehicle. En effet, les associations de type 1-* sont des éléments dont nous savons qu'ils généreront des clés étrangères. Mais certains types d'associations comme 1-1 ou 0..1-0..1 peuvent mener à des ambiguïtés, comme nous l'avons vu précédemment en essayant d'inférer l'existence d'une hiérarchie au niveau conceptuel.

Ainsi, en écartant les entités liées par des associations 1-*, la seule option restante serait Vehicle. Avec tout cela, nous pouvons également savoir que l'implémentation de la hiérarchie au niveau logique a été faite en créant une table pour la super-classe et pour l'entité CruiseShip – mais nous ne pourrions pas être sûrs que les autres entités ont également été implémentées avec une table ou non, car cela dépend fortement de la sémantique.

#### Entité Bike

En continuant avec les différents types de véhicules, nous avons également des bicyclettes représentées dans l'entité Bike, qui hérite de Vehicle. Ici, il est plus clair que les attributs des entités héritières sont plus spécifiques que ceux de la super-classe, car seuls les vélos ont des caractéristiques comme FrameHeight (hauteur du cadre) ou Foldable (pliable).

Si nous ne regardons que le diagramme conceptuel, nous ne pouvons pas être certains que Bike possède une clé étrangère pointant vers Vehicle. C'est précisément parce que, comme mentionné précédemment, sans connaître l'implémentation spécifique au niveau logique, nous ne pouvons pas garantir qu'il existe une clé étrangère dans Bike. Mais en considérant la sémantique de la hiérarchie, nous pourrions proposer les différentes options disponibles pour l'implémenter et déterminer dans chaque cas si une telle clé étrangère existe.

```pgsql
CREATE TABLE Bike (
    BikeID SERIAL PRIMARY KEY,
    Electric BOOLEAN NOT NULL,
    Foldable BOOLEAN NOT NULL,
    HasLights BOOLEAN NOT NULL,
    FrameHeight DOUBLE PRECISION NOT NULL CHECK (FrameHeight >= 0),
    VehicleID INT UNIQUE NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);
```

Comme nous avons décidé d'utiliser une table pour implémenter chaque table de la hiérarchie, dans ce cas, il existe bien une telle clé étrangère, tout comme dans **CruiseShip**. Et nous pouvons la voir déclarée de la même manière que la contrainte FOREIGN KEY.

De plus, la clé primaire de Bike n'est pas la clé étrangère qui identifie de manière unique les véhicules. Au contraire, c'est l'identifiant **BikeID**. Ici, nous supposons que notre domaine exige que chaque type de véhicule ait son propre identifiant. C'est-à-dire qu'en plus de l'identifiant VehicleID qui sert pour n'importe quel type de véhicule, chacun de ces types doit avoir son propre **identifiant spécifique au type**. Cela signifie que les navires de croisière, les vélos, les voitures et les bus auront chacun un moyen de s'identifier (même si tous peuvent être distingués les uns des autres par l'identifiant **VehicleID** qu'ils possèdent indirectement via leur clé étrangère référençant Vehicle. C'est pourquoi l'attribut de clé étrangère est déclaré comme UNIQUE).

Et comme cette clé étrangère ne fait pas partie de la clé primaire, l'entité n'est pas faible en identification. Même si elle l'était, elle ne serait marquée d'aucune manière au niveau conceptuel. En effet, à ce niveau, nous avons une hiérarchie d'entités qui peut être implémentée au niveau logique de nombreuses manières, et toutes n'auront pas d'entités faibles en identification.

![Diagramme entité-relation avec héritage où Bike et Car sont des sous-classes de Vehicle. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752833986569/a77fb4b1-3632-4d63-ad28-750c6768ef0d.png align="center")

Pour comprendre cela, nous pouvons considérer un exemple plus simple d'une hiérarchie avec seulement deux entités héritières (comme vous pouvez le voir dans le diagramme ci-dessus). Si nous n'avons que la conception conceptuelle, nous ne saurons toujours pas quelles tables nous utiliserons pour implémenter la hiérarchie – bien que nous sachions que nous avons plusieurs options, telles que :

* implémenter ou non une table pour la super-classe
    
* implémenter une table pour représenter toutes les entités héritières, ou juste une table pour chaque entité
    
* ou même des implémentations plus complexes comme l'utilisation d'une seule table pour la super-classe et certaines des entités héritières.
    

Chacune de ces options a ses particularités. Si nous n'implémentons pas de table pour la super-classe, alors il n'y aura nécessairement aucune clé étrangère pointant vers elle. Ou si nous décidons de créer une table pour représenter ensemble la super-classe et une entité héritière, alors cette entité héritière n'aura aucune clé étrangère pointant vers la super-classe.

En ce qui concerne la faiblesse d'identification, selon que nous sommes tenus ou non d'avoir chaque type de véhicule avec son propre identifiant, nous pourrions avoir un identifiant global dans la super-classe, ou comme dans notre diagramme, plusieurs identifiants, un pour chaque type de véhicule en plus de l'identifiant de la super-classe Vehicle qui identifie n'importe quel véhicule. Nous voyons donc que la faiblesse d'identification n'existe pas toujours, car elle dépend principalement du domaine et des exigences du problème.

Par exemple, si nous voyons des identifiants dans chacune des entités héritières, et que nous savons que ces identifiants peuvent servir de clés primaires, alors cela suggère que les entités héritières ont pu être implémentées avec une table chacune, où leur clé étrangère n'inclut initialement pas d'autres attributs de clé étrangère. Mais le diagramme conceptuel ne peut pas le garantir, car l'existence ou l'absence d'une clé étrangère pouvant ou non faire partie de la clé primaire lors de l'implémentation d'une hiérarchie est une décision de conception propre au niveau logique.

Un autre aspect que nous pouvons inférer du diagramme conceptuel est les associations 1-* où le 1 se trouve dans l'une des entités de la hiérarchie. Nécessairement, si une clé étrangère pointe vers la super-classe (le côté 1 de l'association est dans la super-classe), alors une table doit être implémentée pour elle.

D'un autre côté, si elle pointe vers l'une des entités héritières, ce n'est pas une condition suffisante pour inférer qu'il existe une table pour cette entité héritière. En effet, il peut y avoir une table représentant la super-classe avec cette entité héritière, la clé étrangère pointant parfaitement vers l'identifiant de cette table.

Ainsi, dans les hiérarchies IS-A du modèle conceptuel, le rôle "weak" n'est jamais utilisé pour indiquer une éventuelle faiblesse d'identification que les tables implémentant les entités pourraient avoir. Il existe de nombreuses façons d'implémenter la hiérarchie avec des tables, et la méthode choisie n'est pas déterminée à 100 % par le diagramme conceptuel.

Mais il est très important d'être clair sur le fait que les entités de la hiérarchie peuvent avoir des associations avec d'autres entités qui les rendent faibles en identification. Dans ce cas, même si elles font partie d'une hiérarchie IS-A, le rôle "weak" serait utilisé pour indiquer que l'entité est faible en identification (mais pas à cause de la hiérarchie – plutôt à cause d'une association avec une autre entité).

#### Entité Car

Semblable aux entités précédentes, nous avons Car, qui représente l'existence de voitures dans le système. Sa clé primaire est Plate (plaque d'immatriculation), que nous supposons unique pour chaque voiture. Comme nous pouvons le voir dans le DDL, le type de données de Plate est VARCHAR. Cela rend tout à fait possible que l'attribut fasse partie d'une clé primaire, car elles ne doivent pas nécessairement être entières ou numériques pour faire partie d'une clé. Tout type de données dont les valeurs sont uniques parmi les uplets stockés dans la table peut convenir.

```pgsql
CREATE TYPE CarFuelType AS ENUM ( 'gas', 'diesel', 'electric', 'hybrid', 'hydrogen' ); 
CREATE TABLE Car (
    Plate VARCHAR(32) PRIMARY KEY,
    FuelType CarFuelType NOT NULL,
    DoorCount INT NOT NULL CHECK (DoorCount >= 0),
    TrunkCapacity INT NOT NULL CHECK (TrunkCapacity >= 0),
    HorsePower INT NOT NULL CHECK (HorsePower >= 0),
    Doors INT NOT NULL CHECK (Doors > 0),
    AirConditioning BOOLEAN NOT NULL,
    VehicleID INT UNIQUE NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID)
);
```

En ce qui concerne les clés étrangères liées à cette entité, nous avons la même que précédemment, qui sert à référencer un uplet de Vehicle stockant des informations sur le modèle de voiture, sa couleur, etc. Mais en regardant le diagramme conceptuel, nous pouvons voir qu'il existe deux autres clés étrangères dans d'autres entités pointant vers Car, puisque le côté 1 des associations 1-* correspondantes se trouve dans Car.

Même si nous ne pouvons pas voir cela dans le DDL de la table Car, ces clés étrangères se trouvent dans d'autres entités référençant Car. Mais nous pouvons les voir dans le diagramme relationnel sous forme de flèches pointant vers les attributs de la clé primaire de Car.

Enfin, nous créons également un ENUM TYPE pour restreindre le domaine de l'attribut FuelType. Nous pourrions implémenter cela parfaitement avec une contrainte, mais pour réutiliser ce type de données dans d'autres entités qui pourraient en avoir besoin, nous devrions définir un DOMAIN ou un ENUM TYPE (comme dans ce cas, qui peut être affecté comme type de données à l'attribut).

De plus, définir un ensemble de valeurs de cette manière est particulièrement utile lorsque l'attribut contient du texte, car dans d'autres attributs numériques, il peut être plus facile de restreindre leurs valeurs possibles avec des conditions comme (HorsePower >= 0).

#### Entité CityBus

Pour en finir avec la hiérarchie des véhicules, nous avons CityBus, qui représente les bus urbains dans notre domaine. Dans cette entité, nous avons également Plate comme clé primaire, qui stocke la plaque d'immatriculation du bus et sert à l'identifier de manière unique (ce qui signifie qu'elle le différencie de tout autre bus urbain).

Mais la plaque d'immatriculation ne le différencie pas directement d'autres types de véhicules comme les voitures ou les vélos, car la sémantique de chaque attribut est différente pour chaque type de véhicule, comme mentionné précédemment.

Par exemple, bien que les voitures et les bus aient tous deux une plaque d'immatriculation, si nous essayons de différencier les voitures des bus à l'aide de leurs attributs Plate, nous verrons que les voitures peuvent avoir une structure de plaque d'immatriculation différente de celle des bus, comme déterminé par le domaine et les exigences du projet.

Ainsi, pour les distinguer et les identifier de manière unique, nous devons utiliser l'identifiant VehicleID, puisque Plate est spécifique aux types de véhicules Car et CityBus.

En plus de représenter l'existence des bus, cette entité possède des associations de type 1-* avec Person et City qui modélisent la personne conduisant chaque bus et la ville où il opère. Ainsi, dans le diagramme conceptuel, nous pouvons voir que l'association avec Person a le rôle **“drives”** (conduit). Cela indique qu'une personne peut conduire un nombre arbitraire de bus, tandis qu'un bus n'est conduit que par une seule et unique personne.

Cette association fait que **CityBus** possède une clé étrangère pointant vers Person, nous permettant de savoir, pour un bus donné, la personne qui le conduit en accédant à l'uplet Person référencé par l'attribut de clé étrangère.

De même, CityBus possède également une association avec City qui représente la ville à laquelle chaque bus appartient et opère. Conceptuellement, nous pouvons voir cela comme chaque bus devant opérer dans une seule ville, et chaque ville ayant un nombre arbitraire de bus opérant en elle, y compris aucun (puisque la cardinalité minimale du côté de CityBus est 0).

Logiquement, cela est implémenté avec une clé étrangère dans CityBus pointant vers City. Ainsi, si nous avons besoin de connaître la ville où opère un certain bus, nous vérifions simplement la valeur de sa clé étrangère, qui identifiera de manière unique un uplet dans City, indiquant la ville que nous recherchons.

```pgsql
CREATE TABLE CityBus (
    Plate VARCHAR(32) PRIMARY KEY,
    RouteNumber INT NOT NULL CHECK (RouteNumber >= 0),
    Seats INT NOT NULL CHECK (Seats > 0),
    FreeWifi BOOLEAN NOT NULL,
    VehicleID INT UNIQUE NOT NULL,
    DriverFK INT NOT NULL,
    CityFK INT NOT NULL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicle(VehicleID),
    FOREIGN KEY (DriverFK) REFERENCES Person(PersonID),
    FOREIGN KEY (CityFK) REFERENCES City(CityID)
);
```

En plus des clés étrangères précédentes, il en existe une autre dans l'entité BusTrip qui référence CityBus, que nous pouvons voir avec l'association de type 1-* qu'elle possède avec cette entité. Cette dernière n'est pas directement reflétée dans le DDL de CityBus, mais elle se trouve dans le diagramme relationnel où nous avons une flèche pointant vers la clé primaire Plate. Et, comme d'habitude, nous n'ajoutons pas la contrainte NOT NULL à l'attribut Plate, puisque nous imposons la contrainte PRIMARY KEY, qui inclut implicitement NOT NULL dans tous les attributs qui la composent.

Les clés étrangères pour Person et City ne peuvent pas non plus être NULL en raison des cardinalités minimales des associations, où le fait d'avoir 1..1 implique qu'un bus urbain doit avoir un conducteur et une ville pour opérer, d'où l'ajout explicite de NOT NULL dans le DDL.

#### Entité CarRegistration

Dans notre domaine, les voitures peuvent appartenir à une personne via un enregistrement dans la table Carownership. Elles peuvent également être enregistrées comme aptes à la conduite via CarRegistration, qui associe les voitures aux permis de conduire pour modéliser leur enregistrement légal. C'est-à-dire qu'une voiture peut exister à tout moment, mais pour pouvoir circuler, elle doit être enregistrée et associée à un permis de conduire. C'est pourquoi CarRegistration est dédiée à l'association des voitures aux permis de conduire.

L'entité est très similaire à certaines que nous avons vues auparavant, comme Residence (bien que les entités auxquelles elle se rapporte ici soient différentes, ainsi que la raison de son existence). Implicitement, une voiture peut être enregistrée et associée à de nombreux permis de conduire, tandis qu'un même permis de conduire peut avoir un nombre arbitraire de voitures qui lui sont associées. Nous pouvons le déterminer en observant les **cardinalités** et la **navigabilité** des associations dans le diagramme conceptuel.

Par exemple, si nous avons une voiture, alors en effectuant une recherche exhaustive dans les uplets de CarRegistration, nous pouvons savoir dans combien d'enregistrements elle figure ou a participé. De plus, pour chacun de ces enregistrements, nous connaissons automatiquement le permis de conduire auquel elle a été associée – ainsi, à partir d'une voiture, nous pouvons en apprendre davantage sur de nombreux permis de conduire.

Inversement, la même chose s'applique : si nous avons un certain permis, nous pouvons découvrir indirectement en regardant dans la table CarRegistration combien d'enregistrements associent des voitures à ce permis. Et pour chacun de ces enregistrements, nous obtiendrions la voiture associée.

Nous avons maintenant analysé la navigabilité au niveau logique. Auparavant, nous avons vu le concept de navigabilité au niveau conceptuel, où les associations ne pouvaient être parcourues que dans une certaine direction selon leur cardinalité. Mais dans le modèle logique, nous avons accès à tous les uplets de toutes les tables du schéma de la base de données.

Ainsi, même si l'association Car-CarRegistration n'est pas navigable vers CarRegistration au niveau conceptuel, elle l'est au niveau logique. C'est-à-dire que si nous avons une voiture, nous pouvons savoir quels uplets dans CarRegistration se réfèrent à cette voiture, en utilisant les clés étrangères qui implémentent l'association. Avec cette information, nous pouvons ensuite naviguer vers DrivingLicense une fois que nous savons quels uplets dans CarRegistration pointaient vers la voiture.

Ce type de navigation est considéré comme plus typique du niveau logique. Grâce à lui, nous pouvons obtenir des informations d'autres entités de manière plus large qu'avec le concept de navigation que nous avons vu au niveau conceptuel.

Ici, sur le **diagramme entité-relation**, nous pouvons voir qu'il existe une association N-M implicite entre Car et DrivingLicense, à travers laquelle nous venons de naviguer.

Pour ce faire, nous avons dû passer par les associations de type 1-*, qui sont divisées de sorte qu'il puisse y avoir une entité "intermédiaire" qui stocke les informations liées à l'association N-M, et pour permettre son implémentation au niveau logique. Mais nous devons garder à l'esprit les cardinalités des associations 1-* qui composent l'association N-M implicite, où du côté de CarRegistration nous avons une optionnalité car la cardinalité minimale est 0. Cela signifie qu'une voiture peut ne pas être enregistrée, il n'y aurait donc aucun uplet dans CarRegistration se référant à une certaine voiture, empêchant ainsi la navigation vers DrivingLicense.

Ceci est tout à fait valide car si une voiture n'est pas enregistrée, elle ne sera associée à aucun permis de conduire, et nous ne pourrons donc accéder à aucune information de DrivingLicense.

Malgré cela, puisqu'il y a une possibilité qu'elle soit enregistrée, nous considérons ces associations au niveau logique comme navigables (tout cela équivaut à l'analyser dans le sens opposé, de DrivingLicense vers Car via CarRegistration).

Pour que ce processus soit mené à bien, CarRegistration doit posséder deux clés étrangères : une pointant vers la clé primaire de Car pour identifier de manière unique la voiture enregistrée, et une autre pointant vers DrivingLicense pour identifier le permis de conduire associé à la voiture.

```pgsql
CREATE TABLE CarRegistration (
    RegistrationID SERIAL PRIMARY KEY,
    RegistrationDate DATE NOT NULL,
    ExpirationDate DATE NOT NULL CHECK (ExpirationDate > RegistrationDate),
    PlateFK VARCHAR(32) NOT NULL,
    LicenseFK INT NOT NULL,
    FOREIGN KEY (PlateFK) REFERENCES Car(Plate),
    FOREIGN KEY (LicenseFK) REFERENCES DrivingLicense(LicenseID)
);
```

Lors de l'implémentation de la table CarRegistration, nous voyons dans son DDL que la clé primaire est déclarée comme SERIAL car il s'agit d'une clé substitutive. De plus, les clés étrangères ont toutes la contrainte NOT NULL en raison de la multiplicité minimale de 1 pour les associations correspondantes, ce qui exige que chaque uplet de CarRegistration référence exactement une voiture et un permis de conduire.

En ce qui concerne les informations stockées dans l'enregistrement de la voiture, nous avons principalement la date d'enregistrement ou la date d'expiration. Aucune des deux ne peut être NULL, car nous supposons que dans notre domaine, les voitures sont toujours enregistrées pour une certaine période qui peut ensuite être prolongée par d'autres enregistrements.

Ici, nous aurions pu définir l'entité CarRegistration comme faible en identification, en incluant les deux clés étrangères dans une clé primaire comme **{RegistrationDate, PlateFK, LicenseFK}**. Mais par souci de simplicité, une clé substitutive est préférée, ce qui simplifie les opérations de base de données. En fait, le seul avantage de ne pas utiliser la clé substitutive serait d'économiser l'espace occupé par les valeurs de cette colonne supplémentaire (et nous pourrions la supprimer si nécessaire). Mais cela compliquerait l'identification des uplets de CarRegistration, et rendrait certaines requêtes moins efficaces et moins lisibles.

Et si nous approfondissions le niveau physique, nous nous rendrions compte que le fait d'avoir une clé primaire composée de plus d'attributs ferait que le SGBD utiliserait plus d'espace pour la gérer. Cela contrebalancerait les économies réalisées en supprimant la clé substitutive – la clé substitutive reste donc l'option préférée.

En résumé, au niveau conceptuel, nous avons appris que la navigation de Car vers DrivingLicense n'est pas tout à fait possible, car il n'y a pas de clé étrangère dans Car pointant vers CarRegistration. Mais au niveau logique, nous pouvons obtenir des informations de CarRegistration car nous pouvons examiner tous les uplets de CarRegistration, ce qui nous permet de savoir lequel d'entre eux a sa clé étrangère correspondante référençant la voiture dont nous sommes partis.

C'est-à-dire que, conceptuellement, les associations de type 1-* ne sont navigables que du côté "plusieurs" vers le côté "un", mais au niveau logique, elles sont considérées comme bidirectionnelles. De plus, les associations 1-* entourant CarRegistration sont toutes deux de type 1-* et donnent implicitement naissance à une association de type N-M, ce qui est une autre raison pour laquelle nous pouvons réellement naviguer de Car vers DrivingLicense via CarRegistration.

#### Entité DrivingLicenseRequest

Dans notre domaine, les gens peuvent demander un permis de conduire à une entité publique, ce qui dans ce cas ne nous importe pas – nous nous soucions seulement du fait qu'elle est responsable de l'acceptation ou du rejet de ces demandes. Si une demande est acceptée, elle doit devenir le permis de conduire de la personne qui l'a demandée, tandis que si elle est rejetée, elle restera dans la base de données comme une demande échouée.

Pour modéliser cela dans notre base de données, nous avons de nombreuses options :

* créer une entité **DrivingLicenseRequest** avec un attribut booléen **Accepted** pour représenter si le statut de la demande est accepté ou non, ou
    
* créer une hiérarchie IS-A comme on le voit dans le diagramme conceptuel, où nous avons une super-classe **DrivingLicenseRequest** dédiée à l'enregistrement de toutes les demandes qui existent ou ont existé. À leur tour, nous avons des entités héritières qui sont créées une fois que la demande a été résolue, une entité représentant les demandes acceptées et l'autre modélisant celles qui sont rejetées.
    

D'une part, l'utilisation d'une entité unique avec des attributs qui déterminent son statut n'est pas la meilleure option, car en plus de savoir si elle a été rejetée ou non, la demande peut être en cours de traitement. Cela signifierait qu'elle n'est ni acceptée ni rejetée pour le moment.

Cela cause de multiples problèmes qui compliquent l'implémentation, comme la nécessité de rendre l'attribut Accepted NULL jusqu'à ce que la demande ait été résolue, ou même d'utiliser cette valeur NULL pour représenter le statut de la demande. Cela "mélange" la sémantique de l'attribut Accepted avec la représentation du statut de la demande. Ce n'est pas nécessairement un problème grave, juste un manque de clarté dans la représentation du statut et de l'issue d'une demande.

Cette option générerait également des valeurs NULL dans les **attributs spécifiques** des demandes rejetées ou acceptées, puisque chacune d'elles nécessite des attributs spécifiques que l'autre type n'a pas (comme le **nombre de points** pour un permis de conduire accepté). Ainsi, avec cette option, en plus de distinguer le type de demande, vous devriez gérer les valeurs NULL dans tous les attributs qui ne correspondent pas au type représenté dans l'attribut **Accepted**. Et cela complique grandement la sémantique et les opérations lors de la gestion des données, en plus de gaspiller de l'espace inutile en stockant ces NULL.

D'un autre côté, l'utilisation d'une hiérarchie IS-A pour modéliser conceptuellement les demandes de permis de conduire peut apporter d'autres inconvénients, tels qu'une plus grande complexité dans le schéma due au nombre élevé de tables pouvant être générées. Vous pouvez également avoir plus de complexité lors de l'ajout de contraintes pour vous assurer qu'une demande n'est pas acceptée et rejetée en même temps. Ou vous pouvez même avoir une fragmentation des données sur plusieurs tables, où une partie de l'information est stockée dans une super-classe et le reste dans une entité représentant le type spécifique de demande, qu'elle soit acceptée ou rejetée.

Pourtant, l'utilisation d'une hiérarchie IS-A résout tous les problèmes que nous avons vus avec l'option précédente, offrant une sémantique plus simple et plus cohérente avec laquelle nous pouvons opérer plus facilement sur la base de données. Elle nous évite également d'avoir à nous soucier de la gestion des valeurs NULL dans certains attributs ou de la cohérence entre les attributs qui déterminent le statut de la demande, car il n'y en a pas ici.

Ainsi, dans le modèle conceptuel, nous avons une hiérarchie IS-A représentant ces demandes, où une super-classe représente les demandes qui viennent d'être créées et sont en cours de traitement. Dans les entités héritières, ces mêmes demandes sont représentées une fois qu'elles ont été résolues. Si elles sont rejetées, elles deviennent un type spécifique **RejectedDrivingLicense**, et si elles sont acceptées, un autre type appelé simplement **DrivingLicense**.

En d'autres termes, au niveau conceptuel, nous pouvons voir chaque demande comme un "individu" qui peut être trouvé dans l'ensemble des occurrences d'entités de la super-classe, indiquant que la demande est en cours de traitement. Lorsqu'elle est rejetée ou acceptée, cet individu appartient alors à l'ensemble de l'entité héritière correspondante.

#### Comment pouvons-nous modéliser la hiérarchie des demandes de permis de conduire au niveau logique ?

Comme nous l'avons vu précédemment, une hiérarchie IS-A n'a pas de traduction directe et unique au niveau logique, car sa sémantique et les exigences du domaine déterminent quelles possibilités sont meilleures ou pires dans des aspects tels que l'efficacité des requêtes, la facilité de gestion, etc.

Ainsi, pour traduire cette hiérarchie d'entités formée par l'entité super-classe **DrivingLicenseRequest** et les entités héritières **RejectedDrivingLicense** et **DrivingLicense** en tables dans un SGBD, nous devons analyser ses caractéristiques pour déterminer quelle implémentation convient le mieux au domaine que nous modélisons. Nous devons également analyser les autres entités et les associations qui s'y connectent, comme l'association entre Person et DrivingLicense, qui modélise la relation entre une personne et son permis de conduire.

La première chose que nous devons vérifier est si la hiérarchie est complète ou non. Dans ce cas, il peut y avoir des demandes en cours de traitement qui n'ont été ni acceptées ni rejetées, et qui ne sont donc représentées dans aucune des entités héritières.

Puisqu'il existe des demandes qui ne doivent pas nécessairement être représentées par une entité héritière, nous voyons que la hiérarchie n'est **pas complète (partielle)**. Étant donné qu'elle n'est pas complète, le seul moyen pour notre base de données de stocker correctement les demandes qui sont en cours de traitement est de créer une table spécifique pour la super-classe DrivingLicenseRequest. Sans elle, il serait plus compliqué de savoir quand une demande a été résolue ou non.

Plus tard, sachant que toutes les demandes sont stockées dans DrivingLicenseRequest, notre système doit pouvoir stocker des informations qui déterminent si elle a été résolue ou non, ainsi que le résultat de sa résolution. Pour cela, lorsqu'une demande est résolue et acceptée, une occurrence de l'entité DrivingLicense est créée. Mais si elle est rejetée, une occurrence de l'autre entité héritière est créée.

Ainsi, en aucun cas la demande ne sera représentée par des occurrences de plusieurs entités héritières en même temps, la hiérarchie est donc **disjointe**. Cela garantit que la décision précédente d'implémenter une table pour la super-classe est la bonne option.

Pour traduire les entités héritières au niveau logique, nous devons décider s'il faut implémenter une table pour chacune, une table unique pour les deux, ou même une table avec toutes les entités de la hiérarchie.

La chose la plus importante à considérer dans cette décision est le nombre d'attributs que possède chaque entité et les uplets que l'on s'attend à voir exister dans la base de données si nous implémentons une table pour chaque entité. En d'autres termes, nous devons considérer combien d'occurrences de chaque entité sont censées exister dans le domaine.

Initialement, nous pouvons supposer qu'il y a toujours plus de permis rejetés que de permis acceptés, car il est très probable d'être rejeté au moins une fois avant d'être accepté. Grâce à cela, nous pourrions décider d'implémenter une table pour les entités **DrivingLicenseRequest** et **RejectedDrivingLicense** ensemble (puisqu'il y a plus de rejetés que d'acceptés) et une autre pour DrivingLicense qui possède une **clé étrangère** pointant vers cette table. Mais cela générerait des valeurs NULL dans les attributs de RejectedDrivingLicense lors de la représentation des permis de conduire acceptés.

Comme l'implémentation de l'intégralité de la hiérarchie avec une seule table conduit également à trop de valeurs NULL dans les attributs lors de la représentation des permis acceptés ou rejetés, la meilleure solution dans ce cas est à nouveau d'implémenter une table pour chaque entité de la hiérarchie.

La raison principale du choix de cette option est le nombre de valeurs NULL générées lors de la représentation des permis acceptés ou rejetés. En général, si les entités héritières n'avaient qu'un seul attribut, alors il serait clair qu'elle pourrait être implémentée plus simplement avec une seule table pour toute la hiérarchie, ou deux.

Mais lorsqu'il y a plus d'un attribut, les requêtes deviennent particulièrement compliquées car nous devons vérifier si plusieurs attributs sont NULL en même temps (et gérer la base de données et l'extension possible de la hiérarchie à plus de types de demandes).

```pgsql
CREATE TABLE DrivingLicenseRequest (
    LicenseID SERIAL PRIMARY KEY,
    RequestDate DATE NOT NULL,
    Fee DOUBLE PRECISION NOT NULL CHECK (Fee >= 0),
    PersonFK INT NOT NULL,
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID)
);
```

Une fois que nous avons décidé d'utiliser une table pour chaque entité de la hiérarchie, nous devons refléter cette décision à la fois dans le diagramme relationnel et dans le DDL SQL. C'est principalement parce qu'elle n'est **pas complète**, **disjointe**, et possède de multiples attributs dans les entités héritières qui conduiraient à trop de valeurs **NULL**.

Ainsi, dans le diagramme relationnel, nous créons les tables correspondantes, où **DrivingLicense** et RejectedDrivingLicense ajoutent des clés étrangères pointant vers DrivingLicenseRequest pour identifier la demande qui a été rejetée ou acceptée.

En d'autres termes, toutes les demandes sont stockées dans la table super-classe. Ensuite, lorsqu'elles sont acceptées ou rejetées, un uplet est ajouté à la table correspondante afin que sa clé étrangère référence l'uplet DrivingLicenseRequest représentant la demande elle-même. De cette façon, la table super-classe est dédiée au stockage des demandes, tandis que les autres tables se concentrent sur la représentation des demandes qui ont été rejetées ou acceptées.

En ce qui concerne les clés étrangères pointant vers ou présentes dans l'une des tables de la hiérarchie, nous pouvons voir que pour savoir à quelle personne appartient une certaine demande, il existe une **clé étrangère** dans DrivingLicenseRequest pointant vers **Person**. Ainsi, pour chaque demande, cette clé étrangère indique la personne associée à cette demande.

D'un autre côté, étant donné les associations que nous voyons dans le diagramme conceptuel, il existe deux autres clés étrangères provenant d'autres entités pointant vers DrivingLicense. Nous devons tenir compte de tout cela car cela peut affecter la décision que nous avons prise précédemment sur la manière d'implémenter la hiérarchie. S'il y a des clés étrangères pointant vers la super-classe, par exemple, nous devrions nécessairement implémenter une table pour elle.

Enfin, nous identifions les demandes à l'aide d'une clé substitutive dans DrivingLicenseRequest, qui identifie de manière unique toutes les demandes, quel que soit leur statut. Nous pouvons également le voir dans les entités héritières, qui ne possèdent aucun type d'identification propre, mais sont censées être identifiées par la clé primaire de DrivingLicenseRequest.

En d'autres termes, même s'il n'y a pas d'identifiant clair dans les entités héritières, il est important de se rappeler que les attributs de la super-classe sont hérités. Ainsi, lorsque nous implémentons la hiérarchie au niveau logique, peu importe comment nous le faisons, nous le ferons toujours de telle sorte que chaque demande acceptée ou rejetée puisse être identifiée par la clé primaire de DrivingLicenseRequest. C'est la table qui stocke la demande résolue.

#### Entité RejectedDrivingLicense

En continuant avec la hiérarchie précédente, étant donné son implémentation, nous avons la table RejectedDrivingLicense, qui représente son entité correspondante. Ses uplets stockeront des informations concernant le rejet des demandes qui ont été refusées, telles que la date ou le motif du rejet.

De plus, pour savoir à quelle demande correspondent les informations de chaque uplet, il existe une clé étrangère pointant vers DrivingLicenseRequest, référençant spécifiquement l'uplet de cette table qui stocke le reste des informations de la demande (y compris la clé primaire qui l'identifie).

Pour éviter d'avoir à inclure une clé substitutive dans cette table ou à définir une clé primaire à partir des attributs de l'entité, nous choisirons la **clé primaire** comme étant la **clé étrangère** elle-même. Celle-ci référence à son tour la clé primaire de la table super-classe qui identifie de manière unique toutes les demandes, quel que soit leur statut.

Cela signifie que la table RejectedDrivingLicense est faible en identification, car elle nécessite la clé primaire de l'entité propriétaire DrivingLicenseRequest pour l'identifier. Mais comme nous l'avons vu précédemment, cela ne devrait pas être reflété dans le diagramme conceptuel car cette façon d'implémenter la hiérarchie n'est pas toujours unique. Ainsi, selon la façon dont nous le faisons, la table peut cesser d'être faible en identification.

En résumé, la variabilité qui existe lors de l'implémentation d'une hiérarchie IS-A avec des tables signifie que des concepts tels que la faiblesse d'identification ne sont pas indiqués dans le diagramme conceptuel, car ils ne sont générés que par certaines implémentations.

Généralement, si nous ne regardons que le diagramme, tout ce que nous pouvons faire est de considérer toutes les options disponibles pour implémenter la hiérarchie, d'analyser chacune d'elles, et même de décider laquelle implémenter au final. Mais c'est une décision que nous prenons et cela n'implique pas ce que nous avons représenté dans la hiérarchie du diagramme.

En d'autres termes, à partir du diagramme, il est impossible d'inférer quelle implémentation logique spécifique a été utilisée, bien que dans des cas très spécifiques, il puisse être plus facile et plus direct de "deviner".

![Diagramme entité-relation avec héritage incomplet et disjoint où AcceptedRequest est une sous-classe de Request. Image de l'auteur. ](https://cdn.hashnode.com/res/hashnode/image/upload/v1752916101394/f9b94685-4891-4174-b38d-35c6d164744b.png align="center")

Par exemple, supposons que nous ayons une hiérarchie avec une seule super-classe **Request** vers laquelle pointe une clé étrangère et une entité héritière **AcceptedRequest** qui est très similaire à celle de notre domaine. Nous pouvons voir au niveau conceptuel que la hiérarchie est incomplète, car il peut y avoir des demandes qui n'ont pas encore été acceptées. Elle est également disjointe, ce qui dans ce cas rend l'analyse de cet aspect de la hiérarchie non pertinente compte tenu du nombre d'entités héritières qu'elle possède.

Ainsi, comme elle est incomplète, nous aurons besoin d'une table pour la super-classe. De plus, pour éviter l'apparition de valeurs NULL si la hiérarchie est implémentée avec une seule table, nous utiliserons une table pour l'entité héritière.

Mais si la hiérarchie était complète, nous n'aurions qu'une seule façon claire d'implémenter la hiérarchie : avec une seule table. En effet, il n'y aurait jamais de NULL dans les attributs de AcceptedRequest, malgré l'option d'utiliser une table pour chaque entité et de compliquer la logique de la base de données en insérant un uplet dans chaque table pour chaque demande.

Avec cet exemple, nous voyons que dans des cas très spécifiques, il est possible d'inférer la manière la plus claire d'implémenter une hiérarchie au niveau logique, même s'il y aura toujours une certaine variabilité qui nous empêchera de "deviner" l'implémentation exacte choisie pour le SGBD. Enfin, il est également important de considérer l'identification des uplets avec lesquels nous modélisons la hiérarchie, où plusieurs options se présentent également.

D'une part, si le domaine ou les exigences dictent que certaines entités doivent avoir leurs propres identifiants, alors nous devrons les définir comme clés primaires des entités correspondantes. Dans notre domaine, toutes les demandes doivent être identifiées de manière unique par un attribut dans DrivingLicenseRequest, nous ajoutons donc une clé substitutive à cette entité.

Si les exigences nous disent que certains attributs d'une entité servent d'identifiant, alors nous les utiliserons comme clé primaire – mais ici, par souci de simplicité, nous supposons qu'il n'y a pas d'identifiant spécifique au domaine, et c'est nous qui ajoutons la clé substitutive comme identifiant pour stocker les données dans notre système.

D'un autre côté, si nous n'avons pas d'informations sur la manière dont les entités doivent être identifiées, alors nous avons la liberté de le faire comme nous le souhaitons, en fonction principalement de l'implémentation choisie au final.

Mais quelle que soit la source de cette identification, en général, tout revient à savoir si chaque entité héritière peut ou non être identifiée par ses propres attributs. Cela détermine si la table en laquelle elle se convertit au niveau logique est faible en identification ou non – car si nous décidons finalement de définir une clé primaire pour une entité héritière, alors nous l'implémenterons nécessairement avec une table concrète.

Comme vous pouvez le voir, l'identification de chaque entité peut nous donner des indices sur la manière dont la hiérarchie sera implémentée, mais ce n'est pas quelque chose d'univoque qui garantit toujours une seule façon de l'implémenter.

Parfois, c'est à nous de définir comment nous les identifions, et cela dépendra du nombre de tables que nous choisissons pour l'implémentation et de la manière dont nous les associons les unes aux autres.

```pgsql
CREATE TABLE RejectedDrivingLicense (
    LicenseID SERIAL PRIMARY KEY,
    RejectionDate DATE NOT NULL,
    ReapplicationDate DATE NOT NULL CHECK (ReapplicationDate >= RejectionDate),
    Reason VARCHAR(32) NOT NULL,
    FOREIGN KEY (LicenseID) REFERENCES DrivingLicenseRequest(LicenseID)
);
```

Dans le DDL correspondant à cette entité, nous voyons qu'une table spécifique est créée pour elle avec les attributs respectifs affichés dans le diagramme conceptuel. De plus, nous en incluons un qui sert de clé étrangère pour référencer l'uplet de DrivingLicenseRequest qui représente la demande rejetée (et sert également de clé primaire de cette table).

Nous pourrions inclure une clé substitutive ici aussi, mais comme nous avons déjà la valeur LicenseID de la table super-classe, nous n'avons pas besoin de le faire (et le domaine ne nous oblige pas à identifier les demandes rejetées de manière spéciale).

Nous ajoutons donc les contraintes PRIMARY KEY et FOREIGN KEY à cet attribut en même temps, de sorte qu'il ne puisse pas contenir de valeurs NULL en raison de la **restriction NOT NULL implicite** ajoutée par PRIMARY KEY. Il doit également référencer l'attribut **clé primaire LicenseID** de DrivingLicenseRequest.

Pour refléter cela dans le diagramme relationnel, nous pouvons simplement souligner l'attribut de clé étrangère, indiquant que la table est faible en identification et que cet attribut ne peut pas prendre de valeurs NULL. Mais pour indiquer clairement que d'autres attributs qui ne font pas partie de la clé (comme RejectionDate) ne peuvent pas être NULL, nous devons utiliser d'autres éléments comme des notes de marge ou toute autre technique qui reflète clairement cette condition.

```pgsql
CREATE ASSERTION RejectionDateConstraint CHECK (
    NOT EXISTS (
        SELECT *
        FROM RejectedDrivingLicense R
            JOIN DrivingLicenseRequest D USING (LicenseID)
        WHERE R.RejectionDate < D.RequestDate
    )
);
CREATE ASSERTION ApprovalDateConstraint CHECK (
    NOT EXISTS (
        SELECT *
        FROM DrivingLicense D
            JOIN DrivingLicenseRequest R USING (LicenseID)
        WHERE D.ApprovalDate < R.RequestDate
    )
);
```

Enfin, bien que nous définissions des contraintes sur la table – comme le fait que la date de nouvelle demande ne peut pas être antérieure à la date de rejet – il existe également d'autres contraintes (comme le fait que la date de rejet doit être postérieure à la date de demande).

Ces types de contraintes impliquant des informations provenant de plusieurs tables doivent être implémentés avec des assertions ou des déclencheurs (triggers). L'option la plus simple est d'utiliser des assertions comme illustré ci-dessus, bien que nous n'ayons pas encore implémenté les instructions ASSERTION dans PostgreSQL, donc tenter de les définir entraînera une erreur du SGBD. Il ignorera simplement ces définitions.

Nous choisirons donc de ne pas implémenter ces types de contraintes à ce stade, en supposant que les données insérées les respectent déjà par souci de simplicité.

```pgsql
CREATE ASSERTION NoSimultaneousApprovalRejection CHECK (
    NOT EXISTS (
        SELECT *
        FROM DrivingLicense d
            JOIN RejectedDrivingLicense r USING (LicenseID)
    )
);
```

De plus, les demandes acceptées et rejetées ne peuvent pas exister en même temps, donc avec cette assertion, nous pourrions prévenir cette incohérence. Fondamentalement, nous définissons ici qu'il ne peut y avoir aucun uplet dans DrivingLicense ou RejectedDrivingLicense avec le même LicenseID. Cela signifie qu'aucune demande (LicenseID) ne peut apparaître simultanément dans les deux tables, car le domaine exige que les personnes soumettent une nouvelle demande lorsque celle qu'elles ont soumise est rejetée.

#### Entité DrivingLicense

Pour conclure avec cette hiérarchie, lorsqu'une demande de permis de conduire est acceptée, un uplet est créé dans la table DrivingLicense avec laquelle nous avons implémenté son entité respective. Ainsi, l'objectif principal de cette entité est de modéliser le permis de conduire d'une personne, car une fois accepté, il peut être utilisé pour enregistrer des voitures, et est indirectement associé à la personne qui détient le permis.

Pour ce faire, tout d'abord, le DrivingLicense possède une clé étrangère pointant vers DrivingLicenseRequest, tout comme l'entité héritée précédente dans la hiérarchie. À son tour, la demande, quel que soit son statut, se réfère toujours à une personne via sa clé étrangère, pour modéliser à qui appartient le permis. Et pour que les voitures puissent être enregistrées en association avec le permis de conduire d'une personne, l'entité CarRegistration possède une clé étrangère pointant vers DrivingLicense, de sorte que chaque enregistrement se réfère nécessairement à un permis spécifique.

Nous pouvons voir tout cela dans le diagramme entité-relation grâce aux associations de type 1-*, ainsi que dans leurs cardinalités minimales. Mais nous ne pouvons pas inférer directement l'existence de la clé étrangère dans DrivingLicense, spécifique à l'implémentation de la hiérarchie, car nous pouvons implémenter la hiérarchie de nombreuses manières.

Pour comprendre ce dernier point, imaginez qu'on vous dise qu'il existe une clé étrangère dans DrivingLicense pointant vers une autre entité. Avec cette information, nous pouvons savoir directement que cette clé étrangère pointe vers la super-classe de la hiérarchie et existe en raison de l'implémentation où il y a au moins une table spécifique pour DrivingLicense.

C'est parce que le reste des associations de l'entité DrivingLicense sont de type 1-*, avec le 1 du côté de DrivingLicense – ces associations donnent donc lieu à des clés étrangères pointant vers DrivingLicense, et non l'inverse. En résumé, avec seulement le diagramme conceptuel, vous ne pouvez pas savoir exactement comment une hiérarchie a été implémentée, mais avec quelques informations supplémentaires, vous le pouvez.

```pgsql
CREATE TABLE DrivingLicense (
    LicenseID SERIAL PRIMARY KEY,
    ApprovalDate DATE NOT NULL CHECK (ApprovalDate <= CURRENT_DATE),
    Points INT NOT NULL CHECK (
        Points BETWEEN 0 AND 15
    ),
    FOREIGN KEY (LicenseID) REFERENCES DrivingLicenseRequest(LicenseID)
);
```

Le DDL de cette entité est très similaire au précédent, où nous avons une clé primaire composée de l'attribut **LicenseID**, également déclaré comme une clé étrangère qui identifie la demande qui a été acceptée. Cela fait référence à l'uplet dans la table super-classe où la demande est stockée et identifiée de manière unique, ainsi qu'aux propres attributs de l'entité.

Les contraintes de table dans ce cas déclarent que la date d'approbation doit être antérieure à la date actuelle, car il est impossible qu'une demande ait été acceptée à une date qui n'a pas encore eu lieu.

Pour cela, nous utilisons **CURRENT_DATE** pour obtenir la date actuelle en SQL et la comparer avec une autre date comme celle stockée dans l'attribut. Il y a aussi l'attribut Points, qui détermine les points restants sur le permis de conduire de la personne. Selon le domaine, cette valeur est un entier compris entre 0 et 15, nous restreignons donc les valeurs possibles qu'il peut prendre avec un CHECK, ainsi qu'avec le type de données INTEGER lui-même, l'empêchant de prendre des valeurs décimales.

Compte tenu de la simplicité du domaine de l'attribut, l'utilisation d'un CHECK est l'option la plus simple, bien que nous aurions pu définir un DOMAIN ou un TYPE ENUM et l'affecter comme type de données à l'attribut. Cela serait utile si nous avions plus d'attributs avec le même domaine dans le reste du schéma.

#### Entité BusTrip

Les personnes de notre domaine peuvent utiliser les bus CityBus comme moyen de transport. À cette fin, nous avons une entité appelée BusTrip qui modélise les itinéraires spécifiques que les bus empruntent à travers la ville. Chaque fois qu'un bus voyage d'un point à un autre, cela est considéré comme un trajet enregistré dans cette entité via un uplet. Cet uplet stocke des informations telles que les adresses de départ et d'arrivée du trajet, la date à laquelle il a lieu et le temps qu'il a fallu.

Pour identifier de manière unique les uplets de cette table, la clé primaire utilise les attributs TripDate, les adresses de départ et d'arrivée, et l'attribut de clé étrangère qui identifie le bus spécifique ayant effectué le trajet. Nous devons inclure la clé étrangère dans la clé primaire car il pourrait y avoir plusieurs BusTrips avec la même date et les mêmes adresses de départ et d'arrivée, tous effectués par des bus différents.

Ainsi, pour les distinguer de manière unique, nous devons inclure les informations du bus effectuant le trajet, ce qui signifie la valeur de la clé étrangère pointant vers CityBus.

En ce qui concerne la sémantique de cette entité, nous pouvons voir qu'aucun bus ne peut effectuer le même trajet plusieurs fois à la même date, car cela entraînerait des uplets en double, violant la contrainte de clé primaire. Nous supposons que c'est le cas en raison des caractéristiques du domaine.

Dans le processus de conception, nous devons parfois modéliser des situations qui ne sont pas forcément intuitives, comme un bus n'effectuant pas le même trajet plus d'une fois par jour.

Comme l'attribut **TripDate** est de type **DATE**, il ne peut stocker que des dates avec une résolution allant jusqu'aux jours. Cela signifie que nous ne pouvons pas représenter le moment exact où le trajet a lieu dans notre base de données (de la même manière que nous le pourrions en utilisant le type de données TIMESTAMP, qui permet de représenter des moments dans le temps avec la date et l'heure).

Ainsi, compte tenu de la granularité du type de données DATE, nous respectons la restriction selon laquelle un bus ne peut pas effectuer le même trajet plusieurs fois par jour (car dans ce cas, plusieurs uplets avec exactement la même date seraient stockés, puisque DATE ne peut représenter que jusqu'aux jours).

C'est un exemple de restriction qui est implicitement modélisée par le type de données de l'attribut lui-même. S'il s'agissait de TIMESTAMP, nous pourrions avoir plusieurs trajets par le même bus le même jour mais à des heures différentes.

```pgsql
CREATE TABLE BusTrip (
    TripDate DATE NOT NULL,
    StartAddress VARCHAR(32) NOT NULL,
    EndAddress VARCHAR(32) NOT NULL,
    Duration INT NOT NULL CHECK (Duration >= 0),
    PlateFK VARCHAR(32) NOT NULL,
    PRIMARY KEY (TripDate, StartAddress, EndAddress, PlateFK),
    FOREIGN KEY (PlateFK) REFERENCES CityBus(Plate)
);
```

Lors de la construction du diagramme relationnel, nous devons également souligner l'attribut de clé étrangère qui pointe vers **CityBus**, car il fait partie de la clé primaire (c'est l'entité faible en identification). Plus précisément, nous pouvons l'inférer du diagramme entité-relation en regardant où se trouve le rôle «weak», qui indique l'**entité propriétaire** de BusTrip, c'est-à-dire celle dont elle dépend pour l'identification.

Dans le DDL, cela se reflète dans les attributs qui composent la clé primaire, où l'on trouve les trois de la table elle-même et PlateFK, qui est la clé étrangère chargée de référencer le bus qui effectue le trajet. Nous n'imposerons aucune restriction supplémentaire sur les attributs StartAddress et EndAddress, même si n'importe quel texte ne peut pas y être stocké – seulement des textes représentant des adresses valides dans une ville (spécifiquement là où le bus opère).

Par souci de simplicité, nous supposerons que si une adresse n'est pas valide, il incombe à une autre partie du système de le vérifier, comme un logiciel dans la couche applicative qui valide les adresses avant d'insérer les uplets dans la base de données.

D'un autre côté, nous ajouterons la restriction de non-négativité sur la durée, car il n'est pas logique qu'elle soit négative. Nous pourrions nommer ces restrictions pour faciliter l'administration de la base de données, mais comme nous n'allons pas travailler dessus ici, nous ne le ferons pas.

#### Entité BusTicket

Pour qu'une personne puisse voyager sur une ligne de bus, elle doit avoir un ticket qui lui permet de monter à bord d'un bus représenté dans la table CityBus. Ainsi, dans notre domaine, nous modéliserons l'existence de tickets avec l'entité BusTicket. Son seul attribut est utilisé pour stocker l'horodatage (timestamp) de son émission.

Il est important d'utiliser le type de données TIMESTAMP ici et non DATE car une personne peut acheter plusieurs tickets le même jour pour différents itinéraires, c'est pourquoi nous devons clarifier quel ticket a été généré en premier.

Lorsque nous voyons comment cela est représenté dans le diagramme conceptuel, vous remarquerez peut-être la restriction XOR qui apparaît entre les associations reliant BusTicket à Person et BusPass. Cette restriction représente le fait que tous les tickets existants sont soit directement associés à une personne qui possède le ticket, soit associés à un BusPass qui appartient à une personne et permet plusieurs trajets avec un abonnement.

C'est ainsi que nous expliquerions sémantiquement la restriction que nous voulons modéliser – mais conceptuellement, lorsque nous avons une restriction représentée par une ligne pointillée et une condition logique comme XOR, cela signifie que soit l'association **BusTicket-Person** existe, soit l'association **BusTicket-BusPass** existe. Il n'est pas possible que ni l'une ni l'autre n'existe ou que les deux existent en même temps.

Parce que ces associations existent, la clé étrangère dans BusTicket pointant vers l'entité respective n'est pas NULL. C'est-à-dire que les deux associations sont de type 1-*, elles sont donc clairement implémentées avec des clés étrangères dans BusTicket. Mais les cardinalités minimales des deux côtés sont 0, indiquant que les associations dans leur ensemble peuvent ne pas exister. En d'autres termes, cela signifie que les valeurs des attributs de clé étrangère peuvent être NULL.

À ce stade, si nous n'avions pas la restriction XOR, les clés étrangères pourraient toutes deux être NULL en même temps, indiquant qu'un ticket n'est associé à aucune personne ou abonnement, ce qui rendrait impossible l'identification du passager effectuant le trajet.

D'un autre côté, si les deux clés étrangères avaient des valeurs dans leurs attributs, nous modéliserions le fait que la personne a utilisé l'abonnement pour voyager en bus via la non-nullité de la clé étrangère **BusTicket->BusPass**, tout en modélisant en même temps que la même personne n'a pas utilisé d'abonnement mais a obtenu un ticket directement via la non-nullité de **BusTicket→Person**.

C'est-à-dire que si la clé étrangère **BusTicket->BusPass** n'est pas NULL, alors nous modélisons la situation où une personne utilise son abonnement pour voyager en bus, tandis que l'autre clé étrangère, lorsqu'elle n'est pas NULL, représente que la personne n'utilise pas d'abonnement pour voyager mais le fait directement avec un ticket.

Ainsi, les deux situations ne peuvent pas se produire en même temps grâce aux restrictions du domaine qui dictent qu'une personne voyage soit avec un ticket, soit avec un abonnement – mais pas les deux à la fois, et pas aucun des deux. En effet, un titre de transport est nécessaire pour voyager. C'est pourquoi nous utilisons la condition XOR pour représenter que soit l'une des associations existe, soit l'autre, mais pas les deux en même temps. Elle interdit également qu'aucune n'existe.

| **PersonFK** | **PassFK** | **Valide** | **Signification** |
| --- | --- | --- | --- |
| Non NULL | NULL | ✔️ | Ticket acheté directement par la personne. |
| NULL | Non NULL | ✔️ | Ticket débité de l'abonnement BusPass de la personne. |
| NULL | NULL | ❌ | Il n'y a aucune information sur la personne qui voyage (ticket orphelin). |
| Non NULL | Non NULL | ❌ | Indique à la fois un achat direct et l'utilisation d'un abonnement en même temps (incohérent). |

Il est également important de souligner que pour que les clés étrangères puissent être NULL, la cardinalité minimale du côté de Person et BusPass dans les associations doit être 0.

Pour modéliser le fait qu'une personne voyage à l'aide d'un abonnement, nous pourrions envisager d'associer l'entité BusPass directement à BusTrip au lieu de BusTicket. Mais ce faisant, cela entraînerait une relation N-M entre BusPass et BusTrip, puisqu'un abonnement peut donner lieu à un nombre indéfini de trajets, tandis que plusieurs personnes peuvent voyager en utilisant leur abonnement sur un seul trajet.

Pour éviter d'avoir à ajouter une autre entité intermédiaire pour implémenter l'association N-M, nous associerons BusTicket à BusPass, afin de pouvoir voir chaque trajet effectué à l'aide d'un abonnement en vérifiant les valeurs de clé étrangère du ticket.

```pgsql
CREATE TABLE BusTicket (
    IssueTime TIMESTAMP,
    TripDateFK DATE,
    StartAddressFK VARCHAR(32),
    EndAddressFK VARCHAR(32),
    PlateFK VARCHAR(32),
    PersonFK INT,
    PassFK INT,
    PRIMARY KEY(
        IssueTime,
        TripDateFK,
        StartAddressFK,
        EndAddressFK,
        PlateFK
    ),
    FOREIGN KEY (
        TripDateFK,
        StartAddressFK,
        EndAddressFK,
        PlateFK
    ) REFERENCES BusTrip(TripDate, StartAddress, EndAddress, PlateFK),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID),
    FOREIGN KEY (PassFK) REFERENCES BusPass(PassID),
    CONSTRAINT XORConstraint CHECK (
        (
            PersonFK IS NULL
            AND PassFK IS NOT NULL
        )
        OR (
            PersonFK IS NOT NULL
            AND PassFK IS NULL
        )
    )
);
```

Pour identifier de manière unique chaque ticket, nous devons utiliser à la fois l'attribut IssueTime de la table et la clé étrangère pointant vers BusTrip, qui détermine quel trajet sera effectué avec ce ticket. Nous avons donc à nouveau une entité faible en identification – et elle est particulière en ce sens que la clé étrangère dans ce cas est composée de plusieurs attributs, puisque la clé primaire de BusTrip (qui est l'entité propriétaire dont elle dépend pour l'identification) est elle-même composée de plusieurs attributs. Plus précisément, cette clé primaire possède 4 attributs – donc dans BusTicket, comme la clé étrangère doit référencer la clé primaire de BusTrip, elle sera composée d'exactement 4 attributs (soit autant que la clé primaire vers laquelle elle pointe).

Pour déclarer cette clé étrangère, nous utilisons la même contrainte FOREIGN KEY que toujours, la seule différence étant qu'ici nous utilisons plusieurs attributs au lieu d'un seul.

La chose la plus importante concernant cette contrainte lorsque nous avons plusieurs attributs est de les déclarer dans l'ordre. Par exemple, si nous voulons que **TripDateFK** pointe vers l'attribut TripDate de la clé primaire BusTrip, alors nous devons mettre ces deux attributs dans le même ordre dans le uplet de la contrainte. Ici, par exemple, ils sont en première position, mais nous pourrions les placer tous les deux en deuxième position après **StartAddressFK** et **StartAddress**, ou en troisième (et ainsi de suite), tant qu'ils correspondent.

Comme c'est la seule clé étrangère qui ne peut pas être NULL dans la table, nous devons nous assurer que tous ses attributs ont la contrainte NOT NULL. Mais comme ils font partie de la clé primaire, nous n'avons pas besoin de déclarer explicitement la contrainte.

D'un autre côté, pour les autres clés étrangères qui modélisent les associations avec Person et BusPass, nous ne devrions pas ajouter cette contrainte car ces clés étrangères devront prendre une valeur NULL dans certaines situations. Aucun des attributs ne nécessite donc que nous déclarions des contraintes.

Enfin, le type de données TIMESTAMP n'est pas le seul capable de stocker la date et l'heure dans l'attribut IssueTime – nous avons également des alternatives comme DATETIME ou TIMESTAMP WITH TIME ZONE. Celles-ci ont des utilisations spécifiques, comme le stockage du fuseau horaire en plus de l'heure elle-même. Par souci de simplicité, dans cet exemple, nous utiliserons TIMESTAMP pour tous les attributs devant stocker la date et l'heure.

#### Entité BusPass

Nous pouvons déjà inférer la sémantique de cette entité à partir de ce que nous venons de voir. Plus précisément, si une personne prévoit d'effectuer plusieurs trajets en bus et ne veut pas acheter de tickets individuels pour chacun de ces trajets, elle peut acheter un abonnement (représenté par l'entité BusPass) qui lui permet d'effectuer plusieurs trajets sans se soucier des tickets.

Si nous regardons le diagramme conceptuel, nous verrons qu'il possède plusieurs associations de type 1-*, dont l'une est affectée par la restriction XOR. Ainsi, compte tenu des cardinalités minimales de cette association, elle peut ne pas exister, comme nous l'avons expliqué précédemment. Nous savons donc qu'il n'y aura pas toujours de clé étrangère pointant vers BusPass, puisque l'association est facultative en raison de ses cardinalités minimales.

Mais d'un autre côté, nous avons l'autre association avec Person qui donne lieu à une clé étrangère dans BusPass qui doit toujours exister, car tous les abonnements doivent avoir une personne associée (ce qui signifie que chaque abonnement doit avoir un propriétaire).

```pgsql
CREATE TYPE ModalityType AS ENUM( 'single', 'round_trip', 'daily', 'weekly', 'monthly', 'annual' ); 
CREATE TABLE BusPass (
    PassID SERIAL PRIMARY KEY,
    IssueDate DATE NOT NULL,
    ExpirationDate DATE NOT NULL CHECK (ExpirationDate > IssueDate),
    Modality ModalityType NOT NULL,
    RemainingTrips INT NOT NULL CHECK (RemainingTrips >= 0),
    PersonFK INT NOT NULL,
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID)
);
```

Pour l'identification de cette entité, nous incluons une clé substitutive pour simplifier le processus. Nous aurions pu sélectionner un autre ensemble d'attributs comme clé primaire, bien que cela rendrait l'entité faible en identification, ainsi qu'une clé primaire avec plus d'attributs qu'elle n'en a en utilisant une clé substitutive. La solution la plus simple est donc généralement préférée.

Nous devrions inclure un CHECK pour nous assurer que la date d'expiration de l'abonnement est postérieure à la date d'émission afin d'éviter d'insérer des uplets avec des dates incohérentes. De plus, aucun des attributs ne peut être NULL. La clé étrangère ne peut pas non plus être NULL en raison de la cardinalité minimale qui l'empêche d'être NULL. Et enfin, d'autres attributs comme la modalité ne peuvent pas être NULL non plus. Pour ceux-ci, nous implémentons un ENUM TYPE personnalisé où nous définissons les différentes modalités d'abonnement qui déterminent comment une personne peut utiliser cet abonnement.

Enfin, nous pouvons indiquer la contrainte que nous avons modélisée au niveau conceptuel avec un XOR de la même manière dans le diagramme relationnel en utilisant une ligne pointillée entre les clés étrangères impliquées. Nous pouvons également l'indiquer avec une note textuelle. Mais dans le DDL, la manière la plus simple de la coder est avec un CHECK dans BusTicket, qui est l'endroit d'où proviennent les clés étrangères impliquées dans la condition d'intégrité.

#### Entité Voyage

En continuant avec les façons dont les gens de notre domaine voyagent en croisière, nous avons l'entité Voyage. Celle-ci modélise les trajets effectués par les croisières. Plus précisément, l'entité stocke des informations sur le trajet, telles que les dates de départ et d'arrivée, ainsi que les ports où le trajet commence et se termine.

Nous pouvons également voir qu'elle possède un attribut appelé Distance, qui pourrait initialement sembler non pertinent – mais Distance enregistre la distance totale parcourue par la croisière pendant le trajet. Et cela ne doit pas nécessairement correspondre à la distance la plus courte entre les ports de départ et d'arrivée.

La décision d'utiliser cette signification pour cet attribut est venue de notre domaine et de ses contraintes. C'est-à-dire que si nous sommes tenus d'enregistrer la distance totale parcourue par la croisière, en plus de la distance entre les deux ports, l'option la plus simple consiste à ajouter un attribut dans cette entité qui enregistre cette magnitude.

En d'autres termes, si nous n'avions pas besoin de connaître la distance parcourue par la croisière elle-même, nous pourrions nous contenter de connaître la distance entre les ports de départ et d'arrivée (que nous pouvons déterminer à partir des informations sur les ports). Mais nous utiliserons ici l'attribut **Distance**, qui enregistre la distance réelle parcourue par la croisière pendant le trajet (puisque nous avons besoin de cette information).

Si nous regardons le modèle conceptuel, nous verrons que cette entité possède deux associations identiques de même type 1-* avec l'entité Port, le tout dans le but de modéliser conceptuellement qu'un voyage est associé à deux ports, un pour le départ et un pour l'arrivée, où les deux peuvent être les mêmes. Concernant ce dernier point, s'ils ne pouvaient pas être les mêmes, nous devrions indiquer cette restriction par une note, car il n'existe pas d'éléments standards dans un diagramme entité-relation ou dans le modèle relationnel pour représenter une telle situation.

D'un autre côté, nous pourrions également envisager de modéliser le trajet de sorte qu'il ait des ports de départ et d'arrivée via une seule association Voyage-Port avec une cardinalité de 2 du côté de Port. Mais si nous faisions cela, conceptuellement, nous ne distinguerions pas quel port était pour le départ et lequel était pour l'arrivée. Au contraire, nous modéliserions le fait que la croisière passe par deux ports lors de ce trajet – mais nous ne saurions pas avec certitude lequel était le port d'arrivée ou de départ (du moins au niveau conceptuel) puisqu'au niveau logique, il devrait nécessairement y avoir deux clés étrangères pointant vers Port.

Ainsi, pour distinguer facilement les ports d'arrivée et de départ d'un trajet et pour clarifier la sémantique de l'association entre Voyage et Port, nous utiliserons plusieurs associations, chacune avec un rôle indiquant explicitement la relation du port avec le trajet.

En plus de ces associations, l'entité Voyage doit référencer CruiseShip pour savoir quelle croisière a effectué ce trajet. C'est pourquoi, dans le diagramme conceptuel, il existe une association 1-* avec CruiseShip, où un navire de croisière peut effectuer de nombreux trajets, mais un trajet n'est effectué que par un seul navire de croisière.

Pour identifier cette entité, nous profiterons du fait que les dates de début et de fin du trajet sont toujours définies pour les inclure dans la clé primaire. Cela signifie que les deux dates ne peuvent pas être NULL car elles définissent la durée du trajet.

Mais, pour identifier réellement de manière unique les uplets de Voyage, nous devons les distinguer en utilisant les ports de départ et d'arrivée du trajet, ainsi que le navire de croisière qui l'effectue. C'est pourquoi nous incluons toutes les clés étrangères dans la clé primaire. Si nous ne le faisions pas, il pourrait y avoir plusieurs uplets de différents trajets effectués par différents navires de croisière ou passant par différents ports qui pourraient tout de même avoir la même valeur dans les dates de départ et d'arrivée. Nous devons donc inclure les informations du navire de croisière effectuant le trajet, ainsi que les ports impliqués.

En définissant la clé primaire de cette manière, nous rendons l'entité faible en identification, où ses entités propriétaires sont CruiseShip et Port, même si une partie de sa clé primaire est composée d'attributs de l'entité elle-même.

```pgsql
CREATE TABLE Voyage (
    DepartureDate DATE,
    ArrivalDate DATE CHECK (ArrivalDate >= DepartureDate),
    Distance DOUBLE PRECISION NOT NULL CHECK (Distance >= 0),
    DepartureNameFK VARCHAR(32) NOT NULL,
    DepartureCityFK INT NOT NULL,
    ArrivalNameFK VARCHAR(32) NOT NULL,
    ArrivalCityFK INT NOT NULL,
    ShipFK INT NOT NULL,
    PRIMARY KEY (
        DepartureDate,
        ArrivalDate,
        DepartureNameFK,
        DepartureCityFK,
        ArrivalNameFK,
        ArrivalCityFK,
        ShipFK
    ),
    FOREIGN KEY (ShipFK) REFERENCES CruiseShip(ShipID),
    FOREIGN KEY (DepartureNameFK, DepartureCityFK) REFERENCES Port(Name, CityFK),
    FOREIGN KEY (ArrivalNameFK, ArrivalCityFK) REFERENCES Port(Name, CityFK)
);
```

Pour implémenter cette entité au niveau logique, dans son DDL, vous pouvez voir que nous définissons d'abord les attributs de l'entité elle-même, ainsi que ceux de la clé étrangère pour le port de départ, qui sont **(DepartureNameFK, DepartureCityFK)**.

Notez que les clés étrangères pointant vers Port doivent avoir deux attributs puisque la clé primaire de Port possède deux attributs. Nous aurons donc besoin d'un total de 4 attributs pour modéliser les clés étrangères qui référencent les ports de départ et d'arrivée du trajet, les deux référençant les attributs Name et CityFK de la table Port (qui constituent sa clé primaire comme nous l'avons vu précédemment). De plus, nous avons besoin d'un autre attribut, ShipFK, pour référencer CruiseShip et ainsi déterminer quel navire de croisière a effectué le trajet.

Avec tout cela, la clé primaire de **Voyage** est définie comme l'ensemble d'attributs **(DepartureDate, ArrivalDate, DepartureNameFK, DepartureCityFK, ArrivalNameFK, ArrivalCityFK, ShipFK)**.

Si nous devions inférer les attributs qui composent la clé primaire en utilisant uniquement le diagramme conceptuel, nous devrions regarder les entités que les clés étrangères référencent. Celles-ci sont représentées par les associations 1-*.

Par exemple, dans CruiseShip, nous verrions que sa clé primaire n'a qu'un seul attribut, donc nécessairement dans Voyage, la clé primaire correspondante qui la référence doit avoir un attribut, ShipFK. Pendant ce temps, les deux autres clés étrangères qui référencent Port doivent avoir deux attributs chacune, puisque nous pouvons voir que Port est identifié par son nom et la ville où il se trouve. Sa clé primaire possède donc deux attributs **(Name, CityFK)** que nous devrons référencer depuis **Voyage**.

Dans le diagramme relationnel, c'est plus facile à interpréter. Nous verrons qu'un attribut référence un attribut de la table CruiseShip, nous savons donc qu'il s'agit d'une clé étrangère qui mène à une association 1-* dans le modèle conceptuel.

De plus, il existe deux autres attributs qui ensemble référencent deux attributs de Port – et ensemble, ils forment également une clé étrangère qui crée une association 1-* dans le diagramme conceptuel, où le côté "plusieurs" se trouve dans l'entité d'où provient la clé étrangère (c'est-à-dire dans Voyage).

Avec cette dernière clé étrangère, nous pouvons représenter le port de départ du trajet. Il existe une autre paire d'attributs **(ArrivalNameFK, ArrivalCityFK)** qui suivent le même modèle pour représenter le port d'arrivée du trajet. À partir d'eux, nous pouvons également inférer qu'au niveau conceptuel, il existe une autre association ayant les mêmes caractéristiques.

Et, puisque toutes ces clés étrangères sont soulignées, cela implique qu'elles font partie de la clé primaire de Voyage. De là, nous pouvons inférer que Voyage est faible en identification.

Enfin, si nous regardons les types de données des clés étrangères, nous verrons qu'ils correspondent exactement aux types des attributs qu'ils référencent. C'est particulièrement important car une clé étrangère, par définition, est un attribut qui détient la valeur d'un autre attribut qu'il référence, les deux doivent donc être du même type pour que cela soit possible.

Comme les clés étrangères sont composées de plusieurs attributs, dans ce cas, nous devons également considérer l'ordre relatif des attributs qui forment la clé étrangère avec l'ordre des attributs qu'ils référencent. C'est différent de ce qui se passe dans la contrainte PRIMARY KEY, où l'ordre dans lequel les attributs de la clé primaire sont déclarés n'a pas d'importance. Dans ce cas, dans PRIMARY KEY, nous déclarons un ensemble d'attributs, où ce qui compte est qu'ils apparaissent dans la contrainte (pas qu'ils suivent un ordre spécifique).

#### Entité CruiseBooking

Pour qu'une personne puisse voyager sur une croisière, elle doit effectuer une réservation pour un voyage spécifique. Ainsi, dans notre domaine, nous avons l'entité CruiseBooking, qui est chargée de stocker les réservations que les gens effectuent pour voyager sur une croisière.

Les données stockées pour chaque réservation incluent la date de réservation, le numéro de cabine, le prix et le mode de paiement. Pour savoir quelle personne a réservé quel voyage, l'entité possède des associations 1-* avec Person et Voyage, qui se traduisent logiquement par deux clés étrangères pointant vers les entités respectives.

Pour identifier de manière unique chaque réservation, nous pourrions choisir l'option facile consistant à inclure un attribut de clé substitutive pour servir de clé primaire. Mais pour illustrer la complexité de ne pas le faire, nous n'utiliserons que des attributs de la table elle-même pour identifier ses uplets. Ainsi, la clé primaire de cette entité est composée des attributs BookingDate, CabinNumber, de la clé étrangère vers Person et de l'autre clé étrangère vers Voyage.

Nous faisons cela parce que nous supposons que plusieurs personnes peuvent réserver la même cabine pour le même voyage, le tout à la même date. Par exemple, cela peut arriver si plusieurs personnes d'une même famille décident de réserver un certain voyage. Chacune de ces personnes aura un enregistrement ou un uplet dans la table CruiseBooking avec les mêmes attributs dans BookingDate, CabinNumber et la clé étrangère de Voyage, mais une valeur différente dans la clé étrangère de Person. Cela permet de distinguer les uplets de manière unique.

La clé étrangère vers Person possède un seul attribut puisque la clé primaire de Person n'a qu'un seul attribut. Mais l'autre clé étrangère qui se réfère au voyage réservé possède exactement 7 attributs (car l'entité Voyage nécessite 7 attributs pour être identifiée de manière unique).

Grâce à cela, nous nous rendons compte que la clé primaire de CruiseBooking aura un total de 10 attributs, ce qui en fait une solution beaucoup plus complexe que le simple fait d'utiliser une clé substitutive. Vous pouvez donc voir pourquoi il est très pratique d'utiliser des clés substitutives chaque fois que possible pour ce type d'entité – surtout lorsque les clés étrangères qui feront partie de la clé primaire possèdent trop d'attributs, comme dans ce cas.

```pgsql
CREATE TYPE PaymentMethodType AS ENUM ('card', 'paypal', 'bank', 'cash', 'mobile');
CREATE TABLE CruiseBooking (
    BookingDate DATE NOT NULL,
    CabinNumber INT NOT NULL CHECK (CabinNumber > 0),
    Price DOUBLE PRECISION NOT NULL CHECK (Price >= 0),
    PaymentMethod PaymentMethodType NOT NULL,
    PersonFK INT NOT NULL,
    DepartureDateFK DATE NOT NULL,
    ArrivalDateFK DATE NOT NULL,
    DepartureNameFK VARCHAR(32) NOT NULL,
    DepartureCityFK INT NOT NULL,
    ArrivalNameFK VARCHAR(32) NOT NULL,
    ArrivalCityFK INT NOT NULL,
    ShipFK INT NOT NULL,
    PRIMARY KEY (
        BookingDate,
        CabinNumber,
        PersonFK,
        DepartureDateFK,
        ArrivalDateFK,
        DepartureNameFK,
        DepartureCityFK,
        ArrivalNameFK,
        ArrivalCityFK,
        ShipFK
    ),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID),
    FOREIGN KEY (
        DepartureDateFK,
        ArrivalDateFK,
        DepartureNameFK,
        DepartureCityFK,
        ArrivalNameFK,
        ArrivalCityFK,
        ShipFK
    ) REFERENCES Voyage(
        DepartureDate,
        ArrivalDate,
        DepartureNameFK,
        DepartureCityFK,
        ArrivalNameFK,
        ArrivalCityFK,
        ShipFK
    )
);
```

Si nous regardons le DDL, il semble beaucoup plus complexe que les précédents. Mais en réalité, les éléments que nous avons utilisés sont les mêmes. Nous définissons la clé primaire avec PRIMARY KEY, et les attributs des clés étrangères avec les mêmes types de données que les attributs qu'ils référencent. Nous utilisons également la contrainte NOT NULL pour implémenter correctement ce qui est indiqué dans les cardinalités minimales des associations.

Nous déclarons chaque clé étrangère avec FOREIGN KEY, ce qui est plus long dans ce cas en raison du nombre d'attributs qui composent chacune d'elles. La seule chose importante à garder à l'esprit ici est que l'une des FOREIGN KEY est exclusivement dédiée à la déclaration de la clé étrangère vers Person (ce qui signifie l'association entre CruiseBooking et Person) tandis que l'autre modélise l'association avec Voyage.

Nous faisons cela sans mélanger les attributs des deux clés étrangères dans la même FOREIGN KEY – car ce serait une erreur puisque nous ne modéliserions pas correctement le diagramme conceptuel. Chaque clé étrangère est indépendante des autres, donc chaque FOREIGN KEY inclut uniquement les attributs qui composent chaque clé étrangère correspondante.

Pour simplifier le domaine de l'attribut PaymentMethod, nous pouvons définir un TYPE ENUM, puisque le mode de paiement est un attribut qui sera probablement utilisé dans d'autres parties du domaine. Même s'il n'est pas nécessaire maintenant, il est possible que dans une future extension du domaine, nous devions l'inclure dans le schéma. C'est pourquoi il est important de le déclarer pour faciliter la gestion de la base de données lors d'une extension potentielle.

#### Entité Pool

Dans notre domaine, il existe également des piscines, qui sont représentées dans la hiérarchie IS-A avec l'entité Pool comme super-classe. Cela permet aux gens d'interagir avec les piscines de différentes manières, comme nous le verrons ci-dessous. Nous considérons donc que notre domaine inclut différents types de piscines, telles que les piscines de croisière situées sur les navires de croisière modélisés avec CruiseShip, les piscines municipales situées dans les villes, ou les piscines olympiques également situées dans les villes.

Comme elles partagent toutes des attributs communs, nous faisons la même chose que dans la hiérarchie Vehicle, en utilisant une super-classe qui inclut ces attributs communs comme le nom de la piscine, son adresse, les profondeurs minimale et maximale, ou l'état actuel de la piscine.

Nous incluons également une association **1-*** entre **Pool** et **City** pour représenter que toutes les piscines sont situées dans une ville – sauf pour celles de type **CruiseShip**, qui se trouvent sur un navire de croisière et non dans une ville. Dans ce cas précis, la sémantique de l'association est différente, comme nous le verrons plus tard. À partir de là, nous pouvons définir différents types de piscines avec des caractéristiques distinctes, où toutes héritent de tous les attributs de leur super-classe, y compris l'association avec **City**.

Comme nous pouvons le voir, **CityPool** et **OlympicPool** n'ont aucun problème avec cela, mais **CruisePool** modélise les piscines sur les navires de croisière, son association avec City n'a donc pas la même sémantique que les autres. En d'autres termes, la piscine n'est pas située dans une ville mais sur un navire de croisière – nous supposons donc que la ville associée est son lieu de fabrication.

Comme vous pouvez le deviner, ce n'est pas la seule façon de modéliser ce domaine, ni la meilleure, puisque la sémantique "locatedAt" (situé à) indiquée dans l'association du diagramme conceptuel entre **City** et **Pool** ne capture pas le sens de cette relation lorsque la piscine est de type CruisePool. Mais une fois que nous avons clarifié cela, le modèle est correct dans le sens où tous les éléments essentiels sont représentés correctement, même si ce n'est pas de la meilleure façon possible.

#### Comment pouvons-nous traduire les entités de la hiérarchie des piscines au niveau conceptuel en tables ?

Une fois que nous avons clarifié la sémantique de la hiérarchie, nous pouvons suivre le même processus qu'auparavant pour l'implémenter au niveau logique.

![Partie du diagramme entité-relation où la hiérarchie IS-A des piscines est représentée selon leur type. Image de l'auteur.](https://cdn.hashnode.com/res/hashnode/image/upload/v1754731726248/2494ed94-aca0-401d-abe5-1e91481f336a.png align="center")

Tout d'abord, nous notons que la hiérarchie n'est pas complète, car nous supposons que dans notre domaine il existe de nombreux types de piscines, dont nous ne modélisons que 3 avec des entités spécifiques, tandis que les autres sont des piscines modélisées avec des occurrences de l'entité Pool.

En d'autres termes, si une piscine est l'un des types des **entités héritières**, elle sera représentée comme une occurrence de cette entité, tandis que si elle est d'un type différent, elle sera représentée par une **occurrence de la super-classe**. Ainsi, dans la hiérarchie, les piscines ne sont pas tenues d'appartenir aux entités héritières, ce qui la rend **incomplète**.

D'un autre côté, les types de piscines sont tous disjoints, ce qui signifie qu'une piscine ne peut pas être à la fois olympique et de croisière, ou municipale et olympique en même temps. La hiérarchie est donc disjointe car aucune piscine ne sera de plusieurs types à la fois.

Tout comme dans la hiérarchie DrivingLicenseRequest, les piscines ici sont également identifiées de manière unique avec une clé substitutive dans l'attribut PoolID, tandis que le reste des entités de la hiérarchie ne possède initialement aucun type d'identification.

Cela pourrait nous amener à penser que la meilleure façon d'implémenter la hiérarchie est, une fois de plus, avec une table pour chaque entité. Mais ce n'est pas nécessairement le cas car une seule table peut être utilisée pour implémenter plusieurs entités à la fois, en utilisant l'identifiant de la table pour distinguer les entités. En effet, nous supposons que le domaine n'impose aucune restriction, contrairement à la hiérarchie Vehicle où chaque type de véhicule devait avoir son propre identifiant.

En ce qui concerne la décision d'implémenter une table pour la **super-classe**, chaque fois que nous avons une **hiérarchie incomplète**, nous aurons besoin d'une table spécifique pour la super-classe – spécifiquement pour stocker les informations sur les piscines qui n'appartiennent à aucun type présent dans les entités héritières. Cela signifie que nous devons inclure une **table Pool**.

Plus tard, pour décider d'utiliser cette table pour implémenter toutes les entités de la hiérarchie, seulement certaines d'entre elles, ou d'inclure une table pour chaque entité héritière, nous devons regarder le nombre d'attributs que possèdent les entités héritières. Dans ce cas, nous voyons qu'elles ont trop d'attributs, en particulier CruisePool et CityPool, l'option la plus simple est donc d'implémenter une table pour chaque entité de la hiérarchie.

Une autre option que nous aurions serait d'utiliser la table Pool pour représenter également OlympicPool (qui possède le moins d'attributs) et de modéliser le reste des entités avec des tables spécifiques. Mais cela présente des inconvénients, comme la division dans la façon dont nous représentons chaque type de piscine.

Par exemple, alors que nous représentons OlympicPool avec certains attributs dans Pool qui peuvent ou non être NULL selon que la piscine est de ce type, les autres types de piscines seraient représentés différemment. Cela peut être déroutant lors de l'interrogation de la base de données.

Nous devons également considérer que certaines clés étrangères pointent vers OlympicPool, de sorte que ces clés étrangères ne seraient valides que pour les uplets de Pool dont les attributs correspondants **SpectatorMaxCapacity** et **CompetitionLanes** ne sont pas NULL, ce qui complique grandement la gestion de la base de données, crée plus de contraintes et complique éventuellement certaines requêtes.

Cependant, peu importe la complexité de cette option, il serait possible de l'implémenter, et elle serait tout aussi valide que l'implémentation d'une table pour chaque entité. C'est-à-dire que la complexité d'une implémentation peut la rendre irréalisable mais pas incorrecte – tant que les contraintes correspondantes sont définies pour maintenir l'intégrité des données.

Ainsi, même si dans ce cas l'option la plus simple est d'utiliser une table par entité, cela ne signifie pas qu'il n'existe pas d'autres manières correctes d'implémenter la hiérarchie. Cela signifie qu'à partir du diagramme entité-relation, nous ne pouvons pas inférer la manière exacte dont elle est finalement implémentée, bien que cela puisse être utile pour prendre cette décision.

```pgsql
CREATE TYPE PoolStatusType AS ENUM ('open', 'closed', 'maintenance', 'renovation');
CREATE TABLE Pool (
    PoolID SERIAL PRIMARY KEY,
    Name VARCHAR(32) NOT NULL,
    Address VARCHAR(32) NOT NULL,
    MinDepth INT NOT NULL CHECK (MinDepth >= 0),
    MaxDepth INT NOT NULL CHECK (MaxDepth >= MinDepth),
    Status PoolStatusType NOT NULL,
    CityFK INT NOT NULL,
    FOREIGN KEY (CityFK) REFERENCES City(CityID)
);
```

Après avoir décidé comment traduire la hiérarchie au niveau logique, nous ajoutons la table au diagramme relationnel et la codons dans le DDL SQL. Comme vous pouvez le voir, elle est très similaire à la table Vehicle, avec une clé substitutive comme identifiant, les attributs d'entité qui caractérisent toutes les piscines, et une clé étrangère qui référence la table City. Cela détermine la ville où se trouve la piscine (ou son lieu de fabrication dans le cas d'une piscine de type CruisePool).

En ce qui concerne l'état de la piscine, nous pouvons voir qu'il est modélisé ici avec un attribut **Status**. Nous définissons un ENUM TYPE pour celui-ci afin de limiter son domaine. Cette décision de conception est justifiée car dans cette hiérarchie, nous représentons les types de piscines dans les entités héritières, pas leurs états. Ainsi, pour représenter les états des piscines, nous devrons utiliser un mécanisme différent de la **généralisation/spécialisation**, comme un simple **attribut Status**.

Il existe d'autres façons de modéliser cela, mais elles seraient plus complexes. Cela ne les rend pas fausses, mais nous n'en discuterons pas et ne les montrerons pas ici.

Pour représenter le type de données de cet attribut dans le diagramme entité-relation, nous avons choisi de définir une entité **«Enum»** en UML avec les valeurs possibles que l'attribut peut prendre. Les entités de type **«Enum»** servent le même but que l'utilisation d'un TYPE ENUM en SQL. Cela définit un ensemble de valeurs qui peuvent ensuite être utilisées comme type de données pour un attribut, restreignant ainsi son domaine.

Mais en général, cela n'a pas besoin d'être entièrement spécifié au niveau conceptuel. Nous aurions pu simplement utiliser **string** comme type de données et omettre cette entité **«Enum»**, en limitant son domaine plus tard au niveau logique. Ou plutôt, lorsque le modèle logique est implémenté dans le SGBD.

Pourtant, si nous voulons que notre conception soit aussi claire et auto-descriptive que possible à tous les niveaux, nous devrions indiquer les valeurs possibles que les attributs peuvent prendre à tous les niveaux, car la restriction du domaine impose implicitement une contrainte d'intégrité. Nous pouvons le faire via des entités «Enum», des notes latérales ou en utilisant d'autres éléments UML standards applicables.

#### Entité CruisePool

Tout comme nous l'avons fait dans la hiérarchie Vehicle, ici chaque type de piscine est représenté par une table dédiée. De cette façon, lors de l'enregistrement d'une nouvelle piscine de type CruisePool dans notre système, un uplet sera créé dans cette table où les données caractérisant les piscines de croisière sont stockées. Mais les données qui la caractérisent en tant que piscine ne seront pas stockées là, car elles ne peuvent être stockées que dans la table Pool.

Ainsi, pour modéliser logiquement l'héritage de tous les attributs de Pool vers le type spécifique de piscine, nous utiliserons une clé étrangère pour pointer vers l'uplet Pool qui contient le reste des informations de la piscine. Plus précisément, nous choisirons PoolID comme clé étrangère, car c'est l'identifiant des piscines dans notre système. Nous le déclarons comme le même type SERIAL pour référencer ce même attribut dans la table Pool, où il est la clé primaire.

Comme vous pouvez le deviner, la table Pool ne stocke pas seulement des informations sur les piscines qui ne sont pas spécifiquement modélisées dans notre système, mais elle contient également des informations sur les piscines de chacun de ces types. Ainsi, si nous voulons obtenir des informations sur toutes les piscines de notre système, quel que soit leur type, il nous suffit d'interroger la table Pool.

Ceci est possible parce que nous avons une table pour la super-classe, alors que dans d'autres hiérarchies nous pourrions ne pas l'implémenter, ce qui nous obligerait à interroger plusieurs tables pour obtenir des informations sur toutes les piscines du système. Ce n'est pas nécessairement un problème, mais c'est un point à considérer lors de l'implémentation de la hiérarchie ou même de la modélisation de certains aspects de notre domaine avec des hiérarchies.

Par exemple, si nous avons une Pool et que nous voulons connaître son type, nous devons vérifier le reste des tables de la hiérarchie pour voir s'il existe un uplet référençant cette piscine. Cela entraîne une opération très coûteuse en termes de calcul car elle doit parcourir toutes les données stockées. Si notre système doit privilégier l'efficacité dans une telle requête, il serait utile de modifier l'implémentation de la hiérarchie pour s'assurer que cette requête s'exécute le plus rapidement possible.

Par exemple, l'ajout d'un attribut redondant dans Pool pour indiquer le type, même s'il introduit une redondance et un espace supplémentaire inutile, peut grandement optimiser la latence de certaines requêtes. Assurez-vous simplement de prendre ces décisions en fonction des exigences du projet, telles que la latence que les requêtes doivent avoir, l'espace que la base de données doit occuper, etc.

```pgsql
CREATE TABLE CruisePool (
    PoolID SERIAL PRIMARY KEY,
    DeckNumber INT NOT NULL CHECK (DeckNumber >= 0),
    MaxCapacity INT NOT NULL CHECK (MaxCapacity >= 0),
    WaterTemperature DOUBLE PRECISION NOT NULL,
    SlideCount INT NOT NULL CHECK (SlideCount >= 0),
    ShipFK INT NOT NULL,
    FOREIGN KEY (PoolID) REFERENCES Pool(PoolID),
    FOREIGN KEY (ShipFK) REFERENCES CruiseShip(ShipID)
);
```

En plus de la clé étrangère pointant vers Pool (qui sert également de clé primaire, rendant cette table faible en identification avec Pool comme entité propriétaire), nous avons une autre clé étrangère référençant CruiseShip pour déterminer la croisière sur laquelle se trouve la piscine. Et, puisque toutes les piscines de croisière doivent se trouver sur un navire de croisière pour être de ce type, la clé étrangère pointant vers CruiseShip ne peut pas être NULL. Elle doit toujours référencer une croisière valide. C'est pourquoi nous incluons la contrainte NOT NULL, ce que nous ne faisons pas pour PoolID car nous le déclarons comme clé primaire.

#### Entité CityPool

Un autre type de piscine que nous pouvons trouver est une piscine municipale, représentée par l'entité CityPool et implémentée avec sa table spécifique. Son DDL est très similaire au précédent, avec la particularité que dans ce cas, nous avons une clé étrangère pointant vers CityPool, qui peut être directement inférée de l'association de type 1-* reliant CityPool à Entry dans le diagramme conceptuel.

```pgsql
CREATE TABLE CityPool (
    PoolID SERIAL PRIMARY KEY,
    MaxCapacity INT NOT NULL CHECK (MaxCapacity >= 0),
    AnnualBudget DOUBLE PRECISION NOT NULL CHECK (AnnualBudget >= 0),
    AccessibilityFeatures VARCHAR(32) NOT NULL,
    FreeWifi BOOLEAN NOT NULL,
    FOREIGN KEY (PoolID) REFERENCES Pool(PoolID)
);
```

Dans le diagramme relationnel, il est important que la clé étrangère PoolID soit soulignée, indiquant que cet attribut, bien qu'étant une clé étrangère, est utilisé pour identifier de manière unique les uplets de CityPool. Cela signifie que lors du référencement de la clé primaire de PoolID, la clé étrangère qui s'y réfère contient exactement la valeur qui identifie la piscine dans Pool.

Ainsi, si une requête a simplement besoin de l'identifiant d'une piscine d'un type spécifique, nous n'avons pas besoin d'accéder à la table Pool, car l'attribut de clé étrangère de la table CityPool, CruisePool ou OlympicPool, par exemple, suffit pour le connaître.

Il arrive même que nous puissions accéder à des données d'autres tables qui sont indirectement associées via plus de niveaux d'association, comme dans CruiseBooking, où nous pouvons accéder à l'identifiant d'un CruiseShip via la valeur de sa clé étrangère, qui ne pointe pas directement vers CruiseShip, mais vers Voyage.

#### Entité OlympicPool

Concernant le dernier type de piscine de notre schéma, il y a OlympicPool, qui représente les piscines olympiques. L'implémentation de cette entité sous forme de table est la même que les précédentes, à la différence que dans le diagramme entité-relation, nous pouvons voir qu'il existe deux clés étrangères pointant vers OlympicPool. Sinon, les seules différences résident dans les attributs qui caractérisent le type de piscine.

```pgsql
CREATE TABLE OlympicPool (
    PoolID SERIAL PRIMARY KEY,
    SpectatorMaxCapacity INT NOT NULL CHECK (SpectatorMaxCapacity >= 0),
    CompetitionLanes INT NOT NULL CHECK (CompetitionLanes > 0),
    FOREIGN KEY (PoolID) REFERENCES Pool(PoolID)
);
```

#### Entité Entry

En continuant avec ce qu'une personne peut faire dans une piscine de notre système, nous avons l'entité Entry. Celle-ci est chargée de stocker les tickets qu'une personne peut utiliser pour entrer dans une piscine municipale, c'est-à-dire une piscine représentée uniquement par l'entité CityPool.

Pour s'assurer qu'une personne ne peut accéder à une piscine municipale qu'avec ces tickets, l'entité possède une association 1-* avec CityPool, et non directement avec Pool, car cela donnerait accès à n'importe quelle piscine quel que soit son type. De plus, pour savoir à quelle personne appartient le ticket, elle possède également une association 1-* avec Person, où une personne peut avoir un nombre arbitraire de tickets, mais un ticket ne peut appartenir qu'à une seule personne.

D'un autre côté, nous avons également une association 1-* où le côté 1 est dans Entry, modélisant le fait que les tickets peuvent avoir des pénalités associées, ce que nous verrons plus tard. Ainsi, avec tout cela, nous pouvons savoir qu'au niveau logique, Entry aura 2 clés étrangères pointant vers d'autres entités, ainsi qu'une clé étrangère provenant d'une autre entité pointant vers Entry.

Pour identifier de manière unique les tickets, l'attribut le plus important est **EntryTimestamp**. Celui-ci enregistre l'heure exacte à laquelle le ticket a été acheté. Mais plusieurs personnes peuvent acheter des tickets en même temps pour entrer dans la même piscine, ce qui entraîne plusieurs uplets avec la même valeur **EntryTimestamp**, la clé primaire doit donc avoir plus d'attributs pour identifier de manière unique tous les tickets.

Plus précisément, la clé primaire a besoin des attributs de clé étrangère **PersonFK** et **PoolFK** pour différencier les entrées par la personne qui les a achetées et la piscine où elle entre, ainsi que l'heure exacte de l'achat. Ainsi, si nous considérons les situations possibles et les combinaisons de valeurs qui peuvent se produire pour la clé primaire de Entry, nous verrons qu'une personne ne peut pas acheter plusieurs entrées au même moment exact pour entrer dans la même piscine.

Cela est logique lorsque le domaine stipule que chaque ticket est associé à une seule personne et qu'une personne ne peut pas acheter de ticket pour quelqu'un d'autre. En d'autres termes, si une personne achète un ticket, elle doit l'utiliser elle-même. Elle ne peut pas acheter plusieurs tickets pour que plusieurs personnes puissent entrer. Cela ne doit pas forcément être le cas dans tous les domaines – nous supposons simplement ici que les gens ne peuvent pas acheter de tickets pour les autres.

Dans d'autres domaines, cela pourrait devoir être modélisé différemment selon les exigences. Nous devrons donc nous assurer que notre modèle répond à ces types d'exigences imposées par le domaine, en particulier lors de la définition de **clés primaires** ou de contraintes **UNIQUE**.

Ainsi, en exigeant que les attributs **PersonFK** et **PoolFK** soient présents dans la clé primaire, l'entité Entry devient faible en identification avec deux entités propriétaires, Person et CityPool, respectivement. Dans le DDL, nous avons explicitement ajouté la contrainte NOT NULL à tous les attributs pour plus de clarté, bien que cela ne soit pas nécessaire pour ceux présents dans la clé primaire.

```pgsql
CREATE TABLE Entry (
    EntryTimestamp TIMESTAMP NOT NULL,
    Price DOUBLE PRECISION NOT NULL CHECK (Price >= 0),
    PaymentMethod PaymentMethodType NOT NULL,
    AppliedDiscount DOUBLE PRECISION NOT NULL CHECK (AppliedDiscount >= 0),
    Duration INT NOT NULL CHECK (Duration >= 0),
    PersonFK INT NOT NULL,
    PoolFK INT NOT NULL,
    PRIMARY KEY (EntryTimestamp, PersonFK, PoolFK),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID),
    FOREIGN KEY (PoolFK) REFERENCES CityPool(PoolID)
);
```

D'un autre côté, l'attribut **EntryTimestamp** de type TIMESTAMP est nommé différemment de l'attribut IssueTime de l'entité BusTicket, par exemple.

Ce n'est pas très important, mais dans un processus de conception réel, nous pourrions être tenus d'utiliser des guides de style qui déterminent comment nous devrions nommer chaque attribut en fonction de sa sémantique, de son type ou de ses contraintes, ainsi que quand et comment nous devrions déclarer certaines contraintes. Dans ce cas précis, nous n'avons suivi aucun guide de style – nous avons simplement nommé les attributs de la manière la plus descriptive possible selon les circonstances. Pourtant, le respect d'un guide de style offre des avantages en termes de maintenabilité du système et de facilité d'administration, entre autres.

#### Entité Team

Pour organiser des compétitions dans les piscines olympiques, notre système doit pouvoir modéliser des équipes sportives composées de personnes qui participent à ces compétitions. Nous avons donc l'entité Team, qui représente les équipes sportives qui ont une piscine olympique de référence, sont composées de personnes et participent à des compétitions dans des piscines olympiques.

Ceci est modélisé en utilisant les attributs de Team pour stocker les caractéristiques des équipes sportives, telles que le nom, la date de création, la couleur de l'uniforme, etc. Nous pouvons également utiliser des associations avec d'autres entités pour déterminer quelle piscine olympique est la piscine officielle de l'équipe, quelles personnes appartiennent à l'équipe, qui entraîne l'équipe et à quelles compétitions elles participent.

Tout d'abord, pour modéliser la piscine olympique considérée comme la piscine officielle de l'équipe, nous utiliserons une association 1-* avec OlympicPool, qui devient une clé étrangère en raison de sa cardinalité. Comme vous pouvez le voir dans le diagramme conceptuel, le rôle de l'association spécifie la sémantique, car sans lui, vous ne pouvez pas inférer directement ce qui est modélisé avec cette association.

Il en va de même pour l'association 1-* avec Person, que nous utilisons pour déterminer qui entraîne l'équipe, nous devons donc spécifier sa sémantique pour éviter toute confusion sur ce que cette association modélise réellement. Bien que, compte tenu de leurs cardinalités, il soit clair qu'une équipe ne peut avoir qu'une seule personne comme entraîneur, et non un nombre arbitraire de personnes, nous pouvons donc exclure que l'association modélise les personnes qui appartiennent à l'équipe.

D'un autre côté, outre les clés étrangères que possède Team, il en existe d'autres qui pointent vers Team et sont chargées de modéliser les personnes qui composent l'équipe, comme celle de Membership, ou la participation de l'équipe à des compétitions, comme celle que nous voyons de Participation.

```pgsql
CREATE TYPE SportType AS ENUM ('waterpolo', 'swimming', 'diving');
CREATE TABLE Team (
    Name VARCHAR(32),
    CreationDate DATE NOT NULL,
    ClothColor ColorType NOT NULL,
    Sport SportType NOT NULL,
    Budget INT NOT NULL CHECK (Budget >= 0),
    ContactEmail VARCHAR(32) NOT NULL,
    CoachFK INT NOT NULL,
    HomePoolFK INT NOT NULL,
    PRIMARY KEY (Name, CoachFK),
    FOREIGN KEY (CoachFK) REFERENCES Person(PersonID),
    FOREIGN KEY (HomePoolFK) REFERENCES OlympicPool(PoolID)
);
```

Pour identifier de manière unique chaque équipe, l'attribut qui peut le mieux nous servir à partir de la table elle-même est Name. Mais dans ce domaine, nous supposons que plusieurs équipes peuvent avoir le même nom, la clé primaire ne peut donc pas être formée uniquement par cet attribut.

Ainsi, parmi tous les autres attributs dont nous disposons, nous incluons finalement la clé étrangère CoachFK dans la clé primaire, ce qui signifie que nous utilisons également les informations de la personne qui entraîne l'équipe pour l'identifier de manière unique. Cela fonctionne car nous supposons qu'il ne peut y avoir plusieurs équipes portant le même nom entraînées par la même personne.

À première vue, cela pourrait sembler tout à fait possible, mais considérez que certaines exigences du domaine pourraient imposer cette condition, que nous pouvons exploiter pour définir **(Name, CoachFK)** comme clé primaire. Dans tous les cas, avant de prendre une telle décision, assurez-vous que l'ensemble d'attributs respecte la restriction de clé primaire, soit en raison des exigences du domaine, soit de la sémantique des attributs eux-mêmes.

Nous pouvons déclarer des clés étrangères avec FOREIGN KEY référençant la clé primaire de Person et OlympicPool. Nous leur imposons la restriction NOT NULL puisque toutes les équipes doivent avoir un entraîneur et une piscine olympique officielle. Ici, nous avons également supposé la nécessité de ces éléments, mais dans d'autres cas, il pourrait ne pas être obligatoire d'avoir une piscine officielle ou un entraîneur – tout dépend du domaine.

Si le fait d'avoir un entraîneur n'était pas obligatoire, nous ne pourrions pas inclure l'attribut de clé étrangère CoachFK dans la clé primaire, car il pourrait être NULL et violerait la restriction de clé primaire. Ainsi, pour qu'une entité soit faible en identification et qu'une autre soit son propriétaire, l'association entre elles doit être obligatoire, ce qui signifie que sa cardinalité minimale du côté du propriétaire ne peut pas être 0.

Enfin, nous définissons ici un TYPE ENUM pour le type de sport pratiqué par l'équipe, qui est stocké dans l'attribut Sport. Mais nous n'avons pas besoin de le redéfinir pour l'attribut **Color**, car nous avions défini précédemment l'**ENUM ColorType**, qui est le meilleur exemple de la façon dont un type de données est **réutilisé** à travers des attributs ayant le même domaine dans différentes entités.

#### Entité Membership

Poursuivons avec la sémantique de l'entité précédente. Pour modéliser la possibilité que des personnes fassent partie d'une équipe, l'approche la plus simple consisterait à inclure une association N-M entre Person et Team. Cela s'ajouterait à l'association 1-* qui existe déjà pour modéliser la personne qui entraîne l'équipe. De cette façon, une personne peut appartenir à un nombre arbitraire d'équipes, tandis qu'une équipe peut être composée d'un nombre arbitraire de personnes.

Mais comme cette association nécessite une entité intermédiaire pour être implémentée au niveau logique, et que nous devons également stocker des informations sur l'adhésion d'une personne à une équipe, nous introduirons l'entité Membership. Cette entité divise l'association N-M en plusieurs associations 1-*, reliant indirectement Person à Team. De cette façon, chaque personne appartenant à une équipe aura un uplet dans cette table représentant son adhésion. Il stockera des informations telles que la date de début ou de fin de l'adhésion ou la cotisation qu'elle doit verser à l'équipe pour en faire partie.

Au niveau conceptuel, nous pouvons voir que cette entité présente de nombreuses similitudes avec d'autres comme Residence. Par exemple, nous définissons la clé primaire de cette entité avec l'attribut JoinDate et les clés étrangères qui déterminent la Personne qui appartient à une certaine équipe. En effet, les attributs qui apparaissent exclusivement dans l'entité ne peuvent pas identifier de manière unique chaque adhésion. C'est-à-dire qu'il peut y avoir plusieurs personnes ayant commencé à appartenir à différentes équipes à la même date, entraînant plusieurs uplets dans Membership avec la même valeur dans leur clé primaire.

Ainsi, même si les attributs de clé étrangère n'apparaissent pas explicitement au niveau conceptuel, il est clair qu'un uplet Membership doit être identifié non seulement par la date de début mais aussi par la personne et l'équipe auxquelles il se rapporte. Cela évitera les situations où plusieurs uplets avec la même personne et la même date sont considérés comme égaux, ou avec la même équipe et la même date de début. Nous savons donc qu'il s'agit d'une entité faible en identification qui dépend de Person et Team.

Puisqu'elle dépend des deux entités auxquelles elle est liée pour l'identification, nous aurions pu la représenter comme une entité associative connectée à l'association N-M possible entre Person et Team. Mais pour rendre le diagramme aussi clair et proche du niveau logique que possible, nous devrions plutôt utiliser une entité "intermédiaire" comme celle représentée ici avec des associations 1-*.

```pgsql
CREATE TYPE PaymentFrequencyType AS ENUM('monthly', 'anual', 'weekly', 'quarterly');
CREATE TABLE Membership (
    JoinDate DATE NOT NULL,
    LeaveDate DATE CHECK (
        LeaveDate IS NULL
        OR LeaveDate >= JoinDate
    ),
    FeeAmount INT NOT NULL CHECK (FeeAmount >= 0),
    PaymentFrequency PaymentFrequencyType NOT NULL,
    AutoRenewal BOOLEAN NOT NULL,
    PersonFK INT NOT NULL,
    TeamNameFK VARCHAR(32) NOT NULL,
    CoachFK INT NOT NULL,
    PRIMARY KEY (JoinDate, PersonFK, TeamNameFK, CoachFK),
    FOREIGN KEY (PersonFK) REFERENCES Person(PersonID),
    FOREIGN KEY (TeamNameFK, CoachFK) REFERENCES Team(Name, CoachFK)
);
```

Pour implémenter les clés étrangères, nous créerons les attributs correspondants : PersonFK, qui est la clé étrangère pointant vers Person, et (TeamNameFK, CoachFK), où les deux constituent l'autre clé étrangère référençant l'équipe à laquelle appartient la personne. Les deux clés sont **not null** car un uplet Membership doit associer une personne à une équipe.

Une fois que nous avons déclaré les attributs et les contraintes FOREIGN KEY, nous pouvons définir la clé primaire comme l'ensemble d'attributs composé de **JoinDate**, de l'attribut de clé étrangère **PersonFK**, et des deux autres attributs **(TeamNameFK, CoachFK)** de la clé étrangère référençant l'équipe. Nous pouvons les déclarer dans n'importe quel ordre dans la contrainte PRIMARY KEY, tant qu'ils apparaissent tous.

Enfin, selon le domaine, nous supposons que les gens ne savent pas exactement quand ils cesseront d'être membres d'une équipe, donc LeaveDate ne doit pas toujours être défini. Cela signifie qu'il peut être NULL jusqu'à ce que la personne quitte l'équipe ou prévoie de la quitter à une date précise. Nous devons donc définir une contrainte CHECK sur cet attribut pour nous assurer qu'il est soit NULL, soit que la date est postérieure à JoinDate, car une personne ne peut pas quitter une équipe avant la date de début de l'adhésion.

#### Entité Participation

De même, une équipe sportive peut également participer à des compétitions sportives enregistrées dans SwimmingCompetition. Nous avons donc une entité appelée Participation qui relie indirectement Team à SwimmingCompetition via des associations 1-*. C'est exactement ce que nous avons vu précédemment avec Membership, mais avec une signification différente. Plus précisément, ce qui change principalement, ce sont les informations stockées sur la participation de l'équipe à une compétition, telles que la date à laquelle elle s'inscrit pour participer, son rang au classement après la compétition ou le temps qu'il a fallu pour terminer la compétition.

Pour identifier de manière unique les uplets de Participation, le moyen le plus simple consiste à utiliser un identifiant de base de données personnalisé comme clé substitutive, tout comme nous l'avons fait auparavant avec certaines entités. Mais si les exigences du domaine ne nous permettent pas d'inclure des clés substitutives ou tout autre identifiant spécifique à la base de données, nous devrons choisir un ensemble d'attributs permettant l'identification.

Ainsi, si nous supposons qu'aucune équipe ne participe plus d'une fois à la même compétition (car cela n'aurait pas de sens), nous pouvons déclarer une clé primaire formée par les clés étrangères référençant **Team** et **SwimmingCompetition**. De cette façon, nous nous assurons que différents uplets de Participation n'associent pas la même équipe à la même compétition plusieurs fois, car cette situation ne peut pas se produire.

Comme vous pouvez le voir, l'identification de cette entité dépend entièrement d'autres entités comme Team et SwimmingCompetition, ce qui signifie qu'il n'y a aucun attribut au niveau conceptuel de l'entité qui fait partie de la clé primaire.

Ce n'est pas nécessairement une mauvaise chose, mais plutôt une conséquence des exigences du domaine nous empêchant d'utiliser une clé substitutive. En fait, cette dépendance dans l'identification peut présenter certains avantages, comme l'évitement de colonnes supplémentaires, ce qui pourrait être une exigence imposée par le domaine (utiliser le moins de colonnes possible).

```pgsql
CREATE TABLE Participation (
    RegistrationDate DATE NOT NULL,
    Rank INT NOT NULL CHECK (Rank > 0),
    RecordedTime DOUBLE PRECISION NOT NULL CHECK (RecordedTime >= 0),
    NameFK VARCHAR(32),
    StartDateFK DATE,
    EndDateFK DATE,
    TeamNameFK VARCHAR(32),
    CoachFK INT,
    PRIMARY KEY (
        NameFK,
        StartDateFK,
        EndDateFK,
        TeamNameFK,
        CoachFK
    ),
    FOREIGN KEY (TeamNameFK, CoachFK) REFERENCES Team(Name, CoachFK),
    FOREIGN KEY (NameFK, StartDateFK, EndDateFK) REFERENCES SwimmingCompetition(Name, StartDate, EndDate)
);
```

Au niveau logique, la clé étrangère référençant Team possède deux attributs, qui constituent la clé primaire de Team. La clé étrangère pointant vers SwimmingCompetition en possède trois pour la même raison. Nous utiliserons donc deux contraintes FOREIGN KEY : une pour déclarer la clé étrangère pointant vers Team et l'autre pour celle pointant vers SwimmingCompetition, respectivement.

Notez que la contrainte FOREIGN KEY n'autorise qu'une seule clause REFERENCES. Ainsi, si nous avons plusieurs clés étrangères pointant vers diverses entités, nous devons utiliser une contrainte FOREIGN KEY distincte pour chaque clé étrangère. Si nous essayons de les déclarer toutes avec une seule contrainte, nous devrions indiquer les multiples entités/tables référencées, ce qui signifie que nous devrions utiliser plusieurs instructions REFERENCES.

Après avoir déclaré les clés étrangères et ajouté leur contrainte NOT NULL respective, puisqu'il est obligatoire pour une participation de relier une équipe à une compétition, nous déclarons la clé primaire comme l'ensemble des attributs qui forment les deux clés étrangères ensemble. Ainsi, dans notre système, il peut y avoir des uplets Participation avec des valeurs Rank ou RegistrationDate différentes sans aucun problème – mais il ne peut y avoir plusieurs uplets avec la même valeur dans leur clé primaire (ce qui signifie qu'ils ne peuvent pas relier la même équipe à la même compétition plusieurs fois).

Enfin, si nous essayons de reconstruire l'entité conceptuelle à partir du diagramme relationnel, la première chose que nous devrions remarquer est que toutes les clés étrangères sont soulignées, et forment donc la clé primaire. Comme ce sont des clés étrangères, ces attributs n'apparaîtront pas dans l'entité conceptuelle de Participation.

Pour déterminer combien de clés étrangères nous avons réellement, et savoir combien d'associations 1-* introduire et avec quelles entités les connecter, nous pouvons voir qu'un sous-ensemble d'attributs comme **(TeamNameFK, CoachFK)** se réfère à la même entité – il y aura donc une relation 1-* avec cette entité, avec le côté "plusieurs" dans Participation. En faisant de même avec les attributs **(NameFK, StartDateFK, EndDateFK)**, nous voyons qu'ils se réfèrent tous à des attributs de la même entité. Ils forment donc une clé étrangère qui donne lieu à une association 1-* comme la précédente, mais se connectant à une autre entité.

Pour inférer les cardinalités minimales, nous devrions regarder les contraintes indiquées dans le diagramme relationnel : quelles clés étrangères peuvent ou ne peuvent pas être NULL, ou combien de participations chaque compétition doit avoir (ainsi que les participations que chaque équipe doit avoir).

Dans ce cas, nous n'avons indiqué aucune contrainte dans le diagramme relationnel par souci de simplicité. Mais, par exemple, si on nous disait qu'une clé étrangère ne peut pas être NULL dans le modèle relationnel, cela se traduit conceptuellement par le fait que son association 1-* respective possède une cardinalité minimale de 1 du côté 1. De même, s'il existe des contraintes spéciales exigeant que chaque équipe ait 2 participations, par exemple, alors nous savons que dans son association correspondante, la cardinalité minimale du côté Participation serait de 2.

Ce processus inverse est ce que nous avons initialement suivi pour implémenter l'entité au niveau logique, où les attributs qui composent chaque clé étrangère sont inférés, et ceux sélectionnés pour déclarer la clé primaire.

#### Entité SwimmingCompetition

Pour modéliser les compétitions sportives qui peuvent avoir lieu dans une piscine olympique, nous avons dans le diagramme conceptuel l'entité appelée **SwimmingCompetition** qui est chargée de stocker les informations sur les compétitions organisées dans toutes les piscines olympiques enregistrées dans le système. Dans celles-ci, n'importe quel nombre d'équipes sportives peut participer.

Les informations que stocke SwimmingCompetition dépendent principalement du domaine et des exigences. Dans ce cas, nous supposons que nous n'avons besoin de stocker que le nom de la compétition, les dates de début et de fin qui seront toujours déterminées, un attribut RecordTime pour stocker tout temps record atteint au cours de cette compétition, et le montant monétaire du prix pour cette compétition.

Avec ces attributs, le moyen le plus simple d'identifier de manière unique chaque uplet dans la table SwimmingCompetition est de définir l'ensemble d'attributs **(Name, StartDate, EndDate)** comme clé primaire.

Par exemple, il peut y avoir des compétitions dans la base de données avec exactement le même nom, mais elles ne peuvent jamais avoir les mêmes dates de début et de fin simultanément (car cela signifierait qu'il s'agit de la même compétition). En fin de compte, en déclarant cette clé primaire, nous supposons qu'il n'existe pas de compétitions différentes ayant le même nom et les mêmes dates de début et de fin – donc si cette condition correspond aux exigences du domaine, elle serait correcte.

Par conséquent, il peut y avoir différentes compétitions dans la base de données avec différentes combinaisons de valeurs pour les attributs de la clé primaire – mais elles pourraient avoir le **même temps record**, ou le même prix dans **PrizeAmount**, puisqu'il n'y a aucune restriction l'empêchant.

```pgsql
CREATE TABLE SwimmingCompetition (
    Name VARCHAR(32),
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL CHECK (EndDate >= StartDate),
    RecordTime DOUBLE PRECISION CHECK (RecordTime >= 0),
    PrizeAmount INT NOT NULL CHECK (PrizeAmount >= 0),
    PRIMARY KEY (Name, StartDate, EndDate)
);
```

Dans le diagramme conceptuel, nous voyons que l'entité possède plusieurs associations qui mènent à l'existence d'une clé étrangère pointant vers OlympicPool, puisque la compétition doit nécessairement avoir lieu dans une piscine olympique. Ainsi, cette clé étrangère référence la piscine spécifique où se déroule la compétition, rendant son existence obligatoire. En d'autres termes, la clé étrangère ne peut pas être NULL car, dans le modèle conceptuel, nous avons fixé la cardinalité minimale à 1 pour garantir que chaque compétition est associée à une piscine où elle a lieu.

Une autre particularité de cette entité est que l'attribut **RecordTime** peut ne pas toujours être défini. Par exemple, lorsque nous enregistrons une compétition dans la base de données et que nous devons fournir une valeur pour cet attribut, une telle valeur peut ne pas exister car c'est la première fois que la compétition a lieu. Ainsi, la manière la plus simple de la modéliser serait de fixer cet attribut au maximum ou au minimum possible, selon la façon dont nous considérons quels temps sont meilleurs que d'autres.

De plus, comme dans notre domaine nous modélisons également la possibilité que les athlètes participant à une compétition soient sanctionnés, il est possible que dans une certaine compétition organisée pour la première fois, tous les participants soient sanctionnés. Cela signifie qu'aucun d'entre eux ne contribuerait à initialiser la valeur de l'attribut **RecordTime**. C'est pourquoi il doit pouvoir être **NULL**.

Mais c'est une décision que nous devons prendre en considérant principalement le domaine et ses exigences, car nous pourrions vouloir initialiser l'attribut avec une valeur par défaut ou spéciale si tous les athlètes sont pénalisés et que le compteur ne peut pas être initialisé, par exemple.

#### Entité Sanction

Compte tenu de tout ce qu'une personne peut faire dans notre domaine en relation avec d'autres entités, elle pourrait enfreindre une règle entraînant une sanction. Ainsi, dans notre schéma, nous pouvons introduire une hiérarchie IS-A où la super-classe est l'entité Sanction, et ses entités héritées sont les différents types de sanctions que nous définissons, tout dépend de leur champ d'application.

Plus précisément, la décision d'utiliser une hiérarchie pour modéliser les sanctions est motivée par les informations spécifiques qui doivent être stockées pour chaque type de sanction. Pour cette raison, si nous essayions d'utiliser une seule entité Sanction pour représenter tous ces types, sa sémantique serait très compliquée (car certains attributs ne seraient utiles que si la sanction était d'un certain type – et il en va de même pour beaucoup d'autres). Nous devrions également utiliser un attribut spécifique pour représenter le type de sanction, car sinon, connaître le type exact pourrait dépendre des attributs qui sont NULL, ce qui compliquerait les requêtes.

Ainsi, avec cette hiérarchie, nous pouvons avoir un ensemble d'attributs communs à toutes les sanctions dans Sanction, tels que le montant monétaire de l'amende, la description, la date de la sanction ou le statut, tandis que dans les entités héritées, nous avons des attributs spécifiques qui caractérisent chaque type de sanction.

#### Comment la hiérarchie IS-A est-elle implémentée avec des tables ?

Tout comme nous l'avons fait avec d'autres hiérarchies, nous devons l'analyser pour savoir comment l'implémenter au niveau logique. Nous devons garder à l'esprit que la conception conceptuelle ne détermine pas de manière univoque l'implémentation que nous réaliserons finalement, en particulier lors du travail avec une hiérarchie IS-A. C'est plutôt une décision que nous devrions prendre en nous basant non seulement sur la conception conceptuelle elle-même, mais aussi sur le domaine et les exigences en matière de données.

Pour ce faire, nous vérifions d'abord si la hiérarchie est complète ou non. Dans ce cas, toutes les sanctions existantes seront d'un type spécifique représenté par les entités héritées. Cela signifie que tous les individus de la hiérarchie appartiendront à l'un des ensembles générés par ces entités, ce qui implique que la hiérarchie est **complète**.

D'un autre côté, les types de sanctions sont tous disjoints, ce qui signifie qu'une sanction ne peut être que d'un seul type, pas de plusieurs à la fois. Cela signifie que la hiérarchie est disjointe car aucun individu ne sera représenté par plusieurs entités héritées en même temps.

Pour identifier chaque sanction, nous utiliserons un attribut SanctionID dans la super-classe Sanction, que nous implémenterons à l'aide d'une clé substitutive. Cela évite que les entités héritées n'aient besoin d'utiliser leurs propres identifiants, car nous supposons que les exigences du domaine ne nous obligent pas à identifier chaque type de sanction différemment.

Ainsi, compte tenu du nombre d'attributs que possède chaque entité héritée, il est clair que nous aurons besoin d'une table pour implémenter chaque entité héritée. Sinon, trop de valeurs NULL seraient générées dans les attributs correspondants, ce qui compliquerait à la fois la gestion de la base de données et les requêtes, et pourrait conduire à des contraintes inutiles visant à assurer l'intégrité du schéma.

D'un autre côté, nous avons plusieurs options pour implémenter la super-classe au niveau logique. Une option consiste à dupliquer tous les attributs dans chacune des tables des types de sanctions spécifiques.

Cela présente des avantages, comme l'identification de chaque table à l'aide de l'attribut SanctionID hérité de la super-classe, mais cela entraîne des problèmes de gestion de schéma. Si nous voulons plus tard supprimer, modifier ou ajouter un attribut de Sanction, nous devrons effectuer cette opération sur toutes les tables des différents types de sanctions, ce qui augmente la probabilité d'erreurs dans le processus. De plus, si nous voulons interroger toutes les sanctions de notre base de données, avec cette option, nous devrions parcourir tous les uplets de toutes les tables de chaque type de sanction, ce qui pourrait être inefficace en raison de l'accès à plusieurs tables.

Pour minimiser les erreurs dans le processus de gestion de la base de données, nous devons simplifier les opérations impliquées autant que possible. Pour ce faire, nous pouvons implémenter une table spécifique pour la super-classe de la hiérarchie de la même manière que nous l'avons fait avec la hiérarchie Vehicle (et pour des raisons similaires).

Chacune des tables pour les entités héritées possédera une clé étrangère référençant la table super-classe, où nous stockerons les informations des attributs communs à toutes les sanctions. Cela facilite la modification de ces attributs. Cela simplifie également d'autres opérations, comme l'ajout d'un nouveau type de sanction. Pour cela, seule une nouvelle table pour ce type doit être créée, et nous devons simplement nous assurer que sa clé étrangère référence **Sanction**.

Si nous regardons les entités héritées, nous verrons que chacune possède une association 1-* avec d'autres entités où le côté "plusieurs" se trouve toujours dans les entités de la hiérarchie. Cela signifie que l'utilisation d'une seule table pour implémenter l'intégralité de la hiérarchie n'est pas une bonne idée, car elle combinerait toutes ces clés étrangères dans une seule table. Cela conduirait à des contraintes d'intégrité beaucoup plus compliquées.

En d'autres termes, si une sanction est d'un type spécifique, les attributs et les clés étrangères des types restants doivent être NULL, donc assurer cela pour tous les types implique des contraintes trop élaborées et complexes.

```pgsql
CREATE TYPE SanctionStatusType AS ENUM ('created', 'active', 'expired');
CREATE TABLE Sanction (
    SanctionID SERIAL PRIMARY KEY,
    Amount DOUBLE PRECISION NOT NULL CHECK (Amount >= 0),
    Description VARCHAR(32),
    IssueDate DATE NOT NULL,
    ExpirationDate DATE CHECK (
        ExpirationDate IS NULL
        OR ExpirationDate >= IssueDate
    ),
    Status SanctionStatusType NOT NULL
);
```

Dans le DDL de la table Sanction, nous pouvons voir que sa clé primaire **{SanctionID}** se compose d'un seul attribut de type SERIAL. Il s'agit d'une clé substitutive qui sera utilisée pour identifier toutes les sanctions de la base de données, quel que soit leur type.

Cette table stocke également le statut de la sanction dans un attribut, puisque le type de sanction est représenté avec des entités héritées de la super-classe au niveau conceptuel. Le statut doit donc être modélisé comme un attribut pour éviter de mélanger la sémantique de ce que nous représentons avec chaque outil du diagramme entité-relation.

En d'autres termes, nous pourrions inclure de nouvelles entités héritées qui modélisent les états des sanctions, mais nous devons considérer que chaque type de sanction pourrait être dans n'importe lequel de ces états – ce qui conduirait à une hiérarchie multi-niveaux inutilement compliquée.

Pour cette raison, nous devrions séparer la sémantique de ce que nous représentons avec les entités héritées de la sémantique du statut de la sanction, en le modélisant avec un attribut dans la super-classe, car n'importe quel type de sanction peut être dans n'importe quel état.

Dans cet attribut Status, nous définissons un TYPE ENUM pour restreindre les états possibles qu'une sanction peut avoir. Mais pour la Description, si nous voulons enregistrer une description de la sanction écrite en langage naturel, nous ne devrions pas ajouter de restrictions à moins que cela ne soit requis par les spécifications du projet.

Une description en langage naturel peut être très diverse, l'approche la plus simple consiste donc à ne pas limiter les valeurs possibles que l'attribut peut prendre, pas même avec une contrainte NOT NULL. Cela peut indiquer qu'une sanction n'a pas de description, bien que ce ne soit pas nécessairement correct.

En général, les décisions d'autoriser NULL ou non dépendent également du domaine et des exigences. Par exemple, les sanctions peuvent avoir ou non une date d'expiration, c'est pourquoi la contrainte CHECK définie sur ExpirationDate spécifie que cet attribut peut soit être NULL, soit contenir une date postérieure à la date d'émission de la sanction.

#### Entité DrivingSanction

Parlons maintenant des différents types de sanctions dans notre système. Tout d'abord, nous avons DrivingSanction, qui sont des sanctions associées aux permis de conduire. Ainsi, dans le diagramme conceptuel, elle possède une association 1-* avec l'entité DrivingLicense, ce qui donne une clé étrangère dans DrivingSanction qui référence le permis de conduire faisant l'objet de la sanction. Cela se réfère au permis de la personne qui a commis une infraction au code de la route, entraînant l'existence de l'amende.

Les attributs spécifiques de ce type de sanction stockent des informations sur la raison pour laquelle l'amende a été émise, comme la vitesse à laquelle le véhicule roulait, ainsi que l'effet de la sanction sur le permis (comme la déduction d'un certain nombre de points ou sa suspension pendant une certaine période).

Dans son DDL, nous pouvons voir que tous les attributs ont été déclarés comme NOT NULL, ce qui au premier abord pourrait sembler inutile dans le cas de RecordedSpeed, puisque toutes les sanctions ne sont pas causées par la vitesse. Mais cela illustre que même si un attribut n'est pas nécessaire, il ne devrait pas être NULL pour être considéré comme inutile.

Par exemple, si une sanction n'est pas liée à la vitesse, au lieu d'utiliser une valeur NULL dans l'attribut RecordedSpeed, nous pouvons utiliser une valeur spéciale comme 0, tant qu'elle respecte les contraintes d'intégrité et les exigences du domaine système. Cela nous permet de distinguer si la sanction est liée à un éventuel excès de vitesse. Nous prenons donc la décision d'autoriser NULL ou non initialement lors de la modélisation de l'entité au niveau logique. Cela fonctionne tant que nous ne sommes pas obligés d'utiliser une sémantique spécifique comme le réglage de l'attribut à 0 lorsqu'il n'est pas nécessaire.

Si nous examinons si d'autres attributs peuvent être NULL ou non, nous pouvons voir que PermanentSuspension a toujours la possibilité de prendre la valeur **false** (car la suspension peut ne pas être permanente). De même, si la suspension est permanente, l'attribut SuspensionDays peut toujours être fixé à 0, ou à une valeur spéciale différente. Nous pourrions également simplement ignorer sa valeur et vérifier d'abord si la suspension est permanente avant d'accéder à l'attribut SuspensionDays, entre autres options.

```pgsql
CREATE TABLE DrivingSanction (
    SanctionID SERIAL PRIMARY KEY,
    RecordedSpeed DOUBLE PRECISION NOT NULL CHECK (RecordedSpeed >= 0),
    PointsDeducted INT NOT NULL CHECK (PointsDeducted >= 0),
    SuspensionDays INT NOT NULL CHECK (SuspensionDays >= 0),
    PermanentSuspension BOOLEAN NOT NULL,
    LicenseFK INT NOT NULL,
    FOREIGN KEY (SanctionID) REFERENCES Sanction(SanctionID),
    FOREIGN KEY (LicenseFK) REFERENCES DrivingLicense(LicenseID)
);
```

D'un autre côté, le NOT NULL est effectivement nécessaire pour les deux clés étrangères de la table, car SanctionID est la clé étrangère qui référence l'uplet dans Sanction qui détient le reste des informations sur la sanction. Son attribut de clé primaire SanctionID sert de clé primaire de la table DrivingSanction elle-même, et c'est le seul moyen d'identifier de manière unique les sanctions. De plus, la clé étrangère qui référence le permis de conduire ayant reçu la sanction ne peut pas non plus être NULL, car si la sanction est de type DrivingSanction, elle doit nécessairement être associée à un permis.

#### Entité SportSanction

Un autre type de sanction est représenté dans l'entité SportSanction. Celle-ci modélise les sanctions qui surviennent lors de compétitions sportives, plus précisément celles causées par une équipe sportive lors de sa participation à une compétition. Comme l'entité précédente, elle possède des attributs qui caractérisent ce type de sanction, tels que le nombre de compétitions pendant lesquelles l'équipe est suspendue ou le nom de l'arbitre qui a émis la sanction.

En plus de ces informations, chaque sanction de ce type doit savoir quelle équipe spécifique a reçu la sanction, ainsi que la compétition à laquelle elle participait lorsqu'elle a été sanctionnée. Ainsi, pour modéliser cela, nous avons plusieurs options. Nous pourrions utiliser deux associations 1-* pour relier SportSanction à Team et à SwimmingCompetition, de sorte qu'à partir de la sanction, vous puissiez identifier l'équipe et la compétition correspondantes. Mais c'est redondant et inutile, car cela conduirait à deux clés étrangères qui peuvent en fait être réduites à une seule.

Rappelez-vous que dans notre schéma, nous avons une entité appelée Participation qui relie les équipes aux compétitions auxquelles elles participent. Ainsi, au lieu de deux associations 1-* dans SportSanction, nous pouvons en utiliser une seule qui la relie à Participation, puisque à partir de Participation, nous pouvons déterminer l'équipe et la compétition.

```pgsql
CREATE TABLE SportSanction (
    SanctionID SERIAL PRIMARY KEY,
    SuspendedCompetitions INT NOT NULL CHECK (SuspendedCompetitions >= 0),
    RefereeName VARCHAR(32) NOT NULL,
    NameFK VARCHAR(32) NOT NULL,
    StartDateFK DATE NOT NULL,
    EndDateFK DATE NOT NULL,
    TeamNameFK VARCHAR(32) NOT NULL,
    CoachFK INT,
    FOREIGN KEY (SanctionID) REFERENCES Sanction(SanctionID),
    FOREIGN KEY (
        NameFK,
        StartDateFK,
        EndDateFK,
        TeamNameFK,
        CoachFK
    ) REFERENCES Participation(
        NameFK,
        StartDateFK,
        EndDateFK,
        TeamNameFK,
        CoachFK
    )
);
```

Pour implémenter cela en SQL, nous pouvons créer une table très similaire à DrivingSanction, où sa clé primaire est l'attribut SanctionID, également déclaré comme une clé étrangère référençant la table Sanction de la super-classe. Nous pouvons déclarer les attributs de la même manière que nous l'avons fait jusqu'à présent, tant pour les attributs de l'entité elle-même que pour les clés étrangères. Les clés étrangères doivent avoir les mêmes types de données que les attributs qu'elles référencent.

Dans ce cas, pour déclarer la clé étrangère qui pointe vers Participation, nous avons besoin d'autant d'attributs que sa clé primaire respective en possède, soit un total de 5. Pour simplifier ce processus, l'approche idéale consiste à regarder directement la contrainte PRIMARY KEY de la table que nous voulons référencer. Ensuite, pour chacun de ces attributs, nous pouvons le déclarer dans notre table avec un nom caractéristique et le type de données correspondant. Nous l'ajoutons enfin à la contrainte FOREIGN KEY afin qu'il référence l'attribut qui lui a donné naissance, comme nous l'avons déjà vu.

Par exemple, si la clé primaire de Participation est **(NameFK, StartDateFK, EndDateFK, TeamNameFK, CoachFK)**, alors nous déclarons un attribut **NameFK** pour la clé étrangère de **SportSanction** qui pointe vers l'attribut **NameFK** de cette clé primaire, un autre **StartDateFK** qui pointe vers l'attribut **StartDateFK** de la clé primaire de **Participation**, et ainsi de suite.

#### Entité PoolSanction

Pour conclure la hiérarchie des sanctions, nous avons PoolSanction. Celles-ci, comme vous pouvez le deviner, sont des sanctions imposées aux personnes qui sont entrées dans un CityPool et ont enfreint les règles de la piscine. Dans ce cas, nous stockons les dates de début et de fin comme attributs, indiquant la période pendant laquelle la personne ne peut pas entrer dans la piscine. Nous pouvons également inclure un montant à titre de compensation si nécessaire, ou un nombre d'heures de service communautaire que la personne doit effectuer.

Pour déterminer à partir de la sanction quelle personne et quelle piscine sont affectées par la sanction, nous pouvons utiliser une association 1-* avec Entry. Cela donne une clé étrangère dans PoolSanction qui pointe vers Entry car le côté "plusieurs" est placé dans PoolSanction. De cette façon, nous pouvons identifier l'entrée que la personne utilisait lorsqu'elle a reçu la sanction.

Outre la personne, l'entrée fournit également des informations sur la piscine dans laquelle elle ne pourra plus entrer librement. La sanction détermine quand elle pourra y entrer à nouveau ou l'action qu'elle doit entreprendre en raison de sa sanction.

```pgsql
CREATE TABLE PoolSanction (
    SanctionID SERIAL PRIMARY KEY,
    BanStartDate DATE,
    BanEndDate DATE,
    CompensationRequired INT NOT NULL CHECK (CompensationRequired >= 0),
    CommunityServiceHours INT NOT NULL CHECK (CommunityServiceHours >= 0),
    EntryFK TIMESTAMP NOT NULL,
    PersonFK INT NOT NULL,
    PoolFK INT NOT NULL,
    FOREIGN KEY (SanctionID) REFERENCES Sanction(SanctionID),
    FOREIGN KEY (EntryFK, PersonFK, PoolFK) REFERENCES Entry(EntryTimestamp, PersonFK, PoolFK),
    CHECK (
        (
            BanEndDate IS NULL
            AND BanStartDate IS NULL
        )
        OR BanEndDate >= BanStartDate
    )
);
```

Dans son DDL, nous pouvons voir que l'identification de la table est la même que les précédentes, avec une clé primaire composée de la clé étrangère pointant vers Sanction, ainsi qu'une autre clé étrangère pointant vers Entry (qui se compose de trois attributs). Dans ce cas, la sanction peut imposer plusieurs conditions à l'utilisateur sanctionné : elle peut soit lui interdire d'entrer pendant une période donnée, soit exiger qu'il paie une compensation, soit effectuer un certain nombre d'heures de service communautaire.

Ainsi, si nous supposons que le domaine et les exigences ne nous obligent pas à stocker des valeurs NULL dans n'importe quel attribut et que nous pouvons prendre n'importe quelle décision sur la façon dont les données sont stockées dans le système, nous déciderons d'autoriser BanStartDate et BanEndDate à être NULL pour les sanctions qui n'interdisent pas à l'utilisateur sanctionné d'entrer dans la piscine. Ainsi, dans la contrainte CHECK définie à la fin, nous voyons que comme condition d'intégrité pour tous les uplets de la table, les deux attributs doivent être soit nuls, soit la date de fin doit être postérieure à la date de début de l'interdiction. Cela garantit que seules des données valides sont stockées dans la table.

Enfin, nous pouvons voir que certains attributs de la clé étrangère pointant vers Entry sont nommés exactement de la même manière que les attributs qu'ils référencent, comme personFK ou PoolFK. Ce n'est ni un problème ni une erreur, bien que dans un projet plus vaste où chaque table possède plus d'attributs, nous devrions suivre un guide de style approprié lors du nommage des attributs, en particulier ceux réservés aux clés étrangères. De cette façon, nous pouvons comprendre plus clairement leur but sans avoir à passer du temps à analyser le schéma en détail.

### Comment créer la base de données

Maintenant que vous comprenez la sémantique du domaine et que vous avez terminé les **phases de conception conceptuelle et logique**, nous pouvons implémenter le modèle logique sur le SGBD.

Le moyen le plus simple de le faire est de créer un script avec une extension **.sql** qui contient tout le code DDL nécessaire pour remplir la base de données – c'est-à-dire les instructions que nous venons de passer en revue où nous créons des tables, des types de données et des contraintes.

Mais comme nous ne travaillons pas avec une base de données de projet réel ici, nous n'avons pas à nous soucier des données qui pourraient se trouver dans des tables existant déjà dans la base de données, en particulier celles ayant le même nom que l'une des tables que nous allons créer. Ainsi, par souci de simplicité, avant de les créer, nous exécuterons des instructions DROP pour supprimer les tables dont les noms correspondent à l'une des tables que nous allons créer. Cela garantira qu'elles ne contiennent aucun uplet.

En suivant ce processus, nous arriverons à un script DDL [comme celui-ci](https://gist.github.com/cardstdani/1247573e1ef2f6ea9ab99b82c5761ad6) (il est assez long, je l'ai donc laissé dans le gist).

Lorsque nous exécutons le script, gardez à l'esprit que les instructions s'exécuteront une par une de haut en bas. Nous utilisons donc d'abord les instructions DROP pour supprimer toutes les tables de la base de données qui ont le même nom que l'une de celles que nous allons créer.

Ce processus équivaut à **supprimer** l'intégralité de notre base de données – c'est-à-dire notre modèle logique qui a été créé une fois – nous devons donc d'abord supprimer les tables qui ne sont pas **référencées** par des **clés étrangères** pour maintenir l'intégrité tout en supprimant les tables restantes.

Ensuite, sous la même condition, toutes les tables correspondantes qui ne sont référencées par aucune clé étrangère sont successivement supprimées jusqu'à ce qu'il ne reste plus aucune table à supprimer.

Il ne devrait plus y avoir de tables dans notre base de données dont les noms entrent en conflit avec les tables de notre modèle logique, nous écrivons donc les instructions CREATE TABLE que nous avons vues précédemment pour chaque table du modèle logique.

Nous devons également le faire dans un ordre spécifique, précisément l'inverse du processus de suppression. Ici, nous devons d'abord créer les tables qui n'ont aucune clé étrangère pointant vers une autre entité. Si nous créons une table au début qui doit référencer une autre table qui n'a pas encore été créée, le SGBD générera une erreur d'intégrité. Ainsi, comme vous pouvez le voir dans le script, nous plaçons les instructions dans un ordre tel que chaque fois qu'une table avec des clés étrangères pointant vers d'autres tables est créée, ces tables ont déjà été créées au préalable.

Pour savoir comment nous devons ordonner les instructions DROP et CREATE TABLE, il existe des [algorithmes](https://medium.com/%40tharinduimalka915/how-kahns-algorithm-helped-me-solve-database-schema-dependencies-2b7e54142fd5) comme le [tri topologique](https://fr.wikipedia.org/wiki/Tri_topologique) que nous pouvons appliquer au diagramme relationnel. De cette façon, nous traitons le schéma de la base de données comme un **graphe orienté** composé de **nœuds (tables)** et d'**arêtes orientées (clés étrangères)**. Avec cet algorithme, par exemple, nous pouvons supprimer progressivement les nœuds minimaux ou maximaux du graphe, créant ou supprimant la table qu'ils représentent. Mais ce n'est pas la seule [méthode](https://softwareengineering.stackexchange.com/questions/359107/resolving-foreign-keys-breaking-cycles-to-enable-a-topological-sort) disponible.

En ce qui concerne les types de données et les contraintes définis dans les **assertions** ou les **déclencheurs (triggers)**, l'ordre de création est plus facile à inférer. En effet, les types ENUM ou DOMAIN doivent toujours être créés avant d'être utilisés dans la déclaration d'un attribut de table. L'approche la plus simple consiste donc à les créer au tout début, ou juste avant de les utiliser pour la première fois (ce que nous avons fait ici).

D'un autre côté, il est préférable de définir les assertions ou les déclencheurs à la fin. Nous voulons également leur donner des noms suffisamment descriptifs des contraintes qu'ils modélisent, car leurs définitions peuvent impliquer plusieurs tables que nous devons créer avant de définir la contrainte. De plus, comme ces éléments ne contiennent pas de **données (uplets)**, nous n'avons pas besoin de les supprimer au début du script à moins que nous n'allions modifier le schéma lui-même. Dans ce cas, certaines contraintes pourraient devenir obsolètes, c'est-à-dire qu'elles accèderaient à des attributs ou des tables qui n'existent plus.

En résumé, avec ce **script SQL**, nous créons les tables, les types de données et les contraintes qui composent notre schéma de base de données, en veillant à ce qu'aucune d'entre elles ne contienne d'uplets immédiatement après avoir été créée.

Mais pour exécuter le script, nous devons créer une base de données dans le SGBD. Utilisons l'instruction CREATE DATABASE pour créer une nouvelle base de données avec un nom spécifique :

```pgsql
 CREATE DATABASE ExampleDataBase OWNER postgres;
```

Si nous exécutons cette commande sur le terminal du SGBD, nous créerons une base de données complètement vide nommée **"exampledatabase"**. Notez que PostgreSQL n'est pas sensible à la casse pour les noms d'éléments ou les instructions SQL. Ainsi, même si nous écrivons le nom d'un élément en majuscules, lorsque nous vérifierons plus tard la valeur du nom stockée par le SGBD pour la base de données, nous la verrons en minuscules.

Nous pouvons également attribuer un utilisateur propriétaire, qui aura tous les [privilèges](https://www.postgresql.org/docs/current/ddl-priv.html) sur cet élément. Par défaut, nous pouvons faire de l'utilisateur propriétaire [postgres](https://stackoverflow.com/questions/50883645/is-postgres-a-default-and-special-user-of-postgresql), mais nous pouvons le changer plus tard avec une instruction comme celle-ci :

```pgsql
ALTER DATABASE exampledatabase
OWNER TO user3; /*user3 est un utilisateur d'exemple*/
```

Une fois la base de données créée, nous pouvons nous y connecter à l'aide de la commande SGBD `\c exampledatabase`. Enfin, nous pouvons exécuter le script **.sql** avec la commande `\i /chemin_vers_script/script.sql`. Le SGBD devrait alors nous informer que les instructions DROP n'ont eu aucun effet puisqu'il n'y a pas de table portant le nom correspondant à supprimer (la base de données est vide). Mais, après avoir créé les tables, si nous réexécutons le script, les instructions **DROP** les supprimeront car elles sont créées, empêchant le SGBD de nous donner ces notifications.

De même, si des instructions rencontrent des erreurs empêchant leur exécution, ou dans des situations spéciales comme celle que nous venons de mentionner, le SGBD nous en informera – mais il n'arrêtera pas l'exécution du script. Il passera simplement à l'exécution des instructions déclarées suivantes (au niveau syntaxique, il exécute l'instruction suivante que nous avons séparée par le `;` correspondant).

## Chapitre 11 : Exemples de requêtes

Une fois que nous aurons fait tout cela, nous aurons la base de données créée et peuplée de tables. Mais ces tables sont vides, ce qui signifie qu'elles ne contiennent aucun uplet. Ainsi, si nous voulons exécuter des requêtes sur elles qui renvoient des résultats, nous devons exécuter des instructions INSERT pour ajouter des uplets à toutes les tables.

Dans ce cas, comme la base de données est un exemple, nous n'avons pas de données réelles à utiliser pour peupler les tables, et il n'existe aucun moyen simple et automatique de les remplir avec des données synthétiques. La meilleure option consiste à utiliser la bibliothèque **Python** **faker** et à créer un script pour générer ces données synthétiques (j'ai expliqué cela dans ce **Jupyter Notebook**).

Il existe également toujours l'option de chercher des sources de données réelles pour peupler notre base de données. Mais ce faisant, ces sources de données pourraient fournir des informations dans des schémas de table qui ne correspondent pas exactement à ceux de nos tables de base de données, nous obligeant à **intégrer** puis à **insérer** les informations via un processus comme un ETL. Ces processus **ETL** d'intégration et d'insertion sont souvent appliqués dans les **Data Warehouses**, qui peuvent également être une base de données comme la nôtre.

### Exécution de requêtes de base

Juste après avoir inséré les données, la première requête que nous pouvons exécuter pour nous assurer que le processus d'insertion a fonctionné est la suivante :

```pgsql
SELECT 'person' AS tableName, COUNT(*) AS numberOfTuples
FROM Person;
```

Comme vous pouvez le voir, nous utilisons la clause FROM pour obtenir toutes les informations stockées dans la table Person (que nous aurions pu écrire entièrement en minuscules). Ensuite, nous utilisons la **fonction d'agrégation COUNT(*)** pour compter le nombre total d'uplets dans la table, en nommant la colonne où ce nombre est stocké **numberOfTuples**.

Mais, si nous voulons également afficher le nom de la table dans le même uplet que le comptage précédent, nous pouvons ajouter une autre colonne dans l'instruction SELECT où toutes ses valeurs sont **'person'**. De cette façon, lorsque la requête sera exécutée, elle renverra une table avec deux colonnes, une **tableName** et une autre **numberOfTuples**. Comme la fonction d'agrégation ne renvoie qu'une seule valeur, la table résultante n'aura qu'un seul uplet, où la colonne tableName aura la valeur 'person' et l'autre colonne affichera le nombre d'uplets dans la table **Person**.

Si nous voulons compter les uplets de toutes les tables de la base de données, nous avons la possibilité de créer une requête plus large qui rassemble tous les résultats des **sous-requêtes** qui comptent les uplets de chaque table. Pour cela, nous pouvons utiliser UNION ALL, qui combine les uplets de toutes les tables résultantes en une seule table. Cela fonctionne tant que toutes les tables résultantes ont exactement le même schéma, avec les mêmes noms de colonnes et types de données, comme dans ce cas.

```pgsql
SELECT 'person' AS tableName, COUNT(*) AS numberOfTuples
FROM Person
UNION ALL
SELECT 'city' AS tableName, COUNT(*) AS numberOfTuples
FROM city;
```

Enfin, lorsque nous disons "obtenir des informations" sur un élément du domaine ou du schéma de base de données dans ce contexte, nous entendons obtenir ses données stockées dans les attributs de la table qui le représente.

Par exemple, les informations sur une personne pourraient être l'attribut **Name** ou **Email** de la table Person, entre autres. Nous ne détaillerons pas ces informations ici, car dans la plupart des cas, il est facile de modifier les attributs sélectionnés pour être renvoyés comme résultat de requête. Mais dans un environnement réel, il est pratique et important de prêter attention aux **attributs** que la requête doit renvoyer, aux **noms/alias** qu'ils devraient avoir et à l'**ordre** dans lequel ils devraient être renvoyés. La fonctionnalité d'autres couches logicielles dépend souvent de l'exécution correcte de cette étape.

### Filtrage d'uplets

La requête que nous venons de voir est utile pour gérer la base de données. Savoir combien d'informations sont stockées dans chaque table nous aide à nous assurer que certaines opérations de normalisation ou de transformation de schéma se sont déroulées correctement (et même que les informations elles-mêmes sont exactes).

Examinons maintenant d'autres requêtes qui nous permettent d'exécuter des services fournis à l'utilisateur final. Nous les utilisons pour opérer sur le domaine selon sa sémantique, elles peuvent donc être très diverses. Ici, nous distinguerons différents types de requêtes en fonction de leur approche et des outils SQL utilisés dans leur construction.

Tout d'abord, nous avons une série de requêtes pour le filtrage d'uplets. Ces requêtes appliquent un filtre sur une table pour ne conserver que certains uplets qui répondent à des conditions spécifiques. Notez que la table contenant les uplets que nous voulons filtrer peut être générée de n'importe quelle manière, que ce soit par un JOIN, une opération d'ensemble ou tout ce que nous voulons faire. Mais si vous devez effectuer un regroupement avec GROUP BY, la table résultante doit être filtrée à l'aide d'une clause HAVING, qui diffère de la clause WHERE habituelle utilisée pour filtrer les uplets.

```pgsql
SELECT *
FROM person P
WHERE P.name LIKE 'Carol%';
```

Ce qui précède est un exemple simple qui récupère les uplets de la table Person pour les personnes dont le nom commence par **“Carol“**. Comme vous pouvez le voir, la seule instruction dont nous avons besoin pour filtrer les uplets est WHERE. Dans celle-ci, toutes les conditions requises pour le filtrage sont définies, quels que soient leur nombre ou leur nature, car certaines seront effectuées à l'aide de résultats de sous-requêtes.

Dans ce cas précis, la requête a pour condition que le nom d'une personne doit commencer exactement par la chaîne qui apparaît dans l'opérateur LIKE. Comme il est sensible à la casse, la chaîne doit correspondre exactement à ce que nous voulons rechercher ou filtrer. Ensuite, tous les uplets qui remplissent cette condition seront renvoyés dans la table résultante. Nous obtiendrons tous ses attributs grâce à la notation **SELECT \*** que nous avons utilisée.

Pour illustrer le fait qu'il n'importe pas que vous utilisiez des majuscules ou des minuscules lors du nommage des éléments de schéma dans les instructions SQL, nous pouvons voir dans la requête ci-dessous que la table City et ses attributs sont tous deux en minuscules (sauf pour un qui est écrit exactement comme il a été déclaré, avec la première lettre en majuscule). Si nous exécutons cette requête, elle fonctionnera de la même manière que si nous utilisions **C.** pour référencer les attributs, puisque l'utilisation d'une seule table signifie qu'il n'y a pas d'ambiguïté lors de la référence aux colonnes de la table.

```pgsql
SELECT *
FROM city C
WHERE (population > 20000 AND C.Latitude >=0) OR C.longitude <= 0;
```

En fin de compte, avec ces conditions, nous obtenons tous les uplets de **City** qui ont une population supérieure à 20 000 et une **latitude** positive, ou ceux qui ont simplement une **longitude** négative.

Regardons un exemple similaire : ici, nous obtenons toutes les réservations de croisière avec un prix inférieur à 500, un numéro de cabine pair et un mode de paiement en espèces (cash). Dans ce cas, nous pouvons voir comment nous pouvons appliquer différents types d'opérateurs pour construire la condition.

```pgsql
SELECT *
FROM cruiseBooking CB 
WHERE CB.price < 500 AND MOD(CB.cabinnumber, 2)=0 AND CB.paymentmethod='cash';
```

D'une part, si nous voulons déclarer que toutes les conditions que nous imposons doivent être remplies, nous utiliserons l'opérateur logique AND. Celui-ci effectue une conjonction logique de ces conditions de sorte que l'uplet sélectionné n'est ajouté à la table résultante que lorsque toutes sont remplies en même temps.

En d'autres termes, nous pouvons voir la clause WHERE comme une fonction logique qui s'exécute une fois pour chaque uplet présent dans la table que nous voulons filtrer. Ainsi, si le résultat de cette fonction logique est TRUE, alors l'uplet remplit les conditions. Sinon, il est écarté et non inclus dans la table de résultat de la requête.

Nous savons donc maintenant que toutes les conditions que nous pouvons définir dans une clause WHERE doivent être composées d'une séquence de conditions logiques plus simples comme **“CB.price < 500“** jointes par des opérateurs logiques. De plus, dans chacune de ces conditions plus simples, nous pouvons trouver plus d'opérateurs logiques, car ce sont des conditions que nous pouvons voir comme des fonctions logiques, qui peuvent elles-mêmes être composées d'une séquence de conditions encore plus simples jointes par des opérateurs logiques. Cela permet la récursion, nous permettant d'utiliser des **parenthèses** comme dans **(C1 AND (C2 OR C3))** pour ajuster la **priorité** et la **précedence** de ces opérateurs à différents niveaux de récursion dans notre condition (tout comme dans d'autres langages de programmation).

D'autre part, nous pouvons également rencontrer des conditions où des opérateurs arithmétiques ou de comparaison sont utilisés, comme dans ce cas lors de la vérification si la chaîne contenant le mode de paiement est exactement la valeur **‘cash‘**.

Alors que dans d'autres langages nous pourrions écrire `CB.paymentmethod='cash'`, en SQL nous écrivons l'opérateur de comparaison avec un seul caractère =. Si nous voulons le nier, nous pouvons le faire soit en utilisant l'opérateur logique NOT (affectant l'intégralité de la condition d'égalité), soit en utilisant `CB.paymentmethod<>'cash'` qui représente la condition où il vérifie que le mode de paiement n'est pas **‘cash‘**, ce qui signifie qu'il est différent de cette valeur.

En plus de ces opérateurs, nous disposons également d'une série de fonctions mathématiques. Par exemple, pour vérifier si un nombre est pair ou impair, dans la plupart des langages de programmation à usage général, nous avons l'**opérateur modulo %** qui calcule le reste de la division du nombre par 2 – donc s'il est 0, le nombre est pair.

Mais en SQL, ces opérations ne sont pas implémentées par défaut avec des opérateurs arithmétiques, mais plutôt avec des fonctions. Plus précisément, pour calculer le modulo, nous utilisons **MOD(Dividende, Diviseur)**, bien qu'il en existe [**beaucoup d'autres**](https://www.postgresql.org/docs/current/functions-math.html) fonctions similaires.

Nous pouvons utiliser certains des opérateurs mentionnés précédemment pour effectuer des calculs en utilisant des colonnes entières. Cela donne d'autres colonnes contenant les résultats de ces opérations.

```pgsql
SELECT *, (CURRENT_DATE - CB.bookingDate) AS DateDifference1, ABS(CB.ArrivalDateFK-CB.DepartureDateFK)
FROM cruiseBooking CB;
```

Par exemple, dans cette requête, nous voulons calculer plusieurs différences de dates, l'une étant le nombre de jours entre la date de réservation et la date actuelle, et l'autre étant le nombre de jours entre les dates de départ et d'arrivée du voyage de croisière.

Pour ce faire pour chaque uplet de la table CruiseBooking, le moyen le plus simple consiste à ajouter plusieurs colonnes qui prennent les résultats de ces calculs comme valeurs. Plus précisément, nous créons ces colonnes dans l'instruction SELECT. Celle-ci sélectionne les attributs correspondants de la table résultante de la requête et les affiche à l'utilisateur. Seuls ces attributs sont visibles par l'utilisateur, même si nous les avons obtenus à partir d'une table comportant plus d'attributs.

Mais, outre la sélection d'attributs, nous pouvons également définir de nouvelles colonnes qui n'existaient pas dans la table à partir de laquelle nous sélectionnons. Par exemple, dans cette requête, en utilisant la notation \*, nous sélectionnons tous les attributs présents dans la table de l'instruction FROM, qui est dans ce cas **CruiseBooking**.

En plus de ceux-ci, nous concaténons plus d'attributs avec une virgule, comme **DateDifference1** ou la différence entre les dates de départ et d'arrivée du voyage correspondant. Si nous regardons le résultat de la requête après avoir ajouté ces attributs supplémentaires, nous verrons une nouvelle colonne dans la table résultante appelée **DateDifference1**, qui prendra comme valeurs la différence entre la date actuelle obtenue avec **CURRENT\_DATE** et la date de réservation, qui est **CB.bookingDate**.

Nous voyons donc que dans l'instruction SELECT, nous pouvons effectuer des opérations avec les valeurs des uplets pour générer de nouvelles colonnes avec des calculs intermédiaires, ou simplement des calculs requis par la requête, comme dans ce cas.

Plus précisément, l'opération effectuée sur chaque uplet pour générer la valeur de la nouvelle colonne est définie dans l'instruction SELECT elle-même. Dans ce cas, avec **CURRENT\_DATE - CB.bookingDate**, nous définissons que la valeur de chaque uplet est égale à la date actuelle moins la date de réservation. Par défaut en SQL, cela renvoie la différence en jours entre les deux dates.

Ensuite, pour obtenir la différence entre les dates de départ et d'arrivée du voyage de croisière, nous utilisons les valeurs des attributs **DepartureDateFK** et **ArrivalDateFK** de la clé étrangère pointant vers Voyage. Cela évite d'avoir à interroger des données d'autres tables qui les contiennent.

Si nous les soustrayons simplement, selon l'ordre, nous pourrions obtenir des résultats négatifs, puisqu'une date est antérieure à l'autre. Donc, si nous voulons juste la différence absolue, nous pouvons envelopper l'opération avec la fonction **ABS()**. Et si nous n'attribuons pas de nom spécifique à cette colonne supplémentaire, SQL lui attribue par défaut le nom **“abs“**. Mais nous voudrons le changer tôt ou tard pour éviter les problèmes d'ambiguïté si nous utilisons à nouveau la fonction **ABS()** pour créer une autre nouvelle colonne.

Dans la requête précédente, nous avons vu que toutes les informations dont nous avions besoin étaient présentes dans la table CruiseBooking de la clause FROM – mais ce n'est pas toujours le cas.

Par exemple, dans la requête ci-dessous, nous voulons faire plusieurs choses : d'abord, nous voulons obtenir toutes les réservations effectuées par des personnes dont le nom commence par une lettre qui est postérieure ou égale à **‘L’**. Elles doivent également répondre à une série de conditions comme celles que nous avons vues auparavant. Enfin, nous voulons calculer la différence en jours entre la date actuelle et la date de réservation comme nous l'avons vu auparavant.

```pgsql
SELECT *, (CURRENT_DATE - CB.bookingDate) AS DateDifferenceColumn 
FROM cruiseBooking CB INNER JOIN Person P ON CB.PersonFK = P.PersonID
WHERE CB.price < 2000
    AND MOD(CB.cabinnumber, 2) = 0
    AND CB.paymentmethod = 'cash'
    AND CB.bookingDate BETWEEN '2025-01-01' AND CURRENT_DATE
    AND P.Name > 'L';
```

Pour cela, si nous utilisons uniquement la table CruiseBooking dans la clause FROM, nous ne pourrons pas accéder au nom de la personne qui a effectué la réservation, car c'est un attribut de la table Person. Nous pouvons obtenir des informations de cette table en utilisant la clé étrangère PersonFK de CruiseBooking. Ainsi, pour utiliser l'attribut Name de la Personne dans notre requête, nous devons d'une manière ou d'une autre "concaténer" ou joindre les colonnes de la table Person avec les informations de la table CruiseBooking que nous avions auparavant.

En SQL, l'opération JOIN nous permet de le faire. Il nous suffit de choisir un type et des conditions qui nous permettent d'obtenir uniquement les uplets contenant les informations que nous voulons.

Parmi tous les types de JOIN, le moins susceptible d'être utilisé en production ou dans des requêtes complexes est le **jointure implicite**. Lorsque nous utilisons une **jointure implicite**, nous effectuons un produit cartésien entre tous les uplets impliqués dans cette jointure. Ainsi, si nous voulons ne conserver que certains uplets de ce produit cartésien, nous devons utiliser une clause WHERE pour imposer certaines conditions sur les attributs.

Les jointures implicites sont plus difficiles à lire et à maintenir. Dans les requêtes volumineuses ou complexes, nous devons séparer la jointure elle-même des conditions sur le produit cartésien. Cela signifie que la logique est divisée entre la liste FROM et la clause WHERE, vous avez donc plus d'endroits à vérifier lorsque vous modifiez ou refactorisez la requête.

De plus, dans les JOIN implicites, nous ne pouvons pas effectuer d'opérations équivalentes à un OUTER JOIN car il n'y a aucun moyen de remplir certains attributs avec NULL s'ils ne sont pas référencés dans l'autre table du JOIN (entre autres inconvénients). Ainsi, le type de JOIN que nous choisissons dépendra de la condition que nous devons imposer aux uplets du produit cartésien.

Gardez simplement à l'esprit qu'il existe certains cas où il peut être pratique d'utiliser des **jointures implicites**, comme dans les requêtes impliquant très peu de tables (au plus 2 pour garder le code aussi simple que possible) avec des restrictions simples, ou lors de la maintenance de [**code hérité (legacy code)**](https://www.ibm.com/fr-fr/topics/legacy-code), c'est-à-dire du code ancien ou hérité qui utilise des jointures implicites.

Dans ce cas, lors de l'exécution du produit cartésien, nous obtiendrons une série d'uplets qui combinent tous ceux de CruiseBooking et Person. Cela donnera des uplets avec des informations sur ces deux tables où les informations de la personne ne correspondent pas à la personne référencée par la clé étrangère de l'uplet CruiseBooking.

Pour cette raison, nous n'avons pas besoin de ces uplets du produit cartésien – ou en d'autres termes, nous voulons obtenir tous ceux où la clé étrangère PersonFK de CruiseBooking pointe vers la personne dont les informations se trouvent effectivement dans ce même uplet du produit cartésien.

Formellement, nous exprimons cette condition par **CB.PersonFK = P.PersonID**. Dans ce cas, nous devons attribuer des noms d'alias aux tables pour différencier leurs attributs et résoudre d'éventuels problèmes d'ambiguïté. Ainsi, le type de JOIN le plus approprié pour cette requête est un INNER JOIN, car il nous permet de déclarer cette condition d'égalité exactement comme nous l'avons écrite ici dans une clause ON, comme vu ci-dessus.

De cette façon, en utilisant un type spécifique de JOIN qui n'est pas implicite, nous pouvons isoler toutes les conditions de filtrage des uplets dans la clause WHERE (en dédiant le FROM à l'obtention des données). Grâce au JOIN, nous pouvons concaténer les attributs d'autres tables à la table résultante de la requête, et appliquer un filtre spécifique aux uplets du produit cartésien de cette opération avec une condition d'égalité.

En ce qui concerne les conditions WHERE de cette requête, nous en avons ajouté une qui s'assure que la date de réservation est comprise entre **'2025-01-01'** et la date actuelle que nous obtenons avec **CURRENT\_DATE**. Nous aurions pu utiliser les opérateurs arithmétiques <= et <= pour cela, mais SQL nous offre une alternative plus pratique en utilisant **BETWEEN**, où nous définissons que la date de l'attribut **bookingDate** doit être comprise entre **'2025-01-01'** et **CURRENT\_DATE**, tous deux inclus.

L'opérateur BETWEEN fonctionnerait également pour vérifier si une chaîne se trouve entre une paire de chaînes, le tout comparé par ordre alphabétique. Dans cette requête, la seule condition que nous imposons sur l'ordre lexicographique d'une chaîne est **P.Name > 'L'**. Cela garantit que le nom de la personne ayant effectué la réservation commence par une lettre **supérieure ou égale** à **L**. (Si son nom est composé d'un texte qui commence par **L** suivi d'autres lettres, ce texte sera automatiquement considéré comme strictement supérieur au texte **'L'**.)

Si nous voulions ne conserver que les personnes dont le nom commence strictement par une lettre supérieure à L, nous devrions utiliser la condition **P.Name > 'M'**.

Et si nous avons besoin d'obtenir une liste de toutes les personnes de la base de données, leurs informations, ainsi que les détails de toutes les réservations de croisière qu'elles ont effectuées ? Nous aurions besoin d'une liste où toutes les personnes enregistrées dans la base de données apparaissent.

```pgsql
SELECT *
FROM cruiseBooking CB RIGHT JOIN Person P ON CB.PersonFK = P.PersonID
ORDER BY P.PersonID;
```

Par exemple, si quelqu'un a effectué 2 réservations, il y aura 2 lignes avec ses informations plus les détails des deux réservations qu'il a effectuées. Pendant ce temps, les personnes qui n'ont jamais effectué de réservation apparaîtront dans la liste avec une ligne contenant leurs informations et une série de valeurs NULL dans les colonnes où se trouveraient les informations de réservation.

Cette requête n'est pas courante dans les cas réels, mais cette structure peut être utile pour résoudre d'autres types de requêtes. Ainsi, pour construire cette liste, le premier opérateur auquel nous pourrions penser est un OUTER JOIN. Dans ce type de jointure, nous spécifions le côté de la table dont les lignes doivent toujours apparaître dans la liste finale, en complétant avec des nuls dans l'autre table si nécessaire.

Pour comprendre cela, dans cet exemple, nous voyons qu'une personne n'est pas obligée d'avoir une réservation associée – ainsi, pour chaque personne, il n'y a pas nécessairement de réservation à son nom. Il peut donc y avoir des personnes qui n'ont aucune réservation associée. Ainsi, lorsque nous essayons de faire un INNER JOIN avec la table CruiseBooking, elles n'apparaîtront pas dans la table résultante de la requête.

C'est pourquoi, au lieu d'un INNER JOIN où nous imposons une condition stricte que tous les uplets de l'opération doivent remplir, nous utilisons un OUTER JOIN. Ainsi, si nous voulons que toutes les personnes apparaissent dans la liste même si elles n'ont effectué aucune réservation, nous devons spécifier le côté de l'OUTER JOIN où nous avons placé la table Person dans l'opération JOIN.

Dans ce cas, la table Person est sur le côté droit, ce qui signifie que ses attributs sont concaténés à droite de ceux de la table CruiseBooking. Ainsi, dans l'OUTER JOIN, nous devons spécifier le côté RIGHT afin que tous les uplets de la table du côté droit apparaissent dans la liste, et pour les personnes qui n'ont aucune réservation associée, leur uplet correspondant sera rempli de valeurs NULL dans les attributs respectifs qui détiennent les informations de réservation.

Si nous avions placé la table Person sur le côté gauche, alors pour obtenir le même résultat que la requête précédente mais avec les colonnes des deux tables réordonnées, il nous suffit de changer **RIGHT** en **LEFT** dans l'opération JOIN. De cette façon, tous les uplets de la table de gauche (c'est-à-dire Person) doivent apparaître dans la table résultante. Le côté droit est rempli de valeurs NULL dans ce cas, puisque c'est là que se trouvent les attributs de la table CruiseBooking.

```pgsql
SELECT *
FROM Person P LEFT JOIN cruiseBooking CB ON CB.PersonFK = P.PersonID
ORDER BY P.PersonID;
```

D'un autre côté, dans les deux requêtes, vous pouvez voir que nous avons utilisé ON pour définir la condition d'égalité sur les uplets du produit cartésien produit par JOIN. Nous devons le faire car si nous utilisons USING au lieu de **ON**, les deux attributs sur lesquels nous voulons imposer la condition d'égalité doivent être nommés exactement de la même manière – nous ne pouvons donc pas utiliser **USING** ici.

En dehors de l'opération JOIN à partir de laquelle les données sont extraites, nous avons souvent besoin de renvoyer le résultat trié par un attribut. Il peut également être simplement utile d'avoir le résultat trié afin de pouvoir effectuer des vérifications plus rapidement, comme dans ce cas.

```pgsql
SELECT P.Birth
FROM Person P LEFT JOIN cruiseBooking CB ON CB.PersonFK = P.PersonID
ORDER BY P.PersonID;
```

Pour ce faire, à la fin de la requête, nous pouvons ajouter une instruction ORDER BY, qui trie les uplets de la table résultante selon l'attribut PersonID de la personne. Cet attribut n'a pas besoin d'apparaître dans le SELECT, car nous pourrions avoir besoin d'autres attributs qui ne sont pas ceux définissant l'ordre, comme illustré ci-dessus.

Pour en finir avec ce type de JOIN, outre la définition d'un côté comme RIGHT ou LEFT, dans un OUTER JOIN, nous pourrions également avoir besoin que tous les uplets des tables des deux côtés apparaissent. Dans la requête ci-dessous, par exemple, nous devons obtenir une liste de toutes les demandes de permis de conduire, de sorte qu'elles apparaissent toutes, une dans chaque uplet, avec toutes les informations concernant leur rejet ou leur acceptation.

```pgsql
SELECT *
FROM DrivingLicense D FULL OUTER JOIN RejectedDrivingLicense R USING (LicenseID);
```

Pour résoudre cette requête, tout d'abord, gardez à l'esprit que les contraintes du schéma nous empêchent d'avoir une demande de permis de conduire à la fois acceptée et rejetée. Ainsi, pour chaque demande enregistrée dans la base de données, il y aura soit un uplet dans RejectedDrivingLicense, soit dans DrivingLicense, selon qu'elle a été rejetée ou non. Ainsi, lors de l'obtention de la liste de requêtes, si la table résultante contient tous les attributs des deux tables, il y aura toujours des NULL dans certains d'entre eux (soit dans RejectedDrivingLicense, soit dans DrivingLicense).

Pour s'assurer que toutes les demandes apparaissent, nous pouvons effectuer un FULL OUTER JOIN, où la spécification OUTER est facultative comme nous l'avons vu à d'autres occasions. Cela force les uplets des deux tables à apparaître dans le résultat final, en remplissant avec NULL du côté correspondant pour chaque uplet.

Par exemple, si un permis est accepté et que nous essayons de le trouver dans la table **RejectedDrivingLicense**, il n'y sera manifestement pas. Ainsi, si nous faisions un **INNER JOIN**, nous n'obtiendrions pas d'uplet pour cette demande, ce qui se produit de manière similaire avec les demandes rejetées et la table DrivingLicense. Ainsi, avec un **FULL OUTER JOIN**, nous nous assurons que toutes les demandes apparaissent, en remplissant avec **NULL** dans RejectedDrivingLicense lorsque la demande est acceptée et dans l'autre table lorsqu'elle est rejetée. Dans ce cas, il est également possible d'utiliser USING dans le JOIN, puisque la condition d'égalité est basée sur des attributs de tables différentes qui ont exactement le même nom.

Un autre JOIN que nous pourrions rencontrer dans des requêtes réelles est le **NATURAL JOIN**, qui est très similaire à l'INNER JOIN mais avec une syntaxe plus simple.

```pgsql
SELECT PersonFK, RequestDate, Fee, ApprovalDate, Points
FROM DrivingLicenseRequest NATURAL JOIN DrivingLicense;
```

Par exemple, vous pouvez voir dans l'exemple ci-dessus une requête qui peut nous aider à vérifier que les contraintes d'intégrité du schéma sont respectées. Dans celle-ci, nous obtenons une liste de toutes les demandes de permis de conduire qui ont été approuvées.

Pour ce faire, nous effectuons un **NATURAL JOIN** entre la table **DrivingLicense** et sa super-classe **DrivingLicenseRequest**. Comme les seuls attributs ayant des noms équivalents sont **LicenseID**, SQL impose automatiquement la condition que l'uplet contenant les informations des deux tables ait les mêmes valeurs dans les attributs LicenseID des deux tables, en supprimant les deux attributs de la table résultante de la requête.

Cette condition imposée automatiquement, ainsi que la suppression des attributs, est ce qui caractérise le NATURAL JOIN. Il est souvent préférable à un INNER JOIN en raison de ces caractéristiques. En éliminant les attributs identiques, nous conservons les informations qui représentent réellement les personnes dans ces uplets. Nous pouvons ensuite les utiliser pour calculer diverses métriques ou même comme résultat d'une sous-requête dans une requête plus générale.

Dans ce cas précis, puisque toutes les demandes acceptées doivent être enregistrées dans la table DrivingLicenseRequest, cette requête devrait renvoyer tous les uplets de DrivingLicense. Mais si certains ne sont pas enregistrés dans DrivingLicenseRequest, la clé étrangère ne référencera aucun uplet valide dans DrivingLicenseRequest, révélant un problème d'intégrité de la base de données.

Heureusement, nous n'avons jamais à vérifier manuellement cette situation avec ces requêtes, car le SGBD vérifie automatiquement que toutes les **contraintes d'intégrité** sont respectées à chaque modification de la base de données, en particulier celles liées aux clés.

Dans les requêtes réelles, **plusieurs opérations JOIN** sont généralement utilisées dans la même instruction FROM car nous devons rassembler des données provenant de plusieurs tables (ou même de la même table).

```pgsql
SELECT *
FROM Person P
    INNER JOIN Residence R1 ON (P.PersonID = R1.PersonFK)
    INNER JOIN Residence R2 ON (
        P.PersonID = R2.PersonFK
        AND R1.CityFK <> R2.CityFK
    )
ORDER BY P.personID;
```

Par exemple, supposons que nous voulions trouver des personnes ayant vécu dans plusieurs villes différentes à un moment donné de leur vie, quel que soit le moment où elles l'ont fait. Comme notre schéma permet aux gens de vivre dans plusieurs villes à la fois, nous devrons utiliser plusieurs opérations JOIN pour rassembler les données de **Person** et **Residence** et les joindre.

Mais compte tenu de la condition que nous imposons aux personnes, pour savoir si quelqu'un a vécu dans plus d'une ville, nous devons vérifier la table Residence et voir s'il existe plusieurs uplets Residence pour la même personne avec des villes différentes.

Plus précisément, la requête que nous voulons effectuer doit obtenir toutes les personnes ayant vécu dans au moins deux villes **différentes**. Si nous imposons seulement la condition qu'une personne apparaisse dans au moins deux uplets de la table **Residence**, nous obtiendrons des personnes ayant eu au moins deux résidences – pas celles ayant vécu dans des villes différentes dans ces résidences.

Par conséquent, la condition finale finit par être que la personne apparaisse dans au moins deux uplets de **Residence** où la ville associée dans laquelle elle a vécu est **différente** dans les deux uplets. De plus, en vérifiant cette condition, nous ne garantissons pas que la personne n'a que ces deux uplets – nous avons juste besoin de savoir si elle apparaît dans au moins deux uplets présentant les caractéristiques précédentes (car une personne peut avoir eu de nombreuses résidences).

Pour implémenter cette requête, nous pourrions d'abord penser à utiliser des opérations d'ensemble et des sous-requêtes – mais il existe un moyen de la résoudre en utilisant uniquement des opérations JOIN.

Lorsque nous effectuons un JOIN entre deux tables, nous effectuons réellement le produit cartésien, dont nous ne conservons que certains uplets répondant à certaines conditions. Par exemple, lors d'un JOIN entre **Person** et **Residence**, la clé étrangère **PersonFK** dans Residence doit se référer à la personne du même uplet dans le **produit cartésien**. Cela signifie qu'elle doit correspondre à l'attribut PersonID de la table Person. Grâce à cela, nous pouvons voir que nous obtenons toutes les résidences que chaque personne a ou a eues.

Ensuite, parmi toutes celles-ci, si nous voulons vérifier qu'il y en a au moins deux avec des valeurs de **clé étrangère CityFK** différentes (ce qui signifie qu'il y a deux résidences dans des villes différentes), nous pouvons effectuer un autre JOIN de la table intermédiaire résultant du JOIN précédent avec la table Residence.

De cette façon, en plus de déclarer que sa **clé étrangère** PersonFK doit se référer à la personne correspondante de chaque uplet résultant du JOIN, nous déclarons également que la ville à laquelle elle se réfère doit être différente de la ville référencée par la table Residence précédente utilisée dans le JOIN précédent.

Pour comprendre cela de manière plus programmatique, lors d'un JOIN entre Residence et elle-même, nous obtenons des uplets qui représentent des **paires de résidences**. Nous obtenons donc une série d'uplets qui représentent ensemble le produit cartésien entre les uplets de la table Residence avec eux-mêmes.

En d'autres termes, nous nous retrouvons avec une série d'uplets où, dans chacun, nous pouvons trouver des informations provenant d'exactement 2 uplets de la table Residence, pour chaque paire possible d'uplets Residence (y compris les cas où les deux uplets sont les mêmes). Si nous ajoutons la restriction que ces paires doivent se référer à une certaine personne, alors elles seront toutes les paires possibles de résidences qu'une personne a eues.

Ensuite, si nous ajoutons également la condition que pour chaque paire de résidences les villes auxquelles elles se réfèrent doivent être différentes, nous nous retrouverons avec des uplets où la personne ayant eu ces résidences a vécu dans au moins deux villes différentes. Cela ne garantit pas qu'il y en ait exactement deux, car elle a pu vivre dans beaucoup d'autres (ce que nous pouvons voir dans les uplets résultant de ces opérations JOIN).

Lors de l'implémentation de cela en SQL, nous voyons que dans les deux clauses ON, nous déclarons la condition que les uplets Residence doivent se référer à la même personne de l'uplet que nous voulons construire – avec cette personne et une paire de ses résidences. De plus, dans le deuxième JOIN, nous déclarons la condition que les villes de la paire de résidences doivent être différentes à l'aide de l'opérateur <>. Enfin, nous trions le résultat selon les valeurs de l'attribut PersonID.

```pgsql
SELECT DISTINCT P.Name
FROM Person P
    INNER JOIN Residence R1 ON (P.PersonID = R1.PersonFK)
    INNER JOIN Residence R2 ON (
        P.PersonID = R2.PersonFK
        AND R1.CityFK <> R2.CityFK
    )
ORDER BY P.personID; /*Erreur*/
```

Comme vous pouvez le voir d'après le résultat de la requête, il y a des personnes qui ont eu de nombreuses résidences, ce qui donne de nombreuses paires de résidences qui répondent aux conditions imposées. Cela crée plusieurs uplets dans la table résultante où les mêmes informations de personne apparaissent.

Ainsi, si nous voulons seulement obtenir le nom de la personne, nous pouvons remplacer \* par **P.Name** dans l'instruction **SELECT** pour sélectionner uniquement cet attribut. Pour éviter les valeurs en double, nous pouvons utiliser **DISTINCT**. Sans DISTINCT, le nom de la même personne peut apparaître plusieurs fois, selon le nombre de paires de résidences qu'elle a eues dans différentes villes. Cela se produit également parce que SQL modélise par défaut les tables avec des multiensembles, autorisant de tels doublons.

Si nous nous soucions de supprimer les doublons, nous devrions utiliser DISTINCT – mais cette décision peut affecter d'autres instructions comme **ORDER BY**. Dans cet exemple, nous trions par les valeurs de l'attribut PersonID, dont nous n'avons pas besoin dans la table résultante où seul l'attribut Name apparaît.

Comme **PersonID** n'apparaît pas dans le SELECT après l'utilisation de DISTINCT, le SGBD nous donnera une erreur. Nous avons plusieurs options pour y remédier.

D'une part, nous pouvons supprimer DISTINCT, ce qui entraînera des données de personne en double mais triées par leur PersonID (même si cela ne sera pas affiché dans le résultat).

D'autre part, nous pouvons conserver DISTINCT et supprimer ORDER BY, car si l'attribut par lequel nous trions n'apparaît pas dans le SELECT après l'utilisation de DISTINCT, nous obtiendrons une erreur qui nous empêchera d'exécuter la requête.

Une autre alternative consiste à afficher toutes les informations sur la personne, pas seulement le nom. De cette façon, nous pouvons trier le résultat par l'attribut PersonID et supprimer les personnes en double. Au lieu d'écrire toute la liste des attributs de la table Person dans le SELECT, nous pouvons utiliser la notation **P.\*** pour désigner **tous les attributs de la table avec l'alias P**.

```pgsql
SELECT DISTINCT P.*
FROM Person P
    INNER JOIN Residence R1 ON (P.PersonID = R1.PersonFK)
    INNER JOIN Residence R2 ON (
        P.PersonID = R2.PersonFK
        AND R1.CityFK <> R2.CityFK
    )
ORDER BY P.personID;
```

Enfin, en SQL, il est courant de rencontrer des requêtes où nous devons travailler avec des dates. Par exemple, dans notre schéma, nous pourrions avoir une requête pour obtenir toutes les personnes nées en mai.

```pgsql
SELECT *, EXTRACT(MONTH FROM Birth) AS BirthMonth
FROM Person
WHERE EXTRACT(MONTH FROM Birth) = 5;
```

Nous pouvons résoudre ce problème en imposant une condition unique sur la date de naissance, avec la particularité que nous ne pouvons pas traiter le type de données exactement comme s'il était entièrement numérique ou textuel. Au lieu de cela, nous devons extraire des [caractéristiques](https://www.w3schools.com/sql/func_mysql_extract.asp) de la date pour opérer avec.

Dans ce cas, la caractéristique la plus claire à obtenir est le mois. En utilisant la fonction EXTRACT() et la caractéristique MONTH, nous extrayons le numéro du mois de la date de l'attribut Birth pour vérifier s'il s'agit de mai ou non.

Notez que la fonction renvoie généralement des nombres pour le jour, le mois, l'année, etc., et non des chaînes de caractères. Nous traitons donc le mois comme s'il s'agissait d'un nombre de 1 à 12.

Nous pouvons convertir entre nombre et chaîne [à l'aide d'autres outils SQL](https://learn.microsoft.com/fr-fr/sql/t-sql/functions/cast-and-convert-transact-sql?view=sql-server-ver17), le tout dans le format approprié selon le fuseau horaire et la zone géographique. Ensuite, si nous voulons que cette caractéristique de date apparaisse comme un attribut supplémentaire dans la table résultante, nous traitons simplement la fonction EXTRACT() comme s'il s'agissait de n'importe quelle fonction SQL qui renvoie une valeur lorsqu'on lui donne certaines valeurs d'un uplet.

Mais même si nous lui attribuons un alias, nous ne pouvons pas utiliser cet alias dans la clause WHERE pour déclarer la condition qu'il soit égal à 5. Au lieu de cela, nous devons écrire l'intégralité du calcul dans la clause WHERE. Bien que cela puisse sembler inefficace en termes de lisibilité, sans utiliser de techniques supplémentaires d'[**Expression de Table Commune (CTE)**](https://www.freecodecamp.org/news/mysql-common-table-expressions/) comme celles que nous verrons plus tard, nous n'avons pas d'autre choix que de dupliquer le calcul de l'attribut dans la clause WHERE si nous voulons lui imposer une condition.

```pgsql
SELECT *, EXTRACT(WEEK FROM Birth)
FROM Person;
```

En plus du jour, du mois et de l'année, la fonction **EXTRACT()** nous permet d'obtenir toutes sortes de caractéristiques d'une date, comme le numéro de la semaine avec **WEEK** comme illustré ci-dessus, ou le numéro du trimestre actuel avec **QUARTER**.

### Sous-requêtes

Il existe certaines requêtes SQL qui nécessitent des sous-requêtes. Une sous-requête est simplement une requête à l'intérieur d'une autre requête. Elle vous aide à résoudre un problème plus petit afin que la requête principale puisse en résoudre un plus grand.

Plongeons un peu plus profondément. Lorsque vous exécutez une requête en SQL, vous obtenez une table de résultat (un multiensemble, puisque les lignes peuvent se répéter). Une sous-requête permet à la requête externe d'utiliser ce résultat – par exemple, pour vérifier l'appartenance ou l'existence.

```pgsql
SELECT *
FROM Person P
WHERE P.PersonID IN (SELECT PersonFK FROM Residence);
```

Ceci renvoie chaque personne dont l'identifiant apparaît dans Residence.PersonFK – c'est-à-dire tous ceux qui ont (ou ont eu) une résidence enregistrée. La sous-requête produit l'ensemble des ID de personnes référencés, tandis que la requête externe conserve les lignes où p.PersonID est dans cet ensemble.

Notez qu'il s'agit d'une [sous-requête non corrélée](https://www.ibm.com/docs/fr/db2-for-zos/12.0.0?topic=subqueries-correlated-non-correlated) (elle ne fait pas référence à la requête externe), que de nombreuses bases de données peuvent **matérialiser une seule fois** ou réécrire sous forme de **semi-jointure** avant d'appliquer le filtre IN. En pratique, cela est généralement comparable à une formulation équivalente basée sur EXISTS ou JOIN. Nous choisirons simplement la forme la plus claire et ajouterons des index appropriés (par exemple, Residence(PersonFK), Person(PersonID)) pour la rapidité.

Si la sous-requête peut renvoyer NULL, IN utilise une logique à trois valeurs. Avec une clé étrangère sur Residence.PersonFK, les valeurs NULL sont généralement interdites, ce n'est donc pas un problème.

D'un autre côté, nous pouvons résoudre la requête en utilisant des opérations JOIN comme illustré ci-dessous :

```pgsql
SELECT DISTINCT P.*
FROM Person P INNER JOIN Entry E ON P.PersonID=E.PersonFK;
```

Ici, nous combinons les données de Person et Residence en utilisant la condition d'égalité qui exige que la clé étrangère de Residence se réfère à la personne dans le même uplet du produit cartésien. De cette façon, nous n'obtenons que les uplets qui ont les informations d'une résidence et de la personne qui lui est associée.

Ensuite, pour ne conserver que les données des personnes, nous utilisons P.\* comme auparavant – mais ici nous devons utiliser DISTINCT, car une personne peut avoir plusieurs résidences. Spécifier DISTINCT empêche cela de dupliquer les données de la même personne.

L'opération JOIN est souvent considérée comme inefficace car il s'agit d'un produit cartésien qui doit construire tous les uplets de ce produit puis les filtrer à l'aide des conditions que nous déclarons. Mais nous pouvons la rendre plus rapide avec le matériel approprié, comme des [**GPU**](https://arxiv.org/html/2406.13831v1).

Pourtant, ici, nous devons supprimer les doublons avec DISTINCT, ce qui implique un traitement supplémentaire du résultat de la requête. Nous avons également besoin d'un autre filtre ou processus qui élimine les uplets en double, ce qui semble donc moins efficace à première vue.

Mais selon la façon dont le SGBD implémente ces opérations au niveau physique, cela peut être plus ou moins efficace que l'utilisation de sous-requêtes (car le matériel fait également une différence).

Voici une autre construction basée sur des sous-requêtes que nous pouvons utiliser pour résoudre la requête précédente. Comme vous pouvez le voir, nous construisons une **sous-requête corrélée** où nous utilisons l'attribut PersonID de la requête de "niveau supérieur" pour obtenir toutes les résidences (uplets) de la table Residence qui appartiennent à la personne indiquée par l'identifiant PersonID. En d'autres termes, puisque la clause WHERE est exécutée pour chaque uplet de Person, nous pouvons construire une sous-requête où, pour une certaine personne avec cet identifiant, nous pouvons obtenir toutes les résidences enregistrées à son nom. Ce seraient celles dont la clé étrangère PersonFK se réfère à l'identifiant PersonID de la personne.

```pgsql
SELECT *
FROM Person P
WHERE EXISTS (
        SELECT *
        FROM Residence R
        WHERE R.PersonFK = P.PersonID
    );
```

Avec cette sous-requête corrélée, SQL doit construire son résultat pour chaque personne de la table Person, car le résultat dépend de la personne spécifique en cours de traitement. Ainsi, pour ne conserver que les personnes ayant une résidence, nous utilisons l'opérateur **EXISTS** pour vérifier que le multiensemble résultant de la sous-requête contient au moins un uplet (indiquant que la personne a une résidence).

SQL doit parcourir la table Residence pour chaque personne de la table Person, bien qu'il ne parcoure Residence que jusqu'à ce qu'il trouve le premier uplet dont la clé étrangère pointe vers la personne correspondante. Cela évite des vérifications inutiles du reste des uplets dans **Residence** car **EXISTS** ne nécessite qu'au moins un uplet dans la sous-requête.

Pourtant, dans le [**pire des scénarios**](https://medium.com/learning-data/understanding-algorithmic-time-efficiency-in-sql-queries-616176a85d02), il devrait parcourir toute la table pour chaque personne si aucune personne n'a ou n'a eu de résidences.

Une autre façon d'utiliser les opérateurs d'appartenance ou d'existence consiste à utiliser une liste de valeurs. Celle-ci est déclarée de manière très similaire à un uplet et une sous-requête mais n'est pas nécessairement un uplet ou une sous-requête.

```pgsql
SELECT *
FROM Pool P
WHERE Status IN ('closed', 'renovation')
    AND mindepth IN (
        SELECT mindepth
        FROM Pool
        WHERE mindepth > 4
    );
```

Par exemple, ci-dessus nous avons une requête qui renvoie toutes les piscines dont le statut est ‘closed’ ou ‘renovation’ et dont la profondeur minimale est supérieure à 4.

Pour vérifier la première condition, nous pourrions facilement utiliser l'opérateur logique OR et déclarer deux conditions plus simples pour vérifier si la valeur Status est soit **‘closed’**, soit **‘renovation’**. Mais nous pouvons le faire plus simplement en utilisant l'opérateur IN. Ainsi, en utilisant la notation **('closed', 'renovation')**, nous déclarons une liste avec ces deux valeurs, en vérifiant avec IN si la valeur contenue dans l'attribut Status est dans la liste ou non. Cela a le même effet que l'utilisation de l'opérateur OR, mais avec une syntaxe plus claire et une efficacité similaire.

Cette vérification que nous effectuons avec IN est comme une vérification d'appartenance sur le résultat d'une sous-requête, car la syntaxe est très similaire. Mais ne confondez pas la déclaration de liste avec une sous-requête, car **('closed', 'renovation')** ne représente pas un multiensemble avec des uplets, mais plutôt une liste de valeurs. Nous pouvons également le voir comme s'il s'agissait d'une colonne sur laquelle nous effectuons une vérification.

D'un autre côté, le moyen le plus simple de vérifier si la profondeur minimale de la piscine est supérieure à 4 est d'utiliser directement la condition **mindepth > 4**. Mais pour montrer une manière équivalente de vérifier avec des sous-requêtes, vous pouvez voir ci-dessus que la sous-requête pour la condition récupère toutes les valeurs mindepth de la table Pool qui sont strictement supérieures à 4. Ensuite, elle utilise IN pour vérifier si la valeur mindepth de la table Pool de la requête externe se trouve dans le résultat de la sous-requête.

Ainsi, au lieu d'écrire directement mindepth > 4, la sous-requête sélectionne d'abord toutes les valeurs mindepth supérieures à 4, et la requête externe utilise IN pour ne conserver une ligne de piscine que si sa profondeur minimale est dans cet ensemble. En pratique, bien que cela puisse également être une solution à la requête, nous devrions garder le code aussi simple que possible. Nous évitons généralement ces techniques.

De plus, nous n'avons pas besoin de l'**alias P.** pour désigner le mindepth de la requête externe – car c'est le seul appelé ainsi dans cette requête. Mais si nous devions l'utiliser dans la sous-requête, nous devrions utiliser l'alias P. pour le distinguer de l'attribut mindepth de la table **Pool** dans la sous-requête. (Celle-ci n'a pas non plus besoin d'alias car c'est une sous-requête simple sans autre sous-requête à l'intérieur. C'est possible de le faire, et parfois même nécessaire.)

Voici une autre façon équivalente de résoudre la requête à l'aide de sous-requêtes :

```pgsql
SELECT *
FROM Pool P
WHERE Status IN ('closed', 'renovation')
    AND P.mindepth > ALL (
        SELECT mindepth
        FROM Pool
        WHERE mindepth <= 4
    );
```

La différence principale est qu'ici, la sous-requête obtient toutes les valeurs mindepth qui sont <= 4, ce qui est la condition opposée à celle que nous voulons que les uplets remplissent. Ainsi, dans la requête externe, nous avons le résultat de cette sous-requête, qui inclut toutes les valeurs mindepth qui ne nous intéressent pas.

Pour vérifier si un uplet remplit la condition d'avoir une profondeur minimale > 4 à l'aide de ces valeurs, nous utilisons l'opérateur **> ALL** pour vérifier si le mindepth de l'uplet que nous vérifions est strictement supérieur à toutes les valeurs présentes dans la sous-requête.

Cette manière équivalente de résoudre la requête est plus élaborée que la solution la plus simple et la plus efficace, qui consiste à utiliser directement la condition **mindepth > 4**. C'est simplement un exemple pour démontrer qu'il existe souvent plus d'une façon d'obtenir le **même résultat** pour **n'importe quel état** de la base de données. C'est la définition de **requêtes équivalentes**.

De plus, dans de nombreuses situations, il est utile d'utiliser des opérateurs tels que ANY, IN, ALL, EXISTS, etc. en combinaison avec d'autres opérateurs arithmétiques sur une sous-requête pour définir des conditions que certains uplets doivent remplir, comme illustré dans ces exemples.

Jusqu'à présent, nous avons vu des requêtes qui utilisent des sous-requêtes dans leur implémentation, mais ces sous-requêtes se comportent essentiellement comme si elles étaient des requêtes elles-mêmes. Cela signifie que nous pouvons les exécuter directement sur le SGBD comme s'il s'agissait de requêtes régulières. Ainsi, rien n'empêche une sous-requête d'être composée de sous-requêtes à un niveau "inférieur", c'est-à-dire des sous-requêtes qui se trouvent à un **niveau d'imbrication** inférieur à l'autre **sous-requête**, qui à son tour se trouve à un niveau d'imbrication inférieur à la **requête** dans laquelle elle se trouve.

Fondamentalement, SQL nous permet de chaîner autant de sous-requêtes que nous le souhaitons à l'intérieur d'une requête ou d'une sous-requête. Cela nous aide à résoudre des problèmes comme la requête ci-dessous, qui récupère une liste avec des informations sur toutes les personnes qui n'ont pas de permis de conduire valide :

```pgsql
SELECT *
FROM Person P
WHERE NOT EXISTS (
        SELECT *
        FROM DrivingLicense D
        WHERE D.LicenseID IN (
                SELECT LicenseID
                FROM DrivingLicenseRequest R
                WHERE R.PersonFK = P.PersonID
            )
    );
```

Nous pourrions aborder cette requête de sorte qu'elle nécessite des opérations JOIN pour la résoudre. Mais dans ce cas, elle est structurée de manière "imbriquée" au niveau de la sous-requête de sorte qu'elle nécessite l'utilisation de sous-requêtes.

Ainsi, pour obtenir cette liste, nous parcourons d'abord toutes les personnes de la table Person. Pour chacune d'elles, nous vérifions qu'il n'existe aucun permis de conduire dont la demande associée a été créée par cette personne. Nous pouvons implémenter cette condition en appliquant l'opérateur **NOT EXISTS** à une sous-requête qui renvoie tous les permis de conduire valides associés à une personne. Nous les obtenons en filtrant DrivingLicense pour les permis dont la ligne DrivingLicenseRequest correspondante a PersonFK = P.PersonID – c'est-à-dire les permis demandés par la personne actuelle.

Concernant ce dernier point, comme vous pouvez le voir dans le code, le moyen le plus simple de l'implémenter avec des sous-requêtes est de vérifier que le LicenseID du permis de conduire valide existe dans l'ensemble des valeurs LicenseID des demandes de la table DrivingLicenseRequest dont la clé étrangère pointe vers la personne en cours d'itération dans Person. Cela rend cette sous-requête **corrélée** à la requête externe que nous effectuons, car elle inclut l'attribut **P.PersonID**.

En résumé, nous avons implémenté cette requête en **imbriquant des sous-requêtes**, où SQL nous permet d'atteindre un niveau d'imbrication arbitraire selon les besoins de la requête. Mais nous aurions pu le faire d'autres manières comme l'utilisation d'opérations JOIN, qui dans certaines situations sont plus faciles à comprendre que l'approche que nous venons de suivre.

Rappelez-vous simplement que l'imbrication de requêtes n'est pas toujours le meilleur moyen de résoudre un problème, surtout lorsque plusieurs niveaux d'imbrication sont créés (qu'ils soient corrélés ou non entre eux). Nous montrons simplement ce qui est possible ici. Cela n'en vaut la peine que si cela améliore suffisamment l'efficacité ou la clarté de la requête par rapport à d'autres alternatives.

Parlons de l'endroit ou de l'instruction dans laquelle les sous-requêtes peuvent être imbriquées. Dans le code ci-dessous, vous pouvez voir comment la sous-requête est imbriquée dans la clause FROM.

```pgsql
SELECT P.Name
FROM Person P
    INNER JOIN (
        SELECT DISTINCT PersonFK
        FROM Rental
    ) R ON R.PersonFK = P.PersonID;
```

Comme elle renvoie une table avec des uplets, nous utiliserons souvent ce résultat de requête dans une clause FROM pour obtenir les informations des uplets et les renvoyer à l'utilisateur via un SELECT. Ou nous pourrions même la combiner avec une autre table à l'aide d'une opération JOIN, comme dans ce cas. Plus précisément, cette requête obtiendra des informations sur toutes les personnes ayant loué un vélo à un moment donné au moins une fois.

Ainsi, l'approche que nous suivons pour résoudre la requête consiste à effectuer un JOIN entre la table Person (qui contient toutes les personnes du système) et une table qui possède les identifiants des personnes pointées par la **clé étrangère** **{PersonFK}** de n'importe quel uplet dans Rental. Cela signifie toute personne dont l'identifiant est référencé par n'importe quel uplet dans Rental, ce qui implique qu'elle a loué un vélo au moins une fois.

Nous pouvons construire cette liste d'identifiants de personnes à l'aide d'une sous-requête qui extrait toutes les valeurs PersonFK de la table Rental tout en supprimant les doublons. Une personne peut avoir effectué un nombre arbitraire de locations tout au long de son histoire, mais nous sommes intéressés de savoir si elle en a effectué au moins une. Nous avons donc simplement besoin de savoir si elle apparaît dans la liste des valeurs PersonFK.

Ensuite, à l'aide d'un **INNER JOIN**, nous combinons les informations de PersonFK renvoyées par la sous-requête avec les uplets de la table Person. Cela nous donne toutes les informations des personnes identifiées par **PersonFK**, qui à son tour pointe vers **PersonID**. Mais comme nous voulons, par exemple, les noms des personnes et pas seulement leurs identifiants, le **JOIN** et la **sous-requête** sont tous deux essentiels, car si nous n'avions besoin que de l'identifiant, il suffirait de renvoyer ce que la sous-requête fournit.

En plus d'imbriquer des sous-requêtes dans la clause FROM, nous pouvons également le faire dans la clause SELECT, où l'objectif principal est de calculer une métrique ou d'obtenir plus d'informations pour chaque uplet de la requête. C'est-à-dire que si dans le SELECT nous obtenons les attributs **P.PersonID** et **P.Name** de chacun des uplets renvoyés à l'utilisateur, nous pourrions vouloir obtenir plus d'informations au-delà de ces deux attributs qui doivent être calculées avec une requête. Dans ce cas, cette requête sera imbriquée en tant que sous-requête dans le SELECT, et son résultat sera la valeur ajoutée à l'attribut supplémentaire représentant la sous-requête dans le SELECT.

```pgsql
SELECT P.PersonID,
    P.Name,
    (
        SELECT COUNT(*)
        FROM Residence R
        WHERE R.PersonFK = P.PersonID
    ) AS NumResidences
FROM Person P;
```

Dans ces cas où la sous-requête est imbriquée dans l'instruction SELECT, la sous-requête doit répondre à une exigence de base : elle doit renvoyer au plus un uplet et une colonne. En effet, le résultat de la sous-requête sera ajouté dans une nouvelle **colonne supplémentaire (et une seule)** dans notre SELECT. Ensuite, nous calculerons son résultat et l'ajouterons dans chaque uplet de la requête externe – la sous-requête ne peut donc pas renvoyer plus d'un uplet.

Par exemple, dans cette requête, nous voulons lister toutes les personnes de la base de données ainsi qu'une colonne contenant le nombre de résidences qu'elles ont eues. Pour résoudre ce problème, l'approche la plus simple consiste à parcourir tous les uplets de Person et, pour chacun d'eux, à compter combien d'uplets de Residence ont leur clé étrangère PersonFK référençant cette personne.

Parcourir les uplets de Person est simple : nous utilisons simplement une combinaison de SELECT et FROM. Mais pour compter combien d'uplets de Residence remplissent cette condition pour chaque personne, nous avons besoin d'une sous-requête corrélée – spécifiquement avec la personne en cours de traitement. Nous pouvons l'identifier de manière unique avec P.PersonID.

Nous devons faire cela car pour compter les uplets dans Residence, nous devons comparer les valeurs de leur clé étrangère PersonFK avec l'identifiant P.PersonID. Pour obtenir la valeur de ce comptage, nous pouvons utiliser une sous-requête : la fonction d'agrégation **COUNT(*)** nous permet de compter tous les uplets présents dans Residence. Elle le fait après les avoir filtrés avec la condition que leur clé étrangère PersonFK référence la personne en cours de traitement dans la table Person.

Il est important de noter que la sous-requête ne renverra qu'une seule valeur générée par COUNT(), et une seule colonne générée par cette fonction. Cela répond à l'exigence que toute sous-requête utilisée dans l'instruction SELECT doit remplir.

Enfin, il convient de mentionner que cette valeur générée dans la sous-requête peuple une colonne supplémentaire que nous avons ajoutée en incluant la sous-requête elle-même dans le SELECT pour chaque uplet de notre requête. En d'autres termes, chaque uplet aura besoin d'une valeur pour cette **nouvelle colonne**, qu'il obtiendra en exécutant la sous-requête corrélée sur cet uplet spécifique.

SELECT et FROM ne sont pas les seules instructions où les sous-requêtes sont autorisées. Nous pouvons également les utiliser dans une clause WHERE, HAVING, ou même ORDER BY. Plus important encore, une requête peut comporter un nombre arbitraire de sous-requêtes (imbriquées ou non) selon ses besoins.

```pgsql
SELECT P.PoolID,
    P.Name AS PoolName,
    C.Name AS CityName,
    P.Status,
    (
        SELECT PoolID
        FROM CityPool C
        WHERE C.PoolID = P.PoolID
    ) AS CityPoolID
FROM (
        SELECT *
        FROM Pool
        WHERE Status = 'maintenance'
    ) AS P
    JOIN City C ON P.CityFK = C.CityID;
```

Par exemple, dans une requête comme celle ci-dessus, nous pouvons voir qu'il y a non seulement une sous-requête dans le SELECT mais aussi une dans le FROM.

Dans ce cas précis, la requête obtient des informations sur toutes les piscines actuellement en maintenance, y compris des détails sur la ville où les piscines sont situées (comme son nom). Il y a également une colonne supplémentaire indiquant l'identifiant de la piscine s'il s'agit du type CityPool, en le laissant vide si ce n'est pas le cas.

Ainsi, pour résoudre cette requête, nous devons d'abord obtenir des informations sur les piscines en maintenance. Cela consiste simplement à parcourir les uplets de la table Pool et à sélectionner ceux dont la valeur Status est **‘maintenance’**.

Ensuite, pour rassembler des informations sur la ville où chaque piscine est située (ainsi que les uplets Pool que nous venons d'obtenir), nous pouvons utiliser un JOIN qui opère sur les uplets précédents et la table City. C'est pourquoi nous extrayons tous les uplets Pool à l'aide d'une sous-requête.

Ainsi, bien que le type de JOIN ne soit pas explicitement spécifié, en utilisant la clause ON, SQL l'interprète automatiquement comme un INNER JOIN (il serait également interprété comme un type INNER si nous avions utilisé la clause USING). Mais cette pratique n'est pas recommandée, car dans la plupart des situations où le type de JOIN est omis, la lisibilité du code est compromise, surtout lorsqu'il y a de nombreux JOIN dans la même requête.

Ici, dans la clause ON, la condition JOIN stipule que dans le même uplet du produit cartésien, la clé étrangère CityFK – qui représente la ville où se trouve la piscine – doit avoir la même valeur que l'identifiant CityID de la ville dans l'uplet.

Ensuite, pour attacher la colonne supplémentaire avec l'identifiant de la piscine de CityPool pour les uplets qui représentent des piscines de ce type, respectivement, nous utiliserons une sous-requête. Cette sous-requête recherche dans la table CityPool un uplet dont le PoolID correspond au PoolID de Pool. Cela vérifie si la piscine de Pool est réellement du type CityPool ou non.

De cette façon, la sous-requête renverra la **valeur de l'identifiant** s'il s'agit du **type CityPool** – sinon, elle ne renverra **rien**, ce qui signifie qu'elle renverra une **table sans uplets** (ou en d'autres termes, un ensemble vide ou un **multiensemble**, plutôt).

Ceci est autorisé en SQL, mais cela peut parfois provoquer des erreurs, il n'est donc généralement pas de bonne pratique d'utiliser des sous-requêtes dans le SELECT dont il n'est pas garanti qu'elles renvoient au moins un uplet.

Ainsi, pour les piscines qui ne sont pas du type CityPool, la sous-requête ne renverra rien. Cela signifie que la valeur de la colonne supplémentaire dans le SELECT sera NULL comme nous pouvons le voir lors de l'exécution de la requête.

Comme elle ne renvoie aucun uplet avec aucune valeur, nous insérerons une valeur **inconnue**. La façon de représenter cela en SQL est avec la valeur spéciale NULL. De plus, cette colonne supplémentaire n'a pas de nom par défaut, nous pouvons donc lui attribuer un alias reconnaissable à l'aide de la clause AS comme illustré dans la requête.

D'un autre côté, si nous voulons éviter d'avoir des valeurs NULL dans la colonne supplémentaire, nous pouvons faire en sorte que cette colonne contienne des valeurs booléennes où TRUE indique que la piscine est du type CityPool et FALSE qu'elle ne l'est pas.

En partant de la même requête qu'auparavant, le seul changement que nous devons faire pour y parvenir est d'ajouter une vérification **IS NOT NULL**. Pour chaque uplet, elle vérifie si la valeur insérée dans la colonne supplémentaire **CityPoolType** est NULL ou non. Ainsi, si son type est bien CityPool, la valeur de la colonne supplémentaire fournie par la sous-requête originale ne sera pas NULL. Cela répond à la condition IS NOT NULL et renvoie TRUE. Inversement, si elle n'est pas de ce type, IS NOT NULL ne sera pas remplie, et la colonne supplémentaire dans ce cas sera remplie avec FALSE.

```pgsql
SELECT P.PoolID,
    P.Name AS PoolName,
    C.Name AS CityName,
    P.Status,
    (
        SELECT PoolID
        FROM CityPool C
        WHERE C.PoolID = P.PoolID
    ) IS NOT NULL AS CityPoolType
FROM (
        SELECT *
        FROM Pool
        WHERE Status = 'maintenance'
    ) AS P
    INNER JOIN City C ON P.CityFK = C.CityID;
```

Ici, nous devons faire attention à l'endroit où nous plaçons la condition IS NOT NULL. D'une part, nous pourrions penser à comparer l'attribut PoolID de la table CityPool elle-même dans la clause SELECT de la sous-requête. Si nous faisons cela, nous comparerons une valeur qui peut exister ou non avec NULL, de sorte que le résultat final de la sous-requête sera FALSE si la piscine est du type CityPool.

Mais si elle est d'un autre type, il n'y aura même pas de valeur pour cet attribut PoolID dans la table CityPool, la comparaison avec NULL ne sera donc pas exécutée. Cela fera en sorte que la sortie finale de la requête aura la colonne supplémentaire contenant des valeurs NULL pour les piscines qui ne sont pas du type CityPool et FALSE pour celles qui sont du type correspondant.

Cela se produit parce que nous ne devrions pas comparer PoolID avec NULL, car sa valeur peut exister ou non. Et si elle n'existe pas, la vérification ne sera pas exécutée pour tous les uplets de notre requête.

Au lieu de cela, nous devrions effectuer cette vérification sur le résultat de la sous-requête entière. Elle peut être NULL lorsque la piscine n'est pas de type CityPool – et nous voyons donc des valeurs dans la colonne supplémentaire remplies de NULL dans le résultat final. Ou elle peut contenir un identifiant valide différent de NULL, ce qui viole la condition IS NOT NULL.

En résumé, la vérification pour s'assurer que la colonne supplémentaire est de type **booléen** doit comparer le résultat de la sous-requête entière (qui est soit NULL, soit une valeur spécifique) avec la valeur NULL elle-même. Cela vérifie si chaque uplet de notre table résultante correspond ou non.

En résumé, bien qu'il ne soit pas de bonne pratique d'utiliser des sous-requêtes dans la clause SELECT pouvant aboutir à un **ensemble vide**, nous pouvons le faire tant que cela ne dégrade pas la lisibilité ou l'efficacité de la requête. Nous devons également avoir certaines garanties qu'elle fait ce qu'on attend d'elle.

Jusqu'à présent, nous avons effectué des vérifications d'appartenance avec IN, ainsi que des vérifications avec d'autres opérateurs. Nous avons utilisé des attributs individuels pour vérifier si la valeur d'un certain attribut se trouvait dans un ensemble formé par les valeurs d'un attribut, entre autres conditions. Et parfois, nous avons besoin que ces conditions impliquent plus d'un attribut pour la vérification.

```pgsql
SELECT E.EntryTimestamp, E.PersonFK, E.PoolFK
FROM Entry E
WHERE (E.EntryTimestamp, E.PersonFK, E.PoolFK) IN (
        SELECT PS.EntryFK, PS.PersonFK, PS.PoolFK
        FROM PoolSanction PS
    );
```

Par exemple, ci-dessus nous avons une requête qui récupère tous les uplets de Entry qui ont été sanctionnés par une sanction de piscine de la table PoolSanction. Pour ce faire, nous devons simplement parcourir les uplets de Entry et, pour chacun d'eux, vérifier s'il a une sanction. En d'autres termes, nous vérifions s'il existe un uplet dans PoolSanction dont la clé étrangère vers Entry référence l'uplet que nous examinons.

En faisant cela, la première chose que nous remarquons est que la clé primaire de Entry ne se compose pas d'un seul attribut, mais de 3. C'est exactement comme la clé étrangère dans PoolSanction – elle détermine que l'entrée qui a été sanctionnée n'a pas un attribut, mais trois.

Ainsi, dans des conditions normales, nous pourrions utiliser une sous-requête pour obtenir toutes les valeurs de clé étrangère de PoolSanction, puis vérifier si l'identifiant (clé primaire) de chaque entrée appartient à cet ensemble de valeurs à l'aide de l'opérateur IN. Mais ici, nous ne pouvons pas le faire de la même manière car nous devons travailler avec trois attributs au lieu d'un.

C'est pourquoi, dans la sous-requête, au lieu de renvoyer un seul attribut, nous renvoyons tous ceux qui composent la clé étrangère vers Entry (ce sont **(EntryFK, PersonFK, PoolFK)**). Grâce à cela, nous avons un ensemble d'uplets où chacun se réfère à un uplet de Entry qui a été sanctionné.

Plus précisément, chacun de ces uplets de l'ensemble se réfère aux trois attributs qui composent la clé primaire de Entry, qui sont **(EntryTimestamp, PersonFK, PoolFK)**. Ainsi, pour vérifier si une entrée appartient à cet ensemble, nous le parcourons simplement en cherchant si l'un des uplets correspond exactement à l'uplet de la clé primaire de l'entrée (avec les trois attributs ayant des valeurs égales).

Nous faisons cela à l'aide de l'opérateur IN, où au lieu de spécifier un seul attribut, nous pouvons en spécifier un nombre arbitraire entre parenthèses. Ainsi, l'opérateur IN effectuera la même opération que dans les cas précédents, en prenant la clé primaire **(EntryTimestamp, PersonFK, PoolFK)** de chaque entrée et en la comparant avec chacun des uplets de la sous-requête, attribut par attribut. Si l'un d'eux correspond, alors il appartient à l'ensemble, remplissant la condition.

Ici, il est très important de noter que les uplets comparés par IN doivent être de la même taille. Cela signifie qu'ils doivent avoir le même nombre d'attributs, le même type de données (ou du moins être comparables), et que leur sémantique doit être la même. C'est-à-dire que si pour chaque uplet de Entry nous utilisons **(EntryTimestamp, PersonFK, PoolFK)** pour vérifier si cet uplet à trois attributs est dans l'ensemble de la sous-requête, alors cette sous-requête doit contenir des uplets de trois attributs où :

* le premier est **EntryFK**, qui se réfère à l'attribut **EntryTimestamp** de la clé primaire de Entry,
* le deuxième est **PersonFK**, se référant à **PersonFK** de la clé primaire,

et ainsi de suite. Cela garantit que la comparaison est sémantiquement correcte, même si dans le DDL la clé primaire a pu être définie dans un ordre complètement différent.

Une autre variante de cette requête consiste à lister toutes les entrées sanctionnées ainsi que les informations de la personne qui possède l'entrée.

```pgsql
SELECT P.*, E.EntryTimestamp, E.PersonFK, E.PoolFK
FROM Person P INNER JOIN Entry E ON P.PersonID=E.PersonFK
WHERE (E.EntryTimestamp, E.PersonFK, E.PoolFK) IN (
        SELECT PS.EntryFK, PS.PersonFK, PS.PoolFK
        FROM PoolSanction PS
    );
```

Pour cela, sur la base de la solution précédente où nous avons obtenu la liste des entrées sanctionnées, la seule étape supplémentaire que nous devons franchir est d'effectuer un JOIN entre Entry et Person. Ce faisant, nous ne conservons que les uplets du produit cartésien où la clé étrangère PersonFK de Entry se réfère à la clé primaire {PersonID} à partir des informations provenant de Person.

Nous pouvons également voir que la condition vérifiant si l'entrée est sanctionnée ou non est la même. Avec cet exemple, nous pouvons voir plus clairement le but de l'opération JOIN, qui est de rassembler des informations provenant de plusieurs tables. Ainsi, pour chaque entrée sanctionnée que nous avions auparavant, si nous devons maintenant concaténer les informations de la personne vers laquelle pointe la clé étrangère PersonFK, nous pouvons simplement effectuer le produit cartésien entre les deux tables et imposer une condition pour s'assurer que la référence de PersonFK est bien la personne présente dans l'uplet.

En continuant avec les utilisations de cette dernière technique, où nous utilisons des opérateurs comme IN pour vérifier si une certaine combinaison de valeurs d'attribut appartient à un ensemble d'uplets, dans l'exemple suivant nous avons une requête qui liste tous les trajets de la table Voyage pour lesquels il existe un trajet de retour. C'est-à-dire que nous devons trouver tous les trajets allant de la ville A à la ville B pour lesquels il existe au moins un autre trajet différent allant de B à A.

```pgsql
SELECT *
FROM Voyage V
WHERE (V.DepartureCityFK, V.ArrivalCityFK) IN (
        SELECT V2.ArrivalCityFK,
            V2.DepartureCityFK
        FROM Voyage V2
    )
ORDER BY (V.DepartureCityFK, V.ArrivalCityFK);
```

Pour ce faire, la première chose que nous devons réaliser est que la clé primaire de Voyage inclut les attributs **DepartureCityFK** et **ArrivalCityFK**, qui se réfèrent respectivement aux villes de départ et d'arrivée du trajet. Ainsi, si nous avons plusieurs trajets avec des valeurs différentes dans ces attributs, nous saurons avec certitude que les deux trajets sont différents. En effet, même si le reste des attributs de la clé primaire était identique, tant qu'au moins l'un d'entre eux est différent, les trajets doivent nécessairement être différents.

Nous pouvons donc formuler la requête de manière similaire aux précédentes, en parcourant tous les uplets de Voyage et pour chacun d'eux, en vérifiant s'il existe un trajet dont les villes de départ et d'arrivée sont les mêmes que les villes d'arrivée et de départ du trajet en cours de vérification. Ainsi, pour chaque trajet de Voyage, nous construisons une sous-requête corrélée où nous parcourons à nouveau tous les uplets de Voyage et n'obtenons que les valeurs des attributs DepartureCityFK et ArrivalCityFK. Ensuite, nous vérifions si les valeurs de ces attributs du trajet dans la requête de "niveau supérieur" se trouvent dans l'ensemble d'uplets que nous venons de construire.

Mais dans ce cas, si nous regardons le code, l'ordre des attributs est inversé par rapport à l'ordre de ces mêmes attributs dans la sous-requête. Ce que nous voulons réellement vérifier, c'est que la valeur de l'attribut DepartureCityFK de l'uplet que nous vérifions dans la requête correspond à la valeur de l'attribut ArrivalCityFK d'un uplet de la sous-requête. De plus, nous devons vérifier que la valeur de l'attribut ArrivalCityFK de l'uplet de la requête correspond à la valeur de l'attribut DepartureCityFK du même uplet qui correspondait à la paire d'attributs précédente.

Nous pouvons comprendre cela plus facilement en considérant la paire **(V.DepartureCityFK, V.ArrivalCityFK)** comme s'il s'agissait des villes de départ et d'arrivée, A et B, d'un trajet. Ce que nous voulons vérifier, c'est s'il existe un uplet dans la sous-requête qui a B et A comme villes de départ et d'arrivée, respectivement.

Le moyen le plus simple d'effectuer cette vérification est soit d'inverser l'ordre des attributs dans l'uplet **(V.DepartureCityFK, V.ArrivalCityFK)**, soit dans les attributs du SELECT de la sous-requête. C'est ce que nous avons décidé de faire ici, c'est pourquoi ArrivalCityFK est renvoyé avant DepartureCityFK.

Enfin, pour vérifier plus facilement l'existence de ces trajets de retour, nous pouvons ajouter la clause ORDER BY, qui trie par plusieurs attributs au lieu d'un seul. C'est-à-dire que nous utilisons les attributs **(V.DepartureCityFK, V.ArrivalCityFK)** comme critères de tri. SQL trie par paires de valeurs pour chaque uplet, comme si chaque paire de valeurs possible était considérée comme une valeur unique pouvant être comparée à d'autres.

En faisant cela, nous pouvons facilement nous concentrer sur la ville de départ d'un trajet, puis chercher un autre trajet dont la ville d'arrivée a la même valeur. Ensuite, nous pouvons en trouver un dont la ville de départ correspond à la ville d'arrivée du trajet d'origine, trouvant ainsi une paire de trajets qui forment un trajet de retour vers une ville.

Enfin, examinons une autre requête où nous devons comparer les valeurs de plusieurs attributs à la fois. Ici, tous les trajets sont listés dont la croisière associée (celle effectuant le trajet) a été affectée à sa ligne de croisière à la même date de début du trajet.

```pgsql
SELECT V.*
FROM Voyage V
WHERE (V.ShipFK, V.DepartureDate)
  IN (
    SELECT SA.ShipFK, SA.StartDate
    FROM ShipAssignment SA
  );
```

Pour implémenter cela, nous devons prendre en compte tous les attributs que possède **Voyage**, y compris les informations contenues dans les clés étrangères, afin d'éviter d'avoir à effectuer des opérations inutiles comme un JOIN avec la table **CruiseShip** ou **CruiseLine**.

Dans ce cas, nous structurons la requête de manière similaire, en parcourant d'abord tous les uplets de Voyage et en vérifiant si la croisière a été affectée à sa ligne de croisière à la même date que le début du trajet.

Pour faciliter cette vérification, nous construisons une sous-requête qui renvoie toutes les valeurs des attributs **ShipFK** et **StartDate** de la table **ShipAssignment**. De cette façon, plus tard dans notre requête, nous pourrons vérifier si la croisière effectuant le trajet (qui est référencée avec la clé étrangère ShipFK de Voyage) a été affectée à la DepartureDate de l'uplet Voyage (date de début du trajet) à n'importe quelle ligne de croisière.

Comme vous pouvez le voir, nous pouvons simplifier la requête si nous pensons à obtenir tous les trajets d'un navire de croisière qui a été affecté à une date de début avec n'importe quelle ligne de croisière. En d'autres termes, il ne doit pas s'agir d'une ligne spécifique, mais de n'importe quelle ligne à laquelle il a été affecté à la date indiquée par **DepartureDate** de **Voyage**. Ainsi, dans la clause WHERE, il vérifie si la paire de valeurs prises par les attributs **(V.ShipFK, V.DepartureDate)** se trouve dans la sous-requête. Et cette fois, il maintient l'ordre correct des attributs, puisque ShipFK de Voyage doit correspondre à ShipFK de ShipAssignment, et **DepartureDate** de **Voyage** doit correspondre à StartDate de ShipAssignment, respectivement.

D'une part, la correspondance de ShipFK garantit que le navire de croisière effectuant le trajet est le même que celui affecté dans l'uplet ShipAssignment. De même, la correspondance des attributs de date garantit que cette affectation a été faite à la date de début du trajet.

Nous avons également résolu cette requête à l'aide d'une sous-requête corrélée et de l'opérateur IN, bien que ce ne soit pas le seul moyen. Comme vous pouvez le deviner, il y a toujours la possibilité d'utiliser des opérations JOIN et des conditions pour filtrer les uplets, ce qui peut être plus ou moins efficace dans certains cas. C'est pourquoi il est important de comprendre ce que SQL fait sous le capot, comme s'il construit et stocke réellement tous les uplets d'une sous-requête ou d'un produit cartésien en mémoire, et quand il le fait.

### Expressions de table communes (CTE)

Nous avons vu que les sous-requêtes nous permettent d'utiliser le résultat d'une requête à l'intérieur d'une autre requête. Nous pouvons construire cela une seule fois pendant l'exécution de l'intégralité de la requête si elle n'est pas corrélée, ou une fois pour chaque uplet de la table avec laquelle elle est corrélée. En d'autres termes, nous pouvons voir une sous-requête comme un ensemble d'uplets avec lesquels nous opérons dans une requête.

Mais nous n'avons pas toujours besoin que les requêtes soient corrélées. Nous avons vu que certaines requêtes peuvent être résolues par des requêtes non corrélées, c'est-à-dire des ensembles d'uplets qui ne sont construits qu'une seule fois et qui suffisent à résoudre l'intégralité de la requête dans laquelle ils sont contenus.

Dans ces situations, pour simplifier la notation, nous pouvons utiliser un outil appelé **CTE (Common Table Expression)** en SQL. Celles-ci utilisent généralement la [**clause WITH**](https://www.geeksforgeeks.org/sql-with-clause/). Grâce à cela, nous pouvons définir et stocker le résultat d'une sous-requête dans une table temporaire qui a besoin d'un alias. Ainsi, au lieu d'utiliser une sous-requête dans la construction d'une requête, nous définissons une [**table intermédiaire temporaire**](https://stackoverflow.com/questions/49990666/trying-to-create-multiple-temporary-tables-in-a-single-query) **(Common Table Expression)** qui n'existe que pendant l'exécution de la requête et contient tous les uplets générés par une certaine sous-requête. Encore une fois, nous devons utiliser un alias pour la désigner, tout comme nous devons fournir aux tables un nom et un schéma lorsque nous les créons dans le DDL.

Pour comprendre la clause WITH avec un exemple, nous pouvons considérer la requête qui obtient des informations sur tous les navires de croisière actuellement actifs. Ici, actif signifie affecté à une ligne de croisière à la date actuelle à laquelle la requête est exécutée.

Avant d'écrire le code, il est utile de réfléchir à la manière dont la requête sera structurée, c'est-à-dire d'où nous obtiendrons les données pour répondre, comment nous devrions combiner les différentes tables avec ces données, quelles conditions ou opérations doivent être appliquées à celles-ci ou aux uplets résultant des opérations effectuées, etc.

```pgsql
WITH ActiveShips AS (
    SELECT ShipFK
    FROM ShipAssignment
    WHERE StartDate <= CURRENT_DATE
        AND EndDate >= CURRENT_DATE
)
SELECT CS.ShipID, CS.Speed, CS.PassengerCapacity
FROM ActiveShips A INNER JOIN CruiseShip CS ON CS.ShipID = A.ShipFK;
```

Dans ce cas, les informations pour toutes les affectations de croisière, qu'elles soient actuelles ou non, se trouvent dans la table ShipAssignment. Ainsi, pour savoir quelles croisières sont actuellement affectées à une ligne de croisière, nous pouvons profiter du fait que cette table possède une **clé étrangère ShipFK** qui identifie la croisière affectée dans chaque uplet de **ShipAssignment**.

Ainsi, si nous fixons la condition que la StartDate de l'affectation doit être antérieure à la date actuelle obtenue à partir de **CURRENT\_DATE**, et que la EndDate est postérieure à la date actuelle, nous obtiendrons toutes les affectations qui sont valides à la date actuelle. En extrayant les valeurs prises par la clé étrangère ShipFK pour ces affectations, nous pouvons identifier les croisières qui sont actuellement affectées.

Mais la requête ne nous demande pas seulement de **les identifier** – mais aussi d'obtenir **des informations à leur sujet** stockées dans CruiseShip. Ainsi, nous enregistrons les identifiants des croisières que nous avons obtenues précédemment dans une table temporaire à utiliser dans la requête. En d'autres termes, nous pourrions faire en sorte que les conditions sur StartDate et EndDate s'appliquent à ShipAssignment dans une sous-requête. Mais pour simplifier la notation et démontrer comment utiliser les **CTE**, nous utiliserons la clause WITH où nous définissons tout le code de la sous-requête et attribuons un alias à cette table temporaire (voir le code ci-dessus).

Plus précisément, en faisant cela, nous enregistrerons les identifiants des croisières actuellement actives dans la table temporaire nommée ActiveShips. C'est l'alias que nous avons attribué à l'aide de l'opérateur AS – mais il fonctionne à l'envers dans la clause WITH : d'abord, vous écrivez le nom de l'alias, puis vous écrivez le code qui récupère les données de la table intermédiaire (l'élément auquel le nom de l'alias est attribué).

Ainsi, lorsque nous utilisons l'instruction WITH, nous voyons que nous avons construit une table ActiveShips avec le résultat de ce qui pourrait être une **sous-requête non corrélée** – mais par souci de simplicité, nous l'avons refactorisée de sorte que son résultat soit stocké dans une table intermédiaire avec un certain alias.

Désormais, nous pouvons traiter ActiveShips comme s'il s'agissait d'une autre table de la base de données, en effectuant un JOIN entre elle et CruiseShip pour obtenir toutes les informations sur les croisières actives. Nous imposons une condition d'égalité sur les attributs **ShipFK** et **ShipID** des tables **ActiveShips** et **CruiseShip**, respectivement. Cela signifie que nous ne conservons que les uplets du produit cartésien où la clé étrangère ShipFK se réfère à l'identifiant ShipID de ce même uplet. Cela nous permet de trouver les informations complètes sur une croisière spécifique.

Dans la requête précédente, nous aurions pu facilement nous passer de WITH et faire d'ActiveShips une sous-requête à laquelle nous aurions également pu attribuer un alias. Mais lors de l'utilisation d'une sous-requête, même si nous lui attribuons un alias, nous ne pouvons pas l'utiliser dans n'importe quelle partie de la requête. C'est-à-dire que si nous avons une sous-requête dans un FROM ou un SELECT, nous ne pouvons pas l'utiliser dans d'autres parties de la requête de la même manière que nous pouvons utiliser une table intermédiaire définie dans un WITH. Celle-ci (WITH), nous pouvons la référencer à n'importe quel point de la requête, qu'elle soit formée ou non par d'autres sous-requêtes.

```pgsql
WITH VoyageDistance AS (
  SELECT * 
  FROM Voyage
  WHERE Distance > 1000
)
SELECT DepartureDate, ArrivalDate, Distance
FROM VoyageDistance 
WHERE DepartureDate BETWEEN '2025-01-01' AND '2025-06-30';
```

Nous avons un autre exemple similaire dans la requête ci-dessus. Ici, nous considérons une requête qui obtient des informations sur tous les voyages qui ont commencé au cours du premier semestre 2025 (environ) et qui ont une distance supérieure à 1000 kilomètres. L'approche dans ce cas est plus simple puisque toutes les informations dont nous avons besoin se trouvent dans la table **Voyage**. Ainsi, la condition selon laquelle la distance est supérieure à 1000 kilomètres est facilement modélisée avec une clause **WHERE** et l'expression **Distance > 1000**.

Tout comme auparavant, dans cette requête, nous pourrions également nous passer de WITH et inclure à la fois la distance et la condition sur la date de début du voyage dans un seul WHERE. Mais souvent, nous pourrions avoir besoin de modifier ou d'étendre une requête – par exemple, à l'avenir, on pourrait nous demander une requête basée sur celle-ci, mais avec plus ou moins de conditions. Ainsi, si nous effectuions une **analyse** de notre domaine, des exigences des utilisateurs et du code de la requête, nous pourrions conclure que les uplets avec des voyages de plus de 1000 kilomètres pourraient être nécessaires dans plusieurs parties de la même requête.

Dans cet exemple, ce phénomène pourrait ne pas se produire, mais il illustre que dans une situation réelle, nous pouvons avoir besoin de prendre en compte divers facteurs qui affectent la conception de la requête.

Ainsi, supposons que nous supposions que les uplets Voyage avec **Distance > 1000** pourraient potentiellement être utilisés plusieurs fois dans une seule requête à travers plusieurs instructions (dans les futures modifications de cette requête). Alors l'option la plus maintenable est d'utiliser une clause WITH où nous stockons temporairement ces uplets, puis nous les utilisons dans la requête via l'alias de cette table intermédiaire (comme s'il s'agissait d'une table de base de données régulière). Ensuite, nous pouvons ajouter une autre clause WHERE à la toute fin de la requête, déclarant la condition que la date de début du voyage se situe dans la première moitié de 2025. Nous pouvons modéliser cela avec l'opérateur **BETWEEN**, la fonction **EXTRACT()**, ou de nombreuses autres manières.

Enfin, il convient de noter que l'utilisation de la clause WITH sans raison claire n'est pas considérée comme une bonne pratique. (Des exemples d'une telle raison claire pourraient inclure une décision de conception basée sur les exigences de l'utilisateur ou une analyse approfondie de la requête qui conclut qu'il pourrait être utile d'avoir une table intermédiaire comme VoyageDistance à l'avenir).

C'est principalement parce que, dans des situations comme celle-ci, une clause WHERE est utilisée à la fois dans la construction de la table intermédiaire et dans la table résultante de la requête. Cela signifie que plusieurs filtres pourraient être appliqués en interne, ce qui peut être inefficace.

Mais le SGBD applique souvent automatiquement certaines techniques comme l'[**inlining**](https://dba.stackexchange.com/questions/212198/how-can-i-find-out-if-a-sql-function-can-be-inlined) pour optimiser l'exécution de la requête via des **refactorisations** du **plan d'exécution**. En d'autres termes, même si notre code n'est pas le plus optimal, le SGBD peut automatiquement trouver un moyen équivalent et plus optimal de résoudre la requête.

Pour illustrer que les tables intermédiaires que nous définissons dans la clause WITH peuvent être construites avec des sous-requêtes aussi "complexes" que nous le souhaitons, considérez cette requête :

```pgsql
WITH Pending AS (
    SELECT D.*
    FROM DrivingLicenseRequest D
        LEFT JOIN DrivingLicense A USING (LicenseID)
        LEFT JOIN RejectedDrivingLicense R USING (LicenseID)
    WHERE A.LicenseID IS NULL
        AND R.LicenseID IS NULL
)
SELECT P.Name, Pending.*
FROM Pending INNER JOIN Person P ON P.PersonID = Pending.PersonFK;
```

Nous obtenons des informations sur toutes les demandes de permis de conduire en cours de traitement, c'est-à-dire celles qui n'ont pas encore été acceptées ou rejetées. Nous incluons également des informations sur la personne qui a effectué chaque demande.

Dans ce cas, le point clé est de réaliser que les demandes en cours sont représentées par des uplets dans DrivingLicenseRequest qui ne sont référencés par aucun uplet dans DrivingLicense ou **RejectedDrivingLicense** (puisqu'ils ne sont pas encore acceptés ou rejetés).

Dans ce cas, nous pouvons utiliser LEFT JOIN de sorte qu'en combinant toutes ces tables avec des opérations LEFT JOIN, nous puissions rassembler des informations complètes sur les demandes. Cela signifie construire une table formée par tous les attributs des trois tables de la hiérarchie, où certains d'entre eux seront NULL ou non dans chaque uplet, selon qu'ils représentent des demandes acceptées, rejetées ou en attente.

Plus précisément, puisque les clés étrangères des entités héritières de la hiérarchie sont toutes deux appelées LicenseID (correspondant à l'identifiant **{LicenseID}** de la super-classe), les **LEFT OUTER JOINs** sont effectués en appliquant une condition d'égalité sur cet attribut. Cela garantit que les uplets que nous obtenons contiennent des informations sur la même demande, plutôt que plusieurs demandes dans le même uplet du produit cartésien.

Nous utilisons LEFT JOIN car la première table que nous combinons est **DrivingLicenseRequest**. Nous savons que tous ses uplets sont non nuls car elle représente la super-classe de la hiérarchie et contient des informations sur toutes les demandes de la base de données, quel que soit leur statut. Ainsi, en plaçant cette table à gauche de l'opération JOIN, nous nous assurons que les informations de tous les uplets qu'elle contient apparaissent – et elle remplit de NULL les attributs de l'autre table, DrivingLicense.

Ensuite, nous effectuons un autre LEFT JOIN avec RejectedDrivingLicense en suivant le même processus. Cela donne une table où, malgré l'utilisation de USING dans les opérations JOIN, nous pouvons imposer des conditions sur les attributs LicenseID de toutes les tables. Ainsi, pour qu'un uplet du produit cartésien résultant représente une demande en attente, les attributs LicenseID des tables **DrivingLicense** et RejectedDrivingLicense doivent être NULL. Cela indique qu'il n'y a pas d'uplets dans les tables respectives car le LEFT JOIN a été rempli de NULL s'ils n'existaient pas. Nous déclarons cette condition à l'aide d'une clause WHERE et de l'opérateur IS, car vous ne pouvez pas comparer un attribut avec NULL directement à l'aide de l'opérateur =.

À ce stade, pour simplifier la syntaxe de la requête et éviter de chaîner trop de JOIN, nous pouvons créer une table intermédiaire avec le résultat que nous avons obtenu en effectuant ces LEFT JOIN et en appliquant la condition précédente. De cette façon, nous pourrons plus tard effectuer un INNER JOIN dans la requête pour obtenir les informations de la personne qui a effectué la demande. Nous faisons tout cela via l'attribut **PersonID** de la table **Person** et la **clé étrangère PersonFK** de la table intermédiaire Pending, qui provient de la table DrivingLicenseRequest et se réfère à la personne associée à la demande.

Dans cette requête, nous pourrions également envisager de combiner toutes les jointures dans une seule clause FROM et de nous passer du WITH. Ce serait correct, mais cela compliquerait le code en ayant tous les JOIN chaînés. Et, bien que cette stratégie puisse être plus efficace dans certaines circonstances, nous devrions rechercher un équilibre entre la lisibilité du code et l'efficacité.

Pour illustrer que les tables intermédiaires de la clause WITH peuvent être définies par des requêtes contenant des sous-requêtes, nous allons considérer la même requête que précédemment et essayer de la résoudre en utilisant une approche différente.

```pgsql
WITH Pending AS (
    SELECT D.*
    FROM DrivingLicenseRequest D
    WHERE NOT EXISTS (
            SELECT *
            FROM DrivingLicense A
            WHERE A.LicenseID = D.LicenseID
        )
        AND NOT EXISTS (
            SELECT *
            FROM RejectedDrivingLicense R
            WHERE R.LicenseID = D.LicenseID
        )
)
SELECT P.Name, Pending.*
FROM Pending INNER JOIN Person P ON P.PersonID = Pending.PersonFK;
```

Pour obtenir les demandes en attente, conservez les uplets de DrivingLicenseRequest dont la clé primaire {**LicenseID**} n'est pas référencée (via la clé étrangère **LicenseID**) par un uplet de DrivingLicense ou RejectedDrivingLicense.

L'option la plus simple pour implémenter cela consiste à parcourir tous les uplets de DrivingLicenseRequest à l'aide de la clause FROM, et pour chacun d'eux, à construire deux requêtes corrélées très similaires.

* Nous pouvons en avoir une qui récupère tous les uplets de DrivingLicense dont la clé étrangère LicenseID se réfère à la clé primaire LicenseID de l'uplet de DrivingLicenseRequest que nous parcourons, et
* Nous pouvons avoir une autre sous-requête qui fait la même chose mais récupère les uplets de la table RejectedDrivingLicense.

De cette façon, nous pourrons plus tard vérifier si l'une des tables renvoyées par les sous-requêtes contient des uplets ou non à l'aide de l'opérateur EXISTS.

Si l'une des sous-requêtes renvoie des uplets, alors la demande est soit acceptée, soit rejetée. Mais si les deux sous-requêtes renvoient un ensemble vide, cela signifie que pour une certaine demande dans DrivingLicenseRequest\*\*,\*\* il n'y a aucun uplet dans les tables respectives DrivingLicense ou RejectedDrivingLicense qui la référence. Cela indique alors que la demande est en cours de traitement.

Grâce à ce processus, nous obtenons les demandes en attente, que nous stockons dans une table intermédiaire à l'aide de la clause WITH. Pour combiner les informations de la personne qui a effectué chaque demande, nous utilisons la table intermédiaire dans la requête, spécifiquement dans une opération INNER JOIN avec la table Person, tout comme nous l'avons fait auparavant.

Ainsi, avec cet exemple, nous avons vu qu'il existe plusieurs constructions SQL qui mènent au même résultat – ce qui signifie qu'une requête ne doit pas nécessairement être résolue d'une seule manière.

De plus, en utilisant la clause WITH, nous pouvons définir chaque table intermédiaire avec un code SQL aussi **"complexe"** que nécessaire. Nous pouvons inclure des sous-requêtes, des conditions et généralement n'importe quelle instruction SQL, à l'exception d'un WITH, qui par défaut ne peut pas apparaître à l'intérieur d'un autre WITH.

Si nous devons utiliser une table intermédiaire pour résoudre une requête définie comme une **CTE**, nous devons la définir au même niveau que les autres tables intermédiaires de notre requête, c'est-à-dire dans une seule instruction WITH (comme nous le verrons ci-dessous).

Jusqu'à présent, nous avons vu que nous pouvons utiliser l'instruction WITH pour définir une table intermédiaire que nous utilisons pour résoudre la requête plus confortablement et plus facilement dans certaines situations. Mais, nous pourrions avoir besoin de plusieurs tables intermédiaires pour résoudre une requête, pas seulement une.

Par exemple, dans le code ci-dessous, nous avons une requête qui obtient des informations sur les personnes ayant vécu dans au moins deux villes. Nous avons résolu cette requête dans la section **“Filtrage d'uplets”** à l'aide d'opérations JOIN – mais nous pouvons également suivre une approche similaire où nous créons d'abord plusieurs tables intermédiaires différentes et résolvons finalement la requête sur la base des résultats de ces tables intermédiaires.

```pgsql
WITH R1 AS (
    SELECT PersonFK, CityFK AS CityA
    FROM Residence
),
R2 AS (
    SELECT PersonFK, CityFK AS CityB
    FROM Residence
),
CityPairs AS (
    SELECT DISTINCT R1.PersonFK
    FROM R1 INNER JOIN R2 ON (R1.PersonFK = R2.PersonFK
        AND R1.CityA <> R2.CityB)
)
SELECT P.*
FROM CityPairs MC INNER JOIN Person P ON MC.PersonFK = P.PersonID
ORDER BY P.personID;
```

Tout d'abord, nous pouvons créer plusieurs tables intermédiaires qui contiennent tous les uplets de Residence – spécifiquement les informations sur la personne et la ville qui constituent chaque résidence. Nous pouvons le faire en obtenant les attributs PersonFK et CityFK, qui sont des clés étrangères se référant à la personne ayant vécu dans une certaine ville pendant cette résidence. En construisant plusieurs tables intermédiaires avec ces informations, nous pouvons renommer CityFK avec un alias comme CityA dans l'une d'elles et CityB dans l'autre table intermédiaire, de sorte que plus tard le JOIN entre elles ait une syntaxe plus claire.

Pour construire plusieurs tables intermédiaires dans une seule instruction WITH, nous pouvons les chaîner avec des virgules. Au lieu d'utiliser le mot-clé WITH plusieurs fois, nous devons l'utiliser une seule fois et chaîner toutes les tables intermédiaires que nous voulons avec des virgules, comme illustré ci-dessus.

Par la suite, avec les tables intermédiaires R1 et R2 contenant ces informations, nous pouvons créer une autre table intermédiaire où nous obtenons les identifiants de toutes les personnes ayant eu une résidence dans plusieurs villes différentes (ou dans au moins deux villes).

Pour ce faire, nous pouvons effectuer un INNER JOIN entre R1 et R2 (un produit cartésien de leurs uplets) et conserver les uplets du produit cartésien où les valeurs de clé étrangère PersonFK correspondent et les valeurs CityFK ne correspondent pas. De cette façon, nous conservons les uplets du produit cartésien qui représentent des informations sur plusieurs résidences de la même personne dans des villes différentes.

Ces identifiants sont destinés aux personnes dont nous devons obtenir les informations à partir de la table Person. Nous pouvons donc enfin effectuer un INNER JOIN entre la table intermédiaire CityPairs et Person, de sorte que le résultat final de la requête soit les informations des personnes ayant eu au moins deux résidences dans des villes différentes. (Elles ne seraient pas apparues dans un uplet du produit cartésien entre R1 et R2 autrement.)

Le point important concernant cette requête est de noter que nous avons utilisé **plusieurs tables intermédiaires** dans la même clause WITH pour la résoudre – et c'est tout à fait **possible** mais pas toujours recommandé. Nous pouvons résoudre cette requête de diverses manières, chacune ayant ses propres avantages ou inconvénients selon les caractéristiques que nous voulons que le code possède, telles que la clarté, l'efficacité, la maintenabilité, etc.

Pour conclure cette section CTE, considérons une autre requête où nous devons obtenir des informations sur les trajets de bus ayant eu lieu après 2025 et où le bus dispose du WiFi. Le moyen le plus simple de créer cette requête consisterait à rassembler les informations des tables CityBus et BusTrip à l'aide d'un JOIN, puis à appliquer des conditions sur les uplets du produit cartésien correspondant. Mais pour illustrer l'utilisation de plusieurs **tables intermédiaires (CTE)** dans une seule clause **WITH**, dans ce cas, nous diviserons la résolution de la requête en plusieurs parties.

```pgsql
WITH WifiBuses AS (
    SELECT Plate, RouteNumber
    FROM CityBus
    WHERE FreeWifi = TRUE
),
AvailableTrips AS (
    SELECT TripDate, StartAddress, EndAddress, PlateFK
    FROM BusTrip
    WHERE EXTRACT(YEAR FROM TripDate) >= 2025 
)
SELECT T.TripDate, T.StartAddress, T.EndAddress, B.RouteNumber
FROM AvailableTrips T INNER JOIN WifiBuses B ON B.Plate = T.PlateFK;
```

Tout d'abord, nous obtiendrons des informations sur les bus avec WiFi dans une table intermédiaire. Pour construire cette table, nous appliquons simplement la condition FreeWifi=TRUE sur les uplets de la table CityBus. Dans ce cas, lorsque nous faisons un **SELECT * FROM CityBus;** nous pouvons voir que dans l'attribut FreeWifi, les valeurs booléennes sont représentées par les lettres **‘t’** ou **‘f’** – nous pourrions donc penser que dans la requête nous devrions comparer l'attribut avec **‘t’**.

Mais les valeurs booléennes en SQL sont TRUE et FALSE, même si le SGBD les [**représente**](https://dba.stackexchange.com/questions/115234/why-t-and-f-instead-of-true-and-false) avec un autre type de notation. Ainsi, la bonne façon de vérifier si l'attribut contient la valeur logique **true** est de le comparer avec **TRUE**. Même si la représentation de la valeur booléenne peut changer, en SQL nous devrions toujours opérer avec des valeurs booléennes en utilisant les littéraux **TRUE** et **FALSE**.

Deuxièmement, nous construisons une autre table intermédiaire avec des informations sur les trajets de bus ayant eu lieu en 2025 ou après. Nous le faisons en récupérant tous les uplets de BusTrip et en les filtrant à l'aide de la fonction **EXTRACT()** et de la caractéristique **YEAR** de la date.

Enfin, dans la requête, nous effectuons un JOIN entre les deux tables intermédiaires pour rassembler toutes les informations sur les trajets et les bus. De cette façon, nous obtenons des uplets avec des trajets ayant eu lieu à des dates égales ou postérieures à l'année 2025, ainsi que les informations sur le bus avec WiFi ayant effectué ce trajet.

Mais dans ce cas, nous ne renvoyons que le numéro de ligne du bus à l'utilisateur, qui fait également partie des informations de la table CityBus. Si cela ne suffit pas à identifier le bus, nous pourrions également renvoyer sa plaque d'immatriculation dans le SELECT, par exemple. Cette décision dépend de ce dont l'utilisateur final a besoin.

De plus, avec cette requête, nous pouvons voir plus clairement l'effet du codage d'une requête utilisant plusieurs tables intermédiaires sur l'efficacité de son exécution. Par exemple, si nous codions la requête sans WITH (et à la place avec des opérations JOIN entre les tables CityBus et BusTrip respectives et imposions des conditions sur les uplets résultants), nous devons considérer que l'intégralité du produit cartésien serait effectuée en premier puis filtrée par les conditions.

Mais en utilisant des tables intermédiaires où chacune impose une certaine condition sur les uplets de chaque table, nous pouvons réduire le nombre d'uplets dans chaque table intermédiaire, puisque **WifiBuses** ne contiendra pas tous les bus existants, mais seulement ceux avec WiFi (qui seront moins nombreux).

En appliquant cette technique (connue sous le nom d'[early filtering](https://docs.oracle.com/cloud/latest/big-data-discovery-cloud/BDDEQ/ceql_bp_filter_early.htm#BDDEQ-concept_F3B83B6965AC40429E5C68AB330BA74E) ou filtrage précoce), nous nous assurons que lors de l'exécution du JOIN final entre les tables intermédiaires, le produit cartésien donne **moins d'uplets** – ce qui signifie qu'il travaille avec des tables plus petites et est donc **plus efficace**.

Gardez simplement à l'esprit que dans les SGBD modernes, cette optimisation peut être effectuée [automatiquement](https://stackoverflow.com/questions/46727600/sql-performance-filter-first-or-join-first) même sans utiliser de tables intermédiaires, selon la nature de la requête. Ainsi, si cela ne dégrade pas significativement la clarté de la requête, nous devrions filtrer les informations des tables à combiner via un JOIN le plus tôt possible, c'est pourquoi nous avons utilisé plusieurs tables intermédiaires dans une clause WITH.

### Opérations sur les ensembles

Nous avons vu que dans la plupart des requêtes, nous devons imposer des conditions sur les uplets de table pour les filtrer et ne conserver que ceux qui nous intéressent. Parfois, nous devons même utiliser des opérateurs logiques pour chaîner plusieurs conditions ensemble.

Mais l'utilisation des opérateurs logiques AND, OR et NOT n'est pas le seul moyen de chaîner plusieurs conditions. Nous pouvons également adopter une approche différente où, au lieu d'appliquer un filtre sur tous les uplets, nous divisons les conditions qui doivent être remplies et appliquons plusieurs filtres, un pour chaque condition basée sur des opérateurs logiques. Enfin, nous obtenons les uplets résultant de ces filtres et les combinons à l'aide d'**opérateurs de la théorie des ensembles**, qui remplissent des fonctions équivalentes aux **opérateurs logiques**.

En d'autres termes, en SQL, nous pouvons chaîner plusieurs conditions dans une clause WHERE, par exemple, à l'aide d'opérateurs logiques. Ou nous pouvons utiliser des opérateurs de la théorie des ensembles pour combiner les uplets résultant de plusieurs filtres, chacun appliquant l'une de ces conditions, le tout sans utiliser d'opérateurs logiques.

Comme nous le verrons ci-dessous, la décision d'utiliser des opérateurs logiques ou d'ensemble dépend largement de la clarté du code résultant et de l'efficacité que nous voulons atteindre dans la requête.

Pour commencer, considérons une requête où nous devons obtenir des informations sur toutes les piscines qui sont actuellement en maintenance ou fermées. Si nous voulions le faire avec ce que nous savons déjà, le moyen le plus simple consisterait à utiliser un filtre avec une clause WHERE, en combinant les conditions selon lesquelles l'attribut Status est 'closed' ou 'maintenance' à l'aide de l'opérateur logique OR.

```pgsql
SELECT *
FROM Pool
WHERE Status='maintenance'
UNION
SELECT *
FROM Pool
WHERE Status='closed';
```

Outre l'utilisation de cet opérateur, nous pouvons repenser la requête pour la résoudre à l'aide d'opérateurs de la théorie des ensembles. Dans ce cas, en utilisant un seul opérateur logique OR, nous divisons la condition WHERE en plusieurs conditions en supprimant cet opérateur OR. Cela donne les conditions **Status='maintenance'** et **Status='closed'**, respectivement.

En faisant cela, nous pouvons résoudre deux requêtes : une appliquant la première condition et une autre appliquant la seconde. Cela nous donne deux tables résultantes, l'une avec des informations sur les piscines en maintenance et une autre table avec toutes les piscines fermées.

Mais nous les voulions toutes dans une seule table de sortie, pas dans plusieurs. Ainsi, pour combiner tous les uplets des deux tables en une seule (afin qu'ils apparaissent tous dans la table résultante), nous utilisons l'opérateur UNION entre les deux requêtes. Il traite les deux requêtes comme s'il s'agissait de **multiensembles** d'uplets, ce qui donne une autre **ensemble** d'uplets finaux où les uplets des deux tables sont présents. C'est-à-dire tous les uplets des deux tables. C'est exactement comme dans la théorie des ensembles où l'union des ensembles **AUB** donne un autre ensemble contenant tous les individus de A, tous ceux de B, et tous ceux présents à la fois dans A et B.

Pour appliquer un opérateur de la théorie des ensembles, le schéma des tables renvoyées par les requêtes avec lesquelles nous opérons doit être exactement le même. Cela signifie qu'elles doivent avoir le même nombre d'attributs avec les mêmes noms et types de données, et dans le même ordre. Sinon, nous ne pouvons pas comparer les uplets des deux tables, et il ne serait pas possible de déterminer si un uplet appartient à l'un des ensembles impliqués dans l'opération.

Lorsque nous exécutons une requête qui inclut un UNION, nous pouvons voir que s'il y a des uplets en double dans les tables résultantes des requêtes avec lesquelles nous travaillons, ces uplets en double disparaissent dans la table résultante de la requête. Cela se produit parce que, par défaut, tous les opérateurs de la théorie des ensembles en SQL prennent des multiensembles avec des uplets en entrée et produisent un ensemble d'uplets, ce qui signifie qu'il ne contiendra pas d'uplets en double. Ainsi, si nous voulons forcer l'apparition d'uplets en double parce que la requête l'exige, nous devons ajouter le modificateur **ALL** après l'opérateur **UNION**, **INTERSECT** ou **EXCEPT** correspondant.

Par exemple, dans ce cas, nous voulons obtenir des informations sur toutes les personnes qui ont loué au moins un vélo **ou** possédé au moins une voiture dans notre système :

```pgsql
SELECT PersonFK
FROM Rental
UNION ALL 
SELECT PersonFK
FROM CarOwnership;
```

Pour ce faire, nous construisons d'abord une requête qui récupère tous les identifiants PersonID des personnes référencées par les uplets de la table Rental via leur clé étrangère PersonFK. En d'autres termes, chaque uplet de Rental possède une valeur dans sa clé étrangère PersonFK qui correspond à l'identifiant d'une certaine personne, lequel correspond à la valeur de son identifiant unique PersonID. Ainsi, la sélection de l'attribut PersonFK suffit pour obtenir les identifiants de toutes les personnes ayant au moins un enregistrement dans cette table.

Nous faisons de même avec une autre requête sur la table CarOwnership, qui possède également une clé étrangère PersonFK présentant les mêmes caractéristiques.

Enfin, en examinant ces résultats partiels des requêtes, nous verrons que certaines personnes ont pu louer plusieurs vélos ou simplement effectuer plusieurs locations, et elles peuvent également avoir plusieurs enregistrements de propriété dans CarOwnership, ce qui entraîne des uplets en double. Ainsi, lors de la construction de la table résultante finale, nous devons obtenir les personnes qui sont présentes dans une table ou dans l'autre. Cela signifie que nous devons combiner les deux tables avec l'opérateur UNION pour obtenir un ensemble final avec tous les uplets des deux tables.

Dans ce cas précis, nous ne devrions pas ajouter le **modificateur ALL**, car nous voulons simplement savoir quelles personnes remplissent la condition d'avoir au moins une location et au moins une propriété de voiture (une personne ayant effectué plusieurs locations n'a donc pas besoin d'apparaître plusieurs fois dans la table finale).

Mais si nous voulions conserver les uplets en double, cet exemple montre clairement qu'en ajoutant ALL après l'opérateur UNION, tous les uplets en double des deux tables sont préservés, ce qui fait que la table finale affiche autant d'uplets avec les mêmes informations de personne que le nombre de locations et de propriétés qu'elles ont eues. En d'autres termes, le modificateur ALL force UNION à renvoyer un **multiensemble**, et non un **ensemble** qui supprime les **uplets en double**.

Nous pouvons voir l'effet du modificateur ALL d'un coup d'œil en examinant la table résultante de la requête. Mais si nous travaillons avec une requête très volumineuse ou une base de données contenant beaucoup d'informations, nous pourrions vouloir **envelopper** notre requête dans une autre requête externe qui utilise la fonction d'agrégation **COUNT()** pour compter le nombre d'uplets qu'elle renvoie.

Par exemple, dans le code ci-dessous, vous pouvez voir que nous avons utilisé la requête que nous venons d'examiner comme sous-requête dans la clause FROM, de sorte que nous obtenons tous les uplets qu'elle contient. Ensuite, dans le SELECT, nous utilisons la fonction COUNT(\*) pour compter le nombre d'uplets.

```pgsql
SELECT COUNT(*)
FROM (
        SELECT PersonFK
        FROM Rental
        UNION
        SELECT PersonFK
        FROM CarOwnership
    ) AS PersonTable;
```

Il est également important ici de fournir un **alias** à la **sous-requête**, car lorsque des sous-requêtes apparaissent dans la clause FROM, le SGBD a besoin qu'elles aient des alias pour les distinguer et éviter les ambiguïtés quant à l'origine des attributs qui sont ensuite sélectionnés ou utilisés dans d'autres clauses.

En continuant avec les différents opérateurs de la théorie des ensembles que propose SQL, nous avons **INTERSECT**, qui combine les résultats de plusieurs tables pour renvoyer un ensemble avec tous les uplets qui apparaissent dans **toutes les tables simultanément**. Pour comprendre cela, nous avons la requête ci-dessous qui récupère des informations sur toutes les personnes qui possèdent un permis de conduire et ont également loué au moins un vélo.

```pgsql
SELECT DR.PersonFK AS PersonID
FROM DrivingLicenseRequest DR INNER JOIN DrivingLicense DL 
  ON DR.LicenseID = DL.LicenseID
INTERSECT
SELECT R.PersonFK
FROM Rental R;
```

Nous pourrions écrire cette requête en utilisant uniquement des opérations JOIN. Mais cette fois, il pourrait être plus naturel et direct de la considérer comme une opération d'ensemble.

Tout d'abord, comme illustré ci-dessus, nous pouvons construire une requête qui renvoie l'identifiant de toutes les personnes qui possèdent actuellement un permis de conduire actif. Pour ce faire, nous effectuons un JOIN entre **DrivingLicenseRequest** et **DrivingLicense**, afin de pouvoir rassembler les informations du permis de conduire avec la **clé étrangère PersonFK** de DrivingLicenseRequest, qui identifie la personne ayant demandé le permis. Ensuite, nous pouvons construire une autre requête qui renvoie toutes les personnes ayant loué au moins un vélo à l'aide de la clé étrangère PersonFK de la table Rental.

Et enfin, pour savoir quelles personnes possèdent un permis de conduire et ont également loué au moins un vélo, nous devons conserver les uplets qui se trouvent dans les deux tables. En d'autres termes, si les tables sont des multiensembles contenant des uplets, nous devons conserver ceux qui apparaissent dans les deux multiensembles en même temps.

Au lieu d'utiliser l'opération UNION, qui représente l'**union d'ensembles**, nous pouvons utiliser INTERSECT. Elle effectue l'**intersection** entre des ensembles, ce qui donne la table finale de la requête où nous n'avons que les personnes qui remplissent toutes les conditions.

Dans la requête précédente, nous n'avons obtenu que l'identifiant de chaque personne, car la connaissance de la valeur de sa clé primaire **{PersonID}** suffit pour identifier de manière unique une personne. Avec les clés étrangères **PersonFK** pointant vers la clé primaire **{PersonID}** de la table Person, nous n'avons pas besoin que la requête renvoie plus d'informations sur la personne, car nous pouvons l'identifier avec sa clé primaire.

Mais il existe des situations où nous pourrions vouloir obtenir plus d'informations sur la personne dans la même requête, comme son nom en plus de l'identification. Ainsi, si nous devions modifier la requête pour renvoyer cela, le moyen le plus simple consisterait à utiliser une clause WITH qui stocke les identifiants des personnes, puis à effectuer un INNER JOIN avec la table Person dans le corps de la requête, obtenant ainsi toutes les informations présentes dans la table Person.

```pgsql
SELECT DR.PersonFK AS PersonID, (SELECT Name FROM Person WHERE PersonID=DR.PersonFK)
FROM DrivingLicenseRequest DR INNER JOIN DrivingLicense DL 
  ON DR.LicenseID = DL.LicenseID
INTERSECT
SELECT R.PersonFK, (SELECT Name FROM Person WHERE PersonID=R.PersonFK)
FROM Rental R
ORDER BY PersonID;
```

Mais pour illustrer d'autres façons d'obtenir plus d'informations sur les personnes du système à partir de leur identification dans la même requête sans utiliser WITH, nous avons la possibilité d'utiliser des sous-requêtes dans l'instruction SELECT, comme vous pouvez le voir dans l'exemple ci-dessus. Plus précisément, si nous n'avons besoin de renvoyer que le nom en plus du PersonID, nous pouvons créer une sous-requête corrélée qui, pour chaque uplet à renvoyer, obtient le nom de la personne avec un identifiant spécifique. En d'autres termes, elle recherche dans la table Person l'uplet avec un certain PersonID, récupère le nom et l'ajoute comme colonne supplémentaire.

En général, l'utilisation de sous-requêtes corrélées dans le SELECT n'est pas une bonne pratique car, comme vous pouvez le deviner, le résultat de la sous-requête doit être calculé pour chaque uplet à renvoyer. Cela complique également la maintenance, la clarté du code et rend l'optimisation par le SGBD plus difficile dans la plupart des cas.

Fondamentalement, avec un simple WITH et un INNER JOIN, vous pouvez éviter d'avoir à parcourir toute la table Person pour chaque personne afin d'obtenir une caractéristique spécifique, en rassemblant plutôt les données de la table intermédiaire du WITH et de la table Person.

Tout comme les autres opérateurs d'ensemble, INTERSECT prend des multiensembles en entrée et renvoie par défaut un ensemble, il ne peut donc pas y avoir d'uplets en double dans la table de sortie, comme nous l'avons vu précédemment avec UNION. Ainsi, si nous devons forcer l'opérateur à toujours travailler avec des multiensembles et à renvoyer également un multiensemble comme sortie de l'**opération d'intersection**, nous pouvons ajouter le modificateur ALL, comme illustré dans l'exemple de requête ci-dessous :

```pgsql

SELECT BikeFK AS BikeID
FROM Rental
WHERE StartTimestamp >= '2024-01-01'
INTERSECT ALL
SELECT BikeFK
FROM Rental
WHERE Duration <= 3
ORDER BY BikeID;
```

Dans cette requête, nous obtenons des informations sur les vélos qui ont été loués au moins une fois pendant ou après 2024 et dont la durée de location était d'au plus 3 heures. Pour ce faire, nous construisons une requête qui récupère tous les vélos ayant eu au moins une location à une date **>= '2024-01-01'**, puis une autre qui récupère ceux ayant eu au moins une location avec une durée maximale de 3 heures.

Ensuite, pour ne conserver que les vélos qui remplissent les deux conditions à la fois, nous effectuons l'intersection entre les multiensembles renvoyés par les requêtes, en conservant les uplets qui se trouvent dans les deux multiensembles à la fois. Et, comme le même vélo a pu faire l'objet de plusieurs locations présentant ces caractéristiques, il peut y avoir des doublons dans la table de résultat finale de la requête. Si nous voulons les préserver, nous devrons ajouter le modificateur ALL.

Par défaut, nous n'utilisons généralement pas ALL dans ce type de requête, car nous voulons simplement savoir quels vélos remplissent les conditions. Mais il est possible que, en raison d'une exigence de l'utilisateur, la requête doive renvoyer des doublons, auquel cas nous utiliserions ALL.

Dans la plupart des situations, les performances sont suffisamment similaires pour être négligeables. Mais plus il y a de données dans la base de données, plus la différence de performance sera notable entre l'utilisation de ALL ou non. Cela dépend également des [algorithmes](https://stackoverflow.com/questions/1111707/what-is-the-difference-between-a-hash-join-and-a-merge-join-oracle-rdbms) que le SGBD utilise en interne pour implémenter cette opération.

Le dernier opérateur d'ensemble que nous examinerons ici est EXCEPT, qui est appelé MINUS dans certains SGBD. Fondamentalement, il implémente l'opération de différence entre ensembles, ce qui signifie que si nous avons plusieurs ensembles A et B avec des uplets, la différence A-B renvoie un ensemble avec tous les uplets qui **sont** dans A et **ne sont pas** dans B.

```pgsql
SELECT p.EntryFK, p.PersonFK, p.PoolFK
FROM PoolSanction p
WHERE p.BanEndDate < CURRENT_DATE
EXCEPT
SELECT p.EntryFK, p.PersonFK, p.PoolFK
FROM PoolSanction p INNER JOIN Sanction s ON p.SanctionID = s.SanctionID
WHERE s.Status = 'active';
```

Par exemple, dans la requête ci-dessus, nous obtenons des informations sur toutes les sanctions de piscine où la date de fin d'interdiction est antérieure à la date actuelle à laquelle la requête est exécutée et qui ne sont pas actives.

Comme toujours, pour ce faire, nous pourrions penser que le moyen le plus simple consiste à utiliser des opérations JOIN et une clause WHERE où les conditions sont implémentées. Mais pour illustrer l'utilisation de EXCEPT, nous pouvons formuler la requête comme la recherche de toutes les sanctions qui remplissent la première condition d'avoir une date de fin d'interdiction avant CURRENT_DATE, puis parmi toutes celles-ci, en sélectionnant uniquement celles qui ne sont pas actives. C'est-à-dire que parmi toutes celles qui remplissent la condition de date, nous ne conservons que celles qui ne sont pas actives.

Vu d'une autre manière, en obtenant toutes celles qui remplissent la condition de date, nous obtenons un ensemble A avec des uplets, où chacun représente une sanction. Parmi toutes celles-ci, il peut y en avoir qui sont actives et d'autres qui ne le sont pas. Ainsi, pour conserver celles qui nous intéressent, nous devons retirer de l'ensemble A toutes celles qui sont actives. En d'autres termes, si nous considérons que toutes les actives sont dans un autre ensemble appelé B, alors les sanctions qui nous intéressent seront dans la différence A-B (cela signifie toutes les sanctions qui remplissent la condition de date (sont dans A) et ne sont pas actives (ne sont pas dans B)).

Ainsi, dans la requête, vous pouvez voir que nous utilisons l'opérateur EXCEPT pour travailler avec les requêtes qui obtiennent respectivement les ensembles A et B. C'est-à-dire que la première requête construit l'ensemble A en imposant la condition **p.BanEndDate < CURRENT_DATE** sur les uplets de **PoolSanction**, tandis que la requête suivant l'opérateur EXCEPT construit l'ensemble B en imposant la condition **s.Status = 'active'**, en rassemblant les données de PoolSanction et Sanction pour filtrer par l'attribut Status, qui se trouve dans Sanction au lieu de PoolSanction.

Pour implémenter la différence A-B, nous utilisons EXCEPT, où la requête au-dessus de EXCEPT est l'ensemble A et celle en dessous est l'ensemble B. Il est important de garder cela à l'esprit car EXCEPT est le seul opérateur où l'ordre des opérandes peut changer le résultat de la requête.

Par exemple, avec les autres opérateurs **UNION** et **INTERSECT**, nous pouvons clairement voir qu'il importe peu que nous unissions ou intersections plusieurs ensembles A et B ou B et A – dans n'importe quel ordre, le résultat sera le même. Ce n'est pas le cas avec la différence A-B, qui ne doit pas nécessairement être équivalente à B-A. Cette propriété est appelée **commutativité**, et EXCEPT est le seul opérateur d'ensemble qui **n'est pas commutatif**.

Enfin, dans cette requête, nous pouvons voir que les alias de table sont tous en minuscules. Ceci est autorisé en SQL, et nous pouvons même déclarer un alias en majuscules puis l'utiliser en minuscules, ou vice versa. Mais si nous entourons les alias de guillemets, comme dans **Person "P"**, nous ne pouvons nous référer à la table avec l'alias qu'exactement tel qu'il est écrit entre les guillemets.

D'une part, ne pas le citer offre de la souplesse lors de l'écriture du code, car nous n'avons pas besoin de nous rappeler exactement comment il a été écrit. Dans la plupart des codes SQL, les guillemets ne sont pas couramment utilisés. Mais cela peut causer des problèmes d'ambiguïté si l'alias est nommé exactement comme une table ou un autre élément de la base de données. Le citer évite ces collisions potentielles avec les noms d'autres éléments.

En fin de compte, la décision de l'alias à attribuer à chaque table ou élément de la requête dépend principalement de sa complexité et du guide de style suivi, entre autres facteurs.

Tout comme les autres opérateurs d'ensemble, EXCEPT prend également des multiensembles en entrée par défaut et renvoie des ensembles, en supprimant tous les uplets en double. Ainsi, si nous devons conserver ces uplets en double, il nous suffit d'ajouter le modificateur ALL.

```pgsql
SELECT BikeFK AS BikeID
FROM Rental
EXCEPT ALL
SELECT BikeFK
FROM Rental
WHERE Duration < 2;
```

Par exemple, dans cette requête, nous obtenons des informations sur tous les vélos qui ont été loués **au moins** une fois et n'ont jamais été loués pendant moins de 2 heures.

Pour implémenter cela, nous construisons d'abord une requête qui récupère tous les vélos ayant été loués au moins une fois à l'aide de l'attribut de clé étrangère **BikeFK** de la table **Rental**. Ensuite, avec une autre requête, nous obtenons tous les vélos ayant été loués au moins une fois pendant moins de 2 heures. Enfin, pour ne conserver que ceux qui nous intéressent, nous obtenons la différence entre le premier ensemble et le second.

Comme vous pouvez le voir, un vélo a pu être loué un nombre arbitraire de fois, la première requête peut donc renvoyer de nombreux uplets en double. Si nous n'utilisons pas le modificateur ALL, tous ces doublons seront perdus, ce qui donnera une table où chaque vélo est garanti d'apparaître au plus une fois.

Mais si nous voulons conserver les doublons, le simple fait d'utiliser ALL montrera que la requête renvoie une table de résultat avec beaucoup plus d'uplets, car beaucoup d'entre eux correspondent à des vélos en double.

Ici, nous devons également considérer que, malgré la possibilité que des vélos en double existent à la fois dans l'ensemble A et dans l'ensemble B, lorsque nous effectuons la différence A-B à l'aide de **EXCEPT**, nous n'obtiendrons aucun vélo se trouvant dans B, quel que soit le nombre de fois qu'il est dupliqué dans les deux ensembles, l'un ou l'autre, ou aucun.

Mais lors de l'exécution de l'opération à l'aide de EXCEPT ALL, si nous avons **x répétitions** d'un uplet dans l'ensemble A et **y répétitions** de ce même uplet dans B, alors dans la table résultante, nous obtiendrons **max{x-y,0}** répétitions de cet uplet. C'est-à-dire que lorsqu'il y a plus de répétitions dans A que dans B, nous obtiendrons **x-y** répétitions de l'uplet dans la table finale. S'il y a plus de répétitions dans B que dans A, alors **x-y** est **négatif**, nous obtiendrons donc simplement 0 répétition de l'uplet. Cela signifie que cet uplet n'apparaîtra pas dans la table résultante de l'**opération de différence** implémentée avec **EXCEPT ALL**.

Pour bien comprendre l'**opérateur de différence,** considérons une requête où nous devons obtenir des informations sur tous les voyages de croisière pour lesquels il n'y a pas de trajet de retour. En d'autres termes, nous voulons trouver tous les trajets allant d'une **ville x** à une autre **ville y** sans retour vers la ville x.

```pgsql
SELECT V.DepartureCityFK, V.ArrivalCityFK
FROM Voyage V
EXCEPT
SELECT V2.ArrivalCityFK, V2.DepartureCityFK
FROM Voyage V2
ORDER BY DepartureCityFK, ArrivalCityFK;
```

L'approche que nous suivrons pour cette requête est basée sur la théorie des ensembles, car elle est particulièrement facile à résoudre dans ce cas. Tout d'abord, nous construisons une requête qui renvoie tous les trajets existants. À partir de ceux-ci, nous pouvons obtenir toutes les informations présentes dans la table Voyage – mais par souci de simplicité, nous nous concentrerons uniquement sur les attributs qui déterminent les villes de départ et d'arrivée du trajet (ce sont leurs clés étrangères **DepartureCityFK** et **ArrivalCityFK)**.

Ensuite, parmi tous les trajets renvoyés par la première requête, nous devons supprimer les trajets de retour. C'est-à-dire que pour chaque trajet existant qui part de la ville x et arrive à la ville y, nous cherchons un **trajet de retour** dans la table Voyage qui part de la ville y et arrive à la ville x. S'il existe, nous supprimons le trajet d'origine de la table de résultat de la première requête.

Nous pourrions implémenter cela à l'aide de l'opérateur IN et d'une sous-requête. Mais il est plus simple et plus efficace de construire une deuxième requête qui récupère tous les trajets de Voyage mais inverse les villes de départ et d'arrivée pour chaque trajet comme illustré ci-dessus. Cette deuxième requête est chargée d'obtenir tous les trajets de retour possibles qui pourraient exister en inversant les valeurs des clés étrangères **DepartureCityFK** et **ArrivalCityFK**, ce qui signifie échanger les villes de départ avec les villes d'arrivée.

Enfin, avec ces deux requêtes, nous appliquons l'opérateur **EXCEPT**, où nous supprimons de la table de résultat de la première requête (qui contient tous les trajets de Voyage) tous ceux contenus dans la table de résultat de la deuxième requête. En d'autres termes, de tous les trajets existants, nous supprimons ceux considérés comme des trajets de retour car ils ont été générés par la deuxième requête en inversant les villes de départ et d'arrivée.

Même si certains de ces trajets de retour n'existent pas dans **Voyage** (ce qui peut arriver), l'opérateur EXCEPT ignorera simplement cet uplet à supprimer puisqu'il n'existe pas dans l'ensemble duquel il doit être retiré.

Pour en finir avec ce type de requête, nous avons vu jusqu'à présent certaines qui appliquent un seul opérateur d'ensemble. Mais SQL nous permet d'en utiliser n'importe quel nombre dans la même requête ou sous-requête selon les besoins. Ceci est appliqué dans la requête ci-dessous, qui récupère des informations sur toutes les personnes qui ont ou ont eu une demande de permis de conduire enregistrée dans la base de données, ou un permis approuvé, et qui n'ont jamais eu de demande rejetée.

```pgsql
WITH Persons AS (
    SELECT DR.PersonFK
    FROM DrivingLicenseRequest DR
        INNER JOIN DrivingLicense DL ON DR.LicenseID = DL.LicenseID
    UNION
    SELECT DR2.PersonFK
    FROM DrivingLicenseRequest DR2
    EXCEPT
    SELECT DR3.PersonFK
    FROM DrivingLicenseRequest DR3
        INNER JOIN RejectedDrivingLicense RD ON DR3.LicenseID = RD.LicenseID
)
SELECT PersonFK
FROM Persons
ORDER BY PersonFK;
```

En ce qui concerne l'implémentation, nous pouvons voir que dans la première requête utilisée pour construire la table intermédiaire Persons, nous obtenons toutes les personnes qui ont ou ont eu un permis de conduire accepté en utilisant un INNER JOIN entre les tables DrivingLicenseRequest et DrivingLicense. De cette façon, avec les données de DrivingLicenseRequest, nous pouvons accéder à la clé étrangère PersonFK qui identifie la personne ayant effectué la demande.

Ensuite, nous effectuons une union avec une deuxième requête qui récupère les personnes ayant effectué une demande, qu'elle soit en attente, acceptée ou rejetée. Cette fois, nous obtenons les données de la table DrivingLicenseRequest, qui englobe toutes les demandes existantes dans la base de données.

En effectuant l'union, nous obtenons toutes les personnes qui ont ou ont eu des demandes en attente, acceptées ou rejetées, puisque la première requête ne renvoie que celles ayant un permis approuvé – mais la seconde renvoie les personnes ayant également eu des demandes rejetées.

Pour exclure celles ayant des demandes rejetées, l'opérateur EXCEPT est utilisé avec une autre requête qui récupère ces personnes ayant des demandes rejetées. Elles sont donc toutes exclues du résultat final de la requête – ou plutôt de la table intermédiaire Persons. De cette table, nous obtenons enfin tous ses uplets et les trions par l'attribut PersonFK – c'est-à-dire par l'identifiant des personnes que nous obtenons.

Comme vous pouvez le voir, l'ordre dans lequel les opérations d'ensemble sont effectuées est de haut en bas. C'est-à-dire que ces opérateurs agissent sur des tables contenant des résultats de requêtes, SQL effectue donc ces opérations dans un ordre descendant (bien que nous puissions utiliser des parenthèses pour changer la priorité des opérateurs selon les besoins de la requête). De plus, dans ce cas, nous pouvons voir que l'opération UNION est redondante puisque tout ce qui est contenu dans la première requête est également contenu dans la seconde.

En d'autres termes, la deuxième requête récupère les personnes qui ont ou ont eu des demandes de tout type, qu'elles soient en attente, acceptées ou rejetées, de sorte que toutes les personnes ayant eu des demandes acceptées sont incluses dans cet ensemble de personnes généré par la deuxième requête. Dans un environnement réel, nous devrions l'optimiser en nous passant de la première requête, ce qui implique également l'élimination de l'opération UNION. Mais ici, nous la laissons telle quelle pour illustrer son équivalence avec la requête optimisée que nous avons décrite.

### Requêtes d'agrégation

Ensuite, nous allons examiner un type de requête qui est souvent utilisé dans l'analyse de données temporelles, le calcul de métriques, la construction de tableaux de bord destinés à la prise de décision stratégique, etc. Ce sont les **requêtes d'agrégation**, et elles sont basées sur le traitement des uplets d'une table comme s'il s'agissait de groupes sur lesquels nous pouvons effectuer certaines opérations. Par exemple, nous pouvons les utiliser pour additionner toutes les valeurs d'un attribut dans un certain groupe, trouver leur moyenne, et calculer la valeur maximale ou minimale, entre autres.

Comme vous pouvez le deviner, les instructions de base pour implémenter ce type de requête sont GROUP BY, HAVING, et les différentes fonctions d'agrégation proposées par SQL.

Avec GROUP BY, nous pouvons choisir une série d'attributs dont les valeurs détermineront la manière dont nous formons des groupes d'uplets dans une table particulière. Cela signifie que chacun de ces groupes sera formé par une combinaison de valeurs prises par les attributs sélectionnés. Ensuite, avec les fonctions d'agrégation, nous calculerons une certaine métrique pour chaque groupe.

Avec HAVING, nous imposerons des conditions liées aux caractéristiques de chaque groupe, principalement la valeur prise par les métriques que nous calculons sur eux.

Pour comprendre tout cela avec des exemples, considérons d'abord une requête où nous voulons obtenir une liste de toutes les nationalités présentes dans la table Person et le nombre de personnes de chaque nationalité.

```pgsql
SELECT Nationality, COUNT(*) AS NumPersons
FROM Person
GROUP BY Nationality
ORDER BY NumPersons DESC;
```

À première vue, nous réalisons que nous devons compter un certain nombre de personnes pour chaque valeur que prend l'attribut **Nationality**. Ainsi, les approches que nous avons vues jusqu'à présent ne sont pas directes pour effectuer cette opération (qui dans certains cas peut ne pas être possible sans regroupement).

Par exemple, ici nous pourrions lister toutes les différentes nationalités qui apparaissent dans Nationality et, pour chacune d'elles, utiliser une sous-requête dans l'instruction SELECT pour compter combien de personnes dans la table Person ont cette nationalité.

Mais cette approche serait très inefficace puisque, pour chaque nationalité différente, nous devrions parcourir toute la table Person à la recherche de personnes ayant cette nationalité. Même si ces recherches peuvent être optimisées, elles ne sont généralement pas aussi efficaces que l'approche que nous allons suivre en utilisant le regroupement.

Au lieu de cela, nous utilisons le **regroupement** avec l'instruction **GROUP BY**. Plus précisément, nous indiquons les attributs de table qui guident la génération des groupes d'uplets dans la table. Dans ce cas, puisque nous voulons calculer une métrique pour chaque valeur de l'attribut **Nationality**, nous utilisons cet attribut pour regrouper les uplets. De cette façon, pour **chaque valeur** de cet attribut, un **groupe d'uplets** est généré, représenté par cette valeur, qui représentera toutes les personnes ayant cette même nationalité.

Ensuite, si nous voulons compter combien de personnes ont cette nationalité, nous comptons simplement combien d'uplets possède chaque groupe. Ainsi, dans l'instruction SELECT, nous ajoutons un attribut supplémentaire où nous utilisons **COUNT(*)**. Cette fois, il ne comptera pas tous les uplets de la table, mais ceux de chaque groupe. Puisque l'utilisation de GROUP BY rend obligatoire le renvoi dans le SELECT des attributs par lesquels nous regroupons, la table finale n'affichera que les valeurs distinctes de Nationality, c'est-à-dire les valeurs "représentatives" de chaque groupe d'uplets.

Pour chacune de ces valeurs, nous joindrons la valeur de **COUNT(*)** dans le même uplet de la table de sortie, ce qui correspondra au **nombre d'uplets** dans le **groupe** correspondant. Cela représente conceptuellement le nombre de personnes ayant cette nationalité.

Enfin, nous pouvons appliquer un tri avec l'instruction ORDER BY – mais nous devons garder à l'esprit que nous ne pouvons trier dans ce cas que par rapport aux attributs que nous renvoyons dans SELECT. En effet, dans la requête, nous créons des groupes représentés par des valeurs de Nationality, ce qui signifie que nous ne pouvons pas "renvoyer" le reste des attributs dans le SELECT comme nous le faisions auparavant.

Nous ne pouvons que calculer des métriques avec eux et renvoyer celles-ci – mais pas les attributs eux-mêmes avec toutes leurs valeurs. En effet, lors du regroupement, la table résultante contient nécessairement **uniquement les valeurs "représentatives"** de chaque groupe et les métriques d'autres attributs calculées à partir de ces groupes (ou les métriques du groupe lui-même, comme le nombre d'uplets qu'il possède dans ce cas).

Il existe diverses métriques que nous pouvons calculer avec les **fonctions d'agrégation** de base que SQL fournit par défaut. Ci-dessous, nous voyons une requête où nous obtenons, pour chaque statut de piscine possible, la plus petite profondeur minimale et la plus grande profondeur maximale des piscines ayant ce statut, ainsi que la profondeur moyenne et le nombre de piscines dans ce statut.

```pgsql
SELECT Status,
    MIN(MinDepth) AS Shallowest,
    AVG((MinDepth + MaxDepth) / 2.0) AS AvgDepth,
    MAX(MaxDepth) AS Deepest,
    COUNT(*) AS NumPools
FROM Pool
GROUP BY Status;
```

L'implémentation de cette requête est très similaire à la précédente, car nous devons regrouper les uplets Pool par les valeurs de leur attribut Status, qui détermine le statut des piscines.

Ainsi, dans la clause GROUP BY, nous spécifions uniquement l'attribut Status. De cette façon, nous regroupons les uplets en autant de groupes qu'il y a de valeurs présentes dans l'attribut Status dans la table, et dans chacun de ces groupes, nous avons tous les uplets représentant les piscines dans ce statut.

Ainsi, parallèlement aux informations pour chaque statut, nous pouvons calculer des métriques pour son groupe d'uplets associé – c'est-à-dire pour les piscines dans ce statut. Par exemple, avec **MIN(MinDepth)**, nous obtenons la plus petite valeur de l'attribut **MinDepth** présente dans le groupe pour lequel cette métrique est calculée. Dans ce cas, cela représente la plus petite profondeur minimale de toutes les piscines dans un certain statut.

De même, avec l'opération d'agrégation **MAX(MaxDepth)**, nous obtenons la plus grande profondeur maximale, ou en d'autres termes, la plus grande valeur de l'attribut MaxDepth dans le groupe de piscines correspondant. Avec COUNT(*), nous obtenons le nombre de piscines dans chaque groupe.

D'un autre côté, la profondeur moyenne associée aux piscines de chaque groupe est calculée avec **AVG((MinDepth + MaxDepth) / 2.0)**. Tout d'abord, il convient de noter que tant dans la clause SELECT que dans l'argument d'entrée d'une fonction d'agrégation comme AVG(), nous pouvons effectuer des opérations arithmétiques sur les attributs.

Par exemple, dans ce cas, avec **(MinDepth + MaxDepth) / 2.0**, nous calculons la valeur moyenne entre la profondeur minimale et maximale de **chaque piscine** – pas de chaque groupe, mais de chaque uplet du groupe – le tout en utilisant des valeurs décimales comme 2.0 afin que le résultat ne soit pas automatiquement arrondi à un entier. Ensuite, avec cette valeur calculée pour chaque uplet, nous utilisons la fonction d'agrégation **AVG()** pour calculer la moyenne de cette valeur pour chaque groupe.

C'est-à-dire qu'avec **(MinDepth + MaxDepth) / 2.0**, nous obtenons une certaine valeur pour chaque uplet, puis avec **AVG()**, nous prenons toutes ces valeurs calculées pour les uplets d'un certain groupe et calculons leur moyenne. Ainsi, pour chaque état possible d'une piscine, nous obtenons la profondeur moyenne de toutes les piscines dans cet état, en calculant d'abord la profondeur moyenne de chaque piscine puis en calculant la moyenne de ces profondeurs pour toutes les piscines dans un certain état.

Mais, en plus de calculer des métriques pour chaque groupe d'uplets, nous pourrions avoir besoin de ne conserver que les groupes dont les métriques répondent à certaines conditions, selon la requête à résoudre. Par exemple, ici nous considérons une requête où nous obtenons, pour chaque personne, le nombre de locations de vélos qu'elle a effectuées depuis le début des enregistrements, tant que cette personne a effectué au moins trois locations.

```pgsql
SELECT P.PersonID,
    P.Name,
    COUNT(*) AS RentalCount
FROM Rental R
    INNER JOIN Person P ON R.PersonFK = P.PersonID
GROUP BY P.PersonID, P.Name
HAVING COUNT(*) > 2
ORDER BY RentalCount;
```

Pour implémenter cette requête, nous aurions pu envisager d'utiliser une sous-requête corrélée dans l'instruction SELECT qui compte combien d'uplets dans Rental ont leur clé étrangère PersonFK pointant vers chaque personne. Mais cela serait inefficace, car les regroupements sont généralement beaucoup plus rapides pour ce type de tâche.

Il n'est également **pas possible** d'imposer une condition **WHERE COUNT(*) > 2**, que ce soit dans la sous-requête de l'instruction SELECT ou dans la requête principale (en général, les conditions sur les fonctions d'agrégation ne peuvent pas être imposées dans une clause WHERE). Ainsi, dans ce cas, nous devrions utiliser une autre sous-requête dans la clause WHERE qui compte le nombre de locations de chaque personne et qui vérifie ensuite que ce nombre est > 2.

Pour éviter d'utiliser des sous-requêtes et rendre notre implémentation aussi rapide que possible, nous effectuons d'abord un INNER JOIN entre les tables Rental et Person. Nous combinons toutes leurs informations dans des uplets de leur produit cartésien où nous avons les locations et les données sur la personne qui les a effectuées. Nous pouvons le faire en imposant la condition dans la jointure que la clé étrangère PersonFK de Rental pointe vers l'identifiant PersonID de son même uplet dans le produit cartésien.

Après avoir effectué le JOIN, nous utilisons la clause GROUP BY pour regrouper les uplets résultants par les attributs PersonID et Name de la table person. Nous faisons cela parce que nous voulons calculer une métrique pour chaque personne, nous devons donc inclure son identifiant (clé primaire) dans le regroupement de l'instruction GROUP BY (ce qui signifie tous les attributs qui forment sa clé primaire).

De plus, comme nous voulons renvoyer le nom de chaque personne avec son identifiant, nous pouvons inclure l'attribut Name dans le GROUP BY. Mais il est important de noter que les attributs par lesquels nous regroupons doivent identifier de manière unique chaque groupe d'uplets formé.

En d'autres termes, en regroupant par **PersonID**, nous formons des groupes d'uplets qui contiennent toutes les locations effectuées par une certaine personne, identifiée par une valeur de sa clé primaire PersonID. Celle-ci sert de "représentant" du groupe d'uplets.

Mais comme cet attribut PersonID suffit à identifier le groupe, il n'y a pas de problème si nous incluons plus d'informations sur la personne dans cette "valeur représentative" du groupe. Ainsi, au lieu de ne contenir que sa clé primaire, elle inclut plus d'informations sur la personne, comme son nom.

Comme vous pouvez le deviner, si au lieu de regrouper par **{PersonID}** nous regroupons par une **clé candidate** (ou plutôt une **super-clé** comme dans ce cas **{PersonID, Name}**), nous obtiendrons les mêmes groupes qu'en regroupant par {PersonID}. Cela signifie que le même nombre de groupes sera toujours généré qu'il y a de personnes dans la table (puisqu'avec une super-clé nous pouvons **identifier de manière unique chaque personne, et donc chaque groupe)**.

L'ajout de l'attribut **Name** au regroupement n'est pas une décision arbitraire – nous devons utiliser l'attribut Name dans l'instruction SELECT. Lors de l'utilisation de GROUP BY, nous ne pouvons renvoyer dans l'instruction SELECT que les attributs que nous avons utilisés dans la clause GROUP BY (donc, ceux que nous avons utilisés pour le regroupement). Ainsi, pour obtenir le nom de la personne et pas seulement son identifiant, une option consiste à inclure l'attribut dans le GROUP BY afin de pouvoir le renvoyer dans le SELECT – ou en d'autres termes, utiliser l'attribut **Name** pour le regroupement.

Mais cela ne fonctionnera pas toujours car il arrive que nous regroupions par un attribut A et que nous voulions renvoyer des informations sur un autre attribut B. Mais pour **chaque valeur** de l'**attribut A**, nous avons **plusieurs uplets** avec **plusieurs valeurs différentes** dans l'attribut B. Cela nous empêche d'utiliser B pour le regroupement, bien que nous puissions toujours calculer des métriques sur B.

D'un autre côté, pour compter combien de locations chaque personne a effectuées, il nous suffit d'utiliser la fonction d'agrégation COUNT(*) après le regroupement par **{PersonID, Name}**. Cela forme des groupes d'uplets à partir du produit cartésien où nous avons les mêmes informations pour la même personne, mais chacun représente une location différente. En comptant combien d'uplets possède chaque groupe, nous obtenons le nombre de locations effectuées.

Pour ne conserver que les groupes (personnes) ayant effectué plus de 2 locations, nous utilisons la clause **HAVING** pour imposer cette condition, puisque les fonctions d'agrégation ne peuvent pas être utilisées dans la clause WHERE. De plus, nous ne pouvons pas utiliser l'alias donné à l'attribut construit avec **COUNT(*)** qui est renvoyé dans le SELECT dans HAVING. Au lieu de cela, nous devons réécrire la définition de l'attribut dans HAVING.

C'est-à-dire que, tout comme avec WHERE, nous ne pouvons pas imposer de conditions sur les attributs ou les colonnes de la table résultante que nous renvoyons en nous référant simplement à leurs alias – nous devons utiliser leurs définitions, comme dans ce cas avec **COUNT(*)**.

Il convient de noter que l'inclusion de l'attribut Name dans le GROUP BY pour le **"renvoyer"** dans le SELECT n'est pas la seule option dont nous disposons pour le faire (ou même pour obtenir plus d'informations sur la personne). Nous avons toujours la possibilité d'enregistrer le résultat de la requête dans une table intermédiaire avec une clause WITH, puis de la joindre à la table Person ou à la table appropriée.

Mais nous avons une autre option, comme illustré ci-dessous, qui consiste à regrouper uniquement par l'**attribut PersonID** puis à utiliser des sous-requêtes corrélées dans le SELECT pour obtenir le reste des informations pour chaque personne.

```pgsql
SELECT P.PersonID,
    (SELECT Name FROM Person WHERE PersonID=P.PersonID),
    COUNT(*) AS RentalCount
FROM Rental R
    INNER JOIN Person P ON R.PersonFK = P.PersonID
GROUP BY P.PersonID
HAVING COUNT(*) > 2
ORDER BY RentalCount;
```

Mais cette option n'est pas la plus optimale : comme avec une **sous-requête corrélée** dans le SELECT, nous ne pouvons ajouter qu'un seul attribut d'information par sous-requête. Cela nous oblige à utiliser une sous-requête par attribut que nous voulons ajouter, ce qui est très inefficace comme vous pouvez le voir. De plus, la corrélation des sous-requêtes réduit la maintenabilité et peut-être aussi la clarté du code, qui sont des qualités méritant d'être prises en compte.

Avec ces requêtes, nous avons vu comment nous pouvons utiliser **GROUP BY** pour regrouper des uplets par un attribut, ou même plusieurs si nous devons ajouter plus d'informations à la table résultante de la requête. De plus, nous avons vu la bonne façon d'imposer des conditions sur des expressions avec des fonctions d'agrégation, qui consiste à utiliser la clause HAVING.

Mais nous n'essayons pas toujours de renvoyer plus d'informations à l'utilisateur chaque fois que nous utilisons plusieurs attributs dans l'instruction GROUP BY. Parfois, nous devons regrouper les uplets par plus d'un attribut.

Par exemple, dans la requête ci-dessous, nous obtenons toutes les **paires personne-piscine** (uniquement celles présentes dans CityPool) qui existent dans le système. Ensuite, pour chacune d'elles, nous calculons la durée moyenne que l'utilisateur a passée dans cette piscine à travers toutes ses entrées.

```pgsql
SELECT E.PersonFK AS PersonID,
    E.PoolFK AS PoolID,
    COUNT(*) AS VisitCount,
    AVG(E.Duration) AS AvgDuration
FROM Entry E
GROUP BY E.PersonFK, E.PoolFK
ORDER BY E.PersonFK, E.PoolFK;
```

Comme vous pouvez le voir, nous obtenons les données de la table Entry, où nous devons effectuer un regroupement avec les attributs **PersonFK** et **PoolFK**, puisque nous devons calculer des métriques pour chaque paire personne-piscine. Avec ce regroupement, chaque paire de valeurs personne-piscine est un groupe formé par tous les uplets de Entry qui représentent les fois où la personne est entrée dans cette piscine.

De cette façon, avec **AVG(E.Duration)**, nous calculons la moyenne de l'attribut **Duration** pour chaque groupe (donc combien de temps, en moyenne, une personne est restée à la piscine à chaque visite) tandis que COUNT(*) compte le nombre de ces entrées.

Enfin, il est important de noter que dans cette requête, nous n'obtenons que les paires personne-piscine qui apparaissent dans la table Entry – nous ne construisons pas toutes les paires possibles. Nous ne trouverons donc aucun uplet dans la table résultante de la requête où une personne n'est jamais entrée dans une certaine piscine.

Si nous voulions inclure cette information, nous devrions structurer la requête différemment, en construisant toutes les combinaisons de personne-piscine dans une table intermédiaire puis en calculant combien d'entrées chaque personne a dans chaque piscine d'une autre manière (soit en utilisant des sous-requêtes, des opérations **OUTER JOIN**, ou même des fonctions plus avancées qui ne sont pas couvertes ici).

Dans la clause GROUP BY, nous pouvons utiliser un nombre arbitraire d'attributs pour le regroupement. La requête ci-dessous montre comment nous pouvons obtenir le nombre de fois que la croisière a effectué cet itinéraire et la somme des distances parcourues lors de ces trajets pour chaque croisière et itinéraire entre deux ports. Nous pouvons également afficher les informations des villes où ces ports sont situés.

```pgsql
SELECT V.ShipFK AS ShipID,
    V.DepartureNameFK AS DeparturePort,
    V.DepartureCityFK AS DepartureCity,
    V.ArrivalNameFK AS ArrivalPort,
    V.ArrivalCityFK AS ArrivalCity,
    COUNT(*) AS TripCount,
    SUM(V.Distance) AS TotalDistance
FROM Voyage V
GROUP BY V.ShipFK,
    V.DepartureNameFK,
    V.DepartureCityFK,
    V.ArrivalNameFK,
    V.ArrivalCityFK
ORDER BY V.ShipFK, TotalDistance DESC;
```

Comme vous pouvez le voir, dans ce cas, nous obtenons toutes ces informations à partir de la table **Voyage**, car elle possède plusieurs clés étrangères vers **CruiseShip** et **Port**, ainsi que **City**. Celles-ci peuvent nous aider à implémenter cette requête facilement.

De tous les attributs qu'elle possède, nous regroupons par **ShipFK**, **DepartureNameFK**, **DepartureCityFK**, **ArrivalNameFK**, et **ArrivalCityFK**. Cela nous permet de regrouper les uplets de la table Voyage sur la base des combinaisons de valeurs représentant une **paire croisière-itinéraire** (où un **itinéraire** est considéré comme une **paire de ports** avec les valeurs de ville où ils sont situés).

Celles-ci sont **redondantes** pour le regroupement lui-même, car il est clair que tous les ports appartiennent à une seule et unique ville (selon le domaine). Mais si nous voulons connaître la ville où se trouve le port, l'option la plus simple consiste à inclure les attributs **DepartureCityFK** et **ArrivalCityFK** dans le regroupement afin de pouvoir les renvoyer dans le SELECT.

Ainsi, pour chaque paire croisière-itinéraire, nous pouvons compter combien de trajets la croisière a effectués sur cet itinéraire à l'aide de **COUNT(*)**, et avec **SUM(V.Distance)** nous pouvons obtenir la somme de toutes les distances parcourues lors de ces trajets (car les uplets de chaque groupe dans ce cas sont les trajets que la croisière effectue ou a effectués sur l'itinéraire correspondant).

D'un autre côté, dans ce type de requête, il est également courant d'utiliser le modificateur DISTINCT pour compter les valeurs dans un groupe ou effectuer une opération d'agrégation spécifique sur celles-ci. Par exemple, dans la requête ci-dessous, nous obtenons toutes les personnes ayant déjà vécu dans une ville. Ensuite, pour chacune d'elles, nous comptons combien de **villes différentes** elles ont habitées.

```pgsql
SELECT R.PersonFK AS PersonID,
    COUNT(DISTINCT R.CityFK) AS NumCities
FROM Residence R
GROUP BY R.PersonFK
ORDER BY NumCities DESC;
```

Pour ce faire, nous utilisons les données stockées dans la table **Residence**, qui possède une clé étrangère PersonFK capable de déterminer, dans chaque uplet, la personne associée à cet enregistrement de résidence. Puisque nous voulons calculer une certaine métrique pour chaque personne ayant eu au moins une résidence, nous regroupons par l'attribut PersonFK, car la sélection de données dans la table Residence garantit que toutes ces personnes ont ou ont eu au moins un enregistrement de résidence.

Ensuite, pour chaque groupe d'uplets formé, nous pourrions utiliser COUNT(*) pour compter combien de résidences la personne "représentative" de chaque groupe a eues. Mais dans ce cas, nous voulons compter le nombre de **villes différentes** qu'elle a habitées.

Pour ce faire, nous donnerons à COUNT() l'attribut **CityFK** comme argument d'entrée, qui est une clé étrangère déterminant la ville associée à un enregistrement de résidence. Cela compterait toutes les valeurs que prend l'attribut CityFK pour chaque groupe, mais pas les valeurs distinctes. Nous devrons donc ajouter le modificateur **DISTINCT** avant l'attribut et à l'intérieur de la fonction d'agrégation COUNT() afin qu'elle ne compte que les valeurs distinctes que prend l'attribut **CityFK** dans chaque groupe. Cela correspond au nombre de villes différentes auxquelles une certaine personne a été associée via Residence, c'est-à-dire où elle a vécu.

Lors de l'utilisation du modificateur DISTINCT dans les fonctions d'agrégation, nous pouvons également avoir besoin d'appliquer des conditions sur ces fonctions d'agrégation. Nous devrons donc utiliser le même modificateur DISTINCT dans d'autres clauses comme **HAVING**, en plus du **SELECT** où la plupart des agrégations sont calculées et renvoyées.

```pgsql
WITH PersonsTable AS (
    SELECT CB.PersonFK AS PersonID,
        COUNT(DISTINCT CB.PaymentMethod) AS NumPaymentMethods
    FROM CruiseBooking CB
    GROUP BY CB.PersonFK
    HAVING COUNT(DISTINCT CB.PaymentMethod) > 1
    ORDER BY NumPaymentMethods DESC
)
SELECT *
FROM PersonsTable PT
    INNER JOIN Person P USING (PersonID);
```

Par exemple, ci-dessus nous avons une requête qui récupère des informations sur toutes les personnes ayant effectué au moins une réservation de croisière. Elle obtient également le nombre de modes de paiement différents qu'elles ont utilisés pour payer toutes ces réservations, tant que ce nombre est d'au moins deux modes de paiement différents.

Tout d'abord, pour implémenter cette requête, nous utilisons la table **CruiseBooking** et regroupons par **PersonFK** – car lorsqu'on doit calculer un nombre pour chaque personne, nous devrions regrouper les uplets de la table par l'attribut **PersonFK**. De cette façon, chaque groupe correspond aux réservations effectuées par une certaine personne.

Nous pouvons donc facilement utiliser **COUNT(DISTINCT CB.PaymentMethod)** pour compter combien de valeurs distinctes prend l'attribut **PaymentMethod** dans chaque groupe d'uplets. Cela correspond au nombre de modes de paiement différents que la personne représentative de ce groupe d'uplets a utilisés pour payer ses réservations.

De plus, pour exiger qu'elles aient utilisé au moins deux modes de paiement, nous utilisons une clause HAVING où nous déclarons que la valeur renvoyée par la fonction d'agrégation **COUNT(DISTINCT CB.PaymentMethod)** doit être **> 1**.

Nous ne pouvons pas utiliser son nom d'alias **NumPaymentMethods** pour déclarer cette condition (certains SGBD l'autorisent, mais pour des raisons de portabilité, il est préférable de la coder sans utiliser l'alias dans la condition), ni utiliser un WHERE car il s'agit d'une fonction d'agrégation. La bonne façon est d'utiliser un HAVING.

Bien qu'il puisse sembler que la valeur de **NumPaymentMethods** soit calculée plusieurs fois inutilement, le SGBD peut optimiser la requête automatiquement en interne pour éviter ce type de calcul inutile. Mais nous devons tout de même écrire la fonction d'agrégation plusieurs fois : une fois pour définir l'attribut **NumPaymentMethods** dans le SELECT et une autre dans le HAVING pour imposer une condition de filtrage sur les uplets de la table résultant d'un regroupement.

Enfin, nous enregistrons le résultat de ce regroupement dans une table intermédiaire appelée **PersonsTable**, où seuls l'identifiant de chaque personne et son nombre respectif de modes de paiement sont stockés. Plus tard, nous pourrons utiliser cette table intermédiaire dans une opération **JOIN** avec la table **Person**. Cela rassemblera toutes les informations de chaque personne ainsi que l'attribut contenant le nombre de modes de paiement dans une seule table. Celle-ci est ensuite finalement renvoyée comme sortie de la requête à l'utilisateur.

Ainsi, comme prévu, si nous utilisons le modificateur **DISTINCT** sur un attribut dans une fonction d'agrégation dans la clause SELECT et que nous voulons lui imposer une condition, nous devons l'écrire exactement tel qu'il apparaît dans une clause **HAVING** – qu'il utilise le modificateur ou non, puisque nous l'écrivons exactement tel qu'il apparaît dans le SELECT.

Jusqu'à présent, nous avons vu que nous pouvons donner à une fonction d'agrégation des attributs d'entrée avec lesquels elle effectuera l'opération d'agrégation correspondante. De plus, si nous n'avons besoin que des valeurs distinctes d'un certain attribut ou du **résultat d'une opération arithmétique entre attributs**, nous pouvons ajouter le modificateur DISTINCT.

Mais DISTINCT n'est pas seulement utilisé pour un attribut unique – nous pouvons également l'utiliser pour obtenir des combinaisons uniques de valeurs à partir d'une série d'attributs, ou même des résultats uniques obtenus à partir d'une opération arithmétique impliquant plusieurs attributs. Par exemple, dans la requête ci-dessous, nous voulons obtenir toutes les croisières ainsi que le nombre de paires de villes de départ et d'arrivée qu'elles ont visitées tout au long de leurs voyages.

```pgsql
SELECT V.ShipFK,
    COUNT(DISTINCT (V.DepartureCityFK, V.ArrivalCityFK)) AS NumRoutes
FROM Voyage V
GROUP BY V.ShipFK
ORDER BY NumRoutes DESC;
```

Pour ce faire, nous regroupons simplement les uplets de la table Voyage par l'attribut ShipFK, puisque nous voulons calculer un nombre pour chaque croisière (et la clé étrangère ShipFK est ce qui détermine la croisière ayant effectué le voyage). Ainsi, chaque groupe d'uplets sera “représenté” par une certaine valeur de ShipFK qui identifie de manière unique une croisière. Ces uplets, à leur tour, représenteront tous les voyages effectués par cette croisière.

Ainsi, pour compter combien de paires **distinctes** de villes de départ et d'arrivée chaque croisière a parcourues, nous pouvons utiliser la fonction d'agrégation **COUNT(DISTINCT (V.DepartureCityFK, V.ArrivalCityFK))**.

Comme vous pouvez le deviner, une croisière peut effectuer le même trajet plusieurs fois, ce qui signifie qu'au sein d'un même groupe d'uplets, nous pourrions trouver la même combinaison de valeurs pour les attributs **(V.DepartureCityFK, V.ArrivalCityFK)** plusieurs fois. Ces attributs identifient de manière unique les villes de départ et d'arrivée du trajet, donc si le trajet est effectué plusieurs fois, il doit y avoir plusieurs uplets "en double" – ou du moins des uplets avec les mêmes valeurs dans ces attributs, puisqu'il peut y avoir plusieurs ports différents dans la même ville.

Si nous regardons toutes les combinaisons de valeurs que prennent les attributs **(V.DepartureCityFK, V.ArrivalCityFK)** dans chaque groupe, nous verrons qu'elles représentent les villes de départ et d'arrivée de la croisière dans chaque trajet qu'elle a effectué. En appliquant le modificateur DISTINCT, nous traitons chaque paire de valeurs comme si elle était unique, et nous conservons toutes celles qui sont uniques. Cela se réfère aux paires de villes de départ et d'arrivée différentes dans le groupe sur lequel cette opération d'agrégation est calculée, en ignorant toutes les paires en double (qui gonfleraient artificiellement le comptage). Cela représenterait le total des trajets effectués par le navire.

Enfin, lors de la résolution d'une requête à l'aide d'un regroupement, nous pourrions avoir besoin de calculer des métriques à l'aide de fonctions d'agrégation avec le modificateur DISTINCT. Pour cette raison, nous devons considérer que si nous devons imposer une condition sur cette métrique, nous devrons utiliser la fonction d'agrégation dans la clause HAVING exactement telle qu'elle est déclarée dans le SELECT (avec le même modificateur DISTINCT et les mêmes attributs présents dans l'argument d'entrée de la fonction d'agrégation).

```pgsql
SELECT CB.PersonFK AS PersonID,
    COUNT(DISTINCT (CB.CabinNumber, CB.PaymentMethod))
FROM CruiseBooking CB
GROUP BY CB.PersonFK
HAVING COUNT(DISTINCT (CB.CabinNumber, CB.PaymentMethod)) > 1
ORDER BY count DESC;
```

Par exemple, dans la requête ci-dessus, nous obtenons les identifiants de certaines personnes, et pour chacune d'elles, nous calculons le nombre de paires distinctes composées de **numéro de cabine-mode de paiement** que la personne a générées à travers ses diverses réservations CruiseBooking à son nom. Ici, nous ne sommes intéressés que par les personnes dont le nombre de paires est d'au moins deux.

Pour implémenter cela, nous regroupons d'abord par l'attribut PersonFK de la table CruiseBooking, car il contient toutes les informations dont nous avons besoin pour calculer la métrique précédente pour chaque personne. C'est pourquoi nous n'avons besoin de regrouper que par l'attribut de clé étrangère PersonFK. Ainsi, pour chaque groupe d'uplets CruiseBooking, nous aurons toutes les réservations associées à une seule personne.

Ensuite, avec **COUNT(DISTINCT (CB.CabinNumber, CB.PaymentMethod))**, nous pouvons calculer le nombre de combinaisons distinctes de valeurs que prennent les attributs **(CB.CabinNumber, CB.PaymentMethod)** dans le groupe d'uplets. Comme vous pouvez le voir, lorsque nous voulons compter les combinaisons de valeurs de plusieurs attributs, nous déclarons les deux attributs dans un "uplet" **(CB.CabinNumber, CB.PaymentMethod)**, que nous fournissons en entrée à la fonction d'agrégation **COUNT()**. Nous utilisons le modificateur DISTINCT pour nous assurer qu'il ne compte que les combinaisons distinctes de ces deux attributs.

Plus tard, si nous voulons dire que le résultat de la fonction d'agrégation doit être supérieur à 1 pour prendre en compte le groupe d'uplets correspondant dans la construction de la sortie de la requête, nous utilisons la clause HAVING. Dans celle-ci, nous pouvons déclarer la condition en réécrivant à nouveau la fonction d'agrégation dans la clause HAVING de la même manière que nous l'avons déclarée dans le SELECT.

Notez que nous n'avons pas attribué d'alias à l'attribut que nous avons construit avec la fonction d'agrégation, SQL attribue donc automatiquement le nom **“count”** à cet attribut supplémentaire. Cela correspond au nom de la fonction d'agrégation utilisée dans sa construction.

Mais si nous créons plus d'attributs à l'aide de la même fonction d'agrégation **COUNT()**, alors tous ces attributs s'appelleront **“count”** par défaut en même temps, créant un problème d'ambiguïté. C'est pourquoi il est essentiel d'utiliser des alias pour les attributs qui sont censés être nommés de la même manière par SQL (le SGBD est responsable de l'attribution des alias par défaut).

Enfin, il est important de noter que les requêtes ne doivent pas nécessairement contenir un seul regroupement. La clause GROUP BY peut être utilisée un nombre indéfini de fois dans une requête, surtout si elle inclut une sous-requête, qui peut à nouveau utiliser la clause GROUP BY.

Mais il est important de se rappeler que vous ne pouvez pas avoir plusieurs regroupements **“en même temps”** dans la même requête. En d'autres termes, si nous utilisons GROUP BY plusieurs fois, c'est parce que notre requête est composée de sous-requêtes, chaque sous-requête effectuant un regroupement, en évitant de les faire toutes au même niveau. En d'autres termes, pour chaque clause GROUP BY, il doit y avoir une seule et unique instruction SELECT.

### Requêtes de division

À ce stade, avec tout ce que nous avons vu, nous avons suffisamment d'outils pour résoudre pratiquement n'importe quelle requête avec SQL. (Il en existe cependant certaines sur lesquelles nous ne nous attarderons pas ici car elles nécessitent d'opérer sur les données de manière récursive ou hiérarchique, ce qui est plus complexe.)

Maintenant, nous allons examiner une série de requêtes où nous utilisons ces outils précédents pour implémenter un opérateur de l'algèbre relationnelle qui n'a pas d'implémentation directe en SQL. Par exemple, nous avons vu que l'instruction **SELECT** représente l'implémentation de l'opérateur de **projection** en algèbre relationnelle. D'autres instructions telles que certains types de JOIN ou UNION, INTERSECT et EXCEPT ont également des opérateurs équivalents directs.

Mais l'opérateur de **division** n'a pas de clause ou de fonction équivalente en SQL en raison de sa nature. En résumé, si nous avons plusieurs tables, cet opérateur est chargé d'obtenir tous les uplets de l'une des tables qui sont **“associés”** à chacun des uplets de l'autre table.

Pour comprendre comment cela fonctionne, considérons l'exemple suivant :

```pgsql
SELECT R.PersonFK
FROM Rental R
GROUP BY R.PersonFK
HAVING COUNT(DISTINCT R.BikeFK) = (
        SELECT COUNT(*)
        FROM Bike
    );
```

Supposons que nous voulions trouver les personnes qui ont loué chaque vélo enregistré dans notre base de données. Pour implémenter cela, nous devrons utiliser l'opérateur de **division**, puisque dans la configuration de la requête, nous aurons deux tables : une avec des uplets contenant des informations sur une personne et un vélo, indiquant que la personne a loué le vélo, et une autre table avec tous les vélos enregistrés dans le système. Si nous appliquons une opération de division de l'algèbre relationnelle sur ces tables, nous pouvons trouver toutes les personnes qui apparaissent dans suffisamment d'uplets dans la première table pour avoir loué tous les vélos de la seconde table.

Cela peut être implémenté de nombreuses manières, et ici nous nous concentrerons sur deux. La première méthode consiste à **compter** combien de vélos différents chaque personne a loués et à vérifier si ce nombre correspond au nombre total de vélos dans le système (nous verrons comment faire cela ci-dessous). S'il correspond, alors nous savons que cette personne a loué tous les vélos.

Pour ce faire, nous pouvons regrouper les uplets de la table **Rental** par l'attribut de clé étrangère PersonFK, puisque nous devons calculer combien de vélos **chaque personne** a loués. Nous formons ainsi des groupes d'uplets représentant les locations de chaque personne ayant loué au moins une fois (les personnes n'ayant jamais loué n'apparaissent pas dans PersonFK de la table Rental).

Ensuite, à l'aide de la clause HAVING, nous comptons combien de vélos différents chaque personne a loués avec **COUNT(DISTINCT R.BikeFK)**. Cela signifie que pour chaque groupe d'uplets, nous comptons combien de valeurs différentes prend l'attribut BikeFK dans ce groupe. Cela représente le nombre de vélos différents loués, puisque BikeFK est la clé étrangère pointant vers Bike et identifie de manière unique le vélo qui a été loué.

Enfin, nous comparons ce nombre avec le nombre total de vélos dans notre base de données, que nous pouvons obtenir via une sous-requête à l'aide de la fonction d'agrégation COUNT(*). Rappelez-vous que nous pouvons utiliser COUNT(*) sans que la clause GROUP BY ne soit présente dans la sous-requête.

Nous pouvons également aborder la division des tables d'un point de vue plus proche de la théorie des ensembles. Par exemple, voici la même requête résolue en utilisant uniquement NOT EXISTS et des sous-requêtes :

```pgsql
SELECT P.PersonID
FROM Person P
WHERE NOT EXISTS (
        SELECT *
        FROM Bike B
        WHERE NOT EXISTS (
                SELECT *
                FROM Rental R
                WHERE R.PersonFK = P.PersonID
                    AND R.BikeFK = B.BikeID
            )
    );
```

Ici, si chaque personne a loué chaque vélo de la base de données, alors il n'y a pas de vélo existant qu'elle n'a pas loué. Essayons de traduire ce concept littéralement en une requête SQL : d'abord, avec un SELECT et un FROM, nous pouvons **“parcourir”** tous les uplets de Person. Ensuite, pour chacun d'eux, nous vérifions qu'il n'y a aucun vélo que la personne n'a pas loué. Pour ce faire, nous construisons une **sous-requête corrélée** qui renvoie tous les vélos que cette personne n'a pas loués.

Cette sous-requête est simplement construite en "parcourant" tous les uplets de Bike et en vérifiant qu'il n'existe aucun enregistrement de location entre la personne et le vélo en cours de parcours. Nous faisons cela par une autre sous-requête corrélée qui parcourt les uplets de Rental et ne renvoie que ceux dans lesquels la personne a loué le vélo. Si elle ne renvoie aucun uplet, c'est qu'il n'y en avait aucun présentant ces caractéristiques, ce qui nous indique que la personne parcourue n'a jamais loué le vélo parcouru. Dans ce cas, nous ne sommes pas intéressés par cette personne puisqu'elle n'a pas loué tous les vélos de la base de données.

Si quelqu'un les avait réellement tous loués, alors la **sous-requête corrélée** qui parcourt les uplets de **Rental** renverrait toujours au moins un uplet. Par conséquent, la sous-requête corrélée qui parcourt les uplets de Bike ne renverrait jamais d'uplets. Et cela satisferait la condition NOT EXISTS que nous avons imposée sur les personnes.

Si nous lisons le code SQL que nous avons implémenté "littéralement", nous **parcourons les personnes, et pour chacune nous vérifions qu'elles ont loué chaque vélo**. Nous obtenons donc finalement les mêmes personnes qu'avec la requête utilisant un regroupement et un comptage des vélos loués par chaque personne.

Si nous exécutons l'une ou l'autre de ces requêtes, elles ne renverront probablement aucun résultat. Après tout, la probabilité qu'une personne ait loué chaque vélo enregistré dans la base de données est faible.

Mais si nous voulons vérifier si les requêtes fonctionnent ou non, nous pouvons toujours insérer manuellement des uplets dans **Person**, **Bike**, et **Rental**, en particulier dans Rental. Il y aurait alors une personne ayant un uplet dans Rental pour chaque vélo de la table Bike, et pouvant ainsi être présente dans le résultat de l'opération de **division**.

Une autre requête que nous pouvons résoudre à l'aide d'une opération de division de l'algèbre relationnelle est celle ci-dessous. Nous y trouvons toutes les personnes qui sont entrées dans **toutes** les piscines d'une certaine ville (spécifiquement celle ayant la valeur CityID de 55).

```pgsql
SELECT E.PersonFK
FROM Entry E
    INNER JOIN CityPool CP ON E.PoolFK = CP.PoolID
    INNER JOIN Pool P ON CP.PoolID = P.PoolID
WHERE P.CityFK = 55
GROUP BY E.PersonFK
HAVING COUNT(DISTINCT E.PoolFK) = (
        SELECT COUNT(*)
        FROM CityPool CP2
            INNER JOIN Pool P2 ON CP2.PoolID = P2.PoolID
        WHERE P2.CityFK = 55
    );
```

Dans ce cas, nous rassemblons d'abord toutes les informations des tables Entry, CityPool et Pool. Cela nous permet d'obtenir les informations des personnes qui sont entrées dans les piscines et les informations de la ville où la piscine est située. Ainsi, après avoir rassemblé ces informations avec les opérations INNER JOIN, nous imposons la condition que la clé étrangère CityFK doit référencer une certaine ville, spécifiquement celle identifiée par la valeur 55 dans sa clé primaire **{CityID}**. Nous faisons cela pour filtrer les uplets résultant des JOIN, afin de n'avoir que ceux où les personnes sont entrées dans des piscines de la ville spécifique que nous considérons dans la requête.

Mais cette condition ne doit pas nécessairement se trouver dans cette clause WHERE, car il existe d'autres alternatives tout aussi valables (utilisation de sous-requêtes, CTE, etc.).

Ensuite, nous regroupons les uplets par PersonFK, de sorte que chaque groupe d'uplets représente toutes les entrées en piscine d'une certaine personne (spécifiquement les entrées dans les piscines de la ville identifiée par la valeur **CityID=55**). Pour ne trouver que les personnes qui sont entrées dans toutes les piscines de cette ville, nous utilisons **COUNT(DISTINCT E.PoolFK)** pour compter le nombre de piscines différentes dans lesquelles elles sont entrées. Cela équivaut au nombre de valeurs distinctes prises par la **clé étrangère PoolFK** dans la table **Entry**. Nous comparons ensuite ce nombre avec le nombre total de piscines municipales situées dans la ville avec CityID=55, le tout obtenu via une sous-requête non corrélée simple.

Dans cette sous-requête, nous effectuons un autre INNER JOIN entre CityPool et Pool pour rassembler les données sur toutes les piscines municipales avec la clé étrangère CityFK qui détermine la ville où elles se trouvent. Cela nous permet de déclarer la condition **P2.CityFK = 55** pour compter toutes les piscines de cette ville à l'aide de **COUNT(*)**. De plus, l'avantage de la sous-requête non corrélée est qu'elle n'a besoin d'être calculée qu'une seule fois, puisque le nombre de piscines dans cette ville ne change pas pendant l'exécution de la requête.

Si nous essayons de résoudre la requête précédente en utilisant l'approche la plus proche de la théorie des ensembles, comme nous l'avons fait précédemment, nous aboutirons à une implémentation qui utilise principalement l'opérateur NOT EXISTS et des sous-requêtes corrélées.

Conceptuellement, nous pouvons résoudre la requête en parcourant toutes les personnes de la base de données et en vérifiant qu'il n'y a aucune piscine municipale située dans la ville avec **CityID=55** pour laquelle il n'y a pas d'entrée associant la personne à la piscine. En d'autres termes, pour chaque personne, il doit y avoir une entrée pour chaque piscine municipale de la ville avec **CityID=55**.

```pgsql
SELECT * 
FROM Person P
WHERE NOT EXISTS (
        SELECT *
        FROM CityPool CP
            INNER JOIN Pool PL ON CP.PoolID = PL.PoolID
        WHERE PL.CityFK = 55
            AND NOT EXISTS (
                SELECT *
                FROM Entry E
                WHERE E.PersonFK = P.PersonID
                    AND E.PoolFK = CP.PoolID
            )
    );
```

Maintenant, en codant tout cela, nous arrivons à une requête très similaire à la précédente où nous cherchions des personnes ayant loué tous les vélos. Comme vous pouvez le voir, nous parcourons d'abord tous les uplets de Person, et pour chacun d'eux, nous construisons une sous-requête corrélée qui obtient toutes les piscines municipales dans lesquelles la personne correspondante n'est pas entrée.

Pour ce faire, nous effectuons un JOIN entre CityPool et Pool et imposons la condition qui garantit que toutes les piscines municipales que nous considérons sont situées dans la ville avec CityID=55. De plus, nous vérifions avec une autre sous-requête corrélée qu'il n'y a pas d'entrée de la personne dans la piscine que nous examinons.

Chacune de ces approches pour la même requête présente des différences de performance significatives. Dans cette dernière implémentation, nous imbriquons plusieurs sous-requêtes, ce qui conduit à parcourir de nombreux uplets, ce qui est souvent inutile. D'un autre côté, l'utilisation du regroupement a tendance à être plus rapide puisque le parcours des uplets dépend principalement de la manière dont l'opération GROUP BY est implémentée (ce qui offre généralement des performances adéquates pour la plupart des requêtes).

Outre la performance, dans cette dernière requête, nous pouvons facilement renvoyer toutes les informations pour chaque personne car nous utilisons directement la table Person dans l'implémentation. En revanche, dans l'approche précédente utilisant GROUP BY, nous ne renvoyions que l'identifiant de chaque personne, nous obligeant à utiliser des CTE pour effectuer un JOIN avec la table Person si nous voulons renvoyer plus d'informations que l'identifiant.

Ainsi, lors de l'exécution d'une division en SQL, nous devrions considérer non seulement l'efficacité de l'implémentation mais aussi la facilité de modification de la requête, ainsi que sa clarté et sa maintenabilité.

Les deux requêtes précédentes ont été formulées en considérant la ville avec CityID=55, bien qu'il s'agisse d'une décision arbitraire. Si nous voulons choisir une valeur appropriée pour **CityID** afin que les deux requêtes précédentes renvoient des données, puisqu'il peut y avoir des villes où personne n'est entré dans toutes leurs piscines, nous pouvons utiliser la requête ci-dessous. Pour chaque personne et ville, elle obtient le nombre de piscines dans cette ville dans lesquelles la personne est entrée, ainsi que le nombre total de piscines dans cette ville.

```pgsql
SELECT E.PersonFK,
    P.CityFK,
    COUNT(DISTINCT E.PoolFK) AS EnteredPools,
    (
        SELECT COUNT(*)
        FROM CityPool AS CP2
            INNER JOIN Pool AS P2 ON CP2.PoolID = P2.PoolID
        WHERE P2.CityFK = P.CityFK
    ) AS TotalPools
FROM Entry AS E
    INNER JOIN CityPool AS CP ON E.PoolFK = CP.PoolID
    INNER JOIN Pool AS P ON CP.PoolID = P.PoolID
GROUP BY E.PersonFK, P.CityFK
ORDER BY EnteredPools, TotalPools;
```

Comme vous pouvez le voir, plusieurs opérations JOIN sont d'abord effectuées pour rassembler toutes les informations de Entry, CityPool et Pool, afin de pouvoir ensuite regrouper les uplets résultants par PersonFK et CityFK. Cela signifie regrouper les uplets en groupes où chacun représente les entrées qu'une certaine personne a effectuées dans les piscines d'une certaine ville. Ensuite, avec **COUNT(DISTINCT E.PoolFK)**, nous comptons les piscines dans lesquelles elle est entrée, puisque PoolFK est la clé étrangère dans la table Entry qui détermine la piscine dans laquelle la personne est entrée. Enfin, avec une sous-requête corrélée dans le SELECT, nous obtenons le nombre total de piscines dans la ville identifiée par CityFK.

Enfin, il est important de noter qu'avec cette requête, nous n'obtiendrons jamais une valeur de 0 dans l'attribut EnteredPools. Si une personne n'est jamais entrée dans une piscine d'une certaine ville, il n'y aura pas d'uplets résultant de ces opérations JOIN avec des attributs **(E.PersonFK, P.CityFK)** qui référencent à la fois la personne et la ville.

Cela se produit parce qu'aucune entrée (uplet Entry) n'aura sa clé étrangère PersonFK correspondant à la personne et sa clé étrangère PoolFK correspondant à une piscine dans la ville correspondante que la personne a visitée (puisqu'elle n'a visité aucune piscine dans cette ville).

Ainsi, si nous voulons également inclure dans la table résultante de notre requête des uplets avec des paires **(E.PersonFK, P.CityFK)** de personnes n'ayant jamais visité de piscine dans la ville **CityFK**, nous devrions utiliser des opérations d'ensemble pour trouver ces paires **(E.PersonFK, P.CityFK)** et ajouter les uplets construits à partir de ces paires à la table résultante finale.

Nous pouvons voir un autre cas fondamental que nous pourrions rencontrer lors de l'implémentation d'une opération de division en SQL ci-dessous. Ici, nous avons une requête où nous obtenons toutes les personnes qui ont ou ont eu des sanctions de piscine dans tous les états possibles.

```pgsql
SELECT PS.PersonFK
FROM PoolSanction PS
    INNER JOIN Sanction S ON PS.SanctionID = S.SanctionID
GROUP BY PS.PersonFK
HAVING COUNT(DISTINCT S.Status) = 3;
```

Pour implémenter cela, nous effectuons d'abord un JOIN entre **PoolSanction** et **Sanction**, en nous assurant avec la première table que la sanction a eu lieu dans une piscine et en utilisant la seconde table pour obtenir l'état de la sanction (qui est stocké dans l'attribut Status).

Ensuite, comme nous devons compter dans combien d'états chaque personne a des sanctions, nous regroupons par l'attribut PersonFK, créant des groupes d'uplets qui représentent les sanctions que chaque personne a ou a eues. De cette façon, nous pouvons utiliser HAVING pour exiger que le nombre d'états dans lesquels une personne a des sanctions soit égal au nombre total d'états possibles qu'une sanction peut avoir.

D'une part, avec **COUNT(DISTINCT S.Status)**, nous pouvons compter combien de valeurs différentes l'attribut Status prend dans chaque groupe – ou en d'autres termes, le nombre d'états des sanctions associées à une personne. Et, puisqu'il y a trois états possibles ('created', 'active', 'expired'), nous comparons simplement le comptage résultant de la fonction d'agrégation avec 3.

Mais si nous utilisons la constante 3 dans la comparaison et que nous modifions plus tard la base de données pour inclure plus ou moins d'états dans les sanctions, nous serons obligés de changer ce nombre. Cela rend la requête moins maintenable qu'elle ne pourrait l'être.

Ainsi, une autre option que nous avons pour déclarer la condition dans la clause HAVING est de comparer le résultat de la fonction d'agrégation COUNT(*) avec le résultat d'une sous-requête qui calcule combien d'états possibles une sanction peut avoir.

```pgsql
SELECT PS.PersonFK
FROM PoolSanction PS
    INNER JOIN Sanction S ON PS.SanctionID = S.SanctionID
GROUP BY PS.PersonFK
HAVING COUNT(DISTINCT S.Status) = (SELECT COUNT(DISTINCT Status) FROM Sanction);
```

Comme vous pouvez le voir ci-dessus, cette sous-requête est non corrélée, car elle compte simplement combien de **valeurs distinctes** l'attribut **Status** prend dans la table **Sanction**. Mais l'implémentation de la requête de cette manière pose un problème : nous supposons que dans la table Sanction, spécifiquement dans l'attribut Status, nous pouvons trouver toutes les valeurs possibles que Status peut prendre. Mais cela pourrait ne pas être le cas, car si la table est vide, aucune valeur distincte ne peut être comptée dans l'attribut Status.

Cela signifie que cette dernière implémentation de la requête ne fonctionne que lorsque la table **Sanction** contient des uplets représentant des sanctions où il y a au moins une sanction dans tous les états possibles. Si nous pouvons garantir que la base de données remplit cette condition, alors l'implémentation ci-dessus est plus pratique pour nous car elle ne nécessite aucune maintenance.

Mais cette condition n'est généralement pas remplie, il n'est donc pas de bonne pratique de supposer que nous trouverons toutes les valeurs possibles qu'un attribut peut prendre dans cet attribut. Par exemple, si nous pensons à un attribut **entier**, il est clair qu'il n'y a pas forcément d'uplets qui prennent une valeur différente pour chaque valeur possible que l'attribut peut avoir.

Une autre option que nous avons est de nous passer du regroupement et d'utiliser une approche basée sur la théorie des ensembles. Comme vous pouvez le voir, dans l'implémentation ci-dessus, nous parcourons tous les uplets de Person, et pour chacun d'eux, nous vérifions qu'il **existe** une sanction de piscine avec le statut **‘created’**. De plus, à l'aide de l'opérateur logique AND, nous exigeons qu'en même temps il existe une autre sanction de piscine avec le statut **‘active’**. Enfin, nous utilisons un autre opérateur logique AND pour exiger également que pour cette personne il existe une autre sanction de piscine dans le statut **‘expired’**.

```pgsql
SELECT p.PersonID
FROM Person p
WHERE EXISTS (
        SELECT *
        FROM PoolSanction ps
            INNER JOIN Sanction s ON ps.SanctionID = s.SanctionID
        WHERE ps.PersonFK = p.PersonID
            AND s.Status = 'created'
    )
    AND EXISTS (
        SELECT *
        FROM PoolSanction ps
            INNER JOIN Sanction s ON ps.SanctionID = s.SanctionID
        WHERE ps.PersonFK = p.PersonID
            AND s.Status = 'active'
    )
    AND EXISTS (
        SELECT *
        FROM PoolSanction ps
            INNER JOIN Sanction s ON ps.SanctionID = s.SanctionID
        WHERE ps.PersonFK = p.PersonID
            AND s.Status = 'expired'
    );
```

Comme vous pouvez le voir ci-dessus, cette implémentation est équivalente à la précédente où nous utilisions des regroupements et des comptages pour implémenter l'opération de division. Mais cette approche est clairement moins maintenable, bien que peut-être plus facile à comprendre sous certains aspects.

Par exemple, dans cette implémentation, les noms des différentes valeurs de **Status** apparaissent explicitement dans les conditions que nous imposons dans chaque sous-requête corrélée, ce qui n'est généralement pas une bonne pratique. Si vous souhaitez modifier le domaine de la base de données, vous devrez également modifier ces valeurs.

De plus, nous dupliquons le même code plusieurs fois, ce qui rend le code de la requête dans son ensemble moins maintenable. En effet, si la requête elle-même doit être modifiée, il est très probable que nous devions apporter des modifications dans les trois sous-requêtes, ce qui ralentit le processus de gestion.

Ainsi, bien que l'approche basée sur la théorie des ensembles puisse être peu pratique dans certaines situations, elle peut fonctionner pour une petite base de données comme celle que nous traitons ici. Mais, chaque fois que possible, il est préférable de choisir des solutions plus maintenables et nécessitant moins de changements à l'avenir.

Dans ce cas précis, la meilleure option serait d'utiliser l'approche par regroupement où le nombre d'états de sanction pour une personne est comparé au nombre total d'états, car changer ce nombre dans la requête est plus facile que de modifier le code de plusieurs sous-requêtes. Cela évite également d'avoir à faire des suppositions sur les uplets de **Sanction**.

Regardons une autre requête similaire aux précédentes, où nous pouvons voir une autre façon dont l'opérateur de division peut apparaître. Elle récupère toutes les personnes qui, pour chaque ville où elles ont vécu, ont visité au moins une piscine située dans cette ville.

```pgsql
SELECT P.PersonID
FROM Person P
WHERE NOT EXISTS (
        SELECT *
        FROM Residence R
        WHERE R.PersonFK = P.PersonID
            AND NOT EXISTS (
                SELECT *
                FROM Entry E
                    INNER JOIN Pool PO ON E.PoolFK = PO.PoolID
                WHERE E.PersonFK = P.PersonID
                    AND PO.CityFK = R.CityFK
            )
    );
```

Pour chaque personne, ne la conservez que s'il n'y a aucune résidence de sa part qui manque d'une visite de piscine correspondante dans la même ville. Équivalemment : pour chaque ville où une personne a vécu (d'après Residence), il doit y avoir au moins un enregistrement montrant qu'elle a visité une piscine dans cette ville.

L'implémentation de cette approche est très similaire à la façon dont nous l'exprimons en langage naturel. D'une part, nous parcourons les uplets de Person avec un SELECT et un FROM, et nous fixons la condition que le résultat d'une sous-requête soit vide à l'aide de NOT EXISTS.

Dans cette sous-requête corrélée, nous parcourons les uplets de Residence pour la personne pour laquelle nous vérifions actuellement la condition, donc pour ne conserver que les résidences qui nous intéressent, nous imposons la condition **R.PersonFK = P.PersonID** dans la sous-requête. Cela garantit que les uplets Residence sélectionnés ont leur clé étrangère PersonFK pointant vers la personne que nous parcourons, dont l'identification est donnée par **P.PersonID**.

D'autre part, au sein de cette sous-requête, nous vérifions également qu'une autre sous-requête corrélée et imbriquée ne renvoie aucun uplet non plus. Cette dernière sous-requête est dédiée à l'obtention de toutes les entrées où la personne identifiée par **P.PersonID** est entrée dans une piscine située dans la ville identifiée par **R.CityFK** – c'est-à-dire la ville de la résidence que nous parcourons au moment de l'exécution de cette sous-requête.

En résumé, dans cette requête, nous avons vu que les divisions ne se réfèrent pas toujours à des situations où les uplets que nous voulons obtenir sont "associés" à tous les uplets d'une autre table. Au contraire, comme dans ce cas, elles peuvent également se référer au fait que les uplets de sortie de notre requête doivent remplir une certaine condition par rapport à tous les uplets d'une autre table.

Semblable à la requête précédente, nous pouvons en considérer une autre où nous devons trouver des personnes qui ont ou ont eu au moins une réservation de voyage dans toutes les classes de croisière existantes.

```pgsql
SELECT CB.PersonFK
FROM CruiseBooking CB
    INNER JOIN CruiseShip CS ON CB.ShipFK = CS.ShipID
GROUP BY CB.PersonFK
HAVING COUNT(DISTINCT CS.Class) = (
        SELECT COUNT(DISTINCT Class)
        FROM CruiseShip
    );
```

Dans ce cas, nous commençons par configurer l'opération de division par regroupement et comptage. Tout d'abord, nous effectuons un INNER JOIN entre les tables **CruiseBooking** et **CruiseShip**. Cela nous permet de rassembler des informations sur la personne qui a effectué chaque réservation de voyage à l'aide de la clé étrangère **PersonFK** de CruiseBooking et les informations sur la classe de croisière pour le voyage. Cette même table possède une clé étrangère **ShipFK** qui identifie de manière unique le navire de croisière pour le voyage, à partir duquel nous pouvons déterminer sa classe.

Ainsi, après cette opération, nous regroupons par l'attribut PersonFK, car nous devrons compter combien de classes de croisière différentes chaque personne a réservées pour effectuer la division.

Concernant cette quantité, nous la calculons à l'aide de la fonction d'agrégation **COUNT(DISTINCT CS.Class)**, qui est exécutée une fois pour chaque groupe d'uplets. Ensuite, nous la comparons avec le nombre total de classes de croisière dans notre base de données.

Dans ce cas, nous aurions pu écrire directement le nombre au lieu d'utiliser une sous-requête non corrélée pour obtenir le nombre total de classes en regardant les valeurs distinctes de l'attribut **Class** de la table **CruiseShip**. Ainsi, en l'état, avec la sous-requête, nous supposons implicitement que la table CruiseShip contient des croisières dans toutes les classes existantes (mais cela pourrait ne pas être le cas).

Imaginez si la table est vide, par exemple – la sous-requête donnerait un total de 0 classe de croisière, alors qu'en réalité, il peut y en avoir plus (le domaine de l'attribut Class peut contenir plus de valeurs que celles apparaissant réellement dans la table).

Mais il est important de clarifier ici que par “toutes les classes de croisière”, nous entendons toutes les valeurs possibles que l'attribut **Status** peut prendre – c'est-à-dire les valeurs que nous définissons comme le domaine de l'attribut. D'un autre côté, dans certaines circonstances, nous pouvons supposer que toutes les classes de croisière correspondent aux valeurs distinctes que l'attribut Status prend dans la table **CruiseShip**, tout dépend du domaine avec lequel nous travaillons.

Par souci de simplicité, nous supposerons désormais dans ce domaine que les valeurs distinctes d'un attribut comme **Class** trouvées dans sa table correspondante sont équivalentes à toutes les valeurs qu'il peut prendre. Si nous y réfléchissons, cela est logique car s'il n'y a que 2 valeurs distinctes dans l'attribut Class de la table CruiseShip, alors toutes les réservations effectuées pendant tout le temps où la base de données a existé devront référencer une croisière dans la table CruiseShip (dont la classe aura l'une de ces deux valeurs). Il se peut qu'il n'y ait aucune réservation référençant des croisières d'une certaine classe, mais s'il y a des croisières de deux classes, alors il est logique de supposer que ces deux classes constituent **“toutes les classes que l'attribut Class peut contenir.”**

Ainsi, en supposant que l'attribut Class de la table CruiseShip contient "toutes les classes" de croisières, nous pouvons résoudre la requête en utilisant une approche de théorie des ensembles comme illustré dans la requête ci-dessous.

Ici, nous parcourons d'abord tous les uplets de CruiseBooking qui représentent des réservations. Dans chacun d'eux, nous vérifions qu'il n'y a pas de croisière (de n'importe quelle classe, plutôt) pour laquelle aucune réservation n'a été effectuée par la personne référencée par la clé étrangère PersonFK de l'uplet CruiseBooking que nous examinons.

```pgsql
SELECT DISTINCT CB.PersonFK
FROM CruiseBooking CB
WHERE NOT EXISTS (
        SELECT *
        FROM CruiseShip C
        WHERE NOT EXISTS (
                SELECT *
                FROM CruiseBooking CB2
                    INNER JOIN CruiseShip CS2 ON CB2.ShipFK = CS2.ShipID
                WHERE CB2.PersonFK = CB.PersonFK
                    AND CS2.Class = C.Class
            )
    );
```

C'est-à-dire que, puisque nous ne sommes intéressés qu'à obtenir les personnes qui ont déjà réservé, nous commençons la requête en parcourant CruiseBooking, et non Person, car il peut y avoir des personnes dans Person qui n'ont jamais réservé.

Ainsi, pour vérifier qu'il n'y a pas de croisière présentant ces caractéristiques, nous utilisons l'opérateur NOT EXISTS et une sous-requête corrélée dans laquelle nous parcourons toutes les croisières enregistrées dans la table CruiseShip. Pour chacune d'elles, nous vérifions qu'il n'y a pas de réservation de voyage où la croisière est celle **dont la classe est la même** que la croisière et la personne que nous examinons actuellement dans la requête.

En faisant cela, nous nous assurons que pour toutes les personnes renvoyées par notre requête, il n'y a aucune croisière de n'importe quelle classe qui n'a pas été réservée au moins une fois par cette personne. Mais nous ne pouvons le faire correctement que si nous sommes sûrs que l'attribut Class de CruiseShip inclut ce que nous considérons comme **“toutes les classes de croisière possibles“**. Si nous n'avions pas cette assurance, alors cette approche par théorie des ensembles ne serait pas correcte, car la sous-requête corrélée qui parcourt les uplets de CruiseShip pourrait ne pas couvrir toutes les classes de croisière possibles.

Par exemple, imaginez que la table CruiseShip soit vide. Dans ce cas, cette approche renverrait plus de personnes qu'elle ne le devrait, puisque cette sous-requête ne renverrait jamais d'uplets.

Au contraire, dans l'autre approche basée sur les regroupements, si la table CruiseShip est vide, alors la sous-requête non corrélée qui compte le nombre total de classes renverrait 0. De plus, la condition HAVING ne serait jamais remplie, empêchant le renvoi de personnes qui ne remplissent pas la condition définie dans l'énoncé de la requête.

Ainsi, comme vous pouvez le voir, il n'est pas toujours préférable d'utiliser une seule approche basée soit sur les **regroupements**, soit sur la **théorie des ensembles** – cela varie selon la situation.

Dans ce cas précis, il est plus pratique d'utiliser les regroupements – principalement pour l'efficacité (puisqu'en interne un regroupement est généralement plus rapide que l'exécution d'une sous-requête corrélée plusieurs fois) mais aussi pour la simplicité de maintenance et la clarté du code.

Pour en finir avec l'opérateur de division de l'algèbre relationnelle, il est important de noter qu'il arrive que nous devions effectuer une division en utilisant des tables intermédiaires (CTE) au lieu de tables de la base de données elle-même.

Par exemple, dans la requête ci-dessous, nous obtenons les navires qui ont effectué au moins un trajet au départ et à l'arrivée de chaque paire de villes ayant une superficie d'au plus 11 km². En d'autres termes, tous les navires qui ont effectué au moins un trajet entre chaque paire de villes présentant cette caractéristique.

```pgsql
WITH AllPairs AS (
    SELECT C1.CityID AS Dep, C2.CityID AS Arr
    FROM City C1 CROSS JOIN City C2
    WHERE C1.CityID <> C2.CityID AND C1.Area<11 AND C2.Area<11
),
ShipVisits AS (
    SELECT V.ShipFK,
        V.DepartureCityFK AS Dep,
        V.ArrivalCityFK AS Arr
    FROM Voyage V
        INNER JOIN City C1 ON V.DepartureCityFK = C1.CityID
        INNER JOIN City C2 ON V.ArrivalCityFK = C2.CityID
    WHERE C1.Area<11 AND C2.Area<11
)
SELECT SV.ShipFK
FROM ShipVisits SV
GROUP BY SV.ShipFK
HAVING COUNT(DISTINCT (SV.Dep, SV.Arr)) = (
        SELECT COUNT(*)
        FROM AllPairs
    );
```

Comme vous pouvez le voir dans l'implémentation, pour simplifier le code, nous pouvons d'abord construire une table intermédiaire avec toutes les paires de villes possibles ayant une valeur de superficie **< 11**. Nous pouvons le faire en exécutant un **CROSS JOIN** entre la table **City** et elle-même, car elle contient toutes les villes enregistrées dans notre base de données. Ensuite, nous exigeons que les deux villes de la paire aient une superficie < 11.

Il est important de noter que l'attribut **Area** de la table City contient des valeurs représentant des kilomètres carrés, il est donc direct de déclarer la condition < 11 dans notre requête. Mais si cet attribut avait des valeurs dans d'autres unités, nous devrions nous y adapter ou les convertir dans d'autres unités avec lesquelles nous pourrions facilement travailler. Il est crucial de considérer les unités dans lesquelles les valeurs que nous comparons sont mesurées pour coder correctement la requête.

Enfin, cette table inclut toutes les paires de villes possibles qui répondent à la caractéristique de superficie, ce qui signifie qu'il importe peu que la même paire de villes **(A,B)** apparaisse également dans la table comme **(B,A)**.

Ensuite, nous construisons une autre table intermédiaire où nous stockons les différentes paires de villes que chaque croisière a visitées tout au long de tous ses trajets, en ne considérant que les villes qui répondent aux conditions de la requête (superficie < 11).

Pour ce faire, nous extrayons simplement les attributs de clé étrangère ShipFK, DepartureCityFK et ArrivalCityFK. Ceux-ci déterminent la croisière ayant effectué le trajet et les villes de départ et d'arrivée du trajet à partir de la table résultante des opérations INNER JOIN entre la table **Voyage** et la table City elle-même.

Nous effectuons ces opérations pour accéder aux informations de superficie de chaque ville, nous permettant d'imposer les mêmes conditions de superficie que dans la première table intermédiaire **AllPairs**. Si nous ne le faisions pas, nous pourrions considérer des trajets de croisière entre des villes qui ne répondent pas aux conditions que nous recherchons. Cela augmenterait le nombre de paires de villes “valides” entre lesquelles la croisière a voyagé. Puisque nous allons structurer la requête à l'aide d'un regroupement et d'un **comptage**, il est essentiel de ne pas compter d'éléments non pertinents pour notre requête.

Une fois les deux CTE construites, nous effectuons un regroupement sur les tables **ShipVisits** basé sur l'attribut **ShipFK**. Nous faisons cela pour calculer, pour chaque croisière, le nombre de paires de villes distinctes entre lesquelles elle a voyagé. Nous calculons cela facilement à l'aide de la fonction d'agrégation **COUNT(DISTINCT (SV.Dep, SV.Arr))**. Ensuite, nous pouvons comparer la valeur renvoyée avec le nombre total de paires de villes qui existent et que nous avons stockées dans la première CTE appelée **AllPairs**, le tout au sein de la clause HAVING.

Pour ne conserver que les croisières qui ont voyagé à travers chaque paire de villes calculée dans AllPairs, nous comparons la sortie de la fonction d'agrégation **COUNT()** avec le résultat d'une sous-requête non corrélée qui compte simplement combien d'uplets possède la table intermédiaire **AllPairs**.

Dans le comptage total des paires, nous n'avons pas besoin d'utiliser le modificateur **DISTINCT**, puisque le CROSS JOIN ne génère jamais de paires de villes répétées étant donné la définition même de l'opération de produit croisé. Et il n'y a pas d'uplets identiques dans la table City, ce qui signifie qu'il n'y a pas de villes identiques dans notre base de données (encore moins avec la même valeur de leur clé primaire **CityID**). Mais si nous voulions utiliser le modificateur DISTINCT pour compter combien d'uplets distincts se trouvent dans AllPairs, nous pourrions utiliser la syntaxe **COUNT(DISTINCT AllPairs.*)**.

Concernant cette dernière sous-requête, nous aurions pu éviter de construire explicitement toutes les paires de villes dans **AllPairs** si nous avions directement effectué le même calcul que dans **AllPairs** – mais en ne renvoyant que **COUNT(*)**. Cela compterait directement toutes les paires de villes présentant les caractéristiques que nous recherchons. Mais nous ne pouvons le faire que si nous codons la requête à l'aide d'un regroupement et d'un comptage, car nous verrons qu'elle peut également être implémentée sur la base d'opérations d'ensemble, pour lesquelles nous devrons nécessairement construire et stocker les paires dans **AllPairs**.

Ainsi, tout comme nous l'avons montré avec d'autres requêtes, nous pouvons également aborder celle-ci en utilisant des **opérateurs de la théorie des ensembles**. Comme vous pouvez le voir ci-dessous, les tables intermédiaires sont construites de la même manière sauf pour **ShipVisits**, où nous n'avons pas besoin que les villes impliquées dans les trajets répondent à la condition d'avoir une superficie < 11.

C'est parce que ces uplets ShipVisits seront plus tard comparés aux paires de villes dans AllPairs, qui, elles, répondent à la condition. De cette façon, nous nous retrouvons avec des croisières qui ont effectué un trajet dans toutes les paires de AllPairs, quels que soient les uplets supplémentaires dans ShipVisits avec des trajets entre des villes qui ne répondent pas à la condition que nous recherchons.

Bien que cela ne soit pas crucial pour résoudre la requête, il est important de noter que ShipVisits contient plus d'uplets que nécessaire, ce qui pourrait ralentir la requête puisque **ShipVisits** sera plus tard utilisé dans une **sous-requête corrélée**, entraînant de multiples scans de ses uplets.

```pgsql
WITH AllPairs AS (
    SELECT C1.CityID AS Dep, C2.CityID AS Arr
    FROM City C1 CROSS JOIN City C2
    WHERE C1.CityID <> C2.CityID AND C1.Area<11 AND C2.Area<11
),
ShipVisits AS (
    SELECT V.ShipFK,
        V.DepartureCityFK AS Dep,
        V.ArrivalCityFK AS Arr
    FROM Voyage V
)
SELECT SV.ShipFK
FROM ShipVisits SV
WHERE NOT EXISTS (
        SELECT *
        FROM AllPairs AP
        WHERE NOT EXISTS (
                SELECT *
                FROM ShipVisits SV2
                WHERE SV2.ShipFK = SV.ShipFK
                    AND SV.Dep = AP.Dep
                    AND SV.Arr = AP.Arr
            )
    );
```

Après avoir construit les CTE, nous résolvons la requête d'une manière similaire aux autres divisions que nous avons vues. D'abord, nous parcourons les uplets de ShipVisits (bien que nous pourrions également choisir de parcourir ceux de CruiseShip, puisque ce que nous voulons, c'est parcourir toutes les croisières de la base de données, ou du moins celles qui ont effectué un trajet). Ainsi, au lieu d'utiliser CruiseShip, qui pourrait contenir des croisières n'ayant jamais effectué de trajet, nous choisissons de parcourir les uplets de ShipVisits, où nous pouvons trouver des croisières référencées par la **clé étrangère ShipFK** de la table **Voyage**, dont nous savons qu'elles ont effectué au moins un trajet.

Dans chacun de ces uplets, nous vérifions qu'il n'y a aucune paire de villes de AllPairs pour laquelle il n'y a pas de trajet effectué par la croisière que nous parcourons actuellement entre les villes de cette paire.

Pour ce faire, nous utilisons l'opérateur NOT EXISTS et deux sous-requêtes corrélées imbriquées. Dans la première, nous parcourons les uplets de AllPairs – c'est-à-dire les paires de villes qui répondent à la condition d'avoir une superficie < 11. Ensuite, pour chaque paire, nous utilisons à nouveau NOT EXISTS sur une autre sous-requête corrélée qui obtient tous les trajets effectués par la croisière actuellement traitée dans l'exécution de la requête sur les villes de la paire correspondante de AllPairs.

De manière plus intuitive, nous obtenons toutes les croisières pour lesquelles il n'y a aucune paire de villes de AllPairs où la croisière n'a pas voyagé au moins une fois. Comme vous pouvez le deviner, puisque les villes de AllPairs répondent à la condition d'avoir une superficie inférieure à 11 km², peu importe que ShipVisits ait des trajets avec des villes qui ne répondent pas à cette condition – car dans la requête, nous vérifions que pour une certaine paire de villes de **AllPairs**, il n'y a pas de trajet d'une croisière dans ces villes. Il est donc réellement indifférent de savoir quelles villes sont présentes dans les trajets de ShipVisits, car celles qui répondent à la condition y seront certainement puisque nous n'imposons aucune condition lors de la construction de cette table intermédiaire.

En résumé, avec cette approche, nous pouvons résoudre la requête tout comme nous l'avons fait auparavant en utilisant des regroupements et des comptages. Mais la différence ici est que nous pouvons économiser les conditions (superficie < 11) que nous avons imposées lors de la construction des uplets de ShipVisits.

À première vue, cela pourrait sembler être une amélioration de la clarté du code, car il est plus court. Cela le rend plus maintenable dans ce cas car moins d'opérations et d'instructions sont nécessaires pour construire la CTE. Mais la CTE résultante contient plus d'uplets, spécifiquement ceux qui représentent tous les trajets effectués par chaque croisière, et pas seulement ceux effectués entre des villes répondant à la condition d'avoir une superficie < 11.

Ce nombre supplémentaire d'uplets a un impact sur le calcul de la requête. Mais pour analyser cet impact, nous devons également considérer que dans la construction de ShipVisits, nous économisons deux opérations JOIN, qui sont très coûteuses, en plus de la quantité de données attendue avec laquelle la requête sera exécutée.

Par exemple, si la quantité de données dans les tables impliquées est faible, la différence de performance ne sera pas notable de manière significative. Mais si elle est importante, il est plus bénéfique d'avoir le plus petit nombre d'uplets possible dans ShipVisits, même si cela nécessite d'effectuer un JOIN supplémentaire.

C'est parce que la sous-requête corrélée qui parcourt les uplets de ShipVisits est exécutée une fois pour chaque uplet de AllPairs, et tout cela est exécuté une fois pour chaque uplet de ShipVisits (nous aurions pu remplacer ce dernier par CruiseShip pour améliorer les performances, car le nombre de croisières est fixe et a tendance à être plus petit que le nombre de trajets).

Ainsi, le calcul impliqué dans le parcours de tous les uplets de ShipVisits est beaucoup plus important que le calcul d'un simple JOIN utilisé pour construire la CTE elle-même – qui, bien qu'étant coûteux en termes de calcul, ne doit être exécuté qu'une seule fois (et non plusieurs fois selon le nombre d'uplets dans d'autres tables).

Pour en finir avec l'opération de division, nous avons vu que nous pouvons l'implémenter en SQL à l'aide de l'opérateur **EXISTS** (soit tel quel, soit nié avec l'opérateur logique NOT) et d'une sous-requête corrélée. Dans celle-ci, l'instruction SELECT utilise la notation * pour renvoyer tous les attributs de la table correspondante. Cela signifie que pour vérifier si la sous-requête renvoie un uplet ou non, nous construisons son résultat de sorte que chaque uplet possède éventuellement plusieurs attributs – c'est-à-dire tous ceux qui résultent de l'utilisation de la notation **SELECT \***. Mais parfois, au lieu de renvoyer plusieurs attributs, elle renvoie simplement une colonne avec une valeur fixe comme l'entier 1.

En général, l'utilisation de la notation SELECT * dans une sous-requête corrélée à laquelle l'opérateur EXISTS est appliqué est considérée comme une bonne pratique, elle est donc codée de cette manière par défaut. Mais il existe également d'autres possibilités comme **SELECT 1**, qui à première vue pourrait sembler plus efficace car elle ne renvoie pas d'attributs inutiles puisqu'elle vérifie seulement si la sous-requête aboutit à un uplet ou non.

En résumé, la décision sur les attributs à renvoyer dans une sous-requête corrélée utilisant l'opérateur EXISTS est principalement déterminée par les caractéristiques du SGBD, car chaque [implémentation](https://dba.stackexchange.com/questions/159413/exists-select-1-vs-exists-select-one-or-the-other) du [SGBD](https://stackoverflow.com/questions/424212/performance-of-sql-exists-usage-variants) gère ces opérations différemment au niveau physique.

### Requêtes de classement (Ranking)

Pour conclure avec les différents "types" de requêtes que nous pourrions rencontrer, il existe des requêtes où nous devons calculer un **classement** – c'est-à-dire ordonner des éléments en fonction de la valeur qu'ils ont pour une certaine métrique. Par exemple, ordonner les personnes par le nombre de locations de vélos qu'elles ont effectuées, nous permettant de savoir qui a effectué le plus ou le moins de locations, parmi de nombreuses autres tâches similaires.

Dans ce cas, ces approches n'ont aucun opérateur équivalent en algèbre relationnelle. En effet, le calcul des classements repose sur la combinaison de multiples techniques et outils comme les regroupements, les agrégations ou les sous-requêtes non corrélées qui ne sont pas présents dans l'algèbre relationnelle en tant qu'opérateurs spécifiques.

C'est principalement parce qu'en algèbre relationnelle, il n'y a pas de concept d'ordre, et puisque les tables sont traitées comme des ensembles d'uplets, il n'y a pas de moyen unique de numéroter les uplets de manière positionnelle pour établir un **ordre interne de l'ensemble**. En d'autres termes, au sein d'un ensemble, ses éléments n'ont pas nécessairement d'ordre entre eux à moins que nous ne le définissions explicitement.

Nous pouvons commencer par trouver la valeur maximale de ce que nous classons (et, éventuellement, où dans la table cela se produit). Par exemple, dans la requête ci-dessous, nous obtenons la capacité maximale de passagers parmi tous les navires de croisière de la table CruiseShip.

```pgsql
SELECT MAX(PassengerCapacity) AS MaxCapacity
FROM CruiseShip;
```

En termes d'approche, la résolution de cette requête implique d'établir un classement des navires de croisière en fonction de leur capacité de passagers (c'est leur métrique). Celui ayant la capacité la plus élevée occupe la première place du classement, suivi des autres navires de croisière. Ainsi, si nous prenons le premier du classement et accédons à sa métrique, nous aurons la capacité maximale de passagers, ce que nous voulons obtenir.

En SQL, l'implémentation de cette requête est très simple si nous voulons seulement obtenir la valeur de la métrique et que ses valeurs sont déjà calculées dans un attribut. Comme vous pouvez le voir, nous utilisons simplement la fonction d'agrégation **MAX()**, à laquelle nous donnons l'attribut où les valeurs de la métrique sont calculées comme argument d'entrée. Enfin, lorsque nous exécutons la requête, nous verrons qu'un seul uplet est renvoyé avec cette valeur maximale dans l'attribut que nous avons nommé avec l'alias **MaxCapacity**.

Mais l'implémentation n'est pas toujours aussi simple. Par exemple, si nous voulons obtenir non seulement la valeur maximale de la métrique mais aussi l'élément spécifique associé à cette métrique – dans ce cas, le navire de croisière ayant la capacité de passagers la plus élevée – nous devons d'abord parcourir les uplets de CruiseShip et vérifier chacun pour voir s'il correspond au navire de croisière ayant la capacité de passagers la plus élevée.

Plus précisément, ce que nous vérifions dans chaque uplet est si le nombre de passagers est égal au maximum ou non, afin de ne conserver que les uplets où la valeur **PassengerCapacity** est exactement égale à la valeur maximale de cet attribut.

```pgsql
SELECT ShipID, PassengerCapacity
FROM CruiseShip
WHERE PassengerCapacity = (
    SELECT MAX(PassengerCapacity)
    FROM CruiseShip
);
```

Ceci est reflété dans le code de la requête ci-dessus. Dans la clause WHERE, nous vérifions que la valeur de l'attribut PassengerCapacity est égale au résultat de la sous-requête non corrélée qui renvoie sa valeur maximale. Nous utilisons pour cela la fonction d'agrégation MAX() tout comme auparavant.

Si les valeurs correspondent, nous aurons trouvé l'uplet du navire de croisière ayant la capacité de passagers la plus élevée. Mais il peut y avoir plusieurs navires de croisière avec cette même capacité, notre requête les renverra donc également.

Si nous voulons obtenir un seul navire de croisière, nous avons la possibilité d'ajouter une clause supplémentaire **LIMIT 1** à la toute fin de la requête, qui renvoie fondamentalement uniquement le premier uplet de la table résultante de la requête.

Cette [clause LIMIT](https://www.datacamp.com/tutorial/sql-limit), ne fait pas partie de la [norme SQL-92](https://www.contrib.andrew.cmu.edu/~shadow/sql/sql1992.txt), mais elle peut toujours être utilisée dans n'importe quelle requête dont nous avons besoin tant que le SGBD la supporte (tous les SGBD **modernes** la supportent). Son utilisation est simple : nous lui donnons simplement un nombre qui indique le nombre d'uplets de la table résultante de la requête que nous voulons obtenir à partir du premier uplet situé en haut de la table, en ignorant le reste.

Une autre option que nous avons est de nous passer de la fonction d'agrégation MAX(). Comme vous pouvez le voir ci-dessous, la majeure partie du code de la requête est la même, sauf pour la sous-requête. Au lieu de renvoyer la valeur maximale de l'attribut PassengerCapacity, elle renvoie l'attribut lui-même – c'est-à-dire toutes les valeurs de sa colonne correspondante dans la table CruiseShip.

```pgsql
SELECT ShipID, PassengerCapacity
FROM CruiseShip
WHERE PassengerCapacity >= ALL (
    SELECT PassengerCapacity
    FROM CruiseShip
);
```

De cette façon, la condition de la clause WHERE utilise l'opérateur >= avec le modificateur ALL, qui établit que, pour un certain uplet de CruiseShip, sa valeur PassengerCapacity doit être supérieure à toutes les valeurs renvoyées par la sous-requête. Ou dit autrement, notre requête récupère des informations sur tous les navires de croisière dont la capacité de passagers est supérieure ou égale à chacune des capacités stockées dans l'attribut PassengerCapacity de la table CruiseShip.

Plus précisément, ici nous devons utiliser l'opérateur **>=,** et non **>**, car si nous parcourons l'uplet d'un navire de croisière qui possède effectivement la capacité de passagers la plus élevée, sa capacité sera au plus égale à la capacité maximale de la table CruiseShip (mais jamais supérieure). C'est-à-dire que si le maximum est une valeur **X**, alors il n'y aura aucun navire de croisière avec une capacité **>X**, mais il y en aura un ou plusieurs avec une capacité **=X**, qui sont ceux que nous voulons trouver.

En même temps, ceux-ci ont une capacité X qui est supérieure au reste des capacités des autres navires de croisière, c'est pourquoi nous utilisons l'opérateur **>=**.

Le modificateur **ALL** est nécessaire pour s'assurer que la valeur de l'attribut PassengerCapacity remplit la condition imposée par l'opérateur >= par rapport à chaque uplet renvoyé par la sous-requête. Dans ce cas, elle ne renvoie que des uplets avec un attribut ou une colonne contenant les valeurs de toutes les capacités de passagers auxquelles elle doit être comparée.

Comme vous pouvez le deviner, même si cette façon d'implémenter la requête est équivalente à la précédente, ici la sous-requête renvoie une série de valeurs qui sont comparées pour chaque uplet de CruiseShip. C'est-à-dire que pour chaque navire de croisière, tous les uplets de la sous-requête sont parcourus pour effectuer la comparaison déclarée dans la clause **WHERE**. Cela nécessite beaucoup plus de calcul que de simplement comparer avec un nombre comme la capacité maximale obtenue à partir de la fonction MAX().

Ainsi, puisque la **sous-requête** est **non corrélée** et n'est calculée qu'une seule fois, il est plus optimal d'utiliser l'approche précédente où nous utilisions MAX() que celle-ci, car cette approche utilise plus d'espace pour stocker les uplets de la sous-requête et plus de temps à les parcourir inutilement pour effectuer les comparaisons.

En continuant avec les requêtes où nous devons calculer un **maximum**, en voici une autre où nous obtenons la personne (ou les personnes) ayant eu le plus de résidences dans des villes, ainsi que ce nombre maximum de résidences.

```pgsql
SELECT R.PersonFK AS PersonID, COUNT(*) AS NumResidences
FROM Residence AS R
GROUP BY R.PersonFK
HAVING COUNT(*) >= ALL (
        SELECT COUNT(*)
        FROM Residence
        GROUP BY PersonFK
    );
```

Nous pouvons trouver les informations pour résoudre cette requête dans la table **Residence** – spécifiquement dans les uplets eux-mêmes, où chacun représente une résidence. La personne est référencée par la clé étrangère **PersonFK** et la ville où la personne a vécu est référencée par la clé étrangère **CityFK**.

Ainsi, dans cette table, nous n'avons pas de nombre dans un attribut qui nous indique le nombre de résidences qu'une personne a eues. Au contraire, les uplets eux-mêmes représentent les résidences des personnes, et nous devons les compter pour savoir quelle personne a ou a eu le plus de résidences.

Pour ce faire, nous pouvons regrouper les uplets de Residence par l'attribut PersonFK, puisque nous devons compter les résidences pour chaque personne. De cette façon, nous formons des groupes d'uplets qui représentent toutes les résidences qu'une personne a eues.

Une fois les groupes constitués, nous pouvons utiliser **COUNT(*)** pour compter combien de résidences la personne "représentative" de ce groupe d'uplets a ou a eues. Ensuite, pour s'assurer que ce nombre est le maximum, nous utilisons l'opérateur >= avec le modificateur ALL et une sous-requête.

Dans ce cas, la sous-requête calcule, pour chaque personne, le nombre total de résidences qu'elle a ou a eues de la même manière que dans la requête principale, en utilisant un regroupement par l'attribut PersonFK de Residence et la fonction d'agrégation COUNT(*).

Grâce à cela, nous pouvons vérifier, dans la clause **HAVING**, que le nombre de résidences d'une certaine personne est supérieur ou égal à tous les nombres de résidences que toutes les personnes présentes dans la table Residence ont ou ont eues.

D'un autre côté, nous pourrions essayer d'implémenter la requête sans utiliser l'opérateur **>=** et le modificateur ALL, et utiliser à la place uniquement une sous-requête non corrélée et la fonction d'agrégation MAX().

```pgsql
SELECT
  R.PersonFK   AS PersonID,
  COUNT(*)     AS NumResidences
FROM Residence AS R
GROUP BY R.PersonFK
HAVING COUNT(*) = (
  SELECT MAX(COUNT(*))
  FROM Residence
  GROUP BY PersonFK
);
```

Comme vous pouvez le voir ci-dessus, la construction de la requête est très similaire, sauf que dans la clause HAVING, nous comparons directement COUNT(*), qui renvoie le nombre de résidences qu'une personne a ou a eues, avec le résultat de la sous-requête, qui semble obtenir le nombre maximum de résidences qu'une personne a eues.

Mais si nous regardons la clause SELECT de la sous-requête, plusieurs fonctions d'agrégation imbriquées comme **MAX(COUNT(*))** apparaissent, dans l'intention de calculer la valeur maximale des nombres de résidences que les gens ont eues. Mais **cela n'est pas autorisé en SQL**. En fait, si nous exécutons la requête, le SGBD nous donnera une erreur car **une fonction d'agrégation ne peut pas être utilisée comme argument d'entrée d'une autre fonction d'agrégation**.

Si nous voulons réellement utiliser la fonction d'agrégation MAX() pour résoudre la requête, nous n'avons pas d'autre choix que de construire d'abord une CTE où nous stockons toutes les personnes ayant déjà eu une résidence et leur nombre respectif de résidences.

Vous pouvez le voir dans le code ci-dessous, et c'est très similaire à l'approche que nous avons suivie auparavant pour résoudre la requête. Cela consiste à regrouper les uplets de résidence par leur attribut de clé étrangère **PersonFK** et à utiliser **COUNT(*)** pour compter combien d'uplets possède chaque groupe, c'est-à-dire combien de résidences possède chaque personne.

```pgsql
WITH ResCount AS (
    SELECT PersonFK AS PersonID, COUNT(*) AS NumResidences
    FROM Residence
    GROUP BY PersonFK
)
SELECT RC.PersonID,
    RC.NumResidences
FROM ResCount RC
WHERE RC.NumResidences = (
        SELECT MAX(NumResidences)
        FROM ResCount
    );
```

Ensuite, une fois cette table intermédiaire **ResCount** construite, nous sommes dans la même situation que dans les requêtes du début de cette section, où les nombres de résidences sont maintenant des valeurs stockées dans un attribut.

Nous pouvons donc suivre l'approche habituelle pour obtenir l'uplet ou les uplets de ResCount ayant la valeur maximale dans leur attribut **NumResidences**. Cela consiste à parcourir tous ses uplets et à vérifier si leur valeur NumResidences correspond au maximum. Nous pouvons facilement calculer cela avec une sous-requête non corrélée et la fonction d'agrégation MAX().

Après ces requêtes, nous pouvons envisager de les résoudre en obtenant l'élément ayant la valeur la plus basse dans sa métrique dans le classement.

Par exemple, dans ce dernier cas, cela correspondrait à trouver la personne ou les personnes ayant eu le moins de résidences (ce qui n'a pas beaucoup de sens dans cette requête, mais en a dans d'autres).

Ainsi, pour calculer des **minimums** au lieu de **maximums** en SQL, vous utilisez exactement les mêmes constructions que nous venons de voir, à la différence que les opérateurs et les fonctions d'agrégation utilisés changent, comme l'opérateur >= en <= et la fonction d'agrégation MIN() est utilisée à la place de MAX().

En plus de calculer des maximums et des minimums, en SQL il est parfois utile de calculer les **positions de classement** des éléments en fonction de la valeur de leurs métriques.

```pgsql
SELECT
  P1.PoolID,
  P1.Name,
  P1.MaxDepth,
  (
    SELECT COUNT(*) + 1
    FROM Pool AS P2
    WHERE P2.MaxDepth > P1.MaxDepth
  ) AS DepthRank
FROM Pool AS P1
ORDER BY DepthRank;
```

Par exemple, dans la requête ci-dessus, nous obtenons une liste de toutes les piscines de la base de données, où pour chacune, nous calculons sa position dans le classement des piscines ordonné par la valeur de son attribut **MaxDepth**, c'est-à-dire par sa profondeur maximale.

De plus, comme il peut y avoir plusieurs piscines avec la même valeur MaxDepth, dans ce cas, les deux piscines auront la même position dans le classement. Ainsi, la position suivante avec une valeur MaxDepth inférieure ne sera pas la position immédiatement suivante – au lieu de cela, vous devez ajouter le nombre de piscines de la position précédente qui avaient la même valeur MaxDepth à cette position de classement.

| **PoolID** | **Nom** | **MaxDepth** | **DepthRank** |
| --- | --- | --- | --- |
| 1 | Sample Pool Name 1 | 5 | 1 |
| 2 | Sample Pool Name 2 | 5 | 1 |
| 3 | Sample Pool Name 3 | 3 | 3 |
| 4 | Sample Pool Name 4 | 2 | 4 |
| 5 | Sample Pool Name 5 | 2 | 4 |

Pour comprendre cela, voici un tableau où vous pouvez voir que les deux premières piscines ont la même position (DepthRank) dans le classement des piscines car elles ont la même valeur MaxDepth. Ensuite, la piscine suivante avec **PoolID=3** a la position 3 dans le classement, car il y a deux piscines avant elle dans le classement. Enfin, les deux piscines suivantes avec **PoolID=4** et **PoolID=5** ont à nouveau la même position dans le classement pour la même raison que précédemment.

Comme nous pouvons le voir, cette façon de définir et de construire le classement n'est pas celle à laquelle nous pourrions nous attendre, où chaque piscine a une position unique. Au lieu de cela, nous modifions légèrement la définition du classement pour permettre aux piscines ayant la même valeur MaxDepth de partager la même position dans le classement, de sorte que l'implémentation SQL ne nécessite pas de fonctions plus avancées.

En ce qui concerne l'implémentation, si nous regardons les attributs de la table d'exemple, spécifiquement **MaxDepth** et sa relation avec **DepthRank**, nous pouvons conclure que la position que nous devrions attribuer à chaque piscine dans le classement correspond au nombre de piscines ayant une MaxDepth strictement supérieure à la sienne **plus 1**.

Par exemple, pour la piscine avec **PoolID=2**, nous voyons qu'il n'y a aucune piscine avec une MaxDepth supérieure à la sienne – tout au plus, il y en a avec une MaxDepth équivalente, mais jamais supérieure car cette piscine a la valeur MaxDepth la plus élevée (c'est-à-dire le maximum). Pendant ce temps, la piscine avec **PoolID=3** a deux piscines avec une MaxDepth supérieure à la sienne.

Ainsi, si nous **ajoutons un** au nombre de piscines ayant une valeur de métrique, qui dans ce cas se trouve dans l'attribut MaxDepth, supérieure à la valeur MaxDepth d'une certaine piscine, alors la quantité que nous obtenons est la position de classement de cette piscine.

Le moyen le plus simple d'implémenter ce calcul en SQL est via une sous-requête corrélée dans le SELECT, où, comme vous pouvez le voir, nous obtenons tous les uplets Pool ayant une MaxDepth supérieure à la piscine sur laquelle nous itérons dans la requête. Et enfin, avec **COUNT(*)+1**, nous ajoutons 1 au nombre d'uplets renvoyés par la sous-requête, générant ainsi la **position** dans le classement de la piscine en cours d'itération dans la requête.

En continuant avec l'idée d'obtenir la position de classement des éléments, nous avons également la possibilité de sélectionner uniquement les éléments ayant une position de classement supérieure ou inférieure à une certaine quantité que nous devons fixer.

```pgsql
SELECT PoolID, Name, MaxDepth
FROM Pool AS P
WHERE (
        SELECT COUNT(*)
        FROM Pool AS P2
        WHERE P2.MaxDepth > P.MaxDepth
    ) < 5
ORDER BY MaxDepth DESC;
```

Par exemple, ci-dessus nous avons une requête où nous obtenons les piscines qui font partie des 5 premières positions distinctes du classement. En d'autres termes, nous n'obtenons pas les 5 premières lignes avec les piscines ordonnées dans le classement selon leur valeur MaxDepth, mais nous obtenons toutes celles dont la position de classement fait partie des 5 premières positions distinctes.

Comme vous pouvez le voir, l'implémentation est simple. Nous parcourons tous les uplets Pool et pour chacun d'eux, nous exécutons une sous-requête comme celle que nous avons vue dans la requête précédente : elle obtient le nombre de piscines ayant une MaxDepth supérieure à la piscine que nous parcourons – c'est-à-dire sa position dans le classement. Ensuite, nous comparons ce nombre avec 5 pour nous assurer qu'il est strictement inférieur.

De plus, ici nous devons noter que nous n'avons pas ajouté 1 à **COUNT(*)**, ce qui signifie que le classement commence à compter à la **position 0**, et non 1, afin que nous puissions ensuite vérifier que la position fait partie des 5 premières distinctes avec < 5 et non < 6. Cela ne doit pas nécessairement être fait de cette façon, car nous aurions pu ajouter 1 à **COUNT(*)** et déclarer la comparaison en utilisant **<6**, ou **<=5**.

En résumé, dans cette requête, nous avons utilisé une sous-requête corrélée pour obtenir la position de classement (en commençant par la position 0) de chaque piscine, de sorte que nous ne conservons que celles dont la position est strictement inférieure à 5. Mais nous aurions également pu pré-calculer les positions de chaque piscine dans une CTE puis appliquer cette condition à un attribut au lieu de la valeur renvoyée par une sous-requête.

Cette alternative utilisera probablement plus de mémoire que nécessaire, puisque le calcul de l'exécution de la sous-requête qui calcule la position de classement sera présent que nous utilisions une CTE ou non. L'approche la plus optimale consisterait donc à éviter de gaspiller de la mémoire à moins que nous n'ayons réellement besoin d'une table intermédiaire avec cette information pour d'autres utilisations.

Nous avons donc maintenant vu une série de requêtes qui suivent certains modèles qui sont les plus basiques et fondamentaux en SQL. Mais il existe de nombreuses autres requêtes que nous pourrions effectuer sur le schéma de cet exemple avec une grande variété d'objectifs. Celles-ci sont **essentielles** à savoir formuler et coder.

Pour en apprendre davantage sur les requêtes, vous pouvez consulter la ressource suivante : **PostgreSQL.ipynb**.

%[https://github.com/cardstdani/sql-storage/blob/main/PostgreSQL.ipynb] 

Il s'agit d'un notebook Jupyter que vous pouvez exécuter depuis Google Colab. Il contient du code Python et des commandes Bash qui vous permettent d'installer le **SGBD PostgreSQL** sur une **machine virtuelle Linux** comme celles utilisées par [Google Compute Engine](https://cloud.google.com/products/compute) (le backend de Google Colab). Vous pouvez également exécuter du code SQL pour créer la base de données à partir du DDL, puis exécuter des requêtes et obtenir leurs résultats.

Le notebook contient une série d'énoncés de requêtes avec des solutions, ainsi que tout le nécessaire pour les exécuter. Ces requêtes ne sont pas ordonnées ou classées comme celles que nous avons vues dans le dernier chapitre, car le but est que vous essayiez de les résoudre à partir des énoncés sans regarder la solution. De cette façon, vous pourrez voir plus tard comment elles ont été résolues et gagner de l'expérience dans la formulation de requêtes, qui est l'une des compétences les plus précieuses pour fournir des services aux utilisateurs finaux à partir de la base de données.

Vous n'êtes pas obligé de le faire dans un environnement Google Colab – vous pouvez également le faire sur une installation PostgreSQL sur une **machine locale** et exécuter les requêtes en copiant et collant le code de la requête dans le terminal PostgreSQL. Mais le faire dans un environnement distant comme celui proposé par Google Colab présente certains avantages, comme ne pas avoir à se soucier d'installer quoi que ce soit manuellement, puisque tout est configuré automatiquement en exécutant simplement les cellules de code ou en pouvant voir le texte des énoncés dans le notebook rendu avec markdown.

Pourtant, il y a certains inconvénients, comme le fait que la base de données soit stockée sur une machine virtuelle Google, ce qui signifie que vous n'avez pas le contrôle total sur la machine et l'environnement dans lequel le SGBD s'exécute. Son exécution peut également être interrompue selon la façon dont vous utilisez la machine virtuelle et le forfait que vous avez avec Google Colab.

Ainsi, même s'il ne s'agit peut-être pas d'un environnement où vous pouvez déployer une base de données de production entièrement fonctionnelle, il est suffisamment similaire à un environnement réel où vous pourriez avoir une base de données déployée pour un projet, ce qui rend le travail dans Google Colab intéressant.

## Conclusion

Dans ce livre, nous avons couvert tous les concepts clés que vous devez connaître pour concevoir une base de données, sur la base de certaines exigences, pour un projet logiciel.

Mais encore une fois, ces concepts et commandes ne sont que les plus basiques et fondamentaux. Pour en savoir plus sur la conception de bases de données SQL, consultez également d'autres ressources comme des livres de référence, des articles ou les nombreuses ressources disponibles sur Internet.

Votre objectif devrait être d'acquérir une compréhension plus profonde de ce que vous avez appris ici. Cela vous aidera à concevoir des bases de données robustes selon les exigences des clients et à coder des requêtes encore plus efficaces.

Merci de votre lecture !