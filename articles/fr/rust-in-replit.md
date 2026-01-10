---
title: Cours de Programmation Rust – Tutoriel Interactif sur le Langage Rust sur Replit
subtitle: ''
author: Shaun Hamilton
co_authors: []
series: null
date: '2021-11-30T14:35:18.000Z'
originalURL: https://freecodecamp.org/news/rust-in-replit
coverImage: https://www.freecodecamp.org/news/content/images/2021/11/rust-and-sunset.png
tags:
- name: repl.it
  slug: replit
- name: Rust
  slug: rust
- name: RustLang
  slug: rustlang
- name: youtube
  slug: youtube
seo_title: Cours de Programmation Rust – Tutoriel Interactif sur le Langage Rust sur
  Replit
seo_desc: 'For six years in a row, Rust has been voted the most loved programming
  language by Stack Overflow.

  So if you''re ready to learn this popular programming language, this course will
  introduce you to Rust so you can start using it in your projects.

  You w...'
---

Pendant six années consécutives, Rust a été élu le langage de programmation le plus apprécié par [Stack Overflow](https://insights.stackoverflow.com/survey/2021#technology-most-loved-dreaded-and-wanted).

Si vous êtes prêt à apprendre ce langage de programmation populaire, ce cours vous introduira à Rust afin que vous puissiez commencer à l'utiliser dans vos projets.

Vous travaillerez entièrement dans votre navigateur en utilisant l'environnement de programmation interactif [Replit](https://replit.com). freeCodeCamp s'est associé à Replit qui a rendu ce cours possible.

%[https://youtu.be/MsocPEZBd-M]

Il existe également une version vidéo de ce cours sur la [chaîne YouTube freeCodeCamp](https://youtu.be/MsocPEZBd-M).

Pour tirer le meilleur parti de ce cours, vous devriez avoir des connaissances intermédiaires dans au moins un autre langage de programmation. Si vous êtes nouveau en programmation, vous devriez essayer le [programme interactif de freeCodeCamp](https://www.freecodecamp.org/learn/) puis revenir à ce cours.

Pour vous aider à apprendre Rust, nous créerons deux projets :

1. Une calculatrice pour la ligne de commande
2. Un outil en ligne de commande qui prend deux images et combine leurs pixels

## Table des Matières

Voici les sections et les sujets que nous aborderons dans ce cours. Vous pouvez cliquer sur la table des matières ci-dessous pour accéder à des parties spécifiques, ou vous pouvez simplement suivre de début à fin.

- [Aperçu de Rust](#heading-aperçu-de-rust)
- [Comment Utiliser Rust dans Replit](#heading-comment-utiliser-rust-dans-replit)
- [Bases de Rust](#heading-bases-de-rust)
  - [Variables en Rust](#heading-variables-en-rust)
  - [Fonctions en Rust](#heading-fonctions-en-rust)
  - [Chaînes de caractères et Tranches en Rust](#heading-chaînes-de-caractères-et-tranches-en-rust)
  - [Le type `char` en Rust](#heading-le-type-char-en-rust)
  - [Types de Nombres en Rust](#heading-types-de-nombres-en-rust)
  - [Structures en Rust](#heading-structures-en-rust)
  - [Énumérations en Rust](#heading-énumérations-en-rust)
  - [Macros en Rust](#heading-macros-en-rust)
  - [Possession en Rust](#heading-possession-en-rust)
- [Projet #1 - Construire une Calculatrice CLI en Rust](#heading-projet-1-construire-une-calculatrice-cli-en-rust)
  - [Résultat du Projet](#heading-resultat-du-projet)
  - [Méthodologie du Projet de Calculatrice CLI](#heading-methodologie-du-projet-de-calculatrice-cli)
    - [Étape 1 - Créer un Nouveau Projet](#heading-etape-1-creer-un-nouveau-projet)
    - [Étape 2 - Comprendre la Syntaxe](#heading-etape-2-comprendre-la-syntaxe)
    - [Étape 3 - Exécuter le Projet](#heading-etape-3-executer-le-projet)
    - [Étape 4 - Arguments de Ligne de Commande](#heading-etape-4-arguments-de-ligne-de-commande)
    - [Étape 5 - Analyser les Chaînes en Nombres](#heading-etape-5-analyser-les-chaines-en-nombres)
    - [Étape 6 - Effectuer des Opérations Arithmétiques de Base](#heading-etape-6-effectuer-des-operations-arithmetiques-de-base)
    - [Étape 7 - Formater la Sortie](#heading-etape-7-formater-la-sortie)
    - [Étape 8 - Tout Rassembler](#heading-etape-8-tout-rassembler)
- [Projet #2 - Construire un Combineur d'Images en Rust](#heading-projet-2-construire-un-combineur-dimages-en-rust)
  - [Résultat du Projet](#heading-resultat-du-projet-1)
  - [Méthodologie du Projet de Combineur d'Images](#heading-methodologie-du-projet-de-combineur-dimages)
    - [Étape 1 - Créer un Nouveau Projet](#heading-etape-1-creer-un-nouveau-projet-1)
    - [Étape 2 - Ajouter un Nouveau Module pour les Args](#heading-etape-2-ajouter-un-nouveau-module-pour-les-args)
    - [Étape 3 - Importer et Utiliser le Module `args`](#heading-etape-3-importer-et-utiliser-le-module-args)
    - [Étape 4 - Ajouter une Caisse Externe](#heading-etape-4-ajouter-une-caisse-externe)
    - [Étape 5 - Lire un Fichier Image](#heading-etape-5-lire-un-fichier-image)
    - [Étape 6 - Gérer les Erreurs avec `Result`](#heading-etape-6-gerer-les-erreurs-avec-result)
    - [Étape 7 - Redimensionner les Images pour les Faire Correspondre](#heading-etape-7-redimensionner-les-images-pour-les-faire-correspondre)
    - [Étape 8 - Créer une Image Flottante](#heading-etape-8-creer-une-image-flottante)
    - [Étape 9 - Créer les Données d'Image Combinées](#heading-etape-9-creer-les-donnees-dimage-combinees)
    - [Étape 10 - Attacher les Données Combinées à l'Image Flottante](#heading-etape-10-attacher-les-donnees-combinees-a-limage-flottante)
    - [Étape 11 - Écrire l'Image dans un Fichier](#heading-etape-11-ecrire-limage-dans-un-fichier)
    - [Étape 12 - Tout Rassembler](#heading-etape-12-tout-rassembler)
- [Conclusion](#heading-conclusion)

## Aperçu de Rust

Rust est un langage de programmation de _niveau système_.

> "[Rust] traite les détails de bas niveau de la gestion de la mémoire, de la représentation des données et de la concurrency."
>   
> "... le langage est conçu pour vous guider naturellement vers un code fiable qui est efficace en termes de vitesse et d'utilisation de la mémoire." ([Source : Rust docs](https://doc.rust-lang.org/book/foreword.html))

Les principaux outils de l'écosystème Rust sont :

* rustc – Le compilateur qui prend votre code Rust et le compile en binaire (code lisible par la machine)
* rustup – L'utilitaire en ligne de commande pour installer et mettre à jour Rust
* cargo – Le système de construction et le gestionnaire de paquets Rust

## Comment Utiliser Rust dans Replit

Pour ce cours, vous utiliserez [ce dépôt GitHub](https://github.com/freeCodeCamp/Rust-In-Replit/) comme modèle.

Pour commencer, cliquez sur le lien suivant pour créer un nouveau REPL à partir du modèle :

<a href="https://replit.com/github/freeCodeCamp/Rust-in-Replit">
  <img src="https://replit.com/badge/github/freeCodeCamp/Rust-in-Replit" alt="exécuter sur replit" width="200" height="60" style="display: block; margin: 0 auto" />
</a>

Ensuite, dans la fenêtre modale Import from GitHub, ouvrez le menu déroulant Langage et sélectionnez Bash :

![La fenêtre modale Import from GitHub sur Replit montrant le menu déroulant Langage et sélectionnant Bash comme langage.](https://www.freecodecamp.org/news/content/images/2022/10/select-bash-as-language.jpg)

Ensuite, cliquez sur le bouton Import from GitHub en bas à droite pour importer le code modèle dans Replit.

Enfin, pour commencer le cours, cliquez sur le bouton Run en haut de l'écran et suivez les instructions dans la console à droite :

![Le début du cours après avoir cliqué sur le bouton Run, avec un README avec des instructions à gauche et la console Replit à droite avec un message de bienvenue.](https://www.freecodecamp.org/news/content/images/2022/10/run-the-course-and-select-a-language.jpg)

## Bases de Rust

### Variables en Rust

Vous pouvez déclarer des variables en utilisant les mots-clés `let`, `const`, ou `static` :

```rust
let my_variable = 0;
const MY_CONSTANT: u8 = 0;
static MY_STATIC: u8 = 0;

```

Par défaut, toutes les variables sont immuables. Vous pouvez rendre une variable mutable en utilisant le mot-clé `mut` :

```rust
let mut my_mutable_variable = 0;

```

La convention Rust repose sur les conventions de casse suivantes :

<table>
<thead>
<tr>
<th>Objet</th>
<th>Casse</th>
</tr>
</thead>
<tbody>
<tr>
<td>Variables</td>
<td>snake_case</td>
</tr>
<tr>
<td>Fonctions</td>
<td>snake_case</td>
</tr>
<tr>
<td>Fichiers</td>
<td>snake_case</td>
</tr>
<tr>
<td>Constantes</td>
<td>SCREAMING_SNAKE_CASE</td>
</tr>
<tr>
<td>Statiques</td>
<td>SCREAMING_SNAKE_CASE</td>
</tr>
<tr>
<td>Types</td>
<td>PascalCase</td>
</tr>
<tr>
<td>Traits</td>
<td>PascalCase</td>
</tr>
<tr>
<td>Énumérations</td>
<td>PascalCase</td>
</tr>
</tbody>
</table>

Puisque Rust est typé statiquement, vous devez typer explicitement les variables – sauf si la variable est déclarée avec `let` et que le type peut être inféré.

### Fonctions en Rust

Vous déclarez des fonctions en utilisant le mot-clé `fn` :

```rust
fn main() {
  // Ceci est un commentaire de code
}

```

Les fonctions retournent en utilisant le mot-clé `return`, et vous devez spécifier explicitement le type de retour d'une fonction, sauf si le type de retour est un tuple vide `()` :

```rust
fn main() -> () { // Type de retour inutile
  my_func();
}

fn my_func() -> u8 {
  return 0;
}

```

Les fonctions retournent également une expression sans point-virgule :

```rust
fn my_func() -> u8 {
  0
}

```

Les paramètres de fonction sont typés en utilisant la syntaxe `:` :

```rust
fn main() {
  let _unused_variable = my_func(10);
}

fn my_func(x: u8) -> i32 {
  x as i32
}

```

Le soulignement avant un nom de variable est une convention pour indiquer que la variable n'est pas utilisée. Le mot-clé `as` affirme le type de l'expression, à condition que la conversion de type soit valide.

### Chaînes de caractères et Tranches en Rust

Un point de confusion courant pour les débutants en Rust est la différence entre la structure `String` et le type `str`.

```rust
let my_str: &str = "Bonjour, le monde !";

let my_string: String = String::from("Bonjour, le monde !");

```

Dans l'exemple ci-dessus, `my_str` est une référence à un _littéral de chaîne_, et `my_string` est une instance de la structure `String`.

Une distinction importante entre les deux est que `my_str` est stocké dans la pile, et `my_string` est alloué dans le tas. Cela signifie que la valeur de `my_str` ne peut pas changer, et sa taille est fixe, tandis que `my_string` peut avoir une taille inconnue au moment de la compilation.

Le _littéral de chaîne_ est également connu sous le nom de _tranche de chaîne_. Cela est dû au fait qu'un `&str` fait référence à une partie d'une chaîne. Généralement, voici comment les tableaux et les chaînes sont similaires :

```rust
let my_string = String::from("The quick brown fox");
let my_str: &str = &my_string[4..9]; // "quick"

let my_arr: [usize; 5] = [1, 2, 3, 4, 5];
let my_arr_slice: &[usize] = &my_arr[0..3]; // [1, 2, 3]

```

La notation `[T; n]` est utilisée pour créer un tableau de `n` éléments de type `T`.

### Le type `char` en Rust

Un `char` est une USV (Unicode Scalar Value), qui est représentée en unicode avec des valeurs comme `U+221E` – l'unicode pour ' 221e'. Vous pouvez penser à une collection ou un tableau de `char` comme une chaîne :

```rust
let my_str: &str = "Bonjour, le monde !";

let collection_of_chars: &str = my_str.chars().as_str();

```

### Types de Nombres en Rust

Il existe de nombreux types de nombres en Rust :

* Entiers non signés : `u8`, `u16`, `u32`, `u64`, `u128`
* Entiers signés : `i8`, `i16`, `i32`, `i64`, `i128`
* Nombres à virgule flottante : `f32`, `f64`

Les entiers non signés ne représentent que des nombres entiers positifs.

Les entiers signés représentent à la fois des nombres entiers positifs et négatifs.

Et les flottants ne représentent que des fractions positives et négatives.

### Structures en Rust

Une _structure_ est un type de données personnalisé utilisé pour regrouper des données liées. Vous avez déjà rencontré une structure dans la section [Chaînes de caractères et Tranches](#heading-chaînes-de-caractères-et-tranches-en-rust) :

```rust
struct String {
  vec: Vec<u8>,
}

```

La structure `String` se compose d'un champ `vec`, qui est un `Vec` de `u8`. Le `Vec` est un tableau de taille dynamique.

Une instance d'une structure est ensuite déclarée en donnant des valeurs aux champs :

```rust
struct MyStruct {
  field_1: u8,
}

let my_struct = MyStruct { field_1: 0, };

```

Précédemment, la structure `String` a été utilisée avec sa fonction `from` pour créer une `String` à partir d'un `&str`. Cela est possible, car la fonction `from` est implémentée pour `String` :

```rust
impl String {
  fn from(s: &str) -> Self {
    String {
      vec: Vec::from(s.as_bytes()),
    }
  }
}

```

Vous utilisez le mot-clé `Self` à la place du type de la structure.

Les structures peuvent également prendre d'autres variantes :

```rust
struct MyUnitStruct;
struct MyTupleStruct(u8, u8);

```

### Énumérations en Rust

Similaires à d'autres langages, les énumérations sont utiles pour agir comme des types et comme des valeurs.

```rust
enum MyErrors {
  BrainTooTired,
  TimeOfDay(String)
  CoffeeCupEmpty,
}

fn work() -> Result<(), MyErrors> { // Result est aussi une énumération
  if state == "missing semi-colon" {
    Err(MyErrors::BrainTooTired)
  } else if state == "06:00" {
    Err(MyErrors::TImeOfDay("Il est trop tôt pour travailler".to_string()))
  } else if state == "22:00" {
    Err(MyErrors::TimeOfDay("Il est trop tard pour travailler".to_string()))
  } else if state == "empty" {
    Err(MyErrors::CoffeeCupEmpty)
  } else {
    Ok(())
  }
}

```

### Macros en Rust

Une macro est similaire à une fonction, mais vous pouvez la considérer comme un morceau de code qui écrit d'autres codes. Pour l'instant, les principales différences entre une fonction et une macro à garder à l'esprit sont :

* Les macros sont appelées en utilisant un point d'exclamation (`!`)
* Les macros peuvent prendre un nombre variable d'arguments, tandis que les fonctions en Rust ne le peuvent pas

L'une des macros les plus courantes est la macro `println!`, qui imprime sur la console :

```rust
let my_str = "Bonjour, le monde !";
println!("{}", my_str);

```

Vous utilisez la syntaxe `{}` pour insérer une variable dans une chaîne.

Une autre macro courante est `panic!`. _Paniquer_ est la manière de Rust de 'sortir avec une erreur'. Il est judicieux de considérer un panic en Rust comme une erreur mal gérée. La macro accepte un littéral de chaîne, et panique avec ce message.

```rust
let am_i_an_error = true;

if (am_i_an_error) {
  panic!("Il y a eu une erreur");
}

```

```bash
$ cargo run
   Compiling fcc-rust-in-replit v0.1.0 (/home/runner/Rust-in-Replit)
    Finished dev [unoptimized + debuginfo] target(s) in 1.66s
     Running `target/debug/calculator`
thread 'main' panicked at 'Il y a eu une erreur', src/main.rs
note: run with `RUST_BACKTRACE=1` environment variable to display a backtrace

```

### Possession en Rust

Un concept important en Rust est la _possession_. Il y a trois règles principales de possession :

* Chaque valeur en Rust a une variable qui est appelée son _propriétaire_.
* Il ne peut y avoir qu'un seul propriétaire à la fois.
* Lorsque le propriétaire sort de la portée, la valeur sera abandonnée.  
([Source : The Rust Book](https://doc.rust-lang.org/book/ch04-01-what-is-ownership.html?highlight=heap#ownership-rules))

C'est ainsi que Rust se passe d'un ramasse-miettes typique, tout en ne nécessitant pas que le programmeur gère explicitement la mémoire. Voici un exemple de possession :

```rust
fn main() { // first_string n'est pas encore déclaré -> n'a pas de valeur
  let first_string = String::from("freeCodeCamp"); // first_string est maintenant propriétaire de la valeur "freeCodeCamp"
  let second_string = first_string; // second_string prend possession de la valeur "freeCodeCamp"

  println!("Bonjour, {}!", first_string); // first_string n'est PAS valide, car la valeur a été déplacée vers second_string
}

```

Comme la macro `println!` essaie de faire référence à une variable invalide, ce code ne compile pas. Pour corriger cela, au lieu de déplacer la valeur de `first_string` dans `second_string`, `second_string` peut être assigné une référence à `first_string` :

```rust
fn main() {
  let first_string: String = String::from("freeCodeCamp");
  let second_string: &String = &first_string; // first_string est toujours le propriétaire de la valeur "freeCodeCamp"

  println!("Bonjour, {}!", first_string);
}

```

Le esperluette (`&`) indique que la valeur est une référence. C'est-à-dire que `second_string` ne prend plus possession de `"freeCodeCamp"`, mais, au lieu de cela, pointe vers le même point en mémoire que `first_string`.

## Projet #1 – Construire une Calculatrice CLI en Rust

### Résultat du Projet

À la fin de ce projet, vous serez en mesure d'effectuer des opérations arithmétiques de base sur des nombres en utilisant la ligne de commande.

Des exemples d'entrée et de sortie attendues ressemblent à ceci :

```bash
$ calculator 1 + 1
$ 1 + 1 = 2

$ calculator 138 / 4
$ 138 / 4 = 34.5

```

### Méthodologie du Projet de Calculatrice CLI

#### Étape 1 – Créer un Nouveau Projet

Utilisez Cargo pour créer un nouveau projet nommé `calculator` :

```bash
$ cargo new calculator

```

Cela crée un nouveau répertoire nommé `calculator`, l'initialise comme un dépôt Git, et ajoute un modèle utile pour votre projet.

Le modèle inclut :

* `Cargo.toml` – Le fichier manifeste utilisé par Cargo pour gérer les métadonnées de votre projet
* `src/` – Le répertoire où votre code de projet doit résider
* `src/main.rs` – Le fichier par défaut que Cargo utilise comme point d'entrée de votre application

#### Étape 2 – Comprendre la Syntaxe

Le fichier `calculator/Cargo.toml` contient ce qui suit :

```toml
[package]
name = "calculator"
version = "0.1.0"
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]


```

Le `[package]` désigne les métadonnées de votre projet.

L'en-tête `[dependencies]` désigne les crates dont votre projet dépend. _Les crates sont comme des bibliothèques externes._

Le fichier `calculator/src/main.rs` contient ce qui suit :

```rust
fn main() {
  println!("Bonjour, le monde !");
}

```

Ce fichier contient une déclaration de fonction avec le handle `main`. Par défaut, rustc appelle la fonction `main` en premier chaque fois que l'exécutable est lancé.

`println!` est une macro intégrée qui imprime sur la console.

#### Étape 3 – Exécuter le Projet

Vous pouvez soit utiliser Cargo pour exécuter votre code de projet :

```bash
# Dans le répertoire calculator/
$ cargo run
   Compiling fcc-rust-in-replit v0.1.0 (/home/runner/Rust-in-Replit-1)
    Finished dev [unoptimized + debuginfo] target(s) in 0.80s
     Running `target/debug/calculator`
Bonjour, le monde !

```

Ou, vous pouvez utiliser rustc pour compiler votre projet, puis vous pouvez exécuter le binaire :

```bash
# Dans le répertoire calculator/
$ rustc src/main.rs
$ ./main
Bonjour, le monde !

```

#### Étape 4 – Arguments de Ligne de Commande

La bibliothèque standard Rust est livrée avec un module `env`, qui permet l'accès aux arguments de ligne de commande passés lors de l'appel du programme.

Les exports nécessaires du module `env` sont la fonction `args`, et la structure `Args`. La fonction `args` retourne une instance de la structure `Args`, et est importée dans la portée du fichier avec :

```rust
use std::env::{args, Args};

```

Pour avoir une idée de ce à quoi ressemble la structure `Args`, la variable `args` est imprimée sur la console :

```rust
fn main() {
  let args: Args = args();
  println!("{:?}", args);
}

```

```bash
$ cargo run -- fCC
   Compiling calculator v0.1.0 (/home/runner/Rust-in-Replit/calculator)
    Finished dev [unoptimized + debuginfo] target(s) in 1.71s
     Running `target/debug/calculator`
Args { inner: ["target/debug/toto", "fCC"] }

```

Ce qui précède montre que la structure `Args` contient un `champ` appelé `inner` qui se compose de l'emplacement du binaire compilé, et des arguments de ligne de commande passés au programme.

Pour accéder aux valeurs des arguments, vous pouvez utiliser la méthode `nth` sur la variable `args`. La méthode `nth` prend un argument `index`, et retourne la valeur à cet index enveloppée dans un `Option`. Ainsi, la valeur doit être déballée.

```rust
fn main() {
  let mut args: Args = args();

  let first: String = args.nth(1).unwrap();
}

```

La variable `args` doit être déclarée comme mutable, car la méthode `nth` itère de manière mutable sur les éléments, et supprime l'élément accédé.

```rust
fn main() {
  let mut args: Args = args();

  // Le premier argument est l'emplacement du binaire compilé, alors ignorez-le
  let first: String = args.nth(1).unwrap();
  // Après avoir accédé au deuxième argument, le prochain élément de l'itérateur devient le premier
  let operator: String = args.nth(0).unwrap();
  let second: String = args.nth(0).unwrap();

  println!("{} {} {}", first, operator, second);
}

```

```bash
$ cargo run -- 1 + 1
   Compiling calculator v0.1.0 (/home/runner/Rust-in-Replit/calculator)
    Finished dev [unoptimized + debuginfo] target(s) in 1.71s
     Running `target/debug/calculator`
1 + 1

```

#### Étape 5 – Analyser les Chaînes en Nombres

Les variables `first` et `second` sont des chaînes, et vous devez les analyser en nombres. La structure `String` implémente la méthode `parse`, qui prend une annotation de type, et retourne un `Result` contenant la valeur analysée.

```rust
use std::env::{args, Args};

fn main() {
  let mut args: Args = args();

  let first: String = args.nth(1).unwrap();
  let operator: String = args.nth(0).unwrap();
  let second: String = args.nth(0).unwrap();

  let first_number = first.parse::<f32>().unwrap();
  let second_number = second.parse::<f32>().unwrap();

  println!("{} {} {}", first_number, operator, second_number);
}

```

La méthode `parse` ci-dessus utilise la syntaxe _turbofish_ pour spécifier le type à essayer d'analyser la chaîne.

#### Étape 6 – Effectuer des Opérations Arithmétiques de Base

Rust utilise les opérateurs standard pour l'addition, la soustraction, la multiplication et la division.

Pour gérer les opérations, vous définissez une fonction nommée `operate` qui prendra trois arguments : l'opérateur en tant que `char`, et les deux nombres en tant que `f32`. La fonction doit également retourner un `f32` représentant le résultat de l'opération.

```rust
fn operate(operator: char, first_number: f32, second_number: f32) -> f32 {
  match operator {
    '+' => first_number + second_number,
    '-' => first_number - second_number,
    '/' => first_number / second_number,
    '*' | 'X' | 'x' => first_number * second_number,
    _ => panic!("Opérateur invalide utilisé."),
  }
}

```

L'expression `match` fonctionne de manière similaire à une instruction `switch` dans d'autres langages. L'expression `match` prend une valeur, et une liste de _bras_. Chaque _bras_ est un motif et un bloc. Le motif est une valeur à comparer, et le bloc est le code à exécuter si le motif correspond. Le motif `_` est un joker, agissant comme une clause `else`.

Le bras de multiplication inclut la comparaison `OR` pour permettre les cas de `X` et `x` à être gérés.

Maintenant, pour appeler `operate` avec l'`operator`, vous devez d'abord le convertir en `char`. Vous faites cela avec la méthode `chars` sur la structure `String` qui retourne un itérateur sur les caractères de la chaîne. Ensuite, le premier caractère est déballé :

```rust
fn main() {
  let mut args: Args = args();

  let first: String = args.nth(1).unwrap();
  let operator: char = args.nth(0).unwrap().chars().next().unwrap();
  let second: String = args.nth(0).unwrap();

  let first_number = first.parse::<f32>().unwrap();
  let second_number = second.parse::<f32>().unwrap();
  let result = operate(operator, first_number, second_number);

  println!("{} {} {}", first_number, operator, second_number);
}

```

Le retour de `operate` est stocké dans la variable `result`.

#### Étape 7 – Formater la Sortie

Pour obtenir la sortie souhaitée, les variables `first_number`, `second_number`, `operator`, et `result` doivent être formatées. Vous pouvez utiliser la macro `format!` pour créer une `String` à partir d'une chaîne de format et d'une liste d'arguments :

```rust
fn output(first_number: f32, operator: char, second_number: f32, result: f32) -> String {
  format!(
    "{} {} {} = {}",
    first_number, operator, second_number, result
  )
}

```

#### Étape 8 – Tout Rassembler

```rust
use std::env::{args, Args};

fn main() {
  let mut args: Args = args();

  let first: String = args.nth(1).unwrap();
  let operator: char = args.nth(0).unwrap().chars().next().unwrap();
  let second: String = args.nth(0).unwrap();

  let first_number = first.parse::<f32>().unwrap();
  let second_number = second.parse::<f32>().unwrap();
  let result = operate(operator, first_number, second_number);

  println!("{}", output(first_number, operator, second_number, result));
}

fn output(first_number: f32, operator: char, second_number: f32, result: f32) -> String {
  format!(
    "{} {} {} = {}",
    first_number, operator, second_number, result
  )
}

fn operate(operator: char, first_number: f32, second_number: f32) -> f32 {
  match operator {
    '+' => first_number + second_number,
    '-' => first_number - second_number,
    '/' => first_number / second_number,
    '*' | 'X' | 'x' => first_number * second_number,
    _ => panic!("Opérateur invalide utilisé."),
  }
}

```

Pour construire le code en un binaire exécutable, exécutez la commande suivante :

```bash
$ cargo build --release
   Compiling calculator v0.1.0 (/home/runner/Rust-in-Replit/calculator)
    Finished release [optimized] target(s) in 3.26s

```

Le drapeau `--release` indique à Cargo de construire le binaire en mode release. Cela réduira la taille du binaire et supprimera également toutes les informations de débogage.

Le binaire est construit dans le répertoire `target/release`. Pour exécuter le binaire et tester votre application, exécutez la commande suivante :

```bash
$ target/release/calculator 1 + 1
1 + 1 = 2

```

## Projet #2 – Construire un Combineur d'Images en Rust

### Résultat du Projet

À la fin de ce projet, vous serez en mesure de combiner deux images en utilisant la ligne de commande.

Voici un exemple d'une entrée attendue :

```bash
$ combiner ./image1.png ./image2.png ./output.png

```

Pour un exemple de la sortie, ne cherchez pas plus loin que la première image de cet article  261d fe0f

### Méthodologie du Projet de Combineur d'Images

#### Étape 1 - Créer un Nouveau Projet

Utilisez Cargo pour créer un nouveau projet nommé `combiner` :

```bash
$ cargo new combiner

```

#### Étape 2 - Ajouter un Nouveau Module pour les Args

Pour éviter que le fichier `main.rs` ne devienne trop écrasant, créez un nouveau fichier nommé `args.rs` dans le répertoire `src`.

Dans `args.rs`, créez une fonction nommée `get_nth_arg` qui prend un `usize`, `n`, et retourne une `String`. Ensuite, à partir du module `std::env`, appelez la fonction `args`, et enchaînez la méthode `nth` pour obtenir le `n`ième argument, en déballant la valeur :

```rust
fn get_nth_arg(n: usize) -> String {
  std::env::args().nth(n).unwrap()
}

```

Définissez une structure publique nommée `Args` qui se compose de trois champs publics de type `String` : `image_1`, `image_2`, et `output` :

```rust
pub struct Args {
  pub image_1: String,
  pub image_2: String,
  pub output: String,
}

```

Déclarez la structure et ses champs comme publics avec le mot-clé `pub` afin que vous puissiez y accéder depuis l'extérieur du fichier `args.rs`.

Enfin, vous pouvez utiliser la fonction `get_nth_arg` pour créer une nouvelle structure `Args` dans une fonction `new` :

```rust
impl Args {
  pub fn new() -> Self {
    Args {
      image_1: get_nth_arg(1),
      image_2: get_nth_arg(2),
      output: get_nth_arg(3),
    }
  }
}

```

Ensemble, le fichier `args.rs` ressemble à ceci :

```rust
pub struct Args {
  pub image_1: String,
  pub image_2: String,
  pub output: String,
}

impl Args {
  pub fn new() -> Self {
    Args {
      image_1: get_nth_arg(1),
      image_2: get_nth_arg(2),
      output: get_nth_arg(3),
    }
  }
}

fn get_nth_arg(n: usize) -> String {
  std::env::args().nth(n).unwrap()
}

```

#### Étape 3 – Importer et Utiliser le Module `args`

Dans `main.rs`, vous devez déclarer le fichier `args.rs` comme un module. Ensuite, pour utiliser la structure `Args`, vous devez l'importer :

```rust
mod args;
use args::Args;

fn main() {
  let args = Args::new();
  println!("{:?}", args);
}

```

Mais le test du code révèle une erreur :

```bash
$ cargo run -- arg1 arg2 arg3
   Compiling combiner v0.1.0 (/home/runner/Rust-in-Replit/combiner)
error[E0277]: `args::Args` doesn't implement `Debug`
  --> src/main.rs:12:20
   |
12 |   println!("{:?}", args);
   |                    ^^^^ `args::Args` cannot be formatted using `{:?}`
   |
   = help: the trait `Debug` is not implemented for `args::Args`
   = note: add `#[derive(Debug)]` or manually implement `Debug`
   = note: required by `std::fmt::Debug::fmt`
   = note: this error originates in a macro (in Nightly builds, run with -Z macro-backtrace for more info)

error: aborting due to previous error

For more information about this error, try `rustc --explain E0277`.
error: could not compile `combiner`

To learn more, run the command again with --verbose.

```

De manière similaire à la façon dont les fonctions sont implémentées pour les structures, les traits peuvent être implémentés pour les structures. Cependant, le trait `Debug` est spécial en ce sens qu'il peut être implémenté en utilisant des attributs :

```rust
#[derive(Debug)]
pub struct Args {
  pub image_1: String,
  pub image_2: String,
  pub output: String,
}

```

Le trait `Debug` a été _dérivé_ pour la structure `Args`. Cela signifie que le trait `Debug` est automatiquement implémenté pour la structure, sans que vous ayez à l'implémenter manuellement 🚀.

Maintenant, l'exécution du code fonctionne :

```bash
$ cargo run -- arg1 arg2 arg3
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/combiner arg1 arg2 arg3`
Args { image_1: "arg1", image_2: "arg2", output: "arg3" }

```

#### Étape 4 – Ajouter une Caisse Externe

De la même manière que d'autres langages ont des bibliothèques ou des paquets, Rust a des crates. Afin de coder et de décoder des images, vous pouvez utiliser la crate `image`.

Ajoutez la crate `image` avec la version `0.23.14` au fichier `Cargo.toml` :

```toml
[package]
name = "combiner"
version = "0.1.0"
edition = "2018"

# See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
image = "0.23.14"

```

Maintenant, lorsque `cargo run` est appelé ensuite, Cargo récupérera et installera la crate `image`.

#### Étape 5 – Lire un Fichier Image

La crate `image` est livrée avec un module `io` incluant une structure `Reader`. Cette structure implémente une fonction `open` qui prend un chemin vers un fichier image, et retourne un `Result` contenant un _reader_. Vous pouvez formater et décoder ce reader pour obtenir le format de l'image (par exemple PNG, JGP, etc.) et les données de l'image.

Créez une fonction nommée `find_image_from_path` pour ouvrir le fichier image à partir d'un argument `path` :

```rust
fn find_image_from_path(path: String) -> (DynamicImage, ImageFormat) {
  let image_reader: Reader<BufReader<File>> = Reader::open(path).unwrap();
  let image_format: ImageFormat = image_reader.format().unwrap();
  let image: DynamicImage = image_reader.decode().unwrap();
  (image, image_format)
}

```

Les variables `image` et `image_format` sont retournées sous forme de tuple.

Incluez les imports nécessaires en haut du fichier :

```rust
use image::{ io::Reader, DynamicImage, ImageFormat };

fn main() {
  // ...
  let (image_1, image_1_format) = find_image_from_path(args.image_1);
  let (image_2, image_2_format) = find_image_from_path(args.image_2);
}

```

Dans `main`, le tuple retourné peut être déstructuré en deux nouvelles variables pour chaque chemin d'image.

#### Étape 6 – Gérer les Erreurs avec `Result`

Il est important de pouvoir gérer les erreurs qui surviennent. Par exemple, vous pourriez avoir un cas où deux images de formats différents sont données comme arguments à combiner.

Une manière sémantique de gérer une telle erreur est de retourner un `Result` qui peut consister en un `Ok` ou un `Err`.

```rust
fn main() -> Result<(), ImageDataErrors> {
  let args = Args::new();
  println!("{:?}", args);

  let (image_1, image_1_format) = find_image_from_path(args.image_1);
  let (image_2, image_2_format) = find_image_from_path(args.image_2);

  if image_1_format != image_2_format {
    return Err(ImageDataErrors::DifferentImageFormats);
  }
  Ok(())
}

```

La fonction `main` retourne un `Err` contenant une énumération avec une variante unitaire `DifferentImageFormats` si les deux formats d'image ne sont pas égaux. Sinon, elle retourne un `Ok` avec un tuple vide.

L'énumération est définie comme suit :

```rust
enum ImageDataErrors {
  DifferentImageFormats,
}

```

#### Étape 7 – Redimensionner les Images pour les Faire Correspondre

Pour faciliter la combinaison des images, vous redimensionnez la plus grande image pour qu'elle corresponde à la plus petite image.

Tout d'abord, vous pouvez trouver la plus petite image en utilisant la méthode `dimensions` qui retourne la largeur et la hauteur de l'image sous forme de tuple. Ces tuples peuvent être comparés, et le plus petit est retourné :

```rust
fn get_smallest_dimensions(dim_1: (u32, u32), dim_2: (u32, u32)) -> (u32, u32) {
  let pix_1 = dim_1.0 * dim_1.1;
  let pix_2 = dim_2.0 * dim_2.1;
  return if pix_1 < pix_2 { dim_1 } else { dim_2 };
}

```

Les valeurs du tuple sont accessibles en utilisant la notation par points à partir d'un index basé sur zéro.

Si `image_2` est la plus petite image, alors `image_1` doit être redimensionnée pour correspondre aux plus petites dimensions. Sinon, `image_2` doit être redimensionnée.

```rust
fn standardise_size(image_1: DynamicImage, image_2: DynamicImage) -> (DynamicImage, DynamicImage) {
  let (width, height) = get_smallest_dimensions(image_1.dimensions(), image_2.dimensions());
  println!("width: {}, height: {}\n", width, height);

  if image_2.dimensions() == (width, height) {
    (image_1.resize_exact(width, height, Triangle), image_2)
  } else {
    (image_1, image_2.resize_exact(width, height, Triangle))
  }
}

```

La méthode `resize_exact` implémentée sur la structure `DynamicImage` emprunte de manière mutable l'image, et, en utilisant les arguments `width`, `height`, et `FilterType`, redimensionne l'image.

En utilisant le retour de la fonction `standardise_size`, vous pouvez redéclarer les variables `image_1` et `image_2` :

```rust
use image::{ io::Reader, DynamicImage, ImageFormat, imageops::FilterType::Triangle };

fn main() -> Result<(), ImageDataErrors> {
  // ...
  let (image_1, image_2) = standardise_size(image_1, image_2);
  Ok(())
}

```

#### Étape 8 – Créer une Image Flottante

Pour gérer la sortie, créez une structure temporaire pour contenir les métadonnées de l'image de sortie.

Définissez une structure nommée `FloatingImage` pour contenir la `width`, `height`, et `data` de l'image, ainsi que le `name` du fichier de sortie :

```rust
struct FloatingImage {
  width: u32,
  height: u32,
  data: Vec<u8>,
  name: String,
}

```

Ensuite, implémentez une fonction `new` pour `FloatingImage` qui prend des valeurs pour la `width`, `height`, et `name` de l'image de sortie :

```rust
impl FloatingImage {
  fn new(width: u32, height: u32, name: String) -> Self {
    let buffer_capacity = 3_655_744;
    let buffer: Vec<u8> = Vec::with_capacity(buffer_capacity);
    FloatingImage {
      width,
      height,
      data: buffer,
      name,
    }
  }
}

```

Comme vous n'avez pas encore créé les données pour l'image, créez un tampon sous la forme d'un `Vec` de `u8` avec une capacité de 3,655,744 (956 x 956 x 4). La syntaxe `<nombre>_<nombre>` est la numérotation facile à lire de Rust qui sépare le nombre en groupes de trois chiffres.

Utilisez les valeurs `width` et `height` de la variable `image_1` pour créer une instance de `FloatingImage`, et utilisez le troisième argument stocké dans `args` pour définir le nom de `FloatingImage` :

```rust
fn main() -> Result<(), ImageDataErrors> {
  // ...
  let mut output = FloatingImage::new(image_1.width(), image_1.height(), args.output);
  Ok(())
}

```

Déclarez les variables `output` comme mutables afin que vous puissiez modifier le champ `data` plus tard.

#### Étape 9 – Créer les Données d'Image Combinées

Afin de traiter les images, vous devez les convertir en un vecteur de pixels RGBA. Les pixels sont stockés sous forme de `u8`, car leurs valeurs sont comprises entre 0 et 255.

La structure `DynamicImage` implémente la méthode `to_rgba8`, qui retourne un `ImageBuffer` contenant un `Vec<u8>`, et le `ImageBuffer` implémente la méthode `into_vec`, qui retourne le `Vec<u8>` :

```rust
fn combine_images(image_1: DynamicImage, image_2: DynamicImage) -> Vec<u8> {
  let vec_1 = image_1.to_rgba8().into_vec();
  let vec_2 = image_2.to_rgba8().into_vec();

  alternate_pixels(vec_1, vec_2)
}

```

Ensuite, les variables `vec_1` et `vec_2` sont passées à la fonction `alternate_pixels` qui retourne les données d'image combinées en alternant les ensembles de pixels RGBA des deux images :

```rust
fn alternate_pixels(vec_1: Vec<u8>, vec_2: Vec<u8>) -> Vec<u8> {
  // Un Vec<u8> est créé avec la même longueur que vec_1
  let mut combined_data = vec![0u8; vec_1.len()];

  let mut i = 0;
  while i < vec_1.len() {
    if i % 8 == 0 {
      combined_data.splice(i..=i + 3, set_rgba(&vec_1, i, i + 3));
    } else {
      combined_data.splice(i..=i + 3, set_rgba(&vec_2, i, i + 3));
    }
    i += 4;
  }

  combined_data
}

```

La fonction `set_rgba` prend une référence à un `Vec<u8>`, et retourne l'ensemble de pixels RGBA pour ce `Vec<u8>` commençant et se terminant à un index donné :

```rust
fn set_rgba(vec: &Vec<u8>, start: usize, end: usize) -> Vec<u8> {
  let mut rgba = Vec::new();
  for i in start..=end {
    let val = match vec.get(i) {
      Some(d) => *d,
      None => panic!("Index out of bounds"),
    };
    rgba.push(val);
  }
  rgba
}

```

La syntaxe `..=` est la syntaxe de plage de Rust qui permet à la plage d'être inclusive de la valeur de fin. Le symbole `*` avant une variable est l'opérateur de déréférencement de Rust, qui permet d'accéder à la valeur de la variable.

Ensuite, attribuez le retour de `combine_images` à la variable `combined_data` :

```rust
fn main() -> Result<(), ImageDataErrors> {
  // ...
  let combined_data = combine_images(image_1, image_2);
  Ok(())
}

```

#### Étape 10 – Attacher les Données Combinées à l'Image Flottante

Pour définir les données de `combined_data` dans l'image `output`, une méthode sur `FloatingImage` est définie pour définir le champ `data` de `output` à la valeur de `combined_data`.

Jusqu'à présent, vous n'avez implémenté que des fonctions sur des structures. Les méthodes sont définies de manière similaire, mais elles prennent une instance de la structure comme premier argument :

```rust
struct MyStruct {
  name: String,
}
impl MyStruct {
  fn change_name(&mut self, new_name: &str) {
    self.name = new_name.to_string();
  }
}

let mut my_struct = MyStruct { name: String::from("Shaun") };
// my_struct.name == "Shaun"
my_struct.change_name("Tom");
// my_struct.name == "Tom"

```

Puisque vous devez changer la valeur de l'instance de `FloatingImage`, la méthode `set_data` prend une référence mutable à l'instance comme premier argument.

```rust
impl FloatingImage {
  // ...
  fn set_data(&mut self, data: Vec<u8>) -> Result<(), ImageDataErrors> {
    // Si le tampon précédemment assigné est trop petit pour contenir les nouvelles données
    if data.len() > self.data.capacity() {
      return Err(ImageDataErrors::BufferTooSmall);
    }
    self.data = data;
    Ok(())
  }
}

```

L'énumération doit être étendue pour inclure la nouvelle variante unitaire `BufferTooSmall` :

```rust
enum ImageDataErrors {
  // ...
  BufferTooSmall,
}

```

_Remarque :_ La méthode est toujours appelée avec un seul argument :

```rust
fn main() -> Result<(), ImageDataErrors> {
  // ...
  output.set_data(combined_data)?;
  Ok(())
}

```

La syntaxe `?` à la fin d'une expression est un moyen abrégé de gérer le résultat d'un appel de fonction. Si l'appel de fonction retourne une erreur, l'opérateur de _propagation d'erreur_ retournera l'erreur de l'appel de fonction.

#### Étape 11 – Écrire l'Image dans un Fichier

Enfin, sauvegardez la nouvelle image dans un fichier. La crate `image` dispose d'une fonction `save_buffer_with_format` prenant la forme suivante :

```rust
fn save_buffer_with_format(
    path: AsRef<Path>,
    buf: &[u8],
    width: u32,
    height: u32,
    color: image::ColorType,
    format: image::ImageFormat
  ) -> image::ImageResult<()>;

```

Voyant que `AsRef` est implémenté pour `String`, vous pouvez utiliser un argument de type `String` pour le `path`.

```rust
fn main() -> Result<(), ImageDataErrors> {
  // ...
  image::save_buffer_with_format(
    output.name,
    &output.data,
    output.width,
    output.height,
    image::ColorType::Rgba8,
    image_1_format,
  )
  .unwrap();
  Ok(())
}

```

#### Étape 12 – Tout Rassembler

Voici le code final :

```rust
mod args;

use args::Args;
use image::{
  imageops::FilterType::Triangle, io::Reader, DynamicImage, GenericImageView, ImageFormat,
};

fn main() -> Result<(), ImageDataErrors> {
  let args = Args::new();
  println!("{:?}", args);

  let (image_1, image_1_format) = find_image_from_path(args.image_1);
  let (image_2, image_2_format) = find_image_from_path(args.image_2);

  if image_1_format != image_2_format {
    return Err(ImageDataErrors::DifferentImageFormats);
  }

  let (image_1, image_2) = standardise_size(image_1, image_2);
  let mut output = FloatingImage::new(image_1.width(), image_1.height(), args.output);

  let combined_data = combine_images(image_1, image_2);

  output.set_data(combined_data)?;

  image::save_buffer_with_format(
    output.name,
    &output.data,
    output.width,
    output.height,
    image::ColorType::Rgba8,
    image_1_format,
  )
  .unwrap();
  Ok(())
}

enum ImageDataErrors {
  BufferTooSmall,
  DifferentImageFormats,
}

struct FloatingImage {
  width: u32,
  height: u32,
  data: Vec<u8>,
  name: String,
}

impl FloatingImage {
  fn new(width: u32, height: u32, name: String) -> Self {
    let buffer_capacity = 3_655_744;
    let buffer: Vec<u8> = Vec::with_capacity(buffer_capacity);
    FloatingImage {
      width,
      height,
      data: buffer,
      name,
    }
  }
  fn set_data(&mut self, data: Vec<u8>) -> Result<(), ImageDataErrors> {
    if data.len() > self.data.capacity() {
      return Err(ImageDataErrors::BufferTooSmall);
    }
    self.data = data;
    Ok(())
  }
}

fn find_image_from_path(path: String) -> (DynamicImage, ImageFormat) {
  let image_reader = Reader::open(path).unwrap();
  let image_format = image_reader.format().unwrap();
  let image = image_reader.decode().unwrap();
  (image, image_format)
}

fn standardise_size(image_1: DynamicImage, image_2: DynamicImage) -> (DynamicImage, DynamicImage) {
  let (width, height) = get_smallest_dimensions(image_1.dimensions(), image_2.dimensions());
  println!("width: {}, height: {}\n", width, height);
  if image_2.dimensions() == (width, height) {
    (image_1.resize_exact(width, height, Triangle), image_2)
  } else {
    (image_1, image_2.resize_exact(width, height, Triangle))
  }
}

fn get_smallest_dimensions(dim_1: (u32, u32), dim_2: (u32, u32)) -> (u32, u32) {
  let pix_1 = dim_1.0 * dim_1.1;
  let pix_2 = dim_2.0 * dim_2.1;
  return if pix_1 < pix_2 { dim_1 } else { dim_2 };
}

fn combine_images(image_1: DynamicImage, image_2: DynamicImage) -> Vec<u8> {
  let vec_1 = image_1.to_rgba8().into_vec();
  let vec_2 = image_2.to_rgba8().into_vec();

  alternate_pixels(vec_1, vec_2)
}

fn alternate_pixels(vec_1: Vec<u8>, vec_2: Vec<u8>) -> Vec<u8> {
  let mut combined_data = vec![0u8; vec_1.len()];

  let mut i = 0;
  while i < vec_1.len() {
    if i % 8 == 0 {
      combined_data.splice(i..=i + 3, set_rgba(&vec_1, i, i + 3));
    } else {
      combined_data.splice(i..=i + 3, set_rgba(&vec_2, i, i + 3));
    }
    i += 4;
  }

  combined_data
}

fn set_rgba(vec: &Vec<u8>, start: usize, end: usize) -> Vec<u8> {
  let mut rgba = Vec::new();
  for i in start..=end {
    let val = match vec.get(i) {
      Some(d) => *d,
      None => panic!("Index out of bounds"),
    };
    rgba.push(val);
  }
  rgba
}

```

Construction du binaire :

```bash
$ cargo build --release

```

Création d'une image combinée, en utilisant les images dans [`freeCodeCamp/Rust-In-Replit`](https://github.com/freeCodeCamp/Rust-In-Replit) :

```bash
$ ./target/release/combiner images/pro.png images/fcc_glyph.png images/output.png

```

Et voici le résultat dans `images/output.png` :

![Image combinée de sortie](https://www.freecodecamp.org/news/content/images/2021/11/output.png)

## Conclusion

Avec cela, vous connaissez maintenant les bases de Rust.

Il reste encore beaucoup à apprendre. Alors, surveillez cet espace pour plus de contenu 😉.