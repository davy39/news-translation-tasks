---
title: Fonctionnement des tests unitaires en Rust
date: '2022-07-27T16:26:05.000Z'
authorURL: ''
originalURL: https://freecodecamp.org/news/unit-testing-in-rust
posteditor: ''
proofreader: ''
author: freeCodeCamp
co_authors: []
series: null
coverImage: https://www.freecodecamp.org/news/content/images/2022/07/UNIT-TESTING-IN-RUST.png
tags:
- name: Rust
  slug: rust
- name: Testing
  slug: testing
- name: unit testing
  slug: unit-testing
seo_desc: 'By Menard Maranan

  Testing is an essential part of Software Development. Testing your code ensures
  that the software you develop works as expected and makes it less vulnerable to
  attackers.

  Software testing is a very broad topic. That''s why in the sof...'
---


Par Menard Maranan

<!-- more -->

Le test est une partie essentielle du développement logiciel. Tester votre code garantit que le logiciel que vous développez fonctionne comme prévu et le rend moins vulnérable aux attaquants.

Le test logiciel est un sujet très vaste. C'est pourquoi, dans l'industrie du logiciel, il existe des professionnels distincts qui se spécialisent uniquement dans la QA (assurance qualité) et les tests. Ces professionnels sont souvent appelés ingénieurs QA.

Bien que la QA soit une discipline à part entière, cela ne signifie pas que les développeurs ne font pas de tests du tout.

Les tests les plus courants que les développeurs effectuent sont les **tests unitaires**. Le test unitaire est un type de test où vous testez de petites unités de code (comme des fonctions) – d'où le terme, test unitaire. Vous le faites souvent en comparant le comportement attendu d'une unité de code avec son comportement réel.

Le test unitaire est une partie tellement intégrante du flux de travail de développement que la culture de développement de certaines entreprises est centrée sur ce qu'on appelle le [**Développement piloté par les tests** (ou TDD)][1].

En TDD, les développeurs écrivent d'abord des cas de test (à partir des exigences de la fonctionnalité, souvent appelées **user story**) et procèdent ensuite à l'écriture du code qui les satisfait. Le TDD brille principalement dans les projets où les exigences sont très spécifiques.

Vous pouvez implémenter les tests unitaires de différentes manières selon les langages de programmation. Mais à la base, le test unitaire consiste simplement à comparer le comportement attendu par rapport au comportement réel du code.

Ainsi, quelle que soit la manière dont il est implémenté dans un langage particulier, le même principe s'applique généralement lorsque vous travaillez dans n'importe quel autre langage.

Dans ce tutoriel, vous apprendrez les tests unitaires dans le langage de programmation Rust. Cela dit, vous devriez connaître au moins les [bases de la programmation en Rust][2], bien que vous n'ayez pas besoin de connaissances avancées.

Cet article couvrira :

-   Le fonctionnement des tests unitaires en Rust
-   Comment écrire un test unitaire en Rust
-   Comment tester une fonction
-   Pourquoi les tests qui échouent sont utiles
-   Comment gérer les comportements d'erreur attendus pour que vos tests n'échouent pas

Alors, avec tout cela dit, apprenons les tests unitaires avec Rust !

# Fonctionnement des tests unitaires en Rust

Rust est construit avec la sécurité du code en son cœur. Les règles strictes d'annotation de type de Rust aident à éliminer une multitude de bugs dès le début de la phase de développement. Mais malgré tout, ce n'est pas infaillible.

Comme pour tout autre langage, la logique métier repose sur vos épaules et vous devez aider Rust à comprendre ce qui est acceptable dans votre code et ce qui ne l'est pas.

Et oui, c'est pour cela que nous faisons des tests.

Vous n'avez pas besoin d'installer une suite de tests pour commencer à tester en Rust, car il dispose d'un support intégré pour les tests.

