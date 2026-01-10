---
title: Comment tester et jouer avec les API Web facilement avec Postman
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-06-30T16:34:32.000Z'
originalURL: https://freecodecamp.org/news/how-to-test-and-play-with-web-apis-the-easy-way-with-postman
coverImage: https://www.freecodecamp.org/news/content/images/2020/06/postman.jpg
tags:
- name: api
  slug: api
- name: Developer Tools
  slug: developer-tools
- name: programing
  slug: programing
- name: QA
  slug: qa
- name: Quality Assurance
  slug: quality-assurance
- name: REST API
  slug: rest-api
- name: software development
  slug: software-development
- name: Software Engineering
  slug: software-engineering
- name: Software Testing
  slug: software-testing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Testing
  slug: testing
- name: tools
  slug: tools
seo_title: Comment tester et jouer avec les API Web facilement avec Postman
seo_desc: "In a world where static websites and apps increasingly depend on separately\
  \ maintained APIs, it can be hard to figure out how they work by just playing around\
  \ in the browser. \nSo how can we use Postman to both test our existing APIs and\
  \ understand ho..."
---

Dans un monde où les sites web et les applications statiques dépendent de plus en plus d'API maintenues séparément, il peut être difficile de comprendre comment elles fonctionnent en jouant simplement dans le navigateur. 

Alors, comment pouvons-nous utiliser Postman pour tester nos API existantes et comprendre comment elles fonctionnent ?

