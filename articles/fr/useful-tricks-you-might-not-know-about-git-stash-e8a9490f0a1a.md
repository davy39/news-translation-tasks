---
title: Astuces utiles que vous ne connaissez peut-être pas sur Git stash
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-26T18:43:32.000Z'
originalURL: https://freecodecamp.org/news/useful-tricks-you-might-not-know-about-git-stash-e8a9490f0a1a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KDah4xyJW5PtPuN6LOlFiQ.png
tags:
- name: General Programming
  slug: programming
- name: software
  slug: software
- name: software development
  slug: software-development
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
seo_title: Astuces utiles que vous ne connaissez peut-être pas sur Git stash
seo_desc: 'By Srebalaji Thirumalai


  I have launched a newsletter Git Better to help learn new tricks and advanced topics
  of Git. If you are interested in getting your game better in Git, you should definitely
  check that out.


  If you have been using Git for a wh...'
---

Par Srebalaji Thirumalai

> **J'ai lancé une newsletter [Git Better](https://gitbetter.substack.com/) pour aider à apprendre de nouvelles astuces et des sujets avancés de Git. Si vous êtes intéressé à améliorer votre maîtrise de Git, vous devriez définitivement y jeter un coup d'œil.**

Si vous utilisez Git depuis un certain temps, vous avez peut-être utilisé Git stash. C'est l'une des fonctionnalités utiles de Git.

Voici quelques astuces utiles que j'ai apprises sur Git stash la semaine dernière.

1. Git stash save
2. Git stash list
3. Git stash apply
4. Git stash pop
5. Git stash show
6. Git stash branch <nom>
7. Git stash clear
8. Git stash drop

#### **Git stash save**

Cette commande est similaire à Git stash. Mais cette commande vient avec diverses options. Je vais discuter de quelques options importantes dans cet article.

**Git stash avec message**

```bash
git stash save "Votre message de stash".
```

La commande ci-dessus stocke avec un message. Nous verrons comment cela est utile dans un instant.

**Stocker des fichiers non suivis**

Vous pouvez également stocker des fichiers non suivis.

```bash
git stash save -u

ou

git stash save --include-untracked
```

#### **Git stash list**

Avant de discuter de cette commande, laissez-moi vous dire quelque chose sur le fonctionnement de stash.

Lorsque vous utilisez Git stash ou Git stash save, Git crée en réalité un objet de commit Git avec un nom et l'enregistre dans votre dépôt.

Cela signifie que vous pouvez voir la liste des stashes que vous avez faits à tout moment.

```bash
git stash list
```

Voir l'exemple ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/757jZHhanVirv5F5ZBeTXi2XNVPyAhOmDgwV)
_exemple de git stash list_

Vous pouvez voir la liste des stashes effectués. Le stash le plus récent est en haut.

Et vous pouvez voir que le stash du haut est donné avec un message personnalisé (en utilisant Git stash save "message").

#### **Git stash apply**

Cette commande prend le stash le plus récent dans la pile et l'applique au dépôt. Dans notre cas, il s'agit de **stash@{0}**

Si vous voulez appliquer un autre stash, vous pouvez spécifier l'identifiant du stash.

Voici l'exemple :

```bash
git stash apply stash@{1}
```

#### **Git stash pop**

Cette commande est très similaire à stash apply mais elle supprime le stash de la pile après l'avoir appliqué.

Voici l'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/NrqQy5PTwIBRxvQ2WnlY09EV3ayd7DTbr2k9)
_exemple de Git stash pop_

Comme vous pouvez le voir, le stash du haut est supprimé et **stash@{0}** est mis à jour avec l'ancien stash.

De même, si vous voulez faire éclater un stash particulier, vous pouvez spécifier l'identifiant du stash.

```bash
git stash pop stash@{1}
```

#### **Git stash show**

Cette commande montre le résumé des différences du stash. La commande ci-dessus ne considère que le dernier stash.

Voici l'exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/W6tFM8O0xrUfFznYg9O-mvAND4zNDX2R-RFc)
_exemple de Git stash show_

Si vous voulez voir le diff complet, vous pouvez utiliser

```bash
git stash show -p
```

De même, avec d'autres commandes, vous pouvez également spécifier l'identifiant du stash pour obtenir le résumé des différences.

```bash
git stash show stash@{1}
```

#### **Git stash branch <nom>**

Cette commande crée une nouvelle branche avec le dernier stash, puis supprime le dernier stash (comme stash pop).

Si vous avez besoin d'un stash particulier, vous pouvez spécifier l'identifiant du stash.

```bash
git stash branch <nom> stash@{1}
```

Cela sera utile lorsque vous rencontrez des conflits après avoir appliqué le stash à la dernière version de votre branche.

#### **Git stash clear**

Cette commande supprime tous les stashes effectués dans le dépôt. Il peut être impossible de revenir en arrière.

#### **Git stash drop**

Cette commande supprime le dernier stash de la pile. Mais utilisez-la avec prudence, il peut être difficile de revenir en arrière.

Vous pouvez également spécifier l'identifiant du stash.

```bash
git stash drop stash@{1}
```

J'espère que vous avez appris quelques astuces utiles sur Git stash.

> Si vous êtes arrivé jusqu'ici, alors je pense que vous êtes assez intéressé par Git. Consultez ma newsletter [Git Better](https://gitbetter.substack.com/) pour apprendre de nouvelles astuces et des sujets avancés de Git. :)

Si vous avez aimé l'article, essayez de donner quelques applaudissements et de le partager :) :)