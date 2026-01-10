---
title: Comment déployer un blog Next.js sur Sevalla
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2025-07-09T15:43:22.921Z'
originalURL: https://freecodecamp.org/news/how-to-deploy-a-nextjs-blog-on-sevalla
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1752075758399/7d8a494b-a5f0-4fb7-841b-8758d1cbc94d.png
tags:
- name: Next.js
  slug: nextjs
- name: Blogging
  slug: blogging
- name: Web Development
  slug: web-development
seo_title: Comment déployer un blog Next.js sur Sevalla
seo_desc: 'In this tutorial, I’ll teach you how to use Next.js and Sevalla to build
  and deploy your own Next.js blog.

  But first, let me answer your likely question: “Why host a blog yourself when there
  are hundreds of blogging platforms available? “

  One answer:...'
---

Dans ce tutoriel, je vais vous apprendre à utiliser Next.js et Sevalla pour construire et déployer votre propre blog Next.js.

Mais d'abord, laissez-moi répondre à votre question probable : « Pourquoi héberger un blog soi-même alors qu'il existe des centaines de plateformes de blogging disponibles ? »

Une réponse : [Next.js](https://nextjs.org/).

## Table des matières

* [Qu'est-ce que Next.js ?](#heading-qu-est-ce-que-nextjs)
    
* [Qu'est-ce que Sevalla ?](#heading-qu-est-ce-que-sevalla)
    
* [Construction et déploiement d'un blog Next.js](#heading-construction-et-deploiement-d-un-blog-nextjs)
    
    * [Construction du blog](#heading-construction-du-blog)
        
    * [Déploiement du blog](#heading-deploiement-du-blog)
        
    * [Ajout d'un domaine personnalisé](#heading-ajout-d-un-domaine-personnalise)
        
* [Conclusion](#heading-conclusion)
    

## **Qu'est-ce que Next.js ?**

![Framework Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871450742/adc4f876-dbad-41a3-b310-6c8f3e470c20.webp align="center")

Next.js est un framework de développement web construit sur React. Alors que React est une bibliothèque pour construire des interfaces utilisateur, Next.js ajoute des fonctionnalités supplémentaires pour faciliter et accélérer la construction de sites web et d'applications web.

Next.js vous donne un contrôle total. Vous possédez votre contenu, votre design et votre stratégie SEO. Contrairement à Medium ou Substack, vous n'êtes pas limité par les règles ou le branding de la plateforme. Vous pouvez optimiser chaque partie de votre blog, de la vitesse de chargement à son apparence dans les résultats de recherche Google.

Next.js n'est pas seulement un outil pour construire un blog. C'est une plateforme pour construire toute votre marque. C'est pourquoi les développeurs et les [indie hackers](https://www.indiehackers.com/post/why-next-js-is-perfect-for-saas-development-27f98e471b) l'adorent.

## **Qu'est-ce que Sevalla ?**

[Sevalla](https://sevalla.com/) est un fournisseur de Plateforme-en-tant-que-Service que j'ai récemment découvert et apprécié. Développé par l'équipe derrière [Kinsta](https://kinsta.com/), la plateforme d'hébergement WordPress populaire, Sevalla combine des fonctionnalités puissantes avec une expérience développeur fluide. Ils offrent l'hébergement d'applications, de bases de données, de stockage d'objets et de sites statiques pour vos projets.

Contrairement à des plateformes comme Heroku, qui fournissent presque toutes les fonctionnalités via des intégrations supplémentaires, Sevalla vous donne exactement ce dont vous avez besoin pour construire et déployer une application pour vos utilisateurs.

![Panneau d'administration Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871511816/7de2c52f-da06-4891-a62d-dad4eb4ca57a.webp align="center")

Imaginez si quelqu'un prenait uniquement les fonctionnalités essentielles des plateformes cloud comme AWS ou Azure et les mettait dans un seul tableau de bord facile à utiliser. C'est exactement ce que le panneau d'administration Sevalla offre. Une interface propre et simple avec tout ce dont vous avez besoin, et rien de superflu.

En résumé, Sevalla gère tout le travail lourd de déploiement et de mise à l'échelle de votre application, afin que vous puissiez vous concentrer entièrement sur sa construction.

## **Construction et déploiement d'un blog Next.js**

Maintenant, construisons et déployons notre blog Next.js. Nous n'avons pas besoin de le construire à partir de zéro – il existe de nombreux modèles disponibles pour nous, [comme celui-ci](https://github.com/sevalla-templates/nextjs-blog).

Nous allons faire trois choses.

* Cloner le dépôt et configurer le blog sur notre machine locale.
    
* Déployer le site sur Sevalla
    
* Ajouter un domaine personnalisé.
    

### Construction du blog

Tout d'abord, forkez le dépôt du blog Next.js.

![Fork Repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871568856/84bb32da-25b9-4a0b-8170-658914a643fe.webp align="center")

Une fois que vous l'avez forké, clonez-le sur votre machine locale.

![Clone repository](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871607179/716dfc07-d0c8-4ab5-9c45-8ee72fca3f09.webp align="center")

```plaintext
git clone <repository url>
```

Une fois que vous avez cloné le dépôt, allez dans le répertoire et exécutez `npm install`. Assurez-vous d'avoir les dernières versions de [Node.js](https://nodejs.org/en) et Next.js installées sur votre machine.

Maintenant, exécutons le blog sur notre machine. La commande est `npm run dev`. Une fois le serveur en cours d'exécution, allez sur `localhost:3000` pour voir le site.

![Demo Next.js blog](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871654364/b738b6f7-b272-4b75-bf5b-b2af40ccd035.webp align="center")

Vous devriez voir la page ci-dessus. Maintenant, ajoutons notre propre article de blog. Allez dans le répertoire `content/blog`. Chaque page dans le répertoire de contenu est votre article de blog, et vous pouvez utiliser [Markdown](https://www.markdownguide.org/basic-syntax/) pour le styliser. Enregistrez le fichier avec l'extension `.mdx`

Ajoutez le texte suivant (la première partie est les métadonnées pour que le blog comprenne le titre et la date de publication) :

```plaintext
---
title: "Mon Nouvel Article"
date: 2025-07-07
---

Bienvenue dans mon premier article de blog utilisant Next.js et MDX !
```

Rechargez la page d'accueil, et vous devriez maintenant voir deux articles – l'article par défaut et votre nouvel article.

![Nouvel article dans le blog Next.js](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871689247/e3ec1407-33d7-4c9c-9032-3e2e36b189a7.webp align="center")

Ainsi, chaque fois que vous voulez publier un nouvel article, vous créez une nouvelle page en utilisant Markdown. C'est aussi simple que cela.

Commitez ce nouveau fichier et poussez-le vers votre dépôt.

```plaintext
git add .
git commit -m "nouvel article"
git push origin main
```

### Déploiement du blog

Maintenant, créez un compte sur Sevalla (utilisez la connexion GitHub pour ne pas avoir à vous réauthentifier).

Une fois connecté à Sevalla, vous verrez l'option Site statique. Cliquez dessus pour créer un site statique.

Comme pour d'autres fournisseurs d'hébergement, tous les produits Sevalla ne sont pas gratuits, mais il offre des crédits gratuits généreux. À moins que vous n'ayez un nombre raisonnable d'utilisateurs qui accèdent à votre blog, vous n'aurez aucun coût pour les blogs/petits projets. Mais en ce qui concerne les sites statiques, vous pouvez héberger jusqu'à 100 sites complètement gratuitement.

![Tableau de bord Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871726773/aaee5778-f9c8-4454-9349-154aa4d291d3.webp align="center")

Sélectionnez le dépôt dans la liste. Cochez l'option « Déploiement automatique à la validation ». Ainsi, chaque fois que vous poussez du code, Sevalla déployera automatiquement votre nouvel article sur le serveur.

![Créer un site statique](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871773521/44aafcba-a5cf-4017-b28e-f3271414f8c8.webp align="center")

Dans la page « paramètres de construction », gardez les valeurs par défaut. Cliquez sur « Créer un site ». En quelques minutes, l'application sera extraite de GitHub, déployée sur un serveur, et vous devriez voir le bouton `visiter le site`.

![Succès du déploiement](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871809727/1658eca6-9f0e-4a7d-94c8-4519491940be.webp align="center")

Si vous visitez le site, vous devriez voir la page ci-dessous :

![Blog en direct](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871841987/f9e9784a-bcac-4265-b060-2894fcc7fb16.webp align="center")

Hourra ! Votre blog est en ligne. Vous pouvez également voir les journaux de construction détaillés sous l'onglet « déploiements » et vérifier s'il y a des problèmes de déploiement de votre application.

![Journaux de déploiement Sevalla](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871895728/00d0c956-991b-42e1-bafe-1bde592009f2.webp align="center")

### Ajout d'un domaine personnalisé

Bien. Pour la dernière étape, ajoutons un domaine personnalisé à notre blog.

Allez dans l'onglet « domaines », et cliquez sur « ajouter un domaine » sous les domaines personnalisés. J'utiliserai un sous-domaine `next` de mon domaine privé [`manishshivanandhan.com`](http://manishshivanandhan.com), mais les instructions sont les mêmes pour les domaines racines également.

![Ajouter un domaine personnalisé](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871942423/faba7435-4f1e-4565-8f41-ac9f41257532.webp align="center")

Une fois que vous cliquez sur « ajouter un domaine », Sevalla vous donnera les instructions pour ajouter les enregistrements TXT pour la vérification et les enregistrements CNAME/A pour pointer le nouveau site vers votre domaine.

Une fois ces étapes effectuées chez votre fournisseur de domaine, vérifiez à nouveau après quelques minutes.

![Domaine personnalisé vérifié](https://cdn.hashnode.com/res/hashnode/image/upload/v1751871974507/fbf19bd2-b862-4bab-bd0b-ff2d83e133eb.webp align="center")

Hourra ! Vous avez créé votre propre blog Next.js. Voici le site exemple que j'ai construit pour ce projet – [http://next.manishshivanandhan.com](http://next.manishshivanandhan.com/)

## **Conclusion**

Et voilà ! Votre propre blog Next.js est maintenant en ligne sur Sevalla.

En peu de temps, vous êtes passé du clonage d'un modèle à la publication de votre premier article et à son déploiement dans le monde avec un domaine personnalisé. Avec Next.js, vous avez un contrôle total sur votre contenu et votre marque, et avec Sevalla, le déploiement devient sans effort et fluide.

Rappelez-vous, chaque fois que vous voulez publier un nouvel article, il suffit de créer un simple fichier markdown et de pousser votre code. Sevalla gère le reste, afin que vous puissiez vous concentrer sur ce qui compte vraiment : écrire un excellent contenu et construire votre marque personnelle.

J'espère que vous avez apprécié cet article ! Je serai de retour bientôt avec plus de tutoriels sur la construction avec Next.js. N'hésitez pas à [me connecter sur LinkedIn](https://www.linkedin.com/in/manishmshiva/) pour rester en contact.