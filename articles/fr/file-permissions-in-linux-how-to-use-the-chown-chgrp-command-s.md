---
title: Permissions de fichiers sous Linux – Comment utiliser les commandes chown et
  chgrp
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-01-13T16:25:20.000Z'
originalURL: https://freecodecamp.org/news/file-permissions-in-linux-how-to-use-the-chown-chgrp-command-s
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/BB
seo_title: Permissions de fichiers sous Linux – Comment utiliser les commandes chown
  et chgrp
---

Manage-Users-and-Groups-in-Linux.png
tags:
- name: Linux
  slug: linux
seo_title: null
seo_desc: "En ce qui concerne les grandes organisations, les utilisateurs et les groupes sous Linux jouent un rôle important pour aider à maintenir les systèmes sécurisés et fonctionnant correctement. Il peut y avoir différents niveaux d'utilisateurs dans une organisation avec différents rôles et permissions. Et vous aurez besoin d'une bonne compréhension des permissions Linux pour les gérer et/ou les comprendre."
---

En ce qui concerne les grandes organisations, les utilisateurs et les groupes sous Linux jouent un rôle important pour aider à maintenir les systèmes sécurisés et fonctionnant correctement. 

Il peut y avoir différents niveaux d'utilisateurs dans une organisation avec différents rôles et permissions. Et vous aurez besoin d'une bonne compréhension des permissions Linux pour les gérer et/ou les comprendre.

Pour protéger les fichiers et les répertoires sous Linux contre l'accès par certains types d'utilisateurs, nous pouvons utiliser les commandes `chown` et `chgrp`. Ces commandes vous permettent de gérer quel type d'utilisateur peut lire, écrire et exécuter un fichier.

Avant de discuter des spécificités de ces commandes, cependant, vous devez comprendre les bases de fonctionnement des groupes et des utilisateurs sous Linux. Vous devrez également savoir comment vous pouvez manipuler les permissions pour eux.

Plongeons dans le sujet sans plus tarder. 

## Qu'est-ce que les groupes et les utilisateurs sous Linux ?

Un utilisateur est une entité régulière qui peut manipuler des fichiers, des répertoires et effectuer divers types d'actions dans un système. Nous pouvons créer n'importe quel nombre d'utilisateurs sous Linux.

Un groupe contient zéro ou plusieurs utilisateurs. Les utilisateurs d'un groupe partagent les mêmes permissions. Le groupe vous permet de définir des permissions au niveau du groupe au lieu de devoir définir des permissions pour chaque utilisateur individuel.

Considérons un scénario dans le développement logiciel où une machine est utilisée par divers types de personnes comme les administrateurs, les développeurs et les testeurs.

Chaque personne doit avoir un niveau d'accès individuel aux fichiers du système. En conséquence, il y aura un ensemble commun de permissions pour les développeurs, les testeurs et les administrateurs, dans leurs groupes respectifs. 

Disons qu'il y a 10 développeurs et 8 testeurs dans votre équipe et que vous utilisez 1 ordinateur partagé (chacun de vous a aussi un laptop).

Vous voulez créer un fichier qui doit être accessible uniquement aux développeurs. Pouvez-vous y parvenir sans utiliser le concept de groupes ? Oui – c'est faisable. Mais cela signifie que vous devrez attribuer des permissions individuellement à chaque développeur.

Le lendemain, disons que vous apprenez que votre équipe s'agrandit à 150 développeurs et 20 testeurs en raison d'une exigence immédiate du client.

Encore une fois, vous pourriez attribuer toutes ces permissions supplémentaires individuellement. Mais ce n'est pas scalable. C'est si fastidieux de gérer les permissions pour chaque développeur – alors pourquoi ne pas tout faire ensemble s'ils partagent des permissions communes ?

Voici l'utilité des groupes. Si nous avons tous les 10 (ou 150) développeurs dans un groupe appelé `dev_group`, nous pouvons simplement donner la permission au groupe `dev_group`. 

Il y a d'autres cas d'utilisation en dehors des permissions pour les groupes, mais nous n'entrerons pas dans cela ici.

## Qu'est-ce que les groupes primaires et secondaires sous Linux ? 

Comme le nom l'indique, un groupe primaire est un groupe auquel un utilisateur appartient par défaut. 

Par exemple, supposons que votre nom d'utilisateur est `arun`, et que vous créez un groupe appelé `admin`. Alors vous appartiendrez au groupe `admin` par défaut. 

Un groupe secondaire est un groupe auquel vous pouvez ajouter n'importe quel nombre d'utilisateurs.

## Comment créer un utilisateur

Vous pouvez créer un utilisateur en utilisant la commande `useradd`. Chaque utilisateur dans un système Linux a un identifiant utilisateur unique. 

```bash
useradd [OPTIONS] <nom_utilisateur>
```

