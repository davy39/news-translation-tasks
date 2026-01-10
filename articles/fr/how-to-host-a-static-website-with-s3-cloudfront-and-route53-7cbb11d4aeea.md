---
title: Comment héberger un site web statique avec S3, CloudFront et Route53
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T16:17:52.000Z'
originalURL: https://freecodecamp.org/news/how-to-host-a-static-website-with-s3-cloudfront-and-route53-7cbb11d4aeea
coverImage: https://cdn-media-1.freecodecamp.org/images/1*mY5cuvV50_Jpya9yTWpzdQ.jpeg
tags:
- name: AWS
  slug: aws
- name: cloudfront
  slug: cloudfront
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
- name: Web Development
  slug: web-development
seo_title: Comment héberger un site web statique avec S3, CloudFront et Route53
seo_desc: 'By Paul Berg

  I recently set-up my self-hosted personal blog and I underestimated the effort I
  had to put in to make it exactly as I wanted. So I decided to write a tutorial to
  help others do it with less overhead.

  This article will go into fine detai...'
---

Par Paul Berg

J'ai récemment configuré mon blog personnel auto-hébergé [blog](https://paulrberg.com/) et j'ai sous-estimé l'effort que je devais fournir pour le rendre exactement comme je le souhaitais. J'ai donc décidé d'écrire un tutoriel pour aider les autres à le faire avec moins de travail.

Cet article entrera dans les détails sur la manière de cocher toutes les cases ci-dessous, avec un accent sur les composants backend.

1. Hébergement pay-as-you-go
2. Certificat SSL
3. Sous-domaine www fonctionnel
4. Design hautement personnalisable mais minimaliste
5. Articles alimentés par Markdown

Pour les points 4 et 5 ci-dessus, j'ai utilisé [Hugo](https://gohugo.io/) avec le thème [Minimal](https://themes.gohugo.io/minimal/).

#### Avertissement

