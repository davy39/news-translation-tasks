---
title: How to Create Your Own Cryptocurrency Using Python
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
seo_title: null
seo_desc: 'By Alfrick Opidi


  With the current rise of cryptocurrencies, blockchain is creating a buzz in the
  technology world. This technology has attracted so much attention mainly because
  of its ability to guarantee security, enforce decentralization, and qui...'
---

By Alfrick Opidi

> With the current rise of cryptocurrencies, blockchain is creating a buzz in the technology world. This technology has attracted so much attention mainly because of its ability to guarantee security, enforce decentralization, and quicken processes to several industries—especially to the financial industry.

Essentially, a blockchain is a public database that irreversibly documents and authenticates the possession and transmission of digital assets. Digital currencies, like Bitcoin and Ethereum, are based on this concept. Blockchain is an exciting technology that you can use to transform the capabilities of your applications.

Of late, we’ve been seeing governments, organizations, and individuals using the blockchain technology to create their own cryptocurrencies—and avoid being left behind. Notably, when Facebook proposed its own cryptocurrency, called [Libra](https://libra.org/en-US/white-paper/#introduction), the announcement stirred many waters across the world.

What if you could also follow suit and create your own version of a cryptocurrency?

I thought about this and decided to develop an algorithm that creates a crypto.

I decided to call the cryptocurrency **fccCoin**.

In this tutorial, I’m going to illustrate the step-by-step process I used to build the digital currency (I used the object-oriented concepts of the [Python](https://www.freecodecamp.org/news/best-python-tutorial/) programming language).

Here is the basic blueprint of the blockchain algorithm for creating the **fccCoin**:

```python
class Block:

    def __init__():

    #first block class

        pass
    
    def calculate_hash():
    
    #calculates the cryptographic hash of every block
        
    
class BlockChain:
    
    def __init__(self):
     # constructor method
    pass
    
    def construct_genesis(self):
        # constructs the initial block
        pass

    def construct_block(self, proof_no, prev_hash):
        # constructs a new block and adds it to the chain
        pass

    @staticmethod
    def check_validity():
        # checks whether the blockchain is valid
        pass

    def new_data(self, sender, recipient, quantity):
        # adds a new transaction to the data of the transactions
        pass

    @staticmethod
    def construct_proof_of_work(prev_proof):
        # protects the blockchain from attack
        pass
   
    @property
    def last_block(self):
        # returns the last block in the chain
        return self.chain[-1]


```

Now, let me explain what is taking place…

## 1. Building the first Block class

A blockchain comprises of several blocks that are joined to each other (that sounds familiar, right?).

The chaining of blocks takes place such that if one block is tampered with, the rest of the chain becomes invalid.

In applying the above concept, I created the following initial block class:

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

  
As you can see from the code above, I defined the **__init__()** function, which will be executed when the **Block** class is being initiated, just like in any other Python class.

I provided the following parameters to the initiation function:

* **self**—this refers to the instance of the **Block** class, making it possible to access the methods and attributes associated with the class;
* **index**—this keeps track of the position of the block within the blockchain;
* **proof_no**—this is the number produced during the creation of a new block (called mining);
* **prev_hash**—this refers to the hash of the previous block within the chain;
* **data**—this gives a record of all transactions completed, such as the quantity bought;
* **timestamp**—this places a timestamp for the transactions.

The second method in the class, **calculate_hash**, will generate the hash of the blocks using the above values. The SHA-256 module is imported into the project to assist in obtaining the hashes of the blocks.  


After the values have been inputted into the cryptographic hash algorithm, the function will return a 256-bit string representing the contents of the block.  


This is how security is achieved in blockchains—every block will have a hash and that hash will rely on the hash of the previous block. 

As such, if someone tries to compromise any block in the chain, the other blocks will have invalid hashes, leading to disruption of the entire blockchain network.  


Ultimately, a block will look like this:

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

## 2. Building the Blockchain class

The main idea of a blockchain, just as the name implies, involves “chaining” several blocks to one another. 

Therefore, I’m going to construct a **Blockchain** class that will be useful in managing the workings of the whole chain. This is where most of the action is going to take place.

The **Blockchain** class will have various helper methods for completing various tasks in the blockchain.

Let me explain the role of each of the methods in the class.

### a. Constructor method  


This method ensures the blockchain is instantiated.

```python
class BlockChain:

    def __init__(self):
        self.chain = []
        self.current_data = []
        self.nodes = set()
        self.construct_genesis()

```

  
Here are the roles of its attributes:  


* **self.chain**—this variable keeps all blocks;
* **self.current_data**—this variable keeps all the completed transactions in the block;
* **self.construct_genesis()**—this method will take care of constructing the initial block.

### b. Constructing the genesis block  


The blockchain requires a _**construct_genesis**_ method to build the initial block in the chain. In the blockchain convention, this block is special because it symbolizes the start of the blockchain.  


In this case, let’s construct it by simply passing some default values to the _**construct_block**_ method.

I gave both _**proof_no**_ and _**prev_hash**_ a value of zero, although you can provide any value you want.  


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

###   
c. Constructing new blocks

  
The **_construct_block_** method is used for creating new blocks in the blockchain.

Here is what is taking place with the various attributes of this method:  


* **index**—this represents the length of the blockchain;
* **proof_nor & prev_hash**—the caller method passes them;
* **data**—this contains a record of all the transactions that are not included in any block on the node;
* **self.current_data**—this is used to reset the transaction list on the node. If a block has been constructed and the transactions allocated to it, the list is reset to ensure that future transactions are added into this list. And, this process will take place continuously;
* **self.chain.append()—**this method joins newly constructed blocks to the chain;
* **return**—lastly, a constructed block object is returned.  


### d. Checking validity

  
The _**check_validity**_ method is important in assessing the integrity of the blockchain and ensuring anomalies are absent.  


As mentioned earlier, hashes are essential for the security of the blockchain as even the slightest change in the object will lead to the generation of a completely new hash.  


Therefore, this **_check_validity_** method uses _**if**_ statements to check whether the hash of every block is correct.  


It also verifies if every block points to the right previous block, through comparing the value of their hashes. If everything is correct, it returns true; otherwise, it returns false.  


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

### e. Adding data of transactions

  
The _**new_data**_ method is used for adding the data of transactions to a block. It’s a very simple method: it accepts three parameters (sender’s details, receiver’s details, and quantity) and append the transaction data to _**self.current_data**_ list.  


Anytime a new block is created, this list is allocated to that block and reset once more as explained in the _**construct_block**_ method.  


Once the transaction data has been added to the list, the index of the next block to be created is returned.  


This index is calculated by adding 1 to the index of the current block (which is the last in the blockchain). The data will assist a user in submitting the transaction in future.

```python
def new_data(self, sender, recipient, quantity):
    self.current_data.append({
        'sender': sender,
        'recipient': recipient,
        'quantity': quantity
    })
    return True


```

###   
f. Adding proof of work

  
[Proof of work](https://en.bitcoin.it/wiki/Proof_of_work) is a concept that prevents the blockchain from abuse. Simply, its objective is to identify a number that solves a problem after a certain amount of computing work is done.

If the difficulty level of identifying the number is high, it discourages spamming and tampering with the blockchain.

In this case, we’ll use a simple algorithm that discourages people from mining blocks or creating blocks easily.

```python
@staticmethod
def proof_of_work(last_proof):
    '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
    proof_no = 0
    while BlockChain.verifying_proof(proof_no, last_proof) is False:
        proof_no += 1

    return proof_no


@staticmethod
def verifying_proof(last_proof, proof):
    #verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

    guess = f'{last_proof}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:4] == "0000"


```

### g. Getting the last block

  
Lastly, the **_latest_block_** method is a helper method that assists in obtaining the last block in the blockchain. Remember that the last block is actually the current block in the chain.

```python
@property
    def latest_block(self):
        return self.chain[-1]

```

## Let’s sum everything together

  
Here is the entire code for creating the **fccCoin** cryptocurrency.

You can also get the code on [this GitHub repository.](https://github.com/Alfrick/Create-Cryptocurrency-in-Python)

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
        '''this simple algorithm identifies a number f' such that hash(ff') contain 4 leading zeroes
         f is the previous f'
         f' is the new proof
        '''
        proof_no = 0
        while BlockChain.verifying_proof(proof_no, last_proof) is False:
            proof_no += 1

        return proof_no

    @staticmethod
    def verifying_proof(last_proof, proof):
        #verifying the proof: does hash(last_proof, proof) contain 4 leading zeroes?

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

    @property
    def latest_block(self):
        return self.chain[-1]

    def block_mining(self, details_miner):

        self.new_data(
            sender="0",  #it implies that this node has created a new block
            receiver=details_miner,
            quantity=
            1,  #creating a new block (or identifying the proof number) is awarded with 1
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
        #obtains block object from the block data

        return Block(
            block_data['index'],
            block_data['proof_no'],
            block_data['prev_hash'],
            block_data['data'],
            timestamp=block_data['timestamp'])


```

  
Now, let’s test our code to see if it works.

```python
blockchain = BlockChain()

print("***Mining fccCoin about to start***")
print(blockchain.chain)

last_block = blockchain.latest_block
last_proof_no = last_block.proof_no
proof_no = blockchain.proof_of_work(last_proof_no)

blockchain.new_data(
    sender="0",  #it implies that this node has created a new block
    recipient="Quincy Larson",  #let's send Quincy some coins!
    quantity=
    1,  #creating a new block (or identifying the proof number) is awarded with 1
)

last_hash = last_block.calculate_hash
block = blockchain.construct_block(proof_no, last_hash)

print("***Mining fccCoin has been successful***")
print(blockchain.chain)

```

  
It worked!

Here is the output of the mining process:

```python
***Mining fccCoin about to start***
[0 - 0 - 0 - [] - 1566930640.2707076]
***Mining fccCoin has been successful***
[0 - 0 - 0 - [] - 1566930640.2707076, 1 - 88914 - a8d45cb77cddeac750a9439d629f394da442672e56edfe05827b5e41f4ba0138 - [{'sender': '0', 'recipient': 'Quincy Larson', 'quantity': 1}] - 1566930640.5363243]

```

##   
Conclusion

  
There you have it!

That’s how you could create your own blockchain using Python.

Let me say that this tutorial just demonstrates the basic concepts for getting your feet wet in the innovative blockchain technology.

If **this coin** were deployed as-is, it could not meet the present market demands for a stable, secure, and easy-to-use cryptocurrency.

Therefore, it can still be improved by adding additional features to enhance its capabilities for mining and sending [financial transactions](https://www.forextradingbig.com/).

Nonetheless, it’s a good starting point if you decide to make your name known in the amazing world of cryptos.

If you have any comments or questions, please post them below.

Happy (crypto) coding!

