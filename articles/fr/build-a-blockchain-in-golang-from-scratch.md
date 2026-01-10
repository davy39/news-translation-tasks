---
title: Comment Construire une Blockchain à partir de Zéro avec Go
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-14T06:50:49.000Z'
originalURL: https://freecodecamp.org/news/build-a-blockchain-in-golang-from-scratch
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/blockchain-bar.png
tags:
- name: Blockchain
  slug: blockchain
- name: Go Language
  slug: go
- name: golang
  slug: golang
seo_title: Comment Construire une Blockchain à partir de Zéro avec Go
seo_desc: 'By Lukas Lukac

  Introduction

  With Web 3.0 and blockchain becoming more mainstream every day, do you know what
  blockchain is? Do you know its technical advantages and use-cases?

  The goal of this tutorial is to introduce blockchain technology from a tec...'
---

Par Lukas Lukac

## Introduction

Avec le Web 3.0 et la blockchain devenant de plus en plus populaires chaque jour, savez-vous ce qu'est la blockchain ? Connaissez-vous ses avantages techniques et ses cas d'utilisation ?

**L'objectif de ce tutoriel est d'introduire la technologie blockchain d'un point de vue technique en en construisant une à partir de zéro.**

Oubliez tout ce que vous avez entendu sur la blockchain à travers les réseaux sociaux. Maintenant, vous allez construire un système blockchain à partir de zéro pour vraiment comprendre les tenants et aboutissants de cette technologie pair-à-pair et distribuée.

Ensuite, faites-vous votre propre opinion sur son avenir et ses avantages. Spoiler alert : vous allez tomber amoureux de la programmation de logiciels blockchain.

### Comment ?

Vous allez suivre l'histoire d'un développeur logiciel qui cherche à révolutionner son bar local en implémentant la technologie blockchain pour son système de paiement.

Bien que la blockchain ait plusieurs cas d'utilisation indéniables, à l'heure actuelle, l'application numéro un est les paiements. Cela est dû au fait que les banques fonctionnent encore sur une infrastructure inefficace, vieille de 40 ans, alimentée par des fichiers CSV et FTP.

L'histoire est accompagnée de nombreux faits amusants et intrigants sur l'écosystème blockchain global et différents protocoles tels que Bitcoin, Ethereum et XRP.

## Que allez-vous construire, apprendre et faire dans ce tutoriel ?

* Vous allez configurer un projet Go sur votre machine locale sans aucune expérience préalable en GoLang
* Vous allez générer et distribuer vos premiers jetons blockchain
* Vous allez développer une base de données contrôlée par CLI en Go à partir de zéro
* Vous allez découvrir combien de droits les utilisateurs possèdent dans leurs applications préférées
* Vous allez découvrir la principale proposition de valeur de la blockchain
* Vous allez rendre votre base de données immuable en utilisant une fonction de hachage cryptographique sécurisée

Alors, commençons et plongeons dans notre histoire.

## ⭐ Rencontrez le protagoniste, Andrej.

Andrej est propriétaire de bar la nuit et développeur logiciel le jour dans une petite ville slovaque appelée Bardejov.

Andrej en a assez de :
- **Programmer des applications solides, à l'ancienne en PHP/Java/Javascript**
- Oublier combien d'argent ses amis et clients lui doivent pour tous les shots de vodka non payés du vendredi soir
- Passer du temps à collecter et compter des pièces, rendre la monnaie et généralement toucher des billets de banque exposés au COVID-19
- Maintenir différentes puces en plastique pour le baby-foot, les fléchettes, le billard et le poker

Andrej aimerait :
- **Avoir un historique parfait et auditable des activités** et des ventes du bar pour rendre son bar conforme aux réglementations fiscales
- **Transformer son bar en un environnement autonome, efficace en matière de paiements, décentralisé et sûr auquel ses clients peuvent faire confiance et profiter**

Son objectif est d'écrire un programme simple et de garder toutes les balances de ses clients sous forme virtuelle.

Andrej partage ses pensées ici :

"Chaque nouveau client me donnera de l'argent liquide, et **je lui créditerai un montant équivalent de mes jetons numériques (pièces/cryptomonnaie).** Les jetons représenteront une unité monétaire à l'intérieur et à l'extérieur du bar.

Les utilisateurs utiliseront les jetons pour toutes les fonctionnalités du bar, de l'achat de boissons, à leur prêt et emprunt entre amis, et pour jouer au tennis de table, au poker et au baby-foot.

Avoir un bar alimenté par des jetons blockchain générera des tonnes de valeur pour mes clients. Contrairement à mes concurrents et aux autres bars de cette rue, où les clients ne dépensent que de l'argent et obtiennent une gueule de bois en échange, **mes clients du bar détenant des jetons du bar auront des droits d'actionnaires.**

Similaire à la possession d'une grande partie des actions d'une entreprise comme Apple ou Microsoft, les clients détenant ces jetons de bar pourront décider comment le bar fonctionnera en votant et en décidant sur :
- les prix des boissons
- les heures d'ouverture
- les nouvelles fonctionnalités (TV, Jukebox...)
- la conception intérieure et extérieure
- l'allocation des profits
- etc.

Oh, ce sera un rêve de programmation !

Je vais appeler les jetons : Les jetons du Blockchain Bar, **TBB !**"

Maintenant qu'Andrej a partagé son rêve, nous allons commencer.

## Table des Matières

