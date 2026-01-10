---
title: Comment simplifier vos commandes Git avec les alias Git
subtitle: ''
author: Grant Riordan
co_authors: []
series: null
date: '2024-11-12T11:57:40.068Z'
originalURL: https://freecodecamp.org/news/how-to-simplify-your-git-commands-with-git-aliases
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730061609849/a3f3e8f3-102e-4dde-bec7-660be0121fad.png
tags:
- name: Git
  slug: git
- name: Productivity
  slug: productivity
seo_title: Comment simplifier vos commandes Git avec les alias Git
seo_desc: 'As a developer, you probably use the Git CLI (Command Line Interface) daily.
  However, writing the same old commands repeatedly can be laborious, especially when
  the commands are lengthy. This is where Git aliases come in to help out.

  In this article,...'
---

En tant que développeur, vous utilisez probablement l'interface en ligne de commande (CLI) de Git quotidiennement. Cependant, écrire les mêmes commandes encore et encore peut être fastidieux, surtout lorsque les commandes sont longues. C'est là que les alias Git interviennent pour vous aider.

Dans cet article, vous apprendrez comment simplifier vos commandes Git en utilisant des alias.

## Table des matières

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que les alias Git ?](#heading-quest-ce-que-les-alias-git)
    
* [Comment ajouter des alias Git via le fichier de configuration global Git (recommandé)](#heading-comment-ajouter-des-alias-git-via-le-fichier-de-configuration-global-git-recommande)
    
    * [Comment définir votre éditeur Git préféré](#heading-comment-definir-votre-editeur-git-prefere)
        
    * [Comment ouvrir le fichier de configuration Git](#heading-comment-ouvrir-le-fichier-de-configuration-git)
        
    * [Comment ajouter un alias Git via votre fichier de configuration](#heading-comment-ajouter-un-alias-git-via-votre-fichier-de-configuration)
        
* [Comment ajouter des alias dans le CLI](#heading-comment-ajouter-des-alias-dans-le-cli)
    
* [Comment créer des commandes personnalisées pour des raccourcis plus complexes](#heading-comment-creer-des-commandes-personnalisees-pour-des-raccourcis-plus-complexes)
    
    * [Comment utiliser des paramètres dans toutes les commandes](#heading-comment-utiliser-des-parametres-dans-toutes-les-commandes)
        
* [Autres alias utiles](#heading-autres-alias-utiles)
    
* [Résumé](#heading-resume)
    

## Prérequis

* Connaissance de Git.
    
* Git Bash installé (optionnel mais recommandé pour les utilisateurs Windows).
    
* Un IDE comme VS Code (ceci est également optionnel).
    

## Qu'est-ce que les alias Git ?

Les alias Git sont des raccourcis personnalisés pour les commandes Git existantes, rendant les tâches courantes plus rapides et plus faciles. Ils vous permettent de définir vos propres commandes, vous permettant de personnaliser les raccourcis exactement comme vous le souhaitez.

Vous avez deux options principales pour ajouter/créer des alias git dans votre configuration git, en utilisant votre fichier de configuration Git ou en les ajoutant directement via le CLI (terminal/ligne de commande).

## Comment ajouter des alias Git via le fichier de configuration global Git (recommandé)

Cette option implique d'ouvrir votre fichier de configuration git global et d'ajouter vos alias git à la fin du fichier.

### Comment définir votre éditeur Git préféré

Définissez votre logiciel d'édition de configuration Git par défaut, par exemple, j'utilise VS Code pour éditer mon fichier de configuration Git, mais vous pouvez utiliser n'importe quel éditeur de texte/éditeur de code que vous préférez.

Exécutez cette commande pour définir Notepad comme votre éditeur préféré sur Windows (CMD/PowerShell) :

```bash
git config --global core.editor "notepad"
```

Exécutez cette commande pour définir VS Code comme votre éditeur préféré sur Windows & MacOS/Linux :

```bash
git config --global core.editor "code --wait"
```

Pour définir un autre éditeur par défaut, recherchez en ligne "Définir {éditeur} comme éditeur Git par défaut", et remplacez `{éditeur}` par votre application préférée.

### Comment ouvrir le fichier de configuration Git

Ouvrez votre terminal de choix et entrez la commande suivante. Cela ouvrira le fichier de configuration Git global (`git config --global`), en mode édition (`-e`).

```bash
git config --global -e
```

Vous pouvez ouvrir le fichier de configuration git directement depuis les emplacements suivants :

**Mac Os** : Répertoire personnel → montrer les fichiers cachés (Cmd + Shift + H) → `.gitconfig`  
  
**Windows** : `C:\Users\VotreNomUtilisateur\` → puis montrer les fichiers cachés (dans Affichage) → et trouver `.gitconfig`  
  
**Linux** : Répertoire personnel → montrer les fichiers cachés (Ctrl + H) → `.gitconfig`

### Comment ajouter un alias Git via votre fichier de configuration

Si vous ajoutez des alias Git pour la première fois, ouvrez votre fichier `.gitconfig`, ajoutez `[alias]` à la fin, puis listez vos raccourcis ci-dessous. Cela indique à Git que ce sont des alias. Ajoutez votre alias préféré (la commande raccourcie que vous souhaitez exécuter).

Le format d'un alias git est `<alias> = <command>`, donc nous avons :

```bash
co = checkout
cob = checkout -b
```

**Explication des exemples ci-dessus :**

`co = checkout` cela mappe la commande `git checkout` à une commande plus courte `git co`. Vous appelerez ensuite `git co feature/123` dans votre terminal.

Vous n'avez pas besoin de taper `git` devant la commande, car la configuration le préfixera automatiquement car elle sait que la commande que vous mappez est une commande Git.  
  
**Note** : Tout paramètre passé à la commande sera appliqué à la commande finale appelée dans l'alias uniquement.  
  
D'autres alias peuvent être ajoutés de cette manière, en mappant des raccourcis aux commandes git existantes. L'enregistrement et la fermeture du fichier rendront alors les alias disponibles dans votre terminal.

## Comment ajouter des alias dans le CLI

Si vous voulez une approche plus rationalisée pour ajouter des alias Git, vous pouvez les ajouter directement depuis le terminal/la ligne de commande.

En prenant les exemples ci-dessus, nous pouvons les ajouter directement de la manière suivante :

Le format de la commande est : `git config --global alias.{alias} "{original command}"` :

```bash
git config --global alias.co "checkout"
#ou
git config --global alias.cob "checkout -b"
```

C'est aussi simple que cela !

## Comment créer des commandes personnalisées pour des raccourcis plus complexes

D'accord, cela semble génial, mais ce n'est pas vraiment si impressionnant – nous ne supprimons que quelques caractères. Cependant, nous pouvons les rendre beaucoup plus utiles, nous pouvons créer nos commandes en utilisant des commandes shell.

Prenons l'exemple suivant, une commande que j'utilise beaucoup !

```bash
new-work = !git checkout main && git pull && git cob  
```

Cet alias combine plusieurs commandes Git en une seule commande shell. Le caractère `!` indique à Git de le traiter comme une commande shell, et non comme une commande Git standard.  
  
Sans `!`, Git traite l'alias comme une commande Git (par exemple, `checkout` devient `git checkout`). Avec `!`, Git sait qu'il doit l'exécuter comme une commande shell sans ajouter `git` devant.

En enchaînant ces commandes, nous pouvons écrire des alias beaucoup plus utiles. Celui ci-dessus va :

* D'abord, basculer vers la branche `main`.
    
* En utilisant l'opérateur `&&`, cela signifie que les autres commandes ne s'exécuteront que si la précédente a réussi.
    
* Ensuite, il va récupérer les changements de `main`.
    
* Enfin, créer une nouvelle branche à partir de la branche `main` en utilisant notre autre alias `git cob`.
    

La commande finale peut alors accepter des paramètres (comme le ferait la commande Git originale), donc elle peut être utilisée comme suit :

```bash
git new-work 'feature/new-work-from-main'
```

### Comment utiliser des paramètres dans toutes les commandes

Jusqu'à présent, nous n'avons pu passer nos paramètres qu'à la commande git finale dans notre alias. Cependant, que faire si nous voulons passer des paramètres à certaines, sinon toutes les commandes dans l'alias ? Nous pouvons y parvenir en utilisant une fonction shell.

Prenons l'exemple suivant :

```bash
new-work = "!f() { git checkout \"$1\" && git pull && git checkout -b \"$2\"; }; f"
```

Ci-dessus, nous utilisons une fonction shell qui traite les paramètres d'entrée.

**Explication :**

1. `!f()`:
    
    * Le `!` indique à Git d'interpréter l'alias comme une commande shell plutôt que comme une commande Git standard.
        
    * `f()` définit une fonction shell `f` qui nous permettra d'exécuter plusieurs commandes en séquence.
        
2. Tout ce qui se trouve à l'intérieur de `{ }` est ce qui sera exécuté dans la fonction `f()`.
    
3. `git checkout \"$1\"` : Exécutera une commande Git paramétrée, où `$1` est échappé et sera remplacé par le premier paramètre passé à l'alias. Les séquences d'échappement `\"` autour de `$1` permettent des noms de branche avec espaces.
    
4. `&&` est un opérateur logique qui garantit que chaque commande ne s'exécute que si la précédente réussit. Si `git checkout "$1"` échoue, les commandes qui suivent ne s'exécuteront pas.
    
5. `git checkout -b \"$2\"` : Crée une nouvelle branche avec le nom du deuxième paramètre comme précédemment.
    
6. `;` : Marque la fin de la fonction `f()` ;
    
7. `f` : Le `f` final appelle la fonction alias immédiatement, ce qui signifie que lorsque vous appelez l'alias, il déclare la fonction puis l'appelle immédiatement.
    

**Utilisation :**

```bash
git new-work development task/feat-123
```

## Autres alias utiles

```bash
[alias]
 	co = checkout
    cob = checkout -b
    s = status
    tidy-up = !git checkout main && git branch | grep -v "main" | xargs git branch -D
    latest = !git checkout main && git pull
    new-work = "!f() { git checkout \"$1\" && git pull && git checkout -b \"$2\"; }; f"
    done = !git push -u origin HEAD
    save = !git add -A && git commit
    saveM = !git add -A && git commit -m
    br = branch --format='%(HEAD) %(color:yellow)%(refname:short)%(color:reset) - %(contents:subject) %(color:green)(%(committerdate:relative)) [%(authorname)]' --sort=-committerdate
```

## Résumé

`co` : Basculer vers la branche donnée → `git co task/feat-123`  
  
`cob` : Crée une nouvelle branche à partir de la branche actuelle → `git cob feature/123`  
  
`s` : Appelle `git status` pour voir le statut de la branche git actuelle → `git s`  
  
`tidy-up` : Supprime toutes les branches locales autres que `main` → `git tidy-up`  
  
`latest` : Récupère les derniers changements de la branche `main` distante → `git latest`  
  
`new-work` : Crée une nouvelle branche (2ème paramètre) à partir de la branche du 1er paramètre → `git new-work main feat/123`

`git done` : Pousse la branche actuelle vers le dépôt distant (`origin`) et la définit comme branche amont. Cela peut être utile lorsque vous poussez votre premier commit et que vous obtenez l'erreur :  
`fatal: The current branch has no upstream branch. To push the current branch and set the remote as upstream, use git push --set-upstream origin`

`save` : Ajoutera simplement tous les fichiers modifiés, et les commitera, en ouvrant votre éditeur Git par défaut et en demandant un message de commit → `git save`

`savem` : Fera comme ci-dessus, mais au lieu d'ouvrir votre éditeur, vous pouvez passer un message de commit en ligne → `git savem 'Task123: add index.html`

`br` : Celui-ci semble compliqué, mais il n'est pas aussi compliqué qu'il n'y paraît, mais il met en évidence la puissance des alias. En essence, il personnalise le format de sortie de `git branch` pour afficher une liste détaillée et colorée des branches, triées par la date de commit la plus récente, cela ressemblera à quelque chose comme l'image ci-dessous pour chaque branche que vous avez localement.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1730060113591/36008ee8-e54e-4b06-8a84-2a20885a1255.png align="center")

Voilà, une introduction aux alias Git et quelques exemples utiles d'alias que vous pouvez ajouter comme point de départ à votre configuration.

Comme toujours, si vous voulez en discuter ou entendre parler des futurs articles, vous pouvez me suivre sur [Twitter](https://x.com/grantdotdev).