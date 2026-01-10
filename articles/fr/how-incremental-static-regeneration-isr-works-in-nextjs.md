---
title: Comment fonctionne la régénération statique incrémentielle (ISR) dans Next.js
subtitle: ''
author: Joan Ayebola
co_authors: []
series: null
date: '2025-05-01T16:13:41.260Z'
originalURL: https://freecodecamp.org/news/how-incremental-static-regeneration-isr-works-in-nextjs
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1746114577532/94c5118c-f931-415a-932e-45b7e24b99f6.png
tags:
- name: Next.js
  slug: nextjs
- name: JavaScript
  slug: javascript
- name: Web Development
  slug: web-development
seo_title: Comment fonctionne la régénération statique incrémentielle (ISR) dans Next.js
seo_desc: 'When you build a website, you often have two main choices for how pages
  are created: statically or dynamically.

  Static pages are created once when you build your project. They’re fast because
  the server doesn’t have to do any extra work when someone ...'
---

Lorsque vous construisez un site web, vous avez souvent deux choix principaux pour la création des pages : de manière statique ou dynamique.

Les pages statiques sont créées une fois lors de la construction de votre projet. Elles sont rapides car le serveur n'a pas besoin de faire de travail supplémentaire lorsqu'un utilisateur visite la page.

Les pages dynamiques sont créées à la volée. Chaque fois qu'un utilisateur demande une page, le serveur la construit à nouveau. Cela peut être plus lent, mais cela signifie que le contenu est toujours à jour.

Les deux options ont des avantages et des inconvénients. Les pages statiques sont très rapides, mais elles peuvent afficher un contenu obsolète si quelque chose change après la construction. Les pages dynamiques sont toujours fraîches, mais elles peuvent être lentes car le serveur doit travailler plus dur.

C'est là qu'intervient la régénération statique incrémentielle (ISR). L'ISR vous offre le meilleur des deux mondes : la vitesse des pages statiques avec la fraîcheur des pages dynamiques.

Dans cet article, nous allons explorer ce qu'est l'ISR, comment elle fonctionne dans Next.js, et comment vous pouvez l'utiliser pour rendre vos sites web plus rapides et plus intelligents.

## Table des matières

