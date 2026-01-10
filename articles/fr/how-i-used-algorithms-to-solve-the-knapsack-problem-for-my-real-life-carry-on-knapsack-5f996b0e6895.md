---
title: Comment j'ai utilisé des algorithmes pour résoudre le problème du sac à dos
  pour mon vrai sac à dos de cabine
subtitle: ''
author: Victoria Drake
co_authors: []
series: null
date: '2018-05-15T14:36:26.000Z'
originalURL: https://freecodecamp.org/news/how-i-used-algorithms-to-solve-the-knapsack-problem-for-my-real-life-carry-on-knapsack-5f996b0e6895
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Vu-yZ0y22GkbnJ0K3zregw.png
tags:
- name: algorithms
  slug: algorithms
- name: coding
  slug: coding
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment j'ai utilisé des algorithmes pour résoudre le problème du sac à
  dos pour mon vrai sac à dos de cabine
seo_desc: I’m a nomad and live out of one carry-on bag. This means that the total
  weight of all my worldly possessions must fall under airline cabin baggage weight
  limits — usually 10kg. On some smaller airlines, however, this weight limit drops
  to 7kg. Occasi...
---

Je suis une nomade et je vis avec un seul sac de cabine. Cela signifie que le poids total de toutes mes possessions doit être inférieur aux limites de poids des bagages en cabine des compagnies aériennes — généralement 10 kg. Cependant, sur certaines petites compagnies aériennes, cette limite de poids passe à 7 kg. Parfois, je dois décider de ne pas emporter quelque chose avec moi pour m'adapter à la limite de poids plus petite.

En tant qu'exercice pratique, décider quoi laisser derrière (ou se débarrasser complètement) implique de disposer toutes mes affaires et de choisir celles à garder. Cette décision est basée sur l'utilité de l'objet pour moi (sa valeur) et son poids.

![Image](https://cdn-media-1.freecodecamp.org/images/0*IJPBUwDAGDhz13i2.jpeg)
_Ce sont toutes mes affaires, et mon sac de cabine Minaal._

En tant que programmeur, je sais que des décisions comme celle-ci pourraient être prises plus efficacement par un ordinateur. C'est fait si fréquemment et si universellement, en fait, que beaucoup reconnaîtront ce scénario comme le problème classique de l'emballage ou le problème du sac à dos. Comment faire pour dire à un ordinateur de mettre autant d'objets importants que possible dans mon sac tout en restant à ou sous une limite de poids de 7 kg ? Avec des algorithmes ! Hourra !

Je vais discuter de deux approches courantes pour résoudre le problème du sac à dos : l'une appelée un algorithme glouton, et une autre appelée programmation dynamique (un peu plus difficile, mais meilleure, plus rapide, plus forte…).

Commençons.

### L'installation

J'ai préparé mes données sous la forme d'un fichier CSV avec trois colonnes : le nom de l'objet (une chaîne), une représentation de sa valeur (un entier), et son poids en grammes (un entier). Il y a 40 objets au total. J'ai représenté la valeur en classant chaque objet de 40 à 1, avec 40 étant le plus important et 1 équivalant à quelque chose comme « pourquoi est-ce que j'ai encore ça ? » (Si vous n'avez jamais listé toutes vos possessions et les avez classées par ordre d'utilité pour vous, je vous recommande vivement d'essayer. Cela peut être un exercice très révélateur.)

**Poids total de tous les objets et du sac :** 9003 g

**Poids du sac :** 1415 g

**Limite de la compagnie aérienne :** 7000 g

**Poids maximum des objets que je peux emballer :** 5585 g

**Valeur totale possible des objets :** 820

**Le défi :** Emballer autant d'objets que la limite le permet tout en maximisant la valeur totale.

### Structures de données

#### Lecture d'un fichier

Avant de pouvoir commencer à réfléchir à la manière de résoudre le problème du sac à dos, nous devons résoudre le problème de la lecture et du stockage de nos données. Heureusement, le package `io/ioutil` de la bibliothèque standard de Go rend la première partie simple.

