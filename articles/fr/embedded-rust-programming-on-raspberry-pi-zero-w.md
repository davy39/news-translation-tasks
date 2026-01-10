---
title: Programmation Rust embarquée sur Raspberry Pi Zero W
subtitle: ''
author: Shaun Hamilton
co_authors: []
series: null
date: '2022-06-09T15:37:48.000Z'
originalURL: https://freecodecamp.org/news/embedded-rust-programming-on-raspberry-pi-zero-w
coverImage: https://www.freecodecamp.org/news/content/images/2022/06/rpi-rust.png
tags:
- name: embedded systems
  slug: embedded-systems
- name: Raspberry Pi
  slug: raspberry-pi
- name: Rust
  slug: rust
seo_title: Programmation Rust embarquée sur Raspberry Pi Zero W
seo_desc: "Embedded programming in Rust requires a whole new knowledge base. Using\
  \ a Raspberry Pi Zero W, you can quickly get up and running with embedded Rust.\
  \ \nStarting with an embedded \"Hello World\" equivalent, and advancing to a text-to-morse-code\
  \ translato..."
---

La programmation embarquée en Rust nécessite une toute nouvelle base de connaissances. En utilisant un Raspberry Pi Zero W, vous pouvez rapidement démarrer avec Rust embarqué. 

En commençant par un équivalent embarqué de "Hello World", et en progressant vers un traducteur de texte en code Morse, cet article vous guidera à travers le processus.

