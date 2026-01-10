---
title: Comment utiliser Google Tag Manager pour maintenir Google Analytics et d'autres
  balises marketing
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2019-11-20T16:04:05.000Z'
originalURL: https://freecodecamp.org/news/how-to-use-google-tag-manager-to-maintain-google-analytics-and-other-marketing-tags
coverImage: https://www.freecodecamp.org/news/content/images/2019/11/take-control-of-your-marketing-tags.jpg
tags:
- name: analytics
  slug: analytics
- name: '#content marketing'
  slug: content-marketing
- name: 'Digital Marketing '
  slug: digital-marketing
- name: front end
  slug: front-end
- name: frontend
  slug: frontend
- name: Google
  slug: google
- name: Google Analytics
  slug: google-analytics
- name: google tag manager
  slug: google-tag-manager
- name: marketing
  slug: marketing
- name: '#reporting'
  slug: reporting
- name: SEO
  slug: seo
- name: website development,
  slug: website-development
seo_title: Comment utiliser Google Tag Manager pour maintenir Google Analytics et
  d'autres balises marketing
seo_desc: Managing code snippets and pixels on your website or app to measure traffic
  can be a little bit stressful, especially if you have a marketing team that constantly
  needs to make changes. Luckily, there are tools out there like Google Tag Manager
  that ...
---

Gérer des extraits de code et des pixels sur votre site web ou votre application pour mesurer le trafic peut être un peu stressant, surtout si vous avez une équipe marketing qui doit constamment apporter des modifications. Heureusement, il existe des outils comme Google Tag Manager qui faciliteront leur gestion.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/giphy.gif)
_Sandy wrangling_

## **Qu'est-ce que Google Tag Manager ?**

Si vous avez déjà travaillé avec un logiciel d'analyse ou si vous avez déjà travaillé avec une équipe marketing, vous avez probablement entendu le mot pixel. Un pixel est littéralement ce à quoi il ressemble : une image de 1x1 qui envoie des informations à un serveur via une requête d'image.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-analytics-pixel-request.jpg)
_Requête de pixel Google Analytics_

Bien que les pixels soient encore courants, de nombreuses équipes sont passées à de petits extraits de code JavaScript qui se trouvent juste à côté du reste de votre HTML. Ils permettent à des logiciels comme Google Analytics d'exécuter leurs propres scripts sur votre page, parfois même avec un pixel de secours, au cas où un navigateur n'exécuterait pas JavaScript.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/crazy-egg-tracking-snippet.jpg)
_Extrait Crazy Egg_

Ces pixels et extraits fonctionnent très bien. Mais lorsque vous avez affaire à plusieurs d'entre eux et qu'ils utilisent tous les mêmes données, cela peut sembler ajouter à un désordre ingérable d'extraits de code à usage unique qui ne semblent jamais être au bon endroit.

Google Tag Manager, ou GTM, est une solution logicielle pour gérer ces pixels et extraits pour vous. Pour commencer, GTM fonctionne à peu près comme n'importe quel autre extrait de code, car c'est un extrait de code lui-même. Mais là où il brille, c'est que vous pouvez gérer le reste de ces pixels et extraits ainsi que le flux de données à l'intérieur de GTM, le laissant être le seul extrait à gérer dans votre code.

## **Pourquoi devrais-je l'utiliser ?**

### **Moins de modifications de code, moins de déploiements**

La plupart du temps, si vous gérez ces extraits dans votre code, chaque modification nécessitera une autre demande de fusion et un autre déploiement pour mettre les changements en ligne. Non seulement cela ajoute plus de risques, car vous devez apporter une autre modification au code, mais cela représente également du temps supplémentaire passé à gérer votre pipeline de déploiement et à vous assurer que tout fonctionne comme il se doit.

GTM vous permet de sortir de ce flux, vous offrant plus de flexibilité pour apporter des modifications qui pourraient donner un aperçu nécessaire pour corriger certaines erreurs d'interface utilisateur ou ajouter quelques dollars à la ligne de fond.

### **Flux de données plus gérable**

Gérer toutes les différentes variables dans votre application, en vous assurant qu'elles sont toutes disponibles au bon endroit, et en suivant les changements pour éviter de tout casser peut s'avérer difficile. Cela rend également votre code plus fragile et sujet à des erreurs.

