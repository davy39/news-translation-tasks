---
title: Comment automatiser le CI/CD avec GitHub Actions et optimiser votre flux de
  travail
subtitle: ''
author: Chidiadi Anyanwu
co_authors: []
series: null
date: '2025-04-14T15:45:58.059Z'
originalURL: https://freecodecamp.org/news/automate-cicd-with-github-actions-streamline-workflow
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1744638276204/5cf04403-6bf0-4bf1-b9d3-89722bd90425.png
tags:
- name: github-actions
  slug: github-actions-1
- name: GitHub
  slug: github
- name: workflow
  slug: workflow
- name: Productivity
  slug: productivity
seo_title: Comment automatiser le CI/CD avec GitHub Actions et optimiser votre flux
  de travail
seo_desc: 'CI/CD stands for Continuous Integration and Continuous Delivery. It is
  a system or set of processes and methodologies that help developers quickly update
  codebases and deploy applications.

  The Continuous Integration (CI) part of CI/CD means that deve...'
---

CI/CD signifie Intégration Continue et Livraison Continue. Il s'agit d'un système ou d'un ensemble de processus et de méthodologies qui aident les développeurs à mettre à jour rapidement les bases de code et à déployer des applications.

La partie Intégration Continue (CI) de CI/CD signifie que les développeurs peuvent toujours intégrer ou fusionner leurs modifications dans le dépôt partagé sans rien casser. La Livraison Continue, en revanche, signifie que les modifications de code sont automatiquement préparées pour la publication après les tests et la validation.

Le CI/CD implique principalement diverses étapes comme la construction, les tests, la mise en scène et le déploiement.

* **Phase de construction :** C'est ici que le code et ses dépendances sont compilés en un seul exécutable. Il s'agit de la première phase de l'Intégration Continue, déclenchée par un événement comme le fait de pousser du code vers le dépôt.

* **Phase de test :** Ici, les artefacts construits sont testés pour s'assurer que le code s'exécute comme prévu.

* **Mise en scène :** Ici, l'application est exécutée dans un environnement similaire à la production afin de s'assurer qu'elle est prête pour la production.

* **Déploiement :** Ici, l'application est automatiquement déployée auprès des utilisateurs finaux.

Dans cet article, je vais expliquer comment fonctionne GitHub Actions. Je parlerai également des concepts de base de GitHub Actions, puis nous l'utiliserons pour construire un exemple de pipeline CI/CD.

## Qu'est-ce que GitHub Actions ?

GitHub Actions est un service ou une fonctionnalité de la plateforme GitHub qui permet aux développeurs de créer leurs propres flux de travail CI/CD directement sur GitHub. Il exécute des tâches sur des conteneurs hébergés par GitHub. Les tâches sont exécutées comme défini dans un fichier YAML appelé un flux de travail. Ce fichier de flux de travail doit se trouver dans le dossier *.github/workflows* du dépôt pour fonctionner.

## Concepts de base de GitHub Actions

GitHub Actions se compose d'événements, de tâches, de runners, de flux de travail et de diverses autres fonctionnalités. Voici une brève explication des principaux concepts :

**Événements :** Un événement est essentiellement quelque chose qui s'est produit. Avec GitHub, un événement peut être un push (lorsque vous poussez votre code vers le dépôt), une pull request, ou même une tâche cron. Ces événements déclenchent le processus CI/CD.

**Tâches :** Lorsque vous utilisez CI/CD, vous souhaitez pouvoir déclencher une activité qui doit être effectuée automatiquement. Cette activité est connue sous le nom de tâche ou d'étape dans GitHub. Il peut s'agir de construire votre code, de le tester ou de le déployer.

Chacune de ces tâches doit être définie par des commandes. Une tâche GitHub Actions se compose généralement du nom et des instructions sur ce qu'il faut faire sous la forme d'une commande qui commence par `- run:` ou d'une Action qui commence par `- uses:`.

```yaml
steps:
  - name: Checkout code
    uses: actions/checkout@v3

  - name: Set up Node.js
    uses: actions/setup-node@v3
    with:
      node-version: 16

  - name: Install dependencies
    run: npm install

  - name: Run tests
    run: npm test

  - name: Build project
    run: npm run build

  - name: Deploy
    run: echo "Deploy step goes here"
```

**Runner :** Un runner GitHub est un serveur qui exécute vos tâches. Il exécute ce qui est défini dans votre flux de travail GitHub. Vous pouvez utiliser vos propres runners ou utiliser les runners GitHub.

**Job :** Un job est une collection d'étapes qui sont exécutées sur le même runner. Les jobs sont définis dans un fichier appelé le workflow.

**Workflow :** Le workflow GitHub est une série de jobs définis dans un fichier YAML, qui sont déclenchés par un événement. Les événements ne déclenchent pas de tâches individuelles. Ils ne peuvent déclencher que des workflows. Ensuite, les tâches dans les jobs du workflow sont exécutées.

**Contextes :** Ils fournissent un moyen d'accéder à des informations sur les workflows, les jobs et les environnements dans GitHub. Ils sont accessibles avec l'expression `$${{ <context> }}`. Les exemples incluent `github`, `env`, `vars` et `secrets`. Le contexte `github` est utilisé pour accéder à des informations sur le workflow. Par exemple :

