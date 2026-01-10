---
title: Comment déployer une application Node.js sur AWS
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2025-04-02T16:36:18.698Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nodejs-application-on-aws
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1743611764466/96a89440-1c72-4ac0-861d-0ea29aeb90bf.png
tags:
- name: AWS
  slug: aws
- name: Node.js
  slug: nodejs
- name: Caddy
  slug: caddy
seo_title: Comment déployer une application Node.js sur AWS
seo_desc: Cloud platforms and infrastructure allow you to easily deploy and host backend
  services and applications. In this article, you’ll learn how to run a Node.js/Express
  application away from the confines of your local personal computer to make it accessi...
---

Les plateformes cloud et les infrastructures vous permettent de déployer et d'héberger facilement des services et applications backend. Dans cet article, vous apprendrez à exécuter une application Node.js/Express en dehors des limites de votre ordinateur personnel local pour la rendre accessible mondialement sur le cloud. Nous utiliserons Amazon Web Services pour cela.

Mais avant de commencer, voici quelques prérequis pour ce tutoriel :

* Un compte AWS actif

* Des connaissances de base à intermédiaires de Node.js et Express

* Des connaissances des commandes Linux

Avec cela, commençons.

### Points clés à retenir

À la fin de ce guide, vous devriez être équipé de connaissances de base sur :

* AWS EC2 et autres médias d'hébergement

* Linux

* Réseautage

## Table des matières

