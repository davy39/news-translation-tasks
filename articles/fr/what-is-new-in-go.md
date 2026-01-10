---
title: Quoi de neuf dans Go 1.25 ? Explications et exemples
subtitle: ''
author: Pedro
co_authors: []
series: null
date: '2025-09-06T00:03:38.471Z'
originalURL: https://freecodecamp.org/news/what-is-new-in-go
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1757071558420/9a83b3fb-dbea-4d38-96ca-460bf20c213d.png
tags:
- name: golang
  slug: golang
- name: Go Language
  slug: go
seo_title: Quoi de neuf dans Go 1.25 ? Explications et exemples
seo_desc: 'Go 1.25 isn’t a flashy release with big syntax changes. Instead, it’s a
  practical one: it fixes long-standing pitfalls, improves runtime safety, adds smarter
  tooling, and introduces a powerful new JSON engine. These are the kind of updates
  that make ...'
---

Go 1.25 n'est pas une version tape-à-l'œil avec de grands changements de syntaxe. C'est plutôt une version pragmatique : elle corrige des pièges de longue date, améliore la sécurité au Runtime, ajoute des outils plus intelligents et introduit un nouveau moteur JSON puissant. Ce sont le genre de mises à jour qui rendent votre expérience de codage quotidienne plus fluide et vos applications en production plus fiables.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Adieu aux « Core Types »](#heading-adieu-aux-core-types)
    
