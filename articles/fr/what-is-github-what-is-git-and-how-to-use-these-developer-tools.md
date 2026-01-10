---
title: Qu'est-ce que GitHub ? Qu'est-ce que Git ? Et comment utiliser ces outils de
  développement.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-05T14:05:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-github-what-is-git-and-how-to-use-these-developer-tools
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/ambers-article.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: Qu'est-ce que GitHub ? Qu'est-ce que Git ? Et comment utiliser ces outils
  de développement.
seo_desc: "By Amber Wilkie\nThe first programs you write will probably not be very\
  \ impressive. You'll make lots of mistakes and you'll never want to revisit the\
  \ past. \nBut soon enough, you'll be writing large, complex programs. Maybe you'll\
  \ delete some stuff now..."
---

Par Amber Wilkie

Les premiers programmes que vous écrirez ne seront probablement pas très impressionnants. Vous ferez beaucoup d'erreurs et vous ne voudrez jamais revenir sur le passé. 

Mais assez tôt, vous écrirez des programmes complexes et volumineux. Peut-être supprimerez-vous des éléments que vous voudrez récupérer plus tard. Ou peut-être ferez-vous appel à un ami pour vous aider, et vous voudrez ajouter ses modifications à votre programme tout en continuant à travailler sur vos propres parties. 

C'est là qu'intervient la **gestion de version** (version control), et c'est une compétence que tout employeur s'attendra à ce que vous maîtrisiez. C'est également extrêmement utile pour toute personne travaillant sur des éléments sauvegardés par morceaux — d'un programme informatique à une recette de cuisine, en passant par un roman.

## Qu'est-ce que la gestion de version ?

La gestion de version fait référence à la capacité de sauvegarder votre progression dans un document ou un dossier et de pouvoir consulter les sauvegardes précédentes. 

Pendant que j'écris cet article, mes modifications les plus récentes écrasent constamment mes versions précédentes. Ce n'est pas de la gestion de version, car je ne peux pas revenir au brouillon que j'avais il y a une semaine. Mais si j'écrivais cela en utilisant Git, ce serait possible.

## Qu'est-ce que Git ?

Git est un système de gestion de version développé par Linus Torvalds en 2005 (le créateur de Linux). Git aide les développeurs à suivre l'état de leur code et permet la collaboration sur une base de code. Nous passerons en revue les principaux composants un peu plus tard.

Si vous souhaitez suivre, vous devrez avoir Git installé sur votre ordinateur. Ouvrez un terminal et tapez `git`. Si vous voyez une liste de commandes possibles, vous êtes prêt ! 

De nombreux ordinateurs sont livrés avec Git déjà installé. Si vous devez l'installer, vous pouvez suivre les [instructions ici](https://www.linode.com/docs/development/version-control/how-to-install-git-on-linux-mac-and-windows/) pour votre ordinateur.

## Utiliser Git

Si vous avez déjà utilisé un programme informatique ou un jeu vidéo et remarqué que vous pouvez revenir à une version précédemment enregistrée, vous comprenez intrinsèquement le besoin de Git. Il s'agit simplement d'enregistrer un instantané (snapshot) de votre programme à un moment donné. 

Mais au lieu de devoir suivre chaque ligne de code de votre programme, il note plutôt les changements entre le code que vous avez maintenant et la dernière fois que vous avez sauvegardé. Il tient une note continue du moment où chaque ligne de code a été sauvegardée pour la dernière fois et les stocke dans un dossier caché spécial. 

Considérons ce programme JavaScript. Il affiche trois lignes dans la console (une sortie que vous pouvez voir dans votre navigateur ou votre terminal) :

```
console.log('Bonjour, ceci est un exemple git !')
console.log('Et en voici un autre !')
console.log('Et même un troisième')
```

### git init

Si je veux sauvegarder des versions de mon travail, je peux utiliser Git. Tout d'abord, je vais taper `git init` dans mon terminal pour pouvoir commencer à utiliser Git. Cela créera un dossier `.git`, où Git stockera ses fichiers. 

### git add

