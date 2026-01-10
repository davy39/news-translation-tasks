---
title: Aperçu d'Erlang avec des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-02-01T00:00:00.000Z'
originalURL: https://freecodecamp.org/news/an-overview-of-erlang-with-examples
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9d15740569d1a4ca35d2.jpg
tags:
- name: Erlang
  slug: erlang
- name: Functional Programming
  slug: functional-programming
- name: toothbrush
  slug: toothbrush
seo_title: Aperçu d'Erlang avec des exemples
seo_desc: 'Erlang is a functional programming language developed by Ericsson for use
  in telecom applications. Because they felt that it’s unacceptable for a telecom
  system to have any significant downtime, Erlang was built to be (among other things):


  distribut...'
---

Erlang est un langage de programmation fonctionnel développé par Ericsson pour une utilisation dans les applications de télécommunications. Parce qu'ils estimaient qu'il est inacceptable pour un système de télécommunications d'avoir un temps d'arrêt significatif, Erlang a été conçu pour être (entre autres) :

* distribué et tolérant aux pannes _(un morceau de logiciel ou de matériel défaillant ne devrait pas faire tomber le système)_
* concurrent _(il peut engendrer de nombreux processus, chacun exécutant un petit et bien défini morceau de travail, et isolé des autres mais capable de communiquer via des messages)_
* échangeable à chaud _(le code peut être échangé dans le système pendant qu'il fonctionne, conduisant à une haute disponibilité et un temps d'arrêt minimal du système)_

### **Syntaxe**

Erlang utilise largement la **récursion**. Puisque les données sont immuables en Erlang, l'utilisation de boucles `while` et `for` (où une variable doit continuer à changer sa valeur) n'est pas autorisée.

Voici un exemple de récursion, montrant comment une fonction retire répétitivement la première lettre du début d'un nom et l'imprime, ne s'arrêtant que lorsque la dernière lettre a été rencontrée.

```erlang
-module(name).

-export([print_name/1]).

print_name([RemainingLetter | []]) ->
  io:format("~c~n", [RemainingLetter]);
print_name([FirstLetter | RestOfName]) ->
  io:format("~c~n", [FirstLetter]),
  print_name(RestOfName).
```

Sortie :

```text
> name:print_name("Mike").
M
i
k
e
ok
```

Il y a aussi un fort accent sur la **correspondance de motifs**, qui élimine fréquemment le besoin d'une structure `if` ou d'une instruction `case`. Dans l'exemple suivant, il y a deux correspondances pour des noms spécifiques, suivies d'une correspondance générale pour tout autre nom.

```erlang
-module(greeting).

-export([say_hello/1]).

say_hello("Mary") ->
  "Welcome back Mary!";
say_hello("Tom") ->
  "Howdy Tom.";
say_hello(Name) ->
  "Hello " ++ Name ++ ".".
```

Sortie :

```text
> greeting:say_hello("Mary").
"Welcome back Mary!"
> greeting:say_hello("Tom").
"Howdy Tom."
> greeting:say_hello("Beth").
"Hello Beth."
```

## **Stockage de termes Erlang**

Le stockage de termes Erlang, normalement abrégé ETS, est une base de données en mémoire intégrée à OTP. Elle est accessible dans Elixir, et est une alternative puissante aux solutions comme Redis lorsque votre application fonctionne sur un seul nœud.

## **Démarrage rapide**

Pour créer une table ETS, vous devez d'abord initialiser une table `tableName = :ets.new(:table_otp_name, [])`, une fois que vous avez initialisé une table, vous pouvez : insérer des données, rechercher des valeurs, supprimer des données, et plus encore.

### **Démonstration ETS dans IEX**

```elixir
iex(1)> myETSTable = :ets.new(:my_ets_table, [])
#Reference<0.1520230345.550371329.65846>
iex(2)> :ets.insert(myETSTable, {"favoriteWebSite", "freeCodeCamp"})
true
iex(3)> :ets.insert(myETSTable, {"favoriteProgrammingLanguage", "Elixir"})
true
iex(4)> :ets.i(myETSTable)
<1   > {<<"favoriteProgrammingLanguage">>,<<"Elixir">>}
<2   > {<<"favoriteWebSite">>,<<"freeCodeCamp">>}
EOT  (q)uit (p)Digits (k)ill /Regexp -->
```

## **Persistance**

Les tables ETS ne sont pas persistantes et sont détruites une fois que le processus qui les possède se termine. Si vous souhaitez stocker des données de manière persistante, une base de données traditionnelle et/ou un stockage basé sur des fichiers est recommandé.

## **Cas d'utilisation**

Les tables ETS sont couramment utilisées pour mettre en cache des données dans l'application, par exemple, les données de compte récupérées depuis une base de données peuvent être stockées dans une table ETS pour réduire le nombre de requêtes à la base de données. Un autre cas d'utilisation est la limitation de débit de l'utilisation de fonctionnalités dans une application web - la vitesse de lecture et d'écriture rapide de l'ETS le rend idéal pour cela. Les tables ETS sont un outil puissant pour développer des applications web hautement concurrentes au coût matériel le plus bas possible.

### **Essayez-le**

Il existe des sites web où vous pouvez essayer d'exécuter des commandes Erlang sans avoir à installer quoi que ce soit localement, comme ceux-ci :

* [Essayez-le ! (un tutoriel pratique)](http://www.tryerlang.org/)
* [TutorialsPoint CodingGround](https://www.tutorialspoint.com/compile_erlang_online.php)

Si vous souhaitez l'installer sur votre machine (ou une machine virtuelle), vous pouvez trouver les fichiers d'installation sur [Erlang.org](https://www.erlang.org/downloads) ou sur [Erlang Solutions](https://www.erlang-solutions.com/resources/download.html).

#### **Plus d'informations :**

* [À propos d'Erlang](https://www.erlang.org/about)
* [Erlang (langage de programmation)](https://en.wikipedia.org/wiki/Erlang_(programming_language))