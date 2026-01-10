---
title: Tutoriel Rust – Apprenez les itérateurs avancés et le pattern matching en construisant
  un parseur JSON
date: '2024-05-29T10:45:15.000Z'
author: Anshul Sanghi
authorURL: https://www.freecodecamp.org/news/author/anshulsanghi/
originalURL: https://freecodecamp.org/news/rust-tutorial-build-a-json-parser
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2024/05/JSON-Parser-Cover.png
tags:
- name: Rust
  slug: rust
seo_desc: 'Iterators and match patterns are two of the most used language features
  in Rust. If you have written any real world application, big or small, chances are
  that you''ve already used these, whether knowingly or unknowingly.

  In this tutorial, I aim to he...'
---


Les itérateurs et les match patterns sont deux des fonctionnalités les plus utilisées du langage Rust. Si vous avez écrit une application réelle, petite ou grande, il y a de fortes chances que vous les ayez déjà utilisés, consciemment ou non.

<!-- more -->

Dans ce tutoriel, mon objectif est de vous aider à comprendre comment ils fonctionnent réellement, les nombreuses façons dont ils sont habituellement utilisés, et leur puissance en écrivant un parseur JSON qui utilise intensivement ces fonctionnalités.

## Avertissement

L'objectif de ce tutoriel est de créer une bibliothèque réelle qui utilise largement les match patterns et les itérateurs. Le but n'est pas d'écrire un parseur JSON performant ou totalement conforme aux spécifications.

Si vous êtes très familier avec le format JSON, vous remarquerez que de nombreuses choses manquent dans ce code, la principale étant la gestion des erreurs lorsque des tokens invalides sont rencontrés, ainsi que le retour d'informations à l'utilisateur ou des suggestions utiles sur ce qui ne va pas avec le JSON.

Ce programme ne gère pas non plus les caractères d'échappement et les séquences au sein des littéraux de chaîne, par exemple. Le code suppose, pour l'essentiel, que vous avez un JSON valide.

## Prérequis

Bien que ce tutoriel puisse être suivi par des programmeurs Rust de tout niveau, une expérience préalable ou une compréhension de base des itérateurs et des match patterns en Rust est utile.

Il est également supposé que vous êtes familier avec les concepts Rust les plus basiques tels que les `traits`, `structs`, `enums`, les boucles `for`, les blocs `impl`, et ainsi de suite. Le tutoriel vous présente l'`iterator` et le `match`, vous n'avez donc pas besoin d'être un expert de ces notions pour en tirer profit.

## Table des matières

1.  [Que sont les itérateurs en Rust ?][1]
    1.  [Comment implémenter des itérateurs en Rust][2]
    2.  [Que sont les itérateurs peekable en Rust ?][3]
