---
title: Pourquoi l'utilisation de données structurées aide le référencement de votre
  site web
subtitle: ''
author: Luke Ciciliano
co_authors: []
series: null
date: '2019-08-28T18:21:57.000Z'
originalURL: https://freecodecamp.org/news/using-structured-data-helps-your-websites-seo
coverImage: https://www.freecodecamp.org/news/content/images/2019/08/seo-and-ipad-1.jpg
tags:
- name: schema
  slug: schema
- name: SEO
  slug: seo
- name: structured data
  slug: structured-data
- name: Web Development
  slug: web-development
seo_title: Pourquoi l'utilisation de données structurées aide le référencement de
  votre site web
seo_desc: 'Few things are as exciting for a new developer as getting their first customers.
  The idea of putting one’s new coding knowledge to work can be exhilarating.

  There’s an important thing to remember though, especially if your customer is some
  type of sm...'
---

Peu de choses sont aussi excitantes pour un nouveau développeur que d'obtenir ses premiers clients. L'idée de mettre en pratique ses nouvelles connaissances en codage peut être exaltante.

Il y a cependant une chose importante à retenir, surtout si votre client est une sorte de petite entreprise qui traite avec le public (comme un restaurant, une boulangerie, etc.). Cette chose à retenir est que le client ne se soucie probablement pas du HTML, du CSS ou du JavaScript. Ils se soucient de savoir si le site web performe bien dans les recherches et si des clients viennent dans leur entreprise en conséquence.

Cela signifie que vous devez construire le site web en gardant à l'esprit l'optimisation pour les moteurs de recherche (SEO). L'un des développements majeurs récents dans le domaine du SEO est l'utilisation croissante par Google des "données structurées" dans son analyse des sites web. Cette tendance m'a décidé à écrire cet article sur l'utilisation des données structurées dans vos divers projets web.

Je vais diviser cette discussion en quatre sections. Les domaines que je vais explorer incluent :

1. Qu'est-ce que les données structurées et pourquoi Google s'en soucie-t-il ?
   
2. Comment utiliser les données structurées dans un site web.
   
3. Comment tester vos données structurées et surveiller les erreurs après le lancement du site.
   
4. La nécessité de maintenir vos données structurées à jour après le lancement du site web.
   

C'est une discussion importante à avoir. Je trouve que beaucoup, beaucoup, beaucoup, beaucoup... (beaucoup) de personnes qui se présentent comme des développeurs web ne savent en réalité pas grand-chose (voire rien) sur le SEO.

Je trouve également que beaucoup de personnes qui se présentent comme aidant avec le SEO ne savent en réalité rien sur le développement web (et souvent ne peuvent à peine coder du tout).

Une personne qui peut réellement coder et qui comprend ce que les moteurs de recherche recherchent peut apporter une grande valeur à ses clients. Cette valeur, à son tour, vous aide à gagner plus d'argent en tant que développeur. En d'autres termes, associer une compréhension du SEO à vos compétences nouvellement acquises en développement web peut vous aider à passer de cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Computer-with-help-sign.jpg align="left")

À cela :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/computer-and-money.jpg align="left")

Alors, commençons et discutons de pourquoi les données structurées sont importantes pour le SEO d'un site web.

### Qu'est-ce que les données structurées et pourquoi Google s'en soucie-t-il ?

Les données structurées sont une forme de balisage que vous pouvez appliquer au contenu de votre site web. Ce balisage vous permet de fournir des informations aux moteurs de recherche sur vos pages web et les informations qu'elles contiennent.

Ce balisage est important car les moteurs de recherche, bien qu'ils s'améliorent dans la compréhension du langage naturel, peuvent avoir du mal à comprendre la formulation ou d'autres contenus contenus dans une page web.

Par exemple, si quelqu'un recherche "professionnel pour aider avec l'investissement", les moteurs de recherche peuvent avoir du mal à distinguer les sites qui appartiennent à des gestionnaires d'investissement et les sites qui discutent de la manière de choisir un gestionnaire d'investissement en général (ceci est un exemple très généralisé).

En utilisant des données structurées, vous pouvez aider Google à savoir que votre site web appartient réellement à un gestionnaire d'investissement.

Un autre objectif des données structurées est qu'elles aident les moteurs de recherche à identifier qui est qui sur le web. Supposons, par exemple, que vous réalisiez un site web pour un candidat politique. Le candidat, en plus d'un site web officiel de campagne, a une page Facebook officielle pour la campagne.

