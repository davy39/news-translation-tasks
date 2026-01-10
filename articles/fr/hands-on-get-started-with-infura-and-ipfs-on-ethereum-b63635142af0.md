---
title: 'Pratique : Commencez avec Infura et l''IPFS sur Ethereum'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-07-28T17:14:14.000Z'
originalURL: https://freecodecamp.org/news/hands-on-get-started-with-infura-and-ipfs-on-ethereum-b63635142af0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*cQNpUgQlMS2Almmpav-_Xg.png
tags:
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: 'Pratique : Commencez avec Infura et l''IPFS sur Ethereum'
seo_desc: 'By Niharika Singh

  Why Infura?

  There are a lot of pain points being faced by blockchain which may be solved by
  Infura and/or the InterPlanetary File System (IPFS), to some extent. These are the
  main challenges:


  It’s expensive to store data on the Eth...'
---

Par Niharika Singh

### Pourquoi Infura ?

Il y a beaucoup de points douloureux rencontrés par la blockchain qui peuvent être résolus par Infura et/ou le InterPlanetary File System (IPFS), dans une certaine mesure. Voici les principaux défis :

1. Il est coûteux de stocker des données sur la blockchain Ethereum
2. Il est difficile de configurer un client Ethereum geth
3. Il est difficile de mettre à l'échelle l'infrastructure

Si vous utilisez Infura, l'accès au réseau Ethereum et à l'IPFS devient beaucoup plus rapide. Cela ne prend plus des heures pour synchroniser le client geth qui utilise une énorme quantité de mémoire et de bande passante pendant que toute la blockchain est téléchargée.

Voici quelques autres avantages qui viennent avec l'utilisation d'Infura :

* De grandes quantités de données peuvent être stockées sur l'IPFS, et seul le hash du fichier peut être stocké sur Ethereum.
* Infura fournit des API sécurisées, fiables, scalables et faciles à utiliser pour accéder au réseau Ethereum et à l'IPFS. Les développeurs n'ont pas à se soucier de l'infrastructure d'un nœud Ethereum ou d'un nœud IPFS. Cela est pris en charge par Infura.
* Infura fournit des endpoints publics avec TLS activé.
* Le code est portable sur l'interface d'Ethereum en utilisant JSON RPC, Web3.
* Infura est pratiquement le couteau suisse du développeur, et sauve également l'équipe de déploiement de l'enfer des problèmes de scalabilité.

