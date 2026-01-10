---
title: J'ai utilisé la programmation pour comprendre comment fonctionne vraiment le
  comptage de cartes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-23T20:54:43.000Z'
originalURL: https://freecodecamp.org/news/i-used-programming-to-figure-out-how-card-counting-really-works-7ecefdb1b8d4
coverImage: https://cdn-media-1.freecodecamp.org/images/0*sTtAxozPICvu9A05.jpg
tags:
- name: coding
  slug: coding
- name: gambling
  slug: gambling
- name: Kotlin
  slug: kotlin
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: J'ai utilisé la programmation pour comprendre comment fonctionne vraiment
  le comptage de cartes
seo_desc: 'By Marcin Moskala

  When I was younger, I loved the movie 21. Great story, acting skills, and obviously
  this inner dream to win huge and beat the casino. I never learned to count cards,
  and I’ve never actually played Blackjack. But I always wanted to c...'
---

Par Marcin Moskala

Quand j'étais plus jeune, j'adorais le film [21](https://en.wikipedia.org/wiki/21_(2008_film)). Une grande histoire, des compétences d'acteur, et évidemment ce rêve intérieur de gagner gros et de battre le casino. Je n'ai jamais appris à compter les cartes, et je n'ai jamais réellement joué au Blackjack. Mais j'ai toujours voulu vérifier si ce comptage de cartes était une vraie chose, ou juste un leurre de casino répandu sur internet grâce à l'argent et aux grands rêves.

Aujourd'hui, je suis programmeur. Comme j'avais un peu de temps libre entre les préparations d'ateliers et le développement de projets, j'ai décidé de enfin révéler la vérité. J'ai donc écrit un programme minimal qui simule le jeu avec comptage de cartes.

Comment l'ai-je fait, et quels ont été les résultats ? Voyons cela.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DZD00vHuupPY5kQo.jpg)

### Modèle

Cela est censé être une implémentation minimale. Si minimale que je n'ai même pas introduit le concept de carte. Les cartes sont représentées par le nombre de points qu'elles valent. Par exemple, un As vaut 11 ou 1.

Le jeu est une liste d'entiers, et nous pouvons le générer comme montré ci-dessous. Lisez-le comme « quatre 10, les nombres de 2 à 9 et un seul 11, le tout 4 fois » :

```kotlin
fun generateDeck(): List<Int> = (List(4) { 10 } + (2..9) + 11) * 4
```

Nous définissons la fonction suivante qui nous permet de multiplier le contenu de `List` :

```kotlin
private operator fun <E> List<E>.times(num: Int) = (1..num).flatMap { this }
```

Le jeu du croupier n'est rien d'autre que 6 jeux mélangés — dans la plupart des casinos :

```kotlin
fun generateDealerDeck() = (generateDeck() * 6).shuffled()
```

### Comptage de cartes

Différentes techniques de comptage de cartes suggèrent différentes façons de compter les cartes. Nous utiliserons la plus populaire, qui évalue une carte à 1 lorsqu'elle est inférieure à 7, -1 pour les dix et les as, et 0 sinon.

Voici l'implémentation de ces règles en [Kotlin](https://kotlinlang.org/) :

```kotlin
fun cardValue(card: Int) = when (card) {
    in 2..6 -> 1
    10, 11 -> -1
    else -> 0
}
```

Nous devons compter toutes les cartes utilisées. Dans la plupart des casinos, nous pouvons voir toutes les cartes qui ont été utilisées.

Dans notre implémentation, il sera plus facile pour nous de compter les points des cartes qui restent dans le jeu et de soustraire ce nombre de 0. Ainsi, l'implémentation peut être `0 - this.sumBy { card -> cardValue(card) }` qui est équivalent à `-this.sumBy { cardValue(it) }` ou `-sumBy(::cardValue)`. C'est la somme des points pour toutes les cartes utilisées.

Ce qui nous intéresse, c'est le soi-disant « True Count », qui est le nombre de points comptés divisé par le nombre de jeux restants. Normalement, le joueur doit estimer ce nombre.

Dans notre implémentation, nous pouvons utiliser un nombre beaucoup plus précis et calculer `trueCount` de cette manière :

```kotlin
fun List<Int>.trueCount(): Int = -sumBy(::cardValue) * 52 / size
```

#### Stratégie de mise

Le joueur doit toujours décider avant le jeu combien d'argent il mise. Basé sur [cet article](http://www.instructables.com/id/Card-Counting-and-Ranging-Bet-Sizes/), j'ai décidé d'utiliser la règle où le joueur calcule son unité de mise — qui est égale à 1/1000 de l'argent qui lui reste. Ensuite, il calcule la mise comme une unité de mise multipliée par le vrai compte moins 1. J'ai également découvert que la mise doit être comprise entre 25 et 1000.

Voici la fonction :

```kotlin
fun getBetSize(trueCount: Int, bankroll: Double): Double {
    val bettingUnit = bankroll / 1000
    return (bettingUnit * (trueCount - 1)).coerceIn(25.0, 1000.0)
}
```

#### Que faire ensuite ?

Il y a une dernière décision pour notre joueur. Dans chaque jeu, le joueur doit prendre certaines actions. Pour prendre des décisions, le joueur doit décider en fonction des informations sur sa main et la carte visible du croupier.

Nous devons représenter la main du joueur et celle du croupier d'une manière ou d'une autre. D'un point de vue mathématique, la main n'est rien d'autre qu'une liste de cartes. Du point de vue du joueur, elle est représentée par des points, le nombre d'as non utilisés si elle peut être divisée, et si c'est un blackjack. D'un point de vue d'optimisation, je préfère calculer toutes ces propriétés une fois et réutiliser les valeurs, car elles sont vérifiées encore et encore.

J'ai donc représenté la main de cette manière :

```kotlin
class Hand private constructor(val cards: List<Int>) {
    val points = cards.sum()
    val unusedAces = cards.count { it == 11 }
    val canSplit = cards.size == 2 && cards[0] == cards[1]
    val blackjack get() = cards.size == 2 && points == 21
}
```

#### As

Il y a un défaut dans cette fonction : que se passe-t-il si nous dépassons 21 et que nous avons encore un As non utilisé ? Nous devons changer l'As de 11 à 1 tant que cela est possible. Mais où cela devrait-il être fait ? Cela pourrait être fait dans le constructeur, mais cela serait très trompeur si quelqu'un définissait la main à partir des cartes 11 et 11 pour avoir les cartes 11 et 1.

Ce comportement devrait être fait dans la méthode de fabrication. Après réflexion, voici comment je l'ai implémenté (il y a aussi l'opérateur plus implémenté) :

