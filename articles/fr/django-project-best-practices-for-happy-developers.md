---
title: Meilleures pratiques pour les projets Django qui rendront vos développeurs
  heureux
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2020-09-24T16:24:57.000Z'
originalURL: https://freecodecamp.org/news/django-project-best-practices-for-happy-developers
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/cover-4.png
tags:
- name: best practices
  slug: best-practices
- name: Django
  slug: django
- name: Productivity
  slug: productivity
seo_title: Meilleures pratiques pour les projets Django qui rendront vos développeurs
  heureux
seo_desc: 'Do you want your team to enjoy your development workflow? Do you think
  building software should be fun and existentially fulfilling? If so, this is the
  post for you.

  I’ve been developing with Django for years, and I’ve never been happier with my
  Djan...'
---

Voulez-vous que votre équipe _apprécie_ votre flux de développement ? Pensez-vous que la création de logiciels devrait être _amusante et existentiellement épanouissante_ ? Si oui, cet article est fait pour vous.

Je développe avec Django depuis des années, et je n'ai jamais été aussi satisfait de la configuration de mon projet Django qu'aujourd'hui.

Dans cet article, je vais expliquer comment je fais en sorte qu'une journée de développement avec Django soit l'expérience de développement la plus relaxante et agréable possible pour moi et mon équipe d'ingénieurs.

## Un outil CLI personnalisé pour votre projet Django

Au lieu de taper :

```sh
python3 -m venv env
source env/bin/activate
pip install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py runserver

```

Ne serait-il pas beaucoup plus agréable de taper :

```sh
make start

```

026et que tout cela se fasse pour vous ? Je le pense !

Nous pouvons faire cela avec un Makefile auto-documenté. En voici un que j'utilise fréquemment lors du développement de mes applications Django, comme [ApplyByAPI.com](https://applybyapi.com/) :

```makefile
SHELL := /bin/bash

include .env

.PHONY: help
help: ## Afficher cette aide
    @egrep -h '\s##\s' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

.PHONY: venv
venv: ## Créer un nouvel environnement virtuel
    python3 -m venv $(VENV) && source $(BIN)/activate

.PHONY: install
install: venv ## Créer venv et installer les dépendances
    $(BIN)/pip install -r requirements.txt

migrate: ## Créer et exécuter les migrations
    $(PYTHON) manage.py makemigrations
    $(PYTHON) manage.py migrate

db-up: ## Télécharger et démarrer le conteneur Docker Postgres en arrière-plan
    docker pull postgres
    docker-compose up -d

db-shell: ## Accéder à la base de données Docker Postgres de manière interactive avec psql
    docker exec -it container_name psql -d $(DBNAME)

.PHONY: test
test: ## Exécuter les tests
    $(PYTHON) $(APP_DIR)/manage.py test application --verbosity=0 --parallel --failfast

.PHONY: run
run: ## Démarrer le serveur Django
    $(PYTHON) $(APP_DIR)/manage.py runserver

start: install migrate run ## Installer les dépendances, appliquer les migrations, puis démarrer le serveur de développement

```

Vous remarquerez la présence de la ligne `include .env` ci-dessus. Cela garantit que `make` a accès aux variables d'environnement stockées dans un fichier appelé `.env`.

Cela permet à Make d'utiliser ces variables dans ses commandes, par exemple, le nom de mon environnement virtuel, ou pour passer `$(DBNAME)` à `psql`.

Qu'en est-il de cette syntaxe de commentaire étrange "`##`" ? Un Makefile comme celui-ci vous offre une suite pratique d'alias de commande que vous pouvez consulter dans votre projet Django. C'est très utile à condition de pouvoir vous souvenir de tous ces alias.

La commande `help` ci-dessus, qui s'exécute par défaut, imprime une liste utile des commandes disponibles lorsque vous exécutez `make` ou `make help` :

```text
aide                 Afficher cette aide
venv                 Créer un nouvel environnement virtuel
install              Créer venv et installer les dépendances
migrate              Créer et exécuter les migrations
db-up                Télécharger et démarrer le conteneur Docker Postgres en arrière-plan
db-shell             Accéder à la base de données Docker Postgres de manière interactive avec psql
test                 Exécuter les tests
run                  Démarrer le serveur Django
start                Installer les dépendances, appliquer les migrations, puis démarrer le serveur de développement

```

Toutes les commandes Django habituelles sont couvertes, et nous avons une commande `test` qui exécute nos tests avec les options que nous préférons. Brillant.

