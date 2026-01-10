---
title: Guide du développeur pour l'optimisation de la vitesse des sites web
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-05-12T16:07:06.000Z'
originalURL: https://freecodecamp.org/news/developers-guide-to-website-speed-optimization
coverImage: https://www.freecodecamp.org/news/content/images/2020/05/Developers-Guide-To-optimize-website.png
tags:
- name: optimization
  slug: optimization
- name: Website performance
  slug: website-performance
seo_title: Guide du développeur pour l'optimisation de la vitesse des sites web
seo_desc: 'By Digvijay Singh

  I think a lot about how we can optimize our websites for speed. The world is getting
  busy and nobody likes to wait for a website to load.

  There are very few things a user can do to make a website go faster. But for developers
  like u...'
---

Par Digvijay Singh

Je réfléchis beaucoup à la manière dont nous pouvons optimiser nos sites web pour la vitesse. Le monde devient de plus en plus occupé et personne n'aime attendre qu'un site web se charge.

Il y a très peu de choses qu'un utilisateur peut faire pour accélérer un site web. Mais pour des développeurs comme nous, les possibilités sont infinies. La véritable optimisation commence avec le code et se termine avec des aspects côté serveur comme l'hébergement, les CDN, la mise en cache et bien plus encore.

Ici, j'ai rassemblé les meilleures façons possibles d'optimiser un site web, que j'ai apprises et mises en œuvre en créant un thème pour mon blog sur Ghost CMS.

Voici une image des résultats.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ghost-new-theme-speed-demo.png)
_Démonstration du thème personnalisé_

Le thème est si rapide car il ne contient aucune fonctionnalité supplémentaire autre que ce dont j'ai besoin pour un blog très minimaliste. Je paie 5 $/mois pour l'hébergement cloud. Pour l'instant, j'ai masqué le domaine car il est hébergé temporairement (test avec quelques nouvelles choses).

## Pourquoi la vitesse est importante

Les gens sont occupés et ils ne gaspilleront pas leur temps précieux à attendre que votre site web se charge.

La vitesse de chargement des sites web est l'un des facteurs les plus importants en SEO depuis [avril 2010](https://webmasters.googleblog.com/2010/04/using-site-speed-in-web-search-ranking.html). Les utilisateurs adorent les sites web rapides où ils peuvent obtenir des informations utiles.

Une autre chose passionnante à propos de la vitesse de chargement est qu'elle affecte l'image de votre marque. Je peux facilement me rappeler de 3 à 4 sites web super rapides qui se chargent immédiatement après le clic.

Supposons que vous visitez un site de produit et qu'il met 10 secondes à se charger. Allez-vous gaspiller encore 10 secondes sur la page de paiement ? Comment cela affecterait-il votre confiance ? Ferez-vous confiance à un site web qui met autant de temps à se charger ?

> Pensez comme un utilisateur avant d'agir en tant que développeur.

Les bons sites web se chargent plus rapidement et les utilisateurs obtiennent la page web en un clin d'œil.

## Différents outils de test de vitesse

Maintenant que vous savez pourquoi nous devons optimiser nos sites web pour qu'ils se chargent plus rapidement, voici un aperçu rapide des outils populaires pour évaluer les performances.

### Votre propre navigateur

Oui, votre navigateur dispose d'un outil puissant pour vous informer de la vitesse de chargement de votre site web. Je l'utilise généralement pour obtenir des informations détaillées sur le nombre de fichiers (scripts et feuilles de style) qui se chargent à chaque requête de page web.

Ouvrez les outils de développement de votre navigateur (clic droit puis inspecter) et allez dans l'onglet réseau. Rechargez la page web avec le cache désactivé et vous verrez les statistiques détaillées de la vitesse de chargement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/chrome-network-tools.png)
_Outils réseau de Chrome_

Mais cette méthode est limitée car elle teste la vitesse de chargement uniquement depuis votre emplacement. Et nous savons que la vitesse change à différents endroits dans le monde.

### [Outils Pingdom](https://tools.pingdom.com/)

Voici la solution pour les tests de vitesse globaux : choisissez plusieurs emplacements depuis lesquels tester la vitesse de chargement de votre site web.