1. [Qu'est-ce que la régénération statique incrémentielle (ISR)](#heading-quest-ce-que-la-regeneration-statique-incrementielle-isr)

2. [Comment l'ISR fonctionne en arrière-plan](#heading-comment-lisr-fonctionne-en-arriere-plan)

3. [Quand l'ISR déclenche-t-elle une nouvelle génération de page](#heading-quand-lisr-declenche-t-elle-une-nouvelle-generation-de-page)

4. [Cas d'utilisation courants pour l'ISR](#heading-cas-dutilisation-courants-pour-lisr)

5. [Bonnes pratiques pour utiliser l'ISR](#heading-bonnes-pratiques-pour-utiliser-lisr)

6. [Pièges potentiels et comment les éviter](#heading-pieges-potentiels-et-comment-les-eviter)

7. [Conseils avancés : ISR à la demande](#heading-conseils-avances-isr-a-la-demande)

8. [Conclusion](#heading-conclusion)

## Qu'est-ce que la régénération statique incrémentielle (ISR) ?

La régénération statique incrémentielle (ISR) est une fonctionnalité de Next.js qui vous permet de mettre à jour des pages statiques après avoir construit votre site.

Auparavant, si vous construisiez un site statique et deviez changer quelque chose, vous deviez reconstruire tout le site à partir de zéro. Cela pouvait prendre beaucoup de temps, surtout pour les grands sites web.

L'ISR résout ce problème. Avec l'ISR, vous pouvez dire à Next.js de reconstruire une page en arrière-plan après un certain temps, ou chaque fois que vous le demandez. L'utilisateur voit toujours une page statique rapide, mais la page peut également se mettre à jour en arrière-plan sans que vous ayez à tout reconstruire manuellement.

En termes simples, les pages sont pré-rendues et servies comme des fichiers statiques. Après un temps défini, Next.js peut régénérer la page avec de nouvelles données et les utilisateurs obtiennent toujours des pages rapides et fiables.

## Comment l'ISR fonctionne en arrière-plan

Pour comprendre l'ISR, examinons d'abord les trois façons dont vous pouvez construire des pages dans Next.js :

* **Génération statique (SSG) :** Les pages sont construites une fois lors du déploiement. Elles ne changent jamais sauf si vous reconstruisez tout le site.

* **Rendu côté serveur (SSR) :** Les pages sont construites à chaque demande. Cela peut ralentir les choses car le serveur travaille à chaque fois.

* **Régénération statique incrémentielle (ISR) :** Les pages sont construites au moment de la demande *uniquement si nécessaire* après qu'un certain temps s'est écoulé. Sinon, les utilisateurs obtiennent la page déjà construite instantanément.

### **Comment l'ISR fonctionne réellement :**

Lorsque vous utilisez l'ISR :

1. Un utilisateur visite votre page.

2. Si la page est déjà construite et non expirée, Next.js sert la page statique mise en cache.

3. Si la page a expiré en fonction du temps que vous avez défini, Next.js reconstruit la page en arrière-plan tout en servant l'ancienne page.

4. Le prochain utilisateur qui visite obtient automatiquement la nouvelle version fraîche.

Vous contrôlez quand les pages expirent en définissant une limite de temps, en utilisant la clé `revalidate` à l'intérieur de votre fonction `getStaticProps`.

Voici la configuration de base pour l'ISR :

```javascript
// pages/posts/[id].js

export async function getStaticProps(context) {
  const { id } = context.params;

  const post = await fetch(`https://example.com/posts/${id}`).then(res => res.json());

  return {
    props: {
      post,
    },
    revalidate: 60, // Régénère la page après 60 secondes
  };
}

export async function getStaticPaths() {
  const posts = await fetch('https://example.com/posts').then(res => res.json());

  const paths = posts.map((post) => ({
    params: { id: post.id.toString() },
  }));

  return { paths, fallback: 'blocking' };
}
```

**Ce que cela fait :**

* La page est construite et mise en cache la première fois que quelqu'un la visite.

* Après 60 secondes, si quelqu'un la visite à nouveau, Next.js reconstruira la page en arrière-plan avec de nouvelles données.

* Les utilisateurs obtiennent toujours une page immédiatement. Ils n'ont jamais à attendre.

## Quand l'ISR déclenche-t-elle une nouvelle génération de page ?

Maintenant que vous savez ce qu'est l'ISR, examinons quand et comment une page est réellement régénérée.

Voici le flux :

1. Un utilisateur demande une page.

2. Next.js vérifie si une page mise en cache (déjà construite) existe.

3. Si la page est toujours "fraîche" (dans le temps de `revalidate`), elle sert simplement la page mise en cache.

4. Si la page est "obsolète" (hors du temps de `revalidate`), elle **sert l'ancienne page mise en cache** immédiatement mais commence également à reconstruire la page en arrière-plan.

5. Une fois la reconstruction terminée, le prochain utilisateur obtient la nouvelle page mise à jour.

**Important :**
Personne n'attend jamais. L'ISR sert toujours quelque chose instantanément, soit la page fraîche, soit la version précédente.

```plaintext
L'utilisateur visite la page --> La page est-elle fraîche ?
         |
    Oui  |  Non
    Servir la page mise en cache  Servir la page mise en cache + Démarrer la régénération en arrière-plan
                           |
                  Régénération terminée
                           |
                  Le prochain utilisateur voit la page mise à jour
```

### Exemple rapide

Supposons que vous définissez `revalidate: 30` secondes pour votre page.

* À 12:00:00 PM → La page est construite et mise en cache.

* À 12:00:10 PM → Un utilisateur visite. La page est servie à partir du cache (toujours fraîche).

* À 12:00:35 PM → Un autre utilisateur visite. Le cache est obsolète, donc Next.js sert l'ancienne page mais déclenche une reconstruction.

* À 12:00:36 PM → La reconstruction se termine. La nouvelle page est prête.

* À 12:00:40 PM → Le prochain visiteur obtient la nouvelle page fraîche.

#### **En bref :**

La page est toujours disponible rapidement, et elle se met à jour discrètement sans que les utilisateurs ne s'en aperçoivent.

## Cas d'utilisation courants pour l'ISR

Vous vous demandez peut-être quand utiliser réellement l'ISR ?

Voici les situations les plus courantes où l'ISR est le choix parfait :

### 1. Blogs et sites d'actualités

Si vous gérez un blog ou un site d'actualités, de nouveaux articles sont souvent ajoutés. Vous voulez que vos lecteurs voient un contenu frais, mais vous voulez également que les pages se chargent rapidement.

Avec l'ISR :

* Les articles sont construits comme des pages statiques.

* Lorsque vous publiez un nouvel article, il se met à jour discrètement après un court laps de temps.

* Les lecteurs obtiennent toujours des vitesses de chargement rapides.

**Exemple :**
Un blog technologique se met à jour toutes les quelques heures. Vous définissez `revalidate: 3600` (1 heure) pour que les pages se rafraîchissent avec un nouveau contenu une fois par heure.

### 2. Pages de produits de commerce électronique

Dans les magasins en ligne, les informations sur les produits comme les prix, la disponibilité et les descriptions changent souvent. Vous voulez que les données soient assez fraîches, mais vous avez également besoin de chargements de pages rapides pour de bonnes ventes.

Avec l'ISR :

* Les pages de produits se chargent instantanément.

* Si quelque chose change (comme une vente), la page se met à jour discrètement sans nuire à l'expérience d'achat.

**Exemple :**
Vous définissez `revalidate: 300` (5 minutes) pour vos produits afin que les changements apparaissent rapidement sans ralentir le magasin.

### 3. Tableaux de bord et contenu généré par les utilisateurs

Si votre site comporte des tableaux de bord, des avis, des forums ou des profils d'utilisateurs qui ne changent pas toutes les secondes, l'ISR peut être un choix judicieux.

Avec l'ISR :

* Vous pouvez afficher des publications, des commentaires ou des statistiques mis à jour sans faire travailler trop dur le serveur.

* Le contenu se rafraîchit à des intervalles que vous décidez.

**Exemple :**
Un site d'avis rafraîchit sa liste des "Meilleurs produits" tous les jours en utilisant `revalidate: 86400` (24 heures).

#### En bref :

Si votre page change parfois (pas toutes les secondes) et que vous voulez une grande vitesse et un contenu frais, utilisez l'ISR.

## Bonnes pratiques pour utiliser l'ISR

Pour obtenir les meilleurs résultats avec l'ISR, vous devez la configurer correctement. Voici quelques conseils importants pour vous assurer que tout fonctionne sans accroc.

### 1. Choisissez le bon temps de `revalidate`

Réfléchissez à la fréquence à laquelle votre contenu change réellement.

* Si votre contenu change **toutes les heures**, vous pouvez définir `revalidate: 3600` (ce qui équivaut à 1 heure).

* Si votre contenu change **quotidiennement**, vous pouvez définir `revalidate: 86400` (ce qui équivaut à 24 heures).

* Si votre contenu change **toutes les quelques minutes**, vous pouvez définir `revalidate: 300` (ce qui équivaut à 5 minutes).

**Conseil :**
Choisissez un temps de `revalidate` qui équilibre la fraîcheur et la charge du serveur. Des temps plus courts signifient des données plus fraîches mais peuvent mettre plus de pression sur votre serveur.

### 2. Gérez les erreurs efficacement

Parfois, votre source de données (comme une API) peut échouer lors de la régénération d'une page.

Pour éviter de casser votre page :

* Utilisez toujours un bloc try-catch dans votre `getStaticProps`.

* Affichez un message de repli ou une page d'erreur simple si la récupération échoue.

**Exemple :**

```javascript
export async function getStaticProps() {
  try {
    const data = await fetch('https://example.com/data').then(res => res.json());

    return {
      props: { data },
      revalidate: 60,
    };
  } catch (error) {
    console.error('Échec de la récupération des données :', error);

    return {
      props: { data: null },
      revalidate: 60,
    };
  }
}
```

### 3. Pensez au SEO

Puisque l'ISR sert des pages statiques rapidement, c'est idéal pour le SEO.

N'oubliez pas :

* Retournez toujours un contenu significatif même si la récupération des données échoue.

* Évitez d'afficher des états "Chargement..." lors de l'utilisation de l'ISR. La page doit sembler complète à la fois pour les utilisateurs et les moteurs de recherche.

## Pièges potentiels et comment les éviter

Même si l'ISR est incroyable, il y a quelques choses qui peuvent vous poser problème si vous n'êtes pas prudent. Voici ce à quoi il faut faire attention.

### 1. Problèmes de données obsolètes

Parfois, les utilisateurs peuvent voir des données anciennes si la page n'a pas encore été révalidée. Cela se produit parce que l'ISR sert la version mise en cache jusqu'à ce qu'une nouvelle soit construite.

**Comment gérer cela :**

* Définissez un temps de `revalidate` qui a du sens pour votre contenu.

* Si votre contenu est très sensible (comme les prix des actions), vous pouvez vouloir utiliser le rendu côté serveur (SSR) au lieu de l'ISR.

### 2. Mauvaises configurations de déploiement

L'ISR nécessite un support serveur pour fonctionner correctement. Si vous hébergez votre site sur des plateformes comme Vercel ou Netlify, elles gèrent cela pour vous.

Mais si vous utilisez un serveur personnalisé ou un hébergement différent, assurez-vous :

* Que vous avez des fonctions serverless ou un support backend en cours d'exécution.

* Que vous ne transformez pas votre site en hébergement uniquement statique par erreur (comme des buckets S3 simples sans aucun backend).

**Conseil :**
Consultez toujours la documentation de votre fournisseur d'hébergement pour confirmer qu'il supporte correctement **Next.js ISR**.

### 3. Les grandes reconstructions peuvent provoquer des pics de charge

Si votre `revalidate` est trop court et que vous avez des milliers de pages, le serveur peut être inondé de demandes de régénération en arrière-plan.

**Comment gérer cela :**

* Soyez intelligent avec vos valeurs de `revalidate`.

* Pour les très grands sites, envisagez l'ISR à la demande (où vous contrôlez manuellement quand les pages se reconstruisent - nous en parlerons ensuite).

## Conseils avancés : ISR à la demande

Normalement, avec l'ISR, les pages se régénèrent après un temps défini que vous définissez avec `revalidate`.

Mais parfois, vous voulez un contrôle total. Vous voulez régénérer une page immédiatement après qu'un événement se produise, comme :

* Un nouvel article de blog est publié

* Un produit est mis à jour

* Un utilisateur soumet un nouveau contenu

C'est là qu'intervient l'ISR à la demande.

Avec l'ISR à la demande, vous déclenchez manuellement la reconstruction d'une page en utilisant une route API. Pas besoin d'attendre le minuteur - vous décidez quand cela se produit.

### Comment configurer l'ISR à la demande

Vous avez besoin de deux choses simples :

1. Une route API qui indique à Next.js de révalider une page.

2. Un jeton secret pour protéger votre API afin que n'importe qui ne puisse pas la déclencher.

### Exemple : Route API de base pour l'ISR à la demande

Créez un fichier comme ceci :

```javascript
// pages/api/revalidate.js

export default async function handler(req, res) {
  // Vérification du jeton secret pour la sécurité
  if (req.query.secret !== process.env.MY_SECRET_TOKEN) {
    return res.status(401).json({ message: 'Jeton invalide' });
  }

  try {
    const pathToRevalidate = req.query.path;

    await res.revalidate(pathToRevalidate);

    return res.json({ revalidated: true });
  } catch (err) {
    return res.status(500).json({ message: 'Erreur de révalidation' });
  }
}
```

### Comment la déclencher

Vous pouvez faire une requête **POST** à votre route API comme ceci :

```plaintext
POST /api/revalidate?secret=VOTRE_JETON&path=/votre-chemin-de-page
```

Par exemple :

```plaintext
POST /api/revalidate?secret=MY_SECRET_TOKEN&path=/posts/mon-nouvel-article
```

Next.js reconstruira immédiatement `/posts/mon-nouvel-article`, pas besoin d'attendre le minuteur.

### Important :

* Utilisez toujours un jeton secret et stockez-le en sécurité (comme dans les fichiers `.env`).

* Assurez-vous que seuls les systèmes de confiance (comme votre CMS ou panneau d'administration) peuvent appeler l'API de révalidation.

## Conclusion

La régénération statique incrémentielle (ISR) est l'une des meilleures fonctionnalités de Next.js. Elle vous offre la vitesse des pages statiques et la fraîcheur du contenu dynamique en même temps.

Avec l'ISR :

* Vos pages se chargent instantanément.

* Votre contenu reste à jour sans reconstructions complètes.

* Votre site web semble fluide, moderne et professionnel.

Si vous utilisez l'ISR judicieusement, vous pouvez construire des sites web plus rapides et plus intelligents sans compliquer les choses.