---
title: Comment ajouter la prise en charge des cartes-cadeaux sur vos dapps basées
  sur Ethereum
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-12-28T13:21:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-support-for-gift-cards-on-your-ethereum-based-dapps-6389959265ba
coverImage: https://cdn-media-1.freecodecamp.org/images/1*i0MghtjGDTM7j0Wlaj9JfA.jpeg
tags:
- name: Blockchain
  slug: blockchain
- name: General Programming
  slug: programming
- name: software development
  slug: software-development
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment ajouter la prise en charge des cartes-cadeaux sur vos dapps basées
  sur Ethereum
seo_desc: 'By Pablo Ruiz

  Ahhh, Christmas… That magical time of the year where you have to buy presents for
  all your loved ones and you don’t know what to get them…

  Gift Cards are the perfect option for those who don’t know what to buy for someone
  for the Holida...'
---

Par Pablo Ruiz

Ahhh, Noël… Cette période magique de l'année où vous devez acheter des cadeaux pour tous vos proches et vous ne savez pas quoi leur offrir…

Les cartes-cadeaux sont l'option parfaite pour ceux qui ne savent pas quoi acheter pour quelqu'un pendant les fêtes, leur anniversaire ou une autre occasion spéciale.

Faire en sorte que votre boutique accepte les cartes-cadeaux offre une très bonne façon de stimuler les ventes et permet réellement des achats en chaîne « au nom » de quelqu'un d'autre.

Vous ne savez pas quels Cryptokitties acheter pour vos proches ? Pourquoi ne pas leur offrir une carte-cadeau et les laisser acheter ceux qu'ils veulent vraiment ? (_Bien sûr, cela ne fonctionnerait pas directement car les contrats intelligents Cryptokitties devraient être modifiés pour accepter les cartes-cadeaux._ 🤔)

Dans cet article, je vais expliquer comment émettre des cartes-cadeaux en chaîne et comment les accepter dans vos propres contrats intelligents/dapps. Pour cela, nous allons créer un contrat intelligent GiftCardIssuer que vos propres contrats intelligents pourront hériter pour travailler avec des cartes-cadeaux.

### Comment fonctionnent les cartes-cadeaux

L'idée derrière ce contrat intelligent est de fournir la logique nécessaire à vos propres contrats qui reçoivent des paiements afin qu'ils puissent accepter une carte-cadeau avec un solde prépayé au lieu de « cash ».

N'importe qui pourrait émettre une nouvelle carte-cadeau qui n'est valable que pour les achats sur votre contrat intelligent, et uniquement valable pour la personne que le compte émetteur choisit comme bénéficiaire.

Émettre une carte-cadeau dans une boutique compatible serait très facile et simple. Le compte souhaitant offrir une carte-cadeau doit simplement appeler la fonction correspondante sur votre contrat intelligent, fournir un identifiant pour la carte, sélectionner le compte bénéficiaire et payer pour celle-ci.

Notre contrat intelligent GiftCardIssuer générera ensuite la carte-cadeau selon les paramètres et les règles commerciales que nous avons prédéfinis. Par exemple, nous pouvons faire en sorte que les cartes-cadeaux générées par nos contrats intelligents n'acceptent qu'un montant minimum de financement à fournir, ou nous pourrions les rendre rechargeables.

### Développement du contrat intelligent GiftCardIssuer

