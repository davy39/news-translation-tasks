---
title: Comment optimiser AWS Simple Storage Service pour de meilleures performances
subtitle: ''
author: The ERIN
co_authors: []
series: null
date: '2024-01-16T21:36:44.000Z'
originalURL: https://freecodecamp.org/news/how-to-optimize-aws-s3-for-performance
coverImage: https://www.freecodecamp.org/news/content/images/2024/01/s3.png
tags:
- name: AWS
  slug: aws
- name: performance
  slug: performance
- name: S3
  slug: s3
seo_title: Comment optimiser AWS Simple Storage Service pour de meilleures performances
seo_desc: 'S3 is an Amazon Web Service that provides data storage and retrieval in
  the cloud. ‌‌

  This article will discuss the common S3 performance bottlenecks and how they impact
  the service''s overall performance. It will also share some best practices to ser...'
---

S3 est un service Web Amazon qui fournit le stockage et la récupération de données dans le cloud. 

Cet article discutera des goulots d'étranglement courants de S3 et de leur impact sur les performances globales du service. Il partagera également quelques bonnes pratiques pour servir de directives afin d'optimiser les performances de votre S3. 

À la fin, vous aurez des conseils pratiques pour garantir que votre AWS S3 fonctionne au mieux et gère toutes vos données en douceur.

## Goulots d'étranglement des performances de S3

Voici quelques goulots d'étranglement courants qui influencent les performances globales de S3 :

### Latence du réseau :

La latence du réseau est le délai encouru lorsque les données voyagent entre votre application et le stockage S3. Ce délai est dû à la distance physique, au nombre de sauts de réseau et à la vitesse à laquelle les données peuvent être transmises. 

En termes plus simples, c'est comme le temps qu'il faut pour que votre demande atteigne le serveur S3 et que la réponse trouve son chemin de retour. 

### Temps de traitement des demandes :

Lorsque vous envoyez une demande à Amazon S3, le temps qu'il faut pour que le système comprenne et exécute cette demande est appelé temps de traitement des demandes. Cela implique l'authentification, l'autorisation et tout calcul nécessaire avant de répondre. 

### Traitement côté serveur :

Une fois que votre demande atteint le serveur S3, elle subit un traitement pour exécuter l'action demandée. Cela peut impliquer des tâches comme le chiffrement, les vérifications de contrôle d'accès et d'autres opérations qui impactent le temps nécessaire pour servir vos données. 

Bien que ces opérations soient essentielles, elles peuvent devenir des goulots d'étranglement si elles ne sont pas gérées efficacement.

## Impact des goulots d'étranglement sur les performances globales de S3

Ces goulots d'étranglement, individuellement ou collectivement, peuvent affecter les performances globales d'Amazon S3. Voici quelques-uns des impacts : 

### Récupération des données plus lente :

La latence du réseau et le temps de traitement des demandes peuvent entraîner des retards dans la récupération des données, affectant la vitesse globale de vos applications dépendant de S3. Une récupération lente des données peut impacter l'expérience utilisateur et la réactivité de l'application, comme attendre qu'une page web se charge.

### Débit réduit :

Les goulots d'étranglement, en particulier dans le traitement côté serveur et le temps de traitement des demandes, peuvent limiter la quantité de données transférées à un moment donné. Cette réduction du débit peut impacter la vitesse à laquelle vos applications peuvent lire ou écrire des données vers S3.

### Coûts accrus :

Les inefficacités dans le transfert et le traitement des données peuvent contribuer à une augmentation des coûts. Des temps de traitement plus longs et une utilisation supplémentaire du réseau peuvent entraîner des dépenses plus élevées pour l'utilisation de S3. L'identification et l'atténuation des goulots d'étranglement peuvent conduire à des économies de coûts et à une utilisation plus efficace des ressources.

