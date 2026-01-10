---
title: Comment gérer les abonnements GraphQL avec Go, GQLgen et MongoDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-05T22:02:32.000Z'
originalURL: https://freecodecamp.org/news/https-medium-com-anshap1719-graphql-subscriptions-with-go-gqlgen-and-mongodb-5e008fc46451
coverImage: https://cdn-media-1.freecodecamp.org/images/1*t6tknSDmtS0IcPRSRWDc8w.jpeg
tags:
- name: golang
  slug: golang
- name: GraphQL
  slug: graphql
- name: MongoDB
  slug: mongodb
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment gérer les abonnements GraphQL avec Go, GQLgen et MongoDB
seo_desc: 'By Anshul Sanghi

  Creating a real-time data server with GraphQL subscriptions and MongoDB ChangeStreams


  If you have used GQLgen in the past, you know that it indeed supports subscription
  models, but the implementation they use doesn’t exactly work wi...'
---

Par Anshul Sanghi

#### Création d'un serveur de données en temps réel avec les abonnements GraphQL et les ChangeStreams de MongoDB

![Image](https://cdn-media-1.freecodecamp.org/images/1*t6tknSDmtS0IcPRSRWDc8w.jpeg)

Si vous avez déjà utilisé GQLgen, vous savez qu'il supporte effectivement les modèles d'abonnement, mais l'implémentation qu'ils utilisent ne fonctionne pas exactement correctement avec MongoDB.

Pour ceux d'entre vous qui n'ont pas encore entendu parler ou utilisé GQLgen, c'est un package Go qui génère automatiquement du code boilerplate à partir de vos schémas GraphQL et vous fournit des fonctionnalités supplémentaires comme la configuration d'un serveur GraphQL, etc. Nous allons l'utiliser extensivement pour notre configuration GraphQL, donc je vous suggère d'aller y jeter un coup d'œil avant de continuer car je ne vais pas le couvrir beaucoup ici. Un bon point de départ serait [celui-ci](https://hackernoon.com/graphql-with-golang-6e8da2054c25).

Nous allons construire une API qui gère la création/interrogation/mise à jour d'un utilisateur et écoute lorsqu'un utilisateur a une nouvelle notification via un abonnement.

*J'ai dû apporter quelques modifications à mon code ainsi qu'au code généré par GQLgen pour que cela fonctionne correctement, mais je ne suis pas vraiment sûr que ce soit la meilleure façon de procéder d'un point de vue performance et j'aimerais avoir des suggestions. Cela ne couvrira pas non plus tout en détail sauf les parties nécessaires puisque le post est déjà assez long.*

### Installation

Configurons un projet de démarrage avant de plonger dans le code. Créez un nouveau projet dans votre `GOPATH` et créez un package `db` à l'intérieur. Ce répertoire contiendra tout le code lié à la base de données elle-même (dans ce cas, MongoDB).

Ensuite, installez les packages suivants requis :

```
go get github.com/99designs/gqlgengo get github.com/gorilla/muxgo get github.com/globalsign/mgo
```

Les packages suivants doivent être installés et sont uniquement utilisés par GQLgen en interne. Nous ne allons pas travailler directement avec ceux-ci mais ils sont requis :

```
go get github.com/pkg/errorsgo get github.com/urfave/cligo get golang.org/x/tools/go/ast/astutilgo get golang.org/x/tools/go/loadergo get golang.org/x/tools/importsgo get gopkg.in/yaml.v2
```

Nous sommes prêts à commencer à écrire du code :)

### Configuration du projet

