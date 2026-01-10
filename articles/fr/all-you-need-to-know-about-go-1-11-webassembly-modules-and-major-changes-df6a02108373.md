---
title: Tout ce que vous devez savoir sur Go version 1.11
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-08-27T09:48:15.000Z'
originalURL: https://freecodecamp.org/news/all-you-need-to-know-about-go-1-11-webassembly-modules-and-major-changes-df6a02108373
coverImage: https://cdn-media-1.freecodecamp.org/images/1*ZhP-Sh-b9W-Y4IeI84prkw.png
tags:
- name: Go Language
  slug: go
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: WebAssembly
  slug: webassembly
seo_title: Tout ce que vous devez savoir sur Go version 1.11
seo_desc: 'By Ridham Tarpara

  Go 1.11 hit the ground on 24 August 2018. It introduces a few really needed tools
  and components such as versioned modules, WebAssembly support, and debugging improvements.
  It also brings some changes to core packages and performanc...'
---

Par Ridham Tarpara

Go 1.11 est sorti le 24 août 2018. Il introduit quelques outils et composants vraiment nécessaires tels que les modules versionnés, la prise en charge de WebAssembly et des améliorations de débogage. Il apporte également quelques changements aux packages principaux et aux performances/temps d'exécution.

Comme toujours, la version maintient la [promesse de compatibilité](https://golang.org/doc/go1compat.html) de Go 1. Ainsi, presque tous les programmes Go continuent à compiler et à s'exécuter comme avant avec cette mise à jour. Il n'y a pas de changements dans la spécification du langage.

Examinons ce qui est nouveau.

### **Modules**

Go 1.11 inclut une prise en charge expérimentale des modules Go, y compris une nouvelle commande `go get` consciente des modules.

Le moyen le plus rapide de tirer parti de la nouvelle prise en charge des modules est de cloner votre dépôt dans un répertoire **externe**, de créer un fichier go.mod et d'exécuter les commandes Go à partir de cet arbre de fichiers.

Démontrons cela. J'utilise les [bibliothèques de test testify puissantes et standard de Go](https://github.com/stretchr/testify).

Clonons le dépôt testify dans mon dossier préféré `~/proj/github`.

```
$ git clone https://github.com/stretchr/testify ~/proj/github/testify$ cd ~/proj/github/testify
```

Maintenant, pour utiliser les commandes Go à partir de ici, vous devez initialiser ce dépôt en tant que module avec la commande suivante :

```
go mod init github.com/stretchr/testify
```

Où `github.com/stretchr/testify` est l'emplacement où vous placeriez généralement ce dépôt, sous le dossier src de Go.

Cette commande créera un fichier go.mod à la racine du dossier. Dans un projet utilisant déjà un outil de gestion des dépendances existant comme godep, glide ou dep, `go mod init` ajoutera également des instructions require correspondant à la configuration existante.

Maintenant, si vous ouvrez le fichier `go.mod`, vous pouvez voir la liste des dépendances avec le nom du module.

```
$ vi go.mod
```

```
module github.com/stretchr/testify
```

```
require (    github.com/davecgh/go-spew v1.1.0    github.com/pmezard/go-difflib v1.0.0    github.com/stretchr/objx v0.1.0)
```

Comme vous le remarquerez, ces trois dépendances sont celles de testify. Voici le fichier `Gopkg.toml` de testify :

```
[prune] unused-packages = true non-go = true go-tests = true
```

```
[[constraint]] name = "github.com/davecgh/go-spew" version = "~1.1.0"
```

```
[[constraint]] name = "github.com/pmezard/go-difflib" version = "~1.0.0"
```

```
[[constraint]] name = "github.com/stretchr/objx" version = "~0.1.0"
```

Maintenant que le module a été initialisé, vous pouvez utiliser n'importe quelle commande Go à partir de ce dossier.

```
[1;34m~/proj/github/testify[0m [32mmaster*[0m $ go build                               go: finding github.com/davecgh/go-spew v1.1.0go: finding github.com/pmezard/go-difflib v1.0.0go: finding github.com/stretchr/objx v0.1.0go: downloading github.com/davecgh/go-spew v1.1.0go: downloading github.com/pmezard/go-difflib v1.0.0go: downloading github.com/stretchr/objx v0.1.0
```

```
[1;34m~/proj/github/testify[0m [32mmaster*[0m $ go test PASSok   github.com/stretchr/testify 0.001s
```

Ainsi, avec Go 1.11 et les modules, vous pouvez écrire vos modules Go _n'importe où vous le souhaitez et vous n'avez pas besoin de maintenir une copie_ dans un sous-répertoire spécifique de votre `$GOPATH`.

### WebAssembly

Go 1.11 ajoute un port expérimental vers WebAssembly.

> WebAssembly (abréviation _Wasm_) est un format d'instruction binaire pour une machine virtuelle basée sur une pile. Wasm est conçu comme une cible portable pour la compilation de langages de haut niveau comme C/C++/Rust, permettant le déploiement sur le web pour les applications client et serveur.

Maintenant, nous pouvons exécuter Go dans le navigateur, et vice versa — nous pouvons exécuter JavaScript dans Go facilement. Bien que cette fonctionnalité soit à l'état expérimental, elle est toujours très utile.

Cet petit exemple appelle Go depuis le Web :

**wasm-exec.html**

```
<!doctype html><!--Copyright 2018 The Go Authors. All rights reserved.Use of this source code is governed by a BSD-stylelicense that can be found in the LICENSE file.--><html>
```

```
<head>    <meta charset="utf-8">    <title>Go wasm</title></head>
```

```
<body>    <script src="wasm_exec.js"></script>    <script>        if (!WebAssembly.instantiateStreaming) { // polyfill            WebAssembly.instantiateStreaming = async (resp, importObject) => {                const source = await (await resp).arrayBuffer();                return await WebAssembly.instantiate(source, importObject);            };        }        const go = new Go();        let mod, inst;        WebAssembly.instantiateStreaming(fetch("test.wasm"), go.importObject).then((result) => {            mod = result.module;            inst = result.instance;            document.getElementById("runButton").disabled = false;        });        let printMessage // Notre référence au callback Go        let printMessageReceived // Notre promesse        let resolvePrintMessageReceived // Notre résolveur de promesse        function setPrintMessage(callback) {          printMessage = callback          resolvePrintMessageReceived()        }        async function run() {          console.clear()          // Crée la promesse et stocke sa fonction de résolution          printMessageReceived = new Promise(resolve => {            resolvePrintMessageReceived = resolve          })          const run = go.run(inst) // Démarre le binaire wasm          await printMessageReceived // Attend la réception du callback          printMessage('Hello Wasm!') // Invoque le callback          await run // Attend la terminaison du binaire          inst = await WebAssembly.instantiate(mod, go.importObject) // réinitialise l'instance        }    </script>
```

```
<button onClick="run();" id="runButton" disabled>Run</button></body>
```

```
</html>
```

**go-call.go**

```
package main
```

```
import (  "fmt"  "syscall/js")
```

```
var done = make(chan struct{})
```

```
func main() {  callback := js.NewCallback(printMessage)  defer callback.Release() // Différer la libération du callback est une bonne pratique  setPrintMessage := js.Global().Get("setPrintMessage")  setPrintMessage.Invoke(callback)  <-done}
```

```
func printMessage(args []js.Value) {  message := args[0].String()  fmt.Println(message)  done <- struct{}{} // Notifie que printMessage a été appelé}
```

Vous pouvez trouver plus d'exemples [ici](https://github.com/nlepage/golang-wasm/blob/master/examples). Et voici une vidéo sur [la construction d'une calculatrice avec WebAssembly](https://www.youtube.com/watch?v=4kBvvk2Bzis&feature=youtu.be).

### **Autres changements à considérer**

* Comme la prise en charge des modules Go attribue une signification spéciale au symbole `@` dans les opérations de ligne de commande, la commande `go` n'autorise plus l'utilisation de chemins d'importation contenant des symboles `@`.
* Avec la nouvelle API d'annotation utilisateur du package `runtime/trace`, les utilisateurs peuvent enregistrer des informations de niveau application dans les traces d'exécution et créer des groupes de goroutines liées. La commande `go tool trace` visualise ces informations dans la vue de trace et la nouvelle page d'analyse des tâches/régions utilisateur.
* Le runtime utilise maintenant une disposition de tas clairsemée, il n'y a donc plus de limite à la taille du tas Go (auparavant, la limite était de 512 GiB). Cela corrige également les rares échecs de "conflit d'espace d'adressage" dans les binaires mixtes Go/C ou les binaires compilés avec `-race`.
* [time](https://golang.org/pkg/time/) : L'analyse des fuseaux horaires désignés par un signe et un décalage est maintenant prise en charge. Dans les versions précédentes, les noms de fuseaux horaires numériques (tels que `+03`) n'étaient pas considérés comme valides, et seules les abréviations en trois lettres (telles que `MST`) étaient acceptées lors de l'attente d'un nom de fuseau horaire.
* [text/scanner](https://golang.org/pkg/text/scanner/) : La méthode `[Scanner.Scan](https://golang.org/pkg/text/scanner/#Scanner.Scan)` retourne maintenant le jeton `[RawString](https://golang.org/pkg/text/scanner/#RawString)` au lieu de `[String](https://golang.org/pkg/text/scanner/#String)` pour les littéraux de chaîne brute.
* Il y a des changements dans [crypto](https://golang.org/pkg/crypto/), [encoding](https://golang.org/pkg/encoding/), [net/http](https://golang.org/pkg/net/http/), [os](https://golang.org/pkg/os/), [runtime](https://golang.org/pkg/runtime/), [sync](https://golang.org/pkg/sync/), [mime](https://golang.org/pkg/mime/) et quelques autres que vous pouvez lire [ici](https://golang.org/doc/go1.11#library).

Si vous avez aimé cet article, offrez-moi quelques applaudissements — cela signifie beaucoup pour l'auteur. Suivez-moi si vous voulez lire plus d'articles sur Go, JavaScript, la Technologie et les Startups.