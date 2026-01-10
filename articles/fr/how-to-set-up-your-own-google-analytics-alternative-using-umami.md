---
title: Comment mettre en place votre propre alternative à Google Analytics avec Umami
subtitle: Apprenez à configurer votre propre plateforme d'analyse web open-source
  et respectueuse de la vie privée en utilisant Umami comme une alternative simple
  et puissante à Google Analytics.
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-11-11T23:36:55.160Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-your-own-google-analytics-alternative-using-umami
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1762904171356/3c714de7-3aa3-4c4f-946f-23cecb747a2a.png
tags:
- name: analytics
  slug: analytics
- name: privacy
  slug: privacy
seo_title: Comment mettre en place votre propre alternative à Google Analytics avec
  Umami
seo_desc: 'Website analytics are crucial for understanding how visitors interact with
  your content. And while Google Analytics dominates the market, it often raises privacy
  concerns and can be complex for small projects.

  If you’re looking for a simpler, open-so...'
---

Les analyses de site web sont cruciales pour comprendre comment les visiteurs interagissent avec votre contenu. Et bien que Google Analytics domine le marché, il soulève souvent des préoccupations en matière de confidentialité et peut s'avérer complexe pour les petits projets.

Si vous recherchez une solution plus simple, open-source et respectueuse de la vie privée, [Umami](https://github.com/umami-software/umami) est une excellente alternative. Il est léger, facile à déployer et ne suit pas les données personnelles, ce qui le rend conforme aux lois modernes sur la confidentialité comme le RGPD.

Dans cet article, vous apprendrez ce qu'est Umami, pourquoi c'est une excellente alternative à Google Analytics, et comment l'installer sur votre propre serveur à partir de zéro en utilisant Sevalla.

## Ce que nous allons aborder :

1. [Comprendre Umami](#heading-comprendre-umami)
    
2. [Pourquoi choisir Umami plutôt que Google Analytics](#heading-pourquoi-choisir-umami-plutot-que-google-analytics)
    
3. [Comment installer Umami](#heading-comment-installer-umami)
    
    * [Étape 1 : Obtenir le code source](#heading-etape-1-obtenir-le-code-source)
        
    * [Étape 2 : Configurer la base de données](#heading-etape-2-configurer-la-base-de-donnees)
        
    * [Étape 3 : Construire l'application](#heading-etape-3-construire-l-application)
        
    * [Étape 4 : Démarrer le serveur](#heading-etape-4-demarrer-le-serveur)
        
    * [Étape 5 : Maintenir Umami à jour](#heading-etape-5-maintenir-umami-a-jour)
        
    * [Étape 6 : Ajouter le suivi à votre site web](#heading-etape-6-ajouter-le-suivi-a-votre-site-web)
        
    * [Étape 7 : Explorer le tableau de bord](#heading-etape-7-explorer-le-tableau-de-bord)
        
4. [Héberger Umami sur le cloud avec Sevalla](#heading-heberger-umami-sur-le-cloud-avec-sevalla)
    
5. [Confidentialité et conformité](#heading-confidentialite-et-conformite)
    
6. [Conclusion](#heading-conclusion)
    

## Comprendre Umami

Umami est une plateforme d'analyse web open-source conçue pour être rapide, simple et axée sur la confidentialité.

Elle collecte des données essentielles du site web comme les vues de pages, les référents et les informations sur les appareils sans stocker de détails personnellement identifiables. Contrairement à Google Analytics, Umami n'utilise pas de cookies et ne partage pas de données avec des tiers.

Le projet est activement maintenu par la communauté open-source et est devenu l'un des outils les plus fiables pour les développeurs et les entreprises qui souhaitent un contrôle total sur leurs analyses. Il fournit un tableau de bord clair qui affiche toutes les métriques clés en temps réel et fonctionne sur n'importe quel site web ou application.

![Tableau de bord Umami](https://cdn.hashnode.com/res/hashnode/image/upload/v1762526959534/6eb011e3-c2e4-4c22-afbe-278aa7c89847.png align="center")

Vous pouvez trouver le projet sur GitHub à l'adresse github.com/umami-software/umami et même essayer une [démo en direct ici](https://cloud.umami.is/analytics/eu/share/LGazGOecbDtaIwDr).

## Pourquoi choisir Umami plutôt que Google Analytics

Google Analytics est puissant mais souvent écrasant pour les sites web simples. Il est également lié à l'écosystème de collecte de données de Google, ce qui peut entrer en conflit avec les organisations axées sur la confidentialité.

Umami adopte une approche différente. Il ne collecte que les informations dont vous avez besoin pour prendre des décisions, telles que les sources de trafic et les pages populaires, et il stocke tout sur votre propre infrastructure.

Il n'y a pas de cookies tiers, pas de suivi des utilisateurs et pas d'intégrations cachées. Vous obtenez la propriété complète de vos données et la tranquillité d'esprit en sachant qu'elles ne quittent pas votre serveur.

De plus, Umami est gratuit sous licence MIT, ce qui le rend adapté aussi bien aux projets personnels qu'aux déploiements commerciaux.

## Comment installer Umami

Avant de commencer, assurez-vous d'avoir quelques outils et prérequis de base prêts.

Vous aurez besoin d'un serveur avec Node.js version 18.18 ou plus récente installé. Umami nécessite également une base de données pour stocker les données d'analyse. Il prend en charge PostgreSQL (version 12.14 ou supérieure), MySQL (version 8.0 ou supérieure) et MariaDB (version 10.5 ou supérieure).

### Étape 1 : Obtenir le code source

La première étape consiste à télécharger le code source d'Umami depuis GitHub. Ouvrez votre terminal et exécutez :

```powershell
git clone https://github.com/umami-software/umami.git
```

```powershell
cd umami
```

```powershell
pnpm install
```

La commande `pnpm install` installe toutes les dépendances nécessaires à l'application. Assurez-vous d'avoir pnpm installé globalement avant d'exécuter cette commande. Vous pouvez l'installer en exécutant `npm install -g pnpm`.

### Étape 2 : Configurer la base de données

Ensuite, vous devez configurer une connexion à la base de données. Créez un nouveau fichier `.env` dans le répertoire racine du projet Umami. Dans ce fichier, ajoutez la ligne suivante :

```powershell
DATABASE_URL=connection-url
```

Remplacez `connection-url` par votre chaîne de connexion réelle à la base de données. Voici deux exemples selon votre type de base de données :

Pour PostgreSQL :

```powershell
postgresql://username:password@localhost:5432/umami
```

Pour MySQL :

```powershell
mysql://username:password@localhost:3306/umami
```

Cette chaîne de connexion permet à Umami de se connecter à votre base de données et de créer automatiquement les tables nécessaires lors de la configuration.

### Étape 3 : Construire l'application

Une fois votre configuration terminée, vous pouvez construire l'application en exécutant :

```powershell
pnpm run build
```

Cette étape compile le code et le prépare pour la production. Elle initialisera également votre base de données avec les tables requises et créera un compte administrateur par défaut.

Vous pourrez vous connecter avec le nom d'utilisateur `admin` et le mot de passe `umami` après la configuration. Il est conseillé de changer ce mot de passe immédiatement après votre première connexion.

### Étape 4 : Démarrer le serveur

Il est maintenant temps de démarrer l'application. Exécutez la commande suivante :

```powershell
pnpm run start
```

Par défaut, Umami démarrera sur [http://localhost:3000.](http://localhost:3000.) Vous pouvez ouvrir cette adresse dans votre navigateur pour accéder au tableau de bord d'analyse. Si vous souhaitez le rendre accessible publiquement, vous devrez configurer un proxy inverse en utilisant un serveur web comme nginx.

### Étape 5 : Maintenir Umami à jour

Comme tout logiciel, Umami reçoit des mises à jour régulières qui incluent de nouvelles fonctionnalités, des correctifs de sécurité et des améliorations de performance. Maintenir votre installation à jour est simple.

Si vous avez installé à partir de la source, naviguez vers votre dossier Umami et exécutez :

```powershell
git pull
```

```powershell
pnpm install
```

```powershell
pnpm run build
```

Cette commande met à jour le code source, installe les nouvelles dépendances et reconstruit l'application. Si vous utilisez Docker, vous pouvez mettre à jour en récupérant les dernières images et en redémarrant les conteneurs :

```powershell
docker compose pull
```

```powershell
docker compose up — force-recreate -d
```

Une mise à jour régulière garantit que vous avez accès aux dernières fonctionnalités d'analyse et aux corrections de bogues.

### Étape 6 : Ajouter le suivi à votre site web

Après vous être connecté au tableau de bord, vous verrez une option pour ajouter un nouveau site web. Une fois créé, Umami générera un petit script de suivi.

Copiez la balise script et collez-la dans la section &lt;head&gt; des pages HTML de votre site web.

Ce script est léger et ne ralentira pas votre site. Une fois ajouté, vous commencerez à voir les données de trafic dans votre tableau de bord presque instantanément.

![Sources de trafic Umami](https://cdn.hashnode.com/res/hashnode/image/upload/v1762526987669/f1bb73cd-2e04-43e5-95a9-105f16e80f0c.png align="center")

Vous pouvez suivre plusieurs sites web à partir de la même installation Umami, ce qui est idéal pour les développeurs gérant plusieurs projets.

### Étape 7 : Explorer le tableau de bord

Le tableau de bord Umami est propre, moderne et facile à comprendre. Il affiche des métriques telles que les vues de pages, les référents, les systèmes d'exploitation et les appareils. Vous pouvez filtrer par date, voir les visiteurs en direct et exporter des données pour des rapports.

Il n'y a pas d'options de configuration compliquées ou de fonctionnalités cachées – juste les informations dont vous avez besoin pour prendre des décisions éclairées sur le trafic de votre site web. Tout fonctionne rapidement, même sur des serveurs modestes.

## Héberger Umami sur le cloud avec Sevalla

Lorsque vous êtes prêt à aller au-delà des tests, Umami vous offre deux options. Vous pouvez l'auto-héberger en utilisant votre propre infrastructure ou utiliser leur version cloud gérée sur [Umami.is](https://umami.is/).

L'auto-hébergement vous donne un contrôle total et est généralement préféré par les équipes techniques qui souhaitent conserver les données sensibles en interne.

Vous pouvez choisir n'importe quel fournisseur cloud, comme AWS, DigitalOcean ou d'autres pour configurer Umami. Mais je vais utiliser Sevalla.

[Sevalla](https://sevalla.com/) est un fournisseur PaaS conçu pour les développeurs et les équipes de développement qui déploient constamment des fonctionnalités et des mises à jour de la manière la plus efficace possible. Il propose l'hébergement d'applications, de bases de données, de stockage objet et d'hébergement de sites statiques pour vos projets.

J'utilise Sevalla pour deux raisons :

* Chaque plateforme vous facturera la création d'une ressource cloud. Sevalla offre un crédit de 50 $ à utiliser, nous n'aurons donc aucun coût pour cet exemple.
    
* Sevalla dispose d'un [modèle pour Umami](https://docs.sevalla.com/templates/overview), ce qui simplifie l'installation manuelle et la configuration de chaque ressource nécessaire à l'installation.
    

[Connectez-vous](https://app.sevalla.com/login) à Sevalla et cliquez sur Templates. Vous pouvez voir Umami parmi les modèles.

![Modèles Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1762527152703/5fdd384a-bbc0-474a-a977-501ffbcaa906.png align="center")

Cliquez sur le modèle « Umami ». Vous verrez les ressources nécessaires pour provisionner l'application comme PostgreSQL et Redis. Cliquez sur « Deploy Template ».

![Déploiements Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1762527179056/93d52be1-813f-41fa-9790-120639602275.png align="center")

Vous pouvez voir la ressource en cours de provisionnement. Une fois les ressources provisionnées, allez dans votre application Umami et cliquez sur « Visit app ».

Vous obtiendrez une URL cloud avec une page de connexion. Utilisez les identifiants de connexion par défaut `admin` pour le nom d'utilisateur et `umami` pour le mot de passe. Vous verrez le tableau de bord vide.

![Tableau de bord Umami](https://cdn.hashnode.com/res/hashnode/image/upload/v1762527213359/63015ae9-8716-4819-80c5-4352a163b87f.png align="center")

Vous avez maintenant un serveur Umami de qualité production fonctionnant sur le cloud. Vous pouvez l'utiliser pour configurer les analyses de votre site web en cliquant sur « Settings » puis sur « Add website ».

![Configuration du site Umami](https://cdn.hashnode.com/res/hashnode/image/upload/v1762527254085/e6b53462-8361-47f1-afe0-dc4c23a1734e.png align="center")

Vous pouvez ensuite cliquer sur « Edit » pour obtenir le code de suivi de votre site web.

![Configuration du site Umami](https://cdn.hashnode.com/res/hashnode/image/upload/v1762527330314/e03b25a5-9558-4937-a6dc-5d0fb50a83e3.png align="center")

Une fois que vous avez ajouté le code de suivi à votre site web, vous pouvez commencer à surveiller votre trafic et d'autres analyses dans votre nouveau tableau de bord.

## Confidentialité et conformité

L'une des meilleures raisons d'utiliser Umami est son engagement envers la confidentialité. Il n'utilise pas de cookies, ne suit pas les utilisateurs individuels et ne partage pas de données avec des services tiers.

Toutes les informations restent sur votre serveur. Cela en fait un excellent choix pour les sites web qui doivent se conformer aux lois sur la confidentialité comme le RGPD, le CCPA ou le PECR.

Puisque vous possédez les données, vous pouvez décider de la durée de conservation, de la manière de les analyser et de qui y a accès.

## Conclusion

Mettre en place votre propre système d'analyse peut sembler complexe, mais avec Umami, c'est étonnamment facile. Il vous donne tout ce dont vous avez besoin pour comprendre le trafic de votre site web sans compromettre la confidentialité des utilisateurs. Vous contrôlez les données, l'infrastructure et la configuration.

En suivant ces étapes, vous pouvez déployer Umami sur votre propre serveur en moins d'une heure et commencer à surveiller les visiteurs de votre site web immédiatement. Que vous gériez un blog personnel, une plateforme SaaS ou un projet client, Umami offre une alternative transparente, rapide et respectueuse de la vie privée à Google Analytics.

*J'espère que vous avez apprécié cet article. Retrouvez-moi sur* [*Linkedin*](https://linkedin.com/in/manishmshiva) *ou* [***visitez mon site web***](https://manishshivanandhan.com/)