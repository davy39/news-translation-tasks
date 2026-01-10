---
title: 10 commandes Git que tout développeur devrait connaître
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-19T23:07:10.000Z'
originalURL: https://freecodecamp.org/news/10-important-git-commands-that-every-developer-should-know
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/Ekran-Resmi-2020-01-12-21.59.37.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: version control
  slug: version-control
seo_title: 10 commandes Git que tout développeur devrait connaître
seo_desc: 'By Cem Eygi

  Git is an important part of daily programming (especially if you''re working with
  a team) and is widely used in the software industry.

  Since there are many various commands you can use, mastering Git takes time. But
  some commands are used ...'
---

Par Cem Eygi

Git est une partie importante de la programmation quotidienne (surtout si vous travaillez en équipe) et est largement utilisé dans l'industrie du logiciel.

Puisqu'il existe de nombreuses commandes variées que vous pouvez utiliser, la maîtrise de Git prend du temps. Mais certaines commandes sont utilisées plus fréquemment (certaines quotidiennement). Donc dans cet article, je vais partager et expliquer les 10 commandes Git les plus utilisées que tout développeur devrait connaître.

**Note : Pour comprendre cet article, vous devez connaître les bases de Git.**

## 1. Git clone

Git clone est une commande pour télécharger le code source existant depuis un dépôt distant (comme Github, par exemple). En d'autres termes, Git clone crée essentiellement une copie identique de la dernière version d'un projet dans un dépôt et l'enregistre sur votre ordinateur.

Il existe plusieurs façons de télécharger le code source, mais je préfère surtout la méthode **clone avec https** :

```
git clone <https://nom-du-lien-du-depot>
```

Par exemple, si nous voulons télécharger un projet depuis Github, tout ce que nous avons à faire est de cliquer sur le bouton vert (clone ou download), copier l'URL dans la boîte et la coller après la commande git clone que j'ai montrée juste au-dessus.

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim-4.png)
_**Exemple de code source Bootstrap depuis Github**_

Cela créera une copie du projet dans votre espace de travail local afin que vous puissiez commencer à travailler avec.

## 2. Git branch

Les branches sont très importantes dans le monde de git. En utilisant des branches, plusieurs développeurs peuvent travailler en parallèle sur le même projet simultanément. Nous pouvons utiliser la commande git branch pour créer, lister et supprimer des branches.

**Créer une nouvelle branche :**

```
git branch <nom-de-la-branche>
```

Cette commande créera une branche **localement**. Pour pousser la nouvelle branche dans le dépôt distant, vous devez utiliser la commande suivante :

```
git push -u <remote> <nom-de-la-branche>
```

**Voir les branches :**

```
git branch ou git branch --list
```

**Supprimer une branche :**

```
git branch -d <nom-de-la-branche>
```

## 3. Git checkout

Ceci est également l'une des commandes Git les plus utilisées. Pour travailler dans une branche, vous devez d'abord basculer vers celle-ci. Nous utilisons **git checkout** principalement pour passer d'une branche à une autre. Nous pouvons également l'utiliser pour extraire des fichiers et des commits.

```
git checkout <nom-de-votre-branche>
```

Il y a quelques étapes que vous devez suivre pour basculer avec succès entre les branches :

* Les changements dans votre branche actuelle doivent être validés ou mis de côté avant de basculer
* La branche que vous souhaitez extraire doit exister dans votre local

**Il existe également une commande raccourcie qui vous permet de créer et de basculer vers une branche en même temps :**

```
git checkout -b <nom-de-votre-branche>
```

Cette commande crée une nouvelle branche dans votre local (-b signifie branche) et bascule vers la nouvelle branche juste après sa création.

## 4. Git status

La commande Git status nous donne toutes les informations nécessaires sur la branche actuelle.

```
git status
```

Nous pouvons recueillir des informations comme :

* Si la branche actuelle est à jour
* S'il y a quelque chose à valider, pousser ou tirer
* S'il y a des fichiers indexés, non indexés ou non suivis
* S'il y a des fichiers créés, modifiés ou supprimés

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim-5.png)
_**Git status donne des informations sur la branche et les fichiers**_

## 5. Git add

Lorsque nous créons, modifions ou supprimons un fichier, ces changements se produisent dans notre local et ne seront pas inclus dans le prochain commit (sauf si nous changeons les configurations).

Nous devons utiliser la commande git add pour inclure les changements d'un ou plusieurs fichiers dans notre prochain commit.

**Pour ajouter un seul fichier :**

```
git add <fichier>
```

**Pour tout ajouter à la fois :**

```
git add -A
```

Lorsque vous visitez la capture d'écran ci-dessus dans la 4ème section, vous verrez qu'il y a des noms de fichiers qui sont en rouge - cela signifie qu'ils sont des fichiers non indexés. Les fichiers non indexés ne seront pas inclus dans vos commits.

