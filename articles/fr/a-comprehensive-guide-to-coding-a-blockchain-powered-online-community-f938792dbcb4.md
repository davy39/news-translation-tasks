---
title: Un guide complet pour coder une communauté en ligne alimentée par la blockchain
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
seo_title: Un guide complet pour coder une communauté en ligne alimentée par la blockchain
seo_desc: 'By Sandeep Panda

  At Hashnode we have been experimenting a lot with blockchain and its use-cases.
  We have been running a developers’ community ourselves, and the idea behind “decentralized
  communities” fascinates me a lot. The fact that everyone owns ...'
---

Par Sandeep Panda

Chez Hashnode, nous avons beaucoup expérimenté avec la blockchain et ses cas d'utilisation. Nous gérons nous-mêmes une communauté de développeurs, et l'idée des "communautés décentralisées" me fascine beaucoup. Le fait que chacun possède les données et contrôle la plateforme peut donner naissance à de nouveaux types d'applications sociales et perturber la manière traditionnelle de construire des communautés en ligne.

Des plateformes comme [Steemit](https://steemit.com) ont prouvé qu'il est possible de construire de telles communautés et de récompenser les utilisateurs pour leurs contributions. Mais comment quelqu'un peut-il reproduire cela et lancer sa propre plateforme sociale décentralisée alimentée par la blockchain ?

Pour répondre à cette question, j'ai relevé le défi de construire une version décentralisée de HackerNews.

Lors du processus, j'ai évalué plusieurs plateformes et j'ai finalement choisi un protocole appelé [Tendermint](https://tendermint.com). En utilisant Tendermint, j'ai construit un prototype appelé "Mint" qui peut servir de modèle pour construire des applications sociales alimentées par la blockchain.

Le code source est sur GitHub. Vous pouvez consulter les liens suivants pour le code et la démonstration :

* [Mint Blockchain](https://github.com/Hashnode/mint)
* [Code du site web (Front-end Blockchain)](https://github.com/Hashnode/Uphack)
* [Démonstration](http://uphack.co)

Alors, qu'est-ce qu'il faut pour construire une communauté sociale alimentée par la blockchain où les données générées par les utilisateurs sont décentralisées ? Si vous cherchez une réponse, vous êtes au bon endroit. Continuez votre lecture.

### Observations préliminaires

Initialement, j'ai pensé à utiliser une plateforme existante pour construire l'application. Les plateformes de contrats intelligents comme **Ethereum**, **NEM**, **NEO**, et ainsi de suite, offrent le stockage d'actifs, mais celles-ci ne sont pas conçues pour stocker de grandes quantités de données.

HyperLedger Fabric est convaincant, mais il est conçu pour être déployé dans des réseaux de blockchain privés. Hashgraph semble intéressant, mais il est expérimental pour le moment.

D'autres solutions potentielles étaient : **Lisk Sidechains**, **Loom Network**, et **BigChainDB**. Les deux premières sont en alpha privé (sur invitation uniquement), tandis que BigChainDB est alimenté par [Tendermint](https://tendermint.com/).

Ainsi, au lieu d'utiliser BigChainDB, j'ai décidé de jouer directement avec Tendermint et de voir ce qui était possible.

### Pourquoi Tendermint

Tendermint est un protocole qui prend en charge la couche de consensus en utilisant l'algorithme BFT tandis que vous vous concentrez simplement sur l'écriture de la logique métier.

La beauté du protocole est que vous êtes littéralement libre de choisir n'importe quel langage de programmation pour construire une interface (Application Blockchain Interface ou simplement ABCI) qui interagit avec la blockchain.

Tendermint gère les aspects les plus complexes d'une blockchain tels que les rounds de production de blocs, la connectivité pair à pair, les commérages sur les nouveaux blocs, la gestion des transactions, et plus encore. Il stocke les transactions sur le disque en utilisant LevelDB et livre également la transaction confirmée à votre serveur ABCI afin que vous puissiez créer un état global à partir de celle-ci.

Cela semble intéressant ? Voyons comment créer une application blockchain qui stocke des données sur la chaîne en utilisant Tendermint.

### Ce dont vous avez besoin

Voici ce dont vous allez avoir besoin :

* Macbook / Serveur Ubuntu
* Golang
* Tendermint
* MongoDB
* Et de la bière… (Les amateurs de café peuvent remplacer cela par du café)

### Configuration de la machine

Tendermint est écrit en [Go](https://golang.org/). Donc, nous devons d'abord installer le langage Go. Visitez [ce lien](https://golang.org/dl/) pour consulter quelques options de téléchargement. Si vous êtes sur Ubuntu, vous pouvez suivre [ce guide](https://medium.com/@patdhlk/how-to-install-go-1-9-1-on-ubuntu-16-04-ee64c073cd79).

Par défaut, Go choisit `$HOME/go` comme votre espace de travail. Si vous souhaitez utiliser un emplacement différent comme espace de travail, vous pouvez définir la variable `GOPATH` dans `~/.profile`. À partir de maintenant, nous ferons référence à cet emplacement sous le nom de `GOPATH`.

Voici à quoi ressemble le fichier `~/.profile` sur ma machine :

```
export GOPATH="$HOME/go" export PATH=~/.yarn/bin:$GOPATH/bin:$PATHexport GOBIN="$GOPATH/bin"
```

N'oubliez pas de définir la variable `GOBIN` comme indiqué ci-dessus. C'est là que les binaires Go seront installés.

**N'oubliez pas d'exécuter source ~/.profile après avoir mis à jour le fichier.**

Maintenant, nous pouvons installer Tendermint. Voici les étapes :

* `cd $GOPATH/src/github.com`
* `mkdir tendermint`
* `cd tendermint`

Et enfin,

```
git clone https://github.com/tendermint/tendermint
```

Cela installera la dernière version de Tendermint. Comme j'ai testé mon code contre `v0.19.7`, vérifions la version spécifique.

```
cd tendermintgit checkout v0.19.7
```

Cela vous placera sur v0.19.7. Pour procéder à l'installation, exécutez les commandes suivantes :

```
make get_tools make get_vendor_depsmake install
```

Félicitations ! Vous avez installé Tendermint avec succès. Si tout a été installé comme prévu, la commande `tendermint version` imprimera la version de Tendermint.

Maintenant, vous devriez installer [MongoDB](https://docs.mongodb.com/manual/installation/).

### Codage de la Blockchain

Si vous souhaitez comprendre comment Tendermint fonctionne, parcourez [ce guide](http://tendermint.readthedocs.io/projects/tools/en/master/introduction.html#intro-to-abci). Vous pourriez également trouver le diagramme suivant utile.

![Image](https://cdn-media-1.freecodecamp.org/images/rJyiZxm-1rAXkSFkV9XY-TtVoqvoS2forja5)
_Source : [Tendermint Docs](http://tendermint.readthedocs.io/projects/tools/en/master/introduction.html" rel="noopener" target="_blank" title=")_

Je vais souligner quelques concepts importants ici :

* Tendermint core gère la partie consensus.
* Vous devez écrire un serveur ABCI qui gère la logique métier, les validations, et ainsi de suite. Bien que vous puissiez écrire cela dans n'importe quel langage, notre langage de choix sera Go.
* Tendermint core interagira avec votre serveur ABCI via des connexions socket.
* Le serveur ABCI possède de nombreuses méthodes (les développeurs JS peuvent les considérer comme des callbacks) qui seront invoquées par Tendermint core sur divers événements.
* Deux méthodes importantes sont : `CheckTx` et `DeliverTx`. La première est appelée pour valider une transaction, tandis que la seconde est appelée lorsque la `Tx` est confirmée.
* `DeliverTx` vous aide à prendre les mesures nécessaires en fonction des transactions confirmées. Dans notre cas, nous l'utiliserons pour créer et mettre à jour notre état global stocké dans MongoDB.
* Tendermint utilise le consensus BFT. Cela signifie que plus de 2/3 des validateurs doivent avoir un consensus afin de valider une transaction. Ainsi, même si 1/3 des validateurs deviennent malveillants, la blockchain fonctionnera toujours.
* Dans un scénario réel (au moins dans un déploiement public), vous ajouterez probablement une sorte de consensus tel que PoS (Proof of State) en plus du consensus BFT. Dans ce cas, nous allons simplement utiliser le consensus BFT simple. Je vous laisse ajouter le PoS.

Je suggère que vous cloniez le serveur ABCI de la blockchain (nom de code [mint](https://github.com/Hashnode/mint)) depuis GitHub. Mais avant de continuer, nous devons installer un outil de gestion des dépendances appelé [dep](https://github.com/golang/dep).

Si vous êtes sur un Mac, vous pouvez simplement exécuter `brew install dep`. Pour Ubuntu, exécutez la commande suivante.

```
curl https://raw.githubusercontent.com/golang/dep/master/install.sh | sh
```

Maintenant, vous pouvez cloner le code source de mint.

```
cd $GOPATH/srcgit clone https://github.com/Hashnode/mintcd mintdep ensurego install mint
```

Super ! Vous avez maintenant installé mint, qui est un serveur ABCI et fonctionne avec Tendermint core.

Maintenant, laissez-moi vous guider à travers toute la configuration et tout le code.

### Point d'entrée

Vous pouvez trouver le code (et le point d'entrée) sur GitHub [ici](https://github.com/Hashnode/mint/blob/master/mint.go).

Le point d'entrée de l'application est `mint.go`. La partie la plus importante du fichier est la section suivante :

```
app = jsonstore.NewJSONStoreApplication(db)srv, err := server.NewServer("tcp://0.0.0.0:46658", "socket", app) if err != nil {  return err }
```

Toute la logique métier, les méthodes, et ainsi de suite sont définies dans le package `jsonstore`. Le code ci-dessus crée simplement un serveur TCP sur le port `46658` qui accepte les connexions socket de Tendermint core.

Maintenant, examinons le package `jsonstore`.

### Logique métier

[Voici](https://github.com/Hashnode/mint/blob/master/jsonstore/jsonstore.go) le dépôt `jsonstore`.

Notre serveur ABCI fait deux choses importantes :

* Valide les transactions entrantes. Si une transaction est invalide, il retourne un code d'erreur et la transaction est rejetée.
* Une fois qu'une transaction est validée (confirmée par > 2/3 des validateurs) et stockée dans LevelDB, le serveur ABCI met à jour son état global stocké dans MongoDB.

Nous allons utiliser [mgo](https://labix.org/mgo) pour interagir avec MongoDB. Ainsi, `jsonstore.go` définit 5 modèles qui correspondent à 5 collections MongoDB différentes.

Le code ressemble à ce qui suit :

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

Nous définissons également quelques fonctions utilitaires telles que les suivantes :

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

Celles-ci seront utilisées ultérieurement dans le code.

#### À l'intérieur de CheckTx

Maintenant, passons à la partie validation. Comment acceptons-nous ou rejetons-nous une transaction ? Supposons que quelqu'un essaie de s'inscrire, mais ne choisit pas un nom d'utilisateur valide. Comment notre application peut-elle valider cela ?

Cela se fait via la fonction `CheckTx`. La signature ressemble à ce qui suit :

```
func (app *JSONStoreApplication) CheckTx(tx []byte) types.ResponseCheckTx {
```

```
 // ... Logique de validation}
```

Lorsque un nœud Tendermint reçoit une transaction, il invoque `CheckTx` du serveur ABCI et passe les données `tx` comme argument de tableau d'octets. Si `CheckTx` retourne un code non nul, la transaction est rejetée.

Dans notre cas, les clients envoient des objets JSON encodés en Base64 sous forme de chaîne au nœud Tendermint via une requête RPC. Donc, c'est à nous de décoder la tx et de désérialiser la chaîne en un objet JSON.

Cela se fait comme suit :

```
var temp interface{}err := json.Unmarshal(tx, &temp)if err != nil {  panic(err)}message := temp.(map[string]interface{})
```

L'objet `message` ressemble généralement à ce qui suit :

```
{  body: {... Corps du message},  publicKey: <Clé publique de l'expéditeur>,  signature: <le corps du message est signé avec la clé privée>}
```

Tout d'abord, nous devons nous assurer que la personne **dite** a effectivement soumis la transaction à la blockchain, et non quelqu'un d'autre prétendant être cette personne.

La meilleure façon de valider est de demander aux clients de signer le corps du message avec la clé privée de l'utilisateur et de joindre à la fois la clé publique et la signature à la charge utile. Nous utiliserons l'algorithme `ed25519` pour générer les clés et signer le message dans le navigateur et frapper le point de terminaison RPC. Dans la fonction `CheckTx`, nous utiliserons à nouveau `ed25519` et vérifierons le message à l'aide de la clé publique de l'utilisateur.

Cela se fait comme suit :

```
pubKeyBytes, err := base64.StdEncoding.DecodeString(message["publicKey"].(string))
```

```
sigBytes, err := hex.DecodeString(message["signature"].(string))
```

```
messageBytes := []byte(message["body"].(string))isCorrect := ed25519.Verify(pubKeyBytes, messageBytes, sigBytes)if isCorrect != true {  return types.ResponseCheckTx{Code: code.CodeTypeBadSignature}}
```

Dans l'exemple ci-dessus, nous utilisons le package `ed25519` pour valider le message. Divers codes tels que `code.CodeTypeBadSignature` sont définis dans le package `code`. Ce sont simplement des entiers. Rappelez-vous simplement que si vous souhaitez rejeter une transaction, vous devez retourner un code non nul. Dans notre cas, si nous détectons que la signature du message n'est pas valide, nous retournons `CodeTypeBadSignature` qui est `4`.

La section suivante de `CheckTx` traite des diverses validations de données, telles que :

* Si l'utilisateur envoie une transaction autre que "createUser (Inscription)", nous vérifions d'abord que la clé publique de l'utilisateur est présente dans notre base de données.
* Si l'utilisateur essaie de créer un post ou un commentaire, il doit avoir des données valides telles qu'un `titre`, un `contenu` non vides, et ainsi de suite.
* Si l'utilisateur essaie de s'inscrire, le nom d'utilisateur doit avoir des caractères acceptables.

Le code ressemble à ce qui suit :

```
// ==== L'utilisateur existe-t-il vraiment ? ======if body["type"] != "createUser" { publicKey := strings.ToUpper(byteToHex(pubKeyBytes))
```

```
 count, _ := db.C("users").Find(bson.M{"publicKey": publicKey}).Count()
```

```
 if count == 0 {  return types.ResponseCheckTx{Code: code.CodeTypeBadData} }}// ==== L'utilisateur existe-t-il vraiment ? ======
```

```
codeType := code.CodeTypeOK
```

```
// ===== Validation des données =======switch body["type"] {case "createPost": entity := body["entity"].(map[string]interface{})
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
// ===== Validation des données =======return types.ResponseCheckTx{Code: codeType}
```

Le code est vraiment simple et assez explicite. Donc, je ne vais pas entrer dans les détails et je vous laisse le lire et l'explorer davantage.

#### À l'intérieur de DeliverTx

Une fois qu'une transaction est confirmée et appliquée à la blockchain, Tendermint core appelle `DeliverTx` et passe la transaction sous forme de tableau d'octets. La signature de la fonction ressemble à ce qui suit :

```
func (app *JSONStoreApplication) DeliverTx(tx []byte) types.ResponseDeliverTx {  // ... Le code va ici}
```

Nous allons utiliser cette fonction pour construire un état global basé sur MongoDB. Nous faisons cela afin que les utilisateurs de notre site web puissent lire les données facilement.

Cette fonction est grande et comporte plusieurs cas. Dans cette section, je ne couvrirai qu'un seul cas qui est la "Création de Post". Comme le reste du code est similaire, je vous laisse creuser plus profondément et explorer le code complet.

Tout d'abord, nous allons désérialiser les données `tx` en un objet JSON :

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

Pour la création de post, l'objet message ressemble à ce qui suit :

```
{body: {  type: "createPost",  entity: {    id: id,    title: title,    url: url,    text: text,    author: author  }},signature: signature,publicKey: publicKey}
```

Et voici comment la fonction `DeliverTx` crée une nouvelle entrée dans la base de données lorsqu'une transaction "createPost" est validée :

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
// Calculer le score hotpost.Score = hotScore(post.Upvotes, post.Date)
```

```
// Lors de la relecture de la transaction, vérifier si elle a été marquée comme spam
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

Le bloc de code réel contient une instruction switch qui gère chaque type de transaction différemment. N'hésitez pas à consulter le code et à jouer avec. Si quelque chose n'est pas clair, n'hésitez pas à écrire vos questions dans les commentaires ci-dessous.

Maintenant que nous avons examiné deux aspects importants du serveur ABCI, essayons d'exécuter à la fois Tendermint core et notre serveur et voyons comment envoyer des transactions.

Pour exécuter l'application, exécutez les commandes suivantes à partir de deux terminaux différents.

Tout d'abord, exécutez :

```
mint
```

Si la commande réussit, vous verrez la sortie suivante dans le terminal :

![Image](https://cdn-media-1.freecodecamp.org/images/ai-JWS7ryQg6Ks0tavletYx274e-0i6830jS)
_Sortie de Mint_

Assurez-vous que MongoDB est déjà en cours d'exécution avant de démarrer `mint`. Si votre terminal ne reconnaît pas la commande `mint`, assurez-vous d'exécuter `source ~/.profile`.

Ensuite, démarrez Tendermint dans un terminal différent :

```
tendermint node --consensus.create_empty_blocks=false
```

Par défaut, Tendermint produit de nouveaux blocs toutes les 3 secondes, même s'il n'y a pas de transactions.

Pour éviter cela, nous utilisons le drapeau :

```
consensus.create_empty_blocks=false
```

Maintenant que Tendermint est en cours d'exécution, vous pouvez commencer à envoyer des transactions. Vous avez besoin d'un client qui peut générer des clés `ed25519`, signer vos requêtes et frapper le point de terminaison RPC exposé par Tendermint.

Une requête exemple (Node.js) ressemble à ceci :

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

Notez que le point de terminaison RPC est exposé sur le port `46657`.

Former et signer les requêtes manuellement peut être fastidieux. Donc, je suggère que vous utilisiez [Uphack](https://github.com/Hashnode/Uphack) (un site web de style HackerNews qui interagit avec la blockchain) pour avoir une vue d'ensemble.

Pour installer Uphack, suivez les étapes ci-dessous :

```
git clone https://github.com/Hashnode/Uphackcd Uphackyarngulp less // assurez-vous que gulp est installé globalementnode server.js
```

Vous pouvez accéder au site web sur `http://localhost:3000`. Voici à quoi il ressemble sur ma machine :

![Image](https://cdn-media-1.freecodecamp.org/images/r4KTf9O7sjlqQah6IgOJ5aNWRDME0mNlpR81)
_Uphack_

Comme vous n'avez pas encore de données, il sera vide au début. N'hésitez pas à vous inscrire et à soumettre quelques posts pour visualiser le processus.

Pendant que vous utilisez l'application, ouvrez l'onglet réseau de votre navigateur et consultez la section XHR. L'URL `/rpc` accepte les données base64 et fait une requête au serveur RPC de Tendermint côté serveur. Vous pouvez copier les données base64 et les coller dans un [décodeur base64](https://www.base64decode.org/) pour voir les données réelles qui sont envoyées.

![Image](https://cdn-media-1.freecodecamp.org/images/SAZpTI3shyASXIL89fVB4dvPP0ucvsNLI1FP)

Entrer dans les détails de Uphack est hors du cadre de ce tutoriel. Cependant, comme mentionné ci-dessus, le code pour Uphack (le client) est open source et la logique est simple. Si vous parcourez le [code source](https://github.com/Hashnode/Uphack) et examinez divers points de terminaison, vous développerez une meilleure compréhension de l'ensemble du processus.

### Conclusion

Pour résumer, nous avons construit une **blockchain** qui stocke des données JSON sur la chaîne et accepte des transactions sous forme de base64. Pour démontrer l'utilisation, nous avons également brièvement examiné Uphack, **un site web de style HackerNews** qui interagit avec la blockchain.

Cependant, voici quelques points dont vous devez être conscient :

* Vous avez construit un réseau à nœud unique. Cela signifie que vous êtes le seul validateur. Si vous êtes intéressé par un déploiement multi-nœuds, consultez la [documentation de mint](https://github.com/Hashnode/mint). Nous avons déployé un réseau à 4 nœuds jusqu'à présent, et si vous souhaitez devenir un validateur et jouer avec la blockchain, n'hésitez pas à me contacter.
* Cet arrangement utilise le consensus BFT. Dans un scénario réel, vous aurez besoin d'un algorithme de consensus comme Proof of Stake, Delegated Proof of Stake, et ainsi de suite.
* Le point de terminaison RPC de la blockchain écoute sur `46657` et le serveur ABCI fonctionne sur `46658`. À tout moment, vous pouvez vérifier l'état de la blockchain en visitant `localhost:46657/status`.
* Pour l'instant, il n'y a aucune incitation à devenir un validateur et à produire des blocs. Dans un cadre (D)PoS, les producteurs de blocs devraient être récompensés avec un jeton chaque fois qu'ils proposent un bloc. C'est laissé comme exercice pour vous.
* Le serveur ABCI peut être écrit dans n'importe quel langage. Par exemple, consultez [js-abci](https://github.com/tendermint/js-abci/).

Pour conclure, je tiens à préciser que je ne suis pas un expert en blockchain. Je suis un apprenant et je partage simplement les choses que je trouve intéressantes. Stocker des données sur la chaîne me fascine et je crois que les **communautés sociales décentralisées** sont l'un des principaux cas d'utilisation de la blockchain.

Si vous repérez des inexactitudes dans le code ou l'article, n'hésitez pas à les signaler. J'apprécierais que vous utilisiez [mint](https://github.com/Hashnode/mint) et [Uphack](https://github.com/Hashnode/Uphack) et que vous donniez votre avis. Les PR sont toujours les bienvenus !

Faites-moi savoir ce que vous en pensez dans les commentaires ci-dessous !