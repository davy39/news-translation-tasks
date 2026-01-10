---
title: Comment bloquer le contenu gênant des pages web en utilisant uBlock Origin
subtitle: ''
author: Seth Falco
co_authors: []
series: null
date: '2021-08-24T19:39:53.000Z'
originalURL: https://freecodecamp.org/news/how-to-block-content-from-web-pages-using-ublock-origin
coverImage: https://www.freecodecamp.org/news/content/images/2021/08/untitled-1.png
tags:
- name: Browsers
  slug: browsers
- name: Productivity
  slug: productivity
seo_title: Comment bloquer le contenu gênant des pages web en utilisant uBlock Origin
seo_desc: 'You can use extensions in your browser to remove parts of a webpage you
  don''t want to see. Removing annoyances, distractions, and irrelevant content is
  a great way to stay focused and remain efficient while you consume information on
  the internet.

  Th...'
---

Vous pouvez utiliser des extensions dans votre navigateur pour supprimer des parties d'une page web que vous ne souhaitez pas voir. Supprimer les éléments gênants, les distractions et le contenu non pertinent est un excellent moyen de rester concentré et efficace tout en consommant des informations sur Internet.

Il existe de nombreuses extensions qui ajoutent cette fonctionnalité à votre navigateur. Je vais me concentrer sur [uBlock Origin,](https://ublockorigin.com/) car beaucoup l'ont déjà. Si ce n'est pas le cas, je vous recommande fortement de l'installer.

## Qu'est-ce que uBlock Origin ?

[uBlock Origin](https://ublockorigin.com/) est un bloqueur de publicités gratuit et open-source disponible pour tous les principaux navigateurs. Il inclut également un outil de [sélecteur d'éléments](https://github.com/gorhill/uBlock/wiki/Element-picker) qui peut supprimer des éléments personnalisés, ce que nous allons utiliser dans cet article.

Avoir des connaissances en sélecteurs CSS ou XPath vous aidera à suivre ce tutoriel, mais ce n'est pas obligatoire. uBlock Origin fournit des outils visuels pour sélectionner des éléments sans connaissances techniques. Cependant, écrire le sélecteur manuellement sera généralement plus fiable.

## Pourquoi bloquer des éléments est utile

Sur Internet, nous consommons constamment des informations, mais souvent il s'agit d'informations qui ne nous sont tout simplement pas pertinentes.

Si vous accédez à des sites web particuliers fréquemment, cela peut être un grand coup de pouce pour la productivité si vous pouvez conditionnellement isoler les informations que vous savez que vous n'aurez pas besoin et ne jamais les consommer en premier lieu.

* Supprimer certains types d'événements des flux d'activité ou des réseaux sociaux.
  
* Supprimer les popups qui vous demandent de faire des choses que vous ne voulez pas.
  
* Supprimer les publications de certains auteurs sur YouTube ou les réseaux sociaux.
  
* Supprimer les distractions ou les éléments dynamiques qui attirent votre attention.
  

## Comment filtrer les éléments HTML

Pour filtrer les éléments, vous pouvez cliquer sur l'icône uBlock Origin en haut de votre navigateur, puis cliquer sur le sélecteur d'éléments, celui avec l'icône de pipette. ([Plus d'informations](https://github.com/gorhill/uBlock/wiki/Element-picker))

![L'interface de uBlock Origin, elle contient toutes les actions qui peuvent être effectuées telles que le blocage des médias, des polices ou des éléments sur la page actuelle.](https://www.freecodecamp.org/news/content/images/2021/08/Untitled.png align="left")

*L'interface de uBlock Origin, cela apparaît si vous cliquez sur l'icône dans la barre d'outils de votre navigateur.*

Vous pouvez commencer par sélectionner le contenu que vous souhaitez supprimer. Même si la sélection n'est pas parfaite, ce n'est qu'un point de départ.

Une fois que la boîte apparaît en bas à droite, vous pouvez utiliser les outils visuels avec le bouton "Pick" et les curseurs, ou spécifier manuellement un sélecteur.

Le contenu mis en surbrillance en rouge est ce qui sera supprimé une fois que vous aurez sélectionné le bouton "Create". Ces modifications persisteront même après l'actualisation ou la réouverture de la page à une date ultérieure. Voyons comment cela fonctionne.

### Sélecteurs CSS

Vous pouvez supprimer la plupart des éléments que vous souhaitez supprimer facilement en utilisant des sélecteurs CSS. C'est idéal pour supprimer le contenu statique de la page.

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-93.png align="left")

*Supprime tous les événements de publication et de push de mon flux d'activité GitHub. (*`##div.news div.release, div.news div.push`)

![Image](https://www.freecodecamp.org/news/content/images/2021/08/image-85.png align="left")

*Supprime la bannière pour télécharger Slack. (*`##.p-client__banners`)

### XPath

Vous voudrez généralement utiliser XPath pour l'une des deux raisons suivantes :

* Vous devez vérifier la valeur d'un élément.
  
* Vous devez sélectionner un élément en fonction des attributs de ses enfants.
  

Cela est utile pour supprimer du contenu dynamique ou généré par les utilisateurs. Nous voulons supprimer l'élément entier, mais seulement si quelque chose à l'intérieur correspond aux critères plutôt que l'élément lui-même.

![Utilisation de l'outil de filtre cosmétique uBlock Origin pour mettre en surbrillance tous les éléments qui seraient supprimés de ma sélection actuelle.](https://www.freecodecamp.org/news/content/images/2021/08/image-57.png align="left")

*Supprime tous les plugins de DevilBro. (*`##:xpath(//a[./div/div/p/object/a = "DevilBro"])`)

![Utilisation de l'outil de filtre cosmétique uBlock Origin pour supprimer tous les éléments que je ne veux pas voir. Le site s'affiche maintenant comme s'ils n'avaient jamais été là.](https://www.freecodecamp.org/news/content/images/2021/08/image-58.png align="left")

*À quoi cela ressemble après avoir supprimé tous les plugins de DevilBro.*

### Dépannage de vos filtres

Lors du filtrage des éléments, vos sélecteurs peuvent cesser de fonctionner à tout moment. Les sites web changent pour diverses raisons, dans la plupart des cas en raison de la maintenance ou des mises à jour.

Ne laissez pas cela vous décourager de faire ce que vous voulez, cependant. Cela signifie simplement que vous devez garder cela à l'esprit lorsque vous supprimez des éléments.

Essayez de garder vos sélecteurs locaux à ce que vous voulez réellement supprimer, mais suffisamment stricts pour qu'ils ne sélectionnent pas faussement d'autres éléments sur la page.

Il existe également de nombreux sites web qui n'apprécient pas les modifications côté client et tentent de les entraver en changeant arbitrairement les valeurs des attributs HTML ou en les obfuscant.

Dans ces cas, il est préférable de spécifier des [sélecteurs d'attributs CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors) ou d'utiliser XPath pour faire correspondre partiellement les valeurs des attributs.

![Sélection de la vue "Active Now" sur Discord en utilisant un sélecteur d'attributs CSS. Le composant "Active Now" est mis en surbrillance en rouge pour indiquer qu'il sera supprimé.](https://www.freecodecamp.org/news/content/images/2021/08/image-91.png align="left")

*Suppression de la vue "Active Now" sur Discord en utilisant un sélecteur d'attributs, (*`##div[class^="nowPlayingColumn"]`)

### Comment supprimer les filtres

Si vous ne souhaitez plus bloquer quelque chose, ou si le site web a changé, vous pouvez aller dans les paramètres pour supprimer l'ancien filtre avant d'en créer un nouveau.

Pour supprimer un filtre personnalisé :

1. Accédez aux paramètres de uBlock Origin.
  
2. Sélectionnez l'onglet "My filters".
  
3. Supprimez les lignes avec le ou les filtres que vous souhaitez supprimer.
  
4. Cliquez sur "Apply changes" en haut.
  
5. Actualisez la page sur laquelle vous étiez.
  

## Autres extensions de navigateur utiles

Il existe d'autres extensions que vous pouvez utiliser pour supprimer des types spécifiques de contenu sur les sites web, également.

### Mettre en surbrillance ou masquer les résultats des moteurs de recherche

[Highlight or Hide Search Engine Results](https://github.com/pistom/hohser) (HOHSER) prend en charge tous les principaux moteurs de recherche, y compris [DuckDuckGo](https://duckduckgo.com/) et Google.

Je pense que la liste noire de domaines devrait être un paramètre utilisateur natif disponible dans les moteurs de recherche, mais jusqu'à ce que ce soit le cas, vous pouvez utiliser cette extension pour masquer les résultats sous les domaines que vous n'aimez pas.

* Sites web avec des liens de téléchargement réhébergés ou douteux.
  
* Contenu optimisé pour les moteurs de recherche, comme les faux sites de coupons.
  
* Sites web qui bloquent les utilisateurs dans l'UE.
  

### I still don't care about cookies

[I still don't care about cookies](https://github.com/OhMyGuus/I-Still-Dont-Care-About-Cookies) supprime les avertissements de cookies de la plupart des sites web, afin que vous n'ayez pas à vous en occuper vous-même.

L'extension tentera de masquer le message de cookies, n'acceptant les cookies que si nécessaire.

Je recommande fortement d'utiliser cela uniquement en combinaison avec des extensions comme uBlock Origin et Privacy Badger, pour empêcher les cookies indésirables d'être enregistrés.

## Conclusion

J'espère que vous n'êtes pas dans une situation où vous sentez le besoin de bloquer une quantité significative de contenu des pages que vous chargez.

Mais si vous en ressentez le besoin, j'espère que cela rend la navigation sur Internet un peu plus supportable pour vous.