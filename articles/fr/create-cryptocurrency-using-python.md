---
title: Comment créer votre propre cryptomonnaie en utilisant Python
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-08T22:16:05.000Z'
originalURL: https://freecodecamp.org/news/create-cryptocurrency-using-python
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/blockchain-3448502_1920-2.jpg
tags:
- name: Cryptocurrency
  slug: cryptocurrency
- name: Python
  slug: python
seo_title: Comment créer votre propre cryptomonnaie en utilisant Python
seo_desc: 'By Alfrick Opidi


  With the current rise of cryptocurrencies, blockchain is creating a buzz in the
  technology world. This technology has attracted so much attention mainly because
  of its ability to guarantee security, enforce decentralization, and qui...'
---

Par Alfrick Opidi

> Avec l'essor actuel des cryptomonnaies, la blockchain crée un buzz dans le monde de la technologie. Cette technologie attire autant d'attention principalement en raison de sa capacité à garantir la sécurité, à renforcer la décentralisation et à accélérer les processus dans plusieurs industries, en particulier dans le secteur financier.

Essentiellement, une blockchain est une base de données publique qui documente et authentifie de manière irréversible la possession et la transmission d'actifs numériques. Les monnaies numériques, comme Bitcoin et Ethereum, sont basées sur ce concept. La blockchain est une technologie passionnante que vous pouvez utiliser pour transformer les capacités de vos applications.