* [Qu'est-ce que Postman ?](#heading-quest-ce-que-postman)
* [Qu'allons-nous construire / apprendre ?](#heading-quallons-nous-construire-apprendre)
* [Partie 0 : Installation avec Postman](#heading-partie-0-installation-avec-postman)
* [Partie 1 : Une introduction à Postman](#heading-partie-1-une-introduction-a-postman)
* [Partie 2 : Création d'une nouvelle requête Postman pour obtenir des informations sur Squirtle](#heading-partie-2-creation-dune-nouvelle-requete-postman-pour-obtenir-des-informations-sur-squirtle)
* [Partie 3 : Création d'une collection de requêtes dans Postman pour le PokéAPI](https://www.freecodecamp.org/news/p/a02335e1-4f9a-453d-8916-db6b8419cf99/partie-3-creation-dune-collection-de-requetes-dans-postman-pour-le-poke-api)
* [Partie 4 : Faire des requêtes POST avec Postman pour traduire des phrases pour qu'elles sonnent comme Yoda](#heading-partie-4-faire-des-requetes-post-avec-postman-pour-traduire-des-phrases-pour-quelles-sonnent-comme-yoda)
* [Partie 5 : Authentification des requêtes à l'API Le Seigneur des Anneaux avec une clé API](#heading-partie-5-authentification-des-requetes-a-lapi-le-seigneur-des-anneaux-avec-une-cle-api)

%[https://www.youtube.com/watch?v=KFuaybrXCdw]

## Qu'est-ce que Postman ?

[Postman](https://www.postman.com/) est un outil que les équipes peuvent utiliser pour tester les API de manière fiable en utilisant des configurations faciles à utiliser. Il est équipé de fonctionnalités que vous attendez lorsque vous travaillez avec des API, y compris l'authentification, la définition des en-têtes, la personnalisation de la charge utile, et bien plus encore qui aident à réduire les frictions de l'utilisation d'une API.

Et ce n'est pas seulement pour les tests. La beauté de cet outil est qu'il peut être utilisé pour de nombreux aspects du travail avec des API pour différents membres de l'équipe. Peut-être qu'un chef de projet veut vérifier que les choses fonctionnent ou trouver plus facile de faire un changement directement avec l'API, ou un ingénieur QA doit s'assurer que tout fonctionne toujours, ou un développeur veut apporter des modifications tout en travaillant sur l'API elle-même.

Le meilleur aspect de Postman est qu'il offre des fonctionnalités de collaboration. Le niveau gratuit inclut l'exportation et l'importation de collections de requêtes API sauvegardées ainsi que la création de liens partagés. Si vous faites partie d'une équipe, ils ont des niveaux payants qui vous permettent de synchroniser vos collections pour vous assurer que tout le monde a la collection la plus récente et à jour.

## Qu'allons-nous construire / apprendre ?

Nous allons parcourir deux API d'exemple différentes pour couvrir les concepts de Postman.

Tout d'abord, nous allons parcourir quelques requêtes HTTP simples avec une [API publique pour Pokémon](https://pokeapi.co/).

Ensuite, nous utiliserons l'API Yoda Translator pour démontrer comment faire des requêtes HTTP spécifiques.

Une fois que nous comprendrons comment fonctionnent les bases, nous utiliserons l'[API Le Seigneur des Anneaux](https://the-one-api.herokuapp.com/) pour apprendre comment fonctionne l'authentification avec les API. Pour cela, vous devrez vous inscrire pour un compte gratuit afin d'obtenir une clé API.

## Partie 0 : Installation avec Postman

Avant de commencer, vous aurez besoin de [Postman](https://www.postman.com/downloads/) pour suivre ce guide. La bonne nouvelle est que Postman est disponible gratuitement sur Mac, Windows et Linux, donc vous devriez pouvoir trouver une version qui fonctionne pour vous.

Obtenez Postman : [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

Une fois téléchargé, suivez les instructions d'installation standard, ouvrez-le, et nous devrions être prêts à partir !

## Partie 1 : Une introduction à Postman

La première fois que vous ouvrez Postman, vous verrez immédiatement un tableau de bord avec plusieurs options pour commencer.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-launchpad.jpg)

Cela peut sembler un peu écrasant, mais décomposons quelques-uns des concepts clés que nous devons connaître.

### Requêtes

Une requête est un peu ce à quoi elle ressemble, c'est une requête API spécifique. Ce sera un seul type de requête, qu'il s'agisse d'un GET ou POST vers un endpoint spécifique. Vous voudrez créer de nouvelles requêtes pour chaque type d'endpoint, ce qui vous permettra de passer entre eux lors des tests.

### Collections

Une collection est un groupe de requêtes. Cela est pratique pour organiser vos requêtes en différents groupes. Cela peut être aussi simple que deux API totalement différentes (par exemple, Twitter vs Slack) ou cela peut être deux groupes différents d'API pour une seule API (par exemple, l'API Tweets de Twitter vs l'API Comptes de Twitter).

### Autorisation

L'autorisation est la manière dont les requêtes sont authentifiées avec une API, que ce soit par une personne faisant une requête ou par un ordinateur faisant cette requête en votre nom. Cela se présente couramment sous la forme d'une clé API qui peut être une valeur statique assignée à votre compte ou générée dynamiquement avec des outils comme [OAuth](https://oauth.net/).

### Environnements

Les environnements vous permettront de configurer vos endpoints pour utiliser des variables spécifiques qui facilitent l'utilisation des mêmes endpoints entre différents environnements. Par exemple, vous pourriez avoir le même endpoint `/profile` sur vos environnements de production et de développement, mais ils ont des domaines différents. Les environnements vous permettent de gérer une seule requête avec un domaine variable.

### Espaces de travail

Nous n'irons pas trop loin dans les espaces de travail dans cet article, mais cela vous permet de gérer et d'organiser différents ensembles de collections. Imaginez si vous voulez utiliser Postman pour le travail et un projet personnel, vous pourriez avoir un espace de travail Travail ainsi qu'un espace de travail Personnel.

Pour les besoins de cet article, nous couvrirons les Requêtes, les Collections et l'Autorisation.

## Partie 2 : Création d'une nouvelle requête Postman pour obtenir des informations sur Squirtle

Maintenant que nous avons une meilleure compréhension de la terminologie différente, créons une requête.

En haut à gauche de l'interface utilisateur, vous devriez voir un bouton orange qui dit **Nouveau**. Allez-y et cliquez dessus, puis sélectionnez **Requête**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-create-new-request.jpg)

Avant de nous pencher sur la requête elle-même, elle demande quelques choses.

La première chose requise est un nom. Nous allons commencer par demander des informations sur le Pokémon Squirtle, alors nommons cela « Pokémon - Squirtle ».

Il nécessite également une collection, alors cliquez sur **Créer une Collection** et nommons la collection « Mes Pokémon préférés ».

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-configure-new-request.jpg)

Cliquez sur le bouton de coche orange à côté du nom de la collection, puis appuyez sur **Enregistrer**.

À ce stade, nous aurons une nouvelle requête, alors construisons cette requête.

Il y a deux choses que nous devons d'abord remplir pour notre première requête :

* **Type de requête** : GET, POST, PUT, etc - nous utiliserons GET
* **URL de la requête** : L'endpoint pour votre requête API - pour notre requête, nous utiliserons [https://pokeapi.co/api/v2/pokemon/squirtle/](https://pokeapi.co/api/v2/pokemon/squirtle/)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-squirtle-pokemon-get.jpg)

Et une fois que vous vous êtes assuré que ceux-ci sont corrects, vous pouvez simplement appuyer sur le bouton bleu **Envoyer** à droite et nous avons réussi à faire notre première requête !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-squirtle-pokemon-get-success.jpg)

Nous obtenons immédiatement quelques choses que nous pouvons voir :

* **Corps** : en bas, nous devrions maintenant voir le corps de la réponse de la requête API. Pour notre API Squirtle, nous devrions avoir un objet JSON avec des données comme `abilities`, `base_experience`, et `forms`.
* **Statut** : à droite, nous devrions voir le code de statut HTTP. « 200 Ok » est un bon signe et cela signifie qu'il a réussi !
* **Temps** : simplement combien de temps la requête a pris pour se terminer
* **Taille** : la taille en KB (dans notre exemple) des données de réponse

Vous pouvez également survoler Statut, Temps et Taille pour obtenir une vue plus approfondie de chaque option.

Nous avons donc fait notre première requête !

Une chose à remarquer avant de continuer est que notre requête semble être dans un onglet de navigateur. Si nous avons terminé avec cette requête particulière, nous pouvons fermer l'onglet et cliquer sur **Enregistrer** pour nous assurer que toutes nos modifications sont là pour la prochaine fois !

## Partie 3 : Création d'une collection de requêtes dans Postman pour le PokéAPI

Maintenant que nous avons créé une requête, créons une collection de celles-ci. Techniquement, nous avons déjà dû créer une nouvelle collection pour la Partie 2, mais nous allons en créer une nouvelle pour apprendre comment fonctionnent les collections elles-mêmes.

En haut à gauche de l'interface utilisateur, cliquez à nouveau sur le bouton orange **Nouveau** et sélectionnez **Collection**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-create-new-collection.jpg)

Similaire à une requête, il demande un nom, alors appelons cela « PokéAPI ». Optionnellement, vous pouvez ajouter une description, puis cliquer sur **Créer** en bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-configure-new-collection.jpg)

À gauche, vous verrez maintenant votre collection. Vous pouvez sélectionner et développer le dossier puisque nous allons travailler avec.

Avant d'ajouter une requête, le PokéAPI a différents types de requêtes, donc il est logique de l'organiser un peu plus en profondeur. Alors cliquez sur les trois points à côté de la collection PokéAPI et sélectionnez **Ajouter un Dossier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-folder-to-collection.jpg)

Similaire aux autres, cela demande un nom. Les dossiers sont un peu comme des collections à l'intérieur d'une collection, donc vous obtenez des options similaires. Nommons celui-ci « Pokémon » et cliquez sur le bouton orange **Enregistrer** comme avant.

Maintenant, ajoutons nos requêtes ! Tout d'abord, cliquez sur les trois points à côté du dossier Pokémon, de manière similaire à la façon dont nous avons ajouté un dossier à la collection, mais cette fois sélectionnez **Ajouter une Requête**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-request-to-collection.jpg)

Nommons cette requête « Pokemon ». Bien que cela puisse être déroutant que nous ayons une requête Pokemon à l'intérieur du dossier Pokémon, Pokemon est simplement l'un des endpoints du groupe Pokémon.

Maintenant, utilisons la même API exacte que nous avons utilisée avec notre requête Squirtle auparavant :

* **Type de Requête** : GET
* **URL de la Requête** : [https://pokeapi.co/api/v2/pokemon/squirtle/](https://pokeapi.co/api/v2/pokemon/squirtle/)

Et de manière similaire à avant, lorsque nous appuyons sur le bouton bleu **Envoyer**, nous devrions voir une requête réussie !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-get-request-squirtle.jpg)

Maintenant, ajoutons une autre requête. Suivez le même processus que précédemment pour créer une nouvelle requête sous le dossier Pokémon de PokéAPI et nommons cette requête « Abilities ».

Si vous faites défiler la réponse du premier endpoint Squirtle, vous voyez beaucoup d'autres URL d'API. En haut, nous avons `abilities` et nous en avons deux différentes — « torrent » et « rain-dish ».

Choisissez votre capacité Squirtle préférée et copiez la valeur `url` dans la nouvelle requête Abilities que nous venons de créer, je vais utiliser `rain-dish`.

Nous pouvons laisser le Type de Requête comme GET, appuyer sur le bouton bleu **Envoyer**, et nous pouvons à nouveau voir une réponse réussie !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-request-squirtle-abilities.jpg)

Ici, nous obtenons beaucoup d'informations sur notre capacité Squirtle Rain Dish et certains des détails sont dans différentes langues, ce qui est cool !

Nous avons donc une nouvelle collection PokéAPI avec un dossier Pokémon représentant le groupe d'endpoints API Pokémon incluant Pokemon et abilities.

Nous allons arrêter la Partie 3 avec ces 2 requêtes, mais n'hésitez pas à continuer et à ajouter autant de requêtes PokéAPI que vous le souhaitez !

## Partie 4 : Faire des requêtes POST avec Postman pour traduire des phrases pour qu'elles sonnent comme Yoda

Jusqu'à présent, nous n'avons fait que des requêtes GET, mais que se passe-t-il si nous voulions faire une requête POST où nous devons réellement envoyer des données ?

Pour faire une requête POST, nous allons utiliser l'API Yoda Translator de funtranslations.com. Bien que cette API ne prenne qu'un seul paramètre, c'est toujours un bon endpoint public que nous pouvons utiliser pour comprendre le concept.

Tout d'abord, créons une nouvelle collection avec une nouvelle requête :

* **Collection** : Fun Translations
* **Requête** : Yoda

Cette fois, au lieu d'une requête GET, notre configuration de requête sera :

* **Type de Requête** : POST
* **URL de la Requête** : [https://api.funtranslations.com/translate/yoda](https://api.funtranslations.com/translate/yoda)

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-new-request-yoda-api.jpg)

Maintenant, cette fois, si nous appuyons sur le bouton bleu **Envoyer**, nous remarquerons que nous n'obtenons pas une réponse réussie 200, nous obtenons une 400 !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-yoda-api-bad-request.jpg)

Nous n'avons jamais réellement configuré de données à envoyer à l'API et elle nécessite ces données, alors ajoutons-les.

Juste en dessous de l'**URL de la Requête**, cliquez sur **Body**. Ensuite, au lieu de none, sélectionnez **raw** comme type de corps. Enfin, à l'extrême droite des types, changez **Text** en **JSON**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-yoda-request-body-type.jpg)

Ensuite, dans l'espace en dessous, vous pouvez ajouter ce qui suit :

```json
{
    "text": "Bonjour, j'apprends à tester les API avec Postman !"
}

```

Et maintenant, cliquez à nouveau sur le bouton bleu **Envoyer** et nous obtenons une réponse réussie !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-post-body-yoda-api.jpg)

Nous pouvons appliquer ce concept à presque n'importe quelle API. Postman ne vous permet pas seulement d'envoyer du JSON, il vous permet d'utiliser les autres formats que nous voyons listés dans la section Type de Corps, ce qui signifie que vous avez beaucoup d'options en fonction de ce que l'API que vous utilisez nécessite.

## Partie 5 : Authentification des requêtes à l'API Le Seigneur des Anneaux avec une clé API

Pour le reste du guide, nous allons utiliser l'API Le Seigneur des Anneaux.

Tout d'abord, l'API Le Seigneur des Anneaux nécessite une authentification afin de faire des requêtes en utilisant une clé API. Donc, pour commencer, avant de plonger, vous devrez [créer un compte gratuit](https://the-one-api.herokuapp.com/sign-up).

[https://the-one-api.herokuapp.com/sign-up](https://the-one-api.herokuapp.com/sign-up)

Une fois que vous vous êtes inscrit et connecté, la première chose que vous verrez est votre clé API ! Copiez cette clé ou souvenez-vous de l'endroit où vous pouvez la trouver plus tard. Si vous quittez la page, vous pouvez toujours la récupérer en naviguant vers **Bienvenue** puis **Compte** dans la navigation du site web de l'API.

Pour commencer, créons d'abord une nouvelle collection et une nouvelle requête :

* **Collection** : Le Seigneur des Anneaux
* **Dossier** : Film
* **Requête** : Tous les Films
* **Type de Requête** : GET
* **URL de la Requête** : [https://the-one-api.herokuapp.com/v1/movie](https://the-one-api.herokuapp.com/v1/movie)

Une fois que vous êtes prêt avec ce qui précède, cliquez sur **Envoyer**, et vous remarquerez immédiatement qu'il donne une réponse qui dit 401 et qu'elle n'est pas authentifiée.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-unauthorized-request-lord-of-the-rings-api.jpg)

Parce que cette API nécessite la clé API, c'est exactement ce à quoi nous nous attendions. Alors cliquons sur l'onglet **Authorization**. Nous pouvons ensuite sélectionner un **Type** de **Bearer Token**, et à droite, nous pouvons coller notre clé que nous venons de configurer avec l'API Le Seigneur des Anneaux.

Et dès que nous appuyons sur **Envoyer**, nous voyons maintenant une réponse réussie !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-authorized-successful-lord-of-the-rings-api-request.jpg)

Cela a très bien fonctionné, mais que se passe-t-il si nous avons un tas de requêtes qui utilisent une seule clé. Devons-nous gérer cela sur chaque requête ?

Au lieu de gérer cela sur chaque requête individuelle, nous pouvons le gérer sur la collection. Construisons d'abord une autre requête.

Sous notre collection Le Seigneur des Anneaux et dans le dossier Film, créez une nouvelle requête :

* **Requête** : Citation par ID de Film
* **Type de Requête** : GET
* **URL de la Requête** : [https://the-one-api.herokuapp.com/v1/movie/{id}](https://the-one-api.herokuapp.com/v1/movie/%7Bid%7D)

Dans cette requête, utilisons un ID de la réponse de la première requête, je vais utiliser `5cd95395de30eff6ebccde5b` qui est l'ID des Deux Tours, donc l'URL de la requête ressemblera à :

```
https://the-one-api.herokuapp.com/v1/movie/5cd95395de30eff6ebccde5b
```

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-inherit-authorization-from-parent.jpg)

Maintenant, au lieu de définir notre token dans l'Autorisation de la requête, nous allons laisser le type comme **Inherit auth from parent**. Cliquez sur les trois points à côté de la collection et sélectionnez **Edit**.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-edit-collection.jpg)

Ici, nous allons faire la même chose exacte que nous avons faite avec la première requête mais sur la configuration de la Collection. Sélectionnez l'onglet **Authorization**, sous type sélectionnez **Bearer Token**, et dans le champ **Token** collez à nouveau votre token.

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-add-authorization-api-key-token-to-collection.jpg)

Enfin, cliquez sur **Update** et appuyez à nouveau sur le bouton bleu **Envoyer** et nous pouvons voir une requête réussie !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-authorized-request-inherit-token-from-parent.jpg)

Nous pouvons maintenant revenir à notre requête Tous les Films et mettre à jour l'Autorisation pour utiliser un Type de Inherit auth from parent et elle devrait continuer à fonctionner !

![Image](https://www.freecodecamp.org/news/content/images/2020/06/postman-successful-request-lord-of-the-rings-api.jpg)

## Que pouvons-nous faire d'autre avec Postman ?

Bien que j'ai couvert beaucoup des bases, il y a encore beaucoup plus de choses que vous pouvez faire avec Postman. Voici quelques-unes de mes préférées.

### Variables d'environnement

Si vous travaillez en tant que développeur sur un projet, il est probable que votre équipe utilise plusieurs environnements, tels qu'un environnement de développement et de production. Au lieu de créer et de maintenir des requêtes complètement séparées, vous pouvez ajouter une variable d'environnement et changer cette variable lorsque vous passez entre les environnements !

Les variables s'appliquent à de nombreux scénarios, mais c'est un usage courant. Consultez la documentation de Postman pour apprendre comment.

[https://learning.postman.com/docs/postman/variables-and-environments/variables/](https://learning.postman.com/docs/postman/variables-and-environments/variables/)

### Importer et exporter des collections et des données

Une chose géniale à propos de Postman est que, une fois que vous avez toutes vos requêtes organisées, vous pouvez les exporter pour que d'autres les utilisent. Cela signifie également que vous pouvez importer des collections d'autres membres de l'équipe. Cela rend beaucoup plus facile de s'assurer que tout le monde utilise la même collection.

Bonus : vous pouvez même stocker ces fichiers dans un dépôt Git, car ils ne sont que du JSON.

Mais gardez à l'esprit - si vous utilisez l'Autorisation sur la collection comme nous l'avons vu dans ce guide, vous voudrez vous assurer de ne pas l'inclure lorsque vous exportez votre collection.

[https://learning.postman.com/docs/postman/collections/importing-and-exporting-data/](https://learning.postman.com/docs/postman/collections/importing-and-exporting-data/)

### Tests automatisés

Une fois que vous avez un ensemble de requêtes dans une collection et mieux encore, si vous les stockez dans Github, vous pouvez commencer à utiliser ces requêtes comme partie d'une manière de gérer les tests automatisés de votre API.

Bien qu'il existe quelques solutions pour faire cela, Postman inclut un Collection runner intégré directement dans l'application et [Newman](https://learning.postman.com/docs/postman/collection-runs/command-line-integration-with-newman/) est un outil en ligne de commande qui vous permet d'exécuter des tests directement depuis le terminal.

[https://www.postman.com/use-cases/api-testing-automation/](https://www.postman.com/use-cases/api-testing-automation/)

## Quelle est votre manière préférée de tester et de jouer avec les API ?

[Partagez avec moi sur Twitter !](https://twitter.com/colbyfayock)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f4f9 Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>