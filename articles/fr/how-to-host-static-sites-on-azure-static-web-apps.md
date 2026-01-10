---
title: Comment héberger des sites statiques sur Azure Static Web Apps gratuitement
subtitle: ''
author: Shrijal Acharya
co_authors: []
series: null
date: '2024-06-18T10:59:18.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-static-sites-on-azure-static-web-apps
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/host_static_sites_swa_azure.png
tags:
- name: Azure
  slug: azure
- name: Web Development
  slug: web-development
seo_title: Comment héberger des sites statiques sur Azure Static Web Apps gratuitement
seo_desc: "In this article, I will show you how you can host your React/Next.js app\
  \ or any static web app on Azure Static Web Apps. \nI will be showing you both ways\
  \ of doing it – through the GUI and with the CLI.\nI assume you already have built\
  \ a project and op..."
---

Dans cet article, je vais vous montrer comment héberger votre application React/Next.js ou toute autre application web statique sur Azure Static Web Apps. 

Je vais vous montrer les deux méthodes pour le faire – via l'interface graphique et avec la CLI.

Je suppose que vous avez déjà construit un projet et, éventuellement, l'avez poussé sur GitHub ou une autre alternative, comme GitLab ou Bitbucket.

Il est temps de mettre votre projet en ligne et de le présenter au monde. 💪 

Que ce soit votre première fois avec Azure ou que vous soyez déjà un expert, n'hésitez pas à suivre ce guide. 

## Qu'est-ce que le CI/CD ?

Avant de plonger dans Azure Static Web App, laissez-moi vous donner un bref aperçu de ce qu'est le CI/CD.

Imaginez que vous construisez votre nouvelle application web géniale. Maintenant, pour vous assurer qu'elle est toujours à jour et fonctionnelle, vous avez besoin de quelque chose appelé Intégration Continue/Déploiement Continu (CI/CD). 

Voici comment cela fonctionne :

* **Intégration Continue (CI)** est le processus de construction et de test automatique de votre code chaque fois que vous apportez des modifications et de vérification qu'il fonctionne comme vous l'attendez.
* **Déploiement Continu (CD)** est le processus de déploiement automatique de votre code testé en production.

Vous avez peut-être déjà rencontré le CI/CD si vous avez déjà hébergé votre projet sur Vercel, Netlify ou toute autre plateforme d'hébergement de sites, et remarqué que, une fois que vous poussez vos modifications locales vers votre dépôt distant, ces modifications sont reflétées sur le site hébergé d'origine en quelques minutes seulement. Magique, n'est-ce pas ? Tout cela est possible grâce au CI/CD.

En bref, le CI/CD garantit que votre projet est testé et déployé chaque fois que vous poussez de nouveaux commits vers le dépôt hébergeant votre projet.

## Comment pousser votre projet sur GitHub

Dans cette étape, j'utiliserai GitHub comme exemple. Si votre projet est déjà poussé sur GitHub, n'hésitez pas à sauter cette étape. Sinon, suivez les étapes décrites ci-dessous.

### Se connecter à GitHub CLI

Saviez-vous que vous pouvez créer un dépôt GitHub directement depuis votre ligne de commande ?

Commençons. Tout d'abord, assurez-vous d'avoir GitHub CLI installé. Pour les instructions d'installation, suivez les étapes décrites [ici](https://github.com/cli/cli/blob/trunk/docs/install_linux.md).

Pour authentifier votre GitHub CLI à votre compte, exécutez la commande suivante :

```bash
gh auth login
```

Suivez les étapes affichées dans votre terminal pour vous authentifier avec GitHub. Une fois terminé, vous pouvez passer à l'étape suivante.

### Créer un dépôt

Une fois connecté, vous pouvez exécuter la commande suivante pour démarrer un mode de création de dépôt interactif :

```bash
gh repo create
```

Ou, spécifiez directement les options comme suit :

```bash
gh repo create <nom_du_depot> --public --license mit --description <description_du_depot>
```

L'exécution de cette commande créera un dépôt avec toutes les options spécifiées dans votre compte GitHub.

### Pousser vos modifications

Maintenant que vous vous êtes authentifié et que vous avez créé un dépôt dans votre compte GitHub, il est temps de pousser vos modifications locales vers le dépôt distant.

Exécutez les commandes suivantes pour pousser vos modifications locales vers le dépôt distant :

```bash
git branch -M main
git remote add origin https://github.com/<nom_utilisateur>/<nom_du_depot>.git
git push -u origin main
```

Notez que si vous avez configuré l'authentification SSH, vous devez vous assurer de changer l'URL d'origine pour suivre le protocole SSH.

