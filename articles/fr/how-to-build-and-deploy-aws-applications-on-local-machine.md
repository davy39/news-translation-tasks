---
title: Comment construire et déployer des applications AWS sur votre machine locale
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-10-26T18:19:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-and-deploy-aws-applications-on-local-machine
coverImage: https://www.freecodecamp.org/news/content/images/2020/10/aws-localstack.png
tags:
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: Comment construire et déployer des applications AWS sur votre machine locale
seo_desc: "By Siben Nayak\nIn my previous articles, I talked about building and deploying\
  \ serverless applications on AWS using Chalice and SAM. \nThese were quick fun projects\
  \ that leveraged the power of serverless computing and allowed us to deploy a serverless\
  \ ..."
---

Par Siben Nayak

Dans mes articles précédents, j'ai parlé de la construction et du déploiement d'applications serverless sur AWS en utilisant [Chalice](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-chalice/) et [SAM](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/).

C'étaient des projets rapides et amusants qui ont exploité la puissance de l'informatique serverless et nous ont permis de déployer une application serverless sur AWS en quelques minutes.

Mais beaucoup de gens ne peuvent pas tirer pleinement parti de tels tutoriels s'ils n'ont pas de compte AWS. La création d'un compte AWS et la configuration d'un environnement de développement peuvent prendre du temps. Et cela peut également entraîner des dépenses non désirées (si vous ne le configurez pas correctement).

Dans cet article, je vais vous guider à travers les étapes nécessaires pour construire et déployer une application serverless sans avoir à créer et configurer un compte AWS réel.

Cette fois, nous allons créer une application de magasin d'animaux de compagnie en utilisant Amazon API Gateway, AWS Lambda et Amazon DynamoDB. Cette application aura des API pour ajouter un nouvel animal de compagnie et récupérer la liste des animaux de compagnie disponibles.

## Prérequis

Nous allons utiliser AWS SAM pour ce tutoriel. Vous pouvez installer et configurer SAM en suivant les directives dans l'article précédent [ici](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/).

## Comment créer un projet

Exécutez la commande `sam init` pour créer un nouveau projet. Cela créera un dossier `pet-store` dans votre répertoire actuel.

```
sam init -r java11 -d maven --app-template pet-store -n pet-store
```

Pour plus de détails sur les paramètres passés, veuillez vous référer à l'article précédent [ici](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/).

Modifions le fichier `pom.xml` pour mettre à jour le nom du module en `PetStore` et utiliser `Java 11` au lieu de `Java 8`.

<script src="https://gist.github.com/theawesomenayak/b4ce1270c5565b03276d1c1c4b781b6f.js"></script>

Créons maintenant une classe `Pet` pour contenir les attributs des animaux de compagnie. Nous commencerons par des attributs simples comme `name`, `age` et `category`.

<script src="https://gist.github.com/theawesomenayak/e8a936936f5682ba7a44f93df9e7a9fa.js"></script>

Puisque nous allons utiliser Amazon DynamoDB comme notre magasin de données, ajoutons les dépendances SDK correspondantes dans le fichier `pom.xml`.

<script src="https://gist.github.com/theawesomenayak/9d973fdfa33f5eed177b683ae7967f33.js"></script>

Cela ajoutera les dépendances pour le SDK AWS pour DynamoDB et le client HTTP Apache que nous utiliserons pour créer un client DynamoDB synchrone.

## Comment lire et écrire des éléments

Nous devons créer une classe d'accès aux données pour interagir avec Amazon DynamoDB et exécuter nos requêtes de lecture/écriture. Créez une classe `PetStoreClient` et ajoutez la dépendance sur `DynamoDbClient`.

<script src="https://gist.github.com/theawesomenayak/2ce83949b4968b7bf1149b984156f48a.js"></script>

Nous allons maintenant créer deux fonctions dans la classe `PetStoreClient` pour lire et écrire des éléments depuis DynamoDB.

