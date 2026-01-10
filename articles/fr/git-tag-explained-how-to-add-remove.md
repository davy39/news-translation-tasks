---
title: 'Explication des balises Git : comment lister, créer, supprimer et afficher
  les balises dans Git'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-18T18:10:00.000Z'
originalURL: https://freecodecamp.org/news/git-tag-explained-how-to-add-remove
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dc7740569d1a4ca3993.jpg
tags:
- name: Git
  slug: git
seo_title: 'Explication des balises Git : comment lister, créer, supprimer et afficher
  les balises dans Git'
seo_desc: 'Tagging lets developers mark important checkpoints in the course of their
  projects'' development. For instance, software release versions can be tagged. (Ex:
  v1.3.2) It essentially allows you to give a commit a special name(tag).

  To view all the creat...'
---

Les balises permettent aux développeurs de marquer des points de contrôle importants dans le cours du développement de leurs projets. Par exemple, les versions de publication de logiciels peuvent être balisées. (Ex: v1.3.2) Cela vous permet essentiellement de donner un nom spécial (balise) à un commit.

Pour afficher toutes les balises créées par ordre alphabétique :

```bash
git tag
```

Pour obtenir plus d'informations sur une balise :

```bash
git show v1.4
```

Il existe deux types de balises :

Annotées

```bash
git tag -a v1.2 -m "ma version 1.4"
```

Légères

```bash
git tag v1.2
```

Elles diffèrent par la manière dont elles sont stockées.  
Celles-ci créent des balises sur votre commit actuel.

Au cas où vous souhaiteriez baliser un commit précédent, spécifiez l'ID du commit que vous souhaitez baliser :

```bash
git tag -a v1.2 9fceb02
```

Les noms des balises peuvent être utilisés à la place des ID de commit lors de la vérification et de l'envoi de commits vers un dépôt distant.

#### **Plus d'informations :**

