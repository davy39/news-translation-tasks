---
title: Comment comprendre Google Analytics et le trafic de votre site web
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-09-04T14:32:00.000Z'
originalURL: https://freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website
coverImage: https://www.freecodecamp.org/news/content/images/2019/09/making-sense-of-google-analytics.jpg
tags:
- name: analytics
  slug: analytics
- name: Google Analytics
  slug: google-analytics
- name: '#reporting'
  slug: reporting
- name: SEO
  slug: seo
- name: user experience
  slug: user-experience
- name: website development,
  slug: website-development
seo_title: Comment comprendre Google Analytics et le trafic de votre site web
seo_desc: 'Google Analytics is a powerful web service that gives you insights into
  your website. But exactly can it help you?

  I’m going to cover a few things here. If you’re already familiar with the basics,
  feel free to skip around:


  What is Google Analytics? ...'
---

[Google Analytics](https://marketingplatform.google.com/about/analytics/) est un puissant service web qui vous donne des informations sur votre site web. Mais comment peut-il vous aider ?

Je vais aborder quelques points ici. Si vous êtes déjà familier avec les bases, n'hésitez pas à sauter certaines sections :

* [Qu'est-ce que Google Analytics ?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#questce-que-google-analytics) (Un aperçu rapide)
* [D'accord, mais par où commencer ?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#daccord-mais-par-ou-commencer) (Guide d'installation rapide)
* [Quels sont quelques insights rapides ?](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#quels-sont-quelques-insights-rapides) (Rapports de base prêts à l'emploi)
* [Bonus : Insights avancés](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/#bonus-insights-avances) (Dimensions personnalisées)

Commençons donc par le début.

## **Qu'est-ce que Google Analytics ?**

> Google Analytics vous donne les outils dont vous avez besoin pour mieux comprendre vos clients. Vous pouvez ensuite utiliser ces insights commerciaux pour agir, comme améliorer votre site web, créer des listes d'audience sur mesure, et plus encore. - [Documentation officielle de Google](https://marketingplatform.google.com/about/analytics/)

Plus simplement, Google Analytics (GA) est un service d'analyse web fourni par Google sur la [Google Marketing Platform](https://marketingplatform.google.com/about/). Il vous permet de suivre et de mesurer le trafic de votre site web avec des insights puissants et des rapports.

GA peut fonctionner de plusieurs manières, mais la plus courante est [d'utiliser un extrait de code JavaScript rapide](https://support.google.com/analytics/answer/1008080?hl=en) qui est placé sur chaque page de votre site web (généralement dans le `<head>`).

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-37.png)
_Google Analytics vous permet de mesurer l'interaction des utilisateurs avec les sites web._

La version de base de Google Analytics est gratuite. Vous avez la possibilité de passer à la suite 360, qui ouvrira certaines limites de fonctionnalités, mais la plupart d'entre vous n'en ont probablement pas besoin, car elle est plus adaptée aux sites web à fort trafic.

### **Pourquoi ai-je besoin de Google Analytics ?**

Vous n'en avez pas besoin. Mais vous pouvez obtenir une quantité incroyable d'informations à partir de GA, même avec une configuration de base prête à l'emploi.

GA est utile si vous êtes un développeur essayant d'obtenir plus de trafic sur votre blog, ou une entreprise essayant d'optimiser votre tunnel de vente.

GA vous aide à répondre à des questions simples comme :

* D'où vient mon trafic ?
* Quelles pages reçoivent le plus de trafic ?
* Quels sont les appareils les plus populaires que les gens utilisent pour visiter mon site ?

Non seulement cela peut vous aider à prendre des décisions plus éclairées avec votre site web. Cela peut également vous aider à révéler des préoccupations en matière d'expérience utilisateur, ou à économiser de l'argent en surveillant les tendances de trafic et les interactions des utilisateurs.

## **D'accord, mais par où commencer ?**

Google rend cela assez facile pour tout développeur de se lancer et de commencer. Le seul vrai prérequis est que vous configuriez un compte. Google lui-même offre un excellent [guide étape par étape et constamment mis à jour](https://support.google.com/analytics/answer/1008015?hl=en), donc je vais les laisser faire.

### **Obtenir le tag sur votre page**

Une fois que vous êtes connecté au tableau de bord Google Analytics, allez dans la section Admin, que vous pouvez trouver sur le côté gauche de la page :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-42.png)
_Lien Admin dans le tableau de bord Google Analytics_

Une fois dans la section admin, vous pouvez naviguer vers Tracking Info puis Tracking code sous la propriété que vous souhaitez suivre.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-43.png)
_Lien du code de suivi dans l'Admin Google Analytics_

Enfin, vous pouvez trouver l'extrait de code JavaScript que vous pouvez placer dans le head de votre site web. N'oubliez pas, cela doit être sur TOUTES les pages.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-44.png)
_Extrait de code de suivi Google Analytics_

### **Laissez le trafic circuler**

À partir de là, vous devez simplement lui donner du temps. Google Analytics n'aura pas de données historiques, il n'aura que le nouveau trafic qui a atteint votre page une fois l'extrait installé.

Vous pouvez vérifier qu'il fonctionne en visitant le rapport en temps réel et en accédant à la page dans un autre onglet ou en voyant vos visiteurs accéder à la page.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-45.png)
_Rapport en temps réel de Google Analytics_

### **Plus de paramètres, plus de configuration**

Google Analytics est une machine complexe et peut faire beaucoup. Commencez lentement et essayez de comprendre ce qui se passe avant de vous précipiter pour activer chaque interrupteur.

Une fois que vous êtes à l'aise, il existe de nombreux [guides excellents](https://www.google.com/search?q=google+analytics+tips) pour les débutants et les utilisateurs avancés afin de libérer tout le pouvoir de vos capacités de reporting.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/super-saiyan.gif)
_Goku devenant Super Saiyan_

## **Quels sont quelques insights rapides ?**

Super, donc vous avez installé GA, vous voyez votre trafic, et vous êtes prêt à commencer à regarder vos rapports, mais par où commencer ?

### **Quelles pages reçoivent le plus de trafic ?**

Commençons par quelque chose de simple. Quelles pages de mon site web reçoivent le plus de trafic ? Pour le découvrir, nous voudrons consulter l'Aperçu du comportement, que nous pouvons trouver en visitant Comportement puis Aperçu.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-46.png)
_Trouver la page la plus visitée dans le rapport Aperçu du comportement de Google Analytics_

Ci-dessus, nous regardons le mois complet d'août, que vous pouvez changer avec le sélecteur de date en haut à droite du rapport. Nous pouvons voir que, globalement, nous avons eu 3 853 265 pages vues au total et 121 187 d'entre elles étaient pour /news, la page d'accueil de freeCodeCamp News, qui était notre page la plus populaire du mois.

### **D'où vient mon trafic ?**

Une question courante est : « d'où viennent les gens ? » Comment les gens trouvent-ils réellement mon site web ? Cela se fait en deux parties, commençons par le trafic global.

Un bon moyen de commencer est de trouver la page Aperçu de l'acquisition. Vous pouvez y naviguer en sélectionnant Acquisition puis Aperçu.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-47.png)
_Trouver la principale source de trafic dans le rapport Aperçu de l'acquisition de Google Analytics_

Comme montré ci-dessus, la majorité du trafic provient de recherches organiques sur Google, un peu plus de 75 % en fait. C'est un bon [SEO](https://moz.com/beginners-guide-to-seo) !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-48.png)
_Mouvement exceptionnel_

Mais que faire si nous voulions voir comment les gens arrivent à un article particulier ? Cela implique un peu plus de travail, mais plongeons-nous dedans.

Retournez à Comportement dans la barre latérale, puis Contenu du site, et enfin Pages de destination. Une fois là, vous pouvez utiliser la recherche pour trouver votre article comme montré ci-dessous et le sélectionner.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-49.png)
_Recherche d'une page dans le rapport Pages de destination de Google Analytics_

Après avoir trouvé votre article, nous allons ajouter une dimension secondaire. En particulier, nous voudrons trouver et sélectionner « Source / Support » dans le menu déroulant de la dimension secondaire.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-50.png)
_Ajout d'une dimension secondaire dans le rapport Pages de destination de Google Analytics_