Google Tag Manager utilise ce qu'ils appellent un `dataLayer`, qui fonctionne essentiellement comme un tableau d'événements auxquels il écoute. Cela vous permet de pousser ou de semer de nouvelles données pour les rendre disponibles dans GTM lui-même. Et cela signifie que vous canalisez toutes vos variables vers un seul endroit dans le code. Cela permet à la personne qui gère GTM de faire le reste – elle peut utiliser ces données en toute tranquillité, sachant que votre flux de données ne se cassera pas après avoir oublié de mettre à jour 1 des 10 emplacements.

### **Capacité à donner aux marketeurs un peu plus d'accès**

C'est une opportunité de libérer du temps en laissant l'équipe marketing gérer elle-même les modifications des balises plutôt que d'être l'intermédiaire. Peut-être ont-ils besoin d'ajuster l'ID de votre logiciel d'analyse ou peut-être veulent-ils ajouter [Crazy Egg](https://www.crazyegg.com/). Avec les bonnes permissions (expliquées plus tard), ils peuvent faire tout le travail et vous envoyer les modifications pour révision avant de les publier.

## **Comment cela se rapporte-t-il à Google Analytics ?**

Il n'y a pas de relation directe. Mais avec Google Analytics, GTM est un autre outil de la plateforme Google Marketing et vous donne la capacité immédiate de gérer plus facilement votre installation Google Analytics. GA est livré avec des balises préconstruites dans GTM qui le rendent facile à configurer.

## **Pour quoi d'autre puis-je utiliser cela ?**

Google Analytics n'est qu'un des nombreux extraits de code pour lesquels cela peut être utilisé. Idéalement, vous n'allez pas écrire tout votre site ici. Mais vous avez la possibilité de faire à peu près ce que vous voulez sur votre propre site tant que [Google ne le considère pas comme un malware](https://support.google.com/tagmanager/answer/6328489?hl=en).

D'autres cas d'utilisation incluent :

