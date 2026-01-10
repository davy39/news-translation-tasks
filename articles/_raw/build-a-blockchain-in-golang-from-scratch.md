---
title: How to Build a Blockchain from Scratch with Go
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
seo_title: null
seo_desc: 'By Lukas Lukac

  Introduction

  With Web 3.0 and blockchain becoming more mainstream every day, do you know what
  blockchain is? Do you know its technical advantages and use-cases?

  The goal of this tutorial is to introduce blockchain technology from a tec...'
---

By Lukas Lukac

## Introduction

With Web 3.0 and blockchain becoming more mainstream every day, do you know what blockchain is? Do you know its technical advantages and use-cases?

**The goal of this tutorial is to introduce blockchain technology from a technical perspective by building one from scratch.**

Forget everything you've heard about blockchain from social media. Now, you will build a blockchain system from ground zero to really understand the ins and outs of this peer-to-peer, distributed technology. 

Afterwards, make your own mind up about its future and advantages. Spoiler alert: you will fall in love with programming blockchain software.

### How?

You will follow the story of a software developer who is looking to revolutionize his local bar by implementing blockchain technology for its payment system.

Although blockchain has several undeniable use-cases, at the moment, the number one application is payments. This is because banks are still running on an inefficient, 40 year old infrastructure powered by CSV files and FTP.

The story comes with a lot of fun and intriguing facts about the overall blockchain ecosystem and different protocols such as Bitcoin, Ethereum and XRP.

## What will you build, learn, and do in this tutorial?

* You'll setup a Go project on your local machine without any prior GoLang experience
* You'll generate and distribute your first blockchain tokens
* You'll develop a CLI controlled database in Go from scratch
* You'll find out how few rights users posses in their favourite apps
* You'll discover the blockchain's main value proposition
* You'll make your DB immutable using a secure cryptographic hash function

So let's get started and jump into our story.

## ⭐ Meet the protagonist, Andrej.

Andrej is a bar owner by night and a software developer by day in a small Slovakian town called Bardejov.

Andrej is tired of:
- **Programming solid, old fashion PHP/Java/Javascript applications**
- Forgetting how much money his friends and clients owe him for all the unpaid Friday night vodka shots
- Spending time collecting and counting coins, returning change and generally touching COVID-19-exposed bank bills
- Maintaining different plastic chips for table football, darts, billiard and poker

Andrej would love to:
- **Have a perfect auditable history of the bar's activities** and sales to make his bar compliant with tax regulations
- **Transform his bar into an autonomous, payment-efficient, decentralized and safe environment his customers can trust and profit from**

His goal is to write a simple program and keep all the balances of his clients in virtual form.

Andrej shares his thoughts here:

"Every new customer will give me cash, and **I will credit them an equivalent amount of my digital tokens (coins/cryptocurrency).** The tokens will represent a monetary unit within and outside the bar.
 
The users will use the tokens for all bar functionalities from paying for drinks, borrowing and lending them to their friends, and playing table tennis, poker and kicker.
 
Having a bar powered by blockchain tokens will generate tons of value for my customers. Contrary to my competition and other bars on this street, where the customers only spend money and get a hangover in exchange, **my bar customers holding bar's tokens will have shareholders rights.**
 
Similar to owning a large portion of stocks in a company like Apple or Microsoft, the customers holding these bar tokens will be able to decide how the bar will operate by voting and deciding on:
 - drinks prices
 - opening hours
 - new features (TV, Jukebox...)
 - interior and exterior design
 - profits allocation
 - etc.
 
Oh, this will be a programming dream!

I will call the tokens: The Blockchain Bar tokens, **TBB!**"

Now that Andrej has shared his dream, we'll get started.

## Table of Contents

