---
title: Les macros procédurales en Rust – Un guide pour débutants
date: '2024-04-24T17:49:17.000Z'
author: Anshul Sanghi
authorURL: https://www.freecodecamp.org/news/author/anshulsanghi/
originalURL: https://freecodecamp.org/news/procedural-macros-in-rust
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Procedural-Macros-in-Rust-Cover--1-.png
tags:
- name: handbook
  slug: handbook
- name: Rust
  slug: rust
seo_desc: 'In this handbook, you''ll learn about procedural macros in Rust, and what
  purposes they serve. You''ll also learn how to write your own procedural macros
  with both hypothetical and real-world examples.

  This guide assumes that you''re familiar with Rust ...'
---


Dans ce manuel, vous découvrirez les macros procédurales en Rust et leur utilité. Vous apprendrez également à écrire vos propres macros procédurales à l'aide d'exemples hypothétiques et concrets.

<!-- more -->

Ce guide suppose que vous êtes familier avec Rust et ses concepts de base, tels que les types de données, les itérateurs et les traits. Si vous avez besoin d'établir ou de réviser vos bases en Rust, [consultez ce cours interactif][1].

Aucune connaissance préalable des macros n'est requise, car cet article couvre tout depuis le début.

## Table des matières

1.  [Que sont les macros en Rust ?][2]
    1.  [Les types de macros en Rust][3]
    2.  [Les types de macros procédurales][4]
2.  [Prérequis][5]
    1.  [Dépendances utiles][6]
