---
title: Tout ce que vous devez savoir sur AWS S3
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2020-08-10T20:25:33.000Z'
originalURL: https://freecodecamp.org/news/everything-you-need-to-know-about-aws-s3
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-10-at-6.26.31-PM.png
tags:
- name: AWS
  slug: aws
- name: S3
  slug: s3
- name: Security
  slug: security
- name: storage
  slug: storage
seo_title: Tout ce que vous devez savoir sur AWS S3
seo_desc: 'This article will provide an in-depth introduction to AWS S3 — the secure,
  scalable, and super cheap storage service from Amazon Web Services.

  If you have ever worked as a developer, you have likely come across file storage
  use cases. From simple ima...'
---

Cet article fournira une introduction approfondie à AWS S3, le service de stockage sécurisé, évolutif et super économique d'Amazon Web Services.

Si vous avez déjà travaillé en tant que développeur, vous avez probablement rencontré des cas d'utilisation de stockage de fichiers. Des images simples aux grandes vidéos, le téléchargement, le stockage et l'accès à ces fichiers lorsque vous en avez besoin est toujours délicat.

La réponse habituelle au stockage de fichiers est de les conserver sur le même serveur où vous hébergez vos applications web. Mais avec l'avènement des architectures serverless et des applications monopages, stocker des fichiers sur le même serveur n'est pas une bonne idée.

Vous pourriez argumenter que vous pouvez stocker des fichiers dans des bases de données. Mais croyez-moi, ce ne sera pas une expérience agréable.

Alors, quelle est une autre option ?

## Qu'est-ce que S3 ?

Regardons AWS S3. S3 est un service de stockage facile à utiliser, évolutif et économique d'Amazon. Vous pouvez utiliser S3 pour stocker n'importe quelle quantité de données pour une large gamme de cas d'utilisation.

L'hébergement de sites web statiques, l'archivage de données et la livraison de logiciels sont quelques scénarios généraux où S3 serait un outil parfait.

Vous pouvez facilement pousser et tirer des données avec S3 en utilisant le SDK AWS. S3 prend également en charge un certain nombre de langages de programmation populaires, vous pouvez donc utiliser votre stack existante et intégrer S3 assez facilement.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/Screenshot-2020-08-10-at-6.14.06-PM.png)
_Console AWS_