Pour commencer, créez un nouveau projet cargo (notez l'option `--lib`) sur votre machine locale et ouvrez-le dans l'éditeur de texte ou l'IDE de votre choix. Pour ce tutoriel, j'utiliserai VS Code.

```
cargo new --lib rust_unit_testing
code rust_unit_testing
```

Ensuite, ouvrez le fichier `src/lib.rs`. C'est là que nous passerons le plus de temps dans ce tutoriel.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/1-2.JPG) _Fichier src/lib.rs d'un projet de bibliothèque Rust_

Dans un projet de bibliothèque Rust nouvellement créé, vous remarquerez que le fichier `lib.rs` est déjà pré-rempli par défaut avec un exemple de code de test.

Le but principal est de vous donner un modèle pour commencer à écrire vos tests. Nous allons disséquer chaque partie de ce test simple et comprendre les concepts de base des tests en Rust.

Tout d'abord, comprenons ce que font ces lignes de code de test. Dans cet exemple, vous verrez un module de test défini dans `lib.rs` avec un test à l'intérieur qui vérifie si 2 + 2 est égal à 4.

Si vous ne connaissez pas encore le concept de modules et d'attributs en Rust, ce n'est pas grave et vous pouvez les ignorer pour l'instant.

Mais juste pour vous donner une idée, les tests en Rust sont écrits à l'intérieur du module `tests` (la partie `mod tests` indique qu'il s'agit du module de tests), et tout ce qui est écrit à l'intérieur de ce module indique à cargo de ne les exécuter que pendant les tests (et c'est essentiellement ce que l'attribut `#[cfg(test)]` implique).

Un test en Rust est essentiellement une fonction annotée comme test. Dans l'exemple ci-dessus, vous remarquerez l'attribut `#[test]` au-dessus de la fonction `it_works`. Cela indique simplement à cargo que cette fonction est un test et qu'elle doit être invoquée pendant les tests.

À l'intérieur de la fonction de test `it_works`, on vérifie si la valeur de `result` dérivée de 2 + 2 est égale à 4. Elle effectue la vérification à l'aide de la macro `assert_eq!`. La macro `assert_eq!` compare l'égalité ( `==` ) des valeurs gauche et droite qui lui sont passées.

Dans la plupart des langages de programmation, il existe une règle selon laquelle les valeurs de gauche passées à l'assertion doivent être les valeurs attendues, tandis que la valeur réelle doit être à droite. Avec Rust, il n'y a pas de règles strictes pour cela et vous pouvez passer les résultats attendus et réels de n'importe quel côté.

Maintenant, essayez d'exécuter votre test en utilisant cette commande :

```
cargo test
```

Voici à quoi devrait ressembler le résultat pour l'exemple ci-dessus :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/2-1.JPG) _cargo test - résultats_

En exécutant `cargo test`, cargo exécutera vos cas de test et affichera le rapport dans votre terminal. Dans ce rapport, vous verrez les tests exécutés par cargo.

La première ligne du rapport indique `running 1 test` puisque nous n'avons qu'une seule fonction de test `tests::it_works`. À côté de la fonction testée, vous verrez le message `ok`, ce qui signifie que le test a réussi.

Vous pouvez également voir le résumé des résultats ci-dessous :

-   1 passed (réussi)
-   0 failed (échoué)
-   0 ignored (ignoré)
-   0 measured (mesuré)
-   0 filtered out (filtré)
-   et le statut du résultat qui indique `test result: ok`

Le compteur `1 passed` ici représente la fonction de test (`tests::it_works`) qui a réussi le test, tandis que le compteur `failed` indique combien de tests échouent. Il en va de même pour les autres compteurs.

Vous verrez également les résultats des **Doc-tests** ci-dessous. Comme nous n'avons pas de tests de documentation ici, vous verrez `running 0 tests`. Vous pouvez ignorer cela pour l'instant et vous concentrer uniquement sur les tests unitaires. Mais si vous voulez en savoir plus, vous pouvez consulter la [documentation officielle de Rust][3].

## Comment écrire des tests en Rust

Lors de l'écriture d'un test, vous devez généralement passer par ces trois étapes :

1.  **Mocker** les données ou l'état nécessaire pour un cas de test. Par là, j'entends fournir des données fictives ou des échantillons de données nécessaires au code que vous testez (si nécessaire) et/ou configurer l'état ou l'environnement nécessaire pour que le cas de test s'exécute.
2.  Exécuter le code qui doit être testé (en passant les données fictives nécessaires). Un exemple est l'invocation d'une fonction que vous souhaitez tester.
3.  Vérifier si le comportement réel du code que vous testez correspond à son comportement attendu. Par exemple, en passant un argument `x` à une fonction, vous affirmez si sa valeur retournée est la même que ce que vous attendez qu'elle retourne. Ou vérifiez si une unité de code déclenche un `panic!`—ce qui est le comportement attendu, par exemple—si on lui donne un certain paramètre.

En Rust, les tests unitaires sont écrits dans le fichier exact où le code testé est écrit. Les fonctions de test sont ensuite regroupées à l'intérieur du module `tests` (qui est nommé ainsi par convention).

### Comment tester des fonctions en Rust

Passons maintenant au test des fonctions en Rust.

Pour commencer, nous avons besoin d'une fonction simple à tester. Mais d'abord, supprimez la fonction de test `it_works` car nous n'en avons plus besoin. Ensuite, écrivez cette fonction `adder` au-dessus du module `tests` :

```rust
// src/lib.rs

pub fn adder(x: i32, y: i32) -> i32 {
    x + y
}

#[cfg(test)]
mod tests {
// ...
```

La fonction `adder` ci-dessus est une fonction publique simple qui additionne simplement deux nombres et renvoie la somme. Pour tester si elle fonctionne comme prévu, écrivons un test unitaire pour cette fonction.

D'après les trois étapes d'écriture des tests unitaires dont nous avons discuté précédemment, les deux premières étapes sont :

-   définir les données pour le code à tester
-   exécuter le code.

Revenons donc au module `tests`, tout d'abord, amenez la fonction `adder` dans sa portée (en utilisant le mot-clé `use`). Ensuite, écrivez une fonction nommée `it_adds` annotée avec l'attribut `#[test]`.

```rust
// src/lib.rs

pub fn adder (x: i32, y: i32) -> i32 {
    x + y
}

#[cfg(test)]
mod tests {
    // ceci amène tout de la portée parente dans cette portée
    use super::*;

    #[test]
    fn it_adds() {
    }
}
```

C'est à l'intérieur de la fonction de test `it_adds` que nous écrirons les tests. Donc, à l'intérieur, déclarez une variable nommée `sum`, puis appelez la fonction `adder` et passez 4 et 5 comme paramètres (qui sont nos données fictives).

```rust
// src/lib.rs

// --snip--

    #[test]
    fn it_adds() {
        let sum = adder(4, 5);
    }
}
```

Et enfin, la troisième étape de l'écriture des tests unitaires consiste à vérifier le comportement attendu par rapport au comportement réel du code que nous testons.

Ici, affirmons si la valeur de `sum` telle que retournée par la fonction `adder` est égale à `9` (qui est notre valeur de retour attendue) en utilisant la macro `assert_eq!`.

```rust
// src/lib.rs

// --snip--

    #[test]
    fn it_adds() {
        let sum = adder(4, 5);
        assert_eq!(sum, 9);
    }
}
```

Voici la version finale de notre code et de notre test dans le fichier `lib.rs` :

```rust
// src/lib.rs

pub fn adder(x: i32, y: i32) -> i32 {
    x + y
}

#[cfg(test)]
mod tests {
    // ceci amène tout de la portée parente dans cette portée
    use super::*;

    #[test]
    fn it_adds() {
        let sum = adder(4, 5);
        assert_eq!(sum, 9);
    }
}
```

Comme vous l'avez appris précédemment, vous pouvez exécuter ce test en utilisant cette commande :

```
cargo test
```

Si tout fonctionne bien, nous devrions obtenir `test result: ok` indiquant que nos tests ont réussi.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/3.JPG)