Créons un nouvel utilisateur nommé `developer` :

```bash
useradd developer
```

## Comment créer un groupe

Les groupes sont créés en utilisant la commande `groupadd`. Similaire aux utilisateurs, chaque groupe dans un système Linux a un identifiant de groupe unique. 

```
groupadd [OPTIONS] <nom_groupe>
```

Créons un nouveau groupe nommé `developers_group` :

```
groupadd developers_group
```

## Comment ajouter un utilisateur à un groupe

Nous avons donc créé un utilisateur et un groupe. Ajoutons l'utilisateur (`developer`) au groupe (`developers_group`). La commande pour ajouter un utilisateur à un groupe est `usermod -aG`. 

```bash
sudo usermod -aG <nom_groupe> <nom_utilisateur>
```

Voici la commande réelle pour ajouter l'utilisateur `developer` au groupe `developers_group` :

```bash
sudo usermod -aG developers_group developer
```

## Comment lister les groupes

Vous vous demandez peut-être comment vérifier si le groupe créé existe, et comment vérifier si l'utilisateur a été ajouté au groupe. La liste des groupes et des utilisateurs qui ont des permissions dans le groupe sont stockés dans un fichier appelé `group`. Il sera situé dans le répertoire `/etc`. 

Nous pouvons voir les groupes disponibles en lisant ce fichier en utilisant la commande `cat` comme ceci :

```bash
cat /etc/group
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-40.png)
_Début du fichier `group`_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-41.png)
_Fin du fichier `group`_

Ce sera un fichier énorme. Par défaut, il contient 70 à 100 lignes. J'ai donc recadré le haut et le bas de la sortie de la commande dans les captures d'écran ci-dessus. 

Les deux dernières lignes de la capture d'écran ci-dessus décrivent qu'il y a un nouvel utilisateur appelé `developer`, un nouveau groupe appelé `developers_group`, et que l'utilisateur `developer` a été ajouté au groupe `developers_group`. 

## Comment trouver le propriétaire actuel et le groupe propriétaire d'un fichier 

Il existe une commande puissante – et probablement familière – sous Linux qui montre les permissions impliquées dans un fichier/répertoire. Il s'agit de la commande `ls -l` :

```bash
ls -l test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-42.png)
_Propriété du fichier `test.sh`_

Passons en revue la sortie séparée par des espaces et comprenons chaque partie :

* `-rw-rw-r-- 1` – Permission pour le fichier test.sh
* 1ère occurrence de `gogosoon` – Propriétaire du fichier
* 2ème occurrence de `gogosoon` – Groupe propriétaire du fichier

## Comment changer le propriétaire d'un fichier ou d'un répertoire

Vous pouvez utiliser la commande `chown` pour changer le propriétaire d'un fichier. La commande `chown` est l'abréviation de "change owner".  

Dans notre exemple précédent, nous avons vu le fichier `test.sh` appartenant à l'utilisateur nommé `gogosoon`.  

```bash
chown <nom_utilisateur> <nom_fichier>
```

Changeons la propriété du fichier à l'utilisateur `admin` en utilisant la commande `chown`. Nous pouvons faire cela comme ceci :

```bash
sudo chown admin test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-43.png)
_Changer le propriétaire du fichier `test.sh` en utilisant la commande `chown`_

D'après la capture d'écran ci-dessus, vous pouvez clairement voir que le propriétaire du fichier `test.sh` a été changé de `gogosoon` à `admin`. 

## Comment copier la propriété d'un fichier à un autre 

J'ai rencontré ce scénario une fois dans ma carrière. Nous utilisons un système commun dans certains cas d'utilisation rares. Voici ce qui se passait :

Un jour, je travaillais sur ce système pour compléter une POC qui nécessitait de créer des centaines de fichiers avec une propriété d'utilisateur différente. Un fichier était créé avec des permissions par défaut (m'appartenant) chaque fois qu'il était créé. 

Mais je veux que le fichier appartienne à un autre utilisateur. J'étais trop paresseux pour changer la propriété de chaque fichier manuellement. Si je changeais la propriété d'un fichier, je voulais pouvoir copier la même propriété pour d'autres fichiers. J'étais sûr qu'il devait y avoir une commande qui me permettait de faire cela. 

J'ai donc fait une recherche rapide sur Google pour savoir comment copier la propriété d'un fichier à un autre. Après quelques secondes, j'ai trouvé la solution et c'était si simple. Vous pouvez faire cela en ajoutant un drapeau `--reference`. 

```bash
chown --reference=<nom_fichier_source> <nom_fichier_destination>
```

Explorons cela avec un exemple :

Créons un nouveau fichier nommé `copy.sh` avec mon compte utilisateur `gogosoon`. 

Le propriétaire du fichier `test.sh` est l'utilisateur `admin` (d'après notre exemple précédent). Je veux que la propriété du fichier `test.sh` soit copiée vers le fichier nouvellement créé `copy.sh` qui appartient à l'utilisateur `gogosoon`. 

```bash
sudo chown --reference=test.sh copy.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-44.png)
_Propriété du fichier `test.sh` copiée vers le fichier `copy.sh`_

