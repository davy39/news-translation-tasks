---
title: Comment gérer les logs dans les microservices
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-12T16:31:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-logs-in-microservices
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/Microservice-Observability
seo_title: Comment gérer les logs dans les microservices
---

Logs.png
tags:
- name: journalisation
  slug: journalisation
- name: Microservices
  slug: microservices
seo_title: null
seo_desc: 'Par Siben Nayak

  La journalisation est l'une des parties les plus importantes des systèmes logiciels. Que vous veniez de commencer à travailler sur un nouveau logiciel, ou que votre système fonctionne dans un environnement de production à grande échelle, vous vous retrouverez toujours à chercher de l'aide dans les fichiers de log. '
---

Par Siben Nayak

La journalisation est l'une des parties les plus importantes des systèmes logiciels. Que vous veniez de commencer à travailler sur un nouveau logiciel, ou que votre système fonctionne dans un environnement de production à grande échelle, vous vous retrouverez toujours à chercher de l'aide dans les fichiers de log.

Pour cette raison, les logs sont la première chose que les développeurs recherchent lorsqu'un problème survient ou qu'un système ne fonctionne pas comme prévu.

Journaliser les bonnes informations de la bonne manière facilite grandement la vie des développeurs. Et pour mieux maîtriser la journalisation, il faut savoir quoi et comment journaliser.

Dans cet article, nous allons examiner quelques règles de base en matière de journalisation qui peuvent vous aider à tirer le meilleur parti de vos logs.

# Que journaliser et comment fonctionne la journalisation

Commençons par un exemple de système de commerce électronique et examinons la journalisation dans son service de gestion des commandes (OMS).

Supposons qu'une commande client échoue en raison d'une erreur provenant du service de gestion des stocks (IMS), un service en aval que l'OMS utilise pour vérifier les stocks disponibles.

Supposons que l'OMS ait déjà accepté une commande. Mais lors de l'étape de vérification finale, l'IMS retourne l'erreur suivante parce que le produit n'est plus disponible dans l'inventaire.

`404 Product Not Available`

## Que journaliser

Normalement, vous journaliseriez l'erreur de cette manière :

```java
log.error("Exception in fetching product information - {}", ex.getResponseBodyAsString())
```

Cela produira un log dans le format suivant :

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in fetching product information - Product Not Available
```

Eh bien, il n'y a pas beaucoup d'informations disponibles dans cette déclaration de log, n'est-ce pas ? Un log comme celui-ci ne sert pas à grand-chose car il manque toute information contextuelle sur l'erreur.

Pouvons-nous ajouter plus d'informations à ce log pour le rendre plus pertinent pour le débogage ? Que diriez-vous d'ajouter l'ID de commande et l'ID de produit ?

```java
log.error("Exception in processing Order #{} for Product #{} due to exception - {}", orderId, productId, ex.getResponseBodyAsString())
```

Cela produira un log dans le format suivant :

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #182726 for Product #21 due to exception - Product Not Available
```

Maintenant, cela a beaucoup plus de sens ! En regardant les logs, nous pouvons comprendre qu'une erreur s'est produite lors du traitement de la commande #182726 parce que le produit #21 n'était pas disponible.

## Comment journaliser

Bien que le log ci-dessus ait parfaitement du sens pour nous, humains, il ne s'agit peut-être pas du meilleur format pour les machines. Examinons un exemple pour comprendre pourquoi.

