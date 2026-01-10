---
title: Comment écrire des commandes Bash en une ligne pour cloner et gérer des dépôts
  GitHub et GitLab
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2019-08-07T15:14:05.000Z'
originalURL: https://freecodecamp.org/news/bash-one-liners-for-github-and-gitlab
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/cover.png
tags:
- name: Bash
  slug: bash
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: GitLab
  slug: gitlab
- name: terminal
  slug: terminal
seo_title: Comment écrire des commandes Bash en une ligne pour cloner et gérer des
  dépôts GitHub et GitLab
seo_desc: "Few things are more satisfying to me than one elegant line of Bash that\
  \ automates hours of tedious work. \nAs part of some recent explorations into automatically\
  \ re-creating my laptop with Bash scripts (post to come!), I wanted to find a way\
  \ to easily..."
---

Peu de choses sont plus satisfaisantes pour moi qu'une ligne élégante de Bash qui automatise des heures de travail fastidieux. 

Dans le cadre de certaines explorations récentes pour recréer automatiquement mon ordinateur portable avec des scripts Bash (article à venir !), je voulais trouver un moyen de cloner facilement mes dépôts hébergés sur GitHub sur une nouvelle machine. Après quelques recherches, j'ai écrit une commande en une ligne qui faisait exactement cela. 

Ensuite, dans l'esprit de ne pas mettre tous nos œufs dans le même panier, j'ai écrit une autre commande en une ligne pour créer et pousser automatiquement des sauvegardes hébergées sur GitLab. Les voici.

# Une commande Bash en une ligne pour cloner tous vos dépôts GitHub

Avertissement : vous aurez besoin d'une liste des dépôts GitHub que vous souhaitez cloner. Le bon côté de cela est qu'il vous donne le plein contrôle pour choisir uniquement les dépôts que vous voulez sur votre machine, au lieu de tout prendre en bloc.

