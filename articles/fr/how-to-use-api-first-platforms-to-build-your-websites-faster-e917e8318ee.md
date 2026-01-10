---
title: Comment utiliser les plateformes API-first pour construire vos sites web plus
  rapidement
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-01-04T07:45:48.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-api-first-platforms-to-build-your-websites-faster-e917e8318ee
coverImage: https://cdn-media-1.freecodecamp.org/images/1*6T2sSRtPdHIgyrUCeOnVoA.jpeg
tags:
- name: api
  slug: api
- name: Developer Tools
  slug: developer-tools
- name: software architecture
  slug: software-architecture
- name: software development
  slug: software-development
- name: Web Development
  slug: web-development
seo_title: Comment utiliser les plateformes API-first pour construire vos sites web
  plus rapidement
seo_desc: 'By Mike Sedzielewski

  Tools like Jekyll, Hugo, or Hexo have popularized static websites in recent years.
  The so-called JAMstack allows you to deliver highly dynamic content with no back-end
  layer at all. Additionally, developer-first APIs enabled fron...'
---

Par Mike Sedzielewski

Des outils comme [Jekyll](https://jekyllrb.com/), [Hugo](https://gohugo.io/), ou [Hexo](https://hexo.io/) ont popularisé les sites web statiques ces dernières années. La soi-disant [JAMstack](https://jamstack.org/) vous permet de fournir un contenu hautement dynamique sans aucune couche back-end. De plus, les API orientées développeurs ont permis aux développeurs front-end de construire des fonctionnalités encore plus complexes. Tout cela peut être fait sans quitter le bac à sable du navigateur. Voyons comment vous pouvez tirer parti des plateformes API-first modernes pour livrer un prototype solide d'une application métier. L'approche présentée dans cet article pourrait devenir un atout utile dans la boîte à outils de votre architecte de solutions.

Le tutoriel se compose de 2 parties :

* La première vous montrera comment concevoir l'application pour obtenir un soi-disant chemin heureux. Nous construirons un prototype semi-automatisé que vous pouvez utiliser pour obtenir des commentaires des utilisateurs lors d'une session de démonstration.
* La seconde explique comment automatiser les processus métiers afin que l'application puisse gérer le trafic initial en production.

### Qu'est-ce qu'une plateforme API-first ?

Comme Ed Shelley de [ChartMogul](https://chartmogul.com/) le décrit, il y a quelques caractéristiques plutôt difficiles à manquer pour un tel service :

* _Il n'y a PAS d'interface utilisateur (GUI). Ou dans certains cas, il y a une GUI mais elle est secondaire par rapport au produit principal._
* _L'interaction avec le service se fait via une API basée sur le web. Il s'agit d'une manière programmatique de connecter des services et de transférer des données sur le web de manière lisible par une machine._
* _La valeur du service réside généralement dans les données qui sont livrées (via l'API)._
* _Le prix est souvent basé sur l'utilisation, ce qui signifie que le coût est basé sur le nombre de requêtes faites à l'API._

En gros, ce qu'ils offrent est un ensemble de blocs de construction, généralement dans le modèle SaaS. Ceux-ci vous pouvez utiliser pour construire une fonctionnalité spécifique avec moins de code. L'un des premiers et probablement des plus notables représentants de cela est [Stripe](https://stripe.com). Stripe aide à traiter les paiements. Cependant, vous avez peut-être entendu parler d'autres gros poissons récemment émergés du marché, comme [Twilio](https://www.twilio.com/) ou [Algolia](https://www.algolia.com/).

### Pourquoi utiliser une plateforme API-first ?

Commençons par un petit avertissement. Ce tutoriel décrit comment développer des applications sans aucun serveur. Cependant, nous ne pensons pas que ce soit une approche pragmatique de l'architecture logicielle.

Plutôt, nous voulons mettre en évidence certaines parties de votre mécanique back-end que vous n'avez pas besoin d'implémenter à partir de zéro. Cela est particulièrement vrai **lorsque les exigences métiers pour une fonctionnalité particulière ne sont pas gravées dans le marbre** et que votre objectif est de les déterminer. En d'autres termes, pour savoir si la fonctionnalité reçoit une réponse positive des utilisateurs et a éventuellement une place dans votre produit.

En même temps, vous ne voulez pas verrouiller votre produit avec un fournisseur proposant une solution clé en main. Cela est dû au fait que vous savez que cela conduira à un "enfer de contournement" tôt ou tard. Et, comme vous l'avez appris, il est difficile de revenir de là.

Pour vous donner un exemple, imaginez que votre entreprise veut construire un blog. De plus, ils ont déjà déclaré qu'ils veulent l'étendre et le monétiser à l'avenir. Il y a 2 exigences implicites que vous devez prendre en considération avant de proposer une stack technique dans un tel scénario :

* Vous voulez livrer la fonctionnalité de blog rapidement — le business ne peut pas attendre des âges pour un simple blog.
* Vous ne voulez pas vous retrouver à jongler avec les plugins Wordpress.

Le type d'outils que nous voulons présenter pourrait être la réponse. Ils vous donnent quelques blocs de construction fonctionnels et votre seule tâche est de les adapter à votre entreprise.

Vous êtes heureux parce que vous avez un contrôle total sur votre base de code. De plus, la direction est également heureuse car elle obtient de la valeur dès le premier jour. De plus, ils n'ont pas à payer à l'avance !

Alors, laissez-nous maintenant vous montrer comment ces outils peuvent économiser des semaines de temps d'ingénierie tout en gardant votre base de code ouverte aux changements.

**Note :** Les outils que nous allons utiliser fonctionnent également en mode serveur. Ils offrent en fait plus de fonctionnalités lorsqu'ils sont connectés en utilisant des clés API sécurisées. Nous pensons donc qu'il est plus pragmatique de l'avoir intégré côté serveur. Néanmoins, en tant qu'expérience, nous utiliserons uniquement la fonctionnalité côté client. De plus, nous utiliserons un peu de [Zapier](https://zapier.com/) pour automatiser rapidement différents processus métiers.

### nostalgia.io

Nous allons construire une place de marché pour les consultants en technologies web héritées — nostalgia.io. Si par hasard vous cherchez de l'aide pour un ancien système basé sur Struts ou Google Web Toolkit, c'est l'endroit où aller. Dans la première partie de ce tutoriel, nous apprendrons comment tirer parti de plusieurs plateformes API-first pour livrer les fonctionnalités suivantes :

* Navigation à travers les technologies héritées
* Recherche en texte intégral et filtrage des experts
* Réservation de réunions avec des experts
* Application de réductions avec des coupons

La stack technique comprendra :

* [Contentful](https://www.contentful.com/) — comme base de données pour les technologies et les experts
* [Algolia](https://www.algolia.com/) — pour la recherche en texte intégral
* [Timekit](https://www.timekit.io/) — pour la vérification de la disponibilité et la réservation
* [Typeform](https://www.typeform.com/) — pour les formulaires
* [Voucherify](https://www.voucherify.io/) — pour la gestion des coupons (avertissement : c'est notre produit)

**Note :** Nous ne couvrirons pas l'authentification et le traitement des paiements eux-mêmes. Vous pouvez essayer de les implémenter vous-même comme devoir (indice : [auth0](https://auth0.com/) et [Stripe](https://stripe.com) pourraient être utiles).

Plongeons dans le code.

**Note 1 :** pour plus de concision, nous ne décrirons pas un guide détaillé étape par étape. Vous devriez chercher les parties manquantes dans les spécifications — heureusement, les fournisseurs API-first ont tendance à avoir des docs conviviales pour les développeurs, une référence API complète et des dizaines de guides utiles.

**Note 2 :** il existe de nombreuses façons d'héberger votre site web statique. Nous utiliserons la plateforme de développement [glitch](https://glitch.com) afin que vous puissiez facilement la [remixer](https://glitch.com/about/) et jouer avec elle vous-même.

**Note 3 :** nous ne nous soucions pas de l'apparence de l'application pour ne pas obscurcir la partie intégration, et cela correspond quelque peu au thème de l'entreprise, n'est-ce pas ? :)

### Modèle de données — Contentful

Habituellement, la conception de l'application commence par un modèle de relation de données. Cela devrait être notre première préoccupation. Mais sautons la discussion sur les fournisseurs de bases de données pour un moment et passons directement aux modèles. Comment cela ?

Rencontrez [Contentful](https://www.contentful.com/) — un CMS sans tête. En utilisant une simplification marquée, vous pouvez le considérer comme un Wordpress sans front-end.

Il permet :

* **aux développeurs** de livrer le contenu ajusté au support, qu'il s'agisse d'un site web, d'une application mobile ou d'un appareil VR — cela est fait via une API RESTful
* **aux marketeurs** de créer, gérer et publier du contenu sans avoir à traiter le formatage — avec le support du tableau de bord de modélisation de contenu et de l'éditeur de texte enrichi

Nous utiliserons Contentful pour créer 2 entités de base — Technologie et Expert. Un Expert connaît une ou plusieurs Technologies. Voyons à quel point il est facile de créer de telles entités, d'ajouter quelques objets réels et de les afficher sur une page statique.

### Navigateur de technologies

Avec le gestionnaire de modèles de Contentful, la conception d'une entité est aussi simple que de glisser-déposer de nouveaux champs dans le gestionnaire de modèle de contenu de données. Il existe 8 types différents. Ceux-ci incluent les types par défaut, comme une chaîne ou un nombre. Il y a aussi des types spécifiques, comme Localisation ou Média, qui viennent avec des propriétés utiles.

![Image](https://cdn-media-1.freecodecamp.org/images/1*lKRyvvSWtYX8R1VkRpdvsQ.png)

Créez un compte gratuit. Ensuite, suivez le guide d'intégration pour créer un espace.

Enfin, créez votre premier modèle, similaire à ce que vous pouvez voir dans la capture d'écran ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*oeOvlrFC7In9Eqtrq_ydaQ.png)

Maintenant que vous avez le modèle Technologie, allez dans l'onglet Contenu pour créer quelques instances. Comme vous pouvez le voir, Contentful fournit un éditeur intuitif pour la saisie de données. Il prend en charge la validation des données, la localisation, le statut de publication, le contrôle de version, et bien plus encore. C'est avant tout une plateforme orientée développeurs. Pourtant, ces fonctionnalités satisfont également les marketeurs et les gestionnaires de contenu.

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZnSZwdmKWRIB4miEM36Vlw.png)

Assez de clics, passons au codage. La première tâche est d'afficher les technologies que nous venons de créer. Pour ce faire, nous utiliserons le SDK JavaScript de Contentful.

Il facilite la récupération des technologies et se résume à 3 étapes :

* Créez un nouveau projet de site web [glitch](https://glitch.com), chargez le script `contentful.js` et initialisez-le avec les identifiants que vous pouvez trouver dans la section API.

**Note :** il existe 2 types de clés disponibles dans Contentful. L'une est pour la gestion de contenu et l'autre est pour la livraison de contenu.   
Le premier type peut être utilisé pour créer, mettre à jour ou supprimer de nouveaux modèles ou leurs instances de manière programmatique.  
Le second vous donne un moyen de livrer votre contenu à votre site web ou à votre application.  
Cette distinction a été faite pour des raisons de sécurité. Vous ne voulez pas publier vos clés de gestion de contenu sur votre site web, n'est-ce pas ? La même chose s'applique aux autres plateformes API-first que nous utilisons dans ce tutoriel.

* Appelez la méthode [getEntries](https://contentful.github.io/contentful.js/contentful/5.0.5/ContentfulClientAPI.html#.getEntries). Cela charge le contenu selon vos paramètres de requête. Dans notre cas, nous voulons charger uniquement les entités « Technologie ». Construisez un front-end sur les données. Ce que vous obtenez de Contentful est du JSON pur ([exemple](https://gist.github.com/sedzia/56d83d61c35720ecdbe7302c53154888)). Maintenant, vous pouvez l'afficher à vos utilisateurs comme vous le souhaitez. C'est l'un des plus grands avantages lorsque vous voulez ou devez adapter votre contenu à plusieurs appareils.

Jetez un coup d'œil à ce gist :

```js
const client = contentful.createClient({
    space: SPACE_ID,
    accessToken: ACCESS_TOKEN
  })
    
  const techCards = document.querySelector('#cards');

  function fetchTechnologies () {
    return client.getEntries({
        content_type: "technology"
      })
    .then((response) => response.items)
    .catch((error) => {
      console.log(`\nError occurred while fetching Entries for Technology:`)
      console.error(error)
    })
  }

  fetchTechnologies().then((technologies) => {
    techCards.innerHTML += technologies.map(technology => 
      `<div class="col-md-4">
        <div class="card">
          <a href="${technology.fields.link}"><img src="${technology.fields.logo.fields.file.url}"/></a>
          <h2><a href="/experts.html?t=${technology.fields.name}">${technology.fields.name}</a></h2>
          <p>${technology.fields.description}</p>
        </div>
      </div>`).join('')
  })
```

Court et doux, n'est-ce pas ? Vous pouvez voir l'effet global [ici](https://glitch.com/edit/#!/meteor-rooster?path=index.html).

### Ajout d'experts et recherche

Nous voulons maintenant afficher la liste des experts lorsqu'une personne choisit une technologie particulière. Cela devrait être similaire à ce que nous venons de faire avec la Technologie il y a une seconde. Mais faisons-le un peu plus avancé. Que se passe-t-il si nous voulons rendre les experts recherchables ? Pensez à la recherche en texte intégral dans leurs profils et aussi à un filtre de prix.

Certes, vous pouvez le construire sur Contentful. Par exemple, ajoutez une autre entité, configurez les mécanismes de recherche et l'interface utilisateur avec `getEntries`, mais il y a une manière plus rapide. Et en disant plus rapide, je veux dire à la fois en temps d'implémentation et en vitesse de chargement des résultats de recherche.

Nous utiliserons un autre fournisseur d'API — [Algolia](https://www.algolia.com/). Leur plateforme facilite la construction et la maintenance d'une recherche en texte intégral ultra-rapide. Ils prennent en charge la tolérance aux fautes de frappe, les synonymes, la géorecherche et autres petits problèmes. Ces problèmes que vous rencontreriez probablement lorsque votre fonctionnalité de recherche passe en production.

Comment cela fonctionne-t-il ? Vous utilisez simplement une API RESTful pour alimenter leur moteur avec les données. Ensuite, vous configurez quels attributs doivent être recherchables et comment les résultats doivent être classés. Enfin, en utilisant leur SDK JavaScript, vous pouvez offrir l'expérience de recherche instantanée à n'importe quel site web. Rendons nos experts recherchables maintenant !

Nous commencerons par créer un modèle de données dans Contentful et établir une relation avec l'entité Technologie. Ensuite, nous construirons un index Algolia et ajouterons nos entités (format JSON) à celui-ci.

Ajoutez un autre modèle de contenu avec les champs que vous pouvez voir ci-dessous :

![Image](https://cdn-media-1.freecodecamp.org/images/1*Qq8QlKi9kx1j6T6cmasC9g.png)

Remarquez que nous avons fait des relations un-à-plusieurs en utilisant le type de champ Référence. Nous voulons simplement refléter qu'un expert peut connaître plus d'une technologie. Une fois prêt, ajoutez quelques experts et assignez-les à leurs technologies manuellement. Utilisez plusieurs technologies pour l'un des experts.

Vous devriez obtenir une liste similaire :

![Image](https://cdn-media-1.freecodecamp.org/images/1*OsClINqbZQt9BKiMFw9UkA.png)

Et la structure JSON ressemble à ceci :

```json

{
   "sys":{
      "space":{
         "sys":{
            "type":"Link",
            "linkType":"Space",
            "id":"n763nxcwuf4y"
         }
      },
      "id":"1mn1mwlwAcQWqgQamsIEmW",
      "type":"Entry",
      "createdAt":"2017-12-05T11:29:35.202Z",
      "updatedAt":"2017-12-13T10:04:52.381Z",
      "revision":7,
      "contentType":{
         "sys":{
            "type":"Link",
            "linkType":"ContentType",
            "id":"expert"
         }
      },
      "locale":"en-US"
   },
   "fields":{
      "name":"Javier Hernandez",
      "technologies":[
         {
            "sys":{
               "type":"Link",
               "linkType":"Entry",
               "id":"5oKmKwfdjGO2cCaCkwamKW"
            }
         },
         {
            "sys":{
               "type":"Link",
               "linkType":"Entry",
               "id":"7Dtej0GnXqw6cSIMmA6Cko"
            }
         }
      ],
      "image":{
         "sys":{
            "type":"Link",
            "linkType":"Asset",
            "id":"4RZoQOCwvCMEWMMCuqA0ey"
         }
      },
      "description":"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Sed faucibus turpis in eu mi bibendum. Mauris in aliquam sem fringilla ut. Tincidunt nunc pulvinar sapien et ligula. ",
      "projects":53,
      "price":40,
      "city":{
         "lon":2.2247314453125,
         "lat":41.36933709640475
      }
   }
}
```

Chargeons nos experts dans Algolia. Inscrivez-vous pour un compte gratuit, allez dans la section Indices et exécutez `NOUVEL INDEX`.

Maintenant, nous devons transférer nos entités de Contentful vers Algolia. Nous aurions pu utiliser un migrateur dédié. C'est un outil fantastique qui charge automatiquement votre contenu. Il supprime ensuite, dans ce cas redondant, les informations système de Contentful (voir le gist ci-dessus) des JSON effectifs. Il peut également résoudre les relations. Par exemple, au lieu d'ID, vous enverrez les noms réels lorsqu'il s'agit du champ « technologies ». Enfin, il se synchronise avec l'index Algolia.

Mais nous allons le faire manuellement. Nous avons besoin d'une petite amélioration dans la manière dont nous construisons notre index. Par conséquent, la synchronisation un-à-un avec le migrateur n'est pas une option dans notre cas.

Lorsque nous utilisons une entrée de recherche dans un site de technologie, naturellement nous voulons inclure uniquement les experts de la technologie choisie dans les résultats de recherche. Comme vous pouvez le voir dans l'exemple JSON de l'expert, les technologies sont représentées sous forme de tableau d'objets. Le problème est que vous ne pouvez pas construire une facette qui filtre les données en fonction d'un tableau imbriqué d'objets avec Algolia.

Ce qu'ils suggèrent est de diviser l'objet expert en autant de sous-objets que le nombre de technologies. Donc, dans le cas de Javier Hernandez, qui connaît 2 frameworks, nous devrions ajouter 2 objets :

```json
{
  name: "Javier Hernandez", 
  technologies: { 
    name: "Google Web Toolkit"
    … // autres propriétés
  }
  … // autres propriétés
} 
{
  name: "Javier Hernandez" 
  technologies: { 
    name: "Apache Struts 1"
    … // autres propriétés
  }
  … // autres propriétés
}
```

En tant qu'exercice, vous pouvez créer un script qui divise les experts et les ajoute à l'index via l'API Algolia. Vous aurez besoin des clés d'authentification côté serveur d'Algolia. Voici un extrait qui gère la logique de division. Remarquez que le script supprime également les informations système de Contentful.

Cela rend les objets plus légers et rendra la recherche plus rapide :

```js
client.getEntries({ content_type: "expert" })
  .then((response) => {

    const denormalized = [].concat(...response.items.map(item => {
      let arr = []
      
      item.fields.contentfulID = item.sys.id
      delete item.sys

      item.fields.technologies.forEach(tech => {
        const i = JSON.parse(JSON.stringify(item))
        i.fields.technologies = tech.fields
        i.fields.image = item.fields.image.fields
        arr.push(i.fields)
      })
      return arr
    }))
    console.log(JSON.stringify(denormalized))
  })
  .catch((error) => {
    console.log(`\nError occurred while fetching Entries for Expert:`)
    console.error(error)
  })
```

Comme nous avons 6 experts et que 2 d'entre eux connaissent 2 technologies, nous devrions obtenir 8 objets dans l'index. En alternative à la méthode d'insertion API, vous pouvez les télécharger avec le tableau de bord. Une fois téléchargés, vous pouvez essayer d'utiliser la recherche dans le tableau de bord pour voir à quelle vitesse Algolia filtre les données.

![Image](https://cdn-media-1.freecodecamp.org/images/1*B2JuHiQdwdCpUDZYxRStXA.png)

Maintenant, nous sommes presque prêts à connecter notre recherche à Algolia. Presque — car nous devons créer une facette qui nous permettra de filtrer les résultats par technologie et prix. Allez dans AFFICHAGE et sélectionnez `technology.name` et `price` dans « Attributs pour facettage », puis Enregistrez.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9rKcjASE_hiv3RSYX15Y4w.png)

Enfin, nous pouvons connecter notre recherche à notre index afin qu'elle récupère et affiche les résultats. Algolia est livré avec une bibliothèque JavaScript avancée qui rend cela facile comme bonjour.

Jetez un coup d'œil à ce code :

```js
const isConfig = {
    appId: 'N675AF3ESI',
    apiKey: '14b65c352deb9a505131d3d00cba2f6c',
    indexName: 'experts',
    urlSync: false
  }
  
isConfig.searchParameters = {
  filters: `technologies.name:"${selectedTechnology}"`
}

const search = instantsearch(isConfig)

search.addWidget(
  instantsearch.widgets.searchBox({
    container: '#search-input'
  })
)

search.addWidget(
  instantsearch.widgets.hits({
    container: '#hits',
    hitsPerPage: 10,
    templates: {
      item: document.getElementById('hit-template').innerHTML,
      empty: "We didn't find any results for the search <em>\"{{query}}\"</em>"
    },
    cssClasses: {
      root: 'row',
      item: 'col-md-4'
    }
  })
)

search.addWidget(
  instantsearch.widgets.rangeSlider({
    container: '#price-refinement',
    attributeName: 'price',
    tooltips: {
      format: function(rawValue) {
        return '$' + Math.round(rawValue).toLocaleString();
      }
    }
  })
)

search.start()
```

Remarquez comment nous configurons la recherche pour utiliser le filtre de technologie aux lignes 8–10. Voyez à quel point il est facile d'ajuster la page de résultats à un conteneur respectif — ligne 28 (bien que ce soit difficile à trouver dans les docs).

Dans l'ensemble, avec environ deux douzaines de lignes, vous obtenez ceci :

<iframe src="https://giphy.com/embed/3o751QR0q4ELZfyICs" width="480" height="276" frameBorder="0" class="giphy-embed" allowFullScreen></iframe>

Jusqu'à présent, nous avons construit un simple navigateur d'experts prenant en charge la recherche en texte intégral et les curseurs de prix. L'ajout de nouveaux experts est fastidieux à ce stade car vous devez d'abord les créer manuellement dans Contentful puis les synchroniser avec Algolia. Nous automatiserons cela dans la deuxième partie.

La bonne nouvelle est que vous pouvez déjà utiliser ce prototype pour obtenir des commentaires précoces sur la navigation des technologies et le filtrage des experts. L'étape suivante consiste à créer la page de profil de l'expert et à activer la réservation.

Le code de démonstration de recherche peut être trouvé dans [experts.html](https://glitch.com/edit/#!/nostalgia?path=experts.html).

### Réservations

Comme vous l'avez peut-être deviné, nous n'implémenterons pas non plus la fonctionnalité de calendrier à partir de zéro. Nous utiliserons [Timekit](https://www.timekit.io/). Ils offrent l'API + le tableau de bord pour gérer les calendriers et les réservations pour les personnes et les ressources. Pensez-y comme à un moteur de calendrier Google/Outlook exposé avec une API REST.

Le processus de rendre les experts réservables avec Timekit est le suivant :

* Créez une entité Ressource et une entité Calendrier assignée
* Stockez les ID de la ressource et du calendrier dans l'entité expert correspondante dans Contentful
* Utilisez le SDK JS de Timekit pour afficher le calendrier sur la page de profil d'un expert

Et c'est tout, vous venez de mettre en place les réservations ! Vous ne me croyez pas ? Lisez la suite :

* Créez un compte et commencez un [essai gratuit](https://www.timekit.io/) (il n'y a pas de version gratuite).
* Créez un Projet dans lequel vous définirez les mécanismes de base du calendrier. Par exemple, la durée de l'événement, le préavis minimum et les rappels.
* Définissez si les demandes de réservation doivent être acceptées automatiquement ou doivent être confirmées manuellement.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Bb_JKj1_bMeayT7BjAb-3A.png)

Pour chaque expert, créez une ressource et, au sein de cette ressource, créez un calendrier. Remarquez qu'une ressource peut avoir plus d'un calendrier.

C'est une fonctionnalité intéressante à garder à l'esprit lorsque nous planifions certaines mises à niveau dans le modèle économique de Nostalgia.

![Image](https://cdn-media-1.freecodecamp.org/images/1*kXLZEwb6pa_ZTJYjKGaMsw.png)

Maintenant, nous devons stocker l'email de la ressource, l'ID du calendrier nouvellement créé et la clé API côté client dans l'entité expert correspondante dans Contentful.

Vous pouvez modifier le modèle de contenu de l'expert et ajouter un champ JSON nommé `timekit`. Ensuite, modifiez les entités expert pour ajouter les détails `timekit`.

La dernière étape consiste à afficher le calendrier réel dans la page de profil de l'expert. Vous connaissez déjà le processus. Incluez un script SDK et configurez-le correctement pour rendre le widget.

Mais cette fois, nous devons charger 2 bibliothèques :

* Contentful — pour charger les détails des clients, y compris les identifiants Timekit
* Timekit — pour placer le calendrier assigné à un expert donné

![Image](https://cdn-media-1.freecodecamp.org/images/0*t-RhbQuc-QEVo1sr.)

Voici le code :

```js
const widget = new TimekitBooking()
  
const client = contentful.createClient({
  space: SPACE_ID,
  accessToken: ACCESS_TOKEN
})

client.getEntries({'sys.id': expertId}).then((response) => {
  const e = response.items[0].fields

  expertWidget.innerHTML=
  `
  <div class="row card hit">
    <div class="col-md-4">
        <div class="hit-image">
          <img style="height: 5em" src="${e.image.fields.file.url}" alt="${e.name}">
          <h2 class="hit-name">${e.name}</h2>
          <h2 class="hit-price">$<span id="priceTag">${e.price}</span></h2>
        </div>
    </div>
    <div class="col-md-8 start-xs">
        <div class="hit-content">
          <h4 class="hit-price">projects: ${e.projects} </h4>
          <p class="hit-description">${e.description}</p>
        </div>
    </div>
  </div>
  `

  const timekitConf = e.timekit

  widget.init({
      targetEl: '#bookingjs',
      app:      'nostalgia-4592',
      apiToken: timekitConf.apiToken,
      email:    timekitConf.email,
      calendar: timekitConf.calendar,
      name:     'Jane Doe',
      timekitFindTime: {
        length: '3 hours',
        start: 'tomorrow',
        filters: {
          and: [
            { specific_time: { start: '8', end: '17' }}
          ]
        }
      },
      fullCalendar: {
        defaultView: 'month'
      }
    })    

})
.catch((error) => {
  console.log(`\nError occurred while fetching Entries for Expert:`)
  console.error(error)
})
```

Remarquez comment nous pouvons ajuster les détails de la réservation tels que les créneaux horaires (ligne 39). Timekit offre encore plus de capacités de personnalisation, alors assurez-vous de lire la spécification [booking.js](https://github.com/timekit-io/booking-js).

L'effet nous souffle. Vingt lignes de code et nous avons notre widget de réservation en place. Timekit supervise l'ensemble du processus pour vous. Il aide à résoudre les conflits et envoie des confirmations par e-mail aux experts et aux clients.

La chose la plus importante est que cette approche est hautement flexible. Tout est dans le code. Chaque partie de ce mécanisme peut être ajustée via l'API.

Par exemple, supposons que nous voulons examiner une demande de réservation avant de l'accepter. Il se trouve que Timekit le rend possible avec un seul drapeau. De telles options sont la véritable puissance des solutions API-first. Assurez-vous de lire les tutoriels et les docs pour apprendre toutes les fonctionnalités.

### Coupons

Nostalgia n'est pas encore une entreprise bien connue. Nous devons trouver un moyen d'attirer les premiers adopteurs. L'une des méthodes les plus anciennes et les plus réussies est les réductions. Une réduction peut être appliquée soit après avoir échangé un coupon, soit en raison du volume de produits dans le panier. Pour implémenter les deux cas, vous pourriez vouloir utiliser [Voucherify](https://www.voucherify.io/).

Pourquoi Voucherify ? Il y a quelques choses de base que vous devez faire correctement lorsque vous voulez gérer les coupons correctement pour économiser des tonnes de temps d'ingénierie :

* Unicité des codes de coupon — Pour réduire la fraude et obtenir un suivi précis de vos campagnes promotionnelles
* Mécanisme de validation de coupon extensible — Il s'agit d'une approche générique qui permet d'ajouter/supprimer/expirer plusieurs codes de coupon
* Surveillance facile de l'échange — Cela répondra aux questions des départements marketing et service client dès le départ

Vous pouvez prendre soin de ces 3 choses vous-même. Cependant, vous pouvez obtenir le même résultat avec quelques lignes en utilisant les points de terminaison de l'API Voucherify. En faisant cela, vous pouvez immédiatement oublier l'utilisation abusive de coupons, maintenir l'échelle « si » validant si le code est actif et valide. Vous pouvez également éviter de fournir aux équipes marketing les résultats des campagnes de coupons. Ni ne devrez-vous creuser dans les journaux pour comprendre pourquoi l'échange d'un client a échoué.

Créons un lot de 1000 coupons. Ceux-ci, nous les enverrons à nos premiers adopteurs. Enfin, donnons aux clients la possibilité de les utiliser réellement sur notre site web pour profiter de prix réduits.

Inscrivez-vous à un compte Voucherify et allez dans le [gestionnaire de campagne](http://support.voucherify.io/article/17-how-do-i-create-my-first-campaign) pour créer le premier lot de codes de coupon. Disons que chaque coupon offre 25 % de réduction.

Dans le gestionnaire, vous pouvez spécifier les détails de la réduction et d'autres limites commerciales. Par exemple, spécifiez la date d'expiration, le montant total maximum ou un segment de clients spécifique éligible à la réduction.

![Image](https://cdn-media-1.freecodecamp.org/images/1*REoy3OlagtuWrQcV81MXZA.png)

Lorsque le gestionnaire est terminé, vous pouvez commencer à distribuer des coupons via divers canaux. Voucherify offre des e-mails, des SMS, des notifications push, intercom ou braze prêts à l'emploi. Mais il existe de nombreuses autres façons disponibles grâce à l'API REST et aux webhooks.

Avant de les envoyer, vous devriez donner aux clients une option pour les échanger. Cela peut être réalisé en utilisant le point de terminaison [redemption](https://docs.voucherify.io/reference#redeem-voucher) de l'API. Pourtant, vous pouvez également utiliser le widget pré-construit de [voucherify.js](https://github.com/rspective/voucherify.js).

![Image](https://cdn-media-1.freecodecamp.org/images/1*b_RjBXbyhxI1QmQN600A0w.gif)

Voucherify vous permet soit de valider, soit d'échanger le coupon.

La validation vérifie si :

* le coupon provient de votre compte Voucherify
* il n'est pas expiré ou désactivé
* il correspond à toutes les règles commerciales

L'échange effectue la validation en premier et **ensuite** **marque le coupon comme utilisé**. Dans cette partie, nous allons intégrer la validation uniquement pour montrer aux clients un prix réduit. Dans le deuxième article, nous enverrons une demande d'échange lorsque la réservation est confirmée.

Incluez l'extrait `voucherify.js` et éventuellement le fichier CSS correspondant pour une meilleure apparence. Ensuite, mettez le code suivant :

```js
Voucherify.initialize(
    "4dde7477-d8d1-4057-8f91-8a9e7137acee",
    "404c6c0b-4445-4f14-84b1-f4a58f1da2f6"
)

Voucherify.render("#voucher-widget", {
    textPlaceholder: "Your coupon...",
    onValidated: function(response) {
      if (response) {
        const priceTag = document.querySelector('#priceTag') 
        priceTag.innerHTML = Voucherify.utils.calculatePrice(parseInt(priceTag.innerHTML), response)
      }
    }
})
```

La bibliothèque rendra un widget de coupon qui valide automatiquement le code par rapport à l'API Voucherify.

Vous pouvez le tester avec les codes que nous avons pré-générés avec le gestionnaire de campagne :   
* 25 % de réduction : _nstlg-CCAMIDFf, nstlg-wZK4CoLs, nstlg-V8eV9A3p_  
* 5 $ de réduction : _uub-nstlg, afl-nstlg, yeq-nstlg_  
_*_ code expiré : _VuFF2Wyy_

Remarquez que vous pouvez facilement personnaliser les motifs de codes, les préfixes et les suffixes peuvent être utiles pour le suivi et la reporting.

![Image](https://cdn-media-1.freecodecamp.org/images/1*9LQC64sGNxoYoH7f7LUFJA.png)

Maintenant, collez n'importe quel code de coupon dans le widget et voyez la réduction correspondante appliquée :

![Image](https://cdn-media-1.freecodecamp.org/images/1*J0-_vtjHA8vJy8bGgpLlDQ.png)

Dans la 2ème partie, nous vous montrerons comment surveiller les échanges de coupons réussis et échoués pour voir si votre campagne promo est sur la bonne voie.

Voucherify offre bien plus que cela. Consultez les [docs](https://docs.voucherify.io) et les [exemples](http://docs.voucherify.io/docs/examples) pour découvrir comment construire des promotions avancées et des programmes de parrainage en quelques jours au lieu de mois.

Vous pouvez trouver le code de la page de réservation ici ([scheduler.html](https://glitch.com/edit/#!/nostalgia?path=scheduler.html)).

### Récapitulatif

Nous avons prévu de construire une preuve de concept pour une nouvelle application métier — Nostalgia.io. Un prototype que nous pouvons utiliser pour sonder les premiers utilisateurs. Quelque chose que nous pouvons livrer dans un délai décent, mais pas un jetable total.

Espérons que nous vous avons convaincu qu'avec des outils orientés développeurs comme **Contentful**, **Algolia**, **Timekit**, ou **Voucherify**, vous pouvez y parvenir. Plus important encore, vous pouvez le faire sans configurer aucune couche back-end.

Cela nécessite encore un peu de travail manuel pour garder les données synchronisées entre les outils. Pourtant, la flexibilité et la vitesse d'itération de ces outils API-first à votre disposition compensent définitivement cela.

Certes, ces outils ne sont pas tous légers et brillants. Par exemple, nous avons rencontré ces quelques problèmes en parcourant cet article :

* La méthode `getEntry()` de Contentful ne résout pas les liens. Nous avons dû utiliser `getEntries()` à la place pour obtenir une seule entité expert avec l'URL de l'image de profil
* Il nous a fallu plus d'un petit moment pour comprendre comment nous pouvons afficher les résultats en utilisant la disposition en colonnes (par défaut, c'est des lignes)
* Timekit ne permet pas de récupérer la configuration de l'instance de calendrier en utilisant un ID externe. C'est pourquoi nous devons stocker les jetons de calendrier dans l'entité expert dans Contentful
* Le widget Voucherify ne vous permet pas d'essayer un autre code valide sans rafraîchir le site web

Je suis sûr qu'il y en a beaucoup d'autres. Mais vous pouvez contourner ces petits problèmes en bien moins de temps que vous ne mettriez à construire ces fonctionnalités à partir de zéro. En plus de cela, vous évitez les erreurs architecturales sérieuses et chronophages que les équipes de ces plateformes ont commises avant vous.

Le code source du projet peut être trouvé [ici](https://glitch.com/edit/#!/nostalgia?path=index.html:1:0). Et la démo est en ligne [ici](https://nostalgia.glitch.me/) !

### Renforcement et mise à l'échelle

Comme vous pouvez le voir, certains processus sont encore manuels et donc fastidieux :

* Ajout de nouveaux experts
* Rendre les experts recherchables
* Création de calendriers pour les experts

Dans la prochaine partie, nous allons coller ces services en utilisant [Zapier](https://zapier.com/). Zapier est une plateforme qui facilite la connexion des plateformes API-first. De cette manière, nous réduirons le travail manuel nécessaire pour exécuter les flux métiers mentionnés ci-dessus. Par exemple, les experts pourront s'inscrire eux-mêmes. De plus, la plateforme créera toutes les entités nécessaires de manière programmatique.

Enfin, nous pousserons le prototype en production. Ce sera toujours une application en phase initiale, mais elle sera plus robuste et prête à servir de vrais clients. Restez à l'écoute !

**Mise à jour** : vous pouvez trouver la deuxième partie [ici](https://www.freecodecamp.org/news/how-to-use-api-first-platforms-to-build-your-websites-faster-part-2-68085d7cdf36/).