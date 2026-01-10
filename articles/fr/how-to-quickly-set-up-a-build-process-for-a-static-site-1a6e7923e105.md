---
title: Comment configurer rapidement un processus de build pour un site statique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-11T17:23:15.000Z'
originalURL: https://freecodecamp.org/news/how-to-quickly-set-up-a-build-process-for-a-static-site-1a6e7923e105
coverImage: https://cdn-media-1.freecodecamp.org/images/1*lWOnHgWDaYgoBFh9dErY-A@2x.png
tags:
- name: Continuous Integration
  slug: continuous-integration
- name: JavaScript
  slug: javascript
- name: General Programming
  slug: programming
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment configurer rapidement un processus de build pour un site statique
seo_desc: 'By Ondřej Polesný

  You have a static site all implemented and ready for the world to see, but where
  should you host it? How do you select the right platform and plan for a set of static
  files? How can you ensure that the website will automatically reg...'
---

Par Ondřej Polesný

Vous avez un site statique entièrement implémenté et prêt à être vu par le monde, mais où devez-vous l'héberger ? Comment sélectionner la bonne plateforme et le bon plan pour un ensemble de fichiers statiques ? Comment pouvez-vous vous assurer que le site sera automatiquement régénéré chaque fois que vous modifiez son contenu ?

Dans cet article, je vais vous montrer comment générer un site statique, configurer un processus de build automatique déclenché par les changements de contenu et déployer le site sur un serveur public.

### Introduction