Vous pouvez consulter le code complet, entièrement commenté et l'exemple d'implémentation sur mon [dépôt Github](https://github.com/pabloruiz55/GiftCardIssuer).

Dans les paragraphes suivants, je vais passer en revue les aspects les plus importants du contrat intelligent GiftCardIssuer.

#### Structure d'une carte-cadeau

Voici à quoi ressemblerait une carte-cadeau émise par nos contrats intelligents :

```
struct Card {
    uint value;
    uint issueDate;
    uint validThru;
    address beneficiary;
    address generatedBy;
    bool rechargeable;
    bool transfereable;
}
```

La structure ci-dessus définit les propriétés de base des cartes-cadeaux que nous allons émettre, et nous aide à définir et à appliquer les règles commerciales que nous définissons pour elles plus tard.

#### Définition des règles commerciales pour les cartes-cadeaux

Les cartes-cadeaux que nous créons auront certaines règles commerciales codées en elles. Voici les règles que j'ai définies, mais d'autres pourraient être ajoutées en fonction des besoins de la boutique :

```
// Variables des règles commerciales des cartes
uint public rule_Duration = 365 days;
bool public rule_Rechargeable = false;
uint public rule_MinValue = 1 wei;
uint public rule_MaxValue = 100 ether;
bool public rule_Transfereable = true;
```

* `**rule_Duration**` définit la date d'expiration de la carte-cadeau
* `**rule_Rechargeable**` définit si des fonds peuvent être ajoutés à la carte ou non
* `**rule_Transfereable**` définit si la carte peut être donnée à quelqu'un d'autre une fois émise
* `**rule_MinValue**` et `**rule_MaxValue**` définissent le financement minimum et maximum que l'émetteur peut ajouter à la carte

Ces règles commerciales peuvent être modifiées à la volée par le propriétaire de la boutique en utilisant la fonction `**setGiftCardRules()**`, mais gardez à l'esprit que les modifications **ne s'appliquent** qu'aux nouvelles cartes-cadeaux émises. Les cartes déjà émises conserveront les règles avec lesquelles elles ont été émises.

```
function setGiftCardRules(
    bool _rechargeable,
    bool _transfereable,
    uint _duration,
    uint _minValue,
    uint _maxValue
) public {
    require(msg.sender == owner);
    require(duration >= 1 days);
    require(_minValue > 0);
    require(_maxValue >= _minValue);

    rule_Rechargeable = _rechargeable;
    rule_Transfereable = _transfereable;
    rule_Duration = _duration;
    rule_MinValue = _minValue;
    rule_MaxValue = _maxValue;
}
```

#### Émission d'une nouvelle carte-cadeau

Les utilisateurs peuvent émettre de nouvelles cartes-cadeaux en appelant la fonction **payable** `**issueGiftCard()**` qui prend 2 paramètres :

* `**_cardId**` : qui est une chaîne de 32 octets **unique** au choix de l'émetteur (ils pourraient créer une carte dont l'identifiant est « JOYEUX ANNIVERSAIRE, JEAN ! »)
* `**_beneficiary**` : qui est le compte qui pourra utiliser la carte-cadeau émise.

Lorsque la fonction est exécutée, une nouvelle carte-cadeau sera émise (avec les règles commerciales précédemment définies) au nom du bénéficiaire et avec les fonds envoyés avec l'appel de la fonction.

```
function issueGiftCard(bytes32 _cardId, address _beneficiary) public payable {
    require(msg.value > 0);
    require(cards[_cardId].issueDate == 0);
    require(msg.value >= rule_MinValue);
    require(msg.value <= rule_MaxValue);

    cards[_cardId].value = msg.value;
    cards[_cardId].beneficiary = _beneficiary;
    cards[_cardId].generatedBy = msg.sender;
    cards[_cardId].issueDate = now;
    cards[_cardId].validThru = now + rule_Duration;
    cards[_cardId].rechargeable = rule_Rechargeable;
    cards[_cardId].transfereable = rule_Transfereable;

    // ajouter de la valeur au solde du commerçant
    balance += msg.value;

    E_GiftCardIssued(_cardId, now, msg.sender, _beneficiary, msg.value);
}
```

#### Traitement des cartes-cadeaux

Pour accepter un paiement par carte-cadeau, le contrat intelligent de la boutique devrait implémenter une fonction qui appelle la fonction `**useGiftCard()**` de GiftCardIssuer :

```
function useGiftCard(bytes32 _cardId, uint _prodPrice) public returns (bool) {
    // La carte-cadeau ne peut être utilisée que par le compte auquel elle a été émise
    require(msg.sender == cards[_cardId].beneficiary);
    // la carte doit exister
    require(cards[_cardId].issueDate > 0);
    // La carte ne doit pas avoir expiré
    require(now <= cards[_cardId].validThru);
    // La carte doit avoir suffisamment de fonds pour couvrir l'achat
    require(cards[_cardId].value >= _prodPrice);
    // retirer la valeur du solde de la carte
    cards[_cardId].value -= _prodPrice;

    E_GiftCardUsed(_cardId, now, cards[_cardId].beneficiary, _prodPrice);
    return (true);
}
```

