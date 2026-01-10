---
title: Comment visualiser les commandes Git confuses avec Git-Sim
subtitle: ''
author: Jacob Stopak
co_authors: []
series: null
date: '2023-01-23T14:57:06.000Z'
originalURL: https://freecodecamp.org/news/git-sim
coverImage: https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-44-46-1.jpg
tags:
- name: Git
  slug: git
- name: version control
  slug: version-control
seo_title: Comment visualiser les commandes Git confuses avec Git-Sim
seo_desc: 'Git is an essential tool for developers to learn in order to effectively
  collaborate on source code. But certain Git concepts and commands are notoriously
  difficult for devs to learn.

  Not only that, but Git commands often have nuances that lead to va...'
---

Git est un outil essentiel pour les développeurs à apprendre afin de collaborer efficacement sur le code source. Mais certains concepts et commandes Git sont notoirement difficiles à apprendre pour les développeurs.

Non seulement cela, mais les commandes Git ont souvent des nuances qui conduisent à des résultats variés sur l'état de votre dépôt local. De plus, même une fois que vous avez appris une commande Git spécifique, vous pourriez ne pas utiliser cette commande pendant un laps de temps significatif avant d'en avoir à nouveau besoin.

Cela conduit les développeurs à rechercher à plusieurs reprises sur Google ou Stackoverflow des commandes Git spécifiques à des situations, encore et encore, en priant pour que des résultats parallèles se produisent lors de l'exécution de la commande localement.

Cela se produit couramment avec des commandes Git notoirement confuses telles que `git reset`, `git merge`, et `git rebase`.

