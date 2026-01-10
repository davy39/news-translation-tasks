---
title: Comprendre Azure Durable Functions
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-04T19:46:07.000Z'
originalURL: https://freecodecamp.org/news/making-sense-of-azure-durable-functions
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1-0R7Wy1EJa59bvMNMHJaM4A.jpeg
tags:
- name: Azure
  slug: azure
- name: Azure Functions
  slug: azure-functions
- name: serverless
  slug: serverless
seo_title: Comprendre Azure Durable Functions
seo_desc: 'By Mikhail Shilkov

  Stateful Workflows on top of Stateless Serverless Cloud Functions—this is the essence
  of the Azure Durable Functions library. That''s a lot of fancy words in one sentence,
  and they might be hard for the majority of readers to unders...'
---

Par Mikhail Shilkov

Les workflows avec état sur des fonctions cloud sans état&mdash;c'est l'essence de la bibliothèque Azure Durable Functions. C'est beaucoup de mots à la mode dans une seule phrase, et ils peuvent être difficiles à comprendre pour la majorité des lecteurs.

Veuillez me rejoindre dans ce voyage où je vais essayer d'expliquer comment ces mots à la mode s'emboîtent. Je vais le faire en 3 étapes :

- Décrire le contexte des applications cloud modernes reposant sur une architecture sans serveur ;
- Identifier les limitations des approches de base pour composer des applications à partir de blocs de construction simples ;
- Expliquer les solutions que Durable Functions offre pour ces problèmes.

Microservices
-------------

Traditionnellement, les applications côté serveur étaient construites dans un style qui est maintenant appelé **Monolithe**. Si plusieurs personnes et équipes développaient des parties de la même application, elles contribuaient principalement au même code source. Si le code source était bien structuré, il aurait certains modules ou composants distincts, et une seule équipe serait généralement propriétaire de chaque module :

