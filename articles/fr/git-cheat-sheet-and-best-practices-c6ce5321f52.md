---
title: Voici toutes les commandes Git que j'ai utilisées la semaine dernière, et ce
  qu'elles font.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-08-06T07:15:22.000Z'
originalURL: https://freecodecamp.org/news/git-cheat-sheet-and-best-practices-c6ce5321f52
coverImage: https://cdn-media-1.freecodecamp.org/images/1*frC0VgM2etsVCJzJrNMZTQ.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Voici toutes les commandes Git que j'ai utilisées la semaine dernière,
  et ce qu'elles font.
seo_desc: 'By Sam Corcos

  Like most newbies, I started out searching StackOverflow for Git commands, then
  copy-pasting answers, without really understanding what they did.


  _Image credit: [XKCD](https://xkcd.com/1597/" rel="noopener" target="blank" title=")

  I re...'
---

Par Sam Corcos

Comme la plupart des débutants, j'ai commencé par chercher des commandes Git sur StackOverflow, puis à copier-coller des réponses, sans vraiment comprendre ce qu'elles faisaient.

![Image](https://cdn-media-1.freecodecamp.org/images/0qFQGxysX9XwKkft-6Sq0C4JyqfpRLzwvBkZ)
_Crédit image : [XKCD](https://xkcd.com/1597/" rel="noopener" target="_blank" title=")_

Je me souviens avoir pensé : « Ne serait-ce pas bien s'il existait une liste des commandes Git les plus courantes avec une explication de leur utilité ? »

Eh bien, me voilà des années plus tard pour compiler une telle liste et présenter quelques bonnes pratiques que même les développeurs intermédiaires et avancés devraient trouver utiles.

Pour rester pratique, je base cette liste sur les commandes Git que j'ai réellement utilisées au cours de la semaine dernière.

Presque tous les développeurs utilisent Git, et très probablement GitHub. Mais le développeur moyen utilise probablement seulement ces trois commandes 99 % du temps :

```
git add --all
git commit -am "<message>"
git push origin master
```

C'est très bien lorsque vous travaillez sur un projet solo, un hackathon ou une application jetable, mais lorsque la stabilité et la maintenance deviennent une priorité, nettoyer les commits, respecter une stratégie de branchement et écrire des messages de commit cohérents devient important.

Je vais commencer par la liste des commandes couramment utilisées pour faciliter la compréhension des débutants sur ce qui est possible avec Git, puis passer aux fonctionnalités plus avancées et aux bonnes pratiques.

#### Commandes régulièrement utilisées

Pour initialiser Git dans un dépôt (repo), il suffit de taper la commande suivante. Si vous n'initialisez pas Git, vous ne pouvez pas exécuter d'autres commandes Git dans ce repo.

```
git init
```

Si vous utilisez GitHub et que vous poussez du code vers un repo GitHub stocké en ligne, vous utilisez un repo **distant**. Le nom par défaut (également connu sous le nom d'alias) pour ce repo distant est **origin**. Si vous avez copié un projet depuis GitHub, il a déjà un **origin**. Vous pouvez voir cet origin avec la commande **git remote -v**, qui listera l'URL du repo distant.

Si vous avez initialisé votre propre repo Git et que vous souhaitez l'associer à un repo GitHub, vous devrez en créer un sur GitHub, copier l'URL fournie et utiliser la commande **git remote add origin <URL>**, en remplaçant "<URL>" par l'URL fournie par GitHub. À partir de là, vous pouvez ajouter, commiter et pousser vers votre repo distant.

La dernière commande est utilisée lorsque vous devez changer le dépôt distant. Supposons que vous avez copié un repo de quelqu'un d'autre et que vous souhaitez changer le dépôt distant du propriétaire original vers votre propre compte GitHub. Suivez le même processus que **git remote add origin**, mais utilisez **set-url** à la place pour changer le repo distant.

```
git remote -v
git remote add origin <url>
git remote set-url origin <url>
```

La manière la plus courante de copier un repo est d'utiliser **git clone**, suivi de l'URL du repo.

Gardez à l'esprit que le dépôt distant sera lié au compte à partir duquel vous avez clonné le repo. Donc, si vous avez clonné un repo appartenant à quelqu'un d'autre, vous ne pourrez pas pousser vers GitHub tant que vous n'aurez pas changé l'**origin** en utilisant les commandes ci-dessus.

```
git clone <url>
```

Vous vous retrouverez rapidement à utiliser des branches. Si vous ne comprenez pas ce que sont les branches, il existe d'autres tutoriels beaucoup plus détaillés, et vous devriez les lire avant de continuer ([en voici un](https://docs.github.com/fr/get-started/quickstart/github-flow)).

La commande **git branch** liste toutes les branches sur votre machine locale. Si vous souhaitez créer une nouvelle branche, vous pouvez utiliser **git branch <name>**, avec **<name>** représentant le nom de la branche, comme "master".

La commande **git checkout <name>** bascule vers une branche existante. Vous pouvez également utiliser la commande **git checkout -b <name>** pour créer une nouvelle branche et basculer immédiatement dessus. La plupart des gens utilisent cette commande au lieu de commandes séparées pour la branche et le checkout.

```
git branch
git branch <name>
git checkout <name>
git checkout -b <name>
```

Si vous avez apporté un tas de modifications à une branche, appelons-la "develop", et que vous souhaitez fusionner cette branche dans votre branche **master**, vous utilisez la commande **git merge <branch>**. Vous voudrez **checkout** la branche master, puis exécuter **git merge develop** pour fusionner develop dans la branche master.

```
git merge <branch>
```

Si vous travaillez avec plusieurs personnes, vous vous retrouverez dans une situation où un repo a été mis à jour sur GitHub, mais vous n'avez pas les modifications localement. Si c'est le cas, vous pouvez utiliser **git pull origin <branch>** pour récupérer les modifications les plus récentes de cette branche distante.

```
git pull origin <branch>
```

Si vous êtes curieux de voir quels fichiers ont été modifiés et ce qui est suivi, vous pouvez utiliser **git status**. Si vous voulez voir _combien_ chaque fichier a été modifié, vous pouvez utiliser **git diff** pour voir le nombre de lignes modifiées dans chaque fichier.

```
git status
git diff --stat
```

### Commandes avancées et bonnes pratiques

Bientôt, vous atteignez un point où vous voulez que vos commits soient beaux et cohérents. Vous devrez peut-être également manipuler votre historique de commits pour rendre vos commits plus faciles à comprendre ou pour annuler un changement accidentel.

La commande **git log** vous permet de voir l'historique des commits. Vous voudrez utiliser cela pour voir l'historique de vos commits.

Vos commits seront accompagnés de messages et d'un **hash**, qui est une série aléatoire de chiffres et de lettres. Un exemple de hash pourrait ressembler à ceci : **c3d882aa1aa4e3d5f18b3890132670fbeac912f7**

```
git log
```

Supposons que vous avez poussé quelque chose qui a cassé votre application. Plutôt que de le corriger et de pousser quelque chose de nouveau, vous préféreriez simplement revenir à un commit précédent et réessayer.

Si vous voulez revenir en arrière et **checkout** votre application à partir d'un commit précédent, vous pouvez le faire directement en utilisant le hash comme nom de branche. Cela détachera votre application de la version actuelle (parce que vous modifiez un enregistrement historique, plutôt que la version actuelle).

```
git checkout c3d88eaa1aa4e4d5f
```

Ensuite, si vous apportez des modifications à partir de cette branche historique et que vous souhaitez pousser à nouveau, vous devrez faire un push forcé.

**Attention** : Le push forcé est dangereux et ne doit être fait que si vous en avez absolument besoin. Il écrasera l'historique de votre application et vous perdrez tout ce qui est venu après.

```
git push -f origin master
```

Parfois, il n'est tout simplement pas pratique de garder tout dans un seul commit. Peut-être voulez-vous sauvegarder votre progression avant d'essayer quelque chose de potentiellement risqué, ou peut-être avez-vous fait une erreur et souhaitez-vous vous épargner la gêne d'avoir une erreur dans votre historique de version. Pour cela, nous avons **git rebase**.

Supposons que vous avez 4 commits dans votre historique local (non poussés vers GitHub) dans lesquels vous avez fait des allers-retours. Vos commits semblent désordonnés et indécis. Vous pouvez utiliser rebase pour combiner tous ces commits en un seul commit concis.

```
git rebase -i HEAD~4
```

La commande ci-dessus ouvrira l'éditeur par défaut de votre ordinateur (qui est Vim sauf si vous l'avez défini sur autre chose), avec plusieurs options pour modifier vos commits. Cela ressemblera à quelque chose comme le code ci-dessous :

```
pick 130deo9 oldest commit message
pick 4209fei second oldest commit message
pick 4390gne third oldest commit message
pick bmo0dne newest commit message
```

Pour les combiner, nous devons changer l'option "pick" en "fixup" (comme le dit la documentation sous le code) pour fusionner les commits et supprimer les messages de commit. Notez que dans vim, vous devez appuyer sur "**a**" ou "**i**" pour pouvoir éditer le texte, et pour sauvegarder et quitter, vous devez taper la touche **échappement** suivie de "**shift + z + z**". Ne me demandez pas pourquoi, c'est juste comme ça.

```
pick 130deo9 oldest commit message
fixup 4209fei second oldest commit message
fixup 4390gne third oldest commit message
fixup bmo0dne newest commit message
```

Cela fusionnera tous vos commits dans le commit avec le message "oldest commit message".

L'étape suivante consiste à renommer votre message de commit. Cela relève entièrement de l'opinion, mais tant que vous suivez un modèle cohérent, tout ce que vous faites est bien. Je recommande d'utiliser les [directives de commit publiées par Google pour Angular.js](https://github.com/angular/angular.js/blob/master/CONTRIBUTING.md#-git-commit-guidelines).

Pour changer le message de commit, utilisez le flag **amend**.

```
git commit --amend
```

Cela ouvrira également vim, et les règles d'édition et de sauvegarde de texte sont les mêmes que ci-dessus. Pour donner un exemple de bon message de commit, en voici un suivant les règles des directives :

```
feat: ajouter le bouton de paiement stripe à la page des paiements

- ajouter le bouton de paiement stripe
- écrire des tests pour le paiement
```

Un avantage à respecter les **types** listés dans les directives est que cela facilite la rédaction des journaux de modifications. Vous pouvez également inclure des informations dans le **pied de page** (encore une fois, spécifié dans les directives) qui référence les problèmes.

**Note** : vous devriez éviter de rebaser et d'écraser vos commits si vous collaborez sur un projet et avez du code poussé vers GitHub. Si vous commencez à changer l'historique des versions sous le nez des gens, vous pourriez finir par rendre la vie de tout le monde plus difficile avec des bugs difficiles à suivre.

Il existe un nombre presque infini de commandes possibles avec Git, mais ces commandes sont probablement les seules que vous devrez connaître pour vos premières années de programmation.

_Sam Corcos est le développeur principal et cofondateur de Sightline Maps, la plateforme la plus intuitive pour l'impression 3D de cartes topographiques, ainsi que de [LearnPhoenix.io](http://learnphoenix.io/), un site de tutoriels intermédiaires-avancés pour construire des applications de production scalables avec Phoenix et React._