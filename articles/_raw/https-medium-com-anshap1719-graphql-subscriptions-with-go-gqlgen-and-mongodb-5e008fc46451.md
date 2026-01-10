---
title: How to handle GraphQL subscriptions with Go, GQLgen and MongoDB
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
seo_title: null
seo_desc: 'By Anshul Sanghi

  Creating a real-time data server with GraphQL subscriptions and MongoDB ChangeStreams


  If you have used GQLgen in the past, you know that it indeed supports subscription
  models, but the implementation they use doesn’t exactly work wi...'
---

By Anshul Sanghi

#### Creating a real-time data server with GraphQL subscriptions and MongoDB ChangeStreams

![Image](https://cdn-media-1.freecodecamp.org/images/1*t6tknSDmtS0IcPRSRWDc8w.jpeg)

If you have used GQLgen in the past, you know that it indeed supports subscription models, but the implementation they use doesn’t exactly work with MongoDB properly.

For those of you who haven’t heard of or used GQLgen yet, it is a go package that essentially generates boilerplate code automatically from your GraphQL schemas and provides you with added functionality like setting up a GraphQL server, etc. We are going to use this extensively for our GraphQL setup, so I suggest you go take a look at it before continuing as I won’t be covering it much here. A good starting point would be [this](https://hackernoon.com/graphql-with-golang-6e8da2054c25).

We are going to build an API that handles creating/querying/updating a user and listens when a user has a new notification via a subscription.

_I had to make some changes to my code as well as the GQLgen generated code to make it work properly, but I’m not really sure if this is the best way to go from a performance perspective and I would love to have any suggestions. This is also not going to cover everything into detail except for the required parts since the post is already long enough as is._

### Setup

Let’s set up a starter project before we dive into the code. Create a new project in your `GOPATH` and create a package `db` within it. This directory will contain all code related to the database itself (in this case, MongoDB).

Next, install the following required packages:

```
go get github.com/99designs/gqlgengo get github.com/gorilla/muxgo get github.com/globalsign/mgo
```

The following packages are required to be installed and are only used by GQLgen internally. We are not going to work with these directly but they are required:

```
go get github.com/pkg/errorsgo get github.com/urfave/cligo get golang.org/x/tools/go/ast/astutilgo get golang.org/x/tools/go/loadergo get golang.org/x/tools/importsgo get gopkg.in/yaml.v2
```

We are ready to start writing some code :)

### Project Setup

I’ll be using the `globalsign/mgo` package for Golang as my MongoDB driver which is essentially a community maintained version of labix/mgo.v2. Check it out [here](https://github.com/globalsign/mgo).

In your db directory, create a file `setup.go` with the following code:

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

I already have a replica-set set up on ports `27017` and `27018`. I suggest you do the same at this point before proceeding. Next, create a `scripts` folder in your project, and create a new file `gqlgen.go` with the following contents:

```
// +build ignorepackage mainimport "github.com/99designs/gqlgen/cmd"func main() {   cmd.Execute()}
```

This is just required to run the generator and so we are going to exclude it from our build.

Now, let’s create a new package `users` and create a file `schema.graphql` in it with the following code:

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

Now, navigate to the users folder from the command line and run

```
go run ../scripts/gqlgen.go init
```

This will generate 4 files, namely `resolver.go` `generated.go` `models_gen.go` `gqlgen.yml`. It will also create a folder called server within the users package which will hold the code for running the GraphQL server. You can remove that as we are going to have our own server at the root of the project which would also allow us to eventually have multiple GraphQL endpoints being served from a single server.

Initially, we will be working with only `resolver.go` which basically holds the logic for various queries and mutations we defined in our schema file. But first, we need to go to the `models_gen.go` file and add the `bson:"_id"` tag to our ID field in the user struct so that we can get the id from the database into this struct.

```
type User struct {   ID            string         `json:"id" bson:"_id"`   First         string         `json:"first"`   Last          string         `json:"last"`   Email         string         `json:"email"`   Notifications []Notification `json:"notifications"`}
```

Now, let’s quickly set up the basic resolvers without going into much detail. You’ll notice that at the top of the file, you’ll see some code similar to this:

```
type Resolver struct{}func (r *Resolver) Mutation() MutationResolver {   return &mutationResolver{r}}func (r *Resolver) Query() QueryResolver {   return &queryResolver{r}}func (r *Resolver) Subscription() SubscriptionResolver {   return &subscriptionResolver{r}}
```

We are going to replace it with this:

```
type Resolver struct {   users *mgo.Collection}func New() Config {   return Config{      Resolvers: &Resolver{         users: db.GetCollection("users"),      },   }}func (r *Resolver) Mutation() MutationResolver {   r.users = db.GetCollection("users")   return &mutationResolver{r}}func (r *Resolver) Query() QueryResolver {   r.users = db.GetCollection("users")   return &queryResolver{r}}func (r *Resolver) Subscription() SubscriptionResolver {   r.users = db.GetCollection("users")   return &subscriptionResolver{r}}
```

We are doing this so that we can have a reference to our collection directly within the resolver struct which would make it easier for us to work with the collection throughout the resolvers. I’ll explain the significance of the `**New**` function later when we need it.

Let’s quickly set up our basic resolvers.

#### CreateUser Resolver

```
func (r *mutationResolver) CreateUser(ctx context.Context, input NewUser) (User, error) {   var user User   count, err := r.users.Find(bson.M{"email": input.Email}).Count()   if err != nil {      return User{}, err   } else if count > 0 {      return User{}, errors.New("user with that email already exists")   }   err = r.users.Insert(bson.M{"email": input.Email,})   if err != nil {      return User{}, err   }   err = r.users.Find(bson.M{"email": input.Email}).One(&user)   if err != nil {      return User{}, err   }   return user, nil}
```

#### UpdateUser Resolver

```
func (r *mutationResolver) UpdateUser(ctx context.Context, input UpdateUser) (User, error) {   var fields = bson.M{}   var user User   update := false   if input.First != nil && *input.First != "" {      fields["first"] = *input.First      update = true   }   if input.Last != nil && *input.Last != "" {      fields["last"] = *input.Last      update = true   }   if input.Email != nil && *input.Email != "" {      fields["email"] = *input.Email      update = true   }   if !update {      return User{}, errors.New("no fields present for updating data")   }   err := r.users.UpdateId(bson.ObjectIdHex(input.ID), fields)   if err != nil {      return User{}, err   }   err = r.users.Find(bson.M{"_id": bson.ObjectIdHex(input.ID)}).One(&user)   if err != nil {      return User{}, err   }
```

```
   user.ID = bson.ObjectId(user.ID).Hex()
```

```
   return user, nil}
```

#### UpdateNotification Resolver

```
func (r *mutationResolver) UpdateNotification(ctx context.Context, input *UpdateNotification) (User, error) {   var user User   var oid = bson.ObjectIdHex(input.UserID)   if err := r.users.Find(bson.M{"_id": oid}).One(&user); err != nil {      return User{}, err   }   for index, val := range user.Notifications {      if bson.ObjectId(val.ID).Hex() == input.ID {         val.Seen = input.Seen         user.Notifications[index] = val         break      }   }   if err := r.users.UpdateId(oid, user); err != nil {      return User{}, err   }   return user, nil}
```

#### QueryUser Resolver

```
func (r *queryResolver) User(ctx context.Context, id string) (User, error) {   var user User   if err := r.users.FindId(bson.ObjectIdHex(id)).One(&user); err != nil {      return User{}, err   }   user.ID = bson.ObjectId(user.ID).Hex()   return user, nil}
```

Now that we are done with the setup, let’s move on to the main part.

### MongoDB Real-time Data With ChangeStreams

MongoDB now supports real-time data similar to firebase starting from **version 3.6**. The setup isn’t as easy though. There are a few important prerequisites for change streams to work properly:

* It is only available for shared clusters and replica sets with the WireTiger driver. MongoDB v3.6+ have WireTiger as the default driver but we do need to set up a replica set ourselves.
* Change stream is only available if `["majority"](https://docs.mongodb.com/manual/reference/read-concern-majority/#readconcern.%22majority%22)` read concern support is enabled (it is enabled by default).

Here’s what our method signature for NotificationAdded Resolver would look like:

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error) {   panic("not implemented")}
```

There’s a problem with this implementation and we’ll need to change it slightly to make it work properly. But first, let’s look at the code required within the resolver which will also make it easier for us to understand why the change was required.

We are first going to define the two variables `userDoc` and `change` and set up our changeStream listener like so:

```
var userDoc Uservar change bson.Mcs, err := r.users.Watch([]bson.M{}, mgo.ChangeStreamOptions{MaxAwaitTimeMS: time.Hour, FullDocument: mgo.FullDocument("updateLookup")})
```

```
if err != nil {   return err}if cs.Err() != nil {   fmt.Println(err)}
```

Here, we are watching for changes in the user collection. We are also setting the timeout for ChangeStream as 1 hour. This is required to keep the change stream alive and not close automatically. We are also going to need the full document that was changed and so we define that setting in the ChangeStreamOptions as well. The watch function returns a cursor which we can then iterate over.

Next, we are going to start a `goroutine` for handling cursor events like so:

```
go func() {   start := time.Now()   for {      ok := cs.Next(&change)      if ok {         byts, _ := bson.Marshal(change["fullDocument"].(bson.M))         bson.Unmarshal(byts, &userDoc)         userDoc.ID = bson.ObjectId(userDoc.ID).Hex()         if userDoc.ID == id {            *userChan <- userDoc         }      }      if time.Since(start).Minutes() >= 60 {         break      }      continue   }}()
```

Here we are iterating over the cursor using `cursor.Next()` method and a for loop. Whenever there’s a change event, the code inside the for loop will be executed and the data from that event will be available to us within the `change` variable.

We are essentially going to extract the full document field from the change struct as `type User` in the for loop. We then check if the changed user is the same as the one that the subscription is looking for. If so, we send it to our channel and wait for more events.

This is also a good time to discuss the method signature for this method. Once again, you’d have something like this:

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error) {   ...}
```

It receives an id which is the userID and expects that a channel is returned. If we return a channel from this function, it will always be empty. Let’s look at the `generated.go` file to better understand this. The code related to this particular method would look something like this (It’s separated across the file but I am aggregating only the required code here):

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error)}
```

```
func (ec *executionContext) _Subscription_notificationAdded(ctx context.Context, field graphql.CollectedField) func() graphql.Marshaler {   rawArgs := field.ArgumentMap(ec.Variables)   args, err := field_Subscription_notificationAdded_args(rawArgs)   if err != nil {      ec.Error(ctx, err)      return nil   }   ctx = graphql.WithResolverContext(ctx, &graphql.ResolverContext{      Field: field,   })      rctx := ctx   results, err := ec.resolvers.Subscription().NotificationAdded(rctx, args["id"].(string))   if err != nil {      ec.Error(ctx, err)      return nil   }   return func() graphql.Marshaler {      res, ok := <-results      if !ok {         return nil      }      var out graphql.OrderedMap      out.Add(field.Alias, func() graphql.Marshaler {         return ec._User(ctx, field.Selections, &res)      }())      return &out   }}
```

The returned channel is then read by the generated code to get the updates and pass it on to our client. The problem is, once we return the channel from our resolver, that function execution is already over. Basically meaning that the channel would never receive any values here.

On the flip side, if values were added to the channel before returning it from the function, we are essentially going to have to wait an hour for all the updates to be pushed to the client since we are waiting an hour for the change streams to timeout (provided that we use a non-goroutine implementation for our ChangeStream cursor). It’s clear that this is not an ideal situation. Let’s make some changes to the above code to make it work for us.

I’m first going to define a channel in the **_Subscription_notificationAdded** method whose pointer will then be passed to our resolver. It would look something like this:

```
func (ec *executionContext) _Subscription_notificationAdded(ctx context.Context, field graphql.CollectedField) func() graphql.Marshaler {   rawArgs := field.ArgumentMap(ec.Variables)   args, err := field_Subscription_notificationAdded_args(rawArgs)   if err != nil {      ec.Error(ctx, err)      return nil   }   ctx = graphql.WithResolverContext(ctx, &graphql.ResolverContext{      Field: field,   })
```

```
   userChan := make(chan User, 1)   rctx := ctx   go ec.resolvers.Subscription().NotificationAdded(rctx, args["id"].(string), &userChan)
```

```
   return func() graphql.Marshaler {      res, ok := <-userChan      if !ok {         return nil      }      var out graphql.OrderedMap      out.Add(field.Alias, func() graphql.Marshaler {         return ec._User(ctx, field.Selections, &res)      }())      return &out   }}
