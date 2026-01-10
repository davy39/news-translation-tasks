---
title: Que sont les durées de vie (lifetimes) en Rust ? Explications avec des exemples
  de code
date: '2024-09-06T20:03:57.375Z'
author: Oduah Chigozie
authorURL: https://www.freecodecamp.org/news/author/GhoulKingR/
originalURL: https://freecodecamp.org/news/what-are-lifetimes-in-rust-explained-with-code-examples
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725652969333/ba8a3fb6-3ac8-40e0-91e6-3e32e7f7b4b4.jpeg
tags:
- name: Rust
  slug: rust
- name: rust lang
  slug: rust-lang
seo_desc: 'Lifetimes are fundamental mechanisms in Rust. There''s a very high chance
  you''ll need to work with lifetimes in any Rust project that has any sort of complexity.

  Even though they are important to Rust projects, lifetimes can be quite tricky to
  wrap yo...'
---


Les durées de vie (lifetimes) sont des mécanismes fondamentaux en Rust. Il y a de fortes chances que vous deviez manipuler les durées de vie dans n'importe quel projet Rust d'une certaine complexité.

<!-- more -->

Bien qu'elles soient importantes pour les projets Rust, les durées de vie peuvent être assez difficiles à appréhender. J'ai donc créé ce guide pour clarifier ce qu'elles sont et quand vous devriez les utiliser.

### Prérequis pour ce tutoriel

Pour tirer le meilleur parti de ce tutoriel, vous aurez besoin des éléments suivants :

-   Une connaissance de Rust au moins de niveau débutant : Ce tutoriel n'aide pas à apprendre à coder en Rust. Il aide uniquement à comprendre les durées de vie en Rust et leur fonctionnement.
    
-   Une familiarité avec les génériques : Les génériques en Rust fonctionnent de la même manière que dans les langages de programmation populaires. Une connaissance du fonctionnement des génériques dans n'importe quel langage serait utile.
    
-   Savoir comment fonctionne le borrow checker n'est pas autant un prérequis que les deux points précédents, mais cela serait utile. La connaissance du fonctionnement des durées de vie aide également à comprendre comment fonctionne le borrow checker.
    

## Alors, que sont les durées de vie (lifetimes) en Rust ?

Pour que le [borrow checker][1] de Rust puisse garantir la sécurité de votre code, il doit savoir combien de temps toutes les données du programme vivront pendant son exécution. Cela devient difficile dans certaines situations, et c'est là que vous devez utiliser des annotations de durée de vie explicites.

Les durées de vie en Rust sont des mécanismes permettant de s'assurer que tous les emprunts (borrows) qui se produisent dans votre code sont valides. La durée de vie d'une variable correspond au temps pendant lequel elle vit au cours de l'exécution du programme, en commençant par son initialisation et en se terminant par sa destruction.

Le borrow checker peut détecter les durées de vie des variables dans de nombreux cas. Mais lorsqu'il ne le peut pas, vous devez l'aider avec des annotations de durée de vie explicites.

La syntaxe pour les annotations de durée de vie explicites est une apostrophe suivie d'un ensemble de caractères pour l'identification (par exemple, `'static`, `'a`) comme dans :

```
max<'a>
```

L'annotation de durée de vie indique que `max` doit vivre au plus aussi longtemps que `'a`.

L'utilisation de plusieurs durées de vie suit la même syntaxe :

```
max<'a, 'b>
```

Dans ce cas, les annotations de durée de vie indiquent que `max` doit vivre au plus aussi longtemps que `'a` et `'b`.

Les annotations de durée de vie explicites sont gérées de manière similaire aux génériques. Jetons un coup d'œil à un exemple :

```
fn max<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    // return the longest string out of the two
}
```

Dans l'exemple, les annotations de durée de vie indiquent que `max` doit vivre au plus aussi longtemps que les durées de vie de `s1` ou `s2`. Elles indiquent également que `max` renvoie une référence qui vit aussi longtemps que `s1`.

Un projet Rust comporte de nombreux cas nécessitant des annotations de durée de vie explicites, et dans les sections suivantes, nous allons passer en revue chacun d'entre eux.

## Annotations de durée de vie dans les fonctions

Une fonction n'a besoin d'une annotation de durée de vie explicite que lorsqu'elle renvoie une référence provenant de l'un de ses arguments. Prenons un exemple :

```
fn max<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}
```

Si vous supprimez les annotations de durée de vie, vous recevrez un avertissement du LSP (Language Server Protocol) vous demandant d'inclure les annotations de durée de vie. Si vous ignorez le message d'avertissement du LSP et compilez le code, vous obtiendrez le même message sous forme d'erreur du compilateur. Par exemple :

```
fn max(s1: &str, s2: &str) -> &str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