Je vais utiliser le package `globalsign/mgo` pour Golang comme mon pilote MongoDB qui est essentiellement une version maintenue par la communauté de labix/mgo.v2. Consultez-le [ici](https://github.com/globalsign/mgo).

Dans votre répertoire db, créez un fichier `setup.go` avec le code suivant :

```
package dbimport (   "fmt"   "github.com/globalsign/mgo")
```

```
var session *mgo.Sessionvar db *mgo.Database
```

```
func ConnectDB() {   session, err := mgo.Dial("mongodb://localhost:27017,localhost:27018")
```

```
   if err != nil {      fmt.Println(err)   }   session.SetMode(mgo.Monotonic, true)   db = session.DB("subscriptionstest")}
```

```
func GetCollection(collection string) *mgo.Collection {   return db.C(collection)}
```

```
func CloseSession() {   session.Close()}
```

J'ai déjà configuré un ensemble de réplicas sur les ports `27017` et `27018`. Je vous suggère de faire de même à ce stade avant de continuer. Ensuite, créez un dossier `scripts` dans votre projet, et créez un nouveau fichier `gqlgen.go` avec le contenu suivant :

```
// +build ignorepackage mainimport "github.com/99designs/gqlgen/cmd"func main() {   cmd.Execute()}
```

Cela est juste requis pour exécuter le générateur et donc nous allons l'exclure de notre build.

Maintenant, créons un nouveau package `users` et créons un fichier `schema.graphql` avec le code suivant :

```
schema {    query: Query    mutation: Mutation}type Query {    user(id: ID!): User!}
```

```
type Mutation {    createUser(input: NewUser!): User!    updateUser(input: UpdateUser!): User!    updateNotification(input: UpdateNotification): User!}
```

```
type User {    id: ID!    first: String!    last: String!    email: String!    notifications: [Notification!]!}
```

```
type Notification {    id: ID!    seen: Boolean!    text: String!    title: String!}
```

```
input NewUser {    email: String!}input UpdateUser {    id: ID!    first: String    last: String    email: String}input UpdateNotification {    id: ID!    userID: ID!    seen: Boolean!}
```

```
type Subscription {    notificationAdded(id: ID!): User!}
```

Maintenant, naviguez jusqu'au dossier users depuis la ligne de commande et exécutez

```
go run ../scripts/gqlgen.go init
```

Cela générera 4 fichiers, à savoir `resolver.go` `generated.go` `models_gen.go` `gqlgen.yml`. Il créera également un dossier appelé server dans le package users qui contiendra le code pour exécuter le serveur GraphQL. Vous pouvez le supprimer car nous allons avoir notre propre serveur à la racine du projet, ce qui nous permettra également d'avoir éventuellement plusieurs points de terminaison GraphQL servis à partir d'un seul serveur.

Initialement, nous allons travailler uniquement avec `resolver.go` qui contient essentiellement la logique pour diverses requêtes et mutations que nous avons définies dans notre fichier de schéma. Mais d'abord, nous devons aller dans le fichier `models_gen.go` et ajouter le tag `bson:"_id"` à notre champ ID dans la structure utilisateur afin que nous puissions obtenir l'id de la base de données dans cette structure.

```
type User struct {   ID            string         `json:"id" bson:"_id"`   First         string         `json:"first"`   Last          string         `json:"last"`   Email         string         `json:"email"`   Notifications []Notification `json:"notifications"`}
```

Maintenant, configurons rapidement les résolveurs de base sans entrer dans les détails. Vous remarquerez qu'en haut du fichier, vous verrez un code similaire à ceci :

```
type Resolver struct{}func (r *Resolver) Mutation() MutationResolver {   return &mutationResolver{r}}func (r *Resolver) Query() QueryResolver {   return &queryResolver{r}}func (r *Resolver) Subscription() SubscriptionResolver {   return &subscriptionResolver{r}}
```

Nous allons le remplacer par ceci :

```
type Resolver struct {   users *mgo.Collection}func New() Config {   return Config{      Resolvers: &Resolver{         users: db.GetCollection("users"),      },   }}func (r *Resolver) Mutation() MutationResolver {   r.users = db.GetCollection("users")   return &mutationResolver{r}}func (r *Resolver) Query() QueryResolver {   r.users = db.GetCollection("users")   return &queryResolver{r}}func (r *Resolver) Subscription() SubscriptionResolver {   r.users = db.GetCollection("users")   return &subscriptionResolver{r}}
```

Nous faisons cela pour avoir une référence à notre collection directement dans la structure du résolveur, ce qui nous permettra de travailler plus facilement avec la collection tout au long des résolveurs. J'expliquerai l'importance de la fonction **New** plus tard lorsque nous en aurons besoin.

Configurons rapidement nos résolveurs de base.

#### Résolveur CreateUser

```
func (r *mutationResolver) CreateUser(ctx context.Context, input NewUser) (User, error) {   var user User   count, err := r.users.Find(bson.M{"email": input.Email}).Count()   if err != nil {      return User{}, err   } else if count > 0 {      return User{}, errors.New("user with that email already exists")   }   err = r.users.Insert(bson.M{"email": input.Email,})   if err != nil {      return User{}, err   }   err = r.users.Find(bson.M{"email": input.Email}).One(&user)   if err != nil {      return User{}, err   }   return user, nil}
```

#### Résolveur UpdateUser

```
func (r *mutationResolver) UpdateUser(ctx context.Context, input UpdateUser) (User, error) {   var fields = bson.M{}   var user User   update := false   if input.First != nil && *input.First != "" {      fields["first"] = *input.First      update = true   }   if input.Last != nil && *input.Last != "" {      fields["last"] = *input.Last      update = true   }   if input.Email != nil && *input.Email != "" {      fields["email"] = *input.Email      update = true   }   if !update {      return User{}, errors.New("no fields present for updating data")   }   err := r.users.UpdateId(bson.ObjectIdHex(input.ID), fields)   if err != nil {      return User{}, err   }   err = r.users.Find(bson.M{"_id": bson.ObjectIdHex(input.ID)}).One(&user)   if err != nil {      return User{}, err   }
```

```
   user.ID = bson.ObjectId(user.ID).Hex()
```

```
   return user, nil}
```

#### Résolveur UpdateNotification

```
func (r *mutationResolver) UpdateNotification(ctx context.Context, input *UpdateNotification) (User, error) {   var user User   var oid = bson.ObjectIdHex(input.UserID)   if err := r.users.Find(bson.M{"_id": oid}).One(&user); err != nil {      return User{}, err   }   for index, val := range user.Notifications {      if bson.ObjectId(val.ID).Hex() == input.ID {         val.Seen = input.Seen         user.Notifications[index] = val         break      }   }   if err := r.users.UpdateId(oid, user); err != nil {      return User{}, err   }   return user, nil}
```

#### Résolveur QueryUser

```
func (r *queryResolver) User(ctx context.Context, id string) (User, error) {   var user User   if err := r.users.FindId(bson.ObjectIdHex(id)).One(&user); err != nil {      return User{}, err   }   user.ID = bson.ObjectId(user.ID).Hex()   return user, nil}
```

Maintenant que nous avons terminé la configuration, passons à la partie principale.

### Données en temps réel MongoDB avec ChangeStreams

MongoDB supporte désormais les données en temps réel similaires à Firebase à partir de la **version 3.6**. La configuration n'est cependant pas aussi facile. Il y a quelques prérequis importants pour que les change streams fonctionnent correctement :

* Il n'est disponible que pour les clusters partagés et les ensembles de réplicas avec le pilote WireTiger. MongoDB v3.6+ ont WireTiger comme pilote par défaut mais nous devons configurer un ensemble de réplicas nous-mêmes.
* Change stream n'est disponible que si le support de la préoccupation de lecture `["majority"](https://docs.mongodb.com/manual/reference/read-concern-majority/#readconcern.%22majority%22)` est activé (il est activé par défaut).

Voici à quoi ressemblerait la signature de notre méthode pour le résolveur NotificationAdded :

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error) {   panic("not implemented")}
```

Il y a un problème avec cette implémentation et nous devons la modifier légèrement pour qu'elle fonctionne correctement. Mais d'abord, regardons le code requis dans le résolveur, ce qui nous aidera également à comprendre pourquoi le changement était nécessaire.

Nous allons d'abord définir les deux variables `userDoc` et `change` et configurer notre écouteur de changeStream comme suit :

```
var userDoc Uservar change bson.Mcs, err := r.users.Watch([]bson.M{}, mgo.ChangeStreamOptions{MaxAwaitTimeMS: time.Hour, FullDocument: mgo.FullDocument("updateLookup")})
```

```
if err != nil {   return err}if cs.Err() != nil {   fmt.Println(err)}
```

Ici, nous surveillons les changements dans la collection d'utilisateurs. Nous définissons également le délai d'attente pour ChangeStream à 1 heure. Cela est nécessaire pour garder le change stream actif et ne pas le fermer automatiquement. Nous allons également avoir besoin du document complet qui a été modifié et nous définissons donc ce paramètre dans les ChangeStreamOptions. La fonction watch retourne un curseur que nous pouvons ensuite parcourir.

Ensuite, nous allons démarrer une `goroutine` pour gérer les événements du curseur comme suit :

```
go func() {   start := time.Now()   for {      ok := cs.Next(&change)      if ok {         byts, _ := bson.Marshal(change["fullDocument"].(bson.M))         bson.Unmarshal(byts, &userDoc)         userDoc.ID = bson.ObjectId(userDoc.ID).Hex()         if userDoc.ID == id {            *userChan <- userDoc         }      }      if time.Since(start).Minutes() >= 60 {         break      }      continue   }}()
```

Ici, nous parcourons le curseur en utilisant la méthode `cursor.Next()` et une boucle for. Chaque fois qu'il y a un événement de changement, le code à l'intérieur de la boucle for sera exécuté et les données de cet événement seront disponibles pour nous dans la variable `change`.

Nous allons essentiellement extraire le champ de document complet de la structure de changement en tant que `type User` dans la boucle for. Nous vérifions ensuite si l'utilisateur modifié est le même que celui que l'abonnement recherche. Si c'est le cas, nous l'envoyons à notre canal et attendons d'autres événements.

C'est également un bon moment pour discuter de la signature de la méthode pour cette méthode. Une fois de plus, vous auriez quelque chose comme ceci :

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error) {   ...}
```