```go
package main

import (
    "fmt"
    "io/ioutil"
)

func check(e error) {
    if e != nil {
        panic(e)
    }
}

func readItems(path string) {
	dat, err := ioutil.ReadFile(path)
	check(err)
    fmt.Print(string(dat))
}
```

La fonction `ReadFile()` prend un chemin de fichier et retourne le contenu du fichier et une erreur (`nil` si l'appel est réussi), donc nous avons également créé une fonction `check()` pour gérer les erreurs qui pourraient être retournées. Dans une application réelle, nous voudrions probablement faire quelque chose de plus sophistiqué que `panic`, mais ce n'est pas important pour l'instant.

#### Création d'une structure

Maintenant que nous avons nos données, nous devrions probablement faire quelque chose avec elles. Puisque nous travaillons avec des objets réels et un vrai sac, créons quelques types pour les représenter et faciliter la conceptualisation de notre programme. Une `struct` en Go est une collection typée de champs. Voici nos deux types :

```go
type item struct {
	name          string
	worth, weight int
}

type bag struct {
	bagWeight, currItemsWeight, maxItemsWeight, totalWeight int
	items                                                   []item
}
```

Il est utile d'utiliser des noms de champs très descriptifs. Vous pouvez voir que les structures sont configurées exactement comme nous avons décrit les choses qu'elles représentent. Un `item` a un `name` (chaîne), et une `worth` et un `weight` (entiers). Un `bag` a plusieurs champs de type `int` représentant ses attributs, et a également la capacité de contenir des `items`, représentés dans la structure comme une tranche de choses de type `item`.

#### Analyse et stockage de nos données

Plusieurs packages Go complets existent que nous pourrions utiliser pour analyser nos données CSV… mais où est le plaisir dans tout cela ? Allons-y avec un peu de division de chaînes et une boucle for. Voici notre fonction `readItems()` mise à jour :

```go
func readItems(path string) []item {
	
	dat, err := ioutil.ReadFile(path)
	check(err)

	lines := strings.Split(string(dat), "\n")

	itemList := make([]item, 0)

	for i, v := range lines {
		if i == 0 {
			continue
		}
		s := strings.Split(v, ",")
		newItemWorth, _ := strconv.Atoi(s[1])
		newItemWeight, _ := strconv.Atoi(s[2])
		newItem := item{name: s[0], worth: newItemWorth, weight: newItemWeight}
		itemList = append(itemList, newItem)
	}
	return itemList
}
```

En utilisant `strings.Split`, nous divisons notre `dat` en nouvelles lignes. Nous créons ensuite une `itemList` vide pour contenir nos objets.

Dans notre boucle for, nous sautons la première ligne de notre fichier CSV (les en-têtes) puis nous itérons sur chaque ligne. Nous utilisons `strconv.Atoi` (lire « A to i ») pour convertir les valeurs de la valeur et du poids de chaque objet en entiers. Nous créons ensuite un `newItem` avec ces valeurs de champ et l'ajoutons à la `itemList`. Enfin, nous retournons `itemList`.

Voici à quoi ressemble notre configuration jusqu'à présent :

```go
package main

import (
	"io/ioutil"
	"strconv"
	"strings"
)

type item struct {
	name          string
	worth, weight int
}

type bag struct {
	bagWeight, currItemsWeight, maxItemsWeight, totalWeight, totalWorth int
	items                                                               []item
}

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readItems(path string) []item {

	dat, err := ioutil.ReadFile(path)
	check(err)

	lines := strings.Split(string(dat), "\n")

	itemList := make([]item, 0)

	for i, v := range lines {
		if i == 0 {
			continue // sauter les en-têtes sur la première ligne
		}
		s := strings.Split(v, ",")
		newItemWorth, _ := strconv.Atoi(s[1])
		newItemWeight, _ := strconv.Atoi(s[2])
		newItem := item{name: s[0], worth: newItemWorth, weight: newItemWeight}
		itemList = append(itemList, newItem)
	}
	return itemList
}
```

Maintenant que nous avons nos structures de données configurées, commençons à emballer (?) avec la première approche.

### Algorithme glouton

Un algorithme glouton est l'approche la plus directe pour résoudre le problème du sac à dos, en ce sens qu'il s'agit d'un algorithme en une seule passe qui construit une solution finale unique. À chaque étape du problème, l'algorithme glouton choisit l'option qui est localement optimale, ce qui signifie qu'elle semble être l'option la plus appropriée pour l'instant. Il ne révise pas ses choix précédents au fur et à mesure qu'il progresse dans notre ensemble de données.

#### Construction de notre algorithme glouton

Les étapes de l'algorithme que nous allons utiliser pour résoudre notre problème de sac à dos sont :

1. Trier les objets par valeur, par ordre décroissant.
2. Commencer par l'objet de la plus grande valeur. Mettre les objets dans le sac jusqu'à ce que le prochain objet de la liste ne puisse plus entrer.
3. Essayer de remplir toute capacité restante avec le prochain objet de la liste qui peut entrer.

Si vous avez lu mon [article sur la résolution de problèmes et la fabrication de paella](https://victoria.dev/verbose/how-to-code-a-satellite-algorithm-and-cook-paella-from-scratch/), vous savez que je commence toujours par déterminer quelle est la prochaine question la plus importante. Dans ce cas, il y a trois opérations principales que nous devons comprendre comment faire :

* Trier les objets par valeur.
* Mettre un objet dans le sac.
* Vérifier si le sac est plein.

La première est simplement une recherche dans la documentation. Voici comment nous trions une tranche en Go :

```go
sort.Slice(is, func(i, j int) bool {
    return is[i].worth > is[j].worth
})
```

La fonction `sort.Slice()` ordonne nos objets selon la fonction less que nous fournissons. Dans ce cas, elle ordonnera les objets de la plus grande valeur à la plus petite valeur.

Étant donné que nous ne voulons pas mettre un objet dans le sac s'il ne rentre pas, nous allons compléter les deux dernières tâches à l'envers. D'abord, nous allons vérifier si l'objet rentre. Si c'est le cas, il va dans le sac.

```go
func (b *bag) addItem(i item) error {
	if b.currItemsWeight+i.weight <= b.maxItemsWeight {
		b.currItemsWeight += i.weight
		b.items = append(b.items, i)
		return nil
	}
	return errors.New("could not fit item")
}
```

Remarquez le `*` dans notre première ligne. Cela indique que `bag` est un récepteur de pointeur (par opposition à un récepteur de valeur). C'est un concept qui peut être légèrement déroutant si vous êtes nouveau en Go. Voici [quelques choses à considérer](https://github.com/golang/go/wiki/CodeReviewComments#receiver-type) qui pourraient vous aider à décider quand utiliser un récepteur de valeur et quand utiliser un récepteur de pointeur. Pour les besoins de notre fonction `addItem()`, ce cas s'applique :

> _Si la méthode doit muter le récepteur, le récepteur doit être un pointeur._

Notre utilisation d'un récepteur de pointeur indique à notre fonction que nous voulons opérer sur _ce sac spécifique en particulier_, et non sur un nouveau sac. C'est important car sans cela, chaque objet entrerait toujours dans un sac nouvellement créé ! Un petit détail comme celui-ci peut faire la différence entre un code qui fonctionne et un code qui vous tient éveillé jusqu'à 4h du matin à boire du Red Bull et à murmurer pour vous-même. (Allez vous coucher à l'heure même si votre code ne fonctionne pas — vous me remercierez plus tard.)

Maintenant que nous avons nos composants, assemblons notre algorithme glouton :

```go
func greedy(is []item, b bag) {
	sort.Slice(is, func(i, j int) bool {
		return is[i].worth > is[j].worth
	})

	for i := range is {
		b.addItem(is[i])
	}

	b.totalWeight = b.bagWeight + b.currItemsWeight

	for _, v := range b.items {
		b.totalWorth += v.worth
	}
}
```

Ensuite, dans notre fonction `main()`, nous allons créer notre sac, lire nos données et appeler notre algorithme glouton. Voici à quoi cela ressemble, tout prêt à partir :

```go
func main() {

	minaal := bag{bagWeight: 1415, currItemsWeight: 0, maxItemsWeight: 5585}
	itemList := readItems("objects.csv")

	greedy(itemList, minaal)
}
```

#### Résultats de l'algorithme glouton

Alors, comment cet algorithme se comporte-t-il lorsqu'il s'agit d'emballer efficacement notre sac pour maximiser sa valeur totale ? Voici le résultat :

**Poids total du sac et des objets :** 6987 g

**Valeur totale des objets emballés :** 716

Voici les objets que notre algorithme glouton a choisis, triés par valeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*jb4ug2Rd4T46XUdcYSgIJQ.png)
_Ceci est une capture d'écran car Medium n'aime pas les tableaux._

