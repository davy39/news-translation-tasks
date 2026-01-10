---
title: Qu'est-ce que les pointeurs intelligents en Rust ? Explications avec des exemples
  de code
subtitle: ''
author: Oduah Chigozie
co_authors: []
series: null
date: '2024-10-30T03:57:44.416Z'
originalURL: https://freecodecamp.org/news/smart-pointers-in-rust-with-code-examples
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730260779440/3d82425c-fdff-4a17-bb88-8193d964e6ba.jpeg
tags:
- name: Rust
  slug: rust
seo_title: Qu'est-ce que les pointeurs intelligents en Rust ? Explications avec des
  exemples de code
seo_desc: 'Smart pointers are data structures that act like pointers but contain extra
  information and have functionalities that make them excel over regular pointers
  in certain situations.

  So what are regular pointers? Regular pointers (just called “pointers”)...'
---

Les pointeurs intelligents sont des structures de données qui agissent comme des pointeurs mais contiennent des informations supplémentaires et possèdent des fonctionnalités qui les rendent supérieurs aux pointeurs réguliers dans certaines situations.

Alors, qu'est-ce que les pointeurs réguliers ? Les pointeurs réguliers (simplement appelés « pointeurs ») sont des variables qui contiennent des adresses mémoire comme valeurs. Ils permettent aux programmes de stocker, lire et écrire des données dans des emplacements mémoire avec leurs adresses.

Voici un diagramme pour donner une idée de ce qu'ils sont :

