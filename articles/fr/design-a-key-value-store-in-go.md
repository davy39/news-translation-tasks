---
title: Comment concevoir un magasin clé-valeur transactionnel en Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-09T15:29:12.000Z'
originalURL: https://freecodecamp.org/news/design-a-key-value-store-in-go
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/key-value-blog-header--5-.png
tags:
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Comment concevoir un magasin clé-valeur transactionnel en Go
seo_desc: 'By Bhupesh Varshney

  If you want to design an interactive shell that allows access to a transactional
  in-memory key/value store, then you''re in the right place.

  Let''s Go together and design one now.

  Backstory

  System design questions have always intere...'
---

Par Bhupesh Varshney

Si vous souhaitez concevoir un shell interactif qui permet l'accès à un magasin clé/valeur transactionnel en mémoire, alors vous êtes au bon endroit.

Allons-y ensemble et concevons-en un maintenant.

## Contexte

Les questions de conception de systèmes m'ont toujours intéressé car elles permettent d'être créatif. 

Récemment, j'ai lu le [blog](https://meekg33k.dev/) de [Uduak](https://triplebyte.com/blog/the-best-worst-and-most-interesting-moments-from-my-marathon-month-of-technical-interviews/?ref=linews_blog) où il a partagé son expérience d'un marathon d'entretiens de 30 jours, ce qui était assez excitant. Je recommande vivement de le lire.

En tout cas, j'ai découvert cette question intéressante de [conception de système](https://en.wikipedia.org/wiki/Systems_design) qui lui a été posée lors de l'entretien.

## Le Défi

La question est la suivante :

_Construire un shell interactif qui permet l'accès à un "magasin clé/valeur transactionnel en mémoire"._

**Note** : La question est reformulée pour une meilleure compréhension. Elle a été donnée comme un projet "à faire à la maison" lors de l'entretien de l'auteur mentionné ci-dessus.

Le shell doit accepter les commandes suivantes :

<table>
<thead>
<tr>
<th align="center">Commande</th>
<th align="center">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="center"><code>SET</code></td>
<td align="left">Définit la clé donnée à la valeur spécifiée. Une clé peut également être mise à jour.</td>
</tr>
<tr>
<td align="center"><code>GET</code></td>
<td align="left">Affiche la valeur actuelle de la clé spécifiée.</td>
</tr>
<tr>
<td align="center"><code>DELETE</code></td>
<td align="left">Supprime la clé donnée. Si la clé n'a pas été définie, ignore.</td>
</tr>
<tr>
<td align="center"><code>COUNT</code></td>
<td align="left">Retourne le nombre de clés qui ont été définies à la valeur spécifiée. Si aucune clé n'a été définie à cette valeur, affiche 0.</td>
</tr>
<tr>
<td align="center"><code>BEGIN</code></td>
<td align="left">Démarre une transaction. Ces transactions permettent de modifier l'état du système et de valider ou d'annuler vos modifications.</td>
</tr>
<tr>
<td align="center"><code>END</code></td>
<td align="left">Termine une transaction. Tout ce qui a été fait dans la transaction "active" est perdu.</td>
</tr>
<tr>
<td align="center"><code>ROLLBACK</code></td>
<td align="left">Annule les modifications apportées dans le contexte de la transaction active. Si aucune transaction n'est active, affiche "No Active Transaction".</td>
</tr>
<tr>
<td align="center"><code>COMMIT</code></td>
<td align="left">Valide les modifications apportées dans le contexte de la transaction active et termine la transaction active.</td>
</tr>
</tbody>
</table>

## Nous sommes dans l'arène ?

Avant de commencer, nous pouvons poser quelques questions supplémentaires comme :

**Q1.** _Les données persistent-elles après la fin de la session du shell interactif ?_

**Q2.** _Les opérations sur les données se reflètent-elles dans le shell global ?_

**Q3.** _La validation des modifications dans une transaction imbriquée se reflète-t-elle également chez les grands-parents ?_

Vos questions peuvent différer, ce qui est parfait. Plus vous posez de questions, mieux vous comprenez le problème.

