---
title: Comment commencer avec MongoDB en Rust
subtitle: ''
author: Oduah Chigozie
co_authors: []
series: null
date: '2023-02-20T20:41:19.000Z'
originalURL: https://freecodecamp.org/news/mongodb-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2023/02/pexels-ulucas-dube-cantin-10325707.jpg
tags:
- name: database
  slug: database
- name: MongoDB
  slug: mongodb
- name: Rust
  slug: rust
seo_title: Comment commencer avec MongoDB en Rust
seo_desc: "MongoDB is a popular NoSQL database that has been gaining increasing popularity\
  \ in recent years. It offers developers a flexible, scalable, and high-performance\
  \ database solution, which can be used for a wide range of applications. \nFor Rust\
  \ programm..."
---

MongoDB est une base de données NoSQL populaire qui a gagné en popularité ces dernières années. Elle offre aux développeurs une solution de base de données flexible, évolutive et haute performance, qui peut être utilisée pour une large gamme d'applications. 

Pour les programmeurs Rust, MongoDB fournit une excellente option pour stocker et récupérer des données de manière rapide, efficace et fiable.

Rust est un langage de programmation système moderne et haute performance, conçu pour la vitesse, la sécurité et la concurrence. Il est bien adapté pour construire des logiciels haute performance et de bas niveau, et devient de plus en plus populaire parmi les développeurs.

Dans cet article, nous allons explorer comment les programmeurs Rust peuvent tirer parti de MongoDB pour construire des applications haute performance et évolutives. Je vais expliquer comment configurer une base de données MongoDB, et vous montrer comment interagir avec MongoDB depuis Rust en utilisant le pilote officiel MongoDB pour Rust. 

Que vous soyez nouveau dans MongoDB ou un programmeur Rust expérimenté cherchant à exploiter cette puissante technologie de base de données, cet article vous fournira les connaissances et les compétences nécessaires pour commencer.

## Prérequis

Pour suivre cet article, vous n'avez besoin que des éléments suivants :

* Connaissance de Rust.
* Un système sur lequel travailler.
* Rust installé sur votre système.

## Prise en main

Pour commencer avec MongoDB, vous devrez installer le logiciel de base de données MongoDB Community Edition. Les étapes suivantes vous guideront à travers le processus d'installation.

### Télécharger MongoDB Community Edition.

La première étape consiste à télécharger le package MongoDB Community Edition pour votre système d'exploitation. 

Vous pouvez télécharger le package depuis le site officiel de MongoDB à l'adresse [https://www.mongodb.com/try/download/community](https://www.mongodb.com/try/download/community).

### Installer MongoDB Community Edition.

Après avoir téléchargé le package, exécutez l'installateur et suivez les invites pour installer MongoDB Community Edition sur votre système.

### Démarrer le serveur MongoDB.

Une fois l'installation terminée, démarrez le serveur MongoDB en exécutant la commande suivante :

```bash
mongod

```

Cela démarrera le serveur MongoDB et il écoutera sur le port 27017 par défaut.

### Installer MongoDB Compass

MongoDB Compass est une interface graphique (GUI) pour travailler avec MongoDB. Elle fournit un moyen simple et intuitif d'interagir avec les bases de données, les collections et les documents MongoDB. 

Pour installer MongoDB Compass, suivez ces étapes :

1. Allez sur le site officiel de MongoDB à l'adresse [https://www.mongodb.com/products/compass](https://www.mongodb.com/products/compass) et téléchargez la version appropriée pour votre système d'exploitation.
2. Exécutez l'installateur et suivez les invites pour installer MongoDB Compass sur votre système.
3. Une fois l'installation terminée, lancez MongoDB Compass et connectez-vous à votre serveur MongoDB en entrant la chaîne de connexion dans la boîte de dialogue de connexion.

Félicitations, vous avez maintenant installé MongoDB Community Edition et MongoDB Compass. Vous pouvez maintenant commencer à travailler avec les bases de données, les collections et les documents MongoDB. 

Dans la section suivante, nous allons couvrir comment configurer un projet afin que vous puissiez interagir avec la base de données depuis Rust.

