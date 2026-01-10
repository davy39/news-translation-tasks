---
title: '4 Modèles de Conception que Vous Devriez Connaître pour le Développement Web
  : Observer, Singleton, Stratégie et Décorateur'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-27T13:42:14.000Z'
originalURL: https://freecodecamp.org/news/4-design-patterns-to-use-in-web-development
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/design-patterns.jpg
tags:
- name: Design
  slug: design
- name: design patterns
  slug: design-patterns
- name: Web Development
  slug: web-development
seo_title: '4 Modèles de Conception que Vous Devriez Connaître pour le Développement
  Web : Observer, Singleton, Stratégie et Décorateur'
seo_desc: "By Milecia McGregor\nHave you ever been on a team where you need to start\
  \ a project from scratch? That's usually the case in many start-ups and other small\
  \ companies. \nThere are so many different programming languages, architectures,\
  \ and other concern..."
---

Par Milecia McGregor

Avez-vous déjà fait partie d'une équipe où vous devez démarrer un projet à partir de zéro ? C'est généralement le cas dans de nombreuses start-ups et autres petites entreprises. 

Il existe tant de langages de programmation, d'architectures et d'autres préoccupations différentes qu'il peut être difficile de déterminer par où commencer. C'est là que les modèles de conception entrent en jeu.

Un modèle de conception est comme un modèle pour votre projet. Il utilise certaines conventions et vous pouvez vous attendre à un type spécifique de comportement de sa part. Ces modèles ont été créés à partir des expériences de nombreux développeurs, ils sont donc vraiment comme différents ensembles de meilleures pratiques. 

Et vous et votre équipe pouvez décider quel ensemble de meilleures pratiques est le plus utile pour votre projet. En fonction du modèle de conception que vous choisissez, vous allez tous commencer à avoir des attentes quant à ce que le code devrait faire et quel vocabulaire vous allez tous utiliser.

Les modèles de conception de programmation peuvent être utilisés dans tous les langages de programmation et peuvent être adaptés à n'importe quel projet car ils ne vous donnent qu'un aperçu général d'une solution. 

Il existe 23 modèles officiels du livre _Design Patterns - Elements of Reusable Object-Oriented Software_, qui est considéré comme l'un des livres les plus influents sur la théorie orientée objet et le développement logiciel. 

Dans cet article, je vais couvrir quatre de ces modèles de conception juste pour vous donner un aperçu de ce que sont quelques-uns des modèles et quand vous les utiliseriez.

## Le Modèle de Conception Singleton

Le modèle singleton ne permet à une classe ou à un objet d'avoir qu'une seule instance et il utilise une variable globale pour stocker cette instance. Vous pouvez utiliser le chargement paresseux pour vous assurer qu'il n'y a qu'une seule instance de la classe car elle ne créera la classe que lorsque vous en aurez besoin.

Cela empêche plusieurs instances d'être actives en même temps, ce qui pourrait causer des bugs étranges. La plupart du temps, cela est implémenté dans le constructeur. Le but du modèle singleton est généralement de réguler l'état global d'une application.

Un exemple de singleton que vous utilisez probablement tout le temps est votre logger. 

Si vous travaillez avec certains des frameworks front-end comme React ou Angular, vous savez à quel point il peut être délicat de gérer les logs provenant de plusieurs composants. C'est un excellent exemple de singletons en action car vous ne voulez jamais plus d'une instance d'un objet logger, surtout si vous utilisez un outil de suivi des erreurs.

```javascript
class FoodLogger {
  constructor() {
    this.foodLog = []
  }
    
  log(order) {
    this.foodLog.push(order.foodItem)
    // faire du code sophistiqué pour envoyer ce log quelque part
  }
}

// ceci est le singleton
class FoodLoggerSingleton {
  constructor() {
    if (!FoodLoggerSingleton.instance) {
      FoodLoggerSingleton.instance = new FoodLogger()
    }
  }
  
  getFoodLoggerInstance() {
    return FoodLoggerSingleton.instance
  }
}

module.exports = FoodLoggerSingleton
```

Maintenant, vous n'avez pas à vous soucier de perdre des logs provenant de plusieurs instances car vous n'en avez qu'une dans votre projet. Donc, lorsque vous voulez logger la nourriture qui a été commandée, vous pouvez utiliser la même instance _FoodLogger_ dans plusieurs fichiers ou composants.

