---
title: Comment configurer un pipeline CI/CD avec Husky et GitHub Actions
subtitle: ''
author: Viviana Yanez
co_authors: []
series: null
date: '2024-07-15T17:46:34.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-a-ci-cd-pipeline-with-husky-and-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/how-to-set-a-cicd-pipeline-1.jpg
tags:
- name: continuous delivery
  slug: continuous-delivery
- name: Continuous Integration
  slug: continuous-integration
- name: GitHub Actions
  slug: github-actions
seo_title: Comment configurer un pipeline CI/CD avec Husky et GitHub Actions
seo_desc: 'CI/CD is a core practice in the modern software development ecosystem.
  It helps agile teams deliver high-quality software in short release cycles.

  In this tutorial, you''ll learn what CI/CD is, and I''ll help you set up a CI/CD
  pipeline using Husky and...'
---

CI/CD est une pratique essentielle dans l'écosystème moderne de développement logiciel. Elle aide les équipes agiles à livrer des logiciels de haute qualité dans des cycles de publication courts.

Dans ce tutoriel, vous apprendrez ce qu'est le CI/CD, et je vous aiderai à configurer un pipeline CI/CD en utilisant Husky et GitHub Actions dans une application Next.js.

Ce tutoriel suppose que vous avez déjà des connaissances en React et Next.js ou d'autres frameworks JavaScript modernes. Vous aurez également besoin d'un compte GitHub, et des connaissances de base en Git seront fortement bénéfiques.

Si vous avez déjà une application web fonctionnelle qui n'est pas construite avec Next.js, vous pourriez toujours trouver cet article utile. Tous les concepts et la plupart des configurations fonctionneront avec peu d'adaptation dans les applications créées avec d'autres frameworks.

## Voici ce que nous allons couvrir :

