---
title: Signification de RNG – Que signifie RNG dans les jeux ?
subtitle: ''
author: Ilenia Magoni
co_authors: []
series: null
date: '2021-09-15T21:55:10.000Z'
originalURL: https://freecodecamp.org/news/rng-meaning-what-does-rng-stand-for-in-gaming
coverImage: https://www.freecodecamp.org/news/content/images/2021/09/pexels-pixabay-37534.jpg
tags:
- name: '#Game Design'
  slug: game-design
- name: gaming
  slug: gaming
- name: JavaScript
  slug: javascript
- name: Math
  slug: math
- name: Python
  slug: python
- name: random
  slug: random
seo_title: Signification de RNG – Que signifie RNG dans les jeux ?
seo_desc: 'If everything is predictable in a game, that isn''t much fun. RNGs, or
  Random Number Generators, are a way to introduce a touch of randomness and causality
  you need to spice it up.

  In this article, we''ll learn how random number generators work.

  How an...'
---

Si tout est prévisible dans un jeu, ce n'est pas très amusant. Les RNG, ou générateurs de nombres aléatoires, sont un moyen d'introduire une touche d'aléatoire et de causalité pour pimenter le jeu.

Dans cet article, nous allons apprendre comment fonctionnent les générateurs de nombres aléatoires.

## Comment fonctionne un générateur de nombres aléatoires analogique

La forme la plus simple d'un RNG est le lancer de dés ou le pile ou face.

Utiliser un seul dé ou une seule pièce signifie que chaque valeur a la même probabilité de se produire. Utiliser plusieurs dés ou pièces donnera une probabilité plus faible aux valeurs les plus élevées et les plus basses, et une probabilité plus élevée aux valeurs moyennes.

Le plus ancien jeu de table connu, [le Jeu Royal d'Ur](https://en.wikipedia.org/wiki/Royal_Game_of_Ur), utilise quatre dés à quatre faces. Chaque dé peut donner une valeur de 0 ou 1, ce qui signifie que la valeur obtenue par un seul lancer de dé peut aller de 0 à 4.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-1.png)
_Toutes les combinaisons possibles obtenues en lançant 4 dés, chacun pouvant donner une valeur de 0 ou 1_

Il y a 16 combinaisons possibles, dont une donne une valeur de 0, 4 donnent une valeur de 1, 6 donnent une valeur de 2, 4 donnent une valeur de 3, et une donne une valeur de 4.

Dans ce cas, il y a 1 chance sur 16 ou 6,25 % de chance d'obtenir 0, 1 chance sur 4 ou 25 % de chance d'obtenir 1, 3 chances sur 8 ou 37,5 % de chance d'obtenir 2, 1 chance sur 4 ou 25 % de chance d'obtenir 3 et 1 chance sur 16 ou 6,25 % de chance d'obtenir 4.

Des jeux plus complexes ont des manuels remplis de tables pour déterminer quelque chose de manière aléatoire.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-2.png)
_Partie d'une table pour les effets aléatoires après avoir bu une potion. [Voici la table complète](https://luetkemj.github.io/160419/random-potion-effects-table)._

Tout jeu qui utilise des dés a un générateur de nombres aléatoires analogique.

## Comment fonctionnent les générateurs de nombres aléatoires dans les jeux vidéo

Dans les jeux vidéo, les RNG sont beaucoup moins visibles et plus complexes, et les joueurs ne savent peut-être même pas qu'ils existent. [Il existe de nombreuses façons de générer un nombre aléatoire](https://www.freecodecamp.org/news/random-number-generator/), mais comment les utilise-t-on réellement ?

En le décomposant en termes simples, utiliser un RNG n'est pas très différent de ce que vous avez vu ci-dessus avec le lancer de dés utilisé pour déterminer un effet à partir d'une table. Vous ne voyez simplement pas le lancer de dés.

Dans un jeu vidéo, vous pouvez utiliser un RNG pour déterminer quel type de butin peut être abandonné par un ennemi vaincu, ou ce que vous pouvez trouver dans un coffre, ou quel type de rencontre aléatoire vous attend, ou même quel temps il fera.

