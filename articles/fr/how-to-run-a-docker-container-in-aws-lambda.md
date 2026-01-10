---
title: Comment exécuter un conteneur Docker dans AWS Lambda
author: Agnes Olorundare
date: '2025-12-24T23:38:56.938Z'
originalURL: https://freecodecamp.org/news/how-to-run-a-docker-container-in-aws-lambda
description: Bien que les conteneurs soient assez légers et offrent divers avantages,
  il peut être difficile de décider de la meilleure façon de les déployer. Il existe
  de nombreuses façons de déployer et d'exécuter des conteneurs Docker. Mais certaines
  sont plus adaptées à l'orchestration et à la gestion de conteneurs...
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1766599506861/86c07e37-7838-4186-971e-29722ccec785.png
tags:
- name: AWS
  slug: aws
- name: serverless
  slug: serverless
- name: lambda
  slug: lambda
- name: Docker
  slug: docker
- name: containerization
  slug: containerization
- name: ecr
  slug: ecr
seo_desc: While containers are quite lightweight and provide various benefits, it
  can be challenging to decide how best to deploy them. There are a number of ways
  to deploy and run Docker containers. But some are best for orchestrating and managing
  containers,...
---


Bien que les conteneurs soient assez légers et offrent divers avantages, il peut être difficile de décider de la meilleure façon de les déployer. Il existe de nombreuses façons de déployer et d'exécuter des conteneurs Docker. Mais certaines sont plus adaptées à l'orchestration et à la gestion de conteneurs, et peuvent ne pas convenir à un cas d'utilisation simple consistant à n'exécuter qu'un seul conteneur.

Dans cet article, je vais vous apprendre comment déployer un seul conteneur Docker en utilisant un service serverless sur AWS appelé Lambda.

## Table des matières