Vous pouvez lire mon article complet sur les [Makefiles auto-documentés ici](https://victoria.dev/blog/how-to-create-a-self-documenting-makefile/), qui inclut également un exemple de Makefile utilisant `pipenv`.

## Économisez votre puissance cérébrale avec des hooks pre-commit

J'ai précédemment écrit sur certaines [ergonomies techniques](https://victoria.dev/blog/technical-ergonomics-for-the-efficient-developer/) qui peuvent faciliter grandement le développement de logiciels de qualité par les équipes.

Un domaine qui est une évidence est l'utilisation de hooks pre-commit pour lint le code avant de le valider.

Cela aide à maintenir la qualité du code que vos développeurs valident. Mais surtout, cela garantit que personne dans votre équipe ne passe de temps à essayer de se souvenir s'il faut utiliser des guillemets simples ou doubles ou où placer un saut de ligne.

Le framework [pre-commit](https://pre-commit.com/), dont le nom est déroutant, est par ailleurs une excellente façon de garder les hooks (qui ne sont pas inclus dans les dépôts clonés) cohérents entre les environnements locaux.

Voici mon fichier de configuration, `.pre-commit-config.yaml`, pour mes projets Django :

```yaml
fail_fast: true
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v3.1.0
    hooks:
      - id: detect-aws-credentials
  - repo: https://github.com/psf/black
    rev: 19.3b0
    hooks:
      - id: black
  - repo: https://github.com/asottile/blacken-docs
    rev: v1.7.0
    hooks:
      - id: blacken-docs
        additional_dependencies: [black==19.3b0]
  - repo: local
    hooks:
      - id: markdownlint
        name: markdownlint
        description: "Lint les fichiers Markdown"
        entry: markdownlint '**/*.md' --fix --ignore node_modules --config "./.markdownlint.json"
        language: node
        types: [markdown]

```

Ces hooks vérifient les commits accidentels de secrets, formatent les fichiers Python en utilisant [Black](https://github.com/psf/black), formatent les extraits de code Python dans les fichiers Markdown en utilisant [`blacken-docs`](https://github.com/asottile/blacken-docs), et [lint les fichiers Markdown](https://github.com/igorshubovych/markdownlint-cli) également.

Il existe probablement encore plus de hooks utiles disponibles pour votre cas d'utilisation particulier : consultez les [hooks pris en charge](https://pre-commit.com/hooks.html) pour explorer.

## Gitignores utiles

Une méthode sous-estimée pour améliorer l'expérience quotidienne de développement de votre équipe est de vous assurer que votre projet utilise un fichier `.gitignore` bien équilibré.

Cela peut aider à empêcher les fichiers contenant des secrets d'être validés, et peut également faire économiser des heures de travail fastidieux aux développeurs en garantissant que vous ne parcourez jamais un `git diff` de fichiers générés.

Pour créer efficacement un [gitignore pour les projets Python et Django](https://www.toptal.com/developers/gitignore/api/python,django), [gitignore.io](https://gitignore.io/) de Toptal peut être une ressource utile pour générer un fichier `.gitignore` robuste.

Je recommande toujours d'examiner les résultats générés vous-même pour vous assurer que les fichiers ignorés conviennent à votre cas d'utilisation, et que rien de ce que vous souhaitez ignorer n'est commenté.

## Tests continus avec GitHub Actions

Si votre équipe travaille sur GitHub, la mise en place d'un processus de test avec Actions est un fruit à portée de main.

Les tests qui s'exécutent dans un environnement cohérent à chaque pull request peuvent aider à éliminer les énigmes "ça marche sur ma machine". Ils peuvent également aider à garantir que personne ne reste assis à attendre qu'un test s'exécute localement.

Un environnement CI hébergé comme GitHub Actions peut également aider lors de l'exécution de tests d'intégration qui nécessitent l'utilisation de ressources de services gérés.

Vous pouvez utiliser des [secrets chiffrés dans un dépôt](https://docs.github.com/en/actions/configuring-and-managing-workflows/creating-and-storing-encrypted-secrets) pour accorder à l'exécuteur Actions l'accès aux ressources dans un environnement de test, sans vous soucier de la création de ressources de test et de clés d'accès pour chacun de vos développeurs.

J'ai écrit à plusieurs reprises sur la mise en place de flux de travail Actions, y compris [l'utilisation d'un pour exécuter votre Makefile](https://victoria.dev/blog/a-lightweight-tool-agnostic-ci/cd-flow-with-github-actions/), et [comment intégrer les données d'événement GitHub](https://victoria.dev/blog/publishing-github-event-data-with-github-actions-and-pages/). GitHub m'a même [interviewé sur Actions](https://github.blog/2020-06-26-github-action-hero-victoria-drake/) une fois.

Pour les projets Django, voici un flux de travail GitHub Actions simple qui exécute des tests avec une version cohérente de Python.

```yaml
name: Exécuter les tests Django

on: push

jobs:
  test:

    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v2
      - name: Configurer Python
        uses: actions/setup-python@v2
        with:
          python-version: '3.8'
      - name: Installer les dépendances
        run: make install
      - name: Exécuter les tests
        run: make test

```

Pour les commandes d'installation et de test, j'ai simplement utilisé le [Makefile](https://victoria.dev/blog/my-django-project-best-practices-for-happy-developers/#heading-installation) qui a été validé dans le dépôt.

Un avantage d'utiliser vos commandes Makefile dans vos flux de travail de test CI est que vous n'avez besoin de les mettre à jour qu'à un seul endroit - votre Makefile ! Plus de maux de tête "pourquoi cela fonctionne-t-il localement mais pas en CI ??!?".

Si vous voulez améliorer votre jeu de sécurité, vous pouvez ajouter [Django Security Check](https://github.com/victoriadrake/django-security-check) comme une Action également.

## Configurez votre projet Django pour le succès

Vous voulez aider à garder votre équipe de développement heureuse ? Préparez-les au succès avec ces meilleures pratiques pour le développement Django.

Rappelez-vous, une once de puissance cérébrale vaut une livre de logiciel.