---
title: Différents types d'APIs – SOAP vs REST vs GraphQL
subtitle: ''
author: German Cocca
co_authors: []
series: null
date: '2023-03-07T23:24:27.000Z'
originalURL: https://freecodecamp.org/news/rest-vs-graphql-apis
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/john-towner-p-rN-n6Miag-unsplash.jpg
tags:
- name: api
  slug: api
- name: GraphQL
  slug: graphql
- name: REST API
  slug: rest-api
seo_title: Différents types d'APIs – SOAP vs REST vs GraphQL
seo_desc: 'Hi everyone! In this article we''re going to take a good look at APIs,
  a core concept in modern software development.

  We''re going to talk about the main kinds of APIs used nowadays (SOAP, REST and
  GraphQL), their characteristics, pros and cons, and si...'
---

Bonjour à tous ! Dans cet article, nous allons examiner de près les APIs, un concept central dans le développement logiciel moderne.

Nous allons parler des principaux types d'APIs utilisés de nos jours (SOAP, REST et GraphQL), de leurs caractéristiques, avantages et inconvénients, ainsi que des situations dans lesquelles chacun d'eux peut être plus bénéfique.

C'est parti ! 👋

# Table des matières

* [Comment fonctionnent les APIs SOAP](#heading-fonctionnement-apis-soap)
    
    * [À propos de XML](#heading-a-propos-xml)
        
    * [Comment consommer une API SOAP](#heading-comment-consommer-api-soap)
        
* [Comment fonctionnent les APIs REST](#heading-fonctionnement-apis-rest)
    
    * [Comment consommer une API REST](#heading-comment-consommer-api-rest)
        
* [Comment fonctionnent les APIs GraphQL](#heading-fonctionnement-apis-graphql)
    
    * [Comment consommer une API GraphQL](#heading-comment-consommer-api-graphql)
        
* [Conclusion](#heading-conclusion)
    

## Introduction

Dans [un article récent](https://www.freecodecamp.org/news/an-introduction-to-software-architecture-patterns/), j'ai brièvement parlé de deux concepts très importants dans le développement logiciel moderne : le modèle client-serveur et les APIs.

**Client-serveur** est un modèle qui structure les tâches ou charges de travail d'une application entre un fournisseur de ressources ou services (serveur) et un demandeur de services ou ressources (client).

En termes simples, le client est l'application qui demande un certain type d'information ou effectue des actions, et le serveur est le programme qui envoie des informations ou effectue des actions en fonction de ce que fait le client.

La plupart des applications de nos jours utilisent un modèle client-serveur. Le concept le plus important à retenir est que **les clients demandent des ressources ou services** que **le serveur fournit**. La manière dont ces deux parties communiquent généralement est par le biais d'une **API** (interface de programmation d'application).

Une API n'est rien de plus qu'un **ensemble de règles définies qui établit comment une application peut communiquer avec une autre**. C'est comme un contrat entre les deux parties qui dit "Si tu envoies A, je répondrai toujours B. Si tu envoies C, je répondrai toujours D..." et ainsi de suite.

Avec cet ensemble de règles, le client sait exactement ce qu'il doit demander pour accomplir une certaine tâche, et le serveur sait exactement ce que le client demandera lorsqu'une certaine action doit être effectuée.

Les APIs sont absolument partout dans le développement logiciel actuel. Presque tout type d'application utilisera un modèle client-serveur activé par la communication API. C'est pourquoi je pense qu'il est très bon pour nous, en tant que développeurs, de bien les connaître.

Les moyens les plus populaires d'implémenter des APIs de nos jours sont REST et GraphQL. Nous allons également examiner SOAP, qui était assez populaire il y a quelques années et est encore utilisé dans certains secteurs de niche.

Si vous souhaitez une introduction plus approfondie sur ce que sont les APIs, [voici une vidéo géniale à ce sujet](https://www.youtube.com/watch?v=yBZO5Rb4ibo).

Avec tout cela en tête, plongeons dans les détails de fonctionnement des APIs SOAP, REST et GraphQL.

# Comment fonctionnent les APIs SOAP

Simple Object Access Protocol (SOAP) est un protocole de messagerie utilisé pour échanger des données structurées entre différents systèmes sur Internet. SOAP est un protocole basé sur XML et est considéré comme l'un des premiers protocoles de services web.

SOAP a été introduit pour la première fois en 1998 par Microsoft en tant que successeur de Common Object Request Broker Architecture (CORBA) et Distributed Component Object Model (DCOM).

SOAP a été conçu pour fournir un moyen indépendant de la plateforme d'échanger des données entre différents systèmes sur Internet. SOAP a ensuite été standardisé par le World Wide Web Consortium (W3C) en 2003.

**Caractéristiques principales :**

1. **Indépendant du protocole :** SOAP est conçu pour fonctionner avec n'importe quel protocole qui supporte la transmission de messages sur Internet, y compris HTTP, SMTP et FTP.
    
2. **Indépendant de la plateforme :** SOAP est conçu pour fonctionner avec n'importe quel langage de programmation ou plateforme qui supporte XML et peut envoyer et recevoir des messages HTTP.
    
3. **Messagerie :** SOAP est un protocole de messagerie et définit un ensemble de règles pour échanger des données structurées entre différents systèmes.
    
4. **Sécurité :** SOAP supporte plusieurs normes de sécurité, y compris le chiffrement, les signatures numériques et l'authentification.
    
5. **Extensibilité :** SOAP permet la création d'extensions personnalisées au protocole pour supporter des exigences spécifiques.
    

**Avantages :**

1. **Standardisation :** SOAP est un protocole bien établi et standardisé, ce qui en fait un choix fiable pour échanger des données entre différents systèmes.
    
2. **Sécurité :** SOAP fournit un support intégré pour plusieurs normes de sécurité, ce qui en fait un choix sécurisé pour transmettre des données sensibles.
    
3. **Extensibilité :** SOAP est hautement extensible et permet la création d'extensions personnalisées pour supporter des exigences spécifiques.
    

**Inconvénients :**

1. **Complexité :** SOAP peut être complexe à implémenter et peut nécessiter une expertise spécialisée.
    
2. **Overhead :** Les messages SOAP peuvent être volumineux et peuvent nécessiter des ressources de traitement significatives, ce qui entraîne une surcharge accrue.
    
3. **Performance :** SOAP peut être plus lent par rapport à d'autres protocoles d'API en raison de sa nature de messagerie.
    

**Idéal pour :**

1. **Lorsque vous devez transmettre des données sensibles :** SOAP supporte plusieurs normes de sécurité, ce qui en fait un choix sécurisé pour transmettre des données sensibles.
    
2. **Lorsque vous devez supporter des structures de données complexes :** SOAP supporte des structures de données complexes, ce qui en fait un bon choix pour transmettre et échanger des données entre différents systèmes.
    
3. **Lorsque vous avez besoin d'un protocole fiable et standardisé :** SOAP est un protocole bien établi et standardisé, ce qui en fait un choix fiable pour échanger des données entre différents systèmes.
    

Les APIs SOAP étaient largement utilisées dans les premiers jours des services web et sont encore utilisées dans plusieurs industries et secteurs aujourd'hui, bien que REST et GraphQL soient devenus plus populaires ces dernières années.

Voici quelques industries, secteurs et types d'applications dans lesquels SOAP est encore l'option principale :

1. **Santé :** SOAP est encore largement utilisé dans les applications de santé, en particulier dans les dossiers de santé électroniques (DSE) et les échanges d'informations de santé (EIS). Cela est dû au fait que SOAP fournit un moyen sécurisé et fiable de transmettre des informations sensibles sur les patients entre différents systèmes.
    
2. **Finance :** SOAP est encore utilisé dans les applications financières, telles que les passerelles de paiement et les plateformes de trading, car il fournit un moyen sécurisé et fiable de transmettre des données financières.
    
3. **Applications d'entreprise :** SOAP est encore utilisé dans les applications d'entreprise, telles que les systèmes de gestion de la relation client (CRM) et de planification des ressources d'entreprise (ERP), car il fournit un moyen standardisé et fiable d'échanger des données entre différents systèmes.
    
4. **Systèmes hérités :** De nombreux systèmes et applications plus anciens utilisent encore des APIs SOAP, et il peut être coûteux et chronophage de les migrer vers de nouvelles technologies.
    

En conclusion, les APIs SOAP existent depuis longtemps et sont encore utilisées dans plusieurs industries pour échanger des données entre différents systèmes.

SOAP pourrait être l'option la plus bénéfique pour développer une API lorsque vous devez transmettre des données sensibles, supporter des structures de données complexes, ou avoir besoin d'un protocole fiable et standardisé.

## À propos de XML

Comme mentionné, les APIs SOAP utilisent XML comme format principal pour la transmission de données, alors expliquons comment fonctionne XML.

XML signifie Extensible Markup Language. C'est un langage de balisage qui permet aux utilisateurs de créer des balises et attributs personnalisés pour décrire la structure et le contenu des données.

XML utilise un ensemble de règles pour encoder des documents dans un format à la fois lisible par l'homme et par la machine. Cela est réalisé en utilisant des balises pour définir les éléments d'un document, similaire à HTML.

Par exemple, un document XML peut avoir une balise appelée `<person>` pour définir un élément représentant une personne, avec des balises imbriquées pour des propriétés telles que `<name>`, `<age>`, et `<address>`. XML permet également aux utilisateurs de définir des balises personnalisées pour décrire leurs données de manière spécifique à leurs besoins.

XML est largement utilisé dans diverses industries, y compris la finance, la santé et le gouvernement. Il est souvent utilisé pour l'échange de données entre différentes applications et systèmes, car il fournit un moyen standardisé de représenter des données qui peuvent être facilement analysées par des ordinateurs. XML est également utilisé pour stocker des fichiers de configuration et des métadonnées pour diverses applications.

Dans l'ensemble, XML fournit un moyen flexible et extensible de décrire et d'échanger des données qui peuvent être facilement traitées par des ordinateurs. Cependant, son utilisation a décliné ces dernières années avec l'essor de formats plus modernes tels que JSON et YAML, qui sont plus légers et plus faciles à utiliser pour de nombreuses applications.

## Comment consommer une API SOAP

Voici un exemple de la manière dont vous pouvez faire une simple requête à une API SOAP à partir d'une application front-end JavaScript :

```javascript
// spécifier l'URL du point de terminaison de l'API SOAP
const url = 'http://www.example.com/soap-api';

// spécifier le message SOAP à envoyer
const soapMessage = '<?xml version="1.0" encoding="UTF-8"?>' +
                    '<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/" xmlns:ns1="http://example.com">' +
                    '<SOAP-ENV:Header/>' +
                    '<SOAP-ENV:Body>' +
                    '<ns1:GetData>' +
                    '<ns1:Id>123</ns1:Id>' +
                    '</ns1:GetData>' +
                    '</SOAP-ENV:Body>' +
                    '</SOAP-ENV:Envelope>';

// définir le type de contenu du message SOAP
const contentType = 'text/xml';

// faire la requête fetch
fetch(url, {
  method: 'POST', // SOAP utilise la méthode HTTP POST pour envoyer des requêtes à un serveur.
  headers: {
    'Content-Type': contentType,
    'SOAPAction': 'http://example.com/GetData'
  },
  body: soapMessage
})
  .then(response => response.text())
  .then(xml => {
    // gérer la réponse XML
    const parser = new DOMParser();
    const xmlDoc = parser.parseFromString(xml, 'text/xml');
    const value = xmlDoc.getElementsByTagName('Value')[0].childNodes[0].nodeValue;
    console.log(value);
  })
  .catch(error => console.error(error));
```

Décomposons ce que fait chaque ligne :

1. `const url = 'http://www.example.com/soap-api';` spécifie l'URL du point de terminaison de l'API SOAP.
    
2. `const soapMessage = '<?xml version="1.0" encoding="UTF-8"?>' + ...` spécifie le message SOAP à envoyer au point de terminaison de l'API. Il s'agit d'une chaîne contenant le balisage XML pour le message SOAP.
    
3. `const contentType = 'text/xml';` spécifie le type de contenu du message SOAP.
    
4. `fetch(url, { ... })` fait une requête fetch au point de terminaison de l'API en utilisant l'URL et les options spécifiées.
    
5. `method: 'POST',` spécifie la méthode HTTP à utiliser pour la requête.
    
6. `headers: { ... }` spécifie les en-têtes à inclure dans la requête.
    
7. `'Content-Type': contentType,` définit le type de contenu de l'en-tête de la requête à la valeur de `contentType`.
    
8. `'SOAPAction': 'http://example.com/GetData'` définit l'en-tête SOAPAction à la valeur de l'action SOAP qui correspond à la méthode de l'API appelée.
    
9. `body: soapMessage` définit le corps de la requête à la valeur de `soapMessage`.
    
10. `.then(response => response.text())` convertit la réponse en format texte.
    
11. `.then(xml => { ... })` gère la réponse du serveur.
    

Une réponse typique pourrait ressembler à ceci :

```xml
<?xml version="1.0" encoding="UTF-8"?>
<SOAP-ENV:Envelope xmlns:SOAP-ENV="http://schemas.xmlsoap.org/soap/envelope/">
   <SOAP-ENV:Body>
      <ns1:GetDataResponse xmlns:ns1="http://example.com">
         <ns1:Result>
            <ns1:Id>123</ns1:Id>
            <ns1:Value>42</ns1:Value>
         </ns1:Result>
      </ns1:GetDataResponse>
   </SOAP-ENV:Body>
</SOAP-ENV:Envelope>
```

Pour accéder aux valeurs dans la réponse XML, vous pouvez utiliser l'API DOMParser pour analyser la réponse en un objet de document XML, puis utiliser des méthodes de parcours DOM pour naviguer dans le document et extraire les valeurs.

Par exemple, le code suivant extrait la valeur de l'élément `Value` de l'objet de document XML :

```javascript
const parser = new DOMParser();
const xmlDoc = parser.parseFromString(xml, 'text/xml');
const value = xmlDoc.getElementsByTagName('Value')[0].childNodes[0].nodeValue;
console.log(value); // sortie : 42
```

Voici ce que fait chaque ligne :

1. `const parser = new DOMParser();` crée une nouvelle instance de l'objet DOMParser, qui est utilisé pour analyser la réponse XML.
    
2. `const xmlDoc = parser.parseFromString(xml, 'text/xml');` analyse la réponse XML en un objet de document XML.
    
3. `const value = xmlDoc.getElementsByTagName('Value')[0].childNodes[0].nodeValue;` récupère la valeur de l'élément `Value` de l'objet de document XML. Cette ligne utilise la méthode `getElementsByTagName()` pour obtenir tous les éléments avec le nom de balise `Value`, puis accède au premier élément (en supposant qu'il n'y en a qu'un), et obtient la valeur de son premier nœud enfant. La valeur est ensuite assignée à la variable `value`.
    
4. `console.log(value); // sortie : 42` enregistre la valeur de l'élément `Value` dans la console.
    

Dans l'ensemble, les réponses SOAP tendent à être plus verbeuses et complexes que les réponses des APIs REST ou GraphQL, en raison de leur utilisation de XML et du format d'enveloppe. Mais ce format fournit un moyen standardisé d'échanger des informations qui peut être utile dans certains secteurs et cas d'utilisation.

# Comment fonctionnent les APIs REST

Representational State Transfer (REST) est un style architectural largement utilisé pour construire des services web et des APIs.

REST a été introduit pour la première fois en 2000 par Roy Fielding dans sa thèse de doctorat, "Architectural Styles and the Design of Network-based Software Architectures." Fielding, qui était également l'un des principaux auteurs du protocole HTTP, a défini REST comme un style architectural basé sur les principes du web.

Les APIs RESTful sont conçues pour être simples, évolutives et flexibles. Elles sont souvent utilisées dans les applications web et mobiles, ainsi que dans les architectures Internet des objets (IoT) et microservices.

**Caractéristiques principales :**

1. **Sans état :** Les APIs REST sont sans état, ce qui signifie que chaque requête contient toutes les informations nécessaires pour la traiter. Cela facilite la mise à l'échelle de l'API et améliore les performances en réduisant le besoin de stocker et de gérer des données de session sur le serveur.
    
2. **Basé sur les ressources :** Les APIs REST sont basées sur les ressources, ce qui signifie que chaque ressource est identifiée par un URI (Uniform Resource Identifier) unique et peut être accessible en utilisant des méthodes HTTP standard telles que GET, POST, PUT et DELETE.
    
3. **Interface uniforme :** Les APIs REST ont une interface uniforme qui permet aux clients d'interagir avec les ressources en utilisant un ensemble standardisé de méthodes et de formats de réponse. Cela facilite le développement et la maintenance des APIs pour les développeurs, et leur consommation pour les clients.
    
4. **Cacheable :** Les APIs REST sont cacheables, ce qui signifie que les réponses peuvent être mises en cache pour améliorer les performances et réduire le trafic réseau.
    
5. **Système en couches :** Les APIs REST sont conçues pour être en couches, ce qui signifie que des intermédiaires tels que des proxies et des passerelles peuvent être ajoutés entre le client et le serveur sans affecter le système global.
    

**Avantages :**

* **Facile à apprendre et à utiliser :** Les APIs REST sont relativement simples et faciles à apprendre par rapport à d'autres APIs.
    
* **Évolutivité :** La nature sans état des APIs REST les rend hautement évolutives et efficaces.
    
* **Flexibilité :** Les APIs REST sont flexibles et peuvent être utilisées pour construire une large gamme d'applications et de systèmes.
    
* **Large support :** Les APIs REST sont largement supportées par des outils et frameworks de développement, ce qui facilite leur intégration dans des systèmes existants.
    

**Inconvénients :**

* **Manque de standards :** Le manque de standards stricts pour les APIs REST peut conduire à des incohérences et des problèmes d'interopérabilité.
    
* **Fonctionnalités limitées :** Les APIs REST sont conçues pour gérer des requêtes et réponses simples et peuvent ne pas être adaptées à des cas d'utilisation plus complexes.
    
* **Problèmes de sécurité :** Les APIs REST peuvent être vulnérables à des attaques de sécurité telles que le cross-site scripting (XSS) et le cross-site request forgery (CSRF) si elles ne sont pas implémentées correctement.
    

**Idéal pour :**

* Les APIs REST sont bien adaptées pour construire des applications web et mobiles, ainsi que des architectures microservices et des systèmes IoT.
    
* Elles sont particulièrement utiles dans des situations où l'évolutivité et la flexibilité sont importantes, et où les développeurs doivent s'intégrer avec des systèmes et technologies existants.
    

En résumé, les APIs REST sont un style architectural populaire et largement utilisé pour construire des services web et des APIs. Elles sont simples, évolutives et flexibles, et peuvent être utilisées pour construire une large gamme d'applications et de systèmes.

Bien qu'il y ait certaines limitations et préoccupations avec les APIs REST, elles restent une option populaire et efficace pour construire des APIs dans de nombreuses industries et secteurs différents.

## Comment consommer une API REST

Voici un exemple de la manière de faire une simple requête GET à une API REST à partir d'une application front-end JavaScript, et comment accéder aux valeurs dans la réponse :

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
  .then(response => response.json())
  .then(data => {
    console.log(data);
    // Accéder aux valeurs dans la réponse ici
  })
  .catch(error => console.error(error));
```

Voici ce que fait chaque ligne :

1. `fetch('https://jsonplaceholder.typicode.com/todos/1')` initie une requête GET à l'URL spécifiée.
    
2. `.then(response => response.json())` convertit la réponse du format JSON en un objet JavaScript.
    
3. `.then(data => { ... })` définit une fonction qui sera exécutée lorsque la réponse aura été convertie avec succès en un objet JavaScript. Cette fonction aura accès à l'objet JavaScript contenant les données de réponse.
    
4. `console.log(data);` enregistre les données de réponse dans la console. Vous pouvez inspecter les données de réponse pour déterminer comment accéder aux valeurs dans la réponse.
    

Pour accéder aux valeurs dans la réponse, vous pouvez utiliser des techniques standard de parcours d'objets JavaScript, telles que la notation par points ou la notation par crochets. Par exemple, si la réponse de l'API REST est dans le format suivant :

```javascript
{
  "userId": 1,
  "id": 1,
  "title": "delectus aut autem",
  "completed": false
}
```

Vous pouvez accéder à la valeur `title` en utilisant la notation par points ou par crochets comme ceci :

```plaintext
console.log(data.title); // sortie : "delectus aut autem"
console.log(data['title']); // sortie : "delectus aut autem"
```

Ici, `data` fait référence à l'objet JavaScript qui contient les données de réponse.

Les réponses des APIs REST sont généralement plus simples et plus légères que les réponses SOAP, et elles sont souvent formatées en JSON ou XML. L'utilisation de formats standard facilite l'analyse de la réponse par les clients et l'extraction des données pertinentes.

De plus, les APIs REST utilisent souvent des codes d'état HTTP standard pour indiquer le succès ou l'échec d'une requête, ce qui peut simplifier la gestion des erreurs côté client.

Dans l'ensemble, les APIs REST sont une approche populaire et largement utilisée pour construire des APIs web en raison de leur simplicité, de leur flexibilité et de leur facilité d'utilisation.

# Comment fonctionnent les APIs GraphQL

GraphQL est un langage de requête et un runtime pour les APIs qui a été développé par Facebook en 2012. Il a été rendu public en 2015 et a depuis gagné en popularité comme alternative aux APIs REST.

GraphQL a été développé à l'origine par Facebook comme un moyen de simplifier la récupération de données pour leurs applications mobiles. Ils avaient besoin d'un moyen de faire des requêtes de données complexes auprès du serveur sans causer de problèmes de performance ou de sur-récupération de données. GraphQL est né du besoin de résoudre ces problèmes.

GraphQL a été publié en tant que projet open-source en 2015 et a depuis gagné en popularité dans la communauté des développeurs. Il est maintenant supporté par de nombreux outils et frameworks de développement, y compris Apollo, Prisma et Hasura.

**Caractéristiques principales :**

1. **Typage fort :** Les APIs GraphQL sont fortement typées, ce qui signifie que chaque champ a un type de données spécifique. Cela facilite la validation et la gestion des données côté client et serveur.
    
2. **Langage de requête :** GraphQL a son propre langage de requête qui permet aux clients de spécifier exactement les données dont ils ont besoin. Cela réduit la sur-récupération de données et améliore les performances.
    
3. **Point de terminaison unique :** Les APIs GraphQL ont un point de terminaison unique, ce qui signifie que les clients peuvent récupérer toutes les données dont ils ont besoin à partir d'une seule requête.
    
4. **Déclaratif :** Les APIs GraphQL sont déclaratives, ce qui signifie que les clients spécifient ce qu'ils veulent, et non comment l'obtenir. Cela permet une récupération de données plus efficace et flexible.
    
5. **Basé sur le schéma :** Les APIs GraphQL sont basées sur le schéma, ce qui signifie que le schéma définit la structure des données et les requêtes et mutations disponibles. Cela facilite la compréhension et le travail avec l'API pour les développeurs.
    

**Avantages :**

* **Récupération de données efficace :** Les APIs GraphQL permettent aux clients de récupérer uniquement les données dont ils ont besoin, réduisant ainsi la sur-récupération et améliorant les performances.
    
* **Typage fort :** Les APIs GraphQL sont fortement typées, ce qui facilite la validation et la gestion des données.
    
* **Point de terminaison unique :** Les APIs GraphQL ont un point de terminaison unique, ce qui réduit la complexité de l'API et facilite son utilisation.
    
* **Basé sur le schéma :** Les APIs GraphQL sont basées sur le schéma, ce qui facilite la compréhension et le travail avec l'API pour les développeurs.
    

**Inconvénients :**

* **Complexité :** Les APIs GraphQL peuvent être plus complexes à configurer et à utiliser par rapport aux APIs REST.
    
* **Mise en cache :** La mise en cache peut être plus difficile avec les APIs GraphQL en raison de la nature flexible de l'API.
    
* **Courbe d'apprentissage :** GraphQL nécessite une courbe d'apprentissage pour les développeurs et les clients, car il a son propre langage de requête et son approche de la récupération de données.
    

**Idéal pour :**

* **Besoins efficaces et flexibles :** GraphQL est bien adapté pour construire des applications qui nécessitent une récupération de données efficace et flexible, telles que les applications mobiles et web.
    
* **Exigences de données complexes :** Il est particulièrement utile dans les situations où il y a des exigences de données complexes et où la sur-récupération de données peut causer des problèmes de performance.
    

En conclusion, GraphQL est un langage de requête et un runtime pour les APIs qui fournit des capacités de récupération de données efficaces et flexibles.

Bien qu'il puisse être plus complexe à configurer et à utiliser par rapport aux APIs REST, il offre des avantages tels que des données fortement typées, des points de terminaison uniques et un développement basé sur le schéma. Il est bien adapté pour construire des applications avec des exigences de données complexes et où la récupération efficace de données est importante.

## Comment consommer une API GraphQL

Voici un exemple de la manière de faire une simple requête pour récupérer des informations à partir d'une API GraphQL à partir d'une application front-end JavaScript, et comment accéder aux valeurs dans la réponse :

```javascript
fetch('https://api.example.com/graphql', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    query: `
      query {
        user(id: 123) {
          name
          email
          posts {
            title
          }
        }
      }
    `
  })
})
.then(response => response.json())
.then(data => {
  console.log(data);
  // Accéder aux valeurs dans la réponse ici
})
.catch(error => console.error(error));
```

Voici ce que fait chaque ligne :

1. `fetch('https://api.example.com/graphql', { ... })` initie une requête POST au point de terminaison de l'API GraphQL spécifié. Le deuxième argument de la fonction `fetch()` est un objet d'options qui spécifie la méthode HTTP, les en-têtes et le corps de la requête.
    
2. `method: 'POST'` spécifie que la méthode HTTP pour la requête est `POST`.
    
3. `headers: { 'Content-Type': 'application/json' }` spécifie l'en-tête `Content-Type` pour la requête, qui est `application/json` pour indiquer que le corps de la requête est au format JSON.
    
4. `body: JSON.stringify({ ... })` spécifie le corps de la requête sous forme de chaîne encodée en JSON. Dans cet exemple, le corps de la requête est une requête GraphQL qui récupère des informations sur un utilisateur avec l'ID `123`.
    
5. `.then(response => response.json())` convertit la réponse du format JSON en un objet JavaScript.
    
6. `.then(data => { ... })` définit une fonction qui sera exécutée lorsque la réponse aura été convertie avec succès en un objet JavaScript. Cette fonction aura accès à l'objet JavaScript contenant les données de réponse.
    
7. `console.log(data);` enregistre les données de réponse dans la console. Vous pouvez inspecter les données de réponse pour déterminer comment accéder aux valeurs dans la réponse.
    

Pour accéder aux valeurs dans la réponse, vous pouvez utiliser des techniques standard de parcours d'objets JavaScript, telles que la notation par points ou la notation par crochets. Par exemple, si la réponse de l'API GraphQL est dans le format suivant :

```javascript
{
  "data": {
    "user": {
      "name": "John Doe",
      "email": "john.doe@example.com",
      "posts": [
        { "title": "Post 1" },
        { "title": "Post 2" }
      ]
    }
  }
}
```

Vous pouvez accéder à la valeur `name` en utilisant la notation par points ou par crochets comme ceci :

```javascript
console.log(data.data.user.name); // sortie : "John Doe"
console.log(data['data']['user']['name']); // sortie : "John Doe"
```

Ici, `data` fait référence à l'objet JavaScript qui contient les données de réponse. Les données de réponse sont enveloppées dans un objet `data`, et les valeurs peuvent être accessibles en parcourant l'objet en utilisant la notation par points ou par crochets.

Les réponses des APIs GraphQL sont généralement plus ciblées et spécifiques que les réponses des APIs REST car le client peut spécifier exactement les données qu'il souhaite recevoir. Cela facilite l'éviter la sur-récupération ou la sous-récupération de données, et peut améliorer les performances en réduisant la quantité de données transférées sur le réseau.

De plus, les APIs GraphQL peuvent fournir un schéma plus flexible qui peut être facilement modifié au fil du temps sans casser les clients existants. Dans l'ensemble, les APIs GraphQL sont un choix populaire pour construire des applications web modernes en raison de leur flexibilité, de leur efficacité et de leur facilité d'utilisation.

# **Conclusion**

Eh bien, tout le monde, comme toujours, j'espère que vous avez apprécié l'article et appris quelque chose de nouveau.

Si vous le souhaitez, vous pouvez également me suivre sur [LinkedIn](https://www.linkedin.com/in/germancocca/) ou [Twitter](https://twitter.com/CoccaGerman). À la prochaine !

![Image](https://www.freecodecamp.org/news/content/images/2023/03/giphy.gif align="left")