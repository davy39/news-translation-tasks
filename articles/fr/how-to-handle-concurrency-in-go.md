---
title: Comment gérer la concurrence avec les Goroutines et les Channels en Go
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2024-05-10T15:07:54.000Z'
originalURL: https://freecodecamp.org/news/how-to-handle-concurrency-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/joshua-sortino-LqKhnDzSF-8-unsplash.jpg
tags:
- name: concurrency
  slug: concurrency
- name: Go Language
  slug: go
seo_title: Comment gérer la concurrence avec les Goroutines et les Channels en Go
seo_desc: "Concurrency is the ability of a program to perform multiple tasks simultaneously.\
  \ It is a crucial aspect of building scalable and responsive systems. \nGo's concurrency\
  \ model is based on the concept of goroutines, lightweight threads that can run\
  \ mult..."
---

La concurrence est la capacité d'un programme à effectuer plusieurs tâches simultanément. C'est un aspect crucial pour construire des systèmes évolutifs et réactifs. 

Le modèle de concurrence de Go est basé sur le concept de goroutines, des threads légers qui peuvent exécuter plusieurs fonctions de manière concurrente, et des channels, un mécanisme de communication intégré pour un échange de données sûr et efficace entre les goroutines.

Les fonctionnalités de concurrence de Go permettent aux développeurs d'écrire des programmes qui peuvent :

* Gérer plusieurs requêtes simultanément, améliorant la réactivité et le débit.
* Utiliser efficacement les processeurs multi-cœurs, maximisant les ressources du système.
* Écrire du code concurrent qui est sûr, efficace et facile à maintenir.

Le modèle de concurrence de Go est conçu pour minimiser les frais généraux, réduire la latence et prévenir les erreurs de concurrence courantes comme les conditions de course et les interblocages. 

Avec Go, les développeurs peuvent construire des systèmes haute performance, évolutifs et concurrents avec facilité, ce qui en fait un choix idéal pour construire des systèmes distribués modernes, des réseaux et des infrastructures cloud.

## Table des matières

