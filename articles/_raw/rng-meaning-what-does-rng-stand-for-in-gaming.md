---
title: RNG Meaning – What does RNG Stand for in Gaming?
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
seo_title: null
seo_desc: 'If everything is predictable in a game, that isn''t much fun. RNGs, or
  Random Number Generators, are a way to introduce a touch of randomness and causality
  you need to spice it up.

  In this article, we''ll learn how random number generators work.

  How an...'
---

If everything is predictable in a game, that isn't much fun. RNGs, or Random Number Generators, are a way to introduce a touch of randomness and causality you need to spice it up.

In this article, we'll learn how random number generators work.

## How an Analogic Random Number Generator Works

The simplest form of a RNG is throwing dice or flipping coins.

Using a single die or coin means that each value has the same probability of occurring. Using multiple dice or coins instead will give a lower probability to the highest and lower values, and a higher probability to the middle values.

The oldest known tabletop game, [the Royal Game of Ur](https://en.wikipedia.org/wiki/Royal_Game_of_Ur), uses four 4-sided dice. Each die can give a value of 0 or 1 meaning that the value obtained by a single dice throw can go from 0 to 4.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-1.png)
_All the possible combinations obtained by throwing 4 dice, each can give a value of 0 or 1_

There are 16 possible combinations, of which one gives a value of 0, 4 gives a value of 1, 6 gives a value of 2, 4 gives a value of 3, and one gives a value of 4.

In this case there is a 1/16 or 6.25% chance of getting 0, 1/4 or 25% chance of getting 1, 3/8 or 37.5% chance of getting 2, 1/4 or 25% chance of getting 3 and 1/16 or 6.25% change of getting 4.

More complex games have manuals full of tables to determine something randomly.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-2.png)
_Part of a table for random effects after drinking a potion. [Here's the whole table](https://luetkemj.github.io/160419/random-potion-effects-table)._

Any game that uses dice has an analogic random number generator.

## How Random Number Generators Work in Video Games

In video games, RNGs are much less noticeable and more complex, and players might not even be aware they exist. [There are many ways you can generate a Random Number](https://www.freecodecamp.org/news/random-number-generator/), but how do you actually use one?

Breaking it down into the simplest terms, using a RNG is not dissimilar from what you saw above with the dice throw used to determine an effect from a table. You just don't see the dice throw.

In a video game, you can use a RNG to determine what kind of loot might be dropped by a fallen enemy, or what you can find in a chest, or what kind of random encounter will await you, or even what the weather will be.

RNGs are used, for example, to live up open world games without the developers having to code every single section of forests and roads and deserts. Instead, developers code some possibilities and let chance determine what happens when the player reaches a certain point in the map. 

Will you meet a bear, a wolf pack, or some bandits? The game does its version of rolling a die to determine that.

Let's see how to code a simple example of a Random Number Generator to better understand how they actually work.

## How to Code a Random Number Generator

Most programming languages contain a `random` function. This function returns a random number, and what kind of random number depends on its implementation.

For example, in [JavaScript](https://www.freecodecamp.org/news/javascript-math-random-method-explained/), [`Math.random()`](https://www.freecodecamp.org/news/javascript-math-random-method-explained/) returns a random number between 0 (included) and 1 (not included). In Python, `randint` from the `random` module returns a whole number in a range (Python has also a function that does the same as JavaScript's `Math.random`).

Let's consider a pretty common video game situation: we have an enemy that often drops a common item, but now and then drops something rare. This enemy may be, for example, a wolf that could drop a wolf pelt (common) or a wolf fang (rare). 

How do you determine what is "rare"? That depends on you – it can be that 1 in 10 drops is a rare item, or that 1 in 100 drops is a rare item. A middle ground may be a chance of 1 in 25 for a rare items. And to complicate it a bit, there could be also a 1 in 10 chance of no item.

In this case you would need a function that returns a value between 0 and 1.

A chance of 1 in 25 is 4%, and a chance of 1 in 10 is 10%. In decimal form that would be 0.04 and 0.1, respectively. 

In this case you can say that a number in the range from 0 to 0.04 gives the rare item, and a number in the range from 0.9 to 1 gives no item.

![Image](https://www.freecodecamp.org/news/content/images/2021/09/image-3.png)
_The percentage breakdown of the wolf drop_

To avoid sticking to one language, let's first see how we can code this using [pseudocode](https://www.freecodecamp.org/news/what-is-pseudocode-in-programming/). This is not a real programming language – rather, it's a way to break down the code logic. It's like taking notes, as it's personal and will have varied syntax depending on the person writing it.

```
FUNCTION wolfDrop
  randomNumber = random(0,1)
  IF
    randomNumber < 0.04
    THEN
     -> wolf fang
  ELSE IF
    randomNumber < 0.9
    THEN
     -> wolf pelt
  ELSE
    -> empty
  END IF
END FUNCTION
```

Or a more verbose version:

> Create a function called `wolfDrop` and inside it store a random number between 0 (included) and 1 (excluded) in the `randomNumber` variable. If `randomNumber` has a value less than `0.04` the drop will be a wolf fang, else if the `randomNumber` has a value less than `0.9` the drop will be a wolf pelt, and otherwise there will be no drop.

With the pseudocode ready, we can implement the code snippet in any language. Let's see, for example, how to code it in a few different languages:

```javascript
function wolfDrop () {
  const randomNumber = Math.random();
  if (randomNumber < 0.04) {
    return "Wolf fang";
  } else if (randomNumber < 0.9) {
    return "Wolf pelt";
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
    return "Wolf fang"
  elif randomNumber < 0.9:
    return "Wolf pelt"
  else
    return
```

```clojure
(defn wolf-drop []
  (let [random-number (rand)]
    (cond (< random-number 0.04) "Wolf fang"
          (< random-number 0.9) "Wolf pelt")))
```

```go
func wolfDrop() string {
    randomNumber := rand.Float64()
    switch {
        case randomNumber < 0.04:
            return "Wolf fang"
        case randomNumber < 0.9:
            return "Wolf pelt"
        default:
            return ""
    }
}
```

```kotlin
fun wolfDrop(): String {
    val randomNumber = Random.nextFloat()
    when {
        randomNumber < 0.04 -> return "Wolf fang"
        randomNumber < 0.9 -> return "Wolf pelt"
        else -> return ""
    }
}
```

```elixir
def wolf_pelt() do
  random_number = :rand.uniform()
  cond do
    random_number < 0.04 -> "Wolf fang"
    random_number < 0.9 -> "Wolf pelt"
    true -> nil
  end
end
```

```c#
string WolfPelt() {
  var random = new Random();
  double randomNumber = random.NextDouble();
  if (randomNumber < 0.04) return "Wolf fang";
  if (randomNumber < 0.9) return "Wolf pelt";
  return null;
}
```

```rust
extern crate rand;

fn wolf_drop() -> &'static str {
  let random_number: f64 = rand::random();
  if random_number < 0.04 {
    "Wolf fang"
  } else if random_number < 0.9 {
    "Wolf pelt"
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
    strncpy(drop_item, "wolf fang\0", 10);
  } else if (random_number < 0.9) {
    strncpy(drop_item, "wolf pelt\0", 10);
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
        return "wolf fang"
    elseif randomnumber < 0.9
        return "wolf pelt"
    else
        return ""
    end
end
```

(Thanks to [alpox](https://forum.freecodecamp.org/u/alpox) for the code snippets in Clojure, Golang, Kotlin, Elixir and C#, and to [Jeremy](https://www.freecodecamp.org/news/author/jeremylt/) for the snippets in Rust, C, and Julia.)

### Other examples of math.random

If you want to learn more about all this, you can read this article about the [Math.random function in JavaScript](https://www.freecodecamp.org/news/how-to-use-javascript-math-random-as-a-random-number-generator/) and create a Dice Rolling Game. 

You can also read this [article on using the random walk algorithm](https://www.freecodecamp.org/news/how-to-make-your-own-procedural-dungeon-map-generator-using-the-random-walk-algorithm-e0085c8aa9a/) and create a random dungeon map with JavaScript to experiment some more with RNGs.

## Conclusion

Random Number Generators, or RNGs, are used in many games. In this article, you have learned how and why they are used, and you've seen an example implementation. 

Next time you play a video game, will you be able to spot where a RNG may be used?

