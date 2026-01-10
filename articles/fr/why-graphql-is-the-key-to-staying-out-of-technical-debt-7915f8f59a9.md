---
title: Pourquoi GraphQL est la clé pour éviter la dette technique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-03-06T15:49:33.000Z'
originalURL: https://freecodecamp.org/news/why-graphql-is-the-key-to-staying-out-of-technical-debt-7915f8f59a9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*MGM-mwrfaPHWZIr0JiTKfA.png
tags:
- name: GraphQL
  slug: graphql
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Pourquoi GraphQL est la clé pour éviter la dette technique
seo_desc: 'By Burke Holland

  GraphQL (not to be confused with GraphDB or Open Graph or even an actual graph)
  is a remarkably creative solution to a relatively common problem: How do you enable
  front end developers to access backend data in exactly the way they n...'
---

Par Burke Holland

GraphQL (à ne pas confondre avec GraphDB ou Open Graph ou même un _vrai_ graphique) est une solution remarquablement créative à un problème relativement courant : **Comment permettre aux développeurs front-end d'accéder aux données back-end exactement comme ils en ont besoin ?**

Exemple rapide : Nous voulons afficher une liste de produits sur une page web. Nous écrivons donc un service qui retourne une liste de produits. Nous le rendons super RESTful parce que c'est ce que quelqu'un dans un podcast nous a dit de faire.

```js
{
    "items": [
        {
            "id": 2051,
            "name": "Cordon d'extension",
            "price": 15,
            "productType": "Électrique",
            "supplierName": "Northwind",
            "shortDescription": "La prise n'est pas là où vous en avez besoin ? Étendez votre alimentation au bon endroit au bon moment",
        },
        {
            "id": 2053,
            "name": "Lampe LED",
            "price": 14,
            "productType": "Matériel",
            "supplierName": "Northwind",
            "shortDescription": "Lumière à faible consommation fonctionnant sur batterie",
        }
    ]
}
```

Ensuite, nous affichons lesdits produits sur la page. Allez-y et imaginez un son de claque. Ou sentez-vous libre d'utiliser celui-ci...

