---
title: Apprendre Julia pour les débutants – Le langage de programmation du futur pour
  la science des données et le machine learning expliqué
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-27T17:13:56.000Z'
originalURL: https://freecodecamp.org/news/learn-julia-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/LearningJuliafreeCodeCamp.png
tags:
- name: Data Science
  slug: data-science
- name: Julia
  slug: julia
- name: Julialang
  slug: julialang
- name: Machine Learning
  slug: machine-learning
seo_title: Apprendre Julia pour les débutants – Le langage de programmation du futur
  pour la science des données et le machine learning expliqué
seo_desc: 'By Logan Kilpatrick

  Julia is a high-level, dynamic programming language, designed to give users the
  speed of C/C++ while remaining as easy to use as Python. This means that developers
  can solve problems faster and more effectively.

  Julia is great for...'
---

Par Logan Kilpatrick

Julia est un langage de programmation de haut niveau et dynamique, conçu pour offrir aux utilisateurs la vitesse du C/C++ tout en restant aussi facile à utiliser que Python. Cela signifie que les développeurs peuvent résoudre des problèmes plus rapidement et plus efficacement.

Julia est idéal pour les problèmes computationnels complexes. De nombreux premiers adopteurs de Julia étaient concentrés dans des domaines scientifiques comme la chimie, la biologie et le machine learning. 

Cela dit, Julia est un langage polyvalent et peut être utilisé pour des tâches comme le développement web, le développement de jeux, et plus encore. Beaucoup considèrent Julia comme le langage de nouvelle génération pour le machine learning et la science des données, y compris le PDG de Shopify (entre autres) :

