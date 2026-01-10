---
title: 'Introduction à Git merge et rebase : ce qu''ils sont et comment les utiliser'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-14T17:00:10.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-git-merge-and-rebase-what-they-are-and-how-to-use-them-131b863785f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9LlKBmfWia1Uou0ubjWkzg.jpeg
tags:
- name: Git
  slug: git
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
seo_title: 'Introduction à Git merge et rebase : ce qu''ils sont et comment les utiliser'
seo_desc: 'By Vali Shah

  As a Developer, many of us have to choose between Merge and Rebase. With all the
  references we get from the internet, everyone believes “Don’t use Rebase, it could
  cause serious problems.” Here I will explain what merge and rebase are, w...'
---

Par Vali Shah

En tant que développeur, beaucoup d'entre nous doivent choisir entre Merge et Rebase. Avec toutes les références que nous obtenons sur Internet, tout le monde croit « Ne pas utiliser Rebase, cela pourrait causer de sérieux problèmes. » Ici, je vais expliquer ce que sont merge et rebase, pourquoi vous devriez (et ne devriez pas) les utiliser, et comment le faire.

Git Merge et Git Rebase servent le même but. Ils sont conçus pour intégrer les changements de plusieurs branches en une seule. Bien que le but final soit le même, ces deux méthodes l'atteignent de différentes manières, et il est utile de connaître la différence en devenant un [meilleur développeur logiciel](https://www.microverse.org).

Cette question a divisé la communauté Git. Certains croient que vous devriez toujours rebase et d'autres que vous devriez toujours merge. Chaque côté a des avantages convaincants.

### Git Merge

La fusion est une pratique courante pour les développeurs utilisant des systèmes de contrôle de version. Que les branches soient créées pour des tests, des corrections de bugs ou d'autres raisons, la fusion commite les changements vers un autre emplacement. Pour être plus précis, la fusion prend le contenu d'une branche source et l'intègre avec une branche cible. Dans ce processus, seule la branche cible est modifiée. L'historique de la branche source reste le même.

