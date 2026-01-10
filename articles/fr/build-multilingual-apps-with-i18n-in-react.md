---
title: Comment créer des applications multilingues avec i18n dans React
subtitle: ''
author: Ayantunji Timilehin
co_authors: []
series: null
date: '2024-12-04T19:34:29.727Z'
originalURL: https://freecodecamp.org/news/build-multilingual-apps-with-i18n-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1733137904769/d29dd9ea-5794-4fbe-ac1c-066f6a216cb2.png
tags:
- name: React
  slug: reactjs
- name: Accessibility
  slug: accessibility
- name: localization
  slug: localization
seo_title: Comment créer des applications multilingues avec i18n dans React
seo_desc: I recently worked on an exciting project that involved creating a website
  capable of switching between languages to appeal to a broader audience. This made
  me understand the concept of "localization" better, which typically entails adapting
  content t...
---

J'ai récemment travaillé sur un projet passionnant qui consistait à créer un site web capable de basculer entre différentes langues pour toucher un public plus large. Cela m'a permis de mieux comprendre le concept de "localisation", qui consiste généralement à adapter le contenu pour le rendre pertinent, accessible et familier pour les utilisateurs de différentes langues et régions.

La localisation ne se limite pas à la traduction des mots, elle consiste à créer une expérience qui fait sentir les utilisateurs chez eux, quelle que soit leur langue. Par exemple, des plateformes mondiales comme Amazon rendent le changement de langue si fluide que cela semble presque magique. Au-delà de l'amélioration de l'expérience utilisateur, cette fonctionnalité joue un rôle crucial dans le développement des entreprises en atteignant un public plus large et en établissant des liens plus forts avec les clients du monde entier.

## Table des matières

