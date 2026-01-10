---
title: Comment optimiser les applications Web Next.js pour de meilleures performances
subtitle: ''
author: Ayantunji Timilehin
co_authors: []
series: null
date: '2025-01-02T14:30:59.606Z'
originalURL: https://freecodecamp.org/news/optimize-nextjs-web-apps-for-better-performance
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1735828217839/b65374be-d891-4f19-a359-f84f2ac8f3b9.png
tags:
- name: Next.js
  slug: nextjs
- name: Web Development
  slug: web-development
- name: web performance
  slug: web-performance
- name: JavaScript
  slug: javascript
- name: web
  slug: web
- name: Performance Optimization
  slug: performance-optimization
- name: React
  slug: reactjs
- name: optimization
  slug: optimization
seo_title: Comment optimiser les applications Web Next.js pour de meilleures performances
seo_desc: As engineers, we often get so carried away with other aspects of development
  that we overlook how users perceive and interact with our applications. This oversight
  can result in users leaving the app almost as soon as they arrive, leading to higher
  b...
---

En tant qu'ingénieurs, nous sommes souvent tellement absorbés par d'autres aspects du développement que nous négligeons la manière dont les utilisateurs perçoivent et interagissent avec nos applications. Cette négligence peut entraîner le départ des utilisateurs presque dès leur arrivée, ce qui se traduit par des taux de rebond plus élevés et une faible engagement.

Au cœur de toute entreprise, il y a la volonté de fournir de la valeur aux utilisateurs. Lorsque les utilisateurs ne peuvent pas accéder à cette valeur en raison de mauvaises performances, cela impacte finalement le succès de l'entreprise. Les temps de chargement lents, entre autres facteurs, frustrent les utilisateurs et les poussent à quitter avant même d'avoir eu la chance de s'engager.

L'optimisation des performances n'est pas seulement un détail technique – c'est aussi une partie cruciale de la création d'une application réussie. Sans elle, même les meilleures fonctionnalités peuvent passer inaperçues si les utilisateurs ne restent pas assez longtemps pour les voir.

Dans cet article, nous explorerons les approches clés pour optimiser votre application Next.js, la rendant plus rapide et plus efficace.

## Table des matières

