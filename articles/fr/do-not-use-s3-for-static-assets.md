---
title: Pourquoi vous ne devriez pas utiliser AWS S3 ou CloudFront pour livrer des
  actifs statiques
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-06-01T00:20:00.000Z'
originalURL: https://freecodecamp.org/news/do-not-use-s3-for-static-assets
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9ab0740569d1a4ca271f.jpg
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
seo_title: Pourquoi vous ne devriez pas utiliser AWS S3 ou CloudFront pour livrer
  des actifs statiques
seo_desc: "By Mehul Mohan\nAWS is THE cool kid in the town. Every comparison of different\
  \ cloud providers is incomplete unless you compare them with AWS at least once.\
  \ \nBut S3, the most popular solution for storing on the cloud and the one everyone\
  \ loves, should..."
---

Par Mehul Mohan

AWS est LE chouchou de la ville. Toute comparaison des différents fournisseurs de cloud est incomplète si vous ne les comparez pas avec AWS au moins une fois. 

Mais S3, la solution la plus populaire pour stocker dans le cloud et celle que tout le monde adore, ne devrait pas toujours être votre choix. Dans cet article, je vais expliquer pourquoi.

_**Note :** Ne me criez pas immédiatement dessus sur la manière et les raisons pour lesquelles AWS est le meilleur. Je sais qu'ils sont au sommet du cloud computing - et en aucun cas je n'essaie de cibler leurs pratiques commerciales et services._   
  
_J'ai moi-même utilisé CloudFront + S3, ainsi que DigitalOcean + Cloudflare, et j'ai exposé mes observations. Prenez mes pensées de manière constructive, et si vous pensez que j'ai fait des erreurs, tweetez-moi à [mehulmpt](https://twitter.com/mehulmpt)._

## CloudFront + S3

CloudFront est un autre service souvent utilisé (et recommandé) avec S3 lorsque vous essayez de distribuer des fichiers numériquement dans le monde entier. CloudFront est un CDN d'Amazon avec des serveurs de périphérie dans le monde entier. Voici comment cela fonctionne :

Votre utilisateur, disons de l'Inde, essaie de charger votre site web dont le serveur est situé aux États-Unis. Supposons que vous utilisez une SPA comme React ou Angular. La première page index.html se chargera à partir de votre serveur d'origine (il est généralement bon de ne jamais mettre en cache les pages HTML, surtout si vous utilisez des applications SSR pour éviter les problèmes de cache). 

Après cela, si vous avez hébergé vos fichiers JS/CSS sur CloudFront (S3), ces appels seront effectués vers un nom de domaine de CloudFront qui se résout en une adresse IP d'une machine la plus proche de votre emplacement. Dans ce cas, il s'agit probablement d'un serveur AWS situé dans un centre de données à Mumbai, en Inde.

À partir de ce moment, ce serveur a la responsabilité de livrer ce fichier. Deux choses peuvent se produire :

* votre fichier est déjà disponible sur ce serveur de Mumbai (mis en cache), et ce serveur vous retourne ce fichier immédiatement (cache hit), 
* ou il n'a pas ce fichier et doit effectuer un voyage vers votre serveur d'origine (le bucket S3 dans ce cas) pour obtenir ce fichier.

Mais même s'il y a un cache miss, il y a de fortes chances que ce soit encore plus rapide pour un utilisateur par rapport à ne pas avoir CloudFront en avant. 

Pourquoi ? Parce que lorsqu'il y a un cache miss et que le serveur de périphérie essaie d'atteindre le serveur principal, il utilise une ligne de connexion internet Tier 1 exploitée par Amazon - une entreprise américaine valant des billions de dollars. Ils ont probablement une bien meilleure connectivité internet et une latence inférieure à ce que votre FAI peut offrir. 

De plus, parce qu'ils sont sur le même réseau mondial Amazon, ils peuvent faire quelques optimisations pour gagner plus de temps.

D'accord ! Cela semble bien jusqu'à présent, alors quel est le problème ? Retenez vos chevaux, nous y viendrons.

# Compression des actifs

CloudFront vous permet de livrer des actifs compressés en utilisant GZIP. Mais il y a un autre outil encore plus cool sur le marché : la compression brotli. Et elle est supportée par presque tous les principaux navigateurs. 