* [Exigences](#heading-exigences)
* [Configurer le projet](#heading-installation-du-projet)
* [01 | La Base de Données MVP](#heading-01-la-base-de-données-mvp)
* [02 | Mutation de l'État Global de la Base de Données](#heading-02-mutation-de-letat-global-de-la-base-de-données)
* [03 | Événement Monolithique vs Transaction](#heading-03-événement-monolithique-vs-transaction)
* [04 | Les Humains Sont Avides](#heading-04-les-humains-sont-avides)
* [05 | Pourquoi Nous Avons Besoin de la Blockchain](#heading-05-pourquoi-nous-avons-besoin-de-la-blockchain)
* [06 | Le Hash Immuable](#heading-06-le-hash-immuable)
* [Prochaines étapes](#heading-prochaines-étapes)

## Exigences

Plongeons dans notre tutoriel. Je recommande 2+ années d'expérience en programmation en Java/PHP/Javascript, ou dans un autre langage similaire à Go.

Si vous voulez une bonne introduction rapide à Go, [voici un cours gratuit](https://www.freecodecamp.org/news/go-golang-course/) qui vous permettra de commencer.

Vous pouvez également compléter les 17 leçons officielles de [A Tour Of Go](https://tour.golang.org/basics/1) pour vous familiariser avec la syntaxe du langage et les concepts de base (~20 mins).

### Pourquoi Go ?

Parce que comme la blockchain, c'est une technologie fantastique pour votre carrière de programmation en général. Go est un langage tendance et les développeurs Go sont mieux payés que les postes moyens en Java/PHP/Javascript.

Go est optimisé pour l'architecture multi-cœur des CPU. Vous pouvez lancer des milliers de threads légers (Go-routines) sans problème. C'est extrêmement pratique pour les logiciels hautement parallèles et concurrents tels que les réseaux blockchain.

En écrivant votre logiciel en Go, vous atteignez presque le niveau de performance de C++ sans vous tuer pour cette fois où vous avez oublié de libérer la mémoire.

Go compile également en binaire, ce qui le rend très portable.

## Installation du projet

Cet article a un dépôt Github open-source dédié avec le code source complet afin que vous puissiez compiler le code et exécuter le programme sur votre propre machine locale.

Si vous êtes bloqué à un chapitre ou à une ligne de code particulière, créez un Issue Github dans ce dépôt en décrivant votre problème et je vous aiderai dès que possible !

↓ Visitez le dépôt Github et suivez les instructions d'installation ↓

%[https://github.com/web3coach/the-blockchain-bar-newsletter-edition/]

## 01 | La Base de Données MVP

✏️ `git checkout c1_genesis_json`

Andrej a maîtrisé les bases de données relationnelles SQL dans les années 90. Il sait comment créer des modèles de données avancés et comment optimiser les requêtes SQL.

Il est temps pour Andrej de se mettre à jour avec l'innovation et de commencer à construire des logiciels Web 3.0.

Heureusement, après avoir lu le livre "The Lean Startup" la semaine dernière, Andrej a l'impression de ne pas devoir sur-ingénier la solution pour l'instant. Par conséquent, il choisit un fichier JSON simple mais efficace pour la base de données MVP du bar.

Au début, il y avait une base de données centralisée primitive.

### ? Résumé

**La blockchain est une base de données.**

### Utilisateur 1, Andrej

_Lundi, 18 mars._

Andrej génère 1M de jetons utilitaires.

Dans le monde de la blockchain, les jetons sont des unités à l'intérieur de la base de données blockchain. Leur valeur réelle en dollars ou en euros fluctue en fonction de leur demande et de leur popularité.

Chaque blockchain a un fichier **"Genesis"**. Le fichier Genesis est utilisé pour distribuer les premiers jetons aux premiers participants de la blockchain.

Tout commence avec un simple fichier **genesis.json** basique.

Andrej crée le fichier `./database/genesis.json` où il définit que la base de données du Blockchain Bar aura 1M de jetons et que tous appartiendront à Andrej :

```json
{
  "genesis_time": "2019-03-18T00:00:00.000000000Z",
  "chain_id": "the-blockchain-bar-ledger",
  "balances": {
      "andrej": 1000000
  }
}

```

Les jetons doivent avoir une réelle "utilité", c'est-à-dire un cas d'utilisation. Les utilisateurs doivent pouvoir payer avec eux dès le premier jour !

Andrej doit se conformer aux régulateurs légaux (la SEC). Il est illégal d'émettre une sécurité non enregistrée. D'un autre côté, les jetons utilitaires sont acceptables, alors il imprime et colle immédiatement une nouvelle affiche de tarification sur la porte du bar.

Andrej attribue une valeur monétaire initiale à ses jetons afin de pouvoir les échanger contre des euros, des dollars ou d'autres monnaies fiduciaires.

```json
1 jeton TBB = 1€

| Article                      | Prix   |
| ------------------------- | ------- |
| Shot de vodka                | 1   TBB |
| Jus d'orange              | 5   TBB |
| Burger                    | 2   TBB |
| Bouteille de Vodka Crystal Head | 950 TBB |

```

Andrej décide également **qu'il devrait recevoir 100 jetons par jour** pour la maintenance de la base de données et pour avoir eu une idée disruptive aussi brillante.

### ? Faits Amusants

> Le premier genesis Ether (ETH) sur la blockchain Ethereum a été créé et distribué aux premiers investisseurs et développeurs de la même manière que le jeton utilitaire d'Andrej.

> En 2017, lors d'un boom des ICO (offres initiales de pièces basées sur des whitepapers) sur le réseau blockchain Ethereum, les fondateurs de projets rédigeaient et présentaient des whitepapers aux investisseurs. Un whitepaper est un document technique décrivant un problème complexe et une solution possible, destiné à éduquer et à élucider une question particulière. Dans le monde des blockchains, un whitepaper sert à décrire les spécifications de l'apparence et du comportement de cette blockchain particulière une fois développée.

> Les projets blockchain ont levé entre 10M€ et 300M€ par idée de **whitepaper**.

> En échange d'argent (le financement de l'ICO), les noms des investisseurs seraient inclus dans les "balances genesis" initiales, de la même manière qu'Andrej l'a fait. Les espoirs des investisseurs à travers une ICO sont que les pièces genesis prennent de la valeur et que les équipes livrent la blockchain décrite.

> Naturellement, toutes les idées de whitepaper ne se concrétisent pas. Les investissements massifs perdus à cause d'idées floues ou incomplètes sont la raison pour laquelle la blockchain a reçu une couverture médiatique négative lors de ces ICO, et pourquoi certains la considèrent encore comme un battage médiatique. Mais la technologie blockchain sous-jacente est fantastique et utile, comme vous l'apprendrez plus loin dans ce livre. Elle a simplement été abusée par certains mauvais acteurs.

### ? Résumé

La blockchain est une base de données.

**L'offre de jetons, les balances initiales des utilisateurs et les paramètres globaux de la blockchain que vous définissez dans un fichier Genesis.**

## 02 | Mutation de l'État Global de la Base de Données

✏️ `git checkout c2_db_changes_txt`

### Fête Morte

_Lundi, 25 mars._

Après une semaine de travail, les installations du bar sont prêtes à accepter les jetons. Malheureusement, personne ne se présente, alors Andrej commande trois shots de vodka pour lui-même et écrit les changements de la base de données sur un morceau de papier :

```text
andrej-3;   // 3 shots de vodka
andrej+3;   // techniquement achetés dans son propre bar
andrej+700; // Récompense pour une semaine de travail (7x100 par jour)

```

Pour éviter de recalculer le dernier état de la balance de chaque client, Andrej crée un fichier `./database/state.json` stockant les balances dans un format agrégé.

Nouvel état de la base de données :

```json
{
  "balances": {
      "andrej": 1000700
  }
}

```

### Bonus pour BabaYaga

_Mardi, 26 mars._

Pour attirer du monde dans son bar, Andrej annonce un bonus exclusif de 100% pour tous ceux qui achètent des jetons TBB dans les 24 prochaines heures.

Bing ! Il obtient son premier client appelé **BabaYaga**. BabaYaga pré-achète 1000€ de jetons, et pour célébrer, elle dépense immédiatement 1 TBB pour un shot de vodka. Elle a un problème d'alcool.

Transactions de la base de données écrites sur un morceau de papier :

```text
andrej-2000;   // transfert à BabaYaga
babayaga+2000; // pré-achat avec un bonus de 100%
babayaga-1;
andrej+1;
andrej+100;    // 1 jour de soleil qui se lève

```

Nouvel état de la base de données :

```json
{
  "balances": {
      "andrej": 998801,
      "babayaga": 1999
  }
}

```

### ? Faits Amusants

> Les projets blockchain ICO (offres initiales de pièces basées sur des whitepapers) distribuent souvent les jetons genesis avec différents bonus, selon le nombre que vous achetez et la rapidité avec laquelle vous le faites. Les équipes offrent, en moyenne, des bonus de 10-40% aux premiers "participants".

> Le mot "investisseur" est évité, afin que les régulateurs légaux ne considèrent pas les jetons comme une sécurité. Les projets justifieraient que leur produit principal, les jetons blockchain, fonctionne comme des "points de fidélité volants".

> Les "participants" ont ensuite réalisé jusqu'à 1000% de profit sur leur investissement en vendant au public via une bourse plusieurs mois plus tard.

### ? Résumé

La blockchain est une base de données.

L'offre de jetons, les balances initiales des utilisateurs et les paramètres globaux de la blockchain que vous définissez dans un fichier Genesis.

**Les balances Genesis indiquent quel était l'état original de la blockchain et ne sont jamais mises à jour par la suite.**

**Les changements d'état de la base de données sont appelés Transactions (TX).**

## 03 | Événement Monolithique vs Transaction

✏️ `git checkout c3_state_blockchain_component`

Les développeurs habitués à l'architecture event-sourcing doivent avoir immédiatement reconnu les principes familiers derrière les transactions. Ils ont raison.

Les transactions blockchain représentent une série d'événements, et la base de données est un état final agrégé et calculé après avoir rejoué toutes les transactions dans une séquence spécifique.

### Andrej Programme

_Mardi soir, 26 mars._

C'est une soirée de mardi détendue pour Andrej. Pour célébrer son premier client, il décide de jouer à [Starcraft](https://www.youtube.com/watch?v=Ff4VIghrTMg&feature=youtu.be&t=516) et de nettoyer sa machine de développement locale en supprimant quelques vieilles photos.

Malheureusement, il a prématurément appuyé sur entrée en tapant un chemin de commande de suppression dans le terminal `sudo rm -rf /`. Oups.

Tous ses fichiers, y compris le `genesis.json` et le `state.json` du bar, ont disparu.

Andrej, étant un développeur senior, a crié quelques mots en f* très fort pendant quelques secondes, mais il n'a pas paniqué !

Bien qu'il n'ait pas eu de sauvegarde, il avait quelque chose de mieux — un morceau de papier avec toutes les transactions de la base de données. La seule chose qu'il doit faire est de rejouer toutes les transactions une par une, et l'état de sa base de données sera récupéré.

Impressionné par les avantages de l'architecture basée sur les événements, il décide d'étendre sa solution de base de données MVP. Chaque activité du bar, comme les achats individuels de boissons, DOIT être enregistrée à l'intérieur de la base de données blockchain.

Chaque **client** sera représenté dans la base de données à l'aide d'une **Structure de Compte** :

```go
type Account string

```

Chaque **Transaction** (TX - un changement de base de données) aura les quatre attributs suivants : **from, to, value** et **data**.

L'attribut **data** avec une valeur possible (**reward**) capture le bonus d'Andrej pour avoir inventé la blockchain et augmente artificiellement le nombre total de jetons TBB (inflation).

```go
type Tx struct {
   From  Account `json:"from"`
   To    Account `json:"to"`
   Value uint    `json:"value"`
   Data  string  `json:"data"`
}

func (t Tx) IsReward() bool {
   return t.Data == "reward"
}

```

La **Genesis DB** restera un fichier JSON :

```json
{
  "genesis_time": "2019-03-18T00:00:00.000000000Z",
  "chain_id": "the-blockchain-bar-ledger",
  "balances": {
    "andrej": 1000000
  }
}

```

Toutes les transactions, précédemment écrites sur un morceau de papier, seront stockées dans une base de données de fichier texte local appelée **tx.db**, sérialisées au format JSON et séparées par un caractère de saut de ligne :

```json
{"from":"andrej","to":"andrej","value":3,"data":""}
{"from":"andrej","to":"andrej","value":700,"data":"reward"}
{"from":"andrej","to":"babayaga","value":2000,"data":""}
{"from":"andrej","to":"andrej","value":100,"data":"reward"}
{"from":"babayaga","to":"andrej","value":1,"data":""}

```

Le composant de base de données le plus crucial encapsulant toute la logique métier sera **State** :

```go
type State struct {
   Balances   map[Account]uint
   txMempool []Tx

   dbFile *os.File
}

```

La structure `State` connaîtra toutes les balances des utilisateurs et qui a transféré des jetons TBB à qui, et combien ont été transférés.

Elle est construite en lisant les balances initiales des utilisateurs à partir du fichier `genesis.json` :

```go
func NewStateFromDisk() (*State, error) {
   // obtenir le répertoire de travail actuel
   cwd, err := os.Getwd()
   if err != nil {
      return nil, err
   }

   genFilePath := filepath.Join(cwd, "database", "genesis.json")
   gen, err := loadGenesis(genFilePath)
   if err != nil {
      return nil, err
   }

   balances := make(map[Account]uint)
   for account, balance := range gen.Balances {
      balances[account] = balance
   }

```

Ensuite, les balances `State` de la genèse sont mises à jour en rejouant séquentiellement tous les événements de la base de données à partir de `tx.db` :

```go
   txDbFilePath := filepath.Join(cwd, "database", "tx.db")
   f, err := os.OpenFile(txDbFilePath, os.O_APPEND|os.O_RDWR, 0600)
   if err != nil {
      return nil, err
   }

   scanner := bufio.NewScanner(f)
   state := &State{balances, make([]Tx, 0), f}

   // Itérer sur chaque ligne du fichier tx.db
   for scanner.Scan() {
      if err := scanner.Err(); err != nil {
         return nil, err
      }

      // Convertir la TX encodée en JSON en un objet (struct)
      var tx Tx
      json.Unmarshal(scanner.Bytes(), &tx)

      // Reconstruire l'état (balances des utilisateurs),
      // comme une série d'événements
      if err := state.apply(tx); err != nil {
         return nil, err
      }
   }

   return state, nil
}

```

Le composant `State` est responsable de :

* **Ajouter** de nouvelles transactions au **Mempool**
* **Valider** les transactions par rapport à l'état actuel (balance suffisante de l'expéditeur)
* **Changer** l'état
* **Persister** les transactions sur le disque
* **Calculer** les balances des comptes en rejouant toutes les transactions depuis la Genèse dans une séquence

**Ajouter** de nouvelles transactions au Mempool :

```go
func (s *State) Add(tx Tx) error {
   if err := s.apply(tx); err != nil {
      return err
   }

   s.txMempool = append(s.txMempool, tx)

   return nil
}

```

**Persister** les transactions sur le disque :

```go
func (s *State) Persist() error {
   // Faire une copie du mempool car s.txMempool sera modifié
   // dans la boucle ci-dessous
   mempool := make([]Tx, len(s.txMempool))
   copy(mempool, s.txMempool)

   for i := 0; i < len(mempool); i++ {
      txJson, err := json.Marshal(mempool[i])
      if err != nil {
         return err
      }

      if _, err = s.dbFile.Write(append(txJson, '\n')); err != nil {
         return err
      }

      // Supprimer la TX écrite dans un fichier du mempool
      s.txMempool = s.txMempool[1:]
   }

   return nil
}
```

**Changer, Valider** l'état :

```go
func (s *State) apply(tx Tx) error {
   if tx.IsReward() {
      s.Balances[tx.To] += tx.Value
      return nil
   }

   if tx.Value > s.Balances[tx.From] {
      return fmt.Errorf("insufficient balance")
   }

   s.Balances[tx.From] -= tx.Value
   s.Balances[tx.To] += tx.Value

   return nil
}

```

### Construire une Interface en Ligne de Commande (CLI)

_Mardi soir, 26 mars._

Andrej veut avoir un moyen pratique d'ajouter de nouvelles transactions à sa base de données et de lister les dernières balances de ses clients. Comme les programmes Go compilent en binaire, il construit une CLI pour son programme.

Le moyen le plus simple de développer des programmes basés sur CLI en Go est d'utiliser la bibliothèque tierce `github.com/spf13/cobra`.

Andrej initialise le gestionnaire de dépendances intégré de Go pour son projet, appelé `go modules` :

✏️ `cd $GOPATH/src/github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition`

✏️ `go mod init github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition`

La commande `Go modules` récupérera automatiquement toute bibliothèque que vous référencez dans vos fichiers Go.

Andrej crée un nouveau répertoire appelé : `cmd` avec un sous-répertoire `tbb` :

✏️`mkdir -p ./cmd/tbb`

À l'intérieur, il crée un fichier `main.go`, servant de point d'entrée CLI du programme :

```go
package main

import (
    "github.com/spf13/cobra"
    "os"
    "fmt"
)

func main() {
    var tbbCmd = &cobra.Command{
        Use:   "tbb",
        Short: "The Blockchain Bar CLI",
        Run: func(cmd *cobra.Command, args []string) {
        },
    }
    
    err := tbbCmd.Execute()
    if err != nil {
        fmt.Fprintln(os.Stderr, err)
        os.Exit(1)
    }
}

```

Les programmes Go sont compilés en utilisant la commande `install` :

✏️ `go install ./cmd/tbb/...`

```text
go: finding github.com/spf13/cobra v1.0.0
go: downloading github.com/spf13/cobra v1.0.0
go: extracting github.com/spf13/cobra v1.0.0
```

Go détectera les bibliothèques manquantes et les récupérera automatiquement avant de compiler le programme. Selon votre `$GOPATH`, le programme résultant sera enregistré dans le dossier `$GOPATH/bin`.

✏️`echo $GOPATH`

```text
/home/web3coach/go
```

✏️`which tbb`

```text
/home/web3coach/go/bin/tbb
```

Vous pouvez exécuter `tbb` à partir de votre terminal maintenant, mais il ne fera rien car la fonction `Run` à l'intérieur du fichier `main.go` est vide.

La première chose dont Andrej a besoin est la prise en charge de la version pour son programme CLI `tbb`.

À côté du fichier `main.go`, il crée une commande `version.go` :

```go
package main

import (
    "fmt"
    "github.com/spf13/cobra"
)

const Major = "0"
const Minor = "1"
const Fix = "0"
const Verbal = "TX Add && Balances List"

var versionCmd = &cobra.Command{
    Use:   "version",
    Short: "Describes version.",
    Run: func(cmd *cobra.Command, args []string) {
        fmt.Printf("Version: %s.%s.%s-beta %s", Major, Minor, Fix, Verbal)
    },
}

```

Il le compile et l'exécute :
✏️ `go install ./cmd/tbb/...`
✏️ `tbb version`

`Version: 0.1.0-beta TX Add && Balances List`

Parfait.

De manière identique au fichier `version.go`, il crée un fichier `balances.go` :

```go
func balancesCmd() *cobra.Command {
    var balancesCmd = &cobra.Command{
        Use:   "balances",
        Short: "Interact with balances (list...).",
        PreRunE: func(cmd *cobra.Command, args []string) error {
            return incorrectUsageErr()
        },
        Run: func(cmd *cobra.Command, args []string) {
        },
    }

    balancesCmd.AddCommand(balancesListCmd)

    return balancesCmd
}

```

La commande `balances` sera responsable du chargement du dernier état de la base de données et de son impression sur la sortie standard :

```go
var balancesListCmd = &cobra.Command{
    Use:   "list",
    Short: "Lists all balances.",
    Run: func(cmd *cobra.Command, args []string) {
        state, err := database.NewStateFromDisk()
        if err != nil {
            fmt.Fprintln(os.Stderr, err)
            os.Exit(1)
        }
        defer state.Close()

        fmt.Println("Accounts balances:")
        fmt.Println("__________________")
        fmt.Println("")
        for account, balance := range state.Balances {
            fmt.Println(fmt.Sprintf("%s: %d", account, balance))
        }
    },
}

```

Andrej vérifie si la commande fonctionne comme prévu. Elle devrait imprimer les balances exactes définies dans le fichier Genesis car le fichier `tx.db` est encore vide.

✏️ `go install ./cmd/tbb/...`

✏️ `tbb balances list`

```
Accounts balances:
__________________
andrej: 1000000

```

Fonctionne bien ! Maintenant, il ne lui reste plus qu'une commande pour enregistrer l'activité du bar.

Andrej crée la commande `./cmd/tbb/tx.go` :

```go
func txCmd() *cobra.Command {
    var txsCmd = &cobra.Command{
        Use:   "tx",
        Short: "Interact with txs (add...).",
        PreRunE: func(cmd *cobra.Command, args []string) error {
            return incorrectUsageErr()
        },
        Run: func(cmd *cobra.Command, args []string) {
        },
    }

    txsCmd.AddCommand(txAddCmd())

    return txsCmd
}

```

La commande `tbb tx add` utilise la fonction `State.Add(tx)` pour persister les événements du bar dans le système de fichiers :

```go
func txAddCmd() *cobra.Command {
    var cmd = &cobra.Command{
        Use:   "add",
        Short: "Adds new TX to database.",
        Run: func(cmd *cobra.Command, args []string) {
            from, _ := cmd.Flags().GetString(flagFrom)
            to, _ := cmd.Flags().GetString(flagTo)
            value, _ := cmd.Flags().GetUint(flagValue)

            fromAcc := database.NewAccount(from)
            toAcc := database.NewAccount(to)
            
            tx := database.NewTx(fromAcc, toAcc, value, "")

            state, err := database.NewStateFromDisk()
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                os.Exit(1)
            }
            
            // defer signifie, à la fin de l'exécution de cette fonction,
            // exécuter l'instruction suivante (fermer le fichier DB avec toutes les TX)
            defer state.Close()
            
            // Ajouter la TX à un tableau en mémoire (pool)
            err = state.Add(tx)
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                os.Exit(1)
            }
            
            // Vider les TX du mempool vers le disque
            err = state.Persist()
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                os.Exit(1)
            }

            fmt.Println("TX successfully added to the ledger.")
        },
    }

```

La commande `tbb tx add` a 3 drapeaux obligatoires : `--from`, `--to` et `--value`.

```go
cmd.Flags().String(flagFrom, "", "From what account to send tokens")
cmd.MarkFlagRequired(flagFrom)

cmd.Flags().String(flagTo, "", "To what account to send tokens")
cmd.MarkFlagRequired(flagTo)

cmd.Flags().Uint(flagValue, 0, "How many tokens to send")
cmd.MarkFlagRequired(flagValue)

return cmd

```

La CLI est terminée !

Andrej migre toutes les transactions du papier vers sa nouvelle base de données :

✏️ `tbb tx add --from=andrej --to=andrej --value=3`

✏️`tbb tx add --from=andrej --to=andrej --value=700`

✏️`tbb tx add --from=babayaga --to=andrej --value=2000`

✏️`tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

✏️`tbb tx add --from=babayaga --to=andrej --value=1`

Lire toutes les TX depuis le disque et calculer le dernier état :

✏️ `tbb balances list`

```
Accounts balances:
__________________
andrej: 998801
babayaga: 1999

```

Données du bar restaurées avec succès ! Ouf, quelle nuit !

### À propos de la bibliothèque CLI Cobra

Le bon côté de la bibliothèque `Cobra` pour la programmation CLI est les fonctionnalités supplémentaires qu'elle offre. Par exemple, vous pouvez maintenant exécuter la commande `tbb help` et elle imprimera toutes les sous-commandes TBB enregistrées avec des instructions sur la façon de les utiliser.

```bash
 tbb help

The Blockchain Bar CLI

Usage:
  tbb [flags]
  tbb [command]

Available Commands:
  balances    Interact with balances (list...).
  help        Help about any command
  tx          Interact with txs (add...).
  version     Describes version.

Flags:
  -h, --help   help for tbb

Use "tbb [command] --help" for more information about a command.

```

### ? Faits Amusants

> Perdre accidentellement les données des clients est un samedi standard dans le monde de l'entreprise de nos jours. La blockchain résout ce problème en décentralisant le stockage des données.

> L'astuce qu'Andrej a intégrée dans le programme en sautant la vérification de la balance pour les TX marquées comme récompenses. **Bitcoin et Ethereum fonctionnent de la même manière.** La balance du compte qui a **miné un bloc** augmente soudainement en tant que sujet d'inflation de l'offre totale de jetons affectant toute la chaîne. L'offre totale de bitcoins est plafonnée à 21M BTC. Vous en apprendrez plus sur le "minage" et les "blocs" dans les chapitres 7 et 10.

> Les composants **State** et **Mempool** ne sont pas uniques à ce programme. Andrej a choisi les noms et les designs pour correspondre à un modèle simplifié de [go-Ethereum](https://github.com/ethereum/go-ethereum/blob/7b32d2a47017570c44cd7f8a83612a29656c9857/core/tx_pool.go#L211), afin que vous puissiez jeter un coup d'œil au code source principal d'Ethereum.

### ? Résumé

La blockchain est une base de données.

L'offre de jetons, les balances initiales des utilisateurs et les paramètres globaux de la blockchain sont définis dans un fichier Genesis.

Les balances Genesis indiquent quel était l'état original de la blockchain et ne sont jamais mises à jour par la suite.

Les changements d'état de la base de données sont appelés Transactions (TX).

**Les transactions sont des événements à l'ancienne représentant des actions au sein du système.**

### ⚒️ Étudier le Code

Commit: [5d4b0b](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/5d4b0b6a001e616109da732fdaf7094f1e1acf85)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/unlock_blockchain_components_state.png)

Parlons de l'avidité.

## 04 | Les Humains Sont Avides

✏️ `git checkout c4_caesar_transfer`

### L'avidité typique des affaires

_Mercredi, 27 mars._

BabaYaga a investi un peu trop. Elle a oublié que le paiement du loyer de son appartement était imminent, et elle n'a pas l'argent. BabaYaga appelle son propriétaire, **Caesar.**

**BabaYaga:** Hey Caesar, je suis désolée, mais je n'ai pas l'argent pour te payer le loyer ce mois-ci...

**Caesar:** Pourquoi pas ?

**BabaYaga:** L'ICO du Blockchain Bar offrait un bonus massif, et j'ai acheté 2000€ de jetons pour seulement 1000€. C'était une super affaire !

**Caesar:** De quoi tu parles ? Qu'est-ce qu'une ICO ? Qu'est-ce que les jetons ? Peut-on me payer d'une autre manière ?

**BabaYaga:** Oh, pas encore. Je peux te donner 1000 jetons TBB valant 1000€, et tu pourras les utiliser dans le bar pour payer tes boissons ! Laisse-moi appeler le propriétaire du bar, Andrej, et faire le transfert !

**Caesar:** D'accord... Je vais le prendre.

Andrej effectue le transfert, **mais décide de facturer 50 jetons TBB supplémentaires pour ses tracas.** Il ne veut pas, MAIS les actionnaires du bar qui ont investi en lui il y a quelques années le forcent à générer des profits dès que possible.

BabaYaga ne remarquera probablement pas ces frais relativement faibles de toute façon, se dit Andrej. Après tout, seul lui a accès à la base de données.

// Paiement du loyer

✏️`tbb tx add --from=babayaga --to=caesar --value=1000`

// frais cachés

✏️ `tbb tx add --from=babayaga --to=andrej --value=50`

// nouvelle récompense pour une autre journée de maintenance de la base de données

✏️ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

### ? Faits Amusants

> Le principal cas d'utilisation de la blockchain est la banque. De nombreux projets blockchain visent à optimiser l'échange national et international d'argent à travers différents couloirs de devises (XRP).

> D'autres projets se concentrent sur la liberté et l'identité auto-souveraine (SSI) - un mouvement numérique qui reconnaît qu'un individu devrait posséder et contrôler son identité et son argent sans les autorités administratives intermédiaires ou d'autres intermédiaires centralisés. La SSI permet aux gens d'interagir dans le monde numérique avec la même liberté et capacité de confiance que dans le monde hors ligne. (Bitcoin / Ethereum)

> Voici quelques faits amusants sur pourquoi la blockchain est un choix parfait pour remplacer l'infrastructure bancaire actuelle de votre banque.

> Le bon côté des jetons virtuels est leur fongibilité - c'est-à-dire leur capacité à être échangés, chaque unité étant aussi utilisable que la suivante. Effectuer un transfert d'un compte à un autre peut être fait simplement en changeant l'état de la base de données. Les cryptomonnaies sont négociables 24/7.

> Vous ne pouvez pas échanger des actions directement. Vous devez passer par un courtier qui prend une partie du pourcentage de la transaction totale en tant que frais (1-3% à 7% de profit annuel moyen).

> Un virement bancaire international prend entre 3 et 10 jours ouvrables et peut coûter jusqu'à 5% de la valeur transférée ! Si vous envoyez 10 000 $, vous pourriez avoir à payer jusqu'à [500 $](https://www.ofx.com/en-au/faqs/how-much-does-it-cost-to-send-money-internationally/). La technologie derrière cela depuis les 40 dernières années ? FTP + fichiers CSV.

> Pensez-vous que le marché boursier est équitable ? Les banques, les indices et les actions sont fortement centralisés et contrôlés par les gouvernements et les groupes privés de Wall Street. Libre marché ? Wall Street contrôle combien les prix peuvent monter/baisser en une seule journée.

> Par exemple, Wall Street a suspendu la négociation de l'"Indice S&P 500" après une baisse de 7% pour protéger leurs investisseurs et fonds spéculatifs de perdre de l'argent à cause des gens vendant leurs actions en mars 2020 après les nouvelles du COVID. Par la suite, la FED a imprimé des billions de dollars pour eux-mêmes afin de soutenir le prix des actions. Si vous êtes un développeur qui aime économiser de l'argent et éviter les dettes, vos économies viennent de perdre de la valeur du jour au lendemain d'un pourcentage encore inconnu.

> De nombreux pays entrent dans des rendements négatifs, un territoire inexploré avec des conséquences inconnues. Que signifie cela ? Bientôt, vous devrez payer la banque pour garder vos économies. L'inflation à son meilleur. Vous êtes forcé de dépenser votre argent pour soutenir un système que vous ne contrôlez pas.

### ⚒️ Étudier le Code

Commit: [00d6ed](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/00d6ede25b1e54ceb30c0a0314ef99a612db01de)

## 05 | Pourquoi Nous Avons Besoin de la Blockchain

✏️ `git checkout c5_broken_trust`

### BabaYaga Cherche Justice

_Jeudi, 28 mars._

BabaYaga entre dans le bar pour son anniversaire.

**BabaYaga:** Hey, Andrej ! Aujourd'hui c'est mon anniversaire ! Apporte-moi ta bouteille la plus chère !

**Andrej:** Joyeux anniversaire ! La voici : Crystal Head Vodka. Mais tu dois acheter un jeton TBB supplémentaire. La bouteille coûte 950 jetons, et ton solde est de 949.

**BabaYaga:** Quoi ?! Mon solde devrait être de 999 TBB !

**Andrej:** Le transfert de fonds à Caesar que tu as demandé la semaine dernière t'a coûté 50 jetons.

**BabaYaga:** C'est inacceptable ! Je n'aurais jamais accepté des frais aussi élevés. Tu ne peux pas faire ça, Andrej. J'ai fait confiance à ton système, mais tu es aussi peu fiable que tous les autres propriétaires d'entreprise. Les choses doivent changer !

**Andrej:** D'accord, écoute. Tu es ma cliente la plus fidèle, et je ne voulais pas te facturer, mais mes actionnaires m'y ont forcé.

**Laisse-moi reprogrammer mon système et le rendre complètement transparent et décentralisé.** Après tout, si tout le monde pouvait interagir avec le bar sans passer par moi, cela améliorerait considérablement l'efficacité du bar et équilibrerait le niveau de confiance !

* Commander des boissons prendrait des secondes au lieu de minutes
* Les clients qui ont oublié leurs portefeuilles à la maison pourraient emprunter ou prêter des jetons entre eux
* Je n'aurais pas à m'inquiéter de perdre les données des clients (encore) car tout le monde aurait une copie
* **La base de données serait immuable, donc une fois que tout le monde serait d'accord sur un état spécifique, personne d'autre ne pourrait le changer ou modifier malicieusement l'historique.** L'immuabilité aiderait également pour les audits fiscaux annuels !
* Si les actionnaires voulaient introduire de nouveaux frais ou augmenter les frais actuels, tous les participants du système blockchain le remarqueraient et devraient être d'accord avec cela. Les utilisateurs et les propriétaires d'entreprise devraient même s'engager dans un système de gouvernance décentralisé ensemble, basé sur le vote, probablement. En cas de désaccord, les utilisateurs partent avec toutes leurs données !

**BabaYaga:** Eh bien, cela semble certainement bien, mais est-ce même possible ?

**Andrej:** Oui, je pense que oui. Avec un peu de **hachage, listes chaînées, structure de données immuable, réplication distribuée et cryptographie asymétrique !**

**BabaYaga:** Je n'ai aucune idée de ce que tu viens de dire, mais vas-y et fais ta chose de geek, Andrej !

### ? Faits Amusants

> Les mineurs de Bitcoin et Ethereum reçoivent également des récompenses toutes les ~15 minutes pour faire fonctionner les serveurs blockchain (nœuds) et valider les transactions.

> Toutes les 15 minutes, un mineur de Bitcoin reçoit 12,5 BTC (100k$ au moment de la rédaction de cette page) pour couvrir le coût de ses serveurs + faire un peu de profit.

> Le réseau Bitcoin consomme autant d'électricité que l'ensemble du pays de l'Autriche. Il représente 0,29% de la consommation annuelle d'électricité mondiale.

> Annuellement, il consomme 76,84 TWh, produisant une empreinte carbone de 36,50 Mt CO2 (Nouvelle-Zélande). [Source.](https://digiconomist.net/bitcoin-energy-consumption)

> Pourquoi ? Vous en apprendrez plus plus tard (dans le Chapitre 11) où vous programmerez un algorithme de minage Bitcoin à partir de zéro !

> PS : Notre algorithme consommera un peu moins d'électricité :)

### ? Résumé

Les logiciels fermés avec un accès centralisé aux données privées permettent à seulement quelques personnes d'avoir beaucoup de pouvoir. Les utilisateurs n'ont pas le choix, et les actionnaires sont en affaires pour faire de l'argent.

**Les développeurs blockchain visent à développer des protocoles où les entrepreneurs d'applications et les utilisateurs synergisent dans une relation transparente et auditable. Les spécifications du système blockchain doivent être bien définies dès le début et ne changer que si ses utilisateurs le soutiennent.**

La blockchain est une base de données. L'offre de jetons, les balances initiales des utilisateurs et les paramètres globaux de la blockchain sont définis dans un fichier Genesis. Les balances Genesis indiquent quel était l'état original de la blockchain et ne sont jamais mises à jour par la suite.

Les changements d'état de la base de données sont appelés Transactions (TX). Les transactions sont des événements à l'ancienne représentant des actions au sein du système.

### ⚒️ Étudier le Code

Commit: [642045](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/64204512f2173eb3f3e136e7e2674a2c456d351f)

## 06 | Le Hash Immuable

✏️ `git checkout c6_immutable_hash`

_La difficulté technique commence avec cette section ! Les concepts ne feront que devenir plus difficiles mais en même temps, très excitants. Attachez vos ceintures :)_

### Comment Programmer une Base de Données Immuable ?

_Vendredi, 29 mars._

Si Andrej veut comprendre comment programmer une base de données immuable, il doit réaliser pourquoi les autres systèmes de bases de données sont mutables par conception.

Il décide d'analyser une table de base de données MySQL toute-puissante :

```text
| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 998951  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |
```

Dans une base de données MySQL, toute personne ayant accès et une raison suffisante peut effectuer une mise à jour de table telle que :

```mysql
UPDATE user_balance SET balance = balance + 100 WHERE id > 1

```

La mise à jour des valeurs dans différentes lignes est possible car les lignes de la table sont indépendantes, mutables et l'état le plus récent n'est pas apparent. 

Quel est le dernier changement de la base de données ? La dernière colonne modifiée ? La dernière ligne insérée ? Si oui, comment Andrej peut-il savoir quelle ligne a été supprimée récemment ? Si les lignes et l'état de la table étaient étroitement couplés, dépendants, c'est-à-dire, la mise à jour de la ligne 1 générerait une table complètement nouvelle et différente, Andrej atteindrait son immuabilité.

> Comment pouvez-vous dire si un octet dans une base de données a changé ?

### Immuabilité via les Fonctions de Hachage

Le hachage est le processus de prise d'une entrée de chaîne de longueur arbitraire et de production d'une chaîne de hachage de longueur fixe. Tout changement dans l'entrée entraînera un nouveau hachage différent.

```go
package main

import (
	"crypto/sha256"
	"fmt"
)

func main() {
	balancesHash := sha256.Sum256([]byte("| 1 | Andrej | 99895 |"))
	fmt.Printf("%x\n", balancesHash)
	// Output: 6a04bd8e2...f70a3902374f21e089ae7cc3b200751
	
	// Changer le solde de 99895 -> 99896
	
	balancesHashDiff := sha256.Sum256([]byte("| 1 | Andrej | 99896 |"))
	fmt.Printf("%x\n", balancesHashDiff)
	// Output: d04279207...ec6d280f6c7b3e2285758030292d5e1
}

```

Essayez-le : [https://play.golang.org/p/FTPUa7IhOCE](https://play.golang.org/p/FTPUa7IhOCE)

Andrej nécessite également un certain niveau de sécurité pour sa base de données, il opte donc pour une **Fonction de Hachage Cryptographique** avec les propriétés suivantes :

* elle est [déterministe](https://en.wikipedia.org/wiki/Deterministic_algorithm) - le même message donne toujours le même hachage
* elle est rapide à calculer la valeur de hachage pour tout message donné
* il est impossible de générer un message à partir de sa valeur de hachage sauf en essayant tous les messages possibles
* un petit changement dans un message doit changer la valeur de hachage de manière si extensive que la nouvelle valeur de hachage semble non corrélée avec l'ancienne valeur de hachage
* il est [impossible](https://en.wikipedia.org/wiki/Computational_complexity_theory#Intractability) de trouver deux messages différents avec la même valeur de hachage

![Image](https://www.freecodecamp.org/news/content/images/2020/05/hash_fruit.png)
_Exemple de Hachage de Fruits -&gt; img [src](https://twitter.com/cybergibbons/status/1203291585473110016)_

### Implémentation du Hachage du Contenu de la Base de Données

_Samedi Soir, 30 mars._

Andrej modifie la fonction `Persist()` pour retourner un nouveau hachage de contenu, `Snapshot`, chaque fois qu'une nouvelle transaction est persistée.

```go
type Snapshot [32]byte

```

Le `Snapshot` est produit par cette nouvelle fonction de `hachage sécurisé sha256` :

```go
func (s *State) doSnapshot() error {
   // Relire tout le fichier à partir du premier octet
   _, err := s.dbFile.Seek(0, 0)
   if err != nil {
      return err
   }

   txsData, err := ioutil.ReadAll(s.dbFile)
   if err != nil {
      return err
   }
   s.snapshot = sha256.Sum256(txsData)

   return nil
}

```

La fonction `doSnapshot()` est appelée par la fonction `Persist()` modifiée. Lorsqu'une nouvelle transaction est écrite dans le fichier `tx.db`, `Persist()` hache l'intégralité du contenu du fichier et retourne son empreinte numérique de 32 octets.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/persist_function.png)
_Persist() hache l'intégralité du fichier tx.db_

À partir de ce moment, tout le monde peut faire référence à n'importe quel état particulier de la base de données (ensemble de données) avec un hachage de snapshot spécifique, en toute confiance et en toute sécurité.

### ⚒️ Temps de Pratique

**1/4** Exécutez la commande `tbb balances list` et vérifiez que les balances correspondent.

✏️ `tbb balances list`

```text
Account balances at 7d4a360f465d...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999251  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |
```

**2/4** Supprimez les 2 dernières lignes de `./database/tx.db` et vérifiez à nouveau les balances.

✏️ `tbb balances list`

```bash
Account balances at 841770dcd3...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999051  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |

```

**3/4** Récompensez Andrej pour les 2 derniers jours (du 28 au 30 mars) :

Transaction de Récompense 1 :

✏️ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

```bash
Persisting new TX to disk:
       {"from":"andrej","to":"andrej","value":100,"data":"reward"}
       
New DB Snapshot: ff2470c7043f5a34169b5dd38921ba6825b03b3facb83e426
TX successfully persisted to the ledger.

```

Transaction de Récompense 2 :

✏️ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

```bash
Persisting new TX to disk:
       {"from":"andrej","to":"andrej","value":100,"data":"reward"}
       
New DB Snapshot: 7d4a360f468b837b662816bcdc52c1869f99327d53ab4a9ca
TX successfully persisted to the ledger.

```

**4/4** Exécutez la commande `tbb balances list` et assurez-vous que les balances et le hachage du snapshot sont les mêmes qu'au début.

✏️ `tbb balances list`

```bash
Account balances at 7d4a360f465d...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999251  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |

```

**Terminé !**

Parce que la fonction de hachage cryptographique **sha256** produit la même sortie (étant donné les mêmes entrées (fichier `tx.db` actuel et 2x `tbb tx add`)), si vous suivez les étapes exactes sur votre propre ordinateur, vous générerez le même état de base de données et les mêmes hachages !

### ? Résumé

Les logiciels fermés avec un accès centralisé aux données privées ne donnent du pouvoir qu'à quelques personnes. Les utilisateurs n'ont pas le choix, et les actionnaires sont en affaires pour faire de l'argent.

Les développeurs blockchain visent à développer des protocoles où les entrepreneurs d'applications et les utilisateurs synergisent dans une relation transparente et auditable. Les spécifications du système blockchain doivent être bien définies dès le début et ne changer que si ses utilisateurs le soutiennent.

La blockchain est une base de données **immuable**. L'offre de jetons, les balances initiales des utilisateurs et les paramètres globaux de la blockchain que vous définissez dans un fichier Genesis. Les balances Genesis indiquent quel était l'état original de la blockchain et ne sont jamais mises à jour par la suite.

Les changements d'état de la base de données sont appelés Transactions (TX). Les transactions sont des événements à l'ancienne représentant des actions au sein du système.

**Le contenu de la base de données est haché par une fonction de hachage cryptographique sécurisée. Les participants à la blockchain utilisent le hachage résultant pour référencer un état spécifique de la base de données.**

### ⚒️ Étudier le Code

Commit: [b99e51](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/b99e5191b19bc076b98a3869289e4788d0a4a77b)

## **⭐** Prochaines étapes

Vous avez terminé les premiers chapitres ! Félicitations !

█▒▒▒▒▒▒▒▒▒▒ 10%

Mais ce n'était qu'un petit échauffement. La blockchain est une technologie très difficile et extensive, et vous auriez besoin d'un livre entier expliquant comment construire le système complet et tous ses composants à partir de zéro - alors j'en ai écrit un.

Vous pouvez continuer à lire dans le prochain chapitre gratuit de la version newsletter de mon eBook "The Blockchain Way of Programming".

**07 | Le Modèle de Programmation Blockchain**

* Amélioration des Performances d'une Base de Données Immuable
* Batch + Hash + Linked List → Blocks
* Migration de TX.db vers BLOCKS.db

**Apprentissage :** Vous reconcevez et refactorisez votre base de données MVP en une architecture blockchain.

### **Continuer dans le tutoriel : [https://web3.coach#book](https://web3.coach/#book)**

Merci d'avoir lu !