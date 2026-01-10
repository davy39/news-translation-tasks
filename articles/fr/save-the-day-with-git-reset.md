---
title: Git Reset Expliqué – Comment Sauver la Situation avec la Commande Reset
subtitle: ''
author: Omer Rosenbaum
co_authors: []
series: null
date: '2020-09-28T15:55:59.000Z'
originalURL: https://freecodecamp.org/news/save-the-day-with-git-reset
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9882740569d1a4ca1a78.jpg
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
- name: version control
  slug: version-control
seo_title: Git Reset Expliqué – Comment Sauver la Situation avec la Commande Reset
seo_desc: 'Does this sound familiar? “Help! I committed to the wrong branch!” “It
  happened again… Where is my commit?”

  Well, I’ve been there so many times. Someone calls my name for help when something
  goes wrong with git. And it has happened not only when I wa...'
---

Cela vous dit quelque chose ? « Aidez-moi ! J'ai commis sur la mauvaise branche ! » « C'est arrivé encore… Où est mon commit ? »

Eh bien, j'ai été là tant de fois. Quelqu'un m'appelle à l'aide quand quelque chose ne va pas avec `git`. Et cela s'est produit non seulement quand j'enseignais aux étudiants, mais aussi en travaillant avec des développeurs expérimentés.

Avec le temps, je suis devenu « le gars Git ».

Nous utilisons `git` tout le temps, et généralement, cela nous aide à faire le travail. Mais parfois, et bien plus souvent que nous ne le souhaiterions, les choses tournent mal.

Peut-être avons-nous commis sur la mauvaise branche. Peut-être avons-nous perdu du code que nous avons écrit. Peut-être avons-nous commis quelque chose que nous ne voulions pas.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/xkcd_comic.png)
_Source : xkcd.com_

Il existe de nombreuses ressources en ligne sur `git`, et certaines d'entre elles ([comme celle-ci](https://ohshitgit.com/)) se concentrent réellement sur ce qui se passe dans ces scénarios indésirables.

Mais j'ai toujours trouvé que ces ressources manquaient le « pourquoi ». Lorsqu'on fournit un ensemble de commandes, que fait chaque commande ? Et comment en êtes-vous arrivé à ces commandes en premier lieu ? ?

Dans [un précédent article, j'ai fourni une introduction visuelle aux internes de Git](https://medium.com/swimm/a-visualized-intro-to-git-internals-objects-and-branches-68df85864037). Bien que comprendre les internes de `git` soit utile, la théorie seule est presque jamais suffisante. Comment appliquons-nous nos connaissances des internes de `git` et les utilisons-nous pour résoudre les problèmes dans lesquels nous nous sommes mis ?

Dans cet article, je souhaite combler cette lacune et élaborer sur la commande `git reset`. Nous allons comprendre ce que `git reset` fait en coulisses, puis appliquer cette connaissance pour résoudre divers scénarios. ?

## Bases communes – répertoire de travail, index et dépôt

Pour comprendre les mécanismes internes de `git reset`, il est important de comprendre le processus d'enregistrement des changements dans `git`. Plus précisément, je veux parler du **répertoire de travail**, de l'**index** et du **dépôt**.

Si vous êtes à l'aise avec ces termes, n'hésitez pas à passer à la section suivante. Si vous souhaitez une explication encore plus approfondie, consultez cet [article précédent](https://medium.com/swimm/a-visualized-intro-to-git-internals-objects-and-branches-68df85864037).

Lorsque nous travaillons sur notre code source, nous travaillons à partir d'un **répertoire de travail** – tout répertoire sur notre système de fichiers qui a un **dépôt** associé. Il contient les dossiers et fichiers de notre projet, ainsi qu'un répertoire appelé `.git`.

Après avoir apporté des modifications, nous voulons les enregistrer dans notre **dépôt**. Un **dépôt** (ou **repo** en abrégé) est une collection de **commits**, chacun d'eux étant une archive de l'apparence de l'**arbre de travail** du projet à une date passée, que ce soit sur notre machine ou celle de quelqu'un d'autre.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/1-2.png)

Créons un fichier dans le répertoire de travail et exécutons `git status` :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/2-4.png)

Cependant, `git` ne commet pas les changements de l'**arbre de travail** directement dans le **dépôt**.

Au lieu de cela, les changements sont d'abord enregistrés dans quelque chose appelé l'**index**, ou la **zone de staging**. Ces deux termes désignent la même chose, et ils sont souvent utilisés dans la documentation de `git`. Nous utiliserons ces termes de manière interchangeable tout au long de cet article.

Lorsque nous utilisons `git add`, nous ajoutons des fichiers (ou des changements dans des fichiers) à la **zone de staging**. Utilisons cette commande sur le fichier que nous avons créé précédemment :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/3-2.png)

