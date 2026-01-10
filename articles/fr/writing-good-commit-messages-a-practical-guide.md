---
title: 'Comment écrire de bons messages de commit : Un guide pratique Git'
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-11-28T21:23:53.000Z'
originalURL: https://freecodecamp.org/news/writing-good-commit-messages-a-practical-guide
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/article-banner.png
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: version control
  slug: version-control
seo_title: 'Comment écrire de bons messages de commit : Un guide pratique Git'
seo_desc: 'To create a useful revision history, teams should first agree on a commit
  message convention to use. This also applies to personal projects.

  Recently on Hashnode I asked, "Which commit message convention do you use at work?"
  and I got some amazing re...'
---

Pour créer un historique de révision utile, les équipes doivent d'abord se mettre d'accord sur une convention de messages de commit à utiliser. Cela s'applique également aux projets personnels.

Récemment sur [Hashnode](https://hashnode.com), j'ai demandé, **"Quelle convention de messages de commit utilisez-vous au travail ?"** et j'ai obtenu des réponses incroyables avec des utilisateurs expliquant les conventions qu'ils utilisent au travail et pour leurs projets personnels.

%[https://twitter.com/iambolajiayo/status/1198903055372165120]

Dans cet article, je vais expliquer comment écrire de bons messages de commit et pourquoi vous devriez le faire.

J'ai publié cet article, ainsi que beaucoup d'autres, sur mon blog [ici](https://blog.bolajiayodeji.com/writing-good-commit-messages-a-practical-guide).

## Introduction au contrôle de version avec Git

Les logiciels de contrôle de version sont une partie essentielle des pratiques des développeurs de logiciels modernes.

De loin, [Git](https://git-scm.com/) est le système de contrôle de version le plus largement utilisé au monde. Il s'agit d'un projet open source distribué et activement maintenu, initialement développé en 2005 par [Linus Torvalds](https://en.wikipedia.org/wiki/Linus_Torvalds), le célèbre créateur du noyau du système d'exploitation Linux.

Nouveau sur Git ? Consultez le guide officiel [pour commencer](https://git-scm.com/book/en/v1/Getting-Started) ou [cette présentation](https://slides.com/bolajiayodeji/introduction-to-version-control-with-git-and-github) d'une conférence que j'ai donnée.

## Qu'est-ce qu'un message de commit ?

La commande **commit** est utilisée pour sauvegarder les modifications dans un dépôt local après les avoir mises en stage dans Git. Cependant, avant de pouvoir sauvegarder les modifications dans Git, vous devez indiquer à Git quelles modifications vous souhaitez sauvegarder, car vous avez peut-être fait des tonnes de modifications. Une excellente façon de le faire est d'ajouter un **message de commit** pour identifier vos modifications.

### Options de commit

* **\-m**
  
  Cette option définit le message du commit.

```bash
git add static/admin/config.yml
git commit -m "Configuration de plusieurs rôles pour la passerelle git netlify-cms"
```

* **\-a ou --all**
  
  Cette option commite automatiquement tous les fichiers suivis, modifiés ou supprimés (y compris les nouveaux).

```bash
git commit -a -m "Ajout d'un nouveau rôle pour la passerelle git netlify-cms"
```

* **\--amend**
  
  Cette option réécrit le tout dernier commit avec les modifications actuellement mises en stage ou un nouveau message de commit et ne doit être effectuée que sur des commits qui n'ont pas encore été poussés vers un dépôt distant.

```bash
git add .
git commit --amend -m "Mise à jour des rôles pour la passerelle git netlify-cms"
```

## Pourquoi devrais-vous écrire de bons messages de commit ?

Vous pourriez dire, "Ce n'est qu'un projet personnel." Oui, vous travaillez seul maintenant, mais que se passe-t-il lorsque vous travaillez avec une équipe ou contribuez à l'open source ?

Un message de commit Git bien rédigé est le meilleur moyen de communiquer le contexte d'une modification aux autres développeurs travaillant sur ce projet, et en effet, à votre futur vous-même.

Avez-vous déjà essayé d'exécuter `git log` sur l'un de vos anciens projets pour voir les messages de commit "bizarres" que vous avez utilisés depuis sa création ? Il peut être difficile de comprendre pourquoi vous avez apporté certaines modifications dans le passé, et vous souhaiterez avoir lu cet article plus tôt :).

Les messages de commit peuvent communiquer adéquatement pourquoi une modification a été apportée, et comprendre cela rend le développement et la collaboration plus efficaces.

## Comment écrire des messages de commit avec Git

Auparavant, j'utilisais uniquement `git commit -m "Corriger X pour permettre à Y d'utiliser Z"` sur mes projets personnels avec juste un sujet et aucune description supplémentaire. Cela est idéal pour les petites corrections claires comme `git commit -m "Corriger une faute de frappe dans README.md`, mais dans le cas de modifications plus importantes, vous devrez ajouter quelques détails supplémentaires.

### Méthode de l'éditeur

Exécutez `git commit` sans message ni option et il ouvrira votre éditeur de texte par défaut pour écrire un message de commit.

Pour configurer votre éditeur "par défaut" :

```python
git config --global core.editor nano
```

Cela configurera Git pour utiliser nano comme votre éditeur par défaut. Remplacez "nano" par "emacs", "vim", ou tout autre éditeur de votre choix.

Dans l'éditeur ouvert, la première ligne est le sujet (description courte), laissez une ligne vide après celle-ci, et tout le reste est la description détaillée (corps).

```bash
<Résumé des modifications en environ 50 caractères ou moins>

<Description explicative plus détaillée de la modification, enveloppée à environ 72
caractères>
```

### Méthode de la ligne de commande

```python
git commit -m "Sujet" -m "Description..."
```

La première option `-m` est le sujet (description courte), et la suivante est la description détaillée (corps).

## Comment écrire de bons messages de commit

Il existe plusieurs conventions utilisées par différentes équipes et développeurs pour écrire de bons messages de commit. Je ne vais décrire que quelques règles et conseils généraux pour écrire des messages de commit – vous devez décider de la convention que vous souhaitez suivre. Et si vous travaillez pour une entreprise ou contribuez à l'open source, vous devez vous adapter à leur convention :).

Pour la cohérence, vous pouvez utiliser une convention pour le travail et une autre pour les projets personnels, car vous pourriez changer d'emploi un jour, et la convention pourrait également changer.

Assurez-vous de consulter [ce fil de discussion](https://hashnode.com/post/which-commit-message-convention-do-you-use-at-work-ck3e4jbdd00zyo4s1h7mc7e0g) pour quelques conventions de messages de commit incroyables ou ajoutez la vôtre pour aider quelqu'un à prendre une décision.

Voici un excellent modèle de bon message de commit, initialement écrit par [Tim Pope](https://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html)

```bash
Résumé capitalisé et court (50 caractères ou moins)

Texte explicatif plus détaillé, si nécessaire. Enveloppez-le à environ 72
caractères. Dans certains contextes, la première ligne est traitée comme le
sujet d'un email et le reste du texte comme le corps. La ligne vide séparant le
résumé du corps est cruciale (sauf si vous omettez entièrement le corps) ; des outils
comme rebase peuvent être confus si vous les exécutez ensemble.

Rédigez votre message de commit à l'impératif : "Corriger le bug" et non "Bug corrigé"
ou "Corrige le bug." Cette convention correspond aux messages de commit générés
par des commandes comme git merge et git revert.

Les paragraphes supplémentaires viennent après des lignes vides.

- Les puces sont également acceptables

- Typiquement, un tiret ou un astérisque est utilisé pour la puce, suivi d'un
  espace unique, avec des lignes vides entre les deux, mais les conventions varient ici

- Utilisez une indentation suspendue

Si vous utilisez un système de suivi des problèmes, ajoutez une référence à ceux-ci en bas,
comme ceci :

Résout : #123
```

Cela a l'air bien, n'est-ce pas ? Voici comment vous pouvez rendre les vôtres également excellents :

1. Spécifiez le type de commit :
   
* feat : La nouvelle fonctionnalité que vous ajoutez à une application particulière
   
* fix : Une correction de bug
   
* style : Fonctionnalité et mises à jour liées au style
   
* refactor : Refactorisation d'une section spécifique de la base de code
   
* test : Tout ce qui est lié aux tests
   
* docs : Tout ce qui est lié à la documentation
   
* chore : Maintenance régulière du code. [Vous pouvez également utiliser des emojis pour représenter les types de commit]
   

2. Séparez le sujet du corps par une ligne vide
   
3. Votre message de commit ne doit pas contenir d'erreurs d'espacement
   
4. Supprimez les marques de ponctuation inutiles
   
5. Ne terminez pas la ligne de sujet par un point
   
6. Capitalisez la ligne de sujet et chaque paragraphe
   
7. Utilisez le mode impératif dans la ligne de sujet
   
8. Utilisez le corps pour expliquer quelles modifications vous avez apportées et pourquoi vous les avez faites.
   
9. Ne supposez pas que le relecteur comprend quel était le problème initial, assurez-vous de l'ajouter.
   
10. Ne pensez pas que votre code est auto-explicatif
   
11. Suivez la convention de commit définie par votre équipe
   
## Conclusion

La partie la plus importante d'un message de commit est qu'il doit être clair et significatif. À long terme, écrire de bons messages de commit montre à quel point vous êtes un collaborateur. Les avantages d'écrire de bons messages de commit ne sont pas seulement limités à votre équipe, mais s'étendent en effet à vous-même et aux futurs contributeurs.

Vous voulez en savoir plus sur Git et devenir un "contrôleur de version" professionnel ? Consultez ces excellentes ressources :

* [https://try.github.io/](https://try.github.io/)
   
* [https://git-scm.com/book/en/v2](https://git-scm.com/book/en/v2)
   
* [https://www.git-tower.com/learn/](https://www.git-tower.com/learn/)
   
* [https://learngitbranching.js.org/](https://learngitbranching.js.org/)
   
* [https://github.com/commitizen/cz-cli](https://github.com/commitizen/cz-cli)