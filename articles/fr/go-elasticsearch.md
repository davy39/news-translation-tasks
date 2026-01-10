---
title: Comment implémenter Elasticsearch en Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-11-25T20:00:00.000Z'
originalURL: https://freecodecamp.org/news/go-elasticsearch
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/Screenshot-from-2019-11-24-22-21-41-1.png
tags:
- name: elasticsearch
  slug: elasticsearch
- name: Go Language
  slug: go
- name: General Programming
  slug: programming
- name: Software Engineering
  slug: software-engineering
seo_title: Comment implémenter Elasticsearch en Go
seo_desc: 'By Pramono Winata

  Today, I am going to show you how to implement Elasticsearch in Go.But of course,
  before that I am going to give a small introduction to Elasticsearch.If you have
  already gained a basic understanding of Elasticsearch, you can skip t...'
---

Par Pramono Winata

Aujourd'hui, je vais vous montrer comment implémenter Elasticsearch en Go. 
Mais bien sûr, avant cela, je vais donner une petite introduction à Elasticsearch. 
Si vous avez déjà acquis une compréhension de base d'Elasticsearch, vous pouvez passer à la partie suivante.

## **Elasticsearch** 

Elasticsearch a gagné beaucoup de popularité ces derniers temps. La recherche dans une base de données relationnelle pose toujours des problèmes de scalabilité et de performance. 

Elasticsearch est une base de données NoSQL qui a été très efficace pour résoudre ces problèmes. Elle offre une grande scalabilité et des performances élevées, et l'une des fonctionnalités les plus marquantes est le système de notation qui permet une grande flexibilité dans les résultats de recherche. Après tout, ce n'est pas pour rien qu'elle s'appelle Elastic-search !

### Installation d'Elasticsearch