Comme le révèle `git status`, notre fichier est **staged** (et prêt « à être commis »). Cependant, il ne fait pas partie d'un **commit**. En d'autres termes, il est maintenant dans le **répertoire de travail**, ainsi que dans l'**index**, mais pas dans le **dépôt**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/6-3.png)

Ensuite, lorsque nous utilisons `git commit`, nous créons un **commit** basé sur l'état de l'**index**. Ainsi, le nouveau **commit** (commit 3 dans l'exemple ci-dessous) inclura le fichier ajouté à l'index au préalable.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/7-2.png)

En d'autres termes, le **répertoire de travail** a exactement le même état que l'**index** et le **dépôt**.

La commande `git commit` fait également pointer la branche actuelle `master` vers le nouvel objet **commit** créé.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/8-2.png)

## Le fonctionnement interne de git reset

J'aime penser à `git reset` comme une commande qui inverse le processus décrit ci-dessus (introduire un changement dans le **répertoire de travail**, l'ajouter à l'**index**, puis le **commit** dans le **dépôt**).

Git reset a trois modes de fonctionnement – `--soft`, `--mixed`, ou `--hard`. Je les vois comme trois étapes :

* Étape 1 – mettre à jour `HEAD` – `git reset --soft`
* Étape 2 – mettre à jour **index** – `git reset --mixed`
* Étape 3 – mettre à jour **répertoire de travail** – `git reset --hard`

### Étape 1 – mettre à jour `HEAD` (`git reset --soft`)

Tout d'abord, `git reset` met à jour ce que `HEAD` pointe. Pour `git reset --hard HEAD~1`, il déplacera ce que `HEAD` pointe (dans l'exemple ci-dessus, `master`) vers `HEAD~1`. Si le drapeau `--soft` est utilisé, `git reset` s'arrête là.

En continuant avec notre exemple ci-dessus, `HEAD` pointera vers `commit 2`, et ainsi `new_file.txt` ne fera pas partie de l'arbre du commit actuel. Il fera cependant partie de l'**index** et du **répertoire de travail**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/9-2.png)

En regardant `git status`, nous pouvons voir que le fichier est effectivement staged mais pas commis :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/10-2.png)

En d'autres termes, nous avons rétabli le processus à l'étape où nous avons utilisé `git add`, mais nous n'avons pas encore utilisé `git commit`.

### Étape 2 – mettre à jour l'index vers HEAD (`git reset --mixed`)

Si nous utilisons `git reset --mixed HEAD~1`, alors `git` ne s'arrêtera pas après avoir mis à jour ce que `HEAD` pointe ( `master` ) vers `HEAD~1`. Il mettra également à jour l'**index** vers (le déjà mis à jour) `HEAD`.

Dans notre exemple, cela signifie que l'**index** aura le même état que **commit 2** :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/11-1.png)

Nous avons donc rétabli le processus à l'étape avant d'utiliser `git add` – le fichier nouvellement créé fait maintenant partie du répertoire de travail, mais pas de l'**index** ni du **dépôt**.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/12-1.png)

### Étape 3 – mettre à jour le répertoire de travail vers l'index (`git reset --hard`)

En utilisant `git reset --hard HEAD~1`, après avoir mis à jour ce que `HEAD` pointe (`master`) vers `HEAD~1`, ainsi que la mise à jour de l'**index** vers (le déjà mis à jour) `HEAD`, `git` passera à la mise à jour du **répertoire de travail** pour qu'il ressemble à l'**index**.

Dans notre exemple, cela signifie que le **répertoire de travail** aura le même état que l'**index**, qui a déjà le même état que **commit 2** :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/13-1.png)

En fait, nous avons rétabli l'ensemble du processus même avant la création de `my_file.txt`.

## Appliquer nos connaissances à des scénarios réels

Maintenant que nous comprenons comment `git reset` fonctionne, appliquons cette connaissance pour sauver notre journée ! ?

### 1. OOPS ! J'ai commis quelque chose par erreur.

Considérons le scénario suivant. Nous avons créé un fichier avec la chaîne `This is very importnt`, l'avons staged et commis.

