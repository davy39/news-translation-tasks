---
title: A Protocol for Sellable Smart Contracts
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-23T19:04:34.000Z'
originalURL: https://freecodecamp.org/news/a-protocol-for-sellable-smart-contracts-829bc2ce02b3
coverImage: https://cdn-media-1.freecodecamp.org/images/1*DTkbYDqroiSzJ3k5c_x5Zg.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: Ethereum
  slug: ethereum
- name: General Programming
  slug: programming
- name: Smart Contracts
  slug: smart-contracts
- name: Solidity
  slug: solidity
seo_title: null
seo_desc: 'By Pablo Ruiz

  Ethereum doesn’t have the concept of smart contract ownership built into it.Even
  though the creation and deployment of a smart contract is done by an account — be
  it an External Owned Account (EOA) or another contract — being the creato...'
---

By Pablo Ruiz

Ethereum doesn’t have the concept of smart contract ownership built into it.  
Even though the creation and deployment of a smart contract is done by an account — be it an External Owned Account (EOA) or another contract — being the creator of the smart contract doesn’t give the account any special privileges over the contract they deployed.

Most use cases for smart contracts require someone to own the contracts. This “owner” is given privileges — and responsibilities — over the smart contract.

In a crowdsale contract they might be tasked with managing the whole process and pausing the crowdsale if something goes wrong.

In a Lottery/Ruffle Dapp they might be tasked with executing the number draw.

In any contract that holds funds, they might be set as the beneficiary upon construct destruction.

