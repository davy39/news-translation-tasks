---
title: Qu'est-ce que l'orchestration de conteneurs ? Comment gérer vos conteneurs
  avec MicroK8s
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2022-09-12T14:57:00.000Z'
originalURL: https://freecodecamp.org/news/container-orchestration-for-beginners
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-pixabay-163726.jpg
tags:
- name: containerization
  slug: containerization
- name: containers
  slug: containers
- name: Kubernetes
  slug: kubernetes
seo_title: Qu'est-ce que l'orchestration de conteneurs ? Comment gérer vos conteneurs
  avec MicroK8s
seo_desc: 'Container orchestration has been called the next big thing in the world
  of technology. And it’s easy to see why.

  Container orchestration helps IT professionals and programmers maximize their applications’
  performance. It helps them ensure that multip...'
---

L'orchestration de conteneurs a été qualifiée de prochaine grande avancée dans le monde de la technologie. Et il est facile de comprendre pourquoi.

L'orchestration de conteneurs aide les professionnels de l'informatique et les programmeurs à maximiser les performances de leurs applications. Elle les aide à s'assurer que plusieurs conteneurs peuvent travailler ensemble pour gérer plus de tâches simultanément que ce qu'un seul conteneur pourrait gérer seul.

Mais comment fonctionne exactement l'orchestration de conteneurs ? Quels sont ses avantages et comment la mettre en œuvre ? Cet article répondra à toutes vos questions et plus encore.

## Prérequis

Pour comprendre l'orchestration de conteneurs, vous avez besoin de :

* Ubuntu 22.04 LTS, ou toute autre version.
* Une compréhension de base de ce que sont les conteneurs et de leur fonctionnement
* Une connexion internet stable
* Des permissions sudo

## Ce que vous allez apprendre

Si vous n'êtes pas familier avec l'orchestration de conteneurs, vous vous demandez peut-être pourquoi tant de bruit autour de cette technologie.

Dans ce tutoriel, nous passerons en revue les avantages de l'orchestration de conteneurs et comment l'appliquer dans votre organisation.

À la fin, vous comprendrez mieux pourquoi l'orchestration de conteneurs est si essentielle et comment elle peut aider votre entreprise à fonctionner plus efficacement.

## Qu'est-ce que l'orchestration de conteneurs ?

Si vous gérez une entreprise, il est probable que vous utilisiez des conteneurs pour exécuter vos applications. Mais qu'est-ce que l'orchestration de conteneurs, exactement ?

En bref, c'est une manière de gérer et d'automatiser le déploiement, la mise à l'échelle et la gestion des conteneurs.

## Les avantages de l'utilisation d'un orchestrateur de conteneurs

Il existe de nombreux avantages à utiliser un orchestrateur de conteneurs, notamment une efficacité accrue, une scalabilité et une portabilité.

Un orchestrateur de conteneurs peut également vous aider à gérer le cycle de vie de votre application, facilitant ainsi le déploiement et la mise à jour de vos applications. De plus, un orchestrateur de conteneurs peut vous aider à automatiser des tâches telles que la surveillance et la journalisation.

Avec un orchestrateur de conteneurs, vous pouvez définir les contraintes de ressources pour chacun de vos conteneurs. Par exemple, si vous avez besoin de plus de puissance CPU pour l'un de vos conteneurs que pour un autre, l'orchestrateur de conteneurs allouera les ressources en conséquence.

## Comment choisir votre plateforme d'orchestration de conteneurs

Il y a quelques éléments à considérer lors de la sélection d'une plateforme d'orchestration de conteneurs. Le premier est de savoir si vous souhaitez une solution auto-hébergée ou basée sur le cloud. Une solution basée sur le cloud peut être l'option idéale si vous débutez avec les conteneurs.

Un autre élément à considérer est les fonctionnalités dont vous avez besoin. Certaines plateformes offrent des outils de gestion plus complets que d'autres.

Enfin, réfléchissez à la facilité d'utilisation de la plateforme et à son intégration avec les autres outils que vous utilisez.

## Aperçu d'un exemple de stack

Dans une configuration typique d'orchestration de conteneurs, vous aurez plusieurs composants différents travaillant ensemble pour fournir une solution complète.

Par exemple, vous pourriez avoir :

* un registre de conteneurs, où vos images sont stockées
* un runtime de conteneurs, qui gère le cycle de vie de vos conteneurs
* et une plateforme d'orchestration de conteneurs, qui fournit la planification et la coordination pour vos conteneurs.