Il est clair que l'algorithme glouton est un moyen simple de trouver rapidement une solution réalisable. Pour les petits ensembles de données, il sera probablement proche de la solution optimale. L'algorithme a emballé une valeur totale d'objets de 716 (104 points de moins que la valeur maximale possible), tout en remplissant le sac avec seulement 13 g de reste.

Comme nous l'avons appris précédemment, l'algorithme glouton n'améliore pas la solution qu'il retourne. Il ajoute simplement le prochain objet de la plus grande valeur qu'il peut au sac.

Regardons une autre méthode pour résoudre le problème du sac à dos qui nous donnera la solution optimale — la valeur totale la plus élevée possible sous la limite de poids.

### Programmation dynamique

Le nom « programmation dynamique » peut être un peu trompeur. Ce n'est pas un style de programmation, comme le nom pourrait vous le faire croire, mais simplement une autre approche.

La programmation dynamique diffère de l'algorithme glouton simple de plusieurs manières clés. Premièrement, une solution d'emballage de sac par programmation dynamique énumère tout l'espace de solution avec toutes les possibilités de combinaisons d'objets qui pourraient être utilisées pour emballer notre sac. Là où un algorithme glouton choisit la solution locale la plus optimale, les algorithmes de programmation dynamique sont capables de trouver la solution globale la plus optimale.

