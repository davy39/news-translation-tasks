---
title: 'Comment gérer efficacement les identifiants uniques à grande échelle : des
  GUID aux Snowflake ID et autres solutions modernes'
subtitle: ''
author: Gor Grigoryan
co_authors: []
series: null
date: '2024-08-20T18:21:25.416Z'
originalURL: https://freecodecamp.org/news/how-to-effectively-manage-unique-identifiers-at-scale
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1724012658962/2e754dc4-248a-4a2b-8819-993514474a22.jpeg
tags:
- name: scalability
  slug: scalability
- name: design patterns
  slug: design-patterns
- name: unique identifier
  slug: unique-identifier
- name: guid
  slug: guid
- name: best practices
  slug: best-practices
seo_title: 'Comment gérer efficacement les identifiants uniques à grande échelle :
  des GUID aux Snowflake ID et autres solutions modernes'
seo_desc: 'What Are Unique Identifiers? 🪪

  Unique identifiers (UIDs) are crucial components in software engineering and data
  management. They serve as distinct references for entities within a system and ensure
  that each item – whether a database record, a user...'
---

## Que sont les identifiants uniques ? 🪪

Les identifiants uniques (UID) sont des composants cruciaux dans l'ingénierie logicielle et la gestion des données. Ils servent de références distinctes pour les entités au sein d'un système et garantissent que chaque élément – qu'il s'agisse d'un enregistrement de base de données, d'un utilisateur ou d'un fichier – peut être identifié et accédé de manière unique.

Les UID sont essentiels pour la maintenance des données, permettant une recherche et une récupération efficaces, et soutenant des opérations à grande échelle dans les systèmes distribués. À mesure que les volumes de données et la complexité des systèmes augmentent, le besoin de solutions d'UID évolutives devient de plus en plus important.

Dans cet article, vous apprendrez tout sur l'histoire des identifiants uniques, ainsi que sur le fonctionnement de certaines solutions modernes.

## Table des matières :

