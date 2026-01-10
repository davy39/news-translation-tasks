---
title: Une introduction rapide aux proxies de fonction Azure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-08-28T07:36:53.000Z'
originalURL: https://freecodecamp.org/news/introduction-to-azure-function-proxies
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/Azure-Functions-Proxies.jpg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
seo_title: Une introduction rapide aux proxies de fonction Azure
seo_desc: "By Nadeem Ahamed\nIn this article, we'll discuss Azure Function Proxies.\
  \ They provide “Reverse Proxy Functionality” for Azure Functions. Azure Function\
  \ Proxies are quite similar to Azure API management.  \nThis post is largely inspired\
  \ by Matthew Hende..."
---

Par Nadeem Ahamed

Dans cet article, nous allons discuter des proxies de fonction Azure. Ils fournissent une « Fonctionnalité de Proxy Inverse » pour les fonctions Azure. Les proxies de fonction Azure sont assez similaires à la gestion des API Azure. 

Cet article est largement inspiré par Matthew Henderson de l'équipe Microsoft Azure Function. Dans son article de blog, [Azure Functions Proxies public preview](https://blogs.msdn.microsoft.com/appserviceteam/2017/02/22/azure-functions-proxies-public-preview/), Matthew explique la raison pour laquelle Microsoft a eu l'idée des proxies de fonction Azure.

## **Qu'est-ce que les proxies de fonction Azure ?**

L'idée de base derrière les proxies de fonction Azure est qu'ils nous permettent de définir une seule surface API pour plusieurs applications de fonction. Maintenant, toute application de fonction peut définir un point de terminaison qui sert de proxy inverse pour une autre API. Le point de terminaison peut être une application de fonction ou cela peut être autre chose. 

Êtes-vous à la recherche d'un outil prêt à l'emploi pour gérer et surveiller vos fonctions Azure ? [Essayez celui-ci gratuitement ici](http://bit.ly/2L6eEmM).

## **Raison de la mise en œuvre des proxies de fonction Azure**

Pour certains utilisateurs, il est difficile de gérer de grandes solutions avec une seule application de fonction. Il y a un ensemble d'organisations utilisant les fonctions Azure dans leur architecture de micro-services avec un déploiement entre les composants individuels. Dans ce cas, chaque application de fonction a son propre hébergement, donc il y a de nombreuses applications de fonction différentes à suivre. 

Nous pourrions également avoir certaines applications de fonction combinées avec une autre API, mais elles pourraient se trouver dans diverses régions différentes. Nous finissons donc par transmettre beaucoup de cette complexité à notre client ou système consommateur.

Les proxies de fonction Azure viennent à la rescousse en fournissant un URI unifié (Uniform Resource Identifier) que le client peut réellement consommer. En attendant, nous pouvons abstraire toutes les différentes applications de fonction ou autres API, et cela nous permettrait également de construire notre API à un rythme plus rapide.

## **Explication**

![Azure Function Proxies](https://www.serverless360.com/wp-content/uploads/2018/07/Solution-Architecture-Diagram.png)

Dans le diagramme d'architecture de solution ci-dessus, nous avons un proxy de fonction Azure suivi d'une fonction Azure et d'une file d'attente de bus de service en back-end pour stocker les informations. À l'autre extrémité du diagramme, nous avons des éditeurs de données. Aux fins de cette discussion, disons que l'équipement électrique génère l'événement de balise et le transmet aux fonctions Azure via le proxy.

Initialement, nous créons une application de fonction en sélectionnant l'option de fonction dans le portail Azure. Ici, disons que nous créons un déclencheur HTTP pour C# où la fonction du déclencheur HTTP est d'invoquer une fonction avec une requête HTTP. 

Maintenant, nous créons deux fonctions : l'une est PostTag qui représente notre publication si nous voulons créer une balise. Le code pour la fonction PostTag est le suivant :

![Post Tag](https://www.serverless360.com/wp-content/uploads/2018/07/Post-Tag.png)

Ensuite, nous créons une autre fonction appelée GetTag avec le code spécifié comme suit :

![Get Tag](https://www.serverless360.com/wp-content/uploads/2018/07/Get-Tag.png)

Nous utilisons GetTag pour extraire le message de la file d'attente, et la dernière valeur de balise est retournée au client.

Nous pouvons sélectionner le lien spécifié ci-dessous pour récupérer l'URL des deux fonctions. Ce lien nous fournira un jeton de sécurité pour l'autorisation.

![To Get Function URL](https://www.serverless360.com/wp-content/uploads/2018/07/To-Get-Function-URL.png)

À ce stade, nous passons aux paramètres de l'application de fonction et activons les proxies de fonction Azure qui ont la dernière version du runtime proxy 0.2. Par conséquent, nous sélectionnons l'option « Nouveau Proxy » dans le développement de l'application de fonction, ce qui nous permet de créer deux proxies. Ils sont Proxy GetTag et Proxy PostTag. Les options disponibles dans le proxy sont :

* URL du Proxy
* Modèle de Route
* URL Backend

L'URL spécifiée dans l'URL du Proxy et le Modèle de Route sont les mêmes concernant les événements GetTag et PostTag. L'URL Backend du Proxy GetTag sera liée à l'événement GetTag - mais pour le Proxy PostTag, elle sera liée à l'événement PostTag.

## Conclusion

Les proxies de fonction Azure sont un excellent moyen de simuler et de tester votre point de terminaison de fonctions Azure même avant que le développement réel du back-end ne commence. De plus, ils peuvent même être utilisés en production lorsque vous devez router un URI vers un autre.

Je voudrais conclure que les proxies de fonction Azure sont l'une des fonctionnalités les plus engageantes et prêtes pour le marché que l'équipe des fonctions Azure a fournies.

Ce blog a été initialement publié dans [Serverless360](http://bit.ly/2ZkPmLZ).