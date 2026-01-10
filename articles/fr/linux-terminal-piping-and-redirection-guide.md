---
title: Comment utiliser le piping et la redirection dans le terminal Linux
subtitle: ''
author: Alvin
co_authors: []
series: null
date: '2024-04-26T23:15:26.000Z'
originalURL: https://freecodecamp.org/news/linux-terminal-piping-and-redirection-guide
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/piping-redirection-linux.png
tags:
- name: Bash
  slug: bash
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: terminal
  slug: terminal
seo_title: Comment utiliser le piping et la redirection dans le terminal Linux
seo_desc: 'The command line interface in Linux provides a powerful way of perfoming
  a range of tasks on your system. Because of its roots, Linux has many features baked
  into the terminal.

  Two of these powerful features are piping and redirection. These features...'
---

L'interface en ligne de commande sous Linux offre une méthode puissante pour effectuer une gamme de tâches sur votre système. En raison de ses origines, Linux intègre de nombreuses fonctionnalités directement dans le terminal.

Deux de ces fonctionnalités puissantes sont le piping et la redirection. Ces fonctionnalités vous permettent de rediriger la sortie et l'entrée des commandes vers et depuis d'autres commandes et fichiers.

Dans cet article, vous apprendrez ce que signifient le piping et la redirection sous Linux, suivi d'une exploration approfondie de la manière d'utiliser ces fonctionnalités vous-même.

## Prérequis

Pour comprendre pleinement ce guide, vous devez au moins avoir :

