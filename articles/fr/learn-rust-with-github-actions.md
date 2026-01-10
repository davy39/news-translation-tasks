---
title: Comment apprendre Rust sans installer de logiciel
subtitle: ''
author: Michael Yuan
co_authors: []
series: null
date: '2020-03-24T23:03:07.000Z'
originalURL: https://freecodecamp.org/news/learn-rust-with-github-actions
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.09.11-AM-1.png
tags:
- name: GitHub Actions
  slug: github-actions
- name: General Programming
  slug: programming
- name: Rust
  slug: rust
seo_title: Comment apprendre Rust sans installer de logiciel
seo_desc: 'In this article, we''ll learn how to use GitHub Actions to learn Rust from
  your web browser. We''ll code, build, test, run, and release all from a web page.
  No software needed! Learn with GitHub or follow us on Twitter.

  Rust is one of the hottest progr...'
---

Dans cet article, nous allons apprendre à utiliser GitHub Actions pour apprendre Rust depuis votre navigateur web. Nous allons coder, construire, tester, exécuter et publier tout cela depuis une page web. Aucun logiciel nécessaire ! [Apprendre avec GitHub](https://github.com/second-state/learn-rust-with-github-actions) ou [suivez-nous sur Twitter](https://twitter.com/secondstateinc).

Rust est l'un des langages de programmation les plus populaires aujourd'hui. Les [alpha geeks](https://martinfowler.com/bliki/AlphaGeek.html) l'adorent. C'est le langage de programmation le plus apprécié de Stackoverflow depuis 4 années consécutives.

L'une des fonctionnalités les plus uniques et appréciées de Rust est son compilateur agressif qui vous aide à garantir la correction et la sécurité avant même que le programme ne s'exécute. En conséquence, les développeurs Rust peuvent écrire des programmes très performants et sûrs. Rust élimine toute une classe de bugs de programmation, en particulier ceux difficiles à déboguer.

Si vous ne l'avez pas encore essayé, essayez-le ! *C'est magique.* Je crois que Rust pourrait être le prochain Java ou Ruby -- le langage de programmation que tout le monde devra apprendre à l'avenir.

Cependant, [apprendre Rust](https://www.secondstate.io/articles/a-rusty-hello-world/) nécessite généralement d'installer un ensemble d'outils en ligne de commande sur votre ordinateur. Le compilateur Rust est lent car tout le paradigme Rust est conçu pour analyser profondément le code source et trouver des bugs au moment de la compilation, plutôt que de planter à l'exécution.

Les IDE Rust en ligne, comme le [Rust Playground](https://play.rust-lang.org/) et [REPL.it](https://repl.it/languages/rust), sont des outils simples qui ne tirent pas pleinement parti de l'écosystème Rust des cibles de compilateur tierces et des bibliothèques.

Vous pourriez donc vous demander - puis-je essayer et apprendre Rust sans avoir à installer tous ces packages logiciels sur mon ordinateur ?

Eh bien, avec GitHub Actions, vous pouvez ! Vous pouvez apprendre et expérimenter avec le code Rust directement dans votre navigateur web. Commençons !

> GitHub Actions facilite l'automatisation de tous vos flux de travail logiciels, maintenant avec une CI/CD de classe mondiale. Construisez, testez et déployez votre code directement depuis GitHub. Faites en sorte que les revues de code, la gestion des branches et le tri des problèmes fonctionnent comme vous le souhaitez. Le code source et les actions de flux de travail pour l'exemple Hello World peuvent être trouvés dans [ce dépôt GitHub](https://github.com/second-state/learn-rust-with-github-actions).

## Hello world

Tout d'abord, créez un nouveau dépôt GitHub et ajoutez un fichier source Rust. Ajoutons un fichier `src/main.rs` avec le contenu suivant.

```rust
fn main() {
    println!("Hello, world!");
}
```

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.22.33-AM.png align="left")

Ensuite, retournez dans le répertoire racine `/` du dépôt GitHub et ajoutez un fichier `Cargo.toml`. Ce fichier décrit comment le système cargo de Rust doit construire et empaqueter notre projet.

```toml
[package]
name = "hello"
version = "0.1.0"
authors = ["ubuntu"]
edition = "2018"

[dependencies]
```

Nous avons maintenant un projet Rust complet. Construisons-le et exécutons-le maintenant.

## Actions GitHub

Dans l'onglet Actions de GitHub, nous pouvons ajouter des flux de travail associés à ce projet. Ce sont des actions que GitHub effectue automatiquement lorsque certains événements se produisent, comme une poussée de code ou un commit. Dans notre cas, nous aimerions que GitHub construise et exécute automatiquement notre `main.rs`, et nous montre les résultats.

Les actions de flux de travail et leurs déclencheurs d'événements sont définis dans des fichiers `yml` sous le répertoire `.github/workflows`. Vous pouvez écrire vos propres fichiers `yml`, ou choisir parmi l'un des modèles prêts à l'emploi.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.23.39-AM.png align="left")

*Le modèle de flux de travail Rust dans GitHub Actions*

Ici, nous choisissons le modèle Rust. GitHub vous permet de modifier le fichier `rust.yml` avant de l'enregistrer dans le dépôt.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.24.16-AM.png align="left")

*Le modèle d'actions Rust par défaut. Vous pouvez le modifier à votre guise.*

Prenons un moment ici pour expliquer comment fonctionnent les GitHub Actions. Le fichier `rust.yml` par défaut dit que

* Chaque fois qu'un utilisateur pousse du code ou accepte des pull requests dans ce dépôt, les actions de ce flux de travail `rust.yml` seront déclenchées.

* Le flux de travail créera une machine virtuelle exécutant le dernier système d'exploitation Ubuntu. Sur ce système Ubuntu, il effectuera ensuite les étapes suivantes.

* Il extraira le code de la branche `master`.

* Il exécutera la commande `cargo build --verbose` pour compiler et construire le code Rust.

* Il exécutera la commande `cargo test --verbose` pour exécuter les cas de test.

* Toutes les sorties standard et de console sur le système Ubuntu des deux commandes ci-dessus seront capturées par GitHub Actions et affichées sur le web.

Vous pouvez modifier la dernière ligne de `rust.yml` pour effectuer `cargo run`, qui exécute le programme binaire compilé. Notre fichier `rust.yml` mis à jour est le suivant.

```yml
name: Rust

on:
  push:
    branches: [ master ]
  pull_request:
    branches: [ master ]

jobs:
  build:

    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v2
    - name: Build
      run: cargo build --verbose
    - name: Run
      run: cargo run
```

Maintenant, chaque fois que vous poussez du code vers ce dépôt, les actions de `rust.yml` sont exécutées. Vous pouvez voir les résultats sous l'onglet Actions.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.26.32-AM.png align="left")

*Chaque poussée vers le dépôt GitHub déclenchera les actions à exécuter*

Vous pouvez cliquer sur un résultat, et cliquer sur l'onglet de construction à gauche pour voir les détails. Les sections de construction et d'exécution fournissent les détails les plus pertinents. La section Exécution montre l'impression réussie de hello world !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.27.02-AM.png align="left")

*L'action Exécuter montre Hello World ! imprimé sur la console !*

Ensuite, vous pouvez ajouter des dépendances tierces dans `Cargo.toml`, et construire des applications Rust complexes dans main.rs. Chaque fois que quelqu'un pousse du code, nous pourrons voir les résultats.

## Développement piloté par les tests (TDD)

Bien sûr, très peu de développeurs exécutent réellement leurs programmes pour imprimer du texte sur la console. Le `cargo run` ci-dessus n'est qu'un spectacle. En réalité, la plupart des développeurs écrivent des fonctions et des cas de test pour ces fonctions. La tâche la plus fréquente après la compilation et la construction est d'exécuter des cas de test. Voyons comment cela se fait.

Créez un nouveau dépôt GitHub, puis ajoutez un fichier `src/lib.rs` ci-dessous. Comme vous pouvez le voir, il définit une fonction Rust et quelques cas de test. Il peut être construit et publié en tant que package de bibliothèque Rust.

```rust
pub fn say(s: &str) -> String {
  let r = String::from("hello ");
  return r + s;
}

#[cfg(test)]
mod tests {
  use super::*;
  
  #[test]
  fn say_hello() {
    let result = say("ssvm");
    assert!(result.contains("hello ssvm"));
  }
}
```

Ensuite, retournez dans le répertoire racine `/` du dépôt GitHub, et ajoutez le fichier `Cargo.toml` suivant.

```toml
[package]
name = "hello"
version = "0.1.0"
authors = ["ubuntu"]
edition = "2018"

[lib]
name = "hello_lib"
path = "src/lib.rs"
crate-type =["cdylib"]

[dependencies]
```

Cliquez sur l'onglet Actions et ajoutez le flux de travail Rust par défaut. Comme vous vous en souvenez, le flux de travail Rust par défaut se termine par `cargo test`, ce qui est exactement ce dont nous avons besoin ici.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.24.16-AM-1.png align="left")

*Les actions de flux de travail Rust par défaut sont ce dont nous avons besoin ici.*

Le flux de travail s'exécute chaque fois que du nouveau code est poussé dans ce dépôt. Vous pouvez cliquer pour ouvrir une construction réussie et voir la sortie des actions de construction et de test.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/Screen-Shot-2020-03-20-at-2.09.11-AM.png align="left")

*Les actions GitHub construisent et testent votre programme Rust*

## Et ensuite

Maintenant, vous pouvez expérimenter avec votre code Rust, et avoir GitHub le construire, le tester et l'exécuter pour vous avec des sorties de console complètes, gratuitement et sans jamais quitter votre navigateur !

## Ressources

* [Apprendre à programmer en Rust](https://www.rust-lang.org/learn)

* [En savoir plus sur les GitHub Actions](https://github.com/features/actions)

* Bien sûr, la meilleure façon d'exécuter des programmes Rust sur le serveur est [à l'intérieur d'une machine virtuelle WebAssembly](https://www.secondstate.io/articles/rust-and-webassembly/). Consultez la machine virtuelle open source [Second State VM](https://www.secondstate.io/) pour cela !

* Découvrez l'IDE en ligne [BUIDL](https://www.secondstate.io/buidl/) pour [coder et déployer](http://buidl.secondstate.io/) des applications web décentralisées sur des blockchains publiques

## À propos de l'auteur

Le Dr. Michael Yuan est l'[auteur de 5 livres](http://www.michaelyuan.com/) sur l'ingénierie logicielle. Son dernier livre [Building Blockchain Apps](https://www.buildingblockchainapps.com/) a été publié par Addison-Wesley en décembre 2019. Le Dr. Yuan est le co-fondateur de [Second State](https://www.secondstate.io/), une startup financée par des capitaux-risqueurs qui apporte les technologies WebAssembly et Rust aux applications [cloud](https://www.secondstate.io/articles/why-webassembly-server/), [blockchain](https://docs.secondstate.io/) et [IA](https://github.com/second-state/rust-wasm-ai-demo/blob/master/README.md). Elle permet aux développeurs de déployer des fonctions Rust rapides, sûres, portables et sans serveur [sur Node.js](https://www.secondstate.io/articles/getting-started-with-rust-function/).

<iframe src="https://webassemblytoday.substack.com/embed" width="480" height="320" style="border:1px solid #EEE;background:white"></iframe>

Avant Second State, le Dr. Yuan était un contributeur de longue date à l'open source chez Red Hat, JBoss et Mozilla. En dehors du logiciel, le Dr. Yuan est un chercheur principal aux National Institutes of Health, avec plusieurs prix de recherche sur le cancer et la santé publique. Il est titulaire d'un doctorat en astrophysique de l'Université du Texas à Austin.