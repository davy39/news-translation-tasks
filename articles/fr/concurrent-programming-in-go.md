---
title: Programmation concurrente en Go – Goroutines, Canaux et plus expliqués avec
  des exemples
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-12-21T19:02:59.000Z'
originalURL: https://freecodecamp.org/news/concurrent-programming-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2022/12/2-1.png
tags:
- name: concurrency
  slug: concurrency
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Programmation concurrente en Go – Goroutines, Canaux et plus expliqués
  avec des exemples
seo_desc: "By Rwitesh Bera\nConcurrency refers to a programming language's ability\
  \ to deal with lots of things at once. \nA good way to understand concurrency is\
  \ by imagining multiple cars traveling on two lanes. Sometimes the cars overtake\
  \ each other, and someti..."
---

Par Rwitesh Bera

**Concurrency** fait référence à la capacité d'un langage de programmation à gérer de nombreuses choses à la fois. 

Une bonne façon de comprendre la concurrency est d'imaginer plusieurs voitures circulant sur deux voies. Parfois, les voitures se dépassent, et parfois elles s'arrêtent et laissent passer les autres. 

Un autre bon exemple est lorsque votre ordinateur exécute plusieurs tâches en arrière-plan comme la messagerie, le téléchargement de films, l'exécution du système d'exploitation, et ainsi de suite – tout cela en même temps. 


**Parallelism** signifie faire beaucoup de choses simultanément et indépendamment. Cela peut sembler similaire à la concurrency, mais c'est en réalité assez différent. 

Comprenons-le mieux avec le même exemple de trafic. Dans ce cas, les voitures circulent sur leur propre route sans se croiser. Chaque tâche est isolée de toutes les autres tâches. Les tâches concurrentes peuvent être exécutées dans n'importe quel ordre donné. 

C'est une manière non déterministe d'atteindre plusieurs choses à la fois. Les événements véritablement parallèles nécessitent plusieurs CPU.