3.  [Comment écrire une macro de dérivation simple][7]
    1.  [La macro de dérivation `IntoStringHashMap`][8]
    2.  [Comment déclarer une macro de dérivation][9]
    3.  [Comment analyser l'entrée de la macro][10]
    4.  [Comment garantir une cible de type struct pour la macro][11]
    5.  [Comment générer le code de sortie][12]
    6.  [Comment utiliser votre macro de dérivation][13]
    7.  [Comment améliorer notre implémentation][14]
4.  [Une macro de dérivation plus élaborée][15]
    1.  [La macro `DeriveCustomModel`][16]
    2.  [Comment séparer l'implémentation de la déclaration][17]
    3.  [Comment analyser les arguments d'une macro de dérivation][18]
    4.  [Comment implémenter `DeriveCustomModel`][19]
    5.  [Comment générer chaque modèle personnalisé][20]
    6.  [Comment utiliser votre macro `DeriveCustomModal`][21]
5.  [Une macro d'attribut simple][22]
    1.  [L'attribut `log_duration`][23]
    2.  [Comment déclarer une macro d'attribut][24]
    3.  [Comment implémenter la macro d'attribut `log_duration`][25]
    4.  [Comment utiliser votre macro `log_duration`][26]
6.  [Une macro d'attribut plus élaborée][27]
    1.  [L'attribut `cached_fn`][28]
    2.  [Comment implémenter la macro d'attribut `cached_fn`][29]
    3.  [Arguments de l'attribut `cached_fn`][30]
    4.  [Comment utiliser la macro `cached_fn`][31]
7.  [Une macro de type fonction simple][32]
    1.  [La macro `constant_string`][33]
    2.  [Comment déclarer une macro de type fonction][34]
    3.  [Comment implémenter la macro `constant_string`][35]
    4.  [Comment utiliser la macro `constant_string`][36]
8.  [Une macro de type fonction plus élaborée][37]
    1.  [La macro `hash_mapify`][38]
    2.  [Comment implémenter la macro `hash_mapify`][39]
    3.  [Comment analyser l'entrée de `hash_mapify`][40]
    4.  [Comment générer le code de sortie][41]
    5.  [Comment convertir des types de données personnalisés en tokens de sortie][42]
    6.  [Comment utiliser la macro `hash_mapify`][43]
9.  [Au-delà de l'écriture de macros][44]
    1.  [Crates et outils utiles][45]
10.  [Inconvénients des macros][46]
    1.  [Débogage (ou son absence)][47]
    2.  [Coûts au temps de compilation][48]
    3.  [Manque d'autocomplétion et de vérifications de code][49]
    4.  [Où tracer la limite ?][50]
11.  [Conclusion][51]
    1.  [Vous aimez mon travail ?][52]

## **Que sont les macros en Rust ?**

Les macros font partie intégrante du langage de programmation Rust. On ne tarde pas à les rencontrer dès l'apprentissage du langage.

Dans leur forme la plus simple, les macros en Rust vous permettent d'exécuter du code au moment de la compilation. Rust permet pratiquement de faire tout ce que l'on veut en ce qui concerne les macros et leurs possibilités. Le cas d'utilisation le plus courant de cette fonctionnalité est l'écriture de code qui génère d'autre code.

Les macros sont un moyen d'étendre les fonctionnalités du compilateur au-delà de ce qui est supporté en standard. Que vous souhaitiez générer du code basé sur du code existant, ou transformer du code existant sous une certaine forme, les macros sont votre outil de prédilection.

Voici comment le livre officiel de Rust les décrit :

> Le terme _macro_ fait référence à une famille de fonctionnalités en Rust.
> 
> Fondamentalement, les macros sont un moyen d'écrire du code qui écrit d'autre code, ce que l'on appelle la _métaprogrammation_.
> 
> La métaprogrammation est utile pour réduire la quantité de code que vous devez écrire et maintenir, ce qui est également l'un des rôles des fonctions. Cependant, les macros ont des pouvoirs supplémentaires que les fonctions n'ont pas.

En utilisant des macros, vous pouvez également ajouter dynamiquement des éléments qui doivent être ajoutés au moment de la compilation, ce qui n'est pas possible avec les fonctions puisqu'elles sont appelées au moment de l'exécution. L'une de ces fonctionnalités est, par exemple, l'implémentation de _Traits_ sur des types, qui doit être effectuée au moment de la compilation.

Un autre avantage des macros est qu'elles peuvent être très flexibles, car elles peuvent prendre une quantité dynamique de paramètres ou d'entrées, contrairement à une fonction.

Les macros ont leur propre syntaxe, tant pour l'écriture que pour l'utilisation, que nous explorerons en détail dans les sections suivantes.

Quelques exemples d'utilisation des macros aident à comprendre leur puissance :

-   Le projet **SQLx** utilise des macros pour vérifier toutes vos requêtes et instructions SQL (tant que vous les avez créées à l'aide de la macro fournie) au moment de la compilation en les exécutant réellement contre une instance de base de données en cours d'exécution (oui, au moment de la compilation).
-   **typed\_html** implémente un analyseur HTML complet avec validation au moment de la compilation, tout en utilisant la syntaxe familière JSX.

## Les types de macros en Rust

En Rust, il existe 2 types différents de macros : déclaratives et procédurales.

### Macros déclaratives

Les macros déclaratives fonctionnent sur la base de l'analyse syntaxique. Bien que la documentation officielle les définisse comme permettant d'écrire des extensions de syntaxe, je pense qu'il est plus intuitif de les considérer comme une version avancée du mot-clé `match` pour le compilateur.

Vous pouvez définir un ou plusieurs motifs (patterns) à faire correspondre, et leur corps doit retourner le code Rust de sortie que vous souhaitez que la macro produise.

Nous n'allons pas en parler dans cet article, mais si vous souhaitez en savoir plus, [ceci][53] est un bon point de départ.

### Macros procédurales

Ces macros, dans leurs cas d'utilisation les plus basiques, exécutent n'importe quel code Rust que vous voulez au moment de la compilation. La seule exigence est qu'elles doivent prendre du code Rust en entrée et retourner du code Rust en sortie.

Il n'y a pas d'analyse syntaxique spéciale impliquée pour écrire ces macros (sauf si vous souhaitez le faire), c'est pourquoi elles sont personnellement plus faciles à comprendre et à écrire pour moi.

Les macros procédurales sont divisées en 3 catégories : les macros de dérivation (derive), les macros d'attribut et les macros fonctionnelles.

### Les types de macros procédurales

#### Macros de dérivation (derive)

Les macros de dérivation sont, généralement parlant, appliquées aux types de données en Rust. Elles sont un moyen d'étendre la déclaration d'un type pour en "dériver" automatiquement des fonctionnalités.

Vous pouvez les utiliser pour générer des types "dérivés" à partir d'un type, ou comme moyen d'implémenter automatiquement des méthodes sur le type de données cible. Cela devrait prendre tout son sens avec l'exemple ci-dessous.

Afficher des types de données non primitifs, tels que des structures, des énumérations ou même des erreurs, à des fins de débogage est une fonctionnalité très courante dans n'importe quel langage, pas seulement Rust. En Rust, seuls les types primitifs ont implicitement la capacité d'être affichés dans des contextes de "débogage".

Si vous considérez que tout en Rust n'est que traits (même les opérations de base comme l'addition et l'égalité), cela est logique. Vous voulez pouvoir afficher vos types de données personnalisés pour le débogage, mais Rust n'a aucun moyen de dire "veuillez appliquer ce trait à chaque type de données existant dans le code, pour toujours".

C'est là qu'intervient la macro de dérivation `Debug`. Il existe une manière standard d'afficher chaque type de structure de données en Rust qu'il utilise pour ses types internes. La macro `Debug` vous permet d'implémenter automatiquement le trait `Debug` pour vos types personnalisés, tout en suivant les mêmes règles et guide de style que l'implémentation pour les types de données internes.

```
// Exemples de macros de dérivation

/// Exemple pour dériver des méthodes sur des types de données
#[derive(Debug)]
pub struct User {
    username: String,
    first_name: String,
    last_name: String,
}
```

La macro de dérivation `Debug` produira le code suivant (présentation simplifiée, pas exacte) :

```
impl core::fmt::Debug for User {
    fn fmt(&self, f: &mut core::fmt::Formatter) -> core::fmt::Result {
        f.debug_struct(
            "User"
        )
        .field("username", &self.username)
        .field("first_name", &self.first_name)
        .field("last_name", &self.last_name)
        .finish()
    }
}
```

Comme vous pouvez le constater, personne ne veut écrire ce code pour toutes ses structures et énumérations personnalisées encore et encore. Cette simple macro vous donne un aperçu de la puissance des macros en Rust, ainsi que de la raison pour laquelle elles sont une partie essentielle du langage lui-même.

Lors de la compilation réelle, le même code donnerait le résultat suivant :

```
pub struct User {
    username: String,
    first_name: String,
    last_name: String,
}

impl core::fmt::Debug for User {
    fn fmt(&self, f: &mut core::fmt::Formatter) -> ::core::fmt::Result {
        f.debug_struct(
            "User"
        )
        .field("username", &self.username)
        .field("first_name", &self.first_name)
        .field("last_name", &self.last_name)
        .finish()
    }
}
```

Remarquez comment la déclaration du type original est préservée dans le code de sortie. C'est l'une des principales différences entre les macros de dérivation et les autres. Les macros de dérivation préservent le type d'entrée sans modifications. Elles ajoutent seulement du code supplémentaire à la sortie. En revanche, toutes les autres macros ne se comportent pas de la même manière. Elles ne préservent la cible que si la sortie de la macro elle-même inclut également la cible.

#### Macros d'attribut

Les macros d'attribut, en plus des types de données, sont généralement appliquées à des blocs de code tels que des fonctions, des blocs impl, des blocs inline, etc. Elles sont généralement utilisées soit pour transformer le code cible d'une manière ou d'une autre, soit pour l'annoter avec des informations supplémentaires.

Le cas d'utilisation le plus courant consiste à modifier une fonction pour lui ajouter des fonctionnalités ou une logique supplémentaire. Par exemple, vous pouvez facilement écrire une macro d'attribut qui :

-   Journalise (log) tous les paramètres d'entrée et de sortie
-   Journalise le temps d'exécution total de la fonction
-   Compte le nombre de fois que cette fonction est appelée
-   Ajoute des champs prédéterminés à n'importe quelle structure

et ainsi de suite.

Toutes les choses que j'ai mentionnées ci-dessus, et bien plus encore, combinées forment la macro `instrument` incroyablement populaire et utile en Rust fournie par la crate `tracing`. Bien sûr, je simplifie massivement ici, mais c'est suffisant comme exemple.

Si vous avez l'habitude d'utiliser Clippy, il vous a peut-être déjà suggéré d'ajouter l'attribut `#[must_use]` à votre fonction ou méthode.

C'est un exemple de macro utilisée pour annoter la fonction avec des informations supplémentaires. Elle indique au compilateur d'avertir l'utilisateur si la valeur de retour de cet appel de fonction n'est pas utilisée. Le type `Result` est déjà annoté avec `#[must_use]` par défaut, c'est pourquoi vous voyez l'avertissement `Unused Result<...> that must be used` lorsque vous n'utilisez pas une valeur de retour de type `Result`.

Les macros d'attribut sont également ce qui alimente la [compilation conditionnelle][54] en Rust.

#### Macros fonctionnelles

Les macros fonctionnelles sont des macros déguisées en fonctions. Ce sont les types de macros procédurales les moins restrictifs, car elles peuvent être utilisées littéralement n'importe où, tant qu'elles produisent du code valide dans le contexte où elles sont utilisées.

Ces macros ne sont pas "appliquées" à quoi que ce soit contrairement aux deux autres, mais sont plutôt appelées comme vous appelleriez une fonction. En tant qu'arguments, vous pouvez littéralement passer tout ce que vous voulez, tant que votre macro sait comment l'analyser. Cela inclut tout, de l'absence d'arguments au code Rust valide, en passant par du charabia aléatoire que seule votre macro peut comprendre.

Elles sont en quelque sorte la version procédurale des macros déclaratives. Si vous avez besoin d'exécuter du code Rust et de pouvoir également analyser une syntaxe personnalisée, les macros fonctionnelles sont votre outil de prédilection. Elles sont également utiles si vous avez besoin d'une fonctionnalité de type macro dans des endroits où d'autres macros ne peuvent pas être utilisées.

Après cette longue description des informations de base concernant les macros, il est enfin temps de passer à l'écriture concrète de macros procédurales.

## Prérequis

Il existe certaines règles concernant l'écriture de vos propres macros procédurales que vous devrez suivre. Ces règles s'appliquent aux 3 types de macros procédurales. Elles sont :

-   Les macros procédurales ne peuvent être ajoutées qu'à un projet marqué comme `proc-macro` dans le `Cargo.toml`.
-   Les projets marqués comme tels ne peuvent rien exporter d'autre que des macros procédurales.
-   Les macros elles-mêmes doivent toutes être déclarées dans le fichier `lib.rs`.

Commençons par configurer notre projet avec ce code :

```
cargo new --bin my-app
cd my-app
cargo new --lib my-app-macros;
```

Cela créera un projet racine, ainsi qu'un sous-projet à l'intérieur qui hébergera nos macros. Vous devez apporter quelques modifications aux fichiers `Cargo.toml` de ces deux projets.

Tout d'abord, le fichier `Cargo.toml` pour `my-app-macros` doit avoir le contenu suivant (remarquez que vous devez déclarer une section lib qui possède la propriété `proc-macro`) :

```
# my-app/my-app-macros/Cargo.toml

[package]
name = "my-app-macros"
version = "0.1.0"
edition = "2021"

[lib]
name = "my_app_macros"
path = "src/lib.rs"
proc-macro = true

[dependencies]
```

Ensuite, le fichier `Cargo.toml` pour `my-app` doit avoir le contenu suivant :

```
# my-app/Cargo.toml

workspace = { members = ["my-app-macros"] }

[package]
name = "my-app"
version = "0.1.0"
edition = "2021"
resolver = "2"

# Voir plus de clés et leurs définitions sur https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
my-app-macros = { path = "./my-app-macros" }
```

Vous devez définir la version du résolveur de dépendances sur "2" et ajouter votre projet de macros comme dépendance du projet `my-app`.

### Dépendances utiles

Du point de vue du compilateur, voici comment fonctionnent les macros :

-   Elles prennent un flux de tokens (token stream) en entrée (et optionnellement un flux de tokens comme arguments pour la macro elle-même).
-   Elles retournent un flux de tokens en sortie.

C'est tout ce que le compilateur sait ! Et comme vous le verrez bientôt, c'est suffisant pour lui.

Cela crée cependant un problème. Vous devez être capable de donner un sens à ce "flux de tokens" de manière à les comprendre correctement, qu'il s'agisse de code Rust ou d'une syntaxe personnalisée, de pouvoir les modifier et également de les produire en sortie. Faire cela manuellement n'est pas une tâche facile, et pour les besoins de ce tutoriel, c'est hors de portée.

Nous pouvons cependant compter sur l'excellent travail open source réalisé par de nombreux développeurs pour nous faciliter la tâche. Vous devez ajouter quelques dépendances pour aider à résoudre ce problème :

-   `syn` — Un analyseur syntaxique pour Rust. Il vous aide à analyser le flux de tokens d'entrée en tant qu'AST Rust. L'AST (Arbre de Syntaxe Abstraite) est un concept que l'on rencontre principalement lorsqu'on essaie d'écrire son propre interpréteur ou compilateur, mais une compréhension de base est essentielle pour travailler avec les macros. Les macros, après tout, ne sont que des extensions que vous écrivez pour le compilateur en quelque sorte. Si vous souhaitez en savoir plus sur ce que sont les AST, [consultez cette introduction très utile][55].
-   `quote` — quote est, et c'est une énorme généralisation, une crate qui nous aide à effectuer l'opération inverse de ce que fait `syn`. Elle nous aide à convertir le code source Rust en un flux de tokens que nous pouvons renvoyer depuis notre macro.
-   `proc-macro2` — La bibliothèque standard fournit une crate `proc-macro`, mais les types qu'elle fournit ne peuvent pas exister en dehors des macros procédurales. `proc-macro2` est une enveloppe (wrapper) autour de la bibliothèque standard qui rend tous les types internes utilisables en dehors du contexte des macros. Cela permet, par exemple, à `syn` et `quote` d'être utilisés non seulement pour les macros procédurales, mais aussi dans du code Rust classique, si jamais vous en aviez besoin. Et nous l'utiliserons en effet intensivement si nous voulons tester unitairement nos macros ou leurs expansions.
-   `darling` — Il facilite l'analyse et la manipulation des arguments de macro, ce qui est autrement un processus fastidieux car il faut les extraire manuellement de l'arbre syntaxique. `darling` nous offre une capacité similaire à `serde` pour analyser automatiquement l'arbre des arguments d'entrée dans notre structure d'arguments. Il nous aide également dans la gestion des erreurs concernant les arguments invalides, les arguments requis, etc.

Bien que ces projets reçoivent des contributions de nombreux développeurs, je tiens à remercier tout particulièrement [David Tolnay][56]. C'est une légende de la communauté Rust et le créateur de la plupart de ces projets, ainsi que de nombreuses autres crates open source en Rust.

Ajoutons rapidement ces dépendances à notre projet et commençons à écrire notre macro :

```
// my-app-macros

cargo add syn quote proc-macro2 darling
```

## Comment écrire une macro de dérivation simple

Vous allez apprendre à écrire une macro `Derive` dans cette section. À ce stade, vous devriez déjà connaître les différents types de macros et ce qu'ils impliquent, comme nous en avons discuté dans les sections précédentes.

### La macro de dérivation `IntoStringHashMap`

Disons que vous avez une application où vous devez pouvoir convertir des structures en hash maps, utilisant le type `String` pour les clés et les valeurs. Cela signifie qu'elle devrait fonctionner avec n'importe quelle structure dont tous les champs sont convertibles en type `String` à l'aide du trait `Into`.

### Comment déclarer une macro de dérivation

Vous déclarez des macros en créant une fonction et en l'annotant à l'aide de macros d'attribut qui indiquent au compilateur de considérer cette fonction comme une déclaration de macro. Comme votre `lib.rs` est vide pour le moment, vous devez également déclarer `proc-macro2` en tant que crate externe :

```
// my-app-macros/src/lib.rs
extern crate proc_macro;

use proc_macro::TokenStream;

#[proc_macro_derive(IntoStringHashMap)]
pub fn derive_into_hash_map(item: TokenStream) -> TokenStream {
    todo!()
}
```

Tout ce que nous faisons ici est de déclarer notre macro comme une macro de dérivation avec l'identifiant `IntoStringHashMap`. Notez que le nom de la fonction n'est pas important ici. Ce qui est important, c'est l'identifiant passé à la macro d'attribut `proc_macro_derive`.

Voyons immédiatement comment vous pouvez l'utiliser – nous reviendrons terminer l'implémentation plus tard :

```
// my-app/src/main.rs

use my_app_macros::IntoStringHashMap;

#[derive(IntoStringHashMap)]
pub struct User {
    username: String,
    first_name: String,
    last_name: String,
    age: u32,
}

fn main() {

}
```

Vous pouvez simplement utiliser votre macro comme n'importe quelle autre macro de dérivation, en utilisant l'identifiant que vous avez déclaré (dans ce cas, c'était `IntoStringHashMap`).

Si vous essayez de compiler votre code à ce stade, vous devriez voir l'erreur de compilation suivante :

```
   Compiling my-app v0.1.0 

error: proc-macro derive panicked
 --> src/main.rs:3:10
  |
3 | #[derive(IntoHashMap)]
  |          ^^^^^^^^^^^
  |
  = help: message: not yet implemented

error: could not compile `my-app` (bin "my-app") due to 1 previous error
```

Cela prouve clairement que notre macro a été exécutée pendant l'étape de compilation car, si vous n'êtes pas familier avec la macro `todo!()`, elle panique avec le message `help: message: not yet implemented` lors de son exécution.

Cela signifie que tant la déclaration de notre macro que son utilisation fonctionnent. Nous pouvons maintenant passer à l'implémentation réelle de cette macro.

### Comment analyser l'entrée de la macro

Tout d'abord, vous analysez le flux de tokens d'entrée en tant que `DeriveInput` en utilisant `syn`, qui est une représentation de n'importe quelle cible avec laquelle vous pouvez utiliser une macro de dérivation :

```
let input = syn::parse_macro_input!(item as syn::DeriveInput);
```

`syn` nous fournit la macro `parse_macro_input` qui utilise une syntaxe quelque peu personnalisée pour ses arguments. Vous lui fournissez le nom de votre variable d'entrée, le mot-clé `as`, et le type de données dans `syn` sous lequel il doit analyser le flux de tokens d'entrée (dans notre cas, un `DeriveInput`).

Si vous examinez le code source de `DeriveInput`, vous verrez qu'il nous donne les informations suivantes :

-   `attrs` : Attributs appliqués à ce type, qu'il s'agisse d'autres macros d'attribut déclarées par nous, ou des attributs intégrés tels que `must_use`.
-   `vis` : Le spécificateur de visibilité pour cette déclaration de type.
-   `ident` : L'identifiant (nom) du type.
-   `generics` : Informations sur les paramètres génériques que ce type prend, y compris les durées de vie (lifetimes).
-   `data` : Une énumération qui décrit si la cible est une structure (struct), une énumération (enum) ou une union, et nous fournit également plus d'informations pour chacune d'elles.

Ces noms de champs et leurs types (à l'exception du champ data) sont assez standard pour les cibles supportées par `syn`, telles que les fonctions, les énumérations, etc.

Si vous allez plus loin dans la déclaration de l'énumération `Data`, et dans `DataStruct` en particulier, vous verrez qu'elle vous fournit un champ appelé `fields`. C'est une collection de tous les champs de cette structure et vous pouvez l'utiliser pour itérer sur eux. C'est exactement ce dont nous avons besoin pour construire notre hash map !

L'implémentation complète de cette macro ressemble à ceci :

```
// my-app/my-app-macros/lib.rs

extern crate proc_macro2;

use proc_macro::TokenStream;
use quote::quote;
use syn::Data;

#[proc_macro_derive(IntoHashMap)]
pub fn into_hash_map(item: TokenStream) -> TokenStream {
    let input = syn::parse_macro_input!(item as syn::DeriveInput);

    let struct_identifier = &input.ident;

    match &input.data {
        Data::Struct(syn::DataStruct { fields, .. }) => {
            let mut implementation = quote!{
                let mut hash_map = std::collections::HashMap::<String, String>::new();
            };

            for field in fields {
                let identifier = field.ident.as_ref().unwrap();
                implementation.extend(quote!{
                    hash_map.insert(stringify!(#identifier).to_string(), String::from(value.#identifier));
                });
            }

            quote! {
                #[automatically_derived]
                impl From<#struct_identifier> for std::collections::HashMap<String, String> {
                    fn from(value: #struct_identifier) -> Self {
                        #implementation

                        hash_map
                    }
                }
            }
        }
        _ => unimplemented!()
    }.into()
}
```

Il se passe beaucoup de choses ici, alors décomposons-les :

### Comment garantir une cible de type `struct` pour la macro

`let struct_identifier = &input.ident;` : Vous stockez l'identifiant de la structure dans une variable séparée, afin de pouvoir l'utiliser facilement plus tard.

```
match &input.data {
    Data::struct(syn::DataStruct { fields, .. }) => { ... },
    _ => unimplemented!()
}
```

Vous effectuez un filtrage par motif (match) sur le champ data analysé à partir de `DeriveInput`. S'il est de type `DataStruct` (une structure Rust), alors continuez, sinon paniquez, car la macro n'est pas implémentée pour les autres types.

### Comment générer le code de sortie

Jetons un coup d'œil à l'implémentation de la branche du match lorsque vous avez une `DataStruct` :

```
let mut implementation = quote!{
    let mut hash_map = std::collections::HashMap::<String, String>::new();
};
```

Ici, vous avez créé un nouveau `TokenStream` en utilisant `quote`. Ce `TokenStream` est différent de celui fourni par la bibliothèque standard, alors ne les confondez pas. Celui-ci doit être mutable, car nous y ajouterons bientôt plus de code.

`TokenStream` est fondamentalement la représentation inverse d'un AST. Vous fournissez du code Rust réel à la macro `quote`, et elle nous donne le "flux de tokens" pour ce code source.

Ce `TokenStream` peut soit être converti vers le type de sortie de la macro, soit être manipulé à l'aide de méthodes fournies par `quote` telles que `extend`.

En continuant,

```
for field in fields {
    let identifier = field.ident.as_ref().unwrap();
    implementation.extend(quote!{
        hash_map.insert(
            stringify!(#identifier).to_string(),
            String::from(value.#identifier)
        );
    });
}
```

Vous bouclez sur tous les champs. À chaque itération, vous créez d'abord une variable `identifier` pour contenir le nom du champ pour une utilisation ultérieure. Vous utilisez ensuite la méthode `extend` sur notre `TokenStream` précédemment créé pour lui ajouter du code supplémentaire.

La méthode `extend` prend simplement un autre `TokenStream`, qui peut facilement être généré à l'aide de la macro `quote`. Pour l'extension, vous écrivez simplement le code pour insérer une nouvelle entrée dans la `hash_map` qui sera créée dans la sortie de la macro.

Regardons cela de plus près :

```
hash_map.insert(
    stringify!(#identifier).to_string(),
    String::from(value.#identifier)
);
```

Comme vous le savez, la méthode `insert` prend une clé et une valeur. Vous avez indiqué au compilateur que la clé et la valeur sont de type `String`. `stringify` est une macro intégrée à la bibliothèque standard qui convertit n'importe quel type `Ident` en son équivalent `&str`. Vous l'utilisez ici pour convertir vos identifiants de champs en `&str` réels. Vous appelez ensuite la méthode `to_string()` dessus pour le convertir en type `String`.

Mais que représente le `#identifier` ?

`quote` vous offre la possibilité d'utiliser n'importe quelle variable déclarée en dehors du `TokenStream` à l'intérieur de celui-ci en utilisant le préfixe `#`. Considérez-le comme le `{}` dans les arguments de formatage. `#identifier` dans ce cas est simplement remplacé par l'identifiant du champ que nous avons déclaré en dehors de l'appel à `extend`. Ainsi, vous appelez essentiellement la macro `stringify!()` directement sur l'identifiant du champ.

De même, vous pouvez accéder à la valeur d'un champ en utilisant la syntaxe familière `variable_struct.nom_du_champ`, mais en utilisant la variable identifier à la place du nom du champ. C'est ce que vous faites lorsque vous passez la valeur à votre instruction d'insertion : `String::from(value.#identifier)`.

Si vous avez examiné le code de près, vous réaliserez d'où vient `value`, mais sinon, c'est simplement ce que la méthode d'implémentation du trait utilise pour déclarer son argument d'entrée plus bas.

Une fois que vous avez construit votre implémentation à l'aide de la boucle for pour chaque champ de la structure, vous avez un `TokenStream` qui, à des fins de représentation, contient le code suivant :

```
let mut hash_map = std::collections::HashMap::<String, String>::new();
hash_map.insert("username".to_string(), String::from(value.username));
hash_map.insert("first_name".to_string(), String::from(value.first_name));
hash_map.insert("last_name".to_string(), String::from(value.last_name));
```

Passons enfin à la génération de la sortie de notre macro :

```
quote! {
    impl From<#struct_identifier> for std::collections::HashMap<String, String> {
        fn from(value: #struct_identifier) -> Self {
            #implementation

            hash_map
        }
    }
}
```

Ici, vous commencez par créer un autre `TokenStream` à l'aide de `quote`. Vous écrivez votre implémentation du trait `From` dans ce bloc.

La ligne suivante utilise à nouveau la syntaxe du préfixe `#` que nous venons d'examiner pour déclarer que l'implémentation du trait doit concerner votre structure cible, basée sur l'identifiant de la structure. Dans ce cas, cet identifiant sera remplacé par `User` si vous appliquez la macro de dérivation à la structure `User`.

```
impl From<#struct_identifier> for std::collections::HashMap<String, String> {}
```

Enfin, vous avez le corps de la méthode réelle :

```
fn from(value: #struct_identifier) -> Self {
    #implementation

    hash_map
}
```

Comme vous pouvez le voir, vous pouvez facilement imbriquer des `TokenStream` dans d'autres `TokenStream` en utilisant la même syntaxe `#` qui vous permet d'utiliser des variables externes à l'intérieur de la macro `quote`.

Ici, vous déclarez que votre implémentation de hash map doit être insérée comme les premières lignes de la fonction. Et ensuite, vous retournez simplement la même `hash_map`. Cela complète votre implémentation du trait.

Comme toute dernière étape, vous appelez `.into()` sur le type de retour de notre bloc `match`, qui renvoie la sortie de l'appel à la macro `quote`. Cela convertit le type `TokenStream` utilisé par `quote` en type `TokenStream` provenant de la bibliothèque standard et attendu par le compilateur en retour d'une macro.

Si c'était difficile à comprendre lors de la décomposition ligne par ligne, vous pouvez consulter en complément le code complet mais commenté suivant :

```
// Indique au compilateur que cette fonction est une macro de dérivation, et l'identifiant pour derive est `IntoHashMap`.
#[proc_macro_derive(IntoHashMap)]
// Déclare une fonction qui prend un `TokenStream` en entrée et produit un `TokenStream`.
pub fn into_hash_map(item: TokenStream) -> TokenStream {
    // Analyse le flux de tokens d'entrée sous le type `DeriveInput` fourni par la crate `syn`.
    let input = syn::parse_macro_input!(item as syn::DeriveInput);

    // Stocke l'identifiant (nom) de la structure dans une variable afin de pouvoir l'insérer dans le code de sortie.
    let struct_identifier = &input.ident;

    // Match sur le type cible auquel la macro de dérivation a été appliquée
    match &input.data {
        // Vérifie que la cible était une structure, et déstructure le champ `fields` de ses informations.
        Data::Struct(syn::DataStruct { fields, .. }) => {
            // Déclare un nouveau bloc quote qui contiendra le code pour votre implémentation de la hash map.
            // Ce bloc va à la fois créer une nouvelle hash map, et aussi la remplir avec tous les champs de
            // la structure.
            let mut implementation = quote!{
                // C'est juste du code que vous voulez voir dans la sortie. Dans ce cas, vous voulez avoir
                // une nouvelle hash map créée.
                let mut hash_map = std::collections::HashMap::<String, String>::new();
            };

            // Itère sur tous les champs de votre structure cible
            for field in fields {
                // Crée une variable pour stocker l'identifiant (nom) du champ pour une utilisation ultérieure
                let identifier = field.ident.as_ref().unwrap();
                // Étend votre bloc `implementation` pour inclure le code dans la sortie qui remplit
                // la hash map que vous créez avec les informations du champ actuel.
                implementation.extend(quote!{
                    // Convertit l'identifiant du champ en chaîne à l'aide de la macro `stringify!`. Elle est utilisée
                    // comme clé dans votre nouvelle entrée de hash map. Pour la valeur de cette clé, nous accédons à la valeur du champ
                    // de la structure en utilisant `value.#identifier`, où `#identifier` est remplacé par le nom réel
                    // du champ dans le code de sortie.
                    hash_map.insert(stringify!(#identifier).to_string(), String::from(value.#identifier));
                });
            }

            // Crée le bloc de sortie final
            quote! {
                // Implémente le trait `From` pour permettre la conversion de votre structure cible, identifiée par
                // `struct_identifier` en une HashMap avec la clé et la valeur en tant que `String`.
                // Tout comme précédemment, #struct_identifier est remplacé par le nom réel de la
                // structure cible dans le code de sortie.
                impl From<#struct_identifier> for std::collections::HashMap<String, String> {
                    // C'est juste une méthode que le trait `From` vous oblige à implémenter. Le
                    // type de la valeur d'entrée est à nouveau `#struct_identifier`, qui est remplacé par
                    // le nom de la structure cible dans le code de sortie.
                    fn from(value: #struct_identifier) -> Self {
                        // Inclut le bloc `implementation` que vous avez créé à l'aide de `quote!` comme corps
                        // de cette méthode. `quote` vous permet d'imbriquer d'autres blocs `quote` librement.
                        #implementation

                        // Retourne la hash_map.
                        hash_map
                    }
                }
            }
        }
        // Si la cible est d'un autre type, panique.
        _ => unimplemented!()
        // Convertit le type `TokenStream` utilisé par `quote` au type `TokenStream` utilisé par la
        // bibliothèque standard et le compilateur
    }.into()
}
```

Et voilà. Vous avez écrit votre toute première macro procédurale en Rust !

**Il est maintenant temps de profiter des fruits de votre travail.**

### Comment utiliser votre macro de dérivation

En revenant à votre `my-app/main.rs`, affichons pour débogage la hashmap que vous créez en utilisant la macro que vous avez implémentée. Votre `main.rs` devrait ressembler à ceci :

```
// my-app/src/main.rs

use std::collections::HashMap;
use my_app_macros::IntoHashMap;

#[derive(IntoHashMap)]
pub struct User {
    username: String,
    first_name: String,
    last_name: String,
}

fn main() {
    let user = User {
        username: "username".to_string(),
        first_name: "First".to_string(),
        last_name: "Last".to_string(),
    };

    let hash_map = HashMap::<String, String>::from(user);

    dbg!(hash_map);
}
```

Si vous lancez cela avec `cargo run`, vous devriez voir la sortie suivante dans votre terminal :

```
[src/main.rs:20:5] hash_map = {
    "last_name": "Last",
    "first_name": "First",
    "username": "username",
}
```

Et voilà !

### Comment améliorer notre implémentation

Il existe une meilleure façon de travailler avec les itérateurs et `quote` que j'ai volontairement omise dans notre implémentation originale, car elle nécessite d'apprendre un peu plus de syntaxe spécifique à `quote`.

Voyons à quoi cela aurait ressemblé avec cela, avant de plonger dans son fonctionnement :

```
let input = syn::parse_macro_input!(item as syn::DeriveInput);
    let struct_identifier = &input.ident;

    match &input.data {
        Data::Struct(syn::DataStruct { fields, .. }) => {
            let field_identifiers = fields.iter().map(|item| item.ident.as_ref().unwrap()).collect::<Vec<_>>();

            quote! {
                impl From<#struct_identifier> for std::collections::HashMap<String, String> {
                    fn from(value: #struct_identifier) -> Self {
                        let mut hash_map = std::collections::HashMap::<String, String>::new();

                        #(
                            hash_map.insert(stringify!(#field_identifiers).to_string(), String::from(value.#field_identifiers));
                        )*

                        hash_map
                    }
                }
            }
        }
        _ => unimplemented!()
    }.into()
```

C'est tellement plus concis et facile à comprendre ! Regardons le morceau de syntaxe spécial qui rend cela possible – en particulier, la ligne suivante :

```
#(
    hash_map.insert(stringify!(#field_identifiers).to_string(), String::from(value.#field_identifiers));
)*
```

Décomposons-la. Tout d'abord, vous enveloppez tout le bloc dans un `#()*` et votre code va à l'intérieur des parenthèses. Cette syntaxe est ce qui vous permet d'utiliser n'importe quel itérateur à l'intérieur des parenthèses, et elle répétera ce bloc de code pour tous les éléments de l'itérateur, tout en remplaçant la variable par l'élément correct à chaque itération.

Dans ce cas, vous créez d'abord un itérateur `field_identifiers`, qui est une collection de tous les identifiants de champs de votre structure cible. Vous écrivez ensuite votre instruction d'insertion `hash_map` tout en utilisant l'itérateur directement comme s'il s'agissait d'un seul élément. L'enveloppe `#()*` convertit cela en la sortie attendue de plusieurs lignes, une pour chaque élément de l'itérateur.

## Une macro de dérivation plus élaborée

Maintenant que vous êtes à l'aise avec l'écriture d'une macro de dérivation simple, il est temps de passer à autre chose et de créer quelque chose qui sera réellement utile dans le monde réel – surtout si vous travaillez avec des modèles de base de données.

### La macro `DeriveCustomModel`

Vous allez construire une macro de dérivation qui vous aide à générer des structures dérivées à partir de votre structure originale. Vous en aurez besoin tout le temps lorsque vous travaillez avec des bases de données et que vous ne souhaitez charger qu'une partie des données.

Par exemple, si vous avez une structure `User`, qui contient toutes les informations de l'utilisateur, mais que vous ne souhaitez charger que les informations de nom pour l'utilisateur depuis la base de données, vous aurez besoin d'une structure qui ne contient que ces champs – à moins que vous ne vouliez rendre tous les champs optionnels (`Option`), ce qui n'est pas la meilleure idée.

Nous devrons également ajouter une implémentation du trait `From` pour convertir automatiquement la structure `User` vers la structure dérivée. Une autre chose dont notre macro a besoin est de pouvoir dériver plusieurs modèles à partir de la même structure cible.

Commençons par la déclarer dans `lib.rs` :

```
// lib.rs

#[proc_macro_derive(DeriveCustomModel, attributes(custom_model))]
pub fn derive_custom_model(item: TokenStream) -> TokenStream {
    todo!()
}
```

La majeure partie de cette syntaxe devrait vous être familière grâce à notre exemple précédent. Le seul ajout ici est que nous définissons maintenant `attributes(custom_model)` dans l'appel à `proc_macro_derive`, ce qui indique essentiellement au compilateur de traiter tout attribut commençant par `#[custom_model]` comme un argument pour cette macro de dérivation sur cette cible.

Par exemple, une fois que vous avez défini cela, vous pouvez appliquer `#[custom_model(name = "SomeName")]` à la structure cible, pour définir que la structure dérivée doit porter le nom "SomeName". Vous devez analyser cela vous-même et le gérer également, bien sûr – la définition servait uniquement à dire au compilateur de transmettre cela à l'implémentation de votre macro et de ne pas le traiter comme un attribut inconnu.

Créons également un nouveau fichier qui contiendra les détails de l'implémentation de cette macro. La règle des macros stipule qu'elle doit être **définie** dans `lib.rs`, et nous l'avons fait. L'implémentation elle-même peut vivre n'importe où dans le projet.

Créez un nouveau fichier `custom_model.rs` :

```
touch src/custom_model.rs
```

### Comment séparer l'implémentation de la déclaration

Définissez une fonction qui implémente la macro `DeriveCustomModel`. Nous allons également ajouter tous les imports tout de suite pour éviter toute confusion plus tard :

```
// custom_model.rs

use syn::{
    parse_macro_input, Data::Struct, DataStruct, DeriveInput, Field, Fields, Ident, Path,
};
use darling::util::PathList;
use darling::{FromAttributes, FromDeriveInput, FromMeta};
use proc_macro::TokenStream;
use quote::{quote, ToTokens};

pub(crate) fn derive_custom_model_impl(input: TokenStream) -> TokenStream {
    // Analyse le flux de tokens d'entrée comme `DeriveInput`
    let original_struct = parse_macro_input!(input as DeriveInput);

    // Déstructure les champs data & ident de l'entrée
    let DeriveInput { data, ident, .. } = original_struct.clone();
}
```

C'est juste une fonction Rust, donc il n'y a pas de règles spéciales ici. Vous pouvez l'appeler depuis la déclaration comme une fonction Rust ordinaire.

```
#[proc_macro_derive(DeriveCustomModel, attributes(custom_model))]
pub fn derive_custom_model(item: TokenStream) -> TokenStream {
    custom_model::custom_model_impl(item)
}
```

### Comment analyser les arguments d'une macro de dérivation

Pour analyser les arguments de notre macro de dérivation (qui sont généralement fournis à l'aide d'attributs appliqués soit à la cible, soit à ses champs), nous allons nous appuyer sur la crate `darling` pour rendre cela aussi simple que de définir le type de données pour eux.

```
// custom_model.rs

// Dérive `FromDeriveInput` pour cette structure, qui est une
// macro fournie par darling pour ajouter automatiquement la capacité
// d'analyser les tokens d'arguments dans la structure donnée.
#[derive(FromDeriveInput, Clone)]
// Nous indiquons à darling que nous recherchons des arguments
// définis à l'aide de l'attribut `custom_model`, et
// que nous ne supportons que les structures nommées pour cela.
#[darling(attributes(custom_model), supports(struct_named))]
struct CustomModelArgs {
    // Spécifie les paramètres pour générer un modèle dérivé.
    // Plusieurs modèles peuvent être générés en répétant
    // cet attribut avec des paramètres pour chaque modèle.
    #[darling(default, multiple, rename = "model")]
    pub models: Vec<CustomModel>,
}
```

Nous avons indiqué à `darling` que pour les arguments de la structure, nous devrions nous attendre à une liste d'arguments `model`, et chacun définira les paramètres d'un seul modèle dérivé. Cela nous permet d'utiliser la macro pour générer plusieurs structures dérivées à partir d'une seule structure d'entrée.

Ensuite, définissons les arguments pour chaque modèle :

```
// custom_model.rs

// Dérive `FromMeta` pour cette structure, qui est une
// macro fournie par darling pour ajouter automatiquement la capacité
// d'analyser les métadonnées dans la structure donnée.
#[derive(FromMeta, Clone)]
struct CustomModel {
    // Nom du modèle généré.
    name: String,
    // Liste d'identifiants de champs séparés par des virgules
    // à inclure dans le modèle généré
    fields: PathList,
    // Liste de dérivations supplémentaires à appliquer à la
    // structure résultante comme `Eq` ou `Hash`.
    #[darling(default)]
    extra_derives: PathList,
}
```

Ici, nous avons deux arguments obligatoires, `name` et `fields`, et un argument optionnel `extra_derives`. Il est optionnel grâce à l'annotation `#[darling(default)]`.

### Comment implémenter `DeriveCustomModel`

Maintenant que tous nos types de données sont définis, passons à l'analyse – ce qui est aussi simple que d'appeler une méthode sur notre structure d'arguments ! L'implémentation complète de la fonction devrait ressembler à ceci :

```
// custom_model.rs

pub(crate) fn derive_custom_model_impl(input: TokenStream) -> TokenStream {
    // Analyse le flux de tokens d'entrée comme `DeriveInput`
    let original_struct = parse_macro_input!(input as DeriveInput);

    // Déstructure les champs data & ident de l'entrée
    let DeriveInput { data, ident, .. } = original_struct.clone();

    if let Struct(data_struct) = data {
        // Extrait les champs de cette structure de données
        let DataStruct { fields, .. } = data_struct;

        // `darling` fournit cette méthode sur la structure
        // pour analyser facilement les arguments, et gère également
        // les erreurs pour nous.
        let args = match CustomModelArgs::from_derive_input(&original_struct) {
            Ok(v) => v,
            Err(e) => {
                // Si darling a renvoyé une erreur, génère un
                // flux de tokens à partir de celle-ci afin que le compilateur
                // affiche l'erreur au bon endroit.
                return TokenStream::from(e.write_errors());
            }
        };

        // Déstructure le champ `models` des arguments analysés.
        let CustomModelArgs { models } = args;

        // Crée une nouvelle sortie
        let mut output = quote!();

        // Panique si aucun modèle n'est défini mais que la macro est
        // utilisée.
        if models.is_empty() {
            panic!(
                "Veuillez spécifier au moins 1 modèle à l'aide de l'attribut `model`"
            )
        }

        // Itère sur tous les modèles définis
        for model in models {
            // Génère le modèle personnalisé à partir des champs de la structure cible et des arguments `model`.
            let generated_model = generate_custom_model(&fields, &model);

            // Étend la sortie pour inclure le modèle généré
            output.extend(quote!(#generated_model));
        }

        // Convertit la sortie en TokenStream et retourne
        output.into()
    } else {
        // Panique si la cible n'est pas une structure nommée
        panic!("DeriveCustomModel ne peut être utilisé qu'avec des structures nommées")
    }
}
```

Le code qui génère les tokens pour chaque modèle a été extrait dans une autre fonction que nous appelons `generate_custom_model`. Implémentons-la également :

### Comment générer chaque modèle personnalisé

```
// custom_model.rs

fn generate_custom_model(fields: &Fields, model: &CustomModel) -> proc_macro2::TokenStream {
    let CustomModel {
        name,
        fields: target_fields,
        extra_derives,
    } = model;

    // Crée une nouvelle sortie pour les champs
    let mut new_fields = quote!();

    // Itère sur tous les champs de la structure source
    for Field {
        // L'identifiant de ce champ
        ident,
        // Tous les attributs appliqués à ce champ
        attrs,
        // Le spécificateur de visibilité pour ce champ
        vis,
        // Le jeton deux-points `:`
        colon_token,
        // Le type de ce champ
        ty,
        ..
    } in fields
    {
        // S'assure que le champ a un identifiant, panique sinon
        let Some(ident) = ident else {
            panic!("Échec de l'obtention de l'identifiant du champ de la structure")
        };

        // Essaie de convertir l'identifiant du champ en `Path` qui est un type fourni
        // par `syn`. Nous faisons cela parce que le type PathList de `darling` est juste une
        // collection de ce type avec des méthodes supplémentaires.
        let path = match Path::from_string(&ident.clone().to_string()) {
            Ok(path) => path,
            Err(error) => panic!("Échec de la conversion de l'identifiant du champ en chemin : {error:?}"),
        };

        // Si la liste des champs cibles ne contient pas ce champ,
        // passe au champ suivant
        if !target_fields.contains(&path) {
            continue;
        }

        // S'il le contient, reconstruit la déclaration du champ
        // et l'ajoute dans la sortie `new_fields` afin que nous puissions l'utiliser
        // dans la structure de sortie.
        new_fields.extend(quote! {
            #(#attrs)*
            #vis #ident #colon_token #ty,
        });
    }

    // Crée un nouvel identifiant pour la structure de sortie
    // à partir du nom fourni.
    let struct_ident = match Ident::from_string(name) {
        Ok(ident) => ident,
        Err(error) => panic!("{error:?}"),
    };

    // Crée un TokenStream pour contenir les déclarations de dérivation supplémentaires
    // sur la nouvelle structure.
    let mut extra_derives_output = quote!();

    // Si extra_derives n'est pas vide,
    if !extra_derives.is_empty() {
        // Cette syntaxe est un peu compacte, mais vous devriez déjà
        // savoir tout ce qu'il faut pour la comprendre maintenant.
        extra_derives_output.extend(quote! {
            #(#extra_derives,)*
        })
    }

    // Construit la structure finale en combinant tous les
    // TokenStreams générés jusqu'à présent.
    quote! {
        #[derive(#extra_derives_output)]
        pub struct #struct_ident {
            #new_fields
        }
    }
}
```

### Comment utiliser votre macro `DeriveCustomModel`

En revenant à votre `my-app/main.rs`, affichons pour débogage les hash-maps générées pour vos nouvelles structures que vous créez en utilisant la macro que vous avez implémentée. Votre `main.rs` devrait ressembler à ceci :

```
// my-app/src/main.rs

use macros::{DeriveCustomModel, IntoStringHashMap};
use std::collections::HashMap;

#[derive(DeriveCustomModel)]
#[custom_model(model(
    name = "UserName",
    fields(first_name, last_name),
    extra_derives(IntoStringHashMap)
))]
#[custom_model(model(name = "UserInfo", fields(username, age), extra_derives(Debug)))]
pub struct User2 {
    username: String,
    first_name: String,
    last_name: String,
    age: u32,
}

fn main() {
    let user_name = UserName {
        first_name: "first_name".to_string(),
        last_name: "last_name".to_string(),
    };
    let hash_map = HashMap::<String, String>::from(user_name);

    dbg!(hash_map);

    let user_info = UserInfo {
        username: "username".to_string(),
        age: 27,
    };

    dbg!(user_info);
}
```

Comme vous pouvez le voir, `extra_derives` nous est déjà utile puisque nous devons dériver `Debug` et `IntoStringHashMap` pour les nouveaux modèles.

Si vous lancez cela avec `cargo run`, vous devriez voir la sortie suivante dans votre terminal :

```
[src/main.rs:32:5] hash_map = {
    "last_name": "last_name",
    "first_name": "first_name",
}
[src/main.rs:39:5] user_info = UserInfo {
    username: "username",
    age: 27,
}
```

Nous allons conclure sur les macros de dérivation ici.

## Une macro d'attribut simple

Dans cette section, vous allez apprendre à écrire une macro d'**attribut**.

### L'attribut `log_duration`

Vous allez écrire une macro d'attribut simple qui peut être appliquée à n'importe quelle fonction (ou méthode) et qui enregistrera le temps d'exécution total de cette fonction à chaque fois qu'elle est appelée.

### Comment déclarer une macro d'attribut

Vous déclarez des macros d'attribut en créant une fonction et en l'annotant à l'aide de la macro `proc_macro_attribute` qui indique au compilateur de considérer cette fonction comme une déclaration de macro. Voyons à quoi cela ressemble :

```
// my-app-macros/src/lib.rs

#[proc_macro_attribute]
pub fn log_duration(args: TokenStream, item: TokenStream) -> TokenStream {
    log_duration_impl(args, item)
}
```

Pour ces macros, le nom de la fonction est important, car il devient également le nom de la macro. Comme vous pouvez le voir, elles prennent deux arguments différents. Le premier est l'argument passé à la macro d'attribut, et le second est la cible de la macro d'attribut.

Implémentons également `log_duration_impl`. Créez un nouveau fichier `log_duration.rs` :

```
touch src/log_duration.rs
```

### Comment implémenter la macro d'attribut `log_duration`

Je vais d'abord vous donner l'implémentation complète, puis je détaillerai les parties que je n'ai pas encore utilisées :

```
// my-app-macros/src/log_duration.rs

use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, ItemFn};

pub(crate) fn log_duration_impl(_args: TokenStream, input: TokenStream) -> TokenStream {
    // Analyse l'entrée comme `ItemFn` qui est un type fourni
    // par `syn` pour représenter une fonction.
    let input = parse_macro_input!(input as ItemFn);

    let ItemFn {
        // La signature de la fonction
        sig,
        // Le spécificateur de visibilité de cette fonction
        vis,
        // Le bloc ou corps de la fonction
        block,
        // Autres attributs appliqués à cette fonction
        attrs,
    } = input;

    // Extrait les instructions dans le corps des fonctions
    let statements = block.stmts;

    // Stocke l'identifiant de la fonction pour la journalisation
    let function_identifier = sig.ident.clone();

    // Reconstruit la fonction en sortie en utilisant l'entrée analysée
    quote!(
        // Réapplique tous les autres attributs sur cette fonction.
        // Le compilateur n'inclut pas la macro sur laquelle nous
        // travaillons actuellement dans cette liste.
        #(#attrs)*
        // Reconstruit la déclaration de la fonction
        #vis #sig {
            // Au début de la fonction, crée une instance de `Instant`
            let __start = std::time::Instant::now();

            // Crée un nouveau bloc, dont le corps est le corps de la fonction.
            // Stocke la valeur de retour de ce bloc dans une variable afin que nous puissions
            // la retourner plus tard depuis la fonction parente.
            let __result = {
                #(#statements)*
            };

            // Journalise les informations de durée pour cette fonction
            println!("{} a pris {}μs", stringify!(#function_identifier), __start.elapsed().as_micros());

            // Retourne le résultat (s'il y en a un)
            return __result;
        }
    )
    .into()
}
```

Les seules choses que vous n'avez peut-être pas vues précédemment sont les champs `sig` et `block` que vous obtenez en analysant l'entrée comme `ItemFn`. `sig` contient la signature entière d'une fonction tandis que `block` contient le corps entier de la fonction. C'est pourquoi, en utilisant le code suivant, nous pouvons essentiellement reconstruire la fonction non modifiée :

```
// Exemple de code pour reconstruire une fonction non modifiée dans une macro

#vis #sig #block
```

Dans cet exemple, vous souhaitez modifier le corps de la fonction, c'est pourquoi vous créez un nouveau bloc qui encapsule le bloc de fonction original.

### Comment utiliser votre macro `log_duration`

En revenant à `main.rs`, l'utilisation d'une macro d'attribut est plus simple que vous ne le pensez :

```
// main.rs

#[log_duration]
#[must_use]
fn function_to_benchmark() -> u16 {
    let mut counter = 0;
    for _ in 0..u16::MAX {
        counter += 1;
    }

    counter
}

fn main() {
    println!("{}", function_to_benchmark());
}
```

Lorsque vous lancez cela, vous devriez obtenir la sortie suivante :

```
function_to_benchmark a pris 498μs
65535
```

Nous sommes maintenant prêts à passer à un cas d'utilisation plus complexe.

## Une macro d'attribut plus élaborée

### L'attribut `cached_fn`

Vous allez écrire une macro d'attribut qui permettra d'ajouter une capacité de mise en cache (caching) à n'importe quelle fonction. Pour les besoins de cet exemple, nous allons supposer que notre fonction a toujours des arguments de type `String` et retourne également une valeur `String`.

Certains d'entre vous connaissent peut-être cela sous le nom de fonction "mémorisée" (memoized).

De plus, vous devrez permettre à l'utilisateur de cette macro d'indiquer à la macro comment elle peut générer une clé dynamique basée sur les arguments de la fonction.

Pour nous aider à faciliter la partie mise en cache afin de ne pas nous disperser, nous allons utiliser une dépendance appelée `cacache`. `cacache` est une bibliothèque Rust pour gérer les caches locaux de clés et de contenu. Elle fonctionne en écrivant le cache sur le disque.

Ajoutons-la au projet en éditant directement le fichier `Cargo.toml` de `my-app` :

```
// Cargo.toml

workspace = { members = ["my-app-macros"] }

[package]
name = "my-app"
version = "0.1.0"
edition = "2021"
resolver = "2"

# Voir plus de clés et leurs définitions sur https://doc.rust-lang.org/cargo/reference/manifest.html

[dependencies]
# Nouvelle dépendance
cacache = { version = "13.0.0", default-features = false, features = ["mmap"] }
macros = { path = "./macros" }
```

### Comment implémenter la macro d'attribut `cached_fn`

Commençons par déclarer cette macro dans `lib.rs` :

```
// my-app-macros/src/lib.rs

#[proc_macro_attribute]
pub fn cached_fn(args: TokenStream, item: TokenStream) -> TokenStream {
    cached_fn_impl(args, item)
}
```

Créez un nouveau fichier `cached_fn.rs` pour stocker l'implémentation :

```
touch my-app-macros/src/cached_fn.rs
```

Définissons à quoi nos arguments devraient ressembler avant de passer à l'implémentation :

### Arguments de l'attribut `cached_fn`

```
// my-app-macros/src/cached_fn.rs

#[derive(FromMeta)]
struct CachedParams {
    // Accepte n'importe quelle expression que nous devrions utiliser pour calculer la
    // clé. Cela peut être une chaîne constante, ou un calcul
    // basé sur les arguments de la fonction.
    keygen: Option<Expr>,
}
```

Le seul argument est un `keygen` optionnel, qui est de type `Expr`. `Expr` représente n'importe quelle [expression Rust][57] valide, elle peut donc être très dynamique. Dans cet exemple, vous passerez une expression qui génère la clé basée sur les arguments de la fonction cible.

Comme toujours, nous verrons d'abord l'implémentation complète, puis nous détaillerai les parties qui sont nouvelles :

```
// my-app-macros/src/cached_fn.rs

pub fn cached_fn_impl(args: TokenStream, item: TokenStream) -> TokenStream {
    // Analyse les tokens d'arguments comme une liste d'éléments NestedMeta
    let attr_args = match NestedMeta::parse_meta_list(args.into()) {
        Ok(v) => v,
        Err(e) => {
            // Écrit l'erreur dans le flux de tokens de sortie s'il y en a une
            return proc_macro::TokenStream::from(Error::from(e).write_errors());
        }
    };

    // Analyse la liste meta imbriquée comme notre structure `CachedParams`
    let CachedParams { keygen } = match CachedParams::from_list(&attr_args) {
        Ok(params) => params,
        Err(error) => {
            // Écrit l'erreur dans le flux de tokens de sortie s'il y en a une
            return proc_macro::TokenStream::from(Error::from(error).write_errors());
        }
    };

    // Analyse l'élément cible d'entrée comme une fonction
    let ItemFn {
        // La signature de la fonction
        sig,
        // Le spécificateur de visibilité de cette fonction
        vis,
        // Le bloc ou corps de la fonction
        block,
        // Autres attributs appliqués à cette fonction
        attrs,
    } = parse_macro_input!(item as ItemFn);

    // Génère notre instruction de clé basée sur le paramètre donné (ou son absence)
    let key_statement = if let Some(keygen) = keygen {
        // Si l'utilisateur a spécifié un `keygen`, l'utilise comme expression pour
        // obtenir la clé de cache.
        quote! {
            let __cache_key = #keygen;
        }
    } else {
        // Si aucun `keygen` n'a été fourni, utilise le nom de la fonction
        // comme clé de cache.
        let fn_name = sig.ident.clone().to_string();
        quote! {
            let __cache_key = #fn_name;
        }
    };

    // Reconstruit la fonction en sortie en utilisant l'entrée analysée
    quote!(
        // Applique les autres attributs de la fonction originale à la fonction générée
        #(#attrs)*
        #vis #sig {
            // Inclut le key_statement que nous avons généré ci-dessus comme première
            // chose dans le corps de la fonction
            #key_statement

            // Essaie de lire la valeur depuis le cache
            match cacache::read_sync("./__cache", __cache_key.clone()) {
                // Si la valeur existe, l'analyse comme chaîne et la retourne
                Ok(value) => {
                    println!("Les données sont récupérées du cache");
                    from_utf8(&value).unwrap().to_string()
                },
                Err(_) => {
                    println!("Les données ne sont pas récupérées du cache");
                    // Sauvegarde la sortie du bloc de fonction original dans
                    // une variable.
                    let output = #block;

                    // Écrit la valeur de sortie dans le cache sous forme d'octets
                    cacache::write_sync("./__cache", __cache_key, output.as_bytes()).unwrap();

                    // Retourne la sortie originale
                    output
                }
            }
        }
    )
    .into()
}
```

Eh bien, il s'avère que vous avez déjà vu tout ce que nous avons utilisé dans celle-ci.

La seule nouveauté ici est l'utilisation de la dépendance `cacache`, mais c'est aussi assez simple. Vous donnez simplement l'emplacement où vous souhaitez stocker les données mises en cache comme premier argument aux fonctions `read_sync` et `write_sync` fournies par `cacache`.

Nous avons également ajouté quelques logs pour nous aider à vérifier que la macro fonctionne comme prévu.

### Comment utiliser la macro `cached_fn`

Pour rendre n'importe quelle fonction mémorisée ou mise en cache, nous l'annotons simplement à l'aide de l'attribut `cached_fn` :

```
// src/main.rs

#[cached_fn(keygen = "format!(\"{first_name} {last_name}\")")]
fn test_cache(first_name: String, last_name: String) -> String {
    format!("{first_name} {last_name}")
}

fn main() {
    test_cache("John".to_string(), "Appleseed".to_string());
    test_cache("John".to_string(), "Appleseed".to_string());
    test_cache("John".to_string(), "Doe".to_string());
}
```

Si vous lancez cela, vous devriez voir la sortie suivante :

```
Les données ne sont pas récupérées du cache
Les données sont récupérées du cache
Les données ne sont pas récupérées du cache
```

Ce qui montre clairement que si la fonction est appelée plus d'une fois pour les mêmes arguments, les données sont renvoyées depuis le cache. Mais si les arguments sont différents, elle ne renvoie pas la valeur qui a été mise en cache pour un ensemble d'arguments différent.

Nous avons fait beaucoup d'hypothèses pour celle-ci qui ne seraient pas vraies pour un cas d'utilisation réel. En tant que tel, ceci n'est qu'à des fins d'apprentissage, mais illustre un cas d'utilisation réel.

Par exemple, j'ai écrit des macros d'attribut pour mettre en cache des fonctions de gestionnaire HTTP en utilisant `redis` pour des serveurs de production. Celles-ci ont une implémentation très similaire à celle-ci, mais contiennent beaucoup de fioritures pour fonctionner avec ce cas d'utilisation particulier.

## Une macro de type fonction simple

Il est enfin temps de s'amuser à nouveau. Nous allons commencer simple, mais le deuxième exemple inclura l'analyse d'une syntaxe personnalisée. Sympa, non ?

Avertissement : si vous êtes familier avec les macros déclaratives (utilisant la syntaxe `macro_rules!`), vous réaliserez peut-être que les exemples suivants peuvent facilement être écrits en utilisant cette syntaxe et n'ont pas besoin d'être des macros procédurales. Écrire des exemples de macros procédurales qui ne peuvent pas être écrites en tant que macros déclaratives est extrêmement difficile si vous voulez aussi garder les choses simples, c'est pourquoi ces exemples ont été choisis malgré cela.

### La macro `constant_string`

Nous allons construire une macro très simple qui prend une chaîne littérale (de type `&str`) en entrée et crée une constante publique globale pour elle (le nom de la variable étant le même que la valeur). Fondamentalement, notre macro générera ce qui suit :

```
pub const STRING_LITERAL: &str = "STRING_LITERAL";
```

### Comment déclarer une macro de type fonction

Vous déclarez des macros de type fonction en créant une fonction et en l'annotant à l'aide d'une macro `proc_macro`. Elle indique au compilateur de considérer cette fonction comme une déclaration de macro. Voyons à quoi cela ressemble :

```
// my-app-macros/src/lib.rs

#[proc_macro]
pub fn constant_string(item: TokenStream) -> TokenStream {
    constant_string_impl(item)
}
```

Pour ces macros, le nom de la fonction est important, car il devient également le nom de la macro. Comme vous pouvez le voir, elles ne prennent qu'un seul argument, qui est tout ce que vous passez à la macro. Cela peut littéralement être n'importe quoi, même une syntaxe personnalisée qui n'est pas du code Rust valide.

### Comment implémenter la macro `constant_string`

Pour l'implémentation, créons un nouveau fichier `constant_string.rs` :

```
touch my-app-macros/src/constant_string.rs
```

L'implémentation est assez simple :

```
use darling::FromMeta;
use proc_macro::TokenStream;
use quote::quote;
use syn::{parse_macro_input, Ident, LitStr};

pub fn constant_string_impl(item: TokenStream) -> TokenStream {
    // Analyse l'entrée comme une chaîne littérale
    let constant_value = parse_macro_input!(item as LitStr);

    // Crée un nouvel `Ident` (identifiant) à partir de la valeur de chaîne passée.
    // Ce sera le nom de la variable constante.
    let constant_value_name = Ident::from_string(&constant_value.value()).unwrap();

    // Génère le code pour déclarer la variable constante.
    quote!(pub const #constant_value_name: &str = #constant_value;).into()
}
```

Tout ce que nous faisons est d'analyser l'entrée comme une chaîne littérale. Si vous passez quelque chose qui n'est pas une chaîne littérale, cela générera une erreur. Ensuite, nous prenons la chaîne, en créons un identifiant et générons le code de sortie. Court et simple.

### Comment utiliser la macro `constant_string`

L'utilisation de cette macro est également assez simple :

```
// src/main.rs

constant_string!("SOME_CONSTANT_STRING_VALUE");
```

Le code ci-dessus s'étendra comme ceci :

```
pub const SOME_CONSTANT_STRING_VALUE: &str = "SOME_CONSTANT_STRING_VALUE";
```

## Une macro de type fonction plus élaborée

Les macros de type fonction, comme leur nom l'indique, peuvent être utilisées de manière similaire à l'appel d'une fonction. Vous pouvez également les utiliser à n'importe quel endroit où vous pouvez appeler une fonction, et même au-delà.

### La macro `hash_mapify`

Passons aux parties intéressantes : la macro que vous allez écrire maintenant vous permettra de générer une `HashMap` en passant simplement une liste de paires clé-valeur. Par exemple :

```
let variable = "Une variable";

hash_mapify!(
    &str,
    key = "valeur", 
    key2 = "valeur2", 
    key3 = "valeur3", 
    key4 = variable
);
```

Comme vous pouvez le voir, nous voulons que le premier argument soit le type de la valeur, et les arguments suivants soient les paires clé-valeur. Et nous devrons analyser tout cela nous-mêmes.

Pour garder les choses simples, car cela peut facilement devenir incontrôlable, nous allons seulement supporter les valeurs primitives telles que les chaînes, les entiers, les flottants et les booléens. Nous n'allons donc pas supporter la création d'une `hash_map` avec des clés qui ne sont pas des chaînes ou des `enum` et `struct` comme valeurs.

### Comment implémenter la macro `hash_mapify`

Nous allons commencer comme d'habitude par déclarer notre macro :

```
// my-app-macros/src/lib.rs

#[proc_macro]
pub fn hash_mapify(item: TokenStream) -> TokenStream {
    hash_mapify_impl(item)
}
```

Ensuite, vous allez définir une structure de données pour contenir vos données d'entrée. Dans ce cas, vous devez connaître le type de valeur passé, ainsi qu'une liste de paires clé-valeur.

Nous allons extraire l'implémentation dans un fichier séparé, qui est également l'endroit où vous implémenterez les types de données et la logique d'analyse.

Créez un nouveau fichier `hash_mapify.rs` et déclarez le type de données pour contenir les données d'entrée :

```
touch my-app-macros/src/hash_mapify.rs
```

### Comment analyser l'entrée de `hash_mapify`

```
// my-app-macros/src/hash_mapify.rs

use proc_macro::TokenStream;
use quote::{quote, ToTokens};
use syn::parse::{Parse, ParseStream};
use syn::{parse_macro_input, Lit, LitStr, Token, Type};

pub struct ParsedMapEntry(String, proc_macro2::TokenStream);

pub struct ParsedMap {
    value_type: Type,
    entries: Vec<ParsedMapEntry>,
}
```

Vous stockez la valeur directement en tant que `TokenStream` car vous devez supporter à la fois les valeurs littérales et les variables, qui n'ont qu'un seul type commun dans ce contexte, `TokenStream`.

Vous avez peut-être aussi remarqué que nous sauvegardons le `value_type` en tant que `Type` qui est un type fourni par la crate `syn` et qui est une énumération des types possibles qu'une valeur Rust pourrait avoir.

Vous n'aurez pas besoin de gérer chaque variante de cette énumération, car ce type peut également être directement converti en `TokenStream`. Vous comprendrez mieux ce que cela signifie sous peu.

Ensuite, vous devez implémenter le trait `syn::parse::Parse` pour `ParsedMap` déclaré précédemment, afin qu'il puisse être calculé à partir du `TokenStream` passé en arguments à la macro.

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        let mut entries = Vec::<ParsedMapEntry>::new();
    }
}
```

`input`, qui est de type `ParsedStream` dans ce cas, fonctionne de manière similaire à un itérateur. Vous devez analyser les tokens à partir de l'entrée en utilisant la méthode `parse` sur celle-ci, ce qui fera également avancer le flux au début du token suivant.

Par exemple, si vous avez un flux de tokens représentant `[a, b, c]`, dès que vous analysez `[` à partir de ce flux, le flux sera muté pour ne contenir que `a, b, c]`. C'est très similaire aux itérateurs, où dès que vous extrayez une valeur, l'itérateur avance d'une position et ne contient plus que les éléments restants.

Avant d'analyser quoi que ce soit, vous devez vérifier si l'entrée est vide, et paniquer si c'est le cas :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        // ...

        // Vérifie si l'entrée est vide (aucun argument n'est passé). Si
        // ce n'est pas le cas, panique car nous ne pouvons pas continuer.
        if input.is_empty() {
            panic!("Au moins un type doit être spécifié pour une hashmap vide");
        }

        // ...
    }
}
```

Puisque nous attendons que le premier argument passé à la macro soit le type de la valeur dans notre hashmap, analysons-le à partir du flux de tokens :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        // ...

        // Puisque le premier argument doit être de type `Type`, vous essayez
        // d'analyser `Type` à partir de l'entrée et retournez une erreur sinon.
        let ty = input.parse::<Type>()?;

        // ...
    }
}
```

`Parse` prend un seul argument de type qui représente ce qu'il faut analyser.

Si le premier argument ne peut pas être analysé comme un type valide, une erreur sera retournée. Notez que cela ne vérifie pas si le type que vous avez passé existe réellement ou non, cela validera seulement si les tokens du premier argument sont valides pour une définition de type, et c'est tout.

Cela signifie que si vous passez `SomeRandomType` alors que `SomeRandomType` n'est pas réellement défini, l'analyse réussira quand même. Elle n'échouera qu'après l'expansion de la macro pendant le temps de compilation.

En continuant, nous attendons également de l'utilisateur qu'il utilise `,` pour séparer les arguments. Analysons cela comme le token suivant après le type :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        // ...

        // Ensuite, analyse le token `,`, que vous attendez pour
        // séparer les arguments.
        input.parse::<Token![,]>()?;

        // ...
    }
}
```

Vous remarquerez peut-être l'utilisation de la macro `Token!` lors de la fourniture de l'argument de type pour la méthode `parse`. C'est une macro fournie par `syn` pour convertir facilement les éléments intégrés tels que les mots-clés (`type`, `async`, `fn`, etc.) ainsi que la ponctuation (`,`, `.`, `;`, etc.) et les délimiteurs (`{`, `[`, `(`, etc.). Cette macro prend un seul argument, qui est le littéral du mot-clé/ponctuation/délimiteur pour lequel le type est nécessaire.

La documentation officielle la définit comme :

> Une macro de type qui s'étend au nom de la représentation de type Rust d'un token donné.

Maintenant que vous avez le type de valeur ainsi que le premier séparateur (virgule), il est temps de commencer à analyser les paires clé-valeur. Toutes les paires clé-valeur suivent la même structure `clé = valeur` et sont séparées par des virgules.

Notez que les espaces ne sont pas importants, car cela est entièrement géré pendant le processus de tokenisation et n'est pas quelque chose que vous devez gérer.

Comme vous ne saurez pas combien de paires clé-valeur sont passées, vous avez besoin de quelque chose pour vous dire quand tout a été analysé :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        // ...

        // Boucle jusqu'à ce que l'entrée soit vide (il n'y a plus rien
        // à analyser).
        while !input.is_empty() {
            // ..
        }

        // ...
    }
}
```

Comme je l'ai expliqué précédemment, les tokens sont extraits du flux et celui-ci avance à chaque fois que vous analysez quelque chose. Cela signifie que lorsque tous les tokens sont analysés, le flux sera vide. Nous utilisons ce fait ici pour savoir quand sortir de la boucle.

Chaque paire clé-valeur peut être analysée de la même manière que vous avez analysé l'argument de type :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        // ...

        // Boucle jusqu'à ce que l'entrée soit vide (il n'y a plus rien
        // à analyser).
        while !input.is_empty() {
            // Essaie d'analyser la clé comme un identifiant
            let key = if let Ok(key) = input.parse::<syn::Ident>() {
                key.to_string()
                // Si ce n'est pas un identifiant, essaie de l'analyser comme
                // une chaîne littérale
            } else if let Ok(key) = input.parse::<LitStr>() {
                key.value()
                // Si ce n'est ni un identifiant ni une chaîne littérale,
                // ce n'est pas une clé valide, donc panique avec l'erreur
                // appropriée.
            } else {
                panic!("La clé doit être soit une chaîne littérale, soit un identifiant !");
            };

            // Analyse le signe `=`, qui devrait être le token suivant après
            // une clé.
            input.parse::<Token![=]>()?;

            // Ensuite, essaie d'analyser la valeur comme un identifiant. Si c'en est un, cela
            // signifie que c'est une variable, nous devrions donc la convertir en flux de tokens
            // directement.
            let value = if let Ok(value) = input.parse::<syn::Ident>() {
                value.to_token_stream()
                // Si l'entrée n'est pas un identifiant, essaie de l'analyser comme une
                // valeur littérale telle que `"string"` pour les chaînes, `42`
                // pour les nombres, `false` pour une valeur booléenne, etc.
            } else if let Ok(value) = input.parse::<Lit>() {
                value.to_token_stream()
            } else {
                // Si l'entrée n'est ni un identifiant ni une valeur littérale,
                // panique avec l'erreur appropriée.
                panic!("La valeur doit être soit un littéral, soit un identifiant !");
            };

            // Ajoute la paire clé-valeur analysée à notre liste.
            entries.push(ParsedMapEntry(key, value));

            // Vérifie si le token suivant est une virgule, sans faire avancer le flux
            if input.peek(Token![,]) {
                // Si c'en est une, alors l'analyse et fait avancer le flux avant
                // de passer à la paire clé-valeur suivante
                input.parse::<Token![,]>()?;
            }
        }

        // ...
    }
}
```

La seule chose nouvelle ici est l'appel à la méthode `peek` à la fin. C'est une méthode spéciale qui retourne un booléen si le token passé à `peek` est le token suivant dans le flux, et faux sinon.

Comme son nom l'indique, cela effectue seulement une vérification, donc cela n'extrait pas ce token du flux et ne fait pas avancer le flux sous aucune forme.

Une fois que toute l'analyse est terminée, vous retournez simplement les informations dans le cadre de la structure `ParsedMap` que nous avons déclarée plus tôt. L'implémentation complète de ce trait est ci-dessous si c'est plus facile à lire pour vous :

```
// my-app-macros/src/hash_mapify.rs

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        let mut entries = Vec::<ParsedMapEntry>::new();

        // Vérifie si l'entrée est vide (aucun argument n'est passé). Si ce n'est pas le cas, alors
        // panique car nous ne pouvons pas continuer.
        if input.is_empty() {
            panic!("Au moins un type doit être spécifié pour une hashmap vide");
        }

        // Puisque le premier argument doit être de type `Type`, vous essayez
        // d'analyser `Type` à partir de l'entrée et retournez une erreur sinon.
        let ty = input.parse::<Type>()?;

        // Ensuite, analyse le token `,`, que vous attendez pour
        // séparer les arguments.
        input.parse::<Token![,]>()?;

        // Boucle jusqu'à ce que l'entrée soit vide (il n'y a plus rien
        // à analyser).
        while !input.is_empty() {
            // Essaie d'analyser la clé comme un identifiant
            let key = if let Ok(key) = input.parse::<syn::Ident>() {
                key.to_string()
                // Si ce n'est pas un identifiant, essaie de l'analyser comme
                // une chaîne littérale
            } else if let Ok(key) = input.parse::<LitStr>() {
                key.value()
                // Si ce n'est ni un identifiant ni une chaîne littérale,
                // ce n'est pas une clé valide, donc panique avec l'erreur
                // appropriée.
            } else {
                panic!("La clé doit être soit une chaîne littérale, soit un identifiant !");
            };

            // Analyse le signe `=`, qui devrait être le token suivant après
            // une clé.
            input.parse::<Token![=]>()?;

            // Ensuite, essaie d'analyser la valeur comme un identifiant. Si c'en est un, cela
            // signifie que c'est une variable, nous devrions donc la convertir en flux de tokens
            // directement.
            let value = if let Ok(value) = input.parse::<syn::Ident>() {
                value.to_token_stream()
                // Si l'entrée n'est pas un identifiant, essaie de l'analyser comme une
                // valeur littérale telle que `"string"` pour les chaînes, `42`
                // pour les nombres, `false` pour une valeur booléenne, etc.
            } else if let Ok(value) = input.parse::<Lit>() {
                value.to_token_stream()
            } else {
                // Si l'entrée n'est ni un identifiant ni une valeur littérale,
                // panique avec l'erreur appropriée.
                panic!("La valeur doit être soit un littéral, soit un identifiant !");
            };

            // Ajoute la paire clé-valeur analysée à notre liste.
            entries.push(ParsedMapEntry(key, value));

            // Vérifie si le token suivant est une virgule, sans faire avancer le flux
            if input.peek(Token![,]) {
                // Si c'en est une, alors l'analyse et fait avancer le flux avant
                // de passer à la paire clé-valeur suivante
                input.parse::<Token![,]>()?;
            }
        }

        Ok(ParsedMap {
            value_type: ty,
            entries,
        })
    }
}
```

### Comment générer le code de sortie

Vous pouvez maintenant enfin écrire l'implémentation réelle de la macro, qui sera assez directe :

```
// my-app-macros/src/hash_mapify.rs

pub fn hash_mapify_impl(item: TokenStream) -> TokenStream {
    // Analyse le flux de tokens d'entrée comme `ParsedMap` défini par nous.
    // Cela utilisera la logique du trait parse que nous avons implémenté
    // plus tôt.
    let input = parse_macro_input!(item as ParsedMap);

    let key_value_pairs = input.entries;
    let ty = input.value_type;

    // Génère la hashmap de sortie à l'intérieur d'un bloc de code afin que
    // nous ne masquions aucune variable existante. Retourne la hashmap
    // depuis le bloc.
    quote!({
        // Crée une nouvelle hashmap avec `String` pour le type de clé et `#ty` pour 
        // le type de valeur, analysé à partir des arguments d'entrée de la macro.
        let mut hash_map = std::collections::HashMap::<String, #ty>::new();

        // Insère toutes les paires clé-valeur dans la hashmap.
        #(
            hash_map.insert(#key_value_pairs);
        )*

        // Retourne la hashmap générée
        hash_map
    })
    .into()
}
```

Si vous codez en même temps que moi, ou si vous avez l'œil vif, vous avez peut-être remarqué qu'il y a une erreur ici. Le type de la variable `key_value_pairs` est `Vec<ParsedMapEntry>`. Nous essayons de l'utiliser dans la sortie comme ceci :

```
#(hash_map.insert(#key_value_pairs);)*
```

ce qui est la syntaxe correcte pour travailler avec des listes, mais le type sous-jacent `ParsedMapEntry` est un type personnalisé. Et ni `syn` ni `quote` ne sauraient comment le convertir en un flux de tokens. Nous ne pouvons donc pas l'utiliser avec cette syntaxe.

Mais si nous essayons d'écrire manuellement une implémentation où nous bouclons nous-mêmes, générons un flux de tokens séparé dans chaque boucle et étendons celui existant, cela va être assez fastidieux. Ne serait-ce pas génial s'il y avait une meilleure solution ? Il s'avère qu'il y en a une : le trait `ToTokens`.

### Comment convertir des types de données personnalisés en tokens de sortie

Ce trait peut être implémenté pour n'importe lequel de nos types personnalisés et définit à quoi ressemble le type lorsqu'il est converti en flux de tokens.

```
// my-app-macros/src/hash_mapify.rs

impl ToTokens for ParsedMapEntry {
    fn to_tokens(&self, tokens: &mut proc_macro2::TokenStream) {
        let key = self.0.clone();
        let value = self.1.clone();

        tokens.extend(quote!(String::from(#key), #value));
    }
}
```

Dans le cadre de l'implémentation, vous devez muter l'argument `tokens` et l'étendre pour qu'il contienne le flux de tokens que nous voulons que notre type génère. La syntaxe que j'ai utilisée pour faire cela devrait vous être familière maintenant.

Une fois cela fait, `quote` peut maintenant facilement convertir le code problématique en flux de tokens. Ainsi, ceci : `#(hash_map.insert(#key_value_pairs);)*` fonctionnera désormais directement.

Comme d'habitude, voici l'implémentation complète si c'est plus facile à comprendre :

```
// my-app-macros/src/hash_mapify.rs

use proc_macro::TokenStream;
use quote::{quote, ToTokens};
use syn::parse::{Parse, ParseStream};
use syn::{parse_macro_input, Lit, LitStr, Token, Type};

pub struct ParsedMapEntry(String, proc_macro2::TokenStream);

pub struct ParsedMap {
    value_type: Type,
    entries: Vec<ParsedMapEntry>,
}

impl ToTokens for ParsedMapEntry {
    fn to_tokens(&self, tokens: &mut proc_macro2::TokenStream) {
        let key = self.0.clone();
        let value = self.1.clone();

        tokens.extend(quote!(String::from(#key), #value));
    }
}

impl Parse for ParsedMap {
    fn parse(input: ParseStream) -> syn::Result<Self> {
        let mut entries = Vec::<ParsedMapEntry>::new();

        // Vérifie si l'entrée est vide (aucun argument n'est passé). Si ce n'est pas le cas, alors
        // panique car nous ne pouvons pas continuer.
        if input.is_empty() {
            panic!("Au moins un type doit être spécifié pour une hashmap vide");
        }

        // Puisque le premier argument doit être de type `Type`, vous essayez
        // d'analyser `Type` à partir de l'entrée et retournez une erreur sinon.
        let ty = input.parse::<Type>()?;

        // Ensuite, analyse le token `,`, que vous attendez pour
        // séparer les arguments.
        input.parse::<Token![,]>()?;

        // Boucle jusqu'à ce que l'entrée soit vide (il n'y a plus rien
        // à analyser).
        while !input.is_empty() {
            // Essaie d'analyser la clé comme un identifiant
            let key = if let Ok(key) = input.parse::<syn::Ident>() {
                key.to_string()
                // Si ce n'est pas un identifiant, essaie de l'analyser comme
                // une chaîne littérale
            } else if let Ok(key) = input.parse::<LitStr>() {
                key.value()
                // Si ce n'est ni un identifiant ni une chaîne littérale,
                // ce n'est pas une clé valide, donc panique avec l'erreur
                // appropriée.
            } else {
                panic!("La clé doit être soit une chaîne littérale, soit un identifiant !");
            };

            // Analyse le signe `=`, qui devrait être le token suivant après
            // une clé.
            input.parse::<Token![=]>()?;

            // Ensuite, essaie d'analyser la valeur comme un identifiant. Si c'en est un, cela
            // signifie que c'est une variable, nous devrions donc la convertir en flux de tokens
            // directement.
            let value = if let Ok(value) = input.parse::<syn::Ident>() {
                value.to_token_stream()
                // Si l'entrée n'est pas un identifiant, essaie de l'analyser comme une
                // valeur littérale telle que `"string"` pour les chaînes, `42`
                // pour les nombres, `false` pour une valeur booléenne, etc.
            } else if let Ok(value) = input.parse::<Lit>() {
                value.to_token_stream()
            } else {
                // Si l'entrée n'est ni un identifiant ni une valeur littérale,
                // panique avec l'erreur appropriée.
                panic!("La valeur doit être soit un littéral, soit un identifiant !");
            };

            // Ajoute la paire clé-valeur analysée à notre liste.
            entries.push(ParsedMapEntry(key, value));

            // Vérifie si le token suivant est une virgule, sans faire avancer le flux
            if input.peek(Token![,]) {
                // Si c'en est une, alors l'analyse et fait avancer le flux avant
                // de passer à la paire clé-valeur suivante
                input.parse::<Token![,]>()?;
            }
        }

        Ok(ParsedMap {
            value_type: ty,
            entries,
        })
    }
}

pub fn hash_mapify_impl(item: TokenStream) -> TokenStream {
    // Analyse le flux de tokens d'entrée comme `ParsedMap` défini par nous.
    // Cela utilisera la logique du trait parse que nous avons implémenté
    // plus tôt.
    let input = parse_macro_input!(item as ParsedMap);

    let key_value_pairs = input.entries;
    let ty = input.value_type;

    // Génère la hashmap de sortie à l'intérieur d'un bloc de code afin que
    // nous ne masquions aucune variable existante. Retourne la hashmap
    // depuis le bloc.
    quote!({
        // Crée une nouvelle hashmap avec `String` pour le type de clé et `#ty` pour
        // le type de valeur, analysé à partir des arguments d'entrée de la macro.
        let mut hash_map = std::collections::HashMap::<String, #ty>::new();

        // Insère toutes les paires clé-valeur dans la hashmap.
        #(
            hash_map.insert(#key_value_pairs);
        )*

        // Retourne la hashmap générée
        hash_map
    })
    .into()
}
```

### Comment utiliser la macro `hash_mapify`

Nous pouvons vérifier que notre macro fonctionne en écrivant une utilisation simple :

```
// src/main.rs

fn main() {
    test_hashmap();
}

fn test_hashmap() {
    let some_variable = "Valeur d'une variable";

    let hash_map = hash_mapify!(
        &str,
        "first_key" = "first_value",
        "second_variable" = some_variable,
        some_key = "valeur pour une clé variable",
    );

    let number_hash_map =
        hash_mapify!(usize, "first_key" = 1, "second_variable" = 2, some_key = 3,);

    dbg!(hash_map);
    dbg!(number_hash_map);
}
```

Si vous lancez ce code, vous devriez voir la sortie suivante :

```
[src/main.rs:62:5] hash_map = {
    "first_key": "first_value",
    "some_key": "valeur pour une clé variable",
    "second_variable": "Valeur d'une variable",
}
[src/main.rs:63:5] number_hash_map = {
    "second_variable": 2,
    "first_key": 1,
    "some_key": 3,
}
```

ce qui correspond à ce que nous attendions.

Et maintenant que nous avons couvert les trois types de macros procédurales, nous allons conclure les exemples ici.

## Au-delà de l'écriture de macros

Maintenant que vous avez appris à écrire des macros de dérivation de base, j'aimerais prendre un peu de temps pour présenter rapidement quelques outils et techniques supplémentaires qui seront utiles lors de la manipulation des macros. Je soulignerai également certains inconvénients pour expliquer pourquoi et quand les éviter.

### Crates et outils utiles

[**cargo-expand**][58]

Il s'agit d'un outil en ligne de commande (CLI) qui peut générer le code étendu par les macros pour n'importe quel fichier de votre projet. Un autre excellent projet de [David Tolnay][59]. Vous avez cependant besoin de la chaîne d'outils nightly pour Rust pour l'utiliser. Ne vous inquiétez pas – elle n'est requise que pour le fonctionnement de l'outil lui-même. Vous n'avez pas besoin de faire passer votre projet en nightly également. Votre projet peut rester en version stable.

Installez la chaîne d'outils nightly :

```
rustup toolchain install nightly
```

Installez `cargo-expand` :

```
cargo install cargo-expand
```

Maintenant que cela est fait, vous pouvez voir à quoi ressemble l'expansion réelle de votre code dans main. Lancez simplement la commande suivante dans le répertoire du projet `my-app` :

```
cargo expand
```

et il affichera le code étendu dans la sortie du terminal. Vous verrez également des choses peu familières, comme ce à quoi la macro `dbg!` s'étend, mais vous pouvez les ignorer.

**[trybuild][60] & [macrotest][61]**

Ce sont 2 crates extrêmement utiles si vous voulez tester unitairement les formes étendues de vos macros procédurales, ou vérifier les erreurs de compilation attendues.

## Inconvénients des macros

### Débogage (ou son absence)

Vous ne pouvez pas placer de point d'arrêt (breakpoint) sur une ligne de code générée par une macro. Vous ne pouvez pas non plus y accéder à partir de la trace d'appels (stacktrace) d'une erreur. Cela rend le débogage du code généré très difficile.

Dans mon flux de travail habituel, soit je place des logs dans le code généré, soit si cela ne suffit pas, je remplace temporairement l'utilisation de la macro par le code qui m'est donné par `cargo expand` pour le déboguer, apporter des modifications, puis mettre à jour le code de la macro en conséquence.

Il existe peut-être de meilleures façons de faire, et si vous en connaissez, je vous serais reconnaissant de les partager avec moi.

### Coûts au temps de compilation

L'expansion des macros a un coût non nul que le compilateur doit exécuter et traiter, puis vérifier que le code généré est valide. Cela devient encore plus coûteux lorsque des macros récursives sont impliquées.

À titre d'estimation très brute, chaque expansion de macro ajoute 10 ms au temps de compilation du projet. Si vous êtes intéressé, je vous encourage à lire cette [introduction sur la façon dont le compilateur traite les macros][62] en interne.

### Manque d'autocomplétion et de vérifications de code

Le code écrit dans le cadre de la sortie d'une macro n'est actuellement pas entièrement supporté par les IDE, ni par rust-analyzer. Ainsi, dans la plupart des cas, vous écrivez du code sans pouvoir compter sur des fonctionnalités telles que l'autocomplétion, les suggestions automatiques, etc.

### Où tracer la limite ?

Compte tenu du potentiel incroyable des macros, il est très facile de s'emballer. Il est important de se rappeler tous les inconvénients et de prendre des décisions en conséquence, en veillant à ne pas tomber dans une abstraction prématurée.

En règle générale, j'évite personnellement d'implémenter toute "logique métier" avec des macros, et je n'essaie pas non plus d'écrire des macros pour générer du code que je devrai parcourir avec un débogueur à maintes reprises. Ou le code dans lequel je devrai apporter des micro-changements pour tester et améliorer les performances.

## Conclusion

Ce fut un long voyage ! Mais je voulais que toute personne ayant des connaissances et une expérience de base avec Rust puisse suivre et être capable d'écrire des macros dans ses propres projets.

J'espère avoir réussi à le faire pour vous. J'écrirai beaucoup plus sur les macros en général, alors restez à l'écoute.

Vous pouvez trouver le code complet de tout ce que nous avons examiné dans cet article dans le dépôt [https://github.com/anshulsanghi-blog/macros-handbook][63].

N'hésitez pas non plus à **[me contacter][64]** si vous avez des questions ou des avis sur ce sujet.

### **Vous aimez mon travail ?**

Pensez à m'offrir un café pour soutenir mon travail !

[☕Offrez-moi un café][65]

À la prochaine, bon codage et je vous souhaite un ciel dégagé !

[1]: https://www.freecodecamp.org/news/rust-in-replit/
[2]: #heading-que-sont-les-macros-en-rust
[3]: #heading-les-types-de-macros-en-rust
[4]: #heading-les-types-de-macros-procedurales
[5]: #heading-prerequis
[6]: #heading-dependances-utiles
[7]: #heading-comment-ecrire-une-macro-de-derivation-simple
[8]: #heading-la-macro-de-derivation-intostringhashmap
[9]: #heading-comment-declarer-une-macro-de-derivation
[10]: #heading-comment-analyser-lentree-de-la-macro
[11]: #heading-comment-garantir-une-cible-de-type-struct-pour-la-macro
[12]: #heading-comment-generer-le-code-de-sortie
[13]: #heading-comment-utiliser-votre-macro-de-derivation
[14]: #heading-comment-ameliorer-notre-implementation
[15]: #heading-une-macro-de-derivation-plus-elaboree
[16]: #heading-la-macro-derivecustommodel
[17]: #heading-comment-separer-limplementation-de-la-declaration
[18]: #heading-comment-analyser-les-arguments-dune-macro-de-derivation
[19]: #heading-comment-implementer-derivecustommodel
[20]: #heading-comment-generer-chaque-modele-personnalise
[21]: #heading-comment-utiliser-votre-macro-derivecustommodal
[22]: #heading-une-macro-dattribut-simple
[23]: #heading-lattribut-logduration
[24]: #heading-comment-declarer-une-macro-dattribut
[25]: #heading-comment-implementer-la-macro-dattribut-logduration
[26]: #heading-comment-utiliser-votre-macro-logduration
[27]: #heading-une-macro-dattribut-plus-elaboree
[28]: #heading-lattribut-cachedfn
[29]: #heading-comment-implementer-la-macro-dattribut-cachedfn
[30]: #heading-arguments-de-lattribut-cachedfn
[31]: #heading-comment-utiliser-la-macro-cachedfn
[32]: #heading-une-macro-de-type-fonction-simple
[33]: #heading-la-macro-constantstring
[34]: #heading-comment-declarer-une-macro-de-type-fonction
[35]: #heading-comment-implementer-la-macro-constantstring
[36]: #heading-comment-utiliser-la-macro-constantstring
[37]: #heading-une-macro-de-type-fonction-plus-elaboree
[38]: #heading-la-macro-hashmapify
[39]: #heading-comment-implementer-la-macro-hashmapify
[40]: #heading-comment-analyser-lentree-de-hashmapify
[41]: #heading-comment-generer-le-code-de-sortie
[42]: #heading-comment-convertir-des-types-de-donnees-personnalises-en-tokens-de-sortie
[43]: #heading-comment-utiliser-la-macro-hashmapify
[44]: #heading-au-dela-de-lecriture-de-macros
[45]: #heading-crates-et-outils-utiles
[46]: #heading-inconvenients-des-macros
[47]: #heading-debogage-ou-son-absence
[48]: #heading-couts-au-temps-de-compilation
[49]: #heading-manque-dautocompletion-et-de-verifications-de-code
[50]: #heading-ou-tracer-la-limite
[51]: #heading-conclusion
[52]: #heading-vous-aimez-mon-travail
[53]: https://doc.rust-lang.org/reference/macros-by-example.html
[54]: https://doc.rust-lang.org/reference/conditional-compilation.html
[55]: https://dev.to/balapriya/abstract-syntax-tree-ast-explained-in-plain-english-1h38
[56]: https://crates.io/users/dtolnay
[57]: https://doc.rust-lang.org/reference/expressions.html
[58]: https://github.com/dtolnay/cargo-expand
[59]: https://crates.io/users/dtolnay
[60]: https://docs.rs/trybuild/latest/trybuild/#
[61]: https://docs.rs/macrotest/latest/macrotest/#
[62]: https://rustc-dev-guide.rust-lang.org/macro-expansion.html
[63]: https://github.com/anshulsanghi-blog/macros-handbook
[64]: mailto:contact@anshulsanghi.tech
[65]: https://buymeacoffee.com/anshulsanghi