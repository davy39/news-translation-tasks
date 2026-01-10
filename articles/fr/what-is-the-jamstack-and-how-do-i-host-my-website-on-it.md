---
title: Qu'est-ce que le JAMstack et comment commencer ?
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-02-19T15:45:00.000Z'
originalURL: https://freecodecamp.org/news/what-is-the-jamstack-and-how-do-i-host-my-website-on-it
coverImage: https://www.freecodecamp.org/news/content/images/2020/02/what-is-jamstack-2.jpg
tags:
- name: architecture
  slug: architecture
- name: front end
  slug: front-end
- name: Front-end Development
  slug: front-end-development
- name: frontend
  slug: frontend
- name: HTML
  slug: html
- name: JAMstack
  slug: jamstack
- name: JavaScript
  slug: javascript
- name: software architecture
  slug: software-architecture
- name: Web Development
  slug: web-development
seo_title: Qu'est-ce que le JAMstack et comment commencer ?
seo_desc: 'JAMstack sites are all the rage right now in the web dev world. And rightfully
  so! But what exactly is it and how can we all take advantage of its benefits?


  What is this JAMstack?

  That’s not to be confused with serverless

  What makes up the JAMstack?...'
---

Les sites JAMstack sont très en vogue actuellement dans le monde du développement web. Et à juste titre ! Mais qu'est-ce que c'est exactement et comment pouvons-nous tous profiter de ses avantages ?

