---
title: Comment terminer les programmes Go de manière élégante – Un guide pour les
  arrêts gracieux
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-08-13T20:30:58.889Z'
originalURL: https://freecodecamp.org/news/graceful-shutdowns-k8s-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723496940277/5fe7a894-9c67-40fd-95c4-64ef32444a4d.png
tags:
- name: Kubernetes
  slug: kubernetes
- name: Go Language
  slug: go
- name: Devops
  slug: devops
seo_title: Comment terminer les programmes Go de manière élégante – Un guide pour
  les arrêts gracieux
seo_desc: 'Have you ever pulled the power cord out of your computer in frustration?
  While this might seem like a quick solution to certain problems, it can lead to
  data loss and system instability.

  In the world of software, a similar concept exists: the hard sh...'
---

Avez-vous déjà débranché le câble d'alimentation de votre ordinateur par frustration ? Bien que cela puisse sembler une solution rapide à certains problèmes, cela peut entraîner une perte de données et une instabilité du système.

Dans le monde du logiciel, un concept similaire existe : l'arrêt brutal. Cette terminaison abrupte peut causer des problèmes tout comme son homologue physique. Heureusement, il existe une meilleure façon : l'arrêt gracieux.

Pour les applications déployées dans des environnements orchestrés (comme Kubernetes), la gestion gracieuse des signaux de terminaison est cruciale.

En intégrant l'arrêt gracieux, vous fournissez une notification préalable au service. Cela lui permet de compléter les requêtes en cours, potentiellement sauvegarder des informations d'état sur le disque, et finalement éviter la corruption des données pendant l'arrêt.

Dans ce guide, nous plongerons dans le monde des arrêts gracieux, en nous concentrant spécifiquement sur leur implémentation dans les applications Go s'exécutant sur Kubernetes.

## Signaux dans les systèmes Unix

L'un des outils clés pour réaliser des arrêts gracieux dans les systèmes basés sur Unix est le concept de signaux. Ce sont, en termes simples, un moyen simple de communiquer une chose spécifique à un processus, depuis un autre processus.

En comprenant comment fonctionnent les signaux, vous pouvez les utiliser pour implémenter des procédures de terminaison contrôlées dans vos applications, assurant un processus d'arrêt fluide et sécurisé pour les données.