* [Étude de cas : Un guichet de banque](#heading-etude-de-cas-un-guichet-de-banque)
* [Traitement séquentiel](#heading-traitement-sequentiel-aucune-concurrence)
* [Concurrence](#heading-concurrence)
* [Qu'est-ce que les Goroutines et les Channels ?](#heading-quest-ce-que-les-goroutines-et-les-channels)
* [Qu'est-ce qu'une Goroutine ?](#quest-ce-quune-goroutine)
* [Comment implémenter une Goroutine](#heading-comment-implementer-une-goroutine)
* [Comment fonctionne une Goroutine ?](#heading-comment-fonctionne-une-goroutine)
* [Qu'est-ce que les WaitGroups ?](#heading-quest-ce-que-les-waitgroups)
* [Qu'est-ce que les Channels ?](#heading-quest-ce-que-les-channels)
* [Comment écrire des données dans un Channel](#heading-comment-ecrire-des-donnees-dans-un-channel)
* [Comment lire des données depuis un Channel](#heading-comment-lire-des-donnees-depuis-un-channel)
* [Comment implémenter des Channels avec Goroutine](#heading-comment-implementer-des-channels-avec-goroutine)
* [Qu'est-ce que les tampons de Channel ?](#heading-quest-ce-que-les-tampons-de-channel)
* [Qu'est-ce qu'un Channel non tamponné ?](#heading-quest-ce-quun-channel-non-tamponne)
* [Comment créer un Channel tamponné](#heading-comment-creer-un-channel-tamponne)
* [Qu'est-ce que les directions de Channel ?](#heading-quest-ce-que-les-directions-de-channel)
* [Comment gérer plusieurs opérations de communication avec Channel Select](#heading-comment-gerer-plusieurs-operations-de-communication-avec-channel-select)
* [Comment mettre en timeout des processus longs dans un Channel](#comment-mettre-en-timeout-des-processus-longs-dans-un-channel)
* [Comment fermer un Channel](#heading-comment-fermer-un-channel)
* [Comment itérer sur les messages d'un Channel](#heading-comment-iterer-sur-les-messages-dun-channel)
* [Conclusion](#heading-conclusion)

Considérons un scénario pour illustrer la concurrence :

## Étude de cas : Un guichet de banque

Imaginez une banque occupée avec deux guichetiers, Maria et David. Les clients arrivent à la banque pour effectuer diverses transactions comme des dépôts, des retraits et des transferts. L'objectif est de servir les clients rapidement et efficacement.

### Traitement séquentiel (aucune concurrence)

Maria et David travaillent de manière séquentielle, un à la fois. Lorsqu'un client arrive, Maria aide le client, et David attend que Maria ait terminé avant d'aider le client suivant. Cela entraîne un long temps d'attente pour les clients.

### Concurrence

Maria et David travaillent de manière concurrente, servant les clients simultanément. Lorsqu'un client arrive, Maria aide le client avec une transaction, et David aide simultanément un autre client avec une transaction différente. Ils travaillent ensemble, partageant des ressources comme la base de données de la banque et les réserves de liquidités, pour servir plusieurs clients en même temps.

Dans ce scénario, la concurrence permet à Maria et David de travailler ensemble efficacement, servant plusieurs clients simultanément, et améliorant l'expérience globale des clients. Ce même concept s'applique à la programmation informatique, où la concurrence permet à plusieurs tâches de s'exécuter simultanément, améliorant la réactivité, l'efficacité et les performances.

## Qu'est-ce que les Goroutines et les Channels ?

Une goroutine est un thread léger géré par le runtime Go. C'est une fonction qui s'exécute sur le runtime Go. Elle aide à répondre aux exigences de concurrence et de flux asynchrone.

Les goroutines vous permettent de démarrer et d'exécuter d'autres threads d'exécution de manière concurrente dans votre programme.

Les channels sont utilisés pour communiquer entre les goroutines. C'est un conduit typé à travers lequel vous pouvez envoyer et recevoir des valeurs avec l'opérateur de channel : `<-`.

### Comment implémenter une Goroutine

Pour utiliser et implémenter une `goroutine`, le mot-clé `go` est utilisé pour précéder une fonction.

```go
package main

import (
  "fmt"
  "math/rand"
  "time"
)

func pause() {
  time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
}

func sendMsg(msg string) {
  pause()
  fmt.Println(msg)
}

func main() {
  sendMsg("hello") // sync

  go sendMsg("test1") // async
  go sendMsg("test2") // async
  go sendMsg("test3") // async

  sendMsg("main") // sync

  time.Sleep(2 * time.Second)
}

```

Dans l'exemple ci-dessus,

* La fonction `sendMsg` est appelée de manière synchrone et asynchrone.
* La fonction `sendMsg` est appelée de manière synchrone lorsque la fonction `sendMsg` est appelée sans le mot-clé `go`.
* La fonction `sendMsg` est appelée de manière asynchrone lorsque la fonction `sendMsg` est appelée avec le mot-clé `go`.

### Comment fonctionne une Goroutine ?

Lorsque la fonction `sendMsg` est appelée avec le mot-clé `go`, la fonction `main` n'attendra pas que la fonction `sendMsg` termine son exécution avant de continuer à la ligne de code suivante et retournera immédiatement après que la fonction `sendMsg` soit appelée.

Sinon, la fonction est appelée de manière synchrone, et la fonction `main` attendra que la fonction `sendMsg` termine son exécution avant de continuer à la ligne de code suivante.

L'ordre de la sortie lorsque vous exécutez l'exemple ci-dessus différera de l'ordre du code car les trois `goroutine` s'exécutent toutes de manière concurrente et puisque les fonctions font une pause pendant une période de temps, l'ordre dans lequel elles se réveillent différera et sera sorti.

Le `time.Sleep(2 * time.Second)` est une méthode rapide et simple utilisée pour garder la fonction principale en cours d'exécution pendant 2 secondes pour permettre à la `goroutine` de terminer son exécution avant que la fonction principale ne se termine. Sinon, la fonction principale se terminera immédiatement après que la `goroutine` soit appelée et la `goroutine` n'aura pas assez de temps pour terminer son exécution, ce qui entraînera des erreurs.

### Qu'est-ce que les WaitGroups ?

Contrairement au `time.Sleep(2 * time.Second)` utilisé dans l'exemple ci-dessus, les `WaitGroups` sont plus standard pour attendre qu'une collection de goroutines termine son exécution. C'est un moyen simple de synchroniser plusieurs goroutines.

Une goroutine peut également être déclarée avec des fonctions anonymes

```go
package main

import (
  "fmt"
  "sync"
  "time"
  "math/rand"
)

func pause() {
  time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
}

func sendMsg(msg string, wg *sync.WaitGroup) {
  defer wg.Done()
  pause()
  fmt.Println(msg)
}

func main() {
  var wg sync.WaitGroup

  wg.Add(3)

  go func(msg string) {
    defer wg.Done()
    pause()
    fmt.Println(msg)
  }("test1")


  go sendMsg("test2", &wg)
  go sendMsg("test3", &wg)

  wg.Wait()
}

```

Dans l'exemple ci-dessus, le **`sync.WaitGroup`** est utilisé pour attendre que les trois `goroutine` terminent leur exécution avant que la fonction principale ne se termine. Il synchronise les trois `goroutine` et la fonction principale.

* Le **`sync.WaitGroup (wg)`** gère les goroutines et garde une trace du nombre de goroutines qui s'exécutent.
* La méthode **`sync.WaitGroup.Add (wg.Add)`** est utilisée pour ajouter le nombre de goroutines en tant qu'arguments qui s'exécutent.
* La méthode **`sync.WaitGroup.Done (wg.Done)`** est utilisée pour décrémenter le nombre de goroutines qui s'exécutent.
* La méthode `**sync.WaitGroup.Wait (wg.Wait)**` est utilisée pour attendre que toutes les goroutines terminent leur exécution avant que la fonction principale ne se termine.

## Qu'est-ce que les Channels ?

Les channels sont utilisés pour communiquer entre les goroutines. C'est un conduit typé à travers lequel vous pouvez envoyer et recevoir des messages avec l'opérateur de channel, `**<-**`.

Dans leur forme la plus simple, une goroutine écrit des messages dans le channel et une autre goroutine lit les mêmes messages depuis le channel.

Les channels sont créés en utilisant la méthode `make` et le mot-clé `chan` ainsi que son type. Les channels sont utilisés pour transférer des messages du type avec lequel ils ont été déclarés.

Exemple :

```go
package main

func main(){
	msgChan := make(chan string)
}
```

L'exemple ci-dessus crée un channel `msgChan` de type `string`.

### Comment écrire des données dans un Channel

Pour écrire des données dans un channel, spécifiez d'abord le nom (`msgChan`) du channel, suivi de l'opérateur `<-` et du message. Cela est considéré comme l'**Émetteur.**

```go
msgChan <- "hello world"
```

### Comment lire des données depuis un Channel

Pour lire des données depuis un channel, déplacez simplement l'opérateur (`<-`) devant le nom du channel (`msgChan`) et vous pouvez l'assigner à une variable. Cela est considéré comme le **Récepteur.**

```go
msg := <- msgChan
```

### Comment implémenter des Channels avec Goroutine

```go
package main

import (
  "fmt"
  "math/rand"
  "time"
)

func main() {

  msgChan := make(chan string)

  go func() {
    time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
    msgChan <- "hello" // Écrire des données dans le channel
    msgChan <- "world" // Écrire des données dans le channel
  }()

  msg1 := <- msgChan
  msg2 := <- msgChan

  fmt.Println(msg1, msg2)
}
```

L'exemple ci-dessus montre comment écrire et lire des données depuis un channel. Le channel `msgChan` est créé et le mot-clé `go` est utilisé pour créer une goroutine qui écrit des données dans le channel. Les variables `msg1` et `msg2` sont utilisées pour lire des données depuis le channel.

Les channels se comportent comme une file `premier entré, premier sorti`. Ainsi, lorsqu'une goroutine écrit des données dans le channel, l'autre goroutine lit les données depuis le channel dans le même ordre dans lequel elles ont été écrites.

## Qu'est-ce que les tampons de Channel ?

Les channels peuvent être `tamponnés` ou `non tamponnés`. Les exemples précédents incluent l'utilisation de channels non tamponnés.

### Qu'est-ce qu'un Channel non tamponné ?

Un channel non tamponné fait en sorte que l'émetteur se bloque immédiatement après l'envoi d'un message dans le channel jusqu'à ce que le récepteur reçoive le message.

### Qu'est-ce qu'un Channel tamponné ?

Un channel tamponné permet à l'émetteur d'envoyer des messages dans le channel sans se bloquer jusqu'à ce que le tampon soit plein. Ainsi, l'émetteur se bloque uniquement une fois que le tampon est rempli et attend qu'une autre goroutine lise depuis le channel, s'assurant que l'espace devient disponible avant de se débloquer.

### Comment créer un Channel tamponné

Lors de la création d'un channel tamponné, utilisez la fonction `make` et spécifiez un deuxième paramètre pour indiquer la taille du tampon.

```go
msgBufChan := make(chan string, 2)
```

L'exemple ci-dessus crée un channel tamponné `msgBufChan` de type `string` avec une taille de tampon de 2. Cela signifie que le channel peut contenir jusqu'à deux messages avant de se bloquer.

```go
package main

import (
  "time"
)

func main() {
  size := 3
  msgBufChan := make(chan int, size)

  // lecteur (récepteur)
  go func() {
    for {
      _ = <- msgBufChan
      time.Sleep(time.Second)
    }
  }()

  // écrivain (émetteur)
  writer := func() {
    for i := 0; i <= 10; i++ {
      msgBufChan <- i
      println(i)
    }
  }

  writer()
}
```

L'exemple ci-dessus crée un channel tamponné `msgBufChan` de type `int` avec une taille de tampon de 3.

* La fonction `writer` écrit des données dans le channel et la fonction `reader` lit des données depuis le channel.
* Lorsque le programme s'exécute, vous verrez que les nombres `0 à 3` sont imprimés immédiatement et les nombres restants `5 à 10` sont imprimés lentement, environ un par seconde (`time.Sleep(time.Second)`).
* Cela montre l'effet du channel tamponné qui spécifie la taille qu'il peut contenir avant de se bloquer.

## Qu'est-ce que les directions de Channel ?

Lors de l'utilisation de channels comme paramètres de fonction, par défaut, vous pouvez envoyer et recevoir des messages dans la fonction. Pour fournir une sécurité supplémentaire au moment de la compilation, les paramètres de fonction de channel peuvent être définis avec une direction. C'est-à-dire qu'ils peuvent être définis pour être **lecture seule** ou **écriture seule**.

Exemple :

```go
package main

import (
  "fmt"
  "time"
)

func writer(channel chan<- string, msg string) {
  channel <- msg
}

func reader(channel <-chan string) {
  msg := <- channel
  fmt.Println(msg)
}

func main() {
  msgChan := make(chan string, 1)

  go reader(msgChan)


  for i := 0; i < 10; i++ {
    writer(msgChan, fmt.Sprintf("msg %d", i))
  }

  time.Sleep(time.Second * 5)
}
```

L'exemple ci-dessus montre comment définir un channel avec une direction.

* La fonction `writer` est définie avec un channel en écriture seule et
* La fonction `reader` est définie avec un channel en lecture seule.

Le channel `msgChan` est créé avec une taille de tampon de 1. La fonction `writer` écrit des données dans le channel et la fonction `reader` lit des données depuis le channel.

## Comment gérer plusieurs opérations de communication avec Channel Select

L'instruction `select` permet à une goroutine d'attendre sur plusieurs opérations de communication. Un `select` bloque jusqu'à ce que l'un de ses cas puisse s'exécuter, puis il exécute ce cas. Il en choisit un au hasard si plusieurs sont prêts.

Les instructions `select` et `case` sont utilisées pour simplifier la gestion et la lisibilité de `wait` sur plusieurs channels.

Exemple :

```go
package main

import (
  "fmt"
  "time"
  "math/rand"
)

func pause() {
  time.Sleep(time.Duration(rand.Intn(1000)) * time.Millisecond)
}

func test1(c chan<- string) {
  for {
    pause()
    c <- "hello"
  }
}

func test2(c chan<- string) {
  for {
    pause()
    c <- "world"
  }
}

func main() {
  rand.Seed(time.Now().Unix())

  c1 := make(chan string)
  c2 := make(chan string)

  go test1(c1)
  go test2(c2)

  for {
    select {
    case msg1 := <- c1:
      fmt.Println(msg1)
    case msg2 := <- c2:
      fmt.Println(msg2)
    }
  }
}
```

L'exemple ci-dessus montre comment utiliser l'instruction `select` pour attendre sur plusieurs channels. Les fonctions `test1` et `test2` écrivent des données dans les channels `c1` et `c2` respectivement. La fonction `main` lit des données depuis les channels `c1` et `c2` en utilisant l'instruction `select`.

L'instruction select se bloquera jusqu'à ce que l'un des channels soit prêt à envoyer ou recevoir des données. Si les deux channels sont prêts, l'instruction select en choisira un au hasard.

## Comment mettre en timeout des processus longs dans un Channel

La fonction `time.After` est utilisée pour créer un channel qui envoie un message après une durée spécifiée. Cela peut être utilisé pour implémenter un timeout pour un channel.

Il peut être spécifié dans une instruction `select` pour aider à gérer les situations où il faut trop de temps pour recevoir un message depuis l'un des channels surveillés.

Pensez également à utiliser `timeout` lorsque vous travaillez avec des ressources externes, car vous ne pouvez jamais garantir le temps de réponse et, par conséquent, vous devrez peut-être prendre des mesures proactives après qu'un temps prédéterminé se soit écoulé.

L'implémentation d'un `timeout` avec une instruction `select` est très simple.

Exemple :

```go
package main

import (
  "fmt"
  "time"
)

func main() {
 	c1 := make(chan string)

	go func(channel chan string) {
		time.Sleep(1 * time.Second)
		channel <- "hello world"
	}(c1)

	select {
	case msg2 := <-c1:
		fmt.Println(msg2)
	case <-time.After(2 * time.Second): // Timeout après 2 secondes
		fmt.Println("timeout")
  }
}

```

* L'exemple ci-dessus montre comment utiliser la fonction `time.After` pour créer un channel qui envoie un message après une durée spécifiée.
* La fonction `main` lit des données depuis le channel `c1` en utilisant l'instruction `select`.
* L'instruction `select` se bloquera jusqu'à ce que l'un des channels soit prêt à envoyer ou recevoir des données.
* Si le channel `c1` est prêt, la fonction `main` imprimera le message.
* Si le channel `c1` n'est pas prêt après 2 secondes, la fonction `main` imprimera un message de timeout.

## Comment fermer un Channel

Fermer un channel est utilisé pour indiquer qu'aucune autre valeur ne sera envoyée sur le channel. Il est utilisé pour signaler au récepteur que le channel a été fermé et qu'aucune autre valeur ne sera envoyée.

Les channels Go peuvent être explicitement fermés pour aider avec les problèmes de synchronisation. L'implémentation par défaut fermera le channel lorsque toutes les valeurs auront été envoyées.

Fermer un channel se fait en invoquant la fonction intégrée `close`.

```go
close(channel)
```

Exemple :

```go
package main

import (
  "fmt"
  "bytes"
)

func process(work <-chan string, fin chan<- string) {
  var b bytes.Buffer
  for {
    if msg, notClosed := <-work; notClosed {
      fmt.Printf("%s received...\n", msg)
    } else {
      fmt.Println("Channel closed")
      fin <- b.String()
      return
    }
  }
}

func main() {
  work := make(chan string, 3)
  fin := make(chan string)

  go process(work, fin)

  word := "hello world"

  for i := 0; i < len(word); i++ {
    letter := string(word[i])
    work <- letter
    fmt.Printf("%s sent ...\n", letter)
  }

  close(work)

  fmt.Printf("result: %s\n", <-fin)
}


```

L'exemple ci-dessus montre comment fermer un channel. Le channel `work` est créé avec une taille de tampon de 3. La fonction `process` lit des données depuis le channel `work` et écrit des données dans le channel `fin`. La fonction `main` écrit des données dans le channel `work` et ferme le channel `work`. La fonction `process` imprimera le message si le channel `work` n'est pas fermé. Si le channel `work` est fermé, la fonction `process` imprimera un message et écrira les données dans le channel `fin`.

## Comment itérer sur les messages d'un Channel

Les channels peuvent être itérés en utilisant le mot-clé `range`, similaire aux `arrays, slice, et/ou maps`. Cela vous permet d'itérer rapidement et facilement sur les messages dans un channel.

Exemple :

```go
package main

import (
  "fmt"
)

func main() {
  c := make(chan string, 3)

  go func() {
    c <- "hello"
    c <- "world"
    c <- "goroutine"
    close(c) // Fermer le channel est très important avant de procéder à l'itération, sinon erreur de deadlock
  }()

  for msg := range c {
    fmt.Println(msg)
  }
}

```

L'exemple ci-dessus montre comment itérer sur un channel en utilisant le mot-clé `range`. Le channel `c` est créé avec une taille de tampon de 3. Le mot-clé `go` est utilisé pour créer une goroutine qui écrit des données dans le channel `c`. La fonction `main` itère sur le channel `c` en utilisant le mot-clé `range` et imprime le message.

## Conclusion

Dans cet article, nous avons appris comment gérer la concurrence avec les goroutines et les channels en Go. Nous avons appris comment créer des goroutines, et comment utiliser les `WaitGroups` et les channels pour communiquer entre les goroutines. 

Nous avons également appris comment utiliser les tampons de channel, les directions de channel, le `select` de channel, le timeout de channel, la fermeture de channel et la portée de channel. 

Les goroutines et les channels sont des fonctionnalités puissantes de Go qui aident à répondre aux exigences de concurrence et de flux asynchrone.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/destiny-erhabor) ou [Twitter](https://twitter.com/caesar_sage).