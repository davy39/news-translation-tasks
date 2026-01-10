---
title: Comment envoyer et analyser des données JSON en Golang – Encodage et décodage
  de données expliqués avec des exemples
subtitle: ''
author: Destiny Erhabor
co_authors: []
series: null
date: '2024-08-05T13:00:54.000Z'
originalURL: https://freecodecamp.org/news/encoding-and-decoding-data-in-golang
coverImage: https://www.freecodecamp.org/news/content/images/2024/07/ferenc-almasi-HfFoo4d061A-unsplash.jpg
tags:
- name: Go Language
  slug: go
- name: json
  slug: json
seo_title: Comment envoyer et analyser des données JSON en Golang – Encodage et décodage
  de données expliqués avec des exemples
seo_desc: "When building web applications in Golang, working with JSON data is inevitable.\
  \ Whether you're sending responses to clients or parsing requests, JSON encoding\
  \ and decoding are essential skills to master. \nIn this article, we'll explore\
  \ the different ..."
---

Lors de la création d'applications web en Golang, travailler avec des données JSON est inévitable. Que vous envoyiez des réponses aux clients ou que vous analysiez des requêtes, l'encodage et le décodage JSON sont des compétences essentielles à maîtriser. 

Dans cet article, nous explorerons les différentes façons d'encoder et de décoder JSON en Golang.

## Table des matières

