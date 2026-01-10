---
title: Le Guide Essentiel de Git – Apprendre Git pour Débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-30T17:16:29.000Z'
originalURL: https://freecodecamp.org/news/the-essential-git-handbook-a1cf77ed11b5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*AhGSZ1spetb37qk_bZd9XA.png
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Le Guide Essentiel de Git – Apprendre Git pour Débutants
seo_desc: 'By Sanjula Madurapperuma

  Introduction

  Hi! I am Sanjula, and in this guide I hope to teach you a little bit about Git including:


  What Git is

  Why learn Git

  Setting configuration variables

  Introduction to the help command in Git

  How to convert an exist...'
---

Par Sanjula Madurapperuma

### Introduction

Bonjour ! Je suis [Sanjula](https://www.linkedin.com/in/sanjula-madurapperuma/), et dans ce guide, j'espère vous apprendre un peu sur Git, y compris :

* Qu'est-ce que Git
* Pourquoi apprendre Git
* Configurer les variables de configuration
* Introduction à la commande d'aide dans Git
* Comment convertir un projet existant en un dépôt Git local
* Choses à faire avant le premier commit
* Comment ajouter des fichiers à la zone de staging
* Comment supprimer des fichiers de la zone de staging
* Faire votre premier commit
* Comment cloner un dépôt distant
* Voir les informations sur le dépôt distant
* Comment pousser vos changements vers le dépôt distant
* Comment créer une branche pour une fonctionnalité ou un problème spécifique
* Pousser la branche vers le dépôt distant après le commit
* Comment fusionner une branche
* Comment supprimer une branche

Commençons !

### Qu'est-ce que Git ?

En termes simples, Git est un **système de contrôle de version distribué open-source**.

Les systèmes de contrôle de version aident toute équipe logicielle à gérer les changements apportés au code source d'un produit ou d'un service au fil du temps. Il garde une trace de toutes les modifications apportées au code source dans une base de données. Si une erreur critique a été commise dans le code source, les développeurs d'une équipe logicielle peuvent alors revenir à une version du code source avant que la modification erronée ne soit faite. Par conséquent, les systèmes de contrôle de version protègent le code source des catastrophes, des erreurs humaines et des conséquences involontaires (quand une correction de bug en casse une autre partie de l'application, par exemple).

### Pourquoi apprendre Git ?

Git est le système de contrôle de version le plus largement utilisé dans le monde aujourd'hui. C'est un projet open-source mature et activement maintenu, développé à l'origine par Linus Torvalds.

Une quantité impressionnante de projets logiciels dépendent de Git pour le contrôle de version, y compris les projets commerciaux et open-source, en particulier en utilisant le service d'hébergement de dépôts git, GitHub, qui est maintenant détenu par Microsoft. D'où l'importance d'apprendre Git.

### Prérequis pour ce guide

