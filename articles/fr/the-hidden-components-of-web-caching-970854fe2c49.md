---
title: Les composants cachés de la mise en cache Web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-27T23:30:59.000Z'
originalURL: https://freecodecamp.org/news/the-hidden-components-of-web-caching-970854fe2c49
coverImage: https://cdn-media-1.freecodecamp.org/images/0*wIzKPeRpU_xcx6Cb.
tags:
- name: optimization
  slug: optimization
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Les composants cachés de la mise en cache Web
seo_desc: 'By Nick Karnik

  Caching allows you to increase application processing speed. Storing a copy of the
  previously fetched data or computed results increases processing speed. This enables
  future requests to be served faster. It is an effective architectur...'
---

Par Nick Karnik

La mise en cache vous permet d'augmenter la vitesse de traitement des applications. Stocker une copie des données précédemment récupérées ou des résultats calculés augmente la vitesse de traitement. Cela permet de servir les requêtes futures plus rapidement. Il s'agit d'un modèle architectural efficace, car la plupart des programmes accèdent aux mêmes données ou instructions encore et encore.

Elle est appliquée à tout, des navigateurs web aux serveurs web et des disques durs aux CPU. Adoptons une approche ascendante pour comprendre les différentes couches de la mise en cache. Nous nous concentrerons sur **où** les données peuvent être mises en cache plutôt que sur **comment** les mettre en cache.

### Cache CPU

La mémoire cache est un type de mémoire extrêmement rapide qui agit comme un tampon entre la RAM et le CPU. Elle contient les données et instructions fréquemment demandées afin qu'elles soient immédiatement disponibles pour le CPU lorsque nécessaire.

Les CPU sont construits avec une mémoire spéciale intégrée appelée 'Registres' qui consiste généralement en une petite quantité de stockage rapide. Ils sont les plus proches, les plus petits et les plus rapides de la mémoire disponible. Parfois, ces registres sont appelés 'cache L0'.

Les CPU ont également accès à jusqu'à quatre niveaux supplémentaires de caches allant du cache L1 (Niveau-1) au cache L4 (Niveau-4). Les architectures du CPU et de la carte mère déterminent si les registres sont L0 ou L1 cache. Ils déterminent également si les différentes couches résident sur le CPU ou la carte mère.

