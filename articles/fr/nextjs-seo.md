---
title: SEO Next.js pour les développeurs – Comment créer des applications hautement
  performantes avec Next
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2023-03-20T21:17:55.000Z'
originalURL: https://freecodecamp.org/news/nextjs-seo
coverImage: https://www.freecodecamp.org/news/content/images/2023/03/pexels-andrei-photo-2127783.jpg
tags:
- name: Next.js
  slug: nextjs
- name: performance
  slug: performance
- name: SEO
  slug: seo
- name: web performance
  slug: web-performance
seo_title: SEO Next.js pour les développeurs – Comment créer des applications hautement
  performantes avec Next
seo_desc: 'By Scott Gary

  Next.js is a popular React-based web framework that has gained popularity and a
  growing community in recent years. It''s a powerful tool for building fast and SEO-friendly
  web applications with dynamic pages that work great on mobile dev...'
---

Par Scott Gary

Next.js est un Framework web populaire basé sur React qui a gagné en notoriété et vu sa communauté grandir ces dernières années. C'est un outil puissant pour créer des applications web rapides et optimisées pour le SEO, avec des pages dynamiques qui fonctionnent parfaitement sur les appareils mobiles.

En raison de la nature complexe de la conception de systèmes isomorphes, le SEO de Next.js peut être un sujet délicat à appréhender. Surtout si vous venez d'applications React traditionnelles et que vous vous fiez uniquement à la documentation.

Grâce à son support intégré pour le rendu côté serveur (SSR), la génération de sites statiques (SSG) et maintenant les React Server Components, Next.js offre une plateforme robuste pour atteindre des métriques SEO de qualité dans votre application web. Il vous aide également à offrir des expériences utilisateur exceptionnelles sur plusieurs pages dans les applications Node et React tout en les rendant adaptées au SEO.

## Pourquoi devriez-vous apprendre Next.js pour le développement Front-End ?

En résumé, la plus récente version de Next.js est une plateforme open source qui résout de nombreux problèmes de rendu que React rencontre actuellement. J'ai écrit cet article parce que beaucoup de développeurs front-end se fâchent contre moi :-D.

Ils passent 6 à 9 mois à développer une application React, puis je dois leur demander de refactoriser leur code.

Next.js évite de nombreux problèmes de rendu – il permet aux moteurs de recherche de comprendre très facilement le sujet de votre site web.

### À qui s'adresse cet article ?

Ceci vous sera très utile si vous êtes un marketeur ou un développeur plus avancé rencontrant des problèmes de SEO.

Cependant, les nouveaux développeurs sont également invités à consulter ces informations, car elles vous aideront sur le long terme.

## Comment devriez-vous rendre votre application Web Next.js ?

J'ai personnellement examiné une tonne de ces sites via mon cabinet de conseil [OhMyCrawl](https://www.ohmycrawl.com/) et j'ai réalisé une vidéo de présentation pour aider à comprendre les avantages de l'utilisation de frameworks tels que Next.js pour le SEO :