Vous pouvez ajouter plus de tests dans le module `tests` pour la fonction `adder` si vous le souhaitez (par exemple, ajouter des nombres négatifs). Ou mieux encore, créez votre propre fonction et écrivez un test (ou des tests) pour celle-ci.

De plus, il existe de nombreuses autres macros d'assertion intégrées en Rust que vous pouvez utiliser en plus de la macro `assert_eq!`. Certaines d'entre elles incluent la macro `assert_ne!` pour affirmer des valeurs non égales (`!=`), et la macro `assert!` qui affirme simplement si le code que vous testez renvoie une valeur `true`.

Si vous avez besoin de plus de macros d'assertion (par exemple, des assertions de comparaison qui supportent `>`, `<`, `>=`, `<=`), vous pouvez installer des crates externes comme celle-ci : [claim][4]. Vous pouvez consulter la [documentation de claim ici][5] pour plus d'informations.

## Pourquoi les tests qui échouent sont utiles

Jusqu'à présent, nous obtenons toujours des résultats positifs pour nos tests.

Bien que ce soit une bonne chose, la véritable puissance des tests unitaires vient de la détection d'erreurs ou de bugs dans notre code et de leur signalement par des tests qui échouent. Pour cette fois, écrivons intentionnellement un code "buggé" et voyons ce qui se passe.