```yaml
$${{github.repository}} # devrait indiquer le nom du dépôt

$${{github.actor}}  # devrait indiquer le nom d'utilisateur de l'utilisateur qui a initialement déclenché le workflow
```

**Secrets :** Cela est utilisé pour stocker et accéder à des informations sensibles qui sont utilisées par le workflow et disponibles pour celui-ci. Les secrets sont masqués lorsqu'ils sont imprimés dans le journal. Un exemple est $${{secrets.GITHUB\_TOKEN}}.

## Comment construire un pipeline CI/CD simple

Ici, nous allons construire un exemple de workflow pour déployer un site web simple en HTML et CSS sur GitHub Pages. Suivez les étapes ci-dessous :

1. Allez au code d'exemple dans mon dépôt et forkz-le depuis [ici](https://github.com/chidiadi01/StaticPage-Starter).

2. Allez dans l'onglet des paramètres du dépôt GitHub :

![Onglet des paramètres](https://cdn.hashnode.com/res/hashnode/image/upload/v1744220928970/d2f62ae0-49be-4770-b931-59e5bc28e20e.png align="center")

3. Allez dans les paramètres des Pages :

![Menu des paramètres des Pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1744220974335/4aeac1df-be0d-493d-98d3-fb9ea4d48ca0.png align="center")

4. Définissez la source de déploiement sur la branche `main` :

![Définir la source de déploiement sur la branche main dans GitHub Pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1744290941501/365d8b5d-1265-42be-9de4-d3a07b984736.png align="center")

5. Allez dans les paramètres généraux des Actions et faites défiler jusqu'en bas :

6. ![Trouver le paramètre Général des Actions](https://cdn.hashnode.com/res/hashnode/image/upload/v1744221468786/d94fe477-65a3-49dc-85ea-6ab8cb2f9c63.png align="center")

En bas, définissez les permissions du workflow sur lecture et écriture :

![Définir les permissions du workflow sur lecture et écriture](https://cdn.hashnode.com/res/hashnode/image/upload/v1744221589612/4f5b1cf2-8343-4da8-ad61-21ba76319ffc.png align="center")

7. Dans le dépôt GitHub, vous pouvez le cloner sur votre PC ou appuyer sur le point (.) sur votre clavier pour ouvrir GitHub Codespaces, la version en ligne de VS Code.

8. Allez dans la barre latérale et cliquez sur créer un nouveau fichier :

![Créer un nouveau fichier](https://cdn.hashnode.com/res/hashnode/image/upload/v1744292745424/a3ca0a1e-13cf-4182-8425-9c3500e01e3d.png align="center")

9. Créez un dossier workflows et un fichier. Vous pouvez l'appeler `deploy.yaml`.

![Créer un dossier workflows et un fichier nommé deploy.yaml](https://cdn.hashnode.com/res/hashnode/image/upload/v1744292931628/300665a5-d517-46b1-9b30-21dd4bc228a6.png align="center")

10. Copiez ce code dans le fichier :

```yaml
name: Déployer HTML et CSS statiques sur GitHub Pages

# Déclencher le workflow lors du push vers la branche main

on:
  push:
    branches:
      - main
# Définir sur quel système d'exploitation le job doit s'exécuter
jobs:
  deploy:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      # Étape 1 : Checkout du dépôt
      - name: Checkout Code
        uses: actions/checkout@v4

      # Étape 2 : Vérifier les fichiers qui ont été checkés
      - name: Afficher les fichiers
        run: ls

      # Étape 3 : Déployer sur GitHub Pages
      - name: Déployer
        uses: peaceiris/actions-gh-pages@v4
        with:
          github_token: ${{ secrets.GITHUB_TOKEN }}
          publish_dir: ./ # Les fichiers HTML et CSS se trouvent dans le répertoire racine, donc celui-ci devrait être le répertoire de publication
```

11. Commitez le code. Vous devriez voir le job en cours d'exécution lorsque vous revenez au dépôt :

![Job en cours d'exécution](https://cdn.hashnode.com/res/hashnode/image/upload/v1744292376966/93d6078c-02c3-41f4-a4b5-09639522bbbe.png align="center")

Lorsque vous avez terminé, revenez à la page d'accueil du dépôt et cliquez sur la section Déploiements. Là, vous verrez le lien GitHub Pages vers le déploiement :

![Lien GitHub Pages](https://cdn.hashnode.com/res/hashnode/image/upload/v1744293345646/e523a2b9-73a6-4ecf-9df8-99e03b457ad1.png align="center")

Lorsque vous avez terminé, votre dépôt devrait ressembler à [celui-ci](https://github.com/chidiadi01/StaticPage-Final).

## Conclusion

Dans cet article, vous avez appris comment fonctionne le processus CI/CD. Nous avons également couvert les concepts de base de GitHub Actions. Enfin, nous avons créé un exemple de pipeline CI/CD avec GitHub Actions. Si vous avez aimé cet article, partagez-le avec d'autres. Vous pouvez également me contacter sur [LinkedIn](https://linkedin.com/in/chidiadi-anyanwu) ou [X](https://x.com/chidiadi01).