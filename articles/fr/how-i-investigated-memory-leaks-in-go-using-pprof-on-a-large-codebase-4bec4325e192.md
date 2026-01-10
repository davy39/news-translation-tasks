---
title: Comment j'ai enquêté sur les fuites de mémoire en Go en utilisant pprof sur
  une grande base de code
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-11T20:16:13.000Z'
originalURL: https://freecodecamp.org/news/how-i-investigated-memory-leaks-in-go-using-pprof-on-a-large-codebase-4bec4325e192
coverImage: https://cdn-media-1.freecodecamp.org/images/0*7A3B-JS9mz8nyqmk
tags:
- name: debugging
  slug: debugging
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: technology
  slug: technology
seo_title: Comment j'ai enquêté sur les fuites de mémoire en Go en utilisant pprof
  sur une grande base de code
seo_desc: 'By Jonathan Levison

  I have been working with Go for the better part of the year, implementing a scalable
  blockchain infrastructure at Orbs, and it’s been an exciting year. Over the course
  of 2018, we researched on which language to choose for our blo...'
---

Par Jonathan Levison

Je travaille avec Go depuis la majeure partie de l'année, en implémentant une infrastructure blockchain scalable chez Orbs, et cela a été une année excitante. Au cours de l'année 2018, nous avons recherché quel langage choisir pour notre implémentation de blockchain. Cela nous a conduit à choisir Go en raison de notre compréhension qu'il a une bonne communauté et un ensemble d'outils amazing.

Ces dernières semaines, nous entrons dans les phases finales d'intégration de notre système. Comme dans tout grand système, les problèmes de dernière phase qui incluent des problèmes de performance, en particulier les fuites de mémoire, peuvent survenir. Alors que nous intégrions le système, nous avons réalisé que nous en avions trouvé une. Dans cet article, je vais aborder les spécificités de la façon d'enquêter sur une fuite de mémoire en Go, en détaillant les étapes prises pour la trouver, la comprendre et la résoudre.

L'ensemble d'outils offert par Golang est exceptionnel mais a ses limitations. En touchant d'abord à celles-ci, la plus grande est la capacité limitée à enquêter sur les vidages de mémoire complets. Un vidage de mémoire complet serait l'image de la mémoire (ou de la mémoire utilisateur) prise par le processus exécutant le programme.

Nous pouvons imaginer le mappage de la mémoire comme un arbre, et le parcours de cet arbre nous mènerait à travers les différentes allocations d'objets et les relations. Cela signifie que ce qui est à la racine est la raison de "retenir" la mémoire et de ne pas la GC (Garbage Collecting). Puisque dans Go il n'y a pas de moyen simple d'analyser le vidage de mémoire complet, il est difficile de trouver les racines d'un objet qui n'est pas GC.

Au moment de l'écriture, nous n'avons pas été en mesure de trouver un outil en ligne qui puisse nous aider avec cela. Puisqu'il existe un format de vidage de mémoire et un moyen assez simple de l'exporter depuis le package de débogage, il se pourrait qu'il y en ait un utilisé chez Google. En cherchant en ligne, il semble que cela soit dans le pipeline de Golang, créant un visualiseur de vidage de mémoire, mais il ne semble pas que quelqu'un travaille dessus. Cela dit, même sans accès à une telle solution, avec les outils existants, nous pouvons généralement trouver la cause racine.

#### Fuites de mémoire

Les fuites de mémoire, ou pression mémoire, peuvent prendre de nombreuses formes dans le système. Habituellement, nous les traitons comme des bugs, mais parfois leur cause racine peut être dans des décisions de conception.

Alors que nous construisons notre système sous des principes de conception émergents, de telles considérations ne sont pas jugées importantes et c'est acceptable. Il est plus important de construire le système de manière à **éviter les optimisations prématurées** et à permettre de les effectuer plus tard, à mesure que le code mature, plutôt que de le sur-ingénierer dès le départ. Cependant, quelques exemples courants de problèmes de **pression mémoire** qui se matérialisent sont :

* Trop d'allocations, représentation incorrecte des données
* Utilisation intensive de la réflexion ou des chaînes de caractères
* Utilisation de variables globales
* Goroutines orphelines, sans fin

En Go, la manière la plus simple de créer une fuite de mémoire est de définir une variable globale, un tableau, et d'ajouter des données à ce tableau. Cet [excellent article de blog décrit](https://medium.com/dm03514-tech-blog/sre-debugging-simple-memory-leaks-in-go-e0a9e6d63d4d) ce cas de manière approfondie.

