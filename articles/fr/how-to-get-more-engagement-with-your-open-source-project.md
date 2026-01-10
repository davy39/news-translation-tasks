---
title: Comment nous avons obtenu 4,5K+ étoiles GitHub sur notre projet open source
  en 6 mois
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2022-01-26T14:54:43.000Z'
originalURL: https://freecodecamp.org/news/how-to-get-more-engagement-with-your-open-source-project
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/t3.png
tags:
- name: Collaboration
  slug: collaboration
- name: community
  slug: community
- name: GitHub
  slug: github
- name: open source
  slug: open-source
seo_title: Comment nous avons obtenu 4,5K+ étoiles GitHub sur notre projet open source
  en 6 mois
seo_desc: "By navaneeth pk\nWe launched our open source project in June 2021, and\
  \ since then we've gotten more than 4500 stars for our repository. \nHere are the\
  \ strategies that worked for us. This is not an article about how to just get more\
  \ stars for your repos..."
---

Par navaneeth pk

Nous avons lancé [notre projet open source](https://github.com/ToolJet/ToolJet) en juin 2021, et depuis, nous avons obtenu **plus de 4500 étoiles** pour notre dépôt. 

Voici les stratégies qui ont fonctionné pour nous. Cet article ne traite pas uniquement de la manière d'obtenir plus d'étoiles pour votre dépôt. Il explique plutôt comment présenter votre projet de manière à ce qu'il soit utile pour la communauté open source. 

Certains de ces points nous ont également aidés à obtenir des contributions de plus de développeurs. Nous avons maintenant des contributions de plus de 100 développeurs. 

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-79.png)

