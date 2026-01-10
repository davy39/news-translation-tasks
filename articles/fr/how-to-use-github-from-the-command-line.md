---
title: Qu'est-ce que la GitHub CLI ? Comment utiliser GitHub depuis la ligne de commande
subtitle: ''
author: AYUSH MISHRA
co_authors: []
series: null
date: '2025-09-26T16:51:19.071Z'
originalURL: https://freecodecamp.org/news/how-to-use-github-from-the-command-line
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758905411969/b1506cff-650a-4098-bd70-e8bb3b0bcb9a.png
tags:
- name: GitHub
  slug: github
- name: Git
  slug: git
- name: terminal
  slug: terminal
- name: command line
  slug: command-line
seo_title: Qu'est-ce que la GitHub CLI ? Comment utiliser GitHub depuis la ligne de
  commande
seo_desc: The GitHub CLI (Command Line Interface) is a powerful tool developed by
  GitHub that allows developers to interact with GitHub directly from the terminal.
  It provides a simple way to perform many GitHub tasks without leaving the command
  line interface...
---

La GitHub CLI (Command Line Interface) est un outil puissant développé par GitHub qui permet aux développeurs d'interagir avec GitHub directement depuis le terminal. Elle offre un moyen simple d'effectuer de nombreuses tâches GitHub sans quitter l'interface de ligne de commande, comme la gestion des dépôts, le traitement des pull requests et des tickets (issues), le travail avec GitHub Actions, et bien plus encore.

Dans ce tutoriel, vous apprendrez ce qu'est la GitHub CLI, comment l'installer et la configurer, et comment l'utiliser pour des tâches quotidiennes telles que la création de dépôts, la gestion des tickets et des pull requests, l'utilisation de GitHub Actions et l'automatisation des tâches à l'aide d'alias personnalisés. Vous apprendrez comment remplacer certaines fonctionnalités de l'interface web de GitHub par des commandes rapides dans votre terminal.

## **Voici ce que nous allons aborder :**

