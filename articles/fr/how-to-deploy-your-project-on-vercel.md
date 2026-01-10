---
title: Comment déployer votre projet sur Vercel avec un domaine personnalisé
subtitle: ''
author: Okoro Emmanuel Nzube
co_authors: []
series: null
date: '2024-10-25T19:35:48.953Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-your-project-on-vercel
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729806244084/f4aca70a-801e-4577-8073-e078323db51a.jpeg
tags:
- name: deployment
  slug: deployment
seo_title: Comment déployer votre projet sur Vercel avec un domaine personnalisé
seo_desc: 'Have you ever built a project but found it difficult to make it live on
  the internet? Well, worry no more because this article will help you do that.

  In this article, I will introduce you to one of the fastest and easiest deployment
  platforms for bri...'
---

Avez-vous déjà construit un projet mais trouvé difficile de le mettre en ligne sur Internet ? Ne vous inquiétez plus, car cet article va vous aider à le faire.

Dans cet article, je vais vous présenter l'une des plateformes de déploiement les plus rapides et les plus faciles pour mettre votre code/projet sur le web.

Je vais également vous montrer comment déployer une application web avec votre domaine personnalisé et pourquoi il est important de le faire.

Plongeons directement dans le sujet.

## Table des matières

* [Aperçu de Vercel](#heading-aperçu-de-vercel)
    
* [Qu'est-ce que les domaines ?](#heading-quest-ce-que-les-domaines)
    
* [Comment créer un compte Vercel](#heading-comment-creer-un-compte-vercel)
    
* [Comment configurer un domaine personnalisé](#heading-comment-configurer-un-domaine-personnalise)
    
* [Conclusion](#heading-conclusion)
    

## **Aperçu de Vercel**

Vercel est une plateforme d'hébergement cloud qui fournit des outils permettant aux développeurs de construire, déployer et mettre à l'échelle leurs applications web. Un fait important à propos de cette plateforme est qu'elle est rapide, facile à naviguer/utiliser, et très efficace.

Vercel supporte et déploie de nombreux frameworks avec une configuration minimale, en particulier les frameworks construits avec JavaScript. Voici une liste des frameworks qui peuvent être déployés sur Vercel : Angular, Astro, Brunch, React, Dojo, Gatsby.js, Next.js, Nuxt.js, Vite, Vue.js, Vuepress, et bien d'autres.

Vous ne connaissez peut-être pas tous ces frameworks à ce stade, mais il est important de savoir que Vercel supporte ces frameworks et bien d'autres.

Consultez la [documentation de Vercel](https://vercel.com/docs/frameworks/more-frameworks) pour en voir plus.

## **Qu'est-ce que les domaines ?**

Les domaines sont des "identifiants uniques" utilisés pour localiser ou trouver un site web spécifique sur Internet. Par exemple, [freecodeCamp.org](http://freecodeCamp.org). Chaque fois que vous voyez un nom de domaine, vous devriez avoir une idée du site web auquel il appartient.

Il est important de noter qu'un nom de domaine peut être créé avec une combinaison de lettres (A-z), de chiffres (0-9) et de traits d'union.

### **Importance d'avoir un nom de domaine**

Voici quelques raisons pour lesquelles vous devriez avoir un nom de domaine :

* **Facile à trouver et à localiser :** Avoir un nom de domaine facilite la recherche de votre entreprise et augmente également la possibilité de réaliser plus de ventes depuis votre page web. Si vous avez un magasin physique, tout le monde ne voudra pas forcément le visiter.
    
* **Pour le professionnalisme et la crédibilité :** Imaginez avoir une entreprise mais pas de site web ou de domaine. Cela vous fera paraître peu professionnel aux yeux des clients, car ils pourraient ne pas vous prendre au sérieux.
    
* **Augmentez votre présence en ligne :** Avec un nom de domaine, votre présence en ligne ou celle de votre marque est augmentée, ce qui vous rend plus visible.
    

Maintenant, parlons de la création d'un compte Vercel. Ce processus est en réalité simple et facile à suivre.

## **Comment créer un compte Vercel**

La première étape consiste à visiter [Vercel](https://vercel.com/).

Sur la page d'accueil de Vercel, cliquez sur le bouton d'inscription, situé en haut à droite de la page d'accueil.

![Page d'accueil de Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1729808253459/5946836c-3de9-4d27-bb5a-dd992446bd9c.png align="center")

Choisissez votre "Type de plan" puis entrez votre nom. Ensuite, cliquez sur Continuer pour procéder.

![Processus de configuration de Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1729807310680/e4872073-f8de-4e74-9555-281cf96efa01.png align="center")

Ensuite, connectez le compte depuis lequel vous importerez votre projet. Vous aurez trois options : GitHub, GitLab ou BitBucket.

![Lier votre compte GitHub, GitLab ou Bitbucket à Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1729807383749/7bab422e-87cd-4b9a-b254-25af80f9a73b.png align="center")

Dans mon cas, j'ai cliqué sur "Continuer avec GitHub".

**Note :** Si vous n'avez pas de compte GitHub, vous pouvez lire comment en créer un [ici](https://www.freecodecamp.org/news/git-and-github-the-basics/).

Une fois que vous avez lié votre compte GitHub avec Vercel, l'interface devrait ressembler à ceci :

![Interface de configuration complète de Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1729807623924/c44c31f2-e77a-4538-9a86-c80d06680779.png align="center")

À ce stade, vous avez terminé la configuration de votre compte Vercel. L'étape suivante consiste à déployer votre projet.

D'après la description de l'image ci-dessus, vous pouvez voir un bouton "import". Allez dans le projet particulier que vous souhaitez déployer et cliquez sur le bouton d'importation. Dans mon cas, j'ai nommé mon dépôt de projet "practice-purpose".

Une fois que vous cliquez sur le bouton d'importation, cela devrait vous mener à la page suivante où vous pouvez entrer le nom de votre projet et enfin le déployer.

![Interface de configuration de déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1729807744450/3eaf81e5-f53c-45bb-9890-166516ff17c4.png align="center")

Attendez quelques minutes pour que le déploiement soit terminé. Après cela, votre interface devrait ressembler à ceci :

![Interface après déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1729807863920/fcfdfaa7-a42e-451a-b539-74dc151eca69.png align="center")

Félicitations ! À ce stade, vous avez déployé votre premier projet.

## **Comment configurer un domaine personnalisé**

Avant de continuer avec le processus de configuration d'un domaine personnalisé, vous devez avoir votre domaine prêt. Si ce n'est pas le cas, j'ai ajouté une vidéo rapide qui vous guidera.

%[https://youtu.be/JRRXTR7PUug?si=ag-HnhZtpIJPpgJd]

Pour cet article, j'utiliserai Namecheap, car c'est là que j'ai obtenu le domaine que j'utilise. N'hésitez pas à utiliser le fournisseur de domaine de votre choix.

À ce stade, votre nom de domaine devrait être disponible. Si c'est le cas, continuons.

Sur votre page de déploiement sur Vercel, cliquez sur "Domaine" dans la barre de navigation, entrez votre nom de domaine personnalisé (celui que vous avez acheté) dans l'espace prévu et cliquez sur "Ajouter".

Lorsque vous cliquez sur le bouton "Ajouter", une invite devrait apparaître – ne changez rien, utilisez l'option recommandée et cliquez sur le bouton "Ajouter".

Pour l'étape suivante, cliquez sur l'option "Serveurs de noms", puis cliquez sur "Activer le DNS Vercel".

Enfin, copiez le DNS et rendez-vous sur le site où vous avez acheté votre domaine.

Voici des images détaillées qui montrent les étapes ci-dessus.

![Configuration du domaine personnalisé sur Vercel](https://cdn.hashnode.com/res/hashnode/image/upload/v1729808085843/7061315b-ca1e-4201-bd00-6d3b02bfa456.gif align="center")

À ce stade, tout ce que vous avez à faire est de lier votre domaine personnalisé avec Vercel, en utilisant le DNS que vous venez de copier depuis Vercel.

Voici comment vous pouvez faire cela (j'utiliserai le processus Namecheap pour l'expliquer) :

Rendez-vous sur le site où vous avez acheté votre domaine et connectez-vous à votre tableau de bord.

Allez dans l'option de liste des domaines et cliquez dessus. Cela devrait afficher une liste des domaines que vous avez achetés avec ce compte.

Ensuite, allez dans le nom de domaine que vous avez utilisé pour votre projet Vercel et cliquez sur l'option "gérer". Cela devrait ouvrir une page où les détails du domaine sont affichés.

Trouvez où vous avez "serveurs de noms" et choisissez l'option "DNS personnalisé". Enfin, collez chacun des DNS que vous avez copiés depuis Vercel dans les espaces prévus et cliquez sur enregistrer.

Après cela, vous devriez recevoir une invite indiquant que le domaine personnalisé sera actif dans les 48 prochaines heures. Dans la plupart des cas, cela ne prend pas plus d'une journée pour être actif.

Voici une image détaillée qui montre les étapes ci-dessus.

![Configuration du domaine personnalisé sur Namecheap](https://cdn.hashnode.com/res/hashnode/image/upload/v1729808142674/7d533d7d-0ea9-4cf8-bd19-183283ffa150.gif align="center")

## **Conclusion**

Dans cet article, vous avez appris à connaître la plateforme Vercel, ce qu'est un nom de domaine et son importance.

Vous avez également appris comment créer votre compte Vercel, déployer votre projet et ajouter un domaine personnalisé.

Si vous avez lu jusqu'à ce point, je veux vous dire un grand bravo, et j'espère que vous avez tiré profit de cet article.