---
title: Comment ajouter Google Analytics à votre site Astro
subtitle: ''
author: Ihechikara Abba
co_authors: []
series: null
date: '2023-10-18T18:07:14.000Z'
originalURL: https://freecodecamp.org/news/how-to-add-google-analytics-to-your-astro-website
coverImage: https://www.freecodecamp.org/news/content/images/2023/10/andy-hermawan-bVBvv5xlX3g-unsplash.jpg
tags:
- name: analytics
  slug: analytics
- name: Astro
  slug: astro
- name: Google Analytics
  slug: google-analytics
seo_title: Comment ajouter Google Analytics à votre site Astro
seo_desc: 'You can use data insights derived from your website or app to make important
  decisions that''ll help grow your business. This information can help you improve
  user experience, create effective content strategies, and so on.

  Google Analytics is an effe...'
---

Vous pouvez utiliser les informations dérivées de votre site web ou de votre application pour prendre des décisions importantes qui aideront à développer votre entreprise. Ces informations peuvent vous aider à améliorer l'expérience utilisateur, à créer des stratégies de contenu efficaces, et ainsi de suite.

Google Analytics est un outil efficace pour suivre et analyser le trafic et les événements sur vos sites web et applications mobiles. Dans cet article, vous apprendrez comment ajouter Google Analytics à votre site Astro.

Pour suivre ce guide, vous aurez besoin des éléments suivants :

* Un compte Google.
* Un projet Astro déployé.

Commençons !

## Comment ajouter Google Analytics à un site Astro

Avant d'ajouter Google Analytics, assurez-vous d'avoir déjà déployé votre projet. Voici un exemple que j'ai déployé en utilisant Netlify : [https://astro-article.netlify.app/](https://astro-article.netlify.app/). Il s'agit d'un modèle de blog Astro créé avec la commande `npm create astro@latest -- --template blog`.

Cette section sera divisée en deux sous-sections. Dans la première sous-section, vous apprendrez comment créer un compte Analytics et comment configurer votre compte pour suivre et surveiller votre site web.

Dans la deuxième sous-section, vous apprendrez comment configurer votre code pour le synchroniser avec Google Analytics.

### Comment configurer Google Analytics

Vous pouvez suivre ces étapes pour configurer Google Analytics :

#### Étape #1 – Page de création de compte

La première étape consiste à créer un compte Google Analytics. Vous pouvez le faire en visitant [le site web de Google Analytics](https://analytics.google.com/).

Lorsque la page se charge, vous devriez voir quelque chose de similaire à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/google-analytics-2.png)
_Page d'accueil de Google Analytics_

Cliquez sur le bouton "Commencer la mesure". Cela vous mènera à la page de création de compte où vous remplirez quelques informations sur votre site web/application. C'est-à-dire :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/account-creation.png)
_Page "Créer un compte" sur Google Analytics_

Après avoir saisi un nom de compte, faites défiler la page vers le bas et cliquez sur le bouton "Suivant".

#### Étape #2 – Page de création de propriété

Sur la page de création de propriété, vous pouvez créer un nom de propriété, un fuseau horaire et une devise.

Une propriété agit comme un identifiant unique pour vos sites web et applications. C'est donc comme un conteneur pour toutes les données liées à un site web ou une application spécifié.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/property-creation.png)
_Page "Créer une propriété" sur Google Analytics_

#### Étape #3 – Page des détails de l'entreprise

Sur la page des détails de l'entreprise, vous pouvez spécifier votre catégorie d'industrie et la taille de l'entreprise.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/business-details.png)
_Page "Décrivez votre entreprise" sur Google Analytics_

#### Étape #4 – Page des objectifs de l'entreprise

Les objectifs de l'entreprise aident Analytics à générer des rapports personnalisés pour votre entreprise. Vous pouvez sélectionner les options qui sont importantes pour votre site web, votre application ou votre catégorie de produit.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/business-objectives.png)
_Page "Objectifs de l'entreprise" sur Google Analytics_

Après avoir sélectionné les options, cliquez sur le bouton "Créer".

#### Étape #5 – Page de collecte de données