Comprendre et traiter ces goulots d'étranglement courants est essentiel pour libérer tout le potentiel d'Amazon S3. La section suivante abordera les bonnes pratiques pour optimiser les performances de S3 et garantir une expérience de stockage cloud fluide.

## Bonnes pratiques pour l'optimisation des performances de S3

### Accélération du transfert Amazon S3

Le transfert de données vers et depuis Amazon S3 peut prendre du temps en raison de la distance physique entre votre emplacement et le serveur S3. 

L'accélération du transfert Amazon S3 est une fonctionnalité au niveau du bucket qui permet des transferts rapides, faciles et sécurisés de fichiers sur de longues distances entre votre client et un bucket S3. 

#### Quand opter pour l'accélération du transfert

Vous pourriez vouloir utiliser l'accélération du transfert sur un bucket pour diverses raisons :

* Si vous êtes loin du serveur S3, l'accélération du transfert est votre raccourci. C'est comme prendre un vol direct au lieu d'un vol avec escale.
* Pour les applications en temps réel ou les situations où le temps est essentiel, l'augmentation de la vitesse grâce à l'accélération du transfert peut être un changement de jeu.
* Vous devez transférer des gigaoctets à des téraoctets de données régulièrement à travers les continents.
* Vous ne pouvez pas utiliser toute votre bande passante disponible sur Internet lors du téléchargement vers Amazon S3.

#### Points à garder à l'esprit

* **Considérations de coût :** Bien que l'accélération du transfert accélère vos données, elle entraîne des coûts supplémentaires. 
* Le nom du bucket utilisé pour l'accélération du transfert doit être conforme DNS et ne pas contenir de périodes (".").
* L'accélération du transfert doit être activée sur le bucket.
* Après avoir activé l'accélération du transfert sur un bucket, cela peut prendre jusqu'à 20 minutes avant que la vitesse de transfert de données vers le bucket n'augmente.
* L'accélération du transfert est uniquement prise en charge dans certaines régions suivantes [régions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/transfer-acceleration.html).
* Vous devez être le propriétaire du bucket pour définir l'état d'accélération du transfert.

#### Avantages de l'accélération du transfert

* **Téléchargements et téléchargements plus rapides :** Vos données atteignent leur destination plus rapidement, rendant les téléchargements et téléchargements plus rapides. C'est comme envoyer un colis avec une livraison express au lieu d'un courrier ordinaire.
* **Expérience utilisateur améliorée :** Pour les applications dépendant de S3, les utilisateurs bénéficient de temps d'attente réduits.
* **Portée mondiale, touche locale :** Que vos utilisateurs soient à New York, Tokyo ou répartis dans le monde entier, ils bénéficient d'une vitesse comme si les données étaient juste à côté. C'est comme avoir un magasin local dans chaque ville.

