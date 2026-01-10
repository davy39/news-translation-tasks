---
title: Comment héberger votre site web statique avec AWS - Un guide pour débutants
subtitle: ''
author: Phoebe Voong-Fadel
co_authors: []
series: null
date: '2019-08-08T11:48:00.000Z'
originalURL: https://freecodecamp.org/news/a-beginners-guide-on-how-to-host-a-static-site-with-aws
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/undraw_blogging_vpvv.png
tags:
- name: AWS
  slug: aws
- name: dns
  slug: dns
- name: SSL
  slug: ssl
- name: Web Hosting
  slug: web-hosting
seo_title: Comment héberger votre site web statique avec AWS - Un guide pour débutants
seo_desc: 'When I created my first portfolio last year, I based it on what I had learned
  from freeCodeCamp (HTML, CSS and a little JavaScript).

  At that point, I had only viewed my portfolio on localhost by viewing the files
  on my local computer. I didn’t know a...'
---

Lorsque j'ai créé mon premier [portfolio](https://thecodinghamster.com/) l'année dernière, je l'ai basé sur ce que j'avais appris de [freeCodeCamp](https://www.freecodecamp.org/) (HTML, CSS et un peu de JavaScript).

À ce moment-là, je n'avais vu mon portfolio que sur localhost en visualisant les fichiers sur mon ordinateur local. Je ne savais rien sur la façon d'héberger un site web en ligne.

Apprendre à héberger mon premier site web n'a pas été facile, mais ce fut une excellente expérience d'apprentissage. Si vous êtes un développeur web en herbe ou simplement intéressé par le lancement de votre propre site web statique, alors j'espère que vous trouverez ce guide utile.

#### **À qui s'adresse ce guide ?**

Ce guide est destiné aux **débutants complets** qui souhaitent héberger un site web statique (un site avec un contenu fixe). Je vais fournir un guide pratique pour les éléments suivants :

1. Comment acheter un domaine.
   
2. Comment configurer votre domaine pour un fournisseur d'hébergement externe.
   
3. Comment héberger votre site web avec Amazon Web Services (AWS).
   
4. Comment sécuriser votre site web (certification SSL) en utilisant Amazon Certification Manager.
   

Il peut y avoir quelques termes qui vous sont nouveaux. N'hésitez pas à rechercher les termes qui ne vous sont pas familiers. J'ai inséré des liens utiles et des explications là où je l'ai jugé approprié.

#### **Qu'est-ce qu'un nom de domaine et le DNS (Domain Name System) ?**

Un nom de domaine est l'adresse de votre site web. Par exemple, thecodinghamster.com. Mais pour un ordinateur, un nom de domaine est en réalité une série de chiffres (une adresse IP). Une adresse IP ressemble à ceci : 123.321.0.1

Il n'est pas facile pour nous de mémoriser une longue chaîne de chiffres. Ainsi, votre ordinateur se réfère à un **DNS** pour traduire une adresse de site web basée sur du texte en une adresse IP qu'il peut ensuite comprendre. Un DNS est comme un annuaire.

J'ai regardé cette excellente vidéo qui explique le nom de domaine, le DNS et comment cela fonctionne en moins de cinq minutes. Veuillez regarder les cinq premières minutes de la vidéo si vous êtes intéressé :

%[https://youtu.be/e2xLV7pCOLI] 

### Où pouvez-vous acheter votre nom de domaine ?

Vous pouvez acheter un nom de domaine auprès d'un registrar de noms de domaine. Les prix commencent à partir de quelques dollars. Votre nom de domaine est unique. Chaque registrar de noms de domaine offre différents niveaux de services/support. Mais vous pouvez enregistrer votre domaine avec n'importe quel registrar.

#### **Qu'est-ce qu'un fournisseur d'hébergement ?**

> « Un [service d'hébergement Internet](https://en.wikipedia.org/wiki/Internet_hosting_service) est un service qui exécute des serveurs Internet, permettant aux organisations et aux particuliers de servir du contenu sur Internet. Il existe divers niveaux de service et divers types de services offerts. »

Lorsque je cherchais un fournisseur d'hébergement pour mon site web, j'ai exploré différentes options. Les prix variaient de 2,00 £ à 5,00 £ par mois avec diverses options de stockage de 0,5 Go à 10 Go. Les prix semblaient raisonnables, mais tout ce que je voulais faire était d'héberger un site web statique. Il avait quelques images, des fichiers HTML, CSS et JavaScript. Aucun contenu dynamique.

#### **Pourquoi AWS ?**

Après quelques recherches supplémentaires, j'ai trouvé AWS. AWS offre une [option de niveau gratuit](https://aws.amazon.com/free/?nc2=h_ql_pr). Essentiellement, vous obtenez beaucoup de produits gratuits. Certains d'entre eux expirent après 12 mois et d'autres sont gratuits à perpétuité. Le seul coût que vous aurez pour héberger un site web statique est le coût de la configuration d'une zone hébergée. Cela coûte 0,50 $ par mois. J'ai donc choisi AWS et j'ai créé mon compte.

Le grand avantage d'AWS est le prix et c'est un fournisseur d'hébergement fiable. Mais une chose à garder à l'esprit est que vous dépendez de leur documentation. Lorsque j'ai commencé à lire sur les services offerts par AWS, cela est rapidement devenu confus ! J'ai utilisé le guide officiel d'AWS [fournis](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) pour configurer des sites web statiques. Mais je me suis perdu en cliquant sur un lien vers un autre lien et ainsi de suite. J'ai commencé à rechercher d'autres guides pour combler les lacunes de connaissances.

J'ai trouvé ce guide excellent [guide de Victoria Drake](https://victoria.dev/verbose/hosting-your-static-site-with-aws-s3-route-53-and-cloudfront/).

J'ai suivi le guide de Victoria Drake parallèlement à celui d'AWS et j'ai réussi à me débrouiller. Mais il y avait encore quelques choses qui n'étaient pas expliquées et que j'espère éclaircir.

Avant de continuer, voici votre liste de choses à faire :

* Faites des recherches sur les registrars de domaines et achetez votre nom de domaine.
   
* Inscrivez-vous pour un compte gratuit avec AWS.
   
* Ayez à la fois la [documentation d'AWS](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html) et le [guide de Victoria Drake ouvert](https://victoria.dev/verbose/hosting-your-static-site-with-aws-s3-route-53-and-cloudfront/). Utilisez mon guide pour vous guider à travers la documentation (j'espère que cela a du sens !).
   

C'est parti !

#### **AWS : Créer une zone hébergée sur Route 53.**

Route 53 est l'endroit où toutes vos requêtes DNS sont gérées.

La première chose que vous devez configurer est votre zone hébergée avec Route 53. C'est vraiment facile si vous avez acheté votre domaine via AWS. Une zone hébergée est créée automatiquement une fois que vous l'avez acheté. Si vous avez fait cela, passez simplement à la section suivante (**Configurer vos buckets S3**).

Cependant, si vous êtes comme moi et que vous avez acheté votre nom de domaine via un autre registrar, veuillez faire ce qui suit.

**Cette partie suivante explique comment créer une zone hébergée sur Route 53 si vous n'avez pas acheté votre nom de domaine auprès d'AWS :**

1. [Allez sur Route 53](https://console.aws.amazon.com/route53/home?#hosted-zones:) dans votre console et cliquez sur « Créer une zone hébergée ». Remplissez votre adresse de domaine, le commentaire est facultatif et choisissez une « Zone hébergée publique ». Cliquez sur « Créer ».
   

![Image](https://www.freecodecamp.org/news/content/images/2019/08/hostedzone1.png align="left")

2. Une fois votre zone hébergée créée, vous avez besoin de vos enregistrements NS (Name Servers) :
   

![Image](https://www.freecodecamp.org/news/content/images/2019/08/hostedzone2-1.png align="left")

3. Allez sur votre registrar de nom de domaine et connectez-vous. Selon votre registrar, vous devriez trouver une section dans vos paramètres appelée « Nameservers » que vous pouvez modifier. Vous devez copier les enregistrements NS d'AWS et modifier les enregistrements NS existants dans vos paramètres de domaine.
   

Veuillez noter, ne copiez pas le point final à la fin de l'enregistrement NS. Par exemple, cela devrait être « ns-63.awsdns-07.com », et non « ns-63.awsdns-07.com. »

**Cela peut prendre jusqu'à 24 heures pour se propager.**

### **Configurer vos buckets S3**

En attendant, vous pouvez configurer vos buckets S3. Le bucket S3 est le stockage pour vos fichiers tels que votre index.html.

Vous devez configurer deux buckets pour votre site web : 1) votredomaine.com et 2) www.votredomaine.com.

Le premier bucket est votre bucket principal où vous téléchargerez tous vos documents, comme votre index.html. Le deuxième bucket redirige vers le premier bucket. Pour configurer vos buckets S3, veuillez suivre la documentation AWS sur la façon de configurer votre bucket S3 ([2 : Créer et configurer des buckets et télécharger des données](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html#root-domain-walkthrough-s3-tasks)).

En plus de la documentation, il y a quelques points à noter :

* Dans la section 2.1 (partie 2) : cliquez sur le lien [Comment créer un bucket S3 ?](https://docs.aws.amazon.com/AmazonS3/latest/user-guide/create-bucket.html) C'est un guide étape par étape qui explique tous les paramètres que vous devez choisir.
   
* Dans la section 2.1 (partie 3) : vous n'avez pas encore à télécharger vos fichiers de site web. Vous pouvez ajouter un index.html de test en attendant.
   

Prenez note de votre **endpoint**. Vous pouvez le trouver dans votre bucket S3 > onglet « Propriétés » > boîte « Hébergement de site web statique ». Cela devrait ressembler à ceci : http://votredomaine.com.s3-website.eu-west-2.amazonaws.com

### **Ajouter les enregistrements Alias/A dans Route 53**

Enfin, retournez à Route 53 et ouvrez votre zone hébergée pour configurer vos enregistrements Alias. Vous pouvez suivre [la documentation](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-custom-domain-walkthrough.html#root-domain-walkthrough-add-arecord-to-hostedzone) sur « Étape 3 : Ajouter des enregistrements Alias pour exemple.com et www.exemple.com ». C'est assez simple.

Une fois que les paramètres NS se sont propagés, **votre site est en ligne** ! Vous pourrez visiter votre site à l'adresse de domaine, par exemple votredomaine.com

Cependant, veuillez noter qu'il ne sera pas sécurisé et vous verrez un préfixe **http://** dans la barre d'adresse. J'en parlerai dans la section suivante.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/undraw_security_o890.png align="left")

### **Comment sécuriser votre site web et qu'est-ce qu'un certificat SSL ?**

Il est très important de sécuriser votre site web et pour cela, vous devrez obtenir un certificat SSL. SSL signifie [Secure Sockets Layer](https://en.wikipedia.org/wiki/Transport_Layer_Security) et il utilise le chiffrement pour transférer des données de manière sécurisée entre un utilisateur et un site. Google donnera également un coup de pouce dans le classement pour les sites web avec HTTPS.

Si vous sécurisez le site web avec un certificat SSL, vous verrez **https://** et un symbole de cadenas dans votre barre d'adresse.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-19-at-01.05.23.png align="left")

Il existe différents types de certificats SSL : [Certificat à validation étendue](https://en.wikipedia.org/wiki/Extended_Validation_Certificate) et un [Certificat validé par domaine](https://en.wikipedia.org/wiki/Domain-validated_certificate). Pour un site web personnel ou un blog, seul un certificat validé par domaine est requis. Vous ne verrez pas non plus le nom de votre entreprise à gauche de la barre comme dans l'exemple ci-dessus. Vous n'obtenez cela que si vous avez un certificat à validation étendue, qui est plus destiné aux grandes entreprises/entreprises.

### **Combien coûte un certificat SSL ?**

J'ai vu différentes façons d'obtenir un certificat SSL. Vous pouvez payer un supplément pour un service qui le fera pour vous ou vous pouvez le faire gratuitement avec [Lets Encrypt](https://letsencrypt.org/getting-started/). Lets Encrypt est une autorité de certification (CA) officielle. Mais vous devez renouveler votre certificat tous les trois mois et le processus est assez compliqué.

Je ne voulais pas payer un supplément ni avoir la corvée de renouveler tous les trois mois. Heureusement, AWS peut délivrer des certificats SSL pour un [très petit coût](https://aws.amazon.com/certificate-manager/pricing/). Vous payez 0,75 $ pour chaque certificat délivré et il est valable pour un an.

Si vous choisissez de ne pas utiliser AWS, assurez-vous de faire vos recherches et de choisir une [CA de confiance](https://www.geckoandfly.com/24460/free-trusted-ssl-certificate/) !

### **Comment obtenir un certificat SSL avec AWS ?**

Connectez-vous à votre console AWS et accédez à [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/) (ACM).

**Assurez-vous de changer la région de la valeur par défaut (Ohio) à N. Virginie.** Cela n'est pas explicite dans les guides et seule la région N. Virginie peut délivrer des certificats. J'ai appris à la dure et j'ai perdu beaucoup de temps !

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-19-at-01.23.52.png align="left")

Ensuite, cliquez sur « Commencer » sous « Approvisionner des certificats ».

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-18-at-14.55.14.png align="left")

Suivez [la documentation avec AWS](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) (« Demander un certificat public en utilisant la console ») et utilisez [le guide de Victoria Drake](https://vickylai.com/verbose/hosting-your-static-site-with-aws-s3-route-53-and-cloudfront/) (sous « Certificat SSL »).

**En plus des guides**, il y a quelques points qui n'étaient pas entièrement expliqués :

* Vous devrez **valider la propriété de votre domaine** par e-mail ou directement avec le DNS. Je vous suggère de toujours vérifier la propriété par [**validation DNS**](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-validate-dns.html).
   
* Une fois que vous avez demandé votre certificat, vous obtiendrez quelque chose comme ceci (sauf que le statut sera en attente). Cliquez sur « Exporter le fichier de configuration DNS » :
   

![Image](https://www.freecodecamp.org/news/content/images/2019/08/acm.png align="left")

C'est un fichier Excel qui contiendra quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-18-at-15.28.11.png align="left")

* Vous devrez ajouter ces enregistrements à vos paramètres DNS avec votre registrar. Connectez-vous et allez dans les paramètres DNS. L'interface varie selon les différents registrars, mais vous cherchez vos enregistrements d'hôte sous vos paramètres DNS.
   
* Cliquez sur « Ajouter un enregistrement » > le type d'enregistrement est **CNAME** :
   

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-18-at-15.48.11.png align="left")

Vous devez ajouter deux enregistrements : 1) Le nom d'hôte doit être « @ » et le nom de cible doit être la valeur de l'enregistrement du fichier de configuration DNS.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-18-at-16.01.07.png align="left")

2. Le nom d'hôte doit être * (astérisque) et le nom de cible doit être la valeur de l'enregistrement du fichier de configuration DNS.
   

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-18-at-16.01.31.png align="left")

Si vous souhaitez plus d'informations sur le CNAME et les types d'enregistrements, j'ai trouvé cet [article utile](https://help.hover.com/hc/en-us/articles/217282457-How-to-Edit-DNS-records-A-AAAA-CNAME-MX-TXT-SRV-).

C'est assez long, mais j'ai extrait la partie utile :

> « Remarque : Le nom d'hôte fait référence au préfixe avant le nom de domaine. Pour créer un enregistrement vide, utilisez un @ dans le champ Nom d'hôte. Cela représente un préfixe vide (donc le nom correspond exactement au nom de domaine ; par exemple divapirate.com). Le nom d'hôte @ est également appelé la racine du domaine. Un * (astérisque) dans le nom d'hôte est un caractère générique et représente n'importe quel préfixe. Par exemple, créer un enregistrement pour *.divapirate.com pointera .divapirate.com vers l'adresse IP fournie. »

Vous devez simplement attendre la vérification. Pour moi, cela a pris environ une heure.

### **Comment ajouter votre certificat SSL ?**

Avec AWS, vous pouvez ajouter un certificat SSL à votre site web en configurant [**CloudFront**](https://docs.aws.amazon.com/AmazonS3/latest/dev/website-hosting-cloudfront-walkthrough.html). CloudFront est excellent pour accélérer votre site web. J'ai utilisé la [documentation AWS](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/using-https.html) et le [guide de Victoria Drake](https://victoria.dev/verbose/hosting-your-static-site-with-aws-s3-route-53-and-cloudfront/) (recherchez ses conseils utiles).

Veuillez noter que lorsque vous créez votre distribution CloudFront, il y a un menu déroulant pour ajouter votre certificat SSL. Si vous avez déjà reçu un certificat SSL, il sera pré-rempli dans le menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Screen-Shot-2019-01-19-at-01.36.02-1.png align="left")

L'état dans votre tableau de bord CloudFront devrait passer à « Activé ». Cela n'est pas instantané et prend un peu de temps.

### **Presque terminé…**

Enfin, vous devez obtenir votre **Nom de domaine** à partir de la distribution CloudFront. Cela devrait être quelque chose comme ceci dsfdser83543.**cloudfront.net**.

Retournez à Route 53 > zone hébergée > modifiez les deux enregistrements Alias (Cible de l'alias) pour le nom de domaine CloudFront.

Et voilà ! Vous avez hébergé votre premier **site web statique sécurisé** avec AWS.

---

J'espère que vous avez trouvé cela utile. Si vous avez des questions ou si vous voulez simplement dire bonjour, trouvez-moi sur Twitter [@PhoebeVF](https://twitter.com/PhoebeVF)

Un grand merci à Victoria Drake pour son guide. Pour un tutoriel plus avancé sur ce sujet, veuillez consulter l'article de Victoria : ["Héberger votre site statique avec AWS S3, Route 53 et CloudFront"](https://victoria.dev/verbose/hosting-your-static-site-with-aws-s3-route-53-and-cloudfront/).

Illustrations fournies par [https://undraw.co](https://undraw.co/)