Enfin, nous aurons une idée de l'endroit d'où viennent les gens pour visiter notre article.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-51.png)
_Trouver la principale Source / Support dans le rapport Pages de destination de Google Analytics_

Il semble que cela suive la tendance du bon SEO organique. Cependant, vous remarquerez que nous avons « (direct) / (none) » comme deuxième source/support la plus élevée.

Malheureusement, ce n'est pas toujours aussi simple. Et si Google Analytics ne peut pas déterminer d'où vient l'utilisateur, il le marquera comme « (direct) / (none) ». [Bien que cela soit résolvable](https://moz.com/blog/guide-to-direct-traffic-google-analytics), et signifie parfois réellement quelque chose, nous pouvons voir que la majorité provient de simples recherches sur Google lui-même.

### **Quels sont les appareils les plus populaires que les gens utilisent pour visiter mon site ?**

Comprendre quels appareils vos visiteurs utilisent est un outil incroyablement utile pour optimiser l'expérience utilisateur, ainsi que pour maximiser les revenus potentiels en vous assurant que votre site fonctionne.

Dans un monde parfait, votre site web fonctionnerait dans tous les navigateurs. Mais nous pouvons peut-être exclure en toute sécurité certains navigateurs plus anciens.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-52.png)
_Internet Explorer derrière un arbre_

