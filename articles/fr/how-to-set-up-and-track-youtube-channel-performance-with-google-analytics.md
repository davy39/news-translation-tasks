---
title: Comment configurer et suivre les performances de votre chaîne YouTube avec
  Google Analytics
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-03-18T13:27:39.000Z'
originalURL: https://freecodecamp.org/news/how-to-set-up-and-track-youtube-channel-performance-with-google-analytics
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/youtube-analytics-1.jpg
tags:
- name: analytics
  slug: analytics
- name: '#content marketing'
  slug: content-marketing
- name: Google Analytics
  slug: google-analytics
- name: marketing
  slug: marketing
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
- name: youtube
  slug: youtube
seo_title: Comment configurer et suivre les performances de votre chaîne YouTube avec
  Google Analytics
seo_desc: 'Managing a YouTube channel is a lot of work. It includes content experimentation
  which can make or break your SEO effectiveness for your channel. How can we track
  our channel’s performance to see what works?


  Why is SEO important?

  How is SEO importan...'
---

Gérer une chaîne YouTube demande beaucoup de travail. Cela inclut l'expérimentation de contenu qui peut faire ou défaire l'efficacité de votre SEO pour votre chaîne. Comment pouvons-nous suivre les performances de notre chaîne pour voir ce qui fonctionne ?