- [Comment installer le Pi](#heading-comment-installer-le-pi)
  - [Formater la carte SD](#heading-formater-la-carte-sd)
  - [Flashing de la distribution](#heading-flashing-de-la-distribution)
    - [Configurer le Wifi et SSH](#heading-configurer-le-wifi-et-ssh)
  - [Compléter le circuit](#heading-completer-le-circuit)
- [Comment configurer la compilation croisée](#heading-comment-configurer-la-compilation-croisee)
  - [Installer la cible](#heading-installer-la-cible)
  - [Spécifier le linker](#heading-specifier-le-linker)
- [Comment programmer un "Hello World" embarqué](#heading-comment-programmer-un-hello-world-embarque)
  - [Quitter le programme avec succès](#heading-quitter-le-programme-avec-succes)
- [Comment compiler le programme en cross-compilation](#heading-comment-compiler-le-programme-en-cross-compilation)
- [Comment transférer le binaire vers le Pi](#heading-comment-transférer-le-binaire-vers-le-pi)
- [Comment se connecter en SSH au Pi](#heading-comment-se-connecter-en-ssh-au-pi)
  - [Exécuter le programme](#heading-executer-le-programme)
- [Comment coder un traducteur de texte en code Morse](#heading-comment-coder-un-traducteur-de-texte-en-code-morse)
- [Annexe](#heading-annexe)
  - [Cibles](#heading-cibles)

## Comment installer le Pi

### Formater la carte SD

Utilisez Raspberry Pi Imager qui peut être téléchargé depuis la [page Web des logiciels Raspberry Pi](https://www.raspberrypi.com/software/).

![rpi-imager](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager.png)

### Flashing de la distribution

Une distribution que je suggère est [Raspberry Pi OS Lite](https://www.raspberrypi.com/software/operating-systems/). Il s'agit d'une distribution _headless_, ce qui signifie qu'elle ne dispose pas d'une interface graphique.

![rpi-imager-os](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager-os.png)

#### Configurer le Wifi et SSH

![rpi-imager-ssh](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager-ssh.png)

Une fois cela fait, vous pouvez insérer la carte SD dans le Raspberry Pi et le mettre sous tension.

### Compléter le circuit

**Schéma du circuit**

![rpi-circuit](https://www.freecodecamp.org/news/content/images/2022/06/rpi-circuit.png)

**Brochage du Pi**

Connectez le négatif à la masse et le positif à la broche BCM 17 comme indiqué ci-dessous :

![rpi-pinout](https://www.freecodecamp.org/news/content/images/2022/06/rpi-pinout.png)

Le brochage peut être vu ici : https://pinout.xyz/

![IMG_3418-1-](https://www.freecodecamp.org/news/content/images/2022/06/IMG_3418-1-.JPG)

## Comment configurer la compilation croisée

### Installer la cible

Utilisez `rustup` pour installer la cible nécessaire pour votre Raspberry Pi :

```bash
my-pc$ rustup add target arm-unknown-linux-gnueabihf
```

[Annexe](#heading-cibles) pour plus d'informations sur les cibles dans Rust.

### Spécifier le linker

Téléchargez le dépôt `raspberrypi/tools` dans un répertoire nommé `rpi_tools` :

```bash
my-pc:~ $ git clone https://github.com/raspberrypi/tools $HOME/rpi_tools
```

Éditez le fichier `~/.cargo/config` en utilisant votre éditeur de texte préféré :

```bash
my_pc:~ $ sudo nano ~/.cargo/config
```

Indiquez à Cargo d'utiliser une version spécifique du linker pour votre cible :

```conf
[target.arm-unknown-linux-gnueabihf]
linker = "/rpi_tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc"
```

## Comment programmer un "Hello World" embarqué

Commencez par créer un nouveau projet Rust et ouvrez le fichier `main.rs` dans votre éditeur de texte préféré :

```bash
my-pc:~ $ cargo new blink
my-pc:~ $ cd blink
my-pc:~/blink $ nano src/main.rs
```

Importez la crate `rust_gpiozero` et programmez une LED pour qu'elle alterne entre allumée et éteinte toutes les secondes :

```rust
use rust_gpiozero::*;

fn main() {
    // Créez une nouvelle LED attachée à la broche 17
    let mut led = LED::new(17);

    led.blink(1.0, 1.0);

    led.wait();
}
```

Assurez-vous d'ajouter la dépendance au fichier `Cargo.toml` :

```toml
[dependencies]
rust-gpiozero = "0.2.1"
```

### Quitter le programme avec succès

Depuis `rustc 1.61.0` <sup>[[1]]</sup>, vous pouvez utiliser la structure `std::process::ExitCode` pour spécifier le code de statut retourné au parent du processus :

```rust
use std::process::ExitCode;
fn main() -> ExitCode {
    // ...
    if error {
      return ExitCode::from(1);
    }
    ExitCode::SUCCESS
}
```

Sinon, vous pouvez simplement retourner un `Result` :

```rust
fn main() -> Result<(), std::io::Error> {
  // ...
  Ok(())
}
```

## Comment compiler le programme en cross-compilation

Construisez une version de votre programme, en ciblant l'architecture requise :

```bash
my-pc:~/blink $ cargo build --release --target=arm-unknown-linux-gnueabihf
```

## Comment transférer le binaire vers le Pi

Utilisez `scp` pour transférer le binaire compilé de votre ordinateur hôte vers le Raspberry Pi via SSH :

```bash
my-pc:~/blink $ scp target/arm-unknown-linux-gnueabihf/release/blink pi@192.168.1.199:~/blink
```

**Note :** L'IP locale de votre Pi sera probablement différente.

## Comment se connecter en SSH au Pi

Connectez-vous en SSH au Raspberry Pi via son adresse IP locale :

```bash
my-pc:~ $ ssh pi@192.168.1.199
```

### Exécuter le programme

Depuis le Raspberry Pi, exécutez le binaire compilé :

```bash
pi:~ $ ./blink
```

## Comment coder un traducteur de texte en code Morse

Voici un exemple d'application qui lit l'entrée standard ligne par ligne, traduit l'entrée en code Morse et fait clignoter la LED en fonction du code Morse des caractères.

```rust
use rust_gpiozero::*;
use std::io::{BufRead, self};
use std::collections::HashMap;
use std::thread::sleep;
use std::time::Duration;

fn main() -> Result<(), std::io::Error> {
    println!("Démarrage...\n- Tapez du texte pour le convertir en code Morse\n- Tapez `quit()` pour quitter\n");
    // Créez une nouvelle LED attachée à la broche 17
    let led = LED::new(17);

    /// Durée d'un point en millisecondes
    const DOT_DELAY: u64 = 80;
    /// Durée d'un trait en millisecondes
    const DASH_DELAY: u64 = DOT_DELAY * 3;
    /// Délai entre les entrées en millisecondes
    const PUSH_DELAY: u64 = DOT_DELAY;
    /// Délai entre les lettres en millisecondes
    const LETTER_DELAY: u64 = DOT_DELAY * 3;
    /// Délai entre les mots en millisecondes
    const WORD_DELAY: u64 = DOT_DELAY * 7;

    let morse_code_alphabet: HashMap<char, &'static str> =
    [
        ('a', ".-"),
        ('b', "-..."),
        ('c', "-.-."),
        ('d', "-.."),
        ('e', "."),
        ('f', "..-."),
        ('g', "--."),
        ('h', "...."),
        ('i', ".."),
        ('j', ".---"),
        ('k', "-.-"),
        ('l', ".-.."),
        ('m', "--"),
        ('n', "-."),
        ('o', "---"),
        ('p', ".--."),
        ('q', "--.-"),
        ('r', ".-."),
        ('s', "..."),
        ('t', "-"),
        ('u', "..-"),
        ('v', "...-"),
        ('w', ".--"),
        ('x', "-..-"),
        ('y', "-.--"),
        ('z', "--.."),
        ('1', ".----"),
        ('2', "..---"),
        ('3', "...--"),
        ('4', "....-"),
        ('5', "....."),
        ('6', "-...."),
        ('7', "--..."),
        ('8', "---.."),
        ('9', "----."),
        ('0', "-----"),
        ('.', ".-.-.-"),
        (',', "--..--"),
        ('?', "..--.."),
        ('\'', ".----."),
        ('!', "-.-.--"),
        ('/', "-..-."),
        ('(', "-.--."),
        (')', "-.--.-"),
        ('&', ".-..."),
        (':', "---..."),
        (';', "-.-.-."),
        ('=', "-...-"),
        ('+', ".-.-."),
        ('-', "-....-"),
        ('_', "..--.-"),
        ('"', ".-..-."),
        ('$', "...-..-"),
        ('@', ".--.-."),
        (' ', " "),
    ].iter().cloned().collect();

    // Lire l'entrée standard ligne par ligne
    for line_res in io::stdin().lock().lines() {
        let line = line_res?;
        if line == "quit()" {
            break;
        }
        // Transformer la ligne en code Morse
        let mut morse = String::new();
        for c in line.chars() {
            if let Some(morse_code_char) = morse_code_alphabet.get(&c) {
                morse.push_str(morse_code_char);
                // Séparer les caractères avec une virgule
                morse.push_str(",");
            }
        }
        // Faire clignoter la LED en fonction des caractères
        for c in morse.chars() {
            match c {
                '.' => {
                    led.on();
                    sleep(Duration::from_millis(DOT_DELAY));
                    led.off();
                    sleep(Duration::from_millis(PUSH_DELAY));
                },
                '-' => {
                    led.on();
                    sleep(Duration::from_millis(DASH_DELAY));
                    led.off();
                    sleep(Duration::from_millis(PUSH_DELAY));
                },
                ',' => {
                    sleep(Duration::from_millis(LETTER_DELAY));
                },
                ' ' => {
                    sleep(Duration::from_millis(WORD_DELAY));
                },
                _ => {
                    println!("Caractère inconnu : {}", c);
                    break;
                }
            }
        }
        sleep(Duration::from_millis(WORD_DELAY));
    }

    // Libérer la variable et les ressources associées
    led.close();

    Ok(())
}
```

## Annexe

### Cibles

Dans Rust, la _cible_ est la plateforme (architecture) pour laquelle le programme est compilé. Cargo détecte automatiquement la cible, en fonction de la structure du système de fichiers <sup>[[2]]</sup>.

Vous pouvez voir la liste des cibles intégrées en exécutant :

```bash
rustc --print target-list
# OU
rustup target list
```

À partir de là, vous pouvez ajouter une nouvelle cible à votre projet en exécutant :

```bash
rustup target add <cible>
```

La cible donnée est souvent sous la forme d'un _triplet_ <sup>[[3]]</sup> :

- L'architecture
- Le fournisseur
- Le type de système d'exploitation
- Le type d'environnement

_Cela est appelé un 'triplet de cible', car la quatrième partie est optionnelle._

[1]: https://doc.rust-lang.org/stable/std/process/struct.ExitCode.html
[2]: https://doc.rust-lang.org/cargo/reference/cargo-targets.html#target-auto-discovery
[3]: https://rust-lang.github.io/rfcs/0131-target-specification.html