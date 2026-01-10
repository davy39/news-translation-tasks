---
title: Comment mieux protéger vos secrets dans Logic Apps à l'aide du connecteur Key
  Vault
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-30T08:46:35.000Z'
originalURL: https://freecodecamp.org/news/how-to-better-protect-your-secrets-in-logic-apps-using-key-vault-connector
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/secret-banner.png
tags:
- name: Azure
  slug: azure
- name: Logic Apps
  slug: logic-apps
- name: serverless
  slug: serverless
seo_title: Comment mieux protéger vos secrets dans Logic Apps à l'aide du connecteur
  Key Vault
seo_desc: 'By Nadeem Ahamed

  One of the key challenges that users face while using Logic Apps is managing secret
  values. This used to be handled by passing the secrets through ARM templates, which
  is not an out of the box solution.

  Before the availability of the...'
---

Par Nadeem Ahamed

L'un des principaux défis auxquels les utilisateurs sont confrontés lors de l'utilisation de [Logic Apps](https://www.serverless360.com/azure-logic-apps) est la gestion des valeurs secrètes. Cela était auparavant géré en passant les secrets via des modèles ARM, ce qui n'est pas une solution prête à l'emploi.

Avant la disponibilité du connecteur Key Vault dans Logic Apps, [l'une des solutions de contournement idéales](https://www.serverless360.com/blog/managing-secrets-in-azure-logic-apps-using-managed-identities) consistait à utiliser une action HTTP disponible dans Logic Apps et à exploiter le mode d'authentification Managed Identity. Même cette solution de contournement présente quelques considérations comme suit :

1. L'historique d'exécution de Logic App contient les valeurs secrètes qui ne peuvent pas être masquées
2. Actuellement, nous ne pouvons avoir que 10 Logic Apps avec des identités managées attribuées par le système

Explorons comment mieux protéger vos secrets dans vos Logic Apps à l'aide du nouveau connecteur Key Vault. De plus, je vais vous montrer comment le problème ci-dessus peut être résolu avec le connecteur Key Vault.

## Concevez votre Logic App d'exemple

Suivez les étapes ci-dessous pour créer votre Logic App d'exemple dans la page de conception.

1. Ajoutez un déclencheur "Http request" à la Logic App. Plus tard, nous appellerons cette Logic App via un client REST.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p1.png)

2. Ensuite, recherchez les actions de Key Vault et ajoutez l'action "Get Secret" à la Logic App. Vous avez maintenant plusieurs options ici pour l'authentification : soit vous pouvez utiliser **Azure AD**, soit [**Service Princip**](https://docs.microsoft.com/en-us/azure/active-directory/develop/howto-create-service-principal-portal)**al**. Dans cet exemple, je vais utiliser le service Azure AD.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p2.png)

3. Connectez-vous avec votre compte. Ce compte doit avoir suffisamment de permissions pour accéder à votre Key Vault. Sinon, vous devez fournir manuellement l'accès via les **Access policies**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p3.png)

4. Remplissez le champ requis avec le "<secret name>". Si vous n'en avez pas déjà un, vous pouvez en créer un en vous rendant dans le menu Key Vault. Là, vous pouvez trouver l'option "secrets" dans le volet de gauche.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p4.png)

> _Note : Si vous provisionnez le Key Vault lui-même pour la première fois, rappelez-vous : parfois, vous devrez peut-être enregistrer le service Key Vault à votre abonnement manuellement. (J'ai rencontré ce problème lorsque je l'ai fait pour la première fois)._

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p5.png)

5. Maintenant, ajoutez l'action "Http response" à la Logic App. Remplissez les champs suivants comme suit :  
  
**Status Code** : 200  
**Body** : <ajoutez l'expression dynamique : The Secret>

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p6.png)

6. Enregistrez la Logic App.

## Test de la Logic App

Maintenant, copiez l'URL HTTP POST du déclencheur Logic App et rendez-vous sur [reqbin](https://reqbin.com/) (client REST en ligne). Collez l'URL dans le champ d'adresse et changez la méthode par défaut de **GET** à **POST** et cliquez sur Send. 

La Logic App aurait été déclenchée et aurait renvoyé le code de réponse 200 avec la valeur secrète comme montré dans l'image ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p7.png)

## Inspection de l'historique d'exécution

