---
title: Améliorez vos compétences en programmation en lisant le code de Git
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2021-03-10T01:40:53.000Z'
originalURL: https://freecodecamp.org/news/boost-programming-skills-read-git-code
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/Boost-Your-Programming-Skills-by-Reading-Git-s-Code.png
tags:
- name: C
  slug: c-3
- name: FOSS
  slug: foss
- name: Git
  slug: git
- name: open source
  slug: open-source
seo_title: Améliorez vos compétences en programmation en lisant le code de Git
seo_desc: 'These days there are plenty of trendy ways to improve your programming
  skills and knowledge, including:


  Taking a free or paid online programming course


  Reading a programming book


  Picking a personal project and hacking away to learn as you code


  Fo...'
---

De nos jours, il existe de nombreuses façons tendance d'améliorer vos compétences et connaissances en programmation, notamment :

* Suivre un cours de programmation en ligne gratuit ou payant
  
* Lire un livre de programmation
  
* Choisir un projet personnel et coder pour apprendre en pratiquant
  
* Suivre un projet de tutoriel en ligne
  
* Se tenir au courant des blogs de programmation pertinents
  
Chacune de ces méthodes plaira à différentes personnes, et chacune d'entre elles contient des éléments qui vous rendront définitivement meilleur en programmation. Si vous êtes un codeur intermédiaire ou avancé, il est presque certain que vous avez essayé chacune de ces méthodes au moins une fois.

Cependant, il existe une autre méthode que la grande majorité des développeurs négligent, ce qui est dommage à mon avis car elle a tant à offrir. Cette méthode consiste à **apprendre en lisant, en analysant et en comprenant des bases de code existantes et de haute qualité !**

Nous avons de la chance de vivre à une époque où le bon code est souvent accessible gratuitement via des projets libres et open-source (FOSS) de haute qualité. Et il faut moins d'une minute pour cloner des copies de ces bases de code sur nos machines locales à partir de sites comme GitHub ou BitBucket.

De plus, les systèmes modernes de contrôle de version comme Git nous permettent de voir le code à n'importe quel moment de son historique de développement. Il est clair qu'il y a une mine d'informations juste sous nos yeux !

Dans cet article, nous allons discuter de la version originale du code de Git afin de mettre en lumière comment la lecture de code existant peut aider à améliorer vos compétences en codage.

Nous allons aborder pourquoi il est utile d'apprendre le code de Git, comment accéder au code de Git, et passer en revue quelques concepts de programmation C liés.

Nous allons fournir un aperçu de la structure de la base de code originale de Git et apprendre comment les fonctionnalités principales de Git sont implémentées dans le code.

Enfin, nous recommanderons quelques prochaines étapes pour les développeurs curieux afin de continuer à apprendre à partir du code de Git et d'autres projets.

## Pourquoi apprendre le code de Git ?

La base de code de Git est une ressource incroyable pour les développeurs intermédiaires afin d'approfondir leurs connaissances et compétences en programmation. Voici 7 raisons pour lesquelles il vaut la peine de se plonger dans le code de Git :

1. Git est probablement l'outil de développement logiciel le plus populaire utilisé aujourd'hui. En bref, si vous êtes un développeur, vous utilisez probablement Git. Apprendre comment fonctionne le code de Git vous donnera une compréhension plus profonde d'un outil essentiel que vous utilisez tous les jours.
   
2. Git est intéressant ! Git est un outil polyvalent qui résout de nombreux problèmes intéressants pour permettre aux développeurs de collaborer sur du code. En tant qu'être humain curieux, j'ai vraiment apprécié en apprendre davantage à ce sujet.
   
3. Le code de Git est écrit en langage de programmation **C**, ce qui offre une excellente opportunité pour les développeurs de se diversifier dans un langage important qu'ils n'ont peut-être pas beaucoup utilisé auparavant.
   
4. Git utilise de nombreux concepts de programmation importants, notamment les *bases de données adressables par contenu, la compression/décompression de fichiers, les fonctions de hachage, la mise en cache*, et un *modèle de données simple*. Le code de Git illustre comment ces concepts peuvent être implémentés dans un projet réel.
   
5. Le code et la conception de Git sont *élégants*. C'est un excellent exemple d'une base de code fonctionnelle et minimaliste qui atteint son objectif de manière claire et efficace.
   
6. Le commit initial de Git est petit en taille - il est composé de seulement 10 fichiers, contenant moins de 1 000 lignes de code au total. Cela est très petit par rapport à la plupart des autres projets et est très gérable à comprendre en un temps raisonnable.
   
