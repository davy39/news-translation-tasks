---
title: Edge Cloud Microservices – Comment construire des applications haute performance
  et sécurisées avec WasmEdge et Rust
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2022-09-16T17:43:57.000Z'
originalURL: https://freecodecamp.org/news/edge-cloud-microservices-with-wasmedge-and-rust
coverImage: https://www.freecodecamp.org/news/content/images/2022/09/richard-r-schunemann-DD3VNthK_Kw-unsplash.jpg
tags:
- name: Microservices
  slug: microservices
- name: performance
  slug: performance
- name: Rust
  slug: rust
seo_title: Edge Cloud Microservices – Comment construire des applications haute performance
  et sécurisées avec WasmEdge et Rust
seo_desc: 'The edge cloud allows developers to deploy microservices (that is, fine-grained
  web services) close to their users. This gives them a better user experience (and
  very fast response times), security, and high availability.

  It also leverages local or e...'
---

Le edge cloud permet aux développeurs de déployer des microservices (c'est-à-dire des services web à grain fin) près de leurs utilisateurs. Cela leur offre une meilleure expérience utilisateur (et des temps de réponse très rapides), une sécurité et une haute disponibilité.

Il exploite également des centres de données locaux ou même privés, des réseaux CDN et des centres de données de télécommunications (par exemple, les MEC 5G) pour fournir des services de calcul.

Des exemples réussis de edge clouds incluent Cloudflare, Fastly, Akamai, fly.io, Vercel, Netlify et bien d'autres.

Mais le edge cloud est également un environnement aux ressources limitées par rapport aux grands clouds publics. Si les microservices de edge eux-mêmes sont lents, gonflés ou non sécurisés, ils annuleront tout l'intérêt de déployer sur le edge cloud.

Dans cet article, je vais vous montrer comment créer des services web légers et haute performance dans le [bac à sable WebAssembly](https://github.com/WasmEdge), puis les déployer gratuitement sur le fournisseur de edge cloud [fly.io](http://fly.io).

[Fly.io](http://Fly.io) est un fournisseur de services VM sur le edge cloud. Il dispose de centres de données de edge dans le monde entier. Les VM [fly.io](http://Fly.io) supportent les serveurs d'applications, les bases de données et, dans notre cas, des runtimes légers pour les microservices.

J'utiliserai le [WasmEdge Runtime](https://github.com/WasmEdge/WasmEdge) comme bac à sable de sécurité pour ces microservices. WasmEdge est un runtime WebAssembly spécifiquement optimisé pour les services cloud-native.

Nous allons packager l'application de microservice, écrite en Rust ou JavaScript, dans des [images Docker basées sur WasmEdge](https://hub.docker.com/u/wasmedge).

Il y a plusieurs avantages convaincants à cette approche :

* WasmEdge exécute des applications en bac à sable à une vitesse proche du natif. Selon une étude évaluée par des pairs, WasmEdge exécute des programmes Rust à presque la même vitesse que Linux exécute du code machine natif.

* WasmEdge est un runtime hautement sécurisé. Il protège votre application contre les menaces externes et internes.

* La surface d'attaque du runtime WasmEdge est considérablement réduite par rapport à un runtime Linux OS standard.

* Le risque d'attaque de la chaîne d'approvisionnement logicielle est grandement réduit puisque le bac à sable WebAssembly n'a accès qu'aux capacités explicitement déclarées.

* WasmEdge fournit un environnement d'exécution d'application complet et portable avec une empreinte mémoire qui n'est que de 1/10 de celle d'une image de runtime Linux OS standard.

* Le runtime WasmEdge est multiplateforme. Cela signifie que les machines de développement et de déploiement n'ont pas besoin d'être les mêmes. Et une fois que vous avez créé une application WasmEdge, vous pouvez la déployer partout où WasmEdge est supporté, y compris l'infrastructure [fly.io](http://fly.io).

Les avantages de performance sont amplifiés si l'application est complexe. Par exemple, une application d'inférence IA WasmEdge ne nécessiterait PAS d'installation Python. Une application WasmEdge node.js ne nécessiterait PAS d'installation Node.js et v8.

Dans le reste de cet article, je vais démontrer comment exécuter :

* un serveur HTTP asynchrone (en Rust)

* un service web de classification d'images très rapide (en Rust), et

* un serveur web node.JS

* des microservices avec état avec des connexions à une base de données

Tous fonctionnent rapidement et en toute sécurité dans WasmEdge tout en consommant 1/10 des ressources requises par les conteneurs Linux standard.

### Prérequis

Tout d'abord, si vous avez déjà installé les outils Docker sur votre système, c'est parfait. Sinon, veuillez suivre [la première section de ce manuel](https://www.freecodecamp.org/news/the-docker-handbook/) pour installer Docker maintenant. Ensuite, nous utiliserons des installateurs en ligne pour installer WasmEdge, Rust et l'outil `flyctl` pour [fly.io](http://fly.io).

Installez WasmEdge. [Voir les détails ici](https://wasmedge.org/book/en/start/install.html).

```bash
curl -sSf https://raw.githubusercontent.com/WasmEdge/WasmEdge/master/utils/install.sh | bash -s -- -e all
```

Installez Rust. [Voir les détails ici](https://www.rust-lang.org/tools/install).

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

Installez l'outil `flyctl` pour [fly.io](http://fly.io). [Voir les détails ici](https://fly.io/docs/hands-on/install-flyctl/).

```bash
curl -L https://fly.io/install.sh | sh
```

Une fois que vous avez installé `flyctl`, suivez les instructions pour [vous inscrire à un compte gratuit](https://fly.io/docs/hands-on/sign-up/) sur [fly.io](http://fly.io). Vous êtes maintenant prêt à déployer des services web sur le edge cloud !

## Un Microservice Simple en Rust

Notre premier exemple est un service HTTP simple écrit en Rust. Il démontre une application web moderne qui peut être étendue pour supporter une logique métier arbitrairement complexe.

Basé sur les crates populaires tokio et hyper, ce microservice est rapide, asynchrone (non bloquant) et très facile à créer pour les développeurs.

L'image WasmEdge entièrement liée statiquement ne fait que 4 Mo contre 40 Mo pour une image Linux de base. Cela est suffisant pour exécuter un service HTTP asynchrone écrit avec les frameworks tokio et hyper de Rust.

Exécutez les deux commandes CLI suivantes pour créer puis déployer une application [fly.io](http://fly.io) à partir de notre image Docker légère pour WasmEdge.

```bash
$ flyctl launch --image juntaoyuan/flyio-echo
$ flyctl deploy
```

C'est tout ! Vous pouvez utiliser la commande curl pour tester si le service web déployé fonctionne réellement. Il renvoie les données que vous lui envoyez.

```bash
$ curl https://proud-sunset-3795.fly.dev/echo -d "Hello WasmEdge on fly.io!"
Hello WasmEdge on fly.io!
```

Le Dockerfile pour l'image Docker `juntaoyuan/flyio-echo` contient le package complet du runtime WasmEdge et l'application web personnalisée `wasmedge_hyper_server.wasm`.

```dockerfile
FROM wasmedge/slim-runtime:0.11.0
ADD wasmedge_hyper_server.wasm /
CMD ["wasmedge", "--dir", ".:/", "/wasmedge_hyper_server.wasm"]
```

Le projet de code source Rust pour construire l'application `wasmedge_hyper_server.wasm` [est disponible sur GitHub](https://github.com/WasmEdge/wasmedge_hyper_demo/tree/main/server). Il utilise l'API tokio pour démarrer un serveur HTTP.

Lorsque le serveur reçoit une requête, il délègue à la fonction `echo()` pour traiter la requête de manière asynchrone. Cela permet au microservice d'accepter et de gérer plusieurs requêtes HTTP concurrentes.

```rust
#[tokio::main(flavor = "current_thread")]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let addr = SocketAddr::from(([0, 0, 0, 0], 8080));

    let listener = TcpListener::bind(addr).await?;
    println!("Listening on http://{}", addr);
    loop {
        let (stream, _) = listener.accept().await?;

        tokio::task::spawn(async move {
            if let Err(err) = Http::new().serve_connection(stream, service_fn(echo)).await {
                println!("Error serving connection: {:?}", err);
            }
        });
    }
}
```

La fonction asynchrone `echo()` est la suivante. Elle utilise l'API HTTP fournie par hyper pour analyser la requête et générer la réponse. Ici, la réponse est simplement le corps des données de la requête.

```rust
async fn echo(req: Request<Body>) -> Result<Response<Body>, hyper::Error> {
    match (req.method(), req.uri().path()) {
        ... ...
        (&Method::POST, "/echo") => Ok(Response::new(req.into_body())),
        ... ...

        // Retourne 404 Not Found pour les autres routes.
        _ => {
            let mut not_found = Response::default();
            *not_found.status_mut() = StatusCode::NOT_FOUND;
            Ok(not_found)
        }
    }
}
```

Maintenant, ajoutons au microservice de base pour faire quelque chose d'impressionnant !

## Un Microservice d'Inférence IA en Rust

Dans cet exemple, nous allons créer un service web pour la classification d'images. Il traite une image téléchargée à travers un modèle Tensorflow Lite.

Au lieu de créer un programme Python complexe (et gonflé), nous allons utiliser l'API Rust de WasmEdge pour accéder à Tensorflow, qui exécute la tâche d'inférence à la vitesse du code machine natif (par exemple, en utilisant le matériel GPU si disponible).

Grâce à la norme WASI-NN, l'API Rust de WasmEdge peut fonctionner avec des modèles IA dans Tensorflow, PyTorch, OpenVINO et d'autres frameworks IA.

Pour les applications d'inférence IA avec toutes les dépendances Tensorflow Lite incluses, l'empreinte de WasmEdge est inférieure à 115 Mo. Cela se compare à plus de 400 Mo pour l'image Linux Tensorflow standard.

Exécutez les deux commandes CLI suivantes pour créer puis déployer une application [fly.io](http://fly.io) à partir de notre image Docker légère pour WasmEdge + Tensorflow.

```bash
$ flyctl launch --image juntaoyuan/flyio-classify
$ flyctl deploy
```

C'est tout ! Vous pouvez utiliser la commande curl pour tester si le service web déployé fonctionne réellement. Il retourne le résultat de la classification de l'image avec un niveau de confiance.

```bash
$ curl https://silent-glade-6853.fly.dev/classify -X POST --data-binary "@grace_hopper.jpg"
military uniform is detected with 206/255 confidence
```

Le Dockerfile pour l'image Docker `juntaoyuan/flyio-classify` contient le package complet du runtime WasmEdge, l'ensemble des bibliothèques Tensorflow et leurs dépendances, et l'application web personnalisée `wasmedge_hyper_server_tflite.wasm`.

```dockerfile
FROM wasmedge/slim-tf:0.11.0
ADD wasmedge_hyper_server_tflite.wasm /
CMD ["wasmedge-tensorflow-lite", "--dir", ".:/", "/wasmedge_hyper_server_tflite.wasm"]
```

Le projet de code source Rust pour construire l'application `wasmedge_hyper_server_tflite.wasm` [est disponible sur GitHub](https://github.com/WasmEdge/wasmedge_hyper_demo/tree/main/server-tflite). Le serveur HTTP asynchrone basé sur tokio est dans la fonction asynchrone `main()` comme dans l'exemple précédent.

La fonction `classify()` traite les données d'image dans la requête, transforme l'image en un tenseur, exécute le modèle Tensorflow, puis transforme les valeurs de retour (dans un tenseur) en étiquettes de texte et en probabilités pour les classifications possibles.

```rust
async fn classify(req: Request<Body>) -> Result<Response<Body>, hyper::Error> {
    let model_data: &[u8] = include_bytes!("models/mobilenet_v1_1.0_224/mobilenet_v1_1.0_224_quant.tflite");
    let labels = include_str!("models/mobilenet_v1_1.0_224/labels_mobilenet_quant_v1_224.txt");
    match (req.method(), req.uri().path()) {

        (&Method::POST, "/classify") => {
            let buf = hyper::body::to_bytes(req.into_body()).await?;
            let flat_img = wasmedge_tensorflow_interface::load_jpg_image_to_rgb8(&buf, 224, 224);

            let mut session = wasmedge_tensorflow_interface::Session::new(&model_data, wasmedge_tensorflow_interface::ModelType::TensorFlowLite);
            session.add_input("input", &flat_img, &[1, 224, 224, 3])
                .run();
            let res_vec: Vec<u8> = session.get_output("MobilenetV1/Predictions/Reshape_1");
            ... ...

            let mut label_lines = labels.lines();
            for _i in 0..max_index {
              label_lines.next();
            }
            let class_name = label_lines.next().unwrap().to_string();

            Ok(Response::new(Body::from(format!("{} is detected with {}/255 confidence", class_name, max_value))))
        }

        // Retourne 404 Not Found pour les autres routes.
        _ => {
            let mut not_found = Response::default();
            *not_found.status_mut() = StatusCode::NOT_FOUND;
            Ok(not_found)
        }
    }
}
```

Dans la dernière section de cet article, nous discuterons de la manière d'ajouter plus de fonctionnalités, telles que des clients de base de données et des clients de services web, au microservice Rust.

## Un Microservice Simple en Node.js

Bien que les microservices basés sur Rust soient légers et rapides, tout le monde n'est pas (encore) un développeur Rust.

Si vous êtes plus à l'aise avec JavaScript, vous pouvez toujours tirer parti de la sécurité, des performances, de la petite empreinte et de la portabilité de WasmEdge dans le edge cloud. Plus précisément, vous pouvez utiliser les API Node.js pour créer des microservices pour WasmEdge !

Pour les applications Node.js, l'empreinte de WasmEdge est inférieure à 15 Mo. Cela se compare à plus de 150 Mo pour l'image Linux Node.js standard.

Exécutez les deux commandes CLI suivantes pour créer puis déployer une application [fly.io](http://fly.io) à partir de notre image Docker légère pour WasmEdge + Node.js.

```rust
$ flyctl launch --image juntaoyuan/flyio-nodejs-echo
$ flyctl deploy
```

C'est tout ! Vous pouvez utiliser la commande curl pour tester si le service web déployé fonctionne réellement. Il renvoie les données que vous lui envoyez.

```bash
$ curl https://solitary-snowflake-1159.fly.dev -d "Hello WasmEdge for Node.js on fly.io!"
Hello WasmEdge for Node.js on fly.io!
```

Le Dockerfile pour l'image Docker `juntaoyuan/flyio-nodejs-echo` contient le package complet du runtime WasmEdge, le runtime QuickJS `wasmedge_quickjs.wasm`, les modules Node.js [modules](https://wasmedge.org/book/en/dev/js/nodejs.html#the-javascript-modules), et l'application de service web `node_echo.js`.

```dockerfile
FROM wasmedge/slim-runtime:0.11.0
ADD wasmedge_quickjs.wasm /
ADD node_echo.js /
ADD modules /modules
CMD ["wasmedge", "--dir", ".:/", "/wasmedge_quickjs.wasm", "node_echo.js"]
```

Le code source JavaScript complet pour l'application `node_echo.js` est le suivant. Comme vous pouvez le voir clairement, il utilise simplement les API Node.js standard pour créer un serveur HTTP asynchrone qui renvoie le corps de la requête HTTP.

```javascript
import { createServer, request, fetch } from 'http';

createServer((req, resp) => {
  req.on('data', (body) => {
    resp.end(body)
  })
}).listen(8080, () => {
  print('listen 8080 ...\n');
})
```

Le moteur QuickJS de WasmEdge fournit non seulement le support Node.js, mais aussi le support d'inférence Tensorflow. Nous avons enveloppé les SDK Rust Tensorflow et WASI-NN dans des API JavaScript afin que les développeurs JavaScript puissent [créer facilement des applications d'inférence IA](https://wasmedge.org/book/en/dev/js/tensorflow.html).

## Microservices avec État sur le Edge

Avec WasmEdge, il est également possible de créer des microservices avec état soutenus par des bases de données. [Ce dépôt GitHub](https://github.com/WasmEdge/wasmedge-db-examples) contient des exemples de clients de base de données non bloquants basés sur tokio dans des applications WasmEdge.

* Le [client MySQL](https://github.com/WasmEdge/wasmedge-db-examples/tree/main/mysql) permet aux applications WasmEdge d'accéder à la plupart des bases de données cloud.

* Le [projet anna-rs](https://github.com/essa-project/anna-rs) est un magasin KV natif pour le edge avec des niveaux de synchronisation et de cohérence ajustables sur les nœuds de edge. Les applications WasmEdge [peuvent utiliser anna-rs](https://github.com/WasmEdge/wasmedge-db-examples/tree/main/anna) comme cache ou base de données de edge.

Vous pouvez maintenant construire une grande variété de services web sur le edge cloud en utilisant les SDK et runtimes WasmEdge. J'ai hâte de voir vos créations !