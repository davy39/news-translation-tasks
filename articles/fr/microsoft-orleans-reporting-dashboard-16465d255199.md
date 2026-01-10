---
title: Comment configurer le tableau de bord de reporting Microsoft Orleans
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-10-31T14:43:07.000Z'
originalURL: https://freecodecamp.org/news/microsoft-orleans-reporting-dashboard-16465d255199
coverImage: https://cdn-media-1.freecodecamp.org/images/1*YKJq8TmRwJ6L8sn37vtwUw.png
tags:
- name: C#
  slug: csharp
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment configurer le tableau de bord de reporting Microsoft Orleans
seo_desc: 'By Russell Hammett Jr. (Kritner)

  Orleans is an easy to use actor framework, but how can you monitor your deployment?
  Luckily, there’s something simple to use — Orleans Dashboard!

  As a refresher — Orleans, like other actor model frameworks, is a means...'
---

Par Russell Hammett Jr. (Kritner)

Orleans est un framework d'acteurs facile à utiliser, mais comment pouvez-vous surveiller votre déploiement ? Heureusement, il y a quelque chose de simple à utiliser — [Orleans Dashboard](https://github.com/OrleansContrib/OrleansDashboard) !

Pour rappel — Orleans, comme d'autres frameworks de modèle d'acteurs, est un moyen de distribuer le calcul sur une série de machines qui agissent comme un cluster. Dans le cas d'Orleans, une grande partie de cette gestion de cluster est apparemment transparente et abstraite pour l'utilisateur. C'est à la fois génial et cela me rend un peu mal à l'aise ! Heureusement, les personnes formidables qui ont construit et/ou utilisent le produit ont créé un tableau de bord complémentaire pour aider à soulager une partie du stress.

[Orleans Dashboard](https://github.com/OrleansContrib/OrleansDashboard) m'a été suggéré dans le [Orleans Gitter](https://gitter.im/dotnet/orleans) lorsque je demandais comment examiner "comment mon système se comporte" lors de l'exécution d'un cluster. Le tableau de bord est extrêmement simple à démarrer, alors commençons !

J'utilise la version [v0.30](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30) de [Kritner-Blogs/OrleansGettingStarted](https://github.com/Kritner-Blogs/OrleansGettingStarted) comme point de départ. Cela nous donnera quelques types de grains différents avec lesquels jouer pour observer le nouveau tableau de bord.

Le README.md de [OrleansDashboard](https://github.com/OrleansContrib/OrleansDashboard) couvre très bien la configuration. Comme il est si court et simple, voici les étapes de base :

* Ajoutez le package `OrleansDashboard` à notre projet `Kritner.OrleansGettingStarted.SiloHost`.
* Ajoutez une nouvelle option à la configuration `ISiloHostBuilder`.

C'est tout !

#### Installation du package

Dans le projet `Kritner.OrleansGettingStarted.SiloHost`, ajoutez la ligne suivante (surlignée)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dIg2bYGH-keppGEpeydE6A.png)
_Nouveau package NuGet `OrleansDashboard`_

#### Configurer SiloHostBuilder

À nouveau dans le projet SiloHost, modifiez le ISiloHostBuilder pour avoir la ligne suivante avant `Build()` :

```
.UseDashboard(options => { })
```

Cela devrait ressembler à :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDt9140Xpfonsf93ZrxP7g.png)
_Configurer le tableau de bord dans le builder_

Il y a quelques options de configuration que nous pourrions utiliser, mais pour simplifier, voyons simplement ce que nous avons maintenant.

#### Démarrer le tableau de bord

La seule chose que nous devons faire maintenant est de démarrer le SiloHost et de naviguer vers l'URL par défaut `localhost:8080`. Nous démarrerons le SiloHost normalement, en naviguant vers le dossier SiloHost dans une invite de commande et en exécutant `dotnet run`. Ensuite, naviguez vers [http://localhost:8080](http://localhost:8080). Nous devrions maintenant être accueillis avec quelque chose comme :

