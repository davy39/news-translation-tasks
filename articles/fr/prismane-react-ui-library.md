---
title: Aperçu de Prismane – Une bibliothèque d'interface utilisateur React open-source
subtitle: ''
author: valentine Gatwiri
co_authors: []
series: null
date: '2023-09-27T12:52:48.000Z'
originalURL: https://freecodecamp.org/news/prismane-react-ui-library
coverImage: https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-26-15-16-49.png
tags:
- name: Libraries
  slug: libraries
- name: React
  slug: react
seo_title: Aperçu de Prismane – Une bibliothèque d'interface utilisateur React open-source
seo_desc: 'Prismane is a free, comprehensive, have-it-all React UI library that provides
  a broad array of hooks, components, and form validators to help you build beautiful
  and functional user interfaces.

  Prismane was designed with performance in mind, ensuring...'
---

Prismane est une bibliothèque d'interface utilisateur React gratuite, complète et tout-en-un qui fournit un large éventail de hooks, de composants et de validateurs de formulaires pour vous aider à créer des interfaces utilisateur belles et fonctionnelles.

Prismane a été conçu en tenant compte de la performance, garantissant des temps de chargement ultra-rapides pour une meilleure expérience utilisateur.

Dans cet article, vous apprendrez ce qu'est Prismane, ses avantages et inconvénients, comment configurer notre environnement de développement et comment construire des applications en utilisant Prismane.

## Fonctionnalités clés de Prismane UI

La bibliothèque est une grande collection de 107+ composants React, incluant des boutons, des entrées, des menus, des tableaux, et plus encore. Cela permet aux développeurs de ne pas réinventer la roue chaque fois qu'ils ont besoin d'éléments d'interface utilisateur courants. De plus, vous pouvez les personnaliser selon vos préférences.

De plus, Prismane offre un support intégré pour le mode sombre, ce qui ajoute une couche supplémentaire d'accessibilité et de style à vos projets. De nombreux utilisateurs préfèrent le mode sombre car il réduit la fatigue oculaire et améliore la lisibilité dans des conditions de faible luminosité.

Il dispose également d'un support TypeScript, qui permet un développement sûr et sans erreur. TypeScript impose une typographie forte, ce qui signifie que les variables, les paramètres et les valeurs de retour doivent adhérer à des types de données spécifiques. Cela aide à attraper les erreurs liées aux types au moment de la compilation plutôt qu'à l'exécution, ce qui réduit la probabilité de problèmes inattendus dans votre code.

Prismane offre également un système de style personnalisé qui vous permet de créer et d'appliquer facilement des thèmes personnalisés à vos applications.

Enfin, il dispose d'une variété de hooks personnalisés, tels qu'un hook de construction de formulaire et un hook de notification toast, qui vous permettent d'encapsuler et de réutiliser une logique complexe dans différentes parties de votre application.

## Avantages de l'utilisation de Prismane UI

Les composants de l'interface utilisateur Prismane sont tous conçus pour suivre un guide de style cohérent, ce qui garantit que votre application a un aspect et une sensation polis et professionnels.

La bibliothèque offre également une variété d'options de style, ainsi que la possibilité de créer vos propres composants personnalisés. Elle est hautement personnalisable, vous pouvez donc facilement créer des interfaces utilisateur qui correspondent à vos besoins spécifiques.

En plus de cela, elle est gratuite et open source, ce qui vous donne la liberté d'exécuter, d'étudier, de modifier et de distribuer le logiciel. Cela signifie que vous avez le contrôle sur le fonctionnement du logiciel, ce qui peut être crucial pour la personnalisation et la sécurité.

Enfin, la bibliothèque est conçue pour être facile à utiliser – même pour les développeurs qui sont nouveaux dans React. Elle fournit aux développeurs une grande collection de composants et de hooks pré-construits, ce qui peut accélérer considérablement le processus de développement.

## Inconvénients de l'utilisation de Prismane UI

Prismane est une bibliothèque relativement nouvelle, donc elle peut ne pas avoir le même niveau de documentation, de fonctionnalités et de communauté que les bibliothèques plus anciennes et plus établies.

## Comment construire une application Prismane

Nous allons utiliser Next.js et Prismane pour développer notre application.

Commençons par nous assurer que notre environnement de développement est prêt.

Tout d'abord, installez Node.js (vous pouvez le télécharger [ici](https://nodejs.org/en) si vous ne l'avez pas déjà). La version 18 ou supérieure de Node.js est requise.

Dans ce tutoriel, nous allons utiliser Visual Studio Code, mais vous pouvez utiliser n'importe quel IDE de votre choix.

Maintenant, créons une application Next.js en exécutant la commande suivante :

```plaintext
npx create-next-app@latest nextjs-blog --use-npm --example "https://github.com/vercel/next-learn/tree/main/basics/learn-starter"
```

Ensuite, changez le répertoire pour le répertoire de notre projet en utilisant la commande suivante :

```bash
cd nextjs-blog
```

Lançons le serveur de développement en utilisant la commande suivante pour nous assurer que notre application fonctionne bien :

```plaintext
npm run dev
```

Après vous être assuré que tout est correct, appuyez sur `CTRL+C` et installez Prismane :