```javascript
const FoodLogger = require('./FoodLogger')

const foodLogger = new FoodLogger().getFoodLoggerInstance()

class Customer {
  constructor(order) {
    this.price = order.price
    this.food = order.foodItem
    foodLogger.log(order)
  }
  
  // d'autres choses sympas se passant pour le client
}

module.exports = Customer
```

```javascript
const FoodLogger = require('./FoodLogger')

const foodLogger = new FoodLogger().getFoodLoggerInstance()

class Restaurant {
  constructor(inventory) {
    this.quantity = inventory.count
    this.food = inventory.foodItem
    foodLogger.log(inventory)
  }
  
  // d'autres choses sympas se passant au restaurant
}

module.exports = Restaurant
```

Avec ce modèle singleton en place, vous n'avez pas à vous soucier de ne recevoir que les logs du fichier principal de l'application. Vous pouvez les obtenir de n'importe où dans votre base de code et ils iront tous à la même instance exacte du logger, ce qui signifie qu'aucun de vos logs ne devrait se perdre en raison de nouvelles instances.

## Le Modèle de Conception Stratégie

Le modèle stratégie est comme une version avancée d'une instruction if else. C'est essentiellement là où vous créez une interface pour une méthode que vous avez dans votre classe de base. Cette interface est ensuite utilisée pour trouver la bonne implémentation de cette méthode qui devrait être utilisée dans une classe dérivée. L'implémentation, dans ce cas, sera décidée à l'exécution en fonction du client.

Ce modèle est incroyablement utile dans les situations où vous avez des méthodes requises et optionnelles pour une classe. Certaines instances de cette classe n'auront pas besoin des méthodes optionnelles, et cela pose un problème pour les solutions d'héritage. Vous pourriez utiliser des interfaces pour les méthodes optionnelles, mais alors vous devriez écrire l'implémentation chaque fois que vous utilisez cette classe puisque qu'il n'y aurait pas d'implémentation par défaut.

C'est là que le modèle stratégie nous sauve. Au lieu que le client recherche une implémentation, il délègue à une interface de stratégie et la stratégie trouve la bonne implémentation. Une utilisation courante de cela est avec les systèmes de traitement des paiements.

Vous pourriez avoir un panier d'achat qui ne permet aux clients de payer qu'avec leur carte de crédit, mais vous perdrez des clients qui veulent utiliser d'autres méthodes de paiement. 

Le modèle de conception stratégie nous permet de découpler les méthodes de paiement du processus de paiement, ce qui signifie que nous pouvons ajouter ou mettre à jour des stratégies sans changer de code dans le panier d'achat ou le processus de paiement.

Voici un exemple d'implémentation du modèle stratégie en utilisant l'exemple de méthode de paiement.

```typescript
class PaymentMethodStrategy {

  const customerInfoType = {
    country: string
    emailAddress: string
    name: string
    accountNumber?: number
    address?: string
    cardNumber?: number
    city?: string
    routingNumber?: number
    state?: string
  }
  
  static BankAccount(customerInfo: customerInfoType) {
    const { name, accountNumber, routingNumber } = customerInfo
    // faire des choses pour obtenir le paiement
  }
  
  static BitCoin(customerInfo: customerInfoType) {
    const { emailAddress, accountNumber } = customerInfo
    // faire des choses pour obtenir le paiement
  }
  
  static CreditCard(customerInfo: customerInfoType) {
    const { name, cardNumber, emailAddress } = customerInfo
    // faire des choses pour obtenir le paiement
  }
  
  static MailIn(customerInfo: customerInfoType) {
    const { name, address, city, state, country } = customerInfo
    // faire des choses pour obtenir le paiement
  }
  
  static PayPal(customerInfo: customerInfoType) {
    const { emailAddress } = customerInfo
    // faire des choses pour obtenir le paiement
  }
}
```

Pour implémenter notre stratégie de méthode de paiement, nous avons créé une seule classe avec plusieurs méthodes statiques. Chaque méthode prend le même paramètre, _customerInfo_, et ce paramètre a un type défini de _customerInfoType_. (Hey tous les développeurs TypeScript ! 💡) Notez que chaque méthode a sa propre implémentation et utilise différentes valeurs de _customerInfo_.

