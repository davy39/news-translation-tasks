---
title: Comment fonctionne la programmation asynchrone en Rust – Les Futures et Async/Await
  expliqués avec des exemples
date: '2024-08-15T15:18:18.081Z'
author: Oduah Chigozie
authorURL: https://www.freecodecamp.org/news/author/ghoulkingr/
originalURL: https://freecodecamp.org/news/how-asynchronous-programming-works-in-rust
posteditor: ''
proofreader: ''
co_authors: []
series: null
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723746256888/b046d857-161c-41be-96d0-1c05b1e448b8.jpeg
tags:
- name: Rust
  slug: rust
- name: async/await
  slug: asyncawait
- name: asynchronous
  slug: asynchronous
seo_desc: 'If you''re familiar with languages like JavaScript and Python, you may
  have heard about asynchronous programming. And perhaps you''re wondering how it
  works in Rust.

  In this article, I''ll give you a simple overview of how asynchronous programming
  works...'
---


Si vous êtes familier avec des langages comme JavaScript et Python, vous avez peut-être entendu parler de la programmation asynchrone. Et vous vous demandez peut-être comment cela fonctionne en Rust.

<!-- more -->

Dans cet article, je vais vous donner un aperçu simple du fonctionnement de la programmation asynchrone en Rust. Vous en apprendrez davantage sur les futures ainsi que sur `async`/`.await`.

Cet article n'est pas un guide pour débutants sur Rust ou sur la programmation asynchrone. Vous devrez donc avoir une certaine expérience de la programmation en Rust et une connaissance de la programmation asynchrone pour tirer le meilleur parti de ce guide.

Ceci étant dit, commençons !

## Quand devriez-vous utiliser la programmation asynchrone ?

Les tâches asynchrones fonctionnent comme une version plus intégrée des threads. Vous pouvez les utiliser dans la plupart des scénarios où vous utiliseriez plusieurs threads. L'avantage de la programmation asynchrone par rapport au multi-threading est que les applications multi-threadées ont un overhead plus important pour gérer plusieurs tâches simultanément.

Cependant, cela ne rend pas les applications asynchrones intrinsèquement meilleures que les applications multi-threadées. Les programmes multi-threadés peuvent exécuter plusieurs tâches intensives en calcul simultanément – et ce, plusieurs fois plus vite que si vous exécutiez toutes les tâches dans un seul thread.

Avec le code asynchrone, essayer d'exécuter simultanément plusieurs applications intensives en calcul sera beaucoup plus lent que de simplement exécuter chaque tâche sur un seul thread.

La programmation asynchrone est très efficace pour créer des applications qui effectuent de nombreuses requêtes réseau ou de nombreuses opérations d'E/S (Entrées/Sorties), comme la lecture et l'écriture de fichiers.

Je ne peux pas couvrir tous les cas où vous voudrez utiliser des techniques asynchrones. Mais je peux dire qu'elles sont particulièrement bénéfiques pour les tâches qui comportent beaucoup de temps d'inactivité (par exemple, attendre qu'un serveur réponde à une requête réseau).

Pendant le temps d'inactivité d'une tâche asynchrone, au lieu de bloquer le thread, le gestionnaire d'événements travaille sur d'autres tâches du programme jusqu'à ce que la tâche asynchrone soit prête à progresser.

## Aperçu de Rust asynchrone – Les Futures

La base de Rust asynchrone repose sur les Futures. Les Futures sont similaires aux promesses en JavaScript. C'est la façon pour Rust de dire : "Hé, je vais te donner le résultat plus tard, mais garde ceci (l'instance de la future) pour savoir quand le résultat sera prêt."

Les Futures sont des traits, avec un état de `poll` qui est soit `Poll::Pending` pour signifier que la future est en cours d'exécution, soit `Poll::Ready` pour signifier que la future a terminé sa tâche.

Les Futures sont paresseux (lazy). Ils ne s'exécutent que lorsque vous les utilisez avec `.await` (nous verrons comment faire dans la section suivante). Utiliser `.await` sur une future interrompt l'exécution d'un thread asynchrone et commence l'exécution de sa tâche. À ce stade, le résultat de la méthode `poll` est `Poll::Pending`. Lorsque la future a terminé sa tâche, l'état de `poll` devient `Poll::Ready`, et la future permet à son thread de continuer.