* [Prérequis / Exigences](#heading-prerequis-exigences)
    
* [Le Serverless avec AWS Lambda](#heading-le-serverless-avec-aws-lambda)
    
* [Comment construire, exécuter et tester un conteneur localement](#heading-comment-construire-executer-et-tester-un-conteneur-localement)
    
* [Comment pousser votre image vers Amazon Elastic Container Registry (ECR)](#heading-comment-pousser-votre-image-vers-amazon-elastic-container-registry-ecr)
    
* [Comment déployer votre image Docker vers Lambda](#heading-comment-deployer-votre-image-docker-vers-lambda)
    
* [Nettoyage](#heading-nettoyage)
    
* [Conclusion](#heading-conclusion)
    

## Prérequis / Exigences

Les outils et compétences suivants sont nécessaires pour suivre ce tutoriel :

* Connaissance de Docker, et avoir Docker installé localement.
    
* Un compte AWS avec des identifiants disposant de privilèges administratifs pour effectuer des appels API via la CLI. La bonne pratique serait de limiter les privilèges exactement à ce qui doit être fait.
    
* AWS CLI installé localement.
    
* Des gestionnaires d'environnements virtuels Python [tels que uv](https://github.com/astral-sh/uv) (optionnel).
    

## Le Serverless avec AWS Lambda

Les conteneurs offrent une manière légère, cohérente et économe en ressources d'exécuter des applications. Le serverless élimine la surcharge liée à la gestion des infrastructures sous-jacentes sur lesquelles le conteneur s'exécute. Ainsi, comme vous pouvez commencer à le voir, la combinaison de ces outils vous aide à déployer des applications d'une manière qui vous permet de vous concentrer sur la logique métier, la performance et ce qui donne à votre produit un avantage concurrentiel.

Un outil AWS qui vous permet de passer au serverless est Lambda. Avec Lambda, vous n'êtes facturé que pour le nombre de fois où le code de la fonction s'exécute, la mémoire que vous avez sélectionnée au moment du provisionnement du service, et la durée de chaque invocation de la fonction.

En plus de supprimer la surcharge opérationnelle, Lambda peut également vous aider à économiser de l'argent puisque vous n'aurez pas à gérer des ressources inactives. La fonction ne s'active que lorsqu'elle est déclenchée par une requête qui lui est envoyée.

## Comment construire, exécuter et tester un conteneur localement

Docker est un outil qui vous aide à packager des applications ou des logiciels dans des unités portables, standardisées et partageables qui contiennent tout ce dont les applications ont besoin, comme les bibliothèques, le runtime, les outils système et le code de l'application, afin de s'exécuter. Ces unités sont appelées conteneurs.

Dans cette section, je vais vous guider à travers la construction de l'image Docker, l'exécution du conteneur et son test une fois qu'il est lancé.

Vous pouvez trouver le projet que vous utiliserez ici dans ce [dépôt GitHub](https://github.com/Agnes4Him/freecodecamp-lambda-docker).

### Construire l'image Docker

Pour exécuter un conteneur Docker, vous devez d'abord construire une image. L'image devient le modèle ou la `class` à partir de laquelle vous créez le conteneur ou l' `instance of the class`.

Vous pouvez trouver le code pour construire une image dans `lambda_function.py`.

```python
# lambda_function.py

def lambda_handler(event, context):
    name = event["name"]
    message = f"Hello, {name}!"

    try:
        return {
            "statusCode": 200,
            "body": message
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": {"error": str(e)}
        }
```

Comme vous pouvez le voir dans le code ci-dessus, il s'agit d'une application Python très basique qui attend une requête HTTP `POST`, avec un payload JSON contenant la clé – `name` – et une valeur correspondante. Le code renvoie ensuite une salutation contenant le nom qu'il a reçu. L'application n'a qu'une seule fonction, qui sert également de point d'entrée (entry point).

Pour construire une image Docker, vous aurez besoin d'un Dockerfile pour fournir le plan de l'image. Pour ce cas spécifique, le Dockerfile que vous utiliserez est également très basique. Chaque ligne d'un Dockerfile est appelée une `Directive`, et celle-ci fournit l'instruction que Docker doit suivre lors de la création d'une image. Ainsi, construire une image Docker signifie créer un modèle pour un conteneur en suivant les instructions ou directives du Dockerfile.

```plaintext
# Dockerfile

FROM public.ecr.aws/lambda/python:3.12

# Copy function code... LAMBDA_TASK_ROOT is /var/task, the working directory set in the base image
COPY lambda_function.py ${LAMBDA_TASK_ROOT}    

# Set the CMD to your handler - lambda_handler
CMD ["lambda_function.lambda_handler"]  
```

Un Dockerfile commence généralement par une image de base. Pour déployer une application en tant que conteneur Docker dans AWS Lambda, l'image de base doit être d'un type spécifique, selon le runtime de l'application. Dans ce cas, vous aurez besoin du runtime Python, donc l'image de base est `public.ecr.aws/lambda/python:3.12`. Il est possible d'utiliser une version différente de Python.

La directive suivante dans le Dockerfile consiste à copier le fichier `lambda_function.py` vers un chemin spécifique dans l'image de base. Ce chemin est référencé à l'aide d'une variable d'environnement qui a déjà été définie dans l'image de base et pointe vers `/var/task`. C'est le répertoire à partir duquel votre code s'exécutera.

La dernière directive est simplement une commande pour démarrer l'application lorsque le conteneur s'exécute.

Maintenant, vous pouvez lancer la commande de build depuis le répertoire racine du projet :

```bash
docker build -t <IMAGE_NAME>:<iIMAGE_TAG> .
```

![Exécution de la commande docker build sur le terminal](https://cdn.hashnode.com/res/hashnode/image/upload/v1766415846066/f128b7fc-f3a0-4770-b361-3f27c36a6ec4.png align="center")

![Sortie de la commande docker images montrant une liste de toutes les images existantes](https://cdn.hashnode.com/res/hashnode/image/upload/v1766415895836/d4653144-51b2-437d-8d73-4aaa42651206.png align="center")

### Exécuter le conteneur Docker

Ensuite, créons un conteneur en cours d'exécution à partir de cette image.

```bash
docker run -it --rm -p 8080:8080  lambda_docker:1.0.0
```

La commande ci-dessus créera un conteneur et l'exécutera en mode interactif juste pour que vous puissiez voir les logs générés par l'application dans le conteneur. Le port 8080 est également exposé sur l'hôte où le conteneur s'exécute et mappé au port du conteneur, qui est également 8080 (défini par AWS). Le conteneur est automatiquement supprimé une fois que vous arrêtez le processus en cours avec CTRL + C.

![Affichage de la commande docker run en mode interactif](https://cdn.hashnode.com/res/hashnode/image/upload/v1766416250857/62584a3c-bf5e-4cd9-b8d5-fc6734c50075.png align="center")

### Tester le conteneur en cours d'exécution

Maintenant, confirmez que l'application s'exécutant dans le conteneur peut recevoir et traiter des requêtes. Pour ce faire, utilisez le code dans le fichier `test.py` :

```python
# test.py

import requests

url = "http://localhost:8080/2015-03-31/functions/function/invocations"

data = {
    "name": "Janet"
}

response = requests.post(url, json=data)

print("Status Code:", response.status_code)
print("Response Body:", response.json())
```

Vous pouvez utiliser la bibliothèque Python `requests` pour effectuer cet appel. Installez la bibliothèque en utilisant un environnement virtuel pour isoler l'application de votre système global. Cela aide à prévenir les problèmes de conflits entre les versions des bibliothèques que vous installez pour une application.

Si vous utilisez uv pour gérer votre environnement virtuel, exécutez simplement la commande :

```python
uv add requests
```

Ensuite, exécutez le code dans `test.py` depuis l'environnement virtuel :

```python
uv run python3 test.py
```

![Test du bon fonctionnement du conteneur docker en exécutant le fichier test.py](https://cdn.hashnode.com/res/hashnode/image/upload/v1766419713310/1ebc3435-3826-46fb-93f3-4218c367e280.png align="center")

Vous devriez voir la réponse souhaitée sur le terminal.

![Logs du conteneur Docker en temps réel](https://cdn.hashnode.com/res/hashnode/image/upload/v1766419866358/8f0c2867-64c6-4b16-a5a7-5a0eedf9470f.png align="center")

## Comment pousser votre image vers Amazon Elastic Container Registry (ECR)

Maintenant que vous avez une image Docker fonctionnelle à déployer sur Lambda, l'étape suivante consiste à pousser l'image vers un registre Docker. Pour ce cas d'utilisation, votre image doit être poussée vers Amazon ECR, un registre de conteneurs pour stocker des images Docker.

Pour pousser votre image Docker, vous devez d'abord tagger l'image, ce qui signifie simplement nommer l'image d'une manière spécifique.

Actuellement, le tag de cette image est `lambda-docker:1.0.0`. Pour la tagger à la manière AWS, créez d'abord un dépôt (repository) ECR. Utilisons l'AWS CLI pour cela (cela nécessite de configurer les identifiants AWS localement en exécutant la commande `aws configure` et en fournissant vos identifiants).

### Configuration des variables d'environnement

```bash
# Set AWS profile
export AWS_PROFILE=<PROFILE_NAME>
```

```bash
# Set other variables

AWS_REGION=<AWS_REGION>
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
REPO_NAME=lambda-docker
TAG=1.0.0
```

Les commandes ci-dessus définissent le `AWS_PROFILE` pour que la CLI cible le bon compte AWS pour les appels API. Les autres variables spécifient la région, l'ID du compte, ainsi que le nom et le tag du dépôt ECR.

### Créer le dépôt ECR et s'authentifier

Maintenant, créez le dépôt ECR :

```bash
aws ecr create-repository \
  --repository-name "$REPO_NAME" \
  --region "$AWS_REGION"
```

Authentifiez-vous auprès d'Amazon ECR :

```bash
aws ecr get-login-password --region "$AWS_REGION" \
  | docker login \
  --username AWS \
  --password-stdin "$ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com"
```

### Tagger et pousser l'image Docker

Maintenant, taggez l'image Docker :

```bash
docker tag $REPO_NAME:$TAG \
  $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$TAG
```

Poussez l'image vers le dépôt ECR que vous avez créé :

```bash
docker push $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/$REPO_NAME:$TAG
```

Et voilà ! Votre image est maintenant dans ECR.

![Image d'Amazon ECR montrant le dépôt créé précédemment](https://cdn.hashnode.com/res/hashnode/image/upload/v1766420761622/5a18e41b-be41-4660-8d6c-59b12aebb4de.jpeg align="center")

![Image de l'image docker poussée vers le dépôt ECR existant](https://cdn.hashnode.com/res/hashnode/image/upload/v1766420810814/9f65af4b-a509-45e3-be8f-0bed08cfe6b2.png align="center")

## Comment déployer votre image Docker vers Lambda

Avec votre image maintenant dans ECR, vous pouvez créer une fonction Lambda. Naviguez vers la console Lambda et cliquez sur `Create a Function`.

### Créer la fonction Lambda

![Console AWS Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421062231/19bae74d-a6d5-4e73-8cca-102be40be214.png align="center")

Sélectionnez `Container Image` et recherchez le dépôt ECR que vous avez créé.

![Sélectionner le dépôt ECR pour créer une fonction Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421207358/25ae6eb2-1b1b-43c7-86dc-6dcd512ddc81.jpeg align="center")

Ensuite, sélectionnez l'image :

![Sélectionner l'image Docker existante depuis ECR](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421335963/ab7d9103-0ea6-4e25-be8c-139344acb5c5.png align="center")

Laissez les autres configurations par défaut et cliquez sur créer.

![Cliquer sur le bouton Create pour créer une fonction Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421506518/2f6e631a-a0c7-4f20-966f-2ef87f91bfb7.jpeg align="center")

Naviguez vers la fonction après sa création.

![Le tableau de bord / aperçu de la fonction Lambda nouvellement créée](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421673261/71c60ac4-35e7-4458-b4a7-1be2440b9e16.jpeg align="center")

### Tester le déploiement

Maintenant, testons le déploiement. Pour cela, utilisez simplement l'onglet `Test` existant de Lambda. Fournissez tous les détails nécessaires, y compris le payload pour votre requête `POST`.

![Créer une nouvelle instance de test pour tester la fonction Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421769909/008473e4-bb28-4fdd-8c5b-7e1f3489a3a0.png align="center")

![Le résultat du test de la fonction Lambda](https://cdn.hashnode.com/res/hashnode/image/upload/v1766421889043/86f6dbe6-be94-4dca-973e-9e7b68064ff3.png align="center")

Et c'est tout. Vous avez déployé avec succès un conteneur Docker sur AWS en tirant parti d'ECR et de Lambda. Vous pouvez aller plus loin en intégrant API Gateway et en rendant la fonction accessible depuis Internet.

## Nettoyage

N'oubliez pas de supprimer les services que vous avez créés sur votre dépôt AWS ECR et votre fonction Lambda pour éviter des frais supplémentaires.

## Conclusion

Déployer votre conteneur Docker sur AWS Lambda est un moyen efficace de faire fonctionner votre application rapidement sans vous soucier de la gestion des serveurs ou des plateformes.

Merci de m'avoir lu !