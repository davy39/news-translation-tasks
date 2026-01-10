---
title: Comment configurer l'intégration continue avec Circle CI, EmberJS et GitHub
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-25T15:22:23.000Z'
originalURL: https://freecodecamp.org/news/first-steps-into-continuous-integration-with-circle-ci-emberjs-and-github-1e273ea62f0c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*BH8-NzQcUrhzko9JUIGYGg.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: Devops
  slug: devops
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment configurer l'intégration continue avec Circle CI, EmberJS et GitHub
seo_desc: 'By Michael Xavier

  What is Continuous Integration and why should we do it?

  Continuous Integration (CI) is the process of automating the building and testing
  of code. This happens every time a project team member commits changes to version
  control.

  For...'
---

Par Michael Xavier

### **Qu'est-ce que l'intégration continue et pourquoi devrions-nous le faire ?**

L'intégration continue (CI) est le processus d'automatisation de la construction et des tests de code. Cela se produit chaque fois qu'un membre de l'équipe de projet commite des changements dans le contrôle de version.

Par exemple, vous apportez des modifications au code de votre dépôt GitHub et poussez ce changement vers la branche master. Cela déclenche un processus CI pour construire un environnement virtuel et exécuter des commandes. Les commandes configurent l'environnement tel qu'il serait sur un serveur de production. Ensuite, ils exécutent la suite de tests automatisés que vous avez écrite pour tester votre code.

CI est souvent utilisé pour :

* valider les branches séparées sur lesquelles un développeur travaille. Les branches sont bien testées avant d'être fusionnées dans la branche principale du projet.
* valider et déployer les dernières versions d'un projet lorsque les branches passent la validation.

Avoir du code continuellement intégré dans le projet et le tester réduit :

* les conflits de fusion
* les bugs difficiles à corriger
* les stratégies de code divergentes
* les efforts dupliqués

Cela garde la branche master propre. En savoir plus sur l'intégration continue [ici](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration).

### Objectifs du tutoriel

C'est votre première étape dans le processus d'intégration continue. Alors, gardons les choses très simples. Notre objectif est de créer un dépôt sur GitHub et d'exécuter CI sur ce dépôt chaque fois qu'un nouveau commit est poussé. Nous afficherons également un badge qui indique le statut de notre build actuel.

Les outils que nous utiliserons pour cette démonstration :