Supposons qu'il y ait un problème de disponibilité d'un certain produit (disons le produit #21) à cause duquel toutes les commandes contenant ce produit échouent. Vous avez été chargé de trouver toutes les commandes échouées pour ce produit.

Vous faites joyeusement un `grep` pour le produit #21 dans vos logs et attendez avec impatience les résultats. Lorsque la recherche est terminée, vous obtenez quelque chose comme ceci :

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #182726 for Product #21 due to exception - Product Not Available

[2020-09-27T18:53:29,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #972526 for Product #217 due to exception - Product Not Available

[2020-09-27T18:52:34,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #46675754 for Product #21 due to exception - Product Not Available

[2020-09-27T18:52:13,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing Order #332254 for Product #2109 due to exception - Product Not Available
```

Pas tout à fait ce à quoi vous vous attendiez, n'est-ce pas ? Alors, comment pouvez-vous améliorer cela ? La journalisation structurée à la rescousse.

# Qu'est-ce que la journalisation structurée ?

La journalisation structurée résout ces problèmes courants et permet aux outils d'analyse de logs de fournir des capacités supplémentaires. Les logs écrits dans un format structuré sont plus adaptés aux machines, ce qui signifie qu'ils peuvent être facilement analysés par une machine.

Cela peut être utile dans les scénarios suivants :

* Les développeurs peuvent rechercher des logs et corréler des événements, ce qui est inestimable à la fois pendant le développement et pour le dépannage des problèmes de production.
* Les équipes métiers peuvent analyser ces logs et effectuer des analyses sur certains champs (par exemple, le nombre de produits uniques par jour) en extrayant et en résumant ces champs.
* Vous pouvez construire des tableaux de bord (à la fois métiers et techniques) en analysant les logs et en effectuant des agrégations sur des champs pertinents.

Utilisons notre déclaration de log précédente et apportons une petite modification pour la structurer.

```java
log.error("Exception in processing OrderId={} for ProductId={} due to Error={}", orderId, productId, ex.getResponseBodyAsString())
```

Cela produira un log dans le format suivant :

```
[2020-09-27T18:54:41,500+0530]-[ERROR]-[InventoryValidator]-[13] Exception in processing OrderId=182726 for ProductId=21 due to Error=Product Not Available
```

Maintenant, ce message de log peut être facilement analysé par la machine en utilisant "=" comme délimiteur pour extraire les champs `OrderId`, `ProductId` et `Error`. Nous pouvons maintenant effectuer une recherche exacte sur `ProductId=21` pour accomplir notre tâche.

Cela nous permet également d'effectuer des analyses plus avancées sur les logs, telles que la préparation d'un rapport de toutes les commandes qui ont échoué avec de telles erreurs.

Si vous utilisez un système de gestion des logs comme Splunk, la requête `Error="Product Not Available" | stats count by ProductId` peut maintenant produire le résultat suivant :

```
+-----------+-------+
| ProductId | count |
+-----------+-------+
| 21        | 5     |
| 27        | 12    |
+-----------+-------+
```

Nous pourrions également utiliser une mise en page JSON pour imprimer nos logs au format JSON :

```json
{  
    "timestamp":"2020-09-27T18:54:41,500+0530"  
    "level":"ERROR"  
    "class":"InventoryValidator"  
    "line":"13"  
    "OrderId":"182726"  
    "ProductId":"21"  
    "Error":"Product Not Available"
}
```

Il est important de comprendre l'approche derrière la journalisation structurée. Il n'y a pas de norme fixe et cela peut être fait de nombreuses manières différentes.

# Conclusion

Dans cet article, nous avons vu les pièges de la journalisation non structurée et les avantages offerts par la journalisation structurée.

Les systèmes de gestion des logs tels que Splunk bénéficient grandement d'un message de log bien structuré et peuvent offrir une recherche et une analyse faciles des événements de log.

Le plus grand défi, cependant, lorsqu'il s'agit de journalisation structurée, est d'établir un ensemble standard de champs pour votre logiciel. Cela peut être réalisé en suivant un modèle de journalisation personnalisé ou une journalisation centralisée qui garantit que tous les développeurs utilisent les mêmes champs dans leurs messages de log.

Merci de m'avoir suivi jusqu'ici. J'espère que vous avez aimé l'article. Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/theawesomenayak/) où je discute régulièrement de technologie et de vie. Jetez également un coup d'œil à certains de [mes autres articles](https://www.freecodecamp.org/news/author/theawesomenayak/). Bonne lecture. 👋