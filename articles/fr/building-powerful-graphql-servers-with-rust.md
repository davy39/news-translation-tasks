---
title: Comment construire des serveurs GraphQL puissants avec Rust
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-09-16T16:00:00.000Z'
originalURL: https://freecodecamp.org/news/building-powerful-graphql-servers-with-rust
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9ca05e740569d1a4ca483f.jpg
tags:
- name: GraphQL
  slug: graphql
- name: postgres
  slug: postgres
- name: Rust
  slug: rust
- name: RustLang
  slug: rustlang
- name: Web Development
  slug: web-development
seo_title: Comment construire des serveurs GraphQL puissants avec Rust
seo_desc: 'By Ian Wilson

  Setting up a GraphQL server with Rust, Juniper, Diesel, and Actix; learning about
  Rust''s web frameworks and powerful macros along the way.

  Source Code: github.com/iwilsonq/rust-graphql-example

  Serving applications via GraphQL is quickly...'
---

Par Ian Wilson

Configuration d'un serveur GraphQL avec Rust, Juniper, Diesel et Actix ; apprentissage des frameworks web de Rust et des macros puissantes en cours de route.

Code source : [github.com/iwilsonq/rust-graphql-example](https://github.com/iwilsonq/rust-graphql-example)

Servir des applications via GraphQL devient rapidement le moyen le plus facile et le plus efficace de fournir des données aux clients. Que vous soyez sur un appareil mobile ou un navigateur, il fournit les données demandées et rien de plus.

Les applications clientes n'ont plus besoin d'assembler des informations provenant de sources de données séparées. Les serveurs GraphQL sont responsables de l'intégration, éliminant ainsi le besoin de données excédentaires et de requêtes aller-retour pour les données.

Bien sûr, cela implique que le serveur doit gérer l'agrégation de données provenant de différentes sources, telles que des services backend internes, des bases de données ou des API tierces. Cela peut être intensif en ressources, comment pouvons-nous optimiser le temps CPU ?

Rust est un langage remarquable, combinant la performance brute d'un langage de bas niveau comme C avec l'expressivité des langages modernes. Il met l'accent sur la sécurité des types et de la mémoire, surtout lorsqu'il y a potentiellement des conditions de course dans les opérations concurrentes.

Voyons ce qui entre dans la construction d'un serveur GraphQL avec Rust. Nous allons apprendre sur

* Juniper GraphQL Server
* Actix web framework intégré avec Juniper
* Diesel pour interroger une base de données SQL
* Macros Rust utiles et traits dérivés pour travailler avec ces bibliothèques

Notez que je ne vais pas entrer dans les détails concernant l'installation de Rust ou Cargo. Cet article suppose une connaissance préliminaire de la chaîne d'outils Rust.

## Configuration d'un serveur HTTP

Pour commencer, nous devons initialiser notre projet avec `cargo` puis installer les dépendances.

```sh
    cargo new rust-graphql-example
    cd rust-graphql-example
```

La commande d'initialisation démarre notre fichier Cargo.toml qui contient les dépendances de notre projet ainsi qu'un fichier [main.rs](http://main.rs) qui a un simple exemple "Hello World".

```rust
    // main.rs
    
    fn main() {
      println!("Hello, world!");
    }
```

Pour une vérification de bon sens, n'hésitez pas à exécuter `cargo run` afin d'exécuter le programme.

L'installation des bibliothèques nécessaires dans Rust signifie ajouter une ligne contenant le nom de la bibliothèque et le numéro de version. Mettons à jour la section des dépendances de Cargo.toml comme suit :

```rust
    # Cargo.toml
    
    [dependencies]
    actix-web = "1.0.0"
    diesel = { version = "1.0.0", features = ["postgres"] }
    dotenv = "0.9.0"
    env_logger = "0.6"
    futures = "0.1"
    juniper = "0.13.1"
    serde = "1.0"
    serde_derive = "1.0"
    serde_json = "1.0"
```

Cet article couvrira la mise en œuvre d'un serveur GraphQL en utilisant [Juniper](https://github.com/graphql-rust/juniper) comme bibliothèque GraphQL et [Actix](https://actix.rs/) comme serveur HTTP sous-jacent. Actix a une API très agréable et fonctionne bien avec la version stable de Rust.

Lorsque ces lignes sont ajoutées, la prochaine fois que le projet compile, il inclura ces bibliothèques. Avant de compiler, mettons à jour main.rs avec un serveur HTTP de base, gérant la route d'index.

```rust
    // main.rs
    use std::io;
    
    use actix_web::{web, App, HttpResponse, HttpServer, Responder};
    
    fn main() -> io::Result<()> {
        HttpServer::new(|| {
            App::new()
                .route("/", web::get().to(index))
        })
        .bind("localhost:8080")?
        .run()
    }
    
    fn index() -> impl Responder {
        HttpResponse::Ok().body("Hello world!")
    }
```

Les deux premières lignes en haut importent le module dont nous avons besoin. La fonction principale ici retourne un type `io::Result`, ce qui nous permet d'utiliser le point d'interrogation comme raccourci pour gérer les résultats.

La configuration du routage et du serveur est créée dans l'instance de `App`, qui est créée dans une fermeture fournie par le constructeur du serveur HTTP.

La route elle-même est gérée par la fonction index, dont le nom est arbitraire. Tant que cette fonction implémente correctement `Responder`, elle peut être utilisée comme paramètre pour la requête GET à la route d'index.

Si nous écrivions une API REST, nous pourrions procéder en ajoutant plus de routes et de gestionnaires associés. Nous verrons bientôt que nous échangeons une liste de gestionnaires de routes contre des objets et leurs relations.

Maintenant, nous allons introduire la bibliothèque GraphQL.

## Création du schéma GraphQL

À la racine de chaque schéma GraphQL se trouve une requête racine. À partir de cette racine, nous pouvons interroger des listes d'objets, des objets spécifiques et tous les champs qu'ils peuvent contenir.

Appelons cela QueryRoot, et nous le désignerons par le même nom dans notre code. Puisque nous n'allons pas configurer de base de données ou d'API tierces, nous allons coder en dur les quelques données que nous avons ici.

Pour ajouter un peu de couleur à cet exemple, le schéma décrira une liste générique de membres.

Sous src, ajoutez un nouveau fichier appelé graphql_schema.rs avec le contenu suivant :

```rust
    // graphql_schema.rs
    use juniper::{EmptyMutation, RootNode};
    
    struct Member {
      id: i32,
      name: String,
    }
    
    #[juniper::object(description = "Un membre d'une équipe")]
    impl Member {
      pub fn id(&self) -> i32 {
        self.id  
      }
    
      pub fn name(&self) -> &str {
        self.name.as_str()
      }
    }
    
    pub struct QueryRoot;
    
    #[juniper::object]
    impl QueryRoot {
      fn members() -> Vec<Member> {
        vec![
          Member {
            id: 1,
            name: "Link".to_owned(),
          },
          Member {
            id: 2,
            name: "Mario".to_owned(),
          }
        ]
      }
    }
```

Avec nos imports, nous définissons notre premier objet GraphQL dans ce projet, le membre. Ils sont des êtres simples, avec un id et un nom. Nous penserons à des champs et des motifs plus compliqués plus tard.

Après avoir ébauché le type `QueryRoot` en tant que struct unitaire, nous pouvons définir le champ lui-même. Juniper expose une macro Rust appelée `object` qui nous permet de définir des champs sur les différents nœuds de notre schéma. Pour l'instant, nous n'avons que le nœud QueryRoot, nous allons donc exposer un champ appelé members sur celui-ci.

Les macros Rust ont souvent une syntaxe inhabituelle par rapport aux fonctions standard. Elles ne se contentent pas de prendre des arguments et de produire un résultat, elles se développent en un code beaucoup plus complexe au moment de la compilation.

## Exposition du schéma

Sous notre appel de macro pour créer le champ members, nous allons définir le type `RootNode` que nous exposons sur notre schéma.

```rust
    // graphql_schema.rs
    
    pub type Schema = RootNode<'static, QueryRoot, EmptyMutation<()>>;
    
    pub fn create_schema() -> Schema {
      Schema::new(QueryRoot {}, EmptyMutation::new())
    }
```

En raison du typage fort dans Rust, nous sommes obligés de fournir l'argument de l'objet de mutation. Juniper expose une struct `EmptyMutation` pour cette occasion, c'est-à-dire lorsque nous voulons créer un schéma en lecture seule.

Maintenant que le schéma est préparé, nous pouvons mettre à jour notre serveur dans main.rs pour gérer la route "/graphql". Puisque avoir un terrain de jeu est également agréable, nous ajouterons une route pour GraphiQL, le terrain de jeu interactif GraphQL.

```rust
    // main.rs
    #[macro_use]
    extern crate juniper;
    
    use std::io;
    use std::sync::Arc;
    
    use actix_web::{web, App, Error, HttpResponse, HttpServer};
    use futures::future::Future;
    use juniper::http::graphiql::graphiql_source;
    use juniper::http::GraphQLRequest;
    
    mod graphql_schema;
    
    use crate::schema::{create_schema, Schema};
    
    fn main() -> io::Result<()> {
        let schema = std::sync::Arc::new(create_schema());
        HttpServer::new(move || {
            App::new()
                .data(schema.clone())
                .service(web::resource("/graphql").route(web::post().to_async(graphql)))
                .service(web::resource("/graphiql").route(web::get().to(graphiql)))
        })
        .bind("localhost:8080")?
        .run()
    }
```

Vous remarquerez que j'ai spécifié un certain nombre d'imports que nous allons utiliser, y compris le schéma que nous venons de créer. Notez également que :

* nous appelons `create_schema` à l'intérieur d'un Arc (comptage de références atomique), pour permettre un état immutable partagé entre les threads (cuisine avec ? ici je sais)
* nous marquons la fermeture à l'intérieur de HttpServer::new avec **move**, indiquant que la fermeture prend possession des variables internes, c'est-à-dire qu'elle obtient une copie de `schema`
* `schema` est passé à la méthode `data` indiquant qu'il doit être utilisé à l'intérieur de l'application comme état partagé entre les deux services

Nous devons maintenant implémenter les gestionnaires pour ces deux services. Commençons par la route "/graphql" :

```rust
    // main.rs
    
    // fn main() ...
    
    fn graphql(
        st: web::Data<Arc<Schema>>,
        data: web::Json<GraphQLRequest>,
    ) -> impl Future<Item = HttpResponse, Error = Error> {
        web::block(move || {
            let res = data.execute(&st, &());
            Ok::<_, serde_json::error::Error>(serde_json::to_string(&res)?)
        })
        .map_err(Error::from)
        .and_then(|user| {
            Ok(HttpResponse::Ok()
                .content_type("application/json")
                .body(user))
        })
    }
```

Notre implémentation de la route "/graphql" exécute une requête GraphQL contre notre schéma à partir de l'état de l'application. Elle le fait en créant un **futur** à partir de `web::block` et en enchaînant des gestionnaires pour les états de succès et d'erreur.

Les futurs sont analogues aux Promesses en JavaScript, ce qui est suffisant pour comprendre cet extrait de code. Pour une plus grande explication des Futures en Rust, je recommande [cet article de Joe Jackson](https://www.viget.com/articles/understanding-futures-in-rust-part-1/).

Afin de tester notre schéma GraphQL, nous allons également ajouter un gestionnaire pour "/graphiql".

```rust
    // main.rs
    
    // fn graphql() ...
    
    fn graphiql() -> HttpResponse {
        let html = graphiql_source("http://localhost:8080/graphql");
        HttpResponse::Ok()
            .content_type("text/html; charset=utf-8")
            .body(html)
    }
```

Ce gestionnaire est beaucoup plus simple, il retourne simplement le html du terrain de jeu interactif GraphiQL. Nous devons seulement spécifier quel chemin sert notre schéma GraphQL, qui est "/graphql" dans ce cas.

Avec `cargo run` et la navigation vers [http://localhost:8080/graphiql](http://localhost:8080/graphiql), nous pouvons essayer le champ que nous avons configuré.

![Requête Members dans graphiql](https://thepracticaldev.s3.amazonaws.com/i/t22qyi7xarthf9xm2yvl.png)

Il semble que cela demande un peu plus d'efforts que la configuration d'un serveur GraphQL avec [Node.js et Apollo](https://www.freecodecamp.org/news/learn-to-build-a-graphql-server-with-minimal-effort-fc7fcabe8ebd/), mais le typage statique de Rust combiné à ses performances incroyables en fait un échange valable — si vous êtes prêt à travailler dessus.

## Configuration de Postgres pour des données réelles

Si je m'arrêtais ici, je ne rendrais même pas justice [aux exemples dans la documentation](https://graphql-rust.github.io/juniper/master/index.html). Une liste statique de deux membres _que j'ai écrits moi-même_ au moment du développement ne passera pas dans cette publication.

L'installation de Postgres et la configuration de votre propre base de données appartiennent à un autre article, mais je vais vous guider à travers l'installation de [diesel](http://diesel.rs), la bibliothèque Rust populaire pour la gestion des bases de données SQL.

[Voir ici pour installer Postgres localement sur votre machine](https://www.postgresql.org/download/). Vous pouvez également utiliser une autre base de données comme MySQL si vous êtes plus familier avec celle-ci.

L'interface de ligne de commande de diesel nous guidera à travers l'initialisation de nos tables. Installons-la :

```sh
    cargo install diesel_cli --no-default-features --features postgres
```

Après cela, nous allons ajouter une URL de connexion à un fichier .env dans notre répertoire de travail :

```sh
    echo DATABASE_URL=postgres://localhost/rust_graphql_example > .env
```

Une fois que c'est fait, vous pouvez exécuter :

```sh
    diesel setup
    
    # suivi de
    
    diesel migration generate create_members
```

Maintenant, vous aurez un dossier de migrations dans votre répertoire. À l'intérieur, vous aurez deux fichiers SQL : un up.sql pour configurer votre base de données, l'autre down.sql pour la supprimer.

Je vais ajouter ce qui suit à up.sql :

```sql
    CREATE TABLE teams (
      id SERIAL PRIMARY KEY,
      name VARCHAR NOT NULL
    );
    
    CREATE TABLE members (
      id SERIAL PRIMARY KEY,
      name VARCHAR NOT NULL,
      knockouts INT NOT NULL DEFAULT 0,
      team_id INT NOT NULL,
      FOREIGN KEY (team_id) REFERENCES teams(id)
    );
    
    INSERT INTO teams(id, name) VALUES (1, 'Heroes');
    INSERT INTO members(name, knockouts, team_id) VALUES ('Link', 14, 1);
    INSERT INTO members(name, knockouts, team_id) VALUES ('Mario', 11, 1);
    INSERT INTO members(name, knockouts, team_id) VALUES ('Kirby', 8, 1);
    
    INSERT INTO teams(id, name) VALUES (2, 'Villains');
    INSERT INTO members(name, knockouts, team_id) VALUES ('Ganondorf', 8, 2);
    INSERT INTO members(name, knockouts, team_id) VALUES ('Bowser', 11, 2);
    INSERT INTO members(name, knockouts, team_id) VALUES ('Mewtwo', 12, 2);
```

Et dans down.sql, je vais ajouter :

```sql
    DROP TABLE members;
    DROP TABLE teams;
```

Si vous avez écrit du SQL dans le passé, ces instructions auront du sens. Nous créons deux tables, une pour stocker les équipes et une pour stocker les membres de ces équipes.

Je modélise ces données en fonction de Smash Bros si vous ne l'avez pas encore remarqué. Cela aide à faire adhérer l'apprentissage.

Maintenant, pour exécuter les migrations :

```sh
    diesel migration run
```

Si vous souhaitez vérifier que le script down.sql fonctionne pour détruire ces tables, exécutez : `diesel migration redo`.

Maintenant, la raison pour laquelle j'ai nommé le fichier de schéma GraphQL graphql_schema.rs au lieu de schema.rs, c'est parce que diesel écrase ce fichier dans notre direction src par défaut.

Il conserve une représentation de macro Rust de nos tables SQL dans ce fichier. Il n'est pas si important de savoir comment fonctionne exactement cette macro `table!`, mais essayez de ne pas éditer ce fichier — l'ordre des champs compte !

```rust
    // schema.rs (Généré par diesel cli)
    
    table! {
        members (id) {
            id -> Int4,
            name -> Varchar,
            knockouts -> Int4,
            team_id -> Int4,
        }
    }
    
    table! {
        teams (id) {
            id -> Int4,
            name -> Varchar,
        }
    }
    
    joinable!(members -> teams (team_id));
    
    allow_tables_to_appear_in_same_query!(
        members,
        teams,
    );
```

## Connexion de nos gestionnaires avec Diesel

Afin de servir les données dans nos tables, nous devons d'abord mettre à jour notre struct `Member` avec les nouveaux champs :

```diff
    // graphql_schema.rs
    
    + #[derive(Queryable)]
    pub struct Member {
      pub id: i32,
      pub name: String,
    + pub knockouts: i32,
    + pub team_id: i32,
    }
    
    #[juniper::object(description = "Un membre d'une équipe")]
    impl Member {
      pub fn id(&self) -> i32 {
        self.id  
      }
    
      pub fn name(&self) -> &str {
        self.name.as_str()
      }
    
    + pub fn knockouts(&self) -> i32 {
    +   self.knockouts
    + }
    
    + pub fn team_id(&self) -> i32 {
    +   self.team_id
    + }
    }
```

Notez que nous ajoutons également l'attribut dérivé `Queryable` à `Member`. Cela indique à Diesel tout ce qu'il doit savoir pour interroger la bonne table dans Postgres.

De plus, ajoutez une struct `Team` :

```rust
    // graphql_schema.rs
    
    #[derive(Queryable)]
    pub struct Team {
      pub id: i32,
      pub name: String,
    }
    
    #[juniper::object(description = "Une équipe de membres")]
    impl Team {
      pub fn id(&self) -> i32 {
        self.id
      }
    
      pub fn name(&self) -> &str {
        self.name.as_str()
      }
    
      pub fn members(&self) -> Vec<Member> {
        vec![]
      }
    }
```

Dans un instant, nous mettrons à jour la fonction `members` sur `Team` pour retourner une requête de base de données. Mais d'abord, ajoutons un appel racine pour les membres.

```diff
    // graphql_schema.rs
    + extern crate dotenv;
    
    + use std::env;
    
    + use diesel::pg::PgConnection;
    + use diesel::prelude::*;
    + use dotenv::dotenv;
    use juniper::{EmptyMutation, RootNode};
    
    + use crate::schema::members;
    
    pub struct QueryRoot;
    
    +  fn establish_connection() -> PgConnection {
    +    dotenv().ok();
    +    let database_url = env::var("DATABASE_URL").expect("DATABASE_URL doit être défini");
    +    PgConnection::establish(&database_url).expect(&format!("Erreur de connexion à {}", database_url))
    +  }
    
    #[juniper::object]
    impl QueryRoot {
      fn members() -> Vec<Member> {
    -   vec![
    -     Member {
    -       id: 1,
    -       name: "Link".to_owned(),
    -     },
    -     Member {
    -       id: 2,
    -       name: "Mario".to_owned(),
    -     }
    -   ]
    +   use crate::schema::members::dsl::*;
    +   let connection = establish_connection();
    +   members
    +     .limit(100)
    +     .load::<Member>(&connection)
    +     .expect("Erreur de chargement des membres")
      }
    }
```

Très bien, nous avons notre première utilisation d'une requête diesel. Après avoir initialisé une connexion, nous utilisons le dsl des membres, qui est généré à partir de nos macros `table!` dans schema.rs, et appelons **load**, indiquant que nous souhaitons charger des objets `Member`.

Établir une connexion signifie se connecter à notre base de données Postgres locale en utilisant la variable d'environnement que nous avons déclarée précédemment.

En supposant que tout a été saisi correctement, redémarrez le serveur avec `cargo run`, ouvrez GraphiQL et émettez la requête des membres, peut-être en ajoutant les deux nouveaux champs.

La requête des équipes sera très similaire — la différence étant que nous devons également ajouter une partie de la requête à la fonction des membres sur la struct `Team` afin de résoudre la relation entre les types GraphQL.

```rust
    // graphql_schema.rs
    
    #[juniper::object]
    impl QueryRoot {
      fn members() -> Vec<Member> {
        use crate::schema::members::dsl::*;
        let connection = establish_connection();
        members
          .limit(100)
          .load::<Member>(&connection)
          .expect("Erreur de chargement des membres")
      }
    
    +  fn teams() -> Vec<Team> {
    +    use crate::schema::teams::dsl::*;
    +    let connection = establish_connection();
    +    teams
    +      .limit(10)
    +      .load::<Team>(&connection)
    +      .expect("Erreur de chargement des équipes")
    +  }
    }
    
    // ...
    
    #[juniper::object(description = "Une équipe de membres")]
    impl Team {
      pub fn id(&self) -> i32 {
        self.id
      }
    
      pub fn name(&self) -> &str {
        self.name.as_str()
      }
    
      pub fn members(&self) -> Vec<Member> {
    -    vec![]
    +    use crate::schema::members::dsl::*;
    +    let connection = establish_connection();
    +    members
    +      .filter(team_id.eq(self.id))
    +      .limit(100)
    +      .load::<Member>(&connection)
    +      .expect("Erreur de chargement des membres")
      }
    }
```

Lorsque nous exécutons cela dans GraphiQL, nous obtenons :

![Requête plus complexe dans graphiql](https://thepracticaldev.s3.amazonaws.com/i/1gsj02nf5m8le9ujjbr8.png)

J'aime vraiment la façon dont cela se passe, mais il y a une dernière chose que nous devons ajouter pour considérer ce tutoriel complet.

## La mutation Create Member

À quoi bon un serveur s'il est en lecture seule et non modifiable ? Eh bien, je suis sûr que ceux-ci ont aussi leurs utilités, mais nous aimerions écrire des données dans notre base de données, à quel point cela peut-il être difficile ?

Tout d'abord, nous allons créer une struct `MutationRoot` qui remplacera éventuellement notre utilisation de `EmptyMutation`. Ensuite, nous ajouterons la requête d'insertion diesel.

```rust
    // graphql_schema.rs
    
    // ...
    
    pub struct MutationRoot;
    
    #[juniper::object]
    impl MutationRoot {
      fn create_member(data: NewMember) -> Member {
        let connection = establish_connection();
        diesel::insert_into(members::table)
          .values(&data)
          .get_result(&connection)
          .expect("Erreur lors de l'enregistrement du nouveau membre")
      }
    }
    
    #[derive(juniper::GraphQLInputObject, Insertable)]
    #[table_name = "members"]
    pub struct NewMember {
      pub name: String,
      pub knockouts: i32,
      pub team_id: i32,
    }
```

Comme le font généralement les mutations GraphQL, nous définissons un objet d'entrée appelé `NewMember` et en faisons l'argument de la fonction `create_member`. À l'intérieur de cette fonction, nous établissons une connexion et appelons la requête d'insertion sur la table des membres, en passant l'objet d'entrée entier.

C'est super pratique que Rust nous permette d'utiliser les mêmes structs pour les objets d'entrée GraphQL ainsi que pour les objets insérables Diesel.

Permettez-moi de rendre cela un peu plus clair, pour la struct `NewMember` :

* nous dérivons `juniper::GraphQLInputObject` afin de créer un objet d'entrée pour notre schéma GraphQL
* nous dérivons `Insertable` afin de laisser Diesel savoir que cette struct est une entrée valide pour une instruction SQL d'insertion
* nous ajoutons l'attribut `table_name` afin que Diesel sache dans quelle table l'insérer

Il y a beaucoup de _magie_ qui se passe ici. C'est ce que j'aime dans Rust, il a de grandes performances mais le code a des fonctionnalités comme les macros et les traits dérivés pour abstraire le code passe-partout et ajouter des fonctionnalités.

Enfin, en bas du fichier, ajoutez le `MutationRoot` au schéma :

```rust
    // graphql_schema.rs
    
    pub type Schema = RootNode<'static, QueryRoot, MutationRoot>;
    
    pub fn create_schema() -> Schema {
      Schema::new(QueryRoot {}, MutationRoot {})
    }
```

J'espère que tout est là, nous pouvons maintenant tester toutes nos requêtes et mutations jusqu'à présent :

```graphql
    # GraphiQL
    
    mutation CreateMemberMutation($data: NewMember!) {
      createMember(data: $data) {
        id
        name
        knockouts
        teamId
      }
    }
    
    # exemple de variables de requête
    # {
    #   "data": {
    #     "name": "Samus",
    #     "knockouts": 19,
    #     "teamId": 1
    #   }
    # }
```

Si cette mutation s'est exécutée avec succès, vous pouvez ouvrir une bouteille de champagne car vous êtes en route pour construire des serveurs GraphQL performants et sûrs avec Rust.

## Merci d'avoir lu

J'espère que vous avez apprécié cet article, j'espère aussi qu'il vous a donné une sorte d'inspiration pour votre propre travail.

Si vous souhaitez rester informé la prochaine fois que je publie un article dans le domaine de Rust, ReasonML, GraphQL, ou le développement logiciel en général, n'hésitez pas à me suivre sur [Twitter](https://twitter.com/iwilson), [dev.to](https://dev.to/iwilsonq), ou sur mon site web à [ianwilson.io](https://ianwilson.io).

Le code source est ici [github.com/iwilsonq/rust-graphql-example](https://github.com/iwilsonq/rust-graphql-example).

### Autres lectures intéressantes

Voici quelques-unes des bibliothèques avec lesquelles nous avons travaillé ici. Elles ont également une excellente documentation et des guides, alors assurez-vous de les lire :)

* [Implémentation des Futures Rust dans Tokio](https://tokio.rs/docs/getting-started/futures/)
* [Juniper - Serveur GraphQL pour Rust](https://graphql-rust.github.io/juniper/master/index.html)
* [Diesel - ORM et constructeur de requêtes sûr et extensible pour Rust](http://diesel.rs/)
* [Actix - Système d'acteurs puissant de Rust et framework web le plus amusant](https://actix.rs/)