---
title: Comment implémenter l'injection de dépendances en Go - Expliqué avec des exemples
  de code
subtitle: ''
author: Gabor Koos
co_authors: []
series: null
date: '2025-09-24T19:22:45.098Z'
originalURL: https://freecodecamp.org/news/how-to-use-dependency-injection-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1758741125008/e796d218-2cf6-43ed-87a5-dfc772e121f8.png
tags:
- name: Go Language
  slug: go
- name: dependency injection
  slug: dependency-injection
- name: handbook
  slug: handbook
seo_title: Comment implémenter l'injection de dépendances en Go - Expliqué avec des
  exemples de code
seo_desc: Regardless of their initial size or scope, projects tend to grow in complexity
  over time. As new features are added and requirements evolve, the number of components
  and the connections between them multiply. Services, handlers, repositories, externa...
---

Quelle que soit leur taille ou leur portée initiale, les projets ont tendance à gagner en complexité avec le temps. À mesure que de nouvelles fonctionnalités sont ajoutées et que les exigences évoluent, le nombre de composants et les connexions entre eux se multiplient. Les services, les gestionnaires (handlers), les dépôts (repositories), les clients externes et bien d'autres s'entremêlent, ce qui rend de plus en plus difficile le suivi de qui dépend de quoi.

Ce réseau croissant de dépendances peut rapidement devenir un problème. Lorsque les relations entre les composants ne sont pas claires ou sont fortement couplées, la base de code devient plus difficile à tester, à refactoriser et à maintenir. Apporter des modifications ou ajouter de nouvelles fonctionnalités peut introduire des bogues inattendus, et isoler des parties du système pour les tests nécessite souvent d'importer bien plus que ce que vous aviez prévu.

Considérez une équipe travaillant sur un service backend. Au début, la base de code est gérable : quelques gestionnaires, une connexion à la base de données, peut-être un logger. Mais à mesure que le produit mûrit, de nouvelles exigences apparaissent : authentification, mise en cache, intégrations avec des API tierces, tâches de fond, et plus encore. Soudain, un seul gestionnaire peut avoir besoin d'accéder à plusieurs services, chacun ayant ses propres dépendances. L'équipe se retrouve à passer plus de temps à comprendre ce qui a besoin de quoi, et moins de temps à construire réellement des fonctionnalités. Les tests deviennent un casse-tête et la refactorisation semble risquée.

Pourquoi est-ce un tel défi ? Lorsque les dépendances sont cachées à l'intérieur des composants, il est difficile de voir comment tout s'assemble. Un code fortement couplé signifie qu'un changement à un endroit peut se répercuter de manière imprévisible dans tout le système. Il est facile de se retrouver avec un code fragile, difficile à tester, difficile à étendre et risqué à modifier.

Une façon de relever ce défi est l'injection de dépendances - souvent appelée DI (Dependency Injection). L'idée centrale est simple : au lieu que chaque partie d'un programme crée ses propres dépendances, ces dépendances sont fournies de l'extérieur. Cela rend les relations entre les composants explicites, permettant des tests plus faciles, le remplacement des implémentations et une plus grande flexibilité à mesure que le projet évolue.

La DI n'est pas une question de Frameworks ou de modèles d'entreprise, c'est une technique pratique pour structurer le code afin que la complexité reste gérable. En rendant les dépendances claires et configurables, la DI aide à maintenir le code adaptable, peu importe l'évolution des exigences.

Dans ce tutoriel, nous aborderons :

* Ce qu'est l'injection de dépendances en Go.
    
* Comment implémenter la DI manuelle, de manière idiomatique.
    
* Quand la DI manuelle devient encombrante.
    
* Les bibliothèques de DI populaires en Go.
    
* Les meilleures pratiques pour gérer les dépendances dans des projets réels.
    

À la fin de ce guide, vous aurez une compréhension claire de la DI en Go et saurez comment choisir la bonne approche pour vos projets.

## Ce que nous allons couvrir :