```bash
npm install @prismane/core
```

Dans `pages/index.js`, ajoutez le code suivant :

```jsx
import { Card, Image, Text, Button, Flex, fr, PrismaneProvider } from "@prismane/core";
import { Star, ShoppingCart } from "@phosphor-icons/react";


export default function App() {
  return (
    <PrismaneProvider>
    <Card w={360} gap={fr(2)} className="card">
      <Image
        src="https://img.freepik.com/free-photo/black-headphones-digital-device_53876-96805.jpg?size=626&ext=jpg&ga=GA1.1.460882575.1681882906&semt=sph"
        br="md"
        fit="cover"
        mb={fr(2)}
      />
      <Flex gap={fr(2)}>
        <Text fs="md" cl="green">
          <Star /> 4.5 (120 reviews)
        </Text>
        <Text fs="md" cl="blue">
          In Stock
        </Text>
      </Flex>
      <Text fs="lg" fw="bold" cl="black">
        Premium Headphones
      </Text>
      <Text cl="gray">
        Enjoy crystal-clear sound quality with our premium headphones, perfect
        for music lovers and audiophiles.
      </Text>
      <Text fw="bold" fs="2xl" cl="primary">
        $149.99
      </Text>
      <Flex gap={fr(4)} mt="auto">
        <Button cl="primary" bg="yellow">
          Add to Wishlist
        </Button>
        <Button cl="white" bg="blue">
          <ShoppingCart /> Add to Cart
        </Button>
      </Flex>
    </Card>
    </PrismaneProvider>
  );
}
```

Le code ci-dessus est un composant React qui rend une carte avec des informations sur un produit. Le code importe les composants et icônes nécessaires depuis les bibliothèques Prismane et Phosphor Icons, puis définit un composant nommé `App()`.

Le composant `App()` rend un composant `Card` avec les enfants suivants :

* Un composant `Image` avec l'image du produit

* Un conteneur `Flex` avec deux composants `Button`, l'un pour ajouter le produit à la liste de souhaits, et l'autre pour ajouter le produit au panier

* Un composant `Text` affichant le nom du produit

* Un composant `Text` affichant la description du produit

* Un composant `Text` affichant le prix du produit

* Un conteneur `Flex` avec deux composants `Button`, l'un pour ajouter le produit à la liste de souhaits et l'autre pour ajouter le produit au panier

Nous utilisons également les [props de style de Prismane](https://www.prismane.io/docs/styling/style-props) pour styliser notre application dans le code ci-dessus.

Prismane a son propre `reset.css`, donc il est automatiquement injecté lorsque l'application est enveloppée avec le composant `PrismaneProvider`.

## Comment styliser notre application

Ensuite, créons un fichier `_app.js` dans le dossier `pages` et ajoutons le code suivant :

```jsx
function App({ Component, pageProps }) {
    return (
      <Component {...pageProps} />
    );
  }

  export default App;
```

Dans une application Next.js, le fichier `_app.js` est un composant de mise en page spécial qui est utilisé pour envelopper toute notre application. Il sert de point d'entrée pour personnaliser le comportement et l'apparence de notre application sur toutes les pages.

Maintenant, stylisons notre application. Créez un fichier `global.css` dans notre dossier `pages` et ajoutez le code suivant :

```plaintext
@import url('https://fonts.googleapis.com/css2?family=Poppins:ital,wght@0,100;0,200;0,300;0,400;0,500;0,600;0,700;0,800;0,900;1,100;1,200;1,300;1,400;1,500;1,600;1,700;1,800;1,900&display=swap');

  .card {
    font-family: Poppins, sans-serif;
  }
  body {
    width: 100vw;
    height: 100vh;
    display: flex;
    background-color: rgb(var(--prismane-colors-base-300));
  }
```

Le code importe la police `Poppins` depuis Google Fonts et l'applique à l'élément `.card`. Il définit également la largeur, la hauteur, la propriété d'affichage et la couleur de fond pour l'élément `body`.

Enfin, importons notre fichier `global.css` dans notre fichier `app.js` en ajoutant la ligne de code suivante :

```jsx
import './global.css';
```

Vous pouvez trouver le code complet [ici](https://github.com/gatwirival/prismane-ui-demo).

Et voici la sortie du code :

![Image](https://www.freecodecamp.org/news/content/images/2023/09/Screenshot-from-2023-09-26-13-34-29.png align="left")

*Sortie*

Ce n'est qu'un simple exemple de la façon de développer une application web en utilisant Prismane. Il existe de nombreuses autres fonctionnalités et options disponibles dans Prismane UI que vous pouvez utiliser pour créer des applications plus complexes et sophistiquées.

## Conclusion

Dans l'ensemble, Prismane UI est une excellente bibliothèque d'interface utilisateur React qui offre une large gamme de fonctionnalités et d'avantages. C'est un bon choix pour les développeurs de tous niveaux d'expérience, et elle est bien adaptée à une variété de projets.

## Références

[Site web de Prismane](https://www.prismane.io/)

[Site web de Next.js](https://nextjs.org/learn/basics/create-nextjs-app)

[Dépôt Phosphor-icons](https://github.com/phosphor-icons/react)