![Image](https://cdn-media-1.freecodecamp.org/images/BXe8PzvTK9LjO7-H1962DwtjrlaAXfNmD8kC)
_Photo by [Unsplash](https://unsplash.com/photos/OvitgXQeN0Q?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Ricardo Resende</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

A common pattern used by many smart contracts is to set the owner to the account deploying the contract like so:

```
pragma solidity 0.4.19;
```

```
contract MyContract {  address owner;
```

```
  function MyContract(){    owner = msg.sender;  }}
```

Then, adding a modifier:

```
modifier onlyOwner {  require(msg.sender == owner);  _;    }
```

And finally, using that modifier to enforce that critical operations can only be performed by the owner of the contract:

```
// Suicide the contract and transfer funds to the owner// Only available to the owner, for obvious reasons.
```

```
function destroyContract() public onlyOwner {  selfdestruct(owner);}
```

### The Problem with Changing Contract Ownership

There are some situations that would require ownership of a contract to be given to someone else. To name a few:

* The person that deployed the contract did it on behalf of someone else  
A developer or consultant doing a contracting job for a company
* A company wants to liquidate / sell its assets, which include smart contracts  
Which might or not have ether balance
* The owner of the smart contract wants to give it away, donate it, or just flip it for profit

![Image](https://cdn-media-1.freecodecamp.org/images/NFbHtRcIE62fv8DdiE144boi720LyXmFMp7I)
_Photo by [Unsplash](https://unsplash.com/photos/5x8kipLwVug?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">rawpixel.com</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

Some contracts, but unfortunately not many, include a function to give ownership of the contract to some other account. And some of them also include another function for that person to accept the ownership that has been bestowed upon him.

```
function changeOwner(address _newOwner)public onlyOwner {  ownerCandidate = _newOwner;}
```

```
function acceptOwnership()public {  require(msg.sender == ownerCandidate);    owner = ownerCandidate;}
```

Now, the situations mentioned above share a few common issues that these not-so-widely-used `changeOwner()` and `acceptOwnership()` functions don’t address:

* How can the buyer of the contract be certain that once they pay for the ownership of the contract, the seller will actually execute the corresponding `changeOwner()` function?
* This can happen the other way around. How can the seller of the contract be certain that they will get paid if they cede ownership first?
* How can the buyer of the contract be certain that the current owner of the contract will not modify it (well, it’s data) before giving away its ownership?

### The Sellable Contract Protocol

The solution I propose is implementing a series of functions that would allow the owner of a smart contract to sell it in exchange of ether to someone of his choosing or just put it up for sale for anyone to buy at the asking price on a first-come first-save basis. This could be extended to allow different sale methods using different auction styles.

The details of the protocol can be read — and discussed — [on the corresponding EIP](https://github.com/ethereum/EIPs/issues/798).

In the following paragraphs I’ll go through an implementation example, which is available on my [Github Repository.](https://github.com/pabloruiz55/Saleable)

#### Handling Ownership

Handling ownership of the contract is pretty basic. As typically done, we set the owner of the deployed contract to `msg.sender` upon initialization:

```
function Sellable() public {        owner = msg.sender;        Transfer(now,address(0),owner,0);    }
```

Then, we add the `onlyOwner` modifier, which will be used on every function that we want to make only executable by the person currently owning the contract:

```
modifier onlyOwner {        require(msg.sender == owner);        _;    }
```

What we’ll want our contract to do is to allow the `owner` to be changed under certain conditions.

#### Putting the Contract for Sale

The owner of the contract can put it up for sale by calling the following function:

```
function initiateSale(uint _price, address _to) onlyOwner public {        require(_to != address(this) && _to != owner);        require(!selling);                selling = true;                // Set the target buyer, if specified.        sellingTo = _to;                askingPrice = _price;    }
```

`initiateSale()` takes two parameters:

* **uint _price**: which is the price the owner wants to sell the contract for.
* **address _to:** which is optional, and corresponds to who the owner wants to sell the contract to.

When putting the contract up for sale, the owner has two options: They can choose the buyer, in that case the sale has been prearrange. Or they can simply “announce” the contract is for sale and the first person to claim it (and paying its price) gets it.

Additionally, the asking price can be set to 0. This means that the owner of the contract is allowed to gift, donate or give the contract away.

There’s one more important thing to notice: There’s a `ifNotLocked` modifier that can be added to the contract’s functions to prevent them from being executed if the contract is in a sale process. If used properly, this prevents the contract’s data from being modified just before it is purchased.

Finally, there’s the `cancelPurchase()` function which allows the owner to cancel the sale before someone completes it.

```
function cancelSale() onlyOwner public {        require(selling);                // Reset sale variables        resetSale();    }
```

#### Buying the Contract

Once the contract is up for sale, all it takes to complete the sale is for the buyer (if it was specified) or anyone (if no particular buyer was specified) to call the following function:

```
function completeSale() public payable {        require(selling);        require(msg.sender != owner);        require(msg.sender == sellingTo || sellingTo == address(0));        require(msg.value == askingPrice);                // Swap ownership        address prevOwner = owner;        address newOwner = msg.sender;        uint salePrice = askingPrice;                owner = newOwner;                // Transaction cleanup        resetSale();                prevOwner.transfer(salePrice);                Transfer(now,prevOwner,newOwner,salePrice);    }
```

The `completeSale()` function is a `payable` function which requires the ether to be sent. The amount to be sent must be the exactly the same the owner set as the asking price.

When `completeSale()` is executed, the ether will be transferred to the owner and then the ownership will be transferred to the buyer. This finishes the transaction and cleans up the contract for the new owner, who can now use it normally, or even put it up for sale again.

#### An Example Use Case

Here’s a very simple example of how this base contract could be used:

```
contract Kitty is Sellable {        string public name;    uint public kittyValue = 0;        function Kitty(string _name) public {        name = _name;    }        function findNewOwner() public onlyOwner {        kittyValue = kittyValue + 1 ether;           super.initiateSale(kittyValue,address(0));    }        function renameKitty(string newName) ifNotLocked public onlyOwner {        name = newName;    }        function buyKitty() public payable {        require(msg.value == kittyValue);        super.completeSale();    }}
```

We have a contract which represents a CryptoKitty ?. The owner can f`indNewOwner()` to put it up for sale. Each time the kitty is bought his value increases by 1 ether. The owner of the kitty can change its name, as long as it is not being sold at the moment by implementing the i`fNotLocked` modifier in r`enameKitty` .

#### **That’s it!**

If you have further suggestions to improve this Sellable protocol, please add your comments, bugs or suggestions [in the EIP I created.](https://github.com/ethereum/EIPs/issues/798)

![Image](https://cdn-media-1.freecodecamp.org/images/4T98AkZfQPTp94yyrhpXDLhgsJ76RIWbt1FH)
_Photo by [Unsplash](https://unsplash.com/photos/xulIYVIbYIc?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title="">Jonas Vincent</a> on <a href="https://unsplash.com/?utm_source=unsplash&amp;utm_medium=referral&amp;utm_content=creditCopyText" rel="noopener" target="_blank" title=")_