* [Comment envoyer des réponses JSON (Encodage)](#heading-comment-envoyer-des-reponses-json-encodage)
* [Comment utiliser la fonction Marshal pour l'encodage JSON](#heading-comment-utiliser-la-fonction-marshal-pour-lencodage-json)
* [Comment utiliser la fonction NewEncoder](#heading-comment-utiliser-la-fonction-newencoder)
* [Comment analyser les requêtes JSON (Décodage)](#heading-comment-analyser-les-requetes-json-decodage)
* [Comment utiliser la fonction Unmarshal pour analyser les requêtes JSON](#heading-comment-utiliser-la-fonction-unmarshal-pour-analyser-les-requetes-json)
* [Comment utiliser la fonction NewDecoder pour le décodage JSON](#heading-comment-utiliser-la-fonction-newdecoder-pour-le-decodage-json)
* [Encodage et décodage JSON personnalisés](#heading-encodage-et-decodage-json-personnalises)
* [Comment utiliser JSON Marshaler](https://www.freecodecamp.org/news/p/4e27d014-692d-4c5d-bad0-0bd1af87cef3/how-to-use-json-marshaler)
* [Comment utiliser JSON Unmarshaler](#heading-comment-utiliser-json-unmarshaler)
* [Compromis](#heading-compromis)
* [Cas d'utilisation et recommandations](#heading-cas-dutilisation-et-recommandations)
* [Conclusion](#heading-conclusion)

## Comment envoyer des réponses JSON (Encodage)

L'encodage JSON est le processus de conversion des structures de données Go en format JSON.

L'encodage fait référence au processus de conversion de données d'un format à un autre. Dans le contexte de l'informatique et de la transmission de données, l'encodage implique généralement la conversion de données dans un format standardisé qui peut être facilement stocké, transmis ou traité par différents systèmes ou applications.

Pensez à l'encodage comme à l'action de faire une valise pour un voyage. Vous prenez vos vêtements (données) et les rangez dans une valise (format encodé) afin qu'ils puissent être facilement transportés (transmis) et déballés (décodés) à votre destination.

Dans le cas de l'encodage JSON, les données sont converties dans un format basé sur du texte qui utilise des caractères lisibles par l'homme pour représenter les données. Cela facilite la lecture et la compréhension des données par les humains, ainsi que l'échange et le traitement des données par différents systèmes.

Voici quelques raisons courantes d'encoder des données :

* Compression des données : Réduire la taille des données pour faciliter leur stockage ou leur transmission.
* Sécurité des données : Protéger les données contre les accès non autorisés ou les altérations.
* Compatibilité des données : Convertir les données dans un format qui peut être lu et traité par différents systèmes ou applications.
* Transmission des données : Convertir les données dans un format qui peut être facilement transmis sur un réseau ou d'autres canaux de communication.

En Golang, nous pouvons utiliser le package `encoding/json` pour encoder les données JSON.

### Comment utiliser la fonction Marshal pour l'encodage JSON

La fonction `Marshal` est la méthode la plus couramment utilisée pour encoder les données JSON en Golang. Elle prend une structure de données Go en entrée et retourne une chaîne encodée en JSON.

```go
package main

import ( 
	"encoding/json"
    "fmt"
    "net/http"
 )
 
type Person struct { 
	Name string `json:"name"` 
    Age int `json:"age"`
}

func handler(w http.ResponseWriter, r *http.Request) { 
	person := Person{  Name: "John",  Age: 30, } 
    
    // Encodage - Une étape
    jsonStr, err := json.Marshal(person) 
    
    if err != nil {  
    	http.Error(w, err.Error(), http.StatusInternalServerError)  
        return 
    } 
    
    w.Write(jsonStr)
}

func main() { 
	http.HandleFunc("/", handler) 
    http.ListenAndServe(":8080", nil)
 }
```

#### Explication du code :

###### Imports :

* `encoding/json` : Fournit des fonctions pour l'encodage et le décodage JSON.
* `fmt` : Pour l'impression de la sortie.

###### Struct Person :

* Définit une struct `Person` avec les champs `Name` et `Age`.
* Les tags de struct (par exemple : `json:"name"`) spécifient les noms des clés JSON.

###### Fonction main :

* Crée une instance de `Person`.
* Appelle `json.Marshal` pour encoder la struct `person` en JSON. Cela retourne une tranche de bytes et une erreur.
* Si aucune erreur n'est présente, elle convertit la tranche de bytes en une chaîne et l'imprime.

### Comment utiliser la fonction NewEncoder

La fonction `NewEncoder` est utilisée pour encoder les données JSON vers un writer, tel qu'un fichier ou une connexion réseau.

```go
package main

import ( 
	"encoding/json" 
    "fmt" 
    "net/http"
)

type Person struct { 
	Name string `json:"name"` 
    Age int `json:"age"`
}

func handler(w http.ResponseWriter, r *http.Request) { 
	person := Person{  Name: "John",  Age: 30 } 
    
    // Encodage - 2 étapes. NewEncoder et Encode
    encoder := json.NewEncoder(w) 
    
    err := encoder.Encode(person) 
    
    if err != nil {  
    	http.Error(w, err.Error(), http.StatusInternalServerError)  
        
        return 
   }}
   
func main() { 
   http.HandleFunc("/", handler) http.ListenAndServe(":8080", nil)
}
```

#### Explication du code :

###### À l'intérieur du handler :

* La fonction `handler` est un gestionnaire HTTP qui traite les requêtes HTTP entrantes.
* `w http.ResponseWriter` : Utilisé pour écrire la réponse.
* `r *http.Request` : Représente la requête entrante.
* Une instance de `Person` nommée `person` a été créée et initialisée avec les valeurs `Name: "John"` et `Age: 30`.
* Un encodeur JSON a été créé en utilisant `json.NewEncoder(w)`, qui écrira la sortie JSON vers le writer de réponse `w`.
* La struct `person` a été encodée en JSON et écrite dans la réponse en utilisant `encoder.Encode(person)`.
* Si une erreur se produit lors de l'encodage, elle est renvoyée au client en tant que réponse d'erreur HTTP avec un code de statut `500 Internal Server Error`.

## Comment analyser les requêtes JSON (Décodage)

Le décodage JSON est le processus de conversion des données JSON en structures de données Go. 

Le décodage fait référence au processus de conversion de données d'un format standardisé vers leur forme originale. En informatique et en transmission de données, le décodage implique de prendre des données encodées et de les transformer dans un format qui peut être facilement compris et traité par un système ou une application spécifique.

Pensez au décodage comme au déballage d'une valise après un voyage. Vous prenez la valise emballée (données encodées) et la déballage, en remettant chaque article (données) à sa place d'origine, afin de pouvoir l'utiliser à nouveau.

Dans le cas du décodage JSON, les données JSON basées sur du texte sont converties vers leur forme originale, telle qu'une structure de données Go (comme une struct ou une tranche), afin qu'elles puissent être facilement accessibles et traitées par l'application.

Voici quelques raisons courantes de décoder des données :

* Extraction de données : Récupération de données spécifiques à partir d'un ensemble de données encodé plus grand.
* Analyse de données : Conversion de données encodées dans un format qui peut être facilement analysé ou traité.
* Stockage de données : Conversion de données encodées dans un format qui peut être facilement stocké dans une base de données ou un système de fichiers.
* Visualisation de données : Conversion de données encodées dans un format qui peut être facilement visualisé ou affiché.

Le décodage est essentiellement le processus inverse de l'encodage, et c'est une étape essentielle dans de nombreux pipelines de traitement de données.

En Golang, nous pouvons utiliser le package `encoding/json` pour décoder les données JSON.

### Comment utiliser la fonction Unmarshal pour analyser les requêtes JSON

La fonction `Unmarshal` est la méthode la plus couramment utilisée pour décoder les données JSON en Golang. Elle prend une chaîne encodée en JSON en entrée et retourne une structure de données Go.

```go
package main

import ( 
	"encoding/json" 
    "fmt" 
    "net/http"
)

type Person struct { 
	Name string `json:"name"` 
    Age int `json:"age"`
}

func handler(w http.ResponseWriter, r *http.Request) { 
	var person Person err := json.NewDecoder(r.Body).Decode(&person)
    
    if err != nil {  
    	http.Error(w, err.Error(), http.StatusBadRequest)  
        return
    } 
    
    fmt.Println(person.Name) 
    // Sortie: John fmt.Println(person.Age) 
    // Sortie: 30
}

func main() { 
	http.HandleFunc("/", handler) http.ListenAndServe(":8080", nil)
}
```

#### Explication du code :

###### À l'intérieur du handler :

* La fonction `handler` est un gestionnaire HTTP qui traite les requêtes HTTP entrantes.
* `w http.ResponseWriter` : Utilisé pour écrire la réponse.
* `r *http.Request` : Représente la requête entrante.
* Une variable `person` de type `Person` a été déclarée.
* `json.NewDecoder(r.Body).Decode(&person)` : Cela décode le corps de la requête JSON dans la struct `person`.
* Si une erreur se produit lors du décodage, elle envoie une réponse d'erreur HTTP 400 avec un code de statut `400 Bad Request`.
* Si le décodage est réussi, les champs de la struct `person` `Name` et `Age` sont imprimés en utilisant `fmt.Println`.

### Comment utiliser la fonction NewDecoder pour le décodage JSON

La fonction `NewDecoder` est également utilisée pour décoder les données JSON à partir d'un reader, tel qu'un fichier ou une connexion réseau.

```go
package main

import ( 
	"encoding/json" 
    "fmt" 
    "net/http"
)

type Person struct { 
	Name string `json:"name"` 
    Age int `json:"age"`
}

func handler(w http.ResponseWriter, r *http.Request) { 

	decoder := json.NewDecoder(r.Body) 
    
    var person Person err := decoder.Decode(&person) 
    
    if err != nil {  
    	http.Error(w, err.Error(), http.StatusBadRequest)  
        return 
   	} 
    
    fmt.Println(person.Name) 
    // Sortie: John fmt.Println(person.Age) 
    // Sortie: 30
}

func main() { 
	http.HandleFunc("/", handler) 
    
    http.ListenAndServe(":8080", nil)
 }
```

#### Explication du code :

###### À l'intérieur de la fonction handler :

* La fonction `handler` est un gestionnaire HTTP qui traite les requêtes HTTP entrantes.
* `w http.ResponseWriter` : Utilisé pour écrire la réponse.
* `r *http.Request` : Représente la requête entrante.

###### Créer un Décodeur :

* `decoder := json.NewDecoder(r.Body)` : Crée un nouveau décodeur JSON qui lit à partir du corps de la requête.

###### Déclarer une Variable Person :

* `var person Person` : Déclare une variable `person` de type `Person`.

###### Décoder JSON dans la Struct Person :

* `err := decoder.Decode(&person)` : Décode le JSON du corps de la requête dans la struct `person`.
* Si une erreur se produit lors du décodage, elle envoie une réponse d'erreur HTTP 400 avec le code de statut `400 Bad Request` et retourne de la fonction.

###### Imprimer les Valeurs Décodées :

* `fmt.Println(person.Name)` : Imprime le champ `Name` de la struct `person`.
* `fmt.Println(person.Age)` : Imprime le champ `Age` de la struct `person`.

### Encodage et décodage JSON personnalisés

Dans certains cas, le comportement par défaut d'encodage et de décodage JSON fourni par `json.Marshal` et `json.Unmarshal` peut ne pas être suffisant. Par exemple, vous pouvez avoir besoin de personnaliser la façon dont certains champs sont représentés en JSON. C'est là que les interfaces `json.Marshaler` et `json.Unmarshaler` deviennent utiles.

#### Comment utiliser JSON Marshaler

L'interface `json.Marshaler` vous permet de personnaliser l'encodage JSON d'un type en implémentant la méthode `MarshalJSON`. Cette méthode retourne une tranche de bytes encodée en JSON et une erreur.

```go
func (p Person) MarshalJSON() ([]byte, error) {
    type Alias Person
    return json.Marshal(&struct {
        Alias
        Age string `json:"age"`
    }{
        Alias: (Alias)(p),
        Age:   strconv.Itoa(p.Age) + " ans",
    })
}

```

Dans cet exemple, le champ `Age` est converti en une chaîne avec un suffixe " ans" lors de l'encodage en JSON.

#### Comment utiliser JSON Unmarshaler

L'interface `json.Unmarshaler` vous permet de personnaliser le décodage JSON d'un type en implémentant la méthode `UnmarshalJSON`. Cette méthode prend une tranche de bytes encodée en JSON et retourne une erreur.

```go
func (p *Person) UnmarshalJSON(data []byte) error {
    type Alias Person
    aux := &struct {
        Alias
        Age string `json:"age"`
    }{Alias: (Alias)(*p)}

    if err := json.Unmarshal(data, &aux); err != nil {
        return err
    }

    ageStr := strings.TrimSuffix(aux.Age, " ans")
    age, err := strconv.Atoi(ageStr)
    if err != nil {
        return err
    }

    p.Age = age
    p.Name = aux.Name
    return nil
}

```

Dans cet exemple, le champ `Age` est converti d'une chaîne avec un suffixe " ans" en un entier lors du décodage à partir de JSON.

## Compromis

Parmi les différentes méthodes décrites ci-dessus pour l'encodage et le décodage JSON, voici les compromis pour les méthodes les plus couramment utilisées :

### json.Marshal et json.Unmarshal :

#### Avantages :

* **Facilité d'utilisation** : Simple pour l'encodage (Marshal) et le décodage (Unmarshal) JSON.
* **Flexibilité** : Peut être utilisé avec divers types, y compris les structs, les maps, les tranches, et plus encore.
* **Personnalisation** : Les tags de struct (`json:"name"`) permettent la personnalisation des clés JSON et d'autres options.

#### Inconvénients :

* **Performance** : Peut ne pas être la méthode la plus rapide pour les structures JSON très grandes ou complexes.
* **Gestion des erreurs** : Les messages d'erreur peuvent parfois être moins descriptifs pour les structures de données profondément imbriquées ou complexes.

### json.NewEncoder et json.NewDecoder :

#### Avantages :

* **Basé sur le flux** : Adapté pour l'encodage/décodage JSON de manière continue, ce qui peut gérer de grands ensembles de données sans consommer beaucoup de mémoire.
* **Flexibilité** : Peut fonctionner directement avec les interfaces `io.Reader` et `io.Writer`, ce qui les rend utiles pour les opérations réseau et les grands fichiers.

#### Inconvénients :

* **Complexité** : Légèrement plus complexe à utiliser par rapport à `json.Marshal` et `json.Unmarshal`.
* **Gestion des erreurs** : Similaire à `json.Marshal` et `json.Unmarshal`, les messages d'erreur peuvent être moins clairs pour les structures complexes.

### Interfaces Marshaler et Unmarshaler personnalisées (json.Marshaler et json.Unmarshaler) :

#### Avantages :

* **Personnalisation** : Contrôle total sur la manière dont les types sont encodés/décodés. Utile pour gérer les types complexes ou les structures JSON personnalisées.
* **Flexibilité** : Permet d'implémenter une logique personnalisée lors de l'encodage/"décodage."

#### Inconvénients :

* **Complexité** : Plus complexe à implémenter et à utiliser, car cela nécessite l'écriture de méthodes personnalisées.
* **Maintenance** : Augmente la charge de maintenance, car la logique personnalisée doit être maintenue en synchronisation avec tout changement dans la struct ou le format de données.

### Cas d'utilisation et recommandations

* **Structures de données simples** : Utilisez `json.Marshal` et `json.Unmarshal` pour l'encodage/décodage simple de structures de données simples.
* **Flux de données volumineux** : Utilisez `json.NewEncoder` et `json.NewDecoder` pour travailler avec des flux de données volumineux ou lors d'interactions avec des fichiers ou des opérations réseau.
* **Exigences personnalisées** : Implémentez les interfaces `json.Marshaler` et `json.Unmarshaler` lorsque vous avez besoin d'un comportement personnalisé pour des types spécifiques.
* **Opérations rapides** : Utilisez des structs anonymes pour des opérations rapides et jetables où la définition d'un type de struct complet est inutile.

Chaque méthode a ses propres forces et compromis, et le meilleur choix dépend des exigences spécifiques de votre application.

### Conclusion

En conclusion, maîtriser l'encodage et le décodage JSON est crucial pour le développement d'applications web en Golang. 

En comprenant les différentes méthodes disponibles dans le package `encoding/json`, vous pouvez choisir l'approche la plus adaptée en fonction de vos exigences spécifiques.

Les fonctions `Marshal` et `Unmarshal` offrent simplicité et flexibilité pour une utilisation générale, tandis que `NewEncoder` et `NewDecoder` fournissent des capacités de streaming efficaces pour les grands ensembles de données. 

Pour les scénarios qui nécessitent des représentations JSON personnalisées, l'implémentation des interfaces `json.Marshaler` et `json.Unmarshaler` vous donne un contrôle précis sur les processus d'encodage et de décodage. 

Chaque méthode a ses propres forces et compromis, et savoir quand et comment les utiliser vous permettra de gérer les données JSON efficacement dans vos applications.