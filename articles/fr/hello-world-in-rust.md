---
title: Hello World en Rust – Programme d'exemple
subtitle: ''
author: Sahil
co_authors: []
series: null
date: '2024-04-08T09:21:17.000Z'
originalURL: https://freecodecamp.org/news/hello-world-in-rust
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Neon-Green-Motivational.png
tags:
- name: beginner
  slug: beginner
- name: Rust
  slug: rust
seo_title: Hello World en Rust – Programme d'exemple
seo_desc: 'Starting with a new programming language is like taking your first step
  into a whole new world. One of the very first things you''ll do is write a simple
  program that says "Hello World!".

  Rust, known for being fast and safe, is no exception. Let''s jum...'
---

Commencer avec un nouveau langage de programmation, c'est comme faire ses premiers pas dans un monde entièrement nouveau. L'une des toutes premières choses que vous ferez est d'écrire un programme simple qui affiche "Hello World!".

Rust, connu pour être rapide et sûr, ne fait pas exception. Plongeons directement et créons ensemble notre tout premier programme Rust !

## Comment écrire un programme Hello World en Rust

Tout d'abord, créez un fichier nommé `main.rs`. Chaque programme Rust contient `.rs` comme extension de fichier.

Ensuite, écrivez le code suivant dans le fichier :

```rust
// main.rs
fn main() {
	println!("Hello World!");
}

```

Dans le code ci-dessus, nous essayons d'afficher `Hello World!` dans la console ou le terminal.

## Comment compiler le code Rust

En Rust, la compilation et l'exécution du code sont deux processus distincts.

Tout d'abord, vous devez compiler le programme Rust. Pour le compiler, écrivez ce qui suit dans le terminal (assurez-vous que le terminal se trouve dans le même répertoire que le fichier Rust) :

```bash
rustc main.rs

```

Pour l'instant, vous ne verrez aucune sortie car le code a simplement été compilé. Mais une chose que vous pouvez voir dans le répertoire actuel est qu'un nouveau fichier exécutable a été ajouté avec le même nom que le fichier Rust.

## Comment exécuter le fichier exécutable

Maintenant, vous pouvez exécuter le fichier exécutable qui est généré après avoir compilé avec succès le code Rust.

Pour exécuter le fichier exécutable, écrivez ce qui suit dans votre terminal :

```bash
./main

```

Vous devriez voir une sortie comme celle-ci :

```bash
Hello World!

```

## Comprendre le code Hello World en profondeur

```rust
fn main() {

}

```

Le programme commence avec une fonction appelée `main()`. Chaque code exécutable Rust commence l'exécution à partir de la fonction main.

La fonction main peut avoir certains paramètres à l'intérieur des parenthèses `()`, mais nous n'en avons pas besoin dans le code, donc nous les avons laissées vides.

Tout ce qui se trouve entre les accolades `{}` est le corps de la fonction. Il est nécessaire d'avoir des accolades pour le corps, sinon cela générera une erreur.

```rust
fn main() {
  println!("Hello World!");
}

```

Cette ligne se charge d'afficher le texte "Hello World!" dans le terminal ou la console.

Ici, `println!` n'est pas une fonction contrairement à d'autres langages comme C, Python, etc. C'est une macro – si un mot-clé se termine par un symbole `!`, alors c'est une macro.

Enfin, nous avons passé la chaîne de caractères comme argument à la macro et elle affiche la chaîne dans le terminal.

Pour terminer l'instruction en Rust, vous devez utiliser `;`. Si vous ne fournissez pas le point-virgule à la fin de chaque instruction, cela générera une erreur.

## Conclusion

Et voilà – votre premier programme Rust ! En affichant "Hello World!" vous avez trempé vos orteils dans le monde de Rust.

Ce programme simple vous a donné un aperçu de la syntaxe de Rust et de sa compilation. En continuant, vous découvrirez davantage les fonctionnalités intéressantes de Rust et constaterez à quel point il peut être puissant.

Prêt à plonger plus profondément ? Continuons à explorer !

Si vous avez des commentaires, n'hésitez pas à me contacter en DM sur [Twitter](https://twitter.com/introvertedbot) et [LinkedIn](https://www.linkedin.com/in/sahil-mahapatra/)