Il reçoit un id qui est l'userID et s'attend à ce qu'un canal soit retourné. Si nous retournons un canal à partir de cette fonction, il sera toujours vide. Regardons le fichier `generated.go` pour mieux comprendre cela. Le code lié à cette méthode particulière ressemblerait à quelque chose comme ceci (il est séparé dans le fichier mais j'agrège seulement le code requis ici) :

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error)}
```

```
func (ec *executionContext) _Subscription_notificationAdded(ctx context.Context, field graphql.CollectedField) func() graphql.Marshaler {   rawArgs := field.ArgumentMap(ec.Variables)   args, err := field_Subscription_notificationAdded_args(rawArgs)   if err != nil {      ec.Error(ctx, err)      return nil   }   ctx = graphql.WithResolverContext(ctx, &graphql.ResolverContext{      Field: field,   })      rctx := ctx   results, err := ec.resolvers.Subscription().NotificationAdded(rctx, args["id"].(string))   if err != nil {      ec.Error(ctx, err)      return nil   }   return func() graphql.Marshaler {      res, ok := <-results      if !ok {         return nil      }      var out graphql.OrderedMap      out.Add(field.Alias, func() graphql.Marshaler {         return ec._User(ctx, field.Selections, &res)      }())      return &out   }}
```

Le canal retourné est ensuite lu par le code généré pour obtenir les mises à jour et les transmettre à notre client. Le problème est que, une fois que nous retournons le canal de notre résolveur, l'exécution de cette fonction est déjà terminée. Cela signifie essentiellement que le canal ne recevra jamais de valeurs ici.

D'un autre côté, si des valeurs étaient ajoutées au canal avant de le retourner de la fonction, nous allons essentiellement devoir attendre une heure pour que toutes les mises à jour soient poussées vers le client puisque nous attendons une heure pour que les change streams se terminent (à condition que nous utilisions une implémentation non-goroutine pour notre curseur ChangeStream). Il est clair que ce n'est pas une situation idéale. Apportons quelques modifications au code ci-dessus pour qu'il fonctionne pour nous.

Je vais d'abord définir un canal dans la méthode **_Subscription_notificationAdded** dont le pointeur sera ensuite passé à notre résolveur. Cela ressemblerait à quelque chose comme ceci :

```
func (ec *executionContext) _Subscription_notificationAdded(ctx context.Context, field graphql.CollectedField) func() graphql.Marshaler {   rawArgs := field.ArgumentMap(ec.Variables)   args, err := field_Subscription_notificationAdded_args(rawArgs)   if err != nil {      ec.Error(ctx, err)      return nil   }   ctx = graphql.WithResolverContext(ctx, &graphql.ResolverContext{      Field: field,   })
```

```
   userChan := make(chan User, 1)   rctx := ctx   go ec.resolvers.Subscription().NotificationAdded(rctx, args["id"].(string), &userChan)
```

```
   return func() graphql.Marshaler {      res, ok := <-userChan      if !ok {         return nil      }      var out graphql.OrderedMap      out.Add(field.Alias, func() graphql.Marshaler {         return ec._User(ctx, field.Selections, &res)      }())      return &out   }}
