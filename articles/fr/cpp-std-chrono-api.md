---
title: 'Garder le temps en C++ : Comment utiliser l''API std::chrono'
subtitle: ''
author: Jayant Chowdhary
co_authors: []
series: null
date: '2023-12-04T23:38:45.000Z'
originalURL: https://freecodecamp.org/news/cpp-std-chrono-api
coverImage: https://www.freecodecamp.org/news/content/images/2023/12/ClangCover.jpg
tags:
- name: C++
  slug: c-2
- name: profiling
  slug: profiling
seo_title: 'Garder le temps en C++ : Comment utiliser l''API std::chrono'
seo_desc: "Keeping track of time is a very important aspect of computer programs.\
  \ Some common use cases are:\n\nMeasure/profile the performance of certain parts\
  \ of code.\nDo work at certain periods of time, from within a program. \nDetect\
  \ whether threads are in a d..."
---

Garder une trace du temps est un aspect très important des programmes informatiques. Voici quelques cas d'utilisation courants :

* Mesurer/profiler les performances de certaines parties du code.
* Effectuer des travaux à certains intervalles de temps, depuis un programme.
* Détecter si les threads sont en deadlock / prennent trop de temps pour compléter une opération.
* Synchroniser des tâches entre différents composants de logiciels

et bien plus encore...

Cet article vous guidera sur la manière de mesurer le temps en C++ moderne.

### Prérequis