2.  [Qu'est-ce que l'instruction match en Rust ?][4]
    1.  [Comment utiliser les itérateurs dans les instructions match en Rust][5]
    2.  [Que sont les gardes de match en Rust ?][6]
    3.  [Qu'est-ce que le binding en Rust ?][7]
3.  [Comment construire un parseur JSON – Étape 1 : Le Reader][8]
    1.  [Qu'est-ce que l'encodage d'octets UTF-8 ?][9]
    2.  [Comment lire les données][10]
    3.  [Comment implémenter l'itérateur pour JsonReader][11]
4.  [Comment construire un parseur JSON – Étape 2 : Préparer les types de données intermédiaires][12]
    1.  [Le type value][13]
    2.  [Comment ajouter des méthodes de conversion utiles][14]
5.  [Comment construire un parseur JSON – Étape 3 : Tokenisation][15]
    1.  [Comment définir les tokens valides attendus][16]
    2.  [Comment implémenter la struct tokenizer][17]
    3.  [Comment tokeniser un itérateur de caractères][18]
    4.  [Comment parser les tokens de chaîne][19]
    5.  [Comment parser les tokens de nombre][20]
    6.  [Comment parser les tokens booléens][21]
    7.  [Comment parser le littéral Null][22]
    8.  [Comment parser les délimiteurs][23]
    9.  [Comment parser un caractère de terminaison][24]
6.  [Comment construire un parseur JSON – Étape 4 : Des tokens à la valeur][25]
    1.  [Comment parser les primitifs][26]
    2.  [Comment parser les tableaux][27]
    3.  [Comment parser les objets][28]
7.  [Comment utiliser le parseur JSON][29]
8.  [Conclusion][30]

## Que sont les itérateurs en Rust ?

Les itérateurs ne sont pas un concept nouveau, ni spécifique à Rust. C'est à la fois un pattern qui est également implémenté comme un objet dans la plupart des langages de programmation pour travailler avec des listes (comme les tableaux ou les vecteurs) ou des collections (comme les HashMaps), vous permettant de parcourir ces types de données et d'agir sur chaque entrée individuelle.

En Rust, les itérateurs sont une fonctionnalité très puissante. Le livre officiel de Rust les décrit ainsi :

> Le pattern iterator vous permet d'effectuer une tâche sur une séquence d'éléments tour à tour. Un itérateur est responsable de la logique d'itération sur chaque élément et de la détermination du moment où la séquence est terminée. Lorsque vous utilisez des itérateurs, vous n'avez pas à réimplémenter cette logique vous-même.
> 
> En Rust, les itérateurs sont *paresseux* (lazy), ce qui signifie qu'ils n'ont aucun effet tant que vous n'appelez pas de méthodes qui consomment l'itérateur pour l'utiliser.

Un itérateur est un objet qui facilite l'accès séquentiel aux éléments d'une collection, comme un tableau ou un vecteur, sans exposer les détails d'implémentation.

### Comment implémenter des itérateurs en Rust

Les itérateurs sont implémentés en Rust à l'aide d'un ensemble de traits, dont le plus fondamental est le trait `Iterator`. Il est implémenté pour toutes les collections de la bibliothèque standard et peut également être implémenté pour des types personnalisés.

> Il nécessite l'implémentation d'une seule méthode : `next()`. Cette méthode retourne une `Option<T>`, où `T` est le type d'élément pour lequel l'itérateur est conçu. Lorsque `next()` est appelée (l'appel est implicite dans la plupart des cas et vous utilisez généralement des méthodes de plus haut niveau), l'itérateur produit `Some(value)` pour l'élément suivant de la séquence ou `None` lorsque l'itération est terminée. Dans la plupart des cas, le fait que la valeur soit `Some` ou `None` est également implicite.

Par exemple, tout ce qui implémente le trait `Iterator` peut être utilisé directement avec une boucle `for`, qui gère implicitement l'appel à la méthode `next` ainsi que la gestion de la valeur `Some` ou `None`. Une valeur `None` déclenche la fin de la boucle. Cela est vrai pour les types intégrés tels que les tableaux, les slices, les vecteurs et les hash-maps.

Par exemple, implémentons le trait iterator sur un type personnalisé simple. Vous devez stocker l'état actuel de l'itérateur dans le type. Vous pouvez également stocker toute information supplémentaire dont vous avez besoin. Ici, nous avons juste besoin de connaître le nombre maximum après lequel l'itération doit s'arrêter :

```
use std::iter::Iterator;

struct CustomType {
    current: usize,
    max: usize,
}

impl CustomType {
    fn new(max: usize) -> Self {
        Self {
            current: 0,
            max,
        }
    }
}

impl Iterator for CustomType {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current >= self.max {
            None
        } else {
            self.current += 1;
            Some(self.current)
        }
    }
}

fn main() {
    let custom = CustomType::new(10);

    for item in custom {
        println!("Item is {item}");
    }
}
```

```
# Output

Item is 1
Item is 2
Item is 3
Item is 4
Item is 5
Item is 6
Item is 7
Item is 8
Item is 9
Item is 10
```

Les itérateurs Rust sont également évalués de manière paresseuse, ce qui signifie qu'ils ne font rien à moins d'être utilisés. Cela signifie que tant que vous ne voulez pas réellement obtenir la valeur suivante et faire quelque chose avec, il ne calculera même pas quelle est cette valeur.

Cela signifie également que si vous avez une chaîne d'opérations, comme un `map` et un `filter`, chaque élément passera d'abord par l'ensemble du pipeline avant que le code ne traite l'élément suivant. C'est différent de nombreux autres langages supportant `map` et `filter` comme méthodes, où le `map` entier sera d'abord traité pour toutes les opérations, puis le `filter` sera effectué.

Si vous y réfléchissez bien, les itérateurs nous permettent d'écrire des pipelines de traitement parallèle de manière beaucoup plus simple que d'autres approches.

Puisque `Iterator` n'est qu'un trait, il permet aux itérateurs d'être chaînables et transformables en d'autres itérateurs à l'aide de diverses méthodes d'adaptation (soit celles de la bibliothèque standard, soit celles que vous pouvez implémenter vous-même).

### Que sont les itérateurs peekable en Rust ?

Souvent, vous avez besoin de savoir quel sera l'élément suivant pour décider de l'action à entreprendre, sans pour autant modifier l'état de l'itérateur pour qu'il passe à l'élément suivant. C'est particulièrement nécessaire lorsque l'on travaille avec un itérateur de tokens pour le parsing, comme nous le ferons plus tard dans ce tutoriel.

C'est là qu'intervient la struct `Peekable`. Vous pouvez convertir n'importe quel itérateur en itérateur peekable en appelant la méthode `peekable` sur celui-ci.

Reprenons l'exemple précédent et voyons comment le mode peekable fonctionne en action :

```
use std::iter::Iterator;

struct CustomType {
    current: usize,
    max: usize,
}

impl CustomType {
    fn new(max: usize) -> Self {
        Self {
            current: 0,
            max,
        }
    }
}

impl Iterator for CustomType {
    type Item = usize;

    fn next(&mut self) -> Option<Self::Item> {
        if self.current >= self.max {
            None
        } else {
            self.current += 1;
            Some(self.current)
        }
    }
}

fn main() {
    let mut custom = CustomType::new(2).peekable();

    let first = custom.peek();
    println!("{first:?}");

    let second = custom.next();
    println!("{second:?}");

    let third = custom.next();
    println!("{third:?}");

    let fourth = custom.next();
    println!("{fourth:?}");
}
```

```
# Output

Some(1)
Some(1)
Some(2)
None
```

Je voulais également vous montrer comment utiliser les itérateurs manuellement sans boucle `for`, c'est pourquoi vous voyez tous les appels à la méthode `next`, et aussi qu'elle retourne une `Option` au lieu de la valeur directement.

Remarquez également que les variables `first` et `second` valent toutes deux `Some(1)`. C'est parce que nous avons appelé `peek` la première fois, ce qui a retourné le premier élément mais sans modifier l'état de l'itérateur.

## Qu'est-ce que l'instruction match en Rust ?

L'instruction `match` est une syntaxe de pattern-matching en Rust qui vous permet d'exécuter du code de manière conditionnelle en fonction de conditions complexes avec une syntaxe concise. Vous pouvez la voir comme une instruction `switch` d'autres langages, mais beaucoup plus puissante.

Un exemple très simple d'instruction match est :

```
let value = true;

match value {
    true => {
        println!("Value is true")
    },
    false => {
        println!("Value is false")
    }
}
```

Les différentes conditions définies ci-dessus, à savoir `true` et `false`, sont appelées des branches (arms). Chaque branche peut avoir une correspondance unique, des correspondances multiples séparées par l'opérateur pipe `|`, et des plages (ranges). Elles peuvent également avoir des gardes (`guards`) et des liaisons (`binding`) pour chaque branche. Voyons ce que chacun de ces termes signifie :

```
// Multiple conditions per branch

let value = "some_string";

match value {
    "some_string1" | "some_string2" | "some_string3" => {
        println!("Bad match");
    }
    "some_string" => {
        println!("Good match");
    }
    _ => {
        println!("No match");
    }
}
```

Notez la branche `_` dans l'exemple ci-dessus. Les instructions match exigent que vous couvriez tous les cas possibles. Dans le premier exemple, comme la valeur était un booléen, il n'y avait que deux valeurs possibles, `true` et `false`. C'est pourquoi dans le premier cas, nous avions déjà couvert toutes les valeurs possibles.

Dans le deuxième exemple cependant, la valeur que nous comparons est une chaîne de caractères (`&str` pour être plus précis). Une chaîne peut avoir n'importe quelle valeur. Il est impossible d'écrire une instruction match qui puisse couvrir tous les cas possibles pour cet exemple. Heureusement, Rust dispose d'un matcher spécial `_` qui correspond à n'importe quelle valeur.

Si vous avez de l'expérience avec JavaScript ou C (ou beaucoup d'autres langages ayant la syntaxe traditionnelle `switch`), `_` est l'équivalent du cas `default` dans un `switch`, mais vous n'êtes pas obligé d'utiliser `_`, vous pouvez également le lier à une variable et le gérer différemment. Nous verrons comment faire cela sous peu.

### Comment utiliser les itérateurs dans les instructions match en Rust

Une instruction match vous permet d'utiliser des itérateurs comme branches. Une correspondance réussie se produit si la valeur comparée est l'une des valeurs de l'itérateur. Par exemple, supposons que vous vérifiez si un type `char` est un chiffre ou non. Vous pouvez écrire un itérateur simple de caractères contenant tous les caractères numériques et l'utiliser comme branche :

```
let value: char = '5';

match value {
    '0'..='9' => {
        println!("Character is a digit");
    }
    _ => {
        println!("Character is not a digit");
    }
}
```

L'exemple ci-dessus affichera "Character is a digit". Si vous n'êtes pas familier avec la syntaxe `..=`, c'est un raccourci pour créer des itérateurs sur une plage. Dans l'exemple ci-dessus, l'itérateur commence au caractère `'0'` et se termine au caractère `'9'`, incluant tous les caractères intermédiaires.

Vous pouvez également utiliser `1..5` pour créer un itérateur sur la plage entre 1 et 5 mais en excluant 5, de sorte que l'itérateur contiendra `1, 2, 3, 4`.

Vous pouvez également utiliser une variable qui contient l'itérateur comme valeur, ce qui signifie que les itérateurs n'ont pas besoin d'être créés en ligne :

```
let list = vec!["1, 2", "3, 4"].iter();
    let value = "3, 4";

    match value {
        list => {
            println!("Matched");
        }
        _ => {
            println!("No matches");
        }
    }
```

Notez que l'exemple appelle `.iter()` sur le vec pour stocker l'itérateur dans la variable `list` et non le vecteur lui-même. Les branches de match ne peuvent pas contenir d'appels de méthodes, il est donc important de convertir la valeur en itérateur en dehors de l'instruction match.

### Que sont les gardes de match en Rust ?

Les gardes (guards) dans les instructions match sont des conditions supplémentaires pour une branche particulière que celle-ci doit satisfaire pour qu'une correspondance soit considérée comme réussie. Par exemple, si vous voulez faire correspondre une plage de nombres, mais aussi vérifier s'ils sont pairs ou impairs, les gardes de match peuvent être utiles.

La syntaxe est assez intuitive. Elle est de la forme `<pattern> if <condition> => {}`.

```
let value: u8 = 5;

match value {
    0..=9 if value % 2 == 0 => {
        println!("Value is even");
    }
    0..=9 if value % 2 == 1 => {
        println!("Value is odd");
    }
    _ => {
        println!("Unexpected value");
    }
}
```

Le code ci-dessus affichera "Value is odd".

### Qu'est-ce que le binding en Rust ?

Le binding (liaison) vous permet de stocker des valeurs dans des variables qui peuvent être utilisées au sein de la branche où le binding est présent. Il s'agit essentiellement d'assigner des variables à certaines parties du pattern.

#### Pattern Binding

Un exemple très simple consiste à lier le pattern "catch-all" à une variable au lieu d'ignorer sa valeur avec `_`.

```
let value: u8 = 5;

match value {
    0..=9 if value % 2 == 0 => {
        println!("Value is even");
    }
    0..=9 if value % 2 == 1 => {
        println!("Value is odd");
    }
    other_value => {
        println!("Unexpected value: {other_value}");
    }
}
```

Remarquez que dans cet exemple, nous avons utilisé la variable `other_value` pour lier la valeur de `value` dans le dernier pattern, qui capture tout si aucun des patterns précédents ne correspond. Nous pouvons ensuite utiliser la variable dans la logique de cette branche. Ici, nous l'affichons simplement dans la console.

D'autres exemples de binding sont :

```
let value: Option<i32> = Some(43);

match value {
    Some(matched_value) => println!("The value is {matched_value}"),
    None => println!("There is no value")
}
```

Dans cet exemple, nous avons lié la valeur à l'intérieur du pattern `Some` pour stocker la valeur interne de l'option, et l'utiliser dans notre logique.

```
pub struct Person {
    name: String,
    age: u32,
}

let value: Option<Person> = Some(Person {
    name: "Name".to_string(),
    age: 23,
});

match value {
    Some(Person { name: person_name, age }) => {
        println!("{person_name} is {age} years old");
    },
    None => {
        println!("The value is empty");
    }
}
```

Nous voyons deux types de binding différents dans cet exemple. Le premier consiste à assigner un nom différent à un champ de struct en le déstructurant (champ `name`), et l'autre consiste à utiliser le même nom que celui du champ (champ `age`).

#### Le Binding `@`

Le livre officiel de Rust le décrit ainsi :

> L'opérateur at @ nous permet de créer une variable qui contient une valeur en même temps que nous testons cette valeur pour une correspondance de pattern.

Dans notre exemple de pattern matching contre une plage de valeurs, ou contre un itérateur, nous pouvons lier la valeur correspondante à une variable en utilisant cette syntaxe pour l'utiliser dans cette branche :

```
let value: u8 = 5;

match value {
    digit @ 0..=9 => {
        println!("The matched value is {digit}");
    }
    _ => {
        println!("Unexpected value");
    }
}
```

Ici, nous lions la valeur correspondante de l'itérateur à la variable `digit`, que nous utilisons ensuite dans la branche pour lire la valeur réelle.

## Comment construire un parseur JSON – Étape 1 : Le Reader

Avant de pouvoir parser les données JSON entrantes, nous devons être capables de les lire d'une manière qui facilite le parsing. Pour pouvoir tokeniser le JSON entrant, nous devons analyser chaque caractère au fur et à mesure qu'il arrive, et selon qu'il représente une valeur littérale, ou un délimiteur (ou une valeur invalide), décider quoi en faire ainsi que des caractères suivants.

C'est un excellent cas d'utilisation pour une combinaison d'itérateurs et de la syntaxe match de Rust.

Notre reader doit contenir deux éléments de données. Un reader bufferisé grâce auquel nous pouvons itérer sur l'entrée, et un `character_buffer`, qui contiendra le caractère actuel en cours de décodage.

À ce stade, vous pourriez demander pourquoi nous devons conserver le buffer de caractères dans le reader, et la raison est que le JSON est encodé en UTF-8.

### Qu'est-ce que l'encodage d'octets UTF-8 ?

Un caractère UTF-8 peut mesurer entre 1 et 4 octets. Nous devons être capables de parser tous les caractères valides car la spécification JSON supporte ces caractères. Cela signifie que les caractères JSON peuvent être longs de 1, 2, 3 ou 4 octets.

Pour chaque itération, nous devons lire 4 octets à la fois, décider combien de caractères ces 4 octets contiennent (par exemple, ces 4 octets peuvent contenir 4 caractères de 1 octet), finir d'itérer sur eux, puis passer à la lecture des 4 octets suivants et répéter le processus. Pour stocker cette information intermédiaire, nous avons besoin du buffer de caractères.

Il est également possible que nous n'ayons qu'une partie du caractère dans les 4 octets actuels. Par exemple, si vous considérez 2 caractères de 1 octet suivis d'un caractère de 3 octets comme `23€`, les 4 premiers octets contiendront 2 caractères valides et seulement une partie du caractère valide suivant. Vous devez également être capable de gérer cela, ce qui impliquera de revenir en arrière dans l'itérateur.

Il est possible de gérer cela d'une manière qui ne nécessite pas d'allocations, et pour des raisons de performance, il est en fait préférable de le faire. Mais je vous laisse, en tant que lecteur, réfléchir à la manière de l'implémenter dans ce cas, car ce n'est pas le sujet principal de cet article.

J'espère qu'il est maintenant clair pourquoi les itérateurs sont le meilleur outil pour cette tâche.

### Comment lire les données

Nous allons supporter deux readers différents. L'un provient directement d'un reader bufferisé (qui est le plus souvent créé à partir d'un fichier), et l'autre d'un itérateur sur des octets.

Ceux-ci vont être assez simples. Pour lire à partir d'un fichier, vous devez créer un curseur bufferisé sur les données du fichier sous-jacent :

```
let file = File::create("dummy.json").unwrap();
let reader = BufReader::new(file);
```

Commençons par implémenter la struct JSON Reader et ces méthodes sur celle-ci :

```
// src/reader.rs

use std::collections::VecDeque;
use std::io::{BufReader, Cursor, Read, Seek};
use std::str::from_utf8;

/// A struct that handles reading input data to be parsed and
/// provides an iterator over said data character-by-character.
pub struct JsonReader<T>
where
    T: Read + Seek,
{
    /// A reference to the input data, which can be anything
    /// that implements [`Read`]
    reader: BufReader<T>,

    /// A character buffer that holds queue of characters to
    /// be used by the iterator.
    ///
    /// This is necessary because UTF-8 can be 1-4 bytes long.
    /// Because of this, the reader always reads 4 bytes at a 
    /// time. We then iterate over "characters", irrespective of 
    /// whether they are 1 byte long, or 4.
    ///
    /// A [`VecDeque`] is used instead of a normal vector 
    /// because characters need to be read out from the start 
    /// of the buffer.
    character_buffer: VecDeque<char>,
}

impl<T> JsonReader<T>
where
    T: Read + Seek,
{
    /// Create a new [`JsonReader`] that reads from a file
    ///
    /// # Examples
    ///
    /// ```rust
    /// use std::fs::File;
    /// use std::io::BufReader;
    /// use json_parser::reader::JsonReader;
    ///
    /// let file = File::create("dummy.json").unwrap();
    /// let reader = BufReader::new(file);
    ///
    /// let json_reader = JsonReader::new(reader);
    /// ```
    pub fn new(reader: BufReader<T>) -> Self {
        JsonReader {
            reader,
            character_buffer: VecDeque::with_capacity(4),
        }
    }

    /// Create a new [`JsonReader`] that reads from a given byte stream
    ///
    /// # Examples
    ///
    /// ```rust
    /// use std::io::{BufReader, Cursor};
    /// use json_parser::reader::JsonReader;
    ///
    /// let input_json_string = r#"{"key1":"value1","key2":"value2"}"#;
    ///
    /// let json_reader = JsonReader::<Cursor<&'static [u8]>>::from_bytes(input_json_string.as_bytes());
    /// ```
    #[must_use]
    pub fn from_bytes(bytes: &[u8]) -> JsonReader<Cursor<&[u8]>> {
        JsonReader {
            reader: BufReader::new(Cursor::new(bytes)),
            character_buffer: VecDeque::with_capacity(4),
        }
    }
}
```

### Comment implémenter l'itérateur pour `JsonReader`

Ensuite, vous allez devoir implémenter le trait `Iterator` sur ce `JsonReader`, ce qui facilitera le parsing.

Tout d'abord, si le buffer de caractères n'est pas déjà vide, vous pouvez retourner le premier caractère du buffer depuis l'itérateur :

```rust
if !self.character_buffer.is_empty() {
    return self.character_buffer.pop_front();
}
```

S'il est vide, vous devez créer un nouveau buffer et lire dans ce buffer à partir du reader :

```rust
let mut utf8_buffer = [0, 0, 0, 0];
let _ = self.reader.read(&mut utf8_buffer);
```

Ici, vous créez un nouveau tableau de taille 4, et vous allez lire 4 octets dedans à partir du reader.

Ensuite, vous devez le parser en tant qu'UTF-8. Rust vous fournit une fonction `from_utf8` qui tentera de parser les octets donnés en UTF-8. Elle retourne une chaîne contenant les caractères parsés si elle était valide.

Elle retourne une erreur avec le nombre d'octets invalides dans les informations d'erreur, que vous pouvez utiliser pour faire reculer le reader afin de ne conserver que les caractères valides, et essayer les 4 caractères suivants à partir du point d'échec.

Si cela ne vous semble pas très clair, regarder le code rendra les choses limpides :

```rust
match from_utf8(&utf8_buffer) {
    Ok(string) => {
        self.character_buffer = string.chars().collect();
        self.character_buffer.pop_front()
    }
    Err(error) => {
        // Read valid bytes, and rewind the buffered reader for 
        // the remaining bytes so that they can be read again in the
        // next iteration.

        let valid_bytes = error.valid_up_to();
        let string = from_utf8(&utf8_buffer[..valid_bytes]).unwrap();

        let remaining_bytes = 4 - valid_bytes;

        let _ = self.reader.seek_relative(-(remaining_bytes as i64));

        // Collect the valid characters into character_buffer
        self.character_buffer = string.chars().collect();

        // Return the first character from character_buffer
        self.character_buffer.pop_front()
    }
}
```

Voici l'implémentation complète du trait `Iterator` :

```rust
// src/reader.rs

impl<T> Iterator for JsonReader<T>
where
    T: Read + Seek,
{
    type Item = char;

    #[allow(clippy::cast_possible_wrap)]
    fn next(&mut self) -> Option<Self::Item> {
        if !self.character_buffer.is_empty() {
            return self.character_buffer.pop_front();
        }

        let mut utf8_buffer = [0, 0, 0, 0];
        let _ = self.reader.read(&mut utf8_buffer);

        match from_utf8(&utf8_buffer) {
            Ok(string) => {
                self.character_buffer = string.chars().collect();
                self.character_buffer.pop_front()
            }
            Err(error) => {
                // Read valid bytes, and rewind the buffered reader for
                // the remaining bytes so that they can be read again in the
                // next iteration.

                let valid_bytes = error.valid_up_to();
                let string = from_utf8(&utf8_buffer[..valid_bytes]).unwrap();

                let remaining_bytes = 4 - valid_bytes;

                let _ = self.reader.seek_relative(-(remaining_bytes as i64));

                // Collect the valid characters into character_buffer
                self.character_buffer = string.chars().collect();

                // Return the first character from character_buffer
                self.character_buffer.pop_front()
            }
        }
    }
}
```

Et c'est tout ce que vous avez à faire pour lire les données d'entrée pour le parsing. Il est temps de passer à l'étape suivante du processus.

## Comment construire un parseur JSON – Étape 2 : Préparer les types de données intermédiaires

Ce n'est pas vraiment une étape dans le pipeline de parsing, mais c'est un prérequis pour les étapes suivantes. Nous devons définir des types Rust qui correspondent à tous les types possibles supportés par JSON.

JSON supporte les types de données suivants :

-   String
-   Number
-   Boolean
-   Array
-   Object
-   Null

Un nombre peut en outre être soit un entier, soit un nombre à virgule flottante. Bien que vous puissiez utiliser `f64` comme type Rust pour tous les nombres JSON, ce n'est pas pratique car cela parsemerait votre code de casts de types partout où vous essayeriez de l'utiliser.

Donc, dans ce tutoriel, nous allons effectivement faire cette distinction et enregistrer ce fait.

### Le type value

Les enums sont le moyen idéal pour stocker un état comme celui-ci, où chaque variante doit avoir un identifiant comme métadonnée (dans ce cas le type de valeur JSON), et optionnellement des données attachées. Les données que vous allez attacher à ces variantes seront la valeur réelle de ce type en JSON.

```rust
// src/value.rs

use std::collections::HashMap;

#[derive(Debug, Copy, Clone, PartialEq)]
pub enum Number {
    I64(i64),
    F64(f64),
}

#[derive(Debug, PartialEq, Clone)]
pub enum Value {
    String(String),
    Number(Number),
    Boolean(bool),
    Array(Vec<Value>),
    Object(HashMap<String, Value>),
    Null,
}
```

Les premières variantes sont assez simples, vous définissez la variante et la donnée qu'elle contient est un type Rust correspondant. La dernière variante est encore plus simple, représentant la valeur `null` qui n'a pas besoin de données supplémentaires pour être stockée.

Les variantes `Array` et `Object` sont cependant un peu plus intéressantes, car elles stockent récursivement l'Enum lui-même. C'est logique, car les tableaux en JSON peuvent avoir n'importe quel type de valeur supporté par la spécification JSON. Et les objets en JSON ont toujours des clés de type chaîne et n'importe quelle valeur supportée par JSON, y compris d'autres objets.

### Comment ajouter des méthodes de conversion utiles

Vous aurez également besoin d'un moyen de convertir le type enum en types sous-jacents, et de renvoyer une erreur si la donnée sous-jacente n'est pas celle attendue. Il s'agit principalement de code répétitif (boilerplate), je vais donc tout mettre ensemble sans plus d'explications :

```rust
// src/value.rs

impl TryFrom<&Value> for String {
    type Error = ();

    fn try_from(value: &Value) -> Result<Self, ()> {
        match value {
            Value::String(value) => Ok(value.clone()),
            _ => Err(()),
        }
    }
}

impl TryFrom<&Value> for i64 {
    type Error = ();

    #[allow(clippy::cast_possible_truncation)]
    fn try_from(value: &Value) -> Result<Self, ()> {
        match value {
            Value::Number(value) => match value {
                Number::I64(value) => Ok(*value),
                Number::F64(value) => Ok(*value as i64),
            },
            _ => Err(()),
        }
    }
}

impl TryFrom<&Value> for f64 {
    type Error = ();

    fn try_from(value: &Value) -> Result<Self, ()> {
        match value {
            Value::Number(value) => match value {
                Number::F64(value) => Ok(*value),
                Number::I64(value) => Ok(*value as f64),
            },
            _ => Err(()),
        }
    }
}

impl TryFrom<&Value> for bool {
    type Error = ();

    fn try_from(value: &Value) -> Result<Self, ()> {
        match value {
            Value::Boolean(value) => Ok(*value),
            _ => Err(()),
        }
    }
}

impl<'a> TryFrom<&'a Value> for &'a Vec<Value> {
    type Error = ();

    fn try_from(value: &'a Value) -> Result<Self, ()> {
        match value {
            Value::Array(value) => Ok(value),
            _ => Err(()),
        }
    }
}

#[allow(clippy::implicit_hasher)]
impl<'a> TryFrom<&'a Value> for &'a HashMap<String, Value> {
    type Error = ();

    fn try_from(value: &'a Value) -> Result<Self, ()> {
        match value {
            Value::Object(value) => Ok(value),
            _ => Err(()),
        }
    }
}
```

## Comment construire un parseur JSON – Étape 3 : Tokenisation

L'étape suivante consiste à prendre les données d'entrée et à les tokeniser.

La tokenisation est le processus consistant à diviser un gros bloc d'entrée en unités plus petites et plus digestes qui peuvent ensuite être analysées indépendamment. Cela vous permet également de travailler avec elles beaucoup plus facilement que de simples flux d'octets ; elles aident à représenter les données entrantes sous une forme standard et permettent de mapper les tokens aux types de valeurs de sortie.

Le parseur peut ensuite traiter récursivement tous les tokens jusqu'à ce qu'il n'y ait plus rien à traiter, nous donnant les données parsées une fois terminé.

### Comment définir les tokens valides attendus

Il va y avoir une certaine duplication ici par rapport au type de valeur que vous avez examiné précédemment, mais c'est normal, car la représentation en token de toute valeur littérale sera cette valeur elle-même. Il n'y a aucun moyen de la décomposer en unités plus petites dans ce cas.

Encore une fois, l'Enum est le bon type de données pour cela puisque nous avons besoin à la fois de métadonnées (comme le type de token), et optionnellement de données associées.

Les tokens représentant des valeurs littérales peuvent être définis de cette manière :

```rust
// src/token.rs

use std::io::{Read, Seek};
use std::iter::Peekable;
use crate::reader::JsonReader;

#[derive(Debug, Copy, Clone, PartialEq)]
pub enum Number {
    I64(i64),
    F64(f64),
}

#[derive(Debug, Clone, PartialEq)]
pub enum Token {
    String(String),
    Number(Number),
    Boolean(bool),
    Null,
}
```

En dehors de ceux-ci, nous avons également beaucoup d'autres tokens en JSON qui forment la "grammaire" du format JSON. Ce sont :

-   Les accolades (`{` ou `}`) qui représentent respectivement l'ouverture et la fermeture d'un objet.
-   Les crochets (`[` ou `]`) qui représentent respectivement l'ouverture et la fermeture d'un tableau.
-   Le deux-points (`:`) pour séparer les paires clé-valeur au sein de l'objet.
-   La virgule (`,`) pour séparer les valeurs.
-   Les guillemets (`"`) qui représentent l'ouverture/fermeture des valeurs littérales de chaîne.

Tous ces éléments n'ont pas besoin de données associées, ils seront donc des variantes unitaires dans l'enum. En les ajoutant, l'enum complet sera :

```rust
// src/token.rs

use std::io::{Read, Seek};
use std::iter::Peekable;
use crate::reader::JsonReader;
use crate::value::Number;

#[derive(Debug, Clone, PartialEq)]
pub enum Token {
    CurlyOpen,
    CurlyClose,
    Quotes,
    Colon,
    String(String),
    Number(Number),
    ArrayOpen,
    ArrayClose,
    Comma,
    Boolean(bool),
    Null,
}
```

### Comment implémenter la struct tokenizer

Vous allez avoir besoin d'une struct `JsonTokenizer` qui peut faciliter le processus tout en étant responsable de la conservation de l'état du processus de tokenisation :

```rust
// src/token.rs

pub struct JsonTokenizer<T>
    where
        T: Read + Seek,
{
    tokens: Vec<Token>,
    iterator: Peekable<JsonReader<T>>,
}

impl<T> JsonTokenizer<T>
where
    T: Read + Seek,
{
    pub fn new(reader: T) -> JsonTokenizer<T> {
        let json_reader = JsonReader::<T>::new(BufReader::new(reader));

        JsonTokenizer {
            iterator: json_reader.peekable(),
            tokens: vec![],
        }
    }

    pub fn from_bytes<'a>(input: &'a [u8]) -> JsonTokenizer<Cursor<&'a [u8]>> {
        let json_reader = JsonReader::<Cursor<&'a [u8]>>::from_bytes(input);

        JsonTokenizer {
            iterator: json_reader.peekable(),
            tokens: Vec::with_capacity(input.len()),
        }
    }
}
```

Dans ce cas, nous l'avons rendu générique par rapport à la provenance de l'entrée. Le type T doit implémenter les traits `Read` & `Seek`, dont la raison est expliquée peu après.

L'itérateur doit également être `Peekable`, ce qui signifie essentiellement que nous devrions être capables de lire l'élément suivant dans l'itérateur sans faire avancer l'itérateur lui-même.

### Comment tokeniser un itérateur de caractères

Une fois que vous avez défini tous les tokens attendus, vous devez prendre votre itérateur de caractères et le convertir en une liste de tokens, où chaque entrée est une variante de l'enum `Token` défini dans la section précédente.

Nous allons commencer par écrire une fonction squelette qui fait un match sur le caractère entrant et panique s'il rencontre un token invalide :

```rust
// src/token.rs

impl<T> JsonTokenizer<T> where
    T: Read + Seek, {
    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // Parse all other tokens here
                // ...
                character => {
                    if character.is_ascii_whitespace() {
                        let _ = self.iterator.next();
                        continue;
                    }

                    panic!("Unexpected character: ;{character};")
                }
            }
        }

        Ok(&self.tokens)
    }
}
```

Il y a deux choses notables ici, commençons par la plus simple. Si votre bloc match ne rencontre aucun caractère connu (vous allez implémenter cela sous peu), vous devez avoir une condition "catch-all" qui correspond à n'importe quel caractère.

Ici, nous allons ignorer tous les caractères d'espacement et passer à l'itération suivante s'il en rencontre un. Si le caractère n'est pas un espacement, alors vous devez paniquer (ou retourner une erreur) ici.

La chose suivante notable ici est `self.iterator.peek()`. Pour faciliter le parsing de différents types de tokens, des délimiteurs aux valeurs littérales, il est important que l'itérateur ne soit pas avancé lors de la lecture du caractère suivant. Cela doit se produire afin que vous puissiez l'avancer conditionnellement en fonction du caractère suivant.

Vous devez également déléguer le parsing de certains ensembles de tokens à différentes fonctions, qui auront leur propre logique pour faire avancer l'itérateur.

Un bon exemple est le parsing de la valeur littérale `null`. Si le match rencontre un caractère `n` et n'est pas à l'intérieur d'une chaîne, d'un objet, d'un nombre, etc., alors vous devez vous assurer que les trois caractères suivants sont respectivement `u`, `l`, `l` pour former la valeur littérale `null`, puis faire avancer l'itérateur de quatre pour que la boucle suivante commence le parsing après le caractère `null` et non au milieu de celui-ci.

### Comment parser les tokens de chaîne

Nous allons commencer par parser les chaînes. Arrêtons-nous une seconde et réfléchissons à ce qui doit se passer étape par étape :

-   Vérifier si le match rencontre un caractère `"`. Si c'est le cas, pousser `Token::Quotes` à votre liste de tokens de sortie.
-   Faire avancer l'itérateur d'un cran pour que les étapes suivantes commencent après le caractère `"`.
-   Parser tous les caractères faisant partie de la chaîne jusqu'à ce que vous rencontriez un autre caractère `"` qui indique la fermeture de la valeur de chaîne.
-   Faire avancer l'itérateur d'autant de caractères qu'il y en a dans la chaîne, plus un supplémentaire pour sauter par-dessus le caractère `"` de fermeture.
-   Pousser `Token::String` avec la valeur parsée à votre liste de tokens de sortie.
-   Pousser `Token::Quotes` à votre liste de tokens de sortie.

J'espère que ce n'est pas trop confus. Mais le code devrait vous aider à mieux comprendre :

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                '"' => {
                    // Pushed opening quote to output tokens list.
                    self.tokens.push(Token::Quotes);

                    // Skip quote token since we already added it to the tokens list.
                    let _ = self.iterator.next();

                    // Delegate parsing string value to a separate function.
                    // The function should also take care of advancing the iterator properly.
                    let string = self.parse_string();

                    // Push parsed string to output tokens list.
                    self.tokens.push(Token::String(string));

                    // Pushed closing quote to output tokens list.
                    self.tokens.push(Token::Quotes);
                }
                // ...
            }
        }

        Ok(&self.tokens)
    }

    fn parse_string(&mut self) -> String {
        // Create new vector to hold parsed characters.
        let mut string_characters = Vec::<char>::new();

        // Take each character by reference so that they
        // aren't moved out of the iterator, which will
        // require you to move the iterator into this
        // function.
        for character in self.iterator.by_ref() {
            // If it encounters a closing `"`, break
            // out of the loop as the string has ended.
            if character == '"' {
                break;
            }

            // Continue pushing to the vector to build
            // the string.
            string_characters.push(character);
        }

        // Create a string out of character iterator and
        // return it.
        String::from_iter(string_characters)
    }
}
```

Comme je l'ai mentionné précédemment, nous n'allons pas traiter la gestion des caractères d'échappement dans ce tutoriel, car ils n'apportent pas beaucoup de valeur à l'apprentissage du sujet présent, mais si cela vous intéresse, ce sera un bon exercice pour vous de les ajouter par-dessus l'implémentation.

Cela s'occupe du parsing de la chaîne, nous pouvons passer à un type de valeur plus intéressant ensuite.

### Comment parser les tokens de nombre

Les nombres dans la spécification JSON présentent beaucoup de variations. Ils peuvent être positifs ou négatifs, entiers ou décimaux. Ils peuvent également être définis en notation scientifique (par exemple exponentielle négative `3.7e-5` ou exponentielle positive `3.7e5`). Et nous devons parser toutes ces variations.

Comme toujours, nous allons commencer par la partie facile. Si nous rencontrons un caractère qui peut être un caractère valide dans un nombre, vous devez déléguer le parsing à une fonction `parse_number`. De plus, tout nombre valide ne peut commencer que par un chiffre ou un signe moins. Un nombre ne peut pas commencer par un caractère décimal ou un caractère epsilon, ce qui nous facilite les choses.

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // ...

                '-' | '0'..='9' => {
                    let number = self.parse_number()?;
                    self.tokens.push(Token::Number(number));
                }

                // ...
            }
        }

        Ok(&self.tokens)
    }

    // ...
}
```