* [Requirements](#heading-requirements)
* [Setup the project](#heading-setup-the-project)
* [01 | The MVP Database](#heading-01-the-mvp-database)
* [02 | Mutating Global DB State](#heading-02-mutating-global-db-state)
* [03 | Monolithic Event vs Transaction](#heading-03-monolithic-event-vs-transaction)
* [04 | Humans Are Greedy](#heading-04-humans-are-greedy)
* [05 | Why We Need Blockchain](#heading-05-why-we-need-blockchain)
* [06 | L'Hash de Immutable](#heading-06-lhash-de-immutable)
* [Next steps](#heading-next-steps)

## Requirements

Let's dive into our tutorial. I recommend 2+ years of programming experience in Java/PHP/Javascript, or another language similar to Go.

If you want to get a good quick intro to go, [here's a free course](https://www.freecodecamp.org/news/go-golang-course/) that'll get you started.

You can also complete the official 17 lectures of [A Tour Of Go](https://tour.golang.org/basics/1) to get familiar with the language syntax and basic concepts (~20 mins).

### Why Go?

Because like blockchain, it's a fantastic technology for your overall programming career. Go is a trendy language and Go devs are better paid than the average Java/PHP/Javascript positions.

Go is optimized for multi-core CPU architecture. You can spawn thousands of light-weight threads (Go-routines) without problems. It's extremely practical for highly parallel and concurrent software such as blockchain networks. 

By writing your software in Go, you achieve nearly C++ level of performance out of the box without killing yourself for that one time you forgot to free up memory.

Go also compiles to binary which makes it very portable.

## Setup the project

This article has a dedicated open-sourced Github repository with full source code so you can compile the code and run the program on your own local machine.

If you get stuck at any chapter or a particular line of code, create a Github Issue in this repository describing your problem and I will help you out ASAP!

↓ Visit the Github repository and follow the installation instructions ↓

%[https://github.com/web3coach/the-blockchain-bar-newsletter-edition/]

## 01 | The MVP Database

✍ `git checkout c1_genesis_json`

Andrej mastered relational SQL databases in the 90s. He knows how to make advanced data models and how to optimize the SQL queries.

It's time for Andrej to catch up with innovation and start building Web 3.0 software.

Luckily, after reading "The Lean Startup" book last week, Andrej feels like he shouldn't over-engineer the solution just yet. Hence, he chooses a simple but effective JSON file for the bar's MVP database.

In the beginning, there was a primitive centralized database.

### ? Summary

**Blockchain is a database.**

### User 1, Andrej

_Monday, March 18._

Andrej generates 1M utility tokens.

In the blockchain world, tokens are units inside the blockchain database. Their real value in dollars or euro fluctuates based on their demand and popularity.

Every blockchain has a **"Genesis"** file. The Genesis file is used to distribute the first tokens to early blockchain participants.

It all starts with a simple, dummy **genesis.json**.

Andrej creates the file `./database/genesis.json` where he defines that The Blockchain Bar's database will have 1M tokens and all of them will belong to Andrej:

```json
{
  "genesis_time": "2019-03-18T00:00:00.000000000Z",
  "chain_id": "the-blockchain-bar-ledger",
  "balances": {
      "andrej": 1000000
  }
}

```

The tokens need to have a real "utility", that is a use case. Users should be able to pay with them from day 1! 

Andrej must comply with law regulators (the SEC). It is illegal to issue unregistered security. On the other hand, utility tokens are fine, so right away he prints and sticks a new pricing white p̶a̶p̶e̶r̶ poster on the bar's door.

Andrej assigns a starting monetary value to his tokens so he can exchange them for euro, dollars, or other fiat currency.

```json
1 TBB token = 1€

| Item                      | Price   |
| ------------------------- | ------- |
| Vodka shot                | 1   TBB |
| Orange juice              | 5   TBB |
| Burger                    | 2   TBB |
| Crystal Head Vodka Bottle | 950 TBB |

```

Andrej also decides **he should be getting 100 tokens per day** for maintaining the database and having such a brilliant disruptive idea.

### ?Fun Facts

> The first genesis Ether (ETH) on Ethereum blockchain was created and distributed to early investors and developers in the same way as Andrej's utility token.

> In 2017, during an ICO (initial coin offerings) boom on the Ethereum blockchain network, project founders wrote and presented whitepapers to investors. A whitepaper is a technical document outlining a complex issue and possible solution, meant to educate and elucidate a particular matter. In the world of blockchains, a white paper serves to outline the specifications of how that particular blockchain will look and behave once it is developed.

> Blockchain projects raised between €10M to €300M per **whitepaper** idea.

> in exchange for money (the ICO "funding"), investor names  would be included in the initial "genesis balances", similar to how Andrej did it. Investors' hopes through an ICO are the genesis coins go up in value and that the teams deliver the outlined blockchain.

> Naturally, not all whitepaper ideas come to fruition. Massive investments lost to unclear or incomplete ideas are why blockchain received negative coverage in the media throughout these ICOs, and why some still considered it a hype. But the underlying blockchain technology is fantastic and useful, as you will learn further in this book. It's just been abused by some bad actors.

### ? Summary

Blockchain is a database.

**The token supply, initial user balances, and global blockchain settings you define in a Genesis file.**

## 02 | Mutating Global DB State

✍ `git checkout c2_db_changes_txt`

### Dead Party

_Monday, March 25._

After a week of work, the bar facilities are ready to accept tokens. Unfortunately, no one shows up, so Andrej orders three shots of vodka for himself and writes the database changes on a piece of paper:

```text
andrej-3;   // 3 shots of vodka
andrej+3;   // technically purchasing from his own bar
andrej+700; // Reward for a week of work (7x100 per day)

```

To avoid recalculating the latest state of each customer's balance, Andrej creates a `./database/state.json` file storing the balances in an aggregated format.

New DB state:

```json
{
  "balances": {
      "andrej": 1000700
  }
}

```

### Bonus for BabaYaga

_Tuesday, March 26._

To bring traffic to his bar, Andrej announces an exclusive 100% bonus for everyone who purchases the TBB tokens in the next 24 hours.

Bing! He gets his first customer called **BabaYaga**. BabaYaga pre-purchases 1000€ worth of tokens, and to celebrate, she immediately spends 1 TBB for a vodka shot. She has a drinking problem.

DB transactions written on a piece of paper:

```text
andrej-2000;   // transfer to BabaYaga
babayaga+2000; // pre-purchase with 100% bonus
babayaga-1;
andrej+1;
andrej+100;    // 1 day of sun coming up

```

New DB state:

```json
{
  "balances": {
      "andrej": 998801,
      "babayaga": 1999
  }
}

```

### ?Fun Facts

> Blockchain ICO (initial coin offerings based on whitepapers) projects often distribute the genesis tokens with different bonuses, depending on how many of them you buy and how early you do it. Teams offer, on average, 10-40% bonuses to early "participants".

> The word "investor" is avoided, so law regulators won't consider the tokens as a security. Projects would reason their main product, blockchain tokens, function as "flying, loyalty points."

> The "participants" later made even 1000% on their investment selling to the public through an exchange several months later.

### ?Summary

Blockchain is a database. 

The token supply, initial user balances, and global blockchain settings you define in a Genesis file. 

**The Genesis balances indicate what was the original blockchain state and are never updated afterwards.**

**The database state changes are called Transactions (TX).**

## 03 | Monolithic Event vs Transaction

✍ `git checkout c3_state_blockchain_component`

Developers used to event-sourcing architecture must have immediately recognized the familiar principles behind transactions. They are correct. 

Blockchain transactions represent a series of events, and the database is a final aggregated, calculated state after replaying all the transactions in a specific sequence.

### Andrej Programming

_Tuesday evening, March 26._

It's a relaxing Tuesday evening for Andrej. Celebrating his first client, he decides to play some [Starcraft](https://www.youtube.com/watch?v=Ff4VIghrTMg&feature=youtu.be&t=516) and clean up his local development machine by removing some old pictures. 

Unfortunately, he prematurely pressed enter when typing a removal command path in terminal `sudo rm -rf /`. Oops.

All his files, including the bar's `genesis.json` and `state.json` are gone.

Andrej, being a senior developer, repeatedly shouted some f* words very loudly for a few seconds, but he didn't panic! 

While he didn't have a backup, he had something better — a piece of paper with all the database transactions. The only thing he needs to do is replay all the transactions one by one, and his database state will get recovered.

Impressed by the advantages of event-based architecture, he decides to extend his MVP database solution. Every bar's activity, such as individual drink purchases, MUST be recorded inside the blockchain database.

Each **customer** will be represented in DB using an **Account** Struct:

```go
type Account string

```

Each **Transaction** (TX - a database change) will have the following four attributes: **from, to, value** and **data**.

The **data** attribute with one possible value (**reward**) captures Andrej's bonus for inventing the blockchain and increases the initial TBB tokens total supply artificially (inflation).

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

The **Genesis DB** will remain a JSON file:

```json
{
  "genesis_time": "2019-03-18T00:00:00.000000000Z",
  "chain_id": "the-blockchain-bar-ledger",
  "balances": {
    "andrej": 1000000
  }
}

```

All the transactions, previously written on a piece of paper, will be stored in a local text-file database called **tx.db**, serialized in JSON format and separated by line-break character:

```json
{"from":"andrej","to":"andrej","value":3,"data":""}
{"from":"andrej","to":"andrej","value":700,"data":"reward"}
{"from":"andrej","to":"babayaga","value":2000,"data":""}
{"from":"andrej","to":"andrej","value":100,"data":"reward"}
{"from":"babayaga","to":"andrej","value":1,"data":""}

```

The most crucial database component encapsulating all the business logic will be **State**:

```go
type State struct {
   Balances   map[Account]uint
   txMempool []Tx

   dbFile *os.File
}

```

The `State` struct will know about all user balances and who transferred TBB tokens to whom, and how many were transferred.

It's constructed by reading the initial user balances from `genesis.json` file:

```go
func NewStateFromDisk() (*State, error) {
   // get current working directory
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

Afterwards, the genesis `State` balances are updated by sequentially replaying all the database events from `tx.db`:

```go
   txDbFilePath := filepath.Join(cwd, "database", "tx.db")
   f, err := os.OpenFile(txDbFilePath, os.O_APPEND|os.O_RDWR, 0600)
   if err != nil {
      return nil, err
   }

   scanner := bufio.NewScanner(f)
   state := &State{balances, make([]Tx, 0), f}

   // Iterate over each the tx.db file's line
   for scanner.Scan() {
      if err := scanner.Err(); err != nil {
         return nil, err
      }

      // Convert JSON encoded TX into an object (struct)
      var tx Tx
      json.Unmarshal(scanner.Bytes(), &tx)

      // Rebuild the state (user balances),
      // as a series of events
      if err := state.apply(tx); err != nil {
         return nil, err
      }
   }

   return state, nil
}

```

The `State` component is responsible for:

* **Adding** new transactions to **Mempool**
* **Validating** transactions against the current State (sufficient sender balance)
* **Changing** the state
* **Persisting** transactions to disk
* **Calculating** accounts balances by replaying all transactions since Genesis in a sequence

**Adding** new transactions to Mempool:

```go
func (s *State) Add(tx Tx) error {
   if err := s.apply(tx); err != nil {
      return err
   }

   s.txMempool = append(s.txMempool, tx)

   return nil
}

```

**Persisting** the transactions to disk:

```go
func (s *State) Persist() error {
   // Make a copy of mempool because the s.txMempool will be modified
   // in the loop below
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

      // Remove the TX written to a file from the mempool
      s.txMempool = s.txMempool[1:]
   }

   return nil
}
```

**Changing, Validating** the state:

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

### Building a Command-Line-Interface (CLI)

_Tuesday evening, March 26._

Andrej wants to have a convenient way to add new transactions to his DB and list the latest balances of his customers. Because Go programs compile to binary, he builds a CLI for his program.

The easiest way to develop CLI based programs in Go is by using the third party `github.com/spf13/cobra` library.

Andrej initializes Go's built-in dependency manager for his project, called `go modules`:

✍ `cd $GOPATH/src/github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition`

✍ `go mod init github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition`

The `Go modules` command will automatically fetch any library you reference within your Go files.

Andrej creates a new directory called: `cmd` with a subdirectory `tbb`:

✍`mkdir -p ./cmd/tbb`

Inside he creates a `main.go` file, serving as the program's CLI entry point:

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

The Go programs are compiled using the `install` cmd:  
  
✍ `go install ./cmd/tbb/...`

```text
go: finding github.com/spf13/cobra v1.0.0
go: downloading github.com/spf13/cobra v1.0.0
go: extracting github.com/spf13/cobra v1.0.0
```

Go will detect missing libraries and automatically fetch them before compiling the program. Depending on your `$GOPATH` the resulting program will be saved in the `$GOPATH/bin` folder.

✍`echo $GOPATH`

```text
/home/web3coach/go
```

✍`which tbb`

```text
/home/web3coach/go/bin/tbb
```

You can run `tbb` from your terminal now, but it will not do anything because the `Run` function inside the `main.go` file is empty.

The first thing Andrej needs is versioning support for his `tbb` CLI program.

Next to the `main.go` file, he creates a `version.go` command:

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

Compiles and runs it:  
✍ `go install ./cmd/tbb/...`  
✍ `tbb version`

`Version: 0.1.0-beta TX Add && Balances List`

Perfect.

Identically to the `version.go` file, he creates a `balances.go` file:

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

The `balances` command will be responsible for loading the latest DB State and printing it to the standard output:

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

Andrej verifies if the cmd works as expected. It should print the exact balances defined in the Genesis file because the `tx.db` file is still empty.

✍ `go install ./cmd/tbb/...`

✍ `tbb balances list`

```
Accounts balances:
__________________
andrej: 1000000

```

Works well! Now he only needs a cmd for recording the bar's activity.

Andrej creates `./cmd/tbb/tx.go` cmd:

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

The `tbb tx add` cmd uses `State.Add(tx)` function for persisting the bar's events into the file system:

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
            
            // defer means, at the end of this function execution,
            // execute the following statement (close DB file with all TXs)
            defer state.Close()
            
            // Add the TX to an in-memory array (pool)
            err = state.Add(tx)
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                os.Exit(1)
            }
            
            // Flush the mempool TXs to disk
            err = state.Persist()
            if err != nil {
                fmt.Fprintln(os.Stderr, err)
                os.Exit(1)
            }

            fmt.Println("TX successfully added to the ledger.")
        },
    }

```

The `tbb tx add` cmd has 3 mandatory flags: `--from`, `--to` and `--value`.

```go
cmd.Flags().String(flagFrom, "", "From what account to send tokens")
cmd.MarkFlagRequired(flagFrom)

cmd.Flags().String(flagTo, "", "To what account to send tokens")
cmd.MarkFlagRequired(flagTo)

cmd.Flags().Uint(flagValue, 0, "How many tokens to send")
cmd.MarkFlagRequired(flagValue)

return cmd

```

The CLI is done!

Andrej migrates all transactions from paper to his new DB:

✍ `tbb tx add --from=andrej --to=andrej --value=3`

✍`tbb tx add --from=andrej --to=andrej --value=700`

✍`tbb tx add --from=babayaga --to=andrej --value=2000`

✍`tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

✍`tbb tx add --from=babayaga --to=andrej --value=1`

Read all TXs from disk and calculate the latest state:

✍ `tbb balances list`

```
Accounts balances:
__________________
andrej: 998801
babayaga: 1999

```

Bar data successfully restored! Phew, what a night!

### About the Cobra CLI library

The good thing about the `Cobra` lib for CLI programming is the additional features it comes with. For example, you can now run: `tbb help` cmd and it will print out all TBB registered sub-commands with instructions on how to use them.

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

### ?Fun Facts

> Accidentally losing customers' data is a standard Saturday in the corporate world these days. Blockchain fixes this by decentralizing the data storage.

> The trick Andrej baked into the program by skipping balance verification for TXs marked as rewards. **Bitcoin and Ethereum work in the same way.** The balance of the Account who **mined a block** increases out of the blue as a subject of total tokens supply inflation affecting the whole chain. The total supply of bitcoins is capped at 21M BTC. You will learn more about "mining" and "blocks" in chapters 7 and 10.

> The components **State** and **Mempool** are not unique to this program. Andrej chose the names and designs to match a simplified [go-Ethereum](https://github.com/ethereum/go-ethereum/blob/7b32d2a47017570c44cd7f8a83612a29656c9857/core/tx_pool.go#L211), model so you have a glance inside the core Ethereum source code.

### ? Summary

Blockchain is a database. 

The token supply, initial user balances, and global blockchain settings are defined in a Genesis file. 

The Genesis balances indicate what the original blockchain state was and are never updated afterwards.

The database state changes are called Transactions (TX). 

**Transactions are old fashion Events representing actions within the system.**

### ⚒ Study Code

Commit: [5d4b0b](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/5d4b0b6a001e616109da732fdaf7094f1e1acf85)

![Image](https://www.freecodecamp.org/news/content/images/2020/05/unlock_blockchain_components_state.png)

Let's talk about greed.

## 04 | Humans Are Greedy

✍ `git checkout c4_caesar_transfer`

### Typical business greediness

_Wednesday, March 27._

BabaYaga invested a bit too much. She forgot her flat rent payment was around the corner, and she doesn't have the money. BabaYaga calls her flat owner, **Caesar.**

**BabaYaga:** Hey Caesar, I am sorry, but I don't have the cash to pay you the rent this month…

**Caesar:** Why not?

**BabaYaga:** The Blockchain Bar ICO offered a massive bonus, and I purchased 2000€ worth of tokens for just 1000€. It was a great deal!

**Caesar:** What the heck are you talking about? What is an ICO? What on earth are tokens? Can you pay me in some other way?

**BabaYaga:** Oh, not again. I can give you 1000 TBB tokens worth 1000€, and you can use them in the bar to pay for your drinks! Let me call the bar owner, Andrej, and make the transfer!

**Caesar:** All right... I will take it.

Andrej performs the transfer, **but decides to charge an extra 50 TBB tokens for his troubles.** He doesn't want to, BUT the bar shareholders who invested in him a few years ago are forcing him to generate profit as soon as possible.

BabaYaga won't notice this relatively small fee most likely anyway, Andrej tells himself. In the end, only he has the DB access.

// Rent payment

✍`tbb tx add --from=babayaga --to=caesar --value=1000`

// hidden fee charge

✍ `tbb tx add --from=babayaga --to=andrej --value=50`

// new reward for another day of maintaining the DB

✍ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

### ?Fun Facts

> The number one blockchain use-case is banking. Many blockchain projects aim to optimize the domestic and international exchange of money across different currency corridors (XRP).

> Other projects focus on freedom and self-sovereign identity (SSI) - a digital movement that recognizes an individual should own and control their identity and money without the intervening administrative authorities or other centralized intermediaries. SSI allows people to interact in the digital world with the same freedom and capacity for trust as they do in the offline world. (Bitcoin / Ethereum)

> Here are few fun facts why blockchain is a perfect fit for replacing your bank's current banking infrastructure.

> The good thing about virtual tokens is their fungibility - i.e., their ability to be traded, with each unit being as usable as the next. Performing a transfer from account to account can be done by simply changing the database state. Cryptocurrencies are tradeable 24/7.

> You can't trade stocks directly. You need to go through a broker who takes part a percentage of the total transaction as a fee (1-3% to 7% average yearly profit).

> An international bank transfer takes between 3-10 business days and can cost as much 5% of the transferred value! If you’re sending $10,000, you may have to pay up to [$500.](https://www.ofx.com/en-au/faqs/how-much-does-it-cost-to-send-money-internationally/) The technology behind for the last 40 years? FTP + CSV files.

> Do you think the stock market is fair? Banks, indexes, and stocks are highly centralized and controlled by governments and private Wall Street groups. Free market? Wall Street controls how much can prices jump/fall in a single day.

> As an example, Wall Street halted the trading of "S&P 500 Index" after a 7% drop to protect their investors and hedge funds from losing money from people selling their stocks during March 2020 after COVID news. Afterward, the FED printed trillions of dollars for themselves to support the stock price. If you are a developer who likes to save money and avoid debt, your savings just lost value overnight by a yet unknown percentage.

> Many countries are going into negative yields, an unexplored territory with unknown consequences. What does this mean? Soon you will have to pay the bank to keep your savings. Inflation at its best. You are being forced to spend your money to support a system you don't control.

### ⚒ Study Code

Commit: [00d6ed](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/00d6ede25b1e54ceb30c0a0314ef99a612db01de)

## 05 | Why We Need Blockchain

✍ `git checkout c5_broken_trust`

### BabaYaga Seeks Justice

_Thursday, March 28._

BabaYaga enters the bar for her birthday.

**BabaYaga:** Hey, Andrej! Today is my birthday! Get me your most expensive bottle!

**Andrej:** Happy birthday! Here you go: Crystal Head Vodka. But you need to purchase one additional TBB token. The bottle costs 950 tokens, and your balance is 949.

**BabaYaga:** What?! My balance is supposed to be 999 TBB!

**Andrej:** The funds transfer to Caesar you requested last week cost you 50 tokens.

**BabaYaga:** This is unacceptable! I would never agree to such a high fee. You can't do this, Andrej. I trusted your system, but you are as unreliable as every other business owner. Things must change!

**Andrej:** All right, look. You are my most loyal customer, and I didn't want to charge you, but my shareholders forced me. 

**Let me re-program my system and make it completely transparent and decentralized.** After all, if everyone were able to interact with the bar without going through me, it would significantly improve the bar's efficiency and balance the level of trust!

* Ordering drinks would take seconds instead of minutes
* The customers who forgot their wallets at home could borrow or lend tokens to each other
* I wouldn't have to worry about losing the clients data (again) as everyone would have a copy of it
* **The database would be immutable, so once everyone would agree on a specific state, no one else can change it or maliciously modify the history.** Immutability would help with yearly tax audits as well!
* If shareholders wanted to introduce new fees or raise the current ones, everyone involved in the blockchain system would notice and have to agree with it. The users and business owners would even have to engage in some decentralized governance system together, based on voting, probably. In case of a disagreement, the users walk away with all their data!

**BabaYaga:** Well, it certainly sounds good, but is this even possible?

**Andrej:** Yes, I think so. With a bit of **hashing, linked lists, immutable data structure, distributed replication, and asymmetric cryptography!**

**BabaYaga:** I have no idea what you have just said but go and do your geeky thing, Andrej!

### ?Fun Facts

> Bitcoin and Ethereum miners also receive rewards every ~15 minutes for running the blockchain servers (nodes) and validating transactions.

> Every 15 minutes, one Bitcoin miner receives 12.5 BTC ($100k at the moment of writing this page) to cover his servers cost + make some profit.

> The Bitcoin network consumes as much electricity as the entire country of Austria. It accounts for 0.29% of the world's annual electricity consumption.

> Annually it consumes 76.84 TWh, producing 36.50 Mt CO2 carbon footprint (New Zealand). [Source.](https://digiconomist.net/bitcoin-energy-consumption)

> Why? You will learn more later (in Chapter 11) where you will program a Bitcoin mining algorithm from scratch!

> PS: Our algorithm will consume a bit less electricity :)

### ? Summary

Closed software with centralized access to private data allows for just a handful of people to have a lot of power. Users don’t have a choice, and shareholders are in business to make money.

**Blockchain developers aim to develop protocols where applications' entrepreneurs and users synergize in a transparent, auditable relationship. Specifications of the blockchain system should be well-defined from the beginning and only change if its users support it.**

Blockchain is a database. The token supply, initial user balances, and global blockchain settings are defined in a Genesis file. The Genesis balances indicate what was the original blockchain state and are never updated afterwards.

The database state changes are called Transactions (TX). Transactions are old fashion Events representing actions within the system.

### ⚒ Study Code

Commit: [642045](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/64204512f2173eb3f3e136e7e2674a2c456d351f)

## 06 | L'Hash de Immutable

✍ `git checkout c6_immutable_hash`

_The technical difficulty starts with this section! The concepts will only get more challenging but at the same time, very exciting. Buckle up :)_

### How to Program an Immutable Database?

_Friday, March 29._

If Andrej wants to figure out how to program an immutable DB, he has to realize why other database systems are mutable by design.

He decides to analyze an all-mighty MySQL DB Table:

```text
| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 998951  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |
```

In MySQL DB, anyone with access and a good enough reason can perform a table update such as:

```mysql
UPDATE user_balance SET balance = balance + 100 WHERE id > 1

```

Updating values across different rows is possible because the table rows are independent, mutable, and the latest state is not apparent. 

What’s the latest DB change? Last column changed? Last row inserted? If so, how can Andrej know what row was deleted recently? If the rows and table state were tightly coupled, dependent, a.k.a, updating row 1 would generate a completely new, different table, Andrej would achieve his immutability.

> How can you tell if any byte in a database has changed?

### Immutability via Hash Functions

Hashing is process of taking a string input of arbitrary length and producing a hash string of fixed length. Any change in input, will result in a new, different hash.

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
	
	// Change balance from 99895 -> 99896
	
	balancesHashDiff := sha256.Sum256([]byte("| 1 | Andrej | 99896 |"))
	fmt.Printf("%x\n", balancesHashDiff)
	// Output: d04279207...ec6d280f6c7b3e2285758030292d5e1
}

```

Try it: [https://play.golang.org/p/FTPUa7IhOCE](https://play.golang.org/p/FTPUa7IhOCE)

Andrej also requires some level of security for his database, so he decides for a **Cryptographic Hash Function** with the following properties:

* it is [deterministic](https://en.wikipedia.org/wiki/Deterministic_algorithm) - the same message always results in the same hash
* it is quick to compute the hash value for any given message
* it is infeasible to generate a message from its hash value except by trying all possible messages
* a small change to a message should change the hash value so extensively that the new hash value appears uncorrelated with the old hash value
* it is [infeasible](https://en.wikipedia.org/wiki/Computational_complexity_theory#Intractability) to find two different messages with the same hash value

![Image](https://www.freecodecamp.org/news/content/images/2020/05/hash_fruit.png)
_Hashing Fruits Example -&gt; img [src](https://twitter.com/cybergibbons/status/1203291585473110016)_

### Implementing the DB Content Hashing

_Saturday Evening, March 30._

Andrej modifies the `Persist()` function to return a new content hash, `Snapshot`, every time a new transaction is persisted.

```go
type Snapshot [32]byte

```

The `Snapshot` is produced by this new `sha256 secure hashing` function:

```go
func (s *State) doSnapshot() error {
   // Re-read the whole file from the first byte
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

The `doSnapshot()` is called by the modified `Persist()` function. When a new transaction is written into the `tx.db` file, the `Persist()` hashes the entire file content and returns its 32 bytes "fingerprint" hash.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/persist_function.png)
_Persist() hashes the entire tx.db file_

From this moment, everyone can 100% confidently and securely refer to any particular database state (set of data) with a specific snapshot hash.

### ⚓Practice time

**1/4** Run the `tbb balances list` cmd and check the balances are matching.

✍ `tbb balances list`

```text
Account balances at 7d4a360f465d...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999251  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |
```

**2/4** Remove the last 2 rows from `./database/tx.db` and check the balances again.

✍ `tbb balances list`

```bash
Account balances at 841770dcd3...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999051  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |

```

**3/4** Reward Andrej for the last 2 days (from 28th to 30th of March):

Reward Transaction 1:

✍ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

```bash
Persisting new TX to disk:
       {"from":"andrej","to":"andrej","value":100,"data":"reward"}
       
New DB Snapshot: ff2470c7043f5a34169b5dd38921ba6825b03b3facb83e426
TX successfully persisted to the ledger.

```

Reward Transaction 2:

✍ `tbb tx add --from=andrej --to=andrej --value=100 --data=reward`

```bash
Persisting new TX to disk:
       {"from":"andrej","to":"andrej","value":100,"data":"reward"}
       
New DB Snapshot: 7d4a360f468b837b662816bcdc52c1869f99327d53ab4a9ca
TX successfully persisted to the ledger.

```

**4/4** Run the `tbb balances list` cmd and ensure the balances and the snapshot hash is the same as at the beginning.

✍ `tbb balances list`

```bash
Account balances at 7d4a360f465d...

| id | name     | balance |
| -- | -------- | ------- |
| 1  | Andrej   | 999251  |
| 2  | BabaYaga | 949     | 
| 3  | Caesar   | 1000    |

```

**Done!**

Because the cryptographic hash function **sha256** produces the same output (given the same inputs (current `tx.db` and 2x `tbb tx add`)), if you follow the exact steps on your own computer, you will generate the exact same database state and hashes!

### ? Summary

Closed software with centralized access to private data puts only a few people to the position of power. Users don’t have a choice, and shareholders are in business to make money.

Blockchain developers aim to develop protocols where applications' entrepreneurs and users synergize in a transparent, auditable relation. Specifications of the blockchain system should be well defined from the beginning and only change if its users support it.

Blockchain is an **immutable** database. The token supply, initial user balances, and global blockchain settings you define in a Genesis file. The Genesis balances indicate what was the original blockchain state and are never updated afterwards.

The database state changes are called Transactions (TX). Transactions are old fashion Events representing actions within the system.

**The database content is hashed by a secure cryptographic hash function. The blockchain participants use the resulted hash to reference a specific database state.**

### ⚒ Study Code

Commit: [b99e51](https://github.com/web3coach/the-blockchain-way-of-programming-newsletter-edition/commit/b99e5191b19bc076b98a3869289e4788d0a4a77b)

## **⭐**Next steps

You finished the first few chapters! Congratulations!

█▒▒▒▒▒▒▒▒▒ 10%

But this was just a quick warm-up. Blockchain is a very challenging and extensive technology, and you would need an entire book explaining how to build the full system and all of its components from scratch - so I wrote one.

You can continue reading in the next free chapter in my newsletter version of "The Blockchain Way of Programming" eBook.

  
**07 | The Blockchain Programming Model**

* Improving Performance of an Immutable DB
* Batch + Hash + Linked List ⇒ Blocks
* Migrating from TX.db to BLOCKS.db

**Learning:** You redesign and refactor your MVP database into a blockchain architecture.

### **Continue in the tutorial: [https://web3.coach#book](https://web3.coach/#book)**

Thanks for reading!