* [Construire une application performante](#heading-construction-dune-application-performante)
    
* [Comment optimiser vos applications](#heading-comment-optimiser-vos-applications)
    
* [Techniques clés pour optimiser les performances](#heading-techniques-cles-pour-optimiser-les-performances)
    
    * [Utilisation du composant Image de Next.js](#heading-1-utilisation-du-composant-image-de-nextjs)
        
    * [Optimisation des scripts tiers avec le composant Script de Next.js](#heading-2-optimisation-des-scripts-tiers-avec-le-composant-script-de-nextjs)
        
    * [Supprimer les packages/dépendances inutilisés](#heading-3-supprimer-les-packagesdependances-inutilises)
        
    * [Mise en cache et régénération statique incrémentielle (ISR)](#heading-4-mise-en-cache-et-regeneration-statique-incrementielle-isr)
        
    * [Mise en cache du contenu fréquemment utilisé](#heading-mise-en-cache-du-contenu-frequemment-utilise)
        
    * [Optimisation des polices avec next/font](#heading-5-optimisation-des-polices-avec-nextfont)
        
    * [Chargement paresseux et division de code](#heading-6-chargement-paresseux-et-division-de-code)
        
    * [Chargement paresseux dans Next.js](#heading-chargement-paresseux-dans-nextjs)
        
    * [Division de code](#heading-division-de-code)
        
* [Conclusion](#heading-conclusion)
    

## Construire une application performante

Rendre vos applications plus performantes signifie trouver le bon équilibre entre vitesse, réactivité et utilisation efficace des ressources. Vous devez vous efforcer de créer une application qui offre de la valeur et garde les utilisateurs satisfaits.

Construire une application performante consiste à s'assurer que l'application est fluide et intuitive, afin qu'il n'y ait pas de retards frustrants lorsque l'utilisateur clique sur des boutons, fait défiler ou navigue. Vous voudrez également vous assurer que les données se chargent ou se mettent à jour sans délais inutiles.

## Comment optimiser vos applications

La première étape pour optimiser votre application consiste à identifier les zones problématiques. Plusieurs outils et packages peuvent vous aider à analyser efficacement les performances de votre application. Voici comment vous pouvez les utiliser :

### Utilisation de `npm run build`

Lorsque vous exécutez `npm run build`, Next.js crée une version prête pour la production de votre application et fournit une analyse détaillée de vos pages. Cela inclut :

* **Taille** : La taille des fichiers JavaScript pour chaque route. Mettre en évidence les routes trop volumineuses qui pourraient ralentir les choses. Des tailles de page plus petites entraînent généralement des temps de chargement plus rapides, tandis que les grandes pages peuvent prendre plus de temps à télécharger, surtout pour les utilisateurs avec des connexions réseau plus lentes.
    
* **First Load Js** : Cette colonne fournit des informations sur la quantité totale de JavaScript que le navigateur doit télécharger et exécuter pour rendre complètement la page pour la première fois. Des valeurs élevées de **First Load JS**
    
    provoquent un temps plus lent jusqu'à l'interactivité (TTI).
    

L'exécution de cette commande produit une analyse comme ci-dessous :

![Exemple de résultat de l'exécution de npm run build](https://cdn.hashnode.com/res/hashnode/image/upload/v1734639730677/cfd1f858-a9df-4e6c-af28-454857309156.png align="center")

### Utilisation de `@next/bundle-analyzer`

Le [bundle analyzer](https://www.npmjs.com/package/@next/bundle-analyzer) est un package fourni par Next.js pour analyser la taille des bundles JavaScript en fournissant une représentation visuelle des modules et dépendances de l'application. Voici comment utiliser le package :

Tout d'abord, installez le package en exécutant cette commande :

```bash
npm install @next/bundle-analyzer
```

Ou vous pouvez utiliser yarn :

```bash
yarn add @next/bundle-analyzer
```

Ensuite, ajoutez la configuration `@next/bundle-analyzer` à votre fichier `next.config.js` :

```javascript
const withBundleAnalyzer = require('@next/bundle-analyzer')({
  enabled: process.env.ANALYZE === 'true',
});

module.exports = withBundleAnalyzer({
  // autres options de configuration de Next.js ici
});
```

Pour analyser les bundles de votre application tout en générant une version de production, exécutez la commande suivante :

```bash
ANALYZE=true npm run build
```

Pour un guide étape par étape sur l'utilisation efficace de l'analyseur de bundles, consultez ce [tutoriel vidéo détaillé](https://www.youtube.com/watch?v=EIGmcxwbbZw).

### Outils du navigateur

Enfin, les navigateurs modernes, y compris Google Chrome, Firefox et Edge, offrent des outils puissants pour analyser et améliorer les performances de votre application. Des fonctionnalités comme l'onglet Performance vous aident à enregistrer et visualiser le fonctionnement de votre application, en identifiant des problèmes comme le rendu lent ou les tâches longues.

Vous pouvez également utiliser des outils comme Lighthouse (disponible dans Chrome et Edge) pour générer des audits automatisés, mettant en évidence des problèmes tels que les actifs volumineux et les ressources non optimisées.

Pour accéder aux onglets **Lighthouse** et **Performance** :

1. Ouvrez les outils de développement de votre navigateur en cliquant avec le bouton droit n'importe où sur le navigateur et en sélectionnant l'option **Inspecter** ou en appuyant sur **Command + Option + I** (sur Mac) ou **Ctrl + Shift + I** (sur Windows).
    
2. Regardez le menu supérieur dans les outils de développement.
    
3. Si vous ne voyez pas les onglets **Lighthouse** ou **Performance** immédiatement, cliquez sur la **double flèche droite (&gt;&gt;)** pour révéler les onglets cachés.
    
4. Sélectionnez l'onglet souhaité pour commencer à analyser les performances ou générer un rapport Lighthouse.
    

Voici un exemple d'audit généré dans l'onglet Performance sur Chrome

![image de l'onglet performance sur le navigateur chrome](https://cdn.hashnode.com/res/hashnode/image/upload/v1735616911745/e5f09934-df99-40fc-b194-a292a21a4517.png align="center")

Voici une autre image montrant l'audit généré par lighthouse

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1735617075187/dfde608b-eeb7-443d-81c6-56ff2a6dd92b.png align="center")

## Techniques clés pour optimiser les performances

### 1.) Utilisation du composant `Image` de Next.js

Les images représentent souvent la plus grande partie du poids d'une page, affectant directement les temps de chargement et l'expérience utilisateur. Les grandes images ralentissent le rendu et augmentent finalement l'utilisation de la bande passante.

Next.js dispose d'un composant `Image` intégré qui optimise automatiquement les images, ce qui le rend très utile pour les performances web. Il s'occupe du redimensionnement, du chargement paresseux et de l'optimisation du format, de sorte que les images sont servies dans le format le plus performant (comme .WebP) lorsque le navigateur le supporte.

```javascript
import Image from 'next/image';

    <Image
      src="/house.jpg"
      alt="Image de maison"
      width={700}
      height={500}
      priority={false} // Charge paresseusement l'image par défaut
    />
```

Dans l'extrait ci-dessus,

* `src="/house.jpg"` : Cela pointe vers l'emplacement du fichier image, qui se trouve dans le dossier `public`. Les images dans le répertoire `/public` sont servies statiquement, donc vous n'avez pas besoin de configuration supplémentaire.
    
* `alt="Image de maison"` : Le texte `alt` (comme dans l'élément HTML natif `image`) fournit une description de l'image, ce qui est idéal pour l'accessibilité (comme les lecteurs d'écran) et aide également au référencement.
    
* `width & height` : En définissant explicitement la largeur et la hauteur, Next.js peut calculer l'espace que l'image occupera sur la page avant qu'elle ne se charge. Cela empêche le décalage de la mise en page de la page lorsque l'image se charge, ce qui améliore l'expérience utilisateur et booste les métriques de performance comme le [Cumulative Layout Shift](https://blog.hubspot.com/marketing/cumulative-layout-shift) (comme montré dans l'image ci-dessus).
    
* `priority={false}` : Cela garantit que l'image ne se chargera que lorsqu'elle sera proche du viewport de l'utilisateur, économisant la bande passante et améliorant les temps de chargement des pages pour les images non critiques. Cependant, pour les images importantes qui doivent se charger immédiatement (comme celles visibles dès l'ouverture de la page), vous pouvez définir `priority={true}` pour contourner le chargement paresseux et garantir que l'image se charge aussi rapidement que possible.
    

L'un des principaux avantages du composant `Image` de Next.js est sa fonctionnalité de **chargement paresseux** intégrée. Cela signifie que les images ne seront pas chargées tant qu'elles ne sont pas réellement nécessaires (quand elles entrent dans le viewport). En ne chargeant que les images qui sont sur le point d'être vues, les performances sont améliorées et les pages peuvent se charger plus rapidement, même avec de nombreuses images de haute qualité.

### 2.) Optimisation des scripts tiers avec le composant Script de Next.js

Les scripts tiers, tels que les outils d'analyse ou les réseaux publicitaires, peuvent fortement affecter les performances de votre application s'ils ne sont pas correctement gérés. Next.js dispose d'un composant **Script** qui facilite le chargement efficace des scripts, vous donnant le contrôle sur la manière et le moment où ils se chargent.

Le composant `Script` vous permet de définir une **stratégie de chargement** pour les scripts, déterminant quand et comment ils sont récupérés et exécutés. En priorisant ou en différant les scripts en fonction de leur importance, vous pouvez améliorer les performances globales et l'expérience utilisateur de votre application.

* `beforeInteractive`**:** Utilisez cette stratégie pour les scripts qui doivent se charger avant que la page ne devienne interactive, comme les outils d'analyse ou de surveillance essentiels.
    
* `afterInteractive` : Lorsque vous utilisez cette stratégie, le script se charge après que la page est devenue interactive, ce qui est le comportement par défaut. Cela est idéal pour les scripts qui ajoutent des fonctionnalités mais ne sont pas essentiels pour le rendu initial.
    
* `lazyOnload` : Diffère le chargement du script jusqu'à ce que toutes les autres ressources de la page aient terminé de se charger. Cela est parfait pour les scripts non essentiels comme les publicités ou les widgets de réseaux sociaux.
    

```javascript
<Script src="https://example.com/non-essential.js" strategy="lazyOnload" /> // Passez la stratégie en tant que prop au composant
```

En utilisant le composant `Script` de Next.js, vous pouvez empêcher les scripts de bloquer le rendu critique, réduisant ainsi les temps de chargement et améliorant le [Time to Interactive](https://developer.mozilla.org/en-US/docs/Glossary/Time_to_interactive) (TTI).

### 3.) Supprimer les packages/dépendances inutilisés

Au fil du temps, alors que vous construisez et maintenez votre projet, des dépendances inutilisées peuvent s'accumuler dans votre base de code. Ces packages inutiles augmentent la taille de votre projet, ralentissent les temps d'installation et rendent le code plus difficile à maintenir. Nettoyer ces dépendances inutilisées est essentiel pour optimiser les performances de votre application et garder votre base de code propre.

L'outil [depcheck](https://www.npmjs.com/package/depcheck) est un excellent moyen d'identifier et de supprimer les dépendances inutilisées de votre projet. Il analyse votre `package.json` et les fichiers du projet pour trouver les dépendances inutilisées, les devDependencies inutilisées et les dépendances manquantes.

Vous pouvez exécuter un `depcheck` comme ceci :

```bash
npx depcheck
```

Après avoir identifié les dépendances inutilisées, vous pouvez les supprimer en exécutant :

```bash
npm uninstall <package-name>
```

ou avec yarn :

```bash
yarn remove <package-name>
```

Exécuter régulièrement `depcheck` est un moyen simple mais efficace de garder votre projet propre et efficace.

### 4.) Mise en cache et régénération statique incrémentielle (ISR)

Lorsque vous vous retrouvez à exécuter les mêmes calculs ou requêtes de base de données de manière répétée, vous devriez envisager la mise en cache. C'est une méthode simple mais puissante pour améliorer les performances de votre application web, surtout pour le contenu qui ne change pas souvent. En stockant les données fréquemment accédées dans un cache, vous pouvez éviter un traitement inutile et accélérer les temps de chargement.

Dans Next.js, vous pouvez aller plus loin avec la régénération statique incrémentielle (ISR), qui vous permet de servir du contenu statique instantanément tout en le gardant frais en arrière-plan.

**La régénération statique incrémentielle (ISR)** dans Next.js vous permet de mettre à jour des pages statiques sans reconstruire l'ensemble du site. Voici comment cela fonctionne :

1. **Génération au moment de la construction** : ISR génère les pages lorsque le site est construit.
    
2. **Mise en cache** : Il stocke les pages afin qu'elles se chargent rapidement lorsque les utilisateurs les visitent.
    
3. **Mises à jour en arrière-plan** : Lorsque le contenu change, ISR met à jour les pages en arrière-plan sans affecter les utilisateurs.
    
4. **Mises à jour dynamiques** : Il combine le chargement rapide des pages statiques avec la capacité de mettre à jour régulièrement le contenu.
    

```javascript
export async function getStaticProps() {
  
  const data = await fetchData();

  return {
    props: { data },
    // régénère la page toutes les 20 secondes.
    revalidate: 20,
  };
}

// pré-rendre la page en tant que contenu statique
function MyPage({ data }) {
  return (
    <div>
      <h1>Ma Page</h1>
      <p>{data}</p>
    </div>
  );
}

export default MyPage;
```

### Mise en cache du contenu fréquemment utilisé

Pour les sites web avec des pages qui reçoivent beaucoup de visiteurs, comme les listes de produits ou les articles de blog, il est important de garder le contenu rapide et à jour.

La mise en cache aide à atteindre cet objectif en sauvegardant une copie de la page afin qu'elle n'ait pas besoin d'être créée à partir de zéro chaque fois que quelqu'un la visite. Le navigateur ou le serveur stockera cette page mise en cache pendant une durée déterminée, qui est contrôlée par les en-têtes de cache. Pendant ce temps, l'ISR (Régénération Statique Incrémentielle) garantit que la page peut être mise à jour en arrière-plan lorsque cela est nécessaire, sans avoir besoin de reconstruire l'ensemble du site.

Dans les applications avec beaucoup de données, la mise en cache peut également accélérer le processus en stockant les réponses de l'API. Ainsi, lorsque les utilisateurs demandent les mêmes données à nouveau, ils peuvent les obtenir rapidement à partir du cache au lieu d'attendre qu'elles soient récupérées à nouveau. Des outils comme Vercel et les réseaux de diffusion de contenu (CDN) aident en stockant ces pages mises en cache dans plusieurs emplacements à travers le monde, afin que les visiteurs puissent y accéder plus rapidement.

```javascript
export async function getStaticProps() {
  const data = await fetchData();

  return {
    props: { data },
    // Régénère la page au plus une fois toutes les 30 secondes
    revalidate: 30,
    // Cache pendant 1 heure au niveau du CDN
    headers: {
      'Cache-Control': 'public, max-age=3600, must-revalidate',
    },
  };
}
```

Ici, la page se régénère toutes les 30 secondes et est mise en cache au niveau du CDN pendant une heure. L'en-tête `Cache-Control` indique au CDN et au navigateur de mettre en cache la page pendant 1 heure et de la révalider ensuite.

Pour une plongée plus profonde dans la mise en cache et son rôle dans les performances web, consultez cet article perspicace de [freeCodeCamp sur la mise en cache vs les réseaux de diffusion de contenu](https://www.freecodecamp.org/news/caching-vs-content-delivery-network/).

### 5.) Optimisation des polices avec `next/font`

Le module `next/font` dans Next.js gère automatiquement le chargement des polices pour améliorer les performances, donc vous n'avez pas besoin de configurer manuellement ou d'utiliser des bibliothèques supplémentaires. Il charge uniquement les parties essentielles de la police, ce qui entraîne des temps de chargement de page plus rapides.

Pour réduire davantage la taille du fichier de police, vous pouvez fournir le tableau `subsets` qui garantit que moins d'octets sont transférés et que les pages se chargent rapidement.

Voici comment cela fonctionne :

* **Chargement automatique des polices** : Le module optimise automatiquement le chargement des polices, en s'assurant que les polices sont servies de la manière la plus efficace, améliorant les performances sans effort supplémentaire.
    
* **Sous-ensembles de polices** : Vous pouvez spécifier les caractères de police exacts nécessaires pour votre application.
    
* **Stratégie d'affichage des polices** : La stratégie d'affichage des polices détermine comment le texte est affiché à l'utilisateur pendant le chargement des polices. Next.js utilise généralement la stratégie `swap` par défaut, mais vous pouvez la configurer manuellement si nécessaire. Les stratégies les plus courantes sont `swap`, `fallback`, `optional` et `block`.
    
* ```javascript
    import { Inter } from 'next/font/google'
    
    const inter = Inter({
      subsets: ['latin', 'latin-ext'], // Charge uniquement les sous-ensembles Latin et Latin étendu
      weight: '400', // Choisissez le poids spécifique dont vous avez besoin
      style: 'normal', // Spécifiez le style si nécessaire
    })
    
    export default function Page() {
      return <div className={inter.className}>Bonjour le monde</div>
    }
    ```
    

L'extrait ci-dessus utilise l'outil intégré de Next.js pour les polices Google. Au lieu d'ajouter le lien de la police dans votre HTML ou d'utiliser une bibliothèque tierce, vous pouvez l'importer directement comme ceci pour plus de facilité et d'efficacité.

* **subsets** : Indique à l'application de charger uniquement les caractères nécessaires. En sautant d'autres jeux de caractères comme le cyrillique (utilisé en russe) ou le grec, cela évite de télécharger des données supplémentaires et inutiles, ce qui maintient votre application légère et plus rapide à charger.
    
* **weight** : Au lieu de charger tous les poids de police (par exemple, Gras, Léger), vous ne chargez que le Régulier (400). Cela réduit la taille globale.
    
* **style** : Restez avec le style standard (pas d'italique fantaisiste). Cela réduit également ce qui est téléchargé.
    

### 6.) Chargement paresseux et division de code

Lorsque vous construisez des applications web, vous voulez vous assurer que vos utilisateurs n'attendent pas trop longtemps pour que vos pages se chargent. Une grande partie de cela implique de réduire la quantité de JavaScript chargée lorsque la page s'ouvre pour la première fois. Deux techniques qui aident à cela sont le **chargement paresseux** et la **division de code**, que Next.js rend faciles à utiliser.

#### Chargement paresseux dans Next.js

Pensez au chargement paresseux comme à attendre de télécharger un film uniquement lorsque vous décidez de le regarder. Imaginez que vous avez un grand composant comme un graphique ou une carte que les utilisateurs ne voient qu'après avoir interagi avec une page. Au lieu de le charger dès le début, vous pouvez dire à Next.js de le charger uniquement lorsqu'il est nécessaire en utilisant `next/dynamic`.

#### Division de code dans Next.js

La division de code divise votre JavaScript en petits morceaux (appelés bundles), de sorte que les utilisateurs ne chargent que ce qui est nécessaire. Par exemple, si un utilisateur visite votre page d'accueil, il n'est pas nécessaire de charger le JavaScript pour d'autres pages comme "À propos" ou "Tableau de bord". Cela se produit généralement pendant le processus de construction ou dynamiquement à l'exécution.

```javascript
import dynamic from 'next/dynamic'

// Charge HeavyComponent uniquement lorsqu'il est rendu
const HeavyComponent = dynamic(() => import('./HeavyComponent'), { ssr: false })

export default function Home() {
  return (
    <div>
      <h1>Bienvenue à la maison !</h1>
      <HeavyComponent /> {/* Cela se charge uniquement lorsqu'il est rendu */}
    </div>
  )
}
```

Dans le code ci-dessus, `dynamic` importe dynamiquement le composant uniquement lorsqu'il est nécessaire. `ssr: false` désactive le rendu côté serveur pour le composant, ce qui peut économiser des ressources si le composant n'a pas besoin d'être pré-rendu.

Next.js divise automatiquement le code par page, ce qui signifie que chaque page ne charge que le JavaScript nécessaire lorsqu'elle est accédée, améliorant ainsi les temps de chargement. Pour un contrôle plus granulaire, `next/dynamic` vous permet d'importer dynamiquement des composants spécifiques, en vous assurant qu'ils sont chargés de manière paresseuse uniquement lorsqu'ils sont nécessaires. Bien que Next.js gère la division de code au niveau de la page par défaut, l'utilisation de `next/dynamic` vous donne la flexibilité d'appliquer la division de code au niveau des composants, optimisant ainsi le chargement des ressources et améliorant les performances.

## Conclusion

Créer une application haute performance est un aspect très important de toute entreprise. Une application plus rapide et plus efficace améliore l'engagement des utilisateurs, réduit les taux de rebond et booste les classements SEO, ce qui contribue à la croissance de l'entreprise et à la satisfaction des clients.

En utilisant ces techniques que nous avons discutées dans ce guide, vous pouvez offrir une expérience utilisateur fluide tout en maintenant une efficacité optimale en arrière-plan.

Rappelez-vous, chaque seconde économisée dans le temps de chargement se traduit par des utilisateurs plus heureux et, en fin de compte, de meilleurs résultats commerciaux.

Merci d'avoir lu !

Vous voulez entrer en contact avec moi ?

* Twitter / X : [@timi471](https://x.com/Timi471)
    
* Linkedin : [Ayantunji Timilehin](https://www.linkedin.com/in/timilehin-micheal/)
    
* Email : ayantunjitimilehin@gmail.com
    

### Références

* [Documentation Next.Js](https://nextjs.org/docs/pages/building-your-application/optimizing)
    
* [Caching-vs-content-delivery-network](https://www.freecodecamp.org/news/caching-vs-content-delivery-network/)
    
* [Utilisation de next/bundle-analyzer](https://www.youtube.com/watch?v=EIGmcxwbbZw)
    
* [Cumulative layout shift](https://blog.hubspot.com/marketing/cumulative-layout-shift)