Avec le modèle stratégie, vous pouvez également changer dynamiquement la stratégie utilisée à l'exécution. Cela signifie que vous pourrez changer la stratégie, ou l'implémentation de la méthode, utilisée en fonction de l'entrée de l'utilisateur ou de l'environnement dans lequel l'application s'exécute.

Vous pouvez également définir une implémentation par défaut dans un simple fichier _config.json_ comme ceci :

```json
{
  "paymentMethod": {
    "strategy": "PayPal"
  }
}
```

Chaque fois qu'un client commence à passer par le processus de paiement sur votre site web, la méthode de paiement par défaut qu'il rencontrera sera l'implémentation PayPal qui provient du _config.json_. Cela pourrait facilement être mis à jour si le client sélectionne une méthode de paiement différente.

Maintenant, nous allons créer un fichier pour notre processus de paiement.

```javascript
const PaymentMethodStrategy = require('./PaymentMethodStrategy')
const config = require('./config')

class Checkout {
  constructor(strategy='CreditCard') {
    this.strategy = PaymentMethodStrategy[strategy]
  }
  
  // faire du code sophistiqué ici et obtenir l'entrée de l'utilisateur et la méthode de paiement
  
  changeStrategy(newStrategy) {
    this.strategy = PaymentMethodStrategy[newStrategy]
  }
  
  const userInput = {
    name: 'Malcolm',
    cardNumber: 3910000034581941,
    emailAddress: 'mac@gmailer.com',
    country: 'US'
  }
  
  const selectedStrategy = 'Bitcoin'
  
  changeStrategy(selectedStrategy)
  
  postPayment(userInput) {
    this.strategy(userInput)
  }
}

module.exports = new Checkout(config.paymentMethod.strategy)
```

Cette classe _Checkout_ est là où le modèle stratégie peut se montrer. Nous importons quelques fichiers pour avoir les stratégies de méthodes de paiement disponibles et la stratégie par défaut du _config_.

Ensuite, nous créons la classe avec le constructeur et une valeur de repli pour la stratégie _strategy_ par défaut au cas où aucune n'aurait été définie dans le _config_. Ensuite, nous attribuons la valeur _strategy_ à une variable d'état locale.

Une méthode importante que nous devons implémenter dans notre classe _Checkout_ est la capacité de changer la stratégie de paiement. Un client pourrait changer la méthode de paiement qu'il souhaite utiliser et vous devrez être en mesure de gérer cela. C'est à cela que sert la méthode _changeStrategy_.

Après avoir fait du code sophistiqué et obtenu toutes les entrées d'un client, vous pouvez alors mettre à jour la stratégie de paiement immédiatement en fonction de leur entrée et elle définit dynamiquement la _strategy_ avant que le paiement ne soit envoyé pour traitement.

À un moment donné, vous pourriez avoir besoin d'ajouter plus de méthodes de paiement à votre panier d'achat et tout ce que vous aurez à faire est de l'ajouter à la classe _PaymentMethodStrategy_. Elle sera instantanément disponible partout où cette classe est utilisée.

Le modèle de conception stratégie est puissant lorsque vous traitez avec des méthodes qui ont plusieurs implémentations. Cela peut sembler que vous utilisez une interface, mais vous n'avez pas à écrire une implémentation pour la méthode chaque fois que vous l'appelez dans une classe différente. Cela vous donne plus de flexibilité que les interfaces.

## Le Modèle de Conception Observateur

Si vous avez déjà utilisé le modèle MVC, vous avez déjà utilisé le modèle de conception observateur. La partie Modèle est comme un sujet et la partie Vue est comme un observateur de ce sujet. Votre sujet contient toutes les données et l'état de ces données. Ensuite, vous avez des observateurs, comme différents composants, qui obtiendront ces données du sujet lorsque les données auront été mises à jour.

Le but du modèle de conception observateur est de créer cette relation un-à-plusieurs entre le sujet et tous les observateurs attendant des données pour qu'ils puissent être mis à jour. Ainsi, chaque fois que l'état du sujet change, tous les observateurs seront notifiés et mis à jour instantanément.

Quelques exemples de quand vous utiliseriez ce modèle incluent : l'envoi de notifications utilisateur, la mise à jour, les filtres et la gestion des abonnés.

Supposons que vous avez une application monopage qui a trois listes déroulantes de fonctionnalités qui dépendent de la sélection d'une catégorie à partir d'une liste déroulante de niveau supérieur. C'est courant sur de nombreux sites de shopping, comme Home Depot. Vous avez un tas de filtres sur la page qui dépendent de la valeur d'un filtre de niveau supérieur.