Dans cet article, nous allons fournir un aperçu de ces 3 commandes en utilisant un outil en ligne de commande appelé [Git-Sim pour simuler visuellement les opérations Git dans votre dépôt local](https://initialcommit.com/blog/git-sim). Cet outil nous permettra de créer facilement des diagrammes et des animations pratiques illustrant comment chaque commande Git affectera l'état de votre propre dépôt Git.

## `git reset` – Comment réinitialiser Git HEAD tout en gérant les changements

La [commande git reset](https://initialcommit.com/blog/git-reset) est une commande que je me surprends constamment à rechercher sur Google avant de devoir l'utiliser.

Cela est en partie dû au fait qu'il existe plusieurs commandes que vous pouvez utiliser pour [annuler les changements dans Git](https://initialcommit.com/blog/undoing-changes-in-git), et je veux m'assurer de choisir la bonne.

De plus, toute commande qui pourrait accidentellement conduire à "perdre du travail", comme `git reset --hard`, vaut la peine de prendre quelques secondes au préalable pour s'assurer que vous êtes confiant dans ce que vous êtes sur le point de faire.

### Que fait `git reset` ?

En résumé, git reset déplace simplement la pointe de la branche actuelle vers un commit précédent. En ce sens, il peut être utilisé pour "annuler" les changements appliqués par les commits entre le commit actuel et le commit vers lequel vous souhaitez réinitialiser.

Techniquement parlant, une branche Git est simplement un nom (ou une étiquette) qui pointe vers le commit le plus récent dans une chaîne de commits. Cela est déplacé vers l'avant chaque fois que vous faites un nouveau commit sur une branche, et identifie donc toujours ce que l'on appelle le commit **head de la branche**.

La commande `git reset` déplace cette étiquette de branche vers un commit précédent, qui devient le nouveau head de la branche – annulant effectivement tous les changements intermédiaires.

Considérons un exemple simple. Supposons que nous avons un dépôt qui ne suit qu'un seul fichier appelé `cheese.txt`. Le dépôt a 5 commits, chacun changeant le contenu textuel du fichier en un nom de fromage différent.

Nous pouvons illustrer cela visuellement en utilisant Git-Sim en exécutant la commande `$ git-sim log` pour simuler visuellement la sortie de la commande `$ git log` :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-33-17.jpg align="left")

*Note : nous avons en fait simulé cette* sortie `git log` en utilisant la commande git-sim `$ git-sim log`, qui dessine 5 commits dans l'image de sortie par défaut.

Comme vous pouvez le voir, nous avons une branche `main` pointant vers le commit avec l'ID `14c121...` avec le message de commit `Cheddar`.

Maintenant, disons que nous voulons annuler les commits changeant le contenu de `cheese.txt` en "cheddar" et "Swiss". Nous pouvons faire cela en utilisant la commande `git reset` pour réinitialiser la branche `main` de 2 commits, à "Gouda" :

```sh
$ git reset HEAD~2
```

Mais si nous ne sommes jamais sûrs de l'impact que cette commande aura, nous pouvons d'abord la simuler en utilisant Git-Sim :

```sh
$ git-sim reset HEAD~2
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-reset_01-05-23_09-34-16.jpg align="left")

Ou si vous préférez, la simulation peut être rendue sous forme de vidéo animée dynamique en utilisant le flag `--animate` de Git-Sim comme suit :

```sh
$ git-sim --animate reset HEAD~2
```

%[https://youtu.be/mJHdM6nTjb4]

Comme vous pouvez le voir, la sortie simulée de Git-Sim ci-dessus montre que la branche `main` et le pointeur `HEAD` sont réinitialisés de 2 commits en arrière vers le commit "Gouda".

De plus, nous pouvons voir que Git-Sim a créé un tableau avec 3 colonnes :

* **Changements supprimés de**

* **Modifications du répertoire de travail**

* **Zone de staging**

Par défaut, la commande `git reset` applique le comportement du flag `--mixed`, qui déplace tous les changements dans les commits réinitialisés vers le répertoire de travail.

Git-Sim reflète cela dans la sortie simulée ci-dessus en ajoutant le fichier `cheese.txt` dans la colonne **Modifications du répertoire de travail**.

Maintenant que vous avez simulé la commande `git reset` en utilisant Git-Sim et que vous pouvez clairement voir le résultat attendu dans l'image de sortie ci-dessus, vous pouvez exécuter la commande Git réelle `$ git reset HEAD~2` en toute confiance.

En plus de `--mixed`, Git-Sim comprend les réinitialisations `--soft` et `--hard`. La commande `$ git-sim reset --soft HEAD~2` garderait les changements annulés dans la colonne **Zone de staging**, tandis que la commande `$ git-sim reset --hard HEAD~2` placerait les changements annulés dans la colonne **Changements supprimés de** puisque une réinitialisation hard supprime les changements des fichiers committés.

Notez que `git reset` ne supprime jamais de commits (même lorsque vous utilisez l'option `--hard`), ce qui signifie que vous ne perdez aucun travail au moment de l'exécuter. Mais gardez à l'esprit que les commits peuvent devenir *orphelins*, ce qui signifie que certains commits deviennent inaccessibles par toute tête de branche. Git finira par les supprimer via le garbage collection, mais ils sont récupérables pendant un certain temps si vous en avez besoin !

## `git merge` – Comment fusionner les changements de plusieurs branches

La [commande git merge](https://initialcommit.com/blog/git-merge) est une autre commande délicate pour les utilisateurs débutants et intermédiaires de Git à comprendre. Il existe plusieurs types de fusions différents que Git effectue en fonction des circonstances.

Pour fournir une base, cette séquence de deux commandes met en évidence le fonctionnement de la syntaxe de fusion :

```sh
$ git checkout <fusion-dans>
$ git merge <fusion-de>
```

La première commande montre que la branche `<fusion-dans>` est la branche active que vous avez actuellement cochée dans votre répertoire de travail. Ensuite, lorsque vous exécutez la fusion, vous spécifiez `<fusion-de>` comme la branche à partir de laquelle vous souhaitez fusionner les changements, dans la branche active.

Par exemple, les commandes suivantes fusionneraient les changements de la branche `dev` dans `main` :

```sh
$ git checkout main
$ git merge dev
```

### Fusion trois-voies de Git

Le cas de fusion le plus courant se produit lorsque l'historique de deux branches a divergé et que le développeur souhaite recombiner les changements. Dans ce scénario, Git effectue ce que l'on appelle une **fusion trois-voies**.

Elle est appelée fusion trois-voies car Git utilise trois commits pour déterminer comment combiner les changements dans vos branches divergées :

* Le commit à la pointe de la branche A

* Le commit à la pointe de la branche B

* La base de fusion des deux branches

Nous pouvons utiliser Git-Sim pour simuler une fusion trois-voies qui fusionne les changements de deux nouveaux commits sur la branche `dev` dans `main` :

```sh
$ git checkout main
$ git-sim merge dev
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-44-46.jpg align="left")