* Visualisation du trafic avec [Crazy Egg](https://www.crazyegg.com/) ou [Hot Jar](https://www.hotjar.com/)
* Pixels de conversion et de reciblage avec [Google Ads](https://ads.google.com/home/)
* Tests A/B avec [Google Optimize](https://marketingplatform.google.com/about/optimize/) ou [AB Tasty](https://www.abtasty.com/)
* Suivi des [erreurs côté client](https://support.google.com/tagmanager/answer/7679411?hl=en) (et leur journalisation)
* Gestion de la conformité GDPR

Il y en a beaucoup de préconfigurés comme les exemples ci-dessus, ce qui signifie que vous n'avez même pas besoin de toucher au code. Il suffit d'ajouter les ID ou les paramètres et c'est parti. Mais pour toute solution ou balise personnalisée dont vous avez besoin, vous pouvez toujours configurer le HTML manuellement.

## **Y a-t-il quelque chose que je dois savoir avant de me lancer ?**

Avant de vous lancer, familiarisons-nous avec quelques termes clés qui faciliteront cette expérience.

### **Balises**

Les balises dans GTM sont vos pixels ou extraits de code. Une balise inclut une seule instance d'un morceau de code contenu qui est utilisé pour une fonction.

_Exemple :_ votre extrait Google Analytics sera une balise et si vous ajoutez Crazy Egg, ce sera une autre balise.

### **Variables**

Une variable est un nom que vous donnez à une valeur prédéterminée ou dynamique. La variable peut être basée sur une variété de choses différentes, d'où le nom "variable". Mais elle fonctionnera comme un seul nom que vous pouvez donner et référencer et qui ne changera jamais lorsque vous l'utiliserez.

_Exemple :_ nous allons configurer votre ID Google Analytics comme une variable, ce qui signifie que vous utiliserez cette variable dans la balise GA elle-même. Si vous devez mettre à jour cet ID, vous n'aurez pas besoin de modifier la balise ou toute autre balise utilisant la variable – vous devrez uniquement mettre à jour la variable elle-même.

### **Déclencheurs**

Les déclencheurs sont l'événement ou l'action qui font que votre balise se déclenche ou se charge. Cela peut se produire de diverses manières, comme lorsque toutes les pages ou une page spécifique se charge, lorsque quelque chose est cliqué, ou lorsque vous avez un [événement complètement personnalisé](https://support.google.com/tagmanager/answer/7679219?hl=en) que vous déclenchez avec JavaScript.

_Exemple :_ lorsque nous configurons Google Analytics, notre déclencheur sera lorsque n'importe quelle page se charge.

### **Conteneur**

GTM vous permet de gérer plusieurs "conteneurs" ou groupes de balises au sein de votre organisation. Cela est utile lorsque vous avez une entreprise avec quelques propriétés de sites web différentes.

_Exemple :_ vous êtes une petite entreprise sous une société mère. La société mère souhaite maintenir une seule organisation, mais chaque petite entreprise obtient son propre conteneur, car elles ont leurs besoins individuels en matière de balises et d'extraits de code.

## **Comment me configurer ?**

### **Configurer votre compte**

La première chose à faire est de configurer votre compte. Après être arrivé sur la [page d'accueil du gestionnaire de balises](https://tagmanager.google.com/), vous voudrez probablement utiliser votre compte Google existant. Si vous êtes dans une organisation qui le configure pour l'organisation, vous souhaitez probablement utiliser votre email professionnel, sinon votre compte personnel fonctionne également.

Ensuite, créez un nouveau compte GTM :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-new-account.jpg)
_Nouveau compte Google Tag Manager_

Une fois là-bas, remplissez le formulaire de manière appropriée. Le nom du compte doit représenter le niveau supérieur de votre hiérarchie et le nom du conteneur doit représenter l'instance d'installation spécifique.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-new-account-container.jpg)
_Nouveau conteneur de compte Google Tag Manager_

En ce qui concerne la plateforme cible, choisissez celle qui a le plus de sens. Si c'est un site web ou une application web, le Web est le choix le plus judicieux ici.

### **Trouver et installer votre extrait**

Dès que vous acceptez les termes et cliquez sur créer, un extrait vous sera présenté dans une petite fenêtre modale. Vous devrez faire exactement ce qu'il dit et installer les extraits selon les instructions.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-install-snippet.jpg)
_Installer l'extrait Google Tag Manager_

Vous n'avez pas obtenu l'écran ou vous l'avez accidentellement quitté ? Vous pouvez retrouver votre extrait en naviguant vers Admin dans la barre de navigation supérieure, puis en cliquant sur Installer Google Tag Manager sous Conteneur à droite.

### **Tester que cela fonctionne**

Pour vous assurer que cela fonctionne, vérifions quelques choses :

* Nous avons créé notre compte
* Nous avons créé notre conteneur
* Nous avons installé les extraits Google Tag Manager sur notre page et les modifications sont en ligne

Une fois que toutes ces choses sont vraies, allez-y et cliquez sur le bouton Aperçu en haut à droite de la page.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-preview.jpg)
_Aperçu Google Tag Manager_

Si cela réussit, vous verrez maintenant une bannière orange en haut de la page indiquant que vous êtes en mode Aperçu :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-preview-mode.jpg)
_Mode aperçu Google Tag Manager_

Maintenant, rendez-vous sur le site web où vous avez installé GTM et vous devriez voir une bannière en bas de la page. Cela servira de débogueur pour travailler avec l'aperçu de GTM.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-debugger.jpg)
_Débogueur Google Tag Manager_

Vous devriez voir quelque chose de similaire, ce qui signifie que cela a fonctionné ! ?

Remarque : si vous avez un bloqueur de publicités activé, similaire à GA, vous devrez peut-être le désactiver sur la page où vous installez pour voir son fonctionnement.

## **Super, cela fonctionne, qu'en est-il de Google Analytics ?**

Maintenant que nous avons une installation de base de GTM qui fonctionne, configurons Google Analytics. D'abord, nous voulons faire quelques préparatifs, alors retournons au tableau de bord du gestionnaire de balises.

### **Créer une variable de paramètres**

Naviguez vers Variables dans la barre latérale de gauche, puis cliquez sur Nouveau à côté des Variables définies par l'utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-new-variable.jpg)
_Nouvelle variable Google Tag Manager_

Pour le nom, entrez "Paramètres GA" et sous Type de variable, cliquez et sélectionnez Paramètres Google Analytics. Entrez votre ID de suivi Google Analytics (ou ID de propriété) dans le champ approprié, et enfin cliquez sur Enregistrer, moment auquel vous aurez votre nouvelle variable de paramètres.

### **Créer une nouvelle balise GA**

Naviguez vers Balises dans la barre latérale de gauche, puis cliquez sur Nouveau à côté des Balises.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-new-tag.jpg)
_Nouvelle balise Google Tag Manager_

Pour le nom, entrez "GA - Toutes les pages". Sous Type de balise, cliquez et sélectionnez Google Analytics : Universal Analytics dans le panneau qui apparaît à droite.

Après avoir sélectionné le type de balise, sous Paramètres Google Analytics, sélectionnez votre variable de l'étape précédente, qui, si vous avez suivi, s'appellera "Paramètres GA".

Ensuite, cliquez au milieu de la boîte de déclenchement, ce qui devrait ouvrir une nouvelle interface utilisateur pour sélectionner un déclencheur.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-trigger.jpg)
_Déclencheur Google Tag Manager_

