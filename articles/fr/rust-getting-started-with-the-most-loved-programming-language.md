---
title: Rust pour les débutants – Commencez avec le langage de programmation le plus
  apprécié
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-18T22:09:21.000Z'
originalURL: https://freecodecamp.org/news/rust-getting-started-with-the-most-loved-programming-language
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/rust-2.jpg
tags:
- name: programming languages
  slug: programming-languages
- name: Rust
  slug: rust
seo_title: Rust pour les débutants – Commencez avec le langage de programmation le
  plus apprécié
seo_desc: 'Rust has been voted Stack Overflow’s most loved programming language for
  five years in a row. This article will tell you why Rust is awesome.

  Rust is a systems programming language that you can use to write applications with
  high performance. Rust is...'
---

Rust a été élu langage de programmation le plus apprécié sur Stack Overflow pendant cinq années consécutives. Cet article vous expliquera pourquoi Rust est génial.

Rust est un [langage de programmation système](https://www.techopedia.com/definition/9616/system-programming) que vous pouvez utiliser pour écrire des applications à haute performance. Rust est utilisé par certaines des plus grandes entreprises technologiques comme Dropbox et Cloudflare pour offrir rapidité et concurrency à leurs clients.

Depuis cinq années consécutives, Rust a été élu langage de programmation le plus apprécié.

Mais il est probable que vous n'ayez pas encore travaillé avec Rust. Ou pire, que vous n'en ayez même jamais entendu parler. Alors, apprenons-en plus.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-5.png)
_Enquête StackOverflow 2020_

## Pourquoi Rust ?

Examinons pourquoi un développeur choisirait Rust.

Les langages de programmation typiques comme Python et C++ abstraient beaucoup de détails pour les développeurs.

Si vous êtes un développeur junior travaillant sur une simple application web, cela ne pose peut-être pas de problème. Vous voulez simplement trouver une solution à un problème.

Pour les applications à grande échelle utilisées par des millions d'utilisateurs au quotidien, l'approche de "résolution de problèmes" ne fonctionnera pas. Plus d'utilisateurs consomment plus de ressources système. Et plus de ressources signifient des factures plus élevées pour votre entreprise.

C'est là que Rust brille. Rust combine la facilité de programmation avec l'accès aux configurations système de base. Rust est conçu avec la sécurité de la mémoire, la concurrency et la sécurité dès le départ.

> Rust est un "langage de programmation système qui se concentre sur la vitesse, la sécurité de la mémoire et le parallélisme".

Rust est également considéré comme une excellente alternative à C++. Rust offre des performances élevées en plus de vous aider à [éliminer les bugs courants causés par des langages comme C++](https://polyfloyd.net/post/how-rust-helps-you-prevent-bugs/).

Maintenant que vous savez ce que Rust peut faire pour vous, examinons Rust en détail.

## Origines

Rust est un langage de programmation open-source. Il a été introduit pour la première fois en 2010 par Graydon Hoare, alors qu'il travaillait chez Mozilla. Peu après, Mozilla a commencé à sponsoriser ce projet et reste un contributeur clé de Rust.

Rust a commencé à gagner en popularité au fil des ans. Même Microsoft utilise Rust pour construire des composants logiciels sécurisés et critiques pour la sécurité.

## Fonctionnalités principales

Examinons quelques fonctionnalités principales qui font de Rust un langage de programmation unique.

### Performance

Rust a été conçu pour être performant dès le départ. Rust offre un contrôle fin de la gestion de la mémoire et possède une bibliothèque standard minimale.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/performance.png)
_Source : Figma_

