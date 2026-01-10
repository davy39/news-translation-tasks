---
title: Comment déployer un microservice Kotlin sur AWS avec App Runner
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-15T06:34:00.000Z'
originalURL: https://freecodecamp.org/news/kotlin-aws-app-runner
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/kotlin-aws-app-runner.png
tags:
- name: AWS
  slug: aws
- name: Kotlin
  slug: kotlin
- name: ktor
  slug: ktor
- name: Microservices
  slug: microservices
seo_title: Comment déployer un microservice Kotlin sur AWS avec App Runner
seo_desc: "By Piotr Wolak\nHello, everyone. In this step-by-step tutorial, I would\
  \ like to show you how to deploy a Kotlin Microservice using Docker and AWS App\
  \ Runner. \nTogether, we will learn:\n\nwhat exactly is AWS App Runner? \nhow to\
  \ configure AWS Command Line..."
---

Par Piotr Wolak

Bonjour à tous. Dans ce tutoriel pas à pas, je vais vous montrer comment déployer un microservice Kotlin en utilisant Docker et AWS App Runner. 

Ensemble, nous allons apprendre :

* qu'est-ce exactement AWS App Runner ?
* comment configurer l'interface de ligne de commande AWS sur votre machine locale
* comment pousser des images Docker vers Amazon Elastic Container Registry (ECR)
* et enfin, comment déployer notre application conteneurisée avec AWS App Runner

Je sais, cela peut sembler être une quantité de travail énorme. Mais je suis convaincu que vous allez découvrir à quel point cela peut être simple avec cette pile technologique.

## Prérequis

Avant de commencer, assurez-vous d'avoir **Docker** déjà installé sur votre machine locale. Nous aurons besoin de conteneuriser notre application. 

Si vous n'avez pas Docker, alors la [documentation officielle de Docker](https://docs.docker.com/engine/install/) vous aidera à le configurer en quelques minutes. 

## Qu'est-ce exactement AWS App Runner ?

Tout d'abord, prenons une minute pour comprendre ce qu'est exactement **AWS App Runner**.

Pour faire simple, il s'agit d'un service entièrement géré qui permet de construire et de déployer des applications web et des API conteneurisées avec facilité. 

Il prend en charge de nombreuses choses, comme l'équilibrage de charge du trafic ou la mise à l'échelle, ce qui aide les développeurs comme vous et moi à se concentrer sur le code. 

**AWS App Runner** est souvent un excellent choix lors de la création d'une démonstration ou d'une preuve de concept, mais il vaut également la peine d'être considéré pour les petites équipes sans personne dédiée travaillant sur l'infrastructure. 

## Comment créer un microservice Kotlin simple

Cela dit, préparons une API REST simple en utilisant Kotlin et Ktor. 

