---
title: Comment rechercher des fichiers depuis la ligne de commande Linux
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-03-17T19:55:40.000Z'
originalURL: https://freecodecamp.org/news/how-to-search-for-files-from-the-linux-command-line
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/Copy-of-remove-key-val.gif
tags:
- name: command line
  slug: command-line
- name: Linux
  slug: linux
seo_title: Comment rechercher des fichiers depuis la ligne de commande Linux
seo_desc: 'Searching for files is relatively easy when you are using a GUI. But in
  certain environments like GUI-less servers, you need to search for files using the
  command line.

  There is a powerful command in Linux that helps you search for files and folders
  ...'
---

La recherche de fichiers est relativement facile lorsque vous utilisez une interface graphique (GUI). Mais dans certains environnements comme les serveurs sans interface graphique, vous devez rechercher des fichiers en utilisant la ligne de commande.

Il existe une commande puissante sous Linux qui vous aide à rechercher des fichiers et des dossiers appelée `find`. Dans cet article, nous allons aborder la commande `find` avec quelques exemples.

## Qu'est-ce que la commande find sous Linux ?

La commande `find` vous permet de rechercher efficacement des fichiers, des dossiers, ainsi que des périphériques de caractères et de blocs. 

Voici la syntaxe de base de la commande `find` :

```bash
find /path/ -type f -name file-to-search

```

Où :

* `/path` est le chemin où le fichier est censé se trouver. C'est le point de départ pour la recherche de fichiers. Le chemin peut également être `/` ou `.` qui représentent respectivement la racine et le répertoire courant.
* `-type` représente les descripteurs de fichiers. Ils peuvent être l'un des suivants :

	`f` – **Fichier régulier** tel que les fichiers texte, les images et les fichiers cachés.

	`d` – **Répertoire**. Ce sont les dossiers pris en compte.

	`l` – **Lien symbolique**. Les liens symboliques pointent vers des fichiers et sont similaires à des raccourcis.

	`c` – **Périphériques de caractères**. Les fichiers utilisés pour accéder aux périphériques de caractères sont appelés fichiers de périphériques de caractères. Les pilotes communiquent avec les périphériques de caractères en envoyant et en recevant des caractères uniques (octets). Les exemples incluent les claviers, les cartes son et les souris.

	`b` – **Périphériques de blocs**. Les fichiers utilisés pour accéder aux périphériques de blocs sont appelés fichiers de périphériques de blocs. Les pilotes communiquent avec les périphériques de blocs en envoyant et en recevant des blocs entiers de données. Les exemples incluent les clés USB, les CD-ROM.

* `-name` est le nom du type de fichier que vous souhaitez rechercher.

## Exemples de la commande find

Maintenant que nous connaissons la syntaxe de la commande `find`, regardons quelques exemples.

### Comment rechercher des fichiers par nom ou extension

Supposons que nous devions trouver des fichiers contenant "style" dans leur nom. Nous utiliserons cette commande :

```bash
find . -type f -name "style*"
```

**Résultat**

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-2.png)

Maintenant, disons que nous voulons trouver des fichiers avec une extension particulière comme `.html`. Nous modifierons la commande comme ceci :

```bash
find . -type f -name "*.html"
```

**Résultat**

![Image](https://www.freecodecamp.org/news/content/images/2023/04/image-3.png)

### Comment rechercher des fichiers cachés

Les fichiers cachés sont représentés par un point au début du nom du fichier. Ils sont normalement masqués, mais peuvent être consultés avec `ls -a` dans le répertoire courant.

Nous pouvons modifier la commande `find` comme indiqué ci-dessous pour rechercher des fichiers cachés.

```bash
find . -type f -name ".*"
```

**Résultat**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-61.png)
_Liste des fichiers cachés dans mon répertoire personnel_

### Comment rechercher des fichiers journaux et des fichiers de configuration

Les fichiers journaux ont généralement l'extension `.log`, et nous pouvons les trouver comme ceci :

```bash
 find . -type f -name "*.log"
```