![Image](https://cdn-media-1.freecodecamp.org/images/1*YKJq8TmRwJ6L8sn37vtwUw.png)
_OrleansDashboard_

Il y a une quantité considérable d'informations présentes sur cette page et les autres pages fournies dans le OrleansDashboard. De plus, le code frontal est personnalisable, donc vous pourriez théoriquement intégrer vos propres métriques. Comme vous pouvez le voir ci-dessus, il y a déjà quelques grains qui font leur magie — de nouveaux grains introduits par le tableau de bord lui-même.

Actuellement, l'utilisation du CPU/mémoire n'est pas visible depuis l'implémentation .net core d'Orleans. Espérons que quelque chose sera fait pour remédier à cela à l'avenir ? Peut-être est-ce une limitation de l'API disponible dans netstandard ?

#### Montrer plus d'activations de grains

Ce tableau de bord est génial et tout, mais comment puis-je le voir en action ? Plutôt, pas l'action des grains par défaut ? Eh bien, c'est facile ! Nous devons simplement exécuter quelques grains.

Je veux exécuter un nombre potentiellement élevé de grains, peut-être un nombre saisi par l'utilisateur. Pour ce faire, je vais développer le travail basé sur le polymorphisme que nous avons fait dans "[Mise à jour du projet Orleans pour être plus prêt pour les nouveaux exemples Orleans !](https://medium.com/@kritner/updating-orleans-project-to-be-more-ready-for-new-orleans-examples-2105b29a46fd)", en ajoutant une nouvelle option de menu.

> Note : J'avais quelques problèmes avec mon client ou mon serveur qui obtenait ou servait des instances de grains. J'ai corrigé cela mais je vais probablement ouvrir un problème GitHub et/ou un article séparé pour essayer de comprendre la raison derrière ce problème. L'essentiel du problème était que la génération de code ne semblait pas s'exécuter sur les builds de silo pour une raison quelconque, même si elle le faisait auparavant.

En tout cas, voici la nouvelle `IOrleansFunction` :

```
public class ShowoffDashboard : IOrleansFunction{ public string Description => "Démarre de nouvelles activations de plusieurs grains, afin de montrer le OrleansDashboard.";
```

```
 public async Task PerformFunction(IClusterClient clusterClient) {  Console.WriteLine("Combien d'activations souhaitez-vous faire par grain ? (100-500 peut-être ?)");  var times = Console.ReadLine();
```

```
  if (!int.TryParse(times, out var result))  {   Console.WriteLine("entrée invalide, retour au menu.");   ConsoleHelpers.ReturnToMenu();  }
```

```
  Console.WriteLine($"Sur le point de démarrer {result} instances d'un grain. Accrochez-vous bien.");  Console.WriteLine("Appuyez sur n'importe quelle touche pour commencer.");  Console.ReadKey();
```

```
  for (int i = 0; i < result; i++)  {   var helloGrain = clusterClient.GetGrain<IHelloWorld>(    Guid.NewGuid()   );   await helloGrain.SayHello(i.ToString());
```

```
   var statefulGrain = clusterClient.GetGrain<IVisitTracker>(    i.ToString()   );   await statefulGrain.Visit();  }
```

```
  Console.WriteLine("Tout est terminé !");  ConsoleHelpers.ReturnToMenu(); }}
```

Dans ce qui précède, nous demandons simplement à l'utilisateur une entrée numérique. Ensuite, nous exécutons nos deux grains implémentés autant de fois. Nous devrions pouvoir démontrer que le tableau de bord capte les activations de grains assez facilement en utilisant cette nouvelle `IOrleansFunction`.

Cela devrait ressembler à quelque chose comme ceci lors de l'exécution :

Les changements de code (bien que minimes par rapport au précédent article) peuvent être trouvés ici : [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35).

Notez qu'il y a des changements supplémentaires non couverts dans cet article entre v0.3 et v0.35 liés à la génération de grains qui ne se déclenchait pas. J'aurai (probablement) un autre article à ce sujet à un moment donné.

Articles connexes :

* [Getting Started with Microsoft Orleans](https://medium.com/@kritner/getting-started-with-microsoft-orleans-882cdac4307f?source=friends_link&sk=1fc3451d71a19dcb49f2c8bbeb6b079e)
* [Microsoft Orleans — Réutilisation des grains et de l'état des grains](https://medium.com/@kritner/microsoft-orleans-reusing-grains-and-grain-state-136977facd42?source=friends_link&sk=f19cfa3f17665c3d700bfe0df56e27a9)
* [Mise à jour du projet Orleans pour être plus prêt pour les nouveaux exemples Orleans !](https://medium.com/@kritner/updating-orleans-project-to-be-more-ready-for-new-orleans-examples-2105b29a46fd)
* [Microsoft Orleans — Injection de dépendances](https://medium.com/@kritner/microsoft-orleans-dependency-injection-6379d52a7169?source=friends_link&sk=6c3883a5213d65eb251b56c717e0e4f2)
* [Microsoft Orleans — Basculer facilement entre les configurations "développement" et "production".](https://medium.com/@kritner/microsoft-orleans-easily-switching-between-development-and-production-configurations-20e109be6458?source=friends_link&sk=1e8fc6aa072a5b293d029c00012165b3)
* [Microsoft Orleans — Observateurs](https://medium.com/@kritner/microsoft-orleans-observables-5e0040c949cd?source=friends_link&sk=bcb921fdf593bdc97b9c5909b2730f2d)
* Point de départ du code — [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30)
* Point final du code — [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35)
* GitHub — [OrleansDashboard](https://github.com/OrleansContrib/OrleansDashboard)