---
title: Comment configurer facilement le suivi des événements personnalisés dans Google
  Analytics
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-19T17:41:51.000Z'
originalURL: https://freecodecamp.org/news/how-to-easily-set-up-custom-events-tracking-in-google-analytics-d1818e2ecdd0
coverImage: https://cdn-media-1.freecodecamp.org/images/1*FnDrSxZXNERxjYqpHoM1mA.jpeg
tags:
- name: data analysis
  slug: data-analysis
- name: Google Analytics
  slug: google-analytics
- name: marketing
  slug: marketing
- name: General Programming
  slug: programming
- name: 'tech '
  slug: tech
seo_title: Comment configurer facilement le suivi des événements personnalisés dans
  Google Analytics
seo_desc: 'By Pankaj Singh

  The Growing need for Custom Event Tracking

  I am a technologist-turned-analytics professional since five-plus years. Recently,
  a friend asked me how he can set up a custom event tracking on his small business
  website and understand his...'
---

Par Pankaj Singh

### **Le besoin croissant de suivi des événements personnalisés**

Je suis un technologue devenu professionnel de l'analyse depuis plus de cinq ans. Récemmment, un ami m'a demandé comment il pouvait configurer un suivi d'événements personnalisés sur le site web de sa petite entreprise et mieux comprendre le comportement des utilisateurs de son site.

Il y a quelques années, les petites entreprises et les blogueurs personnels étaient satisfaits de connaître le nombre de visiteurs uniques et de vues de pages sur leur site web. Mais aujourd'hui, tout le monde veut comprendre bien plus que de simples vues de pages. Ils veulent savoir combien d'utilisateurs ont cliqué sur différents boutons, regardé une vidéo, vérifié les détails d'un produit ou cliqué sur des publicités tierces, entre autres. Il y a une demande croissante de comprendre comment différents utilisateurs interagissent avec leurs actifs numériques.

Il existe de nombreux objectifs pour lesquels vous pouvez utiliser votre site web, et il y a autant d'activités à surveiller sur un site web. Alors que les grandes entreprises ont des équipes dédiées, les petites entreprises ont généralement une seule personne qui gère à la fois l'analyse et la configuration technique de leur compte d'analyse.

> "Heureusement, la configuration des objectifs de base et même des objectifs personnalisés avancés dans Google Analytics n'est pas difficile, tant que vous connaissez les bonnes étapes. Et dans cet article, nous allons passer en revue exactement cela. Je vais vous guider à travers les étapes de configuration des objectifs personnalisés de la manière la plus simple pendant que vous profitez de votre café !" - Documentation de Google

## Aperçu

Tout d'abord, pour réviser, passons en revue les quatre principaux types d'objectifs personnalisés disponibles dans votre compte Google Analytics. Si vous les connaissez déjà et souhaitez comprendre uniquement le dernier (le type d'objectif "Événement"), faites défiler jusqu'au point 4 : "Configuration d'un objectif d'événement". Un coup d'œil à la capture d'écran ci-dessous vous expliquera les quatre principaux objectifs que vous pouvez personnaliser dans Google Analytics.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_jVaB9r6Kdv_fxeObzUeKXg.png)
_Les 4 types d'objectifs personnalisés dans vos paramètres d'objectif GA_

Vous remarquerez que les trois premiers objectifs sont très intuitifs et directement utilisables. Une fois configurés, ils vous donneront un taux de conversion x% au cours des 7 derniers jours. Mais le dernier retournera un taux de conversion de 0%. Passons d'abord en revue les trois objectifs plus simples, puis nous pourrons comprendre l'objectif d'événement en détail.

## **1. Configuration d'un objectif de destination**

Tout ce dont vous avez besoin pour cela est de donner l'URL de la page que vous identifiez comme un succès lors d'une visite de page. Par exemple, sur les sites web de commerce électronique, lorsqu'une personne effectue un achat et atteint une page de "remerciment", c'est un succès. Ainsi, la visite de la page de remerciement peut être un objectif.