Les RNG sont utilisés, par exemple, pour donner vie aux jeux en monde ouvert sans que les développeurs aient à coder chaque section de forêts, de routes et de déserts. Au lieu de cela, les développeurs codent quelques possibilités et laissent le hasard déterminer ce qui se passe lorsque le joueur atteint un certain point sur la carte.

Rencontrerez-vous un ours, une meute de loups ou des bandits ? Le jeu fait sa version du lancer de dés pour le déterminer.

Voyons comment coder un exemple simple de générateur de nombres aléatoires pour mieux comprendre comment ils fonctionnent réellement.

## Comment coder un générateur de nombres aléatoires

La plupart des langages de programmation contiennent une fonction `random`. Cette fonction retourne un nombre aléatoire, et le type de nombre aléatoire dépend de son implémentation.

Par exemple, en [JavaScript](https://www.freecodecamp.org/news/javascript-math-random-method-explained/), [`Math.random()`](https://www.freecodecamp.org/news/javascript-math-random-method-explained/) retourne un nombre aléatoire entre 0 (inclus) et 1 (non inclus). En Python, `randint` du module `random` retourne un nombre entier dans une plage (Python a également une fonction qui fait la même chose que `Math.random` de JavaScript).

Considérons une situation assez courante dans les jeux vidéo : nous avons un ennemi qui abandonne souvent un objet commun, mais de temps en temps abandonne quelque chose de rare. Cet ennemi peut être, par exemple, un loup qui pourrait abandonner une peau de loup (commune) ou une dent de loup (rare).

Comment déterminez-vous ce qui est "rare" ? Cela dépend de vous – il peut s'agir que 1 sur 10 abandons soit un objet rare, ou que 1 sur 100 abandons soit un objet rare. Un terrain d'entente peut être une chance de 1 sur 25 pour un objet rare. Et pour compliquer un peu les choses, il pourrait y avoir aussi une chance de 1 sur 10 de ne pas obtenir d'objet.

Dans ce cas, vous auriez besoin d'une fonction qui retourne une valeur entre 0 et 1.

Une chance de 1 sur 25 est de 4 %, et une chance de 1 sur 10 est de 10 %. En forme décimale, cela serait 0,04 et 0,1, respectivement.

Dans ce cas, vous pouvez dire qu'un nombre dans la plage de 0 à 0,04 donne l'objet rare, et qu'un nombre dans la plage de 0,9 à 1 ne donne aucun objet.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-3.png)
_La répartition en pourcentage de l'abandon du loup_

Pour éviter de se limiter à un seul langage, voyons d'abord comment nous pouvons coder cela en utilisant du [pseudocode](https://www.freecodecamp.org/news/what-is-pseudocode-in-programming/). Ce n'est pas un vrai langage de programmation – plutôt, c'est une façon de décomposer la logique du code. C'est comme prendre des notes, car c'est personnel et aura une syntaxe variée selon la personne qui l'écrit.

```
FONCTION wolfDrop
  randomNumber = random(0,1)
  SI
    randomNumber < 0.04
    ALORS
     -> dent de loup
  SINON SI
    randomNumber < 0.9
    ALORS
     -> peau de loup
  SINON
    -> vide
  FIN SI
FIN FONCTION
```

Ou une version plus verbeuse :

> Créez une fonction appelée `wolfDrop` et à l'intérieur stockez un nombre aléatoire entre 0 (inclus) et 1 (exclu) dans la variable `randomNumber`. Si `randomNumber` a une valeur inférieure à `0.04`, l'abandon sera une dent de loup, sinon si `randomNumber` a une valeur inférieure à `0.9`, l'abandon sera une peau de loup, et sinon il n'y aura pas d'abandon.

Avec le pseudocode prêt, nous pouvons implémenter l'extrait de code dans n'importe quel langage. Voyons, par exemple, comment le coder dans quelques langages différents :

```javascript
function wolfDrop () {
  const randomNumber = Math.random();
  if (randomNumber < 0.04) {
    return "Dent de loup";
  } else if (randomNumber < 0.9) {
    return "Peau de loup";
  } else {
    return;
  }
}
```

```python
import random
def wolfDrop():
  randomNumber = random.random()
  if randomNumber < 0.04:
    return "Dent de loup"
  elif randomNumber < 0.9:
    return "Peau de loup"
  else:
    return
```

```clojure
(defn wolf-drop []
  (let [random-number (rand)]
    (cond (< random-number 0.04) "Dent de loup"
          (< random-number 0.9) "Peau de loup")))
```

```go
func wolfDrop() string {
    randomNumber := rand.Float64()
    switch {
        case randomNumber < 0.04:
            return "Dent de loup"
        case randomNumber < 0.9:
            return "Peau de loup"
        default:
            return ""
    }
}
```

```kotlin
fun wolfDrop(): String {
    val randomNumber = Random.nextFloat()
    when {
        randomNumber < 0.04 -> return "Dent de loup"
        randomNumber < 0.9 -> return "Peau de loup"
        else -> return ""
    }
}
```

```elixir
def wolf_pelt() do
  random_number = :rand.uniform()
  cond do
    random_number < 0.04 -> "Dent de loup"
    random_number < 0.9 -> "Peau de loup"
    true -> nil
  end
end
```

```c#
string WolfPelt() {
  var random = new Random();
  double randomNumber = random.NextDouble();
  if (randomNumber < 0.04) return "Dent de loup";
  if (randomNumber < 0.9) return "Peau de loup";
  return null;
}
```

```rust
extern crate rand;

fn wolf_drop() -> &'static str {
  let random_number: f64 = rand::random();
  if random_number < 0.04 {
    "Dent de loup"
  } else if random_number < 0.9 {
    "Peau de loup"
  } else {
    ""
  }
}
```

```c
#include <stdlib.h>
#include <string.h>
#include <time.h>

int wolf_drop(char *drop_item) {
  srand((unsigned) time(0));
  double random_number = 1.0 * rand() / RAND_MAX;
  if (random_number < 0.04) {
    strncpy(drop_item, "dent de loup\0", 12);
  } else if (random_number < 0.9) {
    strncpy(drop_item, "peau de loup\0", 12);
  } else {
    strncpy(drop_item, "\0", 1);
  }
  return 0;
}
```

```julia
function wolfdrop()
    randomnumber = rand()
    if randomnumber < 0.04
        return "dent de loup"
    elseif randomnumber < 0.9
        return "peau de loup"
    else
        return ""
    end
end
```

(Merci à [alpox](https://forum.freecodecamp.org/u/alpox) pour les extraits de code en Clojure, Golang, Kotlin, Elixir et C#, et à [Jeremy](https://www.freecodecamp.org/news/author/jeremylt/) pour les extraits en Rust, C et Julia.)

### Autres exemples de math.random

Si vous voulez en apprendre plus sur tout cela, vous pouvez lire cet article sur la [fonction Math.random en JavaScript](https://www.freecodecamp.org/news/how-to-use-javascript-math-random-as-a-random-number-generator/) et créer un jeu de lancer de dés.

Vous pouvez également lire cet [article sur l'utilisation de l'algorithme de marche aléatoire](https://www.freecodecamp.org/news/how-to-make-your-own-procedural-dungeon-map-generator-using-the-random-walk-algorithm-e0085c8aa9a/) et créer une carte de donjon aléatoire avec JavaScript pour expérimenter davantage avec les RNG.

## Conclusion

Les générateurs de nombres aléatoires, ou RNG, sont utilisés dans de nombreux jeux. Dans cet article, vous avez appris comment et pourquoi ils sont utilisés, et vous avez vu un exemple d'implémentation.

La prochaine fois que vous jouerez à un jeu vidéo, serez-vous capable de repérer où un RNG peut être utilisé ?