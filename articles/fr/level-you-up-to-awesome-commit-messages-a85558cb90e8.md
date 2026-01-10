---
title: Comment rendre vos messages de commit géniaux et garder votre équipe heureuse
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-08T23:22:17.000Z'
originalURL: https://freecodecamp.org/news/level-you-up-to-awesome-commit-messages-a85558cb90e8
coverImage: https://cdn-media-1.freecodecamp.org/images/1*D3L--z7Mx3-LqL9o6sbUgQ.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment rendre vos messages de commit géniaux et garder votre équipe heureuse
seo_desc: 'By Bruno

  Commit messages are important means of communication between team members


  What matters most in team software development is communication. Commit messages
  are important means of communication between team members: its past and its future.

  W...'
---

Par Bruno

#### Les messages de commit sont des moyens importants de communication entre les membres de l'équipe

![Image](https://cdn-media-1.freecodecamp.org/images/KTwUWqoJVaLxvcNiUMaOupwuWnCGoMkyODUR)

Ce qui compte le plus dans le développement logiciel en équipe, c'est la communication. Les messages de commit sont des moyens importants de communication entre les membres de l'équipe : son passé et son avenir.

Lors de l'analyse du code ou du débogage, nous avons tous des questions comme :

* Pourquoi ce _if_ est-il ici ?
* Qui a oublié de mettre à jour la branche ?
* Quel impact a eu ce changement ?
* Comment ce changement peut-il corriger ou améliorer le code ?

À cette fin, [git-blame](https://git-scm.com/docs/git-blame) nous permet de découvrir quelle révision a été la dernière à modifier le fichier. Mais savoir cela seulement n'est pas suffisant. Il serait utile de lire le message de commit pour comprendre ce qui s'est vraiment passé.

Nous devons lire le message pour ressentir la vraie valeur d'un bon message de commit, et être motivé à les écrire.

#### Quelques bonnes pratiques

Donc, si la majorité de vos commits Git jusqu'à présent ont été créés avec quelque chose comme `git commit -m "9000 — Bug fixes issue"`, alors la prochaine fois, essayez ce guide :

> Ne jamais utiliser le flag `-m <msg>` ou `--message=<msg>` avec git commit.

Cela vous donne une mauvaise mentalité dès le départ, car vous aurez l'impression de devoir adapter votre message de commit à la commande du terminal, et cela donne l'impression que le commit est plus un argument ponctuel qu'une page d'histoire.

> La première ligne doit toujours être [50 caractères ou moins](https://commit.style) et doit être suivie d'une ligne vide.

Écrivez à l'impératif : « Fix bug ». [_Add | Fix | Remove | Update | Refactor_] Une formulation cohérente facilite le traitement mental d'une liste de commits.

> Description plus longue enveloppée à 72 caractères.

Souvent, un sujet seul est suffisant. Lorsqu'il ne l'est pas, ajoutez une ligne vide (ceci est important) suivie d'un ou plusieurs paragraphes enveloppés à 72 caractères.

Ces paragraphes doivent expliquer :

**Pourquoi ce changement est-il nécessaire ?**

Cette réponse explique ce qu'il faut attendre dans le commit, permettant ainsi d'identifier et de pointer plus facilement les changements non liés.

**Comment cela résout-il le problème ?**

Décrivez, à un niveau élevé, ce qui a été fait pour affecter le changement. Si votre changement est évident, vous pouvez omettre de répondre à cette question.

**Quels sont les effets secondaires de ce changement ?**

C'est la question la plus importante à répondre, car elle peut pointer des problèmes où vous faites trop de changements dans un seul commit ou une seule branche. Un ou deux points pour les changements liés peuvent être acceptables, mais cinq ou six sont probablement des indicateurs d'un commit qui fait trop de choses.

```
# 50 caractères pour la ligne de sujet
# Description plus longue enveloppée à 72 caractères. Cela devrait répondre à :
# * Pourquoi ce changement était-il nécessaire ?
# * Comment cela résout-il le problème ?
# * Y a-t-il des effets secondaires ?
# Inclure un lien vers le ticket, le cas échéant.
```

#### Comment faciliter votre vie

C'est beaucoup à retenir, mais vous pouvez configurer un modèle de message de commit en utilisant `commit.template`

Configurez Git pour utiliser un fichier de modèle (par exemple, `.gitmessage`), puis créez le fichier de modèle avec Vim :

```
git config --global commit.template ~/.gitmessage
vim ~/.gitmessage
```

Lorsque nous exécutons `git commit` sans le flag de message `-m`, l'éditeur ouvrira notre modèle utile prêt à l'emploi :

```
# [Add/Fix/Remove/Update/Refactor/Document] [summary]
# Pourquoi est-ce nécessaire ? (Correction de bug, fonctionnalité, améliorations ?)
# Comment le changement résout-il le problème ?
# Quels sont les effets secondaires de ce changement ?
# Inclure un lien vers le ticket, le cas échéant.
```

Les lignes commentées ne sont pas incluses dans le message final. Il suffit de remplir les lignes vides avec du texte et des puces sous les invites.

Les suiveurs de problèmes dans GitHub et Bitbucket reconnaissent tous les deux les mots-clés `close`, `fix` et `resolve` suivis immédiatement du numéro de problème ou de la demande de tirage.

Je pense que Linus serait très heureux si nous n'utilisions plus jamais `git commit -m "Fix bug"` dans un dépôt public :)

Vous pouvez simplement rechercher dans le journal git un numéro de problème, par exemple, avec `git log --grep=JIRA-1234`

Vous pouvez également utiliser des plugins comme `vim-fugitive` pour _vim_ ou `git lens` pour _vs code_ pour accéder rapidement aux messages de commit git.

#### Réflexions finales

Créer des commits Git propres en dit long sur vous et peut être un moyen principal pour les gens d'interagir avec vous sur des projets.

Avec un peu de pratique, vous pouvez faire de vos habitudes de commit une meilleure réflexion de votre meilleur travail — un travail qui est clairement créé avec soin et fierté.

Votre futur vous, et votre équipe, vous remercieront pour votre prévoyance et votre verbosité lorsqu'ils exécuteront `git blame` pour voir pourquoi ce conditionnel est là.

*Si vous avez aimé cet article, applaudissez, recommandez et partagez.*