![Diagramme montrant un tableau de variables et d'adresses mémoire. "Text" et "Name" sont des pointeurs qui contiennent les adresses 0x80012 et 0x80018 respectivement](https://cdn.hashnode.com/res/hashnode/image/upload/v1730198558597/cd21ca42-32bb-4b41-98d3-b30956a6a398.png align="center")

Dans des langages de programmation comme C, C++ et Rust, les pointeurs sont utiles pour accéder à la mémoire allouée manuellement, mais ils présentent ces limitations :

* L'adresse mémoire qu'un pointeur contient peut être désallouée alors que le pointeur y fait toujours référence, ce qui en fait un pointeur pendouillant.

* Le pointeur n'aide pas à gérer l'allocation de mémoire, ce qui peut provoquer des fuites de mémoire ou d'autres types de bugs mémoire dans les cas où la gestion des allocations de mémoire est complexe.

Rust ne donne pas le même niveau de contrôle des pointeurs que C et C++. Cependant, comme C++, Rust fournit des pointeurs intelligents qui surmontent les limitations des pointeurs réguliers tout en offrant des fonctionnalités supplémentaires.

En Rust, il existe quatre principaux types de pointeurs intelligents : `Box`, `Rc`, `Arc` et `Weak`. Je vais les discuter dans cet article. Je vais également aborder un peu `RefCell`, car il ajoute une fonctionnalité spécifique qui manque dans les autres pointeurs intelligents.

## Table des matières

* [Pointeurs Box](#heading-box-pointers)

* [Pointeurs Rc et Arc](#heading-rc-and-arc-pointers)

* [Pointeurs Weak](#heading-weak-pointers)

* [RefCell](#heading-refcell)

* [Résumé](#heading-resume)

## Pointeurs `Box`

`Box` est le type de pointeur intelligent le plus simple. Il vous permet d'allouer manuellement de la mémoire dans le tas.

```rust
#[allow(dead_code)]
#[derive(Debug)]
struct Point {
    x: f32,
    y: f32,
}

fn main() {
    let point = Box::new(Point { x: 0.0, y: 0.0 });
    println!("{:?}", point);
}
```

Vous pouvez accéder au contenu d'un pointeur `Box` comme vous le feriez avec une variable régulière :

```rust
println!("{}", point.x); // -> sortie : 0.0
println!("{}", point.y); // -> sortie : 0.0
```

Cela fonctionne presque identiquement à `malloc` en C et `new` en C++, à l'exception que `Box` est automatiquement libéré lorsqu'il sort de portée, ou lorsque l'exécution du programme se termine, contrairement à la libération manuelle de l'allocation dans `malloc` et `new`.

## Pointeurs `Rc` et `Arc`

Je mets `Rc` et `Arc` ensemble car ils sont très similaires dans ce qu'ils font et dans leur fonctionnement.

`Rc` et `Arc` sont des pointeurs à comptage de références qui permettent une propriété multiple d'une allocation mémoire. Similaires à `Box`, ils allouent de la mémoire dans le tas, mais ce qui les différencie de `Box` est qu'ils incluent également un comptage de références.

`Rc` et `Arc` vous permettent de créer plusieurs clones d'une référence à une allocation mémoire. Cela vous permet de déplacer ces références vers plusieurs portées, et dans le cas de `Arc`, plusieurs threads, sans emprunt. Par exemple :

```rust
use std::sync::Arc;
use std::thread;
use std::thread::JoinHandle;

struct GameState {
    user_name: String,
}

impl GameState {
    fn new() -> Self {
        GameState { user_name: "Chigozie".to_string() }
    }
}

fn main() {
    let mut threads: Vec<JoinHandle<()>> = vec![];
    let game_state = Arc::new( GameState::new() );

    let g1 = Arc::clone(&game_state); // premier clone
    threads.push(thread::spawn(move || {
        let username = &g1.user_name;
        // ...
    }));

    let g2 = Arc::clone(&game_state); // deuxième clone
    threads.push(thread::spawn(move || {
        let username = &g2.user_name;
        // ...
    }));

    let g3 = Arc::clone(&game_state); // troisième clone
    threads.push(thread::spawn(move || {
        let username = &g3.user_name;
        // ...
    }));

    let g4 = Arc::clone(&game_state); // quatrième clone
    threads.push(thread::spawn(move || {
        let username = &g4.user_name;
        // ...
    }));

    let g5 = Arc::clone(&game_state); // cinquième clone
    threads.push(thread::spawn(move || {
        let username = &g5.user_name;
        // ...
    }));

    for th in threads {
        th.join().unwrap();
    }
}
```

Dans cet exemple, j'ai créé une instance d'une structure de jeu dans une structure de données `Arc`, j'ai lancé cinq threads, puis j'ai créé et passé cinq autres références `Arc` de la structure de jeu aux cinq threads lancés.

La différence entre les pointeurs `Rc` et `Arc` est que les références dans les pointeurs `Arc` sont comptées de manière atomique, tandis que les références dans les pointeurs `Rc` sont comptées en utilisant les opérations mathématiques habituelles. Cela signifie que les opérations qui entrent dans le comptage des références dans les pointeurs `Arc` sont garanties de ne pas être interrompues ou chevauchées par d'autres threads ou processus, ce qui les rend très utiles pour les environnements multithreads.

Une application utile des pointeurs `Rc` et `Arc` est dans les structures de données basées sur des références, comme les listes chaînées, où chaque nœud a sa valeur et une référence au nœud suivant. Par exemple :

```rust
use std::rc::Rc;

#[derive(Debug)]
struct Node {
    value: i32,
    next: Option<Rc<Node>>,
}

fn main() {
    // Une chaîne de nœuds
    let node1 = Rc::new(Node { value: 1, next: None });
    let node2 = Rc::new(Node { value: 2, next: Some(Rc::clone(&node1)) });
    let node3 = Rc::new(Node { value: 3, next: Some(Rc::clone(&node2)) });

    // Plusieurs propriétaires de node2
    let another_ref_to_node2 = Rc::clone(&node2);

    println!("Node 3: {:?}", node3);
    println!("Another reference to Node 2: {:?}", another_ref_to_node2);
}
```

Les allocations mémoire pointées par les références `Rc` et `Arc` sont supprimées lorsque leur comptage de références atteint 0. Le comptage de références des pointeurs `Rc` et `Arc` atteint 0 lorsqu'ils et tous leurs clones sont sortis de portée, ou ont été supprimés manuellement.

## Pointeurs `Weak`

Contrairement aux pointeurs `Arc` ou `Rc`, les pointeurs `Weak` sont des références non propriétaires aux allocations mémoire. Cela signifie qu'ils ne comptent pas pour la propriété de l'allocation mémoire et n'empêchent pas les allocations mémoire d'être supprimées.

Les références `Weak` sont utiles dans les scénarios où vous pourriez préférer une référence à une allocation mémoire pour l'empêcher d'être désallouée. Un bon exemple de scénario comme celui-ci est une liste doublement chaînée, où chaque nœud contient une référence au nœud suivant et au nœud précédent :

![Diagramme d'une liste doublement chaînée. Chaque nœud de la liste doublement chaînée a un pointeur vers le nœud qui le précède et le nœud qui le suit.](https://cdn.hashnode.com/res/hashnode/image/upload/v1729610464614/f2f11dcd-56e9-401d-b35b-f5a29d8d9dc5.png align="center")

Un scénario comme celui-ci utilisant `Rc` ou `Arc` pour les nœuds suivant et précédent peut provoquer des cycles de référence. Les cycles de référence empêchent les nœuds d'être désalloués car pour qu'un nœud soit désalloué, toutes les références `Arc` ou `Rc` à celui-ci doivent être à 0. Puisque les nœuds dans ce cas contiennent des références à d'autres nœuds qui contiennent également des références en retour, les deux nœuds ne peuvent pas être désalloués automatiquement et ils peuvent finir par empêcher tous les autres nœuds de la structure de données d'être désalloués, provoquant une fuite de mémoire.

Pour éviter les cycles de référence tout en permettant aux nœuds de référencer à la fois les nœuds précédents et suivants, vous pouvez rendre la référence de chaque nœud à son nœud précédent une référence `Weak`. Par exemple :

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

#[derive(Debug)]
struct Node {
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
    prev: Option<Weak<RefCell<Node>>>, // Référence Weak pour éviter les cycles
}

fn main() {
    let node1 = Rc::new(RefCell::new(Node { value: 1, next: None, prev: None }));
    let node2 = Rc::new(RefCell::new(Node { value: 2, next: None, prev: Some(Rc::downgrade(&node1)) }));

    // Définir le next de node1 sur node2
    node1.borrow_mut().next = Some(Rc::clone(&node2));

    println!("Node 1: {:?}", node1);
    println!("Node 2: {:?}", node2);
}
```

Cependant, puisque les références `Weak` ont des références non propriétaires aux allocations mémoire, elles doivent être mises à niveau vers des références `Rc` ou `Arc` avec `.upgrade()` pour permettre l'accès à l'allocation mémoire qu'elles pointent.

De plus, comme vous pouvez le voir dans l'exemple de code ci-dessous (ainsi que ci-dessus à la ligne 13), les références `Rc` et `Arc` peuvent être rétrogradées en références `Weak` avec `Rc::downgrade()` ou `Arc::downgrade()` :

```rust
use std::rc::{Rc, Weak};

fn main() {
    let strong = Rc::new(5);
    let weak = Rc::downgrade(&strong);

    // Supprimer la référence faible
    drop(weak);

    // essayer de mettre à niveau la référence faible
    if let Some(shared) = weak.upgrade() {
        println!("Les données sont toujours vivantes : {}", shared);
    } else {
        println!("Les données ont été supprimées");
    }
}
```

L'exécution de ce code donne le résultat suivant :

```rust
Les données ont été supprimées
```

Cela montre que le fait de n'avoir que des références faibles à une allocation mémoire ne l'empêche pas d'être supprimée. Si l'allocation mémoire d'un pointeur `Weak` est supprimée, l'appel de `.upgrade()` sur le pointeur `Weak` retournerait `None`.

## `RefCell`

Pour garantir la sécurité de la mémoire, Rust ne vous permet pas de muter les données vers lesquelles pointent les pointeurs intelligents. Cela peut prévenir les mutations cachées, mais peut devenir vraiment gênant lorsque vous devez construire quelque chose qui change dynamiquement (par exemple, la capacité d'ajouter un nouveau nœud n'importe où dans une structure de données de liste chaînée).

`RefCell` vous permet de surmonter cette limitation car c'est une structure de données qui permet la mutabilité intérieure des variables immuables en appliquant les règles d'emprunt de Rust au moment de l'exécution.

Vous avez peut-être remarqué son utilisation dans l'exemple de pointeur `Weak` précédent :

```rust
use std::rc::{Rc, Weak};
use std::cell::RefCell;

#[derive(Debug)]
struct Node {
    value: i32,
    next: Option<Rc<RefCell<Node>>>,
    prev: Option<Weak<RefCell<Node>>>,
}

fn main() {
    let node1 = Rc::new(RefCell::new(Node { value: 1, next: None, prev: None }));
    let node2 = Rc::new(RefCell::new(Node { value: 2, next: None, prev: Some(Rc::downgrade(&node1)) }));

    // Définir le next de node1 sur node2
    node1.borrow_mut().next = Some(Rc::clone(&node2));

    println!("Node 1: {:?}", node1);
    println!("Node 2: {:?}", node2);
}
```

Vous pouvez appeler `.borrow()` et `.borrow_mut()` sur un type `RefCell` pour emprunter des références à sa valeur interne au moment de l'exécution, tout en gardant son propre type immuable, ce qui le rend utile dans des cas comme celui-ci qui nécessitent l'immuabilité.

Les emprunts mutables et immuables dans un type `RefCell` fonctionnent exactement comme les emprunts réguliers qui sont vérifiés au moment de la compilation, mais ils vous permettent de contourner les restrictions de compilation pour être vérifiés au moment de l'exécution.

Une règle majeure d'emprunt à surveiller est la règle « propriété mutable unique et propriété immuable multiple ». Emprunter deux références mutables à un `RefCell` entraînerait une panique, faisant planter l'application. Par exemple :

```rust
#![allow(unused_variables)]
#![allow(dead_code)]
#![allow(unused_mut)]
use std::cell::RefCell;

fn main() {
    let counter = RefCell::new(100);
    let mut c1 = counter.borrow_mut();
    let mut c2 = counter.borrow_mut();

    println!("J'ai terminé");
}

/**
 * sortie :
 *  thread 'main' panicked at src/main.rs:9:26:
 *  already borrowed: BorrowMutError
 *  note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace
 */
```

## Résumé

Pour donner un aperçu des points abordés dans cet article, il existe quatre types courants de pointeurs intelligents en Rust :

* `Box` est utilisé pour l'allocation manuelle de mémoire dans le tas (similaire à `malloc` et `new` en C et C++ respectivement)

* `Rc` et `Arc` sont utilisés pour permettre une propriété multiple d'une allocation mémoire. `Arc` est idéal pour les environnements multithreads, et `Rc` est idéal pour les environnements monothreads.

* `Weak` est principalement utilisé pour donner une propriété multiple d'une allocation mémoire tout en empêchant les cycles de référence.

* `RefCell` permet la mutabilité dans les scénarios qui nécessitent l'immuabilité, par exemple, dans les pointeurs intelligents.

J'espère que cet article a fourni des éclaircissements sur les pointeurs intelligents en Rust et leur fonctionnement. Merci pour la lecture !