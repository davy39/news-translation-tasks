---
title: Qu'est-ce que le Typecasting en Go ? Explications avec des Exemples de Code
subtitle: ''
author: Pedro
co_authors: []
series: null
date: '2025-04-22T14:06:43.682Z'
originalURL: https://freecodecamp.org/news/what-is-typecasting-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1745329132242/7af1f157-973f-4375-8b09-b79a4f444805.png
tags:
- name: golang
  slug: golang
- name: Golang developer
  slug: golang-developer
- name: typecasting
  slug: typecasting
seo_title: Qu'est-ce que le Typecasting en Go ? Explications avec des Exemples de
  Code
seo_desc: 'When you’re working with data in Go, especially when you need to handle
  dynamic inputs like JSON from third-party APIs, understanding how to properly convert
  between data types is key. This helps you avoid bugs and crashes.

  Often times, the values re...'
---

Lorsque vous travaillez avec des données en Go, surtout lorsque vous devez gérer des entrées dynamiques comme du JSON provenant d'API tierces, comprendre comment convertir correctement les types de données est essentiel. Cela vous aide à éviter les bugs et les plantages.

Souvent, les valeurs retournées par les API sont stockées sous forme de types génériques `interface{}`. Ces types nécessitent un typecasting explicite pour être utilisés correctement. Mais sans une conversion de type appropriée, vous risquez une perte de données, un comportement inattendu, voire des plantages à l'exécution.

Dans cet article, nous allons explorer comment fonctionne le typecasting en Go. Vous apprendrez ce que c'est, comment le faire correctement et pourquoi c'est crucial pour écrire un code sûr et fiable.

Vous apprendrez la différence entre le typecasting implicite et explicite, les pièges courants à éviter et comment travailler en toute sécurité avec des données dynamiques. Nous aborderons également des exemples pratiques, y compris la gestion des données JSON et comment la nouvelle fonctionnalité de génériques de Go peut simplifier les conversions de type.

### Table des Matières :