Sélectionnez Toutes les pages, qui devrait être le seul déclencheur là si vous êtes dans un nouveau compte. Cela vous ramènera à l'interface utilisateur Nouvelle balise avec votre nouveau déclencheur sélectionné.

Une fois ce qui précède terminé, cliquez sur Enregistrer en haut à droite de l'interface utilisateur, ce qui enregistrera et créera votre nouvelle balise Google Analytics.

### **Tester que GTM fonctionne**

Similaire à lorsque nous avons installé GTM au début, retournons à l'accueil de l'espace de travail en cliquant sur Aperçu dans la barre latérale de gauche. Ensuite, cliquez sur Aperçu en haut à droite.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-debugger-google-analytics.jpg)
_Débogueur Google Tag Manager avec Google Analytics_

Ouvrez votre page où GTM est installé et vous devriez voir à nouveau votre débogueur, mais cette fois avec la balise Google Analytics en cours de chargement.

## **Avons-nous terminé ?**

Pas tout à fait. Bien que nous ayons GA qui fonctionne, nous devons ajuster la configuration pour nous assurer que GA et GTM fonctionnent correctement ensemble.

### **Mettre à jour l'extrait de page**

Plongeons une dernière fois dans le code pour mettre à jour nos extraits Google Analytics et Google Tag Manager.

Le problème avec l'installation que nous avons configurée ici est que nous avons installé GA via les instructions GA et GA à l'intérieur de GTM. Cela signifie que nous avons installé GA deux fois. En pratique, GA peut envoyer 1 page vue depuis votre installation par défaut et une autre via GTM. Pour éviter cela, nous voulons supprimer la page vue de l'extrait GA par défaut.

Si vous avez une installation par défaut super basique, j'ai fait le travail pour vous et vous pouvez copier l'extrait ci-dessous. Remplacez `[YOUR GA PROPERTY ID]` par votre ID de propriété GA et `[YOUR GTM CONTAINER ID]` par votre ID de conteneur GTM, et échangez-le avec votre installation GA et GTM existante sur votre page.

```html
<script>
// Configurer une configuration initiale de dataLayer
window.dataLayer = window.dataLayer || [{
  "gaPropertyId": "[YOUR GA PROPERTY ID]"
}];

// Configurer gtag et votre ID GA
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', '[YOUR GA PROPERTY ID]');

// Extrait Google Tag Manager
(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl+'&gtm_cookies_win=x';f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer', '[YOUR GTM CONTAINER ID]');
</script>
```

Cela devrait REMPLACER votre extrait Google Analytics actuel si vous en avez un. Si vous n'en avez pas, cela devrait aller aussi loin que possible dans le haut de votre balise `<head>`, mais sous la balise méta `charset`.

Pour les utilisateurs plus avancés, assurez-vous simplement de ne pas envoyer de pages vues ou d'événements en double entre l'extrait de page et toute balise GTM que vous créez.

### **Tester que GA fonctionne**

Suivez les étapes ci-dessus pour vous assurer que GA apparaît avec le débogueur.

La dernière chose que vous voudrez faire est de vous assurer que votre installation fonctionne en utilisant [l'extension Tag Assistant de Google](https://chrome.google.com/webstore/detail/tag-assistant-by-google/kejbdjndbnbjgmefkgdddjlbokphdefk?hl=en). Une fois que vous avez installé l'extension, retournez sur votre page et cliquez sur Activer dans l'interface utilisateur de l'extension.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-assistant-record.jpg)
_Activer l'enregistrement Google Tag Assistant_

Actualisez la page et vous devriez voir 2 balises, GA et GTM.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-assistant-results.jpg)
_Résultats Google Tag Assistant_

Si vous remarquez, ma balise GA est bleue et la vôtre peut l'être aussi. Cliquez sur Google Analytics pour plus d'informations.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-assistant-implementation.jpg)
_Implémentation non standard Google Tag Assistant_