![Monolithe](https://thepracticaldev.s3.amazonaws.com/i/7hdmn8wjk67mbd0z8pp0.png)

<figcaption>Plusieurs composants d'une application monolithique</figcaption>

Habituellement, les modules étaient regroupés lors de la construction et ensuite déployés en tant qu'unité unique, de sorte qu'une grande partie de la communication entre les modules restait à l'intérieur du processus du système d'exploitation.

Bien que les modules aient pu rester faiblement couplés au fil du temps, le couplage se produisait presque toujours au niveau du stockage des données car toutes les équipes utilisaient une base de données centralisée unique.

Ce modèle fonctionne bien pour les applications de petite à moyenne taille, mais il s'avère que les équipes commencent à se gêner mutuellement à mesure que l'application grandit, car la synchronisation des contributions prend de plus en plus d'efforts.

En tant qu'alternative complexe mais viable, l'industrie a proposé une approche révisée orientée service, communément appelée **Microservices**. Les équipes divisent la grande application en "tranches verticales" structurées autour des capacités commerciales distinctes :

![Microservices](https://thepracticaldev.s3.amazonaws.com/i/mfpnrqhb9783uzv3jxm2.png)

<figcaption>Plusieurs composants d'une application basée sur des microservices</figcaption>

Chaque équipe possède ensuite une tranche verticale complète&mdash;des contrats de communication publics, voire des interfaces utilisateur, jusqu'au stockage des données. Les bases de données explicitement partagées sont fortement déconseillées. Les services communiquent entre eux via des contrats publics documentés et versionnés.

Si les frontières de la division ont été bien sélectionnées&mdash;et c'est la partie la plus délicate&mdash;les contrats restent stables au fil du temps et suffisamment minces pour éviter trop de bavardage. Cela donne à chaque équipe suffisamment d'autonomie pour innover à leur meilleur rythme et prendre des décisions techniques indépendantes.

L'un des inconvénients des microservices est le changement de modèle de déploiement. Les services sont désormais déployés sur des serveurs séparés connectés via un réseau :

![Systèmes Distribués](https://thepracticaldev.s3.amazonaws.com/i/wgg72smliy1lgcaz8ssl.png)

<figcaption>Défis de la communication entre les composants distribués</figcaption>

Les réseaux sont fondamentalement peu fiables : ils fonctionnent très bien la plupart du temps, mais lorsqu'ils échouent, ils échouent de toutes sortes de manières imprévisibles et les moins souhaitables. Il existe des livres écrits sur le sujet de l'architecture des systèmes distribués. TL;DR : c'est difficile.

Beaucoup des nouveaux adopteurs de microservices tendent à ignorer de telles complications. REST sur HTTP(S) est le style dominant de connexion des microservices. Comme tout autre protocole de communication synchrone, il rend le système fragile.

Considérez ce qui se passe lorsqu'un service devient temporairement malsain : peut-être que sa base de données est hors ligne, ou il a du mal à suivre la charge de requêtes, ou une nouvelle version du service est en cours de déploiement. Toutes les requêtes vers le service problématique commencent à échouer&mdash;ou pire&mdash;deviennent très lentes. Le service dépendant attend la réponse, et bloque ainsi toutes les requêtes entrantes. L'erreur se propage en amont très rapidement, provoquant des pannes en cascade partout :

![Pannes en Cascade](https://thepracticaldev.s3.amazonaws.com/i/7ab7puvdzc2v0w3jo9aa.png)

<figcaption>Erreur dans un composant provoquant des pannes en cascade</figcaption>

L'application est hors service. Tout le monde crie et commence la guerre des reproches.

Applications pilotées par événements
-------------------------------------

Bien que les pannes en cascade de la communication HTTP puissent être atténuées avec des modèles comme un disjoncteur et une dégradation élégante, une meilleure solution est de passer au style de communication asynchrone par défaut. Un type de service de mise en file d'attente persistante est utilisé comme intermédiaire.

Le style d'architecture d'application qui repose sur l'envoi d'événements entre les services est connu sous le nom de **piloté par événements**. Lorsqu'un service fait quelque chose d'utile, il publie un événement&mdash;un enregistrement du fait qui s'est produit dans son domaine commercial. Un autre service écoute les événements publiés et exécute son propre devoir en réponse à ces faits :

![Application pilotée par événements](https://thepracticaldev.s3.amazonaws.com/i/o5wml467ggim3ebfg1i4.png)

<figcaption>Communication dans les applications pilotées par événements</figcaption>

Le service qui produit des événements peut ne pas connaître les consommateurs. De nouveaux abonnés aux événements peuvent être introduits au fil du temps. Cela fonctionne mieux en théorie qu'en pratique, mais les services tendent à être moins couplés.

Plus important encore, si un service est hors service, les autres services ne prennent pas feu immédiatement. Les services en amont continuent de publier les événements, qui s'accumulent dans la file d'attente mais peuvent être stockés en toute sécurité pendant des heures ou des jours. Les services en aval peuvent ne rien faire d'utile pour ce flux particulier, mais ils peuvent rester sains par ailleurs.

Cependant, un autre problème potentiel vient de pair avec le couplage lâche : la faible cohésion. Comme le souligne Martin Fowler dans son essai
[Que voulez-vous dire par "piloté par événements"](https://martinfowler.com/articles/201701-event-driven.html) :

> Il est très facile de créer des systèmes bien découplés avec la notification d'événements, sans réaliser que vous perdez de vue le flux à grande échelle.

Étant donné de nombreux composants qui publient et s'abonnent à un grand nombre de types d'événements, il est facile de ne plus voir la forêt pour les arbres. Les combinaisons d'événements constituent généralement des workflows progressifs exécutés dans le temps. Un workflow est plus que la somme de ses parties, et la compréhension du flux de haut niveau est primordiale pour contrôler le comportement du système.

Gardez cette pensée à l'esprit pendant une minute ; nous y reviendrons plus tard. Il est maintenant temps de parler du *cloud*.

Cloud
-----

La naissance du cloud public a changé la façon dont nous architectons les applications. Elle a rendu de nombreuses choses beaucoup plus simples : le provisionnement de nouvelles ressources en quelques minutes au lieu de mois, la mise à l'échelle élastique basée sur la demande, et la résilience et la reprise après sinistre à l'échelle mondiale.

Elle a rendu d'autres choses plus compliquées. Voici une image du réseau mondial Azure :

![Réseau Azure](https://thepracticaldev.s3.amazonaws.com/i/0kg17c6l48zwj3404yyg.png)

<figcaption>Emplacements Azure avec des connexions réseau</figcaption>

Il y a de bonnes raisons de déployer des applications dans plus d'un emplacement géographique : entre autres, pour réduire la latence du réseau en restant proche du client, et pour atteindre la résilience grâce à la redondance géographique. Le cloud public est le système distribué ultime. Comme vous vous en souvenez, les systèmes distribués sont difficiles.

Il y a plus à cela. Chaque fournisseur de cloud dispose de dizaines et de dizaines de services gérés, ce qui est à la fois une malédiction et une bénédiction. Les services spécialisés sont excellents pour fournir des solutions clés en main à des problèmes complexes courants. En revanche, chaque service a des propriétés distinctes en matière de cohérence, de résilience et de tolérance aux pannes.

À mon avis, à ce stade, les développeurs doivent adopter le cloud public et appliquer la conception de systèmes distribués par-dessus. Si vous êtes d'accord, il existe une excellente façon de l'aborder.

Sans serveur
------------

Le terme légèrement provocateur **sans serveur** est utilisé pour décrire les services cloud qui ne nécessitent pas le provisionnement de VM, d'instances, de workers ou de toute autre capacité fixe pour exécuter des applications personnalisées par-dessus. Les ressources sont allouées dynamiquement et de manière transparente, et le coût est basé sur leur consommation réelle, plutôt que sur une capacité pré-achetée.

Le sans serveur concerne davantage les propriétés opérationnelles et économiques du système que la technologie en tant que telle. Les serveurs existent, mais ils sont la préoccupation de quelqu'un d'autre. Vous ne gérez pas le temps de fonctionnement des applications sans serveur : le fournisseur de cloud le fait.

En plus de cela, vous payez pour ce que vous utilisez, similaire à la consommation d'autres ressources de base comme l'électricité. Au lieu d'acheter un générateur pour alimenter votre maison, vous achetez simplement de l'énergie auprès de la compagnie d'électricité. Vous perdez un certain contrôle (par exemple, aucun moyen de sélectionner la tension), mais cela convient dans la plupart des cas. Le grand avantage est de ne pas avoir à acheter et à maintenir le matériel.

Le calcul sans serveur fait de même : il fournit des services standard sur une base de paiement à l'usage.

Si nous parlons plus spécifiquement des offres de type Function-as-a-Service comme Azure Functions, elles fournissent un modèle standard pour exécuter de petits morceaux de code dans le cloud. Vous regroupez le code ou les binaires et l'envoyez à Azure ; Microsoft prend en charge tout le matériel et les logiciels nécessaires pour l'exécuter. L'infrastructure se met à l'échelle automatiquement en fonction de la demande, et vous payez par requête, temps CPU et mémoire que l'application a consommés. Aucune utilisation&mdash;aucune facture.

Cependant, il y a toujours un "mais". Les services FaaS viennent avec un modèle de développement opinionné que les applications doivent suivre :

- **Piloté par événements** : pour chaque fonction sans serveur, vous devez définir un déclencheur spécifique&mdash;le type d'événement qui provoque son exécution, qu'il s'agisse d'un point de terminaison HTTP ou d'un message de file d'attente ;

- **De courte durée** : les fonctions ne peuvent s'exécuter que pendant quelques minutes, et de préférence pendant quelques secondes ou moins ;

- **Sans état** : comme vous ne contrôlez pas où et quand les instances de fonction sont provisionnées ou désapprovisionnées, il n'y a aucun moyen de stocker des données dans le processus entre les requêtes de manière fiable ; un stockage externe doit être utilisé.

Franchement, la majorité des applications existantes ne correspondent pas vraiment à ce modèle. Si vous avez la chance de travailler sur une nouvelle application (ou un nouveau module de celle-ci), vous êtes en meilleure posture.

Beaucoup d'applications sans serveur peuvent être conçues pour ressembler à cet exemple du [blog Serverless360](https://www.serverless360.com/blog/building-reactive-solution-with-azure-event-grid) :

![Application sans serveur "serviceful"](https://thepracticaldev.s3.amazonaws.com/i/6nmkm9cytuxdh1jmmjzo.png)

<figcaption>Application exemple utilisant une architecture sans serveur "serviceful"</figcaption>

Il y a 9 services Azure gérés qui travaillent ensemble dans cette application. La plupart d'entre eux ont un objectif unique, mais les services sont tous collés ensemble avec Azure Functions. Une image est téléchargée dans Blob Storage, une Azure Function appelle l'API Vision pour reconnaître la plaque d'immatriculation et envoyer le résultat à Event Grid, une autre Azure Function met cet événement dans Cosmos DB, et ainsi de suite.

Ce style d'applications cloud est parfois appelé **Serviceful** pour souligner l'utilisation intensive de services gérés "collés" ensemble par des fonctions sans serveur.

Créer une application comparable sans aucun service géré serait une tâche beaucoup plus difficile, d'autant plus si l'application doit fonctionner à grande échelle. De plus, il n'y a aucun moyen de conserver le modèle de tarification à l'usage dans le monde de l'auto-service.

L'application illustrée ci-dessus est encore assez simple. Les processus dans les applications d'entreprise sont souvent beaucoup plus sophistiqués.

Souvenez-vous de la citation de Martin Fowler sur la perte de vue du flux à grande échelle. C'était vrai pour les microservices, mais c'est encore plus vrai pour les "nanoservices" des fonctions cloud.

Je veux approfondir et vous donner plusieurs exemples de problèmes connexes.

Défis de la composition sans serveur
-------------------------------------

Pour le reste de l'article, je vais définir une application commerciale imaginaire pour la réservation de voyages vers des conférences logicielles. Pour aller à une conférence, je dois acheter des billets pour la conférence elle-même, acheter les vols et réserver une chambre d'hôtel.

Dans ce scénario, il est logique de créer trois Azure Functions, chacune responsable d'une étape du processus de réservation. Comme nous préférons le passage de messages, chaque Function émet un événement que la fonction suivante peut écouter :

![Application de réservation de conférence](https://thepracticaldev.s3.amazonaws.com/i/nprzua8g1w231xwd47az.png)

<figcaption>Application de réservation de conférence</figcaption>

Cette approche fonctionne, cependant, des problèmes existent.

### Séquençage flexible

Comme nous devons exécuter l'ensemble du processus de réservation en séquence, les Azure Functions sont connectées les unes après les autres en configurant la sortie d'une fonction pour correspondre à la source d'événement de la fonction en aval.

Dans l'image ci-dessus, la séquence des fonctions est définie de manière rigide. Si nous devions échanger l'ordre de réservation des vols et de la réservation de l'hôtel, cela nécessiterait une modification du code&mdash;au moins des définitions de câblage d'entrée/sortie, mais probablement aussi des types de paramètres des fonctions.

Dans ce cas, les fonctions sont-elles *vraiment* découplées ?

### Gestion des erreurs

Que se passe-t-il si la fonction Book Flight devient malsaine, peut-être en raison de la panne du service de réservation de vols tiers ? Eh bien, c'est pourquoi nous utilisons la messagerie asynchrone : après l'échec de l'exécution de la fonction, le message retourne à la file d'attente et est repris par une autre exécution.

Cependant, de telles nouvelles tentatives se produisent presque immédiatement pour la plupart des sources d'événements. Cela peut ne pas être ce que nous voulons : une politique de repli exponentiel pourrait être une idée plus intelligente. À ce stade, la logique de nouvelle tentative devient **avec état** : la tentative suivante devrait "connaître" l'historique des tentatives précédentes pour prendre une décision sur le timing de la nouvelle tentative.

Il existe également des modèles de gestion des erreurs plus avancés. Si les échecs d'exécution ne sont pas intermittents, nous pouvons décider d'annuler l'ensemble du processus et d'exécuter des actions compensatoires contre les étapes déjà terminées.

Un exemple de cela est une action de repli : si le vol n'est pas possible (par exemple, aucune route pour cette combinaison origine-destination), le flux pourrait choisir de réserver un train à la place :

![Repli en cas d'erreur](https://thepracticaldev.s3.amazonaws.com/i/1xm0gct4oqulu30xoa3y.png)

<figcaption>Repli après 3 échecs consécutifs</figcaption>

Ce scénario n'est pas trivial à implémenter avec des fonctions sans état. Nous pourrions attendre qu'un message aille dans la file d'attente des lettres mortes et le router à partir de là, mais cela est fragile et pas assez expressif.

### Actions parallèles

Parfois, le processus commercial n'a pas besoin d'être séquentiel. Dans notre scénario de réservation, il peut ne pas y avoir de différence si nous réservons un vol avant un hôtel ou vice versa. Il pourrait être souhaitable d'exécuter ces actions en parallèle.

L'exécution parallèle des actions est facile avec les capacités de publication-abonnement d'un bus d'événements : les deux fonctions doivent s'abonner au même événement et agir sur celui-ci indépendamment.

Le problème survient lorsque nous devons réconcilier les résultats des actions parallèles, par exemple, calculer le prix final à des fins de rapport de dépenses :

![Fan-out / Fan-in](https://thepracticaldev.s3.amazonaws.com/i/jg39oi8g8ft0qfp3ugk4.png)

<figcaption>Modèle Fan-out / Fan-in</figcaption>

Il n'y a aucun moyen d'implémenter le bloc Report Expenses en tant que fonction Azure unique : les fonctions ne peuvent pas être déclenchées par deux événements, et encore moins corrélées à deux événements *connexes*.

La solution inclurait probablement deux fonctions, une par événement, et le stockage partagé entre elles pour transmettre des informations sur la première réservation terminée à celle qui termine en dernier. Tout ce câblage doit être implémenté dans un code personnalisé. La complexité augmente si plus de deux fonctions doivent s'exécuter en parallèle.

De plus, n'oubliez pas les cas limites. Que se passe-t-il si l'une des fonctions échoue ? Comment vous assurez-vous qu'il n'y a pas de condition de course lors de l'écriture et de la lecture vers/depuis le stockage partagé ?

### Orchestrateur manquant

Tous ces exemples nous donnent un indice que nous avons besoin d'un outil supplémentaire pour organiser des fonctions indépendantes à usage unique de bas niveau en workflows de haut niveau.

Un tel outil peut être appelé un **Orchestrateur** car sa seule mission est de déléguer le travail à des actions sans état tout en maintenant la vue d'ensemble et l'historique du flux.

Azure Durable Functions vise à fournir un tel outil.

Présentation d'Azure Durable Functions
---------------------------------------

### Azure Functions

Azure Functions est le service de calcul sans serveur de Microsoft. Les fonctions sont pilotées par événements : chaque fonction définit un **déclencheur**&mdash;la définition exacte de la source d'événement, par exemple, le nom d'une file d'attente de stockage.

Azure Functions peut être programmé dans [plusieurs langages](https://docs.microsoft.com/fr-fr/azure/azure-functions/supported-languages). Une fonction de base avec un déclencheur [Storage Queue](https://docs.microsoft.com/fr-fr/azure/azure-functions/functions-bindings-storage-queue) implémentée en C# ressemblerait à ceci :

``` csharp
[FunctionName("MyFirstFunction")]
public static void QueueTrigger(
    [QueueTrigger("myqueue-items")] string myQueueItem, 
    ILogger log)
{
    log.LogInformation($"C# function processed: {myQueueItem}");
}
```

L'attribut `FunctionName` expose la méthode statique C# en tant que fonction Azure nommée `MyFirstFunction`. L'attribut `QueueTrigger` définit le nom de la file d'attente de stockage à écouter. Le corps de la fonction journalise les informations sur le message entrant.

### Durable Functions

[Durable Functions](https://docs.microsoft.com/fr-fr/azure/azure-functions/durable/durable-functions-overview) est une bibliothèque qui apporte des abstractions d'orchestration de workflows à Azure Functions. Elle introduit un certain nombre d'idiomes et d'outils pour définir des opérations avec état, potentiellement de longue durée, et gère beaucoup de mécanismes de communication fiable et de gestion d'état en arrière-plan.

La bibliothèque enregistre l'historique de toutes les actions dans les services de stockage Azure, permettant la durabilité et la résilience aux pannes.

Durable Functions est [open source](https://github.com/Azure/azure-functions-durable-extension), Microsoft accepte les contributions externes, et la communauté est assez active.

Actuellement, vous pouvez écrire des Durable Functions dans 3 langages de programmation : C#, F#, et Javascript (Node.js). Tous mes exemples seront en C#. Pour Javascript, consultez [ce guide de démarrage rapide](https://docs.microsoft.com/fr-fr/azure/azure-functions/durable/quickstart-js-vscode) et [ces exemples](https://github.com/Azure/azure-functions-durable-extension/tree/master/samples/javascript). Pour F#, voir [les exemples](https://github.com/Azure/azure-functions-durable-extension/tree/master/samples/fsharp), [la bibliothèque spécifique à F#](https://github.com/mikhailshilkov/DurableFunctions.FSharp) et mon article [Un conte de fées de F# et Durable Functions](https://mikhail.io/2018/12/fairy-tale-of-fsharp-and-durable-functions/).

La fonctionnalité de construction de workflow est réalisée par l'introduction de deux types supplémentaires de déclencheurs : les Activity Functions et les Orchestrator Functions.

### Activity Functions

Les Activity Functions sont des blocs de construction simples, sans état et à usage unique qui effectuent une seule tâche et n'ont aucune connaissance du workflow plus large. Un nouveau type de déclencheur, `ActivityTrigger`, a été introduit pour exposer les fonctions en tant qu'étapes de workflow, comme je l'explique ci-dessous.

Voici une simple Activity Function implémentée en C# :

``` csharp
[FunctionName("BookConference")]
public static ConfTicket BookConference([ActivityTrigger] string conference)
{
    var ticket = BookingService.Book(conference);
    return new ConfTicket { Code = ticket };
}
```

Elle a un attribut `FunctionName` commun pour exposer la méthode statique C# en tant que fonction Azure nommée `BookConference`. Le nom est important car il est utilisé pour invoquer l'activité à partir des orchestrateurs.

L'attribut `ActivityTrigger` définit le type de déclencheur et pointe vers le paramètre d'entrée `conference` que l'activité s'attend à recevoir pour chaque invocation.

La fonction peut retourner un résultat de n'importe quel type sérialisable ; ma fonction exemple retourne un simple sac de propriétés appelé `ConfTicket`.

Les Activity Functions peuvent faire presque n'importe quoi : appeler d'autres services, charger et sauvegarder des données depuis/vers des bases de données, et utiliser n'importe quelle bibliothèque .NET.

### Orchestrator Functions

L'Orchestrator Function est un concept unique introduit par Durable Functions. Son seul but est de gérer le flux d'exécution et de données parmi plusieurs fonctions d'activité.

Sa forme la plus basique enchaîne plusieurs activités indépendantes en un seul workflow séquentiel.

Commençons par un exemple qui réserve un billet de conférence, un itinéraire de vol et une chambre d'hôtel un par un :

![Workflow séquentiel](https://thepracticaldev.s3.amazonaws.com/i/q1mogb5rtgdspw9o0p8w.png)

<figcaption>3 étapes d'un workflow exécutées en séquence</figcaption>

L'implémentation de ce workflow est définie par une autre fonction Azure C#, cette fois avec `OrchestrationTrigger` :

``` csharp
[FunctionName("SequentialWorkflow")]
public static async Task Sequential([OrchestrationTrigger] DurableOrchestrationContext context)
{
    var conference = await context.CallActivityAsync<ConfTicket>("BookConference", "ServerlessDays");
    var flight = await context.CallActivityAsync<FlightTickets>("BookFlight", conference.Dates);
    await context.CallActivityAsync("BookHotel", flight.Dates);
}
```

Encore une fois, les attributs sont utilisés pour décrire la fonction pour le runtime Azure.

Le seul paramètre d'entrée est de type `DurableOrchestrationContext`. Ce contexte est l'outil qui permet les opérations d'orchestration.

En particulier, la méthode `CallActivityAsync` est utilisée trois fois pour invoquer trois activités les unes après les autres. Le corps de la méthode semble très typique pour tout code C# travaillant avec une API basée sur `Task`. Cependant, le comportement est entièrement différent. Examinons les détails de l'implémentation.

Derrière les coulisses
---------------------

Parcourons le cycle de vie d'une exécution du workflow séquentiel ci-dessus.

Lorsque l'orchestrateur commence à s'exécuter, la première invocation de `CallActivityAsync` est faite pour réserver le billet de conférence. Ce qui se passe réellement ici, c'est qu'un message de file d'attente est envoyé de l'orchestrateur à la fonction d'activité.

La fonction d'activité correspondante est déclenchée par le message de la file d'attente. Elle fait son travail (réserve le billet) et retourne le résultat. La fonction d'activité sérialise le résultat et l'envoie en tant que message de file d'attente à l'orchestrateur :

![Durable Functions : Passage de messages](https://thepracticaldev.s3.amazonaws.com/i/gqiln55lyrdboph9vkct.png)

<figcaption>Messagerie entre l'orchestrateur et l'activité</figcaption>

Lorsque le message arrive, l'orchestrateur est à nouveau déclenché et peut passer à la deuxième activité. Le cycle se répète&mdash;un message est envoyé à l'activité Book Flight, elle est déclenchée, fait son travail et envoie un message à l'orchestrateur. Le même flux de messages se produit pour le troisième appel.

### Comportement d'arrêt-reprise

Comme discuté précédemment, le passage de messages est destiné à découpler l'expéditeur et le destinataire dans le temps. Pour chaque message dans le scénario ci-dessus, aucune réponse immédiate n'est attendue.

Au niveau C#, lorsque l'opérateur `await` est exécuté, le code ne bloque pas l'exécution de l'ensemble de l'orchestrateur. Au lieu de cela, il quitte simplement : l'orchestrateur cesse d'être actif et son étape actuelle se termine.

Chaque fois qu'un message de retour arrive d'une activité, le code de l'orchestrateur redémarre. Il commence toujours par la première ligne. Oui, cela signifie que la même ligne est exécutée plusieurs fois : jusqu'au nombre de messages à l'orchestrateur.

Cependant, l'orchestrateur stocke l'historique de ses exécutions passées dans Azure Storage, donc l'effet du deuxième passage de la première ligne est différent : au lieu d'envoyer un message à l'activité, il connaît déjà le résultat de cette activité, donc `await` retourne ce résultat et l'assigne à la variable `conference`.

En raison de ces "replays", l'implémentation de l'orchestrateur doit être déterministe : n'utilisez pas `DateTime.Now`, des nombres aléatoires ou des opérations multithread ; plus de détails [ici](https://docs.microsoft.com/fr-fr/azure/azure-functions/durable/durable-functions-checkpointing-and-replay#orchestrator-code-constraints).

### Event Sourcing

Les Azure Functions sont sans état, tandis que les workflows nécessitent un état pour suivre leur progression. Chaque fois qu'une nouvelle action vers l'exécution du workflow se produit, le framework enregistre automatiquement un événement dans le stockage de tables.

Chaque fois qu'un orchestrateur redémarre l'exécution parce qu'un nouveau message arrive de son activité, il charge l'historique complet de cette exécution particulière à partir du stockage. Le contexte durable utilise cet historique pour prendre des décisions sur l'appel de l'activité ou le retour du résultat précédemment stocké.

Le modèle de stockage de l'historique complet des changements d'état sous forme de magasin d'événements en ajout uniquement est connu sous le nom d'Event Sourcing. Le magasin d'événements offre plusieurs avantages :

- **Durabilité**&mdash;si un hôte exécutant une orchestration échoue, l'historique est conservé dans le stockage persistant et est chargé par le nouvel hôte où l'orchestration redémarre ;
- **Évolutivité**&mdash;les écritures en ajout uniquement sont rapides et faciles à répartir sur plusieurs serveurs de stockage ;
- **Observabilité**&mdash;aucun historique n'est jamais perdu, il est donc simple d'inspecter et d'analyser même après la fin du workflow.

Voici une illustration des événements notables qui sont enregistrés pendant notre workflow séquentiel :

![Durable Functions : Event Sourcing](https://thepracticaldev.s3.amazonaws.com/i/i56z7uddemycm69j1ey1.png)

<figcaption>Journal des événements au cours de la progression de l'orchestrateur</figcaption>

### Facturation

Les Azure Functions sur le plan de consommation sans serveur sont facturées par exécution + par durée d'exécution.

Le comportement d'arrêt-reprise des orchestrateurs durables entraîne l'exécution de la même fonction d'orchestrateur plusieurs fois pour une seule "instance" de workflow. Cela signifie également payer pour plusieurs exécutions courtes.

Cependant, la facture totale finit généralement par être beaucoup plus faible par rapport au coût potentiel des appels synchrones bloquants aux activités. Le prix de 5 exécutions de 100 ms chacune est significativement inférieur au coût de 1 exécution de 30 secondes.

D'ailleurs, le premier million d'exécutions par mois est [sans frais](https://azure.microsoft.com/fr-fr/pricing/details/functions/), donc de nombreux scénarios n'entraînent aucun coût du tout pour le service Azure Functions.

Un autre composant de coût à garder à l'esprit est Azure Storage. Les files d'attente et les tables utilisées en arrière-plan sont facturées au client final. Selon mon expérience, cette charge reste proche de zéro pour les applications à faible ou moyenne charge.

Méfiez-vous des boucles éternelles involontaires ou des fan-out récursifs indéfinis dans vos orchestrateurs. Ceux-ci peuvent devenir coûteux si vous les laissez hors de contrôle.

Gestion des erreurs et nouvelles tentatives
-------------------------------------------

Que se passe-t-il lorsqu'une erreur se produit quelque part au milieu du workflow ? Par exemple, un service de réservation de vols tiers peut ne pas être en mesure de traiter la demande :

![Gestion des erreurs](https://thepracticaldev.s3.amazonaws.com/i/p79a4ajxrhxh52h7cb84.png)

<figcaption>Une activité est malsaine</figcaption>

Cette situation est attendue par Durable Functions. Au lieu d'échouer silencieusement, la fonction d'activité envoie un message contenant des informations sur l'erreur à l'orchestrateur.

L'orchestrateur désérialise les détails de l'erreur et, au moment du replay, lève une exception .NET à partir de l'appel correspondant. Le développeur est libre de mettre un bloc `try .. catch` autour de l'appel et de gérer l'exception :

``` csharp
[FunctionName("SequentialWorkflow")]
public static async Task Sequential([OrchestrationTrigger] DurableOrchestrationContext context)
{
    var conf = await context.CallActivityAsync<ConfTicket>("BookConference", "ServerlessDays");
    try
    {
        var itinerary = MakeItinerary(/* ... */);
        await context.CallActivityAsync("BookFlight", itinerary);
    }
    catch (FunctionFailedException)
    {
        var alternativeItinerary = MakeAnotherItinerary(/* ... */);
        await context.CallActivityAsync("BookFlight", alternativeItinerary);
    }
    await context.CallActivityAsync("BookHotel", flight.Dates);
}
```

Le code ci-dessus revient à un "plan de secours" de réservation d'un autre itinéraire. Un autre modèle typique serait d'exécuter une activité compensatoire pour annuler les effets de toute action précédente (annuler la réservation de la conférence dans notre cas) et laisser le système dans un état propre.

Très souvent, l'erreur peut être transitoire, il peut donc être judicieux de réessayer l'opération échouée après une pause. C'est un scénario si courant que Durable Functions fournit une API dédiée :

``` csharp
var options = new RetryOptions(
    firstRetryInterval: TimeSpan.FromMinutes(1),                    
    maxNumberOfAttempts: 5);
options.BackoffCoefficient = 2.0;

await context.CallActivityWithRetryAsync("BookFlight", options, itinerary);
```

Le code ci-dessus indique à la bibliothèque de

- Réessayer jusqu'à 5 fois
- Attendre 1 minute avant la première nouvelle tentative
- Augmenter les délais avant chaque nouvelle tentative ultérieure par un facteur de 2 (1 min, 2 min, 4 min, etc.)

Le point important est que, une fois de plus, l'orchestrateur ne bloque pas pendant l'attente des nouvelles tentatives. Après un appel échoué, un message est programmé pour le moment dans le futur pour réexécuter l'orchestrateur et réessayer l'appel.

Sous-orchestrateurs
-------------------

Les processus commerciaux peuvent consister en de nombreuses étapes. Pour garder le code des orchestrateurs gérable, Durable Functions permet des orchestrateurs imbriqués. Un orchestrateur "parent" peut appeler des orchestrateurs enfants via la méthode `context.CallSubOrchestratorAsync` :

``` csharp
[FunctionName("CombinedOrchestrator")]
public static async Task CombinedOrchestrator([OrchestrationTrigger] DurableOrchestrationContext context)
{
    await context.CallSubOrchestratorAsync("BookTrip", serverlessDaysAmsterdam);
    await context.CallSubOrchestratorAsync("BookTrip", serverlessDaysHamburg);
}
```

Le code ci-dessus réserve deux conférences, l'une après l'autre.

Fan-out / Fan-in
----------------

Que se passe-t-il si nous voulons exécuter plusieurs activités en parallèle ?

Par exemple, dans l'exemple ci-dessus, nous pourrions souhaiter réserver deux conférences, mais l'ordre de réservation peut ne pas avoir d'importance. Cependant, lorsque les deux réservations sont terminées, nous voulons combiner les résultats pour produire un rapport de dépenses pour le département financier :

![Appels parallèles](https://thepracticaldev.s3.amazonaws.com/i/cb52udipp47s36ik71es.png)

<figcaption>Appels parallèles suivis d'une étape finale</figcaption>

Dans ce scénario, l'orchestrateur `BookTrip` accepte un paramètre d'entrée avec le nom de la conférence et retourne les informations de dépenses. `ReportExpenses` doit recevoir les deux dépenses combinées.

Cet objectif peut être facilement atteint en planifiant deux tâches (c'est-à-dire en envoyant deux messages) sans les attendre séparément. Nous utilisons la méthode familière `Task.WhenAll` pour attendre les deux et combiner les résultats :

``` csharp
[FunctionName("ParallelWorkflow")]
public static async Task Parallel([OrchestrationTrigger] DurableOrchestrationContext context)
{
    var amsterdam = context.CallSubOrchestratorAsync("BookTrip", serverlessDaysAmsterdam);
    var hamburg   = context.CallSubOrchestratorAsync("BookTrip", serverlessDaysHamburg);

    var expenses = await Task.WhenAll(amsterdam, hamburg);

    await context.CallActivityAsync("ReportExpenses", expenses);
}
```

Rappelez-vous que l'attente de la méthode `WhenAll` ne bloque pas de manière synchrone l'orchestrateur. Il quitte la première fois et redémarre ensuite deux fois sur les messages de réponse reçus des activités. Le premier redémarrage quitte à nouveau, et seul le deuxième redémarrage passe l'`await`.

`Task.WhenAll` retourne un tableau de résultats (un résultat par chaque tâche d'entrée), qui est ensuite passé à l'activité de rapport.

Un autre exemple de parallélisation pourrait être un workflow envoyant des e-mails à des centaines de destinataires. Un tel fan-out ne serait pas difficile avec des fonctions normales déclenchées par une file d'attente : il suffit d'envoyer des centaines de messages. Cependant, la combinaison des résultats, si nécessaire pour l'étape suivante du workflow, est assez difficile.

C'est simple avec un orchestrateur durable :

``` csharp
var emailSendingTasks =
    recepients
    .Select(to => context.CallActivityAsync<bool>("SendEmail", to))
    .ToArray();

var results = await Task.WhenAll(emailSendingTasks);

if (results.All(r => r)) { /* ... */ }
```

Faire des centaines d'allers-retours vers les activités et revenir pourrait causer de nombreux replays de l'orchestrateur. En tant qu'optimisation, si plusieurs fonctions d'activité se terminent à peu près au même moment, l'orchestrateur peut traiter plusieurs messages en interne comme un lot et redémarrer la fonction d'orchestrateur une seule fois par lot.

Autres concepts
---------------

Il existe de nombreux autres modèles activés par Durable Functions. Voici une liste rapide pour vous donner une perspective :

- Attendre la *première* tâche terminée dans une collection (plutôt que *toutes*) en utilisant la méthode `Task.WhenAny`. Utile pour les scénarios comme les délais d'attente ou les actions concurrentes.
- Mettre en pause le workflow pendant une période donnée ou jusqu'à une date limite.
- Attendre des événements externes, par exemple, intégrer l'interaction humaine dans le workflow.
- Exécuter des workflows récurrents, lorsque le flux se répète jusqu'à ce qu'une certaine condition soit remplie.

Une explication plus approfondie et des exemples de code se trouvent dans [la documentation](https://docs.microsoft.com/fr-fr/azure/azure-functions/durable/durable-functions-overview).

Conclusion
----------

Je suis fermement convaincu que les applications sans serveur utilisant une large gamme de services cloud gérés sont hautement bénéfiques pour de nombreuses entreprises, en raison à la fois du processus de développement rapide et du modèle de facturation correctement aligné.

La technologie sans serveur est encore jeune ; davantage de modèles architecturaux de haut niveau doivent émerger pour permettre des implémentations expressives et composables de grands systèmes commerciaux.

Azure Durable Functions suggère certaines des réponses possibles. Il combine la clarté et la lisibilité du code de style RPC séquentiel avec la puissance et la résilience de l'architecture pilotée par événements.

[La documentation](https://docs.microsoft.com/fr-fr/azure/azure-functions/durable/durable-functions-overview) pour Durable Functions est excellente, avec de nombreux exemples et guides pratiques. Apprenez-la, essayez-la pour vos scénarios réels, et faites-moi savoir votre opinion&mdash;je suis enthousiaste pour l'avenir sans serveur !

Remerciements
--------------

Un grand merci à [Katy Shimizu](https://twitter.com/kashimizMSFT), [Chris Gillum](https://twitter.com/cgillum), [Eric Fleming](https://twitter.com/efleming18), [KJ Jones](https://twitter.com/KevinJonesD), [William Liebenberg](https://twitter.com/William_DotNet), [Andrea Tosato](https://twitter.com/ATosato86) pour avoir révisé le brouillon de cet article et pour leurs contributions et suggestions précieuses.