---
title: Comment annuler les modifications dans Git
subtitle: ''
author: Zell Liew
co_authors: []
series: null
date: '2018-12-07T16:47:47.000Z'
originalURL: https://freecodecamp.org/news/how-to-undo-changes-in-git-e1da7930afdb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*6JjR02sGP4FgM6zj.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: videos
  slug: videos
seo_title: Comment annuler les modifications dans Git
seo_desc: 'You may already know that Git is like a save point system. What you generally
  learn with Git initially is to learn to save your changes and commit them to a remote
  repository. But how do you undo a change, and go back to a previous state?

  That’s what...'
---

Vous savez peut-être déjà que Git est comme un système de points de sauvegarde. Ce que vous apprenez généralement avec Git au début, c'est à sauvegarder vos modifications et à les commiter dans un dépôt distant. Mais comment annuler une modification et revenir à un état précédent ?

C'est ce que nous allons couvrir dans cet article.

J'ai couvert le contenu de cet article dans une vidéo si vous préférez apprendre en regardant plutôt qu'en lisant.

### Local vs Distant

Il est plus compliqué d'annuler quelque chose qui est déjà sur le dépôt distant. C'est pourquoi vous voulez garder les choses en local jusqu'à ce qu'elles soient confirmées.

### Quatre scénarios courants

Nous allons couvrir les quatre scénarios courants suivants :

1. Abandonner les modifications locales
2. Modifier le dernier commit
3. Revenir à un commit précédent
4. Annuler un commit qui a été poussé vers le dépôt distant

Note : Dans les captures d'écran ci-dessous, j'ai utilisé le client Git [Fork pour Mac OS](https://git-fork.com/). Vous pouvez faire de même dans d'autres clients Git similaires.

#### Scénario 1 : Abandonner les modifications locales

Le premier scénario est lorsque vous avez créé des modifications. Elles ne sont pas encore commitées. Et vous voulez supprimer ces modifications.

Supposons que nous voulons créer une nouvelle fonctionnalité. Nous allons ajouter du HTML et du CSS au projet :

```html
<!--Dans index.html-->
<div class="feature"></div>
```

```css
/* Dans le fichier CSS */
.feature {
  font-size: 2em; 
  /* Autres styles */
}
```

Pour abandonner ces modifications :

1. Allez dans la zone de staging
2. Sélectionnez les fichiers où vous voulez abandonner les modifications
3. Faites un clic droit sur les fichiers
4. Sélectionnez abandonner les modifications

![Image](https://cdn-media-1.freecodecamp.org/images/0*6JjR02sGP4FgM6zj.png)

#### Scénario 2 : Modifier le dernier commit

Lorsque vous avez créé un commit et que vous avez oublié certaines modifications et que vous voulez ajouter ces modifications dans le message du commit précédent.

1. Allez dans la zone de staging
2. Ajoutez les fichiers à commiter
3. Cliquez sur la case à cocher amend
4. Modifiez votre message de commit
5. Commitez

![Image](https://cdn-media-1.freecodecamp.org/images/0*1wkCc2i9X8JWsBz4.png)

#### Scénario 3 : Revenir à un commit précédent

Vous avez déjà plusieurs commits dans votre dépôt local. Vous décidez que vous ne voulez plus de ces commits et que vous voulez "charger" vos fichiers à partir d'un état précédent.

1. Allez dans l'historique Git
2. Faites un clic droit sur le commit auquel vous voulez revenir
3. Sélectionnez réinitialiser la `branche` ici

![Image](https://cdn-media-1.freecodecamp.org/images/0*IwWQ9XZNRmCaVvb8.png)

> Note : Vous ne pouvez réinitialiser qu'à un commit qui n'a pas été poussé vers le dépôt distant.

#### Scénario 4 : Annuler un commit qui a été poussé vers le dépôt distant

Si vous avez un commit qui a été poussé vers la branche distante, vous devez l'annuler.

> Annuler signifie défaire les modifications en créant un nouveau commit. Si vous avez ajouté une ligne, ce commit d'annulation supprimera la ligne. Si vous avez supprimé une ligne, ce commit d'annulation ajoutera la ligne à nouveau.

Pour annuler, vous pouvez :

1. Allez dans l'historique Git
2. Faites un clic droit sur le commit que vous voulez annuler
3. Sélectionnez annuler le commit
4. Assurez-vous que `commiter les modifications` est coché.
5. Cliquez sur annuler

![Image](https://cdn-media-1.freecodecamp.org/images/0*29rgArX4rXn3aH6x.png)

![Image](https://cdn-media-1.freecodecamp.org/images/0*fUD5rUESrzaMnbXu.png)

### Autres scénarios

GitHub a un article utile qui vous montre comment annuler presque tout avec Git. Il sera utile si vous rencontrez d'autres scénarios. Lisez-le [ici](https://blog.github.com/2015-06-08-how-to-undo-almost-anything-with-git/).

Merci d'avoir lu. Cet article vous a-t-il aidé d'une manière ou d'une autre ? Si c'est le cas, [j'espère que vous envisagerez de le partager](http://twitter.com/share?text=Annuler%20les%20modifications%20dans%20Git%20par%20@zellwk%20?%20&url=https://zellwk.com/blog/git-undo/&hashtags=). Vous pourriez aider quelqu'un. Merci !

Cet article a été initialement publié sur [mon blog](https://zellwk.com/blog/git-undo).  
Inscrivez-vous à ma [newsletter](https://zellwk.com/) si vous voulez plus d'articles pour vous aider à devenir un meilleur développeur frontend.