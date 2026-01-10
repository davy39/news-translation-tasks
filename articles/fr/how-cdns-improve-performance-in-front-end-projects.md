---
title: Comment utiliser les CDN pour améliorer les performances dans vos projets Front-end
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-10-14T19:36:06.558Z'
originalURL: https://freecodecamp.org/news/how-cdns-improve-performance-in-front-end-projects
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1728820334493/8ef2738f-c2ac-42d3-be3f-5a6a3bddbdbd.png
tags:
- name: Frontend Development
  slug: frontend-development
- name: CDN
  slug: cdn
- name: computer networking
  slug: computer-networking
seo_title: Comment utiliser les CDN pour améliorer les performances dans vos projets
  Front-end
seo_desc: In web development, styling plays a crucial role in the visual presentation
  of web applications. According to a study by Adobe, 59% of users would choose a
  beautifully designed website over a “simple and plain” design. So designs that are
  crafted in ...
---

Dans le développement web, le style joue un rôle crucial dans la présentation visuelle des applications web. Selon une étude d'Adobe, 59 % des utilisateurs choisiraient un site web magnifiquement conçu plutôt qu'un design "simple et basique". Ainsi, les designs conçus de manière visuellement attrayante tendent à attirer les utilisateurs pour consommer du contenu sur un site web.

Ces derniers temps, il y a eu une augmentation constante des outils de style que vous pouvez utiliser pour améliorer l'attrait visuel de vos sites web. Ces outils incluent les frameworks CSS, les bibliothèques d'animation, les bibliothèques d'icônes et les bibliothèques de typographie. Ces outils offrent une flexibilité de personnalisation, une réactivité et une cohérence.

Une chose géniale à propos de ces outils de style est qu'ils regroupent des effets stylistiques dans un fichier auquel vous pouvez accéder via un Content Delivery Network (CDN).

Dans cet article, nous allons examiner en détail les CDN, leur fonctionnement, leurs différentes méthodes d'hébergement, les différences entre elles, leurs avantages et inconvénients, et les meilleurs cas d'utilisation des méthodes pour votre projet.

Plongeons directement dans le sujet !

### Ce que nous allons couvrir :

