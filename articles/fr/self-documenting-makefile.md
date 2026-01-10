---
title: Comment créer un Makefile auto-documenté
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-08-10T13:59:08.000Z'
originalURL: https://freecodecamp.org/news/self-documenting-makefile
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/cover-1.png
tags:
- name: Devops
  slug: devops
- name: Productivity
  slug: productivity
- name: workflow
  slug: workflow
seo_title: Comment créer un Makefile auto-documenté
seo_desc: 'My new favorite way to completely underuse a Makefile? Creating personalized,
  per-project repository workflow command aliases that you can check in.

  Can a Makefile improve your DevOps and keep developers happy? How awesome would
  it be if a new develo...'
---

Ma nouvelle façon préférée de sous-utiliser complètement un Makefile ? Créer des alias de commandes de workflow de dépôt personnalisés et spécifiques à chaque projet que vous pouvez vérifier.

Un Makefile peut-il améliorer votre DevOps et garder les développeurs heureux ? Ce serait génial si un nouveau développeur travaillant sur votre projet ne commençait pas par copier et coller des commandes depuis votre README. Et s'au lieu de :

```shell
pip3 install pipenv
pipenv shell --python 3.8
pipenv install --dev
npm install
pre-commit install --install-hooks
# chercher comment installer le Framework X...
# copier et coller depuis le README...
npm run serve
```

… vous pouviez simplement taper :

`make start`

… et ensuite commencer à travailler ?

## Faire la différence

J'utilise `make` tous les jours pour éliminer la monotonie des activités de développement courantes comme la mise à jour des programmes, l'installation des dépendances et les tests.

Pour faire tout cela avec un Makefile (GNU make), nous utilisons [les règles Makefile](https://www.gnu.org/software/make/manual/make.html#Rules) et [les recettes](https://www.gnu.org/software/make/manual/make.html#Recipes). Des parallèles similaires existent pour la version POSIX de make, comme [les règles de cible](https://pubs.opengroup.org/onlinepubs/9699919799/utilities/make.html#tag_20_76_13_04). Voici [un excellent article](https://nullprogram.com/blog/2017/08/20/) sur les Makefiles compatibles POSIX.

Voici quelques exemples de choses que nous pouvons rendre plus faciles avec `make` (désolé) :

```makefile
update: ## Faire une mise à jour et un autoremove avec apt
    sudo apt update && sudo apt upgrade -y
    sudo apt autoremove -y

env:
    pip3 install pipenv
    pipenv shell --python 3.8

install: ## Installer ou mettre à jour les dépendances
    pipenv install --dev
    npm install
    pre-commit install --install-hooks

serve: ## Lancer le serveur de développement local
    hugo serve --enableGitInfo --disableFastRender --environment development

initial: update env install serve ## Installer les outils et démarrer le serveur de développement

```

Maintenant, nous avons des alias en ligne de commande que vous pouvez vérifier. Bonne idée ! Si vous vous demandez ce qui se passe avec cette syntaxe de commentaire étrange `##`, cela devient encore mieux.

## Un Makefile auto-documenté

Les alias sont géniaux, si vous vous souvenez de ce qu'ils sont et de ce qu'ils font sans avoir à taper constamment `cat Makefile`. Naturellement, vous avez besoin d'une commande `help` :

```makefile
.PHONY: help
help: ## Afficher cette aide
    @egrep -h '\s##\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

```

Avec un peu de magie en ligne de commande, cette commande `egrep` prend la sortie de `MAKEFILE_LIST`, la trie et utilise `awk` pour trouver les chaînes qui suivent le motif `##`. Elle imprime ensuite une version formatée et utile des commentaires.

Nous allons le placer en haut du fichier pour qu'il soit la cible par défaut. Maintenant, pour voir tous nos raccourcis pratiques et ce qu'ils font, nous exécutons simplement `make`, ou `make help` :

```text
help                 Afficher cette aide
initial              Installer les outils et démarrer le serveur de développement
install              Installer ou mettre à jour les dépendances
serve                Lancer le serveur de développement local
update               Faire une mise à jour et un autoremove avec apt

```

Maintenant, nous avons notre propre outil CLI personnalisé et spécifique au projet !

Les possibilités d'améliorer votre flux DevOps avec un Makefile auto-documenté sont presque infinies. Vous pouvez l'utiliser pour simplifier n'importe quel workflow et produire des développeurs très heureux.