**Résultat**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-62.png)

De même, nous pouvons rechercher des fichiers de configuration comme ceci :

```bash
 find . -type f -name "*.conf"
```

### Comment rechercher d'autres fichiers par type

Nous pouvons rechercher des fichiers de blocs de caractères en fournissant `c` à `-type` :

```bash
find / -type c
```

De même, les fichiers de blocs de périphériques peuvent être trouvés en utilisant `b` :

```bash
find / -type b
```

### Comment rechercher des répertoires

Dans l'exemple ci-dessous, nous recherchons les dossiers nommés `lib`. Notez que nous utilisons `-type d`.

```bash
find . -type d -name "lib*"
```

**Résultat**

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-63.png)

💡 Astuce : nous pouvons identifier les répertoires en regardant le drapeau `d` dans la sortie de `ls -lrt`.

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-64.png)

### Comment rechercher des fichiers par taille

Une utilisation incroyablement utile de la commande `find` consiste à lister les fichiers en fonction d'une taille particulière.

```bash
find / -size +250M
```

Les autres unités incluent :

* `G` : GigaOctets.
* `M` : MégaOctets. 
* `K` : KiloOctets 
* `c` : octets.

Remplacez simplement <Unit Type> par l'unité correspondante.

```bash
find <directory> -type f -size +N<Unit Type>

```

### Comment rechercher des fichiers par date de modification

```bash
find /path -name "*.txt" -mtime -10 


```

* **-mtime +10** signifie que vous recherchez un fichier modifié il y a plus de 10 jours.
* **-mtime -10** signifie moins de 10 jours.
* **-mtime 10** Si vous omettez + ou –, cela signifie exactement 10 jours.

Voici le contenu de mon répertoire personnel :

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-65.png)

Appliquons un exemple dans mon répertoire personnel.

```bash
find . -type f -name ".*" -mtime +10
```

![Image](https://www.freecodecamp.org/news/content/images/2022/03/image-66.png)
_Ici, nous avons des fichiers qui ont été modifiés il y a plus de 10 jours._

## Exemples pratiques de `find` avec des scripts bash

Nous pouvons combiner `find` avec `rm` ou `mv` pour créer des scripts bash utiles qui peuvent être automatisés.

Disons que nous voulons créer un script qui déplace les fichiers journaux de plus de 7 jours vers un chemin de sauvegarde. De là, il supprime les fichiers journaux de plus de 30 jours. Nous pouvons créer un script et le planifier avec `cron`. Vous pouvez en savoir plus sur les tâches `cron` [ici](https://www.freecodecamp.org/news/cron-jobs-in-linux/).

Voyons le script :

```bash
#!/bin/bash
# Script pour déplacer les journaux de plus de 7 jours vers le chemin de sauvegarde : /app/backup_logs/ESB0*

# déplacer les journaux ESB01 vers la sauvegarde
find /logs/esb01/audit  -name "*.tar.gz" -mtime +7 -exec mv {} app/backup_logs/ESB01/ \;

# Supprimer les journaux du chemin de sauvegarde après 30 jours
find /app/backup_logs/ESB01 -name "*.tar.gz" -mtime +30  -exec rm {} \;

```

Notez que nous utilisons `exec` avec `find`. Fondamentalement, `exec` exécute la commande fournie (`mv` et `rm` dans notre cas). `{}` est l'espace réservé qui contient les résultats de la commande. Enfin, nous fournissons le délimiteur `;`. Comme nous ne voulons pas que le shell interprète le point-virgule, nous l'échappons avec `\`.

Le script partagé est très utile pour l'archivage et la suppression des journaux.

## Conclusion

Dans cet article, nous avons étudié la commande `find` en détail et appris comment rechercher des fichiers par nom, type, taille et date de modification.

J'espère que vous avez trouvé ce tutoriel utile.

Partagez vos réflexions sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

Ressources : Images de bannière provenant de [Office illustrations by Storyset](https://storyset.com/office) et Canva.