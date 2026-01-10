---
title: Comment j'ai construit un Airdrop Central multi-tokens pour distribuer des
  tokens ERC20
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
seo_title: Comment j'ai construit un Airdrop Central multi-tokens pour distribuer
  des tokens ERC20
seo_desc: 'By Pablo Ruiz

  Every now and then, while browsing questions on Ethereum Stack Exchange — the go-to
  site for questions related to Solidity development, and for me, the go-to place
  to contribute to the dev community — I see the following question:

  “How ...'
---

Par Pablo Ruiz

De temps en temps, en parcourant les questions sur [Ethereum Stack Exchange](https://ethereum.stackexchange.com/) — le site de référence pour les questions liées au développement Solidity, et pour moi, l'endroit idéal pour contribuer à la communauté des développeurs — je vois la question suivante :

« Comment faire un **airdrop** de mes tokens. »

Dans le contexte d'une campagne de vente de tokens, un Airdrop fait référence à l'envoi de tokens à plusieurs comptes gratuitement. C'est une tendance qui est récemment devenue populaire pour promouvoir les prochaines ICO / ventes de tokens.

Certains de ces airdrops sont réalisés dans le cadre d'une campagne basée sur le temps et/ou le volume, où les gens sont informés que s'ils possèdent une certaine quantité de tokens à une certaine date, ils recevront plus de tokens.

D'autres airdrops sont même réalisés de manière non sollicitée. Les équipes envoient simplement des tokens à des comptes aléatoires d'une liste. Si vous étiez sur cette liste et que vous vérifiez votre solde pour ce token, vous les verrez.

Il existe également quelques sites qui permettent aux utilisateurs de s'abonner pour découvrir comment participer volontairement à ces airdrops. Ils vous demanderont généralement de vous abonner à une liste de diffusion ou de vous donner des liens de parrainage pour participer aux ventes de tokens.

### Comment les Airdrops de Tokens sont généralement réalisés

Il existe plusieurs façons dont ces airdrops de tokens sont gérés par les équipes.

* Certains le font manuellement. Ils construisent simplement une liste sur une feuille de calcul, puis procèdent au transfert manuel des tokens à chaque compte.
* D'autres créent un contrat intelligent très simple, qui reçoit un tableau d'adresses, et procède au transfert d'une certaine quantité de tokens à chacune de ces adresses.
* D'autres utilisent également un contrat intelligent pour permettre aux gens de retirer proactivement les tokens qui leur ont été attribués au préalable.

Je n'ai pas encore vu de solution qui permet aux gens de simplement s'inscrire et de recevoir **des tokens envoyés par plusieurs équipes.**

### L'Airdrop Central

Dans cet article, je vais décrire comment j'ai construit un contrat intelligent qui fonctionne comme un central pour les airdrops. Basiquement, les gens peuvent s'abonner à ce central d'airdrop, et à partir de là, lorsqu'une équipe effectue un airdrop vers le central, les utilisateurs abonnés peuvent retirer leur part de l'airdrop gratuitement.

D'autre part, les équipes réalisant des airdrops peuvent simplement envoyer les tokens à ce central qui seront distribués équitablement à tous les utilisateurs abonnés à ce moment-là. Le Central d'Airdrop conserve 2 % de ces tokens comme frais pour le service.

Il est important de noter que ce Central d'Airdrop permet à toute équipe de déposer ses tokens pour que la communauté existante puisse les retirer. La liste des utilisateurs est partagée entre toutes les équipes. Ainsi, plus chaque équipe atteint de personnes individuellement, plus de personnes bénéficieront des tokens airdroppés par d'autres équipes.

En tant que note supplémentaire, il est intéressant de mentionner que cette solution n'est pas complètement décentralisée, car elle dépend d'un propriétaire pour examiner et approuver les soumissions. Ce mécanisme est en place pour prévenir les problèmes de sécurité potentiels liés à la nécessité de faire confiance à des contrats tiers inconnus (tokens ERC20 soumis par des équipes). Je ne pouvais pas permettre à n'importe qui de soumettre n'importe quelle adresse de contrat, qui pourrait contenir du code malveillant au lieu du token ERC20 typique.

Le Central d'Airdrop n'a pas encore été déployé sur un réseau, car je souhaite d'abord le tester minutieusement. En attendant, vous pouvez consulter le code (et même soumettre des bugs ou des suggestions) sur mon dépôt Github :

* Si vous êtes un utilisateur souhaitant recevoir des tokens, [veuillez ajouter votre adresse à cette liste.](https://goo.gl/forms/5HBhlXacSXm8xRl22) Lorsque je déploierai le Central d'Airdrop sur le mainnet, j'ajouterai votre compte pour que vous puissiez recevoir des tokens dès le départ. Une fois que les équipes commenceront à faire des airdrops, vous pourrez retirer des tokens gratuitement.
* Si vous êtes une équipe cherchant un moyen facile d'envoyer des tokens pour promouvoir votre vente de tokens, veuillez suivre les instructions ci-dessous pour commencer le processus de vérification.

Une fois que j'aurai déployé le Central d'Airdrop sur le mainnet, j'accepterai/rejeterai les soumissions. [Ouvrez un Issue sur le dépôt Github du Central d'Airdrop](https://github.com/pabloruiz55/AirdropCentral/issues) avec le tag « Submission » et le titre suivant : **[Symbole du Token] — [Nom du Token] — [Adresse du Token] — [Adresse du Propriétaire du Token]**. Le token doit déjà être déployé sur le mainnet pour que le contrat intelligent puisse être examiné. Un administrateur vous informera lorsqu'il sera approuvé en vous laissant un message sur l'Issue Github que vous avez créé.

#### Comment cela fonctionne

**Pour les utilisateurs finaux :** Les utilisateurs s'inscrivent au Token Central. Ensuite, lorsqu'une équipe airdrop des tokens, les utilisateurs peuvent vérifier combien de tokens ils ont reçus (en fonction du nombre de tokens envoyés et du nombre d'utilisateurs inscrits au central à ce moment-là) et les retirer. Tout ce qu'ils doivent savoir pour retirer leur part des tokens est l'adresse du contrat de token.

**Pour les équipes :** Les soumissions doivent d'abord être approuvées. Étant donné que le contrat Airdrop Central interagit avec des contrats tiers inconnus et potentiellement dangereux, il doit être approuvé par le propriétaire du central ou les administrateurs désignés avant qu'un token ne soit accepté. Les administrateurs devront essentiellement vérifier que l'adresse soumise correspond à un contrat de token conforme à l'ERC20 et qu'il ne contient aucun code malveillant.

Une fois l'équipe et le token approuvés, ils peuvent effectuer autant d'airdrops qu'ils le souhaitent en utilisant le même compte et la même adresse de token. Le propriétaire du central conserve 2 % des tokens soumis comme frais pour l'utilisation du service, et le reste est stocké dans le contrat, disponible pour que les utilisateurs les retirent. Chaque airdrop a une date d'expiration. Les tokens non retirés par les utilisateurs à cette date peuvent être récupérés par l'équipe.

#### Utilisation du contrat Airdrop Central

**Pour les utilisateurs finaux :**

1. Inscrivez-vous à l'Airdrop Central en exécutant la fonction `signUpForAirdrops()`. Cela vous inscrira aux futurs airdrops.
2. Appelez `getTokensAvailableToMe(address _tokenAddress)` pour vérifier combien de tokens vous avez droit pour le token donné, en fonction du fait que l'airdrop correspondant a expiré ou non et du nombre de tokens que vous avez déjà retirés.
3. Si vous souhaitez retirer vos tokens, appelez `withdrawTokens(address _tokenAddress)` qui vérifiera les tokens disponibles avec la même logique que ci-dessus et les transférera.
4. Vous devriez maintenant pouvoir appeler `balanceOf(address _owner)` sur le contrat de token pour voir les tokens ajoutés à votre solde.

**Pour les équipes :**

1. Soumettez les informations de votre token comme expliqué ci-dessus.
2. Une fois la soumission approuvée, vous pourrez effectuer l'airdrop. Tout d'abord, vous devez donner une autorisation pour les tokens à l'Airdrop Central sur votre token ERC20. Vous pouvez le faire en appelant approve() sur le token et en passant l'adresse de l'Airdrop Central et le montant à autoriser. **Ne faites pas cela tant que votre soumission n'a pas été approuvée. De plus, n'appelez que approve() — n'appelez pas transfer() ou vous perdrez vos tokens.**
3. Une fois que vous avez donné à l'Airdrop Central une autorisation sur les tokens que vous possédez, vous pouvez initier l'airdrop en appelant la fonction `airdropTokens(address _tokenAddress, uint _totalTokensToDistribute, uint _expirationTime)`
   où :
   `address _tokenAddress` est l'adresse du token que vous avez soumis.
   `uint _totalTokensToDistribute` est le total des tokens à distribuer.
   `uint _expirationTime` est la durée (en secondes) pendant laquelle l'airdrop durera.
4. *Étape optionnelle :* Vous pouvez exécuter `returnTokensToAirdropper(address _tokenAddress)` pour récupérer les tokens qui n'ont pas été collectés une fois la date d'expiration atteinte.

**Concernant la distribution des tokens :**

* `_totalTokensToDistribute` est le montant total de tokens que vous souhaitez distribuer. La fonction se chargera d'ajouter les décimales nécessaires, obtenues à partir du contrat de token. Par exemple : Si vous souhaitez airdrop 100 tokens, entrez simplement 100, peu importe le nombre de décimales de votre token.
* Les tokens que vous envoyez seront distribués équitablement entre tous les utilisateurs actuellement inscrits. Vous pouvez vérifier combien d'utilisateurs inscrits le central a actuellement en appelant `userSignupCount()` afin de déterminer approximativement combien de tokens vous souhaitez distribuer à chacun.
* Les utilisateurs qui s'inscrivent **après** que l'airdrop a été soumis ne recevront pas de tokens de cette soumission.

### Construction de l'Airdrop Central

[Le code complet et entièrement commenté peut être trouvé sur mon dépôt Github.](https://github.com/pabloruiz55/AirdropCentral)
Ce qui suit est une explication détaillée des parties les plus importantes du code.

#### Gestion des soumissions

Comme mentionné ci-dessus, nous devons mettre en place quelques mécanismes pour empêcher n'importe qui de soumettre n'importe quel contrat. Puisque le contrat Airdrop Central interagit avec des contrats de tokens tiers qui pourraient contenir du code malveillant, nous devons d'abord examiner chaque soumission pour prévenir les problèmes.

Pour ce faire, nous recevrons les soumissions hors chaîne, les examinerons manuellement, et si tout est correct, nous les approuverons.

```
function approveSubmission(address _airdropper, address _tokenAddress) public onlyAdmin {
    require(!airdropperBlacklist[_airdropper]);
    require(!tokenBlacklist[_tokenAddress]);
    
    tokenWhitelist[_tokenAddress] = true;
}
```

À tout moment, si nous détectons un problème avec un contrat soumis ou un compte soumettant des contrats malveillants, nous pouvons révoquer l'accès aux tokens associés et les mettre sur une liste noire pour empêcher de nouvelles soumissions. **Faire cela rend également les tokens inaccessibles pour le retrait.**

Cela pourrait être controversé, car cela permet au propriétaire/administrateurs de geler les tokens dans le contrat à leur guise. Mais d'un autre côté, c'est le seul mécanisme que nous avons pour lutter contre le code malveillant qui pourrait être passé inaperçu lors de l'approbation initiale du contrat de token.

```
function revokeSubmission(address _airdropper, address _tokenAddress) public onlyAdmin {
    if(_tokenAddress != address(0)){
        tokenWhitelist[_tokenAddress] = false;
        tokenBlacklist[_tokenAddress] = true;
    }
    
    if(_airdropper != address(0)){
        airdropperBlacklist[_airdropper] = true;
    }
}
```

Si, pour une raison quelconque, nous avons mis sur liste noire le mauvais token/compte ou s'ils étaient de bons citoyens après tout, le propriétaire peut les retirer de la liste noire. Cela réactive également les tokens gelés pour qu'ils puissent être retirés.

#### Processus d'inscription des utilisateurs

Une fois le contrat Airdrop Central déployé, les utilisateurs peuvent commencer à s'inscrire. Il existe deux façons d'inscrire les utilisateurs :

Ils peuvent le faire eux-mêmes en appelant la fonction suivante :

```
function signUpForAirdrops() public ifNotPaused{
    require(signups[msg.sender].userAddress == address(0));
    signups[msg.sender] = User(msg.sender,now);
    userSignupCount++;
    
    E_Signup(msg.sender,now);
}
```

Ou un administrateur peut les inscrire en appelant `signupUsersManually()`. Remarquez que, contrairement à un airdrop « régulier », les équipes ne peuvent pas ajouter manuellement des utilisateurs car nous voulons éviter le « spamming » et l'ajout d'utilisateurs sans leur consentement.

```
function signupUsersManually(address _user) public onlyAdmin {
    require(signups[_user].userAddress == address(0));
    signups[_user] = User(_user,now);
    userSignupCount++;
    
    E_Signup(msg.sender,now);
}
```

De plus, les utilisateurs peuvent se retirer de l'Airdrop Central pour cesser de recevoir des tokens. Cela les empêche également de pouvoir retirer les tokens en attente. En fait, ils les perdront, ils devraient donc y réfléchir à deux fois avant de le faire.

#### Airdrop de tokens

Une fois qu'une équipe a fait approuver ses tokens par l'administrateur de l'Airdrop Central, elle peut effectuer autant d'airdrops qu'elle le souhaite pour ce token.

Tout d'abord, ils doivent donner une autorisation des tokens qu'ils souhaitent distribuer au contrat Airdrop Central. Pour ce faire, ils doivent appeler la fonction approve() sur le token, en spécifiant combien de tokens ils souhaitent permettre à l'Airdrop Central d'utiliser.

Une fois que cela est fait, ils peuvent effectuer l'airdrop en appelant la fonction suivante :

```
function airdropTokens(address _tokenAddress, uint _totalTokensToDistribute, uint _expirationTime) public ifNotPaused {
    require(tokenWhitelist[_tokenAddress]);
    require(!airdropperBlacklist[msg.sender]);
    
    ERC20Basic token = ERC20Basic(_tokenAddress);
    require(token.balanceOf(msg.sender) >= _totalTokensToDistribute);
    
    // Multiplier le nombre saisi par les décimales du token.
    _totalTokensToDistribute = _totalTokensToDistribute.mul(10 ** uint256(token.decimals()));
    
    // Calculer les tokens du propriétaire et les tokens à airdrop
    uint tokensForOwner = _totalTokensToDistribute.mul(ownersCut).div(100);
    _totalTokensToDistribute = _totalTokensToDistribute.sub(tokensForOwner);
    
    // Stocker l'ID unique de l'airdrop dans le tableau (adresse du token + ID)
    TokenAirdropID memory taid = TokenAirdropID(_tokenAddress,airdroppedTokens[_tokenAddress].length);
    TokenAirdrop memory ta = TokenAirdrop(_tokenAddress,airdroppedTokens[_tokenAddress].length,msg.sender,now,now+_expirationTime,_totalTokensToDistribute,_totalTokensToDistribute,userSignupCount);
    airdroppedTokens[_tokenAddress].push(ta);
    airdrops.push(taid);
    
    // Transférer les tokens
    require(token.transferFrom(msg.sender,this,_totalTokensToDistribute));
    require(token.transferFrom(msg.sender,owner,tokensForOwner));
    
    E_AirdropSubmitted(_tokenAddress,ta.tokenOwner,ta.totalDropped,ta.airdropDate,ta.airdropExpirationDate);
```

```
}
```

La fonction airdropTokens() stocke les tokens que le contrat était autorisé à utiliser dans son solde interne. 2 % d'entre eux sont transférés au propriétaire du contrat et le reste est transféré au contrat. Il peut ensuite les distribuer parmi les utilisateurs qui étaient abonnés jusqu'à ce moment-là.

L'équipe qui a effectué l'airdrop peut également récupérer les tokens qui restent non réclamés après la date d'expiration de chaque airdrop en appelant cette fonction :

```
function returnTokensToAirdropper(address _tokenAddress) public ifNotPaused {
    require(tokenWhitelist[_tokenAddress]); // Le token doit être sur la liste blanche d'abord
    
    // Obtenir le token
    ERC20Basic token = ERC20Basic(_tokenAddress);
    
    uint tokensToReturn = 0;
    for (uint i =0; i<airdroppedTokens[_tokenAddress].length; i++){
        TokenAirdrop storage ta = airdroppedTokens[_tokenAddress][i];
        if(msg.sender == ta.tokenOwner &&
            airdropHasExpired(_tokenAddress,i)){
            tokensToReturn = tokensToReturn.add(ta.tokenBalance);
            ta.tokenBalance = 0;
        }
    }
    require(token.transfer(msg.sender,tokensToReturn));
    E_TokensWithdrawn(_tokenAddress,msg.sender,tokensToReturn,now);
```

```
}
```

#### Retrait des tokens

La dernière chose que nous devons aborder est le processus par lequel les utilisateurs retirent les tokens qui leur ont été envoyés. Pour ce faire, ils doivent appeler la fonction `withdrawTokens(address _tokenAddress)`. La fonction passera en revue tous les airdrops actifs (non encore expirés ou gelés) du token spécifié et les transférera.

```
function withdrawTokens(address _tokenAddress) ifNotPaused public {
    require(tokenWhitelist[_tokenAddress]); // Le token doit être sur la liste blanche d'abord
    
    // Obtenir l'instance de l'utilisateur, étant donné le compte de l'expéditeur
    User storage user = signups[msg.sender];
    require(user.userAddress != address(0));
    
    uint totalTokensToTransfer = 0;
    // Pour chaque airdrop effectué pour ce token (le propriétaire du token peut avoir effectué plusieurs airdrops à un moment donné)
    for (uint i =0; i<airdroppedTokens[_tokenAddress].length; i++){
        TokenAirdrop storage ta = airdroppedTokens[_tokenAddress][i];
        
        uint _withdrawnBalance = user.withdrawnBalances[_tokenAddress][i];
        // Vérifier que l'utilisateur s'est inscrit avant que l'airdrop ne soit effectué. Si c'est le cas, il a droit aux tokens
        // Et l'airdrop ne doit pas avoir expiré
        if(ta.airdropDate >= user.signupDate &&
            now <= ta.airdropExpirationDate){
            // L'utilisateur recevra une partie des tokens totaux airdroppés,
            // divisée par les utilisateurs au moment où l'airdrop a été créé
            uint tokensToTransfer = ta.totalDropped.div(ta.usersAtDate);
            // si l'utilisateur n'a pas déjà retiré les tokens
            if(_withdrawnBalance < tokensToTransfer){
                // Enregistrer les tokens retirés par l'utilisateur et les tokens totaux retirés
                user.withdrawnBalances[_tokenAddress][i] = tokensToTransfer;
                ta.tokenBalance = ta.tokenBalance.sub(tokensToTransfer);
                totalTokensToTransfer = totalTokensToTransfer.add(tokensToTransfer);
            }
        }
    }
    // Obtenir le token
    ERC20Basic token = ERC20Basic(_tokenAddress);
    // Transférer les tokens de tous les airdrops qui correspondent à cet utilisateur
    require(token.transfer(msg.sender,totalTokensToTransfer));
    
    E_TokensWithdrawn(_tokenAddress,msg.sender,totalTokensToTransfer,now);
}
```

#### Prochaines étapes

L'une des nombreuses choses que j'aimerais faire ensuite est de construire une interface web (une dapp) qui permet aux gens de voir les derniers airdrops et ceux à venir et de s'y abonner.

Si vous faites partie d'une équipe avec un token ERC20 actif, ou si vous prévoyez d'en lancer un et que vous souhaitez utiliser l'Airdrop Central pour faire un airdrop, envoyez-moi un message. Sinon, tout retour et toute suggestion sont grandement appréciés.

J'espère que vous avez apprécié la lecture de cet article autant que j'ai apprécié l'écrire. Je prends actuellement des missions de conseil liées au développement de contrats intelligents. Si vous prévoyez de lever des fonds via une ICO ou de construire un produit basé sur la Blockchain, n'hésitez pas à me contacter.