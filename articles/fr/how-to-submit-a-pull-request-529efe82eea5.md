---
title: Comment soumettre une pull request
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-11-08T04:52:17.000Z'
originalURL: https://freecodecamp.org/news/how-to-submit-a-pull-request-529efe82eea5
coverImage: https://cdn-media-1.freecodecamp.org/images/0*dpIaMx00--Gq9hde.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment soumettre une pull request
seo_desc: 'Let’s say you wrote some code on the develop branch. You’re done with what
  you were working on, and you want to merge it into the master branch.

  But you don’t know whether the code you’ve written is good enough. You want someone
  to review your code b...'
---

Disons que vous avez écrit du code sur la branche `develop`. Vous avez terminé ce sur quoi vous travailliez, et vous souhaitez le fusionner dans la branche `master`.

Mais vous ne savez pas si le code que vous avez écrit est suffisamment bon. Vous voulez que quelqu'un révise votre code avant de le fusionner dans la branche master.

Vous pouvez faire cela avec une pull request.

### Qu'est-ce qu'une pull request ?

Une pull request est l'abréviation de « request for a Git Pull ».

Cela peut être confus à comprendre, alors nous allons l'expliquer avec une analogie.

Imaginez que vous avez une caisse de bananes que vous voulez charger sur un navire. La seule façon de charger les bananes est :

1. Vous faites en sorte que quelqu'un vous lance une corde
2. Vous attachez la corde à la caisse
3. Ils tirent la caisse vers le haut

Quand ils tirent la caisse vers le haut, ils voudront vérifier si vos bananes sont bonnes. S'ils repèrent une banane pourrie, ils pourraient vous demander de remplacer cette banane pourrie par une bonne.

Ils pourraient aussi penser que toutes vos bananes sont mauvaises et décider de les jeter. (Mais espérons que cela n'arrive pas, n'est-ce pas ?)

Dans cette analogie, la caisse de bananes est votre code de la branche develop. Le navire est la branche master. Le marin est là pour vérifier si votre code est suffisamment bon pour la branche master.

**C'est ce qu'est une pull request : vous faites en sorte que quelqu'un vérifie votre code avant de le fusionner dans une autre branche.**

La seule différence entre notre analogie et une vraie pull request est : vous ne demandez pas à quelqu'un de vous lancer une corde. Vous apportez la corde vous-même, vous l'attachez à vos bananes au port, et vous la lancez sur le navire. La seule chose que le marin doit faire est de vérifier les bananes.

C'est ce que nous entendons par soumettre une pull request.

Il existe deux façons de soumettre une pull request. La façon dont vous le faites dépend de si vous avez un accès en écriture au dépôt.

Avant de soumettre une pull request, nous devons apporter quelques modifications, afin d'avoir quelque chose à fusionner. Dans ce cas, nous allons ajouter un en-tête au code :

```
<!-- Le code que nous utilisons pour soumettre la pull request --> <h2>Je suis un en-tête</h2>
```

Vous devez commiter ce code dans la branche develop. Ensuite, vous devez le pousser vers le dépôt distant git.

Il apparaîtra dans la section que j'ai mise en évidence dans l'image ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dpIaMx00--Gq9hde.png)

Si vous voyez le message, c'est bien. Cliquez dessus. Vous économiserez quelques étapes.

Si vous ne le voyez pas, vous pouvez cliquer sur l'onglet pull request en haut de votre dépôt Github.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Pkg8pBcBj8GZEGZv.png)

Ensuite, cliquez sur le bouton vert qui dit « new pull request ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*s-7kajV7028oZyMS.png)

Vous arriverez à une page qui dit « Compare changes ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*JLiYZw4G99Cz2gLC.png)

Pour créer une pull request, vous voulez définir les branches de base et de comparaison comme suit :

* `base` : branche dans laquelle vous voulez fusionner
* `compare` : branche à partir de laquelle vous voulez fusionner

Dans notre cas, nous voulons fusionner dans master, donc nous définissons `base` à `master`. Nous fusionnons à partir de `develop`, donc nous définissons `compare` à `develop`.

Une fois que vous avez sélectionné vos branches, Github vous montrera la liste des commits qui ont été faits. Ici, ce que vous devez faire est de cliquer sur le bouton « Create pull request ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*usMPzWvpQ4CGwAAU.png)

Github vous montrera une page qui dit « Open a pull request ».

Note : C'est la page à laquelle vous arriverez si vous avez vu le message « Your branch has been updated X minutes ago » dont j'ai parlé plus tôt.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DZklVY-15f7sbKTb.png)

Le titre que vous écrivez sera le titre que les gens verront dans l'onglet pull request. Nous allons le définir à « Add a heading to the index ».

Pour les commentaires, ce sera le premier message que les gens verront lorsqu'ils cliqueront sur la pull request. Dans ce cas, nous dirons « J'ai ajouté un en-tête. Faites-moi savoir si c'est bien ? »

