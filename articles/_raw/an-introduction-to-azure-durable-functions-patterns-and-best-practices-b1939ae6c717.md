---
title: 'An introduction  to Azure Durable Functions: patterns and best practices'
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
seo_title: null
seo_desc: 'By Nadeem Ahamed

  Authored with Steef-Jan Wiggers at Microsoft Azure

  With Durable Functions, you can program a workflow and instantiate tasks in sequential
  or parallel order, or you can build a watch or support a human interaction flow
  (approval workf...'
---

By Nadeem Ahamed

Authored with [Steef-Jan Wiggers](https://www.serverless360.com/blog/author/steef) at Microsoft Azure

With Durable Functions, you can program a workflow and instantiate tasks in sequential or parallel order, or you can build a watch or support a human interaction flow ([approval workflow](https://blog.mexia.com.au/azure-durable-functions-approval-workflow-with-slack)). You can chain functions to control your flow. You can use fan-in and fan-out scenarios, correlating events, flexible automation, and long-running processes, and human interaction patterns that are hard to put in place with only functions or with logic apps.

### Chaining functions

The most natural and straightforward use of Durable Functions is chaining functions together. You have one orchestrator function that calls many functions in the order you desire. You can do this with functions alone and using Service Bus Queues, yet you will face some challenges:

* no visualization to show the relationship between functions and queues
* middle queues are an implementation detail, with a conceptual overhead
* error handling adds a lot more complexity

Using Durable Functions, you will not run into those challenges. With an orchestrator you:

* can have a central place to set the order of function calls (relations)
* need no management of queues — under the hood, Durable Functions use and manage storage queues
* have central error handling — when an error occurs in one of the activity functions, the error propagates back to the orchestrator

```java
//calls functions in sequence
public static async Task<object> Run (DurableOrchestrationContext ctx)
{ 
 try
 {
 var x = await ctx.CallFunctionAsync (“F1”);
 var y = await ctx.callFunctionAsync (“F2”, x);
 var z = await ctx.callFunctionAsync (“F3”, y);
 return = await ctx.CallFunctionAsync (“F4”, z);
 }
 
catch (Exception )
 {
 //global error handling /compensation goes here
 }
}
```

### Fan-out/Fan-in

Fan-out/fan-in can be used when you need to execute one or more functions in parallel and, based on the results, you run some other tasks. With functions, you cannot put in place such an approach. Moreover, you will also face the challenges mentioned in the previous section. But, with Durable Functions, you can achieve fan-out/fan-in:

```java
public static async Task Run (Durableorchestrationcontext ctx)
{
var parallelTasks = new List<Task<int>>();
//get a list of N work items to process in parallel
object []workBatch = await ctx.CallFunctionAsync<object[]> (“F1”);
for (int i = 0; i < workBatch.Length; i++)
{
Task<int> task = ctx.CallFunctionAsync <int> (“F2”, workBatch [i]); 
parallelTasks.Add (task);
}
await Task.WhenAll(parallelTasks);
//aggregate all N outputs and send result to F3
int sum = parallelTasks.Sum(t=> t.Result); 
await ctx.CallFunctionAsync (“F3”, sum);
}
```

### HTTP Async Response

With functions, it is possible that when you call another API you do not know the amount of time it would take before a response is returned. For example, latency and volume can cause the time it would make the API to process the request and return a response to be unknown.

A function can time-out when using a Consumption plan. The state needs to be maintained, which is undesirable for functions, as they need to be stateless. Durable Functions provide built-in APIs that simplify the code you write for interacting with long-running function executions. Furthermore, the state is managed by the Durable Functions run-time.

```java
//HTTP-triggered function to start a new orchestrator function instance.
public static async Task<HttpResponseMessage> Run (
HttpReq uestMessage req, DurableOrchestrationClient starter,
string functionName,
Ilogger log)
{
//Function name comes from the request URL.
//Function input comes from the request content .
dynamic eventData await req.Content .ReadAsAsync<object>();
string instanceid = await starter.StartNewAsync (functionName , eventData);
log .Loginformation ($”Started orchestration with ID = ‘{instanceid} ‘.”);
return starter.CreateCheckStatusResponse (req, instanceid);
}
```

### Actors

Another use is the watcher — a recurring process in a workflow such as a clean-up process. You can put this in place with a function. But, again, you will have some challenges:

* functions are stateless and short-lived
* read/write access to an external state needs to be synchronized

With Durable Functions, you can have flexible recurrence intervals, task lifetime management, and the ability to create many watch processes from a single orchestration.

```
public static async Task Run(DurableOrchestrationContext ctx)
{
int counterState = ctx.Getinput<int>();
string operation = await ctx.WaitForExternalEvent<string>(“operation”);
if (operation == “incr”)
{
counterState++;
}
else if (operation == “decr”)
{
counterstate --;
}
ctx.ContinueAsNew(counterState);
}
```

### Human interaction

Within organizations, you will face processes that require some human interaction such as approvals. Interactions like approvals require the availability of the approver. Thus, the process needs to be active for some time, and needs a reliable mechanism when the process times out. For instance, when an approval doesn’t occur within 72 hours, an escalation process must start. With Durable Functions, you can support such a scenario.

```java
public static async Task Run(DurableOrchestrationContext ctx)
{
await ctx.CallFunctionAsync<object []>(“RequestApproval”);
using (var timeoutCts = new CancellationTokenSource())
{
DateTime dueTime = ctx.CurrentUtcDateTime.AddHours(72);
Task durableTimeout = ctx.CreateTimer(dueTime, 0, cts.Token);
Task<bool > approvalEvent = ctx.WaitForExternalEvent< bool>(“ApprovalEvent”);
if (approvalEvent == await Task .WhenAny(approvalEvent, durableTimeout ))
{
timeoutCts.Cancel();
await ctx .CallFunctionAsync(“HandleApproval”, approvalEvent.Result);
}
else
{
await ctx.CallFunctionAsy nc(“Escalate” );
}
}
}
```

### Sample implementation: Chaining using Durable Functions

![Image](https://cdn-media-1.freecodecamp.org/images/lTP6pk0wQqW51rdYVip5Kd5z0mPhwvjG1vsm)

The Orchestrator Client is a function that can be triggered when a message is sent. This Client, a function, will call the Orchestrator and pass the order message.

```java
public static async Task<HttpResponseMessage> Run (
HttpReq uestMessage req, DurableOrchestrationClient starter, string functionName,
Ilogger log)
{
//Function name comes from the request URL.
//Function input comes from the request content .
dynamic eventData await req.Content .ReadAsAsync<object>();
string instanceid = await starter.StartNewAsync ( functionName , eventData);
log .Loginformation ($”Started orchestration with ID = ‘{instanceid} ‘.”);
return starter.CreateCheckStatusResponse (req, instanceid);
}
```

The Orchestrator will receive the order and call the activity functions.

```java
public static async Task Run(DurableOrchestrationContext context, object order, ILogger log)
{
log.LogInformation($”Data = ‘{order}’.”);
var orderDetail = (OrderDetail) order;
try
{
bool x = await context.CallActivityAsync<bool>(“WriteToDatabase”, orderDetail);
log.LogInformation($”Data storage = ‘{x}’.”);
if (x == true)
{
await context.CallActivityAsync<OrderDetail>(“WriteToArchive”, orderDetail);
await context.CallActivityAsync<OrderDetail>(“SendNotification”, orderDetail);
}
}
catch (Exception)
{
//ErrorHandling
}
}
```

Each of the activity functions will perform a task — in this case, store the order in a document collection in a CosmosDB instance, archive the stored message, and send a message to the queue to send out a notification via a logic app.

### Best practices

With Durable Functions there are a few best practices to follow:

* use the Azure App Insights app to monitor running instances and health, including Azure Functions
* the Durable Functions app also exposes the HTTP API for management. With the API methods, you can influence the course of action for your Durable Functions.
* use version control with your durable function
* you can use side-by-side deployment, updating the name of your task hub on deployment. See [Durable Functions Blue Green Deployment Strategies](https://medium.com/@tsuyoshiushio/durable-functions-blue-green-deployment-strategies-ed25509ecd60) for more information.

### Wrap-up

In this blog post, we hope you have a better understanding of the use of Durable Functions, and what value they offer. Durable Functions give you the ultimate control over a workflow, not achievable with alternative technologies such as logic apps or functions alone. Together with some of the best practices we consolidated, you should now be able to build sustainable solutions with Durable Functions.

[This article was originally published at Serverless360.](https://www.serverless360.com/blog/azure-durable-functions-patterns-best-practices)

