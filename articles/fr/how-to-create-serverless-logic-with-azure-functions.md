---
title: Comment créer une logique Serverless avec Azure Functions
subtitle: ''
author: Salim Oyinlola
co_authors: []
series: null
date: '2022-09-26T22:35:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-serverless-logic-with-azure-functions
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/pexels-sagui-andrea-618833.jpg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
- name: serverless
  slug: serverless
seo_title: Comment créer une logique Serverless avec Azure Functions
seo_desc: "What is Serverless Computing?\nServerless computing is a cloud computing\
  \ model where backend services are provided on a pay-as-you-use basis. \nIn this\
  \ model, developers get to create and run development code without having to manage\
  \ or provision serve..."
---

## **Qu'est-ce que le Serverless Computing ?**

Le serverless computing est un modèle de cloud computing où les services backend sont fournis sur la base d'un paiement à l'usage.

Dans ce modèle, les développeurs peuvent créer et exécuter du code de développement sans avoir à gérer ou à provisionner des serveurs. Ainsi, ils peuvent se concentrer uniquement sur l'écriture du code de la logique métier (ou du développement front-end).

Microsoft Azure propose une large gamme d'options pour concevoir ce type d'architecture. Cependant, les méthodes les plus fréquemment utilisées sont Azure Logic Apps et Azure Functions, qui seront le sujet principal de cet article.

## **Que sont les Azure Functions ?**

Azure Functions est le modèle de serverless computing sur la plateforme Microsoft Azure pour créer des applications sans serveur. Il permet aux développeurs d'héberger leur logique métier sans avoir besoin d'infrastructure.

Le code des Azure Functions peut être écrit dans une large gamme de langages de programmation, notamment C#, JavaScript et Python, entre autres. Comme d'autres services cloud, il fonctionne sur la base d'un paiement à l'usage, où vous ne payez que pour les ressources que vous consommez.

À la fin de ce tutoriel, vous serez en mesure de :

* Créer une application Azure Function dans le portail Azure.
* Utiliser une fonction à l'aide de déclencheurs (triggers).
* Surveiller et tester votre Azure Function depuis le portail Azure.

### **Prérequis**

Vous aurez besoin d'un compte Microsoft Azure valide et actif pour suivre ce tutoriel. Vous pouvez utiliser soit :

* [Essai gratuit Azure](https://azure.microsoft.com/en-us/free/) : Avec cette option, vous commencerez avec un crédit Azure de 200 $ et aurez 30 jours pour l'utiliser, en plus des services gratuits.
* [Azure pour les étudiants](https://azure.microsoft.com/en-us/free/students/) : Cette offre est réservée aux étudiants. Avec cette option, vous commencerez avec un crédit Azure de 100 $ sans carte de crédit requise et aurez accès gratuitement aux services populaires tant que vous disposez de votre crédit.

## **Étape 1 – Créez votre application Azure Function**

Pour établir une ressource de serverless computing pour votre logique métier à l'aide d'Azure Functions, il est essentiel de créer une application Azure Function. Après avoir créé un compte Microsoft Azure valide et actif, accédez au [portail](https://portal.azure.com/).

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-128.png)

* Sélectionnez `Create a resource`.
* Sélectionnez le bouton `Create` sous le volet `Function App`.
* En cliquant sur le bouton, une page où vous saisissez les détails de votre projet apparaît comme indiqué ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-129.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-130.png)

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-131.png)

Saisissez les détails de configuration pour ce tutoriel sous l'onglet `Basics` avant de cliquer sur le bouton `Review + create` :

* Saisissez l'abonnement (`Subscription`) disponible sur votre compte. Notez que votre abonnement peut ne pas être `Visual Studio Enterprise Subscription` comme le mien.
* Pour le groupe de ressources (`Resource group`), si vous en avez déjà créé un, vous pouvez l'utiliser. Cependant, si vous n'en avez pas créé ou si vous n'êtes pas familier avec les groupes de ressources Azure, créez-en un nouveau en utilisant le bouton `Create new`.

Fondamentalement, un groupe de ressources est utilisé pour regrouper des services Azure similaires sur votre abonnement Azure afin de faciliter leur gestion.

* Pour l'option `Function App name`, saisissez un nom d'application unique au niveau mondial. Il est important de noter que ce nom fera partie de l'URL de base de votre service.
* Pour l'option `Publish`, sélectionnez `Code`.
* Choisissez `Node.js` pour l'option `Runtime Stack` puisque les exemples de fonctions de ce tutoriel ont été implémentés en utilisant ce langage.
* Laissez l'option `Version` par défaut.
* Sélectionnez la région géographiquement la plus proche de vous lors du choix de la `Region`. Une région est un ensemble de centres de données physiques. Étant basé à Lagos, au Nigeria, j'ai choisi `South Africa North`.
* Pour le `Operating System`, sélectionnez celui qui est conforme à votre sélection de runtime.
* Pour l'option `Plan`, sélectionnez `Consumption (Serverless)`. Le plan que vous choisissez déterminera comment votre application évolue et quelles fonctionnalités sont activées.
* À ce stade, vous pouvez cliquer sur le bouton `Review + create`.

