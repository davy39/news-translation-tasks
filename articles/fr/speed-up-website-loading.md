---
title: Comment accélérer le chargement d'un site web en supprimant les octets superflus
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2025-02-24T17:05:58.966Z'
originalURL: https://freecodecamp.org/news/speed-up-website-loading
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1740094347867/d1097d7b-776f-4228-8088-7726b827271f.png
tags:
- name: code optimization
  slug: code-optimization
- name: server
  slug: server
- name: hosting
  slug: hosting
- name: Google PageSpeed
  slug: google-pagespeed
- name: cloudflare
  slug: cloudflare
- name: performance
  slug: performance
seo_title: Comment accélérer le chargement d'un site web en supprimant les octets
  superflus
seo_desc: 'Let’s start with an interesting fact: according to research done by Akamai,
  a 1-second delay in loading a website’s page can decrease the conversion rate by
  7%.

  We are currently living in a fast-paced world, where time is money for everyone.
  People e...'
---

Commençons par un fait intéressant : selon une recherche menée par [Akamai](https://www.akamai.com/newsroom/press-release/akamai-releases-spring-2017-state-of-online-retail-performance-report), un délai d'une seconde dans le chargement d'une page web peut réduire le taux de conversion de 7 %.

Nous vivons actuellement dans un monde rapide, où le temps est de l'argent pour tout le monde. Les gens s'attendent à ce que leurs sites web préférés se chargent à la vitesse de l'éclair. Une vitesse de chargement lente non seulement les poussera à aller chez un concurrent, mais nuira également au [classement du site web](https://www.freecodecamp.org/news/how-to-use-on-page-seo-techniques-to-rank-on-the-first-page/) dans les SERP.

Mais la question principale est : qui est le coupable ? Ces octets superflus que presque tous les sites contiennent. Il s'agit de fichiers de code inutiles, d'images non optimisées, et bien plus encore. Mais en suivant la bonne approche, vous pouvez facilement éliminer ces inefficacités et obtenir une excellente vitesse de chargement.

Dans cet article, je vais discuter de cette approche en détail, alors restez avec moi jusqu'à la fin.

## Table des matières

* [Pourquoi la vitesse de chargement est-elle importante ?](#heading-pourquoi-la-vitesse-de-chargement-est-elle-importante)
  
  * [Facteur de classement Google](#heading-facteur-de-classement-google)
    
  * [Impact sur l'expérience utilisateur](#heading-impact-sur-lexperience-utilisateur)
    
  * [Perception négative de la marque](#heading-perception-negative-de-la-marque)
    
  * [Conserver les utilisateurs mobiles](#heading-conserver-les-utilisateurs-mobiles)
    
* [Comment supprimer les octets superflus du site web - Différentes stratégies](#heading-comment-supprimer-les-octets-superflus-du-site-web-differentes-strategies)
  
  * [Optimiser le code](#heading-optimiser-le-code)
    
  * [Optimisation des images et des médias](#heading-optimisation-des-images-et-des-medias)
    
  * [Gérer les plugins et les scripts](#heading-gerer-les-plugins-et-les-scripts)
    
  * [Mises à niveau du serveur et de l'hébergement](#heading-mises-a-niveau-du-serveur-et-de-lhebergement)
    
* [Outils que vous pouvez utiliser pour simplifier le processus](#heading-outils-que-vous-pouvez-utiliser-pour-simplifier-le-processus)
  
  * [Minifier](#heading-minifierhttpswwwminifierorg)
    
  * [TinyPNG](#heading-tinypnghttpstinypngcom)
    
  * [Convertisseur PNG en WebP](#heading-png-to-webp-converterhttpscloudconvertcompng-to-webp)
    
  * [Google PageSpeed Insight](#heading-google-pagespeed-insighthttpspagespeedwebdev)
    
  * [Cloudflare](#heading-cloudflarehttpswwwcloudflarecom)
    
* [Conclusion](#heading-conclusion)
  

## Pourquoi la vitesse de chargement est-elle importante ?

Il existe plusieurs raisons pour lesquelles la vitesse de chargement d'un site web est considérée comme essentielle. En voici quelques-unes.

1. ### Facteur de classement Google :
  

La vitesse de chargement d'un site web est un facteur de classement confirmé. Cela signifie que les moteurs de recherche comme Google tiennent définitivement compte du temps de chargement lors de l'évaluation de la qualité d'un site web. Habituellement, la [vitesse de chargement idéale](https://sematext.com/glossary/page-load-time/) est comprise entre 0 et 2 secondes. Cependant, 3 secondes sont parfois acceptables.

Si votre site ne répond pas à ces critères, il y a une forte probabilité qu'il reçoive une pénalité de Google. Cela entraînera un classement plus bas dans la niche ciblée, ce que aucun webmaster ou entreprise ne souhaite.

2. ### Impact sur l'expérience utilisateur :
  

Une vitesse de chargement lente peut à elle seule détruire toute l'expérience utilisateur. Lorsque le site web ne se charge pas rapidement devant le visiteur, il peut le fermer et passer à un autre site pour trouver les informations, produits ou services nécessaires.

Cela réduira le nombre d'engagements des utilisateurs et augmentera le taux de rebond global du site. Un taux de rebond élevé augmente les chances de recevoir une pénalité de Google.

3. ### Perception négative de la marque :
  

Pour les entreprises ou marques en ligne, leur autorité et leur image sont tout. Lorsque leur site officiel prend trop de temps à se charger, cela endommage finalement la perception ou la crédibilité de la marque dans leur esprit. Ils se demanderont comment vous pouvez livrer un service ou un produit de premier ordre si vous n'êtes pas capable de gérer correctement un site web.

Cette impression négative réduira non seulement l'engagement des clients, mais aussi les conversions.

4. ### Conserver les utilisateurs mobiles :
  

Le mobile contribue à [58 % du trafic internet mondial](https://www.mobiloud.com/blog/what-percentage-of-internet-traffic-is-mobile). Il est également vrai que les réseaux mobiles ont souvent des problèmes de vitesse internet lente par rapport au Wi-Fi. Cela peut être particulièrement vrai pour les personnes vivant dans les zones rurales. C'est pourquoi vous devriez toujours prioriser la vitesse de chargement pour conserver efficacement les utilisateurs mobiles.

## Comment supprimer les octets superflus du site web - Différentes stratégies

Voici quelques-unes des stratégies les plus éprouvées que vous pouvez utiliser pour supprimer les octets superflus de vos sites web.

1. ### Optimiser le code :
  

Un excès de HTML, CSS et JavaScript peut grandement ralentir un site web. En raison de la taille importante des fichiers de code, le serveur hôte devra transférer plus de paquets au navigateur client, ce qui entraînera un chargement lent.

Pour résoudre ce problème, il est toujours recommandé d'optimiser le code. La technique la plus connue et utilisée à cette fin est la minification. Elle consiste à supprimer tous les :

* Caractères inutiles
  
* Espaces blancs
  
* Sauts de ligne
  
* Commentaires
  
* Éléments inutilisés.
  

Mais vous devrez vous assurer que le code fonctionne comme avant, même après la minification.

L'optimisation du code améliore les performances de l'application en réduisant le temps d'exécution et la consommation de ressources. Refactorisez les boucles inefficaces, minimisez les requêtes de base de données et utilisez la mise en cache pour améliorer la vitesse. Vous pouvez utiliser des outils de profilage pour identifier les goulots d'étranglement et rationaliser les fonctions pour des performances plus fluides et plus rapides.

Pour mieux démontrer, voici un exemple :

**Code JavaScript non optimisé :**

```javascript
greet(name) {
    if (!name) {
        console.log("Hello, Guest!");
    } else {
        console.log("Hello, " + name + "!");
    }
}
greet("John");
```

**Version minifiée :**

```javascript
function greet(n){console.log("Hello, "+(n||"Guest")+"!")}greet("John");
```

Comme vous pouvez le voir, j'ai créé la version minifiée en supprimant tous les sauts de ligne et les espaces blancs. En outre, j'ai utilisé des variables raccourcies, comme "**n**" au lieu de "**Name**". Enfin, j'ai également remplacé l'instruction If Else par une expression plus courte n || "Guest".

C'est ainsi que vous pouvez facilement condenser tout le code HTML, CSS et JavaScript de votre site web et améliorer la vitesse de chargement globale.

Gardez simplement à l'esprit qu'il existe plusieurs inconvénients à la minification du code. Par exemple, elle affecte considérablement la lisibilité du code et peut causer des défis en matière de débogage et de maintenance. Utilisez donc cette approche avec discernement.

2. ### Optimisation des images et des médias :
  

Outre le code, les images non optimisées, les [fichiers de logo](https://logocreator.io/blog/logo-file-formats/) et autres fichiers multimédias sont souvent les principaux responsables de la lenteur de la [vitesse de chargement](https://www.freecodecamp.org/news/developers-guide-to-website-speed-optimization/) d'un site web. Cela signifie que vous devez également les optimiser. Il y a de nombreuses choses que vous pouvez faire à cet égard.

Tout d'abord, vous devriez réduire la taille de l'image en termes de stockage. Il est généralement recommandé que chaque [image soit inférieure à 500 Ko](https://www.foregroundweb.com/image-size/). Mais notez que cette taille peut varier en fonction du cas d'utilisation.

Il est également judicieux de choisir des formats d'image de nouvelle génération comme WebP au lieu des formats typiques comme JPEG ou PNG. En ce qui concerne les fichiers vidéo, il est également utile d'opter pour des vidéos intégrées provenant de plateformes comme YouTube.

**Expliquons tout cela avec un exemple concret (Avant & Après).**

Supposons qu'un site web utilise une image JPEG de 2 Mo pour son article de blog. Son processus d'optimisation comprendra les étapes suivantes :

* Redimensionner l'image en premier. Les dimensions recommandées sont 1200x800.
  
* Compresser la taille de l'image à l'aide d'outils de compression d'image (nous discuterons d'un tel outil plus tard dans cet article)
  
* Maintenant, convertir le fichier JPEG en format WebP.
  
* Ajouter un texte alternatif avant la publication
  

**Après optimisation :**

* La taille du fichier image sera maintenant réduite à environ 120 Ko.
  
* Votre site web bénéficiera d'une meilleure vitesse de chargement ainsi que d'une expérience utilisateur améliorée.
  

Un autre conseil que vous pouvez considérer est le [chargement paresseux](https://www.freecodecamp.org/news/how-lazy-loading-works-in-web-development/). Cela signifie ne charger les images et les vidéos que lorsqu'elles sont sur le point d'être consommées.

En prenant soin de ces quelques éléments, vous pouvez optimiser efficacement les images et les fichiers multimédias pour obtenir des vitesses de chargement plus rapides.

3. ### Gérer les plugins et les scripts :
  

Votre site web peut contenir des plugins et des scripts inutilisés qui peuvent causer du ballonnement. Il est donc essentiel de faire des vérifications régulières pour supprimer les octets superflus.

Tout d'abord, assurez-vous de désactiver et de supprimer tous les plugins qui ne sont pas nécessaires. Ensuite, commencez à explorer des alternatives plus légères pour les plugins que vous utilisez activement. Si vous en trouvez, optez pour elles et désinstallez les plugins volumineux pour améliorer les performances et renforcer la sécurité, en particulier pour des processus comme la vérification d'identité. Assurez-vous d'utiliser la version la plus récente et la plus optimisée.

Par exemple, Revolution Slider est un plugin lourd. Il charge de grands scripts et images sur chaque page, même lorsqu'ils ne sont pas nécessaires. Cela affecte finalement la vitesse globale du site web. Certaines de ses alternatives légères que vous pourriez considérer incluent [Smart Slider 3](https://smartslider3.com/), ou tout autre slider basé sur CSS.

Ensuite vient la gestion des scripts. Ici, vous devriez d'abord limiter les scripts tiers, tels que le suivi excessif de code, les widgets de réseaux sociaux et le contenu intégré. En outre, n'oubliez pas de désactiver complètement les scripts sur les pages où ils ne sont pas nécessaires.

Un exemple utile ici est Google Analytics qui charge des scripts de suivi sur chaque page, augmentant le temps de requête. Pour résoudre ce problème, vous pouvez utiliser [Google Tag Manager](https://tagmanager.google.com/) pour charger les scripts uniquement lorsqu'ils sont nécessaires.

De plus, vous pouvez utiliser des [outils d'automatisation de workflow sans code](https://www.blaze.tech/post/no-code-automation-how-to-streamline-your-business-now) comme Zapier, Make, ou Uncanny Automator qui aident à rationaliser les processus en réduisant la dépendance aux plugins et scripts lourds.

4. ### Mises à niveau du serveur et de l'hébergement :
  

Il s'agit de la dernière stratégie que vous pouvez considérer. Votre fournisseur d'hébergement joue un rôle clé dans la détermination de la vitesse de chargement du site web. Il est donc judicieux de mettre à niveau votre plan d'hébergement et de l'obtenir auprès d'un service réputé et crédible.

N'oubliez pas non plus d'activer la compression côté serveur. Cela réduira automatiquement la taille des fichiers avant la transmission. L'optimisation des performances de la base de données est tout aussi cruciale, car [l'observabilité de la base de données permet l'analyse du pipeline de la base de données](https://www.liquibase.com/resources/guides/database-observability), aidant à identifier les inefficacités, à réduire le temps d'exécution des requêtes et à améliorer la réactivité globale du site.

Prenez également des mesures pour optimiser les requêtes de la base de données. Vous pouvez le faire en supprimant les données inutiles tout en mettant en cache les mécanismes de données. Il existe également des plugins spécialisés disponibles pour cela comme [WP-Optimize](https://wordpress.org/plugins/wp-optimize/). Il nettoie efficacement toutes les données inutiles, économisant ainsi un temps et des efforts précieux.

Vous devriez également commencer à mettre en cache les requêtes. Stockez toutes les requêtes fréquentes en mémoire. Cela réduira considérablement la charge de la base de données.

```sql
SELECT * FROM products WHERE category = 'Laptops' CACHE;
```

Cela empêche le serveur de réexécuter la même requête à plusieurs reprises.

Voici donc quelques-unes des stratégies éprouvées que vous pouvez appliquer pour éliminer les octets supplémentaires du site web et obtenir un chargement plus rapide.

## Outils que vous pouvez utiliser pour simplifier le processus

Pour simplifier le processus d'optimisation de la vitesse de chargement d'un site web, vous pouvez envisager d'utiliser les outils suivants.

1. ### [Minifier](https://www.minifier.org/)
  

Tout d'abord, nous avons Minifier, un outil dédié spécialement conçu pour automatiser le processus de minification du code en un seul clic. Il est disponible gratuitement et fonctionne pour les codes HTML, CSS et JavaScript.

En outre, l'outil dispose d'une interface intuitive pour que vous puissiez naviguer rapidement. Le minifier est formé selon les normes de développement et de minification pour garantir une vitesse et une précision maximales dans le résultat.

Tout ce que vous avez à faire est de coller ou de télécharger le fichier de code dans l'outil, d'appuyer sur le bouton "**Minify**" et d'obtenir une version condensée. Vous pouvez consulter la capture d'écran ci-dessous pour mieux comprendre son fonctionnement.

![Capture d'écran montrant le résultat de Minify](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcu5gaAosAaUCZQ7oIp3J_m_CIEyAshp2Ob6rmguvQOQvxuuz6rXJ1QdO_FSD_McnO1S-fkqv38cY7B0e4s5xBtjNa78mVns2VZRe3iUemWxR-dKgct9-OJkb6YIO2fTkhB_W3If4DYj6hb2vnzknY?key=W-8S2j9mlTlf7KW39H_m9bHu align="left")

Minify propose également une large variété d'autres outils utiles que vous pouvez utiliser si nécessaire. Certaines options notables incluent le minifier JSON et le formateur XML, entre autres.

Il n'est donc plus nécessaire de passer du temps et des efforts à minifier manuellement votre code pour une meilleure vitesse de chargement. Vous pouvez simplement utiliser cet outil et obtenir le travail fait en un seul clic.

2. ### [TinyPNG](https://tinypng.com/)
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXckb9b-_Pfw-T4icivrTC6g_pnhjpu3BSK0s-7ussuhsRRY22qGNe8DAyUINv8GgGQ5DmY579muEPcGkCjRsbSZofP9XZ1y3xqPBYriFDyh_2vl6yWM4fNYBKaA7k5Jx05pRjjw3ShVU3tT3JjeHwM?key=W-8S2j9mlTlf7KW39H_m9bHu align="left")

Beaucoup d'entre vous ont peut-être entendu parler ou même utilisé cet outil. Il s'agit d'un outil de compression d'images qui vous aidera à réduire efficacement la taille de vos images pour l'optimisation. Le bon point est que TinyPNG préserve parfaitement la qualité originale de l'image (en termes de résolution) même après la compression.

Tout ce que vous avez à faire est de télécharger la photo requise depuis votre stockage local, et l'outil fournira automatiquement une version compressée. Ne vous inquiétez pas du format de fichier, car TinyPNG prend en charge JPG, PNG, JPEG, et bien d'autres.

L'outil indique même le pourcentage de compression de l'image téléchargée, comme -51 %, et ainsi de suite. Il mentionne également la taille de la photo compressée en termes de Ko. Donc, si vous n'êtes pas satisfait de la taille du fichier, vous pouvez le compresser davantage.

3. ### [Convertisseur PNG en WebP](https://cloudconvert.com/png-to-webp) :
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcSaBUNNRRqk5A4EetHdg1CK1P6F-Ro213s3DnifuZZFF24BNJZHsP_qXjVe1rn72iPH2jZd707JRsOSIUe7PzEAH7jE0ccacHXaEbqJ0YDILtM4K4gF5IYao0wOpJ13jw-xNOzrKaJiRP926kjqQ?key=W-8S2j9mlTlf7KW39H_m9bHu align="left")

Comme je l'ai mentionné précédemment, je recommande d'utiliser des formats d'image de nouvelle génération comme WebP au lieu des anciens formats lorsque cela est possible. Habituellement, le format largement utilisé est PNG, mais pour le convertir en WebP de manière transparente, vous pouvez utiliser ce convertisseur PNG en WebP.

Il est disponible gratuitement et ne demande pas d'inscription/connexion. Visitez simplement la page et commencez à effectuer des conversions. La conversion est effectuée sans causer de dommages à la qualité et au formatage de l'image.

L'outil offre également de nombreuses fonctionnalités supplémentaires. Par exemple, vous pouvez ajuster à la fois la largeur et la hauteur de l'image. Vous pouvez également définir la qualité de l'image (niveau de compression WebP) si nécessaire. Et ce n'est pas tout, vous pouvez même sélectionner le bon ajustement pour la photo parmi les options suivantes :

* Max
  
* Rogner
  
* Mettre à l'échelle
  

4. ### [Google PageSpeed Insight](https://pagespeed.web.dev/)
  

Comment pouvez-vous améliorer la vitesse de chargement du site web lorsque vous ne savez même pas quels éléments causent des problèmes ? À cette fin, Google PageSpeed Insight est la meilleure solution. Il est développé et géré par Google.

L'outil analyse efficacement le lien de la page donné et met en évidence tous les problèmes qui causent un chargement lent. Il fournit même quatre scores différents (0-100) pour l'évaluation. Ceux-ci incluent :

* Performance
  
* Accessibilité
  
* Bonnes pratiques
  
* SEO
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXet-k73bv-y0HQXbGHfrcntmms8k_nQvcrrADNI3w9cBrFKGv9CAkMSEdOCWHFVyuRQxVXaUseYQxIa_2GA9Hl7TzDGSSO_vZqZliiX32ZNdkvoQZYhCf4i3PyKtGHOzk8pwqZ6O-gZRCwPC3gzBt0?key=W-8S2j9mlTlf7KW39H_m9bHu align="left")

Le bon point est que Google PageSpeed Insights évalue la page pour les utilisateurs mobiles et de bureau. Les résultats sont également fournis séparément. Les domaines à améliorer sont mis en évidence en rouge, avec les instructions nécessaires que vous pouvez suivre. Les bonnes parties sont marquées en vert.

En utilisant cet outil, vous pouvez facilement évaluer votre site web et ensuite faire des efforts pour améliorer la vitesse de chargement.

5. ### [Cloudflare](https://www.cloudflare.com/)
  

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeKEUhCvUoLArPXA_KRMaH4ws28-YXc6OSzP9idKqis14maZynQIrYUoHaJWF1LJ20q7UcFjAhUGc7WRKpk1S37tkaanh5VRqguD2u7ICzp5eFY5e0mMNjZJU_yl-YCm2O1hdaq2gsnwpWJDbPMGGI?key=W-8S2j9mlTlf7KW39H_m9bHu align="left")

Enfin, mais non des moindres, Cloudflare est un bon outil qui aide à améliorer la vitesse de chargement d'un site web en utilisant son réseau mondial de diffusion de contenu (CDN). Avec cette fonctionnalité, il met en cache le contenu statique sur différents serveurs dans le monde. Cela réduit finalement la latence globale et améliore la vitesse de chargement pour les utilisateurs dans différentes localisations.

En outre, Cloudflare offre également une série d'autres fonctionnalités. Par exemple, il minifie automatiquement les fichiers HTML, CSS et JavaScript. Il peut même compresser et convertir les images en formats de nouvelle génération, en particulier WebP.

Il offre une résolution DNS robuste qui réduit les temps de recherche et aide la page à se charger plus rapidement. Cette fonctionnalité protège également le site contre les attaques DDoS.

## Conclusion

Si vous souhaitez obtenir un meilleur classement et une augmentation de l'engagement des utilisateurs, vous devez optimiser la vitesse de chargement de votre site web. Les octets superflus comme les fichiers de code, les médias, etc., peuvent causer de réels obstacles, mais ne vous inquiétez pas.

En utilisant ces stratégies et outils, vous serez en mesure d'accélérer le chargement des pages en un rien de temps. J'espère que vous avez trouvé cet article intéressant et précieux.