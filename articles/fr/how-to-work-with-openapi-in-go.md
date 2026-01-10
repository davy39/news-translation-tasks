---
title: Comment travailler avec OpenAPI en Go
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2025-02-19T13:19:09.738Z'
originalURL: https://freecodecamp.org/news/how-to-work-with-openapi-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740164911110/7954a7d5-39dc-4504-82eb-f5fe583b7b84.png
tags:
- name: APIs
  slug: apis
- name: REST API
  slug: rest-api
- name: OpenApi
  slug: openapi
- name: swagger
  slug: swagger
- name: RESTful APIs
  slug: restful-apis
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Comment travailler avec OpenAPI en Go
seo_desc: 'Well-structured and well-documented APIs are a pleasure to work with. And
  nowadays the standard is OpenAPI, which comes with a good methodology for defining
  an API interface first, and only then constructing everything around it.

  This makes it easier...'
---

Les API bien structurées et bien documentées sont un plaisir à utiliser. Et de nos jours, le standard est [OpenAPI](https://www.openapis.org/), qui offre une bonne méthodologie pour définir une interface API en premier, puis construire tout autour.

Cela facilite la compréhension, l'implémentation et la consommation de ces API. Et les standards sont importants, car ils permettent à différentes équipes, indépendamment de leur stack technologique, de communiquer efficacement et de travailler avec la même API.

![Cycle de vie de l'API](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3191c4bd-690b-45e8-86bb-8b460ae434c6_1295x1490.png align="left")

Dans ce guide pratique, je vais vous guider à travers toutes les parties importantes impliquées dans l'architecture, l'implémentation et la consommation d'une API en utilisant le standard OpenAPI.

Avant de plonger, il est utile d'avoir une compréhension de base des éléments suivants :

* Le langage de programmation Go

* Les API RESTful

* JSON/YAML

* Utilisation de base de la ligne de commande

## Table des matières

1. [Qu'est-ce que la spécification OpenAPI (OAS) ?](#heading-questce-que-la-specification-openapi-oas)

2. [Architecture de l'API](#heading-architecture-de-lapi)

   * [openapi.yaml](#heading-openapiyaml)

   * [Chemins et opérations](#heading-chemins-et-operations)

   * [Schéma](#heading-schemas)

   * [Extensions](#heading-extensions)

3. [Comment générer un serveur Go](#heading-comment-generer-un-serveur-go)

4. [Comment visualiser la documentation de l'API](#heading-comment-visualiser-la-documentation-de-lapi)

5. [Code client](#heading-code-client)

6. [Conclusion](#heading-conclusion)

## Qu'est-ce que la spécification OpenAPI (OAS) ?

La spécification OpenAPI (OAS) fournit un moyen cohérent de transporter des informations à travers chaque étape du cycle de vie de l'API. Il s'agit d'un langage de spécification pour les API HTTP qui définit la structure et la syntaxe de manière à ne pas être liée au langage de programmation dans lequel l'API est créée.

La [spécification OpenAPI (OAS)](https://spec.openapis.org/) était à l'origine basée sur la spécification Swagger 2.0 de SmartBear Software. Plus tard, elle a été transférée à l'[OpenAPI Initiative (OAI)](https://www.openapis.org/), un consortium d'experts de l'industrie sous la Linux Foundation.

L'idée principale d'OpenAPI est de pouvoir décrire les API en termes agnostiques, les découplant de tout langage de programmation spécifique. Les consommateurs de votre spécification d'API n'ont pas besoin de comprendre les détails de votre application ou d'essayer d'apprendre Lisp ou Haskell si c'est ce que vous avez choisi pour l'écrire. Ils peuvent comprendre exactement ce dont ils ont besoin à partir de votre spécification d'API, écrite dans un langage simple et expressif.

Ce langage simple et expressif est appelé [DSL (langage spécifique au domaine)](https://www.jetbrains.com/mps/concepts/domain-specific-languages/). Il peut être écrit en JSON ou en YAML.

La dernière version de l'OAS est [v3.1.1](https://spec.openapis.org/oas/latest.html) et la spécification elle-même est énorme. Il y a de nombreuses fonctionnalités et cas particuliers, mais nous allons essayer de passer en revue les plus importants.

## Architecture de l'API

Tout commence par la définition de ce que l'API doit fournir à ses consommateurs et à quoi elle sert. Bien que cette étape ne soit pas toujours purement technique, avoir une ébauche de la conception de votre API en OAS lors de la collecte des exigences vous donne une longueur d'avance lorsque vous commencez la conception.

Une fois les exigences prêtes, il est temps d'ouvrir votre [éditeur OpenAPI](https://editor.swagger.io/) et de collaborer avec vos coéquipiers.

Et il est important de comprendre qu'il ne s'agit pas seulement d'écrire la spécification JSON/YAML, mais aussi de s'accorder sur la conception de l'API.

Je vous recommande de suivre un guide de conception d'API - [Google en a un](https://cloud.google.com/apis/design), par exemple. Cela vous aidera à éviter les styles mélangés (comme **/resourceName/{id}** et **/resource\_name/{id}**, l'utilisation incohérente des méthodes HTTP, ou les relations de ressources peu claires.

### openapi.yaml

La spécification de votre API commence dans le document d'entrée `openapi.yaml` (nom recommandé mais non obligatoire) ou `openapi.json`. J'ai vu des fichiers `openapi.yaml` très volumineux (50k lignes), mais il est possible de diviser votre spécification en plusieurs parties. Gardez simplement à l'esprit que cela peut ne pas bien fonctionner pour certains outils OpenAPI car ils s'attendent à un seul fichier. [Google Maps OAS](https://github.com/googlemaps/openapi-specification/) est un bon exemple de la façon de diviser le schéma, mais il est également livré avec un pré-processeur pour générer un seul fichier.

Il existe quelques outils open source pour regrouper l'OAS : [swagger-cli](https://github.com/APIDevTools/swagger-cli) (archivé) et [redocly-cli](https://github.com/Redocly/redocly-cli) sont de bonnes options.

```bash
swagger-cli bundle -o _bundle/openapi.yaml openapi.yaml
```

Comme je l'ai mentionné précédemment, la spécification est énorme, mais décomposons-la en parties plus petites. Pour ce tutoriel, j'ai créé une API fictive "Smart Home". Vous pouvez voir la spécification complète et le code [ici](https://github.com/plutov/packagemain/tree/master/oapi-example).

L'objet racine est appelé [OpenAPI Object](https://spec.openapis.org/oas/latest.html#openapi-object) et a la structure suivante :

```yaml
# version du schéma
openapi: 3.1.1

# docs
info:
  title: Smart Home API
  description: Spécification de l'API pour Smart Home API
  version: 0.0.1

# serveurs optionnels pour les API publiques
servers:
  - url: "https://..."

# les tags sont utilisés pour regrouper les endpoints
tags:
  - name: device
    description: Gérer les appareils
  - name: room
    description: Gérer les pièces

# les endpoints vont ici
paths:
  # ...

# objets réutilisables tels que les schémas, les types d'erreurs, les corps de requête
components:
  # ...

# mécanismes de sécurité, doivent correspondre à components.securitySchemes
security:
  - apiKeyAuth: []
```

Nous avons défini le squelette de notre schéma, mais la majorité du schéma OpenAPI se trouve dans les propriétés `paths` et `components`.

### Chemins et opérations

Ajoutons maintenant quelques endpoints à notre schéma. Les opérations sont regroupées par chemins, donc vous pouvez avoir plusieurs méthodes HTTP sur un seul chemin - par exemple `GET /devices/{deviceId}` et `DELETE /devices/{deviceId}`.

Il est bon de définir tous les types (corps de requête, réponses, erreurs) dans la section `components` et de les référencer au lieu de les définir manuellement dans la section `paths`. Cela permet une réutilisation plus facile des entités. Par exemple, dans notre API, nous avons un type `Device` qui peut être utilisé dans de nombreux endpoints.

```yaml
paths:

  # le chemin a un paramètre
  /devices/{deviceId}:
    get:
      tags:
        - device
      summary: Obtenir un appareil
      operationId: getDevice

      parameters:
        - name: deviceId
          in: path
          required: true
          schema:
            $ref: "#/components/schemas/ULID"

      responses:

        "200":
          description: Succès
          content:
            application/json:
              schema:
                $ref: "#/components/schemas/Device"

        "404":
          description: Non trouvé
          content:
            application/json:
              schema:
                # utiliser un type commun pour les erreurs 404
                $ref: "#/components/schemas/ErrorNotFound"
```

Dans la spécification ci-dessus, nous avons défini deux endpoints de notre API et référencé les types que nous devons encore définir : `Device`, `ErrorNotFound` et `ULID`. Remarquez que pour le paramètre de chemin `deviceId`, nous avons également utilisé un type personnalisé au lieu d'une chaîne standard, ce qui peut être utile à l'avenir si nous voulons changer le format de nos ID (par exemple UUID, ULID, entier, etc.).

Remarquez que chaque opération a un `operationId` unique. Bien que ce soit optionnel, il est très utile d'en définir un, afin qu'il puisse être utilisé côté serveur et client.

Il s'agit d'une configuration de base que vous pouvez étendre davantage si vous le souhaitez. Par exemple, lors de la diffusion de ce schéma dans Swagger, il est bon de voir les exemples de nos requêtes (et leurs variations). Nous pouvons le définir ici dans la section `responses`, ou directement dans nos `components.schemas`.

```yaml
responses:
  "200":
    content:
      application/json:
        examples:
          new_device:
            value: # toute valeur
```

### Schémas

`components` est une partie intégrale de l'OAS, et contient les propriétés suivantes :

* schemas

* responses

* parameters

* requestBodies

* headers

* securitySchemes

Vous pouvez [tout voir ici](https://spec.openapis.org/oas/latest.html#components-object).

Nous pourrions définir notre type `Device` comme ceci :

```yaml
components:
  schemas:
    Device:
      type: object
      properties:
        id:
          $ref: '#/components/schemas/ULID'
        name:
          type: string
      required:
        - id
        - name
```

Mais plus tard, vous pourriez avoir d'autres types qui ont des champs `name` ou `id`, il est donc recommandé de les définir séparément et de les combiner dans le type final en utilisant `allOf` :

```yaml
components:
  schemas:
    WithId:
      type: object
      required:
        - id
      properties:
        id:
          $ref: "#/components/schemas/ULID"

    WithName:
      type: object
      required:
        - name
      properties:
        name:
          type: string

    Device:
      allOf:
        - $ref: "#/components/schemas/WithId"
        - $ref: "#/components/schemas/WithName"
```

`allOf`, `oneOf`, et `anyOf` sont des techniques très puissantes pour modéliser votre OAS.

### Extensions

Les schémas OpenAPI peuvent être étendus avec des propriétés internes qui n'affectent pas le schéma lui-même, mais sont utiles pour les générateurs de serveur ou de client. Un bon exemple est notre type [ULID](https://github.com/ulid/spec) pour les identifiants :

```yaml
ULID:
  type: string
  minLength: 26
  maxLength: 26

  # exemple utile pour la documentation Swagger
  example: 01ARZ3NDEKTSV4RRFFQ69G5FAV

  x-go-type: ulid.ULID
  x-go-type-import:
    path: github.com/oklog/ulid/v2
```

Les propriétés `x-` seront utilisées par le générateur de serveur Go pour utiliser les types Go existants pour ce champ au lieu d'en générer un nouveau.

## Comment générer un serveur Go

Nous n'avons pas passé en revue toutes les propriétés possibles du schéma ici et nous avons simplement couvert les principales - donc si vous n'êtes pas familier avec l'OAS, vous devriez maintenant avoir une bonne compréhension de ce standard. Vous pouvez lire la spécification complète [ici](https://spec.openapis.org/oas/latest.html). Mais maintenant que notre schéma est prêt, nous pouvons générer un serveur Go à partir de celui-ci.

Vous pouvez trouver la liste complète des générateurs sur [opeanapi.tools](https://openapi.tools/) - il y en a beaucoup. Mais le plus populaire pour les serveurs Go est [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen).

> oapi-codegen ne prend pas en charge cette OAS 3.1 pour le moment. [issue](https://github.com/oapi-codegen/oapi-codegen/issues/373). [ogen](https://github.com/ogen-go/ogen/) le fait, cependant.

Vous pouvez l'installer via `go install` :

```bash
go install github.com/oapi-codegen/oapi-codegen/v2/cmd/oapi-codegen@latest
```

La configuration pour le générateur `oapi-codegen` est simple. Vous pouvez soit fournir des arguments de ligne de commande, soit spécifier les mêmes arguments dans un fichier de configuration yaml. Vous pouvez choisir quel routeur HTTP utiliser pour le serveur, où placer le fichier de sortie, et plus encore. Dans notre cas, utilisons le routeur [echo](https://github.com/labstack/echo).

```yaml
# oapi-codegen.yaml

package: api
output: pkg/api/api.gen.go

generate:
  strict-server: true
  models: true
  echo-server: true
```

Nous pouvons maintenant générer le code du serveur en utilisant la commande suivante :

```bash
oapi-codegen --config=oapi-codegen.yaml openapi.yaml
```

Explorons maintenant le fichier généré `api.gen.go`.

Puisque nous avons activé `strict-server`, qui générera du code analysant les corps de requête et encodant les réponses automatiquement, l'interface que nous devons implémenter s'appelle `StrictServerInterface` :

```go
type StrictServerInterface interface {

  // Liste des appareils
  // (GET /devices)
  ListDevices(ctx context.Context, request ListDevicesRequestObject) (ListDevicesResponseObject, error)

  // Obtenir un appareil
  // (GET /devices/{deviceId})
  GetDevice(ctx context.Context, request GetDeviceRequestObject) (GetDeviceResponseObject, error)

}
```

Tous nos types sont également générés :

```go
type ULID = ulid.ULID

type Device struct {
	Id   ULID   `json:"id"`
	Name string `json:"name"`
}

// ...
```

Ainsi que le code pour analyser les requêtes automatiquement et la définition Swagger.

### Implémentation

Ce qu'il nous reste à faire est de créer un serveur en utilisant echo, d'implémenter l'interface générée et de tout assembler. Nous pouvons écrire le code suivant dans `pkg/api/impl.go` :

```go
package api

import "context"

type Server struct{}

func NewServer() Server {
	return Server{}
}

func (Server) ListDevices(ctx context.Context, request ListDevicesRequestObject) (ListDevicesResponseObject, error) {
	// implémentation réelle
	return ListDevices200JSONResponse{}, nil
}

func (Server) GetDevice(ctx context.Context, request GetDeviceRequestObject) (GetDeviceResponseObject, error) {
	// implémentation réelle
	return GetDevice200JSONResponse{}, nil
}
```

J'ai sauté la partie implémentation et j'ai simplement démontré comment retourner les réponses. Il est assez pratique que `oapi-codegen` ait généré toutes les réponses possibles pour nous.

Il nous reste à démarrer le serveur echo lui-même. Notez que nous n'avons pas besoin d'écrire manuellement les endpoints maintenant, et toute l'analyse des requêtes et des réponses est gérée pour nous. Cependant, nous devons valider les requêtes à l'intérieur de notre implémentation.

```go
package main

import (
	"oapiexample/pkg/api"

	"github.com/labstack/echo/v4"
)

func main() {
	server := api.NewServer()

	e := echo.New()

	api.RegisterHandlers(e, api.NewStrictHandler(
		server,
		// ajouter les middlewares ici si nécessaire
		[]api.StrictMiddlewareFunc{},
	))

	e.Start("127.0.0.1:8080")
}
```

Maintenant, lorsque nous exécutons notre serveur en utilisant `go run .`, nous pouvons faire un curl sur `localhost:8080/devices` pour voir la réponse !

### Serveurs supportés

`oapi-codegen` supporte de nombreux frameworks/serveurs web, tels que Chi, Fiber, Gin ainsi que le `net/http` standard.

### Comment visualiser la documentation de l'API

Parfois, il est pratique d'avoir la documentation Swagger livrée avec votre API - pour les tests, par exemple, ou simplement comme documentation publique. `oapi-codegen` ne génère pas l'interface utilisateur Swagger directement, mais nous pouvons avoir une simple page HTML qui contient un Swagger JS qui charge notre OAS.

Vous pouvez trouver le code HTML pour notre `pkg/api/index.html` [ici](https://swagger.io/docs/open-source-tools/swagger-ui/usage/installation/).

Et ensuite, nous pouvons utiliser `go:embed` pour intégrer les fichiers statiques et ajouter notre endpoint Swagger :

```go
//go:embed pkg/api/index.html
//go:embed openapi.yaml
var swaggerUI embed.FS

func main() {
	// ...

	// servir les docs swagger
	e.GET("/swagger/*", echo.WrapHandler(http.StripPrefix("/swagger/", http.FileServer(http.FS(swaggerUI)))))
}
```

Maintenant, nous pouvons visiter `localhost:8080/swagger/` pour voir l'interface utilisateur Swagger avec notre OAS.

![Swagger UI](https://substackcdn.com/image/fetch/w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9d35f8f-e1e7-4e51-9149-e180bb192fd8_1092x922.png align="left")

Des outils comme Postman sont très populaires pour la documentation des API, et il est également possible d'[importer](http://learning.postman.com/docs/integrations/available-integrations/working-with-openAPI/) vos définitions OpenAPI 3.0 et 3.1 existantes dans Postman. Postman supporte les formats YAML et JSON.

### Générer OAS à partir du code

Il existe également une pratique consistant à générer des schémas OpenAPI à partir du code, en particulier dans les langages typés. Cette approche a été populaire, le principal argument de vente étant que le fait de garder votre schéma OpenAPI près du code signifie que les développeurs le maintiennent à jour lorsqu'ils travaillent sur le code.

Ce n'est pas toujours le cas, ce qui est l'une des raisons pour lesquelles cette pratique est en train de disparaître. Et je ne suis pas non plus un grand fan, car je n'ai pas vu une grande valeur dans cela. Quoi qu'il en soit, vous pouvez jeter un coup d'œil aux projets suivants : [go-swagger](https://github.com/go-swagger/go-swagger), [swag](https://github.com/swaggo/swag), [swaggest/rest](https://github.com/swaggest/rest/).

## Code client

Comme mentionné précédemment, OpenAPI est très puissant pour la collaboration entre équipes, et tout ce que vous avez à faire maintenant est de versionner correctement votre schéma (voir la partie `info.version`) et de le distribuer aux équipes.

Cette partie peut être automatisée dans une certaine mesure en empaquetant votre schéma OpenAPI et en le rendant disponible. J'ai vu des développeurs utiliser des sous-modules Git pour cela ou des actions GitHub pour publier les schémas de version.

Supposons que notre client est une application web écrite en TypeScript, ce qui est assez courant pour les API web. Encore une fois, il existe de nombreux générateurs disponibles sur [opeanapi.tools](https://openapi.tools/) en ligne, mais le plus populaire est [openapi-typescript](https://openapi-ts.dev/).

Voici comment vous pouvez générer le code TypeScript pour les schémas locaux ou distants :

```bash
# Schéma local
npx openapi-typescript openapi.yaml -o ./client/schema.d.ts

# Schéma distant
npx openapi-typescript https://.../openapi.yaml -o ./client/schema.d.ts
```

## Conclusion

OpenAPI est un standard de facto pour la conception, l'implémentation et la consommation des API REST, il est donc crucial de comprendre comment cela fonctionne.

J'espère que cet article a fourni une introduction utile à la spécification OpenAPI, ainsi que des conseils pratiques et des exemples sur la façon d'utiliser l'OAS pour architecturer, implémenter et consommer des API.

### Ressources

* [Code source](https://github.com/plutov/packagemain/tree/master/oapi-example)

* [OpenAPI Initiative](https://www.openapis.org/)

* [openapi.tools](https://openapi.tools/)

* [Swagger Editor](https://editor.swagger.io/)

* [oapi-codegen](https://github.com/oapi-codegen/oapi-codegen)

* [Explorez plus d'articles sur packagemain.tech](https://packagemain.tech)