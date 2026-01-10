---
title: Comment accélérer votre site web avec Azure CDN
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-26T15:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-speed-up-your-website-with-azure-cdn
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/cdn-cover.jpg
tags:
- name: Azure
  slug: azure
- name: 'content delivery network '
  slug: content-delivery-network
- name: Microsoft
  slug: microsoft
- name: web performance
  slug: web-performance
seo_title: Comment accélérer votre site web avec Azure CDN
seo_desc: 'By Arjav Dave

  What is a CDN?

  A Content Delivery Network (CDN) helps you deliver your content more quickly. You
  can serve any type of content that remains unchanged over a period of time, like
  images, videos, CSS, JavaScript, HTML files, PDFs, and mor...'
---

Par Arjav Dave

## Qu'est-ce qu'un CDN ?

Un réseau de diffusion de contenu (CDN) vous aide à livrer votre contenu plus rapidement. Vous pouvez servir tout type de contenu qui reste inchangé sur une période de temps, comme des images, des vidéos, du CSS, du JavaScript, des fichiers HTML, des PDF, et plus encore. 

Un CDN est un groupe de serveurs répartis dans le monde pour livrer le contenu à partir des serveurs de périphérie. Les serveurs de périphérie sont les serveurs situés le plus près de l'endroit d'où la requête est faite. 

Selon la requête, les serveurs de périphérie peuvent soit retourner le contenu à partir de leur cache, soit le récupérer à partir du serveur d'origine. Les serveurs qui servent le contenu réel sont appelés serveurs d'origine.

![Aperçu du CDN](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/0i7t9e95tryv3mi44ghc.png)

Dans l'image ci-dessus, les serveurs de périphérie sont situés autour du monde et le serveur d'origine est situé en Californie, États-Unis. Lorsqu'une requête est faite, le serveur de périphérie situé à Mumbai, en Inde, peut contacter le serveur d'origine s'il n'est pas en mesure de servir le contenu.

## Comment fonctionne un CDN ?

Les CDN ont quatre parties principales : un consommateur, un DNS, un serveur de périphérie et un serveur d'origine.

![Détail du CDN](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/gni65528kxlmciivhnyw.png)

Lorsque le consommateur fait une requête, elle est d'abord acceptée par son fournisseur de services Internet (FAI). Le FAI contactera ensuite le DNS autoritaire du fournisseur de contenu.

> Un DNS autoritaire convertit la requête DNS en une requête IP.

Lorsque le DNS autoritaire est consulté, il retourne l'adresse IP du serveur de périphérie le plus proche. Le serveur de périphérie vérifiera ensuite dans son propre cache si le contenu demandé est disponible. 

Si c'est le cas, il retourne le contenu. Si le contenu n'est pas disponible, il demande le contenu au serveur d'origine et le met en cache après l'avoir récupéré.

## Avantages d'un CDN

### Faible consommation de bande passante

De nombreux hébergeurs web ont une allocation de bande passante limitée par mois. Si vous dépassez cette limite, des frais supplémentaires vous seront facturés. 

Avec un CDN, la plupart de votre bande passante sera économisée puisque le contenu sera servi par les serveurs de périphérie.

### Faible latence

Les serveurs de périphérie mettent en cache le contenu. Ainsi, chaque fois que du contenu mis en cache est demandé, la latence est considérablement réduite. Cela est dû au fait que la requête ne va pas jusqu'au serveur d'origine.

### Sécurité contre les DDoS

Presque tous les CDN populaires ont la capacité de protéger votre serveur web contre les attaques par déni de service distribué (DDoS).

### Améliore le SEO

Le temps de chargement est l'un des facteurs qui peuvent affecter le classement SEO de votre site. Si vous servez la plupart de votre contenu via un CDN, les temps de chargement sont considérablement réduits et peuvent aider à améliorer votre SEO.

## Plongez dans Azure CDN

Supposons que vous avez créé un compte de stockage Azure et hébergé un site très simple qui affiche Hello World en tant que h1. Maintenant que vous connaissez les avantages des CDN, vous souhaitez servir votre site simple via un CDN. 

