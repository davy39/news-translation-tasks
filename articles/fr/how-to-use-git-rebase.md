---
title: Comment utiliser Git Rebase – Tutoriel pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-04-17T22:17:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-git-rebase
coverImage: https://www.freecodecamp.org/news/content/images/2023/04/Screenshot-2023-04-15-at-10.58.48-PM.png
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment utiliser Git Rebase – Tutoriel pour débutants
seo_desc: 'By Nick Abbene

  The software engineering landscape is constantly changing. Staying up to date on
  new technologies is absolutely critical.

  But as developers, sometimes we forget how important it is to dig a bit deeper into
  the tried and true technologi...'
---

Par Nick Abbene

Le paysage de l'ingénierie logicielle est en constante évolution. Rester à jour sur les nouvelles technologies est absolument crucial.

Mais en tant que développeurs, nous oublions parfois à quel point il est important d'approfondir les technologies éprouvées qui constituent l'épine dorsale du développement logiciel – comme les systèmes de contrôle de version tels que Git.

Dans cet article, nous allons examiner une alternative à la commande git merge largement utilisée. Cette alternative est git rebase.

## Comprendre Git Rebase

Git rebase est une fonctionnalité puissante de Git qui permet de réécrire et de réorganiser votre historique de commits. Git rebase vous permet de changer la base de votre branche.

Contrairement à la fusion, qui crée un nouveau commit de fusion et combine l'historique des deux branches, le rebasage rejoue les commits d'une branche sur une autre. Cela résulte en un historique de commits linéaire, plus facile à lire et à comprendre.

### Préparer le terrain avec Git Merge

Vous ne comprenez pas la différence entre git merge et git rebase ? Considérons un exemple. Vous travaillez sur une nouvelle modification, donc vous créez une nouvelle branche avec `git checkout -b`. Vous commitez ensuite quelques modifications sur votre nouvelle branche.


