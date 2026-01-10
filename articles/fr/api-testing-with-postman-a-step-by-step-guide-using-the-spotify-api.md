---
title: 'Test d''API avec Postman : un guide étape par étape utilisant l''API Spotify'
subtitle: ''
author: Matthes B.
co_authors: []
series: null
date: '2024-09-11T17:23:24.971Z'
originalURL: https://freecodecamp.org/news/api-testing-with-postman-a-step-by-step-guide-using-the-spotify-api
coverImage: https://cdn.hashnode.com/res/hashnode/image/stock/unsplash/uv5_bsypFUM/upload/ef5e3375e4ea08db6b5addd47afbc82f.jpeg
tags:
- name: Postman
  slug: postman
- name: APIs
  slug: apis
- name: 'API basics '
  slug: api-basics
- name: Spotify
  slug: spotify
seo_title: 'Test d''API avec Postman : un guide étape par étape utilisant l''API Spotify'
seo_desc: '🎯 The Objective

  In this guide, I’ll introduce you to Postman, a popular API development and testing
  tool.

  If you are a beginner mainly focused on frontend development, you may not have had
  much experience fetching data from an API. And in that case ...'
---

## **🎯** L'Objectif

Dans ce guide, je vais vous présenter Postman, un outil populaire de développement et de test d'API.

Si vous êtes un débutant principalement axé sur le développement frontend, vous n'avez peut-être pas encore beaucoup d'expérience dans la récupération de données à partir d'une API. Dans ce cas, vous n'avez probablement pas rencontré beaucoup de situations où vous devez effectuer plusieurs requêtes vers une API à des fins de test pendant votre processus de développement.

Mais comprendre comment tester les API et s'y connecter via Postman ou des outils similaires deviendra important à un moment donné de votre carrière. Si vous décidez de vous lancer dans le développement backend, la compréhension de ces concepts est essentielle.

Après avoir couvert quelques informations de base sur Postman et la documentation de l'API Spotify, nous plongerons dans d'autres fonctionnalités clés de Postman. Ensuite, nous sélectionnerons un endpoint Spotify et suivrons le processus pour y effectuer des requêtes.

## **🔑 Voici ce que nous allons couvrir**

* Vous acquerrez des connaissances fondamentales sur l'utilisation de Postman.
    
* Vous renforcerez votre capacité à travailler avec les API et leur documentation.
    
* Vous explorerez les bases de l'API publique Spotify.
    

## **📝** Prérequis

* Vous devez avoir une compréhension de base des API.
    
* Vous n'avez besoin d'aucune connaissance préalable de Postman.
    

## Table des matières

