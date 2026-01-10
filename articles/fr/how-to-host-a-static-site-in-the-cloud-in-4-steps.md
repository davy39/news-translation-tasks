---
title: Comment héberger un site statique dans le cloud en quatre étapes
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-09-09T22:03:49.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-a-static-site-in-the-cloud-in-4-steps
coverImage: https://www.freecodecamp.org/news/content/images/2020/09/aws-lambda
seo_title: Comment héberger un site statique dans le cloud en quatre étapes
---

deno--3-.png
étiquettes:
- nom: AWS
  slug: aws
- nom: Cloud
  slug: cloud
- nom: Services Cloud
  slug: cloud-services
seo_title: null
seo_desc: "Par Marcia Villalba\nLes sites statiques peuvent héberger tous types de sites web, de votre\
  \ portfolio personnel à une page de destination d'entreprise, ou même un blog. \nL'avantage principal\
  \ des sites statiques est qu'ils sont simples à gérer. Ils sont également très économiques.\
  \ Et avec..."
---

Par Marcia Villalba

Les sites statiques peuvent héberger tous types de sites web, de votre portfolio personnel à une page de destination d'entreprise, ou même un blog. 

L'avantage principal des sites statiques est qu'ils sont simples à gérer. Ils sont également très économiques. Et avec les sites statiques, vous n'avez pas besoin de services complexes de gestion de contenu (CMS) qui fonctionnent sur des serveurs en permanence (même si vous n'avez aucun trafic). 

