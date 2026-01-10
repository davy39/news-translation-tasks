---
title: Comment fonctionne le bitcoin ? J'ai créé une application pour vous le montrer.
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-22T16:52:01.000Z'
originalURL: https://freecodecamp.org/news/how-does-bitcoin-work-i-built-an-app-to-show-you-f9fcd50bdd0d
coverImage: https://cdn-media-1.freecodecamp.org/images/1*M9e2wG1vsgiZqyhtAm-bkw.png
tags:
- name: Apps
  slug: apps-tag
- name: Bitcoin
  slug: bitcoin
- name: Blockchain
  slug: blockchain
- name: Cryptocurrency
  slug: cryptocurrency
- name: data
  slug: data
seo_title: Comment fonctionne le bitcoin ? J'ai créé une application pour vous le
  montrer.
seo_desc: 'By Sean Han

  As Bitcoin rose to unprecedented levels, it caught my attention & curiosity. I wondered,
  how does bitcoin really work?

  As I went down the blockchain rabbit hole, I found that many resources rarely go
  beyond the “revolutionary”, “distribut...'
---

Par Sean Han

Alors que le Bitcoin atteignait des niveaux sans précédent, il a attiré mon attention et ma curiosité. Je me suis demandé : comment fonctionne **réellement** le bitcoin ?

En m'enfonçant dans le terrier du lapin de la blockchain, j'ai constaté que de nombreuses ressources dépassent rarement le discours sur le côté « révolutionnaire », « distribué » et « immuable ». Beaucoup parlent du *quoi*, mais pas tellement du *pourquoi* et du *comment*.

J'ai eu recours à la lecture de documents techniques et du code source pour découvrir cette boîte noire. J'ai commencé à partager ce que j'ai appris en créant des [apps](https://www.producthunt.com/@seanhan/submitted) qui démontraient le fonctionnement interne de la blockchain.