Alors pourquoi j'écris cet article ? Lorsque je faisais des recherches sur ce cas, j'ai trouvé de nombreuses ressources sur les fuites de mémoire. Pourtant, en réalité, les systèmes ont plus de 50 lignes de code et une seule structure. Dans de tels cas, trouver la source d'un problème de mémoire est beaucoup plus complexe que ce que cet exemple décrit.

Golang nous offre un outil amazing appelé `pprof`. Cet outil, une fois maîtrisé, peut aider à enquêter et très probablement à trouver tout problème de mémoire. Un autre objectif qu'il a est d'enquêter sur les problèmes de CPU, mais je n'aborderai rien de lié au CPU dans cet article.

#### go tool pprof

Couvrir tout ce que fait cet outil nécessiterait plus d'un article de blog. Une chose qui a pris un certain temps est de découvrir comment utiliser cet outil pour obtenir quelque chose d'actionnable. Je vais me concentrer dans cet article sur la fonctionnalité liée à la mémoire.

Le package `pprof` crée un fichier de vidage échantillonné du tas, que vous pouvez ensuite analyser / visualiser pour obtenir une carte des deux éléments suivants :

* Allocations de mémoire actuelles
* Allocations de mémoire totales (cumulatives)

L'outil a la capacité de comparer des instantanés. Cela peut vous permettre de comparer un affichage de différence de temps entre ce qui s'est passé maintenant et il y a 30 secondes, par exemple. Pour les scénarios de stress, cela peut être utile pour aider à localiser les zones problématiques de votre code.

#### Profils pprof

La manière dont pprof fonctionne est en utilisant des profils.

Un Profil est une collection de traces de pile montrant les séquences d'appels qui ont conduit à des instances d'un événement particulier, tel qu'une allocation.