Ensuite, nous allons implémenter la méthode `parse_number` :

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    fn parse_number(&mut self) -> Result<Number, ()> {
        // Store parsed number characters.
        let mut number_characters = Vec::<char>::new();

        // Stores whether the digit being parsed is after a `.` character
        // making it a decimal.
        let mut is_decimal = false;

        // Stores the characters after an epsilon character `e` or `E`
        // to indicate the exponential value.
        let mut epsilon_characters = Vec::<char>::new();

        // Stores whether the digit being parsed is part of the epsilon
        // characters.
        let mut is_epsilon_characters = false;

        while let Some(character) = self.iterator.peek() {
            match character {
                // Match the negative sign character that indicates whether number is negative
                '-' => {
                    if is_epsilon_characters {
                        // If it's parsing epsilon characters, push it to the epsilon
                        // character set.
                        epsilon_characters.push('-');
                    } else {
                        // Otherwise, push it to normal character set.
                        number_characters.push('-');
                    }

                    // Advance the iterator by 1.
                    let _ = self.iterator.next();
                }
                // Match a positive sign, which can be treated as redundant and ignored since
                // positive is the default.
                '+' => {
                    // Advance the iterator by 1.
                    let _ = self.iterator.next();
                }
                // Match any digit between 0 and 9, and store it into the `digit`
                // variable.
                digit @ '0'..='9' => {
                    if is_epsilon_characters {
                        // If it's parsing epsilon characters, push it to the epsilon
                        // character set.
                        epsilon_characters.push(*digit);
                    } else {
                        // Otherwise, push it to normal character set.
                        number_characters.push(*digit);
                    }
                    // Advance the iterator by 1.
                    let _ = self.iterator.next();
                }
                // Match the period character which indicates start of the fractional
                // part of a decimal number.
                '.' => {
                    // Push the decimal character to numbers character set.
                    number_characters.push('.');

                    // Set the current state of number being decimal to true.
                    is_decimal = true;

                    // Advance the iterator by 1.
                    let _ = self.iterator.next();
                }
                // Match any of the characters that can signify end of the number
                // literal value. This can be a comma which separates key-value pair,
                // closing object character, closing array character, or a `:` which
                // separates a key from its value.
                '}' | ',' | ']' | ':' => {
                    break;
                }
                // Match the epsilon character which indicates that the number is in
                // scientific notation.
                'e' | 'E' => {
                    // Panic if it's already parsing an exponential number since this would
                    // mean there are 2 epsilon characters which is invalid.
                    if is_epsilon_characters {
                        panic!("Unexpected character while parsing number: {character}. Double epsilon characters encountered");
                    }

                    // Set the current state of number being in scientific notation to true.
                    is_epsilon_characters = true;

                    // Advance the iterator by 1.
                    let _ = self.iterator.next();
                }
                // Panic if any other character is encountered.
                other => {
                    if !other.is_ascii_whitespace() {
                        panic!("Unexpected character while parsing number: {character}")
                    } else {
                        self.iterator.next();
                    }
                },
            }
        }

        if is_epsilon_characters {
            // if the number is an exponential, perform the calculations to convert it
            // to a floating point number in rust.

            // Parse base as floating point number.
            let base: f64 = String::from_iter(number_characters).parse().unwrap();

            // Parse exponential as floating point number.
            let exponential: f64 = String::from_iter(epsilon_characters).parse().unwrap();

            // Return the final computed decimal number.
            Ok(Number::F64(base * 10_f64.powf(exponential)))
        } else if is_decimal {
            // if the number is a decimal, parse it as a floating point number in rust.
            Ok(Number::F64(
                String::from_iter(number_characters).parse::<f64>().unwrap(),
            ))
        } else {
            // Parse the number as an integer in rust.
            Ok(Number::I64(
                String::from_iter(number_characters).parse::<i64>().unwrap(),
            ))
        }
    }
}
```

Il vous est conseillé de parcourir le code et de lire les commentaires pour comprendre cette fonction. Vous ne devriez rencontrer aucune nouvelle syntaxe qui ne soit déjà couverte ou supposée connue par le lecteur.

### Comment parser les tokens booléens

Le parsing des booléens va être le plus simple que nous ayons vu jusqu'à présent. Tout ce que nous avons à faire est de faire correspondre `t` ou `f` comme premier caractère, puis de vérifier les quelques caractères suivants pour s'assurer qu'ils forment la valeur littérale `true` ou `false`.

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // ...

                // Match `t` character which indicates beginning of a boolean literal.
                't' => {
                    // Advance iterator by 1.
                    let _ = self.iterator.next();

                    // Assert next character is `r` while advancing the iterator by 1.
                    assert_eq!(Some('r'), self.iterator.next());
                    // Assert next character is `u` while advancing the iterator by 1.
                    assert_eq!(Some('u'), self.iterator.next());
                    // Assert next character is `e` while advancing the iterator by 1.
                    assert_eq!(Some('e'), self.iterator.next());

                    // Push the literal value to token list.
                    self.tokens.push(Token::Boolean(true));
                }
                'f' => {
                    // Advance iterator by 1.
                    let _ = self.iterator.next();

                    // Assert next character is `a` while advancing the iterator by 1.
                    assert_eq!(Some('a'), self.iterator.next());
                    // Assert next character is `l` while advancing the iterator by 1.
                    assert_eq!(Some('l'), self.iterator.next());
                    // Assert next character is `s` while advancing the iterator by 1.
                    assert_eq!(Some('s'), self.iterator.next());
                    // Assert next character is `e` while advancing the iterator by 1.
                    assert_eq!(Some('e'), self.iterator.next());

                    // Push the literal value to token list.
                    self.tokens.push(Token::Boolean(false));
                }

                // ...
            }
        }

        Ok(&self.tokens)
    }
}
```

