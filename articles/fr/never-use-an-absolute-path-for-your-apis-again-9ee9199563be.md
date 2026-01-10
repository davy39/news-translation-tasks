---
title: Pourquoi vous ne devriez (presque) jamais utiliser un chemin absolu vers vos
  APIs à nouveau
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-11-25T00:15:36.000Z'
originalURL: https://freecodecamp.org/news/never-use-an-absolute-path-for-your-apis-again-9ee9199563be
coverImage: https://cdn-media-1.freecodecamp.org/images/1*jimGwpz6a99t5R_GfP15lA.jpeg
tags:
- name: AWS
  slug: aws
- name: Devops
  slug: devops
- name: Front-end Development
  slug: front-end-development
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Pourquoi vous ne devriez (presque) jamais utiliser un chemin absolu vers
  vos APIs à nouveau
seo_desc: 'By Vitaly Kondratiev

  Recent advances in web apps architecture show that a decoupled front-end provides
  more flexibility for development and operations. It


  lets you work on one end without depending on the other

  lets you build and deploy separately

  m...'
---

Par Vitaly Kondratiev

Les avancées récentes dans l'architecture des applications web montrent qu'un front-end découplé offre plus de flexibilité pour le développement et les opérations. Cela permet de :

* travailler sur une extrémité sans dépendre de l'autre
* construire et déployer séparément
* faciliter l'utilisation d'outils différents sur chaque extrémité

