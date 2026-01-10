---
title: Comment configurer l'intégration continue sur GitLab en utilisant Docker
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-12T19:11:31.000Z'
originalURL: https://freecodecamp.org/news/how-to-setup-ci-on-gitlab-using-docker-66e1e04dcdc2
coverImage: https://cdn-media-1.freecodecamp.org/images/1*b7KBZqZQ_VZ3kFu6lQQaYQ.png
tags:
- name: coding
  slug: coding
- name: Continuous Integration
  slug: continuous-integration
- name: Docker
  slug: docker
- name: GitLab
  slug: gitlab
- name: 'tech '
  slug: tech
seo_title: Comment configurer l'intégration continue sur GitLab en utilisant Docker
seo_desc: 'By Ying Kit Yuen

  An example using Docker to test and build your pipeline


  In the past you may have tried different tools to manage the deployment of your
  applications effectively. In this tutorial, I’ll be showing you a quick and easy
  way to set up c...'
---

Par Ying Kit Yuen

Un exemple utilisant Docker pour tester et construire votre pipeline

![Image](https://cdn-media-1.freecodecamp.org/images/1*b7KBZqZQ_VZ3kFu6lQQaYQ.png)

Dans le passé, vous avez peut-être essayé différents outils pour gérer efficacement le déploiement de vos applications. Dans ce tutoriel, je vais vous montrer une méthode rapide et facile pour configurer l'intégration continue pour votre environnement en utilisant GitLab et Docker. Alors, commençons.

Voici ce que nous allons configurer :

* Contrôle de version
* Suivi des problèmes
* Documentation
* Intégration continue
* Livraison continue
* Dépôt (artifacts/images docker)

Des outils comme [Jenkins](https://jenkins.io/) sont bons pour l'intégration et la livraison continues. [Mantis](https://www.mantisbt.org/) aide au suivi des problèmes. Mais pour améliorer l'efficacité et la qualité de notre projet, nous devons rassembler tous ces outils. Par exemple, nous pouvons vouloir un hook de commit git avec les problèmes existants, ou déclencher un test automatisé après avoir poussé des commits sur la branche master.

Habituellement, la plupart des outils fournissent déjà une intégration prête à l'emploi avec d'autres services courants, mais il est encore difficile de les configurer parfois. De plus, le flux de travail serait interrompu si l'un des services de la chaîne tombait en panne. Il serait donc idéal d'avoir une seule plateforme qui pourrait répondre à toutes ces exigences, et c'est pourquoi nous avons choisi [GitLab](https://gitlab.com).

### GitLab CI

[GitLab.com](https://gitlab.com) est un service basé sur SAAS où vous pouvez héberger votre dépôt Git, suivre les problèmes et écrire le wiki en markdown. [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/) vous permet également de configurer l'intégration continue en utilisant n'importe quelle image Docker disponible sur [Docker Hub](https://hub.docker.com/). Examinons l'exemple suivant.

#### Le fichier YML de GitLab CI

GitLab CI utilise un fichier YAML `.gitlab-ci.yml` pour définir la configuration du projet, qui inclut une définition de toutes les étapes à exécuter après qu'un pipeline CI/CD est déclenché en réponse à un git push/merge. Dans cet exemple, nous avons un projet Node.js simple et nous aimerions nous assurer que le code est bon en utilisant un linter et en exécutant un test unitaire. Pour suivre, forkez ce [dépôt](https://gitlab.com/ykyuen/gitlab-ci-demo) et consultez-le.

Dans le fichier de configuration YAML ci-dessus, nous avons défini 3 étapes. Chaque étape est simplement une tâche gulp définie dans `gulpfile.js`. N'importe qui pourrait exécuter la tâche localement tant qu'il a Node.js installé. Mais dans [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/), nous devons seulement mentionner quelle image Docker est nécessaire. Dans notre cas, il s'agit de node:6.11.2. De plus, cet attribut d'image pourrait être défini dans la définition de l'étape afin que vous puissiez utiliser différents outils pour chaque étape.

#### La définition des étapes

Examinons plus en détail la définition des étapes.

Les attributs `before_script` et `script` peuvent avoir plusieurs valeurs (tableau dans .yml). Et si l'exécution du script échoue, l'étape sera classée comme échouée.

#### Déclencher le pipeline

Il suffit de faire quelques modifications sur la branche master et vous pouvez trouver le pipeline en cours d'exécution sur la page `CI / CD -> Pipeline`.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rtj97p-NEzbJjOe2Lh3-8A.jpeg)
_L'historique du pipeline_

#### Voir l'étape en détail

Cliquez sur un pipeline spécifique et vous pouvez lire la sortie de la console de chaque étape. Cela est utile lorsque l'étape/tâche échoue.

![Image](https://cdn-media-1.freecodecamp.org/images/1*t_0-lH0Hi05sEBeK8XzDIg.jpeg)
_La sortie de l'étape_

### Les avantages de l'utilisation de GitLab CI avec Docker

Différents projets peuvent nécessiter différentes dépendances telles que Node.js, Ant, Maven. Dans le passé, en utilisant un outil comme [Jenkins](https://jenkins.io/), je devais m'assurer que tous ceux-ci étaient installés sur le serveur. En utilisant [Docker](https://www.docker.com/), le développeur peut référencer les dépendances disponibles sur [Docker Hub](https://hub.docker.com/) sans demander à l'administrateur du serveur de configurer de telles dépendances sur le serveur à chaque fois. En fait, Jenkins dispose également d'un plugin de pipeline et il pourrait fonctionner avec Docker pour servir exactement le même objectif. Mais un effort supplémentaire pour intégrer Jenkins avec le contrôle de version est nécessaire et comme je l'ai mentionné auparavant.

Bien que je préfère utiliser [GitLab CI](https://about.gitlab.com/features/gitlab-ci-cd/), cela ne signifie pas qu'il pourrait complètement remplacer [Jenkins](https://jenkins.io/). [Jenkins](https://jenkins.io/) offre une interface utilisateur configurable qui est pratique pour les non-développeurs tels que les QA pour exécuter certaines tâches comme les déploiements et les tests d'intégration.

### Choisir un outil adapté - Il n'a pas besoin d'être parfait

La clé n'est pas de choisir l'outil parfait. Au lieu de cela, il s'agit davantage des personnes qui l'utilisent. Donc, avant de chercher un nouvel outil, essayez d'identifier le problème que vous aimeriez résoudre en premier.

— Article initialement publié sur [Boatswain Blog](https://blog.boatswain.io/post/a-simple-gitlab-ci-example/).