Ce que j'ai réalisé, c'est que le bitcoin n'était que la blockchain + des transactions. Cet article couvrira la partie transactions de l'équation. Si vous souhaitez un rappel sur la blockchain, consultez [Blockchain Demo](https://blockchaindemo.io) ou cet [article](https://medium.freecodecamp.org/how-does-blockchain-really-work-i-built-an-app-to-show-you-6b70cd4caf7d).

Un bloc sur la blockchain se compose des parties suivantes :

![Image](https://cdn-media-1.freecodecamp.org/images/3xihokAJ-UV7oTKZyhWJjcsfR3TELOf9Hngu)
_Un bloc sur la blockchain — [https://blockchaindemo.io](https://blockchaindemo.io" rel="noopener" target="_blank" title=")_

* **Index** (Bloc #1)**:** De quel bloc s'agit-il ?
* **Hash** (#00001834d29f33…)**:** Le bloc est-il valide ?
* **Previous Hash** (#000dc75…)**:** Le bloc précédent est-il valide ?
* **Timestamp** (Mar, 19 Déc 2017 …)**:** Quand le bloc a-t-il été ajouté ?
* **Data** (I ❤️ freeCodeCamp)**:** Quelles informations sont stockées sur le bloc ?
* **Nonce** (1263)**:** Combien d'itérations avons-nous effectuées avant de trouver un bloc valide ?

Au lieu d'avoir du **texte** (I ❤️ freeCodeCamp) comme données, les cryptomonnaies ont des **transactions** comme données.

### Qu'est-ce qu'une transaction ?

Les transactions sont un enregistrement de paiement entre deux parties. Lorsqu'il y a un échange de valeur, une transaction est créée pour l'enregistrer.

Par exemple, disons que Satoshi possède 100 pièces.

Il veut payer 5 pièces à Dean, avec des frais de minage de 1 pièce. Il utilise les 100 pièces qu'il possède pour effectuer la transaction. Il s'attend à récupérer 94 pièces en monnaie de retour.

Lorsque Satoshi mine un nouveau bloc avec la transaction ci-dessus, il est récompensé par 100 nouvelles pièces.

L'exemple ci-dessus créera les **outputs** (sorties) de transaction suivants (qui seront expliquées) :

![Image](https://cdn-media-1.freecodecamp.org/images/0wM7d2vfFKsrniUQ5epFSS1w1seZFXG4ohxY)
_Outputs de transaction — [http://coindemo.io](http://coindemo.io" rel="noopener" target="_blank" title=")_

Puisque les 100 pièces initiales que Satoshi possédait ont été utilisées comme **input** (entrée) pour créer la transaction ci-dessus, les 100 pièces initiales sont maintenant **dépensées**. (à expliquer)

![Image](https://cdn-media-1.freecodecamp.org/images/Wgm2it0MNwmwF5cbmkAudnERrdAlDiXr6BVv)
_Output de transaction dépensé — [http://coindemo.io](http://coindemo.io" rel="noopener" target="_blank" title=")_

Les concepts ci-dessus seront expliqués ensuite.

### Trois types de transactions :

1. **Reward** — Satoshi est récompensé par 100 pièces pour avoir miné un nouveau bloc
2. **Regular** — Satoshi a payé 5 pièces à Dean avec un rendu de monnaie de 94 pièces
3. **Fee** — Frais de minage de 1 pour celui qui mine la transaction (Satoshi dans l'exemple ci-dessus)

### Transaction

Une transaction se compose de quatre parties :

1. Inputs — **D'où vient la valeur**
2. Outputs — **Où va la valeur**
3. Hash — Identifie de manière unique la transaction (en utilisant les inputs et les outputs)
4. Type — Reward, Regular ou Fee

### Outputs — Où va la valeur

Un output a deux parties :

1. Address — Quelle est l'adresse publique du portefeuille vers laquelle envoyer les pièces ?
2. Amount — Combien de pièces ?

### Inputs — D'où vient la valeur

Un input **doit provenir d'un output précédent**. Cependant, un output ne peut être utilisé comme input qu'**une seule fois**. Lorsqu'un output est utilisé, il est considéré comme **dépensé**. Les outputs qui n'ont pas été utilisés comme inputs sont **non dépensés**.

Un input a cinq parties :

1. Transaction Hash — Hash de la transaction de l'output (non dépensé)
2. Output Index — L'index de l'output (non dépensé) dans la transaction
3. Amount — Montant de l'output (non dépensé)
4. Address — Adresse de l'output (non dépensé)
5. Signature — Signée par la clé privée de l'Address

### Reward Transaction

Les transactions de type Reward sont créées suite à la découverte d'un bloc valide sur la blockchain. Par conséquent, les transactions Reward n'ont aucun input car elles créent de nouvelles pièces.

**Par exemple :** Satoshi a miné un nouveau bloc avec une récompense de minage de 100. La transaction sur le bloc ressemblera à ceci :

**Type :** Reward

**Inputs :** Aucun

**Outputs :**

* _Address :_ Adresse publique du portefeuille de Satoshi
* _Amount :_ 100 (récompense spécifiée par la cryptomonnaie)

**Hash :** ?(inputs + outputs) = 000abcdefg…

### Regular Transaction

Les transactions de type Regular sont des transactions créées lorsqu'une partie en paie une autre.

**Suite de l'exemple :** Satoshi utilise l'**output** (non dépensé) de la transaction Reward comme **input** pour payer 5 pièces à Dean. Il spécifie des frais de minage de 1 pièce.

**Type :** Regular

**Inputs :**

* _Transaction Hash :_ 000abcdefg… (hash de la transaction Reward ci-dessus)
* _Output Index :_ 0 (le premier index d'un output est 0)
* _Amount :_ 100 (montant de l'output)
* _Address :_ Adresse publique du portefeuille de Satoshi (adresse de l'output)
* _Signature :_ Satoshi signe cet input avec sa clé privée

**Outputs :**

_Output 1_ : (index 0)

* _Address_ : Adresse de Dean
* _Amount :_ 5 pièces

_Output 2_ : (index 1)

* _Address :_ Adresse de Satoshi
* _Amount :_ 94 pièces = 100 - 5 (paiement) - 1 (frais)

1. Le premier output est le **paiement** destiné à Dean.
2. Le deuxième output est la **monnaie** retournant à Satoshi.

Parce que l'output de la transaction Reward de Satoshi (de l'exemple précédent) a été utilisé comme input pour ce paiement, il est maintenant **dépensé et ne peut plus être utilisé**. Si il est réutilisé, il y a alors une [double dépense](https://en.bitcoin.it/wiki/Irreversible_Transactions).

#### Pourquoi le compte n'y est-il pas ???

Le montant total des inputs est de 100.  
Le montant total des outputs est de 5 + 94 = 99.

Dans l'exemple, Satoshi a spécifié des frais de minage de 1 pièce. _La différence entre les inputs et les outputs d'une transaction Regular constitue les **frais de minage**._

Les inputs doivent être supérieurs ou égaux aux outputs. _Si les inputs et les outputs sont égaux, alors il n'y a **pas de frais de minage**._

### Fee Transaction

_Quiconque mine la transaction Regular ci-dessus ajoutera la transaction de frais de minage (Fee)._ Parce qu'il y avait un déficit de 1 dans la transaction Regular, le montant des frais est de 1.

**Suite de l'exemple :** Bob mine la transaction de Satoshi et Dean.

Type : Fee

Inputs : Aucun

Outputs :

* _Address :_ Adresse publique du portefeuille de Bob
* _Amount :_ 1 (frais, différence entre l'input et l'output de la transaction Regular)

Parce que Bob a miné cette transaction dans le nouveau bloc, il y aura une transaction Reward de 100 pour Bob.

### Sur la blockchain :

![Image](https://cdn-media-1.freecodecamp.org/images/zj7QIcMsAcZvLjX8s-rUgg3wug1yVmmgNrrj)

![Image](https://cdn-media-1.freecodecamp.org/images/VEVo84o9jNG6d1IkdmXx3u9VARSDXZ08RN35)
_**1.** Satoshi dépense son output Reward **2.** Satoshi paie Dean **3.** Bob mine la transaction — [http://coindemo.io](http://coindemo.io" rel="noopener" target="_blank" title=")_

### Soldes finaux :

Satoshi : **94** = 100 (récompense) - 5 (paiement) - 1 (frais)  
Dean : **5** (paiement de Satoshi)  
Bob : **101** = 100 (récompense pour avoir miné un nouveau bloc avec la transaction) + 1 (frais)

**Total des devises en circulation :** **200** = 94 (Satoshi) + 5 (Dean) + 101 (Bob)

Deux blocs ont été minés, et chaque bloc a une récompense de 100, il devrait donc y avoir 200 pièces en circulation.

### **Conclusion**

Sur un nouveau bloc, **les totaux des inputs et des outputs des transactions Regular et Fee doivent être égaux**. Cela garantit que seules les transactions Reward génèrent de nouvelles pièces.

Les déficits des outputs Regular sont compensés par les outputs des transactions Fee. Ne laissant que les transactions Reward comme seul excédent d'output.

### Essayez par vous-même sur [http://coindemo.io](http://coindemo.io)

![Image](https://cdn-media-1.freecodecamp.org/images/eLhaBYWQvL7s-HqVe1n-NLfvMUomEEY7mGAj)