---
title: Comment écrire des applications en ligne de commande rapides et amusantes avec
  Golang
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2016-10-24T04:29:16.000Z'
originalURL: https://freecodecamp.org/news/writing-command-line-applications-in-go-2bc8c0ace79d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*8Y-A5uFE028SqeflYpJ-7Q.png
tags:
- name: golang
  slug: golang
- name: learn to code
  slug: learn-to-code
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Tutorial
  slug: tutorial
seo_title: Comment écrire des applications en ligne de commande rapides et amusantes
  avec Golang
seo_desc: 'By Peter Benjamin

  A while back, I wrote an article about “Writing Command-Line Applications in NodeJS”.

  I love JavaScript, Node.JS, npm, and the whole ecosystem. To me, nothing feels more
  natural than writing modern JavaScript applications with ES6 o...'
---

Par Peter Benjamin

Il y a quelque temps, j'ai écrit un article sur « [Écrire des applications en ligne de commande en NodeJS](https://medium.freecodecamp.com/writing-command-line-applications-in-nodejs-2cf8327eee2) ».

J'adore JavaScript, Node.JS, npm et tout l'écosystème. Pour moi, rien ne semble plus naturel que d'écrire des applications JavaScript modernes avec ES6 ou TypeScript.

Mais, récemment, j'ai eu besoin de tirer parti de la concurrency multi-processeur (parallèle). En raison de la boucle d'événements à thread unique de NodeJS, NodeJS est concurrent, mais pas parallèle. NodeJS ne supporte pas la concurrency parallèle « hors de la boîte ».

#### Pourquoi Go ?

Le langage Go (souvent appelé « Golang »), utilisera tous les cœurs d'une machine par défaut. Go apporte également les avantages suivants :

