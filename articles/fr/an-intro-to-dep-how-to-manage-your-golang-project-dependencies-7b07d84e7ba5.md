---
title: 'Une introduction à dep : Comment gérer les dépendances de votre projet Golang'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-02T20:23:34.000Z'
originalURL: https://freecodecamp.org/news/an-intro-to-dep-how-to-manage-your-golang-project-dependencies-7b07d84e7ba5
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nPaOoEou7T-cM9WZGtU-gg.png
tags:
- name: Dep
  slug: dep
- name: glide
  slug: glide
- name: golang
  slug: golang
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: 'Une introduction à dep : Comment gérer les dépendances de votre projet
  Golang'
seo_desc: 'By Ying Kit Yuen

  Update @ 2018–11–26: Technology is not just moving at a breakneck speed but also
  changing rapidly. Within a year, this article is OUTDATED!

  And according to the dep project page:


  dep was the “official experiment.” The Go toolchain, ...'
---

Par Ying Kit Yuen

**Mise à jour @ 20181126 : La technologie ne se déplace pas seulement à une vitesse effrénée, mais elle change également rapidement. En un an, cet article est OBSOLÈTE !**

Et selon la [page du projet dep](https://github.com/golang/dep) :

> _dep était l'« expérience officielle ». La chaîne d'outils Go, à partir de la version 1.11, a (expérimentalement) adopté une approche qui diverge fortement de dep. En conséquence, nous continuons le développement de dep, mais nous orientons principalement le travail vers le développement d'un prototype alternatif pour le comportement de versionnage dans la chaîne d'outils._

Pour plus d'informations sur la nouvelle gestion intégrée de Go, veuillez consulter le Wiki officiel GitHub  [Go 1.11 Modules](https://github.com/golang/go/wiki/Modules).

Merci à [John Arundel @bitfield](https://twitter.com/bitfield) et [Erhan Yakut @yakuter](https://twitter.com/yakuter) pour avoir révélé le problème. ?



**Mise à jour @ 20180203 : [Sam Boyer](https://medium.com/@sdboyer) de l'équipe godep a clarifié certaines informations incorrectes dans cet article. Je m'excuse auprès de [Sam Boyer](https://medium.com/@sdboyer) et des lecteurs pour tout désagrément.** ?



Précédemment, j'ai publié un [article](https://blog.boatswain.io/post/manage-go-dependencies-using-glide/) sur la gestion des dépendances dans [Go](https://golang.org/) en utilisant [Glide.](https://glide.sh/) J'ai reçu un retour selon lequel [Glide](https://glide.sh/) deviendra obsolète. L'équipe [Glide](https://glide.sh/) suggère aux utilisateurs de passer à un autre outil de gestion des dépendances appelé [dep](https://github.com/golang/dep) écrit par l'équipe [Golang](https://github.com/golang).

> La communauté Go dispose désormais du projet dep pour gérer les dépendances. Veuillez envisager d'essayer de migrer de Glide à dep. Glide continuera à être supporté pendant un certain temps, mais il est considéré comme étant dans un état de support plutôt que de développement actif de fonctionnalités.

Il y avait un plan concernant l'intégration de [dep](https://github.com/golang/dep) dans la chaîne d'outils dans la [version Go 1.10](https://tip.golang.org/doc/go1.10), mais il semble [qu'il reste encore du chemin à parcourir](https://www.reddit.com/r/golang/comments/7dd2ty/go_110_release_notes_draft/#thing_t1_dpwyj4i).

**Mise à jour @ 20180203 :**

* [**dep**](https://github.com/golang/dep) **est officiellement sorti.**
* [**dep**](https://github.com/golang/dep) **ne sera pas intégré dans la chaîne d'outils avec la version 1.10. Veuillez consulter la [feuille de route](https://github.com/golang/dep/wiki/Roadmap) pour les dernières informations.**

![Image](https://cdn-media-1.freecodecamp.org/images/1*-jTtAekDfSoJn1uDzeyFVg.jpeg)
_Et je ne suis tout simplement pas assez rapide. ?_

### Créer le projet dans $GOPATH

Le dossier du projet doit être dans _$GOPATH_ afin de résoudre les chemins des packages [Go](https://golang.org/). Créons un nouveau projet dans _$GOPATH/src/gitlab.com/ykyuen/dep-example_ et ajoutons le fichier suivant.

**main.go**

### La méthode dep

#### Gopkg.toml et Gopkg.lock

[dep](https://github.com/golang/dep) lit deux fichiers appelés _Gopkg.toml_ et _Gopkg.lock_. Initialisons ces deux fichiers en utilisant la commande _dep init_.

```
[ykyuen@camus dep-example]$ dep init  Utilisation de master comme contrainte pour la dépendance directe github.com/dustin/go-humanize  Verrouillage de master (bb3d318) pour la dépendance directe github.com/dustin/go-humanize
```

Comme vous pouvez le voir, la commande _dep init_ analyse les codes sources et télécharge tous les packages nécessaires pour le projet dans le dossier _vendor_.

Le fichier _Gopkg.lock_ sert exactement la même fonction que le fichier _glide.lock_. Il verrouille la version des packages **SAUF** que la version doit être maintenue dans le _Gopkg.toml_. En bref, le fichier _Gopkg.lock_ est généré automatiquement et il dépend des instructions _import_ dans la source versionnée contrôlée par _Gopkg.toml_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*4rou4TKFvTSHxo_OSLp4jg.png)

#### Mettre à jour la version d'une dépendance

Modifions le fichier _Gopkg.toml_ et utilisons une version légèrement plus ancienne du package [go-humanize](https://github.com/dustin/go-humanize) au lieu de la dernière branche master.

Ensuite, exécutez _dep ensure_ pour mettre à jour le package à la version souhaitée. Voici le diff du fichier _Gopkg.lock_ mis à jour.

#### Ajouter une nouvelle dépendance

Un nouveau package peut être ajouté en utilisant la commande _dep ensure -add_.

```
[ykyuen@camus dep-example]$ dep ensure -add github.com/leekchan/accountingRécupération des sources...
```

```
"github.com/leekchan/accounting" n'est pas importé par votre projet, et a été temporairement ajouté à Gopkg.lock et vendor/.Si vous exécutez "dep ensure" à nouveau avant de l'importer réellement, il disparaîtra de Gopkg.lock et vendor/.
```

Maintenant, nous avons le nouveau package _accounting_ prêt dans le dossier _vendor_ avec de nouvelles contraintes écrites dans _Gopkg.toml_ et verrouillées dans _Gopkg.lock_. Mettons à jour le fichier _main.go_ comme suit.

**main.go**

Et exécutons-le.

```
[ykyuen@camus dep-example]$ go run main.gohello worldCe fichier fait 83 Mo.Vous êtes mon 193ème meilleur ami.Vous devez $6,582,491.$123,456,789.21$12,345,678.00$25,925,925.67-$25,925,925.67$123,456,789.21
```

### Le problème avec les sous-modules git

Une différence majeure de [dep](https://github.com/golang/dep) par rapport à [Glide](https://glide.sh/) est que les sous-modules des packages sont ignorés. Par exemple, après avoir ajouté le package [go-goracle/goracle](https://github.com/go-goracle/goracle) avec [dep](https://github.com/golang/dep), le sous-module [odpi](https://oracle.github.io/odpi/) à l'intérieur est vide et entraîne une erreur. La raison de l'abandon du sous-module peut être trouvée au lien suivant.

* [Y a-t-il des plans pour ajouter la prise en charge des sous-modules Git ?](https://github.com/golang/dep/issues/1240)

**Mise à jour @ 20180203 :**

**Le paragraphe sur les sous-modules Git est incorrect.**

[**Sam Boyer**](https://github.com/sdboyer) **a écrit :**

> _dep devrait être parfaitement capable de récupérer les sous-modules git dans le cas que vous décrivez. Je viens de reproduire ce que vous décrivez ici localement, et le problème n'est pas les sous-modules  il n'y a pas de code Go dans github.com/go-goracle/goracle/odpi, donc il ne peut pas être importé directement._

> _Vous devez probablement désactiver l'élagage des packages inutilisés dans Gopkg.toml pour ce projet spécifique, sinon dep ensure supprimera automatiquement ce qui semble être un répertoire inutilisé (mais il semble qu'il soit réellement utilisé par cgo)._

**Mise à jour @ 20180304 :**

Il a été constaté que le package [go-goracle/goracle](https://github.com/go-goracle/goracle) ne fonctionne pas avec [dep](https://github.com/golang/dep). Vous pouvez suivre le problème ci-dessous et vérifier la dernière mise à jour de l'équipe [dep](https://github.com/golang/dep).

* [Échec de la récupération du sous-module git d'un package après la commande dep ensure](https://github.com/golang/dep/issues/1633)

### Résumé

* dep est likely to be the official dependency management tool in the Golang community.
* Si vous débutez un nouveau projet Go, dép est un bon outil pour gérer les dépendances. Vous pourriez envisager de migrer de Glide à dép, mais il n'y a pas de mal à continuer à utiliser Glide pour l'instant.
* Si vous utilisez Glide dans un projet hérité, vous pourriez envisager de migrer vers dép, mais ce n'est pas urgent car Glide continuera à être supporté pendant un certain temps.
* En cas d'ajout, les sous-modules git du package peuvent être manquants. Cela peut entraîner des erreurs dans votre code.
* [**dep**](https://github.com/golang/dep) **est officiellement sorti.**
* [**dep**](https://github.com/golang/dep) **fonctionne bien pour récupérer les sous-modules git.**
* Utilisez la bibliothèque standard chaque fois que possible. (Suggéré par [philoserf](https://www.freecodecamp.org/news/an-intro-to-dep-how-to-manage-your-golang-project-dependencies-7b07d84e7ba5/undefined))
* Vous pouvez consulter cet exemple sur [gitlab.com](https://gitlab.com/ykyuen/dep-example).

 Article initialement publié sur [Boatswain Blog](https://blog.boatswain.io/post/manage-go-dependencies-using-dep/).