Vous pouvez facilement cloner des dépôts GitHub sans entrer votre mot de passe à chaque fois en utilisant HTTPS avec vos [identifiants mis en cache pendant 15 minutes](https://help.github.com/en/articles/caching-your-github-password-in-git) ou, ma méthode préférée, en [vous connectant à GitHub avec SSH](https://help.github.com/en/articles/connecting-to-github-with-ssh). Pour faire court, je vais supposer que nous utilisons cette dernière méthode et que nos clés SSH sont configurées.

Étant donné une liste d'URLs GitHub dans le fichier `gh-repos.txt`, comme ceci :

```txt
git@github.com:username/first-repository.git
git@github.com:username/second-repository.git
git@github.com:username/third-repository.git
```

Nous exécutons :

```bash
xargs -n1 git clone < gh-repos.txt
```

Cela clone tous les dépôts de la liste dans le dossier courant. Cette même commande en une ligne fonctionne également pour GitLab, si vous substituez les URLs appropriées.

## Que se passe-t-il ici ?

Il y a deux parties à cette commande en une ligne : l'entrée, contre-intuitivement du côté droit, et la partie qui fait que les choses se passent, du côté gauche. Nous pourrions rendre l'ordre de ces parties plus intuitif (peut-être ?) en écrivant la même commande comme ceci :

```bash
<gh-repos.txt xargs -n1 git clone 
```

Pour exécuter une commande pour chaque ligne de notre entrée, `gh-repos.txt`, nous utilisons `xargs -n1`. L'outil `xargs` lit les éléments de l'entrée et exécute les commandes qu'il trouve (il fera `echo` s'il n'en trouve pas). Par défaut, il suppose que les éléments sont séparés par des espaces ; les nouvelles lignes fonctionnent également et rendent notre liste plus facile à lire. Le drapeau `-n1` indique à `xargs` d'utiliser `1` argument, ou dans notre cas, une ligne, par commande. Nous construisons notre commande avec `git clone`, que `xargs` exécute ensuite pour chaque ligne. Et voilà.

# Une commande Bash en une ligne pour créer et pousser plusieurs dépôts sur GitLab

GitLab, contrairement à GitHub, nous permet de faire cette astuce où nous n'avons pas besoin d'utiliser le site web pour créer un nouveau dépôt d'abord. Nous pouvons [créer un nouveau dépôt GitLab depuis notre terminal](https://gitlab.com/help/gitlab-basics/create-project#push-to-create-a-new-project). Le dépôt nouvellement créé est par défaut défini comme Privé, donc si nous voulons le rendre Public sur GitLab, nous devrons le faire manuellement plus tard.

La documentation de GitLab nous dit de pousser pour créer un nouveau projet en utilisant `git push --set-upstream`, mais je ne trouve pas cela très pratique pour utiliser GitLab comme sauvegarde. Alors que je travaille avec mes dépôts à l'avenir, j'aimerais exécuter une commande qui pousse à la fois sur GitHub _et_ GitLab sans effort supplémentaire de ma part.

Pour que cette commande Bash en une ligne fonctionne, nous aurons également besoin d'une liste d'URLs de dépôts pour GitLab (celles qui n'existent pas encore). Nous pouvons facilement faire cela en copiant notre liste de dépôts GitHub, en l'ouvrant avec Vim, et en faisant une [recherche-et-remplacement](https://vim.fandom.com/wiki/Search_and_replace) :

```bash
cp gh-repos.txt gl-repos.txt
vim gl-repos.txt
:%s/\<github\>/gitlab/g
:wq
```

Cela produit `gl-repos.txt`, qui ressemble à :

```txt
git@gitlab.com:username/first-repository.git
git@gitlab.com:username/second-repository.git
git@gitlab.com:username/third-repository.git
```

Nous pouvons créer ces dépôts sur GitLab, ajouter les URLs comme remotes, et pousser notre code vers les nouveaux dépôts en exécutant :

```bash
awk -F'\/|(\.git)' '{system("cd ~/FULL/PATH/" $2 " && git remote set-url origin --add " $0 " && git push")}' gl-repos.txt
```

Accrochez-vous et je vais l'expliquer ; pour l'instant, notez que `~/FULL/PATH/` doit être le chemin complet vers le répertoire contenant nos dépôts GitHub.

Nous devons noter quelques hypothèses :

1. Le nom du répertoire sur votre machine locale qui contient le dépôt est le même que le nom du dépôt dans l'URL (ce sera le cas s'il a été cloné avec la commande en une ligne ci-dessus) ;
2. Chaque dépôt est actuellement sur la branche que vous voulez pousser, c'est-à-dire `master`.

La commande en une ligne pourrait être étendue pour gérer ces hypothèses, mais il est de l'humble avis de l'auteur qu'à ce stade, nous devrions vraiment écrire un script Bash.

## Que se passe-t-il ici ?

Notre commande Bash en une ligne utilise chaque ligne (ou URL) dans le fichier `gl-repos.txt` comme entrée. Avec `awk`, elle sépare le nom du répertoire contenant le dépôt sur notre machine locale, et utilise ces morceaux d'information pour construire notre commande plus large. Si nous devions `print` la sortie de `awk`, nous verrions :

```bash
cd ~/FULL/PATH/first-repository && git remote set-url origin --add git@gitlab.com:username/first-repository.git && git push
cd ~/FULL/PATH/second-repository && git remote set-url origin --add git@gitlab.com:username/second-repository.git && git push
cd ~/FULL/PATH/third-repository && git remote set-url origin --add git@gitlab.com:username/third-repository.git && git push
```

Examinons comment nous construisons cette commande.

### Division de chaînes avec `awk`

L'outil `awk` peut diviser l'entrée en fonction des [séparateurs de champs](https://www.gnu.org/software/gawk/manual/html_node/Command-Line-Field-Separator.html). Le séparateur par défaut est un caractère d'espace blanc, mais nous pouvons changer cela en passant le drapeau `-F`. Outre les caractères uniques, nous pouvons également utiliser un [séparateur de champs d'expression régulière](https://www.gnu.org/software/gawk/manual/html_node/Regexp-Field-Splitting.html#Regexp-Field-Splitting). Puisque nos URLs de dépôt ont un format défini, nous pouvons obtenir les noms des dépôts en demandant la sous-chaîne entre le caractère slash `/` et la fin de l'URL, `.git`.

Une façon d'y parvenir est avec notre regex `\/|(\.git)` :

* `\/` est un caractère `/` échappé ;
* `|` signifie "ou", indiquant à awk de correspondre à l'une ou l'autre expression ;
* `(\.git)` est le groupe de capture à la fin de notre URL qui correspond à "git", avec un caractère `.` échappé. C'est un peu une triche, car "git" ne divise strictement rien (il n'y a rien de l'autre côté), mais c'est un moyen facile pour nous de prendre ce morceau.

Une fois que nous avons dit à `awk` où diviser, nous pouvons obtenir la bonne sous-chaîne avec l'[opérateur de champ](https://www.gnu.org/software/gawk/manual/html_node/Fields.html#index-_0024-_0028dollar-sign_0029_002c-_0024-field-operator). Nous faisons référence à nos champs avec un caractère `$`, puis par le numéro de colonne du champ. Dans notre exemple, nous voulons le deuxième champ, `$2`. Voici à quoi ressemblent toutes les sous-chaînes :

```bash
1: git@gitlab.com:username
2: first-repository
```

Pour utiliser la chaîne entière, ou dans notre cas, l'URL entière, nous utilisons l'opérateur de champ `$0`. Pour écrire la commande, nous substituons simplement les opérateurs de champ pour le nom du dépôt et l'URL. Exécuter cela avec `print` pendant que nous le construisons peut aider à s'assurer que nous avons tous les espaces corrects.

```bash
awk -F'\/|(\.git)' '{print "cd ~/FULL/PATH/" $2 " && git remote set-url origin --add " $0 " && git push"}' gl-repos.txt
```

### Exécution de la commande

Nous construisons notre commande à l'intérieur des parenthèses de `system()`. En utilisant cela comme sortie de `awk`, chaque commande sera exécutée dès qu'elle sera construite et sortie. La fonction `system()` crée un [processus enfant](https://en.wikipedia.org/wiki/Child_process) qui exécute notre commande, puis retourne une fois la commande terminée. En anglais simple, cela nous permet d'effectuer les commandes Git sur chaque dépôt, un par un, sans interrompre notre processus principal dans lequel `awk` fait des choses avec notre fichier d'entrée. Voici notre commande finale à nouveau, tout assemblée.

```bash
awk -F'\/|(\.git)' '{system("cd ~/FULL/PATH/" $2 " && git remote set-url origin --add " $0 " && git push")}' gl-repos.txt
```

### Utilisation de nos sauvegardes

En ajoutant les URLs GitLab comme remotes, nous avons simplifié le processus de poussée vers les deux dépôts hébergés en externe. Si nous exécutons `git remote -v` dans l'un de nos répertoires de dépôt, nous verrons :

```bash
origin  git@github.com:username/first-repository.git (fetch)
origin  git@github.com:username/first-repository.git (push)
origin  git@gitlab.com:username/first-repository.git (push)
```

Maintenant, simplement exécuter `git push` sans arguments poussera la branche actuelle vers les deux dépôts distants.

Nous devons également noter que `git pull` essaiera généralement de tirer uniquement depuis le dépôt distant que vous avez initialement cloné (l'URL marquée `(fetch)` dans notre exemple ci-dessus). Tirer depuis plusieurs dépôts Git en même temps est possible, mais compliqué, et dépasse le cadre de cet article. Voici une [explication de la poussée et de la traction vers plusieurs remotes](https://astrofloyd.wordpress.com/2015/05/05/git-pushing-to-and-pulling-from-multiple-remote-locations-remote-url-and-pushurl/) pour vous aider à commencer, si vous êtes curieux. La [documentation Git sur les remotes](https://git-scm.com/book/en/v2/Git-Basics-Working-with-Remotes) peut également être utile.

# Pour élaborer sur la concision des commandes Bash en une ligne

Les commandes Bash en une ligne, une fois comprises, peuvent être des raccourcis amusants et pratiques. À tout le moins, être conscient des outils comme `xargs` et `awk` peut aider à automatiser et à atténuer beaucoup de fastidieux dans notre travail. Cependant, il y a quelques inconvénients.

En termes d'outil facile à comprendre, maintenable et abordable, les commandes Bash en une ligne sont nulles. Elles sont généralement plus compliquées à écrire qu'un script Bash utilisant des boucles `if` ou `while`, et certainement plus compliquées à lire. Il est probable que lorsque nous les écrivons, nous oublions une guillemet simple ou une parenthèse fermante quelque part ; et comme je l'espère, cet article le démontre, elles peuvent également nécessiter beaucoup d'explications. Alors pourquoi les utiliser ?

Imaginez lire une recette pour faire un gâteau, étape par étape. Vous comprenez les méthodes et les ingrédients, et vous rassemblez vos fournitures. Ensuite, en y réfléchissant, vous commencez à réaliser que si vous jetez simplement tous les ingrédients dans le four dans le bon ordre, un gâteau apparaîtra instantanément. Vous essayez, et ça marche !

Ce serait assez satisfaisant, n'est-ce pas ?