* [GitHub](https://github.com/)
* [CircleCI](https://circleci.com/)
* [EmberCLI](https://ember-cli.com/)

Maintenant, commençons.

### **Configurer un compte Github**

Si vous n'en avez pas déjà un, procurez-vous un [compte GitHub gratuit](https://github.com/).

Ensuite, rendez-vous dans les [paramètres de facturation](https://github.com/settings/billing) et entrez vos informations de paiement. Ne vous inquiétez pas des frais. Nous aurons 1000 minutes mensuelles de build gratuites avec l'option que nous choisirons (Circle CI). C'est plus que suffisant pour ce projet de démonstration.

Enfin, créez un nouveau dépôt appelé **ci-ember-demo**. Ne l'initialisez pas.

![Image](https://cdn-media-1.freecodecamp.org/images/x5yCA6KDo-gkSEn8p1vXtco-DDr0Dvzloctb)

### **Créer une application Ember de base**

#### **Installer Ember CLI**

Utilisons NPM pour installer [Ember CLI](https://ember-cli.com/). Il inclut les outils dont nous avons besoin pour générer un projet de base.

```
npm install -g ember-cli
```

#### Créer un projet Ember

Créons un projet appelé **ci-ember-demo** en utilisant Ember CLI :

```
# cd dans le bureau
  cd ~/desktop/
# créer un nouveau projet
  ember new ci-ember-demo
# cd dans le répertoire
  cd ci-ember-demo
# exécuter le serveur
  ember s
```

Maintenant, rendez-vous sur `http://localhost:4200` et vous devriez voir cet écran :

![Image](https://cdn-media-1.freecodecamp.org/images/Lht9dx68OGa2jvn7tugfFsk1HpvrHVgLqi6Y)
_En cours d'exécution_

Le projet Ember de base fonctionne comme prévu. Vous pouvez arrêter le serveur avec `ctrl+C`.

#### Vérifier que les tests par défaut sont réussis

Maintenant, dans le terminal, exécutons les tests qui ont été générés avec le projet :

```
npm test
# ou alternativement
ember test
```

![Image](https://cdn-media-1.freecodecamp.org/images/vvTynyhB8ykZweETG6aF6AKvCgD8z2WPkMwx)

Vous devriez voir une série de six tests par défaut s'exécuter. Tous devraient réussir.

L'idée est que ces tests et d'autres que vous écrivez au fur et à mesure que vous développez votre projet seront continuellement exécutés lorsque vous pousserez des changements vers le dépôt.

### **Pousser votre projet vers Github**

Rendez-vous dans le dossier du projet **ci-ember-demo** pour modifier le fichier `README.md`. Remplacez ce qui s'y trouve par quelque chose comme :

```
## ci-ember-demo
```

```
Ceci est une application de démonstration CI Ember de base. Consultez le tutoriel : 'Premier pas dans l'intégration continue avec Circle CI'.
```

#### Obtenez votre URL distante et configurez-la

Retournez à votre dépôt GitHub et récupérez l'URL distante qui devrait ressembler à ceci :

```
git@github.com:username/repo_name.git
```

À l'intérieur du dossier **ci-ember-demo**, initialisez le dépôt :

```
git init
```

Ensuite, [ajoutez l'URL distante](https://help.github.com/articles/adding-a-remote/) pour que Git sache où nous poussons nos fichiers :

```
git remote add origin git@github.com:username/repo_name.git
# vérifiez qu'elle a été configurée, devrait afficher l'origine mise à jour
  git remote -v
```

Il est temps de pousser notre code vers Github :

```
# ajouter tous les changements
  git add .
# créer un commit avec un message
  git commit -m "[INIT] Project"
# pousser les changements vers la branche master du dépôt
  git push origin master
```

Le dépôt Git distant se met à jour avec les changements que nous avons poussés :

![Image](https://cdn-media-1.freecodecamp.org/images/34KNCYpk2Mvtkk4SDX43szu7ijYY6FaeobDj)

Maintenant, nous avons un répertoire de projet principal et un dépôt. Il est temps de configurer la plateforme CI.

### Configurer CircleCI — Une plateforme d'intégration et de livraison continues

[CircleCI](https://circleci.com/) sera notre outil de choix pour l'intégration continue. Il est simple, populaire et offre 1000 minutes de build gratuites par mois.

Rendez-vous sur le [marketplace de GitHub](https://github.com/marketplace/circleci) et configurez un plan.

![Image](https://cdn-media-1.freecodecamp.org/images/fUkXRbm841dluhObt9rkeZ5SO4GPLkf-X22N)

Sélectionnez le plan gratuit.

![Image](https://cdn-media-1.freecodecamp.org/images/0CttA0zoPXBe5fqJ7oAmzCvPGjkLf--7qqGO)

Ensuite, rendez-vous sur CircleCI et [connectez-vous avec votre compte GitHub](https://circleci.com/vcs-authorize/) :

![Image](https://cdn-media-1.freecodecamp.org/images/UnCvLRsJdIcS3EfzGFBC-iFi26m5I8XNuT2Z)

Une fois connecté, allez dans la section **Ajouter un projet**. Vous verrez une liste de tous vos dépôts GitHub.

Cliquez sur **Configurer le projet** sur notre **ci-ember-demo**.

Ensuite, sélectionnez Linux comme système d'exploitation et Node pour le langage.

![Image](https://cdn-media-1.freecodecamp.org/images/GorjgybJB7RTI-hR0b3bpmMGhEPMKPSF1rfp)

Cliquez sur **Démarrer la construction**. Le projet tentera de construire et de faire ce que les processus d'intégration continue font.

Étant donné que nous n'avons aucun paramètre de configuration, le processus échouera presque immédiatement.

Rendez-vous dans l'onglet **Builds** qui liste tous les **Jobs** qui ont été exécutés, vous devriez voir cet échec comme suit :

![Image](https://cdn-media-1.freecodecamp.org/images/C9IIu6eDlvxDogb5ECMMXX2NfGzJCQg-fKDZ)

C'est ce à quoi nous nous attendions. Rien ne fonctionne vraiment car le processus CI n'est pas configuré.

### **Configurer CI dans le projet Ember**

#### **Obtenir le markdown pour afficher le statut CI de notre projet**

CircleCI fournit des badges de statut intégrables. Ils affichent le statut de votre dernier build. Avant de partir, obtenons le markdown pour un badge de statut.

Allez dans Paramètres → Projets → paramètres de **ember-ci-demo** → Badges de statut.

Copiez le code d'intégration en Markdown.

![Image](https://cdn-media-1.freecodecamp.org/images/xVXSeQDm6r6gBlJmYF-sQo7iZVF6R1BgEnVD)

Dans le fichier `README.md` de **ci-ember-demo**, collez le code d'intégration sous le titre. Cela ressemblera à ceci :

```
## ci-ember-demo
[![CircleCI](https://circleci.com/gh/username/ci-ember-demo.svg?style=svg)](https://circleci.com/gh/username/ci-ember-demo)
...
```

#### Ajouter la configuration CI

À la racine de **ember-ci-demo**, créez un dossier nommé `.circleci` et créez un fichier appelé `config.yml`. C'est là que tous nos paramètres de configuration iront. Ajoutez ce qui suit :

```
version: 2
jobs:
  build:
    docker:
      - image: circleci/node:7.10-browsers
        environment:
          CHROME_BIN: "/usr/bin/google-chrome"
    steps:
      - checkout
      - run: npm install
      - run: npm test
```

Arrêtons-nous et regardons ce qui se passe ici.

```
# définir la version de CircleCI à utiliser.
# nous utiliserons la dernière version.
version: 2
```

Ensuite, nous configurerons les jobs à exécuter lorsque le CI est déclenché.

```
jobs:
  # dire à CI de créer un environnement de nœud virtuel avec Docker
  # spécifier l'image virtuelle à utiliser
  # le suffixe -browsers indique qu'il doit avoir des navigateurs préinstallés
  build:
    docker:
      - image: circleci/node:7.10-browsers
        
        # utiliser Google Chrome pour exécuter nos tests
        environment:
          CHROME_BIN: "/usr/bin/google-chrome"
```

Enfin, disons-lui quoi faire une fois l'environnement configuré :

```
steps:
  - checkout
  
  # installer les packages npm requis
  - run: npm install
  # exécuter la suite de tests
  - run: npm test
```

#### Pousser les changements vers la branche master.

Passez en revue vos changements et poussez-les vers la branche master du dépôt.

Maintenant, retournez à CircleCI et consultez l'onglet **Jobs**. Vous verrez maintenant un build réussi. Il a pu prendre les paramètres de `config.yml`, configurer les environnements virtuels corrects et exécuter nos tests comme nous l'avons fait localement lorsque nous avons généré le projet pour la première fois.

![Image](https://cdn-media-1.freecodecamp.org/images/tPRGc-3ndS44MTBiEwSGIdc5IrWpJREtNMki)

Si vous regardez le dépôt sur GitHub, vous verrez le badge de statut CircleCI en vert. Cela indique à nouveau que le dernier build est réussi.

![Image](https://cdn-media-1.freecodecamp.org/images/10naRjzFWzkWjnlKNh8YB5FyZ8rk-Ie1MeLn)

### **Conclusion**

C'est tout ! Maintenant, chaque fois que vous créez une nouvelle pull request ou poussez des changements vers master, le CI exécutera tous les tests. Le statut de ce job sera affiché dans CircleCI et le badge sur votre dépôt. Réussite ou échec, vous obtenez les bonnes informations dont vous avez besoin pour bien développer.

Félicitations pour avoir fait vos premiers pas dans l'intégration continue !

![Image](https://cdn-media-1.freecodecamp.org/images/qwchC6rl8eTEAMzd2WE2hHlNYGNdStMJsuMG)
_Des moments excitants_

### Sources

[Qu'est-ce que l'intégration continue ? — Sam Guckenheimer](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration)