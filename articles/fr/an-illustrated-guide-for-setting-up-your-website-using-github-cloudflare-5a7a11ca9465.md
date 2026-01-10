---
title: Un guide illustré pour configurer votre site web en utilisant Github et Cloudflare
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-04-25T18:20:21.000Z'
originalURL: https://freecodecamp.org/news/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465
coverImage: https://cdn-media-1.freecodecamp.org/images/1*TW_xtI15RW9vMZh4u2szIQ.png
tags:
- name: cloudflare
  slug: cloudflare
- name: GitHub
  slug: github
- name: General Programming
  slug: programming
- name: startup
  slug: startup
- name: Web Development
  slug: web-development
seo_title: Un guide illustré pour configurer votre site web en utilisant Github et
  Cloudflare
seo_desc: 'By Karan Thakkar

  You should read this if…


  You want to setup custom redirects or other server configuration for free

  You want to get your site on HTTPS but don’t know where to start

  You’re overwhelmed with the amount of choices out there (like Netlif...'
---

Par Karan Thakkar

Vous devriez lire ceci si…

1. Vous souhaitez configurer des redirections personnalisées ou d'autres configurations de serveur **gratuitement**
2. Vous souhaitez mettre votre site en HTTPS mais ne savez pas par où commencer
3. Vous êtes submergé par le nombre de choix disponibles (comme [Netlify](https://www.netlify.com), [Surge](https://surge.sh), [BitBalloon](https://www.bitballoon.com/), [Now](https://zeit.co/now))

### **Pourquoi Github ?**

1. Facile à configurer et à démarrer avec Github Pages
2. Déploiements instantanés lors de l'envoi de nouveau code

### **Pourquoi Cloudflare ?**

1. C'est gratuit
2. Il offre un support SSL (HTTPS) prêt à l'emploi. ([Voici pourquoi HTTPS est important](https://developers.google.com/web/fundamentals/security/encrypt-in-transit/why-https).)
3. Gestion DNS super simple
4. Possibilité de définir l'expiration du cache du navigateur pour les ressources
5. Minification automatique de vos ressources statiques
6. Règles de page personnalisées pour configurer des redirections, toujours HTTPS, etc.
7. [HTTP2](https://hpbn.co/http2/)/[SPDY](http://googlecode.blogspot.in/2012/01/making-web-speedier-and-safer-with-spdy.html) pour les navigateurs supportés
8. Permet de configurer [HSTS](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet) (HTTP Strict Transport Security)

### Avant de commencer, vous aurez besoin de quelques éléments :

1. Un [compte Github](https://github.com/join)
2. Un [compte Cloudflare](https://www.cloudflare.com/a/sign-up)
3. Accès à un domaine personnalisé. Vous pouvez l'acheter auprès de n'importe quel registraire de noms de domaine comme : [Namecheap](https://www.namecheap.com/), [GoDaddy](http://www.godaddy.com), [BigRock](https://www.bigrock.in), etc.

Si tout cela a piqué votre curiosité, alors commençons !

### **Étape 1** : Créer un dépôt Github avec votre code

![Image](https://cdn-media-1.freecodecamp.org/images/Pazu9SBLRgkH49CuRwj69THDH-6P0YwQcmGs)
_Sélectionnez l'option **Site de projet** pour commencer_

* Allez sur [https://pages.github.com](https://pages.github.com/)
* Sélectionnez l'option **Site de projet** pour trouver les instructions sur la création d'une page de base à partir de zéro ou avec un thème personnalisé

### Étape 2 : Configurer Github Pages pour le dépôt

![Image](https://cdn-media-1.freecodecamp.org/images/NUb2qLmGitHj03aUVC971xLzhpKLAXAXS8K4)
_Allez dans **Paramètres** pour votre dépôt_

![Image](https://cdn-media-1.freecodecamp.org/images/iDbE5EYxOtNXFGOtShTGVO251jLHWvD0UFQs)
_Choisissez de servir votre site web à partir de la branche **master**_

Allez dans **Paramètres** pour votre dépôt. Dans la section **Github Pages**, choisissez la branche **master** pour servir votre site web. Une fois que vous avez fait cela, vous pouvez aller sur [**https://_<votre_nom_d_utilisateur_github>.github.io/repo**](https://<votre_nom_d_utilisateur_github>.github.io/repository)**s**itory pour voir votre site web en action comme montré ci-dessous.

![Image](https://cdn-media-1.freecodecamp.org/images/ZFsmt9wTMIQKRm-mat0mzabszDO2DaaWHBtI)

### Étape 3 : Ajouter un domaine personnalisé

![Image](https://cdn-media-1.freecodecamp.org/images/zkaZLSVwWXTLlOaBbbvOY5GYCp71NbUyWKfL)
_Ajoutez un domaine personnalisé pour votre site web_

Ajoutez le domaine personnalisé que vous avez acheté et enregistrez-le. Votre site web est maintenant prêt avec votre propre domaine personnalisé ? WOOT! ✨

Donc, nous avons tout configuré sur Github. Nous allons commencer à configurer [Cloudflare](https://www.cloudflare.com) pour dynamiser votre site web avec toutes les fonctionnalités puissantes que j'ai mentionnées au début de cet article.

### Étape 4 : Configurer votre domaine sur Cloudflare

![Image](https://cdn-media-1.freecodecamp.org/images/Zu8TUIiDXMS8gVd6QNhQ8CSnuaOH28V2XJ-P)

Connectez-vous à [Cloudflare](https://www.cloudflare.com). Si vous l'utilisez pour la première fois, vous devriez voir un écran comme l'image montrée ci-dessus. Si vous l'avez déjà utilisé, vous pouvez cliquer sur l'option **Ajouter un site** dans la barre de navigation en haut à droite pour ajouter un nouveau domaine. Entrez le domaine que vous souhaitez gérer et cliquez sur **Démarrer l'analyse**.

### Étape 5 : Configurer les enregistrements DNS pour votre domaine

![Image](https://cdn-media-1.freecodecamp.org/images/0o3RqClqVNTmOlgOx0XdqFSMuep-HkESF3tQ)

![Image](https://cdn-media-1.freecodecamp.org/images/BzsyCCy9E8niq5cc-yp73Lnl4Yxha0TBgckh)
_**Gauche** : Configurer les enregistrements DNS pour le domaine apex. Il est désigné par @. **Droite** : Liste finale des enregistrements DNS_

Dans cette étape, nous informons Cloudflare de pointer notre domaine vers le [serveur Github Pages](https://help.github.com/articles/setting-up-an-apex-domain/#configuring-a-records-with-your-dns-provider) en utilisant deux entrées DNS **A Record** :
1. 192.30.252.153
2. 192.30.252.154

Une fois que vous avez configuré cela, toutes les requêtes vers votre domaine personnalisé, c'est-à-dire _votredomainepersonnalise.com_, seront acheminées vers votre site web sur Github à l'[**Étape 3**](#heading-installation).

Il y a une étape supplémentaire avant de passer à l'étape suivante. Souvent, vous souhaiterez utiliser un sous-domaine comme **www** pour votre site web, c'est-à-dire _www.votredomainepersonnalise.com_. Pour cela, vous devrez ajouter une entrée DNS **CNAME record** qui pointera votre sous-domaine (www) vers votre domaine apex (@).

Une fois que vous avez configuré cela, toutes les requêtes vers votre sous-domaine personnalisé, c'est-à-dire www._votredomainepersonnalise.com_, seront acheminées vers votre site web sur Github à l'[**Étape 3**](#heading-installation).

**NOTE : N'essayez pas d'accéder à votre domaine personnalisé tout de suite. Cela ne fonctionnera pas. Nous avons seulement fait la configuration Cloudflare vers Github. Nous devons encore faire la configuration Registraire DNS -> Cloudflare. Cela viendra à l'[Étape 7](#heading-etape-7).**

Cliquez sur **Continuer** pour passer à l'étape suivante.

### Étape 6 : Choisir le plan gratuit de Cloudflare

![Image](https://cdn-media-1.freecodecamp.org/images/Hfj01XM5X73NgF4qdFHNZoOrYPFhuwnAeP9t)

Le plan gratuit de Cloudflare offre de nombreuses options sophistiquées comme discuté dans la section [Pourquoi Cloudflare ?](#heading-pourquoi-cloudflare) au début.

Cliquez sur **Continuer** pour passer à l'étape suivante.

### Étape 7 : Mettre à jour les serveurs de noms sur votre registraire DNS

![Image](https://cdn-media-1.freecodecamp.org/images/jj0tx9LYgfGjvgWbK4o3G9jNzFvWB9IT49o7)
_Copiez ces deux serveurs de noms mis en évidence dans les paramètres des serveurs de noms de votre registraire DNS_

Une fois que vous êtes sur cette page, gardez-la ouverte dans un onglet et ouvrez le site de votre registraire DNS (l'endroit où vous avez acheté votre domaine) dans un autre. Si vous utilisez l'un des registraires suivants, voici les liens pour comprendre comment changer les serveurs de noms :

1. [Bigrock](http://manage.bigrock.in/kb/servlet/KBServlet/faq455.html)
2. [Namecheap](https://www.namecheap.com/support/knowledgebase/article.aspx/767/10/how-can-i-change-the-nameservers-for-my-domain)
3. [GoDaddy](https://godaddy.com/help/set-custom-nameservers-for-domains-registered-with-godaddy-12317)

Vous devez remplacer les serveurs de noms existants dans les paramètres de votre domaine par ceux sur la page Cloudflare qui est ouverte dans l'autre onglet.

![Image](https://cdn-media-1.freecodecamp.org/images/l8OShr9wOBhUhAUEaK39Qhk0ZY3wWNexIegs)

![Image](https://cdn-media-1.freecodecamp.org/images/8weSeErWSdaqs3qt030oLmhhwPtBMBHUH82u)
_Exemple de l'apparence après avoir mis à jour vos paramètres de serveurs de noms dans votre registraire DNS_

YASSS ! Vous avez réussi à configurer votre domaine personnalisé pour utiliser Cloudflare comme fournisseur DNS. Vous pouvez aller dans l'option **Aperçu** en haut et vous verrez qu'il attend toujours que votre changement de serveurs de noms soit traité.

![Image](https://cdn-media-1.freecodecamp.org/images/gZxnctD-E1ynvH15OWmr20pS0VwfsuUK8XUS)

![Image](https://cdn-media-1.freecodecamp.org/images/CPBfFUpCocFyYLsZS0QZEKnIcFBPhHHscNJs)
_**Gauche** : Le changement de serveurs de noms est toujours en cours de traitement. **Droite** : Le changement de serveurs de noms est traité !_

Une fois que l'onglet **Aperçu** indique **Statut : Actif**, vous pouvez maintenant essayer de visiter votre site en utilisant votre domaine personnalisé, **ET ÇA DEVRAIT JUSTE MARCHER** ! ??

### Étape 8 : Configurer la minification

![Image](https://cdn-media-1.freecodecamp.org/images/-UlrTmWe2KFzCmp1AEaDXiz8ty7uVnnBbQlc)

Dans les paramètres **Vitesse**, dans la section **Minification automatique**, choisissez l'option pour minifier automatiquement tout : Javascript, CSS, HTML. Cela sera fait par Cloudflare à la volée une fois, puis mis en cache. Chaque fois que l'un de vos actifs change, Cloudflare le fera à nouveau pour vous.

L'avantage de la minification est que la taille du fichier livré à votre navigateur est beaucoup plus petite car elle supprime les espaces et les commentaires indésirables.

### Étape 9 : Configurer l'expiration du cache du navigateur

![Image](https://cdn-media-1.freecodecamp.org/images/mlTJMCzd6FA104vxzf16EF-CNcFjhQnUxxzq)
_Expiration du cache définie à 1 mois_

Si vous faites défiler la même page que **Minification automatique**, vous trouverez la section **Expiration du cache du navigateur**. Elle doit être définie à 30 jours/1 mois, idéalement, pour que [WebpageTest](https://www.webpagetest.org) ne vous donne pas d'avertissement. Ce que ce temps indique, c'est que, une fois votre site chargé dans un navigateur, celui-ci ne demandera aucune ressource une seconde fois jusqu'à ce que la période d'expiration du cache du navigateur pour ces ressources expire.

![Image](https://cdn-media-1.freecodecamp.org/images/kz4YtuVfiBzB6VfYkpmkyTPpMZfVa54jx90q)
_Exemple : L'image **iphone.png** se charge depuis votre serveur pour la première fois (22,3 Ko en 349 ms). Toutes les requêtes suivantes pour récupérer cette ressource sont servies depuis le cache disque, ce qui signifie qu'elle est [instantanément](http://www.softwaretestingclub.com/forum/topics/what-is-the-difference-between-disk-cache-memory-cache-browser?commentId=751045%3AComment%3A304464" rel="noopener" target="_blank" title="">presque</a> <a href="https://www.reddit.com/r/explainlikeimfive/comments/3660ig/eli5what_is_the_difference_between_disk_caching/crb1c3i/" rel="noopener" target="_blank" title=") disponible (en 5 ms)_

Avant de passer à l'étape suivante, veuillez vérifier les paramètres **Crypto** sur Cloudflare. Il devrait indiquer **Certificat actif** dans la section **SSL**. (_Note : Essayez de recharger la page. Parfois, elle ne se met pas à jour_). Dans les deux prochaines étapes, nous allons faire en sorte que votre site soit toujours servi via HTTPS. Pour que cela fonctionne sans problème, il est important que vous ayez un certificat actif sur Cloudflare.

![Image](https://cdn-media-1.freecodecamp.org/images/J8VNQi2SB589JR0LyZQfuK8vOZ6T5TCJy9Oy)

![Image](https://cdn-media-1.freecodecamp.org/images/itx2jsX4P4J2Ji-J-y5K98REbZfYnD4uaqkT)
_La section SSL montre **Certificat en cours d'autorisation** après que vos changements de serveurs de noms ont été traités. Une fois qu'un certificat SSL pour vous a été émis, ce message changera pour **Certificat actif**._

### Étape 10 : Configurer les règles de page

Dans cette étape, nous allons faire deux choses :

1. Rediriger toutes les requêtes pour **www.votredomainepersonnalise.com** vers **votredomainepersonnalise.com**
2. Rediriger toutes les requêtes pour **http://votredomainepersonnalise.com** vers **https://votredomainepersonnalise.com**

Allez dans les paramètres **Règles de page** et cliquez sur **Créer une règle de page**.

![Image](https://cdn-media-1.freecodecamp.org/images/WTI5cCO1bX3uOwQzqx35LEADKZM0R87uGV1v)

Pour gérer la redirection de [www.votredomainepersonnalise.com](http://www.votredomainepersonnalise.com) vers **votredomainepersonnalise.com**, remplacez **tweetify.io** par le nom de **votredomainepersonnalise.com**. Cliquez sur **Enregistrer et déployer**.

![Image](https://cdn-media-1.freecodecamp.org/images/7DSCSliTrRLyMYPhwzyAt6acJHmcDrL5ozAp)

Pour gérer la redirection de [http://votredomainepersonnalise.com](http://votredomainepersonnalise.com) vers [**https://votredomainepersonnalise.com**](https://votredomainepersonnalise.com), remplacez **tweetify.io** par le nom de **votredomainepersonnalise.com**. Cliquez sur **Enregistrer et déployer**.

![Image](https://cdn-media-1.freecodecamp.org/images/Hlh3AtXIwFdLiEFxhQx8MRxCs9e5Vnvls7iN)

### Étape 11 : Configurer [HSTS](https://www.owasp.org/index.php/HTTP_Strict_Transport_Security_Cheat_Sheet)

![Image](https://cdn-media-1.freecodecamp.org/images/DZA9uBhWCKwH1jgdXrE0y7dZU2IgPkZExk7P)

Allez dans les paramètres **Crypto** et faites défiler jusqu'à la section **HTTP Strict Transport Security (HSTS)**. Cliquez sur **Activer HSTS**. Cela vous demandera de confirmer que vous savez ce que vous faites. Avant de sélectionner **Je comprends**, laissez-moi vous expliquer pourquoi nous devons activer ce paramètre :

> Si un utilisateur a ouvert votre site web dans le passé, à partir de ce moment, chaque fois que l'utilisateur essaiera d'accéder à votre site web, il sera toujours redirigé vers la version HTTPS de votre site. Cela rend votre site un peu plus rapide lors des visites suivantes car la redirection HTTP vers HTTPS se fait sur le client et non via la règle de page Cloudflare que nous avons ajoutée à l'[Étape 10](#heading-etape-10).

Une fois que vous passez à l'étape suivante, vous devez activer tous les paramètres comme montré ci-dessous. Vous pouvez lire plus de détails sur ces options [ici](https://tools.ietf.org/html/rfc6797#section-6.1.1) et [ici](https://www.owasp.org/index.php/Security_Headers)

![Image](https://cdn-media-1.freecodecamp.org/images/NsniSTdbRi9BbuX44xAekAg93ez8Ehv58lmQ)
_Capture d'écran des paramètres HSTS dans Cloudflare_

![Image](https://cdn-media-1.freecodecamp.org/images/LalAmuWF1UBaysA7p5p9xg4Vr1qIYXvr0Bwq)
_En-têtes qui sont ajoutés par Cloudflare aux requêtes pour votre domaine après avoir configuré HSTS [comme montré ci-dessus](#heading-comme-montre-ci-dessus)_

C'est tout. Vous êtes prêt à montrer votre site web au monde ! ?? Si vous avez trouvé cela utile, veuillez le ❤️ et le partager.

![Image](https://cdn-media-1.freecodecamp.org/images/b-0jLfEMlmveor1qxAnKWoKKZWuXQugsTv6J)

[Karan Thakkar](https://twitter.com/geekykaran) est le responsable frontend chez [Crowdfire](https://www.freecodecamp.org/news/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465/undefined) - _Votre assistant marketing super-intelligent_. Son [article](https://bit.ly/hackingtwitter) a été précédemment [mis en avant](https://bit.ly/geekyonhuffpo) sur [The Huffington Post](https://www.freecodecamp.org/news/an-illustrated-guide-for-setting-up-your-website-using-github-cloudflare-5a7a11ca9465/undefined). Il aime essayer de nouvelles technologies pendant son temps libre et a construit [Tweetify](https://karanjthakkar.com/projects/tweetify) (en utilisant React Native) et [Show My PR's](https://showmyprs.com) (en utilisant Golang).

Autres articles écrits par lui :

[**Comment je suis passé de 300 à 5k abonnés en seulement 3 semaines**](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)
[_#GrowthHacking mon compte Twitter pour @Crowdfire Twitter Premier League_blog.markgrowth.com](https://blog.markgrowth.com/how-i-grew-from-300-to-5k-followers-in-just-3-weeks-2436528da845)[**Utiliser le Certbot de Let's Encrypt pour obtenir HTTPS sur votre boîte Amazon EC2 NGINX**](https://medium.freecodecamp.com/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76)
[_Let's Encrypt est une nouvelle autorité de certification qui fournit des certificats SSL gratuits (jusqu'à une certaine limite par semaine). Il…_medium.freecodecamp.com](https://medium.freecodecamp.com/going-https-on-amazon-ec2-ubuntu-14-04-with-lets-encrypt-certbot-on-nginx-696770649e76)