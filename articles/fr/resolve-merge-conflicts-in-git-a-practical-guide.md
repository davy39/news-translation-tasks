---
title: Comment résoudre les conflits de fusion dans Git – Un guide pratique avec des
  exemples
subtitle: ''
author: Tapas Adhikary
co_authors: []
series: null
date: '2022-05-09T23:09:43.000Z'
originalURL: https://freecodecamp.org/news/resolve-merge-conflicts-in-git-a-practical-guide
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/freeCodeCamp-Cover-1.png
tags:
- name: Collaboration
  slug: collaboration
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment résoudre les conflits de fusion dans Git – Un guide pratique avec
  des exemples
seo_desc: "Git is an open-source distributed version control system. It helps you\
  \ manage your project files easily using local branching, staging, and workflows.\
  \ \nMany developers use Git today. And they're usually familiar with basic Git concepts\
  \ like:\n\nHow to ..."
---

`Git` est un système de contrôle de version distribué open-source. Il vous aide à gérer facilement les fichiers de votre projet en utilisant le branchement local, la mise en attente et les flux de travail. 

De nombreux développeurs utilisent Git aujourd'hui. Et ils sont généralement familiers avec les concepts de base de Git comme :

* Comment initier un dépôt.
* Comment créer des branches.
* Comment mettre en attente/annuler la mise en attente des changements.
* Comment valider les changements.
* Comment pousser les validations vers le dépôt distant.

Cependant, de nombreux développeurs sont confus concernant des concepts comme `fusion` et `résolution des conflits de fusion`. Dans cet article, nous allons apprendre comment résoudre les conflits de fusion de manière pratique. Cela signifie que vous allez lire, comprendre et essayer pendant que vous parcourez cet article.

Si vous aimez apprendre à partir de contenu vidéo également, cet article est également disponible sous forme de tutoriel vidéo ici : 👨‍💻

