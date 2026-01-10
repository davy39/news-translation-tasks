---
title: Un million de WebSockets et Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-08-02T20:40:03.000Z'
originalURL: https://freecodecamp.org/news/million-websockets-and-go-cc58418460bb
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wLetcGEycR5rjU-q.jpeg
tags:
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Un million de WebSockets et Go
seo_desc: 'By Sergey Kamardin

  Hi everyone! My name is Sergey Kamardin and I’m a developer at Mail.Ru.

  This article is about how we developed the high-load WebSocket server with Go.

  If you are familiar with WebSockets, but know little about Go, I hope you will s...'
---

Par Sergey Kamardin

Bonjour à tous ! Je m'appelle Sergey Kamardin et je suis développeur chez Mail.Ru.

Cet article parle de la manière dont nous avons développé le serveur WebSocket haute charge avec Go.

Si vous êtes familier avec les WebSockets, mais que vous connaissez peu Go, j'espère que vous trouverez cet article intéressant en termes d'idées et de techniques pour l'optimisation des performances.

### 1. Introduction

Pour définir le contexte de notre histoire, quelques mots doivent être dits sur pourquoi nous avons besoin de ce serveur.

Mail.Ru possède de nombreux systèmes stateful. Le stockage des emails des utilisateurs en est un. Il existe plusieurs façons de suivre les changements d'état au sein d'un système et les événements du système. Principalement, cela se fait soit par sondage périodique du système, soit par des notifications du système sur ses changements d'état.

Les deux méthodes ont leurs avantages et inconvénients. Mais lorsqu'il s'agit de courrier, plus un utilisateur reçoit de nouveaux emails rapidement, mieux c'est.

Le sondage des emails implique environ 50 000 requêtes HTTP par seconde, dont 60 % retournent le statut 304, ce qui signifie qu'il n'y a pas de changements dans la boîte de réception.

Par conséquent, afin de réduire la charge sur les serveurs et d'accélérer la livraison des emails aux utilisateurs, la décision a été prise de réinventer la roue en écrivant un serveur publisher-subscriber (également connu sous le nom de bus, courtier de messages ou canal d'événements) qui recevrait les notifications sur les changements d'état d'une part, et les abonnements à de telles notifications d'autre part.

Auparavant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*TtT-WkAScOObNmkC8a8GRA.png)

Maintenant :

