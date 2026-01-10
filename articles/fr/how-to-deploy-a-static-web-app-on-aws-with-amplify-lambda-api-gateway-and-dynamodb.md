---
title: Comment déployer une application Web statique sur AWS avec Amplify, Lambda,
  API Gateway et DynamoDB
subtitle: ''
author: Raju Manoj
co_authors: []
series: null
date: '2025-07-18T13:50:19.362Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-static-web-app-on-aws-with-amplify-lambda-api-gateway-and-dynamodb
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752792908077/abfe8200-e4bd-4c3c-892f-15847715c918.png
tags:
- name: AWS
  slug: aws
- name: aws lambda
  slug: aws-lambda
- name: AWS Amplify
  slug: awsamplify
- name: Beginner-friendly AWS projects for hands-on experience
  slug: beginner-friendly-aws-projects-for-hands-on-experience
- name: '#aws projects'
  slug: aws-projects
- name: aws-apigateway
  slug: aws-apigateway
- name: ' #HandsOnLearning '
  slug: handsonlearning
- name: cloud project
  slug: cloud-project
seo_title: Comment déployer une application Web statique sur AWS avec Amplify, Lambda,
  API Gateway et DynamoDB
seo_desc: Building modern web applications often involves complex setups and managing
  servers – but it doesn't have to be that way. Amazon Web Services (AWS) offers a
  powerful suite of "serverless" services that allow you to build and deploy applications
  witho...
---

La construction d'applications Web modernes implique souvent des configurations complexes et la gestion de serveurs – mais cela n'a pas à être le cas. Amazon Web Services (AWS) offre une puissante suite de services "serverless" qui vous permettent de construire et de déployer des applications sans avoir à vous soucier de l'infrastructure sous-jacente. Cela signifie qu'AWS gère tout le travail lourd des serveurs, de la mise à l'échelle et de la maintenance pour vous.

Dans ce tutoriel, nous allons vous guider à travers la construction d'une application Web simple mais entièrement fonctionnelle en utilisant plusieurs services serverless clés d'AWS. Vous apprendrez comment connecter un frontend (ce que les utilisateurs voient) avec un backend puissant (ce qui traite les données) qui peut se mettre à l'échelle automatiquement et efficacement.

## **Table des matières**

