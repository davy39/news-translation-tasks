---
title: Comment construire un modèle d'apprentissage automatique en Rust
subtitle: ''
author: Oduah Chigozie
co_authors: []
series: null
date: '2022-10-12T22:31:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-machine-learning-model-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2022/10/guerrillabuzz-crypto-pr-IlUq1ruyv0Q-unsplash.jpg
tags:
- name: Machine Learning
  slug: machine-learning
- name: Rust
  slug: rust
seo_title: Comment construire un modèle d'apprentissage automatique en Rust
seo_desc: "Machine learning is a really interesting concept in computer programming.\
  \ It involves using data to train a computer program to carry out tasks. \nDuring\
  \ the process, the program learns from data by discovering patterns. This reduces\
  \ the need for prog..."
---

L'apprentissage automatique (Machine Learning) est un concept vraiment intéressant en programmation informatique. Il consiste à utiliser des données pour entraîner un programme informatique à effectuer des tâches.

Au cours de ce processus, le programme apprend à partir des données en découvrant des modèles. Cela réduit la nécessité pour les programmeurs de coder des règles en dur dans certaines applications.

Les langages comme Python et R sont excellents pour apprendre et réaliser des tâches d'apprentissage automatique. Mais ces langages ne sont pas une solution absolue. Ils ont des faiblesses. Certaines applications d'apprentissage automatique peuvent nécessiter d'effectuer des opérations avec une grande vitesse et une grande efficacité des ressources informatiques.

Rust est un langage de programmation puissant et efficace. Bien que Rust ne dispose pas encore d'un écosystème mature, la nature même du langage le rend parfait pour les applications qui exigent rapidité et efficacité.

Les programmeurs Rust trouveront ce tutoriel utile pour débuter en apprentissage automatique. De même, les ingénieurs en apprentissage automatique trouveront ce tutoriel utile pour commencer à utiliser Rust.

## Prérequis

Pour suivre ce tutoriel, vous aurez besoin des éléments suivants :

* Des connaissances en Rust
* Rust installé sur votre système

## Qu'est-ce que l'apprentissage automatique ?

En apprentissage automatique, un **modèle** est un objet logiciel capable de comprendre des motifs à partir de données. L'entraînement d'un modèle est le processus consistant à fournir des données au modèle pour qu'il en dégage des motifs. L'apprentissage automatique est le processus d'entraînement d'un modèle pour accomplir des tâches.

Une fois que vous avez entraîné votre modèle, vous pouvez l'utiliser pour tirer des conclusions à partir de nouvelles données. Vous pouvez baser ces conclusions soit sur des classifications, soit sur des prédictions. Un modèle prédictif utilise les données actuelles pour prédire un événement, un résultat ou une conséquence. Un modèle de classification utilise les données pour classer un objet ou un concept.

Le schéma suivant est un aperçu de base du processus d'apprentissage automatique :