En inspectant l'historique d'exécution de la Logic App, nous remarquons que les valeurs secrètes sont visibles en texte brut. 

Vous vous souvenez du même problème que nous avons rencontré dans la méthode classique ? Comme je l'ai déjà dit, cela peut être facilement résolu via les paramètres du connecteur Key Vault en suivant les étapes ci-dessous :

1. Retournez à la page de conception et cliquez sur l'option des paramètres sous le menu "more options" dans le connecteur Key Vault.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p8.png)

2. Maintenant, dans les paramètres de l'action "Get Secret", activez l'option Secure **Inputs** et **Outputs** et cliquez sur Done.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p9.png)

3. Une fois de plus, enregistrez la Logic App et appelez-la via le client REST (reqbin.com). Vous obtiendrez la même réponse dans le Request Bin, mais l'historique d'exécution ne contient pas les valeurs secrètes en format texte brut. Au lieu de cela, il affiche "Content not shown due to security configuration".  


![Image](https://www.freecodecamp.org/news/content/images/2020/03/p10.png)

Nous avons maintenant résolu la première préoccupation de la méthode classique. La deuxième préoccupation était que nous ne pouvons avoir que 10 Logic Apps avec des identités managées attribuées par le système.

Nous avons également surmonté ce problème en n'utilisant pas le mode d'authentification Managed Identity dans le connecteur. Au lieu de cela, il s'authentifie via Azure Active Directory ou Service Principal (ce qui a l'inconvénient de faire tourner les secrets, cependant). 

Une fois que l'utilisateur obtient suffisamment de permissions pour le Key Vault via Access Policy, il pourra accéder au Key Vault dans n'importe quel nombre de Logic Apps.

## Ensemble de fonctionnalités étendu

En explorant davantage les actions Key Vault de Logic Apps, j'ai trouvé quelques cas d'utilisation intéressants qui peuvent être réalisés via les actions de chiffrement et de déchiffrement.

Si l'utilisateur est plus préoccupé par ses données, il peut utiliser les actions de chiffrement et de déchiffrement pour garder les valeurs plus sécurisées.

Pour ce faire, créez une clé de chiffrement dans le Key Vault.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p11.png)

En utilisant les actions Encrypt et Decrypt dans les connecteurs Key Vault, vous pouvez chiffrer les données et les déchiffrer à nouveau. Comme vu ci-dessus, nous pouvons même activer l'option Secure Inputs et Outputs dans les paramètres pour les rendre plus sécurisées.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/p12.png)

## Gérer et surveiller Logic Apps avec Serverless360

[Serverless360](https://www.serverless360.com/) est une plateforme pour gérer et surveiller toutes vos ressources Azure Serverless, avec pour objectif d'aider vos opérations et de soutenir votre équipe au quotidien.

_Considérez le flux de travail ci-dessus d'une application métier définie à l'aide de plusieurs Azure Logic Apps._ 

Les différentes parties prenantes de l'application métier auront des besoins différents lorsqu'elles [gèrent et surveillent les Azure Logic Apps](https://www.serverless360.com/azure-logic-apps-monitoring-management). 

Quelques exigences clés qui sont difficiles à réaliser via le portail Azure sont :

* corriger automatiquement l'état de la Logic App lorsqu'il n'est pas celui attendu
* réflexion instantanée de l'état d'avertissement et d'erreur de la Logic App dans une vue de carte de service
* détection quasi en temps réel des échecs
* automatisation de la rémission d'actions spécifiques ayant échoué
* suivi de bout en bout du message circulant dans les Logic Apps, et 
* évaluation de la consommation, des performances et de la fiabilité. 

Ces exigences ne peuvent pas être réalisées directement via le portail Azure. Mais [Serverless360](https://www.serverless360.com/) peut compléter le portail Azure, car il est conçu avec des capacités pour combler les lacunes du portail Azure.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Topology.png)
_Carte de service dans Serverless360_

## Conclusion

Dans ce blog, nous avons vu les méthodes classiques et récentes pour protéger vos secrets dans Logic Apps. De plus, j'espère que ce blog vous a donné une compréhension plus claire du connecteur Key Vault qui est maintenant disponible.

Enfin, j'ai couvert les ensembles de fonctionnalités étendus du connecteur Key Vault de Logic Apps, les actions de chiffrement et de déchiffrement.

J'espère que vous avez apprécié la lecture de cet article. Bon apprentissage !