Notez que ce tutoriel est verbeux, destiné à ceux qui valorisent la flexibilité et l'interopérabilité avec d'autres services AWS plus que tout. Si vous cherchez quelque chose de léger et rapide, vous pouvez utiliser [Netlify](https://netlify.com/) ou [Amplify](https://aws-amplify.github.io/).

#### Prérequis

Je vais supposer que :

1. Vous avez conçu et codé votre site web ou au moins avez une maquette.
2. Vous avez un compte AWS (si ce n'est pas le cas, allez [enregistrer un](https://portal.aws.amazon.com/billing/signup). Les comptes AWS incluent un an d'accès gratuit).
3. Vous êtes familier avec le DNS et [son fonctionnement](https://www.cloudflare.com/learning/dns/what-is-dns/), au moins à un niveau élevé.

Concernant le DNS, une explication rapide est qu'il s'agit en quelque sorte de l'annuaire de l'Internet et, tout comme Google possède `google.com`, vous pouvez posséder votre propre domaine tel que `example.com`. Pour ce faire, vous devez aller chez un registraire DNS et acheter le domaine que vous souhaitez. Je recommande fortement d'utiliser [Namecheap](https://namecheap.pxf.io/c/1243704/386170/5618) comme registraire, car ils ont une interface utilisateur géniale et des prix bas. En alternative, vous pourriez choisir [GoDaddy](https://godaddy.com).

Au cas où votre domaine ".com" serait pris et que vous souhaitiez des mashups intelligents, les sites suivants pourraient être utiles :

* [LeanDomainSearch](https://leandomainsearch.com/)
* [Wordoid](https://wordoid.com/)
* [Domainr](https://domainr.com/)

Après l'avoir acheté, ne configurez aucun enregistrement DNS pour l'instant. Nous le ferons plus tard une fois que nous en arriverons à Route53.

#### Hébergement avec Amazon AWS

Comme mentionné ci-dessus, l'objectif est d'utiliser un service pay-as-you-go car c'est de loin l'option la plus rentable. Je payais auparavant un coût fixe de l'ordre de dizaines de USD par mois pour un serveur même si j'avais des périodes où il y avait à peine une activité dessus.

Cependant, d'après mon expérience, je recommande d'opter pour une approche modulaire et d'utiliser un service pay-as-you-go comme AWS.

Avant de se lancer, il est important de comprendre la nomenclature :

* AWS : Amazon Web Services
* S3 : Simple Storage Service, pour stocker des fichiers
* Route53 : Un service pour gérer les enregistrements DNS
* CloudFront : réseau de diffusion de contenu (CDN) pour accélérer votre site web, également requis pour générer le certificat SSL

Voici une [Mindmap](https://cloudcraft.co/view/d2391653-9c67-4bcd-84f2-977b0e32ecfc?key=aoBnq-ksfVXmgA4yjWIWSQ) conçue avec [Cloudcraft](https://cloudcraft.co/) pour ce que vous allez construire :

![Image](https://cdn-media-1.freecodecamp.org/images/RCkmAwdM0GuBLFaTJiqr69WGHCi05pJHZb1y)

Nous allons d'abord nous concentrer sur le chemin du **côté droit**, donc la configuration normale (avec Route53, CloudFront et S3), et non celle pour le sous-domaine www. Importamment, en utilisant cette configuration modulaire, vous n'exécuterez aucun serveur backend Linux, donc vous n'aurez pas à vous soucier de la mise à jour ou de la correction de quoi que ce soit. N'est-ce pas pratique ?

#### Amazon Simple Storage Service (S3)

C'est là que vous stockerez vos fichiers statiques (HTML, CSS, JavaScript). Si vous avez utilisé Create React App ou un autre framework de développement frontend, recherchez votre dossier "build" ou "public" généré.

![Image](https://cdn-media-1.freecodecamp.org/images/fnj6dQpZoJ7f5DJ1zIFpJW1lz2o6Uq4uz2sq)

Voici ce que vous devez faire :

1. Configurez un bucket S3 nommé "example.com". Notez que les noms de buckets S3 sont [globaux](https://stackoverflow.com/questions/24112647/why-are-s3-and-google-storage-bucket-names-a-global-namespace) et, tout comme avec les domaines, vous devrez trouver un autre nom si quelqu'un a déjà pris `example.com`. Selon vos besoins, vous pouvez activer ou désactiver les options fournies par AWS : versioning, journalisation de l'accès serveur, chiffrement, etc.
2. Assurez-vous de décocher les cases qui mentionnent le blocage et la suppression des ACL et politiques d'accès public. Souvent, les buckets S3 sont utilisés pour stocker des données privées, donc AWS optimise la configuration pour des configurations hautement sécurisées. Dans votre cas, vous souhaitez que le bucket soit accessible au public.
3. Assurez-vous de définir une politique, voici un [exemple](https://gist.github.com/PaulRBerg/61e0c998f105fedb627fa66ff2c6aea6).
4. Activez "Hébergement de site web statique" pour votre bucket et cochez "Utiliser ce bucket pour héberger un site web".
5. Téléchargez vos fichiers, en vous assurant que "index.html" est à la racine de votre bucket.

Toutes les opérations ci-dessus peuvent être effectuées en utilisant soit la [Console Web de Gestion AWS](http://console.aws.amazon.com/) soit l'[AWS CLI](https://github.com/aws/aws-cli). Plus précisément pour l'étape 4, je recommande de le faire dans la console afin que vous puissiez obtenir le point de terminaison pour votre nouveau site web hébergé (j'ai caché le mien pour des raisons de confidentialité) :

![Image](https://cdn-media-1.freecodecamp.org/images/WKY2huZtZz18qLUplSfDof0L9d5VdcnZSi7N)

Testez-le dans le navigateur pour vous assurer que vous avez correctement configuré votre bucket S3. Cela devrait ressembler à ceci :

> example.com.s3-website.your-region.amazonaws.com

#### CloudFront

Pour héberger un site web statique, vous n'avez pas réellement besoin de CloudFront ou de tout autre CDN, car il n'y a pas beaucoup de données à stocker et les gains en efficacité et en UX sont minimes. Cependant, l'un des objectifs initiaux était d'avoir un site web sécurisé par un certificat SSL, donc nous utiliserons CloudFront.

![Image](https://cdn-media-1.freecodecamp.org/images/3rjcxs8vIoL988yxADq-guuSj6cXvaEWY2Tb)

Vous avez peut-être entendu parler de CloudFlare, qui est probablement le moyen le plus simple de se lancer avec un CDN et qui offre également l'avantage d'une certaine sécurité SSL. Je dis "certaine" car ils ont cette fonctionnalité trompeuse appelée "Flexible SSL", qui [n'a pas les garanties de sécurité](http://disq.us/p/1ycwtny) qu'un certificat SSL auto-signé a.

Par conséquent, vous n'allez pas utiliser cela, mais plutôt utiliser un service similaire dans AWS appelé CloudFront. Vous pouvez le considérer comme ayant vos propres serveurs de distribution de contenu, car les données sont mises en cache dans plusieurs endroits autour du monde pour fournir à vos utilisateurs des temps de réponse rapides. Plus important pour le site web statique, cela permet également l'utilisation d'un certificat SSL.

Encore une fois, vous pouvez créer votre distribution CloudFront en utilisant l'interface d'administration AWS ou l'outil CLI. Voici un exemple de [configuration](https://gist.github.com/PaulRBerg/7d946e54c8f5cfc22f514855c6b6e864).

Avertissements :

1. Le nom de l'origine doit être le point de terminaison que vous avez obtenu après avoir activé "Hébergement de site web statique" sur votre bucket S3.
2. Ne définissez aucun "DefaultRootObject". Laissez-le vide.
3. Autorisez HTTP et HTTPS. Vous pourrez rediriger automatiquement les utilisateurs de HTTP vers HTTPS après que le certificat soit signé et installé.

Assurez-vous d'attendre un certain temps pour que la distribution démarre correctement (peut prendre jusqu'à 15 minutes). Testez-la en ouvrant le point de terminaison que vous recevez, votre site web statique S3 devrait apparaître. Le point de terminaison devrait ressembler à ceci :

> _13fb4knzujxq0b.cloudfront.net_

Notez votre point de terminaison CloudFront quelque part car nous allons l'utiliser avec Route53 dans un instant.

### Route53

Il est temps de connecter le domaine que vous avez acheté chez votre registraire DNS avec CloudFront et S3. Route53 agit comme le pont pour cela.

![Image](https://cdn-media-1.freecodecamp.org/images/9bjF7WQmstIAdJvspRcxpibs7CscN0fMRuZm)

Voici ce que vous devez faire pour configurer Route53 et connecter le domaine avec CloudFront :

1. Créez une zone hébergée Route53 et définissez votre domaine. Rendez-la publique.
2. Vous recevrez 4 enregistrements NS. Copiez et collez les serveurs de noms dans la page d'administration de votre domaine externe. Si vous utilisez [Namecheap](https://namecheap.pxf.io/c/1243704/386170/5618), voici comment vous pouvez mettre à jour vos serveurs de noms. Dans Namecheap, allez dans Compte -> Tableau de bord -> Gérer -> Serveurs de noms -> DNS personnalisé et mettez vos 4 serveurs de noms là :

![Image](https://cdn-media-1.freecodecamp.org/images/YVjqg3qgpaZP6JCDi2v3c6k6OsvZFB3epuc5)

3. Créez un ensemble d'enregistrements et laissez le nom vide (il sera par défaut example.com). Ensuite, vous devrez :

* Définir le type sur "A — adresse IPv4"
* Répondre avec "Oui" à "Alias" et définir la cible de l'alias sur l'URL de votre distribution CloudFront.
* Gardez la politique de routage comme "Simple" et, en fonction de votre budget et de vos besoins, activez ou désactivez "Évaluer la santé de la cible".

4. Répétez l'étape 3 pour le type "AAAA - adresse IPv6" si vous avez activé votre distribution CloudFront pour qu'elle soit compatible IPv6. Si vous avez suivi ce tutoriel, IPv6 était activé par défaut.

Notez que la propagation DNS peut prendre jusqu'à [72 heures](https://www.youtube.com/watch?v=Gr8RzCZWh5M), bien qu'elle soit normalement mise à jour en quelques heures ou plus rapidement. Si vous avez précédemment défini d'autres enregistrements DNS (comme MX pour les emails professionnels), vous devrez les réinitialiser dans Route53.

#### Configuration de votre sous-domaine WWW

Félicitations pour être arrivé jusqu'ici ! Je suis désolé de vous dire que vous devez maintenant répéter toutes les trois étapes précédentes. Oui, vous avez bien entendu, en raison de la manière insaisissable dont fonctionne l'Internet, `www` n'est pas quelque chose d'inclus comme un composant holistique de HTTP.

Il est important de souligner qu'il n'est vraiment pas obligatoire d'ajouter un sous-domaine www à votre site web et vous pouvez passer en toute sécurité à l'étape suivante _si_ vous êtes d'accord pour que vos utilisateurs finaux ne puissent pas accéder à votre site web via `www.example.com`. J'étais un peu pédant à ce sujet et j'ai simplement dû ajouter le sous-domaine www.

Notes :

1. Refaites uniquement les étapes pour S3, CloudFront et Route53, vous n'avez pas à (et ne pouvez pas) aller chez [Namecheap](https://namecheap.pxf.io/c/1243704/386170/5618) pour acheter `www.example.com`.
2. Pour tous les champs où vous deviez mettre `example.com`, mettez maintenant `www.example.com`.

Si vous vous demandez si, en créant des buckets S3, cela signifie que vous devez déployer vos fichiers statiques sur les deux, la réponse est non, vous n'avez pas à le faire. Lorsque vous activez "Hébergement de site web statique" pour votre deuxième bucket S3, sélectionnez "Rediriger les requêtes" au lieu de "Utiliser ce bucket pour héberger un site web" :

![Image](https://cdn-media-1.freecodecamp.org/images/sLTt9ve75kNIECFDmnM1dNrnWhd4wtPUTIau)

#### Certificat SSL

LetsEncrypt est l'une des meilleures choses qui soient arrivées à l'Internet ces dernières années. Ils ont démocratisé l'accès aux certificats SSL et c'est un énorme accomplissement, bravo à eux ! Si LetsEncrypt vous a été si utile, envisagez de faire un [don](https://letsencrypt.org/donate/).

Cette étape est cruciale et aussi la plus difficile de tout le tutoriel, alors procédez avec prudence. Vous pourriez utiliser votre propre machine ou un serveur Linux pour générer le certificat, mais j'ai choisi la première option, c'est plus simple et moins coûteux.

1. Rendez-vous sur le dépôt [certbot-s3front](https://github.com/dlapiduz/certbot-s3front) et installez l'outil. Vous devez avoir Python et pip installés.
2. Suivez leurs instructions, mais (1) sautez les parties S3 et CloudFront, vous l'avez déjà fait et (2) définissez "example.com,[www.example.com](http://www.example.com/)" comme valeur pour le paramètre "-d" (domaine). Lisez plus à ce sujet sur le [forum](https://community.letsencrypt.org/t/certification-is-not-working-in-firefox-your-connection-is-not-secure/43090/6?u=paulrberg) de LE.
3. Après avoir généré avec succès votre certificat SSL, vous pourriez éventuellement activer "Rediriger HTTP vers HTTPS" sur votre domaine nu (c'est-à-dire, "example.com") distribution CloudFront. Ne faites pas cela pour "www", car il redirigera vers votre domaine nu de toute façon.
4. Assurez-vous de sauvegarder votre/vos certificat(s) `/etc/letsencrypt/live/example.com`.

Notes :

1. En raison de [raisons mystérieuses](https://github.com/dlapiduz/certbot-s3front/issues/70), je n'ai pas pu faire fonctionner l'authentification de certbot en définissant les variables d'environnement "AWS_ACCESS_KEY_ID" et "AWS_SECRET_ACCESS_KEY". Cela pourrait être causé par le fait que j'ai plusieurs profils différents dans mon `~/.aws/credentials`, mais je n'en suis pas sûr. Pour éviter une "NoCredentialsError", définissez simplement temporairement un profil "default" et certbot le prendra.
2. Si vous êtes malchanceux comme moi et que vous obtenez une erreur "IAMCertificateId", consultez [cette solution](https://github.com/dlapiduz/certbot-s3front/issues/76).

#### ACM

Peu après la publication de cet article, beaucoup de gens ont suggéré qu'il serait beaucoup plus facile d'utiliser l'AWS Certificate Manager (ACM) pour générer des certificats. Pas besoin de penser aux renouvellements, mais cela signifie que vous êtes verrouillé avec AWS.

#### Goulots d'étranglement

1. Pas de logique serveur : Ce tutoriel n'est applicable qu'aux sites web statiques, donc vous ne pouvez pas exécuter de logique backend en utilisant un module Node.js comme [ExpressJS](https://expressjs.com/). Pour cela, vous pouvez soit lancer une instance EC2, écrire des fonctions Lambda ou utiliser Docker via ECS/Kubernetes.
2. Les certificats LetsEncrypt expirent en 90 jours : Vous pouvez résoudre cela de deux manières. Premièrement, vous pourriez définir un rappel dans votre calendrier, ce que j'admets être sous-optimal, mais je suis en phase d'expérimentation donc je ne suis pas dérangé par un peu de travail manuel. Deuxièmement, vous pourriez définir une tâche cron, mais vous avez besoin d'un serveur Linux et utiliser les options "--renew-by-default --text" lors de l'interaction avec certbot.
3. Les aperçus de liens riches peuvent être un désordre : Cela pourrait être un problème spécifique à mon thème Hugo, mais je pense aussi que tout le monde veut avoir une image et une description appropriées lors du partage de leurs liens de site web. [Voici](https://github.com/calintat/minimal/issues/61#issuecomment-449999181) comment j'ai réussi à le faire.

#### Conclusion

Félicitations, vous avez maintenant un site web statique vraiment bon marché mais toujours très flexible ! Les statistiques de facturation pour 100 à 1000 visiteurs actifs mensuels et des déploiements S3 assez fréquents sont **entre 1 et 2 $**, donc c'est une aubaine ! Pour une utilisation bien au-delà de cela, vous devrez peut-être mettre à niveau vos composants AWS, mais cela est hors du cadre de ce tutoriel.

Si vous êtes un développeur expérimenté intéressé à reproduire ce tutoriel sur plusieurs comptes AWS, vous pourriez vouloir consulter [Terraform](https://terraform.io/). C'est un outil super cool d'Infrastructure-as-a-Service que vous pouvez utiliser pour définir vos S3, CloudFront et Route53 comme des extraits de code. La technologie n'est-elle pas si incroyablement géniale ?

J'espère que vous trouverez ce tutoriel utile ! Trouvez-moi sur [**Twitter**](https://twitter.com/PaulRBerg) ou [**Keybase**](https://keybase.io/PaulRBerg) si vous voulez discuter.

### Crédits

* [Amazon](https://amazon.com/) pour les logos AWS, S3, CloudFront et Route53

_Publié à l'origine sur [paulrberg.com](https://paulrberg.com/post/static-website-aws/s3.png)_