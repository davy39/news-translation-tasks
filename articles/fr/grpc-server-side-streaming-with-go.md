---
title: Comment configurer le streaming côté serveur gRPC avec Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-20T00:21:08.000Z'
originalURL: https://freecodecamp.org/news/grpc-server-side-streaming-with-go
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5fb5449249c47664ed8226c5.jpg
tags:
- name: Go Language
  slug: go
seo_title: Comment configurer le streaming côté serveur gRPC avec Go
seo_desc: "By Pramono Winata\nHave you ever thought about returning multiple server\
  \ responses using only a single connection? Yes, that’s what this article is about.\
  \ \nToday I will be showing you how to implement gRPC server-side streaming with\
  \ Go.\n\nIt's okay, he..."
---

Par Pramono Winata

Avez-vous déjà pensé à retourner plusieurs réponses serveur en utilisant une seule connexion ? Oui, c'est ce dont parle cet article. 

Aujourd'hui, je vais vous montrer comment implémenter le streaming côté serveur gRPC avec Go.

![Image](https://www.freecodecamp.org/news/content/images/2020/11/7f6189eec678dc80b34e16ec51aa6133dcab12e3-1-.png)
_C'est bon, il ne mordra pas_

Avant de passer directement à l'implémentation, couvrons ce que nous allons apprendre. Si vous avez cliqué sur cet article, vous connaissez peut-être déjà gRPC. Mais si vous avez cliqué par curiosité, ne vous inquiétez pas – je vais vous donner une brève introduction à gRPC dans un instant.

Et si vous ne savez pas grand-chose sur le streaming côté serveur non plus, ce n'est pas grave. Je vais aussi couvrir cela ci-dessous.

Enfin, si vous vous demandez ce qu'est Go, la réponse rapide est que c'est un langage de programmation. Je ne vais pas le couvrir ici, mais vous pouvez en lire plus sur Go dans [sa documentation officielle ici](https://golang.org/) avant de continuer.

Dans cet article, je commencerai par décrire gRPC et le streaming côté serveur. 
Si vous avez déjà une idée de ce que sont ces deux concepts, n'hésitez pas à sauter les deux premières sections ci-dessous.

## Qu'est-ce que gRPC ?

![Image](https://www.freecodecamp.org/news/content/images/2020/11/index-1.png)

Avez-vous déjà rêvé d'appeler une requête serveur avec un appel de fonction ? Au lieu d'utiliser un appel HTTP avec une URL ? Eh bien, cela existe déjà depuis quelque temps – et nous l'appelons [Remote Procedure Call](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/).

Et en 2015, Google a introduit quelque chose appelé gRPC, qui est essentiellement un Remote Procedure Call sur stéroïdes. 

Il fonctionne presque de la même manière qu'un Remote Procedure Call traditionnel. Mais Google a introduit l'utilisation de HTTP/2 comme protocole de communication et protobuf comme contrat de communication entre le serveur et le client.

HTTP/2 a également été créé par Google et permet une communication beaucoup plus performante. Il permet également le multiplexage, dont je parlerai plus tard.

Protobuf est essentiellement le contrat utilisé pour permettre la communication entre le serveur et le client via un appel de fonction.

D'accord, c'est un aperçu de base de gRPC. Si vous êtes toujours intéressé et souhaitez approfondir, vous pouvez en lire plus en détail à ce sujet [ici](https://www.freecodecamp.org/news/what-is-grpc-protocol-buffers-stream-architecture/).

## Qu'est-ce que le streaming côté serveur ?

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-269.png)
_Photo par [Unsplash](https://unsplash.com/@jonflobrant?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Jon Flobrant</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

Et maintenant, qu'en est-il du streaming côté serveur ?

Par conception, gRPC utilise HTTP/2 et prend en charge quelque chose appelé multiplexage. Je ne vais pas entrer dans trop de détails ici, mais il permet à une seule requête d'avoir plusieurs réponses, et vice versa. 

Ce mécanisme est implémenté dans gRPC et il est appelé streaming.

Il existe 3 types de streaming :

* Streaming côté client : où le client aura plusieurs requêtes et le serveur ne retournera qu'une seule réponse.
* Streaming bidirectionnel : où le client et le serveur peuvent avoir plusieurs requêtes et réponses ensemble dans une seule connexion.
* Streaming côté serveur : où le client envoie une seule requête et le serveur peut retourner plusieurs réponses ensemble. C'est celui que je vais vous montrer comment implémenter aujourd'hui.

## Comment implémenter le streaming côté serveur

![Image](https://www.freecodecamp.org/news/content/images/2021/04/image-270.png)
_Photo par [Unsplash](https://unsplash.com/@camadams?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit">Cam Adams</a> / <a href="https://unsplash.com/?utm_source=ghost&amp;utm_medium=referral&amp;utm_campaign=api-credit)_

C'est l'heure de l'implémentation ! Si vous lisez cette section, je suppose que vous connaissez déjà ces trois choses :

* gRPC
* Streaming côté serveur
* Go

Le streaming côté serveur est particulièrement utile si votre serveur doit retourner une charge utile volumineuse. 

En utilisant le streaming, vous pouvez diviser ces réponses et les retourner une par une. Le client pourra couper les réponses inutilisées s'il a déjà suffisamment de réponses, ou s'il a attendu trop longtemps pour certaines réponses.

D'accord, passons directement au code.

### Créer le fichier Proto

Pour commencer, nous devrons définir notre fichier protobuf qui sera utilisé par le client et le serveur. Faisons-en un simple ici, comme ceci :

```proto
syntax = "proto3";

package protobuf;

service StreamService {
  rpc FetchResponse (Request) returns (stream Response) {}
}

message Request {
  int32 id = 1;
}

message Response {
  string result = 1;
}
```

Ce fichier proto contient essentiellement un seul appel de fonction avec un paramètre `Request` et retourne un flux de `Response`.

Avant de continuer, nous devons également générer notre fichier `pb` qui sera utilisé par notre programme Go. Chaque langage de programmation aura une manière différente de générer le fichier de buffer de protocole. En Go, nous utiliserons la bibliothèque `protoc`. 

Si vous ne l'avez pas encore installée, Google fournit le [guide d'installation pour cela ici](https://developers.google.com/protocol-buffers/docs/reference/go-generated).

Générons le fichier de buffer de protocole en exécutant la commande suivante :  
`protoc --go_out=plugins=grpc:. *.proto`   

Et maintenant nous avons `data.pb.go` prêt à être utilisé.

### Créer le fichier Client

Pour l'étape suivante, vous pouvez créer soit le fichier client soit le fichier serveur, dans n'importe quel ordre. Mais dans cet exemple, je vais d'abord créer le fichier client.

```go
package main

import (
	"context"
	"io"
	"log"

	pb "github.com/pramonow/go-grpc-server-streaming-example/src/proto"

	"google.golang.org/grpc"
)

func main() {
	// composer le serveur
	conn, err := grpc.Dial(":50005", grpc.WithInsecure())
	if err != nil {
		log.Fatalf("impossible de se connecter au serveur %v", err)
	}

	// créer un flux
	client := pb.NewStreamServiceClient(conn)
	in := &pb.Request{Id: 1}
	stream, err := client.FetchResponse(context.Background(), in)
	if err != nil {
		log.Fatalf("erreur d'ouverture de flux %v", err)
	}

	done := make(chan bool)

	go func() {
		for {
			resp, err := stream.Recv()
			if err == io.EOF {
				done <- true // signifie que le flux est terminé
				return
			}
			if err != nil {
				log.Fatalf("impossible de recevoir %v", err)
			}
			log.Printf("Réponse reçue : %s", resp.Result)
		}
	}()

	<-done // nous attendrons jusqu'à ce que toutes les réponses soient reçues
	log.Printf("terminé")
}
```

Le client sera essentiellement celui qui envoie la requête. Il sera également celui qui reçoit plusieurs réponses.

Le client appellera la méthode gRPC `FetchResponse` et attendra toutes les réponses. J'utilise une `goroutine` ici pour montrer la possibilité de concurrence. Et j'utilise un `channel` afin d'attendre que tous les processus soient terminés avant de quitter le programme.

### Créer le fichier Serveur

Pour le troisième et dernier fichier, nous allons créer le fichier serveur. Ce fichier recevra la réponse du client et enverra en retour un flux de réponses au client.

```go
package main

import (
	"fmt"
	"log"
	"net"
	"sync"
	"time"

	pb "github.com/pramonow/go-grpc-server-streaming-example/src/proto"

	"google.golang.org/grpc"
)

type server struct{}

func (s server) FetchResponse(in *pb.Request, srv pb.StreamService_FetchResponseServer) error {

	log.Printf("récupération de la réponse pour l'id : %d", in.Id)

  	// utiliser wait group pour permettre au processus d'être concurrent
	var wg sync.WaitGroup
	for i := 0; i < 5; i++ {
		wg.Add(1)
		go func(count int64) {
			defer wg.Done()
      
      			// temps de sommeil pour simuler le temps de traitement du serveur
			time.Sleep(time.Duration(count) * time.Second)
			resp := pb.Response{Result: fmt.Sprintf("Requête #%d Pour Id:%d", count, in.Id)}
			if err := srv.Send(&resp); err != nil {
				log.Printf("erreur d'envoi %v", err)
			}
			log.Printf("fin de la requête numéro : %d", count)
		}(int64(i))
	}

	wg.Wait()
	return nil
}

func main() {
	// créer un écouteur
	lis, err := net.Listen("tcp", ":50005")
	if err != nil {
		log.Fatalf("échec de l'écoute : %v", err)
	}

	// créer un serveur grpc
	s := grpc.NewServer()
	pb.RegisterStreamServiceServer(s, server{})

	log.Println("démarrage du serveur")
	// et démarrer...
	if err := s.Serve(lis); err != nil {
		log.Fatalf("échec du service : %v", err)
	}

}
```

Dans le fichier serveur, j'utilise également une `goroutine` pour simuler un processus concurrent. 
Pour chacune des requêtes, je vais envoyer cinq requêtes en flux vers le client. Chacune aura également un temps de traitement différent afin de simuler les différents temps de traitement que vous auriez dans un scénario réel.

### Le résultat

Maintenant vient la partie excitante. Construisons notre fichier client et serveur avec `go build` pour obtenir notre fichier binaire. Ensuite, nous ouvrirons deux commandes de console séparées pour l'exécuter.

**Juste une petite note** : vous devez démarrer le serveur avant le client puisque le client va directement invoquer la méthode du serveur.

Alors, allons dans le répertoire de chacun de nos fichiers binaires et exécutons les deux avec `/.server` et `./client`.

Votre client affichera ceci :

```
2020/11/10 22:26:11 Réponse reçue : Requête #0 Pour Id:1
2020/11/10 22:26:12 Réponse reçue : Requête #1 Pour Id:1
2020/11/10 22:26:13 Réponse reçue : Requête #2 Pour Id:1
2020/11/10 22:26:14 Réponse reçue : Requête #3 Pour Id:1
2020/11/10 22:26:15 Réponse reçue : Requête #4 Pour Id:1
2020/11/10 22:26:15 terminé
```

Et le serveur affichera ceci :

```
2020/11/10 22:26:09 démarrage du serveur
2020/11/10 22:26:11 récupération de la réponse pour l'id : 1
2020/11/10 22:26:11 fin de la requête numéro : 0
2020/11/10 22:26:12 fin de la requête numéro : 1
2020/11/10 22:26:13 fin de la requête numéro : 2
2020/11/10 22:26:14 fin de la requête numéro : 3
2020/11/10 22:26:15 fin de la requête numéro : 4
```

Si tout se passe bien, vous avez réussi à construire un service de streaming côté serveur gRPC avec Go ! Si vous avez besoin du code GitHub pour l'exemple complet, vous pouvez le trouver [ici](https://github.com/pramonow/go-grpc-server-streaming-example).

## Conclusion

J'espère que cet exemple de la façon d'implémenter le streaming côté serveur gRPC avec Go vous a aidé à comprendre le processus. 

Cette implémentation peut ne pas être très courante, et vous n'aurez peut-être même pas besoin de ce type d'implémentation complexe dans votre projet. Mais pensez-y comme un outil pour élever votre projet encore plus.

Si vous voulez en apprendre plus, consultez ces autres concepts intéressants tels que le streaming côté client ou même le streaming bidirectionnel. J'ai trouvé l'exemple [ici](https://github.com/pahanini/go-grpc-bidirectional-streaming-example) assez bon.

Merci d'avoir lu mon article jusqu'à la fin ! J'espère vraiment que vous avez appris quelque chose de nouveau et d'utile aujourd'hui. Comme je l'ai dit, vous n'en aurez peut-être pas vraiment besoin, mais pourquoi ne pas essayer ?

> Ne attendez pas le changement, prenez l'initiative et soyez le catalyseur du changement.