Le code pour la liste déroulante de niveau supérieur pourrait ressembler à ceci :

```javascript
class CategoryDropdown {
  constructor() {
    this.categories = ['appliances', 'doors', 'tools']
    this.subscriber = []
  }
  
  // prétendez qu'il y a du code sophistiqué ici
  
  subscribe(observer) {
    this.subscriber.push(observer)
  }
  
  onChange(selectedCategory) {
    this.subscriber.forEach(observer => observer.update(selectedCategory))
  }
}
```

Ce fichier _CategoryDropdown_ est une simple classe avec un constructeur qui initialise les options de catégorie que nous avons disponibles dans la liste déroulante. C'est le fichier où vous géreriez la récupération d'une liste à partir du back-end ou tout type de tri que vous souhaitez faire avant que l'utilisateur ne voie les options.

La méthode _subscribe_ est la façon dont chaque filtre créé avec cette classe recevra des mises à jour sur l'état de l'observateur.

La méthode _onChange_ est la façon dont nous envoyons une notification à tous les abonnés qu'un changement d'état s'est produit dans l'observateur qu'ils surveillent. Nous parcourons simplement tous les abonnés et appelons leur méthode _update_ avec le _selectedCategory_.

Le code pour les autres filtres pourrait ressembler à ceci :

```javascript
class FilterDropdown {
  constructor(filterType) {
    this.filterType = filterType
    this.items = []
  }
  
  // plus de code sophistiqué ici ; peut-être faire cet appel API pour obtenir la liste des éléments en fonction de filterType
  
  update(category) {
    fetch('https://example.com')
      .then(res => this.items(res))
  }
}
```

Ce fichier _FilterDropdown_ est une autre simple classe qui représente toutes les listes déroulantes potentielles que nous pourrions utiliser sur une page. Lorsqu'une nouvelle instance de cette classe est créée, elle doit recevoir un _filterType_. Cela pourrait être utilisé pour faire des appels API spécifiques afin d'obtenir la liste des éléments.

La méthode _update_ est une implémentation de ce que vous pouvez faire avec la nouvelle catégorie une fois qu'elle a été envoyée par l'observateur.

Maintenant, nous allons voir ce que cela signifie d'utiliser ces fichiers avec le modèle observateur :

```javascript
const CategoryDropdown = require('./CategoryDropdown')
const FilterDropdown = require('./FilterDropdown')

const categoryDropdown = new CategoryDropdown() 

const colorsDropdown = new FilterDropdown('colors')
const priceDropdown = new FilterDropdown('price')
const brandDropdown = new FilterDropdown('brand')

categoryDropdown.subscribe(colorsDropdown)
categoryDropdown.subscribe(priceDropdown)
categoryDropdown.subscribe(brandDropdown)
```

Ce que ce fichier nous montre, c'est que nous avons 3 listes déroulantes qui sont abonnées à la liste déroulante de catégorie observable. Ensuite, nous abonnons chacune de ces listes déroulantes à l'observateur. Chaque fois que la catégorie de l'observateur est mise à jour, elle enverra la valeur à chaque abonné qui mettra à jour les listes déroulantes individuelles instantanément.

## Le Modèle de Conception Décorateur

Utiliser le modèle de conception décorateur est assez simple. Vous pouvez avoir une classe de base avec des méthodes et des propriétés qui sont présentes lorsque vous créez un nouvel objet avec la classe. Maintenant, disons que vous avez certaines instances de la classe qui ont besoin de méthodes ou de propriétés qui ne proviennent pas de la classe de base.

Vous pouvez ajouter ces méthodes et propriétés supplémentaires à la classe de base, mais cela pourrait perturber vos autres instances. Vous pourriez même créer des sous-classes pour contenir des méthodes et des propriétés spécifiques dont vous avez besoin et que vous ne pouvez pas mettre dans votre classe de base.

Chacune de ces approches résoudra votre problème, mais elles sont encombrantes et inefficaces. C'est là que le modèle décorateur intervient. Au lieu de rendre votre base de code laide juste pour ajouter quelques choses à une instance d'objet, vous pouvez ajouter ces choses spécifiques directement à l'instance.