1. [Introduction](#heading-introduction)

2. [Comment configurer AWS](#heading-comment-configurer-aws)

3. [Comment déployer l'application Node.js](#heading-comment-deployer-lapplication-nodejs)

4. [Qu'est-ce que Caddy ?](#heading-quest-ce-que-caddy)

5. [Configuration de Caddy](#heading-configuration-de-caddy)

6. [Informations supplémentaires](#heading-informations-supplementaires)

7. [Conclusion](#heading-conclusion)

## Introduction

Le déploiement d'applications backend sur le cloud est assez simple grâce à l'avènement des fournisseurs de services cloud publics comme AWS.

Vous pouvez héberger ces applications sur le cloud en utilisant plusieurs méthodes, selon la complexité et les cas d'utilisation de votre application.

Pour la plateforme AWS, vous pourriez déployer sur :

* **AWS EC2 (Elastic Cloud Compute)** : Cette option vous permet de déployer un serveur de système d'exploitation virtuel qui sert de colonne vertébrale sur laquelle l'application est hébergée. Il est adapté aux applications backend monolithiques complexes.

* **AWS Lambda** : Cela est couramment appelé AWS serverless qui permet une exécution rapide des fonctions lorsque nécessaire. Il ne nécessite pas d'heures de disponibilité constante. Cela est plus adapté aux fonctions backend simples avec des cas d'utilisation spécifiques.

Pour les besoins de ce tutoriel, nous allons explorer l'option AWS EC2 pour déployer une application Node.js. Nous allons également couvrir l'utilisation d'un proxy inverse dédié pour vous donner un accès facile à votre application déployée.

## Comment configurer AWS

Tout d'abord, je suppose que vous avez un compte AWS (niveau gratuit minimum). Si ce n'est pas le cas, veuillez [naviguer ici](https://portal.aws.amazon.com/billing/signup) et configurer votre compte.

Après vous être connecté avec succès, vous aurez accès à tous les différents produits AWS disponibles. Recherchez AWS EC2 dans la barre de recherche. Une fois que vous avez cliqué dessus, vous verrez le tableau de bord EC2.

![Tableau de bord EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697716239/8020771d-3941-490b-8468-36d82e5e8c24.png align="center")

Nous allons maintenant créer une nouvelle instance EC2.

Pour des raisons de coût et de simplicité, nous utiliserons les options de niveau gratuit mises à disposition par AWS. Tout d'abord, vous commencerez par créer un nom d'instance. Vous pouvez le définir selon votre préférence.

Ensuite, vous choisirez un système d'exploitation spécifique pour servir de système d'exploitation pour votre serveur virtuel. Dans ce tutoriel, j'opterai pour la distribution Linux Ubuntu.

![Images du système d'exploitation](https://cdn.hashnode.com/res/hashnode/image/upload/v1742826868559/a08cbc5c-e35f-4264-ab17-6746dfea74d8.png align="center")

Ensuite, vous choisirez un type d'instance de calcul compatible. AWS fournit un accès gratuit aux types *t2.micro* et *t3.micro*, ce qui suffira pour héberger votre application.

![Type d'instance EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697788341/b4462135-7657-4608-a339-3a18d7187db1.png align="center")

Cette partie vous permet de configurer `ssh` pour activer l'accès à distance à votre serveur. Dans mon cas, j'ai choisi de ne pas le faire puisque je prévois d'utiliser l'option de console de connexion EC2.

Après avoir complété les étapes ci-dessus, vous configurerez les paramètres réseau. C'est ici que vos connaissances en réseautage seront utiles.

Automatiquement, AWS crée et attribue un réseau cloud privé virtuel à votre instance EC2 sur le point d'être lancée. Vous pouvez le personnaliser pour répondre à vos besoins, mais pour ce tutoriel, nous utiliserons le VPC par défaut attribué. De plus, nous laisserons le sous-réseau et l'attribution automatique d'IP tels quels.

Pour les paramètres de pare-feu, il existe deux options : créer un groupe de sécurité ou utiliser un groupe de sécurité existant. Pour faciliter l'utilisation avec l'instance EC2 que vous allez créer, vous pouvez configurer le paramètre de pare-feu en créant un nouveau groupe de sécurité, en spécifiant les types de réseau et en restreignant l'adresse IP des utilisateurs tentant d'accéder à l'instance EC2 que vous allez créer. De plus, vous pouvez toujours utiliser l'une de vos configurations de pare-feu préformées dans l'option *"utiliser un groupe de sécurité existant"*.

Vous pouvez laisser les autres sections telles quelles, puis créer votre instance EC2.

Une fois que vous avez créé avec succès l'instance EC2, vous pouvez vous connecter à l'instance via les options fournies.

![Options de connexion EC2](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697864497/40b77502-7f7b-4f76-9e8d-fbabfe3d5755.png align="center")

Pour les besoins de ce tutoriel, vous utiliserez l'option de connexion à l'instance EC2 pour accéder à votre instance EC2. Une fois que vous avez cliqué sur le bouton, vous serez alors amené à la console Linux.

![Console Linux](https://cdn.hashnode.com/res/hashnode/image/upload/v1742826982246/5c4f67d6-11f1-4346-9c33-a3fbb969bbba.png align="center")

Pour commencer, vous mettrez immédiatement à jour les paquets de votre système d'exploitation en utilisant la commande `sudo`.

La commande `sudo apt update` permettra de faire cela. Avec vos paquets à jour, vous pouvez maintenant installer les paquets nécessaires pour alimenter votre application Node.js : le paquet d'installation de *Node.js* et les outils *npm* (gestionnaire de paquets node), respectivement.

Ensuite, installez-les en utilisant la commande `sudo apt install nodejs npm`.

Avec cela fait, vous avez tout prêt pour exécuter votre application.

### Comment déployer l'application Node.js

Nous utiliserons une application Node.js/Express simple dans ce tutoriel. Vous pouvez trouver le code source [ici](https://github.com/rat9615/simple-nodejs-app). À l'intérieur de votre console EC2, clonez le code source de l'application en utilisant la commande `git clone` [`https://github.com/rat9615/simple-nodejs-app`](https://github.com/rat9615/simple-nodejs-app).

![Cette image montre le processus de clonage du code de l'application en utilisant git](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697610337/b777176a-d97e-4289-bb43-002d4b80f88c.png align="center")

Après avoir clonné avec succès le projet de code, exécutez la commande `cd simple-nodejs-app` pour naviguer dans le répertoire du dossier de code. Maintenant, installez les diverses dépendances nécessaires de l'application qui sont incluses dans le fichier `package.json` du projet de code en exécutant `npm install` :

![Cette image montre l'installation de tous les paquets nécessaires pour exécuter l'application backend. La commande exécutée est npm install](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697545681/8c99ae1f-8d4e-4116-944d-5ce0d7613550.png align="center")

Après avoir complété les étapes ci-dessus, la commande `npm start` donnera vie à votre application. Vous devriez alors voir un message de succès sur votre écran.

Mais si vous naviguez vers l'adresse IP publique de l'instance EC2 avec le sous-port 3000 de l'adresse IP de l'instance, vous verrez toujours une erreur – alors qu'est-ce que nous n'avons pas complété ?

C'est ici que vos connaissances en réseautage interviennent à nouveau. Maintenant, naviguez de nouveau vers votre tableau de bord de calcul EC2 cloud et allez dans les groupes de sécurité. Ceux-ci contiennent et appliquent vos règles entrantes et sortantes.

Mais avant de continuer, qu'est-ce que les règles entrantes et sortantes ?

* **Les règles entrantes** vous permettent de configurer facilement l'accès à la ressource cloud via n'importe quelle route. Elles garantissent que seuls ceux qui sont expressément autorisés se voient accorder l'accès. Ces routes incluent, sans s'y limiter, SSH, HTTP, HTTPS et TCP.

* **Les règles sortantes** vous permettent de configurer facilement le flux d'informations des ressources cloud vers le monde extérieur. Seules les adresses de protocole Internet autorisées auront accès aux informations demandées.

Alors maintenant, vous allez créer une nouvelle règle entrante qui vous donnera accès au point de terminaison de l'API backend au port 3000 :

![Dans cette image, nous définissons les règles entrantes pertinentes pour notre machine](https://cdn.hashnode.com/res/hashnode/image/upload/v1743174093701/0d31d813-58cb-40d3-8559-71974aefaefd.png align="center")

En cliquant sur le bouton Ajouter une règle, vous pouvez ajouter de nouvelles routes d'accès réseau sur votre machine EC2. Les routes de trafic HTTP et TCP sont déjà configurées.

![Cela montre les différents ports et routes de réseau sur notre machine AWS](https://cdn.hashnode.com/res/hashnode/image/upload/v1743174075948/e0d6a6c9-3f7a-48bd-804b-083eb1d7514f.png align="center")

L'image ci-dessus met en évidence toutes les règles entrantes incluses dans une application de démonstration. Maintenant, revenons à la configuration de nos paramètres réseau.

Dans les groupes de sécurité de votre tableau de bord, cliquez sur le bouton **Ajouter une règle** à la fin de la page.

Sélectionnez le type de réseau TCP, définissez l'hôte sur `0.0.0.0.0/0`, et définissez le port sur le port 3000. Enfin, pour compléter la configuration de la demande d'adresse IP, cliquez simplement sur l'option "autoriser depuis n'importe où". Enregistrez la règle et actualisez votre onglet. En quelques minutes, le point de terminaison sera disponible sur le port 3000.

Pour voir l'application en action, cliquez sur l'adresse IP externe de l'instance EC2 et ajoutez un suffixe de port 3000 pour afficher l'interface de l'application backend. Et voilà, votre application devrait maintenant être en ligne.

Mais ce n'est pas tout – il est peu pratique d'inclure le numéro de sous-port lors de la navigation sur l'adresse IP. Vous aurez donc besoin d'un outil de proxy inverse efficace et compatible qui route toute information du port 3000 vers le port 80 (qui est un port général). Un proxy inverse dans ce scénario route et transfère les requêtes des clients vers un serveur servant d'intermédiaire protecteur. Pour cela, vous pouvez utiliser un outil appelé Caddy.

## Qu'est-ce que Caddy ?

Caddy est un outil flexible, convivial pour les débutants et open-source qui offre des fonctionnalités de proxy inverse, d'équilibrage de charge et de mise en cache en plus de son rôle de serveur web. Il dispose d'un guide utilisateur étendu et d'une documentation que vous pouvez consulter [ici](https://caddyserver.com/docs/).

Maintenant, configurons Caddy sur votre instance EC2.

## Configuration de Caddy

### Installer Caddy

Tout d'abord, vous devrez installer Caddy sur votre système d'exploitation Linux. Vous pouvez le faire en exécutant `sudo apt install caddy`.

![Processus d'installation de l'outil Caddy](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697469605/cf58d75f-ed72-4078-8e45-30b7da0916b1.png align="center")

Après avoir complété le processus d'installation, l'image ci-dessus devrait être ce que vous voyez sur votre écran. Une fois que vous avez fait cela, assurez-vous que Caddy est activé et allumé en exécutant cette commande :

`caddy run`

Après avoir exécuté la commande ci-dessus, l'outil Caddy devrait être activé et actif. Vous devriez alors voir l'image ci-dessous sur votre écran :

![État actuel de l'outil Caddy](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697342473/be0499f4-6a0f-406b-87d9-0688e56d8783.png align="center")

Ensuite, naviguez vers l'adresse IP externe disponible sur votre instance EC2. Là, affichée sur l'écran, devrait se trouver la page d'accueil de Caddy.

### Configurer Caddy

En revenant à votre console, vous devrez modifier le fichier de configuration de Caddy pour activer le proxy inverse du **port 3000** vers le port par défaut **80**.

Pour accéder au fichier de configuration, naviguez vers le fichier à partir du répertoire racine via la commande `cd /etc/caddy/Caddyfile`.

Vous pouvez ensuite utiliser la commande `sudo nano` pour ouvrir le fichier de configuration en édition. Le préfixe `sudo` vous donne des privilèges d'administrateur qui vous permettent d'apporter les modifications nécessaires au fichier de configuration.

![Fichier de configuration de Caddy](https://cdn.hashnode.com/res/hashnode/image/upload/v1742697233724/cf694df5-74bc-4975-b3e7-c0414fb68646.png align="center")

Dans la section du port 80 du fichier de configuration, ajoutez cette ligne de code :

`reverse_proxy :3000`

Enregistrez le fichier – et maintenant vous avez terminé. Vous pouvez redémarrer l'outil Caddy pour refléter les nouveaux paramètres en exécutant `sudo systemctl restart caddy`. L'actualisation de l'adresse IP affichera votre application Node.js alimentée. Avec cela, vous avez hébergé avec succès votre application Node.js sur EC2 et utilisé un outil de proxy inverse pour la rendre accessible.

![Page d'accueil du projet](https://cdn.hashnode.com/res/hashnode/image/upload/v1742827013554/f99be1e5-bfc6-444c-b620-9c47ae43dc3a.png align="center")

## Informations supplémentaires

À l'avenir, il est bon de pratiquer l'activation des fonctionnalités DNS avec la personnalisation du nom de domaine, car les utilisateurs ne se souviendront pas toujours de l'adresse IP. Vous pouvez également augmenter davantage votre expertise dans le déploiement d'applications backend en expérimentant l'alimentation des fonctions backend avec AWS Lambda.

## Conclusion

Avec cela, nous arrivons à la fin du tutoriel. J'espère que vous avez appris les opérations AWS et la configuration d'une application backend sur le cloud. Vous pouvez également me contacter sur mon blog et consulter mes autres articles [ici](http://portfolio-oluwatobi.netlify.app). Jusqu'à la prochaine fois, continuez à coder !