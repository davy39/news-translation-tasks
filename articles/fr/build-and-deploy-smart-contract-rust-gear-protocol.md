---
title: Comment construire et déployer un contrat intelligent avec Rust et le protocole
  Gear
subtitle: ''
author: Rocky Essel
co_authors: []
series: null
date: '2024-06-04T10:36:01.000Z'
originalURL: https://freecodecamp.org/news/build-and-deploy-smart-contract-rust-gear-protocol
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/How-to-Build-and-Deploy-a-Smart-Contract-With-Rust-and-the-Gear-Protocol-Cover.png
tags:
- name: handbook
  slug: handbook
- name: Rust
  slug: rust
- name: Web3
  slug: web3
seo_title: Comment construire et déployer un contrat intelligent avec Rust et le protocole
  Gear
seo_desc: "Smart contracts are like digital agreements that run on blockchain technology,\
  \ making transactions automatic and secure. While many people use Ethereum and Solidity\
  \ to create these contracts, there are other options that can be just as powerful.\
  \ \nOne..."
---

Les contrats intelligents sont comme des accords numériques qui fonctionnent sur la technologie blockchain, rendant les transactions automatiques et sécurisées. Bien que beaucoup de gens utilisent Ethereum et Solidity pour créer ces contrats, il existe d'autres options qui peuvent être tout aussi puissantes.

Une grande combinaison est l'utilisation de Rust avec le protocole Gear. Dans ce guide, je vais vous montrer comment construire et déployer un contrat intelligent en utilisant Rust et le protocole Gear. Que vous soyez nouveau dans ce domaine ou que vous ayez une certaine expérience, cet article vous aidera à commencer avec des étapes claires et faciles à suivre.

## Prérequis

1. Avoir des connaissances de base en Rust.
2. Avoir une compréhension de base de la décentralisation.

## Table des matières

