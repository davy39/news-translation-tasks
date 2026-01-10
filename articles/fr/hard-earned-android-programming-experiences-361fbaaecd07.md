---
title: Expériences de programmation Android acquises à la dure
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-07-07T15:42:18.000Z'
originalURL: https://freecodecamp.org/news/hard-earned-android-programming-experiences-361fbaaecd07
coverImage: https://cdn-media-1.freecodecamp.org/images/1*5v2uWjgpnjKka7rhTyxzmA.png
tags:
- name: Android
  slug: android
- name: android app development
  slug: android-app-development
- name: androiddev
  slug: androiddev
- name: General Programming
  slug: programming
- name: Startups
  slug: startups
seo_title: Expériences de programmation Android acquises à la dure
seo_desc: 'By Arun (now voidmain.dev)

  This post, like Kent Beck says in his book Implementation Patterns, “…is based on
  a rather fragile premise that good code matters…”. But we all know that clean code
  matters as we’ve had to deal for so long with its lack. An...'
---

Par Arun (maintenant voidmain.dev)

Ce post, comme le dit Kent Beck dans son livre **Implementation Patterns**, « ...est basé sur une prémisse plutôt fragile que le bon code compte... ». Mais nous savons tous que le code propre compte, car nous avons dû gérer son absence pendant si longtemps. Et Kent aussi.

