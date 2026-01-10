---
title: Aide-mémoire Git – Commandes Git utiles avec exemples
subtitle: ''
author: Flavio Copes
co_authors: []
series: null
date: '2024-08-20T14:47:35.583Z'
originalURL: https://freecodecamp.org/news/git-cheat-sheet-helpful-git-commands-with-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723993272242/896730cc-3e03-43be-83d9-06d37ebab5a5.jpeg
tags:
- name: Git
  slug: git
- name: GitHub
  slug: github
- name: Gitcommands
  slug: gitcommands
- name: '#codenewbies'
  slug: codenewbies
- name: Programming Tips
  slug: programming-tips
seo_title: Aide-mémoire Git – Commandes Git utiles avec exemples
seo_desc: 'This Git Cheat Sheet will provide you with a handy list of common (and
  not so common) commands that will make your life easier when working with Git.

  You can also download the Git Cheat Sheet in PDF format (along with some other resources)
  for free b...'
---

Cet Aide-mémoire Git vous fournira une liste pratique de commandes courantes (et moins courantes) qui vous faciliteront la vie lors de votre travail avec Git.

Vous pouvez également télécharger l'Aide-mémoire Git au format PDF (ainsi que d'autres ressources) gratuitement en rejoignant ma newsletter sur [flaviocopes.com/access](https://flaviocopes.com/access/).

## Table des matières

* [**Préface**](#heading-preface)
    
* [**Commandes Git de base**](#heading-commandes-git-de-base)
    
* [**Le répertoire de travail et la zone de transit**](#heading-le-repertoire-de-travail-et-la-zone-de-transit)
    
* [**Travailler avec les branches**](#heading-travailler-avec-les-branches)
    
* [**Fusionner dans Git**](#heading-fusionner-dans-git)
    
* [**Git Remotes**](#heading-git-remotes)
    
* [**Amender des Commits**](#heading-amender-des-commits)
    
* [**Le remisage (Stashing) dans Git**](#heading-le-remisage-stashing-dans-git)
    
* [**Étiquetage (Tagging) Git**](#heading-etiquetage-tagging-git)
    
* [**Annuler des changements dans Git**](#heading-annuler-des-changements-dans-git)
    
* [**Consulter les journaux d'historique**](#heading-consulter-les-journaux-dhistorique)
    
* [**Git Diffs**](#heading-git-diffs)
    
* [**Git Flow**](#heading-git-flow)
    
* [**Explorer les références Git**](#heading-explorer-les-references-git)
    
* [**Comment configurer Git**](#heading-comment-configurer-git)
    
* [**Sécurité Git**](#heading-securite-git)
    
* [**Comment définir des alias dans Git**](#heading-comment-definir-des-alias-dans-git)
    
* [**Rebasing dans Git**](#heading-rebasing-dans-git)
    
* [**Qu'est-ce que le Cherry-Picking ?**](#heading-quest-ce-que-le-cherry-picking)
    
* [**Le patching dans Git**](#heading-le-patching-dans-git)
    
* [**Dates relatives dans Git**](#heading-dates-relatives-dans-git)
    
* [**Git Blame**](#heading-git-blame)
    
* [**Archivage dans Git**](#heading-archivage-dans-git)
    
* [**Comment suivre des fichiers dans Git**](#heading-comment-suivre-des-fichiers-dans-git)
    
* [**Manipulation de l'index dans Git**](#heading-manipulation-de-lindex-dans-git)
    
* [**Squashing dans Git**](#heading-squashing-dans-git)
    
* [**Intégrité des données dans Git**](#heading-integrite-des-donnees-dans-git)
    
* [**Nettoyage dans Git**](#heading-nettoyage-dans-git)
    
* [**Git Subtree**](#heading-git-subtree)
    
* [**Comment rechercher dans Git**](#heading-comment-rechercher-dans-git)
    
* [**Bisecting dans Git**](#heading-bisecting-dans-git)
    
* [**Attributs Git**](#heading-git-attributes)
    
* [**Git Checkout**](#heading-git-checkout-2)
    
* [**Git Reflog**](#heading-git-reflog)
    
* [**Comment gérer les fichiers non suivis dans Git**](#heading-comment-gerer-les-fichiers-non-suivis-dans-git)
    
* [**Force Pushing dans Git**](#heading-force-pushing-dans-git)
    
* [**Git Fetch et Pull**](#heading-git-fetching-et-pulling)
    
* [**Comment gérer les conflits de fusion dans Git**](#heading-comment-gerer-les-conflits-de-fusion-dans-git)
    
* [**Working Trees dans Git**](#heading-working-trees-dans-git)
    
* [**Sous-modules (Submodules) dans Git**](#heading-sous-modules-submodules-dans-git)

## Préface

Bienvenue dans cet Aide-mémoire Git ! C'est un guide complet que j'ai créé pour aider les développeurs, novices comme chevronnés, à acquérir les connaissances nécessaires pour utiliser efficacement Git, le système de contrôle de version le plus populaire de l'industrie logicielle.

Cet aide-mémoire est conçu pour être votre ressource de référence, que vous gériez un projet solo ou que vous collaboriez au sein d'une grande équipe. En fournissant des explications claires et des exemples pratiques, il devrait aider à démystifier les complexités de Git et à les transformer en informations intuitives et exploitables.

Tout au long de ce guide, vous explorerez un large éventail de commandes et de concepts Git qui constituent l'épine dorsale du contrôle de version logiciel. Des opérations fondamentales comme l'initialisation de dépôts et le Commit de changements, aux techniques plus avancées telles que le branching, le merging et le rebasing, cet aide-mémoire couvre tout.

Vous plongerez également dans des sujets spécialisés comme le squashing de commits, le bisecting pour le débogage, la gestion des submodules et l'implémentation de subtrees. Tout cela contribuera à garantir que vous êtes bien préparé à relever tous les défis qui surviennent dans votre processus de développement.

Au fur et à mesure de votre progression, vous apprendrez comment maintenir l'intégrité des données, gérer plusieurs working trees et résoudre efficacement les conflits de fusion. À la fin, vous aurez non seulement une compréhension plus approfondie de Git, mais aussi la confiance nécessaire pour l'utiliser afin de rationaliser votre flux de travail et d'améliorer la collaboration avec vos pairs.

### Prérequis

Pour profiter pleinement de cet aide-mémoire, vous devriez avoir une connaissance de base des opérations en ligne de commande et des principes généraux de programmation. Vous devriez également être familier avec l'utilisation d'un terminal ou d'une invite de commande afin de mieux comprendre et appliquer les exemples fournis. Enfin, avoir une compréhension de base des concepts de contrôle de version améliorera votre capacité à naviguer efficacement dans ce guide.

## **Commandes Git de base**

Dans cette section, vous apprendrez les commandes Git fondamentales qui servent de base à la gestion et à la navigation efficaces dans vos dépôts Git.

Git est un système de contrôle de version distribué essentiel pour suivre les modifications de votre code, collaborer avec d'autres développeurs et maintenir l'intégrité de l'historique de votre projet. Comprendre ces commandes de base est crucial pour quiconque souhaite exploiter toute la puissance de Git dans son flux de travail de développement.

Nous explorerons une variété de commandes couvrant les aspects clés de l'utilisation de Git, tels que l'initialisation de nouveaux dépôts, le Commit de modifications, le branching et le merging.

Chaque commande est expliquée par une courte phrase décrivant son but ainsi que sa syntaxe, afin que vous puissiez l'utiliser efficacement dans des scénarios réels. Que vous mettiez en place un nouveau projet ou que vous travailliez sur un code existant, ces commandes vous aideront à organiser votre travail et à maintenir un flux de travail fluide.

### `git help`

La commande `git help` affiche les informations d'aide de Git. Elle fournit une référence rapide à l'utilisation de base de Git et aux commandes Git les plus couramment utilisées. Cette commande est utile lorsque vous avez besoin d'un rappel rapide des fonctionnalités de Git ou que vous souhaitez explorer les commandes disponibles.

Vous pouvez également utiliser `git help <command>` pour afficher l'aide d'une commande Git spécifique. Par exemple, `git help git` affiche l'aide Git spécifiquement pour la commande Git elle-même.

Ces commandes d'aide sont des ressources précieuses pour les débutants comme pour les utilisateurs expérimentés afin d'accéder rapidement aux informations sur les fonctionnalités et l'utilisation de Git.

### `git version`

La commande `git version` affiche la version de Git installée sur votre système. Cette commande est utile pour vérifier quelle version de Git vous utilisez actuellement, ce qui peut être important pour la compatibilité avec certaines fonctionnalités ou lors du dépannage de problèmes.

### `git init`

La commande `git init` est utilisée pour initialiser un nouveau dépôt Git dans le répertoire actuel. Cette commande crée un nouveau sous-répertoire nommé `.git` qui contient toutes les métadonnées nécessaires au nouveau dépôt. C'est généralement la première commande que vous exécutez lorsque vous commencez un nouveau projet que vous souhaitez gérer avec Git.

Après avoir exécuté cette commande, vous pouvez commencer à suivre les fichiers et à effectuer des commits dans votre nouveau dépôt Git.

### `git clone <repository_url>`

La commande `git clone <repository_url>` crée une copie d'un dépôt Git distant sur votre machine locale. Elle télécharge tous les fichiers, les branches et l'historique des commits, vous permettant de commencer à travailler sur le projet immédiatement.

### `git status`

La commande `git status` affiche l'état actuel du répertoire de travail et de la zone de transit (staging area) du dépôt Git. Elle affiche des informations sur les fichiers qui ont été modifiés, ajoutés ou supprimés, et si ces modifications sont indexées pour le prochain commit.

## **Le répertoire de travail et la zone de transit**

Le répertoire de travail (working directory) et la zone de transit (staging area) sont des concepts fondamentaux de Git qui jouent un rôle crucial dans le processus de contrôle de version.

Le répertoire de travail est l'environnement où vous modifiez activement vos fichiers, représentant l'état actuel de votre projet. C'est essentiellement un bac à sable où vous pouvez librement éditer, supprimer et créer des fichiers au fur et à mesure que vous développez votre projet. Mais ces modifications sont locales à votre machine et ne font pas encore partie de l'historique des versions.

D'un autre côté, la zone de transit, également appelée l'index, sert d'espace intermédiaire entre le répertoire de travail et le dépôt. Elle agit comme un point de contrôle où vous pouvez organiser sélectivement les modifications avant qu'elles ne soient validées dans l'historique du dépôt. Cela vous permet de préparer un ensemble de changements logiquement liés, garantissant que chaque commit est significatif et cohérent.

Les commandes ci-dessous vous aideront à gérer les modifications entre le répertoire de travail et la zone de transit. Elles vous permettront d'ajouter des fichiers à la zone de transit, de les supprimer ou de modifier les fichiers existants, vous donnant le contrôle sur ce qui sera inclus dans le prochain commit.

En utilisant ces commandes, vous pouvez vous assurer que seules les mises à jour prévues sont validées, rendant l'historique de votre projet clair et organisé. Ce processus est essentiel pour maintenir un historique propre et compréhensible, car il vous permet de suivre l'évolution de votre projet avec précision et clarté.

### `git checkout .`

Cette commande annule toutes les modifications dans le répertoire de travail, ramenant les fichiers à leur dernier état validé (committed). Cette commande est utile pour annuler rapidement les modifications locales et restaurer le répertoire de travail dans un état propre.

### `git reset -p`

Cette commande vous permet de réinitialiser de manière interactive les modifications dans le répertoire de travail. Elle offre un moyen d'annuler sélectivement les modifications, vous donnant un contrôle précis sur les changements à conserver ou à ignorer.

### `git add <file>`

Cette commande ajoute un fichier spécifique à la zone de transit dans Git. Cela prépare le fichier pour son inclusion dans le prochain commit, vous permettant de choisir sélectivement les modifications à inclure dans votre historique de version.

### `git add -p`

Permet d'indexer (stage) interactivement les modifications de votre répertoire de travail en les découpant en morceaux (hunks). Cela vous permet de réviser et d'ajouter sélectivement des parties des modifications à l'index avant de valider.

### `git add -i`

Entre dans le mode interactif d'ajout de fichiers. Fournit un menu interactif textuel où vous pouvez sélectionner diverses actions à effectuer, comme indexer des modifications individuelles, mettre à jour des fichiers ou consulter l'état.

### `git rm <file>`

Supprime un fichier du répertoire de travail et indexe sa suppression.

### `git rm --cached <file>`

Supprime le fichier spécifié de la zone de transit (index) mais le laisse intact dans votre répertoire de travail. Cela arrête efficacement le suivi du fichier par le contrôle de version.

### `git mv <old_path> <new_path>`

Cette commande est utilisée pour déplacer ou renommer un fichier ou un répertoire au sein d'un dépôt Git. Elle indexe automatiquement la modification, la rendant prête pour le prochain commit.

### `git commit -m "message"`

Cette commande est utilisée pour créer un nouveau commit dans votre dépôt Git. Elle enregistre les modifications qui ont été indexées (ajoutées à l'index) accompagnées d'un message descriptif. Ce message doit expliquer brièvement quelles modifications ont été apportées dans ce commit.

## **Travailler avec les branches**

Les branches Git sont des lignes de développement parallèles au sein d'un dépôt Git. Elles vous permettent de travailler sur différentes fonctionnalités, corrections de bugs ou expérimentations indépendamment de la base de code principale.

Chaque branche peut avoir son propre historique de commits, et les modifications apportées dans une branche n'affectent pas les autres jusqu'à ce qu'elles soient fusionnées (merged). Cela vous aide à organiser votre travail et facilite la collaboration en permettant à plusieurs développeurs de travailler simultanément sur différents aspects d'un projet sans interférer avec les progrès des autres.

Dans cette section, nous présenterons les commandes qui vous permettent de créer, basculer, lister, renommer et supprimer des branches dans votre dépôt Git. Ces commandes aident à gérer les lignes de développement parallèles. Vous apprendrez également comment afficher les historiques de commits et les relations entre branches, ainsi que la gestion des branches distantes.

### `git branch <branch_name>`

Crée une nouvelle branche.

### `git checkout <branch_name>`

Bascule vers la branche spécifiée et met à jour le répertoire de travail.

### `git branch`

Liste toutes les branches.

### `git branch -d <branch_name>`

Supprime une branche.

### `git push --delete <remote> <branch>`

Supprime une branche distante.

### `git branch -m <old_name> <new_name>`

Renomme une branche.

### `git checkout -b <new_branch>`

Crée et bascule vers une nouvelle branche nommée `<new_branch>`, basée sur la branche actuelle.

### `git switch <branch>`

Bascule le répertoire de travail vers la branche spécifiée.

### `git show-branch <branch>`

Affiche un résumé de l'historique des commits et des relations entre branches pour toutes les branches ou celles sélectionnées, montrant où chaque branche a divergé.

### `git show-branch --all`

Idem que ci-dessus, mais pour toutes les branches et leurs commits.

### `git branch -r`

Liste toutes les branches distantes dont votre dépôt local a connaissance.

### `git branch -a`

Liste toutes les branches de votre dépôt, y compris les branches locales et distantes.

### `git branch --merged`

Liste toutes les branches qui ont été entièrement fusionnées dans la branche actuelle et qui peuvent être supprimées en toute sécurité si elles ne sont plus nécessaires.

### `git branch --no-merged`

Liste toutes les branches qui n'ont pas été entièrement fusionnées dans votre branche actuelle, montrant les branches avec des modifications non encore intégrées.

## **Fusionner dans Git**

La commande `git merge` est utilisée pour combiner les modifications d'une branche dans une autre. Elle intègre les historiques des deux branches, créant un nouveau commit qui inclut les changements des deux sources.

Ce processus permet de rassembler plusieurs lignes de développement, facilitant la collaboration et garantissant que toutes les mises à jour sont incorporées dans le projet principal.

Pendant une fusion, des conflits peuvent survenir si des modifications se chevauchent, nécessitant une résolution manuelle pour assurer un résultat final cohérent.

### `git merge <branch>`

Intègre les modifications de la branche spécifiée dans votre branche actuelle, combinant leurs historiques.

### `git merge --no-ff <branch>`

Fusionne la branche spécifiée dans votre branche actuelle, en créant toujours un nouveau commit de fusion même si une fusion en avance rapide (fast-forward) est possible.

### `git merge --squash <branch>`

Combine toutes les modifications de la branche spécifiée en un seul commit, préparant les changements pour un commit dans la branche actuelle sans fusionner l'historique de la branche. Cela vous permet de modifier manuellement le message de commit.

### `git merge --abort`

Annule un processus de fusion en cours et restaure l'état de votre répertoire de travail et de l'index à ce qu'ils étaient avant le début de la fusion.

### `git merge -s ours <branch>` ou

### `git merge —-strategy=ours <branch>`

Ces commandes sont fonctionnellement identiques, mais la seconde est la version étendue (plus explicite), tandis que `git merge -s ours <branch>` est la version courte (couramment utilisée). Vous verrez cela plusieurs fois dans ce guide.

La commande `git merge —-strategy=ours <branch>` effectue une fusion en utilisant la stratégie "ours" (la nôtre), qui conserve les modifications de la branche actuelle et ignore celles de la branche spécifiée. Cela fusionne efficacement les historiques sans intégrer les changements de l'autre branche.

### `git merge --strategy=theirs <branch>`

Fusionne la branche spécifiée dans la branche actuelle en utilisant la stratégie "theirs" (la leur), qui résout tous les conflits en favorisant les modifications de la branche fusionnée. Notez que la stratégie "theirs" n'est pas une stratégie native intégrée et nécessite généralement un script personnalisé ou l'utilisation d'outils pour gérer la résolution des conflits.

## **Git Remotes**

Les "remotes" Git sont des références à des dépôts distants, qui sont des versions de votre projet hébergées sur Internet ou sur un autre réseau. Ils permettent la collaboration en permettant à plusieurs utilisateurs de partager et de synchroniser les modifications avec un dépôt central.

Les opérations courantes avec les remotes incluent `git fetch` pour récupérer les mises à jour, `git pull` pour récupérer et fusionner les modifications, et `git push` pour télécharger les commits locaux vers le dépôt distant.

La gestion des remotes implique l'ajout, la suppression et le renommage des connexions distantes, ainsi que la configuration des URL pour une collaboration fluide.

### `git fetch`

Récupère les modifications d'un dépôt distant mais ne les fusionne pas dans votre branche actuelle.

### `git pull`

Récupère les modifications d'un dépôt distant et les fusionne immédiatement dans votre branche actuelle.

### `git push`

Télécharge les modifications de votre branche locale vers un dépôt distant.

### `git remote`

Liste les noms des dépôts distants configurés pour votre dépôt local.

### `git remote -v`

Affiche les URL des dépôts distants associés à votre dépôt local, montrant à la fois les URL de récupération (fetch) et de poussée (push).

### `git remote add <name> <url>`

Ajoute un nouveau dépôt distant avec le nom et l'URL spécifiés à la configuration de votre dépôt local.

### `git remote remove <name>` ou

### `git remote rm <name>`

Supprime la connexion au dépôt distant spécifié de votre configuration Git locale. `git remote rm <name>` est la version courte de la commande.

### `git remote rename <old_name> <new_name>`

Modifie le nom d'une connexion de dépôt distant existante dans votre configuration Git locale.

### `git remote set-url <name> <newurl>`

Modifie l'URL d'une connexion de dépôt distant existante dans votre configuration Git locale.

### `git fetch <remote>`

Récupère les dernières modifications du dépôt distant spécifié, mettant à jour votre copie locale des branches distantes sans les fusionner dans vos branches locales.

### `git pull <remote>`

Récupère les modifications du dépôt distant spécifié et les fusionne dans votre branche actuelle.

### `git remote update`

Récupère les mises à jour pour tous les remotes suivis par le dépôt.

### `git push <remote> <branch>`

Télécharge la branche spécifiée de votre dépôt local vers le dépôt distant donné.

### `git push <remote> --delete <branch>`

Supprime la branche spécifiée du dépôt distant.

### `git remote show <remote>`

Affiche des informations détaillées sur le dépôt distant spécifié, y compris son URL, ses configurations de fetch et push, ainsi que les branches qu'il suit.

### `git ls-remote <repository>`

Liste les références (telles que les branches et les tags) et leurs IDs de commit du dépôt distant spécifié. Cette commande vous permet de visualiser les branches et tags disponibles dans un dépôt distant sans le cloner.

### `git push origin <branch> --set-upstream`

Pousse la branche locale &lt;branch&gt; vers le dépôt distant origin et configure la branche locale pour suivre la branche distante. Cela permet aux futures commandes git push et git pull d'utiliser ce dépôt distant par défaut.

### `git remote add upstream <repository>`

Ajoute un nouveau remote nommé upstream à votre dépôt local, pointant vers le &lt;repository&gt; spécifié. Ceci est couramment utilisé pour suivre le dépôt original à partir duquel vous avez fait un fork, tandis que origin fait généralement référence à votre propre fork.

### `git fetch upstream`

Récupère les mises à jour du dépôt distant upstream, mettant à jour vos références locales aux branches et tags de ce remote sans modifier votre répertoire de travail ni fusionner les changements.

### `git pull upstream <branch>`

Récupère les mises à jour de la &lt;branch&gt; du dépôt distant upstream et fusionne ces modifications dans votre branche actuelle. C'est souvent utilisé pour intégrer les modifications du dépôt original dans votre propre branche locale.

### `git push origin <branch>`

Télécharge la branche locale &lt;branch&gt; vers le dépôt distant origin, rendant votre branche et ses commits disponibles sur le remote.

## **Amender des Commits**

Amender des commits Git vous permet de modifier le commit le plus récent, généralement pour corriger ou mettre à jour son contenu ou son message. Vous pouvez le faire en utilisant la commande `git commit --amend`, qui ouvre le commit dans votre éditeur de texte par défaut pour les modifications.

L'amendement est particulièrement utile pour corriger de petites erreurs ou ajouter des modifications oubliées sans créer un nouveau commit, ce qui donne un historique de commits plus propre et plus précis.

### `git commit --amend`

Modifie le commit le plus récent, en combinant les modifications indexées.

### `git commit --amend -m "new message"`

Amende le message de commit du commit le plus récent.

### `git commit --fixup=HEAD`

Crée un nouveau commit avec l'option `--fixup` destiné à corriger ou amender le commit le plus récent (HEAD). Le nouveau commit est marqué par un préfixe `fixup!` dans le message de commit et sera utilisé pour corriger ou amender automatiquement le commit spécifié lors d'un rebase interactif.

## **Le remisage (Stashing) dans Git**

Le remisage (stashing) Git est une fonctionnalité qui vous permet de sauvegarder temporairement les modifications de votre répertoire de travail qui ne sont pas encore prêtes à être validées.

En utilisant la commande `git stash`, vous pouvez mettre de côté ces modifications et restaurer votre répertoire de travail dans un état propre, vous permettant de changer de branche ou d'effectuer d'autres tâches sans perdre votre progression. Plus tard, vous pourrez réappliquer les modifications remisées avec `git stash apply` ou `git stash pop`, vous permettant de reprendre là où vous vous étiez arrêté.

Cette fonctionnalité est particulièrement utile pour gérer le travail en cours lorsque vous devez traiter un problème urgent ou expérimenter un chemin de code différent.

### `git stash`

Sauvegarde temporairement vos modifications non validées, vous permettant de changer de branche ou d'effectuer d'autres opérations sans commiter un travail incomplet.

Il existe une version plus ancienne, `git stash save`, qui permet de spécifier un message personnalisé. Mais elle a été largement dépréciée au profit du simple `git stash`.

### `git stash -m "message"`

Idem que ci-dessus, mais stocke les modifications avec un message. Il existe également une version plus ancienne, `git stash save "message"`, mais `git stash -m "message"` est préféré pour les versions de Git 2.13 et plus récentes.

### `git stash show`

Affiche un résumé des modifications dans l'entrée de remise la plus récente, montrant quels fichiers ont été modifiés.

### `git stash list`

Affiche toutes les modifications remisées dans votre dépôt, présentées sous forme de liste numérotée.

### `git stash pop`

Applique la remise la plus récente puis la supprime immédiatement de la liste des remises.

### `git stash drop`

Supprime l'entrée de remise la plus récente de la liste des remises sans l'appliquer à votre répertoire de travail.

### `git stash apply`

Réapplique les modifications remisées les plus récentes à votre répertoire de travail sans les supprimer de la liste des remises.

### `git stash clear`

Efface et supprime toutes les entrées remisées, supprimant définitivement toutes les modifications sauvegardées dans votre pile de remise.

### `git stash branch <branch>`

Crée une nouvelle branche nommée &lt;branch&gt; à partir du commit où vous étiez avant de remiser vos modifications. Ensuite, elle applique les modifications remisées à cette nouvelle branche.

Cette commande vous permet efficacement de continuer à travailler sur vos modifications remisées dans une branche séparée, en préservant le contexte et les modifications d'origine.

## **Étiquetage (Tagging) Git**

L'étiquetage (tagging) Git est une fonctionnalité qui vous permet de marquer des points spécifiques de l'historique de votre dépôt comme importants avec un nom significatif, souvent utilisé pour des versions (releases) ou des jalons importants.

Contrairement aux branches, les tags sont généralement immuables et ne changent pas, servant de référence permanente à un commit particulier.

Il existe deux types de tags dans Git : les tags légers (lightweight), qui sont de simples pointeurs vers un commit, et les tags annotés, qui stockent des métadonnées supplémentaires comme le nom de l'auteur du tag, son e-mail, la date et un message.

Les tags peuvent être facilement créés, listés, poussés vers des dépôts distants et supprimés, offrant un moyen pratique de gérer et de référencer les points clés de la chronologie de développement de votre projet.

### `git tag <tag_name>`

Crée un nouveau tag avec le nom spécifié pointant vers le commit actuel (généralement utilisé pour marquer des points spécifiques dans l'historique des commits, comme les versions).

### `git tag -a <tag_name> -m "message"`

Crée un tag annoté avec le nom et le message spécifiés, qui inclut des métadonnées supplémentaires comme le nom du créateur du tag, l'e-mail et la date, et pointe vers le commit actuel.

### `git tag -d <tag_name>`

Supprime le tag spécifié de votre dépôt local.

### `git tag -f <tag> <commit>`

Force un tag à pointer vers un commit différent.

### `git show <tag_name>`

Affiche des informations détaillées sur le tag spécifié, y compris le commit vers lequel il pointe et tout message ou annotation de tag associé.

### `git push origin <tag_name>`

Télécharge le tag spécifié vers le dépôt distant, le rendant disponible pour les autres.

### `git push origin --tags`

Pousse tous les tags locaux vers le dépôt distant, garantissant que tous les tags sont synchronisés avec le remote.

### `git push --follow-tags`

Pousse à la fois les commits et les tags.

### `git fetch --tags`

Récupère tous les tags du dépôt distant par défaut et met à jour votre dépôt local avec ceux-ci, sans affecter vos branches actuelles.

## **Annuler des changements dans Git**

Annuler des changements dans Git consiste à défaire les modifications apportées à l'historique d'un dépôt. Vous pouvez le faire en utilisant plusieurs commandes, telles que `git revert`. Elle crée un nouveau commit qui annule les modifications d'un commit précédent spécifié, inversant efficacement ses effets tout en préservant l'historique des commits.

Une autre méthode consiste à utiliser `git reset`, qui change le HEAD actuel vers un commit spécifié et peut mettre à jour la zone de transit et le répertoire de travail selon les options choisies (`--soft`, `--mixed`, ou `--hard`).

Vous pouvez également utiliser `git checkout` pour ignorer les modifications dans le répertoire de travail, ramenant les fichiers à leur état lors du dernier commit.

Ces outils offrent une flexibilité dans la gestion et la correction des modifications, garantissant que le dépôt reste précis et propre.

### `git checkout -- <file>`

Ignore les modifications dans le fichier spécifié du répertoire de travail, le ramenant à l'état du dernier commit et annulant efficacement toute modification qui n'a pas été indexée.

### `git revert <commit>`

Crée un nouveau commit qui annule les modifications du commit spécifié, inversant efficacement ses effets tout en préservant l'historique.

### `git revert -n <commit>`

Annule un commit mais ne crée pas automatiquement le commit de résultat.

### `git reset`

Réinitialise le HEAD actuel à l'état spécifié, et met éventuellement à jour la zone de transit et le répertoire de travail, selon les options utilisées (`--soft`, `--mixed`, ou `--hard`).

### `git reset --soft <commit>`

Déplace HEAD vers le commit spécifié, tout en gardant l'index (zone de transit) et le répertoire de travail inchangés, de sorte que toutes les modifications après le commit spécifié restent indexées pour être validées. C'est utile lorsque vous voulez annuler des commits tout en gardant les changements prêts à être validés à nouveau.

### `git reset --mixed <commit>`

Déplace HEAD vers le commit spécifié et met à jour l'index (zone de transit) pour correspondre à ce commit. Mais cela laisse le répertoire de travail inchangé, de sorte que les modifications après le commit spécifié sont conservées mais ne sont plus suivies.

### `git reset --hard <commit>`

Déplace HEAD vers le commit spécifié et met à jour à la fois l'index (zone de transit) et le répertoire de travail pour correspondre à ce commit. Cela supprime toutes les modifications et les fichiers non suivis après le commit spécifié.

## **Consulter les journaux d'historique**

L'historique Git fait référence à l'enregistrement de toutes les modifications apportées à un dépôt au fil du temps. Il comprend une séquence chronologique de commits, chacun représentant un instantané (snapshot) du dépôt à un moment précis.

Cet historique vous permet de suivre les modifications, de comprendre l'évolution de la base de code et de collaborer efficacement en fournissant un journal détaillé de qui a apporté des modifications, quand et pourquoi.

Des outils comme `git log` vous aident à naviguer dans cet historique, offrant des aperçus du processus de développement et facilitant le débogage et la gestion de projet.

### `git log`

Affiche le journal des commits.

### `git log --oneline`

Affiche un résumé des commits sur une seule ligne chacun.

### `git log --graph`

Affiche une représentation graphique de l'historique des commits.

### `git log --stat`

Affiche les statistiques de fichiers en plus de l'historique des commits.

### `git log --pretty=format:"%h %s"`

Formate la sortie du journal selon le format spécifié.

### `git log --pretty=format:"%h - %an, %ar : %s"`

Fournit un format de journaux plus lisible pour l'homme.

### `git log --author=<author>`

Affiche les commits effectués par l'auteur spécifié.

### `git log --before=<date>`

Affiche les commits effectués avant la date spécifiée.

### `git log --after=<date>`

Affiche les commits effectués après la date spécifiée (identique à `git log --since=<date>`)

### `git log --cherry-pick`

Omet les commits qui sont équivalents entre deux branches.

### `git log --follow <file>`

Affiche les commits pour un fichier, y compris les renommages.

### `git log --show-signature`

Affiche les informations de signature GPG pour les commits.

### `git shortlog`

Résume la sortie de git log par auteur.

### `git shortlog -sn`

Résume la sortie de git log par auteur, avec le nombre de commits.

### `git log --simplify-by-decoration`

Affiche uniquement les commits qui sont référencés par des tags ou des branches.

### `git log --no-merges`

Omet les commits de fusion du journal.

### `git whatchanged`

Liste les données de commit dans un format similaire à un journal de commit.

### `git diff-tree --pretty --name-only --root <commit>`

Affiche des informations détaillées pour un arbre de commit.

### `git log --first-parent`

Affiche uniquement les commits de la branche actuelle et exclut ceux fusionnés à partir d'autres branches.

## **Git Diffs**

Les Git diffs sont une fonctionnalité de Git qui vous permet de voir les différences entre divers états de votre dépôt. Cela peut inclure des différences entre votre répertoire de travail et la zone de transit, entre la zone de transit et le dernier commit, ou entre n'importe quels deux commits ou branches.

En affichant les modifications ligne par ligne dans les fichiers, les diffs vous aident à réviser les modifications avant de commiter, de fusionner ou d'appliquer des changements, garantissant ainsi la précision et la cohérence de votre base de code.

### `git diff`

Affiche les différences entre divers états de votre dépôt, comme entre votre répertoire de travail et l'index (zone de transit), entre l'index et le dernier commit, ou entre deux commits. Il affiche les modifications ligne par ligne dans les fichiers, vous aidant à réviser les modifications avant de valider ou de fusionner.

### `git diff --stat`

Affiche un résumé des modifications entre votre répertoire de travail et l'index (zone de transit), vous aidant à voir quels fichiers ont été modifiés et combien de lignes ont été ajoutées ou supprimées.

### `git diff --stat <commit>`

Visualise les modifications entre un commit et le répertoire de travail.

### `git diff --stat <commit1> <commit2>`

Fournit un résumé des modifications entre deux commits, montrant quels fichiers ont été altérés et l'étendue des changements entre eux.

### `git diff --stat <branch1> <branch2>`

Résume les différences entre deux branches, indiquant les fichiers modifiés et l'ampleur des changements.

### `git diff --name-only <commit>`

Affiche uniquement les noms des fichiers qui ont changé dans le commit spécifié.

### `git diff --cached`

Affiche les différences entre les modifications indexées (index) et le dernier commit, vous aidant à réviser ce qui sera inclus dans le prochain commit.

### `git diff HEAD`

Affiche les différences entre le répertoire de travail et le dernier commit (HEAD), vous permettant de voir quels changements ont été apportés depuis le dernier commit.

### `git diff <branch1> <branch2>`

Affiche les différences entre les pointes (tips) de deux branches, mettant en évidence les changements entre les commits à la fin de chaque branche.

### `git difftool`

Lance un outil de diff pour comparer les modifications.

### `git difftool <commit1> <commit2>`

Utilise l'outil de diff pour afficher les différences entre deux commits spécifiés.

### `git difftool <branch1> <branch2>`

Ouvre l'outil de diff pour comparer les changements entre deux branches.

### `git cherry <branch>`

Compare les commits de votre branche actuelle par rapport à une autre branche et montre quels commits sont uniques à chaque branche. C'est couramment utilisé pour identifier quels commits d'une branche n'ont pas été appliqués à une autre.

## **Git Flow**

Git Flow est un modèle de branching pour Git qui fournit un cadre robuste pour gérer des projets plus importants. Il définit une stratégie de branching stricte conçue autour du cycle de release du projet, avec deux branches principales (main et develop) et des branches de support pour les fonctionnalités (features), les releases et les correctifs urgents (hotfixes).

Ce modèle aide à organiser le travail, garantissant un historique propre et gérable, et facilitant la collaboration en définissant clairement les rôles et les processus pour différents types de travaux de développement.

### `git flow init`

Initialise un dépôt pour un modèle de branching git-flow.

### `git flow feature start <feature>`

Démarre une nouvelle branche de fonctionnalité dans git-flow.

### `git flow feature finish <feature>`

Termine une branche de fonctionnalité dans git-flow.

## **Explorer les références Git**

Les références Git, souvent appelées "refs", sont des pointeurs vers des commits ou des objets spécifiques au sein d'un dépôt Git. Ceux-ci peuvent inclure des branches, des tags et d'autres références comme HEAD, qui pointe vers le commit actuel extrait dans votre répertoire de travail.

Les références sont utilisées pour suivre la structure et l'historique du dépôt. Elles aident Git à gérer et à naviguer efficacement entre différents points de la chronologie du projet.

Les refs fournissent également un moyen de nommer et de se référer à des commits particuliers, ce qui facilite le travail et la manipulation de l'historique du dépôt.

### `git show-ref --heads`

Liste les références de toutes les têtes (branches).

### `git show-ref --tags`

Liste les références de tous les tags.

## **Comment configurer Git**

La configuration de Git consiste à définir diverses options et préférences qui contrôlent le comportement de votre environnement Git. Cela peut inclure la spécification de votre nom d'utilisateur et de votre e-mail, la configuration des éditeurs de texte par défaut, la création d'alias pour les commandes fréquemment utilisées et la configuration des fichiers d'ignorance globaux.

Vous pouvez appliquer des paramètres de configuration à différents niveaux : global (affectant tous les dépôts de votre système), local (affectant un seul dépôt) et au niveau du système. Ces paramètres garantissent une expérience utilisateur personnalisée et cohérente, rationalisent les flux de travail et améliorent l'efficacité globale des opérations de contrôle de version.

### `git config --global` [`user.name`](http://user.name) `"Votre Nom"`

Définit le nom d'utilisateur au niveau global.

### `git config --global` [`user.email`](http://user.email) `"votre_email@example.com"`

Définit l'e-mail de l'utilisateur au niveau global.

### `git config --global core.editor <editor>`

Définit l'éditeur de texte par défaut.

### `git config --global core.excludesfile <file>`

Définit le fichier d'exclusion (ignore) global.

### `git config --list`

Liste tous les paramètres de configuration.

### `git config --list --show-origin`

Liste toutes les variables de configuration, en indiquant leur origine.

### `git config <key>`

Récupère la valeur pour la clé spécifiée.

### `git config --get <key>`

Récupère la valeur pour la clé de configuration spécifiée.

### `git config --unset <key>`

Supprime la clé de configuration spécifiée.

### `git config --global --unset <key>`

Supprime la clé de configuration spécifiée globalement.

## **Sécurité Git**

La sécurité GPG dans Git implique l'utilisation de GNU Privacy Guard (GPG) pour signer les commits et les tags, garantissant leur authenticité et leur intégrité. En configurant une clé GPG et en activant la signature automatique, vous pouvez vérifier que les commits et les tags ont été créés par une source de confiance. Cela aide à prévenir les altérations et garantit l'intégrité de l'historique du dépôt.

Cette pratique renforce la sécurité en fournissant une assurance cryptographique que les modifications proviennent d'un contributeur légitime.

### `git config --global user.signingKey <key>`

Configure la clé GPG pour signer les commits et les tags.

### `git config --global commit.gpgSign true`

Signe automatiquement tous les commits avec GPG.

## **Comment définir des alias dans Git**

Les alias Git sont des raccourcis personnalisés que vous pouvez créer pour simplifier et accélérer votre flux de travail en associant des commandes Git plus longues à des noms plus courts et plus mémorisables.

En configurant des alias dans vos paramètres Git, vous pouvez exécuter rapidement les commandes fréquemment utilisées en tapant moins. Cela améliore non seulement la productivité, mais réduit également le risque d'erreurs.

Par exemple, vous pouvez définir un alias comme `git st` pour remplacer `git status`, ou `git co` pour remplacer `git checkout`.

Vous pouvez définir des alias globalement pour qu'ils s'appliquent à tous les dépôts ou localement pour des projets individuels, offrant ainsi une flexibilité dans la rationalisation de vos opérations Git.

### `git config --global alias.ci commit`

Définit `git ci` comme alias pour `git commit`.

### `git config --global alias.st status`

Définit `git st` comme alias pour `git status`.

### `git config --global alias.co checkout`

Définit `git co` comme alias pour `git checkout`.

### `git config --global alias.br branch`

Définit `git br` comme alias pour `git branch`.

### `git config --global alias.graph "log --graph --all --oneline --decorate"`

Crée un alias pour un graphique détaillé de l'historique du dépôt.

## **Rebasing dans Git**

Le rebasing Git réapplique vos modifications par-dessus l'historique d'une autre branche, créant un historique de projet plus propre et plus linéaire.

En pratique, cela aide à intégrer les mises à jour en douceur en évitant les commits de fusion inutiles, garantissant que la séquence des commits est simple et facilitant la compréhension de l'évolution du projet.

### `git rebase <branch>`

La commande `git rebase` est utilisée pour réappliquer des commits sur une autre pointe de base. Elle vous permet de déplacer ou de combiner une séquence de commits vers un nouveau commit de base. C'est couramment utilisé pour :

1. Maintenir un historique de projet linéaire.
    
2. Intégrer les modifications d'une branche dans une autre.
    
3. Mettre à jour une branche de fonctionnalité avec les dernières modifications de la branche principale.
    

L'utilisation de base est `git rebase <branch>`, qui rebasera la branche actuelle sur la branche spécifiée.

### `git rebase --interactive <branch>`

Démarre une session de rebase interactif, vous permettant de modifier les commits à partir de la &lt;base&gt; jusqu'au HEAD actuel. Cela vous permet de réordonner, fusionner (squash), éditer ou supprimer des commits, offrant un moyen de nettoyer et d'affiner l'historique des commits avant de pousser les modifications. Version courte : `git rebase -i <branch>`

### `git rebase --continue`

Continue le processus de rebase après avoir résolu les conflits.

### `git rebase --abort`

Interrompt le processus de rebase et revient à la branche d'origine.

### `git fetch --rebase`

Récupère les données du dépôt distant et rebase les modifications locales.

## **Qu'est-ce que le Cherry-Picking ?**

Le cherry-picking Git est un processus qui vous permet d'appliquer les modifications introduites par un commit spécifique d'une branche dans une autre branche. C'est particulièrement utile lorsque vous souhaitez incorporer sélectivement des modifications individuelles de différentes branches sans fusionner l'intégralité de la branche.

En utilisant la commande `git cherry-pick`, vous pouvez isoler et intégrer uniquement les commits souhaités, garantissant que des modifications spécifiques sont incluses dans votre branche actuelle tout en évitant les conflits potentiels et les modifications indésirables d'autres parties de la branche.

### `git cherry-pick <commit>`

Applique les modifications introduites par un commit existant.

### `git cherry-pick --continue`

Continue le cherry-picking après avoir résolu les conflits.

### `git cherry-pick --abort`

Interrompt le processus de cherry-picking.

### `git cherry-pick --no-commit <commit>`

Effectue un cherry-pick d'un commit sans valider automatiquement, permettant d'autres modifications. Version courte : `git cherry-pick -n <commit>`

## **Le patching dans Git**

Le patching Git est une méthode utilisée pour appliquer des modifications d'un dépôt à un autre ou d'une branche à une autre au sein du même dépôt. Cela implique la création de fichiers patch, qui sont des fichiers texte représentant les différences entre les commits ou les branches. Ces fichiers patch peuvent ensuite être appliqués à un dépôt à l'aide de commandes telles que `git apply` ou `git am`, permettant de transférer et d'intégrer des modifications sans fusionner directement les branches.

Le patching est particulièrement utile pour partager des modifications ou des mises à jour spécifiques sur différentes bases de code, en garantissant que seules les modifications prévues sont appliquées.

### `git apply <patch_file>`

Applique les modifications au répertoire de travail à partir d'un fichier patch.

### `git apply --check`

Vérifie si les patchs peuvent être appliqués proprement.

### `git format-patch <since_commit>`

Crée des fichiers patch pour chaque commit depuis le commit spécifié.

### `git am <patch_file>`

Applique des patchs à partir d'une boîte aux lettres (mailbox).

### `git am --continue`

Continue l'application des patchs après avoir résolu les conflits.

### `git am --abort`

Interrompt le processus d'application du patch.

### `git diff > <file.patch>`

Crée un fichier patch à partir des différences.

## **Dates relatives dans Git**

Les dates relatives dans Git permettent aux utilisateurs de se référer à des points spécifiques de l'historique du dépôt en utilisant des expressions temporelles lisibles par l'homme. Par exemple, des commandes comme `main@{1.week.ago}` ou `@{3.days.ago}` vous permettent d'accéder à l'état d'une branche ou de visualiser les modifications apportées depuis une certaine période par rapport à la date actuelle.

Cette fonctionnalité simplifie la navigation dans la chronologie du dépôt en utilisant des termes intuitifs comme "hier", "il y a 2 semaines" ou des dates spécifiques, facilitant ainsi le suivi et la gestion de l'évolution de la base de code sans avoir besoin de se souvenir des hashs de commit exacts ou des horodatages.

### `git show main@{1.week.ago}`

Permet de voir l'état de votre branche principale il y a une semaine.

### `git diff @{3.days.ago}`

Affiche les modifications que vous avez apportées au cours des 3 derniers jours.

### `git checkout main@{2.weeks.ago}`

Extrait votre dépôt tel qu'il était il y a 2 semaines.

### `git log @{1.month.ago}..HEAD`

Affiche le journal des commits depuis 1 mois jusqu'à maintenant.

### `@{2024-06-01}`

### `@{yesterday}`

### `@{"1 week 2 days ago"}`

Autres exemples d'utilisation.

## **Git Blame**

Le "blaming" Git est une fonctionnalité qui identifie la dernière modification apportée à chaque ligne d'un fichier, en attribuant les changements à des commits et des auteurs spécifiques. Vous pouvez le faire en utilisant la commande `git blame`, qui fournit une annotation détaillée du fichier, montrant qui a apporté des modifications et quand elles ont été effectuées.

Cet outil est particulièrement utile pour suivre l'historique d'un fichier, comprendre l'évolution du code et identifier la source des bugs ou des changements.

En identifiant précisément le commit et l'auteur responsables de chaque ligne, les développeurs peuvent obtenir des informations sur le processus de développement et faciliter une meilleure collaboration et responsabilité au sein d'une équipe.

### `git blame <file>`

Affiche la dernière modification pour chaque ligne d'un fichier.

### `git blame <file> -L <start>,<end>`

Limite la sortie de blame à la plage de lignes spécifiée.

### `git blame <file> <commit>`

Affiche les informations de blame jusqu'au commit spécifié.

### `git blame <file> -C -C`

Affiche quelles révisions et quels auteurs ont modifié chaque ligne d'un fichier pour la dernière fois, avec détection de copie.

L'option `-C` détecte les lignes déplacées ou copiées au sein du même fichier. L'utiliser une fois (`-C`) détecte les lignes déplacées ou copiées dans le même fichier. Utiliser l'option `-C` deux fois (`-C -C`) incite Git à inspecter les fichiers non modifiés comme candidats pour la source de la copie. Cela signifie qu'il essaiera de trouver l'origine des lignes copiées non seulement dans le même fichier mais aussi dans d'autres fichiers.

### `git blame <file> --reverse`

Travaille à l'envers, montrant qui a modifié chaque ligne pour la dernière fois dans le fichier spécifié.

### `git blame <file> --first-parent`

Montre qui a modifié le plus récemment chaque ligne d'un fichier, en suivant uniquement le premier commit parent pour les changements de fusion.

## **Archivage dans Git**

L'archivage Git est une fonctionnalité qui vous permet de créer des fichiers d'archive, tels que .tar ou .zip, contenant le contenu d'un commit, d'une branche ou d'un tag spécifique. C'est utile pour emballer un instantané de votre dépôt à un moment précis, vous permettant de distribuer ou de sauvegarder l'état du dépôt sans inclure tout l'historique Git.

La commande `git archive` est généralement utilisée à cette fin, offrant un moyen pratique d'exporter l'état actuel du projet dans un format portable.

### `git archive <format> <tree-ish>`

Crée un fichier d'archive (par exemple, un fichier .tar ou .zip) contenant le contenu de l'objet tree-ish spécifié (comme un commit, une branche ou un tag) dans le format donné. Par exemple :

* `git archive --format=tar HEAD` crée une archive .tar du commit actuel (HEAD).
    
* `git archive --format=zip v1.0` crée une archive .zip des fichiers du tag v1.0.
    

Cette commande est utile pour emballer un instantané de votre dépôt à un moment précis.

## **Comment suivre des fichiers dans Git**

Le suivi Git fait référence au processus de surveillance et de gestion des fichiers dans un dépôt.

La commande `git ls-files` liste tous les fichiers qui sont suivis par Git, offrant une vue claire des fichiers actuellement sous contrôle de version. D'un autre côté, `git ls-tree <branch>` affiche le contenu d'un objet arbre pour une branche spécifiée, montrant la structure et les fichiers à ce point du dépôt.

Ensemble, ces commandes aident les développeurs à comprendre quels fichiers sont inclus dans le dépôt et comment ils sont organisés, garantissant un suivi et une gestion efficaces de la base de code du projet.

### `git ls-files`

Liste tous les fichiers suivis.

### `git ls-tree <branch>`

Liste le contenu d'un objet arbre.

## **Manipulation de l'index dans Git**

La manipulation de l'index Git implique la gestion de la zone de transit (également appelée l'index) où les modifications sont préparées avant d'être validées. Cela peut inclure le marquage de fichiers comme "assume unchanged" (supposé inchangé) pour ignorer temporairement les modifications, ou la réinitialisation de ces marquages pour suivre à nouveau les modifications.

Les commandes de manipulation de l'index, telles que `git update-index`, vous permettent de contrôler quels fichiers sont inclus dans le prochain commit, offrant une flexibilité dans la gestion des changements et optimisant le flux de travail pour des tâches spécifiques.

### `git update-index --assume-unchanged <file>`

Marque un fichier comme étant supposé inchangé.

### `git update-index --no-assume-unchanged <file>`

Enlève le marquage d'un fichier supposé inchangé.

## **Squashing dans Git**

Le squashing Git est le processus de combinaison de plusieurs commits en un seul. Les développeurs font souvent cela pour nettoyer l'historique des commits avant de fusionner les modifications dans une branche principale, rendant l'historique plus concis et plus facile à lire.

Le squashing peut être effectué à l'aide de la commande de rebase interactif (`git rebase -i`), qui vous permet de fusionner, réordonner ou éditer les commits de manière sélective. En écrasant (squashing) les commits, vous pouvez consolider les changements redondants ou mineurs, présentant un récit plus clair du processus de développement.

### `git rebase -i HEAD~<n>`

Écrase (squash) les commits de manière interactive.

## **Intégrité des données dans Git**

L'intégrité des données dans Git fait référence aux mécanismes et processus que Git utilise pour garantir la précision et la cohérence des données au sein d'un dépôt.

Git utilise des hachages cryptographiques (SHA-1 ou SHA-256) pour identifier de manière unique les objets tels que les commits, les arbres et les blobs. Ce hachage fournit non seulement un identifiant unique pour chaque objet, mais garantit également que toute modification du contenu de l'objet entraînera un hachage différent, détectant ainsi toute corruption ou altération.

Vous pouvez utiliser des commandes comme `git fsck` pour vérifier la connectivité et la validité des objets dans la base de données, garantissant la santé globale et l'intégrité du dépôt.

### `git fsck`

Vérifie la connectivité et la validité des objets dans la base de données.

### `git fsck --unreachable`

Trouve les objets du dépôt qui ne sont accessibles à partir d'aucune référence.

### `git prune`

Supprime les objets inaccessibles.

### `git gc`

Exécute un processus de ramasse-miettes (garbage collection).

Le ramasse-miettes Git est un processus de maintenance qui nettoie et optimise le dépôt en supprimant les fichiers inutiles et en compressant les révisions de fichiers pour gagner de l'espace. Ce processus, déclenché par la commande `git gc`, consolide et supprime les objets inaccessibles, tels que les commits orphelins et les blobs non référencés, garantissant que le dépôt reste efficace et performant.

Un ramasse-miettes régulier aide à gérer efficacement le stockage et maintient la structure du dépôt organisée.

## **Nettoyage dans Git**

Le nettoyage dans Git consiste à supprimer les fichiers, références et branches inutiles qui ne sont plus nécessaires. Cela aide à garder votre dépôt organisé et efficace.

Les activités de nettoyage régulières, telles que l'élagage (pruning) des branches de suivi à distance, la suppression des fichiers non suivis et le retrait des références obsolètes, garantissent que votre dépôt reste gérable et exempt de désordre.

En pratique, ces actions peuvent améliorer les performances, réduire les besoins de stockage et faciliter la navigation et le travail au sein de votre projet.

### `git fetch --prune`

Supprime les références qui n'existent plus sur le remote.

### `git remote prune <name>`

Élague toutes les branches de suivi à distance obsolètes.

### `git fetch origin --prune`

Nettoie les références obsolètes du dépôt distant.

### `git clean -f`

Supprime les fichiers non suivis du répertoire de travail, forçant la suppression des fichiers qui ne sont pas suivis par Git.

### `git clean -fd`

Supprime les fichiers et répertoires non suivis du répertoire de travail, y compris tous les fichiers et répertoires non suivis par Git.

### `git clean -i`

Entre en mode interactif pour nettoyer les fichiers non suivis.

### `git clean -X`

Supprime uniquement les fichiers ignorés du répertoire de travail.

## **Git Subtree**

Git subtree est un mécanisme permettant de gérer et d'intégrer des sous-projets dans un dépôt principal. Contrairement aux submodules, qui traitent le sous-projet comme une entité séparée avec son propre dépôt, les subtrees vous permettent d'inclure le contenu d'un autre dépôt directement dans un sous-répertoire de votre dépôt principal.

Cette approche simplifie le flux de travail en éliminant le besoin de dépôts multiples et en permettant l'intégration, la fusion et la récupération (pull) transparentes des mises à jour du sous-projet. Les subtrees offrent un moyen flexible et pratique de gérer les dépendances et de collaborer sur des projets nécessitant l'incorporation de bases de code externes.

### `git subtree add --prefix=<dir> <repository> <branch>`

Ajoute un dépôt en tant que subtree.

### `git subtree merge --prefix=<dir> <branch>`

Fusionne un subtree.

### `git subtree pull --prefix=<dir> <repository> <branch>`

Récupère les nouveaux changements du dépôt du subtree.

## **How to Search in Git**

`git grep` est une puissante commande de recherche dans Git qui permet aux utilisateurs de rechercher des chaînes de caractères ou des motifs spécifiques dans les fichiers d'un dépôt. Elle effectue la recherche dans le répertoire de travail et l'index, offrant un moyen rapide et efficace de localiser les occurrences d'un motif spécifié à travers plusieurs fichiers.

Cette commande est particulièrement utile pour les développeurs cherchant à trouver des instances de code, des commentaires ou du texte au sein d'un projet, leur permettant de naviguer et de comprendre facilement de grandes bases de code. Avec diverses options et drapeaux, `git grep` vous permet d'effectuer des recherches ciblées, ce qui en fait un outil essentiel pour l'analyse et la maintenance du code.

### `git grep <pattern>`

Recherche une chaîne de caractères dans le répertoire de travail et l'index.

### `git grep -e <pattern>`

Recherche un motif spécifique.

## **Bisecting dans Git**

Le bisecting Git est un puissant outil de débogage qui aide à identifier le commit spécifique ayant introduit un bug ou un problème dans un projet. En effectuant une recherche binaire dans l'historique des commits, `git bisect` réduit efficacement la plage des commits problématiques potentiels.

Le processus consiste à marquer un commit connu comme bon et un commit connu comme mauvais, puis à tester de manière répétée les commits intermédiaires pour déterminer s'ils sont bons ou mauvais.

Cette approche itérative isole rapidement le commit défectueux, permettant aux développeurs de localiser le changement exact qui a causé le problème. Cela facilite un débogage plus rapide et plus précis.

### `git bisect start`

Démarre une session de bisect.

### `git bisect bad`

Marque la version actuelle comme mauvaise.

### `git bisect good <commit>`

Marque le commit spécifié comme bon.

### `git bisect reset`

Termine une session de bisect et revient à la branche d'origine.

### `git bisect visualize`

Lance un outil visuel pour aider au bisecting.

## **Attributs Git**

Les attributs Git sont des paramètres qui définissent comment Git doit gérer des fichiers ou des chemins spécifiques au sein d'un dépôt. Ces attributs sont définis dans un fichier nommé `.gitattributes`, et ils peuvent contrôler divers comportements tels que l'encodage du texte, la normalisation des fins de ligne, les stratégies de fusion et les algorithmes de diff.

En définissant des attributs, vous pouvez garantir un comportement cohérent à travers différents environnements et collaborateurs, facilitant ainsi la gestion des fichiers ayant des exigences ou des complexités particulières.

Par exemple, vous pouvez marquer certains fichiers comme binaires pour empêcher Git d'essayer de les fusionner, ou spécifier des pilotes de diff personnalisés pour des comparaisons plus significatives.

### `git check-attr <attribute> -- <file>`

Affiche la valeur d'un attribut spécifique pour le fichier donné tel que défini dans la configuration `.gitattributes`, vous aidant à comprendre comment Git traite le fichier en ce qui concerne des attributs tels que l'encodage du texte, le comportement de fusion ou la gestion du diff.

## **Git Checkout**

`git checkout` est une commande polyvalente dans Git utilisée pour basculer entre différentes branches, tags ou commits au sein d'un dépôt. En mettant à jour le répertoire de travail et l'index pour qu'ils correspondent à la branche ou au commit spécifié, elle vous permet de visualiser ou de travailler avec l'état du dépôt à ce point.

Vous pouvez également utiliser `git checkout` pour créer de nouvelles branches, restaurer des fichiers spécifiques à partir d'un commit, ou même démarrer une nouvelle branche sans historique en utilisant l'option `--orphan`. Cette commande est essentielle pour naviguer et gérer les différentes versions de la base de code d'un projet.

### `git checkout <commit>`

Met à jour le répertoire de travail et l'index pour correspondre au commit spécifié, vous permettant de visualiser ou de travailler avec l'état du dépôt à ce commit. Gardez simplement à l'esprit que cela vous laisse dans un état de "HEAD détachée" (detached HEAD), ce qui signifie que vous n'êtes sur aucune branche.

### `git checkout -b <branch> <commit>`

Crée une nouvelle branche nommée &lt;branch&gt; à partir du commit spécifié et bascule sur cette branche, vous permettant de commencer à travailler à partir de ce point de l'historique des commits.

### `git checkout <commit> -- <file>`

Restaure le fichier spécifié à partir d'un commit particulier dans votre répertoire de travail, remplaçant la version actuelle du fichier par la version de ce commit sans modifier l'historique des commits ou l'index.

### `git checkout --orphan <new_branch>`

Crée une nouvelle branche nommée &lt;new\_branch&gt; sans historique de commit, démarrant ainsi une nouvelle branche qui commence avec un répertoire de travail et un index propres, comme s'il s'agissait d'un nouveau dépôt.

## **Git Reflog**

Git reflog est un outil puissant qui enregistre toutes les modifications apportées aux pointes des branches et à la référence HEAD dans un dépôt Git. Cela inclut des actions telles que les commits, les checkouts, les merges et les resets.

En maintenant un historique de ces changements, le reflog permet aux utilisateurs de suivre les modifications récentes et de récupérer des commits perdus, même s'ils ne font pas partie de l'historique de la branche actuelle. Il fournit un moyen de naviguer à travers les changements d'état du dépôt, ce qui en fait une ressource inestimable pour le débogage et l'annulation d'erreurs.

### `git reflog`

Affiche un journal de toutes les modifications apportées à la référence HEAD et aux pointes de branches, y compris les commits, les checkouts, les merges et les resets, vous permettant de récupérer des commits perdus ou de suivre les modifications récentes de l'état du dépôt.

### `git reflog show <ref>`

Affiche le reflog pour la référence spécifiée (&lt;ref&gt;), montrant un journal des modifications apportées à cette référence, y compris les mises à jour de HEAD ou des pointes de branches, ainsi que les messages de commit et les horodatages associés.

## **Comment gérer les fichiers non suivis dans Git**

### `git clean`

`git clean` supprime les fichiers et répertoires non suivis du répertoire de travail. Par défaut, il affiche seulement ce qui serait supprimé sans rien effacer réellement.

Pour effectuer le nettoyage réel, vous devez utiliser des drapeaux supplémentaires :

* `git clean -f`: Supprime les fichiers non suivis.
    
* `git clean -fd`: Supprime les fichiers et répertoires non suivis.
    
* `git clean -fx`: Supprime les fichiers non suivis, y compris ceux ignorés par .gitignore.
    
* `git clean -n`: Affiche quels fichiers seraient supprimés sans les supprimer réellement.
    

## **Force Pushing dans Git**

### `git push --force`

Force une poussée (push) de votre branche locale vers le dépôt distant, même si cela entraîne une fusion non-avance rapide (non-fast-forward). Cela écrase la branche distante avec vos modifications locales.

Cela peut être nécessaire lorsque vous avez réécrit l'historique (par exemple, avec un rebase) et que vous devez mettre à jour la branche distante pour qu'elle corresponde à votre branche locale. Mais cela peut également potentiellement écraser les modifications des autres – utilisez-le donc avec prudence.

## **Git Fetch et Pull**

### `git fetch --all`

Récupère les mises à jour de tous les dépôts distants configurés pour votre dépôt local, récupérant les modifications de toutes les branches et tags sans modifier vos branches locales.

### `git pull --rebase`

Récupère les modifications du dépôt distant et rebase vos commits locaux par-dessus la branche distante mise à jour, au lieu de les fusionner. Cela maintient l'historique des commits linéaire et évite les commits de fusion inutiles.

## **Comment gérer les conflits de fusion dans Git**

Gérer les conflits de fusion dans Git est une compétence essentielle pour collaborer sur des projets avec plusieurs contributeurs.

Les conflits de fusion surviennent lorsque les modifications dans différentes branches ou commits se chevauchent ou se contredisent, empêchant une fusion automatique. La résolution de ces conflits implique de réviser et de concilier manuellement les différences pour s'assurer que le code final intègre avec précision les contributions de toutes les parties.

En pratique, la gestion efficace des conflits de fusion aide à maintenir l'intégrité du code et facilite une collaboration fluide en garantissant que les modifications de chacun sont correctement incorporées dans l'historique du projet.

### `git mergetool`

Lance un outil de fusion pour vous aider à résoudre les conflits qui surviennent lors d'une fusion ou d'un rebase. Il ouvre une interface graphique ou un outil textuel configuré dans vos paramètres Git, vous permettant de résoudre manuellement les conflits et de finaliser la fusion.

### `git rerere`

`rerere` signifie "reuse recorded resolution" (réutiliser la résolution enregistrée) et est une fonctionnalité qui aide à résoudre automatiquement les conflits lors de futures fusions ou rebases en réutilisant les résolutions de conflits que vous avez précédemment enregistrées.

Une fois activé, Git enregistre comment vous avez résolu les conflits. Si les mêmes conflits se reproduisent, il peut appliquer automatiquement les mêmes résolutions.

## **Working Trees dans Git**

Les working trees dans Git vous permettent d'avoir plusieurs répertoires de travail associés à un seul dépôt. C'est particulièrement utile pour travailler simultanément sur plusieurs branches sans avoir besoin de changer constamment de branche dans le même répertoire.

En utilisant les working trees, vous pouvez facilement gérer différentes fonctionnalités, corrections de bugs ou expérimentations dans des environnements isolés, améliorant ainsi l'efficacité du flux de travail et réduisant le risque de conflits.

### `git worktree add ../new-branch feature-branch`

Crée un nouvel arbre de travail (working tree) dans un répertoire nommé "new-branch" basé sur la branche "feature-branch".

### `git worktree list`

Liste tous les arbres de travail associés au dépôt actuel, affichant leurs chemins et les branches sur lesquelles ils sont extraits.

### `git worktree remove <path>`

Supprime l'arbre de travail spécifié au &lt;path&gt; donné, effaçant le répertoire de travail et détachant la branche.

### `git worktree prune`

Supprime les références aux arbres de travail inexistants, nettoyant la liste des arbres de travail.

### `git worktree lock <path>`

Verrouille l'arbre de travail spécifié au &lt;path&gt; donné, empêchant son élagage (pruning).

### `git worktree unlock <path>`

Deverrouille l'arbre de travail spécifié au &lt;path&gt; donné, permettant son élagage si nécessaire.

## **Sous-modules (Submodules) dans Git**

Les sous-modules (submodules) dans Git sont un moyen d'inclure et de gérer des dépôts distants au sein de votre propre dépôt. Ils sont particulièrement utiles pour réutiliser du code sur plusieurs projets, maintenir des dépendances ou intégrer des bibliothèques tierces.

En utilisant des submodules, vous pouvez garder votre dépôt principal propre et modulaire, tout en vous assurant que tous les composants nécessaires sont inclus et contrôlés en version.

### `git submodule init`

Initialise les submodules dans votre dépôt. Cette commande configure le nécessaire pour les submodules, mais ne les clone pas réellement.

### `git submodule update`

Clone et extrait les submodules dans les chemins spécifiés. Ceci est généralement exécuté après `git submodule init`.

### `git submodule add <repository> <path>`

Ajoute un nouveau submodule à votre dépôt au chemin spécifié, en le liant au dépôt spécifié.

### `git submodule status`

Affiche l'état de tous les submodules, montrant leurs hashs de commit et s'ils sont à jour, modifiés ou non initialisés.

### `git submodule foreach <command>`

Exécute la commande spécifiée dans chaque submodule. C'est utile pour effectuer des opérations par lots sur tous les submodules.

### `git submodule sync`

Synchronise les URL des submodules dans votre fichier de configuration avec celles du fichier `.gitmodules`, garantissant qu'elles sont à jour.

### `git submodule deinit <path>`

Désenregistre le submodule spécifié, supprimant sa configuration. Cela ne supprime pas le répertoire de travail du submodule.

### `git submodule update --remote`

Récupère et met à jour les submodules vers le dernier commit de leurs dépôts distants.

### `git submodule set-url <path> <newurl>`

Modifie l'URL du submodule spécifié vers la nouvelle URL.

### `git submodule absorbgitdirs`

Absorbe le répertoire Git du submodule dans le projet parent (superproject) pour simplifier la structure.

Merci de votre lecture ! J'espère que cet aide-mémoire vous aidera à travailler plus facilement avec Git.