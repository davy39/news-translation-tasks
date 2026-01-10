---
title: Comment comprendre et résoudre les conflits dans Git
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-24T18:55:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-merge-conflicts-in-git
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/header-image@1000x420.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment comprendre et résoudre les conflits dans Git
seo_desc: 'By Tobias Günther

  There it is, the word that every developer hates to see: conflict. 😱 There''s just
  no way around the occasional merge conflict when working with Git (or other version
  control systems).

  But when speaking with developers, I often hear...'
---

Par Tobias Günther

Le voici, le mot que tous les développeurs détestent voir : **conflit.** 😱 Il n'y a tout simplement pas moyen d'éviter les conflits de fusion occasionnels lors de l'utilisation de Git (ou d'autres systèmes de contrôle de version).

Mais en parlant avec des développeurs, j'entends souvent qu'il y a un sentiment d'_anxiété_ ou de _malaise_ autour du sujet des conflits de fusion.

La gestion des conflits reste souvent un domaine obscur et mystérieux : une situation où les choses sont gravement endommagées et où il n'est pas clair comment s'en sortir (sans empirer les choses).

Bien qu'il soit vrai que les conflits de fusion soient une partie inévitable de la vie d'un développeur, le malaise dans ces situations est entièrement optionnel.

Mon intention avec cet article est d'apporter un peu de clarté à ce sujet : comment et quand les conflits se produisent généralement, ce qu'ils sont réellement, et comment les résoudre - ou les annuler.

Lorsque vous comprendrez correctement ces choses, vous serez en mesure de gérer les conflits de fusion de manière beaucoup plus détendue et confiante. 😊

## Comment et quand les conflits se produisent

Le nom le dit déjà : les "conflits de fusion" peuvent se produire lors du processus d'intégration de commits provenant d'une source différente.

Gardez à l'esprit, cependant, que "l'intégration" n'est pas limitée à la seule "fusion de branches". Cela peut également se produire lors d'un rebase ou d'un rebase interactif, lors de l'exécution d'un cherry-pick ou d'un pull, ou même lors de la réapplication d'un Stash.

Toutes ces actions effectuent une sorte d'intégration - et c'est à ce moment-là que les conflits de fusion peuvent se produire.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/situations-where-conflicts-can-happen-1.png)

Mais bien sûr, ces actions ne entraînent pas un conflit de fusion _à chaque fois_ (Dieu merci !). Idéalement, vous ne devriez vous retrouver dans ces situations que rarement. _Mais quand exactement les conflits se produisent-ils ?_

En fait, les capacités de fusion de Git sont l'un de ses plus grands avantages : la fusion de branches fonctionne sans effort la plupart du temps, car Git est généralement capable de comprendre les choses par lui-même.

Mais il existe des situations où des **changements contradictoires** ont été apportés - et où la technologie ne peut tout simplement pas décider ce qui est juste ou faux. Ces situations nécessitent simplement une décision d'un être humain.

Le vrai classique est lorsque la _même ligne de code exacte_ a été modifiée dans deux commits, sur deux branches différentes. Git n'a aucun moyen de savoir quel changement vous préférez ! 🤔

Il existe d'autres situations similaires - par exemple, lorsqu'un fichier a été _modifié_ dans une branche et _supprimé_ dans une autre - mais elles sont un peu moins courantes.

Le [**"Tower" Git desktop GUI**](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), par exemple, propose une belle façon de visualiser ces types de situations :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tower-conflict-wizard-1.png)

## Comment savoir quand un conflit s'est produit

Ne vous inquiétez pas : Git vous indiquera très clairement quand un conflit s'est produit. 😉

Tout d'abord, il vous le fera savoir _immédiatement dans la situation_, par exemple lorsqu'une fusion ou un rebase échoue en raison d'un conflit :

```git on cli
$ git merge develop
Auto-merging index.html
CONFLICT (content): Merge conflict in index.html
CONFLICT (modify/delete): error.html deleted in HEAD and modified in develop. Version develop of error.html left in tree.
Automatic merge failed; fix conflicts and then commit the result.
```

Comme vous pouvez le voir dans l'exemple ci-dessus, lorsque j'ai essayé d'effectuer une fusion, j'ai créé un conflit de fusion - et Git communique le problème très clairement et rapidement :

* Un conflit dans le fichier "index.html" s'est produit.
* Un autre conflit dans le fichier "error.html" s'est produit.
* Et enfin, en raison des conflits, l'opération de fusion a échoué.

Ce sont les situations où nous devons creuser dans le code et voir ce qui doit être fait.

Dans l'éventualité peu probable où vous auriez négligé ces messages d'avertissement lorsque le conflit s'est produit, Git vous informe également chaque fois que vous exécutez `git status` :

```git on cli
$ git status
On branch main
You have unmerged paths.
  (fix conflicts and run "git commit")
  (use "git merge --abort" to abort the merge)

Unmerged paths:
  (use "git add/rm <file>..." as appropriate to mark resolution)
	deleted by us:   error.html
	both modified:   index.html
```

En d'autres termes : ne vous inquiétez pas de _ne pas remarquer_ les conflits de fusion. Git s'assure que vous ne pouvez pas les ignorer.

## Comment annuler un conflit dans Git et recommencer

Les conflits de fusion s'accompagnent d'un certain sentiment d'urgence. Et à juste titre : vous devrez les gérer avant de pouvoir continuer votre travail.

