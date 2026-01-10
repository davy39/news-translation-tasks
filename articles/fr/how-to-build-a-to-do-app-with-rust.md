---
title: Tutoriel du langage de programmation Rust – Comment construire une application
  de liste de tâches
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-01-04T19:16:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-to-do-app-with-rust
coverImage: https://www.freecodecamp.org/news/content/images/2021/01/rust-mascot.png
tags:
- name: app development
  slug: app-development
- name: Rust
  slug: rust
seo_title: Tutoriel du langage de programmation Rust – Comment construire une application
  de liste de tâches
seo_desc: 'By Claudio Restifo

  Since its first open-source release in 2015, the Rust programming language has gained
  a lot of attention from the community. It''s also been voted the most loved programming
  language on StackOverflow''s developer survey each year sin...'
---

Par Claudio Restifo

Depuis sa première sortie open-source en 2015, le langage de programmation Rust a attiré beaucoup d'attention de la communauté. Il a également été élu le langage de programmation le plus apprécié sur le sondage des développeurs de [StackOverflow](https://insights.stackoverflow.com/survey/2020#technology-most-loved-dreaded-and-wanted-languages) chaque année depuis 2016.

Rust a été conçu par Mozilla et est considéré comme un langage de programmation système (comme C ou C++). Il n'a pas de garbage collector, ce qui le rend très performant. Mais sa conception le fait souvent paraître et se comporter de manière très "haut niveau".

La courbe d'apprentissage de Rust est considérée comme quelque peu raide. Je ne suis pas un expert du langage moi-même, mais avec ce tutoriel, je vais essayer de vous donner une approche pratique de certains concepts pour vous aider à approfondir.

## Ce que nous allons construire dans ce tutoriel pratique

J'ai décidé de suivre la longue tradition des applications JavaScript et de créer une application de liste de tâches comme premier projet. Nous travaillerons avec la ligne de commande, donc une certaine familiarité avec celle-ci est nécessaire. Vous aurez également besoin de quelques connaissances en concepts de programmation générale.

Cette application s'exécutera dans le terminal. Nous stockerons les valeurs sous forme de collection d'éléments et d'une valeur booléenne représentant son état actif.

## Ce que nous allons couvrir ici

- La gestion des erreurs en Rust.
- Les options et les types Null.
- Les structs et impl.
- L'I/O du terminal.
- La gestion du système de fichiers.
- La possession et l'emprunt en Rust.
- Les motifs de correspondance.
- Les itérateurs et les fermetures.
- L'utilisation de crates externes.

## Avant de commencer

Quelques conseils avant de commencer, de la part de quelqu'un venant d'un background JavaScript :

