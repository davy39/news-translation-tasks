---
title: Comment Git fonctionne sous le capot
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-04T16:34:00.000Z'
originalURL: https://freecodecamp.org/news/git-under-the-hood
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Git-under-the-hood.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment Git fonctionne sous le capot
seo_desc: "By Faisal Albasu\nAs developers, we all use some form of version control\
  \ system, and the most popular one is Git. \nA lot of us use Git, but very few know\
  \ how it really works under the hood. We mostly just use it with a GUI client or\
  \ the ones built int..."
---

Par Faisal Albasu

En tant que développeurs, nous utilisons tous une forme de système de contrôle de version, et le plus populaire est Git. 

Beaucoup d'entre nous utilisent Git, mais très peu savent comment il fonctionne vraiment sous le capot. Nous l'utilisons principalement avec un client GUI ou ceux intégrés dans nos IDE et éditeurs de code. Certains d'entre nous (moi y compris) ne savent même pas comment le naviguer en utilisant le terminal. 

Cela peut être préjudiciable à vos projets, car vous pourriez rencontrer des problèmes que vous ne saurez pas résoudre sans comprendre pleinement comment Git fonctionne en arrière-plan.

Dans cet article, je vais partager un peu de ce qui se passe derrière les scènes avec Git et ce que vous devez savoir lorsque vous travaillez avec lui. 

Cet article a été inspiré par un cours que j'ai suivi appelé Collaborative Coding with Git qui vous apprend à utiliser Git pour collaborer avec des partenaires et des membres d'équipe sur des projets. 

Très bien, commençons.

Note : Cet article n'est pas un guide détaillé pour travailler avec Git. Il est plutôt destiné à vous donner un aperçu de ce qui se passe derrière les scènes lorsque vous travaillez avec Git.

Si vous voulez une introduction de base à Git et GitHub, [voici un bon guide pour débutants](https://www.freecodecamp.org/news/git-and-github-for-beginners/).

## Qu'est-ce que Git et comment fonctionne-t-il ?

Git est un système de contrôle de version distribué qui aide les développeurs à suivre les changements dans leurs projets. Pensez-y comme à une chronologie complète de votre projet, du début à la fin.

Lorsque vous créez un nouveau projet et initialisez un dépôt Git en utilisant `git init`, il crée un dossier caché appelé `.git` qui contient un ensemble d'autres fichiers et dossiers. Ces fichiers et dossiers contiennent tout le contenu nécessaire pour que Git référence ce répertoire particulier.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-10.45.26-AM.png)
_Le dossier .git_

Après avoir initialisé le dépôt, Git commence à suivre tous les fichiers et dossiers à l'intérieur de ce répertoire, sauf ceux que vous lui dites explicitement de ne pas suivre dans le fichier `.gitignore`. Le fichier `.gitignore` est un fichier caché qui vous permet de lister tous les fichiers et dossiers que vous ne voulez pas que Git suive. Ces fichiers et dossiers ne seront jamais référencés par Git dans votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-11.24.05-AM.png)
_Le fichier .gitignore_

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-11.30.06-AM.png)
_À l'intérieur du fichier .gitignore_

Lorsque vous travaillez avec git, vos fichiers sont enregistrés dans l'un des 3 états de Git :

* L'état modifié – C'est lorsque vous ajoutez, supprimez ou changez quelque chose dans un fichier. Git a remarqué le changement mais vous n'avez pas encore formellement informé Git du changement.
* L'état indexé – C'est lorsque vous informez Git du changement et dites à Git de prendre note de ce changement. Communément appelé la "zone de transit", les fichiers dans cette étape sont appelés les fichiers indexés. Vous pouvez modifier un fichier même après l'avoir indexé, ce qui vous permet de voir le fichier à la fois dans un état modifié et un état indexé. Les modifications apportées après l'indexation n'apparaîtront pas après qu'un commit ait été fait.
* L'état validé – C'est lorsque Git a enregistré vos modifications.