### Écrire un élément

L'ajout d'un seul élément dans DynamoDB est une requête `PUT`. Nous allons créer une `PutItemRequest` et spécifier le nom de la table et les attributs de l'élément à ajouter.

Nous allons ensuite utiliser le `DynamoDbClient` pour mettre cet élément dans DynamoDB.

<script src="https://gist.github.com/theawesomenayak/0582463529a6527ee35b5062e5c50b67.js"></script>

### Lire des éléments

La lecture d'une liste d'éléments dans DynamoDB est une requête `SCAN`. Nous allons créer une `ScanRequest` et spécifier le nom de la table à scanner.

Nous allons ensuite utiliser le `DynamoDbClient` pour scanner la table dans DynamoDB et retourner une liste d'éléments.

<script src="https://gist.github.com/theawesomenayak/d9ce18ec8aa219c529e5072705a3f10d.js"></script>

**Note :** Une requête de scan parcourt tous les éléments de la table, donc je ne la recommande pas pour des cas d'utilisation réels.

## Comment résoudre les dépendances

Nous avons ajouté `DynamoDbClient` comme dépendance dans notre classe `PetStoreClient`. En tant que bonne pratique générale, toutes ces dépendances dans votre code doivent être résolues en utilisant l'injection de dépendances (DI).

Lorsque vous entendez parler de DI, Spring est probablement le nom qui vous vient à l'esprit. Mais l'écosystème Spring est ENORME et vous devrez inclure beaucoup de ses frameworks même si vous voulez juste utiliser la partie DI.

De plus, l'injection est faite au moment de l'exécution, ce qui rend le temps de démarrage à froid de Lambda encore plus long.

Guice est un autre framework d'injection de dépendances qui est beaucoup plus léger que Spring. Mais comme Spring, il fait l'injection au moment de l'exécution, donc ce n'est pas un bon candidat pour DI non plus.

Ensuite, il y a Dagger, un framework purement DI qui injecte les dépendances pendant la compilation ! Sa petite taille et l'injection à la compilation en font le choix parfait pour implémenter DI dans les Lambdas.

Je vais approfondir les détails de DI et couvrir l'utilisation de Dagger dans un autre article. Dans cet article, nous allons utiliser le style intemporel des méthodes de fabrique statiques pour fournir des dépendances.

Créons une classe appelée `DependencyModule` et déclarons toutes nos dépendances dans celle-ci.

<script src="https://gist.github.com/theawesomenayak/897bba001e0074b6366a1e427430fc93.js"></script>

Dans cette classe, nous créons une nouvelle instance de `DynamoDbClient` et l'injectons dans notre `PetStoreClient`. Nous créons également une instance de `ObjectMapper` pour nous aider à gérer la sérialisation et la désérialisation des objets JSON.

## Comment mettre à jour le Lambda et les points de terminaison de l'API

Ensuite, nous devons mettre à jour le point d'entrée pour la fonction Lambda et ajouter nos points de terminaison spécifiques pour ajouter et récupérer des animaux de compagnie.

Ajoutez le fragment suivant à la section `Resources` du fichier `template.yaml`.

<script src="https://gist.github.com/theawesomenayak/c9dbf3c18711e930a0ad496155e35d1a.js"></script>

Cela met à jour notre fonction pour utiliser la méthode `handleRequest` de la classe `App`. Il ajoute également deux points de terminaison d'API pour ajouter et récupérer des animaux de compagnie.

Mettez également à jour la section `Outputs` pour refléter le nouveau nom de la fonction.

## Comment intégrer le client

Maintenant que nous avons le code pour interagir avec DynamoDB prêt et les dépendances triées, nous devons apporter des modifications dans le gestionnaire Lambda pour invoquer ce code.

Mettez à jour le code dans `App.java` pour invoquer les fonctions dans `PetStoreClient` et effectuer les actions selon la requête de l'API.