* [Prérequis](#heading-prerequis)
    
* [Qu'est-ce que l'injection de dépendances ?](#heading-qu-est-ce-que-l-injection-de-dependances)
    
* [DI manuelle en Go](#heading-di-manuelle-en-go)
    
    * [La couche Repository](#heading-la-couche-repository)
        
    * [La couche Service](#heading-la-couche-service)
        
    * [La couche Handler](#heading-la-couche-handler)
        
    * [Tout assembler dans main.go](#heading-tout-assembler-dans-maingo)
        
    * [Pourquoi la DI manuelle fonctionne bien en Go](#heading-pourquoi-la-di-manuelle-fonctionne-bien-en-go)
        
    * [Inconvénients de la DI manuelle](#heading-inconvenients-de-la-di-manuelle)
        
    * [Un exemple rapide de test](#heading-un-exemple-rapide-de-test)
        
    * [À retenir](#heading-a-retenir)
        
    * [Exercice pour le lecteur](#heading-exercice-pour-le-lecteur)
        
* [Quand la DI devient difficile](#heading-quand-la-di-devient-difficile)
    
    * [Dépendances imbriquées](#heading-dependances-imbriquees)
        
    * [Tester à grande échelle](#heading-tester-a-grande-echelle)
        
    * [Complexité de la configuration](#heading-complexite-de-la-configuration)
        
    * [Modèles pour atténuer la complexité](#heading-modeles-pour-attenuer-la-complexite)
        
    * [Quand les développeurs envisagent des Frameworks de DI](#heading-quand-les-developpeurs-envisagent-des-frameworks-de-di)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir)
        
* [Bibliothèques et outils de DI en Go](#heading-bibliotheques-et-outils-de-di-en-go)
    
    * [Google Wire (DI au temps de compilation)](#heading-google-wire-di-au-temps-de-compilation)
        
    * [Uber Dig (DI au temps d'exécution)](#heading-uber-dig-di-au-temps-d-execution)
        
    * [Uber Fx (DI + Cycle de vie de l'application)](#heading-uber-fx-di-cycle-de-vie-de-l-application)
        
    * [Autres aides de DI légers](#heading-autres-aides-de-di-legers)
        
* [Choisir le bon outil](#heading-choisir-le-bon-outil)
    
    * [Points clés à retenir](#heading-points-cles-a-retenir-1)
        
    * [Exercice pour le lecteur](#heading-exercice-pour-le-lecteur-1)
        
* [Meilleures pratiques et points à retenir](#heading-meilleures-pratiques-et-points-a-retenir)
    
    * [Préférer les dépendances explicites](#heading-preferer-les-dependances-explicites)
        
    * [Commencer simplement (DI manuelle)](#heading-commencer-simplement-di-manuelle)
        
    * [Utiliser des Frameworks pour maîtriser la complexité](#heading-utiliser-des-frameworks-pour-maitriser-la-complexite)
        
    * [Garder l'assemblage aux extrémités](#heading-garder-l-assemblage-aux-extremites)
        
    * [Privilégier les interfaces pour la testabilité](#heading-privilegier-les-interfaces-pour-la-testabilite)
        
    * [Éviter la sur-ingénierie](#heading-eviter-la-sur-ingenierie)
        
    * [Équilibrer verbosité et magie](#heading-equilibrer-verbosite-et-magie)
        
    * [Adopter progressivement](#heading-adopter-progressivement)
        
    * [Documenter votre assemblage](#heading-documenter-votre-assemblage)
        
    * [Points clés à retenir](#heading-points-cles-a-retenir-2)
        
* [Conclusion](#heading-conclusion)

## Prérequis

Cet article suppose que vous comprenez les bases de Go. Vous n'avez pas besoin d'être un expert, mais vous devriez être à l'aise avec :

* Les fonctions et les structs – comprendre comment définir des types et leurs méthodes.
    
* Les interfaces – savoir comment les déclarer et les implémenter.
    
* Les packages et les imports – organiser le code à travers les fichiers et les packages.
    
* Un serveur web Go basique – la familiarité avec `net/http` et les gestionnaires simples aidera lorsque nous construirons des exemples.
    

Si vous avez lu les guides précédents de freeCodeCamp sur les collections Go et les aides de la bibliothèque standard, vous êtes sur la bonne voie. Sinon, ne vous inquiétez pas - tous les exemples de code ici sont autonomes et expliqués étape par étape.

Vous aurez également besoin de :

* Go installé (1.20 ou plus récent recommandé)
    
* Un éditeur de texte ou un IDE de votre choix
    
* Être à l'aise pour exécuter `go run` depuis le terminal
    

C'est tout. Aucune bibliothèque spéciale n'est requise, sauf si nous les installons explicitement dans les sections suivantes (par exemple, lorsque nous explorerons `wire`, `dig` ou `fx`).

## Qu'est-ce que l'injection de dépendances ?

Commençons par un exemple simple. Imaginez un gestionnaire web qui récupère un utilisateur d'une base de données. Sans DI, cela pourrait ressembler à ceci :

```go
type UserService struct{}

func (us *UserService) GetUser(id int) string {
    // Imaginons que nous récupérons un utilisateur de la base de données
    return "user"
}

type Handler struct {
    userService UserService
}

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    user := h.userService.GetUser(1)
    fmt.Fprintln(w, user)
}
```

Ici, `Handler` est fortement couplé à `UserService`. Nous ne pouvons pas facilement remplacer `UserService` par un mock dans les tests ou le remplacer par une implémentation différente.

Avec l'injection de dépendances, nous passons la dépendance dans la struct, généralement via une fonction constructeur :

```go
type UserService interface {
    GetUser(id int) string
}

type Handler struct {
    userService UserService
}

func NewHandler(us UserService) *Handler {
    return &Handler{userService: us}
}
```

Maintenant, `Handler` ne se soucie pas de la façon dont le `UserService` est créé. Cette décision est laissée au code appelant (`main.go` ou un test). C'est l'essence de la DI : vous injectez ce dont un composant a besoin plutôt que de le laisser le créer en interne.

Cette approche présente plusieurs avantages :

* **Testabilité** : Vous pouvez facilement passer un mock ou un faux `UserService` lors du test de `Handler`.
    
* **Flexibilité** : Vous pouvez changer d'implémentation sans modifier `Handler`.
    
* **Séparation des préoccupations** : Chaque composant se concentre sur sa propre logique sans se soucier de la façon dont ses dépendances sont créées.
    

Comme vous pouvez le voir, le concept est assez simple, mais il a des implications puissantes sur la façon dont vous structurez votre code. Gérer explicitement les dépendances présente de nombreux avantages et presque aucun inconvénient. Peut-être devez-vous écrire un peu de code répétitif (boilerplate) supplémentaire, mais c'est un petit prix à payer pour la clarté et la flexibilité que cela apporte.

Le principe de l'injection de dépendances n'est pas unique à Go, c'est un principe général de conception logicielle que vous pouvez trouver dans de nombreux langages de programmation. Cependant, la façon dont vous l'implémentez peut varier selon le langage, l'écosystème et votre cas d'utilisation spécifique. C'est un thème récurrent dans les modèles de conception de haut niveau : ils vous disent quoi accomplir, mais ne s'occupent pas des détails de la mise en œuvre.

Ainsi, l'idée clé est de gérer explicitement les dépendances en les transmettant, plutôt que de laisser les composants les récupérer ou les créer eux-mêmes. Cela peut se faire de plusieurs manières :

* **Injection par constructeur** : Comme indiqué ci-dessus, les dépendances sont fournies via des fonctions constructeurs. C'est la manière la plus courante et la plus idiomatique en Go.
    
* **Injection par champ** : Les dépendances sont définies directement sur les champs de la struct. C'est moins courant en Go et non considéré comme idiomatique, mais cela peut être utile dans certains scénarios.
    
* **Injection par méthode** : Les dépendances sont passées en paramètres aux méthodes. C'est également moins courant en Go, mais peut être utile dans certaines situations.
    

L'approche la plus universelle en Go est l'injection par constructeur. L'injection par champ et par méthode est moins fréquente, principalement parce qu'elles peuvent conduire à un code moins clair et à des dépendances plus difficiles à suivre (il est toujours préférable de voir ce dont un composant a besoin dès le départ dans le constructeur plutôt que de l'avoir caché dans des appels de méthode ou des affectations de champs).

## DI manuelle en Go

La manière la plus courante et la plus idiomatique de gérer les dépendances en Go est de les assembler manuellement. Cela peut paraître ennuyeux, mais c'est en fait l'une des forces de Go : vous savez toujours d'où vient une dépendance, et rien n'est caché derrière un Framework. Surtout si vous injectez des dépendances via des constructeurs, il est toujours clair ce dont un composant a besoin pour fonctionner correctement. Cette explicitation est une partie clé de la philosophie de Go : vous rendez les dépendances évidentes et explicites, afin que quiconque lisant le code puisse facilement comprendre comment les composants s'assemblent.

Construisons une petite application web avec trois couches pour voir comment cela fonctionne en pratique :

* Un **repository** qui communique avec la base de données.
    
* Un **service** qui contient la logique métier.
    
* Un **handler** qui expose un point de terminaison HTTP.
    

Nous assemblerons ensuite ces pièces ensemble dans `main.go`.

### La couche Repository

Au bas de la pile, nous définirons un `UserRepository`. Dans un projet réel, celui-ci communiquerait avec une base de données, mais pour simplifier, nous retournerons simplement des données fictives.

```go
type UserRepository struct {
    // Imaginez que cette struct contient un client de base de données
}

func NewUserRepository() *UserRepository {
    return &UserRepository{}
}

func (r *UserRepository) FindUser(id int) string {
    // Dans une application réelle, cela interrogerait la base de données
    return fmt.Sprintf("user-%d", id)
}
```

L'élément clé ici est le constructeur `NewUserRepository()`. C'est une convention Go :

* Les fonctions nommées `NewXxx` créent et retournent de nouvelles instances.
    
* Elles rendent l'assemblage des dépendances explicite.
    

(Nous l'appelons un "constructeur" parce que Go n'a pas de constructeurs au sens traditionnel de la POO. Au lieu de cela, nous utilisons des fonctions qui retournent des structs initialisées, ce qui est plus proche des fonctions d'usine, mais le terme "constructeur" est couramment utilisé dans le jargon Go.)

### La couche Service

Au-dessus du repository, nous ajouterons un service qui l'utilise :

```go
type UserService struct {
    repo *UserRepository
}

func NewUserService(r *UserRepository) *UserService {
    return &UserService{repo: r}
}

func (s *UserService) GetUser(id int) string {
    // Ajoutez de la logique métier ici
    return s.repo.FindUser(id)
}
```

Le `UserService` dépend du repository. Notez que la dépendance est passée dans le "constructeur". C'est l'injection de dépendances en action : au lieu que `UserService` crée son propre repository, nous lui en donnons un.

Cela rend également le service facile à tester. Dans les tests, nous pouvons passer un faux repository au lieu du vrai.

### La couche Handler

Enfin, au sommet, ajoutons un gestionnaire web. C'est ce qui répond aux requêtes HTTP :

```go
type Handler struct {
    service *UserService
}

func NewHandler(s *UserService) *Handler {
    return &Handler{service: s}
}

func (h *Handler) ServeHTTP(w http.ResponseWriter, r *http.Request) {
    user := h.service.GetUser(1)
    fmt.Fprintln(w, user)
}
```

Le gestionnaire dépend du service. Encore une fois, nous injectons la dépendance via le constructeur.

### Tout assembler dans `main.go`

Maintenant, nous devons assembler les pièces. En partant du bas vers le haut, nous créons le repository, puis le service, et enfin le gestionnaire. Cela se fait dans `main.go` :

```go
func main() {
    repo := NewUserRepository()      // couche la plus basse
    service := NewUserService(repo)  // dépend du repo
    handler := NewHandler(service)   // dépend du service

    http.Handle("/user", handler)
    http.ListenAndServe(":8080", nil)
}
```

Ici, `main()` est responsable de tout assembler. C'est une façon simple et claire de gérer les dépendances :

* Chaque composant déclare ce dont il a besoin via son constructeur.
    
* `main()` crée et connecte tout.
    
* Le flux de dépendances est explicite et facile à suivre.
    
* Pas de magie cachée : tout est du code Go pur, sans Frameworks ni réflexion.
    

Si vous exécutez ce programme et visitez `http://localhost:8080/user`, vous verrez :

```bash
user-1
```

C'est tout. Nous avons injecté manuellement chaque dépendance et tout assemblé dans `main()`. Nous avons un contrôle total sur la façon dont les composants sont créés et connectés. Nous pouvons facilement changer d'implémentation, ajouter de nouvelles couches ou modifier l'assemblage selon les besoins.

### Pourquoi la DI manuelle fonctionne bien en Go

Ce style de gestion des dépendances est le choix par défaut en Go. Il présente plusieurs avantages :

* Dépendances explicites et claires : Chaque dépendance est visible dans le constructeur. Si `UserService` a besoin d'un repository, vous le voyez directement dans `NewUserService()`. Rien n'est caché.
    
* Pas de magie : Il n'y a pas d'astuces de réflexion, pas de conteneurs cachés, pas d'annotations. Quand vous regardez `main.go`, vous voyez exactement comment l'application est assemblée.
    
* Facile à tester : Parce que les dépendances sont injectées, vous pouvez passer des mocks ou des stubs dans les tests. Par exemple, vous pourriez créer un `FakeUserRepository` et le passer à `NewUserService()` dans un test unitaire. (Et votre `fakeUserRepository` ressemblerait probablement au `UserRepository` ci-dessus.)
    
* Idéal pour les petites et moyennes applications : Pour la plupart des projets, cette approche est tout ce dont vous avez besoin. De nombreux services Go en production dans de grandes entreprises n'utilisent rien de plus que la DI manuelle.
    

### Inconvénients de la DI manuelle

Bien sûr, rien n'est parfait. La DI manuelle présente certains inconvénients, surtout à mesure que votre application grandit :

* `main.go` verbeux : À mesure que le nombre de services augmente, `main.go` peut devenir un mur de code d'assemblage. Vous pouvez avoir des dizaines de lignes rien que pour créer et transmettre des dépendances. La même approche qui fonctionne si bien pour les petites ou moyennes applications peut devenir encombrante dans de très grands projets.
    
* Dépendances imbriquées : Imaginez que le service A dépend du service B, qui dépend du service C, qui dépend d'un repository. Au moment où vous assemblez tout dans `main.go`, vous pourriez vous retrouver avec de longues chaînes d'appels de constructeurs. Contrairement à notre exemple précédent, imaginez des centaines de services et de dépôts. Cela peut rendre le code d'assemblage presque impossible à lire et à maintenir.
    
* Difficulté de mise à l'échelle : Dans les très grandes applications comportant de nombreux modules, il peut être difficile de suivre quel service dépend de quel autre service. Une fois que votre application atteint une certaine taille, la DI manuelle peut ne plus suffire. C'est là que divers Frameworks de DI entrent en jeu, comme nous le verrons bientôt.
    

### Un exemple rapide de test

Pour voir l'avantage de la DI manuelle, écrivons un test rapide. Supposons que nous voulions tester `UserService` sans toucher au vrai repository. Nous pouvons définir un faux repository :

```go
type FakeUserRepository struct{}

func (f *FakeUserRepository) FindUser(id int) string {
    return "fake-user"
}
```

Et ensuite injecter cela dans le service :

```go
func TestUserService(t *testing.T) {
    fakeRepo := &FakeUserRepository{}
    service := NewUserService(fakeRepo)

    got := service.GetUser(1)
    want := "fake-user"

    if got != want {
        t.Errorf("got %s, want %s", got, want)
    }
}
```

Ce test n'est possible que parce que nous avons injecté la dépendance. Si `UserService` avait créé son propre repository en interne, nous ne pourrions pas le remplacer.

### À retenir

La DI manuelle en Go est simple, explicite et puissante. C'est la manière idiomatique de gérer les dépendances dans les applications Go. Pour de nombreux projets, c'est tout ce dont vous aurez besoin. Dans un monde idéal, cet article s'arrêterait ici et tout le monde pourrait continuer son chemin pour construire de superbes logiciels.

Mais comme nous le verrons dans la section suivante, lorsque votre projet s'agrandit et que votre code d'assemblage devient incontrôlable, la DI manuelle peut commencer à devenir pénible. C'est alors que les développeurs cherchent souvent des Frameworks ou des outils pour les aider.

### Exercice pour le lecteur

Nous avons fourni tous les extraits de code pertinents dans cette section, mais vous pouvez essayer de construire l'application complète vous-même. Créez un nouveau module Go, ajoutez les couches repository, service et handler comme indiqué, et assemblez-les dans `main.go`. Lancez le serveur et visitez le point de terminaison pour le voir en action. Ensuite, essayez d'écrire un test pour `UserService` en utilisant un faux repository. Cette pratique pratique aidera à consolider votre compréhension de la DI manuelle en Go.

## Quand la DI devient difficile

L'injection de dépendances manuelle fonctionne magnifiquement dans les projets Go de petite à moyenne taille. Elle est explicite, testable et facile à comprendre. Mais à mesure que votre application grandit, l'assemblage manuel des dépendances peut devenir fastidieux. Dans cette section, nous explorerons les points de friction qui apparaissent lors de la mise à l'échelle de la DI manuelle, et pourquoi les développeurs se tournent parfois vers des Frameworks ou des bibliothèques de DI.

### Dépendances imbriquées

Considérez un projet légèrement plus grand avec plusieurs services :

* `AuthService` dépend de `UserService`.
    
* `UserService` dépend de `UserRepository`.
    
* `EmailService` dépend d'un `SMTPClient`.
    
* `NotificationService` dépend à la fois d' `EmailService` et de `SMSService`.
    
* `Handler` dépend d' `AuthService` et de `NotificationService`.
    

Si vous essayez d'assembler tout cela manuellement, votre `main.go` commence à ressembler à ceci :

```go
func main() {
    userRepo := NewUserRepository()
    userService := NewUserService(userRepo)
    authService := NewAuthService(userService)

    smtpClient := NewSMTPClient("smtp.example.com")
    emailService := NewEmailService(smtpClient)
    smsService := NewSMSService()
    notificationService := NewNotificationService(emailService, smsService)

    handler := NewHandler(authService, notificationService)

    http.Handle("/signup", handler)
    http.ListenAndServe(":8080", nil)
}
```

Cet exemple est déjà verbeux et difficile à lire, même si l'application n'est pas très grande. Imaginez ce qui se passe lorsque des dizaines de services et de dépôts sont impliqués.

Problèmes que vous pourriez remarquer :

* Longues chaînes de dépendances : Les services dépendent d'autres services, qui dépendent de dépôts, qui pourraient dépendre de clients de base de données. La chaîne grandit rapidement et peut être difficile à gérer.
    
* Logique d'assemblage dans `main.go` : `main.go` se remplit d'appels de constructeurs. Bien qu'explicite, il peut être difficile de voir la structure globale de l'application d'un coup d'œil.
    
* Risque accru d'erreurs : Passer la mauvaise dépendance à un constructeur ou oublier d'assembler un nouveau service peut provoquer des erreurs d'exécution. La DI manuelle nécessite une attention particulière à mesure que les projets s'agrandissent.
    

### Tester à grande échelle

Un autre défi apparaît lors du test de grandes applications. Supposons que vous vouliez écrire des tests d'intégration pour `Handler` avec de fausses dépendances. Vous devrez créer manuellement des fakes ou des mocks pour chaque couche :

```go
fakeRepo := &FakeUserRepository{}
fakeUserService := NewUserService(fakeRepo)
fakeAuthService := NewAuthService(fakeUserService)
fakeEmailService := &FakeEmailService{}
fakeSMSService := &FakeSMSService{}
fakeNotificationService := NewNotificationService(fakeEmailService, fakeSMSService)
handler := NewHandler(fakeAuthService, fakeNotificationService)
```

Bien que cela fonctionne, la configuration des tests devient verbeuse et répétitive, surtout si plusieurs tests nécessitent différentes combinaisons de fausses dépendances. Cette verbosité peut rendre les tests très difficiles à maintenir.

### Complexité de la configuration

Certains services nécessitent une configuration ou des clients externes, tels que :

* Connexions aux bases de données
    
* Clients HTTP
    
* Clés API ou identifiants
    
* Frameworks de logging
    

Dans la DI manuelle, vous finissez souvent par écrire du code répétitif pour initialiser et transmettre ces dépendances :

```go
db := NewDatabase("postgres://user:pass@localhost:5432/db")
logger := NewLogger("INFO")
repo := NewUserRepository(db, logger)
service := NewUserService(repo, logger)
handler := NewHandler(service, logger)
```

À mesure que le nombre de dépendances augmente, il est facile d'oublier un paramètre requis ou de mal configurer un service. Cela peut entraîner des erreurs d'exécution difficiles à déboguer.

### Modèles pour atténuer la complexité

Même sans Frameworks, il existe des stratégies pour garder la DI manuelle gérable :

1. **Grouper les dépendances liées** : Si plusieurs services dépendent de la même configuration ou des mêmes clients, regroupez-les dans une struct :
    

```go
type AppDeps struct {
    DB     *Database
    Logger *Logger
}

func NewAppDeps() *AppDeps {
    db := NewDatabase("...")
    logger := NewLogger("INFO")
    return &AppDeps{DB: db, Logger: logger}
}
```

Cela réduit les paramètres de constructeur répétitifs :

```go
deps := NewAppDeps()
repo := NewUserRepository(deps.DB, deps.Logger)
service := NewUserService(repo, deps.Logger)
```

2. **Constructeurs par couches** : Créez des constructeurs de plus haut niveau pour les modules de fonctionnalités :
    

```go
func NewUserModule(deps *AppDeps) (*UserService, *UserHandler) {
    repo := NewUserRepository(deps.DB, deps.Logger)
    service := NewUserService(repo, deps.Logger)
    handler := NewHandler(service)
    return service, handler
}
```

Cela permet de garder `main.go` plus propre et d'encapsuler l'assemblage pour un module spécifique.

### Quand les développeurs envisagent des Frameworks de DI

Une fois que votre projet dépasse une poignée de services, la DI manuelle peut devenir un fardeau de maintenance :

* Longues chaînes de constructeurs
    
* Configuration de test verbeuse
    
* Code d'assemblage répétitif
    

C'est là que les bibliothèques de DI Go comme `Google Wire`, `Uber Dig` ou `Uber Fx` peuvent aider. Elles automatisent une partie de l'assemblage tout en gardant les dépendances explicites. Les Frameworks ne sont pas strictement nécessaires, mais ils peuvent rendre les projets à grande échelle plus gérables. Dans la section suivante, nous explorerons certaines bibliothèques de DI populaires en Go, leur fonctionnement et quand envisager de les utiliser.

### Points clés à retenir

* La DI manuelle est explicite, simple et idiomatique. Elle fonctionne mieux dans les petites et moyennes applications.
    
* À mesure que le nombre de dépendances augmente, `main.go` peut devenir long et répétitif.
    
* Tester des services complexes nécessite une configuration minutieuse de fakes ou de mocks.
    
* Des stratégies comme le regroupement de dépendances ou les constructeurs par couches peuvent réduire le code répétitif.
    
* Pour les très grandes applications, les Frameworks de DI peuvent aider à gérer l'assemblage, mais la DI manuelle reste le fondement du Go idiomatique.
    

## Bibliothèques et outils de DI en Go

Une fois que votre projet dépasse une poignée de services, l'assemblage manuel de toutes les dépendances peut devenir verbeux et sujet aux erreurs. C'est là que les bibliothèques d'injection de dépendances peuvent aider. Go ne vous oblige pas à les utiliser - la DI manuelle est toujours idiomatique - mais les Frameworks peuvent simplifier l'assemblage dans les projets plus importants.

Dans cette section, nous explorerons certains des outils de DI Go les plus populaires :

* Google Wire (DI au temps de compilation)
    
* Uber Dig (DI au temps d'exécution)
    
* Uber Fx (DI avec gestion du cycle de vie de l'application)
    
* Un bref aperçu d'autres aides de DI légers
    

Nous montrerons comment chacun fonctionne, avec des exemples, et discuterons du moment où les envisager.

### Google Wire (DI au temps de compilation)

[Google Wire](https://github.com/google/wire) est un outil de génération de code au temps de compilation. Vous définissez comment les dépendances sont liées entre elles, et Wire génère le code pour les assembler. Il n'y a pas de magie au moment de l'exécution, tout l'assemblage est explicite dans le code généré.

**Exemple : Wire en action**

Supposons que nous ayons un service simple avec un repository et un gestionnaire :

```go
type UserRepository struct{}
func NewUserRepository() *UserRepository { return &UserRepository{} }

type UserService struct { repo *UserRepository }
func NewUserService(r *UserRepository) *UserService { return &UserService{repo: r} }

type Handler struct { service *UserService }
func NewHandler(s *UserService) *Handler { return &Handler{service: s} }
```

Avec Wire, nous définissons un *provider set* et un *injector* :

```go
import "github.com/google/wire"

// Provider set
var Set = wire.NewSet(NewUserRepository, NewUserService, NewHandler)

// Injector function
func InitializeHandler() *Handler {
    wire.Build(Set) // génère le code ici pour assembler les dépendances
    return nil
}
```

`wire` dispose d'un outil CLI qui génère le code pour assembler vos dépendances. Lorsque vous exécutez `wire` dans votre projet, il génère le code Go pour `InitializeHandler()`, assemblant toutes les dépendances. Vous pouvez ensuite l'utiliser dans `main.go` :

```go
func main() {
    handler := InitializeHandler()
    http.Handle("/user", handler)
    http.ListenAndServe(":8080", nil)
}
```

En gros, vous définissez les dépendances dans le provider set, puis vous annotez la fonction injecteur avec `wire.Build(Set)`, et Wire génère le code répétitif pour vous dans cette fonction. Le code généré se trouve dans un fichier séparé.

Avantages :

* Pas de surcoût à l'exécution, l'assemblage se fait au temps de compilation.
    
* Le code généré est lisible et explicite.
    
* Sécurisé : les dépendances manquantes provoquent des erreurs de compilation.
    

Inconvénients :

* Nécessite un outil supplémentaire (CLI `wire`).
    
* Les fichiers générés ajoutent un peu de bruit à la base de code.
    
* Pas aussi flexible pour une configuration dynamique au moment de l'exécution.
    

### Uber Dig (DI au temps d'exécution)

[Uber Dig](https://github.com/uber-go/dig) est un conteneur d'injection de dépendances au temps d'exécution. Contrairement à Wire, Dig utilise la réflexion pour résoudre automatiquement les dépendances lorsque vous les invoquez.

**Exemple : Dig en action**

```go
import "go.uber.org/dig"

func main() {
    c := dig.New() // créer un nouveau conteneur

    // Fournir les constructeurs au conteneur
    c.Provide(NewUserRepository)
    c.Provide(NewUserService)
    c.Provide(NewHandler)

    // Invoquer la fonction, en laissant Dig résoudre les dépendances
    err := c.Invoke(func(h *Handler) {
        http.Handle("/user", h)
    })
    if err != nil {
        log.Fatal(err)
    }

    http.ListenAndServe(":8080", nil)
}
```

Ici, Dig inspecte les paramètres des constructeurs et fournit automatiquement les dépendances requises. Vous n'avez plus besoin de passer manuellement chaque dépendance dans `main()`. Il crée un conteneur, puis `Provide()` enregistre les constructeurs auprès du conteneur. Dig analyse les paramètres de chaque constructeur pour comprendre quelles dépendances sont nécessaires. Ensuite, `c.Invoke(func(h *Handler) { ... })` demande à Dig d'appeler la fonction fournie, en résolvant et en construisant automatiquement toutes les dépendances requises pour `*Handler` (en utilisant les constructeurs enregistrés).

Comment Dig résout les dépendances :

* Dig regarde `NewHandler` et voit qu'il a besoin d'un `*UserService`.
    
* Il regarde `NewUserService` et voit qu'il a besoin d'un `*UserRepository`.
    
* Il appelle les constructeurs dans le bon ordre, en passant les résultats au fur et à mesure, et fournit enfin le `*Handler` entièrement construit à votre fonction.
    

Cela ressemble-t-il à de la magie ? Un peu, mais tout est basé sur la réflexion et les constructeurs que vous fournissez. Vous gardez toujours le plein contrôle sur la façon dont les dépendances sont créées, mais Dig gère l'assemblage pour vous.

Avantages :

* Réduit l'assemblage manuel, surtout dans les grands projets.
    
* Flexible : facile de changer d'implémentation au moment de l'exécution.
    
* Fonctionne bien avec des configurations dynamiques.
    

Inconvénients :

* Utilise la réflexion, ce qui peut introduire des erreurs d'exécution si les dépendances sont mal configurées.
    
* Moins explicite : il n'est pas toujours évident de savoir comment une dépendance est résolue.
    
* Le débogage des problèmes de DI au moment de l'exécution peut être délicat.
    
* La réflexion peut avoir des implications sur les performances, bien qu'elles soient généralement négligeables.
    

### Uber Fx (DI + Cycle de vie de l'application)

[Uber Fx](https://github.com/uber-go/fx) s'appuie sur Dig et ajoute la gestion du cycle de vie de l'application. C'est idéal pour les grands microservices avec plusieurs modules et processus en arrière-plan.

**Exemple : Fx en action**

```go
import "go.uber.org/fx"

func registerRoutes(lc fx.Lifecycle, handler *Handler) {
    lc.Append(fx.Hook{
        OnStart: func(ctx context.Context) error {
            http.Handle("/user", handler)
            go http.ListenAndServe(":8080", nil)
            return nil
        },
        OnStop: func(ctx context.Context) error {
            log.Println("arrêt du serveur")
            return nil
        },
    })
}

func main() {
    app := fx.New(
        fx.Provide(NewUserRepository, NewUserService, NewHandler),
        fx.Invoke(registerRoutes),
    )

    app.Run() // démarre l'application et gère les hooks de cycle de vie
}
```

Fx utilise Dig sous le capot pour la DI, mais ajoute des hooks de cycle de vie pour gérer la logique de démarrage et d'arrêt. Vous pouvez enregistrer des fonctions à exécuter lorsque l'application démarre ou s'arrête, ce qui facilite la gestion des ressources comme les serveurs HTTP, les connexions aux bases de données, etc. Cela peut être particulièrement utile dans les microservices qui nécessitent des workers en arrière-plan, des connexions aux bases de données ou des tâches planifiées.

Fx fournit également une structure plus opinionnée pour votre application, encourageant les meilleures pratiques et facilitant le raisonnement sur votre code. L'inconvénient est qu'il introduit plus de complexité et une courbe d'apprentissage plus raide par rapport à la DI manuelle ou même à Dig seul.

Avantages :

* Simplifie les applications complexes avec la gestion du cycle de vie.
    
* Intègre la DI au démarrage et à l'arrêt de l'application.
    
* Bon pour les microservices et les projets à l'échelle de l'entreprise.
    

Inconvénients :

* Courbe d'apprentissage plus raide que la DI manuelle ou Wire.
    
* Vous enferme dans le Framework Fx.
    
* Un peu plus lourd que d'autres solutions. Peut sembler excessif pour de petites applications.
    

### Autres aides de DI légers

Outre Wire, Dig et Fx, il existe des outils plus petits comme :

* [do](https://github.com/samber/do) : Un conteneur de DI minimaliste qui se concentre sur la simplicité et la facilité d'utilisation. Il fournit des fonctionnalités de base pour enregistrer et résoudre des dépendances sans trop de surcoût.
    
* [alice](https://github.com/justinas/alice) : Une bibliothèque légère de chaînage de middleware qui peut aider à gérer les dépendances dans les gestionnaires HTTP, bien que ce ne soit pas un Framework de DI complet.
    

Ces bibliothèques sont moins couramment utilisées mais peuvent être utiles dans des scénarios spécifiques. Elles offrent généralement un juste milieu entre la DI manuelle et les Frameworks complets.

## Choisir le bon outil

Quelques considérations lors de la décision d'adopter une bibliothèque de DI :

| Facteur | Recommandation |
| --- | --- |
| Petit projet | Restez-en à la DI manuelle. L'explicite est simple et idiomatique. |
| Projet moyen avec plusieurs services | Envisagez Wire pour la sécurité au temps de compilation. |
| Grands microservices | Dig et Fx peuvent gérer l'assemblage et le cycle de vie. |
| Flexibilité des tests | Dig et Fx permettent de changer d'implémentation dynamiquement. |

Rappelez-vous : **la DI manuelle est toujours valide**. Les bibliothèques sont des outils optionnels pour réduire le code répétitif et améliorer la maintenabilité dans les grands systèmes. Elles ne doivent pas remplacer la compréhension du modèle sous-jacent.

### Points clés à retenir

* Les Frameworks de DI peuvent réduire la complexité de l'assemblage, mais la DI manuelle est toujours idiomatique et souvent suffisante.
    
* Wire : sécurité au temps de compilation, code généré explicite.
    
* Dig : réflexion au temps d'exécution, assemblage flexible.
    
* Fx : DI + cycle de vie de l'application, idéal pour les grands services.
    
* Autres outils : aides légers pour des cas d'utilisation spécifiques.
    

En comprenant ces outils, vous pouvez faire évoluer vos applications Go proprement tout en gardant les dépendances gérables, testables et explicites.

### Exercice pour le lecteur

Essayez d'intégrer l'une de ces bibliothèques de DI dans l'exemple d'application que nous avons construit plus tôt (ou toutes). Commencez par Wire pour voir comment fonctionne la DI au temps de compilation, puis expérimentez avec Dig ou Fx pour des scénarios plus complexes. Observez comment le code d'assemblage change et considérez les compromis en termes de complexité, de lisibilité et de maintenabilité. Consultez la documentation de chaque bibliothèque pour comprendre ses fonctionnalités et ses limites. Cette expérience pratique vous aidera à décider quand et comment utiliser les Frameworks de DI dans vos propres projets.

## Meilleures pratiques et points à retenir

Nous avons maintenant examiné l'injection de dépendances (DI) sous plusieurs angles : l'approche manuelle idiomatique, les défis qui apparaissent à grande échelle et les bibliothèques qui peuvent aider. La question logique suivante est : comment décider de ce qui convient à votre projet ?

Cette section résume les meilleures pratiques qui s'appliquent, que vous restiez fidèle à la DI manuelle ou que vous adoptiez un Framework. L'objectif est de vous aider à faire des choix pratiques et éclairés.

### Préférer les dépendances explicites

Le principe le plus important en Go est la clarté. Que vous écriviez un petit service ou que vous assembliez une grande application, rendez les dépendances explicites.

* Passez les dépendances par les constructeurs, pas par des variables globales cachées.
    
* Utilisez des interfaces pour abstraire le comportement lors des tests ou du remplacement des implémentations.
    
* Évitez la magie - les lecteurs doivent voir comment les choses sont connectées.
    

Exemple de DI explicite basée sur un constructeur :

```go
func NewOrderService(repo OrderRepository, logger Logger) *OrderService {
    return &OrderService{repo: repo, logger: logger}
}
```

Quiconque lit ce constructeur sait immédiatement que `OrderService` dépend d'un repository et d'un logger.

### Commencer simplement (DI manuelle)

Pour la plupart des projets Go, la DI manuelle suffit. Elle garde les choses simples, prévisibles et faciles à suivre.

* Dans les services de petite à moyenne taille, l'assemblage à la main dans `main.go` est rarement un goulot d'étranglement.
    
* L'assemblage explicite sert également de documentation : vous pouvez jeter un coup d'œil à `main.go` pour voir comment l'application est assemblée.
    
* Ajouter un Framework trop tôt peut ajouter de la complexité sans bénéfices clairs.
    

Une règle empirique utile : si votre assemblage tient confortablement sur un seul écran, la DI manuelle est probablement le meilleur choix.

### Utiliser des Frameworks pour maîtriser la complexité

Cela dit, les Frameworks existent pour une raison. Lorsque votre `main.go` se transforme en centaines de lignes de code répétitif, envisagez un outil de DI.

* Wire : idéal si vous voulez une sécurité au temps de compilation et un code généré explicite.
    
* Dig : idéal si vous voulez une flexibilité au temps d'exécution avec une configuration minimale.
    
* Fx : idéal si vous voulez à la fois la DI et la gestion du cycle de vie de l'application.
    

Considérez ces Frameworks comme des aides à la productivité, et non comme des substituts à la compréhension de la DI. Vous devriez toujours comprendre comment les dépendances circulent dans votre code, même si une bibliothèque les assemble pour vous.

### Garder l'assemblage aux extrémités

Une meilleure pratique courante consiste à séparer l'assemblage de la logique métier.

* La logique métier ne doit pas se soucier de la façon dont les dépendances sont construites.
    
* L'assemblage doit se faire au point d'entrée de l'application (`main.go` ou une fonction `initApp()`).
    
* Cette séparation permet de garder votre code central découplé et testable.
    

Structure d'exemple :

```bash
/cmd/app/main.go    <-- tout l'assemblage ici
/internal/service/  <-- logique métier
/internal/repo/     <-- accès aux données
```

De cette façon, les tests peuvent contourner entièrement l'assemblage et construire uniquement ce dont ils ont besoin.

### Privilégier les interfaces pour la testabilité

L'injection de dépendances brille lorsqu'il s'agit de tests. Pour en tirer le meilleur parti, dépendez d'interfaces plutôt que de types concrets.

Par exemple :

```go
type UserRepository interface {
    FindUser(id int) string
}

type UserService struct {
    repo UserRepository
}
```

En production, vous pouvez injecter un vrai `DBUserRepository`. Dans les tests, vous pouvez injecter un `FakeUserRepository`. Cela rend les tests rapides, isolés et faciles.

### Éviter la sur-ingénierie

Bien que les interfaces soient puissantes, leur utilisation excessive peut nuire à la lisibilité. Une bonne heuristique en Go est :

* S'il n'y a qu'une seule implémentation, vous n'avez probablement pas besoin d'une interface.
    
* Ajoutez des interfaces lorsque vous avez besoin de mocker quelque chose ou de changer d'implémentation.
    

Cela permet de garder votre base de code propre sans abstractions inutiles.

### Équilibrer verbosité et magie

Chaque stratégie de DI se situe sur un spectre :

* DI manuelle : explicitation maximale, mais verbeuse à grande échelle.
    
* Dig/Fx : moins verbeux, mais assemblage plus caché.
    
* Wire : juste milieu : le code généré est explicite, mais vous ne l'écrivez pas à la main.
    

Il n'y a pas de réponse unique. Le bon choix dépend de la taille de votre équipe, de la complexité du projet et de votre tolérance au code répétitif.

### Adopter progressivement

Vous n'avez pas besoin de vous engager dans un Framework de DI dès le premier jour. De nombreuses équipes :

* Commencent par la DI manuelle.
    
* À mesure que le projet grandit, refactorisent vers Wire pour la sécurité au temps de compilation.
    
* Si le projet évolue vers un service complexe avec de nombreux modules, adoptent Fx pour la gestion du cycle de vie.
    

Cette approche incrémentale garantit que vous n'ajoutez jamais plus de complexité que nécessaire.

### Documenter votre assemblage

Qu'il soit manuel ou basé sur un Framework, documentez la façon dont les dépendances sont assemblées.

* Dans la DI manuelle, `main.go` sert souvent de code auto-documenté.
    
* Avec les Frameworks, ajoutez des commentaires ou des diagrammes expliquant le flux.
    
* Les nouveaux contributeurs doivent pouvoir comprendre la structure sans deviner.
    

### Points clés à retenir

* Soyez explicite : rendez les dépendances visibles et testables.
    
* Commencez simplement : la DI manuelle fonctionne bien dans la plupart des projets.
    
* N'utilisez des Frameworks que lorsque c'est nécessaire : Wire, Dig et Fx ne peuvent aider à gérer la complexité que s'il *y a* de la complexité.
    
* Gardez l'assemblage aux extrémités : la logique métier doit rester propre et découplée.
    
* Suivez la philosophie de Go : préférez la clarté et la simplicité à l'ingéniosité.
    

En suivant ces meilleures pratiques, vous serez en mesure de gérer efficacement les dépendances en Go - que vous écriviez un minuscule outil CLI ou un microservice à grande échelle.

## Conclusion

L'injection de dépendances en Go n'a pas besoin d'être mystérieuse ou compliquée. À la base, il s'agit simplement de passer des dépendances à votre code plutôt que de les créer à l'intérieur. Ce petit changement de conception rend vos applications plus faciles à tester, plus modulaires et plus maintenables.

Nous avons vu les trois approches principales :

* DI manuelle : la base idiomatique en Go. Explicite, claire et idéale pour la plupart des projets.
    
* Outils au temps de compilation comme Wire : réduisent le code répétitif tout en gardant l'assemblage explicite.
    
* Frameworks au temps d'exécution comme Dig et Fx : puissants pour les grandes applications qui ont besoin de flexibilité et de gestion du cycle de vie.
    

Il n'y a pas de "bon" choix unique. La meilleure approche dépend de la taille et de la complexité de votre projet, des préférences de votre équipe et de la quantité d'assemblage que vous êtes prêt à gérer à la main.

Si vous ne deviez retenir qu'une chose de ce guide, que ce soit celle-ci : **commencez simplement avec la DI manuelle, et ne vous tournez vers des outils que lorsque le coût de l'assemblage à la main l'emporte sur les avantages de l'explicitation**.

En comprenant les compromis et en suivant les meilleures pratiques, vous serez bien équipé pour structurer des applications Go claires, testables et évolutives, que vous écriviez un minuscule service web ou un système distribué complet.