Pour commencer, trouvez votre chemin vers Audience puis Aperçu. Une fois là, sélectionnez Navigateurs dans la liste comme montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-53.png)
_Trouver le navigateur principal dans le rapport d'acquisition de Google Analytics_

Nous pouvons voir que, heureusement, nos principaux navigateurs sont dominés par des navigateurs modernes, avec Chrome représentant 76,42 %.

Mais attendez, Internet Explorer représente 1,06 % ou 22 499, ce qui n'est pas négligeable. Alors creusons un peu plus en cliquant sur Internet Explorer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-54.png)
_Trouver le trafic pour les versions d'Internet Explorer dans le rapport Navigateurs de Google Analytics_

Ouf, je pense que nous sommes en sécurité. Maintenant, nous pouvons voir combien de personnes visitent chaque version d'Internet Explorer et, heureusement, presque 99 % de ce trafic provient d'IE9 ou supérieur. Bien que nous devrions être aussi inclusifs que possible, cela peut nous aider à déterminer les priorités et à prendre des décisions sur [les versions de navigateurs à supporter officiellement](https://caniuse.com/).

Parlons sérieusement : 5 personnes sur IE5 ? ?

## **Bonus : Insights avancés**

Dès la sortie de la boîte, Google Analytics est puissant, mais avec un peu de personnalisation et une intégration plus profonde avec vos données web, vous pouvez donner à votre tableau de bord d'analyse des superpouvoirs supplémentaires.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/darkwing-duck-lets-get-dangerous.gif)
_Darkwing Duck : Passons à l'action_

## **Dimensions personnalisées**

Les [Dimensions personnalisées](https://support.google.com/analytics/answer/2709829?hl=en) sont ce que Google spécifie comme des « données non standard ». En réalité, ce sont simplement des points de données supplémentaires que nous pouvons configurer pour mieux comprendre ce qui rend notre site web unique.

Pour les besoins de cet article (peut-être un autre plus tard), je ne vais pas expliquer comment ajouter des Dimensions personnalisées, mais Google fournit un [excellent guide pour une compréhension approfondie](https://support.google.com/analytics/answer/2709828?hl=en) et un [guide pour les développeurs](https://developers.google.com/analytics/devguides/collection/analyticsjs/custom-dims-mets). Ce que je vais aborder ici, c'est comment explorer nos rapports une fois que certaines Dimensions personnalisées sont déjà configurées.

### **Quelles sont nos Dimensions personnalisées ?**

Pour commencer, nous allons parler de 2 Dimensions personnalisées spécifiques : Auteur et Catégorie de page.

L'Auteur est ce à quoi cela ressemble, c'est la personne qui a écrit l'article. La Catégorie de page dans notre cas est la catégorie principale, de premier niveau, qui représente l'article.

Sur freeCodeCamp News, vous pouvez spécifier autant de catégories que vous le souhaitez (faites-le de manière responsable), mais la première de la liste est considérée comme votre catégorie « principale » et est utilisée lorsque vous voyez votre article dans les vues de liste telles que la page d'accueil.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-55.png)
_Article sur la page d'accueil de freeCodeCamp News_

### **Que pouvons-nous faire avec celles-ci ?**

Le plus grand avantage est que lorsque nous les configurons, nous les attribuons à une vue de page. Une fois que cette vue de page est collectée par Google Analytics, nous pouvons l'utiliser pour effectuer des recherches, ce qui est vraiment ce qui la rend puissante. Commençons par l'Auteur.

### **Trouver tous les articles d'un Auteur spécifique**

Si nous voulions rechercher tout article écrit par Quincy Larson, nous voudrions naviguer vers **Comportement**, puis **Contenu du site**, et enfin **Toutes les pages**.

Une fois là, nous voudrions ajouter une **Dimension secondaire**, similaire à lorsque nous avons ajouté Source / Support, mais maintenant nous voudrions rechercher et sélectionner **Auteur**, que vous trouverez également imbriqué sous l'en-tête Dimensions personnalisées de ce menu déroulant.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-56.png)
_Sélection de l'Auteur comme dimension secondaire dans le rapport Comportement de Google Analytics_

À partir de là, nous voudrions sélectionner Avancé à droite (surligné ci-dessous), ajouter le nom de notre auteur, et enfin cliquer sur le bouton Appliquer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-57.png)
_Recherche d'un Auteur dans la recherche avancée du rapport Comportement de Google Analytics_

Après avoir cliqué sur Appliquer, nous avons maintenant toutes les statistiques dont nous pourrions rêver pour les articles écrits par notre auteur, Quincy Larson.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-58.png)
_Tous les articles d'un Auteur dans le rapport Comportement de Google Analytics_

### Vous pouvez également simplement taper une requête dans la barre de recherche de Google Analytics.

Google Analytics dispose d'une barre de recherche en haut, et vous pouvez simplement taper des requêtes en langage naturel comme celle-ci :

![Image](https://www.freecodecamp.org/news/content/images/2019/09/Analytics.png)
_Les résultats d'une requête pour « articles de quincy larson au cours des 30 derniers jours » montrent le nombre de vues de chaque article de Quincy au cours des 30 derniers jours._

### **Quelles catégories performantes sont les meilleures ?**

Cela est un peu plus compliqué. Il y a beaucoup de questions auxquelles nous pourrions répondre avec les rapports de base comme nous l'avons fait avec l'Auteur, comme « parmi tous les articles JavaScript, lequel a le plus de trafic ? », mais peut-être voulons-nous savoir généralement quelle catégorie est la plus populaire sur le site.

Pour cela, nous devons nous salir les mains avec les Rapports personnalisés. Cela est trop avancé pour essayer de le traiter dans cet article, mais [Google fait un excellent travail en le détaillant](https://support.google.com/analytics/answer/1151300?hl=en).

Pour l'instant, je vous ai rendu service et j'ai configuré un rapport que vous pouvez facilement importer dans votre compte et utiliser immédiatement. Donc, la première chose à faire est d'importer le rapport : [https://analytics.google.com/analytics/web/template?uid=4fHol2S_TZqcQACAwfcmfg](https://analytics.google.com/analytics/web/template?uid=4fHol2S_TZqcQACAwfcmfg)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-59.png)
_Importation d'un Rapport personnalisé dans Google Analytics_

Ici, vous devriez voir un écran comme ci-dessus qui nous demande deux choses : où devons-nous appliquer le rapport et comment voulons-nous l'appeler ? Si vous êtes un auteur de freecodecamp.org avec accès à GA et que vous souhaitez le consulter, vous sélectionneriez la vue Toutes les données du site web sous la propriété freeCodeCamp News.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-60.png)
_Sélection d'une Propriété et d'une Vue lors de l'importation d'un Rapport personnalisé dans Google Analytics_

Une fois sélectionné, nommez le rapport comme vous le souhaitez, par exemple « Top Catégories principales », et cliquez sur Créer.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/image-61.png)
_Rapport personnalisé montrant les principales Catégories principales dans Google Analytics_

Une fois terminé, vous atterrirez sur le rapport personnalisé nouvellement importé où vous pourrez immédiatement voir les catégories les plus populaires sur le site, qui pour le mois d'août est JavaScript !

## **Résumé**

C'était beaucoup !

![Image](https://www.freecodecamp.org/news/content/images/2019/09/galaxy-quest-alan-rickman-tired.gif)
_Alan Rickman dans Galaxy Quest s'enfonçant dans son fauteuil_

Mais ce n'est que la pointe de l'iceberg des données. Même avec ce qui précède, vous pouvez voir qu'il se passe beaucoup de choses et qu'il y a beaucoup de configuration à faire pour tirer le meilleur parti de Google Analytics pour vos besoins spécifiques.

Si cela vous intéresse, je vous encourage à faire quelques recherches par vous-même, [ajouter une nouvelle vue](https://support.google.com/analytics/answer/1009714?hl=en) (en particulier [une Vue de test](https://www.e-nor.com/blog/google-analytics/best-practices-views-google-analytics) pour jouer avec), et vous salir les mains en explorant les différents rapports. Sinon, restez à l'affût pour plus de mes articles sur GA couvrant l'installation avancée et des insights plus approfondis.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? fe0f Abonnez-vous à ma chaîne YouTube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Inscrivez-vous à ma newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2019/09/making-sense-of-google-analytics-and-the-traffic-to-your-website](https://www.colbyfayock.com/2019/09/making-sense-of-google-analytics-and-the-traffic-to-your-website)_