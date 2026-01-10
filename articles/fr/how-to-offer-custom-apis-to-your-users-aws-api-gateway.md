---
title: Comment offrir des API personnalisées à vos utilisateurs avec AWS API Gateway
subtitle: ''
author: Arunachalam B
co_authors: []
series: null
date: '2023-06-21T13:56:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-offer-custom-apis-to-your-users-aws-api-gateway
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/AWS-API-Gateway-Banner.png
tags:
- name: api
  slug: api
- name: AWS
  slug: aws
- name: Cloud Computing
  slug: cloud-computing
- name: serverless
  slug: serverless
seo_title: Comment offrir des API personnalisées à vos utilisateurs avec AWS API Gateway
seo_desc: "In the world of cloud computing and serverless architecture, AWS API Gateway\
  \ is a powerful tool that helps you build robust, secure, and scalable APIs. \n\
  In this tutorial, I'll introduce you to API Gateway and explain the benefits of\
  \ using this helpfu..."
---

Dans le monde de l'informatique en nuage et de l'architecture serverless, AWS API Gateway est un outil puissant qui vous aide à construire des API robustes, sécurisées et évolutives. 

Dans ce tutoriel, je vais vous présenter API Gateway et expliquer les avantages de l'utilisation de cet outil utile. Ensuite, je vous montrerai comment créer et déployer une API Rest, et créer des plans d'utilisation pour offrir des clés API. Très bien, commençons. 

## Qu'est-ce que API Gateway ?

AWS API Gateway est un service entièrement géré fourni par Amazon Web Services (AWS) qui simplifie la création, le déploiement et la gestion des API à toute échelle. 

Il agit comme une porte d'entrée pour les applications et vous permet de créer des API qui servent de ponts entre les clients et les services back-end. Cela permet une communication sécurisée et efficace.

## Pourquoi avez-vous besoin de API Gateway ?

AWS API Gateway offre de nombreux avantages pour les entreprises et les développeurs. Voici quelques avantages de l'utilisation de API Gateway. 

### Évolutivité et haute disponibilité

Avec AWS API Gateway, la mise à l'échelle de vos API devient beaucoup plus facile. Il gère de manière transparente les pics de trafic en mettant à l'échelle automatiquement l'infrastructure sous-jacente. Cela entraîne une haute disponibilité et aide à prévenir les interruptions de service.

### Sécurité et authentification

API Gateway offre des fonctionnalités de sécurité robustes, y compris des mécanismes d'authentification et d'autorisation intégrés. 

Il prend en charge l'authentification des utilisateurs via les rôles IAM pour les applications internes, Cognito pour les applications externes (par exemple, les utilisateurs mobiles), et il prend également en charge les autorisateurs personnalisés. 

### Intégration avec d'autres services AWS

En tant que partie de l'écosystème AWS, API Gateway s'intègre de manière transparente avec une gamme d'autres services AWS. Cela vous permet de tirer parti de fonctionnalités supplémentaires comme les fonctions AWS Lambda, AWS Cognito pour la gestion des utilisateurs, et AWS CloudWatch pour la surveillance et la journalisation.

### Gestion du cycle de vie des API

Avec API Gateway, vous pouvez facilement versionner, déployer et gérer différentes étapes de vos API. Cela simplifie le processus de déploiement des mises à jour, de test de nouvelles fonctionnalités et de gestion de différents environnements tels que le développement, la pré-production et la production.

J'espère que vous avez maintenant compris ce qu'est API Gateway et pourquoi il est précieux. Plongeons dans la création de notre propre API Gateway.

## Comment créer une AWS API Gateway

Dans cette section, nous allons :

* Créer une API Rest avec la méthode GET
* L'intégrer avec une simple fonction lambda hello world et la déployer

Commençons par créer une fonction lambda

## Comment créer une fonction AWS Lambda