![Image](https://cdn-media-1.freecodecamp.org/images/VonhijTBQgjwtRXz31wLzF7iWDnDFk2o8EWi)
_Fusion Master -> Branche de fonctionnalité_

#### **Avantages**

* Simple et familier
* Préserve l'historique complet et l'ordre chronologique
* Maintient le contexte de la branche

#### **Inconvénients**

* L'historique des commits peut devenir pollué par de nombreux commits de fusion
* Le débogage utilisant `git bisect` peut devenir plus difficile

#### **Comment faire**

Fusionnez la branche master dans la branche de fonctionnalité en utilisant les commandes `checkout` et `merge`.

```bash
$ git checkout feature
$ git merge master

(ou)

$ git merge master feature
```

Cela créera un nouveau « **Commit de fusion** » dans la branche de fonctionnalité qui contient l'historique des deux branches.

### Git Rebase

Rebase est une autre façon d'intégrer les changements d'une branche à une autre. Rebase compresse tous les changements en un seul « patch ». Ensuite, il intègre le patch sur la branche cible.

Contrairement à la fusion, le rebase aplatit l'historique car il transfère le travail terminé d'une branche à une autre. Dans le processus, l'historique indésirable est éliminé.

> _Les rebases sont la façon dont les changements doivent passer du haut de la hiérarchie vers le bas, et les fusions sont la façon dont ils remontent vers le haut_

![Image](https://cdn-media-1.freecodecamp.org/images/aEjZMJ6s4rDVqzXveqgLrwkQ0RJEvOTjAIUc)
_Rebase de la branche de fonctionnalité dans master_

#### **Avantages**

* Simplifie un historique potentiellement complexe
* Manipuler un seul commit est facile (par exemple, les annuler)
* Évite le « bruit » des commits de fusion dans les dépôts et branches actifs
* Nettoie les commits intermédiaires en les regroupant en un seul commit, ce qui peut être utile pour les équipes DevOps

#### **Inconvénients**

* Réduire la fonctionnalité à quelques commits peut masquer le contexte
* Le rebase des dépôts publics peut être dangereux lorsque l'on travaille en équipe
* C'est plus de travail : utiliser rebase pour garder votre branche de fonctionnalité à jour
* Le rebase avec des branches distantes vous oblige à faire un _force push_. Le plus gros problème auquel les gens sont confrontés est qu'ils font un force push mais n'ont pas défini git push default. Cela entraîne des mises à jour de toutes les branches portant le même nom, à la fois localement et à distance, et c'est **terrible** à gérer.

> _Si vous rebased incorrectement et réécrivez l'historique par inadvertance, cela peut entraîner de sérieux problèmes, alors assurez-vous de savoir ce que vous faites !_

#### **Comment faire**

Rebasez la branche de fonctionnalité sur la branche master en utilisant les commandes suivantes.

```
$ git checkout feature
$ git rebase master
```

Cela déplace toute la branche de fonctionnalité au-dessus de la branche master. Il le fait en réécrivant l'historique du projet en créant de nouveaux commits pour chaque commit dans la branche originale (feature).

#### **Rebase interactif**

Cela permet de modifier les commits lorsqu'ils sont déplacés vers la nouvelle branche. Cela est plus puissant que le rebase automatique, car il offre un contrôle complet sur l'historique des commits de la branche. Typiquement, cela est utilisé pour nettoyer un historique désordonné avant de fusionner une branche de fonctionnalité dans master.

```
$ git checkout feature
$ git rebase -i master
```

Cela ouvrira l'éditeur en listant tous les commits qui sont sur le point d'être déplacés.

```bash
pick 22d6d7c Message de commit #1
pick 44e8a9b Message de commit #2
pick 79f1d2h Message de commit #3
```

Cela définit exactement à quoi la branche ressemblera après que le rebase soit effectué. En réorganisant les entités, vous pouvez faire en sorte que l'historique ressemble à ce que vous voulez. Par exemple, vous pouvez utiliser des commandes comme `fixup`, `squash`, `edit`, etc., à la place de `pick`.

![Image](https://cdn-media-1.freecodecamp.org/images/c0OgwrajpcLfLs75zq0mF5DP3sTBQ-oLjU02)

### Lequel utiliser

Alors, qu'est-ce qui est le mieux ? Que recommandent les experts ?

Il est difficile de généraliser et de décider pour l'un ou l'autre, car chaque équipe est différente. Mais nous devons commencer quelque part.

Les équipes doivent considérer plusieurs questions lors de la définition de leurs politiques Git rebase vs. merge. Car il s'avère qu'une stratégie de flux de travail n'est pas meilleure que l'autre. Cela dépend de votre équipe.

Considérez le niveau de rebase et de compétence Git dans votre organisation. Déterminez dans quelle mesure vous valorisez la simplicité du rebase par rapport à la traçabilité et à l'historique de la fusion.

Enfin, les décisions concernant la fusion et le rebase doivent être considérées dans le contexte d'une stratégie de branchement claire (**Voir** [**cet article**](https://medium.freecodecamp.org/adopt-a-git-branching-strategy-ac729ff4f838) pour mieux comprendre la stratégie de branchement). Une stratégie de branchement réussie est conçue autour de l'organisation de vos équipes.

### Que recommandé-je ?

À mesure que l'équipe grandit, il deviendra difficile de gérer ou de tracer les changements de développement avec une **politique de fusion toujours**. Pour avoir un historique de commits propre et compréhensible, utiliser **Rebase** est raisonnable et efficace.

En considérant les circonstances et les directives suivantes, vous pouvez tirer le meilleur parti de **Rebase** :

* **Vous développez localement** : Si vous n'avez pas partagé votre travail avec quelqu'un d'autre. À ce stade, vous devriez préférer le rebase à la fusion pour garder votre historique propre. Si vous avez votre propre fork du dépôt et qu'il n'est pas partagé avec d'autres développeurs, vous pouvez rebase en toute sécurité même après avoir poussé vers votre branche.
* **Votre code est prêt pour la révision** : Vous avez créé une pull request. D'autres examinent votre travail et le récupèrent potentiellement dans leur fork pour une révision locale. À ce stade, vous ne devriez pas rebase votre travail. Vous devriez créer des commits de 'rework' et mettre à jour votre branche de fonctionnalité. Cela aide à la traçabilité dans la pull request et empêche la rupture accidentelle de l'historique.
* **La révision est terminée et prête à être intégrée dans la branche cible.** Félicitations ! Vous êtes sur le point de supprimer votre branche de fonctionnalité. Étant donné que d'autres développeurs ne feront pas de fetch-merge de ces changements à partir de ce point, c'est votre chance de nettoyer votre historique. À ce stade, vous pouvez réécrire l'historique et regrouper les commits originaux et ces commits de 'pr rework' et de 'merge' en un petit ensemble de commits ciblés. Créer une fusion explicite pour ces commits est optionnel, mais a de la valeur. Cela enregistre quand la fonctionnalité a été intégrée à master.

### Conclusion

J'espère que cette explication a donné quelques insights sur **Git merge** et **Git rebase**. La stratégie merge vs rebase est toujours débattable. Mais peut-être que cet article vous aidera à dissoudre vos doutes et à adopter une approche qui fonctionne pour votre équipe.

J'ai hâte d'écrire sur les **flux de travail Git** et les concepts de **Git**. Commentez les sujets que vous souhaitez que j'aborde ensuite. Santé !

`**code** = **caf**éfé + **dé**veloppeur`

[école de codage pour développeurs logiciels](https://www.microverse.org/)

![Image](https://cdn-media-1.freecodecamp.org/images/imcvBz4swIFiLs19gCb7EiWDFbtWOA9hFGmb)