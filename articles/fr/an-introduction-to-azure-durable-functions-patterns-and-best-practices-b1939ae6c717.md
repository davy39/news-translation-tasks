---
title: 'Une introduction aux Azure Durable Functions : modèles et meilleures pratiques'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-25T16:09:14.000Z'
originalURL: https://freecodecamp.org/news/an-introduction-to-azure-durable-functions-patterns-and-best-practices-b1939ae6c717
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5LHDlzgD4qCho-AIjh7pOA.png
tags:
- name: Azure
  slug: azure
- name: Productivity
  slug: productivity
- name: General Programming
  slug: programming
- name: serverless
  slug: serverless
- name: 'tech '
  slug: tech
seo_title: 'Une introduction aux Azure Durable Functions : modèles et meilleures pratiques'
seo_desc: 'By Nadeem Ahamed

  Authored with Steef-Jan Wiggers at Microsoft Azure

  With Durable Functions, you can program a workflow and instantiate tasks in sequential
  or parallel order, or you can build a watch or support a human interaction flow
  (approval workf...'
---

Par Nadeem Ahamed

Rédigé avec [Steef-Jan Wiggers](https://www.serverless360.com/blog/author/steef) chez Microsoft Azure

Avec les Durable Functions, vous pouvez programmer un workflow et instancier des tâches dans un ordre séquentiel ou parallèle, ou vous pouvez créer une surveillance ou supporter un flux d'interaction humaine ([workflow d'approbation](https://blog.mexia.com.au/azure-durable-functions-approval-workflow-with-slack)). Vous pouvez enchaîner des fonctions pour contrôler votre flux. Vous pouvez utiliser des scénarios de fan-in et fan-out, corrélation d'événements, automatisation flexible, et processus longs, ainsi que des modèles d'interaction humaine qui sont difficiles à mettre en place avec seulement des fonctions ou avec des logic apps.

### Enchaînement de fonctions

L'utilisation la plus naturelle et directe des Durable Functions est l'enchaînement de fonctions. Vous avez une fonction orchestrateur qui appelle de nombreuses fonctions dans l'ordre que vous souhaitez. Vous pouvez faire cela avec des fonctions seules et en utilisant des files d'attente Service Bus, mais vous rencontrerez certains défis :

* aucune visualisation pour montrer la relation entre les fonctions et les files d'attente
* les files d'attente intermédiaires sont un détail d'implémentation, avec une surcharge conceptuelle
* la gestion des erreurs ajoute beaucoup plus de complexité

En utilisant les Durable Functions, vous ne rencontrerez pas ces défis. Avec un orchestrateur, vous pouvez :

* avoir un endroit central pour définir l'ordre des appels de fonctions (relations)
* ne pas avoir besoin de gestion des files d'attente — sous le capot, les Durable Functions utilisent et gèrent des files d'attente de stockage
* avoir une gestion centrale des erreurs — lorsqu'une erreur se produit dans l'une des fonctions d'activité, l'erreur se propage à l'orchestrateur

```java
//appelle les fonctions en séquence
public static async Task<object> Run (DurableOrchestrationContext ctx)
{ 
 try
 {
 var x = await ctx.CallFunctionAsync ("F1");
 var y = await ctx.callFunctionAsync ("F2", x);
 var z = await ctx.callFunctionAsync ("F3", y);
 return = await ctx.CallFunctionAsync ("F4", z);
 }
 
catch (Exception )
 {
 //gestion globale des erreurs / compensation ici
 }
}
```

### Fan-out/Fan-in

Le fan-out/fan-in peut être utilisé lorsque vous devez exécuter une ou plusieurs fonctions en parallèle et, en fonction des résultats, vous exécutez d'autres tâches. Avec les fonctions, vous ne pouvez pas mettre en place une telle approche. De plus, vous rencontrerez également les défis mentionnés dans la section précédente. Mais, avec les Durable Functions, vous pouvez atteindre le fan-out/fan-in :

```java
public static async Task Run (Durableorchestrationcontext ctx)
{
var parallelTasks = new List<Task<int>>();
//obtenir une liste de N éléments de travail à traiter en parallèle
object []workBatch = await ctx.CallFunctionAsync<object[]> ("F1");
for (int i = 0; i < workBatch.Length; i++)
{
Task<int> task = ctx.CallFunctionAsync <int> ("F2", workBatch [i]); 
parallelTasks.Add (task);
}
await Task.WhenAll(parallelTasks);
//agréger toutes les N sorties et envoyer le résultat à F3
int sum = parallelTasks.Sum(t=> t.Result); 
await ctx.CallFunctionAsync ("F3", sum);
}
```

### Réponse HTTP Asynchrone

Avec les fonctions, il est possible que lorsque vous appelez une autre API, vous ne sachiez pas combien de temps il faudra avant qu'une réponse ne soit retournée. Par exemple, la latence et le volume peuvent faire que le temps nécessaire à l'API pour traiter la demande et retourner une réponse soit inconnu.

Une fonction peut expirer lors de l'utilisation d'un plan de consommation. L'état doit être maintenu, ce qui est indésirable pour les fonctions, car elles doivent être sans état. Les Durable Functions fournissent des API intégrées qui simplifient le code que vous écrivez pour interagir avec des exécutions de fonctions longues. De plus, l'état est géré par le runtime des Durable Functions.

```java
//Fonction déclenchée par HTTP pour démarrer une nouvelle instance de fonction orchestrateur.
public static async Task<HttpResponseMessage> Run (
HttpReq uestMessage req, DurableOrchestrationClient starter,
string functionName,
Ilogger log)
{
//Le nom de la fonction provient de l'URL de la requête.
//L'entrée de la fonction provient du contenu de la requête.
dynamic eventData await req.Content .ReadAsAsync<object>();
string instanceid = await starter.StartNewAsync (functionName , eventData);
log .Loginformation ($"Started orchestration with ID = '{instanceid}'.");
return starter.CreateCheckStatusResponse (req, instanceid);
}
```

### Acteurs

Une autre utilisation est le surveillant — un processus récurrent dans un workflow tel qu'un processus de nettoyage. Vous pouvez mettre cela en place avec une fonction. Mais, encore une fois, vous rencontrerez certains défis :

* les fonctions sont sans état et de courte durée
* l'accès en lecture/écriture à un état externe doit être synchronisé

Avec les Durable Functions, vous pouvez avoir des intervalles de récurrence flexibles, une gestion de la durée de vie des tâches, et la capacité de créer de nombreux processus de surveillance à partir d'une seule orchestration.

```
public static async Task Run(DurableOrchestrationContext ctx)
{
int counterState = ctx.Getinput<int>();
string operation = await ctx.WaitForExternalEvent<string>("operation");
if (operation == "incr")
{
counterState++;
}
else if (operation == "decr")
{
counterstate --;
}
ctx.ContinueAsNew(counterState);
}
```

### Interaction humaine

Au sein des organisations, vous rencontrerez des processus qui nécessitent une interaction humaine, comme des approbations. Les interactions comme les approbations nécessitent la disponibilité de l'approbateur. Ainsi, le processus doit être actif pendant un certain temps et nécessite un mécanisme fiable lorsque le processus expire. Par exemple, lorsqu'une approbation ne se produit pas dans les 72 heures, un processus d'escalade doit commencer. Avec les Durable Functions, vous pouvez supporter un tel scénario.

```java
public static async Task Run(DurableOrchestrationContext ctx)
{
await ctx.CallFunctionAsync<object []>("RequestApproval");
using (var timeoutCts = new CancellationTokenSource())
{
DateTime dueTime = ctx.CurrentUtcDateTime.AddHours(72);
Task durableTimeout = ctx.CreateTimer(dueTime, 0, cts.Token);
Task<bool > approvalEvent = ctx.WaitForExternalEvent< bool>("ApprovalEvent");
if (approvalEvent == await Task .WhenAny(approvalEvent, durableTimeout ))
{
timeoutCts.Cancel();
await ctx .CallFunctionAsync("HandleApproval", approvalEvent.Result);
}
else
{
await ctx.CallFunctionAsy nc("Escalate" );
}
}
}
```

### Implémentation d'exemple : Enchaînement utilisant les Durable Functions

![Image](https://cdn-media-1.freecodecamp.org/images/lTP6pk0wQqW51rdYVip5Kd5z0mPhwvjG1vsm)

Le client Orchestrateur est une fonction qui peut être déclenchée lorsqu'un message est envoyé. Ce client, une fonction, appellera l'Orchestrateur et transmettra le message de commande.

```java
public static async Task<HttpResponseMessage> Run (
HttpReq uestMessage req, DurableOrchestrationClient starter, string functionName,
Ilogger log)
{
//Le nom de la fonction provient de l'URL de la requête.
//L'entrée de la fonction provient du contenu de la requête.
dynamic eventData await req.Content .ReadAsAsync<object>();
string instanceid = await starter.StartNewAsync ( functionName , eventData);
log .Loginformation ($"Started orchestration with ID = '{instanceid}'.");
return starter.CreateCheckStatusResponse (req, instanceid);
}
```

L'Orchestrateur recevra la commande et appellera les fonctions d'activité.

```java
public static async Task Run(DurableOrchestrationContext context, object order, ILogger log)
{
log.LogInformation($"Data = '{order}'.");
var orderDetail = (OrderDetail) order;
try
{
bool x = await context.CallActivityAsync<bool>("WriteToDatabase", orderDetail);
log.LogInformation($"Data storage = '{x}'.");
if (x == true)
{
await context.CallActivityAsync<OrderDetail>("WriteToArchive", orderDetail);
await context.CallActivityAsync<OrderDetail>("SendNotification", orderDetail);
}
}
catch (Exception)
{
//Gestion des erreurs
}
}
```

Chacune des fonctions d'activité effectuera une tâche — dans ce cas, stocker la commande dans une collection de documents dans une instance CosmosDB, archiver le message stocké, et envoyer un message à la file d'attente pour envoyer une notification via une logic app.

### Bonnes pratiques

Avec les Durable Functions, il y a quelques bonnes pratiques à suivre :

* utilisez l'application Azure App Insights pour surveiller les instances en cours d'exécution et la santé, y compris les Azure Functions
* l'application Durable Functions expose également l'API HTTP pour la gestion. Avec les méthodes de l'API, vous pouvez influencer le cours d'action pour vos Durable Functions.
* utilisez le contrôle de version avec votre fonction durable
* vous pouvez utiliser le déploiement côte à côte, en mettant à jour le nom de votre hub de tâches lors du déploiement. Voir [Stratégies de déploiement Blue Green pour Durable Functions](https://medium.com/@tsuyoshiushio/durable-functions-blue-green-deployment-strategies-ed25509ecd60) pour plus d'informations.

### Conclusion

Dans cet article de blog, nous espérons que vous avez une meilleure compréhension de l'utilisation des Durable Functions et de la valeur qu'elles offrent. Les Durable Functions vous donnent le contrôle ultime sur un workflow, ce qui n'est pas réalisable avec des technologies alternatives telles que les logic apps ou les fonctions seules. Ensemble avec certaines des meilleures pratiques que nous avons consolidées, vous devriez maintenant être en mesure de construire des solutions durables avec les Durable Functions.

[Cet article a été initialement publié sur Serverless360.](https://www.serverless360.com/blog/azure-durable-functions-patterns-best-practices)