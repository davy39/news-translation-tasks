---
title: Comment utiliser GitHub Actions pour automatiser des projets open source
subtitle: ''
author: Hillary Nyakundi
co_authors: []
series: null
date: '2023-03-28T15:51:39.000Z'
originalURL: https://freecodecamp.org/news/automate-open-source-projects-with-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/OOP--4-.png
tags:
- name: automation
  slug: automation
- name: GitHub Actions
  slug: github-actions
- name: open source
  slug: open-source
seo_title: Comment utiliser GitHub Actions pour automatiser des projets open source
seo_desc: "These days, developers use automation tools all the time to manage tasks\
  \ effectively and streamline their daily activities. And one of these popular tools\
  \ is GitHub Actions. \nWhen talking about software, including the open-source variety,\
  \ you'll like..."
---

De nos jours, les développeurs utilisent sans cesse des outils d'automatisation pour gérer leurs tâches efficacement et optimiser leurs activités quotidiennes. L'un de ces outils populaires est GitHub Actions.

Lorsqu'on parle de logiciels, y compris de la variété open source, vous conviendrez probablement avec moi que l'efficacité est très demandée. Grâce à de tels outils d'automatisation, les mainteneurs peuvent automatiser les tâches répétitives et se concentrer sur des tâches plus importantes telles que l'écriture de code de qualité, la révision des contributions et la création d'une communauté active autour du projet.

J'ai dû effectuer manuellement certaines tâches qui auraient pu être automatisées, je me sens donc bien placé pour partager comment l'utilisation de GitHub Actions peut faire gagner du temps.

Je passe la majeure partie de mes matinées à examiner l'un de mes [mini-python-projects](https://github.com/larymak/Python-project-Scripts) qui a attiré des contributeurs. J'écris des messages chaleureux et accueillants aux nouveaux contributeurs, je vérifie les PR (Pull Requests) récemment créées pour m'assurer qu'elles respectent les règles du projet, comme l'inclusion de fichiers README avec des instructions, des captures d'écran si nécessaire, et ainsi de suite.

Mais ce que je ne savais pas, c'est que je pouvais automatiser certaines de ces tâches et bien plus encore pour réduire ma charge de travail. Et je pouvais le faire à l'aide de GitHub Actions.

Dans ce guide, je vais en partager davantage sur GitHub Actions et la manière dont je l'utilise. Je vous montrerai comment vous pouvez en tirer parti pour automatiser divers aspects de vos projets, de l'accueil des nouveaux contributeurs à l'attribution des tâches, en passant par la vérification de la qualité du code, et bien plus encore. Rendons votre projet plus efficace et interactif ensemble.

## Qu'est-ce que GitHub Actions ?
GitHub Actions est un outil qui vous permet d'effectuer différentes automatisations au sein d'un dépôt GitHub. Il vous permet de créer des flux de travail (workflows) personnalisés que vous pouvez utiliser pour automatiser votre processus de développement, tel que la construction (build), les tests et le déploiement du code.

Après avoir intégré cet outil aux autres fonctionnalités de GitHub, vous pouvez transformer votre routine de gestion de projet et la rendre plus agréable et engageante pour tous ceux qui y contribuent.

### Comment configurer GitHub Actions dans votre dépôt
Tout commence dans le dossier racine. Par défaut, GitHub Actions est généralement intégré à votre dépôt GitHub, vous n'aurez donc pas besoin de vous inscrire pour un compte séparé ou de l'installer. Mais vous devrez suivre quelques étapes afin d'accéder à ses fonctionnalités.

* Dans votre dépôt GitHub, sur l'onglet de navigation supérieur, vous verrez l'onglet **Actions**. Cliquez dessus, et il vous donnera accès à une liste de flux de travail recommandés ainsi qu'à une option pour créer le vôtre.