Il fournit également un rapport détaillé avec des recommandations que vous pouvez utiliser pour optimiser davantage.

### [Page Speed Insights](https://developers.google.com/speed/pagespeed/insights/) (Basé sur Lighthouse)

Page Speed Insights a créé la croyance qu'un score de 100 est obligatoire pour le SEO.

Ce n'est pas complètement vrai, cependant, car certains des sites web les plus populaires ont un score inférieur à 70.

Page Speed Insights utilise Lighthouse comme outil d'analyse et il n'est pas directement lié au SEO.

Lighthouse est un outil d'analyse de performance de site web open-source. Il audite le site web pour la performance, le SEO, l'accessibilité, les applications web progressives et bien plus encore.

Lighthouse est également disponible en tant qu'extension de navigateur ou [package NPM](https://www.npmjs.com/package/lighthouse) si vous développez un site web localement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/lighthouse-screenshot.png)
_Rapport d'analyse de site web Lighthouse_

Il donne des détails d'optimisation importants que d'autres outils ne signalent pas. Il est très utile pour réduire la taille de la page web et optimiser la vitesse de chargement du site web.

### [GTmetrix](https://gtmetrix.com/)

Je trouve cela beaucoup plus précis que les autres services. Il donne des informations précises sur la vitesse de chargement de votre site web. Il donne également un rapport approfondi des meilleures pratiques qui peuvent améliorer davantage les performances de votre site web.

## Les meilleures façons d'optimiser la vitesse de chargement des sites web

Voici la partie où nous allons commencer à travailler sur l'optimisation. Toutes ces étapes sont très utiles pour améliorer les performances de n'importe quel site web.

Mais rappelez-vous simplement que toutes les étapes ne sont pas nécessaires pour tout le monde. Vous pouvez sauter les étapes qui pourraient casser votre site (cela arrive souvent pendant l'optimisation).

### Évitez les packages et scripts supplémentaires autant que possible

Quand j'ai commencé le développement web, je préférais NPM install pour chaque problème. Mais j'étais un débutant :). Très vite, j'ai réalisé le coût de l'installation d'un nouveau package pour chaque problème que je rencontrais.

Utiliser des packages npm est bon pour le développement rapide, mais chaque nouveau package vient avec de nombreuses fonctionnalités supplémentaires dont vous n'aurez peut-être jamais besoin.

Le vrai problème réside dans la mise à jour du projet. Les packages se déprécient avec le temps, donc gérer beaucoup de packages est comme un cauchemar.

C'est une bonne idée d'essayer de résoudre les problèmes de base par vous-même au lieu de chercher un package NPM pour le faire à votre place.

