---
title: Commencez à interroger des données avec ce langage de requête simple
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-06-12T11:42:00.000Z'
originalURL: https://freecodecamp.org/news/start-querying-data-with-google-query-language
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca217740569d1a4ca5281.jpg
tags:
- name: analysis
  slug: analysis
- name: data
  slug: data
- name: data analysis
  slug: data-analysis
- name: data visualization
  slug: data-visualization
- name: google sheets
  slug: google-sheets
- name: SQL
  slug: sql
seo_title: Commencez à interroger des données avec ce langage de requête simple
seo_desc: "By Peter Gleeson\nWorking with data is becoming an increasingly important\
  \ skill in the modern workplace. \nData is no longer the domain of analysts and\
  \ software engineers. With today's technology, anyone can work with data to analyse\
  \ trends and inform ..."
---

Par Peter Gleeson

Travailler avec des données devient une compétence de plus en plus importante dans le milieu professionnel moderne. 

Les données ne sont plus réservées aux analystes et aux ingénieurs logiciels. Avec la technologie d'aujourd'hui, tout le monde peut travailler avec des données pour analyser des tendances et éclairer sa prise de décision.

Un concept fondamental lors du travail avec des données est l'« interrogation » d'un ensemble de données. Cela consiste littéralement à poser des questions sur un ensemble de données. Un langage de requête est un langage logiciel qui fournit une syntaxe pour poser de telles questions.

Si vous n'avez aucune expérience dans l'écriture de requêtes, elles peuvent sembler un peu intimidantes. Cependant, avec un peu de pratique, vous pouvez maîtriser les bases.

Voici comment vous pouvez commencer dans [Google Sheets](https://www.google.com/sheets/about/).

### Langage de requête de l'API Google Visualization

Vous utilisez peut-être déjà Google Sheets pour une grande partie de votre travail quotidien. Peut-être êtes-vous familier avec son utilisation pour générer des graphiques et des diagrammes. 

Le [langage de requête de l'API Google Visualization](https://developers.google.com/chart/interactive/docs/querylanguage) est la magie qui fonctionne en coulisses pour rendre cela possible.

Mais saviez-vous que vous pouvez accéder à ce langage via la fonction `QUERY()` ? Cela peut être un outil puissant pour travailler avec de grandes feuilles de données.

Il y a beaucoup de similitudes entre le langage de requête et SQL.

Dans les deux cas, vous définissez un ensemble de données de colonnes et de lignes, et vous choisissez différentes colonnes et lignes en spécifiant divers critères et conditions.

Dans cet article, les données d'exemple proviendront d'un grand fichier CSV contenant les résultats de football international entre 1872 et 2019. Vous pouvez [télécharger les données depuis Kaggle](https://www.kaggle.com/martj42/international-football-results-from-1872-to-2017).

Dans une nouvelle feuille Google Sheets, téléchargez le fichier CSV. Vous pouvez sélectionner toutes les données avec Ctrl+A (ou Cmd+A sur Mac). 

Dans le ruban de menu, choisissez Données > Plages nommées... et appelez la plage sélectionnée quelque chose comme 'data'. Cela facilitera le travail.

Maintenant, vous êtes prêt à commencer à interroger les données. Créez un nouvel onglet dans la feuille de calcul, et dans la cellule A1, créez une nouvelle formule `QUERY()`.

### Obtenir tous les matchs de l'Angleterre

Cette première requête trouve toutes les lignes de l'ensemble de données où l'Angleterre est soit l'équipe à domicile, soit l'équipe à l'extérieur.

La formule `QUERY()` prend au moins deux arguments. Le premier est la plage nommée, qui sera l'ensemble de données interrogé. Le second est une chaîne qui contient la requête réelle.

```
=QUERY(data, "SELECT * WHERE B = 'England' OR C = 'England'")
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-21.40.48.png)

Décomposons cela.

`SELECT *` demande de retourner toutes les colonnes de l'ensemble de données. Si vous ne vouliez que les colonnes A, B et C, vous écrirez `SELECT A, B, C`.

Ensuite, vous incluez un filtre pour trouver uniquement les lignes où la colonne B ou la colonne C contient l'équipe `'England'`. Assurez-vous d'utiliser des guillemets simples pour les chaînes à l'intérieur de la requête. Les guillemets doubles sont utilisés pour ouvrir et fermer la requête elle-même.

Cette formule retourne toutes les lignes où l'Angleterre a joué. Si vous voulez rechercher une autre équipe, changez simplement la condition dans le filtre.

### Compter tous les matchs amicaux

Ensuite, comptons combien de matchs amicaux se trouvent dans l'ensemble de données.

```
=QUERY(data, "SELECT COUNT(A) WHERE F = 'Friendly'")
```

Cela utilise la fonction `COUNT()` du langage de requête. C'est un exemple de fonction d'agrégation. Les fonctions d'agrégation résument de nombreuses lignes en une seule.

Par exemple, dans cet ensemble de données, il y a 16 716 lignes où la colonne F est égale à `'Friendly'`. Au lieu de retourner toutes ces lignes, la requête retourne une seule ligne - qui les compte à la place.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-21.40.18.png)

D'autres exemples de fonctions d'agrégation incluent `MAX()`, `MIN()` et `AVG()`. Au lieu de retourner toutes les lignes correspondant à la requête, elles trouvent leurs valeurs maximales, minimales et moyennes.

### Grouper par tournoi

Les fonctions d'agrégation peuvent faire plus si vous utilisez une instruction `GROUP BY` avec elles. Cette requête permet de savoir combien de matchs ont été joués par type de tournoi.

```
=QUERY(data, "SELECT F, COUNT(A) GROUP BY F")
```

Cette requête regroupe l'ensemble de données par chacune des valeurs de la colonne F. Elle compte ensuite combien de lignes il y a dans chaque groupe.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-21.44.50.png)

Vous pouvez utiliser `GROUP BY` sur plus d'une colonne. Par exemple, pour trouver combien de matchs ont été joués dans chaque pays par tournoi, utilisez la requête suivante :

```
=QUERY(data, "SELECT H, F, COUNT(A) GROUP BY H, F")
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-09-at-02.01.17.png)

Essayons un filtrage plus avancé.

### Obtenir tous les matchs Angleterre vs Allemagne

Vous pouvez spécifier une logique de filtre plus complexe en utilisant les mots-clés `AND` et `OR`. Pour la lisibilité, il peut être utile d'utiliser des parenthèses autour de chaque partie du filtre.

Par exemple, pour trouver tous les matchs entre l'Angleterre et l'Allemagne :

```
=QUERY(data, "SELECT * WHERE (B = 'England' AND C = 'Germany') OR (C = 'England' AND B ='Germany')")
```

Ce filtre a deux critères - un où l'Angleterre est l'équipe à domicile et l'Allemagne est à l'extérieur, et l'autre vice versa.

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-21.57.15.png)

L'utilisation de la validation des données facilite la sélection de n'importe quelles deux équipes dans l'ensemble de données.

Ensuite, vous pouvez écrire une requête qui utilise les valeurs de différentes cellules dans son filtre. N'oubliez pas d'utiliser des guillemets simples pour identifier les chaînes à l'intérieur de la requête, et des guillemets doubles pour ouvrir et fermer différentes parties de la requête.

```
=QUERY(data, "SELECT * WHERE (B = '"&B1&"' AND C = '"&B2&"') OR (C = '"&B1&"' AND B ='"&B2&"')")
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-21.58.00.png)

### Recherche de tendances

Les fonctions d'agrégation et les filtres sont des outils puissants lorsqu'ils sont utilisés en combinaison. Une fois que vous êtes à l'aise avec leur fonctionnement, vous pouvez commencer à rechercher toutes sortes de tendances intéressantes dans votre ensemble de données.

Par exemple, la requête ci-dessous trouve le nombre moyen de buts par match, par année depuis 1900.

```
=QUERY(data, "SELECT YEAR(A), AVG(D) + AVG(E) WHERE YEAR(A) >= 1900 GROUP BY YEAR(A)")
```

![Image](https://www.freecodecamp.org/news/content/images/2024/04/score-chart.png)

Si vous tracez le résultat de la requête sous forme de graphique en ligne, vous pouvez immédiatement commencer à voir des tendances au fil du temps.

### Ordonner les résultats

Parfois, vous n'êtes pas intéressé par la recherche de toutes les lignes correspondantes dans un ensemble de données. Souvent, vous voudrez les trier selon certains critères. Peut-être souhaitez-vous uniquement trouver les dix meilleurs enregistrements.

Cette requête trouve les dix matchs avec le plus grand nombre de buts dans l'ensemble de données.

```
=QUERY(data, "SELECT * ORDER BY (D+E) DESC LIMIT 10")
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-22.45.42.png)