Brotli compresse vos données de transmission encore plus. Cela signifie que ce n'est pas seulement bon pour votre portefeuille, mais aussi pour l'utilisateur final (parce qu'il passera moins de temps à voir cet écran de chargement/blanc).

Amazon CloudFront ne supporte pas encore la livraison de compression brotli. Et je ne les en blâmerai pas non plus. Cela est dû au fait que la compression brotli est lente à faire à la volée (CloudFront fait du gzip à la volée), donc ils ne l'ont pas encore implémentée.

Bien sûr, alors faisons-le nous-mêmes et stockons-le sur S3 et livrons la version compressée, n'est-ce pas ? Malheureusement, ce n'est pas si simple, et nous allons bientôt plonger dans un problème d'architecture.

Une URL d'actif typique ressemblerait à ceci : http://mysite/assets/javascript/file.js

Lorsque votre navigateur fait une demande, il envoie un en-tête : Accept-Encoding. Cet en-tête peut contenir des algorithmes de compression que votre navigateur peut supporter, comme gzip, deflate, brotli, etc. Le serveur doit maintenant agir intelligemment pour avoir une efficacité maximale.

1. Si le client supporte brotli, alors livrez toujours l'actif compressé brotli.
2. Si le client supporte gzip, alors livrez toujours gzip.
3. Sinon, livrez le fichier original.
4. Assurez-vous également que dans le type de réponse, le Content-Encoding correct est défini afin que le navigateur puisse reconnaître l'algorithme de compression.

Maintenant, tout d'abord, vous devez créer 3 variantes de chaque fichier d'actif :

1. file.js
2. file.js.br - brotli
3. file.js.gz - gzip

Et vous devez les livrer _conditionnellement_ en fonction du support du navigateur. CloudFront est un CDN "stupide" - il va simplement mapper votre URL de demande au fichier sur votre serveur. Il ne peut effectuer aucune transformation à moins que... vous optiez pour un autre service AWS - les fonctions Lambda@edge

Nous savons tous probablement ce qu'est Lambda sur AWS - vous pouvez exécuter des fonctions sur le cloud sans vous soucier de la mise à l'échelle ou de la réduction de l'infrastructure sous-jacente. Tarification par demande d'API, limitée dans le temps, génial. Lambda@edge est un service similaire mais conçu pour les serveurs de périphérie (centres de données CDN CloudFront)

Vous pouvez techniquement configurer un serveur Lambda pour agir comme un "intermédiaire" entre la demande faite par votre client et le CDN CloudFront. Lambda peut ouvrir la demande, voir les en-têtes de contenu supportés, modifier l'URL en conséquence et la transmettre au CloudFront "stupide" qui va récupérer le fichier de l'URL modifiée ensuite. 

Par exemple, si Lambda voit que le navigateur a envoyé un Accept-Encoding: br, alors lambda peut être utilisé pour modifier l'URL de la demande de /javascript/file.js à /javascript/file.js.br sans en informer le côté utilisateur. Cloudfront va maintenant récupérer une charge utile plus petite et retourner une réponse pour un encodage brotli. GAGNÉ !

Mais c'est bien, n'est-ce pas ? OÙ est le problème ? Le problème est... le prix.

## AWS est ridiculement cher (pour cette tâche)

Tout ce que vous avez fait jusqu'à présent semble et paraît très bien. Mais lorsque vous regardez ce qui se passe lorsque vous commencez à atteindre des nombres significatifs, vous réaliserez qu'AWS n'est pas génial en matière de transfert de données. [Zoom a récemment quitté AWS pour la même raison](https://www.lastweekinaws.com/blog/why-zoom-chose-oracle-cloud-over-aws-and-maybe-you-should-too/). 

De plus, avec la compression des actifs, vous devez maintenant payer pour les appels Lambda@edge. J'ai découvert que la mise en œuvre de Lambda@edge réduira en fait vos coûts, sinon vous paierez beaucoup plus pour AWS pour le trafic !

CloudFront fonctionne sur la tarification du transfert de données. Il ne vous facture pas lorsqu'il récupère des données depuis le bucket S3, il vous facture lorsqu'un utilisateur récupère des données depuis les serveurs de périphérie.

## Limite de coût supérieure

Dans le pays le plus cher - l'Inde - CloudFront vous facture 0,170 USD par Go de données transférées. C'est énorme ! 

Disons que vous avez un site web populaire (principalement) indien avec environ 50 000 utilisateurs visitant votre site quotidiennement. Supposons également que vous apportez des modifications de conception chaque semaine sur votre site (assez courant pour les produits à itération rapide), vous devez donc invalider le cache du navigateur et de CloudFront.

Supposons également qu'en moyenne, un seul utilisateur télécharge environ 10 Mo d'actifs statiques depuis votre site (incluant CSS/JS/images/polices) hébergés sur S3 via CloudFront.

Calculons le coût :

1. 50 000 utilisateurs indiens
2. 0,17 USD par Go
3. 10 Mo par utilisateur
4. Chaque utilisateur récupère cela 4 fois par mois (vous videz votre cache 4 fois - une fois par semaine)

Coût = 50000 * 0,17 * (10/1024) * 4 = 332 USD. C'est votre COÛT de transfert de données uniquement ! Je n'ai pas calculé le coût de stockage S3 et le coût d'hébergement du site. (Je n'ai pas non plus inclus la tarification lambda car ce n'est pas beaucoup => $(0,20 * (50 000 * 4))/1 million = 4 cents.)

## Limite de coût inférieure

Dans ce cas, supposons un site de trafic basé aux États-Unis. Les paramètres seraient maintenant :

1. 50 000 utilisateurs américains
2. 0,085 USD par Go
3. 3 Mo par utilisateur
4. Chaque utilisateur récupère cela 4 fois par mois (vous videz votre cache 4 fois - une fois par semaine)

Le coût = 50000*0,085*3*4/1024 = 50 USD. C'est le minimum que vous paierez en utilisant CloudFront avec le trafic mentionné (à condition que tous vos 50 000 utilisateurs soient uniquement des États-Unis). Et rappelez-vous, c'est le coût uniquement pour les transferts de données ! (Sans inclure les coûts du serveur pour héberger votre site web.)

## Alternative

Supposons maintenant que vous hébergez tous ces actifs statiques uniquement sur votre serveur principal - en reverse proxy via NGiNX et disons, en cours d'exécution sur une instance DigitalOcean de 60 $.

Votre transfert de données par mois = 50000 * (10/1024) * 4 = 1952 Go environ 2 To - DigitalOcean couvre votre 1 To de transfert par droplet gratuitement. Et c'est 10 $ par To à partir de là, donc cela coûtera 70 $ net pour faire fonctionner le serveur.

Bien sûr, vous aurez un peu de latence maintenant - parce que vous l'hébergez vous-même (nous allons même corriger cela plus tard). NGiNX est un serveur web haute performance et vous pouvez compter sur lui pour ne pas être un goulot d'étranglement dans la livraison de vos actifs statiques. 

Vous venez donc de réduire le coût de "transfert d'actifs uniquement" de 332 $ à 70 $ pour faire fonctionner le serveur entier ! Conseil bonus ? Nous nous concentrions sur l'exécution de cela uniquement en Inde, alors utilisez un serveur DigitalOcean en Inde. Cela signifierait moins de latence.

Non seulement cela, mais vous pouvez également opter pour le CDN Cloudflare - qui est GRATUIT. Cloudflare ne respectera pas vos fichiers à garder dans le CDN s'ils sont trop gros ou trop rarement consultés. Mais nous supposons un site très populaire ici, donc nous devrions être bien. Sinon, optez pour un autre service CDN, et je vous garantis qu'il coûtera moins de 332 $ par mois.

TL;DR - Si vous hébergez un site web avec des quantités de trafic moyennes à grandes avec des mises à jour planifiées régulièrement, il est beaucoup plus rentable d'héberger les actifs vous-même et d'utiliser des CDN externes (ou même des choses comme le CDN DigitalOcean) au lieu d'utiliser S3 et CloudFront (où les tarifs de trafic de données sont exorbitants).

## Conclusion

J'ai utilisé cette configuration (CloudFront + AWS S3) sur [codedamn.com](https://codedamn.com) - une plateforme pour les développeurs pour apprendre et grandir. J'ai rapidement réalisé que bien que cela semble fancy et que j'ai mis codedamn dans les grandes ligues - Amazon - ce n'est tout simplement pas assez efficace. 

Êtes-vous d'accord avec moi ? Que pensez-vous ? Faites-le moi savoir en [tweetant à mon Twitter](https://twitter.com/mehulmpt) ou en me contactant sur [Instagram](https://instagram.com/mehulmpt).

Paix !