---
title: 'Applications Web Progressives vs Pages Mobiles Accélérées : Quelles sont les
  différences et quelle est la meilleure option pour vous ?'
subtitle: ''
author: Oleh Romanyuk
co_authors: []
series: null
date: '2020-01-07T14:00:00.000Z'
originalURL: https://freecodecamp.org/news/pwa-vs-amp-what-is-the-difference-and-how-do-you-choose
coverImage: https://www.freecodecamp.org/news/content/images/2020/01/PWA-vs-AMP.png
tags:
- name: AMP
  slug: amp-tag
- name: mobile
  slug: mobile
- name: mobile app development
  slug: mobile-app-development
- name: PWA
  slug: pwa
seo_title: 'Applications Web Progressives vs Pages Mobiles Accélérées : Quelles sont
  les différences et quelle est la meilleure option pour vous ?'
seo_desc: 'Do you understand what PWAs and AMPs are, and which might be better for
  you? Let''s have a look and find out.

  So many people own smartphones these days. This opens up endless opportunities for
  a business - opportunities which, however, are immediately...'
---

Comprenez-vous ce que sont les PWAs et les AMPs, et laquelle de ces technologies pourrait vous convenir le mieux ? Examinons cela de plus près.

De nos jours, tant de personnes possèdent des smartphones. Cela ouvre des opportunités infinies pour les entreprises - des opportunités qui, cependant, sont immédiatement mises à l'épreuve par le nombre immense de concurrents sur le marché des logiciels mobiles.

Les applications mobiles sont certainement plus pratiques que les plateformes web ou de bureau. Pourtant, elles ne sont pas l'option la plus confortable que l'industrie offre.

Pour atteindre le plus haut niveau de satisfaction utilisateur et pour devancer les concurrents, les personnes inventives optent en faveur des applications web progressives (PWAs) ou des pages mobiles accélérées (AMPs).

Quelles sont ces technologies, et comment choisir la meilleure option ? Considérons chacune d'elles une par une en répondant à ces questions simples :

1. Qu'est-ce qu'une PWA ?
2. Qu'est-ce qu'une AMP ?
3. En quoi sont-elles similaires ?
4. En quoi sont-elles différentes ?
5. Pourquoi les PWAs sont meilleures que les pages web
6. Pourquoi les PWAs sont meilleures que les applications mobiles natives
7. Pourquoi les AMPs sont meilleures que les pages web
8. Pourquoi les AMPs ne sont PAS meilleures que les applications mobiles natives

## 1. Qu'est-ce qu'une PWA ?