Sur la page de collecte de données, vous pouvez choisir entre différentes plateformes pour collecter des données. Puisque nous travaillons avec un site web, nous choisirons l'option Web.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/data-collection.png)
_Page "Commencer à collecter des données" sur Google Analytics_

Ensuite, vous devrez créer un flux de données en saisissant l'URL de votre site web et le nom de votre flux (celui-ci peut être ce que vous voulez, mais je recommande d'utiliser un nom lié à votre site web).

![Image](https://www.freecodecamp.org/news/content/images/2023/10/stream.png)
_Page de configuration d'un flux de données sur Google Analytics_

Dans mes informations de flux de données, j'ai utilisé [https://astro-article.netlify.app/](https://astro-article.netlify.app/) comme URL et "Astro Blog Template" comme nom de flux.

Assurez-vous de supprimer la partie "https://" du lien dans la boîte de saisie pour éviter l'erreur "Une URL de site web valide est requise".

Ainsi, au lieu de [https://astro-article.netlify.app/](https://astro-article.netlify.app/), cela devrait être astro-article.netlify.app/.

Voici à quoi ressemble le mien :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/stream-data.png)
_Exemple d'informations saisies correctement dans la page de configuration du flux de données_

Allez-y et cliquez sur le bouton "Créer un flux".

Sur la page/invite suivante, vous verrez le nom de votre flux, l'URL, l'ID et les valeurs d'ID de mesure.

L'ID de mesure sera important dans notre intégration de code, vous pouvez donc le copier et le coller quelque part.

Voici à quoi ressemble la page :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/stream-details.png)
_Page "Détails du flux web" sur Google Analytics_

Si vous cliquez sur "Voir les instructions de balise", vous verrez un extrait de code pour une intégration manuelle avec le code. Copiez le code et collez-le quelque part car nous allons l'utiliser bientôt.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/installation-instructions.png)
_Instructions d'installation_

Voici l'extrait de code si vous l'avez manqué :

```js
<!-- Balise Google (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=MEASUREMENT_ID"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'MEASUREMENT_ID');
</script>

```

Si vous copiez le code ci-dessus, assurez-vous de remplacer les deux valeurs `MEASUREMENT_ID` par la valeur réelle de votre ID de mesure.

### Comment intégrer Google Analytics et Astro

À ce stade, nous avons créé un compte Google Analytics et généré l'ID de mesure de notre projet. La prochaine chose à faire est de synchroniser notre code avec Google Analytics.

Mais d'abord, nous devons installer une bibliothèque appelée Partytown. Lorsque vous utilisez des intégrations tierces, vous pouvez rencontrer des problèmes de performance car vous utilisez du code tiers.

Partytown permet à ces intégrations de fonctionner comme prévu sans réduire les performances de votre site. Vous pouvez en lire plus à ce sujet [ici](https://partytown.builder.io/how-does-partytown-work).

#### Étape #1 – Installer Partytown

Rendez-vous dans le terminal de votre projet Astro et exécutez cette commande pour installer Partytown :

```bash
npm install @astrojs/partytown
```

#### Étape #2 – Configurer Partytown

Une fois l'installation terminée, vous devrez ajouter l'intégration à votre fichier **astro.config.mjs** :

```js
import { defineConfig } from 'astro/config';
import mdx from '@astrojs/mdx';
import partytown from '@astrojs/partytown'

import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
	site: 'https://astro-article.netlify.app/',
	integrations: [
		mdx(), 
		sitemap(),
		partytown({
			config: {
			  forward: ["dataLayer.push"],
			},
		}),
	],
});

```

Dans le code ci-dessus, nous avons importé la bibliothèque Partytown : `import partytown from '@astrojs/partytown'`.

Nous avons ensuite ajouté ce morceau de code à l'objet `integrations` :

```js
partytown({
      config: {
        forward: ["dataLayer.push"],
      },
})

```

Tout le reste du code est venu avec le projet Astro.

#### Étape #3 – Ajouter la balise Google à vos pages

Vous vous souvenez de l'extrait de code de Google Analytics ? C'est ici que nous allons l'utiliser.

```js
<!-- Balise Google (gtag.js) -->
<script type="text/partytown" async src="https://www.googletagmanager.com/gtag/js?id=MEASUREMENT_ID"></script>
<script type="text/partytown">
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'MEASUREMENT_ID');
</script>

```

Notez que nous avons ajouté l'attribut `type="text/partytown"` aux deux balises `<script>`.

N'oubliez pas de changer les valeurs `MEASUREMENT_ID` par la valeur de votre ID de mesure. Le mien ressemble à ceci :

```js
<!-- Balise Google (gtag.js) -->
<script type="text/partytown" async src="https://www.googletagmanager.com/gtag/js?id=G-KM36S70L8Y"></script>
<script type="text/partytown">
	window.dataLayer = window.dataLayer || [];
	function gtag(){dataLayer.push(arguments);}
	gtag('js', new Date());

	gtag('config', 'G-KM36S70L8Y');
</script>

```

N'utilisez pas l'extrait de code ci-dessus car il contient mon ID de mesure et est donc déjà associé à mon site web (pas mon site web réel :)). Copiez le premier extrait de code et changez les valeurs `MEASUREMENT_ID` par la valeur de votre ID de mesure.