/**
 * Output ->
 *
error[E0106]: missing lifetime specifier
  --> src/main.rs:44:31
   |
44 | fn max(s1: &str, s2: &str) -> &str {
   |            ----      ----     ^ expected named lifetime parameter
   |
   = help: this function's return type contains a borrowed value, but the signature does not say whether it is borrowed from `s1` or `s2`
help: consider introducing a named lifetime parameter
   |
44 | fn max<'a>(s1: &'a str, s2: &'a str) -> &'a str {
   |       ++++      ++           ++          ++

For more information about this error, try `rustc --explain E0106`.
error: could not compile `lifetime-test` (bin "lifetime-test") due to 1 previous error
 ***********************
 */
```

D'un autre côté, une fonction n'a pas besoin de durées de vie explicites si elle ne renvoie pas de référence parmi ses arguments. Par exemple :

```
fn print_longest(s1: &str, s2: &str) {
    if s1.len() > s2.len() {
        println!("{s1} is longer than {s2}")
    } else {
        println!("{s2} is longer than {s1}")
    }
}
```

Une fonction renvoyant une valeur différente n'a pas non plus besoin d'annotations de durée de vie explicites :

```
fn join_strs(s1: &str, s2: &str) -> String {
    let mut joint_string = String::from(s1);
    joint_string.push_str(s2);
    return joint_string;
}
```

Vous ne devez spécifier les durées de vie que si une fonction renvoie une référence provenant de l'un de ses arguments qui est une référence empruntée.

## Annotations de durée de vie dans les structures

Les structures nécessitent des annotations de durée de vie explicites lorsque l'un de leurs champs est une référence. Cela permet au borrow checker de s'assurer que les références dans les champs de la structure vivent plus longtemps que la structure elle-même. Par exemple :

```
struct Strs<'a, 'b> {
    x: &'a str,
    y: &'b str,
}
```

Sans les annotations de durée de vie, vous obtiendrez un message d'erreur du LSP et du compilateur similaire à celui de la section précédente :

```
struct OtherStruct {
    x: &str,
    y: &str,
}

/**
* Output ->
**********************
error[E0106]: missing lifetime specifier
 --> src/main.rs:7:8
  |
7 |     x: &str,
  |        ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
6 ~ struct OtherStruct<'a> {
7 ~     x: &'a str,
  |

error[E0106]: missing lifetime specifier
 --> src/main.rs:8:8
  |
8 |     y: &str,
  |        ^ expected named lifetime parameter
  |
help: consider introducing a named lifetime parameter
  |
6 ~ struct OtherStruct<'a> {
7 |     x: &str,
8 ~     y: &'a str,
  |

For more information about this error, try `rustc --explain E0106`.
error: could not compile `lifetime-test` (bin "lifetime-test") due to 2 previous errors
**********************
*/
```

## Annotations de durée de vie dans les méthodes

Les annotations de durée de vie concernant les méthodes peuvent être effectuées sur des méthodes autonomes, des blocs `impl` ou des traits. Examinons chacun d'entre eux :

### Méthodes autonomes

L'annotation des durées de vie sur les méthodes autonomes est identique à l'annotation des durées de vie dans les fonctions :

```
impl Struct {
    fn max<'a>(self: &Self, s1: &'a str, s2: &'a str) -> &'a str {
        if s1.len() > s2.len() {
            s1
        } else {
            s2
        }
    }
}
```

### Blocs `impl`

L'écriture d'annotations de durée de vie explicites pour les blocs `impl` est requise si la structure à laquelle il est associé possède des annotations de durée de vie dans sa définition. Voici la syntaxe pour écrire des blocs `impl` avec des annotations de durée de vie explicites :

```
struct Struct<'a> {
}

impl<'a> Struct<'a> {
}
```

Cela permet à n'importe quelle méthode que vous écrivez dans le bloc `impl` de renvoyer une référence provenant de `Struct`. Par exemple :

```
struct Strs<'a> {
    x: &'a str,
    y: &'a str,
}

impl<'a> Strs<'a> {
    fn max(self: &Self) -> &'a str {
        if self.y.len() > self.x.len() {
            self.y
        } else {
            self.x
        }
    }
}
```

### Traits

Les annotations de durée de vie dans les traits dépendent des méthodes définies par le trait.

Regardons un exemple. Une méthode à l'intérieur d'une définition de trait peut utiliser des annotations de durée de vie explicites comme une méthode autonome, et la définition du trait ne nécessitera pas d'annotations de durée de vie explicites. Comme ceci :

```
trait Max {
    fn longest_str<'a>(s1: &'a str, s2: &'a str) -> &'a str;
}

