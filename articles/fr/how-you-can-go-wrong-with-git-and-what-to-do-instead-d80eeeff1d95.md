---
title: Comment vous pouvez vous tromper avec Git — et que faire à la place.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-14T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-you-can-go-wrong-with-git-and-what-to-do-instead-d80eeeff1d95
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Tj_DgrXII8u5E1sv
tags:
- name: coding
  slug: coding
- name: Git
  slug: git
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment vous pouvez vous tromper avec Git — et que faire à la place.
seo_desc: 'By Aditya Sridhar

  I am not able to commit to the remote repository, let me do a force push.

  Let me run rebase on the remote repository, to make the commit history neater.

  Let me amend my previous commit which is in the remote repository.

  The points m...'
---

Par Aditya Sridhar

Je ne peux pas commiter vers le dépôt distant, laissez-moi faire un force push.

Laissez-moi exécuter rebase sur le dépôt distant, pour rendre l'historique des commits plus propre.

Laissez-moi modifier mon précédent commit qui est dans le dépôt distant.

**Les points mentionnés ci-dessus sont quelques-unes des choses à éviter de faire dans Git.**

Dans mes précédents articles, j'ai couvert [les bases de Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61) et [Git amend et rebase](https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826). Cliquez sur les liens pour en savoir plus à leur sujet.

Git a des fonctionnalités incroyables et est très utile pour les développeurs. Mais des erreurs se produisent encore lors de l'utilisation de Git. Ici, je vais mentionner certaines des **choses à éviter** lors de l'utilisation de Git et aussi **expliquer pourquoi** vous devriez les éviter.

### Force push vers le dépôt distant