Si vous regardez certaines des [métriques partagées par Figma](https://www.figma.com/blog/rust-in-production-at-figma/), ils ont obtenu des améliorations incroyables en performance une fois qu'ils sont passés à Rust.

L'empreinte mémoire faible de Rust en fait également un choix idéal pour la programmation des systèmes embarqués. Vous pouvez utiliser Rust pour écrire des logiciels pour des appareils IoT comme des hubs de domotique, des systèmes de sécurité intelligents, etc.

### Sécurité

L'une des principales raisons pour lesquelles Microsoft a décidé de soutenir Rust est sa sécurité.

La majorité des vulnérabilités dans les logiciels Microsoft étaient dues à une mauvaise gestion de la mémoire en C et C++. Cela a conduit à des exploits simples mais puissants comme l'exploit de [débordement de tampon](https://www.imperva.com/learn/application-security/buffer-overflow) qui a paralysé Windows pendant des années.

Microsoft a donc décidé de chercher la meilleure alternative à C++. Et ils ont trouvé Rust.

L'utilisation de Rust élimine une classe entière de vulnérabilités de sécurité des applications logicielles. Cela aide les entreprises à construire des applications avec de meilleures performances et une sécurité accrue.

### Concurrency

La concurrency est lorsque deux tâches ou plus commencent, s'exécutent et se terminent en temps chevauchant. Les opérations de base de données sont un excellent exemple pour expliquer la concurrency.

Lorsque des milliers d'utilisateurs utilisent votre application en même temps pour effectuer différentes actions, votre base de données les traite de manière concurrente. La concurrency est un concept clé lorsqu'il s'agit de mettre à l'échelle des applications.

La concurrency et le parallélisme sont également intégrés à Rust. Rust résout la plupart des problèmes de concurrency lors de la compilation en utilisant le concept de Propriétés. [Apprenez comment Rust gère la concurrency ici](https://doc.rust-lang.org/book/ch16-00-concurrency.html).

## Travailler avec Rust

Maintenant que vous comprenez les fonctionnalités principales de Rust, écrivons quelques lignes de code. Vous pouvez [trouver les instructions d'installation ici](https://www.rust-lang.org/tools/install) si vous souhaitez essayer Rust sur votre ordinateur.

Commençons par une simple fonction "Hello World !".

```rust
// Fonction principale
fn main() {
	println!("Hello World!");
}
```

Oui, c'est à peu près tout. Essayons d'additionner deux nombres.

```rust
// Fonction principale
fn main() {
	let a = 100;
    let b = 200;
    println!("Le résultat est {}",a+b);
}
```

Encore une fois, assez standard. Maintenant, regardons une opération sur un tableau.

```rust
// Fonction principale
fn main(){
	let arr:[i32;4] = [1,2,3,4];
    println!("La taille du tableau est {}",arr.len());
}
```

Si vous regardez la ligne 3, nous utilisons :[i32;4]. Ici, nous disons à Rust que nous déclarons un tableau de longueur 4 avec des entiers 32 bits.

Déclarer les types de données en détail est un facteur clé pour améliorer les performances d'un programme. Vous aidez le compilateur à gagner du temps en déclarant explicitement quel type de données vous allez assigner à une variable.

Laisser le compilateur deviner le type de données est l'une des principales raisons pour lesquelles vous rencontrez des problèmes de performance lors de la mise à l'échelle de votre application.

De plus, [Rust est un langage typé statiquement](https://stackoverflow.com/questions/1517582/what-is-the-difference-between-statically-typed-and-dynamically-typed-languages), ce qui signifie qu'il doit connaître les types de toutes les variables au moment de la compilation.

Bien que Rust soit syntaxiquement similaire à C et C++, ne vous laissez pas tromper par sa simplicité. Rust présente une courbe d'apprentissage abrupte. Mais cela en vaut vraiment la peine une fois que vous maîtrisez les bases.

## Qui utilise Rust ?

Maintenant que vous avez une bonne compréhension de ce qu'est Rust, voyons qui utilise Rust.

### Microsoft

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-6.png)

Autrefois un adversaire farouche de l'open source, Microsoft est désormais un contributeur assidu à de nombreux projets open-source. Leur projet .net core est l'un des frameworks open-source les plus populaires utilisés par les développeurs aujourd'hui.

Microsoft a choisi Rust pour les applications critiques en matière de sécurité et de performance. Rust est également largement utilisé dans Azure, en particulier dans sa [plateforme IoT Edge](https://azure.microsoft.com/en-in/services/iot-edge/) pour exécuter des applications d'IA sur des appareils IoT.

### Dropbox

![Image](https://www.freecodecamp.org/news/content/images/2020/08/1-7.png)

Dropbox utilise Rust pour améliorer l'efficacité de son centre de données. Rust alimente désormais les services principaux de Dropbox servant plus de 500 millions d'utilisateurs.

Dropbox [a récemment écrit un article détaillé](https://dropbox.tech/infrastructure/rewriting-the-heart-of-our-sync-engine) sur la manière dont ils ont réécrit leur moteur principal.

Selon les propres mots de Dropbox,

> Rust a été un multiplicateur de force pour notre équipe, et parier sur Rust a été l'une des meilleures décisions que nous ayons prises.

Rust a également été un facteur contribuant qui a aidé Dropbox à déplacer son infrastructure d'AWS vers ses propres centres de données.

### Figma

![Image](https://www.freecodecamp.org/news/content/images/2020/08/figma.png)

---

Figma est un outil de conception et de prototypage basé sur le cloud que vous pouvez utiliser dans votre navigateur. C'est un excellent outil pour la conception, le prototypage et l'exportation de vos designs en code. [En savoir plus sur Figma ici](https://www.figma.com/).

La concurrency est cruciale pour un outil collaboratif où de nombreux utilisateurs travailleront sur un seul design à la fois. Figma a utilisé Rust pour écrire un serveur haute performance qui les a aidés à mettre à l'échelle leur produit et à atteindre les performances qu'ils recherchaient.

[Voici l'article que Figma a écrit](https://www.figma.com/blog/rust-in-production-at-figma/) sur leur expérience avec Rust.

## TL;DR

Rust est un langage de programmation système qui a été élu [langage de programmation le plus apprécié de StackOverflow](https://stackoverflow.blog/2020/01/20/what-is-rust-and-why-is-it-so-popular/), quatre années de suite.

Rust vous donne le contrôle sur les détails de bas niveau et offre des améliorations remarquables en vitesse et en stabilité.

Il a aidé des entreprises comme Dropbox, Figma et Microsoft à construire de meilleures applications pour leurs clients.

Le langage est de plus en plus adopté par des entreprises cherchant à mettre à l'échelle leurs applications avec des performances et une concurrency accrues. Cela semble intéressant ? [Commencez à apprendre Rust ici](https://doc.rust-lang.org/stable/rust-by-example/).

---

_Je écris régulièrement sur l'apprentissage automatique, la cybersécurité et DevOps. Vous pouvez vous inscrire à ma [newsletter hebdomadaire](https://www.manishmshiva.com/) ici._