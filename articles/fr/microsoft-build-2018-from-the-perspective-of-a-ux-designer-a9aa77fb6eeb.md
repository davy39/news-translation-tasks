---
title: Microsoft Build 2018 du point de vue d'un designer UX
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-05-24T18:46:03.000Z'
originalURL: https://freecodecamp.org/news/microsoft-build-2018-from-the-perspective-of-a-ux-designer-a9aa77fb6eeb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*KUVkepN4MnBioPAqGhRCdg.png
tags:
- name: Fluent Design
  slug: fluent-design
- name: Microsoft
  slug: microsoft
- name: technology
  slug: technology
- name: ux design
  slug: ux-design
- name: Windows
  slug: windows
seo_title: Microsoft Build 2018 du point de vue d'un designer UX
seo_desc: "By Samuele Dassatti\nI recently attended Microsoft Build 2018 in Seattle,\
  \ because one of my apps was nominated for Design Innovator of the Year at the Windows\
  \ Developer Awards.   \nDuring the three-day conference, the Redmond giant detailed,\
  \ among othe..."
---

Par Samuele Dassatti

J'ai récemment assisté à Microsoft Build 2018 à Seattle, car l'une de mes applications était nominée pour le prix Design Innovator of the Year aux Windows Developer Awards.   
   
Lors de cette conférence de trois jours, le géant de Redmond a détaillé, entre autres, ce qui attend le Fluent Design System. Il s'agit du langage de design annoncé lors du Build de l'année dernière, sur lequel Microsoft espère construire l'interface utilisateur de Windows et de ses applications.

Voici les annonces les plus importantes concernant l'avenir de la conception de l'expérience utilisateur sur la plateforme Windows.

### Fluent partout

L'une des plus grandes tendances du point de vue de l'interface utilisateur que j'ai observée était la volonté de Microsoft de rendre le nouveau langage de design accessible au plus grand nombre de développeurs possible, quel que soit leur framework de choix.  
   
Nous pouvons résumer cette stratégie avec trois éléments : **UWP XAML Islands**, la **Windows UI library** et **Fluent Design Web** (brièvement évoqué). Examinons chacun d'eux de plus près.

### UWP XAML Islands

