---
title: Comment utiliser GitHub Discussions comme système de chat pour votre blog
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-05-13T15:48:14.000Z'
originalURL: https://freecodecamp.org/news/github-discussions-as-chat-system
coverImage: https://www.freecodecamp.org/news/content/images/2022/05/GitHub-Discussions-as-chat-system-1.png
tags:
- name: blog
  slug: blog
- name: Chat
  slug: chat
- name: GitHub
  slug: github
seo_title: Comment utiliser GitHub Discussions comme système de chat pour votre blog
seo_desc: "By Rakesh Potnuru\nIf you have a personal blog, you might be using a comment\
  \ system to manage your blog's discussions and comments. If so, it's time to think\
  \ about updating your comment system. \nYou can take your blog's comments to the\
  \ next level with..."
---

Par Rakesh Potnuru

Si vous avez un blog personnel, vous utilisez probablement un système de commentaires pour gérer les discussions et les commentaires de votre blog. Si c'est le cas, il est temps de penser à mettre à jour votre système de commentaires. 

Vous pouvez faire passer les commentaires de votre blog au niveau supérieur avec l'aide de GitHub Discussions. Dans cet article, je vais expliquer comment intégrer GitHub Discussions à votre blog et en tirer le meilleur parti.

## Qu'est-ce que "GitHub Discussions" ?

![Page des discussions GitHub](https://www.freecodecamp.org/news/content/images/2022/05/screely-1652334880222-1.png)
_[GitHub Discussions](https://github.com/facebook/create-react-app/discussions)_

[GitHub Discussions](https://docs.github.com/en/discussions) est un forum qui peut être activé sur chaque dépôt GitHub. Il permet aux développeurs de discuter de nouvelles fonctionnalités, d'obtenir des retours de la communauté, de créer des sondages, de faire des annonces, et plus encore. 

GitHub Discussions est un lieu de collaboration unique pour les développeurs et les membres de la communauté. 

## Comment utiliser GitHub Discussions comme système de chat

Pour intégrer GitHub Discussions à votre blog, nous allons utiliser **[giscus](https://giscus.app/)**.

![Site web de giscus](https://www.freecodecamp.org/news/content/images/2022/05/screely-1652335682833.png)
_[giscus](https://giscus.app/)_

giscus est un système de commentaires basé sur GitHub Discussions. Il vous permet d'intégrer les discussions de votre dépôt à votre blog. 

Vos lecteurs peuvent laisser des commentaires sur votre blog, qui apparaîtront à la fois sur le blog et sur la page des discussions de votre dépôt.

### Avantages de l'utilisation de Discussions comme système de chat pour votre blog

* C'est complètement gratuit
* Il n'y a pas de publicités ni de suivi
* C'est très puissant
* Vous avez un contrôle complet sur les commentaires et une autorité de modération totale.
* Il y a beaucoup de thèmes
* C'est assez personnalisable
* Vous pouvez l'auto-héberger sur vos propres serveurs

Gardez simplement à l'esprit que cet outil est principalement adapté aux blogs de développeurs, car ce sont surtout les développeurs qui utilisent GitHub.

## Comment intégrer giscus dans votre blog

### Prérequis

* Un blog (vous devez avoir accès au code source)
* Un [compte GitHub](https://github.com/)
* Votre dépôt sélectionné doit être public

Tout d'abord, vous devrez activer les discussions pour votre dépôt.

Allez dans les **Paramètres** du dépôt -> Dans la section **Fonctionnalités** -> Cochez la case Discussions.

![Discussions activées](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-123606.png)
_Discussions activées_

Ensuite, installez l'application giscus dans votre dépôt.

Allez sur [https://github.com/apps/giscus](https://github.com/apps/giscus), suivez les instructions et donnez accès uniquement au dépôt sélectionné.

![Sélection de l'accès au dépôt](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-124524.png)
_Accès au dépôt_

Maintenant, la partie importante : nous devons configurer le widget giscus.

Tout d'abord, allez sur la [page d'accueil](https://giscus.app/) de giscus et faites défiler jusqu'à la section **Configuration**.

Sélectionnez la langue de votre widget. Il s'agit de la langue dans laquelle vous souhaitez afficher votre widget.

![Sélection de la langue](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-125354.png)
_Sélection de la langue_

Ensuite, tapez le **nom de votre dépôt** ainsi que votre **nom d'utilisateur** comme `username/reponame`.

![Saisie du nom du dépôt avec le nom d'utilisateur](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-125933.png)
_Saisie du nom du dépôt avec le nom d'utilisateur_

Pour le **Mappage Page ↔️ Discussions**, je recommande de choisir "Le titre de la discussion contient l'URL de la page". Mais selon vos besoins, choisissez celui qui vous convient le mieux.

![Mappage Page ↔️ Discussions](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-130653.png)
_Mappage Page ↔️ Discussions_

Ensuite, créez une catégorie dans votre page de discussions sur votre dépôt GitHub – quelque chose comme "Commentaires" – ou choisissez une catégorie existante.

![Création d'une catégorie de discussion](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-131045.png)
_Création d'une catégorie de discussion_

![Choix de la catégorie](https://www.freecodecamp.org/news/content/images/2022/05/Screenshot-2022-05-12-131542.png)
_Choix de la catégorie_

Ensuite, activez les **Fonctionnalités** optionnelles si vous le souhaitez.

Puis, sélectionnez le thème. Et ne vous inquiétez pas – vous pouvez basculer entre différents thèmes de manière programmatique.

Enfin, copiez et collez le code généré.

giscus générera une balise de script basée sur vos paramètres, que vous pouvez coller dans votre code. Mais nous allons voir comment utiliser le composant giscus.

### Comment utiliser giscus-component

Si votre blog est construit avec React/Vue/Svelte ou des composants Web, vous pouvez installer le composant giscus.

Par exemple, pour intégrer giscus dans React, procédez comme suit :

* Installez le package giscus.

```bash
npm i @giscus/react

ou

yarn add @giscus/react
```

* Ensuite, importez `giscus` dans votre composant et utilisez-le. Copiez les attributs que nous avons obtenus à l'étape précédente, retirez `data-` de tous les attributs et convertissez les attributs en attributs `jsx` valides.

```js
import Giscus from '@giscus/react';

export default function MyApp() {
  return (
    <Giscus
      id="comments"
      repo="giscus/giscus-component"
      repoId="MDEwOlJlcG9zaXRvcnkzOTEzMTMwMjA="
      category="Announcements"
      categoryId="DIC_kwDOF1L2fM4B-hVS"
      mapping="specific"
      term="Welcome to @giscus/react component!"
      reactionsEnabled="1"
      emitMetadata="0"
      inputPosition="top"
      theme="light"
      lang="en"
      loading="lazy"
    />
  );
}
```

C'est essentiellement la même procédure pour les autres frameworks.

## Voici le résultat final

Voici comment tout cela fonctionne :

![Résultat final](https://www.freecodecamp.org/news/content/images/2022/05/ezgif-4-4662469443-2.gif)
_Résultat final_

## Conclusion

Dans cet article, nous avons appris les avantages de l'utilisation de GitHub Discussions comme système de chat. Nous avons également appris comment créer et intégrer le widget giscus dans notre site web.

J'espère que vous avez trouvé cela utile. N'oubliez pas de ⭐ le [dépôt GitHub](https://github.com/giscus) de giscus pour les soutenir.

Suivez-moi sur [Twitter](https://twitter.com/rakesh_at_tweet) où je partage des conseils aléatoires, des ressources et mes apprentissages autour du développement web et de la rédaction technique.