D'après la capture d'écran ci-dessus, vous pouvez voir que la première commande décrit la propriété du fichier `test.sh`, qui appartient à l'utilisateur `admin`. 

La deuxième commande décrit la propriété du fichier `copy.sh` qui appartient à l'utilisateur `gogosoon`. 

La troisième commande copie la propriété du fichier `test.sh` vers le fichier `copy.sh`. 

La dernière commande décrit à nouveau la propriété du fichier `copy.sh` qui appartient maintenant à l'utilisateur `admin`. 

Vous vous demandez peut-être qu'au début j'ai dit que j'avais créé des centaines de fichiers – mais comment ai-je changé la propriété de tous les fichiers en une seule fois ? 

C'est une autre histoire. Mais voici une réponse rapide : j'ai écrit un script qui a parcouru tous les fichiers et changé la propriété en référençant un seul fichier maître. 

## Comment changer la propriété de plusieurs fichiers avec une seule commande

Vous pouvez faire cela en passant plusieurs noms de fichiers à la commande `chown` avec un nom d'utilisateur. Cela définit la propriété de tous les fichiers donnés à cet utilisateur particulier. 

```bash
sudo chown <nom_utilisateur> fichier1 fichier2 ...
```

Voici un exemple où je veux définir la propriété des fichiers `copy.sh` et `test.sh` à l'utilisateur `admin` :

```bash
sudo chown admin copy.sh test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-45.png)
_Définir la propriété des fichiers `copy.sh` et `test.sh` à l'utilisateur `admin`_

## Comment changer le groupe propriétaire d'un fichier

Presque toutes les opérations liées aux groupes peuvent être réalisées avec la commande `chgrp` (une abréviation de "change group"). Elle est assez similaire à la commande `chown`. 

Syntaxe de la commande `chgrp` :

```bash
sudo chgrp <nom_groupe> <nom_fichier/répertoire>
```

J'ai déjà créé un groupe appelé `admin`. Je n'appartiens pas à ce groupe. Changeons le groupe propriétaire du fichier `test.sh` de `gogosoon` au groupe `admin`. 

```bash
sudo chgrp admin test.sh
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-46.png)
_Changer le groupe propriétaire du fichier `test.sh` en `admin`_

D'après la capture d'écran ci-dessus, vous pouvez voir que j'ai changé le groupe propriétaire du fichier `test.sh` de `gogosoon` à `admin`. Comme je n'appartiens pas à ce groupe, je n'aurai pas d'accès en écriture au fichier. 

Vérifions cela en ouvrant le fichier en mode écriture en utilisant `nano test.sh` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-47.png)
_Vous pouvez voir que je n'ai pas de permission d'écriture pour ce fichier_

## Comment changer le groupe propriétaire d'un répertoire 

La même syntaxe pour les fichiers est applicable aux répertoires. Voici un exemple rapide :

```bash
sudo chgrp test group_test/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-48.png)
_Changer le groupe propriétaire du répertoire `group_test` en groupe `test`_

Mais rappelez-vous que la commande ci-dessus change le groupe propriétaire uniquement des fichiers de ce répertoire. Pour changer récursivement les permissions de groupe de tous les répertoires à l'intérieur de ce répertoire, nous devons ajouter le drapeau `-R` comme ceci :

```
sudo chgrp -R admin group_test/
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-51.png)

Maintenant, le groupe propriétaire de tous les fichiers et répertoires à l'intérieur de group_test a été changé de `gogosoon` à `admin`. 

Vérifions la sortie en essayant d'écrire un fichier à partir du répertoire `group_test` en tant qu'utilisateur `gogosoon` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-52.png)
_Essayer de modifier les fichiers `hello1.sh` et `hello3.sh`_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-53.png)
_Erreur montrant que le fichier `hello1.sh` n'est pas accessible en écriture_

![Image](https://www.freecodecamp.org/news/content/images/2023/01/image-54.png)
_Erreur montrant que le fichier `hello3.sh` n'est pas accessible en écriture_

Hourra ! La propriété a été appliquée correctement. 

## Conclusion

Dans cet article, vous avez appris à gérer la propriété des utilisateurs et des groupes pour les fichiers et les dossiers. J'espère que vous avez apprécié sa lecture. 

Abonnez-vous à ma newsletter en visitant mon [site](https://5minslearn.gogosoon.com/?ref=fcc_grp_own_blog) et consultez également la liste consolidée de tous mes blogs. 

Santé !