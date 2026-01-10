---
title: Embedded Rust Programming on Raspberry Pi Zero W
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
seo_title: null
seo_desc: "Embedded programming in Rust requires a whole new knowledge base. Using\
  \ a Raspberry Pi Zero W, you can quickly get up and running with embedded Rust.\
  \ \nStarting with an embedded \"Hello World\" equivalent, and advancing to a text-to-morse-code\
  \ translato..."
---

Embedded programming in Rust requires a whole new knowledge base. Using a Raspberry Pi Zero W, you can quickly get up and running with embedded Rust. 

Starting with an embedded _"Hello World"_ equivalent, and advancing to a text-to-morse-code translator, this article will walk you through the process.

- [How to Set Up the Pi](#heading-how-to-set-up-the-pi)
  - [Format the SD Card](#heading-format-the-sd-card)
  - [Flash the Distribution](#heading-flash-the-distribution)
    - [Configure Wifi and SSH](#heading-configure-wifi-and-ssh)
  - [Complete the Circuit](#heading-complete-the-circuit)
- [How to Set Up Cross Compilation](#heading-how-to-set-up-cross-compilation)
  - [Install the Target](#heading-install-the-target)
  - [Specify the Linker](#heading-specify-the-linker)
- [How to Program an Embedded "Hello World"](#heading-how-to-program-an-embedded-hello-world)
  - [Successfully Exit the Program](#heading-successfully-exit-the-program)
- [How to Cross Compile the Program](#heading-how-to-cross-compile-the-program)
- [How to Transfer the Binary to the Pi](#heading-how-to-transfer-the-binary-to-the-pi)
- [How to SSH into the Pi](#heading-how-to-ssh-into-the-pi)
  - [Run the Program](#heading-run-the-program)
- [How to Code a Text-to-Morse-Code Translator](#heading-how-to-code-a-text-to-morse-code-translator)
- [Appendix](#heading-appendix)
  - [Targets](#heading-targets-1)

## How to Set Up the Pi

### Format the SD Card

Use the Raspberry Pi Imager which can be downloaded from the [Raspberry Pi Software Webpage](https://www.raspberrypi.com/software/).

![rpi-imager](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager.png)

### Flash the Distribution

A distribution I'd suggest is [Raspberry Pi OS Lite](https://www.raspberrypi.com/software/operating-systems/). This is a _headless_ distribution, which means it does not come with a GUI.

![rpi-imager-os](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager-os.png)

#### Configure Wifi and SSH

![rpi-imager-ssh](https://www.freecodecamp.org/news/content/images/2022/06/rpi-imager-ssh.png)

Once that is done, you can insert the SD card into the Raspberry Pi, and power it up.

### Complete the Circuit

**Circuit Diagram**

![rpi-circuit](https://www.freecodecamp.org/news/content/images/2022/06/rpi-circuit.png)

**Pi Pinout**

Connect negative to ground, and positive to BCM pin 17 as shown below:

![rpi-pinout](https://www.freecodecamp.org/news/content/images/2022/06/rpi-pinout.png)

The pinout can be seen here: https://pinout.xyz/

![IMG_3418-1-](https://www.freecodecamp.org/news/content/images/2022/06/IMG_3418-1-.JPG)

## How to Set Up Cross Compilation

### Install the Target

Use `rustup` to install the necessary target for your Raspberry Pi:

```bash
my-pc$ rustup add target arm-unknown-linux-gnueabihf
```

[Appendix](#heading-targets-1) for more information about targets in Rust.

### Specify the Linker

Download the `raspberrypi/tools` repository into a directory named `rpi_tools`:

```bash
my-pc:~ $ git clone https://github.com/raspberrypi/tools $HOME/rpi_tools
```

Edit the `~/.cargo/config` file using your favourite text editor:

```bash
my_pc:~ $ sudo nano ~/.cargo/config
```

Tell Cargo to use a specific linker version for your target:

```conf
[target.arm-unknown-linux-gnueabihf]
linker = "/rpi_tools/arm-bcm2708/arm-rpi-4.9.3-linux-gnueabihf/bin/arm-linux-gnueabihf-gcc"
```

## How to Program an Embedded "Hello World"

Start by creating a new Rust project, and opening the `main.rs` file in your favourite text editor:

```bash
my-pc:~ $ cargo new blink
my-pc:~ $ cd blink
my-pc:~/blink $ nano src/main.rs
```

Import the `rust_gpiozero` crate, and program an LED to alternate between on and off every second:

```rust
use rust_gpiozero::*;

fn main() {
    // Create a new LED attached to Pin 17
    let mut led = LED::new(17);

    led.blink(1.0, 1.0);

    led.wait();
}
```

Be sure to add the dependency to the `Cargo.toml` file:

```toml
[dependencies]
rust-gpiozero = "0.2.1"
```

### Successfully Exit the Program

Since `rustc 1.61.0` <sup>[[1]]</sup>, you can use the `std::process::ExitCode` struct to specify the status code returned to the process' parent:

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

Otherwise, you can simply return a `Result`:

```rust
fn main() -> Result<(), std::io::Error> {
  // ...
  Ok(())
}
```

## How to Cross Compile the Program

Build a release of your program, targeting the required architecture:

```bash
my-pc:~/blink $ cargo build --release --target=arm-unknown-linux-gnueabihf
```

## How to Transfer the Binary to the Pi

Use `scp` to transfer the compiled binary from your host computer to the Raspberry Pi over SSH:

```bash
my-pc:~/blink $ scp target/arm-unknown-linux-gnueabihf/release/blink pi@192.168.1.199:~/blink
```

**Note:** The local IP of your Pi will likely be different.

## How to SSH into the Pi

SSH and log in to the Raspberry Pi via its local IP address:

```bash
my-pc:~ $ ssh pi@192.168.1.199
```

### Run the Program

From the Raspberry Pi, run the compiled binary:

```bash
pi:~ $ ./blink
```

## How to Code a Text-to-Morse-Code Translator

Here is an example of an application that reads the stdin line by line, translates the input into Morse Code, and toggles the LED on and off based on the Morse Code for the characters.

```rust
use rust_gpiozero::*;
use std::io::{BufRead, self};
use std::collections::HashMap;
use std::thread::sleep;
use std::time::Duration;

fn main() -> Result<(), std::io::Error> {
    println!("Starting...\n- Type in text to turn into Morse Code\n- Type `quit()` to quit\n");
    // Create a new LED attached to Pin 17
    let led = LED::new(17);

    /// Length of a dot in milliseconds
    const DOT_DELAY: u64 = 80;
    /// Length of a dash in milliseconds
    const DASH_DELAY: u64 = DOT_DELAY * 3;
    /// Delay between inputs in milliseconds
    const PUSH_DELAY: u64 = DOT_DELAY;
    /// Delay between letters in milliseconds
    const LETTER_DELAY: u64 = DOT_DELAY * 3;
    /// Delay between words in milliseconds
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

    // Read standard input per line
    for line_res in io::stdin().lock().lines() {
        let line = line_res?;
        if line == "quit()" {
            break;
        }
        // Turn line into morse code
        let mut morse = String::new();
        for c in line.chars() {
            if let Some(morse_code_char) = morse_code_alphabet.get(&c) {
                morse.push_str(morse_code_char);
                // Separate characters with a comma
                morse.push_str(",");
            }
        }
        // Blink LED based on characters
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
                    println!("Unknown character: {}", c);
                    break;
                }
            }
        }
        sleep(Duration::from_millis(WORD_DELAY));
    }

    // Free the variable and associated resources
    led.close();

    Ok(())
}
```

## Appendix

### Targets

In Rust, the _target_ is the platform (architecture) the program is compiled for. Cargo automatically detects the target, based on the file system layout <sup>[[2]]</sup>.

You can see the list of built-in targets, by running:

```bash
rustc --print target-list
# OR
rustup target list
```

From here you can add a new target to your project, by running:

```bash
rustup target add <target>
```

The given target is often in the form of a _triple_ <sup>[[3]]</sup>:

- The architecture
- The vendor
- The operating system type
- The environment type

_This is refered to as a 'target triple', because the fourth part is optional._

[1]: https://doc.rust-lang.org/stable/std/process/struct.ExitCode.html
[2]: https://doc.rust-lang.org/cargo/reference/cargo-targets.html#target-auto-discovery
[3]: https://rust-lang.github.io/rfcs/0131-target-specification.html



