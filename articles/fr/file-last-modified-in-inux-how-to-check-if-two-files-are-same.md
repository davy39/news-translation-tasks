---
title: Qu'est-ce qu'une somme de contrôle ? Comment vérifier si un fichier a été modifié
  en utilisant la commande cksum sous Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-07-19T15:33:13.000Z'
originalURL: https://freecodecamp.org/news/file-last-modified-in-inux-how-to-check-if-two-files-are-same
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/Copy-of-Cast-a-Function-in-SQL
seo_title: Qu'est-ce qu'une somme de contrôle ? Comment vérifier si un fichier a été
  modifié en utilisant la commande cksum sous Linux
---

Convert-Char-to-Int-SQL-Server-Example.gif
tags:
- name: ligne de commande
  slug: ligne-de-commande
- name: sécurité de l'information
  slug: securite-de-linformation
- name: Linux
  slug: linux
seo_title: null
seo_desc: "Lorsque vous travaillez avec des fichiers sur la ligne de commande, vous pourriez avoir besoin de vérifier leur heure de modification et l'intégrité de leur contenu. Linux dispose d'une ligne de commande puissante qui vous permet d'explorer plusieurs aspects des fichiers et des systèmes de fichiers. Au cas où vous auriez besoin de ..."
---

Lorsque vous travaillez avec des fichiers sur la ligne de commande, vous pourriez avoir besoin de vérifier leur heure de modification et l'intégrité de leur contenu.

Linux dispose d'une ligne de commande puissante qui vous permet d'explorer plusieurs aspects des fichiers et des systèmes de fichiers.

Au cas où vous auriez besoin de vérifier si un fichier a été modifié, vous pouvez suivre ces deux approches :

## Comment vérifier si un fichier a été modifié en vérifiant l'heure de modification

Lorsque qu'un fichier est édité, son horodatage change pour correspondre à l'heure de modification.

Nous pouvons voir la dernière heure de modification d'un fichier en utilisant la liste détaillée (`ls -l`).

Dans la sortie ci-dessous, nous pouvons voir que le fichier a été modifié le `19 juil. 13:22`.

```bash
zaira@Zaira:~$ ls -lrt | grep calculator.py
-rw-r--r--  1 zaira zaira  263 19 juil. 13:22 calculator.py
```

## Comment vérifier si un fichier a été modifié en vérifiant la taille du fichier

Si nous connaissons la taille précédente du fichier, nous pouvons la comparer avec la taille actuelle du fichier pour voir s'il a changé.

Nous pouvons voir la taille du fichier en utilisant la liste détaillée (`ls -l`). La 5ème colonne montre la taille du fichier en octets.

```bash
zaira@Zaira:~$ ls -lrt | grep calculator.py
-rw-r--r--  1 zaira zaira  263 19 juil. 13:22 calculator.py
```

Les méthodes mentionnées ci-dessus permettent généralement d'accomplir la tâche, mais il existe une méthode avancée pour vérifier l'intégrité des fichiers en utilisant un hachage. Cette méthode est appelée 'somme de contrôle' et la commande correspondante sous Linux est `cksum`.

## Qu'est-ce qu'une somme de contrôle sous Linux ?

Parfois, les données sont corrompues lors de la transmission ou du stockage. Pour s'assurer que les données restent cohérentes, nous pouvons utiliser la somme de contrôle.

La somme de contrôle est le résultat d'un algorithme appelé fonction de hachage cryptographique. Il est appliqué aux blocs de données du fichier.

En réseau, vous pouvez utiliser la somme de contrôle pour comparer la valeur de hachage aux extrémités de l'expéditeur et du destinataire. Si la valeur de hachage est la même, cela implique que votre copie du fichier est authentique et sans erreur.

Certaines fonctions de hachage cryptographique couramment utilisées incluent MD5 et SHA-1.

Ensuite, nous verrons comment nous pouvons calculer le hachage sous Linux.

## Comment trouver la somme de contrôle sous Linux en utilisant `cksum`

**`cksum`** est une commande trouvée dans les systèmes d'exploitation de type *nix qui génère une valeur de somme de contrôle pour un fichier ou un flux de données.

Selon la page de manuel de `cksum`, la commande imprime la somme de contrôle CRC (contrôle de redondance cyclique) et le nombre d'octets de chaque FICHIER.

Pour en savoir plus sur l'algorithme CRC, consultez [cette](https://www.tutorialspoint.com/what-is-algorithm-for-computing-the-crc) page.

### Syntaxe de `cksum`

La commande `cksum` prend le nom de fichier comme argument et génère sa valeur de hachage. La syntaxe de base est la suivante :

```bash
cksum [FICHIER]
```

### Comment utiliser `cksum`

Supposons que nous avons un fichier nommé `calculator.py`. Nous pouvons calculer sa somme de contrôle comme ceci :

```bash
zaira@Zaira:~$ cksum calculator.py
1991291549 262 calculator.py
```

Dans la sortie, nous obtenons trois colonnes :

* La première colonne est la valeur de hachage.
* La deuxième valeur est la quantité de données en octets pour le fichier donné.
* La troisième colonne est le nom du fichier.

Même une légère modification change la valeur de hachage. Voyons à quoi cela ressemble avec un exemple.

Modifions notre fichier original `calculator.py` en ajoutant une ligne supplémentaire à la fin :

```bash
zaira@Zaira:~$ echo >> "ce fichier est maintenant changé" >> calculator.py
```

Recalculons la somme de contrôle et voyons si la valeur de hachage a changé :

```bash
zaira@Zaira:~$ cksum calculator.py
331872555 263 calculator.py
```

La première colonne est la valeur de hachage et elle a changé depuis que nous avons ajouté le texte.

Maintenant, nous savons que le fichier a changé car les valeurs de hachage de la somme de contrôle ne sont plus les mêmes.

Nous pouvons utiliser la même méthode pour comparer des fichiers avec le même nom, la même taille et la même heure de modification sur différentes machines pour nous assurer que les deux fichiers sont identiques.

## Conclusion

Il existe des cas où vous devez comparer les fichiers entre systèmes, surtout lorsqu'ils sont transférés d'un emplacement à un autre. Nous pouvons utiliser une combinaison des trois méthodes pour vérifier si notre fichier est intact :

* Voir l'heure de modification du fichier.
* Vérifier la taille du fichier.
* Générer et comparer la valeur de hachage en utilisant `cksum`.

J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu jusqu'à la fin.

Quelle est la chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).