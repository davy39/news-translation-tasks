---
title: Comment commencer avec Golang – un guide pour les développeurs
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2024-02-14T14:01:00.000Z'
originalURL: https://freecodecamp.org/news/golang-developer-roadmap
coverImage: https://www.freecodecamp.org/news/content/images/2024/02/go-roadmap-fcc.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Comment commencer avec Golang – un guide pour les développeurs
seo_desc: "By Shubham Chadokar\nThe Go programming language – also known as Golang\
  \ – is now almost 15 years old. And it's become a popular choice for web development\
  \ and microservices thanks to its performance and efficient resource utilisation.\
  \ \nGo jobs are als..."
---

Par Shubham Chadokar

Le langage de programmation Go – également connu sous le nom de Golang – existe depuis presque 15 ans. Et il est devenu un choix populaire pour le développement web et les microservices grâce à ses performances et son utilisation efficace des ressources.

Les emplois liés à Go sont également assez bien rémunérés. Selon le [rapport Glassdoor](https://www.glassdoor.com/Salaries/golang-developer-salary-SRCH_KO0,16.htm?countryPickerRedirect=true), le salaire moyen d'un développeur Go est d'environ 103 000 $ aux États-Unis, et peut atteindre jusqu'à 200 000 $.

Prêt à commencer votre parcours en tant que développeur Go ? Ce guide peut vous servir de référence.
Dans celui-ci, j'ai essayé de détailler autant de points que possible. Pour chaque point, j'ai inclus des commentaires et des exemples pour l'expliquer en profondeur. Les références fournies à la fin couvrent tous les points.

Voici ce que nous allons couvrir :

1. [Pourquoi apprendre Go ?](#heading-pourquoi-apprendre-go)
2. [Comment installer Go](#heading-comment-installer-go)
3. [Les bases de Go](#heading-les-bases-de-go)
4. [Concepts avancés](#heading-concepts-avances)
5. [Développement web en Go](#heading-developpement-web-en-go)
6. [Journalisation, tests, benchmarking et débogage](#heading-journalisation-tests-benchmarking-et-debogage)
7. [Comment construire des microservices scalables](#heading-comment-construire-des-microservices-scalables)
8. [Comment construire des outils en ligne de commande (CLI)](#heading-comment-construire-des-outils-en-ligne-de-commande)
9. [Projets pour améliorer vos compétences en Go](#heading-projets-pour-ameliorer-vos-competences-en-go)
10. [Et ensuite ?](#heading-et-ensuite)
11. [Références](#heading-references)

## 🏆 Pourquoi apprendre Go ?

Go a été introduit pour la première fois à la fin de l'année 2009. C'est un langage de programmation open-source, statiquement typé, compilé et de haut niveau, conçu chez Google. C'est un choix populaire pour construire des systèmes sécurisés et scalables.

Selon l'enquête annuelle [StackOverflow](https://survey.stackoverflow.co/2023/), c'est l'un des langages de programmation les plus populaires et appréciés. De plus, dans l'[Index Tiobe 2024](https://www.tiobe.com/tiobe-index/), Go occupe actuellement la 11e position, et sa position s'améliore régulièrement chaque année.

Go est un choix populaire pour construire des services et des API scalables et efficaces. Il est largement utilisé pour l'architecture des microservices grâce à son faible empreinte mémoire, sa compilation rapide et ses performances élevées.

Grâce à son support intégré pour la concurrence via les goroutines et les canaux, c'est un choix populaire pour le développement de la blockchain. Par exemple, Ethereum et Hyperledger Fabric sont écrits en Go.

Vos logiciels préférés comme Docker, Kubernetes, Hugo, GitHub CLI, Prometheus, Terraform, et bien d'autres sont également écrits en Go.

Et des entreprises comme Google, Meta, Netflix et Uber utilisent toutes Go.

Vous pouvez consulter les ressources suivantes pour en savoir plus :

* [go.dev](https://go.dev/solutions/case-studies)
* [stackshare](https://stackshare.io/golang)

## Comment installer Go

Vous pouvez installer Go sur votre système d'exploitation respectif depuis [ici](https://go.dev/dl/).

Testez l'installation en utilisant la commande `go version` :

```bash
$ go version
go version go1.21.4 darwin/arm64
```

Si vous obtenez une erreur, vérifiez les variables d'environnement.

## Les bases de Go

Commençons par comprendre la syntaxe de base pour exécuter un programme Go. Le programme commence par le package `main` et la fonction `main`. Les fichiers sont enregistrés avec une extension `.go`.

En Go, un package est une unité fondamentale pour structurer et gérer le code. Vous pouvez utiliser le mot-clé `import` pour importer n'importe quel package. Par exemple, pour afficher un message, vous pouvez utiliser le package `fmt` ou `log`.

Voici un programme simple d'affichage de message en Go :

```go
// main.go
package main

import "fmt"

func main() {
	fmt.Println("freecodecamp")
}
```

Pour exécuter le programme, utilisez `go run <nom_du_fichier>.go`.

```bash
$ go run main.go
freecodecamp
```

Maintenant, vous pouvez commencer à apprendre les sujets suivants :

* **Types de données de base** : int, float, bool, string, array
* **Types de données de référence** : channel, map, slices
* **Variables et constantes**
* **Instructions conditionnelles** : if, if else, switch
* **Instruction d'itération** : for (seul "for" est disponible, pas de "while")
* **Conversion de type et inférence** : il n'y a pas de conversion de type implicite disponible
* **Fonction d'export** : Exporter une fonction se fait en mettant une majuscule à sa première lettre
* **Module** : Initialisation du module. Apprenez les commandes sous `go mod`.
* **Importation de packages tiers** : Utilisation de `go get <url_du_depot_git>.git`
* **Mots-clés de base** : `make`, `new`, `range`, `defer`

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-14-at-9.58.31-PM.png)

Beaucoup de ces concepts sont couverts dans [ce guide pour débutants](https://www.freecodecamp.org/news/golang-for-beginners/). Et si vous voulez approfondir davantage, [voici un manuel complet](https://www.freecodecamp.org/news/learn-golang-handbook/) qui couvre en détail les concepts de base de Go.

## Concepts avancés

Pour exploiter le potentiel de Go afin de construire un système scalable et distribué, il est essentiel d'avoir une solide compréhension de ses fonctionnalités principales.

Voici les fonctionnalités principales de Go :

* Fonctions et packages
* Concurrence et goroutines
* Canaux
* Gestion de contexte
* Gestion des erreurs
* Pointeurs et gestion de la mémoire
* Collecte des déchets (Vous pouvez ajuster le GC par défaut pour obtenir un gain de performance)
* Modèles de concurrence
* Mutexes
* Waitgroups

![Image](https://www.freecodecamp.org/news/content/images/2024/02/Screenshot-2024-02-14-at-9.57.15-PM.png)

Si vous souhaitez approfondir tous ces concepts importants de Go, [voici un cours gratuit de 10 heures pour vous](https://www.freecodecamp.org/news/go-programming-video-course/).

## Développement web en Go

Avec une bibliothèque standard riche, une concurrence intégrée et des performances excellentes, Go est un choix idéal pour le développement web. Au-delà de ses packages intégrés, l'écosystème Go offre une variété de frameworks et de packages pour le développement web parmi lesquels choisir.

Voici quelques frameworks et packages bien connus :

* net/http (package intégré)
* [gorilla/mux](https://github.com/gorilla/mux)
* [gin](https://github.com/gin-gonic/gin)
* [chi](https://github.com/go-chi/chi)
* [fiber](https://github.com/gofiber/fiber)
* [echo](https://github.com/labstack/echo)

Tous sont des frameworks bien connus, et vous pouvez commencer avec n'importe lequel d'entre eux. Certains suivent le modèle `net/http` et d'autres sont inspirés par Express ou d'autres frameworks.

## Journalisation, tests, benchmarking et débogage

Le langage fournit un package de journalisation complet `log` pour une surveillance efficace, ainsi qu'un package intégré pour les tests et le benchmarking. Vous devez comprendre les techniques de débogage efficaces pour identifier et résoudre les problèmes dans le code.

### Journalisation en Go

Le package standard `log` est un excellent point de départ. Il est facilement configurable pour inclure le chemin du fichier, le type de journal et tout message personnalisé dans le message de journal.

En plus de cela, il existe de nombreux loggers disponibles. Ces loggers suivent les normes industrielles de journalisation et sont hautement performants par rapport au package standard `log`.

Voici quelques-uns des loggers disponibles :

* [uber-go/zap](https://github.com/uber-go/zap)
* [logrus](https://github.com/sirupsen/logrus)
* [zerolog](https://github.com/rs/zerolog)
* [apex/log](https://github.com/apex/log)
* [slog (package standard)](https://go.dev/blog/slog)

### Tests et benchmarking en Go

Le framework de test intégré `testing` fournit un support pour écrire des tests et des benchmarks.

La commande `go test` est utilisée pour exécuter les tests et les benchmarks. Vous pouvez ajouter des tests et des benchmarks dans un fichier se terminant par `_test.go`.

Pour écrire un test, utilisez `testing.T` et suivez la convention de nommage des fonctions `TestXxx`.

Par exemple, pour écrire un test pour la fonction `fibonaci`, le nom de sa fonction de test serait `TestFibonaci` où `Test` est le mot-clé qui indique au compilateur Go qu'il s'agit d'une fonction de test, et `Fibonaci` est le nom de la fonction. N'oubliez pas de mettre une majuscule à la première lettre du nom de la fonction de test, `Fibonaci`.

Vous pouvez en savoir plus sur [l'ajout de tests à votre code Go ici](https://go.dev/doc/tutorial/add-a-test).

Pour écrire un benchmark, utilisez `testing.B` et suivez la convention de nommage des fonctions `BenchmarkXxx`. Le benchmarking est utilisé pour mesurer les performances des fonctions ou des extraits de code.

Ainsi, pour écrire un benchmark pour la fonction `fibonaci`, le nom de sa fonction de benchmark serait `BenchmarkFibonaci`, où `Benchmark` est le mot-clé qui indique au compilateur Go qu'il s'agit d'une fonction de benchmark, et `Fibonaci` est le nom de la fonction.

Vous pouvez [en savoir plus sur le benchmarking en Go ici](https://www.practical-go-lessons.com/chap-34-benchmarks).

Si vous êtes habitué aux fonctions d'assertion, vous pouvez essayer le package `testify`. C'est un package externe qui améliore la lisibilité des cas de test. En interne, il utilise le package intégré `testing`.

### Débogage en Go

[Delve](https://github.com/go-delve/delve) est un débogueur puissant disponible pour Go. Il s'intègre facilement avec des IDE populaires comme Visual Studio Code, Goland de JetBrains, Neovim, Atom, et bien d'autres.

Vous pouvez utiliser le package intégré `pprof` pour analyser et identifier les goulots d'étranglement de performance et les problèmes d'utilisation de la mémoire. Son chemin est `net/http/pprof`.

## Comment construire des microservices scalables

La construction de microservices scalables nécessite une combinaison d'architecture réfléchie, de pratiques de codage efficaces et d'outils robustes.

Le modèle de concurrence léger de Go, son runtime efficace et sa bibliothèque standard riche peuvent gérer des charges de trafic élevées et évoluer horizontalement, ce qui en fait un choix idéal pour les microservices.

Voici quelques sujets que vous pouvez aborder :

* [Fondamentaux des microservices](https://martinfowler.com/tags/microservices.html)
* Protocoles de communication ([API REST](https://www.freecodecamp.org/news/what-is-rest-rest-api-definition-for-beginners/), [gRPC](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/), [WebSockets](https://www.freecodecamp.org/news/beginners-guide-to-websockets/))
* [Découverte de services](https://www.nginx.com/blog/service-discovery-in-a-microservices-architecture/)
* [Modèle Pub-Sub](https://cloud.google.com/pubsub/docs/overview)
* [Files d'attente de messages](https://www.freecodecamp.org/news/message-queues-in-distributed-systesms/) ([Apache Kafka](https://www.freecodecamp.org/news/apache-kafka-handbook/), [RabbitMQ](https://www.freecodecamp.org/news/message-queues-with-rabbitmq-in-nest-js/))

## Comment construire des outils en ligne de commande

En matière de CLI, Go est une star. Il existe des packages disponibles en Go pour construire des CLI très facilement. Le package intégré `flag` peut être utilisé pour construire des CLI de base.

Le package [Cobra](https://github.com/spf13/cobra) est très populaire pour créer des applications CLI modernes et puissantes. De nombreux projets Go comme GitHub CLI, Hugo et Kubernetes utilisent Cobra.

Voici quelques projets CLI que vous pouvez construire pour vous entraîner :

* **Gestionnaire de tâches** : Développez un gestionnaire de tâches basé sur CLI qui permet les opérations CRUD.
* **Notes** : Construisez un CLI pour prendre des notes.
* **Gestionnaire de mots de passe** : Créez un CLI qui stocke et gère les mots de passe de manière sécurisée avec un chiffrement approprié, une génération et une récupération de mots de passe.
* **Outil de conversion universel** : Construisez un convertisseur universel, qui peut convertir toutes les métriques et devises.

## Projets pour améliorer vos compétences en Go

Pour mieux comprendre les capacités de Go, vous pouvez acquérir une expérience pratique en construisant des projets.

Voici une liste de projets que vous pouvez construire en Go :

* Application Todo
* Application de chat
* CLI
* Microservices qui communiquent en utilisant gRPC
* Conteneurisation d'une application Go
* Création d'un site web de blogging
* Webscraper utilisant le package `net/http` et `goquery`
* Limiteur de débit
* Générateur de modèles d'e-mails utilisant le package `template`

Si vous souhaitez plus de pratique pour construire des projets avec Go, [voici un cours gratuit complet](https://www.freecodecamp.org/news/learn-go-by-building-11-projects/) qui vous guide à travers la construction de 11 projets Go.

## Et ensuite ?

Pour vos prochaines étapes, vous pouvez suivre cette incroyable **[Feuille de route Go](https://roadmap.sh/golang)** créée par Kamran.

![Image](https://www.freecodecamp.org/news/content/images/2024/02/go-roadmap.png)
_Feuille de route Go_

### Références

* [Documentation officielle de Go](https://golang.org/doc/)
* [Effective Go](https://github.com/golang/go)
* [Go Tour](https://go.dev/tour/list)
* [Gobyexample](https://gobyexample.com/)
* [PracticeGo](https://www.youtube.com/@practicego)
* [Microservices](https://martinfowler.com/tags/microservices.html)
* [Créer un CLI avec cobra](https://medium.com/towards-data-science/how-to-create-a-cli-in-golang-with-cobra-d729641c7177)
* [Créer une application de chat](https://medium.com/gitconnected/create-a-chat-application-in-golang-with-redis-and-reactjs-c75611717f84)
* [Enquête StackOverflow 2023](https://survey.stackoverflow.co/2023/)

😃 J'espère que vous avez aimé cet article.

👋 Je suis Shubham Chadokar, développeur de logiciels et créateur de contenu. Vous pouvez me suivre sur Twitter (X) [@schadokar1](https://twitter.com/schadokar1) et vous abonner à ma chaîne YouTube [practicego](https://www.youtube.com/@practicego).