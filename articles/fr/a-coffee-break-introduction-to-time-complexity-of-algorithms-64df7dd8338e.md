---
title: Une introduction pendant la pause-café à la complexité temporelle des algorithmes
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2018-06-04T23:44:40.000Z'
originalURL: https://freecodecamp.org/news/a-coffee-break-introduction-to-time-complexity-of-algorithms-64df7dd8338e
coverImage: https://cdn-media-1.freecodecamp.org/images/1*_YsSsyFQ5sgS8F0kiZ1USA.png
tags:
- name: algorithms
  slug: algorithms
- name: learning
  slug: learning
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Une introduction pendant la pause-café à la complexité temporelle des algorithmes
seo_desc: Just like writing your very first for loop, understanding time complexity
  is an integral milestone to learning how to write efficient complex programs. Think
  of it as having a superpower that allows you to know exactly what type of program
  might be t...
---

Tout comme écrire votre toute première boucle `for`, comprendre la complexité temporelle est une étape intégrale pour apprendre à écrire des programmes complexes efficaces. Considérez cela comme avoir un superpouvoir qui vous permet de savoir exactement quel type de programme pourrait être le plus efficace dans une situation particulière — avant même d'exécuter une seule ligne de code.

Les concepts fondamentaux de l'analyse de complexité valent bien la peine d'être étudiés. Vous serez en mesure de mieux comprendre comment le code que vous écrivez interagira avec les entrées du programme, et par conséquent, vous passerez beaucoup moins de temps à écrire du code lent et problématique.

