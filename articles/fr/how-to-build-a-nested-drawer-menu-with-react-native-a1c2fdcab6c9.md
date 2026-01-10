---
title: Comment créer un menu tiroir imbriqué avec React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-25T01:59:28.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-nested-drawer-menu-with-react-native-a1c2fdcab6c9
coverImage: https://cdn-media-1.freecodecamp.org/images/1*rts2oeflx0NgkJ5wdhBUhg.png
tags:
- name: mobile app development
  slug: mobile-app-development
- name: General Programming
  slug: programming
- name: React
  slug: react
- name: 'tech '
  slug: tech
- name: technology
  slug: technology
seo_title: Comment créer un menu tiroir imbriqué avec React Native
seo_desc: 'By Dhruvdutt Jadhav

  Screen space is a precious commodity on mobile. The drawer menu (or “hamburger menu”)
  is one of the most popular navigation patterns that helps you save it while offering
  intuitive navigation. In this post, I will demystify how to...'
---

Par Dhruvdutt Jadhav

L'espace à l'écran est une denrée précieuse sur mobile. Le **menu tiroir** (ou « menu hamburger ») est l'un des modèles de navigation les plus populaires qui vous aide à l'économiser tout en offrant une navigation intuitive. Dans cet article, je vais démystifier comment construire un menu tiroir imbriqué (multi-niveaux) en utilisant [React Native](https://facebook.github.io/react-native/) et [React Navigation](https://reactnavigation.org/). ?

![Image](https://cdn-media-1.freecodecamp.org/images/1*YYYyBYo_SjxfgVnIsZyKUQ.gif)
_Menus tiroirs imbriqués dans React Native_

Essayez la démonstration en direct sur [**mobile**](https://expo.io/@dhruvdutt/native-kitchensink)?ou sur le [web.](https://expo.io/appetize-simulator?url=https://expo.io/@dhruvdutt/native-kitchensink&appetizeCode=pc_0dybu6gxac) ?_
_

### _Navigation dans React Native ⚒️_

_La navigation constitue l'épine dorsale d'une grande majorité des applications construites pour la production. L'apparence et la convivialité de la navigation sont importantes pour stimuler l'utilisation et l'engagement dans les applications mobiles._

_Cependant, si vous êtes développeur React Native, il n'y a pas d'opinion claire lorsqu'il s'agit de construire un menu de navigation. React Native [recommande](https://facebook.github.io/react-native/docs/navigation.html) plusieurs bibliothèques pour la navigation. Chacune a ses forces, selon vos besoins, mais il n'y a pas de gagnant clair pour tous les cas d'utilisation._

_Aucune des bibliothèques de navigation ne supporte actuellement les tiroirs imbriqués « prêt à l'emploi ». Mais l'une des bibliothèques qui fournit une API riche pour construire des solutions personnalisées est [React Navigation](https://reactnavigation.org/) — une navigation basée sur JavaScript. Elle est fortement soutenue et maintenue par la communauté React Native. C'est ce que nous allons utiliser dans ce tutoriel._

### _Le cas d'utilisation ?_

_Je devais construire une application de démonstration pour présenter une bibliothèque de composants UI pour React Native. Elle se compose de huit composants différents, chacun supportant diverses props, et plus de 50 options différentes._

_Il n'était pas possible de montrer toutes les options à l'intérieur du tiroir en une seule fois sans un tiroir multi-niveaux qui regrouperait les options en fonction du composant sélectionné. Je n'ai pas trouvé de solution prête à l'emploi pour cela, donc j'ai dû en construire une personnalisée._

### _Configuration de base ?_

_Pour la configuration de base, je suppose que vous avez déjà un projet React Native configuré avec soit [CRNA](https://facebook.github.io/react-native/docs/getting-started.html), [Expo Kit](https://docs.expo.io/versions/latest/), ou [React Native CLI](https://facebook.github.io/react-native/docs/getting-started.html). Assurez-vous d'avoir la bibliothèque [react-navigation](https://www.npmjs.com/package/react-navigation) installée avec soit yarn ou npm. Nous allons commencer directement avec l'utilisation de l'API de navigation._

> _N'hésitez pas à consulter le [guide de démarrage](https://reactnavigation.org/docs/getting-started.html) avant de continuer si vous n'êtes pas familier avec l'API React Navigation._

_Nous allons commencer avec un exemple similaire à celui documenté dans le guide officiel [DrawerNavigator](https://reactnavigation.org/docs/drawer-based-navigation.html) de React Navigation. Nous allons créer un tiroir simple qui a deux éléments de tiroir : Accueil et Notifications._

![Image](https://cdn-media-1.freecodecamp.org/images/1*48Gg3UOqNIKZpDGDlJ9tFQ.png)
_Configuration de base_

### _Contenu personnalisé du tiroir_

_React Navigation permet à tous les navigateurs de faire beaucoup de personnalisations en passant une configuration de navigateur comme deuxième paramètre. Nous allons l'utiliser pour rendre un contenu personnalisé autre que les éléments de tiroir standard._

_**DrawerNavigator**(RouteConfigs, DrawerNavigatorConfig)_

_Nous allons passer une prop appelée `[contentComponent](https://reactnavigation.org/docs/drawer-navigator.html#drawernavigatorconfig)` à la configuration qui nous permettra de rendre un contenu personnalisé pour le tiroir. Nous allons l'utiliser pour montrer un en-tête et un pied de page ainsi que les `[DrawerItems](https://reactnavigation.org/docs/drawer-navigator.html#providing-a-custom-contentcomponent)` existants de `react-navigation`._

![Image](https://cdn-media-1.freecodecamp.org/images/1*wz9NtNNwoXfw5mv7fv2EmQ.png)
_DrawerNavigator : Composant de contenu_

_Cela déverrouille potentiellement beaucoup de choses qui peuvent être faites en contrôlant ce qui doit être rendu à l'intérieur du tiroir._

### _Création de la cartographie des écrans_

_Nous devons construire un tiroir imbriqué pour chaque composant que nous voulons présenter. Commençons donc par enregistrer tous les écrans avec la [Config](https://reactnavigation.org/docs/drawer-navigator.html#drawernavigatorconfig) du DrawerNavigator. Nous avons créé un fichier de cartographie des écrans séparé pour les composants. Vous pouvez très bien avoir votre propre convention, ou définir l'objet directement de manière similaire au composant de l'écran d'accueil._

_La cartographie des écrans se compose d'objets simples avec la propriété screen. L'objet `screenMapping` ressemble à ceci :_

_Après avoir enregistré tous les composants, le tiroir ressemblera à ceci :_

![Image](https://cdn-media-1.freecodecamp.org/images/1*Rh-POAkjqZBruVHAdejFlw.png)
_Enregistrement de tous les composants avec les options enfants_

_Cela rendra tous les composants avec leurs options. Nous avons deux composants principaux : [DataSearch](https://opensource.appbase.io/reactive-manual/native/components/datasearch.html) et [TextField](https://opensource.appbase.io/reactive-manual/native/components/textfield.html). Chacun a des options comme « Avec position d'icône », « Avec placeholder », et plus. Notre tâche est de les séparer en une liste de seulement les composants (DataSearch, TextField)._

### _Regroupement du tiroir extérieur_

_Un modèle que j'ai suivi dans la cartographie était d'utiliser un délimiteur `_` pour regrouper les options d'un composant. Par exemple, les clés de navigation que j'ai utilisées étaient « DataSearch_Basic » et « DataSearch_With Icon Position ». C'est exactement ce qui va nous aider à combiner les options pour un seul composant comme DataSearch. Nous allons évaluer de manière unique tous les composants que nous devons montrer pour le tiroir extérieur._

_Nous allons créer une fonction utilitaire pour évaluer les éléments de la liste du tiroir extérieur à rendre._

_Cette fonction retournera un objet avec des composants uniques pour les composants principaux comme (DataSearch, TextField) que nous allons rendre à l'écran avec l'aide du composant personnalisé `contentComponent`. Nous allons également maintenir un _booléen_ pour déterminer le contenu rendu sur le tiroir à un instant particulier._

_`renderMainDrawerComponent` est simplement une fonction qui itère sur les clés de l'objet des composants. Elle rend des éléments de tiroir extérieur personnalisés construits sur la base de `Text` et `View` de react-native. Consultez le code complet [ici](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/components/OuterDrawerItem.js)._

_Cela rendra le tiroir comme ceci :_

![Image](https://cdn-media-1.freecodecamp.org/images/1*NeMPqRQBQJr4JChGL2SMmQ.png)
_Affichage uniquement des éléments de tiroir des composants extérieurs_

### _Rendu du tiroir enfant ?_

_Maintenant, nous devons montrer les options en fonction du composant qui est sélectionné. Vous avez peut-être remarqué que dans les utilitaires, nous extrayons également les index de début et de fin des groupes de composants en fonction du modèle de délimiteur._

_Par exemple, les écrans DataSearch commencent à l'index 1 (l'index 0 est l'écran d'accueil) et se terminent à 3. TextField commence à 3 et se termine à 5. Nous allons utiliser ces index pour découper magiquement les `items` qui sont passés à `DrawerItems` en fonction du composant sélectionné et de ses index._

_Maintenant, après avoir tapé sur DataSearch, le tiroir se transformera en quelque chose comme ceci :_

![Image](https://cdn-media-1.freecodecamp.org/images/1*WdWUmlaxr-NUQaOr5C7UIA.png)
_Composants enfants pour un composant sélectionné_

_Nous avons également ajouté un joli bouton de retour qui bascule essentiellement un booléen pour rendre les éléments du tiroir principal. Vous pouvez consulter le code complet [ici](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js)._

_Maintenant, la seule chose restante à faire est de rendre les éléments du tiroir plus propres en supprimant le nom de composant redondant. Encore une fois, la riche API React Navigation se révèle utile ici._

_Il existe diverses propriétés que nous pouvons passer avec `[navigationOptions](https://reactnavigation.org/docs/stack-navigator.html#navigationoptions-used-by-stacknavigator)`. Une en particulier que nous allons utiliser ici est la prop `[title](https://reactnavigation.org/docs/stack-navigator.html#title)` avec la cartographie des écrans. Cela nous permettra de supprimer la partie avant le premier délimiteur. Ainsi, « DataSearch_Basic » s'affichera comme « Basic » uniquement._

![Image](https://cdn-media-1.freecodecamp.org/images/1*k9mp_b8adb_a6WJlVwx63Q.png)
_Éléments du tiroir enfant_

_C'est tout. Nous pouvons ajouter autant d'éléments que nous voulons en fonction du modèle de délimiteur. L'application de démonstration que nous avons construite se compose de huit composants principaux et de plus de 53 options au total._

![Image](https://cdn-media-1.freecodecamp.org/images/1*7cawloWms3S3_t23c03L4g.png)

> _Voici le [lien](https://expo.io/@dhruvdutt/native-kitchensink) vers l'application finale et le [code source](https://github.com/appbaseio-apps/native-kitchensink)._

### _Résumé ?_

*_**Configuration de base** : Bonjour le monde avec DrawerNavigation depuis les [docs](https://reactnavigation.org/docs/drawer-based-navigation.html)._
*_**Contenu personnalisé du tiroir** : Rendre les éléments du tiroir avec `[contentComponent](https://reactnavigation.org/docs/drawer-navigator.html#providing-a-custom-contentcomponent)`._
*_**Cartographie des écrans** : [Définir](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/screenMapping.js) et [enregistrer](https://github.com/appbaseio-apps/native-kitchensink/blob/master/App.js#L14-L15) tous les composants des tiroirs._
*_**Regrouper le tiroir extérieur** : [Lire](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/utils.js#L1-L20) le modèle de délimiteur pour [regrouper](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js#L67-L68) les éléments du tiroir._
*_**Rendu du tiroir enfant** : [Découper](https://github.com/appbaseio-apps/native-kitchensink/blob/master/src/drawers/MainDrawer.js#L81) et rendre les éléments du tiroir enfant._

### _Conclusion ?_

_Nous avons appris à construire un menu tiroir multi-niveaux avec React Native. Nous avons utilisé l'API React Navigation pour rendre un composant de contenu personnalisé à l'intérieur du tiroir, et utilisé le modèle de délimiteur pour la cartographie des écrans. Utilisez ce modèle pour construire n'importe quel niveau d'imbrication ou de rendu conditionnel pour les tiroirs._

### _ReactiveSearch ?_

_Fournit des composants UI pour les plateformes Native et Web afin de construire des expériences de recherche parfaites. Vous pouvez vérifier tous les composants qu'il offre en jouant avec l'[application de démonstration](https://expo.io/@dhruvdutt/native-kitchensink) elle-même ou [en créant votre propre composant](https://opensource.appbase.io/reactive-manual/native/advanced/reactivecomponent.html)._

_[**appbaseio/reactivesearch**](https://github.com/appbaseio/reactivesearch)_  
_[reactivesearch - Une bibliothèque de composants UI React et React Native pour construire des applications pilotées par les données](https://github.com/appbaseio/reactivesearch)github.com_