Une application web progressive, ou PWA, unit les avantages des applications web et mobiles en un seul produit logiciel. Comme le déclare [<ins>Google</ins>](https://developers.google.com/web/progressive-web-apps), les PWAs sont des "expériences utilisateur qui ont la portée du web et sont fiables, rapides et engageantes". C'est une technologie qui vous permet d'utiliser un site web comme si c'était une application native.

[<ins>Twitter</ins>](https://twitter.com/?lang=en) est l'une des principales entreprises utilisant les PWAs. Pour installer l'application, vous ouvrez la version web sur votre téléphone et l'ajoutez à votre écran d'accueil. Lorsque vous ouvrez Twitter depuis l'icône de l'écran d'accueil, vous l'utilisez comme une application web progressive.

![PWA](https://images.ctfassets.net/6xhdtf1foerq/1TGtQag89baQtjFwQFRG1t/29cacc2916819498d669921833c88ceb/8-min.png?fm=png&q=85&w=1000)

### Fondamentaux

Les PWAs sont une solution hautement réactive et facilement partageable, qui peut fonctionner hors ligne. Elles stockent les fichiers HTML et CSS dans le cache du navigateur et les archivent avec des service workers. Cela permet d'utiliser la page web hors ligne. Les service workers sont l'un des trois composants essentiels d'une PWA, avec le fichier manifest et un protocole sécurisé HTTPS.

**Les service workers** sont des composants de code JavaScript qui jouent le rôle de proxy entre le réseau et le navigateur.

Lorsque vous ouvrez une page web pour la première fois, les service workers stockent les données nécessaires dans le cache du navigateur. Lorsque vous l'ouvrez une deuxième fois, les service workers récupèrent ces données depuis le cache avant même que l'application ait vérifié la disponibilité du réseau.

Non seulement ils permettent de travailler hors ligne, mais ils améliorent également considérablement le temps de réponse. Les service workers gèrent également les notifications push.

**Le fichier manifest** est un fichier JSON contenant toutes les informations sur votre application. Par exemple, il contient des données sur l'icône de l'écran d'accueil de votre PWA, son nom court, sa palette de couleurs ou son thème.

Si vous utilisez le navigateur Chrome sur un téléphone Android, le fichier manifest déclenchera l'installation automatique de la PWA sur votre téléphone.

**Le protocole sécurisé HTTPS** est une nécessité absolue si vous développez une application web progressive. Bien que les service workers rendent le concept même d'une PWA possible, ils sont vulnérables aux erreurs ou aux violations du réseau. Les service workers peuvent intercepter les requêtes réseau et modifier les réponses. Pour garantir la sécurité des données et la sécurité du réseau, le protocole sécurisé doit être utilisé.

### Histoires de succès

Twitter n'est pas la seule entreprise à avoir bénéficié des PWAs. Consultez ces [études de cas](https://developers.google.com/web/showcase/) publiées par Google pour voir comment cette technologie a aidé des entreprises populaires à réussir. Parmi ces entreprises figurent [Pinterest](https://www.pinterest.com/), [Alibaba](https://www.alibaba.com/), [The Weather Channel](https://weather.com/), [Lancome](https://www.lancome.com/), et [The Home Depot.](https://www.homedepot.com/)

## 2. Qu'est-ce qu'une AMP ?

AMP signifie Accelerated Mobile Page. Il s'agit d'une page web adaptée aux mobiles, conçue pour être chargée instantanément. C'est une solution de chargement rapide et fluide, développée en gardant à l'esprit l'expérience utilisateur. Introduite en tant que projet open-source, la technologie AMP a été intégrée par Google en février 2016.

En 2016, [The Guardian a annoncé](https://www.theguardian.com/membership/2016/feb/24/todays-release-of-accelerated-mobile-pages-amp) que leur plateforme était désormais disponible en tant qu'AMP. Pour aider les lecteurs à voir comment cela fonctionnait, ils ont affiché le même article à la fois comme [une version web](https://www.theguardian.com/us-news/commentisfree/2016/feb/16/thomas-piketty-bernie-sanders-us-election-2016) et [une version AMP](https://amp.theguardian.com/us-news/commentisfree/2016/feb/16/thomas-piketty-bernie-sanders-us-election-2016).

Il y avait quelques différences, mais elles étaient insignifiantes. Mais ce que vous remarqueriez tout de suite, c'est à quel point l'article AMP se chargeait plus rapidement que l'article web régulier.

![*En comparant cette illustration avec celle que j'ai incluse précédemment, vous pourriez remarquer un point intéressant. Une PWA doit être installée. En revanche, vous n'avez pas besoin d'installer AMP. Elle est accessible via un lien différent.
](https://images.ctfassets.net/6xhdtf1foerq/1ARjDXZC1yH4p15rxRosIW/e23cf5144729c5985e5a8ac156fb66a6/2.7_billion_people_use_smartphones__1_-min.png?fm=png&q=85&w=1000)
_*En comparant cette illustration avec celle que j'ai incluse précédemment, vous pourriez remarquer un point intéressant. Une PWA doit être installée. En revanche, vous n'avez pas besoin d'installer AMP. Elle est accessible via un lien différent._

### Fondamentaux

L'idée des AMPs est de réduire la quantité de contenu et de fonctionnalités inutiles afin que l'application affiche le contenu essentiel immédiatement. Les données peuvent être réduites jusqu'à dix fois. Les trois composants essentiels des AMPs sont AMP HTML, les composants AMP et le cache AMP.

**AMP HTML** est une version simplifiée du HTML régulier. AMP HTML n'autorise pas certaines balises et éléments de HTML (par exemple, les formulaires). Pour mieux comprendre à quoi devrait ressembler AMP HTML, consultez le [balisage requis](https://amp.dev/documentation/guides-and-tutorials/start/create/basic_markup/?referrer=ampproject.org).

**Les composants AMP** sont les scripts qui vous permettent de vous passer de JavaScript. L'idée de AMP est de se débarrasser de tous les scripts JavaScript qui rendent les pages plus lentes à charger.

Mais cela ne signifie pas que votre page doit se passer d'animations, de mises en page modifiées, de données analytiques, de suggestions de saisie semi-automatique ou de publicités. Il existe une bibliothèque extensive de [composants](https://amp.dev/documentation/components/?referrer=ampproject.org) qui vous permettent d'implémenter ces fonctionnalités et bien d'autres.

**Le cache AMP** est un réseau de diffusion de contenu basé sur un proxy qui récupère et met en cache le contenu des pages. Le cache AMP vous permet, en tant que propriétaire d'application, d'introduire facilement des mises à jour de pages. Il optimise et, si nécessaire, modifie l'AMP.

### Histoires de succès

Comme pour les PWAs, les entreprises sont souvent très fières des avantages commerciaux que les AMPs offrent. Voici une collection d'[histoires de succès](https://amp.dev/success-stories/) et d'études de cas d'entreprises qui ont utilisé les AMPs et en ont bénéficié. [<ins>Musement</ins>](https://www.musement.com/us/), [<ins>RCS MediaGroup</ins>](http://www.rcsmediagroup.it/), [<ins>CNBC</ins>](https://www.cnbc.com/), [<ins>The Washington Post</ins>](https://www.washingtonpost.com/) sont toutes des entreprises qui ont implémenté ou prévoient d'implémenter des AMPs.

## 3. En quoi les PWAs et les AMPs sont-elles similaires ?

Les PWAs et les AMPs sont toutes deux des méthodes d'affichage de pages web sur des appareils mobiles. Elles sont toutes deux créées pour améliorer l'expérience utilisateur.

Les AMPs et les PWAs aident toutes deux à réduire le temps de chargement des pages. Bien que les AMPs puissent être légèrement plus efficaces en termes de vitesse de chargement que les PWAs, la différence entre les temps de chargement des AMPs et des PWAs est à peine perceptible.

Les deux technologies sont activement soutenues par Google. Il existe [une page PWA sur Google Developers](https://developers.google.com/web/progressive-web-apps) et [une page AMP sur Google Developers](https://developers.google.com/amp) également.

Il n'y a pas beaucoup d'autres similitudes, mais cette similitude primaire est essentielle.

Maintenant, voyons quelles sont les différences.

## 4. En quoi les PWAs et les AMPs sont-elles différentes ?

### Apparence

En utilisant une PWA, vous n'avez pas l'impression d'utiliser une page web. Les PWAs ont l'apparence et le comportement d'une application mobile.

En utilisant des AMPs, vous êtes bien conscient d'utiliser une page web car elle a la même apparence.

### Développement

Dans le cas des PWAs, le code de l'application est écrit soit à partir de zéro, soit avec certaines parties du code existant.

Dans le cas des AMPs, le code existant d'une page web est dépouillé du CSS et du JS inutiles afin que la page web se charge plus rapidement.

### Expérience utilisateur

Les PWAs offrent une bien meilleure expérience utilisateur. Elles ont des notifications push, une icône sur l'écran d'accueil et aucun onglet de navigateur. De plus, elles sont beaucoup plus faciles à télécharger et plus légères qu'une application mobile régulière. Les PWAs se chargent plus rapidement qu'une version web régulière car elles sont intégrées avec App Shell. Et les PWAs peuvent être utilisées lorsque la connexion réseau est interrompue.

Les AMPs offrent une expérience utilisateur légèrement améliorée puisque la page se charge plus rapidement qu'une page régulière. Cependant, c'est le seul avantage UX qu'elles offrent. Contrairement aux PWAs, les AMPs ne peuvent pas fonctionner hors ligne.

### Performance

D'un point de vue SEO, AMP remporte la compétition. Google favorise ces pages et les liste dans le carrousel des principales histoires, ce qui peut augmenter votre taux de clics.

Les PWAs, en revanche, n'ont pas d'avantage direct pour le SEO. Cependant, une meilleure expérience utilisateur se traduit par des taux de rétention plus élevés, ce qui vous aide à gagner en SEO.

### Support

Les PWAs ne sont pas supportées de manière égale sur tous les appareils, donc vous pourriez rencontrer des inconvénients mineurs lorsqu'elles sont affichées sur iOS. De plus, elles ne supportent pas toutes les fonctionnalités matérielles, telles que Bluetooth, NFC, GPS ou les accéléromètres.

Les AMPs sont supportées par tous les principaux navigateurs sur tous les appareils.

### Applications pour lesquelles elles sont les mieux adaptées

Les PWAs fonctionnent parfaitement pour les applications qui nécessitent des interactions utilisateur. Les sites de commerce électronique, les réseaux sociaux ou les plateformes d'apprentissage en ligne où l'application doit être réactive et constamment mise à jour peuvent tirer parti de cette technologie. C'est pourquoi Twitter utilise une PWA, par exemple.

Les AMPs sont plus adaptées aux plateformes avec un mur de contenu, telles que les magazines ou journaux en ligne. Les AMPs chargent le contenu instantanément, mais les opportunités d'interaction sont limitées. C'est pourquoi The Guardian a décidé d'utiliser des AMPs.

## 5. Pourquoi les PWAs sont meilleures que les pages web

Si vous accédez à une page web sur mobile, vous devrez gérer les onglets du navigateur, les temps de chargement lents et les pop-ups ennuyeux. Si votre appareil a un écran relativement petit ou une connexion réseau lente, surfer sur le web devient insupportable.

Ce problème est résolu par les applications web progressives. En quelques clics, vous installez l'application sur votre téléphone et commencez à l'utiliser. Pas besoin de taper un lien, pas d'onglets de navigateur et pas d'écrans pop-up. L'application fonctionne rapidement, et elle fonctionne même si la connexion réseau est interrompue.

D'accord, les avantages de cette solution sont évidents, mais il semble que les applications mobiles natives pourraient fonctionner parfaitement à la place. Non, ce ne serait pas le cas. Voyons pourquoi les PWAs sont meilleures que les applications mobiles natives.

## 6. Pourquoi les PWAs sont meilleures que les applications mobiles natives

Pour utiliser une application mobile native, vous devez la trouver dans les catalogues de l'App Store ou de Google Play. Ensuite, vous devez attendre un certain temps pour la télécharger. Vous n'avez peut-être pas assez d'espace libre sur votre appareil, donc vous devrez en trouver.

En revanche, les PWAs sont installées et prêtes à être utilisées en quelques secondes. La taille du fichier est petite (bien qu'elle soit destinée à augmenter pendant que vous utilisez l'application et qu'elle met en cache). Cependant, la taille des données mises en cache dépend de la quantité d'espace de stockage libre que vous avez sur votre appareil.

Comme vous pouvez le voir, les PWAs semblent meilleures qu'une application web ou mobile native. Mais vous devez comprendre que cette solution n'est pas universelle. Consultez mon article récent sur [PWA vs Native](https://keenethics.com/blog/progressive-web-apps-vs-native-which-to-choose-and-when) pour savoir quand une application native est un meilleur choix qu'une PWA.

## 7. Pourquoi les AMPs sont meilleures que les pages web

Comme mentionné précédemment, les applications web sont lentes et peu pratiques, surtout lorsqu'elles sont accessibles sur des appareils mobiles avec un petit écran ou un matériel sous-alimenté.

En éliminant tous les composants web qui sont inutiles pour une bonne expérience utilisateur, les pages mobiles accélérées résolvent ce problème. Les AMPs sont 4 fois plus rapides et utilisent 10 fois moins de données que les pages web régulières.

## 8. Pourquoi les AMPs ne sont PAS meilleures que les applications mobiles natives

Malheureusement, les AMPs ne peuvent pas être un substitut complet aux applications mobiles natives. Elles ne peuvent pas être installées sur l'écran d'accueil, elles incluent toujours des onglets de navigateur et leur fonctionnalité est limitée à des choses de base.

Mais pour un journal en ligne ou pour un site d'information, comme [WebMD](https://www.webmd.com/), il est préférable d'utiliser des AMPs plutôt qu'une application mobile native. Ces sites ne nécessitent aucune fonctionnalité supplémentaire pour afficher le contenu des pages.

## Pour conclure

Les AMPs et les PWAs sont des technologies puissantes. Pour résumer les résultats de notre question initiale - PWAs vs AMPs :

* Les AMPs seront plus faciles, plus rapides et moins chères à développer
* Les PWAs offriront plus d'avantages.

Rappelez-vous simplement - aucune d'entre elles n'est une solution universelle, et aucune n'est une panacée. Même l'utilisation conjointe des AMPs et des PWAs peut ne pas répondre à toutes vos exigences. Parfois, vous devrez peut-être choisir des types de logiciels plus conventionnels.

Si vous n'êtes toujours pas sûr de ce qu'il faut choisir, nos spécialistes partagent <ins>[quatre questions pour comprendre si vous avez besoin d'une PWA](https://www.freecodecamp.org/news/four-questions-to-understand-if-you-need-pwa/)</ins>. En bref : _Nous croyons que les applications web progressives sont l'avenir. Les pages mobiles accélérées sont simplement trop simples et limitées en fonctionnalités pour rivaliser._

## Avez-vous une idée pour un projet ?

Mon entreprise KeenEthics est expérimentée à la fois dans les AMP et le [développement d'applications web progressives](https://keenethics.com/tech-apps-progressive-web-apps). Si vous êtes prêt à changer la donne et à démarrer votre projet, n'hésitez pas à [nous contacter](https://keenethics.com/contacts).

## P.S.

L'article original publié sur le blog de KeenEthics peut être trouvé ici : [PWA vs AMP : Quelles sont les différences et comment choisir ?](https://keenethics.com/blog/pwa-vs-amp)