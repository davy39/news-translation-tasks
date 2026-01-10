---
title: Une introduction animée à SQL – Apprendre à interroger des bases de données
  relationnelles
subtitle: ''
author: Mark Mahoney
co_authors: []
series: null
date: '2025-04-16T15:43:24.941Z'
originalURL: https://freecodecamp.org/news/an-animated-introduction-to-sql-learn-to-query-relational-databases
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744818155429/10b16956-a249-4815-b50a-594b58330a01.png
tags:
- name: SQL
  slug: sql
- name: SQLite
  slug: sqlite
seo_title: Une introduction animée à SQL – Apprendre à interroger des bases de données
  relationnelles
seo_desc: 'In this tutorial, you’ll learn about the Structured Query Language (SQL),
  the standard language used to query relational databases.

  SQL is not a traditional programming language. In Python or Java, you write step-by-step
  instructions that tell the co...'
---

Dans ce tutoriel, vous apprendrez le [Structured Query Language (SQL)](https://www.freecodecamp.org/news/what-is-sql-database-definition-for-beginners/), le langage standard utilisé pour interroger les bases de données relationnelles.

SQL n'est pas un langage de programmation traditionnel. En Python ou Java, vous écrivez des instructions étape par étape qui indiquent à l'ordinateur exactement **comment** faire quelque chose. Cela s'appelle la programmation **impérative**.

SQL fonctionne différemment. D'abord, vous comprenez quelles données sont stockées dans vos tables. Ensuite, vous écrivez une requête décrivant **quelles** données vous voulez et vous la donnez à un système de gestion de base de données. Le système de gestion de base de données détermine **comment** les obtenir. Ce style **déclaratif** fait partie de ce qui rend SQL puissant (et amusant à utiliser).

Vous n'avez pas besoin d'être programmeur pour apprendre SQL, mais avoir une certaine expérience en programmation aide. Des concepts comme la logique conditionnelle et la comparaison de valeurs pour voir si quelque chose est vrai ou faux vous sembleront familiers si vous avez déjà codé.

Si vous voulez une introduction aux bases, consultez certains de mes tutoriels sur les langages de programmation listés ci-dessous.

## **Structure du tutoriel**

Ce tutoriel est construit autour de trois livres de replay de code interactifs que j'utilise dans mes cours sur les bases de données :

* [Conception de bases de données et SQL pour débutants](https://playbackpress.com/books/sqlbook)

* [Exemples pratiques de SQL](https://playbackpress.com/books/workedsqlbook)

* [Programmation avec SQLite](https://playbackpress.com/books/sqlitebook)

Chaque section de ce tutoriel inclut des exemples pratiques où je montre comment j'écris du SQL étape par étape, en expliquant mon processus de réflexion. Vous me verrez expérimenter, affiner et construire des requêtes pièce par pièce, comme le ferait un vrai développeur. Je m'appuie fortement sur les diagrammes entité-relation et les schémas pour m'aider à visualiser les données stockées dans les bases de données.

Voici comment le tutoriel est organisé :

### **Partie 1 : Un tour d'horizon de SQL**

(issu de [Conception de bases de données et SQL pour débutants](https://playbackpress.com/books/sqlbook))

Je commence par explorer une base de données simple pour un centre d'adoption d'animaux fictif appelé *Paw Prints Adoption Center*. J'introduis des concepts essentiels comme :

* Les diagrammes entité-relation (ER)

* Les schémas

* La structure des tables et les relations

Cette fondation prépare le terrain pour tout ce qui suit. Si vous êtes nouveau dans la conception de bases de données, passez un peu de temps ici avant de continuer.

### **Partie 2 : Concepts et mots-clés SQL de base**

(également issu de [Conception de bases de données et SQL pour débutants](https://playbackpress.com/books/sqlbook))

Je couvre les mots-clés et idées SQL les plus importants. Chaque sujet est expliqué dans son propre replay avec des exemples :

* `CREATE TABLE`, `ALTER TABLE`

* `SELECT`, `FROM`, `WHERE`, `JOIN`

* `ORDER BY`, `GROUP BY`, `HAVING`

* `INSERT`, `UPDATE`, `DELETE`

* Les requêtes imbriquées, les expressions de table communes et les opérations d'ensemble (`UNION`, `INTERSECT`, `EXCEPT`)

* Les index et les transactions

Cette section fonctionne comme une référence. Si vous êtes bloqué sur une requête ou si vous avez oublié ce que fait un mot-clé, revenez ici.

### **Partie 3 : Problèmes pratiques**

(issu de [Exemples pratiques de SQL](https://playbackpress.com/books/workedsqlbook))

La pratique est la meilleure façon d'apprendre. J'ai inclus 36 problèmes pratiques utilisant la base de données Paw Prints et une nouvelle base de données universitaire. Chaque problème a un replay animé montrant comment j'ai travaillé à travers la solution étape par étape.

Essayez d'écrire votre propre requête avant de regarder la solution. Lutter avec le problème d'abord vous aidera à apprendre beaucoup plus que simplement me regarder fournir la réponse.

Ces problèmes développent vos compétences progressivement et aident à renforcer l'utilisation des diagrammes ER et des schémas dans des scénarios réels.

### **Partie 4 : Utilisation de SQLite dans les programmes**

(issu de [Programmation avec SQLite](https://playbackpress.com/books/sqlitebook))

Dans cette dernière section optionnelle, je montre comment connecter SQL à du vrai code. Vous apprendrez comment utiliser la base de données [SQLite](https://sqlite.org/) dans :

* C/C++

* Python et Flask

* Java

### **Exécution de requêtes**

Un système de gestion de base de données (SGBD) est le logiciel utilisé pour gérer et interroger les données dans une base de données. De nombreux SGBD nécessitent une configuration significative et souvent un serveur séparé pour répondre aux requêtes. Configurer ceux-ci peut être difficile pour les nouveaux venus.

[SQLite](https://sqlite.org/) est un SGBD simple qui ne nécessite pas beaucoup de configuration. C'est un excellent outil pour commencer. Il n'a pas besoin d'un serveur autonome et stocke l'ensemble de la base de données dans un seul fichier.

Pour faciliter la visualisation et l'édition de vos bases de données, je recommande d'utiliser [DB Browser for SQLite](https://sqlitebrowser.org/). C'est un outil gratuit et open-source avec une interface simple et toutes les fonctionnalités de SQLite intégrées. Vous pouvez ouvrir des fichiers de base de données, parcourir des tables, exécuter des requêtes et éditer des données en utilisant une interface utilisateur intuitive. Il est particulièrement utile lorsque vous apprenez et que vous voulez voir rapidement comment vos requêtes affectent les données.

### **Alternative basée sur le Web à DB Browser**

Si vous préférez ne pas installer de logiciel, vous pouvez utiliser un outil basé sur le Web comme [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) ou [SQLite Online](https://sqliteonline.com/). Ceux-ci vous permettent de télécharger un fichier `.sqlite`, d'exécuter des requêtes et d'explorer une base de données depuis votre navigateur.

* [SQLite Viewer](https://inloop.github.io/sqlite-viewer/) : Un visualiseur simple, en lecture seule. Bon pour inspecter les tables et tester des requêtes de base.

* [SQLite Online](https://sqliteonline.com/) : Un IDE SQLite complet. Vous pouvez créer des bases de données, télécharger des fichiers, exécuter des requêtes et même sauvegarder votre travail.

Les deux outils sont excellents pour des expériences rapides ou pour vérifier votre travail sans installer quoi que ce soit.

### **Replays de code**

Ce tutoriel n'est pas une vidéo traditionnelle ou un texte statique. Chaque section inclut des liens vers des **replays de code** interactifs qui animent comment le code ou la requête a été construit, étape par étape. Vous pouvez mettre en pause et revenir en arrière pour voir chaque changement au fur et à mesure.

Chaque replay inclut un récit, des captures d'écran, des dessins de type tableau blanc et des questions à choix multiples auto-évaluées pour renforcer ce que vous avez appris.

Si vous n'avez jamais vu un replay de code auparavant, ne vous inquiétez pas. Ils sont faciles à utiliser et vous permettent de voir comment les requêtes évoluent au fil du temps. Voici une courte vidéo montrant comment visualiser un replay de code :

%[https://youtu.be/uYbHqCNjVDM]

### **Playback Press**

[Playback Press](https://playbackpress.com/books) est la plateforme où je publie mes parcours de code interactifs. Chaque livre inclut des animations étape par étape, un tutorat IA et des quiz intégrés.

J'ai également créé [Storyteller](https://markm208.github.io/), l'outil gratuit et open-source qui alimente ces replays.

### **Tuteur IA**

Pendant que vous visualisez un replay de code, vous pouvez poser des questions à un tuteur IA sur les requêtes. Il donne des réponses claires et ciblées et ne vous presse pas. Vous pouvez également lui demander de créer de nouvelles questions à choix multiples auto-évaluées pour tester votre compréhension.

Pour utiliser le tuteur IA et les quiz, créez un compte gratuit sur Playback Press et ajoutez l'un des livres à votre bibliothèque.

## **Table des matières**

* [Partie 1 : Un tour d'horizon de SQL](#heading-partie-1-un-tour-dhorizon-de-sql-1)

* [Partie 2 : Une référence pour débutants à SQL](#heading-partie-2-une-reference-pour-debutants-a-sql)

* [Partie 3 : Problèmes pratiques — Bases de données Paw Prints et Université](#heading-partie-3-problemes-pratiques-bases-de-donnees-paw-prints-et-universite)

* [Partie 4 : Utilisation de SQLite dans les programmes](#heading-partie-4-utilisation-de-sqlite-dans-les-programmes-1)

* [Conclusion](#heading-conclusion)

* [Commentaires et retours](#heading-commentaires-et-retours)

## **Partie 1 : Un tour d'horizon de SQL**

Quand on demande à quelqu'un de gérer des données, la première réaction de la plupart des gens est d'utiliser un tableur. Les tableurs sont faciles à utiliser et flexibles. Mais à mesure que vos données deviennent plus complexes, ils commencent à montrer certaines faiblesses.

Un problème majeur est la redondance des données. Quand la même information apparaît à plusieurs endroits, il y a un risque qu'une copie change tandis que les autres restent les mêmes. Cela peut conduire à des incohérences, des erreurs et des résultats confus.

Les bases de données relationnelles aident à résoudre ce problème en organisant les données de manière structurée qui réduit la redondance par conception. Avant de construire une base de données, il est utile de modéliser les données en utilisant un diagramme entité-relation (ER).

### **Diagrammes entité-relation**

Un diagramme ER est un outil de planification utilisé pour visualiser la structure d'une base de données. Il vous aide à déterminer quels types de données vous devez stocker et comment ces morceaux de données sont liés les uns aux autres.

* Les **entités** sont les principaux objets ou concepts de votre système, comme `Personne`, `Cours` ou `Chien`. Les entités ont des attributs qui les décrivent. Une `Personne` peut avoir des attributs `nom`, `date de naissance` et `adresse`, par exemple.

* Les **relations** décrivent comment les entités sont connectées. Par exemple, une `Personne` peut *adopter* un `Chien`, ou un `Étudiant` peut *s'inscrire* à un `Cours`.

En disposant cela dans un diagramme, vous pouvez clairement voir quelles données sont stockées et comment les entités sont liées les unes aux autres. Cela facilite la conception correcte des tables dans votre base de données.

Voici un exemple de diagramme ER utilisé dans cette partie du tutoriel :

![Un diagramme entité-relation pour la base de données Paw Prints](https://cdn.hashnode.com/res/hashnode/image/upload/v1744664220972/dc57e1fa-bad9-42b0-9158-0f2649c4f282.png align="center")

### **Schéma**

Un **schéma** est une autre façon de décrire la structure d'une base de données. Il montre les mêmes informations que le diagramme ER, mais dans un format plus technique et précis, axé sur la manière dont les données seront réellement stockées. Chaque élément d'un schéma deviendra une table dans une base de données.

Au lieu de lignes reliant des boîtes, un schéma utilise des clés primaires et des clés étrangères :

* Une **clé primaire** identifie de manière unique chaque ligne dans une table. Les clés primaires ont un soulignement solide.

* Une **clé étrangère** fait référence à la clé primaire dans une autre table, reliant les deux ensemble. Les clés étrangères ont un soulignement en pointillés.

Voici un exemple de schéma utilisé dans cette partie du tutoriel :

![Un schéma pour la base de données Paw Prints](https://cdn.hashnode.com/res/hashnode/image/upload/v1744664247677/146dff90-e366-4ba2-b584-07d5ff42cca9.jpeg align="center")

Alors qu'un diagramme ER est plus visuel et conceptuel, un schéma est plus concret et plus proche de l'implémentation réelle dans le SGBD. Vous verrez les deux utilisés tout au long de ce tutoriel alors que je passe de la planification à l'écriture de SQL.

### **Essayez-le : Explorez une base de données relationnelle en action**

Pour voir comment ces concepts fonctionnent en pratique, jetez un coup d'œil aux trois replays de code suivants. Ils parcourent la conception d'une base de données relationnelle pour un centre d'adoption d'animaux fictif appelé **Paw Prints**. Ces exemples vous aideront à comprendre comment les entités, les relations et les schémas se combinent dans une base de données réelle et comment écrire des requêtes SQL simples pour explorer ces données.

Commencez par le premier replay et parcourez les trois dans l'ordre :

1. #### [**Conception de base de données et SQL simple**](https://playbackpress.com/books/sqlbook/chapter/1/1) : Présente la base de données Paw Prints et montre comment écrire des requêtes SQL de base.

2. #### [**Relations un-à-plusieurs et plus de SQL**](https://playbackpress.com/books/sqlbook/chapter/1/2) : Couvre les relations un-à-plusieurs et comment joindre des tables liées.

3. #### [**Relations plusieurs-à-plusieurs et encore plus de SQL**](https://playbackpress.com/books/sqlbook/chapter/1/3) : Montre comment gérer les relations plusieurs-à-plusieurs en utilisant des tables de jointure et des requêtes plus avancées.

Pendant que vous regardez, faites des pauses pour vous assurer de comprendre comment les données sont structurées et comment chaque requête SQL est écrite. Vous pouvez toujours vous référer à cette section plus tard si quelque chose dans les prochains chapitres n'est pas clair.

## **Partie 2 : Une référence pour débutants à SQL**

Cette section examine de plus près les commandes SQL de base introduites dans le tour d'horizon. Chaque replay se concentre sur un sujet et montre comment l'utiliser à travers des exemples étape par étape. Je continue à utiliser la base de données Paw Prints dans ces exemples.

Considérez cela comme une section de référence. Vous n'avez pas besoin de tout parcourir dans l'ordre, mais vous pourriez vouloir tout parcourir au moins une fois avant de commencer à pratiquer dans la partie 3. Revenez ici chaque fois que vous avez besoin d'un rappel sur un concept SQL particulier.

Voici les concepts clés que nous allons couvrir :

#### [**CREATE TABLE et ALTER TABLE**](https://playbackpress.com/books/sqlbook/chapter/2/1)

Apprenez à définir des tables dans une base de données relationnelle. Ce replay montre comment créer des tables à partir de zéro et comment les modifier plus tard en utilisant `ALTER TABLE`.

#### [**INSERT**](https://playbackpress.com/books/sqlbook/chapter/2/2)

Voyez comment ajouter de nouvelles lignes de données à une table. Cet exemple montre comment utiliser la commande `INSERT` et s'assurer que vos données correspondent à la structure de la table.

#### [**SELECT**](https://playbackpress.com/books/sqlbook/chapter/2/3)

Ce replay introduit le mot-clé `SELECT` en SQL. Vous apprendrez à récupérer des colonnes spécifiques (ou attributs) d'une table et verrez à quoi ressemble l'ensemble de résultats.

#### [**FROM**](https://playbackpress.com/books/sqlbook/chapter/2/4)

Explorez comment la clause `FROM` spécifie les tables à partir desquelles proviennent vos données. Cela prépare le terrain pour combiner des données de plusieurs sources en utilisant un produit cartésien. Vous verrez également comment `JOIN` des tables ensemble.

#### [**WHERE**](https://playbackpress.com/books/sqlbook/chapter/2/5)

Apprenez à filtrer les résultats en utilisant des conditions. La clause `WHERE` aide à réduire les lignes retournées par une requête. Ce replay montre également comment joindre des tables en faisant correspondre des clés étrangères à des clés primaires.

#### [**UPDATE et DELETE**](https://playbackpress.com/books/sqlbook/chapter/2/6)

Apprenez à modifier les données existantes dans la base de données avec `UPDATE` et à supprimer des données en utilisant `DELETE`. Vous verrez également comment éviter les changements accidentels en utilisant soigneusement les conditions `WHERE`.

#### [**ORDER BY**](https://playbackpress.com/books/sqlbook/chapter/2/7)

Triez vos résultats en utilisant `ORDER BY`. Vous apprendrez à contrôler l'ordre de votre sortie en utilisant un ou plusieurs attributs.

#### [**Opérateurs d'agrégation, GROUP BY et HAVING**](https://playbackpress.com/books/sqlbook/chapter/2/8)

Groupez les lignes et calculez des valeurs de synthèse en utilisant des fonctions d'agrégation comme `COUNT`, `AVG`, `MIN`, `MAX` et `SUM`. Ce replay montre également comment utiliser `GROUP BY` et `HAVING` pour travailler avec des résultats groupés.

#### [**Requêtes imbriquées avec IN et expressions de table communes**](https://playbackpress.com/books/sqlbook/chapter/2/9)

Apprenez à utiliser des requêtes imbriquées - des requêtes à l'intérieur d'autres requêtes - pour construire une logique plus flexible. Ce replay montre également comment écrire des requêtes plus propres en utilisant des expressions de table communes (CTE).

#### [**UNION, INTERSECT, EXCEPT**](https://playbackpress.com/books/sqlbook/chapter/2/10)

Voyez comment combiner les résultats de plusieurs requêtes. Cet exemple montre comment `UNION`, `INTERSECT` et `EXCEPT` vous aident à travailler avec des données de différentes requêtes comme si c'était un seul ensemble.

#### [**Transactions**](https://playbackpress.com/books/sqlbook/chapter/2/11)

Apprenez à regrouper plusieurs commandes SQL en une seule **transaction**, afin qu'elles réussissent ou échouent toutes ensemble. Les transactions aident à protéger vos données contre les mises à jour partielles.

#### [**CREATE INDEX**](https://playbackpress.com/books/sqlbook/chapter/2/12)

Améliorez les performances des requêtes en utilisant des index. Ce replay montre comment créer un index sur une ou plusieurs colonnes et explique pourquoi cela rend certaines requêtes plus rapides.

## **Partie 3 : Problèmes pratiques — Bases de données Paw Prints et Université**

Il est maintenant temps d'appliquer ce que vous avez appris.

Voici six problèmes pratiques qui utilisent la base de données Paw Prints des exemples précédents. Si vous ne l'avez pas recréée vous-même, voici un lien vers le fichier SQLite [dogsFinal.sqlite](https://markm208.github.io/sqlbook/dogsFinal.sqlite). Chacun pose une question spécifique qui nécessite d'écrire une requête SQL pour trouver la réponse. Essayez de résoudre chacun par vous-même avant de regarder la solution.

Ne vous inquiétez pas si vous ne réussissez pas du premier coup. Écrire du SQL implique souvent des essais et des erreurs, même pour les développeurs expérimentés. Le but est de réfléchir au problème et de progresser, pas d'être parfait. Commencez petit et construisez vos requêtes par un processus itératif.

Cliquez sur chaque lien pour visualiser le replay après avoir fait votre tentative :

1. #### [**Quels chiens ont eu le plus de visites ?**](https://playbackpress.com/books/sqlbook/chapter/3/1)

Découvrez comment compter les visites pour chaque chien et les trier pour trouver les plus fréquemment visités.

2. #### [**Nombre d'adoptions et âge moyen**](https://playbackpress.com/books/sqlbook/chapter/3/2)

Trouvez le nombre total d'adoptions et l'âge moyen des chiens adoptés. Vous devrez filtrer les données de manière appropriée.

3. #### [**Lieux avec le moins/plus de chiens agressifs**](https://playbackpress.com/books/sqlbook/chapter/3/3)

Utilisez le regroupement pour comparer les niveaux d'agressivité entre les lieux et déterminer où se trouvent le plus et le moins de chiens agressifs.

4. #### [**Temps moyen d'adoption par lieu**](https://playbackpress.com/books/sqlbook/chapter/3/4)

Calculez le temps moyen nécessaire pour que les chiens soient adoptés, ventilé par lieu.

5. #### [**Trouver la capacité disponible à chaque lieu**](https://playbackpress.com/books/sqlbook/chapter/3/5)

Déterminez combien d'espace reste à chaque lieu de refuge en comparant la capacité totale à l'occupation actuelle.

6. #### [**Qui a visité puis adopté un chien agressif**](https://playbackpress.com/books/sqlbook/chapter/3/6)

Cette requête complexe vous demande de suivre les actions des utilisateurs au fil du temps, d'abord en visitant, puis en adoptant un chien agressif. Un bon défi !

### **Base de données universitaire**

Ensuite, vous travaillerez avec une base de données plus complexe qui modélise le système de cours et de notation d'une université. Vous l'utiliserez pour analyser les relations du monde réel entre les étudiants, les professeurs, les cours et les départements.

Téléchargez la version SQLite de la base de données ici :
[studentGrades.sqlite](https://markm208.github.io/workedsqlbook/studentGrades.sqlite)

Voici les **entités** de la base de données :

* `Étudiants`

* `Sections`

* `Cours`

* `Professeurs`

* `Départements`

Et voici les **relations** entre eux :

* Chaque étudiant suit zéro ou plusieurs sections. (Chaque étudiant reçoit une note.)

* Chaque section a zéro ou plusieurs étudiants qui la suivent.

* Chaque section est une instance d'un cours.

* Chaque cours a zéro ou plusieurs sections.

* Chaque section est enseignée par un seul professeur.

* Chaque professeur enseigne zéro ou plusieurs sections.

* Chaque professeur appartient à zéro ou plusieurs départements.

* Chaque département a zéro ou plusieurs professeurs.

* Chaque département a, au plus, un professeur qui en est le président.

* Chaque professeur peut présider, au plus, un département.

* Chaque cours est offert par un département.

* Chaque département offre zéro ou plusieurs cours.

Les replays de code mettent en évidence comment j'utilise les **diagrammes ER** et les **schémas** pour m'aider à construire mes requêtes. Vous pouvez les prévisualiser ici :

![Un diagramme entité-relation pour la base de données universitaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1744665047915/c0c0c31a-8463-4d01-a15c-930d6e24b574.jpeg align="center")

![Un schéma pour la base de données universitaire](https://cdn.hashnode.com/res/hashnode/image/upload/v1744665070077/fd9c60be-0140-4281-ba8c-a3216001a043.jpeg align="center")

Essayez chaque requête par vous-même avant de regarder la solution.

7. #### [**Lister chaque nom de cours, numéro de section et nom de professeur par ordre chronologique pour chaque section qui a déjà été offerte**](https://playbackpress.com/books/workedsqlbook/chapter/1/1)

8. #### [**Lister chaque nom de cours et numéro de section pour chaque cours offert par le département d'informatique**](https://playbackpress.com/books/workedsqlbook/chapter/1/2)

9. #### [**Trouver le nom de chaque professeur qui a déjà enseigné CSCI111**](https://playbackpress.com/books/workedsqlbook/chapter/1/3)

10. #### [**Lister tous les noms de professeurs et leurs départements**](https://playbackpress.com/books/workedsqlbook/chapter/1/4)

11. #### [**Lister les noms des professeurs qui ont enseigné à la fois CSCI111 et CSCI112**](https://playbackpress.com/books/workedsqlbook/chapter/1/5)

12. #### [**Lister les noms de tous les étudiants de professeur Mark Mahoney qui ont 21 ans ou plus**](https://playbackpress.com/books/workedsqlbook/chapter/2/1)

13. #### [**Lister les noms de tous les étudiants qui sont enseignés par un président de département**](https://playbackpress.com/books/workedsqlbook/chapter/2/2)

14. #### [**Lister tous les noms de cours et numéros de section de chaque cours jamais enseigné par un président de département**](https://playbackpress.com/books/workedsqlbook/chapter/2/3)

15. #### [**Lister tous les cours avec l'étudiant le plus âgé**](https://playbackpress.com/books/workedsqlbook/chapter/2/4)

16. #### [**Lister tous les cours et numéros de section avec l'âge moyen des étudiants le plus jeune**](https://playbackpress.com/books/workedsqlbook/chapter/2/5)

17. #### [**Lister tous les noms de cours et numéros de section des cours avec moins de quatre crédits**](https://playbackpress.com/books/workedsqlbook/chapter/3/1)

18. #### [**Lister tous les noms de cours et numéros de section avec l'inscription la plus faible**](https://playbackpress.com/books/workedsqlbook/chapter/3/2)

19. #### [**Lister tous les noms d'étudiants qui ont suivi plus d'un cours avec Mark Mahoney**](https://playbackpress.com/books/workedsqlbook/chapter/3/3)

20. #### [**Lister tous les noms d'étudiants qui ont suivi un cours avec Mark Mahoney et Eric Whendon**](https://playbackpress.com/books/workedsqlbook/chapter/3/4)

21. #### [**Lister tous les noms de cours et numéros de section qui ont eu deux étudiants ou plus obtenir des A**](https://playbackpress.com/books/workedsqlbook/chapter/3/5)

22. #### [**Trouver les noms de tous les étudiants qui ont suivi CSCI111**](https://playbackpress.com/books/workedsqlbook/chapter/4/1)

23. #### [**Trouver les noms de tous les professeurs du département d'informatique qui ne sont pas présidents de département**](https://playbackpress.com/books/workedsqlbook/chapter/4/2)

24. #### [**Trouver les noms de tous les professeurs qui sont présidents de département**](https://playbackpress.com/books/workedsqlbook/chapter/4/3)

25. #### [**Trouver le numéro de sécurité sociale, le prénom et le nom, le nom du cours et la note obtenue pour tous les cours suivis au printemps 2007**](https://playbackpress.com/books/workedsqlbook/chapter/4/4)

26. #### [**Trouver le nom du cours et le numéro de section de tous les cours qui ont déjà été offerts à l'automne**](https://playbackpress.com/books/workedsqlbook/chapter/4/5)

27. #### [**Trouver les noms de tous les professeurs enseignant au printemps 2007**](https://playbackpress.com/books/workedsqlbook/chapter/5/1)

28. #### [**Trouver les noms de tous les étudiants qui ont reçu un A et un B dans un cours quelconque**](https://playbackpress.com/books/workedsqlbook/chapter/5/2)

29. #### [**Découvrir combien d'étudiants ont déjà suivi CSCI111**](https://playbackpress.com/books/workedsqlbook/chapter/5/3)

30. #### [**Trouver l'âge moyen de tous les étudiants qui ont déjà eu un cours avec Mark Mahoney**](https://playbackpress.com/books/workedsqlbook/chapter/5/4)

31. #### [**Trouver les noms de tous les professeurs qui n'ont jamais enseigné un cours**](https://playbackpress.com/books/workedsqlbook/chapter/5/5)

32. #### [**Trouver les noms de tous les professeurs qui ont enseigné à May Jones**](https://playbackpress.com/books/workedsqlbook/chapter/6/1)

33. #### [**Trouver les noms des étudiants qui ont eu un cours à l'automne 2006 ou au printemps 2007**](https://playbackpress.com/books/workedsqlbook/chapter/6/2)

34. #### [**Trouver les noms des étudiants qui ont suivi un cours avec un professeur qui a plus d'une nomination dans un département**](https://playbackpress.com/books/workedsqlbook/chapter/6/3)

35. #### [**Trouver l'âge moyen des étudiants qui ont suivi des cours au printemps 2007**](https://playbackpress.com/books/workedsqlbook/chapter/6/4)

36. #### [**Trouver la somme de toutes les heures de crédit offertes par le département d'informatique en 2007**](https://playbackpress.com/books/workedsqlbook/chapter/6/5)

## **Partie 4 : Utilisation de SQLite dans les programmes**

Jusqu'à présent, vous avez appris à écrire des requêtes SQL et à concevoir des bases de données relationnelles. Dans cette section optionnelle, vous verrez comment utiliser SQLite dans du vrai code. Chaque replay parcourt un programme fonctionnel qui lit et écrit dans une base de données SQLite.

### **Pourquoi utiliser SQLite dans les programmes ?**

La simplicité de SQLite en fait un excellent choix pour des projets rapides, des prototypes et des petites applications. Vous n'avez pas besoin de faire tourner un serveur, et tout est stocké dans un seul fichier.

Ces replays montrent comment intégrer SQL directement dans votre code, afin que vos programmes puissent stocker et récupérer des données dans le cadre de leur flux de travail normal. J'adore vraiment l'utiliser dans mes projets !

Voici un aperçu des replays :

### **C/C++**

1. #### [**L'API C++ SQLite**](https://playbackpress.com/books/sqlitebook/chapter/2/1)

Montre comment configurer et utiliser l'API C++ SQLite. Vous ouvrirez une base de données, exécuterez des requêtes de base et traiterez les résultats.

2. #### [**Un programme d'enchères orienté objet**](https://playbackpress.com/books/sqlitebook/chapter/2/2)

Conçoit un programme C++ plus complexe qui suit les enchères, les articles et les utilisateurs. Cet exemple montre comment structurer une application du monde réel avec SQLite.

3. #### [**Transactions SQLite**](https://playbackpress.com/books/sqlitebook/chapter/2/3)

Explique comment regrouper plusieurs opérations de base de données en une seule transaction. Cela protège vos données contre les mises à jour partielles.

### **Python et Flask**

1. #### [**Interrogation d'une base de données SQLite**](https://playbackpress.com/books/sqlitebook/chapter/3/1)

Connecte un script Python à une base de données SQLite, exécute des requêtes et traite les résultats en utilisant les bibliothèques intégrées de Python.

2. #### [**Création de bases de données SQLite**](https://playbackpress.com/books/sqlitebook/chapter/3/2)

Montre comment créer de nouvelles bases de données SQLite directement à partir de Python, en définissant des tables et en insérant des données initiales.

3. #### [**Bases de Flask**](https://playbackpress.com/books/sqlitebook/chapter/3/3)

Introduit Flask. Vous verrez comment construire une application web simple qui peut servir des pages et se connecter à votre base de données SQLite.

4. #### [**Création d'une API**](https://playbackpress.com/books/sqlitebook/chapter/3/4)

Va plus loin avec Flask en créant une API RESTful qui interagit avec une base de données SQLite, vous permettant d'effectuer des opérations CRUD sur une base de données SQLite.

### **Java**

1. #### [**Utilisation d'une base de données SQLite dans un programme Java**](https://playbackpress.com/books/sqlitebook/chapter/4/1)

Montre comment intégrer le pilote SQLite dans une application Java. Vous apprendrez à ouvrir une connexion, exécuter des requêtes et gérer les exceptions correctement.

## **Conclusion**

À ce stade, vous avez appris à lire et écrire du vrai SQL. Vous avez vu comment concevoir une base de données, comment écrire des requêtes qui récupèrent et modifient des données, et comment aborder des questions de plus en plus complexes en utilisant les outils que SQL vous offre.

Si vous avez travaillé sur les problèmes pratiques, vous avez déjà fait ce que beaucoup de développeurs font sur le terrain : examiner des données inconnues, comprendre les relations et écrire des requêtes pour répondre à des questions réelles.

SQL est une compétence qui s'affûte plus vous l'utilisez. Ne vous inquiétez pas si vous vous sentez encore un peu incertain. La répétition et l'exploration renforceront votre confiance. Continuez à expérimenter, cassez des choses et essayez de les réparer. C'est ainsi que vous apprenez vraiment.

Si vous prévoyez d'utiliser SQL dans vos propres projets, essayez de construire une petite base de données à partir de zéro ou de connecter SQLite à l'un de vos programmes. Vous apprendrez beaucoup en voyant quelles questions vos propres données soulèvent.

Merci d'avoir lu. J'espère que ces replays ont aidé à rendre SQL un peu plus facile à comprendre. Bonne chance avec votre prochain projet SQL.

## **Commentaires et retours**

Vous pouvez trouver tous ces replays de code et plus dans l'un de mes livres gratuits :

* [Conception de bases de données et SQL pour débutants](https://playbackpress.com/books/sqlbook)

* [Exemples pratiques de SQL](https://playbackpress.com/books/workedsqlbook)

* [Programmation avec SQLite](https://playbackpress.com/books/sqlitebook)

* [Une introduction animée à la programmation en C++](https://playbackpress.com/books/cppbook/)

* [Une introduction animée à la programmation avec Python](https://playbackpress.com/books/pybook)

* [Une introduction au développement web de l'arrière vers l'avant](https://playbackpress.com/books/webdevbook)

* [Une introduction animée à Clojure](https://playbackpress.com/books/cljbook)

* [Une introduction animée à Elixir](https://playbackpress.com/books/exbook)

* [Une brève introduction à Ruby](https://playbackpress.com/books/rubybook)

* [Développement d'applications mobiles avec Dart et Flutter](https://playbackpress.com/books/flutterbook)

* [Modèles de conception OO avec Java](https://playbackpress.com/books/patternsbook)

* [Comment je l'ai construit : Word Zearch](https://playbackpress.com/books/wordzearchbook)

Les commentaires et retours sont les bienvenus à tout moment : [mark@playbackpress.com](mailto:mark@playbackpress.com).

Si vous souhaitez soutenir mon travail et aider à garder Playback Press gratuit pour tous, envisagez de faire un don en utilisant [GitHub Sponsors](https://github.com/sponsors/markm208). J'utilise toutes les donations pour les coûts d'hébergement. Votre soutien m'aide à continuer à créer du contenu éducatif comme celui-ci. Merci !