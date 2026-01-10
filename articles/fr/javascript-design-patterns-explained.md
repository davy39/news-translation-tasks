---
title: Modèles de conception JavaScript – Expliqués avec des exemples
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2022-06-22T17:06:02.000Z'
originalURL: https://freecodecamp.org/news/javascript-design-patterns-explained
coverImage: https://www.freecodecamp.org/news/content/images/2022/04/pexels-pixabay-161043.jpg
tags:
- name: design patterns
  slug: design-patterns
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software design patterns
  slug: software-design-patterns
seo_title: Modèles de conception JavaScript – Expliqués avec des exemples
seo_desc: 'Hi everyone! In this article I''ll explain what design patterns are and
  why they''re useful.

  We''ll also go through some of the most popular design patterns out there and give
  examples for each of them. Let''s go!

  Table of Contents


  What Are Design Patte...'
---

Bonjour à tous ! Dans cet article, je vais expliquer ce que sont les modèles de conception et pourquoi ils sont utiles.

Nous allons également passer en revue certains des modèles de conception les plus populaires et donner des exemples pour chacun d'eux. C'est parti !

## Table des matières

* [Qu'est-ce que les modèles de conception ?](#heading-quest-ce-que-les-modeles-de-conception)
    
* [Modèles de conception de création](#heading-modeles-de-conception-de-creation)
    
    * [Modèle Singleton](#heading-modele-singleton)
        
    * [Modèle de méthode de fabrication](#heading-modele-de-methode-de-fabrication)
        
    * [Modèle de fabrique abstraite](#heading-modele-de-fabrique-abstraite)
        
    * [Modèle de construction](#heading-modele-de-construction)
        
    * [Modèle de prototype](#heading-modele-de-prototype)
        
* [Modèles de conception structurels](#heading-modeles-de-conception-structurels)
    
    * [Modèle d'adaptateur](#heading-modele-dadaptateur)
        
    * [Modèle de décorateur](#heading-modele-de-decorateur)
        
    * [Modèle de façade](#heading-modele-de-facade)
        
    * [Modèle de proxy](#heading-modele-de-proxy)
        
* [Modèles de conception comportementaux](#heading-modeles-de-conception-comportementaux)
    
    * [Modèle de chaîne de responsabilité](#heading-modele-de-chaine-de-responsabilite)
        
    * [Modèle d'itérateur](#heading-modele-diterateur)
        
    * [Modèle d'observateur](#heading-modele-dobservateur)
        
* [Résumé](#heading-resume)
    

# Qu'est-ce que les modèles de conception ?

Les modèles de conception ont été popularisés par [le livre "Design Patterns: Elements of Reusable Object-Oriented Software"](https://en.wikipedia.org/wiki/Design_Patterns), publié en 1994 par un groupe de quatre ingénieurs C++.

Le livre explore les capacités et les pièges de la programmation orientée objet, et décrit 23 modèles utiles que vous pouvez implémenter pour résoudre des problèmes de programmation courants.

Ces modèles ne sont **pas des algorithmes ou des implémentations spécifiques**. Ils sont plus comme des **idées, des opinions et des abstractions** qui peuvent être utiles dans certaines situations pour résoudre un type particulier de problème.

L'implémentation spécifique des modèles peut varier en fonction de nombreux facteurs différents. Mais ce qui est important, ce sont les concepts qui les sous-tendent, et comment ils peuvent nous aider à atteindre une meilleure solution pour notre problème.

Cela étant dit, gardez à l'esprit que ces modèles ont été conçus en pensant à la programmation OOP C++. En ce qui concerne les langages plus modernes comme JavaScript ou d'autres paradigmes de programmation, ces modèles peuvent ne pas être également utiles et peuvent même ajouter un code inutile à notre code.

Néanmoins, je pense qu'il est bon de les connaître en tant que connaissances générales en programmation.

Commentaire secondaire : Si vous n'êtes pas familier avec [les paradigmes de programmation](https://www.freecodecamp.org/news/an-introduction-to-programming-paradigms/) ou [la POO](https://www.freecodecamp.org/news/object-oriented-javascript-for-beginners/), j'ai récemment écrit deux articles sur ces sujets. 😉

En tout cas... Maintenant que nous avons fait l'introduction, les modèles de conception sont classés en trois catégories principales : **modèles de création, structurels et comportementaux**. Explorons brièvement chacun d'eux. 🧠

# Modèles de conception de création

Les modèles de création consistent en différents mécanismes utilisés pour créer des objets.

## Modèle Singleton

**Singleton** est un modèle de conception qui garantit qu'une classe n'a qu'une seule instance immuable. Dit simplement, le modèle singleton consiste en un objet qui ne peut pas être copié ou modifié. Il est souvent utile lorsque nous voulons avoir un seul *point de vérité* immuable pour notre application.

Disons par exemple que nous voulons avoir toute la configuration de notre application dans un seul objet. Et nous voulons interdire toute duplication ou modification de cet objet.

Deux façons d'implémenter ce modèle sont d'utiliser des littéraux d'objet et des classes :

```javascript
const Config = {
  start: () => console.log('App has started'),
  update: () => console.log('App has updated'),
}

// Nous gelons l'objet pour empêcher l'ajout de nouvelles propriétés et la modification ou la suppression de propriétés existantes
Object.freeze(Config)

Config.start() // "App has started"
Config.update() // "App has updated"

Config.name = "Robert" // Nous essayons d'ajouter une nouvelle clé
console.log(Config) // Et vérifions que cela ne fonctionne pas : { start: [Function: start], update: [Function: update] }
```

```javascript
class Config {
    constructor() {}
    start(){ console.log('App has started') }  
    update(){ console.log('App has updated') }
}
  
const instance = new Config()
Object.freeze(instance)
```

## Modèle de méthode de fabrication

Le modèle **Factory method** fournit une interface pour créer des objets qui peuvent être modifiés après leur création. Le truc cool avec cela est que la logique de création de nos objets est centralisée en un seul endroit, simplifiant et mieux organisant notre code.

Ce modèle est beaucoup utilisé et peut également être implémenté de deux manières différentes, via des classes ou des fonctions de fabrication (fonctions qui retournent un objet).

```javascript
class Alien {
    constructor (name, phrase) {
        this.name = name
        this.phrase = phrase
        this.species = "alien"
    }
    fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
    sayPhrase = () => console.log(this.phrase)
}

const alien1 = new Alien("Ali", "I'm Ali the alien!")
console.log(alien1.name) // output: "Ali"
```

```javascript
function Alien(name, phrase) {
    this.name = name
    this.phrase = phrase
    this.species = "alien"
}

Alien.prototype.fly = () => console.log("Zzzzzziiiiiinnnnnggggg!!")
Alien.prototype.sayPhrase = () => console.log(this.phrase)

const alien1 = new Alien("Ali", "I'm Ali the alien!")

console.log(alien1.name) // output "Ali"
console.log(alien1.phrase) // output "I'm Ali the alien!"
alien1.fly() // output "Zzzzzziiiiiinnnnnggggg"
```

## Modèle de fabrique abstraite

Le modèle **Abstract Factory** nous permet de produire des familles d'objets liés sans spécifier de classes concrètes. Il est utile dans les situations où nous devons créer des objets qui partagent seulement certaines propriétés et méthodes.

La façon dont cela fonctionne est en présentant une fabrique abstraite avec laquelle le client interagit. Cette **fabrique abstraite** appelle la **fabrique concrète** correspondante selon la logique correspondante. Et cette fabrique concrète est celle qui retourne l'objet final.

En gros, cela ajoute simplement une couche d'abstraction au-dessus du modèle de méthode de fabrication, afin que nous puissions créer de nombreux types d'objets différents, mais toujours interagir avec une seule fonction ou classe de fabrication.

Alors voyons cela avec un exemple. Disons que nous modélisons un système pour une entreprise automobile, qui construit des voitures, mais aussi des motos et des camions.

```javascript
// Nous avons une classe ou une "fabrique concrète" pour chaque type de véhicule
class Car {
    constructor () {
        this.name = "Car"
        this.wheels = 4
    }
    turnOn = () => console.log("Chacabúm!!")
}

class Truck {
    constructor () {
        this.name = "Truck"
        this.wheels = 8
    }
    turnOn = () => console.log("RRRRRRRRUUUUUUUUUMMMMMMMMMM!!")
}

class Motorcycle {
    constructor () {
        this.name = "Motorcycle"
        this.wheels = 2
    }
    turnOn = () => console.log("sssssssssssssssssssssssssssssshhhhhhhhhhham!!")
}

// Et une fabrique abstraite qui sert de point d'interaction unique pour nos clients
// Selon le paramètre de type qu'elle reçoit, elle appellera la fabrique concrète correspondante
const vehicleFactory = {
    createVehicle: function (type) {
        switch (type) {
            case "car":
                return new Car()
            case "truck":
                return new Truck()
            case "motorcycle":
                return new Motorcycle()
            default:
                return null
        }
    }
}

const car = vehicleFactory.createVehicle("car") // Car { turnOn: [Function: turnOn], name: 'Car', wheels: 4 }
const truck = vehicleFactory.createVehicle("truck") // Truck { turnOn: [Function: turnOn], name: 'Truck', wheels: 8 }
const motorcycle = vehicleFactory.createVehicle("motorcycle") // Motorcycle { turnOn: [Function: turnOn], name: 'Motorcycle', wheels: 2 }
```

## Modèle de construction

Le modèle **Builder** est utilisé pour créer des objets en "étapes". Normalement, nous aurons des fonctions ou des méthodes qui ajoutent certaines propriétés ou méthodes à notre objet.

Le truc cool avec ce modèle est que nous séparons la création des propriétés et des méthodes en différentes entités.

Si nous avions une classe ou une fonction de fabrication, l'objet que nous instancions aura toujours toutes les propriétés et méthodes déclarées dans cette classe/fabrique. Mais en utilisant le modèle de construction, nous pouvons créer un objet et lui appliquer uniquement les "étapes" dont nous avons besoin, ce qui est une approche plus flexible.

Cela est lié à [la composition d'objets](https://www.youtube.com/watch?v=wfMtDGfHWpA&t=3s), un sujet dont j'ai parlé [ici](https://www.freecodecamp.org/news/object-oriented-javascript-for-beginners/#object-composition).

```javascript
// Nous déclarons nos objets
const bug1 = {
    name: "Buggy McFly",
    phrase: "Your debugger doesn't work with me!"
}

const bug2 = {
    name: "Martiniano Buggland",
    phrase: "Can't touch this! Na na na na..."
}

// Ces fonctions prennent un objet comme paramètre et lui ajoutent une méthode
const addFlyingAbility = obj => {
    obj.fly = () => console.log(`Now ${obj.name} can fly!`)
}

const addSpeechAbility = obj => {
    obj.saySmthg = () => console.log(`${obj.name} walks the walk and talks the talk!`)
}

// Enfin, nous appelons les fonctions de construction en passant les objets comme paramètres
addFlyingAbility(bug1)
bug1.fly() // output: "Now Buggy McFly can fly!"

addSpeechAbility(bug2)
bug2.saySmthg() // output: "Martiniano Buggland walks the walk and talks the talk!"
```

## Modèle de prototype

Le modèle **Prototype** vous permet de créer un objet en utilisant un autre objet comme modèle, héritant de ses propriétés et méthodes.

Si vous êtes dans le monde JavaScript depuis un certain temps, vous êtes probablement familier avec [l'héritage prototypal](https://www.freecodecamp.org/news/prototypes-and-inheritance-in-javascript/) et comment JavaScript fonctionne autour de cela.

Le résultat final est très similaire à ce que nous obtenons en utilisant des classes, mais avec un peu plus de flexibilité puisque les propriétés et méthodes peuvent être partagées entre les objets sans dépendre de la même classe.

```javascript
// Nous déclarons notre objet prototype avec deux méthodes
const enemy = {
    attack: () => console.log("Pim Pam Pum!"),
    flyAway: () => console.log("Flyyyy like an eagle!")
}

// Nous déclarons un autre objet qui héritera de notre prototype
const bug1 = {
    name: "Buggy McFly",
    phrase: "Your debugger doesn't work with me!"
}

// Avec setPrototypeOf nous définissons le prototype de notre objet
Object.setPrototypeOf(bug1, enemy)

// Avec getPrototypeOf nous lisons le prototype et confirmons que le précédent a fonctionné
console.log(Object.getPrototypeOf(bug1)) // { attack: [Function: attack], flyAway: [Function: flyAway] }

console.log(bug1.phrase) // Your debugger doesn't work with me!
console.log(bug1.attack()) // Pim Pam Pum!
console.log(bug1.flyAway()) // Flyyyy like an eagle!
```

# Modèles de conception structurels

Les modèles structurels font référence à la manière d'assembler des objets et des classes en structures plus grandes.

## Modèle d'adaptateur

L'**Adaptateur** permet à deux objets avec des interfaces incompatibles d'interagir l'un avec l'autre.

Disons, par exemple, que votre application consulte une API qui retourne du [XML](https://www.freecodecamp.org/news/what-is-an-xml-file-how-to-open-xml-files-and-the-best-xml-viewers/) et envoie ces informations à une autre API pour traiter ces informations. Mais l'API de traitement attend du [JSON](https://www.freecodecamp.org/news/what-is-json-a-json-file-example/). Vous ne pouvez pas envoyer les informations telles qu'elles sont reçues puisque les deux interfaces sont incompatibles. Vous devez d'abord les *adapter*. 😉

Nous pouvons visualiser le même concept avec un exemple encore plus simple. Supposons que nous avons un tableau de villes et une fonction qui retourne le plus grand nombre d'habitants que ces villes ont. Le nombre d'habitants dans notre tableau est en millions, mais nous avons une nouvelle ville à ajouter qui a ses habitants sans la conversion en millions :

```javascript
// Notre tableau de villes
const citiesHabitantsInMillions = [
    { city: "London", habitants: 8.9 },
    { city: "Rome", habitants: 2.8 },
    { city: "New york", habitants: 8.8 },
    { city: "Paris", habitants: 2.1 },
] 

// La nouvelle ville que nous voulons ajouter
const BuenosAires = {
    city: "Buenos Aires",
    habitants: 3100000
}

// Notre fonction d'adaptateur prend notre ville et convertit la propriété habitants au même format que toutes les autres villes
const toMillionsAdapter = city => { city.habitants = parseFloat((city.habitants/1000000).toFixed(1)) }

toMillionsAdapter(BuenosAires)

// Nous ajoutons la nouvelle ville au tableau
citiesHabitantsInMillions.push(BuenosAires)

// Et cette fonction retourne le plus grand nombre d'habitants
const MostHabitantsInMillions = () => {
    return Math.max(...citiesHabitantsInMillions.map(city => city.habitants))
}

console.log(MostHabitantsInMillions()) // 8.9
```

## Modèle de décorateur

Le modèle **Décorateur** vous permet d'attacher de nouveaux comportements aux objets en les plaçant à l'intérieur d'objets conteneurs qui contiennent les comportements. Si vous êtes quelque peu familier avec React et les composants d'ordre supérieur (HOC), ce type d'approche vous est probablement familier.

Techniquement, les composants dans React sont des fonctions, pas des objets. Mais si nous pensons à la manière dont React Context ou [Memo](https://www.freecodecamp.org/news/memoization-in-javascript-and-react/) fonctionnent, nous pouvons voir que nous passons un composant comme enfant à ce HOC, et grâce à cela, ce composant enfant est capable d'accéder à certaines fonctionnalités.

Dans cet exemple, nous pouvons voir que le composant ContextProvider reçoit des enfants comme props :

```javascript

import { useState } from 'react'
import Context from './Context'

const ContextProvider: React.FC = ({children}) => {

    const [darkModeOn, setDarkModeOn] = useState(true)
    const [englishLanguage, setEnglishLanguage] = useState(true)

    return (
        <Context.Provider value={{
            darkModeOn,
            setDarkModeOn,
            englishLanguage,
            setEnglishLanguage
        }} >
            {children}
        </Context.Provider>
    )
}

export default ContextProvider
```

Ensuite, nous enveloppons toute l'application autour :

```javascript
export default function App() {
  return (
    <ContextProvider>
      <Router>

        <ErrorBoundary>
          <Suspense fallback={<></>}>
            <Header />
          </Suspense>

          <Routes>
              <Route path='/' element={<Suspense fallback={<></>}><AboutPage /></Suspense>}/>

              <Route path='/projects' element={<Suspense fallback={<></>}><ProjectsPage /></Suspense>}/>

              <Route path='/projects/helpr' element={<Suspense fallback={<></>}><HelprProject /></Suspense>}/>

              <Route path='/projects/myWebsite' element={<Suspense fallback={<></>}><MyWebsiteProject /></Suspense>}/>

              <Route path='/projects/mixr' element={<Suspense fallback={<></>}><MixrProject /></Suspense>}/>

              <Route path='/projects/shortr' element={<Suspense fallback={<></>}><ShortrProject /></Suspense>}/>

              <Route path='/curriculum' element={<Suspense fallback={<></>}><CurriculumPage /></Suspense>}/>

              <Route path='/blog' element={<Suspense fallback={<></>}><BlogPage /></Suspense>}/>

              <Route path='/contact' element={<Suspense fallback={<></>}><ContactPage /></Suspense>}/>
          </Routes>
        </ErrorBoundary>

      </Router>
    </ContextProvider>
  )
}
```

Et plus tard, en utilisant le hook `useContext`, je peux accéder à l'état défini dans le Context depuis n'importe quel composant de mon application.

```javascript

const AboutPage: React.FC = () => {

    const { darkModeOn, englishLanguage } = useContext(Context)
    
    return (...)
}

export default AboutPage
```

Encore une fois, cela peut ne pas être l'implémentation exacte que les auteurs du livre avaient en tête lorsqu'ils ont écrit sur ce modèle, mais je crois que l'idée est la même. Placer un objet à l'intérieur d'un autre afin qu'il puisse accéder à certaines fonctionnalités. ;)

## Modèle de façade

Le modèle **Façade** fournit une interface simplifiée à une bibliothèque, un framework, ou tout autre ensemble complexe de classes.

Eh bien... nous pouvons probablement trouver de nombreux exemples pour cela, n'est-ce pas ? Je veux dire, React lui-même ou l'une des milliards de bibliothèques utilisées pour à peu près tout ce qui est lié au développement logiciel. Surtout lorsque nous pensons à la [programmation déclarative](https://www.freecodecamp.org/news/an-introduction-to-programming-paradigms/#declarative-programming), il s'agit de fournir des abstractions qui cachent la complexité des yeux du développeur.

Un exemple simple pourrait être les fonctions `map`, `sort`, `reduce` et `filter` de JavaScript, qui fonctionnent toutes comme de bonnes vieilles boucles `for` sous le capot.

Un autre exemple pourrait être l'une des bibliothèques utilisées pour le développement d'interfaces utilisateur de nos jours, comme [MUI](https://mui.com/). Comme nous pouvons le voir dans l'exemple suivant, ces bibliothèques nous offrent des composants qui apportent des fonctionnalités et des fonctionnalités intégrées qui nous aident à construire du code plus rapidement et plus facilement.

Mais tout cela, une fois compilé, se transforme en simples éléments HTML, qui sont la seule chose que les navigateurs comprennent. Ces composants ne sont que des abstractions qui sont là pour faciliter notre vie.

![Image](https://www.freecodecamp.org/news/content/images/2022/06/thewolfofwallstreet-fairydust.gif align="left")

*Une façade...*

```javascript
import * as React from 'react';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TableRow from '@mui/material/TableRow';
import Paper from '@mui/material/Paper';

function createData(
  name: string,
  calories: number,
  fat: number,
  carbs: number,
  protein: number,
) {
  return { name, calories, fat, carbs, protein };
}

const rows = [
  createData('Frozen yoghurt', 159, 6.0, 24, 4.0),
  createData('Ice cream sandwich', 237, 9.0, 37, 4.3),
  createData('Eclair', 262, 16.0, 24, 6.0),
  createData('Cupcake', 305, 3.7, 67, 4.3),
  createData('Gingerbread', 356, 16.0, 49, 3.9),
];

export default function BasicTable() {
  return (
    <TableContainer component={Paper}>
      <Table sx={{ minWidth: 650 }} aria-label="simple table">
        <TableHead>
          <TableRow>
            <TableCell>Dessert (100g serving)</TableCell>
            <TableCell align="right">Calories</TableCell>
            <TableCell align="right">Fat&nbsp;(g)</TableCell>
            <TableCell align="right">Carbs&nbsp;(g)</TableCell>
            <TableCell align="right">Protein&nbsp;(g)</TableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {rows.map((row) => (
            <TableRow
              key={row.name}
              sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
            >
              <TableCell component="th" scope="row">
                {row.name}
              </TableCell>
              <TableCell align="right">{row.calories}</TableCell>
              <TableCell align="right">{row.fat}</TableCell>
              <TableCell align="right">{row.carbs}</TableCell>
              <TableCell align="right">{row.protein}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
```

## Modèle de proxy

Le modèle **Proxy** fournit un substitut ou un espace réservé pour un autre objet. L'idée est de contrôler l'accès à l'objet original, en effectuant une sorte d'action avant ou après que la demande atteigne l'objet original réel.

Encore une fois, si vous êtes familier avec [ExpressJS](https://expressjs.com/), cela vous dit probablement quelque chose. Express est un framework utilisé pour développer des API NodeJS, et l'une des fonctionnalités qu'il possède est l'utilisation de Middlewares. Les Middlewares ne sont rien de plus que des morceaux de code que nous pouvons faire exécuter avant, au milieu ou après qu'une demande atteigne nos endpoints.

Voyons cela avec un exemple. Ici, j'ai une fonction qui valide un jeton d'authentification. Ne prenez pas trop attention à la manière dont elle le fait. Sachez simplement qu'elle reçoit le jeton comme paramètre, et une fois qu'elle a terminé, elle appelle la fonction `next()`.

```javascript
const jwt = require('jsonwebtoken')

module.exports = function authenticateToken(req, res, next) {
    const authHeader = req.headers['authorization']
    const token = authHeader && authHeader.split(' ')[1]
  
    if (token === null) return res.status(401).send(JSON.stringify('No access token provided'))
  
    jwt.verify(token, process.env.TOKEN_SECRET, (err, user) => {
      if (err) return res.status(403).send(JSON.stringify('Wrong token provided'))
      req.user = user
      next()
    })
}
```

Cette fonction est un middleware, et nous pouvons l'utiliser dans n'importe quel endpoint de notre API de la manière suivante. Nous plaçons simplement le middleware après l'adresse de l'endpoint et avant la déclaration de la fonction de l'endpoint :

```javascript
router.get('/:jobRecordId', authenticateToken, async (req, res) => {
  try {
    const job = await JobRecord.findOne({_id: req.params.jobRecordId})
    res.status(200).send(job)

  } catch (err) {
    res.status(500).json(err)
  }
})
```

De cette manière, si aucun jeton ou un jeton incorrect est fourni, le middleware retournera la réponse d'erreur correspondante. Si un jeton valide est fourni, le middleware appellera la fonction `next()` et la fonction de l'endpoint sera exécutée ensuite.

Nous aurions pu simplement écrire le même code dans l'endpoint lui-même et valider le jeton là, sans nous soucier des middlewares ou autre chose. Mais le truc, c'est que maintenant nous avons une abstraction que nous pouvons réutiliser dans de nombreux endpoints différents. 😉

Encore une fois, cela peut ne pas avoir été l'idée précise que les auteurs avaient en tête, mais je crois que c'est un exemple valide. Nous contrôlons l'accès à un objet afin de pouvoir effectuer des actions à un moment particulier.

# Modèles de conception comportementaux

Les modèles comportementaux contrôlent la communication et l'assignation de responsabilités entre différents objets.

## Modèle de chaîne de responsabilité

La **Chaîne de responsabilité** transmet les demandes le long d'une chaîne de gestionnaires. Chaque gestionnaire décide soit de traiter la demande, soit de la transmettre au gestionnaire suivant dans la chaîne.

Pour ce modèle, nous pourrions utiliser le même exemple exact que précédemment, car les middlewares dans Express sont en quelque sorte des gestionnaires qui traitent soit une demande, soit la transmettent au gestionnaire suivant.

Si vous souhaitez un autre exemple, pensez à n'importe quel système dans lequel vous avez certaines informations à traiter à travers de nombreuses étapes. À chaque étape, une entité différente est responsable de l'exécution d'une action, et les informations ne sont transmises à une autre entité que si une certaine condition est remplie.

Une application front-end typique qui consomme une API pourrait servir d'exemple :

* Nous avons une fonction responsable du rendu d'un composant UI.
    
* Une fois rendu, une autre fonction fait une demande à un endpoint d'API.
    
* Si la réponse de l'endpoint est celle attendue, les informations sont transmises à une autre fonction qui trie les données d'une certaine manière et les stocke dans une variable.
    
* Une fois que cette variable stocke les informations nécessaires, une autre fonction est responsable de les rendre dans l'UI.
    

Nous pouvons voir comment ici nous avons de nombreuses entités différentes qui collaborent pour exécuter une certaine tâche. Chacune d'elles est responsable d'une seule "étape" de cette tâche, ce qui aide à la modularité du code et à la séparation des préoccupations.👌👌

## Modèle d'itérateur

L'**itérateur** est utilisé pour parcourir les éléments d'une collection. Cela peut sembler trivial dans les langages de programmation utilisés de nos jours, mais ce n'était pas toujours le cas.

En tout cas, l'une des fonctions intégrées de JavaScript que nous avons à notre disposition pour itérer sur des structures de données (`for`, `forEach`, `for...of`, `for...in`, `map`, `reduce`, `filter`, etc.) sont des exemples du modèle d'itérateur.

De même que tout [algorithme de parcours](https://www.freecodecamp.org/news/introduction-to-algorithms-with-javascript-examples/#traversing-algorithms) que nous codons pour itérer à travers des [structures de données plus complexes comme les arbres ou les graphes](https://www.freecodecamp.org/news/data-structures-in-javascript-with-examples/).

## Modèle d'observateur

Le modèle **observateur** vous permet de définir un mécanisme de souscription pour notifier plusieurs objets de tout événement qui se produit sur l'objet qu'ils observent. En gros, c'est comme avoir un écouteur d'événement sur un objet donné, et lorsque cet objet effectue l'action que nous écoutons, nous faisons quelque chose.

Le hook useEffect de React pourrait être un bon exemple ici. Ce que fait useEffect, c'est exécuter une fonction donnée au moment où nous la déclarons.

Le hook est divisé en deux parties principales, la fonction exécutable et un tableau de dépendances. Si le tableau est vide, comme dans l'exemple suivant, la fonction est exécutée chaque fois que le composant est rendu.

```javascript
  useEffect(() => { console.log('The component has rendered') }, [])
```

Si nous déclarons des variables dans le tableau de dépendances, la fonction ne s'exécutera que lorsque ces variables changeront.

```javascript
  useEffect(() => { console.log('var1 has changed') }, [var1])
```

Même les anciens écouteurs d'événements JavaScript peuvent être considérés comme des observateurs. De plus, la programmation réactive et les bibliothèques comme [RxJS](https://rxjs.dev/), qui sont utilisées pour gérer des informations et des événements asynchrones à travers des systèmes, sont de bons exemples de ce modèle.

# **Résumé**

Si vous souhaitez en savoir plus sur ce sujet, je recommande cette [vidéo Fireship](https://www.youtube.com/watch?v=tv-_1er1mWI) et [ce site web génial](https://refactoring.guru/) où vous pouvez trouver des explications très détaillées avec des illustrations pour vous aider à comprendre chaque modèle.

Comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau. Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman).

Santé et à la prochaine ! ✋

![Image](https://www.freecodecamp.org/news/content/images/2022/06/See-ya-GIF.gif align="left")