```kotlin
class Hand private constructor(val cards: List<Int>) {
    val points = cards.sum()
    val unusedAces = cards.count { it == 11 }
    val canSplit = cards.size == 2 && cards[0] == cards[1]
    val blackjack get() = cards.size == 2 && points == 21

    operator fun plus(card: Int) = Hand.fromCards(cards + card)

    companion object {
        fun fromCards(cards: List<Int>): Hand {
            var hand = Hand(cards)
            while (hand.unusedAces >= 1 && hand.points > 21) {
                hand = Hand(hand.cards - 11 + 1)
            }
            return hand
        }
    }
}
```

Les décisions possibles sont représentées comme une énumération ([enum](https://en.wikipedia.org/wiki/Enumerated_type)) :

```kotlin
enum class Decision { STAND, DOUBLE, HIT, SPLIT, SURRENDER }
```

Il est temps d'implémenter la fonction de décision du joueur. Il existe de nombreuses stratégies pour cela.

J'ai décidé d'utiliser [celle-ci](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/) :

![Image](https://cdn-media-1.freecodecamp.org/images/0*Be3OphVR7yf6dzkx.png)

Je l'ai implémentée en utilisant la fonction suivante. J'ai supposé que le pliage n'est pas autorisé par le casino :

```kotlin
fun decide(hand: Hand, casinoCard: Int, firstTurn: Boolean): Decision = when {
    firstTurn && hand.canSplit && hand.cards[0] == 11 -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] == 9 && casinoCard !in listOf(7, 10, 11) -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] == 8 -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] == 7 && casinoCard <= 7 -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] == 6 && casinoCard <= 6 -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] == 4 && casinoCard in 5..6 -> SPLIT
    firstTurn && hand.canSplit && hand.cards[0] in 2..3 && casinoCard <= 7 -> SPLIT
    hand.unusedAces >= 1 && hand.points >= 19 -> STAND
    hand.unusedAces >= 1 && hand.points == 18 && casinoCard < 9 -> STAND
    hand.points > 16 -> STAND
    hand.points > 12 && casinoCard < 4 -> STAND
    hand.points > 11 && casinoCard in 4..6 -> STAND
    hand.unusedAces >= 1 && casinoCard in 2..6 && hand.points >= 18 -> if (firstTurn) DOUBLE else STAND
    hand.unusedAces >= 1 && casinoCard == 3 && hand.points >= 17 -> if (firstTurn) DOUBLE else HIT
    hand.unusedAces >= 1 && casinoCard == 4 && hand.points >= 15 -> if (firstTurn) DOUBLE else HIT
    hand.unusedAces >= 1 && casinoCard in 5..6 -> if (firstTurn) DOUBLE else HIT
    hand.points == 11 -> if (firstTurn) DOUBLE else HIT
    hand.points == 10 && casinoCard < 10 -> if (firstTurn) DOUBLE else HIT
    hand.points == 9 && casinoCard in 3..6 -> if (firstTurn) DOUBLE else HIT
    else -> HIT
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/0*z7LiE9T-DyO9W2NH.jpg)

#### Jouons !

Tout ce dont nous avons besoin maintenant est une simulation de jeu. Que se passe-t-il dans un jeu ? D'abord, les cartes sont prises et mélangées.

Représentons-les comme une liste mutable :

```kotlin
val cards = generateDealerDeck().toMutableList()
```

Nous aurons besoin de fonctions `pop` pour cela :

```kotlin
fun <T> MutableList<T>.pop(): T = removeAt(lastIndex)
fun <T> MutableList<T>.pop(num: Int): List<T> = (1..num).map { pop() }
```

Nous devons aussi savoir combien d'argent nous avons :

```kotlin
var bankroll = initialMoney
```

Ensuite, nous jouons de manière itérative jusqu'à... jusqu'à quand ? Selon [ce forum](https://www.blackjackinfo.com/community/threads/how-often-does-the-dealer-shuffle.7459/), c'est normalement jusqu'à ce que 75 % des cartes soient utilisées. Ensuite, les cartes sont mélangées, donc nous commençons essentiellement depuis le début.

Nous pouvons donc l'implémenter comme ceci :

```kotlin
val shufflePoint = cards.size * 0.25
while (cards.size > shufflePoint) {
```

Le jeu commence. Le casino prend une seule carte :

```kotlin
val casinoCard = cards.pop()
```

Les autres joueurs prennent également des cartes. Ce sont des cartes brûlées, mais nous les brûlerons plus tard pour laisser le joueur les inclure pendant le calcul des points (les brûler maintenant donnerait au joueur des informations qui ne sont pas vraiment accessibles à ce stade).

Nous prenons également une carte et nous prenons des décisions. Le problème est que nous commençons en tant que joueur unique, mais nous pouvons diviser les cartes et participer en tant que 2 joueurs.

Par conséquent, il est préférable de représenter le jeu comme un processus récursif :

```kotlin
fun playFrom(playerHand: Hand, bet: Double, firstTurn: Boolean): List<Pair<Double, Hand>> =
        when (decide(playerHand, casinoCard, firstTurn)) {
            STAND -> listOf(bet to playerHand)
            DOUBLE -> playFrom(playerHand + cards.pop(), bet * 2, false)
            HIT -> playFrom(playerHand + cards.pop(), bet, false)
            SPLIT -> playerHand.cards.flatMap {
                val newCards = listOf(it, cards.pop())
                val newHand = Hand.fromCards(newCards)
                playFrom(newHand, bet, false)
            }
            SURRENDER -> emptyList()
        }
```

Si nous ne divisons pas, la valeur retournée est toujours une seule mise et une main finale.

Si nous divisons, la liste de deux mises et mains sera retournée. Si nous plions, alors une liste vide est retournée.

Voici comment nous devons démarrer cette fonction :

```kotlin
val betsAndHands = playFrom(
        playerHand = Hand.fromCards(cards.pop(2)),
        bet = getBetSize(cards.trueCount(), bankroll),
        firstTurn = true
)
```

Après cela, le croupier du casino doit jouer son jeu. C'est beaucoup plus simple, car il ne reçoit une nouvelle carte que lorsqu'il a moins de 17 points. Sinon, il tient.

```kotlin
var casinoHand = Hand.fromCards(listOf(casinoCard, cards.pop()))
while (casinoHand.points < 17) {
    casinoHand += cards.pop()
}
```

Ensuite, nous devons comparer nos résultats.

Nous devons le faire pour chaque main séparément :

```kotlin
for ((bet, playerHand) in betsAndHands) {
    when {
        playerHand.blackjack -> bankroll += bet * if (casinoHand.blackjack) 1.0 else 1.5
        playerHand.points > 21 -> bankroll -= bet
        casinoHand.points > 21 -> bankroll += bet
        casinoHand.points > playerHand.points -> bankroll -= bet
        casinoHand.points < playerHand.points -> bankroll += bet
        else -> bankroll -= bet
    }
}
```

Nous pouvons enfin brûler quelques cartes utilisées par les autres joueurs. Disons que nous jouons avec deux autres personnes et qu'elles utilisent 3 cartes en moyenne chacune :

```kotlin
cards.pop(6)
```

C'est tout ! De cette manière, la simulation jouera tout le jeu du croupier et s'arrêtera ensuite.

À ce moment-là, nous pouvons vérifier si nous avons plus ou moins d'argent qu'avant :

```kotlin
val differenceInBankroll = bankroll - initialMoney
return differenceInBankroll
```

La simulation est très rapide. Vous pouvez faire des milliers de simulations en quelques secondes. De cette manière, vous pouvez facilement calculer le résultat moyen :

```kotlin
(1..10000).map { simulate() }.average().let(::print)
```

Commencez avec cet algorithme et amusez-vous. Ici, vous pouvez jouer avec le code en ligne :

[**Blackjack**](https://try.kotlinlang.org/#/UserProjects/l7skht95bhqsih73fag4bl623v/ljsmfeic0savbgva6qa6nocjb0)  
[_Kotlin directement dans le navigateur._try.kotlinlang.org](https://try.kotlinlang.org/#/UserProjects/l7skht95bhqsih73fag4bl623v/ljsmfeic0savbgva6qa6nocjb0)

### Résultats

Malheureusement, mon joueur simulé perd toujours de l'argent. Beaucoup moins qu'un joueur standard, mais ce comptage n'a pas suffisamment aidé. Peut-être que j'ai manqué quelque chose. Ce n'est pas ma discipline.

Corrigez-moi si je me trompe ;) Pour l'instant, tout ce comptage de cartes semble être une énorme arnaque. Peut-être que ce site présente simplement un mauvais algorithme. Bien que ce soit l'algorithme le plus populaire que j'ai trouvé !

Ces résultats peuvent expliquer pourquoi, même si des techniques de comptage de cartes sont connues depuis des années — et que tous ces films ont été produits (comme 21) — les casinos du monde entier offrent toujours le Blackjack avec tant de bonheur.

Je crois qu'ils savent (peut-être que c'est même mathématiquement prouvé) que la seule façon de gagner contre un casino est de ne pas jouer du tout. Comme dans presque tous les autres jeux de hasard.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wJKLFeo872PKNVnj.jpg)

### À propos de l'auteur

[Marcin Moskała](http://marcinmoskala.com/) ([@marcinmoskala](https://twitter.com/marcinmoskala)) est un formateur et consultant, se concentrant actuellement sur la formation Kotlin pour Android et les ateliers Kotlin avancés ([formulaire de contact pour postuler pour votre équipe](https://marcinmoskala.typeform.com/to/iwKnN9)). Il est également un [conférencier](https://www.youtube.com/results?search_query=Marcin+Moska%C5%82a), auteur d'[articles](https://medium.com/@marcinmoskala) et d'[un livre](https://www.packtpub.com/application-development/android-development-kotlin) sur le développement Android en Kotlin.