---
title: Comment utiliser Git stash comme stockage temporaire
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-10-22T20:38:50.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-stash-as-temporary-storage-84a0a1e37a43
coverImage: https://cdn-media-1.freecodecamp.org/images/0*5QOUGLobId0ruTih.png
tags:
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: version control
  slug: version-control
seo_title: Comment utiliser Git stash comme stockage temporaire
seo_desc: 'Let’s say you’re coding on your development branch. And you get a notice
  that there’s a bug in the production branch.

  You want to check for the bug, but you don’t want to lose the work you’ve created
  on the development branch. You also don’t want to ...'
---

Disons que vous codez sur votre branche de développement. Et vous recevez une notification qu'il y a un bug dans la branche de production.

Vous voulez vérifier le bug, mais vous ne voulez pas perdre le travail que vous avez créé sur la branche de développement. Vous ne voulez pas non plus commiter ce que vous avez écrit parce que ce n'est pas encore terminé.

Que faites-vous ? Vous ne pouvez pas commiter et vous ne pouvez pas changer de branche. Si vous changez de branche, les choses qui ne sont pas commitées seront transférées à la branche vers laquelle vous avez basculé.

Ce que vous voulez faire, c'est sauvegarder les changements quelque part temporairement pendant que vous basculez vers une autre branche. **Un Git stash est ce stockage temporaire.**

### Utiliser un Stash avec Git Fork

Pour utiliser un stash, vous devez commencer avec du code non commité. Pour cette leçon, nous allons utiliser le morceau de code suivant comme les changements non commités :

```
<!-- Some uncommitted code in index.html -->
```

```
<main>  <p> A new paragraph</p></main>
```

Pour stash ce code, vous pouvez cliquer sur le bouton stash.

![Image](https://cdn-media-1.freecodecamp.org/images/0*5QOUGLobId0ruTih.png)

Une fois que vous cliquez sur le bouton stash, Fork vous demandera de laisser un message. Ce message indique de quoi parle le stash.

Puisque les stashes sont temporaires, vous pouvez utiliser n'importe quel nom que vous voulez. Nous allons l'appeler « Temp storage ».

![Image](https://cdn-media-1.freecodecamp.org/images/0*iPtWYwszjCoDgTMx.png)

Une fois que vous avez créé un nouveau stash, vous le trouverez dans la section Stashes de la barre latérale.

![Image](https://cdn-media-1.freecodecamp.org/images/0*dbSJ_kDKSTlCKbSt.png)

Note : Vous ne pourrez pas voir les changements dans ce stash, mais ce n'est pas un problème parce que vous n'aurez pas à le faire. Ce que vous voulez faire, c'est changer de branche, terminer ce que vous avez à faire et revenir en arrière.

Dans ce cas, nous allons basculer vers la branche `master`. Lorsque vous le faites, remarquez que vous ne voyez pas le code non commité que nous avons écrit ci-dessus dans les branches `master` et `develop`.

### Appliquer les changements stashés

Vous pouvez revenir à la branche où vous étiez, puis faire un clic droit sur votre stash et sélectionner Apply stash.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Iajs_VZW2LF43WnM.png)

Fork vous demandera si vous voulez supprimer le stash lorsque vous le faites. Je supprime généralement le stash parce que je ne veux pas garder plus d'un stash à la fois.

![Image](https://cdn-media-1.freecodecamp.org/images/0*xBHNRhlClGgyIUiu.png)

Une fois que vous appliquez le stash, vous pourrez voir les changements que vous avez faits.

```
<!-- Vous verrez à nouveau votre code non commité ! -->
```

```
<main>  <p> A new paragraph</p></main>
```

### Conclusion

Les stashes sont des espaces de stockage temporaires où vous pouvez stocker votre code. Lorsque vous avez stocké votre code, vous pouvez passer à d'autres branches pour faire autre chose.

Lorsque vous avez terminé, vous pouvez remettre votre code depuis le stash.

Avec Git Stash, vous n'aurez pas à vous soucier de perdre des changements non commités !

Merci d'avoir lu. Cet article vous a-t-il aidé d'une quelconque manière ? Si c'est le cas, [j'espère que vous envisagez de le partager](http://twitter.com/share?text=How%20to%20use%20Git%20stashes%20as%20a%20temporary%20storage%20by%20@zellwk%20?%20&url=https://zellwk.com/blog/git-stash/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [zellwk.com](https://zellwk.com/blog/git-stash).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur front-end.