* Une compréhension de base du [système d'exploitation Linux](https://www.freecodecamp.org/news/learn-the-basics-of-the-linux-operating-system).
* Une expérience de base avec la ligne de commande Linux.
* Un accès à une ligne de commande Linux pour essayer les commandes.

Consultez ce [tutoriel sur la ligne de commande Linux](https://www.freecodecamp.org/news/linux-command-line-tutorial/) si vous êtes nouveau ou avez besoin d'un rappel.

## Qu'est-ce que le Piping sous Linux ?

Avant de plonger dans le comment, que signifie même le piping ? Le piping est l'action de diriger la sortie d'une commande Linux comme entrée vers une autre commande. Vous pouvez diriger la sortie standard ou l'erreur standard d'une commande vers une autre en utilisant le piping.

Un exemple simple de piping est lorsque vous prenez la sortie d'une commande et l'utilisez comme entrée pour une autre commande. Le métacaractère pipe (|) est utilisé pour y parvenir.

Si vous êtes nouveau dans le concept de métacaractères, ce n'est qu'un nom fantaisiste pour les caractères ayant une signification spéciale dans la ligne de commande. Il existe d'autres métacaractères sous Linux en plus du pipe (|). Des exemples courants incluent inférieur à (<), supérieur à (>), et esperluette (&), pour en nommer quelques-uns.

### Les bases du Piping

La syntaxe de base de l'utilisation de la commande `pipe` est la suivante :

```
commande1 | commande2 | commande3 | ... | commandeN
```

Dans la syntaxe ci-dessus, le terminal exécutera les commandes de gauche à droite. Il commencera par `commande1`, puis la sortie sera utilisée comme entrée pour `commande2`. Les sorties de `commande2` seront ensuite utilisées comme entrées de `commande3` et ainsi de suite. Le bon côté du piping est que vous pouvez enchaîner autant de commandes que vous le souhaitez.

### Exemples de Piping

Voici plusieurs exemples d'utilisation de la commande `pipe` pour effectuer diverses tâches.

#### 1. Compter le nombre de fichiers et de répertoires

```bash
ls -l | wc -l
```

Dans l'exemple ci-dessus, la première section liste tous les fichiers et répertoires dans le répertoire courant en utilisant la commande `ls`. L'option supplémentaire `-l` indique à la commande `ls` de lister le contenu dans un format de liste longue.

La sortie de la commande `ls -l` est ensuite transmise à la deuxième section. La commande `wc -l` compte le nombre de lignes à partir de la sortie de la commande `ls -l` dans la première section et imprime le résultat dans le terminal.

#### 2. Trier une liste de fichiers et de répertoires

```bash
ls | sort
```

Dans la commande ci-dessus, la commande `ls` affichera la liste des fichiers et répertoires dans le répertoire courant. La liste est ensuite transmise à la commande `sort`, qui les trie par ordre alphabétique et imprime le résultat dans le terminal.

#### 3. Trier et afficher les mots uniques d'un fichier

```bash
cat words.txt | sort -r | uniq
```

Le troisième exemple comprend trois commandes séparées connectées par deux pipes. La première commande affiche le contenu du fichier `words.txt`, qui contient une liste de mots.

La sortie est transmise à la commande `sort -r`, qui trie les mots par ordre alphabétique inverse. Enfin, les mots triés sont transmis à la commande `uniq`, qui supprime les doublons et affiche les mots triés uniques.

### Pourquoi et quand appliquer le Piping de commandes sous Linux ?

Le piping ne se limite pas à connaître la syntaxe. La syntaxe est assez simple. Pour utiliser efficacement le piping, vous devez comprendre son essence.

Le but du piping est de vous aider à enchaîner des commandes, en utilisant la sortie de l'une comme entrée de l'autre.

Le piping n'est pas destiné à être un moyen d'enchaîner des commandes sans rapport que vous souhaitez exécuter séquentiellement. Si vous devez faire cela, écrivez vos commandes dans le terminal et séparez-les par un point-virgule (;) en utilisant la syntaxe suivante :

```
commande1 ; commande2 ; ... ; commandeN
```

## Qu'est-ce que la Redirection sous Linux ?

La redirection est l'action de dicter où vont les entrées ou sorties de vos commandes. Par défaut, les commandes reçoivent des données depuis l'entrée standard et affichent les résultats dans la sortie standard.

L'un des principaux domaines où la redirection s'avère utile est lors de la manipulation de commandes et de fichiers. Vous pouvez, par exemple, rediriger la sortie d'une commande vers un fichier au lieu d'afficher la sortie dans le terminal. Alternativement, vous pouvez déclarer un certain fichier comme entrée pour une commande.

Comme pour le piping, Linux fournit des caractères spéciaux pour effectuer la redirection. Voici les caractères importants de redirection de fichiers sous Linux et ce qu'ils font :

* `>` – dirige la sortie d'une commande vers un fichier donné.
* `<` – dirige le contenu d'un fichier donné vers une commande.
* `>>` – dirige la sortie d'une commande vers un fichier donné. Ajoute la sortie si le fichier existe et a du contenu.
* `2>` – dirige les messages d'erreur d'une commande vers un fichier donné.
* `2>>` – dirige un message d'erreur d'une commande vers un fichier donné. Ajoute le message d'erreur si le fichier existe et a du contenu.
* `&>` – dirige la sortie standard et l'erreur vers un fichier donné.
* `&>>` – dirige la sortie standard et l'erreur vers un fichier donné. Ajoute au fichier s'il existe et a du contenu.

Examinons chaque caractère de redirection de fichiers en profondeur.

### 1. Redirection de sortie avec `>`

Le symbole `>` vous permet de rediriger la sortie d'une commande vers un certain fichier. En utilisant le symbole, vous pouvez rediriger la sortie vers n'importe quel fichier existant. S'il n'existe pas, le caractère de redirection de sortie créera automatiquement un nouveau fichier.

Cependant, vous devez être prudent lorsque vous écrivez dans un fichier existant car son contenu sera écrasé sans avertissement.

Vous pouvez effectuer une redirection de sortie en utilisant la syntaxe suivante :

```
commande > fichier
```

La sortie de l'exécution de `commande` sera écrite dans le `fichier` au lieu de la sortie standard (ou, en d'autres termes, imprimée dans le terminal). Voici un exemple de la manière dont vous pouvez effectuer une redirection de sortie :

```bash
ls -a > contents.txt
```

Dans la commande ci-dessus, la liste des éléments dans le répertoire courant (y compris les fichiers cachés, répertoires et fichiers) sera écrite dans le fichier `contents.txt`. Vous ne verrez aucune sortie dans le terminal en raison de la redirection.

### 2. Redirection de sortie avec `>>`

`>>` vous permet de rediriger la sortie d'une commande vers un fichier. Mais, contrairement à l'utilisation d'un seul caractère supérieur à (`>`), `>>` ajoutera la sortie si vous essayez d'écrire dans un fichier existant (au lieu d'écraser son contenu). Si le fichier n'existe pas, il en créera un nouveau.

La syntaxe est la suivante :

```
commande >> fichier
```

Voici un exemple d'utilisation de la redirection de sortie avec `>>` pour effectuer la même action que précédemment :

```bash
ls -a >> contents.txt
```

### 3. Redirection d'entrée avec `<`

Le caractère `<` dans la ligne de commande vous permet de rediriger l'entrée vers une commande depuis un fichier au lieu du clavier. La syntaxe de la redirection d'entrée utilisant `<` est la suivante :

```
commande < fichier
```

Voici un exemple d'utilisation de la redirection d'entrée :

```bash
wc -w < files.txt
```

Dans l'exemple ci-dessus, nous passons `files.txt` comme entrée à la commande `wc -w`, qui compte le nombre de mots dans le fichier. Mais vous n'avez pas besoin d'utiliser le caractère de redirection d'entrée dans de nombreux scénarios car c'est le comportement par défaut. Par exemple, la commande ci-dessus est similaire à la suivante :

```bash
wc -w files.txt
```

### 4. Redirection d'erreur avec `2>` et `2>>`

Lorsque vous travaillez sur la ligne de commande, vous pouvez rencontrer des erreurs. Par exemple, si vous souhaitez exécuter un fichier sans permissions appropriées. Au lieu de laisser le terminal afficher une erreur en l'imprimant, vous pouvez utiliser le caractère de redirection d'erreur pour dicter où le message d'erreur doit aller.

Un bon endroit pour rediriger les erreurs est un fichier dédié au stockage des erreurs. Voici un exemple simple d'une commande essayant d'accéder à la liste des fichiers dans un répertoire qui n'existe pas :

```bash
ls nonexistent 2> error.txt
```

Dans l'exemple ci-dessus, le terminal affichera une erreur puisque le fichier `nonexistent` n'existe pas. Mais au lieu de l'imprimer dans la console, il sera stocké dans le fichier `error.txt` grâce au caractère de redirection d'erreur. Cependant, le fichier sera vide s'il n'y a pas d'erreur.

Si vous devez ajouter une erreur à un fichier existant au lieu d'écraser son contenu, utilisez `2>>` au lieu de `2>`.

### 5. Redirection de sortie et d'erreur avec `&>` et `&>>`

Au lieu de choisir de rediriger la sortie standard ou les erreurs standard vers un fichier, `&>` vous permet de rediriger les deux simultanément. Vous pouvez considérer `&>` comme un raccourci pour combiner le caractère de redirection de sortie (>) et le caractère de redirection d'erreur (2>).

La syntaxe de l'utilisation de `&>` est la suivante :

```
commande &> output.txt
```

L'erreur ou la sortie de la `commande` est écrite dans le fichier `output.txt`. Voici un exemple :

```bash
ls sample &> output.txt
```

Dans la commande ci-dessus, si le répertoire `sample` n'est pas disponible ou est disponible mais que vous n'avez pas les permissions de lecture, une erreur appropriée sera écrite dans le fichier `output.txt`. Mais s'il existe et que vous avez les permissions de lecture, son contenu sera écrit dans le fichier `output.txt`.

L'utilisation de `&>>` vous permet d'ajouter la sortie au fichier s'il existe et a du contenu.

## Comment combiner le Piping et la Redirection pour libérer la puissance de la ligne de commande

L'utilisation combinée du piping et de la redirection peut vous permettre d'effectuer des opérations complexes sans effort. En apprenant à combiner les deux, vous pouvez créer des commandes complexes pour effectuer diverses actions avec moins de frappe.

Prenez la commande suivante comme exemple :

```bash
ls | grep ".txt" > text_files.txt
```

La commande `ls` liste le contenu du répertoire courant. La sortie est transmise à la commande `grep` pour filtrer les fichiers texte. Enfin, la sortie de la commande `grep` est redirigée vers le fichier `text_files.txt`.

Cet exemple simple mais puissant montre que lorsqu'il s'agit de piping et de redirection, la seule limite est votre esprit.

## Conclusion

Dans ce tutoriel, vous avez appris les bases du piping et de la redirection sous Linux. Nous avons couvert les bases ainsi que des exemples de la manière dont vous pouvez utiliser les deux.

Les deux fonctionnalités isolément peuvent être puissantes, mais vous pouvez aller plus loin en les combinant dans vos commandes, comme montré dans la dernière section.