![Image](https://cdn-media-1.freecodecamp.org/images/D1y48LxFVLN-7DJq2e-GSt4r868LL7H45DCS)
_Kent Beck_

#### Le coût total de possession d'un désordre

Il y a quelques années, comme tout développeur Android naïf travaillant dans une startup en phase de démarrage en Inde, j'ai essayé de « bidouiller » des problèmes du monde réel, de « disrupter l'industrie » et de « faire une marque dans l'univers ». Sans me soucier du monde de la bonne conception logicielle ou de l'architecture, j'ai commencé à écrire du code pour construire une application Android qui deviendrait un jour l'une des plus grandes applications de santé grand public en Inde.

Sprint après sprint, bidouille après bidouille, les fonctionnalités étaient construites dans une course folle. _Build. Measure. Learn_. Le _time-to-market_ était important et chaque jour comptait. Le temps a filé, nous grandissions au rythme d'un membre d'équipe tous les 6 mois et l'application avait atteint le million de téléchargements.

![Image](https://cdn-media-1.freecodecamp.org/images/hLHerHSI0WHhoNSBZ8iTKX7KjbmvHDmEv90H)
_Les téléchargements et la note de notre application sur le Google Play Store._

À ce moment-là, l'application avait cessé d'être triviale et était devenue un client _multi-locataire_, si tant est que cela existe. Les fonctionnalités qui prenaient des heures au début prenaient maintenant des jours, parfois des semaines. Chaque Activity était composée de 1000+ lignes de code spaghetti, car Android ne se soucie pas inherently trop de la séparation des préoccupations. **Le coût total de possession d'un désordre nous avait considérablement ralentis.**

#### Le dilemme Android

Le code avait l'air laid, les _Activities_ géraient tout :

* _Threading_
* _I/O_
* _Computation_
* _Layouts_
* _Config changes_
* _What not_

Après tout, les _Activities_ sont des _Controllers_, non ? Ou sont-elles des _Views_ ? Je ne savais plus.

![Image](https://cdn-media-1.freecodecamp.org/images/DmDdWfbf3wRAQaclKUYmFWXXcgEOZsrDOh2L)
_MVC_

#### La grande refonte dans le ciel

Nous devions concevoir l'application de manière à ce que la modification d'une ligne de code quelque part ne casse pas quelque chose ailleurs. L'application devait être, comme le dit Uncle Bob, « robuste mais pas rigide, flexible mais pas fragile ».

![Image](https://cdn-media-1.freecodecamp.org/images/IfUwvie1Hd9-7z1AqmI7VATBu3Mct0kjXXvE)
_Robert « Uncle Bob » Martin_

C'est à ce moment-là que mon mentor et ami [Kashif Razzaqui](https://www.freecodecamp.org/news/hard-earned-android-programming-experiences-361fbaaecd07/undefined) a rejoint l'équipe pour nous aider à atténuer le désordre. La grande refonte n'a jamais eu lieu, mais nous avons refactorisé notre code à fond :

* Nous avons ajouté une couche « service » et avons déplacé tout le code non-UI vers eux, un service à la fois.
* Nous avons abandonné les _AsyncTasks_ et sommes passés aux _ListenableFutures_ en utilisant _Guava_.
* Nous avons remplacé _AsyncHttpClient_ par _OkHttp_.
* Mais surtout, nous avons commencé à lire beaucoup : Clean Code, Clean Architecture, SOLID, DRY, The Pragmatic Programmer, Java Concurrency In Practice, Domain Driven Design, etc.

Bientôt, nous avons commencé à voir les bénéfices de nos efforts. La productivité a augmenté, nous écrivions les choses plus rapidement, tout le monde était heureux.

Cela a duré jusqu'à ce que nous unifiions nos applications et que tout l'enfer se déchaîne. Le simple fait d'avoir une couche _service_ supplémentaire ne suffisait pas.

#### L'art du code propre

Après avoir regardé les vidéos d'Uncle Bob sur [Clean Architecture](https://www.youtube.com/results?search_query=clean+architecture&page=&utm_source=opensearch) plusieurs fois et avoir lu beaucoup sur l'architecture des applications Android, j'ai décidé d'expérimenter avec le [modèle de conception MVP et RxJava](https://github.com/esoxjem/MovieGuide).

Quelques jours après le début de l'expérimentation, nous avons décidé de passer à _RxJava_ et d'implémenter _MVP en utilisant Clean Architecture_. Nous nous sommes assurés d'encapsuler toutes les couches derrière des interfaces et de bien séparer les préoccupations.

* _La Vue_, généralement implémentée par un Fragment, contient une référence au présentateur. La seule chose que la vue fera est d'appeler une méthode du Présentateur chaque fois qu'il y a une action d'interface.
* _Le Présentateur_ est responsable de servir d'intermédiaire entre la _Vue_ et le _Modèle_. Il récupère les données du Modèle et les retourne formatées à la Vue. Mais contrairement au MVC typique, il décide également de ce qui se passe lorsque vous interagissez avec la Vue.
* _Le Modèle_ n'est que la passerelle vers la couche _domaine_ ou la _logique métier_.
* _L'Interactor_ traite les I/O et est le fournisseur de données à afficher dans la _Vue_.

Maintenant, il est beaucoup plus facile de remplacer une couche par une implémentation complètement nouvelle. La refonte de l'UI, une partie intégrante du développement d'applications Android, est devenue beaucoup plus facile. Les choses peuvent enfin avancer rapidement sans se casser.

#### La règle du scout

Il ne suffit pas d'écrire du code correctement, le code doit être **gardé propre** au fil du temps. Le fait est que le logiciel a une tendance à l'_entropie_. Nous avons tous vu le code se dégrader et se détériorer avec le temps, alors nous avons emprunté la règle simple des scouts : « Laissez le campement plus propre que vous ne l'avez trouvé. »

Si nous vérifions tous notre code un peu plus propre que lorsque nous l'avons extrait, le code ne pourrait tout simplement pas se dégrader. Le nettoyage n'a pas besoin d'être quelque chose de grand. Changez un nom de variable pour mieux, divisez une fonction qui est un peu trop grande, éliminez un petit morceau de duplication, nettoyez une instruction if composite.

#### Conclusion

Notre façon de construire une application scalable peut ne pas être « correcte » et vous pouvez ne pas être d'accord avec ce post. Après tout, tous les artistes martiaux ne sont pas d'accord sur le meilleur art martial, ou la meilleure technique au sein d'un ;)

Il existe de nombreuses approches différentes de MVP et de nombreuses solutions intéressantes pour l'adapter à Android. Le fait que nous ne pouvons pas nier est que le _Clean Code_ compte et vous ne pouvez tout simplement pas le balayer sous le tapis.

Ce post s'inspire fortement du **Clean Code** d'Uncle Bob et emprunte le titre à la [_conférence Droidcon de Kashif_](https://www.youtube.com/watch?v=dauMw_Bns0w) de 2011.

Si le _Clean Code_ compte pour vous, discutons :)   
_Twitter : [@_arunsasi](http://twitter.com/_arunsasi)_  
_LinkedIn :_ [https://www.linkedin.com/in/arunsasidharan](https://www.linkedin.com/in/arunsasidharan)

### Si vous avez aimé ce post, cliquez sur le petit cœur ! ❤