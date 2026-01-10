---
title: Hébergement de site simple avec Amazon S3 et HTTPS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-01-08T16:25:45.000Z'
originalURL: https://freecodecamp.org/news/simple-site-hosting-with-amazon-s3-and-https-5e78017f482a
coverImage: https://cdn-media-1.freecodecamp.org/images/1*nKAE02IQZHWQ9oqNgGX3ag.jpeg
tags:
- name: AWS
  slug: aws
- name: Cloud Services
  slug: cloud-services
- name: S3
  slug: s3
- name: Web Development
  slug: web-development
- name: Web Hosting
  slug: web-hosting
seo_title: Hébergement de site simple avec Amazon S3 et HTTPS
seo_desc: 'By Georgia Nola

  Hiya folks!

  In this tutorial I’ll show you how to host a static website with HTTPS on AWS with
  a custom domain. All this is possible using AWS free tier.

  However, the services we are going to use do incur some small charges. Generally...'
---

Par Georgia Nola

Salut tout le monde !

Dans ce tutoriel, je vais vous montrer comment héberger un site web statique avec HTTPS sur AWS avec un domaine personnalisé. Tout cela est possible en utilisant le niveau gratuit d'AWS.

Cependant, les services que nous allons utiliser entraînent certains petits frais. En général, ceux-ci ne devraient pas dépasser 1 $/mois.

Nous allons utiliser une combinaison des services AWS suivants :  
 — S3  
 — Route53  
 — Certificate Manager  
 — CloudFront

_Commençons !_

### Configurer vos buckets S3

Tout d'abord, vous aurez besoin de **deux buckets S3**, tous deux doivent correspondre à votre nom de domaine personnalisé, le second incluant le sous-domaine www.

Bucket 1 : mon-site.com  
Bucket 2 : www.mon-site.com

Le premier bucket (mon-site.com) est le bucket principal pour votre site. Il contient tous vos fichiers et ressources pour votre site web statique.