*Sortie de fusion trois-voies dans Git-Sim*

Dans l'exemple ci-dessus, la pointe de la branche `main` avant la fusion est le commit `14c121` ("Cheddar"), et la pointe de la branche `dev` est `f42fee` ("Asiago"). Le troisième commit utilisé dans l'algorithme de fusion trois-voies de Git est le commit `640bb5` qui est la **base de fusion** des deux branches. Vous pouvez l'identifier en remontant les deux branches jusqu'à ce que vous trouviez le premier ancêtre commun.

En utilisant le contenu de ces 3 commits, Git crée un nouveau **commit de fusion** (étiqueté `abcdef` dans le diagramme Git-Sim ci-dessus) qui combine les changements des deux branches.

Contrairement aux commits réguliers, un commit de fusion a deux parents au lieu d'un, correspondant aux pointes des deux branches qui ont été fusionnées ensemble. Ces deux relations parentales sont désignées par les deux lignes pointillées dans l'image ci-dessus.

### Fusion rapide de Git

Une **fusion rapide** dans Git se produit lorsque la branche à partir de laquelle vous fusionnez est simplement plus avancée sur la même ligne de développement que la branche active. Considérez l'exemple ci-dessous :

```sh
$ git-sim log
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-49-08.jpg align="left")

Dans ce cas, les branches `dev` et `main` n'ont en fait pas divergé – elles se trouvent toutes deux sur la même ligne de développement. Par conséquent, si vous cochez la branche `dev` et essayez de fusionner `main`, Git n'a même pas besoin de fusionner le contenu des deux branches.

Au lieu de cela, Git peut simplement rediriger la référence de la branche `dev` vers le même commit que `main` pointe, qui est `14c121`. (Rappelez-vous qu'une branche dans Git est simplement une étiquette pointant vers un commit particulier).

Git-Sim sait également comment simuler ce type de fusion :

```sh
$ git checkout dev
$ git-sim merge main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-49-49.jpg align="left")

*Fusion rapide*

Notez qu'après avoir coché la branche `dev` et fusionné `main` dedans, l'étiquette de la branche `dev` a simplement été *avancée rapidement* vers le même commit que `main`, et aucun nouveau commit de fusion n'a été créé.

Cependant, dans certains cas, vous pourriez vouloir **forcer** Git à créer un commit de fusion même lors d'une fusion rapide.

Cela pourrait être utile si vous souhaitez préserver l'historique de toutes les fusions afin que votre équipe sache quand une fusion a été effectuée. Vous pouvez faire cela en utilisant le flag `--no-ff`, qui est également supporté par Git-Sim :