Tout d'abord, vous devrez installer Elasticsearch sur votre machine locale. Vous pouvez vous rendre sur leur [site web](https://www.elastic.co/guide/index.html) et obtenir le [guide d'installation](https://www.elastic.co/guide/en/elasticsearch/reference/7.4/install-elasticsearch.html). Au moment où j'écris cet article, j'utilise Elasticsearch avec le numéro de version 7.4.2.

Elasticsearch a apporté de nombreux changements dans ses versions, dont la [suppression du type de mapping](https://www.elastic.co/guide/en/elasticsearch/reference/master/removal-of-types.html). Ne vous attendez donc pas à ce que cela fonctionne complètement si vous utilisez une autre version d'Elasticsearch.

Après avoir terminé votre installation, n'oubliez pas de lancer votre service Elasticsearch, ce qui est mentionné assez clairement dans leur guide d'installation (pour Linux, en bref, faites ceci : `./bin/elasticsearch`).

**Assurez-vous que votre Elasticsearch est en cours d'exécution** en faisant une requête sur le port 9200 de votre machine locale.

GET `localhost:9200`

Cela devrait afficher quelque chose comme ci-dessous.

```json
{
  "name": "204371",
  "cluster_name": "elasticsearch",
  "cluster_uuid": "8Aa0PznuR1msDL9-PYsNQg",
  "version": {
    "number": "7.4.2",
    "build_flavor": "default",
    "build_type": "tar",
    "build_hash": "2f90bbf7b93631e52bafb59b3b049cb44ec25e96",
    "build_date": "2019-10-28T20:40:44.881551Z",
    "build_snapshot": false,
    "lucene_version": "8.2.0",
    "minimum_wire_compatibility_version": "6.8.0",
    "minimum_index_compatibility_version": "6.0.0-beta1"
  },
  "tagline": "You Know, for Search"
}
```

Si cela s'affiche correctement, félicitations ! Vous avez réussi à lancer votre service Elasticsearch sur votre machine locale. Faites-vous une ovation et prenez une tasse de café, car la journée est encore jeune.

### Création de votre premier index

Dans Elasticsearch, un index est similaire à une base de données. Auparavant, il y avait une table dans Elasticsearch appelée type. Mais puisque le type a été supprimé dans la version actuelle, il n'y a plus que des index maintenant.

Confus maintenant ? Ne le soyez pas. En résumé, pensez simplement que vous n'avez besoin que d'un index, puis ensuite vous n'avez qu'à insérer vos données dans Elasticsearch.

Maintenant, nous allons créer un index nommé `students` en effectuant la requête ci-dessous.
PUT `localhost/9200/students`

```json
{
	"settings": {
    	"number_of_shards": 1,
    	"number_of_replicas": 1
	},
   "mappings": {
       "properties": {
         "name": {
               "type": "text"
         },
         "age": {
               "type": "integer"
         },
         "average_score": {
               "type": "float"
         }
     }
   }
}
```

Si tout se passe bien, il devrait répondre en donnant ceci.

```json
{
    "acknowledged": true,
    "shards_acknowledged": true
}

```

Votre index devrait être créé. Nous allons maintenant passer à l'étape suivante : jouer avec notre index Elasticsearch.

### Peuplement de votre Elasticsearch

Tout d'abord, ce que nous allons faire maintenant est de remplir notre index Elasticsearch avec des documents. Si vous n'êtes pas familier avec cette définition, sachez simplement que c'est très similaire aux lignes dans une base de données.

Dans une base de données NoSQL, il est en fait possible pour chaque document de contenir des champs différents qui ne correspondent pas au schéma.

Mais ne faisons pas cela – construisons notre colonne avec un schéma que nous avons défini auparavant. L'API précédente vous permettra de remplir le document dans votre index.

POST `localhost:9200/students/doc`

```json
{
	"name":"Alice",
	"age":17,
	"average_score":81.1
}

```

Votre Elasticsearch devrait avoir un document maintenant. Nous allons devoir insérer plusieurs autres données dans notre Elasticsearch. Et bien sûr, nous n'allons pas insérer nos données d'étudiants une par une – ce serait assez fastidieux !

Elasticsearch a spécifiquement préparé une API de masse afin d'envoyer plusieurs requêtes à la fois. Utilisons cela pour insérer plusieurs données à la fois.

POST `/students/_bulk`

```json
{ "index":{"_index": "students" } }
{ "name":"john doe","age":18, "average_score":77.7 }
{ "index":{"_index": "students" } }
{ "name":"bob","age":16, "average_score":65.5 }
{ "index":{"_index": "students" } }
{ "name":"mary doe","age":18, "average_score":97.7 }
{ "index":{"_index": "students" } }
{ "name":"eve","age":15, "average_score":98.9 }
```

### Interrogeons les données

Nous avons enfin peuplé notre Elasticsearch avec plusieurs autres données d'étudiants. Maintenant, faisons ce pour quoi Elasticsearch est connu : nous allons essayer de rechercher dans notre Elasticsearch les données que nous venons d'insérer.

Elasticsearch supporte de nombreux types de mécanismes de recherche, mais pour cet exemple, nous allons utiliser une simple requête de correspondance.

Commençons notre recherche en appelant cette API :

POST `localhost:9200/_search`

```json
{
    "query" : {
        "match" : { "name" : "doe" }
    }
}

```

Vous obtiendrez votre réponse avec les données des étudiants qui correspondent à votre requête. Vous êtes maintenant officiellement un ingénieur de recherche !

```json
{
    "took": 608,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 2,
            "relation": "eq"
        },
        "max_score": 0.74487394,
        "hits": [
            {
                "_index": "students",
                "_type": "_doc",
                "_id": "rgpef24BTFuh7kXolTpo",
                "_score": 0.74487394,
                "_source": {
                    "name": "john doe",
                    "age": 18,
                    "average_score": 77.7
                }
            },
            {
                "_index": "students",
                "_type": "_doc",
                "_id": "sApef24BTFuh7kXolTpo",
                "_score": 0.74487394,
                "_source": {
                    "name": "mary doe",
                    "age": 18,
                    "average_score": 97.7
                }
            }
        ]
    }
}
```

## Maintenant, passons à Go !

![Image](https://www.freecodecamp.org/news/content/images/2019/11/download--2-.png)
_Go en action !_

Si vous avez atteint cette partie, vous devriez avoir saisi les concepts très basiques de l'utilisation d'Elasticsearch. Maintenant, nous allons implémenter Elasticsearch en Go.

Une méthode très primitive pour implémenter Elasticsearch est de continuer à faire des requêtes HTTP vers l'IP de votre Elasticsearch. Mais nous ne allons pas faire cela.

J'ai trouvé [cette](https://github.com/olivere/elastic) bibliothèque très utile pour implémenter Elasticsearch en Go. Vous devriez installer cette bibliothèque avant de continuer dans vos modules Go.

### Créez votre struct

Tout d'abord, vous aurez définitivement besoin de créer une struct pour votre Modèle. Dans cet exemple, nous allons utiliser la même modélisation que dans notre exemple précédent, qui dans ce cas est la struct `Student`.

```go
package main

type Student struct {
	Name         string  `json:"name"`
	Age          int64   `json:"age"`
	AverageScore float64 `json:"average_score"`
}
```

### Création d'une connexion client

Maintenant, créons une fonction qui nous permettra d'initialiser notre connexion client ES.
Si vous avez une instance en cours d'exécution d'Elasticsearch en dehors de votre localhost, vous pouvez simplement changer la partie à l'intérieur de `SetURL`.

```go
func GetESClient() (*elastic.Client, error) {

	client, err :=  elastic.NewClient(elastic.SetURL("http://localhost:9200"),
		elastic.SetSniff(false),
		elastic.SetHealthcheck(false))

	fmt.Println("ES initialisé...")

	return client, err

}
```

### **Insertion de données**

Après cela, la première chose que nous pouvons faire est d'essayer d'insérer nos données dans Elasticsearch via Go. Nous allons créer un modèle de `Student` et l'insérer dans notre client Elasticsearch.

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	elastic "gopkg.in/olivere/elastic.v7"
)

func main() {

	ctx := context.Background()
	esclient, err := GetESClient()
	if err != nil {
		fmt.Println("Erreur d'initialisation : ", err)
		panic("Échec du client")
	}

	// création de l'objet étudiant
	newStudent := Student{
		Name:         "Gopher doe",
		Age:          10,
		AverageScore: 99.9,
	}

	dataJSON, err := json.Marshal(newStudent)
	js := string(dataJSON)
	ind, err := esclient.Index().
		Index("students").
		BodyJson(js).
		Do(ctx)

	if err != nil {
		panic(err)
	}

	fmt.Println("[Elastic][InsertProduct]Insertion réussie")

}
```

### **Interrogation de nos données**

Enfin, nous pouvons faire quelques recherches. Le code ci-dessous peut sembler un peu complexe. Mais soyez assuré, il sera plus clair pour vous après l'avoir examiné attentivement. Je vais utiliser une requête de correspondance de base dans l'exemple ci-dessous.

```go
package main

import (
	"context"
	"encoding/json"
	"fmt"

	elastic "gopkg.in/olivere/elastic.v7"
)

func main() {

	ctx := context.Background()
	esclient, err := GetESClient()
	if err != nil {
		fmt.Println("Erreur d'initialisation : ", err)
		panic("Échec du client")
	}

	var students []Student

	searchSource := elastic.NewSearchSource()
	searchSource.Query(elastic.NewMatchQuery("name", "Doe"))

	/* ce bloc imprimera essentiellement la requête es */
	queryStr, err1 := searchSource.Source()
	queryJs, err2 := json.Marshal(queryStr)

	if err1 != nil || err2 != nil {
		fmt.Println("[esclient][GetResponse]err lors du marshaling de la requête=", err1, err2)
	}
	fmt.Println("[esclient]Final ESQuery=\n", string(queryJs))
    /* jusqu'à ce bloc */

	searchService := esclient.Search().Index("students").SearchSource(searchSource)
    
	searchResult, err := searchService.Do(ctx)
	if err != nil {
		fmt.Println("[ProductsES][GetPIds]Erreur=", err)
		return
	}

	for _, hit := range searchResult.Hits.Hits {
		var student Student
		err := json.Unmarshal(hit.Source, &student)
		if err != nil {
			fmt.Println("[Getting Students][Unmarshal] Err=", err)
		}

		students = append(students, student)
	}

	if err != nil {
		fmt.Println("Échec de la récupération de l'étudiant : ", err)
	} else {
		for _, s := range students {
			fmt.Printf("Étudiant trouvé Nom : %s, Âge : %d, Score : %f \n", s.Name, s.Age, s.AverageScore)
		}
	}

}
```

La requête devrait être imprimée comme ceci :

```
ES initialisé...
[esclient]Final ESQuery=
 {"query":{"match":{"name":{"query":"Doe"}}}}
```

Et oui, cette requête est ce qui sera posté dans Elasticsearch.

Le résultat de votre requête devrait également sortir comme ceci si vous avez suivi mon exemple depuis le début :

```
Étudiant trouvé Nom : john doe, Âge : 18, Score : 77.700000 
Étudiant trouvé Nom : mary doe, Âge : 18, Score : 97.700000 
Étudiant trouvé Nom : Gopher doe, Âge : 10, Score : 99.900000 
```

Et voilà !

C'est la fin de mon tutoriel sur la façon d'implémenter Elasticsearch en Go. J'espère avoir couvert les parties très basiques de l'utilisation d'Elasticsearch en Go.

Pour obtenir plus d'informations sur ce sujet, vous devriez lire sur [Query DSL](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl.html) et [Function Scoring](https://www.elastic.co/guide/en/elasticsearch/reference/current/query-dsl-function-score-query.html) dans Elasticsearch, qui, à mon avis, sont l'une des meilleures choses à propos d'Elasticsearch.

Et ne vous inquiétez pas, la bibliothèque utilisée dans cet exemple supporte également de nombreuses fonctionnalités d'Elasticsearch, même la requête de notation de fonction dans Elasticsearch.

Merci d'avoir lu mon article ! J'espère qu'il sera utile et pourra vous aider à commencer à utiliser Elasticsearch.

> Ne cessez jamais d'apprendre ; les connaissances doublent tous les quatorze mois. ~Anthony J.D'Angelo