---
title: Comment rédiger des messages de commit que les mainteneurs de projets apprécieront
subtitle: ''
author: Christine Belzie
co_authors: []
series: null
date: '2023-11-11T01:16:19.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-commit-messages-maintainers-will-like
coverImage: https://www.freecodecamp.org/news/content/images/2023/11/Commit-message-post.png
tags:
- name: best practices
  slug: best-practices
- name: community
  slug: community
- name: open source
  slug: open-source
seo_title: Comment rédiger des messages de commit que les mainteneurs de projets apprécieront
seo_desc: "You know the saying “If you keep looking at the past, you’ll miss the future”?\
  \ Well in the context of coding and working with Git, that’s not the case. \nYour\
  \ commit history plays a huge role in the future of the open source projects that\
  \ you contribu..."
---

Vous connaissez le dicton « Si vous continuez à regarder le passé, vous allez manquer l'avenir » ? Eh bien, dans le contexte de la programmation et du travail avec Git, ce n'est pas le cas. 

Votre historique de commits joue un rôle énorme dans l'avenir des projets open source auxquels vous contribuez, et les messages de commit sont essentiels pour rendre cela possible. 

Qu'est-ce que les messages de commit, pouvez-vous demander ? Ces brèves explications décrivent les modifications que vous avez apportées à la base de code, et elles sont très utiles si des choses comme des bugs se produisent. 

Les messages de commit sont également d'excellents points de contrôle si vous revenez à un projet open source auquel vous n'avez pas contribué depuis un certain temps et que vous devez vous rappeler des modifications que vous avez apportées jusqu'à présent. 

Vous vous sentez intimidé ? Pas de soucis. Dans ce guide rapide, vous apprendrez à rédiger des messages de commit efficaces.

## Qu'est-ce qui fait un mauvais message de commit ?

Comme la plupart des choses dans la vie, nous devons apprendre ce qui fait un message de commit peu utile avant d'apprendre à en écrire un bon. 

Regardons un exemple :

```git
mention information

```

Même si ce message de commit décrit le changement, il n'explique pas **pourquoi** le changement a été fait, ce qui peut laisser les mainteneurs perplexes. 

Il ne précise pas non plus **quel** type d'information a été mentionné. Les mainteneurs pourraient se demander « Était-ce un extrait de code manquant ? Un lien vers une section spécifique ? ». Ce sont des choses que vous voulez éviter lors de la rédaction de messages de commit. 

Maintenant que nous avons vu le mauvais, apprenons à transformer ce message de commit en quelque chose que les mainteneurs peuvent comprendre.

## Caractéristiques d'un bon message de commit

Vous vous souvenez comment j'ai dit que le message de commit précédent était un peu vague ? Eh bien, voici comment nous pouvons le corriger :

### Étape 1 – Mentionner le type

C'est ici que vous précisez le type de changement que vous apportez à la base de code. Cela facilite la compréhension de votre contribution pour les mainteneurs et les autres contributeurs. 

Voici à quoi ressemblerait cette étape avec l'exemple de commit :

```git
feat: mention information

```

Puisque l'exemple de commit semble se concentrer sur l'ajout de texte, j'ai décidé d'utiliser `feat` car il est souvent utilisé pour décrire des contributions où des informations ou une nouvelle fonctionnalité sont ajoutées à un projet open source. 

Voici quelques autres abréviations courantes utilisées pour catégoriser les commits :

* `docs` : Cela est couramment utilisé pour décrire les révisions des versions actuelles ou les mises à jour de la documentation d'un projet open source.
* `fix` : Cela est généralement utilisé pour corriger des bugs dans la base de code du projet ou de petites erreurs de grammaire dans la documentation du projet. 
* `chore` : Cela est souvent utilisé pour une contribution qui peut prendre plus de temps que d'habitude à terminer. 

### Étape 2 – Résumer le changement

C'est ici que vous donnez un aperçu du changement et de la manière dont vous l'avez fait. Cela aide les mainteneurs à comprendre comment votre contribution résout le problème que vous essayez de résoudre. 

Il est important de noter que GitHub a une limite de 72 caractères, vous devrez donc garder votre description dans cette plage. Reprenons notre exemple :

```git
feat: mention information
```

Vous vous souvenez comment j'ai dit qu'il ne précise pas la faute de frappe qui a été corrigée ? Eh bien, après réflexion, j'ai décidé d'écrire ceci :

```git
feat: mention de Christine Peterson dans l'intro du cours
```

C'est tellement mieux ! :) Contrairement à avant, cette version de l'exemple de commit mentionne le type d'information et précise où elle a été ajoutée dans le projet. Cela aide les mainteneurs à mieux comprendre pourquoi cette contribution a été faite. 

### Étape facultative – Ajouter une description

C'est ici que vous décrivez le changement plus en détail en mentionnant pourquoi vous l'avez fait. Bien que cette étape soit facultative, envisagez de le faire afin que les mainteneurs puissent se faire une idée de la manière dont votre contribution améliore ou résout un problème dans leur projet. 

Voici à quoi cela ressemblerait avec notre exemple :

```git
J'ai décidé d'ajouter cette information pour que les participants obtiennent des informations précises.
```

En faisant la description, j'ai décidé de la garder courte mais spécifique. De cette façon, cela aiderait les mainteneurs à comprendre pourquoi j'ai fait cette contribution et comment elle améliore le projet. 

Maintenant, rassemblons toutes ces parties :

```git
feat: mention de Christine Peterson dans l'intro du cours

J'ai décidé d'ajouter cette information pour que les participants puissent obtenir des informations précises
```

Maintenant, en comparaison avec l'exemple original, ce message de commit est plus efficace car il fait ce qui suit :

* Précise le type de commit effectué 
* Décrit comment la contribution améliore le projet
* Résume le changement 

Ça a l'air bien, n'est-ce pas ? 😉

## Conclusion

Que vous soyez un nouveau contributeur ou un vétéran expérimenté, la rédaction de messages de commit efficaces est cruciale pour communiquer vos contributions aux mainteneurs. 

Si vous cherchez d'autres moyens d'améliorer vos compétences en rédaction de messages de commit, consultez [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/). De plus, suivez-moi sur [BioDrop](https://www.biodrop.io/CBID2) pour découvrir mes réseaux sociaux et d'autres articles techniques.