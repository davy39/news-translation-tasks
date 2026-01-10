---
title: How to set up Microsoft Orleans’ Reporting Dashboard
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
seo_title: null
seo_desc: 'By Russell Hammett Jr. (Kritner)

  Orleans is an easy to use actor framework, but how can you monitor your deployment?
  Luckily, there’s something simple to use — Orleans Dashboard!

  As a refresher — Orleans, like other actor model frameworks, is a means...'
---

By Russell Hammett Jr. (Kritner)

Orleans is an easy to use actor framework, but how can you monitor your deployment? Luckily, there’s something simple to use — [Orleans Dashboard](https://github.com/OrleansContrib/OrleansDashboard)!

As a refresher — Orleans, like other actor model frameworks, is a means of distributing compute across a series of machines that act as a cluster. In the case of Orleans, a lot of that cluster management is seemingly transparent, and abstracted away from the user. That is both awesome, and makes me a bit uncomfortable! Thankfully, the awesome people that built and/or use the product built an add-on dashboard to help alleviate some stress.

[Orleans Dashboard](https://github.com/OrleansContrib/OrleansDashboard) was suggested to me in the [Orleans Gitter](https://gitter.im/dotnet/orleans) when I was inquiring about how to look into “how my system is doing” when running a cluster. The dashboard is stupid simple to get started with, so let’s get going!

I’m using release [v0.30](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30) of [Kritner-Blogs/OrleansGettingStarted](https://github.com/Kritner-Blogs/OrleansGettingStarted) as my starting point. This will give us a few different grain types to play around with to watch the fancy new dashboard.

The README.md from [OrleansDashboard](https://github.com/OrleansContrib/OrleansDashboard) covers the setup very well. Since it’s so short and sweet, here are the basic steps:

* Add the `OrleansDashboard` package to our `Kritner.OrleansGettingStarted.SiloHost` project.
* Add a new option to the `ISiloHostBuilder` configuration.

That’s it!

#### Package Installation

Within the `Kritner.OrleansGettingStarted.SiloHost` project, add the following line (highlighted)

![Image](https://cdn-media-1.freecodecamp.org/images/1*dIg2bYGH-keppGEpeydE6A.png)
_New NuGet package `OrleansDashboard`_

#### Configure SiloHostBuilder

Again within the SiloHost project, modify the ISiloHostBuilder to have the following line prior to `Build()`:

```
.UseDashboard(options => { })
```

Should look like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*vDt9140Xpfonsf93ZrxP7g.png)
_Configure dashboard within builder_

There are a few configuration options we could make use of, but for simplicity, let’s just see what we have right now.

#### Firing it up

The only thing we need to do now is start up the SiloHost, and navigate to the default URL of `localhost:8080`. We’ll start the SiloHost as normal, by navigating to the SiloHost folder in a command prompt, and running `dotnet run`. Next navigate to [http://localhost:8080.](http://localhost:8080.) We should now be greeted with something like:

![Image](https://cdn-media-1.freecodecamp.org/images/1*YKJq8TmRwJ6L8sn37vtwUw.png)
_OrleansDashboard_

There’s a fair amount of information present on this, and the other pages that are provided in the OrleansDashboard. Additionally, the front end code is customizable so you could theoretically work in your own metrics. As you can see from the above, there are already some grains working their magic — new grains introduced by the dashboard itself.

Currently CPU/Memory usage is not visible from the .net core implementation of Orleans. Hopefully something will be done to remedy that in the future? Perhaps it’s a limitation of the API available in netstandard?

#### Showing off more grain activations

This dashboard is great and all, but how do I see it in action? Rather, not the default grains action? Well that’s easy! We just need to run a few grains.

I want to run a potentially large number of grains, perhaps the number of which is input by the user. To do that, I’m going to expand on the Polymorphism-based work we did in “[Updating Orleans Project to be more ready for new Orleans Examples!](https://medium.com/@kritner/updating-orleans-project-to-be-more-ready-for-new-orleans-examples-2105b29a46fd)”, by adding a new menu option.

> Note, I was having some trouble with my Client or Server getting or serving instances of grains. I have corrected this but will likely put in a GitHub issue and/or separate post to try to understand the reasoning behind it being an issue. The gist of the issue was code generation did not seem to be running on the silo builds for some reason, even though it did previously.

Anyway, onto the new `IOrleansFunction`:

```
public class ShowoffDashboard : IOrleansFunction{ public string Description => "Starts new activations of several grains, as to show off the OrleansDashboard.";
```

```
 public async Task PerformFunction(IClusterClient clusterClient) {  Console.WriteLine("How many activations would you like to do per grain? (100-500 perhaps?)");  var times = Console.ReadLine();
```

```
  if (!int.TryParse(times, out var result))  {   Console.WriteLine("invalid input, returning to menu.");   ConsoleHelpers.ReturnToMenu();  }
```

```
  Console.WriteLine($"About to start {result} instances of a grain.  Hold onto your butts.");  Console.WriteLine("Press any key to get started.");  Console.ReadKey();
```

```
  for (int i = 0; i < result; i++)  {   var helloGrain = clusterClient.GetGrain<IHelloWorld>(    Guid.NewGuid()   );   await helloGrain.SayHello(i.ToString());
```

```
   var statefulGrain = clusterClient.GetGrain<IVisitTracker>(    i.ToString()   );   await statefulGrain.Visit();  }
```

```
  Console.WriteLine("All done!");  ConsoleHelpers.ReturnToMenu(); }}
```

In the above, we’re simply prompting the user for a number input. Then running our two implemented grains that many times. We should be able to demonstrate the dashboard picking up the grain activations quite easily using this new `IOrleansFunction`.

It should look something like this when running:

Code changes (though minimal from the previous post) can be found here: [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35).

Note that there are additional changes not covered in this post between v0.3 and v0.35 related to the grain generation not firing. I will (probably) have another post regarding that at some point.

Related:

* [Getting Started with Microsoft Orleans](https://medium.com/@kritner/getting-started-with-microsoft-orleans-882cdac4307f?source=friends_link&sk=1fc3451d71a19dcb49f2c8bbeb6b079e)
* [Microsoft Orleans — Reusing Grains and Grain State](https://medium.com/@kritner/microsoft-orleans-reusing-grains-and-grain-state-136977facd42?source=friends_link&sk=f19cfa3f17665c3d700bfe0df56e27a9)
* [Updating Orleans Project to be more ready for new Orleans Examples!](https://medium.com/@kritner/updating-orleans-project-to-be-more-ready-for-new-orleans-examples-2105b29a46fd)
* [Microsoft Orleans — Dependency Injection](https://medium.com/@kritner/microsoft-orleans-dependency-injection-6379d52a7169?source=friends_link&sk=6c3883a5213d65eb251b56c717e0e4f2)
* [Microsoft Orleans — Easily switching between “development” and “production” configurations.](https://medium.com/@kritner/microsoft-orleans-easily-switching-between-development-and-production-configurations-20e109be6458?source=friends_link&sk=1e8fc6aa072a5b293d029c00012165b3)
* [Microsoft Orleans — Observers](https://medium.com/@kritner/microsoft-orleans-observables-5e0040c949cd?source=friends_link&sk=bcb921fdf593bdc97b9c5909b2730f2d)
* Starting point of code — [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.30)
* Ending point of code — [https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35](https://github.com/Kritner-Blogs/OrleansGettingStarted/releases/tag/v0.35)
* GitHub — [OrleansDashboard](https://github.com/OrleansContrib/OrleansDashboard)

