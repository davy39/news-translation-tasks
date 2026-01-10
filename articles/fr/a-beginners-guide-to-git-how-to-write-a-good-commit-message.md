---
title: Un guide pour débutants sur Git — Comment rédiger un bon message de commit
subtitle: ''
author: Gaël Thomas
co_authors: []
series: null
date: '2020-03-24T14:15:54.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-to-git-how-to-write-a-good-commit-message
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/how-to-write-a-good-commit-message.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Un guide pour débutants sur Git — Comment rédiger un bon message de commit
seo_desc: 'Are you a developer who has recently started using Git? If you are wondering
  how to create a good commit message for your project, then this article is made
  for you.

  After a few weeks away from writing, I’m coming back today with a follow-up to one
  o...'
---

Êtes-vous un développeur qui a récemment commencé à utiliser Git ? Si vous vous demandez comment créer un bon message de commit pour votre projet, alors cet article est fait pour vous.

Après quelques semaines sans écrire, je reviens aujourd'hui avec une suite à l'un de mes articles les plus recherchés sur Google.

Quand j'ai commencé à écrire, il y a un an, j'ai créé un article sur [comment démarrer et créer votre premier dépôt avec Git](https://herewecode.io/blog/a-beginners-guide-to-git-how-to-start-and-create-your-first-repository/).

Cet article aide de nombreuses personnes chaque semaine. J'ai donc décidé d'écrire cet article sur la façon de rédiger un bon message de commit pour que vous puissiez passer vos compétences Git au niveau supérieur.

## Qu'est-ce qu'un bon message de commit ?

Pour rappel, un message de commit est le texte court que vous laissez lorsque vous sauvegardez votre travail sur Git. Ce message vise à identifier votre travail.

L'idée est que simplement en le lisant, n'importe qui pourra comprendre clairement ce que vous avez fait dans cette partie de votre travail.

### Un bon exemple de commit

Ci-dessous, vous pouvez trouver les derniers commits du projet Angular.js sur GitHub. Comme vous pouvez le voir, les messages sont clairs et nous pouvons mieux comprendre quel travail a été effectué dans différentes parties.

Par exemple, le 24 juillet 2019, « gkalpak » a mis à jour « SauceConnect » et est passé à la dernière version de Safari (le navigateur web).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/git-commits-history.png)
_Historique des commits Git sur le projet Angular.js [sur GitHub](https://github.com/angular/angular.js/commits/master)_

### Pourquoi tout le monde ne commit pas de la même manière ?

Malheureusement, il n'existe pas de méthode universelle pour écrire des commits. Chaque projet et chaque entreprise définissent des règles spécifiques pour leurs besoins.

Mais ne vous inquiétez pas, vous trouverez souvent des façons similaires d'écrire un message.

Pour savoir quelles sont ces règles, je vous recommande vivement de les lire avant de commencer dans une entreprise ou de travailler sur un projet open-source.

Je vous donnerai plus de détails sur ces directives plus tard dans cet article.

## Pourquoi il est essentiel de bien rédiger votre commit

J'ai créé une courte liste des avantages d'utiliser un bon message de commit.

### Meilleure collaboration

Si vous travaillez dans une entreprise ou sur un projet open-source, il est essentiel de suivre les règles pour une meilleure coopération. Si vous écrivez quelque chose de compréhensible, en suivant les règles du projet, les autres développeurs pourront travailler plus efficacement. Ils n'auront pas à vous poser de questions sur votre travail.

> Note : Si vous travaillez sur un projet personnel, je vous recommande également de suivre des règles spécifiques. Cela améliorera votre productivité, et si vous avez besoin de l'aide d'un autre développeur, il lui sera plus facile de commencer à travailler sur votre projet.

### Meilleure compréhension

Vous devez créer des messages clairs et compréhensibles. Cela vous aidera, vous et vos collaborateurs, à travailler ensemble sur un projet. Ci-dessous, vous pouvez trouver un exemple d'historique de commits git avec uniquement des messages flous. Comme vous le verrez, il est difficile de comprendre ce qui s'est passé.

### BONUS - Une génération de changelog

Je vais vous révéler un petit secret : si vous écrivez de bons messages, vous pourrez générer un changelog directement à partir de vos messages de commit.

Voici quelques outils pour le faire :

* [Github Changelog Generator](https://github.com/github-changelog-generator/github-changelog-generator)
* [Git Chglog](https://github.com/git-chglog/git-chglog)
* [Auto Changelog](https://github.com/CookPete/auto-changelog)
* [Conventional Changelog](https://github.com/conventional-changelog/conventional-changelog).

J'écrirai prochainement un article sur ce sujet également. Si vous souhaitez être informé, [vous pouvez me suivre sur Twitter](https://twitter.com/gaelgthomas/). Je poste toutes les mises à jour là-bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/bad-git-commits.png)
_Exemple de mauvais commits git de [Jason McCreary](https://jasonmccreary.me/articles/when-to-make-git-commit/)_

> Note : Si vous voulez avoir plus d'exemples de mauvais commits et vous amuser en même temps, [un compte Twitter nommé "gitlost"](https://twitter.com/gitlost) tweete chaque jour avec des commits drôles et non filtrés.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/git-changelog.png)
_Exemple de changelog Git généré automatiquement_

D'accord, maintenant, entrons dans les détails et voyons ce qu'il faut vraiment pour écrire un bon message de commit.

## Comment écrire un message de commit

Si vous voulez écrire un bon message de commit, vous devez suivre certaines règles. J'ai créé une liste de contrôle ci-dessous. Chaque fois que vous voulez commiter, prenez le temps de vous référer à cette liste.

* **Vérifiez toujours votre grammaire.** Ce n'est jamais agréable de lire un message rempli d'erreurs. Pour cela, je vous recommande d'utiliser un outil de grammaire. Si vous écrivez en anglais, vous pouvez utiliser [Grammarly](https://www.grammarly.com/), [Reverso](https://www.reverso.net/spell-checker/english-spelling-grammar/), ou [GrammarCheck](https://www.grammarcheck.net/editor/). Ces outils ne sont pas parfaits, mais ils élimineront la plupart de vos erreurs.
* **Un commit, un changement.** Essayez de commiter souvent. Il est idéal d'avoir chaque changement dans un commit différent. Il sera plus facile pour vous de revenir à votre travail précédent.
* **Soyez clair.** Lorsque vous écrivez un commit, essayez d'être aussi transparent que possible. Je vous recommande d'utiliser un anglais simple et d'aller droit au but.
* **Détaillez ce que vous avez fait.** Prenez le temps de relire votre code pour écrire ce que vous avez fait. Au cas où vous auriez besoin d'ajouter beaucoup de détails, utilisez la partie description du commit.

### La commande git commit

Je veux partager plus de détails sur la commande 'git commit'. Si vous n'utilisez pas de logiciel git, vous devez savoir que vous pouvez créer des commits détaillés en tapant cette commande :

```
$ git commit -m "Titre" -m "Description"
```

C'est la même chose qu'avant, mais avec une deuxième partie pour la description. Donc, "-m 'titre' " vous permet d'écrire le titre court du commit, et "-m 'description' " vous permet d'écrire la description si vous devez donner plus de détails.

### Utilisez des directives git

Si vous voulez avoir un historique de commits git clair, vous devez suivre certaines directives. Dans mon cas, j'ai choisi [celle simple de Udacity](http://udacity.github.io/git-styleguide/).

Il en existe beaucoup d'autres, comme [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/), et [Angular Guideline](https://github.com/angular/angular/blob/master/CONTRIBUTING.md#commit). Une directive de commit vous aidera à donner une structure à vos commits.

Par exemple, ajouter une balise pour clarifier ce que vous avez fait : "git commit -m 'fix: supprime correctement toutes les informations de l'utilisateur lorsque le bouton supprimer le compte est déclenché'".

## Conclusion

J'espère que vous avez aimé ce guide sur la façon de commiter sur Git ! Si vous avez des questions ou des commentaires, n'hésitez pas à demander.

Si vous avez d'autres conseils sur la façon de faire de bons commits, faites-le moi savoir.

Si vous voulez plus de contenu comme celui-ci, vous pouvez [me suivre sur Twitter](https://twitter.com/gaelgthomas/), où je tweete sur le développement web, l'amélioration de soi et mon parcours en tant que développeur full stack !