Pour des raisons évidentes, il peut y avoir des personnes qui créent de fausses pages Facebook sur le candidat. En incluant certaines données structurées dans le site web, vous pouvez créer un lien relationnel entre la page Facebook officielle et le site web de la campagne. Cela aide les moteurs de recherche à savoir quelle page Facebook est légitime et laquelle est frauduleuse.

Google travaille à identifier qui est qui sur le web depuis environ une décennie. Cela a commencé avec leur réseau social maintenant défunt, Google+ (vous savez... ce réseau social que vous avez peut-être essayé mais sur lequel aucun de vos amis n'était).

Au début de cette décennie, si un site web incluait un lien vers un profil Google+, et que le lien incluait l'attribut "rel=author", le lien informait Google que le site web appartenait au détenteur du profil Google+. C'était quelque chose que Google avait l'intention de renforcer dans la recherche, comme l'un de leurs dirigeants l'a expliqué dans cette vidéo de 2013 :

%[https://www.youtube.com/watch?v=3QlY8ba0jYI] 

Google a abandonné cette approche, principalement en raison des difficultés de Google+, en août 2014. Depuis lors, Google a augmenté son accent sur les données structurées comme moyen d'annoter les informations dans les résultats de recherche et d'identifier qui est qui sur le web.

Donc, en bref, les données structurées sont quelque chose que vous devriez inclure pour ajouter de la valeur à tout site web que vous construisez pour vos clients.

### Comment utiliser les données structurées dans un site web

Les données structurées peuvent être utilisées de plusieurs manières. En plus de les utiliser pour aider à identifier l'individu ou l'entité exploitant le site, vous pouvez les utiliser pour aider Google à mieux comprendre le contenu d'une page.

Si, par exemple, vous avez construit un site web pour une boulangerie, alors il existe des types de balisage que vous pouvez utiliser pour mettre en avant les bonnes critiques de l'entreprise, pour mettre en avant les événements à venir, et ainsi de suite. Ce balisage peut conduire à des mises en avant dans les résultats de recherche qui, à leur tour, rendront votre client (le propriétaire de la boulangerie) heureux.

Regardons quelques exemples de ce à quoi cela ressemble dans la vie réelle, en utilisant un [site web d'agent immobilier](https://www.dayton-real-estate-agent.com/) que j'ai récemment construit (j'inclus le lien au cas où vous voudriez jeter un coup d'œil au code).

L'agent immobilier pour lequel j'ai construit le site web concentre son activité sur les investisseurs. Le site web inclut des données structurées qui informent Google que le site appartient à un véritable agent immobilier. Lorsque je effectue une recherche Google pour "Dayton realtor for investors", les trois premiers résultats organiques que je reçois sont comme montré dans cette photo :

![Image](https://www.freecodecamp.org/news/content/images/2019/08/Investor-search.png align="left")

Le premier résultat est le site web que j'ai construit. Les deux derniers sont des sites web qui n'appartiennent pas à de véritables agents immobiliers, même si c'est ce que je cherchais clairement avec mon terme de recherche. En fait, seul un autre site web d'agent immobilier apparaît même sur la première page des résultats de recherche. Maintenant, je ne dis pas que cela est entièrement dû aux données structurées, mais cela aide certainement.

Le balisage utilisé pour les données structurées est généré/régit par [Schema.org](https://schema.org/). Lorsque vous balisez un site, une page individuelle, un événement ou un produit, il est important d'utiliser autant de balisage que *raisonnablement* possible afin de fournir aux moteurs de recherche des informations pertinentes.

Le site web de Schema.org fournit souvent des exemples de ce à quoi votre balisage devrait ressembler. Le début du balisage que j'ai utilisé pour le site de l'agent immobilier impliquait d'informer Google que le site appartenait à un agent immobilier en plaçant ce qui suit à l'intérieur d'un

:

```html
<itemscope itemtype=http://schema.org/RealEstateAgent>
```

Cela indique aux moteurs de recherche que je m'appuie sur le balisage de schema pour identifier et décrire le site et que le site appartient à un agent immobilier, tel que défini par schema [ici](https://schema.org/RealEstateAgent).

J'ai également pu utiliser des données structurées pour dire à Google que cet agent immobilier a de bonnes critiques en ligne et qu'il travaille à la commission. Cela, à son tour, apparaît maintenant dans les résultats de recherche.

Par exemple, la page au lien suivant est sur la première page de recherche lorsque je cherche [Dayton apartments for sale](https://www.dayton-real-estate-agent.com/apartments-multi-family-homes-for-sale/). (Encore une fois, j'inclus ce lien au cas où vous voudriez regarder le code source du site).

![Image](https://www.freecodecamp.org/news/content/images/2019/08/multifamily-1.png align="left")

Remarquez que les résultats de recherche incluent le fait que c'est un agent immobilier noté cinq étoiles et que le professionnel travaille à la commission ? En d'autres termes, l'utilisation de données structurées aide le site à se démarquer davantage dans les résultats de recherche. Ces informations ont été ajoutées au site avec le balisage suivant :

```html
<div itemprop="aggregateRating" itemscope itemtype="http://schema.org/AggregateRating">
Noté <span itemprop="ratingValue">Note réelle de l'agent immobilier</span> sur <span itemprop="bestRating">Note maximale possible de l'agent immobilier</span> par <span itemprop="ratingCount">Nombre total de critiques</span> clients sur <a href="URL du site où se trouvent les critiques" target="_blank" rel="noopener">Nom du site où se trouvent les critiques</a>
Structure de frais : <span itemprop="priceRange">Commission</span>
</div>
```

Déterminer quelles données structurées utiliser dans un site, ou sur une page particulière, peut être difficile. Heureusement, Google fournit quelques outils qui aident à cela. Regardons ces outils dans la section suivante de cet article.

### Tester vos données structurées et les surveiller après le lancement de votre site

La première étape pour ajouter des données structurées à votre contenu est de déterminer la catégorie dans laquelle il tombe. Vous pouvez le faire en recherchant sur le site web Schema.org, en regardant les données d'autres sites web, ou une combinaison des deux. Une fois que vous avez trouvé la catégorie dans laquelle vous tombez, le reste est assez facile. Restons avec l'exemple de l'agent immobilier ci-dessus.

La première étape consiste à ajouter le balisage de l'agent immobilier, de Schema, au site. Ensuite, entrez votre URL dans [l'outil de test de données structurées de Google](https://search.google.com/structured-data/testing-tool). L'outil vous indiquera quelles données structurées ont été trouvées sur votre site, quelles erreurs vous pouvez avoir, et quelles données structurées sont "suggérées" pour la catégorie que vous avez sélectionnée. Une fois que vous commencez à utiliser cet outil, vous trouverez que vous assurer d'avoir les bonnes informations dans le site web devient assez simple et direct.

De plus, je m'appuie fortement sur les exemples que Schema fournit pour diverses catégories et types de données. L'utilisation de l'outil de test de Google peut vous aider à vous assurer que vous avez les bonnes données dans votre site dès le départ.

Un autre outil important, pour surveiller les erreurs, est [Google Search Console](https://search.google.com/search-console/about). C'est un autre outil de développeur, de Google, qui vous informera lorsque des erreurs de données structurées apparaissent sur votre site web après le lancement. C'est un outil incroyablement utile et si vous soutenez le site web de votre client de manière continue, après le lancement, alors vous devez l'utiliser pour surveiller les choses.

### La nécessité de maintenir vos données structurées à jour après le lancement d'un site web

Il est important de comprendre que vous devrez peut-être revenir en arrière et modifier les anciennes données structurées d'un site après le lancement d'un site. Cela est dû au fait que, comme beaucoup d'autres choses, les normes pour les données structurées changent avec le temps. Par exemple, je construis et maintient des sites web pour des cabinets d'avocats dans le cadre de mon activité principale. Selon les normes précédentes de données structurées, ces sites web étaient balisés avec ce qui suit :

Dans les révisions ultérieures des normes de données structurées, cependant, la classification "Attorney" a été obsolète et changée en "LegalService" – ainsi, j'ai dû changer le balisage sur chaque site web que je gère. Je vous dis cela parce qu'il est important de réaliser que ces normes changent assez souvent. Il est important que vous restiez à jour avec les changements.

### Conclusion

Les résultats web deviennent de plus en plus riches en ce sens qu'ils fournissent plus d'informations qu'un simple lien vers un site web. Il est important pour vos clients que vous balisiez vos pages en conséquence. Faire cela est important pour vos efforts de SEO et pour fournir de la valeur à vos clients. C'est pourquoi il est important d'inclure des données structurées dans vos projets.

### À propos de moi

Je suis un développeur web qui fournit principalement divers types de services aux cabinets d'avocats. Je suis également co-fondateur de [Modern Website Design](https://www.modern-website.design/). J'aime écrire sur des sujets qui aident les développeurs freelances et les petites entreprises à augmenter leurs revenus.