**Pour les inclure, nous devons utiliser git add :**

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim-6.png)
_**Les fichiers en vert sont maintenant indexés avec git add**_

**Important : La commande git add ne change pas le dépôt et les changements ne sont pas enregistrés tant que nous n'utilisons pas git commit.**

## 6. Git commit

Ceci est peut-être la commande la plus utilisée de Git. Une fois que nous atteignons un certain point dans le développement, nous voulons enregistrer nos changements (peut-être après une tâche ou un problème spécifique).

Git commit est comme un point de contrôle dans le processus de développement auquel vous pouvez revenir plus tard si nécessaire.

Nous devons également écrire un court message pour expliquer ce que nous avons développé ou changé dans le code source.

```
git commit -m "message de commit"
```

**Important : Git commit enregistre vos changements uniquement localement.**

## 7. Git push

Après avoir validé vos changements, la prochaine chose que vous voulez faire est d'envoyer vos changements au serveur distant. Git push télécharge vos commits vers le dépôt distant.

```
git push <remote> <nom-de-la-branche>
```

Cependant, si votre branche est nouvellement créée, vous devez également télécharger la branche avec la commande suivante :

```
git push --set-upstream <remote> <nom-de-votre-branche>
```

ou

```
git push -u origin <nom_de_la_branche>
```

**Important : Git push ne télécharge que les changements qui sont validés.**

## 8. Git pull

La commande **git pull** est utilisée pour obtenir les mises à jour du dépôt distant. Cette commande est une combinaison de **git fetch** et **git merge**, ce qui signifie que, lorsque nous utilisons git pull, elle obtient les mises à jour du dépôt distant (git fetch) et applique immédiatement les derniers changements dans votre local (git merge).

```
git pull <remote>
```

**Cette opération peut causer des conflits que vous devez résoudre manuellement.**

## 9. Git revert

Parfois, nous devons annuler les changements que nous avons faits. Il existe diverses façons d'annuler nos changements localement ou à distance (selon ce dont nous avons besoin), mais nous devons utiliser ces commandes avec prudence pour éviter les suppressions indésirables.

Une manière plus sûre d'annuler nos commits est d'utiliser **git revert**. Pour voir notre historique de commits, nous devons d'abord utiliser **git log --oneline** :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim.png)
_**historique des commits de ma branche master**_

Ensuite, nous devons simplement spécifier le code de hachage à côté de notre commit que nous souhaitons annuler :

```
git revert 3321844
```

Après cela, vous verrez un écran comme ci-dessous - appuyez simplement sur **shift + q** pour quitter :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim-2.png)

La commande Git revert annulera le commit donné, mais créera un nouveau commit sans supprimer l'ancien :

![Image](https://www.freecodecamp.org/news/content/images/2020/01/resim-3.png)
_**nouveau commit "revert"**_

L'avantage d'utiliser **git revert** est qu'il ne touche pas à l'historique des commits. Cela signifie que vous pouvez toujours voir tous les commits dans votre historique, même ceux qui ont été annulés.

Une autre mesure de sécurité ici est que tout se passe dans notre système local à moins que nous les poussions vers le dépôt distant. C'est pourquoi git revert est plus sûr à utiliser et est la manière préférée pour annuler nos commits.

## 10. Git merge

Lorsque vous avez terminé le développement dans votre branche et que tout fonctionne bien, l'étape finale est la fusion de la branche avec la branche parente (dev ou master). Cela se fait avec la commande `git merge`.

Git merge intègre essentiellement votre branche de fonctionnalité avec tous ses commits dans la branche dev (ou master). Il est important de se rappeler que vous devez d'abord être sur la branche spécifique avec laquelle vous souhaitez fusionner votre branche de fonctionnalité.

Par exemple, lorsque vous voulez fusionner votre branche de fonctionnalité dans la branche dev :

**D'abord, vous devez basculer vers la branche dev :**

```
git checkout dev
```

**Avant de fusionner, vous devez mettre à jour votre branche dev locale :**

```
git fetch
```

**Enfin, vous pouvez fusionner votre branche de fonctionnalité dans dev :**

```
git merge <nom-de-la-branche>
```

**Astuce : Assurez-vous que votre branche dev a la dernière version avant de fusionner vos branches, sinon vous pourriez rencontrer des conflits ou d'autres problèmes indésirables.**

Donc, ce sont mes 10 commandes git les plus utilisées que je rencontre dans ma programmation quotidienne. Il y a beaucoup plus de choses à apprendre sur Git et je les expliquerai plus tard dans des articles séparés.

**Si vous voulez en savoir plus sur le développement web, n'hésitez pas à** [**me suivre sur Youtube**](https://www.youtube.com/channel/UC1EgYPCvKCXFn8HlpoJwY3Q)** !**

Merci d'avoir lu !