Téléchargez et installez git [**ici**](http://www.git-scm.com/downloads)

### Vérifier la version de git

```
git --version
```

![Image](https://cdn-media-1.freecodecamp.org/images/G81z00SqImj30aOmL1mnhLIa6tW08Xyws1z6)
_Figure-2: Version de Git_

Si le numéro de version est retourné, cela signifie que git est installé avec succès sur votre ordinateur.

### Configurer les valeurs de configuration

Maintenant, nous devons définir les variables de configuration globales, qui sont très importantes, surtout si vous travaillez avec d'autres développeurs. L'avantage principal est qu'il est plus facile de savoir qui a commis un certain bloc de code, par exemple.

```
git config --global user.name "Sanjula Madurapperuma"
```

```
git config --global user.email "sanjula@mail.com"
```

```
git config --list
```

### Commande d'aide

Comme vous l'avez peut-être remarqué, _config_ est un verbe qui a été utilisé fréquemment jusqu'à présent dans ce manuel, et les verbes peuvent également être utilisés comme préfixe ou suffixe avec la commande d'aide. Nous pouvons utiliser le même exemple (le verbe _config_) ci-dessus pour expliquer ces commandes.

```
git help config
```

```
git config --help
```

![Image](https://cdn-media-1.freecodecamp.org/images/TpOqdmWxNM11sihKZDfCBkvpqrPyO0QVMkhj)
_Figure-3: Commande d'aide_

Les deux commandes ci-dessus effectuent la même action. Elles affichent la page du manuel pour le verbe spécifié. Cela sera utile pour identifier des capacités plus avancées de git.

### Comment initialiser un dépôt à partir d'un code existant

Si vous avez un dépôt local que vous souhaitez convertir en un projet git pour commencer à le suivre, alors nous pouvons commencer par exécuter la commande suivante dans le répertoire du projet.

```
git init
```

![Image](https://cdn-media-1.freecodecamp.org/images/X5ju5iD8xMwFsvQ5xomZtkvkGbo2GCAWLYVQ)
_Figure-4: Git init_

Fini ! Tout simplement, vous avez converti votre projet en un dépôt git local. Si vous ouvrez le dossier du projet, vous verrez qu'un nouveau répertoire appelé .git a été créé.

### Que faire avant le premier commit

Entrez la commande suivante pour voir les fichiers non suivis :

```
git status
```

![Image](https://cdn-media-1.freecodecamp.org/images/A1cKNf7PUeDJ-SI2zyrkuH-g3NvF5YfHy-T7)
_Figure-5: Git status_

Si vous avez des fichiers que vous ne voulez pas que les autres voient dans le dépôt, comme les fichiers contenant des préférences personnelles ou celles de l'IDE, alors faites ce qui suit :

```
touch .gitignore
```

![Image](https://cdn-media-1.freecodecamp.org/images/AkaWuuihvkq5cE5P1r8E0QHOF6cgDzrQlJsy)
_Figure-6: Créer le fichier .gitignore_

Pour spécifier quels fichiers ne doivent pas être ajoutés au dépôt git, ouvrez un éditeur de texte et affichez le fichier .gitignore, qui peut être édité comme un fichier texte normal. Maintenant, nous pouvons entrer ce qui suit dans le fichier, par exemple :

```
.project
```

```
*.java
```

Les caractères génériques peuvent également être utilisés. Dans ce cas, il a été utilisé pour spécifier de ne pas ajouter tous les fichiers se terminant par l'extension .java au dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/Q3wRtlkpWsPt02lPztKmqDDVfWuKovzkZGL5)
_Figure-7: Édition dans l'éditeur de texte_

Maintenant, exécutez à nouveau git status

![Image](https://cdn-media-1.freecodecamp.org/images/V5AwN6ykf9r1dBZ87ViMbvschLJI2iTfBJ4t)
_Figure-8: Après la mise à jour de .gitignore_

Maintenant, vous pouvez voir que les fichiers que nous avons exclus dans le fichier .gitignore ne sont plus affichés dans la liste des fichiers non suivis. Le fichier .gitignore doit être commis dans le dépôt afin de maintenir les mêmes exclusions dans tous les autres endroits.

### Ajouter des fichiers à la zone de staging

Tout ce temps, nous étions dans le répertoire de travail. La zone de staging est l'endroit où nous organisons tous les fichiers qui sont suivis et doivent être commis avant d'être poussés vers le dépôt git. C'est un fichier qui stocke ce qui doit être inclus dans le prochain commit.

Si vous voulez ajouter tous les fichiers qui sont actuellement non suivis et que vous avez modifiés à la zone de staging, utilisez la commande suivante :

```
git add -A
```

Si vous voulez ajouter des fichiers individuellement, vous pouvez donner le nom du fichier après git add. Par exemple,

```
git add .gitignore
```

Maintenant, si vous tapez git status, vous verrez que le fichier .gitignore est maintenant dans la zone de staging.

![Image](https://cdn-media-1.freecodecamp.org/images/HaV5Fai1lvx-xPkdMRsRdCM8Gp8D8Ns6M5fX)
_Figure-9: Zone de staging_

### Supprimer des fichiers de la zone de staging

Pour supprimer des fichiers individuellement de la zone de staging, tapez ce qui suit (par exemple) :

```
git reset simple.py
```

Cela supprimera le fichier simple.py de la zone de staging. Pour voir ce changement, tapez à nouveau git status.

![Image](https://cdn-media-1.freecodecamp.org/images/hbseWQzJKSluv5zAwHbsj7gi6DBAWt6YBWwM)
_Figure-10: Supprimer un fichier de la zone de staging_

Si vous voulez supprimer tous les fichiers de la zone de staging, exécutez ce qui suit :

```
git reset
```

Maintenant, si nous tapons git status, nous verrons que tous les fichiers ont été changés en fichiers non suivis.

![Image](https://cdn-media-1.freecodecamp.org/images/aUpZJl-E8YA74eLlnf6en0ojS1ohWSil09wY)
_Figure-11: Réinitialiser tous les fichiers_

### Faire le premier commit

Maintenant, exécutez ce qui suit pour ajouter tous les fichiers à la zone de staging pour être commis.

```
git add -A
```

Si vous le souhaitez, vous pouvez exécuter git status pour voir tous les fichiers qui seront commis.

Pour commettre, tapez ce qui suit.

```
git commit -m "Initial Commit"
```

"-m" spécifie un message à passer décrivant le commit. Puisque c'est notre premier commit, nous dirons Initial Commit.

![Image](https://cdn-media-1.freecodecamp.org/images/lAHfY5GgwQEjkE8HBcuXiDGM9yDFdqxS0AvX)
_Figure-12: Initial Commit_

Comme vous pouvez le voir, les fichiers ont été commis avec succès.

Si vous exécutez git status maintenant, vous verrez qu'il dit que le répertoire de travail est propre parce que nous avons commis les fichiers et n'avons modifié aucun fichier depuis.

![Image](https://cdn-media-1.freecodecamp.org/images/UscWoVk2VszFJowNHo8kawe9dPqmanjl717h)
_Figure-13: Arbre de travail après commit_

Si nous exécutons la commande suivante :

```
git log
```

alors nous pouvons voir le commit que nous venons de faire, y compris le numéro de hachage du commit.

![Image](https://cdn-media-1.freecodecamp.org/images/cjCho8GR69IU5ACe0ghU7TsDOKFKuP4Flbjt)
_Figure-14: Numéro de hachage du commit_

Nous suivons maintenant avec succès le projet local avec git !

### Cloner un dépôt distant

Si nous voulons suivre un projet distant existant avec git, alors nous devons taper une commande dans le format suivant :

```
git clone <url> <où cloner>
```

Par exemple, j'utiliserai le dépôt git à [ce lien](https://github.com/sanjulamadurapperuma/GitDemoMedium.git).

Je vais d'abord me déplacer dans le répertoire où je veux cloner le projet, bien que vous puissiez spécifier cela comme montré ci-dessus également.

Allez au lien du dépôt donné ci-dessus et cliquez sur le bouton "Clone or Download", puis copiez le lien donné là.

Ensuite, entrez :

```
git clone https://github.com/sanjulamadurapperuma/GitDemoMedium.git
```

![Image](https://cdn-media-1.freecodecamp.org/images/lHzsIA1k-D5qeBSOciWt443gD3YClS8q8e9y)
_Figure-15: Cloner le dépôt distant_

Maintenant, nous avons cloné le dépôt avec succès.

Si nous entrons la commande suivante, nous verrons tous les fichiers qui sont dans le répertoire local maintenant.

```
ls -la
```

![Image](https://cdn-media-1.freecodecamp.org/images/2OMMDj4xttnnVsgamdc36jy5B2oopjLcSLsB)
_Figure-16: Lister tous les fichiers dans le répertoire_

### Voir les informations sur le dépôt distant

Si vous tapez la commande suivante :

```
git remote -v
```

![Image](https://cdn-media-1.freecodecamp.org/images/qkYzprJKHXHwd4KHfzDQwF3Sjj2Nh1niZIZU)
_Figure-17: Git remote -v_

Cette commande listera les emplacements où le dépôt local récupérera les commits externes et poussera vos commits vers le dépôt distant.

Si vous deviez taper la commande

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/ig6sDj8Y1Gzqm2UMsvRvbwZlxnVrtKy6MBBl)
_Figure-18: Lister toutes les branches git_

Cela listera toutes les branches qui sont dans le dépôt, à la fois localement et à distance.

Afin de démontrer la mise à jour du dépôt distant, nous allons apporter quelques modifications aux fichiers dans le dépôt que nous avons cloné.

![Image](https://cdn-media-1.freecodecamp.org/images/n7tWT09vfQnKeaxoN0XyCY1r9Ql4pbwUozXw)
_Figure-19: Apporter des modifications à simple.py_

Maintenant que nous avons apporté une modification à notre code, la prochaine action que nous devons faire est de pousser ces modifications vers le dépôt distant.

### Pousser les modifications vers le dépôt distant

La commande suivante montrera toutes les modifications qui ont été apportées aux fichiers.

```
git diff
```

![Image](https://cdn-media-1.freecodecamp.org/images/UiWSb3gZiGs5A7fBksCDIDHkt99puF551amJ)
_Figure-20: Voir les modifications du fichier_

Si nous entrons à nouveau git status, nous pouvons voir que les modifications ont été suivies et que simple.py a été modifié.

![Image](https://cdn-media-1.freecodecamp.org/images/n9A8DdvhDyKjllzgS2ExFYrM4FsofyoUA0gR)
_Figure-21: Voir les fichiers modifiés_

Maintenant, ajoutez-les à la zone de staging

```
git add -A
```

Exécutez à nouveau git status

![Image](https://cdn-media-1.freecodecamp.org/images/7jaUjBjc3Y2870zUbEllhi8rWvQ1Hshgcyqx)
_Figure-22: Ajouter des fichiers à la zone de staging_

Maintenant, nous pouvons voir que simple.py est prêt à être commis.

Ensuite, entrez la commande de commit avec un message

```
git commit -m "Mise à jour de la fonction hello"
```

![Image](https://cdn-media-1.freecodecamp.org/images/XU3eet4u0GXZ7QHQNz98n2nN5fEVlswPV1s2)
_Figure-23: Message de commit_

Maintenant, nous devons pousser les modifications commises vers le dépôt distant afin que les autres personnes y aient accès.

Étant donné que le cas courant est que plusieurs développeurs travaillent sur un seul projet, nous devons d'abord récupérer toutes les modifications qui ont été faites dans le dépôt distant avant de pousser nos modifications pour éviter les conflits.

Exécutez la commande suivante :

```
git pull origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/5TkIfVHFN2pS9akhGmgjHVxHRoR6SrgwJEYc)
_Figure-24: Récupérer les modifications du dépôt distant_

Puisque nous sommes déjà à jour, nous pouvons maintenant pousser nos modifications vers le dépôt distant.

Maintenant, exécutez ce qui suit :

```
git push origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/t7wVKea6PcQGihQzTeoz3WdS66L8IGjPdpqE)
_Figure-25: Pousser les modifications vers le dépôt distant_

Nous avons réussi à pousser nos modifications vers la branche master du dépôt distant !

### Créer une branche pour une fonctionnalité ou un problème

Jusqu'à présent, nous avons travaillé sur notre branche master, mais ce n'est pas ainsi que vous devriez travailler dans git en tant que développeur, car la branche master devrait être une version stable du projet sur lequel vous travaillez. Donc, pour chaque fonctionnalité ou problème, il est généralement normal de créer votre propre branche et de travailler à partir de cette branche.

La commande pour créer une nouvelle branche appelée simple-greeting est la suivante :

```
git branch simple-greeting
```

Maintenant, si vous exécutez

```
git branch
```

alors vous verrez toutes les branches dans le dépôt, et la branche actuelle dans laquelle vous vous trouvez est mise en évidence avec un astérisque sur le côté gauche.

![Image](https://cdn-media-1.freecodecamp.org/images/XlYSPXjn7qFPNQiLTIywhgNdYKjxD9MFzip4)
_Figure-26: git branch_

Si vous voulez passer à la branche que vous venez de créer, tapez ce qui suit :

```
git checkout simple-greeting
```

Maintenant, si vous tapez git branch, vous verrez que vous êtes maintenant sur la branche simple-greeting.

Maintenant, nous devons apporter les modifications dans le projet. Nous allons passer au projet et définir la fonction de salutation.

![Image](https://cdn-media-1.freecodecamp.org/images/VLWULRA1hRT85jSYBs1d4JH90JBUQP2kDrrc)
_Figure-27: Définir la fonction de salutation_

Maintenant, nous allons répéter le processus de commit de ces modifications :

```
git status
```

![Image](https://cdn-media-1.freecodecamp.org/images/lFNjI8aQZ7CZFUUnNMieYovVJ218kg9MO3Lf)
_Figure-28: Voir les modifications qui ne sont pas en staging_

```
git add -A
```

```
git commit -m "Fonction de salutation"
```

![Image](https://cdn-media-1.freecodecamp.org/images/vsigz7NjuUVcgaaPetiERCN1La5W8F5BoOFd)
_Figure-29: Message de commit pour la fonction de salutation_

Ce commit ne modifiera que les fichiers dans la branche locale simple-greeting et n'aura eu aucun effet sur la branche master locale ou le dépôt distant pour l'instant.

### Pousser la branche vers le dépôt distant après le commit

Entrez la commande suivante :

```
git push -u origin simple-greeting
```

où origin est le nom du dépôt et simple-greeting est la branche que nous voulons pousser.

![Image](https://cdn-media-1.freecodecamp.org/images/M3mB0GiO80v-Jk56yKQKuIgnUVaXQvDfGnM-)
_Figure-30: Pousser la branche vers le dépôt distant_

Maintenant, nous avons poussé la branche simple-greeting vers le dépôt distant. Si vous tapez :

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/GrUXJqmZJmFgb3jHf8B3PlxT7yxVwOCncuIB)
_Figure-31: Branche simple-greeting dans le dépôt distant_

Nous pouvons voir que, dans notre dépôt distant, nous avons maintenant la branche simple-greeting. Pourquoi devons-nous pousser la branche vers le dépôt distant ? Parce que dans certaines entreprises, c'est là qu'ils exécutent leurs tests unitaires et divers autres tests pour s'assurer que le code fonctionne bien avant qu'il ne soit fusionné avec la branche master.

Étant donné que tous les tests se sont bien passés (nous n'entrerons pas dans les détails ici), nous pouvons maintenant fusionner la branche simple-greeting avec la branche master.

### Fusionner une branche

Tout d'abord, nous devons nous placer dans la branche master locale

```
git checkout master
```

![Image](https://cdn-media-1.freecodecamp.org/images/OvI0f0CpYa3xrFvKv-HQ5LB20HxbgOEHxT9I)
_Figure-32: Se placer dans la branche master_

Récupérez toutes les modifications dans la branche master distante :

```
git pull origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/S1bz0eJjDY1avLSy4Gl7Et33gwDw2uGVeih3)
_Figure-33: Récupérer les modifications du dépôt distant_

Nous allons maintenant voir les branches que nous avons fusionnées jusqu'à présent :

```
git branch --merged
```

![Image](https://cdn-media-1.freecodecamp.org/images/v9PBL7dVbIsb3aIz61PRypR6qorrAcw6nahW)
_Figure-34: Afficher les branches fusionnées_

La branche simple-greeting n'apparaîtra pas ici car nous ne l'avons pas encore fusionnée.

Pour fusionner simple-greeting avec master, entrez :

```
git merge simple-greeting
```

(Notez que nous sommes dans la branche master en ce moment)

![Image](https://cdn-media-1.freecodecamp.org/images/4G84bB5YgbwdfH8XkDHUxUZwGfi8mMw0ZHKa)
_Figure-35: Fusionner la branche simple-greeting_

Maintenant qu'elle a été fusionnée, nous pouvons pousser les modifications vers la branche master du dépôt distant.

```
git push origin master
```

![Image](https://cdn-media-1.freecodecamp.org/images/bQjuJUw584OprdvxUzmNs1yxOh8Ijd3WLQwK)
_Figure-36: Pousser vers la branche master distante_

Maintenant, les modifications ont été poussées vers la branche master dans le dépôt distant.

### Supprimer une branche

Puisque la fonctionnalité a maintenant été déployée, nous pouvons supprimer la branche simple-greeting. Pour vérifier la fusion effectuée dans la section précédente, nous pouvons exécuter :

```
git branch --merged
```

![Image](https://cdn-media-1.freecodecamp.org/images/C-XMNUIumKsfPaPVDD5BFyvDBzo8rrJCTTEl)
_Figure-37: Afficher les branches fusionnées_

Si simple-greeting apparaît ici, cela signifie que nous avons fusionné toutes les modifications et que la branche peut maintenant être supprimée.

```
git branch -d simple-greeting
```

![Image](https://cdn-media-1.freecodecamp.org/images/hd10e8Mc246riKYeTEvv0hL1xz7k7b7njSHf)
_Figure-38: Supprimer la branche locale simple-greeting_

Maintenant, la branche a été supprimée localement.

Mais puisque nous avons poussé la branche vers le dépôt distant, elle y est toujours dans le dépôt distant. Cela peut être vu en exécutant :

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/gHdlHkbjv1QhmID0PkoWM35qMagnJ9B-qIkx)
_Figure-39: Afficher toutes les branches_

Pour supprimer la branche du dépôt distant, entrez :

```
git push origin --delete simple-greeting
```

![Image](https://cdn-media-1.freecodecamp.org/images/5-equM6f4mL9prXhxNiet0JC4lqhn4uzn84v)
_Figure-40: Supprimer la branche distante simple-greeting_

Si nous réexécutons

```
git branch -a
```

![Image](https://cdn-media-1.freecodecamp.org/images/33hTj4HTBLKO5Eg345weOEBa4yNE2uXglp5Z)
_Figure-41: Afficher toutes les branches_

nous pouvons voir que la branche a maintenant été supprimée du dépôt distant également.

Félicitations !!! Vous êtes maintenant un expert des commandes Git de base mais critiques !

Pour référence ou utilisation de ce tutoriel, voici le dépôt public GitHub [Lien](https://github.com/sanjulamadurapperuma/GitDemoMedium)

**En attendant, donnez autant d'applaudissements que vous le souhaitez à cet article si vous l'avez aimé, commentez ci-dessous pour toute préoccupation. Consultez également mon profil sur [LinkedIn](https://www.linkedin.com/in/sanjula-madurapperuma/) et suivez-moi sur Twitter !**