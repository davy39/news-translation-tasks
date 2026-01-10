---
title: Comment automatiser votre vie et vos tâches quotidiennes avec Zapier
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-07-23T16:27:16.000Z'
originalURL: https://freecodecamp.org/news/how-to-automate-your-life-and-everyday-tasks-with-zapier
coverImage: https://www.freecodecamp.org/news/content/images/2020/07/zapier.jpg
tags:
- name: automation
  slug: automation
- name: Productivity
  slug: productivity
- name: workflow
  slug: workflow
seo_title: Comment automatiser votre vie et vos tâches quotidiennes avec Zapier
seo_desc: "Every day, we perform hundreds of small tasks. On their own, they don’t\
  \ take much time. But they can add up, especially if you consider that time for\
  \ a whole year. \nBut we’re technologists and it’s 2020. How can we use tools like\
  \ Zapier to make robot..."
---

Chaque jour, nous effectuons des centaines de petites tâches. Individuellement, elles ne prennent pas beaucoup de temps. Mais elles peuvent s'accumuler, surtout si vous considérez ce temps sur une année entière. 

Mais nous sommes des technologues et nous sommes en 2020. Comment pouvons-nous utiliser des outils comme Zapier pour faire faire ces choses par des robots ?

* [Qu'est-ce que Zapier ?](#heading-quest-ce-que-zapier)
* [Que pouvons-nous faire avec les Zaps de Zapier ?](#heading-que-pouvons-nous-faire-avec-les-zaps-de-zapier)
* [Zap 1 : Recevoir un SMS s'il va pleuvoir avec Zapier](#heading-zap-1-recevoir-un-sms-sil-va-pleuvoir-avec-zapier)
* [Zap 2 : Imprimer un test chaque semaine avec Google Cloud Print](#heading-zap-2-imprimer-un-test-chaque-semaine-avec-google-cloud-print)
* [Zap 3 : Alertes d'emploi de Smashing Magazine avec Gmail](#heading-zap-3-alertes-demploi-de-smashing-magazine-avec-gmail)

%[https://www.youtube.com/watch?v=12oAIHHEJMw]

## Qu'est-ce que Zapier ?

[Zapier](https://zapier.com/) est un outil d'automatisation qui connecte toutes les applications que vous aimez et crée des flux de travail puissants et entièrement automatisés. Que ce soit pour automatiser l'envoi d'un email ou pour s'assurer que le nouveau post de blog soit tweeté, nous pouvons supprimer les étapes manuelles des tâches fastidieuses pour nous concentrer sur d'autres choses importantes.

Chaque fois que vous créez un nouveau flux de travail, vous créez un "Zap". C'est essentiellement la manière de Zapier de donner un nom au flux de travail que vous créez.

## Que pouvons-nous faire avec les Zaps de Zapier ?

La partie brillante de Zapier est que chaque intégration d'application rend son API disponible via Zapier pour d'autres intégrations d'applications, vous offrant ainsi une multitude d'options pour connecter et créer des flux de travail puissants.

En particulier, nous allons apprendre à faire quelques choses :

* Envoyer un SMS chaque matin s'il va pleuvoir
* Configurer une impression hebdomadaire pour garder votre encre fraîche
* Recevoir des emails pour les nouveaux emplois sur le tableau d'emplois de Smashing Magazine

Bien que chacune de ces tâches soit petite, elles finissent par vous faire gagner beaucoup de temps. Et si vous êtes créatif, vous pouvez construire sur ces flux de travail pour personnaliser bien plus encore.

## Commencer avec un compte Zapier

Avant de commencer à configurer des flux de travail, vous aurez besoin d'un compte.

[S'inscrire à Zapier](https://zapier.com/) est gratuit et vous obtenez 5 Zaps gratuits pour commencer, donc nous n'avons pas à nous soucier du coût ici.

Maintenant, plongeons dans les Zaps.

## Zap 1 : Recevoir un SMS s'il va pleuvoir avec Zapier

Pour avoir une idée de comment cela fonctionne, nous allons commencer par quelque chose de simple. Nous allons configurer un Zap qui nous enverra un SMS si la météo prévoit de la pluie.

Pour commencer, cliquez sur le gros bouton **Créer un Zap** en haut à gauche de la page lorsque vous êtes connecté à votre compte.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-make-new-zap.jpg)
_Création d'un nouveau Zap_

Ici, Zapier veut savoir quelle est la première application que nous voulons connecter. Puisque nous allons baser notre Zap sur la météo, recherchez "weather" et sélectionnez **Weather by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/weather-by-zapier.jpg)
_Sélection de l'intégration Weather by Zapier_

Il vous demandera ensuite de choisir un **Événement de déclenchement**, où vous sélectionnerez "Will It Rain Today?", puis vous pourrez cliquer sur le bouton **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-weather-will-it-rain.jpg)
_Choix de l'événement Will it Rain Today?_

Lors du choix de la météo comme événement, il nécessite un peu d'informations pour nous donner une prédiction personnalisée. En particulier, il nécessite votre Latitude et Longitude, que nous pouvons rechercher en utilisant [latlong.net](https://www.latlong.net/).

![Image](https://www.freecodecamp.org/news/content/images/2020/07/latitude-longitude-finder.jpg)
_Trouver la latitude et la longitude avec latlong.net_

Vous pouvez ensuite entrer votre **Latitude** et **Longitude** dans l'écran **Personnaliser la Prévision** de Zapier, sélectionner vos **Unités** qui par défaut sont en **Fahrenheit**, et ensuite cliquer sur le gros bouton **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-customize-weather-forcast.jpg)
_Configuration de la prévision avec la latitude et la longitude_

À ce stade, vous pouvez cliquer sur **Tester le déclencheur**, ce qui vérifie simplement qu'il fonctionne, et cliquer à nouveau sur **Continuer**.

Maintenant, nous allons dire à Zapier quoi faire avec l'information une fois qu'il sait qu'il va pleuvoir.

Dans le panneau "Do this...", recherchez "sms" et sélectionnez **SMS by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-by-zapier.jpg)
_Sélection de SMS by Zapier_

Nous allons laisser l'**Application** et l'**Événement** par défaut, donc à l'écran suivant, vous pouvez simplement cliquer sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-sms-action-event.jpg)
_Application et Événement SMS_

Maintenant, pour que Zapier vous envoie un SMS, il doit vérifier que votre numéro de téléphone vous appartient ou que le numéro de téléphone s'inscrit volontairement pour recevoir ces SMS. Pour cela, il vous envoie un code PIN à usage unique que vous devrez entrer.

Donc, cliquez sur **Se connecter à SMS by Zapier**, ce qui ouvrira une fenêtre pop-up.

Ici, entrez votre numéro de téléphone, et choisissez SMS ou Appel comme méthode de vérification, moment auquel il vous contactera avec un code PIN.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sign-in-to-sms-by-zapier.jpg)
_Se connecter à SMS by Zapier et envoyer un code PIN_

Avec ce code PIN, entrez-le dans le champ et cliquez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-by-zapier-enter-pin.jpg)
_Entrez le code PIN de vérification SMS_

À ce stade, la fenêtre se fermera et vous reviendrez au flux original. Ici, cliquez à nouveau sur **Continuer**.

Maintenant, nous pouvons personnaliser le texte que nous recevons.

Dans le champ **Numéro d'expéditeur**, Zapier propose une série de numéros de téléphone que vous pouvez utiliser. Vous pouvez soit sélectionner un numéro pour toujours envoyer depuis celui-ci, que vous pouvez configurer comme contact pour savoir que c'est Zapier, soit vous pouvez sélectionner **Aléatoire**, qui utilisera un numéro aléatoire à chaque fois.

Ensuite, cliquez à l'intérieur de **Message**, et il affichera certaines options. Je veux savoir tout ce qui est possible s'il va pleuvoir, y compris la probabilité, la température maximale et le résumé, donc nous pouvons sélectionner tout ou autant que nous voulons et cliquer à nouveau sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/sms-zapier-configure-message.jpg)
_Configuration du message météo_

Enfin, nous pouvons tester si notre Zap a fonctionné. À ce stade, tout devrait être configuré, donc cliquez sur le bouton **Tester et Réviser** et vous devriez recevoir un SMS d'exemple !

_Note : Si vous choisissez un seul numéro d'expéditeur, vous pourriez être limité dans la fréquence à laquelle vous pouvez recevoir des SMS, donc si vous ne le recevez pas immédiatement, cela pourrait en être la raison. Le choix aléatoire aide à prévenir ce problème, mais le numéro n'est pas cohérent._

Et une fois que vous êtes satisfait de la configuration, vous pouvez cliquer sur **Activer le Zap**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-turn-on-zap.jpg)
_Activation du Zap SMS_

Vous recevrez maintenant des SMS le matin si la météo prévoit de la pluie !

## Zap 2 : Imprimer un test chaque semaine avec Google Cloud Print

Cela ne semble pas excitant, mais avez-vous déjà traversé une longue période où vous n'avez rien imprimé, pour finir avec des têtes d'impression séchées ou pire encore, une imprimante maintenant irréparable ?

Nous pouvons éviter cela en exécutant simplement un travail d'impression hebdomadaire qui maintient l'encre de notre imprimante fraîche et neuve.

Pour cela, nous utiliserons [Google Cloud Print](https://www.google.com/cloudprint/learn/). Pour que cela fonctionne, vous devez déjà l'avoir configuré avec votre compte Google.

Créons un nouveau Zap et cette fois pour notre "Quand cela se produit..." recherchez et sélectionnez **Schedule by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/schedule-by-zapier.jpg)
_Sélection de Schedule by Zapier_

Nous pouvons ensuite sélectionner un **Événement de déclenchement** de **Chaque semaine** et cliquer sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-schedule-trigger-every-week.jpg)
_Définir l'Événement de déclenchement comme Chaque semaine_

