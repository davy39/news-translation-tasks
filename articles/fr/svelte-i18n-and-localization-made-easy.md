---
title: Svelte i18n et localisation simplifiés
subtitle: ''
author: Alex Tray
co_authors: []
series: null
date: '2024-12-05T19:42:00.566Z'
originalURL: https://freecodecamp.org/news/svelte-i18n-and-localization-made-easy
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733421094910/f2f91ab6-0717-4135-9f08-719f041471f6.jpeg
tags:
- name: localization
  slug: localization
- name: Svelte
  slug: svelte
- name: i18n
  slug: i18n
- name: app development
  slug: app-development
- name: App Localization
  slug: app-localization
seo_title: Svelte i18n et localisation simplifiés
seo_desc: "Apps are accessible worldwide. This means anyone from anywhere in the world\
  \ can download your app. \nSo, if you want to cater to people everywhere, your app\
  \ needs to support multiple languages. \nFortunately, Svelte is easy to work with,\
  \ and it makes l..."
---

Les applications sont accessibles dans le monde entier. Cela signifie que n'importe qui, n'importe où dans le monde, peut télécharger votre application.

Ainsi, si vous souhaitez vous adresser à des personnes partout dans le monde, votre application doit prendre en charge plusieurs langues.

Heureusement, Svelte est facile à utiliser et rend la localisation (l10n) et l'internationalisation (i18n) assez simples.

Cependant, il manque de support intégré pour l'i18n, vous devez donc utiliser une bibliothèque comme svelte-i18n ou l'une des autres disponibles. Créons une simple application Svelte pour démontrer comment la localisation peut être implémentée.

Nous allons créer un écran de bienvenue qui peut être utilisé en anglais et en espagnol, puis construire des fonctionnalités plus avancées.

<dl>
<summary>Table des matières</summary>
<ul>
<li>
  <a href="#heading-ce-qui-rend-svelte-unique">Ce qui rend Svelte unique</a></li>
  <li><a href="#heading-comment-localiser-une-application-svelte">Comment localiser une application Svelte</a></li>
  <li><a href="#heading-ajout-de-la-prise-en-charge-des-langues">Ajout de la prise en charge des langues</a></li>
  <li><a href="#heading-mise-a-jour-des-composants-pour-utiliser-les-traductions">Mise à jour des composants pour utiliser les traductions</a></li>
  <li><a href="#heading-creation-dun-selecteur-de-langue">Création d'un sélecteur de langue</a></li>
  <li><a href="#heading-ajout-de-fonctionnalites-avancees">Ajout de fonctionnalités avancées</a></li>
<details>
  <li><a href="#heading-formatage-des-nombres-et-des-devises">Formatage des nombres et des devises</a></li>
  <li><a href="#heading-formatage-des-dates">Formatage des dates</a></li>
  <li><a href="#heading-localisation-des-images">Localisation des images</a></li>
<details>
  <li><a href="#heading-chemins-dimages-dynamiques">Chemins d'images dynamiques</a></li><li>
  </li><li><a href="#heading-integration-de-la-localisation-du-texte-alternatif">Intégration de la localisation du texte alternatif</a></li>
 <li><a href="#heading-changement-dynamique-du-contenu-svg">Changement dynamique du contenu SVG</a></li>
</details>
  <li><a href="#heading-gestion-de-plusieurs-formes-de-pluriel">Gestion de plusieurs formes de pluriel</a></li>
  <li><a href="#heading-gestion-des-traductions-manquantes">Gestion des traductions manquantes</a></li>
</details>
  <li><a href="#heading-preparation-de-votre-application-pour-la-production">Préparation de votre application pour la production</a></li>
 <li><a href="#heading-meilleures-pratiques-pour-developper-votre-localisation">Meilleures pratiques pour développer votre localisation</a></li>
  <li><a href="#heading-conclusion">Conclusion</a></li>
</ul>
</dl>

## Ce qui rend Svelte unique

