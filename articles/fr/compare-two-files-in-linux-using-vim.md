---
title: Commande Linux `Vimdiff` – Comment comparer deux fichiers en ligne de commande
subtitle: ''
author: Zaira Hira
co_authors: []
series: null
date: '2022-08-08T20:08:39.000Z'
originalURL: https://freecodecamp.org/news/compare-two-files-in-linux-using-vim
coverImage: https://www.freecodecamp.org/news/content/images/2022/08/Copy-of-Cast-a-Function-in-SQL
seo_title: Commande Linux `Vimdiff` – Comment comparer deux fichiers en ligne de commande
---

Convert-Char-to-Int-SQL-Server-Example--3-.png
étiquettes:
- name: ligne de commande
  slug: command-line
- name: Linux
  slug: linux
- name: vim
  slug: vim
seo_title: null
seo_desc: "Le développement et la maintenance de logiciels peuvent parfois devenir compliqués. Et vous pourriez vous retrouver à comparer du code ou des changements de configuration. \nLorsque vous les comparez manuellement, vous pourriez faire une erreur, et il est facile de manquer des changements minimes. \nEn plus de cela,..."
---

Le développement et la maintenance de logiciels peuvent parfois devenir compliqués. Et vous pourriez vous retrouver à comparer du code ou des changements de configuration. 

Lorsque vous les comparez manuellement, vous pourriez faire une erreur, et il est facile de manquer des changements minimes. En plus de cela, trouver des changements dans de grands fichiers peut être épuisant. 

Il existe de nombreux outils en ligne et éditeurs de texte qui vous aident à comparer efficacement des fichiers. Mais il existe une méthode plus simple et sans tracas pour comparer des fichiers en utilisant la ligne de commande Linux. 

La ligne de commande Linux est très puissante et fournit un utilitaire de comparaison de fichiers dans `vim` pour différencier les fichiers côte à côte.

Apprendre à comparer des fichiers en ligne de commande est utile car de nombreux serveurs utilisent uniquement une CLI (Interface en Ligne de Commande). Cela signifie que vous n'avez pas le luxe d'une interface graphique où vous pouvez exécuter le navigateur ou d'autres éditeurs de texte.

## Qu'est-ce que vimdiff ?

`Vimdiff` est une commande Linux qui peut éditer deux, trois ou quatre versions d'un fichier avec `Vim` et montrer leurs différences.

### Syntaxe de `Vimdiff`

Pour comparer deux fichiers, la syntaxe est la suivante :

```bash
 vimdiff [options] fichier1 fichier2
```

Comparons deux fichiers `index.js` et `index.js.bkp` pour voir leurs différences.