Si vous souhaitez obtenir plus de détails techniques sur les Futures, vous pouvez consulter [la documentation][1].

## async/.await en Rust

`async` et `.await` sont les principaux moyens de travailler avec du code asynchrone en Rust. `async` est un mot-clé permettant de déclarer des fonctions asynchrones. À l'intérieur de ces fonctions, le mot-clé `.await` suspend l'exécution jusqu'à ce que le résultat de la future soit prêt.

Regardons un exemple :

```
async fn add(a: u8, b: u8) -> u8 {
    a + b
}

async fn secondFunc() -> u8 {
    let a = 10;
    let b = 20;
    let result = add(a, b).await;
    return result;
}
```

Toute fonction asynchrone déclarée avec `async fn` enveloppe sa valeur de retour dans une future. À la troisième ligne de `secondFunc`, nous utilisons `.await` sur la future retournée par `add(a, b)` pour obtenir son résultat avant de le retourner.

## Comment travailler avec des opérations asynchrones dans `main`

Rust ne vous permet pas de déclarer des fonctions `main` avec `async fn`. L'exécution d'opérations asynchrones à partir d'une fonction non asynchrone peut entraîner la fin du thread principal avant que certaines opérations ne soient totalement terminées.

Dans cette section, nous examinerons deux façons de résoudre ce problème : avec `tokio` et avec la bibliothèque `futures`.

### `tokio`

`tokio` est une plateforme qui fournit des outils et des API pour réaliser des applications asynchrones. `tokio` vous permet également de déclarer facilement une fonction `main` asynchrone, ce qui aide à résoudre le problème décrit précédemment.

Pour installer `tokio` dans votre projet, ajoutez cette ligne à votre fichier `Cargo.toml` :

```
[dependencies]
tokio = { version = "1", features = ["full"] }
```

Après avoir ajouté cette ligne, vous pouvez écrire vos fonctions `main` comme ceci :

```
async fn add(a: u8, b: u8) -> u8 {
    a + b
}

#[tokio::main]
async fn main() {
    let a = 10;
    let b = 20;
    let result = add(a, b).await;
    println!("{result}");
}
```

### La bibliothèque `futures`

`futures` est une bibliothèque qui fournit des méthodes pour travailler avec Rust asynchrone. Pour notre cas d'utilisation, `futures` propose `futures::executor::block_on()`. Cette méthode fonctionne de manière similaire à `.await` dans les fonctions asynchrones. Elle bloque le thread principal jusqu'à ce que le résultat de la future soit prêt. `futures::executor::block_on()` retourne également le résultat de la future terminée.

Pour installer `futures` dans votre projet, ajoutez cette ligne à votre fichier `Cargo.toml` :

```
[dependencies]
futures = "0.3"
```

Après avoir installé la bibliothèque, vous pouvez faire quelque chose comme ceci :

```
use futures::executor::block_on;

async fn add(a: u8, b: u8) -> u8 {
    a + b
}

fn main() {
    let a = 10;
    let b = 20;
    let result = block_on(add(a, b));
    println!("{result}"); 
}
```

Tout d'abord, nous importons la méthode `block_on` à la première ligne et nous l'utilisons pour bloquer le thread principal jusqu'à ce que le résultat de la fonction `add(a, b)` soit prêt. Nous n'avons pas eu besoin de rendre la fonction `main` asynchrone comme nous l'avons fait avec `tokio`.

## Conclusion

La programmation asynchrone vous permet d'exécuter des opérations en parallèle avec moins d'overhead et de complexité que le multi-threading traditionnel. En Rust, elle vous permet de créer des applications d'E/S et réseau plus efficacement.

Bien que cet article devrait vous aider à vous familiariser avec les bases de la programmation asynchrone en Rust, il ne s'agit que d'un aperçu. Dans certains cas, vous devrez utiliser d'autres constructions de Rust comme le Pinning, les Arcs, etc.

Si vous avez des questions ou des réflexions, n'hésitez pas à me contacter. Merci de m'avoir lu !

[1]: https://rust-lang.github.io/async-book/02_execution/01_chapter.html