Si vous n'êtes pas intéressé par l'implémentation de Ktor, vous pouvez simplement cloner [ce dépôt GitHub](https://github.com/codersee-blog/ktor-app-runner-skeleton) et passer à l'étape _Comment construire l'image Docker_. 

Si vous utilisez l'édition Ultimate d'IntelliJ IDEA, vous pouvez créer un projet Ktor en utilisant l'application. Sinon, vous pouvez utiliser l'outil [Ktor Project Generator](https://start.ktor.io/) et télécharger le projet sur votre machine locale.

Quelle que soit votre choix, assurez-vous d'importer les plugins suivants : 

* ContentNegotiation
* kotlinx.serialization
* Routing

### Comment configurer la sérialisation

Après avoir importé le projet, créez le fichier `Serialization.kt` et enregistrez le type de contenu `application/json` pour la fonctionnalité ContentNegotiation :

```kotlin
fun Application.configureSerialization() {
    install(ContentNegotiation) {
        json()
    }
}
```

En termes simples, avec ce snippet de code, nous pourrons sérialiser des objets Kotlin en JSON (et désérialiser le JSON en objets, également). 

### Comment créer un DTO

Maintenant, implémentons une classe de données `MessageDto` comme ceci :

```kotlin
@Serializable
data class MessageDto(val message: String)
```

En gros, nous utiliserons cette classe générique pour fournir des messages à nos consommateurs d'API. 

### Comment exposer des endpoints

Ensuite, créons un fichier `Routing.kt` et exposons un nouvel endpoint :

```kotlin
fun Application.configureRouting() {
    routing {
        helloWorldRoute()
    }
}

fun Routing.helloWorldRoute() {
    route("/hello") {
        get {
            call.respond(HttpStatusCode.OK, MessageDto("Hello World!"))
        }
    }
}
```

Comme vous pouvez le voir, notre application répondra avec un code de statut **200 OK** à chaque requête `GET` vers le chemin `/hello`.

### Comment configurer l'application

Maintenant, combinons tout dans le fichier `Application.kt` :

```kotlin
fun main() {
    embeddedServer(Netty, port = 8080, host = "0.0.0.0") {
        configureRouting()
        configureSerialization()
    }.start(wait = true)
}
```

Comme vous pouvez le voir, notre microservice Kotlin sera un **serveur intégré Netty** fonctionnant sur `localhost:8080`. 

Je vous encourage vivement à exécuter l'application et à vérifier que tout fonctionne correctement :

```
GET localhost:8080/hello

Statut : 200 OK
Corps de la réponse : 
{
    "message": "Hello World!"
}
```

### Comment implémenter le Dockerfile

Enfin, ajoutons le `Dockerfile` au répertoire racine de notre projet :

```
FROM openjdk:8-jdk
EXPOSE 8080:8080
RUN mkdir /app
COPY ./build/install/com.codersee.ktor-app-runner/ /app/
WORKDIR /app/bin
CMD ["./com.codersee.ktor-app-runner"]
```

Assurez-vous que le répertoire spécifié pour les commandes `COPY` et `CMD` correspond à la valeur de `rootProject.name` dans le fichier `settings.gradle.kts`. Si le nom du projet est `xyz`, alors ces commandes doivent refléter cela :

```
...
COPY ./build/install/xyz/ /app/
...
CMD ["./xyz"]
```

## Comment construire l'image Docker

À ce stade, nous avons tout ce dont nous avons besoin pour construire notre **image Docker**, que nous utiliserons plus tard pour le déploiement **AWS App Runner**.

### Exécuter la commande Gradle

En premier lieu, exécutons la commande `installDist` avec Gradle Wrapper :

```
./gradlew installDist
```

La commande ci-dessus est responsable de l'assemblage du contenu de la distribution et de son installation sur la machine actuelle. Bien que cela puisse sembler difficile, elle créera simplement les fichiers nécessaires dans le répertoire `./build/install/{nom-du-projet}/`. 

### Construire l'image Docker

Ensuite, construisons une image Docker :

```
 docker build -t ktor-aws-runner . 
```

Comme vous pouvez le voir, nous avons nommé notre image souhaitée `ktor-aws-runner` avec l'option `-t` (un raccourci pour `--tag`).

### Vérifier la configuration Docker

Enfin, exécutons notre conteneur pour nous assurer que notre microservice Kotlin fonctionne correctement :

```
docker run -p 8080:8080 ktor-aws-runner
```

Pour expliquer, le drapeau `-p` (`--port`) est responsable de la publication du port `8080` du conteneur vers le port `8080` de l'hôte. 

Cela étant fait, après quelques secondes, nous devrions voir le message suivant dans les logs :

```
Application démarrée en 0,078 secondes
```

De même, nous pouvons effectuer une requête GET pour vérifier si l'endpoint exposé répond correctement.

## Comment créer et configurer un utilisateur AWS

Avec tout cela fait, nous pouvons enfin commencer à travailler avec AWS. Mais avant de pouvoir pousser notre image Docker, nous devons nous assurer que nous avons **AWS CLI** installé sur notre machine locale. 

Nous pouvons le faire facilement avec la commande ci-dessous :

```
 aws --version
 
 # Résultat :
 aws-cli/2.5.3 Python/3.9.11 Windows/10 exe/AMD64 prompt/off
```

Le résultat ci-dessus indique que tout est configuré correctement. Néanmoins, si nous souhaitons installer ou mettre à jour le CLI, AWS fournit un article très utile à ce sujet dans leur [documentation officielle](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). 

De plus, nous devons avoir accès à AWS Cloud depuis notre ordinateur – et c'est ce que nous allons configurer dans cette étape.

Pour configurer l'accès, connectons-nous à la **Console de gestion AWS** et naviguons vers la fonction **Utilisateurs** de la **Console IAM**. Nous pouvons le faire facilement avec la barre de recherche en haut :

![L'image montre les résultats de recherche pour la requête "users" dans la Console de gestion AWS](https://www.freecodecamp.org/news/content/images/2022/04/1-1.png)

Sur la page suivante, cliquons sur le bouton **Ajouter des utilisateurs** :

![L'image montre une liste vide d'utilisateurs dans la Console IAM AWS](https://www.freecodecamp.org/news/content/images/2022/04/2-1.png)

Ensuite, nous spécifierons le **Nom d'utilisateur** préféré ainsi que la **Clé d'accès** – le type de credential **Accès programmatique** :

![L'image montre le nom d'utilisateur et les options de type d'accès AWS pour un nouvel utilisateur](https://www.freecodecamp.org/news/content/images/2022/04/3-1.png)

Avec ces paramètres, nous pourrons accéder à AWS en utilisant une combinaison de clé d'accès et de secret.

Cela étant fait, cliquons sur le bouton Suivant. Sur cette page, nous devons sélectionner le groupe pour notre utilisateur. Pour les besoins de ce tutoriel, créons un nouveau groupe en utilisant le bouton visible ci-dessous :

![L'image montre les paramètres de permissions et de limites de permissions pour un nouvel utilisateur](https://www.freecodecamp.org/news/content/images/2022/04/4-2.png)

Ensuite, spécifions un **Nom de groupe** (dans mon cas, `admin-group`) dans la modale et sélectionnons **AdministratorAccess** :

Pour simplifier, nous allons utiliser AdministratorAccess. Mais dans des scénarios réels, nous devons toujours respecter le Principe du Moindre Privilège.

![L'image montre un nouveau nom de groupe avec la politique sélectionnée - AdministratorAccess](https://www.freecodecamp.org/news/content/images/2022/04/5-2.png)

Après la création du groupe, cliquons à nouveau sur le bouton Suivant :

![L'image montre les groupes existants et le groupe admin-group sélectionné](https://www.freecodecamp.org/news/content/images/2022/04/6-2.png)

Sur la page suivante, nous avons l'option d'ajouter des **tags personnalisés** sous forme de paires clé-valeur. 

Mais nous n'en aurons pas besoin aujourd'hui, alors passons simplement cette page :

![L'image montre le formulaire d'ajout de tags (optionnel)](https://www.freecodecamp.org/news/content/images/2022/04/7-2.png)

Enfin, nous serons redirigés vers la page **Révision**, où nous pouvons valider nos étapes précédentes :

![L'image présente les détails de révision du nouvel utilisateur](https://www.freecodecamp.org/news/content/images/2022/04/8-1.png)

Comme vous pouvez le voir, tout semble bon, alors cliquons sur **Créer un utilisateur** :

![L'image montre l'utilisateur créé](https://www.freecodecamp.org/news/content/images/2022/04/9-1.png)

L'utilisateur a été créé avec succès, donc nous pouvons enfin importer nos clés d'accès et secrètes. 

Gardez à l'esprit que les clés d'accès et secrètes sont des données hautement confidentielles et que vous ne devez jamais les partager avec qui que ce soit !

Cliquons sur le bouton **Télécharger .csv** et récupérons le fichier. Personnellement, je l'ai nommé `some_user_credentials.csv`, mais n'hésitez pas à choisir le nom que vous souhaitez (et à vous en souvenir :) ).

Ensuite, naviguons vers le répertoire de téléchargement et exécutons la commande suivante :

```
 aws configure import --csv file://some_user_credentials.csv
 
 # Résultat :
 1 profil(s) importé(s) avec succès
```

Étant donné le message ci-dessus, nous pouvons nous attendre à ce que tout ait été configuré correctement. De plus, nous pouvons vérifier qu'un nouveau fichier appelé `credentials` a été créé (ou mis à jour) dans le répertoire `.aws`. 

Si vous utilisez Windows, votre chemin sera `C:\Users\[votre_nom_d_utilisateur]\.aws`:

```
[some-admin]
aws_access_key_id = [votre_id_de_clé_d_accès] 
aws_secret_access_key = [votre_secret] 

```

## Comment pousser l'image Docker vers ECR

À ce stade, notre CLI est correctement préparée, donc nous pouvons apprendre à pousser notre image Docker locale vers le **Elastic Container Registry**.

En premier lieu, retournons à la **Console de gestion** et tapons **container registry** dans la barre de recherche :

![L'image montre les résultats de recherche pour la requête 'container reqistry'](https://www.freecodecamp.org/news/content/images/2022/04/10-1.png)

Cliquons sur **Elastic Container Registry** et sur la page suivante, sur le bouton **Créer un dépôt**. Sur la page suivante, sélectionnons un dépôt privé et spécifions un nom pour celui-ci :

![L'image montre les paramètres généraux de création de dépôt](https://www.freecodecamp.org/news/content/images/2022/04/11-1.png)

Pour le reste des paramètres, laissons les valeurs par défaut, comme ci-dessous :

![L'image montre les paramètres d'analyse et de chiffrement de l'image](https://www.freecodecamp.org/news/content/images/2022/04/12.png)

Enfin, cliquons sur le bouton **Créer un dépôt**.

Après cela, nous serons redirigés vers la liste des dépôts privés, qui contient maintenant notre dépôt nouvellement créé :

![L'image présente les dépôts privés avec un élément - my-ktor-registry dans la liste](https://www.freecodecamp.org/news/content/images/2022/04/13.png)

Copions l'URI et spécifions la commande suivante dans le terminal sur notre machine locale :

```
docker tag ktor-aws-runner:latest [votre_uri_de_registre]:latest

# Exemple : docker tag ktor-aws-runner:latest 111111111111.dkr.ecr.us-east-1.amazonaws.com/my-ktor-registry:latest
```

Pourquoi avons-nous besoin de cela ? Eh bien, en gros, lorsque nous travaillons avec Docker, **nous devons taguer les images avec l'hôte et le port du registre** (si nécessaire) afin de les pousser vers un dépôt privé.

Cela étant fait, authentifions-nous auprès du registre Amazon ECR :

```
aws ecr get-login-password --profile some-admin --region us-east-1 | docker login --username AWS --password-stdin [votre_uri_de_registre]

# Résultat :
Connexion réussie
```

Après cela, nous pouvons exécuter la commande `git push` afin de pousser l'image vers ECR :

```
docker push [votre_image_taguée] 

# Exemple : docker push 111111111111.dkr.ecr.us-east-1.amazonaws.com/my-ktor-registry:latest
```

Selon votre connexion, cela peut prendre un certain temps, mais finalement, nous devrions voir la liste mise à jour dans notre dépôt :

![L'image montre les images de my-ktor-registry avec un élément - latest dans la liste](https://www.freecodecamp.org/news/content/images/2022/04/14.png)

## Comment déployer l'application sur AWS App Runner

Maintenant, nous avons tout ce dont nous avons besoin pour partager notre microservice Kotlin avec le monde :) 

Retournons à la Console de gestion et recherchons app runner :

![L'image présente les résultats de recherche pour la requête app runner](https://www.freecodecamp.org/news/content/images/2022/04/15.png)

Sur la page suivante, cliquons sur le bouton **Créer un service**.

Pour la configuration de la source, choisissons **Container registry** ainsi que **Amazon ECR** :

![L'image présente les paramètres de source et de déploiement pour le nouveau déploiement](https://www.freecodecamp.org/news/content/images/2022/04/16.png)

Comme vous l'aurez peut-être remarqué, AWS App Runner peut déployer des services directement à partir d'un dépôt de code source. Si vous êtes intéressé par une telle configuration, contactez-moi simplement par email (contact[at]codersee[dot]com).

Ensuite, cliquons sur Parcourir et sélectionnons l'**image créée précédemment** :

![L'image présente le dépôt d'images sélectionné et le tag de l'image](https://www.freecodecamp.org/news/content/images/2022/04/17.png)

Cliquons sur continuer et pour les paramètres de déploiement, choisissons **Manuel** et **Créer un nouveau rôle de service** :

![L'image montre le déclencheur de déploiement, le rôle d'accès ECR et le nom du rôle de service](https://www.freecodecamp.org/news/content/images/2022/04/18.png)

Le nom du rôle n'est pas important dans ce tutoriel, donc nous pouvons spécifier n'importe quelle valeur. 

Ensuite, cliquons sur Suivant et sur la page suivante, fournissons un **Nom de service** ainsi que les informations **CPU**, **Mémoire** et **Port** :

![Image](https://www.freecodecamp.org/news/content/images/2022/04/19.png)
_L'image présente le nom du service, le CPU, la mémoire, les variables d'environnement, le port et les paramètres de configuration supplémentaires_

Comme vous pouvez le voir, nous avons choisi la combinaison minimale disponible (et c'est ce que je vous suggère de faire également).

Si nous souhaitons spécifier des variables d'environnement supplémentaires ou une commande de démarrage personnalisée, cette page nous permet de le faire. Mais nous n'aurons pas besoin de variables d'environnement et nous avons déjà ajouté une commande de démarrage à notre image Docker, alors laissons-la telle quelle.

Sur la page de mise à l'échelle automatique, sélectionnons **Configuration personnalisée** :

![L'image montre les paramètres de mise à l'échelle automatique avec une configuration personnalisée définie](https://www.freecodecamp.org/news/content/images/2022/04/20.png)

Ensuite, créons une nouvelle configuration appelée **my-configuration** :

![L'image montre la modale d'ajout de configuration de mise à l'échelle automatique personnalisée](https://www.freecodecamp.org/news/content/images/2022/04/21.png)

Comme je l'ai mentionné au début, AWS App Runner prend en charge de nombreuses choses dès la sortie de la boîte. L'une d'entre elles est la mise à l'échelle automatique. Bien que ce soit une fonctionnalité formidable, nous devons la limiter à nos préférences et toujours nous rappeler que plus de ressources signifie des coûts plus élevés. 

Comme vous pouvez le voir ci-dessus, cette configuration d'exemple **ne mettra pas à l'échelle notre microservice Kotlin**. Cependant, si nous augmentons la taille maximale, une nouvelle instance sera créée chaque fois que le nombre de requêtes simultanées augmente de 10. 

Ajoutons la configuration ci-dessus et laissons le reste des éléments avec leurs valeurs par défaut. Après avoir cliqué sur Suivant, nous verrons la page de révision avec le résumé du déploiement. 

Sur cette page, cliquons sur le bouton `Créer et déployer`, ce qui démarrera le processus de déploiement :

![L'image présente le processus de déploiement AWS App Runner démarré](https://www.freecodecamp.org/news/content/images/2022/04/22.png)

![L'image présente les logs de déploiement avec l'événement appelé Créer un service](https://www.freecodecamp.org/news/content/images/2022/04/23.png)

Et encore une fois, ce processus peut prendre quelques minutes. Une fois terminé, le statut passera de `Opération en cours` à `En cours d'exécution` et nous pourrons tester notre API REST Ktor.

Tout comme précédemment, testons l'endpoint `GET /hello`. Mais cette fois, en tant que nom d'hôte de notre microservice, nous devons utiliser la valeur de `Domaine par défaut` :

```
#Exemple : 

GET https://aaaaaaaaaa.us-east-1.awsapprunner.com/hello

Statut : 200 OK
Corps de la réponse : 
{
    "message": "Hello World!"
}
```

## ⚠️ Avis important

Veuillez vous souvenir de **supprimer toutes les ressources que nous avons créées aujourd'hui**, afin de ne pas être facturé pour celles-ci. 

Il est vraiment facile d'oublier toutes les choses que nous créons en apprenant AWS Cloud et à un moment donné, vous pourriez dépasser votre quota gratuit. Ainsi, il est bon de tout supprimer.

## Résumé

Et c'est tout pour ce tutoriel sur comment déployer un microservice Kotlin sur AWS Cloud avec AWS App Runner. J'espère vraiment qu'après avoir suivi ce guide, vous êtes en mesure de déployer facilement vos applications sur Amazon Cloud. 

Si vous avez apprécié ce matériel, alors vous pourriez vouloir consulter mes [autres articles](https://codersee.com/articles/). Sur mon blog, je couvre de nombreux sujets liés à Kotlin, Ktor et Spring Boot. 

Si vous souhaitez me poser une question, n'hésitez pas à me contacter à l'adresse _contact[at]codersee[dot]com_.