```bash
vimdiff index.js index.js.bkp 
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-13.png)
_Sortie de `Vimdiff`_

Ici, nous pouvons voir la différence dans la ligne surlignée. 

Pour faciliter les choses, nous pouvons également afficher le numéro de ligne. Lorsque vous êtes dans `Vim`, passez en mode commande étendu en appuyant deux fois sur échap et en tapant `:set number`. Cela révèlera les numéros de ligne pour la session en cours.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-14.png)
_Numéros de ligne dans `vim`_

Examinons de plus près la sortie à nouveau :

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-16.png)
_Sortie détaillée de `vimdiff`._

* **Lignes non repliées :** Ce sont les lignes de code qui n'ont pas été modifiées. Elles sont enveloppées et peuvent être dépliées en utilisant une combinaison des touches `z+c` et `z+o`.
* **Changements surlignés :** Ce sont les différences présentes dans un fichier.
* **Numéros de ligne :** Ce sont les numéros de ligne correspondants dans les fichiers.
* **Noms de fichiers :** Le nom de fichier à gauche est le premier nom de fichier mentionné dans la commande. Le nom de fichier à droite est le deuxième nom de fichier fourni dans la commande.

Il existe également un moyen d'activer les numéros de ligne dans Vim par défaut afin de ne pas avoir à les définir manuellement à chaque fois.

### Comment afficher les numéros de ligne par défaut dans Vim sur Linux

Si vous souhaitez voir les numéros de ligne par défaut dans `Vim`, vous pouvez suivre ces étapes :

1. Localisez le fichier `vimrc`.

Les configurations de `Vim` sont présentes dans le fichier `vimrc`. L'emplacement du fichier peut varier d'une distribution Linux à l'autre. Dans Ubuntu, le fichier `vimrc` est situé dans `/usr/share/vim/`.

2.  Modifiez le fichier `vimrc`.

Ajoutez simplement `set number` dans le fichier et sauvegardez et quittez.

Maintenant, chaque fois que vous ouvrez `Vim`, les numéros de ligne seront là par défaut. 

## Opérations de `Vimdiff`

Voyons comment nous pouvons utiliser les pouvoirs de `vimdiff`. 

Tout d'abord, assurez-vous d'être en mode commande.

Vous pouvez passer en mode commande en appuyant deux fois sur la touche `échap`.

### Comment diviser les écrans horizontalement

Par défaut, `vimdiff` divise l'écran verticalement. Si vous souhaitez voir les fichiers divisés horizontalement, vous pouvez utiliser le drapeau `-o` comme ceci :

```bash
vimdiff -o index.js index.js.bkp
```

**Sortie :**

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-17.png)
_Division horizontale_

### Comment naviguer dans la fenêtre de diff

* Naviguer entre les fenêtres de diff

Pour naviguer entre les panneaux, utilisez une combinaison de touches `Ctrl+W+W`. Le curseur passera d'un fichier à l'autre une fois que vous aurez pressé les touches.

* Sauter aux changements

Au lieu de faire défiler ligne par ligne et de rechercher les changements, vous pouvez sauter au changement avec une combinaison de touches spécifique. 

1. Pour aller au changement précédent, utilisez : `[ + c`.
2. Pour aller au changement suivant, utilisez : `] + c`

### Comment appliquer les changements depuis la fenêtre de diff

* Pour appliquer les changements du fichier de gauche au fichier de droite :

Pour appliquer les changements du fichier de gauche au fichier de droite, déplacez-vous d'abord vers le changement surligné. Ensuite, utilisez la commande :

`:diffput`

Rappelez-vous que vous devrez être en mode commande.

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-18.png)
_Utilisation de `diffput` pour appliquer les changements de gauche à droite._

* Pour appliquer les changements du fichier de droite au fichier de gauche :

Pour appliquer les changements du fichier de droite au fichier de gauche, déplacez-vous d'abord vers le changement surligné. Ensuite, utilisez la commande :

`:diffget`

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-19.png)
_Utilisation de `diffget` pour appliquer les changements de droite à gauche._

### Comment annuler les changements

Si vous faites une erreur, vous pouvez annuler les changements à condition de ne pas avoir sauvegardé le fichier.

Lorsque vous êtes en mode commande, appuyez sur `u` pour annuler le dernier changement.

Si vous avez récemment annulé un changement, vous ne pourrez pas voir les changements surlignés comme avant. Vous devrez actualiser pour voir les changements une fois de plus. Vous pouvez le faire en utilisant la commande :

`:diffupdate`

### Comment ouvrir et fermer les plis

Les lignes non modifiées sont enveloppées pour une meilleure lisibilité. 

![Image](https://www.freecodecamp.org/news/content/images/2022/08/image-33.png)

Pour voir les lignes dépliées comme montré ci-dessus, déplacez le curseur à cet endroit et utilisez les combinaisons de touches suivantes :

* Pour ouvrir les plis : `z + o`.
* Pour fermer les plis : `z + c`.

### Comment quitter la fenêtre de diff

Il existe plusieurs façons de quitter la fenêtre de diff en fonction du résultat final.

* `:qa` pour quitter tous les fichiers sans sauvegarder.
* `:q` pour quitter les fichiers un par un sans sauvegarder.
* `:wq!` pour sauvegarder et quitter les fichiers un par un.

## Conclusion

Comparer des fichiers est facile et rapide avec `vimdiff` car nous comparons des fichiers dans la ligne de commande. Dans ce tutoriel, vous avez appris comment utiliser la commande `vimdiff` pour trouver efficacement les différences dans le code ou les fichiers de configuration. 

J'espère que vous avez trouvé ce tutoriel utile. Merci d'avoir lu jusqu'à la fin.

Quelle est votre chose préférée que vous avez apprise dans ce tutoriel ? Faites-le moi savoir sur [Twitter](https://twitter.com/hira_zaira) !

Vous pouvez également lire mes autres articles [ici](https://www.freecodecamp.org/news/author/zaira/).

<sub>Crédits image :
Vecteur de programmation créé par storyset - www.freepik.com</sub>