Vous pouvez utiliser la commande `git status` pour voir dans quels états se trouvent actuellement vos fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-11.32.24-AM.png)

Lorsque vous validez du code, Git prend un instantané de cette version particulière de votre code que vous pouvez référencer à une date ultérieure.

Vous pourriez donc dire que Git est une base de données de références à votre projet. Cette base de données est construite en utilisant trois types d'objets : 

* les commits qui contiennent les métadonnées de chaque commit telles que le message et l'auteur,
* l'arborescence des changements qui contiennent des références aux noms de fichiers, aux contenus de fichiers, et parfois à d'autres arborescences, 
* et le blob qui représente les données réelles contenues dans les fichiers.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-10.48.27-AM.png)
_Contenu à l'intérieur du dossier .git_

Note : Le dossier .git est parfois caché dans macOS, vous devrez donc activer les fichiers cachés dans vos paramètres système pour le voir.

### Comment Git suit vos fichiers

Lorsque vous travaillez avec Git, il y a beaucoup de parties mobiles et parfois nous travaillons avec plusieurs fichiers différents. 

Pour que Git puisse suivre tous ces fichiers, il crée quelque chose appelé l'Algorithme de Hachage Sécurisé (SHA), qui est une série de fonctions de hachage cryptographique, et l'assigne à chaque commit. Cela facilite l'identification des doublons et leur donne le même identifiant que le fichier original, économisant ainsi de l'espace de stockage. 

En utilisant le SHA, nous pouvons référencer n'importe quoi dans Git, comme regarder un commit et revenir à celui-ci, ou simplement le tagger.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-10-25-at-10.52.26-AM--1-.png)
_Un graphique terminal d'un arbre Git_

Chaque commit, sauf le commit initial, a un commit parent, et lorsque vous commencez un projet, votre HEAD est pointé vers le dernier commit sur la branche master ou main. 

Tout cela est maintenu en utilisant les numéros SHA assignés aux commits. Lorsque vous créez une branche, elle crée une copie séparée des fichiers. Lorsque vous changez de branche, le HEAD change son point vers le dernier commit sur la branche à laquelle vous avez basculé.

Les branches supprimées sont dites être dans un état HEAD détaché ou sans tête. Nous pouvons y accéder si nous avons le hachage unique, mais il n'y a pas de HEAD pointant vers elles – donc si nous n'avons pas leur hachage, il n'y a aucun moyen d'y accéder. 

Nous pouvons également garder l'accès à celles-ci en les vérifiant en tant que branches individuelles.

Lorsque vous travaillez avec Git, vous créez souvent des branches séparées pour des tâches séparées, comme travailler sur de nouvelles fonctionnalités ou des corrections de bugs. Vous créez des branches en utilisant la commande `git branch`.

```bash
git branch [nom de la branche]

```

Lorsque nous passons d'une branche à une autre, Git n'a plus accès à aucun des commits dans la branche précédente. Donc si nous voulons revenir à un commit dans une autre branche, nous devons basculer vers cette branche ou rebaser notre branche actuelle sur l'autre branche que nous aimerions utiliser. 

Je vais parler du rebasage dans un instant, mais d'abord, je veux parler un peu de la fusion et des conflits de fusion.

### Qu'est-ce que la fusion Git et comment fonctionne-t-elle ?

Lorsque vous créez une branche pour quelque chose sur lequel vous travaillez dans votre projet, vous ne voulez généralement pas que le reste de votre travail soit affecté si vous faites une erreur. Donc, lorsque vous terminez cette tâche, vous voudrez l'ajouter à votre projet principal. 

La méthode la plus courante pour faire cela est de **fusionner** la branche dans la branche principale ou master du projet. 

Il existe 3 types de fusion : la fusion rapide, la fusion à trois voies et le rebasage que j'ai brièvement mentionné ci-dessus.