Tout ce que vous avez à faire est d'entrer l'URL de cette page comme destination, _www.votresiteexemple.com/merci.html_. Il est possible que votre site web ait différents paramètres de requête, vous pouvez donc utiliser des options comme "URL commence par", "URL se termine par" ou "Regex".

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_ijl4io4cmLAvEf1cSOOLiw.png)
_Définition d'un objectif de "Destination" dans Google Analytics_

## **2. Configuration d'un objectif de durée**

Cela fait référence au nombre de minutes (ou d'heures) passées sur votre site web par un utilisateur. L'utilisation de cet objectif peut varier en fonction du but d'un site web. Passer plus de temps sur votre site peut être souhaitable, mais cela ne signifie pas une conversion certaine. Cela peut aussi signifier que votre site web n'est pas assez facile pour aider les utilisateurs à accomplir leurs tâches rapidement.

Cependant, pour les sites web orientés contenu tels que ceux des journaux, des blogueurs, des magazines ou du contenu vidéo, un objectif de durée peut être important. Ainsi, en fonction du but de votre site, il peut être judicieux de définir différents objectifs de durée.

Comme vous pouvez le voir ci-dessous, vous pouvez entrer une durée pour cet objectif et vous serez prêt à suivre tous les utilisateurs qui dépassent cette marque.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_oTaECRqhsaVI8eL1P0Y6_Q.png)
_Définition de l'objectif de "Durée" dans Google Analytics_

## **3. Pages/écrans par session**

Il s'agit du nombre de pages consultées lors d'une seule session ou visite. Si un visiteur ferme le site web et revient le lendemain, ou après un intervalle de 30 minutes le même jour, cela s'appelle une nouvelle session.

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_LCkKm70Q-_vwKR3gOEpAMQ.png)
_Définition des "Pages par session" dans Google Analytics_

## **4. Configuration d'un type d'objectif d'événement personnalisé**

Un "événement" est toute action effectuée par un utilisateur qui marque une interaction avec votre site web après avoir atterri sur l'une de ses pages. L'exemple le plus simple est lorsqu'ils cliquent sur un bouton comme "Acheter maintenant" ou "En savoir plus". Il peut également être utilisé pour des options comme le téléchargement d'un PDF ou d'un e-book, entre autres actions.

Cliquer sur un bouton est généralement appelé un CTA, abréviation de "Call to Action". Lorsque vous choisissez cette option dans vos paramètres d'objectifs personnalisés, vous verrez cette fenêtre s'ouvrir avec quatre options :

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_A0292cpFgkeBgN_nJb2g5Q.png)
_Configuration des champs pour l'objectif "Événement" de Google Analytics_

Les quatre champs ou paramètres sont simples à entrer. GA vous demande de définir chaque événement avec ces quatre champs afin que vous puissiez facilement les identifier lors de l'analyse.

> _"__Vous pouvez écrire n'importe quoi dans ces paramètres, mais il est recommandé de les définir de manière à ce qu'ils aient le plus de sens pour votre entreprise.__" - Documentation de Google_

Par exemple, si vous gérez un magasin vendant des gadgets électroniques et des accessoires, vous pouvez vouloir le remplir comme suit :

**A. Catégorie :** Catégorie du produit. Exemple, 'Écouteurs'

**B. Action :** Supposons qu'un utilisateur a cliqué sur le bouton 'Ajouter au panier'. Vous pourriez alors écrire 'AjouterAuPanierClic' dans votre action. Dans le cas où vous avez un bouton supplémentaire pour 'Caractéristiques' ou 'En savoir plus' pour ce produit, vous pouvez avoir un objectif supplémentaire et définir son action comme 'EnSavoirPlusClic' pour ce bouton.

**C. Libellé :** Le libellé peut être n'importe quoi qui vous aide à reconnaître ou à regrouper vos événements lors de votre analyse. Il peut s'agir du nom d'une 'Campagne' ou d'une 'Marque'. Par exemple, 'CampagneUniversitaireSony'.

**D. Valeur :** Il s'agit d'une valeur optionnelle, principalement utilisée pour définir un chiffre de revenus. Elle peut être utilisée pour définir un nombre spécifique comme 50 $, ou pour prendre une valeur dynamique à partir de la variable de revenus de votre page, comme $("VariablePrix"). Notez que $ ici est un identifiant jquery et non la devise dollar. La récupération d'un ID dépendrait de la variable de prix ou de coût définie dans votre HTML.