Connectez-vous à la console de gestion AWS [Console](https://console.aws.amazon.com/) et recherchez "Lambda" dans la barre de recherche de la console de gestion AWS. Cliquez sur Créer une fonction. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-145.png)
_Naviguer vers la console AWS Lambda_

Sélectionnez l'option "Créer à partir de zéro", entrez un nom pour votre fonction lambda, sélectionnez l'environnement d'exécution "Python" et cliquez sur le bouton Créer une fonction en bas à droite. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-146.png)
_Créer une fonction AWS Lambda_

Une fois la fonction créée, mettez à jour le code suivant et déployez les modifications :

```python
import json

def lambda_handler(event, context):
    body = "Hello from 5minslearn!"
    statusCode = 200
    return {
        "statusCode": statusCode,
        "body": json.dumps(body),
        "headers": {
            "Content-Type": "application/json"
        }
    }
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-147.png)
_Déployer une fonction Lambda_

Félicitations ! Vous avez créé avec succès une fonction AWS Lambda. Maintenant, créons l'API Rest. 

## Comment créer une API Rest et l'intégrer avec AWS Lambda

Recherchez API Gateway dans la barre de recherche. Dans la section API REST, cliquez sur le bouton Build. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-183.png)
_Créer une API Rest_

Choisissez le protocole comme Rest et sélectionnez Nouvelle API dans la section Créer une nouvelle API. Dans la section des paramètres, entrez le nom de l'API de votre choix et laissez le type de point de terminaison par défaut. Ensuite, cliquez sur le bouton Créer une API. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-148.png)
_Configurer la création d'une API Rest_

Cliquez sur le bouton Actions en haut à gauche. Ensuite, cliquez sur Méthode et sélectionnez la méthode comme GET et cliquez sur l'icône de validation. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-149.png)
_Créer une méthode_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-150.png)
_Choisir la méthode "GET"_

Sélectionnez Fonction Lambda comme type d'intégration et entrez le nom de la fonction Lambda que vous avez créée précédemment. Ensuite, enregistrez la fonction. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-151.png)
_Sélectionner la configuration de la méthode_

Une fois que vous cliquez sur enregistrer, "Ajouter une permission à la fonction Lambda" demandera une confirmation. Cela signifie essentiellement que vous autorisez API Gateway à invoquer une fonction Lambda. Dans ce cas, il s'agit de la fonction Lambda "DemoFunction". Acceptez la confirmation et passez à l'étape suivante. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-152.png)
_Autoriser la permission d'invoquer la fonction Lambda depuis API Gateway_

Cliquez sur Test. Cela vous mènera à une nouvelle page. Cliquez sur le bouton "Test". Vous pourrez voir la réponse de la fonction Lambda dans le panneau de droite. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-153.png)
_Notre architecture API_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-184.png)
_Tester notre API Gateway_

Maintenant que vous avez testé avec succès votre API, vous êtes prêt à déployer l'API. Pour déployer l'API, cliquez à nouveau sur le bouton Actions et cliquez sur Déployer l'API. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-185.png)
_Déployer l'API Gateway_

La boîte de dialogue Déployer l'API s'ouvrira. Sélectionnez Nouveau stade pour l'étape de déploiement et nommez-le comme vous le souhaitez. Cliquez sur le bouton Déployer. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-155.png)
_Configurer le déploiement de l'API Gateway_

Cliquez sur l'URL d'invocation affichée en haut. Vous pouvez voir la réponse de la fonction Lambda. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-156.png)
_API Gateway créée_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-186.png)
_Tester notre API_

Super ! Nous avons créé avec succès l'API Rest, l'avons intégrée avec la fonction Lambda et l'avons déployée.

Mais vous pouvez faire cela avec plusieurs services disponibles sur le marché. Pourquoi choisiriez-vous AWS API Gateway ? 

Eh bien. C'est une question intéressante. Tout d'abord, vous pouvez configurer le plan d'utilisation pour votre API. Le meilleur, c'est que vous n'avez pas à écrire de code pour cela. 

Maintenant, créons un plan d'utilisation, générons une clé API et rendons notre API Rest accessible uniquement en passant la clé API dans l'en-tête. 

## Comment créer un plan d'utilisation d'API Gateway

Dans la barre latérale de gauche, cliquez sur Plans d'utilisation et cliquez sur le bouton Créer. Entrez le nom de votre plan – j'ai choisi "Basique". Entrez les sections Limitation de débit et Quota selon vos besoins et cliquez sur Suivant. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-159.png)
_Créer un plan d'utilisation AWS API Gateway_

Cliquez sur le bouton Ajouter une étape d'API. Sélectionnez l'API et son étape. Cliquez sur l'icône de validation dans le coin droit et sélectionnez Suivant. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-from-2023-06-19-10-46-19.png)
_Créer une étape pour notre API_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-164.png)
_Créer une étape pour notre API_

Cliquez sur Créer une clé API et ajouter au plan d'utilisation. Une fenêtre modale s'ouvrira. Entrez le nom de la clé API. Pour la clé API, j'ai sélectionné Générer automatiquement, mais si vous souhaitez donner une clé personnalisée, vous pouvez entrer une clé personnalisée. Cliquez sur le bouton Enregistrer. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-160.png)
_Créer une clé API pour accéder au service_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-161.png)
_Configurer la clé API_

Sélectionnez Ressources dans la barre latérale, cliquez sur l'API GET que vous venez de créer, et cliquez sur la demande de méthode. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-162.png)
_Sélectionner la méthode_

Dans la section Paramètres, mettez à jour le champ Clé API requise à vrai et cliquez sur l'icône de validation. Une fois mis à jour, n'oubliez pas de déployer les modifications en cliquant sur le menu déroulant Actions. Vos modifications ne seront pas mises à jour sinon. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-187.png)
_Activer le champ Clé API requise_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-165.png)
_Déployer l'API_

Cliquez maintenant sur la même URL et voyez la magie. 

Interdit !

Parce que notre couche API est maintenant protégée. Vous devez passer la clé API dans l'en-tête pour accéder aux données. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-163.png)
_Accès interdit si aucune clé API n'est fournie_

Maintenant, cliquez sur les Plans d'utilisation dans la barre latérale. Sélectionnez votre plan et accédez à l'onglet Clés API. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-166.png)
_Accéder à votre clé API_

Cliquez sur la clé API que vous avez créée à l'étape 3. Cliquez sur Afficher. Copiez la clé API. 

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-188.png)
_Liste des clés API_

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-167.png)
_Révéler votre clé API_

Vous devez passer la clé API dans l'en-tête 'x-api-key'. Passons au terminal pour tester cela. 

Vérifiez votre API Rest sans passer la clé API au début. Ouvrez le terminal et entrez la commande curl suivante. Vous verrez une fois de plus le message interdit. 

```bash
curl --location --request GET '[entrez votre URL d\'invocation]'
--header 'Content-Type: application/json
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-189.png)
_Accès interdit sans clé API dans le terminal_

Maintenant, passez la clé API cette fois. Exécutez la commande curl suivante :

```bash
curl --location --request GET '[votre URL d\'invocation]' \
--header 'x-api-key: [votre clé API]' \
--header 'Content-Type: application/json' \
--data-raw ''
```

![Image](https://www.freecodecamp.org/news/content/images/2023/06/image-190.png)
_Données reçues en passant la clé API dans l'en-tête x-api-key_

Vous pouvez voir la sortie de la fonction Lambda car vous avez passé 'x-api-key' dans l'en-tête. 

Super ! Vous avez créé avec succès le plan d'utilisation, généré la clé API, et l'avez attachée à la méthode de l'API Rest et vérifié l'intégration. 

## Conclusion

Dans ce tutoriel, vous avez appris ce qu'est AWS API Gateway et comment créer des plans d'utilisation pour l'API Rest. 

Si vous souhaitez en savoir plus sur les services AWS, abonnez-vous à ma [newsletter par email](https://5minslearn.gogosoon.com/?ref=fcc_aws_api_gateway) ([https://5minslearn.gogosoon.com/](https://5minslearn.gogosoon.com/?ref=fcc_aws_api_gateway)) et suivez-moi sur les réseaux sociaux.