7. Le code dans le commit initial de Git peut être compilé et exécuté avec succès. Cela signifie que vous pouvez jouer avec et tester la version originale du code de Git pour voir comment il fonctionne.
   
Maintenant, voyons comment accéder à la version originale du code de Git.

## Comment consulter le commit initial de Git ?

La copie officielle de la base de code de Git est hébergée dans [ce dépôt public GitHub](https://github.com/git/git). Cependant, j'ai créé un fork de la base de code de Git et ajouté des commentaires en ligne extensifs au code source, pour aider les développeurs à le lire facilement ligne par ligne.

Puisque j'ai travaillé à partir du tout premier commit dans l'historique de Git, j'ai nommé ce projet **Baby Git**. La base de code de Baby Git se trouve dans [ce dépôt public BitBucket](https://bitbucket.org/jacobstopak/baby-git).

Je recommande de cloner la base de code de Baby Git sur votre machine locale en exécutant la commande suivante dans votre terminal :

```sh
git clone https://bitbucket.org/jacobstopak/baby-git.git
```

Si vous souhaitez rester avec la base de code originale de Git (sans les commentaires extensifs que j'ai ajoutés), utilisez plutôt cette commande :

```sh
git clone https://github.com/git/git.git
```

Parcourez le nouveau répertoire `git` en exécutant la commande `cd git`. N'hésitez pas à explorer les dossiers et fichiers ici.

Vous remarquerez rapidement que dans la version actuelle de Git - la version actuellement extraite dans votre répertoire de travail - qu'il y a **beaucoup** de fichiers contenant beaucoup de code long et compliqué.

Clairement, cette version actuelle de Git est trop grande pour qu'un seul développeur puisse s'y familiariser en un temps raisonnable.

Simplifions les choses en consultant le commit initial de Git, en utilisant la commande :

```sh
git log --reverse
```

Cela montre une liste du journal des commits de Git dans l'ordre inverse, en commençant par le commit initial de Git. Notez que le premier ID de commit dans la liste est `e83c5163316f89bfbde7d9ab23ca2e25604af290`.

Consultez le contenu de ce commit dans le répertoire de travail en exécutant la commande :

```sh
git checkout e83c5163316f89bfbde7d9ab23ca2e25604af290
```

Cela [met Git dans un état de *tête détachée*](https://initialcommit.com/blog/what-is-git-head) et place les fichiers de code originaux de Git dans le répertoire de travail.

Exécutez maintenant la commande `ls` pour lister ces fichiers, et notez qu'il n'y en a que 10 qui contiennent réellement du code ! (Le 11ème est juste un README). Comprendre le code dans ces fichiers est tout à fait gérable pour un développeur intermédiaire !

**Note :** Si vous utilisez mon dépôt Baby Git, vous voudrez exécuter la commande `git checkout master` pour abandonner la tête détachée et revenir à la pointe de la branche master. Cela vous permettra de voir tous les commentaires en ligne décrivant comment le code de Git fonctionne ligne par ligne !

## Concepts importants en C qui vous aideront à comprendre le code de Git

Avant de plonger directement dans le code de Git, il est utile de faire un rappel sur quelques concepts de programmation C qui apparaissent dans toute la base de code.

### Fichiers d'en-tête C

Un fichier d'en-tête C est un fichier de code se terminant par l'extension `.h`. Les fichiers d'en-tête sont utilisés pour stocker des variables, des fonctions et d'autres objets C qu'un développeur souhaite inclure dans plusieurs fichiers de code source `.c` en utilisant la directive `#include "headerFile.h"`.

Si vous êtes familiarisé avec l'importation de fichiers en Python ou Java, c'est une procédure comparable.

### Prototypes de fonctions C (ou signatures de fonctions)

Un prototype ou une signature de fonction indique au compilateur C des informations sur une définition de fonction - le nom de la fonction, le nombre d'arguments, les types d'arguments et le type de retour - sans fournir un corps de fonction. Ils aident le compilateur C à identifier les propriétés des fonctions dans des situations où le corps de la fonction apparaît après que la fonction est appelée.

Voici un exemple de prototype de fonction :

```c
int multiplyNumbers(int a, int b);
```

### Macros C

Une macro en C est essentiellement une variable rudimentaire qui est traitée avant la compilation du code dans un programme C. Les macros sont créées en utilisant la directive `#define`, telle que :

```c
#define TESTMACRO asdf
```

Cela crée une macro appelée `TESTMACRO` avec une valeur de `asdf`. Partout où le placeholder `TESTMACRO` est utilisé dans le code, il sera remplacé par le préprocesseur (avant la compilation du code) par la valeur `asdf`.

Les macros sont couramment utilisées de quelques manières :

* Comme un interrupteur vrai/faux en vérifiant si une macro est définie
  
* Pour stocker une valeur entière ou de chaîne simple à remplacer dans le code à plusieurs endroits
  
* Pour stocker un extrait de code simple (généralement d'une ligne) à remplacer dans le code à plusieurs endroits
  
Les macros sont des outils pratiques car elles permettent aux développeurs de mettre à jour une seule ligne de code qui influence le comportement du code à plusieurs endroits.

### Structs C

Un struct en C est un ensemble groupé de propriétés qui sont liées à un seul objet.

Vous êtes probablement familiarisé avec les Classes dans des langages tels que Java et Python. Un struct est un prédécesseur d'une classe - il peut être considéré comme une classe primitive sans méthodes.

```c
struct person {

	int person_id;
	char *first_name;
	char *last_name;

};
```

Ce struct représente une personne, en regroupant un champ ID, ainsi que le prénom et le nom de la personne. Une variable peut être instanciée et initialisée à partir de ce struct comme suit :

```c
struct person jacob = { 1, "Jacob", "Stopak" };
```

Les propriétés du struct peuvent être récupérées en utilisant l'opérateur point :

```c
jacob.person_id
jacob.first_name
jacob.last_name
```

### Pointeurs C

Un pointeur est une adresse mémoire d'une variable - c'est l'adresse mémoire à laquelle la valeur de cette variable est stockée.

Un pointeur vers une variable existante peut être obtenu en utilisant le symbole `&`, et stocké dans une variable de pointeur déclarée avec le symbole `*` :

```c
int age = 21;

int* age_pointer = &age;
```

Ce snippet définit la variable `age` et lui attribue une valeur de 21. Ensuite, il définit un *pointeur vers un entier* appelé `age_pointer`, et utilise le `&` pour obtenir l'adresse mémoire à laquelle la valeur de la variable age est stockée.

Les pointeurs peuvent être *déréférencés* (c'est-à-dire obtenir la valeur stockée à l'adresse mémoire), en utilisant le `*` également.

```c
int new_age = *age_pointer + 10;
```

En continuant à partir de notre exemple précédent, nous utilisons la syntaxe `*age_pointer` pour récupérer la valeur stockée dans le pointeur (21), et nous ajoutons 10 à celle-ci. Ainsi, la variable `new_age` contiendrait une valeur de 31.

Maintenant que notre courte digression dans la programmation C est terminée, revenons au code de Git.

## Aperçu de la structure de la base de code de Git

Il y a dix fichiers de code pertinents qui composent le commit initial de Git. Nous commencerons par discuter brièvement de ces deux-là :

* Makefile
  
* cache.h
  
Nous discuterons d'abord de `Makefile` et `cache.h` parce qu'ils sont un peu spéciaux.

`Makefile` est un fichier de construction qui contient un ensemble de commandes utilisées pour construire les autres fichiers de code source en exécutables.

Lorsque vous exécutez la commande `make all` à partir de la ligne de commande, le Makefile compilera les fichiers de code source et produira les exécutables pertinents pour les commandes de Git. Si vous êtes intéressé, j'ai écrit un [guide approfondi sur le makefile de Git](https://initialcommit.com/blog/Learn-Git-Makefile).

**Note :** Si vous voulez vraiment compiler le code de Git localement, ce que je vous recommande de faire, vous devrez utiliser ma version Baby Git du code mentionné ci-dessus. La raison est que j'ai apporté quelques modifications pour permettre au code original de Git de compiler sur les systèmes d'exploitation modernes.

Ensuite, il y a le fichier `cache.h`, qui est le seul fichier d'en-tête de Baby Git. Comme mentionné ci-dessus, le fichier d'en-tête définit de nombreuses signatures de fonctions, structs, macros et autres paramètres qui sont utilisés dans les fichiers de code source `.c`. Si vous êtes curieux, j'ai écrit un [guide approfondi sur les fichiers d'en-tête de Git](https://initialcommit.com/blog/Learn-Git-Header-Files).

Les huit fichiers de code restants sont tous des fichiers de code source `.c` :

* `init-db.c`
  
* `update-cache.c`
  
* `read-cache.c`
  
* `write-tree.c`
  
* `commit-tree.c`
  
* `read-tree.c`
  
* `cat-file.c`
  
* `show-diff.c`
  
Chaque fichier (sauf `read-cache.c`) est nommé d'après la commande Git qu'il contient le code pour - certains vous semblent probablement familiers. Par exemple, le fichier `init-db.c` contient le code pour la commande `init-db` utilisée pour initialiser un nouveau dépôt Git. Comme vous l'avez probablement deviné, c'était le précurseur de la commande `git init`.

En fait, chacun de ces fichiers `.c` (sauf `read-cache.c`) contient le code pour l'une des huit commandes Git originales. Le processus de construction compile chacun de ces fichiers et crée un fichier exécutable (avec un nom correspondant) pour chacun. Une fois que ces exécutables sont ajoutés au chemin du système de fichiers, ils peuvent être exécutés de manière similaire à n'importe quelle commande Git moderne.

Ainsi, après avoir compilé le code en utilisant la commande `make all`, les exécutables suivants sont produits :

* `init-db` : Initialise un nouveau dépôt Git. Équivalent à `git init`.
  
* `update-cache` : Ajoute un fichier à l'index de staging. Équivalent à `git add`.
  
* `write-tree` : Crée un objet arbre dans le dépôt Git à partir du contenu actuel de l'index.
  
* `commit-tree` : Crée un nouvel objet commit dans le dépôt Git. Équivalent à `git commit`.
  
* `read-tree` : Affiche le contenu d'un arbre à partir du dépôt Git.
  
* `cat-file` : Récupère le contenu d'un objet à partir du dépôt Git et le stocke dans un fichier temporaire dans le répertoire courant. Équivalent à `git show`.
  
* `show-diff` : Affiche les différences entre les fichiers mis en stage dans l'index et les versions actuelles de ces fichiers telles qu'elles existent dans le système de fichiers. Équivalent à `git diff`.
  
Ces commandes sont exécutées individuellement en séquence, de manière similaire à l'exécution des commandes Git modernes dans le cadre des flux de travail de développement standard.

Le seul fichier que nous n'avons pas encore discuté est `read-cache.c`. Ce fichier contient un ensemble de fonctions auxiliaires que les autres fichiers de code source `.c` utilisent pour récupérer des informations à partir du dépôt Git.

Maintenant que nous avons abordé chacun des fichiers importants dans le commit initial de Git, discutons de certains des concepts de programmation principaux qui permettent à Git de fonctionner.

## Implémentation des concepts principaux de Git

Dans cette section, nous allons discuter des concepts de programmation suivants que Git utilise pour fonctionner, ainsi que de la manière dont ils ont été implémentés dans le code original de Git :

* Compression de fichiers
  
* Fonction de hachage
  
* Objets
  
* Cache du répertoire courant (zone de staging)
  
* Base de données adressable par contenu (base de données d'objets)
  
### Compression de fichiers

La compression de fichiers, également connue sous le nom de déflation, est utilisée pour l'efficacité du stockage et des performances dans Git. Cela réduit la taille des fichiers que Git stocke sur le disque et augmente la vitesse de récupération des données lorsque Git doit transférer ces fichiers sur un réseau.

Cela est important puisque les opérations locales et réseau de Git doivent être aussi rapides que possible. Dans le cadre du processus de récupération des données, Git décompresse, ou gonfle, les fichiers pour obtenir leur contenu.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/image-37.png align="left")

*Source : https://initialcommit.com/blog/Learn-Git-Guidebook-For-Developers-Chapter-2*

La déflation et l'inflation des fichiers ont été implémentées dans le code original de Git en utilisant la bibliothèque C populaire `zlib.h`. Cette bibliothèque contient des fonctions, des structures et des propriétés pour compresser et décompresser le contenu. Plus précisément, `Zlib` définit une structure `z_stream` qui est utilisée pour contenir le contenu qui doit être déflé ou gonflé.

Les fonctions `zlib` suivantes sont utilisées pour *initialiser* un flux pour la déflation ou l'inflation, respectivement :

```c
/*
 * Initialise l'état interne `z_stream`
 * pour la compression au `niveau`, qui indique
 * l'échelle de la vitesse par rapport à la compression sur une
 * échelle de 0-9. Provenant de <zlib.h>.
 */
deflateInit(z_stream, level);

/*
 * Initialise l'état interne `z_stream` pour
 * la décompression. Provenant de <zlib.h>.
 */
inflateInit(z_stream);
```

Les fonctions `zlib` suivantes sont utilisées pour effectuer les opérations réelles de déflation et d'inflation :

```c
/*
 * Compresse autant de données que possible et s'arrête
 * lorsque le tampon d'entrée devient vide ou que le
 * tampon de sortie devient plein. Provenant de <zlib.h>.
 */
deflate(z_stream, flush);

/*
 * Décompresse autant de données que possible et s'arrête
 * lorsque le tampon d'entrée devient vide ou que le
 * tampon de sortie devient plein. Provenant de <zlib.h>.
 */
inflate(z_stream, flush);
```

Le processus réel de déflation/inflation est un peu plus complexe que cela et implique la définition de plusieurs paramètres du flux de compression, mais nous n'entrerons pas dans plus de détails ici.

Ensuite, nous discuterons du concept des fonctions de hachage et de leur implémentation dans le code original de Git.

### Fonctions de hachage

Une fonction de hachage est une fonction qui peut facilement transformer une entrée en une sortie unique, mais rend très difficile ou impossible d'inverser cette opération. En d'autres termes, c'est une **fonction à sens unique**. Il n'est pas possible avec la technologie actuelle d'utiliser la sortie d'une fonction de hachage pour déduire l'entrée qui a été utilisée pour générer cette sortie.

Git utilise une fonction de hachage - spécifiquement la fonction de hachage SHA-1 - pour générer des identifiants uniques pour les fichiers que nous demandons à Git de suivre.

En tant que développeurs, nous apportons des modifications aux fichiers de code dans la base de code sur laquelle nous travaillons en utilisant un éditeur de texte, et à un moment donné, nous demandons à Git de suivre ces modifications. À ce stade, Git utilise ces modifications de fichiers comme entrées pour la fonction de hachage.

La sortie de la fonction de hachage est appelée un **hachage**. Le hachage est une valeur hexadécimale de 40 caractères de long, telle que `47a013e660d408619d894b20806b1d5086aab03b`.

![Fonction de hachage Git](https://initialcommit.com/img/initialcommit/figure5.png align="left")

*Source : https://initialcommit.com/blog/Learn-Git-Guidebook-For-Developers-Chapter-2*

Git utilise ces hachages à diverses fins que nous verrons dans les sections suivantes.

### Objets

Git utilise un modèle de données simple - un ensemble structuré d'objets liés - pour implémenter sa fonctionnalité. Ces objets sont les pépites d'information qui permettent à Git de suivre les modifications des fichiers d'une base de code. Les trois types d'objets que Git utilise sont :

* Blob
  
* Tree
  
* Commit
  
Discutons de chacun d'eux à tour de rôle.

#### Blob

Un blob est l'abréviation de **B**inary **L**arge **OB**ject. Lorsque Git reçoit l'ordre de suivre un fichier en utilisant la commande `update-cache <filename.ext>` (le précurseur de `git add`), Git crée un nouveau blob en utilisant le contenu compressé de ce fichier.

Git prend le contenu du fichier, le compresse en utilisant les fonctions `zlib` que nous avons décrites ci-dessus, et utilise ce contenu compressé comme entrée pour la fonction de hachage SHA-1. Cela crée un hachage de 40 caractères que Git utilise pour identifier le blob en question.

Enfin, Git sauvegarde le blob sous forme de fichier binaire dans un dossier spécial appelé la **base de données d'objets** (nous en parlerons plus en détail dans un instant). Le nom du fichier blob est le hachage généré, et le contenu du fichier blob est le contenu du fichier compressé qui a été ajouté en utilisant `update-cache`.

#### Tree

Les objets tree sont utilisés pour lier ensemble plusieurs blobs qui sont ajoutés à Git en une seule fois. Ils sont également utilisés pour corrélér les blobs avec les noms de fichiers (et d'autres métadonnées de fichiers comme les permissions), puisque les blobs ne fournissent aucune information autre que le hachage et le contenu binaire compressé du fichier.

Par exemple, si deux fichiers modifiés sont ajoutés en utilisant la commande `update-cache`, un tree sera créé contenant les hachages de ces fichiers, ainsi que le nom de fichier auquel chacun de ces blobs correspond.

Ce que Git fait ensuite est très intéressant, alors soyez attentif. Git utilise **le contenu du tree lui-même** comme entrée pour la fonction de hachage SHA-1, qui génère un hachage de 40 caractères. Ce hachage est utilisé pour identifier l'objet tree, et Git sauvegarde cela dans le même dossier spécial que celui où les blobs sont sauvegardés - la base de données d'objets dont nous parlerons bientôt.

#### Commit

Vous êtes probablement plus familier avec les objets commit qu'avec les blobs et les trees. Un commit représente un ensemble de modifications de fichiers sauvegardées par Git, ainsi que des informations descriptives sur la modification telles qu'un message de commit, le nom de l'auteur et l'horodatage du commit.

Dans le code original de Git, un objet commit est le résultat de l'exécution de la commande `commit-tree <tree-hash>`. L'objet commit résultant inclut l'objet tree spécifié (qui, rappelez-vous, représente une collection de modifications de fichiers via un ou plusieurs blobs mappés à leurs noms de fichiers), et les informations descriptives mentionnées dans le paragraphe précédent.

Comme les blobs et les trees, Git identifie le commit en hachant son contenu en utilisant la fonction de hachage SHA-1, et en le sauvegardant dans la base de données d'objets. Importamment, chaque objet commit contient également le hachage de son commit parent. De cette manière, les commits forment une chaîne que Git peut utiliser pour représenter l'historique d'un projet.

### Cache du répertoire courant (Zone de staging)

Vous connaissez probablement la zone de staging de Git comme l'endroit où vos fichiers modifiés vont après avoir utilisé la commande `git add`, en attendant patiemment d'être validés en utilisant `git commit`. Mais qu'est-ce que la zone de staging exactement ?

Dans la version originale de Git, la zone de staging est appelée le **cache du répertoire courant**. Le cache du répertoire courant est simplement un fichier binaire stocké dans le dépôt au chemin `.dircache/index`.

Comme mentionné dans la section précédente, après que les fichiers modifiés sont ajoutés à Git en utilisant la commande `update-cache` (`git add`), Git calcule les objets blob et tree associés à ces modifications. L'objet tree généré associé aux fichiers mis en stage est ajouté au fichier `index`.

Il est appelé un **cache** car il s'agit simplement d'un emplacement de stockage temporaire pour les modifications mises en stage avant d'être validées. Lorsque l'utilisateur effectue un commit en exécutant la commande `commit-tree`, le tree du cache du répertoire courant peut être fourni. Il inclut également d'autres informations de commit comme le message de commit pour que Git crée un nouvel objet commit.

À ce stade, le fichier `index` est simplement supprimé pour laisser place à de nouvelles modifications à mettre en stage.

### Base de données adressable par contenu (Base de données d'objets)

La base de données d'objets est l'emplacement de stockage principal de Git. C'est là que tous les objets dont nous avons discuté ci-dessus - blobs, trees et commits - sont stockés. Dans la version originale de Git, la base de données d'objets est simplement un répertoire au chemin `.dircache/objects/`.

Lorsque Git crée des objets via des opérations telles que `update-cache`, `write-tree` et `commit-tree` (les prédécesseurs de `git add` et `git commit`), ces objets sont compressés, hachés et stockés dans la base de données d'objets.

Le nom de chaque objet est le hachage de son contenu, d'où le fait que la base de données d'objets est également appelée une **base de données adressable par contenu**. Chaque morceau de contenu (blob, tree ou commit) est stocké et récupéré en fonction d'un identifiant généré à partir du contenu lui-même.

La version moderne de Git fonctionne de manière très similaire. La différence est que les formats de stockage ont été optimisés pour utiliser des méthodes plus efficaces (surtout en ce qui concerne le transfert de données sur les réseaux), mais les principes de base sont les mêmes.

## Résumé

Dans cet article, nous avons discuté de la version originale du code de Git afin de mettre en lumière comment la lecture de code existant peut aider à améliorer vos compétences en codage.

Nous avons abordé les raisons pour lesquelles Git est un excellent projet à apprendre de cette manière, comment accéder au code de Git, et passé en revue quelques concepts de programmation C liés. Enfin, nous avons fourni un aperçu de la structure de la base de code originale de Git et nous sommes plongés dans certains concepts sur lesquels le code de Git repose.

## Prochaines étapes

Si vous êtes intéressé à en apprendre davantage sur le code de Git, [nous avons écrit un guide que vous pouvez consulter ici](https://initialcommit.com/store/baby-git-guidebook-for-developers). Ce livre plonge dans le code C original de Git en détail et explique directement comment le code fonctionne.

J'encourage tous les développeurs à explorer la communauté open-source pour essayer de trouver des projets de qualité qui les intéressent. Ces projets auront des bases de code que vous pourrez cloner en quelques minutes.

Prenez le temps d'explorer le code, et vous pourriez apprendre quelque chose que vous ne vous attendiez pas à trouver.