### Comment parser le littéral Null

C'est très similaire à la façon dont nous avons parsé les booléens à l'étape précédente :

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // ...

                'n' => {
                    // Advance iterator by 1.
                    let _ = self.iterator.next();

                    // Assert next character is `u` while advancing the iterator by 1.
                    assert_eq!(Some('u'), self.iterator.next());
                    // Assert next character is `l` while advancing the iterator by 1.
                    assert_eq!(Some('l'), self.iterator.next());
                    // Assert next character is `l` while advancing the iterator by 1.
                    assert_eq!(Some('l'), self.iterator.next());

                    // Push null literal value to output tokens list.
                    self.tokens.push(Token::Null);
                }

                // ...
            }
        }

        Ok(&self.tokens)
    }
}
```

### Comment parser les délimiteurs

Le parsing des délimiteurs est très simple. Tout ce que vous avez à faire est de faire un match sur eux, et de pousser le token respectif dans la liste des tokens de sortie :

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // ...

                '{' => {
                    self.tokens.push(Token::CurlyOpen);
                    let _ = self.iterator.next();
                }
                '}' => {
                    self.tokens.push(Token::CurlyClose);
                    let _ = self.iterator.next();
                }
                '[' => {
                    self.tokens.push(Token::ArrayOpen);
                    let _ = self.iterator.next();
                }
                ']' => {
                    self.tokens.push(Token::ArrayClose);
                    let _ = self.iterator.next();
                }
                ',' => {
                    self.tokens.push(Token::Comma);
                    let _ = self.iterator.next();
                }
                ':' => {
                    self.tokens.push(Token::Colon);
                    let _ = self.iterator.next();
                }

                // ...
            }
        }

        Ok(&self.tokens)
    }
}
```

