---
title: Comment émuler des dépendances réelles dans les tests d'intégration en utilisant
  Testcontainers
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-08-14T19:55:12.123Z'
originalURL: https://freecodecamp.org/news/integration-tests-using-testcontainers
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723631770942/c82aabb6-a9b4-4085-8b06-b4ba1b1cdbd3.png
tags:
- name: Testing
  slug: testing
- name: Go Language
  slug: go
- name: Docker
  slug: docker
- name: containers
  slug: containers
seo_title: Comment émuler des dépendances réelles dans les tests d'intégration en
  utilisant Testcontainers
seo_desc: 'What is Integration Testing?

  The purpose of integration tests is to validate that different software components,
  subsystems, or applications work well together combined as a group.

  It’s an important step in the testing pyramid that can help you ident...'
---

## Qu'est-ce que les tests d'intégration ?

Le but des tests d'intégration est de valider que différents composants logiciels, sous-systèmes ou applications fonctionnent bien ensemble lorsqu'ils sont combinés en un groupe.

C'est une étape importante dans la pyramide des tests qui peut vous aider à identifier tout problème qui survient lorsque les composants sont combinés – par exemple, des problèmes de compatibilité, des incohérences de données ou des problèmes de communication.

Cet article est un guide pratique pour les tests d'intégration en Go utilisant Testcontainers. Nous définirons les tests d'intégration comme des tests de communication entre une application backend et des composants externes tels que la base de données et le cache.

## Table des matières

