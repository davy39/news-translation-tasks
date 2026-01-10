---
title: Environnement Golang – GOPATH vs go.mod
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-05-26T00:23:11.000Z'
originalURL: https://freecodecamp.org/news/golang-environment-gopath-vs-go-mod
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/pexels-james-wheeler-1578750.jpg
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Environnement Golang – GOPATH vs go.mod
seo_desc: "By Otavio Ehrenberger\nIn this article, we'll explore the differences between\
  \ the traditional GOPATH environment and the go.mod based environment for Go programming.\
  \ \nThis distinction has significant implications for how Go developers structure\
  \ and ma..."
---

Par Otavio Ehrenberger

Dans cet article, nous allons explorer les différences entre l'environnement traditionnel `GOPATH` et l'environnement basé sur `go.mod` pour la programmation Go.

Cette distinction a des implications significatives sur la manière dont les développeurs Go structurent et gèrent leurs espaces de travail et leurs dépendances.

Nous commencerons par comprendre l'environnement `GOPATH`, son organisation et sa structure. Ensuite, nous explorerons l'approche `go.mod`, adoptée pour fournir une manière modulaire et flexible d'organiser les projets Go.

Comprendre ces deux environnements et la transition de `GOPATH` à `go.mod` offre des informations précieuses sur l'écosystème en évolution de Go.

# Espace de travail unique – la variable d'environnement GOPATH

Le langage de programmation Go a initialement délimité un périmètre pour l'emplacement des dépendances et des projets personnalisés à l'intérieur d'un système de fichiers. Cela était défini par la variable d'environnement `GOPATH`. Cela signifie que Go recherchait les binaires et le code source uniquement sous le répertoire pointé par cette variable.

La variable `GOPATH` pointait par défaut vers un dossier `/go` défini directement sous le chemin du répertoire personnel de l'utilisateur (`~/` dans les systèmes basés sur Unix ou `%HOMEPATH%` sur les systèmes basés sur Windows).

`GOPATH` pouvait également être défini avec des chemins personnalisés, et plus d'un `GOPATH` pouvait être défini pour un seul utilisateur (mais cela était déconseillé en raison des difficultés ajoutées dans la gestion des dépendances).

Il y a trois répertoires notables sous `GOPATH` : `src`, `pkg`, et `bin`. Le répertoire `src` contient le code source de vos projets et des dépendances installées. Lorsque vous exécutez une commande telle que `go get github.com/user/repo`, l'outil Go récupère le module depuis l'emplacement spécifié et le place dans le répertoire `src` sous le `GOPATH`, avec un chemin nommé d'après l'URL de la ressource.

Par exemple, si vous deviez télécharger une bibliothèque depuis un dépôt appartenant à "someuser" sur GitHub, le code source de la bibliothèque résiderait dans `/home/user/go/src/github.com/someuser/library`.

Le répertoire `pkg` contient les objets de package compilés (fichiers .a) dont votre code dépend. Lorsqu'un package est construit, le fichier résultant est placé dans le répertoire `pkg`. Les fichiers de package compilés aident à réduire le temps de compilation car ils peuvent être importés directement dans d'autres packages sans nécessiter de recompilation.

Le répertoire `bin` contient les exécutables binaires de vos applications. Lorsque vous construisez un programme exécutable, le fichier binaire résultant est placé dans le répertoire `bin`.

## Arbre de fichiers pour un espace de travail GOPATH

Cela suppose le chemin par défaut pour `GOPATH` :

```
/home/user/go/         <--- C'est votre GOPATH
├── bin/
├── pkg/
│   └── linux_amd64/
│       └── github.com/
│           └── someuser/
│               └── somelib.a    <--- Package de dépendance compilé
└── src/
    ├── github.com/
    │   └── someuser/
    │       └── somelib/         <--- Code source de la dépendance
    │           └── somelib.go
    └── myapp/                   <--- Votre projet
        └── main.go

```

Dans cette structure :

* Le répertoire src contient le code source de vos projets et des dépendances installées.
* Le répertoire pkg contient les versions compilées des packages dont votre code dépend.
* Le répertoire bin contient les exécutables binaires compilés.

La structure d'espace de travail unique définie par `GOPATH` signifie que tout votre code Go et ses dépendances partagent un espace commun unique.

Il est cependant intéressant de noter que cette approche a évolué avec l'introduction des modules Go dans Go 1.11. Cela répond principalement au manque d'un système de versionnement approprié pour les dépendances et à la flexibilité de stocker des projets sous un système de fichiers.