impl<'a> Max for Struct<'a> {
    fn longest_str(s1: &'a str, s2: &'a str) {
        if s1.len() > s2.len() {
            s1
        } else {
            s2
        }
    }
}
```

Si une méthode de trait nécessite des références de la structure à laquelle elle est associée, la définition du trait nécessitera des annotations de durée de vie explicites. Par exemple :

```
trait Max<'a> {
    fn max(self: &Self) -> &'a str;
}
```

Ce qui peut être implémenté de cette façon :

```
struct Strs<'a> {
    x: &'a str,
    y: &'a str,
}

trait Max<'a> {
    fn max(self: &Self) -> &'a str;
}

impl<'a> Max<'a> for Strs<'a> {
    fn max(self: &Self) -> &'a str {
        if self.y.len() > self.x.len() {
            self.y
        } else {
            self.x
        }
    }
}
```

## Annotations de durée de vie dans les enums

Tout comme les structures, les enums ont besoin d'annotations de durée de vie explicites si l'un de leurs champs est une référence. Par exemple :

```
enum Either<'a> {
    Str(String),
    Ref(&'a String),
}
```

## La durée de vie `'static`

Dans de nombreux projets Rust, vous avez probablement rencontré des variables ayant une durée de vie `'static`. Dans cette section, nous allons passer en revue ce qu'est une durée de vie `'static`, comment elle fonctionne et où elle est couramment utilisée.

`'static` est un nom de durée de vie réservé en Rust. Il signifie que les données vers lesquelles pointe une référence vivent depuis leur initialisation jusqu'à la fin du programme. Cela diffère légèrement des variables statiques, qui sont stockées directement dans le fichier binaire du programme. Cependant, toutes les variables statiques ont une durée de vie `'static`.

Les variables avec des durées de vie `'static` peuvent être créées au moment de l'exécution. Mais elles ne peuvent pas être supprimées (dropped), seulement contraintes à des durées de vie plus courtes. Par exemple :

```
// The lifetime annotation 'a is the shorter lifetime of the
// two arguments s1 and s2
fn max<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

fn main() {
    let first = "First string"; // Longer lifetime

    {
        let second = "Second string"; // Shorter lifetime

        // In the max function, the lifetime of first is
        // coerced into the lifetime of second
        println!("The biggest of {} and {} is {}", first, second, max(first, second));
    };
}
```

Les chaînes littérales sont des exemples de valeurs ayant des durées de vie `'static`. Elles sont également stockées dans le fichier binaire du programme et peuvent être créées au moment de l'exécution.

Rust vous permet de déclarer des variables statiques avec le mot-clé `static`, en utilisant cette syntaxe :

```
static IDENTIFIER: &'static str = "value";
```

Les variables statiques peuvent être déclarées dans n'importe quelle portée, y compris la portée globale. Cela signifie que vous pouvez utiliser des variables statiques comme variables globales. Par exemple :

```
static FIRST_NAME: &'static str = "John";
static LAST_NAME: &'static str = "Doe";

fn main() {
    println!("First name: {}", FIRST_NAME);
    println!("Last name: {}", LAST_NAME);
}
```

Les variables statiques peuvent également être mutables ou immuables. Mais travailler avec des variables statiques mutables n'est autorisé que dans des blocs `unsafe` car elles ne sont pas sûres.

```
static mut FIRST_NAME: &'static str = "John";
static LAST_NAME: &'static str = "Doe";

fn main() {
    unsafe {
        println!("First name: {}", FIRST_NAME);
    }
    println!("Last name: {}", LAST_NAME);
    unsafe {
        FIRST_NAME = "Jane";
        println!("First name changed to: {}", FIRST_NAME);
    }
}
```

## Résumé

Les durées de vie en Rust aident le borrow checker à s'assurer que toutes les références empruntées sont valides. Le borrow checker peut détecter les durées de vie des variables dans de nombreux cas, mais lorsqu'il ne le peut pas, vous devez l'aider avec des annotations de durée de vie explicites.

Les annotations de durée de vie explicites sont ces éléments `'a`, `'b` et `'static` que vous voyez dans de nombreux projets Rust. Vous ne devez les utiliser que dans les structures (structs, enums, traits et impls) qui manipulent des références, et dans les fonctions ou méthodes qui reçoivent et renvoient des références.

Dans ce guide, vous avez découvert les annotations de durée de vie explicites et vu quelques exemples de la manière de les utiliser. J'espère que cela vous a apporté de la clarté sur le sujet et vous a aidé à mieux comprendre les durées de vie.

Merci de m'avoir lu !

[1]: https://doc.rust-lang.org/rust-by-example/scope/borrow.html