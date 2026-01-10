---
title: Comment effectuer des tests de fuzzing sur les services HTTP Golang
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-11-04T21:51:34.458Z'
originalURL: https://freecodecamp.org/news/how-to-fuzz-test-golang-http-services
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1730664559414/b64781c3-341f-4a5d-94fe-38ff78099b42.png
tags:
- name: Go Language
  slug: go
- name: Testing
  slug: testing
- name: fuzzing
  slug: fuzzing
seo_title: Comment effectuer des tests de fuzzing sur les services HTTP Golang
seo_desc: 'As a developer, you can’t always envision all of the possible inputs your
  programs or functions might receive.

  Even though you can define the major edge cases, you still can’t predict how your
  program will behave in the case of some weird unexpected ...'
---

En tant que développeur, vous ne pouvez pas toujours imaginer toutes les entrées possibles que vos programmes ou fonctions pourraient recevoir.

Même si vous pouvez définir les principaux cas limites, vous ne pouvez toujours pas prédire comment votre programme se comportera en cas d'entrée inattendue étrange. En d'autres termes, vous ne pouvez généralement trouver que les bugs que vous *vous attendez* à trouver.

C'est là que les tests de fuzzing ou le fuzzing viennent à la rescousse. Et dans ce tutoriel, vous apprendrez comment effectuer des tests de fuzzing en Go.

## Table des matières

