---
title: Comment créer une base de données NoSQL avec RavenDB
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-07-09T15:06:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-nosql-database-with-ravendb
coverImage: https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.18.04-AM.jpg
tags:
- name: database
  slug: database
- name: NoSQL
  slug: nosql
seo_title: Comment créer une base de données NoSQL avec RavenDB
seo_desc: "By Nahla Davies\nIf you look at any website or application today, somewhere\
  \ under the hood there is a database. After all, we live in the world of Big Data.\
  \ And the volume of data is growing exponentially. \nWith so much data at hand,\
  \ we need ever more..."
---

Par Nahla Davies

Si vous regardez n'importe quel site web ou application aujourd'hui, quelque part sous le capot, il y a une base de données. Après tout, nous vivons dans le monde du Big Data. Et le volume de données croît de manière exponentielle. 

Avec autant de données à portée de main, nous avons besoin de moyens de plus en plus sophistiqués pour les stocker et les traiter. 

Ainsi, les marchés de l'emploi restent solides pour la plupart des professionnels de l'informatique [travaillant à distance depuis chez eux](https://www.freecodecamp.org/news/my-personal-tips-on-working-from-home-during-this-covid-19-season/), y compris les architectes de bases de données et les administrateurs de bases de données. 

Il existe encore plus d'opportunités dans la science des données et l'analyse. Mais vous avez besoin d'une solide fondation en programmation de bases de données pour tirer parti de ces opportunités.

Dans cet article, je vais vous présenter le système de gestion de base de données RavenDB. Nous passerons en revue certaines fonctionnalités essentielles de RavenDB et après cela, je vous guiderai à travers la configuration de votre première base de données RavenDB.

## Qu'est-ce que RavenDB ?

RavenDB est une base de données NoSQL, multiplateforme, distribuée, conforme ACID, basée sur des documents, qui offre des performances élevées tout en restant relativement facile à utiliser. 

La connaissance de la programmation de données est également cruciale pour le développement web et logiciel, qui est devenu l'un des [emplois à distance les plus lucratifs](https://www.waveapps.com/freelancing/web-development/back-end-web-developer-salary) aux États-Unis aujourd'hui. 

## Fonctionnalités de RavenDB

Pour utiliser RavenDB efficacement, vous devez comprendre comment chacune de ses fonctionnalités fonctionne et pourquoi elles sont importantes.

### Multiplateforme

RavenDB est disponible pour Windows, Linux et Raspberry Pi. Les utilisateurs de Mac peuvent exécuter RavenDB dans le système de conteneurs Docker. 

Cela donne aux développeurs une grande flexibilité lors du développement de bases de données et d'applications associées.

### Base de données distribuée

En général, une base de données distribuée héberge des données dans plusieurs emplacements physiques (par exemple, différents sites ou ordinateurs). 

Bien que les spécificités de l'architecture distribuée de RavenDB dépassent le cadre de cet article, vous devez comprendre deux de ses éléments fondamentaux : les clusters et les nœuds.

Les **clusters** sont des collections d'un nombre impair de machines, avec un minimum de trois. Chaque machine dans le cluster est un **nœud**. Les bases de données peuvent s'étendre sur un ou plusieurs nœuds du cluster. Dans certains cas, une base de données entière peut être présente sur chaque nœud d'un cluster. 

En plus de la distribution des données, les clusters gèrent automatiquement la distribution du travail, ainsi que les efforts de récupération en cas de défaillance.

L'architecture de base de données distribuée permet un débit de transactions élevé, c'est-à-dire des performances élevées. RavenDB peut gérer jusqu'à 150 000 écritures et 1 million de lectures par seconde. 

L'architecture distribuée est également plus résiliente en cas de défaillances par rapport aux bases de données relationnelles traditionnelles. 

L'architecture distribuée des bases de données NoSQL (voir ci-dessous) les rend utiles pour le développement d'applications mobiles. Cependant, vous devez rester vigilant contre les risques de sécurité mobile, car [89 % des vulnérabilités des appareils mobiles](https://tokenist.com/mobile-device-security/) ne nécessitent pas d'accès physique à l'appareil mobile.

### Conforme ACID

ACID est un acronyme pour un ensemble de propriétés de base de données qui aident à garantir le traitement fiable des transactions de base de données : 

* **Atomicité** garantit que chaque transaction de base de données est traitée comme une seule unité, peu importe le nombre de déclarations que la transaction inclut. L'atomicité empêche les mises à jour partielles problématiques. Pendant le traitement, les transactions réussissent ou échouent en tant qu'unités. Si une seule déclaration au sein de la transaction échoue, l'ensemble de la transaction échoue. Les autres clients de la base de données ne peuvent jamais percevoir une transaction comme étant partiellement résolue. 
* **Cohérence** garantit que les transactions respectent toutes les règles de validation des données dans la base de données. Si une transaction génère des données non conformes, la base de données revient à la version valide précédente. 
* **Isolation** garantit que lorsque plusieurs transactions ont lieu simultanément, les transactions ne s'affectent pas mutuellement et n'essaient pas d'utiliser des données d'une transaction en cours. La mise à jour finale de la base de données pour un ensemble de transactions simultanées est la même que si chaque transaction était traitée en série.
* **Durabilité** empêche la perte de données de transaction complétées, même en cas de défaillances du système post-traitement. Les données de transaction complétées deviennent permanentes dans le système de base de données, généralement dans une mémoire non volatile.

La plupart des bases de données NoSQL ne sont pas conformes ACID. RavenDB est une exception, [utilisant les principes ACID pour stimuler les performances élevées](https://www.ibm.com/docs/en/cics-ts/5.4?topic=processing-acid-properties-transactions) tout en garantissant l'intégrité et la fiabilité des données.

### NoSQL

La valeur de NoSQL par rapport à SQL est souvent débattue. Pour nos besoins, nous pouvons simplifier la différence. 

Dans les bases de données relationnelles traditionnelles, la programmation SQL domine. Dans les bases de données non relationnelles et distribuées, NoSQL règne. 

Les bases de données SQL reposent sur des tables. Les bases de données NoSQL peuvent utiliser d'autres bases, y compris des documents (comme le fait RavenDB), des tables dynamiques, des paires clé-valeur, et plus encore.

Les bases de données NoSQL reposent sur une architecture distribuée pour une mise à l'échelle horizontale. À mesure que la taille de la base de données augmente, elle est divisée entre plusieurs nœuds différents dans un cluster. Les bases de données SQL s'adaptent verticalement – plus de données nécessitent des serveurs plus grands.

Les recherches sont également souvent plus rapides dans les bases de données NoSQL. Alors que les requêtes de bases de données SQL reposent sur des jointures ou des combinaisons de données provenant de plusieurs tables dans une nouvelle table, les requêtes NoSQL n'ont généralement pas besoin de jointures. 

Étant donné que de nombreuses implémentations NoSQL sont basées sur le cloud, les développeurs doivent toujours garder à l'esprit le [chiffrement de leurs bases de données](https://www.freecodecamp.org/news/understanding-encryption-algorithms/) et applications à des fins de sécurité.

### Basé sur des documents

Basé sur des documents ne signifie pas que Raven ne stocke que des PDF ou des documents de traitement de texte. Pour les besoins des bases de données NoSQL, un document est une collection de données structurées (en fait semi-structurées) [autonomes](https://ravendb.net/articles/nosql-document-oriented-databases-detailed-overview). 

Vous pouvez utiliser l'un des plusieurs langages pour coder les documents qui résideront éventuellement dans la base de données NoSQL, y compris le langage de balisage extensible (XML) et la notation d'objet JavaScript (JSON). RavenDB utilise principalement des documents JSON.

Les bases de données basées sur des documents sont généralement plus efficaces que leurs homologues relationnels car elles stockent toutes les informations sur un objet dans une seule instance de document plutôt que réparties sur plusieurs tables. Cette structure augmente l'efficacité de la base de données, car elle ne nécessite pas de mappage objet-relationnel.

## Comment créer une nouvelle base de données RavenDB

Il est relativement simple de créer une nouvelle base de données RavenDB. Mais avant de créer une base de données, vous devez d'abord installer le système RavenDB. 

Vous pouvez [télécharger RavenDB sur son site web](https://ravendb.net/) en fonction de votre système d'exploitation choisi (Windows, Linux ou [Raspberry Pi](https://www.raspberrypi.org/software/)), et il existe une version Docker pour les utilisateurs de Mac. 

L'installation est rapide et facile. Vous devez sélectionner si vous souhaitez utiliser une version sécurisée ou non sécurisée. 

Les versions sécurisées nécessitent que vous ayez ou obteniez un certificat de sécurité, mais en obtenir un via RavenDB est également indolore. Des licences de certificats gratuites sont disponibles pour la version d'entrée de gamme de RavenDB.

Une fois que vous avez installé RavenDB, il ne reste que quelques étapes avant de travailler dans votre première base de données :

1. Connectez-vous à votre application RavenDB et accédez à votre tableau de bord.
2. Vous verrez un élément de menu pour les bases de données sur le tableau de bord, que vous cliquerez pour démarrer le processus.

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.18.04-AM-1.jpg)

3. La fenêtre qui s'ouvre inclut une liste déroulante pour rechercher des bases de données existantes, une boîte de recherche et un bouton Nouvelle base de données. Cliquez dessus.

4. Une fois que vous avez ouvert la nouvelle base de données, vous devez la nommer. Les noms peuvent comporter jusqu'à 128 caractères, y compris des lettres, des chiffres et une sélection limitée de caractères spéciaux ("-", "_", ".").

5. Après avoir nommé votre base de données, vous devez attribuer un facteur de réplication, qui spécifie la distribution de vos données sur les nœuds. Un facteur de réplication de un signifie que toutes les données sont dans un seul nœud. Pour les paramètres supérieurs à 1, vous pouvez choisir entre une distribution dynamique ou un paramètre manuel de nœud de réplication (avec la licence appropriée).

![Image](https://www.freecodecamp.org/news/content/images/2021/07/Screen-Shot-2021-07-05-at-9.22.36-AM.jpg)

6. Après avoir terminé ces étapes, vous retournerez à la fenêtre principale de la base de données. Il ne reste plus qu'à cliquer sur le nom de la base de données, et vous êtes prêt à commencer à créer des documents.

Pour les vrais débutants, RavenDB offre aux utilisateurs la possibilité de remplir une base de données vide avec des données d'exemple afin que vous puissiez mieux comprendre comment travailler dans la base de données.

## Conclusion

RavenDB est un système de base de données NoSQL puissant, robuste, facile à utiliser et facile à apprendre. 

Pour les utilisateurs cherchant à améliorer leurs compétences en conception et administration de bases de données, RavenDB est un terrain d'entraînement convivial.