1. [Qu'est-ce que le CI/CD ?](#heading-quest-ce-que-le-cicd)
   - [Qu'est-ce que le CI ?](#heading-quest-ce-que-le-ci)
   - [Qu'est-ce que le CD ?](#heading-quest-ce-que-le-cd)
   - [Qu'est-ce qu'un pipeline CI/CD et quels sont ses avantages ?](#heading-quest-ce-quun-pipeline-cicd-et-quels-sont-ses-avantages)
2. [Comment configurer un pipeline CI/CD](#heading-comment-configurer-un-pipeline-cicd)
   - [Étape 1 : Configurer une application Next.js avec Vitest](#heading-etape-1-configurer-une-application-nextjs)
   - [Étape 2 : Configurer un Git Hook](#heading-etape-2-configurer-un-git-hook)
   - [Étape 3 : Créer un workflow GitHub Actions](#heading-etape-3-creer-un-workflow-github-actions)
   - [Étape 4 : Déployer le projet](#heading-etape-4-deployer-le-projet)
3. [Conclusion](#heading-conclusion)

## Qu'est-ce que le CI/CD ?

L'intégration continue/livraison continue ou déploiement continu (CI/CD) est une pratique qui implique l'automatisation du processus de construction, de test et de déploiement de logiciels.

Son principal avantage est d'accélérer l'ensemble du processus de développement. Il augmente également la productivité en garantissant une intégration fluide du code, l'adoption de normes et de meilleures pratiques de sécurité. Il aide également à produire un cycle de feedback plus court avec une détection précoce des problèmes, parmi d'autres avantages expliqués ci-dessous.

Le CI/CD est un outil essentiel dans les pratiques de développement logiciel d'aujourd'hui, permettant aux équipes de livrer des logiciels de haute qualité rapidement, efficacement et de manière fiable.

Apprenons-en plus en détail.

### Qu'est-ce que le CI ?

L'**intégration continue** est une pratique logicielle qui signifie que les développeurs d'une équipe fusionnent les changements de code dans un dépôt central plusieurs fois par jour.

Au lieu d'avoir des environnements de développement indépendants et de fusionner à un moment spécifique, les développeurs intègrent fréquemment leurs changements à une application dans une branche partagée ou un "tronc".

### Qu'est-ce que le CD ?

Le CD dans CI/CD fait généralement référence à la **livraison continue**. C'est une pratique qui, en plus du CI, automatise le processus d'intégration, de test et de publication du logiciel. L'automatisation s'arrête juste avant le déploiement en production, où une étape contrôlée par l'homme est nécessaire.

Mais CD peut également faire référence au **déploiement continu**, qui ajoute l'automatisation à l'étape de publication du logiciel dans un environnement de production.

Bien que CD fasse généralement référence à la livraison continue, les deux termes sont parfois utilisés de manière interchangeable. La différence entre eux est le niveau d'automatisation mis en œuvre dans un projet.

### Qu'est-ce qu'un pipeline CI/CD et quels sont ses avantages ?

Lorsque ces deux pratiques sont combinées, elles créent un pipeline CI/CD. L'ajout de CI/CD à votre projet apporte les avantages suivants :

* Développement plus rapide : réduit le temps nécessaire pour livrer de nouvelles fonctionnalités grâce à l'automatisation de la construction, des tests et du déploiement.
* Collaboration améliorée : encourage les intégrations fréquentes de code et réduit les conflits d'intégration.
* Qualité de code améliorée : impose l'adoption de normes de codage et de meilleures pratiques dans l'ensemble de la base de code.
* Détection précoce des problèmes : réduit le cycle de feedback, car les problèmes peuvent être détectés à l'avance.
* Productivité accrue : évite que les développeurs aient à travailler sur des tâches répétitives.

Ce sont quelques-unes des raisons pour lesquelles le CI/CD est une pratique essentielle dans le développement logiciel moderne et pourquoi c'est un sujet si important à apprendre. Les étapes suivantes vous guideront à travers le processus de configuration d'un pipeline CI/CD pour votre projet.

## Comment configurer un pipeline CI/CD

### Étape 1 : Configurer une application Next.js

Si vous avez déjà une application web fonctionnelle, vous pouvez passer cette étape et aller directement à la première étape.

Sinon, configurons une application Next.js de base avec la configuration ESLint par défaut et Vitest, et poussons-la vers un dépôt GitHub.

#### Créer une application Next.js

Naviguez dans le répertoire où vous souhaitez créer le nouveau dossier de projet, puis exécutez la commande suivante dans votre terminal :

```bash
npx create-next-app@latest
```

Lorsque vous êtes invité avec les options d'installation, assurez-vous de choisir d'utiliser ESLint dans votre projet. Cela garantira que ESLint est correctement installé et qu'un script `lint` est créé dans le package.json.

Attendez que `create-next-app` crée le dossier et installe les dépendances du projet. Une fois terminé, naviguez dans le nouveau dossier et démarrez le serveur de développement :

```bash
cd <votre-nom-de-projet>
npm run dev
```

#### Configurer Vitest

Ajoutons Vitest au projet et ajoutons quelques tests automatisés à exécuter dans le pipeline CI/CD.

Tout d'abord, installez `vitest` et les dépendances de développement nécessaires :

```bash
npm install -D vitest @vitejs/plugin-react jsdom @testing-library/react

```

Créez un fichier `vitest.config.js` (ou `vitest.config.ts` si vous utilisez TypeScript) avec le contenu suivant :

```js
import { defineConfig } from 'vitest/config'
import react from '@vitejs/plugin-react'
 
export default defineConfig({
  plugins: [react()],
  test: {
    environment: 'jsdom',
  },
})
```

Et enfin, ajoutez le script `test` au package.json :

```
 "test": "vitest --no-watch"
```

Notez que j'ai ajouté l'option no-watch au script de test. Cela empêche Vitest de démarrer en mode watch par défaut dans l'environnement de développement.

Maintenant, vous pouvez ajouter des tests pour votre projet. Si vous ne savez pas comment commencer, vous pouvez consulter [ce guide](https://nextjs.org/docs/app/building-your-application/testing/vitest#creating-your-first-vitest-unit-test) pour quelques exemples.

#### Pousser le projet vers GitHub

Connectez-vous à votre compte GitHub et créez un nouveau dépôt. Une fois terminé, vous pouvez connecter le dépôt local avec celui que vous venez de créer, en ajoutant ce dépôt comme distant. Puis poussez les changements :

```bash
git add .
git commit -m "first commit"
git remote add origin git@github.com:<votre-nom-dutilisateur>/<votre-nom-de-depot>.git
git push origin main
```

Vous devriez maintenant être prêt à continuer avec la partie intéressante de ce tutoriel. :)

### Étape 2 : Configurer un Git Hook

Un Git hook est un script qui vous permet d'exécuter un événement dans le cycle de vie de Git. Dans ce cas, nous utiliserons Husky.

[Husky](https://typicode.github.io/husky/) est un hook de pré-commit pour Git qui vous permet de maintenir la qualité du code en exécutant certaines tâches lors de la validation ou de la poussée. Vous pouvez exécuter diverses vérifications avant de faire un commit avec de nouvelles modifications, telles que le linting du code et l'exécution de tests automatisés.

En implémentant ces vérifications, vous pouvez éviter de perdre du temps et des ressources en détectant les problèmes à l'avance avant de déclencher le workflow GitHub Actions.

Commençons par ajouter Husky au projet avec la commande suivante :

```bash
npm install --save-dev husky
```

Ensuite, configurons le projet en utilisant la commande d'initialisation de Husky :

```bash
npx husky init
```

Après avoir exécuté cette commande, vous remarquerez qu'un fichier pre-commit a été créé sous `./husky`. De plus, un script "prepare" a été ajouté dans le package.json.

Si vous ouvrez le fichier pre-commit à l'intérieur de `./husky`, vous trouverez le contenu suivant :

```bash
npm test
```

Comme son nom l'indique, ce fichier contient le code qui s'exécute avant de finaliser un commit. Avec tout configuré comme décrit, les tests s'exécuteront chaque fois que vous tenterez de créer un nouveau commit et les nouveaux commits ne seront ajoutés que si tous les tests passent.

#### Ajouter plus de Git hooks

Maintenant, modifions le contenu du fichier pre-commit pour que le linter de code s'exécute également avant de créer un nouveau commit.

Vous pouvez ouvrir votre éditeur de code préféré et ajouter `npm run lint` (ou le script ESLint correspondant si vous n'utilisez pas Next.js) dans une nouvelle ligne du fichier pre-commit. Alternativement, vous pouvez simplement exécuter la commande suivante depuis le dossier racine de votre projet :

```bash
echo "npm run lint" >> ./.husky/pre-commit
```

Maintenant, chaque fois que vous tenterez de faire un nouveau commit, les tests et le linter s'exécuteront, et le commit sera créé uniquement si tous les tests passent et qu'aucune erreur n'est trouvée dans le code.

#### Configurer lint-staged

Vous pouvez aller plus loin et inclure un outil appelé [lint-staged](https://github.com/lint-staged/lint-staged). Cet outil sera particulièrement utile si votre projet est grand, car il vous permet d'exécuter les Git hooks uniquement pour les fichiers staged. Dans ce cas, il ne lintera que les fichiers qui seront commités, évitant ainsi de perdre du temps à linter l'ensemble du projet.

Pour commencer à utiliser lint-staged, ajoutons-le comme dépendance de développement au projet :

```bash
npm install --save-dev lint-staged
```

Il existe [différentes façons de configurer lint-staged](https://github.com/lint-staged/lint-staged?tab=readme-ov-file#configuration) et vous pouvez choisir celle qui convient le mieux à vos besoins. J'ajouterai un script et un objet `lint-staged` au package.json de mon projet avec le contenu suivant :

```js
  "scripts": {
    "dev": "next dev",
    "build": "next build",
    "start": "next start",
    "lint": "next lint",
    "test": "vitest --no-watch",
    "prepare": "husky"
  },
  "lint-staged": {
	"*.{js, jsx,ts,tsx}": [
		"eslint --fix"
		]
	},
```

Maintenant, je peux remplacer `npm run lint` par `npm run lint-staged` dans le fichier pre-commit.

Chaque fois que je fais un nouveau commit, tous les fichiers staged `js`, `jsx`, `ts` ou `tsx` seront lintés et, s'il y a des problèmes correctibles, ils seront automatiquement corrigés.

Testons que le hook pre-commit fonctionne comme prévu en :

1. Exécutant `git add .`
2. Exécutant `git commit`
3. Attendant que le linter s'exécute et entrant un message de commit lorsque vous y êtes invité
4. Exécutant `git log` pour confirmer que le commit a été correctement créé

Si vous le souhaitez, vous pouvez ajouter plus de vérifications à votre fichier pre-commit pour répondre aux besoins de votre projet. Par exemple, vous pourriez exécuter un outil comme Prettier pour formater automatiquement votre code, ou [commitlint](https://commitlint.js.org/) pour linter vos messages de commit.

Maintenant, passons à la configuration d'un workflow GitHub Actions pour le projet.

### Étape 3 : Créer un workflow GitHub Actions

Avec la première partie terminée, nous pouvons passer à l'étape suivante. Ici, vous ajouterez un workflow GitHub Actions pour garantir l'intégration fluide des changements dans l'ensemble du projet.

#### Bases de GitHub Actions

GitHub Actions est une plateforme CI/CD qui vous permet d'automatiser la construction, les tests et le déploiement de votre projet. Elle vous permet également d'effectuer des actions lorsque certaines activités se produisent dans votre dépôt, comme l'ouverture d'une pull request ou la création d'un problème.

Les GitHub Actions sont configurées via des workflows définis dans des fichiers YAML. Ces workflows s'exécutent généralement lorsqu'ils sont déclenchés par un événement dans le dépôt, mais ils peuvent également être planifiés ou exécutés manuellement.

Les workflows sont situés dans le dossier `.github/workflows` et exécutent différents jobs. Chaque job inclut un ensemble d'étapes qui s'exécutent dans l'ordre sur le même runner ou serveur. Une étape peut être soit un script shell, soit une action (un morceau de code réutilisable qui aide à réduire le code répétitif dans vos workflows).

Mettons tout cela ensemble en créant le premier workflow.

#### Créer un workflow à exécuter lorsque vous poussez vers la branche main

Tout d'abord, créez un `.github/workflows/` sous la racine de votre projet. Ensuite, créez un fichier `run-test.yml`. Vous ajouterez du contenu à ce fichier pour créer un workflow CI.

La première ligne est facultative et inclut un nom pour le workflow. Il apparaîtra dans l'onglet "Actions" du dépôt GitHub :

```yaml
name: Run linter and tests on push

```

Ensuite, vous utiliserez la clé `on` pour définir l'événement ou les événements qui déclencheront l'exécution du workflow. Cela peut être un événement dans votre dépôt ou une planification horaire. Dans ce cas, définissons-le pour qu'il s'exécute chaque fois qu'un push vers le dépôt se produit :

```yml
on:
  push
```

Vous pouvez également définir des options sous le mot-clé `on` pour limiter l'exécution d'un workflow à certaines branches ou fichiers, par exemple pour s'exécuter uniquement lors d'un push vers la branche main :

```yml
on:
  push:
    branches:
      - main
```

En dessous, vous ajouterez la clé `jobs`. Elle regroupe tous les jobs du workflow, suivie du nom du premier job, dans ce cas `run-linter-and-tests`.

Les lignes en dessous définissent les propriétés du workflow, le configurant pour s'exécuter sur la dernière version d'un runner Ubuntu Linux et regroupant toutes les étapes qui s'exécutent sur ce job.

```yaml
jobs:
  run-linter-and-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm i

      - name: Lint code
        run: npm run lint

      - name: Run tests
        run: npm test
```

Comme mentionné précédemment, chaque étape peut être soit un script shell, soit une action. Vous pouvez voir la différence entre la première et la deuxième étape dans le code précédent.

La première spécifie avec le mot-clé `uses` qu'elle exécutera `actions/checkout`. Cette action est utilisée pour cloner le dépôt sur le runner afin que le workflow puisse utiliser le code du dépôt. La deuxième étape `Install dependencies` utilise le mot-clé `run` pour dire au job d'exécuter la commande `npm i` sur le runner.

Voici le fichier résultant complet :

```yaml
name: CI workflow
on:
  push
  
jobs:
  run-linter-and-tests:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: npm install
        run: npm i

      - name: Lint code
        run: npm run lint

      - name: Run tests
        run: npm test

```

Validons les changements et poussons-les vers le dépôt GitHub.

Maintenant, chaque fois que vous pousserez vers votre dépôt, le workflow sera déclenché. Si vous cliquez sur l'onglet "Actions" dans la barre de navigation de votre dépôt GitHub, vous trouverez une liste de toutes les exécutions de tous vos workflows et leurs logs complets.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot-2024-07-03-at-12.13.05-1.png)
_Onglet "Actions" dans une barre de navigation de dépôt GitHub_

De plus, vous verrez que dans l'onglet "Code" du dépôt GitHub, une coche verte apparaît à côté du dernier message de commit. Cela signifie que les workflows se sont exécutés et ont terminé avec succès.

Lorsque les jobs sont encore en cours d'exécution, vous verrez un point marron, et une croix rouge lorsqu'un workflow s'est terminé avec une erreur.

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screenshot_.png)

#### Ajouter un deuxième workflow à exécuter lorsqu'une PR est créée

Chaque dépôt peut avoir un ou plusieurs workflows, alors ajoutons un deuxième workflow à exécuter chaque fois qu'une PR est créée. Exécutons le rapport de couverture de code chaque fois qu'une PR est ouverte contre la branche main du dépôt.

Tout d'abord, créez et basculez vers une nouvelle branche `add-wf` :

```yaml
git checkout -b add-wf
```

Ensuite, créez un nouveau fichier YAML sous le répertoire `.github/workflows` et commencez à ajouter du contenu.

Tout d'abord, ajoutons le nom et quand exécuter le workflow avec le mot-clé `on` :

```yaml
name: Run Coverage on PR
on: pull_request

```

Après cela, vous utiliserez le mot-clé `jobs` pour décrire les jobs à exécuter. Définissons le premier comme `build-and-run-coverage` pour s'exécuter sur le runner `ubuntu-latest` :

```yaml
jobs:
  build-and-run-coverage:
    runs-on: ubuntu-latest
```

Maintenant, ajoutons des `steps` pour ce job :

```yaml
  steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm i
        
      - name: Build code
        run: npm run build

      - name: Run tests and coverage
        run: npm run coverage
```

Voici le code résultant complet :

```yaml
name: Run Coverage on PR
on: pull_request

jobs:
  build-and-run-coverage:
    runs-on: ubuntu-latest

      steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm i
        
      - name: Build code
        run: npm run build

      - name: Run tests and coverage
        run: npm run coverage
```

Maintenant, vous pouvez pousser le changement vers votre dépôt GitHub :

```bash
git add .
git commit -m 'add a wf to run on opened PR'
git push origin add-wf
```

Maintenant, vous pouvez ouvrir une PR contre votre branche `main` et attendre que le workflow se termine.

##### Commenter le rapport de couverture dans la PR

Comme mentionné précédemment dans cet article, les actions sont des morceaux de code réutilisables qui évitent le code répétitif dans le workflow. Une chose intéressante à leur sujet est qu'il existe de nombreuses actions déjà écrites par la communauté que vous pouvez utiliser dans vos workflows, ce qui vous fait gagner beaucoup de temps.

Pour compléter le workflow que nous avons créé, ajoutons une nouvelle étape qui utilise une action pour rapporter les résultats de couverture en tant que commentaire sur la pull request.

Tout d'abord, modifions le mot-clé `permissions` pour nous assurer que le workflow a le bon accès au contenu et pour créer des commentaires :

```yaml
 permissions:
      contents: read
      pull-requests: write
```

Ensuite, utilisons l'action [Vitest Coverage Report](https://github.com/marketplace/actions/vitest-coverage-report) en ajoutant une `step` dans le job `build-and-run-coverage` :

```yaml
- name: Report Coverage
        uses:  davelosert/vitest-coverage-report-action@v2
```

Le fichier `yaml` final ressemblera à ceci :

```yaml
name: Run Coverage on PR
on: pull_request

jobs:
  build-and-run-coverage:
    runs-on: ubuntu-latest

    permissions:
      contents: read
      pull-requests: write

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Install dependencies
        run: npm i
        
      - name: Build
        run: npm run build

      - name: Run test and coverage
        run: npm run coverage

      - name: Report Coverage
        uses:  davelosert/vitest-coverage-report-action@v2

```

Il y a une étape supplémentaire pour s'assurer que tout fonctionne comme prévu. Vous devez ajouter le rapporteur `json-summary` dans la configuration Vitest :

```ts
import { defineConfig } from "vitest/config";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  test: {
    environment: "jsdom",
    coverage: {
      provider: "v8",
      extension: [".tsx"],
      reporter: ['text', 'json-summary', 'json'],
    },
  },
});
```

Maintenant, apportez quelques modifications à votre projet et ajoutez des tests correspondants pour vérifier si le workflow fonctionne comme prévu.

Une fois que vous avez poussé vos changements vers le dépôt GitHub, ouvrez une PR contre la branche main de votre projet. Après que les workflows aient terminé leur exécution, vous devriez voir un commentaire montrant le résultat de la couverture :

![Image](https://www.freecodecamp.org/news/content/images/2024/07/Screen-Shot-2024-07-12-at-19.18.05.png)
_Rapport de couverture dans un commentaire de pull request_

### Étape 4 : Déployer le projet

En tant que dernière étape de ce tutoriel, déployons le projet sur [Vercel](https://vercel.com/). Vous allez configurer un déploiement automatique via Git qui déclenchera un redéploiement chaque fois que de nouveaux changements seront poussés ou fusionnés dans la branche main.

Tout d'abord, connectez-vous à votre compte Vercel, ou créez-en un si vous n'en avez pas déjà un. Ensuite, dans votre tableau de bord, cliquez sur "Add New Project" et cliquez sur le bouton "Import" à côté du nom de votre dépôt dans la section "Import Git Repository".

Si vous ne voyez pas votre dépôt listé, cela peut être dû à la configuration des permissions de votre application GitHub. Vous pouvez les gérer dans la section des paramètres de votre compte GitHub.

Enfin, choisissez un nom pour le projet dans la section "Configure Project" et cliquez sur le bouton "Deploy". Vous pouvez maintenant voir les détails du déploiement en cliquant sur le lien "Deployment".

Les déploiements automatiques de Vercel garantissent que le projet déployé est toujours mis à jour avec les derniers changements. Ils ont également l'avantage des [Preview Deployments](https://vercel.com/docs/deployments/preview-deployments), une URL de prévisualisation qui vous permet de tester de nouvelles fonctionnalités avant de fusionner les changements en production.

Si vous avez suivi ce tutoriel, avec cette étape terminée, vous aurez complété la partie CD du pipeline CI/CD pour votre projet. Maintenant, vous pouvez être sûr que tout code poussé vers la branche main est linté et testé, et une fois que toutes les vérifications passent, il est automatiquement poussé en production.

## Conclusion

Dans ce guide, vous avez appris l'importance du CI/CD dans l'écosystème moderne de développement logiciel et ses principaux avantages. Vous avez également fait vos premiers pas dans ce domaine en créant votre propre pipeline CI/CD pour votre projet, en apprenant à utiliser Husky et GitHub Actions.

Maintenant, vous pouvez continuer à apprendre davantage sur ces outils et améliorer votre pipeline CI/CD en le personnalisant pour mieux répondre aux besoins de votre projet.

J'espère que vous avez pu acquérir de nouvelles connaissances et que vous avez apprécié ce tutoriel. Merci d'avoir lu !