* [Ce que nous allons construire : une calculatrice de somme serverless](#heading-ce-que-nous-allons-construire-une-calculatrice-de-somme-serverless)

* [Services AWS principaux que nous allons utiliser](#heading-services-aws-principaux-que-nous-allons-utiliser)

* [Prérequis : ce dont vous aurez besoin](#heading-prérequis-ce-dont-vous-aurez-besoin)

* [Pour commencer : comment construire notre application Web serverless](#heading-pour-commencer-comment-construire-notre-application-web-serverless)

* [Comment tester votre application : fonctionne-t-elle ?](#heading-comment-tester-votre-application-fonctionne-t-elle)

* [Problèmes courants et solutions](#heading-problèmes-courants-et-solutions)

* [Prochaines étapes : améliorez votre application](#heading-prochaines-étapes-améliorez-votre-application)

* [Conclusion](#heading-conclusion)

## Ce que nous allons construire : une calculatrice de somme serverless

Nous allons créer une application Web de **calculatrice de somme** simple. Cette application permettra aux utilisateurs de saisir deux nombres, de les envoyer à notre backend AWS pour le calcul, de stocker le résultat, puis d'afficher la somme à l'utilisateur.

**Voici comment notre calculatrice fonctionnera :**

* **Tout d'abord, elle prendra les entrées de l'utilisateur :** Vous saisirez deux nombres dans une page Web simple.

* **Ensuite, la magie du backend se produit avec AWS Lambda :** Ces nombres seront envoyés à un morceau spécial de code s'exécutant sur AWS Lambda, qui les additionnera.

* **Ensuite, les données sont stockées à l'aide de DynamoDB :** Les détails du calcul (les deux nombres, leur somme et le moment où cela s'est produit) seront enregistrés dans une base de données super rapide appelée DynamoDB.

* **Enfin, elle affiche les résultats :** La somme sera renvoyée à votre page Web et vous sera affichée.

Ce projet est un excellent moyen de comprendre les concepts de base de l'architecture serverless et comment différents services AWS travaillent ensemble pour créer une application Web dynamique.

## Services AWS principaux que nous allons utiliser

Avant de plonger dans le vif du sujet, familiarisons-nous avec les principaux services AWS que nous allons utiliser. Considérez-les comme des outils spécialisés, chacun ayant son propre rôle, travaillant ensemble pour construire notre application.

1. **AWS Lambda :** Imaginez que vous avez un petit robot qui ne s'active que lorsqu'on lui donne une tâche spécifique. C'est Lambda ! C'est un service de "calcul serverless", ce qui signifie que vous ne gérez aucun serveur. Vous téléchargez simplement votre code (notre logique de calculatrice, dans ce cas), et Lambda l'exécute uniquement lorsque cela est nécessaire.

   **Pourquoi l'utilisons-nous :** Il gère nos calculs mathématiques backend (addition de nombres). Lorsqu'un utilisateur demande une somme, Lambda "se réveille", effectue le calcul, puis se rendort. Cela est efficace et rentable car vous ne payez que pour le temps pendant lequel votre code est réellement en cours d'exécution.

2. **Amazon API Gateway :** Considérez cela comme le portier ou le réceptionniste de votre backend. Lorsque votre page Web veut parler à votre fonction Lambda, elle ne parle pas directement. Au lieu de cela, elle envoie une requête à API Gateway.

   **Pourquoi l'utilisons-nous :** API Gateway reçoit en toute sécurité les requêtes de notre page Web (comme "Veuillez additionner ces deux nombres") et indique ensuite à la fonction Lambda correcte de se réveiller et de les traiter. Il agit comme le point d'entrée sécurisé de notre backend, s'assurant que seules les requêtes autorisées passent.

3. **Amazon DynamoDB :** Il s'agit de notre base de données super rapide et flexible. Contrairement aux bases de données traditionnelles qui sont comme des classeurs, DynamoDB est une base de données NoSQL (Not Only SQL), qui est idéale pour gérer de grandes quantités de données rapidement et efficacement sans une structure fixe.

   **Pourquoi l'utilisons-nous :** Nous utiliserons DynamoDB pour stocker l'historique de nos calculs (les nombres saisis et leurs sommes). Il est conçu pour gérer d'énormes quantités de trafic sans ralentir, ce qui le rend parfait pour les applications Web qui doivent stocker et récupérer des données rapidement.

4. **AWS Amplify :** Amplify est comme votre équipe de construction personnelle pour les applications Web et mobiles. Il simplifie le processus de construction, de déploiement et d'hébergement de votre application frontend, et il s'intègre parfaitement avec d'autres services AWS.

   **Pourquoi l'utilisons-nous :** Nous utiliserons Amplify pour héberger notre simple page Web HTML, CSS et JavaScript. Il fournit un moyen facile de mettre notre site Web en ligne sur Internet, en gérant toutes les étapes de déploiement complexes pour nous.

## Prérequis : ce dont vous aurez besoin

Pour suivre ce tutoriel, vous devez avoir :

* **Un compte AWS :** Cela est essentiel pour accéder à tous les services AWS. Si vous n'en avez pas, vous pouvez vous inscrire pour un compte gratuit sur le site Web d'AWS.

* **Connaissances de base en Python :** Notre logique backend sera écrite en Python.

* **Compréhension des API REST :** Savoir ce qu'est une API (Application Programming Interface) et comment fonctionnent les API RESTful sera utile, mais nous expliquerons les parties clés.

* **Familiarité avec HTML/CSS/JavaScript :** Notre frontend sera construit en utilisant ces technologies Web standard.

* **Connaissances de base en NoSQL :** Bien que ce ne soit pas strictement requis, comprendre le concept des paires clé-valeur dans les bases de données peut être bénéfique.

Commençons !

## Pour commencer : comment construire notre application Web serverless

Nous allons construire notre application étape par étape, en commençant par la base de données, puis notre code backend, en les connectant avec une API, et enfin, en déployant notre frontend.

### Étape 1 : Configurer votre base de données avec Amazon DynamoDB

Notre calculatrice a besoin d'un endroit pour stocker les résultats de ses calculs. Pour cela, nous utiliserons Amazon DynamoDB. Vous pouvez suivre ces étapes pour tout configurer :

#### 1. Accédez à la console DynamoDB :

Tout d'abord, connectez-vous à votre console de gestion AWS. Dans la barre de recherche en haut, tapez "DynamoDB" et sélectionnez "DynamoDB" dans les résultats. Cela vous amènera au tableau de bord DynamoDB.

#### 2. Créez une nouvelle table :

Sur le tableau de bord DynamoDB, recherchez et cliquez sur le bouton **"Créer une table"**.

![Capture d'écran de la console DynamoDB avec le bouton "Créer une table" mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1752056336365/33bf0598-da2e-45b9-9211-833bcd447ca9.png align="center")

Figure 1 : Création d'une nouvelle table dans la console DynamoDB.

#### 3. Configurez votre table :

Vous devrez ajouter les informations suivantes pour la table :

* **Nom de la table :** Entrez `myTable`. Ce sera le nom de notre table de base de données.

* **Clé de partition :** Entrez `ID`.

Mais vous vous demandez peut-être – qu'est-ce qu'une clé de partition ? Dans DynamoDB, la "clé de partition" (parfois appelée clé de hachage) est comme l'identifiant principal pour chaque élément unique de votre table. Considérez-la comme un numéro d'identification unique pour chaque enregistrement. Elle aide DynamoDB à trouver et à distribuer rapidement vos données. Pour notre calculatrice, chaque calcul que nous stockons recevra un `ID` unique.

Laissez tous les autres paramètres à leurs valeurs par défaut pour ce tutoriel. Ces valeurs par défaut sont généralement suffisantes pour les cas d'utilisation de base.

![Capture d'écran du formulaire "Créer une table" de DynamoDB avec "myTable" et "ID" saisis, et les autres paramètres par défaut](https://cdn.hashnode.com/res/hashnode/image/upload/v1752053498063/05a9db73-0df6-4679-b2bd-6eab52f93a6b.png align="center")

Figure 2 : Configuration de la 'myTable' avec 'ID' comme clé de partition.

#### 4. Finalisez la création de la table :

Cliquez sur le bouton **"Créer une table"** en bas de la page. DynamoDB va maintenant créer votre table, ce qui prend généralement quelques secondes.

#### 5. Important : Notez l'ARN de la table (Amazon Resource Name) :

Une fois votre table créée, cliquez sur son nom (`myTable`) dans la liste pour accéder à sa page de détails. Sous l'onglet "Résumé", vous trouverez une section qui affiche l'**"ARN"**. Il s'agit d'un identifiant unique pour votre table DynamoDB dans AWS.

**Copiez cet ARN entier et sauvegardez-le quelque part en sécurité (comme un bloc-notes).** Nous en aurons besoin plus tard lorsque nous configurerons les permissions pour notre fonction Lambda.

![Capture d'écran de la page de détails de la table DynamoDB avec l'ARN mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1752053703489/be90f79a-38cd-42c6-b014-e0be229384fa.png align="center")

Figure 3 : Localisation et copie de l'ARN pour votre table DynamoDB.

### Étape 2 : Création de votre logique backend avec AWS Lambda

Maintenant que nous avons notre base de données, créons le cerveau de notre opération : la fonction Lambda qui effectuera l'addition et sauvegardera les résultats.

#### 1. Accédez à la console Lambda :

Dans la barre de recherche de la console de gestion AWS, tapez "Lambda" et sélectionnez "Lambda" dans les résultats. Cela vous amènera au tableau de bord Lambda.

Ensuite, créez une nouvelle fonction en cliquant sur le bouton **"Créer une fonction"** sur le tableau de bord.

#### 2. Configurez la fonction :

Maintenant, il est temps de configurer votre fonction :

* **Créer à partir de zéro :** Assurez-vous que cette option est sélectionnée.

* **Nom de la fonction :** Donnez à votre fonction un nom significatif, par exemple, `SumCalculatorFunction` ou `AddFunc`.

* **Runtime :** Cela spécifie le langage de programmation dans lequel votre code est écrit. Pour ce tutoriel, sélectionnez **"Python 3.9"** (ou le dernier runtime Python 3.x disponible).

  * **Remarque :** Choisissez toujours un runtime qui correspond au code que vous allez écrire !

* **Architecture :** Laissez `x86_64` (par défaut).

* **Permissions :** Pour l'instant, vous pouvez laisser le rôle d'exécution par défaut. Nous modifierons ses permissions sous peu.

![Capture d'écran de la configuration "Créer une fonction" de Lambda avec le nom et le runtime Python sélectionnés](https://cdn.hashnode.com/res/hashnode/image/upload/v1752053897286/6873bb14-d94e-4857-be6c-2964c21f7759.png align="center")

Figure 4 : Configuration du nom et du runtime de votre fonction Lambda.

#### 3. Créez la fonction :

Ensuite, créez la fonction en cliquant sur le bouton **"Créer une fonction"** en bas.

#### 4. Écrivez le code de la fonction Lambda :

Maintenant, il est temps d'écrire le code de votre fonction Lambda. Une fois votre fonction créée, vous serez redirigé vers sa page de configuration. Faites défiler vers le bas jusqu'à la section **"Source du code"**. C'est ici que vous écrivez ou collez votre code Python.

Vous verrez un fichier `lambda_function.py` par défaut. Remplacez son contenu par le code Python suivant :

```python
import json
import boto3
import time
from botocore.exceptions import ClientError

# Crée un client DynamoDB. Cette ligne crée une connexion au service DynamoDB.
# 'boto3' est le SDK AWS pour Python, permettant à notre code Python de communiquer avec les services AWS.
dynamodb = boto3.resource('dynamodb')
# Spécifie la table DynamoDB avec laquelle nous voulons interagir. Assurez-vous que 'myTable' correspond au nom que vous avez créé.
table = dynamodb.Table('myTable')

# Il s'agit de la fonction principale que Lambda exécutera lorsqu'elle sera déclenchée.
# 'event' contient les données envoyées à notre fonction Lambda (par exemple, les nombres de notre frontend).
# 'context' fournit des informations d'exécution sur l'invocation, la fonction et l'environnement d'exécution.
def lambda_handler(event, context):
    # Extrait les nombres des données 'event'.
    # .get() est utilisé pour récupérer les valeurs en toute sécurité, retournant None si la clé n'existe pas.
    num1 = event.get('num1')
    num2 = event.get('num2')

    # Validation de base : Vérifie si les deux nombres ont été fournis.
    if num1 is None or num2 is None:
        # Si ce n'est pas le cas, retourne un message d'erreur avec un code d'état 400 (Bad Request).
        return {
            'statusCode': 400,
            'body': json.dumps({'message': 'Les deux num1 et num2 sont requis'})
        }

    # Calcule la somme des deux nombres.
    sum_result = num1 + num2

    # Génère un ID unique pour notre élément DynamoDB.
    # Nous utilisons un timestamp (heure actuelle en millisecondes) pour garantir l'unicité.
    partition_key = str(int(time.time() * 1000))

    # Génère une clé de tri (facultatif, mais bonne pratique pour des modèles de données plus complexes).
    # Ici, nous utilisons également un timestamp, mais vous pourriez utiliser d'autres données significatives.
    sort_key = str(int(time.time()))

    # Prépare les données (élément) à stocker dans notre table DynamoDB.
    # Chaque paire clé-valeur ici représente un attribut dans notre enregistrement de base de données.
    item = {
        'ID': partition_key,  # Cela correspond à notre clé de partition dans DynamoDB
        'Timestamp': sort_key, # Un attribut supplémentaire pour suivre le moment où le calcul a eu lieu
        'num1': num1,
        'num2': num2,
        'sum': sum_result
    }

    # Tente de stocker l'élément dans la table DynamoDB.
    try:
        table.put_item(Item=item) # 'put_item' est l'opération DynamoDB pour ajouter un nouvel élément.
    except ClientError as e:
        # Si une erreur survient lors du stockage des données (par exemple, problèmes de permissions), retourne une erreur 500.
        return {
            'statusCode': 500,
            'body': json.dumps({'message': f'Erreur lors du stockage des données dans DynamoDB : {e.response["Error"]["Message"]}'})
        }

    # Si tout s'est bien passé, retourne un message de succès et les détails du calcul.
    # Le 'statusCode: 200' indique un succès.
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'Somme calculée et stockée avec succès',
            'result': {
                'ID': partition_key,
                'Timestamp': sort_key,
                'num1': num1,
                'num2': num2,
                'sum': sum_result
            }
        })
    }
```

J'ai ajouté beaucoup de commentaires au code, mais voici ce qui se passe en résumé :

* `import json, boto3, time, ClientError` : Ces lignes importent les modules Python nécessaires.

  * `boto3` est crucial pour interagir avec les services AWS comme DynamoDB.

  * `json` nous aide à travailler avec les données au format JSON, ce qui est courant pour les API Web.

  * `time` est utilisé pour générer des ID uniques.

  * `ClientError` nous aide à attraper des erreurs spécifiques à AWS.

* `dynamodb = boto3.resource('dynamodb')` : Cette ligne crée un objet de connexion au service DynamoDB.

* `table = dynamodb.Table('myTable')` : Cela spécifie quelle table DynamoDB (celle que nous venons de créer) notre fonction Lambda va utiliser.

* `lambda_handler(event, context)` : Il s'agit de la fonction spéciale qu'AWS Lambda appelle automatiquement lorsque votre fonction est déclenchée.

  * `event` : Contient toutes les informations sur le déclencheur. Dans notre cas, il contiendra `num1` et `num2` envoyés depuis notre frontend Web.

  * `context` : Fournit des informations d'exécution sur la fonction Lambda.

* `num1 = event.get('num1')`, `num2 = event.get('num2')` : Ces lignes extraient en toute sécurité les nombres `num1` et `num2` des données `event` entrantes.

* `if num1 is None or num2 is None:` : Il s'agit d'une vérification de base pour s'assurer que les deux nombres ont été fournis. Sinon, il envoie un message d'erreur.

* `sum_result = num1 + num2` : C'est ici que le calcul de la somme se produit.

* `partition_key = str(int(time.time() * 1000))` : Cela crée un `ID` unique pour chaque enregistrement. Nous utilisons le timestamp actuel (en millisecondes) pour garantir qu'il est toujours unique.

* `item = {...}` : Ce dictionnaire définit la structure de données de l'élément que nous voulons sauvegarder dans notre `myTable` dans DynamoDB.

* `table.put_item(Item=item)` : Il s'agit de la ligne principale qui indique à DynamoDB de sauvegarder notre `item` dans la table `myTable`. Elle est enveloppée dans un bloc `try-except` pour attraper les erreurs lors de l'opération de la base de données.

* `return { 'statusCode': 200, 'body': json.dumps({...}) }` : Il s'agit de la réponse que notre fonction Lambda envoie à celui qui l'a appelée (qui sera API Gateway, puis notre frontend Web). Un `statusCode` de `200` signifie succès. Le `body` contient le message et le résultat du calcul au format JSON.

![Capture d'écran de l'éditeur de code Lambda avec le code Python collé](https://cdn.hashnode.com/res/hashnode/image/upload/v1752053964053/037e2788-b43f-4f43-bc9a-65417001d353.png align="center")

Figure 5 : Saisie du code Python pour votre fonction Lambda de calculatrice de somme.

#### 5. Déployez le code :

Maintenant, il est temps de déployer votre code. Après avoir collé le code, cliquez sur le bouton **"Déployer"** au-dessus de l'éditeur de code. Cela sauvegarde vos modifications et les rend actives.

#### 6. Testez la fonction Lambda :

Enfin, une fois le code déployé, vous voudrez tester votre fonction Lambda (c'est facultatif mais recommandé). Cliquez sur le bouton **"Test"** à côté du bouton "Déployer". Vous serez invité à configurer un événement de test.

Choisissez "Nouvel événement" et pour le "Modèle d'événement", sélectionnez "hello-world" (ou laissez-le par défaut si "hello-world" n'est pas une option). Remplacez le JSON d'exemple dans la zone "JSON de l'événement" par les données de test suivantes :

```json
{ "num1": 5, "num2": 10 }
```

Donnez un nom à votre événement de test (par exemple, `testSum`). Ensuite, cliquez sur **"Enregistrer"** puis sur **"Test"**. Vous devriez voir un message "Statut : Réussi" et dans l'onglet "Résultat de l'exécution", vous verrez un `statusCode: 200` et la somme calculée dans le `body`. Cela confirme que votre fonction Lambda fonctionne correctement !

![Console AWS Lambda montrant un script Python pour une fonction Lambda nommée "AddFunc". Le code importe des modules pour interagir avec DynamoDB et définit une fonction de gestionnaire pour extraire et additionner deux nombres. Un événement de test est configuré avec des valeurs d'entrée JSON pour "num1" et "num2". La sortie de la console indique une exécution réussie, affichant la somme calculée et un message de statut.](https://cdn.hashnode.com/res/hashnode/image/upload/v1752054962119/650bee28-fcd3-416d-9e19-0784274b8210.png align="center")

Figure 6 : Nous pouvons voir 200 ok après le test et le déploiement de votre fonction Lambda.

### Mise à jour des permissions de la fonction Lambda (stratégie de rôle IAM)

Notre fonction Lambda a actuellement des permissions par défaut, qui n'incluent généralement pas l'accès à DynamoDB. Nous devons explicitement lui accorder la permission d'*écrire* des données dans notre `myTable`. Nous allons faire cela via une stratégie de rôle IAM (Identity and Access Management).

#### 1. Accédez aux permissions :

Sur la page de configuration de votre fonction Lambda, cliquez sur l'onglet **"Configuration"**. Ensuite, sélectionnez le sous-onglet **"Permissions"**.

Vous verrez une section **"Rôle d'exécution"** avec un "Nom du rôle". Cliquez sur ce **"Nom du rôle"** (ce sera un lien). Cela vous amènera à la console IAM, spécifiquement aux détails du rôle associé à votre fonction Lambda.

![ Capture d'écran de l'onglet Configuration -> Permissions de la fonction Lambda avec le "Nom du rôle" mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1752054336167/bcb46506-a95b-47f0-b629-3a8ac9024819.png align="center")

Figure 7 : Localisation du rôle IAM associé à votre fonction Lambda.

#### 2. Ajoutez des permissions :

Sur la page du rôle IAM, vous verrez une section intitulée "Stratégies de permissions". Cliquez sur **"Ajouter des permissions"** puis sélectionnez **"Créer une stratégie en ligne"**. Une "stratégie en ligne" est une stratégie qui est intégrée directement dans une identité IAM spécifique (dans ce cas, le rôle d'exécution de notre Lambda).

![ Capture d'écran de la page du rôle IAM, montrant le menu déroulant "Ajouter des permissions" et "Créer une stratégie en ligne" sélectionné](https://cdn.hashnode.com/res/hashnode/image/upload/v1752056539801/500c1465-91dc-49cc-b313-93ddf314142e.png align="center")

Figure 8 : Ajout d'une stratégie en ligne au rôle IAM de la fonction Lambda.

#### 3. Configurez la stratégie :

Vous serez présenté avec un **"Éditeur de stratégie"**. Cliquez sur l'onglet **"Éditeur visuel"** (si ce n'est pas déjà sélectionné).

* **Service :** Cliquez sur **"Choisir un service"** et recherchez et sélectionnez **"DynamoDB"**.

* **Actions :** Dans la section "Actions", développez "Écrire". Nous devons donner à notre fonction Lambda la permission de "mettre" des éléments dans DynamoDB.

  * Recherchez `PutItem` et cochez la case à côté de `PutItem`. **Pourquoi** `PutItem` ? Notre code Python utilise `table.put_item(Item=item)` pour stocker des données. Cette action `PutItem` correspond directement à cette opération.

* **Ressources :** C'est crucial ! Nous devons spécifier *quelle* table DynamoDB notre fonction Lambda est autorisée à écrire.

  * Cliquez sur **"Spécifique"** sous la section "Ressources".

  * Cliquez sur **"Ajouter un ARN"** à côté de "table".

  * Dans la fenêtre contextuelle, collez l'**ARN de la table DynamoDB** que vous avez copié précédemment à l'étape 1.

  * Cliquez à nouveau sur **"Ajouter un ARN"** dans la fenêtre contextuelle pour confirmer.

![ Capture d'écran de l'éditeur de stratégie visuelle IAM : service DynamoDB sélectionné, action PutItem cochée, et ARN de la table DynamoDB collé dans la section des ressources](https://cdn.hashnode.com/res/hashnode/image/upload/v1752056582357/10454e95-e63c-456f-905b-34cb7b8374ab.png align="center")

Figure 9 : Configuration de la stratégie IAM pour permettre à Lambda d'effectuer des actions `PutItem` sur votre table DynamoDB.

#### 4. Passez en revue et créez la stratégie :

Cliquez sur **"Suivant : Balises"** (si applicable, ignorez les balises). Ensuite, cliquez sur **"Suivant : Passer en revue la stratégie"**. Donnez à votre stratégie un nom significatif, par exemple, `DynamoDBPutItemPolicy`.

Passez en revue le JSON de la stratégie pour vous assurer qu'elle accorde la permission `dynamodb:PutItem` sur votre ARN `myTable` spécifique. Ensuite, cliquez sur **"Créer la stratégie"**.

Votre fonction Lambda dispose maintenant des permissions nécessaires pour écrire dans votre table DynamoDB !

### Étape 3 : Connectez le Frontend au Backend avec Amazon API Gateway

Maintenant que nous avons notre fonction Lambda prête, nous avons besoin d'un moyen pour que notre page Web communique avec elle. C'est là qu'intervient API Gateway.

Dans la barre de recherche de la console de gestion AWS, tapez "API Gateway" et sélectionnez "API Gateway" dans les résultats.

#### 1. Créez une nouvelle API :

Sur le tableau de bord d'API Gateway, sous "REST API" (pas Private, WebSocket ou HTTP API), cliquez sur le bouton **"Build"**.

![Capture d'écran de la page d'accueil d'API Gateway avec le bouton "Build" sous "REST API" mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057747903/36c55082-2cac-4f05-831c-610186857a92.png align="center")

Figure 10 : Démarrage de la création d'une nouvelle API REST dans API Gateway.

#### 2. Configurez les paramètres de l'API :

* **Choisissez le protocole :** Sélectionnez `REST`.

* **Créez une nouvelle API :** Sélectionnez `Nouvelle API`.

* **Nom de l'API :** Donnez à votre API un nom clair, par exemple, `SumCalculatorAPI`.

* **Type de point de terminaison :** Choisissez `Régional` (par défaut).

Ensuite, cliquez sur **"Créer l'API"**.

#### 3. Créez une ressource :

Après avoir créé l'API, vous serez redirigé vers son tableau de bord. Dans le menu déroulant "Actions", sélectionnez **"Créer une ressource"**.

* **Nom de la ressource :** Vous pouvez le laisser comme `calculatrice` ou tout autre nom qui a du sens. Pour un point de terminaison de calculatrice simple, nous pouvons même le laisser vide, et appliquer la méthode directement à la ressource racine (`/`). Restons simple pour l'instant, et appliquons la méthode directement à la ressource racine (`/`). Si vous construisez une API plus complexe avec de nombreuses fonctions, la création de ressources spécifiques est une bonne pratique.

* **Partie du chemin :** Laissez `/` (chemin racine).

Ensuite, cliquez sur **"Créer une ressource"**.

#### 4. Créez une méthode (POST) :

Avec la ressource racine (`/`) sélectionnée dans le panneau de navigation de gauche, dans le menu déroulant **"Actions"**, sélectionnez **"Créer une méthode"**.

Choisissez **"POST"** dans le menu déroulant qui apparaît et cliquez sur le bouton de validation à côté. Nous utilisons une requête `POST` car nous *envoyons* des données (les deux nombres) au serveur pour créer un nouvel enregistrement de calcul (ou effectuer une action qui modifie les données).

Voici les détails de la configuration :

* **Type d'intégration :** Sélectionnez `Fonction Lambda`.

* **Utiliser l'intégration proxy Lambda :** Cochez cette case.

  * **Qu'est-ce que l'intégration proxy Lambda ?** Cela indique à API Gateway d'envoyer l'intégralité de la requête entrante (en-têtes, corps, paramètres de requête) directement à votre fonction Lambda en tant que partie de l'objet `event`, et également de prendre l'intégralité de la réponse de Lambda et de la transmettre directement au client. Cela simplifie la configuration car vous n'avez pas à mapper des champs de requête/réponse spécifiques.

* **Région Lambda :** Sélectionnez la région AWS où vous avez créé votre fonction Lambda (par exemple, `us-east-1` si vous avez utilisé celle-ci).

* **Fonction Lambda :** Commencez à taper le nom de votre fonction Lambda (par exemple, `SumCalculatorFunction` ou `AddFunc`) et sélectionnez-la dans la liste déroulante.

Ensuite, cliquez sur **"Enregistrer"**. Vous obtiendrez probablement une fenêtre contextuelle vous demandant de confirmer l'ajout de permissions à Lambda. Cliquez sur **"OK"**. Cela accorde automatiquement à API Gateway la permission d'invoquer votre fonction Lambda.

![Capture d'écran de l'écran "Créer une méthode" d'API Gateway avec POST sélectionné et l'intégration de la fonction Lambda configurée](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057684772/72eb9071-8ba1-42a2-9a34-60d4268ac77e.png align="center")

Figure 11 : Configuration de la méthode POST pour l'intégration avec votre fonction Lambda.

#### 5. Activez CORS (Cross-Origin Resource Sharing) :

Il s'agit d'une étape cruciale ! Notre frontend (qui sera hébergé sur AWS Amplify, un domaine différent) a besoin de la permission de communiquer avec notre point de terminaison API Gateway. CORS est une fonctionnalité de sécurité intégrée dans les navigateurs Web qui empêche les pages Web de faire des requêtes à un domaine différent de celui dont elles proviennent, sauf si cela est explicitement autorisé.

Avec la ressource racine (`/`) toujours sélectionnée, dans le menu déroulant **"Actions"**, sélectionnez **"Activer CORS"**. Une boîte de dialogue apparaîtra. Vous pouvez généralement accepter les paramètres par défaut pour cette application simple. Assurez-vous que `POST` est sélectionné sous "Méthodes" et que "Access-Control-Allow-Origin" est défini sur `'*'` (ce qui signifie que toute origine est autorisée, ce qui est bien pour une démonstration publique).

Ensuite, cliquez sur **"Activer CORS et remplacer les en-têtes CORS existants"**. Cliquez sur **"Oui, remplacer les valeurs existantes"** lorsque vous y êtes invité.

![Capture d'écran de la boîte de dialogue "Activer CORS" d'API Gateway](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057812238/0babb26e-2808-47f9-b6a8-50d31bb84ca9.png align="center")

Figure 12 : Activation de CORS pour votre point de terminaison API Gateway afin de permettre l'accès au frontend.

#### 6. Déployez votre API :

Les modifications apportées aux méthodes d'API Gateway ne sont pas actives tant que l'API n'est pas "déployée" sur un "stage". Dans le menu déroulant **"Actions"**, sélectionnez **"Déployer l'API"**.

* **Stage de déploiement :** Sélectionnez **"\[Nouveau Stage\]"**.

* **Nom du stage :** Donnez un nom à votre stage, par exemple, `dev` (pour développement), `prod` (pour production), etc. `dev` est un bon choix pour ce tutoriel.

* **Description du stage :** (Facultatif) Ajoutez une description comme "Stage de développement pour l'API de la calculatrice".

Ensuite, cliquez sur **"Déployer"**.

![Capture d'écran de la boîte de dialogue "Déployer l'API" d'API Gateway avec "Nouveau Stage" et "dev" saisis](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057834205/5de98b6c-f128-4dc6-ab68-9af65f8b8318.png align="center")

Figure 13 : Déploiement de votre API sur un nouveau stage appelé 'dev'.

#### 7. Notez l'URL d'invocation :

Après le déploiement, vous serez redirigé vers la vue "Stages". Cliquez sur votre stage nouvellement créé (par exemple, `dev`) dans le panneau de navigation de gauche.

Vous verrez une **"URL d'invocation"**. Il s'agit de l'URL publique de votre point de terminaison API.

**Copiez cette URL d'invocation entière et sauvegardez-la quelque part en sécurité. Il s'agit de l'URL que notre frontend utilisera pour envoyer des nombres à notre fonction Lambda !** Elle ressemblera à quelque chose comme [`https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev`](https://xxxxxxxxxx.execute-api.us-east-1.amazonaws.com/dev).

![Capture d'écran de la page des stages d'API Gateway avec l'"URL d'invocation"](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057869112/ec23f6bb-b885-4a44-b135-3a48c76fa93b.png align="center")

Figure 14 : Copie de l'URL d'invocation pour votre API déployée.

### Étape 4 : Créez votre application Web Frontend

Maintenant que notre backend est prêt à recevoir des requêtes et à traiter des calculs, construisons la simple page Web avec laquelle les utilisateurs interagiront. Nous utiliserons HTML, CSS et JavaScript de base.

Vous devrez créer trois fichiers dans un nouveau dossier sur votre ordinateur : `index.html`, `app.js` et `style.css`.

#### 1. `index.html` (La structure de notre page Web)

Ce fichier définit la disposition de base et le contenu de notre calculatrice.

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Calculatrice de Somme</title>
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <h1>CALCULATRICE DE SOMME</h1>

    <form id="calculatorForm">
        <label for="num1">Nombre 1 :</label>
        <input type="number" id="num1" required>

        <label for="num2">Nombre 2 :</label>
        <input type="number" id="num2" required>

        <button type="submit" id="calculateBtn">
            <span id="btnText">CALCULER</span>
            <span id="loadingSpinner" class="spinner d-none"></span> 
        </button>
    </form>

    <div id="errorAlert" class="alert d-none">
        <strong style="color: red;">Erreur !</strong> <span id="errorMessage"></span>
    </div>

    <div id="resultSection" class="result-box d-none">
        <h2>Résultat du calcul :</h2>
        <p><strong>ID de transaction :</strong> <span id="resultId"></span></p>
        <p><strong>Horodatage :</strong> <span id="resultTimestamp"></span></p>
        <p><strong>Nombres :</strong> <span id="resultNum1"></span> + <span id="resultNum2"></span></p>
        <p><strong>Somme :</strong> <span id="resultSum"></span></p>
    </div>

    <script src="app.js"></script>
</body>
</html>
```

* **Explication du code HTML :**

  * `<!DOCTYPE html>`, `<html>`, `<head>`, `<body>` : Il s'agit de balises HTML standard qui définissent la structure du document.

  * `<title>Calculatrice de Somme</title>` : Définit le titre qui apparaît dans l'onglet du navigateur.

  * `<link rel="stylesheet" href="style.css">` : Cette ligne lie notre fichier HTML à notre fichier `style.css`, qui rendra notre page attrayante.

  * `<h1>CALCULATRICE DE SOMME</h1>` : Le titre principal de notre page.

  * `<form id="calculatorForm">` : Il s'agit du conteneur pour nos champs de saisie et notre bouton. L'attribut `id="calculatorForm"` permet à notre JavaScript de trouver et d'interagir facilement avec ce formulaire.

  * `<label for="num1">`, `<input type="number" id="num1" required>` : Ces balises créent des étiquettes et des zones de saisie où les utilisateurs peuvent taper des nombres. `type="number"` garantit que seuls des nombres peuvent être saisis, et `required` signifie que le champ doit être rempli.

  * `<button type="submit" id="calculateBtn">` : Il s'agit du bouton qui, lorsqu'il est cliqué, déclenchera notre JavaScript pour envoyer des données à l'API. `type="submit"` signifie qu'il fait partie d'une soumission de formulaire.

  * `<span id="btnText">CALCULER</span>`, `<span id="loadingSpinner" class="spinner d-none"></span>` : Ces balises sont utilisées pour gérer le texte sur le bouton et afficher une petite animation de spinner lorsque le calcul est en cours. `d-none` masque initialement le spinner.

  * `<div id="errorAlert" ...>` : Une section masquée pour afficher les messages d'erreur.

  * `<div id="resultSection" ...>` : Une section masquée pour afficher les résultats d'un calcul réussi. Nous utilisons des balises `<span>` avec des ID à l'intérieur pour mettre à jour des informations spécifiques (comme `resultId`, `resultSum`, etc.) en utilisant JavaScript.

  * `<script src="app.js"></script>` : Cette ligne lie notre fichier HTML à notre fichier `app.js`. C'est ici que résidera toute la logique interactive de notre calculatrice. Il est placé à la fin du `<body>` afin que les éléments HTML soient entièrement chargés avant que le JavaScript n'essaie d'y accéder.

#### 2. `app.js` (Le cerveau de notre Frontend)

Ce fichier JavaScript gère l'interaction sur la page Web : obtenir des nombres, les envoyer à notre API et afficher les résultats ou les erreurs.

**N'oubliez pas de remplacer** `<YOUR Invoke URL>` par l'URL d'invocation réelle que vous avez copiée depuis API Gateway à l'étape 3 ci-dessus !

```javascript
document.addEventListener('DOMContentLoaded', function() {
    // Définissez le point de terminaison de l'API. REMPLACEZ CECI PAR VOTRE URL D'INVOCATION API GATEWAY RÉELLE !
    const API_ENDPOINT = 'https://YOUR_API_GATEWAY_INVOKE_URL_HERE.execute-api.us-east-1.amazonaws.com/dev'; // Exemple : https://5nur6rhsjb.execute-api.us-east-1.amazonaws.com/dev
    
    // Obtenez des références à nos éléments HTML afin que nous puissions interagir avec eux.
    const calculatorForm = document.getElementById('calculatorForm');
    const num1Input = document.getElementById('num1');
    const num2Input = document.getElementById('num2');
    const calculateBtn = document.getElementById('calculateBtn');
    const btnText = document.getElementById('btnText');
    const loadingSpinner = document.getElementById('loadingSpinner');
    const errorAlert = document.getElementById('errorAlert');
    const errorMessage = document.getElementById('errorMessage');
    const resultSection = document.getElementById('resultSection');
    
    // Références aux éléments où nous afficherons les résultats.
    const resultId = document.getElementById('resultId');
    const resultTimestamp = document.getElementById('resultTimestamp');
    const resultNum1 = document.getElementById('resultNum1');
    const resultNum2 = document.getElementById('resultNum2');
    const resultSum = document.getElementById('resultSum');
    
    // Écoutez lorsque le formulaire de la calculatrice est soumis (c'est-à-dire lorsque le bouton "CALCULER" est cliqué).
    calculatorForm.addEventListener('submit', function(event) {
        event.preventDefault(); // Empêche le comportement de soumission de formulaire par défaut (qui rechargerait la page).
        
        // Masquez les messages d'erreur ou les résultats précédents avant un nouveau calcul.
        errorAlert.classList.add('d-none'); // 'd-none' est une classe (de notre CSS) pour masquer les éléments.
        resultSection.classList.add('d-none');
        
        // Obtenez les valeurs saisies par l'utilisateur dans les champs de saisie et convertissez-les en nombres.
        const num1 = parseFloat(num1Input.value);
        const num2 = parseFloat(num2Input.value);
        
        // Validation de base des entrées : Vérifiez si les valeurs sont réellement des nombres.
        if (isNaN(num1) || isNaN(num2)) {
            showError('Veuillez entrer des nombres valides'); // Affichez une erreur si les entrées ne sont pas des nombres.
            return; // Arrêtez la fonction ici.
        }
        
        // Affichez un état de chargement sur le bouton pour indiquer qu'un calcul est en cours.
        setLoadingState(true);
        
        // Préparez les données à envoyer à notre API Gateway au format JSON.
        const requestData = {
            num1: num1,
            num2: num2
        };
        
        // Utilisez l'API Fetch pour envoyer une requête POST à notre point de terminaison API Gateway.
        fetch(API_ENDPOINT, {
            method: 'POST', // Nous envoyons des données, donc c'est une requête POST.
            headers: {
                'Content-Type': 'application/json' // Indiquez à l'API que nous envoyons des données JSON.
            },
            body: JSON.stringify(requestData) // Convertissez notre objet JavaScript en une chaîne JSON.
        })
        .then(response => {
            // Vérifiez si la réponse du réseau était OK (code d'état 200-299).
            if (!response.ok) {
                // Si ce n'est pas OK, essayez de parser le message d'erreur à partir du corps de la réponse.
                return response.json().then(errData => {
                    throw new Error(errData.message || 'Erreur du serveur');
                });
            }
            // Si OK, parsez le corps de la réponse réussie en JSON.
            return response.json();
        })
        .then(data => {
            // Une fois que nous obtenons une réponse, masquez l'état de chargement.
            setLoadingState(false);
            
            // Traitez la réponse de notre fonction Lambda.
            // Notre fonction Lambda enveloppe le résultat réel dans une chaîne 'body', nous devons donc le parser à nouveau.
            if (data.statusCode && data.statusCode === 200 && data.body) {
                try {
                    // Essayez de parser la chaîne 'body' imbriquée en un objet JavaScript.
                    const resultData = typeof data.body === 'string' 
                        ? JSON.parse(data.body) 
                        : data.body;
                    
                    // Affichez le résultat du calcul sur la page.
                    displayResult(resultData);
                } catch (err) {
                    showError('Erreur lors de l\'analyse du résultat : ' + err.message);
                }
            } else {
                showError('Format de réponse API inattendu'); // Si la réponse n'est pas celle à laquelle nous nous attendons.
            }
        })
        .catch(error => {
            // Attrapez les erreurs qui se sont produites lors de l'opération fetch (par exemple, problèmes de réseau, erreurs de l'API).
            setLoadingState(false); // Masquez l'état de chargement même en cas d'erreur.
            showError(error.message || 'Une erreur s\'est produite lors de la communication avec l\'API');
        });
    });
    
    // Fonction auxiliaire pour afficher un message d'erreur.
    function showError(message) {
        errorMessage.textContent = message; // Définissez le texte du message d'erreur.
        errorAlert.classList.remove('d-none'); // Affichez l'alerte d'erreur.
    }
    
    // Fonction auxiliaire pour gérer l'état de chargement du bouton.
    function setLoadingState(isLoading) {
        if (isLoading) {
            btnText.textContent = 'Calcul en cours...'; // Changez le texte du bouton.
            loadingSpinner.classList.remove('d-none'); // Affichez le spinner.
            calculateBtn.disabled = true; // Désactivez le bouton pour éviter les clics multiples.
        } else {
            btnText.textContent = 'CALCULER'; // Réinitialisez le texte du bouton.
            loadingSpinner.classList.add('d-none'); // Masquez le spinner.
            calculateBtn.disabled = false; // Activez le bouton.
        }
    }
    
    // Fonction auxiliaire pour afficher le résultat du calcul réussi.
    function displayResult(data) {
        // Assurez-vous que nous avons l'objet 'result' de la réponse de l'API.
        if (!data.result) {
            showError('Aucune donnée de résultat dans la réponse de l\'API');
            return;
        }
        
        const result = data.result;
        
        // Formatez le timestamp en une date et une heure lisibles.
        let timestampDisplay = result.Timestamp;
        if (result.Timestamp && !isNaN(result.Timestamp)) {
            const date = new Date(parseInt(result.Timestamp) * 1000); // Convertit les millisecondes en objet Date.
            timestampDisplay = date.toLocaleString(); // Formate en chaîne de date/heure locale.
        }
        
        // Met à jour le contenu textuel de nos éléments d'affichage des résultats.
        resultId.textContent = result.ID || 'N/A';
        resultTimestamp.textContent = timestampDisplay || 'N/A';
        resultNum1.textContent = result.num1;
        resultNum2.textContent = result.num2;
        resultSum.textContent = result.sum;
        
        // Affiche la section des résultats.
        resultSection.classList.remove('d-none');
    }
});
```

* **Explication du code JavaScript – il se passe beaucoup de choses ici :**

  * `document.addEventListener('DOMContentLoaded', function() { ... });` : Cela garantit que notre code JavaScript s'exécute uniquement après que le document HTML entier a été chargé et analysé.

  * `const API_ENDPOINT = '...';` : C'est ici que vous **DEVEZ** coller votre URL d'invocation API Gateway de l'étape 3 ci-dessus. Cette ligne définit où notre frontend enverra ses requêtes.

  * `document.getElementById(...)` : Ces lignes permettent à JavaScript de "saisir" des éléments spécifiques de notre HTML en utilisant leurs attributs `id`. Cela nous permet de lire les valeurs des entrées ou de modifier le texte/la visibilité d'autres éléments.

  * `calculatorForm.addEventListener('submit', function(event) { ... });` : Cela configure un "écouteur d'événement". Il attend que le `calculatorForm` soit soumis (lorsque le bouton "CALCULER" est cliqué) puis exécute le code à l'intérieur de cette fonction. `event.preventDefault()` empêche le navigateur de recharger la page, ce qui est le comportement par défaut pour les soumissions de formulaire.

  * `parseFloat(num1Input.value)` : Cela obtient la valeur textuelle des champs de saisie et les convertit en nombres décimaux.

  * `if (isNaN(num1) || isNaN(num2))` : Cela vérifie si l'utilisateur a saisi des nombres réels. `isNaN` signifie "is Not a Number".

  * `fetch(API_ENDPOINT, { ... })` : Il s'agit de la partie centrale qui communique avec notre backend.

    * `method: 'POST'` : Spécifie que nous envoyons des données.

    * `headers: { 'Content-Type': 'application/json' }` : Indique à API Gateway que les données que nous envoyons sont au format JSON.

    * `body: JSON.stringify(requestData)` : Convertit notre objet JavaScript `requestData` en une chaîne JSON qui peut être envoyée sur le réseau.

  * `.then(response => response.json())` : Après l'appel `fetch`, ces blocs `.then()` gèrent la réponse. Le premier vérifie si la requête réseau a réussi (`response.ok`) puis parse le corps de la réponse en JSON.

  * `.then(data => { ... })` : Ce bloc est exécuté une fois les données JSON de l'API reçues. Il met à jour le frontend avec le `result` ou affiche une `errorAlert`. Remarquez que `JSON.parse(data.body)` est utilisé car notre fonction Lambda retourne les données réelles *à l'intérieur* d'une chaîne `body` dans la réponse JSON globale.

  * `.catch(error => { ... })` : Ce bloc attrape les erreurs qui surviennent pendant l'opération `fetch` (par exemple, problèmes de réseau, ou erreurs retournées par l'API).

  * `showError()`, `setLoadingState()`, `displayResult()` : Il s'agit de fonctions auxiliaires pour garder notre code organisé. Elles gèrent l'affichage des messages, le basculement du spinner de chargement et la mise à jour de l'affichage des résultats.

  * `classList.add('d-none')`, `classList.remove('d-none')` : Ceux-ci sont utilisés pour masquer et afficher dynamiquement des éléments HTML en ajoutant ou en supprimant une classe CSS nommée `d-none`.

#### 3. `style.css` (L'apparence de notre page Web)

Ce fichier CSS ajoute un style de base pour rendre notre calculatrice présentable.

```css
/* Style de base pour le corps */
body {
    background-color: #222629; /* Fond sombre */
    color: #FFFFFF; /* Texte blanc pour le contraste */
    font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
    padding: 20px;
    display: flex;
    flex-direction: column;
    align-items: center; /* Centrer le contenu horizontalement */
    min-height: 100vh; /* Hauteur de la fenêtre */
    margin: 0;
}

h1 {
    color: #86C232; /* Un vert vibrant pour le titre */
    margin-bottom: 30px;
}

/* Style pour les étiquettes (texte à côté des champs de saisie) */
label {
    font-size: 18px;
    margin-right: 10px;
    display: inline-block; /* Permet aux étiquettes et aux champs de saisie d'être sur la même ligne */
    width: 80px; /* Donne aux étiquettes une largeur cohérente */
    text-align: right;
}

/* Style pour les champs de saisie */
input[type="number"] {
    background-color: #333;
    border: 1px solid #444;
    color: #FFFFFF;
    padding: 8px 12px;
    font-size: 16px;
    border-radius: 5px;
    margin-bottom: 15px; /* Espace sous chaque ligne de saisie */
    width: 150px; /* Largeur cohérente pour les saisies */
    outline: none; /* Supprime le contour par défaut */
}

input[type="number"]:focus {
    border-color: #86C232; /* Surbrillance de la bordure au focus */
    box-shadow: 0 0 0 3px rgba(134, 194, 50, 0.5); /* Lueur verte au focus */
}

/* Style pour le bouton CALCULER */
button {
    background-color: #86C232; /* Fond vert */
    border: none; /* Pas de bordure */
    color: #FFFFFF; /* Texte blanc */
    font-size: 18px;
    font-weight: bold;
    padding: 10px 20px;
    border-radius: 5px;
    cursor: pointer; /* Indique qu'il est cliquable */
    transition: background-color 0.3s ease; /* Transition fluide pour l'effet de survol */
    display: flex; /* Permet le spinner à l'intérieur */
    align-items: center;
    justify-content: center;
    gap: 10px; /* Espace entre le texte et le spinner */
    margin-top: 20px;
    width: 180px; /* Largeur cohérente */
}

button:hover:not(:disabled) {
    background-color: #6a9b2b; /* Vert plus foncé au survol */
}

button:disabled {
    background-color: #555; /* Grisez lorsque désactivé */
    cursor: not-allowed;
}

/* Style pour le conteneur du formulaire */
#calculatorForm {
    background-color: #333;
    padding: 30px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    display: flex;
    flex-direction: column;
    align-items: flex-start; /* Alignez les éléments du formulaire à gauche */
    margin-bottom: 30px;
}

/* Style pour le spinner de chargement */
.spinner {
    border: 3px solid rgba(255, 255, 255, 0.3);
    border-top: 3px solid #FFFFFF;
    border-radius: 50%;
    width: 20px;
    height: 20px;
    animation: spin 1s linear infinite; /* Animation pour le spinner */
}

@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}

/* Style pour la boîte de message d'erreur */
.alert {
    background-color: #330d0d; /* Fond rouge foncé pour les erreurs */
    border: 1px solid #ff4d4d; /* Bordure rouge */
    color: #ff4d4d; /* Texte rouge */
    padding: 10px 15px;
    border-radius: 5px;
    margin-top: 20px;
    width: 100%;
    max-width: 400px;
    text-align: center;
}

/* Style pour la boîte d'affichage des résultats */
.result-box {
    background-color: #333;
    border: 1px solid #86C232; /* Bordure verte pour les résultats */
    padding: 20px;
    border-radius: 8px;
    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    width: 100%;
    max-width: 400px;
    margin-top: 20px;
    animation: fadeIn 0.5s ease-in-out; /* Animation de fondu */
}

.result-box h2 {
    color: #86C232;
    margin-top: 0;
    border-bottom: 1px solid #444;
    padding-bottom: 10px;
    margin-bottom: 15px;
}

.result-box p {
    margin-bottom: 8px;
}

.result-box strong {
    color: #99EE33; /* Vert légèrement plus clair pour le texte fort */
}

/* Classe utilitaire pour masquer les éléments */
.d-none {
    display: none !important;
}

/* Animation de l'image clé pour l'effet de fondu */
@keyframes fadeIn {
    from { opacity: 0; transform: translateY(10px); }
    to { opacity: 1; transform: translateY(0); }
}
```

* **Explication du code CSS :**

  * `body { ... }` : Style la page globale, la couleur de fond, la couleur du texte, la police et centre le contenu.

  * `h1 { ... }` : Style le titre principal.

  * `label { ... }`, `input[type="number"] { ... }` : Style les champs de saisie et leurs étiquettes, les rendant cohérents et conviviaux. `input:focus` ajoute une surbrillance visuelle lorsqu'un champ de saisie est cliqué.

  * `button { ... }` : Style le bouton "CALCULER", lui donnant un aspect distinct et ajoutant un effet de survol. `button:disabled` change son apparence lorsqu'il est temporairement inactif.

  * `#calculatorForm { ... }` : Style le conteneur de notre formulaire de saisie, lui donnant un fond, un remplissage et une ombre subtile.

  * `.spinner { ... }`, `@keyframes spin { ... }` : Ceux-ci définissent le style et l'animation du spinner de chargement qui apparaît sur le bouton pendant que le calcul est en cours.

  * `.alert { ... }` : Style la boîte de message d'erreur, lui donnant un fond rouge et un texte pour indiquer clairement une erreur.

  * `.result-box { ... }` : Style la boîte où les résultats du calcul sont affichés, lui donnant une bordure verte et une animation de fondu.

  * `.d-none { display: none !important; }` : Il s'agit d'une classe utilitaire. Lorsque cette classe est ajoutée à un élément HTML via JavaScript, elle masquera complètement cet élément de la page. La suppression de la classe le rend à nouveau visible. Le `!important` garantit que ce style remplace tout autre style de display conflictuel.

  * `@keyframes fadeIn { ... }` : Cela définit une animation simple qui fait apparaître progressivement un élément (fondu) tout en se déplaçant légèrement vers le haut, rendant l'apparition des résultats plus fluide.

### Étape 5 : Déployez votre Frontend avec AWS Amplify

Enfin, mettons notre application Web frontend en ligne en utilisant AWS Amplify. Amplify rend incroyablement facile l'hébergement de sites Web statiques.

#### 1. Préparez vos fichiers Frontend :

Assurez-vous d'avoir les trois fichiers (`index.html`, `app.js`, `style.css`) dans un seul dossier sur votre ordinateur.

**Compressez ce dossier dans un fichier ZIP.** Assurez-vous que le fichier `index.html` est à la racine du fichier ZIP (non imbriqué dans un autre sous-dossier à l'intérieur du ZIP).

#### 2. Accédez à la console AWS Amplify :

Dans la barre de recherche de la console de gestion AWS, tapez "Amplify" et sélectionnez "AWS Amplify" dans les résultats.

#### 3. Déployez sans un fournisseur Git :

Sur la console Amplify, vous verrez des options pour vous connecter à un fournisseur Git (comme GitHub, GitLab, etc.). Pour simplifier dans ce tutoriel, nous choisirons de déployer manuellement.

Sous "Déployer sans fournisseur Git", cliquez sur **"Déployer"**.

![Capture d'écran de la page d'accueil de la console Amplify avec le bouton "Déployer" sous "Déployer sans fournisseur Git" mis en évidence](https://cdn.hashnode.com/res/hashnode/image/upload/v1752057954174/d4579189-1049-4896-8cc9-441101352731.png align="center")

Figure 15 : Choisir de déployer votre application Web manuellement avec AWS Amplify.

#### 4. Téléchargez vos fichiers :

* **Nom de l'application :** Donnez un nom à votre application, par exemple, `SumCalculatorWebApp`.

* **Nom de l'environnement :** Vous pouvez utiliser `dev` ou `main`.

* **Glissez-déposez ou parcourez les fichiers :** Cliquez sur la zone "glissez-déposez" ou sur le bouton "Choisir des fichiers".

* Sélectionnez le **fichier ZIP** que vous avez créé à l'étape 5 ci-dessus.

![Capture d'écran de l'écran "Déployer sans fournisseur Git" d'Amplify avec le nom de l'application et la section de téléchargement du fichier ZIP](https://cdn.hashnode.com/res/hashnode/image/upload/v1752054718089/1e94472b-4190-489b-8c10-ec402f883cef.png align="center")

Figure 16 : Nommer votre application Amplify et télécharger le fichier ZIP contenant votre frontend.

#### 5. Passez en revue et déployez :

Maintenant, cliquez sur **"Enregistrer et déployer"**. Amplify va maintenant prendre votre fichier ZIP, extraire son contenu et déployer votre site Web statique sur un réseau de diffusion de contenu (CDN) mondial fourni par AWS CloudFront. Cela permet à votre site Web de se charger rapidement pour les utilisateurs du monde entier. Ce processus peut prendre quelques minutes.

#### 6. Accédez à votre application en direct :

Une fois le déploiement terminé, Amplify vous fournira une URL de **"Domaine"**. Cliquez sur cette URL. Il s'agit de votre application Web publique en direct !

![Capture d'écran de la console Amplify après un déploiement réussi montrant l'URL du "Domaine"](https://cdn.hashnode.com/res/hashnode/image/upload/v1752054574379/a42bc253-94a1-4bc2-a42c-f7f5444d964b.png align="center")

Figure 17 : Votre application Web de calculatrice de somme déployée avec son URL publique.

## Comment tester votre application : fonctionne-t-elle ?

Maintenant, la partie excitante – testons notre application Web entièrement serverless en suivant ces étapes :

1. **Ouvrez l'URL de votre application Amplify :** Naviguez vers l'URL de "Domaine" fournie par AWS Amplify (de l'étape 5.6).

2. **Saisissez des nombres :** Dans les champs de saisie "Nombre 1" et "Nombre 2", tapez deux nombres (par exemple, 5 et 10).

3. **Cliquez sur "CALCULER" :** Cliquez sur le bouton "CALCULER". Vous devriez voir brièvement "Calcul en cours..." sur le bouton.

4. **Observez le résultat :** Si tout est configuré correctement, vous devriez voir la boîte "Résultat du calcul" apparaître sous le formulaire, affichant l'ID de transaction, l'horodatage, les nombres et leur somme !

5. **Vérifiez dans DynamoDB (facultatif) :**

   * Retournez à votre console DynamoDB.

   * Cliquez sur votre `myTable`.

   * Cliquez sur l'onglet **"Explorer les éléments de la table"**.

   * Vous devriez maintenant voir de nouvelles entrées (éléments) correspondant à chaque calcul que vous avez effectué sur votre application Web, avec l'`ID`, l'`Horodatage`, `num1`, `num2` et `sum` stockés !

## Problèmes courants et solutions

Parfois, les choses ne fonctionnent pas parfaitement du premier coup. Voici quelques problèmes courants et comment les résoudre :

### **Erreurs CORS (Cross-Origin Resource Sharing) :**

* **Symptôme :** La console de développement de votre navigateur Web (généralement accessible en appuyant sur F12 ou en cliquant avec le bouton droit et en sélectionnant "Inspecter") affiche des erreurs comme "L'accès à fetch à '...' depuis l'origine '...' a été bloqué par la politique CORS : Aucun en-tête 'Access-Control-Allow-Origin' n'est présent..."

* **Solution :** Cela signifie que votre frontend n'est pas autorisé à communiquer avec votre API Gateway. Retournez à **l'étape 3, partie 5 (Activer CORS)** dans API Gateway et assurez-vous d'avoir activé CORS pour votre API. Assurez-vous que `POST` est sélectionné et que `Access-Control-Allow-Origin` est correctement configuré (pour ce tutoriel, `'*'` est acceptable, mais en production, vous spécifieriez votre domaine Amplify).

### **Délais d'exécution de Lambda :**

* **Symptôme :** Votre application Web continue d'afficher "Calcul en cours..." ou obtient une erreur générique, et dans les journaux de votre fonction Lambda (CloudWatch Logs), vous voyez "Task timed out".

* **Solution :** Votre fonction Lambda a mis trop de temps à s'exécuter. Pour une simple calculatrice de somme, cela est peu probable, mais pour des opérations plus complexes, vous devrez peut-être augmenter le paramètre "Timeout" pour votre fonction Lambda. Vous pouvez trouver cela sous l'onglet "Configuration" de votre fonction Lambda, dans la section "Configuration générale".

### **Erreurs de permissions DynamoDB :**

* **Symptôme :** L'exécution de votre fonction Lambda échoue, et dans ses journaux CloudWatch, vous voyez une erreur comme "User: arn:aws:sts::... is not authorized to perform: dynamodb:PutItem on resource: arn:aws:dynamodb:..."

* **Solution :** Cela signifie que votre fonction Lambda n'a pas les permissions nécessaires pour écrire dans votre table DynamoDB. Retournez à **l'étape 2, partie 2 (à propos de la mise à jour des permissions de la fonction Lambda)** et assurez-vous d'avoir correctement ajouté l'action `dynamodb:PutItem` et spécifié l'ARN de votre `myTable` comme ressource.

### **URL d'invocation incorrecte de l'API Gateway :**

* **Symptôme :** Votre frontend envoie une requête, mais elle échoue immédiatement, ou vous obtenez une erreur réseau dans la console du navigateur.

* **Solution :** Vérifiez que la constante `API_ENDPOINT` dans votre fichier `app.js` est *exactement* l'URL d'invocation que vous avez copiée depuis API Gateway. Même une petite faute de frappe peut rompre la connexion.

## Prochaines étapes : améliorez votre application

Cette calculatrice est un excellent point de départ, mais vous pouvez l'étendre considérablement :

* **Ajoutez une authentification :** Implémentez une connexion et une inscription d'utilisateur (par exemple, en utilisant AWS Amplify Auth avec Amazon Cognito) afin que seuls les utilisateurs autorisés puissent utiliser la calculatrice.

* **Implémentez une gestion des erreurs :** Rendez le frontend plus robuste en affichant des messages d'erreur spécifiques en fonction de ce que le backend envoie.

* **Créez une vue d'historique des calculs :** Étendez votre frontend pour récupérer et afficher une liste de tous les calculs passés stockés dans DynamoDB. Cela impliquerait une autre fonction Lambda et un point de terminaison API Gateway (par exemple, une méthode `GET`).

* **Ajoutez une validation des entrées :** Implémentez une validation plus robuste à la fois sur le frontend (JavaScript) et le backend (Lambda) pour gérer les entrées non numériques ou d'autres cas limites.

* **Implémentez des mises à jour en temps réel :** Utilisez AWS AppSync (GraphQL) ou WebSockets avec API Gateway pour pousser les nouveaux résultats de calcul vers le frontend en temps réel, sans avoir besoin de recharger la page.

## Conclusion

Félicitations ! Vous avez construit et déployé avec succès une application Web serverless entièrement fonctionnelle sur AWS. Vous avez vu comment exploiter des services puissants comme AWS Lambda, Amazon API Gateway, Amazon DynamoDB et AWS Amplify pour créer une application évolutive, rentable et nécessitant peu de maintenance.

Cette architecture est incroyablement puissante car elle peut se mettre à l'échelle automatiquement pour gérer des milliers, voire des millions d'utilisateurs, sans que vous ayez à gérer un seul serveur. N'oubliez pas de nettoyer vos ressources AWS lorsque vous avez terminé vos expériences pour éviter des frais inutiles.

### Ressources pour aller plus loin

* [Documentation AWS Lambda](https://aws.amazon.com/lambda/resources/) : Approfondissez les fonctions serverless.

* [Guide du développeur Amazon DynamoDB](https://www.google.com/search?q=https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Welcome.html) : En savoir plus sur les bases de données NoSQL.

* [Tutoriels Amazon API Gateway](https://www.google.com/search?q=https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-getting-started.html) : Explorez la construction de divers types d'API.

* [Documentation AWS Amplify](https://docs.amplify.aws/) : Découvrez plus de fonctionnalités pour construire et déployer des applications full-stack.