Comme vous pouvez le voir, nous avons une requête de page vue saine et une note qui dit Implémentation non standard (d'où le bleu). Cela est dû au fait que nous l'avons installé avec GTM au lieu de l'installation par défaut sur la page.

## **Publier et déployer !**

Nous y sommes ! La dernière étape consiste à publier votre conteneur et à rendre les modifications en ligne.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-submit.jpg)
_Soumettre la version Google Tag Manager_

Cliquez sur Soumettre dans l'interface utilisateur Aperçu, entrez un nom et une description.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/google-tag-manager-version-configuration.jpg)
_Configuration de la version Google Tag Manager_

Enfin, cliquez sur Publier et vos modifications seront en ligne sur votre site !

## **Que dois-je savoir d'autre ?**

Il y a beaucoup plus à discuter, mais ce sera pour un autre jour. Il existe de nombreuses ressources en ligne pour vous aider à démarrer avec l'ajout de vos propres nouvelles balises et l'exploration des capacités de Google Analytics, mais voici quelques points à garder à l'esprit avec GTM.

### **Permissions**

Vous ne voulez probablement pas que chaque marketeur de votre équipe de 1 000 personnes ait un accès de publication à votre conteneur GTM. Il est préférable d'avoir une ou quelques personnes responsables de la gestion du conteneur, de la révision et de la publication, tout en gardant tout le monde dans un rôle d'accès inférieur. Cela aidera à prévenir les modifications accidentelles ou les abus au sein d'une grande équipe.

### **Sécurité**

Les permissions sont votre première étape vers le maintien d'une installation sécurisée. Mais Google va plus loin et effectue certaines actions pour vous, comme la vérification des erreurs de code et [la recherche de logiciels malveillants](https://support.google.com/tagmanager/answer/6328489?hl=en). Bien que cela soit génial, il est toujours important de maintenir un cycle de révision actif des balises publiées, comme pour toute autre pièce de code, afin de s'assurer que l'intégrité et la santé du site restent intactes.

### **Conventions**

Je recommande vivement de commencer tôt avec des conventions de nommage et des meilleures pratiques lors de la configuration de vos balises, variables, déclencheurs et vraiment tout ce qui se trouve dans GTM. Les différentes façons de nommer les choses peuvent rapidement devenir ingérables, selon le nombre de personnes qui y travaillent. Cela rendra votre travail difficile à trouver, il est donc préférable de s'accorder avec l'équipe sur une convention à utiliser tôt et de bien démarrer.

### **Applications à page unique**

Cela ne tient pas compte de l'impact des applications à page unique sur une configuration GTM et GA. Le déclencheur que nous avons configuré ici se déclenchera lorsque n'importe quelle page se charge, ce qui est défini par un nouveau chargement de page par le navigateur. Les applications à page unique ne chargent pas réellement une nouvelle page – plutôt, le JavaScript dans l'application donne l'impression qu'une nouvelle page se charge, donc le déclencheur ici ne se déclenchera que pour la première page vue. Bien qu'il n'inclue pas d'informations directement utilisables dans GTM, la documentation GA contient [de bonnes informations](https://developers.google.com/analytics/devguides/collection/analyticsjs/single-page-applications) sur le suivi de ces types d'applications.

### **GDPR**

Bien que GTM seul ne viole pas (actuellement) le GDPR, vous devez toujours être conscient de l'impact de l'une des balises que vous utilisez sur votre conformité. Ce guide n'aborde pas ce sujet, alors assurez-vous de faire vos recherches.

### **Sortir du débogueur**

Bloqué ? Une façon est de supprimer vos cookies, mais vous devriez toujours pouvoir aller sur la page Aperçu de GTM et cliquer sur "Quitter le mode Aperçu" juste sous la bannière orange Mode Aperçu en haut de la page.

## **Quelle est la prochaine étape ?**

À partir de là, vous pouvez commencer à gérer vos balises et pixels via GTM, ce qui vous permet d'avoir une source unique de flux de données cohérent vers ces balises. Expérimentez et utilisez le débogueur pour jouer, car cela ouvre la porte à de nombreuses nouvelles façons de travailler avec le côté marketing.

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Follow me for more Javascript, UX, and other interesting things!" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Follow Me On Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? fe0f Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> 2709 fe0f Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>

_Publié à l'origine sur [https://www.colbyfayock.com/2019/11/how-to-use-google-tag-manager-to-maintain-google-analytics-and-other-marketing-tags](https://www.colbyfayock.com/2019/11/how-to-use-google-tag-manager-to-maintain-google-analytics-and-other-marketing-tags)_