![Image](https://www.freecodecamp.org/news/content/images/2020/09/14-1.png)

Et puis… Oups ! Nous nous sommes rendu compte que nous avions fait une erreur de frappe. ?

Eh bien, maintenant nous savons que nous pouvons facilement résoudre cela. Nous pouvons annuler notre dernier commit et récupérer le fichier dans le répertoire de travail en utilisant `git reset --mixed HEAD~1`. Maintenant, nous pouvons éditer le contenu de notre fichier, le stager et le commiter à nouveau.

**Astuce :** dans ce cas spécifique, nous pourrions également utiliser `git commit --amend`, comme décrit [ici](https://medium.com/@igor_marques/git-basics-adding-more-changes-to-your-last-commit-1629344cb9a8).

### 2. OOPS ! J'ai commis quelque chose sur la mauvaise branche – et j'en ai besoin sur une nouvelle branche

Nous avons tous été là. Nous avons fait du travail, puis l'avons commis…

![Image](https://www.freecodecamp.org/news/content/images/2020/09/15-1.png)

Oh non, nous avons commis sur la branche `master`, alors que nous aurions dû créer une nouvelle branche puis faire une pull request. ?

À ce stade, je trouve utile de visualiser l'état dans lequel nous nous trouvons et où nous aimerions être :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/16.png)

En fait, il y a trois changements entre l'état actuel et l'état souhaité.

Tout d'abord, la branche `new` pointe vers notre commit récemment ajouté. Ensuite, `master` pointe vers le commit précédent. Enfin, `HEAD` pointe vers `new`.

Nous pouvons atteindre l'état souhaité en trois étapes simples :

Tout d'abord, faire pointer la branche `new` vers le commit récemment ajouté – cela peut être simplement réalisé en utilisant `git branch new`. Nous atteignons donc l'état suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/17.png)

Ensuite, faire pointer `master` vers le commit précédent (en d'autres termes, vers `HEAD~1`). Nous pouvons faire cela en utilisant `git reset --hard HEAD~1`. Nous atteignons donc l'état suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/18.png)

Enfin, nous aimerions être sur la branche `new`, c'est-à-dire faire pointer `HEAD` vers `new`. Cela est facilement réalisé en effectuant `git checkout new`.

En résumé :

* `git branch new`
* `git reset --hard HEAD~1`
* `git checkout new`

### 3. OOPS ! J'ai commis quelque chose sur la mauvaise branche – et j'en ai besoin sur une autre branche déjà existante

Dans ce cas, nous avons suivi les mêmes étapes que dans le scénario précédent – nous avons fait du travail, puis l'avons commis…

![Image](https://www.freecodecamp.org/news/content/images/2020/09/19.png)

Oh non, nous avons commis sur la branche `master`, alors que nous aurions dû commiter sur une autre branche qui existe déjà. ?

Retournons à notre tableau de dessin :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/20.png)

Encore une fois, nous pouvons voir qu'il y a quelques différences ici.

Tout d'abord, nous avons besoin du commit le plus récent sur la branche `existing`. Puisque `master` pointe actuellement dessus, nous pouvons simplement demander à `git` de prendre le commit récent de la branche `master` et de l'appliquer à la branche `existing` comme suit :

* `git checkout existing` – basculer vers la branche `existing`
* `git cherry-pick master` – appliquer le dernier commit de la branche `master` à la branche actuelle (`existing`)

Maintenant, nous avons atteint l'état suivant :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/21.png)

Maintenant, nous devons simplement faire pointer `master` vers le commit précédent, plutôt que le dernier. Pour cela, nous pouvons :

* `git checkout master` – changer la branche active vers `master` à nouveau.
* `git reset --hard HEAD~1` – maintenant nous sommes de retour à la branche d'origine.

Et nous avons atteint notre état souhaité :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/22.png)

## Résumé

Dans cet article, nous avons appris comment `git reset` fonctionne et clarifié ses trois modes de fonctionnement – `--soft`, `--mixed` et `--hard`.

Nous avons ensuite appliqué nos connaissances sur `git reset` pour résoudre certains problèmes réels avec `git`.

En comprenant le fonctionnement de `git`, nous pouvons aborder en toute confiance tous types de scénarios et apprécier la beauté de cet outil ?

Dans de futurs articles, nous couvrirons des commandes `git` supplémentaires et comment elles peuvent nous aider à résoudre toutes sortes de situations indésirables.

[_Omer Rosenbaum_](https://www.linkedin.com/in/omer-rosenbaum-034a08b9/), _Directeur Technique de_ [_Swimm_](https://swimm.io). _Expert en formation cybernétique et fondateur de Checkpoint Security Academy. Auteur de_ [_Computer Networks (en hébreu)_](https://data.cyber.org.il/networks/networks.pdf). _Visitez ma_ [_Chaîne YouTube_](https://www.youtube.com/watch?v=79jlgESHzKQ&list=PL9lx0DXCC4BMS7dB7vsrKI5wzFyVIk2Kg).

### Ressources supplémentaires

* [Série Brève sur les Internes de Git sur YouTube](https://www.youtube.com/watch?v=fWMKue-WBok&list=PL9lx0DXCC4BNUby5H58y6s2TQVLadV8v7)
* [Une Introduction Visualisée aux Internes de Git – Objets et Branches](https://medium.com/swimm/a-visualized-intro-to-git-internals-objects-and-branches-68df85864037)
* [Devenir Hardcore – Créer un Dépôt à partir de Zéro](https://medium.com/swimm/getting-hardcore-creating-a-repo-from-scratch-cc747edbb11c)
* [Outils Git – Reset Démystifié (du Livre Pro Git)](https://git-scm.com/book/en/v2/Git-Tools-Reset-Demystified)