![Image](https://cdn-media-1.freecodecamp.org/images/8tMXguNd0mEM-Kdt54Dy0WzMNvD0h0D0Moci)

Ensuite, nous configurons ce bucket pour l'hébergement de site statique. Vous pouvez trouver cette option sous l'onglet Propriétés du bucket, et nous allons garder les paramètres par défaut fournis ici avec l'index du site défini sur index.html.

![Image](https://cdn-media-1.freecodecamp.org/images/-HHilv-8c1Y3OHdtaZhJR9DNlphJOBFd87gy)

Nous devons également rendre ce bucket publiquement accessible, car le navigateur d'un utilisateur devra accéder aux fichiers du bucket pour afficher le site web. Nous pouvons faire cela en définissant une Politique de Bucket sous l'onglet Autorisations.

```
{       "Version": "2012-10-17",       "Statement": [        {            "Sid": "PublicReadGetObject",            "Effect": "Allow",            "Principal": "*",            "Action": "s3:GetObject",            "Resource": "ARN_DU_BUCKET"        }    ]}
```

Il s'agit d'une politique simple qui permettra uniquement l'accès public en lecture des objets dans le bucket. Maintenant, si vous allez à l'endpoint défini dans la configuration d'hébergement statique du bucket, vous devriez voir votre site web.

![Image](https://cdn-media-1.freecodecamp.org/images/yEcjdf6UEr8iPVBjQCT0CtidDLpUQyhQCbLG)

Du progrès ! Mais nous pouvons faire mieux.

Le second bucket (www.mon-site.com) restera vide mais sera configuré pour rediriger vers notre premier bucket en utilisant HTTP comme protocole (nous le rendrons HTTPS plus tard).

![Image](https://cdn-media-1.freecodecamp.org/images/MphGJGErSalxmf76wjQbOGSuyhg6y50dPWxT)
_Rediriger les requêtes vers le bucket principal en utilisant le protocole HTTP_

Vos buckets sont maintenant prêts à l'emploi !

### Configurer les domaines avec Route53

Votre site web est donc opérationnel mais n'est accessible que via l'endpoint du bucket et non via votre domaine personnalisé. Changeons cela.

Rendez-vous dans **Route53**. Si vous avez enregistré votre domaine avec le registraire Amazon, vous devriez voir qu'une zone hébergée a été configurée pour vous avec deux ensembles d'enregistrements. Un pour le serveur de noms (NS) et un pour SOA.

Tout ce que nous devons faire est de créer deux ensembles d'enregistrements supplémentaires pour pointer vers les endpoints des buckets S3.

Pour chaque ensemble d'enregistrements :  
 — Type : A — Adresse IPv4  
 — Alias : Oui  
 — Cible de l'Alias : l'endpoint du site S3 qui correspond à ce que vous avez défini pour le Nom.

![Image](https://cdn-media-1.freecodecamp.org/images/-pRXjHHB-EmOPzuTcNbKribluPQTsshaCGf-)
_Création d'un ensemble d'enregistrements pour le sous-domaine www_

Maintenant, nous pouvons nous rendre à l'URL personnalisée... et voilà !  
Nous y sommes presque, mais il nous manque une dernière chose...

![Image](https://cdn-media-1.freecodecamp.org/images/Tn5XmMFeKZDKn2zLITzmEfYtBOP6OH2ZSrVl)

**Note** : Si votre domaine est enregistré auprès d'un autre registraire de domaines (non Amazon), vous devrez suivre des étapes différentes pour configurer cela. Généralement, vous devrez ajouter un enregistrement CNAME avec une valeur de l'endpoint du bucket S3 principal.

**Dépannage** :  
Si vous avez supprimé la zone hébergée créée par Amazon lorsque vous avez enregistré le domaine pour la première fois (je l'ai fait parce que les zones hébergées entraînent certains frais), vous devrez créer une nouvelle zone hébergée à partir de zéro.

1. Sélectionnez « Créer une zone hébergée » et définissez le nom de domaine, par exemple « mon-site.com »
2. Cela générera de nouveaux ensembles d'enregistrements pour les types NS et SOA.
3. Allez dans votre domaine enregistré et mettez à jour les valeurs des serveurs de noms avec celles générées dans le nouvel ensemble d'enregistrements NS.

### Demander un certificat

Super, le site est maintenant hébergé en utilisant l'URL personnalisée ! Cependant, nous ne pouvons y accéder que via le protocole HTTP.  
Nous devons toujours nous assurer que nos sites sont sécurisés en utilisant le protocole HTTPS. Cela protège notre site et nos utilisateurs contre les attaques par injection malveillante et garantit l'authenticité.

Rendez-vous dans **Certificate Manager** dans la console AWS et demandez un nouveau certificat public (celui-ci est gratuit). Vous serez invité à entrer les noms de domaine que vous souhaitez sécuriser.

![Image](https://cdn-media-1.freecodecamp.org/images/nklZPz8lBuVETFkAxoKadUuDn3PLvztVIH3J)

Avant que le certificat puisse être émis, Amazon doit pouvoir vérifier que vous êtes propriétaire des domaines spécifiés.

Vous pouvez choisir entre deux méthodes de vérification : Email ou DNS.

L'email est généralement plus simple, mais vous devrez vous assurer de pouvoir accéder à l'email utilisé pour enregistrer le domaine. Alternativement, si vous avez utilisé Amazon Registrar et Route53, vous pouvez sélectionner la méthode DNS. Cela nécessite d'ajouter certains ensembles d'enregistrements spécifiques à la zone hébergée, mais cela est principalement automatisé pour vous, donc c'est assez simple.

Cela peut prendre quelques minutes pour que le certificat soit émis après validation.   
Lorsque tout est terminé, nous pouvons passer à l'étape finale !

### Configurer CloudFront

Pour l'étape finale, nous allons utiliser **CloudFront** qui nous permet d'utiliser le nouveau certificat SSL pour servir le site web avec HTTPS. CloudFront accélère également la distribution du contenu web en le stockant à plusieurs emplacements de périphérie et en le livrant depuis l'emplacement de périphérie le plus proche de l'utilisateur.

Nous avons besoin de **deux nouvelles distributions web**, une pour chaque bucket S3. Rendez-vous dans CloudFront dans la console AWS et créez la première distribution web.  
Il existe de nombreuses options de configuration pour créer une distribution web, mais pour les bases, nous devons uniquement modifier cinq paramètres :

1. **Nom de domaine d'origine** : Définissez-le sur l'endpoint du site S3 pour l'un des buckets. **Important** : Ce champ vous donnera quelques options de complétion automatique avec les noms de vos buckets S3. Cependant, l'utilisation de celles-ci peut causer des problèmes de redirection vers l'endpoint du bucket. Utilisez donc directement l'endpoint du bucket.
2. **ID d'origine** : Celui-ci est rempli pour vous lorsque vous entrez le Nom de domaine d'origine.
3. **Stratégie de protocole du spectateur** : Définissez sur « Rediriger HTTP vers HTTPS ».
4. **Noms de domaine alternatifs** : Cela doit correspondre au nom du bucket S3 vers lequel vous pointez. Par exemple « mon-site.com ».
5. **Certificat SSL** : Sélectionnez « Certificat SSL personnalisé » et sélectionnez votre nouveau certificat dans la liste déroulante.

Faites cela à nouveau pour le second bucket S3.

![Image](https://cdn-media-1.freecodecamp.org/images/yAhOQRit35ON9mB7rtO4aefi6w2o9r-RQ2p1)

![Image](https://cdn-media-1.freecodecamp.org/images/AUfGClmx76ORz-sEOSipOFrJmBQE6KH2pDpf)

Les distributions peuvent prendre un certain temps à se lancer, alors en attendant, faisons les dernières étapes.

Retournez dans **S3**, allez dans votre bucket secondaire (www.mon-site.com), dans l'onglet Propriétés et sous Hébergement de site web statique, définissez le protocole de redirection sur HTTPS.

Enfin, retournez dans **Route53**. Nous devons mettre à jour les enregistrements A personnalisés que nous avons créés pour qu'ils ciblent désormais les distributions CloudFront plutôt que les buckets S3. Pour chaque enregistrement, changez la Cible de l'Alias et sélectionnez la distribution CloudFront disponible dans la liste déroulante.

Note : Si vous utilisez un autre service DNS, vous devrez mettre à jour l'enregistrement CNAME depuis celui-ci pour qu'il pointe vers le nom de domaine CloudFront.

![Image](https://cdn-media-1.freecodecamp.org/images/9PtEunXXDJGvAsXD03ZFepeSNosGtlXC-SWl)
_Hourra !_

Et voilà ! Votre magnifique site web est maintenant disponible sur le domaine personnalisé et servi avec HTTPS !

![Image](https://cdn-media-1.freecodecamp.org/images/1q28QH0CERJRnMkDZdrmOImMQD7szHNf5xZI)
_[From Giphy](https://giphy.com" rel="noopener" target="_blank" title=")_

Merci d'avoir lu ! J'espère que ce guide a été utile et agréable, j'adorerais savoir si vous l'avez trouvé utile.