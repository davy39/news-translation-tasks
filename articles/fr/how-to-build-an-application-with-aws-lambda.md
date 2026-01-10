---
title: Comment construire une application avec AWS Lambda
subtitle: ''
author: Ijeoma Igboagu
co_authors: []
series: null
date: '2025-01-28T15:19:50.562Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-application-with-aws-lambda
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1738077341437/939ee844-0f10-4ea6-b031-9c481019e7c6.png
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Cloud Computing
  slug: cloud-computing
- name: aws lambda
  slug: aws-lambda
- name: Cloud
  slug: cloud
seo_title: Comment construire une application avec AWS Lambda
seo_desc: 'AWS Lambda is a service from Amazon Web Services (AWS) that lets you run
  your code in response to events without managing servers. It’s a simple and scalable
  way to build applications.

  In this tutorial, I’ll show you how to use AWS Lambda with three ...'
---

AWS Lambda est un service d'Amazon Web Services (AWS) qui vous permet d'exécuter votre code en réponse à des événements sans gérer de serveurs. C'est une manière simple et évolutive de construire des applications.

Dans ce tutoriel, je vais vous montrer comment utiliser AWS Lambda avec trois autres services :

* **Amazon S3** pour stocker des fichiers, des images et des vidéos

* **Amazon Simple Notification Service (SNS)** pour envoyer des notifications

* **Amazon EventBridge** pour planifier des messages

Nous allons tout passer en revue étape par étape.

À la fin, avec l'intégration des autres services, vous aurez construit une application de citations de manifestation d'objectifs qui envoie des messages inspirants aléatoires pour vous garder motivé et concentré sur vos objectifs.

### Prérequis

* Un compte AWS : Si vous n'en avez pas, inscrivez-vous [ici](https://aws.amazon.com/).

* Un dépôt GitHub : Cela sert à stocker votre code source. Si vous n'avez pas de compte GitHub, vous pouvez en créer un [ici](https://github.com/).