![Image](https://cdn-media-1.freecodecamp.org/images/0*oKIqsx17DQlebWXL.png)

Une fois que vous avez ajouté le titre et le message, vous pouvez cliquer sur le bouton Create pull request en bas de la page.

Maintenant, si vous cliquez sur l'onglet pull request en haut, vous verrez une pull request ouverte que nous venons de soumettre.

![Image](https://cdn-media-1.freecodecamp.org/images/0*G26L9dxWOZMIHYcd.png)

C'est ainsi que vous créez une pull request si vous avez un accès en écriture au dépôt.

Si vous n'avez pas d'accès en écriture à un dépôt, vous devrez créer un Fork. Faisons une pause et parlons de ce qu'est un Fork.

### Qu'est-ce qu'un Fork ?

Un Fork N'EST PAS le client git que vous utilisez. Ne vous trompez pas !

**Un fork dans Git signifie un dépôt qui est basé sur un autre dépôt.**

Vous avez déjà appris sur les branches jusqu'à présent, et vous savez qu'une branche peut être créée à partir d'une autre branche. (Créer une branche `develop` à partir de `master`, par exemple).

Sur la même note, un dépôt peut être créé à partir d'un autre dépôt. Le dépôt qui a été créé à partir d'un autre dépôt est appelé un fork.

Le dépôt forké contient tout ce que le dépôt principal a (au moment où il a été forké). Il inclut toutes les tags et branches.

Vous possédez le dépôt forké (ce qui vous donne un accès en écriture). Ce dépôt forké sera toujours suivi par le dépôt principal. Vous allez faire une pull request via ce lien suivi.

Voyons comment cela fonctionne en pratique.

Note : Vous ne pouvez pas forker votre propre dépôt. Ce que je vais faire est d'utiliser un compte factice pour vous montrer comment cela fonctionne. À partir de ce point, notez ces deux noms de compte :

1. Compte principal : `zellwk`
2. Compte factice : `zellwk2`.

(J'aurais dû créer un nom totalement différent... mais je pense que vous pourrez suivre sans problème).

Pour forker un dépôt, vous cliquez sur le bouton fork qui se trouve dans le coin supérieur droit du dépôt.

![Image](https://cdn-media-1.freecodecamp.org/images/0*PqfVRNirQBswK02X.png)

Une fois le fork terminé, vous verrez un dépôt qui ressemble (presque) exactement au dépôt à partir duquel vous avez forké. Il y a une différence cependant — si vous regardez le titre du projet, vous pouvez voir que le projet est forké à partir d'un autre dépôt.

Vous avez un accès en écriture à ce dépôt forké.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3qg_cY-Xu_I34rJt.png)

Voici ce que nous faisons lorsque nous soumettons une pull request à partir d'un dépôt forké :

1. Créer une nouvelle branche
2. Écrire du code dans cette nouvelle branche
3. Envoyer une pull request à partir de cette nouvelle branche

Mais pour cette leçon, je ne vais pas créer la nouvelle branche car je devrais configurer le compte factice sur mon client Git (ce qui est un processus fastidieux).

Donc, pour cette leçon, nous allons écrire directement dans la branche `develop`. Ensuite, nous soumettrons une pull request à partir de la branche `develop`.

Dans ce cas, j'ajoute une liste avec le HTML suivant dans le fichier `index.html` :

```
<ul>  <li>Item 1</li>   <li>Item 2</li>   <li>Item 3</li>
```

Note : J'ai laissé la balise `<ul>` ouverte dans cet exemple. Nous reprendrons cette erreur lorsque nous examinerons cette pull request dans la prochaine leçon.

Le message de commit pour ces modifications est : `Add list`.

Maintenant, si vous retournez à votre dépôt forké, vous devriez voir un bouton appelé « new pull request ». Ce bouton se trouve à côté du bouton qui vous permet de changer de branche.

![Image](https://cdn-media-1.freecodecamp.org/images/0*zdEIiex6u5Fg4Ztc.png)

Cliquez sur ce bouton new pull request pour créer une pull request.

Github vous amènera à une page qui dit « Open a new pull request ». Cette page ressemble à la page « Open a new pull request » que vous avez vue ci-dessus.

La différence est que vous devez définir quatre choses :

1. Le fork de base
2. La branche de base
3. Le fork head
4. La branche de comparaison

![Image](https://cdn-media-1.freecodecamp.org/images/0*rlg55BYiA5zjPEOB.png)

D'après l'exemple ci-dessus, nous savons deux choses :

1. La branche `base` est la branche dans laquelle vous voulez fusionner
2. La branche `compare` est la branche à partir de laquelle vous voulez fusionner

Cela signifie que nous devons définir ce qui suit :

1. Le fork de base : `zellwk/project`
2. La branche de base : `master`
3. Le fork head : `zellwk2/project`
4. La branche de comparaison : `develop`

Ce que vous devez faire ensuite est d'écrire le titre de la pull request, d'écrire le commentaire, et de cliquer sur le bouton New Pull Request.

![Image](https://cdn-media-1.freecodecamp.org/images/0*FM4gRYAr7KFDM-Q8.png)

Et vous avez soumis une pull request à partir d'un dépôt forké.

![Image](https://cdn-media-1.freecodecamp.org/images/0*igd7AvgrfoCwEDlA.png)

### Conclusion

Lorsque vous soumettez une pull request, vous demandez à quelqu'un de réviser vos modifications avant de les fusionner dans une branche.

Il existe deux façons de créer une pull request. La façon dont vous le faites dépend de si vous avez un accès en écriture au dépôt.

Si vous avez un accès en écriture, vous pouvez créer une pull request à partir de la page du dépôt.

Si vous n'avez pas d'accès en écriture, vous devez forker le dépôt vers votre propre page. Ensuite, vous créez une pull request à partir de votre dépôt forké.

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=How%20to%20submit%20a%20pull%20request%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/submit-pull-request/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [_mon blog_](https://zellwk.com/blog/submit-pull-request)_._  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.