La fonction ci-dessus serait appelée depuis le contrat intelligent de la boutique (qui hérite de GiftCardIssuer) comme ceci :

```
function buyWithGiftCard(bytes32 _cardId) public {
    // Essayer d'acheter le produit avec la carte-cadeau fournie
    require(useGiftCard(_cardId, itemPrice));

    itemsBought[msg.sender]++;
}
```

`**buyWithGiftCard()**` accepte un `_cardId` et appelle sa fonction `useGiftCard` en passant le `_cardId` et `itemPrice`. C'est le prix du produit qui sera acheté (et représente combien d'ether nous allons soustraire du solde de la carte-cadeau).

`**useGiftCard()**` procède à la vérification que la carte-cadeau est valide et, si c'est le cas, soustrait le solde et accepte le paiement. Si la carte-cadeau n'est pas valide ou n'a pas suffisamment de fonds, la fonction échouera et toute la transaction échouera.

#### Accepter les paiements avec des cartes-cadeaux

Voici un exemple d'implémentation d'un contrat intelligent de boutique extrêmement simple qui accepte à la fois l'ether ou les cartes-cadeaux :

```
contract Store is GiftCardIssuer {
    uint itemPrice = 1 ether;
    mapping(address => uint) public itemsBought;

    function buyWithGiftCard(bytes32 _cardId) public {
        // Essayer d'acheter le produit avec la carte-cadeau fournie
        require(useGiftCard(_cardId, itemPrice));

        itemsBought[msg.sender]++;
    }

    function buyWithEther() public payable {
        require(msg.value == itemPrice);

        itemsBought[msg.sender]++;
    }
}
```

Un contrat intelligent souhaitant émettre des cartes-cadeaux et les accepter au lieu de l'ether devrait simplement hériter du contrat de base GiftCardIssuer et appeler correctement `**require(useGiftCard(_cardId, itemPrice));**`.

#### Recharger et transférer les cartes-cadeaux

Comme défini dans la section des règles commerciales des cartes-cadeaux, nous pouvons configurer les cartes-cadeaux pour qu'elles soient « rechargeables » et/ou « transférables ».

**Une carte-cadeau transférable** peut être donnée à un autre compte par le compte actuellement défini comme bénéficiaire. Tout ce qu'ils ont à faire est d'appeler la fonction suivante (tant que les règles de la carte-cadeau le permettent) :

```
function transferGiftCardTo(bytes32 _cardId, address _newBeneficiary) public {
    require(msg.sender == cards[_cardId].beneficiary);
    require(cards[_cardId].transfereable);
    require(cards[_cardId].issueDate > 0);
    require(_newBeneficiary != address(0));

    cards[_cardId].beneficiary = _newBeneficiary;
}
```

Une carte-cadeau rechargeable peut avoir des fonds ajoutés. N'importe qui peut appeler la fonction suivante pour ajouter des fonds à une carte-cadeau existante (tant que les règles de la carte-cadeau le permettent) :

```
function addFundsToGiftCard(bytes32 _cardId) public payable {
    require(cards[_cardId].rechargeable);
    require(msg.value > 0);
    require(cards[_cardId].issueDate > 0);
    require(msg.value >= rule_MinValue);
    require(msg.value <= rule_MaxValue);

    cards[_cardId].value += msg.value;
    cards[_cardId].validThru = now + rule_Duration; // Étendre la durée

    // ajouter de la valeur au solde du commerçant
    balance += msg.value;
}
```

### Joyeux don de cadeaux !

Il y a beaucoup de nouvelles règles et propriétés qui pourraient être ajoutées aux cartes-cadeaux. Il y a aussi la possibilité de créer un émetteur universel de cartes-cadeaux qui génère des cartes-cadeaux non seulement valables dans une boutique, mais dans n'importe quelle boutique faisant partie du réseau de l'émetteur.

_Je espère que vous avez apprécié la lecture de cet article autant que j'ai apprécié l'écrire. Je prends actuellement des missions de conseil liées au développement de contrats intelligents. Si vous prévoyez de lever des fonds via un ICO ou de construire un produit basé sur la Blockchain, n'hésitez pas à me contacter._