* [Table des matières](#heading-table-des-matieres)
    
* [Qu'est-ce que l'i18n et pourquoi l'utiliser ?](#heading-quest-ce-que-li18n-et-pourquoi-lutiliser)
    
* [Plongeons directement](#heading-plongeons-directement)
    
* [Étape 1 : Comment configurer le projet](#heading-etape-1-comment-configurer-le-projet)
    
* [Étape 2 : Comment configurer l'internationalisation avec i18next](#heading-etape-2-comment-configurer-linternationalisation-avec-i18next)
    
* [Étape 3 : Comment construire des composants](#heading-etape-3-comment-construire-des-composants)
    
* [Étape 4 : Composant principal de l'application](#heading-etape-4-composant-principal-de-lapplication)
    
* [Conclusion](#heading-conclusion)
    
* [Références](#heading-references)
    

## Qu'est-ce que l'i18n et pourquoi l'utiliser ?

i18n, abréviation d'internationalisation, signifie qu'une application prend en charge plusieurs langues. "i18n" est dérivé du fait qu'il y a 18 lettres entre le premier "i" et le dernier "n" dans "internationalisation". Il s'agit de rendre votre application adaptable pour les publics mondiaux en gérant la traduction de texte, le formatage des dates et des nombres, la gestion des devises et l'adaptation aux conventions régionales.

En activant l'internationalisation, votre application devient non seulement un outil, mais une plateforme inclusive qui parle directement à la préférence et à la culture de l'utilisateur.

## Plongeons directement

Nous allons créer une application web multilingue très simple avec une fonctionnalité de basculement en mode sombre pour démontrer comment réaliser ce concept.

### Prérequis

1. Connaissance de base de React - Vous devez comprendre comment créer des composants, gérer l'état et utiliser des Hooks comme `useState` et `useEffect`. Si vous êtes nouveau dans React, je vous recommande de commencer par [la documentation officielle de React](https://react.dev/) [pour une base solide](https://react.dev/).
    
2. Familiarité avec les concepts d'internationalisation - Connaître les bases de l'internationalisation (i18n) et pourquoi elle est importante vous donnera le contexte du projet. Les sections précédentes de cet article couvrent les essentiels.
    
3. Tailwind CSS - Nous utiliserons Tailwind CSS pour le style. C'est un framework CSS basé sur les utilitaires qui vous aide à construire des designs modernes et réactifs sans quitter votre HTML. Si vous n'êtes pas familier, consultez [la documentation de Tailwind](https://tailwindcss.com/docs/installation)[.](https://tailwindcss.com/docs/installation)
    
4. Node.js - Assurez-vous que Node.js est installé sur votre système pour gérer les dépendances. Vous pouvez télécharger la dernière version depuis [Node.js](https://nodejs.org/).
    
5. Gestionnaire de paquets - Soit npm (inclus avec Node.js) ou yarn est nécessaire pour gérer les dépendances du projet.
    

### Outils que nous allons utiliser

1. Éditeur de code
    
2. Bibliothèque de localisation : [react-i18next](https://www.i18next.com/)
    
3. Bibliothèque d'icônes : [hero-icons](https://www.npmjs.com/package/heroicons)
    

## Étape 1 : Comment configurer le projet

### Initialiser le projet

Utilisez Vite pour une configuration rapide :

```bash
npm create vite@latest multilingual-demo
```

Suivez les instructions qui s'affichent dans votre terminal, en sélectionnant React et TypeScript pour le développement comme montré dans l'image ci-dessous :

![Image de l'installation de React et TypeScript](https://cdn.hashnode.com/res/hashnode/image/upload/v1733093238523/2d3ee169-bc99-4498-9779-b07067d5e5ee.png align="center")

### Installer les dépendances

Exécutez les commandes suivantes dans votre terminal pour installer les dépendances nécessaires à ce projet :

```bash
npm install i18next react-i18next i18next-browser-languagedetector i18next-http-backend heroicons 
npm install tailwindcss postcss autoprefixer  
npx tailwindcss init  
```

### **Configurer TailwindCSS**

Mettez à jour le fichier `tailwind.config.ts` :

```typescript
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  darkMode: "class", //Pour notre fonctionnalité de mode sombre
  theme: {
    container: {
      center: true,
      padding: "1.25rem",
      screens: {
        sm: "1200px",
      },
    },
    extend: {},
  },
  plugins: [],
};
```

Ajoutez TailwindCSS à `src/index.css` :

```css
@tailwind base;  
@tailwind components;  
@tailwind utilities; 
```

## Étape 2 : Comment configurer l'internationalisation avec i18next

### **Initialiser i18next**

Créez un fichier `i18n.tsx` dans le dossier `src` et configurez i18next :

```typescript
import i18next from "i18next";
import LanguageDetector from "i18next-browser-languagedetector";
import { initReactI18next } from "react-i18next";
import Backend from "i18next-http-backend";

i18next.use(LanguageDetector).use(initReactI18next).use(Backend).init({
  returnObjects: true,
  fallbackLng: "en", // Langue de repli si la langue sélectionnée n'est pas configurée
  debug: true, //Pour nous permettre de voir les erreurs
  //   lng: "en", //Langue par défaut en anglais
});
```

Jetons un rapide coup d'œil au contenu de ce fichier, car il joue un rôle clé dans l'activation de la fonctionnalité de traduction. Ce fichier est responsable de la configuration du cœur du processus de traduction et de s'assurer que la fonctionnalité de changement de langue fonctionne en douceur dans votre application.

* `i18next` : La bibliothèque d'internationalisation principale que nous utilisons pour la traduction.
    
* `LanguageDetector` : Nous aide à détecter automatiquement la langue préférée de l'utilisateur, basée sur les paramètres du navigateur.
    
* `initReactI18next` : Est responsable de l'intégration du plugin `i18next` avec React et fournit des Hooks comme le Hook `useTranslation` et d'autres utilitaires.
    
* `Backend` : Récupère les données de traduction dynamiquement depuis une source externe. Dans ce cas, nous utiliserons des fichiers JSON.
    

Importez ce fichier dans le fichier `main.tsx` :

```typescript
//main.tsx

import React, { StrictMode } from "react";
import { createRoot } from "react-dom/client";
import "./index.css";
import App from "./App.tsx";
import "./i18n.tsx";  //Importer ici

createRoot(document.getElementById("root")!).render(
  <StrictMode>
    <React.Suspense fallback="loading">
      <App />
    </React.Suspense>
  </StrictMode>
);
```

### **Créer des fichiers de traduction**

Dans le répertoire `public/locales`, créez des sous-dossiers pour chaque langue (par exemple, `en`, `fr`) et incluez des fichiers `translation.json` :

`en/translation.json`

```json
{
    "greeting": "Welcome to the Language Playground",
    "detail": {
        "line1": "Did you know that over 7,000 languages are spoken worldwide?",
        "line2": "This Playground demonstrates how web applications can support users in multiple languages, making them accessible and inclusive to people from different backgrounds."
    }
}
```

`fr/translation.json`

```json
{
    "greeting": "Bienvenue sur le terrain de jeu linguistique",
    "detail": {
        "line1": "Saviez-vous que plus de 7 000 langues sont parlées dans le monde ?",
        "line2": "Ce terrain de jeu démontre comment les applications web peuvent prendre en charge les utilisateurs dans plusieurs langues, les rendant accessibles et inclusives aux personnes de différents horizons."
    }
}
```

Ici, vous pouvez ajouter autant de langues avec leurs fichiers de traduction qui seront fournis à `i18next`. Notez que les clés dans les fichiers JSON sont les mêmes car elles seront utilisées comme références lors de leur affichage sur le site web.

![Image de la structure de dossier des fichiers de traduction](https://cdn.hashnode.com/res/hashnode/image/upload/v1733095771585/21cbb0f9-e767-426e-8fc6-2bb4e7abc5ef.png align="center")

## Étape 3 : Comment construire des composants

Créez un dossier `components` dans le répertoire `src` et ajoutez les composants suivants :

### **Sélecteur de langue**

Créez le composant `LanguageSelector` - contient un élément `select` pour aider les utilisateurs à changer de langue dynamiquement :

```typescript
import { useEffect, useState } from "react";
import i18next from "i18next";
import { useTranslation } from "react-i18next";

type languageOption = { language: string; code: string };

const languageOptions: languageOption[] = [
  {
    language: "English",
    code: "en",
  },
  { language: "French", code: "fr" },
  { language: "German", code: "de" },
  { language: "Spanish", code: "es" },
  { language: "Arabic", code: "ar" },
  { language: "Yoruba", code: "yo" },
];

const LanguageSelector = () => {
  // Définir la langue initiale à partir de la langue détectée ou par défaut de i18next
  const [language, setLanguage] = useState(i18next.language);

  const { i18n } = useTranslation();

  const handleLanguageChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const selectedLanguage = e.target.value;
    setLanguage(selectedLanguage);
    i18next.changeLanguage(selectedLanguage); // Mettre à jour la langue dans i18next
  };

  useEffect(() => {
    document.body.dir = i18n.dir(); //définit le body en ltr ou rtl
  }, [i18n, i18n.language]);

  return (
    <select
      id="language"
      value={language}
      onChange={handleLanguageChange}
      className="p-2 border border-gray-300 rounded-md shadow-sm focus:border-indigo-500 focus:ring focus:ring-indigo-200 focus:ring-opacity-50
        dark:bg-gray-800 dark:border-gray-600 dark:text-gray-200 dark:focus:border-indigo-400 dark:focus:ring-indigo-700 dark:focus:ring-opacity-50"
    >
      {languageOptions.map(({ language, code }, key) => (
        <option value={code} key={key}>
          {language}
        </option>
      ))}
    </select>
  );
};

export default LanguageSelector;
```

* Initialiser la langue avec la langue détectée par `i18next` ou la langue définie par défaut.
    
* Le Hook `useTranslation` expose l'instance `i18n` de `i18next` pour interagir avec les paramètres d'internationalisation.
    
* La fonction `handleLanguageChange` sera utilisée pour mettre à jour la langue sélectionnée par l'utilisateur. Elle est déclenchée lorsque l'utilisateur sélectionne une nouvelle langue dans le menu déroulant.
    

### **Implémentation de la direction du texte**

L'attribut `dir` en HTML est une fonctionnalité critique pour garantir l'accessibilité et l'inclusivité dans les applications web, en particulier lors de la gestion de langues qui diffèrent en direction du texte. Par exemple :

* **De gauche à droite (LTR)** : La plupart des langues, y compris l'anglais, le français et l'espagnol, suivent cette direction.
    
    **De droite à gauche (RTL)** : Les langues comme l'arabe et l'hébreu nécessitent que l'alignement du texte et la mise en page soient inversés pour maintenir la lisibilité et le contexte culturel.
    

Pour atteindre cet objectif dans notre application, nous définissons `document.body.dir` sur `dir` de `i18n` tout en écoutant les changements de sélection de langue en utilisant le Hook `useEffect`.

### **Basculer en mode sombre**

Créez le composant `DarkModeToggle` pour basculer entre le mode clair et le mode sombre selon la préférence de l'utilisateur.

```typescript
import { useEffect, useState } from "react";
import { SunIcon, MoonIcon } from "@heroicons/react/solid";

const DarkModeToggle = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    // Vérifier le stockage local ou la préférence système au premier chargement
    const isDark =
      localStorage.getItem("theme") === "dark" ||
      (!localStorage.getItem("theme") &&
        window.matchMedia("(prefers-color-scheme: dark)").matches);
    setDarkMode(isDark);
    document.documentElement.classList.toggle("dark", isDark);
  }, []);

  const toggleDarkMode = () => {
    setDarkMode(!darkMode);
    document.documentElement.classList.toggle("dark", !darkMode);
    localStorage.setItem("theme", !darkMode ? "dark" : "light");
  };

  return (
    <button
      aria-label="Basculer en mode sombre"
      onClick={toggleDarkMode}
      className="p-1 rounded"
    >
      {darkMode ? (
        <SunIcon
          className="w-6 h-6 text-yellow-500 "
          onClick={toggleDarkMode}
        />
      ) : (
        <MoonIcon className="w-6 h-6 text-gray-900 " onClick={toggleDarkMode} />
      )}
    </button>
  );
};

export default DarkModeToggle;
```

### **Composant d'en-tête**

Le composant `Header` sert de composant parent aux composants `DarkModeToggle` et `languageSelector`.

```typescript
import DarkModeToggle from "./DarkModeToggle";
import LanguageSelector from "./LanguageSelector";

const Header = () => {
  return (
    <header className="container flex justify-between">
      <DarkModeToggle />
      <LanguageSelector />
    </header>
  );
};

export default Header;
```

## Étape 4 : Composant principal de l'application

Dans le fichier `src/app`, incluez ce qui suit :

```typescript
import { useTranslation } from "react-i18next";
import Header from "./components/Header";

const App = () => {
  const { t } = useTranslation();

  const line1 = t("detail.line1");
  const line2 = t("detail.line2");

  return (
    <div className="h-[100vh] bg-white text-black dark:bg-gray-900 dark:text-white py-8">
      <Header />
      <div className="container text-center max-w-2xl mt-28">
        <h1 className="text-4xl font-bold">{t("greeting")}</h1>
        <p className="mt-8">{line1}</p>
        <p className="mt-2">{line2}</p>
      </div>
    </div>
  );
};

export default App;
```

* Le Hook `useTranslation` de `react-i18next` expose la fonction `t`, qui est utilisée pour récupérer le texte traduit.
    
* Il récupère la chaîne traduite en fonction d'une clé de vos fichiers de traduction (par exemple, `en.json`, `fr.json`).
    

En suivant ces étapes, votre application devrait maintenant être entièrement fonctionnelle avec des traductions intégrées de manière transparente. Voici à quoi ressemble le résultat final de notre application :

![Image de l'application en cours d'exécution sur localhost](https://cdn.hashnode.com/res/hashnode/image/upload/v1733099671232/67419cbe-ed58-4bb4-9e44-67de2ffa9be4.png align="center")

Consultez la [démo en direct](https://multilingual-demo.vercel.app/) et le code source sur [GitHub](https://github.com/timmy471/multilingual-demo)

## Conclusion

Créer des sites web qui offrent aux utilisateurs la flexibilité de sélectionner leur langue préférée n'est pas seulement une réalisation technique, mais une étape vers la création d'un web plus inclusif et accueillant.

En combinant l'internationalisation (i18n) avec des outils comme React-i18next et le style avec Tailwind CSS, vous pouvez construire des applications flexibles, conviviales et accessibles à un public mondial.

Dans ce projet, nous avons parcouru la configuration de i18n, l'ajout d'un sélecteur de langue et l'inclusion du "mode sombre" pour une meilleure utilisabilité.

## Références

[https://react.i18next.com/](https://react.i18next.com/)

[https://www.youtube.com/watch?v=dltHi9GWMIo](https://www.youtube.com/watch?v=dltHi9GWMIo)