---
title: Comment utiliser Google Cloud Tasks dans Laravel PHP
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-22T11:10:14.000Z'
originalURL: https://freecodecamp.org/news/using-google-cloud-tasks-in-laravel-php-24985db107b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*pGJLCV_d77eyLshIDIVCdQ.png
tags:
- name: google app engine
  slug: google-app-engine
- name: Google Cloud Platform
  slug: google-cloud-platform
- name: Laravel
  slug: laravel
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment utiliser Google Cloud Tasks dans Laravel PHP
seo_desc: 'By Errol Fernandes

  Deploying a Laravel application on Google App Engine is a fairly easy task thanks
  to the documentation available. But setting up asynchronous task processing (Laravel
  Eventing) on Google Cloud effectively is not that simple.

  One of...'
---

Par Errol Fernandes

Déployer une application Laravel sur Google App Engine est une tâche relativement facile grâce à la documentation disponible. Mais configurer le traitement asynchrone des tâches (Laravel Eventing) sur Google Cloud de manière efficace n'est pas si simple.

L'une des façons de procéder est d'utiliser le fichier supervisord.conf pour configurer la commande Laravel `queue:listen`. Mais cela n'est disponible que pour l'environnement Google App Engine Flexible. Donc, si vous avez besoin d'une solution pour l'environnement Google App Engine Standard, vous devez utiliser Google Cloud Tasks pour traiter les jobs asynchrones.

Google Cloud Tasks est un service entièrement géré qui vous permet de gérer l'exécution, la distribution et la livraison d'un grand nombre de tâches distribuées. Avec Cloud Tasks, vous pouvez effectuer des travaux de manière asynchrone en dehors d'une requête utilisateur ou service-à-service.

**Étape 1 :**

Créez une file d'attente de tâches pour gérer les tâches. Ici, nous utilisons le fichier queue.yaml pour spécifier la configuration de la file d'attente à créer dans Google Cloud. Le paramètre target contient le nom de l'application déployée sur App Engine.

![Image](https://cdn-media-1.freecodecamp.org/images/cqgEZ5IU7zeQ-NiFA60HC4AHlIbvjJyzcVn1)

**Étape 2 :**

Déployez le fichier queue.yaml dans Google Cloud en utilisant la commande `gcloud app deploy queue.yaml`. L'image ci-dessous montre une file d'attente Google Task créée dans Google Cloud.

![Image](https://cdn-media-1.freecodecamp.org/images/pLbVCTFBu-PMu1MOQrKXJqlczqPonw2d456T)

**Étape 3 :**

Nous devons passer la route de l'API et l'objet payload pour la tâche. Dans l'exemple ci-dessous, nous allons passer les données requises à une fonction `initTask()` :

![Image](https://cdn-media-1.freecodecamp.org/images/Bu9p27rXvAA4sHalnZHVrvgSrkMaWXSH6SAQ)

**Étape 4 :**

Créez la fonction initTask() :

![Image](https://cdn-media-1.freecodecamp.org/images/9oBdKkfhFjJbbCEB0nuSBr9w3yOp89N1zfIH)

Nous passons l'userID de l'utilisateur actuel dans le payload pour des raisons d'authentification. Maintenant que le payload est prêt, nous passons tous les détails requis à la fonction de construction de la tâche.

**Étape 5 :**

Créez la méthode create_task(). Cette méthode utilisera l'API Google pour construire une Cloud Task et la passer à la file d'attente des tâches. Le fichier gAppCreds.json est le compte de service Google créé pour définir les rôles de l'application.

![Image](https://cdn-media-1.freecodecamp.org/images/VCBtOQ8jdrE-Xp9bVZP8Ec9jkZJkjbRmVDi5)

**Étape 6 :**

Maintenant, nous créons les routes API en utilisant le RouteServiceProvider dans api.php :

![Image](https://cdn-media-1.freecodecamp.org/images/3ELikvkitL6Oyv9u-jB-7IkdEck1xM-3o3xL)

**Étape 7 :**

Maintenant, nous créons un TaskController qui routera les différentes API vers la fonction spécifique. Donc, dans l'exemple ci-dessous, nous créons une fonction `associateApp()` :

![Image](https://cdn-media-1.freecodecamp.org/images/N9zDssAevMKOPAljdNo6Kk9rD7xV1oHhOU6-)

Dans la fonction ci-dessus, nous décodons le payload que nous avons envoyé dans **Étape 4** et le passons à l'événement respectif pour traitement. L'userID que nous avons passé dans **Étape 4** est utilisé pour valider l'authenticité de la requête API entrante.

#### Verdict final :

Normalement dans Laravel, nous appelons l'événement directement depuis le contrôleur respectif. Mais pour utiliser Google Cloud Tasks, nous créons une API de tâche qui appelle à son tour la route qui appelle à son tour l'événement pour traiter nos données. En bref, nous créons plusieurs API pour nos événements et jobs Laravel qui sont ensuite appelés (**par l'API Google Task**) en fonction de la route que vous passez dans **Étape 3** et **Étape 6**.

Puisque j'utilise Google Cloud Tasks, je n'ai pas à me soucier du supervisord ou de la gestion des jobs dans la table de la file d'attente, car tout est géré par la file d'attente Google Task. Tout ce que j'ai à faire est de surveiller la file d'attente des tâches s'il y a une tâche échouée.

En utilisant l'API Google Cloud, je peux créer plusieurs files d'attente pour différentes applications cibles que je déploie sur Google App Engine, que l'environnement soit Standard ou Flexible.