Ensuite, vous pouvez choisir le **Jour de la semaine** et l'**Heure de la journée** à laquelle vous souhaitez imprimer. Personnellement, j'exécute ce travail chaque semaine à 20h le dimanche, juste avant le début d'une nouvelle semaine. Une fois configuré, cliquez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-schedule-sunday-8pm.jpg)
_Configuration de la planification Zapier_

À ce stade, nous pouvons cliquer sur **Tester** le déclencheur, ce qui, comme avant, vérifie qu'il fonctionne correctement, puis nous pouvons cliquer sur **Continuer**.

Maintenant, pour notre "Faire ceci..." nous voulons imprimer, donc recherchez et sélectionnez **Google Cloud Print**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-google-cloud-print.jpg)
_Sélection de Google Cloud Print_

Et pour l'action, sélectionnez **Envoyer un travail d'impression**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-action-event-send-print-job.jpg)
_Définir Envoyer un travail d'impression comme Événement d'action_

À ce stade, vous devrez vous connecter à Google Cloud Print. Cela ouvrira une fenêtre et vous fera vous connecter via Google afin que Zapier puisse interfacer avec le service.

Une fois connecté, cliquez sur **Continuer**.

Maintenant, nous pouvons configurer notre travail d'impression. Ici, nous voudrons définir ce que nous imprimons.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-google-cloud-print-configuration.jpg)
_Configuration du travail d'impression dans Zapier_

