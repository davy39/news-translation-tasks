---
title: Tutoriel sur la commande Grep – Comment rechercher un fichier dans Linux et
  Unix avec une recherche récursive
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-13T22:56:11.000Z'
originalURL: https://freecodecamp.org/news/grep-command-tutorial-how-to-search-for-a-file-in-linux-and-unix
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9b0c740569d1a4ca2969.jpg
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
- name: unix
  slug: unix
seo_title: Tutoriel sur la commande Grep – Comment rechercher un fichier dans Linux
  et Unix avec une recherche récursive
seo_desc: 'By Dillion Megida

  grep stands for Globally Search For Regular Expression and Print out. It is a command
  line tool used in UNIX and Linux systems to search a specified pattern in a file
  or group of files.

  grep comes with a lot of options which allow u...'
---

Par Dillion Megida

`grep` signifie _Globally Search For Regular Expression and Print out_. C'est un outil en ligne de commande utilisé dans les systèmes UNIX et Linux pour rechercher un motif spécifié dans un fichier ou un groupe de fichiers.

`grep` propose de nombreuses options qui nous permettent d'effectuer diverses actions liées à la recherche sur des fichiers. Dans cet article, nous allons voir comment utiliser `grep` avec les options disponibles ainsi que les expressions régulières de base pour rechercher des fichiers.

## Comment utiliser `grep`

Sans passer d'option, `grep` peut être utilisé pour rechercher un motif dans un fichier ou un groupe de fichiers. La syntaxe est :

```bash
grep '<texte-à-rechercher>' <fichier/fichiers>
```

**Notez que** des guillemets simples ou doubles sont nécessaires autour du texte s'il contient plus d'un mot.

Vous pouvez également utiliser le **caractère générique (\*)** pour sélectionner tous les fichiers dans un répertoire.

Le résultat est l'occurrence du motif (par la ligne où il est trouvé) dans le ou les fichiers. Si aucune correspondance n'est trouvée, aucun résultat ne sera affiché dans le terminal.

Par exemple, supposons que nous avons les fichiers suivants (appelés grep.txt) :

```default
Bonjour, comment allez-vous
Je suis grep
Ravi de vous rencontrer
```

La commande `grep` suivante recherchera toutes les occurrences du mot 'you' :

```bash
grep you grep.txt
```

Le résultat est :

```bash
Bonjour, comment allez-vous
Ravi de vous rencontrer
```

Le mot `you` doit avoir une couleur différente des autres textes pour identifier facilement ce qui a été recherché.

Mais `grep` propose plus d'options qui nous aident à accomplir davantage lors d'une opération de recherche. Examinons neuf d'entre elles tout en les appliquant à l'exemple ci-dessus.

### Options utilisées avec `grep`

#### 1. `-n` (--line-number) - lister les numéros de ligne

Cela affiche les correspondances pour le texte ainsi que les numéros de ligne. Si vous regardez le résultat que nous avons ci-dessus, vous remarquerez qu'il n'y a pas de numéros de ligne, juste les correspondances.

```bash
grep you grep.txt -n
```

Résultat :

```bash
1: Bonjour, comment allez-vous
3: Ravi de vous rencontrer
```

#### 2. `-c` (--count) - affiche le nombre de lignes de correspondances

```bash
grep you grep.txt -c
```

Résultat :

```bash
2
```

**Notez que** s'il y avait un autre 'you' sur la ligne un, l'option `-c` afficherait toujours 2. Cela est dû au fait qu'elle est concernée par le nombre de lignes où les correspondances apparaissent, et non par le nombre de correspondances.

#### 3. `-v` (--invert-match) - affiche les lignes qui ne correspondent pas au motif spécifié

```bash
grep you grep.txt -v -n
```

Résultat :

```bash
2. Je suis grep
```

Remarquez que nous avons également utilisé l'option `-n` ? Oui, vous pouvez appliquer plusieurs options dans une seule commande.

#### 4. `-i` (--ignore-case) - utilisé pour l'insensibilité à la casse

```bash
# commande 1
grep You grep.txt
# commande 2
grep YoU grep.txt -i
```

Résultats :

```bash
# résultat 1
# aucun résultat
# résultat 2
Bonjour, comment allez-vous
Ravi de vous rencontrer
```

#### 5. `-l` (--files-with-matches) - affiche les noms de fichiers qui correspondent à un motif

```bash
# commande 1
grep you grep.txt -l
# commande 2
grep You grep.txt -i -l
```

Résultats :

```bash
# résultat 1
grep.txt
# résultat 2
# tous les fichiers dans le répertoire courant qui correspondent
# au texte 'You' de manière insensible à la casse
```

#### 6. `-w` (--word-regexp) - affiche les correspondances du mot entier

Par défaut, `grep` correspond aux chaînes qui contiennent le motif spécifié. Cela signifie que `grep yo grep.txt` affichera les mêmes résultats que `grep yo grep.txt` car 'yo' peut être trouvé dans 'you'. De même pour 'ou'.

Avec l'option `-w`, `grep` garantit que les correspondances sont exactement les mêmes que le motif spécifié. Exemple :

```bash
grep yo grep.txt -w
```

Résultat :

Aucun résultat !

#### 7. `-o` (--only-matching) - affiche uniquement le motif correspondant

Par défaut, `grep` affiche la ligne où le motif correspondant est trouvé. Avec l'option `-o`, seul le motif correspondant est affiché ligne par ligne. Exemple :

```bash
grep yo grep.txt -o
```

Résultat :

```bash
yo
```

#### 8. `-A` (--after-context) et `-B` (--before-context) - affiche les lignes après et avant (respectivement) le motif correspondant

```bash
grep grep grep.txt -A 1 -B 1
```

Résultat :

```bash
Bonjour, comment allez-vous
Je suis grep
Ravi de vous rencontrer
```

Ce motif correspondant est sur la ligne 2. `-A 1` signifie une ligne après la ligne correspondante et `-B 1` signifie une ligne avant la ligne correspondante.

Il existe également une option `-C` (--context) qui est égale à `-A` + `-B`. La valeur passée à `-C` serait utilisée pour `-A` et `-B`.

#### 9. `-R` (--dereference-recursive) - recherche récursive

Par défaut, `grep` ne peut pas rechercher dans les répertoires. Si vous essayez de le faire, vous obtiendrez une erreur ("Is a directory"). Avec l'option `-R`, la recherche de fichiers dans les répertoires et sous-répertoires devient possible. Exemple :

```bash
grep you .
```

Résultat :

```bash
# correspondances de 'you' dans des dossiers
# et fichiers à partir du
# répertoire courant
```

### Expressions régulières pour les motifs

`grep` permet également des expressions régulières de base pour spécifier des motifs. Deux d'entre elles sont :

#### 1. `^motif` - début d'une ligne

Ce motif signifie que `grep` correspondra aux chaînes dont les lignes commencent par la chaîne spécifiée après `^`. Exemple :

```bash
grep ^I grep.txt -n
```

Résultat :

```bash
2: I
```

#### 2. `motif$` - fin d'une ligne

En contraste avec `^`, `$` spécifie les motifs qui seront correspondus si la ligne se termine par la chaîne avant `$`. Exemple :

```bash
grep you$ grep.txt
```

Résultat :

```bash
1: Bonjour, comment allez-vous
3: Ravi de vous rencontrer
```

## Conclusion

`grep` est un outil puissant pour rechercher des fichiers dans le terminal. Comprendre comment l'utiliser vous donne la capacité de trouver facilement des fichiers via le terminal.

Il existe plus d'options attachées à cet outil. Vous pouvez les trouver avec `man grep`.