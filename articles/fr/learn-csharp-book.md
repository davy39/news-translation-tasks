---
title: Apprendre le langage de programmation C# – Livre complet pour débutants
subtitle: ''
author: Gavin Lon
co_authors: []
series: null
date: '2024-02-06T22:35:57.000Z'
originalURL: https://freecodecamp.org/news/learn-csharp-book
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/The-C--Handbook
seo_title: Apprendre le langage de programmation C# – Livre complet pour débutants
---

Version-4-Cover.png
tags:
- name: débutant
  slug: debutant
- name: livre
  slug: livre
- name: C#
  slug: csharp
seo_title: null
seo_desc: 'La version 1 de C# a été publiée en janvier 2002. Il s'agit d'un langage de programmation moderne et généraliste conçu et développé de zéro par le célèbre ingénieur logiciel danois, Anders Heijleberg, et son équipe chez Microsoft.

J'ai entendu Anders Heijlsb...'
---

La version 1 de C# a été publiée en janvier 2002. Il s'agit d'un langage de programmation moderne et généraliste conçu et développé de zéro par le célèbre ingénieur logiciel danois, Anders Heijleberg, et son équipe chez Microsoft.

J'ai entendu Anders Heijlsberg dire dans une interview que l'objectif avec C# était de fournir la puissance et l'expressivité de C++ et les capacités de RAD (Développement Rapide d'Applications) de Visual Basic.

C# est similaire à Java dans le sens où il s'exécute dans son propre environnement. Java s'exécute dans un environnement connu sous le nom de JRE (Java Runtime Environment), tandis que C# s'exécute dans un environnement connu sous le nom de .NET. Le JRE et .NET s'exécutent tous deux sur le système d'exploitation pertinent.

La première version de .NET est connue sous le nom de .NET Framework, qui doit être déployée en totalité sur l'ordinateur cible et ne peut s'exécuter que sur les plateformes Windows. Mais maintenant, .NET a évolué vers un environnement qui peut s'exécuter sur plusieurs plateformes comme Windows, Mac OS, Linux, IOS, Android et plus.

L'environnement .NET est devenu fragmenté en 2016 avec la sortie de .NET Core, qui a permis à .NET d'être multiplateforme et agile dans le sens où seules les dépendances de la bibliothèque de classes de base de votre application doivent être déployées sur l'ordinateur cible avec votre application.

Ensuite, en 2020, .NET est devenu unifié avec la sortie de .NET 5, ce qui signifiait que la confusion créée par l'existence de deux branches de .NET, à savoir .NET Framework et .NET Core, était atténuée.

La dernière version stable de C# est un langage de programmation hautement évolué et sophistiqué qui vous permet de créer presque tout type d'application pouvant s'exécuter sur plusieurs plateformes. Vous pouvez créer une seule base de code qui peut s'exécuter sur plusieurs plateformes, par exemple Linux, Mac OS, Android, IOS, dans le Cloud, bien sûr les systèmes d'exploitation Windows et plus.

Vous êtes en mesure d'écrire et de construire vos applications C# en utilisant des outils gratuits comme Visual Studio 2022 Community edition ou l'outil léger et multiplateforme, Visual Studio Code. Visual Studio Code peut s'exécuter sur les plateformes Windows, Mac OS et Linux.

C# est un langage de programmation très polyvalent. Vous pouvez construire de nombreux types d'applications, telles que des applications basées sur le web utilisant ASP .NET, des applications mobiles et de bureau multiplateformes utilisant le framework .Net MAUI, des applications pour l'Internet des objets, des applications d'IA utilisant ML.NET, des applications natives pour le cloud, des jeux et plus.

C# bénéficie d'une grande base de support, soutenue par Microsoft, et est en constante évolution. Une nouvelle version de .NET est publiée chaque novembre, contenant toujours de nombreuses améliorations et fonctionnalités. Cela signifie que .NET évolue, s'améliore et suit les dernières tendances technologiques.

C# est un langage de programmation moderne, bien conçu et généraliste qui sera un excellent ajout à votre boîte à outils de développeur. Alors, plongeons-nous dans le sujet.

## Table des matières