Le fichier [runtime/pprof/pprof.go](https://golang.org/src/runtime/pprof/pprof.go) contient les informations détaillées et l'implémentation des profils.

Go a plusieurs profils intégrés que nous pouvons utiliser dans des cas courants :

* goroutine — traces de pile de toutes les goroutines actuelles
* heap — un échantillonnage des allocations de mémoire des objets actifs
* allocs — un échantillonnage de toutes les allocations de mémoire passées
* threadcreate — traces de pile qui ont conduit à la création de nouveaux threads OS
* block — traces de pile qui ont conduit au blocage sur des primitives de synchronisation
* mutex — traces de pile des détenteurs de mutex contestés

Lorsque nous examinons les problèmes de mémoire, nous nous concentrerons sur le profil de tas. Le profil d'allocs est identique en ce qui concerne la collecte de données qu'il effectue. La différence entre les deux est la manière dont l'outil pprof les lit au moment du démarrage. Le profil _Allocs_ démarrera pprof dans un mode qui affiche le nombre total d'octets alloués depuis le début du programme (y compris les octets collectés par le garbage collector). Nous utiliserons généralement ce mode lorsque nous essaierons de rendre notre code plus efficace.

#### Le tas

En abstrait, c'est là que l'OS (Système d'exploitation) stocke la mémoire des objets utilisés par notre code. C'est la mémoire qui est ensuite "garbage collected", ou libérée manuellement dans les langages non garbage collected.

Le tas n'est pas le seul endroit où les allocations de mémoire se produisent, une partie de la mémoire est également allouée dans la pile. Le but de la pile est à court terme. En Go, la pile est généralement utilisée pour les affectations qui se produisent à l'intérieur de la fermeture d'une fonction. Un autre endroit où Go utilise la pile est lorsque le compilateur "sait" combien de mémoire doit être réservée avant l'exécution (par exemple, les tableaux de taille fixe). Il existe un moyen d'exécuter le compilateur Go pour qu'il produise une analyse des endroits où les allocations "échappent" de la pile vers le tas, mais je n'aborderai pas cela dans cet article.

Alors que les données du tas doivent être "libérées" et gc-ed, les données de la pile ne le doivent pas. Cela signifie qu'il est beaucoup plus efficace d'utiliser la pile lorsque cela est possible.

Ceci est un résumé des différents emplacements où les allocations de mémoire se produisent. Il y a beaucoup plus à dire, mais cela sera en dehors du cadre de cet article.

#### Obtention des données de tas avec pprof

Il existe deux principales méthodes pour obtenir les données pour cet outil. La première fera généralement partie d'un test ou d'une branche et inclut l'importation de `runtime/pprof` puis l'appel de `pprof.WriteHeapProfile(some_file)` pour écrire les informations du tas.

Notez que `WriteHeapProfile` est un sucre syntaxique pour exécuter :

```
// lookup prend un nom de profil
pprof.Lookup("heap").WriteTo(some_file, 0)
```

Selon la documentation, `WriteHeapProfile` existe pour la compatibilité ascendante. Les autres profils n'ont pas de tels raccourcis et vous devez utiliser la fonction `Lookup()` pour obtenir leurs données de profil.

La seconde méthode, qui est la plus intéressante, est de l'activer via HTTP (points de terminaison basés sur le web). Cela vous permet d'extraire les données de manière ad hoc, à partir d'un conteneur en cours d'exécution dans votre environnement e2e / test ou même à partir de la "production". C'est un autre point où l'environnement d'exécution et l'ensemble d'outils de Go excellent. La documentation complète du package se trouve [ici](https://golang.org/pkg/net/http/pprof/), mais en résumé, vous devrez l'ajouter à votre code comme suit :

```
import (  "net/http"  _ "net/http/pprof")
```

```
...
```

```
func main() {  ...  http.ListenAndServe("localhost:8080", nil)}
```

L'effet "secondaire" de l'importation de `net/http/pprof` est l'enregistrement des points de terminaison pprof sous la racine du serveur web à `/debug/pprof`. Maintenant, en utilisant curl, nous pouvons obtenir les fichiers d'informations de tas à investiguer :

```
curl -sK -v http://localhost:8080/debug/pprof/heap > heap.out
```

L'ajout de `http.ListenAndServe()` ci-dessus n'est requis que si votre programme n'avait pas d'écouteur http auparavant. Si vous en avez un, il s'y accrochera et il n'est pas nécessaire d'écouter à nouveau. Il existe également des moyens de le configurer en utilisant `ServeMux.HandleFunc()` ce qui serait plus logique pour un programme http plus complexe.

#### Utilisation de pprof

Nous avons donc collecté les données, que faire maintenant ? Comme mentionné ci-dessus, il existe deux principales stratégies d'analyse de la mémoire avec pprof. L'une consiste à examiner les allocations actuelles (en octets ou en nombre d'objets), appelée `inuse`. L'autre consiste à examiner tous les octets alloués ou le nombre d'objets tout au long du temps d'exécution du programme, appelée `alloc`. Cela signifie, peu importe si cela a été gc-ed, une somme de tout ce qui a été échantillonné.

C'est un bon endroit pour réitérer que le profil **_heap_** est un échantillonnage des allocations de mémoire. `pprof` utilise en arrière-plan la fonction `runtime.MemProfile`, qui par défaut collecte des informations d'allocation sur chaque 512 Ko d'octets alloués. Il est possible de changer MemProfile pour collecter des informations sur tous les objets. Notez que très probablement, cela ralentira votre application.

Cela signifie que par défaut, il y a une certaine chance qu'un problème puisse survenir avec des objets plus petits qui échapperont au radar de pprof. Pour une grande base de code / un programme de longue durée, ce n'est pas un problème.

Une fois que nous avons collecté le fichier de profil, il est temps de le charger dans la console interactive que pprof offre. Faites-le en exécutant :

```
> go tool pprof heap.out
```

Observons les informations affichées

```
Type: inuse_spaceTime: 22 janv. 2019 à 13:08 (IST)Mode interactif (tapez "help" pour les commandes, "o" pour les options)(pprof)
```

La chose importante à noter ici est `Type: inuse_space`. Cela signifie que nous examinons les données d'allocation d'un moment spécifique (lorsque nous avons capturé le profil). Le type est la valeur de configuration de `sample_index`, et les valeurs possibles sont :

* inuse_space — quantité de mémoire allouée et non libérée
* inuse_objects — quantité d'objets alloués et non libérés
* alloc_space — quantité totale de mémoire allouée (indépendamment de la libération)
* alloc_objects — quantité totale d'objets alloués (indépendamment de la libération)

Maintenant, tapez `top` dans l'interactif, la sortie sera les principaux consommateurs de mémoire

Nous pouvons voir une ligne nous informant des `Dropped Nodes`, cela signifie qu'ils sont filtrés. Un nœud est une entrée d'objet, ou un « nœud » dans l'arbre. Supprimer des nœuds est une bonne idée pour réduire le bruit, mais parfois cela peut cacher la cause racine d'un problème de mémoire. Nous verrons un exemple de cela alors que nous continuons notre enquête.

Si vous souhaitez inclure toutes les données du profil, ajoutez l'option `-nodefraction=0` lors de l'exécution de pprof ou tapez `nodefraction=0` dans l'interactif.

Dans la liste générée, nous pouvons voir deux valeurs, `flat` et `cum`.

* **flat** signifie que la mémoire allouée par cette fonction et est détenue par cette fonction
* **cum** signifie que la mémoire a été allouée par cette fonction ou une fonction qu'elle a appelée dans la pile

Ces informations seules peuvent parfois nous aider à comprendre s'il y a un problème. Prenons par exemple un cas où une fonction est responsable de l'allocation de beaucoup de mémoire mais ne la détient pas. Cela signifierait qu'un autre objet pointe vers cette mémoire et la maintient allouée, ce qui signifie que nous pourrions avoir un problème de conception du système ou un bug.

Un autre truc intéressant à propos de `top` dans la fenêtre interactive est qu'il exécute en réalité `top10`. La commande top prend en charge le format `topN` où `N` est le nombre d'entrées que vous souhaitez voir. Dans le cas collé ci-dessus, taper `top70` par exemple, afficherait tous les nœuds.

#### Visualisations

Alors que `topN` donne une liste textuelle, il existe plusieurs options de visualisation très utiles qui accompagnent pprof. Il est possible de taper `png` ou `gif` et bien d'autres (voir `go tool pprof -help` pour une liste complète).

Sur notre système, la sortie visuelle par défaut ressemble à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*zX28meov6lzXVo4nCkcNvQ.png)

Cela peut être intimidant au premier abord, mais c'est la visualisation des flux d'allocation de mémoire (selon les traces de pile) dans un programme. La lecture du graphique n'est pas aussi compliquée qu'il n'y paraît. Un carré blanc avec un nombre montre l'espace alloué (et le cumul de la quantité de mémoire qu'il prend actuellement sur le bord du graphique), et chaque rectangle plus large montre la fonction d'allocation.

Notez que dans l'image ci-dessus, j'ai pris un png d'un mode d'exécution `inuse_space`. De nombreuses fois, vous devriez également jeter un coup d'œil à `inuse_objects`, car cela peut aider à trouver des problèmes d'allocation.

#### Creuser plus profondément, trouver une cause racine

Jusqu'à présent, nous avons pu comprendre ce qui alloue de la mémoire dans notre application pendant l'exécution. Cela nous aide à avoir une idée de la manière dont notre programme se comporte (ou se comporte mal).

Dans notre cas, nous avons pu voir que la mémoire est retenue par `membuffers`, qui est notre [bibliothèque de sérialisation de données](https://github.com/orbs-network/membuffers). Cela ne signifie pas que nous avons une fuite de mémoire dans ce segment de code, cela signifie que la mémoire est retenue par cette fonction. Il est important de comprendre comment lire le graphique, et la sortie de pprof en général. Dans ce cas, comprendre que lorsque nous sérialisons des données, cela signifie que nous allouons de la mémoire à des structures et à des objets primitifs (int, string), elle n'est jamais libérée.

En sautant aux conclusions ou en interprétant mal le graphique, nous aurions pu supposer qu'un des nœuds sur le chemin de la sérialisation est responsable de la rétention de la mémoire, par exemple :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Yzeo5J1H0T6w6mFdgUDllQ.png)
_sous-ensemble du graphique_

Quelque part dans la chaîne, nous pouvons voir notre bibliothèque de journalisation, responsable de >50 Mo de mémoire allouée. Il s'agit de mémoire allouée par des fonctions appelées par notre logger. En y réfléchissant, cela est en fait attendu. Le logger provoque des allocations de mémoire car il doit sérialiser les données pour les sortir dans le journal et ainsi provoque des allocations de mémoire dans le processus.

Nous pouvons également voir que dans le chemin d'allocation, la mémoire n'est retenue que par la sérialisation et rien d'autre. De plus, la quantité de mémoire retenue par le logger est d'environ 30 % du total. Ce qui précède nous indique que, très probablement, le problème n'est pas avec le logger. Si c'était 100 %, ou quelque chose de proche, alors nous aurions dû regarder là — mais ce n'est pas le cas. Ce que cela pourrait signifier, c'est que quelque chose est journalisé qui ne devrait pas l'être, mais ce n'est pas une fuite de mémoire par le logger.

C'est un bon moment pour introduire une autre commande `pprof` appelée `list`. Elle accepte une expression régulière qui servira de filtre pour ce qu'il faut lister. Le 'list' est en fait le code source annoté lié à l'allocation. Dans le contexte du logger que nous examinons, nous exécuterons `list RequestNew` car nous souhaitons voir les appels effectués au logger. Ces appels proviennent de deux fonctions qui se trouvent commencer par le même préfixe.

Nous pouvons voir que les allocations effectuées se trouvent dans la colonne `cum`, ce qui signifie que la mémoire allouée est retenue dans la pile d'appels. Cela correspond à ce que le graphique montre également. À ce stade, il est facile de voir que la raison pour laquelle le logger allouait la mémoire est que nous lui avons envoyé l'objet 'block' entier. Il devait sérialiser certaines parties de celui-ci au minimum (nos objets sont des objets membuffer, qui implémentent toujours une fonction `String()`). Est-ce un message de journal utile, ou une bonne pratique ? Probablement pas, mais ce n'est pas une fuite de mémoire, ni du côté du logger ni du code qui a appelé le logger.

`list` peut trouver le code source lorsqu'il le recherche sous votre environnement `GOPATH`. Dans les cas où la racine qu'il recherche ne correspond pas, ce qui dépend de votre machine de construction, vous pouvez utiliser l'option `-trim_path`. Cela aidera à le corriger et vous permettra de voir le code source annoté. N'oubliez pas de régler votre git sur le bon commit qui était en cours d'exécution lorsque le profil de tas a été capturé.

#### Alors pourquoi la mémoire est-elle retenue ?

Le contexte de cette enquête était le soupçon que nous avions un problème — une fuite de mémoire. Nous sommes arrivés à cette notion lorsque nous avons vu que la consommation de mémoire était plus élevée que ce que nous attendions du système. En plus de cela, nous l'avons vue augmenter constamment, ce qui était un autre indicateur fort de « il y a un problème ici ».

À ce stade, dans le cas de Java ou .Net, nous ouvririons une analyse des « racines gc » ou un profileur et nous arriverions à l'objet réel qui référence ces données, et qui crée la fuite. Comme expliqué, ce n'est pas exactement possible avec Go, à la fois à cause d'un problème d'outillage mais aussi à cause de la représentation mémoire de bas niveau de Go.

Sans entrer dans les détails, nous ne pensons pas que Go retienne quel objet est stocké à quelle adresse (sauf pour les pointeurs peut-être). Cela signifie qu'en réalité, comprendre quelle adresse mémoire représente quel membre de votre objet (struct) nécessitera une sorte de mappage à la sortie d'un profil de tas. En théorie, cela pourrait signifier que avant de prendre un vidage de mémoire complet, on devrait aussi prendre un profil de tas pour que les adresses puissent être mappées à la ligne et au fichier d'allocation et ainsi à l'objet représenté dans la mémoire.

À ce stade, parce que nous sommes familiers avec notre système, il était facile de comprendre que ce n'était plus un bug. C'était (presque) par conception. Mais continuons à explorer comment obtenir les informations des outils (pprof) pour trouver la cause racine.

Lorsque nous définissons `nodefraction=0`, nous verrons toute la carte des objets alloués, y compris les plus petits. Regardons la sortie :

![Image](https://cdn-media-1.freecodecamp.org/images/1*VaWXnlay3BfCwKGd5ypHUg.png)
_visualisation de la mémoire avec nodefraction=0_

Nous avons deux nouveaux sous-arbres. Rappelons encore une fois, le profil de tas pprof est un échantillonnage des allocations de mémoire. Pour notre système, cela fonctionne — nous ne manquons aucune information importante. Le nouvel arbre plus long, en vert, qui est complètement déconnecté du reste du système est le test runner, il n'est pas intéressant.

![Image](https://cdn-media-1.freecodecamp.org/images/1*jj9eIWDafkAMiC_plwhoww.png)
_le système était configuré pour "fuiter" ?_

Le plus court, en bleu, qui a une arête le connectant à l'ensemble du système est `inMemoryBlockPersistance`. Ce nom explique également la "fuite" que nous imaginions avoir. Il s'agit du backend de données, qui stocke toutes les données en mémoire et ne les persiste pas sur le disque. Ce qui est intéressant à noter, c'est que nous avons pu voir immédiatement qu'il retient deux grands objets. Pourquoi deux ? Parce que nous pouvons voir que l'objet a une taille de 1,28 Mo et que la fonction retient 2,57 Mo, ce qui signifie deux d'entre eux.

Le problème est bien compris à ce stade. Nous aurions pu utiliser delve (le débogueur) pour voir que c'est le tableau qui contient tous les blocs pour le pilote de persistance en mémoire que nous avons.

#### Alors, qu'aurions-nous pu corriger ?

Eh bien, cela a été une erreur humaine. Bien que le processus ait été éducatif (et partager, c'est prendre soin), nous ne nous sommes pas améliorés, ou l'avons-nous fait ?

Il y avait une chose qui "sentait" encore mauvais avec ces informations de tas. Les données désérialisées prenaient trop de mémoire, pourquoi 142 Mo pour quelque chose qui devrait prendre substantiellement moins ? . . pprof peut répondre à cela — en fait, il existe pour répondre à de telles questions exactement.

Pour examiner le code source annoté de la fonction, nous exécuterons `list lazy`. Nous utilisons `lazy`, car le nom de la fonction que nous recherchons est `lazyCalcOffsets()` et nous savons qu'aucune autre fonction dans notre code ne commence par lazy. Taper `list lazyCalcOffsets` fonctionnerait également, bien sûr.

Nous pouvons voir deux informations intéressantes. Encore une fois, rappelez-vous que le profil de tas pprof échantillonne les informations sur les allocations. Nous pouvons voir que les nombres `flat` et `cum` sont les mêmes. Cela indique que la mémoire allouée est également retenue par ces points d'allocation.

Ensuite, nous pouvons voir que le make() prend de la mémoire. Cela a du sens, c'est le pointeur vers la structure de données. Pourtant, nous voyons également que l'affectation à la ligne 43 prend de la mémoire, ce qui signifie qu'elle crée une allocation.

Cela nous a éduqués sur les maps, où une affectation à une map n'est pas une affectation de variable directe. [Cet article](https://dave.cheney.net/2018/05/29/how-the-go-runtime-implements-maps-efficiently-without-generics) entre dans les détails de la manière dont les maps fonctionnent. En bref, une map a un surcoût, et plus il y a d'éléments, plus ce surcoût sera "coûteux" en comparaison avec une slice.

Ce qui suit doit être pris avec des pincettes : Il serait acceptable de dire que l'utilisation d'une `map[int]T`, lorsque les données ne sont pas clairsemées ou peuvent être converties en indices séquentiels, devrait généralement être tentée avec une implémentation de slice si la consommation de mémoire est une considération pertinente. Pourtant, une grande slice, lorsqu'elle est étendue, pourrait ralentir une opération, alors que dans une map, ce ralentissement serait négligeable. Il n'y a pas de formule magique pour les optimisations.

Dans le code ci-dessus, après avoir vérifié comment nous utilisions cette map, nous avons réalisé que bien que nous l'imaginions comme un tableau clairsemé, il s'est avéré qu'elle ne l'était pas tant que cela. Cela correspond à l'argument ci-dessus et nous avons pu voir immédiatement qu'un petit refactoring consistant à changer la map en une slice est en fait possible, et pourrait rendre ce code plus efficace en mémoire. Nous l'avons donc changé en :

Aussi simple que cela, au lieu d'utiliser une map, nous utilisons maintenant une slice. En raison de la manière dont nous recevons les données qui sont chargées de manière paresseuse, et de la manière dont nous accédons plus tard à ces données, en dehors de ces deux lignes et de la structure contenant ces données, aucun autre changement de code n'a été nécessaire. Qu'a-t-il fait à la consommation de mémoire ?

Regardons le `benchcmp` pour quelques tests seulement

Les tests de lecture initialisent la structure de données, ce qui crée les allocations. Nous pouvons voir que le temps d'exécution s'est amélioré d'environ 30 %, les allocations ont diminué de 50 % et la consommation de mémoire de plus de 90 % (!)

Puisque la map, maintenant slice, n'a jamais été remplie avec beaucoup d'éléments, les chiffres montrent à peu près ce que nous verrons en production. Cela dépend de l'entropie des données, mais il peut y avoir des cas où les améliorations des allocations et de la consommation de mémoire auraient été encore plus grandes.

En regardant à nouveau `pprof`, et en prenant un profil de tas à partir du même test, nous verrons que maintenant la consommation de mémoire est en fait réduite d'environ 90 %.

![Image](https://cdn-media-1.freecodecamp.org/images/1*d8jhBw3h_ZrHvbgv95Pjvw.png)

Le point à retenir sera que pour les petits ensembles de données, vous ne devriez pas utiliser de maps là où des slices suffiraient, car les maps ont un surcoût important.

**Vidage de mémoire complet**

Comme mentionné, c'est là que nous voyons la plus grande limitation avec les outils pour le moment. Lorsque nous enquêtions sur ce problème, nous sommes devenus obsédés par la possibilité d'accéder à l'objet racine, sans grand succès. Go évolue au fil du temps à un rythme rapide, mais cette évolution a un prix dans le cas du vidage complet ou de la représentation mémoire. Le format de vidage de mémoire complet, à mesure qu'il change, n'est pas rétrocompatible. La dernière version est décrite [ici](https://github.com/golang/go/wiki/heapdump15-through-heapdump17) et pour écrire un vidage de mémoire complet, vous pouvez utiliser `debug.WriteHeapDump()`.

Bien que pour le moment nous ne nous trouvions pas "bloqués" parce qu'il n'y a pas de bonne solution pour explorer les vidages complets. `pprof` a répondu à toutes nos questions jusqu'à présent.

Notez bien, Internet se souvient de beaucoup d'informations qui ne sont plus pertinentes. Voici quelques choses que vous devriez ignorer si vous allez essayer d'ouvrir un vidage complet vous-même, à partir de go1.11 :

* Il n'y a aucun moyen d'ouvrir et de déboguer un vidage de mémoire complet sur MacOS, seulement sur Linux.
* Les outils à [https://github.com/randall77/hprof](https://github.com/randall77/hprof) sont pour Go1.3, il existe un fork pour 1.7+ mais il ne fonctionne pas correctement non plus (incomplet).
* viewcore à [https://github.com/golang/debug/tree/master/cmd/viewcore](https://github.com/golang/debug/tree/master/cmd/viewcore) ne compile pas vraiment. Il est assez facile de le corriger (les packages dans l'interne pointent vers golang.org et non github.com), mais, _il ne fonctionne pas non plus_, pas sur MacOS, peut-être sur Linux.
* Également [https://github.com/randall77/corelib](https://github.com/randall77/corelib) échoue sur MacOS

#### Interface utilisateur de pprof

Un dernier détail à connaître concernant pprof est sa fonctionnalité d'interface utilisateur. Elle peut économiser beaucoup de temps lors du début d'une enquête sur tout problème lié à un profil pris avec pprof.

```
go tool pprof -http=:8080 heap.out
```

À ce stade, il devrait ouvrir le navigateur web. Si ce n'est pas le cas, naviguez vers le port que vous avez défini. Il vous permet de changer les options et d'obtenir un retour visuel beaucoup plus rapidement que vous ne pouvez le faire depuis la ligne de commande. Une manière très utile de consommer l'information.

L'interface utilisateur m'a en fait familiarisé avec les graphiques de flammes, qui exposent très rapidement les zones coupables du code.

#### Conclusion

Go est un langage passionnant avec un ensemble d'outils très riche, il y a beaucoup plus de choses que vous pouvez faire avec pprof. Cet article n'aborde pas du tout le profilage CPU, par exemple.

Quelques autres bonnes lectures :

* [https://rakyll.org/archive/](https://rakyll.org/archive/) — Je crois que c'est l'un des contributeurs de Go autour de la surveillance des performances, beaucoup de bons articles sur son blog
* [https://github.com/google/gops](https://github.com/google/gops) — écrit par [JBD](https://www.freecodecamp.org/news/how-i-investigated-memory-leaks-in-go-using-pprof-on-a-large-codebase-4bec4325e192/undefined) (qui gère rakyll.org), cet outil mérite son propre article de blog.
* [https://medium.com/@cep21/using-go-1-10-new-trace-features-to-debug-an-integration-test-1dc39e4e812d](https://medium.com/@cep21/using-go-1-10-new-trace-features-to-debug-an-integration-test-1dc39e4e812d) — `go tool trace` qui concerne le profilage CPU, c'est un excellent article sur cette fonctionnalité de profilage.