De retour dans le fichier `lib.rs`, modifiez la fonction `adder` en remplaçant l'opérateur `+` par `-`.

```rust
// src/lib.rs

pub fn adder(x: i32, y: i32) -> i32 {
    // changez l'opérateur de '+' à '-'
    x - y
}

// --snip--
```

Maintenant, exécutez à nouveau les tests en utilisant `cargo test`. Et comme prévu, vous devriez voir un résultat de test échoué comme celui-ci :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/4.JPG) _test échoué par cargo_

Tout d'abord, remarquez que le statut de la fonction de test `tests::it_adds` est un gros `FAILED` rouge. C'est à cela que ressemblent les tests échoués avec cargo.

En dessous, vous verrez le rapport "failures" qui répertorie les tests qui ont échoué et quelques informations sur la raison de leur échec.

Dans notre exemple, le test `tests::it_adds` a échoué et, comme l'indique le rapport, les valeurs gauche et droite passées à la macro `assert_eq!` ne sont pas égales (`==`).

C'est parce que la valeur de gauche est `-1` alors que la valeur de droite est `9`. Rappelez-vous que dans notre assertion `assert_eq!`, la valeur de gauche que nous lui avons passée est la variable `sum` qui contient la valeur de retour de `adder(4, 5)`.

Comme notre opérateur est faux, la fonction `adder` effectue `4 - 5` au lieu de `4 + 5` attendu. C'est pourquoi, au lieu de la valeur attendue de `9`, nous avons obtenu `-1`. Cargo l'a remarqué et a donc déclenché un échec de test.

Sous le rapport des tests échoués se trouve son résumé (en quelque sorte), toujours sous la catégorie `failures`, mais listant simplement les noms des fonctions de test qui ont échoué.

Et enfin, le résumé complet du test global :

-   Le statut est : `test result: FAILED`
-   0 passed
-   1 failed
-   0 ignored
-   0 measured
-   0 filtered out

Cette fois, notre compteur `failed` est à `1` (faisant référence à notre fonction de test échouée) tandis que `passed` est à `0`.

## Comment gérer les erreurs attendues

Dans la section précédente, vous avez appris que les erreurs font échouer les tests.

Mais que se passe-t-il si vous vous attendez à ce que le code que vous testez échoue (comme par exemple, en lui donnant un paramètre invalide). S'il rencontre une erreur, cargo signalera cela comme un test échoué même si vous vous attendiez réellement à ce qu'il échoue.

Peut-on s'attendre à des comportements d'échec ?

La réponse courte est : oui, vous le pouvez !

Pour démontrer cela, retournons au fichier `lib.rs` et modifions notre fonction `adder`. Cette fois, définissons une règle pour qu'elle n'accepte que des entiers à un seul chiffre (positifs, nuls et négatifs) – sinon, elle devrait "paniquer" (`panic`). Et pour des raisons de lisibilité, rennommons notre fonction `adder` en `single_digit_adder`.

```rust
// src/lib.rs

// modifiez la fonction `adder` de tout à l'heure
// et transformez-la en `single_digit_adder`
pub fn single_digit_adder(x: i8, y: i8) -> i8 {
    fn is_single_digit(x: i8) -> bool {
        x < 10 && x > -10
    }

    if !(is_single_digit(x)) || !(is_single_digit(y)) {
        panic!("Only single digit integers are allowed!");
    } else {
        x + y
    }
}

#[cfg(test)]
mod tests {
// --snip--
```