* [Qu'est-ce que ce JAMstack ?](#heading-quest-ce-que-ce-jamstack)
* [À ne pas confondre avec le serverless](#heading-a-ne-pas-confondre-avec-le-serverless)
* [Quels sont les composants du JAMstack ?](#heading-quels-sont-les-composants-du-jamstack)
* [Qu'est-ce qui rend une application JAMstack si géniale ?](#heading-quest-ce-qui-rend-une-application-jamstack-si-geniale)
* [Mon site web est-il considéré comme étant sur le JAMstack ?](#heading-mon-site-web-est-il-considere-comme-etant-sur-le-jamstack)
* [Quels sont quelques exemples de JAMstack ?](#heading-quels-sont-quelques-exemples-de-jamstack)
* [Quels sont quelques outils que je peux utiliser pour construire des sites ou applications JAMstack ?](#heading-quels-sont-quelques-outils-que-je-peux-utiliser-pour-construire-des-sites-ou-applications-jamstack)

## Qu'est-ce que ce JAMstack ?

Pour commencer, [JAMstack](https://jamstack.org/) est une architecture logicielle et une philosophie qui adhère aux composants suivants : JavaScript, APIs et Markup.

Si cela vous semble familier, c'est parce que ça l'est ! Cette application React que vous compilez avec [Webpack](https://webpack.js.org/) et que vous servez finalement depuis [S3](https://aws.amazon.com/s3/) ? Oui, c'est une application JAMstack. Ce simple fichier HTML qui n'a pas de JavaScript et qui ne fait littéralement rien de dynamique ? Oui, c'est aussi une application JAMstack.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/bill-ted-air-guitar.gif)
_Bill et Ted jouent de la guitare invisible_

## À ne pas confondre avec le serverless

Si vous venez davantage du côté cloud des choses (pensez à [AWS](https://aws.amazon.com/), [GCP](https://cloud.google.com/), [Azure](https://azure.microsoft.com/)), vous pourriez être enclin à penser que [serverless](https://serverless-stack.com/chapters/what-is-serverless.html) et JAMstack sont la même chose. Il est vrai qu'ils ont des similitudes dans la philosophie de la gestion des ressources, comme l'hébergement d'un site sur S3. Mais une application JAMstack n'est pas toujours une application serverless.

Prenons l'exemple d'une application hébergée dans un stockage statique sur le fournisseur cloud de votre choix. Oui, vous pourriez servir l'application de manière serverless, mais vous pourriez traiter avec une API qui utilise Wordpress ou Rails, deux technologies qui ne sont certainement pas serverless.

Combiner ces philosophies peut aller loin, mais elles ne doivent pas être confondues comme étant identiques.

## Quels sont les composants du JAMstack ?

Revenons au JAMstack : il est généralement composé de 3 composants : JavaScript, APIs et Markup. Son [histoire provient](https://snipcart.com/blog/jamstack) de l'évolution du terme "site statique" en quelque chose de plus significatif (et commercialisable). Ainsi, bien que le résultat final soit un site statique, il a été développé pour inclure des outils de première classe à chaque étape du processus.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/jamstack-breakdown-3.jpg)
_Découpage du JAMstack_

Bien qu'il n'y ait pas d'ensemble spécifique d'outils que vous devez utiliser, ou même d'outils au-delà du simple HTML, il existe de bons exemples de ce qui peut composer chaque partie de la stack. Plongeons un peu dans chaque composant.

### JavaScript

Le composant qui a probablement le plus contribué à populariser le JAMstack est JavaScript. Notre langage préféré pour les navigateurs nous permet de fournir toutes les parties dynamiques et interactives que nous n'aurions peut-être pas si nous servions du HTML simple sans lui.

C'est là que vous verrez souvent des frameworks UI comme [React](https://reactjs.org/), [Vue](https://vuejs.org/), et des nouveaux venus comme [Svelte](https://svelte.dev/) entrer en jeu.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/react-component-example.jpg)
_Exemple "Un composant simple" de [reactjs.org](https://reactjs.org/)_

Ils rendent la construction d'applications plus simple et plus organisée en fournissant des APIs de composants et des outils qui compilent en un simple fichier HTML (ou plusieurs).

Ces fichiers HTML incluent un groupe d'actifs comme des images, du CSS, et le JS réel qui sont finalement servis à un navigateur via votre CDN préféré (réseau de diffusion de contenu).

### APIs

Utiliser les forces des APIs est au cœur de la manière dont vous rendez une application JAMstack dynamique. Qu'il s'agisse d'authentification ou de recherche, votre application utilisera JavaScript pour faire une requête HTTP à un autre fournisseur qui améliorera finalement l'expérience d'une manière ou d'une autre.

[Gatsby](https://www.gatsbyjs.org/) a inventé l'expression "[content mesh](https://www.gatsbyjs.org/blog/2018-10-04-journey-to-the-content-mesh/)" qui décrit assez bien les possibilités ici.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/content-mesh-1.jpg)
_[Content Mesh](https://www.gatsbyjs.org/blog/2018-10-04-journey-to-the-content-mesh/)_

Vous n'avez pas nécessairement besoin de vous adresser à un seul hôte pour une API, mais vous pouvez vous adresser à autant que vous en avez besoin (mais essayez de ne pas en abuser).

Par exemple, si vous avez une API Wordpress headless où vous hébergez vos articles de blog, un compte [Cloudinary](https://cloudinary.com/) où vous stockez vos médias spécialisés, et une instance [Elasticsearch](https://www.elastic.co/) qui fournit votre fonctionnalité de recherche, ils travaillent tous ensemble pour offrir une expérience unique aux personnes utilisant votre site.

### Markup

C'est la pièce critique. Qu'il s'agisse de votre HTML écrit à la main ou du code qui compile en HTML, c'est la première partie que vous servez au client. C'est un peu une pièce de facto de tout site web, mais la manière dont vous le servez est la partie la plus importante.

Pour être considéré comme une application JAMstack, le HTML doit être servi de manière statique, ce qui signifie essentiellement qu'il n'est pas rendu dynamiquement depuis un serveur.

Si vous assemblez une page et la servez avec PHP, ce n'est probablement pas une application JAMstack. Si vous téléchargez et servez un seul fichier HTML depuis un stockage qui construit une application avec JavaScript, cela ressemble à une application JAMstack.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/aws-s3-static-files-gatsby.jpg)
_Sortie statique de Gatsby sur AWS S3_

Mais cela ne signifie pas que nous devons toujours construire 100% de l'application dans le navigateur. Des outils comme Gatsby et d'autres [générateurs de sites statiques](https://www.staticgen.com/) nous permettent de récupérer certaines ou toutes nos sources d'API au moment de la construction et de rendre les pages sous forme de fichiers HTML.

Imaginez que vous avez un blog Wordpress, nous pouvons récupérer tous les articles et finalement créer un nouveau fichier HTML pour chaque article. Cela signifie que nous allons pouvoir servir une version précompilée de la page directement au navigateur, ce qui équivaut généralement à un [premier rendu](https://developers.google.com/web/tools/lighthouse/audits/first-contentful-paint) plus rapide et une expérience plus rapide pour votre visiteur.

### Une note sur l'"hébergement"

Utiliser le terme hébergement ici peut être trompeur si vous êtes nouveau dans le concept. Oui, votre site est techniquement hébergé quelque part, mais pas au sens traditionnel. Vous n'avez pas de serveur que vous maintenez où vous téléchargez vos fichiers avec un client [FTP](https://en.wikipedia.org/wiki/File_Transfer_Protocol) comme [Cyberduck](https://cyberduck.io/).

Au lieu de cela, que vous le fassiez vous-même avec S3 ou que vous le pipiez dans Netlify (qui est en fait [multi-cloud](https://www.netlify.com/blog/2018/05/14/how-netlify-migrated-to-a-fully-multi-cloud-infrastructure/)), votre HTML et vos actifs statiques sont servis depuis un stockage d'objets. À la fin de cela, vous avez généralement un CDN comme [Cloudflare](https://www.cloudflare.com/) qui met en cache ces fichiers à des emplacements partout dans le monde, rendant vos pages plus rapides à charger pour les personnes visitant votre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/cdn-distribution-map.jpg)
_Carte de distribution du CDN_

## Qu'est-ce qui rend une application JAMstack si géniale ?

Les applications JAMstack satisfont intrinsèquement la plupart, sinon tous, des [5 piliers du cadre AWS Well-Architected Framework](https://aws.amazon.com/blogs/apn/the-5-pillars-of-the-aws-well-architected-framework/). Ce sont des concepts clés qu'AWS considère pour fournir une infrastructure rapide, sécurisée, haute performance, résiliente et efficace.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/aws-well-architected-framework.jpg)
_[AWS Well-Architected](https://aws.amazon.com/architecture/well-architected/)_

Voyons comment...

### Vitesse

Le fait que vous serviez des applications JAMstack en tant que fichiers statiques directement depuis un CDN (généralement) rend probable que votre application se chargera super rapidement. Les jours où le serveur devait passer du temps à construire la page avant de répondre sont révolus ; maintenant vous servez la page en tant que simple HTML "tel quel" ou avec une sorte d'hydratation côté client comme vous le verriez avec [React](https://reactjs.org/).

### Coût

Plus souvent qu'autrement, les sites JAMstack coûteront moins cher que leurs homologues côté serveur. L'hébergement d'actifs statiques est bon marché et maintenant votre page est servie au même tarif.

### Évolutivité

Puisque vous servez vos fichiers depuis un hébergement statique, probablement un CDN, cela vous donne pratiquement une évolutivité infinie. La plupart des fournisseurs feront cette affirmation, ce qui signifie que vous n'aurez aucun problème à laisser un afflux de personnes accéder à votre site par la porte d'entrée.

### Maintenance

Le fondement de votre site statique n'est pas un serveur, ce qui signifie que vous n'avez pas besoin de le maintenir. Que ce soit Netlify, S3, ou tout autre fournisseur, votre HTML, CSS et JS statiques sont maintenus pour vous sans tracas.

### Sécurité

En insistant sur l'absence de serveur que vous devez personnellement maintenir, vous n'avez pas vraiment besoin de vous soucier autant de verrouiller les moyens pour les gens d'intrusion.

Au lieu de cela, vous devrez vous concentrer principalement sur les permissions pour verrouiller le contenu privé et rassurer vos utilisateurs que leurs informations personnelles ne sont pas publiques.

### Mais cela dépend aussi de vos APIs

Autant ces points sont vrais pour les aspects statiques de votre site, gardez à l'esprit que vous dépendez peut-être encore d'un type d'API pour votre expérience côté client.

Essayez de tirer parti de ces requêtes au moment de la compilation lorsque vous le pouvez, comme avec un générateur de site statique. Sinon, vous devrez peser le nombre de requêtes que vous faites à un endpoint dynamique et comment cela impacte tous les points ci-dessus pour votre expérience globale.

## Mon site web est-il considéré comme étant sur le JAMstack ?

Nous avons déjà parlé des 3 composants (JavaScript, APIs, Markup), mais ce dont nous n'avons pas parlé, c'est le fait que vous n'avez pas nécessairement besoin d'utiliser les 3 pour considérer votre site digne de l'étiquette JAM.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/were-not-worthy.gif)
_Wayne's World "we're not worthy"_

En réalité, tout se résume au Markup et à la manière dont vous le servez. Au lieu que votre application Rails rende votre HTML pour vous, vous pourriez héberger une application React précompilée sur S3 qui se connecte à Rails via un ensemble d'APIs.

Mais vous n'avez même pas besoin d'avoir des APIs. Vous n'avez même pas besoin d'avoir du JavaScript ! Tant que vous servez un fichier HTML sans qu'il doive être compilé sur un serveur au moment de la requête (aka pré-rendu), vous avez un site JAMstack.

## Quels sont quelques exemples de JAMstack ?

### freecodecamp.org

Oui ! freecodecamp.org et son portail d'apprentissage [est un site JAMstack](https://www.freecodecamp.org/news/freecodecamp-jamstack/) construit sur Gatsby. Même avec les complexités de fournir une application pour suivre des cours de code, freeCodeCamp est capable de rassembler la puissance d'un générateur de site statique et des APIs puissantes pour apporter aux gens du monde entier le pouvoir d'apprendre à coder.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/freecodecamp.jpg)
_[https://www.freecodecamp.org/](https://www.freecodecamp.org/)_

Vous pouvez voir Quincy de freeCodeCamp parler plus de cela à la JAMstack_conf 2018 :
[https://www.youtube.com/watch?v=e5H7CI3yqPY](https://www.youtube.com/watch?v=e5H7CI3yqPY)

_Note : les portails News et Forum ne sont pas actuellement des sites JAMstack._

### Impossible Foods

Le site principal de [Impossible Foods](https://impossiblefoods.com/) n'est autre qu'un site Gatsby ! Tout, de leurs recettes à leur localisateur, est compilé via notre générateur de site statique "ultra-rapide" préféré.

![Image](https://www.freecodecamp.org/news/content/images/2020/02/impossible-foods.jpg)
_[https://impossiblefoods.com/](https://impossiblefoods.com/)_

### web.dev

Le centre de ressources [web.dev](https://web.dev/) de Google est construit en utilisant le [11ty](https://www.11ty.dev/) en croissance. Vous pouvez même trouver le code open source à l'adresse : [https://github.com/GoogleChrome/web.dev](https://github.com/GoogleChrome/web.dev)

![Image](https://www.freecodecamp.org/news/content/images/2020/02/google-web-dev-1.jpg)
_[https://web.dev/](https://web.dev/)_

## Quels sont quelques outils que je peux utiliser pour construire des sites ou applications JAMstack ?

La bonne nouvelle avec tout ce buzz, c'est qu'il existe une tonne d'outils actuellement disponibles et une tonne d'autres en route. Ils peuvent encore être un peu rugueux sur les bords, mais c'est parce que c'est un tout nouveau monde d'outils et cela nécessite un peu de lissage pour être parfait.

### Construire votre application

C'est la partie amusante. Comment allez-vous construire votre application ? Avec [Scully](https://github.com/scullyio/scully) [dans le paysage](https://www.netlify.com/blog/2019/12/16/introducing-scully-the-angular-static-site-generator/), vous pouvez pratiquement choisir votre framework UI préféré et vous lancer. Voici quelques-uns populaires pour commencer, mais ce n'est pas exhaustif.

* [11ty](https://www.11ty.dev/)
* [Gatsby](https://www.gatsbyjs.org/)
* [Hugo](https://gohugo.io/)
* [Nift](https://www.nift.cc/)
* [Scully](https://github.com/scullyio/scully) (pour les fans d'Angular)
* [Et bien d'autres...](https://www.staticgen.com)

_Besoin que je choisisse un ?_ Commencez avec Gatsby et [démarrez avec un starter simple](https://github.com/colbyfayock/gatsby-starter-sass).

### Servir votre application

J'aime penser que c'est la partie facile selon votre configuration. Des outils comme Netlify et Zeit rendent cela très simple à configurer en se connectant à votre dépôt Github et en construisant à chaque fois qu'un nouveau commit est poussé, mais bien sûr vous avez des options comme AWS si vous voulez plus de contrôle.

* [AWS](https://aws.amazon.com/getting-started/projects/host-static-website/)
* [Azure](https://docs.microsoft.com/en-us/azure/storage/blobs/storage-blob-static-website)
* [GCP](https://cloud.google.com/storage/docs/hosting-static-website)
* [Github Pages](https://pages.github.com/)
* [Netlify](https://www.netlify.com/)
* [Surge](https://surge.sh/)
* [Zeit](https://zeit.co/)

_Besoin que je choisisse un ?_ Commencez avec Netlify et [prenez 5 minutes pour déployer](https://www.netlify.com/blog/2016/09/29/a-step-by-step-guide-deploying-on-netlify/) ce site Gatsby.

### Rendre votre application dynamique

En réalité, cela peut être n'importe quoi qui peut être utilisé comme une API faisant des requêtes depuis le navigateur. Je ne vais pas lister une tonne d'exemples par type, mais voici quelques outils et endroits où vous pouvez trouver des ressources.

* [Auth0](https://auth0.com/) - Authentification
* [Cloudinary](https://cloudinary.com/) - Gestion des médias
* [Google Analytics](https://analytics.google.com/analytics/web/#/) - Analyse du trafic web
* [headlesscms.org](https://headlesscms.org/) - Liste interminable de CMS headless
* [Sanity](https://www.sanity.io/) - CMS
* [Serverless Framework](https://serverless.com/) - Ressources serverless DIY, faciles à déployer
* [Snipcart](https://snipcart.com/) - Ecommerce
* [Stripe](https://stripe.com/) - Gestion des paiements
* [Et une tonne d'autres ressources...](https://github.com/agarrharr/awesome-static-website-services)
* [Et une tonne d'autres choix de CMS...](https://headlesscms.org/)
* [Et quelques informations générales et outils...](https://jamstack.wtf/)

### Et qu'en est-il des ressources générales pour apprendre ?

Vous pouvez trouver beaucoup de ressources pour vous lancer rapidement dans le monde JAMstack.

* [Comment héberger et déployer un site web statique ou une application JAMstack sur AWS S3 et CloudFront](https://www.freecodecamp.org/news/how-to-host-and-deploy-a-static-website-or-jamstack-app-to-s3-and-cloudfront/) de moi sur freeCodeCamp
* [Un guide étape par étape : Gatsby sur Netlify](https://www.netlify.com/blog/2016/02/24/a-step-by-step-guide-gatsby-on-netlify/) de Netlify
* [Construisez votre propre blog à partir de zéro en utilisant Eleventy](https://www.filamentgroup.com/lab/build-a-blog/) du filament group
* [Comment héberger votre site web statique avec AWS - Un guide pour débutants](https://www.freecodecamp.org/news/a-beginners-guide-on-how-to-host-a-static-site-with-aws/) de freeCodeCamp
* [Tutoriel Hugo : Comment construire et héberger un site e-commerce statique (très rapide)](https://snipcart.com/blog/hugo-tutorial-static-site-ecommerce) de SnipCart
* [Comment construire des applications JAMstack serverless authentifiées avec Gatsby et Netlify](https://www.freecodecamp.org/news/building-jamstack-apps/) de freeCodeCamp

## Préparez-vous à en voir plus

Similaire à son homologue serverless, les jours du JAMstack sont jeunes. Avec le temps, nous verrons les outils mûrir et s'étendre, offrant de nouvelles façons passionnantes de construire rapidement des sites rapides que tout le monde peut utiliser.

Rejoignez la conversation sur Twitter et [faites-moi savoir](https://twitter.com/colbyfayock) quelle est votre partie préférée de la construction d'un site JAMstack !

## Quelque chose manque ?

Votre outil JAMstack préféré ou un exemple génial manque ? [Contactez-moi sur Twitter](https://twitter.com/colbyfayock) !

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