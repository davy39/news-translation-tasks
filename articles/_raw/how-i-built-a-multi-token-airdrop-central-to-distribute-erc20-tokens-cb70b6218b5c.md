---
title: How I built a multi-token Airdrop Central to distribute ERC20 tokens
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-11T09:13:15.000Z'
originalURL: https://freecodecamp.org/news/how-i-built-a-multi-token-airdrop-central-to-distribute-erc20-tokens-cb70b6218b5c
coverImage: https://cdn-media-1.freecodecamp.org/images/1*IBcCEfr6Zj3ctsf48bVzvA.jpeg
tags:
- name: Design
  slug: design
- name: Ethereum
  slug: ethereum
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: null
seo_desc: 'By Pablo Ruiz

  Every now and then, while browsing questions on Ethereum Stack Exchange — the go-to
  site for questions related to Solidity development, and for me, the go-to place
  to contribute to the dev community — I see the following question:

  “How ...'
---

By Pablo Ruiz

Every now and then, while browsing questions on [Ethereum Stack Exchange](https://ethereum.stackexchange.com/) — the go-to site for questions related to Solidity development, and for me, the go-to place to contribute to the dev community — I see the following question:

“How to do an **airdrop** of my tokens.”

In the context of a Token Sale campaign, an Airdrop refers to sending tokens to multiple accounts for free. This is a trend that has recently become popular to promote upcoming ICOs / Token Crowdsales.

Some of these airdrops are done as a time and/or volume based campaign, where people are told that if they own some amount of tokens by some date, they will receive more tokens.

Some other airdrops are even done in an unsolicited manner. Teams will just send tokens to random accounts from a list. If you were on that list and you happen to check your balance for that token, you will see them.

There are also a few sites that allow users to subscribe to find out how to willingly participate in these airdrops. They will typically ask you to subscribe to some mailing list or give you referral links to participate in token sales.

### How Token Airdrops are Typically Done

There are a few ways these token airdrops are handled by teams.

* Some of them do it manually. They just build a list on an spreadsheet, and then proceed to manually transfer the tokens to each account.
* Others build a very simple smart contract, which receives an array of addresses, and proceeds to transfer some amount of tokens to each of those address.
* Others also use a smart contract to allow people to proactively withdraw tokens they have been assigned beforehand.

I haven’t yet seen a solution that allows people to just sign up and then receive **any tokens sent by multiple teams.**

### The Token Airdrop Central

In this article, I’m going to describe how I built a smart contract that works as a central for airdrops. Basically, people can subscribe to this airdrop central, and from then on, when a team performs an airdrop to the central, the subscribed users can withdraw their share of the airdrop for free.

On the other hand, teams doing airdrops can just send the tokens to this central which will get evenly distributed to all users subscribed at that time.  
The Airdrop Central keeps 2% of those tokens as a fee for the service.

Its important to notice that this Airdrop Central allows any teams to drop their tokens for the existing community to withdraw. The list of users is shared among all teams. So the more people each team reaches out to individually, the more people that will benefit from tokens airdropped by other teams.

As a side note, it’s worth mentioning that this solution is not completely decentralized, as it depends on an owner to review and approve submissions. This mechanism is in place to prevent potential security issues related to having to trust unknown 3rd party contracts (ERC20 tokens submitted by teams). I couldn’t allow just anyone to submit any contract address, which could contain malicious code instead of the typical ERC20 token.

The Airdrop Central has not been deployed on any network yet, as I’d like to thoroughly test it first. In the meantime, you can check the code (and even submit any bugs or suggestions) on my Github Repository:

* If you are a user wanting to receive tokens, [please add your address to this list.](https://goo.gl/forms/5HBhlXacSXm8xRl22) When I deploy the Airdrop Central to the mainnet, I’ll add your account to it so you can receive tokens from the get-go. Once teams start doing airdrops to it, you will be able to withdraw tokens for free.
* If you are a team looking into an easy way to send tokens to promote your Token Sale, please follow the instructions below to start the verification process.

Once I deploy the Airdrop Central to the mainnet, I’ll accept/reject the submissions. [Open an Issue on the Airdrop Central’s Github Repository](https://github.com/pabloruiz55/AirdropCentral/issues) with the tag “Submission” and the following title: **[Token Symbol] — [Token Name] — [Token Address] — [Token Owner Address]**. The token should already be deployed on the mainnet so the smart contract can be reviewed. An admin will notify you when it gets approved by leaving you a message on the Github Issue you created.

#### How it Works

**For the end users:** Users sign up to the Token Central. Then, when a team airdrops tokens, the users can check how many of them they were awarded (based on how many were sent and how many users were signed to the central at that time) and withdraw them. All they need to know to withdraw their share of the tokens is the address of the token contract.

**For the teams:** Submissions first have to be approved. Given that the Airdrop Central contract interacts with unknown and potentially harmful 3rd party contracts, it has to be approved by the central’s owner or designated admins before a token is accepted. The admins will basically have to check that the address submitted corresponds to an ERC20 compliant token contract and that it doesn’t contain any malicious code.

Once the team and token are approved, they can make as many airdrops as they want using the same account and token address. The owner of the central keeps 2% of the submitted tokens as a fee for using the service, and the rest are stored within the contract, available for the users to withdraw. Each airdrop has an expiration date. Tokens not withdrawn by users by that date can be retrieved by the team.

#### Using the Airdrop Central Contract

**For end users:**

1. Sign up to the Airdrop Central by executing the `signUpForAirdrops()` function. This will subscribe you to future airdrops.
2. Call `getTokensAvailableToMe(address _tokenAddress)` to check how many tokens you are entitled to for the given token, based on whether or not the corresponding airdrop expired and how many tokens you already withdrew.
3. If you want to withdraw your tokens, call `withdrawTokens(address _tokenAddress)` which will check the tokens available with the same logic as above and transfer them.
4. You should now be able to call `balanceOf(address _owner)` on the token contract to see the tokens added to your balance.

**For teams:**

1. Submit your token information as explained above.
2. Once the submission is approved, you’ll be able to do the airdrop. First, you need to give an allowance for the tokens to the Airdrop Central on your ERC20 token. You can do that by calling approve() on the token and passing the address of the Airdrop Central and the amount to allow. **Don’t do this until your submission has been approved. Furthermore, only call approve() — don’t call transfer() or you will lose your tokens.**
3. Once you have given the Airdrop Central an allowance on the tokens you own, you can initiate the airdrop by calling the function `airdropTokens(address _tokenAddress, uint _totalTokensToDistribute, uint _expirationTime)`   
where:  
`address _tokenAddress` is the address of the token you submitted.  
`uint _totalTokensToDistribute` is the total tokens to distribute.  
`uint _expirationTime` is how long (in seconds) will the airdrop last.
4. _Optional step:_ You can execute `returnTokensToAirdropper(address _tokenAddress)` to get back the tokens that were not collected once the expiration date has been reached.

**Regarding token distribution:**

* `_totalTokensToDistribute` is the total amount of tokens you want to distribute. The function will take care of adding the necessary decimals, obtained from the token contract. For example: If you want to airdrop 100 tokens, just enter 100, no matter how many decimals your token has.
* The tokens you send will be evenly distributed between all users currently registered. You can check how many registered users the central currently has by calling `userSignupCount()` in order to approximately figure out how many tokens you want to distribute to each.
* Users that sign up **after** the airdrop has been submitted won’t receive tokens from that submission.

### Building the Airdrop Central

[The complete, fully commented code can be found on my Github Repository.](https://github.com/pabloruiz55/AirdropCentral)  
What follows is a detailed explanation of the most important parts of the code.

#### Managing Submissions

As mentioned above, we need to put a few mechanisms in place to prevent just anyone from submitting any contract. Since the Airdrop Central contract interacts with 3rd party token contracts that could contain harmful code, we first need to review each submission to prevent problems.

In order to do this we will receive submissions off-chain, review them manually, and then, if everything is ok, approve them.

```
function approveSubmission(address _airdropper, address _tokenAddress) public onlyAdmin {        require(!airdropperBlacklist[_airdropper]);        require(!tokenBlacklist[_tokenAddress]);                tokenWhitelist[_tokenAddress] = true;    }
```

At any point, if we detect a problem with either a submitted contract or an account submitting malicious contracts, we can revoke access to the associated tokens and put them in a blacklist to prevent new submissions. **Doing this also causes tokens to be inaccessible for withdrawal.**

This could be controversial, as it allows the owner/admins to freeze the tokens within the contract at their will. But on the other hand, it’s the only mechanism we have to fight malicious code that might have gone undetected when the token contract was first approved.

```
function revokeSubmission(address _airdropper, address _tokenAddress) public onlyAdmin {        if(_tokenAddress != address(0)){            tokenWhitelist[_tokenAddress] = false;            tokenBlacklist[_tokenAddress] = true;        }                if(_airdropper != address(0)){            airdropperBlacklist[_airdropper] = true;        }            }
```

If, for some reason, we blacklisted the wrong token/account or they were good citizens after all, the owner can remove them from the blacklist. This also re-enables the frozen tokens to be withdrawn.

#### User Sign-up Process

Once the Airdrop Central contract has been deployed, users can start signing up. There are two ways to sign users up:

They can do it themselves by calling the following function:

```
function signUpForAirdrops() public ifNotPaused{        require(signups[msg.sender].userAddress == address(0));        signups[msg.sender] = User(msg.sender,now);        userSignupCount++;                E_Signup(msg.sender,now);    }
```

Or an admin can sign them up by calling `signupUsersManually().` Notice that, as opposed to a “regular” airdrop, the teams can’t manually add users as we want to avoid “spamming” and adding users without their consent.

```
function signupUsersManually(address _user) public onlyAdmin {        require(signups[_user].userAddress == address(0));        signups[_user] = User(_user,now);        userSignupCount++;                E_Signup(msg.sender,now);    }
```

Additionally, users can remove themselves from the Airdrop Central to stop receiving tokens. Doing so also prevents them from being able to withdraw pending tokens. As a matter of fact they will be lost to them, so they should think twice before doing so.

#### Token Airdrop

Once a team has had their tokens approved by the Airdrop Central admin, they can perform any amount of airdrops for that token.

First, they need to give an allowance of the tokens they want to distribute to the Airdrop Central contract. In order to do that, they need to call the approve() function on the token, specifying how many tokens they want to allow the Airdrop Central to use.

Once that’s taken care of, they can perform the airdrop by calling the following function:

```
function airdropTokens(address _tokenAddress, uint _totalTokensToDistribute, uint _expirationTime) public ifNotPaused {        require(tokenWhitelist[_tokenAddress]);        require(!airdropperBlacklist[msg.sender]);                ERC20Basic token = ERC20Basic(_tokenAddress);        require(token.balanceOf(msg.sender) >= _totalTokensToDistribute);                //Multiply number entered by token decimals.        _totalTokensToDistribute = _totalTokensToDistribute.mul(10 ** uint256(token.decimals()));                // Calculate owner's tokens and tokens to airdrop        uint tokensForOwner = _totalTokensToDistribute.mul(ownersCut).div(100);        _totalTokensToDistribute = _totalTokensToDistribute.sub(tokensForOwner);                // Store the airdrop unique id in array (token address + id)        TokenAirdropID memory taid = TokenAirdropID(_tokenAddress,airdroppedTokens[_tokenAddress].length);        TokenAirdrop memory ta = TokenAirdrop(_tokenAddress,airdroppedTokens[_tokenAddress].length,msg.sender,now,now+_expirationTime,_totalTokensToDistribute,_totalTokensToDistribute,userSignupCount);        airdroppedTokens[_tokenAddress].push(ta);        airdrops.push(taid);                // Transfer the tokens        require(token.transferFrom(msg.sender,this,_totalTokensToDistribute));        require(token.transferFrom(msg.sender,owner,tokensForOwner));                E_AirdropSubmitted(_tokenAddress,ta.tokenOwner,ta.totalDropped,ta.airdropDate,ta.airdropExpirationDate);
```

```
}
```

The airdropTokens() function stores the tokens the contract was allowed to use in its internal balance. 2% of them are transferred to the contract owner and the rest are transferred to the contract. It can then distribute it among the users that were subscribed up to that moment.

The team that performed the airdrop can also recover the tokens that remain unclaimed past the expiration date of each airdrop by calling this function:

```
function returnTokensToAirdropper(address _tokenAddress) public ifNotPaused {        require(tokenWhitelist[_tokenAddress]); // Token must be whitelisted first                // Get the token        ERC20Basic token = ERC20Basic(_tokenAddress);                 uint tokensToReturn = 0;                for (uint i =0; i<airdroppedTokens[_tokenAddress].length; i++){            TokenAirdrop storage ta = airdroppedTokens[_tokenAddress][i];            if(msg.sender == ta.tokenOwner &&                airdropHasExpired(_tokenAddress,i)){                                tokensToReturn = tokensToReturn.add(ta.tokenBalance);                ta.tokenBalance = 0;            }        }        require(token.transfer(msg.sender,tokensToReturn));        E_TokensWithdrawn(_tokenAddress,msg.sender,tokensToReturn,now);
```

```
}
```

#### Token Withdrawal

The final thing we need to go over is the process by which the users withdraw the tokens they were sent. In order to do that, they need to call the `withdrawTokens(address _tokenAddress)` function. The function will go over all active (not yet expired or frozen) airdrops of the specified token and transfer them.

```
function withdrawTokens(address _tokenAddress) ifNotPaused public {        require(tokenWhitelist[_tokenAddress]); // Token must be whitelisted first                // Get User instance, given the sender account        User storage user = signups[msg.sender];        require(user.userAddress != address(0));                uint totalTokensToTransfer = 0;        // For each airdrop made for this token (token owner may have done several airdrops at any given point)        for (uint i =0; i<airdroppedTokens[_tokenAddress].length; i++){            TokenAirdrop storage ta = airdroppedTokens[_tokenAddress][i];                        uint _withdrawnBalance = user.withdrawnBalances[_tokenAddress][i];                        //Check that user signed up before the airdrop was done. If so, he is entitled to the tokens            //And the airdrop must not have expired            if(ta.airdropDate >= user.signupDate &&                now <= ta.airdropExpirationDate){                                // The user will get a portion of the total tokens airdroped,                // divided by the users at the moment the airdrop was created                uint tokensToTransfer = ta.totalDropped.div(ta.usersAtDate);                                // if the user has not alreay withdrawn the tokens                if(_withdrawnBalance < tokensToTransfer){                    // Register the tokens withdrawn by the user and total tokens withdrawn                    user.withdrawnBalances[_tokenAddress][i] = tokensToTransfer;                    ta.tokenBalance = ta.tokenBalance.sub(tokensToTransfer);                    totalTokensToTransfer = totalTokensToTransfer.add(tokensToTransfer);                                    }            }        }        // Get the token        ERC20Basic token = ERC20Basic(_tokenAddress);         // Transfer tokens from all airdrops that correspond to this user        require(token.transfer(msg.sender,totalTokensToTransfer));                E_TokensWithdrawn(_tokenAddress,msg.sender,totalTokensToTransfer,now);    }
```

#### Next Steps

One of the many things I’d like to do next is to build a web interface (a dapp) that allows people to see the latest and upcoming airdrops and subscribe to them.

If you are part of a team with an active ERC20 token, or you are planning on launching one and you’d like to use the Airdrop Central to do an airdrop, drop me a line. Otherwise, any feedback and suggestions are greatly appreciated.

I hope you enjoyed reading this article as much as I enjoyed writing it. I’m currently taking consultancy jobs related to smart contracts development. If you are planning on raising funds through an ICO or building a Blockchain-based product, feel free to get in touch with me.