Remarquez l'instruction `ORDER BY`. Cela trie les lignes selon les colonnes spécifiées. Ici, la requête trie la sortie par le nombre de buts marqués dans le match. 

Le mot-clé `DESC` indique de trier dans l'ordre décroissant (le mot-clé `ASC` les aurait triés dans l'ordre croissant).

Enfin, le mot-clé `LIMIT` restreint la sortie à un nombre donné de lignes (dans ce cas, dix).

Il semble qu'il y ait eu des matchs assez déséquilibrés en Océanie !

### Quelles villes ont accueilli le plus de matchs de la Coupe du Monde ?

Et maintenant, pour un dernier exemple pour tout rassembler et stimuler votre imagination.

Cette requête trouve les dix villes qui ont accueilli le plus de matchs de la Coupe du Monde de la FIFA.

```
=QUERY(data, "SELECT G, COUNT(A) WHERE F = 'FIFA World Cup' GROUP BY G ORDER BY COUNT(A) DESC LIMIT 10")
```

![Image](https://www.freecodecamp.org/news/content/images/2019/06/Screenshot-2019-06-08-at-22.12.45.png)

### Maintenant, c'est à vous

Espérons que vous avez trouvé cet article utile. Si vous êtes à l'aise avec la logique de chaque exemple, alors vous êtes prêt à essayer le vrai SQL.

Cela introduira des concepts tels que les JOINS, les requêtes imbriquées et les fonctions WINDOW. Lorsque vous maîtriserez ces concepts, votre pouvoir de manipuler des données atteindra des sommets.

Il y a plusieurs endroits pour commencer à apprendre SQL. Essayez les [exemples interactifs sur w3schools](https://www.w3schools.com/sql/default.asp) !