Similaire à [Vue i18n](https://centus.com/blog/vue-i18n), Svelte convertit le code en JavaScript vanilla lors du processus de construction. Cela signifie que votre application est livrée avec un code minimal et offre des performances excellentes.

Alors que d'autres frameworks comme React et Vue ont des temps de démarrage plus longs, le processus de compilation de Svelte change cela. Il crée des bundles beaucoup plus petits, et les applications fonctionnent plus rapidement par défaut.

La syntaxe réactive de Svelte et sa nature légère en font un excellent choix pour les développeurs qui veulent des applications efficaces et modernes.

Son minimalisme s'aligne bien avec la simplicité requise dans les [**langages de développement cloud**](https://v2cloud.com/blog/best-programming-languages-for-cloud-computing), garantissant que les applications sont légères, scalables et optimisées pour les environnements cloud.

Ce minimalisme signifie également que vous n'aurez pas toujours toutes les fonctionnalités intégrées requises. Mais presque toutes les limitations sont résolues avec l'aide de bibliothèques externes.

## Comment localiser une application Svelte

Passons directement à la création d'un projet Svelte maintenant. Je vais créer le projet en utilisant la commande `npm create`. Exécutez les commandes suivantes une par une :

```javascript
npm create svelte@latest freecodecamp-localization-demo
cd freecodecamp-localization-demo
npm install
npm install svelte-i18n
```

La commande `npm create` vous invitera à faire quelques choix. Voici ce que j'ai choisi (mais vous pouvez toujours ajuster cela en fonction des exigences de votre projet) :

* Projet squelette : Sélectionnez **Oui**.

* Ajouter le support TypeScript : Sélectionnez **Non** (ou Oui si vous préférez TypeScript).

* Ajouter ESLint pour le linting du code : Sélectionnez **Oui**.

* Ajouter Prettier pour le formatage du code : Sélectionnez **Oui**.

Maintenant que notre projet est configuré, créons un composant de bienvenue que nous améliorerons plus tard avec des traductions.

Créez un nouveau fichier appelé Welcome.svelte dans votre répertoire src :

```javascript
<!-- src/Welcome.svelte -->
<script>
  export let username;
</script>

<div>Bienvenue {username} !</div>
```

![](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfcaW7fLzjbLa5ysYYu5FplhoGeVNmml9An_l0fcbEwQSxvg5mDbh3PY9b7etS6DESM7ZGdO_R5dqcYaDdgMaaQE2d7w1Q8eU4uAtIfKjHfm58buFwM-KLtJ_bv-x3XyqoYIOgfdQ?key=uXnvRGfJpBUiBb7CkgThtLro align="left")

Ce composant prend la propriété username (que j'ai passée depuis le fichier App.svelte) et affiche un message de bienvenue.

Assez simple pour l'instant, mais que se passe-t-il si vos utilisateurs parlent différentes langues ? Ajoutons la prise en charge des langues.

## Ajout de la prise en charge des langues

Pour ce faire, nous devons créer des fichiers de traduction pour chaque langue. Commencez par créer un nouveau répertoire appelé **locales** dans votre dossier **src**. À l'intérieur du dossier **locales**, créez deux fichiers JSON—*en.json* pour l'anglais et *es.json* pour l'espagnol.

```javascript
// src/locales/en.json
{
  "hello": "Hello {username}!",
  "buttons": {
    "save": "Save",
    "cancel": "Cancel"
  }
}

// src/locales/es.json
{
  "hello": "¡Hola {username}!",
  "buttons": {
    "save": "Guardar",
    "cancel": "Cancelar"
  }
}
```

Ces fichiers contiennent nos chaînes de traduction.

Remarquez comment nous les avons organisées dans une structure imbriquée—cela aide à gérer les traductions à mesure que votre application grandit.

Les placeholders {username} et {count} seront remplacés par des valeurs réelles lors de l'exécution lorsque nous passerons dynamiquement (ou statiquement) les valeurs requises.

Ensuite, nous devons indiquer à Svelte comment utiliser ces traductions. Pour cela, nous avons besoin d'un fichier de **configuration i18n** :

```javascript
// src/i18n.js
import { register, init } from 'svelte-i18n';

register('en', () => import('./locales/en.json'));
register('es', () => import('./locales/es.json'));

init({
  fallbackLocale: 'en',
  initialLocale: 'en',
});
```

Nous avons enregistré nos fichiers de traduction et défini l'anglais comme langue initiale et langue de repli. La langue de repli est utilisée lorsqu'une traduction est manquante dans la langue sélectionnée.

## Mise à jour des composants pour utiliser les traductions

Maintenant, nous pouvons mettre à jour notre composant de bienvenue pour utiliser le texte du fichier JSON :

```javascript
<!-- src/Welcome.svelte -->
<script>
  import { _ } from 'svelte-i18n';
  export let username;
</script>

<div>{$_( 'hello', { username })}</div>
```

La fonction `$_` est un helper spécial de svelte-i18n qui récupère les chaînes traduites.

Lorsque nous passons { username } comme deuxième argument, il remplace le placeholder dans nos chaînes de traduction par le nom d'utilisateur réel.

## Création d'un sélecteur de langue

Mais comment quelqu'un pourrait-il changer de langue ? Créons un simple composant de sélection de langue :

```javascript
<!-- src/LanguageSelect.svelte -->
<script>
  import { locale } from 'svelte-i18n';

  const languages = [
    { code: 'en', name: 'English' },
    { code: 'es', name: 'Español' }
  ];
</script>

<div>
  {#each languages as { code, name }}
    <button on:click={() => locale.set(code)}>{name}</button>
  {/each}
</div>
```

La directive **bind:value** met automatiquement à jour la langue active lorsque les utilisateurs font une sélection.

Le store locale de svelte-i18n gère tout le travail en coulisses pour changer de langue.

Maintenant, rassemblons tout dans notre composant principal **App** :

```javascript
<!-- src/App.svelte -->
<script>
  import { waitLocale } from 'svelte-i18n';
  import Welcome from './Welcome.svelte';
  import LanguageSelect from './LanguageSelect.svelte';

  const username = 'developer';
</script>

{#await waitLocale()}
  <p>Chargement...</p>
{:then}
  <main>
    <LanguageSelect />
    <Welcome {username} />
  </main>
{/await}
```

La fonction `waitLocale` garantit que les traductions sont chargées avant d'afficher le contenu. Cela évite le scintillement ou les traductions manquantes lorsque l'application se charge pour la première fois.

## Ajout de fonctionnalités avancées

À mesure que votre application grandit, vous devrez gérer des scénarios plus complexes. Examinons quelques exigences courantes.

### Formatage des nombres et des devises

Différents pays gèrent les nombres et les devises de manière très différente. Par exemple, si vous montrez le chiffre de cent mille à quelqu'un de France et à quelqu'un des États-Unis, vous devrez montrer le même chiffre différemment.

France → 100 000,00 $

États-Unis → $100,000.00

Vous voyez comment les milliers sont séparés par un espace et les décimales par une virgule en France ? Utiliser le format de nombre américain rendrait cela assez confus pour quelqu'un de France. Voici quelques autres exemples.

* Les États-Unis utilisent des points pour les décimales (1,234.56)

* De nombreux pays européens utilisent des virgules pour les décimales et des points pour les milliers (1.234,56)

* Certains pays groupent les chiffres différemment (comme 1,23,456 en Inde)

```javascript
// src/lib/formatUtils.js
export function formatCurrency(amount, locale, currency = 'USD') {
  return new Intl.NumberFormat(locale, {
    style: 'currency',
    currency
  }).format(amount);
}
```

Vous pouvez maintenant utiliser ces formateurs dans vos composants :

```javascript
<!-- src/lib/PriceDisplay.svelte -->
<script>
  import { formatCurrency } from './lib/formatUtils';
  let price = 1234.56;
  let locale = 'en';
</script>

<p>Prix : {formatCurrency(price, locale, 'USD')}</p>
```

Avec cette configuration, l'application adapte désormais les formats de devise aux différentes locales en fonction des sorties que vous demandez :

* États-Unis : "$1,234.56", "1.2M", "15%"

* Allemand : "1.234,56 €", "1,2 Mio.", "15 %"

### Formatage des dates

Similaire aux formats de devise et de nombre, les dates sont formatées différemment selon les locales.

Ainsi, tandis que les États-Unis utilisent MM/JJ/AAAA, de nombreux pays européens utilisent JJ/MM/AAAA, et le Japon utilise souvent AAAA年MM月DD日.

Heureusement, nous n'avons pas besoin de gérer cela manuellement. Similaire au formatage de devise, nous avons la fonction `Intl.DateTimeFormat` qui accepte la locale et la date en format numérique et retourne la date correctement formatée.

```javascript
// src/lib/dateUtils.js
export function formatDate(date, locale) {
  return new Intl.DateTimeFormat(locale, {
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  }).format(date);
}
```

Vous pouvez maintenant utiliser cette fonction dans votre application Svelte pour afficher les dates correctement pour chaque locale :

```javascript
<!-- src/lib/DateDisplay.svelte -->
<script>
  import { formatDate } from './lib/dateUtils';
  let locale = 'en';
  let today = new Date();
</script>

<p>Date du jour : {formatDate(today, locale)}</p>
```

Une fois implémenté, vous verrez les dates formatées automatiquement, comme ci-dessous :

* Anglais (États-Unis) : "September 23, 2024"

* Espagnol : "23 de septiembre de 2024"

* Allemand : "23. September 2024"

* Japonais : "2024年9月23日"

### Localisation des images

N'oubliez pas que la localisation ne concerne pas seulement la traduction de texte—vos images ont également besoin d'attention. Des visuels culturellement pertinents, du contenu spécifique à la région comme des cartes ou des symboles, et des formats d'image adaptables peuvent faire toute la différence.

#### **Chemins d'images dynamiques**

Utilisez la réactivité de Svelte pour charger dynamiquement des images en fonction de la locale actuelle. Par exemple, vous pouvez stocker des chemins d'images localisés dans un fichier JSON ou directement dans votre configuration i18n :

```javascript
{
  "en": { "logo": "/images/en/logo.png" },
  "fr": { "logo": "/images/fr/logo.png" }
}
```

Ensuite, dans votre composant Svelte :

```javascript
<script>
  import { locale } from 'svelte-i18n';
  import translations from './translations.json';

  $: imagePath = translations[$locale].logo;
</script>

<img src={imagePath} alt="Logo localisé" />
```

#### **Intégration de la localisation du texte alternatif**

Assurez-vous que les attributs alt de vos images sont également localisés. Vous pouvez y parvenir en ajoutant un champ supplémentaire dans vos traductions :

```javascript
{
  "en": { "logoAlt": "Company Logo" },
  "fr": { "logoAlt": "Logo de l'entreprise" }
}

Puis liez le texte alternatif localisé dynamiquement
```

```javascript

<img src={imagePath} alt={translations[$locale].logoAlt} />
```

#### **Changement dynamique du contenu SVG**

Si vous devez localiser le contenu des SVGs, comme du texte ou des icônes, ou si vous souhaitez convertir au format SVG, envisagez d'utiliser le templating de Svelte pour une intégration transparente.

```javascript
<svg>
  <text x="10" y="20">{$t('svgText')}</text>
</svg>
```

Cette approche garantit que vos SVGs sont directement rendus avec du texte localisé.

### Gestion de plusieurs formes de pluriel

Alors que de nombreuses langues ont deux formes de pluriels (singulier et pluriel), il existe de nombreuses langues avec plus de deux formes, et certaines ne pluralisent pas. Par exemple :

* L'arabe a six formes

* Le japonais ne pluralise pas de la même manière

Nous pouvons facilement gérer ces différences en utilisant la syntaxe de message ICU de svelte-i18n. J'ai également ajouté un exemple de la manière dont vous pouvez gérer plus de deux formes lorsque vous utilisez l'arabe.

```javascript
// src/locales/en.json
{
  "items": {
    "count": "{count, plural, =0 {No items} one {1 item} other {{count} items}}"
  }
}

// src/locales/es.json

{
  "items": {
    "count": "{count, plural, =0 {Sin elementos} one {1 elemento} other {{count} elementos}}"
  }
}

// src/locales/ar.json
{
  "items": {
    "count": "{count, plural, =0 {\u0644\u0627 \u0639\u0646\u0627\u0635\u0631} one {\u0639\u0646\u0635\u0631 \u0648\u0627\u062d\u062f} two {\u0639\u0646\u0635\u0631\u0627\u0646} few {# \u0639\u0646\u0627\u0635\u0631} many {# \u0639\u0646\u0635\u0631} other {# \u0639\u0646\u0635\u0631}}",
  }
}
```

Maintenant, créons le composant de pluralisation pour notre application Svelte où un bouton incrémente le compte à chaque clic.

```javascript
<!-- src/lib/ItemCounter.svelte -->
<script>
  import { _ } from 'svelte-i18n';
  let count = 0;
</script>

<p>{$_( 'items.count', { count })}</p>
<button on:click={() => count++}>Ajouter un élément</button>
<button on:click={() => count--} disabled={count === 0}>Retirer un élément</button>
```

Avec cela implémenté, votre application est entièrement prête à gérer la pluralisation dynamiquement (comme vous le remarquerez en cliquant sur le bouton **Ajouter un élément**).

### Gestion des traductions manquantes

Parfois, des traductions pour certaines clés peuvent être manquantes. Cela peut arriver en raison d'une négligence, d'un contenu dynamique ou de fichiers de traduction incomplets. Pour gérer de tels scénarios avec élégance, configurez la gestion des erreurs en utilisant l'option **missingKeyHandler** dans **svelte-i18n**.

```javascript
import { register, init } from 'svelte-i18n';

register('en', () => import('./locales/en.json'));
register('es', () => import('./locales/es.json'));

init({
  fallbackLocale: 'en',
  initialLocale: 'en',
  missingKeyHandler: (locale, key) => {
    console.warn(`Traduction manquante : ${key} (${locale})`);
    return key; // Afficher la clé elle-même lorsque la traduction est manquante
  }
});
```

Ce code enregistre un avertissement lorsqu'une traduction est manquante et affiche la clé au lieu de ne rien montrer.

## Préparation de votre application pour la production

Lorsque vous préparez votre application pour des utilisateurs réels, optimisez-la pour la localisation en détectant automatiquement la langue de l'utilisateur.

Vous pouvez utiliser la propriété **navigator.language** du navigateur pour définir la locale initiale :

```javascript
import { init, getLocaleFromNavigator } from 'svelte-i18n';

init({
  fallbackLocale: 'en',
  initialLocale: getLocaleFromNavigator(),
});
```

## Meilleures pratiques pour développer votre localisation

* **Organisez les traductions** : Regroupez les traductions liées de manière logique (par exemple, boutons, menus, notifications) et utilisez des schémas de nommage cohérents pour les clés.

* **Utilisez une plateforme de gestion des traductions** : À mesure que votre application grandit, la gestion manuelle des fichiers de traduction commence à devenir fastidieuse. Les [plateformes de gestion des traductions](https://centus.com/) sont conçues pour résoudre ce problème exact et aident à gagner des heures chaque jour, facilitent la collaboration sur les projets et permettent de suivre les progrès.

* **Tests approfondis** : Testez votre application avec de vrais utilisateurs dans toutes les langues prises en charge. Vous devez également garder à l'esprit les changements de longueur de texte pour éviter les problèmes de mise en page, surtout avec des langues comme l'allemand ou l'arabe, qui peuvent étendre considérablement le texte.

* **Considérations culturelles** : Adaptez votre application aux normes culturelles, aux directions de lecture (par exemple, RTL pour l'arabe) et aux préférences régionales (par exemple, formats de date et de devise).

## Conclusion

La localisation peut sembler une tâche importante au début, mais elle en vaut totalement la peine. Elle vous permet d'atteindre plus de personnes et rend votre application plus inclusive.

Svelte et svelte-i18n simplifient le processus et le rendent amusant à mesure que vous développez vos compétences.

Pour garder cela simple, commencez par les bases, comme l'ajout de traductions et un sélecteur de langue. Les fonctionnalités avancées comme la gestion des dates, des devises et de la pluralisation peuvent suivre à mesure que vous gagnez en confiance.

Prenez votre temps, testez soigneusement et construisez une application qui semble naturelle pour tous les utilisateurs que vous servez !