> "Après avoir défini les valeurs de votre type d'objectif d'événement ici, la partie délicate commence. Puisque tous les autres objectifs dans GA sont directement utilisables une fois définis, il est déroutant pour beaucoup de ne pas comprendre pourquoi l'objectif d'événement ne commence pas à fonctionner immédiatement. C'est pourquoi lorsque vous cliquez sur 'Vérifier la conversion' pour cet objectif, vous voyez une conversion de 0%." - Documentation de Google

![Image](https://www.freecodecamp.org/news/content/images/2019/11/1_CBDM9KgwzQY-5FwcaLtWQQ.png)
_L'objectif d'événement n'est pas directement utilisable après la configuration_

Pour corriger cette conversion de 0%, vous devez intégrer les paramètres de cet objectif avec l'événement de clic réel ou l'action personnalisée responsable sur votre site web, pour cet objectif.

# **Intégration du suivi des événements personnalisés avec le HTML de votre site web**

Parfois, les utilisateurs commerciaux (en particulier les non-techniciens) ont tendance à se sentir anxieux lorsque quelque chose lié à la programmation survient lors de leurs analyses. Heureusement, Google a rendu très simple le fait de lier tout besoin de suivi d'événements personnalisés qui doit être intégré à votre site web. Seule une gestion d'un site web de commerce électronique complexe nécessiterait l'aide d'un développeur, ce que vous auriez généralement accès si vous travaillez dans une entreprise de taille moyenne.

Pour l'intégration, Google a déjà mis en place une fonction de modèle standard qu'il s'attend à ce que vous utilisiez lors du suivi d'un événement personnalisé sur votre page. Il s'agit d'une ligne de code, pour laquelle vous avez déjà défini des valeurs dans votre compte GA. Les marketeurs ou les codeurs y font généralement référence comme à l'appel GA-Send qui est au format suivant :

```
ga('send', 'event', [eventCategory], [eventAction], [eventLabel], [eventValue]);
```

La fonction JS réelle dans votre page HTML peut être en une seule ligne ou peut ressembler à ceci pour une lisibilité facile :

```
ga('send', {
  hitType: 'event',
  eventCategory: 'Écouteurs',
  eventAction: 'AjouterAuPanierClic',
  eventLabel: 'CampagneUniversitaireSony'
});
```

Notez que les valeurs de cette fonction doivent correspondre aux valeurs entrées dans votre compte GA lors de la configuration de l'événement pour ses paramètres respectifs. **Maintenant, vous devez toujours lier l'appel GA send ci-dessus avec l'action réelle sur le bouton.**

Par exemple, vous souhaitez lier la fonction ci-dessus au clic sur le bouton 'Ajouter au panier'. La seule étape que vous devrez ajouter est d'inclure cette fonction dans l'événement d'action 'onClick' pour cet ID de bouton.

```
Intégration du script d'événement Google Analytics cité ci-dessus dans votre HTML
<script>
$(document).ready(function(){
  $("#exampleAddNowButtonID").click(function(){
    ga('send', 'event', 'Écouteurs', 'AjouterAuPanierClic', 'CampagneUniversitaireSony');
  });
});
</script>
```

# Conclusion

Cela me conduit à la fin de cet article. J'ai essayé d'expliquer avec simplicité et détails que je trouvais manquants lorsque j'apprenais à configurer le suivi personnalisé pour mes propres besoins. Espérons que ce guide étape par étape vous aide à configurer le suivi de vos objectifs personnalisés qui répondent le mieux à vos besoins.

N'hésitez pas à partager vos pensées ou à poser des questions de clarification liées à cet article dans les commentaires.

Si vous souhaitez suivre des cours en ligne gratuits sur Google Analytics, vous pouvez visiter [ici](http://www.quickcode.co/free/course/learn/Google-Analytics-Basics-For-Beginners-Free--2018/1071).

_Certaines parties de cette page sont des modifications basées sur des travaux créés et [partagés par Google](https://developers.google.com/readme/policies/) et utilisés selon les termes décrits dans la [Licence Creative Commons 3.0 Attribution](http://creativecommons.org/licenses/by/3.0/)._