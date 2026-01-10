---
title: Un guide Git simple et un aide-mémoire pour les contributeurs open source
subtitle: ''
author: Saheed Oladele
co_authors: []
series: null
date: '2019-07-12T17:18:51.000Z'
originalURL: https://freecodecamp.org/news/a-simple-git-guide-and-cheat-sheet-for-open-source-contributors
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca17a740569d1a4ca4ed1.jpg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: GitLab
  slug: gitlab
- name: open source
  slug: open-source
seo_title: Un guide Git simple et un aide-mémoire pour les contributeurs open source
seo_desc: 'A go-to git cheat sheet for your open source contributions.

  If you’re reading this article, you already know that the benefit of open source
  contribution abounds. You can skip the article and navigate to the end if you’re
  here for the cheat sheet.

  Th...'
---

Un aide-mémoire Git incontournable pour vos contributions open source.

Si vous lisez cet article, vous savez déjà que les avantages de la contribution open source sont nombreux. Vous pouvez sauter l'article et passer directement à la fin si vous êtes ici pour l'aide-mémoire.

Le problème courant auquel sont confrontés les aspirants contributeurs open source est de savoir comment faire le premier pas, _du fork à la pull request_. Après avoir lu cet article, vous serez bien équipé avec tout ce dont vous avez besoin pour faire votre première pull request open source.

En plus de simplifier le processus pour vous, le flux de travail Git défini dans cet article rend également vos contributions plus professionnelles. Cela est particulièrement utile si vous souhaitez ajouter vos contributions open source à votre portfolio.