La fusion rapide, comme son nom l'indique, est un moyen rapide et facile de fusionner vos branches et de continuer à travailler sur votre projet. Elle ne nécessite pas de travail supplémentaire et vous rencontrerez rarement un conflit de fusion avec elle. 

C'est parce que tout ce qu'elle fait est de déplacer son HEAD du commit actuel de la branche principale vers le dernier commit de la branche en cours de fusion. C'est comme faire avancer votre projet dans le temps.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Fast-Forward-Merge-1.png)
_Fusion rapide_

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.22.33-PM.png)
_Fusion rapide en action_

La fusion à trois voies, en revanche, nécessite un peu plus de travail car vous traitez avec trois commits. 

Une fusion à trois voies se produit lorsque la branche que vous essayez de fusionner est en avance sur la branche que vous essayez de fusionner. Par exemple, vous créez une branche pour corriger un bug et en même temps, un collègue travaille sur la branche principale. Et avant que vous ne puissiez terminer l'écrasement du bug, un nouveau commit a été ajouté à la branche principale. 

Git ne pourra pas intégrer en douceur votre branche dans la branche principale car la branche principale est maintenant en avance sur le commit auquel votre branche pointait. 

Il doit donc créer un commit séparé pour celui-ci et combiner votre commit, le nouveau commit sur la branche principale et le commit auquel ils pointent tous les deux (puisqu'ils ont tous les deux le même commit ancêtre) en un seul commit afin de les fusionner en tant que nouveau commit.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Three-way-Merge-2.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.30.39-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.28.56-PM.png)
_Invite pour créer un troisième commit pour la fusion à 3 voies_

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.35.02-PM.png)
_Fusion à 3 voies réussie_

La dernière méthode, qui est le rebasage, transfère toute la branche de fonctionnalité sur la branche principale. 

Un inconvénient du rebasage que la fusion n'a pas est la perte de l'historique du projet. Lorsque vous fusionnez une branche avec une autre branche, vous avez toujours accès à cette branche jusqu'à ce que vous la supprimiez. Mais lorsque vous rebasez une branche, vous perdez l'accès à tout l'historique de cette branche. Cela peut être bon ou mauvais selon vous, (votre équipe), et votre projet.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Rebasing.png)
_Concept de rebasage_

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.59.33-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-12.56.23-PM.png)
_Invite pour choisir un commit à utiliser pour le rebasage_

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-10-25-at-12.57.56-PM.png)
_Feature-branch-3 rebasée_

Avec toutes les fusions et rebasages qui se produisent dans votre projet, vous êtes sûr de rencontrer des conflits de fusion. 

Les conflits de fusion se produisent lorsque vous apportez des modifications à la même position d'un fichier sur différentes branches. Par exemple, vous avez apporté une modification à la ligne 10 d'une branche de fonctionnalité sur laquelle vous travaillez et une autre personne a également apporté une modification à cette même ligne sur la branche principale. 

À ce stade, Git ne saura pas quelle modification choisir, il lancera donc un conflit de fusion et refusera de fusionner ou de rebaser jusqu'à ce que vous résolviez manuellement le conflit.

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-1.15.50-PM.png)

Lorsque qu'un conflit de fusion se produit, Git pause la fusion et attend que vous résolviez les conflits et continuiez la fusion. Vous pouvez exécuter une commande `git status` pour voir quels fichiers sont fusionnés et lesquels ne le sont pas. 

Vous pouvez résoudre les conflits en utilisant les marqueurs de résolution de conflit de Git qui ressemblent à ceci lorsque vous ouvrez les fichiers où se trouve le conflit :

