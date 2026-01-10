---
title: I used programming to figure out how card counting really works
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
seo_title: null
seo_desc: 'By Marcin Moskala

  When I was younger, I loved the movie 21. Great story, acting skills, and obviously
  this inner dream to win huge and beat the casino. I never learned to count cards,
  and I’ve never actually played Blackjack. But I always wanted to c...'
---

By Marcin Moskala

When I was younger, I loved the movie [21](https://en.wikipedia.org/wiki/21_(2008_film)). Great story, acting skills, and obviously this inner dream to win huge and beat the casino. I never learned to count cards, and I’ve never actually played Blackjack. But I always wanted to check if this card counting was a real thing, or just a casino’s decoy splashed on the internet thanks to big money and big dreams.

Today I am programmer. Since I had some extra time between workshop preparations and project development, I decided to finally reveal the truth. So I wrote a minimal program that simulates gameplay with card counting.

How did I do it, and what were the results? Let’s see.

![Image](https://cdn-media-1.freecodecamp.org/images/0*DZD00vHuupPY5kQo.jpg)

### Model

This is supposed to be a minimal implementation. So minimal that I haven’t even introduced the concept of a card. Cards are represented by the number of points they evaluate to. For example, an Ace is 11 or 1.

The deck is a list of integers, and we can generate it as shown below. Read it as “four 10, number from 2 to 9 and single 11, everything 4 times”:

```kotlin
fun generateDeck(): List<Int> = (List(4) { 10 } + (2..9) + 11) * 4
```

We define the following function that let’s us multiply the contents of `List`:

```kotlin
private operator fun <E> List<E>.times(num: Int) = (1..num).flatMap { this }
```

The dealer’s deck is nothing but 6 decks shuffled — in most casinos:

```kotlin
fun generateDealerDeck() = (generateDeck() * 6).shuffled()

```

### Card counting

Different card counting techniques suggest different ways to count cards. We will use the most popular one, which evaluates a card as 1 when smaller then 7, -1 for tens and aces, and 0 otherwise.

This is the [Kotlin](https://kotlinlang.org/) implementation of these rules:

```kotlin
fun cardValue(card: Int) = when (card) {
    in 2..6 -> 1
    10, 11 -> -1
    else -> 0
}
```

We need to count all used cards. In most casinos, we can see all the cards that were used.

In our implementation, it will be easier for us to count points from cards that are left in the deck and subtract this number from 0. So the implementation can be `0 — this.sumBy { card -> cardValue(card`) } which is an equivalent `of -this.sumBy { cardValue(it`) } `o_r -su_mBy(::cardVal`ue). This is the sum of points for all used cards.

What we are interested in is the so-called “True Count”, which is the number of counted points divided by the number of decks that are left. Normally the player needs to estimate this number.

In our implementation, we can use a much more accurate number and calculate `trueCount` this way:

```kotlin
fun List<Int>.trueCount(): Int = -sumBy(::cardValue) * 52 / size

```

#### Betting Strategy