* [Pourquoi le SEO est-il important ?](#heading-pourquoi-le-seo-est-il-important)
* [Pourquoi le SEO est-il important pour YouTube ?](#heading-pourquoi-le-seo-est-il-important-pour-youtube)
* [Et qu'est-ce que Google Analytics ?](#heading-et-quest-ce-que-google-analytics)
* [Comment connecter ma chaîne ?](#heading-comment-connecter-ma-chaine)
* [Que pourrai-je voir ?](#heading-que-pourrai-je-voir)
* [Que ne pourrai-je pas voir ?](#heading-que-ne-pourrai-je-pas-voir)
* [Que puis-je faire d'autre avec YouTube et Google Analytics ?](#heading-que-puis-je-faire-dautre-avec-youtube-et-google-analytics)

%[https://www.youtube.com/watch?v=P8wv4ylc_-s]

## Pourquoi le SEO est-il important ?

[Le SEO, ou Search Engine Optimization](https://moz.com/learn/seo/what-is-seo), est la pratique d'écrire et d'organiser du contenu de manière à ce que les moteurs de recherche comme Google puissent le parcourir et finalement comprendre de quoi parle votre site web ou votre chaîne YouTube.

En utilisant ces informations, Google et autres prennent des décisions avec leurs algorithmes pour déterminer quel contenu est de meilleure qualité, plus pertinent et plus susceptible de répondre à la question que vous cherchez sur leur moteur de recherche en premier lieu. Avec ces informations, les moteurs de recherche classent ce contenu et affichent leurs résultats ordonnés par ces classements.

## Pourquoi le SEO est-il important pour YouTube ?

Tout comme n'importe quel autre site web, YouTube est parcouru par Google et d'autres moteurs de recherche. De plus, YouTube a son propre moteur de recherche interne qui prendra ces mêmes éléments en considération lors de la décision de la manière d'afficher les résultats d'une recherche YouTube.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/searching-for-code-channels-on-youtube.jpg)
_Recherche de chaînes "code" sur YouTube_

Cela signifie que, selon la manière dont vous créez vos descriptions, gérez vos mots-clés ou nommez vos vidéos, cela pourrait avoir un impact sur la manière dont vos vidéos sont classées dans les résultats. Et cela peut avoir un impact sur le nombre de vues que vos vidéos obtiennent.

Cela s'applique également à votre chaîne. Vous avez des opportunités d'expérimenter l'efficacité à travers le contenu que vous mettez en avant, la description de votre chaîne et le nom de votre chaîne.

## Et qu'est-ce que Google Analytics ?

Google Analytics est un [outil d'analyse gratuit](https://analytics.google.com/analytics/web/) de Google qui vous permettra de mieux comprendre votre trafic. J'ai précédemment écrit sur [ce qu'est Google Analytics et comment vous pouvez le comprendre](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/) ce qui fournit une vue plus approfondie. Donc, si vous voulez en apprendre un peu plus avant de vous lancer, je vous recommande de commencer par là.

## Comment connecter ma chaîne ?

### Configuration d'un nouveau code de suivi

Pour commencer, nous aurons besoin d'un code de suivi de Google Analytics. Google dispose de ressources à jour sur la manière de procéder, donc je ne vais pas essayer de réexpliquer ici :

* [Configurer une nouvelle propriété](https://support.google.com/analytics/answer/1042508)
* [Obtenir votre ID de suivi](https://support.google.com/analytics/answer/1008080?hl=en)

Bien que certains disent que vous pouvez utiliser la propriété de votre site web et créer une vue filtrée, je recommande de commencer avec une propriété séparée. Ainsi, vous n'aurez pas à vous soucier des chevauchements de données ou de la configuration de filtres compliqués.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-tracking-id.jpg)
_ID de suivi dans Google Analytics_

Votre ID de suivi sera au format suivant : `UA-######-#`. Une fois que vous l'avez, nous sommes prêts à partir.

### Ajout de votre code de suivi à YouTube

Il y a quelques étapes que nous devons suivre pour trouver où nous pouvons configurer notre compte Google Analytics. Si vous voulez aller directement au bon endroit, vous pouvez visiter [youtube.com/advanced_settings](https://www.youtube.com/advanced_settings).

Pour prendre la route la plus longue, qui vous aidera également à vous familiariser un peu plus avec votre compte YouTube, rendez-vous d'abord dans la section **Paramètres** depuis votre page **YouTube Studio**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-studio-channel-settings.jpg)
_Trouver les Paramètres sur votre tableau de bord YouTube Studio_

Une fois sélectionné, trouvez le lien **Paramètres avancés de la chaîne** en visitant **Chaîne**, **Paramètres avancés**, puis en faisant défiler vers le bas.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-advanced-channel-settings.jpg)
_**Paramètres avancés de la chaîne** sur YouTube_

Enfin, faites défiler vers le bas de la page, trouvez le champ **ID de suivi de la propriété Google Analytics**, entrez l'ID de suivi que vous avez créé, et cliquez sur enregistrer.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-advanced-channel-settings-google-analytics-property-1.jpg)
_Configuration de l'ID de suivi de la propriété Google Analytics pour votre chaîne YouTube_

### Asseyez-vous et attendez

Google Analytics ne montrera le trafic de votre site web qu'à partir du moment où il a été configuré et dans le futur. Malheureusement, nous ne pouvons pas vérifier ce week-end où votre vidéo est devenue virale pour la première fois si vous n'aviez pas configuré Google Analytics à ce moment-là, mais au moins nous sommes préparés pour la prochaine fois !

![Image](https://www.freecodecamp.org/news/content/images/2020/03/friends-recline-chair.gif)
_Joey et Chandler inclinant leurs chaises_

Cela dit, c'est maintenant le moment de continuer à travailler dur sur votre chaîne puisque vous avez la capacité de suivre comment ce travail acharné porte ses fruits lorsque les gens visitent votre chaîne.

### Optionnel : Configuration de la recherche sur le site

La configuration de la fonctionnalité [Recherche sur le site de Google Analytics](https://support.google.com/analytics/answer/1012264?hl=en) nous offre un moyen facile de séparer l'utilisation de la recherche pour faciliter l'obtention d'informations sur la manière dont les gens recherchent notre chaîne.

Pour activer la recherche sur le site, nous voulons aller dans la section **Admin** de notre propriété Google Analytics, puis naviguer vers **Paramètres de la vue**. Une fois là, sous les **Paramètres de recherche sur le site** en bas, cliquez d'abord sur le bouton pour activer le **Suivi de la recherche sur le site**, puis tapez "query" dans le champ **Paramètre de requête**.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-site-search-tracking.jpg)
_**Suivi de la recherche sur le site** dans Google Analytics_

Optionnellement, bien que recommandé, vous pouvez choisir de supprimer les paramètres de requête de votre URL. Cela signifie que dans votre vue de contenu principal, vous verrez tout le trafic comme /search au lieu de nombreuses instances de /search?query=[keyword], ce qui peut être plus fastidieux à analyser.

_Note : avant de configurer cela, il est [généralement recommandé d'avoir plus d'une vue pour votre propriété](https://www.e-nor.com/blog/google-analytics/best-practices-views-google-analytics). Je recommande d'avoir au moins 2 vues, une vue de données brutes et une vue principale. Vous n'appliquerez la fonctionnalité de recherche sur le site qu'à votre vue principale. Cela aidera à s'assurer que vous pouvez toujours voir la vue de données brutes non filtrées si vous le souhaitez._

## Que pourrai-je voir ?

### Combien de personnes ont visité ma chaîne ?

La première chose que nous obtenons immédiatement avec nos nouvelles données lorsque nous ouvrons notre propriété Google Analytics est le nombre de personnes qui ont visité notre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-home.jpg)
_Accueil de Google Analytics_

Par défaut, cela concerne les 7 derniers jours, mais vous pouvez changer la plage de temps dans le coin inférieur gauche du panneau.

Ce que cela fournit également, c'est un aperçu rapide de la manière dont le nombre de personnes a changé depuis la période précédente (les 7 jours précédents dans cet exemple). Comme nous pouvons le voir ici, le nombre de personnes cette semaine a augmenté de 13,9 %, ce qui est une excellente nouvelle pour la chaîne YouTube de freeCodeCamp, prouvant que ce qu'ils ont fait fonctionne.

### Comment les gens trouvent-ils notre chaîne ?

Alors, comment pouvons-nous déterminer si les stratégies que nous utilisons (comme le SEO) pour amener les gens sur notre chaîne sont efficaces ? En analysant notre trafic de recherche organique.

En naviguant vers le rapport **Source/Moyen** en visitant **Acquisition**, **Tout le trafic**, puis **Source/Moyen**, nous pouvons voir quelles sources fournissent le plus de trafic à notre chaîne YouTube.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-source-medium-report.jpg)
_Rapport Source/Moyen dans Google Analytics_

En cliquant sur **google / organic**, nous pouvons également voir comment cela a changé au fil du temps.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-organic-google-referral-report.jpg)
_Rapport de trafic organique Google dans Google Analytics_

Bien qu'analyser une seule semaine ne soit pas le plus efficace, pouvoir dire comment votre trafic organique a changé sur plusieurs semaines pourra vous indiquer si votre stratégie fonctionne.

### Quels sites web et pages les gens visitent-ils ?

En naviguant vers le rapport **Référents** en allant dans **Acquisition**, **Tout le trafic**, puis **Référents**, nous pouvons voir que la plupart du trafic de référents pour [freeCodeCamp YouTube](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ) provient de [freeCodeCamp.org](https://www.freecodecamp.org/) lui-même.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-freecodecamp.org-referral-traffic.jpg)
_Trafic de référents montrant freecodecamp.org comme le principal référent dans Google Analytics_

Mais disons que nous voulons voir quelles pages ces référents proviennent. Nous pouvons le découvrir en cliquant sur le lien **freecodecamp.org** dans la vue ci-dessus où nous pouvons voir une ventilation complète des pages qui donnent le plus de trafic à la chaîne.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-referring-pages-from-freecodecamp.org.jpg)
_Pages de référents de freecodecamp.org sur Google Analytics_

### Que recherchent les gens sur ma chaîne ?

Après avoir configuré [Site Search](https://support.google.com/analytics/answer/1012264?hl=en) sur votre compte Google Analytics, vous pourrez obtenir de meilleures informations sur la manière dont les gens recherchent réellement sur votre site.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-search-terms.jpg)
_Rapport des termes de recherche dans Google Analytics_

Ici, nous pouvons voir quels mots-clés les gens veulent voir le plus, ce qui signifie que nous pouvons adapter notre contenu et nos futures vidéos à ces mots-clés, rendant notre chaîne plus efficace.

### Plus d'informations

Par défaut, vous obtiendrez beaucoup d'autres informations intéressantes de Google Analytics qui sont intégrées, comme l'endroit où vos visiteurs se trouvent physiquement et s'ils visitent sur un ordinateur de bureau ou un appareil mobile.

Pour en savoir plus sur ce que vous pouvez voir, consultez [mon article sur la compréhension de Google Analytics](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/).

## Que ne pourrai-je pas voir ?

Bien que les informations que vous découvrirez grâce à Google Analytics soient importantes, elles ne sont pas exhaustives. Il y a de nombreux points que vous devrez explorer dans l'outil Analytics propre à YouTube pour voir.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/youtube-studio-analytics-dashboard.jpg)
_Tableau de bord Analytics dans YouTube Studio_

### Analytics des vidéos

Les états et actions des vidéos ne seront pas visibles dans Google Analytics, ce qui inclut des choses comme Lecture, Pause et temps regardé.

Cependant, en utilisant l'onglet **Engagement** dans la section **Analytics** de [YouTube Studio](https://studio.youtube.com/), nous pouvons voir combien de temps les gens regardent nos vidéos et un graphique de la **Rétention du public**. Cela nous aidera à déterminer comment le contenu de nos vidéos performe.

### Abonnés

Vous ne pourrez pas obtenir d'informations sur la manière dont les visiteurs de votre chaîne s'abonnent.

La bonne nouvelle est que vous pouvez trouver cela en visitant la section **Analytics** de votre page YouTube Studio, puis en cliquant sur l'onglet **Public** en haut.

### Explorez les Analytics de YouTube Studio

Il y a beaucoup de choses que vous pouvez découvrir en explorant les Analytics de YouTube Studio. Prenez le temps de parcourir les deux solutions de rapports Analytics et apprenez quelles informations sont les plus utiles pour fournir une expérience impactante pour votre chaîne.

## Que puis-je faire d'autre avec YouTube et Google Analytics ?

### Suivre les liens de YouTube vers votre site web

Si vous avez un site web en dehors de votre chaîne YouTube et que vous avez configuré Google Analytics dessus, vous pouvez créer des URL personnalisées qui vous permettront de voir votre trafic YouTube comme une campagne. Cela est utile non seulement pour YouTube, mais aussi pour toute autre source que vous dirigez vers votre site web.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/google-analytics-campaign-url-builder.jpg)
_Création d'URL de campagne [Campaign URL Builder](https://ga-dev-tools.appspot.com/campaign-url-builder/)_

Google Analytics fournit cette capacité en utilisant des paramètres d'URL attachés aux liens. Vous pouvez en savoir plus sur la configuration et ce que vous devez faire avec [le site d'aide Analytics de Google](https://support.google.com/analytics/answer/1033863?hl=en).

Il convient également de noter que vous n'avez pas vraiment besoin de configurer votre chaîne YouTube avec Google Analytics pour utiliser cette fonctionnalité.

### Suivre comment les vidéos sont regardées lorsqu'elles sont intégrées sur votre site web

YouTube fournit une [API](https://developers.google.com/youtube/iframe_api_reference) que les développeurs peuvent utiliser pour écrire du JavaScript personnalisé et suivre l'utilisation des vidéos intégrées sur un site web donné.

En utilisant cela, nous pouvons envoyer des événements personnalisés basés sur des références temporelles ou des actions vidéo (comme lecture et pause) pour avoir une meilleure idée de la manière dont les vidéos sur notre site sont utilisées.

Pour être clair – cela ne concerne que les vidéos intégrées sur votre site web et suivra probablement l'utilisation avec la propriété Google Analytics de votre site web, sauf si vous le configurez autrement.

Consultez [YouTube iFrame Player API](https://developers.google.com/youtube/iframe_api_reference) pour plus d'informations.

### Pratiquement tout ce que Google Analytics fournit par défaut

[Il y a beaucoup de choses que vous pouvez faire avec Google Analytics](https://www.freecodecamp.org/news/making-sense-of-google-analytics-and-the-traffic-to-your-website/), que ce soit pour obtenir une meilleure visibilité sur l'origine des visiteurs ou sur leur localisation physique. Et en connectant votre chaîne YouTube, vous obtenez automatiquement ces informations.

## Plus de ressources, plus d'informations vous pouvez obtenir

Bien qu'il y ait des avantages à la fois pour YouTube Analytics et Google Analytics, avoir plus d'informations vous aidera finalement à prendre de meilleures décisions sur la manière dont vous gérez votre chaîne et votre contenu. Utilisez ces outils pour vous aider à lancer votre chaîne vers une célébrité YouTube inévitable !

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;"> Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>