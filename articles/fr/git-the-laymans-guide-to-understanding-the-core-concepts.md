---
title: 'Git : Le guide du débutant pour comprendre les concepts de base du contrôle
  de version'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-12T12:00:00.000Z'
originalURL: https://freecodecamp.org/news/git-the-laymans-guide-to-understanding-the-core-concepts
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca066740569d1a4ca4872.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: 'Git : Le guide du débutant pour comprendre les concepts de base du contrôle
  de version'
seo_desc: "By Bob Ziroll\nGit is a vital tool in the toolbelt of any developer. \n\
  For example, just the other day I was able to fix a major problem I had pushed to\
  \ production (totally my fault) in about 20 minutes. This would have probably taken\
  \ me days to fix wi..."
---

Par Bob Ziroll

Git est un outil vital dans la boîte à outils de tout développeur. 

Par exemple, il y a quelques jours, j'ai pu corriger un problème majeur que j'avais poussé en production (totalement de ma faute) en environ 20 minutes. Sans Git, cela m'aurait probablement pris des jours à corriger.

%[https://twitter.com/bobziroll/status/1164527368519610368?s=20]

Alors, prenons le temps de vraiment comprendre les fonctionnalités les plus basiques de Git : **la mise en stage et le commit**.

> Note : cet article ne couvre rien concernant [GitHub](https://github.com), qui est un service web en ligne tiers qui vous permet de sauvegarder le code que vous enregistrez avec Git dans le cloud. _**Git**_ est local, _**GitHub**_ est une application basée sur le cloud, et ce sont deux choses complètement différentes avec un but commun.

## Qu'est-ce que le contrôle de version ?

Si vous êtes assez âgé, vous vous souvenez probablement d'un monde avant Google Drive/Docs/Sheets où vous aviez une situation comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/group_project_example.png)
_Groupe_Papier_Tous_4_Membres_Sections_Incluses_Brouillon_Final_Final_3?.docx_

Travailler sur un projet de groupe conduisait à plusieurs personnes essayant de faire des modifications sur plusieurs copies d'un document original, ce qui menait à de nombreuses duplicatas. Si deux personnes faisaient des modifications en même temps, quelqu'un devait tout passer en revue manuellement et combiner ces modifications ensemble.

Il n'y avait aucun moyen réel de contrôler les différentes versions du projet. C'était essentiellement le Far West. 🤠+🐎

**Git résout ce problème 🎯**

Peut-être avez-vous codé une nouvelle fonctionnalité dans votre projet, cassé quelque chose qui fonctionnait très bien avant, mais vous n'avez aucune idée de l'endroit où trouver le bug ou comment le corriger. Vous avez depuis fermé le fichier dans votre éditeur, donc utiliser "annuler" n'est plus une option.

**Git résout ce problème 🎯**

## D'accord, mais _comment_ Git résout-il ces problèmes ?

La fonctionnalité principale de Git est de créer des points de sauvegarde dans vos fichiers. J'aime penser à ces points de sauvegarde comme à ceux des jeux vidéo - des points de contrôle que vous atteignez où, même si vous gâchez tout après ce point, vous pouvez toujours revenir et réessayer sans avoir à tout recommencer.

Il y a beaucoup d'autres aspects géniaux de Git, mais au cœur, c'est de cela qu'il s'agit : créer des points de sauvegarde dans votre code auxquels vous pouvez revenir plus tard si vous le souhaitez.

## Comment fonctionne Git ?

Cette fonctionnalité principale de Git (créer des points de sauvegarde dans votre projet) fonctionne en 2 phases :

1. Ajouter des choses (code et fichiers modifiés) à une zone de staging pour être commit (sauvegardé) dans une timeline, et
2. Effectuer le commit (sauvegarder) de ces choses.

## Analogie obligatoire

Pensez à ces deux phases comme si vous créiez un album photo à l'ancienne, un dans lequel vous imprimiez des photos et les placiez dans un vrai livre. Au cas où vous seriez trop jeune, voici ce dont je parle :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/photo-album-631084_960_720.jpg)
_D'accord, je ne suis pas vraiment aussi vieux que ça_

**Premièrement**, vous prenez un tas de photos avec votre appareil photo. Prendre une photo seule n'affecte pas l'album photo car vous pouvez toujours choisir les photos que vous voulez inclure dans l'album. Vous pouvez prendre de mauvaises photos et simplement les reprendre si nécessaire.

**Ensuite**, vous choisissez parmi toutes les photos que vous avez prises celles que vous voulez sauvegarder dans l'album photo. Imaginez que vous les avez déjà imprimées et que vous les placez à côté de la page vide de votre album photo. Vous créez une sorte de "zone de staging" où vous n'avez pas encore collé les photos sur la page de l'album photo, mais vous vous préparez à le faire bientôt.

**Enfin**, une fois que vous êtes prêt, vous collez vos photos sur la page et les cimentez essentiellement dans le temps. Une partie importante d'un bon album photo est d'inclure un message ou un titre qui décrit les événements entourant ces photos.

Une fois que vous avez fait cela, vous pouvez toujours revenir à cette page de votre album photo et vous souvenir de ce que les choses étaient à cette époque de votre vie (en bien ou en mal).

## Comment cela se rapporte-t-il à Git ?

Relions cette analogie à Git.

* Prendre des photos est comme modifier des fichiers de projet (écrire du code, créer des fichiers ou supprimer des fichiers).
* Choisir les photos que vous voulez dans votre album photo est comme ajouter vos modifications à une "zone de staging".
* Coller les photos dans la page de l'album photo est comme commiter (sauvegarder) vos modifications dans une timeline de modifications.

Décomposons cela un peu plus.

### Prendre des photos est comme modifier vos fichiers de projet

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-219.png)
_Photo par [Unsplash](https://unsplash.com/@wbayreuther?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">William Bayreuther</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Prendre des photos est comme apporter des modifications à votre projet - écrire du nouveau code, ajouter des images, supprimer des anciens fichiers, etc. Vous créez le contenu que vous souhaitez éventuellement sauvegarder dans le commit Git ("point de sauvegarde"). C'est encore un travail en cours, et vous pouvez toujours écrire, réécrire et supprimer tout ce que vous voulez sans que rien ne soit "permanemment" sauvegardé pour l'instant.

La seule chose que Git fait à ce stade est de surveiller pour voir si quelque chose a changé depuis la dernière fois que vous avez commit (sauvegardé) votre code. Si vous ajoutez une ligne de code puis la supprimez, Git verra que rien n'a globalement changé. Si vous écrivez 500 lignes de code dans des dizaines de fichiers, Git sait exactement quelles lignes de code ont été ajoutées à quels fichiers et suit ces modifications dans sa mémoire. Il ne committera rien dans la timeline des modifications jusqu'à ce que vous le lui disiez, mais il vous surveille de près 👀

> Note : souvenez-vous que nous parlons toujours d'un processus totalement séparé de la sauvegarde de vos modifications sur votre disque dur. Les éditeurs de texte modernes peuvent sauvegarder votre code toutes les secondes, mais ce n'est pas ce à quoi nous faisons référence ici. Lorsque je parle de "sauvegarder" avec Git, je veux dire créer un commit qui sauvegarde vos modifications dans une timeline.

### Imprimer/préparer les photos choisies est comme ajouter vos modifications de projet à la "zone de staging"

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-220.png)
_Photo par [Unsplash](https://unsplash.com/@sarandywestfall_photo?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">sarandy westfall</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Avec Git, c'est la phase qui se produit _avant_ de créer un nouveau commit dans votre code. Ce processus est appelé "ajout à la zone de staging". Ajouter à la zone de staging ne crée pas le commit, cela le _prépare_ simplement.

Après avoir ajouté certains fichiers à la zone de staging, vous pouvez réaliser que vous avez encore des modifications à faire. Pas de problème ! Puisque Git n'a pas encore réellement sauvegardé (commit) quoi que ce soit, vous pouvez simplement faire les nouvelles modifications que vous souhaitez et ensuite ajouter ces modifications à la zone de staging aussi, même si ces modifications se produisent dans le même fichier qu'un fichier précédemment ajouté. Cela serait comme prendre de nouvelles photos que vous avez décidé d'ajouter à la page de l'album photo et les imprimer.

### Coller des photos dans l'album est comme commiter votre code

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-221.png)
_Photo par [Unsplash](https://unsplash.com/@thirdwheelphoto?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Julie Johnson</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

C'est la deuxième (et dernière) phase pour créer votre "point de sauvegarde" (commit). Il y a une exigence majeure lorsque vous créez un commit : **vous devez inclure un message**. Dans l'album photo, vous pouvez écrire un titre ou un message pour donner des informations à un futur observateur sur ce que ces photos signifiaient pour vous. Dans Git, vous écrivez un message pour décrire les modifications que vous sauvegardez dans votre base de code.

Si vous écrivez un mauvais message de commit, regarder l'historique de votre code ne sera pas très utile pour qui que ce soit, y compris vous-même. (À quoi bon un message comme "apporte quelques modifications" si vous n'avez aucune idée de ce que sont ces modifications ? Imaginez trouver une page dans un album photo qui disait simplement "Voici quelques personnes"...) Faites-vous et aux autres une faveur et **utilisez toujours de bons messages de commit descriptifs** qui décrivent la fonctionnalité ou la correction que vous ajoutez à la base de code.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/git_commit_2x.png)
_Ne faites pas cela 😅[https://xkcd.com/1296/](https://xkcd.com/1296/)_

## Installation

Assez d'analogies, commençons !

### Installation

Tout d'abord, vous avez peut-être déjà Git installé. Ouvrez un Terminal/Invite de commande et essayez d'exécuter `git --version`. Si cela affiche un numéro de version, passez à la section suivante. Si cela ne sait pas ce que vous voulez dire par `git`, vous devez l'installer. [Suivez ces instructions](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git) pour le faire pour votre système d'exploitation.

### Créer un dépôt Git

Git ne sait suivre que les projets que vous avez configurés pour être des dépôts Git. Dans l'analogie ci-dessus, nous ne pouvions pas coller des photos dans un album photo si nous n'avions pas d'album photo en premier lieu.

Lorsque vous êtes prêt à commencer un nouveau projet, l'une des premières étapes que vous devriez faire (après avoir créé le dossier du projet) est d'exécuter :

```git
git init
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-24-at-11.37.09-AM.png)

Cela permet à Git de commencer à suivre toutes les modifications que vous apportez à votre projet immédiatement. Sous le capot, il crée un nouveau dossier caché `.git` avec tout ce dont il a besoin pour suivre vos modifications. Vous aurez rarement besoin d'aller dans ce dossier sauf si vous configurez des choses avancées, alors pour l'instant, prévoyez de le laisser tranquille.

### Apporter des modifications à votre projet

Pour le tutoriel ci-dessous, je vais garder les choses aussi simples que possible - un dossier de projet qui est un dépôt Git avec un seul fichier `README.md` markdown à l'intérieur. Si cela aide, vous pouvez imaginer que chaque modification que j'apporte au fichier README représente une nouvelle fonctionnalité et des dizaines ou des centaines de lignes de nouveau code. Cela me rendra aussi plus impressionnant. 😎

## Commandes de base

### `git status`

J'aime penser à cela comme une "vérification de santé mentale" pour m'aider à savoir ce que Git croit être en train de se passer maintenant. (Quelles modifications il a remarquées, si tout fonctionne comme il se doit, etc.)

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-24-at-11.38.21-AM.png)

Il me dit que je suis sur la branche master (je créerai un article séparé sur le branchement à un autre moment), que je n'ai pas encore de commits précédents, et que je n'ai rien à commiter maintenant. (C'est-à-dire, Git ne voit rien dans ce dossier à sauvegarder du tout).

Maintenant, j'ajoute mon fichier README.md et j'exécute à nouveau git status :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-24-at-11.40.35-AM.png)
_La commande `touch` est juste un moyen rapide et facile de créer de nouveaux fichiers vides._

Git voit que j'ai ajouté un nouveau fichier à mon projet ! Cool. Maintenant que ce nouveau projet génial est en cours, créons un point de sauvegarde. Parce que, vous savez, il serait difficile de revenir à ce point à partir de zéro !

### `git add`

La commande `git add` est la façon dont nous mettons les choses dans la zone de staging. Comme imprimer les photos que nous avons prises avant de les coller dans notre page d'album photo. Cependant, nous devons dire à Git _quoi_ nous voulons ajouter à la zone de staging. (Seulement entrer `git add` vous dira que rien n'a été spécifié donc rien n'a été ajouté.) Je vais mettre le nom de fichier du fichier que je veux ajouter en utilisant Git :

```git
git add README.md
git status
```

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-08-24-at-12.21.22-PM.png)

Utiliser `git status` à nouveau nous dit que nous avons un nouveau fichier dans la zone de staging, mais il est devenu vert maintenant ! C'est ma façon facile de savoir qu'il a été ajouté à la zone de staging.

En gros, ce que `git add README.md` a fait, c'est dire à Git "Je veux inclure toutes les modifications apportées à README.md depuis le dernier commit pour être incluses dans le prochain commit."

Cependant, ajouter des fichiers à la zone de staging un par un comme cela est fastidieux, surtout puisque de nombreuses tâches vous obligent à travailler avec de nombreux fichiers. Au lieu de devoir vous souvenir et spécifier chaque fichier sur lequel vous travaillez, vous pouvez utiliser une sorte de "fourre-tout" qui ajoutera automatiquement chaque fichier dans lequel vous avez apporté des modifications à la zone de staging. Ma façon préférée de faire cela est d'utiliser :

```git
git add -A
```

(Le drapeau `-A` indique d'ajouter _tous_ les fichiers avec des modifications à la zone de staging).

> Note : vous verrez souvent les gens utiliser `git add .` pour accomplir le même objectif d'ajouter toutes les modifications à la zone de staging. Bien que cela fonctionne, cela nécessite que vous soyez dans le répertoire racine du projet pour vous assurer de capturer toutes les modifications. (Le `.` est une abréviation pour "le répertoire actuel"). Donc si vous `cd` dans un répertoire imbriqué mais que vous avez apporté des modifications à un fichier en dehors de ce répertoire et que vous essayez d'utiliser `git add .`, vous manquerez ces fichiers modifiés lorsque vous essayez de les ajouter à la zone de staging. `git add -A`, cependant, fonctionne pour tout le projet peu importe où vous vous trouvez actuellement dans le Terminal.

### `git commit`

Une fois que vous êtes prêt à créer un commit, vous le ferez avec la commande `git commit`. Cependant, souvenez-vous que vous devez laisser un message ? Si vous exécutez simplement `git commit` et appuyez sur Entrée, vous serez redirigé vers un éditeur basé sur le Terminal comme Vi ou Nano pour remplir un message pour ce commit.

Au lieu de cela, vous pouvez laisser un message directement en ligne avec votre `git commit` en utilisant le drapeau `-m` suivi d'un message de chaîne entre guillemets. Quelque chose comme ceci :

```git
git commit -m "Ajouté des informations vraiment importantes au README"
```

En supposant que tout le reste était en ordre avant que vous ne committiez, vous avez maintenant réussi à commiter votre code avec Git ! Maintenant, vous avez un point de contrôle auquel vous pouvez toujours revenir si tout va mal à partir de maintenant.

Regardons à nouveau ce processus sous forme de gif :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Git-gif.gif)

> Note : le gif utilise `git add`, mais j'aurais dû utiliser `git add -A` pour être plus précis. De plus, utilisez de meilleurs messages de commit ! Veuillez excuser mes erreurs 🙏

### `git log`

Vous pouvez jeter un coup d'œil à votre historique de commits en exécutant `git log`. En utilisant les touches fléchées, vous pouvez faire défiler vers l'avant et vers l'arrière dans le temps pour vérifier les dates de commit, les messages et les auteurs (la personne qui a fait le commit). Avec chacun de ceux-ci vient un "hash de commit", qui est essentiellement un ID unique (long) pour le commit qui peut être utilisé pour le référencer plus tard si nécessaire.

## Voyage dans le temps

_"Donc vous continuez à parler de la façon dont Git peut me permettre de sauter en avant et en arrière dans le temps... comment fais-je cela réellement ?"_

### `git checkout`

Le terme "checkout" fait référence au processus de passage d'un commit à un autre. Vous vous souvenez de l'ID unique ("hash") que chaque commit reçoit ? Je peux regarder mon historique de commits, choisir l'un de ces hashs de commit uniques, et le vérifier avec la commande `git checkout`. Si le commit que je veux regarder a un hash de `a2` (en réalité, ils sont beaucoup plus longs que cela - comme `0c9b8f7c23dea4cf0a0285f14211124b6d5891e9`), je peux exécuter :

```git
git checkout a2
```

Soudain, toute ma base de code va zoomer dans le temps et tout aura l'air comme c'était juste après que j'ai fait ce commit. (Cela peut être effrayant car il peut sembler que vous avez perdu toutes les mises à jour depuis ce commit, mais ne vous inquiétez pas ! Elles sont toujours là, attendant pour vous... _dans le futur !_)

En forme de gif :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/git_checkout-2.gif)
_Remarquez que le 3ème commit et les modifications qui y sont apportées existent toujours complètement. Revenez à ce commit avec `git checkout a3` ou (plus couramment) `git checkout master` pour ramener toutes vos modifications._

Maintenant que vous êtes revenu dans le temps, vous verrez un message de Git. Quelque chose comme :

```git
Note : checking out 'a2'.

You are in 'detached HEAD' state. You can look around, make experimental
changes and commit them, and you can discard any commits you make in this
state without impacting any branches by performing another checkout.

If you want to create a new branch to retain commits you create, you may
do so (now or later) by using -b with the checkout command again. Example:

  git checkout -b <new-branch-name>

HEAD is now at a2 Another Message
```

Dans cet état, vous n'êtes plus sur la branche `master`, ce qui signifie que vous pouvez faire des modifications expérimentales ici et même créer de nouveaux commits, tout cela sans perdre votre code sur la branche `master` (hash de commit `a3` dans l'exemple ci-dessus).

Encore une fois, je prévois de couvrir le branchement à un autre moment, mais cela est juste pour souligner le fait que Git est un outil vraiment puissant lorsqu'il s'agit de sauvegarder plusieurs versions de votre code.

# Conclusion

Il y a un million de choses que vous pourriez apprendre sur Git, mais sans comprendre les concepts de base, cela restera toujours un peu un mystère.

Cependant, si vous voulez vraiment apprendre et vous familiariser avec Git, la meilleure chose que vous puissiez faire est de jouer et d'expérimenter avec. Lors de la journée d'orientation à [V School](https://vschool.io), je dis toujours à nos nouveaux étudiants que _la manière la plus facile d'apprendre quelque chose de nouveau est de le faire de la manière difficile_. 

Cela signifie se forcer à faire plus que simplement lire un article et espérer apprendre le contenu. Alors, allez créer un nouveau dépôt Git dans un dossier vide, commencez à ajouter des fichiers, utilisez `git status` et `git log` plusieurs fois pour voir à quoi ressemblent les choses, et envisagez de télécharger [Sourcetree](https://www.sourcetreeapp.com/) par Atlassian pour visualiser l'état de votre dépôt pendant que vous manipulez les choses.

Une fois que vous aurez surmonté la courbe d'apprentissage avec Git, vous vous demanderez comment vous avez jamais fait du développement sans lui !