### Prérequis

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-240.png)
_Photo par [Unsplash](https://unsplash.com/@randyfath?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Randy Fath</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Cet article suppose que vous connaissez déjà les étapes à suivre pour contribuer à l'open source. Si ce n'est pas le cas, vous pouvez lire [cet article écrit par Maryna](https://rubygarage.org/blog/how-contribute-to-open-source-projects). Cet article suppose également que vous avez déjà configuré Git sur votre PC. Si ce n'est pas le cas, vous pouvez consulter la [section de configuration de Git de cet article](https://help.github.com/en/articles/set-up-git) et le faire d'abord.

### Étape 1 : Forker le projet

C'est aussi simple que de cliquer sur un bouton sur GitHub. Accédez au dépôt du projet auquel vous souhaitez contribuer, puis cliquez sur le bouton fork en haut à droite comme illustré dans l'image ci-dessous.

![Image](https://lh4.googleusercontent.com/4u1uvX1dRTkG0RLXeWqt6N7-Ed2BeNiOfG8KgXsiOAE-quBpq2rDKS2d6dkxyEWbMThVJu4bgeqU9aKO-vhxyj5XULbRxpV0WedoctN0wm_RhgSyzg5ICn4aZUkk99BwBj2ugCBv)

Après avoir utilisé le bouton fork, vous aurez maintenant le dépôt sur votre compte GitHub.

### Étape 2 : Cloner le projet sur votre machine locale

C'est la partie la plus simple de Git. Accédez à votre dépôt forké (le dépôt est maintenant l'un de vos dépôts GitHub). Suivez les étapes 1 et 2 comme indiqué dans l'image ci-dessous pour copier l'adresse de clonage. Cette adresse devrait ressembler à ceci : `https:[github.com/suretrust.com/freeCodeCamp.git](http://github.com/suretrust.com/freeCodeCamp.git)`

![Image](https://lh5.googleusercontent.com/lyeLwQ6uz-VcEFoQcEGNf5KQiSzaDz1iwefGwi4CAoxuqiOdUPBm_jxVz1GJMgjHYHYkzGIHKb1l7iPdTQ5OIu3WUzK_ouFHHGAruNe-WJVKBsWpPgyLD5EClWnj7kaxsszwFqHB)

Ensuite, clonez le projet en tapant `git clone <l'adresse copiée>` dans votre terminal de commande comme indiqué ci-dessous :

`git clone [https://github.com/suretrust/freeCodeCamp.git](https://github.com/suretrust/freeCodeCamp.git)`

### Étape 3 : Créer un upstream

L'upstream est nécessaire pour suivre la différence entre le dépôt forké qui se trouve sur votre compte Git et le dépôt original. Cela est particulièrement utile si vous souhaitez contribuer à un dépôt populaire.

Certains dépôts fusionnent les pull requests toutes les heures ou moins, alors soyez prudent et supposez que le dépôt forké que vous avez sera en retard par rapport au dépôt original.

**Notez que l'upstream se trouve dans le dépôt freeCodeCamp et non dans votre dépôt forké.** Suivez les étapes 1 et 2 comme indiqué ci-dessous pour copier l'adresse de l'upstream :

![Image](https://lh6.googleusercontent.com/-fIOwK3jSHRJQrtVdCbGYc_0xFxPt-I22JmCqIom7f5F53iKceawsfju-NBw_wQ5LtRmsk9gJB3qJfA28ujR01lhF8VQKvvercoigfnVUbKNHrgOalp4OXz5CH6tXX46ev7d6Acv)

Pour créer un lien vers le dépôt original, copiez et collez la commande suivante dans votre terminal :

`git remote add upstream <adresse de l'upstream>`

Vous pouvez utiliser `git pull upstream master` pour confirmer s'il y a eu des changements depuis que vous avez forké le dépôt.

### Étape 4 : Créer la branche sur laquelle vous souhaitez travailler

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-241.png)
_Photo par [Unsplash](https://unsplash.com/@_zachreiner_?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Zach Reiner</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Il est bon de créer une nouvelle branche chaque fois que vous souhaitez contribuer. Cela illustre que la branche est uniquement pour cette contribution que vous êtes sur le point de faire. Cela peut être aussi simple que de corriger une faute de frappe ou aussi complexe que d'implémenter une nouvelle fonctionnalité. Dans tous les cas, c'est une bonne pratique de créer une branche.

Une autre partie importante de la création de la branche est le nommage. Il est agréable d'utiliser un nom qu'un inconnu qui ne connaît rien au dépôt peut facilement comprendre. Si vous souhaitez ajouter une fonctionnalité de connexion, par exemple, vous pourriez créer une branche appelée `add-login-feature` ou `login-feature`.

Pour créer une branche, tapez la commande suivante dans votre terminal :

`git checkout -b <nom de votre branche>`

Cette commande créera la branche et y naviguera. Si le nom de votre branche est login-feature, alors vous pouvez utiliser la commande suivante :

`git checkout -b login-feature`

_**Ensuite, ajoutez vos contributions. Après avoir ajouté votre contribution, passez à l'étape 5.**_

### Étape 5 : Ajouter et commiter vos contributions avec Git

C'est également assez simple. Indexez et commitez vos changements en tapant ce qui suit dans votre terminal.

`git add .`

`git commit -m 'Message de commit'`

Maintenant, vous avez les changements indexés et commités. Que faire ensuite ?

### Étape 6 : Pull depuis l'upstream vers la branche

Comme je l'ai expliqué à l'étape 4, cette étape consiste à fusionner toute différence dans l'upstream dans la branche afin de prévenir les conflits.

`git pull upstream <nom de la branche>`

Cela fusionne les changements de l'upstream dans votre branche actuelle.

### Étape 7 : Pousser vers la branche sur laquelle vous travaillez

Maintenant, vous y êtes presque. Poussez vos changements vers la branche sur laquelle vous travaillez comme indiqué ci-dessous :

`git push origin <nom-de-la-branche>`

### Étape 8 : Ouvrir une pull request

C'est l'étape finale pour toute contribution open source, vous dites simplement « J'ai fait quelques changements, cela vous dérangerait de les ajouter au projet ? ».

Vous ouvrez une pull request et si le propriétaire du dépôt ou les membres aiment ce qu'ils voient, ils le fusionneront. Sinon, ils pourraient faire des changements puis fusionner ou demander des changements.

Pour ouvrir une pull request, accédez au dépôt forké comme indiqué ci-dessous. Vous verrez votre dernière branche poussée `login-feature`, puis cliquez sur `compare and pull request`.

![Image](https://lh5.googleusercontent.com/GHcFpgR70pKrxpyhfNDnPRvVluSPF-gz2ICUKv1Q3uxZKEaBcwv32E8Rh7d-5yNS9uvGXWzCcoc22KBbddEOybzP7BkONlKdqXXmFtdcqIm6AU5ebZjAZeFV0iL7PMulwrnT8MnA)

Expliquez clairement les changements que vous avez apportés, puis ouvrez une pull request comme indiqué ci-dessous :

![Image](https://lh4.googleusercontent.com/4yGQB3_1-2IyGDiOAfNec1yyoMXyvEzUAEcShTx4xf8_DU5vgfhFN0Uihn0A-BZzKGJkeCnjDbQkXT_AKtTCsgAnXK6vDcIWuvWY5ETmUH4MORXT7kgz_4qKVnD2zj1bLcQRTWf1)

Et voilà. :) Vous pouvez maintenant contribuer comme un PRO !

## Aide-mémoire Git pour les contributeurs open source

![Image](https://lh5.googleusercontent.com/ZoVAty5u4vZaFdwBXh2fpsPQMsgW_3qxnt_dCo8Qn5ayk-fdvIZh6D6jSY_GdUhW8yUZvIIaBc_6WoLTyWseX3M8m7yPIzA8f4fL6X_oikH5wRcykopNH1KPI7eEuiz_8-M-jnZm)

Paix et bonnes contributions !