* Sécurité des types (par exemple, vous ne pouvez pas passer une chaîne à une fonction qui attend un nombre — le compilateur se plaindra)
* Refactoring facile (par exemple, changer le nom d'une fonction ou d'une variable propagera ce changement dans tout le projet)
* Vitesse et performance dès la sortie de la boîte
* Le paradigme de programmation procédurale est certainement beaucoup plus facile à comprendre
* Déploiements faciles (il suffit de déployer le fichier binaire unique et c'est tout !)
* Style standard (Go est exigeant sur la mise en forme et vient avec des outils pour automatiser cela)
* … et bien plus encore !

**Note :** Il est important pour les nouveaux développeurs de **ne pas** être intimidés par les nouveaux concepts. Embrassez ce sentiment d'inconfort que vous ressentez lorsque vous êtes confronté à un nouveau défi. Cela signifie que vous apprenez, grandissez et vous améliorez. Une qualité clé des développeurs réussis est la _persévérance_.

Voici ce que vous apprendrez en suivant cet article :

1. Espaces de noms
2. Imports
3. Variables
4. Structs
5. Fonctions
6. Références et pointeurs
7. Conditions **_If_**
8. Boucles **_For_**

### Getting Started

Afin d'éviter d'alourdir cet article en ayant à supporter différentes commandes pour 3 plateformes différentes, je vais supposer que vous suivez sur [Cloud9](http://c9.io). Cloud9 est un IDE en ligne (environnement de développement intégré) — en gros, c'est génial !

#### Install

Go est déjà préinstallé sur les espaces de travail _blank Ubuntu_ de Cloud9. Vous pouvez donc sauter cette étape.

Si vous souhaitez suivre sur votre ordinateur local, vous pouvez [télécharger et installer Go](https://golang.org/dl/).

#### Installation

Go nécessite que vous configuriez votre environnement d'une manière particulière.

* Vous devez avoir un espace pour tous vos projets Go. Go appelle cet espace un **_workspace_**. Le workspace doit contenir 3 répertoires : _bin_ (pour les binaires), _pkg_ et _src_ (pour le code source) :

```bash
$ pwd
/home/ubuntu/workspace

$ mkdir {bin,src,pkg}
```

* Go suppose que chaque projet vit dans son propre dépôt, donc nous devons organiser davantage notre répertoire _src_ :

```bash
$ mkdir -p src/github.com/<votre_nom_utilisateur_github>/<nom_du_projet>
```

**Note :** Si vous êtes un utilisateur de _gitlab_ ou de _bitbucket_, changez simplement _github.com_ par le nom approprié (par exemple _gitlab.com_ ou _bitbucket.org_ respectivement).

Il y a une raison pour cette structure de répertoire. Go n'a pas de dépôt de code centralisé, comme NPM ou RubyGems. Go peut récupérer le code source directement depuis les systèmes de contrôle de version en ligne (VCS) et, lorsqu'il le fait, il téléchargera le code source dans le chemin correct. Par exemple, la commande suivante :

```
$ go get golang.org/x/tools/cmd/goimports
```

indiquera à Go de contacter golang.org, puis de télécharger la source sous :

```bash
<votre_espace_de_travail_go>/src/golang.org/x/tools/cmd/goimports
```

Ce qui, en retour, permet à Go de trouver des packages et bibliothèques tiers lorsque vous les importez dans votre projet.

* Enfin, nous devons configurer notre variable d'environnement _GOPATH_. Dans Cloud9 Ubuntu, ajoutez simplement ce qui suit à la fin de _.bashrc_ :

```
# dans ~/.bashrc
...
export GOPATH="/home/ubuntu/workspace"
export PATH="$PATH:$GOPATH/bin"
```

Ensuite, enregistrez le fichier et exécutez la commande suivante dans le terminal :

```bash
source ~/.bashrc
```

* Pour vérifier que Go fonctionne sur Cloud9 et que notre GOPATH est configuré correctement :

```bash
$ go version
go version go1.6 linux/amd64

$ go get golang.org/x/tools/cmd/goimports
$ goimports --help
usage: goimports [flags] [path ...]
...
```

Pour plus d'informations sur la configuration de Golang, visitez [la documentation officielle « Getting Started »](https://golang.org/doc/code.html).

### C'est parti !

Notre objectif : créer une application CLI minimale pour interroger les [utilisateurs](https://api.github.com/users) de [GitHub](https://api.github.com/).

Créons un dépôt pour ce projet sur Github.com. Appelez-le **gitgo**. Ensuite, clonez-le :

```bash
$ cd $GOPATH/src/github.com/<votre_nom_utilisateur_github>
$ git clone git@github.com:<votre_nom_utilisateur_github>/gitgo.git
```

#### Un aperçu de Go

Créons notre premier fichier, appelons-le **_main.go_**, et écrivons le code suivant (ne vous inquiétez pas, nous couvrirons chaque ligne) :

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World")
}
```

#### Décomposons cela...

```
package main
```

* Il s'agit d'une déclaration d'espace de noms. Les espaces de noms sont simplement un moyen pour nous de regrouper la logique et la fonctionnalité. Vous verrez comment les espaces de noms nous aideront un peu plus tard.
* Le mot **_main_** est un mot-clé. Il indique au compilateur GO que notre code est destiné à être exécuté en tant qu'**_application_** et non en tant que **_bibliothèque_**. La différence est que les **_applications_** sont utilisées directement par nos utilisateurs, tandis que les **_bibliothèques_** ne peuvent être importées et utilisées que par d'autres morceaux de code.

```
Import "fmt"
```

* Instruction d'importation. Cela importe le package "[fmt](https://golang.org/pkg/)" (abréviation de "format") de la [bibliothèque standard](https://golang.org/pkg/).

```
func main()
```

* **_func_** est le mot-clé pour définir ou déclarer une fonction en GO.
* Le mot **_main_** est un mot-clé spécial en GO. Il indique au compilateur GO que notre application commence ici !

```
fmt.Println("Hello, World")
```

* Cela est assez explicite. Nous utilisons la fonction **Println** du package **fmt** que nous avons importé précédemment pour... eh bien... imprimer une ligne.

Remarquez que la première lettre de la fonction **Println** est en majuscule. C'est la manière de GO d'exporter des variables, des fonctions et d'autres éléments. Si la première lettre de votre fonction ou variable est en majuscule, cela signifie que vous la rendez accessible aux packages ou espaces de noms externes.

#### Exécutons-le !

```bash
$ go run main.go
Hello, World
```

Génial ! Vous avez écrit votre première application GO.  
Qu'est-ce qui vient de se passer ? Eh bien, GO a compilé **ET** exécuté l'application en mémoire ! Plutôt rapide, non ?

#### Construisons-le !

```bash
$ go build     # génère un binaire exécutable dans votre répertoire local 
$ ./gitgo
Hello, World
```

Super ! Vous venez de construire votre première application GO. Vous pouvez envoyer juste ce **seul** fichier à vos amis et à votre famille et ils peuvent l'exécuter et obtenir les **mêmes résultats**. Bien sûr, si ils exécutent Windows, cette application ne fonctionnera pas, car nous l'avons construite pour Linux/Unix. Alors, construisons-la pour Windows :

```bash
$ GOOS=windows go build -o forecaster.exe main.go
```

Et voilà ! Maintenant, vous avez créé une application pour Windows. Plutôt sympa, non ?

En fait, vous pouvez cross-compiler cette application pour une large gamme de plateformes (par exemple, Windows, Linux, OS X) et d'architectures (par exemple, i386, amd64). Vous pouvez voir la liste complète ici : [https://golang.org/doc/install/source#environment](https://golang.org/doc/install/source#environment)

#### Installons-le !

Si vous voulez que votre application soit accessible depuis n'importe où sur votre système :

```
$ go install
```

C'est tout. Maintenant, vous pouvez appeler votre application depuis n'importe où :

```bash
$ gitgo
Hello, World
```

À ce stade, il serait bon de vérifier votre travail dans GitHub :

```bash
$ git add .
$ git commit -am "Add main.go"
$ git push
```

Génial ! Mais jusqu'à présent, notre application ne fait pas grand-chose. Cet exercice était juste meant pour nous familiariser et nous donner une idée de ce que c'est que de coder en Go.

#### Maintenant, plongeons dans notre application CLI !

Nous envisageons que l'interaction avec notre application ressemble à quelque chose comme

```bash
$ gitgo -u pmbenjamin
# ou...
$ gitgo --user pmbenjamin,defunkt
```

Maintenant que nous avons une direction, commençons à créer ces flags.

Nous pourrions utiliser la bibliothèque standard **_flag_** en Go, mais, avec des essais et erreurs et un peu de recherche sur Google, vous découvrirez que la bibliothèque standard **_flag_** ne supporte pas la syntaxe des flags longs (via double tiret). Elle ne supporte que les tirets simples.

Heureusement, quelqu'un a déjà résolu ce problème avec une bibliothèque GO. Téléchargeons-la :

```bash
$ go get github.com/ogier/pflag
```

Maintenant, importons-la dans notre projet :

```go
import (

    "github.com/ogier/pflag"
)
```

En GO, le dernier élément de l'instruction d'importation est l'espace de noms que nous utilisons pour accéder aux fonctions de la bibliothèque :

```go
func main() {
    pflag.SomeFunction()
}
```

Si nous préférons utiliser un nom différent, nous pouvons aliaser nos noms de package à l'importation :

```go
import (

    flag "github.com/ogier/pflag"
)
```

Cela nous permettra de faire :

```go
func main(){
    flag.SomeFunction()
}
```

Ce qui est ce que vous voyez dans les [exemples officiels](https://github.com/ogier/pflag).

Créons les variables qui contiendront les données de l'entrée utilisateur :

```go
import (...)import (
...
)

// flags
var (
   user  string
)

func main() {
...
}
```

Quelques points à souligner ici :

* Nous avons déclaré nos variables _en dehors_ de `func main()`. Cela nous permet de référencer ces variables dans d'autres fonctions en plus de `func main()`. Cela peut vous sembler étrange, car vous ne voulez pas polluer l'espace de noms global. Mais, faites-moi confiance, cela est parfaitement acceptable en Go. Nous sommes limités à l'espace de noms actuel.
* Go est un langage à typage statique, ce qui signifie que vous devez spécifier le type de données qui sera stocké dans chaque variable (d'où les mots-clés `string`)

Maintenant que vous avez déclaré vos variables, déclarons vos flags et liez/mappez chaque flag à la variable appropriée :

```go
import (
    ...
)

// flags
var (
    ...
)

func main() {
 flag.Parse()
}

func init() {
 flag.StringVarP(&user, "user", "u", "", "Search Users")
}
```

#### Décomposons cela...

```
func init()
```

* **init** est une fonction spéciale en GO. GO exécute les applications dans l'ordre suivant :  
1. Instructions d'importation  
2. Déclarations de variables/constantes au niveau du package  
3. fonction init()  
4. fonction main() (si le projet doit être traité comme une application)
* Tout ce que nous essayons de faire est d'initialiser les flags une fois

```go
flag.StringVarP(&user, "user", "u", "", "Search Users")
```

* Du package/bibliothèque **flag**, nous utilisons la fonction **StringVarP()**.
* `StringVarP()` fait 3 choses :   
1. il indique à GO que nous évaluerons une **String**,  
2. il indique à GO que nous voulons lier une **Var**iable à ce flag, et  
3. il indique à GO que nous voulons avoir un flag conforme à **P**osix (par exemple, double tiret et flag à tiret simple)
* `StringVarP()` prend 5 arguments dans cet ordre :  
1. la variable à laquelle nous voulons lier ce flag,  
2. le flag à double tiret,  
3. le flag à tiret simple,  
4. la valeur par défaut à utiliser si le flag n'est pas explicitement appelé,  
5. et la description de ce flag
* `&user` signifie que nous passons une référence (alias adresse mémoire) de la variable **user**. OK, avant de commencer à paniquer à propos des références et des adresses mémoire, décomposons davantage ce concept...
* Dans de nombreux langages, comme JavaScript et Ruby, lorsque vous définissez une fonction qui prend un argument, puis appelez la fonction et lui passez un argument, vous créez essentiellement une nouvelle copie de la variable que vous passez en tant qu'argument. Mais, il y a des moments où vous ne voulez pas passer une copie des données. Parfois, vous devez opérer sur les données originales.
* Par conséquent, si vous passez les données par **valeur**, vous créez essentiellement une autre copie des données et passez cette copie, tandis que si vous passez la variable par **référence** (alias par son adresse mémoire), alors vous passez les données originales.
* En GO, vous pouvez obtenir l'adresse mémoire de presque n'importe quoi en préfixant le symbole esperluette (&).

```go
flag.Parse()
```

* Analyser les flags.

#### Testons notre travail...

```bash
$ go run main.go # rien ne se passe
$ go run main.go --help
Usage of /tmp/go-build375844749/command-line-arguments/_obj/exe/main:
  -u, --user string
        Search Users
exit status 2
```

Super. Cela semble fonctionner.

Remarquez le chemin étrange **_/tmp/go-build…_** ? C'est là que notre application a été compilée et exécutée dynamiquement par Go. Construisons-la et testons-la :

```bash
$ go install -v
$ gitgo --help
Usage of gitgo:
  -u, --user string
        Search Users
```

**Astuce Pro :** Lors de la construction ou de la compilation de binaires, préférez toujours `go install` à `go build`. `go install` mettra en cache les packages non principaux dans `$GOPATH/pkg`, ce qui entraînera des temps de construction plus rapides que `go build`.

#### Logique principale

Maintenant que nous avons initialisé nos flags, commençons à implémenter quelques fonctionnalités principales :

```go
func main() {
 // analyser les flags
 flag.Parse()
 
 // si l'utilisateur ne fournit pas de flags, imprimer l'utilisation
 // nous pouvons nettoyer cela plus tard en mettant cela dans sa propre fonction
  if flag.NFlag() == 0 {
     fmt.Printf("Usage: %s [options]\n", os.Args[0])
     fmt.Println("Options:")
     flag.PrintDefaults()
     os.Exit(1)
  }
  
  users = strings.Split(user, ",")
  fmt.Printf("Searching user(s): %s\n", users)
  
}
```

Notez qu'il n'y a pas de parenthèses autour des conditions **if** en Go.

#### Testons notre travail...

```bash
$ go install
# github.com/pmbenjamin/gitgo
./main.go:15: undefined: fmt in fmt.Printf
./main.go:15: undefined: os in os.Args
./main.go:16: undefined: fmt in fmt.Println
./main.go:18: undefined: os in os.Exit
./main.go:21: undefined: fmt in fmt.Printf
./main.go:24: undefined: fmt in fmt.Printf
```

J'ai intentionnellement voulu vous montrer l'expérience du compilateur Go lorsqu'il se plaint que vous avez fait quelque chose de mal. Il est important que nous soyons capables de comprendre ces messages d'erreur pour corriger notre code.

Donc, le compilateur se plaint que nous utilisons la fonction `Println` du package **fmt**, mais que ce package est indéfini. Même chose avec `Exit` du package **os**.

Il s'avère que nous avons simplement oublié d'importer certains packages ! Dans un IDE normal (par exemple, Atom, VS-Code, vim, emacs… etc), il existe des plugins que vous pouvez installer dans votre éditeur qui importeront dynamiquement et automatiquement tous les packages manquants ! Vous n'avez donc pas à les importer manuellement. N'est-ce pas génial ?

Pour l'instant, ajoutons nous-mêmes les instructions d'importation correctes. Vous vous souvenez de l'outil `goimports` que nous avons installé plus tôt ?

```bash
$ goimports -w main.go # écrire les instructions d'importation dans main.go !
```

Et reconstruisons et retestons l'application :

```bash
$ go install

$ gitgo
Usage: gitgo [options]
Options:
  -u, --user string
        Search Users

$ gitgo -u pmbenjamin        
Searching user(s): [pmbenjamin]
```

Oui ! Cela fonctionne !

Et si l'utilisateur veut interroger plusieurs utilisateurs ?

```bash
$ gitgo -u pmbenjamin,defunkt
Searching user(s): [pmbenjamin defunkt]
```

Cela semble fonctionner aussi !

Maintenant, commençons à obtenir des données réelles. Il est toujours bon de encapsuler différentes fonctionnalités dans des fonctions séparées pour garder notre base de code propre et modulaire. Vous pouvez mettre cette fonction dans **main.go** ou dans un autre fichier. Je préfère un fichier séparé, car cela rendra notre application modulaire, réutilisable et facilement testable.

Pour gagner du temps, voici le code avec des commentaires pour expliquer.

[https://gist.github.com/petermbenjamin/8aeece9305bb44282799384365ab3a3c#file-user-go](https://gist.github.com/petermbenjamin/8aeece9305bb44282799384365ab3a3c#file-user-go)

#### Le gist est le suivant :

1. Dans `user.go`, nous envoyons une requête HTTP GET avec le nom d'utilisateur
2. Ensuite, nous lisons le corps de la réponse et stockons les données dans `resp`.
3. Il est bon de fermer le corps de la réponse avec l'instruction `defer` pour nettoyer après que notre fonction a échoué ou terminé.
4. Ensuite, nous analysons les données JSON avec la fonction `json.Unmarshal`, stockons les données utilisateur analysées dans la variable `user`, et les retournons.
5. Dans `main.go`, nous parcourons le tableau `users`, exécutons `getUser()` pour chaque utilisateur, et affichons les données que nous voulons.

### Améliorations futures

Ce projet était juste un guide d'introduction rapide pour les débutants. Je sais que ce projet peut être écrit un peu plus efficacement.

Dans mon prochain article, je prévois de plonger dans de nouveaux concepts, comme la concurrency (GoRoutines), les canaux, les tests, le vendoring, et l'écriture de bibliothèques Go (au lieu d'applications).

En attendant, le code complet du projet peut être trouvé [ici](https://github.com/pmbenjamin/gitgo).

N'hésitez pas à contribuer en ouvrant des problèmes GitHub ou en soumettant des PR.