* Une compréhension basique de C++ : Pour les lecteurs non familiers avec C++, [Apprendre la programmation C++ pour débutants – Cours gratuit de 31 heures](https://www.freecodecamp.org/news/learn-c-with-free-31-hour-course/) est une ressource utile.
* Une lecture rapide de l'infrastructure de suivi du temps sous Linux – [comme vous pouvez le trouver ici](https://man7.org/linux/man-pages/man2/gettimeofday.2.html) – vous aidera à vous familiariser avec les idées présentées dans l'article.

## Méthodes courantes pour suivre le temps en C++

Cet article couvre comment vous pouvez garder une trace du temps en C++. En C, sur des systèmes de type UNIX, vous pouvez utiliser la fonction [clock_gettime()](https://linux.die.net/man/3/clock_gettime) pour garder une trace du temps. Elle retourne le temps de manière structurée via la structure [`timespec`](https://www.gnu.org/software/libc/manual/html_node/Time-Types.html).

La fonction [`clock_gettime()`](https://linux.die.net/man/3/clock_gettime)/[gettimeofday](https://linux.die.net/man/2/gettimeofday) nous retourne une structure [`timespec`](https://www.gnu.org/software/libc/manual/html_node/Time-Types.html) remplie qui contient deux champs :

1. `tv_sec`, qui nous donne le temps en secondes depuis la source de temps – CLOCK_REALTIME / CLOCK_MONOTONIC – qui a été passée à clock_gettime. Le 'type' de ce champ est [`time_t`](https://en.cppreference.com/w/c/chrono/time_t) qui est généralement une valeur entière.
2. `tv_nsec`, qui donne le temps après `tv_sec`, en nanosecondes depuis la source de temps spécifiée lors de l'appel à `clock_gettime()`. Le type de ce champ est un long int.

Alors pourquoi [`clock_gettime()`](https://linux.die.net/man/3/clock_gettime) n'est-il pas suffisant ? La réponse est que les membres de `struct timespec` peuvent facilement être passés à des fonctions car ils ne sont vraiment que des `int` / `float`. Ils ne sont pas fortement typés.

Il est également facile d'oublier les unités dans lesquelles ils représentent le temps lors du passage d'informations à des fonctions. Cela peut arriver lorsque vous travaillez sur des projets qui ont des milliers de lignes de code.

Alors quelle est la solution ?

## L'API std::chrono

C++11 a introduit l'API std::chrono, qui peut vous aider à éviter certains de ces problèmes.

Il y a 3 parties importantes de l'API.

### 1. `std::chrono::duration`

Comme son nom l'indique, `std::chrono::duration` est un type qui représente un intervalle de temps. La référence officielle C++ mentionne que `std::chrono::duration` est un type templaté avec la signature suivante :

```cpp
template<
    class Rep,
    class Period = std::ratio<1>
> class duration;
```

Ici, le paramètre de template `Rep` représente le type utilisé pour compter les 'ticks' de temps. Un tick est simplement une unité de temps qui est une fraction donnée d'une seconde. `Period`, le deuxième paramètre, définit exactement cette fraction.

Par exemple, si vous écrivez :

```cpp
using my_ms_type = std::chrono::duration<int, std::ratio<1, 1000>>

my_ms_type duration_ms duration = 3; // erreur : impossible de convertir depuis int
my_ms_type duration_ms duration_ok{3} // OK, peut construire depuis int

```

`my_ms_type` est un type qui a été défini, qui compte en unités de millisecondes (1/1000ème de seconde). Ce compte est exprimé comme un entier. Comme vous pouvez le deviner, le paramètre de template `Rep` est `int` et Period est `std::ratio<1,1000>` (qui est en fait une manière de dire 1/1000).

Maintenant qu'il est clair comment les durées sont représentées, voyons ce que nous pouvons et ne pouvons pas faire avec celles-ci.

Si une fonction prend un paramètre de type `my_ms_type` et que vous essayez de passer un type non-`std::chrono::duration`, vous obtiendrez une erreur de compilation.

Il est possible de convertir implicitement entre différents types de `std::chrono::duration` tant que l'information n'est pas perdue avec le type de `Rep`, puisque la bibliothèque standard peut calculer la relation entre deux types `std::chrono::duration`. Il n'est pas possible de convertir implicitement s'il y a une perte d'information. Par exemple :

```cpp
#include<chrono>

using namespace std::chrono;
using my_type_ms = std::chrono::duration<int, std::ratio<1, 1000>>;
using my_type_ms_f = std::chrono::duration<float, std::ratio<1, 1000>>;
using my_type_hundredth_s = std::chrono::duration<int, std::ratio<1, 100>>;
void f(my_type_ms millis) {}
int main()
{
   int duration = 2;
   my_type_ms_f duration_f{2.5};
   my_type_hundredth_s duration_compatible{100};

   f(duration); // erreur : impossible de convertir 'duration' de 'int' en 'my_type_ms'

   f(duration_f) //erreur : puisque float -> int perdra de l'information

   f(duration_compatible) // OK puisque aucune information n'est perdue
}

```

La bibliothèque standard a également quelques spécialisations de templates `std::chrono::duration` prédéfinies pour des durées de temps courantes telles que `std::chrono::duration::seconds`, `milliseconds`, `microseconds`, et ainsi de suite.

Vous pouvez également obtenir la valeur 'count' contenue dans une durée en utilisant la méthode `count` dans une durée.

```cpp
std::chrono::seconds duration{3};
// Affiche : 'Durée count : 3 secondes'
std::cout << "Durée count : " << duration.count() << " secondes";

```

Intéressamment, convertir d'une unité avec une précision plus élevée comme `nanoseconde` à quelque chose avec une précision plus faible comme `milliseconde` peut également entraîner une perte d'information. Pour ces cas spécifiques, vous devez utiliser un _cast explicite_ pour la conversion. Cela s'appelle `duration_cast`. Par exemple :

```cpp
nanoseconds durationInNs = 3000000000;
seconds ms = duration_cast<seconds>(durationInNs); //OK 3s
durationInNs = 3500000000;
ms = duration_cast<nanoseconds>(durationInNs); // OK 3s - troncature vers le bas

```

Maintenant que nous savons pourquoi `std::chrono::duration` est utile, passons à la section suivante qui explore `std::chrono::time_point`.

### 2. `std::chrono::time_point`

`std::chrono::time_point` est une manière d'exprimer un point particulier dans le temps – surprise, surprise !

Si vous y réfléchissez, comment pouvez-vous définir logiquement un point dans le temps ? Nous devons avoir un point de référence de départ et une durée depuis ce point de départ. C'est exactement ce que fait `std::chrono::time_point`.

La déclaration de la classe ressemble à ceci :

```cpp
template<
    class Clock,
    class Duration = typename Clock::duration
> class time_point;

```

Il y a deux paramètres de template ici :

Le premier est `Clock` qui représente une horloge de référence par rapport à laquelle le point dans le temps est mesuré. Pour l'instant, quelques exemples d'horloges sont :

* `system_clock` : cela représente une horloge murale du monde réel. Elle est utile lorsque vous voulez mesurer le temps en termes de temps réels. Il est important de noter que l'heure système peut généralement être changée sur n'importe quel système, donc vous ne devriez pas dépendre de cette horloge pour calculer les périodes de temps entre les tâches / le profilage de performance.
* `steady_clock` : cela représente une horloge qui augmente de manière monotone. Elle est utile lorsque vous avez besoin d'une comptabilité de temps de type chronomètre.

Le deuxième paramètre de template est `Duration` que nous avons discuté dans la section précédente. Un `time_point` doit être associé à un type `duration` puisque c'est ce qui est utilisé pour mesurer les ticks depuis l'« epoch » de l'`Clock`.

Epoch est simplement une manière de dire un point de référence dans le temps. Bien qu'il n'y ait pas de mandat pour savoir quelle référence utiliser, le temps Unix – c'est-à-dire le temps depuis 00:00:00 Temps Universel Coordonné (UTC), jeudi, 1 janvier 1970 – est une référence courante.

Les points dans le temps basés sur la même horloge peuvent être soustraits et non additionnés. Par exemple :

```cpp
auto tp1 = std::chrono::system_clock::now();
...
auto tp2 = std::chrono::system_clock::now()
auto tp3 = std::chrono::steady_clock::now();

auto diff = tp2 - tp1; // OK
auto add = tp1 + tp2; // Pas OK
auto add = tp3 - tp2; // Pas OK - basé sur des horloges différentes

```

Voyons maintenant ce que sont les horloges.

### 3. Types d'horloges

Une `Clock` est un type qui lie ensemble `std::chrono::duration` et `std::chrono::time_point`. Elle a une fonction `now()` qui retourne le `time_point` actuel. Les exigences formelles pour qu'un type soit une `Clock` peuvent être trouvées dans la spécification C++ [ici](https://en.cppreference.com/w/cpp/named_req/Clock).

Comme mentionné précédemment, `system_clock` et `steady_clock` sont deux horloges populaires fournies par la bibliothèque standard. Chaque horloge a sa propre `duration` associée également.

Chaque `time_point` est associé à une certaine horloge, puisqu'il doit vraiment être relatif à une référence donnée.

Enfin, voyons quelques exemples de la manière dont vous pouvez lier ensemble `duration`, `time_point`, et `Clock`. Supposons que vous voulez mesurer le temps que prend une boucle de 100 000 000 de fois en nanosecondes, et que vous voulez également afficher l'heure actuelle de l'horloge murale :

```cpp
#include <chrono>
#include <iostream>
#include <ratio>
#include <thread>
#include <ctime>

using namespace std::chrono;
constexpr size_t kIterations = 100000000;
void testFunction () {
    for (size_t i = 0; i < kIterations; i++) {
    }
}

int main()
{
    auto tStartSteady = std::chrono::steady_clock::now();
    std::time_t startWallTime = system_clock::to_time_t(system_clock::now());
    std::cout << "Heure de début = " << std::ctime(&startWallTime) << " \n";
    testFunction();
    auto tEndSteady = std::chrono::steady_clock::now();
    nanoseconds diff = tEndSteady - tStartSteady;
    std::time_t endWallTime = system_clock::to_time_t(system_clock::now());
    std::cout << "Heure de fin = " << std::ctime(&endWallTime) << " \n";
    std::cout << "Temps pris = " << diff.count() << " ns";
    return 0; 
}

```

La sortie du programme est la suivante :

```
Sortie :
// Cela peut bien sûr varier d'un système à l'autre
Heure de début = Mar 7 nov 07:11:13 2023

Heure de fin = Mar 7 nov 07:11:13 2023

Temps pris = 50998885 ns

```

## Résumé

Cet article a exploré diverses facettes de l'API `std::chrono` en C++. L'API `std::chrono` permet aux programmeurs C++ de garder une trace du temps de manière sûre grâce à son système fortement typé. Elle aide également à maintenir le support pour des conversions pratiques entre différents 'types' de points dans le temps.