* Documentation Git : [Documentation](https://git-scm.com/docs/git-tag)
* Chapitre sur les balises Git : [Livre](https://git-scm.com/book/en/v2/Git-Basics-Tagging)

Vous pouvez lister toutes les balises disponibles dans un projet avec la commande `git tag` (notez qu'elles apparaîtront par ordre alphabétique) :

```text
$ git tag
v1.0
v2.0
v3.0
```

Cette façon de lister les balises est idéale pour les petits projets, mais les grands projets peuvent avoir des centaines de balises, vous devrez donc peut-être les filtrer lors de la recherche d'un point important dans l'historique. Vous pouvez trouver des balises contenant des caractères spécifiques en ajoutant un `-l` à la commande `git tag` :

```text
$ git tag -l "v2.0*"
v2.0.1
v2.0.2
v2.0.3
v2.0.4
```

## **Créer une balise**

Vous pouvez créer deux types de balises : annotées et légères. Les premières sont des objets complets dans la base de données GIT : elles sont vérifiées par somme de contrôle, nécessitent un message (comme les commits) et stockent d'autres données importantes telles que le nom, l'email et la date. En revanche, les balises légères ne nécessitent pas de message ni ne stockent d'autres données, fonctionnant simplement comme un pointeur vers un point spécifique du projet.

### **Créer une balise annotée**

Pour créer une balise annotée, ajoutez `-a tagname -m "tag message"` à la commande `git tag` :

```text
$ git tag -a v4.0 -m "version de publication 4.0"
$ git tag
v1.0
v2.0
v3.0
v4.0
```

Comme vous pouvez le voir, le `-a` spécifie que vous créez une balise annotée, suivi du nom de la balise et enfin, le `-m` suivi du message de la balise à stocker dans la base de données Git.

### **Créer une balise légère**

Les balises légères contiennent uniquement la somme de contrôle du commit (aucune autre information n'est stockée). Pour en créer une, exécutez simplement la commande `git tag` sans aucune autre option (les caractères -lw à la fin du nom sont utilisés pour indiquer les balises légères, mais vous pouvez les marquer comme vous le souhaitez) :

```text
$ git tag v4.1-lw
$ git tag
v1.0
v2.0
v3.0
v4.0
v4.1-lw
```

Cette fois, vous n'avez pas spécifié de message ni d'autres données pertinentes, donc la balise contient uniquement la somme de contrôle du commit référencé.

## **Voir les données d'une balise**

Vous pouvez exécuter la commande `git show` pour afficher les données stockées dans une balise. Dans le cas des balises annotées, vous verrez les données de la balise et les données du commit :

```text
$ git show v4.0
tag v4.0
Tagger: John Cash <john@cash.com>
Date:   Mon Sat 28 15:00:25 2017 -0700

version de publication 4.0

commit da43a5fss745av88d47839247990022a98419093
Author: John Cash <john@cash.com>
Date:   Fri Feb 20 20:30:05 2015 -0700

  détails terminés
```

Si la balise que vous consultez est une balise légère, vous ne verrez que les données du commit référencé :

```text
$ git show v1.4-lw
commit da43a5f7389adcb9201ab0a289c389ed022a910b
Author: John Cash <john@cash.com>
Date:   Fri Feb 20 20:30:05 2015 -0700

  détails terminés
```

## **Baliser les anciens commits**

Vous pouvez également baliser les anciens commits en utilisant le commit de balise git. Pour ce faire, vous devrez spécifier la somme de contrôle du commit (ou au moins une partie de celle-ci) dans la ligne de commande.

Tout d'abord, exécutez git log pour trouver la somme de contrôle du commit requis :

```text
$ git log --pretty=oneline
ac2998acf289102dba00823821bee04276aad9ca added products section
d09034bdea0097726fd8383c0393faa0072829a7 refactorization
a029ac120245ab012bed1ca771349eb9cca01c0b modified styles
da43a5f7389adcb9201ab0a289c389ed022a910b finished details
0adb03ca013901c1e02174924486a08cea9293a2 small fix in search textarea styles
```

Lorsque vous avez la somme de contrôle nécessaire, ajoutez-la à la fin de la ligne de création de la balise :

```text
$ git tag -a v3.5 a029ac
```

Vous verrez que la balise a été correctement ajoutée en exécutant `git tag` :

```text
$ git tag
v1.0
v2.0
v3.0
v3.5
v4.0
v4.1-lw
```

## **Pousser les balises**

Git ne pousse pas les balises par défaut lorsque vous exécutez la commande git push. Donc, pour pousser une balise vers un serveur avec succès, vous devrez utiliser la commande `git push origin` :

```text
$ git push origin v4.0
Counting objects: 14, done.
Delta compression using up to 8 threads.
Compressing objects: 100% (16/16), done.
Writing objects: 100% (18/18), 3.15 KiB | 0 bytes/s, done.
Total 18 (delta 4), reused 0 (delta 0)
To git@github.com:jcash/gitmanual.git
 * [new tag]         v4.0 -> v4.0
```

Vous pouvez également utiliser l'option `--tags` pour ajouter plusieurs balises à la fois avec la commande `git push origin` :

```text
$ git push origin --tags
Counting objects: 1, done.
Writing objects: 100% (1/1), 160 bytes | 0 bytes/s, done.
Total 1 (delta 0), reused 0 (delta 0)
To git@github.com:jcash/gitmanual.git
 * [new tag]         v4.0 -> v4.0
 * [new tag]         v4.1-lw -> v4.1-lw
```

## **Vérifier les balises**

Vous pouvez utiliser `git checkout` pour vérifier une balise comme vous le feriez normalement. Mais vous devez garder à l'esprit que cela entraînerait un état de _HEAD détaché_.

```text
$ git checkout v0.0.3
Note: checking out 'v0.0.3'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.
```

## **Supprimer une balise**

Vous pouvez rencontrer une situation où vous souhaitez supprimer une certaine balise. Il existe une commande très utile pour ces situations :

```text
$ git tag --delete v0.0.2
$ git tag
v0.0.1
v0.0.3
v0.0.4
```

### **Plus d'informations**

* [Git Pro - Bases des balises](https://git-scm.com/book/en/v2/Git-Basics-Tagging)
* [Git Pro - Documentation](https://git-scm.com/docs/git-tag)
* [Git HowTo](https://githowto.com/tagging_versions)
* [Astuce Git : Balises](http://alblue.bandlem.com/2011/04/git-tip-of-week-tags.html)
* [Création d'une balise](https://www.drupal.org/node/1066342)

### **Sources**

Documentation Git : [balises](https://git-scm.com/book/en/v2/Git-Basics-Tagging)