```

We are creating a new channel with a limit of 1 item at a time for performance reasons. We are then passing its pointer to our resolver and also making the call to this resolver a goroutine.

The **_Subscription_notificationAdded** method will then return a function that listens to the `userChan` and pushes the update to our client every time a value is received.

We also need to change the method signature for the method we just modified, we need to change

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string) (&lt;-chan User, error)}
```

to

```
type SubscriptionResolver interface {   NotificationAdded(ctx context.Context, id string, userChan *chan User) error}
```

That’s all the modification we need. Once that’s done, here’s what the complete **NotificationAdded Subscription Resolver** would look like:

```
func (r *subscriptionResolver) NotificationAdded(ctx context.Context, id string, userChan *chan User) error {   var userDoc User   var change bson.M   cs, err := r.users.Watch([]bson.M{}, mgo.ChangeStreamOptions{MaxAwaitTimeMS: time.Hour, FullDocument: mgo.FullDocument("updateLookup")})   if err != nil {      return err   }   if cs.Err() != nil {      fmt.Println(err)   }   go func() {      start := time.Now()      for {         ok := cs.Next(&change)         if ok {            byts, _ := bson.Marshal(change["fullDocument"].(bson.M))            bson.Unmarshal(byts, &userDoc)            userDoc.ID = bson.ObjectId(userDoc.ID).Hex()            if userDoc.ID == id {               *userChan <- userDoc            }         }         if time.Since(start).Minutes() >= 60 {            break         }         continue      }   }()   return nil}
```