1. [Exploration de l'API Spotify avec Postman](#heading-exploration-de-lapi-spotify-avec-postman)
    
2. [L'expérience Postman](#heading-lexperience-postman)
    
3. [Comment effectuer votre première requête vers l'API Spotify](#heading-comment-effectuer-votre-premiere-requete-vers-lapi-spotify)
    
4. [Autorisation de l'API Spotify](#heading-autorisation-de-lapi-spotify)
    
5. [Portées d'autorisation de l'API Spotify](#heading-portees-dautorisation-de-lapi-spotify)
    
6. [Résumé](#heading-resume)
    

## Exploration de l'API Spotify avec Postman

Pour obtenir un bref aperçu de ce qu'est Postman, reportons-nous à l'explication suivante de ChatGPT :

> "Postman est un outil populaire de développement et de test d'API (Application Programming Interface) qui simplifie le travail avec les API en fournissant une interface facile à utiliser pour envoyer des requêtes HTTP et recevoir des réponses. Il est largement utilisé par les développeurs, les ingénieurs QA et les équipes qui travaillent avec des API pour s'assurer qu'elles fonctionnent correctement et efficacement."

Bien que nous nous concentrerons sur les requêtes HTTP, il est important de noter que Postman est également polyvalent et peut être utilisé pour travailler avec GraphQL, gRPC, WebSocket, Socket.IO et MQTT.

Avec Postman en main, nous avons besoin d'un endpoint d'API à tester. Pour cela, nous utiliserons l'API publique Spotify, qui offre une variété d'endpoints pour différents cas d'utilisation. Cela peut même être une opportunité passionnante pour votre prochain projet si vous êtes un débutant à la recherche d'un projet amusant à explorer.

L' [API Web Spotify](https://developer.spotify.com/documentation/web-api) est conçue de manière professionnelle, offrant toutes les informations nécessaires aux développeurs. Avec leurs sections "Overview" et "Getting Started", il est simple de suivre, même pour les débutants.

Tout en apprenant les bases de Postman, nous explorerons les parties clés de la documentation de l'API Spotify nécessaires pour réussir les tests d'API. Par exemple, nous démontrerons comment effectuer une requête HTTP vers l'endpoint pour [récupérer les données d'une playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist).

Mais d'abord, couvrons quelques fondamentaux de Postman.

## L'expérience Postman

Vous pouvez utiliser Postman de plusieurs manières différentes. Dans mon cas, j'utilise la [version de bureau](https://www.postman.com/downloads/) de Postman.

Mais vous pouvez également utiliser Postman directement dans votre navigateur, ou même via la CLI (Interface de ligne de commande) Postman. Il existe également une extension officielle Postman pour VS Code. Vous pouvez trouver ces versions via le lien que je viens de partager.

Si vous êtes complètement nouveau sur Postman, vous voudrez peut-être commencer par la version web ou la version de bureau téléchargeable, surtout si vous prévoyez d'utiliser Postman régulièrement à l'avenir.

Après avoir lancé la version de bureau de Postman, la première chose que vous verrez est ceci :

![Vue initiale de l'interface Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725784802934/f999e51b-13d1-4bfc-b51a-99cf16c51209.png align="center")

Cela peut sembler légèrement différent de ce que vous voyez au départ. J'ai déjà un compte. Vous devrez peut-être en créer un gratuitement d'abord. Vous devrez peut-être aussi créer un espace de travail (workspace) d'abord. Dans mon cas, je suis déjà à l'intérieur de l'espace de travail "My Workspace".

Dans le coin supérieur gauche, vous trouverez plusieurs onglets, notamment "Collections", "Environments", "History" et une icône pour configurer cette barre latérale.

Pour l'instant, nous resterons sur l'onglet "Collections" et cliquerons sur "Create Collection" :

![Création d'une nouvelle collection dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725785048909/3751a2a7-c583-4918-ba92-b14ddf09787c.png align="center")

Une fois que vous aurez cliqué dessus, votre attention se portera sur le nom de la collection au centre en haut. En tapant, vous pouvez renommer votre collection de "New Collection" en quelque chose de plus approprié pour votre cas d'utilisation spécifique.

Pour ce cas, j'ai nommé la collection "Spotify API" :

![Affichage d'une collection créée dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725785166414/65ae8c54-be76-4b70-99b1-87897ef0506d.png align="center")

Maintenant, nous avons une collection, mais qu'est-ce que c'est exactement ? Une collection est essentiellement un espace pour organiser plusieurs structures de requêtes. Cela deviendra plus clair une fois que nous aurons ajouté notre première requête HTTP. Vous pouvez le faire en cliquant sur le texte bleu qui dit "Add a request" :

![Création de la première requête au sein d'une collection dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725785355577/2b7cb0ea-9fe4-41e5-a0b4-a01472a6c4b5.png align="center")

Lorsque vous ferez cela, votre attention sera à nouveau portée sur le nom de l'élément. Si vous tapez quelque chose maintenant, vous pouvez renommer la requête de "New Request" en quelque chose de plus approprié. Dans ce cas, comme je ne sais pas encore quelle requête je veux créer, je l'appellerai simplement "test" pour le moment.

Si vous souhaitez créer une autre requête à ce stade, vous pouvez cliquer sur les trois points à droite du nom de la collection (la 6ème option) :

![Création de nouvelles requêtes au sein d'une collection dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725785494545/227bad55-040f-45c4-8afc-5fb978714d53.png align="center")

Il existe plusieurs options que vous pouvez choisir, "Add request" étant l'une d'entre elles.

À ce stade, nous avons créé une collection dans notre espace de travail, et à l'intérieur de cette collection, nous avons ajouté une requête HTTP. Vous pouvez avoir plusieurs collections, chacune contenant plusieurs requêtes. Cela aide à organiser vos requêtes, surtout lorsque vous atteignez un point où avoir une seule longue liste de requêtes préconfigurées devient difficile à gérer.

Sur la requête HTTP nouvellement créée, nous pouvons voir quelques détails :

![Affichage d'une requête HTTP créée dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725785740673/b7d66a0d-d16c-4cf5-846b-21c0289e1fc9.png align="center")

La première chose que vous remarquerez peut-être est la méthode de requête HTTP, qui est définie sur "GET" par défaut. Si vous cliquez sur "GET" avec la flèche vers le bas, vous pouvez choisir parmi diverses méthodes ou même taper la vôtre si nécessaire.

À droite de cela, il y a un champ de texte où vous entrerez l'URL de votre API ainsi que son endpoint (nous essaierons cela sous peu).

Ci-dessous, il y a plusieurs onglets importants. En ce moment, nous sommes sur l'onglet "Params". Ici, vous pouvez ajouter des paires clé-valeur qui modifieront directement la requête que vous effectuez. Ceux-ci sont appelés Query Params (Paramètres de requête), que vous avez peut-être déjà rencontrés. Par exemple, si votre URL est `https://google.com`, l'ajout d'une paire clé-valeur en tant que Query Param pourrait ressembler à ceci :

![Ajout de Query Params à une requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725786057766/5c379d02-a1db-4484-9951-17d8fc63d9f5.png align="center")

En ce qui concerne les Query Params, leur nécessité dépend de la requête que vous effectuez. Un cas d'utilisation courant serait la pagination sur un site web avec un tableau. Par exemple, vous pourriez utiliser un paramètre de requête comme "page=4" pour spécifier quelle page de résultats vous souhaitez.

Vient ensuite l'onglet "Authorization", qui gère l'authentification et l'autorisation de votre requête. Nous couvrirons cela plus en détail plus tard, nous allons donc l'ignorer pour le moment.

Ensuite, nous avons l'onglet "Headers", qui est crucial car il contient toutes les informations incluses dans l'en-tête de votre requête, telles que les données d'autorisation si elles sont configurées.

Enfin, l'onglet "Body", situé à droite, est également très important. Par exemple, si vous effectuez une requête POST pour ajouter un élément à une base de données, vous devrez probablement envoyer des informations telles que le nom ou la catégorie de l'élément. Ce type de données est souvent inclus dans le corps de la requête au format JSON.

Pour ajouter des données au format JSON, vous pouvez cliquer sur "raw" dans l'onglet "Body", puis sélectionner le format souhaité (JSON étant l'option par défaut) :

![Affichage de l'onglet "Body" d'une requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725786376804/334980e7-f2a4-44ec-b354-6923254c842b.png align="center")

Comme pour les Query Params, le format et les données requis dépendent fortement de l'API et de l'endpoint que vous utilisez. Gardez simplement à l'esprit que vous pouvez configurer toutes les options nécessaires dans ces onglets.

Les deux onglets restants sont "Scripts" et "Settings". Dans l'onglet "Scripts", vous pouvez ajouter du code personnalisé, mais c'est plus avancé et non nécessaire pour notre situation actuelle. L'onglet "Settings" permet des ajustements, bien que dans la plupart des cas, vous n'aurez rien à modifier ici.

## Comment effectuer votre première requête vers l'API Spotify

Maintenant, nous allons effectuer notre première véritable requête en utilisant Postman. Pour cela, nous pouvons plonger dans la documentation développeur de l'API Spotify, où tous les endpoints sont répertoriés. Pour ce premier test, nous allons [récupérer des données sur une playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist).

Dans cette description, vous trouverez une mine d'informations utiles, notamment l'endpoint et les données requises pour une réponse réussie. Vous avez également la possibilité d'effectuer la requête directement depuis la page après vous être connecté avec votre compte Spotify :

![Affichage de la documentation de l'API Spotify "Get Playlist"](https://cdn.hashnode.com/res/hashnode/image/upload/v1725786874122/dfc15da0-4c9d-465d-8f29-470b7978ed18.png align="center")

Une documentation d'API aussi complète est incroyablement utile et facilite le travail, surtout pour les débutants. Gardez toutefois à l'esprit que toutes les documentations d'API ne sont pas aussi approfondies.

Dans ce cas, nous pouvons voir que l'endpoint est `https://api.spotify.com/v1/playlists/{playlist_id}`, `playlist_id` étant le seul paramètre requis entre les accolades. Vous verrez également des paramètres facultatifs comme `market`, `fields` et `additional_types`, qui peuvent aider à affiner la réponse. Mais encore une fois, ils sont facultatifs, et vous n'avez besoin que du `playlist_id` pour la requête de base.

Si vous souhaitez inclure des informations facultatives, comme `market`, vous utiliseriez les Query Params mentionnés précédemment. Par exemple, ajouter `ES` comme marché aux côtés du `playlist_id` changerait l'URL en : `https://api.spotify.com/v1/playlists/3cEYpjA9oz9GiPac4AsH4n?market=ES`.

Pour effectuer la requête de base dans Postman (sans aucun paramètre facultatif), nous retournerons à notre requête "test" et saisirons l'URL avec l'endpoint correspondant :

![Insertion de l'endpoint de l'API Spotify "Get Playlist" dans une requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725787287945/6c54e09f-08c0-4bf9-9dd9-deabe5a24a22.png align="center")

Cette approche fonctionnera, mais je recommande une autre méthode.

Comme nous avons notre collection Spotify API et que nous voudrons peut-être ajouter plusieurs requêtes à cette collection, il est conseillé d'utiliser des variables pour les sections de l'URL ou les informations qui resteront cohérentes sur plusieurs requêtes. Dans ce cas, l'URL de base, `https://api.spotify.com/v1/`, restera la même pour toutes les requêtes de l'API Spotify. Au lieu de l'ajouter manuellement à chaque requête, nous pouvons créer une variable pour cela.

Pour ce faire, nous passerons à l'onglet "Environments" dans le coin supérieur gauche. De là, cliquez sur l'icône plus pour créer un nouvel environnement :

![Création d'un nouvel environnement dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725787536747/937b306f-1f54-4434-973d-6ba389a865fe.png align="center")

Nous nommerons l'environnement "Spotify API".

Ensuite, nous créerons des variables, telles que `base_url`, et lui assignerons la valeur appropriée. Vous pouvez également choisir entre les options de type : `default` ou `secret`. Comme il ne s'agit pas de données sensibles, elles peuvent rester sur `default`. Si vous choisissez `secret`, vous devrez cliquer sur une icône en forme d'œil pour révéler la valeur de la variable à chaque fois, sinon, elle sera masquée par `••••`, comme s'affichent les mots de passe.

Voici à quoi cela ressemble jusqu'à présent :

![Création d'une variable d'environnement dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725787778964/02e4bcf5-3f36-47e8-9882-6cdba591e443.png align="center")

Ensuite, nous retournerons à la collection Spotify API et regarderons dans le coin supérieur droit, où il est actuellement indiqué "No environment". Cliquez là et sélectionnez l'environnement "Spotify API" que nous venons de créer :

![Sélection de l'environnement créé pour la collection actuelle dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725787865310/abb97e82-2a6b-4411-a8cd-9e4430e83956.png align="center")

Maintenant, nous pouvons utiliser les variables de cet environnement pour toutes les requêtes au sein de la collection "Spotify API". Pour insérer une variable, vous utiliserez des doubles accolades, comme ceci :

![Insertion de la variable d'environnement créée pour la requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725788017057/10cd4dbc-fecf-46d7-9789-9c80b1325215.png align="center")

Si vous recevez un message indiquant que la variable n'a pas pu être trouvée, assurez-vous d'enregistrer l'environnement "Spotify API". Les points à droite des noms d'onglets indiquent que vous pouvez enregistrer de nouvelles informations en appuyant sur `CTRL + S`, par exemple. Cette étape est nécessaire pour que la variable créée soit reconnue.

Une fois la variable en place, vous pouvez maintenant modifier cette seule variable pour changer la `base_url` de toutes vos requêtes correspondantes. Bien que cela puisse ne pas sembler immédiatement utile pour la `base_url`, car elle ne changera probablement pas de sitôt, les variables peuvent être incroyablement utiles dans d'autres scénarios. C'était l'occasion de vous présenter leur fonctionnement.

Ensuite, je renommerai la requête HTTP de "test" en quelque chose de plus descriptif, comme "Playlist", pour indiquer l'objet de cette requête. Avec la méthode "GET", il sera clair que cette requête sert à récupérer des données de playlist.

Maintenant que tout est prêt, envoyons la requête en cliquant sur le bouton "Send" à droite tout en visualisant la requête HTTP. Vous verrez la réponse apparaître dans la moitié inférieure de l'écran :

![Affichage de la première réponse de la requête HTTP envoyée dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725788403952/4212378e-c000-4b5c-bdc1-43a5658b1f11.png align="center")

Quelle déception, la requête n'a pas abouti !

Cela s'est produit parce que nous n'avons fourni aucune autorisation. C'est pourquoi nous avons reçu une erreur "401 Unauthorized" avec le message "No token provided".

Comme il s'agit d'un endpoint protégé, nous avons besoin d'un jeton d'accès (access token), que vous obtiendriez en vous connectant à Spotify. Si vous avez essayé d'effectuer une requête sur le site de documentation de l'API Spotify plus tôt, vous avez probablement remarqué qu'il vous a demandé de vous connecter avant d'envoyer la requête. En faisant cela, il a acquis le jeton d'accès de votre session, ce qui est exactement ce dont nous avons besoin dans notre situation également.

Cependant, au lieu de nous connecter avec notre nom d'utilisateur et notre mot de passe, nous utiliserons une méthode d'autorisation différente.

## Autorisation de l'API Spotify

Pour effectuer des requêtes de base vers l'API Spotify, vous aurez besoin d'un jeton d'accès, qui peut être généré à l'aide de vos identifiants. C'est une approche courante avec de nombreuses API, où vous devez obtenir un jeton d'accès avant de pouvoir accéder aux endpoints que vous ciblez.

L'API Spotify pour développeurs fournit un [guide étape par étape](https://developer.spotify.com/documentation/web-api/tutorials/getting-started#request-an-access-token) sur la façon d'obtenir votre jeton d'accès.

En suivant les étapes décrites, la première tâche consiste à créer un profil d'application, ce que vous pouvez faire en quelques secondes, surtout pour un projet de test :

![Affichage de l'application "test" créée dans le tableau de bord Spotify for Developers](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824014786/22229e4f-0605-488b-80ef-72034fd8a414.png align="center")

Après avoir terminé cette étape, nous pouvons continuer en cliquant sur le projet "test" pour naviguer vers les "Settings" du projet. Ici, vous trouverez le "Client ID" et le "Client Secret" :

![Affichage des informations détaillées de l'application "test" créée dans le tableau de bord Spotify for Developers](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824076709/5adfd96a-f7e9-45e8-9dcf-67137ef2c814.png align="center")

Gardez à l'esprit que ces informations sont généralement considérées comme sensibles, vous devriez donc éviter de les partager publiquement (dans la plupart des cas). Mais comme il ne s'agit que d'un projet de test, qui sera supprimé au moment de la publication de ce guide, je les montre pour vous faciliter le suivi de mes explications.

Avec votre Client ID et votre Client Secret en main, vous disposez maintenant des informations nécessaires pour demander un jeton d'accès. Ces jetons d'accès sont utilisés pour vous autoriser lors de l'interaction avec les endpoints de l'API.

Vous pouvez comparer cela à une connexion à un logiciel, où vous devez vous authentifier avant d'accéder à certaines informations. Dans de tels cas, il est probable qu'un jeton d'accès soit généré pour la durée de votre session afin d'autoriser vos requêtes vers l'API backend du logiciel.

N'oubliez pas non plus que les jetons d'accès changent à chaque session de connexion, ce qui signifie que vous recevez un jeton différent à chaque fois. Gardez simplement à l'esprit qu'avec notre méthode actuelle sélectionnée, nous n'avons pas accès aux informations spécifiques de l'utilisateur. Au lieu de cela, nous ne pouvons effectuer que des requêtes GET de base sans agir au nom d'un utilisateur. Nous couvrirons cela un peu plus tard.

La documentation de l'API Spotify est très utile et fournit des instructions détaillées sur la requête exacte que vous devez effectuer. Nous allons maintenant passer dans Postman pour cette étape.

Allez dans votre collection "Spotify API" et cliquez sur l'onglet "Authorization". Ici, vous devez choisir le bon "Auth Type". Il existe plusieurs options, et la méthode d'autorisation peut différer selon l'API que vous utilisez.

Si vous avez déjà un jeton d'accès, vous pouvez opter pour le type d'authentification "Bearer Token", où vous collez simplement le jeton directement. C'est le type d'autorisation que nous utiliserons au final. Mais au lieu de demander manuellement un jeton puis de le saisir dans le champ "Bearer Token", nous pouvons automatiser ce processus. Pour cela, nous sélectionnerons "[OAuth 2.0](https://oauth.net/2/)" comme type d'autorisation.

Comment ai-je su que "OAuth 2.0" était le bon choix ? Si vous consultez la documentation de l'API Spotify, vous trouverez des informations correspondantes en parcourant leur guide étape par étape. De plus, tous les endpoints qui nécessitent une autorisation sont marqués avec "OAuth 2.0", y compris l'endpoint "[Get Playlist](https://developer.spotify.com/documentation/web-api/reference/get-playlist)" :

![Affichage du "Auth Type" nécessaire pour l'endpoint Get Playlist](https://cdn.hashnode.com/res/hashnode/image/upload/v1725971891125/724c447e-3016-42b2-9538-a311933738e6.png align="center")

La documentation mentionne également que Spotify utilise les "Client Credentials" pour son tutoriel. C'est le "grant type" (type d'octroi) et cela indique les informations que vous fournirez pour la demande d'autorisation. Avec les "Client Credentials", vous transmettez votre Client ID et votre Client Secret (les informations de notre application de test).

Par exemple, avec le type d'octroi "Password Credentials", vous transmettriez également un "Username" et un "Password", ce qui est utilisé lors de la connexion avec un compte utilisateur réel.

Il existe également d'autres méthodes d'autorisation, et la documentation de l'API spécifie généralement l'approche à utiliser. Dans notre cas, comme nous avons le Client ID et le Client Secret et que nous n'avons pas besoin d'un accès utilisateur spécifique, nous savons que le type d'octroi "Client Credentials" est le choix approprié.

Lors de la saisie de votre Client ID et de votre Client Secret dans Postman, vous recevrez peut-être une suggestion d'utiliser des variables pour ces informations :

![Configuration de l'"Authorization" pour la collection Spotify API dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824602370/d488cb29-6a62-4756-995e-32a018237893.png align="center")

Tout comme la variable `base_url` que nous avons utilisée précédemment, la création de variables pour le Client ID et le Client Secret peut être utile, surtout si vous prévoyez d'utiliser plusieurs requêtes HTTP avec des autorisations similaires. De cette façon, vous pouvez référencer les mêmes variables dans toutes vos requêtes, et si quelque chose change, vous n'avez qu'à mettre à jour la variable à un seul endroit.

Dans ce cas, nous ferons de même en passant à l'onglet "Environments" et en ajoutant des variables pour `client_id` et `client_secret`.

![Ajout de variables d'environnement pour le Client ID et le Client Secret](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824729649/77ed62b1-7221-4e32-bccf-be366102c3df.png align="center")

Ensuite, vous insérerez ces variables dans le processus d'autorisation que nous avons commencé plus tôt :

![Mise à jour de l'"Authorization" pour la collection Spotify API avec des variables d'environnement dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824827178/98394518-2a93-40ca-9e6f-01544ee3bfbb.png align="center")

Maintenant, nous devons juste ajouter l'URL d'autorisation du jeton, qui se trouve sur la même page qu'auparavant : `https://accounts.spotify.com/api/token`. Entrez ceci dans le champ "Access Token URL". Ensuite, donnez à la configuration un nom approprié de votre choix et faites défiler vers le bas pour cliquer sur le bouton "Get New Access Token" :

![Création réussie d'un jeton d'accès dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824937975/e94e1701-6a4f-43c9-949d-136160a6aeb4.png align="center")

C'est réussi ! Maintenant, cliquez sur "Proceed" pour voir plus de détails sur le jeton d'accès généré :

![Affichage d'informations détaillées sur le jeton d'accès créé dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725824969843/f3985bad-e596-4b72-a31f-cf9fc7b49b8d.png align="center")

Avec notre jeton d'accès prêt, cliquez sur "Use Token" en haut à droite, et Postman confirmera que le jeton a été ajouté.

Maintenant, si nous passons à la requête GET "Playlist" que nous avons créée plus tôt, vous verrez l'option de configurer une méthode d'autorisation pour cette requête spécifique. Mais comme nous avons déjà configuré l'autorisation pour toute la collection, sélectionnez simplement "Inherit auth from parent" comme "Auth Type" pour cette requête :

![Affichage du "Auth Type" pour la requête HTTP au sein de la collection Spotify API dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725825052455/c1167201-89b5-4560-8f83-be0a0e39bcea.png align="center")

Postman indiquera quel type d'autorisation est utilisé et d'où il provient. Dans ce cas, il dira : "The request is using OAuth 2.0 from collection Spotify API."

Ensuite, si nous passons à l'onglet "Headers" et cliquons sur "8 hidden", nous pouvons voir une clé "Authorization". En cliquant sur le symbole de l'œil à droite, nous pouvons révéler cette information.

Si vous comparez cela avec le jeton d'accès que nous venons de générer, vous remarquerez qu'ils sont identiques (avec "Bearer" devant le jeton d'accès réel). Lorsque vous créez un nouveau jeton pour la collection, comme nous l'avons fait précédemment, cette information se met à jour automatiquement.

Avec tout configuré, nous sommes maintenant prêts à envoyer la requête que nous avons essayée plus tôt, cette fois avec un jeton d'accès valide dans l'en-tête "Authorization".

![Inspection de l'onglet "Headers" de la requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725825252369/eedff426-4843-4e63-8022-28ca6f783f8a.png align="center")

Et si nous cliquons maintenant sur "Send", nous obtiendrons une réponse comme celle-ci :

![Affichage de la réponse JSON de la requête HTTP envoyée dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725905470563/ac771bf6-a278-4564-8360-6397b01ea05c.png align="center")

La réponse est un objet JSON contenant beaucoup d'informations à explorer. Vous pouvez le faire pour votre propre playlist également, tant qu'elle est définie sur publique sur Spotify.

Pour donner un autre exemple, je vais aller sur Spotify, utiliser l'option "Partager" pour ma playlist, et copier le lien de la playlist, qui ressemble à ceci : `https://open.spotify.com/playlist/1OPgvkPckzXm9SB0CIJf3o?si=cbe9c361f8024abd`.

La partie qui nous intéresse est l'ID de la playlist, qui se trouve après le dernier slash et avant le point d'interrogation — dans ce cas, `1OPgvkPckzXm9SB0CIJf3o`. Nous remplacerons l'ID de playlist actuel par celui-ci dans Postman :

![Ajustement du "Playlist ID" pour la requête HTTP dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725905870964/588a8569-b8b3-48f4-98c6-3bf1cb636dd1.png align="center")

Maintenant, si nous cliquons sur "Send", nous recevrons la réponse JSON correspondante :

![Inspection de la réponse JSON de la requête HTTP ajustée dans Postman](https://cdn.hashnode.com/res/hashnode/image/upload/v1725905937409/3dd3c6b2-cacb-4a1c-9f2b-687772b34fae.png align="center")

Cette réponse est également un volumineux objet JSON avec de nombreuses données à explorer.

Et voilà ! Nous avons configuré avec succès une installation Postman fondamentale avec une requête HTTP GET, incluant l'autorisation, pour récupérer des données de l'API Spotify.

## Portées d'autorisation de l'API Spotify

À présent, nous avons utilisé avec succès l'autorisation avec notre Client ID et notre Client Secret. Mais si vous plongez plus profondément dans la documentation de l'API Spotify, vous trouverez des situations où cette méthode d'autorisation est insuffisante pour certaines actions.

Alors que la récupération des données de playlist et d'autres requêtes GET fonctionnent avec l'autorisation Client ID et Client Secret, vous pouvez rencontrer des endpoints qui utilisent les méthodes POST, PUT ou DELETE.

Par exemple, ajouter de nouvelles chansons à une playlist nécessite plus qu'une simple autorisation Client ID et Client Secret. Vous devez vous authentifier en tant qu'utilisateur réel associé à la playlist.

Dans de tels cas, la documentation énumère des "Authorization scopes" (portées d'autorisation) qui définissent les permissions requises. Par exemple, les portées "playlist-modify-public" et "playlist-modify-private" sont nécessaires pour modifier respectivement les playlists publiques et privées :

![Reconnaissance des "Authorization scopes" mentionnés pour l'endpoint "Add Items to Playlist" dans l'API Spotify](https://cdn.hashnode.com/res/hashnode/image/upload/v1725972202770/5109da66-792a-4430-855c-9c6db4d06105.png align="center")

Si vous examinez la documentation de l'API Spotify, vous verrez qu'elle décrit quatre méthodes d'autorisation principales :

* [Code d'autorisation](https://developer.spotify.com/documentation/web-api/tutorials/code-flow)
    
* [Code d'autorisation avec extension PKCE](https://developer.spotify.com/documentation/web-api/tutorials/code-pkce-flow)
    
* [Identifiants client (Client credentials)](https://developer.spotify.com/documentation/web-api/tutorials/client-credentials-flow)
    
* [Octroi implicite (Implicit grant)](https://developer.spotify.com/documentation/web-api/tutorials/implicit-flow)
    

La méthode Client credentials (que nous avons utilisée) ne permet pas d'accéder aux données spécifiques de l'utilisateur. Pour effectuer des actions au nom d'un utilisateur, comme modifier ses playlists, la méthode "Authorization code" est requise.

Dans les projets du monde réel, vous implémenteriez généralement cela dans le cadre du processus d'authentification et d'autorisation de votre application lorsque les utilisateurs se connectent. Par exemple, dans les projets Next.js, NextAuth propose un mécanisme de connexion Spotify qui simplifie ce processus.

Alternativement, vous pourriez gérer manuellement les requêtes nécessaires pendant le processus d'authentification et ajouter les données pertinentes aux informations de session.

Ce sujet dépasse le cadre de ce guide, car il traite des flux généraux d'autorisation et d'authentification pour l'API Spotify (et d'autres API) plutôt que des cas d'utilisation spécifiques à Postman. Mais la documentation de l'API Spotify fournit des ressources précieuses si vous souhaitez explorer des tests plus avancés avec Postman. Ils fournissent également un [guide pratique](https://developer.spotify.com/documentation/web-api/howtos/web-app-profile) sur la récupération des données de profil d'un utilisateur et leur affichage dans votre application frontend.

## Résumé

Dans ce guide, nous avons couvert les fondamentaux de Postman : comment configurer votre premier espace de travail avec une collection, créer une requête HTTP, utiliser des variables pour simplifier le processus des requêtes futures, et ajouter une logique d'autorisation pour obtenir un jeton d'accès requis pour effectuer des requêtes. Tout cela a été démontré à l'aide de l'API Spotify, qui fournit une documentation complète sur l'accès à ses endpoints.

À partir d'ici, vous voudrez peut-être explorer davantage en apprenant à accéder aux endpoints de l'API Spotify qui nécessitent des informations d'accès spécifiques à l'utilisateur, combinées à des portées spécifiques, comme l'ajout de nouvelles chansons à une playlist Spotify.