```sh
$ git checkout dev
$ git-sim merge --no-ff main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-merge_01-05-23_09-50-14.jpg align="left")

*Commit de fusion forcé*

Dans l'image de sortie simulée ci-dessus, Git a créé un nouveau commit de fusion `abcdef` vers lequel l'étiquette de la branche `dev` pointe maintenant, même s'il était possible de simplement avancer rapidement vers le commit pointé par `main`.

Gardez à l'esprit que même lorsque vous forcez un commit de fusion de cette manière, aucune divergence de l'historique des branches n'a eu lieu. Les deux branches se trouvent toujours sur une seule ligne de développement.

## `git rebase` – Comment déplacer le commit actuel vers un nouveau commit de base

Enfin, nous allons brièvement couvrir un scénario spécifique de la commande standard [git rebase](https://initialcommit.com/blog/git-rebase). Au lieu de fusionner le contenu de deux branches, `git rebase <new-base>` réapplique les commits accessibles par la branche actuelle sur un nouveau commit de base, spécifié par `<new-base>`.

Par défaut, `git rebase` s'exécute en **mode standard**, qui est ce que nous allons discuter ici. Le flag `-i` permet à rebase de s'exécuter en **mode interactif**, mais cela est hors du cadre de cet article.

En utilisant notre exemple de dépôt précédent, notons les 2 nouveaux commits ajoutés à la branche `dev` `ead5cc` ("Fontina") et `f42fee` ("Asiago") :

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-log_01-05-23_09-53-00.jpg align="left")

Ensuite, nous voulons déplacer ces 2 nouveaux commits vers la pointe de la branche `main` en utilisant la commande `git rebase`. Cela peut être simulé en utilisant les commandes :

```sh
$ git checkout dev
$ git-sim rebase main
```

![Image](https://www.freecodecamp.org/news/content/images/2023/01/git-sim-rebase_01-05-23_09-53-34.jpg align="left")

Dans la sortie simulée ci-dessus, les lignes pointillées montrent comment les 2 nouveaux commits sur la branche `dev` sont rebasés sur la pointe de `main`.

Dans un rebase standard, Git identifie le nombre de commits à rebaser en remontant depuis la pointe de la branche active jusqu'à ce qu'un commit ancêtre commun soit trouvé entre les deux branches.

Bien sûr, cet ancêtre commun existe déjà sur la branche de destination, donc le rebase n'a pas besoin de l'inclure, et peut s'arrêter à ce point.

Dans ce cas, les deux commits sur la branche `dev` qui n'existent pas encore sur `main` sont `ead5cc` ("Fontina") et `f42fee` ("Asiago"). Ceux-ci sont rebasés sur `main` comme le montrent les lignes pointillées ci-dessus. Puisque le commit `640bb5` ("Gouda") existe déjà sur `main`, il n'est pas inclus dans le rebase.

Notez que le rebase dans Git réécrit en fait l'historique des commits, puisque chaque ID de commit dépend du contenu de ce commit *et* de l'historique qui le précède.

Même si le contenu des deux commits rebasés dans l'exemple ci-dessus s'applique proprement à la branche `main`, de nouveaux ID de commit doivent être calculés puisque leur historique diffère maintenant de celui lorsqu'ils étaient appliqués à la branche `dev`.

Pour cette raison, une bonne règle de base est de **ne rebaser que les commits localement qui n'ont pas encore été poussés vers un dépôt distant**. Cela garantira que vous et votre équipe maintenez un état de dépôt cohérent pour votre projet au fil du temps.

## Résumé

Dans cet article, nous utilisons l'[outil Git-Sim](https://initialcommit.com/tools/git-sim) pour fournir un aperçu de 3 commandes Git notoirement confuses – `git reset`, `git merge`, et `git rebase`.

Nous avons illustré comment réinitialiser le pointeur HEAD de Git vers un commit précédent tout en gérant les fichiers committés, les fichiers en staging et les fichiers du répertoire de travail comme souhaité en utilisant les flags `--soft`, `--mixed`, ou `--hard`.

Ensuite, nous avons décrit les types de fusion de base dans Git, y compris la fusion trois-voies et la fusion rapide.

Enfin, nous avons discuté du rebase des branches, ce qui signifie déplacer un ensemble de commits vers un nouveau commit de base.

Pour chacune de ces commandes, nous avons montré comment l'outil en ligne de commande Git-Sim peut être utilisé pour créer des simulations uniques et personnalisées des effets de votre commande Git avant d'exécuter la commande Git réelle.

## Prochaines étapes

Si vous êtes un apprenant visuel et un utilisateur de Git, je vous encourage à essayer [Git-Sim](https://initialcommit.com/tools/git-sim) pour simuler les commandes Git dans vos propres dépôts locaux avant d'exécuter les commandes réelles.

Cela vous donnera la confiance d'exécuter les commandes Git réelles, et même vous fournir du contenu visuel pour aider à la documentation, au partage de contenu et à l'enseignement aux autres de l'utilisation de Git.

Git-Sim est un outil gratuit et open-source écrit en Python, donc si vous êtes intéressé à contribuer ou si vous trouvez des bugs, n'hésitez pas à consulter le [projet Git-Sim sur GitHub](https://github.com/initialcommit-com/git-sim) et/ou à me contacter à [jacob@initialcommit.io](mailto:jacob@initialcommit.io) !