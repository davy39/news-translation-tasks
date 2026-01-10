---
title: 'Comment j''ai déployé mon bot Twitter #100DaysOfCloud sur AWS Fargate'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-07-13T02:31:55.000Z'
originalURL: https://freecodecamp.org/news/how-i-deployed-my-100daysofcloud-twitter-bot-on-aws-fargate
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c99c3740569d1a4ca2191.jpg
tags:
- name: 100DaysOfCloud
  slug: 100daysofcloud
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Docker
  slug: docker
seo_title: 'Comment j''ai déployé mon bot Twitter #100DaysOfCloud sur AWS Fargate'
seo_desc: 'By Johan Rin

  After passing my last certification, I asked myself how much time I spent studying
  cloud computing.

  https://twitter.com/johanrin/status/1276049320748425216

  More than 100 days!

  It also made me realize two things:


  There was no #100DaysOfC...'
---

Par Johan Rin

Après avoir passé ma dernière certification, je me suis demandé combien de temps j'avais passé à étudier le cloud computing.

%[https://twitter.com/johanrin/status/1276049320748425216]

Plus de 100 jours !

Cela m'a également fait réaliser deux choses :

1. Il n'y avait pas de défi #100DaysOfCloud
2. Nous avons maintenant assez de contenu pour créer ce défi

J'ai donc immédiatement contacté Alex Kallaway, le créateur de #100DaysOfCode, pour lui demander s'il était possible de créer #100DaysOfCloud basé sur son défi.

Et quelques jours plus tard, le défi #100DaysOfCloud était officiel :

%[https://twitter.com/johanrin/status/1276409322596155616]

Mais il manquait quelque chose.

Si vous avez déjà utilisé le hashtag #100DaysOfCode, vous savez que vos tweets vont être retweetés au moins trois fois par des bots Twitter.

Comme il n'y avait pas de bots pour le nouveau défi #100DaysOfCloud, j'ai décidé de résoudre ce problème.

Dans cet article, nous allons voir comment j'ai déployé mon bot Twitter et pourquoi j'ai choisi de le déployer sur AWS Fargate.

C'est parti !

## Prérequis

Si vous souhaitez suivre et exécuter les commandes ci-dessous, assurez-vous de :

* Avoir un [compte AWS avec une clé d'accès et une clé secrète](https://docs.aws.amazon.com/general/latest/gr/aws-sec-cred-types.html#access-keys-and-secret-access-keys)
* Avoir des [identifiants d'authentification de l'API Twitter](https://developer.twitter.com/)
* Installer [Docker](https://docs.docker.com/get-docker/) sur votre machine
* Cloner le dépôt depuis [https://github.com/johanrin/100-days-of-cloud-bot](https://github.com/johanrin/100-days-of-cloud-bot)

## Pourquoi AWS Fargate ?

Si vous regardez mon code, vous verrez que :

* Le code est écrit en Python et utilise le package tweepy
* Le bot est toujours en cours d'exécution (en utilisant une boucle `while`)
* Il y a un `Dockerfile` pour construire mon image

Je ne vais pas expliquer tout le code car cela dépasse le cadre de cet article. Mais j'ai mentionné toutes les sources que j'ai utilisées dans le dépôt GitHub.

Mon idée était de déployer l'image Docker dans un conteneur dans le cloud avec les contraintes suivantes :

1. Je ne veux pas dépenser beaucoup d'argent
2. Je ne veux pas gérer et exploiter des serveurs

Comme j'ai des crédits sur AWS, la première contrainte était facile — aller avec AWS.

En ce qui concerne la contrainte numéro 2, je savais grâce au [cours AWS Certified Developer - Associate](https://youtu.be/RrKRN9zRBWs), que nous pouvions déployer des conteneurs serverless avec AWS Fargate.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Screenshot_2020-07-08-AWS-Certified-Developer---Associate-2020--PASS-THE-EXAM---Ad-Free-Course.png)
_Extrait du cours AWS Certified Developer - Associate 2020_

Selon votre région, les prix des services AWS peuvent varier. Il s'agit souvent de quelques centimes, mais je prévoyais de faire fonctionner mon bot pendant au moins un an. Donc, chaque centime comptait.

Pour voir les prix d'AWS Fargate et minimiser vos coûts, vous pouvez [consulter la documentation AWS](https://aws.amazon.com/fargate/pricing/). J'ai trouvé que la région la moins chère près de chez moi était l'Irlande, alors j'ai décidé d'y déployer mon bot sur AWS Fargate.

## Comment j'ai déployé mon bot ?

Maintenant que j'ai expliqué pourquoi j'ai utilisé AWS Fargate, voyons comment j'ai déployé mon bot.

Il y a deux grandes étapes pour déployer une image Docker sur AWS Fargate :

1. Pousser l'image Docker vers Amazon Elastic Container Registry (ECR)
2. Déployer l'image Docker sur Fargate

Expliquons chaque étape en détail.

### Pousser l'image Docker vers Amazon Elastic Container Registry (ECR)

* Dans le répertoire racine, construisez votre image à partir du `Dockerfile`.

```bash
docker build . -t 100-days-of-cloud-bot
```

* Authentifiez votre Docker auprès d'Amazon ECR.

```bash
aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com
```

* Étiquetez votre image avec le dépôt Amazon ECR.

```bash
docker tag 100-days-of-cloud-bot aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot
```

* Poussez votre image vers Amazon ECR.

```bash
docker push aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot
```

### Déployer l'image Docker sur Amazon Fargate

* Ouvrez l'[assistant de première exécution de la console Amazon ECS](https://console.aws.amazon.com/ecs/home#/firstRun).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/01-Screenshot_2020-06-30-Amazon-ECS.png)

* Cliquez sur **Configurer** dans le conteneur personnalisé, complétez avec les paramètres suivants, puis sélectionnez **Mettre à jour**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image1.png)

| Propriété                                                                | Valeur                                                                                                                                                                              |
| ----------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Nom du conteneur**                                                      | container-100-days-of-cloud-bot                                                                                                                                                    |
| **Image**                                                               | aws_account_id.dkr.ecr.region.amazonaws.com/100-days-of-cloud-bot                                                                                                                  |
| **Limites de mémoire (MiB)**                                                 | Limite souple \| 512                                                                                                                                                                   |
| **Mappages de ports**                                                       | _Port du conteneur_ : 80<br />_Protocole_ : tcp                                                                                                                                          |
| **Unités CPU**                                                           | 256                                                                                                                                                                                |
| **Variables d'environnement**<br />(Identifiants d'authentification de l'API Twitter) | CONSUMER_KEY \| Valeur \| consumer_key<br />CONSUMER_SECRET \| Valeur \| consumer_secret<br />ACCESS_TOKEN \| Valeur \| access_token<br />ACCESS_TOKEN_SECRET \| Valeur \| access_token_secret |


* Cliquez sur **Modifier** dans la section **Définition de la tâche**, complétez avec les paramètres suivants, puis sélectionnez **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image1-1.png)

| Propriété                 | Valeur                                 |
| ------------------------ | ------------------------------------- |
| **Nom de la définition de la tâche** | task-definition-100-days-of-cloud-bot |
| **Mémoire de la tâche**          | 0,5 Go (512)                           |
| **CPU de la tâche**             | 0,25 vCPU (256)                       |


* Cliquez sur **Suivant**.
* Cliquez sur **Modifier** dans la section **Définir votre service**, complétez avec les paramètres suivants, puis sélectionnez **Enregistrer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/Image2.png)

| Propriété                    | Valeur                         |
| --------------------------- | ----------------------------- |
| **Nom du service**            | service-100-days-of-cloud-bot |
| **Nombre de tâches souhaitées** | 1                             |
| **Type d'équilibreur de charge**      | Aucun                          |

Nous n'avons pas besoin d'un équilibreur de charge ici en raison de la limite de taux de l'API Twitter. Même si nous augmentons le nombre de nos conteneurs, l'API Twitter nous enverra un message d'erreur 420 car le bot est limité en taux pour avoir fait trop de requêtes.

* Cliquez sur **Suivant**.
* Modifiez votre **Nom de cluster** avec cluster-100-days-of-cloud-bot.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/12-Screenshot_2020-06-30-Amazon-ECS.png)

* Cliquez sur **Suivant**.
* Passez en revue votre configuration et cliquez sur **Créer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/16-Screenshot_2020-06-30-Amazon-ECS.png)

C'est tout, le conteneur est déployé sur AWS Fargate !

## Conclusion

Vous avez déployé votre bot Twitter sur AWS Fargate en seulement quatre étapes.  

AWS Fargate est facile à utiliser, nous permettant de déployer des conteneurs sans gérer et exploiter des serveurs.

Ce cas d'utilisation était simple, mais nous pouvons faire beaucoup plus comme ajouter un équilibreur de charge ou définir plus de tâches. Je vous recommande de [consulter la documentation](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) pour plus de détails.

Comme cet article concernait le défi #100DaysOfCloud, je devrais mentionner que nous avons un [serveur Discord](https://discord.com/invite/c6Db8nY), alors n'hésitez pas à rejoindre la communauté et le défi ! Nous avons des personnes formidables du monde entier prêtes à vous aider à démarrer avec le Cloud.

C'est tout pour moi, j'espère que vous avez appris quelque chose ! Si vous avez des questions, [trouvez-moi sur Twitter](https://twitter.com/johanrin) et n'hésitez pas à me demander quoi que ce soit.