# Approche modulaire – le fichier `go.mod`

À partir de Go 1.11 (août 2018), l'option modulaire est devenue disponible comme alternative à un espace de travail défini par `GOPATH`. Cela est délimité par la présence d'un fichier `go.mod` et également généralement d'un fichier go.sum, généré une fois qu'une opération concernant des packages hébergés externement est exécutée (comme `go get <package>`).

Avant de continuer, il est important de clarifier ce qu'est un package et comment un module diffère d'un package :

## Packages en Go

Un package en Go est la plus petite unité de distribution de code. Ils sont définis par un répertoire contenant un ou plusieurs fichiers source `.go` avec le nom du package déclaré en haut. Tous les fichiers dans le répertoire doivent déclarer le même nom de package.

Les packages permettent de structurer et de réutiliser le code. Ils fournissent un moyen d'encapsuler du code lié dans une seule unité, qui peut être importée et utilisée par d'autres packages. La bibliothèque standard de Go, par exemple, se compose de nombreux packages tels que fmt, os, net, et ainsi de suite.

Il existe un nom de package spécial unique, `main`. Ce package contient la fonction `main()` qui est le point d'entrée pour un projet. Chaque projet destiné à devenir éventuellement un exécutable doit contenir la fonction `main()`, et donc le package `main`.

Il est bon de déclarer le ou les fichiers du package principal à la racine du projet et les autres packages dans leurs propres répertoires.

## Modules en Go

Un module est une collection de packages Go liés qui sont versionnés ensemble comme une seule unité. Les modules enregistrent des exigences de dépendance précises et créent des builds reproductibles.

Un module Go est défini par un fichier go.mod qui réside à la racine de la hiérarchie de répertoires du module. Ce fichier définit le chemin du module, qui est le préfixe du chemin d'importation pour tous les packages au sein du module. Il spécifie les dépendances du module, y compris les versions requises des autres modules.

Les modules permettent le versionnement et la publication d'un ensemble de packages ensemble, et ils rendent également les informations de version des dépendances explicites et plus faciles à gérer. Notez que, bien que versionnées, **les dépendances seront toujours téléchargées sous `src` défini dans le périmètre `GOPATH` par défaut**.

Pour résumer, tandis qu'un package est un moyen de structurer et de réutiliser le code au sein d'un programme Go, un module est une collection versionnée de packages qui gère également les dépendances. Cela permet à chaque projet Go d'avoir son propre environnement de build isolé et reproductible.

## Conventions de nommage pour les modules

En Go, **les noms de modules sont utilisés à l'échelle du système et doivent donc être aussi spécifiques que possible**, surtout si vous prévoyez de distribuer le module à d'autres développeurs. Le nom du module est spécifié dans le fichier `go.mod`, qui agit comme le manifeste du module et est situé à la racine de la hiérarchie de répertoires du module.

Voici quelques directives pour le nommage des modules en Go :

**Chemin du module** : Le chemin du module doit être un identifiant unique global pour le module. Il prend généralement la forme d'un nom de domaine internet à l'envers, suivi du nom du module. Par exemple, `github.com/littlejohnny65/example-module`. Le chemin du module est utilisé comme chemin d'importation lors de l'importation de packages depuis le module.

**Nom du module** : Le nom du module est le dernier composant du chemin du module. Il doit être court, descriptif et respecter les conventions de nommage de Go. Il est recommandé d'utiliser des lettres minuscules sans soulignements ou mixedCaps. Par exemple, `examplemodule`.

**Versionnage** : Le nom du module lui-même n'inclut pas d'informations de version. La version d'un module est spécifiée séparément dans le fichier `go.mod` en utilisant un identifiant de version de module, tel que `v1.2.3`. La combinaison du chemin du module et de l'identifiant de version identifie de manière unique une version spécifique du module.

Il est important de choisir des noms significatifs et descriptifs pour les modules, car ils sont publiquement identifiables et peuvent être utilisés comme dépendances dans d'autres projets. Des conventions de nommage claires et cohérentes aident à comprendre le but et le contexte d'un module.

## Le fichier go.sum

Lorsque vous exécutez une commande comme `go get github.com/user/repo`, les outils Go récupéreront le module depuis cet emplacement. Cela permet d'héberger du code Go sur n'importe quel serveur qui supporte des systèmes de contrôle de version comme Git, Mercurial, Bazaar ou Subversion.