%[https://youtu.be/U8V0rk5AwBU]

## En quoi le SEO de Next est-il différent des autres Frameworks ?

Next SEO se distingue en regroupant de nombreuses fonctionnalités et outils gratuits dans un ensemble bien organisé que vous pouvez facilement assimiler et appliquer à vos applications monopages (SPA). Next fait un excellent travail pour des tâches telles que l'optimisation pour les moteurs de recherche, l'optimisation des images et la réduction du Cumulative Layout Shift (CLS).

Les avantages du SEO avec Next.js ne s'arrêtent pas là. Nous allons aborder de nombreux atouts que Next.js apporte aux moteurs de recherche, qu'ils soient anciens ou récents.

## Les concepts de moteurs de recherche, SSR et SSG évoluent

La plupart des développeurs et experts SEO sont devenus assez familiers avec les stratégies de création de pages existantes et le paradigme SSR vs SSG. Ils ont également développé une grande confiance en la version 12 de Next.js, qui offre une manière claire de gérer ces deux formes de génération de pages.

Comme d'habitude, un nouveau changement de paradigme est en cours, cette fois sous la forme des React Server Components (RSCs), qui sont inclus par défaut dans la version 13 de Next.js.

### Les concepts SEO n'ont pas changé – juste l'approche

Le SEO Next.js ne changera pas beaucoup conceptuellement. Si vous recherchez de bons résultats dans les moteurs de recherche et du trafic organique, le jeu tourne toujours autour des notions de chargement de page rapide, de rendus rapides (paints), d'un faible Cumulative Layout Shift, et tout le reste. Les pages statiques jouent toujours un rôle majeur également.

Mais Next.js nous offre des fonctionnalités inédites et intéressantes qui facilitent l'obtention d'excellentes métriques SEO, et c'est bien plus que les seuls React Server Components.

Nous explorerons quelques meilleures pratiques ainsi que différentes techniques et stratégies pour obtenir d'excellentes métriques d'optimisation SEO avec Next.js. Nous verrons également comment tirer parti de ses fonctionnalités uniques pour améliorer la visibilité de votre site sur les moteurs de recherche et l'engagement des utilisateurs.

## Quelles sont les nouveautés de Next.js 13 liées au SEO ?

Plutôt que de vous donner un guide complet des changements techniques de la version 13, nous allons nous concentrer principalement sur les avantages liés au SEO de Next.js. Nous verrons également comment vous pouvez exploiter les meilleures pratiques SEO pour obtenir les meilleurs résultats possibles dans les moteurs de recherche avec beaucoup moins d'efforts que d'habitude.

Les changements de la version 13 que nous aborderons ici sont les suivants :

* React Server Components
* Streaming de morceaux d'UI
* Mise à jour du composant Next Image
* Composant Next Font

En plus des propriétés SEO par défaut de Next, ces mises à jour particulières sont la pierre angulaire des améliorations SEO de Next.js dans la version 13. Chacune est impressionnante pour ses propres raisons, que nous allons détailler sous peu.

### React Server Components

Les RSCs permettent une approche plus granulaire du rendu, tant sur le client que sur le serveur.

Plutôt que d'être contraint de décider s'il faut rendre une page entière sur le client ou le serveur lors des requêtes des utilisateurs, React permet aux développeurs de choisir si les composants doivent être rendus sur le serveur ou le client. Cela peut vous donner un avantage considérable dans les pages de résultats des moteurs de recherche.

Une grande majorité de l'optimisation des pages repose aujourd'hui sur l'envoi de moins de JavaScript au client. Après tout, c'est l'avantage principal de l'utilisation du pré-rendu et du rendu côté serveur pour créer des pages web et des pages HTML.

Les RSCs sont un outil supplémentaire pour atteindre cet objectif et tirer le maximum de valeur SEO de vos pages web ou applications monopages. Cela aide à obtenir un meilleur SEO en rafraîchissant les données dynamiques dans un composant React tout en laissant intactes les parties statiques du contenu de la page.

### Streaming de morceaux d'UI

Le SEO Next.js a fait un bond de géant en ajoutant les RSC au mélange, et le streaming de morceaux d'UI est la cerise sur le gâteau. L'UI en streaming est une variante d'un nouveau modèle de conception en pleine croissance appelé "l'architecture en îlots" (island architecture), qui s'efforce d'envoyer le moins de code possible au client lors du premier chargement.

Permettre un contrôle granulaire est excellent, mais pourquoi ne pas envoyer une page entièrement rendue et sans JavaScript au client, puis envoyer le reste plus tard ? C'est exactement ce que permet le streaming de morceaux d'UI.

Lorsque Next.js rend une page sur le serveur, la page arrive généralement avec tout le JavaScript regroupé et envoyé avec elle. La capacité de streamer des morceaux de données élimine ce besoin et permet d'envoyer une page statique extrêmement légère au client, améliorant considérablement les métriques web telles que le First Contentful Paint et la vitesse globale de la page.

### Répertoire App de Next.js 13

Lorsque vous démarrez un nouveau projet Next.js 13, vous remarquerez un nouveau répertoire appelé **app**. Tout ce qui se trouve dans le répertoire app est préconfiguré pour permettre les RSCs et le streaming d'UI. Il vous suffit de créer un composant [loading.js](https://beta.nextjs.org/docs/routing/loading-ui), qui enveloppera entièrement la page et tous les enfants dans une frontière de suspense.

Vous pouvez obtenir un modèle de chargement *encore plus* granulaire en créant manuellement les frontières de suspense vous-même, ce qui permet un contrôle illimité sur ce qui est chargé lors de la requête initiale.

Les étapes du streaming de morceaux d'UI ressemblent à ceci :

1. L'utilisateur effectue la requête initiale.
2. Une page HTML minimale est rendue et envoyée au client.
3. Les bundles JavaScript sont en cours de préparation sur le serveur.
4. Une section de la page nécessitant du JavaScript devient visible dans le navigateur du client.
5. Le bundle JavaScript pour ce composant uniquement est envoyé au client.

Ce nouvel outillage a des implications importantes pour le SEO technique en permettant à des pages plus interactives de rivaliser avec des pages statiques en ce qui concerne la vitesse de chargement et d'autres métriques web utilisées comme facteurs de classement dans les résultats de recherche.

### Mise à jour du composant Next Image

Une autre mise à jour importante dans la sphère SEO de Next.js est le composant Image. Bien qu'il ait été quelque peu sous-estimé, l'amélioration la plus importante selon moi est l'utilisation du chargement différé (lazy loading) natif.

Les navigateurs supportent très bien le lazy loading natif depuis un certain temps, et inclure du JavaScript supplémentaire pour cette fonctionnalité est simplement un gaspillage de bande passante.

Quelques autres améliorations notables pour le SEO :

* Balise alt obligatoire par défaut.
* Meilleure validation pour identifier les erreurs liées aux propriétés invalides.
* Plus facile à styliser grâce à une interface plus proche du HTML.

Dans l'ensemble, le nouveau composant Image est simplifié et allégé, et dans le monde de la programmation, plus c'est simple, mieux c'est.

### Le composant Next Font

Le composant font est une grande victoire pour le SEO Next.js, et il aidera certainement à soulager de nombreux maux de tête à l'avenir. Tout développeur expérimenté sait à quel point il peut être fastidieux de configurer correctement les polices (le terme "correctement" n'est pas relatif dans ce cas !).