### Comment parser un caractère de terminaison

L'entrée peut parfois contenir `\0` comme dernier caractère pour indiquer que l'entrée est terminée. C'est plus communément connu sous le nom d'EOF (End Of File) lorsqu'on traite des fichiers. On l'appelle aussi par d'autres noms comme "séquence d'échappement" ou caractère "null".

Nous devons le gérer et sortir de notre boucle de parsing si nous le rencontrons :

```rust
// src/token.rs

impl<T> JsonTokenizer<T>
    where
        T: Read + Seek,
{
    // ...

    pub fn tokenize_json(&mut self) -> Result<&[Token], ()> {
        while let Some(character) = self.iterator.peek() {
            match *character {
                // ...

                '\0' => break,
                other => {
                    if !other.is_ascii_whitespace() {
                        panic!("Unexpected token encountered: {other}")
                    } else {
                        self.iterator.next();
                    }
                },

                // ...
            }
        }

        Ok(&self.tokens)
    }
}
```

## Comment construire un parseur JSON – Étape 4 : Des tokens à la valeur

Maintenant que vous avez tous les tokens, il est temps de passer à l'étape finale du processus : convertir les tokens en valeurs réelles que vous pouvez manipuler dans le code Rust.

Commencez par créer une struct unitaire, qui peut être utilisée comme parseur. À ce stade, nous n'avons pas besoin de conserver d'état pour l'ensemble du processus :