Dans ce qui précède, nous configurons :

* **Quelle imprimante** : l'imprimante à laquelle nous voulons imprimer, connectée à Google Cloud Print
* **Contenu** : cela peut être une URL vers un document, du HTML ou du texte brut. J'utilise une URL qui est une simple page de test que j'ai créée et qui contient un peu de couleur
* **Type de contenu** : vous devrez le définir en fonction de ce que vous avez défini dans Contenu. Si vous avez défini une URL comme je l'ai fait, il devrait être URL
* **Titre du travail d'impression** : le nom du travail afin que vous puissiez le voir dans les journaux d'impression
* **Nombre de copies** : probablement juste 1 pour ne pas gaspiller d'encre et de papier
* **Couleur ou Monochrome** : vous devrez le définir explicitement si vous voulez de la couleur. L'idée est de rafraîchir toutes les cartouches d'encre, donc imprimer uniquement en noir n'aidera pas l'encre couleur, donc dans mon cas, j'ai sélectionné la couleur

Le reste des champs est facultatif, n'hésitez pas à personnaliser selon vos préférences.

Avec notre configuration définie, cliquez sur **Continuer**, et comme avant, nous pouvons cliquer sur **Test** pour voir notre travail d'impression en action et si nous sommes satisfaits, nous pouvons cliquer sur **Activer le Zap** !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-print-test.jpg)
_Test d'impression à partir du travail d'impression Zapier_

_Si vous souhaitez utiliser le même document, vous pouvez le trouver ici : [https://fay.io/printer-test.pdf](https://fay.io/printer-test.pdf)_

## Zap 3 : Alertes d'emploi de Smashing Magazine avec Gmail

Si nous cherchons un emploi, cela peut être une corvée de devoir visiter chaque tableau d'emplois chaque jour (ou chaque heure, n'est-ce pas ?). Mais nous pouvons automatiser ce processus lorsque le tableau d'emplois le supporte.

Heureusement, des tableaux d'emplois comme Smashing Magazine et beaucoup d'autres fournissent des flux RSS que nous pouvons connecter directement à Zapier pour automatiser la réception d'un email chaque fois qu'un nouvel emploi est publié.

Pour commencer, créons un nouveau Zap, et cette fois, recherchez RSS et sélectionnez **RSS by Zapier**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/rss-by-zapier.jpg)
_Sélection de RSS by Zapier_

Pour notre **Événement de déclenchement**, sélectionnez **Nouvel élément dans le flux**, puis cliquez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-new-feed-item.jpg)
_Définir Nouvel élément dans le flux comme Événement de déclenchement_