Certains cas d'utilisation nécessitant une approche orchestrée incluent l'intégration/deploiement continu (CI/CD) et le traitement par lots.

Un pipeline CI/CD est un système automatisé qui aide les développeurs à publier de nouvelles fonctionnalités en production à tout moment en réduisant les tâches manuelles comme les scripts de déploiement et la gestion de la configuration.

Une charge de travail de traitement par lots est celle où de nombreuses tâches intensives en calcul partagent des ressources pendant des périodes spécifiques, comme les week-ends ou après les heures de travail lorsque la demande est faible.

Une façon d'exécuter ces tâches serait avec une file d'attente, mais cette méthode ne s'adapte pas bien. Pour traiter plus de jobs en parallèle, vous avez besoin d'un planificateur capable de gérer des centaines ou des milliers de jobs simultanés.

Le traitement par lots a également des exigences strictes en matière de cohérence des données : il ne peut tolérer un degré élevé de variabilité dans les temps d'exécution entre les jobs individuels car il peut y avoir certaines dépendances entre eux.

Les algorithmes de planification qui peuvent réduire la variabilité des temps d'exécution en gérant intelligemment l'ordre dans lequel ils exécutent leurs jobs sont préférables ici.

## Comment planifier votre mise en œuvre

### Étape 1 – Décider de l'architecture

Maintenant que vous savez ce qu'est l'orchestration de conteneurs et pourquoi vous en avez besoin, il est temps de commencer à planifier votre mise en œuvre.

La première étape consiste à décider de l'architecture de votre système. Cela impliquera de décider du nombre de nœuds dont vous avez besoin, du type de stockage que chaque nœud utilisera et de la manière dont les nœuds seront interconnectés.

Une fois que vous avez une bonne compréhension de l'architecture souhaitée, vous pouvez commencer à examiner différentes solutions d'orchestration qui répondront à vos besoins.

Il existe deux méthodes courantes pour orchestrer vos conteneurs : l'orchestration basée sur un planificateur et l'orchestration basée sur les ressources.

Dans l'orchestration basée sur un planificateur, un planificateur externe décide quand et où les conteneurs doivent s'exécuter. Dans l'orchestration basée sur les ressources, l'allocation des ressources est effectuée en interne par l'orchestrateur en fonction de politiques préconfigurées.

Si vous souhaitez un contrôle accru sur le placement des conteneurs, alors l'orchestration basée sur un planificateur peut être meilleure pour vous. Si vous souhaitez moins de surcharge en ce qui concerne la configuration des ressources, alors l'orchestration basée sur les ressources peut être plus appropriée.

### Étape 2 – Préparation

À mesure que votre entreprise se développe, vous devrez considérer comment évoluer.

Une méthode consiste à utiliser l'orchestration de conteneurs. Cela vous permet de gérer et de déployer vos conteneurs plus efficacement. Vous pouvez même configurer une automatisation qui s'occupera automatiquement de la mise à l'échelle pour vous selon les besoins.

### Étape 3 – Mettre tout ensemble

Maintenant que vous connaissez les bases de l'orchestration de conteneurs et comment elle peut bénéficier à votre entreprise, il est temps de tout mettre ensemble. Voici les étapes que vous devrez suivre :

1. Définissez vos objectifs et vos buts. Que souhaitez-vous accomplir avec l'orchestration de conteneurs ?
2. Choisissez le bon outil pour le travail. Il existe divers outils d'orchestration de conteneurs, alors faites vos recherches pour trouver celui qui correspond le mieux à vos besoins.
3. Configurez votre environnement. La configuration de vos conteneurs peut être difficile si vous ne savez pas ce que vous faites. Assurez-vous de lire la documentation et de suivre les instructions avant de commencer.
4. Testons ! Essayez d'exécuter votre application avec un nouveau système d'orchestration avant de vous engager pleinement. La dernière chose que vous voulez est que quelque chose ne fonctionne pas ou ne se passe pas comme prévu une fois qu'il est déjà implémenté sur les serveurs de production. Heureusement, tester les choses au préalable vous aidera à minimiser les surprises à l'avenir.

Maintenant que vous connaissez les bases de l'orchestration de conteneurs à un niveau élevé, il est temps de commencer !

## Types de plateformes d'orchestration de conteneurs

Il existe trois principaux types de plateformes d'orchestration de conteneurs : Kubernetes, Docker Swarm et Apache Mesos. Chacune a ses avantages et ses inconvénients, il est donc crucial de choisir celle qui convient le mieux à vos besoins.