The player always has to decide before the game how much money they bet. Based on [this article](http://www.instructables.com/id/Card-Counting-and-Ranging-Bet-Sizes/), I decided to use the rule where the player calculates their betting unit — which is equal to 1/1000 of their money left. Then they calculate the bet as a betting unit times the true count minus 1. I also found out that the bet needs to be between 25 and 1000.

Here is the function:

```kotlin
fun getBetSize(trueCount: Int, bankroll: Double): Double {
    val bettingUnit = bankroll / 1000
    return (bettingUnit * (trueCount - 1)).coerceIn(25.0, 1000.0)
}
```

#### What to do next?

There is one final decision for our player. In every game, player needs to make some actions. To make decisions, the player needs to decide based on the information about their hand and the dealer’s visible card.

We need to represent player and dealer hands somehow. From a mathematical point of view, the hand is nothing else but a list of cards. From the player’s point of view, it is represented by points, the number of unused aces if it can be split, and if it is a blackjack. From the optimization point of view, I prefer to calculate all these properties once and reuse the values, since they are checked over and over again.

So I represented the hand this way:

```kotlin
class Hand private constructor(val cards: List<Int>) {
    val points = cards.sum()
    val unusedAces = cards.count { it == 11 }
    val canSplit = cards.size == 2 && cards[0] == cards[1]
    val blackjack get() = cards.size == 2 && points == 21
}
```

#### Aces

There is one flaw in this function: what if we pass 21 and we still have an unused Ace? We need to change the Ace from 11 to 1 as long as this is possible. But where should this be done? It could be done in the constructor, but it would be highly misleading if someone set the hand from cards 11 and 11 to have cards 11 and 1.

This behavior should be done in the factory method. After some consideration, this is how I implemented it (there is also plus operator implemented):

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

Possible decisions are represented as an enumeration ([enum](https://en.wikipedia.org/wiki/Enumerated_type)):

```kotlin
enum class Decision { STAND, DOUBLE, HIT, SPLIT, SURRENDER }

```

Time to implement the player’s decision function. There are numerous strategies for that.

I decided to use [this one](https://www.blackjackapprenticeship.com/blackjack-strategy-charts/):

![Image](https://cdn-media-1.freecodecamp.org/images/0*Be3OphVR7yf6dzkx.png)

I implemented it using the following function. I assumed that folding is not allowed by the casino:

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

#### Let’s Play!

All we need now is a game simulation. What happens in a game? First, cards are taken and shuffled.

Let’s represent them as a mutable list:

```kotlin
val cards = generateDealerDeck().toMutableList()

```

We will need `pop` functions for it:

```kotlin
fun <T> MutableList<T>.pop(): T = removeAt(lastIndex)
fun <T> MutableList<T>.pop(num: Int): List<T> = (1..num).map { pop() }
```

We also need to know how much money do we have:

```kotlin
var bankroll = initialMoney
```

Then we play iteratively until … until when? According to [this forum](https://www.blackjackinfo.com/community/threads/how-often-does-the-dealer-shuffle.7459/), it is normally until 75% of cards are used. Then cards are shuffled, so we basically start from the beginning.

So we can implement it like that:

```kotlin
val shufflePoint = cards.size * 0.25
while (cards.size > shufflePoint) {
```

The game starts. The casino takes single card:

```kotlin
val casinoCard = cards.pop()
```

Other players take cards as well. These are burned cards, but we will burn them later to let the player now include them during the points calculation (burning them now would give player information that is not really accessible at this point).

We also take a card and we make decisions. The problem is that we start as a single player, but we can split cards and attend as 2 players.

Therefore, it is better to represent gameplay as a recursive process:

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

If we don’t split, the returned value is always a single bet and a final hand.

If we split, the list of two bets and hands will be returned. If we fold, then an empty list is returned.

This is how we should start this function:

```kotlin
val betsAndHands = playFrom(
        playerHand = Hand.fromCards(cards.pop(2)),
        bet = getBetSize(cards.trueCount(), bankroll),
        firstTurn = true
)
```

After that, the casino dealer needs to play their game. It is much simpler, because they only get a new card when they have less then 17 points. Otherwise he holds.

```kotlin
var casinoHand = Hand.fromCards(listOf(casinoCard, cards.pop()))
while (casinoHand.points < 17) {
    casinoHand += cards.pop()
}
```

Then we need to compare our results.

We need to do it for every hand separately:

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

We can finally burn some cards used by other players. Let’s say that we play with two other people and they use 3 cards on average each:

```kotlin
cards.pop(6)
```

That’s it! This way the simulation will play the whole dealer’s deck and then it will stop.

At this moment, we can check out if we have more or less money then before:

```kotlin
val differenceInBankroll = bankroll - initialMoney
return differenceInBankroll
```

The simulation is very fast. You can make thousands of simulations in seconds. This way you can easily calculate the average result:

```kotlin
(1..10000).map { simulate() }.average().let(::print)
```

Start with this algorithm and have fun. Here you can play with the code online:

[**Blackjack**](https://try.kotlinlang.org/#/UserProjects/l7skht95bhqsih73fag4bl623v/ljsmfeic0savbgva6qa6nocjb0)  
[_Kotlin right in the browser._try.kotlinlang.org](https://try.kotlinlang.org/#/UserProjects/l7skht95bhqsih73fag4bl623v/ljsmfeic0savbgva6qa6nocjb0)

### Results

Sadly my simulated player still loses money. Much less than a standard player, but this counting didn’t help enough. Maybe I missed something. This is not my discipline.

Correct me if I am wrong ;) For now, this whole card-counting looks like a huge scam. Maybe this website just presents a bad algorithm. Although this is the most popular algorithm I found!

These results might explain why even though there have been known card-counting techniques for years — and all these movies were produced (like 21) — casinos around the world still offer Blackjack so happily.

I believe that they know (maybe it is even mathematically proven) that the only way to win with a casino is to not play at all. Like in nearly every other hazard game.

![Image](https://cdn-media-1.freecodecamp.org/images/0*wJKLFeo872PKNVnj.jpg)

### About the author

[Marcin Moskała](http://marcinmoskala.com/) ([@marcinmoskala](https://twitter.com/marcinmoskala)) is a trainer and consultant, currently concentrating on giving Kotlin in Android and advanced Kotlin workshops ([contact form to apply for your team](https://marcinmoskala.typeform.com/to/iwKnN9)). He is also a [speaker](https://www.youtube.com/results?search_query=Marcin+Moska%C5%82a), author of [articles](https://medium.com/@marcinmoskala) and [a book](https://www.packtpub.com/application-development/android-development-kotlin) about Android development in Kotlin.