Il existe de nombreux signaux, et vous pouvez les trouver [**ici**](https://en.wikipedia.org/wiki/Signal_(IPC)). Mais notre préoccupation dans cet article ne concerne que les signaux d'arrêt :

* **SIGTERM** – envoyé à un processus pour demander sa terminaison. Le plus couramment utilisé, et nous nous concentrerons dessus plus tard.

* **SIGKILL** – "quitter immédiatement", ne peut pas être interféré.

* **SIGINT** – signal d'interruption (comme Ctrl+C)

* **SIGQUIT** – signal de sortie (comme Ctrl+D)

Ces signaux peuvent être envoyés par l'utilisateur (Ctrl+C / Ctrl+D), depuis un autre programme/processus, ou depuis le système lui-même (noyau / OS). Par exemple, un **SIGSEGV** aka segmentation fault est envoyé par le système d'exploitation.

## Notre service de test

Pour explorer le monde des arrêts gracieux dans un cadre pratique, créons un service simple avec lequel nous pouvons expérimenter. Ce service "de test" aura un seul endpoint qui simule un travail réel (nous ajouterons un léger délai) en appelant la commande Redis [INCR](https://redis.io/docs/latest/commands/incr/). Nous fournirons également une configuration Kubernetes de base pour tester comment la plateforme gère les signaux de terminaison.

L'objectif ultime : garantir que notre service gère gracieusement les arrêts sans perdre de requêtes/données. En comparant le nombre de requêtes envoyées en parallèle avec la valeur finale du compteur dans Redis, nous pourrons vérifier si notre implémentation d'arrêt gracieux est réussie.

Nous n'entrerons pas dans les détails de la configuration du cluster Kubernetes et de Redis, mais vous pouvez trouver la [configuration complète dans ce dépôt Github](https://github.com/plutov/packagemain/tree/master/graceful-shutdown).

Le processus de vérification est le suivant :

1. Déployer Redis et l'application Go sur Kubernetes.

2. Utiliser [**vegeta**](https://github.com/tsenart/vegeta) pour envoyer 1000 requêtes (25/s sur 40 secondes).

3. Pendant que vegeta s'exécute, initialiser une [**Rolling Update**](https://kubernetes.io/docs/tutorials/kubernetes-basics/update/update-intro/) Kubernetes en mettant à jour le tag de l'image.

4. Se connecter à Redis pour vérifier le "compteur", il devrait être 1000.

Commençons par notre serveur HTTP Go de base.

**hard-shutdown/main.go :**

```go
package main

import (
  "net/http"
  "os"
  "time"

  "github.com/go-redis/redis"
)

func main() {
  redisdb := redis.NewClient(&redis.Options{
    Addr: os.Getenv("REDIS_ADDR"),
  })

  server := http.Server{
    Addr: ":8080",
  }

  http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
    go processRequest(redisdb)
    w.WriteHeader(http.StatusOK)
  })

  server.ListenAndServe()
}

func processRequest(redisdb *redis.Client) {
  // simuler une logique métier ici
  time.Sleep(time.Second * 5)
  redisdb.Incr("counter")
}
```

Lorsque nous exécutons notre procédure de vérification en utilisant ce code, nous verrons que certaines requêtes échouent et que le **compteur est inférieur à 1000** (le nombre peut varier à chaque exécution).

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F96fe0766-1aee-4865-a233-1827d4eb92cc_1172x222.png align="left")

Ce qui signifie clairement que nous avons perdu des données pendant la mise à jour progressive. 😢

## Comment gérer les signaux en Go

Go fournit un package [signal](https://pkg.go.dev/os/signal) qui permet de gérer les signaux Unix. Il est important de noter que par défaut, les signaux SIGINT et SIGTERM provoquent la sortie du programme Go. Et pour que notre application Go ne se termine pas si abruptement, nous devons gérer les signaux entrants.

Il existe deux options pour le faire.

La première consiste à utiliser un canal :

```go
c := make(chan os.Signal, 1)
signal.Notify(c, syscall.SIGTERM)
```

La seconde consiste à utiliser un contexte (l'approche préférée de nos jours) :

```go
ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)
defer stop()
```

**NotifyContext** retourne une copie du contexte parent qui est marqué comme terminé (son canal Done est fermé) lorsqu'un des signaux listés arrive, lorsque la fonction **stop()** retournée est appelée, ou lorsque le canal Done du contexte parent est fermé – selon ce qui se produit en premier.

Il y a quelques problèmes avec notre implémentation actuelle du serveur HTTP :

1. Nous avons une goroutine `processRequest` lente, et puisque nous ne gérons pas le signal de terminaison, le programme se termine automatiquement. Cela signifie que toutes les goroutines en cours sont également terminées.

2. Le programme ne ferme aucune connexion.

Réécrivons-le.

**graceful-shutdown/main.go :**

```go
package main

// imports

var wg sync.WaitGroup

func main() {
  ctx, stop := signal.NotifyContext(context.Background(), syscall.SIGTERM)
  defer stop()

  // redisdb, server

  http.HandleFunc("/incr", func(w http.ResponseWriter, r *http.Request) {
    wg.Add(1)
    go processRequest(redisdb)
    w.WriteHeader(http.StatusOK)
  })

  // en faire une goroutine
  go server.ListenAndServe()

  // écouter le signal d'interruption
  <-ctx.Done()

  // arrêter le serveur
  if err := server.Shutdown(context.Background()); err != nil {
    log.Fatalf("could not shutdown: %v\n", err)
  }

  // attendre que toutes les goroutines se terminent
  wg.Wait()

  // fermer la connexion redis
  redisdb.Close()

  os.Exit(0)
}

func processRequest(redisdb *redis.Client) {
  defer wg.Done()

  // simuler une logique métier ici
  time.Sleep(time.Second * 5)
  redisdb.Incr("counter")
}
```

Voici le résumé des mises à jour :

* Ajout de **signal.NotifyContext** pour écouter le signal de terminaison SIGTERM.

* Introduction d'un **sync.WaitGroup** pour suivre les requêtes en cours (goroutines processRequest).

* Enveloppement du serveur dans une goroutine et utilisation de **server.Shutdown** avec un contexte pour arrêter gracieusement l'acceptation de nouvelles connexions.

* Utilisation de **wg.Wait()** pour s'assurer que toutes les requêtes en cours (goroutines processRequest) se terminent avant de continuer.

* Nettoyage des ressources : Ajout de **redisdb.Close()** pour fermer correctement la connexion Redis avant de quitter.

* Sortie propre : Utilisation de **os.Exit(0)** pour indiquer une terminaison réussie.

Maintenant, si nous répétons notre processus de vérification, nous verrons que les 1000 requêtes sont traitées correctement. 🎉

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0852d7a6-be64-44fb-bb00-c48489365585_1172x222.png align="left")

### Frameworks Web / Bibliothèque HTTP

Les frameworks comme Echo, Gin, Fiber et autres créeront une goroutine pour chaque requête entrante. Cela lui donne un contexte et appelle ensuite votre fonction / gestionnaire en fonction du routage que vous avez décidé. Dans notre cas, ce serait la fonction anonyme donnée à HandleFunc pour le chemin "/incr".

Lorsque vous interceptiez un signal **SIGTERM** et demandez à votre framework de s'arrêter gracieusement, deux choses importantes se produisent (pour simplifier) :

* Votre framework cesse d'accepter les requêtes entrantes

* Il attend que les requêtes entrantes existantes se terminent (attendant implicitement la fin des goroutines).

*Note : Kubernetes cesse également de diriger le trafic entrant depuis le loadbalancer vers votre pod une fois qu'il l'a marqué comme Terminating.*

### Optionnel : Délai d'arrêt

Terminer un processus peut être complexe, surtout s'il y a de nombreuses étapes impliquées comme la fermeture des connexions. Pour s'assurer que tout se passe bien, vous pouvez définir un délai d'attente. Ce délai d'attente agit comme un filet de sécurité, quittant gracieusement le processus s'il prend plus de temps que prévu.

```go
shutdownCtx, cancel := context.WithTimeout(context.Background(), 10*time.Second)
defer cancel()

go func() {
  if err := server.Shutdown(shutdownCtx); err != nil {
    log.Fatalf("could not shutdown: %v\n", err)
  }
}()

select {
case <-shutdownCtx.Done():
  if shutdownCtx.Err() == context.DeadlineExceeded {
    log.Fatalln("timeout exceeded, forcing shutdown")
  }

  os.Exit(0)
}
```

## Cycle de vie de la terminaison Kubernetes

![](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5a391d61-99c1-4e3b-a4f3-35877570b74f_4251x940.jpeg align="left")

Puisque nous avons utilisé Kubernetes pour déployer notre service, plongeons plus profondément dans la manière dont il termine les pods. Une fois que Kubernetes décide de terminer le pod, les événements suivants auront lieu :

1. Le pod est défini à l'état "Terminating" et retiré de la liste des endpoints de tous les Services.

2. Le hook **preStop** est exécuté s'il est défini.

3. Le signal **SIGTERM** est envoyé au pod. Mais maintenant, notre application sait quoi faire !

4. Kubernetes attend une période de grâce (**terminationGracePeriodSeconds**), qui est de 30s par défaut.

5. Le signal **SIGKILL** est envoyé au pod, et le pod est retiré.

Comme vous pouvez le voir, si vous avez un processus de terminaison long, il peut être nécessaire d'augmenter le paramètre **terminationGracePeriodSeconds**. Cela permet à votre application d'avoir suffisamment de temps pour s'arrêter gracieusement.

## Conclusion

Les arrêts gracieux protègent l'intégrité des données, maintiennent une expérience utilisateur fluide et optimisent la gestion des ressources. Avec sa bibliothèque standard riche et son accent sur la concurrency, Go permet aux développeurs d'intégrer facilement les pratiques d'arrêt gracieux – une nécessité pour les applications déployées dans des environnements conteneurisés ou orchestrés comme Kubernetes.

Vous pouvez trouver le code Go et les manifests Kubernetes dans [ce dépôt Github](https://github.com/plutov/packagemain/tree/master/graceful-shutdown).

## Ressources

* [package os/signal](https://pkg.go.dev/os/signal)

* [Cycle de vie des pods Kubernetes](https://kubernetes.io/docs/concepts/workloads/pods/pod-lifecycle/)

* [Explorez plus d'articles de packagemain.tech](https://packagemain.tech/p/graceful-shutdowns-k8s-go)