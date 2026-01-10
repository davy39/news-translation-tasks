---
title: Comment j'ai créé un langage de type SQL pour exécuter des requêtes sur des
  dépôts Git locaux
subtitle: ''
author: Amr Hesham
co_authors: []
series: null
date: '2023-10-26T17:00:00.000Z'
originalURL: https://freecodecamp.org/news/gql-design-and-implementation
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/gitql_banner.png
tags:
- name: Git
  slug: git
- name: SQL
  slug: sql
seo_title: Comment j'ai créé un langage de type SQL pour exécuter des requêtes sur
  des dépôts Git locaux
seo_desc: 'Hello everyone! I''m a Software engineer who''s interested in low-level
  programming, compilers, and tool development.

  Three months ago I decided to learn the Rust programming language and build a Git
  client that focuses on simplicity and productivity.

  ...'
---

Bonjour à tous ! Je suis un ingénieur logiciel intéressé par la programmation bas niveau, les compilateurs et le développement d'outils.

Il y a trois mois, j'ai décidé d'apprendre le langage de programmation Rust et de construire un client Git axé sur la simplicité et la productivité.

J'ai commencé à réfléchir à la manière de construire le client Git pour fournir des fonctionnalités uniques et utiles.

Par exemple, j'aime la page d'analyse sur GitHub qui vous indique combien de commits chaque développeur a effectués et combien de lignes ils ont insérées ou supprimées. Mais que faire si je veux obtenir cette analyse pour une période donnée, ou tout classer par lignes insérées et non par nombre de commits ? Ou les classer par le nombre de commits effectués par semaine ou par mois ?

Vous pouvez ajouter une option de tri personnalisée pour le client, n'est-ce pas ? Mais j'ai commencé à réfléchir à la manière de le rendre plus dynamique. Cela m'a motivé à me demander si je pouvais exécuter des requêtes de type SQL sur les fichiers .git locaux afin de pouvoir interroger n'importe quelle information que je voulais.

Alors imaginez si vous pouviez exécuter une requête comme celle-ci sur vos dépôts git locaux :

```sql
SELECT name, COUNT(name) AS commit_num FROM commits GROUP BY name ORDER BY commit_num DESC LIMIT 10
```

J'ai implémenté cette idée avec un projet que j'ai créé appelé **GQL** (Git Query Language). Et dans cet article, je vais vous montrer comment j'ai conçu et implémenté cette fonctionnalité.

## Comment pouvez-vous prendre une requête de type SQL et l'exécuter sur des fichiers .git ?

La première idée que j'ai eue était d'utiliser SQLite. Mais il y avait quelques problèmes que je ne pouvais pas résoudre.

Par exemple, je ne pouvais pas personnaliser la syntaxe, et je ne voulais pas lire les fichiers .git et les stocker dans une base de données SQLite puis effectuer la requête. Je voulais que tout fonctionne à la volée.

Je voulais également pouvoir utiliser non seulement les commandes SELECT, DELETE et UPDATE, mais aussi fournir des commandes liées à Git comme `push`, `pull`, et ainsi de suite.

J'ai créé différents outils comme des compilateurs auparavant, alors pourquoi ne pas créer un langage de type SQL à partir de zéro et le faire fonctionner à la volée pour voir si cela fonctionne ?

## Comment j'ai conçu et implémenté un langage de requête à partir de zéro

Je voulais commencer modestement en ne supportant que la commande `SELECT` sans fonctionnalités avancées telles que les agrégations, les regroupements, les jointures, et ainsi de suite.

J'ai donc prévu de parser la requête dans une structure de données qui faciliterait la validation et l'évaluation (comme la vérification de type et l'affichage de messages d'erreur utiles si quelque chose allait mal). Après cela, je passerais cette structure de données à l'évaluateur qui appliquerait la requête sur mes fichiers .git.

### Choisir une structure de données à utiliser