* [Introduction aux identifiants uniques 🪪](#introduction-aux-identifiants-uniques)
    
    * [Le contexte historique des identifiants](#le-contexte-historique-des-identifiants)
        
    * [Gestion des identifiants uniques par les gouvernements](#gestion-des-identifiants-uniques-par-les-gouvernements)
        
    * [Structure des numéros de sécurité sociale](#structure-des-numeros-de-securite-sociale)
        
* [Scalabilité dans les systèmes gouvernementaux](#scalabilite-dans-les-systemes-gouvernementaux)
    
    * [Les entreprises technologiques et leur échelle](#les-entreprises-technologiques-et-leur-echelle)
        
    * [Meta (Facebook)](#meta-facebook)
        
    * [X (Twitter)](#x-twitter)
        
    * [Telegram](#telegram)
        
* [Le rôle des identifiants auto-incrémentés et leurs problèmes de scalabilité](#le-role-des-identifiants-auto-incrementes-et-leurs-problemes-de-scalabilite)
    
* [Les numéros de séquence et leurs avantages par rapport aux identifiants auto-incrémentés](#les-numeros-de-sequence-et-leurs-avantages-par-rapport-aux-identifiants-auto-incrementes)
    
* [UUIDs : vue d'ensemble et utilisation](#uuids-vue-densemble-et-utilisation)
    
    * [Qu'est-ce qui rend les UUID si géniaux ?](#questce-qui-rend-les-uuid-si-geniaux)
        
    * [UUID Version 1](#uuid-version-1)
        
    * [UUID Version 4](#uuid-version-4)
        
    * [UUID Version 5](#uuid-version-5)
        
    * [UUID Version 7](#uuid-version-7)
        
    * [UUID Version 2, 3 et 6](#heading-uuid-version-2-3-et-6)
        
* [Snowflake ID](#snowflake-id)
    
    * [« Le problème » énoncé par Twitter :](#le-probleme-enonce-par-twitter)
        
    * [Trouver les horodatages des tweets](#trouver-les-horodatages-des-tweets)
        

### Le contexte historique des identifiants

Le concept d'identifiant unique a considérablement évolué au fil du temps, reflétant la complexité et l'échelle croissantes des sociétés humaines et des systèmes technologiques. Pour comprendre pourquoi les identifiants uniques sont si importants aujourd'hui, examinons comment nous avons historiquement géré l'identification et comment elle a été développée.

Dans les premières sociétés humaines, les individus étaient souvent identifiés par un **nom unique**. Cela suffisait généralement dans les petites communautés où tout le monde se connaissait personnellement. Mais à mesure que les populations augmentaient, il est devenu nécessaire de distinguer les individus partageant le même prénom. Cela a conduit à l'adoption des **noms de famille**.

Par exemple, en Arménie 🇦🇲, les noms de famille sont utilisés pour identifier les individus par leur famille ou leur ascendance. Prenons l'exemple d'une personne nommée Gor. Dans un petit groupe de 50 personnes, disons, identifier Gor par son seul prénom est facile.

Mais à mesure que le groupe s'agrandit pour devenir une communauté de, disons, 500 personnes, des identifiants supplémentaires deviennent nécessaires. Gor sera identifié comme Gor Grigoryan, indiquant qu'il appartient à la famille/ascendance Grigoryan. Ce nom de famille fournit une identification plus claire et relie Gor à sa lignée familiale.

Alors que les sociétés continuaient de s'étendre et que les systèmes bureaucratiques devenaient plus complexes, même les noms de famille ne suffisaient plus pour identifier les individus de manière unique. C'était particulièrement vrai dans les grandes villes et pour l'administration des services gouvernementaux. Le besoin de méthodes d'identification plus robustes est devenu évident.

### Gestion des identifiants uniques par les gouvernements

L'introduction des passeports au début du XXe siècle a marqué une étape importante dans cette direction. Les passeports comprenaient des identifiants personnels uniques, tels que les numéros de passeport, pour distinguer clairement les individus. Ces ID uniques garantissaient que chaque personne pouvait être identifiée avec précision, indépendamment des similitudes de noms ou d'autres ambiguïtés.

Plusieurs pays ont été les pionniers de l'utilisation de numéros d'identification personnels uniques pour répondre à ce besoin :

* **Allemagne** 🇩🇪 : Au XIXe siècle, l'Allemagne a mis en œuvre un système de suivi des individus à des fins de protection sociale et de conscription militaire.
    
* **Suède** 🇸🇪 : La Suède a commencé à émettre des numéros d'identification personnels (Personnummer) dans les années 1940, fournissant à chaque citoyen un identifiant unique à utiliser dans divers processus administratifs.
    
* **France** 🇫🇷 : La France a introduit le numéro d'identification national (Numéro de Sécurité Sociale) au milieu du XXe siècle pour simplifier l'administration de la sécurité sociale et d'autres services gouvernementaux.
    
* **États-Unis** 🇺🇸 : Les USA ont suivi avec l'introduction des numéros de sécurité sociale (SSN) en 1936 dans le cadre du Social Security Act. Cette approche de l'identification unique a depuis été adoptée dans le monde entier, les pays délivrant des numéros d'identification nationaux à leurs citoyens.
    

![](https://www.freecodecamp.org/news/content/images/2024/07/image-49.png align="left")

Page d'information du passeport d'Edwin James Tharp, 27 mars 1936, [Robert and Eva Tharp Collection](https://library.csun.edu/SCA/Peek-in-the-Stacks/identities).

Comme l'illustre l'image d'exemple, le passeport britannique 🇬🇧 de 1936 comprenait des informations personnelles détaillées telles que la couleur des yeux, la couleur des cheveux, la profession, la taille, ainsi que des informations sur le conjoint et les enfants du titulaire.

### Structure des numéros de sécurité sociale

Un numéro de sécurité sociale (SSN) aux États-Unis est un numéro à neuf chiffres formaté comme « AAA-GG-SSSS ». Chaque partie du SSN a historiquement porté des informations spécifiques :

1. **Numéro de zone (AAA)** : À l'origine, les trois premiers chiffres, connus sous le nom de numéro de zone, représentaient la région géographique où le SSN a été émis. Cette attribution régionale aidait à assurer une distribution systématique des numéros à travers le pays.
    
2. **Numéro de groupe (GG)** : Les deux chiffres du milieu, appelés numéro de groupe, étaient utilisés pour organiser les numéros dans une zone donnée. Les numéros de groupe allaient de 01 à 99 et étaient émis dans un ordre spécifique pour éviter les numéros en double au sein d'une même zone.
    
3. **Numéro de série (SSSS)** : Les quatre derniers chiffres sont le numéro de série, qui identifie séquentiellement chaque individu au sein d'un groupe. Cette partie du SSN garantit que même si les numéros de zone et de groupe sont les mêmes, le SSN global reste unique.
    

La Social Security Administration (SSA) a mis en œuvre plusieurs mesures pour garantir que chaque SSN soit unique pour l'ensemble de la population américaine (**341,9 millions de personnes).**

Les gouvernements du monde entier gèrent des identifiants uniques principalement à des fins administratives, telles que la sécurité sociale, la fiscalité et l'identification nationale. Ces systèmes sont conçus pour gérer de grandes populations et garantir que chaque citoyen dispose d'un identifiant unique pour les dossiers officiels.

Par exemple, la Social Security Administration (SSA) des États-Unis 🇺🇸 gère les SSN pour plus de 330 millions de personnes. De même, le gouvernement indien 🇮🇳 a émis des numéros Aadhaar, un identifiant unique à 12 chiffres, à plus de **1,3 milliard de citoyens**. Ces identifiants sont cruciaux pour accéder aux services gouvernementaux, aux prestations et à d'autres processus officiels.

![](https://www.freecodecamp.org/news/content/images/2024/07/image-52.png align="left")

[Aadhaar est le plus grand système d'identification biométrique au monde](https://en.wikipedia.org/wiki/Aadhaar) décrit comme « le programme d'identification le plus sophistiqué au monde ».

## Scalabilité dans les systèmes gouvernementaux

Bien que les systèmes gouvernementaux soient vastes, ils ne sont généralement pas confrontés aux mêmes défis de scalabilité que les entreprises technologiques. Les bases de données gouvernementales sont souvent centralisées, et le rythme auquel les nouveaux identifiants sont émis est relativement stable et prévisible. De plus, la fréquence des mises à jour et des interactions avec ces identifiants est plus faible par rapport à l'environnement dynamique des entreprises technologiques.

Les entreprises technologiques, en particulier les géants des réseaux sociaux, opèrent à une échelle totalement différente. Ces entreprises gèrent des milliards d'utilisateurs et génèrent chaque jour d'énormes quantités de données. Par exemple, Meta (anciennement Facebook) compte plus de 3 milliards d'utilisateurs actifs mensuels sur ses plateformes, incluant Facebook, Instagram et WhatsApp.

### Les entreprises technologiques et leur échelle

Prenons quelques exemples :

#### Meta (Facebook)

1. **Base d'utilisateurs** : Avec plus de **3 milliards d'utilisateurs actifs mensuels**, Meta a besoin d'un système robuste pour garantir que chaque utilisateur est identifié de manière unique.
    
2. **Publications et interactions** : Facebook voit à lui seul environ **350 millions de nouvelles publications par jour**. Chacune de ces publications, ainsi que les commentaires, mentions J'aime et partages, nécessitent un identifiant unique pour gérer les interactions efficacement.
    
3. **Messages** : Les utilisateurs de WhatsApp envoient environ **100 milliards de messages chaque jour**, chacun nécessitant un identifiant unique pour garantir que les messages sont correctement routés et stockés.
    
4. **Lignes de données uniques** : Avec la combinaison des profils utilisateurs, des publications, des commentaires, des mentions J'aime et des messages, Meta gère probablement plus de **10 billions (10^13) de lignes de données uniques**. (Si la population mondiale est d'environ 8 milliards de personnes, alors 10 billions de personnes représenteraient environ **1 250** fois la population mondiale actuelle).
    

#### X (Twitter)

Twitter, un autre géant des réseaux sociaux, compte environ **450 millions d'utilisateurs actifs mensuels**. En moyenne, les utilisateurs envoient environ **500 millions de tweets par jour**. Chaque tweet, réponse et retweet nécessite un identifiant unique pour maintenir l'intégrité et l'utilisabilité de la plateforme.

#### Telegram

Telegram est connu pour sa plateforme de messagerie à fort trafic et robuste. Avec plus de **700 millions d'utilisateurs actifs mensuels**, Telegram connaît des pics de trafic particulièrement élevés lors d'événements comme le réveillon du Nouvel An, où les utilisateurs envoient des milliards de messages en peu de temps.

Lors d'une journée typique, Telegram traite plus de **70 milliards de messages**. Chaque message, publication de canal et interaction de groupe nécessite un identifiant unique pour assurer une livraison et une organisation appropriées.

L'échelle à laquelle opèrent les entreprises technologiques nécessite des systèmes d'identifiants uniques sophistiqués et hautement évolutifs. Ces systèmes doivent gérer une forte concurrence, supporter des architectures distribuées et garantir une faible latence.

## Le rôle des identifiants auto-incrémentés et leurs problèmes de scalabilité

Les identifiants auto-incrémentés sont une méthode courante pour générer des identifiants uniques dans les bases de données relationnelles. Lorsqu'un nouvel enregistrement est ajouté à une table, la base de données attribue automatiquement la valeur entière suivante disponible au champ ID. Cette méthode est simple et garantit que chaque enregistrement au sein d'une table possède un identifiant unique sans nécessiter d'intervention manuelle.

Considérons une table pour stocker les informations des utilisateurs dans une base de données relationnelle. Lorsque le premier utilisateur est ajouté, un ID de 1 peut lui être attribué. Le deuxième utilisateur recevrait un ID de 2, et ainsi de suite.

Bien que les identifiants auto-incrémentés soient simples et efficaces pour les applications à petite échelle, ils font face à des défis importants dans les systèmes distribués plus vastes.

1. **Problèmes de concurrence** : Dans les applications à fort trafic, plusieurs transactions peuvent tenter d'insérer des enregistrements simultanément. Garantir que chaque transaction reçoive un ID auto-incrémenté unique peut entraîner des goulots d'étranglement de performance et nécessiter des mécanismes de verrouillage complexes.
    
2. **Systèmes distribués** : Dans les bases de données distribuées, où les données sont réparties sur plusieurs serveurs, maintenir une séquence globale pour les ID auto-incrémentés devient problématique. Chaque serveur devrait se coordonner avec les autres pour éviter de générer des ID en double, ce qui peut impacter considérablement la performance et la fiabilité.
    
3. **Point de défaillance unique** : S'appuyer sur une autorité centrale pour générer des identifiants auto-incrémentés introduit un point de défaillance unique. Si le serveur responsable de l'attribution des ID tombe en panne, le système entier pourrait être incapable d'ajouter de nouveaux enregistrements.
    
4. **Prévisibilité** : Les ID auto-incrémentés sont prévisibles. Si quelqu'un connaît l'ID d'un enregistrement, il peut en déduire les ID des enregistrements suivants. Cette prévisibilité peut être un problème de sécurité dans certaines applications, comme celles impliquant des transactions financières ou des données utilisateur sensibles.
    

```sql
CREATE TABLE Admins (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Users (
    Id SERIAL PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

INSERT INTO Admins (Name)
VALUES ('GorGrigoryan'),
       ('GorGrigoryan2');

SELECT * FROM Admins;


-- +----+---------------+
-- | Id | Name          |
-- +----+---------------+
-- | 1  | GorGrigoryan  |
-- +----+---------------+
-- | 2  | GorGrigoryan2 |
-- +----+---------------+
```

## Les numéros de séquence et leurs avantages par rapport aux identifiants auto-incrémentés

Les numéros de séquence sont une méthode de génération d'identifiants uniques consistant à maintenir un compteur qui est incrémenté à chaque nouvel enregistrement. Contrairement aux identifiants auto-incrémentés, qui sont généralement limités à une seule instance de base de données, les numéros de séquence peuvent être conçus pour fonctionner sur des systèmes distribués, répondant ainsi à certains problèmes de scalabilité et de concurrence associés aux ID auto-incrémentés.

Comment fonctionnent les numéros de séquence :

1. **Générateurs de séquence centralisés** : Un service central ou une table de base de données génère et gère les numéros de séquence. Chaque demande pour un nouvel identifiant incrémente le compteur et renvoie la valeur suivante.
    
2. **Générateurs de séquence distribués** : Dans un environnement distribué, les numéros de séquence peuvent être générés en divisant la plage de valeurs possibles entre différents nœuds ou en utilisant des algorithmes plus complexes pour garantir l'unicité sans coordination centrale.
    

Considérons un système de base de données distribué avec plusieurs nœuds, chacun étant responsable de la génération de numéros de séquence uniques. Le système pourrait allouer des plages de numéros de séquence à chaque nœud, garantissant qu'ils peuvent générer des identifiants de manière indépendante :

* **Nœud 1** : Plage de numéros de séquence allouée de 1 000 000 à 1 999 999
    
* **Nœud 2** : Plage de numéros de séquence allouée de 2 000 000 à 2 999 999
    
* **Nœud 3** : Plage de numéros de séquence allouée de 3 000 000 à 3 999 999
    

Chaque nœud peut désormais générer jusqu'à un million d'identifiants uniques sans avoir besoin de communiquer avec un serveur central. Cette approche améliore la scalabilité et les performances, particulièrement dans les environnements avec de fortes charges d'écriture.

```sql
CREATE SEQUENCE UserIdentifier
INCREMENT 1
START 1;

CREATE TABLE Admins (
    Id INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);

CREATE TABLE Users (
    Id INT PRIMARY KEY,
    Name VARCHAR(255) NOT NULL
);


INSERT INTO Admins (Id, Name)
VALUES(nextval('UserIdentifier'), 'GorGrigoryan'),
(nextval('UserIdentifier'), 'GorGrigoryan2');

INSERT INTO Users (Id, Name)
VALUES(nextval('UserIdentifier'), 'UserGorGrigoryan'),
(nextval('UserIdentifier'), 'UserGorGrigoryan2');


SELECT * FROM Admins;

-- +----+---------------+
-- | Id | Name          |
-- +----+---------------+
-- | 1  | GorGrigoryan  |
-- +----+---------------+
-- | 2  | GorGrigoryan2 |
-- +----+---------------+

SELECT * FROM Users;

-- +----+---------------+
-- | Id | Name          |
-- +----+---------------+
-- | 3  | GorGrigoryan  |
-- +----+---------------+
-- | 4  | GorGrigoryan2 |
-- +----+---------------+
```

Un autre avantage de l'utilisation de numéros de séquence est que vous pouvez obtenir l'ID de l'entité avant qu'elle ne soit insérée dans la base de données.

Dans le cas des ID auto-incrémentés, cette attribution est généralement gérée par la base de données lors de l'insertion, ce qui peut limiter la flexibilité. Avec les numéros de séquence, vous pouvez facilement générer l'ID côté application, ce qui peut être une tâche aisée lors de l'utilisation de certains ORM, par exemple l'ORM EF Core en C#.

Consultez les numéros de séquence sur SQL Server [ici](https://learn.microsoft.com/en-us/sql/relational-databases/sequence-numbers/sequence-numbers?view=sql-server-ver16).

## UUIDs : vue d'ensemble et utilisation

Les GUID (Globally Unique Identifiers), également connus sous le nom d'UUID (Universally Unique Identifiers), sont des identifiants de 128 bits conçus pour être globalement uniques. Un UUID typique est affiché sous forme d'une chaîne hexadécimale de 32 caractères, divisée en cinq groupes séparés par des traits d'union. Par exemple : `126e3456-e89b-12d3-a456-426614174000`.

### Qu'est-ce qui rend les UUID si géniaux ?

L'une des caractéristiques marquantes des GUID est leur immense capacité d'unicité. Avec une structure de 128 bits, le nombre total de GUID possibles est très élevé : spécifiquement, il existe `340 282 366 920 938 463 463 374 607 431 770 000 000` GUID disponibles. Pour mettre cela en perspective, comparons-le avec quelque chose de tangible.

![](https://www.freecodecamp.org/news/content/images/2024/07/image-94.png align="left")

Saviez-vous que des scientifiques ont tenté de calculer le nombre de grains de sable sur Terre ? L'écrivain scientifique David Blatner, dans son livre [Spectrums](https://www.amazon.com/Spectrums-Mind-boggling-Universe-Infinitesimal-Infinity/dp/1620405202), mentionne qu'un groupe de chercheurs de l'Université d'Hawaï a essayé d'estimer ce nombre. Ils ont déterminé que la Terre contient environ (et nous parlons de manière très approximative) 7,5 x 10<sup>18</sup> grains de sable, soit sept quintillions cinq cents quadrillions de grains. Pour en savoir plus, vous pouvez lire l'article intitulé : « [**Qu'est-ce qui est le plus grand, le nombre de grains de sable sur Terre ou d'étoiles dans le ciel ?**](https://www.npr.org/sections/krulwich/2012/09/17/161096233/which-is-greater-the-number-of-sand-grains-on-earth-or-stars-in-the-sky) »

Maintenant, comparons ces nombres :

```sql
| GUID disponibles | 340,282,366,920,938,463,463,374,607,431,770,000,000
| Grains de sable  | 75,000,000,000,000,000,000
```

Si vous décidiez de créer une application pour suivre chaque grain de sable sur Terre et attribuer à chacun un identifiant unique, vous pourriez facilement le faire en utilisant des GUID. Le plus amusant est que vous pourriez en fait répéter ce processus `4 537 098 225 612 512 846` fois sans manquer de GUID uniques ! 🤯

### UUID Version 1

L'UUID Version 1 génère des identifiants uniques basés sur l'horodatage actuel, une séquence d'horloge et un identifiant de nœud (généralement l'adresse MAC de la machine générant l'UUID).

Selon la [RFC 4122](https://datatracker.ietf.org/doc/html/rfc4122), l'horodatage est le nombre de nanosecondes depuis le 15 octobre 1582 à minuit UTC. La plupart des ordinateurs n'ont pas une horloge qui tourne assez vite pour mesurer le temps en nanosecondes. Au lieu de cela, un nombre aléatoire est souvent utilisé pour remplir les chiffres de l'horodatage au-delà de la précision de mesure de l'ordinateur.

Lorsque plusieurs UUID version 1 sont générés lors d'un seul appel d'API, la partie aléatoire peut être incrémentée plutôt que régénérée pour chaque UUID. Cela garantit l'unicité et permet une génération plus rapide.

L'UUID v1 a également l'adresse MAC attachée à lui. En incluant une adresse MAC dans l'UUID, vous pouvez être sûr que deux ordinateurs différents ne généreront jamais le même UUID. Comme les adresses MAC sont globalement uniques, notez également que les UUID version 1 peuvent être tracés jusqu'à l'ordinateur qui les a générés.

Cela garantit que l'UUID est unique à la fois dans le temps et dans l'espace. Il est approprié lorsque le **temps de génération et l'unicité de la machine** sont importants. Il est souvent utilisé dans les systèmes où l'horodatage de création est pertinent ou nécessaire.

![](https://www.freecodecamp.org/news/content/images/2024/07/image-95.png align="left")

(Image provenant d' [ici](https://datatracker.ietf.org/doc/html/rfc4122))

### UUID Version 4

L'UUID Version 4 génère des identifiants à l'aide de nombres aléatoires ou pseudo-aléatoires. Cette méthode garantit une forte probabilité d'unicité en raison du vaste nombre de GUID possibles. C'est la version d'UUID la plus courante.

Il existe 2 variantes principales d'UUID :

* Variante 1 : [Minecraft UUID](https://minecraft.fandom.com/wiki/Universally_unique_identifier), également appelé UUID « Timestamp-first »
    
* Variante 2 : « GUID »
    

![](https://www.freecodecamp.org/news/content/images/2024/07/image-96.png align="left")

([Image d'ici](https://www.uuidtools.com/minecraft))

Le GUID est entièrement aléatoire, ce qui le rend simple à générer et garantit que chaque identifiant est unique avec une probabilité très élevée. Les identifiants uniques sont composés de 128 bits. Ils sont écrits sous forme de 32 caractères utilisant des chiffres (0-9) et des lettres (A-F). Les caractères sont regroupés dans un format spécifique : 8-4-4-4-12, séparés par des traits d'union, comme ceci : `{XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX}`.

L'avantage des GUID est que vous n'avez pas besoin d'un système central pour les créer. N'importe qui peut générer un GUID à l'aide d'un algorithme, et il restera unique à travers différents systèmes et applications. Ils sont conçus pour être utilisés presque partout où un identifiant unique est nécessaire. Voici quelques exemples d'utilisation :

* Windows : utilise des GUID pour générer des clés de produit uniques
    
* Microsoft SQL Server : utilise des GUID comme clés primaires pour assurer l'unicité globale sur des bases de données distribuées
    
* AWS : utilise des GUID pour identifier de manière unique les ressources dans leur infrastructure cloud, telles que les instances EC2 et les objets S3
    
* eBay : utilise des GUID pour identifier les annonces, les transactions et les utilisateurs
    

### UUID Version 5

L'UUID Version 5 génère des identifiants uniques basés sur un identifiant d'**espace de noms** (namespace) et un **nom**. L'espace de noms et le nom sont combinés et hachés à l'aide de SHA-1 pour produire l'UUID. Cela garantit que la même combinaison d'espace de noms et de nom produira toujours le même UUID. Dans un UUID, l'espace de noms doit lui-même être un UUID, et le nom peut être n'importe quoi.

L'UUID V5 est utile pour générer des identifiants uniques cohérents pour les mêmes données d'entrée à travers différents systèmes et contextes. Disons que nous voulons générer un ID utilisateur basé sur son nom d'utilisateur. Voici comment vous pouvez y parvenir en C# :

![](https://www.freecodecamp.org/news/content/images/2024/07/image-97.png align="left")

Ici, l'UUID Version 5 résout plusieurs problèmes importants, en particulier lorsque vous avez besoin d'un identifiant cohérent et unique basé sur une entrée donnée.

Par exemple, considérons un scénario où vous avez besoin d'un ID utilisateur pour effectuer un appel API (ou toute autre chose), mais dans votre code, vous n'avez accès qu'au nom d'utilisateur. Comment le problème serait-il résolu si nous utilisions l'UUID Version 4 (GUID) ? Très probablement, cela fonctionnerait ainsi :

```csharp
/* En utilisant GUID (UUID v4) */

var userName = "bob"; // Supposons que nous n'ayons que le nom d'utilisateur
// Appel API ou appel DB pour obtenir l'ID utilisateur en utilisant le nom
var userId = await userService.GetUserIdAsync(userName);

await userService.ChangeUserNameAsync(userId, "bob-2");
```

En utilisant l'UUID Version 5 avec un espace de noms partagé entre tous vos projets, vous pouvez facilement générer l'ID utilisateur à partir du nom d'utilisateur sans effectuer d'appels API supplémentaires. Ainsi, le même code ressemblerait à ceci :

```csharp
/* En utilisant UUID v5 */

// À partir d'un code partagé
var userNamespace = SharedConstants.UserNamespace;

var userName = "bob"; // Supposons que nous n'ayons que le nom d'utilisateur

// Générer l'ID utilisateur sur place, sans appel supplémentaire
var userId = Uuid.NewNameBased(userNamespace, userName);

await userService.ChangeUserNameAsync(userId, "bob-2");
```

Cette approche élimine le besoin d'appels API redondants. Dans un système distribué, effectuer un appel API pour récupérer un ID utilisateur chaque fois que vous en avez besoin peut être inefficace et lent. Avec l'UUID Version 5, vous pouvez générer localement l'ID utilisateur à partir du nom d'utilisateur (ou de toute autre entrée), réduisant ainsi le besoin de requêtes réseau et améliorant considérablement l'efficacité de votre application.

Quel type de problème avons-nous résolu avec l'UUID v5 ? Disons que vous avez besoin d'un ID utilisateur pour un appel API mais que vous n'avez qu'un nom d'utilisateur. Si l'espace de noms est partagé entre vos projets, vous obtenez l'ID via le nom d'utilisateur sans appel API, car l'UUID v5 reproduit toujours le même UUID pour la même entrée.

De plus, l'UUID Version 5 assure l'unicité et la cohérence entre différents systèmes. Lors de l'intégration de plusieurs systèmes ou microservices, il peut être difficile de garder les ID utilisateurs cohérents. En utilisant le même espace de noms et la même entrée (comme un nom d'utilisateur), l'UUID Version 5 garantit que les ID générés sont uniques et cohérents sur tous les systèmes, facilitant une intégration et une cohérence des données plus fluides.

### UUID Version 7

Le GUID Version 7 est une nouvelle version proposée qui vise à combiner les forces des GUID basés sur l'horodatage et de ceux basés sur l'aléatoire.

#### **Problèmes avec l'UUID v4 (GUID)**

L'UUID Version 4 génère des valeurs non ordonnées dans le temps, ce qui signifie que les identifiants créés ne sont pas séquentiels. Comme ces valeurs sont générées aléatoirement, elles ne seront pas regroupées dans un index de base de données. Au lieu de cela, les insertions se produiront à des emplacements aléatoires, ce qui peut impacter négativement les performances des structures de données d'index courantes, telles que les B-trees et leurs variantes.

Dans un scénario où votre produit nécessite un *accès fréquent aux données récentes*, les identifiants non séquentiels posent un défi majeur.

Avec l'UUID Version 4, les données les plus récentes seront insérées de manière aléatoire dans tout l'index, *manquant de regroupement (clustering)*. Par conséquent, la récupération des données les plus récentes à partir d'un grand ensemble de données nécessite de parcourir de nombreuses pages d'index de la base de données.

En revanche, l'utilisation d'identifiants séquentiels garantit que les dernières données sont logiquement disposées dans la partie la plus à droite de l'index, ce qui est beaucoup plus favorable à la mise en cache. Cette organisation permet une récupération plus rapide et plus efficace des données récentes, car elle minimise le nombre de pages d'index à consulter, ce qui fait défaut à l'UUID v4.

#### **La solution avec l'UUID v7**

L'UUID v7 est conçu pour fournir des identifiants uniques et triables qui sont à la fois faciles à générer et utiles pour les systèmes distribués. Il utilise une combinaison d'horodatages et de données aléatoires pour garantir à la fois l'unicité et l'ordre temporel.

La première partie de l'UUID est un horodatage qui fournit une composante chronologique, garantissant que les UUID générés à des moments proches sont également proches en valeur. La partie restante est remplie de données aléatoires, assurant l'unicité de chaque identifiant.

![](https://www.freecodecamp.org/news/content/images/2024/07/image-98.png align="left")

[Article de Buildkite sur la migration vers UUID v7](https://buildkite.com/blog/goodbye-integers-hello-uuids)

### UUID Versions 2, 3 et 6

Vous avez peut-être remarqué que notre discussion se concentre sur les UUID Versions 1, 4, 5 et 7, et passe sous silence les Versions 2, 3 et 6. Voici pourquoi :

* **UUID Version 2** : Cette version est rarement utilisée dans les applications modernes. Elle est similaire à la Version 1 mais inclut des champs supplémentaires pour des informations de domaine (comme l'UID ou le GID POSIX). Elle était principalement utilisée dans les systèmes hérités et est aujourd'hui considérée comme largement obsolète.
    
* **UUID Version 3** : Cette version est basée sur un nom et un espace de noms, comme la Version 5. La différence principale est que la Version 3 utilise l'algorithme de hachage MD5, qui est moins sécurisé et moins efficace que l'algorithme SHA-1 utilisé dans la Version 5. La Version 5 est généralement préférée car SHA-1 est plus robuste.
    
* **UUID Version 6** : La Version 6 est encore à l'état de projet de standard. Elle est destinée à fournir un UUID ordonné dans le temps avec de meilleures performances pour les systèmes distribués, mais comme elle n'a pas encore été pleinement adoptée, nous nous concentrons sur la Version 7, qui offre des fonctionnalités similaires et bénéficie d'une plus grande dynamique.
    

## Snowflake ID

Le Snowflake ID est un système de génération d'identifiants uniques développé par Twitter pour répondre aux défis de la génération d'identifiants uniques, séquentiels et distribués de manière hautement évolutive et efficace.

Contrairement aux GUID, qui sont souvent non séquentiels et peuvent causer des problèmes de performance dans l'indexation des bases de données, les Snowflake ID sont conçus pour être à la fois ordonnés dans le temps et globalement uniques, ce qui les rend idéaux pour les systèmes distribués et les bases de données où l'ordre séquentiel est important.

Un Snowflake ID est un entier de 64 bits composé de plusieurs parties distinctes :

1. **Horodatage (41 bits) :** La plus grande partie du Snowflake ID est l'horodatage, qui enregistre le nombre de millisecondes depuis une époque personnalisée (souvent fixée à la date du premier déploiement du système). Cela garantit que les ID sont ordonnés dans le temps et peuvent être facilement triés selon leur moment de création.
    
2. **ID de Centre de données (5 bits) :** Cette partie de l'ID identifie le centre de données où l'ID a été généré, permettant au système de générer des ID uniques sur plusieurs centres de données sans conflits.
    
3. **ID de Machine (5 bits) :** Similaire à l'ID de centre de données, l'ID de machine identifie le serveur ou la machine spécifique au sein du centre de données qui a généré l'ID. Cela garantit que même au sein d'un même centre de données, les ID restent uniques.
    
4. **Numéro de séquence (12 bits) :** Le numéro de séquence est utilisé pour différencier plusieurs ID générés au cours de la même millisecondes par la même machine. *Avec 12 bits, jusqu'à 4 096 ID uniques peuvent être générés par machine par milliseconde.*
    

Le format a été créé par Twitter (désormais X) et est utilisé pour les ID des tweets. On croit souvent que chaque flocon de neige a une structure unique, d'où le nom « Snowflake ID ». Le format a été adopté par d'autres entreprises, notamment Discord et Instagram. Le réseau social Mastodon utilise une version modifiée.

Le format a été annoncé pour la première fois par X/Twitter en juin 2010. En raison de défis de mise en œuvre, [ils ont attendu la fin de l'année pour déployer la mise à jour](https://techcrunch.com/2010/10/12/twitter-snowflake/).

* X utilise des Snowflake ID pour les publications, les messages directs, les utilisateurs, les listes et tous les autres objets disponibles via l'API.
    
* Discord utilise également des snowflakes, avec leur époque fixée à la première seconde de l'année 2015.
    
* Instagram utilise une version modifiée du format, avec 41 bits pour l'horodatage et 10 bits pour un numéro de séquence.
    
* Le format modifié de Mastodon possède 48 bits pour un horodatage au niveau de la milliseconde, car il utilise l'époque UNIX. Les 16 bits restants sont destinés aux données de séquence.
    

![](https://www.freecodecamp.org/news/content/images/2024/08/image-3.png align="left")

### « Le problème » énoncé par Twitter :

> Nous utilisons actuellement MySQL pour stocker la plupart de nos données en ligne. Au début, les données étaient dans une petite instance de base de données qui est devenue une grande instance, puis finalement de nombreux grands clusters de bases de données. Pour diverses raisons, dont les détails mériteraient un article de blog entier, nous travaillons à remplacer bon nombre de ces systèmes par [la base de données distribuée Cassandra](http://cassandra.apache.org/) ou du MySQL partitionné horizontalement (sharded) (en utilisant [gizzard](http://github.com/twitter/gizzard)).
> 
> Contrairement à MySQL, Cassandra n'a aucun moyen intégré de générer des identifiants uniques – et il ne devrait pas en avoir, car à l'échelle où Cassandra devient intéressante, il serait difficile de fournir une solution universelle pour les ID. Il en va de même pour le MySQL partitionné. Nous avions besoin de quelque chose capable de générer des dizaines de milliers d'ID par seconde de manière hautement disponible.
> 
> Cela nous a naturellement conduits à choisir une approche non coordonnée. Ces ID doivent être *approximativement triables*, ce qui signifie que si les tweets A et B sont publiés à peu près au même moment, ils devraient avoir des ID proches l'un de l'autre, car c'est ainsi que nous et la plupart des clients Twitter trions les tweets.
> 
> De plus, ces numéros doivent tenir sur 64 bits. Nous avons déjà traversé le processus douloureux d'augmentation du nombre de bits utilisés pour stocker les ID de tweets [auparavant](http://www.twitpocalypse.com/). Il n'est pas surprenant que ce soit difficile à faire quand plus de [100 000 bases de code différentes sont impliquées](http://social.venturebeat.com/2010/04/14/twitter-applications/).

Consultez [ici](https://blog.x.com/engineering/en_us/a/2010/announcing-snowflake) pour plus d'informations.

### Trouver les horodatages des tweets

Nous savons tous que supprimer un tweet n'est pas vraiment possible — une fois qu'il est publié, c'est ainsi que Twitter est conçu. Cependant, l'utilisation par Twitter des Snowflake ID ajoute une tournure intéressante à cette narration. Les Snowflake ID sont conçus pour être uniques et ordonnés dans le temps, ce qui en fait non seulement des identifiants mais aussi une trace qui peut être suivie.

Le 11 mai 2019, Derek Willis de Politwoops a découvert une [liste d'ID de tweets supprimés](https://gist.github.com/naumansiddiqui4/ba3398ea85ed0ef1f3af23d47b4dcd42). En utilisant la structure Snowflake, il a pu extraire les horodatages de ces ID et a découvert les 107 tweets manquants. Cette découverte a inspiré la création de TweetedAt, un outil conçu pour récupérer avec précision les horodatages des Snowflake ID et estimer le moment des tweets générés avant que Snowflake ne soit utilisé.

![](https://www.freecodecamp.org/news/content/images/2024/08/image-2.png align="left")

Consultez [ici.](https://ws-dl.blogspot.com/2019/08/2019-08-03-tweetedat-finding-tweet.html)

## Conclusion

Les identifiants uniques jouent un rôle critique dans l'ingénierie logicielle, garantissant l'intégrité des données et permettant une gestion efficace des données à travers les systèmes distribués.

Des GUID traditionnels aux solutions modernes comme les Snowflake ID, chaque système d'identifiants offre des avantages distincts adaptés à des cas d'utilisation spécifiques.

À mesure que la technologie évolue, la compréhension de ces systèmes et de leurs implémentations devient de plus en plus importante pour faire évoluer les applications efficacement. En explorant les diverses versions et alternatives, nous pouvons prendre des décisions éclairées qui répondent au mieux à nos besoins de gestion des données à grande échelle.

#### Image de couverture : [Une publication de 2017 célébrant le franchissement de la barre des 2 milliards d'utilisateurs par Facebook](https://www.facebook.com/photo/?fbid=10103832396388711&set=a.941146602501).