`git add .` ajoutera tous les fichiers de notre programme. Si vous avez fait `git init` après avoir créé un fichier, ou chaque fois que vous créez de nouveaux fichiers, vous devrez dire à Git de commencer à suivre leurs modifications avec cette commande.

### git commit

Ensuite, je vais taper `git commit -am "Initial commit"`. `git commit` est la commande pour sauvegarder une version de notre code. Le `-am` est ce qu'on appelle un "flag" et signale qu'il y a des actions optionnelles que nous aimerions entreprendre avec ce commit. Le flag `a` signifie que nous allons sauvegarder tous (All) nos changements. Le flag `m` indique que nous fournirons un message (Message) par la suite, qui est `"Initial commit"`. 

Vous pouvez écrire ce que vous voulez ici — freeCodeCamp propose de nombreux articles sur [comment écrire de bons messages de commit](https://www.freecodecamp.org/news/writing-good-commit-messages-a-practical-guide/).

## Comment Git enregistre les modifications

Si nous apportons une modification à notre programme (comme changer le texte de la première ligne), nous pouvons vouloir sauvegarder une version. Nous pourrions même basculer entre les versions si nous voulions voir comment notre programme a évolué au fil du temps.

```
console.log('Maintenant, j\'ai modifié la première ligne.')
console.log('Et en voici un autre !')
console.log('Et même un troisième')
```

### git diff

Voici à quoi cela ressemble lorsque vous lancez `git diff`. Git vous montrera la _différence_ entre le code que vous avez maintenant et la dernière fois qu'il a été sauvegardé. 

C'est un peu difficile de comprendre ce qui se passe ici, mais les `-` sont des suppressions et les `+` sont des insertions. Nous avons supprimé le texte "Bonjour, ceci est un exemple git !" et ajouté le texte "Maintenant, j'ai modifié la première ligne.". C'est ainsi que Git assure le suivi de ce qui a changé entre les versions.

```bash
diff --git a/git.js b/git.js
index eb0f1d1..8dbf769 100644
--- a/git.js
+++ b/git.js
@@ -1,3 +1,3 @@
+console.log('Maintenant, j\'ai modifié la première ligne.')
-console.log('Bonjour, ceci est un exemple git !')
 console.log('Et en voici un autre !')
 console.log('Et même un troisième')
```

Maintenant que nous avons examiné les changements que nous commitons, nous pouvons procéder à un deuxième commit : `git commit -am 'Mise à jour du premier console log'`. Cela sauvegardera les modifications que j'ai apportées à la première ligne de texte.

### git log

Nous pouvons passer en revue les commits que nous avons effectués avec la commande `git log`. Si je l'exécute dans mon programme maintenant, j'obtiens cette sortie :

```bash
commit 67627dd44e84a3106a18a19e94cf9f3723e59b3c (HEAD -> master)
Author: amberwilkie <amber@amberwilkie.com>
Date:   Wed Apr 22 16:55:39 2020 -0400

    Mise à jour du premier console log

commit 49fe4152f474a9674a83e2b014a08828209d2690
Author: amberwilkie <amber@amberwilkie.com>
Date:   Wed Apr 22 16:54:59 2020 -0400

    Initial commit
```

Nous voyons nos messages de commit, l'heure à laquelle nous avons commité et un identifiant unique pour notre commit, que nous pouvons utiliser pour référencer les commits à l'avenir.

### git checkout

Si nous voulions revenir en arrière et voir les modifications apportées à notre code lors d'un commit précédent, nous le ferions avec `git checkout 49fe4152f474a9674a83e2b014a08828209d2690`. Git mettra notre code dans un état temporaire afin que nous puissions voir à quoi ressemblait le code à cet instant précis. 

J'ai copié l'ID de mon premier commit. Si j'exécute cette commande, mon programme affichera "Bonjour, ceci est un exemple git !" sur la première ligne.

Pour revenir au code le plus récent, vous taperez `git checkout master`.

## Branches

Si vous avez remarqué plus haut, nous avons dû taper `master` pour revenir à l'état actuel de notre code. Pourquoi ? Parce que `master` est le nom par défaut de la branche des branches — l'endroit où notre code est le plus à jour.

Git s'appuie sur les branches pour maintenir notre code. Vous pouvez considérer `master` comme le tronc de votre arbre de code. Vous pouvez vous en détacher pour effectuer des modifications, mais l'objectif final est toujours de les ramener vers le tronc, vers `master`.

Vous pouvez utiliser `git checkout` pour créer une nouvelle branche, et pas seulement pour consulter les versions précédentes de votre code. Essayez `git checkout -b new-branch`. Le flag `-b` est utilisé lorsque nous créons une nouvelle Branch et après le flag, nous écrivons le nom de notre nouvelle branche. Nous pouvons effectuer de nombreux commits sur cette branche et les ramener plus tard sur master grâce à un processus appelé **merging** (fusion).

Dans le schéma ci-dessous, les points représentent des commits. Deux branches ont été créées "à partir" de master. En développement logiciel, nous appelons souvent cela des branches de "fonctionnalités" (feature branches), par opposition à la branche principale master. La branche bleue a été fusionnée (merged) dans master et la branche jaune est toujours en cours de développement. 

Notez que même si la branche jaune a été créée après la branche bleue, seules les modifications provenant de master seront visibles dans cette branche. Si nous créions une troisième branche plus tard, les modifications de master et de la branche bleue seraient présentes dans cette nouvelle troisième branche.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-03-at-09.16.25.png)
_Visualisation des branches Git_