Vous aurez un point de terminaison comme _[https://demostorageaccountarjav.z29.web.core.windows.net/](https://demostorageaccountarjav.z29.web.core.windows.net/)_ (où au lieu de demostorageaccountarjav ce sera le nom de votre compte de stockage). Voici plus de détails sur la façon de [configurer un site web statique](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website).

Connectez-vous à votre portail Azure et cliquez sur _Créer une ressource_ depuis votre tableau de bord. Recherchez _CDN_ qui ouvrira la ressource dans la marketplace comme ci-dessous.

![Créer une ressource CDN](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ravgtt3j0xmeu5osd9d2.png)
_Créer un CDN_

Cela ouvrira un formulaire pour créer un profil CDN. Un profil CDN est un ensemble de points de terminaison CDN. Il n'y a pas grand-chose à remplir ici, à part le nom, le groupe de ressources et le niveau de tarification.

Ensuite, sélectionnez la case à cocher pour créer un point de terminaison CDN. Un point de terminaison est l'endroit où le consommateur demandera le contenu. Donc, si vous avez plusieurs sites, vous pouvez créer plusieurs points de terminaison également.

J'ai joint une capture d'écran pour votre référence sur les valeurs à mettre. Comme le CDN est un service global, la sélection de la région sera désactivée.

![Détails du CDN](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/z35xu3l7ox243ea6ecfj.png)
_Détails du CDN_

Vous pouvez maintenant cliquer sur _Créer_ pour générer le profil et le point de terminaison. Cela prendra quelques minutes pour être créé. Une fois créé et lorsque vous irez à l'écran d'accueil, vous aurez ces 4 ressources :

![Ressources Azure](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/o6bxldg59sqod68o4kq1.png)
_Ressources Azure_

Comme discuté précédemment, le profil CDN est un groupe de _Points de terminaison_. Pour voir les détails, cliquez sur la ressource *_Point de terminaison_. Vous verrez un aperçu avec un lien vers le _Nom d'hôte du point de terminaison_.

![Aperçu du point de terminaison](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/vt4t5uxyv6u0i5llicwp.png)
_Aperçu du point de terminaison_

Lorsque vous ouvrez le nom d'hôte du point de terminaison, il peut afficher "404 non trouvé" initialement. Vous devrez peut-être attendre encore 10-15 minutes avant que votre site réel ne soit visible.

Comme discuté dans la section [avantages](#heading-avantage-dun-cdn), vous pouvez configurer le point de terminaison pour la sécurité, la mise en cache, le routage et bien d'autres choses. Vous pouvez explorer plus d'options [ici](https://docs.microsoft.com/en-us/azure/cdn/cdn-how-caching-works).

## Comment accéder via un jeton SAS

Vous vous demandez peut-être quoi faire si votre ressource est dans un conteneur privé et ne peut être accessible que via un jeton de signature d'accès partagé (SAS). Eh bien, vous avez de la chance ! Les chaînes de requête sont transmises telles quelles et comme le SAS est une chaîne de requête, vous êtes prêt.

Allez-y et créez un nouveau compte de stockage (avec le site web statique désactivé). Ajoutez un nouveau point de terminaison dans le profil CDN qui pointe vers le compte de stockage nouvellement créé.

À des fins de démonstration, j'ai créé un conteneur nommé _site_ avec un niveau d'accès privé. Et j'ai téléchargé un Blob nommé _Photo.jpeg_ dans un compte de stockage avec l'URL [https://demostorageaccountarjav.blob.core.windows.net](https://demostorageaccountarjav.blob.core.windows.net).

Vous pouvez bien sûr obtenir un jeton SAS directement depuis le portail Azure pour les tests, mais ce n'est pas ainsi que vous le feriez habituellement dans le monde réel. Pour cela, vous trouverez ci-dessous un simple extrait de code pour créer un jeton SAS en Node.js.

```
const azureSasToken = require('azure-sas-token');
 
// La validité du jeton par défaut est de 7 jours
let sasToken = azureSasToken.createSharedAccessToken('https://<service namespace>.servicebus.windows.net/<nom du sujet ou de la file d'attente>',
                                '<nom de la clé de signature>',
                                '<hachage de la signature>');
console.log(`sasToken: ${sasToken}`);
 
// Spécifiez votre propre validité en secondes, deux heures dans cet exemple
sasToken = azureSasToken.createSharedAccessToken('https://<service namespace>.servicebus.windows.net/<nom du sujet ou de la file d'attente>',
                                '<nom de la clé de signature>',
                                '<hachage de la signature>', 
                                60 * 60 * 2);
console.log(`sasToken: ${sasToken}`);

```

Nous avons utilisé un simple package npm nommé [azure-sas-token](https://www.npmjs.com/package/azure-sas-token). Une fois le SAS généré, votre URL ressemblera à quelque chose comme ceci :

```
https://demostorageaccountarjav.blob.core.windows.net/site/Photo.jpeg?sp=r&st=2021-03-25T07:28:45Z&se=2022-02-02T15:28:45Z&spr=https&sv=2020-02-10&sr=b&sig=PD4HlRI8bDEirMevpYQgpx6drwh%2BE5EpILfXkQOMlvw%3D

```

L'URL ci-dessus pointe directement vers le compte de stockage. Alors, allez-y et changez l'origine pour qu'elle utilise le point de terminaison d'origine.

```
https://demowebsitearjav.azureedge.net/site/Photo.jpeg?sp=r&st=2021-03-25T07:28:45Z&se=2022-02-02T15:28:45Z&spr=https&sv=2020-02-10&sr=b&sig=PD4HlRI8bDEirMevpYQgpx6drwh%2BE5EpILfXkQOMlvw%3D

```

Lorsque vous visitez ce site, vous pourrez maintenant voir la ressource protégée via le CDN. Vous devrez peut-être attendre quelques minutes et/ou purger votre point de terminaison pour voir le contenu mis à jour.

## Conclusion

À mon avis, tout le monde devrait utiliser un réseau de diffusion de contenu. Il existe de nombreux autres fournisseurs comme Cloudflare, S3, et bien d'autres. Mais Microsoft est l'un des principaux acteurs émergents avec une large variété de services. 

Si vous êtes un fan d'Azure comme je le suis, vous devriez définitivement essayer Azure CDN.

Pour tout commentaire ou question, vous pouvez me contacter.

Consultez [ici](https://arjavdave.com) pour plus de tutoriels comme celui-ci.