Fait amusant : le graphique ci-dessus a été généré à l'aide d'une application construite avec notre outil. Vous pouvez [l'essayer ici](https://apps.tooljet.com/github-star-history) pour générer un graphique d'historique des étoiles pour votre projet.

D'accord, plongeons dans les stratégies que nous avons utilisées pour sensibiliser à notre projet.

## Écrire un bon Readme

Le README est la première chose qu'un visiteur de votre dépôt voit. Il doit être capable de transmettre ce que fait votre projet, comment installer le projet, comment déployer le projet (le cas échéant), comment contribuer et comment il fonctionne. 

Vous pouvez également utiliser des badges utiles pour les développeurs. Nous avons utilisé [https://shields.io/](https://shields.io/) pour ajouter des badges à notre Readme.   
  
Voici à quoi ressemble notre Readme :

![Image](https://blog.tooljet.com/content/images/2022/01/image-1.png)

  
Et voici quelques exemples de projets avec des fichiers README excellents :

1. [https://github.com/nestjs/nest](https://github.com/nestjs/nest) 
2. [https://github.com/typesense/typesense](https://github.com/typesense/typesense)
3. [https://github.com/airbytehq/airbyte](https://github.com/airbytehq/airbyte)
4. [https://github.com/strapi/strapi](https://github.com/strapi/strapi)

## Se concentrer sur la documentation

Nous recevons plus de trafic sur notre [portail de documentation](https://docs.tooljet.com/) que sur notre site web principal. Un projet bien documenté est toujours apprécié par la communauté. 

Des projets open source comme [Docusaurus](https://github.com/facebook/docusaurus/) rendent super facile la création de portails de documentation qui ont fière allure dès le départ. L'ajout de liens vers le dépôt depuis la documentation peut attirer plus de visiteurs vers votre dépôt.

### Que inclure dans la documentation

#### Comment installer/déployer le projet

Si le projet a un logiciel compilé comme produit final, assurez-vous d'ajouter des instructions d'installation. 

Si le projet est la base de code pour une bibliothèque telle qu'un package npm ou un gem Ruby, incluez des détails sur la manière d'importer et d'utiliser la bibliothèque. 

Si le projet doit être ou peut être déployé sur des plateformes comme Kubernetes, Docker, Heroku, et autres, incluez des guides séparés pour chacune des options. 

#### Guide de contribution

En plus du guide de contribution dans la base de code, ajoutez-en un à la documentation également. Il doit inclure des guides pour configurer un environnement local sur différentes plateformes comme Docker, Mac OS, Ubuntu, Windows, et ainsi de suite. 

#### Tutoriels et exemples de code

Si cela est applicable, cela peut être vraiment utile. Les guides sur l'utilisation du projet montreront aux autres développeurs comment ils peuvent réellement commencer. Cela peut être des exemples de code si le projet est une bibliothèque. 

#### Référence d'architecture

Cela sera utile pour les contributeurs si la documentation contient des détails sur les différents composants du projet. 

Par exemple, si le projet a des composants serveur et client, incluez un diagramme sur la manière dont tout fonctionne ensemble. Voici [un exemple](https://docs.tooljet.com/docs/intro) de la documentation de ToolJet. 

Voici quelques projets avec une excellente documentation :

1. [https://docs.nestjs.com/](https://docs.nestjs.com/)
2. [https://docs.n8n.io/](https://docs.n8n.io/)
3. [https://guides.rubyonrails.org/](https://guides.rubyonrails.org/)
4. [https://plotly.com/python/](https://plotly.com/python/)
5. [https://docs.mapbox.com/](https://docs.mapbox.com/)

## Diriger les visiteurs de votre site web vers GitHub 

![Image](https://blog.tooljet.com/content/images/2022/01/image-6.png)

De nombreux visiteurs ont consulté notre dépôt après avoir visité notre site web. Ajoutez des bannières, des badges et d'autres incitations à votre site web afin que les visiteurs consultent votre dépôt. 

Ajoutez un CTA à votre site web et à votre blog afin que les visiteurs consultent votre dépôt. Écrivez sur des sujets pertinents pour votre audience. Par exemple, si votre projet est utilisé pour journaliser les erreurs, il pourrait être judicieux d'écrire sur la manière de suivre les erreurs dans une application. 

Publier des articles sur des plateformes comme freeCodeCamp, dev.to, Hashnode et Hackernoon peut également vous aider à obtenir plus de visibilité pour vos articles de blog. Certaines de ces plateformes permettent le cross-posting tandis que d'autres sont plus adaptées au contenu exclusif. 

## Soyez actif dans les communautés de développeurs

Il existe de nombreuses communautés Discord/Slack, forums, communautés Reddit, etc., où les développeurs se retrouvent généralement. Soyez actif dans ces communautés sans que cela ne ressemble à de l'auto-promotion (ce qui peut vous faire bannir pour des raisons évidentes).

Vous pouvez ajouter de la valeur aux communautés en participant à des discussions pertinentes. Par exemple, si vous construisez une bibliothèque de graphiques et que quelqu'un pose une question sur la création de graphiques avec React, vous pouvez intervenir pour aider. 

N'oubliez pas, soyez gentil. N'essayez pas simplement de lier votre projet s'il n'ajoute aucune valeur à la discussion. Plus vous construisez des relations en aidant les gens, plus vous pourrez partager des informations sur votre projet de manière naturelle et utile.

## Dépôts tendance sur GitHub

![Image](https://blog.tooljet.com/content/images/2022/01/image-4.png)

Si vous faites partie de la [liste des dépôts GitHub tendance](https://github.com/trending?since=daily), cela peut donner beaucoup plus de visibilité à votre dépôt. 

Lorsque nous avons fait partie de la liste des tendances, nous avons eu plus de visiteurs sur notre dépôt et notre site web. 

Il existe également des listes de tendances pour des langues spécifiques. De nombreux bots Twitter et autres outils avertissent les développeurs chaque fois qu'il y a un nouveau dépôt qui a fait partie de la liste des tendances. 

### Comment figurer sur la liste des tendances de GitHub

Le principe général devrait être que les dépôts avec le plus d'activité (étoiles, visiteurs, problèmes, contributions, etc.) seront ajoutés à la liste des tendances.

GitHub n'a pas mentionné publiquement les critères de sélection des dépôts tendance, nous ne pouvons donc que supposer comment cela fonctionne. 

## Demander des commentaires aux communautés pertinentes

![Image](https://blog.tooljet.com/content/images/2022/01/image-5.png)

Des communautés telles que [ProductHunt](https://www.producthunt.com/posts/tooljet), [Hackernews](https://news.ycombinator.com/item?id=27421408), les communautés Reddit, et autres peuvent trouver votre projet utile. Cela peut attirer plus de visiteurs et de stargazers vers votre dépôt. 

Ciblez uniquement les communautés pertinentes. Si vous pensez que la majorité des membres ne trouveront pas votre projet intéressant, ce n'est pas une communauté pertinente. Le spam peut causer plus de tort que de bien. De plus, ce n'est tout simplement pas gentil.

## Développer une communauté autour de votre projet

Créez une communauté sur Discord ou Slack où vos utilisateurs et contributeurs peuvent se retrouver. 

Les communautés peuvent être utiles lorsque les membres sont bloqués avec quelque chose et s'ils veulent proposer quelque chose de nouveau. Si une communauté active existe, vos futurs posts et annonces pourraient avoir plus de portée. 

Nous avons créé la communauté sur Slack puisque la plupart des développeurs ont un compte Slack. N'utilisez pas de plateformes moins connues pour construire votre communauté, car cela nécessitera une étape supplémentaire pour la personne qui souhaite rejoindre la communauté.

## Ajouter une feuille de route publique

Une feuille de route publique aide vos utilisateurs et contributeurs à comprendre où votre projet se dirige. Elle donne un aperçu de la vision à court terme du projet.

Il existe de nombreux outils disponibles pour créer des feuilles de route publiques, mais dans la plupart des cas, les projets GitHub seront plus que suffisants pour créer une feuille de route publique simple mais efficace. 

Les feuilles de route publiques doivent inclure toutes les fonctionnalités majeures et les changements prévus pour être publiés dans les prochains mois. L'ajout de fonctionnalités mineures et de bugs dans le cadre de la feuille de route du produit peut entraîner beaucoup de bruit, évitez donc cela autant que possible. 

Si vous utilisez des projets GitHub, liez les problèmes ou discussions pertinents afin que la communauté puisse commenter ses suggestions. 

Nous en avons créé une en utilisant les projets GitHub que [vous pouvez consulter ici](https://github.com/ToolJet/ToolJet/projects/2).

## Soyez actif sur Twitter 

Être actif sur les posts liés à vos projets peut créer de la notoriété, augmenter le nombre d'abonnés sur Twitter et attirer plus de visiteurs vers votre dépôt. 

Participez aux discussions liées à votre projet. Par exemple, si votre projet est un framework de documentation, vous pouvez ajouter beaucoup de valeur aux fils de discussion qui comparent différents frameworks de documentation. 

Assurez-vous de lier votre dépôt sur le profil Twitter du projet. Ajoutez également un bouton de tweet à votre dépôt GitHub. 

Encore une fois, assurez-vous d'ajouter de la valeur aux discussions. Personne n'aime un spammer.

## Répondre aux commentaires 

Les communautés open source sont généralement très utiles et donnent beaucoup de commentaires. Répondez à tous ces commentaires, car la personne a pris son temps précieux pour vous aider à améliorer votre projet. 

Les commentaires positifs vous aident à rester motivé, tandis que les commentaires négatifs vous aident à repenser ce que vous avez fait jusqu'à présent. 

N'essayez pas d'éviter ou d'ignorer les commentaires négatifs. Soyez ouvert d'esprit et considérez soigneusement ce que la personne a partagé. Travaillez dessus si cela correspond à votre vision, sinon expliquez poliment.

## Ajouter des étiquettes pertinentes pour les contributeurs

L'ajout d'étiquettes telles que "good first issue" et "up for grabs" peut attirer plus de contributeurs vers votre dépôt. 

Il existe de nombreuses plateformes telles que [https://goodfirstissue.dev/](https://goodfirstissue.dev/) qui scannent les problèmes étiquetés avec des étiquettes pertinentes pour aider les contributeurs à découvrir de nouveaux dépôts et problèmes auxquels contribuer. 

Assurez-vous de répondre rapidement aux contributeurs. Les contributeurs peuvent être des développeurs expérimentés ainsi que des développeurs en début de carrière ou des étudiants. Essayez d'aider les premiers contributeurs afin qu'ils puissent s'intégrer facilement.

## Conclusion

Vous êtes arrivé sur cet article probablement parce que vous avez un projet open source intéressant. J'adorerais voir votre projet. Je suis disponible à navaneeth@tooljet.com et sur [Twitter](https://twitter.com/navaneeth_pk).

J'espère que cet article vous a été utile. Nous apprécierions vraiment que vous preniez un moment pour [découvrir notre projet, ToolJet](https://github.com/ToolJet/ToolJet), et nous donner tout commentaire que vous pourriez avoir.