```rust
// src/parser.rs

use std::collections::HashMap;
use std::fs::File;
use std::io::{BufReader, Cursor};
use std::iter::Peekable;
use std::slice::Iter;
use crate::token::{JsonTokenizer, Token};
use crate::value::Value;

/// Main parser which is the entrypoint for parsing JSON.
pub struct JsonParser;
```

Nous allons également l'utiliser comme interface publique pour le parseur. Commençons donc par implémenter ces méthodes en premier :

```rust
// src/parser.rs

impl JsonParser {
    /// Create a new [`JsonParser`] that parses JSON from bytes.
    pub fn parse_from_bytes<'a>(input: &'a [u8]) -> Result<Value, ()> {
        let mut json_tokenizer = JsonTokenizer::<Cursor<&[u8]>>::from_bytes(input);
        let tokens = json_tokenizer.tokenize_json()?;

        Ok(Self::tokens_to_value(tokens))
    }

    /// Create a new [`JsonParser`] that parses JSON from file.
    pub fn parse(reader: File) -> Result<Value, ()> {
        let mut json_tokenizer = JsonTokenizer::<File>::new(reader);
        let tokens = json_tokenizer.tokenize_json()?;

        Ok(Self::tokens_to_value(tokens))
    }
}
```

Ceci étant fait, vous devez d'abord implémenter la méthode `tokens_to_value` que ces méthodes publiques appellent.