Récemment, nous avons vu des gouvernements, des organisations et des individus utiliser la technologie blockchain pour créer leurs propres cryptomonnaies et éviter de rester à la traîne. Notamment, lorsque Facebook a proposé sa propre cryptomonnaie, appelée [Libra](https://libra.org/en-US/white-paper/#introduction), l'annonce a suscité de nombreuses réactions à travers le monde.

Et si vous pouviez suivre le mouvement et créer votre propre version de cryptomonnaie ?

J'ai réfléchi à cela et décidé de développer un algorithme qui crée une crypto.

J'ai décidé d'appeler la cryptomonnaie **fccCoin**.

Dans ce tutoriel, je vais illustrer le processus étape par étape que j'ai utilisé pour construire la monnaie numérique (j'ai utilisé les concepts orientés objet du langage de programmation [Python](https://www.freecodecamp.org/news/best-python-tutorial/) ).

Voici le plan de base de l'algorithme de blockchain pour créer le **fccCoin** :

```python
class Block:

    def __init__():

    # première classe de bloc

        pass
    
    def calculate_hash():
    
    # calcule le hachage cryptographique de chaque bloc
        
    
class BlockChain:
    
    def __init__(self):
     # méthode de constructeur
    pass
    
    def construct_genesis(self):
        # construit le bloc initial
        pass

    def construct_block(self, proof_no, prev_hash):
        # construit un nouveau bloc et l'ajoute à la chaîne
        pass

    @staticmethod
    def check_validity():
        # vérifie si la blockchain est valide
        pass

    def new_data(self, sender, recipient, quantity):
        # ajoute une nouvelle transaction aux données des transactions
        pass

    @staticmethod
    def construct_proof_of_work(prev_proof):
        # protège la blockchain contre les attaques
        pass
   
    @property
    def last_block(self):
        # retourne le dernier bloc de la chaîne
        return self.chain[-1]


```

Maintenant, laissez-moi expliquer ce qui se passe...

## 1. Construction de la première classe Block

Une blockchain est composée de plusieurs blocs qui sont joints les uns aux autres (cela semble familier, n'est-ce pas ?).

L'enchaînement des blocs se fait de telle sorte que si un bloc est falsifié, le reste de la chaîne devient invalide.

En appliquant le concept ci-dessus, j'ai créé la classe de bloc initiale suivante :

```python
import hashlib
import time

class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash, self.data,
                                              self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.data,
                                               self.timestamp)

```

Comme vous pouvez le voir dans le code ci-dessus, j'ai défini la fonction **__init__()**, qui sera exécutée lorsque la classe **Block** est initiée, comme dans toute autre classe Python.

J'ai fourni les paramètres suivants à la fonction d'initiation :

* **self**—cela fait référence à l'instance de la classe **Block**, ce qui permet d'accéder aux méthodes et attributs associés à la classe ;
* **index**—cela suit la position du bloc dans la blockchain ;
* **proof_no**—c'est le nombre produit lors de la création d'un nouveau bloc (appelé minage) ;
* **prev_hash**—cela fait référence au hachage du bloc précédent dans la chaîne ;
* **data**—cela donne un enregistrement de toutes les transactions effectuées, comme la quantité achetée ;
* **timestamp**—cela place un horodatage pour les transactions.

La deuxième méthode de la classe, **calculate_hash**, générera le hachage des blocs en utilisant les valeurs ci-dessus. Le module SHA-256 est importé dans le projet pour aider à obtenir les hachages des blocs.

Après que les valeurs ont été entrées dans l'algorithme de hachage cryptographique, la fonction retournera une chaîne de 256 bits représentant le contenu du bloc.

C'est ainsi que la sécurité est assurée dans les blockchains—chaque bloc aura un hachage et ce hachage dépendra du hachage du bloc précédent.

Ainsi, si quelqu'un essaie de compromettre un bloc dans la chaîne, les autres blocs auront des hachages invalides, entraînant la perturbation de l'ensemble du réseau blockchain.

En fin de compte, un bloc ressemblera à ceci :

```python
{
    "index": 2,
    "proof": 21,
    "prev_hash": "6e27587e8a27d6fe376d4fd9b4edc96c8890346579e5cbf558252b24a8257823",
    "transactions": [
        {'sender': '0', 'recipient': 'Quincy Larson', 'quantity': 1}
    ],
    "timestamp": 1521646442.4096143
}

```

## 2. Construction de la classe Blockchain

L'idée principale d'une blockchain, comme son nom l'indique, implique l'enchaînement de plusieurs blocs les uns aux autres.

Par conséquent, je vais construire une classe **Blockchain** qui sera utile pour gérer le fonctionnement de toute la chaîne. C'est là que la plupart de l'action va se dérouler.

La classe **Blockchain** aura diverses méthodes auxiliaires pour accomplir diverses tâches dans la blockchain.

Laissez-moi expliquer le rôle de chacune des méthodes de la classe.

### a. Méthode de constructeur

Cette méthode garantit que la blockchain est instanciée.

```python
class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

```

Voici les rôles de ses attributs :

* **self.chain**—cette variable conserve tous les blocs ;
* **self.current_data**—cette variable conserve toutes les transactions complétées dans le bloc ;
* **self.construct_genesis()**—cette méthode prendra en charge la construction du bloc initial.

### b. Construction du bloc genesis

La blockchain nécessite une méthode _**construct_genesis**_ pour construire le bloc initial de la chaîne. Dans la convention blockchain, ce bloc est spécial car il symbolise le début de la blockchain.

Dans ce cas, construisons-le simplement en passant quelques valeurs par défaut à la méthode _**construct_block**_.

J'ai donné à la fois _**proof_no**_ et _**prev_hash**_ une valeur de zéro, bien que vous puissiez fournir n'importe quelle valeur que vous voulez.

```python
def construct_genesis(self):
    self.construct_block(proof_no=0, prev_hash=0)


def construct_block(self, proof_no, prev_hash):
    block = Block(
        index=len(self.chain),
        proof_no=proof_no,
        prev_hash=prev_hash,
        data=self.current_data)
    self.current_data = []

    self.chain.append(block)
    return block

```

### c. Construction de nouveaux blocs

La méthode **_construct_block_** est utilisée pour créer de nouveaux blocs dans la blockchain.

Voici ce qui se passe avec les différents attributs de cette méthode :

* **index**—cela représente la longueur de la blockchain ;
* **proof_nor & prev_hash**—la méthode appelante les passe ;
* **data**—cela contient un enregistrement de toutes les transactions qui ne sont pas incluses dans un bloc sur le nœud ;
* **self.current_data**—cela est utilisé pour réinitialiser la liste des transactions sur le nœud. Si un bloc a été construit et les transactions qui lui sont allouées, la liste est réinitialisée pour s'assurer que les transactions futures sont ajoutées à cette liste. Et ce processus se déroulera en continu ;
* **self.chain.append()**—cette méthode joint les blocs nouvellement construits à la chaîne ;
* **return**—enfin, un objet bloc construit est retourné.

### d. Vérification de la validité

La méthode _**check_validity**_ est importante pour évaluer l'intégrité de la blockchain et s'assurer qu'il n'y a pas d'anomalies.

Comme mentionné précédemment, les hachages sont essentiels pour la sécurité de la blockchain, car même le moindre changement dans l'objet entraînera la génération d'un hachage complètement nouveau.

Par conséquent, cette méthode **_check_validity_** utilise des instructions _**if**_ pour vérifier si le hachage de chaque bloc est correct.

Elle vérifie également si chaque bloc pointe vers le bon bloc précédent, en comparant la valeur de leurs hachages. Si tout est correct, elle retourne vrai ; sinon, elle retourne faux.

```python
@staticmethod
def check_validity(block, prev_block):
    if prev_block.index + 1 != block.index:
        return False

    elif prev_block.calculate_hash != block.prev_hash:
        return False

    elif not BlockChain.verifying_proof(block.proof_no, prev_block.proof_no):
        return False

    elif block.timestamp <= prev_block.timestamp:
        return False

    return True

```

### e. Ajout des données de transactions

La méthode _**new_data**_ est utilisée pour ajouter les données de transactions à un bloc. C'est une méthode très simple : elle accepte trois paramètres (détails de l'expéditeur, détails du destinataire et quantité) et ajoute les données de transaction à la liste _**self.current_data**_.

À chaque fois qu'un nouveau bloc est créé, cette liste est allouée à ce bloc et réinitialisée une fois de plus comme expliqué dans la méthode _**construct_block**_.

Une fois les données de transaction ajoutées à la liste, l'index du prochain bloc à créer est retourné.

Cet index est calculé en ajoutant 1 à l'index du bloc actuel (qui est le dernier dans la blockchain). Les données aideront un utilisateur à soumettre la transaction à l'avenir.

```python
def new_data(self, sender, recipient, quantity):
    self.current_data.append({
        'sender': sender,
        'recipient': recipient,
        'quantity': quantity
    })
    return True


```

### f. Ajout de la preuve de travail

[Preuve de travail](https://en.bitcoin.it/wiki/Proof_of_work) est un concept qui empêche la blockchain d'être abusée. Simplement, son objectif est d'identifier un nombre qui résout un problème après qu'une certaine quantité de travail informatique a été effectuée.

Si le niveau de difficulté pour identifier le nombre est élevé, cela décourage le spam et la falsification de la blockchain.

Dans ce cas, nous utiliserons un algorithme simple qui décourage les gens de miner des blocs ou de créer des blocs facilement.

```python
@staticmethod
def proof_of_work(last_proof):
    '''cet algorithme simple identifie un nombre f' tel que hash(ff') contient 4 zéros initiaux
         f est le précédent f'
         f' est la nouvelle preuve
        '''
    proof_no = 0
    while BlockChain.verifying_proof(proof_no, last_proof) is False:
        proof_no += 1

    return proof_no


@staticmethod
def verifying_proof(last_proof, proof):
    #vérification de la preuve : est-ce que hash(last_proof, proof) contient 4 zéros initiaux ?

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


```

### g. Obtention du dernier bloc

Enfin, la méthode **_latest_block_** est une méthode auxiliaire qui aide à obtenir le dernier bloc de la blockchain. Rappelez-vous que le dernier bloc est en fait le bloc actuel de la chaîne.

```python
@property
    def latest_block(self):
        return self.chain[-1]

```

## Mettons tout ensemble

Voici le code complet pour créer la cryptomonnaie **fccCoin**.

Vous pouvez également obtenir le code sur [ce dépôt GitHub](https://github.com/Alfrick/Create-Cryptocurrency-in-Python).

```python
import hashlib
import time


class Block:

    def __init__(self, index, proof_no, prev_hash, data, timestamp=None):
        self.index = index
        self.proof_no = proof_no
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = timestamp or time.time()

    @property
    def calculate_hash(self):
        block_of_string = "{}{}{}{}{}".format(self.index, self.proof_no,
                                              self.prev_hash, self.data,
                                              self.timestamp)

        return hashlib.sha256(block_of_string.encode()).hexdigest()

    def __repr__(self):
        return "{} - {} - {} - {} - {}".format(self.index, self.proof_no,
                                               self.prev_hash, self.data,
                                               self.timestamp)


class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

    def construct_genesis(self):
        self.construct_block(proof_no=0, prev_hash=0)

    def construct_block(self, proof_no, prev_hash):
        block = Block(
            index=len(self.chain),
            proof_no=proof_no,
            prev_hash=prev_hash,
            data=self.current_data)
        self.current_data = []

        self.chain.append(block)
        return block

    @staticmethod
    def check_validity(block, prev_block):
        if prev_block.index + 1 != block.index:
            return False

        elif prev_block.calculate_hash != block.prev_hash:
            return False

        elif not BlockChain.verifying_proof(block.proof_no,
                                            prev_block.proof_no):
            return False

        elif block.timestamp <= prev_block.timestamp:
            return False

        return True

    def new_data(self, sender, recipient, quantity):
        self.current_data.append({
            'sender': sender,
            'recipient': recipient,
            'quantity': quantity
        })
        return True

    @staticmethod
    def proof_of_work(last_proof):
        '''cet algorithme simple identifie un nombre f' tel que hash(ff') contient 4 zéros initiaux
         f est le précédent f'
         f' est la nouvelle preuve
        '''
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        #vérification de la preuve : est-ce que hash(last_proof, proof) contient 4 zéros initiaux ?

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  #cela implique que ce nœud a créé un nouveau bloc
            receiver=details_miner,
            quantity=
            1,  #créer un nouveau bloc (ou identifier le numéro de preuve) est récompensé par 1
        )

        last_block = self.latest_block

        last_proof_no = last_block.proof_no
        proof_no = self.proof_of_work(last_proof_no)

        last_hash = last_block.calculate_hash
        block = self.construct_block(proof_no, last_hash)

        return vars(block)

    def create_node(self, address):
        self.nodes.add(address)
        return True

    @staticmethod
    def obtain_block_object(block_data):
        #obtient l'objet bloc à partir des données de bloc

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])


```

Maintenant, testons notre code pour voir s'il fonctionne.

```python
blockchain = BlockChain()

print("***Minage de fccCoin sur le point de commencer***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #cela implique que ce nœud a créé un nouveau bloc
    recipient="Quincy Larson",  #envoyons quelques pièces à Quincy !
    quantity=
    1,  #créer un nouveau bloc (ou identifier le numéro de preuve) est récompensé par 1
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Minage de fccCoin a été réussi***")
print(blockchain.chain)

```

Cela a fonctionné !

Voici le résultat du processus de minage :

```python
***Minage de fccCoin sur le point de commencer***
[0 - 0 - 0 - [] - 1566930640.2707076]
***Minage de fccCoin a été réussi***
[0 - 0 - 0 - [] - 1566930640.2707076, 1 - 88914 - a8d45cb77cddeac750a9439d629f394da442672e56edfe05827b5e41f4ba0138 - [{'sender': '0', 'recipient': 'Quincy Larson', 'quantity': 1}] - 1566930640.5363243]

```

## Conclusion

Voilà !

C'est ainsi que vous pourriez créer votre propre blockchain en utilisant Python.

Je dois dire que ce tutoriel démontre simplement les concepts de base pour vous initier à la technologie blockchain innovante.

Si **cette pièce** était déployée telle quelle, elle ne pourrait pas répondre aux demandes actuelles du marché pour une cryptomonnaie stable, sécurisée et facile à utiliser.

Par conséquent, elle peut encore être améliorée en ajoutant des fonctionnalités supplémentaires pour améliorer ses capacités de minage et d'envoi de [transactions financières](https://www.forextradingbig.com/).

Néanmoins, c'est un bon point de départ si vous décidez de vous faire un nom dans le monde amazing des cryptos.

Si vous avez des commentaires ou des questions, veuillez les poster ci-dessous.

Bon (crypto) codage !