## Comment configurer votre projet

Maintenant que vous avez installé MongoDB sur votre système, il est temps de configurer votre projet Rust pour utiliser le pilote officiel MongoDB pour Rust. Suivez ces étapes pour commencer :

### Créer un nouveau projet Rust.

Ouvrez votre terminal et créez un nouveau projet Rust en exécutant la commande suivante :

```bash
cargo new myproject

```

Cela créera un nouveau projet Rust avec le nom "myproject".

### Ajouter la dépendance du pilote Rust pour MongoDB.

Ouvrez le fichier _Cargo.toml_ dans votre répertoire de projet et ajoutez la dépendance suivante :

```toml
[dependencies]
mongodb = "2.3.1"

```

Cela ajoutera la dépendance du pilote Rust pour MongoDB à votre projet.

### Importer les bibliothèques nécessaires.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et importez les bibliothèques nécessaires en ajoutant les lignes suivantes en haut du fichier :

```rust
extern crate mongodb;
use mongodb::bson::doc;
use mongodb::{Client, options::ClientOptions};

```

Cela importera la macro `doc`, et les types `Client` et `ClientOptions` depuis le pilote Rust pour MongoDB.

### Se connecter à votre serveur MongoDB.

Ajoutez le code suivant à votre fonction `main` pour vous connecter à votre serveur MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

```

Cela créera un nouvel objet `ClientOptions` avec la chaîne de connexion à votre serveur MongoDB. Ensuite, créez un nouvel objet `Client` avec l'objet `ClientOptions`.

Félicitations, vous avez maintenant configuré votre projet Rust pour utiliser le pilote officiel MongoDB pour Rust. 

Dans les sections suivantes, nous allons couvrir comment créer une base de données en utilisant MongoDB Compass.

## Comment créer une base de données dans MongoDB

Avant de pouvoir créer une collection dans MongoDB, vous devez avoir une base de données pour la stocker. Dans cette section, je vais vous montrer comment créer une nouvelle base de données dans MongoDB en utilisant MongoDB Compass.

1. Ouvrez MongoDB Compass et cliquez sur le bouton **Se connecter** dans le coin supérieur gauche de l'écran.
2. Dans la fenêtre **Nouvelle connexion**, entrez les détails de connexion pour votre instance MongoDB. Cela inclut le nom d'hôte, le numéro de port et les détails d'authentification si nécessaire.
3. Cliquez sur **Se connecter** pour établir une connexion à votre instance MongoDB.
4. Dans le volet de navigation de gauche, cliquez sur **Bases de données** pour afficher une liste des bases de données existantes.
5. Cliquez sur le bouton **Créer une base de données** dans le coin supérieur gauche de la fenêtre **Bases de données**.
6. Entrez un nom pour votre nouvelle base de données (par exemple "mydatabase") et cliquez sur **Créer**.

Félicitations, vous avez créé une nouvelle base de données dans MongoDB Compass ! Vous pouvez maintenant commencer à créer des collections et à ajouter des documents à votre base de données.

## Comment créer une collection dans MongoDB

Dans MongoDB, une collection de base de données est équivalente à une table dans une base de données relationnelle. Une collection est un groupe de documents MongoDB qui partagent un ensemble de caractéristiques communes. 

Dans cette section, je vais vous montrer comment créer une nouvelle collection dans MongoDB en utilisant Rust.

### Créer une nouvelle fonction Rust.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et créez une nouvelle fonction appelée `create_collection`. Cette fonction créera une nouvelle collection dans votre base de données MongoDB. Ajoutez le code suivant à votre fichier _main.rs_ :

```rust
async fn create_collection(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    db.create_collection(coll_name, None).await.unwrap();
}

```

Cette fonction prend un objet `Client`, un nom de base de données et un nom de collection comme arguments. Elle crée ensuite une nouvelle collection dans la base de données spécifiée.

### Appeler la fonction `create_collection`.

Dans votre fonction principale, ajoutez le code suivant pour appeler la fonction `create_collection` et créer une nouvelle collection dans votre base de données MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

create_collection(&client, db_name, coll_name).await;

```