* [Gestion plus sûre des pointeurs nil](#heading-gestion-plus-sure-des-pointeurs-nil)
    
* [Informations de débogage DWARF v5 par défaut](#heading-informations-de-debogage-dwarf-v5-par-defaut)
    
* [testing/synctest est stable](#heading-testingsynctest-est-stable)
    
* [encoding/json/v2 expérimental](#heading-experimental-encodingjsonv2)
    
* [Améliorations de l'outillage](#heading-ameliorations-de-l-outillage)
    
* [Améliorations du Runtime](#heading-ameliorations-du-runtime)
    
* [API Flight Recorder](#heading-api-flight-recorder)
    
* [Mises à jour des plateformes](#heading-mises-a-jour-des-plateformes)
    
* [Points clés à retenir](#heading-points-cles-a-retenir)
    
* [Sources](#heading-sources)
    

Passons en revue les points forts.

## Adieu aux « Core Types »

Les « Core Types » (types de base) ont été introduits dans Go 1.18 où, [selon la documentation](https://go.dev/blog/coretypes), « un core type est une construction abstraite introduite par commodité et pour simplifier la gestion des opérandes génériques ». Par exemple :

* Si un type n'est pas un paramètre de type, son core type est simplement son type sous-jacent.
    
* Si le type est un paramètre de type, son core type n'existe que si tous les types de son ensemble de types partagent le même type sous-jacent. Dans ce cas, ce type sous-jacent commun devient le core type. Sinon, aucun core type n'existe.
    

Dans Go 1.25, l'équipe a supprimé la notion de core types de la spécification et a défini chaque fonctionnalité avec des règles explicites pour les génériques, simplifiant le langage tout en conservant une compatibilité ascendante totale. Par exemple, les opérations comme l'addition sur un type générique sont désormais décrites directement en termes d'ensembles de types, sans avoir besoin de faire référence aux core types.

## Gestion plus sûre des pointeurs nil

Un bug introduit dans Go 1.21 empêchait parfois le déclenchement des panics sur les pointeurs `nil`. C'est désormais corrigé. Si vous déréférencez un `nil`, il provoquera de manière fiable un panic. Auparavant, le comportement était le suivant :

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	// Tente d'ouvrir un fichier qui n'existe pas.
	// os.Open renvoie un handle de fichier nil et une erreur non-nil.
	f, err := os.Open("does-not-exist.txt") // f est nil, err est non-nil
	fmt.Println("err:", err) // Affiche l'erreur

	// Explication du comportement buggé :
	// Le programme utilise f.Name() avant de vérifier l'erreur.
	// Puisque f est nil, cet appel panique à l'exécution.
	// Les anciennes versions de Go (1.21–1.24) laissaient parfois cela s'exécuter,
	fmt.Println("name:", f.Name())
}
```

Dans Go 1.21–1.24, un bug du compilateur supprimait parfois le panic dans le code ci-dessus et donnait l'impression que votre programme allait « bien ». Dans Go 1.25, il ne s'exécutera plus avec succès. Avec le comportement corrigé, nous avons :

```go
package main

import (
	"fmt"
	"os"
)

func main() {
	// Tente d'ouvrir un fichier qui n'existe pas.
	// os.Open renvoie un handle de fichier nil et une erreur non-nil.
	f, err := os.Open("does-not-exist.txt") 
	fmt.Println("err:", err) // Affiche une erreur

	// Cela panique maintenant de manière fiable, car f est nil et vous le déréférencez.
	fmt.Println("name:", f.Name())
}
```

La différence clé est qu'il lève désormais un panic, rendant le comportement plus prévisible.

## Informations de débogage DWARF v5 par défaut

DWARF est un format standardisé pour stocker les informations de débogage à l'intérieur des binaires compilés. Voyez cela comme une carte qui indique aux débogueurs (comme `gdb`, `dlv` pour Go, ou des IDE comme VS Code/GoLand) comment votre programme compilé se rapporte à votre code source.

Go 1.25 utilise désormais DWARF v5 pour les informations de débogage. Le résultat : des binaires plus petits et une édition de liens (linking) plus rapide. Si vous avez besoin d'une compatibilité avec des outils plus anciens, vous pouvez le désactiver avec `GOEXPERIMENT=nodwarf5`.

```bash
# Build normal (DWARF v5 activé automatiquement) :
go build ./...

# Si vous avez des outils qui ne supportent pas DWARF v5, vous pouvez le désactiver :
GOEXPERIMENT=nodwarf5 go build ./...
```

## testing/synctest est stable

Tester du code concurrent devient plus facile. Le nouveau package [`testing/synctest`](https://pkg.go.dev/testing/synctest) vous permet d'exécuter des tests de concurrence dans un environnement contrôlé où les goroutines et le temps sont déterministes.

```go
// Exécuter avec : go test
package counter

import (
	"testing"
	"testing/synctest"
)

// Counter est une structure simple contenant un entier.
// Elle possède des méthodes pour incrémenter le compte et récupérer la valeur.
type Counter struct{ n int }

func (c *Counter) Inc() { c.n++ } // Augmente le compteur de 1
func (c *Counter) N() int { return c.n } // Renvoie le compte actuel

func TestCounter_Inc_Deterministic(t *testing.T) {
	// synctest.New crée un environnement de test déterministe spécial ("bulle").
	// À l'intérieur de cette bulle, les goroutines sont planifiées de manière contrôlée,
	// de sorte que le résultat du test est toujours prévisible (pas de conditions de concurrence).
	st := synctest.New()
	defer st.Done() // Nettoyage : toujours fermer la bulle de test à la fin.

	c := &Counter{}
	const workers = 10

	// Démarre 10 goroutines à l'intérieur de la bulle synctest.
	// Chaque goroutine appelle c.Inc(), incrémentant le compteur.
	for i := 0; i < workers; i++ {
		st.Go(func() { c.Inc() })
	}

	// Exécute la bulle jusqu'à ce que toutes les goroutines soient terminées.
	// Cela garantit une fin de test déterministe.
	st.Run()

	// Vérifie le résultat : le compteur doit être égal au nombre de goroutines (10).
	// Si ce n'est pas le cas, fait échouer le test avec un message clair.
	if got, want := c.N(), workers; got != want {
		t.Fatalf("attendu %d, obtenu %d", want, got)
	}
}
```

Avec le nouveau `testing/synctest`, les tests garantissent une exécution déterministe et sans instabilité (flake-free), de sorte que le compteur finit toujours à 10.

## encoding/json/v2 expérimental

Un tout nouveau moteur JSON est disponible via le flag `GOEXPERIMENT=jsonv2`. Il est plus rapide, plus efficace et inclut un package `jsontext` adapté au streaming. Mieux encore, l'ancien `encoding/json` peut s'appuyer sur le nouveau moteur, vous bénéficiez donc de gains de performance sans casser votre ancien code.

## Améliorations de l'outillage

* `go vet` détecte désormais des erreurs courantes comme l'utilisation incorrecte de `sync.WaitGroup.Add` et la gestion non sécurisée de host:port.
    
* `go doc -http` sert la documentation localement dans votre navigateur.
    
* `go build -asan` peut détecter automatiquement les fuites de mémoire.
    

Ces petites améliorations s'additionnent pour offrir un flux de travail de développement plus fluide.

## Améliorations du Runtime

Go fonctionne désormais de manière plus intelligente à l'intérieur des conteneurs. Sur Linux, il détecte automatiquement le nombre de CPU que le conteneur est autorisé à utiliser et s'ajuste en conséquence. Il existe également un nouveau garbage collector expérimental appelé *greenteagc*, qui peut rendre le nettoyage de la mémoire jusqu'à 40 % plus rapide dans certains cas.

## API Flight Recorder

Avez-vous déjà souhaité voir exactement ce que faisait votre application Go lorsqu'un problème survenait — par exemple lorsqu'une requête prend soudainement 10 secondes au lieu de 100 millisecondes, ou que votre application commence mystérieusement à utiliser trop de CPU ? Au moment où vous le remarquez, il est généralement trop tard pour déboguer car le problème est déjà passé. La nouvelle fonctionnalité FlightRecorder de Go résout ce problème en capturant en continu une trace runtime légère en mémoire, permettant à votre programme de sauvegarder un instantané des dernières secondes d'activité dans un fichier chaque fois qu'un événement significatif se produit.

## Mises à jour des plateformes

* macOS 12 (Monterey) est désormais la version minimale prise en charge.
    
* Le support de Windows/ARM 32 bits est obsolète et sera supprimé dans Go 1.26.
    
* RISC-V et Loong64 ont acquis de nouvelles capacités comme la construction de plugins et la détection de concurrence (race detection).
    

## Points clés à retenir

* **Plus sûr par défaut** : plus de bugs de pointeurs nil silencieux, meilleur rapport de panic.
    
* **Compilations et runtime plus rapides** : informations de débogage DWARF v5, planification consciente des conteneurs et améliorations optionnelles du GC.
    
* **Meilleur outillage** : `go vet` plus intelligent, détection de fuites de mémoire, doc locale.
    
* **JSON moderne** : `encoding/json/v2` est l'avenir, avec d'énormes gains de performance.
    

Go 1.25 apporte des améliorations significatives en termes de performance, de justesse et d'expérience développeur. De l'utilisation plus intelligente du CPU dans les conteneurs à la réduction de la charge du garbage collector, d'un comportement runtime plus prévisible aux nouveaux outils comme FlightRecorder, cette version montre l'engagement de Go à rester simple tout en évoluant avec les charges de travail modernes. Si vous ne l'avez pas encore essayée, c'est le moment : mettez à jour, expérimentez les nouvelles fonctionnalités et voyez comment elles peuvent rendre vos applications plus rapides, plus sûres et plus faciles à déboguer.

## Sources

[https://go.dev/doc/go1.25](https://go.dev/doc/go1.25)