```

Nous créons un nouveau canal avec une limite de 1 élément à la fois pour des raisons de performance. Nous passons ensuite son pointeur à notre résolveur et faisons également de l'appel à ce résolveur une goroutine.

La méthode **_Subscription_notificationAdded** retournera ensuite une fonction qui écoute le `userChan` et pousse la mise à jour vers notre client chaque fois qu'une valeur est reçue.

Nous devons également changer la signature de la méthode pour la méthode que nous venons de modifier, nous devons changer

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error)}
```

en

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string, userChan *chan User) error}
```

C'est toutes les modifications dont nous avons besoin. Une fois que c'est fait, voici à quoi ressemblerait le résolveur d'abonnement **NotificationAdded** complet :

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string, userChan *chan User) error {   var userDoc User   var change bson.M   cs, err := r.users.Watch([]bson.M{}, mgo.ChangeStreamOptions{MaxAwaitTimeMS: time.Hour, FullDocument: mgo.FullDocument("updateLookup")})   if err != nil {      return err   }   if cs.Err() != nil {      fmt.Println(err)   }   go func() {      start := time.Now()      for {         ok := cs.Next(&change)         if ok {            byts, _ := bson.Marshal(change["fullDocument"].(bson.M))            bson.Unmarshal(byts, &userDoc)            userDoc.ID = bson.ObjectId(userDoc.ID).Hex()            if userDoc.ID == id {               *userChan <- userDoc            }         }         if time.Since(start).Minutes() >= 60 {            break         }         continue      }   }()   return nil}
```