Now the code that is sending an item to the channel and the one that is receiving it are both non-blocking and running in the background.

Phew! That was a lot of work but that was all the heavy lifting that we had to do. Let’s move on to the fun part and create a server and see the result of our efforts.

### The fun stuff

Create a file `main.go` at the root of your project with the following code:

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

GQLgen provides us with some built-in handlers like Playground and WebsocketUpgrader which essentially creates a UI for testing our GraphQL server and for having a WebSocket connection with the clients.

Also, remember we added a function called `**New**` to our resolvers earlier, which I mentioned that we’d talk about later? Well, here you can see why it was required. It essentially returned a Configuration struct that was required by the handlers provided by GQLgen for our code to work properly. You can see that the default code uses `users.Config{Resolvers: &users.Resolvers{}}` directly which is also fine as long as you include the code for the `users` field in the resolvers struct and set it to the users collection.

At this point, we are ready to start our GraphQL server and test things out.

Run `go build` and then execute the generated binary file. The server should be running by now. Make sure you do have the MongoDB replica set running before trying to run our server, otherwise, it will throw an error. You can start [here](https://docs.mongodb.com/manual/tutorial/deploy-replica-set-for-testing/) if you need help with running a replica set.

#### Create User

![Image](https://cdn-media-1.freecodecamp.org/images/1*L6xZoH6YqWpn7lhaI-qrsQ.png)

#### Update User

![Image](https://cdn-media-1.freecodecamp.org/images/1*9PYTvkFpdyKRQ9Z0RWLaLw.png)

#### Query User

![Image](https://cdn-media-1.freecodecamp.org/images/1*eUVMzZNj3Yp2hg6JsHf7Pg.png)

#### NotificationAdded Subscription

And there you have it!

I once again, I want to stress that this might not be the optimal solution to the problem at hand, but it’s my take on a possible solution and I would love to have your feedback and suggestions on this.

Thanks for reading. A few ? are always appreciated ?