%[https://twitter.com/tobi/status/1474369669888937992?s=20]

## Comment télécharger le langage de programmation Julia ⚡

Il existe deux principales façons d'exécuter Julia : via un fichier `.jl` dans un [IDE comme VS Code](https://code.visualstudio.com/docs/languages/julia) ou commande par commande dans le REPL de Julia (Read Evaluate Print Loop). Dans ce guide, nous utiliserons principalement le REPL de Julia. Avant de pouvoir utiliser l'un ou l'autre, vous devrez télécharger Julia :

%[https://www.youtube.com/watch?v=t67TGcf4SmM]

ou rendez-vous simplement sur : [https://julialang.org/downloads/](https://julialang.org/downloads/)

Après avoir installé Julia, vous devriez pouvoir le lancer et voir :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-24-at-5.56.14-AM.png)
_Julia 1.7 REPL après l'installation_

## Les bases du langage de programmation Julia pour les débutants

Avant de pouvoir utiliser Julia pour toutes les choses passionnantes pour lesquelles il a été conçu, comme le machine learning ou la science des données, nous devons d'abord nous familiariser avec les bases du langage. 

Nous commencerons par passer en revue les variables, les types et les conditionnelles. Ensuite, nous parlerons des boucles, des fonctions et des packages. Enfin, nous aborderons des concepts plus avancés comme les structs et nous parlerons des ressources d'apprentissage supplémentaires. 

Ce sera un tourbillon, alors accrochez-vous et préparez-vous ! Il est également utile de noter que ce tutoriel suppose que vous avez une certaine familiarité de base avec la programmation. Si ce n'est pas le cas, consultez ce cours sur une [Introduction à Julia pour les débutants nerveux](https://juliaacademy.com/p/julia-programming-for-nervous-beginners).

## Introduction aux variables et types de Julia 📨

Dans Julia, les variables sont typées dynamiquement, ce qui signifie que vous n'avez pas besoin de spécifier le type de la variable lorsque vous la créez.

```julia
julia> a = 10 # Crée la variable "a" et lui assigne le nombre 10
10

julia> a + 10 # Effectue une opération mathématique de base en utilisant "a"
20
```

_(Notez que dans les extraits de code, lorsque vous voyez `julia>`, cela signifie que le code est exécuté dans le REPL)_

Tout comme nous avons défini une variable ci-dessus et lui avons assigné un entier (nombre entier), nous pouvons également faire quelque chose de similaire pour les chaînes de caractères et autres types de variables :

```julia
julia> my_string = "Bonjour freeCodeCamp" # Définir une variable de chaîne de caractères
"Bonjour freeCodeCamp"

julia> balance = 238.19 # Définir une variable flottante 
238.19
```

Lors de la création de variables dans Julia, le nom de la variable ira toujours du côté gauche, et la valeur ira toujours du côté droit après le signe égal. Nous pouvons également créer de nouvelles variables basées sur les valeurs d'autres variables :

```julia
julia> new_balance = balance + a
248.19
```

Ici, nous pouvons voir que le `new_balance` est maintenant la somme (total) de 238.19 et 10. Notez en outre que le type de `new_balance` est un flottant (nombre avec une précision décimale) car lorsque nous additionnons un flottant et un entier, nous obtenons automatiquement le type avec la précision la plus élevée, qui dans ce cas est un flottant. Nous pouvons confirmer cela en faisant :

```julia
julia> typeof(new_balance)
Float64
```

En raison de la nature du typage dynamique, les variables dans Julia peuvent également changer de type. Cela signifie qu'à un moment donné, `holder_balance` pourrait être un flottant, et plus tard, il pourrait être une chaîne de caractères :

```julia
julia> holder_balance = 100.34
100.34

julia> holder_balance = "Le type a changé"
"Le type a changé"

julia> typeof(holder_balance)
String
```

Vous serez également ravi de savoir que les noms de variables dans Julia sont très flexibles, en fait, vous pouvez faire quelque chose comme :

```julia
julia> 😀 = 10
10

julia> 🥲 = -10
-10

julia> 😀 + 🥲
0
```

En plus des noms de variables emoji, vous pouvez également utiliser n'importe quel autre nom de variable Unicode, ce qui est très utile lorsque vous essayez de représenter des idées mathématiques. Vous pouvez accéder à ces variables Unicode en faisant un `\` puis en tapant le nom, suivi en appuyant sur la touche tabulation :

```julia
julia> \sigma # appuyez sur tab et cela rendra le symbole

julia> σ = 10 # définissez sigma égal à 10
```

Dans l'ensemble, le système de variables dans Julia est flexible et offre un ensemble de fonctionnalités qui rendent l'écriture de code Julia facile tout en restant expressif. Si vous souhaitez en savoir plus sur les variables dans Julia, consultez la documentation Julia : [https://docs.julialang.org/en/v1/manual/variables/](https://docs.julialang.org/en/v1/manual/variables/)

## Comment écrire des instructions conditionnelles dans Julia 🔍

En programmation, vous devez souvent vérifier certaines conditions afin de vous assurer que des lignes de code spécifiques s'exécutent. Par exemple, si vous écrivez un programme bancaire, vous ne voulez peut-être autoriser quelqu'un à retirer de l'argent que si le montant qu'il essaie de retirer est inférieur au montant qu'il a présent dans son compte. 

Examinons un exemple de base d'une instruction conditionnelle dans Julia :

```julia
julia> bank_balance = 4583.11
4583.11

julia> withdraw_amount = 250
250

julia> if withdraw_amount <= bank_balance
           bank_balance -= withdraw_amount
           print("Retiré ", withdraw_amount, " de votre compte")
       end
Retiré 250 de votre compte
```

Examinons de plus près certaines parties de l'instruction if qui peuvent différer d'autres codes que vous avez vus : Tout d'abord, nous n'utilisons pas de `:` pour indiquer la fin de la ligne et nous ne sommes pas non plus obligés d'utiliser `()` autour de l'instruction (bien que cela soit encouragé). Ensuite, nous n'utilisons pas `{}` ou similaire pour indiquer la fin de la conditionnelle, au lieu de cela, nous utilisons le mot-clé `end`. 

Tout comme nous avons utilisé l'instruction if, nous pouvons la chaîner avec un `else` ou un `elseif` :

```julia
julia> withdraw_amount = 4600
4600

julia> if withdraw_amount <= bank_balance
           bank_balance -= withdraw_amount
           print("Retiré ", withdraw_amount, " de votre compte")
       else
           print("Solde insuffisant")
       end
Solde insuffisant
```

Vous pouvez en lire plus sur le flux de contrôle et les expressions conditionnelles dans la documentation Julia : [https://docs.julialang.org/en/v1/manual/control-flow/#man-conditional-evaluation](https://docs.julialang.org/en/v1/manual/control-flow/#man-conditional-evaluation)

## Comment utiliser les boucles dans Julia 🔁

Il existe deux principaux types de boucles dans Julia : une boucle for et une boucle while. Comme pour les autres langages, la plus grande différence est que dans une boucle for, vous parcourez un nombre prédéfini d'éléments, tandis que dans une boucle while, vous itérez jusqu'à ce qu'une certaine condition soit modifiée. 

Sur le plan syntaxique, les boucles dans Julia ressemblent beaucoup en structure aux conditionnelles if que nous venons de voir :

```julia
julia> greeting = ["Bonjour", "monde", "et", "bienvenue", "à", "freeCodeCamp"] # définir greeting, un tableau de chaînes de caractères
6-element Vector{String}:
 "Bonjour"
 "monde"
 "et"
 "bienvenue"
 "à"
 "freeCodeCamp"

julia> for word in greeting
           print(word, " ")
       end
Bonjour monde et bienvenue à freeCodeCamp 
```

Dans cet exemple, nous avons d'abord défini un nouveau type : un vecteur (également appelé tableau). Ce tableau contient un ensemble de chaînes de caractères que nous avons définies. Le comportement est très similaire à celui des tableaux dans d'autres langages, mais il est utile de noter que les tableaux sont mutables (ce qui signifie que vous pouvez changer le nombre d'éléments dans le tableau après l'avoir créé).

Encore une fois, lorsque nous regardons la structure de la boucle for, vous pouvez voir que nous itérons à travers la variable `greeting`. Chaque fois, nous obtenons un nouveau mot (dans ce cas) du tableau et l'assignons à une variable temporaire `word` que nous imprimons ensuite. Vous remarquerez que la structure de cette boucle ressemble à l'instruction if et utilise à nouveau le mot-clé `end`. 

Maintenant que nous avons exploré les boucles for, changeons de vitesse et regardons une boucle while dans Julia :

```julia
julia> while user_input != "End"
           print("Entrez une entrée, ou End pour quitter : ")
           user_input = readline() # Demander à l'utilisateur une entrée
       end
Entrez une entrée, ou End pour quitter : bonjour
Entrez une entrée, ou End pour quitter : test
Entrez une entrée, ou End pour quitter : non
Entrez une entrée, ou End pour quitter : End
```

Pour cette boucle while, nous l'avons configurée pour qu'elle s'exécute indéfiniment jusqu'à ce que l'utilisateur tape le mot "End". Comme vous l'avez maintenant vu à quelques reprises, la structure de la boucle devrait commencer à vous sembler familière. 

Si vous voulez voir d'autres exemples de boucles dans Julia, vous pouvez consulter la section sur les boucles de la documentation Julia : [https://docs.julialang.org/en/v1/manual/control-flow/#man-loops](https://docs.julialang.org/en/v1/manual/control-flow/#man-loops)

## Comment utiliser les fonctions dans Julia 

Les fonctions sont utilisées pour créer plusieurs lignes de code, enchaînées ensemble, et accessibles lorsque vous référencez un nom de fonction. Tout d'abord, regardons un exemple de fonction de base :

```julia
julia> function greet()
           print("Bonjour nouvel utilisateur de Julia !")
       end
greet (fonction générique avec 1 méthode)

julia> greet()
Bonjour nouvel utilisateur de Julia !
```

Les fonctions peuvent également prendre des arguments, comme dans d'autres langages :

```julia
julia> function greetuser(user_name)
           print("Bonjour ", user_name, ", bienvenue dans la communauté Julia")
       end
greetuser (fonction générique avec 1 méthode)

julia> greetuser("Logan")
Bonjour Logan, bienvenue dans la communauté Julia
```

Dans cet exemple, nous prenons un argument, puis ajoutons sa valeur à l'impression. Mais que se passe-t-il si nous n'obtenons pas une chaîne de caractères ?

```julia
julia> greetuser(true)
Bonjour true, bienvenue dans la communauté Julia
```

Dans ce cas, puisque nous imprimons simplement, la fonction continue de fonctionner malgré le fait qu'elle ne prend plus une chaîne de caractères et prend plutôt une valeur booléenne (vrai ou faux). Pour empêcher cela de se produire, nous pouvons typer explicitement les arguments d'entrée comme suit :

```julia
julia> function greetuser(user_name::String)
           print("Bonjour ", user_name, ", bienvenue dans la communauté Julia")
       end
greetuser (fonction générique avec 2 méthodes)

julia> greetuser("Logan")
Bonjour Logan, bienvenue dans la communauté Julia
```

Ainsi, la fonction est maintenant définie pour ne prendre qu'une chaîne de caractères. Testons cela pour nous assurer que nous ne pouvons appeler la fonction qu'avec une valeur de chaîne de caractères :

```julia
julia> greetuser(true)
Bonjour true, bienvenue dans la communauté Julia
```

Attendez une seconde, pourquoi cela se produit-il ? Nous avons redéfini la fonction `greetuser`, elle ne devrait plus prendre `true`. 

Ce que nous expérimentons ici est l'une des fonctionnalités sous-jacentes les plus puissantes de Julia : le Multiple Dispatch. Julia nous permet de définir des fonctions avec le même nom et le même nombre d'arguments mais qui acceptent différents types. Cela signifie que nous pouvons créer des versions génériques ou spécifiques de fonctions, ce qui aide énormément à la lisibilité du code puisque vous n'avez pas besoin de gérer tous les scénarios dans une seule fonction. 

Nous devrions rapidement confirmer que nous avons effectivement défini les deux fonctions :

```julia
julia> methods(greetuser)
# 2 méthodes pour la fonction générique "greetuser" :
[1] greetuser(user_name::String) dans Main à REPL[34]:1
[2] greetuser(user_name) dans Main à REPL[30]:1
```

La fonction intégrée `methods` est parfaite pour cela et elle nous indique que nous avons deux fonctions définies, la seule différence étant que l'une prend n'importe quel type, et l'autre ne prend qu'une chaîne de caractères. 

Il est utile de noter que puisque nous avons défini une version spécialisée qui n'accepte qu'une chaîne de caractères, chaque fois que nous appelons la fonction avec une chaîne de caractères, elle appellera la version spécialisée. La fonction plus générique ne sera pas appelée lorsqu'une chaîne de caractères est passée.

Ensuite, parlons de la retour de valeurs depuis une fonction. Dans Julia, vous avez deux options, vous pouvez utiliser le mot-clé `return` explicite, ou vous pouvez choisir de le faire implicitement en ayant la dernière expression dans la fonction servir de valeur de retour comme ceci :

```julia
julia> function sayhi()
           "Ceci est un test"
           "salut"
       end
sayhi (fonction générique avec 1 méthode)

julia> sayhi()
"salut"
```

Dans l'exemple ci-dessus, la valeur de chaîne de caractères "salut" est retournée par la fonction puisque c'est la dernière expression et qu'il n'y a pas d'instruction return explicite. Vous pourriez également définir la fonction comme :

```julia
julia> function sayhi()
           "Ceci est un test"
          return "salut"
       end
sayhi (fonction générique avec 1 méthode)

julia> sayhi()
"salut"
```

En général, du point de vue de la lisibilité, il est logique d'utiliser l'instruction return explicite au cas où quelqu'un lisant votre code ne connaîtrait pas le comportement de retour implicite dans les fonctions Julia.

Une autre fonctionnalité utile des fonctions est la possibilité de fournir des arguments optionnels : 

```julia

julia> function sayhello(response="bonjour")
          return response
       end
sayhello (fonction générique avec 2 méthodes)

julia> sayhello()
"bonjour"

julia> sayhello("salut")
"salut"
```

Dans cet exemple, nous définissons `response` comme un argument optionnel afin que nous puissions soit permettre qu'il utilise le comportement par défaut que nous avons défini, soit le remplacer manuellement lorsque cela est nécessaire. Ces exemples ne font qu'effleurer ce qui est possible avec les fonctions dans Julia. Si vous souhaitez en lire plus sur toutes les choses cool que vous pouvez faire, consultez : [https://docs.julialang.org/en/v1/manual/functions/](https://docs.julialang.org/en/v1/manual/functions/)

## Comment utiliser les packages dans Julia 📦

Le gestionnaire de packages Julia et l'écosystème de packages sont certaines des fonctionnalités les plus importantes du langage. J'ai même écrit un article entier sur [pourquoi c'est l'une des fonctionnalités les plus sous-estimées du langage](https://logankilpatrick.medium.com/the-most-underrated-feature-of-the-julia-programming-language-the-package-manager-652065f45a3a). 

Cela dit, il existe deux façons d'interagir avec les packages dans Julia : via le REPL ou en utilisant le package Pkg. Nous nous concentrerons principalement sur le REPL dans cet article, car il est beaucoup plus facile à utiliser selon mon expérience.

Après avoir installé Julia, vous pouvez entrer dans le gestionnaire de packages depuis le REPL en tapant `]`. 

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screen-Shot-2021-12-26-at-9.50.05-AM.png)
_Mode Pkg dans le REPL de Julia_

Maintenant que nous sommes dans le gestionnaire de packages, il y a quelques choses que nous voulons communément faire :

* Ajouter un package
* Supprimer un package
* Vérifier ce qui est déjà installé

Si vous voulez voir toutes les commandes possibles dans le REPL, entrez simplement en mode Pkg en tapant `]` puis tapez `?` suivi de la touche entrée / retour.

### Comment ajouter des packages Julia ➕

Ajoutons notre premier package, `Example.jl`. Pour ce faire, nous pouvons exécuter :

```julia
(@v1.7) pkg> add Example
```

ce qui devrait fournir une sortie qui ressemble à quelque chose comme :

```julia
(@v1.7) pkg> add Example
Mise à jour du registre à `~/.julia/registries/General`
Mise à jour du dépôt git `https://github.com/JuliaRegistries/General.git`
Mise à jour du registre à `~/.julia/registries/JuliaPOMDP`
Mise à jour du dépôt git `https://github.com/JuliaPOMDP/Registry`
Résolution des versions des packages...
Installé Example ━ v0.5.3
Mise à jour de `~/.julia/environments/v1.7/Project.toml`
[7876af07] + Example v0.5.3
Mise à jour de `~/.julia/environments/v1.7/Manifest.toml`
[7876af07] + Example v0.5.3
Précompilation du projet...
1 dépendance précompilée avec succès en 1 seconde (69 déjà précompilées)
(@v1.7) pkg>
```

_Pour des raisons d'espace, je vais sauter les sorties supplémentaires en supposant que vous suivez avec moi._

### Comment vérifier le statut du package dans Julia 🔍

Maintenant que nous pensons avoir un package installé, vérifions s'il est vraiment là en tapant `status` (ou `st` pour l'abréviation) dans le gestionnaire de packages :

```julia
(@v1.7) pkg> st
Statut `~/.julia/environments/v1.7/Project.toml`
[7876af07] Example v0.5.3
[587475ba] Flux v0.12.8
```

Ici, nous pouvons voir que j'ai deux packages installés, Flux et Example. Il me donne également le chemin vers le fichier qui gère mon environnement actuel (dans ce cas, Julia global v1.7) ainsi que les versions des packages que j'ai installées.

### Comment supprimer un package Julia 📝

Si je voulais supprimer un package de mon environnement actif, comme Flux, je peux simplement taper `remove Flux` (ou `rm` comme abréviation) :

```julia
(@v1.7) pkg> rm Flux
Mise à jour de `~/.julia/environments/v1.7/Project.toml`
[587475ba] - Flux v0.12.8
```

Un rapide `status` par la suite montre que cela a réussi :

```julia
(@v1.7) pkg> st
Statut `~/.julia/environments/v1.7/Project.toml`
[7876af07] Example v0.5.3
```

Nous connaissons maintenant les bases de l'utilisation des packages. Mais nous avons commis un crime majeur en programmation, utiliser notre environnement de packages global. 

### Comment utiliser les packages Julia 📦

Maintenant que nous avons passé en revue comment gérer les packages, explorons comment les utiliser. Tout simplement, vous devez taper `using packageName` pour utiliser un package spécifique que vous souhaitez. L'une de mes nouvelles fonctionnalités préférées dans Julia 1.7 (mise en avant dans [cet article de blog](https://julialang.org/blog/2021/11/julia-1.7-highlights/)) est montrée ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/1-jI58_UDd87Q4fQ326r6E6Q.png)
_Image capturée par l'auteur_

Si vous vous souvenez, nous avons supprimé le package Flux, et bien sûr, je l'ai oublié, alors je suis allé l'utiliser et le charger en tapant `using Flux`. Le REPL me demande automatiquement de l'installer via une simple invite "y/n". C'est une petite fonctionnalité mais qui économise une énorme quantité de temps et de confusion potentielle.

Il est utile de noter qu'il existe deux façons d'accéder aux fonctions exportées d'un package : via le mot-clé `using` et le mot-clé `import`. La grande différence est que `using` amène automatiquement toutes les fonctions dans l'espace de noms actuel (que vous pouvez considérer comme une grande liste de fonctions dont Julia connaît les définitions) tandis que `import` vous donne accès à toutes les fonctions mais vous devez préfixer la fonction avec le nom du package comme : `Flux.gradient()` où `Flux` est le nom du package et `gradient()` est le nom d'une fonction.

---

## Comment utiliser les Structs dans Julia ?

Julia n'a pas de paradigmes de programmation orientée objet (POO) intégrés dans le langage comme les classes. Cependant, les structs dans Julia peuvent être utilisés de manière similaire aux classes pour créer des objets et des types personnalisés. Ci-dessous, nous montrerons un exemple de base :

```julia
julia> mutable struct dog
           breed::String
           paws::Int
           name::String
           weight::Float64
       end

julia> my_dog = dog("Australian Shepard", 4, "Indy", 34.0)
dog("Australian Shepard", 4, "Indy", 34.0)

julia> my_dog.name
"Indy"
```

Dans cet exemple, nous définissons un struct pour représenter un chien. Dans le struct, nous définissons quatre attributs qui composent l'objet chien. Dans les lignes suivantes, nous montrons le code pour créer un objet chien et accéder à certains de ses attributs. Notez que vous n'avez pas besoin de spécifier les types des attributs, vous pouvez le laisser plus ouvert. Pour cet exemple, nous avons défini des types explicites pour mettre en avant cette fonctionnalité.

Vous remarquerez que, similaire aux classes en Python (et autres langages), nous n'avons pas défini de constructeur explicite pour créer l'objet chien. Nous pouvons, cependant, en définir un si cela serait utile :

```julia
julia> mutable struct dog
           breed::String
           paws::Int
           name::String
           weight::Float64
           
           function dog(breed, name, weight, paws=4)
               new(breed, paws, name, weight)
           end
       end

julia> new_dog = dog("German Shepard", "Champ", 46)
dog("German Shepard", 4, "Champ", 46.0)
```

Ici, nous avons défini un constructeur et utilisé le mot-clé spécial `new` afin de créer l'objet à la fin de la fonction. Vous pouvez également créer des getters et setters spécifiquement pour l'objet chien en faisant ce qui suit :

```julia
julia> function get_name(dog_obj::dog)
           print("Le nom du chien est : ", dog_obj.name)
       end
get_name (fonction générique avec 1 méthode)

julia> get_name(new_dog)
Le nom du chien est : Champ
```

Dans cet exemple, la fonction `get_name` ne prend qu'un objet de type `dog`. Si vous essayez de passer autre chose, cela générera une erreur :

```julia
julia> get_name("test")
ERREUR : MethodError : aucune méthode correspondant à get_name(::String)
Les candidats les plus proches sont :
  get_name(::dog) à REPL[61]:1
Stacktrace :
 [1] top-level scope
   @ REPL[63]:1
```

Il est utile de noter que nous avons également défini le struct comme mutable initialement afin que nous puissions changer les valeurs des champs après avoir créé l'objet. Vous pouvez omettre le mot-clé `mutable` si vous voulez que l'état initial de l'objet persiste.

Les structs dans Julia ne nous permettent pas seulement de créer des objets, nous définissons également un type personnalisé dans le processus :

```julia
julia> typeof(new_dog)
dog
```

En général, les structs sont largement utilisés dans l'écosystème Julia et vous pouvez en apprendre plus à leur sujet dans la documentation : [https://docs.julialang.org/en/v1/base/base/#struct](https://docs.julialang.org/en/v1/base/base/#struct)

## Ressources d'apprentissage supplémentaires pour la programmation Julia 📚

J'espère que ce tutoriel vous a aidé à vous familiariser avec de nombreuses idées fondamentales du langage Julia. Cela dit, je sais qu'il reste encore des lacunes car il s'agit d'un guide étendu mais non exhaustif. Pour en savoir plus sur Julia, vous pouvez consulter l'onglet d'apprentissage sur le site Julia : [https://julialang.org/learning/](https://julialang.org/learning/) qui propose des cours guidés, des vidéos YouTube et des problèmes pratiques encadrés. 

Si vous avez d'autres questions ou avez besoin d'aide pour commencer avec Julia, n'hésitez pas à me contacter : [https://twitter.com/OfficialLoganK](https://twitter.com/OfficialLoganK)