<script src="https://gist.github.com/theawesomenayak/eb0a804afa955087aecf32b6e990f997.js"></script>

Puisque nous avons utilisé des fabriques statiques pour l'injection de dépendances, nous ne pourrons pas tester efficacement notre code. Je couvrirai les tests unitaires des applications cloud dans un autre article. Pour l'instant, nous devons supprimer les tests unitaires afin de construire le projet.

## Comment construire le projet

Depuis le dossier `pet-store`, exécutez la commande `sam build`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-build-1.png)

Cela compile votre code source et construit toutes les dépendances que vous avez dans l'application. Il déplace ensuite tous les fichiers dans le dossier `.aws-sam/build` afin qu'ils soient prêts à être emballés et déployés.

## Comment tester localement (Partie 1)

Dans l'article précédent [ici](https://www.freecodecamp.org/news/how-to-build-a-serverless-application-using-aws-sam/), nous avons discuté de la manière dont l'interface de ligne de commande SAM fournit la commande `sam local` pour exécuter votre application localement. Cela utilise en interne Docker pour simuler l'environnement d'exécution de Lambda. Si vous n'avez pas Docker installé, vous pouvez l'obtenir [ici](https://docs.docker.com/get-docker/).

Cela convenait pour l'API Daily News car elle récupérait des données depuis Internet et ne dépendait d'aucun autre composant AWS.

Cependant, dans notre projet actuel, nous dépendons d'Amazon DynamoDB comme magasin de données et avons besoin d'y accéder pour pouvoir exécuter notre application avec succès.

Essentiellement, nous avons besoin d'un moyen de simuler les services fournis par AWS sur notre machine locale afin de pouvoir les tester localement sans utiliser un compte AWS réel.

### Comment exécuter AWS localement

[LocalStack](https://localstack.cloud/) a été créé juste pour résoudre ce problème. En ses propres termes :

> LocalStack fournit un framework de test/simulation facile à utiliser pour développer des applications Cloud. Il lance un environnement de test sur votre machine locale qui fournit la même fonctionnalité et les mêmes API que l'environnement cloud AWS réel.

En résumé, LocalStack apporte toutes les fonctionnalités du cloud AWS dans un conteneur Docker s'exécutant localement sur votre machine. Cela vous permet de construire et de tester vos applications cloud sans avoir à les déployer sur un compte cloud AWS réel.

Que signifie cela pour vous en tant que développeur ?

1. Pas besoin de provisionner un compte AWS.
2. Pas besoin de configurer un environnement de développement et de penser à la sécurité et à d'autres configurations.
3. Pas besoin de supporter des coûts AWS inutiles pendant la période de développement.
4. Environnement local transparent qui imite exactement l'environnement AWS réel.

### Comment configurer LocalStack

LocalStack est vraiment facile à configurer et à commencer à utiliser. Nous allons utiliser Docker pour obtenir la dernière image de LocalStack et démarrer un conteneur qui exécute une version simulée d'Amazon DynamoDB.

Créez un fichier `docker-compose.yaml` dans le dossier `pet-store` et ajoutez le contenu suivant :

<script src="https://gist.github.com/theawesomenayak/baee28a3d38a28c4870e2638cf03feb9.js"></script>

Examinons quelques-unes des configurations que nous utilisons :

* SERVICES – puisque Amazon DynamoDB est notre seule dépendance, nous n'activerons que ce service spécifique
* DEFAULT_REGION – nous utiliserons us-west-1 comme notre région AWS
* LAMBDA_EXECUTOR – le définir à local signifie que toutes nos fonctions Lambda s'exécuteront dans un répertoire temporaire sur la machine locale
* DATA_DIR – emplacement pour sauvegarder les données persistantes pour des services comme Amazon DynamoDB

**Note :** Tous les services LocalStack sont exposés via le service edge sur le port 4566. C'est le seul port que nous devons utiliser.

Maintenant, nous pouvons utiliser `docker-compose` pour démarrer notre version locale d'Amazon DynamoDB dans son propre conteneur.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/localstack-up.png)

### Comment créer une table

Maintenant que nous avons une configuration locale d'Amazon DynamoDB en cours d'exécution, nous devrions être en mesure de créer une table pour notre application.

Nous avons utilisé `pet-store` comme nom de table dans notre code, alors allons-y et créons-la. Nous allons utiliser AWS CLI pour accéder à Amazon DynamoDB s'exécutant sur notre machine locale et créer la table requise.

Exécutez la commande suivante pour créer une table nommée `pet-store` avec un attribut `id` comme clé primaire.

```
aws --endpoint-url "http://localhost:4566" dynamodb create-table \ 
    --table-name pet-store \    
    --attribute-definitions AttributeName=id,AttributeType=S \    
    --key-schema AttributeName=id,KeyType=HASH \    
    --billing-mode PAY_PER_REQUEST
```

Notez que nous avons utilisé le paramètre `endpoint-url` pour spécifier que nous pointons vers l'instance AWS s'exécutant localement plutôt que vers celle réelle.

## Comment tester localement (Partie 2)

Apportez la modification suivante au code DynamoDbClient pour le pointer vers l'instance Amazon DynamoDB s'exécutant localement :

<script src="https://gist.github.com/theawesomenayak/887b3bbea7565cc123b1ce44a6121d7c.js"></script>

Ensuite, utilisez `sam build` pour construire le projet et exécutez la commande suivante pour démarrer l'API localement :

```
sam local start-api
```

Cela crée en interne un serveur local et expose un point de terminaison local qui réplique votre API REST.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/sam-start.png)

Maintenant, testons notre application en ajoutant un nouvel animal de compagnie. Exécutez la commande suivante pour ajouter un nouvel animal de compagnie en invoquant le point de terminaison `/pet` que nous avons spécifié précédemment.

```
curl --location --request PUT 'http://127.0.0.1:3000/pet' \
--header 'Content-Type: application/json' \
--data-raw '{    
    "name": "Rocket",    
    "age": 2,    
    "category": "Dog"
}'
```

Cela crée un nouvel enregistrement Pet, l'ajoute à notre Amazon DynamoDB local et retourne l'UUID généré dans la réponse.

Ajoutons un autre animal de compagnie à notre magasin.

```
curl --location --request PUT 'http://127.0.0.1:3000/pet' \
--header 'Content-Type: application/json' \
--data-raw '{    
    "name": "Candle",    
    "age": 1,    
    "category": "Pig"
}'
```

Maintenant, invoquons notre API `/pets` pour obtenir une liste des animaux de compagnie disponibles dans notre magasin de données. Nous devrions nous attendre à obtenir une liste d'animaux de compagnie contenant `Rocket` et `Candle`.

![Image](https://www.freecodecamp.org/news/content/images/2020/10/curl-pets.png)

## Conclusion

Félicitations ! Vous venez de construire et de déployer une application serverless qui utilise AWS DynamoDB complètement sur votre machine locale.

Vous pouvez maintenant apporter des modifications à votre fichier `App.java`. Réexécutez `sam deploy` pour redéployer vos modifications et `sam local start-api` pour démarrer le serveur local et tester les modifications.

Une fois que vous êtes prêt pour le déploiement, vous devez simplement supprimer les remplacements de point de terminaison et vous êtes prêt à partir. Dans une situation idéale, cela serait contrôlé par des variables d'environnement et ne nécessiterait absolument aucun changement de code pour le rendre prêt pour la production.

Le code source complet de ce tutoriel peut être trouvé [ici](https://github.com/theawesomenayak/pet-store).

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de technologie et de vie. Jetez également un coup d'œil à certains de mes autres articles [ici sur freeCodeCamp News](https://www.freecodecamp.org/news/author/theawesomenayak/) ou sur [Medium](https://medium.com/@theawesomenayak).

Bonne lecture 📖