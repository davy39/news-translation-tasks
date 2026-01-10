---
title: Comment les CDN aident à accélérer les performances en réduisant la latence
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-06-27T00:17:23.000Z'
originalURL: https://freecodecamp.org/news/cdns-speed-up-performance-by-reducing-latency
coverImage: https://www.freecodecamp.org/news/content/images/2023/06/pexels-pixabay-315934.jpg
tags:
- name: 'content delivery network '
  slug: content-delivery-network
- name: web performance
  slug: web-performance
seo_title: Comment les CDN aident à accélérer les performances en réduisant la latence
seo_desc: 'By Austin Gil

  In some recent tutorials, I covered supporting file uploads on the front end, supporting
  file uploads on the back end, and optimizing costs by moving file uploads to object
  storage.

  Today, I''ll continue to focus on more architectural wo...'
---

Par Austin Gil

Dans certains tutoriels récents, j'ai couvert [la prise en charge des téléchargements de fichiers sur le front-end](https://austingil.com/uploading-files-with-html/), [la prise en charge des téléchargements de fichiers sur le back-end](https://austingil.com/file-uploads-in-node/), et l'optimisation des coûts en [déplaçant les téléchargements de fichiers vers le stockage d'objets](https://austingil.com/upload-to-s3/).

Aujourd'hui, je vais continuer à me concentrer sur des travaux architecturaux, mais cette fois-ci, cela sera axé sur l'optimisation des performances.

%[https://www.youtube.com/watch?v=Vymnxp-t0qs]

## Aperçu de la solution de stockage d'objets

Supposons que nous avons une application qui stocke des fichiers téléchargés quelque part dans le monde. Pour cet exemple, il s'agit d'un [seau de stockage d'objets d'Akamai cloud computing services](https://www.linode.com/products/object-storage/), et je l'ai déployé dans la région `us-southeast-1`.

Vous pouvez utiliser un autre fournisseur et une autre région, mais les points suivants s'appliquent toujours.

Ainsi, lorsque je télécharge une photo mignonne de Nugget faisant un grand bâillement, je pourrai y accéder à une URL comme austins-bucket.us-southeast-1.linodeobjects.com/files/nugget.jpg

![Capture d'écran de mon navigateur montrant une photo mignonne de Nugget faisant un grand bâillement, et il y a une boîte mettant en évidence l'URL d'Akamai Object Storage.](https://austingil.com/wp-content/uploads/image-65-1080x608.png)

Nugget est un chien super mignon. Naturellement, beaucoup de gens vont vouloir voir cela. Malheureusement, parce que cette photo est hébergée dans la région `us-southeast-1`, toute personne vivant loin de cette région doit attendre plus longtemps avant que leurs yeux ne puissent se régaler de cette bête.

La latence est pénible.

Et c'est pourquoi les CDN existent.

## Qu'est-ce qu'un CDN ?

CDN signifie "**réseau de diffusion de contenu**". Il s'agit d'un réseau connecté d'ordinateurs répartis dans le monde entier et qui peuvent stocker des copies des mêmes fichiers afin que, lorsqu'un utilisateur fait une demande pour un fichier spécifique, il puisse être servi à partir de l'ordinateur le plus proche de l'utilisateur.

En utilisant un CDN, la distance qu'une demande doit parcourir est réduite. Cela aide à résoudre les demandes plus rapidement, indépendamment de l'emplacement de l'utilisateur.

Voici les [résultats des tests webpagetest.org](https://www.webpagetest.org/result/230417_BiDc3J_AP8/) pour cette photo de Nugget. La demande a été faite à partir de leurs serveurs au Japon, et il a fallu 1,1 seconde pour que la demande soit complétée.

![Image](https://austingil.com/wp-content/uploads/image-69-1080x723.png)

Au lieu de servir le fichier directement depuis mon seau de stockage d'objets, je peux configurer un CDN devant mon application pour mettre en cache la photo partout dans le monde.

Ainsi, les utilisateurs à Tokyo obtiendront la même photo, mais servie depuis l'emplacement CDN le plus proche (qui est probablement à Tokyo), et les utilisateurs à Toronto obtiendront ce même fichier, mais servi depuis l'emplacement CDN le plus proche (qui est probablement à Toronto).

Cela peut avoir des implications significatives sur les performances.

Regardons cette même demande, mais servie derrière un CDN. Les [résultats de webpagetest.org](https://www.webpagetest.org/result/230417_BiDc41_ARJ/) montrent toujours la même photo de Nugget, et la demande provient toujours de Tokyo, mais cette fois-ci, il n'a fallu que 0,2 seconde - **une fraction du temps !**

![Image](https://austingil.com/wp-content/uploads/image-68-1080x956.png)

Lorsque la demande est faite pour cette image, le CDN peut vérifier s'il a déjà une version mise en cache. Si c'est le cas, il peut répondre immédiatement. Si ce n'est pas le cas, il peut aller chercher le fichier original depuis le stockage d'objets, puis enregistrer une version mise en cache pour toute demande future.

**Note** : les chiffres rapportés ci-dessus proviennent d'un seul test. Ils peuvent varier en fonction des conditions du réseau.

## Les rendements composés des CDN

L'exemple ci-dessus s'est concentré sur l'amélioration des vitesses de livraison des fichiers téléchargés. Dans ce contexte, je ne traitais que d'une seule image téléchargée dans un seau de stockage d'objets. Il montre une amélioration de près d'une seconde complète des temps de réponse, ce qui est génial, mais les choses s'améliorent encore lorsque vous considérez d'autres types d'actifs.

Les CDN sont excellents pour tout actif statique (CSS, JavaScript, polices, images, icônes, etc.). En le plaçant devant mon application, tous les autres fichiers statiques peuvent également être automatiquement mis en cache. Cela inclut les fichiers que Nuxt.js génère dans le processus de construction et qui sont hébergés sur le serveur d'application.

Cela est particulièrement pertinent lorsque vous considérez le "[Chemin de rendu critique](https://developer.mozilla.org/en-US/docs/Web/Performance/Critical_rendering_path)" et les ressources bloquant le rendu comme le CSS, le JavaScript ou les polices.

Lorsque qu'une page web se charge, lorsque le navigateur rencontre une ressource bloquant le rendu, il mettra en pause l'analyse et ira télécharger la ressource avant de continuer (d'où le terme "bloquant le rendu"). Ainsi, toute latence qui affecte un seul actif peut également impacter les performances d'autres actifs plus bas dans la cascade réseau.

Cela signifie que les améliorations de performance d'un CDN sont cumulatives. Bien !

Alors, est-ce que cela concerne le fait de montrer des photos mignonnes de mon chien à plus de gens encore plus rapidement, ou est-ce que cela concerne le fait de vous aider à faire fonctionner vos applications plus rapidement ? OUI !

Quoi que ce soit qui vous motive à construire des sites web plus rapides, inclure un CDN dans votre infrastructure d'application est une étape cruciale si vous prévoyez de servir des clients depuis plus d'une région.

## Comment connecter le CDN Akamai au stockage d'objets

Maintenant, je veux faire une petite quête annexe et partager comment j'ai configuré Akamai avec le stockage d'objets. Je n'ai pas trouvé beaucoup d'informations sur le sujet, et j'aimerais aider toute personne dans cette situation spécifique. Si cela ne s'applique pas à votre cas d'utilisation, n'hésitez pas à sauter cette section.

Avec quelque chose comme 300 000 serveurs répartis dans 4 000 emplacements, Akamai est le plus grand fournisseur de CDN au monde. Il est utilisé par certaines des plus grandes entreprises du monde, mais il est difficile de trouver du contenu lié à Akamai car la plupart des grandes entreprises n'aiment pas partager des informations inutiles sur leur infrastructure.

Mais je ne suis pas la plupart des entreprises :)

(Note : Vous aurez besoin d'un compte Akamai et d'un accès à votre éditeur DNS)

Dans le [Akamai Control Center](https://control.akamai.com/), j'ai créé [une nouvelle propriété](https://control.akamai.com/apps/create/#/property/products) en utilisant le [produit Ion Standard](https://www.akamai.com/products/web-performance-optimization), qui est idéal pour la livraison CDN à usage général.

![Image](https://austingil.com/wp-content/uploads/image-71-1080x274.png)

Après avoir cliqué sur "Créer une propriété", vous serez invité à choisir entre utiliser l'assistant de configuration pour vous guider tout au long de la création de la propriété, ou vous pouvez passer directement aux paramètres du gestionnaire de propriétés pour la nouvelle propriété. J'ai choisi cette dernière option.

Dans le gestionnaire de propriétés, j'ai dû ajouter un nouveau nom d'hôte dans la section Noms d'hôte de la propriété. J'ai ajouté le nom d'hôte pour mon application. Il s'agit de l'URL où les utilisateurs trouveront votre application. Dans mon cas, c'était uploader.austingil.com.

![Image](https://austingil.com/wp-content/uploads/image-76-1080x520.png)

Une partie de ce processus nécessite également la configuration d'un certificat SSL pour le nom d'hôte. J'ai laissé la valeur par défaut sélectionnée pour Enhanced TLS.

![Image](https://austingil.com/wp-content/uploads/image-77-1080x520.png)

Avec tout cela configuré, Akamai me montrera le nom d'hôte de la propriété et le nom d'hôte Edge suivants. Nous reviendrons à ceux-ci plus tard lorsqu'il sera temps d'apporter des modifications DNS.

* **Nom d'hôte de la propriété** : uploader.austingil.com
* **Nom d'hôte Edge** : uploader.austingil.com-v2.edgekey.net

![Image](https://austingil.com/wp-content/uploads/image-72-1080x155.png)

Ensuite, j'ai dû configurer le comportement réel de la propriété, ce qui signifiait modifier la règle par défaut sous les paramètres de configuration de la propriété. Plus précisément, j'ai dû pointer le **Nom d'hôte du serveur d'origine** vers le domaine où mon serveur d'origine résidera.

![Image](https://austingil.com/wp-content/uploads/image-73-1080x761.png)

Dans mon DNS, j'ai créé un nouvel enregistrement A pointant origin-uploader.austingil.com vers l'adresse IP de mon serveur d'origine, puis j'ai ajouté un enregistrement CNAME qui pointe uploader.austingil.com vers le nom d'hôte Edge fourni par Akamai.

* A : origin-uploader.austingil.com -> IP du serveur d'origine
* CNAME : uploader.austingil.com -> uploader.austingil.com-v2.edgekey.net

Cela me permet de construire ma configuration CDN et de la tester selon les besoins, en n'envoyant le trafic à travers le CDN que lorsque je suis prêt.

Enfin, pour servir les fichiers dans mon instance de stockage d'objets via Akamai, j'ai créé une nouvelle règle basée sur le modèle de règle vide. J'ai défini les critères de la règle pour qu'ils s'appliquent à toutes les demandes allant au sous-chemin `/files/*`.

![Image](https://austingil.com/wp-content/uploads/image-74-1080x402.png)

Le comportement de la règle est configuré pour réécrire le nom d'hôte du serveur d'origine de la demande et le changer pour mon emplacement de stockage d'objets : npm.us-southeast-1.linodeobjects.com.

![Image](https://austingil.com/wp-content/uploads/image-75-1080x602.png)

Ainsi, toute demande allant à [uploader.austingil.com/files/nugget.jpeg](https://uploader.austingil.com/files/nugget.jpg) est servie **via** le CDN, mais le fichier provient de l'emplacement de stockage d'objets. Et lorsque vous chargez l'application, tous les actifs statiques générés par Nuxt sont également servis depuis le CDN. Toutes les autres demandes sont transmises via Akamai et transférées à origin-uploader.austingil.com, qui pointe vers le serveur d'origine.

Voici comment j'ai configuré le CDN Akamai pour qu'il se place devant mon application. J'espère que tout cela avait du sens, mais si vous avez des questions, n'hésitez pas à me les poser.

## Pour résumer

Aujourd'hui, nous avons examiné ce qu'est un CDN, le rôle qu'il joue dans la réduction de la latence du réseau et comment configurer le CDN Akamai avec le stockage d'objets.

Mais ce n'est que la partie émergée de l'iceberg. Il existe tout un monde de configuration de CDN à ajuster pour obtenir encore plus de performances.

Il existe également de nombreuses autres fonctionnalités de performance et de sécurité qu'un CDN peut offrir au-delà de la simple mise en cache des fichiers statiques : pare-feu d'applications web, résolution plus rapide des chemins réseau, [protection DDoS](https://www.akamai.com/solutions/security/ddos-protection), atténuation des bots, [calcul en périphérie](https://www.akamai.com/solutions/edge), optimisation automatisée des [images et vidéos](https://www.akamai.com/products/image-and-video-manager), analyse des logiciels malveillants, en-têtes de sécurité des demandes, et plus encore.

Mon collègue [Mike Elissen](https://www.linkedin.com/in/mikeelissen/) couvre également certains sujets de sécurité intéressants [sur son blog](https://blog.securitylevelup.eu/).

La chose la plus importante que je voulais transmettre aujourd'hui est que l'utilisation d'un CDN améliore les performances de livraison des fichiers en mettant en cache le contenu près de l'utilisateur.

Merci beaucoup d'avoir lu cet article. Si vous avez aimé cet article et souhaitez me soutenir, les meilleures façons de le faire sont de [le partager](https://twitter.com/share?via=heyAustinGil), de [vous inscrire à ma newsletter](https://austingil.com/newsletter/), et de [me suivre sur Twitter](https://twitter.com/heyAustinGil).

_Vous pouvez trouver cet article et mes autres articles publiés sur [austingil.com](https://austingil.com/file-uploads-cdn/).