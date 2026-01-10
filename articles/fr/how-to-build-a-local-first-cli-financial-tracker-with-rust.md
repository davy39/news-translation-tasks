---
title: Comment créer un gestionnaire financier en ligne de commande local-first avec
  Rust [Guide complet]
subtitle: ''
author: Stephen Emmanuel
date: '2026-01-09T22:40:38.493Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-local-first-cli-financial-tracker-with-rust
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1767998415383/82c48f39-cd5e-4f66-af83-2b65bafccd65.png
tags:
- name: Rust
  slug: rust
- name: handbook
  slug: handbook
seo_title: Comment créer un gestionnaire financier en ligne de commande local-first
  avec Rust [Guide complet]
seo_desc: Most financial apps store your sensitive data on remote servers. This requires
  you to trust a company with your records and rely on their service staying online.
  But if you build a local-first application, you can keep your data on your own machine
  i...
---

La plupart des applications financières stockent vos données sensibles sur des serveurs distants. Cela vous oblige à confier vos enregistrements à une entreprise et à dépendre de la disponibilité de leur service. Mais si vous construisez une application local-first, vous pouvez conserver vos données sur votre propre machine dans un format que vous pouvez réellement lire.

Dans ce guide, vous apprendrez à créer un gestionnaire financier qui s'exécute entièrement dans votre terminal. Vous utiliserez Rust pour construire un système qui sauvegarde les transactions dans un fichier JSON local, vous garantissant ainsi la propriété totale de vos informations.

En chemin, vous apprendrez à utiliser le système de types de Rust pour valider les données financières et gérer les erreurs de fichiers avec élégance. Vous utiliserez également la bibliothèque Clap pour créer une interface en ligne de commande professionnelle. À la fin, vous comprendrez comment gérer l'état local, sérialiser des données avec Serde et structurer une application Rust modulaire.

## Table des matières