%[https://soundcloud.com/acharus/slap-sound-effect]

![Image](https://cdn-media-1.freecodecamp.org/images/1*DPtCGHJIWOH2gZJi1ZApAw.png)

Maintenant que tout est fait, quelqu'un décide que nous devons également afficher la quantité de chaque produit en stock, bien sûr.

D'accord. Je suppose. Je veux dire, vous ne l'avez pas spécifié dans le document de projet original, mais pourquoi pas. Faisons en sorte que la portée soit ce que **vous** voulez qu'elle soit.

Les informations sur la quantité de produits sont un champ dans la base de données, mais il n'est pas retourné par le service. Pour y accéder depuis le front-end, nous devons modifier le code de notre service et ensuite le redéployer avant même de penser à apporter des modifications sur le front-end. Pour un seul champ.

De même, si cette même personne (qui ne semble pas pouvoir décider ce qu'elle veut vraiment dans la vie) décide que nous n'avons plus besoin du SKU, nous pouvons l'ignorer sur le front-end, mais il fait partie de la réponse de l'API, donc il finit par être des données inutiles dans la charge utile, et des bits inutiles que nos utilisateurs n'ont pas besoin.

**Chaque projet** est simplement cette série d'allers-retours de changements imprévus. C'est littéralement la définition de "Développement Logiciel". Je veux dire que ce n'est pas le cas, mais mon point semble meilleur si je référence un dictionnaire.

Le point est que nous finissons par faire beaucoup de compromis sur les fronts et les backs ends juste pour faire fonctionner les choses et suivre le rythme du changement. Et les compromis égalent la dette technique.

![Image](https://cdn-media-1.freecodecamp.org/images/0*LQSVhGCpmMOzBdSq.)

C'est l'essence même du problème que GraphQL essaie de résoudre.

Je n'ai que récemment assemblé toutes les pièces de GraphQL dans ma propre tête. Ce n'est pas avant que ma collègue [Simona Cotin](https://twitter.com/simona_cotin) se soit portée volontaire pour m'enseigner GraphQL que j'ai eu l'éclair de génie que c'est, peut-être, la réponse à un problème que j'ai essayé de contourner pendant la majeure partie de ma carrière professionnelle.

#### Apprenez GraphQL avec nous

Simona et moi avons fait trois sessions d'enseignement ensemble et nous avons enregistré chacune d'elles. Dans ces trois vidéos, vous pouvez apprendre avec moi alors que je passe de zéro connaissance sur GraphQL, à la mise en œuvre d'une interface GraphQL et ensuite à sa consommation depuis une application React.

Chaque vidéo est accompagnée d'un dépôt Github que vous pouvez cloner pour obtenir la solution complète fonctionnelle au cas où vous vous perdriez en chemin.

Nous utilisons beaucoup Azure Functions dans cette série de vidéos parce qu'il est beaucoup plus facile de construire une API Serverless que de commencer à partir de zéro. Obtenez un compte Azure gratuit si vous n'en avez pas déjà un.

[**Créez votre compte Azure gratuit aujourd'hui | Microsoft Azure**](https://azure.microsoft.com/free/?WT.mc_id=video-youtube-sicotin)  
[_Commencez avec 12 mois de services gratuits et 200 USD de crédit. Créez votre compte gratuit aujourd'hui avec Microsoft..._azure.microsoft.com](https://azure.microsoft.com/free/?WT.mc_id=video-youtube-sicotin)

### Partie 1 : Introduction à GraphQL

Dans la première vidéo, Simona m'introduit aux concepts de GraphQL et à la syntaxe particulière qu'il utilise. Nous créons également l'API GraphQL dans cette vidéo et la déployons.

%[https://youtu.be/x-imn__380s]

[**simonaco/serverless-graphql-apis-part1**](https://github.com/simonaco/serverless-graphql-apis-part1)  
[_Contribuez au développement de simonaco/serverless-graphql-apis-part1 en créant un compte sur GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part1)

### Partie 2 : Installation de Graphiql en local et déploiement

Dans la partie 2, je fais fonctionner l'outil de test visuel GraphQL [Graphiql](https://github.com/graphql/graphiql) localement sur ma propre machine, puis je le déploie sur [Azure Storage](https://code.visualstudio.com/tutorials/static-website/getting-started?WT.mc_id=freecodecamp-blog-sicotin) afin de pouvoir tester facilement mon API GraphQL sans avoir besoin de connecter une application.

%[https://youtu.be/X2846rUj_P8]

[**simonaco/serverless-graphql-apis-part2**](https://github.com/simonaco/serverless-graphql-apis-part2)  
[_Contribuez au développement de simonaco/serverless-graphql-apis-part2 en créant un compte sur GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part2)

### Partie 3 : Utilisation de l'API dans une application React

Nous terminons cette série en examinant comment appeler cette API depuis une application. C'est un détail plutôt important.

%[https://youtu.be/c2r_nUDUYe0]

[**simonaco/serverless-graphql-apis-part3**](https://github.com/simonaco/serverless-graphql-apis-part3)  
[_Contribuez au développement de simonaco/serverless-graphql-apis-part3 en créant un compte sur GitHub._github.com](https://github.com/simonaco/serverless-graphql-apis-part3)

#### En savoir plus sur GraphQL

Une fois que vous comprenez le problème que GraphQL résout, vous commencerez à voir des opportunités pour l'utiliser partout. Et le meilleur, c'est que vous n'avez pas besoin de commencer à partir de zéro pour l'utiliser. En fait, il est _recommandé_ de l'utiliser par-dessus une API REST typique, donc vous êtes probablement dans la position parfaite pour utiliser GraphQL aujourd'hui.

Si vous voulez aller plus loin avec GraphQL et React, consultez le cours de [Wes Bos](https://twitter.com/wesbos). Il est payant, mais il en vaut chaque centime. C'est un investissement dont vous serez content d'avoir fait. Wes ne me paie rien pour dire cela. Mais peut-être qu'il devrait.

[**Advanced React & GraphQL**](https://advancedreact.com/)  
[_Construisez des applications Full Stack avec React et GraphQL_advancedreact.com](https://advancedreact.com/)