Deuxièmement, la programmation dynamique utilise la mémoïsation pour stocker les résultats des opérations précédemment calculées et retourne le résultat mis en cache lorsque l'opération se produit à nouveau. Cela lui permet de « se souvenir » des combinaisons précédentes. Cela prend moins de temps que de recalculer la réponse à nouveau.

#### Construction de notre algorithme de programmation dynamique

Pour utiliser la programmation dynamique afin de trouver la recette optimale pour emballer notre sac, nous devons :

1. Créer une matrice représentant tous les sous-ensembles des objets (l'espace de solution) avec des lignes représentant les objets et des colonnes représentant la capacité de poids restante du sac
2. Parcourir la matrice et calculer la valeur qui peut être obtenue par chaque combinaison d'objets à chaque étape de la capacité du sac
3. Examiner la matrice complétée pour déterminer quels objets ajouter au sac afin de produire la valeur maximale possible pour le sac au total

Il sera plus utile de visualiser notre espace de solution. Voici une représentation de ce que nous construisons avec notre code :

![Image](https://cdn-media-1.freecodecamp.org/images/0*s0ASnto3_AQSGjs1.jpg)
_L'univers multivers du sac à dos vide._

En Go, nous pouvons créer cette matrice comme une tranche de tranches.

```go
matrix := make([][]int, numItems+1) // lignes représentant les objets
for i := range matrix {
	matrix[i] = make([]int, capacity+1) // colonnes représentant les grammes de poids
}
```

Nous avons rembourré les lignes et les colonnes de `1` pour que les indices correspondent aux numéros d'objets et de poids.

Maintenant que nous avons créé notre matrice, nous allons la remplir en parcourant les lignes et les colonnes :

```go
// parcourir les lignes du tableau
for i := 1; i <= numItems; i++ {
	// parcourir les colonnes du tableau
	for w := 1; w <= capacity; w++ {
		// faire des choses dans chaque élément
	}
}
```

Ensuite, pour chaque élément, nous allons calculer la valeur de la valeur à lui attribuer. Nous faisons cela avec un code qui représente le processus suivant :

Si l'objet à l'index correspondant à la ligne actuelle s'insère dans la capacité de poids représentée par la colonne actuelle, prenez le maximum de soit :

* La valeur totale des objets déjà dans le sac ou,
* La valeur totale de tous les objets dans le sac sauf l'objet à l'index de ligne précédent, plus la valeur du nouvel objet.

En d'autres termes, alors que notre algorithme considère l'un des objets, nous lui demandons de décider si cet objet ajouté au sac produirait une valeur totale plus élevée que le dernier objet qu'il a ajouté au sac, au poids total actuel du sac. Si cet objet actuel est un meilleur choix, mettez-le dedans — sinon, laissez-le dehors.

Voici le code qui accomplit cela :

```go
// si le poids de l'objet correspondant à cet index peut s'insérer dans la colonne de capacité actuelle...
if is[i-1].weight <= w {
	// valeur de ce sous-ensemble sans cet objet
	valueOne := float64(matrix[i-1][w])
	// valeur de ce sous-ensemble sans l'objet précédent, et cet objet à la place
	valueTwo := float64(is[i-1].worth + matrix[i-1][w-is[i-1].weight])
	// prendre le maximum de valueOne ou valueTwo
	matrix[i][w] = int(math.Max(valueOne, valueTwo))
// si la nouvelle valeur n'est pas plus élevée, reporter la valeur précédente
} else {
	matrix[i][w] = matrix[i-1][w]
}
```

Ce processus de comparaison des combinaisons d'objets se poursuivra jusqu'à ce que chaque objet ait été considéré à chaque étape possible de l'augmentation du poids total du sac. Lorsque tout ce qui précède a été considéré, nous aurons énuméré l'espace de solution — rempli la matrice — avec toutes les valeurs de valeur totale possibles.

Nous aurons un grand tableau de nombres, et dans la dernière colonne à la dernière ligne, nous aurons notre valeur la plus élevée possible.

![Image](https://cdn-media-1.freecodecamp.org/images/0*1OZ_-r3Zx-Yhm4zR.jpg)
_Une représentation strictement représentative de la matrice remplie._

C'est génial, mais comment savons-nous quels objets ont été mis dans le sac pour atteindre cette valeur ?

#### Obtenir notre liste d'objets optimisée

Pour voir quels objets se combinent pour créer notre liste d'emballage optimale, nous devons examiner notre matrice à l'envers par rapport à la manière dont nous l'avons créée. Puisque nous savons que la valeur la plus élevée possible se trouve dans la dernière ligne de la dernière colonne, nous commencerons par là. Pour trouver les objets, nous :

1. Obtenons la valeur de la cellule actuelle
2. Comparons la valeur de la cellule actuelle à la valeur de la cellule directement au-dessus
3. Si les valeurs diffèrent, il y a eu un changement dans les objets du sac. Trouvons la cellule suivante à examiner en reculant à travers les colonnes selon le poids de l'objet actuel (trouvons la valeur du sac avant que cet objet actuel ne soit ajouté)
4. Si les valeurs correspondent, il n'y a pas eu de changement dans les objets du sac. Montez à la cellule de la ligne au-dessus et répétez

La nature de l'action que nous essayons d'accomplir se prête bien à une fonction récursive. Si vous vous souvenez de [mon article précédent sur la fabrication de tarte aux pommes](https://victoria.dev/verbose/understanding-array.prototype.reduce-and-recursion-using-apple-pie/), les fonctions récursives sont simplement des fonctions qui s'appellent elles-mêmes sous certaines conditions. Voici à quoi cela ressemble :

```go
func checkItem(b *bag, i int, w int, is []item, matrix [][]int) {
	if i <= 0 || w <= 0 {
		return
	}

	pick := matrix[i][w]
	if pick != matrix[i-1][w] {
		b.addItem(is[i-1])
		checkItem(b, i-1, w-is[i-1].weight, is, matrix)
	} else {
		checkItem(b, i-1, w, is, matrix)
	}
}
```

Notre fonction `checkItem()` s'appelle elle-même si la condition que nous avons décrite à l'étape 4 est vraie. Si l'étape 3 est vraie, elle s'appelle également elle-même, mais avec des arguments différents.

Les fonctions récursives nécessitent un cas de base. Dans cet exemple, nous voulons que la fonction s'arrête une fois que nous n'avons plus de valeurs de valeur à comparer. Ainsi, notre cas de base est lorsque `i` ou `w` sont `0`.

Voici à quoi ressemble l'approche de programmation dynamique lorsqu'elle est entièrement assemblée :

```go
func checkItem(b *bag, i int, w int, is []item, matrix [][]int) {
	if i <= 0 || w <= 0 {
		return
	}

	pick := matrix[i][w]
	if pick != matrix[i-1][w] {
		b.addItem(is[i-1])
		checkItem(b, i-1, w-is[i-1].weight, is, matrix)
	} else {
		checkItem(b, i-1, w, is, matrix)
	}
}

func dynamic(is []item, b *bag) *bag {
	numItems := len(is)          // nombre d'objets dans le sac à dos
	capacity := b.maxItemsWeight // capacité du sac à dos

	// créer la matrice vide
	matrix := make([][]int, numItems+1) // lignes représentant les objets
	for i := range matrix {
		matrix[i] = make([]int, capacity+1) // colonnes représentant les grammes de poids
	}

	// parcourir les lignes du tableau
	for i := 1; i <= numItems; i++ {
		// parcourir les colonnes du tableau
		for w := 1; w <= capacity; w++ {

			// si le poids de l'objet correspondant à cet index peut s'insérer dans la colonne de capacité actuelle...
			if is[i-1].weight <= w {
				// valeur de ce sous-ensemble sans cet objet
				valueOne := float64(matrix[i-1][w])
				// valeur de ce sous-ensemble sans l'objet précédent, et cet objet à la place
				valueTwo := float64(is[i-1].worth + matrix[i-1][w-is[i-1].weight])
				// prendre le maximum de valueOne ou valueTwo
				matrix[i][w] = int(math.Max(valueOne, valueTwo))
			// si la nouvelle valeur n'est pas plus élevée, reporter la valeur précédente
			} else {
				matrix[i][w] = matrix[i-1][w]
			}
		}
	}

	checkItem(b, numItems, capacity, is, matrix)

	// ajouter d'autres statistiques au sac
	b.totalWorth = matrix[numItems][capacity]
	b.totalWeight = b.bagWeight + b.currItemsWeight

	return b
}
```

#### Résultats de la programmation dynamique

Nous nous attendons à ce que l'approche de programmation dynamique nous donne une solution plus optimisée que l'algorithme glouton. Alors, est-ce le cas ? Voici les résultats :

**Poids total du sac et des objets :** 6982 g

**Valeur totale des objets emballés :** 757

Voici les objets que notre algorithme de programmation dynamique a choisis, triés par valeur :

![Image](https://cdn-media-1.freecodecamp.org/images/1*BYsgbQMgcl2jzkgSNIE3mA.png)

Il y a une amélioration évidente de notre solution de programmation dynamique par rapport à ce que l'algorithme glouton nous a donné. Notre valeur totale de 757 est de 41 points supérieure à la solution de 716 de l'algorithme glouton, et pour quelques grammes de poids en moins aussi !

#### Ordre de tri de l'entrée

Lors du test de ma solution de programmation dynamique, j'ai implémenté l'algorithme de mélange Fisher-Yates sur l'entrée avant de la passer dans ma fonction, juste pour m'assurer que la réponse n'était pas d'une manière ou d'une autre dépendante de l'ordre de tri de l'entrée. Voici à quoi ressemble le mélange en Go :

```go
rand.Seed(time.Now().UnixNano())

for i := range itemList {
	j := rand.Intn(i + 1)
	itemList[i], itemList[j] = itemList[j], itemList[i]
}
```

Bien sûr, j'ai ensuite réalisé que Go 1.10 a maintenant un mélange intégré. Il fonctionne précisément de la même manière et ressemble à ceci :

```go
rand.Shuffle(len(itemList), func(i, j int) {
	itemList[i], itemList[j] = itemList[j], itemList[i]
})
```

Alors, l'ordre dans lequel les objets ont été traités a-t-il affecté le résultat ? Eh bien...

#### Soudain... un poids indésirable apparaît !

Comme il s'avère, d'une certaine manière, la réponse dépendait de l'ordre de l'entrée. Lorsque j'ai exécuté mon algorithme de programmation dynamique plusieurs fois, j'ai parfois vu un poids total différent pour le sac, bien que la valeur totale soit restée à 757. J'ai d'abord pensé que c'était un bug avant d'examiner les deux ensembles d'objets qui accompagnaient les deux valeurs de poids total différentes. Tout était identique sauf pour quelques changements qui, collectivement, ont abouti à un sous-ensemble d'objets différent comptant pour 14 des 757 points de valeur.

Dans ce cas, il y avait deux solutions également optimales basées uniquement sur la métrique de succès de la valeur totale possible la plus élevée. Le mélange de l'entrée semblait affecter le placement des objets dans la matrice et ainsi, le chemin que la fonction `checkItem()` a pris en parcourant la matrice pour trouver les objets choisis. Puisque la métrique de succès d'avoir la valeur la plus élevée possible était la même dans les deux ensembles d'objets, nous n'avons pas une solution unique - il y en a deux !

En tant qu'exercice académique, ces deux ensembles d'objets sont des réponses correctes. Nous pouvons choisir d'optimiser davantage selon une autre métrique, disons, le poids total de tous les objets. La valeur la plus élevée possible au poids le plus faible possible pourrait être considérée comme une solution idéale.

Voici le deuxième résultat de programmation dynamique, plus léger :

**Poids total du sac et des objets :** 6955 g

**Valeur totale des objets emballés :** 757

![Image](https://cdn-media-1.freecodecamp.org/images/1*_PzSh7J1yDo29RGh-DSlSg.png)

### Quelle approche est meilleure ?

#### Benchmarking Go

Le package `testing` de la bibliothèque standard de Go nous permet de [benchmark](https://golang.org/pkg/testing/#hdr-Benchmarks) ces deux approches de manière simple. Nous pouvons découvrir combien de temps chaque algorithme prend pour s'exécuter, et combien de mémoire chacun utilise. Voici un simple fichier `main_test.go` :

```go
package main

import (
	"testing"
)

func Benchmark_greedy(b *testing.B) {
	itemList := readItems("objects.csv")
	for i := 0; i < b.N; i++ {
		minaal := bag{bagWeight: 1415, currItemsWeight: 0, maxItemsWeight: 5585}
		greedy(itemList, minaal)
	}
}

func Benchmark_dynamic(b *testing.B) {
	itemList := readItems("objects.csv")
	for i := 0; i < b.N; i++ {
		minaal := bag{bagWeight: 1415, currItemsWeight: 0, maxItemsWeight: 5585}
		dynamic(itemList, &minaal)
	}
}
```

Nous pouvons exécuter `go test -bench=. -benchmem` pour voir ces résultats :

```sh
Benchmark_greedy-4       1000000              1619 ns/op            2128 B/op          9 allocs/op
Benchmark_dynamic-4         1000           1545322 ns/op         2020332 B/op         49 allocs/op

```

#### Performance de l'algorithme glouton

Après avoir exécuté l'algorithme glouton 1 000 000 fois, la vitesse de l'algorithme a été mesurée de manière fiable à 0,001619 millisecondes (traduction : très rapide). Il a nécessité 2128 octets ou 2 kilooctets de mémoire et 9 allocations de mémoire distinctes par itération.

#### Performance de la programmation dynamique

L'algorithme de programmation dynamique a été exécuté 1 000 fois. Sa vitesse a été mesurée à 1,545322 millisecondes ou 0,001545322 secondes (traduction : toujours assez rapide). Il a nécessité 2 020 332 octets ou 2 mégaoctets, et 49 allocations de mémoire distinctes par itération.

### Le verdict

Une partie du choix de la bonne approche pour résoudre un problème de programmation consiste à prendre en compte la taille de l'ensemble de données d'entrée. Dans ce cas, il est petit. Dans ce scénario, un algorithme glouton en une seule passe sera toujours plus rapide et moins gourmand en ressources que la programmation dynamique, simplement parce qu'il a moins d'étapes. Notre algorithme glouton était presque deux ordres de grandeur plus rapide et moins gourmand en mémoire que notre algorithme de programmation dynamique.

Cependant, ne pas avoir ces étapes supplémentaires signifie qu'il est peu probable d'obtenir la meilleure solution possible de l'algorithme glouton.

Il est clair que l'algorithme de programmation dynamique nous a donné de meilleurs chiffres : un poids plus faible et une valeur globale plus élevée.

#### Algorithme glouton

* Poids total : 6987 g
* Valeur totale : 716

#### Programmation dynamique

* Poids total : 6955 g
* Valeur totale : 757

Là où la programmation dynamique sur de petits ensembles de données manque de performance, elle compense en optimisation. La question devient alors de savoir si cette optimisation supplémentaire vaut le coût de performance.

« Meilleur », bien sûr, est un jugement subjectif. Si la vitesse et la faible utilisation des ressources sont notre métrique de succès, alors l'algorithme glouton est clairement meilleur. Si la valeur totale des objets dans le sac est notre métrique de succès, alors la programmation dynamique est clairement meilleure.

Cependant, notre scénario est pratique, et seule l'une de ces conceptions d'algorithme a retourné une réponse que je choisirais. En optimisant pour la plus grande valeur totale possible des objets dans le sac, l'algorithme de programmation dynamique a laissé de côté mon objet de la plus grande valeur, mais aussi le plus lourd, mon ordinateur portable. Les chargeurs et câbles, le support Roost et le clavier qui étaient inclus ne sont pas très utiles sans lui.

### Meilleure conception d'algorithme

Il existe un moyen simple de modifier l'approche de programmation dynamique pour que l'ordinateur portable soit toujours inclus : nous pouvons modifier les données pour que la valeur de l'ordinateur portable soit supérieure à la somme de la valeur de tous les autres objets. (Essayez-le !)

Peut-être qu'en reconcevant l'algorithme de programmation dynamique pour qu'il soit plus pratique, nous pourrions choisir une autre métrique de succès qui reflète mieux l'importance d'un objet, au lieu d'une valeur subjective. Il existe de nombreuses métriques possibles que nous pouvons utiliser pour représenter la valeur d'un objet. Voici quelques exemples d'un bon proxy :

* Quantité de temps passé à utiliser l'objet
* Coût initial de l'achat de l'objet
* Coût de remplacement si l'objet était perdu aujourd'hui
* Valeur en dollars du produit de l'utilisation de l'objet

De la même manière, les résultats de l'algorithme glouton pourraient être améliorés avec l'utilisation de l'une de ces métriques alternatives.

En plus de choisir une approche appropriée pour résoudre le problème du sac à dos en général, il est utile de concevoir notre algorithme de manière à traduire les réalités d'un scénario en code.

Il existe de nombreuses considérations pour une meilleure conception d'algorithme au-delà de la portée de cet article d'introduction que je prévois de couvrir (certaines) dans des articles ultérieurs. Un algorithme futur pourrait très bien décider du contenu de mon sac pour le prochain voyage, mais nous n'en sommes pas encore là. Restez à l'écoute !

_Merci d'avoir lu ! J'espère que cet article vous a donné une meilleure idée de la manière dont ces deux approches courantes fonctionnent. Si vous souhaitez en savoir plus sur la manière dont je vis avec un seul sac de cabine, consultez mon blog nomade sur [herOneBag.com](https://heronebag.com/)._

_Passez une très bonne journée. :)_