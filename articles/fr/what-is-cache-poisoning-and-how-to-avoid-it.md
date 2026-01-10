---
title: Qu'est-ce que l'empoisonnement de cache ? Comment les hackers manipulent les
  caches web et comment l'éviter
subtitle: ''
author: Manish Shivanandhan
co_authors: []
series: null
date: '2024-09-05T15:00:53.243Z'
originalURL: https://freecodecamp.org/news/what-is-cache-poisoning-and-how-to-avoid-it
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1725456042044/d3744ebe-ad28-42c4-99a2-25d6bd250aee.webp
tags:
- name: '#cybersecurity'
  slug: cybersecurity-1
seo_title: Qu'est-ce que l'empoisonnement de cache ? Comment les hackers manipulent
  les caches web et comment l'éviter
seo_desc: 'Web caches play an important role in speeding up our browsing experience.
  They save copies of web pages and other resources so that users can access them
  faster.

  But what happens when these caches become a tool for hackers?

  Let’s look at cache poison...'
---

Les caches web jouent un rôle important pour accélérer notre expérience de navigation. Ils enregistrent des copies de pages web et d'autres ressources afin que les utilisateurs puissent y accéder plus rapidement.

Mais que se passe-t-il lorsque ces caches deviennent un outil pour les hackers ?

Examinons l'empoisonnement de cache (cache poisoning), son fonctionnement et comment s'en protéger.

## Qu'est-ce qu'un cache web ?

La mise en cache consiste à stocker une copie d'un élément de contenu. Un cache web stocke temporairement des copies de pages web ou des parties de contenu web.

Lorsque vous visitez un site web, votre navigateur peut mettre en cache certains éléments, comme des images et des scripts. Ainsi, la prochaine fois que vous visiterez le même site, le navigateur pourra le charger plus rapidement.

Le cache accélère les sites web. Il réduit la quantité de données qui doivent être transférées sur le réseau. Cela rend la navigation plus efficace et offre une expérience plus fluide aux utilisateurs.

Un cache peut se trouver à plusieurs endroits. Ceux-ci incluent :

**Cache du navigateur** : Votre navigateur conserve une copie des pages web, images et autres contenus récemment visités.

**Cache CDN** : Les réseaux de diffusion de contenu (CDNs) stockent des copies de ressources web dans de multiples emplacements à travers le monde. Cela garantit que les utilisateurs accèdent à un serveur proche, réduisant ainsi les temps de chargement.

**Cache de Reverse Proxy** : Un serveur proxy inverse se situe entre les utilisateurs et le serveur web. Il met le contenu en cache pour réduire la charge du serveur et améliorer les temps de réponse.

La mise en cache web repose sur quelques principes de base.

**Expiration** : Le contenu mis en cache a une valeur de durée de vie (TTL - Time-To-Live). Après ce délai, le cache est vidé.

**Validation** : Le cache vérifie auprès du serveur si le contenu stocké est toujours valide ou s'il doit être actualisé.

**Invalidation** : Si le contenu d'un site web est mis à jour, il supprimera le cache et récupérera la dernière version auprès du serveur.

## Comment fonctionne l'empoisonnement de cache ?

L'empoisonnement de cache est une cyberattaque par laquelle un hacker manipule les données stockées dans un cache web. Le cache stocke une version malveillante ou altérée, et non la page réelle.

Lorsqu'un utilisateur demande ce contenu mis en cache, il reçoit à la place les données manipulées. Cette attaque peut entraîner l'exécution de scripts dangereux sur les navigateurs de l'utilisateur.