* [Qu'est-ce que le Fuzz Testing](#heading-quest-ce-que-le-fuzz-testing)?
    
* [Fuzz Testing en Go](#heading-fuzz-testing-en-go)
    
* [Fuzzing des services HTTP](#heading-fuzzing-des-services-http)
    
* [Conclusion](#heading-conclusion)
    
* [Ressources](#heading-ressources)
    

## Qu'est-ce que le Fuzz Testing?

Le fuzzing est une technique automatisée de test de logiciels qui consiste à entrer une grande quantité de données aléatoires valides, presque valides ou invalides dans un programme informatique et à observer son comportement et sa sortie. L'objectif du fuzzing est donc de révéler des bugs, des plantages et des vulnérabilités de sécurité dans le code source que vous ne trouveriez peut-être pas par des méthodes de test traditionnelles.

La vidéo [Fuzz Testing in Go](https://youtu.be/w8STTZWdG9Y), que j'ai réalisée il y a quelques années, montre un exemple très simple de code Go qui peut bien fonctionner sauf si vous fournissez une certaine entrée :

```go
func Equal(a []byte, b []byte) bool {
  for i := range a {
    // peut provoquer une panique avec une erreur d'exécution : index hors limites.
    if a[i] != b[i] {
      return false
    }
  }

  return true
}
```

Cette fonction d'exemple fonctionne parfaitement tant que la longueur des deux tranches est égale. Mais elle va paniquer lorsque la première tranche est plus longue que la seconde (erreur d'index hors limites). De plus, elle ne retourne pas un résultat correct lorsque la deuxième tranche est un sous-ensemble de la première.

La technique de fuzzing repérerait facilement ce bug en bombardant cette fonction avec diverses entrées.

Il est bon de pratique d'intégrer le fuzzing dans le cycle de développement logiciel (SDLC) de votre équipe. Par exemple, Microsoft utilise le fuzzing comme [l'une des étapes de son SDLC](https://learn.microsoft.com/en-us/compliance/assurance/assurance-microsoft-security-development-lifecycle), pour trouver des bugs et vulnérabilités potentiels.

## Fuzz Testing en Go

Il existe de nombreux outils de fuzzing disponibles depuis un certain temps, comme [oss-fuzz](https://github.com/google/oss-fuzz), par exemple, mais depuis Go 1.18, le fuzzing a été ajouté à la bibliothèque standard de Go. Il fait donc maintenant partie du package de test régulier, car c'est une sorte de test. Vous pouvez également l'utiliser avec les autres primitives de test, ce qui est bien.

Les étapes pour créer un test de fuzzing en Go sont les suivantes :

1. Dans un fichier **_test.go**, créez une fonction qui commence par `Fuzz` et qui accepte `*testing.F`.
    
2. Ajoutez des seeds de corpus en utilisant `f.Add()` pour permettre au fuzzer de générer les données en fonction de celles-ci.
    
3. Appelez la cible de fuzzing en utilisant `f.Fuzz()` en passant les arguments de fuzzing que notre fonction cible accepte.
    
4. Lancez le fuzzer en utilisant la commande `go test` régulière, mais avec le flag `--fuzz=Fuzz`.
    

Notez que les arguments de fuzzing ne peuvent être que des types suivants :

* string, byte, []byte
    
* int, int8, int16, int32/rune, int64
    
* uint, uint8, uint16, uint32, uint64
    
* float32, float64
    
* bool
    

Un simple test de fuzzing pour la fonction **Equal** ci-dessus pourrait ressembler à ceci :

```go
// Test de fuzzing
func FuzzEqual(f *testing.F) {
  // Ajout de seed de corpus
  f.Add([]byte{'f', 'u', 'z', 'z'}, []byte{'t', 'e', 's', 't'})

  // Cible de fuzzing avec des arguments de fuzzing
  f.Fuzz(func(t *testing.T, a []byte, b []byte) {
    // Appel de notre fonction cible et passage des arguments de fuzzing
    Equal(a, b)
  })
}
```

Par défaut, les tests de fuzzing s'exécutent indéfiniment, vous devez donc soit spécifier la limite de temps, soit attendre que les tests de fuzzing échouent. Vous pouvez spécifier quels tests exécuter en utilisant l'argument `--fuzz`.

```bash
go test --fuzz=Fuzz -fuzztime=10s
```

Si des erreurs surviennent pendant l'exécution, la sortie devrait ressembler à ceci :

```bash
go test --fuzz=Fuzz -fuzztime=30s
--- FAIL: FuzzEqual (0.02s)
    --- FAIL: FuzzEqual (0.00s)
        testing.go:1591: panic: runtime error: index out of range
    Failing input written to testdata/fuzz/FuzzEqual/84ed65595ad05a58
    To re-run:
    go test -run=FuzzEqual/84ed65595ad05a58
```

Remarquez que l'entrée pour laquelle le test `fuzz` a échoué est écrite dans un fichier dans le dossier `testdata` et peut être rejouée en utilisant cet identifiant d'entrée.

```bash
go test -run=FuzzEqual/84ed65595ad05a58
```

Le dossier `testdata` peut être ajouté au dépôt et utilisé pour les tests réguliers, car les tests de fuzzing peuvent également agir comme des tests réguliers lorsqu'ils sont exécutés sans le flag `--fuzz`.

## Fuzzing des services HTTP

Il est également possible de tester les services HTTP en écrivant un test pour votre `HandlerFunc` et en utilisant le package `httptest`. Cela peut être très utile si vous devez tester l'ensemble du service HTTP, et pas seulement les fonctions sous-jacentes.

Introduisons maintenant un exemple plus réaliste, comme un gestionnaire HTTP qui accepte certaines entrées utilisateur dans le corps de la requête, puis écrivons un test de fuzzing pour celui-ci.

Notre gestionnaire accepte une requête JSON avec les champs `limit` et `offset` pour paginer certaines données statiques simulées. Définissons d'abord les types.

```go
type Request struct {
  Limit  int `json:"limit"`
  Offset int `json:"offset"`
}

type Response struct {
  Results    []int `json:"items"`
  PagesCount int   `json:"pagesCount"`
}
```

Notre fonction de gestionnaire analyse ensuite le JSON, pagine la tranche statique et retourne un nouveau JSON en réponse.

```go
func ProcessRequest(w http.ResponseWriter, r *http.Request) {
 var req Request

  // Décoder la requête JSON
  if err := json.NewDecoder(r.Body).Decode(&req); err != nil {
    http.Error(w, err.Error(), http.StatusBadRequest)
    return
  }

 // Appliquer le décalage et la limite à certaines données statiques
 all := make([]int, 1000)
 start := req.Offset
 end := req.Offset + req.Limit
 res := Response{
   Results:    all[start:end],
   PagesCount: len(all) / req.Limit,
 }

 // Envoyer la réponse JSON
 if err := json.NewEncoder(w).Encode(res); err != nil {
   http.Error(w, err.Error(), http.StatusInternalServerError)
   return
 }

 w.WriteHeader(http.StatusOK)
}
```

Comme vous l'avez peut-être déjà remarqué, cette fonction ne gère pas très bien les opérations sur les tranches et peut facilement provoquer une `panique`. Elle peut également paniquer si elle essaie de diviser par 0. C'est bien si nous pouvons repérer cela pendant le développement ou en utilisant uniquement des tests unitaires, mais parfois tout n'est pas visible à notre œil, et notre gestionnaire peut transmettre l'entrée à d'autres fonctions et ainsi de suite.

En suivant notre exemple `FuzzEqual` ci-dessus, implémentons un test de fuzzing pour le gestionnaire `ProcessRequest`. La première chose à faire est de fournir les entrées d'exemple pour le fuzzer. Ce sont les données que le fuzzer utilisera et modifiera pour générer de nouvelles entrées à essayer. Nous pouvons créer une requête JSON d'exemple et utiliser `f.Add()` avec le type `[]byte`.

```go
func FuzzProcessRequest(f *testing.F) {
  // Créer des entrées d'exemple pour le fuzzer
  testRequests := []Request{
    {Limit: -10, Offset: -10},
    {Limit: 0, Offset: 0},
    {Limit: 100, Offset: 100},
    {Limit: 200, Offset: 200},
  }

  // Ajouter au corpus de seeds
  for _, r := range testRequests {
    if data, err := json.Marshal(r); err == nil {
      f.Add(data)
    }
  }

  // ...
}
```

Après cela, nous pouvons utiliser le package **httptest** pour créer un serveur HTTP de test et faire des requêtes.

Note : Comme notre fuzzer peut générer des requêtes non-JSON invalides, il est préférable de simplement les ignorer avec `t.Skip()`. Nous pouvons également ignorer les erreurs `BadRequest`.

```go
func FuzzProcessRequest(f *testing.F) {
  // ...
  // Créer un serveur de test
  srv := httptest.NewServer(http.HandlerFunc(ProcessRequest))
  defer srv.Close()

  // Cible de fuzzing avec un seul argument []byte
  f.Fuzz(func(t *testing.T, data []byte) {
    var req Request
    if err := json.Unmarshal(data, &req); err != nil {
      // Ignorer les requêtes JSON invalides qui peuvent être générées pendant le fuzzing
      t.Skip("json invalide")
    }

    // Transmettre les données au serveur
    resp, err := http.DefaultClient.Post(srv.URL, "application/json", bytes.NewBuffer(data))
    if err != nil {
      t.Fatalf("impossible d'appeler le serveur: %v, données: %s", err, string(data))
    }
    defer resp.Body.Close()

    // Ignorer les erreurs BadRequest
    if resp.StatusCode == http.StatusBadRequest {
      t.Skip("json invalide")
    }

    // Vérifier le code de statut
    if resp.StatusCode != http.StatusOK {
      t.Fatalf("code de statut non-200 %d", resp.StatusCode)
    }
  })
}
```

Notre cible de fuzzing a un seul argument de type `[]byte` qui contient la requête JSON complète, mais vous pouvez le modifier pour avoir plusieurs arguments.

Tout est prêt maintenant pour exécuter nos tests de fuzzing. Lors du fuzzing de serveurs HTTP, vous devrez peut-être ajuster le nombre de travailleurs parallèles, sinon la charge pourrait submerger le serveur de test. Vous pouvez le faire en définissant le flag `-parallel=1`.

```bash
go test --fuzz=Fuzz -fuzztime=10s -parallel=1
go test --fuzz=Fuzz -fuzztime=30s
--- FAIL: FuzzProcessRequest (0.02s)
    --- FAIL: FuzzProcessRequest (0.00s)
        runtime error: integer divide by zero
        runtime error: slice bounds out of range
```

Et comme prévu, nous verrons les erreurs ci-dessus découvertes.

Nous pouvons également voir les entrées de fuzzing dans le dossier `testdata` pour voir quel JSON a contribué à cet échec. Voici un exemple du contenu du fichier :

```bash
go test fuzz v1
[]byte("{\"limit\":0,\"offset\":0}")
```

Pour corriger ce problème, nous pouvons introduire une validation des entrées et des paramètres par défaut :

```go
if req.Limit <= 0 {
  req.Limit = 1
}
if req.Offset < 0 {
  req.Offset = 0
}
if req.Offset > len(all) {
  start = len(all) - 1
}
if end > len(all) {
  end = len(all)
}
```

Avec cette modification, les tests de fuzzing s'exécuteront pendant 10 secondes et se termineront sans erreur.

## **Conclusion**

Écrire des tests de fuzzing pour vos services HTTP ou toute autre méthode est un excellent moyen de détecter des bugs difficiles à trouver. Les fuzzers peuvent détecter des bugs difficiles à repérer qui se produisent uniquement pour certaines entrées inattendues étranges.

C'est incroyable de voir que le fuzzing fait partie de la bibliothèque de test intégrée de Go, ce qui facilite sa combinaison avec les tests réguliers. Note : avant Go 1.18, les développeurs utilisaient [go-fuzz](https://github.com/dvyukov/go-fuzz), qui est également un excellent outil pour le fuzzing.

### **Ressources**

* [Code Source](https://github.com/plutov/packagemain/tree/master/fuzz-testing-http-services)
    
* [Fuzz Testing in Go](https://youtu.be/w8STTZWdG9Y)
    
* [Go Fuzzing](https://go.dev/doc/security/fuzz/)