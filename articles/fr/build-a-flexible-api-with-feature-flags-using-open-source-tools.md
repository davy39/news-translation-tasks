---
title: Comment construire une API flexible avec des Feature Flags en utilisant des
  outils open source
subtitle: ''
author: Pradumna Saraf
co_authors: []
series: null
date: '2024-11-19T22:56:26.069Z'
originalURL: https://freecodecamp.org/news/build-a-flexible-api-with-feature-flags-using-open-source-tools
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1732044691446/abd5596c-3523-4278-957c-109388690bcc.png
tags:
- name: Open Source
  slug: opensource
- name: Go Language
  slug: go
- name: Redis
  slug: redis
- name: '  feature flags'
  slug: feature-flags
- name: backend developments
  slug: backend-developments
- name: Docker
  slug: docker
- name: APIs
  slug: apis
seo_title: Comment construire une API flexible avec des Feature Flags en utilisant
  des outils open source
seo_desc: Feature flagging has changed the paradigm of how backend developers can
  test and modify the things they build. With feature flags, we can enable and disable
  a feature or change the functionality of something on the fly with a single click
  (no need to...
---

Les feature flags ont changé le paradigme de la manière dont les développeurs backend peuvent tester et modifier ce qu'ils construisent. Avec les feature flags, nous pouvons activer et désactiver une fonctionnalité ou changer le fonctionnement de quelque chose à la volée avec un seul clic (pas besoin de redéployer).

Dans ce tutoriel, nous verrons comment les feature flags nous aident à activer et désactiver une fonctionnalité/une partie du code quand nous le voulons depuis l'UI, sans avoir besoin de redéployer tout le code.

Pour comprendre les choses plus en profondeur, nous allons construire une application à partir de zéro, examiner les capacités de feature flagging, et utiliser un outil appelé Flagsmith pour gérer nos feature flags créés depuis un seul tableau de bord.

## Voici ce que nous allons couvrir :

* [Prérequis](#heading-prerequisites)
    
* [Qu'est-ce qu'un Feature Flag ?](#heading-questce-quun-feature-flag)
    
* [Feature Flags pour le développement backend](#heading-feature-flags-pour-le-developpement-backend)
    
* [Pourquoi utiliser des outils open source ?](#heading-pourquoi-utiliser-des-outils-open-source)
    
* [C'est parti pour le code !](#heading-cest-parti-pour-le-code)
    
    * [Initialisation des outils](#heading-initialisation-des-outils)
        
    * [Création des endpoints pour l'API](#heading-creation-des-endpoints-pour-lapi)
        
    * [Comment ajouter le Feature Flagging](#heading-comment-ajouter-le-feature-flagging)
        
    * [Comprendre la logique du code des Feature Flags](#heading-comprendre-la-logique-du-code-des-feature-flags)
        
    * [Comment créer des Feature Flags dans le tableau de bord Flagsmith](#heading-comment-creer-des-feature-flags-dans-le-tableau-de-bord-flagsmith)
        
    * [Feature Flag de limitation de débit](#heading-feature-flag-de-limitation-de-debit)
        
    * [Feature Flag Bêta](#heading-feature-flag-beta)
        
    * [Obtenir la clé d'accès](#heading-obtenir-la-cle-dacces)
        
    * [Exécuter l'API](#heading-executer-lapi)
        
    * [Mettre à jour le Flag rate_limit](#heading-mettre-a-jour-le-flag-ratelimit)
        
    * [Comment intégrer les Feature Flags avec l'application GitHub](#heading-comment-integrer-les-feature-flags-avec-lapplication-github)
        
    * [Tester l'application GitHub Flagsmith](#heading-tester-lapplication-github-flagsmith)
        
* [Conclusion](#heading-conclusion)
    

## Prérequis

* [Golang](https://go.dev/) installé et une compréhension de niveau moyen de celui-ci.
    
* Une instance [Redis](https://redis.io) en cours d'exécution (instance distante ou locale)
    
* Compte [Flagsmith](https://www.flagsmith.com/) (C'est gratuit. Nous couvrirons cela plus tard dans l'article.)
    

## Qu'est-ce qu'un Feature Flag ?

Un Feature Flag est une technique en développement qui permet aux équipes d'activer ou de désactiver des fonctionnalités sans modifier le code source ou redéployer.

Pour simplifier, pensez à eux comme fonctionnant un peu comme des instructions conditionnelles (par exemple, des instructions if-else) : en fonction de si quelque chose est vrai ou faux, cela détermine le chemin de code qui sera exécuté.

## Feature Flags pour le développement backend

Vous avez peut-être vu des feature flags utilisés dans les frontends et les sites web, mais il y a beaucoup plus à eux. Vous pouvez les utiliser côté serveur pour modifier la fonctionnalité d'une API, faire des choses comme modifier/définir la limite de débit, changer la fonctionnalité de l'endpoint de l'API ou la désactiver complètement. En tant que développeurs backend, nous pouvons améliorer nos tests avec les feature flags.

Pour démontrer cela, nous allons passer par la construction d'une application de démonstration. L'application de démonstration est conçue pour montrer les capacités de feature flagging, de la modification de la fonctionnalité (limite de débit) à la volée à l'ajout d'un nouvel endpoint à l'API pour des tests bêta ou des déploiements initiaux. Nous utiliserons entièrement des outils open source en cours de route !

## Pourquoi utiliser des outils open source ?

Nous allons utiliser des outils open source pour construire cette application (Golang, [Redis](https://redis.io/), et [Flagsmith](https://www.flagsmith.com/?utm_source=thirdparty&utm_medium=freecodecamp&utm_campaign=pradumna)). L'open source apporte plus de transparence et de confiance et encourage la collaboration avec la communauté mondiale des développeurs backend.

En intégrant des outils open source, nous obtenons une visibilité totale lors de la construction et des tests. Par exemple, nous allons intégrer des feature flags avec GitHub, ce qui nous permet de suivre le cycle de vie d'une fonctionnalité en liant un feature flag Flagsmith avec une Pull Request ou un Issue GitHub. Cela nous permet de rester à jour avec les changements de nos fonctionnalités sans avoir à suivre manuellement chaque modification. Nous pouvons facilement suivre l'état de nos fonctionnalités dans différents environnements.

## C'est parti pour le code !

Dans ce tutoriel, vous verrez comment la fonctionnalité d'une application change avant et après les tests avec les mécanismes de feature flagging. Les outils et frameworks que nous allons utiliser sont Golang, Docker, Redis, Flagsmith et GitHub. Comme discuté, tous sont open source et gratuits pour créer un compte de test.

Pour commencer, ouvrez votre IDE préféré, initialisez un projet Golang, puis copiez le code ci-dessous dans le fichier `main.go`. Ensuite, exécutez `go mod tidy` pour installer toutes les dépendances nécessaires.

Comprenons ce qui se passe dans l'extrait de code ci-dessous :

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"
	"strconv"

	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis_rate/v10"
	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
)

var (
	redisClient *redis.Client
	limiter     *redis_rate.Limiter
)

func initClients() {
	redisClient = redis.NewClient(&redis.Options{
		Addr: os.Getenv("REDIS_URL"),
	})
	limiter = redis_rate.NewLimiter(redisClient)
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Printf("Chargement des variables d'environnement à partir du système hôte")
	} else {
		log.Printf("Chargement de l'environnement à partir du fichier .env")
	}

	initClients()
	defer redisClient.Close()

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		err, remainingLimit := rateLimitCall(c.ClientIP())
		if err != nil {
			c.JSON(
				http.StatusTooManyRequests,
				gin.H{"error": "Limite de débit atteinte"})
		} else {
			c.JSON(
				http.StatusOK,
				gin.H{"Vos requêtes API restantes sont": remainingLimit})
		}
	})
	r.GET("/beta", func(c *gin.Context) {
		c.JSON(
			http.StatusOK,
			gin.H{"message": "Ceci est un endpoint bêta"})
	})
	r.Run(":" + os.Getenv("PORT"))
}

func rateLimitCall(ClientIP string) (error, int) {
	ctx := context.Background()

	rateLimitString := os.Getenv("RATE_LIMIT")
	RATE_LIMIT, _ := strconv.Atoi(rateLimitString)

	res, err := limiter.Allow(ctx, ClientIP, redis_rate.PerHour(RATE_LIMIT))
	if err != nil {
		panic(err)
	}

	if res.Remaining == 0 {
		return errors.New("Vous avez atteint la limite de débit pour l'API. Réessayez plus tard"), 0
	}

	fmt.Println("requêtes restantes pour", ClientIP, "est", res.Remaining)
	return nil, res.Remaining
}
```

### Initialisation des outils

```go
func initClients() {
	redisClient = redis.NewClient(&redis.Options{
		Addr: os.Getenv("REDIS_URL"),
	})
	limiter = redis_rate.NewLimiter(redisClient)
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Printf("Chargement des variables d'environnement à partir du système hôte")
	} else {
		log.Printf("Chargement de l'environnement à partir du fichier .env")
	}

	initClients()
	defer redisClient.Close()

	r := gin.Default()
    ...
	})
```

En haut, nous déclarons des variables pour stocker les clients Redis et Rate limiter afin de les réutiliser et de les initialiser une fois. Ensuite, nous les initialisons dans la fonction `initClients()`.

Dans `main()`, nous chargeons d'abord les variables d'environnement à partir du système ou du fichier .env. Ensuite, nous appelons `initClients()`. Cela créera les clients et les stockera dans les variables que nous avons créées.

Ensuite, nous créons un routeur **Gin** qui gère toutes nos requêtes entrantes. Ce sont les variables d'environnement dont nous avons besoin dans notre fichier `.env`. Pour cette démonstration, nous avons besoin d'une instance Redis en cours d'exécution pour stocker toutes les données pour la fonctionnalité de limitation de débit. Nous pouvons utiliser Docker ou toute machine distante, il suffit de se souvenir de mettre à jour `REDIS_URL` en conséquence. Je vais utiliser Docker.

Nous pourrions également aller plus loin et obtenir toutes les variables d'environnement à partir des feature flags, mais nous ne le ferons pas ici.

```bash
REDIS_URL=localhost:6379
PORT=8080
RATE_LIMIT=10
```

### Création des endpoints pour l'API

```go
r.GET("/ping", func(c *gin.Context) {
		err, remainingLimit := rateLimitCall(c.ClientIP())
		if err != nil {
			c.JSON(
				http.StatusTooManyRequests,
				gin.H{"error": "Limite de débit atteinte"})
		} else {
			c.JSON(
				http.StatusOK,
				gin.H{"Vos requêtes API restantes sont": remainingLimit})
		}
	})
	r.GET("/beta", func(c *gin.Context) {
		c.JSON(
			http.StatusOK,
			gin.H{"message": "Ceci est un endpoint bêta"})
	})
	r.Run(":" + os.Getenv("PORT"))
```

Ensuite, nous créons deux endpoints **GET**, `/ping` et `/beta`. Chaque fois que quelqu'un appelle l'endpoint `/ping`, nous appelons la fonction `rateLimitCall()`. Elle vérifie et définit la limite de débit des requêtes entrantes à partir d'une **adresse IP**. Tout cela est stocké dans l'instance Redis que nous avons créée.

Donc, maintenant, si l'utilisateur a interagi avec l'endpoint de l'API `/ping` pour la première fois, cela créera une entrée avec une limite de **10 par heure**. Le nombre de limite **10** provient du `RATE_LIMIT` que nous avons défini, et le rafraîchissement horaire provient de la fonction `redis_rate.PerHour(RATE_LIMIT)`.

Ensuite, nous vérifions si l'utilisateur a une limite restante. Si oui, nous retournerons un message avec le nombre de requêtes qu'il lui reste. Sinon, s'il atteint la limite maximale, nous retournerons un message pour l'informer.

En plus de l'endpoint `/ping`, nous avons un autre endpoint `/beta`. Il retourne un message simple, mais plus tard nous verrons comment (en utilisant les feature flags) nous pouvons activer et désactiver complètement la fonctionnalité de cet endpoint.

### Comment ajouter le Feature Flagging

Maintenant, il est temps d'ajouter des capacités de feature flagging à notre application. Nous allons utiliser [Flagsmith](https://flagsmith.com/). Flagsmith est un logiciel open source qui nous permet de créer et de gérer facilement des feature flags sur les applications web, mobiles et côté serveur.

En utilisant Flagsmith, nous pouvons envelopper des fonctionnalités dans un flag et ensuite les activer ou les désactiver pour différents environnements, utilisateurs ou segments d'utilisateurs. Et ensuite, vous pourrez gérer le tout depuis le tableau de bord Flagsmith sans avoir besoin de redéployer.

Donc, installons le package Flagsmith en exécutant la commande ci-dessous :

```bash
go get github.com/Flagsmith/flagsmith-go-client/v3
```

Ensuite, nous importons le package en lui donnant un alias **flagsmith**. Voici la fonctionnalité mise à jour après avoir appliqué le feature flagging à notre code existant.

Comprenons les changements que nous avons apportés ici (je vais expliquer ci-dessous l'extrait de code) :

```go
package main

import (
	"context"
	"errors"
	"fmt"
	"log"
	"net/http"
	"os"

	flagsmith "github.com/Flagsmith/flagsmith-go-client/v3"
	"github.com/gin-gonic/gin"
	"github.com/go-redis/redis_rate/v10"
	"github.com/joho/godotenv"
	"github.com/redis/go-redis/v9"
)

var (
	redisClient     *redis.Client
	limiter         *redis_rate.Limiter
	flagsmithClient *flagsmith.Client
)

func initClients() {
	redisClient = redis.NewClient(&redis.Options{
		Addr: os.Getenv("REDIS_URL"),
	})
	limiter = redis_rate.NewLimiter(redisClient)
	flagsmithClient = flagsmith.NewClient(os.Getenv("FLAGSMITH_ENVIRONMENT_KEY"))
}

func main() {
	err := godotenv.Load()
	if err != nil {
		log.Printf("Chargement des variables d'environnement à partir du système hôte")
	} else {
		log.Printf("Chargement de l'environnement à partir du fichier .env")
	}

	initClients()
	defer redisClient.Close()

	r := gin.Default()
	r.GET("/ping", func(c *gin.Context) {
		err, remainingLimit := rateLimitCall(c.ClientIP())
		if err != nil {
			c.JSON(
				http.StatusTooManyRequests,
				gin.H{"error": "Limite de débit atteinte"})
		} else {
			c.JSON(
				http.StatusOK,
				gin.H{"Vos requêtes API restantes sont": remainingLimit})
		}
	})
	r.GET("/beta", func(c *gin.Context) {
		flags := getFeatureFlags()
		isEnabled, _ := flags.IsFeatureEnabled("beta")
		if isEnabled {
			c.JSON(
				http.StatusOK,
				gin.H{"message": "Ceci est un endpoint bêta"})
		} else {
			c.String(http.StatusNotFound, "404 page non trouvée")
		}
	})

	r.Run(":" + os.Getenv("PORT"))
}

func rateLimitCall(ClientIP string) (error, int) {

	ctx := context.Background()

	flags := getFeatureFlags()
	rateLimitInterface, _ := flags.GetFeatureValue("rate_limit")
	RATE_LIMIT := int(rateLimitInterface.(float64))
	fmt.Println("La limite de débit actuelle est", RATE_LIMIT)

	res, err := limiter.Allow(ctx, ClientIP, redis_rate.PerHour(RATE_LIMIT))
	if err != nil {
		panic(err)
	}

	if res.Remaining == 0 {
		return errors.New("Vous avez atteint la limite de débit pour l'API. Réessayez plus tard"), 0
	}

	fmt.Println("requêtes restantes pour", ClientIP, "est", res.Remaining)
	return nil, res.Remaining
}

func getFeatureFlags() flagsmith.Flags {
	ctx := context.Background()
	flags, _ := flagsmithClient.GetEnvironmentFlags(ctx)
	return flags
}
```

### Comprendre la logique du code des Feature Flags

```go
func getFeatureFlags() flagsmith.Flags {
	ctx := context.Background()
	flags, _ := flagsmithClient.GetEnvironmentFlags(ctx)
	return flags
}
```

Tout d'abord, passons directement à la nouvelle fonction `getFeatureFlags()` que nous avons créée en bas. Cette fonction retournera tous les flags que nous avons créés sur le tableau de bord Flagsmith, en appelant la méthode `GetEnvironmentFlags()` sur `flagsmithClient`.

Nous avons initié le `flagsmithClient` à l'intérieur de la fonction `initClients()`. Le client Flagsmith a besoin de la clé d'accès (la fonction `NewClient()`) que nous pouvons obtenir à partir du tableau de bord Flagsmith. Comme nous l'avons fait pour les clients Redis et Limter, nous stockerons le client dans une variable globale pour la réutilisabilité. Vous comprendrez le tableau de bord, la création de flags et la récupération de la clé dans les étapes suivantes.

```go
func rateLimitCall(ClientIP string) (error, int) {

	ctx := context.Background()

	flags := getFeatureFlags()
	rateLimitInterface, _ := flags.GetFeatureValue("rate_limit")
	RATE_LIMIT := int(rateLimitInterface.(float64))
	fmt.Println("La limite de débit actuelle est", RATE_LIMIT)

	res, err := limiter.Allow(ctx, ClientIP, redis_rate.PerHour(RATE_LIMIT))
	if err != nil {
		panic(err)
	}

	if res.Remaining == 0 {
		return errors.New("Vous avez atteint la limite de débit pour l'API. Réessayez plus tard"), 0
	}

	fmt.Println("requêtes restantes pour", ClientIP, "est", res.Remaining)
	return nil, res.Remaining
}
```

Maintenant, en ce qui concerne la fonction `rateLimitCall()`, au lieu d'obtenir `RATE_LIMIT` à partir de l'environnement, nous obtenons la valeur à partir du flag `rate_limit` (que nous créerons plus tard). Nous appelons `getFeatureFlags()` et obtenons la valeur du flag `rate_limit` à partir de tous les flags.

En les définissant comme des feature flags, nous pouvons changer dynamiquement la limite à tout moment à partir du tableau de bord. Nous n'avons pas besoin de changer la fonctionnalité du code ou de le faire de la manière traditionnelle en changeant la valeur `RATE_LIMIT` et en relançant le serveur pour qu'il récupère les nouvelles valeurs mises à jour.

```go
	r.GET("/beta", func(c *gin.Context) {
		flags := getFeatureFlags()
		isEnabled, _ := flags.IsFeatureEnabled("beta")
		if isEnabled {
			c.JSON(
				http.StatusOK,
				gin.H{"message": "Ceci est un endpoint bêta"})
		} else {
			c.String(http.StatusNotFound, "404 page non trouvée")
		}
	})
```

Maintenant, en ce qui concerne l'endpoint `/beta`, en fonction de si le flag bêta est activé ou désactivé, cet endpoint servira la requête. Sinon, il agira comme un endpoint inaccessible et retournera un message d'erreur 404.

Dans notre exemple, j'ai ajouté un message de remplissage de base pour montrer comment cela fonctionnera, mais cela ouvre de nouvelles possibilités en matière de tests et de versions initiales (bêta). Si l'API a un nouvel endpoint, nous pouvons envelopper la fonctionnalité dans le feature flag et la rendre disponible et indisponible avec un simple clic sur un bouton. De plus, nous pouvons faire beaucoup plus comme la planification et les versions canaries.

De plus, notre fichier `.env` ressemblera à ceci. Nous avons supprimé `RATE_LIMIT` et ajouté `FLAGSMITH_ENVIRONMENT_KEY`.

```bash
REDIS_URL=localhost:6379
PORT=8080
FLAGSMITH_ENVIRONMENT_KEY=ser.ZRd***********469
```

### Comment créer des Feature Flags dans le tableau de bord Flagsmith

Rendons-nous sur le tableau de bord Flagsmith pour créer les flags que nous avons utilisés ci-dessus et obtenir la clé d'accès. Si vous n'avez pas de compte Flagsmith, vous pouvez vous inscrire gratuitement [ici](https://app.flagsmith.com/signup).

Après votre inscription, vous serez invité à créer une organisation et un projet. La séparation des projets est bonne, car elle nous aide à isoler la logique pour différents projets. Une fois que vous avez terminé, vous verrez un tableau de bord, comme sur la capture d'écran ci-dessous.

Nous avons de nombreuses fonctionnalités, des intégrations à la planification des flags pour comparer les changements. En plus de Go, Flagsmith fournit de nombreux [SDK](https://docs.flagsmith.com/clients/). Vous pouvez cliquer sur l'endroit où le nom du langage est écrit et il vous donnera un code de base pour ce langage.

![Capture d'écran d'une interface web intitulée "Features" pour gérer les feature flags et la configuration à distance. Elle inclut des exemples de code Go pour installer le SDK et initialiser un projet, avec des options pour tester les valeurs de l'API. Il y a des boutons et des onglets pour la navigation et les paramètres.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544211942/57f3651f-b62a-4b8f-beb7-4320ef0e0a8e.png align="center")

### Feature Flag de limitation de débit

Maintenant, créons notre premier feature flag pour la limite de débit. Cliquez sur le bouton **Créer un Feature** dans le coin supérieur droit. Une fenêtre de barre latérale s'ouvrira. Définissez le nom, puis pour que le flag s'active correctement lors de la création, nous pouvons sélectionner **Activé par défaut.**

Dans la section valeur, nous devons définir la valeur du flag. Il peut prendre des formats comme Txt, JSON, XML, etc. Comme notre valeur de feature est un texte simple comme 20, 30, etc., nous choisirons Txt (celui par défaut) et définirons une limite aléatoire - nous allons choisir **20**.

Vous pouvez également donner des tags et des descriptions. Les tags peuvent être utiles lors du filtrage des Feature Flags. Par exemple, nous pouvons créer un tag `backend` pour filtrer tous les feature flags liés au Backend. La description est une explication concise de ce que fait ce flag particulier lorsqu'il est activé (et aidera à la compréhension future).

La capture d'écran ci-dessous montre à quoi cela ressemblera après avoir rempli les détails. Ensuite, cliquez sur le bouton **Créer un Feature** pour créer le flag.

![Capture d'écran d'une interface d'application web montrant la création d'une nouvelle fonctionnalité. À gauche, il y a un menu avec des options comme Features et SDK Keys. À droite, des champs pour ajouter une nouvelle fonctionnalité sont visibles, incluant un ID/Nom, un toggle pour activer par défaut, une valeur définie à 20, et des options pour les tags et les descriptions. Il y a une note indiquant la création de fonctionnalités pour tous les environnements, avec un bouton "Créer un Feature" en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544238847/4e5cf3ab-1fb6-4783-afcc-39adcebae48e.png align="center")

### Feature Flag Bêta

Créons maintenant un deuxième flag de fonctionnalité, `beta`. Ce sera le même processus que le premier, mais dans celui-ci, nous n'avons pas besoin de définir de valeur de flag et laissons cette colonne vide. Une fois que nous avons créé les deux flags, notre tableau de bord ressemblera à ceci. Il montre le nom du flag, la valeur, l'état actuel (vue), etc.

![Interface logicielle présentant une section "Features" avec des bascules pour les fonctionnalités "beta" et "rate_limit". La page inclut des options de navigation à gauche et des boutons pour créer des fonctionnalités et exécuter des tests.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544256561/3735429f-8dd0-4f0f-a01e-b4a4a7b5aa75.png align="center")

### Obtenir la clé d'accès

Pour obtenir la clé d'accès, cliquez sur **SDK Keys** dans la barre latérale, puis cliquez sur le bouton **Créer une clé d'environnement côté serveur** pour générer une clé. Comme notre application est côté serveur, il est bon d'utiliser celle-ci uniquement. Ensuite, copiez et collez cette clé dans la valeur placée dans `.env` pour la clé `FLAGSMITH_ENVIRONMENT_KEY`.

![Capture d'écran d'une interface logicielle montrant les sections "Client-side Environment Key" et "Server-side Environment Keys". Un bouton intitulé "Create Server-side Environment Key" est affiché de manière proéminente. Le menu de la barre latérale inclut des options comme "SDK Keys" et "Environment Settings".](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544280780/fc37cb29-3069-4e2f-b35b-eea7632c47cd.png align="center")

### Exécuter l'API

Maintenant, tout est prêt, alors retournons à l'IDE et exécutons le serveur en exécutant la commande `go run main.go` dans le terminal. Nous verrons ce message dans le terminal. En cas d'erreurs, vérifiez simplement que les packages sont correctement installés, que les variables sont correctement définies et que l'application accède à l'instance Redis.

![Capture d'écran d'une fenêtre VS Code montrant un projet Go avec le fichier "main.go" ouvert. Le code inclut des fonctions pour limiter le débit des appels API et récupérer les feature flags. Le terminal en bas affiche la sortie de l'exécution de l'application, avec des avertissements et des messages de statut liés à un serveur web.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544780659/95fbbb17-43c3-4cd1-b84f-020c08ec38d3.png align="center")

Maintenant, si nous visitons [**localhost:8080/ping**](http://localhost:8080/ping), nous obtiendrons un message `{"Vos requêtes API restantes sont":19}`. La limite était de 20, nous avons fait une requête maintenant, et il reste 19.

![Fenêtre de navigateur affichant une page web à "localhost:8080/ping" montrant le message JSON : {"Vos requêtes API restantes sont": 19}.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544374092/bc97064c-285e-44fa-990d-51a52a671d26.png align="center")

### Mettre à jour le flag `rate_limit`

Mettons à jour la valeur du flag `rate_limit` à 10 et voyons ce qui se passe. Pour ce faire, visitez à nouveau le tableau de bord Flagsmith et cliquez sur le nom du flag. Une barre de menu latérale s'ouvrira. Mettez à jour la valeur à 10, et cliquez sur le bouton **Mettre à jour la valeur du Feature**.

Nous pouvons également planifier la mise à jour. Par exemple, cela peut être utile lorsque nous prévoyons un pic de trafic à un certain moment et réduisons la limite par utilisateur pour réduire la charge du serveur.

![Capture d'écran d'un tableau de bord logiciel montrant une interface de gestion des fonctionnalités. La fonctionnalité "rate_limit" est activée avec une valeur de 10. Les options incluent la modification de la valeur, les remplacements de segment et la planification des mises à jour.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730545050685/f253ea86-de3d-4a6a-b5fd-35f489da86cf.png align="center")

Si vous visitez maintenant [**localhost:8080/ping**](http://localhost:8080/ping), vous obtiendrez un message `{"Vos requêtes API restantes sont":8}` - car la limite totale est de 10 et nous avons déjà fait deux requêtes.

![Fenêtre de navigateur affichant une réponse JSON avec le texte : "Vos requêtes API restantes sont : 8".](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544415108/97e6fd9c-b5a1-4143-877a-6724cf871a6b.png align="center")

Testons maintenant l'endpoint `/beta`. Visitez [localhost:8080/beta](http://localhost:8080/beta), et nous verrons un message `{"message":"Ceci est un endpoint bêta"}`.

![Capture d'écran d'un navigateur web affichant des données JSON à l'URL "localhost:8080/beta" avec le message : "Ceci est un endpoint bêta".](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544479869/623d8b72-3648-46ae-b79f-409da44c1d38.png align="center")

Maintenant, retournez au tableau de bord Flagsmith et basculez l'interrupteur pour désactiver ce flag. Maintenant, visitez l'URL. Vous obtiendrez un message 404 comme si cet endpoint n'avait jamais existé.

![Capture d'écran d'une fenêtre de navigateur affichant un message d'erreur "404 page non trouvée".](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544488522/518c58b2-f767-4396-9020-99e8cd01586a.png align="center")

Maintenant que nous avons configuré la fonctionnalité et démontré les capacités de feature flagging, voyons comment nous pouvons intégrer l'application GitHub Flagsmith.

### Comment intégrer les Feature Flags avec l'application GitHub

Tout d'abord, assurez-vous d'avoir poussé votre application sur GitHub. Après cela, installez l'application GitHub Flagsmith sur votre dépôt à partir du [GitHub Marketplace](https://github.com/apps/flagsmith).

En intégrant GitHub et Flagsmith, nous pouvons voir les mises à jour de vos feature flags/fonctionnalités en tant que commentaires dans les Issues et Pull Requests GitHub. Cela nous permet de suivre facilement les fonctionnalités, de la création d'une issue à la fusion d'une PR et au déploiement des changements.

![Capture d'écran de la page d'intégration de l'application GitHub Flagsmith, détaillant ses fonctionnalités et avantages, avec une option pour installer l'application.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544845464/dcce9af3-a34f-420a-b9c4-2968d47fda70.png align="center")

Ensuite, sélectionnez votre organisation et les dépôts où vous souhaitez installer l'application. Vous pouvez l'installer sur tous vos dépôts ou en sélectionner un en particulier.

Lorsque vous l'installez, vous serez automatiquement redirigé vers le tableau de bord Flagsmith pour configurer et compléter l'intégration. La plupart des données seront pré-remplies, vous devez donc simplement sélectionner et ajouter un projet, puis enregistrer la configuration.

![Capture d'écran d'une page web pour configurer l'intégration GitHub avec Flagsmith. Elle inclut des champs pour sélectionner l'organisation, le projet et le dépôt, avec des options définies pour "Pradumna", "go-api" et "go-redis-flagsmith". Il y a un bouton "Ajouter un projet" et un bouton "Enregistrer la configuration" en bas.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730544640407/8ac36f96-d61b-47f7-ad3a-f914f0f01824.png align="center")

Une fois que vous avez cliqué sur le bouton **Enregistrer la configuration**, vous serez redirigé vers le tableau de bord principal Flagsmith où nous travaillions précédemment.

Maintenant, liez l'un des flags existants à l'issue ou à la pull request GitHub (créez une PR/issue factice pour la tester), ou vous pouvez créer un nouveau flag pour le tester. Continuons avec le flag beta que nous avons déjà créé pour l'endpoint `beta`.

Pour lier le flag à une issue ou à une pull request existante, cliquez sur le nom du flag, et un menu latéral s'ouvrira à droite. Ensuite, choisissez l'onglet 'Link'. Ensuite, sélectionnez l'option Pull Request, et choisissez la Pull Request que vous souhaitez lier. Toutes vos Issues et Pull Requests liées à ce flag sont visibles ci-dessous :

![Capture d'écran d'un environnement de développement montrant la section "Features", avec un menu de barre latérale à gauche. Le panneau "Edit Feature: beta" est ouvert à droite, affichant des options pour lier une issue ou une pull request et une pull request listée intitulée "feat: Update the beta endpoint feature (#2)" avec son statut marqué comme ouvert.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730546404697/0fb1c515-ab42-494d-ac84-87e076d30607.png align="center")

Pour vérifier que le flag est correctement lié, cliquez sur l'hyperlien avec l'icône de flèche sous l'en-tête de la colonne **Nom**. Il vous redirigera vers cette Issue/Pull Request spécifique sur GitHub. Vous pouvez voir que l'application GitHub Flagsmith a commenté ci-dessous avec tous les détails, tels que l'environnement, la valeur activée, etc.

![Page de pull request GitHub montrant une demande intitulée "feat: Update the beta endpoint feature #2" pour fusionner un commit de la branche "beta" dans "main". Elle inclut un commentaire utilisateur sur la mise à jour et un commentaire du bot Flagsmith montrant l'état de la fonctionnalité pour les environnements de production et de développement. La pull request est ouverte, sans avis pour l'instant.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730545132237/4601a08e-62d9-4ebc-890e-89430bf6624e.png align="center")

### Tester l'application GitHub Flagsmith

Après cela, lorsque vous apportez des modifications aux paramètres du flag, comme activer/désactiver le flag ou changer la valeur, le bot commentera avec tous les détails mis à jour.

Testons en désactivant le flag. Dès que vous désactivez le flag depuis le tableau de bord, le bot devrait commenter que le flag a maintenant été désactivé :

![Image montrant une interface de pull request GitHub. La pull request est intitulée "feat: Update the beta endpoint feature #2" et montre une mise à jour du bot flagsmith indiquant que la fonctionnalité "beta" pour l'environnement "Development" est actuellement désactivée.](https://cdn.hashnode.com/res/hashnode/image/upload/v1730545146615/b76f2f21-369a-4617-b55b-abc3201a1c52.png align="center")

C'est tout. C'est ainsi qu'il est simple d'intégrer Flagsmith avec GitHub.

## Conclusion

Pour résumer, vous savez maintenant comment vous pouvez utiliser les feature flags en tant que développeur backend pour changer la fonctionnalité de votre application à la volée.

Pour passer les choses au niveau supérieur, nous avons intégré notre application de démonstration avec l'application GitHub Flagsmith afin qu'elle puisse rester à jour avec les changements de statut de nos feature flags sur les Pull Requests/Issues sans avoir à les mettre à jour manuellement.

Consultez le dépôt Flagsmith [ici](https://github.com/Flagsmith/flagsmith) et n'oubliez pas de donner une étoile à chacun de ces projets pour montrer votre soutien. Vous pouvez également rejoindre leur communauté incroyable [ici](https://discord.com/invite/hFhxNtXzgm) pour obtenir un soutien technique.

Vous pouvez me contacter - Pradumna Saraf, sur les réseaux sociaux [ici](https://links.pradumnasaraf.dev/).