![Image](https://lh4.googleusercontent.com/KzlG4wOQ_D3M6THap-VPhIQaRsYs2_PjXrbwwzru4fiYmAorZZJLMUl0SqH6MeTCLDXE5rHtpzpLztENpFBRXMcM0EFbUS-mb3cnOuC7kSgsiMdK5NWo138AcbTVNF_ePqLsMRMbnx-7HuH4SFjL5_E)
_Illustration de base des commits_

Pendant ce temps, quelqu'un d'autre travaillant sur une partie séparée du système fusionne sa propre Pull Request ! L'historique git ressemble maintenant un peu à ceci, car ils n'ont aucun contexte ou connaissance de vos modifications.


![Image](https://lh3.googleusercontent.com/qLOwHczX8I02UWtZ5ymTVSvaaXB9760kv0UhDDx-e3eOPtjM93jNhsxTHePfyWL0OBrAxEgR8X9mRgUg_U-q0AHtSnZDad5HJyZeEMQMkb7CXBY18xRBhzgP6pXhW-uuhUX0LsHJCdxf81XCex5FIR8)
_Illustration de git, votre coéquipier a poussé de nouveaux commits._

Vous terminez vos modifications avec un dernier commit final. Mais que faites-vous ensuite pour les réintégrer dans la branche principale ?


![Image](https://lh4.googleusercontent.com/1mzTfQy7U1z6hMtin6JHIpJofRSoeElpHJcflmFIE2niq16PP-GlqWn6ebw1O0TKTmivUVJPOh3oaCc6sVOB751x3TDJNDVgXiVgmVMb2zu3kw9bDHXffG15bLA6uaWb7nqKwRMQ9nIqdhHgaqT64EU)
_Illustration de git, avec un commit supplémentaire sur votre branche_

Eh bien, vous avez deux options. La première est une commande que vous connaissez probablement si vous avez déjà utilisé Git : git merge. Le résultat final ressemble un peu à ceci.

![Image](https://lh5.googleusercontent.com/S4eILyjWjxrmlBThz1q2wKQgSddVJ0QGkGTUiDP2y_f3TX1NoMNRfVkmklgmLDICBeRyBPVUOdeD7HbGs6HzSszEv01pXl8TWxhLSEKq44MVsVqWIYcJSec85gkfO53B9sUCRc9MA3I9mgOfetVHYu4)
_Illustration de git, avec un commit de fusion supplémentaire_

Comme vous pouvez le voir, nous avons un commit supplémentaire juste pour la fusion. L'historique se poursuit à partir de là, et c'est bien ! De nombreux codeurs s'en sortent très bien en utilisant des commits de fusion. Mais que se passe-t-il si vous avez une branche de longue durée que vous devez maintenir à jour ?

Dans ce cas, nous travaillons sur une branche nommée `foo`. Nos commits sont ceux avec les commentaires, `some other thing`, `adding test`, et `addressing comments`. Jetez un coup d'œil à ce à quoi ressemble l'historique.

![Image](https://lh3.googleusercontent.com/RVMAGg4oPs1DSX6gFjo1CClg4Vtl6uLmc_-sWsb9dkw-5bxPRTWkSVPVR7C-vCLobok6kpWU942RtRJPwq8xP_p5HuA0mJSdrH7dxLJwhlj2oZjhx29RTvrTswKf0eSqOUF3jz2HFqu8vSQkPkQchDI)
_Historique Git avec fusion_

Ces commits `Merge branch 'main' into foo` ne semblent pas très utiles - ils sont simplement logistiques et ne décrivent pas réellement les modifications que vous apportez à votre branche. Il est également un peu difficile de raisonner sur les modifications consécutives que vous avez apportées à votre branche actuelle lorsque vous regardez votre historique Git.

### Comment effectuer le rebase

Explorons l'alternative avec git rebase. En reprenant le même exemple ci-dessus, commençons par notre dernier commit juste avant d'être prêt à fusionner à nouveau dans `main`.

![Image](https://lh4.googleusercontent.com/1mzTfQy7U1z6hMtin6JHIpJofRSoeElpHJcflmFIE2niq16PP-GlqWn6ebw1O0TKTmivUVJPOh3oaCc6sVOB751x3TDJNDVgXiVgmVMb2zu3kw9bDHXffG15bLA6uaWb7nqKwRMQ9nIqdhHgaqT64EU)
_Le cas de base_

Cette fois, nous allons faire un git rebase. Cela va effectivement rejouer vos commits **par-dessus** les nouveaux commits (connus sous le nom de HEAD) de `main`, évitant ainsi les commits de fusion.

![Image](https://lh5.googleusercontent.com/0sbSYMp0Xhbod-lkHDr-24wrB4NWov857B7C_vnpkQlM7bTq1qFbGMcWqfYrDHWDs1lHlxm9ZyLJaRfRr0pmcqVf7nfe_siDLv0dWdq2ZtoCUboChjR_9SzAAtMOVapYaK3kF40E3CY_qrbEveA6_jk)
_Illustration du rebasage_

Alors, comment accomplissons-nous cela ? Tout en étant sur votre branche secondaire (dans notre cas, `foo`), vous voudrez faire ce qui suit.

1. Passez à votre branche `main` avec `git checkout main`
2. Mettez à jour votre branche locale `main` avec `git pull`. Cela permet d'avoir le dernier HEAD de `main` disponible pour le rebase.
3. Revenez à votre branche `foo` avec `git checkout foo`
4. Utilisez `git rebase main`, cela complétera le rebase, en rejouant vos commits par-dessus le HEAD de `main`.

En comparaison avec l'exemple précédent, à quoi cela ressemble-t-il avec les mêmes commits "some other thing", "adding test", et "addressing comments" ?

![Image](https://lh5.googleusercontent.com/aS-mY0pqWfzcT-uIvvILDMouHOys4MEtiORn_jpVk479QVopePBM-2h4YwiW4Do5k7127Gkb_dbYfWuGyr508Te2ISmsWQgEgSRK3qxY82pNnb6b9mjIc7yxQJS7gNuypru_-zjPBdNFD9uBhxpUMvg)
_Historique des commits plus propre avec git rebase_

Très bien ! C'est plus propre, et en regardant l'historique de ma branche, il est assez simple de raisonner sur les modifications de ma branche. Je n'ai besoin de savoir que par où j'ai commencé (hash de commit `2a2db46`).

## Bonnes pratiques de Rebase

Bien que git rebase garde sans aucun doute votre historique de commits plus propre, il y a quelques points à garder à l'esprit :

* Utilisez rebase **uniquement** pour les branches locales. **Ne rebasez pas les branches sur lesquelles d'autres personnes travaillent.** Rebase _modifie_ l'historique des commits, et les autres ne seront pas au courant.
* Récupérez et rebasez régulièrement vos branches locales pour rester à jour avec la branche principale. Les conflits deviennent compliqués ! Rebases tôt et souvent.

## Conclusion

Bien qu'il soit facile de se laisser emporter par les nouvelles technologies en plein essor telles que les [outils d'intelligence artificielle](https://nickabbene.com/best-ai-productivity-tools) et le [edge computing](https://www.forbes.com/sites/forbestechcouncil/2023/03/17/top-six-edge-computing-trends-to-know-about-in-2023/?sh=4b239b886754), il est également important pour nous, en tant que développeurs, de faire un pas en arrière et de nous assurer que nous utilisons des outils éprouvés comme Git à leur plein potentiel.

Dans cet article, nous avons examiné `git rebase`, et donné un exemple de pourquoi le rebasage pourrait être un bon outil dans votre boîte à outils.

Bon rebasage !