![Image](https://cdn-media-1.freecodecamp.org/images/y7eSHuzFbLdkk7o7arOBwEsSEfD0CzqH8zs3)

Alors, que sont les UWP XAML Islands ? Il s'agit d'une nouvelle bibliothèque homonyme qui permet aux applications WinForms, WPF et Win32 de présenter des éléments d'interface utilisateur qui, jusqu'à présent, étaient limités aux applications UWP.   
   
Cela signifie que les développeurs pourront commencer à moderniser progressivement les interfaces utilisateur de leurs applications en intégrant des "îlots" (le nom prend enfin tout son sens) d'éléments d'interface utilisateur XAML.

Ces îlots pourraient être une zone limitée de l'interface utilisateur ou une fenêtre entière, permettant ainsi aux développeurs de conserver le code-behind d'une application héritée de Windows tout en modernisant son apparence pour augmenter l'engagement des utilisateurs et rendre l'application plus cohérente avec le reste du système d'exploitation.

> Un XAML Island est simplement un contrôle UWP standard ou même une interface utilisateur UWP complète qui est intégrée de manière transparente dans n'importe quel autre framework d'interface utilisateur. [] Cela fonctionne simplement.

> Kevin Gallo, responsable de la plateforme Windows Developer, lors de Microsoft Build 2018

### La bibliothèque Windows UI

Le concept central de la bibliothèque Windows UI (ou WinUI, comme l'ont appelé de nombreux représentants de Microsoft) est très similaire à celui des UWP XAML Islands. Cependant, son objectif est très différent.

Islands se concentre sur l'intégration des contrôles XAML UWP dans les applications héritées. En revanche, WinUI permettrait aux développeurs de tirer parti de la polyvalence des contrôles XAML qui ne sont disponibles nativement que sur les dernières versions de Windows sur chaque version du système d'exploitation (à partir de la mise à jour Anniversary, également connue sous le nom de version 1607).  
   
Comme vous pouvez vous y attendre, l'enthousiasme pour cette nouvelle fonctionnalité a été limité, puisque les nouvelles mises à jour de Windows atteignent généralement presque tous les appareils Windows en quelques mois seulement. Mais quoi qu'il en soit, c'est une fonctionnalité intéressante.

![Image](https://cdn-media-1.freecodecamp.org/images/WrUMtrNigImCQTnQs5PHA2qbwZf82K1WeSXe)
_La bibliothèque WinUI signifie que vous pouvez utiliser les dernières API dans votre application tout en atteignant près de 10 % de clients supplémentaires. Le graphique est basé sur les données du rapport AdDuplex d'avril 2018_

### Fluent Design Web

Si c'est la première fois que vous entendez parler de cela malgré avoir suivi de près la conférence Build, ne vous inquiétez pas. Le projet a été brièvement évoqué lors d'une session de questions-réponses après une présentation sur les Progressive Web Apps et, au moment de la rédaction, il n'y a eu aucune confirmation officielle.  
   
Voici ce que nous savons à ce sujet : Microsoft tente de promouvoir son système de design comme n'étant pas limité à la plateforme Windows. Cela fait partie d'un effort de Microsoft pour aider les développeurs web à rendre leurs PWAs plus natives pour le système d'exploitation.

Au fait, si vous êtes intéressé à apprendre comment rendre votre application web plus native, je vous suggère de lire [cet article](https://medium.freecodecamp.org/how-you-can-develop-progressive-web-apps-that-feel-native-5110fbbcbf4b).

### Élargir la boîte à outils Fluent

Une annonce clé lors de la conférence Build de cette année était l'introduction de nouvelles API de fenêtrage pour les applications UWP. En particulier, les fenêtres companions ont enfin été introduites. Je dis "enfin", car cela permettra à la fenêtre principale de l'application de déplacer certains de ses éléments d'interface utilisateur vers des fenêtres plus petites qui suivent la fenêtre principale. Cela permettra aux développeurs de construire des applications plus complexes pour la plateforme Windows universelle.

Une autre addition bienvenue était les nouveaux principes de design appliqués aux menus contextuels. Non seulement ils seront mis en évidence par une ombre portée qui sera rendue différemment en fonction de sa position sur l'axe Z, mais ils sont également soumis à une fermeture légère (c'est-à-dire la capacité de les fermer en cliquant simplement à l'extérieur). Cela sera représenté par l'utilisation de l'effet acrylique emblématique.

J'espère vraiment que ces changements de design subtils amélioreront la productivité pour les utilisateurs UWP à travers le monde.

![Image](https://cdn-media-1.freecodecamp.org/images/unmsLg6YtQsd8DCWXCmuK7ryMIzlRrzGAESq)
_Un exemple du nouveau design des menus contextuels_

### Faire de Fluent Design une expérience multi-appareils et multi-sensorielle

![Image](https://cdn-media-1.freecodecamp.org/images/cVxpVgVN3ZPasgS7Dz6ZgqL4uewSKNbaJfi3)
_La timeline de Microsoft Launcher est le premier exemple de la manière dont Microsoft tente d'étendre son langage de design au-delà de Windows_

Lors de la deuxième keynote, l'un des premiers produits mentionnés par Joe Belfiore était le Microsoft Launcher pour Android. L'accent mis sur un tel produit, qui aurait été impensable il y a seulement quelques années, souligne à quel point Microsoft est sérieux quant à l'extension du Fluent Design System à d'autres plateformes. Cela renforce également la vision de Satya Nadella selon laquelle l'expérience Microsoft est multi-appareils et multi-sensorielle.  
   
L'autre annonce clé concernant la nature universelle du système de design était le nouveau standard de densité. Il passe des rectangles larges et adaptés au tactile de Metro à un juste milieu qui permet aux utilisateurs de voir plus de détails sans sacrifier l'utilisabilité sur les appareils tactiles. Microsoft a également montré un standard encore plus dense, optimisé pour les applications desktop-first et les applications professionnelles.

### Conclusion

Rien de particulièrement révolutionnaire en termes de design n'a été introduit. Mais les annonces de Build 2018 montrent un système de design qui, bien que manquant dans certains domaines, est relativement jeune et va dans la bonne direction. Je pense que c'est le cas parce que Microsoft se concentre sur le rendre véritablement universel et plus polyvalent que jamais.

J'espère que cet article vous a aidé à comprendre la direction dans laquelle le Fluent Design System se dirige et, si vous avez des pensées sur les récentes annonces, je serai ravi de lire vos réponses.