![Image](https://cdn-media-1.freecodecamp.org/images/y8iwhXpRkRt2PGMowxrJ7p8UY8PXSdhy-Sjc)

![Image](https://cdn-media-1.freecodecamp.org/images/GS-bzDc0-YSK4Ut4mryw7AjVcYL3UUF2IJB5)

* Et enfin, Infura est de confiance :

![Image](https://cdn-media-1.freecodecamp.org/images/nWAllpEFkm1FUmv0KIYZAPEW9sEanL0oQbvB)

### Description de la dApp

Notre dApp prendra un fichier en entrée d'un utilisateur et le téléchargera sur l'IPFS en invoquant un contrat Ethereum. Le hash du fichier sera stocké sur Ethereum.

Voici le processus que nous allons suivre :

1. Prendre un fichier en entrée
2. Convertir le fichier en buffer
3. Télécharger le buffer sur IPFS
4. Stocker le hash du fichier retourné par IPFS
5. Obtenir l'adresse Ethereum de l'utilisateur via Metamask
6. L'utilisateur confirme la transaction vers Ethereum via Metamask
7. Le hash IPFS est écrit sur Ethereum

![Image](https://cdn-media-1.freecodecamp.org/images/iO9rRzyMkmjnJABUKCkFMbVvByzCUh7HWPXZ)
_Architecture de la dApp_

### Pile technologique impliquée

* [React](https://reactjs.org/) — Bibliothèque front-end
* [Solidity](https://solidity.readthedocs.io/en/develop/) — Le langage utilisé pour construire des contrats intelligents qui s'exécutent sur Ethereum
* [IPFS](https://ipfs.io/) — Stockage décentralisé
* [Infura](https://infura.io) — Accès API au réseau Ethereum et IPFS

### Codons !

> _Assurez-vous d'avoir déjà téléchargé Metamask. Si ce n'est pas le cas, téléchargez-le depuis [ici](https://metamask.io/)._

> _Assurez-vous également que votre Node et NPM sont à jour._

#### **Installez les dépendances suivantes :**

```
$ npm i -g create-react-app
$ npm install react-bootstrap
$ npm install fs-extra
$ npm install ipfs-api
$ npm install web3
```

Une fois terminé, exécutez la commande suivante sur votre CLI pour créer un projet React exemple. Je vais nommer mon projet **ipfs**.

```
$ create-react-app ipfs
```

#### **Déployez le contrat intelligent sur le réseau de test Ropsten**

Assurez-vous d'être sur le réseau de test Ropsten dans Metamask.

Pour déployer le contrat intelligent, nous avons besoin d'ether. Pour obtenir de l'ether pour le réseau de test Ropsten, allez sur [https://faucet.metamask.io/](https://faucet.metamask.io/).

Pour déployer le contrat intelligent, allez sur [https://remix.ethereum.org](https://remix.ethereum.org).

```
pragma solidity ^0.4.17;
```

```
contract Contract {
  string ipfsHash;
  function setHash(string x) public {
    ipfsHash = x;
  }
  function getHash() public view returns (string x) {
    return ipfsHash;
  }
```

```
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/agAOGfoOvoQfYAqSDGqH94y4Lw1KoYHdrF4d)

Enregistrez l'adresse du contrat intelligent. La mienne est : 0x610DD75057738B73e3F17A9D607dB16A44f962F1

Enregistrez également l'Interface Binaire d'Application (ABI) en JSON. Elle peut être trouvée dans l'onglet "compile", sous "details".

La mienne est la suivante :

```
[ {
  "constant": false,
  "inputs": [
    {
      "name": "x",
      "type": "string"
    }
  ],
  "name": "sendHash",
  "outputs": [],
  "payable": false,
  "stateMutability": "nonpayable",
  "type": "function"
},
{
  "constant": true,
  "inputs": [],
  "name": "getHash",
  "outputs": [
    {
      "name": "x",
      "type": "string"
    }
  ],
  "payable": false,
  "stateMutability": "view",
  "type": "function"
}
]
```

Dans le répertoire "ipfs/src", créez les fichiers suivants : **web3.js**, **ipfs.js**, et **storehash.js**.

#### Fichier 1 — Web3.js

```
import Web3 from 'web3';
```

```
const web3 = new Web3(window.web3.currentProvider);
```

```
export default web3;
```

#### Fichier 2 — Storehash.js

```
import web3 from './web3';
```

```
//Votre adresse de contrat
const address = '0x610dd75057738b73e3f17a9d607db16a44f962f1';
```

```
//Votre ABI de contrat
const abi = [
  {
    "constant": false,
    "inputs": [
      {
        "name": "x",
        "type": "string"
      }
    ],
    "name": "sendHash",
    "outputs": [],
    "payable": false,
    "stateMutability": "nonpayable",
    "type": "function"
  },
  {
    "constant": true,
    "inputs": [],
    "name": "getHash",
    "outputs": [
      {
        "name": "x",
        "type": "string"
      }
    ],
    "payable": false,
    "stateMutability": "view",
    "type": "function"
  }
]
```

```
export default new web3.eth.Contract(abi, address);
```

#### Fichier 3 — Ipfs.js

```
const IPFS = require('ipfs-api');
const ipfs = new IPFS({ host: 'ipfs.infura.io', port: 5001, protocol: 'https' });
```

```
export default ipfs;
```

#### Édition — Index.js

```
import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import App from './App';
import registerServiceWorker from './registerServiceWorker';
import 'bootstrap/dist/css/bootstrap.min.css';
```

```
ReactDOM.render(<App />, document.getElementById('root'));
registerServiceWorker();
```

#### Fichier 4 — App.js

```
import React, { Component } from 'react';
import web3 from './web3';
import ipfs from './ipfs';
import storehash from './storehash';
import { Button } from 'reactstrap';
```

```
class App extends Component {
```

```
state = {
  ipfsHash:null,
  buffer:'',
  ethAddress:'',
  transactionHash:'',
  txReceipt: ''
};
```

```
//Prendre le fichier en entrée de l'utilisateur
captureFile =(event) => {
  event.stopPropagation()
  event.preventDefault()
  const file = event.target.files[0]
  let reader = new window.FileReader()
  reader.readAsArrayBuffer(file)
  reader.onloadend = () => this.convertToBuffer(reader)
};
```

```
//Convertir le fichier en buffer pour le stocker sur IPFS
convertToBuffer = async(reader) => {
  //le fichier est converti en buffer pour le téléchargement sur IPFS
  const buffer = await Buffer.from(reader.result);
  //définir ce buffer en utilisant la syntaxe es6
  this.setState({buffer});
};
```

```
//Fonction asynchrone ES6
onClick = async () => {
  try{
    this.setState({blockNumber:"waiting.."});
    this.setState({gasUsed:"waiting..."});

    await web3.eth.getTransactionReceipt(this.state.transactionHash, (err, txReceipt)=>{
      console.log(err,txReceipt);
      this.setState({txReceipt});
    });
  }catch(error){
    console.log(error);
  }
}
```

```
onSubmit = async (event) => {
  event.preventDefault();
```

```
//apporter l'adresse du compte metamask de l'utilisateur
const accounts = await web3.eth.getAccounts();
//obtenir l'adresse du contrat depuis storehash.js
const ethAddress= await storehash.options.address;
this.setState({ethAddress});
//sauvegarder le document sur IPFS, retourner son hash#, et définir le hash# à l'état
await ipfs.add(this.state.buffer, (err, ipfsHash) => {
  console.log(err,ipfsHash);
  //définir l'état en définissant ipfsHash à ipfsHash[0].hash
  this.setState({ ipfsHash:ipfsHash[0].hash });
  //appeler la méthode du contrat Ethereum "sendHash" et .send le hash IPFS au contrat ethereum
  //retourner le hash de transaction du contrat ethereum
  storehash.methods.sendHash(this.state.ipfsHash).send({
    from: accounts[0]
  }, (error, transactionHash) => {
    console.log(transactionHash);
    this.setState({transactionHash});
  });
})
};
```

```
render() {
```

```
return (
  <div className="App">
    <header className="App-header">
      <h1>Ethereum et IPFS utilisant Infura</h1>
    </header>
```

```
<hr/><grid>
  <h3> Choisissez le fichier à envoyer à IPFS </h3>
  <form onSubmit={this.onSubmit}>
    <input
      type = "file"
      onChange = {this.captureFile}
    />
    <Button
      bsStyle="primary"
      type="submit">
      Envoyez-le
    </Button>
  </form>
  <hr/> 
  <Button onClick = {this.onClick}> Obtenir le reçu de transaction </Button> 
  <hr/> 
  <table bordered responsive>
    <thead>
      <tr>
        <th>Catégorie de reçu de transaction</th>
        <th> </th>
        <th>Valeurs</th>
      </tr>
    </thead>
```

```
<tbody>
  <tr>
    <td>Hash IPFS stocké sur Ethereum</td>
    <td> : </td>
    <td>{this.state.ipfsHash}</td>
  </tr>
  <tr>
    <td>Adresse du contrat Ethereum</td>
    <td> : </td>
    <td>{this.state.ethAddress}</td>
  </tr>
  <tr>
    <td>Tx # </td>
    <td> : </td>
    <td>{this.state.transactionHash}</td>
  </tr>
</tbody>
</table>
</grid>
</div>
);
}
}
export default App;
```

**Et c'est tout !**

Accédez à votre dApp sur localhost:3000. Téléchargez un fichier et vous verrez un hash généré. Pour vous assurer que votre fichier est téléchargé, accédez-y via la passerelle IPFS. Assurez-vous d'accepter les demandes de Metamask.

![Image](https://cdn-media-1.freecodecamp.org/images/gsZvutm3tRljA5j6vS4MygjSlmfnQ072vBO6)

![Image](https://cdn-media-1.freecodecamp.org/images/4KoRXxzXfal5sHgZyDbbP8pZ8xodGPSMeaK6)

Accédez à votre fichier à l'adresse : https://gateway.ipfs.io/ipfs/votre hash IPFS

Le mien est à l'adresse : [https://gateway.ipfs.io/ipfs/QmbyizSHLirDfZhms75tdrrdiVkaxKvbcLpXzjB5k34a31](https://gateway.ipfs.io/ipfs/QmbyizSHLirDfZhms75tdrrdiVkaxKvbcLpXzjB5k34a31)

Pour en savoir plus sur l'IPFS, consultez mes autres articles :

[**Apprendre en faisant : une introduction agréable et facile au Inter Planetary File System**](https://medium.freecodecamp.org/ipfs-101-understand-by-doing-it-9f5622c4d4ed)
[_Primer on IPFS_medium.freecodecamp.org](https://medium.freecodecamp.org/ipfs-101-understand-by-doing-it-9f5622c4d4ed)
[**IPFS ? et Merkle Forest ?**](https://hackernoon.com/ipfs-and-merkle-forest-a6b7f15f3537)
[**W**h_at is IPFS?ha_ckernoon.com](https://hackernoon.com/ipfs-and-merkle-forest-a6b7f15f3537)

#### Merci d'avoir lu. Si vous avez aimé cela, applaudissez ! Suivez-moi sur Twitter [@](https://www.freecodecamp.org/news/hands-on-get-started-with-infura-and-ipfs-on-ethereum-b63635142af0/undefined)Niharika3297