Go a une approche très flexible et directe pour télécharger des dépendances depuis des dépôts externes. La solution adoptée pour garantir l'intégrité des dépendances est donc de créer un fichier local pour stocker une somme de contrôle pour chaque dépendance. C'est ce qui garantit que la dépendance installée est exactement la même.

Le fichier de somme de contrôle est généré par les outils Go locaux. Il **doit être poussé vers des environnements externes** tels que des serveurs et des Dockerfiles si vous voulez vous assurer que les dépendances seront exactement les mêmes que dans votre environnement local.

## Arbre de fichiers pour un projet Go modulaire

```
/home/user/projects/
└── myapp/                         # Votre projet
    ├── custom/                   # Packages personnalisés
       └── ...                          # Fichiers .go définissant la fonctionnalité
    ├── go.mod                     # Fichier go.mod définissant les dépendances et versions
    ├── go.sum                     # Fichier go.sum qui vérifie l'intégrité des dépendances
    └── main.go                    # Point d'entrée

```

Arbre de fichiers pour le cache de modules, en supposant le chemin GOPATH par défaut :

```
/home/user/go/        # C'est votre GOPATH
└── pkg/
    └── mod/
        └── cache/
            └── download/
                └── github.com/
                    └── someuser/
                        └── somelib/     # Code source de la dépendance
                            └── somelib.go

```

Dans cette structure :

* Votre projet peut vivre n'importe où dans votre système de fichiers. Il contient un fichier go.mod et un fichier go.sum.
* Le fichier go.mod liste les versions spécifiques des dépendances que votre projet utilise.
* Le fichier go.sum fournit des sommes de contrôle pour le contenu exact de chaque dépendance au moment où elle est ajoutée à votre module.
* Les dépendances sont stockées dans le cache de modules Go, qui est partagé entre tous les projets sur votre système.

# Commandes CLI de module

Il existe plusieurs commandes pratiques disponibles pour travailler avec des projets Go modulaires :

**`go mod init`** : Initialise un nouveau module dans le répertoire courant. Il crée un fichier `go.mod` qui définit le chemin du module et le configure pour la gestion des dépendances.

**`go mod tidy`** : Ajoute les modules et dépendances manquants et supprime ceux inutilisés du fichier `go.mod`. Il garantit que le fichier `go.mod` reflète avec précision les dépendances requises de votre projet.

**`go mod download`** : Télécharge les dépendances définies dans le fichier `go.mod` et les stocke dans le cache de modules. Il récupère les versions spécifiques des dépendances nécessaires pour votre projet.

**`go mod vendor`** : Copie les dépendances dans un répertoire `vendor` au sein de votre projet. Cette commande est utile lorsque vous souhaitez créer un projet autonome qui inclut toutes ses dépendances.

**`go mod verify`** : Vérifie que les dépendances dans le cache de modules correspondent aux sommes de contrôle cryptographiques attendues spécifiées dans le fichier `go.sum`. Il garantit l'intégrité et l'authenticité des dépendances téléchargées.

**`go mod graph`** : Affiche le graphe de dépendance des modules, montrant les relations entre les modules et leurs versions. Il peut être utile pour comprendre la structure globale des dépendances de votre projet.

**`go mod edit`** : Fournit une gamme de sous-commandes pour effectuer des modifications manuelles au fichier `go.mod`. Il vous permet d'ajouter, de supprimer ou de mettre à jour les exigences des modules, de remplacer des modules, et plus encore.

Ce ne sont là que quelques-unes des commandes `go mod` couramment utilisées. Vous pouvez explorer plus de commandes et leurs options en exécutant `go help mod` ou en vous référant à la documentation officielle de Go sur les modules.

# Conclusion

L'approche modulaire n'est pas radicalement différente ni incompatible avec l'espace de travail unique. Mais elle s'appuie sur celui-ci pour apporter plus de flexibilité et de gestion.

Les modules vous permettent d'avoir un projet où vous le souhaitez dans votre système de fichiers et également d'avoir des dépendances avec espace de noms pour une meilleure stabilité. Mais il utilise toujours GOPATH comme emplacement par défaut pour stocker les dépendances et les exécutables.

En conclusion, l'environnement modulaire fourni par go.mod est un outil puissant dans la boîte à outils du développeur Go, complémentant et étendant la fonctionnalité de l'environnement traditionnel GOPATH. Il signale l'adaptation de Go à la complexité et à l'échelle croissantes du développement logiciel moderne, démontrant l'évolution continue du langage pour répondre aux besoins changeants de ses utilisateurs.

Alors que nous avançons, il est passionnant d'imaginer ce que les futurs développements dans l'écosystème de Go apporteront.