1. [Introduction au réseau Vara et au protocole Gear.](#heading-introduction-au-reseau-vara-et-au-protocole-gear)
2. [Pourquoi utiliser l'analogie Web2](#heading-pourquoi-utiliser-lanalogie-web2)?
3. [Communication basée sur les messages](#heading-communication-basee-sur-les-messages).
4. [Illustration](#heading-illustration)
5. [Rôle du réseau Vara](#heading-role-du-reseau-vara).
6. [Premier projet – Lire une blague](#heading-premier-projet-lire-une-blague)
7. [Projet suivant – `input-msg`](#heading-projet-suivant-input-msg)
8. [Métadonnées et état](#heading-metadonnees-et-etat)
9. [Troisième projet – Construction de messages](#heading-troisieme-projet-construction-de-messages)
10. [Projet final – Affrontement](#heading-projet-final)
11. [Conclusion.](#conclusion-1)

## Introduction au réseau Vara et au protocole Gear.

### Réseau Vara

Considérez Vara comme la fondation solide de la technologie blockchain. C'est une blockchain de couche 1, ce qui signifie qu'elle est au cœur des transactions, garantissant qu'elles sont sécurisées et décentralisées. Vara utilise la preuve d'enjeu nominée (NPoS) pour l'accord, la rendant fiable et efficace.

De plus, le réseau Vara se distingue par son nouveau modèle d'acteur, une architecture caractérisée par l'isolement et la messagerie asynchrone. Ce changement de paradigme dans l'exécution des contrats intelligents dote le réseau Vara d'une sécurité et d'une évolutivité inégalées, le différenciant des plateformes blockchain conventionnelles.

### Protocole Gear

Le protocole Gear est comme une boîte à outils pour les développeurs. C'est un moteur de contrats intelligents qui rend la construction d'applications décentralisées (dApps) plus rapide, plus sûre et moins chère. En utilisant la technologie de substrat et WebAssembly (Wasm), Gear facilite la création de dApps qui fonctionnent en douceur et en toute sécurité.

L'utilisation par Gear de la machine virtuelle Wasm sert de pierre angulaire à son efficacité. En exploitant la puissance de Wasm, les développeurs peuvent transcender les barrières linguistiques, intégrant de manière transparente des bases de code existantes et accélérant le cycle de développement. Cette fusion de familiarité et de performance ouvre la voie à une nouvelle ère de création de dApps, où vitesse, sécurité et évolutivité convergent harmonieusement.

En termes plus simples, le réseau Vara et le protocole Gear travaillent ensemble pour rendre la technologie blockchain plus conviviale et sécurisée pour la construction et l'utilisation d'applications décentralisées.

## Pourquoi utiliser l'analogie Web2 ?

Comprendre la communication basée sur les messages, en particulier dans le contexte du protocole Gear, peut être assez difficile. Pour obtenir une compréhension plus claire, j'ai étudié la documentation et effectué des recherches supplémentaires. Finalement, je suis tombé sur une analogie qui a fait cliquer tout : l'analogie des requêtes HTTP Web, spécifiquement la méthode POST.

Décomposons cette analogie étape par étape. Considérez le scénario familier d'un utilisateur visitant un site Web comme google.com et interagissant avec la barre de recherche. Lorsque l'utilisateur entre une requête de recherche et appuie sur Entrée, ce qui se passe en coulisses est similaire à une requête HTTP POST étant envoyée.

### Voici comment cela se déroule :

1. **Interaction de l'utilisateur** : L'utilisateur initie l'action en tapant une requête de recherche dans la barre de recherche et en appuyant sur Entrée. Cette action déclenche une demande d'informations.
2. **Reconnaissance du client** : Le site Web de Google, agissant comme l'interface utilisateur côté client (UI), reconnaît l'entrée de l'utilisateur et se prépare à envoyer une requête au serveur pour traitement.
3. **Requête envoyée** : Tout comme lorsque vous appuyez sur Entrée après avoir tapé une requête, le site Web de Google envoie une requête POST à son serveur, transmettant la requête de recherche de l'utilisateur.
4. **Traitement du serveur** : À la réception de la requête POST, le serveur de Google traite la requête, recherchant dans son vaste index des informations pertinentes.
5. **Génération de la réponse** : Après avoir traité la requête, le serveur de Google génère une réponse contenant les résultats de la recherche.
6. **Réponse envoyée** : Enfin, le serveur de Google envoie la réponse au client (le navigateur Web de l'utilisateur), complétant le cycle de communication.

Dans cette analogie, l'utilisateur représente l'initiateur de la communication, le client (UI) sert d'intermédiaire entre l'utilisateur et le serveur, et le serveur agit comme le répondeur, traitant les requêtes et générant des réponses.

En établissant des parallèles entre la communication basée sur les messages dans le protocole Gear et le concept familier des requêtes HTTP Web, nous pouvons mieux comprendre les dynamiques en jeu. Tout comme comprendre comment les requêtes Web facilitent la communication entre les utilisateurs et les serveurs est essentiel pour naviguer sur Internet, comprendre la communication basée sur les messages dans le protocole Gear est crucial pour construire et interagir avec des applications décentralisées de manière efficace.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-114.png)
_fonctionnement de la méthode POST_

## Communication basée sur les messages

De même, le protocole Gear fonctionne en fonction des interactions de l'utilisateur ou du programme. **Note** : Les programmes sur Gear peuvent également interagir les uns avec les autres. Voici donc une explication détaillée du flux de communication complet dans Gear.

### Interaction de l'utilisateur et @gear-js/api

Lorsque l'utilisateur (acteur) interagit avec les éléments de l'interface utilisateur de la dApp (comme des boutons ou des formulaires), `@gear-js/api` (qui est intégré dans l'interface utilisateur) capture ces interactions. En fonction des interactions, il extrait des informations et potentiellement des formats de message prédéfinis, puis contracte un objet de message contenant l'intention ou la demande de l'utilisateur.

### Comment envoyer des messages

L'objet de message construit encapsule l'entrée de l'utilisateur et devient les données que `@gear-js/api` transmet à travers le réseau Vara à la crate Gear dans le programme.

### Comment le programme reçoit et traite les messages

Gear (`crate`) livre l'objet de message au programme approprié déployé sur le réseau Vara en fonction de l'emplacement où l'utilisateur a initié l'action. La crate Gear dans le programme utilise des fonctions comme `msg::load()` et accède à l'objet de message livré, que le programme extrait des informations (telles que `payload`, `source`, `messsageId`), et le traite selon la manière dont il est conçu par le développeur.

### Comment générer une réponse

En fonction de l'entrée traitée, le programme crée un nouvel objet de message contenant une réponse (`response` dans `web2`) à l'action ou à l'interaction de l'utilisateur (appelée `reply`) pour ou pour l'utilisateur. Notez que le programme n'envoie généralement pas l'objet de message original, il en génère un nouveau basé sur le message reçu, qu'une réponse est envoyée pour être reçue par `@gear-js/api` en utilisant la crate `gstd` du programme utilisant des fonctions comme `msg::reply` ou `msg::reply_bytes`.

### Mise à jour de l'interface utilisateur

`@gear-js/api`, dans la dApp, reçoit l'objet de message de réponse livré par la crate `gstd` du programme à travers le réseau Vara et extrait les données de réponse de l'objet de réponse, et met enfin à jour l'interface utilisateur reflétant la réponse du programme à l'interaction de l'utilisateur.

Et c'est à peu près la communication entre les utilisateurs, le client (dApp), le protocole Gear (`gstd`), et enfin le réseau Vara.

## Illustration

Discutons davantage des diagrammes ci-dessous et de la manière dont ils interagissent les uns avec les autres.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-1.png)
_Mise à jour de l'interface utilisateur_

Cette illustration ci-dessus est juste une vue d'ensemble de la manière dont la communication circule de l'utilisateur au programme. Je vais fournir une illustration complète pour plus de clarté. Mais avant cela, divisons l'illustration d'ensemble en trois étapes.

### Étape d'interaction initiale

Comme dit précédemment, c'est lorsque l'utilisateur interagit avec le programme, à la fois `@gear-js/api` et `gstd`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-124.png)
_Étape d'interaction initiale_

### Logique métier/programme

Cette section décrit la communication entre le programme et Gear au sein du réseau Vara. Le `gstd` est utilisé par le programme pour accéder au message transmis (`msg::load()`) de l'étape initiale afin d'exécuter la logique métier.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-126.png)
_Logique métier/programme_

### Réponse (Réponse)

Cette étape finale montre comment les commentaires de l'utilisateur sont livrés à l'utilisateur ou au programme. `@gear-js/api` le traduit si nécessaire, puis met à jour l'interface utilisateur de la dApp avec les résultats. Cela permet à l'utilisateur de voir le résultat de son action au sein de la dApp.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-127.png)
_Réponse (Réponse)_

C'est super, n'est-ce pas ? Cela devrait vous aider à comprendre comment les messages sont transmis du client au programme. Mais que signifie le rôle du réseau Vara ici ? Plus tôt, j'ai dit que l'objet de message est transmis à travers le réseau Vara, mais je n'ai pas dit comment. Expliquons cela.

## Rôle du réseau Vara

Dans Vara, tous les participants, y compris les interfaces utilisateur (via `@gear-js/api`) et les contrats intelligents (programmes et `gstd`), sont considérés comme des acteurs. Un autre point à savoir est que les acteurs n'appellent pas directement les fonctions au sein d'autres acteurs (comme dans les programmes interagissant avec d'autres programmes ou même avec les utilisateurs).

Au lieu de cela, ils envoient des messages contenant des données ou des instructions. Donc, dans notre explication de la communication basée sur les messages, Vara sert d'infrastructure de réseau décentralisée sous-jacente pour la communication de notre système (dApps). Il fournit une plateforme sécurisée et fiable pour la transmission de messages à travers un réseau distribué de nœuds. Et puisque Vara utilise un mécanisme de consensus NPoS (Nominated Proof-of-Stake), il garantit la sécurité du réseau et la validation des transactions.

## Mettons les mains dans le cambouis

Afin de construire sur les informations ci-dessus que j'ai fournies, vous et moi devons nous salir les mains en construisant et en déployant des programmes avec une explication supplémentaire pour une compréhension plus claire.

Commençons.

### Premier projet - Lire une blague

Dans ce projet, vous allez interagir avec et déployer votre contrat intelligent sur le réseau Vara, et recevoir un message de réponse en retour.

Ceci est juste un projet simple, et rien de trop complexe. J'ai choisi cet exemple de projet parce qu'il s'aligne avec l'analogie que j'ai donnée précédemment.

Actuellement, ce projet devrait bien fonctionner lorsqu'il est exécuté sur votre système Windows. Au cas où vous obtiendriez une erreur, faites défiler jusqu'à la partie de cet article avec un guide pour configurer un sous-système Windows pour Linux (WSL), car cela vous permettrait d'exécuter un environnement Linux, y compris des outils et applications en ligne de commande, directement sur Windows, sans le surcoût d'une machine virtuelle traditionnelle ou d'une configuration de démarrage double.

Pour commencer, créez un répertoire nommé `freecodecamp-gear-protocol`. Puisque vous allez construire environ quatre projets, et je pense qu'il est important de savoir comment configurer vos projets pour le protocole Gear.

Donc, dans votre répertoire `freecodecamp-gear-protocol`, créez un fichier `Cargo.toml` avec le code suivant :

```toml
[workspace]
resolver = "2"
members = []


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates
# External Crates
```

Pour quelqu'un qui est nouveau dans Rust ou habitué à créer des projets uniques, je vais vous guider à travers la compréhension et la configuration d'un espace de travail dans Rust, rendant cela facile à comprendre.

### Comprendre votre espace de travail

Un espace de travail dans Rust est un ensemble de packages (crates) qui sont gérés ensemble. Décomposons les sections clés : `[workspace]`, `members`, `[workspace.package]`, et `[workspace.dependencies]`. Donc, pensez à cela comme une cabine pour vos chaussures, où chaque paire de chaussures est une crate (package) que vous voulez garder organisée.

#### Section `[workspace]`

La section `[workspace]` définit l'espace de travail global. Il contient généralement plusieurs membres.

**`resolver = "2"`** : Spécifie la version du résolveur de fonctionnalités de Cargo à utiliser, améliorant la manière dont les dépendances sont gérées dans l'espace de travail.

**`members`** : Liste les crates qui font partie de l'espace de travail. Lorsque vous ajoutez un projet avec `cargo new --lib sneakers` ou `boots`, la section `members` du `Cargo.toml` est remplie avec le nom du projet que vous avez créé.

> Si elles ne sont pas ajoutées automatiquement, vous pouvez les ajouter vous-même.

Par exemple :

```toml
members = ["sneakers", "boots"]

```

#### Section `[workspace.package]`

Cette section fournit des métadonnées pour l'espace de travail entier comme s'il s'agissait d'un seul package.

* **`name`** : Le nom du package de l'espace de travail.
* **`version`** : La version du package de l'espace de travail.
* **`edition`** : L'édition de Rust utilisée (par exemple, "2021").
* **`authors`** : Liste des auteurs.
* **`license`** : La licence pour le package de l'espace de travail.
* **`publish`** : Indique si le package de l'espace de travail doit être publié sur crates.io.

Exemple :

```toml
[workspace.package]
name = "my-shoe-collection"
version = "0.1.0"
edition = "2021"
authors = ["Your Name"]
license = "MIT"
publish = false
```

#### Section `[workspace.dependencies]`

Liste les dépendances qui s'appliquent à l'espace de travail entier. Cela signifie que chaque crate, qu'elle soit externe ou interne, ajoutée à `[workspace.dependencies]` est accessible à chaque projet que vous créez sous l'espace de travail du projet. Voici donc comment les crates externes et internes sont rendues accessibles à d'autres projets.

**Note** : Pour les crates internes, vous devez les ajouter vous-même.

**`Internal Crates`** : Ajoutez les crates internes comme ceci :

```toml
sneakers = { path = "sneakers" }
boots = { path = "boots" }
```

**`External Crates`** : Ajoutez les crates externes comme ceci :

```toml
polish = "1.0"
```

### Exemple de `Cargo.toml`

Voici un exemple combinant ces sections :

```toml
[workspace]
resolver = "2"
members = ["sneakers", "boots"]

[workspace.package]
name = "my-shoe-collection"
version = "0.1.0"
edition = "2021"
authors = ["Your Name"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal crate
sneakers = { path = "sneakers" } 
boots = { path = "boots" } 

# External crate
polish = "1.0"
```

Donc, voici comment vous configurez un espace de travail pour votre projet afin de gérer plusieurs crates (sous-projets) et de partager des dépendances et des paramètres de configuration entre eux. J'ai passé beaucoup de temps à comprendre cela, alors j'ai pensé le partager avec vous tous pour le rendre plus facile.

Pour construire votre premier contrat intelligent, exécutez la commande ci-dessous dans votre répertoire parent (`freecodecamp-gear-protocol`) sur votre terminal.

```bash
cargo new --lib receive-joke
```

```bash
.freecodecamp-gear-protocol
├── Cargo.toml
└── receive-joke
    ├── Cargo.toml
    └── src
        └── lib.rs

2 directories, 3 files
```

Rendez-vous dans votre fichier `freecodecamp-gear-protocol/receive-joke/Cargo.toml`, et voici comment vous accédez aux crates et à la configuration du répertoire de l'espace de travail (principal) en utilisant `.workspace=true`, comme ci-dessous ;

```toml
[package]
name ="receive-joke"
version.workspace = true
edition.workspace = true
authors.workspace = true
license.workspace = true
publish.workspace = true

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
```

Ensuite, créez un fichier `build` dans votre répertoire `receive-joke` avec un chemin comme `receive-joke/build.rs`, et collez le code ci-dessous. Maintenant, le `build.rs` vous aide à construire votre projet en un fichier `.wasm`, qui est utilisé pour déployer votre contrat intelligent.

**build.rs:**

```rust
fn main() {
    gear_wasm_builder::build();
}
```

Actuellement, vous n'avez pas installé la crate nécessaire pour vous aider à créer votre contrat intelligent. Par conséquent, ajoutez la crate suivante à votre dépendance de l'espace de travail.

**Cargo.toml:**

```toml
[workspace]
resolver = "2"
members = ["receive-joke"]


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates

# External Crates
gstd = "1.4.1"
gmeta = "1.4.1"
gtest  = "1.4.1"
gear-wasm-builder = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

Pour votre premier projet, seule `gstd` sera utilisée, alors ajoutez cette crate externe au `Cargo.toml` de votre `receive-joke`. Comme ci-dessous :

```toml
[dependencies]
gstd.workspace = true


[build-dependencies]
gear-wasm-builder.workspace = true
```

Si vous êtes arrivé ici sans aucune erreur, bien joué mon ami. Ensuite, il faut effacer tout code dans `freecodecamp-gear-protocol/receive-joke/src/lib.rs`. Passons à l'étape suivante.

Dans le protocole Gear, il y a des points d'entrée. Un point d'entrée sert de passerelle ou de porte à votre code. Gear a quelques points d'entrée, à savoir :

```rust
state(),
handle(),
handle_reply(),
init(),
handle_signal(),
```

Chaque point d'entrée joue un rôle significatif. Par exemple, `init()` est appelé lorsque le contrat intelligent (`.wasm`) est déployé, vous permettant de définir certaines conditions ou variables ou même d'autres fonctions qui doivent être exécutées pour le bon fonctionnement de votre contrat intelligent ou programme.

Cependant, il est facultatif, ce qui signifie que vous pouvez choisir de l'inclure ou de l'exclure en fonction de votre projet, mais il est toujours exécuté, et c'est le premier message que vous verrez une fois que vous aurez déployé votre contrat intelligent.

La méthode `handle()` est cruciale car elle contient la majeure partie de la logique métier. Il est obligatoire de l'inclure dans votre programme. Plus de détails seront partagés sur les points d'entrée au fur et à mesure que vous avancerez.

Maintenant, collez le code suivant dans votre fichier `receive-joke/src/lib.rs` :

```rust
#![no_std]

use gstd::msg;

#[no_mangle]
extern "C" fn handle() {
    // Envoyer une réponse (dans une requête HTTP GET, vous utiliseriez "response").
    msg::reply_bytes(
        "What did the dirt say to the rain? If you keep this up, my name will be mud!",
        0,
    )
    .expect("Unable to reply");
}
```

Le code ci-dessus définit une fonction `handle` qui, lorsqu'elle est appelée, envoie un message que vous avez défini comme réponse en utilisant la fonctionnalité `gstd::msg`. Ce `gstd` est une crate fournie par le protocole Gear, pour envoyer et recevoir des messages, et cela est crucial pour que les programmes fonctionnant sur le réseau Vara communiquent entre eux et avec des systèmes externes. Et le `reply_bytes` envoie un nouveau message en réponse au message qui est actuellement traité.

Il est temps de déployer et d'envoyer votre premier message et de recevoir votre réponse de blague. Dans votre terminal, exécutez la commande suivante pour construire votre programme en **`.wasm`**.

Habituellement, j'utilise `cargo check` pour vérifier les erreurs d'abord, avant d'utiliser la commande `build` ci-dessous, les deux méthodes sont correctes.

```bash
cargo build --release
```

Après la construction, suivez la structure ci-dessous pour localiser votre fichier **`.wasm`** dans le chemin ci-dessous :

```bash
.freecodecamp-gear-protocol
├── Cargo.lock
├── Cargo.toml
├── receive-joke
│   └── ...
└── target
    ├── ...
    └── wasm32-unknown-unknown
        ├── ...
        └── release
            ├── receive_joke.opt.wasm <--- Optimisé pour le déploiement.
            └── receive_joke.wasm
```

### Comment déployer votre contrat intelligent

Tout comme dans d'autres outils blockchain qui vous aident à déployer votre contrat intelligent depuis le terminal, IDEA est l'endroit où vous déployez votre contrat intelligent et interagissez avec lui. Nous allons explorer l'interface dans un instant. Donc, enfin, rendez-vous sur [IDEA](https://idea.gear-tech.io/) pour commencer à vous familiariser avec votre environnement de déploiement.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-135927.png)
_Application Web de déploiement de contrats intelligents - IDEA_

1. Première étape, cliquez sur **Upload program**, puis sélectionnez ou glissez votre fichier **`.opt.wasm`** à l'intérieur de la modale. Cela vous amène à la page de téléchargement, où vous pouvez changer les noms, entrer des valeurs pour la charge utile, ou changer le type de charge utile. Pour l'instant, laissons tout tel quel, et cliquons sur **Calculate**, qui entrera une valeur de frais de gaz de `0.00015` pour télécharger votre programme.

**Note** : Vous pouvez soit définir vous-même la limite de gaz, soit cliquer sur **Calculate** pour permettre au programme d'en générer une pour vous.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-144729.png)
_Détails de la page de téléchargement_

À ce stade, cliquez sur **Upload Program**, puis sur le bouton **Submit**.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-144825.png)
_Détails de la transaction - PopUp_

Lorsque vous soumettez, vous serez invité à vous connecter à votre portefeuille et à approuver.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-128.png)
_Portefeuille - SubWallet_

Après l'approbation, un message toast devrait s'afficher dans le coin supérieur droit de l'écran de votre ordinateur/portable pour que vous puissiez voir l'état de votre programme, s'il a échoué ou réussi.

En supposant que c'est un succès, cliquez sur **Programs** dans la barre latérale, puis BOOM!, voici votre programme. Cliquez dessus, et explorons.

Lors du déploiement, la première chose que vous voyez est l'ID du programme, mais après quelques secondes, le nom de votre programme sera affiché.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-150230.png)
_Bloc de contrat intelligent - Page_

Plus tôt, j'ai dit que lorsque vous déployez un programme, la fonction `init()` est exécutée indépendamment du fait que vous l'ayez définie dans votre projet ou non, et c'est ce que vous voyez dans la section **Messages**. Ci-dessous se trouve une simple illustration pour vous familiariser et comprendre les informations concernant votre programme.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-129.png)
_Illustration de la page_

Maintenant, il est temps d'envoyer un message à votre programme et de recevoir une réponse, qui est notre blague. N'oubliez pas que vous ne saisissez aucune valeur, vous effectuez simplement une action simple pour recevoir une réponse du programme. Donc, cliquez sur **Calculate** et appuyez sur le bouton **Send Message** (c'est l'action ou l'interaction).

![Image](https://www.freecodecamp.org/news/content/images/2024/03/Screenshot-2024-03-30-152529.png)
_Exécution d'une action - Étape initiale_

Après l'envoi du message, un toast de `success` s'affichera. Ensuite, revenez à votre programme en cliquant sur le bouton **Cancel**, et vous verrez deux messages supplémentaires.

N'oubliez pas que la couleur bleue avec la flèche représente le message que vous avez envoyé, et le vert représente la réponse que vous avez reçue. Donc, cliquez sur le message répondu pour voir la blague, qui dit : `What did the dirt say to the rain? If you keep this up, my name will be mud!`.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/image-130.png)
_Réception de la réponse et plus d'illustrations_

Maintenant, vous avez enfin terminé ce projet. Dans le prochain projet, vous allez envoyer des données ou des informations à votre programme, et il renverra une réponse avec votre valeur saisie attachée. [Voici le programme déployé sur le **réseau Vara**](https://idea.gear-tech.io/programs/0x79e6c86aa1ab2026ef3bbc0ccbe801ce085ca2614b36f9e5be04d2354ad56396).

### Informations importantes

Bien que j'aie fourni un certain contexte à l'image ci-dessus, je souhaite l'approfondir. À la fois la `Source` et la `Destination` prennent une adresse qui peut être soit un utilisateur (acteur) et un programme (acteur), ou même un objet de message.

## Projet suivant – `input-msg`

Tout comme l'illustration précédente, vous allez interagir avec votre programme en envoyant une valeur d'entrée à votre contrat intelligent déployé sur **`[IDEA](https://idea.gear-tech.io/programs?node=wss%3A%2F%2Ftestnet.vara.network)`**. [**IDEA**](https://idea.gear-tech.io/programs?node=wss%3A%2F%2Ftestnet.vara.network) est votre environnement de déploiement où vous déployez votre contrat intelligent sur le réseau Vara. Le but ici est pour vous de charger des valeurs d'entrée de votre utilisateur, et de les traiter en concaténant une chaîne à la valeur d'entrée de l'utilisateur : "Nous avons reçu votre requête. {entrée de l'utilisateur}".

C'est la réponse que vous enverrez à l'utilisateur qui envoie un message (valeur d'entrée).

Donc, dans votre répertoire `freecodecamp-gear-protocol`, exécutez la commande ci-dessous pour ajouter un autre membre à votre `freecodecamp-gear-protocol/Cargo.toml`.

```bash
cargo new --lib input-msg
```

Après avoir ajouté un autre membre ou projet dans le `freecodecamp-gear-protocol`, votre chemin devrait être `freecodecamp-gear-protocol/input-msg`.

Plus tôt, j'ai mentionné comment accéder aux valeurs d'entrée dans le contrat intelligent ou le programme en utilisant `gstd`, qui a une fonction ou méthode appelée `load()`. Pour l'étape suivante, effacez votre fichier `freecodecamp-gear-protocol/input-msg/src/lib.rs`, et collez le code suivant et exécutez `cargo check`.

```bash
#![no_std]

use gstd::{msg, prelude::*};

#[no_mangle]
extern "C" fn handle() {
    let new_msg = msg::load().expect("Unable to create string");
    let reply_msg = format!("We've received your query {}", new_msg);
    msg::reply_bytes(reply_msg, 0).expect("Unable to reply.");
}

```

La vérification échoue, mais pourquoi ? Eh bien, la fonction `load()` a un type de `unknown`. Et puisque Rust est un langage fortement typé, il doit toujours connaître le type à l'avance, ce qui n'était pas le cas, donc il n'a pas pu construire le projet.

Cela devrait vous dire que `load()` n'a pas de type, et c'est à vous de définir le bon type de données, et l'échec à le faire entraînerait des erreurs frustrantes comme ci-dessous.

### Débogage

Maintenant, si vous deviez utiliser un projet unique et non un espace de travail, alors le débogage de l'erreur aurait été facile comme ci-dessous.

```bash
     
  error[E0282]: type annotations needed
   --> C:\Users\user\Desktop\2024\web3\re-gear\input-msg\src\lib.rs:7:9
    |
  7 |     let new_msg = msg::load().expect("Unable to create string");
    |         ^^^^^^^
    |
  help: consider giving `new_msg` an explicit type
    |
  7 |     let new_msg: /* Type */ = msg::load().expect("Unable to create string");
    |                ++++++++++++

```

Mais puisque vous et moi utilisons un espace de travail, cela rend le débogage un peu difficile. Voici le message d'erreur que j'ai obtenu lors du débogage de cette erreur.

```bash
  error[E0275]: overflow evaluating the requirement `gstd::parity_scale_codec::Compact<_>: gstd::Decode`
    |
    = help: consider increasing the recursion limit by adding a `#![recursion_limit = "256"]` attribute to your crate (`input_msg`)
    = note: required for `gstd::parity_scale_codec::Compact<_>` to implement `gstd::Decode`
    = note: 125 redundant requirements hidden
    = note: required for `gstd::parity_scale_codec::Compact<<_ as CompactAs>::As>` to implement `gstd::Decode`

  For more information about this error, try `rustc --explain E0275`.
  error: could not compile `input-msg` (lib) due to 1 previous error
  warning: build failed, waiting for other jobs to finish...
  error: cargo command run failed: exit status: 101
warning: build failed, waiting for other jobs to finish...
```

Et si vous regardez de près, vous pouvez dire que `input-msg` est ce qui crée l'erreur. Dans ce cas, exécutez `rustc --explain E0275`, qui produit une suggestion comme celle-ci

```bash
An evaluation of a trait requirement overflowed.

Erroneous code example:

trait Foo {}

struct Bar<T>(T);

impl<T> Foo for T where Bar<T>: Foo {}

This error occurs when there was a recursive trait requirement that overflowed before it could be
evaluated. This often means that there is an unbounded recursion in resolving some type bounds.

To determine if a T is Foo, we need to check if Bar<T> is Foo. However, to do this check, we need to
determine that Bar<Bar<T>> is Foo. To determine this, we check if Bar<Bar<Bar<T>>> is Foo, and so on. This
is clearly a recursive requirement that can't be resolved directly.

Consider changing your trait bounds so that they're less self-referential.
```

Maintenant, bien que, comparé au premier message d'erreur, ce message ne fournit pas de solution directe, il vous indique qu'il y a une erreur de type dans votre code. Et la raison est que `load()` peut charger n'importe quel type de données, donc vous devez toujours définir un type pour celui-ci.

```rust
#![no_std]

use gstd::{msg, prelude::*};

#[no_mangle]
extern "C" fn handle() {
    let new_msg: String = msg::load().expect("Unable to create string");
    let reply_msg = format!("We've received your query {}", new_msg);
    msg::reply_bytes(reply_msg, 0).expect("Unable to reply.");
}

```

Dans le code ci-dessus, vous avez ajouté un type `String` à `new_msg` car c'est le `type` que vous attendez. Maintenant, exécutez la commande de construction et déployez le fichier **`.opt.wasm`** sur `IDEA`.

```bash
.freecodecamp-gear-protocol
├── receive-joke
├── Cargo.toml
├── input-msg
│   └── ...
└── target
    ├── ...
    └── wasm32-unknown-unknown
        ├── ...
        └── release
            ├── input_msg.opt.wasm <--- Optimisé pour le déploiement.
            ├── input_msg.wasm
            ├── receive_joke.opt.wasm
            └── receive_joke.wasm
```

Lorsque vous avez terminé, allez dans votre programme et cliquez sur **Send Messages**. Tapez n'importe quelle valeur dans le champ `payload`, et il doit être de type `String`.

Soumettez et approuvez, puis revenez à votre programme, sélectionnez votre boîte `reply_message` et vous devriez voir votre `reply message`.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/Screenshot-2024-04-06-080437.png)
_Contrat intelligent - Message de réponse_

[Vous pouvez trouver le programme ici sur le réseau Vara](https://idea.gear-tech.io/programs/0x25629eaa3c7a51ec407f89bbaae7ccb4f58c6026283758d0fccb50e3bb042bdd).

## Métadonnées et État

Les métadonnées et l'état vont de pair. Pour que votre application cliente permette aux utilisateurs d'interagir ou de demander des données (état) à partir de votre contrat intelligent, vous devez définir à la fois les métadonnées et l'état, et même si l'état est défini et que les métadonnées n'ont pas été fournies, vous ne pouvez pas accéder aux données.

Alors, prenons chaque étape une par une.

### Métadonnées

Dans le monde du protocole Gear, les métadonnées sont comme un plan pour définir comment différentes parties d'une application décentralisée (dApp) communiquent entre elles. C'est similaire à la manière dont les interfaces ou les types fonctionnent en TypeScript. Ces plans décrivent comment des choses comme le type de données initial à attendre, la gestion des messages et l'échange de données se produisent dans la dApp, qu'il s'agisse de `In`, `Out` et `InOut`.

Lorsque nous créons des plans clairs, cela aide les développeurs à s'assurer que toutes les différentes parties de la dApp comprennent les formats de données des unes et des autres. Cela facilite le partage de données entre le contrat intelligent (programme-acteur) et l'application côté client.

Pour créer ces plans pour votre programme, nous utilisons l'outil `gmeta`. Il nous aide à définir ces plans en décrivant comment différentes interactions fonctionnent et quels types de données elles impliquent.

Donc, pensez aux métadonnées dans votre programme comme étant similaires à la manière dont les interfaces/types fonctionnent en TypeScript. Ils aident à organiser comment les différentes parties de votre dApp communiquent et comprennent les données des unes et des autres.

### Exemple de métadonnées

```bash
use gmeta::{InOut, Metadata, Out};

pub struct ProgramMetadata;

// Assurez-vous de décrire tous les types.
// Mais si l'un des points de terminaison est manquant dans votre programme, vous pouvez utiliser ();
// comme indiqué dans le cas de `type Signal`.

impl Metadata for ProgramMetadata {
    type Init = InOut<MessageInitIn, MessageInitOut>;
    type Handle = InOut<MessageIn, MessageOut>;
    type Others = InOut<MessageAsyncIn, Option<u8>>;
    type Reply = String;
    type Signal = ();
    type State = Out<Vec<Wallet>>;
}
```

Ce qui précède est un exemple de la manière dont cela est défini. Ne vous inquiétez pas si vous ne le comprenez pas maintenant, je couvrirai plus de détails plus tard. Parlons maintenant de l'état.

### État

Dans le protocole Gear, la fonction `state` sert d'espace de stockage dédié au sein d'un programme. Ce stockage nous permet de stocker et de récupérer des données selon les besoins. Puisque ces données sont stockées dans une mémoire persistante, elles restent accessibles même après l'arrêt du contrat. Ce qui est fascinant, c'est que toute personne ayant accès à la blockchain peut consulter ces données stockées. La fonction `state` ne modifie ni ne modifie la blockchain elle-même. Au lieu de cela, elle fournit simplement un moyen d'accéder aux données stockées dans le programme.

Voici un exemple de fonction `state` :

```bash
// Décrire la structure de l'état
#[derive(TypeInfo, Decode, Encode, Clone)]
pub struct Messages {
    pub id: ActorId,
    pub content: String,
}

// Déclarer et initialiser l'état
static mut MESSAGES: Vec<Messages> = Vec::new();

#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}
```

Lorsque la fonction `state` est appelée, elle retourne une liste de données `wallets` stockées dans le programme. Cela signifie que, une fois qu'un programme est déployé sur la blockchain, n'importe qui peut lire son état.

De plus, les développeurs ont la flexibilité de créer des programmes personnalisés qui peuvent lire l'état. Cela nous permet, à vous et à moi, de personnaliser nos méthodes d'accès aux données en fonction des besoins spécifiques de notre dApp, même si le programme principal subit des modifications.

Le point clé à retenir est que la fonction `state` facilite l'accès aux données stockées dans les contrats intelligents. Il est important de noter que les utilisateurs et d'autres programmes peuvent accéder à l'état d'un programme, offrant un moyen polyvalent d'interagir avec les données stockées.

## Troisième projet - Construction de messages

Dans notre dernier projet `input-msg`, nous n'avons pas gardé trace des messages qui ont été envoyés. Donc dans ce projet, nous allons couvrir les métadonnées et l'état.

Exécutez la commande ci-dessous pour créer votre projet dans **/freecodecamp-gear-protocol/**:

```bash
cargo new --lib messages
```

Ensuite, ajoutez votre fichier **build.rs**, et rendez les dépendances de l'espace de travail disponibles pour le répertoire **/freecodecamp-gear-protocol/messages**.

### Ajout de métadonnées aux messages

Pour configurer des métadonnées pour votre projet, vous devez créer une crate supplémentaire pour gérer cela, donc `cd` dans **messages**, et exécutez la commande ci-dessous.

```bash
cargo new --lib io
```

Dans votre fichier **freecodecamp-gear-protocol/messages/io/Cargo.toml**, copiez et collez le code suivant :

```toml
[package]
name = "messages-io"
version.workspace = true
edition.workspace = true


[dependencies]
gstd.workspace = true
gmeta.workspace = true
```

Ici, j'ai changé le nom de `io` en `messages-io`, et la raison est pour moi de l'identifier et de le séparer des autres `io` dans l'espace de travail. Et ajoutez les dépendances.

Pour utiliser `io` dans votre espace de travail, vous devez aller dans le fichier **freecodecamp-gear-protocol/Cargo.toml**, et ajouter un chemin de votre `io` à votre espace de travail, que vous pouvez ensuite utiliser dans l'un des projets qui ont besoin de `struct`, `enum`, et `method`.

Dans **freecodecamp-gear-protocol/Cargo.toml** :

```bash
[workspace]
resolver = "2"
members = ["receive-joke","input-msg"]


[workspace.package]
name = "freecodecamp-gear-protocol"
version = "0.1.0"
edition = "2021"
authors = ["Rocky Essel"]
license = "MIT"
publish = false

[workspace.dependencies]
# Internal Crates
messages-io={path = "messages/io"} < ---- Here

# External Crates
gstd = "1.4.1"
gmeta = "1.4.1"
gtest  = "1.4.1"
gear-wasm-builder = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

Et c'est la `Internal Crate` dont j'ai parlé plus tôt. Ensuite, vous devez inclure `messages-io` dans votre projet `messages`, comme ci-dessous :

```toml
[package]
name="messages"
version.workspace = true
edition.workspace = true
authors.workspace = true
license.workspace = true
publish.workspace = true


[dependencies]
gstd.workspace = true
messages-io.workspace = true <---

[build-dependencies]
gear-wasm-builder.workspace = true
messages-io.workspace = true < ---

```

La raison d'ajouter `messages-io.workspace` à la fois dans les sections `[dependencies]` et `[build-dependencies]` est de rendre les `struct`, `enums`, `pub variables` et `methods` accessibles à `messages/src/lib.rs`, et `messages/build.rs` en utilisant `messages-io.workspace`.

### Métadonnées dans `io/src/lib.rs`

```rust
#![no_std]

use gmeta::{InOut, Metadata, Out};
use gstd::{prelude::*, ActorId, Vec};

pub struct MessageMetadata;

pub static mut MESSAGES: Vec<User> = Vec::new();

pub struct Message {
    pub id: ActorId,
    pub content: String,
}

impl Metadata for MessageMetadata {
    type Init = InOut<Message, String>;
    type Handle = InOut<Message, String>;
    type State = Out<Vec<Message>>;
    type Reply = ();
    type Others = ();
    type Signal = ();
}

```

Pour implémenter la logique du système de gestion des messages pour votre programme ou contrat intelligent, comprendre comment définir les métadonnées de votre programme est crucial. Par conséquent, une attention particulière est nécessaire ici.

La structure `MessageMetadata` que vous avez définie implémente le trait `Metadata`, qui structure ensuite les métadonnées des messages pour le programme. De plus, une variable statique mutable `MESSAGES` est déclarée pour stocker tous les messages que vous et vos utilisateurs envoyez au programme. Et puisque c'est une variable statique mutable, un code non sécurisé sera nécessaire pour la modifier en raison des garanties de sécurité de Rust autour des variables statiques mutables.

La structure `Message` est définie avec deux champs : `id` (identifiant de l'expéditeur) et `content` (le texte du message).

Le trait `Metadata` est implémenté pour `MessageMetadata`, définissant plusieurs types associés. Le type `Init` est défini comme `InOut<MessageInit, String>`, spécifiant les types d'entrée-sortie pour la phase d'initialisation. \

Cela signifie que lorsque le contrat est initialisé, il acceptera un type `MessageInit` et retournera une `String`. Le type `Handle` est défini comme `InOut<Message, String>`, spécifiant les types d'entrée-sortie pour la gestion des messages. Il accepte un type `Message` en entrée et retourne une `String`.

Le type `State` est défini comme `Out<Vec<Message>>`, définissant le type de sortie de l'état, ce qui signifie que l'état du contrat sera un vecteur d'objets `Message`, et il n'accepte aucune entrée pour récupérer cet état. Les types `Reply`, `Others` et `Signal` sont tous définis comme `()`, indiquant qu'aucune réponse supplémentaire, d'autres types ou signaux ne sont utilisés dans ce cas.

### Contexte supplémentaire de son utilisation.

Dans ce système, la définition des métadonnées spécifie comment le contrat intelligent doit gérer l'initialisation et la gestion des messages. Pendant la phase d'initialisation (`Init`), lorsque le contrat est déployé sur le réseau Vara, il utilise le type `Init` pour configurer l'état initial. L'entrée est censée être de type `MessageInit`, et la sortie sera une `String`. Pendant le déploiement, vous fournissez votre ID et le contenu du message, que le contrat traite en utilisant la méthode `init()`.

Après le déploiement, le contrat peut gérer de nouveaux messages en utilisant le type `Handle`, qui attend un type `Message` en entrée et retourne une `String` en réponse. Cette fonctionnalité est utile pour ajouter de nouveaux messages au vecteur `MESSAGES`. Pour la gestion de l'état (`State`), l'état du contrat est une liste de messages (`Vec<Message>`), et il n'accepte aucune entrée pour récupérer l'état mais produit l'état actuel lorsqu'il est interrogé.

Donc, pour résumer, le code dans **freecodecamp-gear-protocol/messages/io/src/lib.rs** définit la structure et le comportement d'un contrat intelligent de gestion de messages, spécifiant comment il s'initialise, gère les messages et gère l'état.

### Construction des métadonnées

Pour construire votre projet avec les métadonnées, vous devez modifier le fichier **build.rs**, qui initialement ressemble à ceci :

```rust
fn main() {
    gear_wasm_builder::build();
}

```

Il n'y a rien de mal à utiliser le code ci-dessus, mais si vous prévoyez de construire votre programme et de le déployer sur la blockchain pour l'utiliser sur le client ou ailleurs, il serait impossible d'interagir avec votre contrat intelligent si les métadonnées ne sont pas définies. Pensez à cela comme à l'`ABI` dans d'autres environnements blockchain.

Donc, remplacez le code par :

```rust
use messages_io::MessageMetadata;

fn main() {
    gear_wasm_builder::build_with_metadata::<MessageMetadata>();
}
```

Enfin, vous allez gérer la logique de votre contrat intelligent dans le fichier `messages/src/lib.rs` en utilisant la fonction `handle()`.

Voici le code pour le fichier `lib.rs` :

```rust
#![no_std]

use gstd::{exec, msg, prelude::*, ActorId};

use messages_io::*;

#[no_mangle]
extern "C" fn init() {
    let init: Message = msg::load().expect("Unable to decode Message");
    let init_message = Message {
        id: init.id,
        content: init.content,
    };

    unsafe { MESSAGES.push(init_message) };    
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}


#[no_mangle]
extern "C" fn handle() {
    
    let message_handler: Message = msg::load().expect("Unable to decode Message");
    let message = Message {
        id: message_handler.id,
        content: message_handler.content,
    };
    unsafe { MESSAGES.push(message) };
    msg::reply_bytes("Message sent successfully.", 0).expect("Failed to send  reply message.");
}


#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}
```

### Fonction d'initialisation (`init`)

```rust
#[no_mangle]
extern "C" fn init() {
    let init: Message = msg::load().expect("Unable to decode Message");
    let init_message = Message {
        id: init.id,
        content: init.content,
    };

    unsafe { MESSAGES.push(init_message) };
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}

```

La fonction `init` est le point d'entrée pour l'initialisation du contrat intelligent. Elle est marquée avec `#[no_mangle]` pour empêcher Rust d'appliquer le name mangling, rendant la fonction accessible depuis l'environnement d'exécution du contrat intelligent.

La fonction commence par charger le message initial à partir de la charge utile d'entrée en utilisant `msg::load()`. Ce message est censé être de type `Message`, et si le décodage échoue, la fonction paniquera avec un message d'erreur. Ensuite, une nouvelle instance de `Message` est créée à partir des données chargées. Ce nouveau message est ensuite ajouté au vecteur global `MESSAGES`, qui est une variable statique mutable marquée comme non sécurisée en raison des risques potentiels de course de données. Enfin, la fonction envoie une réponse indiquant une initialisation réussie en utilisant `msg::reply_bytes`. Si cette réponse échoue, la fonction paniquera.

### Fonction de gestion des messages (`handle`)

```rust
#[no_mangle]
extern "C" fn handle() {
    let message_handler: Message = msg::load().expect("Unable to decode Message");
    let message = Message {
        id: message_handler.id,
        content: message_handler.content,
    };
    unsafe { MESSAGES.push(message) };
    msg::reply_bytes("Message sent successfully.", 0).expect("Failed to send  reply message.");
}

```

La fonction `handle` est conçue pour gérer les messages entrants après le déploiement du contrat. Comme la fonction `init`, elle est marquée avec `#[no_mangle]` pour s'assurer qu'elle peut être appelée depuis l'environnement d'exécution du contrat intelligent. La fonction commence par charger le message entrant à partir de la charge utile d'entrée. Ce message est décodé dans une structure `Message`, et si le décodage échoue, la fonction paniquera.

Une nouvelle instance de `Message` est ensuite créée à partir des données décodées et ajoutée au vecteur global `MESSAGES` en utilisant un bloc non sécurisé. La fonction envoie ensuite une réponse indiquant que le message a été envoyé avec succès. Si la réponse échoue, la fonction paniquera.

### Fonction de requête d'état (`state`)

```rust
#[no_mangle]
extern "C" fn state() {
    msg::reply(unsafe { MESSAGES.clone() }, 0).expect("Failed to share state");
}

```

La fonction `state` permet d'interroger l'état actuel du contrat intelligent. Elle est également marquée avec `#[no_mangle]` pour les mêmes raisons que les fonctions précédentes. La fonction répond avec une version clonée du vecteur global `MESSAGES`, contenant tous les messages qui ont été ajoutés jusqu'à présent. Cela est fait dans un bloc non sécurisé en raison de la variable statique mutable. Si la fonction échoue à envoyer l'état, elle paniquera.

Ainsi, ce code définit simplement un contrat intelligent avec trois fonctions principales : `init` pour l'initialisation, `handle` pour le traitement des messages entrants, et `state` pour l'interrogation de l'état actuel du contrat. Chaque fonction gère soigneusement le vecteur global `MESSAGES`.

### Déploiement sur le réseau Vara

%[https://www.loom.com/share/e967ebf211f54f2c9c85fedc593e427e?sid=3ef6709a-8b5a-412b-b80c-93f721ba135b]

Maintenant, vous avez terminé ce projet, et j'espère que vous avez appris et compris la plupart de ce que j'ai écrit. Dans notre prochain projet, vous allez construire quelque chose d'un peu plus complexe que cela. Alors, commençons.

[Voici le programme déployé sur le réseau Vara](https://idea.gear-tech.io/programs/0x58acd467aa011554b0dc167f741e745b336a03943df6f1eba635e9c28ca9824e), et voici [le dépôt entier pour les 3 projets](https://github.com/rockyessel/freecodecamp-gear-protocol) que nous avons construits jusqu'à présent. Le prochain projet sera un projet autonome, donc vous n'utiliserez pas l'espace de travail.

## Projet final

Dans ce projet final, vous allez construire un jeu très simple : où vous (joueur) combattez contre le `boss`. Voici une explication simple des mécanismes du jeu.

### Description du jeu

Ce jeu est un combat un contre un entre un joueur et un boss. Pour commencer, le joueur sélectionne son personnage parmi trois options : Guerrier, Mage ou Archer. Une fois les données du personnage du joueur stockées dans le programme, le jeu commence.

Dans le jeu, le joueur affronte immédiatement le boss, qui commence avec 10 vies (représentées par un entier), tandis que le joueur commence avec 10 vies par défaut. L'objectif est de vaincre le boss en utilisant une règle spécifique : le boss a des faiblesses représentées par des lettres (X, Y, Z), chacune associée à un nombre aléatoire.

Pendant le jeu, si le joueur entre l'une de ces lettres, par exemple, 'Y' avec une valeur de 4, et que le boss commence avec 0 vie, le programme soustrait 4 vies au boss, laissant 6. De même, lorsque le joueur fait un mouvement avec une lettre, le boss fait également un mouvement avec une lettre aléatoire avec une valeur associée ajoutée à celle-ci.

Le joueur passe au niveau suivant après avoir vaincu le boss, continuant le combat avec de nouveaux défis. J'appelle ce jeu Battle Showdown **🤣😁😂.**

### **Battle Showdown** Résumé des mécanismes

#### Vies du joueur et du boss

* Le joueur commence avec 10 vies.
* Le boss commence avec 10 vies.

#### Faiblesses et valeurs

* Le boss et le joueur ont des faiblesses représentées par des lettres ( `X`, `Y`, `Z`), chacune associée à un nombre aléatoire.

#### Gameplay

* Le joueur entre une lettre (par exemple, `'Y'`) et la valeur associée (par exemple, `4`) est soustraite des vies du boss.
* Le boss riposte avec une lettre et la même valeur est soustraite des vies du joueur.
* L'objectif est que le joueur réduise les vies du boss à 0 pour passer au niveau suivant.

### Équation de match

Définissons les variables clés :

* (`Lp`) = Vies actuelles du joueur.
* (`Lb`) = Vies actuelles du boss.
* (`V`) = Valeur associée à la lettre représentant l'attaque.

**Conditions initiales :**

* ( `Lp` = 10 )
* ( `Lb` = 10 )

**Tour du joueur :**

* Le joueur sélectionne une lettre avec une valeur associée (`V`).
* Les vies du boss sont réduites : (`Lb` = `Lb` - `V`).

**Riposte du boss :**

* Le boss sélectionne une lettre (même valeur (`V`)).
* Les vies du joueur sont réduites : (`Lp` = `Lp` - `V`).

Cela continue jusqu'à ce que soit ( `Lb` ) (vies du boss) ou ( `Lp` ) (vies du joueur) atteigne 0.

### Équations

Après l'attaque du joueur et la riposte du boss :  
[`Lb` = `Lb` - `V`]  
[`Lp` = `Lp` - `V`]

La boucle de jeu continue avec le joueur et le boss échangeant des mouvements. Répéter jusqu'à ce que `Lb` `<= 0` ou `Lp` `<= 0`

### Exemple

Si le joueur entre `'Y'` avec une valeur de `4`:

* Initial : ( `Lp` = 10 ), ( `Lb` = 10 )
* Attaque du joueur : ( `Lb` = 10 - 4 = 6 )
* Riposte du boss : ( `Lp` = 10 - 4 = 6 )

Prochain mouvement :

* Si le joueur entre une autre valeur, disons : `'X'` avec une valeur de `5`:
* Attaque du joueur : ( `Lb` = 6 - 5 = 1 )
* Riposte du boss : ( `Lp` = 6 - 5 = 1 )

Le joueur gagne car les vies du boss ( `Lb` ) ont atteint 0.

L'équation de match pour chaque round du jeu peut être résumée comme suit :  
[`Lb` = `Lb` - `V`]  
[`Lp` = `Lp` - `V`]  
Ce processus est répété jusqu'à ce que soit les vies du joueur (( `Lp` )) ou les vies du boss (( `Lb` )) atteignent 0, déterminant le gagnant de la bataille.

### Erreur Windows

Si vous utilisez Windows, vous pouvez rencontrer une erreur avec le fichier **link.exe**. Honnêtement, je ne peux pas expliquer la raison derrière cette erreur, mais dans la documentation de Gear, il a été clairement indiqué que les utilisateurs de Windows pourraient rencontrer certains problèmes lors de la construction de leur projet.

Mais rassurez-vous, il existe une solution, et je vais vous guider à travers celle-ci. Veuillez donc suivre ces étapes attentivement afin de ne pas avoir à gérer des bugs en cours de route.

### Étape 1 - Installer WSL via l'invite de commandes

Ouvrez votre CLI avec des privilèges d'administrateur, et exécutez la commande suivante :

```bash
wsl --install
```

Après avoir exécuté la commande, exécutez la commande suivante pour lister d'autres versions de Linux.

```bash
wsl -l -o
```

Cette commande montre une liste d'autres distributions Linux, et vous pouvez en sélectionner une que vous avez utilisée auparavant. Si vous êtes nouveau dans les distributions Linux, je recommande de sélectionner `Ubuntu-22.04`.

Ce ne sont que des listes et sont en lecture seule. Pour sélectionner votre système, exécutez la commande suivante.

```bash
wsl --install -d {Distribtion Name here(Ubuntu-22.04)} 
```

Après avoir terminé l'installation, redémarrez votre PC. Attendez un peu que le terminal s'ouvre et vous demande vos détails tels que votre nom d'utilisateur et votre mot de passe. Si le terminal ne s'ouvre pas, allez dans votre menu Démarrer, et vous trouverez quelque chose de similaire à ceci dans votre menu `Démarrer`.

![Image](https://www.freecodecamp.org/news/content/images/2024/04/image-6.png)
_Ubuntu dans le menu démarrer_

Après cela, la prochaine chose à faire est d'installer Rust sur votre WSL.

### Comment installer Rust sur votre WSL

Pour installer Rust sur votre machine, je recommande que chaque fois que vous voulez installer un package, il est bon de mettre à jour et de mettre à niveau le système avant de continuer avec l'installation.

```bash
sudo apt update && sudo apt upgrade -y
```

Lorsque vous exécutez `sudo apt update && sudo apt upgrade -y`, vous mettez d'abord à jour les listes de packages pour obtenir les dernières informations sur les packages logiciels disponibles. Ensuite, si la mise à jour est réussie, elle procède à la mise à niveau des packages installés vers leurs dernières versions, en confirmant automatiquement les mises à niveau pour éviter une intervention manuelle. C'est une pratique courante et recommandée pour garder votre système Linux à jour et sécurisé.

### Dépendances essentielles.

La commande ci-dessous installe des outils de développement essentiels (`build-essential`, `gcc`, et `make`) et l'utilitaire `curl` pour effectuer des requêtes HTTP et télécharger des fichiers. Ces packages sont généralement requis pour les tâches de développement logiciel, de compilation et d'administration système.

```bash
 sudo apt install curl build-essential gcc make -y
```

Après cela, exécutez la commande dans le terminal

```bash
 curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

```

Dans le processus d'installation, vous serez invité à une question : choisissez le `default` lorsqu'elle se présente.

```bash
1. Proceed with installation (default) --> Enter
2. Customize installation
3. Cancel installation.


```

Après cette invite, vous avez installé Rust avec succès sur le système Ubuntu. Maintenant, l'étape suivante consiste à redémarrer votre terminal, il suffit de fermer le terminal actuel. Ouvrez-en un nouveau, et exécutez la commande ci-dessous.

```bash
source "$HOME/.cargo/env"

```

Ce que fait cette commande source `"$HOME/.cargo/env"` est d'activer l'environnement Rust. La raison est que l'environnement Rust comprend des variables et des configurations essentielles nécessaires pour une utilisation efficace de Rust. Maintenant, une fois exécuté, il n'y a pas de sortie, donc vous pouvez vérifier l'installation en exécutant la commande ci-dessous.

```bash
 rustc -V

```

Sortie attendue :

```bash
rockyessel@UBUNTU-ROCKY:~$ rustc -V rustc 1.73.0 (cc66ad468 2024-02-07)

```

Lorsque vous avez terminé, il y a aussi des dépendances supplémentaires que nous devons installer. Donc, voici, installez-les.

```bash
// Installer les éléments suivants.

 --> rustup toolchain add nightly-2023-09-18
 --> rustup target add wasm32-unknown-unknown --toolchain nightly-2023-09-18
```

Après avoir installé avec succès, passez à la section suivante, qui consiste à construire un projet de jeu.

Dans votre terminal WSL, créez votre projet nommé `battle-showdown`, et ajoutez tous les fichiers **toml** nécessaires, et les dépendances. Après cela, `cd` dans votre projet `battle-showdown` et ajoutez un autre programme appelé **io**, c'est là que vous écrivez votre métadonnée et d'autres types de données complexes ou simples pour votre dApp.

```bash
battle-showdown
.
├── Cargo.toml
├── io
│   ├── Cargo.toml
│   └── src
│       └── lib.rs
└── src
    └── lib.rs
```

Donc, rendez-vous dans votre fichier **./io/src/lib.rs** et collez le code suivant :

```bash
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = ();
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}

```

Ici, vous avez défini une nouvelle structure publique nommée `BattleShowdown`. Les structures sont utilisées pour créer des types de données personnalisés en regroupant des champs de divers types. Mais dans ce cas, vous fournissez une implémentation pour les types requis du trait `Metadata` pour la structure `BattleShowdown` : `impl Metadata for BattleShowdown`.

`type Init = ()`, `type Handle = ()`, `type State = ()`, `type Reply = ()`, `type Others = ()`, et `type Signal = ()` spécifient que les types de données des gestionnaires ou fonctions pour `BattleShowdown` sont de type `()`, qui dans le type unité de Rust, équivaut à `void` dans d'autres langages comme `TypeScript`.

Donc, pour l'instant, nous disons que ces gestionnaires n'envoient ni ne reçoivent de données en tant que telles. Par conséquent, le code spécifie simplement comment `BattleShowdown` interagit avec le système. Cependant, il est important de mentionner que la structure `BattleShowdown` elle-même n'a pas de données d'initialisation spécifiques, d'état, de comportement de gestion, de réponses, de signaux ou d'autres types associés définis.

### Construction de notre jeu

Tout d'abord, enregistrons le **io** dans votre répertoire parent **cargo.toml**. Donc, rendez-vous dans `./cargo.toml` et collez le code ci-dessous :

```toml
workspace = { members = ["io"] }
[package]
name = "battle-showdown"
version = "0.1.0"
edition = "2021"

[dependencies]
gstd = "1.4.1"
battle-showdown-io={path = "io"}



[build-dependencies]
gear-wasm-builder = "1.4.1"
battle-showdown-io={path = "io"}
```

J'ai veillé à ce que le chemin "battle-showdown-io" soit inclus dans les sections des dépendances et des build-dependencies. Cette décision était intentionnelle car lorsqu'il est ajouté uniquement aux build-dependencies, seules les structures, les énumérations et autres types de données ou fonctions au sein du fichier build.rs y ont accès, et non les dépendances dans votre fichier **`./src/lib.rs`**. Cela est important car j'utiliserai `battle-showdown-io` à la fois dans les build-dependencies (`build.rs`) et les dépendances (`./src/lib.rs`).

Cette étape est cruciale car l'ignorer peut entraîner des erreurs d'importation frustrantes.

Ensuite, le fichier **`./io/cargo.toml`**, collez le code suivant ci-dessous.

```toml
[package]
name = "battle-showdown-io"
version = "0.1.0"
edition = "2021"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
gstd = "1.4.1"
gmeta = "1.4.1"
parity-scale-codec = { version = "3.6.12", default-features = false }
scale-info = { version = "2.11.3", default-features = false }
```

### Explication des métadonnées pour BattleShown

Il est crucial de prêter une attention particulière à cette section, car je vais éclairer davantage l'explication des types de métadonnées pour `BattleShown` et son déploiement sur le réseau Vara.

```rust
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = ();
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}
```

### Définition de l'initialisation – `Init`

Pour définir les types à cette fin, considérez si votre programme ou contrat intelligent doit stocker des données ou effectuer des actions avant que l'utilisateur puisse interagir avec lui. Dans le cas de ce jeu, la réponse est oui. 

Le jeu suppose qu'une seule personne joue et ne permet pas aux utilisateurs de créer leurs personnages ou joueurs. Cela signifie que vous devez stocker des données avant de pouvoir utiliser ce programme, et dans ce scénario, nous avons besoin d'informations sur la personne/développeur/acteur/utilisateur déployant le contrat ou le programme, qui est vous.

Voici les informations que vous souhaitez stocker :

* **playerId - Type : ActorId**  
L'ID du joueur est en fait l'adresse associée à votre compte, qui est de type `ActorId`.
* **playerName - Type : String**  
Cela est de type chaîne, assez simple.
* **playerCharacterType - Type : Enum**  
Le `playerCharacterType` est une énumération qui donne à l'acteur une option pour sélectionner le type qu'il souhaite être, avec des options incluant Mage, Warrior et Archer.

```rust
#![no_std]

use gmeta::Metadata;

pub struct BattleShowdown;

impl Metadata for BattleShowdown {
    type Init = InOut<InitBattleShowdown, String>;
    type Handle = ();
    type State = ();
    type Reply = ();
    type Others = ();
    type Signal = ();
}

#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum CharacterType {
    Warrior,
    Mage,
    Archer,
}


#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct InitBattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub player_name: String,
}
```

Bien que j'aie déjà discuté des métadonnées, vous pourriez être curieux de savoir ce que signifie `type Init = InOut<InitBattleShowdown, String>;` Eh bien, ce n'est rien de complexe. Ici, nous disons simplement que le gestionnaire `init` acceptera un type de données `InitBattleShowdown` et répondra avec un type de données `String`.

Avant de continuer, une étape supplémentaire reste : implémenter un `default trait` pour l'énumération `CharacterType`. Cela garantit que si le `CharacterType` n'est pas explicitement défini, il est par défaut `Warrior`. Il suffit d'ajouter le code suivant au code existant ci-dessus :

```rust
impl Default for CharacterType {
    fn default() -> Self {
        CharacterType::Warrior
    }
}
```

### Définition du `Handle`

Définir un type pour la fonction `handle` est similaire au processus pour la fonction `init`, mais l'implémentation réelle est laissée au développeur, qui dans ce cas, est vous. Après avoir examiné le code et expérimenté différentes approches, j'ai découvert une méthode utilisée par le protocole Gear (qui partage des similitudes avec certains de leurs projets) qui avait plus de sens.

### Action & Événement

Dans leur implémentation, ils ont utilisé des Actions et des Événements. Les Actions représentent un ensemble d'opérations que le programme peut effectuer, tandis que les Événements sont les résultats de ces Actions.

Par exemple, dans le contexte de ce jeu, vous pourriez avoir une action nommée `Attack` avec un Événement correspondant nommé `Attacked`. Ceux-ci pourraient potentiellement accepter des paramètres et retourner des résultats.

Par conséquent, pour définir le type de gestion, incluez le code suivant dans votre base de code existante :

```rust

#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownAction {
    Attack {
        character_hit_power_value: PlayerHitPowerValue,
    },
}
```

Précédemment, lors de la description des mécanismes du jeu, j'ai introduit une mécanique impliquant une lettre avec un nombre assigné aléatoirement pour injecter un élément d'aléatoire. Dans ce contexte, ces lettres correspondent à un état `ENUM` de `X`, `Z`, et `Y`.

Par conséquent, pour implémenter cette mécanique, ajoutez le code suivant :

```rust
...

#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum PlayerHitPowerValue {
    X,
    Y,
    Z,
}
```

Lorsque qu'un acteur ou un utilisateur décide d'attaquer le boss, il peut choisir parmi les options fournies ci-dessus, chacune avec une valeur aléatoire. Par conséquent, chaque attaque sur le boss donnera des résultats différents en raison de la variabilité de ces valeurs. De la même manière que vous avez implémenté un trait par défaut pour le `CharacterType`, vous devriez faire de même ici.

```rust
impl Default for PlayerHitPowerValue {
    fn default() -> Self {
        PlayerHitPowerValue::X
    }
}
```

### Événement

Comme mentionné précédemment, les événements sont les résultats des actions. Contrairement à `BattleShowdownAction`, qui n'avait qu'une seule action, `BattleShowdownEvent` englobera plus de deux actions. Pourquoi ? Parce que la logique du jeu dicte que lorsque l'utilisateur attaque, le boss contre-attaque également. Cela entraîne trois résultats possibles : soit l'utilisateur perd, le boss est vaincu, ou le combat continue. 

Cependant, le troisième résultat dépend des deux premiers résultats.  
Par conséquent, pour `BattleShowdownEvent`, vous devrez définir :

```rust
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownEvent {
    Attacked {
        id: ActorId,
        character_type: CharacterType,
        name: String,
        player_lives: u32,
        boss_livesL: u32,
    },

    PlayerLost {
        id: ActorId,
        character_type: CharacterType,
        boss_livesL: u32,
        player_lives: u32,
        message: String,
    },

    BossLost {
        character_type: CharacterType,
        player_lives: u32,
        boss_livesL: u32,
        message: String,
    },
}

```

Vous avez une action, mais il y a trois événements possibles, n'est-ce pas ? Lorsque l'utilisateur/acteur attaque le boss et que le boss contre-attaque, si l'un d'eux est vaincu, l'événement "Attacked" est retourné. Cependant, si le joueur réussit à vaincre le boss, l'événement "BossLost" est retourné. 
Maintenant que vous avez une bonne compréhension, intégrons les types d'entrée et de sortie pour la fonction Handle : `type Handle = InOut<BattleShowdownAction, BattleShowdownEvent>;`.

### Définition de `State`

Comme mentionné précédemment, l'état stocke des informations au sein de votre programme. Pour `BattleShowdown`, l'état que vous souhaiteriez stocker inclut des informations sur le joueur, le boss et le niveau actuel.

```rust
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct BattleShowdownState {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
}
```

Par conséquent, chaque fois que vous appelez la fonction state, vous devriez vous attendre à voir le résultat dans ce format. Maintenant, ajoutez `BattleShowdownState` à l'état dans les métadonnées, comme ceci : `type State = Out<BattleShowdownState>;`.

Avec cela, la configuration est complète. Voici le code complet pour le fichier **./io/src/lib.rs**.

```rust
#![no_std]

use gmeta::{In, InOut, Metadata, Out};
use gstd::{prelude::*, ActorId};

// Définir la structure principale pour BattleShowdown
pub struct BattleShowdown;

// Implémentation des métadonnées pour BattleShowdown
impl Metadata for BattleShowdown {
    // Définir le type pour les messages d'initialisation
    type Init = InOut<InitBattleShowdown, String>;
    // Définir le type pour les messages de gestion
    type Handle = InOut<BattleShowdownAction, BattleShowdownEvent>;
    // Définir le type pour les messages d'état
    type State = Out<BattleShowdownState>;
    type Reply = ();
    type Others = ();
    type Signal = ();
}

// Structure pour l'initialisation de BattleShowdown
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct InitBattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub player_name: String,
}

// Structure représentant l'état de BattleShowdown
#[derive(Default, Debug, Encode, Decode, TypeInfo)]
pub struct BattleShowdownState {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
}

// Enum représentant différents types de personnages
#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum CharacterType {
    Warrior,
    Mage,
    Archer,
}

// Enum représentant différentes valeurs pour la puissance de frappe du joueur
#[derive(Debug, Clone, Copy, Encode, Decode, TypeInfo)]
pub enum PlayerHitPowerValue {
    X,
    Y,
    Z,
}

// Implémentation de Default pour PlayerHitPowerValue
impl Default for PlayerHitPowerValue {
    fn default() -> Self {
        PlayerHitPowerValue::X
    }
}

// Implémentation de Default pour CharacterType
impl Default for CharacterType {
    fn default() -> Self {
        CharacterType::Warrior
    }
}

// Enum représentant différentes actions dans BattleShowdown
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownAction {
    Attack {
        character_hit_power_value: PlayerHitPowerValue,
    },
}

// Enum représentant différents événements dans BattleShowdown
#[derive(Debug, Encode, Decode, TypeInfo)]
pub enum BattleShowdownEvent {
    Attacked {
        id: ActorId,
        character_type: CharacterType,
        name: String,
        player_lives: u32,
        boss_lives: u32,
    },
    PlayerLost {
        id: ActorId,
        character_type: CharacterType,
        boss_lives: u32,
        player_lives: u32,
        message: String,
    },
    BossLost {
        character_type: CharacterType,
        player_lives: u32,
        boss_lives: u32,
        message: String,
    },
}

```

### `Build.rs`

Importez `BattleShowdown` dans le fichier **build.rs** depuis votre répertoire parent à **./src/build.rs**. Si vous rencontrez une erreur d'importation, assurez-vous que dans votre fichier **./cargo.toml**, vous enregistrez `battle-showdown-io={path = "io"}`.

```rust
use battle_showdown_io::BattleShowdown;

fn main() {
    gear_wasm_builder::build_with_metadata::<BattleShowdown>();
}
```

C'est tout pour le fichier **build.rs**, et ce qu'il fait est de construire votre projet en `wasm` puis de construire les `metadata` pour `BattleShown` pour vous.

### Implémentation de la logique du jeu - `./src/lib.rs`

Pour cette section, je vais écrire le code ci-dessous, puis je vais l'expliquer au fur et à mesure. Il y aura un problème que je vais vous demander de résoudre, qui concernera l'état.

```rust
#![no_std]

use gstd::{exec, msg, prelude::*, ActorId};

use battle_showdown_io::*;

// Fonction pour générer un nombre aléatoire entre 1 et 3
fn get_random_u32() -> u32 {
    let salt = msg::id();
    let (hash, _num) = exec::random(salt.into()).expect("get_random_u32(): random call failed");
    (u32::from_le_bytes([hash[0], hash[1], hash[2], hash[3]]) % 3) + 1 // Génère un nombre aléatoire entre 1 et 3
}

#[derive(Debug, Default)]
pub struct BattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub character_hit_power_value: PlayerHitPowerValue,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
    pub game_state: String,
}

static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;

#[no_mangle]
unsafe extern "C" fn init() {
    let init: InitBattleShowdown = msg::load().expect("Unable to decode InitBattleShowdown");

    let battle_showdown = BattleShowdown {
        player_id: msg::source(),
        player_character_type: init.player_character_type,
        player_name: init.player_name,
        boss_lives: 10,
        player_lives: 10,
        ..Default::default()
    };

    BATTLESHOWNDOWN = Some(battle_showdown);

    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}

impl Encode for BattleShowdown {
    fn encode(&self) -> Vec<u8> {
        let mut encoded = Vec::new();

        // Encoder chaque champ de la structure BattleShowdown
        encoded.extend_from_slice(&self.player_id.encode());
        encoded.extend_from_slice(&self.player_character_type.encode());
        encoded.extend_from_slice(&self.current_level.encode());
        encoded.extend_from_slice(&self.player_lives.encode());
        encoded.extend_from_slice(&self.player_name.encode());
        encoded.extend_from_slice(&self.boss_lives.encode());
        encoded.extend_from_slice(&self.character_hit_power_value.encode());
        encoded.extend_from_slice(&self.player_hit_power.encode());
        encoded.extend_from_slice(&self.boss_hit_power.encode());
        encoded.extend_from_slice(&self.game_state.encode());

        encoded
    }
}

impl BattleShowdown {
    // Placeholder pour la méthode `attack`
    fn attack(&mut self, _character_hit_power_value: PlayerHitPowerValue) -> BattleShowdownEvent {
        // Implémenter cette méthode selon la logique de votre jeu
        // Pour l'instant, retourne simplement un événement vide

        // Calculer la puissance de frappe totale pour le joueur en fonction du type de personnage et des valeurs aléatoires
        let character_hit_power = match &self.player_character_type {
            CharacterType::Warrior => 4,
            CharacterType::Mage => 3,
            CharacterType::Archer => 2,
        };

        let player_hit_power = match &self.character_hit_power_value {
            PlayerHitPowerValue::X => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Y => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Z => character_hit_power + get_random_u32(),
        };

        // Placeholder pour la logique d'attaque du boss
        // Mettre à jour la puissance de frappe du boss à une valeur aléatoire pour chaque attaque
        self.boss_hit_power = get_random_u32();

        self.player_hit_power = player_hit_power;

        // Réduire les vies du boss en fonction de la puissance de frappe du joueur
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Réduire les vies du joueur en fonction de la puissance de frappe du boss
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);

        // Vérifier si le joueur ou le boss a perdu
        if self.player_lives == 0 {
            // Le joueur a perdu
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Le boss a perdu
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boos".to_string(),
            };
        }

        self.game_state = "The games continues.".to_string();
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
    }
}

#[no_mangle]
extern "C" fn handle() {
    let battle_showdown_action: BattleShowdownAction =
        msg::load().expect("Could not load BattleShowdownAction");
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .as_mut()
            .expect("`BattleShowdown` is not initialized.")
    };
    let result: BattleShowdownEvent = match battle_showdown_action {
        BattleShowdownAction::Attack {
            character_hit_power_value,
        } => battle_showdown.attack(character_hit_power_value),
    };
    msg::reply_bytes(result.encode(), 0)
        .expect("Failed to encode or reply with `BattleShowdownEvent`.");
}

#[no_mangle]
extern "C" fn state() {
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .take()
            .expect("Unexpected error in taking state")
    };

    msg::reply(battle_showdown, 0).expect("Unable to share the state");
}

```

À première vue, cela peut sembler beaucoup, mais ce n'est pas le cas, alors ne vous laissez pas trop intimider. Avant de commencer, assurez-vous de comprendre toute la logique de la description du jeu que j'ai donnée plus tôt, car vous allez l'implémenter ici.

Ci-dessus, nous avons quelques fonctions importantes, `struct`, et `impl`, et voici un aperçu de ce qu'elles font.

1. Avec la fonction `get_random_u32`, nous avons généré un nombre aléatoire entre 1 et 3.
2. La `struct` `BattleShowdown` dans le fichier `/src/lib.rs` représente l'état principal du jeu. Elle contient des informations telles que les statistiques du joueur et du boss, le niveau actuel du jeu et l'état du jeu. La variable `static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;` est une variable statique mutable qui contient l'état actuel du jeu. Elle est enveloppée dans une `Option` pour indiquer si le jeu a été initialisé ou non, ce que vous utiliserez plus tard dans votre implémentation.
3. `unsafe extern "C" fn init()` est responsable de l'initialisation de l'état du jeu lorsqu'il est appelé après le téléchargement du contrat. Il charge un message d'initialisation, construit une instance `BattleShowdown` basée sur ce message, et définit `BATTLESHOWNDOWN` sur `Some` avec l'instance construite.
4. `impl Encode for BattleShowdown` : ce trait est implémenté pour `BattleShowdown`, lui permettant d'être encodé en une représentation binaire. Cela est utile pour la sérialisation et l'envoi de l'état du jeu sur le réseau. Et il existe un moyen d'implémenter également le trait sans créer un `impl` pour `BattleShowdown`.
5. `impl BattleShowdown` : cette `impl` pour `BattleShowdown` est l'endroit où toute la logique se déroule, et pour l'instant, nous n'avons ajouté qu'une méthode `attack`. Il est important de noter que nous en ajouterons davantage au fur et à mesure de ce projet.
6. Alors, que fait la méthode `attack` ? Eh bien, la méthode `attack` simule une rencontre de combat entre le personnage du joueur et le boss dans notre jeu. Elle calcule la puissance de frappe pour les deux entités en fonction du type de personnage et de l'aléatoire, gère leurs points de vie en conséquence et génère des événements de jeu pour refléter le résultat de la rencontre.
7. `extern "C" fn handle()` : Dans notre cas, la fonction `handle` est utilisée pour traiter les messages entrants, spécifiquement `BattleShowdownAction`. Donc, en fonction de l'action effectuée par l'acteur, elle envoie un résultat de l'action aux méthodes appropriées de `BattleShowdown`, comme `attack`, et renvoie les événements de jeu résultants à l'acteur. Comme discuté dans l'illustration.
8. Et enfin, `extern "C" fn state()` récupère simplement l'état actuel du jeu représenté par `BattleShowdown` et l'envoie en réponse.

C'est l'explication générale du code dans le fichier. Mais partir avec cela n'est pas suffisant même pour moi. Discutons-en davantage ci-dessous.

### Comprendre le `init()`

```rust
#[derive(Debug, Default)]
pub struct BattleShowdown {
    pub player_id: ActorId,
    pub player_character_type: CharacterType,
    pub current_level: u32,
    pub player_lives: u32,
    pub player_name: String,
    pub boss_lives: u32,
    pub character_hit_power_value: PlayerHitPowerValue,
    pub player_hit_power: u32,
    pub boss_hit_power: u32,
    pub game_state: String,
}

static mut BATTLESHOWNDOWN: Option<BattleShowdown> = None;

#[no_mangle]
unsafe extern "C" fn init() {
    // Charger les données d'initialisation
    let init: InitBattleShowdown = msg::load().expect("Unable to decode InitBattleShowdown");

    // Créer une instance BattleShowdown avec des valeurs initiales
    let battle_showdown = BattleShowdown {
        player_id: msg::source(),
        player_character_type: init.player_character_type,
        player_name: init.player_name,
        boss_lives: 10,
        player_lives: 10,
        ..Default::default()
    };

    // Stocker l'instance BattleShowdown
    BATTLESHOWNDOWN = Some(battle_showdown);

    // Répondre pour signaler une initialisation réussie
    msg::reply_bytes("Successfully initialized", 0).expect("Failed to initialize successfully.");
}
```

La fonction charge les données d'un message d'initialisation (`InitBattleShowdown`) envoyé par le développeur ou le joueur. Ces données incluent le type de personnage choisi par le joueur et son nom. Sur la base des données d'initialisation, une instance `BattleShowdown` est créée avec des valeurs initiales, qui est stockée dans `battle_showdown`. 

Cette instance représente l'état du jeu, y compris les statistiques du joueur et du boss, le niveau actuel et l'état du jeu. L'instance `BattleShowdown` créée est stockée dans la variable statique `BATTLESHOWNDOWN`, permettant à la logique du jeu d'accéder et de manipuler l'état du jeu tout au long de la partie. Enfin, un message de réponse est envoyé au développeur ou au joueur pour indiquer une initialisation réussie du contrat de jeu. 

Cette fonction configure l'état initial du jeu, ouvrant la voie à des interactions et une logique de jeu ultérieures.

### Comprendre le `handle()`

```rust
#[no_mangle]
extern "C" fn handle() {
    // Charger l'action à partir du message
    let battle_showdown_action: BattleShowdownAction =
        msg::load().expect("Could not load BattleShowdownAction");

    // Récupérer l'état actuel du jeu
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .as_mut()
            .expect("`BattleShowdown` is not initialized.")
    };

    // Exécuter l'action appropriée sur l'état du jeu et obtenir le résultat
    let result: BattleShowdownEvent = match battle_showdown_action {
        BattleShowdownAction::Attack {
            character_hit_power_value,
        } => battle_showdown.attack(character_hit_power_value),
    };

    // Envoyer le résultat en tant que message de réponse
    msg::reply_bytes(result.encode(), 0)
        .expect("Failed to encode or reply with `BattleShowdownEvent`.");
}
```

La fonction `handle()` joue un rôle crucial dans le traitement des messages entrants et l'orchestration des actions du jeu. Elle sert de pont entre les interactions du joueur et la logique interne du jeu. Lorsqu'elle est invoquée, `handle()` commence par charger l'`action` envoyée par le joueur à partir du message. 

Cette `action`, encapsulée en tant que `BattleShowdownAction`, dicte le mouvement prévu du joueur, tel qu'attaquer le boss. Ensuite, la fonction récupère l'état actuel du jeu à partir de la variable `BATTLESHOWNDOWN`. Cet état contient des informations essentielles sur le joueur, le boss et l'environnement de jeu global. 

Avec à la fois l'action et l'état du jeu en main, `handle()` procède à l'exécution de l'action appropriée. Par exemple, si l'action du joueur est une `attaque`, la fonction déclenche la méthode `attack()` sur l'instance `battle_showdown`. Cette méthode calcule le résultat de l'attaque du joueur, en tenant compte de facteurs tels que la puissance de frappe du joueur et les points de vie restants du boss.

Il est crucial de noter que la méthode `attack()` nécessite un paramètre : `character_hit_power_value`. Ce paramètre correspond au choix du joueur entre trois options : `X`, `Y` et `Z`, chacune associée à différentes valeurs de puissance de frappe comme discuté dans les sections précédentes. 

Une fois l'`action` exécutée, `handle()` génère un événement, encapsulé en tant que `BattleShowdownEvent`, reflétant le résultat du mouvement du joueur. Cet événement encapsule des détails importants, tels que les changements dans les points de vie du joueur et du boss. Enfin, `handle()` répond au joueur en renvoyant le résultat de l'action sous forme de message encodé en bytes. Ce message contient l'état du jeu mis à jour, permettant au joueur de comprendre sa situation actuelle, y compris son état de santé et celui du boss.

### Comprendre le `impl BattleShowdown pour attack`

```rust
impl BattleShowdown {
    fn attack(&mut self, _character_hit_power_value: PlayerHitPowerValue) -> BattleShowdownEvent {
        // Calculer la puissance de frappe totale pour le joueur en fonction du type de personnage et des valeurs aléatoires
        let character_hit_power = match &self.player_character_type {
            CharacterType::Warrior => 4,
            CharacterType::Mage => 3,
            CharacterType::Archer => 2,
        };

        let player_hit_power = match &self.character_hit_power_value {
            PlayerHitPowerValue::X => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Y => character_hit_power + get_random_u32(),
            PlayerHitPowerValue::Z => character_hit_power + get_random_u32(),
        };

        // Placeholder pour la logique d'attaque du boss
        // Mettre à jour la puissance de frappe du boss à une valeur aléatoire pour chaque attaque
        self.boss_hit_power = get_random_u32();

        self.player_hit_power = player_hit_power;

        // Réduire les vies du boss en fonction de la puissance de frappe du joueur
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Réduire les vies du joueur en fonction de la puissance de frappe du boss
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);

        // Vérifier si le joueur ou le boss a perdu
        if self.player_lives == 0 {
            // Le joueur a perdu
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Le boss a perdu
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boss".to_string(),
            };
        }

        self.game_state = "The game continues.".to_string();
        // Retourner l'événement indiquant qu'une attaque a eu lieu
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
    }
}
```

La méthode `attack` au sein de l'implémentation de `BattleShowdown` simule un moment crucial du jeu : une rencontre de combat entre le personnage du joueur et le boss.

Voici comment cela fonctionne :

Tout d'abord, la méthode calcule la puissance de frappe totale pour le joueur en fonction de son type de personnage (`character_hit_power`) et de l'aléatoire (`player_hit_power`). Différents types de personnages (`Warrior`, `Mage` ou `Archer`) ont différentes puissances de frappe de base. 

Ensuite, une valeur de puissance de frappe aléatoire est ajoutée à la puissance de frappe de base du personnage. Cela ajoute un élément d'imprévisibilité à chaque attaque. La méthode met ensuite à jour la puissance de frappe du boss (`self.boss_hit_power = get_random_u32();`) à une valeur aléatoire, représentant la frappe de représailles du boss contre le joueur.

Après avoir calculé les puissances de frappe, la méthode réduit les vies du boss en fonction de la puissance de frappe du joueur et vice versa, mettant à jour leurs points de vie respectifs en conséquence.

```rust
        // Réduire les vies du boss en fonction de la puissance de frappe du joueur
        self.boss_lives = self.boss_lives.saturating_sub(self.player_hit_power);
        // Réduire les vies du joueur en fonction de la puissance de frappe du boss
        self.player_lives = self.player_lives.saturating_sub(self.boss_hit_power);
```

L'état du jeu est ensuite vérifié pour déterminer si le joueur ou le boss a perdu la bataille. Si les points de vie du joueur atteignent zéro, l'état du jeu est mis à jour pour indiquer que le joueur a perdu. Inversement, si les points de vie du boss atteignent zéro, l'état du jeu reflète la défaite du boss.

```rust
        // Vérifier si le joueur ou le boss a perdu
        if self.player_lives == 0 {
            // Le joueur a perdu
            self.game_state = "Player lost.".to_string();
            return BattleShowdownEvent::PlayerLost {
                id: self.player_id,
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                message: "".to_string(),
                player_lives: self.player_lives,
            };
        } else if self.boss_lives == 0 {
            // Le boss a perdu
            self.game_state = "Boss lost.".to_string();
            return BattleShowdownEvent::BossLost {
                boss_lives: self.boss_lives,
                character_type: self.player_character_type,
                player_lives: self.player_lives,
                message: "You've defeated the boss".to_string(),
            };
        }

        self.game_state = "The game continues.".to_string();
        // Retourner l'événement indiquant qu'une attaque a eu lieu
        BattleShowdownEvent::Attacked {
            boss_lives: self.boss_lives,
            character_type: self.player_character_type,
            id: self.player_id,
            name: self.player_name.clone(),
            player_lives: self.player_lives,
        }
```

Enfin, si ni le joueur ni le boss n'a perdu, l'état du jeu est mis à jour pour indiquer que la bataille continue.

### Comprendre le `State()`

```rust
#[no_mangle]
extern "C" fn state() {
    let battle_showdown = unsafe {
        BATTLESHOWNDOWN
            .take()
            .expect("Unexpected error in taking state")
    };

    msg::reply(battle_showdown, 0).expect("Unable to share the state");
}
```

Pour cette instance, il n'y a rien de plus à partager, elle récupère l'état actuel du jeu, représenté par la structure `BattleShowdown`, à partir d'une variable statique mutable `BATTLESHOWNDOWN`, et envoie un message de réponse contenant l'état du jeu à l'utilisateur. Si une erreur survient lors de l'envoi du message de réponse, elle paniquera avec un message d'erreur indiquant l'incapacité à partager l'état.

Et c'est tout pour ce projet. Il existe certaines fonctionnalités passionnantes que vous pouvez envisager si vous souhaitez étendre ce projet. Imaginez la possibilité de réinitialiser l'état du jeu, d'accueillir plusieurs joueurs, ou même de réinitialiser le jeu pour un seul joueur. Et pour les plus ambitieux, vous pourriez même relever le défi de réinitialiser l'état pour l'ensemble du jeu. Ces ajouts peuvent offrir de nouvelles dimensions au projet et fournir d'excellentes opportunités pour vous défier.

### Court enregistrement de ce que nous avons construit - Démo

%[https://www.loom.com/share/590d685f311f46c386943c41816dbf83?sid=e99d4948-f0ab-486d-a5fa-98fbcdfe3fe3]

Dans la vidéo, vous pouvez voir que j'ai ajouté une autre méthode pour tout réinitialiser à son état initial. Bien que je ne vous aie pas guidé à travers le processus de le faire, vous devez savoir que c'est facile à implémenter, et j'ai ajouté [un dépôt GitHub](https://github.com/rockyessel/battle-showdown) pour le code complet.

### Conclusion

Comme démontré, le développement d'un contrat intelligent avec le protocole Gear devient simple une fois que vous maîtrisez les concepts de communication par messages. En suivant les étapes décrites, vous pouvez commencer à construire vos propres projets en toute confiance.

Bien que cet article n'ait pas abordé la gestion des transactions telles que les transferts de jetons, le minting ou les NFT, je couvrirai ces sujets dans un futur article.

Pour l'instant, vous pouvez explorer le dépôt du projet que nous avons construit ensemble : [Battle-Showdown](https://github.com/rockyessel/battle-showdown), et si vous avez des questions à poser, n'hésitez pas à contacter @rockyessel sur X.