![Image](https://cdn-media-1.freecodecamp.org/images/vxvEY0Py6Tt3Jsfqcw3H5BSMdGC2qpuA2TqD)
_Photo par [Unsplash](https://unsplash.com/@timmossholder?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Tim Mossholder</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Supposons que deux développeurs travaillent sur une seule branche. Le développeur 2 est un débutant avec Git.

1. Le développeur 1 a terminé ses modifications et a poussé le code vers le dépôt distant.
2. Maintenant, le développeur 2 a terminé ses modifications, mais ne peut pas pousser le code vers le dépôt distant.
3. Le développeur 2 fait une recherche rapide sur Google et découvre la commande force push et l'utilise. La commande est `git push -f`
4. Le développeur 1 vérifie le dépôt distant pour constater que le code qu'il a écrit a complètement disparu.

**C'est parce que force push écrase le code dans le dépôt distant et, par conséquent, le code existant dans le dépôt distant est perdu.**

#### Manière idéale de gérer ce scénario

Le développeur 2 doit tirer les dernières modifications de code du dépôt distant et rebaser les modifications de code dans le dépôt local. Une fois le rebase effectué avec succès, le développeur 2 peut pousser le code dans le dépôt distant. **Ici, nous parlons de rebase du dépôt distant vers le dépôt local dans la même branche.**

**Évitez force push** sauf si absolument nécessaire. Utilisez-le uniquement en dernier recours s'il n'y a pas d'autre moyen de gérer une situation. Mais souvenez-vous que force push écrasera le code dans le dépôt distant.

En fait, si vous utilisez une interface utilisateur comme source tree, par défaut, force push est désactivé. Vous devrez l'activer manuellement pour l'utiliser.

De plus, si les bons [workflows Git](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369) sont utilisés, chaque développeur aura ses propres branches de fonctionnalités, et un tel scénario ne se produirait même pas.

### Essayer de rebaser le dépôt distant

![Image](https://cdn-media-1.freecodecamp.org/images/YYrwWwrW0Le9w89HoybfYPLmJ5JpmwwzABOG)
_green, red, and white high voltage circuit breaker par [Unsplash](https://unsplash.com/@benhershey?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Ben Hershey</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Supposons que deux développeurs travaillent sur une branche de fonctionnalité.

1. Le développeur 1 a fait un ensemble de commits et les a poussés vers la branche de fonctionnalité distante.
2. Le développeur 2 prend les dernières modifications de la branche de fonctionnalité distante dans la branche de fonctionnalité locale.
3. Le développeur 2 ajoute un ensemble de commits à la branche de fonctionnalité locale.
4. Mais le développeur 2 veut également s'assurer que les dernières modifications de la branche de release sont rebasées dans le dépôt de fonctionnalité. Donc, le développeur 2 rebase la branche de release sur la branche de fonctionnalité locale. **C'est le rebase effectué du dépôt distant vers le dépôt local de branches différentes**.
5. Maintenant, le développeur 2 essaie de pousser le code vers la branche de fonctionnalité distante. Git ne vous permettra pas de le faire puisque l'historique des commits a changé. Donc, le développeur 2 ferait un force push.
6. Maintenant, lorsque le développeur 1 veut tirer le dernier code de la branche de fonctionnalité distante, c'est un travail difficile puisque l'historique des commits a changé. Donc, le développeur 1 devra gérer beaucoup de conflits de code — même des conflits de code redondants qui avaient déjà été résolus par le développeur 2.

**Rebaser le dépôt distant modifiera l'historique des commits et créera des problèmes lorsque d'autres développeurs essaieront de tirer le dernier code du dépôt distant.**

#### Manière idéale de gérer ce scénario

La manière idéale de gérer cette situation est de toujours rebaser **uniquement** le dépôt local. Aucun des commits dans le dépôt local ne devrait avoir déjà été poussé vers le dépôt distant.

Si l'un des commits a déjà été poussé vers la branche de fonctionnalité distante, il est préférable de faire un merge avec la branche de release plutôt qu'un rebase puisque le merge ne modifiera pas l'historique des commits.

De plus, si les bons workflows Git sont utilisés, une seule personne travaillerait sur une branche de fonctionnalité, et ce problème ne se produirait même pas.

Si une seule personne travaille sur la branche de fonctionnalité et qu'un rebase est effectué sur la branche de fonctionnalité distante, alors il n'y a pas de problème — aucun autre développeur ne tire de code de la même branche de fonctionnalité distante. Mais il est préférable d'éviter de rebaser un dépôt distant.

**Rebase est une fonctionnalité très puissante, mais utilisez-la avec précaution.**

### Modifier les commits dans le dépôt distant

![Image](https://cdn-media-1.freecodecamp.org/images/gq1Wo6a6yVlzmaudBN6xO6Vs65fZ7EkiYukn)
_broken ceramic plate on floor par [Unsplash](https://unsplash.com/@chuttersnap?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">chuttersnap</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Supposons que deux développeurs travaillent sur une branche de fonctionnalité.

1. Le développeur 1 a fait un commit et l'a poussé vers la branche de fonctionnalité distante. Appelons cela commit old.
2. Le développeur 2 tire le dernier code de la branche de fonctionnalité distante dans la branche de fonctionnalité locale
3. Le développeur 2 travaille sur le code dans le dépôt local et n'a pas encore poussé de code vers le dépôt distant.
4. Le développeur 1 réalise qu'il y avait une erreur dans le commit, et modifie le commit dans le dépôt local. Appelons cela commit new.
5. Le développeur 1 essaie de pousser le commit modifié vers la branche de fonctionnalité distante. Mais Git ne permettrait pas cela puisque l'historique des commits a changé. Donc, le développeur 1 fait un force push.
6. Maintenant, lorsque le développeur 2 veut tirer le dernier code de la branche de fonctionnalité distante, Git remarquera la différence dans les historiques des commits et créera un commit de merge. Lorsque le développeur 2 passera en revue l'historique des commits dans le dépôt local, le développeur 2 remarquera à la fois commit new et commit old. Cela détruit tout l'intérêt de modifier un commit.
7. Même si le développeur 2 fait un rebase de la branche distante vers la branche locale, commit old sera toujours présent dans le dépôt local du développeur 2. Donc, il fera toujours partie de l'historique des commits.

**Modifier un commit change l'historique des commits. Donc, modifier un commit dans le dépôt distant créera de la confusion lorsque d'autres développeurs essaieront de tirer le dernier code du dépôt distant**

#### Manière idéale de gérer ce scénario

La meilleure pratique est de modifier les commits uniquement dans le dépôt local. Une fois que le commit est dans le dépôt distant, il est préférable de ne faire aucune modification.

De plus, si les bons workflows Git sont utilisés, une seule personne travaillerait sur une branche de fonctionnalité et ce problème ne se produirait même pas. Dans ce cas, modifier un dépôt distant ne créerait aucun problème, puisque aucun autre développeur ne tire de code de la même branche de fonctionnalité distante.

### Hard reset

![Image](https://cdn-media-1.freecodecamp.org/images/6JofEPRTTXtI2CQJvVYxKtSnV3NtdyL9TbBZ)
_clear hour glass beside pink flowers par [Unsplash](https://unsplash.com/@nate_dumlao?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Nathan Dumlao</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

1. Le hard reset est effectué en utilisant `git reset --hard`
2. Il existe d'autres types de reset comme `--soft` et `--mixed` qui ne sont pas aussi dangereux que le hard reset

Supposons que le développeur 1 travaille sur une branche de fonctionnalité et a fait cinq commits dans le dépôt local.

1. De plus, le développeur 1 travaille actuellement sur deux fichiers qui ne sont pas encore commités.
2. Si le développeur 1 exécute `git reset --hard <commit4hash>`, les choses suivantes se produiront.
3. Le dernier commit dans la branche de fonctionnalité sera maintenant commit4 et commit5 est perdu.
4. Les deux fichiers non commités sur lesquels le développeur 1 travaillait sont également perdus

Commit5 est toujours là en interne dans Git mais la référence à celui-ci est perdue. Nous pouvons récupérer commit5 en utilisant `git reflog`. Mais, cela dit, il est toujours très risqué d'utiliser le hard reset.

**Soyez très prudent lorsque vous utilisez les commandes de reset dans Git. Vous devrez peut-être utiliser reset dans certains scénarios, mais évaluez complètement la situation avant de procéder à un hard reset.**

### Comment connaître les mauvaises pratiques lors de l'utilisation de Git

![Image](https://cdn-media-1.freecodecamp.org/images/sa54At5X8hjGOHKzP2owlBAfmMuhkjIdpzOy)
_question mark neon signage par [Unsplash](https://unsplash.com/@emilymorter?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Emily Morter</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

La liste que j'ai mentionnée ci-dessus ne couvre pas tout. Elle liste simplement certaines des choses qui peuvent mal tourner lors de l'utilisation de Git.

Alors, comment savez-vous en général quoi éviter lors de l'utilisation de Git ?

1. Une chose commune que vous aurez observée dans la liste ci-dessus est que des problèmes surviennent lorsque plusieurs personnes travaillent sur la même branche. Donc, utiliser les bons workflows Git garantirait qu'une seule personne travaille sur une branche de fonctionnalité à la fois. La branche de release serait gérée par le responsable technique ou un développeur senior. Ce workflow peut prévenir certains problèmes majeurs.
2. Une autre chose commune que vous observerez est l'utilisation de force push partout. Git, par défaut, garantit que vous ne pouvez pas effectuer de changement destructeur dans le dépôt distant. Mais force push remplace le comportement par défaut de Git.
3. Donc, chaque fois que vous êtes dans une position où vous pourriez avoir besoin d'utiliser force push, utilisez-le uniquement en dernier recours. Évaluez également s'il existe un autre moyen d'atteindre ce que vous voulez sans utiliser force push.
4. Toute opération qui modifie l'historique des commits dans le dépôt distant peut être dangereuse. Modifiez l'historique des commits uniquement dans votre dépôt local. Mais même dans le dépôt local, soyez prudent lors de l'utilisation de hard reset.
5. L'utilisation de workflows Git peut être excessive dans des projets très petits. Dans ces projets, plusieurs développeurs travailleront sur la même branche. Mais, avant d'effectuer un changement majeur dans le dépôt distant, il est préférable d'évaluer une fois si cela impactera les autres développeurs.

Espérons que cet article a donné quelques idées sur ce qui peut mal tourner dans Git et comment l'éviter. 💡

### À propos de l'auteur

J'aime la technologie et suis les avancées dans le domaine. J'aime aussi aider les autres avec mes connaissances technologiques.

N'hésitez pas à me contacter sur mon compte LinkedIn [https://www.linkedin.com/in/aditya1811/](https://www.linkedin.com/in/aditya1811/)

Vous pouvez également me suivre sur Twitter [https://twitter.com/adityasridhar18](https://twitter.com/adityasridhar18)

Mon site web : [https://adityasridhar.com/](https://adityasridhar.com/)

### Autres articles de moi

[Une introduction à Git](https://medium.freecodecamp.org/what-is-git-and-how-to-use-it-c341b049ae61)

[Comment utiliser Git efficacement](https://medium.freecodecamp.org/how-to-use-git-efficiently-54320a236369)

[Comment devenir un expert git](https://medium.freecodecamp.org/how-to-become-a-git-expert-e7c38bf54826)

Publié à l'origine sur [adityasridhar.com](https://adityasridhar.com/posts/how-you-can-go-wrong-with-git)