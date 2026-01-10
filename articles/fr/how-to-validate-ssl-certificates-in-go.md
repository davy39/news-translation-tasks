---
title: Comment valider les certificats SSL en Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-11-03T20:11:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-validate-ssl-certificates-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2020/11/S3MQd1604428653.png
tags:
- name: golang
  slug: golang
- name: information security
  slug: information-security
- name: Security
  slug: security
- name: SSL
  slug: ssl
seo_title: Comment valider les certificats SSL en Go
seo_desc: 'By Umesh Yadav

  Recently, I came across a SaaS product that validates SSL certificates for your
  website. I wanted to try writing the same thing in Go – and it turns out that it''s
  pretty straightforward (just 17 lines of code).

  You will need to perform...'
---

Par Umesh Yadav

Récemment, je suis tombé sur un produit SaaS qui valide les certificats SSL pour votre site web. J'ai voulu essayer d'écrire la même chose en Go – et il s'avère que c'est assez simple (seulement 17 lignes de code).

Vous devrez effectuer trois vérifications principales sur votre site web.

1. Tout d'abord, vérifiez si votre site possède un certificat SSL ou non. Vous devrez également savoir si votre site web utilise un certificat SSL auto-signé qui n'est pas considéré comme un certificat valide (il doit être signé par une autorité de certification).
2. Ensuite, vérifiez si le certificat SSL a le bon nom d'hôte.
3. Et enfin, vous devez connaître la date d'expiration du certificat du serveur.

Prérequis :

* Vous devez avoir `go` installé sur votre ordinateur.

### Étape 1 : Vérifier si votre site web possède un certificat SSL

Tout d'abord, nous allons essayer de vérifier si le site web possède un certificat SSL ou non.

Pour cela, nous devons établir une connexion TLS avec le site web. Si cela réussit, cela signifie que le site web possède un certificat TLS valide.

Pour établir une connexion TLS, nous pouvons utiliser le package `crypto/tls` de Go. Nous utiliserons la méthode `Dial` pour nous connecter au site web, comme ceci :

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "example.com:80", nil)
	if err != nil {
		panic("Le serveur ne supporte pas le certificat SSL err: " + err.Error())
	}
}

```

Nous allons essayer d'exécuter notre test sur `example.com`. Lorsque vous exécutez le code ci-dessus, vous devriez obtenir l'erreur suivante :

```
$ go run main.go
panic: Le serveur ne supporte pas le certificat SSL err: tls: premier enregistrement ne ressemble pas à une poignée de main TLS

goroutine 1 [running]:
main.main()
        /Users/umesh/personal/spike/main.go:99 +0x2ca
exit status 2

```

En gros, il a essayé d'établir la connexion mais a échoué. La méthode `Dial` ne réussit que lorsque le site web possède un certificat valide (elle échouera si le certificat est auto-signé).

Maintenant, essayez le même code sur un site web qui a SSL activé. J'utilise l'URL de mon propre site web comme exemple :

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Le serveur ne supporte pas le certificat SSL err: " + err.Error())
	}
}

```

Cette fois, nous devrions pouvoir établir la connexion avec succès sans que le code ne panique.

En production, vous ne devriez pas utiliser panic, mais plutôt gérer l'erreur de manière élégante.

### Étape 2 : Vérifier si le certificat SSL et le nom d'hôte du site web correspondent

Pour vérifier le nom d'hôte, nous devrons appeler `VerifyHostname` sur le `conn` retourné par `Dial`. Cette méthode essaie de faire correspondre le nom commun ou le nom alternatif du sujet spécifié dans le certificat avec le domaine passé en paramètre.

```go
package main

import (
	"crypto/tls"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Le serveur ne supporte pas le certificat SSL err: " + err.Error())
	}

	err = conn.VerifyHostname("blog.umesh.wtf")
	if err != nil {
		panic("Le nom d'hôte ne correspond pas au certificat: " + err.Error())
	}
}

```

Cela s'exécutera avec succès sans aucune erreur car le nom commun du certificat et le nom d'hôte sont les mêmes.

### Étape 3 : Vérifier la date d'expiration du certificat SSL du serveur

Nous pouvons obtenir la chaîne de certificats en utilisant `conn.ConnectionState().PeerCertificates`. Nous pouvons ensuite utiliser ce certificat pour obtenir la date d'expiration du certificat du serveur.

Nous utiliserons le premier certificat de la liste des certificats et essaierons d'obtenir la date d'expiration en utilisant le champ `NotAfter`.

```go
package main

import (
	"crypto/tls"
	"fmt"
	"time"
)

func main() {
	conn, err := tls.Dial("tcp", "blog.umesh.wtf:443", nil)
	if err != nil {
		panic("Le serveur ne supporte pas le certificat SSL err: " + err.Error())
	}

	err = conn.VerifyHostname("blog.umesh.wtf")
	if err != nil {
		panic("Le nom d'hôte ne correspond pas au certificat: " + err.Error())
	}
	expiry := conn.ConnectionState().PeerCertificates[0].NotAfter
	fmt.Printf("Émetteur: %s\nExpiration: %v\n", conn.ConnectionState().PeerCertificates[0].Issuer, expiry.Format(time.RFC850))
}

```

La sortie devrait contenir la date d'expiration du certificat et le nom de l'émetteur.

```
$ go run main.go
Émetteur: CN=Let's Encrypt Authority X3, O=Let's Encrypt, C=US
Expiration: Wednesday, 16-Dec-20 16:20:00 UTC
```

Nous avons maintenant validé avec succès le certificat du site.

### Conclusion

Vous pouvez également obtenir des informations détaillées comme l'autorité de certification racine, la date d'émission du certificat et tous les certificats enchaînés.

Cet outil a été écrit en utilisant uniquement les bibliothèques de base de Go (et aucune bibliothèque externe). Faites-moi savoir ce que vous en pensez !

Si vous avez aimé cet article, vous pouvez vous rendre sur [mon blog personnel](https://umesh.dev/blog) pour voir d'autres articles que j'ai écrits.

J'écris régulièrement sur la programmation et les logiciels, alors abonnez-vous à ma newsletter et recevez les derniers articles directement dans votre boîte de réception. Vous pouvez également me contacter sur [Twitter](https://twitter.com/imumesh18).