La meilleure structure de données pour ce cas est de représenter la requête en utilisant un [A**rbre de Syntaxe Abstraite**](https://en.wikipedia.org/wiki/Abstract_syntax_tree) (AST). Il s'agit d'une structure de données très courante utilisée dans les compilateurs car elle est modifiable et facilite le parcours et la composition des nœuds à l'intérieur des autres.

De plus, dans ce cas, je n'avais pas besoin de conserver toutes les informations sur la requête, seulement les informations nécessaires pour les étapes suivantes (c'est pourquoi on l'appelle Abstraite).

### Décider quelles validations effectuer

La validation la plus importante dans ce cas serait la vérification de type pour s'assurer que chaque valeur est valide et utilisée au bon endroit.

Par exemple, que se passe-t-il si la requête voulait multiplier du texte par un autre texte – serait-ce valide ?

```sql
SELECT "ONE" * "TWO"
```

L'opérateur de multiplication attend que les deux côtés soient des nombres. Donc dans ce cas, je voulais informer l'utilisateur que sa requête est invalide et essayer de l'aider à comprendre le problème autant que possible.

Alors, comment cela fonctionnerait-il ? Lorsque je vois un opérateur comme `*`, vous devez vérifier les deux côtés pour voir si les valeurs sont des types valides pour cet opérateur ou non. Si ce n'est pas le cas, alors signaler un message comme celui-ci :

```sql
SELECT "ONE" * "TWO"
-------------^

ERREUR : L'opérateur `*` attend que les deux côtés soient de type Nombre mais a obtenu du Texte.
```

Outre les opérateurs, je savais que je devais vérifier si chaque identifiant était une table, un champ, un alias ou un nom de fonction, ou s'il devait être indéfini. Je devais également signaler une erreur si, par exemple, une table de branches ne contenait que 2 champs comme dans l'exemple ci-dessous :

```sql
Branches {
   Text name,
   Number commit_count,
}
```

J'ai donc créé une table qui contenait des représentations pour toutes les tables et tous les champs afin de pouvoir effectuer facilement la vérification de type. Si l'utilisateur essayait de sélectionner un champ qui était indéfini dans ce schéma, alors il signalait une erreur :

```sql
SELECT invalid_field_name FROM branches
-------------^

Erreur : Le champ `invalid_field_name` n'est pas défini dans la table branches.
```

Je devais m'assurer que les mêmes vérifications étaient effectuées sur les conditions, les noms de fonctions et les arguments. Ensuite, si tout était correctement défini et avait les types corrects, l'AST serait valide et nous pourrions passer à l'étape suivante.

### Que se passe-t-il après la validation de l'Arbre de Syntaxe Abstraite ?

Après m'être assuré que tout était valide, il était temps d'évaluer la requête et de voir comment elle récupérait le résultat.

Pour ce faire, j'ai simplement parcouru l'arbre de syntaxe et évalué chaque nœud. Après avoir terminé, je devrais avoir le résultat correct dans une liste.

Passons en revue ce processus étape par étape pour voir comment cela fonctionne.

Par exemple, dans une requête comme celle-ci :

```sql
SELECT * FROM branches WHEER name LIKE "%/main" ORDER BY commit_count LIMIE BY 5
```

La représentation AST ressemblera à ceci :

```python
AbstractSyntaxTree {
  Select(*, "branches") 
  Where(Like(name, "%/main"))
  OrderBy(commit_count)
  Limit(5) 
}
```

Maintenant, nous devons parcourir et évaluer chaque nœud mais dans un ordre spécifique. Nous ne allons pas simplement du début à la fin ou de la fin au début car nous devons le faire dans le même ordre que SQL le ferait pour obtenir le même résultat.

Par exemple en SQL, l'instruction `WHERE` doit être exécutée avant `GROUP BY`, et `HAVING` doit être exécutée après.

Dans l'exemple ci-dessus, tout est dans le bon ordre pour l'exécution, alors voyons ce que chaque instruction fera.

* `Select(*, "branches")`
    

Cela sélectionnera tous les champs de la table avec le nom `branches` et les poussera dans une liste – appelons-la `objects`. Mais comment puis-je les sélectionner à partir du dépôt local ?

Toutes les informations sur les commits, les branches, les tags, et ainsi de suite sont stockées par Git dans des fichiers à l'intérieur d'un dossier appelé `.git` dans chaque dépôt. Une option est d'écrire un parseur complet à partir de zéro pour extraire les informations nécessaires. Mais utiliser une bibliothèque pour faire cela à la place a fonctionné pour moi.

J'ai décidé d'utiliser la bibliothèque libgit2 pour effectuer cette tâche. Il s'agit d'une implémentation pure C des méthodes principales de Git, donc vous pouvez lire toutes les informations dont vous avez besoin et les utiliser depuis Rust. Il existe une crate (bibliothèque Rust) créée par l'équipe officielle de Rust appelée `git2`, donc vous pouvez obtenir les informations de branche facilement comme ceci :

```rust
let local_branches = repo.branches(Some(BranchType::Local));
let remote_branches = repo.branches(Some(BranchType::Remote));
let local_and_remote_branches = repository.branches(None);
```

et ensuite itérer sur chaque branche pour obtenir ses informations et les stocker comme ceci :

```rust
for branch in local_and_remote_branches {
   // Extraire les informations de la branche et les stocker
}
```

Maintenant, nous obtenons une liste de toutes les branches que nous utiliserons dans les étapes suivantes.

* `Where(Like(name, "%/main"))`
    

Cela filtrera la liste des objets et supprimera tous les éléments qui ne correspondent pas aux conditions – dans notre cas, ceux se terminant par "/main".

* `OrderBy(commit_count)`
    

Cela trie la liste des objets par la valeur du champ `commit_count`.

* `Limit(5)`
    

Cela prend uniquement les cinq premiers éléments et supprime le reste de la liste des objets.

C'est tout ! Et maintenant nous obtenons un résultat valide, que vous pouvez voir ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/gql_demo.gif align="left")

Les exemples ci-dessous sont valides et s'exécutent correctement :

```sql
SELECT 1
SELECT 1 + 2
SELECT LEN("Git Query Language")
SELECT "One" IN ("One", "Two", "Three")
SELECT "Git Query Language" LIKE "%Query%"

SELECT commit_count FROM branches WHERE commit_count BETWEEN 0 .. 10

SELECT * FROM refs WHERE type = "branch"
SELECT * FROM refs ORDER BY type

SELECT * FROM commits
SELECT name, email FROM commits
SELECT name, email FROM commits ORDER BY name DESC
SELECT name, email FROM commits WHERE name LIKE "%gmail%" ORDER BY name
SELECT * FROM commits WHERE LOWER(name) = "amrdeveloper"
SELECT name FROM commits GROUP By name
SELECT name FROM commits GROUP By name having name = "AmrDeveloper"

SELECT * FROM branches
SELECT * FROM branches WHERE is_head = true
SELECT name, LEN(name) FROM branches

SELECT * FROM tags
SELECT * FROM tags OFFSET 1 LIMIT 1
```

### Comment supporter l'exécution sur plusieurs dépôts en même temps

Après avoir publié GQL, j'ai reçu des retours incroyables de la part des gens. J'ai également reçu quelques demandes de fonctionnalités, comme le support pour plusieurs dépôts et le filtrage par chemin de dépôt.

J'ai pensé que c'était une excellente idée, car je pourrais obtenir des analyses pour plusieurs projets et aussi parce que je pourrais le faire sur plusieurs threads. Cela ne semblait pas très difficile à implémenter non plus.

Donc, après avoir terminé l'étape de validation pour l'AST, il est temps pour l'étape d'évaluation, mais au lieu de l'évaluer une fois, elle sera évaluée une fois pour chaque dépôt, puis fusionner tous les résultats en une seule liste.

Mais qu'en est-il de la prise en charge de la capacité à filtrer par chemin de dépôt ?

C'était assez facile. Vous vous souvenez du schéma de la table des branches ? Tout ce que je devais faire était d'introduire un nouveau champ avec le nom `repository_path` pour représenter le chemin local du dépôt pour cette branche et l'introduire dans d'autres tables également.

Donc le schéma final ressemblera à ceci :

```sql
Branches {
   Text name,
   Number commit_count,
   Text repository_path,
}
```

Maintenant, nous pouvons exécuter une requête qui utilise ce champ :

```sql
SELECT * FROM branches WHERE repository_path LIKE "%GQL"
```

Et c'est tout ! 😉

### Merci d'avoir lu !

Si vous avez aimé le projet, vous pouvez lui donner une étoile  2B50 sur [github.com/AmrDeveloper/GQL](https://github.com/AmrDeveloper/GQL).

Vous pouvez consulter le site web [**github.io/GQL**](https://amrdeveloper.github.io/GQL/) pour savoir comment télécharger et utiliser le projet sur différents systèmes d'exploitation.

Le projet n'est pas encore terminé – ce n'est que le début. Tout le monde est le bienvenu pour rejoindre et contribuer au projet et suggérer des idées ou signaler des bugs.