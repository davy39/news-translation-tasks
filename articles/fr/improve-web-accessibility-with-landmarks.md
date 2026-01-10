---
title: Comment améliorer l'accessibilité Web avec les repères - Expliqué avec des
  exemples
subtitle: ''
author: Ilknur Eren
co_authors: []
series: null
date: '2025-08-05T20:51:05.799Z'
originalURL: https://freecodecamp.org/news/improve-web-accessibility-with-landmarks
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1754425989581/1302898e-439b-4666-af27-cf1b091c6975.png
tags:
- name: Accessibility
  slug: accessibility
- name: Web Development
  slug: web-development
seo_title: Comment améliorer l'accessibilité Web avec les repères - Expliqué avec
  des exemples
seo_desc: If you’re reading this article on the freeCodeCamp publication, you should
  see some visual clues in different sections of the page. The header is at the top
  of the page. If you scroll all the way to the bottom of the page, you can see the
  footer sect...
---

Si vous lisez cet article sur la publication freeCodeCamp, vous devriez voir certains indices visuels dans différentes sections de la page. L'en-tête se trouve en haut de la page. Si vous faites défiler jusqu'en bas de la page, vous pouvez voir la section de pied de page avec un fond gris, qui est clairement séparée du corps avec un fond blanc.

freeCodeCamp, comme d'autres sites web, sépare visuellement les sections de la page pour donner des indices à l'utilisateur afin qu'il puisse naviguer facilement entre les sections.

Alors que les utilisateurs voyants ont des indices visuels sur les sections, ceux qui utilisent des technologies d'assistance comme un lecteur d'écran, s'appuient sur les repères pour naviguer à travers la page.

En termes simples, les repères sont des régions sémantiques dans une page web qui définissent le but de ses sections. Les repères permettent aux technologies d'assistance de sauter entre les principales parties de la page, tout comme les utilisateurs voyants scannent visuellement les titres ou les menus.

Les repères HTML courants incluent :

* `<header>` – Représente le contenu introductif ou l'en-tête de la page.

* `<nav>` – Identifie les liens de navigation.

* `<main>` – Marque la zone de contenu principal de la page.

* `<aside>` – Contient des informations complémentaires ou connexes.

* `<footer>` – Représente le pied de page ou la section de pied de page.

## Table des matières