* [Pourquoi Vous Devriez Vous Soucier du Typecasting](#heading-pourquoi-vous-devriez-vous-soucier-du-typecasting)

* [Qu'est-ce que le Typecasting ?](#heading-quest-ce-que-le-typecasting)

* [Comment Faire du Typecasting en Go](#heading-comment-faire-du-typecasting-en-go)

* [Erreurs Courantes à Éviter](#heading-erreurs-courantes-a-eviter)

* [Un Exemple Concret : Où les Choses Tournent Mal](#heading-un-exemple-concret-ou-les-choses-tournent-mal)

* [Avancé : Comment Utiliser les Génériques pour un Typecasting Plus Sûr](#heading-avance-comment-utiliser-les-generiques-pour-un-typecasting-plus-sur)

* [Réflexions Finales](#heading-reflexions-finales)

* [Tableau des Conversions de Type Courantes en Go](#heading-tableau-des-conversions-de-type-courantes-en-go)

* [Paquets Utiles pour la Conversion de Type](#heading-paquets-utiles-pour-la-conversion-de-type)

* [Références](#heading-references)

## Pourquoi Vous Devriez Vous Soucier du Typecasting

J'ai décidé d'écrire à ce sujet après avoir rencontré un vrai problème dans le codebase d'une entreprise. L'application récupérait des données d'une API tierce qui retournait des objets JSON. Les valeurs étaient dynamiques et stockées sous forme de types génériques `interface{}`, mais le code essayait de les utiliser directement comme `int`, `float64` et `string` sans vérifier ni convertir les types correctement. Cela a causé des bugs silencieux, des comportements inattendus et même des plantages qui ont pris des heures à tracer.

Si vous apprenez Go – ou n'importe quel langage – savoir quand et comment faire du typecasting peut vous faire économiser des heures de débogage. Alors, commençons.

## Qu'est-ce que le Typecasting ?

Le typecasting (ou conversion de type) est le processus de conversion d'un type de variable en un autre. Par exemple, transformer un `int` en `float`, ou une `string` en nombre. C'est une technique simple mais essentielle pour travailler avec des données qui n'arrivent pas toujours dans le type que vous attendez.

Il existe deux principaux types de typecasting :

* **Implicite (automatique) :** Se produit en arrière-plan, généralement lorsque c'est sûr (par exemple, `int` en `float64` dans certains langages).

* **Explicite (manuel) :** Vous, le développeur, êtes responsable de la conversion. C'est le cas en Go.

Pourquoi est-ce important ? Parce que si vous ne convertissez pas les types correctement, votre programme pourrait :

* Perdre des données (par exemple, des décimales tronquées).

* Planter de manière inattendue.

* Afficher des résultats incorrects aux utilisateurs.

Je partage quelques ressources à la fin de l'article si vous cherchez des paquets Go qui simplifient les conversions de type et réduisent le code répétitif.

## Comment Faire du Typecasting en Go

Go est un langage typé statiquement, et il ne fait pas de conversions implicites entre différents types. Si vous voulez changer un type, vous devez le faire vous-même en utilisant une syntaxe explicite.

Regardons quelques exemples de base :

```go
var a int = 42                     // Déclare une variable 'a' de type int et lui attribue la valeur 42
var b float64 = float64(a)        // Convertit explicitement 'a' de int en float64 et le stocke dans 'b'
                                  // Go nécessite une conversion de type manuelle (explicite) entre différents types
```

Ici, nous convertissons un `int` (`a`) en `float64` (`b`). Il s'agit d'une conversion élargissante – elle est sûre car chaque entier peut être représenté comme un float.

Maintenant, l'inverse :

```go
var x float64 = 9.8              // Déclare une variable float64 'x' avec une valeur décimale
var y int = int(x)               // Convertit 'x' en int et le stocke dans 'y'
                                 // Cela supprime (tronque) tout ce qui suit le point décimal
                                 // Donc y sera 9, pas 10 — il n'arrondit pas !
```

Ici, nous convertissons un `float64` en `int`, ce qui **tronque** la partie décimale. Il s'agit d'une conversion rétrécissante et peut entraîner une perte de données.

Go vous oblige à être explicite afin que vous ne perdiez pas accidentellement des informations ou ne cassiez pas votre logique.

## Erreurs Courantes à Éviter

Lorsque vous travaillez avec des données dynamiques comme du JSON ou des API tierces, il est courant d'utiliser `interface{}` pour représenter des types inconnus. Mais vous ne pouvez pas les utiliser directement comme des types spécifiques sans vérifier d'abord.

Voici une erreur que beaucoup de débutants font :

```go
var data interface{} = "123"       // 'data' contient une valeur de type interface{} (un type générique)
value := data.(string)             // Cela essaie d'affirmer que 'data' est une string
                                   // Si ce n'est pas une string, cela provoquera une panique et plantera le programme
```

Si `data` n'est pas réellement une `string`, cela provoquera une panique à l'exécution.

Une version plus sûre serait :

```go
value, ok := data.(string)         // Essaie de convertir 'data' en string, en toute sécurité
if !ok {
    fmt.Println("L'assertion de type a échoué")  // Si le type ne correspond pas, 'ok' sera false
} else {
    fmt.Println("La valeur est :", value)       // N'utilise 'value' que si l'assertion a réussi
}
```

Cela vérifie le type avant de convertir et évite un plantage. Toujours gérer le cas `ok` lors de l'assertion de types à partir de `interface{}`.

## Un Exemple Concret : Où les Choses Tournent Mal

Nous allons beaucoup utiliser les fonctions de marshaling et unmarshaling JSON. Si vous voulez comprendre ce que sont ces fonctions, voici une rapide introduction ou révision.

### Qu'est-ce que le Marshalling en Go ?

Le marshaling fait référence au processus de conversion des structures de données Go en une représentation JSON. Cela est particulièrement utile lorsque vous préparez des données à envoyer sur le réseau ou à sauvegarder dans un fichier. Le résultat du marshaling est généralement un slice de bytes contenant la chaîne JSON.

L'unmarshaling, en revanche, est l'opération inverse. Il convertit les données JSON en structures Go, vous permettant de travailler avec des formats de données externes ou dynamiques de manière fortement typée.

Dans les applications typiques, vous pouvez marshaler une struct pour envoyer des données via une API, ou unmarshaler une charge utile JSON reçue d'un service tiers.

Lorsque vous utilisez des structs, le marshaling et l'unmarshaling sont simples et bénéficient des tags de champs qui guident la correspondance des clés JSON. Mais lorsque vous travaillez avec des formats JSON non structurés ou inconnus, vous pouvez unmarshaler dans un `map[string]interface{}`. Dans ces cas, les assertions de type deviennent nécessaires pour accéder et manipuler les données en toute sécurité.

Comprendre comment fonctionnent le marshaling et l'unmarshaling est fondamental lorsque vous construisez des services qui consomment ou exposent des API, interagissent avec des webhooks, ou traitent des fichiers de configuration au format JSON.

D'accord, revenons à notre exemple :

Disons que vous recevez une réponse JSON d'une API et que vous l'unmarshelez dans une map :

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`{"price": 10.99}`)        // Entrée JSON simulée

    var result map[string]interface{}         // Utilise une map pour unmarshaler le JSON
    json.Unmarshal(data, &result)             // Unmarshal dans une map générique

    price := result["price"].(float64)        // Assertion correcte que price est un float64
    fmt.Println("Le prix est :", price)

    total := int(result["price"])             // ❌ Cela va échouer !
}
```

Cela échoue parce que `result["price"]` est de type `interface{}`. Essayer de le convertir directement en `int` provoque une erreur de compilation :

> cannot convert result\["price"\] (map index expression of type interface{}) to type int: need type assertion

Vous devez d'abord assert le type.

### La Bonne Façon de Faire

Voici la version sûre et correcte :

```go
package main

import (
    "encoding/json"
    "fmt"
)

func main() {
    data := []byte(`{"price": 10.99}`)        // Entrée JSON représentant une valeur float

    var result map[string]interface{}         // Crée une map pour contenir le JSON analysé
    json.Unmarshal(data, &result)             // Analyse le JSON dans la map

    // Étape 1 : Assert que la valeur est un float64
    priceFloat, ok := result["price"].(float64)
    if !ok {
        fmt.Println("Échec de la conversion du prix en float64")
        return
    }

    fmt.Println("Total en float :", priceFloat)  // Valeur float extraite avec succès

    // Étape 2 : Convertit le float en int (tronque les décimales)
    total := int(priceFloat)
    fmt.Println("Total en entier :", total)     // Résultat entier final (par exemple, 10 à partir de 10.99)
}
```

Cela fonctionne parce que nous vérifions d'abord que la valeur est un `float64` et ne la convertissons en `int` qu'ensuite. Ce processus en deux étapes – assertion de type puis conversion – est la clé pour éviter les erreurs.

## Avancé : Comment Utiliser les Génériques pour un Typecasting Plus Sûr

Avec l'introduction des **génériques** dans Go 1.18, vous pouvez écrire des fonctions réutilisables qui fonctionnent avec n'importe quel type. Les génériques vous permettent de définir des fonctions où le type peut être spécifié lorsque la fonction est appelée.

### Qu'est-ce que les Génériques en Go ?

Les génériques ont été introduits dans Go 1.18 pour permettre l'écriture de fonctions et de structures de données qui fonctionnent avec n'importe quel type. Ils aident à réduire la duplication de code et à augmenter la sécurité des types en permettant des types paramétrés.

Dans le contexte du typecasting, les génériques vous permettent d'écrire des helpers flexibles (comme `getValue[T]`) qui réduisent les assertions `interface{}` répétitives et rendent votre code plus facile à maintenir.

* Les paramètres de type sont définis avec des crochets : `[T any]`

* Le mot-clé `any` est un alias pour `interface{}`

* Les vérifications à la compilation garantissent que les types passés sont utilisés en toute sécurité

Les génériques sont particulièrement utiles dans les bibliothèques, les API et lors de la manipulation de structures dynamiques comme les objets JSON.

Disons que vous voulez extraire des valeurs d'un `map[string]interface{}` sans écrire des assertions répétitives :

```go
// Une fonction générique qui récupère et assert le type d'une valeur dans une map de manière sûre
func getValue[T any](data map[string]interface{}, key string) (T, bool) {
    val, ok := data[key]                  // Vérifie si la clé existe dans la map
    if !ok {
        var zero T                        // Déclare une valeur zéro de type T
        return zero, false                // Retourne la valeur zéro et false si la clé n'est pas trouvée
    }

    converted, ok := val.(T)              // Essaie de convertir (assert le type) la valeur en type T
    return converted, ok                  // Retourne le résultat et le statut de succès
}
```

Cette fonction :

* Accepte n'importe quel type `T` que vous spécifiez (comme `float64`, `string`, etc.)

* Assert le type pour vous

* Retourne la valeur et un booléen indiquant le succès

Utilisation :

```go
price, ok := getValue[float64](result, "price") // Essaie d'obtenir un float64 de la map
if !ok {
    fmt.Println("Prix non trouvé ou mauvais type")
}

title, ok := getValue[string](result, "title")  // Essaie d'obtenir une string de la map
if !ok {
    fmt.Println("Titre non trouvé ou mauvais type")
}
```

Ce modèle garde votre code propre et lisible tout en évitant les paniques dues aux assertions non sûres.

## Réflexions Finales

Que vous débutiez avec Go ou que vous plongiez dans des motifs plus avancés comme les génériques, comprendre le typecasting est la clé pour écrire un code sûr et fiable.

Cela peut sembler un petit détail, mais des conversions de type incorrectes peuvent causer des plantages, des bugs ou une perte de données silencieuse – surtout lorsque vous travaillez avec du JSON, des API ou des entrées utilisateur.

Voici ce que vous devez retenir :

* 🔍 Toujours connaître le type avec lequel vous travaillez.

* 🔧 Utilisez les assertions de type avec prudence et vérifiez la valeur `ok`.

* 🤖 Utilisez les génériques pour simplifier la logique d'assertion répétitive.

* ⚠️ Ne comptez pas sur la chance – soyez intentionnel avec les conversions.

Maîtriser le typecasting en Go ne fera pas seulement de vous un meilleur développeur, mais vous aidera également à comprendre comment les systèmes typés fonctionnent dans différents langages.

## Tableau des Conversions de Type Courantes en Go

| Type Source | Type Cible | Exemple de Syntaxe | Notes |
| --- | --- | --- | --- |
| `int` | `float64` | `float64(myInt)` | Conversion élargissante, sûre |
| `float64` | `int` | `int(myFloat)` | Tronque les décimales |
| `string` | `int` | `strconv.Atoi(myString)` | Retourne `int` et une erreur |
| `int` | `string` | `strconv.Itoa(myInt)` | Convertit `int` en chaîne décimale |
| `[]byte` | `string` | `string(myBytes)` | Nécessite un UTF-8 valide |
| `string` | `[]byte` | `[]byte(myString)` | Crée un slice de bytes |

## Paquets Utiles pour la Conversion de Type

* `strconv` : Conversion de chaînes en nombres et vice versa

* `reflect` : Introspection des types à l'exécution (à utiliser avec prudence)

* `encoding/json` : Mappage automatique des types lors de l'unmarshaling

* `fmt` : Conversion rapide en chaîne avec formatage

## Références

* https://go.dev/doc/effective\_go

* https://go.dev/doc/tutorial/generics

* https://gosolve.io/golang-cast-go-type-casting-and-type-conversion/