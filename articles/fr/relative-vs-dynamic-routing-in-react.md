---
title: Relatif Vs Routage Dynamique dans React – Différentes Méthodes de Routage avec
  Exemples
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-08-12T13:57:55.370Z'
originalURL: https://freecodecamp.org/news/relative-vs-dynamic-routing-in-react
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1723295443613/2cf6a928-b2b1-4f71-a6ba-a307b6c13dc9.png
tags:
- name: Web Development
  slug: web-development
- name: React
  slug: reactjs
seo_title: Relatif Vs Routage Dynamique dans React – Différentes Méthodes de Routage
  avec Exemples
seo_desc: 'Single-Page Applications (SPAs) have been growing in popularity as people
  become accustomed to better user experiences and improved application responsiveness.
  This is in part thanks to the introduction of Client-Side Routing (CSR).

  CSR enables navig...'
---

Les Applications à Page Unique (SPA) gagnent en popularité à mesure que les utilisateurs s'habituent à de meilleures expériences utilisateur et à une réactivité améliorée des applications. Cela est en partie grâce à l'introduction du Routage Côté Client (CSR).

Le CSR permet la navigation entre les pages sans avoir à envoyer de requêtes de navigation au serveur. Au lieu de cela, il fournit des mises à jour de contenu instantanées lors de la navigation. Il le fait en manipulant la pile d'historique du navigateur sans faire de requête pour un document au serveur.

Les avantages de l'utilisation du CSR dans la construction d'applications à page unique sont :

* Il améliore l'expérience utilisateur car il permet des transitions plus fluides entre les pages, résultant en des interactions plus rapides.
  
* Il augmente les performances d'une application, car le chargement des ressources telles que JavaScript, CSS et images est fait une seule fois et est ensuite réutilisé.
  
* Il réduit les multiples requêtes de pages traitées par le serveur, résultant en une utilisation réduite de la bande passante et un temps de réponse plus rapide.
  