Dans cet article, vous apprendrez comment héberger un site web statique dans le cloud AWS en 4 étapes, en utilisant [AWS Amplify](https://aws.amazon.com/amplify) et [Route 53](https://aws.amazon.com/route53/). Et la meilleure partie ? Cela vous coûtera presque rien chaque mois.

## Qu'est-ce qu'un site web statique ?

Les sites web statiques sont des sites servis à partir d'un serveur de stockage ou d'un réseau de diffusion de contenu (CDN). Il n'est pas nécessaire d'avoir un serveur en cours d'exécution pour créer les fichiers HTML. 

Ces sites web sont pré-construits sous forme de fichiers HTML qui sont stockés quelque part sur Internet et ensuite servis tels qu'ils ont été construits. 

Les sites statiques peuvent avoir du contenu dynamique, mais il est géré côté client en utilisant JavaScript ou certaines intégrations tierces utilisant des API. 

Certains avantages de l'utilisation d'un site statique sont :

* Ils sont faciles à mettre à l'échelle
* Si vous utilisez un CDN, les temps de chargement sont rapides
* Ils sont économiques
* Ils sont faciles à maintenir 

Par exemple, mon [site personnel](https://marcia.dev/) est un bon exemple de site statique :

![Site personnel de Marcia](https://lh6.googleusercontent.com/oxSzL6eMiurmPo__pMZ1lCpg3Zf0L5ZUlyiVX5ja4X75yKTgbpeWB_HmAQ8EoNYorUOBJoeeHpyEXikfMHEj1CEwzfkE8NaPMHhMug3Al3yJwNcZcyE1Lnkq3FcKJNwDLxOgPAPC)
_Site personnel de Marcia_

## Qu'est-ce qu'AWS ?

[AWS signifie Amazon Web Services](https://aws.amazon.com/) et est la plateforme cloud la plus largement adoptée. Elle dispose de nombreux services différents pour vous aider à développer et héberger vos applications. 

AWS dispose également de centres de données dans le monde entier et des millions de clients l'utilisent. 

En utilisant le cloud pour vos applications, vous réduirez les coûts, vous aiderez à devenir plus agile et vous permettrez d'innover plus rapidement que si vous utilisiez vos propres serveurs sur site.

## Étape 1 - Configurer votre compte AWS

La première étape de ce processus est d'obtenir un [compte AWS](https://portal.aws.amazon.com/billing/signup). Vous allez héberger votre page statique dans le cloud, et pour cela, vous devez avoir un compte AWS valide.

Si vous créez votre compte maintenant, le [niveau gratuit](https://aws.amazon.com/free/) devrait être suffisant pour ce projet. Le niveau gratuit vous donnera accès à de nombreux services AWS gratuitement pendant les 12 premiers mois. 

Par exemple, vous obtiendrez 5 Go de stockage gratuit. C'est génial, car nous avons besoin de stockage pour sauvegarder notre site statique dans le cloud.

Gardez à l'esprit que posséder un compte AWS est gratuit si vous n'utilisez aucun service. Vous ne serez pas facturé pour la création du compte, et si vous n'utilisez pas le compte, rien ne sera facturé.

Pour créer un compte AWS, vous pouvez suivre les étapes de cette vidéo :

%[https://www.youtube.com/watch?v=9_wo0FHtVmY]

## Étape 2 - Créer votre site statique et le configurer avec AWS Amplify

Maintenant, après avoir lu ce titre, vous vous demandez peut-être, qu'est-ce qu'AWS Amplify ?

[AWS Amplify](https://aws.amazon.com/amplify/) est un framework open-source qui fournit des fonctionnalités pour vous aider à construire des applications web et mobiles natives du cloud. Il comporte 4 composants : 

* l'interface de ligne de commande Amplify
* les bibliothèques Amplify
* les composants UI Amplify, et 
* la console Amplify. 

L'interface de ligne de commande Amplify vous aide à configurer tous les services dont vous avez besoin pour créer un backend cloud pour votre application en utilisant l'interface de ligne de commande. 

Les bibliothèques vous aident à intégrer vos applications client directement avec les services backend. 

Les composants UI Amplify sont des bibliothèques UI spécifiquement pour React, React Native, Angular, Ionic et Vue qui vous aideront à développer facilement votre application native du cloud. 

Enfin, la console Amplify est un service AWS qui fournit un flux de travail basé sur git pour le déploiement continu et pour l'hébergement d'applications web et mobiles full-stack. 

Dans cet article, nous n'allons pas utiliser toutes les capacités d'AWS Amplify, nous allons simplement utiliser la console. Mais je vous recommande de consulter [certains tutoriels](https://www.youtube.com/playlist?list=PLGyRwGktEFqfquTNg6u82-m0u45qZUQpL) sur la façon de construire des applications plus complexes en utilisant AWS Amplify. 

### Créer le site statique

Maintenant, vous avez tout ce dont vous avez besoin pour commencer avec votre site statique. Pour cette démonstration, n'importe quel HTML statique fonctionnera. J'ai simplement créé un fichier appelé index.html et ajouté ce code à l'intérieur :

```html
<html>
    <h1>Bonjour Foobar</h1>
    <p>Ceci est mon site super simple</p>
</html>
```

### Le télécharger sur la console AWS Amplify

Après avoir créé le site statique, l'étape suivante consiste à aller sur le [service AWS Amplify dans la console AWS](https://console.aws.amazon.com/amplify/). 

![Trouver le service AWS Amplify dans la console AWS](https://lh3.googleusercontent.com/LwtDo_jercaPlgTy8eQkoH2s3W-Q4bhAarfrtA8Tp_fVShfk0X0jkfgjFp9Q6VAn8WMl8at26F5cNMOVP8W5hEFElg_m2Kjy-6NsszcFg49GHNBOKTP9mM9pNcA2bob22OsX9Y0w)
_Trouver le service AWS Amplify dans la console AWS_

Ensuite, lorsque ce service s'ouvre, vous verrez quelque chose comme ceci :

![Console AWS Amplify](https://lh5.googleusercontent.com/vWp3FCCnIL5cP4NkqTd-iDbVD-DKG8Gz6J3-Liu41mMlUzCPTUW9WK0BPdecyRCeW2dmC-qOkHeWxWfj5uRMW8_oGc_DZVd3zbsfHBcFENYf2pCjSnJTsN4rCiKb91JCVjShRNo5)
_Console AWS Amplify_

Cliquez sur le bouton **Connecter l'application** puis vous serez présenté avec cette page :

![Options pour déployer votre projet existant](https://lh3.googleusercontent.com/pRiA9jSHj1PrIsbvQ4qqmGjGzvDmvqkobhvsDf_KUIrDyVqotWlUyx3I0RhJwSAOkfQhvsl9xcuBjy3gvN06WWl-dPEUNt6n31Xcy_axDc-rIp4b_foTFJRund4vWnDaIxQ_Ypqz)
_Options pour déployer votre projet existant_

Ensuite, vous pouvez sélectionner **Déployer sans un fournisseur Git** et continuer. 

Vous serez présenté avec une page pour déployer manuellement votre application. Là, vous choisissez un **nom d'application** et un **nom d'environnement**, puis vous pouvez glisser votre dossier d'application dans le navigateur.

![Démarrer un déploiement manuel dans AWS Amplify](https://www.freecodecamp.org/news/content/images/2020/09/Screenshot-2020-09-08-at-22.13.29.png)
_Démarrer un déploiement manuel dans AWS Amplify_

Lorsque l'application termine le téléchargement, vous verrez un message indiquant "Déploiement terminé avec succès".

Votre site web est maintenant hébergé dans le cloud. Allez au lien qui se trouve sous le texte **Domaine**. Cela vous mènera à votre site statique nouvellement déployé. 

![Image](https://lh5.googleusercontent.com/8ZxQ_ZEs78VSt1_c0cpL9U2iqMiGlm9oS1WyuF0OOnHi_7GL15p3gNl9Cyrdbk0vGnhx-YkSrRXxC8zZN_TyTM4JcH0nXssRYLK0XbNd5WcF_9aaKSWZdOumZTkeeaD5ONEQEDB7)

## Étape 3 - Acheter un domaine pour votre site web

Maintenant, il est temps d'obtenir un domaine pour votre site web. Partager ce lien **Domaine** n'est pas très pratique et un domaine peut être un moyen plus simple de nommer votre site web.

Pour cela, vous devez aller dans votre [compte AWS vers un service appelé Route53](https://console.aws.amazon.com/route53/v2).

![Trouver le service Route53 dans la console AWS](https://lh5.googleusercontent.com/jHyrb4EAiZr0PiDJzBxn-DU6EeTdfRF3-oWUKmQr9NCMOX5mUYjQzCPYhAtcfwun8vAQhKuCa4ONhqlznKz-cEpwV8u9MK3OZVPLZ_7NVwdgygs-2KhOdGwJAsbFi_thtCYYBlFv)
_Trouver le service Route53 dans la console AWS_

Ensuite, lorsque Route 53 s'ouvre, vous pouvez aller à un lien qui dit **Enregistrer un domaine**, et une page comme celle-ci apparaît. 

![Image](https://lh6.googleusercontent.com/Bnlj5cwDaFGOVMC8VIEfYImlqEx4wTHgpJxipwsRSj1cji-YSpEvLdxIfq6twQRHoQwu4MvUZFJIg1I0M-Uh0kGZSDFsVogkcy2wjko4oZGMKMAy6l8fQclYzHAt1FQGYyIi9wqn)

Ici, vous devez choisir un nom de domaine. Les domaines sont facturés annuellement et ils ont différents coûts selon l'extension (comme .com, .net, etc.).

Après avoir choisi un nom de domaine, vous pouvez l'ajouter au panier. Ensuite, suivez simplement les instructions fournies par Route53. 

## Étape 4 - Configurer le domaine dans votre application AWS Amplify

Maintenant que vous avez le domaine, il est temps de revenir à votre application AWS Amplify – celle que vous venez de configurer. 

Ensuite, à gauche, vous cliquez sur le lien **Gestion de domaine** et cette page s'ouvre :

![Ajouter un domaine à votre site](https://lh4.googleusercontent.com/wsewL3CddWLzQedGnwxWwE7zby8qm4sSYqSEG-JLZewk9Dpgpk4E2iO6v28PviPu-gVRtXX0INbLSUqsfC0b_UP4DxkGxGpzcFta9CojOoYpxsL4-aPaisONN-wzhADNIsj-fpOH)
_Ajouter un domaine à votre site_

La zone de texte **domaine** suggérera le domaine que vous venez d'enregistrer. Il suffit de le sélectionner, d'accepter toutes les configurations par défaut, puis de cliquer sur **Enregistrer**. 

Après cela, vous serez dirigé vers une page où le domaine et le certificat SSL seront configurés. Vous n'avez rien à faire dans cette étape, il suffit d'attendre que tout soit configuré. Cela prend un certain temps, alors soyez patient.  

Maintenant, vous avez terminé, vous pouvez donc aller à votre nouveau domaine et voir votre page statique.

## Comment mettre à jour ce site

Maintenant, chaque fois que vous devez changer quelque chose dans votre site statique, vous devez aller dans AWS Amplify et mettre à jour les fichiers. En gros, vous allez simplement déposer le répertoire dans l'application Amplify.

![Mettre à jour votre site statique](https://lh4.googleusercontent.com/UbaM48h2lYlAyavZKGF4qsMcNqkJYNDrne8Hm5nioBoPuL2WmVqAqLhu1b5_rGLTx6oAsO6WMNgZp9HUTD-D9HMPuxvmM56qrW6vb3bVOTg6xs6e7uYREXAeoccxtfvJAnfNOWq1)
_Mettre à jour votre site statique_

## Conclusion

Maintenant, vous avez un site statique hébergé dans le cloud. Ce site est très scalable et fiable. Le site est hébergé en utilisant le CDN AWS appelé AWS CloudFormation, ce qui rendra votre site très rapide pour vos utilisateurs. 

Le coût total de l'hébergement après que votre compte AWS ait plus de 12 mois sera d'environ [0,50 USD à 4 USD par mois](https://aws.amazon.com/getting-started/hands-on/host-static-website/services-costs/), selon la taille de votre site et la quantité de trafic que vous recevez. 

L'autre coût annuel que vous aurez est le domaine qui peut commencer à partir de 9 USD par an.

Et si vous voulez rendre cela un peu plus automatisé, je vous recommande de regarder [AWS Amplify déploiements automatiques utilisant Github](https://docs.amplify.aws/guides/hosting/git-based-deployments/q/platform/js). 

  
**Merci d'avoir lu.**

Je suis Marcia Villalba, Developer Advocate pour AWS et l'hôte d'une chaîne YouTube appelée FooBar où j'ai plus de 250 tutoriels vidéo sur Serverless, AWS et les pratiques d'ingénierie logicielle.

* Twitter: [https://twitter.com/mavi888uy](https://twitter.com/mavi888uy)
* Youtube: [https://youtube.com/foobar_codes](https://youtube.com/foobar_codes)