Le processus de validation et de déploiement prend généralement jusqu'à trois minutes. Lorsque les processus de validation et de déploiement sont tous deux terminés pour la configuration de l'Azure Function, vous pouvez alors vérifier que votre application Azure Function est en cours d'exécution.

## **Étape 2 – Vérifiez que votre application Azure Function est en cours d'exécution**

Une fois le processus de déploiement terminé, sélectionnez `Go to resource`. Le volet de votre application de fonction apparaîtra alors. Pour l'ouvrir dans un navigateur, sélectionnez le lien `URL` dans la section `Essentials`.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-132.png)

Avec le message ci-dessus, vous verrez apparaître une page d'application web Azure Functions standard : _Your Function 4.0 app is up and running._

## **Étape 3 – Exécutez votre code à la demande avec Azure Functions**

L'application de fonction étant créée, l'étape suivante consiste à construire et configurer la fonction. Pour ce faire, vous devez comprendre ce que sont les Triggers (déclencheurs) et les Bindings (liaisons).

> Les déclencheurs (Triggers) provoquent l'exécution d'une fonction. Un déclencheur définit comment une fonction est invoquée et une fonction doit avoir exactement un seul déclencheur. Les déclencheurs ont des données associées, qui sont souvent fournies comme la charge utile (payload) de la fonction. La liaison (Binding) à une fonction est un moyen de connecter de manière déclarative une autre ressource à la fonction ; les liaisons peuvent être connectées en tant que *liaisons d'entrée* (input bindings), *liaisons de sortie* (output bindings), ou les deux. Les données des liaisons sont fournies à la fonction en tant que paramètres. – [Documentation Microsoft Learn](https://learn.microsoft.com/en-us/azure/azure-functions/functions-triggers-bindings?tabs=csharp)

En général, les Azure Functions s'exécutent en réponse à un événement. Cet événement est connu sous le nom de **Trigger** et les **Bindings** sont utilisés pour connecter des ressources à une fonction. Les déclencheurs typiques sur Azure vont d'un stockage blob qui exécute une fonction lorsqu'un blob est créé ou mis à jour, à un minuteur qui exécute une fonction selon un calendrier.

Pour exécuter votre code sur Azure Functions, vous devez d'abord créer votre fonction pour exécuter votre code au sein de l'application de fonction en utilisant le modèle.

Pour ce faire, cliquez sur l'onglet `Function` dans la barre de menu à gauche de la page d'accueil de votre application de fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-134.png)

* Cliquez sur le bouton `+ Create` pour créer la fonction.
* Sélectionnez le modèle `Azure Queue Storage trigger`. Ce déclencheur exécute l'application de fonction lorsqu'il détecte qu'un message a été ajouté à une file d'attente de stockage Azure.
* Laissez tout le reste à sa valeur par défaut.
* Cliquez sur le bouton `Create` pour créer la fonction.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-135.png)

Étant donné que la fonction a été créée avec un modèle, plusieurs autres fichiers seront créés automatiquement. Ces fichiers comprennent un code source et un fichier de configuration.

* Cliquez sur le bouton `Code + Test` dans le volet de gauche et ouvrez le fichier `function.json` en le sélectionnant dans la liste déroulante.
* Remplacez le bloc de code affiché par celui ci-dessous.

```python
{
  "bindings": [
    {
      "name": "order",
      "type": "queueTrigger",
      "direction": "in",
      "queueName": "myqueue-items",
      "connection": "MY_STORAGE_ACCT_APP_SETTING"
    },
    {
      "name": "$return",
      "type": "table",
      "direction": "out",
      "tableName": "outTable",
      "connection": "MY_TABLE_STORAGE_ACCT_APP_SETTING"
    }
  ]
}
```

Ce bloc de code définit le déclencheur de la fonction comme étant **lorsqu'un message est ajouté à la file d'attente nommée `myqueue-items`.** De plus, il envoie la valeur de retour à la `outTable`.

* Enregistrez et utilisez _Test/Run_ sur la fonction tout en laissant les détails de test à leurs valeurs par défaut et exécutez l'application de fonction.
* Vous verrez le résultat affiché ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2022/10/image-136.png)

Le fait que le résultat s'affiche automatiquement sur l'**onglet Output** suggère que l'application de fonction fonctionne bien. Comme aucune logique métier n'est appliquée à la fonction, l'image ci-dessus est vide.

## **Conclusion**

Dans ce tutoriel, vous avez vu que le serverless computing est une excellente option pour héberger du code de logique métier dans le cloud. Vous avez vu qu'avec des offres serverless telles qu'Azure Functions, vous pouvez écrire votre logique métier dans le langage de votre choix.

De plus, il est important de noter que non seulement l'utilisation de solutions de serverless computing évite la sur-allocation d'infrastructure (car elles peuvent être créées et détruites à la demande), mais elles sont également pilotées par les événements (event driven). Pilotées par les événements dans le sens où elles ne s'exécutent qu'en réponse à un événement (appelé « trigger »), tel qu'un message ajouté à une file d'attente ou la réception d'une requête HTTP.

Enfin, je partage mes écrits sur [Twitter](https://twitter.com/SalimOyinlola) si vous avez apprécié cet article et souhaitez en voir plus.