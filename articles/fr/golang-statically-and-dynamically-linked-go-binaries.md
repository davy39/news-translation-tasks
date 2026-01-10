---
title: Comment fonctionnent les binaires Go liés statiquement et dynamiquement
subtitle: ''
author: Alex Pliutau
co_authors: []
series: null
date: '2024-09-10T14:14:23.514Z'
originalURL: https://freecodecamp.org/news/golang-statically-and-dynamically-linked-go-binaries
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725977444176/20f3bebf-e250-45c3-926e-146d50e4db93.png
tags:
- name: Go Language
  slug: go
- name: Linux
  slug: linux
- name: compiler
  slug: compiler
seo_title: Comment fonctionnent les binaires Go liés statiquement et dynamiquement
seo_desc: 'One of the biggest strengths of Go is its compiler. It abstracts many things
  for you and lets you compile your program easily for almost any platform and architecture.

  And though it seems easy, there are some nuances to it and multiple ways of compil...'
---

L'un des plus grands atouts de Go est son compilateur. Il abstrait de nombreuses choses pour vous et vous permet de compiler facilement votre programme pour presque n'importe quelle [plateforme et architecture](https://pkg.go.dev/cmd/dist).

Et bien que cela semble facile, il existe certaines nuances et plusieurs façons de compiler le même programme, ce qui donne différents exécutables.

Dans cet article, nous explorerons les exécutables liés statiquement et dynamiquement, les linkers internes et externes, et nous examinerons les binaires à l'aide d'outils tels que **file, ld** et **ldd**.

### Voici ce que nous allons aborder :

* [Aperçu](#heading-apercu)
    
* [Qu'est-ce que le liage statique et dynamique ?](#heading-quest-ce-que-le-liage-statique-et-dynamique)
    
* [Programme lié statiquement](#heading-programme-lie-statiquement)
    
* [Qu'est-ce qu'un binaire, au fait ?](#heading-quest-ce-quun-binaire-au-fait)
    
* [Programme lié dynamiquement](#heading-programme-lie-dynamiquement)
    
* [Pouvons-nous le lier statiquement ?](#heading-pouvons-nous-le-lier-statiquement)
    
* [Linker interne vs externe](#heading-linker-interne-vs-externe)
    
* [Cross-compilation](#heading-cross-compilation)
    
* [Point Bonus : Réduire la taille du binaire](#heading-point-bonus-reduire-la-taille-du-binaire)
    
* [Attention : l'astuce LD_PRELOAD](#heading-attention-lastuce-ld-preload)
    
* [Conclusion](#heading-conclusion)
    
* [Lectures complémentaires](#heading-lectures-complementaires)
    

## Qu'est-ce que le liage statique et dynamique ?

Le **liage statique** est la pratique consistant à copier toutes les bibliothèques dont votre programme a besoin directement dans l'image finale du fichier exécutable.

Et Go *adore et privilégie* cela dès que possible. C'est parce que c'est plus portable, car cela ne nécessite pas la présence de la bibliothèque sur le système hôte où il s'exécute. Ainsi, votre binaire peut s'exécuter sur n'importe quel système, peu importe la distribution ou la version, et il ne dépendra d'aucune bibliothèque système.

Le **liage dynamique**, en revanche, se produit lorsque des bibliothèques externes ou partagées sont copiées dans le fichier exécutable *par nom pendant l'exécution*.

Et cela présente aussi ses propres avantages. Par exemple, le programme peut réutiliser des bibliothèques **libc** populaires disponibles sur le système hôte et ne pas les réimplémenter. Vous pouvez également bénéficier des mises à jour de l'hôte sans relier votre programme. Cela peut aussi réduire la taille du fichier exécutable dans de nombreux cas.

## Programme lié statiquement

Examinons un programme qui sera *toujours* lié statiquement. Ce programme n'appelle pas de code C en utilisant [**cgo**](https://pkg.go.dev/cmd/cgo), donc tout peut être empaqueté dans un binaire statique. Notre programme affiche seulement un message simple sur stdout, ce que Go peut faire en interne sans avoir besoin d'utiliser quelque chose de la **libc**.

```go
package main

import "fmt"

func main() {
	fmt.Println("hi, user")
}
```

## Qu'est-ce qu'un binaire, au fait ?

Nous pouvons d'abord utiliser le programme [**file**](https://www.man7.org/linux/man-pages/man1/file.1.html) pour examiner le type de fichier.

```bash
$ go build main1.go

$ file main1 | tr , '\n'
main1: ELF 64-bit LSB executable
 ARM aarch64
 version 1 (SYSV)
 statically linked
 Go BuildID=...
 with debug_info
 not stripped
```

Il nous indique qu'il s'agit d'un fichier exécutable [**ELF**](https://wiki.osdev.org/ELF) (Executable and Linkable Format). Il nous indique également qu'il est « lié statiquement ».

Nous ne plongerons pas dans ce qu'est ELF, mais il existe d'autres formats de fichiers exécutables. ELF est celui par défaut sur Linux, Mach-O est celui par défaut pour macOS, PE/PE32+ pour Windows, et ainsi de loin.

Note : dans cet article, nous travaillerons avec Linux (Ubuntu) et ses outils, mais la même chose est possible sur d'autres plateformes.

Et il existe un autre programme Linux appelé [**ldd**](https://man7.org/linux/man-pages/man1/ldd.1.html) qui peut nous dire si le binaire est lié statiquement ou dynamiquement.

```bash
$ ldd main1
not a dynamic executable
```

## Programme lié dynamiquement

Comme mentionné plus haut, Go dispose d'un mécanisme appelé **cgo** pour appeler du code C depuis Go. Même la stdlib de Go l'utilise à plusieurs endroits – par exemple dans le package [**net**](https://pkg.go.dev/net), où elle utilise la bibliothèque C standard pour travailler avec le DNS.

L'importation de tels packages ou l'utilisation de cgo dans votre code produit par défaut un binaire lié dynamiquement, lié à ces bibliothèques **libc**.

```go
package main

import (
	"fmt"
	"log"
	"net"
)

func main() {
	ipv4Addr, ipv4Net, err := net.ParseCIDR("192.0.2.1/24")
	if err != nil {
		log.Fatal(err)
	}
	fmt.Println(ipv4Addr)
	fmt.Println(ipv4Net)
}
```

Nous pouvons utiliser à nouveau nos programmes **file** et **ldd** pour examiner le second binaire.

```bash
$ go build main2.go

$ file main2 | tr , '\n'
main2: ELF 64-bit LSB executable
 ARM aarch64
 version 1 (SYSV)
 dynamically linked
 interpreter /lib/ld-linux-aarch64.so.1
 Go BuildID=...
 with debug_info
 not stripped

$ ldd main2
	linux-vdso.so.1 (0x0000ffff87c81000)
	libc.so.6 => /lib/aarch64-linux-gnu/libc.so.6 (0x0000ffff87a80000)
	/lib/ld-linux-aarch64.so.1 (0x0000ffff87c44000)
```

Le programme **file** montre maintenant qu'il s'agit d'un binaire **lié dynamiquement** et **ldd** nous montre les dépendances dynamiques de notre binaire. Dans ce cas, il repose sur **libc.so.6** et **ld-linux** qui est un linker dynamique pour les systèmes Linux.

## Pouvons-nous le lier statiquement ?

Il existe de multiples raisons pour lesquelles vous pourriez vouloir que vos binaires soient statiques, mais la principale est de faciliter le déploiement et la distribution. Mais ! Ce n'est pas toujours nécessaire, et en liant la **libc**, vous bénéficiez des mises à jour de l'hôte. De plus, dans le cas de notre package **net**, vous utilisez ces fonctions complexes de recherche DNS incluses dans la **libc**.

Ce qui est intéressant, c'est que le package net de Go possède également une version pur-Go, ce qui permet de désactiver cgo au moment de la compilation. Vous pouvez le faire en spécifiant des build tags ou en désactivant complètement cgo avec **CGO_ENABLED=0**.

```bash
$ go build -tags netgo main2.go
$ ldd main2
not a dynamic executable

$ CGO_ENABLED=0 go build main2.go
$ ldd main2
not a dynamic executable
```

Ce qui précède prouve que nous obtenons un binaire statique dans les deux cas.

## Linker interne vs externe

Un linker est un programme qui lit l'archive Go ou l'objet d'un package main, ainsi que ses dépendances, et les combine en un binaire exécutable.

Par défaut, la chaîne d'outils de Go utilise son linker interne ([go tool link](https://pkg.go.dev/cmd/link)), mais vous pouvez spécifier quel linker utiliser au moment de la compilation. Cela peut vous offrir une combinaison des avantages d'un binaire statique ainsi que les capacités complètes de la libc.

Sur Linux, le linker par défaut est le [**ld**](https://man7.org/linux/man-pages/man1/ld.1.html) de gcc. Et nous pouvons lui dire de produire un binaire statique.

```bash
$ go build -ldflags "-linkmode 'external' -extldflags '-static'" main2.go
# arguments-de-ligne-de-commande
/usr/bin/ld: /tmp/go-link-629224677/000004.o: in function `_cgo_97ab22c4dc7b_C2func_getaddrinfo':
/tmp/go-build/cgo_unix_cgo.cgo2.c:60:(.text+0x30):
warning: Using 'getaddrinfo' in statically linked applications requires at runtime the shared libraries from the glibc version used for linking
$ ldd main2
not a dynamic executable
```

Cela fonctionne, mais nous avons un avertissement ici. Dans notre cas, **glibc** utilise **libnss** pour supporter un certain nombre de fournisseurs différents pour les services de résolution d'adresses, et vous ne pouvez pas lier libnss de manière statique.

D'autres packages cgo peuvent produire des avertissements similaires et vous devrez consulter la documentation pour voir s'ils sont critiques ou non.

## Cross-compilation

Comme mentionné dans l'introduction, la cross-compilation est une fonctionnalité très appréciable de Go. Elle vous permet de compiler votre programme pour presque n'importe quelle plateforme/architecture. Mais cela peut être très complexe si votre programme utilise **cgo**, car il est généralement difficile de cross-compiler du code C.

```bash
$ CGO_ENABLED=0 GOOS=darwin GOARCH=arm64 go build main2.go
$ CGO_ENABLED=1 GOOS=darwin GOARCH=arm64 go build main2.go
# runtime/cgo
cgo: C compiler "clang" not found: exec: "clang":
executable file not found in $PATH
```

Vous pouvez surmonter cela en installant la chaîne d'outils pour l'OS et/ou l'architecture cible.

Si vous le pouvez, il est toujours préférable de ne pas utiliser **cgo** pour la cross-compilation. Vous obtiendrez des binaires stables qui sont liés statiquement.

## Point Bonus : Réduire la taille du binaire

Comme vous l'avez peut-être remarqué, la sortie de la commande **file** ci-dessus contenait ce qui suit : « with debug_info not stripped ». Cela signifie que notre binaire contient des informations de débogage. Mais nous n'en avons généralement pas besoin, et les supprimer peut réduire la taille du binaire.

```bash
$ go build main1.go
$ du -sh main1
1.9M	main1

$ go build -ldflags="-w -s" main1.go
$ du -sh main1
1.3M	main1

$ file main1 | tr , '\n'
main1: ELF 64-bit LSB executable
 ARM aarch64
 version 1 (SYSV)
 statically linked
 Go BuildID=...
 stripped
```

## Attention : l'astuce LD_PRELOAD

Le programme système Linux ld-linux.so (linker/chargeur dynamique) utilise **LD_PRELOAD** pour charger des bibliothèques partagées spécifiées. En particulier, avant toute autre bibliothèque, le chargeur dynamique chargera d'abord les bibliothèques partagées qui se trouvent dans LD_PRELOAD.

L'astuce LD_PRELOAD est une technique puissante utilisée dans les binaires liés dynamiquement pour surcharger ou intercepter les appels de fonction vers les bibliothèques partagées.

En définissant la variable d'environnement LD_PRELOAD pour qu'elle pointe vers un fichier objet partagé personnalisé, les utilisateurs peuvent injecter leur propre code dans l'exécution d'un programme, remplaçant ou augmentant ainsi les fonctions de bibliothèque existantes.

Cette méthode permet diverses applications, telles que le débogage, les tests et même la modification du comportement d'un programme sans altérer le code source original.

```bash
LD_PRELOAD=/path/to/my/malloc.so /bin/ls
```

Cela montre également que les **binaires liés statiquement** sont plus sûrs, car ils n'ont pas ce problème puisqu'ils ne recherchent aucune bibliothèque externe. De plus, il existe un **« mode d'exécution sécurisé »** – une fonctionnalité de sécurité implémentée par le linker dynamique sur les systèmes Linux pour restreindre certains comportements lors de l'exécution de programmes nécessitant des privilèges élevés.

## Conclusion

Les ordinateurs ne sont pas magiques, il suffit de les comprendre.

Et comprendre les processus de compilation et d'exécution de Go est crucial pour développer des applications cross-plateformes robustes.

Espérons qu'après avoir lu cet article, vous avez maintenant une meilleure compréhension du fonctionnement de la compilation Go.

### Lectures complémentaires

* [Explorez plus d'articles sur packagemain.tech](https://packagemain.tech/)
    
* [Code Source](https://github.com/plutov/packagemain/tree/master/static-dynamic-linking)
    
* [src/cmd/cgo/doc.go](https://cs.opensource.google/go/go/+/refs/tags/go1.19.3:src/cmd/cgo/doc.go)
    
* [cmd/link](https://pkg.go.dev/cmd/link)
    
* [Debugging a weird 'file not found' error](https://jvns.ca/blog/2021/11/17/debugging-a-weird--file-not-found--error/)
    
* [How the heck do we get to main()](http://dbp-consulting.com/tutorials/debugging/linuxProgramStartup.html)
    
* [A General Overview of What Happens Before main()](https://embeddedartistry.com/blog/2019/04/08/a-general-overview-of-what-happens-before-main/)
    
* [Rust Before Main](https://www.youtube.com/watch?v=q8irLfXwaFM)