1. [Qu'est-ce qu'un CDN ?](#heading-quest-ce-quun-cdn)
   
   * [Comment fonctionne un CDN ?](#heading-comment-fonctionne-un-cdn)
       
   * [Analogie du monde réel pour expliquer les CDN](#heading-analogie-du-monde-reel-pour-expliquer-les-cdn)
       
2. [Pourquoi les CDN sont-ils importants ?](#heading-pourquoi-les-cdn-sont-ils-importants)
   
3. [Différentes façons d'utiliser un CDN](#heading-differentes-facons-dutiliser-un-cdn)
   
   * [CDN hébergé à distance](#heading-cdn-heberge-a-distance)
       
   * [CDN hébergé localement](#heading-cdn-heberge-localement)
       
   * [CDN hébergé hybride](#heading-cdn-heberge-hybride)
       
4. [Conclusion](#heading-conclusion)
   

## **Qu'est-ce qu'un CDN ?**

Un CDN, ou Content Delivery Network, est un système de serveurs distribués qui livre du contenu web (comme des images, des feuilles de style, des scripts et d'autres ressources) aux utilisateurs, de manière fiable et efficace.

### **Comment fonctionne un CDN ?**

La fonction principale d'un CDN est de mettre en cache et de servir à la fois du contenu web statique et dynamique aux utilisateurs. Il y parvient en utilisant les éléments suivants :

* **Serveur d'origine** : Il s'agit du serveur principal où tout le contenu est initialement hébergé.
   
* **Serveurs de périphérie** : Il s'agit de serveurs distribués dans différentes localisations géographiques pour servir le contenu web aux utilisateurs les plus proches d'eux.
   
* **Mise en cache** : Il s'agit d'une manière de stocker le contenu sur les serveurs de périphérie pour réduire les demandes répétées au serveur d'origine.
   
* **Routage DNS** : Il s'agit du mécanisme qui redirige les utilisateurs vers les serveurs de périphérie les plus proches en fonction de leur localisation.
   

![Diagramme montrant le serveur d'origine communiquant avec différents serveurs de périphérie](https://cdn.hashnode.com/res/hashnode/image/upload/v1728819505243/6389ac39-e1d2-4348-9f97-8ee370eecd7f.png align="center")

Voici ce qui se passe lorsqu'un utilisateur clique sur un lien CDN :

* Si l'utilisateur essaie d'accéder à la ressource pour la première fois, la demande atteint le serveur d'origine.
   
* Le serveur d'origine envoie la ressource à l'utilisateur en tant que réponse et envoie également une copie au serveur de périphérie situé géographiquement le plus proche de l'utilisateur.
   
* Le serveur de périphérie met en cache la copie.
   
* Lorsque l'utilisateur souhaite accéder à nouveau aux ressources, le serveur de périphérie (et non le serveur d'origine) envoie la copie mise en cache.
   

### **Analogie du monde réel pour expliquer les CDN**

Pour expliquer davantage le fonctionnement du CDN, je vais donner une analogie pour le rendre plus clair. Imaginez avoir un compte dans une banque dont le siège est à New York (serveur d'origine).

Vous ne vous attendez pas à ce que les clients qui vivent loin de New York se précipitent au siège social chaque fois qu'ils rencontrent des problèmes. Au lieu de cela, la banque fournit des succursales (serveurs de périphérie) dans différentes localisations pour répondre aux besoins de leurs clients. Les clients peuvent facilement se rendre dans n'importe quelle succursale la plus proche d'eux et régler leurs problèmes ou transactions.

Les succursales disposent de toutes les informations de compte et des journaux de transactions des clients (données mises en cache). Chaque succursale de cette banque fournit les mêmes services et peut satisfaire leurs clients, quelle que soit leur distance par rapport au siège social.

La distribution des succursales dans différentes localisations aide à réduire le trafic qui aurait causé des retards si la banque n'avait que le siège social comme seule option. En contactant le service client de la banque pour un problème, vous seriez probablement redirigé vers la succursale de la banque la plus proche de vous (routage DNS) !

## **Pourquoi les CDN sont-ils importants ?**

Il y a de nombreuses raisons pour lesquelles de nombreux sites web utilisent des CDN de nos jours. Certains des principaux avantages sont :

1. **Amélioration des performances du site web** : Les CDN peuvent compresser des fichiers et optimiser des images automatiquement, ce qui aide à accélérer le temps de chargement.
   
2. **Stockage efficace des ressources** : Avec les CDN, les ressources de style sont stockées et gérées correctement. Les ressources sont également stockées dans des fichiers correspondant à leurs types de contenu.
   
3. **Meilleur référencement (SEO)** : L'utilisation de CDN accélère directement le temps de chargement, ce qui impacte à son tour les classements dans les moteurs de recherche. Google considère la vitesse du site comme une métrique clé qui permet aux pages web de s'afficher plus haut dans les moteurs de recherche.
   
4. **Meilleure expérience utilisateur** : Les utilisateurs préfèrent les sites web plus rapides et plus réactifs aux sites lents et non réactifs. Avec une meilleure expérience utilisateur, un site web est sûr de recevoir plus d'engagement et des taux de rebond plus faibles.
   

## **Différentes façons d'utiliser un CDN**

Il existe trois façons d'accéder aux ressources CDN dans votre projet :

* Hébergement à distance
   
* Hébergement local
   
* Hébergement hybride
   

### **CDN hébergé à distance**

Les liens CDN à distance permettent aux développeurs d'accéder aux ressources de style à partir d'un serveur tiers en liant simplement le CDN dans leurs fichiers HTML via la balise `link` ou `script`.

Bootstrap, par exemple, dispose de deux liens CDN principaux – un pour la feuille de style CSS et un autre pour JavaScript (gère les interactions dynamiques comme les menus déroulants, les pop-overs, etc.).

Pour utiliser une feuille de style Bootstrap dans votre projet, vous devez ajouter cette seule ligne - `https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css`

Et pour le JavaScript : `https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js`

#### **Comment trouver les liens CDN à distance**

La meilleure façon d'identifier les liens CDN à distance de votre outil de style souhaité est de visiter leur site de documentation officiel et de rechercher les liens directs.

#### **Avantages d'un CDN à distance :**

1. **Facile à utiliser** : Vous n'avez pas besoin de télécharger, gérer ou uploader des fichiers avec des liens CDN. Tout ce que vous avez à faire est d'insérer une seule ligne de code dans votre fichier HTML et vous êtes prêt à partir.
   
2. **Mise en cache globale** : chaque fois que vous visitez un site web qui utilise des liens CDN, il télécharge les ressources lors du chargement de la page, puis les enregistre dans le cache de votre navigateur. Lors des visites ultérieures sur le même site web ou d'autres sites qui utilisent le même CDN, il récupère les ressources depuis le cache et les affiche plus rapidement. C'est l'un des plus grands avantages de l'utilisation des liens CDN, car cela améliore le temps de chargement du site web.
   
3. **Livraison globale optimisée** : Les CDN sont conçus pour livrer du contenu aux utilisateurs du monde entier en servant des fichiers depuis les serveurs de périphérie les plus proches des utilisateurs. Cela aide à réduire le temps nécessaire pour transférer des données à travers un réseau, également connu sous le nom de latence, et améliore les performances pour les utilisateurs internationaux.
   
4. **Réduction de la charge du serveur** : En raison de la récupération des données par le CDN depuis une source externe, la charge sur votre serveur est réduite, ce qui est utile pour les sites web à fort trafic.
   
5. **Mises à jour en temps réel** : Les entreprises qui possèdent des liens CDN effectuent des corrections de bugs périodiques, des mises à jour de sécurité et des mises à jour de fonctionnalités, ce qui peut être bénéfique pour votre projet. Ces mises à jour sont reflétées dès qu'elles sont publiées.
   

#### **Inconvénients d'un CDN à distance :**

1. **Limitations de personnalisation** : Les composants de style dans les CDN à distance sont standard et non modifiés. Pour les modifier, vous devriez remplacer les styles spécifiques dans votre fichier local, ce qui peut introduire des complexités.
   
2. **Aucun contrôle sur les mises à jour** : Lorsque des mises à jour automatiques sont effectuées, elles peuvent causer des problèmes dans vos applications web. Si les changements introduits incluent des modifications drastiques, cela peut affecter la mise en page ou le comportement de votre site web de manière significative.
   
3. **Dépendance à la disponibilité des tiers** : Si le service CDN rencontre des problèmes comme des temps d'arrêt ou des lenteurs, cela peut entraîner des styles cassés, affectant ainsi négativement les performances de votre site.
   
4. **Problèmes de confidentialité et de sécurité** : Les liens référençant une source externe peuvent poser de sérieux problèmes de sécurité, car ils peuvent être utilisés pour suivre les utilisateurs et obtenir des informations vitales. Il est important d'inclure uniquement des sources de liens CDN de confiance dans votre projet web pour éviter les violations.
   

### **CDN hébergé localement**

Il s'agit de ressources CDN téléchargées depuis un CDN à distance et enregistrées dans votre dossier de projet ou hébergées sur un serveur local. Cette approche vous permet d'avoir un contrôle total sur les ressources.

#### **Comment héberger des ressources CDN localement :**

L'hébergement local est simple et facile. Tout ce que vous avez à faire est :

* Accéder à la ressource en naviguant vers l'URL du lien CDN (par exemple, [`https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css`](https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css)).
   
* Copier le code trouvé dans l'URL.
   
* Créer un fichier avec l'extension de fichier appropriée (.css, .js) dans votre dossier de projet.
   
* Coller et enregistrer.
   
* Référencer le fichier dans votre document HTML.
   

Si vous suivez ces étapes, vous devriez être en mesure de localiser la ressource CDN et d'accéder à son style localement.

#### **Avantages d'un CDN hébergé localement :**

1. **Contrôle total sur les fichiers** : Avec les ressources résidant dans votre dossier de projet/serveur, vous avez un contrôle total sur vos fichiers, car il n'y aura pas de pannes, de changements ou de mises à jour inattendus qui pourraient casser votre site.
   
2. **Disponibilité hors ligne** : L'hébergement local garantit que vos ressources de style sont toujours disponibles, surtout pour les utilisateurs avec peu ou pas de réseau. Cela est parfait pour construire des Applications Web Progressives (PWA).
   
3. **Personnalisation** : Il n'y aura pas besoin de remplacements, car votre style peut être modifié depuis vos fichiers de projet.
   
4. **Sécurité** : En localisant les ressources CDN, vous réduisez le risque d'attaques potentielles de tiers sur votre projet au minimum.
   

#### **Inconvénients d'un CDN hébergé localement :**

1. **Pas de mise en cache globale** : Il n'y a pas d'avantage de mise en cache globale lorsque les ressources sont hébergées localement. Cela entraînera un temps de chargement plus lent pour les visiteurs pour la première fois.
   
2. **Charge accrue du serveur** : Avec les fichiers résidant localement, la charge sur le serveur augmente, surtout lorsque le trafic augmente. Cette approche met une charge sur le serveur et sa capacité doit être considérée.
   
3. **Mises à jour manuelles** : Bien que l'hébergement local vous donne un contrôle sur les mises à jour, vous devrez suivre et appliquer manuellement les mises à jour à vos feuilles de style lorsque cela est nécessaire. De plus, manquer des mises à jour de sécurité pourrait rendre votre site vulnérable.
   
4. **Impact sur les performances régionales** : Si votre serveur est situé dans une région spécifique, les utilisateurs de lieux éloignés peuvent rencontrer des temps de chargement plus lents car le contenu doit parcourir de plus grandes distances.
   

### **CDN hébergé hybride**

Cette approche implique la combinaison de l'utilisation du lien à distance et de l'hébergement local des ressources CDN. Une approche hybride – qui implique l'utilisation de CDN à distance pour les bibliothèques principales et l'hébergement local pour les feuilles de style personnalisées – peut trouver le juste équilibre entre performance et contrôle.

### **Meilleure approche à utiliser**

La décision entre l'hébergement à distance et local de vos ressources de style CDN dépend de facteurs tels que les besoins de performance du projet, la base d'utilisateurs et la sécurité. Votre choix devrait dépendre de l'adéquation de l'approche à votre projet et devrait améliorer les niveaux de performance.

#### **Meilleurs cas d'utilisation pour un CDN à distance :**

1. **Base d'utilisateurs mondiale** : Si votre site web doit être accessible par un large public réparti dans le monde, l'utilisation de l'option à distance fonctionnerait mieux en raison de ses avantages en termes de performance et de mise en cache.
   
2. **Intégration rapide** : Dans une situation où vous souhaitez développer et déployer un projet dans le plus court laps de temps, l'utilisation du lien CDN à distance est rapide et facile.
   
3. **Site web à faible trafic** : Les petits projets tels que les sites de portfolio et les blogs sont mieux servis en utilisant un lien CDN à distance afin de ne pas mettre à rude épreuve le serveur. Cela conduit également à une implémentation plus facile.
   

#### **Meilleurs cas d'utilisation pour un CDN hébergé localement :**

1. **Besoins élevés en sécurité** : Pour les applications nécessitant une sécurité stricte en raison de la sensibilité de leurs opérations, l'hébergement des ressources CDN localement réduira les risques et vulnérabilités des tiers.
   
2. **Applications hors ligne** : Pour les applications web fonctionnant hors ligne, la localisation des ressources de style serait la meilleure option.
   
3. **Exigences de personnalisation** : Si vous devez créer vos versions de style sur mesure, les héberger localement est la meilleure option.
   

## **Conclusion**

Dans ce guide, vous avez appris ce qu'est un CDN, comment vous pouvez héberger votre CDN, ainsi que certains des avantages, inconvénients et meilleurs cas d'utilisation pour chaque approche.

Les CDN à distance offrent rapidité, commodité et réduction de la charge du serveur, tandis que l'hébergement local offre un meilleur contrôle, une meilleure sécurité et des options de personnalisation.

En fin de compte, la meilleure approche dépend de votre cas d'utilisation spécifique, de votre audience et de vos priorités.

Vous pouvez me contacter sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) ou [X](https://x.com/SmoothTee_DC) pour plus de publications et d'articles liés au frontend.

À la prochaine !