Par exemple, si vous êtes une startup ou une petite entreprise avec des ressources informatiques limitées, vous pourriez vouloir utiliser Docker Swarm. Il est conçu pour les équipes qui n'ont pas beaucoup d'administrateurs système.

Pour les grandes entreprises avec un personnel informatique plus expérimenté, Kubernetes est un bon choix car il est plus évolutif et offre un meilleur contrôle sur la manière dont les conteneurs sont déployés. Mais Kubernetes et Docker Swarm offrent tous deux une excellente évolutivité ainsi qu'un haut degré de convivialité.

Dans ce tutoriel, nous allons travailler avec Kubernetes. Kubernetes est un orchestrateur de conteneurs open source. En orchestrant vos conteneurs avec Kubernetes, vous pouvez automatiser de nombreuses tâches associées à leur gestion.

## Comment installer Kubernetes en tant que nœud unique

Une option pour commencer avec Kubernetes est de l'installer en tant que nœud unique. Cela peut être un excellent moyen d'apprendre les bases du système et de se faire une idée de son fonctionnement. De plus, c'est relativement simple à configurer.

Kubernetes est une plateforme ouverte qui vous permet de prendre de nombreuses décisions par vous-même, ce qui peut être vraiment utile.

Dans le tutoriel suivant, j'ai décidé d'utiliser :

* Ubuntu 22.04 LTS. Si vous utilisez un autre système d'exploitation, vous pouvez en apprendre plus [ici](https://kubernetes.io/docs/home/).
* MicroK8s. À partir d'un seul nœud, MicroK8s crée un cluster Kubernetes certifié en quelques minutes seulement. La distribution MicroK8s Kubernetes de Canonical est petite, polyvalente et portable.

### Étape 1 : Utilisez le package snap pour installer MicroK8s.

MicroK8s est distribué sous forme de snap, ce qui nécessite l'installation de snapd. Cela est déjà inclus dans la version la plus récente d'Ubuntu.

Tapez la commande suivante pour obtenir la version la plus récente de MicroK8s :

```bash
sudo snap install microk8s --classic
```

Après avoir exécuté la commande ci-dessus, le téléchargement de MicroK8s commencera comme montré dans l'image ci-dessous.