![Image](https://lh5.googleusercontent.com/0KA34Lh8SisIZvoBzmMm68mXoyPpcnpahY22r6l0tvF3GLcxeWuDcjhYHgN-3bVLdk2ow2KjrvnpCVoZS5Pd10TGoNymqmF2VyJBtHr8mZaoxnJ3xEtV6wPv_IwIefet3ve79PblWJzPGxhtuhln1gKUUc3Csg63rFfhCE7pjPVeRodJYotYop-h8Q)

## Qu'est-ce qu'un arbre de décision ?

Un algorithme d'arbre de décision est l'un des algorithmes d'apprentissage automatique les plus directs. Cet algorithme, contrairement à la plupart des autres, donne un véritable aperçu de ce qu'est l'apprentissage automatique.

Un arbre de décision est un algorithme d'apprentissage automatique pour les tâches de classification et de régression. Un arbre de décision est structuré comme un arbre. Il possède un nœud racine, des nœuds internes, des nœuds feuilles et des branches.

Le tableau ci-dessous est un exemple de données représentant une classification de quatre animaux avec leurs propriétés :

<table>
  <tbody><tr>
   <td>n°
   </td>
   <td>Est sauvage
   </td>
   <td>A des pupilles rondes
   </td>
   <td>Animal
   </td>
  </tr>
  <tr>
   <td>1
   </td>
   <td>True
   </td>
   <td>True
   </td>
   <td>Loup
   </td>
  </tr>
  <tr>
   <td>2
   </td>
   <td>True
   </td>
   <td>False
   </td>
   <td>Tigre
   </td>
  </tr>
  <tr>
   <td>3
   </td>
   <td>False
   </td>
   <td>True
   </td>
   <td>Chien
   </td>
  </tr>
  <tr>
   <td>4
   </td>
   <td>False
   </td>
   <td>False
   </td>
   <td>Chat
   </td>
  </tr>
</tbody></table>

Un modèle reconnaît le ou les motifs dans le tableau, puis crée un arbre avec cette structure :

![Image](https://lh5.googleusercontent.com/_nOsF4FkJgwcrTW19w8GT4DEtnm6_bvZ5pXXzh14TuXdeEoay9Tmv5dTaPhR7xhkbFLpX4EnmMHhw1GkIvg2GCcEw08rKbCm2cyubxpfaxoIawgRtuYSkRwy6tw-5Jl2ZgpxQ0r0uV6ww21DTXcANAdIJJHyDy2lIJsVqrjX78hOK4vn3XyIQEopIA)

Le nœud racine est le premier nœud d'un arbre de décision. Les nœuds feuilles se trouvent sur la dernière ligne de l'arbre de décision. Les nœuds internes sont situés entre les nœuds racines et les nœuds feuilles. Un arbre de décision peut avoir plus d'une couche de nœuds internes.

Nous utiliserons cet algorithme dans cet article.

## Mise en route

Il existe [un certain nombre d'outils](https://lib.rs/science/ml) qui vous permettent de créer des applications d'apprentissage automatique en Rust. Tous ces outils sont excellents, mais pour ce tutoriel, vous utiliserez [Linfa](https://rust-ml.github.io/linfa/). Linfa est une boîte à outils similaire à la célèbre bibliothèque d'apprentissage automatique Python [scikit-learn](https://scikit-learn.org/).

Dans cette section, vous apprendrez comment configurer un projet Rust pour l'apprentissage automatique. Le processus de configuration d'un projet est relativement simple. Il vous suffit de suivre ces étapes :

Tout d'abord, créez un nouveau projet appelé _ml-project_ avec la commande suivante :

```bash
cargo new --bin ml-project

```

Ensuite, collez les dépendances suivantes dans le fichier _Cargo.toml_ de `ml-project`, sous `[dependencies]` :

```toml
linfa = "0.6.0"
linfa-trees = "0.6.0"
linfa-datasets = { version = "0.6.0", features = ["iris"] }

```

Enfin, exécutez la commande suivante pour construire les dépendances :

```bash
cargo build

```

Voici une explication des dépendances :

* `linfa` est le package de base pour les modèles d'apprentissage automatique Linfa.
* `linfa-trees` est un sous-package pour la construction de modèles d'arbres de décision.
* `linfa-datasets` est un package qui fournit des jeux de données déjà préparés.

Le package `linfa-datasets` est facultatif. Si vous souhaitez préparer votre propre jeu de données, suivez la section suivante.

## Comment préparer le jeu de données

La plupart des modèles d'apprentissage automatique utilisés dans les projets quotidiens sont entraînés avec des données externes, et non avec les données fournies par la boîte à outils. Dans cette section, vous apprendrez comment préparer votre propre jeu de données à partir d'un fichier CSV.

Tout d'abord, vous devez obtenir un jeu de données si vous n'en avez pas déjà un. Vous pouvez en trouver sur [Kaggle](https://www.kaggle.com/). Pour ce tutoriel, j'utiliserai le [jeu de données sur les maladies cardiaques](https://www.kaggle.com/datasets/yasserh/heart-disease-dataset). Le jeu de données ressemble à ceci :

![Image](https://lh3.googleusercontent.com/1Sc-Vza3H9Uy-6yg_LYqwrN8Sx9SITzX01wDXsvli09wYCYKFBHb9-QqwDX-_zU7whFh6b6lCa9ofyMQdy8WbZuLFQZJLolSqChhVsRwWH-beXwLgWoB7IuHJ2RBeFYF4Ef4_VOBvJQhKwknFMPDSAHttGBQGoWHJ27_clN2OPgxrklxafrmOc0vGg)

Dans ce jeu de données, `target` indique si une personne a une maladie cardiaque. 1 signifie qu'elle en a une, 0 signifie qu'elle n'en a pas.

Le reste des champs du jeu de données contient les détails de chaque personne. Un modèle peut apprendre de ce jeu de données et être capable de dire si une personne souffre d'une maladie cardiaque ou non.

Une fois que vous avez téléchargé le jeu de données, extrayez le fichier CSV dans le dossier _src_ de votre projet.

```text
.
├── Cargo.lock
├── Cargo.toml
└── src
    ├── heart.csv
    └── main.rs

```

Pour préparer un jeu de données, vous devrez ajouter les packages `csv` et `ndarray` à votre projet. Ouvrez _Cargo.toml_ et écrivez ce qui suit sous `[dependencies]` :

```toml
csv = "1.1"
ndarray = "0.15.6"

```

Maintenant, exécutez `cargo build` pour télécharger les packages, et vous êtes prêt à continuer.

Dans les étapes suivantes, je vais vous guider dans la création d'une fonction `get_dataset`. La fonction `get_dataset` lit le fichier _heart.csv_, analyse son contenu, prépare un jeu de données et le renvoie. C'est parti !

Tout d'abord, importez les packages nécessaires :

```rust
use csv::Reader;
use std::fs::File;
use ndarray::{ Array, Array1, Array2 };
use linfa::Dataset;

```

Ensuite, écrivez la fonction `get_dataset` ci-dessous dans _main.rs_ :

```rust
fn get_dataset() -> Dataset<f32, i32, ndarray::Dim<[usize; 1]>> {
 let mut reader = Reader::from_path("./src/heart.csv").unwrap();

 let headers = get_headers(&mut reader);
 let data = get_data(&mut reader);
 let target_index = headers.len() - 1;
 
 let features = headers[0..target_index].to_vec();
 let records = get_records(&data, target_index);
 let targets = get_targets(&data, target_index);

 return Dataset::new(records, targets)
   .with_feature_names(features);
}

```

Enfin, terminez en ajoutant les définitions pour `get_headers`, `get_data`, `get_records` et `get_targets` :

```rust
fn get_headers(reader: &mut Reader<File>) -> Vec<String> {
 return reader
   .headers().unwrap().iter()
   .map(|r| r.to_owned())
   .collect();
}

fn get_records(data: &Vec<Vec<f32>>, target_index: usize) -> Array2<f32> {
 let mut records: Vec<f32> = vec![];
 for record in data.iter() {
   records.extend_from_slice( &record[0..target_index] );
 }
 return Array::from( records ).into_shape((303, 13)).unwrap();
}

fn get_targets(data: &Vec<Vec<f32>>, target_index: usize) -> Array1<i32> {
 let targets = data
   .iter()
   .map(|record| record[target_index] as i32)
   .collect::<Vec<i32>>();
  return Array::from( targets );
}

fn get_data(reader: &mut Reader<File>) -> Vec<Vec<f32>> {
 return reader
   .records()
   .map(|r|
     r
       .unwrap().iter()
       .map(|field| field.parse::<f32>().unwrap())
       .collect::<Vec<f32>>()
   )
   .collect::<Vec<Vec<f32>>>();
}

```

Voici une explication étape par étape de la fonction `get_dataset` :

Tout d'abord, initialisez un lecteur pointant vers _./src/heart.csv_ :

```rust
let mut reader = Reader::from_path("./src/heart.csv").unwrap();

```

Ensuite, extrayez les en-têtes et les données du `reader` :

```rust
let headers = get_headers(&mut reader);
let data = get_data(&mut reader);

```

Ensuite, calculez l'index de `target` dans les en-têtes :

```rust
let target_index = headers.len() - 1;

```

Après cela, récupérez les caractéristiques (features) à partir de `headers` :

```rust
let features = headers[0..target_index].to_vec();

```

Ensuite, récupérez les enregistrements (records) et les cibles (targets) à partir de `data` :

```rust
let records = get_records(&data, target_index);
let targets = get_targets(&data, target_index);

```

Enfin, construisez le jeu de données avec `records`, `targets` et `features`, puis renvoyez-le :

```rust
return Dataset::new(records, targets)
   .with_feature_names(features);

```

Pour terminer la fonction et voir à quoi ressemble le jeu de données, utilisez ceci comme fonction `main` :

```rust
fn main() {
   let dataset = get_dataset();
   println!("{:?}", dataset);
}

```

Une fois que vous avez défini cela comme fonction principale et que vous l'exécutez avec `cargo run`, vous verrez le jeu de données dans la sortie :

```rust
DatasetBase { records: [[63.0, 1.0, 3.0, 145.0, 233.0, ..., 0.0, 2.3, 0.0, 0.0, 1.0],
 [37.0, 1.0, 2.0, 130.0, 250.0, ..., 0.0, 3.5, 0.0, 0.0, 2.0],
 [41.0, 0.0, 1.0, 130.0, 204.0, ..., 0.0, 1.4, 2.0, 0.0, 2.0],
 [56.0, 1.0, 1.0, 120.0, 236.0, ..., 0.0, 0.8, 2.0, 0.0, 2.0],
 [57.0, 0.0, 0.0, 120.0, 354.0, ..., 1.0, 0.6, 2.0, 0.0, 2.0],
 ...,
 [57.0, 0.0, 0.0, 140.0, 241.0, ..., 1.0, 0.2, 1.0, 0.0, 3.0],
 [45.0, 1.0, 3.0, 110.0, 264.0, ..., 0.0, 1.2, 1.0, 0.0, 3.0],
 [68.0, 1.0, 0.0, 144.0, 193.0, ..., 0.0, 3.4, 1.0, 2.0, 3.0],
 [57.0, 1.0, 0.0, 130.0, 131.0, ..., 1.0, 1.2, 1.0, 1.0, 3.0],
 [57.0, 0.0, 1.0, 130.0, 236.0, ..., 0.0, 0.0, 1.0, 1.0, 2.0]], shape=[303, 13], strides=[13, 1], layout=Cc (0x5), const ndim=2, targets: [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], shape=[303], strides=[1], layout=CFcf (0xf), const ndim=1, weights: [], shape=[0], strides=[0], layout=CFcf (0xf), const ndim=1, feature_names: ["age", "sex", "cp", "trestbps", "chol", "fbs", "restecg", "thalach", "exang", "oldpeak", "slope", "ca", "thal"] }

```

## Comment créer un modèle d'arbre de décision

Dans cette section, je vais vous montrer comment créer un modèle d'arbre de décision et l'entraîner. Le jeu de données que j'utiliserai est le jeu de données Iris fourni par `linfa-datasets`.

Le jeu de données Iris contient un enregistrement de la largeur du sépale, de la hauteur du sépale, de la largeur du pétale et de la hauteur du pétale de plusieurs iris, et classe chaque enregistrement selon des espèces étiquetées par des numéros.

Le code pour le modèle est simple. Ouvrez le fichier _main.rs_ et collez-y ce qui suit :

```rust
use linfa_trees::DecisionTree;
use linfa::prelude::*;

fn main() {
    let (train, test) = linfa_datasets::iris()
        .split_with_ratio(0.9);

    let model = DecisionTree::params()
        .fit(&train).unwrap();
    
    let predictions = model.predict(&test);
    
    println!("{:?}", predictions);
    println!("{:?}", test.targets);
}

```

Voici une explication :

Tout d'abord, importez les packages nécessaires :

```rust
use linfa_trees::DecisionTree;
use linfa::prelude::*;

```

Ensuite, récupérez le jeu de données et divisez-le en données de test et d'entraînement :

```rust
let (train, test) = linfa_datasets::iris()
    .split_with_ratio(0.9);

```

Après cela, initialisez le modèle et entraînez-le avec les données d'entraînement :

```rust
let model = DecisionTree::params()
    .fit(&train).unwrap();

```

Ensuite, utilisez les données de test pour faire des prédictions :

```rust
let predictions = model.predict(&test);

```

Enfin, comparez les prédictions avec les valeurs réelles :

```rust
println!("{:?}", predictions);
println!("{:?}", test.targets);

```

Si vous lancez le programme avec `cargo run`, vous obtiendrez la catégorie prédite et la catégorie réelle dans le terminal en sortie :

```rust
$ cargo run
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], shape=[15], strides=[1], layout=CFcf (0xf), const ndim=1
[2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], shape=[15], strides=[1], layout=CFcf (0xf), const ndim=1

```

D'après ce qui précède, vous pouvez voir que ce modèle est précis à 100 %. Ce ne sera pas toujours le cas pour tous les modèles d'apprentissage automatique. Si vous mélangez le jeu de données avant d'entraîner le modèle ci-dessus, le modèle pourrait ne plus être aussi précis.

L'objectif de l'apprentissage automatique est d'être aussi précis que possible. La plupart du temps, une précision de 100 % n'est pas réalisable.

## Conclusion

Dans ce tutoriel, vous avez appris quelques notions sur l'apprentissage automatique et vous avez également vu comment créer un modèle d'arbre de décision en utilisant Rust.

Les modèles d'apprentissage automatique dans Linfa suivent un processus similaire de construction et d'entraînement. Ainsi, tout ce que vous avez à faire pour utiliser d'autres types de modèles est de vous renseigner sur chacun d'eux, et vous serez prêt à vous lancer.

Vous pouvez en apprendre davantage sur Linfa et les modèles qu'il prend en charge en consultant [sa documentation](https://docs.rs/linfa/latest/linfa/).

Merci de m'avoir lu, et bon codage !