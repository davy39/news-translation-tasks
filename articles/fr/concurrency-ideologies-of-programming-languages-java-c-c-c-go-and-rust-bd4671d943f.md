---
title: 'État draconien, libre ou nanny : idéologies de concurrency dans Java, C#,
  C, C++, Go et Rust'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-03T17:18:18.000Z'
originalURL: https://freecodecamp.org/news/concurrency-ideologies-of-programming-languages-java-c-c-c-go-and-rust-bd4671d943f
coverImage: https://cdn-media-1.freecodecamp.org/images/1*9cwOzRARFWi3osKGXCZsSw.jpeg
tags:
- name: concurrency
  slug: concurrency
- name: General Programming
  slug: programming
- name: programming languages
  slug: programming-languages
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: 'État draconien, libre ou nanny : idéologies de concurrency dans Java,
  C#, C, C++, Go et Rust'
seo_desc: 'By Srinath Perera

  Why we need Concurrency

  Once, there was a good old time when clock speed doubled every 18 months. This phenomenon
  was called Moore’s law. If a programmer’s program was not fast enough, they could
  wait, and soon computers would catch...'
---

Par Srinath Perera

### Pourquoi nous avons besoin de la Concurrency

Autrefois, il y avait une époque où la vitesse des processeurs doublait tous les 18 mois. Ce phénomène était appelé la loi de Moore. Si le programme d'un programmeur n'était pas assez rapide, il pouvait attendre, et bientôt les ordinateurs rattraperaient.

C'était trop beau pour durer, et cela n'a pas duré. Les concepteurs de CPU ont continué à suivre la loi de Moore en ajoutant plus de cœurs aux ordinateurs.

Cela a créé un problème pour les programmeurs. Dans le nouveau monde, nos programmes s'exécuteront deux fois plus vite tous les 18 mois, mais seulement s'il s'agit d'un programme parallèle qui utilise plus de cœurs.

Par conséquent, pour un programmeur, la capacité à écrire du code dans des environnements parallèles est une compétence critique. Cet article explore comment différents langages de programmation supportent les programmes parallèles et concurrents.

### Primitives Classiques de Concurrency

Presque tous les systèmes d'exploitation supportent plusieurs threads d'exécution. Cependant, les programmeurs concurrents ont besoin d'aide pour résoudre deux autres problèmes.

* Données Partagées — Les données partagées, si elles sont accédées de manière concurrente, peuvent produire des résultats inattendus.
* Signalisation entre les threads — Certains cas d'utilisation nécessitent que les programmeurs contrôlent l'ordre d'exécution des threads. D'autres exemples incluent le fait de vouloir que les threads attendent à un certain point, attendent un autre thread, s'exécutent dans un ordre spécifique, ne dépassent jamais un autre thread et n'aient pas plus de N threads dans la région critique.

Les langages de programmation fournissent différentes primitives pour aider les programmeurs à contrôler les situations ci-dessus. Examinons ces primitives classiques :

