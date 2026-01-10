---
title: A comprehensive guide to coding a blockchain-powered online community
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-05T20:08:25.000Z'
originalURL: https://freecodecamp.org/news/a-comprehensive-guide-to-coding-a-blockchain-powered-online-community-f938792dbcb4
coverImage: https://cdn-media-1.freecodecamp.org/images/1*1h7x469AFYKuUveSj7ZlOA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: decentralization
  slug: decentralization
- name: golang
  slug: golang
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: null
seo_desc: 'By Sandeep Panda

  At Hashnode we have been experimenting a lot with blockchain and its use-cases.
  We have been running a developers’ community ourselves, and the idea behind “decentralized
  communities” fascinates me a lot. The fact that everyone owns ...'
---

By Sandeep Panda

At Hashnode we have been experimenting a lot with blockchain and its use-cases. We have been running a developers’ community ourselves, and the idea behind “decentralized communities” fascinates me a lot. The fact that everyone owns the data and controls the platform can give rise to new types of social apps and disrupt the traditional way of building online communities.

Platforms like [Steemit](https://steemit.com) have proven that it’s possible to build such communities and reward users for their contributions. But how should someone go about replicating it and launching their own decentralized social platform powered by blockchain?

To answer the question, I took up the challenge of building a decentralized version of HackerNews.

During the process, I evaluated multiple platforms and finally zeroed in on a protocol called [Tendermint](https://tendermint.com). Using Tendermint, I have built a prototype called “Mint” which can serve as a boilerplate for building blockchain-powered social apps.

The codebase is on GitHub. You can check out the following links for code and demo:

* [Mint Blockchain](https://github.com/Hashnode/mint)
* [Website Code (Blockchain Front-end)](https://github.com/Hashnode/Uphack)
* [Demo](http://uphack.co)

So what does it take to build a blockchain-powered social community where the user-generated data is decentralized? If you are looking for an answer, you have come to the right place. Read on.

### Preliminary Observations

Initially, I thought of utilizing an existing platform to build the app. Smart Contract platforms like **Ethereum**, **NEM**, **NEO**, and so on offer storage of assets, but these are not designed to store large amount of data.

HyperLedger Fabric is compelling, but it’s designed to be deployed in private blockchain networks. Hashgraph sounds interesting, but it’s experimental as of now.

Other potential solutions were: **Lisk Sidechains**, **Loom Network,** and **BigChainDB**. The first two are in private alpha (invite-only), while BigChainDB is powered by [Tendermint](https://tendermint.com/).

So, instead of using BigChainDB, I decided to play around with Tendermint directly and see what was possible.

### Why Tendermint

Tendermint is a protocol that takes care of the consensus layer using BFT algorithm while you just focus on writing the business logic.

The beauty of the protocol is that you are literally free to choose any programming language to build an interface (Application Blockchain Interface or simply ABCI) that interacts with the blockchain.

Tendermint handles the most complex aspects of a blockchain such as block production rounds, peer to peer connectivity, gossiping about new blocks, transaction handling, and more. It stores the transactions on the disk using LevelDB and also delivers the confirmed transaction to your ABCI server so that you can create a global state out of it.

Sounds interesting? Let’s see how to create a blockchain app that stores data on chain using Tendermint.

### What’s Needed?

Here is what you are going to need:

* Macbook / Ubuntu server
* Golang
* Tendermint
* MongoDB
* And beer… (Coffee lovers can replace this with coffee)

### Setting up the Machine

Tendermint is written in [Go](https://golang.org/). So, we need to install the Go language first. Visit [this link](https://golang.org/dl/) to check out a few download options. If you are on Ubuntu, you can follow [this guide](https://medium.com/@patdhlk/how-to-install-go-1-9-1-on-ubuntu-16-04-ee64c073cd79).

By default, Go chooses `$HOME/go` as your workspace. If you want to use a different location as your workspace, you can set `GOPATH` variable in `~/.profile` . From now on, we’ll refer to this location as `GOPATH`.

Here is how `~/.profile` file looks on my machine:

```
export GOPATH="$HOME/go" export PATH=~/.yarn/bin:$GOPATH/bin:$PATHexport GOBIN="$GOPATH/bin"
```

Remember to set `GOBIN` variable as shown above. This is where the Go binaries will be installed.

**Don’t forget to run source ~/.profile after updating the file.**

Now we can install Tendermint. Here are the steps:

* `cd $GOPATH/src/github.com`
* `mkdir tendermint`
* `cd tendermint`

And finally,

```
git clone https://github.com/tendermint/tendermint
```

This will install the latest version of Tendermint. As I have tested my code against `v0.19.7`, let’s check out the specific release.

```
cd tendermintgit checkout v0.19.7
```

This will put you on v0.19.7. To proceed with the installation, run the following commands:

```
make get_tools make get_vendor_depsmake install
```

Congrats! You have installed Tendermint successfully. If everything was installed as intended, the command `tendermint version` will print out the Tendermint version.

Now, you should go ahead and install [MongoDB](https://docs.mongodb.com/manual/installation/).

### Coding the Blockchain

If you want to understand how Tendermint works, go through [this guide](http://tendermint.readthedocs.io/projects/tools/en/master/introduction.html#intro-to-abci). You may also find the following diagram helpful.

![Image](https://cdn-media-1.freecodecamp.org/images/rJyiZxm-1rAXkSFkV9XY-TtVoqvoS2forja5)
_Source: [Tendermint Docs](http://tendermint.readthedocs.io/projects/tools/en/master/introduction.html" rel="noopener" target="_blank" title=")_

I’ll outline a few important concepts here:

* Tendermint core handles the consensus part.
* You need to write an ABCI server that handles the business logic, validations, and so on. Although you can write this in any language, our language of choice will be Go.
* Tendermint core will interact with your ABCI server via socket connections.
* The ABCI server has many methods (JS developers can think of them as callbacks) that will be invoked by Tendermint core on various events.
* Two important methods are: `CheckTx` and `DeliverTx`. The first one is called to validate a transaction, while the latter is called when the `Tx` is confirmed.
* `DeliverTx` helps you take necessary actions based on the confirmed transactions. In our case, we’ll use this to create and update our global state stored in MongoDB.
* Tendermint uses BFT consensus. This means more than 2/3 of the validators need to have consensus in order to commit a transaction. So, even if 1/3 of the validators go rogue, the blockchain will still work.
* In a real world scenario (at least in a public deployment), you will most likely add some sort of consensus such as PoS (Proof of State) in addition to BFT consensus. In this case, we’ll just go ahead with simple BFT consensus. I’ll leave adding PoS up to you.

I suggest that you clone the blockchain ABCI server (code-named [mint](https://github.com/Hashnode/mint)) from GitHub. But before we go ahead, we need to install a dependency management tool called [dep](https://github.com/golang/dep).

If you are on a Mac, you can just run `brew install dep` . For Ubuntu, run the following command.

```
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
```

Now you can clone the codebase of mint.

```
cd $GOPATH/srcgit clone https://github.com/Hashnode/mintcd mintdep ensurego install mint
```

Sweet! You have now installed mint, which is an ABCI server and works along with Tendermint core.

Now, let me walk you through the whole set-up and all the code.

### Entry Point

You can find the code (and entry point) on GitHub [here](https://github.com/Hashnode/mint/blob/master/mint.go).

The entry point of the app is `mint.go` . The most important part of the file is the following section:

```
app = jsonstore.NewJSONStoreApplication(db)srv, err := server.NewServer("tcp://0.0.0.0:46658", "socket", app) if err != nil {  return err }
```

All the business logic, methods, and so on are defined in the package `jsonstore` . The above code simply creates a TCP server on port `46658` that accepts socket connections from Tendermint core.

Now let’s look at `jsonstore`package.

### Business Logic

[Here’s](https://github.com/Hashnode/mint/blob/master/jsonstore/jsonstore.go) the `jsonstore` repo.

Our ABCI server does two important things:

* Validates incoming transactions. If a transaction is invalid, it returns an error code and the transaction is rejected.
* Once a transaction is committed (confirmed by > 2/3 of the validators) and stored in LevelDB, the ABCI server updates its global state stored in MongoDB.

We’re going to use [mgo](https://labix.org/mgo) for interacting with MongoDB. So, `jsonstore.go` defines 5 models that correspond to 5 different MongoDB collections.

The code looks like the following:

```
// Post ...type Post struct {    ID          bson.ObjectId `bson:"_id" json:"_id"`    Title       string        `bson:"title" json:"title"`    URL         string        `bson:"url" json:"url"`    Text        string        `bson:"text" json:"text"`    Author      bson.ObjectId `bson:"author" json:"author"`    Upvotes     int           `bson:"upvotes" json:"upvotes"`    Date        time.Time     `bson:"date" json:"date"`    Score       float64       `bson:"score" json:"score"`    NumComments int           `bson:"numComments" json:"numComments"`    AskUH       bool          `bson:"askUH" json:"askUH"`    ShowUH      bool          `bson:"showUH" json:"showUH"`    Spam        bool          `bson:"spam" json:"spam"`}
```

```
// Comment ...type Comment struct {    ID              bson.ObjectId `bson:"_id" json:"_id"`    Content         string        `bson:"content" json:"content"`    Author          bson.ObjectId `bson:"author" json:"author"`    Upvotes         int           `bson:"upvotes" json:"upvotes"`    Score           float64       `bson:"score" json:"score"`    Date            time.Time    PostID          bson.ObjectId `bson:"postID" json:"postID"`    ParentCommentID bson.ObjectId `bson:"parentCommentId,omitempty" json:"parentCommentId"`}
```

```
// User ...type User struct {    ID        bson.ObjectId `bson:"_id" json:"_id"`    Name      string        `bson:"name" json:"name"`    Username  string        `bson:"username" json:"username"`    PublicKey string        `bson:"publicKey" json:"publicKey"`}
```

```
// UserPostVote ...type UserPostVote struct {    ID     bson.ObjectId `bson:"_id" json:"_id"`    UserID bson.ObjectId `bson:"userID" json:"userID"`    PostID bson.ObjectId `bson:"postID" json:"postID"`}
```

```
// UserCommentVote ...type UserCommentVote struct {    ID        bson.ObjectId `bson:"_id" json:"_id"`    UserID    bson.ObjectId `bson:"userID" json:"userID"`    CommentID bson.ObjectId `bson:"commentID" json:"commentID"`}
```

We also define a few utility functions such as the following:

```
func byteToHex(input []byte) string {    var hexValue string    for _, v := range input {        hexValue += fmt.Sprintf("%02x", v)    }    return hexValue}
```

```
func findTotalDocuments(db *mgo.Database) int64 {    collections := [5]string{"posts", "comments", "users", "userpostvotes", "usercommentvotes"}    var sum int64
```

```
for _, collection := range collections {        count, _ := db.C(collection).Find(nil).Count()        sum += int64(count)    }
```

```
return sum}
```

```
func hotScore(votes int, date time.Time) float64 {    gravity := 1.8    hoursAge := float64(date.Unix() * 3600)    return float64(votes-1) / math.Pow(hoursAge+2, gravity)}
```

```
// FindTimeFromObjectID ... Convert ObjectID string to Timefunc FindTimeFromObjectID(id string) time.Time {    ts, _ := strconv.ParseInt(id[0:8], 16, 64)    return time.Unix(ts, 0)}
```

These will be used subsequently in the code.

#### Inside CheckTx

Now let’s come to the validation part. How do we accept or reject a transaction? Let’s say someone is trying to sign up, but doesn’t choose a valid username. How can our app validate this?

It’s done via `CheckTx` function. The signature looks like the following:

```
func (app *JSONStoreApplication) CheckTx(tx []byte) types.ResponseCheckTx {
```

```
 // ... Validation logic}
```

When a Tendermint node receives a transaction, it invokes`CheckTx` of ABCI server and passes `tx` data as a `byte` array argument. If `CheckTx` returns a non-zero code, the transaction is rejected.

In our case, clients send Base64 encoded stringified JSON objects to the Tendermint node via an RPC request. So, it is our job to decode the tx and unmarshall the string into a JSON object.

It’s done like this:

```
var temp interface{}err := json.Unmarshal(tx, &temp)if err != nil {  panic(err)}message := temp.(map[string]interface{})
```

`message` object typically looks like the following:

```
{  body: {... Message body},  publicKey: <Public Key of Sender>,  signature: <message.body is signed with the Private Key>}
```

First, we need to make sure that **said** **person** has indeed submitted the transaction to the blockchain, not someone else claiming to be that person.

The best way to validate is to ask clients to sign the message body with the user’s private key and attach both the public key and the signature to the payload. We’ll use `ed25519` algorithm to generate the keys and sign the message in the browser and hit the RPC endpoint. In the `CheckTx` function we’ll again use `ed25519` and verify the message with the help of the user’s public key.

It’s done like this:

```
pubKeyBytes, err := base64.StdEncoding.DecodeString(message["publicKey"].(string))
```

```
sigBytes, err := hex.DecodeString(message["signature"].(string))
```

```
messageBytes := []byte(message["body"].(string))isCorrect := ed25519.Verify(pubKeyBytes, messageBytes, sigBytes)if isCorrect != true {  return types.ResponseCheckTx{Code: code.CodeTypeBadSignature}}
```

In the above example, we use the `ed25519` package to validate the message. Various codes such as `code.CodeTypeBadSignature` are defined inside `code` package. These are just integers. Just remember that if you want to reject a transaction, you have to return a non-zero code. In our case, if we detect that the message signature is not valid, we return `CodeTypeBadSignature` which is `4`.

The next section of `CheckTx` deals with various data validations, such as:

* If the user is sending any transaction other than “createUser (Sign up)”, we first check that the user’s public key is present in our database.
* If the user is trying to create a post or comment, it should have valid data such as non-empty `title` , `content` , and so on.
* If the user is trying to sign up, the username should have acceptable characters.

The code looks like the following:

```
// ==== Does the user really exist? ======if body["type"] != "createUser" { publicKey := strings.ToUpper(byteToHex(pubKeyBytes))
```

```
 count, _ := db.C("users").Find(bson.M{"publicKey": publicKey}).Count()
```

```
 if count == 0 {  return types.ResponseCheckTx{Code: code.CodeTypeBadData} }}// ==== Does the user really exist? ======
```

```
codeType := code.CodeTypeOK
```

```
// ===== Data Validation =======switch body["type"] {case "createPost": entity := body["entity"].(map[string]interface{})
```

```
  if (entity["id"] == nil) || (bson.IsObjectIdHex(entity["id"]. (string)) != true) {  codeType = code.CodeTypeBadData  break }
```

```
if entity["title"] == nil || strings.TrimSpace(entity["title"].(string)) == "" {  codeType = code.CodeTypeBadData  break }
```

```
if (entity["url"] != nil) && (strings.TrimSpace(entity["url"].(string)) != "") {  _, err := url.ParseRequestURI(entity["url"].(string))  if err != nil {   codeType = code.CodeTypeBadData   break  } }case "createUser": entity := body["entity"].(map[string]interface{})
```

```
if (entity["id"] == nil) || (bson.IsObjectIdHex(entity["id"].(string)) != true) {  codeType = code.CodeTypeBadData  break }
```

```
r, _ := regexp.Compile("^[A-Za-z_0-9]+$")
```

```
if (entity["username"] == nil) || (strings.TrimSpace(entity["username"].(string)) == "") || (r.MatchString(entity["username"].(string)) != true) {  codeType = code.CodeTypeBadData  break }
```

```
if (entity["name"] == nil) || (strings.TrimSpace(entity["name"].(string)) == "") {  codeType = code.CodeTypeBadData  break }case "createComment": entity := body["entity"].(map[string]interface{})
```

```
if (entity["id"] == nil) || (bson.IsObjectIdHex(entity["id"].(string)) != true) {  codeType = code.CodeTypeBadData  break }
```

```
if (entity["postId"] == nil) || (bson.IsObjectIdHex(entity["postId"].(string)) != true) {  codeType = code.CodeTypeBadData  break }
```

```
if (entity["content"] == nil) || (strings.TrimSpace(entity["content"].(string)) == "") {  codeType = code.CodeTypeBadData  break }}
```

```
// ===== Data Validation =======return types.ResponseCheckTx{Code: codeType}
```

The code is really simple and pretty self-explanatory. So, I won’t go into the details, and will leave it up to you to read and explore further.

#### Inside DeliverTx

Once a transaction is confirmed and applied to the blockchain, Tendermint core calls `DeliverTx` and passes the transaction as a byte array. The function signature looks like the following:

```
func (app *JSONStoreApplication) DeliverTx(tx []byte) types.ResponseDeliverTx {  // ... Code goes here}
```

We’ll use this function to construct a MongoDB-based global state. We do this so that our website users can read the data easily.

This function is big and has multiple cases. In this section I’ll just cover only one case which is “Post Creation”. As the rest of the code is similar, I’ll leave it up to you to dig deeper and explore the full code.

Firstly, we’ll go ahead and unmarshall the `tx`data into a JSON object:

```
var temp interface{}err := json.Unmarshal(tx, &temp)
```

```
if err != nil { panic(err)}
```

```
message := temp.(map[string]interface{})
```

```
var bodyTemp interface{}
```

```
errBody := json.Unmarshal([]byte(message["body"].(string)), &bodyTemp)
```

```
if errBody != nil { panic(errBody)}
```

```
body := bodyTemp.(map[string]interface{})
```

For post creation, the message object looks like the following:

```
{body: {  type: "createPost",  entity: {    id: id,    title: title,    url: url,    text: text,    author: author  }},signature: signature,publicKey: publicKey}
```

And here is how `DeliverTx` function creates a new entry in the database when a “createPost” transaction is committed:

```
entity := body["entity"].(map[string]interface{})
```

```
var post Postpost.ID = bson.ObjectIdHex(entity["id"].(string))post.Title = entity["title"].(string)
```

```
if entity["url"] != nil { post.URL = entity["url"].(string)}if entity["text"] != nil { post.Text = entity["text"].(string)}
```

```
if strings.Index(post.Title, "Show UH:") == 0 { post.ShowUH = true} else if strings.Index(post.Title, "Ask UH:") == 0 { post.AskUH = true}
```

```
pubKeyBytes, errDecode := base64.StdEncoding.DecodeString(message["publicKey"].(string))
```

```
if errDecode != nil { panic(errDecode)}
```

```
publicKey := strings.ToUpper(byteToHex(pubKeyBytes))
```

```
var user Usererr := db.C("users").Find(bson.M{"publicKey": publicKey}).One(&user)if err != nil { panic(err)}post.Author = user.ID
```

```
post.Date = FindTimeFromObjectID(post.ID.Hex())
```

```
post.Upvotes = 1
```

```
post.NumComments = 0
```

```
// Calculate hot rankpost.Score = hotScore(post.Upvotes, post.Date)
```

```
// While replaying the transaction, check if it has been marked as spam
```

```
spamCount, _ := db.C("spams").Find(bson.M{"postID": post.ID}).Count()
```

```
if spamCount > 0 { post.Spam = true}
```

```
dbErr := db.C("posts").Insert(post)
```

```
if dbErr != nil { panic(dbErr)}
```

```
var document UserPostVotedocument.ID = bson.NewObjectId()document.UserID = user.IDdocument.PostID = post.ID
```

```
db.C("userpostvotes").Insert(document)
```

The actual code block has a switch statement that handles each type of transaction differently. Feel free to check out the code and play around. If something is unclear, feel free to write your queries in the comments below.

Now that we’ve examined two important aspects of the ABCI server, let’s try to run both Tendermint core and our server and see how to send transactions.

In order to run the app, run the following commands from two different terminals.

First, run:

```
mint
```

If the command succeeds, you will see the following output in the terminal:

![Image](https://cdn-media-1.freecodecamp.org/images/ai-JWS7ryQg6Ks0tavletYx274e-0i6830jS)
_Mint Output_

Make sure MongoDB is already running before starting `mint`. If your terminal is unable to recognize `mint` command, be sure to run `source ~/.profile` .

Then start Tendermint in a different terminal:

```
tendermint node --consensus.create_empty_blocks=false
```

By default, Tendermint produces new blocks every 3 seconds, even if there are no transactions.

To prevent that we use the flag:

```
consensus.create_empty_blocks=false
```

Now that Tendermint is running you can start sending the transactions to it. You need a client that can generate `ed25519` keys, sign your requests, and hit the RPC endpoint exposed by Tendermint.

An example request (Node.js) looks like this:

```
const base64Data = req.body.base64Data;
```

```
let headers = {    'Content-Type': 'text/plain',    'Accept':'application/json-rpc'}
```

```
let options = {    url: "http://localhost:46657",    method: 'POST',    headers: headers,    json: true,    body: {"jsonrpc":"2.0","method":"broadcast_tx_commit","params": { "tx" : base64Data } ,"id":"something"}}
```

```
request(options, function (error, response, body) {    res.json({ body: response.body });});
```

Note that the RPC endpoint is exposed on port `46657` .

Forming and signing the requests manually can be tedious. So, I suggest that you use [Uphack](https://github.com/Hashnode/Uphack) (a HackerNews style website that interacts with the blockchain) to get the full picture.

To install Uphack, follow the steps below:

```
git clone https://github.com/Hashnode/Uphackcd Uphackyarngulp less // make sure gulp is installed globallynode server.js
```

You can access the website on `http://localhost:3000` . It looks like this on my machine:

![Image](https://cdn-media-1.freecodecamp.org/images/r4KTf9O7sjlqQah6IgOJ5aNWRDME0mNlpR81)
_Uphack_

As you don’t have any data yet, it will look empty initially. Feel free to register an account and submit some posts to visualize the process.

While you are using the app, open up the network tab of your browser and check out the XHR section. The `/rpc` URL accepts the base64 data and makes request to Tendermint’s RPC endpoint server-side. You can copy the base64 data and paste it into a [base64 decoder](https://www.base64decode.org/) to see the actual data that’s being sent.

![Image](https://cdn-media-1.freecodecamp.org/images/SAZpTI3shyASXIL89fVB4dvPP0ucvsNLI1FP)

Going into the details of Uphack is out of the scope of this tutorial. However, as mentioned above, the code for Uphack (the client) is open source and the logic is straightforward. If you go through the [codebase](https://github.com/Hashnode/Uphack) and examine various endpoints, you will develop a better understanding of the whole process.

### Wrapping up

To summarize, we built a **blockchain** that stores JSON data on chain and accepts transactions in the form of base64. To demonstrate the usage, we also briefly examined Uphack, **a HackerNews style website** that interacts with the blockchain.

However, here are a few things you should be aware of:

* You have built a single node network. This means you are the only validator. If you are interested in multi-node deployment, check out [mint’s](https://github.com/Hashnode/mint) documentation. We have deployed a 4-node network so far, and if you wish to become a validator and play around with the blockchain, feel free to reach out to me.
* This arrangement uses BFT consensus. In a real world scenario you will need some consensus algorithm like Proof of Stake, Delegated Proof of Stake, and so on.
* The blockchain RPC endpoint listens on `46657` and the ABCI server runs on `46658` . At any time you can check the blockchain status by visiting `localhost:46657/status` .
* Right now there is no incentive for becoming a validator and producing blocks. In a (D)PoS setting, the block producers should be rewarded with some token every time they propose a block. It’s left as an exercise to you.
* The ABCI server can be written in any language. For example, check [js-abci](https://github.com/tendermint/js-abci/).

To conclude, I would like to make it clear that I am not a blockchain expert. I am a learner and I am just sharing things I find interesting. Storing data on chain fascinates me and I believe **decentralized social communities** are one of the prime use-cases of blockchain.

If you spot any inaccuracies anywhere in the codebase or article, feel free to point it out. I’ll appreciate if you use [mint](https://github.com/Hashnode/mint) & [Uphack](https://github.com/Hashnode/Uphack) and provide your feedback. PRs are always welcome!

Let me know what you think in the comments below!

