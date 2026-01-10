---
title: Comment déployer une fonction AWS Lambda avec le Framework Serverless
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2023-09-18T23:52:30.000Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-aws-lambda-with-serverless
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/joshua-woroniecki-lzh3hPtJz9c-unsplash.jpg
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: serverless framework
  slug: serverless-framework
seo_title: Comment déployer une fonction AWS Lambda avec le Framework Serverless
seo_desc: 'Serverless computing has revolutionized the way developers build and deploy
  applications in the cloud. It takes away the complexities of server management,
  allowing developers to focus solely on writing code and delivering value to their
  users.

  In th...'
---

Le calcul serverless a révolutionné la manière dont les développeurs construisent et déploient des applications dans le cloud. Il élimine les complexités de la gestion des serveurs, permettant aux développeurs de se concentrer uniquement sur l'écriture de code et la livraison de valeur à leurs utilisateurs.

Dans le domaine du calcul serverless, AWS Lambda se distingue comme une plateforme de premier plan pour exécuter des fonctions serverless de manière scalable et rentable.

## Table des matières

* [Qu'est-ce que le Framework Serverless ?](#heading-questce-que-le-framework-serverless)
* [Objectif et portée du guide](#heading-objectif-et-portee-du-guide)
* [Prérequis](#heading-prerequis)
* [Comment configurer l'AWS CLI](#heading-comment-configurer-laws-cli)
* [Comment créer le rôle IAM](#heading-comment-creer-le-role-iam)
* [Comment créer un projet Serverless](#heading-comment-creer-un-projet-serverless)
* [Comment écrire la fonction Python](#heading-comment-ecrire-la-fonction-python)
* [Comment définir la configuration Serverless](#heading-comment-definir-la-configuration-serverless)
* [Comment déployer la fonction Python](#heading-comment-deployer-la-fonction-python)
* [Comment tester l'API](#heading-comment-tester-lapi)
* [Surveillance et journalisation](#heading-surveillance-et-journalisation)
* [Conclusion](#heading-conclusion)

## Qu'est-ce que le Framework Serverless ?

Le Framework Serverless est un outil puissant qui simplifie le déploiement et la gestion des applications serverless sur divers fournisseurs de cloud, y compris Amazon Web Services (AWS). Ce guide vise à vous guider à travers le processus d'utilisation du Framework Serverless pour déployer une simple fonction Python sur AWS Lambda, l'exposer via API Gateway, et la surveiller en utilisant AWS CloudWatch.

### Objectif et portée du guide

L'objectif de ce guide est de vous fournir un tutoriel étape par étape sur le déploiement d'une fonction Python serverless sur AWS en utilisant le Framework Serverless. Que vous soyez nouveau dans le calcul serverless ou que vous cherchiez à développer vos compétences, ce tutoriel est conçu pour vous aider avec les éléments suivants :

* Comment configurer les prérequis nécessaires, y compris la configuration du compte AWS.
* Comment créer un nouveau projet serverless en utilisant le Framework Serverless.
* Comment écrire une fonction Python qui sera déployée sur AWS Lambda.
* Comment définir la configuration serverless dans un fichier `serverless.yml`.
* Comment déployer la fonction Python et API Gateway.
* Comment tester l'API déployée en utilisant divers outils comme cURL ou Postman.
* Comment configurer la surveillance et la journalisation avec AWS CloudWatch.

À la fin de cet article, vous aurez une compréhension claire de la manière d'utiliser le Framework Serverless pour déployer et gérer des applications serverless sur AWS. 

Vous acquerrez également une expérience pratique dans le déploiement de fonctions serverless et leur exposition via un point de terminaison API, ouvrant la voie à la construction et à la mise à l'échelle d'applications serverless dans vos projets.

Maintenant, plongeons dans les prérequis nécessaires pour commencer ce tutoriel.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* [Un compte AWS](https://www.console.aws.amazon.com).
* [L'AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html) (Interface de Ligne de Commande).
* [Le Framework Serverless](https://www.serverless.com/framework/docs/getting-started/).

## Comment configurer l'AWS CLI

Vous devrez définir les informations d'identification AWS pour l'AWS CLI si vous ne l'avez pas déjà fait. Vous l'utiliserez avec le Framework Serverless pour déployer les ressources sur AWS. 

Vous pouvez créer le fichier d'informations d'identification AWS en entrant la commande suivante dans le terminal :

```bash
 cat <<EOF > ~/.aws/credentials
    [default]
    aws_access_key_id = <REPLACE_WITH_YOUR_SECRET_KEY>
    aws_secret_access_key = <REPLACE_WITH_YOUR_ACCESS_KEY> 
  EOF

  cat <<EOF > ~/.aws/config
    [default]
    region = eu-west-1
    output = json
  EOF
```

## Comment créer le rôle IAM

Le rôle IAM est également utilisé par le Framework Serverless pour déployer les ressources sur AWS. Entrez la commande suivante pour créer le rôle :

```bash
 aws iam create-role --role-name serverlessLabs --assume-role-policy-document '{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}'
```

Cette politique permet au rôle d'être utilisé par le service AWS Lambda.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/create-role-1.png)

Entrez la commande suivante pour attacher la politique **`AWSLambdaBasicExecutionRole`** au rôle :

```bash
aws iam attach-role-policy --role-name serverlessLabs --policy-arn arn:aws:iam::aws:policy/AWSLambda_FullAccess
```

Pour vérifier que le rôle a été créé avec succès, vous pouvez exécuter la commande suivante pour obtenir des informations sur le rôle IAM :

```bash
aws iam get-role --role-name serverlessLabs
```

Voici à quoi les informations devraient ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/role-aws-1.png)

## Comment créer un projet Serverless

Ce projet est une simple fonction Python qui est déployée sur AWS Lambda, API Gateway et CloudWatch en utilisant le Framework Serverless. 

La fonction est déclenchée par une requête HTTP GET et retourne une simple chaîne de caractères. La fonction est déployée dans la région eu-west-1.

Tout d'abord, installez le Framework Serverless en utilisant `npm` :

```bash
npm install -g serverless
```

Ensuite, créez un nouveau projet Framework Serverless en utilisant la commande `serverless` puis suivez les instructions :

```bash
serverless
```

Choisissez ensuite AWS Python Starter dans la liste des modèles. Donnez-lui le nom de votre choix – j'ai utilisé **serverless-lab**.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/serverless-template-1.png)

Après que la commande s'exécute avec succès, vous verrez les deux composants principaux créés : `serverless.yaml`, et `handler.py`.

## Comment écrire la fonction Python

Pour garder les choses organisées, créons un dossier nommé **functions**, et créons un fichier nommé `__init__.py` à l'intérieur. Vous pouvez faire cela en utilisant cette commande :

```bash
mkdir functions  touch functions/__init__.py
```

Créez votre première fonction en créant un fichier nommé `first_function.py` à l'intérieur du dossier **functions** :

```bash
touch functions/first_function.py
```

Ouvrez ensuite le fichier `first_function.py`, et collez le code Python suivant pour définir la fonction que vous allez déployer :

```python
def first_function(event, context):
  print("La première fonction a été invoquée !!")
  return {
    'statusCode': 200,
    'body': "Bonjour, le monde !.\n C'est la première fonction."
  }

```

Le code ci-dessus est une simple fonction Python qui retourne un objet JSON avec des valeurs de code de statut et de corps. Comme vous pouvez le voir, nous avons inséré les deux paramètres — `event` et `context` — requis par les fonctions selon la convention du Framework Serverless.

Ensuite, ouvrez le fichier `handler.py` et supprimez son contenu et collez le code Python suivant pour définir le gestionnaire qui sera invoqué lorsque la fonction est déclenchée :

```python
from functions.first_function import first_function
```

Le code ci-dessus expose la fonction que vous avez créée dans le fichier `first_function.py`. Nous avons importé la fonction et l'avons exposée au framework.

## Comment définir la configuration Serverless

Pour commencer avec la configuration, ouvrez le fichier `serverless.yaml` et supprimez tout son contenu et collez le code YAML suivant pour définir le microservice que vous allez déployer :

```yaml
service: serverless-lab

provider:
  name: aws
  runtime: python3.7
  lambdaHashingVersion: 20201221
  region: eu-west-1
  timeout: 10 # Vous définissez un délai d'expiration de 10 secondes pour les fonctions
  role: arn:aws:iam::155318317806:role/serverlessLabs # Entrez votre rôle Arn ici
  memorySize: 512

functions:
  first_function:
    handler: handler.first_function
    events:
    - http:
        path: first
        method: get    
```

Décomposons chaque section ligne par ligne :

```yaml
service: serverless-lab

```

`**service**` spécifie le nom de votre service Serverless ou projet. Dans ce cas, il est nommé "serverless-lab", qui sera utilisé comme nom de service lors du déploiement sur AWS.

```yaml
provider:
  name: aws
  runtime: python3.7
  lambdaHashingVersion: 20201221
  region: eu-west-1 # entrez votre région
  profile: personalCaesarAcc
  timeout: 10 # Vous définissez un délai d'expiration de 10 secondes pour les fonctions
  role: arn:aws:iam::155318317806:role/serverlessLabs # Entrez votre rôle Arn ici
  memorySize: 512

```

`**provider**` définit le fournisseur AWS pour votre service. Il spécifie divers paramètres de configuration pour les fonctions AWS Lambda et autres ressources AWS.

* `name: aws` spécifie que vous utilisez AWS comme fournisseur de cloud.
* `runtime: python3.7` définit le runtime pour les fonctions AWS Lambda à Python 3.7.
* `lambdaHashingVersion: 20201221` spécifie la version de hachage de la fonction Lambda. Il s'agit d'un paramètre interne AWS.
* `region: eu-west-1` spécifie la région AWS où votre service sera déployé. Vous pouvez remplacer "eu-west-1" par la région AWS souhaitée.
* `timeout: 10` définit un délai d'exécution de 10 secondes pour les fonctions AWS Lambda. Cela signifie que chaque fonction doit terminer son exécution dans les 10 secondes.
* `role: arn:aws:iam::155318317806:role/serverlessLabs` spécifie l'ARN du rôle AWS IAM que vos fonctions Lambda assumeront. Ce rôle définit les permissions que vos fonctions ont au sein des services AWS. Vous pouvez remplacer cela par l'ARN de votre rôle IAM souhaité.

```yaml
functions:
  first_function:
    handler: handler.first_function
    events:
    - http:
        path: first
        method: get

```

`**functions**` définit les fonctions AWS Lambda dans votre service.

* `first_function` désigne le nom de votre fonction AWS Lambda.
* `handler: handler.first_function` spécifie le point d'entrée pour cette fonction, qui est `handler.first_function` dans le module `handler`. Cela est généralement au format `<nom_du_module>.<nom_de_la_fonction>`.
* `events` spécifie les événements qui déclenchent la fonction.
* `- http` indique que la fonction est déclenchée par un événement HTTP (API Gateway).
* `path: first` spécifie le chemin du point de terminaison de l'API (`/first`) qui déclenche la fonction.
* `method: get` spécifie que cette fonction est déclenchée lorsqu'une requête HTTP GET est faite au chemin spécifié.

## Comment déployer la fonction Python

Vous pouvez utiliser la commande suivante pour déployer le microservice sur AWS :

```bash
serverless deploy
```

Après un certain temps, le déploiement sera terminé et vous pourrez voir des informations comme le point de terminaison, hébergé sur API Gateway, pour déclencher la fonction que vous venez de déployer.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/deploy-1.png)

Le framework a déployé la fonction sur AWS Lambda et, parce que vous avez attaché un déclencheur HTTP à celle-ci. Il a déployé une API sur API Gateway pour permettre à la fonction d'être accessible.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/function-on-aws-api-gateway-1.png)

## Comment tester l'API

À partir du déploiement, vous avez une seule fonction nommée `first_function`, et un seul point de terminaison HTTP GET. 

En utilisant le point de terminaison GET (le point de terminaison généré dans le terminal après le déploiement de la fonction) dans votre navigateur, vous pouvez appeler la fonction :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/url-test-2.png)

L'image ci-dessus montre la fonctionnalité créée dans la fonction déployée s'exécutant dans le navigateur.

## Surveillance et journalisation

Le groupe de journaux est automatiquement enregistré sur AWS CloudWatch car il y a une instruction print définie dans la fonction. Entrez la commande suivante pour accéder aux journaux de la fonction :

```bash
serverless logs -f first_function
```

AWS CloudWatch est le service de journalisation natif AWS qui vous permet de surveiller et d'accéder aux journaux de vos applications. Vous pouvez trouver des groupes de journaux, et vous pouvez également appliquer des expressions de filtre sur les journaux pour récupérer ceux dont vous avez besoin.

![Image](https://www.freecodecamp.org/news/content/images/2023/09/cloudwatch-1.png)

Vous pouvez supprimer le microservice et les ressources que vous venez de déployer en utilisant la commande `serverless remove`. 

Consultez [mon dépôt GitHub](https://github.com/Caesarsage/Devops-projects/tree/main/project-08) pour voir le code complet.

## Conclusion

Dans ce guide complet, nous avons exploré le monde puissant du calcul serverless et démontré comment exploiter ses capacités en utilisant le Framework Serverless et Amazon Web Services (AWS). 

Vous avez entrepris un voyage depuis la configuration de votre environnement de développement jusqu'au déploiement d'une simple fonction Python en tant qu'API soutenue par AWS Lambda, tout en acquérant des connaissances sur la surveillance et la journalisation avec AWS CloudWatch.

Ce guide sert de point de départ pour votre voyage serverless. À mesure que vous deviendrez plus compétent avec le Framework Serverless et AWS, vous serez en mesure de construire et de déployer des applications serverless sophistiquées qui s'adaptent dynamiquement et répondent aux exigences des architectures modernes et natives du cloud.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).