![Image](https://cdn-media-1.freecodecamp.org/images/1*dAYPDIPYh_D274DqZ3rnaw.png)

Le premier schéma montre à quoi cela ressemblait avant. Le navigateur sondait périodiquement l'API et demandait les changements de Storage (service de boîte de réception).

Le deuxième schéma décrit la nouvelle architecture. Le navigateur établit une connexion WebSocket avec l'API de notification, qui est un client du serveur Bus. À la réception d'un nouvel email, Storage envoie une notification à Bus (1), et Bus à ses abonnés (2). L'API détermine la connexion pour envoyer la notification reçue, et l'envoie au navigateur de l'utilisateur (3).

Ainsi, aujourd'hui nous allons parler de l'API ou du serveur WebSocket. En regardant vers l'avant, je vous dirai que le serveur aura environ 3 millions de connexions en ligne.

### 2. La manière idiomatique

Voyons comment nous pourrions implémenter certaines parties de notre serveur en utilisant les fonctionnalités de Go sans aucune optimisation.

Avant de procéder avec `net/http`, parlons de la manière dont nous allons envoyer et recevoir des données. Les données qui se trouvent _au-dessus_ du protocole WebSocket (par exemple, les objets JSON) seront désormais appelées _packets_.

Commençons à implémenter la structure `Channel` qui contiendra la logique d'envoi et de réception de tels packets via la connexion WebSocket.

### 2.1. Structure Channel

```go
// Packet représente les données au niveau de l'application.
type Packet struct {
    ...
}

// Channel enveloppe la connexion utilisateur.
type Channel struct {
    conn net.Conn    // Connexion WebSocket.
    send chan Packet // File d'attente des packets sortants.
}

func NewChannel(conn net.Conn) *Channel {
    c := &Channel{
        conn: conn,
        send: make(chan Packet, N),
    }

    go c.reader()
    go c.writer()

    return c
}
```

J'aimerais attirer votre attention sur le lancement de deux goroutines de lecture et d'écriture. Chaque goroutine nécessite sa propre pile de mémoire qui peut avoir une taille initiale de 2 à 8 Ko [selon le système d'exploitation](https://github.com/golang/go/blob/release-branch.go1.8/src/runtime/stack.go#L64-L82) et la version de Go.

Concernant le nombre mentionné de 3 millions de connexions en ligne, nous aurons besoin de **24 Go de mémoire** (avec une pile de 4 Ko) pour toutes les connexions. Et ce, sans la mémoire allouée pour la structure `Channel`, les packets sortants `ch.send` et autres champs internes.

### 2.2. Goroutines d'I/O

Examinons l'implémentation du "reader" :

```go
func (c *Channel) reader() {
    // Nous faisons une lecture tamponnée pour réduire les appels système read.
    buf := bufio.NewReader(c.conn)

    for {
        pkt, _ := readPacket(buf)
        c.handle(pkt)
    }
}
```

Ici, nous utilisons `bufio.Reader` pour réduire le nombre d'appels système `read()` et lire autant que permis par la taille du tampon `buf`. Dans la boucle infinie, nous attendons de nouvelles données. Souvenez-vous de ces mots : _attendre de nouvelles données_. Nous y reviendrons plus tard.

Nous laisserons de côté l'analyse et le traitement des packets entrants, car ce n'est pas important pour les optimisations dont nous allons parler. Cependant, `buf` mérite notre attention maintenant : par défaut, il est de 4 Ko, ce qui signifie **12 Go** supplémentaires de mémoire pour nos connexions. Il en va de même pour le "writer" :

```go
func (c *Channel) writer() {
    // Nous faisons une écriture tamponnée pour réduire les appels système write.
    buf := bufio.NewWriter(c.conn)

    for pkt := range c.send {
        _ := writePacket(buf, pkt)
        buf.Flush()
    }
}
```

Nous itérons à travers le canal des packets sortants `c.send` et les écrivons dans le tampon. Comme nos lecteurs attentifs peuvent déjà le deviner, c'est encore 4 Ko et **12 Go** de mémoire pour nos 3 millions de connexions.

### 2.3. HTTP

Nous avons déjà une implémentation simple de `Channel`, maintenant nous devons obtenir une connexion WebSocket pour travailler avec. Comme nous sommes toujours sous le titre _Idiomatic Way_, faisons-le de la manière correspondante.

> _Note : Si vous ne savez pas comment fonctionne WebSocket, il faut mentionner que le client passe au protocole WebSocket au moyen d'un mécanisme HTTP spécial appelé Upgrade. Après le traitement réussi d'une requête Upgrade, le serveur et le client utilisent la connexion TCP pour échanger des trames WebSocket binaires. [Voici](https://tools.ietf.org/html/rfc6455#section-5.2) une description de la structure de la trame à l'intérieur de la connexion._

```go
import (
    "net/http"
    "some/websocket"
)

http.HandleFunc("/v1/ws", func(w http.ResponseWriter, r *http.Request) {
    conn, _ := websocket.Upgrade(r, w)
    ch := NewChannel(conn)
    //...
})
```

Veuillez noter que `http.ResponseWriter` effectue une allocation de mémoire pour `bufio.Reader` et `bufio.Writer` (tous deux avec un tampon de 4 Ko) pour l'initialisation de `*http.Request` et l'écriture de la réponse.

Indépendamment de la bibliothèque WebSocket utilisée, après une réponse réussie à la requête Upgrade, le [serveur reçoit](https://github.com/golang/go/blob/143bdc27932451200f3c8f4b304fe92ee8bba9be/src/net/http/server.go#L1862-L1869) les tampons I/O avec la connexion TCP après l'appel `responseWriter.Hijack()`.

> _Astuce : dans certains cas, `go:linkname` peut être utilisé pour retourner les tampons au `sync.Pool` à l'intérieur de `net/http` via l'appel `net/http.putBufio{Reader,Writer}`._

Ainsi, nous avons besoin de **24 Go** supplémentaires de mémoire pour 3 millions de connexions.

Donc, un total de **72 Go** de mémoire pour l'application qui ne fait encore rien !

### 3. Optimisations

Rappelons ce dont nous avons parlé dans la partie introduction et souvenons-nous du comportement d'une connexion utilisateur. Après être passé à WebSocket, le client envoie un packet avec les événements pertinents ou, en d'autres termes, s'abonne à des événements. Ensuite (sans prendre en compte les messages techniques tels que `ping/pong`), le client peut ne plus rien envoyer pendant toute la durée de vie de la connexion.

> _La durée de vie de la connexion peut durer de quelques secondes à plusieurs jours._

Ainsi, la plupart du temps, nos `Channel.reader()` et `Channel.writer()` attendent le traitement des données pour la réception ou l'envoi. Avec eux, les tampons I/O de 4 Ko chacun attendent également.

Maintenant, il est clair que certaines choses pourraient être faites mieux, n'est-ce pas ?

### 3.1. Netpoll

Vous souvenez-vous de l'implémentation de `Channel.reader()` qui _attendait de nouvelles données_ en se verrouillant sur l'appel `conn.Read()` à l'intérieur de `bufio.Reader.Read()` ? Si des données étaient présentes dans la connexion, le runtime Go "réveillait" notre goroutine et lui permettait de lire le prochain packet. Après cela, la goroutine se verrouillait à nouveau en attendant de nouvelles données. Voyons comment le runtime Go comprend que la goroutine doit être "réveillée".

Si nous regardons l'[implémentation de conn.Read()](https://github.com/golang/go/blob/release-branch.go1.8/src/net/net.go#L176-L186), nous verrons l'appel [net.netFD.Read()](https://github.com/golang/go/blob/release-branch.go1.8/src/net/fd_unix.go#L245-L257) à l'intérieur :

```go
// net/fd_unix.go

func (fd *netFD) Read(p []byte) (n int, err error) {
    //...
    for {
        n, err = syscall.Read(fd.sysfd, p)
        if err != nil {
            n = 0
            if err == syscall.EAGAIN {
                if err = fd.pd.waitRead(); err == nil {
                    continue
                }
            }
        }
        //...
        break
    }
    //...
}
```

> _Go utilise les sockets en mode non bloquant. EAGAIN indique qu'il n'y a pas de données dans le socket et pour ne pas se bloquer sur la lecture du socket vide, l'OS nous retourne le contrôle._

Nous voyons un appel système `read()` à partir du descripteur de fichier de connexion. Si read retourne l'[erreur EAGAIN](http://man7.org/linux/man-pages/man2/read.2.html#ERRORS), le runtime fait l'appel [pollDesc.waitRead()](https://github.com/golang/go/blob/release-branch.go1.8/src/net/fd_poll_runtime.go#L74-L81) :

```go
// net/fd_poll_runtime.go

func (pd *pollDesc) waitRead() error {
   return pd.wait('r')
}

func (pd *pollDesc) wait(mode int) error {
   res := runtime_pollWait(pd.runtimeCtx, mode)
   //...
}
```

Si nous [creusons plus profond](https://github.com/golang/go/blob/143bdc27932451200f3c8f4b304fe92ee8bba9be/src/runtime/netpoll.go#L14-L20), nous verrons que netpoll est implémenté en utilisant [epoll](http://man7.org/linux/man-pages/man7/epoll.7.html) sous Linux et [kqueue](https://www.freebsd.org/cgi/man.cgi?query=kqueue&sektion=2) sous BSD. Pourquoi ne pas utiliser la même approche pour nos connexions ? Nous pourrions allouer un tampon de lecture et démarrer la goroutine de lecture uniquement lorsque cela est vraiment nécessaire : lorsque des données lisibles sont réellement présentes dans le socket.

> _Sur github.com/golang/go, il y a le [problème](https://github.com/golang/go/issues/15735#issuecomment-266574151) de l'exportation des fonctions netpoll._

### 3.2. Se débarrasser des goroutines

Supposons que nous avons une [implémentation netpoll](https://godoc.org/github.com/mailru/easygo/netpoll) pour Go. Maintenant, nous pouvons éviter de démarrer la goroutine `Channel.reader()` avec le tampon interne, et nous abonner à l'événement de données lisibles dans la connexion :

```go
ch := NewChannel(conn)

// Faire en sorte que conn soit observé par l'instance netpoll.
poller.Start(conn, netpoll.EventRead, func() {
    // Nous lançons une goroutine ici pour empêcher la boucle d'attente du poller
    // de se bloquer pendant la réception du packet de ch.
    go Receive(ch)
})

// Receive lit un packet de conn et le traite d'une manière ou d'une autre.
func (ch *Channel) Receive() {
    buf := bufio.NewReader(ch.conn)
    pkt := readPacket(buf)
    c.handle(pkt)
}
```

C'est plus simple avec `Channel.writer()` car nous pouvons exécuter la goroutine et allouer le tampon uniquement lorsque nous allons envoyer le packet :

```go
func (ch *Channel) Send(p Packet) {
    if c.noWriterYet() {
        go ch.writer()
    }
    ch.send <- p
}
```

> _Notez que nous ne traitons pas les cas où le système d'exploitation retourne `EAGAIN` sur les appels système `write()`. Nous nous appuyons sur le runtime Go pour de tels cas, car c'est effectivement rare pour ce type de serveurs. Néanmoins, cela pourrait être traité de la même manière si nécessaire._

Après avoir lu les packets sortants de `ch.send` (un ou plusieurs), le writer terminera son opération et libérera la pile de la goroutine et le tampon d'envoi.

Parfait ! Nous avons économisé **48 Go** en nous débarrassant de la pile et des tampons I/O à l'intérieur de deux goroutines en cours d'exécution en continu.

### 3.3. Contrôle des ressources

Un grand nombre de connexions implique non seulement une consommation élevée de mémoire. Lors du développement du serveur, nous avons rencontré des conditions de course répétées et des interblocages souvent suivis par le soi-disant self-DDoS — une situation où les clients de l'application tentaient frénétiquement de se connecter au serveur, le cassant ainsi encore plus.

Par exemple, si pour une raison quelconque nous ne pouvions soudainement plus traiter les messages `ping/pong`, mais que le gestionnaire de connexions inactives continuait à fermer de telles connexions (supposant que les connexions étaient rompues et ne fournissaient donc aucune donnée), le client semblait perdre la connexion toutes les N secondes et essayait de se reconnecter au lieu d'attendre des événements.

Il serait idéal si le serveur verrouillé ou surchargé arrêtait simplement d'accepter de nouvelles connexions, et que le répartiteur devant lui (par exemple, nginx) transmettait la requête à l'instance de serveur suivante.

De plus, indépendamment de la charge du serveur, si tous les clients veulent soudainement nous envoyer un packet pour une raison quelconque (probablement à cause d'un bug), les **48 Go** précédemment économisés seront à nouveau utiles, car nous reviendrons effectivement à l'état initial de la goroutine et du tampon pour chaque connexion.

#### Pool de goroutines

Nous pouvons limiter le nombre de packets traités simultanément en utilisant un pool de goroutines. Voici à quoi ressemble une implémentation naïve d'un tel pool :

```go
package gopool

func New(size int) *Pool {
    return &Pool{
        work: make(chan func()),
        sem:  make(chan struct{}, size),
    }
}

func (p *Pool) Schedule(task func()) error {
    select {
    case p.work <- task:
    case p.sem <- struct{}{}:
        go p.worker(task)
    }
}

func (p *Pool) worker(task func()) {
    defer func() { <-p.sem }
    for {
        task()
        task = <-p.work
    }
}
```

Maintenant, notre code avec `netpoll` ressemble à ceci :

```go
pool := gopool.New(128)

poller.Start(conn, netpoll.EventRead, func() {
    // Nous allons bloquer la boucle d'attente du poller lorsque
    // tous les workers du pool sont occupés.
    pool.Schedule(func() {
        Receive(ch)
    })
})
```

Ainsi, maintenant nous lisons le packet non seulement lors de l'apparition de données lisibles dans le socket, mais aussi lors de la première opportunité de prendre la goroutine libre dans le pool.

De même, nous modifierons `Send()` :

```go
pool := gopool.New(128)

func (ch *Channel) Send(p Packet) {
    if c.noWriterYet() {
        pool.Schedule(ch.writer)
    }
    ch.send <- p
}
```

Au lieu de `go ch.writer()`, nous voulons écrire dans l'une des goroutines réutilisées. Ainsi, pour un pool de `N` goroutines, nous pouvons garantir qu'avec `N` requêtes traitées simultanément et la `N + 1` arrivée, nous n'allouerons pas de tampon `N + 1` pour la lecture. Le pool de goroutines nous permet également de limiter `Accept()` et `Upgrade()` des nouvelles connexions et d'éviter la plupart des situations de DDoS.

### 3.4. Zero-copy upgrade

Écartons-nous un peu du protocole WebSocket. Comme cela a déjà été mentionné, le client passe au protocole WebSocket en utilisant une requête HTTP Upgrade. Voici à quoi cela ressemble :

```http
GET /ws HTTP/1.1
Host: mail.ru
Connection: Upgrade
Sec-Websocket-Key: A3xNe7sEB9HixkmBhVrYaA==
Sec-Websocket-Version: 13
Upgrade: websocket

HTTP/1.1 101 Switching Protocols
Connection: Upgrade
Sec-Websocket-Accept: ksu0wXWG+YmkVx+KQR2agP0cQn4=
Upgrade: websocket
```

C'est-à-dire que dans notre cas, nous avons besoin de la requête HTTP et de ses en-têtes uniquement pour passer au protocole WebSocket. Cette connaissance et [ce qui est stocké](https://github.com/golang/go/blob/release-branch.go1.8/src/net/http/request.go#L100-L305) à l'intérieur de `http.Request` suggère que pour le bien de l'optimisation, nous pourrions probablement refuser les allocations et les copies inutiles lors du traitement des requêtes HTTP et abandonner le serveur standard `net/http`.

> _Par exemple, `http.Request` contient un [champ avec le type Header du même nom](https://github.com/golang/go/blob/release-branch.go1.8/src/net/http/header.go#L19) qui est rempli sans condition avec tous les en-têtes de la requête en copiant les données de la connexion vers les chaînes de valeurs. Imaginez combien de données supplémentaires pourraient être conservées à l'intérieur de ce champ, par exemple pour un en-tête Cookie de grande taille._

Mais que prendre en retour ?

#### Implémentation WebSocket

Malheureusement, toutes les bibliothèques existantes au moment de l'optimisation de notre serveur nous permettaient de faire l'upgrade uniquement pour le serveur standard `net/http`. De plus, aucune des (deux) bibliothèques ne permettait d'utiliser toutes les optimisations de lecture et d'écriture mentionnées ci-dessus. Pour que ces optimisations fonctionnent, nous devons avoir une API de plutôt bas niveau pour travailler avec WebSocket. Pour réutiliser les tampons, nous avons besoin que les fonctions de protocole ressemblent à ceci :

```go
func ReadFrame(io.Reader) (Frame, error)
func WriteFrame(io.Writer, Frame) error
```

Si nous avions une bibliothèque avec une telle API, nous pourrions lire les packets de la connexion comme suit (l'écriture des packets serait similaire) :

```go
// getReadBuf, putReadBuf sont destinés à
// réutiliser *bufio.Reader (avec sync.Pool par exemple).
func getReadBuf(io.Reader) *bufio.Reader
func putReadBuf(*bufio.Reader)

// readPacket doit être appelé lorsque des données peuvent être lues depuis conn.
func readPacket(conn io.Reader) error {
    buf := getReadBuf()
    defer putReadBuf(buf)

    buf.Reset(conn)
    frame, _ := ReadFrame(buf)
    parsePacket(frame.Payload)
    //...
}
```

En bref, il était temps de créer notre propre bibliothèque.

#### github.com/gobwas/ws

Idéologiquement, la bibliothèque `ws` a été écrite de manière à ne pas imposer sa logique de fonctionnement du protocole aux utilisateurs. Toutes les méthodes de lecture et d'écriture acceptent les interfaces standard `io.Reader` et `io.Writer`, ce qui permet d'utiliser ou non la mise en tampon ou tout autre wrapper I/O.

En plus des requêtes d'upgrade du `net/http` standard, `ws` supporte le **zero-copy upgrade**, le traitement des requêtes d'upgrade et le passage à WebSocket sans allocations de mémoire ni copies. `ws.Upgrade()` accepte `io.ReadWriter` (`net.Conn` implémente cette interface). En d'autres termes, nous pourrions utiliser le `net.Listen()` standard et transférer la connexion reçue de `ln.Accept()` immédiatement à `ws.Upgrade()`. La bibliothèque permet de copier toutes les données de requête pour une utilisation future dans l'application (par exemple, `Cookie` pour vérifier la session).

Ci-dessous se trouvent les [benchmarks](https://github.com/gobwas/ws/blob/f9c54e121bd17f7e6b9b283bd0299d19149f270b/server_test.go#L397-L464) du traitement des requêtes Upgrade : serveur `net/http` standard versus `net.Listen()` avec zero-copy upgrade :

```http
BenchmarkUpgradeHTTP    5156 ns/op    8576 B/op    9 allocs/op
BenchmarkUpgradeTCP     973 ns/op     0 B/op       0 allocs/op
```

Le passage à `ws` et au **zero-copy upgrade** nous a fait économiser **24 Go** supplémentaires — l'espace alloué pour les tampons I/O lors du traitement de la requête par le gestionnaire `net/http`.

### 3.5. Résumé

Structurons les optimisations dont je vous ai parlé.

* Une goroutine de lecture avec un tampon à l'intérieur est coûteuse. **Solution** : netpoll (epoll, kqueue) ; réutiliser les tampons.
* Une goroutine d'écriture avec un tampon à l'intérieur est coûteuse. **Solution** : démarrer la goroutine lorsque nécessaire ; réutiliser les tampons.
* Avec une tempête de connexions, netpoll ne fonctionnera pas. **Solution** : réutiliser les goroutines avec une limite sur leur nombre.
* `net/http` n'est pas le moyen le plus rapide de gérer l'Upgrade vers WebSocket. **Solution** : utiliser le zero-copy upgrade sur une connexion TCP nue.

Voici à quoi pourrait ressembler le code du serveur :

```go
import (
    "net"
    "github.com/gobwas/ws"
)

ln, _ := net.Listen("tcp", ":8080")

for {
    // Essayer d'accepter la connexion entrante à l'intérieur d'un worker de pool libre.
    // Si aucun worker libre pendant 1ms, ne rien accepter et réessayer plus tard.
    // Cela nous aidera à prévenir de nombreux cas de self-ddos ou de dépassement de la limite des ressources.
    err := pool.ScheduleTimeout(time.Millisecond, func() {
        conn := ln.Accept()
        _ = ws.Upgrade(conn)

        // Envelopper la connexion WebSocket avec notre structure Channel.
        // Cela nous aidera à gérer/envoyer les packets de notre application.
        ch := NewChannel(conn)

        // Attendre les octets entrants de la connexion.
        poller.Start(conn, netpoll.EventRead, func() {
            // Ne pas dépasser les limites des ressources.
            pool.Schedule(func() {
                // Lire et traiter le(s) packet(s) entrant(s).
                ch.Recevie()
            })
        })
    })
    if err != nil {   
        time.Sleep(time.Millisecond)
    }
}
```

### 4. Conclusion

> _L'optimisation prématurée est la racine de tous les maux (ou au moins de la plupart) en programmation. Donald Knuth_

Bien sûr, les optimisations ci-dessus sont pertinentes, mais pas dans tous les cas. Par exemple, si le ratio entre les ressources libres (mémoire, CPU) et le nombre de connexions en ligne est plutôt élevé, il n'y a probablement pas de sens à optimiser. Cependant, vous pouvez tirer grand profit de savoir où et quoi améliorer.

Merci pour votre attention !

### 5. Références

* [https://github.com/mailru/easygo](https://github.com/mailru/easygo)
* [https://github.com/gobwas/ws](https://github.com/gobwas/ws)
* [https://github.com/gobwas/ws-examples](https://github.com/gobwas/ws-examples)
* [https://github.com/gobwas/httphead](https://github.com/gobwas/httphead)
* [Version russe de cet article](https://habrahabr.ru/company/mailru/blog/331784/)