* [Différentes façons d'exécuter les tests d'intégration](#heading-different-ways-to-run-integration-tests)
    
* [Notre service de test : un simple raccourcisseur d'URL](#heading-our-guinea-pig-service-a-simple-url-shortener)
    
* [Tests unitaires avec des dépendances simulées](#heading-unit-tests-with-mocked-dependencies)
    
* [Tests d'intégration avec des dépendances réelles](#heading-integration-tests-with-real-dependencies)
    
* [Tests d'intégration avec Testcontainers](#heading-integration-tests-with-testcontainers)
    
* [Comment fonctionnent les Testcontainers](#heading-how-testcontainers-work)
    
* [Conclusion](#heading-conclusion)
    
* [Ressources](#heading-resources)
    

## Différentes façons d'exécuter les tests d'intégration

![Pyramide de test](https://miro.medium.com/v2/resize:fit:700/0*AbYCn0k0XzRIk3wR.png align="left")

Ce diagramme montre seulement 3 types de tests – mais il en existe d'autres : tests de composants, tests système, tests de charge, etc.

Alors que les tests unitaires sont faciles à exécuter (vous exécutez simplement les tests comme vous exécuteriez votre code), les tests d'intégration nécessitent généralement un certain échafaudage (mettre en place un environnement de test temporaire avec des bases de données et d'autres dépendances). Dans les entreprises où j'ai travaillé, j'ai vu les approches suivantes pour résoudre le problème de l'environnement de test d'intégration.

**Option 1 :** Utiliser des bases de données et autres dépendances jetables, qui doivent être provisionnées avant le début des tests d'intégration et détruites ensuite.

Selon la complexité de votre application, l'effort impliqué dans cette option peut être assez élevé, car vous devez vous assurer que l'infrastructure est opérationnelle et que les données sont préconfigurées dans un état spécifique souhaité.

**Option 2 :** Utiliser les bases de données et autres dépendances partagées existantes. Vous pouvez créer un environnement séparé pour les tests d'intégration ou même utiliser celui existant (par exemple, la préproduction) que les tests d'intégration peuvent utiliser.

Mais il y a de nombreux inconvénients ici, et je ne le recommanderais pas. Parce que c'est un environnement partagé, plusieurs tests peuvent s'exécuter en parallèle et modifier les données simultanément. Vous pouvez donc vous retrouver avec un état de données incohérent pour plusieurs raisons.

**Option 3 :** Utiliser des variations en mémoire ou embarquées des services requis pour les tests d'intégration. Bien que ce soit une bonne approche, toutes les dépendances n'ont pas de variations en mémoire, et même si c'est le cas, ces implémentations peuvent ne pas avoir les mêmes fonctionnalités que votre base de données de production.

**Option 4 :** Utiliser [Testcontainers](https://testcontainers.com/) pour démarrer et gérer vos dépendances de test directement dans votre code de test. Cela garantit une isolation complète entre les exécutions de test, une reproductibilité et une meilleure expérience CI. Nous allons nous pencher sur cela dans un instant.

## Notre service de test : un simple raccourcisseur d'URL

Pour démontrer les tests, nous utiliserons une API de raccourcisseur d'URL super simple écrite en Go. Elle utilise MongoDB pour le stockage des données et Redis comme [cache read-through](https://www.enjoyalgorithms.com/blog/read-through-caching-strategy). Elle dispose de deux endpoints que nous testerons dans nos tests :

* `/create?url=` génère le hachage pour une URL donnée et le stocke dans la base de données.
    
* `/get?key=` retourne l'URL originale pour une clé donnée.
    

Nous n'entrerons pas dans les détails des endpoints, mais vous pouvez trouver le code complet dans [ce dépôt Github](https://github.com/plutov/packagemain/blob/master/testcontainers-demo/main.go). Cependant, voyons comment nous définissons notre struct "server" :

```go
type server struct {
  DB    DB
  Cache Cache
}

func NewServer(db DB, cache Cache) (*server, error) {
  if err := db.Init(); err != nil {
    return nil, err
  }
  if err := cache.Init(); err != nil {
    return nil, err
  }
  return &server{DB: db, Cache: cache}, nil
}
```

La fonction **NewServer** nous permet d'initialiser un serveur avec les instances de base de données et de cache qui implémentent les interfaces DB et Cache.

```go
type DB interface {
  Init() error
  StoreURL(url string, key string) error
  GetURL(key string) (string, error)
}

type Cache interface {
  Init() error
  Set(key string, val string) error
  Get(key string) (string, bool)
}
```

## Tests unitaires avec des dépendances simulées

Parce que nous avons défini toutes les dépendances comme des interfaces, nous pouvons facilement générer des mocks pour elles en utilisant [mockery](https://github.com/vektra/mockery) et les utiliser dans nos tests unitaires.

```bash
mockery --all --with-expecter
go test -v ./...
```

Avec l'aide des tests unitaires, nous pouvons couvrir assez bien les composants de bas niveau de notre application : endpoints, logique de clé de hachage, etc. Tout ce dont nous avons besoin est de simuler les appels de fonctions des dépendances de la base de données et du cache.

unit\_test.go :

```go
func TestServerWithMocks(t *testing.T) {
  mockDB := mocks.NewDB(t)
  mockCache := mocks.NewCache(t)

  mockDB.EXPECT().Init().Return(nil)
  mockDB.EXPECT().StoreURL(mock.Anything, mock.Anything).Return(nil)
  mockDB.EXPECT().GetURL(mock.Anything).Return("url", nil)

  mockCache.EXPECT().Init().Return(nil)
  mockCache.EXPECT().Get(mock.Anything).Return("url", true)
  mockCache.EXPECT().Set(mock.Anything, mock.Anything).Return(nil)

  s, err := NewServer(mockDB, mockCache)
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  // les tests réels se déroulent ici, voir le code dans le dépôt
  testServer(srv, t)
}
```

`mocks.NewDB(t)` et `mocks.NewCache(t)` ont été générés automatiquement par mockery et nous utilisons `EXPECT()` pour simuler les fonctions. Remarquez que nous avons créé une fonction séparée `testServer(srv, t)` que nous utiliserons plus tard dans d'autres tests également, mais en fournissant une struct serveur différente.

Comme vous pouvez déjà le comprendre, ces tests unitaires ne testent pas les communications entre notre application et notre base de données/cache, et nous pouvons facilement manquer certains bugs très critiques.

Pour être plus confiant avec notre application, nous devrions écrire des tests d'intégration ainsi que des tests unitaires pour nous assurer que notre application est pleinement fonctionnelle.

## Tests d'intégration avec des dépendances réelles

Comme mentionné dans les options 1 et 2 ci-dessus, nous pouvons provisionner nos dépendances au préalable et exécuter nos tests contre ces instances. Une option serait d'avoir une configuration Docker Compose avec MongoDB et Redis, que nous démarrons avant les tests et arrêtons après. Les données de seed pourraient faire partie de cette configuration, ou être faites séparément.

compose.yaml :

```go
services:
  mongodb:
    image: mongodb/mongodb-community-server:7.0-ubi8
    restart: always
    ports:
      - "27017:27017"

  redis:
    image: redis:7.4-alpine
    restart: always
    ports:
      - "6379:6379"
```

realdeps\_test.go :

```go
//go:build realdeps
// +build realdeps

package main

func TestServerWithRealDependencies(t *testing.T) {
  os.Setenv("MONGO_URI", "mongodb://localhost:27017")
  os.Setenv("REDIS_URI", "redis://localhost:6379")

  s, err := NewServer(&MongoDB{}, &Redis{})
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  testServer(srv, t)
}
```

Maintenant, ces tests n'utilisent pas de mocks, mais se connectent simplement à la base de données et au cache déjà provisionnés. Remarque : nous avons ajouté une balise de build "realdeps" pour que ces tests doivent être exécutés en spécifiant explicitement cette balise.

```bash
docker-compose up -d
go test -tags=realdeps -v ./...
docker-compose down
```

## Tests d'intégration avec Testcontainers

Cependant, la création de dépendances de service fiables en utilisant Docker Compose nécessite une bonne connaissance des internes de Docker et de la meilleure façon d'exécuter des technologies spécifiques dans un conteneur. Par exemple, la création d'un environnement de test d'intégration dynamique peut entraîner des conflits de ports, des conteneurs qui ne sont pas entièrement en cours d'exécution et disponibles, et ainsi de suite.

Avec Testcontainers, nous pouvons maintenant faire la même chose – mais à l'intérieur de notre suite de tests, en utilisant notre API de langage. Cela signifie que nous pouvons mieux contrôler nos dépendances jetables et nous assurer qu'elles sont isolées pour chaque exécution de test. Vous pouvez exécuter presque n'importe quoi dans Testcontainers, tant qu'il dispose d'un runtime de conteneur compatible avec l'API Docker.

integration\_test.go :

```go
//go:build integration
// +build integration

package main

import (
  "context"
  "net/http/httptest"
  "os"
  "testing"
  "github.com/stretchr/testify/assert"
  "github.com/testcontainers/testcontainers-go/modules/mongodb"
  "github.com/testcontainers/testcontainers-go/modules/redis"
)

func TestServerWithTestcontainers(t *testing.T) {
  ctx := context.Background()

  mongodbContainer, err := mongodb.Run(ctx, "docker.io/mongodb/mongodb-community-server:7.0-ubi8")
  assert.NoError(t, err)
  defer mongodbContainer.Terminate(ctx)

  redisContainer, err := redis.Run(ctx, "docker.io/redis:7.4-alpine")
  assert.NoError(t, err)
  defer redisContainer.Terminate(ctx)

  mongodbEndpoint, _ := mongodbContainer.Endpoint(ctx, "")
  redisEndpoint, _ := redisContainer.Endpoint(ctx, "")

  os.Setenv("MONGO_URI", "mongodb://"+mongodbEndpoint)
  os.Setenv("REDIS_URI", "redis://"+redisEndpoint)

  s, err := NewServer(&MongoDB{}, &Redis{})
  assert.NoError(t, err)

  srv := httptest.NewServer(s)
  defer srv.Close()

  testServer(srv, t)
}
```

Cela est très similaire au test précédent : nous avons simplement initialisé deux conteneurs au début de notre test.

La première exécution peut prendre un certain temps pour télécharger les images. Mais les exécutions suivantes sont presque instantanées.

![Sortie de l'exécution des tests utilisant Testcontainers](https://miro.medium.com/v2/resize:fit:700/0*A3NirSvt1jkADZjq.png align="left")

## Comment fonctionnent les Testcontainers

Pour exécuter des tests avec Testcontainers, vous avez besoin d'un runtime de conteneur compatible avec l'API Docker ou d'installer Docker localement. Essayez d'arrêter votre moteur Docker et cela ne fonctionnera pas.

Mais cela ne devrait pas être un problème pour la plupart des développeurs, car avoir un runtime Docker dans votre CI/CD ou localement est une pratique très courante de nos jours. Vous pouvez facilement avoir cet environnement dans Github Actions, par exemple.

En ce qui concerne les langages supportés, Testcontainers supporte une grande liste de langages et plateformes populaires, y compris Java, .NET, Go, NodeJS, Python, Rust, Haskell, et autres.

Il existe également une liste croissante d'implémentations préconfigurées (appelées modules) que vous pouvez trouver [ici](https://testcontainers.com/modules/). Mais comme je l'ai mentionné précédemment, vous pouvez exécuter n'importe quelle image Docker.

En Go, vous pourriez utiliser le code suivant pour provisionner Redis au lieu d'utiliser un module préconfiguré :

```go
// Utilisation du module disponible
redisContainer, err := redis.Run(ctx, "redis:latest")

// Ou utilisation de GenericContainer
req := testcontainers.ContainerRequest{
  Image:        "redis:latest",
  ExposedPorts: []string{"6379/tcp"},
  WaitingFor:   wait.ForLog("Ready to accept connections"),
}

redisC, err := testcontainers.GenericContainer(ctx, testcontainers.GenericContainerRequest{
  ContainerRequest: req,
  Started:          true,
})
```

## Conclusion

Alors que le développement et la maintenance des tests d'intégration nécessitent des efforts significatifs, ils sont une partie cruciale du SDLC, garantissant que les composants, sous-systèmes ou applications fonctionnent bien ensemble lorsqu'ils sont combinés en un groupe.

En utilisant Testcontainers, nous pouvons simplifier le provisionnement et la désapprovisionnement des dépendances jetables pour les tests, rendant les exécutions de test entièrement isolées et plus prévisibles.

## Ressources

* [Dépôt Github](https://github.com/plutov/packagemain/blob/master/testcontainers-demo)
    
* [Testcontainers](https://testcontainers.com/)
    
* [Découvrez plus d'articles de packagemain.tech](https://packagemain.tech)