Cela conclut la préparation initiale. Maintenant, procédons à la création de l'Azure Static Web App. 🚀

## Héberger votre projet avec Azure SWA CLI

Dans cette section, vous apprendrez comment héberger votre projet statique, qu'il soit construit avec Next.js, React ou tout autre site statique, en utilisant Azure SWA CLI.

Tout d'abord, vous devez installer le package `@azure/static-web-apps-cli` en tant que dépendance de développement. 

Si vous utilisez `pnpm` comme gestionnaire de paquets, exécutez la commande suivante. La commande peut varier en fonction des différents gestionnaires de paquets.

```bash
pnpm install -g @azure/static-web-apps-cli
```

Maintenant, construisez votre projet avec la commande de construction appropriée :

```bash
pnpm run build
```

Il est temps de déployer l'application avec le dossier de construction. Exécutez la commande suivante pour la déployer sur Azure SWA :

```bash
swa deploy <emplacement_construction> --env production
```

Si votre application utilise une API, vous devez alors passer l'emplacement du dossier `api` en tant que flag à la commande ci-dessus. Ainsi, votre commande finale serait :

```bash
swa deploy <emplacement_construction> --api-location <emplacement_dossier_api> --env production
```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-5-.png)
_Déploiement du projet avec Azure Static Web App CLI._

C'est tout. Votre site est déployé sur Azure Static Web App via la CLI. 🎉 Vous pouvez le consulter à l'URL indiquée. 

Il existe d'autres configurations qui peuvent être spécifiées. Pour des configurations supplémentaires, suivez ce [lien](https://learn.microsoft.com/en-us/azure/static-web-apps/static-web-apps-cli-configuration).

## Comment héberger votre projet avec l'interface graphique du portail Azure

Dans cette section, nous allons créer une toute nouvelle Azure SWA via le portail Azure.

Rendez-vous sur le portail Azure à l'adresse [https://portal.azure.com](https://portal.azure.com) et recherchez Azure Static Web App.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-from-2024-06-15-16-24-56.png)
_Résultats de recherche du portail Azure pour Static Web App._

 Cliquez sur "Créer" et vous devriez être invité à fournir une série de configurations supplémentaires.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-1-.png)
_Création d'une nouvelle Azure Static Web App._

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Screenshot-2024-06-15-at-16-39-09-Microsoft-Azure.png)
_Configuration des paramètres pour l'Azure Static Web App._

Pour le Groupe de ressources, créez-en un et nommez-le comme vous le souhaitez. Donnez également un nom à votre application web.

Si votre projet est hébergé sur GitHub, choisissez GitHub comme option et sélectionnez le dépôt dans le menu déroulant. Pour la branche, sélectionnez 'main' si vous avez créé le projet à partir de zéro avec les paramètres par défaut.

Si vous utilisez d'autres alternatives, sélectionnez celle qui correspond à vos critères.

Laissez tout le reste par défaut et cliquez sur "Vérifier + créer" et attendez que le projet soit hébergé sur Azure SWA.

Dans la section Vue d'ensemble de l'application, vous devriez voir l'URL de votre projet construit. Voici un aperçu du mien :

![Image](https://www.freecodecamp.org/news/content/images/2024/06/Untitled-design-2-.png)
_Vue d'ensemble du tableau de bord Azure Static Web App._

Visitez l'URL et vous devriez avoir votre site prêt. 🥳

![Image](https://www.freecodecamp.org/news/content/images/2024/06/image-84.png)
_Section héroïque du projet déployé._

## Conclusion

À ce stade, vous devriez avoir une idée générale de la manière d'héberger une application web statique sur Azure Static Web Apps.

Bien que nous aurions pu aborder des sujets supplémentaires comme l'ajout d'un domaine personnalisé à notre site, cela peut ne pas s'appliquer à la plupart d'entre vous, donc je n'inclus pas les étapes dans cet article. Pour en savoir plus, visitez ce [lien](https://learn.microsoft.com/en-us/azure/static-web-apps/custom-domain-external).

C'est tout pour cet article. Merci beaucoup d'avoir lu ! À la prochaine. 🧡

Maintenant que vous avez eu un aperçu de mon portfolio dans l'image ci-dessus, pourquoi ne pas entrer en contact ? 😉 N'hésitez pas à me connecter ici :

* **GitHub** : [https://github.com/shricodev](https://github.com/shricodev)
* **LinkedIn** : [https://linkedin.com/in/iamshrijal](https://linkedin.com/in/iamshrijal)
* **Twitter** : [https://twitter.com/shricodev](https://twitter.com/shricodev)