La résolution du problème dépendra largement des questions posées, alors définissons ce que nous allons supposer lors de la construction de notre magasin clé-valeur :

1. Les données ne sont pas persistantes (c'est-à-dire que dès que la session du shell se termine, les données sont perdues).
2. Les clés-valeurs ne peuvent être que des chaînes de caractères (nous pouvons implémenter des interfaces pour des types de données personnalisés, mais cela est hors de portée pour ce tutoriel).

Maintenant, essayons de comprendre la partie délicate de notre problème.

### Comprendre une "Transaction"

Une transaction est créée avec la commande `BEGIN` et crée un contexte pour que les autres opérations se produisent. Par exemple :

```go
> BEGIN // Crée une nouvelle transaction
> SET X 200
> SET Y 14
> GET Y
14

```

Ceci est la transaction active actuelle et toutes les opérations ne fonctionnent qu'à l'intérieur de celle-ci.

Jusqu'à ce que la transaction active soit validée à l'aide de la commande `COMMIT`, ces opérations ne persistent pas. Et, la commande `ROLLBACK` annule toute modification apportée par ces opérations dans le contexte de la transaction active. Pour être plus précis, elle supprime toutes les paires clé-valeur de la carte.

Par exemple :

```go
> BEGIN // Crée une nouvelle transaction qui est actuellement active
> SET Y 2020
> GET Y
2020
> ROLLBACK // Annule toute modification apportée
> GET Y
Y not set // Les modifications apportées par SET Y ont été annulées

```

Une transaction peut également être imbriquée, c'est-à-dire avoir des transactions enfants également :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/parent-child.png)
_Hiérarchie parent-enfant dans les transactions_

La nouvelle transaction générée hérite des variables de sa transaction parente et les modifications apportées dans le contexte d'une transaction enfant se refléteront également dans la transaction parente.  


Par exemple :

```go
> BEGIN // Crée une nouvelle transaction active
> SET X 5
> SET Y 19
> BEGIN // Génère une nouvelle transaction dans le contexte de la transaction précédente et maintenant celle-ci est actuellement active
> GET Y
Y = 19 // La nouvelle transaction hérite du contexte de sa transaction parente**
> SET Y 23
> COMMIT // La nouvelle valeur de Y a été persistée dans le magasin clé-valeur**
> GET Y
Y = 23 // Les modifications apportées par SET Y 19 ont été annulées**

```

J'ai essayé juste après avoir lu le blog. Voyons comment nous pouvons résoudre cela.

## Conception

Nous avons discuté du fait que les transactions peuvent également avoir des transactions enfants, nous pouvons utiliser la structure de données [pile](https://en.wikipedia.org/wiki/Stack_(abstract_data_type)) pour généraliser cela :

![Image](https://www.freecodecamp.org/news/content/images/2020/09/kv1.png)
_Visualisation de notre pile de transactions_

* Chaque élément de la pile est une **transaction**.
* Le sommet de la pile stocke notre transaction "Active" actuelle.
* Chaque élément de transaction a sa propre [carte](https://en.wikipedia.org/wiki/Hash_table). Nous l'appellerons "magasin local" qui agit comme un cache local - chaque fois que nous définissons une variable à l'intérieur d'une transaction, ce magasin est mis à jour.
* Une fois les modifications validées à l'intérieur d'une transaction, les valeurs de ce magasin "local" sont écrites dans notre objet de carte global.

Nous allons utiliser une implémentation de [liste liée](https://en.wikipedia.org/wiki/Linked_list) de la pile. Nous pouvons également y parvenir en utilisant des tableaux dynamiques, mais c'est un travail à faire pour le lecteur :

```go
package main

import (
	"fmt"
	"os"
	"bufio"
	"strings"
)

/*GlobalStore contient les variables (globales)*/
var GlobalStore = make(map[string]string)

/*Transaction pointe vers un magasin clé:valeur*/
type Transaction struct {
	store map[string]string // chaque transaction a son propre magasin local
	next  *Transaction
}

/*TransactionStack maintient une liste de transactions actives/suspendues */
type TransactionStack struct {
	top  *Transaction
	size int 			// plus de métadonnées peuvent être sauvegardées comme la limite de la pile, etc.
}

```

* Notre pile est représentée par une structure, `TransactionStack` qui ne stocke qu'un pointeur vers le `top` de la pile.`size` est une variable de structure qui peut être utilisée pour déterminer la taille de notre pile, c'est-à-dire pour trouver le nombre de transactions suspendues et actives (complètement optionnel - vous pouvez omettre de déclarer cela).
* La structure `Transaction` a un magasin que nous avons défini précédemment comme une carte et un pointeur vers la transaction suivante en mémoire.
* `GlobalStore` est une carte qui est partagée par toutes les transactions de la pile. C'est ainsi que nous réalisons une relation parent-enfant, mais nous en parlerons plus tard.

Maintenant, écrivons les méthodes push et pop pour notre `TransactionStack`.

```go

/*PushTransaction crée une nouvelle transaction active*/
func (ts *TransactionStack) PushTransaction() {
	// Pousse une nouvelle transaction, c'est la transaction active actuelle
	temp := Transaction{store : make(map[string]string)}
	temp.next = ts.top
	ts.top = &temp
	ts.size++
}

/*PopTransaction supprime une transaction de la pile*/
func (ts *TransactionStack) PopTransaction() {
	// Supprime la transaction de la pile, n'est plus active
	if ts.top == nil {
		// en gros, débordement de pile
		fmt.Printf("ERROR: No Active Transactions\n")
	} else {
		node := &Transaction{}
		ts.top = ts.top.next
		node.next = nil
		ts.size--
	}
}


```

* Avec chaque opération `BEGIN`, un nouvel élément de pile est poussé dans le `TransactionStack` et met à jour `top` à cette valeur.
* Pour chaque opération `COMMIT` ou `END`, la transaction active est _supprimée_ de la pile et l'élément suivant de la pile est assigné à `top`. Par conséquent, la transaction parente est maintenant notre transaction active actuelle.

Si vous êtes nouveau en Go, notez que `PushTransaction()` et `PopTransaction()` sont des [méthodes](https://gobyexample.com/methods) et non des fonctions du type de récepteur (`*TransactionStack`).

Dans des langages comme JavaScript et Python, l'invocation de méthode de récepteur est réalisée par les mots-clés `this` et `self`, respectivement. 

Cependant, en Go, ce n'est pas le cas. Vous pouvez le nommer comme vous le souhaitez. Pour faciliter la compréhension, nous choisissons `ts` pour faire référence à la pile de transactions.

Maintenant, nous créons une méthode `Peek` pour nous retourner l'élément `top` de la pile :

```go
/*Peek retourne la transaction active*/
func (ts *TransactionStack) Peek() *Transaction {
	return ts.top
}

```

Notez que nous retournons une variable de pointeur de type `Transaction`.

La validation d'une transaction impliquera la "copie" de toutes les nouvelles valeurs et/ou mises à jour du magasin local de la transaction vers notre `GlobalStore` :

```go
/*Commit écrit les modifications (SET) dans le magasin avec la portée de TransactionStack
Écrit également les modifications sur le disque/fichier, si les données doivent persister après la fermeture du shell
*/
func (ts *TransactionStack) Commit() {
	ActiveTransaction := ts.Peek()
	if ActiveTransaction != nil {
		for key, value := range ActiveTransaction.store {
			GlobalStore[key] = value
			if ActiveTransaction.next != nil {
				// met à jour la transaction parente
				ActiveTransaction.next.store[key] = value
			}
		}
	} else {
		fmt.Printf("INFO: Nothing to commit\n")
	}
	// écrire les données dans un fichier pour les rendre persistantes sur le disque
	// Astuce : sérialiser les données de la carte en JSON
}

```

L'annulation d'une transaction est assez simple. Il suffit de supprimer toutes les clés de la carte (la carte locale d'une transaction) :

```go
/*RollBackTransaction efface toutes les clés définies dans une transaction*/
func (ts *TransactionStack) RollBackTransaction() {
	if ts.top == nil {
		fmt.Printf("ERROR: No Active Transaction\n")
	} else {
		for key := range ts.top.store {
			delete(ts.top.store, key)
		}
	}
}

```

Et enfin, voici les fonctions `GET` et `SET` :

```go
/*Obtenir la valeur de la clé à partir du magasin*/
func Get(key string, T *TransactionStack) {
	ActiveTransaction := T.Peek()
	if ActiveTransaction == nil {
		if val, ok := GlobalStore[key]; ok {
		    fmt.Printf("%s\n", val)
		} else {
			fmt.Printf("%s not set\n", key)
		}
	} else {
		if val, ok := ActiveTransaction.store[key]; ok {
		    fmt.Printf("%s\n", val)
		} else {
			fmt.Printf("%s not set\n", key)
		}
	}
}

```

Lors de la définition d'une variable, nous devons également considérer le cas où l'utilisateur ne pourrait pas exécuter de transactions du tout. Cela signifie que notre pile sera vide, c'est-à-dire que l'utilisateur définit des variables dans le shell global lui-même.

```go
> SET F 55
> GET F
55

```

Dans ce cas, nous pouvons mettre à jour directement notre `GlobalStore` :

```go
/*Définir la clé à la valeur */
func Set(key string, value string, T *TransactionStack) {
	// Obtenir le magasin clé:valeur à partir de la transaction active
	ActiveTransaction := T.Peek()
	if ActiveTransaction == nil {
		GlobalStore[key] = value
	} else {
		ActiveTransaction.store[key] = value
	}
}

```

Êtes-vous toujours avec moi ? Ne partez pas !

![we are in the endgame now](https://i.imgflip.com/2pep5c.jpg?a444295)

Nous avons presque terminé avec notre magasin clé-valeur, alors écrivons le code pilote :

```go

func main(){
	reader := bufio.NewReader(os.Stdin)
	items := &TransactionStack{}
	for {
		fmt.Printf("> ")
		text, _ := reader.ReadString('\n')
		// diviser le texte en chaînes d'opération
		operation := strings.Fields(text)
		switch operation[0] {
		case "BEGIN": 		items.PushTransaction()
		case "ROLLBACK": 	items.RollBackTransaction()
		case "COMMIT": 		items.Commit(); items.PopTransaction()
		case "END": 		items.PopTransaction()
		case "SET": 		Set(operation[1], operation[2], items)
		case "GET": 		Get(operation[1], items)
        case "DELETE": 		Delete(operation[1], items)
		case "COUNT": 		Count(operation[1], items)
		case "STOP": 		os.Exit(0)
		default:
			fmt.Printf("ERROR: Unrecognised Operation %s\n", operation[0])
		}
	}
}


```

Les opérations `COUNT` et `DELETE` sont assez faciles à implémenter si vous êtes resté avec moi jusqu'à présent. 

Je vous encourage à faire cela comme devoir, mais j'ai fourni mon implémentation ci-dessous si vous êtes bloqué quelque part.

Temps pour les tests ⚙.

![zoe-demo](https://user-images.githubusercontent.com/34342551/92362469-aa2a7700-f10d-11ea-8426-1e8462b66d18.gif)

Et laissez-moi vous laisser avec [mon code source](https://github.com/Bhupesh-V/zoe) - vous pouvez donner une étoile au dépôt si vous voulez soutenir mon travail.

Si vous avez aimé ce tutoriel, vous pouvez lire plus de mes articles sur [mon blog](https://bhupesh-v.github.io).

Des doutes, quelque chose ne va pas, ou vous avez des commentaires ? Connectez-vous avec moi sur [Twitter](https://twitter.com/bhupeshimself) ou envoyez-les-moi directement par [e-mail](mailto:varshneybhupesh@gmail.com).

Gophers par [MariaLetta/free-gophers-pack](https://github.com/MariaLetta/free-gophers-pack)

Bon apprentissage 😊