* [Introduction à .NET](#heading-introduction-to-net)
* [Outils gratuits disponibles pour créer des applications C#](#heading-outils-gratuits-disponibles-pour-creer-des-applications-c)
  * [Créer une application console de base en utilisant Visual Studio Community Edition](#heading-creer-une-application-console-de-base-en-utilisant-visual-studio-community-edition)
    * [La méthode Main (Point d'entrée de l'application)](#heading-la-methode-main-point-dentree-de-lapplication)
  * [Créer une application console de base en utilisant Visual Studio Code](#heading-comment-creer-une-application-console-de-base-en-utilisant-visual-studio-code)
* [Types de données C#](#heading-types-de-donnees-c)
  * [Types de valeur et types de référence](#heading-types-de-valeur-et-types-de-reference)
  * [Types de valeur intégrés de C#](#heading-types-de-valeur-integrés-de-c)
  * [Types de référence intégrés de C#](#heading-types-de-reference-integrés-de-c)
* [Chaînes de caractères C#](#heading-chaines-de-caracteres-c)
  * [Immuabilité des chaînes de caractères C#](#heading-immuabilite-des-chaines-de-caracteres-c)
  * [Littéraux de chaîne de caractères entre guillemets, littéraux de chaîne de caractères verbatim et littéraux de chaîne de caractères bruts](#heading-litteraux-de-chaine-de-caracteres-entre-guillemets-litteraux-de-chaine-de-caracteres-verbatim-et-litteraux-de-chaine-de-caracteres-bruts)
    * [Littéraux de chaîne de caractères entre guillemets](#heading-litteraux-de-chaine-de-caracteres-entre-guillemets)
    * [Littéraux de chaîne de caractères verbatim](#heading-litteraux-de-chaine-de-caracteres-verbatim)
    * [Littéraux de chaîne de caractères bruts](#heading-litteraux-de-chaine-de-caracteres-bruts)
* [Méthodes intégrées utiles pour les chaînes de caractères C#](#heading-methodes-integrées-utiles-pour-les-chaines-de-caracteres-c)
  * [La méthode intégrée IndexOf](#heading-la-methode-integree-indexof)
  * [La méthode intégrée Replace](#heading-la-methode-integree-replace)
  * [La méthode intégrée Substring](#heading-la-methode-integree-substring)
* [Conversion de types de données C#](#heading-conversion-de-types-de-donnees-c)
  * [Conversion implicite vs explicite de types de données](#heading-conversion-implicite-vs-explicite-de-types-de-donnees)
* [Opérateurs C#](#heading-operateurs-c)
  * [Types d'opérateurs C#](#heading-types-doperateurs-c)
* [Constantes et variables en lecture seule](#heading-constantes-et-variables-en-lecture-seule)
  * [Introduction aux constantes](#heading-introduction-aux-constantes)
  * [Introduction aux variables en lecture seule](#heading-introduction-aux-variables-en-lecture-seule)
  * [Exemple de code utilisant une constante](#heading-exemple-de-code-utilisant-une-constante)
  * [Exemple de code utilisant une variable en lecture seule](#heading-exemple-de-code-utilisant-une-variable-en-lecture-seule)
  * [Exemple de code de l'utilisation incorrecte d'une variable en lecture seule](#heading-exemple-de-code-de-lutilisation-incorrecte-dune-variable-en-lecture-seule)
* [Instructions if / else if / else en C#](#heading-instructions-if-else-if-else-en-c)
  * [Logique conditionnelle if/else de base](#heading-logique-conditionnelle-ifelse-de-base)
  * [Implémentation de la logique conditionnelle if/else if/else](#heading-implementation-de-la-logique-conditionnelle-ifelse-ifelse)
  * [Instructions if imbriquées](#heading-instructions-if-imbriquees)
  * [Expressions conditionnelles plus complexes](#heading-expressions-conditionnelles-plus-complexes)
    * [L'opérateur &&](#heading-loperateur-ampamp)
    * [L'opérateur ||](#heading-loperateur-ou)
* [Boucles C#](#heading-boucles-c)
  * [La boucle for](#heading-la-boucle-for)
  * [La boucle while](#heading-la-boucle-while)
  * [La boucle do-while](#heading-la-boucle-do-while)
  * [La boucle foreach](#heading-la-boucle-foreach)
* [Tableaux C#](#heading-tableaux-c)
  * [Tableaux à une dimension](#heading-tableaux-a-une-dimension)
  * [Tableaux multidimensionnels](#heading-tableaux-multidimensionnels)
    * [Tableaux à deux dimensions](#heading-tableaux-a-deux-dimensions)
    * [Tableaux à trois dimensions](#heading-tableaux-a-trois-dimensions)
  * [Tableaux irréguliers](#heading-tableaux-irreguliers)
* [Méthodes C#](#heading-methodes-c)
  * [Introduction aux méthodes](#heading-introduction-aux-methodes-en-c)
  * [La méthode Main](#heading-la-methode-main)
  * [La structure des méthodes](#heading-la-structure-des-methodes)
* [Classes C#](#heading-classes-c)
  * [Le mot-clé 'class'](#heading-le-mot-cle-class)
  * [Modificateur d'accès public](#heading-le-modificateur-dacces-public)
  * [Variable membre privée](#heading-la-variable-membre-privee)
  * [Le constructeur](#heading-le-constructeur)
* [Structs C#](#heading-structs-c)
  * [Différences clés entre une classe et une struct](#heading-differences-cles-entre-une-classe-et-une-struct)
  * [Utiliser une struct dans le code](#heading-utiliser-une-struct-dans-le-code)
* [Enums et instructions switch](#heading-enums-et-instructions-switch)
  * [Introduction aux enums](#heading-introduction-aux-enums)
  * [Utiliser un enum dans le code](#heading-utiliser-un-enum-dans-le-code)
  * [Utiliser une instruction switch dans le code avec un enum](#heading-utiliser-une-instruction-switch-dans-le-code-avec-un-enum)
  * [Associer un bloc de code à plus d'un cas](#heading-associer-un-bloc-de-code-a-plus-dun-cas)
  * [Utiliser des chaînes de caractères dans les instructions switch](#heading-utiliser-des-chaines-de-caracteres-dans-les-instructions-switch)
* [Héritage en C#](#heading-heritage-en-c)
* [Abstraction en C#](#heading-abstraction-en-c)
* [Exceptions C#](#heading-gestion-des-exceptions-en-c)
* [Délégations C#](#heading-delegations-c)
* [Événements C#](#heading-evenements-c)
* [Génériques C#](#heading-generiques-c)
* [LINQ](#heading-linq)
* [Attributs C#](#heading-attributs-c)
* [Réflexion](#heading-reflexion-en-c)
* [Vidéo sur la programmation asynchrone en C#](#heading-video-sur-la-programmation-asynchrone-en-c)
* [Conclusion](#heading-conclusion)

## Introduction à .NET

Comme nous l'avons brièvement discuté dans la section d'introduction, .NET fournit un environnement dans lequel vos applications C# s'exécutent.

Une caractéristique essentielle de .NET est ce qui peut être décrit comme une machine virtuelle connue sous le nom de CoreCLR ou Core Common Language Runtime.

Le Core Common Language Runtime fournit des services comme la compilation Just-in-time, la gestion de la mémoire, le garbage collection, la sécurité et la gestion des exceptions. Également fourni avec .NET est une variété de bibliothèques de classes de base, qui fournissent des fonctionnalités génériques qui peuvent être exploitées par votre code C#.

La première version de .NET était le .NET Framework qui a été publié en 2002. .NET Framework ne pouvait s'exécuter que sur certaines plateformes Windows et devait être installé dans son intégralité sur l'ordinateur cible.

.NET Core a été publié en 2016 et a fourni une version modulaire et multiplateforme de .NET optimisée pour le cloud. Une caractéristique significative de .NET Core était que seules les dépendances utilisées par votre application devaient être déployées sur l'ordinateur cible, contrairement à .NET Framework qui devait exister dans son intégralité sur l'ordinateur cible.

L'évolution rapide de ces deux versions de .NET, .NET Framework et .NET Core, a entraîné une fragmentation croissante de .NET.

Afin de traiter la fragmentation continue de .NET, Microsoft a créé le .NET Standard, où toutes les plateformes exécutant .NET devaient supporter .NET Standard. Ce fut la première étape vers l'unification de .NET, mais ce fut une solution temporaire.

Ensuite, en novembre 2020, .NET 5 a été publié. Cette version de .NET a conservé les excellentes fonctionnalités de .NET Framework et de .NET Core, mais cette publication était significative en ce sens que .NET 5 signifiait que .NET était désormais unifié sous une seule bannière (pour ainsi dire). Il n'y a plus de .NET Framework et de .NET Core – plutôt une seule version de .NET évoluant.

Avec la sortie de .NET 6 l'année suivante, en novembre 2021, de nombreuses améliorations et nouvelles fonctionnalités significatives sont apparues. Peut-être ce qui est le plus significatif à propos de .NET 6, c'est qu'il a cimenté l'unification de .NET.

À ce stade, .NET est un environnement multiplateforme, modulaire, agile, rapide, robuste et sécurisé dans lequel vos applications C# peuvent s'exécuter. Cela signifie que C# et .NET ont maintenant évolué à un point où vous pouvez "écrire une fois et exécuter partout".

Voici une vidéo de présentation sur le fonctionnement de .NET en plus de détails :

%[https://youtu.be/P6lJA3E3Uog]

Et pour une série vidéo complète sur l'évolution de .NET, vous pouvez consulter ceci :

%[https://www.youtube.com/watch?v=OkeM7XVwEdA&list=PL4LFuHwItvKZAL8rpQiGRbWmgBj6TI7fM]

## Outils gratuits disponibles pour créer des applications C#

Microsoft fournit deux outils sophistiqués gratuits que vous pouvez utiliser pour créer des applications C# : Visual Studio Community Edition, qui est un IDE (Environnement de Développement Intégré) qui peut s'exécuter sur les plateformes Windows, et Visual Studio Code (un éditeur de code léger) qui peut s'exécuter sur les plateformes Windows, Mac OS et Linux.

Vous pouvez télécharger et installer Visual Studio Community Edition 2022 et la dernière version de Visual Studio Code à partir d'ici : [https://visualstudio.microsoft.com/downloads/](https://visualstudio.microsoft.com/downloads/).

### Créer une application console de base en utilisant Visual Studio Community Edition

La manière la plus simple de créer votre première application C# est d'utiliser le modèle de projet le plus simple mis à votre disposition via Visual Studio.

Le modèle de projet le plus simple s'appelle "Console App". Pour commencer à construire votre première application C# en utilisant Visual Studio, suivez simplement les instructions ci-dessous :

* Lancez Visual Studio
* Dans la section "Get Started" de la boîte de dialogue présentée, sélectionnez "Create a new project".
* Trouvez le modèle de projet nommé "Console App".
* Sélectionnez l'option de modèle de projet "Console App" et appuyez sur le bouton "Next".
* Fournissez un nom pour votre projet et l'emplacement sur votre disque dur où vous souhaitez stocker les fichiers de votre projet. Appuyez sur le bouton "Next".
* Au moment de la création de ce livre, la dernière version stable de .NET est la version 8. Si vous avez cette dernière version installée sur votre ordinateur cible, elle sera sélectionnée dans la liste déroulante pertinente pour le champ marqué "Framework".
* Appuyez sur le bouton 'Create' pour générer les fichiers de votre projet C#.

Vous pouvez consulter la vidéo YouTube ci-dessous pour une démonstration de la création d'un projet "Console App" de base en utilisant Visual Studio 2022.

Dans cette vidéo YouTube, la première démonstration de la création d'un projet de base montre comment créer un projet "Console App" qui inclut des instructions de niveau supérieur (c'est-à-dire que la définition de la méthode `Main` n'est pas présente par défaut).

La deuxième démonstration montre la création d'un projet "Console App" de base qui n'inclut pas d'instructions de niveau supérieur. Vous verrez comment la méthode `Main` est affichée dans le code par défaut, tandis que dans la première démonstration, seul le corps de la méthode `Main` est affiché, et la définition réelle de la méthode `Main` n'est pas présente.

Notez que la méthode `Main` est toujours le point d'entrée des applications C#. Lorsque des instructions de niveau supérieur sont incluses, la méthode `Main` est toujours présente mais n'est pas visible par défaut dans votre code. L'inclusion d'instructions de niveau supérieur entraîne une réduction de la quantité de code standard nécessaire pour qu'un développeur puisse commencer.

%[https://youtu.be/10QrZCLfuCQ]

#### La méthode Main (Point d'entrée de l'application)

Si vous regardez le fichier "Program.cs", vous verrez le code suivant :

```csharp

    Console.WriteLine("Hello World"); 

```

Vous pouvez exécuter ce code en appuyant sur le bouton de lecture de votre barre d'outils. Le code de cette application est très basique et affiche simplement la ligne "Hello World" sur l'écran de la console.

Si vous regardez le code dans le fichier "Program.cs", il peut sembler qu'il n'y ait pas de réel point d'entrée pour l'application. Cela est spécifique lorsque vous avez choisi d'utiliser des instructions de niveau supérieur. Si vous avez écrit du code dans des versions précédentes de .NET, l'absence d'une méthode `Main` sera frappante.

Ainsi, dans .NET 5, par exemple, le même code actuellement dans votre application aurait une apparence différente car la classe de programme et, à l'intérieur, la méthode `Main` seraient incluses.

Consultez le code représenté dans la figure 1 pour un exemple de ceci :

Figure 1.

```csharp
namespace CSharpSampleCode
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello, World!");
        }
    }
}

```

Dans .NET 6, un effort marqué a été fait pour simplifier la quantité de code standard nécessaire dans vos applications. Notez qu'avec C# 10, vous pouvez simplement écrire le corps de la méthode `Main` dans le fichier "Program.cs". Vous n'avez pas besoin d'inclure une définition de classe (et, à l'intérieur de la classe pertinente, une définition de méthode `Main`) comme le montre la figure 1.

Ainsi, les instructions pertinentes n'ont pas besoin de résider dans une méthode `Main`. Les instructions peuvent exister en tant que ce qu'on appelle des instructions de niveau supérieur.

Une méthode `Main` existe toujours en coulisses et est toujours le point d'entrée pour toutes les applications C#. Mais après la sortie de .NET 6, la méthode `Main` n'a pas besoin d'être présente dans votre code car le compilateur synthétise une classe `Program` avec une méthode `Main` et place toutes vos instructions de niveau supérieur dans la méthode `Main`.

Mais cela se fait maintenant en coulisses. Le terme instructions de niveau supérieur signifie que vous êtes en mesure d'écrire des instructions qui ne sont pas enveloppées dans une méthode `Main` au sein d'une classe. En coulisses, la méthode `Main` et la classe pertinente sont créées par le compilateur. Vous êtes donc en mesure d'écrire beaucoup moins de code, et le point d'entrée de l'application – qui était auparavant explicitement écrit en utilisant la méthode `Main` – est maintenant synthétisé par le compilateur C#.

La figure 2 montre comment vous pouvez éviter d'écrire plusieurs lignes de code pour la méthode `Main` (le point d'entrée pour une application C#).

Figure 2.

```csharp
Console.WriteLine("Hello, World!"); // La méthode 'Main' n'est pas visible dans le code

```

%[https://youtu.be/2pquQMSYk6c]

### Comment créer une application console de base en utilisant Visual Studio Code

Je vais maintenant vous guider à travers le processus de création d'une application console en utilisant Visual Studio Code.

Tout d'abord, vous devrez lancer VS Code. Pour la meilleure expérience de codage d'une application en C#, vous devriez installer l'extension C# Dev Kit en utilisant la vue Extensions.

Vous pouvez ouvrir la vue Extensions en cliquant sur la barre d'activité sur le côté de Visual Studio Code. Vous pouvez ensuite rechercher C# Dev Kit et installer cette extension.

Ensuite, créez un dossier local où vous souhaitez stocker les fichiers de votre projet C# n'importe où sur votre ordinateur.

En utilisant l'option de menu Fichier > Ouvrir un dossier, ouvrez le dossier que vous avez créé à l'étape précédente, depuis VS Code.

Ensuite, lancez la fenêtre de terminal en utilisant l'option de menu Affichage > Terminal. Vous pouvez également lancer la fenêtre de terminal en appuyant sur ctrl + `

Vous devrez vous assurer que vous avez installé une version appropriée du SDK .NET. La dernière version stable est la version 8 de .NET. Vous pouvez télécharger le fichier d'installation recommandé à partir de cet emplacement, [https://dotnet.microsoft.com/download](https://dotnet.microsoft.com/download).

Afin de vérifier que vous avez installé le SDK .NET, vous pouvez taper `dotnet --version` dans la fenêtre de terminal, puis appuyer sur la touche Entrée.

Pour créer un projet basé sur le modèle de projet "Console App", vous pouvez taper cette commande à votre invite de commande : `dotnet new console`. Ensuite, appuyez sur la touche Entrée.

Pour exécuter le projet, tapez `dotnet run` à l'invite de commande et appuyez sur la touche Entrée.

Après avoir mis à jour le code dans votre fichier 'Program.cs', n'oubliez pas d'enregistrer vos modifications avant d'exécuter le code mis à jour.

En guise d'exercice, modifiez le code pour que la sortie soit 'Hello C#', puis enregistrez votre code, puis exécutez votre code en tapant `dotnet run` dans la fenêtre de terminal. Une fois que vous appuyez sur la touche Entrée, 'Hello C#' devrait être affiché sur votre écran de console.

Pour un guide vidéo détaillé sur la façon d'utiliser Visual Studio Code pour créer des applications C#, vous pouvez regarder la vidéo YouTube suivante :

%[https://youtu.be/rab_1cFQUF4]

## Types de données C#

Il est important de noter que C# est un langage de programmation à typage statique, tandis que JavaScript et Python, par exemple, sont tous deux à typage dynamique.

Cela signifie qu'en C#, lorsque les variables sont déclarées au moment de la compilation, les variables doivent être définies comme un type C# spécifique.

Une exception à cette règle est faite par l'utilisation du type `dynamic`. Le type de données `dynamic` vous permet de contourner le système de types .Net. Si une variable est déclarée comme le type de données `dynamic`, cela est similaire à la façon dont les variables sont typées dans un langage à typage dynamique comme JavaScript.

Dans la plupart des cas, vous devez fortement typer les variables afin de pouvoir tirer parti des avantages inhérents à un langage à typage statique. L'avantage de typer fortement les variables est que les erreurs potentielles liées aux types de données peuvent être signalées au moment de la compilation et ensuite traitées de manière appropriée au moment de la compilation.

Si vous créez du code qui n'est pas valide par rapport au type utilisé pour définir une variable, cela peut être signalé par le compilateur C# au moment de la compilation.

Si vous regardez l'exemple de code dans la figure 3, le code C# est invalide car la variable `a` est définie comme un entier et dans la méthode `DoSomething`, la variable `a` est assignée à une valeur de chaîne.

Le compilateur C# signale l'exception au moment de la compilation, et l'exception est représentée dans l'IDE Visual Studio, où une ligne rouge en zigzag est tracée sous le code incriminé.

Figure 3.

```csharp
internal class SomeClass
{
    int a = 1;

    public void DoSomething()
    {
        a = "Gavin Lon"; // Erreur de compilation indiquant : "Impossible de convertir implicitement le type 'string' en 'int'"
    }
}

```

Ainsi, le code échoue à la compilation et la cause de l'exception de compilation est clairement indiquée par une ligne rouge en zigzag qui apparaît sous le code incriminé.

Cela protège les exceptions liées aux types d'être déployées dans un environnement de production où le code qui n'est pas correctement vérifié au moment de la compilation pourrait être sujet à des erreurs d'exécution.

Les langages à typage statique garantissent une meilleure robustesse du code à l'exécution que les langages à typage dynamique. C# offre également de meilleures performances que les langages à typage dynamique comme JavaScript ou Python, car l'utilisation de variables à typage statique signifie que le type de la variable est connu au moment de la compilation. Cela signifie que les types de variables n'ont pas besoin d'être déterminés à l'exécution, ce qui est ce qui se passe avec les langages à typage dynamique.

Avec les langages à typage dynamique, le type d'une variable est déterminé à l'exécution en fonction de la valeur assignée à la variable pertinente. Avec les langages à typage statique comme C#, le type est connu, pour ainsi dire, au moment de la compilation – donc l'étape supplémentaire de déterminer le type de la variable à l'exécution n'est pas nécessaire. Cela entraîne un avantage de performance par rapport au code à typage dynamique.

### Types de valeur et types de référence

Les types de données C# peuvent être classés en deux catégories principales : les types de valeur et les types de référence. Ces classifications principales de types de données désignent la manière dont les données pour les types de données C# sont stockées en mémoire.

Un type de valeur est stocké dans un emplacement mémoire appelé la pile, où la valeur assignée à une variable est stockée dans l'espace mémoire pertinent sur la pile.

Un type de référence est stocké dans un emplacement mémoire connu sous le nom de tas, où une adresse de l'endroit où les données réelles sont stockées réside sur la pile et pointe vers l'emplacement où les données réelles sont stockées sur le tas.

Une différence clé entre les données stockées sur la pile et les données stockées sur le tas est que toutes les données stockées sur la pile ont une taille fixe, où les données stockées sur le tas n'ont pas une taille fixe. La taille fixe pour les données discrètes stockées sur la pile signifie une plus grande efficacité dans le stockage et la récupération de telles données par rapport à la gestion des données stockées sur le tas.

Un exemple très basique qui met en évidence l'importance des types de valeur et des types de référence est le suivant :

Disons qu'un entier nommé `a` est assigné à une valeur de `1`, et qu'un entier nommé `b` est assigné à la valeur stockée dans `a`. Ensuite, disons que la valeur de `3` est assignée à la variable `a`. Cette assignation affecte-t-elle la valeur stockée dans la variable `b` ?

La réponse est non. Cela est dû au fait que le type de données entier est un type de valeur. Les données de la variable `a` et les données de la variable `b` sont stockées dans des emplacements mémoire complètement différents sur la pile. Ainsi, une modification des données stockées dans la variable `a` n'affectera pas les données stockées dans la variable `b`, même si la valeur stockée dans `a` a été assignée à la variable `b`.

Figure 4.

```csharp
int a = 1;
int b = a;
a = 3;

```

Le type de données objet en C# est le type racine pour tous les types de données en C#. Un type de données objet est un type de référence, et donc tous les types qui héritent directement du type de données objet sont des types de référence.

Dans l'exemple ci-dessous (dans la figure 5), la variable `a`, qui est définie comme le type défini par l'utilisateur `Employee`, est assignée à un nouvel objet `Employee`, où la propriété `Name` est définie sur la valeur de chaîne `"Gavin Lon"`. La variable `b`, qui est définie comme le type défini par l'utilisateur `Employee`, est assignée à la valeur de `a`.

Lorsque la propriété `Name` de la variable d'objet `a` est modifiée en `David Hasslehoff`, la propriété `Name` de la variable d'objet `b` est automatiquement modifiée en `"David Hasslehof"`.

Cela est dû au fait que lorsque `b` est assignée à la valeur stockée dans `a`, les données stockées dans `a` ne sont pas copiées vers l'emplacement de stockage qui stocke les données dans `b`. Une adresse mémoire est copiée vers `b`, qui contient l'emplacement mémoire où les données sont stockées pour la variable `a`. Les données réelles sont stockées sur le tas et seul l'emplacement mémoire où les données sont stockées sur le tas est stocké sur la pile.

Cela signifie que la variable `a` et la variable `b` référencent les mêmes données (stockées sur le tas) à ce stade. Ainsi, lorsque la propriété `Name` de la variable d'objet `a` est modifiée en `"David Hasslehof"`, ce changement affecte également la variable `b`. Ainsi, la propriété `Name` dans la variable `b` reflétera également `"David Hasselhof"`.

Figure 5.

```csharp
Employee a = new Employee { Id = 1, Name = "Gavin Lon" };
Employee b = a;
a.Name = "David Hasslehof";
Console.WriteLine(b.Name); // Ce code imprime la valeur David Hasslehof

```

### Types de valeur intégrés de C#

Vous pouvez voir ci-dessous, dans la figure 6, les types de données de valeur intégrés en C#. Chaque élément contient un lien vers une page Microsoft Learn appropriée afin que vous puissiez lire plus d'informations sur le type de données pertinent.

Figure 6.

<table style="box-sizing: inherit ; outline-color: inherit ; border-collapse: collapse ; border-spacing: 0px ; margin-top: 1rem ; color: rgb(22 , 22 , 22) ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 16px ; font-style: normal ; font-weight: 400 ; letter-spacing: normal ; text-transform: none ; white-space: normal ; word-spacing: 0px ; text-decoration: none"><thead style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">Mot-clé de type C#</th><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">Type .NET</th></tr></thead><tbody style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/bool" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">bool</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.boolean" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Boolean</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">byte</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.byte" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Byte</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">sbyte</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.sbyte" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.SByte</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/char" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">char</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.char" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Char</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">decimal</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.decimal" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Decimal</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">double</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.double" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Double</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/floating-point-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">float</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.single" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Single</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">int</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int32" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int32</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">uint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint32" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt32</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">nint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.intptr" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.IntPtr</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">nuint</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uintptr" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UIntPtr</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">long</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int64" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int64</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">ulong</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint64" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt64</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">short</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.int16" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Int16</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/integral-numeric-types" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">ushort</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.uint16" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.UInt16</a></td></tr></tbody></table>

### Types de référence intégrés de C#

Et vous pouvez également voir tous les types de données de référence intégrés en C# dans la figure 7.

Figure 7.

<table style="box-sizing: inherit ; outline-color: inherit ; border-collapse: collapse ; border-spacing: 0px ; margin-top: 1rem ; color: rgb(22 , 22 , 22) ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 16px ; font-style: normal ; font-weight: 400 ; letter-spacing: normal ; text-transform: none ; white-space: normal ; word-spacing: 0px ; text-decoration: none"><thead style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">Mot-clé de type C#</th><th style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left">Type .NET</th></tr></thead><tbody style="box-sizing: inherit ; outline-color: inherit"><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-object-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">object</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.object" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Object</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-string-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">string</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.string" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.String</a></td></tr><tr style="box-sizing: inherit ; outline-color: inherit"><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/builtin-types/reference-types#the-dynamic-type" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)"><code style="box-sizing: inherit ; outline-color: inherit ; font-family: &quot;segoe ui&quot; , &quot;segoeui&quot; , &quot;helvetica neue&quot; , &quot;helvetica&quot; , &quot;arial&quot; , sans-serif ; font-size: 1em ; direction: ltr">dynamic</code></a></td><td style="box-sizing: inherit ; outline-color: inherit ; padding: 0px ; text-align: left"><a href="https://learn.microsoft.com/en-us/dotnet/api/system.object" class="no-loc" style="box-sizing: inherit ; outline: inherit 0px ; cursor: pointer ; overflow-wrap: break-word ; text-decoration: none ; background-color: rgba(0 , 0 , 0 , 0)">System.Object</a></td></tr></tbody></table>

Et maintenant, vous pouvez consulter deux vidéos YouTube où les types de données C# et les variables C# sont discutés. Des exemples de code sont également fournis.

%[https://youtu.be/sW-fsSJaFA0]

%[https://youtu.be/rM9HostBLJ4]

## Chaînes de caractères C#

En C#, vous pouvez définir une chaîne de caractères en utilisant la classe `System.String` ou son alias, `string`. Dans l'exemple représenté dans la figure 8, les deux lignes de code sont équivalentes :

Figure 8.

```csharp
string fullName = "Gavin Lon";
System.String fullName = "Gavin Lon";

```

Une chaîne de caractères est simplement une référence à un objet en mémoire qui stocke du texte. En interne, une chaîne de caractères est un tableau d'objets char.

Pour créer un nouvel objet de chaîne de caractères, le mot-clé `new` n'est généralement pas utilisé. Le mot-clé `new` n'est utilisé que pour créer une nouvelle chaîne de caractères lorsqu'un tableau d'objets char est passé comme argument au constructeur de l'objet de chaîne de caractères pertinent.

Vous pouvez voir un exemple de ceci ci-dessous dans la figure 9.

Figure 9.

```csharp
char[] nameCharacters = { 'G', 'a', 'v', 'i', 'n', ' ', 'L', 'o', 'n' };
string fullName = new string(nameCharacters);

```

### Immuabilité des chaînes de caractères C#

Les chaînes de caractères sont des types de référence, ce qui signifie qu'une référence numérique à une adresse mémoire est stockée sur la pile et pointe vers les données de chaîne de caractères réelles qui sont stockées sur le tas.

La différence entre le type de référence de chaîne de caractères et les autres types de référence (comme, par exemple, un objet instancié à partir d'une classe) est que les données pour une chaîne de caractères particulière (stockées sur le tas) ne peuvent pas être directement modifiées en mémoire. Cela signifie que chaque fois, par exemple, qu'une opération de concaténation se produit dans le code, l'adresse mémoire stockée sur la pile est simplement modifiée pour pointer vers un nouvel emplacement mémoire sur le tas qui stocke la nouvelle chaîne de caractères qui a été créée à la suite de l'opération de concaténation pertinente.

### Littéraux de chaîne de caractères entre guillemets, littéraux de chaîne de caractères verbatim et littéraux de chaîne de caractères bruts

#### Littéraux de chaîne de caractères entre guillemets

Les littéraux de chaîne de caractères entre guillemets sont des valeurs de chaîne de caractères définies sur une ligne dans le code qui commencent par un seul caractère de guillemet double et se terminent par un seul caractère de guillemet double. Les littéraux de chaîne de caractères entre guillemets sont les mieux adaptés pour les chaînes de caractères qui existent sur une ligne et ne contiennent pas de séquences d'échappement.

Si vous deviez inclure un caractère de barre oblique inverse (`\`) dans un littéral de chaîne de caractères entre guillemets (comme lors de l'expression d'un chemin de répertoire, par exemple), vous devriez échapper le caractère de barre oblique inverse avec un caractère de barre oblique inverse directement précédant le caractère de barre oblique inverse que vous souhaitez sortir comme partie de la chaîne de caractères.

Voici un exemple de ceci représenté dans la figure 11.

Figure 11.

```csharp
string path = "C:\\development\\CSharpProjects";
Console.Write(path);
// Sortie : C:\development\CSharpProjects

```

Le caractère `\` a une signification spéciale en C#, il doit donc être échappé avec le caractère d'échappement approprié – qui est le caractère `\`. Pour clarifier que le caractère `\` est un caractère d'échappement utilisé dans les littéraux de chaîne de caractères C#, voir l'exemple ci-dessous (dans la figure 12) où le caractère `\` est utilisé pour échapper les caractères de guillemet double (`"`) inclus dans un littéral de chaîne de caractères.

Figure 12.

```csharp
string path = "\"C:\\development\\CSharpProjects\"";
Console.WriteLine(path);
//Sortie : "C:\development\CSharpProjects"

```

#### Littéraux de chaîne de caractères verbatim

Les littéraux de chaîne de caractères verbatim sont recommandés lorsque des guillemets et des caractères de barre oblique inverse doivent être inclus dans la sortie pour les littéraux de chaîne de caractères. Si vous précédez un littéral de chaîne de caractères avec le symbole `@`, le code pertinent peut sortir la chaîne de caractères pertinente verbatim.

Notez comment le code dans la figure 13 produit le même résultat que le code représenté dans la figure 12.

Figure 13.

```csharp
string path = @"""C:\development\CSharpProjects""";
Console.WriteLine(path);
// Sortie : "C:\development\CSharpProjects"

```

La sortie est la même lorsque le même littéral de chaîne est représenté dans le code comme un littéral de chaîne de caractères entre guillemets et comme un littéral de chaîne de caractères verbatim.

Mais l'utilisation d'un littéral de chaîne de caractères verbatim est beaucoup plus facile à lire et est plus propre dans sa représentation. Donc, lorsque les symboles de barre oblique inverse et de guillemet double doivent être sortis dans le littéral de chaîne de caractères, il est préférable d'utiliser un littéral de chaîne de caractères verbatim.

Il est également préférable d'utiliser un littéral de chaîne de caractères verbatim pour le code qui sort du texte multilingue. Dans la figure 14 se trouve un exemple de code où un littéral de chaîne de caractères verbatim est utilisé dans le code pour sortir du texte multilingue.

Figure 14.

```csharp
string narrative =
    @"Humpty Dumpty sat on the wall
Humpty Dumpty had a great fall
all the kings horses and all the kings men
couldnt put Humpty together again";

```

Ainsi, l'exemple de code ci-dessus représenté dans la figure 14 produirait le récit tel qu'il est écrit dans le littéral de chaîne – c'est-à-dire que le texte est sorti sur plusieurs lignes comme le texte apparaît dans le littéral de chaîne dans le code.

#### Littéraux de chaîne de caractères bruts

C# 11 a introduit les littéraux de chaîne de caractères bruts. Ceux-ci rendent encore plus facile l'écriture de code pour sortir du texte multilingue.

Les littéraux de chaîne de caractères bruts suppriment le besoin d'utiliser des séquences d'échappement dans les littéraux de chaîne.

Pour indiquer dans le code que vous utilisez un littéral de chaîne de caractères brut, vous enveloppez le texte pertinent dans trois symboles de guillemets doubles. Ainsi, les trois premiers caractères doivent être trois symboles de guillemets doubles suivis du littéral de chaîne, et les trois derniers caractères doivent être trois symboles de guillemets doubles.

Notez que dans cet exemple, les trois guillemets qui enveloppent le littéral de chaîne apparaissent sur leur propre ligne. Cela est important car dans cet exemple, la première partie du littéral de chaîne apparaît dans des guillemets doubles.

Notez la sortie du code ci-dessous dans la figure 15.

Figure 15.

```csharp
string text = """
"To be or not to be" is a quote from Shakespeare's Hamlet.
""";
Console.WriteLine(text);
// Output: "To be or not to be" is a quote from Shakespeares Hamlet.

```

Notez la sortie de l'exemple de code représenté dans la figure 16.

Figure 16.

```csharp
string path = """C:\development\CSharpProjects""";
Console.WriteLine(path);
// Output: C:\development\CSharpProjects

```

Vous pourriez sortir le texte multilingue montré dans l'exemple de code dans la figure 17, où la sortie est affichée à l'écran de la même manière que le texte est représenté sur plusieurs lignes dans le littéral de chaîne brut pertinent dans le code.

Notez que lorsque vous utilisez un littéral de chaîne brut pour sortir plusieurs lignes de texte, les trois caractères de guillemets doubles qui doivent être utilisés pour envelopper le texte multilingue pertinent doivent chacun être sur leur propre ligne, comme le montre l'exemple dans la figure 17.

Figure 17.

```csharp
string narrative = """
Humpty Dumpty sat on the wall
Humpty Dumpty had a great fall
all the kings horses and all the kings men
couldnt put Humpty together again
""";

```

## Méthodes intégrées utiles pour les chaînes de caractères C#

Le langage C# possède de nombreuses méthodes intégrées utiles pour les chaînes de caractères qui peuvent, par exemple, être exploitées pour des fonctionnalités courantes liées aux chaînes de caractères.

### La méthode intégrée IndexOf

Un exemple courant est la recherche d'un littéral de chaîne de caractères dans un texte stocké dans une variable de chaîne de caractères en utilisant la méthode `IndexOf`. Voir l'exemple de code de ceci représenté dans la figure 18.

Figure 18.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";

// trouver freeCodeCamp dans le récit
var indx = narrative.IndexOf("freeCodeCamp");

// la valeur de indx sera 46
if (indx == -1)
{
    Console.WriteLine("\"freeCodeCamp\" could not be found in the narrative");
}
else
{
    Console.WriteLine($"\"freeCodeCamp\" was found at position {indx} in the narrative");
}
indx = narrative.IndexOf("Gavin Lon");

// la valeur de indx sera 0
if (indx == -1)
{
    Console.WriteLine("\"Gavin Lon\" could not be found in the narrative");
}
else
{
    Console.WriteLine($"\"Gavin Lon\" was found at position {indx}");
}
// Output:
// "freeCodeCamp" was found at position 46 in the narrative
// "Gavin Lon" was found at position 0

```

### La méthode intégrée Replace

Un autre exemple de fonctionnalité courante liée aux chaînes de caractères utilisée en C# est la recherche d'une valeur littérale de chaîne de caractères spécifique dans un texte stocké dans une variable et le remplacement du littéral de chaîne de caractères pertinent par une autre valeur littérale de chaîne de caractères. Vous pouvez faire cela en C# en utilisant la méthode intégrée `Replace`.

Consultez l'exemple de code montrant cela dans la figure 19.

Figure 19.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";
var newNarrative = narrative.Replace("Gavin Lon", "Farhan Hassan Chowdury");
Console.WriteLine(newNarrative);
// Output: Farhan Hassan Chowdury loves to create free courses on the freeCodeCamp YouTube channel.

```

### La méthode intégrée Substring

Un autre exemple courant est l'assignation d'une portion de texte stockée dans une variable à une autre variable en utilisant la méthode intégrée `Substring`. Voici un exemple de code illustrant cela dans la figure 20.

Figure 20.

```csharp
var narrative = "Gavin Lon loves to create free courses on the freeCodeCamp YouTube channel.";
var charityName = narrative.Substring(46, 12);
Console.WriteLine(charityName);
// Output: freeCodeCamp

```

Vous pouvez également regarder la vidéo YouTube ci-dessous pour plus d'informations et d'exemples de code sur l'utilisation et la manipulation des chaînes de caractères en C#.

%[https://youtu.be/tzJjrrOe69c]

## Conversion de types de données C#

Comme nous l'avons discuté précédemment, en C#, les variables sont typées statiquement au moment de la compilation. Cela signifie qu'une fois qu'une variable a été définie comme un type spécifique, vous ne pouvez pas redéfinir la variable et vous ne pouvez pas assigner une valeur d'un type de données incompatible à une variable.

Jetez un coup d'œil à l'exemple représenté dans la figure 21 qui met en évidence le typage statique en C#.

Figure 21.

```csharp
string narrative = "The cat sat on the mat.";
narrative = 1 + 1; // Erreur de compilation : "Impossible de convertir implicitement le type 'int' en 'string'"

```

Voici un exemple de ce qui se passe si vous essayez de définir une variable deux fois dans le code :

Figure 22.

```csharp
int a = 1;
string a = "one";
// Le compilateur signalerait immédiatement une erreur et soulignerait la variable 'a', où une tentative de
// définir la variable, a, comme une chaîne est faite.
// Une erreur de compilation se produit : "Une variable locale ou une fonction nommée 'a' est déjà définie dans cette portée"

```

### Conversion implicite vs explicite de types de données

Les variables définies comme des types de données numériques peuvent être converties implicitement en certains autres types de données numériques – mais dans d'autres cas, une conversion explicite est requise.

La conversion implicite de types de données signifie que le compilateur convertira automatiquement une variable définie comme un type de données en un autre type de données, et vous n'avez pas besoin d'implémenter le code de conversion de types de données explicite approprié pour que la conversion de types de données appropriée se produise.

L'exemple de code suivant dans la figure 23 démontre la tentative de conversion implicite d'une variable définie comme un entier court en type de données byte. Notez les lignes commentées qui expliquent ce qui se passe dans votre éditeur de code.

Figure 23.

```csharp
short b = 255;
byte a = b;
// Le compilateur signalerait immédiatement une exception et une ligne rouge en zigzag apparaîtrait sous
// la variable b dans la deuxième ligne de code.
// Si vous passez votre pointeur de souris sur la ligne rouge en zigzag, le message d'erreur suivant est
// présenté : "Impossible de convertir implicitement le type 'short' en 'byte'. Une conversion explicite existe (manque-t-il un cast ?)"

```

Après avoir lu les lignes commentées dans la figure 23, vous pouvez voir qu'une conversion explicite est requise pour satisfaire le compilateur C#.

Le code dans la figure 24 montre comment vous pouvez utiliser une conversion de type explicite dans ce cas pour empêcher l'exception de type de données de compilation pertinente d'être signalée.

Figure 24.

```csharp
short b = 255;
byte a = Convert.ToByte(b);
Console.Write(b);
// Lorsque ce code s'exécute, 255 est imprimé à l'écran de la console

```

Il est important de noter qu'une conversion de type explicite peut entraîner une erreur d'exécution. Si vous aviez assigné à `b` une valeur de `256` au lieu de `255` (comme dans le code représenté dans la figure 24), une erreur d'exécution se produirait lorsque le code est exécuté.

Ainsi, cette conversion de type explicite est dangereuse car, dans ce cas, le code erroné ne serait pas signalé au moment de la compilation – ce qui vous aurait forcé à corriger l'erreur au moment de la compilation (avant que le code ne soit publié en production). Ainsi, ce code entraînerait une erreur d'exécution.

L'erreur est causée parce que le type de données byte prend en charge le stockage de valeurs de nombres entiers en mémoire de `0` à `255`. Une valeur de `256` est clairement en dehors de cette plage, donc une erreur d'exécution se produira avec le message d'erreur suivant, `System.OverFlowException: La valeur était soit trop grande soit trop petite pour un byte non signé.`. Ainsi, une valeur de `256` doit être stockée dans une variable définie avec un type de données qui prend en charge une plage supérieure à celle prise en charge par le type de données byte.

Le type de données suivant en C# qui prend en charge une plage plus grande que le type de données byte pour les valeurs de nombres entiers est le type de données entier court (ou type de données short). La plage de valeurs qu'un type de données short prend en charge est de `-32,768` à `32,767`.

La variable définie comme le type de données short serait clairement appropriée pour stocker une valeur de nombre entier de `256`.

Le type de données suivant qui prend en charge une plage de valeurs plus grande pour les nombres entiers (que le type de données short) est le type de données int. Le type de données int prend en charge une plage de valeurs de `-2,147,483,648` à `2,147,483,647`.

Le type de données qui prend en charge la plus grande plage de valeurs pour les nombres entiers est le type de données long, qui prend en charge des valeurs de `-9,223,372,036,854,775,808` à `9,223,372,036,854,775,807`.

Comme nous venons de le discuter, le langage C# dispose de types de données comme le type de données byte, le type de données short, le type de données int et le type de données long pour définir des variables dans le but de stocker des valeurs de nombres entiers.

En C#, il existe des types de données intégrés appropriés pour le stockage de valeurs contenant des parties fractales. Trois types de données que vous pouvez utiliser pour la définition de variables pour le stockage de valeurs avec des parties fractales sont les types de données float, double et decimal.

Un excellent exemple d'un type de valeur où vous souhaiteriez utiliser l'un de ces types de données pour définir une variable (pour stocker une valeur contenant une partie fractale) est le type de données decimal utilisé pour stocker des valeurs monétaires. Vous pourriez utiliser le type de données float ou double pour stocker des valeurs monétaires, mais le type de données decimal est plus approprié pour ce scénario. Cela est dû au fait que le type de données decimal (bien qu'il supporte une magnitude inférieure à celle des types de données float ou double) supporte une plus grande précision.

Dans une application bancaire, par exemple, où la précision des valeurs monétaires est d'une importance capitale, la prise en compte des fractions de valeur est essentielle. Ainsi, le type de données decimal (qui supporte la plus haute précision pour les valeurs en C#) devrait être utilisé pour stocker les valeurs monétaires.

Gardez à l'esprit que des données peuvent être perdues lors de la conversion d'une valeur stockée dans une variable définie comme un type de données particulier en un autre type de données.

Par exemple, si vous avez une valeur monétaire stockée dans une variable définie comme un type de données decimal qui contient une partie fractale, la conversion de cette valeur en, par exemple, un type de données int entraînerait la perte de la partie fractale de la valeur.

Voici un exemple de ceci représenté dans la figure 25.

Figure 25

```csharp
var monetaryValue = 10.34m; // notez que si le suffixe 'm' n'est pas fourni, le type de données est

// supposé être le type de données double.
// Le suffixe 'm' définit explicitement la variable comme
// décimale
var value = Decimal.ToInt32(monetaryValue); // convertit la décimale en int
Console.WriteLine(value); // cela affiche 10 - la valeur de 0.34 est perdue

```

Ainsi, vous pouvez voir qu'une valeur de `0.34` serait perdue à la suite de l'exécution du code de conversion de type de données représenté dans la figure 25.

Vous pouvez consulter la vidéo YouTube ci-dessous pour plus d'informations sur les conversions de types de données implicites et explicites en C#.

%[https://youtu.be/NF4lyA1yx8Y]

## Opérateurs C#

Les opérateurs C# sont composés d'un ou plusieurs symboles qui indiquent au compilateur C# qu'une opération particulière doit être effectuée entre les opérandes pertinents.

Dans la figure 26, nous avons quelques exemples simples d'opérateurs intégrés C# utilisés pour effectuer des opérations mathématiques.

Figure 26.

```csharp
var a = 1;
var b = 2;
var r = a + b; // le symbole '+' indique au compilateur d'effectuer une opération d'addition appropriée
Console.WriteLine(r); // imprime 3 à l'écran
r = a * 2; // le symbole '*' indique au compilateur d'effectuer une opération de multiplication appropriée
Console.WriteLine(r); // imprime 2 à l'écran
r = b - a; // le symbole '-' indique au compilateur d'effectuer une opération de soustraction appropriée
Console.WriteLine(r); // imprime 1 à l'écran
r = b / 2; // le symbole '/' indique au compilateur d'effectuer une opération de multiplication appropriée
Console.WriteLine(r); // imprime 1 à l'écran

```

Typiquement, vous êtes en mesure de surcharger le comportement par défaut des opérateurs intégrés pour les types de données numériques en C#. Vous pouvez donc changer le comportement d'opérateurs spécifiques entre deux opérandes définis comme des types de données intégrés C# spécifiques.

Dans l'exemple ci-dessus, l'opérateur `+` effectue une opération mathématique d'addition entre les opérandes pertinents. Vous pourriez écrire du code pour surcharger l'opérateur `+` et changer la fonctionnalité d'addition par défaut entre deux entiers.

Par exemple, au lieu d'effectuer une opération d'addition entre `1` et `2` où une valeur de `3` est le résultat de l'opération pertinente, votre code de surcharge d'opérateur pourrait retourner `12`. Dans ce cas, `1` et `2` sont simplement mis ensemble comme si une concaténation de deux valeurs de chaîne était effectuée. Une valeur entière de `12` serait le résultat de l'opération pertinente.

Bien sûr, la surcharge de l'opérateur de cette manière peut ne pas être très pratique. Cet exemple illustre simplement comment vous pourriez changer le comportement de l'opérateur `+` entre deux valeurs entières en surchargeant l'opérateur `+` en C#.

### Types d'opérateurs C#

Le tableau ci-dessous est copié de la plateforme Microsoft Learn à cette URL, [https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators](https://learn.microsoft.com/en-us/dotnet/csharp/language-reference/operators)

<table>
<thead>
<tr>
<th>Opérateurs</th>
<th>Catégorie ou nom</th>
</tr>
</thead>
<tbody>
<tr>
<td><a href="member-access-operators#member-access-expression-" data-linktype="relative-path">x.y</a>, <a href="member-access-operators#invocation-expression-" data-linktype="relative-path">f(x)</a>, <a href="member-access-operators#indexer-operator-" data-linktype="relative-path">a[i]</a>, <a href="member-access-operators#null-conditional-operators--and-" data-linktype="relative-path"><code>x?.y</code></a>, <a href="member-access-operators#null-conditional-operators--and-" data-linktype="relative-path"><code>x?[y]</code></a>, <a href="arithmetic-operators#increment-operator-" data-linktype="relative-path">x++</a>, <a href="arithmetic-operators#decrement-operator---" data-linktype="relative-path">x--</a>, <a href="null-forgiving" data-linktype="relative-path">x!</a>, <a href="new-operator" data-linktype="relative-path">new</a>, <a href="type-testing-and-cast#typeof-operator" data-linktype="relative-path">typeof</a>, <a href="../statements/checked-and-unchecked" data-linktype="relative-path">checked</a>, <a href="../statements/checked-and-unchecked" data-linktype="relative-path">unchecked</a>, <a href="default" data-linktype="relative-path">default</a>, <a href="nameof" data-linktype="relative-path">nameof</a>, <a href="delegate-operator" data-linktype="relative-path">delegate</a>, <a href="sizeof" data-linktype="relative-path">sizeof</a>, <a href="stackalloc" data-linktype="relative-path">stackalloc</a>, <a href="pointer-related-operators#pointer-member-access-operator--" data-linktype="relative-path">x-&gt;y</a></td>
<td>Primaire</td>
</tr>
<tr>
<td><a href="arithmetic-operators#unary-plus-and-minus-operators" data-linktype="relative-path">+x</a>, <a href="arithmetic-operators#unary-plus-and-minus-operators" data-linktype="relative-path">-x</a>, <a href="boolean-logical-operators#logical-negation-operator-" data-linktype="relative-path">!x</a>, <a href="bitwise-and-shift-operators#bitwise-complement-operator-" data-linktype="relative-path">~x</a>, <a href="arithmetic-operators#increment-operator-" data-linktype="relative-path">++x</a>, <a href="arithmetic-operators#decrement-operator---" data-linktype="relative-path">--x</a>, <a href="member-access-operators#index-from-end-operator-" data-linktype="relative-path">^x</a>, <a href="type-testing-and-cast#cast-expression" data-linktype="relative-path">(T)x</a>, <a href="await" data-linktype="relative-path">await</a>, <a href="pointer-related-operators#address-of-operator-" data-linktype="relative-path">&amp;x</a>, <a href="pointer-related-operators#pointer-indirection-operator-" data-linktype="relative-path">*x</a>, <a href="true-false-operators" data-linktype="relative-path">true and false</a></td>
<td>Unaire</td>
</tr>
<tr>
<td><a href="member-access-operators#range-operator-" data-linktype="relative-path">x..y</a></td>
<td>Plage</td>
</tr>
<tr>
<td><a href="switch-expression" data-linktype="relative-path">switch</a>, <a href="with-expression" data-linktype="relative-path">with</a></td>
<td><code>switch</code> et <code>with</code> expressions</td>
</tr>
<tr>
<td><a href="arithmetic-operators#multiplication-operator-" data-linktype="relative-path">x * y</a>, <a href="arithmetic-operators#division-operator-" data-linktype="relative-path">x / y</a>, <a href="arithmetic-operators#remainder-operator-" data-linktype="relative-path">x % y</a></td>
<td>Multiplicatif</td>
</tr>
<tr>
<td><a href="arithmetic-operators#addition-operator-" data-linktype="relative-path">x + y</a>, <a href="arithmetic-operators#subtraction-operator--" data-linktype="relative-path">x  y</a></td>
<td>Additif</td>
</tr>
<tr>
<td><a href="bitwise-and-shift-operators#left-shift-operator-" data-linktype="relative-path">x &lt;&lt;  y</a>, <a href="bitwise-and-shift-operators#right-shift-operator-" data-linktype="relative-path">x &gt;&gt; y</a>, <a href="bitwise-and-shift-operators#unsigned-right-shift-operator-" data-linktype="relative-path">x &gt;&gt;&gt; y</a></td>
<td>Décalage</td>
</tr>
<tr>
<td><a href="comparison-operators#less-than-operator-" data-linktype="relative-path">x &lt; y</a>, <a href="comparison-operators#greater-than-operator-" data-linktype="relative-path">x &gt; y</a>, <a href="comparison-operators#less-than-or-equal-operator-" data-linktype="relative-path">x &lt;= y</a>, <a href="comparison-operators#greater-than-or-equal-operator-" data-linktype="relative-path">x &gt;= y</a>, <a href="type-testing-and-cast#is-operator" data-linktype="relative-path">is</a>, <a href="type-testing-and-cast#as-operator" data-linktype="relative-path">as</a></td>
<td>Relationnel et test de type</td>
</tr>
<tr>
<td><a href="equality-operators#equality-operator-" data-linktype="relative-path">x == y</a>, <a href="equality-operators#inequality-operator-" data-linktype="relative-path">x != y</a></td>
<td>Égalité</td>
</tr>
<tr>
<td><code>x &amp; y</code></td>
<td><a href="boolean-logical-operators#logical-and-operator-" data-linktype="relative-path">ET logique booléen</a> ou <a href="bitwise-and-shift-operators#logical-and-operator-" data-linktype="relative-path">ET logique bit à bit</a></td>
</tr>
<tr>
<td><code>x ^ y</code></td>
<td><a href="boolean-logical-operators#logical-exclusive-or-operator-" data-linktype="relative-path">OU exclusif logique booléen</a> ou <a href="bitwise-and-shift-operators#logical-exclusive-or-operator-" data-linktype="relative-path">OU exclusif logique bit à bit</a></td>
</tr>
<tr>
<td><code>x | y</code></td>
<td><a href="boolean-logical-operators#logical-or-operator-" data-linktype="relative-path">OU logique booléen</a> ou <a href="bitwise-and-shift-operators#logical-or-operator-" data-linktype="relative-path">OU logique bit à bit</a></td>
</tr>
<tr>
<td><a href="boolean-logical-operators#conditional-logical-and-operator-" data-linktype="relative-path">x &amp;&amp; y</a></td>
<td>ET conditionnel</td>
</tr>
<tr>
<td><a href="boolean-logical-operators#conditional-logical-or-operator-" data-linktype="relative-path">x || y</a></td>
<td>OU conditionnel</td>
</tr>
<tr>
<td><a href="null-coalescing-operator" data-linktype="relative-path">x ?? y</a></td>
<td>Opérateur de coalescence nulle</td>
</tr>
<tr>
<td><a href="conditional-operator" data-linktype="relative-path">c ? t : f</a></td>
<td>Opérateur conditionnel</td>
</tr>
<tr>
<td><a href="assignment-operator" data-linktype="relative-path">x = y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x += y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x -= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x *= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x /= y</a>, <a href="arithmetic-operators#compound-assignment" data-linktype="relative-path">x %= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x &amp;= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x |= y</a>, <a href="boolean-logical-operators#compound-assignment" data-linktype="relative-path">x ^= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &lt;&lt;= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &gt;&gt;= y</a>, <a href="bitwise-and-shift-operators#compound-assignment" data-linktype="relative-path">x &gt;&gt;&gt;= y</a>, <a href="null-coalescing-operator" data-linktype="relative-path">x ??= y</a>, <a href="lambda-operator" data-linktype="relative-path">=&gt;</a></td>
<td>Assignation et déclaration de lambda</td>
</tr>
</tbody>
</table>


Pour plus d'informations sur les opérateurs C#, vous pouvez regarder la vidéo YouTube ci-dessous :

%[https://youtu.be/qGgwm95FK5M]

Pour des instructions sur la façon de surcharger les opérateurs en C#, consultez la vidéo YouTube suivante :

%[https://youtu.be/tq3_8GQxM14]

## Constantes et variables en lecture seule

### Introduction aux constantes

Une constante est similaire à une variable dans le sens où vous pouvez y stocker une valeur en la déclarant et en lui assignant une valeur. Vous pouvez ensuite référencer cette valeur avec un nom lisible par l'homme qui désigne la valeur constante dans le code.

Une constante est différente d'une variable dans le sens où elle doit être assignée à une valeur sur la même ligne où elle est déclarée. De plus, une fois que vous avez assigné une valeur à une constante, vous ne pouvez pas assigner une nouvelle valeur à cette constante à un autre moment dans le code.

Vous devriez utiliser des constantes dans votre code lorsqu'elles rendent votre code plus lisible et maintenable. Lorsque vous utilisez une constante de manière appropriée, vous n'avez pas à répéter une valeur que vous avez assignée à la constante dans votre code. Lorsque vous devez référencer cette valeur dans le code, vous pouvez plutôt inclure le nom lisible par l'homme que vous avez donné à la constante dans votre code qui désigne la valeur constante pertinente.

Si une valeur constante doit changer, vous n'avez besoin de changer le code qu'à un seul endroit (c'est-à-dire là où la constante a été déclarée). Ce changement se propagera automatiquement là où la constante est référencée dans d'autres lignes de code (qui sont correctement portées).

### Introduction aux variables en lecture seule

Une variable en lecture seule est similaire à une variable en ce sens que vous pouvez y stocker une valeur en la déclarant et en lui assignant une valeur. Vous pouvez ensuite référencer cette valeur avec un nom lisible par l'homme qui désigne la variable en lecture seule.

Une variable en lecture seule est différente d'une variable en ce sens que sa valeur ne peut être changée qu'une seule fois dans le code après avoir été déclarée. Sa valeur peut être changée dans le constructeur d'une classe, mais ne peut pas être changée dans d'autres parties de votre code.

Ainsi, si vous avez assigné une variable en lecture seule avec une valeur dans la ligne où elle est déclarée, vous pouvez assigner cette variable en lecture seule avec une valeur différente dans le constructeur d'une classe – mais vous ne pouvez pas ensuite assigner une nouvelle valeur à cette variable en lecture seule dans un autre code.

Ainsi, une variable en lecture seule est souvent appelée une constante d'exécution. Une constante est déclarée et assignée à sa valeur sur la même ligne de code au moment de la compilation, et la valeur de cette constante ne peut pas être modifiée ultérieurement au moment de la compilation (et donc ne peut pas non plus être modifiée au moment de l'exécution).

Une variable en lecture seule est assignée à la valeur qui ne peut pas être modifiée ultérieurement au moment de l'exécution. Ainsi, avec une variable en lecture seule, où elle est assignée à une valeur dans le constructeur d'une classe, elle est définie une fois lorsqu'un objet instance est créé à partir de cette classe au moment de l'exécution. Cette variable en lecture seule ne peut pas être modifiée après cette assignation.

### Exemple de code utilisant une constante

Voici un exemple de la façon d'utiliser une constante représenté dans la figure 27.

Figure 27.

```csharp
const int SpeedOfLight = 299792458;
Console.WriteLine($"La vitesse de la lumière est {SpeedOfLight}");
// La sortie pour ce code est :
// La vitesse de la lumière est 299792458

```

### Exemple de code utilisant une variable en lecture seule

Et voici un exemple dans la figure 28 de la façon d'utiliser une variable en lecture seule :

Figure 28.

```csharp
Employee employee = new Employee("Admin");
employee.PrintEmployeeRole();

```

Remarquez comment la variable en lecture seule de type chaîne nommée "RoleName" a été assignée à une valeur deux fois. Elle est assignée à une chaîne vide lorsqu'elle est déclarée pour la première fois en haut de la classe. La variable en lecture seule est assignée à sa valeur finale dans le constructeur de la classe "Employee".

Notez que vous ne pouvez changer la valeur d'une variable en lecture seule qu'une seule fois, et vous ne pouvez le faire que dans le constructeur d'une classe. Une fois qu'une valeur est assignée à une variable en lecture seule dans le constructeur d'une classe, vous ne pouvez pas changer sa valeur dans une autre partie du code.

Dans l'exemple ci-dessous dans la figure 29, une méthode nommée "SetRoleName" contient du code pour changer la valeur de la variable en lecture seule "RoleName". Cela n'est pas possible en C#, car la variable en lecture seule ne peut être assignée à sa valeur finale que dans le constructeur d'une classe. Vous ne pouvez pas, par exemple, assigner une valeur à la variable en lecture seule dans une méthode.

Ce code entraînera une erreur de compilation signalée par le compilateur C#. Le message d'erreur indiquera ce qui suit dans votre éditeur de code : "Un champ en lecture seule ne peut pas être assigné (sauf dans un constructeur ou un setter init-only du type dans lequel le champ est défini ou un initialiseur de variable)".

### Exemple de code de l'utilisation incorrecte d'une variable en lecture seule

Figure 29.

```csharp
Employee employee = new Employee("Admin");
employee.PrintEmployeeRole();

```

Pour plus d'informations sur les constantes et les variables en lecture seule, vous pouvez regarder la vidéo YouTube ci-dessous :

%[https://youtu.be/yvOdN5PBY2g]

## Instructions if / else if / else en C#

### Logique conditionnelle if/else de base

Les instructions if vous permettent d'inclure une logique conditionnelle dans votre code. Regardons un exemple de base pour voir comment elles fonctionnent.

Supposons que vous travaillez sur une application de panier d'achat et qu'un morceau de code particulier ajoute un produit au panier d'achat de l'utilisateur. Dans votre code, vous ne voulez que cet article ajouté au panier d'achat de l'utilisateur si le produit est en stock.

Lorsque l'utilisateur essaie d'ajouter un produit qui est en rupture de stock, vous voulez qu'un message s'affiche pour informer l'utilisateur que l'article qu'il souhaite ajouter n'est pas en stock. Vous pourriez également ajouter à ce message qu'ils devraient essayer d'ajouter cet article à leur panier d'achat dans une semaine (c'est-à-dire lorsque l'article pourrait être en stock).

En C#, pour automatiser cette logique conditionnelle, vous pouvez implémenter une instruction `if / else`. Le code dans la figure 30 montre à quoi cela pourrait ressembler :

```csharp
Product product = new();
product.Name = "Ladder";
product.ItemCount = 10;
if (product.ItemCount == 0)
{
    DisplayMessage($"{product.Name} is currently not in stock. Please try again in a week.");
}
else
{
    AddToShopingCart(product);
    DisplayMessage($"A {product.Name} has been successfully added to your shopping cart.");
}
void DisplayMessage(string message)
{
    Console.WriteLine(message);
}
void AddToShopingCart(Product product)
{
    Console.WriteLine("Code runs to add product");
}

class Product
{
    public string Name { get; set; } = "";
    public int ItemCount { get; set; }
}

```

L'instruction `if` contient une expression booléenne. Une expression booléenne retourne soit `true` soit `false`. Si le produit est en stock, cette expression booléenne, `product.ItemCount == 0`, retournera `false`. Si le produit n'est pas en stock, alors l'expression booléenne retournera `true`.

L'expression de l'instruction `if` évalue si le produit pertinent est actuellement en stock. Si le produit pertinent n'est plus en stock, la propriété `ItemCount` retournera `0`. Dans ce cas, où le nombre de produits en stock est égal à `0`, le code s'exécute et informe l'utilisateur que le produit n'est pas en stock et qu'il devrait essayer d'ajouter le produit à son panier dans une semaine.

Cependant, si le nombre de stocks pour le produit n'est pas égal à `0` (ce qui signifie que le produit est en stock), le code s'exécute pour ajouter le produit au panier d'achat de l'utilisateur. Un message apparaîtra également sur l'écran de l'utilisateur indiquant que le produit a été ajouté avec succès au panier d'achat de l'utilisateur.

Vous pouvez simplement inclure une instruction `if` seule – et ne pas inclure de bloc `else` dans la logique conditionnelle pertinente. Par exemple, supposons que vous souhaitiez afficher un message aux personnes utilisant une application bancaire. Lorsque leur compte est à découvert (c'est-à-dire qu'ils ont retiré trop d'argent), le code pourrait ressembler à l'exemple de base dans la figure 31 :

Figure 31.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 2000m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    DisplayMessage("Your account is overdrawn."); // ce message sera affiché à l'utilisateur
}

```

### Implémentation de la logique conditionnelle if/else if/else

Supposons qu'en plus de la logique de code ci-dessus, nous voulons ajouter une exigence afin qu'un message spécifique soit affiché à la personne si elle peut effectuer un retrait sans que son compte soit à découvert.

Dans cette exigence, nous voulons également inclure un message qui s'affiche si leur retrait entraîne un solde inférieur à `100` dollars.

Pour tenir compte de ces exigences supplémentaires, nous pouvons mettre à jour la logique conditionnelle pertinente avec un bloc `else if` et un bloc `else`. Le code dans la figure 32 montre à quoi pourrait ressembler ce code.

Figure 32.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 876m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    DisplayMessage("Your account is overdrawn.");
}
else if (balance < 100)
{
    DisplayMessage("You have less than 100 dollars left in your account.");
}
else
{
    DisplayMessage($"You have successfully withdrawn {withdrawalAmount} dollars");
}

```

Ainsi, comment fonctionne le code `if/else if/ else` ? La première expression booléenne est évaluée, ce qui tient compte du fait que le solde est inférieur à `0`. Si cette expression retourne `true`, le message, `"Your account is overdrawn."`, est affiché à l'utilisateur.

Si cette expression retourne `false`, le code dans le bloc `else if` est évalué, puis l'expression est évaluée pour vérifier si le solde est inférieur à `100`. Si cette expression retourne `true` (c'est-à-dire si la valeur de `balance` est inférieure à `100`), le message, `"You have less than 100 dollars left in your account."`, est affiché à l'utilisateur.

Si, cependant, l'expression retourne `false`, cela signifie que le code dans le bloc `else` est exécuté. Ainsi, le message, `"You have successfully withdrawn {withdrawalAmount} dollars"` est affiché à l'écran.

Chaque expression est évaluée de haut en bas et chaque section du code `if/else if/else` est mutuellement exclusive. Cela signifie que seule l'une des instructions dans chacune des sections de la logique `if/else if/else` peut être exécutée lorsque la logique conditionnelle pertinente est exécutée.

Lorsque cette logique conditionnelle est exécutée, seul l'un des messages sera affiché à l'utilisateur suite à leur retrait de leur compte.

### Instructions if imbriquées

Vous pouvez également inclure des instructions if imbriquées dans votre logique conditionnelle. Un exemple de ceci est représenté dans la figure 33.

Figure 33.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 6500m;
var balance = currentAccountValue - withdrawalAmount;
if (balance < 0)
{
    if (balance < -5000)
    {
        DisplayMessage(
            "You have reached your allowable overdraft limit. You will be charged a penalty amount!"
        );
    }
    else
    {
        DisplayMessage("Your account is overdrawn.");
    }
}
else if (balance < 100)
{
    DisplayMessage("You have less than 100 dollars left in your account.");
}
else
{
    DisplayMessage($"You have successfully withdrawn {withdrawalAmount} dollars");
}

```

Dans l'exemple ci-dessus, l'instruction `if` supérieure vérifie d'abord si le compte a été à découvert. Si le compte a été à découvert (c'est-à-dire que la valeur de `balance` est inférieure à `0`), une instruction `if/else` imbriquée s'exécute. Une instruction `if` imbriquée est une instruction `if` qui réside dans une autre instruction `if`.

L'instruction `if` imbriquée ne s'exécute que si l'expression dans l'instruction `if` dans laquelle l'instruction `if` imbriquée réside retourne `true`.

L'instruction `if` imbriquée représentée dans la figure 33 évalue en outre si le solde est inférieur à `-5000`. Si cette expression retourne `true`, alors l'utilisateur voit un message l'informant que le montant qu'il vient de retirer de son compte a entraîné un découvert (c'est-à-dire dépassant le montant de découvert autorisé). Il informe également l'utilisateur qu'un montant de pénalité supplémentaire sera facturé.

Le code dans la partie `else` de l'instruction `if` imbriquée s'exécute si le solde de l'utilisateur est compris entre `-5000` et `0`. Cela signifie que son compte est à découvert mais n'entraînera pas, dans ce cas, de montant de pénalité (parce qu'il est dans sa limite de découvert autorisée).

### Expressions conditionnelles plus complexes

#### L'opérateur &&

Une instruction `if` peut inclure une logique booléenne plus complexe. Par exemple, vous pouvez utiliser l'opérateur `&&` ou l'opérateur `||` pour évaluer plusieurs expressions booléennes sur une seule ligne. La figure 34 ci-dessous représente un exemple de code utilisant l'opérateur `&&` dans une instruction `if` pour évaluer plus d'une expression booléenne sur une seule ligne.

L'opérateur `&&` peut être traduit par "Et aussi". Si la première expression du côté gauche de l'opérateur `&&` est évaluée comme `false`, cela signifie que l'expression booléenne entière évaluée par l'instruction `if` est considérée comme `false`. L'expression booléenne du côté droit de l'expression n'est pas évaluée.

Dans ce cas, `false` est retourné par l'instruction `if`, ce qui signifie que le code dans les instructions `if` ne sera pas exécuté.

Mais si, dans cet exemple, la condition du côté gauche de l'opérateur `&&` est `true`, cela signifie que l'expression du côté droit de l'opérateur `&&` doit être évaluée. Donc, dans ce cas, si la valeur de `balance` est inférieure à `-5000`, l'expression booléenne retourne `false`. Cela signifie que l'expression booléenne entière `(balance < -4000 && balance >= -5000)` est `false`. Cela signifie également que le message affiché par le code dans l'instruction `if` ne s'exécutera pas.

Mais si le code du côté droit de l'opérateur `&&` est `true` (donc dans ce cas, le solde est supérieur ou égal à `-5000`), l'expression booléenne entière dans l'instruction `if` est `true`. Cela signifie que le message dans l'instruction `if` sera affiché à l'écran. Donc, `Votre transaction est réussie mais vous êtes proche de votre limite de découvert` sera affiché à l'écran.

Figure 34.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 5500m;
var balance = currentAccountValue - withdrawalAmount;

```

#### L'opérateur ||

Vous pouvez également utiliser l'opérateur `||` (comme le montre la figure 35) lorsque cela est approprié pour les expressions booléennes qui consistent en plus d'une expression booléenne.

L'opérateur `||` peut être traduit par "ou sinon". Lorsque l'expression booléenne du côté gauche de l'opérateur `||` retourne `true`, l'expression booléenne du côté droit de l'opérateur `||` n'a pas besoin d'être évaluée. Cela est dû au fait qu'une seule des expressions doit retourner true pour que l'expression booléenne entière retourne `true`.

Si l'expression booléenne du côté gauche de l'opérateur `||` retourne `false`, alors l'expression du côté droit sera évaluée.

Si l'expression du côté droit retourne `false`, alors l'expression entière retourne `false`. Si, cependant, l'expression du côté droit de l'opérateur `||` retourne `true`, l'expression booléenne entière retourne `true`.

Figure 35.

```csharp
decimal currentAccountValue = 1000m;
decimal withdrawalAmount = 960m;
var balance = currentAccountValue - withdrawalAmount;
if (withdrawalAmount < 50 || balance < -5000)
{
    RollBackTransaction();
    DisplayMessage(
        "Your transaction failed either because you tried to withdraw less than 50 dollars or your total withdrawal would have resulted in your account having a balance of less than -5000 dollars which exceeds your overdraft limit."
    );
}
else
{
    DisplayMessage("Thank you! Your transaction was successful!");
    CommitTransaction();
}

```

Le code dans la figure 35 évalue l'expression booléenne dans l'instruction `if` comme suit : si le montant du retrait est inférieur à 50 dollars, alors annuler la transaction et afficher le message approprié. Si, cependant, le montant du retrait est supérieur à 50 dollars, l'expression du côté droit de l'opérateur `||` doit être évaluée car cela signifie que l'expression du côté gauche de l'opérateur `||` a retourné `false`.

Ainsi, si l'expression du côté droit de l'opérateur `||` retourne `true`, ce qui signifie que le solde du client est inférieur à `-5000`, le code pour annuler la transaction et afficher le message approprié doit être exécuté.

Ainsi, le point clé à retenir lors de l'utilisation de l'opérateur `||` dans une condition `if` est que si l'une des expressions de chaque côté de l'opérateur `||` retourne true, cela signifie que la condition entière retourne `true`. Pour que la condition entière retourne `false`, les deux expressions de chaque côté de l'opérateur `||` doivent retourner `false`.

Ainsi, si les deux expressions de chaque côté de l'opérateur `||` retournent `false`, cela signifie que le client a effectué un retrait valide, et la transaction du client se poursuit avec succès. Un message à cet effet est affiché au client en conséquence.

Voici une explication complète de l'utilisation des instructions `if` pour la logique conditionnelle en C# dans la vidéo YouTube ci-dessous :

%[https://youtu.be/2mChNV9GmpM]

## Boucles C#

### La boucle for

Grâce à l'utilisation de boucles dans le code, les programmeurs sont en mesure de réduire considérablement le nombre de lignes de code nécessaires pour effectuer des tâches spécifiques. Un exemple très simple de cela est l'affichage d'un compte de `1` à `10` où chaque valeur est imprimée sur une nouvelle ligne dans la fenêtre de la console. Sans utiliser de boucle, le code pourrait ressembler au code représenté dans la figure 36.

Figure 36.

```csharp
Console.WriteLine("1");
Console.WriteLine("2");
Console.WriteLine("3");
Console.WriteLine("4");
Console.WriteLine("5");
Console.WriteLine("6");
Console.WriteLine("7");
Console.WriteLine("8");
Console.WriteLine("9");
Console.WriteLine("10");

```

En utilisant une boucle `for` en C#, vous pourriez réduire 10 lignes de code à 3 lignes de code comme le montre la figure 37. Vous pourriez mettre à jour le code pour que la boucle `for` boucle 100 fois au lieu de 10 fois. Pour ce faire, vous changeriez l'expression de la boucle `for` pertinente de `count<=10` à `count <=100`. Ainsi, dans l'exemple de code représenté dans la figure 38, vous auriez réduit 100 lignes de code à 3 lignes de code en utilisant la boucle `for` pour obtenir exactement la même sortie.

Figure 37.

```csharp
for (int count = 1; count <= 10; count++)
{
    Console.WriteLine(count);
}

```

Figure 38.

```csharp
for (int count = 1; count <= 100; count++)
{
    Console.WriteLine(count);
}

```

Vous pourriez implémenter la même fonctionnalité en utilisant une boucle `while` qui boucle 10 fois comme le montre la figure 39.

### La boucle while

Figure 39.

```csharp
var count = 1;

```

### La boucle do-while

Vous pourriez implémenter la même fonctionnalité en utilisant une boucle `do-while` en C# comme le montre la figure 40.

Figure 40.

```csharp
var count = 1;
do
{
    Console.WriteLine(count);
    count++;
} while (count <= 10);

```

La différence entre une boucle `while` et une boucle `do-while` est qu'une boucle `do-while` exécutera toujours le code qu'elle contient au moins une fois. Avec une boucle `while`, l'expression conditionnelle booléenne est en haut de la boucle, donc lorsque cette expression retourne `false` (c'est-à-dire avant que le code dans la boucle `while` n'ait une chance de s'exécuter), aucun code dans la boucle `while` ne s'exécutera. Avec la boucle `do-while`, le code dans la boucle `do-while` est toujours exécuté au moins une fois. Dans l'exemple représenté dans la figure 41, les instructions dans le bloc `while` ne s'exécuteront jamais.

Figure 41.

La valeur de `count` est égale à `11` et l'expression conditionnelle booléenne, `(count <= 10)`, retourne `false`, donc les deux lignes de code dans la boucle `while` ne s'exécuteront pas. Regardons un exemple similaire mais où une boucle `do-while` est utilisée. Cet exemple est représenté dans la figure 42.

Figure 42.

```csharp
var count = 11;
do
{
    Console.WriteLine(count);
    count++;
} while (count <= 10);

```

Les lignes de code dans la boucle `do-while` s'exécuteront une fois. Ainsi, le résultat de ceci est que la valeur de `11` sera imprimée à l'écran de la console. Après que la valeur de `11` soit imprimée à l'écran de la console, l'expression booléenne, `(count <= 10)`, est exécutée. La valeur de `count` est `11`, ce qui signifie que l'expression booléenne en bas de la boucle `do-while` retourne `false`, donc la boucle sera quittée.

### La boucle foreach

En C#, vous pouvez utiliser une boucle `foreach` au lieu d'une boucle `for`. L'un des avantages de l'utilisation d'une boucle `foreach` plutôt qu'une boucle `for` est que si le nombre de traversées qui doivent se produire afin de traverser tous les éléments pertinents dans la boucle change, le code créé pour l'exécution de la boucle n'a pas besoin de changer. Considérez cet exemple représenté dans la figure 43 où une boucle `foreach` est utilisée pour imprimer chaque valeur contenue dans un tableau à l'écran de la console.

Figure 43.

```csharp
int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
foreach (var val in arr)
{
    Console.Write($"{val} ");
}
// Output:  1 2 3 4 5 6 7 8 9 10

```

Considérez ce qui se passe lorsque le nombre d'éléments et de valeurs dans le tableau sont modifiés. Veuillez consulter un exemple de code représentant ceci dans la figure 44.

Figure 44.

```csharp
int[] arr = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 12 };
foreach (var val in arr)
{
    Console.Write($"{val} ");
}
// Output:  1 2 3 4 5 6 7 8 9 10 11 13 12

```

Une boucle `for` utilisée pour exécuter le même code ressemblerait à l'exemple de code représenté dans la figure 45.

Figure 45.

```csharp
int[] arr = { 10, 8, 5, 1, 2, 6, 7, 4, 8, 9, 3, 11, 13, 12 };
for (var x = 0; x <= arr.Length - 1; x++)
{
    Console.Write($"{arr[x]} ");
}
// Output: 10 8 5 1 2 6 7 4 8 9 3 11 13 12

```

Avec la boucle `for`, la longueur du tableau doit être incluse dans le code pour exécuter la boucle. L'index du tableau doit être inclus dans le code où chaque élément est imprimé à l'écran. Vous pouvez accomplir la même tâche en utilisant une boucle `for` et une boucle `foreach` dans ces scénarios, mais la boucle `foreach` est plus propre et plus facile à lire. Ainsi, avec la boucle `foreach`, vous n'avez pas à vous soucier de l'index des éléments dans le tableau ou de la longueur du tableau.

Pour plus de détails sur les boucles en C# et plus d'exemples de code, veuillez regarder la vidéo YouTube ci-dessous ce paragraphe.

%[https://youtu.be/oO0GXIIE56U]

## Tableaux C#

Un tableau est une structure de données. Vous pouvez stocker plusieurs valeurs du même type dans un tableau. Vous pouvez également stocker plusieurs types dans un tableau en définissant les éléments du tableau comme le type de données objet.

Tous les types en C# héritent du type de données objet, donc vous pouvez stocker plusieurs types de données dans un tableau où les éléments sont définis comme des objets.

Considérez l'exemple ci-dessous représenté dans la figure 46 où un tableau d'entiers est défini qui peut stocker 10 valeurs entières.

Figure 46.

```csharp
int[] arrValues = new int[10];

```

Dans cet exemple, le tableau ne peut stocker que des valeurs entières. Si vous essayez de stocker un autre type dans ce tableau, une erreur de compilation appropriée sera signalée.

Dans l'exemple suivant dans la figure 47, vous ne pouvez stocker que des valeurs de chaîne.

Figure 47.

```csharp
string[] arrayStringValues = new string[10];

```

Mais dans l'exemple représenté dans la figure 48 ci-dessous, vous pouvez stocker à la fois des valeurs de chaîne et des valeurs entières ainsi que d'autres types de données dans le tableau. Cela est dû, comme discuté, au fait que tous les types de données en C# héritent du type de données objet. Donc dans le tableau de l'exemple ci-dessous, vous pouvez stocker des valeurs de chaîne, des valeurs entières, des valeurs décimales, des valeurs booléennes, des valeurs de caractère, des valeurs de type défini par l'utilisateur, et ainsi de suite.

Figure 48.

```csharp
object[] arrayObjectValues = new object[10];

```

Le stockage de plusieurs types de données de cette manière est connu sous le nom de 'boxing', car, par exemple, si un entier est stocké comme un élément dans un tableau défini comme un objet, les données entières sont d'abord 'boxées' dans le type objet. Cela signifie que pour récupérer les données sous leur type de données approprié à partir du tableau, la valeur doit d'abord être 'unboxée'. Cela signifie simplement que l'élément de tableau pertinent est explicitement converti d'un objet à son type de données approprié.

Il est important de noter que lorsque vous définissez un tableau comme un objet, vous contournez en effet le système de types du langage C# et perdez les avantages d'un langage fortement typé (comme une meilleure performance, ainsi qu'une robustesse accrue du code d'exécution).

Le code 'unboxing' qui doit s'exécuter lors de la récupération des valeurs du tableau peut potentiellement provoquer des erreurs d'exécution, ainsi que des surcharges de conversion à l'exécution. Et cela ralentit les performances du code.

Ainsi, il est recommandé de typer fortement le tableau pour augmenter les performances d'exécution et la robustesse d'exécution. Cela vous permet de tirer parti des avantages du système de types forts pris en charge par le langage C#.

### Tableaux à une dimension

En C#, vous avez trois types de tableaux : les tableaux à une dimension, les tableaux multidimensionnels et les tableaux irréguliers.

Un tableau à une dimension permet le stockage de données qui sont de nature unidimensionnelle. Un exemple de cela serait un tableau de notes pour un étudiant particulier pour une année particulière.

Ainsi, par exemple, supposons qu'un étudiant a reçu les notes suivantes en 2023 : 60, 50, 72, 85, 91. Ces notes pourraient être stockées dans un tableau d'entiers à une dimension comme le montre la figure 49.

Figure 49.

```csharp
int[] grades = new int[5]{60, 50, 72, 85, 91};

```

### Tableaux multidimensionnels

#### Tableaux à deux dimensions

Un exemple d'utilisation d'un tableau multidimensionnel pourrait être un tableau où les notes de plus d'un étudiant sont stockées dans le tableau. Cet exemple de code est représenté dans la figure 50 ci-dessous.

Ainsi, supposons que les notes de Sarah, John et Bob sont stockées dans le tableau à deux dimensions. Dans l'ensemble principal d'accolades, toutes les valeurs sont incluses dans le tableau à deux dimensions. Également dans l'ensemble principal d'accolades se trouvent trois ensembles d'accolades, un ensemble pour chaque étudiant. Et dans chacun des trois ensembles d'accolades se trouvent 5 notes concernant les trois étudiants.

Ainsi, supposons que le premier ensemble de notes appartient à Sarah, le deuxième ensemble de notes appartient à John et le troisième ensemble de notes appartient à Bob.

Figure 50.

```csharp
int[,] studentGrades = new int[3, 5]
{
    { 60, 50, 72, 85, 91 },
    { 50, 45, 67, 80, 93 },
    { 48, 58, 90, 57, 87 }
};

```

Ainsi, le premier indice dans le tableau est 3, qui dans cet exemple représente le nombre d'étudiants. Le deuxième indice dans le tableau représente le nombre de notes. Vous pourriez donc utiliser une boucle `for` imbriquée en C# pour parcourir les éléments de ce tableau et imprimer leurs valeurs à l'écran dans un affichage matriciel à deux dimensions.

Dans la figure 51, vous verrez un exemple de parcours d'un tableau à deux dimensions et d'affichage des résultats à l'écran de la console dans une matrice à deux dimensions.

Figure 51.

```csharp
int[,] studentGrades = new int[3, 5]
{
    { 60, 50, 72, 85, 91 },
    { 50, 45, 67, 80, 93 },
    { 48, 58, 90, 57, 87 }
};

```

#### Tableaux à trois dimensions

Vous pourriez ajouter une autre dimension à ce tableau – par exemple, vous pourriez diviser les notes pour chaque étudiant afin que les notes se rapportent à une période particulière de l'année.

Pour simplifier, divisons l'année en deux. Ainsi, pour la première moitié de 2023, Sarah a reçu les notes suivantes : 54, 42, 70, 80, 93. Pour la seconde moitié de l'année, Sarah a reçu ces notes : 65, 46, 68, 90, 95.

Ainsi, dans cet exemple (représenté dans la figure 52), le tableau à trois dimensions pertinent inclut les résultats pour Sarah et deux autres étudiants (John et Bob) où leurs résultats incluent leurs notes pour la première moitié de 2023 ainsi que leurs notes pour la seconde moitié de 2023.

Figure 52.

```csharp
int[,,] studentGrades = new int[3, 2, 5]
{
    {
        { 60, 50, 72, 85, 91 },
        { 65, 46, 68, 90, 95 }
    },
    {
        { 45, 40, 64, 70, 90 },
        { 55, 50, 73, 90, 95 }
    },
    {
        { 46, 60, 88, 55, 89 },
        { 50, 56, 92, 59, 85 }
    }
};
for (int i = 0; i < studentGrades.GetLength(0); i++)
{
    for (int j = 0; j < studentGrades.GetLength(1); j++)
    {
        for (int k = 0; k < studentGrades.GetLength(2); k++)
        {
            Console.Write($"{studentGrades[i, j, k]}\t");
        }
        Console.WriteLine();
    }
    Console.WriteLine();
    Console.WriteLine();
}

```

Ainsi, dans la figure 52 ci-dessus, vous pouvez voir que les données du premier étudiant sont imprimées à l'écran de la console où la première ligne présente les notes de l'étudiant pour la première moitié de l'année.

Cela est suivi d'un saut de ligne et les notes du premier étudiant pour la seconde moitié de l'année sont imprimées sur la ligne suivante. Deux sauts de ligne suivent les données imprimées pour le premier étudiant. Cela est suivi des notes du deuxième étudiant, et ainsi de suite.

La première dimension du tableau est dans ce cas désignée par les trois étudiants. La deuxième dimension du tableau est dans ce cas désignée par les parties de l'année (dans ce cas, l'année est divisée en 2 parties (ou deux moitiés)). La troisième dimension du tableau est désignée par les notes réelles pour chaque étudiant (dans ce cas, cinq notes).

Ainsi, représenté dans la figure 52 se trouve un exemple de tableau à trois dimensions déclaré et initialisé. Le code qui suit affiche les valeurs stockées dans le tableau à trois dimensions à l'écran de la console. Ainsi, l'exemple dans la figure 52 est un excellent exemple de code C# qui implémente des boucles for imbriquées pour imprimer les données stockées dans un tableau à 3 dimensions à l'écran de la console.

Ainsi, avec cet exemple, vous imprimez en effet des données à trois dimensions sur un écran à deux dimensions en utilisant C#.

### Tableaux irréguliers

En gros, un tableau irrégulier est un tableau de tableaux. Il vous permet de stocker des données inégales (si vous voulez).

Alors, que veux-je dire par données inégales ? Si vous revenez à l'exemple de tableau à deux dimensions représenté dans la figure 51, vous avez 5 notes représentées pour chacun des trois étudiants.

Supposons que l'étudiant numéro deux (John dans l'exemple) ne suit que les trois premières matières, donc vous n'avez que des notes pour ces trois matières pour John. Mais vous avez cinq notes concernant les trois premières matières ainsi que des notes concernant les deux dernières matières pour les deux autres étudiants (Sarah et Bob) complétées. Vous souhaitez toujours stocker les trois notes de John ainsi que les cinq notes de Sarah et Bob dans le tableau.

Eh bien, bonne nouvelle - vous pouvez stocker toutes les données (sans avoir besoin d'inclure des données de "remplissage" redondantes pour les deux notes manquantes de John) en utilisant un tableau irrégulier.

Dans l'exemple représenté dans la figure 53, le code C# est implémenté pour stocker les notes pertinentes dans un tableau irrégulier. Le code qui suit affiche les notes à l'écran de la console.

Figure 53.

```csharp
int[][] studentGrades = new int[3][];
studentGrades[0] = new int[5] { 60, 50, 72, 85, 91 }; // Notes de Sarah
studentGrades[1] = new int[3] { 50, 45, 67 }; // Notes de John
studentGrades[2] = new int[5] { 48, 58, 90, 57, 87 }; // Notes de Bob
for (int i = 0; i < studentGrades.Length; i++)
{
    for (int j = 0; j < studentGrades[i].Length; j++)
    {
        Console.Write($"{studentGrades[i][j]}\t");
    }
    Console.WriteLine();
}

```

Vous pouvez voir par les résultats affichés que, par rapport à la sortie de l'exemple de tableau à deux dimensions représenté dans la figure 51, la forme des données est irrégulière (inégale). C'est pourquoi cette structure de données est appelée un tableau irrégulier.

Vous pouvez regarder la vidéo YouTube ci-dessous pour plus d'informations sur les tableaux en C#, ainsi que plus d'exemples de code sur la façon dont les tableaux sont utilisés dans le code C#.

%[https://youtu.be/K4wjL7kRJyE]

## Méthodes C#

### Introduction aux méthodes en C#

Une méthode est simplement un bloc de code qui contient une série d'instructions. Lorsqu'un programme est exécuté et qu'une méthode est appelée, les instructions de cette méthode sont exécutées.

En C#, chaque instruction est exécutée dans le contexte d'une méthode. Ainsi, les méthodes sont fondamentales pour la structure et l'exécution du code C#.

### La méthode Main

La méthode `Main` est le point d'entrée de toutes les applications C#. Ainsi, c'est la méthode qui est exécutée en premier chaque fois qu'un programme codé en C# est exécuté.

Le CLR (Common Language Runtime) appelle la méthode `Main` lorsqu'un programme (codé en C#) est démarré pour la première fois. En C#, vous pouvez créer à la fois des méthodes nommées et des méthodes anonymes. Dans cette partie du livre C#, nous discuterons des méthodes nommées.

### La structure des méthodes

Les méthodes sont utilisées pour encapsuler une série d'instructions qui sont exécutées lorsque la méthode est appelée dans le code. Dans certains cas, une méthode est simplement une série d'instructions où (à l'exécution) les instructions sont exécutées en séquence et aucune valeur n'est retournée de la méthode pertinente au code appelant.

Ces méthodes (qui ne retournent pas de valeur) contiennent le mot-clé `void` dans la déclaration de méthode pertinente pour signifier que la méthode ne retourne pas de valeur.

Les méthodes peuvent également être créées pour contenir une liste d'instructions qui sont exécutées séquentiellement. À la fin de la liste d'instructions, une valeur d'un type de données spécifié est retournée au code appelant.

Pour les méthodes qui retournent des valeurs, le type de données indiquant la valeur qui doit être retournée par la méthode est inclus de manière appropriée dans la déclaration de la méthode. À la fin de la séquence d'instructions encapsulée par la méthode, le mot-clé `return` est inclus, suivi de la valeur qui sera retournée au code appelant, sur la même ligne où le mot-clé `return` est inclus.

Vous pouvez voir un exemple simple d'une méthode utilisée pour retourner le résultat d'une opération mathématique dans la figure 54.

Figure 54.

```csharp
int result = AddTwoNumbers(2, 3);
Console.WriteLine(result);
int result2 = AddTwoNumbers(300, 400);
Console.WriteLine(result2);

```

Dans l'exemple ci-dessus, cette méthode simple a une déclaration de méthode qui contient un modificateur d'accès `private`. Cela signifie que la méthode `AddTwoNumbers` n'est accessible qu'à partir des méthodes contenues dans la même classe où réside la méthode `AddTwoNumbers`.

La méthode `AddTwoNumbers` retourne une valeur qui est de type entier. Cela est indiqué par l'alias `int` utilisé dans la déclaration de la méthode.

La déclaration de la méthode contient deux paramètres, tous deux du type de données entier. La première ligne de code dans la méthode exécute l'opération mathématique d'addition entre deux arguments qui sont passés de manière appropriée aux paramètres de la méthode à l'exécution. La deuxième ligne de code dans la méthode utilise le mot-clé `return` de C# suivi du résultat de l'instruction précédente, pour retourner le résultat de l'opération mathématique pertinente au code appelant.

Le mot-clé `return` indique le retour d'une valeur au code appelant, qui dans ce cas sera le résultat de l'opération mathématique exécutée dans la première ligne de code dans la méthode `AddTwoNumbers`.

Dans l'exemple ci-dessous (représenté dans la figure 55), deux instructions sont contenues dans la méthode. Une différence fondamentale entre la méthode `AddTwoNumbers` (représentée dans la figure 54) et la méthode ci-dessous (représentée dans la figure 55) est que la méthode `LogFormulaResultToFile` (représentée dans la figure 55) ne retourne pas de valeur. Cela est indiqué par le mot-clé `void` qui est inclus dans la déclaration de la méthode `LogFormulaResultToFile`.

Figure 55.

```csharp
LogFormulaResultToFile(3, 4, "This is the result: ");

// Output:
// This is the result:  7

void LogFormulaResultToFile(int operand1, int operand2, string message)
{
    int result = operand1 + operand2;
    LogToFile($"{message} {result}");
}

void LogToFile(string message)
{
    Console.WriteLine(message); // pour simplifier, imprimer le message à l'écran plutôt que d'écrire dans un fichier
}

```

La structure fondamentale de chaque méthode en C# est définie par sa signature de méthode. Et nous avons discuté que dans les méthodes se trouve une série d'instructions.

La signature de la méthode définit quel type de valeur est retourné par la méthode, le nom de la méthode et le niveau d'accès (ou la portée) associé à la méthode (par exemple, `private` ou `public`). La signature de la méthode inclut également zéro, un ou une liste de paramètres désignant les arguments qui peuvent être passés à la méthode lorsque la méthode est appelée à l'exécution. La signature de la méthode peut également contenir les mots-clés suivants, `abstract`, `sealed`, ou `virtual`. Ces mots-clés sont hors du cadre de ce manuel.

Les méthodes sont déclarées dans une `class`, `struct` ou `interface`. Les méthodes dans une `interface` ne contiennent aucune implémentation (c'est-à-dire aucune instruction) et seule la signature de la méthode est définie dans une `interface`.

Notez que les méthodes définies dans une `interface` n'incluent pas de modificateurs d'accès. Lorsqu'une `class` implémente une `interface`, les méthodes contenues dans l'`interface` doivent être implémentées de manière appropriée par la `class` qui implémente l'`interface`.

D'autre part, lorsque les méthodes sont contenues dans une `class` ou une `struct`, les signatures de méthode et les implémentations de code pour les méthodes sont incluses.

L'exemple ci-dessous (représenté dans la figure 56) démontre l'implémentation d'une méthode `public` qui peut être utilisée pour retourner la factorielle d'un nombre.

Figure 56.

```csharp
MathFunctions mathFunctions = new MathFunctions();
var result = mathFunctions.GetFactorial(6);
Console.WriteLine(result);

// Output:
// 720
public class MathFunctions
{
    public int GetFactorial(int num)
    {
        int fact = 1;
        for (int i = 1; i <= num; i++)
        {
            fact = fact * i;
        }
        return fact;
    }
}

```

Dans la méthode `public` nommée `GetFactorial`, une variable locale est déclarée et initialisée à une valeur de `1` en haut de la méthode.

Une variable locale est une variable qui a une portée locale, ce qui signifie que dans ce cas, la variable `fact` n'est pas accessible en dehors de la méthode `GetFactorial`. Elle n'est accessible qu'à l'intérieur de la méthode `GetFactorial`. Cela signifie que la valeur de la variable `fact` ne peut pas être modifiée depuis l'extérieur de la méthode mais ne peut être modifiée que depuis l'intérieur de la méthode.

Vous pouvez voir qu'à l'intérieur de la boucle `for`, une instruction est exécutée qui modifie la valeur de la variable `fact` à chaque itération de la boucle. Une fois la boucle terminée, un résultat final est atteint et ce résultat est retourné (en utilisant le mot-clé `return` de C#) au code appelant.

Si, par exemple, la méthode `GetFactorial` réside dans une classe nommée `MathFunctions`, le code appelant pourrait ressembler à l'exemple ci-dessous représenté dans la figure 57.

Figure 57.

```csharp

MathFunctions mathFunctions = new MathFunctions();
var result = mathFunctions.GetFactorial(6);
Console.WriteLine(result);

```

Ci-dessous, vous verrez un exemple d'une méthode `private` qui utilise la manipulation de chaînes de caractères C# pour concaténer et reformater de manière appropriée les arguments de chaîne représentant le prénom et le nom de famille d'un employé (représenté dans la figure 58).

Ainsi, si le prénom de l'employé est "John" et le nom de famille de l'employé est "Denver", la méthode pertinente retournera la valeur de chaîne "Denver, J". La méthode concatène le nom de famille avec une virgule suivie d'une autre concaténation de l'initiale du prénom de l'employé.

Cette opération de concaténation est présentée par le mot-clé `return` sur la même ligne, ce qui signifie que le résultat de l'opération de concaténation est retourné au code appelant.

Figure 58.

```csharp
private string FormatName(string firstName, string lastName)
{
    return lastName + ", " + firstName.Substring(0, 1).ToUpper();
}
```

Dans la figure 59 ci-dessous, nous avons un exemple de code où une classe nommée `Employee` est incluse. Cette classe contient une propriété en lecture seule nommée `DisplayName`. Cette propriété expose le nom formaté à l'appelant via le modificateur d'accès `public`.

Les arguments de chaîne `firstName` et `lastName` sont passés au constructeur de la classe `Employee` lorsqu'elle est instanciée par le code appelant. Le code appelant peut ensuite écrire le nom formaté de l'employé pertinent sur l'écran de la console. Ainsi, la méthode `private` `FormatName` n'est pas accessible au code appelant. Le formatage du nom de l'employé est géré au sein de la classe `Employee`.

Ceci est une décision de conception motivée par les exigences.

Figure 59.

```csharp
public class Employee
{
    private string firstName = "";
    private string lastName = "";

    public Employee(string firstName, string lastName)
    {
        this.firstName = firstName;
        this.lastName = lastName;
    }

    public string DisplayName
    {
        get { return FormatName(this.firstName, this.lastName); }
    }

    private string FormatName(string firstName, string lastName)
    {
        return lastName + ", " + firstName.Substring(0, 1).ToUpper();
    }
}

```

Le code appelant pourrait ressembler à l'exemple de code représenté dans la figure 60 :

Figure 60.

```csharp
Employee employee = new Employee("John", "Denver");
Console.WriteLine(employee.DisplayName);
// Output:
// Denver, J

```

L'exemple de code représenté dans la figure 59 démontre l'utilisation du concept de conception de code d'encapsulation. La complexité de la fonctionnalité `FormatName` est encapsulée dans une méthode `private` dans la classe `Employee` afin que le code appelant ne soit pas concerné par le détail d'implémentation de la fonctionnalité de formatage du nom de l'employé. Le code appelant n'a besoin que de référencer la propriété `DisplayName` sur un objet dérivé du type défini par l'utilisateur `Employee` (ou classe). La fonctionnalité de formatage est gérée au sein de la classe `Employee`.

Le modificateur d'accès `private` impose l'encapsulation de la fonctionnalité de formatage. La méthode `FormatName` n'est pas accessible depuis le code appelant, mais n'est accessible que depuis la classe `Employee`.

Cette décision de conception particulière est imposée par l'utilisation du modificateur d'accès `private` contenu de manière appropriée dans la déclaration de la méthode `FormatName`.

## Classes C#

C# prend en charge la programmation orientée objet. Tous les types de données, y compris les types définis par l'utilisateur en C#, héritent du type de données `object`, donc on pourrait dire que tout en C# est un objet. Ainsi, un `int` est un objet, un `decimal` est un objet, un `string` est un objet, un `bool` est un objet, etc.

La principale différence entre un `int`, un `decimal` et un `bool` par rapport à un type de données `string` est que les types de données `int`, `decimal` et `bool` héritent de la classe abstraite ValueType, la classe ValueType hérite à son tour du type `object`. Cela signifie que les types de données `int`, `decimal` et `bool` sont des types de valeur. Les chaînes, en revanche, sont des types de référence. Le type de données `string` n'hérite pas de la classe abstraite ValueType mais hérite directement de la classe `System.Object`.

Notez que les types de données `int`, `bool` et `decimal` sont implémentés sous forme de structs en C#. Les structs sont des types de valeur et sont similaires aux classes à bien des égards.

La principale différence entre une struct et une classe en C# est que les structs sont des types de valeur et les classes sont des types de référence. Le type de données `string` hérite directement du type `System.Object`, ce qui signifie que le type de données `string` est un type de référence.

En C#, vous êtes en mesure de créer vos propres classes personnalisées. Lorsque vous créez une classe en C#, en coulisses, votre type défini par l'utilisateur hérite du type `System.Object`. Ainsi, votre classe définie par l'utilisateur est un type de référence.

Notez que vous pouvez également créer des structs définis par l'utilisateur en utilisant le mot-clé `struct`, tandis que lorsque vous créez des classes définies par l'utilisateur, vous utilisez le mot-clé `class`.

La différence sous-jacente entre une classe et une struct est la manière dont elles sont stockées en mémoire. Les types de valeur stockent leurs données directement dans un emplacement mémoire appelé la pile, tandis que les types de référence stockent une référence numérique (adresse mémoire) sur la pile, vers un objet contenant les données réelles (où les données sont réellement stockées) appelé le tas.

La pile stocke les données de manière plus structurée que la manière dont les données sont stockées sur le tas. Assurez-vous de comprendre cette différence, car elle affecte la manière dont les objets dérivés de classes ou de structs sont copiés et passés dans le code, et l'efficacité avec laquelle les données sont stockées et récupérées en mémoire.

Les structs sont généralement plus rapides que les classes, donc si vous travaillez avec de grandes quantités de données, les structs peuvent être une option plus efficace car ils ne nécessitent pas la surcharge de la mémoire du tas. Les structs peuvent être la meilleure option lorsque vous avez besoin de représenter une structure de données simple qui contient des types de données comme des entiers, des booléens ou des décimaux.

Les structs ont également l'avantage d'être gérés plus efficacement en mémoire, ce qui signifie que lorsque vous traitez de grandes quantités d'objets instanciés à partir d'une structure de données particulière, une struct peut être une meilleure option pour représenter ces données, plutôt qu'une classe.

Les structs et les classes sont similaires en ce sens qu'ils prennent en charge des concepts comme, par exemple, les constructeurs, les champs, les propriétés et les méthodes.

Dans la figure 61, la classe `Player` est utilisée comme modèle pour un objet qui représente un objet de jeu pour un jeu particulier.

Figure 61

```csharp
public class Player
{
    private string name = "";

    public Player(string name)
    {
        this.name = name;
    }

    public void Move(double x, double y)
    {
        Console.WriteLine($"Moving {name} to coordinates where 'x' = {x}, and 'y' = {y}");
    }
}

```

Dans l'exemple ci-dessus (représenté dans la figure 61), vous pouvez voir certains des concepts fondamentaux en C# être exprimés, par exemple à travers l'utilisation du mot-clé `class`, des modificateurs d'accès `private` et public, un constructeur qui contient un paramètre, une méthode qui contient deux paramètres et une variable membre privée définie comme une chaîne.

### Le mot-clé 'class'

Le mot-clé class en C# est utilisé pour définir un type de référence défini par l'utilisateur ou une classe.

### Le modificateur d'accès public

Précédant le mot-clé `class` se trouve le modificateur d'accès `public`. L'utilisation du modificateur d'accès `public` de cette manière signifie que cette classe peut être accessible et instanciée depuis n'importe où dans l'assembly où la classe réside ainsi que depuis l'extérieur de l'assembly où la classe réside.

### La variable membre privée

La variable membre `private` nommée `name` n'est pas directement accessible au code qui existe en dehors de la classe `Player`. La variable membre `name` ne peut être accessible et utilisée qu'à partir d'une propriété, d'un constructeur ou d'une méthode qui réside dans la classe `Player`.

### Le constructeur

La classe `Player` (représentée dans l'exemple de code de la figure 61) a un constructeur. Les classes sont instanciées en objets à l'exécution. Le constructeur Player contient un paramètre de chaîne nommé `name`. Lorsque le code appelant instancie un objet dérivé de la classe `Player`, le nom du `Player` peut être passé comme argument au constructeur de l'objet Player.

Dans le constructeur de la classe 'Player', la variable membre privée nommée `name` est assignée à la valeur passée par le code appelant au constructeur paramétré de la classe 'Player'. Lorsque le code appelant appelle ensuite la méthode `Move`, la variable membre `name` est accessible et utilisée par le code dans la méthode `Move`. Le constructeur est appelé lorsque l'objet est dérivé de la classe `Player`.

Le constructeur permet au code appelant d'assigner une valeur pour le nom du joueur concernant l'objet pertinent au moment où l'objet pertinent est instancié.

### La méthode Move

Une fois que le code appelant a instancié un objet à partir de la classe `Player`, le code appelant est en mesure d'exécuter le code dans la méthode Move en appelant de manière appropriée la méthode `Move` sur l'objet pertinent.

La méthode `Move` est accessible au code depuis l'extérieur de la classe dans laquelle elle réside car elle a un modificateur d'accès `public`. Si la méthode avait, par exemple, un modificateur d'accès privé, cette méthode ne serait accessible qu'à partir de la classe dans laquelle elle réside.

Lorsque la méthode `Move` est exécutée par le code appelant, deux arguments de type `double` doivent être passés dans la méthode move car la méthode `Move` contient deux paramètres de type `double`.

Ci-dessous (dans la figure 62) se trouve un exemple de code appelant instanciant un objet à partir de la classe `Player` et appelant ensuite la méthode Move sur l'objet joueur instancié pertinent.

Figure 62.

```csharp
Player player = new Player("Bob");
player.Move(10.54, 18.43);

```

Pour plus d'informations sur les classes C#, veuillez consulter la vidéo ci-dessous :

%[https://youtu.be/6rlUl5T2Sck]

Et ci-dessous, vous pouvez trouver une série vidéo complète sur les classes C# :

[Série vidéo complète sur les classes C#](https://www.youtube.com/watch?v=6rlUl5T2Sck&list=PL4LFuHwItvKY76WTDhfGAwrpLZaSxF9fS)

## Structs C#

Le mot-clé `struct` est utilisé pour définir une structure de données en C# qui est un type de valeur. Les structs sont similaires aux classes à bien des égards – par exemple, vous pouvez utiliser à la fois des structs et des classes pour représenter des structures de données qui peuvent contenir des membres de données et des fonctionnalités comportementales connexes exprimées dans des méthodes.

### Différences clés entre une classe et une struct.

* La principale différence est qu'une classe est un type de référence et une struct est un type de valeur. Les structs héritent implicitement de la classe abstraite `System.ValueType` (qui à son tour hérite de la classe `System.Object`), tandis que les types de référence héritent directement du type `System.Object`.
* Une struct est un meilleur choix qu'une classe pour représenter des structures de données qui stockent de petites quantités de données. Une autre bonne raison d'utiliser une struct est si vous devez stocker de petites quantités de données dans la structure de données pertinente et où un grand nombre d'objets dérivés de la struct pertinente sont traités dans le code.
* Vous pouvez instancier un objet à partir d'une struct en utilisant le mot-clé `new` tout comme vous le feriez lors de l'instanciation d'un objet à partir d'une classe. Mais le mot-clé `new` n'est pas requis lors de la déclaration et de l'initialisation d'une struct avant de pouvoir l'utiliser dans le code.
* En C#, certaines primitives de type de valeur sont représentées sous forme de structs, par exemple l'alias `int` représente la struct `System.Int32`, l'alias `bool` représente la struct `System.Bool`, et l'alias `float` représente la struct `System.Single`.

### Utiliser une struct dans le code

Ci-dessous (représenté dans la figure 63) se trouve un exemple de code qui utilise une struct pour stocker les spécifications d'un motif. Le motif est désigné par un cercle qui est dessiné dans un carré.

Le champ `Radius` stocke la valeur qui désigne le rayon du cercle, qui détermine également la taille du carré. Le champ `InnerSymbol` désigne la valeur `char` imprimée à l'écran qui est utilisée pour représenter le cercle intérieur. Le champ `OuterSymbol` désigne la valeur `char` imprimée à l'écran qui est utilisée pour représenter le carré extérieur dans le motif global.

Figure 63.

```csharp
Console.WriteLine("Please enter the radius of the circle");
double radius = Convert.ToDouble(Console.ReadLine());

CircleInSquare circleInSquare;
circleInSquare.Radius = radius;
circleInSquare.InnerSymbol = '0';
circleInSquare.OuterSymbol = '1';
circleInSquare.Draw();

//Output

// 11111111111111111111111111111111111111111
// 11111111111111000000000000011111111111111
// 11111111110000000000000000000001111111111
// 11111111000000000000000000000000011111111
// 11111100000000000000000000000000000111111
// 11110000000000000000000000000000000001111
// 11100000000000000000000000000000000000111
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11000000000000000000000000000000000000011
// 11100000000000000000000000000000000000111
// 11110000000000000000000000000000000001111
// 11111100000000000000000000000000000111111
// 11111111000000000000000000000000011111111
// 11111111110000000000000000000001111111111
// 11111111111111000000000000011111111111111
// 11111111111111111111111111111111111111111
public struct CircleInSquare
{
    public double Radius;
    public char InnerSymbol;
    public char OuterSymbol;

    public CircleInSquare(double radius, char innerSymbol, char outerSymbol)
    {
        Radius = radius;
        InnerSymbol = innerSymbol;
        OuterSymbol = outerSymbol;
    }

    public void WriteMemberValuesToScreen()
    {
        Console.WriteLine(
            $"Radius = {Radius}, InnerSymbol = '{InnerSymbol}', OuterSymbol = '{OuterSymbol}'"
        );
    }

    public void Draw()
    {
        double radiusInner = Radius - 0.5;
        double radiusOuter = Radius + 0.5;

        Console.WriteLine();

        for (double y = Radius; y >= -Radius; --y)
        {
            for (double x = -Radius; x < radiusOuter; x += 0.5)
            {
                double value = x * x + y * y;

                if (value >= radiusInner * radiusInner)
                {
                    Console.Write(OuterSymbol);
                    System.Threading.Thread.Sleep(50);
                }
                else
                {
                    Console.Write(InnerSymbol);
                }
            }
            Console.WriteLine();
        }
    }
}

```

Notez que, comme démontré dans l'exemple ci-dessus (dans la figure 63), le mot-clé `new` n'a pas besoin d'être utilisé lors de l'instanciation d'un objet à partir d'une struct en C#.

Une struct est une structure de données en C# idéale pour stocker une petite quantité de valeurs, par exemple celles nécessaires pour les objets dérivés de la struct `CircleInSquare`.

Comme discuté ci-dessus, les structs sont des types de valeur en C#, ce qui signifie qu'ils sont gérés plus efficacement en mémoire, où les données pertinentes sont stockées en mémoire sur la pile. Si vous deviez stocker un nombre suffisamment grand d'instances d'objets dérivés de la struct `CircleInSquare` dans une collection, c'est là qu'un avantage de performance pourrait être notablement gagné par rapport à un scénario où des instances d'objets dérivés d'une version de classe du modèle `CircleInSquare` sont stockées dans une collection.

Ainsi, par exemple, dans un jeu où peut-être des informations vectorielles doivent être stockées dans une grande collection pour représenter la position d'un objet `player`, vous pourriez utiliser une struct pour représenter les données plutôt qu'une classe. Cela aiderait à gérer les données plus efficacement en mémoire, ce qui apporte également un avantage de performance en termes d'exécution du code.

%[https://youtu.be/NVKGxzuBe8c]

## Enums et instructions switch

### Introduction aux enums

En C#, un enum, abréviation de enumeration, est un type de valeur que vous pouvez utiliser pour définir un ensemble de constantes intégrales nommées. Les enums sont utilisés pour créer des noms lisibles par l'homme pour un ensemble de valeurs liées et uniques, rendant le code plus lisible.

### Utiliser un enum dans le code

Pour déclarer un enum, vous utilisez le mot-clé `enum` de C#. Dans la figure 64 se trouve un exemple de code démontrant l'utilisation d'un enum. Vous pouvez voir que les mois de l'année sont représentés par un enum nommé `MonthOfYear`. Chacun des douze membres de l'enum `MonthOfYear` représente un mois unique de l'année. La valeur entière associée à chaque mois est ordonnée par ordre croissant selon l'ordre chronologique dans lequel ils se produisent pour une année civile.

Ainsi, `Jan` se voit attribuer la valeur `1`, `Feb` se voit attribuer la valeur `2`, `Mar` se voit attribuer la valeur `3` et ainsi de suite, jusqu'au dernier mois `Dec`, auquel est attribuée la valeur `12` (le douzième et dernier mois de l'année civile).

Une méthode simple nommée `OutputMonthMainFocus` reçoit une valeur d'enum afin d'afficher un récit approprié à l'utilisateur qui affiche le focus de l'utilisateur pour l'argument de mois passé.

Figure 64.

```csharp
OutputMonthMainFocus("Focus for Jan:", MonthOfYear.Jan);
OutputMonthMainFocus("Focus for Mar:", MonthOfYear.Mar);
OutputMonthMainFocus("Focus for Dec:", MonthOfYear.Dec);

// Output:
// Focus.for Jan: Health and fitness
// Focus.for Mar: Increase knowledge of calculus
// Focus for Dec: Spend more time with friends and family
void OutputMonthMainFocus(string prependedText, MonthOfYear month)
{
    switch (month)
    {
        case MonthOfYear.Jan:
            Console.WriteLine($"{prependedText} Health and fitness");
            break;
        case MonthOfYear.Feb:
            Console.WriteLine($"{prependedText} Learn Spanish");
            break;
        case MonthOfYear.Mar:
            Console.WriteLine($"{prependedText} Increase knowledge of calculus");
            break;
        case MonthOfYear.Apr:
            Console.WriteLine($"{prependedText} Getting up earlier");
            break;
        case MonthOfYear.May:
            Console.WriteLine($"{prependedText} Better work organisation");
            break;
        case MonthOfYear.Jun:
            Console.WriteLine($"{prependedText} Volunteer work");
            break;
        case MonthOfYear.Jul:
            Console.WriteLine($"{prependedText} Eating more vegetables");
            break;
        case MonthOfYear.Aug:
            Console.WriteLine($"{prependedText} Travel to London");
            break;
        case MonthOfYear.Sep:
            Console.WriteLine($"{prependedText} Learning to cook better");
            break;
        case MonthOfYear.Oct:
            Console.WriteLine($"{prependedText} Learn to. surf");
            break;
        case MonthOfYear.Nov:
            Console.WriteLine($"{prependedText} Be more productive");
            break;
        case MonthOfYear.Dec:
            Console.WriteLine($"{prependedText} Spend more time with friends and family");
            break;
        default:
            throw new ArgumentException("Invalid Month");
    }
}

```

### Utiliser une instruction switch dans le code avec un enum

Vous pouvez voir que l'instruction `switch` ci-dessus représentée dans la figure 64 est similaire à une instruction `if/else`.

En haut de l'instruction `switch` se trouve le code contenant le mot-clé `switch`. Dans les parenthèses suivant le mot-clé `switch` se trouve la valeur que l'opération `switch` compare à une série de valeurs qui sont désignées par chaque instruction `case` qui est encapsulée dans le bloc de code `switch`.

Chaque section `case` compare la valeur dans les parenthèses suivant le mot-clé `switch` à une valeur suivant chaque mot-clé `case`. Lorsqu'une correspondance entre la valeur dans les parenthèses suivant le mot-clé `switch` et une valeur suivant l'un des mots-clés `case` est trouvée, la liste d'instructions dans la section de cas correspondante est exécutée.

Par exemple, lorsque la première ligne du code appelant (c'est-à-dire le code qui appelle la méthode `OutputMonthMainFocus`) est appelée, l'instruction de la première section de cas est exécutée. Cela est dû au fait que `Month.Jan` est passé en argument à la méthode `OutputMonthMainFocus` et que `Month.Jan` correspond à la valeur suivant le mot-clé `case` dans la première section `case`.

Notez qu'un mot-clé `break` ou un mot-clé `return` (si approprié) doit être inclus comme dernière instruction de la liste d'instructions de chaque section de cas.

Chaque section de cas est mutuellement exclusive. Cela signifie que dans l'exemple de code représenté dans la figure 64 où un mot-clé `break` est inclus comme dernière instruction dans chaque section `case`, lorsqu'une correspondance se produit, seules les instructions dans cette section `case` correspondante sont exécutées. Une fois les instructions dans cette instruction `case` exécutées, le code sort du bloc de code `switch`. Si un code se trouve en dessous du bloc de code `switch`, ce code sera ensuite exécuté. Aucun autre code dans cette instruction `switch` ne sera exécuté après qu'une correspondance se produise.

Si aucune correspondance n'est trouvée dans les instructions `case`, le code dans la section `default` est exécuté.

Vous pouvez voir dans l'exemple de la figure 64 que le code lance une `ArgumentException` si aucune des valeurs dans les instructions `case` pertinentes ne correspond à la valeur passée dans l'instruction `switch`.

### Associer un bloc de code à plus d'un cas

Vous pourriez modifier l'instruction `switch` comme le montre la figure 65, de sorte que plus d'une instruction de cas soit associée à un bloc de code (ou des lignes de code). Ainsi, si, par exemple, `Month.Jan` était passé dans l'instruction `switch`, les instructions de code dans la section de cas `Month.Mar` s'exécuteraient.

Les mêmes lignes de code dans la section de cas `Month.Mar` s'exécuteraient également lorsque `Month.Feb` ou `Month.Mar` sont passés en arguments à l'instruction `switch`. Cela se produit parce qu'il n'y a pas de lignes de code incluses dans la section de cas `Month.Jan` et qu'il n'y a pas de lignes de code incluses dans la section de cas `Month.Feb`. Ainsi, si les sections `Month.Jan` ou `Month.Feb` ne sont pas correspondantes, le code passe à la section de cas `Month.Mar` et les lignes de code dans la section de cas `Month.Mar` sont exécutées.

Bien sûr, les lignes de code dans la section `Month.Mar` s'exécuteront également si la section de cas `Month.Mar` est correspondante. Ainsi, la logique pour cela est la même que l'instruction `if` représentée dans la figure 64b.

Figure 64b.

```csharp
MonthOfYear month = MonthOfYear.Feb;
string prependedText = "Focus for Feb";
if (month == MonthOfYear.Jan || month == MonthOfYear.Feb || month == MonthOfYear.Mar)
{
    Console.WriteLine($"{prependedText} Health and fitness");
    Console.WriteLine($"{prependedText} Learn Spanish");
    Console.WriteLine($"{prependedText} Increase knowledge of calculus");
}

```

Figure 65.

```csharp
OutputMonthMainFocus("Focus for Jan:", MonthOfYear.Jan);
OutputMonthMainFocus("Focus for Mar:", MonthOfYear.Feb);
OutputMonthMainFocus("Focus for Dec:", MonthOfYear.Mar);

// Output:
// Focus for Jan: Health and fitness
// Focus for Jan: Learn Spanish
// Focus for Jan: Increase knowledge of calculus
// Focus for Mar: Health and fitness
// Focus for Mar: Learn Spanish
// Focus for Mar: Increase knowledge of calculus
// Focus for Dec: Health and fitness
// Focus for Dec: Learn Spanish
// Focus for Dec: Increase knowledge of calculus
void OutputMonthMainFocus(string prependedText, MonthOfYear month)
{
    switch (month)
    {
        case MonthOfYear.Jan:
        case MonthOfYear.Feb:
        case MonthOfYear.Mar:
            Console.WriteLine($"{prependedText} Health and fitness");
            Console.WriteLine($"{prependedText} Learn Spanish");
            Console.WriteLine($"{prependedText} Increase knowledge of calculus");
            break;
        case MonthOfYear.Apr:
            Console.WriteLine($"{prependedText} Getting up earlier");
            break;
        case MonthOfYear.May:
            Console.WriteLine($"{prependedText} Better work organisation");
            break;
        case MonthOfYear.Jun:
            Console.WriteLine($"{prependedText} Volunteer work");
            break;
        case MonthOfYear.Jul:
            Console.WriteLine($"{prependedText} Eating more vegetables");
            break;
        case MonthOfYear.Aug:
            Console.WriteLine($"{prependedText} Travel to London");
            break;
        case MonthOfYear.Sep:
            Console.WriteLine($"{prependedText} Learning to cook better");
            break;
        case MonthOfYear.Oct:
            Console.WriteLine($"{prependedText} Learn to. surf");
            break;
        case MonthOfYear.Nov:
            Console.WriteLine($"{prependedText} Be more productive");
            break;
        case MonthOfYear.Dec:
            Console.WriteLine($"{prependedText} Spend more time with friends and family");
            break;
        default:
            throw new ArgumentException("Invalid Month");
    }
}

```

### Utiliser des chaînes de caractères dans les instructions switch

L'exemple représenté dans la figure 64 traite spécifiquement de la liste de valeurs dans un type enum. Vous pouvez également, bien sûr, utiliser une instruction `switch` pour évaluer les valeurs de n'importe quel type de données C#.

Par exemple, dans la figure 66, des valeurs du type de données chaîne de caractères sont évaluées au lieu des valeurs numériques contenues dans un enum. Figure 66.

```csharp
OutputMonthMainFocus("Focus for Jan:", "JAN");
OutputMonthMainFocus("Focus for Mar:", "MAR");
OutputMonthMainFocus("Focus for Dec:", "DEC");
// Output:
// Focus for Jan: Health and fitness
// Focus for Mar: Increase knowledge of calculus
// Focus for Dec: Spend more time with friends and family

```

Notez que vous pouvez utiliser la logique conditionnelle `if/else if/else` lorsque cela est approprié afin de remplacer une instruction `switch`, cependant il est préférable d'utiliser une instruction `switch` lorsqu'il y a un grand nombre de conditions logiques à évaluer. Cela est dû au fait qu'une instruction `switch` est plus lisible dans ce scénario.

Vous pouvez regarder les vidéos YouTube ci-dessous pour en savoir plus sur les instructions switch et les enums.

%[https://youtu.be/XTDEYQUymt8]

%[https://youtu.be/1248C0V_yHs]

## Héritage en C#

C# est un langage de programmation orienté objet. Les principes de la programmation orientée objet sont l'encapsulation, l'héritage, le polymorphisme et l'abstraction.

L'héritage est le fait qu'une classe est basée sur une autre classe. Il est important de noter que l'héritage multiple n'est pas autorisé en C#. Une classe en C# peut hériter de plusieurs interfaces mais pas de plusieurs classes à la fois. Nous discuterons des interfaces dans la prochaine section de ce manuel ainsi que du principe d'abstraction.

Ainsi, si, par exemple, la classe `ManagingDirector` est basée sur la classe `Manager`, qui à son tour est basée sur la classe `Employee`, en C# vous ne pouvez pas implémenter le code comme dans l'exemple ci-dessous (dans la figure 67) afin d'exprimer cette hiérarchie d'héritage.

Figure 67.

```csharp
public class ManagingDirector : Manager, Employee
{
    // code goes here
}

```

En C++, ce type d'héritage multiple est autorisé. Mais en C#, seul l'héritage simple est autorisé.

En C#, vous êtes cependant toujours en mesure d'exprimer que la classe `ManagingDirector` hérite de la classe `Manager` qui à son tour hérite de la classe `Employee` – mais vous devez le faire d'une manière spécifique.

L'exemple ci-dessous (dans la figure 68) montre comment cette hiérarchie d'héritage spécifique peut être exprimée en C#.

Figure 68.

```csharp
public class Manager:Employee
{
	// code goes here
} 
public ManagingDirector:Manager
{	
	// code goes here
}

```

Ainsi, C# ne prend en charge que l'héritage simple pour les classes, mais vous pouvez obtenir un héritage multiple en implémentant du code d'une certaine manière en C#. L'exemple ci-dessus (dans la figure 68) vous montre comment faire.

## Abstraction en C#

L'abstraction est un autre principe de la programmation orientée objet. C'est un concept qui est souvent confondu avec un autre des principes de la programmation orientée objet, à savoir l'encapsulation.

L'abstraction peut être définie comme l'inclusion de code lié à la conception essentiel mais aucun détail d'implémentation. Le détail d'implémentation est désigné par les lignes de code dans une méthode, et l'abstraction de cette méthode est la signature de la méthode.

Dans l'exemple simplifié ci-dessous (dans la figure 69), vous pouvez voir une méthode nommée `LogData` qui est responsable soit d'imprimer des données à l'écran de la console, soit d'imprimer des données dans un fichier local prédéfini.

Figure 69

```csharp
public void LogData(string data)
{
	LogToScreen(data);
}

```

L'abstraction de cette méthode serait la signature de la méthode qui pourrait être représentée à l'intérieur d'une interface comme dans l'exemple ci-dessous représenté dans la figure 70 :

Figure 70.

```csharp
public interface ILogging
{
    void LogData(string data);
}

```

La méthode `LogData` pourrait résider à l'intérieur d'une classe nommée `Logging` qui implémente l'interface `ILogging`. Lorsqu'une classe implémente une interface en C#, cela signifie que la classe doit contenir et implémenter toutes les méthodes qui sont définies à l'intérieur de l'interface pertinente.

Voir ci-dessous (dans la figure 71) un exemple de la classe `Logging` implémentant l'interface `ILogging`.

Figure 71

```csharp
public class Logging : ILogging
{
    public void LogData(string data)
    {
        LogToScreen(data);
    }
}

```

L'interface `ILogging` peut être décrite comme une abstraction de la classe `Logging`. En C#, le code appelant n'a pas besoin de connaître (pour ainsi dire) le code d'implémentation de la méthode `LogData`. Le code appelant n'a besoin de connaître que la définition de type. La définition de type est l'abstraction de la classe `Logging`.

Dans l'exemple ci-dessous (dans la figure 72), vous pouvez voir un exemple de code appelant instanciant un objet à partir du type défini par l'utilisateur `Logging`. Remarquez comment la définition de type peut être implémentée en utilisant l'interface `ILogging`. Cela signifie que le code appelant connaîtra la méthode `LogData` au moment de la compilation, mais ne saura rien de son implémentation.

Figure 72.

```csharp
ILogging logging = new Logging();
logging.LogData("Data to be logged.");

```

Maintenant, vous pourriez créer de nombreuses classes de journalisation avec différentes implémentations de la méthode `LogData`.

Par exemple, actuellement, la classe `Logging` contient une implémentation de la méthode `LogData` qui journalise les données à l'écran de la console. Supposons qu'une exigence émerge où vous souhaitez journaliser les données dans un fichier prédéfini. Pour ce faire, vous pourriez simplement créer une nouvelle classe qui implémente l'interface `ILogging`, où le code dans la nouvelle classe contient du code qui journalise les données pertinentes dans un fichier prédéfini.

L'exemple ci-dessous (dans la figure 73) représente la nouvelle classe. Pour simplifier, nommons cette classe `Logging2`.

Figure 73.

```csharp
public class Logging2 : ILogging
{
    public void LogData(string data)
    {
        LogToFile(data);
    }
}
// Calling code
ILogging logging = new Logging2();
logging.LogData("Data to be logged.");

```

Le code appelant qui implémente la méthode `LogData` dans la classe `Logging` ressemblerait beaucoup à lorsque la méthode `LogData` est appelée sur un objet instancié à partir de la classe `Logging2`.

En fait, vous pourriez abstraire l'instanciation de l'objet `logging` pertinent dans sa propre classe de fabrique comme vous le voyez ci-dessous dans la figure 74. Ainsi, grâce à l'utilisation d'une interface, nous sommes en mesure d'abstraire davantage notre code, en abstraisant le processus d'instanciation des classes de journalisation.

Figure 74.

```csharp
public static class LoggingFactory
{
    public static ILogging GetLoggingObject(bool toScreen)
    {
        if (toScreen)
        {
            return new Logging();
        }
        else
        {
            return new Logging2();
        }
    }
}

```

Le code appelant pourrait maintenant être implémenté comme le montre la figure 75 ci-dessous.

Figure 75.

```csharp
ILogging logging = LoggingFactory.GetLoggingObject(true);
logging.LogData("Log data to screen");

```

Et le code appelant pourrait être implémenté comme le montre la figure 76 pour journaliser les données dans un fichier prédéfini.

Figure 76.

```csharp
ILogging logging = LoggingFactory.GetLoggingObject(false);
logging.LogData("Log data to file");

```

Nous avons abstrait l'implémentation à la fois de la méthode `LogData` ainsi que l'instanciation de l'objet `logging`. C'est un exemple très basique de la manière dont le principe d'abstraction peut être implémenté en utilisant C# afin de créer une séparation des préoccupations.

Vous pouvez bien sûr créer de nombreuses couches d'abstraction en utilisant des techniques similaires et divers modèles de conception. Certaines forces motrices clés derrière la manière dont vous abstraitez votre code devraient être une meilleure réutilisation du code, une meilleure lisibilité du code, une maintenance plus facile du code, une extensibilité de la conception et pour faciliter de meilleurs tests unitaires.

Dans ce livre, je n'ai pas approfondi les principes de la programmation orientée objet. Pour une explication plus détaillée de la programmation orientée objet en utilisant C#, vous pouvez consulter les vidéos dans le lien de la liste de lecture ci-dessous. Dans les vidéos de cette liste de lecture, les principes orientés objet d'encapsulation, d'héritage, de polymorphisme et d'abstraction sont expliqués et de nombreux exemples de code pratiques sont inclus.

%[https://www.youtube.com/watch?v=HcjOcwMS43w&list=PL4LFuHwItvKYD0e60jNOtT6mFKqFMH1u_]

Pour une série vidéo complète sur la programmation orientée objet en C#, veuillez visiter ici :

[Série vidéo complète sur la programmation orientée objet en utilisant C#](https://www.youtube.com/watch?v=HcjOcwMS43w&list=PL4LFuHwItvKYD0e60jNOtT6mFKqFMH1u_)

## Gestion des exceptions en C#

L'un de vos critères de conception principaux lors de la conception d'une application devrait être de garantir que votre application est aussi robuste que possible.

Pour ce faire, vous devrez concevoir et implémenter une stratégie de gestion des exceptions bien conçue. C# facilite cela grâce à l'utilisation de blocs `try/catch/finally`.

La gestion des exceptions est utilisée pour empêcher une application de planter. En règle générale, vous devriez essayer autant que possible de prévenir les exceptions d'être levées par le code, et n'utiliser les blocs `try/catch` intégrés de C# que pour gérer les exceptions dans des circonstances véritablement exceptionnelles.

Un bloc `try/catch` vous permet d'encapsuler un certain code que vous savez, dans certaines circonstances exceptionnelles, peut entraîner le plantage de votre application. En comprenant les circonstances exceptionnelles pertinentes qui peuvent provoquer le plantage de votre application, vous pouvez implémenter la fonctionnalité de gestion des exceptions appropriée.

Vous pouvez attraper des exceptions spécifiques via la section `catch` du bloc `try/catch`. Ensuite, vous pouvez gérer l'exception de manière appropriée soit en la traitant dans le bloc catch pertinent, soit en la lançant dans la pile pour être traitée de manière appropriée à un point ultérieur dans la pile d'exécution.

Dans cet exemple de code d'application de calculatrice très basique (représenté dans la figure 77), une méthode nommée `Calculate` est implémentée pour effectuer les calculs.

Figure 77.

```csharp
try
{
    int result1 = Calculate(200000, 500000, '*'); // Une exception OverFlowException se produit
    int result2 = Calculate(5, 2, '^'); // Une exception InvalidOperation se produira dans la méthode Calculate
    int result3 = Calculate(4, 0, '/'); // Tentative de division par zéro
    Console.WriteLine(result1);
}
catch (ArgumentException)
{
    WriteToScreen("Le symbole d'opération d'entrée n'est pas reconnu par cette application");
}
catch (Exception ex)
{
    WriteToScreen(ex.Message);
}
int Calculate(int operand1, int operand2, char operatorSymbol)
{
    int result = 0;
    try
    {
        switch (operatorSymbol)
        {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                checked
                {
                    result = operand1 * operand2;
                }
                break;
            case '/':
                result = operand1 / operand2;
                break;
            default:
                throw new InvalidOperationException();
        }
    }
    catch (OverflowException)
    {
        WriteToScreen(
            "Le résultat du calcul a dépassé la valeur maximale pour le type de données int"
        );
    }
    catch (InvalidOperationException ex)
    {
        throw new ArgumentException(
            $"{nameof(operatorSymbol)} is invalid",
            nameof(operatorSymbol),
            ex
        );
    }
    return result;
}

```

Avec le premier appel à la méthode `Calculate` dans l'exemple ci-dessus, le calcul donnera un résultat trop grand pour être pris en charge par le type de données entier. Cela signifie qu'une exception `OverFlowException` sera initialement signalée par le compilateur C#.

Dans le filtre de capture `OverFlowException` dans l'exemple de code représenté dans la figure 77, un code est implémenté qui gère l'exception localement dans la méthode `Calculate`. Cela signifie que l'exception n'est pas remontée dans la pile pour être gérée dans la méthode appelante. Le code de gestion des exceptions dans le bloc catch `OverFlowException` se contente de journaliser un message dans un fichier via une méthode personnalisée `LogException`.

Avec le deuxième appel à la méthode `Calculate`, un opérateur invalide (c'est-à-dire `^`) est passé à la méthode `Calculate`. Dans la partie par défaut de l'instruction `switch` pertinente, le code lance une exception `InvalidOperation` qui est un type d'exception intégré au langage C#. Dans le bloc `try/catch` se trouve un filtre `catch` pour capturer spécifiquement cette exception `InvalidOperation`.

Dans le bloc `catch`, le code lance une nouvelle exception `ArgumentException` qui est ensuite gérée dans la méthode appelante (qui dans ce cas est la méthode `Main`, le point d'entrée de cette application). Dans l'exemple de code pertinent, les instructions de niveau supérieur sont activées, ce qui signifie que `Main` n'est pas présent dans le code mais, comme discuté précédemment, la méthode `Main` est ajoutée en coulisses et encapsule le code appelant qui est exprimé dans cet exemple sous forme d'instructions de niveau supérieur.

La méthode `Main` contient une section de capture `ArgumentException`. Dans cette section `catch`, l'exception est gérée en affichant un message informatif à l'utilisateur.

On pourrait soutenir que ce type d'exception serait mieux géré dans le code plutôt que d'utiliser le code `try/catch` à cette fin. Vous pourriez, par exemple, valider l'opérateur avant que la méthode `Calculate` ne soit appelée. Si l'opérateur est saisi incorrectement par l'utilisateur, affichez un message informatif. L'utilisateur peut alors modifier son entrée de manière appropriée.

Ainsi, afin d'utiliser la validation plutôt que le code `try/catch` dans ce scénario, le code appelant pourrait être modifié comme vous le voyez dans l'exemple ci-dessous dans la figure 78 :

Figure 78.

```csharp
int result = 0;
Console.WriteLine("Please enter a whole number value for the first operand");
int operand1 = int.Parse(Console.ReadLine());
Console.WriteLine("Please enter a whole number value for the second operand");
int operand2 = int.Parse(Console.ReadLine());
Console.WriteLine("Please enter a valid operator symbol ('+','-','*','/')");
char operatorSymbol = char.Parse(Console.ReadLine());

if (
    operatorSymbol != '+'
    || operatorSymbol != '-'
    || operatorSymbol != '*'
    || operatorSymbol != '/'
)
{
    WriteToScreen(
        "Incorrect operator input. The operator symbol must be one of the following ('+'','-','*','/') "
    );
}
else
{
    result = Calculate(operand1, operand2, operatorSymbol);
    WriteToScreen(result.ToString());
}

int Calculate(int operand1, int operand2, char operatorSymbol)
{
    int result = 0;
    try
    {
        switch (operatorSymbol)
        {
            case '+':
                result = operand1 + operand2;
                break;
            case '-':
                result = operand1 - operand2;
                break;
            case '*':
                checked
                {
                    result = operand1 * operand2;
                }
                break;
            case '/':
                result = operand1 / operand2;
                break;
            default:
                throw new InvalidOperationException();
        }
    }
    catch (OverflowException)
    {
        WriteToScreen(
            "The result of the calculation exceeded that max value for the int data type"
        );
    }
    catch (InvalidOperationException ex)
    {
        throw new ArgumentException(
            $"{nameof(operatorSymbol)} is invalid",
            nameof(operatorSymbol),
            ex
        );
    }
}
return result;

```

Dans ce cas, il est inutile d'utiliser la gestion des exceptions, et au lieu de cela, vous pouvez utiliser un code conditionnel pour valider le symbole de l'opérateur avant même que la méthode `Calculate` ne soit appelée.

Il est important de noter que tous les types d'`Exception` – y compris ceux qui ont été utilisés dans ces exemples de code – sont dérivés du type `Exception`.

Le type `Exception` est intégré à C#. Tous les types d'`Exception` en C# sont dérivés du type de base `Exception`. Une hiérarchie d'héritage d'exceptions a été délibérément conçue et implémentée en C#. Les exceptions que j'ai utilisées dans les exemples de cette section du livre sont `OverflowException`, `InvalidOperationException` et `ArgumentException`. Ces types d'exceptions sont dérivés du type de base `Exception`.

La hiérarchie des types d'exceptions en C# signifie que lorsqu'il y a plusieurs filtres d'exceptions dans un bloc `try/catch`, les types d'exceptions les plus dérivés doivent être inclus en premier dans la liste pertinente des filtres de capture.

Par exemple, dans les exemples représentés dans cette section, l'`ArgumentException` apparaît avant le filtre de capture `Exception`. Si le filtre de capture `Exception` apparaissait avant le filtre `ArgumentException`, cela signifierait que le code dans le filtre de capture `ArgumentException` ne serait jamais appelé. Il est donc important que le filtre de capture `Exception` apparaisse après le filtre de capture `ArgumentException`.

Notez que dans de nombreux cas, vous voudrez inclure une section `finally` dans votre code `try/catch`. Cette section `finally` est toujours appelée lorsque le code `try/catch` pertinent est exécuté. Ainsi, le code inclus dans la section `finally` est exécuté lorsque le code dans la section `try` provoque une exception (entraînant l'exécution du code dans le filtre de capture pertinent) ou même si aucune exception ne se produit en raison du code inclus dans la section `try` pertinente. Cela rend la section `finally` idéale pour inclure du code de nettoyage, utilisé pour nettoyer les ressources (par exemple, les objets de connexion à la base de données) qui ne sont plus nécessaires.

Pour plus de détails sur la gestion des exceptions en C#, vous pouvez consulter les vidéos de la playlist ci-dessous.

%[https://www.youtube.com/watch?v=mpdg6SAaoZ4&list=PL4LFuHwItvKaHOvj1B5DhTnH0MJ1JFJzr]

Pour une série vidéo complète sur la gestion des exceptions en C#, allez ici :

[Série vidéo complète sur la gestion des exceptions en C#](https://www.youtube.com/watch?v=mpdg6SAaoZ4&list=PL4LFuHwItvKaHOvj1B5DhTnH0MJ1JFJzr)

Pour une série vidéo complète sur la gestion des fichiers en C#, allez ici :

[Série vidéo complète sur la gestion des fichiers en C#](https://www.youtube.com/watch?v=DHgU_tAC85U&list=PL4LFuHwItvKaqc6w0awyyNGfkzU4ke5fu)

## Délégations C#

Les délégations peuvent être décrites comme des pointeurs de fonction sécurisés par type. Avec une délégation, vous pouvez définir une définition de méthode qui inclut une liste de paramètres ainsi qu'un type de retour (si aucun type de retour n'est inclus dans la définition de la délégation, le mot-clé `void` doit être inclus à la place d'un type de données).

Les méthodes qui se conforment (de manière appropriée en termes de leurs signatures de méthode) à ce type de délégation défini peuvent être référencées par le type de délégation compatible. Une variable peut être assignée à la délégation pertinente et vous pouvez ensuite utiliser la variable pour invoquer toute méthode appropriée qui est référencée par la délégation.

Dans l'exemple de code représenté dans la figure 79 ci-dessous, une délégation est définie et nommée `LogDel`. Avec la déclaration de la délégation `LogDel`, une définition de méthode pour une méthode est déclarée. La définition de méthode dans ce cas représente toute méthode qui accepte un argument de chaîne et ne retourne pas de valeur (ce qui est désigné par le mot-clé `void`).

Le mot-clé `void` de C# est utilisé dans la définition de la délégation pour signifier que toute méthode référencée par cette délégation ne doit pas retourner de valeur. Bien sûr, vous pouvez déclarer une délégation pour une méthode qui retourne une valeur (auquel cas la définition de la délégation inclurait le type de données approprié au lieu du mot-clé `void`).

Dans ce cas, cependant, une délégation est définie pour fournir une abstraction pour une méthode qui accepte un argument de chaîne et ne retourne pas de valeur.

Dans l'exemple de code représenté dans la figure 79, vous pouvez voir comment une délégation est utilisée pour créer de la flexibilité où le code appelant peut réutiliser la délégation `LogDel` pour journaliser du texte à l'écran de la console ou journaliser le texte dans un fichier texte. En utilisant cette définition de délégation, le code appelant peut même implémenter ce que l'on appelle une délégation multi-cast.

Dans ce cas, une instanciation du type de délégation `LogDel` est utilisée pour combiner la fonctionnalité d'une méthode qui journalise du texte à l'écran ainsi que d'une méthode qui journalise du texte dans un fichier. Dans le code, l'opérateur `+` est utilisé entre deux délégations et le résultat est assigné à une délégation nommée `multiLogDel`.

Lorsque la délégation `multiLogDel` est invoquée, le texte est journalisé à la fois à l'écran de la console et dans le fichier texte. Ainsi, les délégations peuvent être utilisées pour appeler plusieurs méthodes (qui sont définies de manière appropriée où les définitions de méthode correspondent à la définition de la délégation) par une seule invocation de l'instanciation de la délégation.

De plus, par le biais de la délégation, vous pouvez invoquer la fonctionnalité pour une seule des méthodes – dans cet exemple, soit `LogTextToScreen`, soit `LogTextToFile`.

Ainsi, les délégations fournissent une abstraction sécurisée par type et flexible sur les méthodes que vous pouvez utiliser pour appeler une ou plusieurs méthodes qui se conforment à une définition de méthode spécifiée.

Figure 79.

```csharp
Log log = new Log();
LogDel LogTextToScreenDel,
    LogTextToFileDel;
LogTextToScreenDel = new LogDel(log.LogTextToScreen);
LogTextToFileDel = new LogDel(log.LogTextToFile);
LogDel multiLogDel = LogTextToScreenDel + LogTextToFileDel;
Console.WriteLine("Please enter your name");
var name = Console.ReadLine();
LogText(multiLogDel, name);
Console.ReadKey();
void LogText(LogDel logDel, string text)
{
    logDel(text);
}
delegate void LogDel(string text);

class Log
{
    public void LogTextToScreen(string text)
    {
        Console.WriteLine($"{DateTime.Now}: {text}");
    }

    public void LogTextToFile(string text)
    {
        using (
            StreamWriter sw = new StreamWriter(
                Path.Combine(AppDomain.CurrentDomain.BaseDirectory, "Log.txt"),
                true
            )
        )
        {
            sw.WriteLine($"{DateTime.Now}: {text}");
        }
    }
}

```

Pour plus de détails sur les délégations, vous pouvez regarder les vidéos de la playlist ci-dessous.

%[https://www.youtube.com/watch?v=5YTqMe2GC5U&list=PL4LFuHwItvKZwUnVL2KKvfYxNMVo-TQAB]

Pour une série vidéo complète sur les délégations en C#, allez ici :

[Série vidéo complète sur les délégations C#](https://www.youtube.com/watch?v=5YTqMe2GC5U&list=PL4LFuHwItvKZwUnVL2KKvfYxNMVo-TQAB)

## Événements C#

Les événements peuvent être utilisés en C# pour notifier d'autres classes ou objets lorsque, par exemple, une condition est remplie au sein de la classe ou de l'objet dans lequel cet événement réside. Lorsque la condition est remplie au sein de la classe ou de l'objet qui contient l'événement, l'événement peut être déclenché. Cela signifie que les classes ou objets qui ont choisi de recevoir des notifications lorsque l'événement pertinent est déclenché recevront ces notifications.

Les classes ou objets choisissent de recevoir ces notifications en s'abonnant dans le code à l'événement qui réside dans la classe ou l'objet contenant l'événement. La classe ou l'objet qui contient l'événement est connu sous le nom de l'éditeur, et les classes ou objets qui se sont abonnés pour recevoir des notifications lorsque l'événement pertinent est déclenché sont connus sous le nom des abonnés.

Dans l'exemple représenté dans la figure 80 ci-dessous, l'éditeur est la classe nommée `GuessNumberGame`. Vous pouvez voir qu'un événement nommé `GameEvent` a été publié au sein de cette classe. Dans cet exemple simple, l'abonnement à la classe `GameEvent` est fait au sein du point d'entrée ou de la méthode `Main` de l'application (montré dans cet exemple dans les instructions de niveau supérieur de l'application).

Ici, cela est pour la simplicité – mais dans une application réelle, vous pourriez avoir de nombreuses classes abonnées s'abonnant à l'événement au sein de la classe éditeur.

Ainsi, au sein du code appelant, un abonnement à l'événement `GameEvent` est fait par l'utilisation de l'opérateur `+=`. Cet opérateur est utilisé lorsqu'un abonnement à un événement est fait dans le code C#.

Du côté droit de l'opérateur `+=` se trouve le nom d'une méthode qui est désignée pour gérer l'événement lorsque l'événement est déclenché. Ainsi, cette méthode de gestion d'événement réside au sein du code abonné.

Nous avons utilisé un délégué générique intégré de C# pour définir l'événement `GameEvent`. Cela définit en effet la définition de méthode pour la méthode ou les méthodes qui sont désignées pour gérer l'événement.

Le délégué `EventHandler` fournit une définition pour une méthode qui contient deux paramètres. L'un est défini comme `object`, et l'autre est défini comme un argument de type générique qui est passé comme argument au délégué générique intégré `EventHandler` au moment de la compilation au sein de la classe éditeur où l'événement est déclaré.

Ainsi, vous pouvez voir dans le code appelant, une méthode nommée `EventHandlerMethod` est définie qui contient un argument de type `object`. Il y a également un objet défini comme l'argument de type de données passé dans le paramètre de type pour le délégué générique intégré `EventHandler`, lorsque le `GameEvent` est déclaré à l'intérieur de la classe éditeur.

Ainsi, lorsque la condition pertinente est remplie au sein de la méthode `OnCorrectNumberGuessed`, l'événement `GameEvent` est déclenché. Cela, en effet, entraîne l'exécution de la méthode `EventHandlerMethod` au sein du code appelant, ou au sein du code de l'abonné, si vous préférez.

Le code dans la figure 80 est un simple jeu. L'utilisateur a trois chances de deviner un nombre aléatoire entre 1 et 4 (inclus), généré au sein de la classe `GuessNumberGame`.

Si l'utilisateur devine le bon nombre, l'événement `GameEvent` est déclenché et le code au sein de la méthode `EventHandlerMethod` est exécuté. Cela entraîne l'affichage d'un texte à l'utilisateur, l'informant qu'il a deviné le bon nombre et a donc gagné le jeu.

Ainsi, lorsque l'utilisateur devine le bon nombre, le texte suivant est affiché à l'écran de la console : `You guessed it!! Well done! :)`.

Comme nous l'avons discuté précédemment, l'opérateur `+=` est utilisé pour que les abonnés s'abonnent à un événement au sein de la classe ou de l'objet éditeur. Cela leur permet de recevoir des notifications lorsque l'événement est déclenché par le code au sein de la classe ou de l'objet éditeur.

Après le code de la boucle `while`, il y a une ligne de code où l'abonné se désabonne de l'événement. Cela est important, car cela empêche les fuites de mémoire potentielles de se produire.

Pour se désabonner de l'événement, vous pouvez utiliser l'opérateur `-=` de C# :

Figure 80.

```csharp
Console.WriteLine("Guess the number of which the computer is thinking. Is it 1,2,3 or 4?");
Console.WriteLine();
int counter = 0;
bool gameIsWon = false;
GuessNumberGame guessNumberGame = new GuessNumberGame();
guessNumberGame.GameEvent += EventHandlerMethod;
do
{
    counter++;
    Console.WriteLine("Please input your number choice");
    int userGuessedNumber = Int32.Parse(Console.ReadLine());
    guessNumberGame.CompareUsersNumber(userGuessedNumber);
} while (gameIsWon == false && counter < 3);
guessNumberGame.GameEvent -= EventHandlerMethod;
void EventHandlerMethod(object sender, GuessNumberDataEventArgs args)
{
    Console.WriteLine(args.GuessNumberGameOutputMessage);
    gameIsWon = true;
}

class GuessNumberGame
{
    Random rnd = new Random();
    private readonly int generatedRandomNumber = 0;

    public GuessNumberGame()
    {
        this.generatedRandomNumber = rnd.Next(1, 5);
        Console.WriteLine("Computer Gen =" + generatedRandomNumber);
    }

    public void CompareUsersNumber(int guessedNumber)
    {
        if (guessedNumber == this.generatedRandomNumber)
        {
            OnCorrectNumberGuessed(
                new GuessNumberDataEventArgs
                {
                    GuessNumberGameOutputMessage = "You guessed it!! Well done! :)"
                }
            );
        }
    }

    public void OnCorrectNumberGuessed(GuessNumberDataEventArgs e)
    {
        EventHandler & lt;
        GuessNumberDataEventArgs & gt;
        handler = GameEvent;
        if (handler != null)
        {
            handler(this, e);
        }
    }
}

public event EventHandler<GuessNumberDataEventArgs> GameEvent;

}

```

Pour plus de détails sur l'utilisation des événements C# et plus d'exemples de code, vous pouvez consulter la vidéo YouTube ci-dessous.

%[https://www.youtube.com/watch?v=QJJKMW3ErEw&list=PL4LFuHwItvKa3dr0NL732rnnOhcc3aEgG]

Pour une série vidéo complète sur les événements en C#, vous pouvez aller ici :

[Série vidéo complète sur les événements C#](https://www.youtube.com/watch?v=QJJKMW3ErEw&list=PL4LFuHwItvKa3dr0NL732rnnOhcc3aEgG)

## Génériques C#

Les génériques permettent aux développeurs C# de réutiliser un code spécifique (comme celui qui existe dans une méthode, une classe ou une collection) dans le contexte de plusieurs types de données C# différents.

Vous déterminez ce contexte de type de données au moment de la compilation où, par exemple, vous pouvez passer un argument de type de données à un paramètre de type de données contenu dans la définition de la méthode, de la classe ou du type de collection.

Un exemple de code simple de cela est le type générique `List` de C#, qui est une collection intégrée que vous pouvez utiliser. Vous pouvez typer fortement une liste générique au moment de la compilation avec des types de données intégrés de C# comme `int`, `string`, `char`, `bool`, `decimal`, `float`, `double` et ainsi de suite, ainsi que des types définis par l'utilisateur, comme ceux qui sont implémentés en utilisant une classe ou une struct.

Dans l'exemple représenté dans la figure 82, le type de liste générique est utilisé pour stocker les notes d'un étudiant universitaire. Toutes les notes sont des entiers. Lorsque vous regardez la définition du type générique `List` intégré à C#, vous voyez le mot `List` suivi de chevrons, avec un `T` inclus dans les chevrons. Ainsi, le type générique intégré `List` de C# est défini comme le montre la figure 81.

Le `T` est un espace réservé représentant le paramètre de type générique, que vous pouvez utiliser pour passer un argument de type de données au type 'List' au moment de la compilation afin de typer fortement la liste.

Les génériques signifient que les paramètres de type sont inclus dans .NET. Cela permet de concevoir des classes et des méthodes qui reportent la spécification d'un ou plusieurs types jusqu'à ce que la classe ou la méthode soit déclarée et instanciée par le code appelant.

Figure 81.

```csharp
List<T>

```

Figure 82.

```csharp
List<int> grades = new List<int>();
grades.Add(60);
grades.Add(73);
grades.Add(85);
grades.Add(92);
foreach (int grade in grades)
{
    Console.Write($"{grade}, ");
}

// Output: 60, 73, 85, 92,
// Vous pourriez également utiliser la liste générique pour stocker les noms des matières correspondant aux notes de l'étudiant pertinent.
List<string> subjects = new List<string>();
subjects.Add("Observational Astronomy");
subjects.Add("Particle Physics");
subjects.Add("Quantum mechanics");
subjects.Add("Advanced Math");

```

Vous pouvez également utiliser le même type de données de liste générique pour stocker des objets dérivés d'un type défini par l'utilisateur spécifique, implémenté, par exemple, comme une classe dans le code.

Ainsi, dans l'exemple de la figure 83, le type de données de liste est utilisé pour stocker une collection d'objets 'student' :

Figure 83.

```csharp
List<Student> students = new List<Student>();
students.Add(
    new Student
    {
        Id = 1,
        Name = "Dale Jones",
        Grade = 60
    }
);
students.Add(
    new Student
    {
        Id = 2,
        Name = "Gale Davis",
        Grade = 89
    }
);
students.Add(
    new Student
    {
        Id = 3,
        Name = "Debbie Hill",
        Grade = 56
    }
);
students.Add(
    new Student
    {
        Id = 4,
        Name = "Dave Brown",
        Grade = 76
    }
);
foreach (Student student in students)
{
    Console.WriteLine($"{student.Id} {student.Name} {student.Grade} ");
}
// Output:
// 1 Dale Jones 60
// 2 Gale Davis 89
// 3 Debbie Hill 56
// 4 Dave Brown 76

```

Grâce aux génériques, vous êtes en mesure de réutiliser la fonctionnalité du type de données de liste intégré pour stocker plusieurs types de données. Toute liste générique utilisée dans votre code C# doit être fortement typée avec un type de données particulier.

Vous pouvez typer fortement la liste générique en passant le type pertinent comme argument lors de la définition et de l'instanciation d'un objet du type `List`.

Avant l'introduction du type générique `List` (dans .NET Framework 2.0), vous pouviez utiliser un `ArrayList` pour stocker une collection de types de données hétérogènes. Vous pouviez stocker plusieurs types de données différents dans un seul `ArrayList`.

Le problème avec l'`ArrayList` est que tout code appelant récupérant un élément d'un `ArrayList` doit d'abord convertir cette valeur en son type de données approprié avant que la valeur ne puisse être utile.

Chaque élément stocké dans un `ArrayList` est 'boxé' dans le type `object`. Cela est possible car tous les types de données C# héritent du type de données `object`, donc chaque type de données en C# peut être implicitement boxé dans un objet.

Le boxing est simplement le processus de conversion d'un type de valeur en type `object` en C#. Lorsque le runtime de langage commun (CLR) boxe un type de valeur, il enveloppe la valeur dans une instance `System.Object` et la stocke sur le tas géré. Ainsi, pour utiliser un élément récupéré d'un `ArrayList`, l'objet doit d'abord être converti ou 'unboxé' en son type d'origine.

Cela met en évidence l'un des principaux avantages de l'utilisation des génériques en C#. En utilisant la `List` générique pour stocker des éléments fortement typés dans une collection, vous pouvez éviter le 'boxing' et le 'unboxing'. Cela signifie qu'avec les génériques, la surcharge de performance causée par le 'boxing' et le 'unboxing' est également évitée.

L'autre avantage principal est que vous pouvez éviter les erreurs liées aux types qui peuvent se produire à la suite de conversions de types explicites devant être effectuées sur un élément récupéré d'un `ArrayList` à l'exécution.

Ainsi, en typant fortement une `List` au moment de la compilation, le compilateur est en mesure de vérifier que tout le code lié aux types de données est correct avant qu'il ne soit déployé en production. De cette manière, les erreurs liées aux types de données sont anticipées au moment de la compilation.

Représenté dans la figure 84, se trouve un exemple d'utilisation d'un `ArrayList` pour stocker des types de données hétérogènes.

Figure 84.

```csharp
using System.Collections;
using System.ComponentModel;

ArrayList studentDetails = new ArrayList();
int grade = 90;
string name = "Bob Jones";
studentDetails.Add(90); // valeur int boxée en objet
studentDetails.Add("Bob Jones");
studentDetails.Add(
    new Student
    {
        Id = 1,
        Name = "Bob Jones",
        Grade = 90
    }
);
grade = Convert.ToInt32(studentDetails[0]); // performance d'exécution ralentie par le déboxage de l'int student = int32.Parse(studentDetails[2]); // Cela entraînerait une exception d'exécution en raison d'une opération de conversion de type invalide effectuée à l'exécution

```

Ainsi, vous pouvez voir que l'utilisation d'une `List` générique pour stocker des valeurs fortement typées dans une collection (plutôt qu'un `ArrayList` où le code de 'boxing' et de 'unboxing' doit être effectué) entraîne une amélioration des performances. Cela garantit également une meilleure robustesse à l'exécution.

L'exemple représenté dans la figure 85 est un exemple plus compliqué de l'utilisation des génériques en C#. Dans cet exemple, le modèle de fabrique est employé où vous pouvez réutiliser la méthode `GetInstance` pour instancier des objets de différents types en utilisant la même fonctionnalité d'instanciation enveloppée dans la méthode `GetInstance`.

Vous pouvez voir que `K` et `T` sont utilisés comme espaces réservés pour représenter les types qui peuvent être passés comme arguments à la classe au moment de la compilation (c'est-à-dire, afin de typer fortement la classe). Le mot-clé `where` désigne des contraintes (qui sont des règles définies) sur les arguments de type passés à cette classe.

Ainsi, ces contraintes signifient que le type passé comme argument au paramètre représenté par l'espace réservé `T` doit être une classe. Le mot-clé `new` suivi de parenthèses ouvertes et fermées désigne qu'un nouvel objet doit être créé à partir de la classe pertinente qui est de type `K`.

Figure 85.

```csharp
// Instanciation d'objets à partir des types génériques passés comme objets à la classe FactoryPattern.
IStudent student = FactoryPattern<IStudent, Student>.GetInstance();
student.Name = "Bob Jones";
student.Grade = 78;
student.Subject = "Math";
Console.WriteLine($"{student.Name} {student.Grade} {student.Subject}");
IStudent student2 = FactoryPattern<IStudent, Student>.GetInstance();
student2.Name = "Debbie Long";
student2.Grade = 84;
student2.Subject = "Science";
Console.WriteLine($"{student2.Name} {student2.Grade} {student2.Subject}");
IProfessor professor = FactoryPattern<IProfessor, Proffessor>.GetInstance();
professor.Name = "Ron Willis";
professor.MainSubject = "Math";
Console.WriteLine($"{professor.Name} {professor.MainSubject}");

// Output:
// Bob Jones 78 Math
// Debbie Long 84 Science
// Ron Willis Math
static class FactoryPattern<K, T>
    where T : class, K, new()
{
    public static K GetInstance()
    {
        K objK;
        objK = new T();
        return objK;
    }
}

```

Ainsi, dans l'exemple représenté dans la figure 85, les génériques sont utilisés pour créer un code propre et réutilisable pour l'implémentation du modèle de fabrique.

Un seul bloc de code est utilisé pour créer des instances d'objets dérivés de plusieurs types définis par l'utilisateur. Grâce aux génériques, la quantité de code est minimisée, et si vous avez une bonne connaissance des génériques, ce code est facile à maintenir et à réutiliser. Les génériques vous offrent une plus grande flexibilité de conception et garantissent de meilleures performances et robustesse à l'exécution.

Pour plus d'informations sur les génériques C# et plus d'exemples de code, vous pouvez regarder la vidéo YouTube ci-dessous.

%[https://youtu.be/UUF8QCf3rpI&list=PL4LFuHwItvKaeSVOur67Lu-0I7sfjf5N3]

Pour une série vidéo complète sur les génériques en C#, vous pouvez aller ici :

[Série vidéo complète sur les génériques C#](https://youtu.be/UUF8QCf3rpI&list=PL4LFuHwItvKaeSVOur67Lu-0I7sfjf5N3)

## LINQ

LINQ signifie Language-Integrated Query et a été introduit pour la première fois dans les langages .NET avec la version 3.5 de .NET Framework en 2007. Il fournit aux développeurs .NET une abstraction de requête de haut niveau où, par exemple, le code C# peut être utilisé pour interroger nativement des collections d'objets C#. Il est similaire au langage de requête déclaratif bien connu du système de gestion de base de données relationnelle, T-SQL – mais les entités interrogées avec le code LINQ sont des collections d'objets plutôt que des lignes dans des tables de base de données.

L'exemple de code représenté dans la figure 86 montre comment T-SQL pourrait être utilisé pour interroger une table de base de données nommée `Employees`, afin de récupérer toutes les valeurs de champ dans chaque ligne stockée dans la table de base de données `Employees`.

Figure 86.

```sql
SELECT * FROM Employees

```

Dans la figure 87, un exemple de code est représenté où LINQ dans le code C# est utilisé pour interroger une collection d'objets `Employee`.

Figure 87

```csharp
List<Employee> employees = new List<Employee>();
employees.Add(
    new Employee
    {
        Id = 1,
        FirstName = "Gavin",
        LastName = "Lon",
        Salary = 10000
    }
);
employees.Add(
    new Employee
    {
        Id = 2,
        FirstName = "Sandy",
        LastName = "James",
        Salary = 90000
    }
);
employees.Add(
    new Employee
    {
        Id = 3,
        FirstName = "Greg",
        LastName = "Jones",
        Salary = 73000
    }
);
var employeeResults = from e in employees select e;
foreach (Employee emp in employees)
{
    Console.WriteLine(emp.FirstName);
}

```

Si, par exemple, la table de base de données `Employees` contenait quatre champs, à savoir `Id`, `FirstName`, `LastName` et `Salary`, et que vous souhaitiez ne récupérer que les champs `FirstName` et `LastName` via votre requête T-SQL, votre requête ressemblerait à l'exemple de la figure 88.

Figure 88.

```sql
SELECT FirstName, LastName FROM Employees

```

Pour récupérer les champs `FirstName` et `LastName` à partir d'une collection d'objets où chaque objet a une propriété `Id`, une propriété `FirstName`, une propriété `LastName` et une propriété `Salary`, votre requête LINQ pourrait être implémentée comme le montre l'exemple de code dans la figure 89.

Figure 89.

```csharp
var employeeResults =
    from e in employees
    select new Employee { FirstName = e.FirstName, LastName = e.LastName };

```

Il existe deux types de syntaxe que vous pouvez utiliser pour implémenter LINQ en C#. Le type de syntaxe que vous avez vu jusqu'à présent dans cette section est connu sous le nom de syntaxe de requête. Une autre façon d'implémenter le code LINQ est d'utiliser la syntaxe de méthode.

Pour illustrer l'utilisation de la syntaxe de requête par rapport à la syntaxe de méthode, examinons un exemple légèrement plus complexe. Dans l'exemple représenté dans la figure 90, une requête T-SQL est utilisée pour récupérer les champs `FirstName` et `LastName`, pour les lignes concernant les employés ayant un salaire supérieur à `50000`.

Figure 90.

```sql
SELECT FirstName, LastName FROM Employees e WHERE e.Salary > 50000

```

En utilisant la syntaxe de requête dans LINQ pour effectuer la requête équivalente sur une collection d'objets `Employee`, le code ressemblerait à ce qui est représenté dans la figure 91.

Figure 91.

```csharp
var employeeResults =
    from e in employees
    where e.Salary > 50000
    select new Employee
    {
        FirstName = e.FirstName,
        LastName = e.LastName,
        Salary = e.Salary
    };

```

En utilisant la syntaxe de méthode dans LINQ, la requête équivalente pourrait être implémentée avec le code représenté dans la figure 92.

Figure 92.

```csharp
var employeeResults = employees
    .Select(e => new Employee
    {
        FirstName = e.FirstName,
        LastName = e.LastName,
        Salary = e.Salary
    })
    .Where(e => e.Salary > 50000);

```

Ces exemples de code liés à LINQ vous donnent, je l'espère, une idée de l'apparence de la syntaxe de méthode par rapport à la syntaxe de requête.

Notez que vous ne pouvez pas créer toutes les requêtes LINQ en utilisant la syntaxe de requête, donc selon vos besoins, vous devrez peut-être utiliser la syntaxe de méthode pour effectuer certaines requêtes en utilisant LINQ.

En coulisses, le compilateur C# convertit la syntaxe de requête en syntaxe de méthode. La syntaxe de requête a été introduite dans la technologie LINQ spécifiquement pour améliorer la lisibilité de vos requêtes.

LINQ est composé de nombreuses méthodes d'extension qui résident dans l'espace de noms `System.LINQ`. Dans l'exemple de la figure 92, les méthodes d'extension LINQ `Select` et `Where` ont été enchaînées de manière appropriée pour créer la requête souhaitée.

Pour plus de détails sur LINQ et pour plus d'exemples de code, vous pouvez regarder la vidéo YouTube ci-dessous.

%[https://youtu.be/UfZOmSCCbDY&list=PL4LFuHwItvKbzDl6MBp3XY0MrnALSfyub]

Pour une série vidéo complète sur LINQ, vous pouvez aller ici :

[Série vidéo complète sur l'utilisation de LINQ en C#](https://youtu.be/UfZOmSCCbDY&list=PL4LFuHwItvKbzDl6MBp3XY0MrnALSfyub)

## Attributs C#

Vous pouvez associer des métadonnées à des entités de programme (par exemple, des assemblages, des types, des méthodes et des propriétés) par l'utilisation d'attributs en C#.

Les attributs sont puissants lorsqu'ils sont combinés avec la réflexion (un concept que nous discuterons dans la prochaine section). Par l'utilisation de la réflexion, les attributs peuvent être interrogés à l'exécution et ensuite une fonctionnalité personnalisée peut être exécutée en fonction des métadonnées fournies par l'utilisation des attributs pertinents.

Les attributs en C# sont créés comme des objets à l'exécution. Leurs propriétés et méthodes peuvent être utilisées comme n'importe quel autre objet en C#.

Il existe deux grandes catégories d'attributs : les attributs prédéfinis et les attributs personnalisés. Les attributs prédéfinis sont intégrés dans les bibliothèques de classes de base fournies dans .NET, et les attributs personnalisés vous permettent de définir vos propres attributs qui répondent à vos besoins uniques d'application.

Un exemple d'attribut général prédéfini est l'attribut `obsolete`. Vous pouvez consulter la figure 93 pour un exemple de code montrant comment vous pouvez utiliser l'attribut `obsolete` et comment il peut être utile lorsque vous essayez de consommer une méthode obsolète (ou une méthode marquée comme obsolète avec l'attribut `obsolete`).

Dans l'exemple de code, vous pouvez voir que l'attribut `obsolete` décore une méthode nommée `LogToScreen`. Une nouvelle méthode mise à jour nommée `LogToFile` a été créée au sein de la même classe pour remplacer l'ancienne méthode `LogToScreen`. Ainsi, le créateur de la classe `Logging` préférerait que la méthode `LogToFile` soit consommée par les développeurs (lors de l'application de la fonctionnalité de journalisation dans le code appelant) plutôt que la méthode `LogToScreen`.

Lorsque le consommateur de la classe essaie d'utiliser l'ancienne méthode obsolète (dans cet exemple, la méthode `LogToScreen`), un message d'avertissement prédéfini peut être affiché au développeur depuis son éditeur de code. Ce message d'avertissement est créé pour avertir les développeurs qui souhaitent consommer la fonctionnalité de journalisation que la méthode `LogToFile` doit être utilisée pour la journalisation et non la méthode obsolète `LogToScreen`.

Ainsi, pour garantir qu'un message approprié est affiché, vous pouvez passer un message personnalisé approprié comme argument à l'attribut `obsolete` qui décore de manière appropriée la méthode `LogToScreen` (qui a maintenant été jugée comme obsolète). Le message d'avertissement peut, par exemple, avertir les développeurs que l'ancienne méthode (`LogToScreen`) est maintenant obsolète et les diriger pour utiliser la nouvelle méthode préférée (`LogToFile`) à sa place.

Figure 93.

```csharp
Logging logAction = new Logging();
logAction.LogToScreen("Start of Code"); // Ce message, "La méthode LogToScreen est maintenant obsolète. Veuillez utiliser la méthode LogToFile à la place" est signalé par le compilateur C#
SomeFunction();
logAction.LogToScreen("End of Code"); // Ce message, "La méthode LogToScreen est maintenant obsolète. Veuillez utiliser la méthode LogToFile à la place" est signalé par le compilateur C#

```

Dans l'exemple représenté dans la figure 94, un attribut personnalisé est créé par l'implémentation d'une classe C# qui hérite de la classe intégrée de C# `System.Attribute`. Un attribut général prédéfini nommé `AttributeUsage` est utilisé pour décorer la classe afin de faire respecter les règles d'utilisation associées à l'attribut personnalisé `Required`.

Les arguments passés (dans cet exemple) à l'attribut `AttributeUsage` établissent les règles selon lesquelles l'attribut `Required` ne peut être associé qu'aux éléments de programme de champ, de paramètre et de propriété, et ne peut pas être appliqué plusieurs fois au même élément.

L'attribut `Required` ne peut être appliqué qu'une seule fois à un élément de programme particulier et peut être appliqué aux champs, paramètres et propriétés.

Dans l'exemple représenté dans la figure 94, une utilisation très basique d'un attribut personnalisé est implémentée où un attribut personnalisé nommé `RequiredAttribute` est utilisé pour décorer certaines propriétés d'un modèle. Notez que lorsqu'un attribut personnalisé est réellement appliqué, la partie 'Attribute' du nom de l'attribut personnalisé peut être omise. Ainsi, dans la figure 94, vous pouvez voir que les éléments de programme pertinents sont décorés avec l'attribut nommé `Required` et non `RequiredAttribute`.

La classe de modèle `EmployeeModel` est utilisée pour représenter un enregistrement `Employee`. La classe nommée `EmployeeModel` fournit un modèle pour un enregistrement d'employé. L'attribut `Required` vous donne la possibilité de réutiliser cet attribut personnalisé sur les propriétés où la validation `Required` est nécessaire (c'est-à-dire où un utilisateur doit saisir une valeur qui est ensuite assignée à la propriété décorée avec l'attribut `Required`).

Dans le code appelant, la réflexion est employée pour inspecter les éléments de propriété de programme du type défini par l'utilisateur `EmployeeModel` à l'exécution afin de voir s'il y a des attributs appliqués à ses propriétés.

Dans cet exemple basique, le code interroge la propriété `Id` de la classe `EmployeeModel`, et l'attribut `Required` est trouvé être associé à la propriété `Id`. Le code sait alors valider de manière appropriée l'entrée de l'utilisateur pour la propriété `Id` de la classe `EmployeeModel`.

Notez que l'attribut `Required` est également appliqué à la propriété `FirstName`. Vous pouvez donc voir comment un attribut peut être appliqué plusieurs fois afin de répondre à des préoccupations transversales.

Figure 94.

```csharp
using System.Reflection;

Console.WriteLine("Please enter an Id for the employee:");
string id = Console.ReadLine();
Type employeeType = typeof(EmployeeModel);
PropertyInfo prop = employeeType.GetProperty("Id");
Attribute[] attributes = prop.GetCustomAttributes().ToArray();
foreach (Attribute attr in attributes)
{
    if (attr is RequiredAttribute)
    {
        if (string.IsNullOrEmpty(id))
        {
            Console.WriteLine(
                "The employees Id is required. You did not enter the employees Id. "
            );
        }
    }
}

class EmployeeModel
{
    [Required]
    public int Id { get; set; }

    [Required]
    public string FirstName { get; set; }
    public string LastName { get; set; }
}

[AttributeUsage(
    AttributeTargets.Field | AttributeTargets.Parameter | AttributeTargets.Property,
    AllowMultiple = false
)]
class RequiredAttribute : Attribute
{
    public string ErrorMessage { get; set; }

    public RequiredAttribute()
    {
        ErrorMessage = "You cannot leave field, {0}, empty";
    }

    public RequiredAttribute(string errorMessage)
    {
        ErrorMessage = errorMessage;
    }
}

```

Vous pouvez consulter la vidéo suivante qui contient plus de détails et d'exemples de code concernant les attributs C#.

%[https://youtu.be/JOM6zDb9Wa8]

## Réflexion en C#

La réflexion est un concept en C#, où le programmeur est en mesure de créer du code C# qui peut lire dynamiquement les métadonnées des assemblages .NET à l'exécution. Cela vous donne un outil puissant où vous pouvez créer du code pour analyser dynamiquement un assemblage .NET en fonction de ses métadonnées à l'exécution. Votre code peut, par exemple, lire les métadonnées pertinentes de l'assemblage en utilisant la réflexion, et afficher les métadonnées descriptives sur l'assemblage analysé.

La réflexion peut même être utilisée pour lier dynamiquement un objet à un type spécifique qui réside dans l'assemblage à l'exécution et exécuter du code qui réside dans les méthodes du type. Cela est connu sous le nom de liaison tardive.

La plupart du temps, vous n'utiliserez pas la réflexion pour appeler le code dans un assemblage .NET et préférerez plutôt utiliser la liaison précoce. La liaison précoce signifie que le compilateur C# connaît (pour ainsi dire) les éléments de programme pertinents de l'assemblage, par exemple les classes et méthodes publiques d'un assemblage, au moment de la compilation.

L'utilisation de la liaison précoce est la manière la plus sûre de consommer la fonctionnalité d'un type, car toute exception potentielle liée à l'appel de code dans l'objet lié tôt est signalée au moment de la compilation. Cela empêche le code potentiellement erroné d'être publié en production, où il peut entraîner des erreurs d'exécution.

Lorsque la liaison précoce est utilisée, en raison de la nature auto-descriptive des assemblages .NET où les métadonnées sont stockées dans l'assemblage .NET, le compilateur C# est en mesure de connaître (pour ainsi dire) tous les détails pertinents sur l'assemblage au moment de la compilation.

Ainsi, ces métadonnées stockées dans les assemblages .NET signifient que la liaison précoce est possible, où le compilateur C# a toutes les connaissances de type nécessaires, si vous voulez, au moment de la compilation.

En utilisant la réflexion, vous êtes en mesure d'utiliser la technique de liaison tardive qui se produit à l'exécution. La liaison tardive peut être utilisée pour lier dynamiquement à un objet (dérivé d'un type qui réside dans l'assemblage pertinent) à l'exécution et consommer la fonctionnalité qui réside dans l'assemblage .NET pertinent.

C'est un outil puissant, mais ce n'est pas une manière sûre d'exécuter la fonctionnalité dans un assemblage .NET, car la liaison tardive signifie que le code appelant apprend à connaître l'assemblage cible à l'exécution en lisant ses métadonnées avant d'exécuter le code dans l'assemblage. La technique de liaison tardive est donc plus sujette aux erreurs d'exécution, car les erreurs potentielles ne peuvent pas être traitées au moment de la compilation – c'est-à-dire avant que le code dans l'assemblage ne soit exécuté à l'exécution.

Dans l'exemple représenté dans la figure 96, le code dans un assemblage est invoqué dynamiquement en utilisant la réflexion et la liaison tardive.

Figure 95.

```csharp
using System;
using System.Collections.Generic;
using System.Text;

namespace UtilityFunctions
{
    public class BasicMathFunctions
    {
        public double DivideOperation(double number1, double number2)
        {
            return number1 / number2;
        }

        public double MultiplyOperation(double number1, double number2)
        {
            return number1 * number2;
        }
    }
}

```

Un exemple de code est représenté dans la figure 96, où le code réside dans un assemblage différent de celui qui contient le type `BasicMathFunctions` représenté dans la figure 95.

Dans le code appelant (représenté dans la figure 96), la réflexion est utilisée pour lier tardivement au type `BasicMathFunctions` et appeler la méthode `MultiplyOperation`. Ainsi, le code représenté dans la figure 95 réside dans un assemblage désigné par un fichier nommé "UtilityFunctions.dll".

L'assemblage "UtilityFunction.dll" réside dans le même répertoire que l'assemblage qui contient le code appelant (représenté dans la figure 96). La réflexion est utilisée pour charger dynamiquement l'assemblage "UtilityFunctions", lier tardivement au type `BasicMathFunctions` et appeler sa méthode `MultiplyOperation`.

Figure 96.

```csharp
using System.Reflection;

const string TargetAssemblyFileName = "UtilityFunctions.dll";
const string TargetNamespace = "UtilityFunctions";
Assembly assembly = Assembly.LoadFile(
    Path.Combine(AppDomain.CurrentDomain.BaseDirectory, TargetAssemblyFileName)
);
Type classType = assembly.GetType("UtilityFunctions.BasicMathFunctions");
object classInstance = Activator.CreateInstance(classType);
MethodInfo method = classType.GetMethod("MultiplyOperation");
object[] paramValues = new object[2];
paramValues[0] = 2;
paramValues[1] = 3;
object result = method.Invoke(classInstance, paramValues);
Console.WriteLine($"{paramValues[0]} * {paramValues[1]}  = {result}");
// Output:
// 2 * 3  = 6

```

Pour plus de détails et d'exemples de code concernant la réflexion, vous pouvez regarder la vidéo YouTube ci-dessous.

%[https://youtu.be/tGMa9qjncjs]

## Vidéo sur la programmation asynchrone en C#

Je n'ai pas couvert la programmation asynchrone dans ce livre sur C#. Mais si vous souhaitez apprendre la programmation asynchrone en C#, vous pouvez regarder la vidéo YouTube ci-dessous.

%[https://www.youtube.com/watch?v=MyblIAk8cNI&list=PL4LFuHwItvKb5A9W1myICdC-GJU4_6cKE]

Pour une série vidéo complète sur la programmation asynchrone en C#, consultez ceci :

[Série vidéo complète sur la programmation asynchrone en C#](https://www.youtube.com/watch?v=MyblIAk8cNI&list=PL4LFuHwItvKb5A9W1myICdC-GJU4_6cKE)

Si vous souhaitez apprendre à créer des applications web sophistiquées en utilisant C#, j'ai fourni quelques ressources ci-dessous.

Le premier lien vous mène à une playlist YouTube qui fournit des instructions étape par étape sur la façon de construire une SPA (Single Page Application) de panier d'achat en utilisant le framework Blazor. Le deuxième lien vous mène à une playlist YouTube qui fournit des instructions étape par étape sur la façon de construire une application web réelle en utilisant le framework ASP .NET Core MVC.

* [Cours complet sur la SPA de panier d'achat Blazor (Single Page Application)](https://www.youtube.com/watch?v=3_AsedRrqww&list=PL4LFuHwItvKbdK-ogNsOx2X58hHGeQm8c)
* [Cours complet sur ASP .Net CORE MVC](https://www.youtube.com/watch?v=D7R_ToqDKHg&list=PL4LFuHwItvKZ6Mz5W5wzD9uo3w6tNChhX)

## Conclusion

L'objectif de ce livre est de vous aider à acquérir une compréhension des fonctionnalités puissantes disponibles dans le langage de programmation C#. Les exemples de code ont été conçus pour vous fournir une connaissance pratique de ces fonctionnalités.

Vous pouvez appliquer ces exemples de code vous-même en utilisant des outils gratuits comme Visual Studio 2022 Community edition ou Visual Studio Code afin d'acquérir une expérience pratique avec les concepts discutés dans ce livre.

J'ai travaillé avec C# pendant plus de deux décennies et j'ai été impressionné par l'évolution du langage lui-même ainsi que de l'environnement dans lequel le code C# s'exécute, à savoir .NET. Lorsque vous maîtriserez C#, un monde entier de créativité, de concepts intellectuellement stimulants et une multitude d'opportunités de carrière s'ouvriront à vous.

Dans le monde d'aujourd'hui, vous avez l'avantage d'avoir des outils de développement ainsi que des instructions sur la façon de les utiliser librement disponibles. Il existe également beaucoup de contenu gratuit en ligne sur la façon d'utiliser le langage de programmation C# afin de créer des applications réelles.

En utilisant C#, vous pouvez créer une grande variété de types d'applications différents. Vous pouvez créer des applications de bureau multiplateformes, des applications mobiles multiplateformes, une variété de types d'applications web comme des SPAs qui utilisent le framework Blazor. Vous pouvez créer des jeux sophistiqués en 2D et 3D. Vous pouvez créer des applications IoT. Vous pouvez créer des applications cloud natives distribuées mondialement qui utilisent l'architecture Micro-service.

Vous êtes presque illimité en termes des types d'applications que vous pouvez créer pour une multitude de types de plateformes et d'appareils. Avec C#, vous pouvez facilement intégrer l'IA dans vos applications également.

C'est une période très excitante pour être un développeur C# et .NET. Je vous souhaite le meilleur dans l'apprentissage et l'utilisation de ce langage de programmation puissant dans votre parcours en tant que développeur !

Pour un cours complet pour les débutants en C# et un cours avancé complet en C#, consultez ces ressources :

* [Cours complet sur C# pour débutants](https://www.youtube.com/watch?v=2pquQMSYk6c&list=PL4LFuHwItvKbneXxSutjeyz6i1w32K6di)
* [Cours avancé complet sur C#](https://www.youtube.com/watch?v=3cfVmcAkR2w&list=PL4LFuHwItvKaOi-bN1E2WUVyZbuRhVokL)