![Image](https://www.freecodecamp.org/news/content/images/2021/10/Screen-Shot-2021-10-25-at-1.20.45-PM.png)

La version au-dessus de `===` est votre version actuelle vérifiée, c'est pourquoi elle a le HEAD pointant vers elle. La version en dessous est la branche que vous essayez de fusionner. 

Pour résoudre le conflit, vous devez décider quelle version vous voulez garder et laquelle vous voulez supprimer, ou vous devez fusionner le contenu manuellement par vous-même. Après avoir choisi, vous pouvez alors continuer votre fusion.

## Comment sauvegarder les modifications non validées dans Git

Plus tôt, j'ai parlé des 3 états de Git, qui sont modifié, indexé et validé. 

Il arrive que nous voulions changer rapidement de branche sans sauvegarder les modifications que nous avons apportées à la branche actuelle. Cela peut être pour faire une correction rapide ou simplement vérifier des choses, et nous n'avons pas terminé de travailler sur la branche actuelle. Nous pouvons faire cela avec le **stash**.

### Comment fonctionne le stash dans Git

Le stash vous permet de sauvegarder tout votre travail non validé et de les enregistrer en tant que modifications non terminées que vous pouvez réappliquer plus tard, même si vous êtes sur une branche séparée. 

Pour stasher vos fichiers, vous pouvez utiliser la commande `git stash`. Cela sauvegarde toutes vos modifications non validées dans une pile et vous laisse avec une branche propre. Pour voir votre stash, vous pouvez utiliser la commande `git stash list`. Il ne sauvegarde pas les fichiers non suivis, cependant.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-3.05.18-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-3.06.41-PM.png)
_Liste de stash_

Lorsque vous êtes prêt à appliquer vos modifications stashées, il suffit d'exécuter la commande `git stash apply` et elle appliquera ces modifications. 

Si vous avez plusieurs stashs, vous pouvez spécifier quel stash appliquer en spécifiant le stash que vous souhaitez appliquer (par exemple `stash@{0}`). Si vous ne spécifiez pas le stash que vous souhaitez appliquer, Git applique automatiquement les modifications de stash les plus récentes.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-3.14.28-PM--1-.png)
_Stash appliqué_

## Comment annuler les modifications dans Git

Lorsque vous travaillez sur n'importe quel type de projet, il arrive que nous fassions inévitablement des erreurs, peu importe à quel point nous sommes prudents ou à quel point notre système est efficace. Cela peut être une erreur humaine ou informatique. 

Normalement, lorsque vous travaillez avec des applications conventionnelles et des traitements de texte, vous appuyez simplement sur un bouton d'annulation ou utilisez le raccourci cntrl/cmd + z et vous revenez à l'état précédent. Mais lorsque vous travaillez avec Git, vous n'avez pas ce luxe, vous devez donc passer par quelques étapes supplémentaires pour corriger/annuler ces erreurs. 

Il existe plusieurs méthodes que nous pouvons utiliser pour corriger/annuler ces erreurs, alors examinons-les une par une.

### Checkout

Checkout est principalement utilisé pour changer de branche, mais peut également être utilisé pour pointer votre HEAD vers un commit particulier. Vous pouvez faire cela en spécifiant votre numéro de SHA de commit après la commande checkout.

```
git checkout [SHA du commit]
```

Cela vous place dans un état HEAD détaché où vous pouvez faire des modifications temporaires ou expérimentales sans affecter aucune de vos branches.

Après avoir réussi à vérifier votre commit, vous pouvez ensuite le transformer en une branche séparée.