Ainsi, si vous devez ajouter une nouvelle propriété qui contient le prix pour un objet, vous pouvez utiliser le modèle décorateur pour l'ajouter directement à cette instance d'objet particulière et cela n'affectera aucune autre instance de cet objet de classe.

Avez-vous déjà commandé de la nourriture en ligne ? Alors vous avez probablement rencontré le modèle décorateur. Si vous prenez un sandwich et que vous voulez ajouter des garnitures spéciales, le site web n'ajoute pas ces garnitures à chaque instance de sandwich que les utilisateurs actuels essaient de commander.

Voici un exemple de classe client :

```javascript
class Customer {
  constructor(balance=20) {
    this.balance = balance
    this.foodItems = []
  }
  
  buy(food) {
    if (food.price) < this.balance {
      console.log('you should get it')
      this.balance -= food.price
      this.foodItems.push(food)
    }
    else {
      console.log('maybe you should get something else')
    }
  }
}

module.exports = Customer
```

Et voici un exemple de classe sandwich :

```javascript
class Sandwich {
  constructor(type, price) {
    this.type = type
    this.price = price
  }
  
  order() {
    console.log(`You ordered a ${this.type} sandwich for $ ${this.price}.`)
  }
}

class DeluxeSandwich {
  constructor(baseSandwich) {
    this.type = `Deluxe ${baseSandwich.type}`
    this.price = baseSandwich.price + 1.75
  }
}

class ExquisiteSandwich {
  constructor(baseSandwich) {
    this.type = `Exquisite ${baseSandwich.type}`
    this.price = baseSandwich.price + 10.75
  }
  
  order() {
    console.log(`You ordered an ${this.type} sandwich. It's got everything you need to be happy for days.`)
  }
}

module.exports = { Sandwich, DeluxeSandwich, ExquisiteSandwich }
```

Cette classe sandwich est là où le modèle décorateur est utilisé. Nous avons une classe de base _Sandwich_ qui définit les règles pour ce qui se passe lorsqu'un sandwich ordinaire est commandé. Les clients pourraient vouloir améliorer les sandwichs et cela signifie simplement un changement d'ingrédient et de prix.

Vous vouliez simplement ajouter la fonctionnalité d'augmenter le prix et de mettre à jour le type de sandwich pour le _DeluxeSandwich_ sans changer la façon dont il est commandé. Bien que vous ayez peut-être besoin d'une méthode de commande différente pour un _ExquisiteSandwich_ parce qu'il y a un changement drastique dans la qualité des ingrédients.

Le modèle décorateur vous permet de changer dynamiquement la classe de base sans l'affecter ni aucune autre classe. Vous n'avez pas à vous soucier de l'implémentation de fonctions que vous ne connaissez pas, comme avec les interfaces, et vous n'avez pas à inclure des propriétés que vous n'utiliserez pas dans chaque classe.

Maintenant, nous allons passer en revue un exemple où cette classe est instanciée comme si un client passait une commande de sandwich.

```javascript
const { Sandwich, DeluxeSandwich, ExquisiteSandwich } = require('./Sandwich')
const Customer = require('./Customer')

const cust1 = new Customer(57)

const turkeySandwich = new Sandwich('Turkey', 6.49)
const bltSandwich = new Sandwich('BLT', 7.55)

const deluxeBltSandwich = new DeluxeSandwich(bltSandwich)
const exquisiteTurkeySandwich = new ExquisiteSandwich(turkeySandwich)

cust1.buy(turkeySandwich)
cust1.buy(bltSandwich)
```

## Réflexions Finales

Je pensais autrefois que les modèles de conception étaient ces directives de développement logiciel folles et lointaines. Ensuite, j'ai découvert que je les utilisais tout le temps ! 

Quelques-uns des modèles que j'ai couverts sont utilisés dans tant d'applications que cela vous soufflerait l'esprit. Ils ne sont que de la théorie à la fin de la journée. C'est à nous, en tant que développeurs, d'utiliser cette théorie de manière à rendre nos applications faciles à implémenter et à maintenir.

Avez-vous utilisé d'autres modèles de conception pour vos projets ? La plupart des endroits choisissent généralement un modèle de conception pour leurs projets et s'y tiennent, alors j'aimerais avoir de vos nouvelles sur ce que vous utilisez.

Merci d'avoir lu. Vous devriez me suivre sur Twitter car je poste généralement des choses utiles/divertissantes : [@FlippedCoding](https://twitter.com/FlippedCoding)