* [Comment naviguer entre les repères dans n'importe quel navigateur](#heading-comment-naviguer-entre-les-reperes-dans-nimporte-quel-navigateur)

* [Comment naviguer à travers les repères avec Voice Over sur Mac](#heading-comment-naviguer-a-travers-les-reperes-avec-voice-over-sur-mac)

* [Pourquoi les repères sont importants pour l'accessibilité](#heading-pourquoi-les-reperes-sont-importants-pour-laccessibilite)

* [Comment utiliser les repères](#heading-comment-utiliser-les-reperes)

* [Exemples concrets de chaque repère](#heading-exemples-concrets-de-chaque-repere)

* [Réflexions finales](#heading-reflexions-finales)

## Comment naviguer entre les repères dans n'importe quel navigateur

### Support général des navigateurs

La plupart des lecteurs d'écran supportent la navigation par repères avec des raccourcis clavier. Voici un aperçu de base :

| Lecteur d'écran | OS | Raccourci |
| --- | --- | --- |
| VoiceOver | macOS | `Control + Option + U` (pour ouvrir le Rotor), puis les touches fléchées pour naviguer |
| NVDA | Windows | `D` pour passer au repère suivant |
| JAWS | Windows | `R` pour parcourir les régions |
| Narrator | Windows | `Caps Lock + Flèche droite` pour se déplacer par repère |
| ChromeVox | Chrome OS | `Recherche + Flèche gauche/droite` pour se déplacer entre les repères |

Ces raccourcis permettent aux utilisateurs de sauter entre les régions—par exemple, du contenu `<main>` directement au `<footer>`—sans avoir à tabuler à travers chaque élément interactif.

## **Comment naviguer à travers les repères avec Voice Over sur Mac**

1. **Activer VoiceOver** : Vous pouvez facilement activer VoiceOver en ouvrant le Finder et en tapant VoiceOver. Activez VoiceOver.

    ![Finder recherchant le mot "voiceOver" En dessous se trouve VoiceOver avec un bouton pour l'activer. En dessous se trouve VoiceOver Utility](https://cdn.hashnode.com/res/hashnode/image/upload/v1753898345534/2fba73d7-b102-41ce-8731-f865a71631e6.png align="center")

2. **Ouvrir le rotor** : Une fois VoiceOver activé, appuyez sur Control+Option+U sur votre clavier. Cela ouvrira le rotor VoiceOver. Vous pouvez appuyer sur les flèches droite et gauche pour passer à travers différents éléments du rotor qui incluent la navigation avec tous les titres, les liens et les repères. La capture d'écran ci-dessous montre l'option des éléments de repère du rotor d'accessibilité sur un article freeCodeCamp. L'article est divisé en éléments de navigation, recherche, principal, article et pied de page.

![Titre des repères suivi de navigation, recherche, principal, article et pied de page](https://cdn.hashnode.com/res/hashnode/image/upload/v1753897939501/ddef4a40-047d-469c-80e3-add29ff8f297.png align="center")

3. **Appuyez sur les flèches haut et bas pour naviguer entre les repères** : Une fois que vous êtes sur les éléments de repère du rotor d'accessibilité, vous pouvez appuyer sur les flèches haut et bas pour naviguer vers différentes sections de la page. Si vous voulez aller au pied de page, appuyez sur la flèche bas jusqu'à atteindre le pied de page, puis appuyez sur Entrée.

## **Pourquoi les repères sont importants pour l'accessibilité**

### **1. Navigation plus facile pour les utilisateurs de lecteurs d'écran**

Les lecteurs d'écran fournissent des raccourcis pour naviguer à travers les repères. Sans repères, les utilisateurs doivent tabuler à travers chaque lien ou élément, ce qui est frustrant et chronophage. Dans l'exemple de l'article freeCodeCamp, l'utilisateur pourrait vouloir sauter au pied de page afin de trouver et cliquer sur le lien de donation. Sans repères, l'utilisateur devra tabuler à travers tout l'article pour atteindre le pied de page. Cela prend du temps et est épuisant. Les repères offrent une navigation facile aux utilisateurs qui dépendent des lecteurs d'écran.

### **2. Structure cohérente à travers les pages**

Lorsque chaque page utilise la même structure de repères, les utilisateurs peuvent prédire où se trouvent les menus de navigation, le contenu principal et les barres latérales. Cette prévisibilité réduit la charge cognitive. En organisant la page en sections, vous pouvez facilement déterminer où aller ensuite.

### **3. Contexte et orientation clairs**

Les repères communiquent le **rôle** du contenu. Par exemple :

* Le repère `main` signale : *« C'est le contenu principal de la page. »*

* Le repère `aside` signale : *« C'est un contenu supplémentaire ou connexe. »*

Cela aide les utilisateurs à décider quelles zones sauter ou sur lesquelles se concentrer.

## Comment utiliser les repères

### ✅ **Structure de base des repères**

Voici un exemple de page utilisant des repères HTML5 :

```plaintext
<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <title>Exemple de repères accessibles</title>
</head>
<body>

  <header>
    <h1>Logo du site</h1>
    <nav>
      <ul>
        <li><a href="#accueil">Accueil</a></li>
      </ul>
    </nav>
  </header>

  <main>
    <h2>Zone de contenu principal</h2>
    <p>Ceci est le contenu principal de la page.</p>
  </main>

  <aside>
    <h3>Liens connexes</h3>
    <ul>
      <li><a href="#ressource1">Ressource 1</a></li>
    </ul>
  </aside>

  <footer>
    <p>2025 Exemple de société</p>
  </footer>

</body>
</html>
```

Le HTML est divisé en 5 sections de repères qui sont l'en-tête, la navigation, le contenu principal, la barre latérale et le pied de page. Si le lecteur d'écran veut sauter l'en-tête et aller directement au contenu principal, il peut le faire en tournant le rotor d'accessibilité et en cliquant sur le repère principal. Les repères permettent aux utilisateurs de lecteurs d'écran de naviguer facilement à travers la page.

Voici une description de ce que chaque repère est et comment il est typiquement utilisé :

### `<nav>` – Section de navigation

Utilisé pour les menus, les liens du site ou les fil d'Ariane.

```plaintext
<nav>
  <ul>
    <li><a href="/a-propos">À propos</a></li>
    <li><a href="/cours">Cours</a></li>
  </ul>
</nav>
```

**Utilisation réelle** : Sauter directement à la navigation pour trouver la page « Contact » sans parcourir tout le contenu.

### `<main>` – Contenu principal de la page

Utilisé une fois par page pour envelopper le contenu le plus important.

```plaintext
<main>
  <h1>Apprendre l'accessibilité</h1>
  <p>Cet article explique comment utiliser les repères...</p>
</main>
```

**Utilisation réelle** : Sauter l'en-tête et la barre latérale pour plonger dans le tutoriel ou l'article.

### `<aside>` – Informations complémentaires

Utilisé pour les barres latérales, les publicités, les liens connexes ou les citations.

```plaintext
<aside>
  <h3>Tutoriels connexes</h3>
  <ul>
    <li><a href="/accessibilite/formulaires">Formulaires accessibles</a></li>
  </ul>
</aside>
```

**Utilisation réelle** : Les utilisateurs peuvent sauter la barre latérale s'ils ne veulent pas de contenu supplémentaire, ou y sauter pour des ressources utiles.

### `<footer>` – Pied de page

Utilisé pour le contenu de clôture comme les droits d'auteur.

```plaintext
<footer>
  <p>&copy; 2025 FreeCodeCamp. Tous droits réservés.</p>
</footer>
```

**Utilisation réelle** : Naviguer rapidement vers les liens de support, les informations de licence ou l'inscription à une newsletter.

### `<header>` – En-tête de page ou de section

Utilisé pour le contenu introductif, comme les logos ou les barres de recherche.

```plaintext
<header>
  <img src="logo.png" alt="Logo du site" />
  <form role="search">
    <input type="text" aria-label="Rechercher sur le site" />
  </form>
</header>
```

**Utilisation réelle** : Accéder rapidement à l'entrée de recherche ou revenir à la page d'accueil.

## **Réflexions finales**

Les repères ne sont pas seulement un bonus d'accessibilité—ils font partie intégrante d'une bonne UX. En implémentant correctement les repères, vous rendez votre site plus facile à naviguer pour les utilisateurs handicapés, vous conformez aux WCAG et créez une structure plus prévisible pour tout le monde.