### git merge

`git merge` prendra tous les commits que vous avez effectués sur cette branche et les intégrera dans la branche `master`, sauvegardant ainsi votre travail.

### Pourquoi utiliser des branches ?

Si vous travaillez seul, il peut sembler peu utile de diviser votre travail en branches. Pourquoi ne pas tout sauvegarder sur `master` ? 

L'utilité du branching ne devient évidente que lorsque l'on commence à envisager de travailler en équipe. Si tous les développeurs effectuaient des commits sur la branche `master` à chaque modification, les choses deviendraient très vite confuses. Il serait également difficile de contrôler quel code part "en production" (en direct pour les clients) et quel code est encore en cours de test ou de développement. 

De cette façon, chaque développeur peut avoir sa propre branche (ou, probablement, plusieurs), travailler sur sa fonctionnalité aussi longtemps qu'il le souhaite, et la fusionner (merge) le moment venu.

## Qu'est-ce que GitHub ?

[GitHub](https://www.github.com) est une plateforme d'hébergement de code dans le cloud, gratuite (pour un usage personnel). Elle fonctionne avec Git sur votre ordinateur et ceux de vos collègues, servant d'**origin**, la source de vérité pour toute personne travaillant sur le code. 

Vous et vos collaborateurs téléchargez périodiquement votre code sur GitHub, et GitHub fournit des outils pour aider à gérer les modifications du code au fil du temps.

### Télécharger votre code sur GitHub

Tout d'abord, vous devrez créer un [compte GitHub](https://github.com/). Vous utiliserez ce compte pendant toute votre carrière de programmation, alors petit conseil : optez pour un nom professionnel, de préférence avec votre nom réel dedans. 

Une fois connecté, cherchez un `+` dans le coin supérieur. Cliquez sur "New Repository" (le nom des dossiers Git, "repo" en abrégé). Donnez-lui un nom — probablement le même que le dossier que vous avez créé précédemment où vous avez sauvegardé vos commits. Cliquez ensuite sur "Create Repository". Vous pouvez maintenant copier l'URL vers laquelle vous êtes redirigé et nous pouvons définir l'**origin** de notre code.

Il y aura une étape d'authentification à un moment donné — suivez simplement les instructions. Git est très efficace pour nous donner des instructions claires sur les prochaines étapes à suivre.

### git remote add origin

Nous allons maintenant dire à notre codebase (le dossier où se trouve notre code) où stocker notre code dans le cloud. Nous allons taper `git remote add origin <votre-url>`, ce qui définira un `origin` pour notre repository. Nous pouvons maintenant **push** (pousser) vers notre `origin` pour stocker notre code sur GitHub.

### git push

En supposant que nous soyons toujours dans notre branche `master` (c'est-à-dire que nous n'avons pas basculé sur une autre branche), nous pouvons maintenant taper `git push` et notre code sera envoyé sur GitHub.

### Visualiser votre code

Maintenant, votre code vit sur GitHub ! Voici à quoi ressemble mon exemple ci-dessus après avoir suivi les étapes GitHub expliquées :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-03-at-09.39.34.png)
_Dépôt GitHub pour l'exemple git de cet article_