Voici une extension utile pour [VS Code](https://marketplace.visualstudio.com/items?itemName=wix.vscode-import-cost) qui vous permet de connaître la taille du package importé.

La même chose s'applique à jQuery. Il y a eu une époque où c'était une bibliothèque JavaScript indispensable pour chaque application. Mais maintenant, Vanilla JS se tient fermement.

Si vous pouvez éviter d'utiliser jQuery, cela vous fera économiser environ 30 Ko de chargement supplémentaire sur votre page web.

Ce site web est utile pour trouver des alternatives à jQuery : [Collection incroyable d'alternatives à jQuery.](http://youmightnotneedjquery.com/)

J'ai économisé environ 100 ms simplement en supprimant jQuery de mon thème Ghost CMS. C'était beaucoup de travail pour remplacer jQuery par Vanilla JS, mais le résultat était génial.

Et il est bon de dire que chaque script compte en termes de performance.

### Supprimez le CSS inutilisé

Les frameworks CSS sont très utiles pour le développement rapide des applications web. Cependant, ils ont de nombreux composants et styles que nous n'utilisons jamais dans nos projets.

[PurgeCSS](https://purgecss.com/) est très utile dans ce cas, car il supprime le CSS inutilisé de la feuille de style.

Ce n'est pas aussi facile à utiliser qu'il n'y paraît, mais cela vaut l'investissement en temps.

Juste un avertissement : parfois PurgeCSS supprime également le CSS qui est utile à vos projets. Je recommande donc de vérifier manuellement et de tester correctement le site web après l'avoir utilisé.

Par exemple, le thème sombre de mon site web était cassé car PurgeCSS avait supprimé les variables CSS car elles n'étaient pas utilisées à ce moment-là.

### Minifiez le CSS et le JavaScript

Vous devriez minifier les fichiers JavaScript et CSS avant de les pousser sur le serveur de production.

Minifier le CSS et le JavaScript signifie supprimer le code inutile comme les commentaires, les espaces, les tabulations du fichier, car en production ils ne sont là que pour que les navigateurs comprennent.

Cela réduit environ 50 % de la taille du fichier et permet à vos pages web de se charger beaucoup plus rapidement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Minified-javascript-advantage.png)
_Taille du JavaScript minifié réduite de 47 %_

Voici des outils en ligne pour minifier le CSS et le JavaScript que vous pouvez utiliser.

* [Minificateur de CSS en ligne](https://cssminifier.com/)
* [Minificateur de JavaScript en ligne](https://javascript-minifier.com/)

Voici une autre observation en utilisant Tailwind CSS avec minify et purge CSS :

* Taille originale de la feuille de style : ~150 Ko
* Avec Minify+Purge CSS : 4,9 Ko (et tout fonctionnait bien)

Ce n'était pas une solution miracle, cependant. Initialement, cela a cassé beaucoup de choses (comme le mode nuit et de nombreuses autres fonctionnalités déclenchées par JavaScript) car purge CSS les a supprimées car elles n'étaient pas utilisées à ce moment-là.

J'ai dû passer en revue manuellement et exclure ces styles du plugin purge CSS.

### Compressez et redimensionnez les images

Les images sont des facteurs critiques qui affectent la vitesse de chargement de n'importe quel site web. Beaucoup de sites web utilisent des images haute résolution même lorsqu'ils n'en ont pas besoin.

L'exemple parfait est que vous n'avez pas besoin d'une image de 2000 x 2000 pour une image d'auteur de 250 x 250.

Pensez toujours à recadrer et compresser vos images avant de les télécharger sur le web.

Vous pouvez utiliser des outils de compression en ligne comme [Tiny PNG](https://tinypng.com/) pour compresser les images avant de les utiliser sur votre site web. Vous pouvez réduire jusqu'à 60-70 % de la taille de l'image en utilisant la compression d'image.

### Chargement paresseux des images

Comme je l'ai dit, les images sont des facteurs critiques dans la vitesse de chargement des sites web. Cela signifie que vous devez prendre les bonnes mesures pour optimiser les images lors de leur chargement.

Tout d'abord, vous pouvez différer les images hors écran. Cela signifie que les images après 1 hauteur de viewport se chargeront une fois que l'utilisateur fera défiler jusqu'à elles.

Le chargement paresseux est également recommandé et est très efficace pour optimiser votre site web pour un chargement rapide.

C'est utile car parfois l'utilisateur n'a pas besoin de faire défiler jusqu'en bas de la page et de lire tout le contenu de votre site web. Ainsi, le chargement paresseux ne charge les images que lorsque l'utilisateur fait défiler jusqu'à elles.

Vous devez mettre en œuvre le chargement paresseux avec soin et vous assurer que les solutions de repli JavaScript sont en place en tant qu'alternative.

Vous pouvez prendre l'exemple des articles de Medium.com pour le chargement paresseux des images. Ils mettent une image de très basse résolution comme espace réservé et chargent l'image originale une fois que l'utilisateur fait défiler jusqu'à elle.

<p class="codepen" data-height="265" data-theme-id="dark" data-default-tab="html,result" data-user="malchata" data-slug-hash="mXoZGx" data-preview="true" style="height: 265px; box-sizing: border-box; display: flex; align-items: center; justify-content: center; border: 2px solid; margin: 1em 0; padding: 1em;" data-pen-title="Lazy Loading Example">
  <span>See the Pen <a href="https://codepen.io/malchata/pen/mXoZGx">
  Lazy Loading Example</a> by Jeremy Wagner (<a href="https://codepen.io/malchata">@malchata</a>)
  on <a href="https://codepen.io">CodePen</a>.</span>
</p>
<script async src="https://static.codepen.io/assets/embed/ei.js"></script>

### Différez le chargement de JavaScript

Vous devriez toujours placer tous les scripts lourds à la fin de la page avant la balise de fermeture body.

```html
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Script Demo</title>
  </head>
  <body>
    <header>Some Beautiful Header that Rocks</header>
    <article> Some awesome Content ... </article>
    <section>Some more content...</section>


    <!-- C'est ici que tous les scripts et feuilles de style lourds doivent être présents. -->
    <script src="js/scripts.js" defer></script>

  </body>
</html>

```

C'est important car les utilisateurs peuvent au moins lire le contenu sur des connexions plus lentes tandis que les scripts lourds continuent de se charger en arrière-plan.

C'est l'un des problèmes les plus courants mis en évidence par Google Speed Insights. Vous pouvez facilement améliorer votre score en mettant en œuvre cette étape correctement.

L'attribut defer est utile dans ce scénario, car il permet l'exécution du script uniquement après le chargement du document.

### Choisissez un bon fournisseur d'hébergement

Vous ne pouvez jamais vous attendre à une bonne vitesse de chargement de site web sur un hébergement partagé de n'importe quel fournisseur d'hébergement de mauvaise qualité.

Optez pour un VPS si vous pouvez vous le permettre, ou un hébergement cloud (ils sont aussi bon marché que 5 $ par mois chez Linode, Digital Ocean et Vultr, par exemple).

Les fournisseurs d'hébergement de mauvaise qualité n'affecteront pas beaucoup la vitesse de votre site web si vous n'avez pas beaucoup de visiteurs. Cependant, à mesure que le nombre de visiteurs augmente, ils ne parviennent pas à gérer un tel trafic.

C'est pourquoi il est bon de rester du côté sûr et de garder votre site web en fonctionnement lors des pics de trafic.

### Utilisez un CDN

Si votre site web a des visiteurs du monde entier, alors les CDN aideront à livrer vos actifs rapidement.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/CDN-vs-without-CDN.png)
_Avec CDN vs sans CDN_

Les utilisateurs obtiennent les actifs depuis le nœud CDN le plus proche, assurant le trajet le plus court pour les données. Cela réduit la vitesse de chargement globale du site web et offre une expérience cohérente à tous vos utilisateurs.

### Mise en cache

La mise en cache est la meilleure solution possible pour la vitesse de chargement la plus rapide des sites web. Mettez en cache autant que possible, mais avec soin.

La mise en cache côté serveur permet une livraison plus rapide des données et côté client, elle permet une vitesse de chargement ultra-rapide.

Il existe diverses ressources comme des scripts, des feuilles de style et d'autres fichiers communs qui sont utilisés à chaque chargement de page. Nous pouvons les mettre en cache localement afin que la prochaine fois, ils soient récupérés depuis le cache au lieu du serveur.

La mise en cache côté serveur évite les opérations excessives sur la base de données à chaque fois et économise à la fois du temps et de l'argent.

Gardez simplement à l'esprit que la mise en cache côté serveur n'est pas adaptée si vous avez trop de données dynamiques.

Vous devez cependant être prudent avec la mise en cache : si elle n'est pas mise en œuvre correctement, l'utilisateur peut voir le même ancien contenu à chaque visite du site.

### Compression Gzip

La compression Gzip est l'une des recommandations les plus courantes du test de vitesse Pingdom.

Gzip est une méthode de compression de fichiers pour une livraison plus rapide à vos utilisateurs. Elle est activée par défaut par de nombreux fournisseurs d'hébergement.

Si vous utilisez l'hébergement cloud, alors vous êtes seul. Mais l'activation de la compression Gzip non seulement diminuera la vitesse de chargement de votre site web, mais réduira également l'utilisation de la bande passante des serveurs.

Voici le code à ajouter dans le fichier de configuration pour activer la compression Gzip sur un serveur Nginx.

```nginx
gzip on;
gzip_disable "msie6";
gzip_vary on;
gzip_proxied any;
gzip_comp_level 6;
gzip_buffers 16 8k;
gzip_http_version 1.1;
gzip_types application/javascript application/rss+xml application/vnd.ms-fontobject application/x-font application/x-font-opentype application/x-font-otf application/x-font-truetype application/x-font-ttf application/x-javascript application/xhtml+xml application/xml font/opentype font/otf font/ttf image/svg+xml image/x-icon text/css text/javascript text/plain text/xml;
```

Voici le code à ajouter dans le fichier `.htaccess` pour activer Gzip sur un serveur Apache.

```apacheconf
<IfModule mod_deflate.c>
    AddOutputFilterByType DEFLATE application/javascript
    AddOutputFilterByType DEFLATE application/rss+xml
    AddOutputFilterByType DEFLATE application/vnd.ms-fontobject
    AddOutputFilterByType DEFLATE application/x-font
    AddOutputFilterByType DEFLATE application/x-font-opentype
    AddOutputFilterByType DEFLATE application/x-font-otf
    AddOutputFilterByType DEFLATE application/x-font-truetype
    AddOutputFilterByType DEFLATE application/x-font-ttf
    AddOutputFilterByType DEFLATE application/x-javascript
    AddOutputFilterByType DEFLATE application/xhtml+xml
    AddOutputFilterByType DEFLATE application/xml
    AddOutputFilterByType DEFLATE font/opentype
    AddOutputFilterByType DEFLATE font/otf
    AddOutputFilterByType DEFLATE font/ttf
    AddOutputFilterByType DEFLATE image/svg+xml
    AddOutputFilterByType DEFLATE image/x-icon
    AddOutputFilterByType DEFLATE text/css
    AddOutputFilterByType DEFLATE text/javascript
    AddOutputFilterByType DEFLATE text/plain
    AddOutputFilterByType DEFLATE text/xml
</IfModule>
```

[Source](https://www.keycdn.com/support/enable-gzip-compression).

### AMP pour mobile

J'ai lu une [étude de cas](https://kinsta.com/blog/disable-google-amp/) qui indique que AMP peut affecter vos ventes. Mais comme je l'ai dit plus tôt dans l'article, vous n'avez pas besoin de mettre en œuvre toutes les étapes de cet article pour rendre votre site web plus rapide. Choisissez judicieusement.

Si vous gérez une plateforme de publication comme un simple blog, alors vous devez opter pour AMP car cela ne vous apportera que des avantages.

AMP prend également en charge les publicités, donc cela aura le moins d'effet sur vos revenus, mais les avantages sont grands. AMP a la vitesse de chargement la plus rapide sur les téléphones mobiles.

Voici un code AMP très basique. Vous pouvez consulter [ici](https://amp.dev/documentation/guides-and-tutorials/start/create/) pour un guide complet et les meilleures pratiques pour créer une version AMP de votre site web.

```html
<!doctype html>
<html amp lang="en">
  <head>
    <meta charset="utf-8">
    <script async src="https://cdn.ampproject.org/v0.js"></script>
    <title>Hello, AMPs</title>
    <link rel="canonical" href="https://amp.dev/documentation/guides-and-tutorials/start/create/basic_markup/">
    <meta name="viewport" content="width=device-width,minimum-scale=1,initial-scale=1">
    <script type="application/ld+json">
      {
        "@context": "http://schema.org",
        "@type": "NewsArticle",
        "headline": "Open-source framework for publishing content",
        "datePublished": "2015-10-07T12:02:41Z",
        "image": [
          "logo.jpg"
        ]
      }
    </script>
    <style amp-boilerplate>body{-webkit-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-moz-animation:-amp-start 8s steps(1,end) 0s 1 normal both;-ms-animation:-amp-start 8s steps(1,end) 0s 1 normal both;animation:-amp-start 8s steps(1,end) 0s 1 normal both}@-webkit-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-moz-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-ms-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@-o-keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}@keyframes -amp-start{from{visibility:hidden}to{visibility:visible}}</style><noscript><style amp-boilerplate>body{-webkit-animation:none;-moz-animation:none;-ms-animation:none;animation:none}</style></noscript>
  </head>
  <body>
    <h1>Welcome to the mobile web</h1>
  </body>
</html>
```

### Optimisations spécifiques à WordPress

#### Moins de plugins

Les plugins sont la force de WordPress. Ou je devrais dire que les plugins sont le fléau de WordPress.

Les deux dépendent du nombre et de la qualité des plugins que vous utilisez sur votre site.

Le nombre de plugins affecte directement la vitesse de chargement de votre site web. Je recommande toujours d'utiliser uniquement les plugins nécessaires et d'éviter les autres.

#### Un thème minimal fera le travail

Permettez-moi de vous dire que votre "thème WordPress populaire" a un support intégré pour la plupart des plugins WordPress populaires que vous n'utiliserez peut-être jamais.

Oui, c'est la vérité. Ils ont un grand nombre de clients à cibler, donc ils ont construit une solution tout-en-un pour tous (vraiment ?).

Vous devriez opter pour un thème minimal qui est dédié à un but particulier.

S'il n'y a pas de thème qui convient le mieux, alors il est bon de créer votre propre thème à partir de zéro. Ce sera un processus chronophage, mais il chargera les actifs spécifiques à vos besoins et aura définitivement de grands avantages en termes de vitesse.

#### Utilisez le plugin Autoptimize

C'est un plugin simple qui résout la plupart des problèmes avec les feuilles de style et les fichiers JavaScript. J'ai obtenu +20 points dans Google Speed Insights juste après avoir installé ce plugin.

Il met en cache, diffère et minifie automatiquement les fichiers CSS et JavaScript, ce qui améliore la vitesse de chargement des pages.

#### Avez-vous vraiment besoin de WordPress ?

Je sais que ce sujet ne devrait pas être ici sous les optimisations WordPress. Mais il est important de se demander si vous avez vraiment besoin de WordPress.

J'aime WordPress car il est mature et idéal pour les débutants. Mais parfois, je pense qu'il est trop lourd pour des tâches simples.

WordPress est vraiment lourd dans son cœur car il a des fonctionnalités pour tout le monde. Que vous vouliez utiliser ces fonctionnalités ou non, elles sont là, en cours d'exécution et consomment des ressources serveur.

Si vous avez besoin d'une plateforme de publication simple sans intégrations complexes, alors ces options sont de bonnes alternatives.

* Ghost CMS (freeCodeCamp News l'utilise)
* Netlify CMS (De plus en plus populaire avec les générateurs de sites statiques).
* Gatsby, Hugo, Jekyll (Générateurs de sites statiques)

Je voulais inclure Strapi dans la liste, mais il manque de tutoriels et de démonstrations. Il trouvera sa place dans le développement web futur à mesure que sa communauté grandira.

Pour démontrer l'effet, voici une capture d'écran de l'indice de vitesse sur mon site actuel sur WordPress et une version migrée sur Ghost CMS avec un thème personnalisé.

![Image](https://www.freecodecamp.org/news/content/images/2020/05/Wordpress-Neve-theme-performance.png)
_Performance du thème WordPress avec 3 plugins supplémentaires installés uniquement pour la vitesse._

![Image](https://www.freecodecamp.org/news/content/images/2020/05/ghost-cms-custom-theme-performance.png)
_Thème personnalisé Ghost CMS_

Je ne suis en aucun cas partial. Il y a des cas d'utilisation pour chacun. WordPress peut gérer des choses complexes facilement tandis que Ghost gagne en simplicité et les générateurs de sites statiques gagnent en vitesse.

Vous pouvez choisir les alternatives à WordPress en fonction de vos besoins.

## En fin de compte : ne sur-optimisez pas

L'optimisation est bonne, mais vous ne devriez pas essayer d'être strict avec toutes les étapes. Comme je l'ai mentionné plus tôt, il y a une forte probabilité que certaines étapes puissent casser votre site et mener à des sessions de débogage difficiles.

Écrivez toutes les étapes et décidez ensuite si chaque étape convient à votre site web ou non.

Encore une fois, en fin de compte, la sur-optimisation est généralement mauvaise. La vitesse est vraiment nécessaire, mais d'autre part, l'expérience utilisateur (UI et UX) compte également beaucoup.

Un bon site web maintient une vitesse incroyable avec une excellente UI et UX.

> Je peux vous envoyer plus d'articles comme celui-ci avec notre [Newsletter Hebdomadaire](https://holycoders.com/newsletter/).