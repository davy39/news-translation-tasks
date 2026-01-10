---
title: Comment améliorer les liens intégrés dans React avec Microlinks
subtitle: ''
author: Oluwatobi
co_authors: []
series: null
date: '2024-06-18T02:56:25.000Z'
originalURL: https://freecodecamp.org/news/how-to-enhance-embedded-links-in-react-with-microlinks
coverImage: https://www.freecodecamp.org/news/content/images/2024/06/microl.jpg
tags:
- name: React
  slug: react
seo_title: Comment améliorer les liens intégrés dans React avec Microlinks
seo_desc: The web has evolved from rigid color coding and 2D rendering to an era of
  complex, aesthetically pleasing animations and 3D rendering options. There have
  also been integrations with new technologies, such as virtual reality tools and
  frameworks, to i...
---

Le web a évolué des codes de couleur rigides et du rendu 2D vers une ère d'animations complexes et esthétiques ainsi que des options de rendu 3D. Il y a également eu des intégrations avec de nouvelles technologies, telles que les outils et frameworks de réalité virtuelle, pour améliorer l'expérience utilisateur.

Dans cet article, vous apprendrez à optimiser les liens intégrés dans vos projets de développement front-end pour répondre à vos spécifications souhaitées.

L'inspiration pour cet article est venue d'un problème que j'ai rencontré lors de la création d'un site portfolio et des difficultés à intégrer des sites externes—jusqu'à ce que je découvre un outil efficace pour m'aider.

Pour bien comprendre ce tutoriel, voici quelques prérequis :

* Une bonne connaissance de JavaScript.
* Une familiarité avec React JS et l'installation de packages npm.
* Une maîtrise de CSS.

Commençons !

## Le Concept de Micro-liens

Le micro-lien consiste à intégrer un lien vers un site web externe dans une page web par défaut. Les liens intégrés sont différents des attributs HTML par défaut `alt href` couramment utilisés par les développeurs web.

Ce concept implique également l'extraction des métadonnées pertinentes du site, des informations et des images pertinentes à partir du lien du site externe intégré. Cela contribue à fournir plus d'informations sur le site web externe en question.

Cette fonctionnalité n'est pas nouvelle, car elle est couramment utilisée dans les blogs haut de gamme, les sites de streaming vidéo et les sites de commerce électronique. Cette fonctionnalité est également utilisée par les propriétaires de sites pour personnaliser la manière dont les informations de leur site sont affichées lorsqu'elles sont intégrées dans des sites publicitaires.

## Comment Fonctionnent les Micro-liens ?

Normalement, l'intégration d'une URL à l'aide de code HTML simple ne génère aucun aperçu d'image ou de texte. Cependant, ce n'est pas le cas pour les micro-liens. Cela se produit grâce à l'utilisation d'une interface de programmation d'application pour extraire les informations pertinentes du site référencé, puis les transmettre au développeur au format JSON pour une personnalisation et une utilisation faciles.

Il existe de nombreux services de micro-liens disponibles commercialement. Certains exemples sont [Embedly](https://embed.ly/), le protocole [Open Graph](https://ogp.me/), [microlink.io](https://microlink.io/), et ainsi de suite.

## Introduction au Package Microlink

Dans ce tutoriel, nous allons créer un site qui utilise un package Node connu sous le nom de Microlink pour générer des aperçus. Les détails concernant la personnalisation des URL seront également illustrés.

Cette personnalisation permet aux développeurs d'extraire facilement des aperçus de liens pertinents du site Microlink, en évitant la complexité de l'interaction avec l'interface du site web.

Pour un apprentissage plus approfondi, la bibliothèque dispose d'un site de documentation riche qui peut être consulté [ici](https://microlink.io/docs/sdk/integrations/react).

## Comment Configurer Votre Projet

Pour construire le site d'aperçu des liens, nous allons utiliser l'outil React Vite. En entrant la commande `npm create-vite-app@latest links`, un dossier nommé `latest links` est immédiatement créé, que nous utiliserons pour construire ce projet.

De plus, le package `microlink` doit être installé. Pour ce faire, naviguez vers la ligne de commande et exécutez la commande `npm i @microlinks/react`.

## Projet de Démo

Tout d'abord, nous allons créer le composant fonctionnel JSX par défaut pour ce projet.

```
function App() {
return (
<>
</>
)
}
export default App

```

Ensuite, nous allons importer et initialiser la bibliothèque `microlink` installée :

```
import Microlink from '@microlink/react'

```

Après cela, nous pouvons initialiser le package dans la fonction App :

```
return (
<>
<Microlink
url= " https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview "  />
</>
)

```

L'URL que j'ai incluse est un lien vers un site externe que je souhaite prévisualiser sur mon site local. Cela peut être changé pour n'importe quel site que vous souhaitez prévisualiser.

En exécutant cela, vous devriez voir quelque chose de similaire à ceci.

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro1-1.JPG)
_page web du projet microlink_

  
Nous avons réussi à configurer un micro-lien dans notre application. Mais ce n'est pas tout, la puissance du package est énorme, offrant un niveau de flexibilité dans le contrôle de la mise en page et de la taille des micro-liens.

### Ajustement de la Taille

L'ajustement de la taille consiste simplement à ajuster la taille ou les dimensions d'une variable pour répondre à différentes spécifications. Dans ce cas, nous allons ajuster la taille des liens intégrés.

```
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview" />
<p></p>
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview"  size="small"/>
<p></p>

```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro2.JPG)
_micro-liens de différentes tailles_

Le code ci-dessus spécifie la taille du micro-lien à rendre. Si la taille est indiquée comme étant `small`, la dimension du micro-lien est modifiée. Il permet également des tailles grandes et moyennes, et par défaut, la taille moyenne est celle qui est généralement vue lorsqu'aucune dimension de taille n'est spécifiée.

De plus, la balise auto-fermante `microlink` permet un style CSS. Cela peut être réalisé en incluant la variable de style dans la balise `microlink`.

```
<Microlink
url= "https://tobilyn77.hashnode.dev/nodejs-clustering-and-load-balancing-comprehensive-overview"
style= {{color: 'red'}} />

```

![Image](https://www.freecodecamp.org/news/content/images/2024/06/micro3.JPG)
_micro-lien avec la couleur définie sur rouge_

Comme vous pouvez le voir dans le code ci-dessus, le `microlink` a été stylisé avec la couleur rouge et cela se reflète dans la sortie. D'autres styles CSS peuvent également être appliqués pour donner aux utilisateurs une sensation esthétique de votre site.

## Conclusion

Avec cela, nous arrivons à la fin du tutoriel. Nous espérons que vous avez appris à prévisualiser les liens via le package `microlink`.

N'hésitez pas à poser des questions ou à laisser des commentaires dans la boîte de commentaires ci-dessous. Vous pouvez également interagir avec moi sur mon blog et consulter mes autres articles [ici](https://www.freecodecamp.org/news/p/cedba683-793c-4c78-85d9-c46647c75b71/linktr.ee/tobilyn77). Jusqu'à la prochaine fois, continuez à coder !