Maintenant, le code qui envoie un élément au canal et celui qui le reçoit sont tous deux non bloquants et s'exécutent en arrière-plan.

Ouf ! C'était beaucoup de travail, mais c'était tout le travail difficile que nous avions à faire. Passons à la partie amusante et créons un serveur pour voir le résultat de nos efforts.

### La partie amusante

Créez un fichier `main.go` à la racine de votre projet avec le code suivant :

```
package main
```

```
import (   "fmt"   "github.com/gorilla/mux"   "github.com/gorilla/websocket"   "github.com/rs/cors"      "log"   "net/http"   "os"   "github.com/99designs/gqlgen/handler"   "<project path relative to GOPATH>/users"   "<project path relative to GOPATH>/db")
```

```
const defaultPort = "8080"func main() {   port := os.Getenv("PORT")if port == "" {   port = defaultPort}
```

```
db.ConnectDB()
```

```
c := cors.New(cors.Options{   AllowedOrigins:   []string{"http://localhost:" + port},   AllowCredentials: true,})r := mux.NewRouter()r.Handle("/", handler.Playground("User", "/users"))r.Handle("/users", c.Handler(handler.GraphQL(users.NewExecutableSchema(users.New()),   handler.WebsocketUpgrader(websocket.Upgrader{      CheckOrigin: func(r *http.Request) bool {         return true      },   }))),)http.Handle("/", r)log.Fatal(http.ListenAndServe(":8080", nil))}
```

GQLgen nous fournit certains gestionnaires intégrés comme Playground et WebsocketUpgrader qui créent essentiellement une UI pour tester notre serveur GraphQL et pour avoir une connexion WebSocket avec les clients.

Aussi, rappelez-vous que nous avons ajouté une fonction appelée `**New**` à nos résolveurs plus tôt, que j'ai mentionné que nous en parlerions plus tard ? Eh bien, ici vous pouvez voir pourquoi c'était nécessaire. Elle retourne essentiellement une structure de configuration qui était requise par les gestionnaires fournis par GQLgen pour que notre code fonctionne correctement. Vous pouvez voir que le code par défaut utilise `users.Config{Resolvers: &users.Resolvers{}}` directement, ce qui est également bien tant que vous incluez le code pour le champ `users` dans la structure des résolveurs et le définissez sur la collection des utilisateurs.

À ce stade, nous sommes prêts à démarrer notre serveur GraphQL et à tester les choses.

Exécutez `go build` puis exécutez le fichier binaire généré. Le serveur devrait être en cours d'exécution maintenant. Assurez-vous que l'ensemble de réplicas MongoDB est en cours d'exécution avant d'essayer d'exécuter notre serveur, sinon il générera une erreur. Vous pouvez commencer [ici](https://docs.mongodb.com/manual/tutorial/deploy-replica-set-for-testing/) si vous avez besoin d'aide pour exécuter un ensemble de réplicas.

#### Créer un utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*L6xZoH6YqWpn7lhaI-qrsQ.png)

#### Mettre à jour un utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*9PYTvkFpdyKRQ9Z0RWLaLw.png)

#### Interroger un utilisateur

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUVMzZNj3Yp2hg6JsHf7Pg.png)

#### Abonnement NotificationAdded

Et voilà !

Je veux une fois de plus souligner que cela ne peut pas être la solution optimale au problème en question, mais c'est ma prise sur une solution possible et j'aimerais avoir vos commentaires et suggestions à ce sujet.

Merci d'avoir lu. Quelques ? sont toujours appréciés ?