![Image](https://cdn-media-1.freecodecamp.org/images/0*RZp4MGsUeY5WBF5p.)
_Structure de la mémoire cache dans certains des nouveaux CPU_

### Disques

Les disques durs (HDD) sont lents par rapport à la mémoire vive volatile (RAM), mais ils deviennent plus rapides avec les disques à état solide (SSD).

Dans le stockage informatique, le cache de disque (a.k.a. tampon de disque ou tampon de cache) est la mémoire intégrée dans un disque dur agissant comme un tampon entre le CPU et le disque dur physique utilisé pour le stockage.

![Image](https://cdn-media-1.freecodecamp.org/images/0*c9StOFkBugF3htST.)
_Un cache de disque cherche à tirer parti des vitesses de mémoire plus rapides_

Les caches de disque fonctionnent sur le principe que lorsque vous lisez ou écrivez quelque chose sur le disque, il y a des chances que vous le relisiez bientôt.

### RAM

La différence entre le stockage des données temporaires sur la RAM et le HDD est leur performance, leur coût et leur proximité avec le CPU.

La RAM répond en dizaines de nanosecondes tandis que les HDD répondent en dizaines de millisecondes. Cela représente une différence de **six ordres de grandeur** !

![Image](https://cdn-media-1.freecodecamp.org/images/0*lYdjMm5CnJ8PQYBt.)

Une compréhension plus approfondie du fonctionnement de la mise en cache vous permettra de concevoir des applications hautement efficaces, peu coûteuses et maintenables.

### Serveur Web Simple

Lorsque vous faites une requête web, elle va de votre navigateur web à un serveur web qui sert des ressources statiques à partir du système de fichiers sur un disque dur.

![Image](https://cdn-media-1.freecodecamp.org/images/0*3dwP0FGAeaLhkaqw.)
_Serveur Web Simple_

Supposons que nous servons un fichier statique lorsqu'un site web est demandé. Dans un flux de travail typique, la requête entrante sera gérée par le serveur web. Il récupérera le fichier depuis le disque dur et répondra avec son contenu.

À la première requête, le disque dur vérifiera le cache, ce qui entraînera un "cache miss". Il procédera à la récupération des données depuis le disque dur et les stockera dans le cache, en supposant qu'elles pourraient être demandées à nouveau.

À une requête ultérieure, la recherche dans le cache entraînera un "cache hit". Ces données seront servies depuis le tampon jusqu'à ce qu'elles soient écrasées et qu'une recherche entraîne un cache miss.

### Mise en Cache de Base de Données

Les requêtes de base de données peuvent être lentes et intensives car les résultats peuvent nécessiter d'être calculés sur le serveur de base de données. Si ces requêtes sont répétées, les mettre en cache dans la base de données améliorera leur temps de réponse. Cela est également utile lorsque plusieurs machines accèdent à la même base de données et exécutent la même requête.

![Image](https://cdn-media-1.freecodecamp.org/images/0*0pYIm5ZCtHyUNesV.)
_Serveur Web Simple avec une Base de Données_

La plupart des serveurs de base de données seront configurés dès la sortie de l'usine pour une mise en cache optimale. Cependant, il existe de nombreux paramètres qui peuvent être modifiés pour servir les besoins de votre application.

### Mise en Cache des Réponses

Le serveur web peut être configuré pour mettre en cache les réponses afin qu'il ne transfère pas de requêtes similaires à l'hôte de l'application. De même, l'hôte de l'application peut mettre en cache des parties de ses réponses aux requêtes coûteuses de la base de données ou aux fichiers fréquemment demandés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*oUpWqEXElez_Ytsu.)
_Mise en Cache des Réponses et de l'Application_

La réponse du serveur web est mise en cache en mémoire. Le cache de l'application peut être stocké localement en mémoire ou sur un serveur de cache qui exécute un magasin de structures de données en mémoire comme Redis.

> Le serveur web et l'hôte de l'application pourraient faire partie du même service ou de services séparés selon l'architecture de l'application.

### Mémoisation de Fonction

La mémoisation est une forme de mise en cache où vous optimisez les appels de fonction coûteux afin qu'ils ne s'exécutent qu'une seule fois pour une entrée spécifique. Cela est accompli via des tables de recherche où les clés correspondent aux paramètres d'entrée de la fonction et la valeur est le résultat.

![Image](https://cdn-media-1.freecodecamp.org/images/0*OgCEejNKL3VnNiPC.)
_Mémoisation de Fonction via Table de Recherche_

Il s'agit d'une technique courante utilisée pour accélérer les programmes. Cependant, elle peut ne pas être idéale pour les fonctions rarement appelées ou les fonctions qui ont des temps de réponse rapides.

### Mise en Cache du Navigateur via les En-têtes HTTP

Chaque navigateur est livré avec une implémentation d'un cache HTTP (a.k.a. cache web) pour le stockage temporaire de documents web tels que les pages HTML, les fichiers javascript et les images.

Cela est utilisé lorsque la réponse du serveur fournit les directives d'en-tête HTTP correctes pour instruire le navigateur sur le moment et la durée pendant lesquels le navigateur peut mettre en cache la réponse.

Il s'agit d'une fonctionnalité très puissante car elle présente plusieurs avantages :

* L'expérience utilisateur est améliorée car les ressources sont chargées rapidement depuis le cache local. Il n'y a pas de temps de trajet aller-retour (RTT) car les requêtes ne sont pas envoyées sur le réseau.
* Cela réduit la charge sur le serveur d'application et les autres composants dans le pipeline.
* Tout le monde économise en payant pour une bande passante inutile et cela libère cette bande passante pour d'autres utilisateurs sur Internet.

![Image](https://cdn-media-1.freecodecamp.org/images/0*4lXcgXk1zfsB8W6Y.)
_Mise en Cache du Navigateur_

### Serveur Proxy

Dans les réseaux informatiques, un serveur proxy est un système informatique, un appareil matériel ou une application. Il agit comme un intermédiaire pour les requêtes des clients qui cherchent des ressources auprès d'autres serveurs et vice versa.

Il existe diverses formes de serveurs proxy. Ils peuvent résider sur l'ordinateur local d'un utilisateur, un routeur réseau ou sur divers serveurs intermédiaires entre le client et l'hôte de destination. Tous les serveurs proxy sont capables de mettre en cache.

Examinons les variations courantes d'un serveur proxy.

#### Passerelle

Un serveur proxy qui transmet simplement une requête sortante ou une réponse entrante sans la modifier est connu sous le nom de **passerelle, proxy de tunneling, proxy web, proxy ou proxy de niveau application**. Ces proxys sont généralement partagés par tous les clients à l'intérieur d'un pare-feu, ce qui en fait de bons candidats pour la mise en cache des requêtes.

#### Proxy Direct

Un proxy direct (a.k.a serveur proxy) est généralement installé sur l'infrastructure côté client. Un navigateur web configuré pour utiliser un proxy direct lui enverra une requête sortante. Elle sera ensuite transmise au serveur de destination sur Internet. L'un des avantages d'un proxy direct est qu'il masque l'identité du client (Cependant, les VPN sont plus sûrs pour l'anonymat).

#### Accélérateur Web

Un accélérateur web est un serveur proxy qui réduit le temps d'accès au site web. Il le fait en préchargeant les documents qui sont susceptibles d'être consultés dans un avenir proche. Ils peuvent également compresser les documents, accélérer le chiffrement, réduire la qualité des images, etc.

#### Proxy Inverse

Un proxy inverse est généralement un proxy orienté vers l'intérieur utilisé pour empêcher l'accès direct à un serveur sur un réseau privé. Il est utilisé pour équilibrer la charge des requêtes entre les serveurs internes, fournir une authentification SSL ou une mise en cache des requêtes. Les hôtes côté serveur mettent en cache et ils peuvent aider à gérer un grand nombre de requêtes.

#### Mise en Cache en Périphérie

D'autre part, la mise en cache en périphérie (a.k.a. Réseaux de Livraison de Contenu (CDN)) fait référence à l'utilisation de serveurs de cache pour stocker du contenu plus près des utilisateurs finaux. Par exemple, si vous visitez un site web populaire et téléchargez du contenu statique qui est mis en cache. Chaque utilisateur suivant obtiendra ce contenu directement depuis le serveur de cache jusqu'à ce qu'il expire.

Le serveur d'origine est la source de vérité pour le contenu et est capable de servir tout le contenu disponible sur le CDN.

![Image](https://cdn-media-1.freecodecamp.org/images/0*bLYYC2v9zwIF5qNV.)
_Serveurs Proxy dans le pipeline de requête_

### Conclusion

La mise en cache se produit à chaque étape du pipeline, des matériels et logiciels aux appareils de mise en réseau et services. Elle joue un rôle significatif dans l'amélioration des performances globales du serveur d'origine. Chaque machine dispose d'un ensemble similaire de mécanismes de mise en cache autour du HDD et du CPU.

Les caches réduisent la latence et le trafic réseau et diminuent ainsi le temps nécessaire pour afficher une représentation d'une ressource. Toutes les applications web ont une forme de lag de réponse liée aux calculs du CPU. Par exemple, la recherche sur disque, la latence du réseau, la mise en file d'attente des requêtes, la limitation du réseau, etc. Si vous prenez en compte plusieurs combinaisons de ces éléments à travers les différentes machines du pipeline, le temps de trajet aller-retour s'accumule rapidement.

Enfin, voici quelques-uns des avantages que nous tirons de la mise en cache :

* Latence réduite améliore les temps de réponse.
* Temps de trajet aller-retour (RTT) améliorés grâce à un trafic web réduit.
* Débit plus élevé afin que le serveur d'origine puisse servir plus de requêtes.
* Consommation de bande passante réduite diminue le trafic réseau et réduit la congestion du réseau. Cela signifie que le contenu non mis en cache est récupéré beaucoup plus rapidement.
* Servir des documents à partir d'un cache proxy à proximité minimise le délai de transmission.
* La charge de travail du serveur web d'origine est réduite car divers caches à travers Internet servent des données.
* Dans les cas où un serveur distant peut ne pas être disponible en raison d'un crash ou d'un problème réseau, il peut être possible d'obtenir une copie mise en cache des ressources via un proxy.

#### Si cet article vous a été utile, ??? et Su[ivez-moi sur Twitter.](https://twitter.com/intent/follow?screen_name=theoutlander)

[**Extensions GitHub pour Booster Votre Productivité**](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)  
[_Voici les extensions GitHub que j'utilise. Elles vous permettront d'améliorer votre productivité sur GitHub. Veuillez partager votremedium.freecodecamp.org](https://medium.freecodecamp.org/github-extensions-to-boost-your-productivity-4692ad2b1796)