Ce code créera un nouvel objet `Client` et appellera la fonction `create_collection` pour créer une nouvelle collection appelée "mycollection" dans la base de données `mydatabase`.

Félicitations, vous avez maintenant créé une nouvelle collection dans votre base de données MongoDB en utilisant Rust. 

Dans les quatre sections suivantes, nous allons couvrir comment effectuer des opérations CRUD sur vos données, en commençant par l'insertion d'un document.

## Comment insérer un document dans une collection dans MongoDB

Dans MongoDB, une ligne est équivalente à un document dans une collection. Dans cette section, je vais vous montrer comment insérer un nouveau document dans une collection dans MongoDB en utilisant Rust.

### Créer une nouvelle fonction Rust.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et créez une nouvelle fonction appelée `insert_document`. Cette fonction insérera un nouveau document dans la collection spécifiée dans votre base de données MongoDB. Ajoutez le code suivant à votre fichier _main.rs_ :

```rust
async fn insert_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let doc = doc! { "name": "John", "age": 30 };

    coll.insert_one(doc, None).await.unwrap();
}

```

Cette fonction prend un objet `Client`, un nom de base de données et un nom de collection comme arguments. Elle crée ensuite un nouvel objet `Collection` pour la collection spécifiée et insère un nouveau document dans celle-ci.

### Appeler la fonction `insert_document`.

Dans votre fonction principale, ajoutez le code suivant pour appeler la fonction `insert_document` et insérer un nouveau document dans votre collection MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

insert_document(&client, db_name, coll_name).await;

```

Ce code créera un nouvel objet `Client` et appellera sa méthode `insert_one` pour insérer un nouveau document avec les champs `name` et `age` dans la collection.

Félicitations, vous avez maintenant inséré un nouveau document dans votre collection MongoDB en utilisant Rust. 

Dans la section suivante, je vais couvrir comment récupérer un document de la collection et effectuer d'autres opérations CRUD sur vos données.

## Comment récupérer un document d'une collection dans MongoDB

Dans MongoDB, vous pouvez récupérer un document d'une collection en interrogeant la collection avec des critères de filtre spécifiques. 

Dans cette section, je vais vous montrer comment récupérer un document d'une collection dans MongoDB en utilisant Rust.

### Créer une nouvelle fonction Rust.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et créez une nouvelle fonction appelée `get_document`. Cette fonction récupérera un document de la collection spécifiée dans votre base de données MongoDB. Ajoutez le code suivant à votre fichier _main.rs_ :

```rust
fn get_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};

    let result = coll.find_one(Some(filter), None).await.unwrap();
    match result {
        Some(doc) => println!("{}", doc),
        None => println!("Aucun document trouvé"),
    }
}

```

Cette fonction prend un objet `Client`, un nom de base de données et un nom de collection comme arguments. Elle crée ensuite un nouvel objet `Collection` pour la collection spécifiée et récupère un document de celle-ci qui correspond aux critères de filtre spécifiés.

Dans cet exemple, nous récupérons un document dans la collection qui a un champ appelé "name" avec la valeur "John".

### Appeler la fonction `get_document`.

Dans votre fonction principale, ajoutez le code suivant pour appeler la fonction `get_document` et récupérer un document de votre collection MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

get_document(&client, db_name, coll_name).await;

```

Ce code créera un nouvel objet `Client`, et récupérera un document de la collection `mycollection` qui correspond aux critères de filtre.

Félicitations, vous avez maintenant récupéré un document de votre collection MongoDB en utilisant Rust. Dans la section suivante, nous allons couvrir comment supprimer des données de la collection.

## Comment supprimer un document d'une collection dans MongoDB

Dans MongoDB, vous pouvez supprimer un document d'une collection en spécifiant un ou plusieurs critères pour correspondre au document. 

Dans cette section, je vais vous montrer comment supprimer un document d'une collection dans MongoDB en utilisant Rust.

### Créer une nouvelle fonction Rust.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et créez une nouvelle fonction appelée `delete_document`. Cette fonction supprimera un document de la collection spécifiée dans votre base de données MongoDB. Ajoutez le code suivant à votre fichier _main.rs_ :