Il ne faudra pas longtemps pour passer en revue tout ce que vous devez savoir afin de commencer à écrire des programmes plus efficaces — en fait, nous pouvons le faire en environ quinze minutes. Vous pouvez aller chercher un café tout de suite (ou du thé, si c'est votre truc) et je vous guiderai à travers cela avant que votre pause-café ne soit terminée. Allez-y, je vous attends.

Tout est prêt ? C'est parti !

### Qu'est-ce que la « complexité temporelle » après tout ?

La complexité temporelle d'un algorithme est une **approximation** de la durée que cet algorithme mettra pour traiter une certaine entrée. Elle décrit l'efficacité de l'algorithme par l'ampleur de ses opérations. Cela est différent du nombre de fois qu'une opération se répète. Je développerai cela plus tard. Généralement, moins l'algorithme a d'opérations, plus il sera rapide.

Nous écrivons sur la complexité temporelle en utilisant la [notation Big O](https://en.wikipedia.org/wiki/Big_O_notation), qui ressemble à quelque chose comme _O_(_n_). Il y a plutôt beaucoup de mathématiques impliquées dans sa définition formelle, mais informellement nous pouvons dire que la notation Big O nous donne le temps d'exécution approximatif de notre algorithme dans le **pire des cas**, ou en d'autres termes, sa borne supérieure. Elle est intrinsèquement relative et comparative.

Nous décrivons l'efficacité de l'algorithme par rapport à la taille croissante de ses données d'entrée, _n_. Si l'entrée est une chaîne de caractères, alors _n_ est la longueur de la chaîne. Si c'est une liste d'entiers, _n_ est la longueur de la liste.

Il est plus facile de visualiser ce que représente la notation Big O avec un graphique :

![Image](https://cdn-media-1.freecodecamp.org/images/05O9lIJ7IskYF05LomQMNSdgLSxE4qhY3xef)
_Lignes réalisées avec la très excellente calculatrice graphique Desmos. Vous pouvez [jouer avec ce graphique ici](https://www.desmos.com/calculator/xpfyjl1lbn" rel="noopener" target="_blank" title=")._

Voici les principaux points importants à retenir lors de la lecture du reste de cet article :

* La complexité temporelle est une approximation
* La complexité temporelle d'un algorithme approxime son temps d'exécution dans le pire des cas

### Détermination de la complexité temporelle

Il existe différentes classes de complexité que nous pouvons utiliser pour comprendre rapidement un algorithme. J'illustrerai certaines de ces classes à l'aide de boucles imbriquées et d'autres exemples.

### Complexité temporelle polynomiale

Un **polynôme**, du grec _poly_ signifiant « plusieurs », et du latin _nomen_ signifiant « nom », décrit une expression composée de variables constantes, et d'addition, de multiplication, et d'exponentiation à une puissance entière non négative. C'est une manière très mathématique de dire qu'il contient des variables généralement désignées par des lettres, et des symboles qui ressemblent à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/dzjaOr9FE89dYVE5ZlQ5Ddb28xOGZT3vQ8La)

Les classes suivantes décrivent des algorithmes polynomiaux. Certaines ont des exemples alimentaires.

#### Constante

Un algorithme à **temps constant** ne change pas son temps d'exécution en réponse aux données d'entrée. Peu importe la taille des données qu'il reçoit, l'algorithme met le même temps à s'exécuter. Nous désignons cela par une complexité temporelle de _O_(1).

![Image](https://cdn-media-1.freecodecamp.org/images/xgqMQNEOKLYBDBCXNQ4RJBhTUMwKVTgMOt4K)

Voici un exemple d'algorithme constant qui prend le premier élément d'une tranche.

```
func takeCupcake(cupcakes []int) int {
	return cupcakes[0]
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/5Ypub2bQrF6lf4s20VkNpK178mhMLZTNOGZP)
_Le choix des saveurs est : cupcake vanille, cupcake fraise, cupcake chocolat menthe, cupcake citron, et cupcake « wibbly wobbly, timey wimey »._

Avec cet algorithme à temps constant, peu importe le nombre de cupcakes proposés, vous obtenez simplement le premier. Tant pis. Les saveurs sont surévaluées de toute façon.

#### Linéaire

La durée d'exécution d'un algorithme **linéaire** est constante. Il traitera l'entrée en _n_ nombre d'opérations. C'est souvent le meilleur cas possible (le plus efficace) pour la complexité temporelle où toutes les données doivent être examinées.

![Image](https://cdn-media-1.freecodecamp.org/images/EZDOxe5ylKG0rg0H3YRAlTwXp-htTL3RF1pj)

Voici un exemple de code avec une complexité temporelle de _O_(_n_) :

```js
func eatChips(bowlOfChips int) {
	for chip := 0; chip <= bowlOfChips; chip++ {
		// tremper la puce
	}
}
```

Voici un autre exemple de code avec une complexité temporelle de _O_(_n_) :

```js
func eatChips(bowlOfChips int) {
	for chip := 0; chip <= bowlOfChips; chip++ {
		// double tremper la puce
	}
}
```

Peu importe que le code à l'intérieur de la boucle s'exécute une, deux ou un nombre quelconque de fois. Ces deux boucles traitent l'entrée par un facteur constant de _n_, et peuvent donc être décrites comme linéaires.

![Image](https://cdn-media-1.freecodecamp.org/images/c2mTyNEzt4zCa1lqqlOjxSgFyYpxPBDy7oRH)
_Ne double trempez pas dans un bol partagé._

#### Quadratique

![Image](https://cdn-media-1.freecodecamp.org/images/AAOdoTdm2s3fuBxrIw9w1r4iGv9xMs3MFXRy)

Voici maintenant un exemple de code avec une complexité temporelle de _O_(_n_2) :

```js
func pizzaDelivery(pizzas int) {
	for pizza := 0; pizza <= pizzas; pizza++ {
		// couper la pizza
		for slice := 0; slice <= pizza; slice++ {
			// manger une part de pizza
		}
	}
}
```

Parce qu'il y a deux boucles imbriquées, ou des opérations linéaires imbriquées, l'algorithme traite l'entrée _n_2 fois.

#### Cubique

![Image](https://cdn-media-1.freecodecamp.org/images/gCSUwDt1nmJSrTicLxlldqXdH9F0zIHurMN8)

En étendant l'exemple précédent, ce code avec trois boucles imbriquées a une complexité temporelle de _O_(_n_3) :

```js
func pizzaDelivery(boxesDelivered int) {
	for pizzaBox := 0; pizzaBox <= boxesDelivered; pizzaBox++ {
		// ouvrir la boîte
		for pizza := 0; pizza <= pizzaBox; pizza++ {
			// couper la pizza
			for slice := 0; slice <= pizza; slice++ {
				// manger une part de pizza
			}
		}
	}
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/f1h7-yXidgFQESdRK00WNgc-CuXwAQ0BGeGr)
_Sérieusement, qui livre des pizzas non coupées ??_

#### Logarithmique

Un algorithme **logarithmique** est celui qui réduit la taille de l'entrée à chaque étape. Nous désignons cette complexité temporelle par _O_(log _n_), où **log**, la fonction logarithme, a cette forme :

![Image](https://cdn-media-1.freecodecamp.org/images/EFk5xco9PMY-q6Kjv0ZcBq0Fm3PicLRY6CvO)

Un exemple de cela est un [algorithme de recherche binaire](https://en.wikipedia.org/wiki/Binary_search_algorithm) qui trouve la position d'un élément dans un tableau trié. Voici comment cela fonctionnerait, en supposant que nous essayons de trouver l'élément _x_ :

1. Si _x_ correspond à l'élément du milieu _m_ du tableau, retourner la position de _m_.
2. Si _x_ ne correspond pas à _m_, voir si _m_ est plus grand ou plus petit que _x_. Si plus grand, ignorer tous les éléments du tableau supérieurs à _m_. Si plus petit, ignorer tous les éléments du tableau inférieurs à _m_.
3. Continuer en répétant les étapes 1 et 2 sur le tableau restant jusqu'à ce que _x_ soit trouvé.

Je trouve l'analogie la plus claire pour comprendre la recherche binaire est d'imaginer le processus de localisation d'un livre dans une allée de librairie. Si les livres sont organisés par le nom de famille de l'auteur et que vous voulez trouver « Terry Pratchett », vous savez que vous devez chercher dans la section « P ».

Vous pouvez vous approcher de l'étagère à n'importe quel point le long de l'allée et regarder le nom de famille de l'auteur à cet endroit. Si vous regardez un livre de Neil Gaiman, vous savez que vous pouvez ignorer tous les autres livres à votre gauche, puisque aucune des lettres qui viennent avant « G » dans l'alphabet ne se trouve être « P ». Vous vous déplaceriez ensuite le long de l'allée vers la droite d'une certaine quantité, et répéteriez ce processus jusqu'à ce que vous ayez trouvé la section Terry Pratchett, qui devrait être plutôt grande si vous êtes dans une bonne librairie, car il a écrit beaucoup de livres.

#### `Quasilinéaire`

![Image](https://cdn-media-1.freecodecamp.org/images/MtnuvO9ik8A-53LShA7IabhvmsWaIpI7nAZs)

Souvent vu avec des algorithmes de tri, la complexité temporelle _O_(_n_ log _n_) peut décrire une structure de données où chaque opération prend _O_(log _n_) temps. Un exemple de cela est [quick sort](https://en.wikipedia.org/wiki/Quicksort), un algorithme de type diviser-pour-régner.

Quick sort fonctionne en divisant un tableau non trié en morceaux plus petits qui sont plus faciles à traiter. Il trie les sous-tableaux, et ainsi le tableau entier. Pensez à cela comme essayer de mettre un jeu de cartes en ordre. C'est plus rapide si vous divisez les cartes et que vous avez cinq amis pour vous aider.

### Complexité temporelle non polynomiale

Les classes d'algorithmes suivantes sont non polynomiales.

#### Factorielle

![Image](https://cdn-media-1.freecodecamp.org/images/9qJwzt9mivXPNJ3paXniaID4t3nYVVKyfMVc)

Un algorithme avec une complexité temporelle _O_(_n_!) itère souvent à travers toutes les permutations des éléments d'entrée. Un exemple courant est une [recherche par force brute](https://en.wikipedia.org/wiki/Brute-force_search), vue dans le [problème du voyageur de commerce](https://en.wikipedia.org/wiki/Travelling_salesman_problem#Computing_a_solution). Il essaie de trouver le chemin le moins coûteux entre un certain nombre de points en énumérant toutes les permutations possibles et en trouvant celles avec le coût le plus bas.

#### Exponentielle

Un algorithme **exponentiel** itère souvent également à travers tous les sous-ensembles des éléments d'entrée. Il est désigné par _O_(2_n_) et est souvent vu dans les algorithmes de force brute. Il est similaire au temps factoriel sauf dans son taux de croissance, qui, comme vous ne serez peut-être pas surpris de l'apprendre, est exponentiel. Plus l'ensemble de données est grand, plus la courbe devient raide.

![Image](https://cdn-media-1.freecodecamp.org/images/EypghHiSZPBip2XdnBuygTC3GeAmFeAym9EJ)

En cryptographie, une attaque par force brute peut vérifier systématiquement tous les éléments possibles d'un mot de passe en itérant à travers des sous-ensembles. En utilisant un algorithme exponentiel pour cela, il devient incroyablement coûteux en ressources de craquer par force brute un mot de passe long par rapport à un plus court. C'est une des raisons pour lesquelles un mot de passe long est considéré comme plus sécurisé qu'un plus court.

Il existe d'autres classes de complexité temporelle moins couramment vues que je ne couvrirai pas ici, mais vous pouvez lire à leur sujet et trouver des exemples dans [ce tableau pratique](https://en.wikipedia.org/wiki/Time_complexity#Table_of_common_time_complexities).

### Complexité temporelle de la récursivité

Comme je l'ai décrit dans mon article [expliquant la récursivité en utilisant une tarte aux pommes](https://vickylai.com/verbose/reduce-recursion-with-pie), une fonction récursive s'appelle elle-même sous des conditions spécifiées. Sa complexité temporelle dépend du nombre de fois où la fonction est appelée et de la complexité temporelle d'un seul appel de fonction. En d'autres termes, c'est le produit du nombre de fois où la fonction s'exécute et de la complexité temporelle d'une seule exécution.

Voici une fonction récursive qui mange des tartes jusqu'à ce qu'il n'en reste plus :

```
func eatPies(pies int) int {
	if pies == 0 {
		return pies
	}
	return eatPies(pies - 1)
}
```

La complexité temporelle d'une seule exécution est constante. Peu importe le nombre de tartes en entrée, le programme fera la même chose : vérifier si l'entrée est 0. Si oui, retourner, et si non, s'appeler elle-même avec une tarte en moins.

Le nombre initial de tartes pourrait être n'importe quel nombre, et nous devons toutes les traiter, donc nous pouvons décrire l'entrée comme _n_. Ainsi, la complexité temporelle de cette fonction récursive est le produit _O_(_n_).

![Image](https://cdn-media-1.freecodecamp.org/images/nTl7cFkAtXJFXY1J9pXTJ1GGuR87zhgNTO6D)
_La valeur de retour de cette fonction est zéro, plus une certaine indigestion._

### Complexité temporelle dans le pire des cas

Jusqu'à présent, nous avons parlé de la complexité temporelle de quelques boucles imbriquées et de certains exemples de code. Cependant, la plupart des algorithmes sont construits à partir de nombreuses combinaisons de ces éléments. Comment déterminons-nous la complexité temporelle d'un algorithme contenant beaucoup de ces éléments enchaînés ?

Facile. Nous pouvons décrire la complexité temporelle totale de l'algorithme en trouvant la plus grande complexité parmi toutes ses parties. Cela est dû au fait que la partie la plus lente du code est le goulot d'étranglement, et la complexité temporelle est concernée par la description du pire cas pour le temps d'exécution de l'algorithme.

Supposons que nous avons un programme pour une fête de bureau. Si notre programme ressemble à ceci :

```js
package main

import "fmt"

func takeCupcake(cupcakes []int) int {
	fmt.Println("Have cupcake number",cupcakes[0])
	return cupcakes[0]
}

func eatChips(bowlOfChips int) {
	fmt.Println("Have some chips!")
	for chip := 0; chip <= bowlOfChips; chip++ {
		// dip chip
	}
	fmt.Println("No more chips.")
}

func pizzaDelivery(boxesDelivered int) {
	fmt.Println("Pizza is here!")
	for pizzaBox := 0; pizzaBox <= boxesDelivered; pizzaBox++ {
		// open box
		for pizza := 0; pizza <= pizzaBox; pizza++ {
			// slice pizza
			for slice := 0; slice <= pizza; slice++ {
				// eat slice of pizza
			}
		}
	}
	fmt.Println("Pizza is gone.")
}

func eatPies(pies int) int {
	if pies == 0 {
		fmt.Println("Someone ate all the pies!")
		return pies
	}
	fmt.Println("Eating pie...")
	return eatPies(pies - 1)
}

func main() {
	takeCupcake([]int{1, 2, 3})
	eatChips(23)
	pizzaDelivery(3)
	eatPies(3)
	fmt.Println("Food gone. Back to work!")
}
```

Nous pouvons décrire la complexité temporelle de tout le code par la complexité de sa partie la plus complexe. Ce programme est composé de fonctions que nous avons déjà vues, avec les classes de complexité temporelle suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/azvMui-3KR6nAf4wlnKCpTelyz8F7scfqSaA)

Pour décrire la complexité temporelle de l'ensemble du programme de la fête de bureau, nous choisissons le pire des cas. Ce programme aurait la complexité temporelle _O_(_n_3).

Voici la bande-son de la fête de bureau, juste pour le plaisir.

```
Have cupcake number 1
Have some chips!
No more chips.
Pizza is here!
Pizza is gone.
Eating pie...
Eating pie...
Eating pie...
Someone ate all the pies!
Food gone. Back to work!
```

### P vs NP, NP-complet et NP-difficile

Vous pourriez rencontrer ces termes dans vos explorations de la complexité temporelle. Informellement, **P** (pour temps Polynomial), est une classe de problèmes qui est rapide à résoudre. **NP**, pour temps Polynomial Non-déterministe, est une classe de problèmes où la réponse peut être rapidement vérifiée en temps polynomial. NP englobe P, mais aussi une autre classe de problèmes appelée **NP-complet**, pour laquelle aucune solution rapide n'est connue. En dehors de NP, mais incluant toujours NP-complet, se trouve une autre classe appelée **NP-difficile**, qui inclut des problèmes que personne n'a été en mesure de résoudre de manière vérifiable avec des algorithmes polynomiaux.

![Image](https://cdn-media-1.freecodecamp.org/images/n7lVeNIYOP0ZgGmoc8Uj5EBt6yizJQkuNnAJ)
_Diagramme d'Euler P vs NP, [par Behnam Esfahbod, CC BY-SA 3.0](https://commons.wikimedia.org/w/index.php?curid=3532181" rel="noopener" target="_blank" title=")_

[P versus NP](https://en.wikipedia.org/wiki/P_versus_NP_problem) est une question ouverte et non résolue en informatique.

En tout cas, vous n'avez généralement pas besoin de connaître les problèmes NP et NP-difficiles pour commencer à tirer parti de la compréhension de la complexité temporelle. Ce sont une toute autre boîte de Pandore.

### Approximer l'efficacité d'un algorithme avant d'écrire le code

Jusqu'à présent, nous avons identifié certaines classes de complexité temporelle différentes et comment nous pourrions déterminer à laquelle un algorithme appartient. Comment cela nous aide-t-il avant d'avoir écrit du code à évaluer ?

En combinant un peu de connaissances sur la complexité temporelle avec une conscience de la taille de nos données d'entrée, nous pouvons faire une estimation d'un algorithme efficace pour traiter nos données dans une contrainte de temps donnée. Nous pouvons baser notre estimation sur le fait qu'un ordinateur moderne peut effectuer quelques centaines de millions d'opérations en une seconde. Le tableau suivant du manuel du programmeur compétitif offre quelques estimations sur la complexité temporelle requise pour traiter la taille d'entrée respective dans une limite de temps d'une seconde.

![Image](https://cdn-media-1.freecodecamp.org/images/BLsvB66DYy8bOZokzIvje8l5Hnvq9l6M-8sw)

Gardez à l'esprit que la complexité temporelle est une approximation, et non une garantie. Nous pouvons économiser beaucoup de temps et d'efforts en éliminant immédiatement les conceptions d'algorithmes qui sont peu susceptibles de convenir à nos contraintes, mais nous devons également considérer que la notation Big O ne tient pas compte des **facteurs constants**. Voici du code pour illustrer.

Les deux algorithmes suivants ont tous deux une complexité temporelle de _O_(_n_).

```
func makeCoffee(scoops int) {
	for scoop := 0; scoop <= scoops; scoop++ {
		// add instant coffee
	}
}
func makeStrongCoffee(scoops int) {
	for scoop := 0; scoop <= 3*scoops; scoop++ {
		// add instant coffee
	}
}
```

La première fonction prépare une tasse de café avec le nombre de cuillères que nous demandons. La deuxième fonction prépare également une tasse de café, mais elle triple le nombre de cuillères que nous demandons. Pour voir un exemple illustratif, demandons à ces deux fonctions une tasse de café avec un million de cuillères.

Voici le résultat du test Go :

```
Benchmark_makeCoffee-4          1000000000             0.29 ns/op
Benchmark_makeStrongCoffee-4    1000000000             0.86 ns/op
```

Notre première fonction, `makeCoffee`, s'est exécutée en moyenne en 0,29 nanosecondes. Notre deuxième fonction, `makeStrongCoffee`, s'est exécutée en moyenne en 0,86 nanosecondes. Bien que ces deux nombres puissent sembler assez petits, considérons que le café plus fort a pris près de trois fois plus de temps à préparer. Cela devrait avoir du sens intuitivement, puisque nous lui avons demandé de tripler les cuillères. La notation Big O seule ne vous dirait pas cela, puisque le facteur constant des cuillères triplées n'est pas pris en compte.

### Améliorer la complexité temporelle du code existant

Devenir familier avec la complexité temporelle nous donne l'opportunité d'écrire du code, ou de refactoriser du code, pour qu'il soit plus efficace. Pour illustrer, je vais donner un exemple concret d'une manière dont nous pouvons refactoriser un peu de code pour améliorer sa complexité temporelle.

Supposons qu'un groupe de personnes au bureau veulent de la tarte. Certaines personnes veulent plus de tarte que d'autres. La quantité que tout le monde veut de la tarte est représentée par un `int` > 0 :

```
diners := []int{2, 88, 87, 16, 42, 10, 34, 1, 43, 56}
```

Malheureusement, nous sommes en démarrage et il n'y a que trois fourchettes à partager. Puisque nous sommes un groupe coopératif, les trois personnes qui veulent le plus de tarte recevront les fourchettes pour la manger. Même s'ils ont tous convenu de cela, personne ne semble vouloir se trier et se mettre en ligne de manière ordonnée, donc nous devrons nous contenter de tout le monde mélangé.

Sans trier la liste des convives, retourner les trois plus grands entiers dans la tranche.

Voici une fonction qui résout ce problème et a une complexité temporelle de _O_(_n_2) :

```js
func giveForks(diners []int) []int {
	// make a slice to store diners who will receive forks
	var withForks []int
	// loop over three forks
	for i := 1; i <= 3; i++ {
		// variables to keep track of the highest integer and where it is
		var max, maxIndex int
		// loop over the diners slice
		for n := range diners {
			// if this integer is higher than max, update max and maxIndex
			if diners[n] > max {
				max = diners[n]
				maxIndex = n
			}
		}
		// remove the highest integer from the diners slice for the next loop
		diners = append(diners[:maxIndex], diners[maxIndex+1:]...)
		// keep track of who gets a fork
		withForks = append(withForks, max)
	}
	return withForks
}
```

Ce programme fonctionne, et retourne finalement les convives `[88 87 56]`. Tout le monde devient un peu impatient pendant son exécution, car il prend plutôt longtemps (environ 120 nanosecondes) juste pour distribuer trois fourchettes, et la tarte refroidit. Comment pourrions-nous l'améliorer ?

En réfléchissant à notre approche d'une manière légèrement différente, nous pouvons refactoriser ce programme pour qu'il ait une complexité temporelle de _O_(_n_) :

```js
func giveForks(diners []int) []int {
	// make a slice to store diners who will receive forks
	var withForks []int
	// create variables for each fork
	var first, second, third int
	// loop over the diners
	for i := range diners {
		// assign the forks
		if diners[i] > first {
			third = second
			second = first
			first = diners[i]
		} else if diners[i] > second {
			third = second
			second = diners[i]
		} else if diners[i] > third {
			third = diners[i]
		}
	}
	// list the final result of who gets a fork
	withForks = append(withForks, first, second, third)
	return withForks
}
```

Voici comment fonctionne le nouveau programme :

Initialement, le convive `2` (le premier de la liste) se voit attribuer la fourchette `first`. Les autres fourchettes restent non attribuées.

Ensuite, le convive `88` se voit attribuer la première fourchette à la place. Le convive `2` obtient la fourchette `second`.

Le convive `87` n'est pas plus grand que `first` qui est actuellement `88`, mais il est plus grand que `2` qui a la fourchette `second`. Donc, la fourchette `second` va à `87`. Le convive `2` obtient la fourchette `third`.

En continuant cet échange violent et rapide de fourchettes, le convive `16` se voit ensuite attribuer la fourchette `third` au lieu de `2`, et ainsi de suite.

Nous pouvons ajouter une instruction d'impression dans la boucle pour voir comment se déroulent les attributions de fourchettes :

```
0 0 0
2 0 0
88 2 0
88 87 2
88 87 16
88 87 42
88 87 42
88 87 42
88 87 42
88 87 43
[88 87 56]
```

Ce programme est beaucoup plus rapide, et toute la lutte épique pour la domination des fourchettes est terminée en 47 nanosecondes.

Comme vous pouvez le voir, avec un petit changement de perspective et un peu de refactorisation, nous avons rendu ce simple morceau de code plus rapide et plus efficace.

Eh bien, il semble que notre pause-café de quinze minutes soit terminée ! J'espère vous avoir donné une introduction complète au calcul de la complexité temporelle. Il est temps de retourner au travail, en appliquant idéalement vos nouvelles connaissances pour écrire du code plus efficace ! Ou peut-être simplement pour avoir l'air intelligent lors de votre prochaine fête de bureau. :)

### Sources

> « Si j'ai vu plus loin, c'est en me tenant sur les épaules de géants. » – Isaac Newton, 1675

1. Antti Laaksonen. [_Competitive Programmer’s Handbook (pdf)_](https://cses.fi/book.pdf)_,_ 2017
2. Wikipedia : [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
3. StackOverflow : [What is a plain English explanation of “Big O” notation?](https://stackoverflow.com/a/487278)
4. Wikipedia : [Polynomial](https://en.wikipedia.org/wiki/Polynomial)
5. Wikipedia : [NP-completeness](https://en.wikipedia.org/wiki/NP-completeness)
6. Wikipedia : [NP-hardness](https://en.wikipedia.org/wiki/NP-hardness)
7. [Desmos graph calculator](https://www.desmos.com/)

_Merci d'avoir lu ! Si vous avez trouvé cet article utile, veuillez le partager avec quelqu'un d'autre qui pourrait également en bénéficier !_