Vous pouvez parcourir les fichiers et dossiers de votre repository, en visualisant l'état actuel du code. Vous pouvez également consulter les versions précédentes du code en cliquant sur "X commits" sur le côté droit, au milieu. Vous verrez une liste des commits effectués sur le repo et si vous cliquez dessus, vous pourrez parcourir les fichiers de votre projet _tels qu'ils existaient à cet instant précis_.

### Pull Requests

Il existe de nombreuses autres fonctionnalités sur GitHub, mais la plus importante pour collaborer avec des collègues est la **pull request**. Une pull request (très souvent abrégée en PR) est un moyen de gérer les modifications entrantes dans la base de code. 

Pour en créer une, vous créerez une nouvelle branche sur votre ordinateur local, effectuerez au moins un commit sur cette branche, puis taperez `git push origin head` pour envoyer cette branche sur GitHub. (Vous pouvez mettre le nom de votre branche à la place de `head`, mais c'est utile pour que tout corresponde exactement).

Maintenant, quand vous retournez sur GitHub, vous devriez voir votre branche disponible pour créer une PR.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-03-at-09.45.04.png)
_GitHub vous propose automatiquement de créer des PR à partir des nouvelles branches_

Si vous cliquez sur le bouton "Compare & pull request", vous pourrez modifier de nombreux paramètres pour votre PR. Les plus importants sont généralement le titre et la description. Si vous travaillez en équipe, vous pouvez taguer des collègues pour leur demander de relire votre code, l'ajouter à des projets, et bien d'autres fonctionnalités dont vous n'avez probablement pas encore besoin.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-03-at-09.48.31.png)
_Création d'une pull request sur GitHub_

Notez que nous comparons des branches. Ici, nous demandons d'ajouter les modifications de cette branche (`pr-example`) dans la branche `master`. Mais nous pourrions cibler n'importe quelle autre branche de notre repo. Pour l'instant, comprenez simplement que `master` n'est pas la seule branche sur laquelle vous pouvez "faire une pull request".

Lorsque vous cliquez sur "Create Pull Request", vous verrez cet écran :

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Screenshot-2020-05-03-at-09.52.36.png)
_Exemple de pull request_

Vous pouvez voir tous les commits de cette branche (je n'en ai qu'un seul — "Modification de la troisième ligne du programme"), et vous pouvez également **merge** votre pull request. 

Vous vous souvenez comment nous pouvions fusionner notre code localement avec Git ? Nous pouvons effectuer la même action avec notre code hébergé dans le cloud sur GitHub. Si vous cliquez sur le bouton vert "Merge pull request", vos modifications seront fusionnées dans master.

### git pull

La dernière commande que vous devez connaître pour l'instant est `git pull`. Si vous avez fusionné votre PR dans la branche `master` sur GitHub, il y a maintenant des modifications sur l'**origin** que vous n'avez pas encore sur votre ordinateur local. Si vous vous placez sur la branche `master`, puis tapez `git pull origin master`, les modifications que vous venez de fusionner seront désormais sur votre ordinateur local. 

```
➜  git-example git:(master) git pull origin master
From https://github.com/AmberWilkie/git-example
 * branch            master     -> FETCH_HEAD
Updating 67627dd..38ad2da
Fast-forward
 git.js | 2 +-
 1 fichier modifié, 1 insertion(+), 1 suppression(-)
```

Ce "Fast-forward" fait référence à notre branche master locale qui "rattrape" la branche `origin` sur GitHub. Nous avons bouclé la boucle :

* Modifications locales
* Push vers GitHub et création d'une PR
* Merge de la PR dans master
* Pull de master vers l'ordinateur local

Une fois que vous serez à l'aise avec ces étapes, vous aurez parcouru 80 % du chemin pour maîtriser Git et GitHub !