1. Verrous (également appelés Mutex) — assurent qu'un seul thread est exécuté dans des régions sélectionnées du code
2. Moniteurs — ils font la même chose, mais légèrement mieux que les verrous, car ils vous forcent à déverrouiller
3. Sémaphores (comptage) — abstractions puissantes qui peuvent supporter une large gamme de scénarios de coordination
4. Attendre-et-notifier — fait la même chose, mais est plus faible que les sémaphores. Le programmeur doit gérer les déclenchements de notification manqués avant l'attente
5. Variables Conditionnelles — permettent à un thread de dormir et de se réveiller lorsqu'une condition donnée se produit
6. Canaux et tampons avec attente conditionnelle — écoutent et collectent des messages s'il n'y a pas de thread pour les recevoir (avec des tampons optionnellement bornés)
7. Structures de données non bloquantes (telles que la file d'attente non bloquante, les compteurs atomiques) — Ce sont des structures de données intelligentes qui permettent l'accès à partir de nombreux threads sans utiliser de verrous ou une quantité minimale de verrous.

Ces primitives se chevauchent dans ce qu'elles peuvent faire. Tout langage de programmation peut obtenir toute la puissance de la concurrency avec seulement quelques-unes. Par exemple, les verrous et les sémaphores peuvent faire tous les cas d'utilisation de concurrency que vous pouvez imaginer.

### Support des Langages pour les Primitives

La primitive de concurrency n'est pas sélectionnée uniquement pour sa puissance. Différentes primitives ont différents modèles de programmation. Cela nécessite différentes façons de penser au problème. Différents langages de programmation ont sélectionné différents sous-ensembles qui correspondent le mieux à leur modèle de langage. Le choix dépend des goûts du concepteur ainsi que de la philosophie du langage.

Explorons quelques-uns de ces choix.

#### Java et C#

Java et C# ont choisi de ne pas choisir du tout. Les deux supportent toutes les primitives.

Java a commencé par ne supporter que les moniteurs (le mot-clé **synchronized**) et attendre-et-notifier. C'était un cauchemar d'envoyer des signaux entre les threads. Je me souviens avoir passé des heures sur les "signaux manqués" et de toujours me tromper.

Bientôt, les concepteurs de Java ont réalisé leur erreur. Ils ont ajouté un package de concurrency qui contient tout, y compris les structures de données non bloquantes.

La seule primitive non supportée dans ses formes pures est les canaux et les tampons. Cependant, si vous les voulez, il est facile de mimiquer les canaux avec des files d'attente et des tampons. Bien que votre implémentation ne correspondra jamais à Go ou Erlang en termes de performance.

C#, arrivant plus tard, a appris de Java. Il a également presque tout. C# a également quelques constructions d'aide de niveau supérieur que Java n'a pas. Cela résout des problèmes courants tels que les barrières. Pour plus de détails, consultez le [package de threading C#](https://msdn.microsoft.com/en-us/library/system.threading%28v=vs.110%29.aspx).

### C et C++

C dépendait initialement des appels du système d'exploitation pour faire du multithreading. À l'époque, le code n'était pas portable. Au lieu de cela, des bibliothèques de concurrency tierces fournissaient cette fonctionnalité. Malheureusement, comme le langage ne fixe pas l'API, il y avait de nombreuses bibliothèques disponibles.

Comme C et C++ sont les langages les plus proches du système d'exploitation, la recherche de pointe sur les threads est souvent réalisée avec ces deux langages. Par exemple, une recherche rapide a révélé [22 bibliothèques de concurrency C++](https://en.wikipedia.org/wiki/List_of_C%2B%2B_multi-threading_libraries) et [6 bibliothèques de concurrency C](https://stackoverflow.com/questions/5613646/threading-in-c-cross-platform). Il n'y a pas de manque de puissance.

Ces bibliothèques fournissent une technologie de pointe et de large portée. Cependant, en raison de la diversité des API, il n'y a pas beaucoup de programmeurs qui sont aussi compétents avec une API donnée.

### Erlang

Erlang a été conçu dès le départ pour la concurrency. Erlang donne un contrôle total des interactions entre les threads au programmeur. Les programmeurs effectuent toutes les communications via le passage de messages. C'est la source de la performance légendaire d'Erlang sur les ordinateurs multi-cœurs.

Cependant, il y a un prix à payer. Erlang ne supporte pas le partage d'état entre les threads. Ce n'est pas une erreur. L'état partagé déclenche la synchronisation entre les threads, qui ne sera pas sous le contrôle direct du programmeur. Une telle synchronisation réduit souvent les performances.

Par conséquent, l'expérience de programmation Erlang est étrangère à la plupart des programmeurs. Sa nature entièrement fonctionnelle n'aide pas non plus.

La principale construction de concurrency dans Erlang est les canaux. Elle intègre des tampons et supporte l'attente sur une condition. Par exemple, vous pouvez demander à un canal d'attendre jusqu'à ce qu'il reçoive un message qui satisfait une condition donnée. Chaque processus a un canal, et il ne peut recevoir que de ce canal.

En pratique, comme Erlang est un langage de programmation fonctionnelle, les verrous de mémoire partagée sont rarement nécessaires. Malheureusement, de tels cas d'utilisation existent. Comme Erlang n'a pas de mémoire partagée, vous ne pouvez pas verrouiller quelque chose. Cependant, vous pouvez créer un processus pour représenter un verrou. Vous acquérez et libérez un verrou en envoyant des messages au verrou, comme dans un système distribué.

Sauf si vous êtes un expert en langage de programmation qui connaît intimement la programmation fonctionnelle, les programmes résultants ont tendance à être compliqués et difficiles à déboguer. En choisissant Erlang, les programmeurs échangent le support de concurrency et la familiarité.

Si vous souhaitez en savoir plus, lisez ces articles : [Erlang pour la programmation concurrente](https://queue.acm.org/detail.cfm?id=1454463) et [Le guide du voyageur pour la concurrency](http://learnyousomeerlang.com/the-hitchhikers-guide-to-concurrency).

### Go

Go est très similaire à Erlang. [Son mode principal de concurrency est à travers les canaux et les tampons, et il supporte l'attente conditionnelle](https://www.golang-book.com/books/intro/10). Sa philosophie centrale pour la concurrency est : [Ne communiquez pas en partageant la mémoire ; au lieu de cela, partagez la mémoire en communiquant](https://golang.org/doc/effective_go.html#sharing).

Il y a, cependant, une différence fondamentale. Go vous fait confiance pour faire la bonne chose. Go vous permet de partager des données entre les threads et supporte à la fois les [mutex](https://gobyexample.com/mutexes) et les [sémaphores](https://github.com/golang/sync/blob/master/semaphore/semaphore.go). De plus, ils ont assoupli la restriction d'Erlang selon laquelle chaque canal est définitivement assigné à un thread. Vous pouvez créer un canal et le passer.

En résumé, Go veut que nous programmions la concurrency comme Erlang. Cependant, alors qu'Erlang l'impose, Go vous fait confiance pour faire la bonne chose. Si Erlang est draconien, Go est un état libre.

### Rust

Rust est également très similaire à Erlang et Go. Il communique en utilisant des canaux qui ont des tampons et une attente conditionnelle. Tout comme Go, il assouplit les restrictions d'Erlang [en vous permettant de faire du partage de mémoire](https://doc.rust-lang.org/book/second-edition/ch16-03-shared-state.html), en supportant le comptage de références atomiques et les verrous, et en vous permettant de passer des canaux d'un thread à un autre.

Cependant, Rust va encore plus loin. Alors que Go vous fait confiance pour faire la bonne chose, Rust vous assigne un mentor qui s'assoit avec vous et se plaint si vous essayez de faire la mauvaise chose. Le mentor de Rust est le compilateur. Il effectue une analyse sophistiquée pour déterminer la propriété des valeurs qui sont passées entre les threads et fournit des erreurs de compilation s'il y a des problèmes potentiels.

Voici une citation des documents Rust.

> Les règles de propriété jouent un rôle vital dans l'envoi de messages car elles nous aident à écrire du code sûr et concurrent. Prévenir les erreurs dans la programmation concurrente est l'avantage que nous obtenons en faisant le compromis de devoir penser à la propriété tout au long de nos programmes Rust. — [Passage de messages avec propriété des valeurs](https://doc.rust-lang.org/book/second-edition/ch16-02-message-passing.html).

Si Erlang est draconien et Go est un état libre, alors Rust est un état nanny.

Le débogage des programmes concurrents est un cauchemar. Dans une mauvaise journée, cela peut prendre des jours. Donc j'apprécie ce que Rust essaie de faire via l'analyse au niveau du compilateur.

Cependant, si vous n'êtes pas expérimenté en concurrency et essayez d'écrire un programme Rust concurrent, cela vous énervera. Quoi que vous fassiez, il se plaindra de la concurrency dans un langage cryptique. Lorsque vous changerez, il dira autre chose, et ainsi de suite. Jusqu'à ce que vous compreniez la concurrency en détail, cela ne sera pas facile.

En revanche, Go donne une fausse sécurité au programmeur, qui pense que sa tâche, souvent à tort, est terminée. Ils pourraient en payer le prix plus tard. Cependant, ils ne paieront que si le code arrive jamais en production, si l'utilisateur rencontre jamais le scénario, et si cette erreur est détectée. Cela fait beaucoup de "si". Bien que ce soit injuste, les chances sont que le programmeur pourrait s'en tirer. Les humains ne sont pas très doués pour la [gratification différée](https://www.psychologytoday.com/us/blog/your-emotional-meter/201712/the-benefits-delaying-gratification) et la [vision à long terme](http://www.oxfordaspiremuseums.org/long-view-how-futures-thinking-can-help-us-plan-and-innovate) de toute façon. Donc les programmeurs préfèrent souvent Go à Rust.

Rust essaie d'aider, mais c'est rarement une aide qui est appréciée. Personne n'aime un état nanny.

> _Rust n'est pas aussi populaire qu'il le mérite, car trop de développeurs à courte vue sont énervés par la stricte discipline de Rust, au lieu d'apprécier l'immense pouvoir qu'ils gagnent de cette stricte discipline._ — [rjc2013](https://www.reddit.com/r/rust/comments/8x1myq/concurrency_ideologies_of_programming_languages/e21xwqy/)

Pour plus d'informations, veuillez lire [Comment les primitives de concurrency dans Rust se comparent à celles dans Go](https://news.ycombinator.com/item?id=7851274.)?

### Conclusion

En ce qui concerne les idéologies de concurrency, les langages de programmation vous donnent un choix : un état libre (Go), un état draconien (Erlang), ou un état nanny (Rust).

Si vous souhaitez en apprendre davantage, je vous recommande deux ressources.

Premièrement, lisez le [Petit livre des sémaphores](http://greenteapress.com/wp/semaphores/), qui vous enseigne tout sur les verrous et les sémaphores.

Deuxièmement, si vous voulez comprendre les canaux et le modèle Erlang, [consultez MPI](http://mpitutorial.com/). Vous pourriez penser que MPI est un langage mort. Ce n'est pas le cas. La plupart des simulations scientifiques sont encore réalisées avec MPI. La météo est prédite par lui, les véhicules sont conçus avec lui, et les médicaments sont découverts avec lui. La science progresse littéralement en utilisant MPI. MPI utilise la concurrency de manières que nous ne pourrions jamais imaginer. Pour un aperçu, veuillez consulter [MPI Communication Primitives](http://www.mathcs.emory.edu/~cheung/Courses/355/Syllabus/92-MPI/group-comm.html).

Si vous suivez les deux suggestions ci-dessus, vous repartirez avec une appréciation de la complexité et des possibilités de la concurrency. C'est un sujet qui prend une vie à maîtriser.

J'espère que cet article a été utile. J'ai étudié ces langages en réfléchissant à un modèle de concurrency pour Ballerina. Ballerina est un nouveau langage de programmation conçu pour les environnements distribués afin d'écrire des microservices et d'intégrer des API. Il inclut de nouvelles fonctionnalités de concurrency, telles que le verrouillage adaptatif. Il analyse le code et essaie de maintenir les verrous pendant le temps le plus court possible. Consultez-le sur [https://ballerina.io.](https://ballerina.io.)