À ce stade, nous voulons entrer une URL de flux. Il s'agira de l'URL du flux RSS XML que les sites web rendent disponible. Pour Smashing Magazine, vous pouvez le trouver ici :

[https://www.smashingmagazine.com/jobs/feed](https://www.smashingmagazine.com/jobs/feed)

Donc, entrez cette URL ci-dessus dans **URL du flux** (vous pouvez laisser **Nom d'utilisateur** et **Mot de passe** vides), et gardez **GUID différent** sélectionné pour **Ce qui déclenche un nouvel élément de flux**. Ensuite, cliquez sur **Continuer**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-feed-configuration.jpg)
_Définir l'URL du flux RSS_

Comme d'habitude, vous pouvez maintenant tester le déclencheur pour vous assurer qu'il fonctionne. Si le flux RSS est valide, cela se passera sans problème, sinon vous pourriez voir une erreur. L'URL ci-dessus devrait être valide !

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-rss-found-feed-item-test.jpg)
_Test du flux RSS_

Ensuite, nous devons choisir ce que nous voulons faire avec le nouvel élément. Puisque nous voulons qu'il soit envoyé par email, nous pouvons choisir notre service de messagerie, qui dans mon cas est Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail.jpg)
_Sélection de Gmail dans Zapier_

Pour notre action, nous voulons **Envoyer un email**.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-send-email-trigger.jpg)
_Définir l'Événement d'action comme Envoyer un email_

Ensuite, vous devez vous connecter à votre compte, similaire à ce que nous avons fait avec Google Cloud Print. Cela devrait être votre compte Google que vous utilisez avec Gmail.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-sign-in-to-gmail.jpg)
_Se connecter à Gmail_

Maintenant, lorsque nous personnalisons notre email, nous voulons inclure les éléments suivants :

* **À** : où vous voulez que ces emails soient envoyés, probablement le même compte avec lequel vous vous êtes connecté à Gmail
* **De** : sélectionnez votre compte Gmail
* **Nom de l'expéditeur** : peut être n'importe quoi que vous reconnaîtrez, comme je vais utiliser Colbybot
* **Sujet** : peut être ce que vous voulez, mais une idée utile pourrait être "Nouvelle alerte d'emploi :" suivi de la sélection du titre dans la sélection déroulante
* **Type de corps** : vous pouvez laisser en Texte brut
* **Corps** : je recommande d'inclure tous les jetons que vous trouverez utiles, y compris le Titre, la Description et le Lien

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-email-configuration.jpg)
_Configuration de l'email de notification d'emploi_

Une fois que vous avez terminé la configuration, vous pouvez cliquer sur continuer. Ensuite, comme avant, cliquez sur **Tester et Réviser**, et vous devriez recevoir votre email de test.

![Image](https://www.freecodecamp.org/news/content/images/2020/07/zapier-gmail-test-email.jpg)
_Email d'alerte d'emploi de test_

Enfin, si vous êtes satisfait de la configuration, activez le Zap et profitez de votre recherche d'emploi !

## Que pouvez-vous faire d'autre ?

### Plus d'idées

Voici plus d'idées pour vous mettre sur la bonne voie :

* **Publier des Tweets sur Slack** : chaque fois qu'un compte tweete ou que quelqu'un d'une liste de comptes tweete, publiez ce tweet sur Slack
* **Signaler des bugs Github à Jira** : chaque fois que quelqu'un étiquette un problème Github avec le label "bug", créez un nouveau ticket dans Jira avec les détails de ce problème
* **Publier des éléments RSS sur Twitter** : écrivez-vous votre propre contenu ? Configurez un flux RSS pour publier automatiquement un tweet avec votre nouveau post de blog

### Pas Google Assistant

La seule chose qui me manque pour l'instant est Google Assistant, sinon j'aurais inclus quelques idées de Zaps pour cela. [IFTTT](http://ifttt.com/) supporte Google Assistant pour des flux plus simples, mais Zapier peut être plus puissant.

### Webhooks

Zapier supporte les webhooks — ce qui signifie que vous pouvez vraiment faire ce que vous voulez. Bien que ce [soit une fonctionnalité premium](https://zapier.com/apps/webhook/integrations), vous pouvez configurer certains flux de travail personnalisés basés sur les nouvelles données que Zapier voit ou accepter des requêtes que vous publiez pour déclencher d'autres automatisations.

## Quel est votre Zap préféré ?

J'adore entendre de nouvelles façons créatives d'utiliser Zapier. [Partagez avec moi sur Twitter !](https://twitter.com/colbyfayock)

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
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">?f60d Subscribe To My Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">f4e9f60d Sign Up For My Newsletter</a>
    </li>
  </ul>
</div>