AWS fournit un [outil de comparaison de vitesse d'accélération de transfert](https://s3-accelerate-speedtest.s3-accelerate.amazonaws.com/en/accelerate-speed-comparsion.html) afin qu'une comparaison puisse être faite entre les transferts S3 accélérés et non accélérés.

### Téléchargements multi-parties

Par défaut, lorsque vous téléchargez un objet vers S3, il est téléchargé sous forme de blob unique de données en un seul flux. S3 utilise l'opération PUT pour les téléchargements, ce qui limite la vitesse et la fiabilité du téléchargement en raison de la contrainte du flux unique de données.

Au lieu d'essayer de télécharger un fichier colossal, les téléchargements multi-parties le divisent en morceaux plus petits et gérables. La taille minimale des données pour un téléchargement est de 100 Mo, et vous ne devez pas utiliser un téléchargement multi-parties si vos données sont plus petites que cela.

Un téléchargement peut être divisé en un maximum de 10 000 parties, et chaque partie peut varier entre 5 Mo et 5 Go. Chacune des parties individuelles est isolée des autres, ce qui signifie que l'échec d'une partie n'affecte pas les autres parties.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/upload2.png)
_[Source](https://tech.oyorooms.com/efficiently-uploading-large-objects-to-cloud-storage-8712284b0679)_

#### Quand opter pour les téléchargements multi-parties

* **Grandes tailles de fichiers :** Les téléchargements multi-parties doivent devenir votre stratégie de prédilection pour traiter des fichiers de plusieurs gigaoctets ou plus. 
* **Connexions Internet instables :** Dans les zones où la connexion Internet peut ne pas être constante, les téléchargements multi-parties agissent comme un filet de sécurité. C'est comme avoir un plan de secours pour votre transfert de données.

#### Avantages des téléchargements multi-parties

* **Téléchargements plus rapides :** Les téléchargements multi-parties accélèrent le processus. C'est comme assembler une équipe pour travailler sur différentes sections d'un projet simultanément, garantissant une réalisation plus rapide.
* **Fiabilité dans les connexions instables :** Dans les scénarios où votre connexion Internet pourrait avoir un hoquet, les téléchargements multi-parties garantissent que le téléchargement ne échoue pas. C'est similaire à sauvegarder votre progression dans un jeu - même si le courant est coupé, vous ne perdez pas tout.
* **Optimisé pour les grands fichiers :** Lorsque vous traitez des fichiers volumineux, les téléchargements multi-parties sont comme les diviser en chapitres gérables. Cela accélère le processus et simplifie le dépannage si un problème survient.

Pour implémenter les téléchargements multi-parties, vous pouvez trouver les étapes détaillées via la [Documentation AWS](https://aws.amazon.com/premiumsupport/knowledge-center/s3-multipart-upload-cli/) 

### Mesure des performances et surveillance

Pour garantir que votre stockage Amazon S3 fonctionne au mieux, surveiller ses performances est comme lui donner un check-up régulier. Voici un guide simple sur la façon de mesurer les performances et de surveiller efficacement votre environnement S3 :

* **Débit réseau, CPU et DRAM :** Imaginez S3 comme un marché animé. Pour optimiser, vérifiez le "trafic piéton" (débit réseau), "l'efficacité des travailleurs" (CPU) et la "capacité de stockage" (DRAM). Si l'un de ceux-ci est congestionné, il est peut-être temps de considérer différents types de "travailleurs" - ou, en termes AWS, types d'instances Amazon EC2.
* Utilisez des outils d'analyse HTTP pour garantir que vos données se déplacent rapidement et efficacement.
* Surveillez le nombre d'erreurs 503 (Ralentir) Réponses d'erreur de statut en utilisant Amazon Cloudwatch, Amazon S3 Storage Lens et Amazon S3 Server Access Logging.
* **Utilisez CloudWatch pour des informations sur les performances de votre S3 :** CloudWatch utilise des métriques et des dimensions pour visualiser la santé opérationnelle de S3. Les métriques sont les points de données, tels que le nombre de demandes faites à un bucket S3, et les dimensions représentent une paire clé-valeur de l'identité de la métrique, vous aidant à filtrer et à vous concentrer sur des aspects spécifiques, comme les environnements de test. CloudWatch présente vos données visuellement, comme un ensemble de graphiques faciles à lire. C'est comme un rapport de santé pour votre S3. Les alarmes agissent comme votre système d'alerte, vous notifiant si quelque chose nécessite une attention immédiate.

### Utilisez les requêtes par plage d'octets

L'optimisation de la récupération d'objets depuis Amazon S3 implique une technique connue sous le nom de requêtes par plage d'octets. En utilisant l'en-tête HTTP Range dans une requête GET Object, vous pouvez sélectionner des plages d'octets spécifiques depuis un objet, ne transmettant que la portion désignée.

Cette approche est efficace lors de la gestion de grands objets. La récupération de plages plus petites augmente le débit global et facilite des temps de nouvelle tentative plus efficaces en cas de requêtes interrompues. 

Pour une intégration transparente avec les téléchargements multi-parties, il est recommandé d'aligner les tailles des plages d'octets avec les tailles des parties utilisées lors du processus de téléchargement. Cet alignement garantit des performances optimales, et les requêtes GET peuvent cibler directement des parties individuelles, comme en utilisant la syntaxe `GET ?partNumber=N`. 

### CloudFront

CloudFront est un réseau de diffusion de contenu (CDN) mondial qui offre aux spectateurs une diffusion de contenu rapide marquée par une faible latence et des vitesses de transfert élevées. 

En exploitant un réseau de localisations de bord stratégiquement positionnées, CloudFront met intelligemment en cache des copies de votre contenu S3, garantissant la proximité avec le spectateur. Cette proximité réduit la distance parcourue par les requêtes et réponses de contenu mis en cache par rapport aux routes directes vers votre région S3, résultant en une amélioration significative des performances. 

Pour le contenu non mis en cache, CloudFront le récupère de manière transparente depuis S3, le mettant en cache si nécessaire. 

CloudFront offre des améliorations de sécurité en restreignant l'accès direct à S3 et en permettant l'accès au contenu exclusivement via CloudFront. Cette restriction est mise en œuvre en utilisant une identité d'accès d'origine (OAI). 

De plus, le chiffrement HTTPS peut être imposé pour les situations nécessitant un chiffrement en transit entre CloudFront et le spectateur, ajoutant une couche supplémentaire de sécurité au processus de diffusion de contenu.

Pour atteindre des performances élevées, CloudFront incorpore diverses optimisations, y compris la reprise de session TLS, l'ouverture rapide TCP, l'agrafage OCSP, S2N et la fusion de requêtes. Il prend en charge une gamme de protocoles HTTP, y compris HTTP/1.0, HTTP/1.1, HTTP/2 et HTTP/3.

### S3 Select

S3 Select offre une approche rationalisée pour récupérer des données spécifiques depuis le contenu des objets en utilisant des expressions SQL. Il améliore la précision dans la récupération des données, contribue à des économies de coûts et améliore les performances globales en minimisant la quantité de données transférées.

S3 Select est polyvalent, fonctionnant de manière transparente sur des objets stockés dans les formats CSV, JSON et Apache Parquet. Cette flexibilité accommode diverses structures et types de données. Il étend ses capacités aux objets compressés avec GZip et BZip2, garantissant que même les fichiers CSV et JSON compressés peuvent être traités efficacement.

![Image](https://www.freecodecamp.org/news/content/images/2024/01/s3-select.png)
_Un diagramme qui illustre la méthode S3 select (de [ici](https://aws.amazon.com/blogs/aws/s3-glacier-select/))._

En utilisant S3 Select, le transfert de données inutile est réduit. Cette réduction des données transférées se traduit directement par des économies de coûts, car seules les informations requises sont transmises. 

Le processus rationalisé de récupération des données améliore les performances globales en garantissant que les expressions SQL utilisées dans S3 Select récupèrent efficacement les données nécessaires, contribuant à un système plus réactif et agile.

## Conclusion

L'optimisation des performances d'Amazon S3 est essentielle pour un stockage et une récupération plus rapides des données dans le cloud. 

L'identification et la résolution des goulots d'étranglement courants, tels que la latence du réseau et les retards de traitement côté serveur, constituent la base d'un environnement S3 performant. 

Ensuite, la mise en œuvre de bonnes pratiques comme les téléchargements multi-parties, l'accélération du transfert Amazon S3 et l'intégration de CloudFront rationalise les opérations et améliore l'efficacité. 

La puissance de S3 Select offre précision et agilité dans la récupération des données et les outils de surveillance comme CloudWatch pour répondre aux signaux d'erreur 503 et maintenir la santé de S3 sous contrôle. 

Alors que l'environnement cloud évolue, l'adoption de ces pratiques garantit non seulement des performances S3 optimales, mais aussi une infrastructure de stockage cloud résiliente et prête pour l'avenir.