Pour suivre et surveiller une page, vous devez coller l'extrait de code dans cette page. Copiez le code et collez-le dans la section `<head>` de chaque fichier de page (**index.astro**, **BlogPost.astro**, etc.) que vous souhaitez suivre et analyser à l'aide de Google Analytics.

Voici un exemple utilisant le fichier **index.astro** dans le répertoire **pages** :

```js
---
import BaseHead from '../components/BaseHead.astro';
import Header from '../components/Header.astro';
import Footer from '../components/Footer.astro';
import { SITE_TITLE, SITE_DESCRIPTION } from '../consts';
---

<!doctype html>
<html lang="en">
	<head>
		<!-- Balise Google (gtag.js) -->
		<script type="text/partytown" async src="https://www.googletagmanager.com/gtag/js?id=MEASUREMENT_ID"></script>
		<script type="text/partytown">
			window.dataLayer = window.dataLayer || [];
			function gtag(){dataLayer.push(arguments);}
			gtag('js', new Date());

			gtag('config', 'MEASUREMENT_ID');
		</script>
		<BaseHead title={SITE_TITLE} description={SITE_DESCRIPTION} />
	</head>
... <!-- Le reste du code HTML -->

```

Dans le code ci-dessus, nous avons placé le code de Google Analytics dans la balise `<head>`. Vous pouvez faire cela pour toutes les pages que vous souhaitez suivre et surveiller.

N'oubliez pas d'ajouter l'attribut `type="text/partytown"` aux balises `<script>`, et de changer `MEASUREMENT_ID` (utilisé à deux endroits dans l'extrait) par la valeur de votre ID de mesure.

#### Étape #4 – Construire et déployer votre projet

Déployez votre projet en utilisant votre processus préféré.

Dans mon cas, j'utilise `npm run build` pour construire dans le dossier **dist**, puis je pousse le code vers GitHub. Cela déclenche automatiquement un déploiement Netlify.

Vous n'êtes pas obligé d'utiliser ma méthode, mais assurez-vous que votre projet est construit avant le déploiement.

Une fois votre site web déployé, vous devrez peut-être attendre jusqu'à 48 heures pour commencer à voir vos analyses dans le tableau de bord Google Analytics.

![Image](https://www.freecodecamp.org/news/content/images/2023/10/pending-data-collection.png)
_Page en attente_

Vous verrez cette page lorsque vous cliquerez sur le bouton "Continuer vers l'accueil" :

![Image](https://www.freecodecamp.org/news/content/images/2023/10/analytics-home.png)
_Tableau de bord Analytics_

C'est votre tableau de bord Analytics. Vous pouvez consulter et analyser vos données ici lorsqu'elles sont disponibles.

Et voilà ! Vous avez réussi à intégrer votre projet avec Google Analytics.

## Résumé

Dans cet article, nous avons vu comment ajouter Google Analytics à un projet Astro. Cela peut être utilisé pour suivre et analyser le trafic et les événements sur les sites web et les applications.

Nous avons vu comment créer et configurer un compte Analytics.

Nous avons ensuite vu comment intégrer Google Analytics à un projet Astro en utilisant du code.

Bon codage ! Vous pouvez lire plus de tutoriels Astro sur [mon blog](https://ihechikara.com/).