![Image](https://cdn-media-1.freecodecamp.org/images/Jqz03zZXEEbqT9zIoeVOdB6INAhaNScHYDpb)
_Architecture front-end découplée_

### Le problème

Lorsqu'une application est développée avec cette architecture en tête, le front-end doit communiquer avec le back-end via des APIs, généralement [REST](https://developer.mozilla.org/en-US/docs/Glossary/REST). Souvent, l'URL/port du serveur back-end diffère de celui du front-end, étant donné les chemins de déploiement séparés. Dans cet exemple, l'URL de l'application front-end est `https://www.appfocused.com` et le point de terminaison REST pour envoyer des emails de contact est servi depuis `[https://api.appfocused.com](https://api.appfocused.com.)`[.](https://api.appfocused.com.)

Une requête HTTP de l'application front-end vers le serveur back-end échouera car elle viole la [Same Origin Policy](https://developer.mozilla.org/en-US/docs/Web/Security/Same-origin_policy). Dans la console de Chrome, cela ressemblera à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/d9KvUeWl2nx51a4qv75ehlWIjx8VpoEqv3QE)
_Erreur CORS_

Pour des raisons de sécurité, les navigateurs restreignent les requêtes qui ne proviennent pas de la même origine. Cela empêche les attaquants d'injecter du code dans notre application et de voler nos informations sensibles. Les navigateurs ajoutent un en-tête `[origin](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Origin)` aux requêtes cross-origin pour informer le serveur d'une potentielle menace. Le serveur a alors l'autorité d'autoriser ou de rejeter ces origines en fournissant des en-têtes de réponse spécifiques, qui sont analysés par les navigateurs.

Il existe deux solutions pour résoudre ce petit problème :

* coder en dur les URLs absolues des APIs sur le client et configurer les en-têtes CORS sur le serveur
* utiliser des URLs relatives des APIs sur le client et utiliser une approche de reverse-proxy

Dans cet article, je parle de pourquoi la première approche avec les en-têtes CORS devrait être considérée comme un anti-pattern pour le code prêt pour la production. Je parle également de la manière de configurer l'approche reverse-proxy sur diverses configurations :

* serveur de développement local
* serveur web / serveur d'application
* serverless (CloudFront / S3 / Lambda)

### Rationale

La configuration des en-têtes CORS semble moins douloureuse à implémenter, et c'est le cas. Cependant, il y a quelques préoccupations à considérer qui m'ont fait prêcher pour l'**approche reverse proxy** dans presque toutes les circonstances.

Tout d'abord, le back-end peut ne pas vous appartenir et il peut être impossible de modifier les en-têtes CORS.

Si vous avez la chance de contrôler le back-end **et** pouvez configurer les en-têtes CORS, vous devrez maintenir une liste blanche de plusieurs clients web accédant au serveur API afin de leur donner accès. Bien sûr, le wildcard est également une option, mais il serait déraisonnable de mettre en liste blanche toutes les origines en définissant `access-control-allow-origin` sur `*` sauf si c'est un serveur public.

Un autre modèle courant, pendant le développement, est d'exécuter notre application UI à `localhost:$port`. Mais mettre en liste blanche localhost pour faciliter les appels API est un anti-pattern et doit être évité pour des raisons de sécurité.

Enfin, mais non des moindres, j'aime que ma build respecte le principe **Build Once, Deploy Many**. C'est l'un des principes fondamentaux de la **livraison continue**. Le binaire — dans notre cas, les fichiers statiques pour le client web — est construit une seule fois. Les déploiements, tests et releases ultérieurs ne doivent jamais tenter de reconstruire les artefacts binaires. Au lieu de cela, le binaire déjà construit doit être réutilisé.

En pratique, les URLs absolues codées en dur comme `https://api.appfocused.com/email/send` dans notre code client nous empêcheront d'avoir un seul artefact, car dans l'environnement de développement, je veux que mon client web appelle, par exemple, `https://api-dev.appfocused.com/email/send`.

> **_Ne codez jamais en dur une URL absolue d'API dans votre code client._**

Cela est devenu un mantra puissant pour moi et m'a aidé à surmonter certains défis sur le chemin.

### Solution

L'URL relative `/email/send` peut résoudre ce problème une fois pour toutes sur le client, rendant possible le Build Once, Deploy Many. C'est le travail du proxy d'orchestrer la requête plus loin. Il traite également des restrictions imposées par le navigateur. Le serveur proxy, dans ce cas, gère nos requêtes, réponses et effectue les modifications nécessaires pour faciliter la communication cross-origin.

#### Reverse proxy avec webpack-dev-server

Lorsque vous développez sur votre machine locale, vous voulez le même traitement pour votre API que sur les autres environnements. Webpack peut être configuré pour proxyfier les requêtes. Un exemple de "webpack.config.js" est :

```js
module.exports = {
  //...
  devServer: {
    proxy: {
      '/api': 'http://localhost:9000'
    }
  }
};
```

Une requête du client vers le chemin relatif `/api/users` proxyfiera maintenant la requête vers `http://localhost:9000/api/users`. Veuillez consulter la [documentation de Webpack](https://webpack.js.org/configuration/dev-server/#devserver-proxy) si vous souhaitez configurer des scénarios de réécriture d'URL ou ajouter un protocole sécurisé.

Le proxy peut également être configuré pour des projets construits sur Webpack comme [create-react-app](https://facebook.github.io/create-react-app/docs/proxying-api-requests-in-development#docsNav) ou [Gatsby](https://www.gatsbyjs.org/docs/api-proxy/).

#### Reverse proxy avec NGINX

[NGINX](https://www.nginx.com/) est un composant courant dans l'architecture des environnements de production. Il possède un certain nombre de fonctionnalités avancées d'équilibrage de charge, de sécurité et d'accélération que la plupart des applications spécialisées n'ont pas. L'utilisation de NGINX comme reverse proxy vous permet d'ajouter ces fonctionnalités à n'importe quelle application.

La configuration la plus simple du reverse proxy sur NGINX ressemblera à ceci, dans "etc/nginx/conf.d/app.conf"

```
server {
  listen 80;
  listen [::]:80;
  
  server_name appfocused.com;
  
  location /api {
      proxy_pass http://api.appfocused.com/;
  }
}
```

La directive `proxy_pass` fait de cette configuration un reverse proxy. Elle spécifie que toutes les requêtes qui correspondent au bloc de localisation — dans ce cas, le chemin `/api` — doivent être transférées à `http://api.appfocused.com`, où notre back-end est en cours d'exécution.

Consultez la [documentation complète](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/) pour des scénarios plus élaborés.

#### Reverse proxy avec serverless

Nous allons examiner la plateforme AWS pour un scénario serverless. Dans l'un de mes précédents articles, j'ai expliqué comment nous utilisons [l'architecture serverless pour héberger notre site web](https://www.appfocused.com/blog/static-site-with-aws-cloud-front-gatsby/). AWS CloudFront joue l'un des rôles clés, agissant comme CDN et fournissant une sécurité à la périphérie pour nos fichiers statiques stockés sur S3.

La première API que nous avons dû intégrer à cette configuration était un formulaire de contact. Le brief pour l'implémentation était le suivant :

> _Lorsque qu'un client poste à `https://www.appfocused.com/api/send/email`, la requête doit être routée vers `https://api.appfocused.com/api/send/email` où notre API back-end est déployée sous la forme d'une fonction Lambda._

Il s'avère que CloudFront supporte plusieurs serveurs d'origine. Il utilise des motifs de chemin pour déterminer vers quel serveur d'origine transmettre les requêtes. Plusieurs serveurs indépendants, même des systèmes qui ne sont pas à l'intérieur d'AWS, peuvent tous "posséder" un ou plusieurs chemins sous un seul nom d'hôte. L'un d'eux est celui par défaut et possède tous les chemins non explicitement configurés.

Le concept est très similaire aux reverse proxies dans NGINX ou Apache. Mais le routage des requêtes est effectué par CloudFront, qui se connecte au back-end approprié, envoie la requête et retourne — et éventuellement met en cache — la réponse. Il ne redirige pas la requête, donc l'URL ne change jamais pour le consommateur.

### Exemple de configuration CloudFront

Utilisez le nom d'hôte du site principal, par exemple `www.appfocused.com`, comme origine. Configurez le nom de domaine du site comme un nom de domaine alternatif dans CloudFront.

Ensuite, ajoutez une deuxième origine, dont la destination est le nom d'hôte où le déploiement WP peut être atteint. Créez un comportement avec un [motif de chemin](http://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/distribution-web-values-specify.html#DownloadDistValuesPathPattern) qui correspond à `/blog*` et utilise la deuxième origine.

Notre distribution CloudFront existante était configurée pour pointer vers notre contenu S3 statique généré par le formidable Gatsby. N'oubliez **pas** d'utiliser la suggestion automatique d'AWS lors de la création d'une nouvelle distribution avec intégration à S3. Entrez manuellement les [points de terminaison du site web](https://github.com/awsdocs/amazon-s3-developer-guide/blob/master/doc_source/WebsiteEndpoints.md) dans un format similaire à celui-ci `[http://appfocused.s3-website.eu-west-1.amazonaws.com](http://appfocused.s3-website.eu-west-1.amazonaws.com).)`[.](http://appfocused.s3-website.eu-west-1.amazonaws.com).)

Ensuite, nous allons ajouter notre deuxième origine pour servir les requêtes REST depuis API Gateway. Dans l'onglet "Origins", sélectionnez "Create Origin". Entrez le nom de domaine et laissez le chemin d'origine vide. Assurez-vous de sélectionner "HTTPS only" pour "Origin Protocol Policy".

![Image](https://cdn-media-1.freecodecamp.org/images/d1-jb6x0NPwljlX7bTp1j9NxfPccQKwzpzF4)
_Cloudfront : créer une origine_

Ensuite, allez dans l'onglet "Behaviors" et cliquez sur "Create Behavior" pour configurer le chemin.

![Image](https://cdn-media-1.freecodecamp.org/images/oqM3FKso86smQBaaetMgSAtHGgup0uyMcSVI)
_Cloudfront : créer un comportement_

Pour "Path Pattern", nous utiliserons `api/*`. Cela capturera toute requête commençant par `/api` telle que `[https://www.appfocused.com/api/send/email](https://www.appfocused.com/api/send/email)`.

Dans le menu déroulant "Origin", sélectionnez l'Origine que nous venons de créer. Cela garantira que la requête sera routée vers `[https://api.appfocused.com/api/send/email](https://api.appfocused.com/api/send/email)`.

Pour "Viewer Protocol Policy", sélectionnez "HTTPS only".

Pour "Allowed HTTP methods", sélectionnez "GET, HEAD, OPTIONS, PUT, POST, PATCH, DELETE".

Pour "Cache Based on Selected Request Headers", sélectionnez "Whitelist" et ajoutez les en-têtes requis. Cela empêche l'en-tête Host d'être transmis à l'origine.

Pour "Object Caching", sélectionnez "Use Origin Cache Headers".

Pour "Forward Cookies", sélectionnez "All".

Pour "Compress Objects Automatically", sélectionnez "Yes". Cela compressera les réponses en gzip.

CloudFront transmet très peu d'en-têtes à l'origine par défaut. Vous pouvez le configurer pour transmettre ce dont vous avez besoin, mais chaque en-tête que vous transmettez **réduira** votre taux de succès de cache. Personnellement, je transmets "Referer", "Accept", "Content-Type" et "Authorization".

Il y a cependant quelques mises en garde à la proxy serverless sur AWS. CloudFront ne supprimera pas les chemins.

Si une requête est envoyée à `https://www.appfocused.com/api/*`, elle sera routée vers `[https://api.appfocused.com](https://api.appfocused.comwith)`[avec](https://api.appfocused.comwith) le préfixe `/api`, et non à la racine du site.

Cela peut devenir un problème si vous ne possédez pas les APIs back-end ou, pour certaines raisons, celles-ci ne peuvent pas être modifiées. Si c'est le cas, [Lambda@Edge](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/lambda-at-the-edge.html) vient à la rescousse. Ce service vous permet de réécrire les chemins à la volée, au fur et à mesure que les requêtes sont traitées. Pour configurer Lambda@Edge, allez à l'élément CloudFront Behavior et choisissez "Lambda Function Associations".

### Conclusion

En implémentant le reverse proxy dans tous les environnements, nous obtenons :

* **Communication client-serveur sécurisée**
L'identité de vos serveurs back-end reste inconnue. Cela est utile en cas d'attaques DDoS
* **Build Once, Deploy Many**
Avec des chemins relatifs vers les APIs, vous pouvez construire une fois et déployer le même artefact dans plusieurs environnements
* **Same Origin**
Une configuration des en-têtes CORS sur le serveur n'est pas requise

Mon conseil personnel est : ne codez jamais en dur les chemins absolus vers vos APIs, sauf si c'est un prototype. Passez un peu plus de temps à configurer une couche reverse proxy pour faire les choses correctement.

_Cet article a été initialement publié sur le blog de mon entreprise. Notre mission chez Appfocused est d'aider les entreprises à exécuter [de grandes expériences utilisateur sur le web](https://www.appfocused.com) en utilisant notre vaste expérience, notre connaissance des tendances modernes de l'UI, des meilleures pratiques et de l'artisanat du code._