Comme nous nous attendons à ce que la fonction `single_digit_adder` déclenche un `panic!` chaque fois qu'elle reçoit un entier qui n'est pas à un seul chiffre, nous devons le spécifier sur la fonction de test qui est chargée de tester précisément ce comportement.

Pour ce faire, nous devons ajouter un autre attribut à l'une de nos fonctions de test. Il s'agit de l'attribut `#[should_panic]`.

En revenant au module `tests`, tout d'abord, modifiez la fonction de test `it_adds` en renommant l'appel de la fonction `adder` en `single_digit_adder`.

Ensuite, créez une nouvelle fonction de test nommée `it_should_only_accept_single_digits` avec à la fois l'attribut `#[test]` et l'attribut `#[should_panic]`.

À l'intérieur de cette nouvelle fonction de test, appelez la fonction `single_digit_adder` avec un paramètre invalide (`11`) dans ce cas.

```rust
// src/lib.rs

pub fn single_digit_adder(x: i8, y: i8) -> i8 {
    // ...
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_adds() {
        let sum = single_digit_adder(2, 3);
        assert_eq!(sum, 5);
    }

    // notre nouvelle fonction de test qui attend un `panic!` avec un paramètre invalide
    #[test]
    #[should_panic]
    fn it_should_only_accept_single_digits() {
        single_digit_adder(11, 4);
    }
}
```

Vous n'avez pas besoin de macros d'assertion dans la fonction de test `it_should_only_accept_single_digits` puisque nous avons seulement besoin que `single_digit_adder` "panique". Appeler simplement la fonction est donc suffisant.

En lui donnant un paramètre invalide (`11`, qui n'est pas un chiffre unique), nous nous attendons à ce qu'elle déclenche un `panic`. L'attribut `#[should_panic]` attendra alors que quelque chose panique à l'intérieur de la fonction de test `it_should_only_accept_single_digits`. S'il ne capture aucun panic, ce test échouera. Il ne réussira que si `single_digit_adder` panique.

Donc, pour tester si cela fonctionne vraiment, essayez d'abord de mettre en commentaire l'attribut `#[should_panic]` puis exécutez `cargo test`. Vous devriez vous attendre à ce qu'il échoue.

![Image](https://www.freecodecamp.org/news/content/images/2022/07/6.JPG)

Maintenant, décommentez l'attribut `#[should_panic]` et relancez le test. Vos tests devraient tous réussir comme prévu :

![Image](https://www.freecodecamp.org/news/content/images/2022/07/5.JPG) _Le résultat d'un cas de test attendant et capturant effectivement un comportement d'échec_

Remarquez que sur le test `tests::it_should_only_accept_single_digits`, il y a une mention `should panic` à côté, et qu'il a réussi le test. Cela signifie que cette fonction de test a capturé un panic comme prévu.

Et voilà ! Vous venez d'apprendre ce qu'est le test unitaire et comment effectuer des tests unitaires avec le langage de programmation Rust. N'hésitez pas à écrire vos propres tests en utilisant les connaissances acquises dans cet article et à les utiliser dans vos futurs projets.

# Conclusion

Dans cet article, vous avez appris ce qu'est le test unitaire et son importance dans le processus de développement logiciel. Vous avez également appris comment écrire des tests unitaires via un processus simple en trois étapes et comment effectuer réellement des tests dans le langage de programmation Rust.

Nous avons couvert la structure d'un module de test en Rust et comment construire une fonction de test, puis nous avons écrit un programme Rust simple et quelques cas de test pour celui-ci. Nous avons également abordé les tests qui échouent et comment gérer un comportement d'échec attendu dans une unité de code.

Le test est une partie importante du processus de développement logiciel. Tester votre code aide à garantir que le logiciel fonctionne comme prévu. En tant que développeur, il est important que vous testiez votre code pour assurer la qualité du logiciel que vous livrez et pour que ces bugs stupides n'atteignent pas l'utilisateur final !

[1]: https://www.freecodecamp.org/news/test-driven-development-tutorial-how-to-test-javascript-and-reactjs-app/
[2]: https://www.freecodecamp.org/news/rust-in-replit/
[3]: https://doc.rust-lang.org/rust-by-example/testing/doc_testing.html
[4]: https://crates.io/crates/claim
[5]: https://docs.rs/claim/latest/claim/