* [Aperçu de la GitHub CLI](#heading-apercu-de-la-github-cli)
    
* [Fonctionnalités clés](#heading-fonctionnalites-cles-de-la-github-cli)
    
* [Avantages de l'utilisation de la GitHub CLI](#heading-avantages-de-l-utilisation-de-la-github-cli)
    
* [Installation et configuration](#heading-installation-et-configuration)
    
* [Authentification avec un compte GitHub](#authentification-avec-un-compte-github)
    
* [Navigation dans la GitHub CLI](#heading-navigation-dans-la-github-cli)
    
* [Gestion des dépôts](#heading-comment-gerer-les-depots-avec-la-github-cli)
    
* [Travailler avec les pull requests et les tickets](#heading-gestion-des-branches-et-des-pull-requests)
    
* [Pousser et tirer les modifications](#heading-pousser-et-tirer-les-modifications)
    
* [Travailler avec GitHub Actions](#heading-travailler-avec-github-actions)
    
* [Gestion des Gists](#heading-comment-gerer-les-gists-avec-la-github-cli)
    
* [Releases et Tags](#heading-interaction-avec-les-releases-et-les-tags)
    
* [Scripts personnalisés et alias](#heading-comment-etendre-la-github-cli-avec-des-scripts-personnalises-et-des-alias)
    
* [Dépannage](#heading-depannage-des-problemes-courants)
    
* [Conclusion](#heading-conclusion)
    

## Aperçu de la GitHub CLI

Vous pouvez utiliser la GitHub CLI pour combler le fossé entre l'interface web de GitHub et votre environnement local. Vous pouvez effectuer diverses tâches telles que la création de tickets, la gestion de dépôts ou même la vérification de l'état de vos workflows GitHub Actions à l'aide de la CLI. En utilisant la CLI, vous pouvez effectuer presque toutes les tâches que vous pourriez accomplir sur le site web de GitHub.

### Fonctionnalités clés de la GitHub CLI

* **Gestion des dépôts :** Créez, clonez, visualisez et gérez facilement vos dépôts.
    
* **Pull requests et tickets (issues) :** Gérez les pull requests et les tickets directement depuis le terminal, y compris leur création, leur fusion et leur listage.
    
* **GitHub Actions :** Interagissez avec les workflows et gérez les exécutions de workflows.
    
* **Authentification :** Fournit un moyen sécurisé de s'authentifier avec votre compte GitHub, prenant en charge les clés SSH, les jetons (tokens) et OAuth.
    
* **Scripting personnalisé :** Vous permet de créer des scripts personnalisés et des alias pour automatiser les tâches répétitives et optimiser les processus de développement.
    

### Avantages de l'utilisation de la GitHub CLI

Supposons que vous travailliez sur un projet et que vous deviez créer un nouveau ticket sur GitHub. Normalement, vous devriez passer à votre navigateur, vous connecter à GitHub, naviguer vers le dépôt, cliquer sur l'onglet \"Issues\", puis cliquer sur \"New Issue\". Avec la GitHub CLI, vous pouvez faire tout cela en tapant une seule commande, sans jamais quitter votre terminal. Cela rend votre flux de travail plus rapide et fait gagner du temps.

## Installation et configuration

Pour installer la GitHub CLI sur Windows, vous pouvez utiliser le gestionnaire de paquets winget. Winget est un outil en ligne de commande qui vous permet d'installer des logiciels facilement.

### **Installation de la GitHub CLI sur Windows, macOS et Linux**

### **Windows :**

Exécutez la commande ci-dessous :

```plaintext
winget install --id GitHub.cli
```

* `winget install` **:** Indique à Windows d'installer un nouveau paquet logiciel.
    
* `--id GitHub.cli` **:** Spécifie l'ID exact du paquet pour la GitHub CLI.
    

Après avoir exécuté cette commande, la GitHub CLI sera installée sur votre système Windows.

### macOS :

Vous pouvez utiliser Homebrew pour installer la GitHub CLI sur macOS. Ouvrez votre terminal et exécutez :

```plaintext
brew install gh
```

### Linux :

Sur Linux, vous pouvez utiliser votre gestionnaire de paquets. Par exemple, sur Ubuntu, vous pouvez exécuter :

```plaintext
sudo apt install gh
```

### Authentification avec un compte GitHub

Après avoir installé la GitHub CLI, l'étape suivante consiste à l'authentifier avec votre compte GitHub.

#### Exécuter la commande d'authentification :

Tapez `gh auth login` dans le terminal et appuyez sur Entrée.

```plaintext
gh auth login
```

Vous serez ensuite invité à sélectionner une méthode d'authentification. L'option recommandée est de s'authentifier via un navigateur web.

Si vous sélectionnez la méthode par navigateur, la GitHub CLI ouvrira un lien dans votre navigateur par défaut, où vous pourrez vous connecter à GitHub.

#### Terminer l'authentification :

Après vous être connecté, le navigateur confirmera que la GitHub CLI est connectée à votre compte.

Vous pouvez vérifier le statut de l'authentification en exécutant :

```plaintext
gh auth status
```

## Navigation dans la GitHub CLI

La GitHub CLI est facile à naviguer et sa structure de commande est intuitive.

### Structure et syntaxe des commandes

Les commandes de la GitHub CLI suivent un modèle simple et direct :

```plaintext
gh [command] [subcommand] [flags]
```

* **Command :** L'action principale que vous souhaitez effectuer (par exemple, repo, issue, pr).
    
* **Subcommand :** Une tâche spécifique au sein de la commande (par exemple, create, list, view).
    
* **Flags :** Paramètres optionnels qui modifient le comportement de la commande (par exemple, --title, --body).
    

### Commandes et drapeaux (flags) couramment utilisés

Voici quelques commandes courantes de la GitHub CLI :

* **Créer un dépôt :** `gh repo create`
    
* **Lister les tickets :** `gh issue list`
    
* **Créer une pull request :** `gh pr create`
    
* **Voir les détails d'un dépôt :** `gh repo view`
    

Pour voir toutes les commandes et options disponibles, vous pouvez toujours exécuter :

```plaintext
gh help
```

## Comment gérer les dépôts avec la GitHub CLI

Passons en revue des exemples de certaines des commandes que vous utiliserez le plus souvent.

### Création et clonage de dépôts

Pour créer un nouveau dépôt GitHub directement depuis le terminal, utilisez simplement la commande suivante :

```plaintext
gh repo create my-repo-name
```

Pour cloner un dépôt existant, utilisez la commande suivante :

```plaintext
gh repo clone owner/repo-name
```

### Gestion des branches et des pull requests

La GitHub CLI vous permet de gérer les tickets et les pull requests (PR) sans quitter le terminal.

Changer de branche ou créer des pull requests est simple. Pour créer une nouvelle branche :

```plaintext
git checkout -b new-branch-name
```

Ensuite, pour créer une pull request :

```plaintext
gh pr create --title "Your PR Title" --body "Description of your PR"
```

### Pousser et tirer les modifications

Poussez vos modifications vers GitHub avec cette commande :

```plaintext
git push origin branch-name
```

Et tirez les dernières modifications avec :

```plaintext
git pull
```

### Travailler avec GitHub Actions

La GitHub CLI prend également en charge GitHub Actions, vous permettant de gérer les workflows directement depuis votre terminal.

Vous pouvez déclencher manuellement des workflows en utilisant ce qui suit :

```plaintext
gh workflow run workflow-name
```

Et vous pouvez surveiller l'état des workflows avec :

```plaintext
gh run list
```

Pour voir les logs détaillés d'un workflow, exécutez ceci :

```plaintext
gh run view run-id --log
```

### Clonage et fork de dépôts

Le clonage et le forking sont des tâches essentielles lorsque vous travaillez sur des projets provenant d'autres dépôts.

Pour cloner un dépôt, utilisez cette commande :

```plaintext
gh repo clone <repository-name>
```

Pour forker un dépôt, faites ceci :

```plaintext
gh repo fork <repository-url>
```

#### **Exemple :**

Voici à quoi cela ressemblerait :

```plaintext
gh repo clone example-repo
```

```plaintext
gh repo fork https://github.com/username/repository-name
```

### Comment travailler avec GitHub Actions

En utilisant la GitHub CLI, vous pouvez également gérer GitHub Actions, qui sont des tâches automatisées que vous pouvez exécuter en réponse à certains événements dans votre dépôt.

#### Déclenchement et surveillance des workflows

Vous pouvez déclencher un workflow manuellement comme ceci :

```plaintext
gh workflow run <workflow-name>
```

Et vous pouvez surveiller les exécutions de workflow avec ceci :

```plaintext
gh run list
```

#### Gestion des exécutions de workflow et des logs

Si vous souhaitez vérifier les détails d'une exécution de workflow spécifique, vous pouvez consulter les logs directement depuis la CLI :

```plaintext
gh run view <run-id> --log
```

Vous pouvez également utiliser les commandes de la GitHub CLI pour améliorer vos pipelines d'Intégration Continue/Déploiement Continu (CI/CD), assurant une automatisation fluide et un meilleur contrôle sur nos workflows.

### Comment mettre à jour la GitHub CLI

Pour vous assurer que vous utilisez la dernière version de la GitHub CLI avec toutes les dernières fonctionnalités et corrections, vous pouvez la mettre à jour en utilisant winget.

```plaintext
winget upgrade --id GitHub.cli
```

* **winget upgrade :** Vérifie les mises à jour pour le paquet spécifié.
    
* **--id GitHub.cli :** Identifie le paquet GitHub CLI pour la mise à jour.
    

## Fonctionnalités avancées et intégrations de la GitHub CLI

La GitHub CLI n'est pas seulement utile pour effectuer des tâches de base. Vous pouvez également effectuer des opérations avancées avec son aide.

### Comment gérer les Gists avec la GitHub CLI

Les Gists sont un moyen simple de partager des extraits de code. Vous pouvez créer, lister et gérer vos Gists directement depuis la CLI. Voici comment vous pouvez créer un gist :

```plaintext
gh gist create my-code-snippet.py
```

Pour lister vos gists :

```plaintext
gh gist list
```

### Interaction avec les Releases et les Tags

Pour gérer les releases et les tags, la GitHub CLI fournit des commandes pour créer, lister et supprimer des releases. Voici un exemple de création d'une release :

```plaintext
gh release create v1.0.0
```

### Comment étendre la GitHub CLI avec des scripts personnalisés et des alias

Vous pouvez écrire vos propres scripts et les intégrer à la GitHub CLI, ou créer des alias pour les commandes que vous utilisez fréquemment afin de gagner du temps. Les alias vous permettent de créer des raccourcis pour les commandes que vous utilisez souvent. Par exemple, la commande ci-dessous crée un alias `prlist` qui affichera toutes les pull requests, quel que soit leur état :

```plaintext
gh alias set prlist "pr list --state all"
```

De la même manière, vous pouvez créer un raccourci `co` pour extraire rapidement la branche d'une pull request sans taper la commande complète à chaque fois. La commande est donnée ci-dessous :

```plaintext
gh alias set co "pr checkout"
```

### Dépannage des problèmes courants

Si vous rencontrez des problèmes, vous pouvez les dépanner en vérifiant la syntaxe de la commande, en vous assurant que votre GitHub CLI est à jour, ou en consultant la documentation à l'aide de la commande :

```plaintext
gh help <command>
```

## **Conclusion**

La GitHub CLI est un excellent outil qui aide les développeurs à travailler directement depuis le terminal. Elle vous permet de gérer les dépôts, de traiter les pull requests et les tickets, de déclencher et de surveiller GitHub Actions, et même de travailler avec des Gists.

En tant que développeurs, vous pouvez gagner du temps et améliorer votre productivité en utilisant cet outil puissant. Continuez à explorer ses nouvelles fonctionnalités et restez à jour avec la dernière version.