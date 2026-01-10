---
title: Comment utiliser les API REST – Un guide complet pour débutants
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-04-25T13:49:22.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-rest-api
coverImage: https://www.freecodecamp.org/news/content/images/2022/03/The-Complete-Guide-to-Understanding-and-Using-REST-APIs.png
tags:
- name: api
  slug: api
- name: REST API
  slug: rest-api
seo_title: Comment utiliser les API REST – Un guide complet pour débutants
seo_desc: 'By Alex Husar

  Application programming interfaces – or APIs – are an important programming concept
  to understand. And if you invest the time to learn more about these interfaces,
  it can help make your tasks more manageable.

  One of the common types of ...'
---

Par Alex Husar

Les interfaces de programmation d'applications – ou API – sont un concept de programmation important à comprendre. Et si vous investissez du temps pour en apprendre davantage sur ces interfaces, cela peut vous aider à rendre vos tâches plus gérables.

L'un des types courants d'API est une API REST. Si vous avez déjà envisagé d'obtenir des données d'un autre site web, comme Twitter ou GitHub, vous avez probablement utilisé ce type d'API.

Alors, pourquoi comprendre une API REST est-il utile ? Comment assure-t-elle la connectivité moderne des entreprises ?

Avant de construire ou d'opérer une API, ou une API REST en particulier, vous devriez d'abord apprendre ce qu'est une API. Cet article vous guidera à travers les principes des API REST et comment elles ont évolué en applications puissantes.

## **Comment fonctionnent les API et pourquoi en avez-vous besoin ?**

Les API représentent un ensemble de définitions et de protocoles. Vous en avez besoin pour le développement et l'intégration d'applications car elles facilitent l'échange de données entre deux logiciels, comme un fournisseur d'informations (un serveur) et un utilisateur.

Les API spécifient le contenu disponible pour le client qui fait l'appel à partir du producteur qui retourne la réponse.

Les programmes utilisent une API pour communiquer, récupérer des informations ou effectuer une fonction. Les API permettent aux utilisateurs de travailler avec le système pour obtenir le résultat souhaité.

Pour faire simple, une API agit comme un médiateur entre les utilisateurs (clients) et les ressources (serveurs).

Lorsque les utilisateurs font des requêtes API ou visitent une boutique en ligne, ils s'attendent à une réponse rapide. Vous devez donc [optimiser le TTFB de Magento (Time To First Byte)](https://onilab.com/blog/magento-ttfb-optimization/) ou utiliser d'autres stratégies d'amélioration des performances qui fonctionnent le mieux pour votre CMS.

Les raisons d'intégrer une API incluent :