- Rust est un langage fortement typé. Cela signifie que nous devrons prendre soin des types de variables lorsque le compilateur n'est pas en mesure de les inférer pour nous.
- Contrairement à JavaScript, il n'y a pas d'[AFI](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Lexical_grammar#Automatic_semicolon_insertion). Cela signifie que nous devons taper les points-virgules (";") nous-mêmes, sauf s'il s'agit de la dernière instruction d'une fonction. Dans ce cas, vous pouvez omettre `;` pour le retourner.

Sans plus tarder, commençons.

## Comment commencer avec Rust

Pour commencer, téléchargez Rust sur votre ordinateur. Pour ce faire, suivez les instructions que vous trouverez sur la page [getting started](https://www.rust-lang.org/learn/get-started) du site officiel de Rust.

Là, vous trouverez également des instructions pour intégrer le langage avec votre éditeur préféré pour une meilleure expérience.

Avec le compilateur Rust lui-même, Rust est livré avec un outil appelé [Cargo](https://doc.rust-lang.org/cargo/index.html). Cargo est le gestionnaire de paquets Rust, et pour les développeurs JavaScript, il ressemblera à npm ou yarn.

Pour démarrer un nouveau projet, naviguez jusqu'à l'endroit où vous souhaitez créer votre projet, puis exécutez simplement `cargo new <nom-du-projet>`. Dans mon cas, j'ai décidé de nommer mon projet "todo-cli" donc je peux exécuter :

```console
$ cargo new todo-cli
```

Maintenant, naviguez jusqu'au répertoire nouvellement créé et listez son contenu. Vous devriez voir deux fichiers :

```console
$ tree .
.
├── Cargo.toml
└── src
    └── main.rs
```

Nous travaillerons sur le fichier `src/main.rs` pour le reste de ce tutoriel, alors ouvrez-le.

Comme beaucoup d'autres langages, Rust a une fonction main qui sera exécutée en premier. `fn` est la façon de déclarer des fonctions tandis que le `!` dans `println!` est une [macro](https://doc.rust-lang.org/book/ch19-06-macros.html). Comme vous pouvez le deviner, ce programme est la version Rust de "_hello world!_".

Pour le construire et l'exécuter, exécutez simplement `cargo run`.

```console
$ cargo run
Hello world!
```

## Comment lire les arguments

Notre objectif est d'avoir notre CLI accepter deux arguments : le premier sera l'action, et le second sera l'élément.

Nous allons commencer par lire les arguments que l'utilisateur saisit et les imprimer.

**Remplacez** le contenu de main par ce qui suit :

```rust
let action = std::env::args().nth(1).expect("Veuillez spécifier une action");
let item = std::env::args().nth(2).expect("Veuillez spécifier un élément");

println!("{:?}, {:?}", action, item);
```

Commençons par digérer toutes ces informations.

- `let` [[doc]](https://doc.rust-lang.org/std/keyword.let.html) lie une valeur à une variable.
- `std::env::args()` [[doc]](https://doc.rust-lang.org/std/env/fn.args.html) est une fonction importée du module _env_ de la bibliothèque standard qui retourne les arguments avec lesquels le programme a été démarré. Puisqu'il s'agit d'un itérateur, nous pouvons accéder à la valeur stockée à chaque position avec la fonction `nth()`. L'argument à la position 0 est le programme lui-même, c'est pourquoi nous commençons à lire à partir du 1er élément.
- `expect()` [[doc]](https://doc.rust-lang.org/std/option/enum.Option.html#method.expect) est une méthode définie pour l'énumération `Option` qui retournera soit la valeur, soit, si elle n'est pas présente, mettra fin au programme immédiatement (Panic en termes Rust), en retournant le message fourni.

Parce que le programme peut être exécuté sans arguments, Rust nous oblige à vérifier si une valeur est réellement fournie en nous donnant un type Option : soit la valeur est là, soit elle ne l'est pas.

En tant que programmeurs, nous avons la responsabilité de nous assurer que nous prenons l'action appropriée dans chaque cas.

Pour l'instant, si l'argument n'est pas fourni, nous quitterons le programme immédiatement.

Exécutons le programme et passons deux arguments. Pour ce faire, ajoutez-les après `--`. Par exemple :

```console
$ cargo run -- hello world!
    Finished dev [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/todo_cli hello 'world'\!''`
"hello", "world!"
```

## Comment insérer et sauvegarder des données avec un type personnalisé

Réfléchissons un instant à notre objectif pour le programme. Nous voulons lire l'argument donné par l'utilisateur, mettre à jour notre liste de tâches et le stocker quelque part pour une utilisation ultérieure.

Pour ce faire, nous allons implémenter notre propre type où nous pouvons définir nos méthodes pour répondre aux besoins métiers.

Nous allons utiliser les [struct](https://doc.rust-lang.org/std/keyword.struct.html) de Rust, qui nous permettent de faire les deux de manière propre. Cela évite d'avoir à écrire tout le code à l'intérieur de la fonction main.

### Comment définir notre struct

Puisque nous allons taper HashMap beaucoup dans les étapes suivantes, nous pouvons l'importer dans la portée et nous épargner quelques frappes.

En haut de notre fichier, ajoutez cette ligne :

```rust
use std::collections::HashMap
```

Cela nous permettra d'utiliser `HashMap` directement sans avoir à taper le chemin complet à chaque fois.

En dessous de la fonction main, ajoutons le code suivant :

```rust
struct Todo {
    // utilise la HashMap intégrée de Rust pour stocker des paires clé-valeur
    map: HashMap<String, bool>,
}
```

Cela définira notre type Todo personnalisé : une struct avec un seul champ appelé "map".

Ce champ est une [HashMap](https://doc.rust-lang.org/std/collections/struct.HashMap.html). Vous pouvez la considérer comme un *type* d'objet JavaScript, où Rust nous oblige à déclarer les types de la clé et de la valeur.

- `HashMap<String, bool>` signifie que nous avons des clés composées de Strings, et une valeur booléenne : l'état actif.

### Comment ajouter des méthodes à notre struct

Les méthodes sont comme des fonctions régulières – elles sont déclarées avec le mot-clé `fn`, elles acceptent des paramètres et elles ont une valeur de retour. 

Cependant, elles diffèrent des fonctions régulières en ce sens qu'elles sont définies dans le contexte d'une struct et leur premier paramètre est *toujours* `self`.

Nous allons définir un bloc _impl_ (implémentation) en dessous de la struct nouvellement ajoutée.

```rust
impl Todo {
    fn insert(&mut self, key: String) {
        // insère un nouvel élément dans notre map.
        // nous passons true comme valeur
        self.map.insert(key, true);
    }
}
```

Cette fonction est assez simple : elle prend une *référence* à la struct et une clé, et les insère dans notre map en utilisant la méthode intégrée [insert](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.insert) de HashMap.

Deux informations très importantes :

- **mut** [[doc]](https://doc.rust-lang.org/std/keyword.mut.html) rend une variable mutable.
En Rust, chaque variable est _immutable_ par défaut. Si vous voulez mettre à jour une valeur, vous devez opter pour la mutabilité en utilisant le mot-clé `mut`. Puisque avec notre fonction nous modifions effectivement notre map en ajoutant une nouvelle valeur, nous devons la déclarer comme mutable.

- **&** [[doc]](https://doc.rust-lang.org/std/primitive.reference.html) indique une _référence_.
Vous pouvez imaginer la variable comme un pointeur vers l'emplacement mémoire où la valeur est stockée, plutôt que d'être la "valeur" elle-même.<br/>
En termes Rust, cela est appelé un **borrow**, ce qui signifie que la fonction ne possède pas réellement cette valeur, mais pointe simplement vers l'emplacement où elle est stockée.

## Un bref aperçu du système de possession de Rust

Avec l'indice précédent sur le borrow et la référence, c'est maintenant un bon moment pour parler brièvement de la possession.

La possession est la caractéristique la plus unique de Rust. Elle permet aux programmeurs Rust d'écrire des programmes sans avoir besoin d'allouer manuellement de la mémoire (comme en C/C++) tout en étant capable de s'exécuter sans un Garbage Collector (comme en JavaScript ou Python) qui regarde constamment la mémoire du programme pour libérer les ressources non utilisées.

Le système de possession a trois règles :
* Chaque valeur en Rust a une variable : son propriétaire.
* Il ne peut y avoir qu'un seul propriétaire à la fois pour chaque valeur.
* Lorsque le propriétaire sort de la portée, la valeur sera abandonnée.

Rust vérifie ces règles au moment de la compilation, ce qui signifie que vous devez être explicite si et quand vous voulez qu'une valeur soit libérée en mémoire.
Pensez à cet exemple :

```rust
fn main() {
 // le propriétaire de la String est x
 let x = String::from("Hello");

 // nous déplaçons la valeur à l'intérieur de cette fonction.
 // maintenant doSomething est le propriétaire de x.
 // Rust libérera la mémoire associée à x 
 // dès qu'elle sortira de la portée "doSomething".
 doSomething(x);

 // Le compilateur lancera une erreur puisque nous avons essayé d'utiliser la valeur x
 // mais puisque nous l'avons déplacée à l'intérieur de "doSomething"
 // nous ne pouvons pas l'utiliser car nous n'en avons pas la possession
 // et la valeur peut avoir été abandonnée.
 println!("{}", x);
}
```

Ce concept est largement considéré comme le plus difficile à saisir lors de l'apprentissage de Rust, car c'est un concept qui peut être nouveau pour de nombreux programmeurs. 

Vous pouvez lire une explication plus approfondie sur la [Possession](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html) dans la documentation officielle de Rust.

Nous n'allons pas creuser trop profondément dans les tenants et aboutissants du système de possession. Pour l'instant, gardez simplement à l'esprit les règles que j'ai mentionnées ci-dessus. Essayez de réfléchir, à chaque étape, si nous devons "posséder" les valeurs et ensuite les abandonner, ou si nous avons besoin d'une référence pour qu'elles puissent être conservées.

Par exemple, dans la méthode d'insertion ci-dessus, nous ne voulons pas posséder `map`, car nous en avons encore besoin pour stocker ses données quelque part. Ce n'est qu'alors que nous pouvons enfin libérer la mémoire allouée.

### Comment sauvegarder la map sur le disque

Puisque ceci est une application de démonstration, nous allons adopter la solution la plus simple possible pour le stockage à long terme : écrire la map dans un fichier sur le disque.

Créons une nouvelle méthode dans notre bloc `impl`.

```rust
impl Todo {
    // [reste du code]
    fn save(self) -> Result<(), std::io::Error> {
        let mut content = String::new();
        for (k, v) in self.map {
            let record = format!("{}\t{}\n", k, v);
            content.push_str(&record)
        }
        std::fs::write("db.txt", content)
    }
}
```

* `->` annote le type retourné par la fonction. Nous retournons un `Result`.
* Nous itérons sur la map, et formatons chaque chaîne, en séparant la clé et la valeur avec un caractère de tabulation et chaque ligne avec une nouvelle ligne.
* Nous poussons la chaîne formatée dans une variable de contenu.
* Nous écrivons `content` dans un fichier appelé `db.txt`.

Il est important de noter que `save` *prend possession* de self.
Ceci est une décision arbitraire afin que le compilateur nous arrête si nous essayions par accident de mettre à jour la map après avoir appelé save (car la mémoire de self serait libérée).

Ceci est une décision personnelle pour "forcer" save comme la dernière méthode à être utilisée. Et c'est un exemple parfait pour montrer comment vous pouvez utiliser la gestion de la mémoire de Rust pour créer un code plus strict qui ne compilera pas (ce qui aide à prévenir les erreurs humaines pendant le développement).

### Comment utiliser struct dans main

Maintenant que nous avons ces deux méthodes, nous pouvons les utiliser. Nous avons laissé main au point où nous lisions les arguments fournis. Maintenant, si l'action fournie est "add", nous allons insérer cet élément dans le fichier et le stocker pour une utilisation ultérieure.

Ajoutez ces lignes en dessous des deux liaisons d'arguments :

```rust
fn main() {
    // ...[code de liaison des arguments]

    let mut todo = Todo {
        map: HashMap::new(),
    };
    if action == "add" {
        todo.insert(item);
        match todo.save() {
            Ok(_) => println!("todo sauvegardé"),
            Err(why) => println!("Une erreur s'est produite : {}", why),
        }
    } 
}
```

Voyons ce que nous faisons ici :

* `let mut todo = Todo` nous permet d'instancier une struct, en la liant comme mutable.
* nous appelons la méthode `TODO insert` en utilisant la notation `.`.
* nous faisons correspondre ([match](https://doc.rust-lang.org/std/keyword.match.html)) le Result retourné par la fonction save et imprimons un message à l'écran pour les deux cas.

Testons-le. Naviguez jusqu'à votre terminal et tapez :

```console
$ cargo run -- add "code rust"
todo sauvegardé
```

Inspectons l'élément sauvegardé :

```console
$ cat db.txt
code rust true
```

Vous pouvez trouver un extrait complet du code jusqu'à présent dans ce [gist](https://gist.github.com/Marmiz/b67e98c2fc7be3561d124294cf3cb6ac).

## Comment lire depuis un fichier

Actuellement, notre programme a un défaut fondamental : chaque fois que nous "ajoutons", nous écrasons la map au lieu de la mettre à jour. Cela est dû au fait que nous créons une nouvelle map vide chaque fois que nous exécutons le programme. Corrigons cela.

### Ajouter une nouvelle fonction dans TODO

Nous allons implémenter une nouvelle fonction pour notre struct Todo. Une fois appelée, elle lira le contenu de notre fichier et nous rendra notre Todo peuplé avec la valeur précédemment stockée. Notez que ceci n'est pas une méthode car elle ne prend pas `self` comme premier argument.

Nous l'appellerons `new`, qui est simplement une convention Rust (voir HashMap::new() comme utilisé précédemment).

Ajoutons le code suivant à l'intérieur de notre bloc impl :

```rust
impl Todo {
    fn new() -> Result<Todo, std::io::Error> {
        let mut f = std::fs::OpenOptions::new()
            .write(true)
            .create(true)
            .read(true)
            .open("db.txt")?;
        let mut content = String::new();
        f.read_to_string(&mut content)?;
        let map: HashMap<String, bool> = content
            .lines()
            .map(|line| line.splitn(2, '\t').collect::<Vec<&str>>())
            .map(|v| (v[0], v[1]))
            .map(|(k, v)| (String::from(k), bool::from_str(v).unwrap()))
            .collect();
        Ok(Todo { map })
    }

// ...reste des méthodes
}
```

Ne vous inquiétez pas si cela semble un peu écrasant. Nous utilisons un style de programmation plus fonctionnel pour celui-ci, principalement pour montrer et introduire le fait que Rust supporte de nombreux paradigmes trouvés dans d'autres langages tels que les itérateurs, les fermetures et les fonctions lambda.

Voyons ce qui se passe ici :

* Nous définissons une fonction `new` qui retournera un Result qui est soit une struct `Todo`, soit un `io:Error`.
* Nous configurons comment ouvrir le fichier "db.txt" en définissant diverses [OpenOptions](https://doc.rust-lang.org/std/fs/struct.OpenOptions.html). Le plus notable est le drapeau `create(true)` qui créera le fichier s'il n'est pas déjà présent.
* `f.read_to_string(&mut content)?` lit tous les octets du fichier et les ajoute à la chaîne `content`.
*note :* n'oubliez pas d'ajouter `use std::io::Read;` en haut du fichier avec les autres instructions use afin d'utiliser la méthode `read_to_string`.
* Nous devons convertir du type String du fichier en HashMap. Nous le faisons en liant une variable map avec cette ligne : `let map: HashMap<String, bool>`.
C'est l'une des occasions où le compilateur a du mal à inférer le type pour nous, donc nous le déclarons nous-mêmes.
* lines [[doc]](https://doc.rust-lang.org/std/primitive.str.html#method.lines) crée un Iterator sur chaque ligne d'une chaîne, ce qui signifie que maintenant nous allons itérer sur chaque entrée de notre fichier, puisque nous l'avons formaté avec un `/n` à la fin de chaque entrée.
* map [[doc]](https://doc.rust-lang.org/std/iter/trait.Iterator.html#method.map) prend une fermeture et l'appelle sur chaque élément de l'itérateur.
* `line.splitn(2, '\t')` [[doc]](https://doc.rust-lang.org/std/primitive.str.html#method.splitn) divisera nos lignes sur le caractère de tabulation.
* `collect::<Vec<&str>>()`[[doc]](https://doc.rust-lang.org/core/iter/trait.Iterator.html#method.collect) comme décrit dans la documentation est l'une des méthodes les plus puissantes de la bibliothèque standard : elle transforme un itérateur en une collection pertinente.
Ici, nous disons à la fonction map de transformer notre chaîne Split en un Vecteur de tranches de chaînes empruntées en ajoutant `::Vec<&str>` à la méthode. Cela indique au compilateur quelle collection nous voulons à la fin de l'opération.
* Ensuite, nous le transformons en un tuple pour plus de commodité en utilisant `.map(|v| (v[0], v[1]))`.
* Ensuite, nous convertissons les deux éléments du tuple en une String et un booléen en utilisant `.map(|(k, v)| (String::from(k), bool::from_str(v).unwrap()))`.
*note :* n'oubliez pas d'ajouter `use std::str::FromStr;` en haut du fichier avec l'autre instruction use afin de pouvoir utiliser la méthode `from_str`.
* Nous les collectons enfin dans notre HashMap. Cette fois, nous n'avons pas besoin de déclarer le type car Rust l'infère à partir de la déclaration de liaison.
* Enfin, si nous n'avons jamais rencontré d'erreurs, nous retournons notre struct à l'appelant avec `Ok(Todo { map })`. 
Notez ici que, comme en JavaScript, nous pouvons utiliser une notation plus courte si la clé et la variable ont le même nom à l'intérieur d'une struct.

*ouf !*

![dancing ferris.](https://www.freecodecamp.org/news/content/images/2021/01/dancing-ferris.gif)
_Vous vous en sortez très bien ! Crédits image : https://rustacean.net/_

### Une approche alternative

Bien que map soit généralement considéré comme plus idiomatique, ce qui précède aurait également pu être implémenté avec une boucle `for`. N'hésitez pas à utiliser celle que vous préférez.

```rust
fn new() -> Result<Todo, std::io::Error> {
    // ouvrir le fichier db
    let mut f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .read(true)
        .open("db.txt")?;
    // lire son contenu dans une nouvelle chaîne   
    let mut content = String::new();
    f.read_to_string(&mut content)?;
    
    // allouer une HashMap vide
    let mut map = HashMap::new();
    
    // boucler sur chaque ligne du fichier
    for entries in content.lines() {
        // diviser et lier les valeurs
        let mut values = entries.split('\t');
        let key = values.next().expect("No Key");
        let val = values.next().expect("No Value");
        // les insérer dans HashMap
        map.insert(String::from(key), bool::from_str(val).unwrap());
    }
    // Retourner Ok
    Ok(Todo { map })
}
```

Le code ci-dessus est fonctionnellement équivalent à l'approche plus "fonctionnelle" utilisée précédemment.

### Comment utiliser la nouvelle fonction

Dans main, mettez simplement à jour la liaison de notre variable todo avec :

```rust
let mut todo = Todo::new().expect("L'initialisation de la base de données a échoué");
```

Maintenant, si nous retournons au terminal et exécutons une série de commandes "add", nous devrions voir notre base de données se mettre à jour correctement :

```console
$ cargo run -- add "faire du café"
todo sauvegardé
$ cargo run -- add "coder en rust"
todo sauvegardé
$ cat db.txt
faire du café     true
coder en rust       true
```

Vous pouvez trouver le code complet écrit jusqu'à présent ici dans ce [gist](https://gist.github.com/Marmiz/b659c7835054d25513106e3804c4539f).

## Comment mettre à jour une valeur dans la collection

Comme dans toutes les applications TODO, nous voulons pouvoir non seulement ajouter des éléments, mais aussi les basculer et les marquer comme terminés.

### Comment ajouter la méthode complete

Pour ce faire, ajoutons une nouvelle méthode à notre struct appelée "complete". Dans celle-ci, nous prenons une référence à une clé, et mettons à jour la valeur, ou retournons `None` si la clé n'est pas présente.

```rust
impl Todo {
// [Reste des méthodes TODO]

  fn complete(&mut self, key: &String) -> Option<()> {
      match self.map.get_mut(key) {
          Some(v) => Some(*v = false),
          None => None,
      }
  }
}
```

Voyons ce qui se passe ici :

* Nous déclarons le type de retour de notre fonction : un `Option` vide.
* La méthode entière retourne le résultat de l'expression Match qui sera soit un `Some()` vide soit `None`.
* `self.map.get_mut` [[doc]](https://doc.rust-lang.org/std/collections/struct.HashMap.html#method.get_mut) nous donnera une référence mutable à la valeur de la clé, ou `None` si la valeur n'est pas présente dans la collection.
* Nous utilisons l'opérateur `*` [[doc]](https://doc.rust-lang.org/book/appendix-02-operators.html) pour déréférencer la valeur et la définir à false.

### Comment utiliser la méthode complete

Nous pouvons utiliser la méthode "complete" de manière similaire à celle dont nous avons utilisé insert précédemment.

Dans `main`, vérifions que l'action passée en argument est "complete" en utilisant une instruction `else if` :

```rust
// dans la fonction main

if action == "add" {
    // extrait de code d'action d'ajout
} else if action == "complete" {
    match todo.complete(&item) {
        None => println!("'{}' n'est pas présent dans la liste", item),
        Some(_) => match todo.save() {
            Ok(_) => println!("todo sauvegardé"),
            Err(why) => println!("Une erreur s'est produite : {}", why),
        },
    }
}
```

Il est temps d'analyser ce que nous faisons ici :

* Nous faisons correspondre l'Option retourné par la méthode `todo.complete(&item)`.
* Si le cas est `None`, nous imprimons un avertissement à l'utilisateur pour une meilleure expérience.
Nous avons passé l'élément comme une référence avec `&item` à la méthode "todo.complete" afin que la valeur soit toujours possédée par cette fonction. Cela signifie que nous pouvons l'utiliser pour notre macro `println!` dans la ligne suivante.
Si nous ne faisions pas cela, la valeur aurait été possédée par "complete" et abandonnée là.
* Si nous détectons qu'une valeur `Some` a été retournée, nous appelons `todo.save` pour stocker le changement de manière permanente dans notre fichier.

Comme précédemment, vous pouvez trouver un instantané du code écrit jusqu'à présent dans ce [gist](https://gist.github.com/Marmiz/1480b31e8e0890e8745e7b6b44a803b8).

## Essayez d'exécuter le programme

Il est temps d'essayer l'application que nous avons développée localement dans notre terminal. Commençons par supprimer notre fichier db pour repartir de zéro.

```console
$ rm db.txt
```

Ensuite, ajoutez et modifiez certaines des tâches :
```console
$ cargo run -- add "faire du café"
$ cargo run -- add "coder en rust"
$ cargo run -- complete "faire du café"
$ cat db.txt
faire du café     false
coder en rust       true
```
Cela signifie qu'à la fin de ces commandes, nous avons une action terminée ("faire du café") et une en attente : "coder en rust".

Disons que nous voulons faire du café à nouveau :

```console
$ cargo run -- add "faire du café"
$ cat db.txt
faire du café     true
coder en rust       true
```

## Bonus : Comment le stocker en JSON avec Serde

Le programme, même s'il est minimal, fonctionne. Mais donnons-lui un petit coup de pouce. Venant du monde JavaScript, j'ai décidé qu'au lieu d'un fichier texte brut, je veux stocker mes valeurs dans un fichier JSON.

Nous allons profiter de cette occasion pour voir comment installer et utiliser un package de la communauté open source Rust appelé [crates.io](https://crates.io/).

### Comment installer serde

Pour installer un nouveau package dans notre projet, ouvrez le fichier `cargo.toml`. En bas, vous devriez voir un champ `[dependencies]` : ajoutez simplement ce qui suit au fichier :

```toml
[dependencies]
serde_json = "1.0.60"
```

Et c'est tout. La prochaine fois, cargo compilera notre programme et téléchargera et inclura également le nouveau package avec notre code.

### Comment mettre à jour Todo::New

Le premier endroit où nous voulons utiliser Serde est lorsque nous lisons le fichier db. Maintenant, au lieu de lire un ".txt", nous voulons lire un fichier JSON.

À l'intérieur du bloc `impl`, mettons à jour la fonction `new` :

```rust
// à l'intérieur du bloc impl Todo

fn new() -> Result<Todo, std::io::Error> {
    // ouvrir db.json
    let f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .read(true)
        .open("db.json")?;
    // sérialiser json en tant que HashMap
    match serde_json::from_reader(f) {
        Ok(map) => Ok(Todo { map }),
        Err(e) if e.is_eof() => Ok(Todo {
            map: HashMap::new(),
        }),
        Err(e) => panic!("Une erreur s'est produite : {}", e),
    }
}
```

Les changements notables sont :

* Plus de liaison `mut f` pour l'option de fichier, car nous n'avons pas besoin d'allouer manuellement le contenu dans une String comme avant. Serde s'en chargera pour nous.
* Nous avons mis à jour notre extension de fichier en `db.json`.
* `serde_json::from_reader` [[doc]](https://docs.serde.rs/serde_json/fn.from_reader.html) désérialisera le fichier pour nous. Il interfère avec le type de retour de map et tentera de convertir notre JSON en un HashMap compatible. Si tout se passe bien, nous retournons notre struct `Todo` comme avant.
* `Err(e) if e.is_eof()` est une [garde de correspondance](https://doc.rust-lang.org/reference/expressions/match-expr.html#match-guards) qui nous permet d'affiner le comportement de l'instruction Match.
Si Serde retourne une erreur EOF prématurée (fin de fichier), cela signifie que le fichier est totalement vide (par exemple lors du tout premier lancement, ou si nous avons supprimé le fichier). Dans ce cas, nous récupérons de l'erreur et retournons un HashMap vide.
* Pour toutes les autres erreurs, quittez le programme immédiatement.

### Comment mettre à jour Todo.save

L'autre endroit où nous voulons utiliser Serde est lorsque nous sauvegardons notre map en JSON. Pour ce faire, mettez à jour la méthode `save` dans le bloc impl pour qu'elle soit :

```rust
// à l'intérieur du bloc impl Todo
fn save(self) -> Result<(), Box<dyn std::error::Error>> {
    // ouvrir db.json
    let f = std::fs::OpenOptions::new()
        .write(true)
        .create(true)
        .open("db.json")?;
    // écrire dans le fichier avec serde
    serde_json::to_writer_pretty(f, &self.map)?;
    Ok(())
}
```

Comme avant, voyons ce que nous changeons ici :

* `Box<dyn std::error::Error>`. Cette fois, nous retournons une [Box](https://doc.rust-lang.org/std/boxed/index.html) contenant une implémentation d'erreur générique Rust.
Pour faire simple, une box est un pointeur vers une allocation en mémoire.
Puisque nous pouvons retourner soit une erreur du système de fichiers lors de l'ouverture du fichier, soit une erreur Serde lors de sa conversion, nous ne savons pas vraiment laquelle des deux notre fonction peut retourner. 
Par conséquent, nous retournons un pointeur vers l'erreur possible, au lieu de l'erreur elle-même afin que l'appelant les gère.
* Nous avons bien sûr mis à jour le nom du fichier en `db.json` pour correspondre.
* Enfin, nous laissons Serde faire le travail difficile et écrire notre HashMap sous forme de fichier JSON (joliment imprimé).
* N'oubliez pas de supprimer à la fois `use std::io::Read;` et `use std::str::FromStr;` du haut du fichier car nous n'en avons plus besoin.

Et c'est tout.
Maintenant, vous pouvez exécuter votre programme et inspecter la sortie sauvegardée dans le fichier. Si tout s'est bien passé, vous devriez maintenant voir vos tâches sauvegardées en JSON.

Vous pouvez trouver le code complet écrit jusqu'à présent dans ce [gist](https://gist.github.com/Marmiz/541c3ccea832a27bfb60d4882450a4a8).

## Réflexions finales, conseils et ressources supplémentaires

Ce fut un assez long voyage, et je suis honoré que vous l'ayez fait avec moi.
J'espère que vous avez appris quelque chose et que votre curiosité a été éveillée par cette introduction. N'oubliez pas que nous avons travaillé avec un langage très "bas niveau", mais la révision du code a probablement semblé très familière à la plupart.

Et c'est ce qui m'attire personnellement vers Rust – le fait qu'il me permet d'écrire du code qui est à la fois extrêmement rapide et efficace en mémoire sans la peur qui accompagne une telle responsabilité : je sais que le compilateur sera là pour moi, arrêtant mon code avant qu'il ne soit même possible de l'exécuter.

Avant de terminer, je voudrais partager avec vous quelques conseils et ressources supplémentaires pour vous aider à avancer dans votre voyage Rust :

* [Rust fmt](https://github.com/rust-lang/rustfmt) est un outil très pratique que vous pouvez exécuter pour formater votre code selon un modèle cohérent. Plus besoin de perdre du temps à configurer vos plugins linter préférés.
* `cargo check` [[doc]](https://doc.rust-lang.org/cargo/commands/cargo-check.html) tentera de compiler votre code sans l'exécuter : c'est une commande très utile lors du développement, où vous voulez simplement vérifier l'exactitude du code sans l'exécuter.
* Rust est livré avec une suite de tests intégrée et un outil pour générer de la documentation : [cargo test](https://doc.rust-lang.org/cargo/commands/cargo-test.html) et [cargo doc](https://doc.rust-lang.org/cargo/commands/cargo-rustdoc.html). Nous n'en avons pas parlé cette fois, car le tutoriel semble déjà assez dense. Peut-être dans le futur.

Pour en savoir plus sur le langage, à mon avis, les meilleures ressources sont :

* Le site officiel [Rust](https://www.rust-lang.org/), où toutes les informations sont rassemblées.
* Si vous aimez interagir via le chat, le serveur [Discord](https://discord.gg/rust-lang) de Rust a une communauté très active et serviable.
* Si vous aimez apprendre en lisant des livres, le livre "[The Rust programming language](https://doc.rust-lang.org/book/title-page.html)" est le bon choix pour vous.
* Si vous êtes plus du type vidéo, la série de vidéos d'introduction à Rust de Ryan Levick [introduction à Rust](https://youtu.be/WnWGO-tLtLA) est une ressource incroyable.


Vous pouvez trouver le code source de cet article hébergé sur [GitHub](https://github.com/Marmiz/todo-cli).

L'image de couverture provient de [https://rustacean.net/](https://rustacean.net/).

Merci d'avoir lu et bon codage !