Les décalages de mise en page cumulatifs dus à un chargement lent sont une nuisance courante, et les moteurs de recherche comme Google ont [ouvertement déclaré](https://developers.google.com/publisher-tag/guides/minimize-layout-shift) que le CLS est une métrique web importante.

Selon le framework avec lequel vous travaillez (Gatsby me vient à l'esprit), il peut être difficile de précharger vos polices efficacement. Faire des requêtes externes vers des dépôts de polices tels que Google a été un mal nécessaire pendant un certain temps, créant un goulot d'étranglement difficile à gérer dans de nombreuses applications SPA.

Le composant Next Font vise à résoudre ce problème en récupérant toutes les polices externes au moment de la construction (build time) et en les auto-hébergeant sur votre propre domaine. Les polices sont également optimisées automatiquement, et un décalage de mise en page cumulatif nul est atteint grâce à l'utilisation automatique de la propriété CSS **size-adjust**.

## Tâches courantes liées au SEO avec Next.js

Il y a quelques sujets importants à considérer lors de la configuration des tâches SEO courantes de Next.js pour la version 13.

### SEO Next.js avec la version 13

La version précédente du composant React Head a généralement été utilisée pour attribuer des valeurs aux balises meta dans l'en-tête du document et aussi pour injecter des données structurées.

Avec la version 13, cependant, le composant Head disparaît. Dans un premier temps, Next a choisi d'utiliser un fichier spécial appelé **head.js** qui fonctionne de manière similaire au composant Head. Après la version 13.2, Next a implémenté le composant **Metadata**, qui est une implémentation plus propriétaire pour résoudre le problème des métadonnées en remplissant facilement les balises meta.

Examinons de plus près ces deux tâches SEO courantes et voyons comment elles étaient gérées auparavant par rapport à la nouvelle méthode de la version 13.

## Comment configurer la balise Head pour l'optimisation des moteurs de recherche

Avant la version 13, nous importions le composant **Next/Head** et définissions toutes les valeurs de métadonnées nécessaires telles que le titre, la description ou d'autres balises meta dans le fichier html de la page web.

Un exemple simple du composant Head dans la version 12 ressemble à ceci :

```js
import Head from 'next/head'
const structData = {
'@context': 'https://schema.org',
'@type': 'BlogPosting',
headline: 'Apprendre le SEO Next.js',
description: 'Tout sur les fonctionnalités de Next.js et plus encore',
author: [
{
'@type': 'Person',
name: 'Jane Doe',
},
],
datePublished: '2023-02-16T09:00:00.000Z',
};
function IndexPage() {
return (
<div>
<Head>
<meta name="viewport" content="initial-scale=1.0, width=device-width" />
<title>Mon titre de page</title>
<script
key="structured-1"
type="application/ld+json"
dangerouslySetInnerHTML={{ __html: JSON.stringify(structData) }}
/>
</Head>
<p>Bonjour le monde !</p>
</div>
)
}
export default IndexPage
```

L'ajout de données structurées telles que le titre et la description ou toute balise meta supplémentaire dans les métadonnées d'une page est une simple question d'inclusion d'une balise script avec l'attribut **dangerouslySetInnerHTML**, comme on le voit dans l'exemple.

La plupart des développeurs codent un composant SEO qui utilise le composant Head afin d'adopter une approche plus DRY (don't repeat yourself). Ici, vous évitez que les mêmes données ou fichiers HTML ne soient envoyés plusieurs fois à l'utilisateur. Mais sous le capot, c'est la même chose, et Head était l'approche de référence pour optimiser une page web en ce qui concerne les balises meta.

### Le fichier spécial head.js de Next

Avec la version 13, vous pouvez oublier le composant Head habituel. À partir de la première itération de la version 13, Next a implémenté le fichier **head.js (ou .tsx)**. Ce fichier peut être inclus dans n'importe quel dossier à l'intérieur du répertoire app pour gérer dynamiquement les métadonnées SEO et déclarer quelles balises, avec leurs valeurs, seront utilisées pour une route et une page particulières.

Chaque dossier du répertoire app correspond à une nouvelle route, c'est pourquoi vous devrez créer un fichier **head.js** dans chaque dossier pour configurer vos valeurs de métadonnées. Voici un exemple de fichier **head.js** :

```js
export default function Head(params) {
return (
<>
<title>Exemple head.js</title>
</>
);
}
```

Remarquez que nous retournons un fragment React plutôt qu'une balise head réelle ou tout autre élément. C'est un aspect requis du composant **head.js**.

Vous ne pouvez retourner que les balises de métadonnées suivantes depuis le fragment : <title>, <meta>, <link> (avec l'attribut precedence) ou <script> (avec l'attribut async).

Next n'a jamais totalement finalisé ce composant, c'est pourquoi la plupart des développeurs ont concocté des implémentations personnalisées pour ajouter des données structurées au mélange. Bien que, un peu plus tard, Next ait commencé à recommander que les données structurées soient ajoutées directement dans le composant de mise en page (layout) ou de page, ce que nous verrons un peu plus loin.

Ce composant est devenu obsolète dans la version 13.2, et l'équipe Vercel est passée au composant **Metadata**.

### Le composant Metadata de Next

Avec la sortie de la version 13.2, Next a décidé d'abandonner complètement le composant head au profit du composant **Metadata**.

Au moment d'écrire ces lignes, il n'y a pas énormément de documentation avec des exemples d'utilisation. En fait, la 13.2 n'est pas encore officiellement sortie, et nous n'en sommes qu'à la version 13.1.7-canary.

Néanmoins, Next propose un bon résumé dans sa documentation, nous allons donc passer en revue l'utilisation et en donner une analyse de base. Il est important d'être informé à ce sujet si vous prévoyez d'être à la pointe du SEO Next.js, car cela arrive bientôt.

Le composant Metadata vise à être le guichet unique pour remplir la balise **head** avec le titre, la description et d'autres métadonnées dynamiques de manière efficace et facile à utiliser. L'utilisation est vraiment simple et consiste à exporter soit un objet appelé **metadata**, soit une fonction appelée **generateMetadata** depuis le composant de page lui-même.

Jetons un coup d'œil à un exemple d'utilisation basique :

### Exemple d'exportation de métadonnées Next.js

**examplePage.tsx**

```js
import type { Metadata } from 'next';
export const metadata: Metadata = {
title: 'Exemple de composant',
description: 'Apprendre le SEO Next.js',
};
export default function Page() {
return (
<>
<div>Exemple de composant de page…</div>
</>
)  	
}
```

Cela remplira automatiquement le composant **examplePage.tsx** avec les balises HTML meta appropriées et les valeurs fournies.

Le composant **metadata** offre également un ensemble de balises par défaut, qui définit automatiquement les balises meta **charset** et **viewport** suivantes :

```js
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
```

### Exemple d'exportation de generateMetadata Next.js

Dans de nombreuses applications, en particulier le e-commerce, vous aurez besoin de remplir dynamiquement les balises meta et de vous assurer que ces données reflètent toujours les modifications apportées à une base de données ou à un autre stockage de données.

Pour de tels cas, Next propose la fonction **generateMetadata**, qui peut être exportée de n'importe quel composant de page avec tous les appels API nécessaires pour récupérer et injecter les données souhaitées.

Voici un exemple de composant de page utilisant cette méthode :

**pageExample.tsx**

```js
import type { Metadata } from 'next';
// Récupérer des informations via une API
async function getInfo(id) {
const res = await fetch(`https://someapi/product/${id}`);
return res.json();
}
export async function generateMetadata({ params }): Promise<Metadata> {
const product = await getInfo(params.id);
return { title: product.title }
}
export default async function Page() {
return (
<div>Exemple de page…</div>
)
}
```

Comme vous pouvez le voir, nous avons créé une méthode qui renvoie des informations sur un produit depuis une API, et nous avons utilisé cette méthode dans notre fonction **generateMetadata** pour remplir ensuite la propriété **title**. Cela définira à son tour la balise title dans notre page HTML rendue.

Il est important de noter que la fonction **generateMetadata** ne peut être utilisée qu'au sein des composants serveur (server components), dont nous avons parlé plus tôt. Rappelez-vous que tous les composants du répertoire **app** sont automatiquement configurés comme composants serveur par défaut.

Pour une liste exhaustive des propriétés et extensions de propriétés disponibles avec le composant **Metadata**, consultez la [documentation](https://beta.nextjs.org/docs/api-reference/metadata). Presque tout ce que vous pouvez imaginer peut être réalisé avec une relative facilité.

## Comment implémenter des données structurées avec Next 13

Next recommande d'ajouter des données JSON-LD structurées au composant de mise en page ou de page. En toute honnêteté, cela a toujours été une solution bien plus simple car Google n'a jamais rien dit contre l'exclusion des données structurées de la page elle-même.

En fait, c'est une pratique courante depuis longtemps, et on ignore pourquoi tant de développeurs se sont focalisés sur l'idée de les placer dans la balise head.

### Comment ajouter des données structurées au composant Layout ou Page

L'ajout de données structurées à un composant, qu'il s'agisse du layout ou de la page, ressemble à ceci (exemple tiré directement de la documentation) :

```js
export default async function Page({ params }) {
const product = await getProduct(params.id);
const jsonLd = {
'@context': 'https://schema.org',
'@type': 'Product',
name: product.name,
image: product.image,
description: product.description
};
return (
<section>
{/* Ajoutez le JSON-LD à votre page */}
<script type="application/ld+json">{JSON.stringify(jsonLd)}</script>
{/* ... */}
</section>
);
}
```

Comme vous pouvez le voir, c'est extrêmement simple, et il n'est vraiment pas nécessaire de compliquer les choses en essayant d'injecter des données structurées dans la balise head.

## SEO Next.js – Conclusion

Nous avons parcouru beaucoup de terrain ici concernant le [SEO Nextjs](https://www.ohmycrawl.com/next-js-seo/). Des nouvelles fonctionnalités incluses dans Next 13 qui visent à résoudre de nombreux problèmes liés au SEO, aux anciennes fonctionnalités repensées et simplifiées pour une meilleure expérience de développement, l'avenir s'annonce radieux pour Next.

Si vous prévoyez d'utiliser Next.js comme framework de choix, je vous recommande vivement d'expérimenter la version 13. Bien que des fonctionnalités telles que le composant Font soient encore en bêta, et que l'ensemble soit encore en phase de test (canary), une grande partie de la version 13 est déjà considérée comme stable et utilisée par de nombreux développeurs et les plus grandes entreprises mondiales.

Les mises à jour majeures peuvent être intimidantes, mais assurez-vous de lire la documentation complète et de faire des essais afin de rester à la pointe du SEO Next.js.