![Image](https://www.freecodecamp.org/news/content/images/2022/12/1-1.png)
_Illustration montrant la différence entre le parallélisme et la concurrency_

## Qu'est-ce qu'une Goroutine ?
Une goroutine est une fonction indépendante qui s'exécute simultanément dans certains threads légers gérés par Go. GoLang la fournit pour soutenir la concurrency en Go.

Voici un exemple de ce à quoi ressemble une goroutine :

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go helloworld()
	time.Sleep(1 * time.Second)
	goodbye()
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
```

Dans cet exemple, d'abord, la goroutine `main` commence. Ensuite, elle invoque la fonction `helloworld()`, et la goroutine `helloworld` commence. 

Après que la goroutine `helloworld` ait terminé son opération, la goroutine `main` attend 1 seconde et invoque la fonction `goodbye()`. 

Si vous omettez la fonction `time` dans main, alors elle quittera avant que `helloworld()` ne termine son exécution. 

Comprenons les étapes impliquées ici :

1. La goroutine `main` commence
2. Invoque `helloworld` et la goroutine `helloworld` commence
3. Si il n'y a pas de pause en utilisant la méthode sleep, le `main` invoquera alors `goodbye()` et quittera avant que la goroutine `helloworld` ne termine son exécution.

Sans time.Sleep() :

```bash
$ go run HelloWorld.go 
Good Bye!
```

Après avoir ajouté time.Sleep(), la goroutine `helloworld` est capable de terminer son exécution avant que main ne quitte :

```bash
$ go run HelloWorld.go 
Hello World!
Good Bye!
```


### Qu'est-ce que les WaitGroups ?
Vous pouvez utiliser les WaitGroups pour attendre que plusieurs goroutines se terminent. Un WaitGroup bloque l'exécution d'une fonction jusqu'à ce que son compteur interne devienne 0. 

Regardons un simple extrait de code :

```go
package main

import (
	"fmt"
)

func main() {
	go helloworld()
	go goodbye()
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
``` 

Sortie
```bash
$ go run HelloWorld.go 

$
```

Si nous exécutons le programme ci-dessus, il n'imprime rien. Cela est dû au fait que la fonction main s'est terminée dès que ces deux goroutines ont commencé à s'exécuter. Nous pouvons donc utiliser `Sleep` qui pause l'exécution de la fonction main. Cela ressemble à ceci :

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	go helloworld()
	go goodbye()
	time.Sleep(2 * time.Second)
}

func helloworld() {
	fmt.Println("Hello World!")
}

func goodbye() {
	fmt.Println("Good Bye!")
}
```

Voici la sortie :

```bash
$ go run HelloWorld.go 
Good Bye!
Hello World!
```

Ici, la fonction `main` a été bloquée pendant 2 secondes et toutes les goroutines ont été exécutées avec succès. 

Bloquer la méthode pendant 2 secondes peut ne pas poser de problèmes. Mais au niveau de la production, où chaque milliseconde est vitale, des millions de requêtes concurrentes peuvent créer un énorme problème.

Vous pouvez résoudre ce problème en utilisant **sync.WaitGroup** comme ceci :

```go
package main

import (
	"fmt"
	"sync"
)

func main() {
	var wg sync.WaitGroup
	wg.Add(2)
	go helloworld(&wg)
	go goodbye(&wg)
	wg.Wait()
}

func helloworld(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println("Hello World!")
}

func goodbye(wg *sync.WaitGroup) {
	defer wg.Done()
	fmt.Println("Good Bye!")
}
```
Sortie
```bash
$ go run HelloWorld.go 
Good Bye!
Hello World!
```

La sortie est la même que la précédente, mais elle ne bloque pas le `main` pendant 2 secondes.

1. `wg.Add(int)` : Cette méthode indique le nombre de goroutines à attendre. Dans le code ci-dessus, j'ai fourni 2 pour 2 goroutines différentes. Par conséquent, le compteur d'attente interne devient 2.
2. `wg.Wait()` : Cette méthode bloque l'exécution du code jusqu'à ce que le compteur interne devienne 0.
3. `wg.Done()` : Cela réduira la valeur du compteur interne de 1.

**NOTE** : Si un WaitGroup est explicitement passé dans des fonctions, il doit être ajouté par un pointeur.

### Qu'est-ce que les Canaux ?
En programmation concurrente, Go fournit des canaux que vous pouvez utiliser pour la communication bidirectionnelle entre les goroutines. 

La communication bidirectionnelle signifie qu'une goroutine enverra un message et l'autre le lira. Les envois et les réceptions sont bloquants. L'exécution du code sera arrêtée jusqu'à ce que l'écriture et la lecture soient terminées avec succès. 

Les canaux sont l'une des manières les plus pratiques d'envoyer et de recevoir des notifications.

Il existe quelques types différents de canaux :

**Canal non tamponné** : Les canaux non tamponnés nécessitent que l'expéditeur et le destinataire soient présents pour que les opérations soient réussies. Il nécessite une goroutine pour lire les données, sinon, cela conduira à un blocage. Par défaut, les canaux ne sont pas tamponnés.

**Canal tamponné** : Les canaux tamponnés ont la capacité de stocker des valeurs pour un traitement futur. L'expéditeur n'est pas bloqué jusqu'à ce qu'il soit plein et il n'a pas nécessairement besoin d'un lecteur pour compléter la synchronisation avec chaque opération. 

Si un espace dans le tableau est disponible, l'expéditeur peut envoyer sa valeur au canal et compléter son opération d'envoi immédiatement. 

Après son exécution, si un destinataire arrive, le canal commencera à envoyer des valeurs au destinataire et il commencera son opération une fois qu'il aura reçu les valeurs. Comme l'expéditeur et le destinataire fonctionnent à des moments différents, cela s'appelle `communication asynchrone`. 

Voici un exemple :

```txt
Syntaxe pour déclarer un canal
ch := make(chan Type)
```
```txt
Déclaration des canaux basée sur les directions
1. Canal bidirectionnel : chan T
2. Canal d'envoi uniquement : chan <- T
3. Canal de réception uniquement : <- chan T
```

#### Comment écrire et lire depuis un canal
```go
package main

import (
	"fmt"
	"time"
)

func main() {
	msg := make(chan string)
	go greet(msg)
	time.Sleep(2 * time.Second)

	greeting := <-msg

	time.Sleep(2 * time.Second)
	fmt.Println("Salutation reçue")
	fmt.Println(greeting)
}

func greet(ch chan string) {
	fmt.Println("Greeter en attente d'envoyer la salutation !")

	ch <- "Hello Rwitesh"

	fmt.Println("Greeter terminé")
}
```

```bash
$ go run main.go 
Greeter en attente d'envoyer la salutation !
Greeter terminé
Salutation reçue
Hello Rwitesh
```

Dans l'extrait de code ci-dessus, `msg := make(chan string)` déclare un canal de type string. Ensuite, j'ai passé le canal dans la goroutine greet. `ch <-"Hello Rwitesh"` nous permet d'écrire le message dans `ch`.

Le `ch <-"Hello Rwitesh"` bloque l'exécution de la goroutine, car personne ne lit sa valeur écrite dans un canal. Donc dans la goroutine `main`, `time.Sleep(2 * time.Second)` termine l'exécution sans attendre `greet`. 

La deuxième instruction `time.Sleep(2* time.Second)` nous donne le temps de lire depuis le canal. Nous lisons depuis le canal en utilisant `<-msg`.

**Fermeture du canal** : La fermeture du canal indique qu'aucune autre valeur ne doit être envoyée sur celui-ci. Nous voulons montrer que le travail a été terminé et qu'il n'est pas nécessaire de garder un canal ouvert.

```go
package main

import (
	"fmt"
	"time"
)

func main() {
	msg := make(chan string)
	go greet(msg)

	time.Sleep(2 * time.Second)

	greeting := <-msg

	time.Sleep(2 * time.Second)
	fmt.Println("Salutation reçue")
	fmt.Println(greeting)

	_, ok := <-msg
	if ok {
		fmt.Println("Le canal est ouvert !")
	} else {
		fmt.Println("Le canal est fermé !")
	}
}

func greet(ch chan string) {
	fmt.Println("Greeter en attente d'envoyer la salutation !")

	ch <- "Hello Rwitesh"
	close(ch)

	fmt.Println("Greeter terminé")
}
```

Nous fermons un canal en utilisant `close()` comme `close(ch)` dans l'extrait de code ci-dessus.

```bash
$ go run main.go 
Greeter en attente d'envoyer la salutation !
Greeter terminé
Salutation reçue
Hello Rwitesh
Le canal est fermé !
```

## Conclusion

Récapitulons ce que nous avons appris : la concurrency en Go fait référence à la capacité d'effectuer plusieurs tâches simultanément, en utilisant des goroutines et des outils comme WaitGroups et des canaux pour synchroniser et communiquer entre eux. 

Les goroutines sont des threads légers d'exécution utilisés en Go pour soutenir la concurrency. Les WaitGroups sont utilisés pour attendre que plusieurs goroutines se terminent. Ils bloquent l'exécution d'une fonction jusqu'à ce que leur compteur interne devienne 0. 

Les canaux sont un moyen pour les goroutines de communiquer et peuvent être utilisés pour envoyer et recevoir des données entre les goroutines.

J'espère que vous avez trouvé ce tutoriel utile et informatif. Si vous avez apprécié le lire, je vous encourage à le partager avec vos amis et followers sur les réseaux sociaux.

N'oubliez pas de me suivre également sur [Twitter](https://twitter.com/RwiteshBera) pour plus de mises à jour sur le codage et la technologie. Merci d'avoir lu !