1. [Prérequis](#heading-prerequis)
    
2. [Commandes que vous allez créer](#heading-commandes-que-vous-allez-creer)
    
3. [Étape 1 : Configuration du projet](#heading-etape-1-configuration-du-projet)
    
4. [Étape 2 : Conception du modèle de données](#heading-etape-2-conception-du-modele-de-donnees)
    
    * [Ajouter des méthodes à TrackerData](#heading-ajouter-des-methodes-a-trackerdata)
        
5. [Étape 3 : Gestion correcte des erreurs](#heading-etape-3-gestion-correcte-des-erreurs)
    
    * [Mapper les erreurs système vers les erreurs personnalisées](#heading-mapper-les-erreurs-systeme-vers-les-erreurs-personnalisees)
        
    * [Préparer la sortie des erreurs](#heading-preparer-la-sortie-des-erreurs)
        
6. [Étape 4 : Création des opérations de fichier](#heading-etape-4-creation-des-operations-de-fichier)
    
    * [Ajouter des fonctions utilitaires JSON](#heading-ajouter-des-fonctions-utilitaires-json)
        
    * [Enregistrer les utilitaires](#heading-enregistrer-les-utilitaires)
        
7. [Étape 5 : Configuration de la structure CLI](#heading-etape-5-configuration-de-la-structure-cli)
    
    * [L'architecture des commandes](#heading-larchitecture-des-commandes)
        
    * [Gérer les chemins avec le contexte global](#heading-gerer-les-chemins-avec-le-contexte-global)
        
    * [Enregistrer le système de commandes](#heading-enregistrer-le-systeme-de-commandes)
        
8. [Étape 6 : Création des types de réponse](#heading-etape-6-creation-des-types-de-reponse)
    
    * [Définir les structures de réponse](#heading-definir-les-structures-de-reponse)
        
    * [Implémenter le module de sortie](#heading-implementer-le-module-de-sortie)
        
    * [Mettre à jour l'enregistrement de la bibliothèque](#heading-mettre-a-jour-lenregistrement-de-la-bibliotheque)
        
9. [Étape 7 : Création d'aides pour l'analyse des arguments](#heading-etape-7-creation-daides-pour-lanalyse-des-arguments)
    
    * [Implémenter des analyseurs de données personnalisés](#heading-implementer-des-analyseurs-de-donnees-personnalises)
        
10. [Étape 8 : Implémenter la commande Init](#heading-etape-8-implementer-la-commande-init)
    
11. [Étape 9 : Implémenter la commande Add](#heading-etape-9-implementer-la-commande-add)
    
12. [Étape 10 : Implémenter la commande List](#heading-etape-10-implementer-la-commande-list)
    
13. [Étape 11 : Implémenter la commande Update](#heading-etape-11-implementer-la-commande-update)
    
14. [Étape 12 : Implémenter la commande Delete](#heading-etape-12-implementer-la-commande-delete)
    
15. [Étape 13 : Implémenter les commandes de sous-catégorie](#heading-etape-13-implementer-les-commandes-de-sous-categorie)
    
    * [Lister les sous-catégories](#heading-lister-les-sous-categories)
        
    * [Ajouter des sous-catégories](#heading-ajouter-des-sous-categories)
        
    * [Supprimer des sous-catégories](#heading-supprimer-des-sous-categories)
        
    * [Renommer des sous-catégories](#heading-renommer-des-sous-categories)
        
16. [Étape 14 : Implémenter la commande Total](#heading-etape-14-implementer-la-commande-total)
    
17. [Étape 15 : Assemblage de la fonction principale](#heading-etape-15-assemblage-de-la-fonction-principale)
    
18. [Tester votre application](#heading-tester-votre-application)
    
    * [Installer le binaire](#heading-installer-le-binaire)
        
19. [Et après et fonctionnalités avancées](#heading-et-apres-et-fonctionnalites-avancees)
    
    * [Fonctionnalités avancées à explorer](#heading-fonctionnalites-avancees-a-explorer)
        
20. [Conclusion](#heading-conclusion)
    

## Prérequis

Pour suivre ce tutoriel, vous devriez avoir un niveau de confort de base avec la syntaxe Rust. Vous n'avez pas besoin d'être un expert, mais vous devriez comprendre comment utiliser les variables, les fonctions et les structures.

Vous aurez également besoin des outils et connaissances suivants :

* Rust installé (version 1.70 ou ultérieure). Si Rust n'est pas installé, suivez le [guide d'installation officiel](https://rust-book.cs.brown.edu/ch01-01-installation.html). Vous pouvez vérifier votre installation en exécutant `rustc --version` dans votre terminal.
    
* Familiarité avec les outils en ligne de commande et l'utilisation du terminal.
    
* Connaissances de base du format JSON.
    

## Commandes que vous allez créer

Ce tutoriel vous guidera pour implémenter ces commandes étape par étape :

* `init` : Initialise un nouveau gestionnaire et crée votre fichier de stockage.
    
* `add` : Enregistre de nouveaux revenus ou dépenses dans vos données.
    
* `list` : Vous permet de visualiser et de filtrer vos transactions enregistrées.
    
* `update` : Modifie les enregistrements existants dans votre stockage.
    
* `delete` : Supprime des enregistrements spécifiques de votre historique.
    
* `subcategory` : Gère les sous-catégories personnalisées (lister, ajouter, supprimer, renommer).
    
* `total` : Calcule vos totaux financiers et votre solde net.
    

## Étape 1 : Configuration du projet

Pour commencer, vous devez créer un nouveau projet Rust. Ouvrez votre terminal et exécutez ces commandes :

```bash
cargo new fintrack
cd fintrack
```

Cela crée un nouveau répertoire appelé `fintrack` avec une structure de projet Rust de base. `cargo` est le gestionnaire de paquets et l'outil de construction de Rust. Il gère les dépendances, la compilation et la gestion du projet.

Maintenant, ouvrez `Cargo.toml` dans votre éditeur. Ce fichier définit les métadonnées et les bibliothèques de votre projet. Ajoutez les dépendances suivantes dont votre application aura besoin :

```toml
[package]
name = "fintrack"
version = "1.0.0"
edition = "2021"

[dependencies]
chrono = "0.4.42"
clap = { version = "4.5.53", features = ["derive"] }
dirs = "6.0.0"
serde = { version = "1.0.228", features = ["derive"] }
serde_json = "1.0.148"
strum = { version = "0.26", features = ["derive"] }
```

Voici ce que fait chaque dépendance dans votre projet :

* `chrono` : Gère les dates et les heures. Vous l'utiliserez pour analyser les dates saisies par l'utilisateur et les formater pour l'affichage.
    
* `clap` : Une bibliothèque pour construire des interfaces en ligne de commande. Elle gère le processus d'analyse et de validation des arguments que vous tapez dans le terminal.
    
* `dirs` : Fournit un moyen multiplateforme de trouver le répertoire personnel de l'utilisateur, où vous stockerez les données du gestionnaire.
    
* `serde` et `serde_json` : `serde` est le framework de sérialisation de Rust. Combiné avec `serde_json`, il vous permet de convertir des structures Rust en JSON et inversement. C'est ainsi que vous sauvegarderez et chargerez vos données.
    
* `strum` : Fournit des macros pour générer automatiquement du code utile pour les enums, comme la conversion en chaînes de caractères et l'analyse de chaînes en enums.
    

L'option `features = ["derive"]` pour `clap` et `serde` active leurs macros de dérivation, ce qui vous permettra d'utiliser des attributs comme `#[derive(...)]` pour générer automatiquement le code nécessaire à l'analyse et à la conversion des données.

## Étape 2 : Conception du modèle de données

Avant d'écrire toute logique de commande, vous voudrez définir la structure des données que votre gestionnaire stockera. En Rust, vous utilisez des structures (`structs`) pour regrouper des données liées, un peu comme un enregistrement dans une base de données, et des **enums** pour représenter des valeurs qui ne peuvent être que l'une des plusieurs variantes fixes.

Créez un nouveau fichier `src/models.rs` et ajoutez le code pour définir un enregistrement :

```rust
use chrono::NaiveDate;
use serde::{Deserialize, Serialize};
use std::collections::HashMap;

#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct Record {
    pub id: usize,
    pub category: usize,
    pub amount: f64,
    pub subcategory: usize,
    pub description: String,
    pub date: String,
}
```

Cette structure `Record` représente une seule transaction de revenu ou de dépense. L'attribut `#[derive(...)]` implémente automatiquement des traits qui vous permettent d'afficher la structure pour le débogage, de la copier et de la convertir vers ou depuis le format JSON. Le mot-clé `pub` garantit que ces champs sont accessibles aux autres modules que vous allez construire.

Ensuite, ajoutez la structure de données principale au fichier `src/models.rs` :

```rust
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct TrackerData {
    pub version: u32,
    pub currency: String,
    pub created_at: String,
    pub last_modified: String,
    pub opening_balance: f64,
    pub categories: HashMap<String, usize>,
    pub subcategories_by_id: HashMap<usize, String>,
    pub subcategories_by_name: HashMap<String, usize>,
    pub next_subcategory_id: u32,
    pub records: Vec<Record>,
    pub next_record_id: usize,
}
```

Cette structure contient l'état de l'application entière. Elle utilise une `HashMap` pour les catégories et les sous-catégories afin de permettre des recherches rapides par nom ou par ID. Toutes les transactions individuelles sont stockées dans le vecteur `records`, qui peut croître dynamiquement au fur et à mesure que vous ajoutez des données.

Maintenant, ajoutez des enums pour gérer vos catégories fixes et les devises prises en charge :

```rust
#[derive(clap::ValueEnum, Clone, Debug, strum::Display, strum::EnumString)]
#[strum(serialize_all = "lowercase", ascii_case_insensitive)]
pub enum Category {
    Income,
    Expenses,
}

#[derive(clap::ValueEnum, Clone, Debug, strum::Display, strum::EnumString)]
#[strum(serialize_all = "UPPERCASE", ascii_case_insensitive)]
pub enum Currency {
    NGN,
    USD,
    GBP,
    EUR,
    CAD,
    AUD,
    JPY,
}
```

Ces enums garantissent que l'utilisateur ne peut saisir que des catégories ou des devises valides. Les attributs `strum` gèrent la conversion entre les chaînes de caractères saisies dans le terminal et votre code Rust, tandis que `clap::ValueEnum` permet à ces types de fonctionner directement avec vos arguments de ligne de commande.

### Ajouter des méthodes à TrackerData

Pour interagir avec ces données dans la structure `TrackerData`, vous devez ajouter des méthodes en utilisant un bloc `impl`. Ces méthodes géreront l'ajout d'enregistrements et le calcul des totaux :

```rust
impl TrackerData {
    pub fn push_record(&mut self, record: Record) -> &Self {
        self.records.push(record);
        self
    }

    pub fn category_id(&self, category: &str) -> usize {
        self.categories[category]
    }

    pub fn miscellaneous_subcategory_id(&self) -> Option<usize> {
        self.subcategories_by_name.get("miscellaneous").copied()
    }

    pub fn subcategory_id(&self, name: &str) -> Option<usize> {
        self.subcategories_by_name.get(&name.to_lowercase()).copied()
    }

    pub fn category_name(&self, id: usize) -> Option<&String> {
        self.categories.iter().find(|(_, v)| **v == id).map(|(k, _)| k)
    }

    pub fn subcategory_name(&self, id: usize) -> Option<&String> {
        self.subcategories_by_id.get(&id)
    }

    pub fn totals(&self) -> (f64, f64) {
        self.records.iter().fold((0.0, 0.0), |mut acc, r| {
            if r.category == 1 {
                acc.0 += r.amount;
            } else {
                acc.1 += r.amount;
            }
            acc
        })
    }
}
```

Ces méthodes utilisent des modèles Rust clés pour gérer l'état du gestionnaire :

* `&mut self` est utilisé lorsque vous devez modifier les données, comme l'ajout d'un nouvel enregistrement dans le vecteur.
    
* `Option` gère les cas où une valeur pourrait ne pas exister, renvoyant `Some(valeur)` ou `None`.
    
* `iter()` et `fold` sont utilisés dans la méthode `totals()` pour traiter tous les enregistrements et accumuler le revenu total et les dépenses totales dans un seul tuple `(f64, f64)`.
    

Enfin, ajoutez une fonction d'aide pour créer la structure JSON par défaut du gestionnaire. Ajoutez ceci à `src/models.rs` :

```rust
pub fn default_tracker_json(currency: &Currency, opening_balance: f64) -> serde_json::Value {
    serde_json::json!({
        "version": 1,
        "currency": currency.to_string(),
        "opening_balance": opening_balance,
        "created_at": chrono::Utc::now().to_rfc3339(),
        "last_modified": chrono::Utc::now().to_rfc3339(),
        "categories": {
            "income": 1,
            "expenses": 2
        },
        "subcategories_by_id": {
            "1": "miscellaneous"
        },
        "subcategories_by_name": {
            "miscellaneous": 1
        },
        "records": [],
        "next_record_id": 1,
        "next_subcategory_id": 2
    })
}
```

Ensuite, enregistrez ce module dans votre fichier `src/lib.rs` afin que le reste de votre application puisse l'utiliser :

```rust
pub mod models;
```

## Étape 3 : Gestion correcte des erreurs

Dans une application financière, la gestion des erreurs est cruciale pour garantir que vous ne perdez ni ne corrompez vos données. Rust utilise un type `Result` pour gérer les opérations qui pourraient échouer. Un `Result` est soit un `Ok` contenant la valeur de succès, soit un `Err` contenant les détails de l'erreur. Cette structure vous oblige à traiter explicitement les échecs potentiels avant que votre code ne puisse être compilé.

Créez un nouveau fichier nommé `src/error.rs` et commencez par les importations nécessaires :

```rust
use std::io;
```

Maintenant, définissez vos propres types d'erreurs à l'aide d'enums :

```rust
#[derive(Debug)]
pub enum ValidationErrorKind {
    AmountTooSmall { amount: f64 },
    InvalidDate { provided: String, expected_format: String },
    SubcategoryNotFound { name: String },
    SubcategoryAlreadyExists { name: String },
    RecordNotFound { id: usize },
    SubcategoryHasRecords { name: String, count: usize },
    CannotDeleteMiscellaneous,
    CategoryImmutable { category: usize },
    InvalidCategoryName { name: String, reason: String },
    InvalidName { name: String, reason: String },
    InvalidAmount { reason: String },
    TrackerAlreadyInitialized,
    InvalidSubcommand { subcommand: String },
}

#[derive(Debug)]
pub enum CliError {
    FileNotFound(String),
    InvalidJson(String),
    ValidationError(ValidationErrorKind),
    PermissionDenied(String),
    CorruptedData { backup_restored: bool, timestamp: String },
    FileAlreadyExists,
    Other(String),
}
```

Cette structure imbriquée vous permet de catégoriser chaque échec possible pouvant survenir lors de l'exécution de votre programme. L'enum `CliError` agit comme le conteneur de haut niveau pour toutes les erreurs de l'application. Il gère des erreurs telles que les fichiers manquants, les permissions refusées, les erreurs de validation, les conflits d'existence de fichiers, etc.

Une variante spécifique, `ValidationError`, transporte un `ValidationErrorKind` comme contenu. Cela vous permet de regrouper tous les échecs spécifiques à la validation (tels que des formats de date invalides, des noms de sous-catégories en double ou des tentatives de suppression de catégories système protégées) sous un seul type d'erreur tout en préservant les détails spécifiques de ce qui s'est mal passé.

Structurer vos erreurs de cette manière vous permet de signaler exactement ce qui a causé un échec aux côtés des données spécifiques qui l'ont déclenché. Par exemple, une erreur de validation peut inclure le montant exact ou la date qui a échoué à vos règles, tandis qu'une erreur système peut identifier le chemin de fichier spécifique ou le problème de permission qui a arrêté le programme.

### Mapper les erreurs système vers les erreurs personnalisées

Pour garder le code de votre application propre, vous pouvez utiliser le trait `From` pour convertir automatiquement les erreurs système de bas niveau en votre `CliError` personnalisée. Cela vous permet d'utiliser l'opérateur `?` plus tard dans votre logique pour propager les erreurs avec élégance.

Ajoutez ces implémentations à `src/error.rs` :

```rust
impl From<std::io::Error> for CliError {
    fn from(err: std::io::Error) -> Self {
        match err.kind() {
            std::io::ErrorKind::NotFound => CliError::FileNotFound(err.to_string()),
            std::io::ErrorKind::PermissionDenied => CliError::PermissionDenied(err.to_string()),
            std::io::ErrorKind::AlreadyExists => CliError::FileAlreadyExists,
            // ... ajoutez-en d'autres ici si nécessaire.
            _ => CliError::Other(format!("Erreur IO : {}", err)),
        }
    }
}

impl From<serde_json::Error> for CliError {
    fn from(err: serde_json::Error) -> Self {
        CliError::InvalidJson(err.to_string())
    }
}
```

Le bloc `match` à l'intérieur de l'implémentation de `std::io::Error` vous permet d'inspecter l'erreur système et de la catégoriser correctement. Si le système signale une erreur "NotFound", votre application la transforme en `CliError::FileNotFound`. Cela garantit que vos messages destinés à l'utilisateur restent cohérents.

### Préparer la sortie des erreurs

Enfin, ajoutez une signature de méthode au bloc `CliError`. Cela connectera plus tard votre logique d'erreur à un module de sortie dédié qui formate ces erreurs pour le terminal :

```rust
impl CliError {
    pub fn write_to(&self, writer: &mut impl std::io::Write) -> io::Result<()> {
        crate::output::write_error(self, writer)
    }
}
```

Le paramètre `&mut impl std::io::Write` est un moyen flexible de dire que cette méthode peut écrire dans n'importe quel flux de sortie, qu'il s'agisse du flux d'erreur standard dans le terminal ou d'un fichier journal.

Enregistrez le module d'erreur dans votre fichier `src/lib.rs` afin qu'il soit disponible pour le reste de votre projet :

```rust
pub mod models;
pub mod error;
```

## Étape 4 : Création des opérations de fichier

Pour gérer les données de votre gestionnaire, vous avez besoin d'un moyen fiable de lire et d'écrire des fichiers JSON. Au lieu de répéter la logique de fichier dans chaque commande, vous allez créer un trait. En Rust, les traits vous permettent d'ajouter de nouvelles méthodes à des types existants. Ici, vous ajouterez des méthodes de gestion de fichiers personnalisées directement à `Path` et `PathBuf`.

Tout d'abord, créez un nouveau répertoire nommé `src/utils` et créez un fichier à l'intérieur appelé `src/utils/file.rs`. Commencez par les importations nécessaires :

```rust
use std::{
  fs::{self, File},
  io::{self, prelude::*},
  path::Path,
};

use serde_json::Value;

use crate::CliError;
```

Maintenant, définissez et implémentez le trait `FilePath` :

```rust
pub trait FilePath: AsRef<Path> {
    fn create_file_if_not_exists(&self) -> io::Result<File> {
        let path = self.as_ref();
        if let Some(parent) = path.parent() {
            fs::create_dir_all(parent)?;
        }
        File::options().write(true).create_new(true).open(path)
    }

    fn read_file(&self) -> io::Result<File> {
        File::options().read(true).open(self.as_ref())
    }

    fn open_read_write(&self) -> io::Result<File> {
        File::options().read(true).write(true).open(self.as_ref())
    }

    fn open_read(&self) -> io::Result<File> {
        File::options().read(true).open(self.as_ref())
    }

    fn delete_if_exists(&self) -> io::Result<()> {
        let path = self.as_ref();
        if !path.exists() {
            return Ok(());
        }
        if path.is_dir() {
            fs::remove_dir_all(path)?;
        } else {
            fs::remove_file(path)?;
        }
        Ok(())
    }
}

impl<P: AsRef<Path>> FilePath for P {}
```

Cette "implémentation globale" à la fin est puissante. Elle garantit que tout type capable de représenter un chemin de fichier, comme un `PathBuf` ou une `String` standard, gagne automatiquement ces méthodes.

Tout au long de ces méthodes, vous utilisez l'opérateur `?`. C'est le raccourci de Rust pour la propagation d'erreurs. Si une opération comme `create_dir_all` échoue, le `?` renvoie immédiatement l'erreur de la fonction. Si elle réussit, le programme continue à la ligne suivante. Cela garde votre logique plate et lisible sans vérifications d'erreurs imbriquées.

### Ajouter des fonctions utilitaires JSON

L'écriture de données financières dans un fichier nécessite de la précision. Vous devez vous assurer que vous écrasez complètement les anciennes données plutôt que de simplement les ajouter à la fin. Ajoutez cette fonction d'aide à `src/utils/file.rs` :

```rust
pub fn write_json_to_file(json: &Value, file: &mut File) -> Result<(), CliError> {
    let json_string = serde_json::to_string_pretty(&json)?;

    file.seek(io::SeekFrom::Start(0))?;
    file.set_len(0)?;
    file.write_all(json_string.as_bytes())?;

    Ok(())
}
```

L'appel à `seek` ramène le pointeur de fichier au tout début, et `set_len(0)` tronque le fichier à zéro octet. L'utilisation de `to_string_pretty` garantit que votre fichier JSON est lisible par l'homme, ce qui correspond à l'objectif local-first de garder vos données accessibles.

### Enregistrer les utilitaires

Pour rendre ces outils disponibles pour le reste de votre application, vous devez configurer l'arborescence des modules. Créez `src/utils.rs` et ajoutez cette ligne :

```rust
pub mod file;
```

Ensuite, mettez à jour votre fichier `src/lib.rs` pour inclure le nouveau module `utils` et exporter les types que vous avez construits jusqu'à présent :

```rust
pub mod models;
pub mod error;
pub mod utils;

pub use error::{CliError, ValidationErrorKind};
pub use models::{Category, Currency, Record, TrackerData};
```

## Étape 5 : Configuration de la structure CLI

Dans cette étape, vous allez organiser l'interface qui permet aux utilisateurs d'interagir avec votre code. Construire une CLI est plus que simplement lire des chaînes de caractères. Cela implique de mapper des commandes de terminal spécifiques à la logique interne de votre application.

### L'architecture des commandes

Vous suivrez un modèle modulaire où chaque commande a sa propre définition et sa propre logique d'exécution. Cette séparation garantit que l'ajout d'une nouvelle fonctionnalité à l'avenir ne cassera pas vos commandes existantes.

Créez un fichier nommé `src/commands.rs`. Ce fichier agit comme un répartiteur central qui déclare vos modules de commande et achemine l'entrée du terminal vers la fonction correcte :

```rust
use crate::{CliResult, command_prelude::*};
use clap::{ArgMatches, Command};

pub type Exec = fn(&mut GlobalContext, &ArgMatches) -> CliResult;

pub fn cli() -> Vec<Command> {
    vec![
        init::cli(),
        add::cli(),
        list::cli(),
        update::cli(),
        delete::cli(),
        subcategory::cli(),
        total::cli(),
    ]
}

pub fn build_exec(cmd: &str) -> Option<Exec> {
    match cmd {
        "init" => Some(init::exec),
        "add" => Some(add::exec),
        "list" => Some(list::exec),
        "update" => Some(update::exec),
        "delete" => Some(delete::exec),
        "subcategory" => Some(subcategory::exec),
        "total" => Some(total::exec),
        _ => None,
    }
}

pub mod init;
pub mod add;
pub mod list;
pub mod update;
pub mod delete;
pub mod subcategory;
pub mod total;
```

L'alias de type `Exec` définit une signature standard pour toutes vos fonctions de commande. Chaque commande recevra le contexte global et les arguments analysés par `clap`, et chaque commande renverra un `CliResult`.

La fonction `build_exec` utilise ensuite le filtrage par motif (`pattern matching`) pour renvoyer la logique d'exécution spécifique associée à la saisie de l'utilisateur.

### Gérer les chemins avec le contexte global

Puisque votre application est local-first, elle doit savoir exactement où trouver le répertoire de données sur différents systèmes d'exploitation. Vous allez créer une structure `GlobalContext` pour centraliser ces chemins afin de ne pas avoir à les reconstruire manuellement dans chaque module de commande.

Créez maintenant `src/utils/context.rs` pour gérer les chemins de fichiers :

```rust
use std::path::PathBuf;

#[derive(Debug)]
pub struct GlobalContext {
    home_path: PathBuf,
    base_path: PathBuf,
    tracker_path: PathBuf,
}

impl GlobalContext {
    pub fn new(home_dir: PathBuf) -> Self {
        let base_path = home_dir.join(".fintrack");
        let tracker_path = base_path.join("tracker.json");

        GlobalContext {
            home_path: home_dir,
            base_path,
            tracker_path,
        }
    }

    pub fn tracker_path(&self) -> &PathBuf {
        &self.tracker_path
    }

    pub fn home_path(&self) -> &PathBuf {
        &self.home_path
    }

    pub fn base_path(&self) -> &PathBuf {
        &self.base_path
    }
}
```

La méthode `join()` est un moyen multiplateforme de combiner des chemins. Elle utilise automatiquement le séparateur correct pour votre système d'exploitation, comme une barre oblique inverse (`\`) sur Windows ou une barre oblique (`/`) sur Linux.

### Enregistrer le système de commandes

Pour lier ces composants ensemble, mettez à jour vos fichiers d'utilitaires et de bibliothèque. Dans `src/utils.rs`, ajoutez le module de contexte :

```rust
pub mod file;
pub mod context;
```

Enfin, mettez à jour `src/lib.rs` pour exposer les structures de commande et le nouveau type de contexte. Vous définirez également un alias de type `CliResult` pour garder vos signatures de fonction cohérentes dans tout le projet :

```rust
pub mod models;
pub mod error;
pub mod utils;
pub mod commands;

pub use error::*;
pub use models::*;
pub use utils::command_prelude;
pub use utils::context::GlobalContext;
pub use utils::parsers;
```

En définissant le type de résultat ici, vous vous assurez que chaque commande suit les mêmes règles de gestion d'erreurs et de réponse que vous avez établies dans les étapes précédentes.

## Étape 6 : Création des types de réponse

Les commandes de votre gestionnaire font plus que simplement exécuter une logique. Elles renvoient des données qui doivent être formatées et affichées à l'utilisateur.

Dans un outil en ligne de commande, votre « interface utilisateur » est le texte imprimé dans le terminal, vous avez donc besoin d'un moyen structuré de gérer divers résultats. Vous allez créer une enum `ResponseContent` pour catégoriser ces différentes sorties, telles que des enregistrements uniques, des listes de transactions ou des totaux financiers. Cela garantit que votre application communique clairement à la fois les résultats réussis et les messages d'erreur informatifs.

### Définir les structures de réponse

Ouvrez votre fichier `src/models.rs` et ajoutez ces structures pour gérer la manière dont l'application empaquette ses données :

Ajoutez à `src/models.rs` :

```rust
#[derive(Debug)]
pub enum ResponseContent {
    Message(String),
    Record {
        record: Record,
        tracker_data: TrackerData,
        is_update: bool,
    },
    List {
        records: Vec<Record>,
        tracker_data: TrackerData,
    },
    TrackerData(TrackerData),
    Total(Total),
    Categories(Vec<(usize, String)>),
    Subcategories(Vec<(usize, String)>),
}

#[derive(Debug, Clone)]
pub struct Total {
    pub currency: Currency,
    pub opening_balance: f64,
    pub income_total: f64,
    pub expenses_total: f64,
}

#[derive(Debug)]
pub struct CliResponse {
    content: Option<ResponseContent>,
}

impl CliResponse {
    pub fn new(content: ResponseContent) -> Self {
        CliResponse {
            content: Some(content),
        }
    }

    pub fn success() -> Self {
        CliResponse { content: None }
    }

    pub fn content(&self) -> Option<&ResponseContent> {
        self.content.as_ref()
    }

    pub fn write_to(&self, writer: &mut impl std::io::Write) -> std::io::Result<()> {
        crate::output::write_response(self, writer)
    }
}

pub type CliResult = Result<CliResponse, CliError>;
```

La structure `CliResponse` agit comme un conteneur pour votre sortie. En utilisant un `Option<ResponseContent>`, vous pouvez représenter un simple message de succès lorsque le contenu est `None`, ou fournir des données plus complexes comme une structure `Total` si nécessaire. Cette approche maintient la cohérence de votre logique de commande car chaque opération renverra le même type de réponse.

### Implémenter le module de sortie

Ensuite, vous avez besoin d'un endroit central pour transformer ces types Rust en texte formaté pour le terminal. Créez un nouveau fichier nommé `src/output.rs`. Ce module gérera la logique d'impression pour les réponses réussies et les erreurs que vous avez définies précédemment.

```rust
use crate::{CliError, CliResponse, ResponseContent};

pub fn write_response(res: &CliResponse, writer: &mut impl std::io::Write) -> std::io::Result<()> {
    let Some(content) = res.content() else {
        writeln!(writer, "✓ Succès")?;
        return Ok(());
    };

    match content {
        ResponseContent::Message(msg) => {
            writeln!(writer, "✓ {}", msg)?;
        }
        ResponseContent::Record { record, .. } => {
            writeln!(writer, "✓ Enregistrement créé :")?;
            writeln!(writer, "  ID : {}", record.id)?;
            writeln!(writer, "  Montant : {}", record.amount)?;
            // Plus de formatage plus tard
        }
        ResponseContent::List { records, .. } => {
            for record in records {
                writeln!(writer, "{:?}", record)?;
            }
        }
        ResponseContent::Total(total) => {
            writeln!(writer, "Solde d'ouverture : {} {}", total.opening_balance, total.currency)?;
            writeln!(writer, "Revenu total : {} {}", total.income_total, total.currency)?;
            writeln!(writer, "Dépenses totales : {} {}", total.expenses_total, total.currency)?;
            let net_balance = total.opening_balance + total.income_total - total.expenses_total;
            writeln!(writer, "Solde net : {} {}", net_balance, total.currency)?;
        }
        _ => {}
    }
    Ok(())
}

pub fn write_error(err: &CliError, writer: &mut impl std::io::Write) -> std::io::Result<()> {
    match err {
        CliError::FileNotFound(msg) => writeln!(writer, "Erreur : Fichier non trouvé : {}", msg),
        CliError::InvalidJson(msg) => writeln!(writer, "Erreur : JSON invalide : {}", msg),
        CliError::ValidationError(kind) => {
            match kind {
                crate::ValidationErrorKind::AmountTooSmall { amount } => {
                    writeln!(writer, "Erreur : Le montant doit être supérieur à 0, reçu {}", amount)
                }
                crate::ValidationErrorKind::SubcategoryNotFound { name } => {
                    writeln!(writer, "Erreur : Sous-catégorie '{}' non trouvée", name)
                }
                crate::ValidationErrorKind::RecordNotFound { id } => {
                    writeln!(writer, "Erreur : Enregistrement avec l'ID {} non trouvé", id)
                }
                _ => writeln!(writer, "Erreur : La validation a échoué"),
            }
        }
        CliError::FileAlreadyExists => {
            writeln!(writer, "Erreur : Gestionnaire déjà initialisé. Utilisez 'fintrack clear' pour recommencer à zéro.")
        }
        _ => writeln!(writer, "Erreur : {}", err),
    }
}
```

En centralisant la logique de sortie dans ce module, vous remplissez l'objectif de signaler les données exactes qui ont causé un échec aux côtés du message d'erreur lui-même. Si un utilisateur saisit un montant invalide, la sortie d'erreur identifie clairement la valeur problématique.

### Mettre à jour l'enregistrement de la bibliothèque

Pour finaliser cette étape, enregistrez le module de sortie et exportez les nouveaux types de réponse dans votre fichier `src/lib.rs` :

```rust
pub mod commands;
pub mod error;
pub mod models;
pub mod output;
pub mod utils;

pub use error::*;
pub use models::*;
pub use utils::command_prelude;
pub use utils::context::GlobalContext;
pub use utils::parsers;
```

## Étape 7 : Création d'aides pour l'analyse des arguments

L'extraction de valeurs spécifiques comme les montants de transaction, les dates ou les catégories à partir d'une entrée brute de ligne de commande peut rapidement mener à du code répétitif. Bien que `clap` fournisse l'analyse de base, vous avez besoin d'un moyen simplifié pour convertir ces entrées dans les types spécifiques utilisés par votre gestionnaire. En créant un trait personnalisé pour étendre `clap`, vous gérez la conversion de type et le signalement d'erreurs en un seul endroit cohérent.

Créez un nouveau fichier nommé `src/utils/cli.rs` et ajoutez l'implémentation suivante :

```rust
use chrono::NaiveDate;
use clap::ArgMatches;
use crate::{Category, CliError, Currency};

const DEFAULT_F64: f64 = 0.0;
const DEFAULT_USIZE: usize = 0;
const DEFAULT_SUBCATEGORY: &str = "miscellaneous";

pub trait ArgMatchesExt {
    fn get_category(&self, id: &str) -> Result<&Category, CliError>;
    fn get_usize(&self, id: &str) -> Result<usize, CliError>;
    fn get_category_opt(&self, id: &str) -> Option<&Category>;
    fn get_f64_opt(&self, id: &str) -> Option<f64>;
    fn get_usize_opt(&self, id: &str) -> Option<usize>;
    fn get_string_opt(&self, id: &str) -> Option<String>;
    fn get_subcategory_opt(&self, id: &str) -> Option<String>;
    fn get_date_opt(&self, id: &str) -> Option<NaiveDate>;
    fn get_currency_opt(&self, id: &str) -> Option<&Currency>;
    fn get_f64_or_default(&self, id: &str) -> f64;
    fn get_usize_or_default(&self, id: &str) -> usize;
    fn get_string_or_default(&self, id: &str) -> String;
    fn get_subcategory_or_default(&self, id: &str) -> String;
    fn get_currency_or_default(&self, id: &str) -> &Currency;
    fn get_vec<T: Clone + Send + Sync + 'static>(&self, id: &str) -> Vec<T>;
    fn contains_id(&self, id: &str) -> bool;
}

impl ArgMatchesExt for ArgMatches {
    fn get_category(&self, id: &str) -> Result<&Category, CliError> {
        self.get_one::<Category>(id).ok_or_else(|| {
            CliError::ValidationError(crate::ValidationErrorKind::InvalidCategoryName {
                name: id.to_string(),
                reason: "Catégorie non fournie".to_string(),
            })
        })
    }

    fn get_usize(&self, id: &str) -> Result<usize, CliError> {
        self.get_one::<usize>(id).copied().ok_or_else(|| {
            CliError::Other(format!("Argument requis '{}' non fourni", id))
        })
    }

    fn get_category_opt(&self, id: &str) -> Option<&Category> {
        self.get_one::<Category>(id)
    }

    fn get_f64_opt(&self, id: &str) -> Option<f64> {
        self.get_one::<f64>(id).copied()
    }

    fn get_usize_opt(&self, id: &str) -> Option<usize> {
        self.get_one::<usize>(id).copied()
    }

    fn get_string_opt(&self, id: &str) -> Option<String> {
        self.get_one::<String>(id).cloned()
    }

    fn get_subcategory_opt(&self, id: &str) -> Option<String> {
        self.get_one::<String>(id).cloned()
    }

    fn get_date_opt(&self, id: &str) -> Option<NaiveDate> {
        self.get_one::<NaiveDate>(id).copied()
    }

    fn get_currency_opt(&self, id: &str) -> Option<&Currency> {
        self.get_one::<Currency>(id)
    }

    fn get_f64_or_default(&self, id: &str) -> f64 {
        self.get_one::<f64>(id).copied().unwrap_or(DEFAULT_F64)
    }

    fn get_usize_or_default(&self, id: &str) -> usize {
        self.get_one::<usize>(id).copied().unwrap_or(DEFAULT_USIZE)
    }

    fn get_string_or_default(&self, id: &str) -> String {
        self.get_one::<String>(id).cloned().unwrap_or_default()
    }

    fn get_subcategory_or_default(&self, id: &str) -> String {
        self.get_one::<String>(id)
            .cloned()
            .unwrap_or_else(|| DEFAULT_SUBCATEGORY.to_string())
    }

    fn get_currency_or_default(&self, id: &str) -> &Currency {
        self.get_one::<Currency>(id).unwrap_or(&Currency::NGN)
    }

    fn get_vec<T: Clone + Send + Sync + 'static>(&self, id: &str) -> Vec<T> {
        self.get_many::<T>(id)
            .map(|iter| iter.cloned().collect())
            .unwrap_or_default()
    }

    fn contains_id(&self, id: &str) -> bool {
        ArgMatches::contains_id(self, id)
    }
}
```

Ces méthodes d'aide vous permettent de décider exactement comment gérer les données manquantes. Des méthodes comme `ok_or_else` convertissent une entrée vide en une `CliError` spécifique qui informe l'utilisateur de l'argument manquant. En revanche, `unwrap_or_else` permet à l'application de fournir des solutions de repli raisonnables, comme l'utilisation par défaut de la sous-catégorie « miscellaneous » si l'utilisateur n'en spécifie pas.

### Implémenter des analyseurs de données personnalisés

Les arguments standard de la ligne de commande sont reçus sous forme de chaînes de caractères. Pour les transformer en types de données utiles comme des dates ou des catégories, vous avez besoin d'une logique d'analyse spécifique. Créez un nouveau fichier `src/utils/parsers.rs` :

```rust
use chrono::NaiveDate;
use crate::Category;

pub fn parse_date(s: &str) -> Result<NaiveDate, String> {
    NaiveDate::parse_from_str(s, "%d-%m-%Y")
        .map_err(|_| format!("'{}' n'est pas au format JJ-MM-AAAA", s))
}

pub fn parse_category(s: &str) -> Result<Category, String> {
    s.parse::<Category>().map_err(|_| {
        format!("'{}' n'est pas une catégorie valide. Utilisez 'income' ou 'expenses'", s)
    })
}
```

Nous utiliserons ces analyseurs pour nous assurer que toute entrée qui ne correspond pas au format attendu est immédiatement interceptée avec un message d'erreur clair avant même d'atteindre votre logique principale.

Pour finaliser cette configuration, mettez à jour `src/utils.rs` pour inclure les nouveaux fichiers d'aide :

```rust
pub mod cli;
pub mod command_prelude;
pub mod context;
pub mod file;
pub mod parsers;
```

Cette infrastructure garantit que lorsque vous commencerez à implémenter les commandes financières réelles, vous pourrez vous concentrer sur la logique métier au lieu de lutter avec les conversions de chaînes et la répétition de la validation des arguments.

Ensuite, nous commencerons à implémenter la logique métier des commandes, en commençant par la commande `init`.

## Étape 8 : Implémenter la commande Init

La commande `init` configurera l'espace de travail pour le gestionnaire financier. Elle gérera la création de la structure de répertoire caché dans votre dossier personnel et générera le fichier JSON initial avec les paramètres par défaut comme la devise et le solde de départ.

Créez le fichier `src/commands/init.rs` et ajoutez ce code :

```rust
use clap::{Arg, ArgMatches, Command};

use crate::command_prelude::ArgMatchesExt;
use crate::utils::file::{FilePath, write_json_to_file};
use crate::{CliResponse, CliResult, Currency, GlobalContext, default_tracker_json};

pub fn cli() -> Command {
    Command::new("init")
        .about("Initialiser un nouveau gestionnaire financier")
        .arg(
            Arg::new("currency")
                .short('c')
                .value_parser(clap::value_parser!(Currency))
                .default_value("ngn"),
        )
        .arg(
            Arg::new("opening")
                .short('o')
                .value_parser(clap::value_parser!(f64)),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let currency = args.get_currency_or_default("currency");
    let opening_balance = args.get_f64_or_default("opening");

    let mut file = gctx.tracker_path().create_file_if_not_exists()?;

    let default_json = default_tracker_json(currency, opening_balance);
    write_json_to_file(&default_json, &mut file)?;

    Ok(CliResponse::success())
}
```

La fonction `cli` définit l'interface de la commande. `Command::new("init")` définit le nom de la sous-commande que l'utilisateur tape. À l'intérieur des blocs `.arg()`, `.short('c')` et `.long("currency")` permettent deux manières différentes de fournir la même donnée. Un utilisateur peut choisir la forme courte concise ou la forme longue plus descriptive :

```bash
fintrack init -c usd -o 5000
```

OU

```bash
fintrack init --currency usd --opening 5000
```

Les deux commandes correspondent aux mêmes arguments internes `"currency"` et `"opening"`.

La fonction `exec` effectue l'initialisation réelle du gestionnaire. Elle utilise les aides construites dans les étapes précédentes pour garder la logique concise. Plus précisément, elle utilise `get_currency_or_default` et `get_f64_or_default` du trait `ArgMatchesExt` que vous avez créé dans `src/utils/cli.rs`.

Lors de la tentative de création du fichier du gestionnaire, elle appelle `create_file_if_not_exists`. Cette méthode appartient au trait `FilePath` que vous avez implémenté dans `src/utils/file.rs`. Parce que cette méthode a été construite en utilisant `create_new(true)`, elle agit comme une garde qui échoue si un gestionnaire existe déjà avec une erreur `std::io::ErrorKind::AlreadyExists`. Cet échec est capturé et converti en un message `CliError::FileAlreadyExists`, qui a été défini dans votre logique de gestion des erreurs dans `src/error.rs`.

La fonction `default_tracker_json` construit l'état initial de l'application. Elle empaquette la devise de base, le solde d'ouverture et la sous-catégorie par défaut « miscellaneous » dans une structure JSON. Enfin, l'aide `write_json_to_file` de `src/utils/file.rs` écrit ces données sur le disque.

## Étape 9 : Implémenter la commande Add

La commande `add` ajoutera un nouvel enregistrement. Pour ce faire, vous implémenterez un code qui lira les données existantes du fichier JSON, validera la nouvelle entrée et sauvegardera l'enregistrement mis à jour dans le fichier JSON.

Créez `src/commands/add.rs` et insérez ce code :

```rust
use chrono::Local;
use clap::{Arg, ArgMatches, Command};

use crate::command_prelude::ArgMatchesExt;
use crate::utils::file::{FilePath, write_json_to_file};
use crate::utils::parsers::{parse_category, parse_date};
use crate::{
    CliError, CliResponse, CliResult, GlobalContext, Record, ResponseContent, TrackerData,
};

pub fn cli() -> Command {
    Command::new("add")
        .about("Enregistrer une nouvelle transaction de revenu ou de dépense")
        .arg(
            Arg::new("category")
                .index(1)
                .required(true)
                .value_parser(parse_category),
        )
        .arg(
            Arg::new("amount")
                .index(2)
                .required(true)
                .value_parser(clap::value_parser!(f64)),
        )
        .arg(
            Arg::new("subcategory")
                .short('s')
                .long("subcategory")
                .default_value("miscellaneous"),
        )
        .arg(
            Arg::new("description")
                .short('d')
                .long("description"),
        )
        .arg(
            Arg::new("date")
                .short('D')
                .long("date")
                .value_parser(parse_date),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let category = args.get_category("category")?;
    let amount = args.get_f64_or_default("amount");

    if amount <= 0.0 {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::AmountTooSmall { amount },
        ));
    }

    let subcategory_name = args.get_subcategory_or_default("subcategory");
    let description = args.get_string_or_default("description");

    let category_str = category.to_string();
    let category_id = tracker_data.category_id(&category_str);

    let subcategory_id = tracker_data
        .subcategory_id(&subcategory_name)
        .ok_or_else(|| {
            CliError::ValidationError(crate::ValidationErrorKind::SubcategoryNotFound {
                name: subcategory_name,
            })
        })?;

    let date = args
        .get_date_opt("date")
        .map(|d| d.format("%d-%m-%Y").to_string())
        .unwrap_or_else(|| Local::now().format("%d-%m-%Y").to_string());

    let record_id = tracker_data.next_record_id;
    let record = Record {
        id: record_id,
        category: category_id,
        amount,
        subcategory: subcategory_id,
        description,
        date,
    };

    tracker_data.next_record_id += 1;
    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();
    tracker_data.push_record(record.clone());

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::new(ResponseContent::Record {
        record,
        tracker_data,
        is_update: false,
    }))
}
```

La fonction `cli` définit ici des arguments positionnels en utilisant `.index(1)` et `.index(2)`. Cela signifie que les utilisateurs peuvent fournir la catégorie et le montant sans drapeaux spécifiques. Un exemple d'utilisation ressemble à ceci :

```bash
fintrack add income 1500 -s salary -d "Monthly pay"
```

Dans cette commande, `"income"` correspond à la `"category"` et 1500 correspond au `"amount"`. La logique d'analyse de ces entrées utilise les fonctions `parse_category` et `parse_date` créées dans `src/utils/parsers.rs`.

La fonction `exec` ouvre ici le fichier de données avec `open_read_write` du trait `FilePath` (`src/utils/file.rs`) et extrait l'entrée utilisateur à l'aide du trait `ArgMatchesExt` (`src/utils/cli.rs`).

La logique de date gère l'entrée facultative via une chaîne de méthodes. `get_date_opt` renvoie une `Option`, de sorte que lorsqu'une date existe, `.map` la transforme dans le format de chaîne requis. Lorsqu'une date n'existe pas, `.unwrap_or_else` fournit la date système actuelle par défaut.

Une fois la structure `Record` remplie, le code met à jour l'état de `TrackerData` et sauvegarde le résultat à l'aide de l'aide `write_json_to_file`. La `CliResponse` finale contient les détails de l'enregistrement pour que le module de sortie dans `src/output.rs` les affiche.

## Étape 10 : Implémenter la commande List

La commande `list` fournira un moyen de visualiser et de filtrer les enregistrements. Cette logique implique le chargement du fichier de données, l'application de critères tels que des plages de dates ou des catégories, et le tri chronologique des résultats.

Créez `src/commands/list.rs` et ajoutez le code suivant :

```rust
use chrono::NaiveDate;
use clap::{Arg, ArgGroup, ArgMatches, Command};

use crate::command_prelude::ArgMatchesExt;
use crate::utils::file::FilePath;
use crate::utils::parsers::{parse_category, parse_date};
use crate::{CliResponse, CliResult, GlobalContext, Record, ResponseContent, TrackerData};

pub fn cli() -> Command {
    Command::new("list")
        .about("Visualiser et filtrer vos enregistrements de transactions")
        .arg(
            Arg::new("first")
                .short('f')
                .long("first")
                .value_parser(clap::value_parser!(usize)),
        )
        .arg(
            Arg::new("last")
                .short('l')
                .long("last")
                .value_parser(clap::value_parser!(usize)),
        )
        .group(
            ArgGroup::new("first_or_last")
                .args(["first", "last"])
                .multiple(false),
        )
        .arg(
            Arg::new("start")
                .short('S')
                .long("start")
                .value_parser(parse_date),
        )
        .arg(
            Arg::new("end")
                .short('E')
                .long("end")
                .value_parser(parse_date),
        )
        .arg(
            Arg::new("category")
                .short('c')
                .long("category")
                .value_parser(parse_category),
        )
        .arg(
            Arg::new("subcategory")
                .short('s')
                .long("subcategory"),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let file = gctx.tracker_path().open_read()?;
    let tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let start_date = args.get_date_opt("start");
    let end_date = args.get_date_opt("end");

    let category_filter = args
        .get_category_opt("category")
        .map(|cat| tracker_data.category_id(&cat.to_string()));

    let subcategory_filter = args
        .get_subcategory_opt("subcategory")
        .and_then(|name| tracker_data.subcategory_id(&name));

    let mut filtered_data: Vec<Record> = tracker_data
        .records
        .iter()
        .filter(|r| {
            let matches_category = category_filter
                .map(|expected_id| r.category == expected_id)
                .unwrap_or(true);

            let matches_subcategory = subcategory_filter
                .map(|expected_id| r.subcategory == expected_id)
                .unwrap_or(true);

            let matches_date = NaiveDate::parse_from_str(&r.date, "%d-%m-%Y")
                .map(|record_date| {
                    let after_start = start_date.map_or(true, |start| record_date >= start);
                    let before_end = end_date.map_or(true, |end| record_date <= end);
                    after_start && before_end
                })
                .unwrap_or(false);

            matches_category && matches_subcategory && matches_date
        })
        .cloned()
        .collect();

    filtered_data.sort_by(|a, b| {
        let date_a = NaiveDate::parse_from_str(&a.date, "%d-%m-%Y").unwrap_or(NaiveDate::MIN);
        let date_b = NaiveDate::parse_from_str(&b.date, "%d-%m-%Y").unwrap_or(NaiveDate::MIN);
        date_a.cmp(&date_b)
    });

    if args.contains_id("first") {
        let first = args.get_usize_or_default("first");
        if first > 0 {
            filtered_data.truncate(first);
        }
    } else if args.contains_id("last") {
        let last = args.get_usize_or_default("last");
        if last > 0 && filtered_data.len() > last {
            let start_idx = filtered_data.len() - last;
            filtered_data = filtered_data.into_iter().skip(start_idx).collect();
        }
    }

    Ok(CliResponse::new(ResponseContent::List {
        records: filtered_data,
        tracker_data,
    }))
}
```

La fonction `cli` utilise un `ArgGroup` nommé `"first_or_last"`. Cela garantit que l'utilisateur ne peut pas demander à la fois les N premiers et les N derniers enregistrements en même temps. La commande prend en charge plusieurs drapeaux de filtrage, ce qui permet à un utilisateur d'exécuter des requêtes telles que :

```bash
fintrack list -c expenses -S 01-01-2024 -E 31-01-2024
```

La commande ci-dessus filtre spécifiquement pour les « dépenses » au cours du mois de janvier 2024.

La fonction `exec` utilise `open_read` du trait `FilePath` (`src/utils/file.rs`) pour accéder au fichier du gestionnaire sans permissions d'écriture. La logique de filtrage utilise des méthodes comme `and_then` et `map_or` pour gérer les critères facultatifs. Par exemple, le filtre de date utilise `map_or(true, ...)` pour inclure un enregistrement si aucune date de début ou de fin spécifique n'a été fournie.

Le tri des enregistrements utilise `sort_by` pour comparer les dates des enregistrements. Étant donné que les dates sont stockées sous forme de chaînes dans le fichier JSON, elles sont temporairement analysées en objets `NaiveDate` pour une comparaison chronologique précise. Enfin, la fonction utilise `truncate` ou `skip` pour limiter les résultats en fonction des arguments `"first"` ou `"last"` avant de renvoyer un `ResponseContent::List` pour traitement par le module de sortie dans `src/output.rs`.

## Étape 11 : Implémenter la commande Update

La commande `update` permettra à l'utilisateur de modifier des champs spécifiques dans un enregistrement existant. Elle acceptera des arguments similaires à la commande `add` mais, contrairement à cette dernière, chaque argument sauf l'ID sera facultatif, permettant à l'utilisateur de ne changer que ce qui est nécessaire.

Créez `src/commands/update.rs` et ajoutez le code suivant :

```rust
use clap::{Arg, ArgMatches, Command};

use crate::command_prelude::ArgMatchesExt;
use crate::utils::file::{FilePath, write_json_to_file};
use crate::utils::parsers::{parse_category, parse_date};
use crate::{
    CliError, CliResponse, CliResult, GlobalContext, ResponseContent, TrackerData,
};

pub fn cli() -> Command {
    Command::new("update")
        .about("Modifier un enregistrement de transaction existant")
        .arg(
            Arg::new("record_id")
                .index(1)
                .required(true)
                .value_parser(clap::value_parser!(usize)),
        )
        .arg(
            Arg::new("category")
                .short('c')
                .long("category")
                .value_parser(parse_category),
        )
        .arg(
            Arg::new("amount")
                .short('a')
                .long("amount")
                .value_parser(clap::value_parser!(f64)),
        )
        .arg(
            Arg::new("subcategory")
                .short('s')
                .long("subcategory"),
        )
        .arg(
            Arg::new("description")
                .short('d')
                .long("description"),
        )
        .arg(
            Arg::new("date")
                .short('D')
                .long("date")
                .value_parser(parse_date),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let record_id = args
        .get_usize("record_id")
        .map_err(|_| CliError::ValidationError(crate::ValidationErrorKind::RecordNotFound { id: 0 }))?;

    let category_id = args.get_category_opt("category").map(|category| {
        let category_str = category.to_string();
        tracker_data.category_id(&category_str)
    });

    let subcategory_id = args
        .get_subcategory_opt("subcategory")
        .map(|name| {
            tracker_data.subcategory_id(&name).ok_or_else(|| {
                CliError::ValidationError(crate::ValidationErrorKind::SubcategoryNotFound { name })
            })
        })
        .transpose()?;

    let record = tracker_data
        .records
        .iter_mut()
        .find(|r| r.id == record_id)
        .ok_or_else(|| {
            CliError::ValidationError(crate::ValidationErrorKind::RecordNotFound { id: record_id })
        })?;

    if let Some(cat_id) = category_id {
        record.category = cat_id;
    }

    if let Some(amount) = args.get_f64_opt("amount") {
        if amount <= 0.0 {
            return Err(CliError::ValidationError(
                crate::ValidationErrorKind::AmountTooSmall { amount },
            ));
        }
        record.amount = amount;
    }

    if let Some(subcat_id) = subcategory_id {
        record.subcategory = subcat_id;
    }

    if let Some(description) = args.get_string_opt("description") {
        record.description = description;
    }

    if let Some(date) = args.get_date_opt("date") {
        record.date = date.format("%d-%m-%Y").to_string();
    }

    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();

    let updated_record = record.clone();

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::new(ResponseContent::Record {
        record: updated_record,
        tracker_data,
        is_update: true,
    }))
}
```

La fonction `cli` nécessite un `"record_id"` positionnel afin que le programme sache quel enregistrement cibler. Les utilisateurs peuvent trouver cet ID en exécutant la commande `list`. Une commande `update` ressemble à ceci :

```bash
fintrack update 5 -a 2000 -d "Updated price"
```

La commande ci-dessus met à jour spécifiquement le montant et la description de l'enregistrement numéro 5, laissant tous les autres champs inchangés.

La fonction `exec` utilise `iter_mut()` et `find()` pour localiser l'enregistrement spécifique dans votre liste de données. Comme `iter_mut()` fournit une référence mutable, tout changement apporté à la variable `record` met directement à jour l'objet à l'intérieur de `tracker_data.records`.

Pour gérer la mise à jour facultative de la sous-catégorie, le code utilise `transpose()`. Cette méthode est essentielle ici car la recherche d'un nom de sous-catégorie est facultative. Mais si un nom est fourni et qu'il n'existe pas, le programme doit s'arrêter et renvoyer une erreur. `transpose()` transforme l' `Option<Result>` en un `Result<Option>`, permettant à l'opérateur `?` de gérer l'erreur tout en vous donnant une `Option` avec laquelle travailler.

L'état final est sauvegardé dans le fichier à l'aide de l'aide `write_json_to_file` de `src/utils/file.rs`. La `CliResponse` indique qu'une mise à jour a eu lieu en définissant `is_update: true`, ce que le module `output` utilise pour formater le message de succès de manière appropriée.

## Étape 12 : Implémenter la commande Delete

La commande `delete` supprimera des enregistrements spécifiques du gestionnaire. Cette implémentation prendra en charge plusieurs stratégies de suppression : cibler des IDs individuels, supprimer une catégorie entière ou effacer une sous-catégorie spécifique.

```rust
use std::collections::HashSet;

use clap::{Arg, ArgAction, ArgGroup, ArgMatches, Command};

use crate::{
    CliResponse, CliResult, GlobalContext, TrackerData,
    command_prelude::ArgMatchesExt,
    utils::file::{FilePath, write_json_to_file},
    utils::parsers::parse_category,
};

pub fn cli() -> Command {
    Command::new("delete")
        .about("Supprimer des enregistrements de transactions")
        .arg(
            Arg::new("ids")
                .short('i')
                .long("ids")
                .value_parser(clap::value_parser!(usize))
                .action(ArgAction::Append)
                .value_delimiter(','),
        )
        .arg(
            Arg::new("by-cat")
                .short('c')
                .long("by-cat")
                .value_parser(parse_category),
        )
        .arg(
            Arg::new("by-subcat")
                .short('s')
                .long("by-subcat"),
        )
        .group(
            ArgGroup::new("delete_by")
                .args(["ids", "by-cat", "by-subcat"])
                .multiple(false)
                .required(true),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    if args.contains_id("ids") {
        let ids: Vec<usize> = args.get_vec::<usize>("ids");
        let ids_set: HashSet<usize> = ids.into_iter().collect();

        tracker_data.records.retain(|r| !ids_set.contains(&r.id));
    } else if args.contains_id("by-cat") {
        let category = args.get_category("by-cat")?;
        let category_str = category.to_string();
        let category_id = tracker_data.category_id(&category_str);

        tracker_data.records.retain(|r| r.category != category_id);
    } else if args.contains_id("by-subcat") {
        let subcategory_name = args
            .get_subcategory_opt("by-subcat")
            .ok_or_else(|| crate::CliError::Other("Sous-catégorie non fournie".to_string()))?;

        let subcategory_id = tracker_data
            .subcategory_id(subcategory_name.as_str())
            .ok_or_else(|| {
                crate::CliError::ValidationError(crate::ValidationErrorKind::SubcategoryNotFound {
                    name: subcategory_name.clone(),
                })
            })?;

        tracker_data
            .records
            .retain(|r| r.subcategory != subcategory_id);
    }

    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::success())
}
```

La fonction `cli` utilise un `ArgGroup` pour imposer qu'une seule méthode de suppression soit utilisée à la fois (`"ids"`, `"by-cat"` ou `"by-subcat"`). L'argument `"ids"` utilise `value_delimiter(',')`, permettant à un utilisateur de passer plusieurs IDs séparés par une virgule (','). Par exemple :

```bash
fintrack delete --ids 1,4,7
```

De plus, un utilisateur peut effacer tous les enregistrements d'une catégorie ou d'une sous-catégorie particulière en utilisant le drapeau `"by-cat"` ou `"by-subcat"`. Par exemple :

```bash
fintrack delete --by-cat expenses
```

La fonction `exec` détermine quels enregistrements cibler en fonction de trois entrées possibles. Si `--ids` est utilisé, elle collecte les valeurs fournies directement dans un `HashSet`. Si `--by-cat` ou `--by-subcat` est utilisé, le code parcourt les enregistrements existants et rassemble les IDs de chaque enregistrement correspondant à cette catégorie ou sous-catégorie spécifique et les stocke dans un `HashSet`. Quel que soit le drapeau utilisé, la logique converge vers un `HashSet` contenant tous les IDs prévus pour la suppression.

L'utilisation d'un `HashSet` rend le nettoyage final très efficace car il permet au programme de vérifier si un ID existe dans la « liste de suppression » presque instantanément. La méthode `retain` ne conserve alors que les enregistrements dont les IDs ne sont pas dans cet ensemble, élaguant ainsi efficacement les données sur place.

Après la suppression, le code met à jour l'horodatage `last_modified` et sauvegarde le JSON mis à jour à l'aide de l'aide `write_json_to_file` de `src/utils/file.rs`.

## Étape 13 : Implémenter les commandes de sous-catégorie

La commande `subcategory` servira de parent à plusieurs sous-commandes imbriquées, permettant aux utilisateurs d'organiser leurs enregistrements au-delà des catégories de base « income » et « expenses ». Cette structure utilisera une approche modulaire, où chaque tâche de gestion vivra dans son propre fichier dédié.

Créez le fichier de point d'entrée à `src/commands/subcategory.rs` :

```rust
use clap::{ArgMatches, Command};

use crate::{CliResult, GlobalContext, commands::Exec, invalid_subcommand_error};

pub fn cli() -> Command {
    Command::new("subcategory")
        .about("Gérer vos sous-catégories")
        .subcommand_required(true)
        .subcommands(build_cli())
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    match args.subcommand() {
        Some((cmd, sub_args)) => {
            let exec_fn = build_exec(cmd).ok_or_else(|| invalid_subcommand_error(cmd))?;

            exec_fn(gctx, sub_args)
        }
        None => Err(invalid_subcommand_error("")),
    }
}

fn build_cli() -> Vec<Command> {
    vec![add::cli(), delete::cli(), list::cli(), rename::cli()]
}

fn build_exec(cmd: &str) -> Option<Exec> {
    match cmd {
        "add" => Some(add::exec),
        "delete" => Some(delete::exec),
        "list" => Some(list::exec),
        "rename" => Some(rename::exec),
        "update" => Some(rename::exec),
        _ => None,
    }
}

pub mod list;
pub mod add;
pub mod delete;
pub mod rename;
```

La fonction `cli` définit ici `subcommand_required(true)`. Cela signifie que l'utilisateur doit spécifier une action. La fonction `exec` utilise une instruction `match` pour déléguer la logique au module approprié.

### Lister les sous-catégories

Créez `src/commands/subcategory/list.rs` :

```rust
use clap::{ArgMatches, Command};

use crate::{CliResponse, CliResult, GlobalContext, ResponseContent, TrackerData, utils::file::FilePath};

pub fn cli() -> Command {
    Command::new("list")
        .about("Voir toutes les sous-catégories disponibles")
}

pub fn exec(gctx: &mut GlobalContext, _args: &ArgMatches) -> CliResult {
    let file = gctx.tracker_path().open_read()?;
    let tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let mut subcategories: Vec<(usize, String)> = tracker_data
        .subcategories_by_id
        .iter()
        .map(|(&id, name)| (id, name.clone()))
        .collect();

    subcategories.sort_by_key(|(id, _)| *id);

    Ok(CliResponse::new(ResponseContent::Subcategories(subcategories)))
}
```

La fonction `exec` accède d'abord au fichier de données à l'aide de la méthode d'aide `open_read` définie précédemment dans `src/utils/file.rs`. Une fois le fichier ouvert, elle lit le contenu JSON dans la structure `TrackerData`. La logique extrait ensuite la liste spécifique des IDs et des noms de la carte `subcategories_by_id` trouvée dans `src/models.rs` et les convertit en une liste simple pour l'utilisateur.

### Ajouter des sous-catégories

Créez `src/commands/subcategory/add.rs` :

```rust
use clap::{Arg, ArgMatches, Command};

use crate::{
    CliError, CliResponse, CliResult, GlobalContext, TrackerData,
    utils::file::{FilePath, write_json_to_file},
    utils::parsers::parse_label,
};

pub fn cli() -> Command {
    Command::new("add")
        .about("Créer une nouvelle sous-catégorie")
        .arg(
            Arg::new("name")
                .index(1)
                .required(true)
                .value_parser(parse_label),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let name = args
        .get_one::<String>("name")
        .ok_or_else(|| CliError::Other("Nom de sous-catégorie non fourni".to_string()))?;

    let name_lower = name.to_lowercase();
    let name_title = {
        let mut chars = name_lower.chars();
        match chars.next() {
            None => return Err(CliError::Other("Nom invalide".to_string())),
            Some(first) => first.to_uppercase().collect::<String>() + &chars.as_str().to_lowercase(),
        }
    };

    if name_lower == "miscellaneous" {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::CannotDeleteMiscellaneous,
        ));
    }

    if tracker_data.subcategories_by_name.contains_key(&name_lower) {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::SubcategoryAlreadyExists {
                name: name_title.clone(),
            },
        ));
    }

    let subcategory_id = tracker_data.next_subcategory_id as usize;
    tracker_data.subcategories_by_id.insert(subcategory_id, name_title.clone());
    tracker_data.subcategories_by_name.insert(name_lower, subcategory_id);
    tracker_data.next_subcategory_id += 1;
    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::new(crate::ResponseContent::Message(format!(
        "Sous-catégorie '{}' ajoutée (ID : {})",
        name_title, subcategory_id
    ))))
}
```

La fonction `exec` utilise ici `open_read_write` pour charger les données en vue d'une modification. Elle récupère l'entrée de l'utilisateur via l'aide `get_string_opt` du trait `ArgMatchesExt`.

Pour maintenir la cohérence, la fonction de normalisation garantit que tous les noms suivent un format standard de casse de titre. Avant de sauvegarder, la logique vérifie la carte `subcategories_by_name` de `src/models.rs` pour s'assurer que le nom est unique.

Une fois validée, elle met à jour `next_subcategory_id` et écrit les modifications sur le disque à l'aide de `write_json_to_file`.

### Supprimer des sous-catégories

Créez `src/commands/subcategory/delete.rs` :

```rust
use clap::{Arg, ArgMatches, Command};

use crate::{
    CliError, CliResponse, CliResult, GlobalContext, TrackerData,
    utils::file::{FilePath, write_json_to_file},
    utils::parsers::parse_label,
};

pub fn cli() -> Command {
    Command::new("delete")
        .about("Supprimer une sous-catégorie")
        .arg(
            Arg::new("name")
                .index(1)
                .required(true)
                .value_parser(parse_label),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let name = args
        .get_one::<String>("name")
        .ok_or_else(|| CliError::Other("Nom de sous-catégorie non fourni".to_string()))?;

    let name_lower = name.to_lowercase();

    if name_lower == "miscellaneous" {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::CannotDeleteMiscellaneous,
        ));
    }

    let subcategory_id = tracker_data
        .subcategory_id(&name_lower)
        .ok_or_else(|| {
            CliError::ValidationError(crate::ValidationErrorKind::SubcategoryNotFound {
                name: name.to_string(),
            })
        })?;

    let record_count = tracker_data
        .records
        .iter()
        .filter(|r| r.subcategory == subcategory_id)
        .count();

    if record_count > 0 {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::SubcategoryHasRecords {
                name: name.to_string(),
                count: record_count,
            },
        ));
    }

    tracker_data.subcategories_by_id.remove(&subcategory_id);
    tracker_data.subcategories_by_name.remove(&name_lower);
    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::new(crate::ResponseContent::Message(format!(
        "Sous-catégorie '{}' supprimée",
        name
    ))))
}
```

La fonction `exec` effectue une vérification de sécurité avant de supprimer toute donnée. Elle localise d'abord l'ID de la sous-catégorie cible en utilisant le nom fourni par l'utilisateur. Ensuite, elle parcourt le vecteur des enregistrements dans les données du gestionnaire pour compter si des enregistrements sont actuellement liés à cet ID. Si le compte est supérieur à zéro, l'opération s'arrête et renvoie une erreur `SubcategoryHasRecords`, vous empêchant de créer accidentellement des enregistrements « orphelins » qui pointent vers une sous-catégorie manquante. Si la vérification passe, la sous-catégorie est supprimée des deux `HashMaps` dans `src/models.rs`.

### Renommer des sous-catégories

Créez `src/commands/subcategory/rename.rs` :

```rust
use clap::{Arg, ArgMatches, Command};

use crate::{
    CliError, CliResponse, CliResult, GlobalContext, TrackerData,
    utils::file::{FilePath, write_json_to_file},
    utils::parsers::parse_label,
};

pub fn cli() -> Command {
    Command::new("rename")
        .about("Renommer une sous-catégorie existante")
        .arg(
            Arg::new("old")
                .index(1)
                .required(true)
                .value_parser(parse_label),
        )
        .arg(
            Arg::new("new")
                .index(2)
                .required(true)
                .value_parser(parse_label),
        )
}

pub fn exec(gctx: &mut GlobalContext, args: &ArgMatches) -> CliResult {
    let mut file = gctx.tracker_path().open_read_write()?;
    let mut tracker_data: TrackerData = serde_json::from_reader(&file)?;

    let old_name = args
        .get_one::<String>("old")
        .ok_or_else(|| CliError::Other("Ancien nom de sous-catégorie non fourni".to_string()))?;
    let new_name = args
        .get_one::<String>("new")
        .ok_or_else(|| CliError::Other("Nouveau nom de sous-catégorie non fourni".to_string()))?;

    let old_name_lower = old_name.to_lowercase();
    let new_name_lower = new_name.to_lowercase();
    let new_name_title = {
        let mut chars = new_name_lower.chars();
        match chars.next() {
            None => return Err(CliError::Other("Nouveau nom invalide".to_string())),
            Some(first) => first.to_uppercase().collect::<String>() + &chars.as_str().to_lowercase(),
        }
    };

    let subcategory_id = tracker_data
        .subcategory_id(&old_name_lower)
        .ok_or_else(|| {
            CliError::ValidationError(crate::ValidationErrorKind::SubcategoryNotFound {
                name: old_name.to_string(),
            })
        })?;

    if tracker_data.subcategories_by_name.contains_key(&new_name_lower) {
        return Err(CliError::ValidationError(
            crate::ValidationErrorKind::SubcategoryAlreadyExists {
                name: new_name_title.clone(),
            },
        ));
    }

    tracker_data
        .subcategories_by_id
        .insert(subcategory_id, new_name_title.clone());
    tracker_data.subcategories_by_name.remove(&old_name_lower);
    tracker_data
        .subcategories_by_name
        .insert(new_name_lower, subcategory_id);
    tracker_data.last_modified = chrono::Utc::now().to_rfc3339();

    let tracker_json = serde_json::json!(tracker_data);
    write_json_to_file(&tracker_json, &mut file)?;

    Ok(CliResponse::new(crate::ResponseContent::Message(format!(
        "Sous-catégorie renommée : '{}' → '{}'",
        old_name, new_name_title
    ))))
}
```

La fonction `exec` implémente une logique de « permutation » pour préserver l'historique des enregistrements. Elle trouve d'abord l'ID numérique associé au nom actuel. Au lieu de modifier chaque enregistrement individuel, elle supprime simplement l'ancien nom de la `HashMap` `subcategories_by_name` et insère le nouveau nom avec le même ID. Cela garantit que tous les enregistrements existants dans `src/models.rs` reflètent immédiatement le nouveau nom car ils référencent la sous-catégorie par ID plutôt que par une chaîne de caractères.

## Étape 14 : Implémenter la commande Total

La commande `total` agrégera chaque enregistrement de transaction dans votre fichier JSON pour fournir une vue claire de la situation de votre grand livre. Elle additionnera tous les revenus et dépenses pour vous montrer exactement comment votre solde a changé depuis que vous avez initialisé le gestionnaire.

Créez `src/commands/total.rs` et ajoutez le code suivant :

```rust
use clap::{ArgMatches, Command};

use crate::{
    CliError, CliResponse, CliResult, Currency, GlobalContext, Total, TrackerData,
    utils::file::FilePath,
};

pub fn cli() -> Command {
    Command::new("total")
        .about("Afficher le résumé financier avec les totaux")
}


pub fn exec(gctx: &mut GlobalContext, _args: &ArgMatches) -> CliResult {
  let file = gctx.tracker_path().open_read()?;
  let tracker_data: TrackerData = serde_json::from_reader(&file)?;

  let opening_balance = tracker_data.opening_balance;

  let currency = tracker_data
    .currency
    .parse::<Currency>()
    .map_err(|e| CliError::Other(format!("Devise invalide dans les données du gestionnaire : {}", e)))?;

  let (income_total, expenses_total) = tracker_data.totals();

  Ok(CliResponse::new(crate::ResponseContent::Total(Total {
    currency,
    opening_balance,
    income_total,
    expenses_total,
  })))
}
```

La fonction `cli` définit une interface simple sans drapeaux supplémentaires. Elle se concentre entièrement sur le traitement de l'ensemble complet des données.

La fonction `exec` accède d'abord au fichier de données à l'aide de l'aide `open_read`. Après avoir analysé le JSON dans la structure `TrackerData`, la logique appelle la méthode `totals()` que vous avez implémentée dans `src/models.rs`. Cette méthode parcourt vos enregistrements pour renvoyer les sommes brutes de tous les revenus et dépenses.

La structure `Total` contient le solde d'ouverture, le total des revenus et le total des dépenses. Le solde net est calculé dans le module de sortie en ajoutant `income_total` au `opening_balance` et en soustrayant `expenses_total`. Enfin, vous renvoyez une `CliResponse` qui permet au module de sortie de prendre ces chiffres bruts et de les afficher dans le terminal.

## Étape 15 : Assemblage de la fonction principale

Cette étape ramène chaque module séparé à la source. Jusqu'à présent, les modèles, la gestion des erreurs et la logique des commandes existaient en tant que parties isolées. Vous allez maintenant créer le fichier `main.rs` pour établir le point d'entrée central qui connecte ces pièces, permettant à l'application de fonctionner comme un binaire unifié.

Tout d'abord, mettez à jour `src/lib.rs` pour exposer les modules internes :

```rust
pub mod commands;
pub mod error;
pub mod models;
pub mod output;
pub mod utils;

pub use error::*;
pub use models::*;
pub use utils::command_prelude;
pub use utils::context::GlobalContext;
pub use utils::parsers;
```

Ensuite, créez `src/main.rs` :

```rust
use std::io;

use clap::Command;
use fintrack::{GlobalContext, commands};

fn main() {
    let exit_code = match run() {
        Ok(_) => 0,
        Err(e) => {
            eprintln!("Erreur : {}", e);
            1
        }
    };
    std::process::exit(exit_code);
}

fn run() -> Result<(), String> {
    let home_dir = dirs::home_dir()
        .ok_or_else(|| "Échec de la détermination du répertoire personnel".to_string())?;

    let mut gctx = GlobalContext::new(home_dir);

    let matches = Command::new("fintrack")
        .bin_name("fintrack")
        .about("Un gestionnaire financier CLI local-first pour gérer les revenus et les dépenses")
        .version(env!("CARGO_PKG_VERSION"))
        .subcommand_required(true)
        .subcommands(commands::cli())
        .get_matches();

    let (cmd, args) = matches
        .subcommand()
        .expect("sous-commande requise mais non trouvée");

    let exec_fn = commands::build_exec(cmd)
        .ok_or_else(|| format!("Commande inconnue : {}", cmd))?;

    let exec_result = exec_fn(&mut gctx, args);
    process_result(&exec_result).expect("Une erreur est survenue lors de l'affichage de la réponse");

    Ok(())
}

fn process_result(result: &fintrack::CliResult) -> io::Result<()> {
    match result {
        Ok(res) => res.write_to(&mut std::io::stdout()),
        Err(err) => err.write_to(&mut std::io::stderr()),
    }
}
```

La fonction `main` sert de superviseur pour l'ensemble du processus. Elle déclenche la fonction `run` et mappe le résultat final à un code de sortie système standard. Cela informe le terminal si l'opération a réussi ou a rencontré un échec.

La fonction `run` initie un cycle complet à travers l'architecture que vous avez construite dans les étapes précédentes. Elle commence par déterminer le répertoire personnel de l'utilisateur et le transmet à `GlobalContext::new(home_dir)`. Cette instanciation crée l'objet `gctx` de l'étape 5, qui détermine les chemins multiplateformes pour le dossier `.fintrack` et le fichier `tracker.json`.

Lorsqu'un utilisateur tape une commande comme `fintrack add` dans le terminal, le processus commence par appeler `commands::cli()`. Cette fonction, que vous avez définie dans votre répartiteur central `src/commands.rs` à l'étape 5, collecte la liste de toutes les sous-commandes disponibles (`init`, `add`, `list`, etc.). Elle rassemble la configuration spécifique de chaque commande dans une seule instance `clap` afin que le terminal puisse comprendre l'intention de l'utilisateur.

Si l'utilisateur fournit les entrées et arguments corrects et que la validation de `clap` est réussie, elle appelle `commands::build_exec(cmd)` qui utilise la logique de filtrage par motif également définie à l'étape 5. Cette fonction renvoie un pointeur vers la fonction `exec` spécifique pour cette commande. Par exemple, si l'utilisateur a tapé `fintrack add ...`, elle récupère la fonction `exec` de `src/commands/add.rs`. Le code exécute ensuite cette fonction en utilisant une référence mutable au `gctx` que vous venez d'instancier. Cela accorde à la commande l'accès aux chemins de fichiers et aux données dont elle a besoin.

La phase d'exécution finale se déroule dans `process_result`. Cette fonction prend le `CliResult` renvoyé par la commande et appelle la méthode `write_to` que vous avez définie précédemment dans la logique de sortie de l'étape 6. Fournir des références mutables à `std::io::stdout()` pour les succès ou `std::io::stderr()` pour les erreurs garantit que l'application imprime le résultat ou le message d'erreur dans le terminal.

## Tester votre application

Vous pouvez construire et tester votre application en utilisant `cargo run`. Le double tiret `--` indique à Cargo de transmettre les drapeaux suivants directement à votre binaire `fintrack` plutôt que de les interpréter comme des arguments Cargo :

```bash
cargo build
cargo run -- init --currency USD --opening 1000
cargo run -- add income 500 --subcategory salary
cargo run -- add expenses 50 --subcategory groceries
cargo run -- list
cargo run -- total
```

### Installer le binaire

L'exécution avec `cargo run` est utile pendant le développement, mais vous pouvez installer le binaire directement sur votre système pour utiliser la commande `fintrack` globalement. Elle utilisera `fintrack` car c'est la valeur du champ `name` dans votre fichier `Cargo.toml`, que vous avez définie à la première étape lors de l'exécution de `cargo new fintrack`.

Exécutez ceci pour installer `fintrack` en tant que commande :

```bash
cargo install --path .
```

Lorsque vous exécutez la commande d'installation, Cargo compile votre code en mode release et place l'exécutable dans votre dossier bin Cargo (généralement `~/.cargo/bin`). Une fois installé, le système d'exploitation reconnaît `fintrack` comme une commande autonome. Vous pouvez maintenant appeler votre application depuis n'importe quel répertoire sans la préfixer par `cargo` :

```bash
fintrack total
```

## Et après et fonctionnalités avancées

Félicitations ! Vous avez construit un gestionnaire financier CLI local-first complet. L'application que vous avez créée comprend :

* La persistance des données au format JSON
    
* Les opérations CRUD complètes pour les enregistrements financiers
    
* La gestion des sous-catégories
    
* Des calculs financiers
    
* Une gestion complète des erreurs
    
* Une analyse des arguments de ligne de commande de type sécurisé
    

### Fonctionnalités avancées à explorer

L'architecture modulaire que vous avez construite rend cet outil facilement extensible. Pour ajouter de nouvelles commandes, il vous suffit de suivre le modèle établi dans les étapes précédentes : créer un nouveau module de commande, définir sa logique et l'enregistrer dans les fonctions `cli()` et `build_exec` de `src/commands.rs`.

Envisagez d'implémenter ces fonctionnalités pour améliorer l'outil :

* **Export** : Ajoutez un module `export.rs` pour convertir vos données JSON au format CSV pour analyse dans des tableurs.
    
* **Describe** : Créez une commande qui utilise des bibliothèques de graphiques de terminal pour générer des graphiques visuels de vos habitudes de dépenses.
    
* **Formatage de sortie amélioré** : Mettez à jour `src/output.rs` avec des bibliothèques comme `colored` ou `tabled` pour ajouter des couleurs et des bordures professionnelles à vos résumés de terminal.
    

Vous pouvez trouver l'implémentation complète de `fintrack` avec toutes les fonctionnalités, y compris le formatage de sortie avancé, la fonctionnalité d'exportation et plus encore, dans le [dépôt GitHub](https://github.com/steph-crown/fintrack). Le dépôt comprend également des instructions d'installation pour télécharger le binaire ou l'installer via Cargo.

## Conclusion

Dans ce tutoriel, vous avez appris à :

* Structurer une application CLI Rust avec une gestion appropriée des erreurs
    
* Utiliser des traits pour étendre les fonctionnalités
    
* Travailler avec la sérialisation JSON
    
* Analyser et valider les arguments de ligne de commande
    
* Gérer les opérations d'E/S de fichiers
    
* Implémenter un modèle de données complet avec des relations
    

Les modèles que vous avez appris ici s'appliquent à de nombreuses applications Rust. Les traits, la gestion des erreurs avec `Result` et le système de propriété sont fondamentaux pour écrire du code Rust idiomatique. Ces techniques garantissent qu'à mesure que l'application grandit, le code reste maintenable et sûr.

La nature modulaire de ce gestionnaire signifie également que le code source est désormais un modèle pour tout outil local-first. En remplaçant les modèles financiers par d'autres types de données, cette même architecture peut alimenter un gestionnaire de tâches, un wiki personnel ou un suivi du temps.

Continuez à construire, et bon suivi !