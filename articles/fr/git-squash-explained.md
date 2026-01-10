---
title: Git Squash Expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-26T18:07:00.000Z'
originalURL: https://freecodecamp.org/news/git-squash-explained
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d82740569d1a4ca3827.jpg
tags:
- name: Git
  slug: git
- name: toothbrush
  slug: toothbrush
seo_title: Git Squash Expliqué
seo_desc: 'What is Git Squash?

  One of the things that developers hear quite often regarding their pull requests
  is something like “That looks good to me, please squash and merge”. The fun part
  is that there is no such command like git squash (unless you create ...'
---

## **Qu'est-ce que Git Squash ?**

L'une des choses que les développeurs entendent assez souvent concernant leurs pull requests est quelque chose comme « Cela me semble bien, veuillez squasher et merger ». Le côté amusant, c'est qu'il n'existe pas de commande comme `git squash` (sauf si vous créez un [alias](https://guide.freecodecamp.org/git/git-rebase) pour cela).

`Squasher` une pull request signifie généralement compacter tous les commits de cette demande en un seul (rarement en un autre nombre) pour la rendre plus concise, lisible et ne pas polluer l'historique de la branche principale. Pour y parvenir, un développeur doit utiliser le **mode interactif** de la commande [Git Rebase](https://guide.freecodecamp.org/git/git-rebase).

Très souvent, lorsque vous développez une nouvelle fonctionnalité, vous vous retrouvez avec plusieurs commits intermédiaires dans votre historique - vous développez de manière incrémentielle après tout. Cela peut être simplement des fautes de frappe ou des étapes vers la solution finale. La plupart du temps, il n'est pas utile d'avoir tous ces commits dans la version finale publique de votre code, il est donc plus bénéfique de les compacter en une seule version finale.

Supposons donc que vous avez le journal de commits suivant dans la branche que vous souhaitez merger dans le cadre d'une pull request :

```shell
$ git log --pretty=oneline --abbrev-commit
30374054 Ajout du stub Jupyter Notebook aux outils de Data Science
8490f5fc Modifications mineures de formatage et de ponctuation
3233cb21 Prototype de la page Notebook
```

Clairement, nous préférerions n'avoir qu'un seul commit ici, car il n'y a aucun avantage à savoir ce que nous avons commencé à écrire et quelles fautes de frappe nous avons corrigées plus tard. Seul le résultat final est important.

Ce que nous faisons donc, c'est démarrer une session de rebase interactive à partir du **HEAD** actuel (commit **30374054**) jusqu'au commit **3233cb21**, avec l'intention de combiner les **3** derniers commits en un seul :

```shell
$ git rebase -i HEAD~3
```

Cela ouvrira un éditeur avec quelque chose comme ce qui suit :

```shell
pick 3233cb21 Prototype de la page Notebook
pick 8490f5fc Modifications mineures de formatage et de ponctuation
pick 30374054 Ajout de Jupyter Notebook aux outils de Data Science
# Rebase
#
# Commandes :
#  p, pick = utiliser le commit
#  r, reword = utiliser le commit, mais éditer le message du commit
#  e, edit = utiliser le commit, mais s'arrêter pour modifier
#  s, squash = utiliser le commit, mais fusionner dans le commit précédent
#  f, fixup = comme "squash", mais ignorer le message de log de ce commit
#  x, exec = exécuter la commande (le reste de la ligne) en utilisant le shell
#
# Ces lignes peuvent être réorganisées ; elles sont exécutées de haut en bas.
#
# Si vous supprimez une ligne ici, CE COMMIT SERA PERDU.
#
# Cependant, si vous supprimez tout, le rebase sera annulé.
#
# Notez que les commits vides sont commentés
```

Comme toujours, Git nous donne un message d'aide très utile où vous pouvez voir l'option `squash` que nous recherchons.

Actuellement, les instructions pour le rebase interactif disent de `pick` chaque commit spécifié **et** de préserver le message de commit correspondant. C'est-à-dire - ne changez rien. Mais nous voulons n'avoir qu'un seul commit à la fin.

Vous pouvez donc simplement éditer le texte dans votre éditeur en remplaçant `pick` par `squash` (ou simplement `s`) à côté de chaque commit dont nous voulons nous débarrasser, puis sauvegarder/quitter l'éditeur. Cela pourrait ressembler à ceci :

```shell
s 3233cb21 Prototype de la page Notebook
s 8490f5fc Modifications mineures de formatage et de ponctuation
pick 30374054 Ajout de Jupyter Notebook aux outils de Data Science
```

Lorsque vous fermez votre éditeur après avoir sauvegardé cette modification, il sera rouvert immédiatement et vous suggérera de choisir et de reformuler ces messages de commit. Quelque chose comme ceci :

```shell
# Il s'agit d'une combinaison de 3 commits.
# Le message du premier commit est :
Prototype de la page Notebook

# Il s'agit du message du 2ème commit :

Modifications mineures de formatage et de ponctuation

# Il s'agit du message du 3ème commit :

Ajout de Jupyter Notebook aux outils de Data Science

# Veuillez entrer le message de commit pour vos modifications. Les lignes commençant
# par '#' seront ignorées, et un message vide annule le commit.
```

À ce stade, vous pouvez supprimer tous les messages que vous ne souhaitez pas inclure dans la version finale du commit. Vous pouvez également les reformuler ou simplement écrire un message de commit à partir de zéro.

Rappelez-vous simplement que la nouvelle version inclura toutes les lignes qui ne commencent pas par le caractère `#`. Sauvegardez et quittez à nouveau votre éditeur.

Votre terminal devrait maintenant afficher un message de succès incluant `Successfully rebased and updated <branch name>` et le journal git devrait montrer un historique propre et compacté avec un seul commit. Tous les commits intermédiaires ont disparu et nous sommes prêts à merger !

### **Avertissement concernant la divergence entre l'historique local et distant**

Cette opération est légèrement dangereuse si vous avez déjà publié votre branche dans un dépôt distant - vous modifiez l'historique des commits après tout. Il est donc préférable d'effectuer l'opération de squash sur une branche locale avant de faire un **push**.

Parfois, elle aura déjà été poussée - comment créeriez-vous une pull request sinon ? Dans ce cas, vous devrez **forcer** les modifications sur la branche distante après avoir effectué le squash, car votre historique local et l'historique de la branche dans le dépôt distant sont différents :

```shell
$ git push origin +my-branch-name
```

Faites de votre mieux pour vous assurer que vous êtes le seul à utiliser cette branche distante à ce moment-là, ou vous rendrez la vie des autres développeurs plus difficile lorsqu'ils auront une divergence d'historique. Mais comme le **squash** est généralement effectué en tant qu'opération finale sur une branche avant de s'en débarrasser, ce n'est généralement pas une si grande préoccupation.