![Image](https://lh4.googleusercontent.com/UVy9niChsvxmgf_NYAB7km-QaP6b8zOZpzhPqrxQaUIMrKQJVb1EjIjyVAdFnz1-4Ym_Ps3U57Gm5iviWjNlIDwpUN_2Fok0odBJ_QAjBniCqe9PcoopG1EKrbCMGug5VI_foyqWplCjqJD6NXwuzazp_GLZ8UV8Nhkrz_yIPI__tdXVJnlAZt_Nuw)

### Étape 2 : Sur votre système Ubuntu, listez les différentes versions de MicroK8s.

Vous pouvez utiliser la commande snap ci-dessous pour voir toutes les versions possibles de microk8s.

```bash
snap info microk8s
```

Lorsque vous exécutez la commande ci-dessus, vous devriez obtenir la sortie visible dans l'image ci-dessous :

![Image](https://lh5.googleusercontent.com/CSt0TpWVz5w3Fm2nXtAHKSiXtHWdiz9K1tLJaFc3paBgp_EB_aiJluPDWJdOgMOf3TdnkemMIkOhXoL1rSP-klvo7xGB5GJSfPYC6vTMTrdyJEM86G3f91YAfePsW1PwQLb2HBKVFIyyDRszjxj0mp4FdPfTTODZ9slh9xeTRMTgIVt8YfZiCkWNkw)

### Étape 3 : Vérifiez que MicroK8s a été installé.

Vous pouvez vérifier l'état de MicroK8s en utilisant une commande existante dans Ubuntu. Pour ce faire, entrez la commande suivante dans votre terminal.

```bash
sudo microk8s status --wait-ready
```

Notez que pour attendre que les services Kubernetes démarrent, vous devez utiliser le paramètre "--wait-ready" pendant l'installation.

Après avoir exécuté la commande, vous obtiendrez la sortie suivante :

![Image](https://lh5.googleusercontent.com/UGEjgMIJCeT5DdI8rzNgg1uq6fKruooYsrtX70b9dOwA09AIzLHNfTdn939HDFLOO40pliraXPjmEpUHwgmnLHwvGnCvbdI7_kd9I74A0o3ZF0dllsuUTlb8VlbfrHt_xBc5aXJxJaTsaUBcJiCsWC5KWui-sBo9KBPPNZeCX1W8NT5UnyGU8wtVAA)

### Étape 4 : Se connecter à Kubernetes

L'étape la plus cruciale est maintenant d'obtenir l'accès à Kubernetes. MicroK8s offre sa propre version de kubectl pour interagir avec Kubernetes. Il est capable d'exécuter des commandes qui suivent et contrôlent votre cluster Kubernetes.

Entrez la commande suivante dans le terminal pour voir votre nœud actuel.

```bash
sudo microk8s kubectl get nodes
```

Après avoir exécuté la commande ci-dessus, vous obtiendrez la sortie suivante. Comme vous pouvez le voir, le statut est "Ready". En utilisant cette commande, vous pouvez également voir le nom du nœud, ses rôles, son âge et sa version.

![Image](https://lh6.googleusercontent.com/3x_1XVpFrAMNmifEuN1qUHYPsphakd_73WyW-FkAIfKeNnlfPaHctS3WqyQnUponS3yrk4PuO45cnBc-H0coKMJ_TXodapUsanWgZ6FakcoPbXga1eCFy7XOdlCZcgaASPiZz9_ogSQMYjKKK3tKzpZrkRVRFdFNlTX8D7zbRyCCyVH3xSvB_mD7GA)

### Étape 5 : Examiner les services en cours d'exécution

Si vous souhaitez voir quels services MicroK8s sont actuellement en cours d'exécution, utilisez la commande suivante :

```bash
sudo microk8s kubectl get services
```

Cette commande affiche le nom, le type, l'IP du cluster, l'IP externe, le(s) port(s) et l'âge des services actuellement en cours d'exécution.

![Image](https://lh6.googleusercontent.com/XhlBLlIvb6SDUbc9TTGe9JFLJu02k6QbEwIwklatTQ1dqhRp7SkKcXTDuWS6ouhwV3OSfLfUEresQId9Ht3h_bgBu-BmbhYqbyRabtNxzo6gOeAq_iNaH0XFoKtt2zEuT4y60YlLWqxt06ysusCDj8-EwRe2ZthyRuOTXVMxn6MCr6p31CVPysDAQw)

### Étape 6 : Déployer l'application avec MicroK8s.

Dans l'exemple suivant, nous utilisons kubectl pour déployer une application NGINX. Pour déployer NGINX avec succès, entrez la commande suivante :

```bash
sudo microk8s kubectl create deployment nginx --image=nginx
```

Comme vous pouvez le voir dans l'image ci-dessous, l'application a été déployée :

![Image](https://lh6.googleusercontent.com/dAXljEprBhHjUpTd89cYZNgMllC19xMBV-wlBBUNSBGOsatHOWuWaZ1NScWoMRmcVmKKEhfeF397NUJ016MWfRHjyiAfr5PiyuUS1AAB91pmUAxaAV9lNsA4Olr_u5o28k6MGrsWQGkiLib-uZcFcxhX4DJ3viVsD9Iw-VTb_K220gUowJQRh5gisg)

Vous pouvez utiliser la même commande pour déployer toute autre application.

Assurez-vous de remplacer `Nginx` par le nom de votre application préférée, comme montré dans l'image ci-dessous.

![Image](https://lh4.googleusercontent.com/hbSgEc3qSZl74Sb1lY-NxuUrwRNuRcA-q--HR4x9rXGjO1RkprpQhRkihh7uvXVnqkvcLXkOwAFeZfhoCtWQRu9QtO-UOnNUBcqnwJGwsTyoLJD0nI9CeygGX5TRT0g8oQhq7iXoWjarb9EA6ipltCeHR9LSApOmw0w476sh3vvTfqi7ZgsyZU70lA)

## Conclusion

Si vous cherchez un moyen d'améliorer l'efficacité et le déploiement de votre application, l'orchestration de conteneurs est une excellente solution.

En utilisant des conteneurs, vous pouvez regrouper tous les composants nécessaires de votre application en une seule unité facilement déployable.

De plus, en utilisant un outil d'orchestration de conteneurs comme Kubernetes, vous pouvez automatiser l'ensemble du processus. Vous n'avez pas à vous soucier de configurer manuellement quoi que ce soit ; il suffit d'écrire du code, de le mettre dans un conteneur et de le déployer.

Avec ce type d'automatisation, les choses ne vont que s'améliorer.