* Un environnement de développement intégré (IDE) tel que [Visual Studio Code](https://code.visualstudio.com/) ou [Sublime Text](https://www.sublimetext.com/download).

* Une connaissance de base du développement web et d'un langage de programmation de votre choix. J'ai utilisé Python pour ce tutoriel.

* [Zenquote Random API](https://zenquotes.io/)

### Ce que vous allez apprendre

* Comment créer un bucket Amazon S3

* Comment utiliser Amazon Simple Notification Service (SNS)

* Comment utiliser Amazon Lambda

* Comment utiliser Amazon EventBridge

## **Table des matières**

1. [Étape 1 : Configurer votre environnement de développement](#heading-step-1-set-up-your-development-environment)

2. [Étape 2 : Créer un Amazon Simple Storage Service (S3)](#heading-step-2-create-an-amazon-simple-storage-service-s3)

3. [Étape 3 : Créer un Amazon Simple Notification Service (SNS)](#heading-step-3-create-an-amazon-simple-simple-notification-service)

4. [Étape 4 : Créer une politique IAM](#heading-step-4-create-an-iam-policy)

5. [Étape 5 : Créer une fonction Amazon Lambda](#heading-step-5-create-an-amazon-lambda-function)

6. [Étape 6 : Créer un EventBridge](#heading-step-6-create-an-eventbridge)

7. [Étape 7. Télécharger votre code](#heading-step-7-upload-your-code)

8. [Conclusion](#heading-conclusion)

![Commençons 🚀](https://cdn.hashnode.com/res/hashnode/image/upload/v1736791948488/38dfe402-1050-410d-869b-0cef2797b792.png align="center")

## Étape 1 : Configurer votre environnement de développement

Dans cette étape, vous allez tout configurer. Commencez par vous connecter à votre compte AWS, puis installez [Python](https://www.python.org/downloads/) si vous ne l'avez pas sur votre IDE.

## **Étape 2 : Créer un Amazon Simple Storage Service (S3)**

Avant de commencer à créer un bucket S3, comprenons d'abord ce qu'est Amazon S3 :

**Amazon S3 (Simple Storage Service)** est un service d'Amazon qui vous permet de stocker et d'accéder à n'importe quelle quantité ou type de données, telles que des photos, des vidéos, des documents et des sauvegardes, chaque fois que vous en avez besoin.

Maintenant que vous connaissez les bases de ce qu'est Amazon S3, revenons au tutoriel.

### Créer un bucket S3

Il existe plusieurs façons de créer un bucket S3, mais pour ce tutoriel, nous utiliserons la [ligne de commande Ubuntu (CMD)](https://ubuntu.com/download), votre terminal, ou **Amazon CloudShell**, selon ce avec quoi vous êtes le plus à l'aise.

* Tapez boto3 s3 dans la barre de recherche web pour voir une liste de documentations connexes.

* Cliquez sur le premier résultat.

![Recherche Google régulière](https://cdn.hashnode.com/res/hashnode/image/upload/v1736792137101/5f38b4ec-fa23-41b3-b108-ca7fc7b390ba.png align="right")

* Une fois la documentation ouverte, copiez la première commande que vous voyez.

![commande boto3](https://cdn.hashnode.com/res/hashnode/image/upload/v1736792202800/5647c731-734f-4134-a558-9d66eee47734.png align="left")

* Collez-la sur votre CMD ou terminal de votre choix – mais avant cela, n'oubliez pas de faire un "**cd**" dans le bon répertoire.

![coller la commande de la documentation dans votre éditeur](https://cdn.hashnode.com/res/hashnode/image/upload/v1736792298332/d3384fc3-e31c-4d37-8e17-40ad7e77df28.png align="left")

* Dans la documentation, faites défiler vers le bas et cliquez sur "create\_bucket.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736792399748/0cd59a14-b037-464b-8193-7ec515c4772e.png align="left")

* Une fois ouvert, faites défiler vers le bas jusqu'à "Request Syntax." Copiez le **nom du bucket** et la **configuration du bucket**.

* Les autres variables listées dans la syntaxe de la requête sont facultatives.

![Syntaxe de la requête de la documentation](https://cdn.hashnode.com/res/hashnode/image/upload/v1736792898846/eea0f8c4-d153-4bc8-8c78-346fc5bf6a04.png align="left")

* Une fois cela fait, assurez-vous de sauvegarder.

![Toutes les commandes](https://cdn.hashnode.com/res/hashnode/image/upload/v1736793004865/a1c9739c-2d12-4e2d-b057-f09bc61e16a3.png align="left")

* Revenez en arrière et appelez le script :

```plaintext
#python3 votre nom de fichier
```

* L'exécution du script crée automatiquement un bucket S3 dans votre Amazon S3.

![Création automatique](https://cdn.hashnode.com/res/hashnode/image/upload/v1736793086405/9c0b4671-ea07-4ad7-b1d7-0d785aafa954.png align="left")

* Vous pouvez maintenant aller dans la console pour vérifier s'il a été créé :

![Console Amazon](https://cdn.hashnode.com/res/hashnode/image/upload/v1736692453693/320318d4-bdf3-4be3-a709-6cff18459c9c.png align="center")

### Télécharger des fichiers

Avec le bucket créé, nous pouvons maintenant télécharger des fichiers via la console. Je crois qu'il existe également un moyen programmatique de télécharger des fichiers et de tester, mais je n'ai pas encore exploré toutes les méthodes dans la documentation.

Cliquez sur le nom du bucket pour être redirigé vers la page des objets. C'est ici que vous téléchargerez vos fichiers pour le stockage.

![page de téléchargement](https://cdn.hashnode.com/res/hashnode/image/upload/v1736692660862/355f828f-f83f-4501-a960-f0068cf9d977.png align="center")

Cliquez sur le **bouton de téléchargement** pour télécharger un fichier. N'oubliez pas, nous créons une application de citations de manifestation d'objectifs.

Maintenant que nous avons configuré un bucket de stockage :

* Ouvrez un outil comme Google Drive, MS Word, WPS, ou tout autre éditeur de documents.

* Écrivez les objectifs que vous souhaitez atteindre.

* Enregistrez le fichier au format PDF ou DOCX.

* Prenez le document et téléchargez-le sur votre Amazon S3.

![télécharger un document](https://cdn.hashnode.com/res/hashnode/image/upload/v1736693525955/765b6c3a-ae68-4cbc-9df7-e896a1d63cbb.png align="center")

Pour vérifier si c'est le bon fichier :

* Accédez à l'onglet **Permissions**.

* Faites défiler vers le bas jusqu'à **Block public access**.

* Cliquez sur **Edit** et décochez la case.

![bloquer l'accès](https://cdn.hashnode.com/res/hashnode/image/upload/v1736738796036/6ab41bc4-72a8-4874-a491-35bcdda49938.png align="center")

Comme montré ci-dessus, il est actuellement défini sur "on". Décochez-le pour le mettre sur "off".

* Sur la même page des paramètres du bucket, modifiez la politique.

* Faites défiler vers le bas, et vous verrez qu'une politique de bucket a été générée automatiquement.

* Allez-y et copiez la politique.

```plaintext
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::your-bucket-name/*"
    }
  ]
}
```

* Revenez à l'éditeur de politique de bucket et collez la politique.

Une fois que vous avez terminé ces étapes, votre objet aura un accès public.

Retournez à l'onglet **Objets** et cliquez sur l'URL de l'objet fournie ci-dessous :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736740454730/3b36b380-912d-4a2a-a8c5-bee61bd42765.png align="center")

Avec cette URL, votre téléchargement est maintenant visible.

## **Étape 3 : Créer un Amazon Simple Notification Service (SNS)**

**SNS** est un service de messagerie entièrement géré fourni par AWS. Il permet la communication entre les applications ou directement avec les utilisateurs en envoyant des notifications.

Pour créer un SNS, suivez ces étapes :

#### **1. Connectez-vous à la console de gestion AWS**

Ensuite, allez à Amazon SNS. Accédez au tableau de bord SNS et sélectionnez **Topics** dans le menu de gauche.

Pour créer un topic :

* Cliquez sur **Create topic**.

* Choisissez un **Type de topic** : Standard (par défaut) ou FIFO (pour les messages ordonnés).

* Entrez un **Nom** pour votre topic. (par exemple, `MyFirstSNSTopic`).

![création de topic sns](https://cdn.hashnode.com/res/hashnode/image/upload/v1736743311856/fa51ecb9-935a-4567-829c-b84ee3c1bee0.png align="center")

* Configurez les paramètres optionnels comme le chiffrement, les politiques de nouvelle tentative de livraison, ou les tags.

* Cliquez sur **Create topic**.

#### **2. Ajouter des abonnements :**

Une fois le topic créé, cliquez dessus pour ouvrir la page des détails. Sélectionnez l'onglet **Subscriptions**.

Cliquez sur **Create Subscription** et choisissez :

* **Protocol** peut être Email, SMS, HTTP/S, Lambda, ou SQS.

* **Endpoints** tels qu'une adresse email, un numéro de téléphone, ou une URL.

Cliquez sur **Create Subscription**.

![Abonnement créé](https://cdn.hashnode.com/res/hashnode/image/upload/v1736743374208/8005dc71-68ed-4d26-b79b-7b418959ab6c.png align="center")

#### **3. Confirmer l'abonnement :**

Si vous avez sélectionné email ou SMS, un lien de confirmation ou un code sera envoyé à l'endpoint fourni. Suivez les instructions pour confirmer l'abonnement.

![Un message de confirmation d'amazon sns](https://cdn.hashnode.com/res/hashnode/image/upload/v1736743525222/90c3b61d-eeb2-450d-a397-253b9e3c15db.png align="center")

Maintenant que nous avons fait cela, créons une fonction Amazon Lambda qui déclenchera le SNS afin que le message soit envoyé à votre email.

## **Étape 4 : Créer une politique IAM**

Cette politique est créée pour autoriser Amazon Lambda à déclencher l'événement et pour s'assurer que CloudWatch est automatiquement déclenché pour surveiller les événements de l'application.

Pour créer une politique, suivez ces étapes :

#### **1. Connectez-vous à la console de gestion AWS.**

Dans le menu de gauche, sélectionnez **Policies**. Ensuite :

* Cliquez sur **Create policy**.

* Choisissez l'onglet **Visual**, puis sélectionnez le service **SNS**.

* Ensuite, cliquez sur l'onglet **Choose** pour créer une politique personnalisée.

```plaintext
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "sns:Publish",
            "Resource": "arn:aws:sns:REGION:ACCOUNT_ID:goal_topic"
        }
    ]
}
```

Ensuite, remplacez les espaces réservés suivants par vos informations :

* `region` : Votre région AWS (par exemple, `us-east-1`).

* `account-id` : Votre identifiant de compte AWS.

* `topic-name` : Votre nom de topic SNS.

#### **2. Voir et créer la politique :**

Vous pouvez le faire en suivant ces étapes :

* Cliquez sur le bouton Review.

* Donnez un **Nom** à votre politique (par exemple, `LambdaSNSPolicy`), et éventuellement, une **Description**.

* Cliquez sur **Create policy**.

#### 3. Attacher la politique au rôle d'exécution Lambda

Maintenant, vous devez attacher la politique à votre rôle d'exécution Lambda. Pour cela, suivez ces étapes :

* Allez dans la section **Roles** de la console IAM.

* Recherchez et sélectionnez le rôle d'exécution.

![rôle lambdaexecution](https://cdn.hashnode.com/res/hashnode/image/upload/v1736749886571/70ea6752-5c13-465c-bc05-22e3da50127e.png align="center")

* Ensuite, recherchez la politique que vous venez de créer et sélectionnez-la.

* Cliquez sur **Attach policy**.

Les deux politiques seront automatiquement attachées.

## **Étape 5 : Créer une fonction Amazon Lambda**

Amazon Lambda est un service d'AWS qui vous permet d'exécuter du code sans gérer de serveurs. Vous téléchargez votre code, et Lambda l'exécute et le met à l'échelle automatiquement lorsque cela est nécessaire.

Suivez ces étapes pour créer une fonction Amazon Lambda :

#### **1. Connectez-vous à la console de gestion AWS :**

Accédez à AWS Lambda.

#### **2. Créer une fonction :**

Cliquez sur **Create function** et choisissez l'option **Author from scratch**.

Remplissez les détails :

* **Nom de la fonction** : Entrez un nom unique (par exemple, `SNSLambdaFunction`).

* **Runtime** : Sélectionnez le runtime (par exemple, Python, Node.js, Java, etc.).

![création d'une fonction](https://cdn.hashnode.com/res/hashnode/image/upload/v1736751631488/fe254e56-89f1-4938-b2a9-e59b24e54a04.png align="center")

* **Rôle** : Choisissez ou créez un rôle. Si vous avez déjà un rôle, sélectionnez **Use an existing role**. Sinon, sélectionnez **Create a new role with basic Lambda permissions**.

![choix du rôle](https://cdn.hashnode.com/res/hashnode/image/upload/v1736751816631/97475623-10dc-4427-87ab-7e8789526e9e.png align="center")

* Cliquez sur le bouton **Create function**.

#### **3. Coller le code :**

Sur la page de la fonction Lambda, allez à l'onglet **Configuration** :

![onglet configuration](https://cdn.hashnode.com/res/hashnode/image/upload/v1736753706928/b0351665-c506-454e-9c71-b4a52fce5a0a.png align="center")

N'oubliez pas, nous essayons de récupérer une citation. J'ajouterai l'ARN du topic que nous avons créé ici et inclurai mes clés API. Mais pour ce tutoriel, j'utiliserai directement l'API pour récupérer les données.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736754071465/1322e207-5c51-45f1-979f-05f2388e9557.png align="center")

#### **4. Écrire le code Lambda :**

Allez à l'onglet **Code** dans votre fonction Lambda. Ensuite, écrivez ou collez le code de votre IDE pour traiter les messages SNS entrants.

Exemple :

![Test du code](https://cdn.hashnode.com/res/hashnode/image/upload/v1736754319755/60224578-53c2-43f6-9bf1-8cba6afaa1a3.png align="center")

Voici le code :

```python
import os
import json
import urllib.request
import boto3

def fetch_random_quote():
    """
    Récupère une citation aléatoire depuis l'API ZenQuotes.
    """
    api_url = "https://zenquotes.io/api/random"
    try:
        with urllib.request.urlopen(api_url) as response:
            data = json.loads(response.read().decode())
            if data and isinstance(data, list):
                # Formater la citation et l'auteur
                quote = data[0].get("q", "No quote available")
                author = data[0].get("a", "Unknown author")
                return f'"{quote}" - {author}'
            else:
                return "No quote available."
    except Exception as e:
        print(f"Error fetching random quote: {e}")
        return "Failed to fetch quote."

def lambda_handler(event, context):
    """
    Fonction de gestionnaire AWS Lambda pour récupérer une citation aléatoire et la publier sur un topic SNS.
    """
    # Obtenir l'ARN du topic SNS depuis les variables d'environnement
    sns_topic_arn = os.getenv("SNS_TOPIC_ARN")
    sns_client = boto3.client("sns")
    
    # Récupérer une citation aléatoire
    quote = fetch_random_quote()
    print(f"Fetched Quote: {quote}")
    
    # Publier la citation sur SNS
    try:
        sns_client.publish(
            TopicArn=sns_topic_arn,
            Message=quote,
            Subject="Daily Random Quote to help you stay motivated and inspired to achieve your goals",
        )
        print("Quote published to SNS successfully.")
    except Exception as e:
        print(f"Error publishing to SNS: {e}")
        return {"statusCode": 500, "body": "Error publishing to SNS"}
    
    return {"statusCode": 200, "body": "Quote sent to SNS"}
```

#### **5. Sauvegarder :**

Cliquez sur le bouton deploy pour sauvegarder.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736756768348/8ec83b6b-874c-47c3-a1ad-8d8b85cd6d48.png align="center")

#### **6. Tester votre fonction Lambda :**

Allez dans l'onglet **Test** et créez un nouvel événement de test.

![ÉVÉNEMENT DE TEST](https://cdn.hashnode.com/res/hashnode/image/upload/v1736757103169/834c5b6c-8796-4a52-bcc3-cbd8009b01da.png align="center")

Ensuite, sauvegardez et exécutez le test. Si c'est réussi, un message sera envoyé :

![msg de succès](https://cdn.hashnode.com/res/hashnode/image/upload/v1736757309807/d97f9648-0000-4ec8-b287-df5250b3be0a.png align="center")

Cela signifie que le message a été créé pour vous.

Enfin, vérifiez votre email ou SMS, selon l'endpoint que vous avez utilisé pour ce tutoriel. Dans mon cas, j'ai utilisé l'email.

![notification par email](https://cdn.hashnode.com/res/hashnode/image/upload/v1736757884384/d5b949d4-0804-4694-9674-77fc0265e2e8.png align="center")

## **Étape 6 : Créer un EventBridge**

Amazon EventBridge est un service qui vous aide à connecter des applications et des services AWS tels que Amazon SNS et Amazon Lambda.

Pour créer une règle Amazon EventBridge, suivez ces étapes :

#### **1. Accédez à EventBridge :**

Dans la barre de recherche, tapez **EventBridge** et sélectionnez-le dans la liste des services.

#### **2. Créer une règle :**

Dans la console EventBridge, cliquez sur **Rules** dans le panneau de gauche. Ensuite, cliquez sur le bouton **Create rule**.

#### **3. Configurer les détails de la règle :**

* **Nom** : Entrez un nom unique pour votre règle.

* **Description (facultatif)** : Ajoutez une description pour expliquer ce que fait cette règle.

#### **4. Choisir le bus d'événements :**

Sélectionnez **Default event bus** (ou un autre bus d'événements si vous en avez créé un).

#### **5. Définir le motif d'événement ou la planification :**

**Pour le motif d'événement :**

* Choisissez un **service AWS** comme source d'événement.

* Sélectionnez le **type d'événement** spécifique (par exemple, un téléchargement de fichier S3 ou un changement d'état d'instance EC2).

**Pour la planification :**

* Choisissez l'option **Schedule** pour exécuter la règle à intervalles fixes (par exemple, toutes les 5 minutes).

![détails de la règle](https://cdn.hashnode.com/res/hashnode/image/upload/v1736759371221/ca28dcf2-061a-4c8f-8191-32bdf8380111.png align="center")

* Cliquez sur continuer. Cela vous amène à la page des détails spécifiques où :

![page de planification](https://cdn.hashnode.com/res/hashnode/image/upload/v1736759696183/44ba44e8-2a1b-4cd8-928b-6fe87cc35c4e.png align="center")

* Faites défiler vers le bas et cliquez sur le planificateur cron. Le planificateur cron spécifie à quelle heure le message sera envoyé.

* Sélectionnez **"Off"** pour l'option de fenêtre de temps flexible.

* Passez en revue les détails de la règle pour confirmer que tout est correct.

* Cliquez sur le bouton **"Next"** pour passer à la page **Target**.

![planificateur cron](https://cdn.hashnode.com/res/hashnode/image/upload/v1736760213450/c4f6cccf-7f89-485d-802e-051284c89f9a.png align="left")

L'image ci-dessus montre quand les messages seront envoyés.

* Sur la page Target, sélectionnez **AWS Lambda** pour invoquer votre fonction.

![la page target](https://cdn.hashnode.com/res/hashnode/image/upload/v1736761288843/e35a7153-48d7-4b34-86ce-9cba68bd5161.png align="center")

* Faites défiler vers le bas pour invoquer et choisissez la fonction que vous avez créée.

![invoquer la fonction](https://cdn.hashnode.com/res/hashnode/image/upload/v1736761539389/4faa1dbc-5635-4de3-8087-15a444298b2e.png align="center")

* Cliquez sur le bouton "Next" pour continuer. Cela vous amènera à la page des paramètres. Dans la section des permissions, sélectionnez "Use existing rule."

![page des paramètres](https://cdn.hashnode.com/res/hashnode/image/upload/v1736782488383/ffbbcc4e-6379-4c9c-af16-f4c017e7426c.png align="center")

* Enfin, allez à la revue et créez une planification :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736783029778/2d0e7ff9-bb7d-462d-a644-23517f47e53e.png align="center")

* La page suivante vous montre tous les détails :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1736783558777/4545d2da-5020-46c3-a265-5499e6b4e74f.png align="center")

L'utilisation d'EventBridge crée un planificateur pour les utilisateurs.

## **Étape 7 : Télécharger votre code**

Enfin, téléchargez votre code sur GitHub et incluez une documentation appropriée pour aider à expliquer comment le code fonctionne.

Consultez cette documentation si vous ne savez pas comment faire : [Télécharger un projet sur GitHub](https://docs.github.com/en/get-started/start-your-journey/uploading-a-project-to-github).

## Conclusion

Si vous avez suivi toutes ces étapes, vous aurez créé une application de citations de manifestation d'objectifs en utilisant AWS Lambda, Amazon S3, Amazon SNS et Amazon EventBridge. Cette application récupère des citations motivantes et les envoie aux abonnés selon un calendrier.

Vous pouvez trouver le lien du dépôt [ici](https://github.com/ijayhub/goal-manifestation-quote).

N'hésitez pas à partager vos progrès ou à poser des questions si vous avez des problèmes.

Si vous avez trouvé cet article utile, partagez-le avec d'autres.

Restez informé de mes projets en me suivant sur [Twitter](https://https//twitter.com/ijaydimples), [LinkedIn](https://www.linkedin.com/in/ijeoma-igboagu/) et [GitHub](https://github.com/ijayhub)

Merci d'avoir lu 💖.

**Avis de non-responsabilité :**

Les ressources montrées dans cet article, y compris le bucket S3 et son ARN, ont été supprimées et n'existent plus. Les détails visibles dans les captures d'écran sont utilisés uniquement à des fins de démonstration.