React, la bibliothèque la plus populaire pour construire des interfaces utilisateur dynamiques et complexes, permet le CSR grâce à `React Router`. React Router est une bibliothèque tierce qui gère la navigation et le routage dans les applications React. De grandes entreprises telles que Shopify, Spotify, Mozilla et Gumroad (pour n'en nommer que quelques-unes) utilisent React Router sur leurs sites web.

Dans cet article, nous allons plonger en profondeur dans les types de routage utilisés dans les applications web React : le routage `Relatif` et `Dynamique`.

À la fin de cet article, vous aurez une bonne connaissance de ces méthodes de routage, et vous serez en mesure de les différencier. Vous serez également en mesure d'identifier leurs meilleurs cas d'utilisation et même de les combiner pour obtenir les résultats de routage souhaités dans votre application React.

### **Prérequis**

Pour bien comprendre ce que nous allons discuter dans cet article, vous devez avoir une connaissance de base du routage React.

Si vous avez besoin de réviser, vous pouvez lire mon article sur [React Router](https://www.freecodecamp.org/news/use-react-router-to-build-single-page-applications/). Si vous êtes prêt, alors plongeons directement dedans !

### Routage Relatif

Le routage relatif est une manière de définir des routes en référence à leurs routes parent. Il permet la navigation vers différents chemins ou routes au sein d'une application en fonction de l'emplacement actuel plutôt qu'un point spécifié qui est généralement la racine de l'application.

Le routage relatif fonctionne avec des chemins relatifs qui spécifient l'emplacement d'un composant par rapport à la route parent. Nous pouvons également dire que les chemins relatifs sont sensibles au contexte.

Voici un exemple simple de routage relatif utilisant des chemins relatifs :

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="about" element={<About />} />
</Routes>;
```

* Le chemin de la route racine `/` rend le composant `Home`.
  
* Le `<Route path="about" element={<About />} />` est une route relative qui définit le chemin relatif de `about`. Il est relatif car il considère le chemin racine `/` comme son parent.
  

Dans une structure de route relative imbriquée, cela fonctionne de la même manière et s'ajoute toujours à sa route parent.

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="about" element={<About />} />
  <Route path="dashboard" element={<Dashboard />}>
    <Route path="profile" element={<Profile />} />
  </Route>
</Routes>;
```

* La route `Dashboard` définissant le chemin `dashboard` reste une route relative.
  
* La route `Profile` définissant le chemin `profile` est imbriquée dans la route `dashboard`, ce qui la rend relative au chemin `dashboard`. Le chemin complet pour `Profile` sera maintenant `/dashboard/profile`.
  

### **Routage Absolu**

Le routage absolu est similaire au routage relatif mais avec une légère différence. Les chemins absolus dans une application peuvent être distinctement différenciés par la barre oblique initiale `(/)`. La barre oblique initiale préfixe le nom du chemin et indique que le chemin est considéré à partir du niveau racine de l'application.

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
</Routes>;
```

* Le chemin `about` est une route absolue, définissant un chemin `about` absolu et référençant directement la racine de l'application.
  

Dans une structure de route imbriquée absolue, cela ressemble à ceci :

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="/dashboard/profile" element={<Profile />} />
  </Route>
</Routes>;
```

* La route imbriquée `profile` définit le chemin `/dashboard/profile` comme un chemin absolu et rend le composant `Profile` lorsque l'URL correspond à `/dashboard/profile`.
  

#### **Différences entre le Routage Relatif et Absolu**

1. **Flexibilité :** Le routage relatif est plus flexible pour les structures de routes imbriquées car les chemins relatifs s'adaptent automatiquement aux changements des routes parent. Pour le routage absolu, les changements apportés aux routes parent nécessiteront une mise à jour de toutes les routes enfant.
  
2. **Structure :** Les routes relatives sont plus simples à gérer même dans une structure de routes imbriquées, car les routes enfant s'ajoutent par défaut à la route parent. Le routage absolu, en revanche, peut devenir difficile à gérer dans une structure de routes imbriquées complexe car chaque chemin doit être explicitement spécifié.
  
3. **Clarté :** Dans une structure de routes imbriquées, il peut être difficile de comprendre la structure hiérarchique dans le routage relatif. C'est beaucoup plus facile dans le routage absolu, car les chemins sont clairs, concis et directs pour les routes non imbriquées.
  

### Routage Dynamique

Les applications utilisent généralement des données, qui peuvent être des données pour les utilisateurs ou les produits et les entrées utilisateur. Les données peuvent être uniques, et elles peuvent également changer à tout moment, les rendant dynamiques.

Le routage dynamique définit des routes qui peuvent changer en fonction de certains paramètres en utilisant des paramètres de route ou des segments d'URL. Les paramètres ajoutés au chemin de la route permettent à l'application de gérer les routes de manière dynamique et de rendre différents éléments en fonction de l'URL, comme vous pouvez le voir dans l'exemple ci-dessous :

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="profile/:id" element={<Profile />} />
  </Route>
</Routes>;
```

* La route `Profile` avec un segment dynamique `:id` correspondant à `profile/:id`. Les correspondances possibles pour ce chemin dynamique peuvent être `profile/123` ou `profile/abc123`.
  

L'exemple ci-dessus montre le routage relatif avec le routage dynamique. Nous pouvons également utiliser le routage absolu avec le routage dynamique :

```markdown
<Routes>
  <Route path="/" element={<Home />} />
  <Route path="/about" element={<About />} />
  <Route path="/dashboard" element={<Dashboard />}>
    <Route path="/dashboard/profile/:id" element={<Profile />} />
  </Route>
</Routes>;
```

**Différences entre le Routage Statique et Dynamique**

1. **Flexibilité :** La capacité à définir un chemin de route selon un paramètre rend les routes dynamiques flexibles et réactives à l'interaction utilisateur. Les routes statiques sont fixes et ne changent pas.
  
2. **Complexité :** Les routes dynamiques impliquent souvent des segments dynamiques comme des paramètres et une logique conditionnelle qui peut être difficile à comprendre. Les routes statiques sont simples et non complexes.
  
3. **Cas d'utilisation :** Les routes dynamiques sont utilisées pour les pages qui dépendent des entrées utilisateur ou des données. Les routes statiques sont utilisées pour les pages qui ne changent pas.
  

### Comment Combiner le Routage Relatif et Dynamique

Si vous souhaitez créer un système de navigation plus complexe ou robuste qui inclut des structures de routes hiérarchiques et imbriquées, il est préférable de combiner à la fois le routage relatif et dynamique.

La combinaison des deux méthodes de routage ressemble à ceci :

```markdown
<Routes>
  <Route>
    <Route path="/categories" element={<Categories />}>
      <Route path=":categoryId" element={<CategoryDetails />}>
        <Route path="product/:productId" element={<ProductDetails />} />
      </Route>
    </Route>
  </Route>
</Routes>;
```

* Cet exemple montre une structure de route profondément imbriquée avec à la fois des routes relatives et dynamiques.
  
* Le chemin de correspondance complet sera `/categories/:categoryId/product/:productId`.
  

**Avantages de la Combinaison du Routage Relatif et Dynamique**

1. **Flexibilité :** Une combinaison de routage relatif et dynamique est idéale pour construire une structure de navigation robuste. Cela est dû à sa flexibilité et sa polyvalence pour définir certaines routes de manière relative et d'autres routes créées dynamiquement en fonction des données ou des entrées utilisateur.
  
2. **Expérience Utilisateur Améliorée :** Les méthodes de routage combinées offriront aux utilisateurs le meilleur des deux méthodes lors de l'interaction, les laissant satisfaits.
  

### Conclusion

Dans cet article, nous avons discuté du routage dans les applications web React et appris les méthodes de routage utilisées dans React Router : le routage relatif et dynamique. Ils jouent tous deux des rôles cruciaux dans le routage côté client au sein des applications React, et offrent différents avantages selon les cas d'utilisation.

Comprendre et mettre en œuvre ces méthodes de routage peut améliorer l'expérience utilisateur et rendre votre application React à la fois maintenable et évolutive.

Si vous avez aimé lire cet article, vous pouvez [M'offrir un Café](https://buymeacoffee.com/timothyolanrewaju).

Vous pouvez également me connecter sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) pour plus de publications et d'articles perspicaces.

À la prochaine !