%[https://www.youtube.com/watch?v=OulZeVtZhZQ]

Si vous êtes nouveau dans Git et que vous souhaitez apprendre tous les concepts de base, [voici un cours accéléré utile](https://www.youtube.com/watch?v=vWtu4mzUgQo).

## Que disent les développeurs à propos des "Conflits de Fusion" ?

Récemment, j'ai mené un sondage sur Twitter, LinkedIn et YouTube, demandant si les développeurs étaient à l'aise avec la résolution des conflits de fusion dans Git. Devinez ce que j'ai trouvé ? 

70%-80% des développeurs ont partagé qu'ils trouvaient difficile de résoudre un conflit de fusion dans Git. Donc, cela signifie que "Résoudre les Conflits de Fusion" est un sujet important de discussion.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/poll.png)
_Résultats du sondage - Êtes-vous à l'aise pour résoudre les conflits de fusion dans Git ?_

## Qu'est-ce que la Fusion Git et que sont les Conflits de Fusion ?

`Git` est un système de contrôle de version qui conserve un historique de toutes les versions de vos fichiers. Vous pouvez revenir à n'importe quelle version à tout moment et récupérer une version plus ancienne.

Supposons que vous avez créé un fichier appelé `abc.txt` et que vous l'avez poussé vers un dépôt Git. À ce stade, le fichier a sa version actuelle associée. Maintenant, si votre collègue a modifié le même fichier et l'a repoussé vers le dépôt, le fichier a une nouvelle version associée.

`Git Merge` est une fonctionnalité qui vous permet de garder le contenu actuel du fichier synchronisé avec d'autres versions précédentes. Cela est essentiel car toute personne à tout moment devrait travailler sur le contenu le plus récent du fichier sans écraser les changements des versions précédentes. 

Git `merge` vous aide à fusionner les changements d'autres développeurs avant de pousser un nouveau changement vers le même fichier.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-46.png)

Dans le cas de la fusion Git, nous devons être conscients de deux choses :

1. **Changements** : Quel type d'opérations s'est produit entre deux versions d'un fichier ? Du nouveau contenu est ajouté ou supprimé, ou le contenu existant est mis à jour.
2. **Possibilités** : Il y a deux possibilités. Les changements ont eu lieu dans les `régions différentes` du fichier ou les changements ont eu lieu dans la `même région` du fichier. Même région signifie que les développeurs ont apporté des changements autour du même endroit (par exemple, paragraphes, lignes, etc.) d'un fichier.

Heureusement, Git gère automatiquement la plupart de ces cas en utilisant la stratégie `auto-merge`. Mais lorsque les changements ont eu lieu dans la `même région` du fichier, Git n'effectuera pas de fusion automatique. Au lieu de cela, il vous laisse `Résoudre les Conflits de Fusion`.

## Conflits de Fusion Git : Une Histoire d'Horreur

Comprenons les situations ci-dessus avec une histoire de deux développeurs, Alex et Tina. 

Un beau jour,

* Alex a tiré les changements du dépôt distant vers son dépôt local.
* Il a modifié le fichier appelé `abc.txt`, l'a mis en attente, l'a validé et finalement l'a repoussé vers le dépôt distant.
* Pendant ce temps, Tina, ignorant les changements d'Alex dans le fichier `abc.txt`, a apporté quelques modifications dans la `même région` du fichier et a essayé de le pousser vers le dépôt distant.
* `Git` est un système de contrôle de version, donc il a averti Tina qu'elle avait modifié la version plus ancienne que celle du dépôt distant (car les changements d'Alex étaient déjà dans le dépôt distant).
* Maintenant, Tina doit d'abord tirer les changements du dépôt distant, mettre à jour le fichier, puis essayer de pousser à nouveau.
* Tina l'a fait. Cependant, dans son pire cauchemar, elle a reçu l'avertissement que l'`auto-merge` a échoué, et donc elle doit maintenant `Résoudre les conflits de fusion`.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/image-45.png)

Cette histoire vous dit-elle quelque chose ? L'histoire ci-dessus vous concerne-t-elle ? Il y a une chance que vous ayez été dans les chaussures de Tina dans le passé. Si ce n'est pas le cas, vous y arriverez éventuellement ! Alors, comprenons comment Tina doit gérer cette situation efficacement.

## Comment Résoudre les Conflits de Fusion dans Git

Résoudre les conflits de fusion n'est pas aussi compliqué que cela peut paraître. Dans 90% des cas, c'est plus facile une fois que vous avez une compréhension claire des changements et un esprit paisible.

### Processus de Réflexion

Une fois que Tina a tiré les changements, le fichier local de Tina contient ses changements plus ceux d'Alex. Maintenant, Tina peut faire l'une de ces quatre choses :

* Elle peut garder les changements d'Alex et supprimer les siens.
* Elle peut supprimer les changements d'Alex et garder les siens.
* Elle peut garder à la fois les changements d'Alex et les siens.
* Elle peut supprimer à la fois les changements d'Alex et les siens.

D'accord, mais laquelle devrait-elle faire ? Cela dépend entièrement des besoins du projet et des cas d'utilisation. Tina comprendra les changements `entrants` et fera ce qui est pertinent pour la situation.

Alors, quels sont les changements `entrants` ? Comment Tina va-t-elle les identifier ? Comment Tina apporte-t-elle les changements ? Je sais que vous avez beaucoup de questions comme celles-ci. Obtenons les réponses à toutes ces questions en prenant quelques exemples concrets dans la section ci-dessous.

## Étapes pour Résoudre les Conflits de Fusion dans Git

Prenons quelques exemples concrets de conflits de fusion, et apprenons à les résoudre. 

À tout moment, si vous souhaitez apprendre ces concepts de manière interactive, veuillez consulter [cette section de la vidéo](https://www.youtube.com/watch?v=OulZeVtZhZQ&t=397s) que j'ai mentionnée au début de cet article.

### Exemple 1 : Les Changements sont dans la Même Région du Fichier

Lorsque Git ne peut pas effectuer une fusion automatique parce que les changements sont dans la même région, il indique les régions en conflit avec des caractères spéciaux. Les séquences de caractères sont comme suit :

* `<<<<<<<`
* `=======`
* `>>>>>>>`

Tout ce qui se trouve entre `<<<<<<<` et `=======` sont vos changements locaux. Ces changements ne sont pas encore dans le dépôt distant. Toutes les lignes entre `=======` et `>>>>>>>` sont les changements du dépôt distant ou d'une autre branche. Maintenant, vous devez examiner ces deux sections et prendre une décision.

L'image ci-dessous montre le contenu d'un fichier indiquant que la fusion automatique n'a pas eu lieu et qu'il y a un conflit. Le conflit se situe à la ligne où nous avons modifié le fichier localement en ajoutant une ligne `- Sleep`. Mais entre-temps, quelqu'un d'autre a poussé un changement en ajoutant la ligne `- Gym` dans la même région.

Ainsi, la ligne `- Sleep` est marquée comme le changement local et `- Gym` comme les changements entrants du dépôt distant ou d'une autre branche.

![Image](https://www.freecodecamp.org/news/content/images/2022/05/merge-conflict.jpg)
_Conflit de Fusion dû aux Changements dans la Même Région_

En fonction de votre cas d'utilisation et des besoins du projet, vous prendrez la décision de résoudre le conflit. Si vous devez garder uniquement la ligne avec `- Sleep`, vous la garderez et supprimerez le reste des textes en conflit. Dans ce cas, le contenu du fichier devient :

```bash
- Eat
- Read
- Sleep
```

Au contraire, vous pouvez garder la ligne `- Gym` et supprimer les changements `- Sleep` :

```bash
- Eat
- Read
- Gym
```

Si vous devez garder les deux lignes, supprimez les lignes liées aux indicateurs de conflit :

```bash
- Eat
- Read
- Sleep
- Gym
```

Si vous pensez qu'aucun des changements n'est requis, supprimez-les tous.

```bash
- Eat
- Read
```

C'est entièrement à vous de décider quels changements sont pertinents pour la situation. Après vos changements, vous devez vous assurer qu'aucun des caractères indiquant un conflit n'existe (<<<<<<<,  =======, >>>>>>>) dans le fichier. Une fois que vous avez décidé des changements, faites ce qui suit :

Mettez en attente les changements :

```bash
git add <files>
```

Validez les changements avec un message :

```bash
git commit -m "Message"
```

Enfin, poussez les changements vers le dépôt distant :

```bash
git push
```

C'est tout ce qu'il y a à faire pour résoudre le conflit de fusion dans ce scénario.

### Exemple 2 : Le Fichier est Supprimé dans le Dépôt Distant/Autre Branche

Dans les conflits de fusion de fichier supprimé, un développeur supprime un fichier dans une branche tandis qu'un autre développeur modifie le même fichier dans une autre branche. Dans ce cas, vous devez décider si vous souhaitez garder le fichier ou s'il était juste de le supprimer.

Pour ajouter le fichier supprimé à votre branche, faites ceci :

```bash
git add <file-name>
```

Pour procéder à la suppression du fichier, faites ceci :

```bash
git rm <file-name>
```

Ensuite, validez vos changements avec un message :

```bash
git commit -m "Message"
```

Enfin, poussez-le :

```bash
git push
```

## Qu'est-ce qui suit ?

Si vous apprenez des deux exemples ci-dessus et que vous les pratiquez, vous serez en mesure de gérer la plupart des scénarios et de résoudre vos conflits de fusion. Donc, je recommande de les pratiquer quelques fois.

Si vous rencontrez de nouveaux scénarios ou si vous êtes bloqué dans la résolution d'un conflit de fusion, n'hésitez pas à poster un commentaire à ce sujet dans la [section des commentaires de cette vidéo](https://www.youtube.com/watch?v=OulZeVtZhZQ). Je ferai de mon mieux pour répondre !

Avant de conclure, quelques conseils pour vous :

* Tous les exemples présentés dans cet article supposent que vous utilisez GitBash ou un autre CLI Git pour résoudre les conflits de fusion. Vous pouvez utiliser n'importe quel autre outil GUI pour faire de même.
* Toujours tirer du dépôt distant/autres branches connexes avant de commencer un nouveau travail logique sur votre code. Cela gardera votre branche à jour autant que possible et réduira les chances de conflits.
* Toujours tirer avant une poussée pour vous assurer que vous ne rencontrerez aucun rejet de Git.
* Parlez à vos pairs/codéveloppeurs lorsque vous ne pouvez pas décider quoi garder par rapport à quoi supprimer. Associez-vous pour résoudre tout conflit de fusion difficile.

C'est tout pour l'instant. J'espère que vous avez trouvé cet article informatif et perspicace pour vous aider avec les conflits de fusion dans Git.

Restez en contact.

* Donnez un [Follow sur Twitter](https://twitter.com/tapasadhikary) si vous ne voulez pas manquer la dose quotidienne de conseils sur le développement web et la programmation.
* Consultez mes projets open source sur [GitHub](https://github.com/atapas).
* Vous pouvez [VOUS ABONNER](https://www.youtube.com/tapasadhikary?sub_confirmation=1) à ma chaîne YouTube si vous souhaitez apprendre JavaScript, ReactJS, Node.js, Git et tout sur le développement web de manière pratique.

À bientôt avec mon prochain article. En attendant, prenez soin de vous et restez heureux.