Dans les articles précédents, j'ai expliqué comment [construire un site web dynamique JavaScript avec du contenu provenant d'un CMS headless](http://bit.ly/2CyDnhX) [Kentico Cloud](http://bit.ly/2QzUALM). Ensuite, je vous ai montré [comment le convertir en site statique](http://bit.ly/2PN46Jy) pour améliorer les performances, la sécurité et le SEO. Il est maintenant temps de générer ce site et de le mettre en ligne pour que le monde entier puisse le voir.

### Génération d'un site statique

Chaque générateur de site statique vous permet de construire le site localement sans générer tous les fichiers après chaque modification d'un seul fichier. Si vous avez suivi mes articles, vous avez un site sur Vue.js qui est converti pour utiliser Nuxt.js comme framework mais qui nécessite toujours un serveur de développement pour gérer les requêtes du site web. Pour générer les fichiers statiques, exécutez la commande suivante :

```
npx nuxt generate
```

Ouvrez le dossier `dist` à la racine de votre projet pour trouver les fichiers générés et vérifiez `index.html` pour vous assurer que votre site web est généré correctement. J'ai l'habitude de vérifier également les pages enfants où je sais qu'il y a du contenu provenant d'un CMS headless, comme une page de blog. Si vous voyez le contenu sous forme HTML, vous avez gagné !

### Où héberger un site statique ?

C'est probablement la prochaine question que vous vous posez après avoir généré tous les fichiers. Si vous reconstruisez un site et que votre ancien site web est toujours en ligne, vous pensez probablement à utiliser le même fournisseur pour le site statique. C'est parfaitement bien. Cependant, si votre ancien site était construit sur un CMS traditionnel ou un autre langage de programmation, vous devrez peut-être y réfléchir à deux fois.

Votre espace d'hébergement actuel est dimensionné pour répondre aux exigences d'un autre système ou conçu pour supporter une configuration spécifique, comme PHP et MySQL ou .NET et PostgreSQL. Donc, si c'est le cas, vous avez probablement utilisé la quantité de trafic, de sessions et d'autres valeurs pour calculer la quantité de puissance de calcul dont vous aurez besoin (ou comme moi dans le passé, vous avez simplement espéré que cela irait).

Avec les sites statiques vient le soulagement : plus de formules compliquées, d'approximations et de devinettes professionnelles. Héberger un ensemble de fichiers statiques est quelque chose que chaque serveur web peut faire facilement. L'aspect le plus important est que le serveur n'a plus besoin de passer par le pipeline sophistiqué de gestion des requêtes pour chaque hit. Il sert simplement des fichiers statiques à la place. Et c'est facile et rapide.

L'hébergement de sites statiques est donc beaucoup moins cher. Il existe des dizaines de services qui vous permettent d'héberger vos sites web gratuitement ou au moins d'avoir des plans de démarrage gratuits. Ils incluent :

* [GitHub pages](http://bit.ly/2AAQrR5)
* [Netlify](http://bit.ly/2TEmPJK)
* [Heroku](http://bit.ly/2VHD0If)
* et d'autres fournisseurs globaux et locaux. Vous pouvez, bien sûr, utiliser des services d'hébergement de sites web globaux comme Azure ou AWS également.

J'ai décidé de choisir GitHub pages car tous mes dépôts sont déjà hébergés sur GitHub. C'est également complètement gratuit et prend en charge les domaines personnalisés de 2ème niveau.

### Comment construire et déployer un site statique ?

Mais ce n'est pas seulement une question d'hébergement. Avoir les pages en ligne est essentiel, mais il est tout aussi important de penser à l'ensemble du processus de déploiement. C'est-à-dire, comment les pages statiques vont-elles être générées et transportées vers le serveur. Pour la première build, vous pouvez générer des pages dans votre environnement local en utilisant `npx nuxt generate` et copier-coller les fichiers statiques vers votre espace d'hébergement via FTP. Mais allez-vous répéter ce processus chaque fois qu'il y a un changement de contenu ?

![Image](https://cdn-media-1.freecodecamp.org/images/TOkelGF8EBjynGKQy8H62YPjMh98lIWIuNgS)

Le processus de déploiement d'un site statique comporte trois parties :

1. Déclencheur
2. Build
3. Déploiement

### Déclencheur

Une nouvelle build doit se produire lorsqu'un changement de contenu ou de mise en œuvre se produit. Cela signifie que chaque fois qu'un éditeur de contenu publie un nouveau contenu dans un [CMS headless](http://bit.ly/2QzUALM), ou que vous modifiez le code source, le site web doit être reconstruit. Mais comment y parvenir ?

![Image](https://cdn-media-1.freecodecamp.org/images/0UAVMwIbWrAJT-SMlTDL1nDbM7lzGLl3WWA4)

#### Déclencheur de changement de contenu

Chaque CMS headless mature dispose de [webhooks](http://bit.ly/2QzOdeS). Ils représentent une notification de service à service concernant un certain type d'action. Ainsi, lorsqu'un éditeur publie un élément de contenu, le CMS headless initie une notification de webhook qui est envoyée à une URL définie. Dans ce cas, à un serveur de build qui agira en fonction de la notification et reconstruira le site.

Mais comment le serveur de build sait-il quoi faire ? Eh bien, il n'a aucune idée du type de stockage de contenu que vous utilisez et ne comprendrait probablement pas la notification générique de webhook. Pour cette raison, j'ai ajouté une simple fonction Azure au milieu qui fait deux choses — d'abord, elle vérifie que l'origine de la notification est Kentico Cloud :

```
...
```

```
if (!isValidSignature(req, process.env['KC_WEBHOOK_SECRET'])) { context.log('Signature was invalid'); return;}
```

```
...
```

```
const isValidSignature = (req, secret) => { const givenSignature = req.headers['x-kc-signature']; const computedSignature = crypto.createHmac('sha256', secret) .update(req.rawBody) .digest();
```

```
 return crypto.timingSafeEqual(Buffer.from(givenSignature, 'base64'), computedSignature);}
```

_(voir le fichier complet [sur GitHub](https://github.com/Kentico/kentico.github.io/blob/source/src/azureFunctions/fireSiteRegeneration/index.js))_

et ensuite déclenche la build en utilisant l'API du serveur de build :

```
request.post({ url: "https://api.travis-ci.org/repo/Kentico%2Fkentico.github.io/requests", headers: { "Content-Type": "application/json", "Accept": "application/json", "Travis-API-Version": "3", "Authorization": `token ${process.env['TRAVIS_TOKEN']}` },
```

```
...
```

_(voir le fichier complet [sur GitHub](https://github.com/Kentico/kentico.github.io/blob/source/src/azureFunctions/fireSiteRegeneration/index.js))_

Je sais, Azure vous demande votre carte de crédit avant de pouvoir créer des fonctions. Mais vous pouvez utiliser [Webtask.io](http://bit.ly/2yCjNgl), qui est complètement gratuit. J'ai expliqué comment créer une fonction simple là-bas dans [un de mes articles précédents](http://bit.ly/2P0gidP).

![Image](https://cdn-media-1.freecodecamp.org/images/bLPPwLQ6jTgOOAw8WhYfcUEvTxLn5rlloQUb)

### Déclencheur de changement de code

Avec le code, le processus devient encore plus facile. Les serveurs de build offrent souvent une intégration directe avec GitHub, il suffit donc d'autoriser le serveur de build avec GitHub. Lorsque vous poussez votre changement de code dans un dépôt distant, le serveur de build reçoit l'information automatiquement et, en fonction de sa configuration, déclenche une nouvelle build.

### Build

Je sais, les mots « serveur de build » semblent si compliqués et coûteux. Mais lorsque vous y pensez, la seule chose qu'un serveur de build doit faire pour vous est de générer des pages et de les déployer. Exactement ce que vous avez fait manuellement avec une commande `npx` et une opération de copier-coller. Et ce n'était pas si difficile, n'est-ce pas ?

Alors, comment pouvez-vous décider quel serveur de build utiliser ? Tout d'abord, vous devez choisir si vous souhaitez exécuter la build localement sur votre serveur ou à distance sur un service tiers. Je n'ai pas de serveur local que je pourrais utiliser à cette fin, donc j'ai décidé d'utiliser des services tiers. Ces services incluent :

* [AppVeyor](http://bit.ly/2spdv0M)
* [Travis CI](http://bit.ly/2RKgW0q)

Ces deux services sont gratuits pour les projets open-source.

« Quoi ? Mon site web est-il open-source ? Ce gars est fou ! »

Suis-je fou ? 😊 J'ai déjà mentionné les avantages de l'open-sourcing de l'implémentation de votre site web dans mon [article précédent sur la sécurité](http://bit.ly/2QVSm9a). Dans la plupart des cas, les sites web sont très similaires en termes de fonctionnalités, donc il n'y a probablement pas de savoir-faire spécial dans votre implémentation. C'est le contenu qui détient la valeur.

Mais revenons au serveur de build. J'ai choisi Travis CI car il m'a été recommandé par un collègue. Nous l'utilisons pour de nombreux projets GitHub dans notre entreprise. Alors, combien de temps faut-il pour le configurer ?

Au début, je m'attendais à une interface utilisateur compliquée pour configurer tous les aspects d'une build dans Travis (vous vous souvenez de VSTS en ligne ?), donc découvrir que tout se trouve dans un seul fichier a été un soulagement. La première chose que vous devez faire est donc de créer un fichier #.travis.yml# à la racine de votre projet. Ce fichier définit ce qui se passe pendant une build.

```
dist: trusty language: node_js node_js: — "stable" before_script: — npm install script: — npm run build deploy: ...
```

```
packages.json:"scripts": { ... "build": "npx nuxt generate && cpx CNAME dist", ...}
```

Vous voyez, c'est simple à comprendre. D'abord, j'instruis NPM d'installer tous les packages requis comme prérequis à l'exécution d'une build. Ensuite, tous les fichiers statiques sont générés dans un dossier `dist` — c'est la valeur par défaut lors de l'utilisation de Nuxt. J'ai également inclus un aperçu d'un fichier `packages.json`, qui définit le script de build. Notez que je copie également le fichier `CNAME` dans le répertoire `dist` — cela indique à GitHub Pages que j'utilise un domaine personnalisé plutôt que github.io.

### Déploiement

Enfin, la dernière partie de tout le processus. Nous avons généré les fichiers, et maintenant nous devons les transférer vers notre espace d'hébergement, tout comme nous l'avons fait auparavant en utilisant FTP. C'est encore une autre chose qu'un serveur de build peut faire pour vous.

Comme je l'ai mentionné précédemment, j'ai choisi GitHub Pages comme hébergeur et Travis CI comme serveur de build. Travis fournit [de nombreuses options](http://bit.ly/2RshbOb) pour les déploiements automatisés, y compris GitHub Pages, donc la configuration a été un jeu d'enfant. Jetez un coup d'œil à la configuration de déploiement :

```
deploy: local-dir: dist target-branch: master provider: pages skip-cleanup: true github-token: $GITHUB_TOKEN keep-history: true verbose: true on: branch: source
```

`Local-dir` définit où se trouvent mes pages statiques générées, `target-branch` marque une branche dans le dépôt GitHub à déployer, et `pages` est le nom du fournisseur Travis pour GitHub Pages. Pour déployer avec succès, vous devez également générer et fournir un `github-token`. Vous voyez qu'il y a juste une variable dans la configuration de build car le fichier se trouve dans un dépôt public. La valeur du token est stockée dans les paramètres du dépôt dans l'interface utilisateur de Travis.

### La finale de la série

Et c'est tout. C'est tout ce dont vous avez besoin pour déclencher, construire et déployer un site statique automatiquement. Sans aucune expérience préalable avec les processus de build et de déploiement, cela ne devrait pas vous prendre plus de quelques heures. Vous voyez, les sites statiques peuvent être très dynamiques en termes de contenu, la génération réelle de fichiers statiques est gérée automatiquement sans un seul effort humain.

Au cours de cette série d'articles, j'ai expliqué comment construire un site web en utilisant le Content-as-a-Service (CaaS) pour stocker votre contenu, comment garantir que votre site web est sécurisé en n'utilisant aucune base de données, et comment garantir qu'un tel site web contient toujours des fonctionnalités dynamiques comme les soumissions de formulaires.

Bonne chance avec vos nouveaux sites statiques et passez une [#staticNewYear](http://bit.ly/2QLE7Tj) !

#### Autres articles de la série :

1. [Comment commencer à créer un site web impressionnant pour la première fois](http://bit.ly/2Duglu1)
2. [Comment choisir la meilleure technologie pour votre site web ?](http://bit.ly/2N0kXY4)
3. [Comment dynamiser votre site web avec Vue.js et un effort minimal](http://bit.ly/2zLRE8a)
4. [Comment mélanger un CMS headless avec un site web Vue.js et payer zéro](http://bit.ly/2CyDnhX)
5. [Comment sécuriser les soumissions de formulaires sur un site web API](http://bit.ly/2P0gidP)
6. [Construire un site web super rapide et sécurisé avec un CMS n'est pas un gros problème. Ou est-ce que c'est le cas ?](http://bit.ly/2QVSm9a)
7. [Comment générer un site web statique avec Vue.js en un rien de temps](http://bit.ly/2PN46Jy)
8. **Comment configurer rapidement un processus de build pour un site statique**