![DNS cache poisoning](https://cdn.hashnode.com/res/hashnode/image/upload/v1725563209590/ec36e4dd-94cf-47f5-9b9d-5c335fe26327.png align="center")

Dans une attaque d'empoisonnement de cache, un hacker exploite la manière dont les systèmes de mise en cache stockent le contenu. Voici une explication simplifiée du fonctionnement de cette attaque.

L'attaquant identifie d'abord quelles ressources d'un site web sont mises en cache. Il recherche des pages ou des ressources que le cache pourrait stocker en fonction de l'URL ou des en-têtes de requête.

L'attaquant conçoit ensuite une requête incluant un contenu nuisible. Cette requête ressemblera à une requête légitime pour que le cache stocke la réponse.

Le serveur traite la requête et renvoie une réponse qui est mise en cache. Si le serveur de cache ne vérifie pas la requête, il stockera le contenu malveillant.

Désormais, lorsqu'un utilisateur demande la ressource mise en cache, le cache sert la version malveillante au lieu de la version légitime.

### Techniques courantes utilisées dans l'empoisonnement de cache

L'empoisonnement de cache exploite différentes vulnérabilités des mécanismes de mise en cache web. Certaines des techniques les plus courantes incluent :

**Attaques par en-tête Host**

L'en-tête « Host » spécifie le domaine auquel une requête est destinée. Les attaquants peuvent modifier cet en-tête. Ils peuvent tromper le serveur pour qu'il mette en cache une réponse malveillante. Par exemple :

Requête normale

```plaintext
GET /resource HTTP/1.1
Host: www.example.com
```

Requête malveillante

```plaintext
GET /resource HTTP/1.1
Host: attacker.com
```

Si le cache stocke la réponse en fonction de l'hôte manipulé, tous les utilisateurs de « www.example.com » pourraient recevoir du contenu malveillant.

**Pollution de paramètres HTTP (HTTP Parameter Pollution)**

Les attaquants peuvent injecter des paramètres inattendus dans les URLs. Cela modifie le comportement du serveur et empoisonne le cache. Par exemple :

**URL normale** : [`https://www.example.com/page?id=123`](https://www.example.com/page?id=123%60)

**URL malveillante** : [`https://www.example.com/page?id=123&malicious_flag=101`](https://www.example.com/page?id=123&evil=1%60)

Si le serveur ne nettoie pas ces paramètres, il peut mettre en cache un contenu différent. Le prochain utilisateur qui visitera l'URL normale pourrait recevoir le contenu empoisonné.

**Manipulation de l'en-tête Vary**

L'en-tête Vary est un en-tête de réponse HTTP. Il indique aux caches comment stocker différentes versions d'une ressource web en fonction de certains en-têtes de requête.

Par exemple, si un serveur envoie un en-tête **« Vary: User-Agent »**, cela signifie que la réponse peut varier en fonction de l'agent utilisateur du client. Ainsi, les caches stockeront des versions distinctes de la ressource pour différents agents utilisateurs. Par exemple, une pour les navigateurs de bureau et une autre pour les navigateurs mobiles.

Si l'en-tête « Vary » n'est pas correctement vérifié, les attaquants peuvent manipuler les en-têtes de requête pour empoisonner le cache.

Par exemple, un attaquant peut créer une requête avec un en-tête « User-Agent » manipulé. Cela peut entraîner la mise en cache d'un contenu malveillant pour l'utilisateur suivant.

## Comment se protéger contre l'empoisonnement de cache

Maintenant que nous comprenons comment fonctionne l'empoisonnement de cache, voyons comment s'en protéger :

### **Validation appropriée des entrées**

Nettoyez et vérifiez toujours les entrées des utilisateurs. En particulier lorsqu'il s'agit des en-têtes de requête et des paramètres d'URL. Cela empêche les attaquants d'injecter du contenu nuisible dans les requêtes mises en cache.

### Utiliser des en-têtes de mise en cache sécurisés

Configurez correctement les en-têtes de cache comme « Cache-Control » et « Expires » pour éviter de mettre en cache des données sensibles. Utilisez des en-têtes tels que « no-cache », « no-store » et « must-revalidate » pour le contenu dynamique ou sensible.

### Contrôler les paramètres de clé de cache (Cache Key)

Définissez correctement les clés de cache pour éviter de mettre en cache des réponses avec des paramètres spécifiques à l'utilisateur. N'utilisez pas d'en-têtes de requête ou de paramètres de requête que les attaquants peuvent facilement manipuler.

### Implémenter HTTPS

L'utilisation de HTTPS aide à empêcher les attaquants d'intercepter et de modifier les requêtes et les réponses. HTTPS réduit également le risque d'attaques par empoisonnement de cache, car il garantit l'intégrité des données.

## Conclusion

L'empoisonnement de cache représente un risque important pour les applications web et les utilisateurs. Les hackers peuvent manipuler le contenu mis en cache pour diffuser des données malveillantes ou voler des informations sensibles.

Vous pouvez protéger vos applications web contre l'empoisonnement de cache en apprenant son fonctionnement et en prenant les précautions appropriées. Avec la bonne approche, vous pouvez garantir une expérience de navigation plus sûre pour vos utilisateurs.

**Consultez la newsletter** [***Stealth Security***](https://www.stealthsecurity.sh/) **pour plus d'articles sur la cybersécurité offensive et défensive.**