```
git checkout -b [nom de votre nouvelle branche]
ou
git switch -c [nom de votre nouvelle branche]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-4.38.20-PM.png)
_Annuler les modifications avec 'checkout'_

Gardez à l'esprit, cependant, que l'utilisation de checkout peut entraîner la perte de votre branche précédente en raison de son état HEAD détaché.

### Revert

C'est la méthode la plus directe pour corriger les erreurs dans votre dépôt. Revert, comme son nom l'indique, inverse l'erreur en ajoutant un commit avant le commit qui contient l'erreur – mais sans l'erreur. Pensez-y comme à un retour en arrière et en avant dans le temps simultanément. 

Voici un exemple : vous avez 2 commits, nommés "initial commit" et "setting up dev environment". En travaillant, vous remarquez que vous avez fait une erreur dans le 2ème commit et vous voulez revenir à "initial commit". 

Lorsque vous invoquez le mot-clé `git revert`, il crée un troisième commit qui est exactement le même que de ramener votre dépôt avant que le deuxième commit ne se produise. Avec Git revert, vous devrez passer une référence de commit et, similaire à une fusion à trois voies, vous devez passer un message de commit pour le nouveau commit créé.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.30.46-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.33.38-PM.png)

### Reset

C'est la méthode la plus complexe, polyvalente et la plus dangereuse pour annuler les modifications dans Git. Il est souvent déconseillé d'utiliser reset dans un dépôt partagé car cela peut entraîner des pertes importantes dans le projet. Bon, cela étant dit, voyons ce que fait reset et en quoi il est différent des autres méthodes.

Git reset a trois options. Selon celle que vous utilisez, elle peut altérer l'historique des commits, l'historique des commits et l'index de staging, ou l'historique des commits, l'index de staging et le répertoire de travail.

La première, qui est `git reset --soft`, altère uniquement l'historique des commits. Avec cela, vous devrez spécifier à quel commit vous souhaitez revenir en utilisant son ID.

```
git reset --soft [ID du commit]
```

Cela supprime tous les commits qui sont arrivés après le commit auquel vous revenez.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.46.23-PM--1-.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.44.23-PM.png)

La deuxième, `git reset --mixed`, est le comportement par défaut de l'invocation `git reset`. Elle altère à la fois l'historique des commits et l'index de staging. Donc si vous avez des fichiers dans la zone de staging, elle désindexe ces fichiers et si un ID de commit est spécifié, elle revient à ce commit, supprimant tous les commits qui sont arrivés après.

```
//Les deux font la même chose
git reset [ID du commit]
git reset --mixed [ID du commit]
```

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.51.16-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.56.38-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.58.53-PM--1-.png)

La dernière, qui est la plus dangereuse et ne doit être utilisée qu'en dernier recours, est l'option `git reset --hard`. Cela altère l'historique des commits, l'index de staging et le répertoire de travail. 

Donc, il revient d'abord au commit spécifié par l'ID de commit, désindexe tous les fichiers indexés et supprime toutes les modifications effectuées dans le répertoire de travail. Cela signifie que si vous avez modifié des fichiers ou ajouté plus de fichiers, il supprime toutes ces modifications et ajouts du répertoire de travail. 

Vous pouvez voir pourquoi il n'est pas conseillé d'utiliser cette commande sauf lorsque vous n'avez pas d'autre choix.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-6.08.03-PM.png)

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-6.08.37-PM.png)

La méthode la plus sûre pour corriger ou annuler une erreur est d'utiliser la commande `git revert`. Cela est dû au fait qu'elle ne modifie pas votre historique de commits mais crée un nouveau commit avant celui avec l'erreur. De cette façon, vous pouvez toujours revenir au commit avec l'erreur si nécessaire.

## Conclusion

J'espère que cet article vous donne un aperçu clair de ce qui se passe sous le capot lorsque vous travaillez avec Git. Et j'espère que vous êtes maintenant familier avec les parties les plus cruciales de Git que vous devez connaître lorsque vous travaillez avec lui.

Si vous voulez approfondir le travail avec Git, j'ai un [article](https://blog.albasfaisal.com/top-5-resources-for-learning-git) dans mon blog avec certaines des meilleures ressources pour apprendre Git.

Si vous avez atteint ce point, merci d'avoir lu, je suis [Faisal](https://www.freecodecamp.org/news/p/e2f11707-3a1c-4a8e-9520-8c443204353b/links.albasfaisal.com). Vous pouvez me retrouver sur Twitter, Instagram et YouTube. N'hésitez pas à vous connecter sur l'une de ces plateformes.