### Comment parser les primitifs

Cette méthode sera responsable de prendre un itérateur de tokens en entrée et de produire le type `Value` que vous avez défini précédemment. C'est également assez simple, puisque le parsing des objets/tableaux est délégué à des méthodes séparées, que nous examinerons sous peu.

```rust
// src/parser.rs

impl JsonParser {
    // ...

    fn tokens_to_value(tokens: &[Token]) -> Value {
        // Create a peekable iterator over tokens
        let mut iterator = tokens.iter().peekable();

        // Initialize final value to null.
        let mut value = Value::Null;

        // Loop while there are tokens in the iterator.
        // Note that you do not need to manually handle advancing the
        // iterator in this case which is why you can directly call
        // `iterator.next()`.
        while let Some(token) = iterator.next() {
            match token {
                Token::CurlyOpen => {
                    value = Value::Object(Self::process_object(&mut iterator));
                }
                Token::String(string) => {
                    value = Value::String(string.clone());
                }
                Token::Number(number) => {
                    value = Value::Number(*number);
                }
                Token::ArrayOpen => {
                    value = Value::Array(Self::process_array(&mut iterator));
                }
                Token::Boolean(boolean) => value = Value::Boolean(*boolean),
                Token::Null => value = Value::Null,
                // Ignore all delimiters as you don't need to explicitly do anything
                // when you encounter them.
                Token::Comma
                | Token::CurlyClose
                | Token::Quotes
                | Token::Colon
                | Token::ArrayClose => {}
            }
        }

        value
    }
}
```

### Comment parser les tableaux

Le parsing des tableaux est presque aussi simple que la logique de parsing que nous avons examinée ci-dessus. Comme les tableaux ne sont que des collections d'autres valeurs JSON, il n'y a pas beaucoup de logique impliquée dans leur parsing, contrairement aux objets.

```rust
// src/parser.rs

impl JsonParser {
    fn process_array(iterator: &mut Peekable<Iter<Token>>) -> Vec<Value> {
        // Initialise a vector of JSON Value type to hold the value of
        // array that's currently being parsed.
        let mut internal_value = Vec::<Value>::new();

        // Iterate over all tokens provided.
        while let Some(token) = iterator.next() {
            match token {
                Token::CurlyOpen => {
                    internal_value.push(Value::Object(Self::process_object(iterator)));
                }
                Token::String(string) => internal_value.push(Value::String(string.clone())),
                Token::Number(number) => internal_value.push(Value::Number(*number)),
                Token::ArrayOpen => {
                    internal_value.push(Value::Array(Self::process_array(iterator)));
                }
                // Break loop if array is closed. Due to recursive nature of process_array,
                // we don't need to explicitly check if the closing token matches the opening
                // one.
                Token::ArrayClose => {
                    break;
                }
                Token::Boolean(boolean) => internal_value.push(Value::Boolean(*boolean)),
                Token::Null => internal_value.push(Value::Null),
                // Ignore delimiters
                Token::Comma | Token::CurlyClose | Token::Quotes | Token::Colon => {}
            }
        }

        internal_value
    }
}
```

### Comment parser les objets

Le parsing des objets est un peu plus délicat que les types de valeurs précédents, car les objets viennent avec leur propre syntaxe. Mais il ne devrait pas y avoir de surprises pour vous, c'est pourquoi je vous encourage à lire le code et les commentaires ci-dessous pour comprendre comment cela fonctionne.