Mais bien qu'il ne soit pas possible de les ignorer, "gérer les conflits de fusion" ne signifie pas nécessairement que vous devez les résoudre. **Les annuler** est également possible !

Cela mérite peut-être d'être répété : **vous avez toujours la possibilité d'annuler un conflit de fusion et de revenir à l'état précédent.** Cela est vrai même lorsque vous avez déjà commencé à résoudre les fichiers en conflit et que vous vous trouvez dans une impasse.

Dans ces situations, il est bon de garder à l'esprit que vous pouvez toujours recommencer et revenir à un état propre avant même que le conflit ne se produise.

À cette fin, la plupart des commandes disposent d'une option `--abort`, par exemple `git merge --abort` et `git rebase --abort` :

```git on cli
$ git merge --abort
$ git status
On branch main
nothing to commit, working tree clean
```

Cela devrait vous donner la confiance que **vous ne pouvez vraiment rien gâcher.** Vous pouvez toujours annuler, revenir à un état propre et recommencer.

## À quoi ressemblent vraiment les conflits dans Git

Maintenant, en toute sécurité, sachant que rien ne peut se casser, voyons à quoi ressemble _réellement_ un conflit sous le capot. Cela démystifiera ces petits problèmes et, en même temps, vous aidera à perdre le respect pour eux et à gagner confiance en vous.

Par exemple, regardons le contenu du fichier "index.html" (actuellement en conflit) dans un éditeur :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/contents-of-conflicted-file-1.png)

Git a eu la gentillesse de marquer la zone problématique dans le fichier, en l'enfermant dans `<<<<<<< HEAD` et `>>>>>>> [other/branch/name]`. Le contenu qui suit le premier marqueur provient de notre branche de travail actuelle. Enfin, une ligne avec des caractères `=======` sépare les deux changements contradictoires.

## Comment résoudre un conflit dans Git

Notre travail en tant que développeurs consiste maintenant à nettoyer ces lignes : après avoir terminé, le fichier doit avoir exactement l'apparence que nous souhaitons.

Il peut être nécessaire de parler au collègue qui a écrit les changements "autres" et de décider quel code est réellement correct. Peut-être que c'est le nôtre, peut-être que c'est le leur - ou peut-être un mélange des deux.

Ce processus - nettoyer le fichier et s'assurer qu'il contient ce que nous voulons réellement - n'a pas besoin d'impliquer de magie. Vous pouvez faire cela simplement en ouvrant votre éditeur de texte ou IDE et en commençant à faire vos modifications.

Souvent, cependant, vous constaterez que ce n'est pas la méthode la plus efficace. C'est là que des outils dédiés peuvent faire gagner du temps et des efforts :

* **Outils GUI pour Git :** Certaines des interfaces graphiques pour Git peuvent être utiles pour résoudre les conflits. Le [**Tower Git GUI**](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), par exemple, offre un "Assistant de Conflit" dédié qui aide à visualiser et à résoudre la situation :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/tower-conflict-wizard-in-action-1.gif)

* **Outils de Fusion Dédiés :** Pour des conflits plus compliqués, il peut être utile d'avoir un outil "Diff & Merge" dédié à portée de main. Vous pouvez configurer votre outil de choix en utilisant la commande "git config". (Consultez la documentation de votre outil pour des instructions détaillées.) Ensuite, en cas de conflit, vous pouvez l'invoquer en tapant simplement `git mergetool`. Voici, par exemple, une capture d'écran de "[**Kaleidoscope**](https://www.kaleidoscopeapp.com)" sur macOS :

![Image](https://www.freecodecamp.org/news/content/images/2020/11/merge-conflict-in-gui-1.jpg)

Après avoir nettoyé le fichier - manuellement ou dans un GUI Git ou un outil de fusion - nous devons valider cela comme tout autre changement :

* En utilisant `git add <filename>` sur le fichier (précédemment) en conflit, nous informons Git que le conflit a été résolu.
* Lorsque tous les conflits ont été résolus et ajoutés à la zone de staging, vous devez finaliser la résolution en créant un commit régulier.

## Comment devenir plus confiant et productif

Il y a de nombreuses années, lorsque j'ai commencé à utiliser le contrôle de version, les conflits de fusion me faisaient régulièrement paniquer : j'avais peur d'avoir enfin réussi à tout casser pour de bon. 😩

Ce n'est que lorsque j'ai pris le temps de vraiment comprendre ce qui se passait sous le capot que j'ai pu gérer les conflits avec confiance et efficacité.

La même chose était vraie, par exemple, lorsque je traitais des erreurs : ce n'est qu'une fois que j'ai appris **comment annuler les erreurs avec Git** que j'ai pu devenir plus confiant et productif dans mon travail.

Je vous recommande vivement de jeter un œil au "[**First Aid Kit for Git**](https://www.git-tower.com/learn/git/first-aid-kit?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts)", une collection de courtes vidéos sur la façon d'annuler et de se remettre des erreurs avec Git.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/first-aid-kit-3.png)

Amusez-vous à devenir un meilleur programmeur !

## À propos de l'auteur

[Tobias Günther](https://twitter.com/gntr) est le PDG de [Tower](https://www.git-tower.com/?utm_source=freecodecamp&utm_medium=guestpost&utm_campaign=understand-and-solve-conflicts), le client Git de bureau populaire qui aide plus de 100 000 développeurs à travers le monde à être plus productifs avec Git.