S3 offre également une excellente interface utilisateur via la [console AWS](https://aws.amazon.com/console/). Vous pouvez l'utiliser pour voir les données poussées vers S3 ainsi que des options supplémentaires telles que la sécurité et le contrôle de version.

### Buckets

Dans S3, les fichiers sont stockés dans des buckets. Les buckets sont similaires aux dossiers sur votre ordinateur.

Chaque bucket a son propre nom unique qui ne peut être utilisé qu'une seule fois. Par exemple, s'il y a un bucket appelé « freecodecamp », ni vous ni personne d'autre ne pouvez réutiliser le même nom de bucket.

Cela est utile pour identifier de manière unique les ressources et pour l'hébergement de sites web statiques avec des noms de domaine.

Il n'y a pas de limites sur le nombre de fichiers que vous pouvez stocker dans un bucket. Les buckets offrent également des fonctionnalités supplémentaires telles que le contrôle de version et les [politiques](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html).

Vous pouvez également utiliser différents buckets pour une seule application. Par exemple, une application qui stocke des dossiers médicaux peut utiliser deux buckets : un pour les données privées des clients et un autre bucket public qui contient des livres blancs.

S3 est également un service de stockage basé sur des objets, ce qui signifie que S3 considère chaque fichier comme un objet. Chaque objet peut avoir ses propres métadonnées qui incluent le nom, la taille, la date et d'autres informations.

## Types de stockage S3

S3 dispose de trois classes de stockage basées sur des cas d'utilisation généraux.

### S3 Standard

S3 Standard est le plan de stockage par défaut dans lequel vous serez placé lorsque vous commencerez à utiliser S3. La classe de stockage standard offre d'excellentes performances, durabilité et disponibilité.

S3 Standard est idéal si vous avez des données auxquelles vous devez accéder fréquemment.

### S3 Accès peu fréquent (S3-IA)

S3 Accès peu fréquent offre un prix inférieur pour les données par rapport au plan standard. Vous pouvez utiliser S3-IA pour les données dont vous avez besoin moins souvent.

S3-IA est idéal pour des cas d'utilisation tels que les sauvegardes et la récupération après sinistre.

### Glacier

Glacier est l'option de stockage la moins chère dans S3 mais est conçu pour le stockage d'archives. Vous ne pouvez pas récupérer les données de Glacier aussi rapidement que Standard ou S3-IA, mais c'est une excellente option pour l'archivage de données à long terme.

En plus de choisir l'une de ces trois classes de stockage, vous pouvez également définir des politiques de cycle de vie dans S3. Cela signifie que vous pouvez planifier le déplacement automatique des fichiers vers S3-IA ou Glacier après une certaine période de temps.

## Pourquoi utiliser S3 ?

Des entreprises comme Netflix, Dropbox et Reddit sont des utilisateurs assidus de S3. Le populaire système de stockage de fichiers Dropbox a construit toute sa capacité de stockage sur la base d'Amazon S3.

Examinons quelques-unes des fonctionnalités principales de S3 et comprenons pourquoi il est si populaire parmi les entreprises et les startups.

### C'est abordable

S3 est bon marché. Je veux dire super bon marché par rapport à d'autres solutions de stockage. Et avec S3, vous ne payez que pour ce que vous utilisez. Il n'y a pas de coûts initiaux, pas de configuration. C'est juste du plug and play.

En plus d'un prix abordable, S3 offre un niveau gratuit. Ce niveau gratuit comprend 5 Go d'espace de stockage, 20 000 requêtes GET, 2 000 requêtes PUT, COPY, POST ou LIST et 15 Go de transfert de données. Le niveau gratuit est disponible chaque mois pendant la première année.

Avec S3, vous pouvez éviter de payer pour l'espace ou la bande passante dont vous n'avez peut-être même pas besoin.

### C'est évolutif

S3 évolue avec votre application. Puisque vous ne payez que pour ce que vous utilisez, il n'y a pas de limite à la quantité de données que vous pouvez stocker dans S3.

Cela est utile dans plusieurs scénarios, surtout lors d'une augmentation inattendue de la croissance des utilisateurs. Vous n'avez pas à acheter d'espace supplémentaire. S3 vous couvre.

### C'est sécurisé

L'une des nombreuses raisons pour lesquelles les entreprises préfèrent S3 est son inclination vers la sécurité. Alors que vous devez sécuriser les configurations de serveur personnalisées, S3 est sécurisé par défaut.

Cela ne signifie pas que vous ne pouvez pas stocker d'informations accessibles au public dans S3. S3 verrouille toutes vos données avec une sécurité élevée, sauf si vous configurez explicitement le contraire.

S3 maintient également des programmes de conformité, tels que PCI-DSS, HIPAA/HITECH, FedRAMP, EU Data Protection Directive et FISMA, pour vous aider à répondre aux exigences réglementaires de votre secteur.

### Il a un versioning

Le versioning signifie conserver plusieurs copies d'un fichier et suivre ses modifications au fil du temps. Cela est utile, surtout lorsque vous manipulez des données sensibles.

Vous pouvez également récupérer des fichiers supprimés accidentellement lorsque vous activez le versioning avec S3.

Cependant, si vous activez le versioning, vous stockez plusieurs copies du même document. Cela peut avoir un effet sur les prix ainsi que sur les requêtes de lecture/écriture que vous effectuez.

Donc, tenez simplement compte de cela lors de l'intégration du versioning pour votre application.

Le versioning est désactivé par défaut pour S3, mais vous pouvez activer le versioning en utilisant la console AWS.

### C'est durable

La durabilité des données est une fonctionnalité sous-estimée de S3. Étant donné à quel point la perte de données est courante parmi les entreprises, la durabilité des données est un facteur clé à considérer lors de la construction de logiciels d'entreprise.

S3 fournit une infrastructure de stockage hautement durable. S3 stocke de manière redondante les données dans plusieurs installations, rendant vos données sûres en cas de défaillance du système. S3 effectue également des vérifications régulières de l'intégrité des données pour s'assurer que vos données sont intactes.

S3 offre une durabilité de 99,999999999 % (appelée la durabilité des 9s) et une disponibilité de 99,99 % des objets sur une année donnée.

## Cas d'utilisation de S3

### Hébergement de site web statique

Vous pouvez utiliser S3 comme plateforme d'hébergement de site web statique. La différence entre les sites web statiques et dynamiques est que les sites web dynamiques reçoivent et traitent les entrées des utilisateurs. Les sites web statiques sont utilisés uniquement pour afficher des informations.

Avec l'avènement des [applications monopages](https://en.wikipedia.org/wiki/Single-page_application), vous pouvez héberger une application web complète sur S3, souvent gratuitement.

Des frameworks comme React et Angular ont permis de traiter les entrées des utilisateurs dans le navigateur. Vous pouvez construire une SPA qui écoute les API tierces et l'héberger dans S3.

S3 offre également un excellent support pour le routage, vous pouvez donc utiliser votre propre domaine personnalisé.

J'ai récemment écrit un article sur l'hébergement d'une application web React en utilisant S3 et [vous pouvez trouver l'article ici](https://medium.com/@manishmshiva/aws-s3-hosting-a-react-web-app-on-aws-s3-2ff2e8ca78dd).

### Analytics

Vous pouvez exécuter des requêtes sur vos données S3 sans déplacer vos données vers une plateforme d'analyse. Cela fait de S3 un excellent cas d'utilisation pour construire des applications d'analyse puissantes.

S3 offre plusieurs options, y compris S3 Select, Amazon Athena et Amazon Redshift Spectrum. Vous pouvez également combiner ces options avec [AWS Lambda](https://aws.amazon.com/lambda/) pour effectuer le traitement des données à la volée.

### Partage de fichiers

Amazon S3 peut également être utilisé comme une solution de partage de fichiers économique. Comme je l'ai mentionné plus tôt dans l'article, le célèbre service de partage de fichiers Dropbox a été initialement construit sur S3.

Avec des politiques de sécurité flexibles, vous pouvez configurer vos buckets S3 avec des permissions personnalisées pour différents clients. S3 offre également une [accélération de transfert](https://aws.amazon.com/s3/transfer-acceleration/#:~:text=S3%20Transfer%20Acceleration%20%28S3TA%29%20reduces,to%20S3%20for%20remote%20applications.) pour accélérer les transferts de gros fichiers sur de longues distances.

## Résumé

Amazon S3 est un excellent outil pour répondre à vos besoins de stockage pour vos applications web ou mobiles. Avec une tarification à la demande et une évolutivité au cœur de son fonctionnement, S3 a été la solution de stockage cloud préférée des petites et grandes entreprises.

Des entreprises comme Netflix et Pinterest font confiance à S3 pour leurs données, grâce à la promesse de durabilité des données à 99,999999999 % d'Amazon.

Vous pouvez également utiliser Amazon S3 comme solution de stockage personnelle ou héberger votre prochain projet via l'hébergement de site statique. En résumé, S3 est une excellente solution de stockage polyvalente répondant à une large gamme de cas d'utilisation.

_Je rédige régulièrement des articles sur le Machine Learning, la Cybersécurité et AWS. Vous pouvez vous inscrire à ma [newsletter hebdomadaire](https://www.manishmshiva.com/) ici._