* rationaliser le partage des ressources et des informations
* contrôler qui a accès à quoi avec l'aide de [l'authentification et de la définition des droits](https://www.freecodecamp.org/news/authenticate-and-authorize-apis-in-dotnet5/)
* sécurité et contrôle
* pas besoin de comprendre les spécificités du logiciel
* communication cohérente entre les services, même s'ils utilisent des technologies différentes

## **Aperçu des API REST**

![Image](https://lh3.googleusercontent.com/DUwmoHyRnoD1WovETSrQdSaIv8rh5WUVPxVjPN9_cvVokx7E4fZxzGyCY0_XMRA2cikjPkWIUDlXmtDqqGDX-KCzya5EVEEgxi8sEVwpVTeiHBNsqCULC-78QCE4dJ0_ieC1mQzn)

RESTful fait référence à l'architecture logicielle qui signifie « Representational State Transfer ». Vous en avez peut-être entendu parler dans le contexte de la standardisation de l'utilisation des systèmes d'échange d'informations (services web).

Ces services web utilisent un protocole sans état pour rendre les représentations textuelles de leurs ressources en ligne disponibles pour la lecture et le traitement. Un client effectue des activités bien connues basées sur le protocole HTTP comme fetch, update et delete.

REST a été établi pour la première fois en 2000 avec pour objectif d'améliorer les performances, la scalabilité et la simplicité en imposant des limites spécifiques à une API.

Il a gagné en popularité grâce à l'opportunité de couvrir divers appareils et applications. Ci-dessous, vous trouverez quelques-unes des raisons d'utiliser les API REST.

![Image](https://lh4.googleusercontent.com/Jk2xFwUgtgRzOuJuSa9kiWPPe51CN0qLd2hXMJ3F2SyW6MM10Gzq2qIY36dDQQj6fPJPG7Axl3q431QumWwi3WtYyFC1FA5TcI1i7i5PeQOO38tpdSCgIF0dJktnVhoWvVjAwFOK)

### 1. Utilisation Web

Il n'y a pas de technologie spécifique côté client pour REST car il convient à divers projets, tels que :

* développement web
* applications iOS
* appareils IoT
* applications Windows Phone

Comme vous n'aurez pas à vous en tenir à une pile spécifique côté client, vous pouvez construire n'importe quelle infrastructure pour votre entreprise.

### 2. Applications dans le Cloud

Les appels d'API REST sont idéaux pour les applications cloud en raison de leur caractère sans état. Si quelque chose ne va pas, vous pouvez redéployer des composants sans état, et ils peuvent croître pour gérer les changements de trafic.

### 3. Cloud Computing

Une connexion API à un service nécessite de contrôler comment l'URL est décodée. C'est pourquoi REST est devenu plus utile dans les services cloud.

L'architecture RESTful des API deviendra la norme à l'avenir, grâce au cloud computing et aux microservices.

## Comment fonctionnent les API REST ?

Les données (telles que des images, des vidéos et du texte) incarnent les ressources dans REST. Un client visite une URL spécifique et envoie une requête au serveur pour recevoir une réponse.

![Image](https://lh4.googleusercontent.com/HwYHNtAz8M84Tggswzk662nm_dyGUA77st12KGsiqw4rVBGqhJM2gQ5wgL2sL8ZhWmwOGsoEJx6Uqt7TdxU4Bkbg_uccr2UVTXtWsxnR495yZReGoY_reZEd9rq5_9vnjiaUUBs2)

### **Le Concept Derrière les API REST**

Une requête (l'URL que vous accédez) contient quatre composants, qui sont :

* le **endpoint**, qui est l'URL avec la structure `root-endpoint/?`
* la **méthode** avec l'un des cinq types possibles (GET, POST, PUT, PATCH, DELETE)
* les **headers**, servant diverses fonctions, y compris l'authentification et fournissant des informations sur le contenu du corps (vous pouvez utiliser l'option `-H` ou `--header` pour envoyer des headers HTTP)
* **data (ou body)**, ce que vous envoyez au serveur via l'option `-d` ou `--data` avec les requêtes POST, PUT, PATCH ou DELETE.

Les requêtes HTTP vous permettent d'opérer avec la base de données, telles que :

* Requête POST pour créer des enregistrements
* Requête GET pour lire ou obtenir une ressource (un document ou une image, une collection d'autres ressources) à partir du serveur
* Requêtes PUT et PATCH pour mettre à jour des enregistrements
* Requête DELETE pour supprimer une ressource d'un serveur

Ces opérations représentent quatre actions possibles, connues sous le nom de CRUD : Create, Read, Update et Delete.

![Image](https://lh5.googleusercontent.com/Quydyrq2Zw2Mh3uJj4G9LE40DhjJyWLjRCU9-hqs0uKt-hGCgoyGVP9eiU_6IBnb6GwxsILeu9kqjO5LQ6s7LBmHDtbksnqb13YtPoCKRq062zXi1Pz4wf0GAO27maHMlhamixAz)

Le serveur envoie les données au client dans l'un des formats suivants :

* [HTML](https://www.freecodecamp.org/news/html-best-practices/)
* JSON (qui est le plus courant grâce à son indépendance vis-à-vis des langages informatiques et à son accessibilité par les humains et les machines)
* XLT
* PHP
* Python
* texte brut

## Pourquoi utiliser une API REST ?

Pourquoi devriez-vous préférer REST aux autres API, comme SOAP ? Il y a de nombreuses raisons, comme la scalabilité, la flexibilité, la portabilité et l'indépendance.

![Image](https://lh4.googleusercontent.com/yJ2QDrpGbA-RpzwhXOXr1yl9aGTvVHXeiuyBvFxsMtE5KQu2wRmNLwlCX7cNGOlp1TjRK-P9VsBsFaGRNkxZw-QWvggxqXLYFtLg-THClHzB-5GJlMX6hGkY3DQnFh1YpzkHt2iE)

### Ne pas dépendre de la structure du projet

Une opération séparée du client et du serveur signifie que les développeurs ne sont pas liés à une partie spécifique du projet. Grâce aux API REST adaptatives, ils peuvent développer chaque aspect sans influencer un autre.

### Portabilité et adaptabilité

Les API REST fonctionnent uniquement lorsque les données de l'une des requêtes sont livrées avec succès. Elles vous permettent de migrer d'un serveur à un autre et de mettre à jour la base de données à tout moment.

### Opportunité de scaler le projet à l'avenir

Comme le client et le serveur agissent indépendamment, les codeurs peuvent développer rapidement le produit.

## **Caractéristiques du Style d'Architecture RESTful**

Les développeurs doivent considérer une structure rigide de certaines API, comme SOAP ou XML-RPC. Mais les API REST sont différentes. Elles supportent une large gamme de types de données et peuvent être écrites dans pratiquement n'importe quel langage de programmation.

Les six contraintes architecturales REST sont des principes pour concevoir la solution et sont les suivants :

![Image](https://lh5.googleusercontent.com/XRsmwgFoTf1sCI3hZf6n5DxHXDqHclunxf6ocqxjUVgWPss5KHiz8wm4fXYzCJ9mkijpfwhGc-YzSO_R1fm9JtOej1T1SQJwngs-wK_Lz0DhUwI2LfCOQWsZvm88nVlkGkmBgV-E)

### **1. Interface Uniforme (Une Interface Utilisateur Cohérente)**

Ce concept dicte que toutes les requêtes API pour la même ressource, quelle que soit leur origine, doivent être identiques, c'est-à-dire dans une langue spécifique. Une identification uniforme des ressources (URI) est associée aux mêmes données, comme le nom ou l'adresse e-mail d'un utilisateur.

Un autre principe d'interface uniforme stipule que les messages doivent être auto-descriptifs. Ils doivent être compréhensibles pour que le serveur puisse déterminer comment les traiter (par exemple, le type de requête, les types mime, etc.).

### **2. Séparation Client-Serveur**

Le style architectural REST adopte une approche particulière pour les implémentations client et serveur. Le fait est qu'elles peuvent être réalisées indépendamment et n'ont pas besoin de se connaître.

Par exemple, le client n'a que l'identification uniforme de la ressource (URI) de la ressource demandée et ne peut pas communiquer avec le programme serveur de quelque autre manière. D'un autre côté, le serveur ne doit pas affecter le logiciel client. Il envoie donc les données essentielles via HTTP.

Que signifie cela ? Vous pouvez modifier le code client à tout moment sans impacter le fonctionnement du serveur.

Le code serveur est dans le même bateau : changer le côté serveur n'affectera pas le fonctionnement du client.

Vous pouvez garder les programmes client et serveur à la fois modulaires et indépendants tant que chaque côté sait quel format de message livrer à l'autre.

Que réalisons-nous en séparant les problèmes d'interface utilisateur des contraintes de stockage des données ? Nous améliorons la flexibilité de l'interface entre les plateformes et augmentons la scalabilité.

De plus, chaque composant bénéficie de la séparation car il peut évoluer indépendamment. Une interface REST aide différents clients à :

* accéder aux mêmes endpoints REST
* exécuter des activités identiques
* recevoir des réponses similaires

### **3. Communication Sans État Entre Clients et Serveurs**

Les systèmes basés sur REST sont sans état, ce qui signifie que l'état du client reste inconnu du serveur et vice versa. Cette contrainte permet au serveur et au client de comprendre n'importe quel message envoyé, même s'ils n'ont pas vu les précédents.

Pour appliquer cette contrainte de caractère sans état, vous devez utiliser des ressources plutôt que des commandes. Ce sont les noms du web. Leur but est de décrire tout objet que vous pourriez vouloir garder ou communiquer à d'autres services.

Vous pouvez contrôler, changer et réutiliser des composants sans affecter le système dans son ensemble, donc les avantages de cette contrainte incluent l'obtention de :

* stabilité
* vitesse
* scalabilité des applications RESTful

Notez que chaque requête doit inclure toutes les informations nécessaires pour la compléter. Les applications client doivent sauvegarder l'état de la session puisque les applications serveur ne doivent pas stocker de données liées à une requête client.

### **4. Données Mise en Cache**

REST nécessite la mise en cache des ressources côté client ou côté serveur chaque fois que possible. La mise en cache des données et des réponses est cruciale dans le monde d'aujourd'hui car elle entraîne de meilleures performances côté client.

Comment cela affecte-t-il un utilisateur ? Une gestion bien gérée de la mise en cache peut réduire ou éliminer certaines interactions client-serveur.

Elle donne également au serveur plus d'options de scalabilité en raison de la charge plus faible sur le serveur. La mise en cache augmente la vitesse de chargement des pages et vous permet d'accéder au contenu précédemment consulté sans connexion Internet.

### **5. Architecture de Système en Couches**

![Image](https://lh3.googleusercontent.com/DBk2dcqnTMZdz-dBA0sFDUe5cQu71VxMqG8pW-ux4rqNvkVcsixRNR_ZyuY1z6UeWWZ5NRV11FPIv8XYK86EGr2G-Nnb7O_njC9PER6a5TdmfpZ2qmRTI7f9P--S7QU50cYwD9EC)

La structure de conception en couches RESTful est la prochaine contrainte à discuter. Ce principe implique de regrouper différentes couches avec des fonctions spécifiées.

Les couches de l'API REST ont leurs responsabilités et viennent dans un ordre hiérarchique. Par exemple, une couche peut être responsable du stockage des données sur le serveur, la deuxième pour le déploiement des API sur un autre serveur, et la troisième pour l'authentification des requêtes sur un autre serveur.

Ces couches agissent comme des médiateurs et empêchent l'interaction directe entre les applications client et serveur. En conséquence, un client ne sait pas quel serveur ou composant il adresse.

Que signifie le fait que chaque couche effectue sa fonction avant de transférer les données à la suivante ? Cela améliore la sécurité et la flexibilité globales de l'API car l'ajout, la modification ou la suppression d'API n'affecte pas les autres composants de l'interface.

### **6. Codage à la Demande (Non Obligatoire)**

Le scénario le plus courant d'utilisation des API REST est de fournir des représentations de ressources statiques en XML ou JSON.

Cependant, ce style architectural permet aux utilisateurs de télécharger et d'exécuter du code sous forme d'applets Java ou de scripts (comme JavaScript). Par exemple, les clients peuvent récupérer le code de rendu pour les widgets UI en appelant votre API.

## **Défis à Prévoir Lors de l'Utilisation des API REST**

Lorsque vous avez compris la conception et les contraintes architecturales des API REST, vous devez connaître les problèmes à prévoir lors de l'utilisation de ce style architectural :

![Image](https://lh3.googleusercontent.com/FnzdrS-v1CIkyY6lWVBZymkIbLGDOQb4ZFAPqcJD6_EDL9QL1Xd3KGwd2SP24GfYO2CTwO4-9ra4a8Dc8gOvokndr3uO7Zt0-VOjQjR6bdcLrSH3SWK0vmAeg5mZlEavHkgpsIhh)

### Accord sur les endpoints REST

Les API doivent rester cohérentes indépendamment de la construction de l'URL. Mais avec la croissance des combinaisons possibles de méthodes, il est plus difficile de maintenir l'uniformité dans les grandes bases de code.

### Versioning comme caractéristique des API REST

Les API nécessitent une [mise à jour ou un versioning régulier](https://www.freecodecamp.org/news/how-to-version-a-rest-api/) pour éviter les problèmes de compatibilité. Cependant, les anciens endpoints restent opérationnels, ce qui augmente la charge de travail.

### Beaucoup de méthodes d'authentification

Vous pouvez spécifier quelles ressources sont disponibles pour quels types d'utilisateurs. Par exemple, vous pouvez déterminer quels services tiers peuvent accéder aux adresses e-mail des clients ou à d'autres informations sensibles et ce qu'ils peuvent faire avec ces variables.

Mais les 20 différentes méthodes d'autorisation qui existent peuvent rendre votre premier appel API difficile. C'est pourquoi les développeurs ne poursuivent pas le projet en raison des difficultés initiales.

### Vulnérabilités de sécurité des API REST

Bien que les API RESTful aient une structure en couches, il peut encore y avoir certaines préoccupations de sécurité. Par exemple, si une application n'est pas suffisamment sécurisée en raison d'un manque de chiffrement, elle peut exposer des données sensibles.

Ou un pirate peut envoyer des milliers de requêtes API par seconde, provoquant une attaque DDoS ou d'autres abus du service API pour faire planter votre serveur.

### Collecte excessive de données et requêtes

Un serveur peut retourner une requête avec toutes les données, ce qui peut être inutile. Ou vous pourriez avoir besoin d'exécuter plusieurs requêtes pour obtenir les informations nécessaires.

## **Conclusion**

Il n'est pas surprenant que les API soient prédites pour rationaliser les communications basées sur le web à l'avenir. Leur but est de permettre à toute application web d'interagir et de partager des données.

Par exemple, elles aident les entreprises en ligne en croissance à développer des systèmes robustes et inventifs. À mesure que l'architecture API évolue, elle adopte des variantes plus légères et plus flexibles, qui sont cruciales pour les applications mobiles et les réseaux dispersés.

Donc, dans cet article, vous avez appris les bases de ce que vous devez savoir sur l'utilisation des API REST.