```rust
// src/parser.rs

impl JsonParser {
    fn process_object(iterator: &mut Peekable<Iter<Token>>) -> HashMap<String, Value> {
        // Whether the item being parsed is a key or a value. The first element
        // should always be a key so this is initialised to true.
        let mut is_key = true;

        // The current key for which the value is being parsed.
        let mut current_key: Option<&str> = None;

        // The current state of parsed object.
        let mut value = HashMap::<String, Value>::new();

        while let Some(token) = iterator.next() {
            match token {
                // If it is a nested object, recursively parse it and store
                // in the hashmap with current key.
                Token::CurlyOpen => {
                    if let Some(key) = current_key {
                        value.insert(
                            key.to_string(),
                            Value::Object(Self::process_object(iterator)),
                        );
                        current_key = None;
                    }
                }
                // If this token is encountered, break the loop since it
                // indicates end of an object being parsed.
                Token::CurlyClose => {
                    break;
                }
                Token::Quotes | Token::ArrayClose => {}
                // If the token is a colon, it is the separator between key
                // and value pair. So the item being parsed from this point
                // ahead will not be a key.
                Token::Colon => {
                    is_key = false;
                }
                Token::String(string) => {
                    if is_key {
                        // If the process is presently parsing key, set the value
                        // as current key.
                        current_key = Some(string);
                    } else if let Some(key) = current_key {
                        // If the process already has a key set for present item,
                        // parse string as value instead, and set the current_key to none
                        // once done to prepare for the next key-value pair.
                        value.insert(key.to_string(), Value::String(string.clone()));
                        // Set current_key to None to prepare for the next key-value pair.
                        current_key = None;
                    }
                }
                Token::Number(number) => {
                    if let Some(key) = current_key {
                        value.insert(key.to_string(), Value::Number(*number));
                        // Set current_key to None to prepare for the next key-value pair.
                        current_key = None;
                    }
                }
                Token::ArrayOpen => {
                    if let Some(key) = current_key {
                        value.insert(key.to_string(), Value::Array(Self::process_array(iterator)));
                        // Set current_key to None to prepare for the next key-value pair.
                        current_key = None;
                    }
                }
                // If the token is a comma, it is the separator between multiple key-value pairs
                // in JSON. So the item being parsed from this point ahead will be a key.
                Token::Comma => is_key = true,
                Token::Boolean(boolean) => {
                    if let Some(key) = current_key {
                        value.insert(key.to_string(), Value::Boolean(*boolean));
                        // Set current_key to None to prepare for the next key-value pair.
                        current_key = None;
                    }
                }
                Token::Null => {
                    if let Some(key) = current_key {
                        value.insert(key.to_string(), Value::Null);
                        // Set current_key to None to prepare for the next key-value pair.
                        current_key = None;
                    }
                }
            }
        }

        value
    }
}
```

Et voilà. Vous devriez maintenant avoir tout le nécessaire pour commencer à utiliser ceci afin de parser un fichier JSON valide en Rust.

## Comment utiliser le parseur JSON

Créons un nouvel exemple dans le projet pour exécuter notre parseur JSON :

```
mkdir examples; touch examples/json.rs
```

Vous devez également l'enregistrer comme exemple dans le fichier `Cargo.toml` :

```
[package]
name = "json-parser"
version = "0.1.0"
edition = "2021"

[dependencies]

[[example]]
path = "examples/json.rs"
name = "json"
```

Maintenant, écrivons le code à exécuter pour cet exemple. Nous commençons par copier un exemple de fichier JSON à la racine du projet, que vous pouvez trouver [ici][31].

```rust
// examples/json.rs

use std::fs::File;
use json_parser::parser::JsonParser;

fn main() {
    let file = File::open("test.json").unwrap();
    let parser = JsonParser::parse(file).unwrap();

    dbg!(parser);
}
```

En exécutant ce code avec la commande suivante, vous devriez voir la même sortie que ci-dessous :

```
cargo run --example json --release
```

```
[examples/json.rs:8:5] parser = Object(
    {
        "pairs": Array(
            [
                Object(
                    {
                        "x1": Number(
                            F64(
                                41.844453001935875,
                            ),
                        ),
                        "y0": Number(
                            F64(
                                -33.78221816487377,
                            ),
                        ),
                        "y1": Number(
                            F64(
                                -78.10213222087448,
                            ),
                        ),
                        "x0": Number(
                            F64(
                                95.26235434764715,
                            ),
                        ),
                    },
                ),
                Object(
                    {
                        "x0": Number(
                            F64(
                                115.42029308864215,
                            ),
                        ),
                        "y0": Number(
                            F64(
                                1.2002187300000001e-5,
                            ),
                        ),
                        "x1": Number(
                            F64(
                                83.39640643072113,
                            ),
                        ),
                        "y1": Number(
                            F64(
                                28.643090267505812,
                            ),
                        ),
                    },
                ),
                Object(
                    {
                        "isWorking": Boolean(
                            true,
                        ),
                        "sample": String(
                            "string sample",
                        ),
                        "nullable": Null,
                        "isNotWorking": Boolean(
                            false,
                        ),
                    },
                ),
            ],
        ),
        "utf8": Object(
            {
                "key2": String(
                    "value2",
                ),
                "key1": String(
                    "ࠄࠀࠆࠄࠀࠁࠃ",
                ),
            },
        ),
    },
)
```

Félicitations ! Vous avez maintenant écrit votre propre parseur JSON, tout en apprenant certains des cas d'utilisation avancés du match et des itérateurs en Rust.

## **Conclusion**

J'espère que vous voyez déjà des manières intéressantes d'utiliser ce que vous avez appris aujourd'hui pour optimiser le code Rust existant dans vos projets, et tout futur code que vous écrirez impliquant ces notions.

Vous pouvez trouver le code complet pour tout ce que nous avons examiné dans cet article dans [ce dépôt][32].

Aussi, n'hésitez pas à **[me contacter][33]** si vous avez des questions ou des avis sur ce sujet.

### Vous appréciez mon travail ?

Pensez à m'offrir un café pour soutenir mon travail !

[☕Offrez-moi un café][34].

À la prochaine, bon code et je vous souhaite des cieux dégagés !

[1]: #heading-que-sont-les-iterateurs-en-rust
[2]: #heading-comment-implementer-des-iterateurs-en-rust
[3]: #heading-que-sont-les-iterateurs-peekable-en-rust
[4]: #heading-qu-est-ce-que-l-instruction-match-en-rust
[5]: #heading-comment-utiliser-les-iterateurs-dans-les-instructions-match-en-rust
[6]: #heading-que-sont-les-gardes-de-match-en-rust
[7]: #heading-qu-est-ce-que-le-binding-en-rust
[8]: #heading-comment-construire-un-parseur-json-etape-1-le-reader
[9]: #heading-qu-est-ce-que-l-encodage-d-octets-utf-8
[10]: #heading-comment-lire-les-donnees
[11]: #heading-comment-implementer-l-iterateur-pour-jsonreader
[12]: #heading-comment-construire-un-parseur-json-etape-2-preparer-les-types-de-donnees-intermediaires
[13]: #heading-le-type-value
[14]: #heading-comment-ajouter-des-methodes-de-conversion-utiles
[15]: #heading-comment-construire-un-parseur-json-etape-3-tokenisation
[16]: #heading-comment-definir-les-tokens-valides-attendus
[17]: #heading-comment-implementer-la-struct-tokenizer
[18]: #heading-comment-tokeniser-un-iterateur-de-caracteres
[19]: #heading-comment-parser-les-tokens-de-chaine
[20]: #heading-comment-parser-les-tokens-de-nombre
[21]: #heading-comment-parser-les-tokens-booleens
[22]: #heading-comment-parser-le-litteral-null
[23]: #heading-comment-parser-les-delimiteurs
[24]: #heading-comment-parser-un-caractere-de-terminaison
[25]: #heading-comment-construire-un-parseur-json-etape-4-des-tokens-a-la-valeur
[26]: #heading-comment-parser-les-primitifs
[27]: #heading-comment-parser-les-tableaux
[28]: #heading-comment-parser-les-objets
[29]: #heading-comment-utiliser-le-parseur-json
[30]: #heading-conclusion
[31]: https://raw.githubusercontent.com/anshulsanghi-blog/json-parser/master/test.json
[32]: https://github.com/anshulsanghi-blog/json-parser
[33]: mailto:contact@anshulsanghi.tech
[34]: https://buymeacoffee.com/anshulsanghi