![onglet-actions](https://www.freecodecamp.org/news/content/images/2023/03/actions-tab.png)

* Maintenant, selon la nature de votre projet, vous pouvez soit choisir un flux de travail déjà créé dans les listes disponibles, soit choisir d'en créer un vous-même. Puisque vous comprenez en quoi consiste votre projet et ce que vous pourriez avoir besoin d'automatiser, je vous recommande de configurer vous-même un nouveau flux de travail. Cela vous donnera une meilleure compréhension de ce qui se passe.

* Pour configurer un nouveau flux de travail, cliquez sur **Set up a workflow yourself**. Cela vous mènera à un écran de création de flux de travail avec un nouveau fichier YAML nommé `main.yml`. À ce stade, je devrais mentionner qu'avoir une compréhension de YAML est vraiment important puisque vous avez choisi d'écrire vos propres flux de travail.

Ce qui se passe en coulisses, c'est qu'une fois que vous avez cliqué sur cette option, deux dossiers sont créés aux côtés du fichier `main.yml`. Si vous accédez à votre dépôt par la suite ou si vous regardez le chemin juste avant le nom de votre fichier, vous verrez : `.github/workflows/<nom_du_fichier>`.

* C'est à l'intérieur du fichier `main.yml` que vous définissez votre flux de travail, et après avoir tout écrit, vous effectuez un Commit des modifications tout comme vous le feriez lors de modifications sur un dépôt. Avec cela, votre flux de travail est prêt et il s'exécutera en fonction des déclencheurs définis dans le fichier YAML.

Alternativement, vous pouvez toujours accomplir tout cela depuis votre éditeur de code préféré. Tout ce que vous avez à faire est de cloner le dépôt sur votre ordinateur, de créer un dossier `.github` à la racine de votre projet, de créer un autre dossier à l'intérieur nommé `workflows`, et enfin d'ajouter un fichier avec une extension `.yml` et d'y écrire votre script.

Dans les exemples ci-dessous, je ferai référence au code que j'ai implémenté dans mi-projet pour vous aider à comprendre.

## Composants de GitHub Actions

GitHub Actions se compose principalement de trois composants majeurs, qui incluent :

* Flux de travail (Workflows) - Ce sont des ensembles de règles qui définissent le processus d'automatisation. Ils sont définis dans le fichier YAML qui est stocké dans le répertoire `.github/workflows`.
 
* Événements (Events) - Ce sont eux qui initient un flux de travail. Par exemple, vous pouvez avoir un événement configuré pour exécuter un flux de travail lorsqu'une PR est créée, ou lorsqu'un ticket (issue) est ouvert. Pour définir un événement dans un flux de travail, utilisez le mot-clé `on` suivi des noms d'événements.

Par exemple :
```yaml
on:
    issues:
        types: [opened]
    pull_request_target:
        types: [opened]
```

* Jobs - Ce sont les éléments qui constituent un flux de travail. Les jobs sont exécutés simultanément par défaut. Pour définir vos jobs dans un flux de travail donné, utilisez le mot-clé `jobs` suivi d'un identifiant unique pour chaque job et de sa configuration.

Par exemple :

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - name: Check out repository
        uses: actions/checkout@v2
      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.10
      - name: Install dependencies
        run: |
          pip install -r requirements.txt
```

Tous ces composants travaillent ensemble pour garantir qu'un ensemble de règles donné est exécuté avec succès. Commençons maintenant à travailler sur notre projet.

## Comment automatiser la gestion des tickets et des Pull Requests
La gestion des tickets (issues) et des pull requests peut être une tâche très chronophage, surtout pour les grands projets open source. Mais avec GitHub Actions, les mainteneurs sont en mesure d'automatiser ces processus et de passer plus de temps à coder et à s'engager avec la communauté.

### Comment créer des modèles de tickets et de pull requests
Si vous êtes un contributeur open source actif, il y a de fortes chances que vous soyez tombé sur un guide qui vous indique quoi inclure soit dans votre ticket, soit dans votre soumission de PR. L'objectif principal de tels modèles est de fournir des conseils et de s'assurer que les contributeurs fournissent toutes les informations nécessaires.

Voyons maintenant comment vous pouvez implémenter ce modèle sur vos projets :

* La première étape consiste à s'assurer qu'il existe un répertoire `.github` à la racine du dépôt si vous ne l'avez pas déjà.
* Dans le dossier `.github`, créez deux autres dossiers `ISSUE_TEMPLATE` et `PULL_REQUEST_TEMPLATE`.
* Dans ces deux dossiers, ajoutez des fichiers markdown représentant le contenu que vous souhaitez automatiser : Par exemple, vous pouvez avoir `feature_request.md` et `issue_report.md` pour le modèle de ticket et `pull_request_template.md` pour le modèle de PR.

Voici ci-dessous une référence de ce que j'ai dans mon fichier `pull_request_template.md`. C'est un guide simple qui indique aux contributeurs quoi inclure avant de soumettre leur pull request.

```markdown
**Ticket(s) associé(s) :**
Veuillez fournir un titre pour cette pull request.

**Description :**
Veuillez fournir une brève description des modifications que vous proposez.

**Liste de contrôle :**

-   [ ] J'ai lu et suivi les [consignes de contribution](/CONTRIBUTING.md).
-   [ ] J'ai inclus un fichier README pour mon projet.
-   [ ] J'ai mis à jour le fichier README principal si nécessaire.
-   [ ] J'ai inclus un fichier requirements.txt.
-   [ ] J'ai ajouté des tests qui prouvent que mes modifications sont efficaces ou que ma fonctionnalité fonctionne.
-   [ ] Tous les tests nouveaux et existants réussissent.

**Captures d'écran**
Le cas échéant, ajoutez des captures d'écran pour aider à expliquer le comportement de votre code.

**Notes supplémentaires :**
Veuillez fournir toute information supplémentaire sur les modifications que vous proposez.
```

Pour une explication plus détaillée, consultez la documentation de GitHub Actions sur les modèles de tickets et de pull requests [ici](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/about-issue-and-pull-request-templates).

### Accueillir les nouveaux contributeurs et reconnaître les efforts de la communauté

Être un mainteneur et s'engager avec votre communauté est important, car vous avez l'opportunité d'interagir directement avec vos pairs et d'obtenir leurs retours. Mais si vous gérez un projet important qui attire de nombreux contributeurs, vous n'aurez peut-être pas souvent l'occasion de vous engager directement avec la communauté.

À l'aide de GitHub Actions, vous pouvez accomplir certaines de ces tâches comme accueillir les nouveaux contributeurs, reconnaître leurs efforts et créer une atmosphère positive pour les membres existants de la communauté.

Si vous gérez un petit projet, vous pouvez probablement interagir directement avec votre communauté tout en utilisant l'automatisation pour vous aider.

Par exemple, voici un échantillon de code que j'ai implémenté pour accueillir les nouveaux contributeurs lorsqu'ils ouvrent une pull request ou créent un nouveau ticket sur le dépôt. Vous pouvez y voir que j'ai un message les remerciant pour leur effort et les assurant également que leurs modifications seront examinées dès que possible. Malgré cela, je poursuis la conversation si quelque chose de supplémentaire est requis ou pour suggérer de nouvelles idées.

```yaml
name: Welcome New Contributors

on:
    issues:
        types: [opened]
    pull_request_target:
        types: [opened]

jobs:
    welcome:
        runs-on: ubuntu-latest
        steps:
            - name: Welcome Issue
              if: github.event_name == 'issues'
              uses: actions/github-script@v5
              with:
                  script: |
                      const issue = context.issue;
                      const repo = context.repo;
                      const issueAuthor = context.payload.sender.login;
                      const welcomeMessage = `
                        Salut @${issueAuthor} ! :wave:
                        Merci d'avoir créé un ticket dans notre dépôt ! Nous apprécions votre contribution et nous reviendrons vers vous dès que possible.
                      `;
                      github.rest.issues.createComment({
                        ...repo,
                        issue_number: issue.number,
                        body: welcomeMessage
                      });
            - name: Welcome Pull Request
              if: github.event_name == 'pull_request_target'
              uses: actions/github-script@v5
              with:
                  script: |
                      const pr = context.issue;
                      const repo = context.repo;
                      const prAuthor = context.payload.sender.login;
                      const welcomeMessage = `
                        Salut @${prAuthor} ! :wave:
                        Merci d'avoir soumis une pull request ! Nous apprécions votre contribution et nous examinerons vos modifications dès que possible.
                      `;
                      github.rest.issues.createComment({
                        ...repo,
                        issue_number: pr.number,
                        body: welcomeMessage
                      });
```

En plus de ce flux de travail simple, si vous dirigez un projet plus complexe, vous pourriez envisager d'écrire un flux de travail plus détaillé capable d'attribuer automatiquement des badges, des étiquettes (labels) ou des titres personnalisés aux contributeurs.

De même, vous pouvez choisir d'ajouter un flux de travail qui remercie les contributeurs lorsque leur pull request est fusionnée ou que leur ticket est fermé. Vous pouvez consulter la [documentation de GitHub Actions](https://docs.github.com/en/actions/managing-issues-and-pull-requests/using-github-actions-for-project-management) pour un guide détaillé.

## Comment automatiser l'assurance qualité du code
Pour la plupart des développeurs, écrire un code de qualité est très important, surtout s'ils travaillent sur des applications destinées aux consommateurs. Bien que le succès d'un projet dépende d'un code bien écrit et testé, l'examen des modifications peut parfois prendre du temps et même retarder des fonctionnalités très demandées.

Grâce aux outils d'automatisation du code, vous pouvez maintenir un style de codage cohérent et identifier rapidement et facilement les bogues potentiels, gardant ainsi votre projet propre.

Alors, comment configurer l'intégration continue (CI) avec GitHub Actions, intégrer des outils de formatage et de peluchage (linting) de code, et utiliser des services de revue de code automatisée dans votre projet ?

L'intégration continue (CI) vous aide à automatiser des processus tels que la construction, les tests et la validation des modifications de code. Tout comme n'importe quel autre code d'automatisation, le code CI est écrit dans un fichier `.yml` stocké dans les dossiers `.github/workflows`.

Voici ci-dessous un exemple de flux de travail CI pour un projet Python qui s'exécute lorsqu'un push ou une pull request est effectué sur la branche `main` d'un dépôt. Il teste le code Python avec plusieurs versions, installe les dépendances nécessaires et exécute les tests à l'aide du module `unittest`.

```yaml
name: Python CI

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        python-version: [3.7, 3.8, 3.9, 3.10]

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    - name: Run tests
      run: |
        python -m unittest discover
```

En plus du code ci-dessus, si vous souhaitez de l'aide pour maintenir la cohérence de votre style de codage, vous pouvez intégrer des outils de formatage et de peluchage de code tels que `black`, `isort` ou `flake8`. Pour cela, il vous suffit de les ajouter dans votre fichier `requirements.txt` qui est déjà inclus dans le code ci-dessus et d'inclure le bloc ci-dessous pour exécuter les outils.

```yaml
#...
    # ...
    - name: Run black for code formatting
      run: |
        black --check .
    - name: Run isort for import sorting
      run: |
        isort --check --diff .
    - name: Run flake8 for linting
      run: |
        flake8 .
```

S'il trouve des problèmes de formatage de code, la construction CI échouera. Pour le corriger, vous devrez vérifier manuellement les journaux (logs). Consultez ce guide sur [la construction et le test de Python](https://docs.github.com/en/actions/automating-builds-and-tests/building-and-testing-python) pour plus d'exemples.

Les idées ci-dessus ne sont que quelques-unes des automatisations que vous pouvez utiliser dans vos projets. Pour une application plus complexe, vous pourriez envisager d'ajouter également des flux de travail pour générer de la documentation avec des outils comme Sphinx ou MkDocs, automatiser les mises à jour de dépendances, automatiser la gestion des versions et le suivi de projet, et bien plus encore.

## Conseils pour créer des GitHub Actions personnalisées
Il existe de nombreuses actions pré-construites déjà disponibles sur la [place de marché GitHub Actions](https://github.com/marketplace?type=actions). Mais parfois, vous pouvez vouloir ou avoir besoin de personnaliser vos flux de travail pour qu'ils correspondent à vos besoins.

Pour cela, vous pouvez choisir soit JavaScript, soit des conteneurs Docker et les partager avec la communauté.

Voici quelques bonnes pratiques à suivre :

* Comprendre le problème – comme pour tout autre projet, avant de commencer la construction, assurez-vous de comprendre le problème que vous essayez de résoudre et comment vous allez le résoudre.
* Choisir la bonne pile (stack) – comme discuté ci-dessus, les GitHub Actions peuvent être écrites en utilisant JavaScript ou Docker. Assurez-vous de choisir ce qui correspond le mieux à vos besoins et à votre compréhension.
* Assurez-vous de respecter les meilleures pratiques de codage afin que d'autres puissent facilement comprendre et lire votre code.
* Utilisez les paquets déjà disponibles tels que `@actions/core` et `@actions/github` qui permettent une interaction facile avec l'environnement GitHub Actions et l'API GitHub.
* Il y a de fortes chances qu'après avoir créé avec succès votre propre flux de travail, vous souhaitiez le publier. Que vous le publiiez ou non, assurez-vous de tester votre action pour détecter d'éventuels problèmes ou bogues.

Grâce à ces conseils simples, vous pouvez créer une GitHub Action personnalisée qui automatise certaines tâches majeures/basiques de votre projet. En plus des conseils ci-dessus, plus de détails sur la création d'actions personnalisées peuvent être trouvés sur la [documentation officielle](https://docs.github.com/en/actions/creating-actions).

## Conclusion
Dans ce guide, nous avons vu les avantages potentiels que GitHub Actions peut apporter à nos projets. Non seulement cela simplifie le processus de production, mais cela nous permet également de personnaliser les actions pour qu'elles correspondent aux besoins de notre projet.

Ce n'est que la partie visible de ce que nous pouvons accomplir. Je vous encourage à acquérir une meilleure compréhension et à explorer différentes manières de mettre en œuvre davantage GitHub Actions pour améliorer votre projet open source. Adoptons l'automatisation et utilisons-la pour en faire plus.