```rust
fn delete_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};
    coll.delete_one(filter, None).await.unwrap();
}

```

Cette fonction prend un objet `Client`, un nom de base de données et un nom de collection comme arguments. Elle crée ensuite un nouvel objet `Collection` pour la collection spécifiée et supprime un document de celle-ci qui correspond aux critères de filtre spécifiés.

Dans cet exemple, nous supprimons un document de la collection qui a un champ appelé "name" avec la valeur "John".

### Appeler la fonction `delete_document`.

Dans votre fonction principale, ajoutez le code suivant pour appeler la fonction `delete_document` et supprimer un document de votre collection MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

delete_document(&client, db_name, coll_name).await;

```

Ce code créera un nouvel objet `Client`, et supprimera un document de la collection `mycollection` qui correspond aux critères de filtre.

Félicitations, vous avez maintenant supprimé un document de votre collection MongoDB en utilisant Rust. 

Dans la section suivante, je vais couvrir comment modifier des documents dans votre collection.

## Comment modifier un document dans une collection dans MongoDB

Dans MongoDB, vous pouvez modifier un document dans une collection en mettant à jour un ou plusieurs champs dans le document. Dans cette section, je vais vous montrer comment modifier un document dans une collection dans MongoDB en utilisant Rust.

### Créer une nouvelle fonction Rust.

Ouvrez le fichier _src/main.rs_ dans votre répertoire de projet et créez une nouvelle fonction appelée `update_document`. Cette fonction mettra à jour un document dans la collection spécifiée dans votre base de données MongoDB. Ajoutez le code suivant à votre fichier main.rs :

```rust
fn update_document(client: &Client, db_name: &str, coll_name: &str) {
    let db = client.database(db_name);
    let coll = db.collection(coll_name);

    let filter = doc! {"name": "John"};
    let update = doc! {"$set": {"age": 35}};
    coll.update_one(filter, update, None).await.unwrap();
}

```

Cette fonction prend un objet `Client`, un nom de base de données et un nom de collection comme arguments. Elle crée ensuite un nouvel objet `Collection` pour la collection spécifiée et met à jour un document dans celle-ci qui correspond aux critères de filtre spécifiés.

Dans cet exemple, nous mettons à jour un document dans la collection qui a un champ appelé "name" avec la valeur "John". Nous définissons la valeur du champ "age" à "35".

### Appeler la fonction `update_document`.

Dans votre fonction principale, ajoutez le code suivant pour appeler la fonction `update_document` et mettre à jour un document dans votre collection MongoDB :

```rust
let client_options = ClientOptions::parse("mongodb://localhost:27017").await.unwrap();
let client = Client::with_options(client_options).unwrap();

let db_name = "mydatabase";
let coll_name = "mycollection";

update_document(&client, db_name, coll_name).await;

```

Ce code créera un nouvel objet `Client`, et mettra à jour un document dans la collection `mycollection` qui correspond aux critères de filtre.

Félicitations, vous avez maintenant mis à jour un document dans votre collection MongoDB en utilisant Rust. Maintenant, vous avez effectué toutes les opérations CRUD de base sur une base de données MongoDB.

## Conclusion

Dans cet article, je vous ai présenté MongoDB et comment l'utiliser avec Rust. J'ai couvert les bases de la configuration d'un serveur MongoDB, de la création d'une base de données et de la création d'une collection au sein de la base de données. J'ai également montré comment insérer, récupérer, modifier et supprimer des données de votre base de données MongoDB en utilisant Rust.

En tirant parti du langage de programmation Rust et de la base de données MongoDB, vous pouvez construire des applications robustes et évolutives capables de gérer de grandes quantités de données. Les fonctionnalités de performance et de sécurité de Rust en font un excellent choix pour travailler avec des bases de données comme MongoDB.

J'espère que cet article vous a fourni une base solide pour travailler avec MongoDB en Rust. Avec les connaissances acquises dans cet article, vous devriez être en mesure de construire une large gamme d'applications nécessitant une base de données backend.

Merci d'avoir lu, et bon codage !