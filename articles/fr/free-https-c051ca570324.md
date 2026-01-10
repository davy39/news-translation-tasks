---
title: Comment ajouter HTTPS à votre site web gratuitement en 10 minutes, et pourquoi
  vous devez le faire maintenant plus que jamais…
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-02-12T21:54:04.000Z'
originalURL: https://freecodecamp.org/news/free-https-c051ca570324
coverImage: https://cdn-media-1.freecodecamp.org/images/0*G1aejey06DjtUAcO.
tags:
- name: Security
  slug: security
- name: startup
  slug: startup
- name: 'tech '
  slug: tech
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment ajouter HTTPS à votre site web gratuitement en 10 minutes, et pourquoi
  vous devez le faire maintenant plus que jamais…
seo_desc: 'By Ayo Isaiah

  Last week, Google announced that Chrome 68, arriving in July, will mark all HTTP
  pages as “Not secure”.


  The planned change in the Chrome address bar

  This is the strongest nudge yet to drive the web towards encryption by default and
  has...'
---

Par Ayo Isaiah

La semaine dernière, Google a annoncé que Chrome 68, qui arrivera en juillet, marquera toutes les [pages HTTP comme "Non sécurisées"](https://security.googleblog.com/2018/02/a-secure-web-is-here-to-stay.html).

![Image](https://cdn-media-1.freecodecamp.org/images/KJlpSH4gFVWnNr3gacsE9dQS1bnioHJHOdQK)
_Le changement prévu dans la barre d'adresse de Chrome_

C'est la plus forte incitation à ce jour pour pousser le web vers le chiffrement par défaut, et cela fait longtemps que cela arrive.

Bien qu'il y ait une tonne de preuves qui montrent pourquoi tout le monde devrait sauter dans le wagon HTTPS, beaucoup de gens ne voient toujours pas la valeur de servir leurs sites de manière sécurisée.

> « Pourquoi ai-je besoin de cela pour un blog ? »

J'ai déjà écrit sur [la valeur de HTTPS](https://freshman.tech/the-value-of-https/), mais pour réitérer :

* HTTPS protège les utilisateurs contre les [attaques de type Man In the Middle](https://freshman.tech/the-value-of-https/#https-prevents-man-in-the-middle-attacks).
* HTTPS est requis pour utiliser de nombreuses [nouvelles fonctionnalités des navigateurs](https://freshman.tech/the-value-of-https/#many-browser-features-are-exclusive-to-https) telles que les Service Workers.
* HTTPS impacte le [SEO](https://freshman.tech/the-value-of-https/#https-can-provide-seo-benefits).

Si vous n'êtes pas convaincu, lisez [doesmysiteneedhttps.com](https://doesmysiteneedhttps.com/) pour avoir une vue d'ensemble de pourquoi chaque site web devrait être servi de manière sécurisée.

Et si vous ne comprenez toujours pas, alors la vie va devenir beaucoup plus difficile pour vous.

Dans un effort pour éloigner les utilisateurs des sites non sécurisés, les navigateurs ont commencé à stigmatiser les sites servis de manière non sécurisée dans certains contextes.

Chrome 56 a lancé cette tendance en marquant les pages avec des champs de connexion sensibles comme "Non sécurisées", tandis que Chrome 62 a étendu cet avertissement à toutes les pages HTTP contenant un type quelconque de champ de saisie. De plus, l'avertissement est affiché sur toutes les pages HTTP en mode navigation privée, indépendamment de la présence d'un champ de saisie.

Firefox avertit également les utilisateurs lorsqu'ils tentent de remplir un formulaire de connexion non sécurisé.

![Image](https://cdn-media-1.freecodecamp.org/images/UOg75ZXyl499GSy1spRo5U2Vbzlob96XccHK)

Maintenant, Chrome a décidé de placer cet avertissement sur toutes les pages HTTP à l'avenir. Finalement, l'icône à côté de l'étiquette "Non sécurisé" changera et le texte sera mis en rouge pour souligner davantage que les pages HTTP ne peuvent pas être fiables.

![Image](https://cdn-media-1.freecodecamp.org/images/EXVHgs7peMi19ChWdueYMGkF-9wH0beGtkZX)

Pour empêcher les utilisateurs de voir cet avertissement sur votre site web, tout ce dont vous avez besoin est d'obtenir un certificat SSL valide. La bonne nouvelle est que cela n'est plus aussi difficile ou coûteux qu'avant. En fait, je vais vous montrer comment déployer HTTPS sur votre site gratuitement en utilisant [Cloudflare](https://www.cloudflare.com). Et cela ne prendra pas beaucoup de temps du tout.

### Pourquoi Cloudflare ?

Cloudflare peut vous aider à sécuriser un certificat SSL gratuitement, quel que soit l'infrastructure côté serveur que vous avez. Il fonctionne également pour les sites hébergés sur des plateformes qui ne fournissent pas d'accès serveur, comme [GitHub Pages](https://pages.github.com/), [Ghost](https://ghost.org/) et autres.

Vous n'avez pas besoin d'installer quoi que ce soit ou d'écrire du code. Cela en fait une option vraiment excellente pour déployer HTTPS sur votre site web, et le temps de configuration ne devrait littéralement pas prendre plus de 10 minutes.

Il offre également une multitude d'autres avantages en termes de sécurité et de performance de votre site web, que je ne vais pas couvrir ici. Mais je vais parler un peu de son fonctionnement pour que vous ayez une bonne idée de la manière dont il est capable de faire toutes ces choses.

### Comment fonctionne Cloudflare

Cloudflare se place directement au milieu du trafic entre les visiteurs de votre site web et votre serveur. Les visiteurs peuvent être des humains réguliers, des crawlers et des bots (comme les bots des moteurs de recherche) ou des hackers. En agissant comme un intermédiaire entre votre serveur web et les visiteurs de votre site, Cloudflare aide à filtrer tout le trafic illégitime afin que seul le bon trafic passe.

Maintenant, vous pourriez vous demander si tout cela pourrait avoir un effet négatif sur la vitesse de votre site web, mais c'est tout le contraire. Cloudflare a des centres de données partout dans le monde, donc il utilisera simplement le point d'accès le plus proche de votre visiteur, ce qui devrait rendre votre site beaucoup plus rapide qu'avant.

![Image](https://cdn-media-1.freecodecamp.org/images/Lc-xzCU5Cw0u2x-u8zDwE3TFVbv-aUj-JjqK)
_Répartition du réseau mondial de Cloudflare_

Maintenant que nous savons comment fonctionne Cloudflare, examinons comment configurer un site web sur leur infrastructure et comment obtenir HTTPS gratuitement. L'accent ici sera mis sur les fonctionnalités que Cloudflare propose gratuitement, mais notez que des plans payants sont également disponibles avec un ensemble de fonctionnalités supplémentaires.

### Configuration d'un nouveau site

Après vous être [inscrit](https://www.cloudflare.com/a/sign-up) sur Cloudflare, la première chose à faire est d'ajouter un domaine et de scanner les enregistrements DNS.

![Image](https://cdn-media-1.freecodecamp.org/images/o1eN1nEZhtbcRaATWZ1p-nQUCwFBsrWEpalQ)

Une fois l'analyse terminée, tous les enregistrements DNS du domaine seront affichés. Vous pouvez choisir les sous-domaines sur lesquels vous souhaitez activer Cloudflare et apporter les modifications souhaitées. Une fois prêt, cliquez sur **Continuer** pour passer à l'étape suivante.

![Image](https://cdn-media-1.freecodecamp.org/images/XTjdrU156BPJ2Foa2rZuyNAjs53doMdCrJRN)

Sélectionnez le plan gratuit et cliquez sur **Continuer**.

![Image](https://cdn-media-1.freecodecamp.org/images/Nc7rVPCFdQ9LKxx-oEFCj-3zlrjrQqgNQvcO)

Ensuite, vous devrez changer les serveurs de noms sur votre registre de domaine pour ceux fournis par Cloudflare. Le processus pour faire cela sur chaque registre de domaine est légèrement différent, alors vérifiez avec votre registre de domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/xnHu2o4MJrpckhGOvUsDcUoGz0UuujOvxDsU)

Voici à quoi cela ressemble dans [Namecheap](http://namecheap.com) :

![Image](https://cdn-media-1.freecodecamp.org/images/-C7vA1eZcIpP3B5vcq-qYK1eC1Y8Khq8PI9H)
_Changement des serveurs de noms dans Namecheap_

Maintenant, vous devez attendre que les changements de serveurs de noms finissent de se propager. Cliquez sur **Vérifier à nouveau les serveurs de noms** après un certain temps pour voir si votre site est maintenant actif sur Cloudflare. C'est la partie la plus longue de la configuration et cela peut prendre jusqu'à 24 heures, mais dans mon expérience, cela a pris moins de 5 minutes.

![Image](https://cdn-media-1.freecodecamp.org/images/9oHlGNn4TMApCJw1v2GWyQ9ulTA-egOhF6Ew)

Une fois que vos mises à jour de serveurs de noms ont été validées par Cloudflare, votre site devient actif sur le service.

![Image](https://cdn-media-1.freecodecamp.org/images/1AgkTO0uBz8lv0fAdrJhGXz8Rg5nkPfaZDVO)

Si vous voulez être absolument sûr que vos paramètres DNS se sont propagés partout, [What's My DNS](http://whatsmydns.net) fournit un moyen de vérifier quelle adresse IP votre domaine résout dans différents endroits.

Vous pouvez également utiliser `dig` ou `nslookup` en ligne de commande pour vérifier la configuration DNS de votre domaine.

![Image](https://cdn-media-1.freecodecamp.org/images/WAC1LFbxuDtbk-hXxrqot4vUKIxl6b3yFUi9)
_Dans la section RÉPONSE, vous verrez quelle adresse IP votre domaine résout_

De cette façon, vous pouvez être sûr que tout le trafic allant vers votre domaine est maintenant routé via Cloudflare.

Avant de commencer à configurer Cloudflare, assurez-vous que votre navigateur n'utilise pas les anciens enregistrements DNS de son cache. Dans Chrome et Firefox, vous pouvez le faire en effaçant votre historique de navigation.

### Obtenir SSL gratuitement

SSL est toujours un service premium et de nombreuses autorités de certification facturent des montants significatifs avant de délivrer un certificat SSL. Ce n'est pas quelque chose que vous pouvez obtenir gratuitement partout, mais cela change rapidement dans l'industrie.

![Image](https://cdn-media-1.freecodecamp.org/images/kIkCSgOncnKEkE5LClz1UeV0dVDP4i8CFZPw)
_Comodo facture 99,95 $/an pour un certificat SSL_

Maintenant que vous avez Cloudflare qui se place au milieu de votre trafic web, vous devriez obtenir SSL sur votre domaine automatiquement. Cela peut prendre jusqu'à 24 heures pour que le certificat devienne actif, mais dans mon expérience, cela ne prend pas longtemps du tout.

![Image](https://cdn-media-1.freecodecamp.org/images/cZyriRiq6Ao4k48mLCYMjtaLR-aHLa824hXj)
_Vous pouvez vérifier si le certificat de votre site est actif dans les paramètres Crypto._

Une fois que le certificat devient actif, chargez votre site dans un navigateur. Vous devriez voir le site servi via HTTPS et un joli cadenas vert dans la barre d'adresse.

![Image](https://cdn-media-1.freecodecamp.org/images/7ehfhEpKBWEG71hCcQY147j1bBiOQ2Q4YLSF)

Si vous affichez plus d'informations sur le certificat, vous verrez l'autorité de certification qui l'a émis (Comodo dans mon cas) et la date d'expiration. L'une des grandes choses à propos de Cloudflare est que le renouvellement du certificat est fait automatiquement pour vous, donc pas de soucis à ce niveau.

![Image](https://cdn-media-1.freecodecamp.org/images/E6A0jelflOxpON3l4OG-p16p7Qy8udwHqtps)

### Différence entre Flexible, Full et Full (Strict) SSL

Cloudflare rend très facile l'obtention de SSL sur votre site gratuitement sans rien configurer, mais ce n'est pas toujours la même chose que de servir votre site via SSL directement depuis l'origine.

Il existe trois implémentations de SSL de Cloudflare. La première, que vous obtenez par défaut, est Flexible SSL. Dans ce cas, le trafic est chiffré entre les utilisateurs de votre site et Cloudflare, mais ce chiffrement ne va pas jusqu'au serveur d'origine. Cloudflare communique toujours avec votre serveur via HTTP en clair.

Cela signifie que tout Man In The Middle (comme les fournisseurs de réseau) entre Cloudflare et votre serveur peut voir le trafic. Si vous collectez des informations sensibles sur votre site web, abstenez-vous d'utiliser cette option.

Pour avoir un chiffrement jusqu'au serveur d'origine, vous devez utiliser l'implémentation Full ou Full (Strict). La première nécessite que vous installiez un certificat valide sur votre serveur, mais l'authenticité du certificat ne sera pas vérifiée, donc vous pouvez vous en sortir avec un certificat auto-signé. En revanche, l'implémentation Full (Strict) nécessite que vous installiez un certificat SSL valide qui a été signé par une autorité de certification de confiance.

Si vous ne souhaitez pas acheter SSL auprès de sociétés comme Comodo, vous pouvez obtenir des certificats Origin CA gratuits de Cloudflare qui peuvent être utilisés avec les options Full ou Full (Strict) car ils sont approuvés par Cloudflare. Mais gardez à l'esprit que ces certificats ne sont approuvés que par Cloudflare, donc ils cesseront de fonctionner si vous décidez de retirer votre site de l'infrastructure de Cloudflare.

![Image](https://cdn-media-1.freecodecamp.org/images/N2mQFmlgiPlsshjqQml8DLEYBpCfSAwW0049)

Si vous ne contrôlez pas votre environnement serveur, par exemple si votre site est hébergé sur GitHub Pages ou des plateformes similaires, vous ne pourrez pas utiliser les implémentations Full ou Full (Strict), ce qui signifie que même si vos utilisateurs voient HTTPS dans la barre d'adresse, le trafic ne sera pas chiffré jusqu'au serveur d'origine.

Mais c'est toujours une amélioration considérable par rapport à l'absence totale de HTTPS, car cela protégera vos utilisateurs contre les attaques de type Man In The Middle côté client.

### Renforcer l'implémentation SSL

Quelle que soit l'implémentation SSL que vous choisissez, il existe des moyens de la renforcer pour vous assurer que les utilisateurs ne peuvent jamais accéder à votre site via HTTP non sécurisé. [Qualys SSL Labs](https://www.ssllabs.com/ssltest/) est un outil qui vous aide à exécuter un test sur votre configuration SSL pour voir s'il y a des possibilités d'amélioration.

![Image](https://cdn-media-1.freecodecamp.org/images/f9yR7vx-50TyrX2lWQjMTOiFBwc2oUzoUr3W)

Même si j'obtiens une note A sur mon domaine, si vous examinez les résultats en détail, vous verrez qu'il y a définitivement des possibilités d'amélioration dans l'échange de clés et la force de chiffrement.

![Image](https://cdn-media-1.freecodecamp.org/images/EflHwo97oxMhSWGIz6Gu3Xkbq32PwDsBMUl-)

Examinons quelques choses que nous pouvons faire dans Cloudflare pour renforcer notre SSL et obtenir des notes encore plus élevées.

#### Forcer HTTPS partout

Une fois que vous êtes passé à HTTPS, vous voulez définitivement empêcher les utilisateurs d'accéder à votre site via une connexion non sécurisée. Vous pouvez faire cela dans Cloudflare en redirigeant tout le trafic HTTP vers HTTPS avec une redirection 301.

Dans les paramètres Crypto, trouvez l'option **Toujours utiliser HTTPS** et activez-la.

![Image](https://cdn-media-1.freecodecamp.org/images/x1VBeW7nD6Hitnfm6QHowq2bhGAhDXZEsOHw)

#### Activer HTTP Strict Transport Security (HSTS)

[J'ai déjà écrit sur la manière dont HSTS renforce le SSL de votre site](https://freshman.tech/securing-your-website/#http-strict-transport-security-hsts), mais passons brièvement en revue.

Le problème avec la simple redirection 301 du trafic HTTP vers HTTPS est que la requête initiale non sécurisée passe toujours sur le réseau, ce qui signifie qu'elle pourrait être lue par quiconque ayant accès au trafic.

HSTS est un en-tête de réponse qui résout ce problème en indiquant au navigateur qu'il ne peut pas faire de requête non sécurisée à un site web pendant une durée spécifiée.

Voici à quoi ressemble cet en-tête :

```
strict-transport-security: max-age=31536000
```

Une fois que le navigateur reçoit cet en-tête, il ne fera pas de requête non sécurisée à votre site pendant les 31 536 000 prochaines secondes (soit un an). Au lieu de cela, toutes les requêtes HTTP seront automatiquement mises à niveau en HTTPS avant d'être envoyées sur le réseau.

Si vous souhaitez empêcher tous les sous-domaines d'être accessibles via HTTP, vous aurez besoin de la directive `includeSubdomains`. Vous pouvez également ajouter la directive `preload` pour permettre aux fournisseurs de navigateurs d'intégrer votre site dans le navigateur lui-même comme étant uniquement HTTPS.

```
strict-transport-security: max-age=31536000; includeSubdomains; preload
```

Une fois que vous avez activé HSTS sur votre domaine, vous pouvez être assez sûr que, une fois qu'une personne a chargé votre site web via HTTPS, elle ne pourra y accéder que via le schéma sécurisé par la suite.

Donc, avant d'activer HSTS sur votre site, assurez-vous d'être confiant que tout votre trafic sera servi via HTTPS, sinon vous rencontrerez des problèmes.

Pour activer cela dans Cloudflare, allez dans les paramètres **Crypto** et faites défiler jusqu'à la section **HTTP Strict Transport Security (HSTS)**. Cliquez sur **Modifier les paramètres HSTS**, activez toutes les options pertinentes et cliquez sur **Enregistrer**.

![Image](https://cdn-media-1.freecodecamp.org/images/duTVMCLbBXZtlp5QoKLu4gBuzz-qnGRH3CRS)

Et juste au cas où vous vous poseriez la question, le support des navigateurs pour HSTS est assez bon.

![Image](https://cdn-media-1.freecodecamp.org/images/kvk9x7Ffgtm8Hj7uJG3SNbqcVvhv6bdv0Sxy)

#### Corriger les références de schéma non sécurisé

Si vous incorporez une ressource passive (comme une image) de manière non sécurisée sur une page sécurisée, le navigateur la charge toujours correctement. Il retire simplement le cadenas vert de la barre d'adresse. Vous pouvez voir un exemple de cette erreur [ici](https://mixed.badssl.com/).

![Image](https://cdn-media-1.freecodecamp.org/images/PztuGkSktiMG9zRjN4Dc1Haa9ZU4ExWAkcvG)

Si vous vérifiez la console du navigateur, vous verrez des avertissements ou des erreurs qui pointent vers la ressource qui a été incorporée de manière non sécurisée. Dans ce cas, c'est :

```
<img class="mixed" src="http://mixed.badssl.com/image.jpg" alt="HTTP image">
```

![Image](https://cdn-media-1.freecodecamp.org/images/WD4db17NSC2rNZo4gXdamnM6A4q54CE0Y0kQ)

Pour corriger cela, changez simplement le schéma en HTTPS et tout sera à nouveau correct.

```
<img class="mixed" src="https://mixed.badssl.com/image.jpg" alt="HTTP image">
```

Si vous avez beaucoup de contenu sur votre site incorporé de manière non sécurisée, trouver et corriger chacun d'eux pourrait être assez fastidieux. Mais Cloudflare peut à nouveau vous aider avec la fonctionnalité [Automatic HTTPS Rewrites](https://support.cloudflare.com/hc/en-us/articles/227227647-How-do-I-use-Automatic-HTTPS-Rewrites-).

![Image](https://cdn-media-1.freecodecamp.org/images/TInVTocyWO2EfauqD6OfOpmHWb0x65C5-cq3)

Pour être doublement sûr que aucun contenu de votre site web ne puisse jamais être servi de manière non sécurisée, envisagez de mettre en place une [Content Security Policy](https://freshman.tech/securing-your-website/#content-security-policy-csp) sur votre site.

Maintenant, voyons comment les changements ci-dessus ont affecté notre rapport SSL Labs. J'ai relancé le test sur mon domaine, et maintenant nous obtenons une note A+.

![Image](https://cdn-media-1.freecodecamp.org/images/Q0jdFp2spaP7pWbehBEXBQJMFblx4K3YPKIT)

Si vous vérifiez les notes individuelles dans le graphique, rien n'a changé, mais nous obtenons toujours une implémentation SSL vraiment sécurisée gratuitement et en quelques minutes seulement.

![Image](https://cdn-media-1.freecodecamp.org/images/L9vbROCIfrsio5SwUybP-eTil0YGuclRgUzy)

### Alternatives à Cloudflare pour SSL gratuit

Si vous préférez ne pas utiliser Cloudflare pour une raison quelconque, il existe d'autres moyens d'obtenir votre site web sur HTTPS gratuitement. Voici deux options que vous pouvez essayer :

#### Let's Encrypt

Si vous avez le contrôle sur votre serveur, vous pouvez rapidement déployer HTTPS sur votre site en utilisant [Let's Encrypt](https://letsencrypt.org/). Ils offrent des certificats SSL gratuits qui durent trois mois et peuvent être renouvelés automatiquement.

Même si vous n'avez pas accès au serveur, vérifiez avec votre hébergeur web. Certains hébergeurs vous permettront d'utiliser Let's Encrypt SSL sans fournir d'accès shell.

#### Amazon AWS Certificate Manager

[Amazon](https://aws.amazon.com/certificate-manager/) délivre également et renouvèle automatiquement les certificats SSL pour les clients sur son infrastructure Amazon Web Services (AWS). Ainsi, vous pouvez configurer et oublier HTTPS sur votre site si vous utilisez des ressources AWS telles que Cloudfront.

Quelle que soit la manière dont vous implémentez HTTPS sur votre site web, l'essentiel est de vous assurer que vous êtes configuré dès que possible afin que vos utilisateurs bénéficient des avantages de sécurité qu'il offre et que vous ne manquiez pas plusieurs fonctionnalités intéressantes dans les navigateurs qui vous aideront à créer de meilleures expériences web.

Si vous avez aimé cet article, partagez-le avec d'autres qui pourraient en bénéficier. Au fait, consultez mon blog sur [freshman.tech](https://freshman.tech) pour des articles sur le développement web. Merci pour la lecture.