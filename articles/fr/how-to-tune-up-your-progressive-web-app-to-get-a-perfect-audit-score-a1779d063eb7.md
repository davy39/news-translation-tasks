---
title: Comment optimiser votre Progressive Web App pour obtenir un score d'audit parfait
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-06-18T16:27:12.000Z'
originalURL: https://freecodecamp.org/news/how-to-tune-up-your-progressive-web-app-to-get-a-perfect-audit-score-a1779d063eb7
coverImage: https://cdn-media-1.freecodecamp.org/images/0*Xfaf0E9NtFH7seZM.png
tags:
- name: Angular
  slug: angular
- name: JavaScript
  slug: javascript
- name: progressive web app
  slug: progressive-web-app
- name: technology
  slug: technology
- name: Web Development
  slug: web-development
seo_title: Comment optimiser votre Progressive Web App pour obtenir un score d'audit
  parfait
seo_desc: 'By Ondrej Chrastina

  Progressive Web Apps (PWAs) quickly became the hottest development platform during
  the last year. Let’s take a look at what you need to do to adhere to the PWA standards.

  Articles about the PWA concept are all over the place. I wi...'
---

Par Ondrej Chrastina

Les Progressive Web Apps (PWA) sont rapidement devenues la plateforme de développement la plus en vogue l'année dernière. Examinons ce que vous devez faire **pour adhérer aux normes PWA.**

Les articles sur le concept des PWA sont partout. Je vais me concentrer sur les étapes concrètes à suivre pour que la PWA soit parfaitement alignée sur les spécifications. Je fournirai un lien GitHub avec la liste des modifications pour chaque étape que j'ai effectuée afin que vous puissiez facilement essayer par vous-même.

### Prérequis

* [node.js](https://nodejs.org/en/download) v8+
* Navigateur [Google Chrome](https://www.google.com/chrome/) v60+

Je vais commencer avec cette simple application Angular que j'ai utilisée pour montrer la combinaison d'Angular et de l'approche PWA dans mon [article précédent](http://bit.ly/pwa-in-angular-and-headless-cms). Je l'ai [mise à niveau](https://github.com/Kentico/cloud-sample-angular-pwa-app/pull/1) vers Angular v6 et [Kentico Cloud SDK v4](http://bit.ly/kc-js-cloud-sdk-v4).

![Image](https://cdn-media-1.freecodecamp.org/images/DgVUccQ9UixlgkMxLh7qbEg-AX40bYZiXcJJ)
_[Modifications de mise à niveau](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/443472555e627fc149e8b6d38d84cef228e0ac21" rel="noopener" target="_blank" title=")_

Cette application est une simple liste de lieux intéressants stockés dans un CMS headless chargés par le SDK. L'application possède déjà ces deux avantages qui en font une application PWA :

* `manifest.json` avec un ensemble d'icônes utilisées lorsque l'application est installée dans le système.
* implémentation d'un service worker utilisé pour la mise en cache du squelette de l'application (appelé app shell) et des données du CMS headless.

![Image](https://cdn-media-1.freecodecamp.org/images/hsRG5ts-kQ1s1k5uVWD1D1bMcC5RuUsvDA5P)

Bien que l'application soit prête à être installée et utilisée, **elle a encore besoin de quelques ajustements pour répondre aux spécifications PWA.**

### Comment passer la checklist PWA

Pour vérifier si l'application répond à tous les critères définis par la [checklist Google](https://developers.google.com/web/progressive-web-apps/checklist), on peut utiliser divers outils de nos jours. Le plus populaire s'appelle [Lighthouse](https://developers.google.com/web/tools/lighthouse).

![Image](https://cdn-media-1.freecodecamp.org/images/gL2OcEH88JhPypm7IMJKxpIJaafA5XW7wt1v)
_[Checklist Google](https://developers.google.com/web/progressive-web-apps/checklist" rel="noopener" target="_blank" title=")_

Lighthouse est déjà intégré dans les outils de développement du navigateur Google Chrome [developer tools](https://developers.google.com/web/tools/lighthouse/#devtools) sur l'onglet [audit](https://developers.google.com/web/updates/2017/05/devtools-release-notes#lighthouse). Pour l'exécuter, je vous recommande de publier la variante de production de l'application sur Internet et d'effectuer l'audit à partir de là.

Pour y parvenir, téléchargez simplement l'application dans l'état "initial" puis exécutez les commandes suivantes.

Pour le déploiement, j'utilise [surge](https://surge.sh/). Vous devez simplement vous inscrire et installer les outils CLI. Ensuite, vous pouvez déployer le dossier dans un sous-domaine *.source.sh.

![Image](https://cdn-media-1.freecodecamp.org/images/SvXmPZVDOy8AbV4N1w6jMyeP2CtRAzDl4hD0)
_[État initial de l'application](http://bit.ly/git-repo-angular-pwa-before-audit" rel="noopener" target="_blank" title=")_

* `npm install`
* `npm run build` pour construire l'application en mode production dans le dossier `/dist`
* `npm install -g surge` pour installer surge CLI globalement
* `surge /dist votre-sous-domaine.surge.sh` déployer le dossier "dist" vers l'URL spécifiée. Cela nécessite que vous vous connectiez ou [définissiez les variables d'environnement surge](https://docs.travis-ci.com/user/deployment/surge#Environment-variables) avec le login et le token.

Ensuite, naviguez simplement vers l'application dans le navigateur Chrome. Allez dans "Outils de développement" > "Audits" > "Effectuer un audit" > sélectionnez "Progressive Web App" > "Exécuter l'audit". Vous verrez les résultats suivants.

![Image](https://cdn-media-1.freecodecamp.org/images/gk8m5IDRjuVsWu1lMwdkkjPBcSU9SmWCHz4o)

Comme vous pouvez le voir, huit vérifications ont déjà réussi.

Maintenant, examinons la checklist PWA.

### Checklist PWA

#### Solution de repli lorsque JavaScript n'est pas disponible

Tout ce que vous avez à faire pour supprimer ce message est de fournir un message pour les navigateurs sans JavaScript. La balise `noscript` est un moyen idéal pour cela. Ajoutez simplement le code HTML suivant au corps de `index.html`.

```
...<noscript>    Cette page nécessite que JavaScript soit activé.</noscript>...
```

![Image](https://cdn-media-1.freecodecamp.org/images/hoYVfT5QWsbq8seVneFyXYi-6HimWlhEJnuw)
_[Ajouter le contenu no-script](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/65ae78f74713eb3d6719673e6d21ae0e8c8d5497" rel="noopener" target="_blank" title=")_

#### La barre d'adresse ne correspond pas aux couleurs de la marque

Cet avertissement vous indique que vous devez spécifier la couleur thématique de base pour la barre d'adresse. Tout ce dont vous avez besoin est une balise méta `HTML` dans la section head de la page. J'ai choisi la même couleur que celle utilisée pour la barre d'outils supérieure.

```
<html><head>...<meta name="theme-color" content="#1e88e5">...</head>...
```

![Image](https://cdn-media-1.freecodecamp.org/images/AebJUq6fV5ESn9rJemam9Xp2JvhONfNYROGM)
_[Ajouter la balise méta de couleur de thème](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/3293c5f93726674289186ccddedaeac99350bc0b" rel="noopener" target="_blank" title=")_

![Image](https://cdn-media-1.freecodecamp.org/images/OJVdeXrUQlSZMNnFZFQaRbbuaruwuRj4tYzJ)

#### Le trafic HTTP n'est pas automatiquement redirigé vers HTTPS

Il s'agit simplement de la configuration du déploiement. Pour obtenir une [application automatique de https](https://surge.sh/help/using-https-by-default), utilisez simplement "https://" avant le domaine où vous souhaitez déployer l'application.

* `surge /dist [**https://**votre-sous-domaine.surge.sh](https://url-where-you-want-to-deploy-you-app.surge.sh)`

Vous êtes maintenant prêt à effectuer l'audit à nouveau.

* `npm run build`
* `surge /dist [**https://**votre-sous-domaine.surge.sh](https://url-where-you-want-to-deploy-you-app.surge.sh)`

![Image](https://cdn-media-1.freecodecamp.org/images/Wjq4nJ11MBLPuI-LTFTqQVwYSPhzanujT4oh)

**Hourra !**

Vous avez réussi toutes les vérifications automatiques. Maintenant, vous avez peut-être remarqué qu'il y avait des étapes manuelles décrites dans le rapport :

* Le site fonctionne sur plusieurs navigateurs
* Les transitions de page ne donnent pas l'impression de bloquer le réseau. Chaque fois que vous appuyez sur un lien/bouton, l'application doit effectuer la transition immédiatement ou afficher un indicateur de chargement pendant que l'application attend une réponse du réseau.
* Chaque page doit avoir une URL — nous devons pouvoir créer des URL pour le partage. Cela est principalement destiné aux applications monopages pour s'assurer que le routeur côté client est capable de reconstruire l'état de l'application à partir d'une URL donnée.

### Bonus - chargement initial plus rapide dans Angular

Prévoyez-vous de rendre votre application vraiment grande ? Voulez-vous qu'elle affiche immédiatement son squelette tout en chargeant tous les composants Angular en arrière-plan ? En fait, avec des applications plus grandes, vous pourriez obtenir un avertissement dans le rapport indiquant que le premier chargement prend trop de temps.

Pour accélérer les choses, ajoutez simplement un code `HTML` statique dans le fichier du composant racine Angular. Ce HTML sera affiché pendant l'initialisation. Dans le lien de commit ci-dessous, vous pouvez voir que j'ai également ajouté quelques styles statiques pour que tout soit rendu en une seule fois.

```
..<app-root>    <header class="static" style="width: 100%;        height: 56px;        color: #fff;        background: #1e88e5;        position: fixed;        box-shadow: 0 4px 5px 0 rgba(0, 0, 0, .14), 0 2px 9px 1px rgba(0, 0, 0, .12), 0 4px 2px -2px rgba(0, 0, 0, .2);        padding-left: 16px;        margin: auto;        z-index: 10000;">        <h2 style="font-size: 20px;">Pack and Go</h2>    </header>    <main style="padding-top: 60px;        flex: 1;        overflow-x: hidden;        overflow-y: auto;"></main></app-root>...
```

Ci-dessous, vous pouvez voir le résultat lorsque testé avec le paramètre de connexion "Slow 3G".

![Image](https://cdn-media-1.freecodecamp.org/images/b0fN53QRtod8uKy6bSGLYhdzZldy2hLS8LsM)

![Image](https://cdn-media-1.freecodecamp.org/images/Q5OWTluieGNAAtF22wXF1mKgMeb90kWr5uOr)
_[Ajouter un squelette d'application statique](https://github.com/Kentico/cloud-sample-angular-pwa-app/commit/8521c612e273fc91670a408488dc981ad7023895" rel="noopener" target="_blank" title=")_

### Conclusion

Très bien, nous avons terminé ! Si vous aspirez à une application PWA ultra-moderne construite sur un framework robuste, vous l'avez maintenant.

L'application fonctionne sur la dernière version d'Angular et est soutenue par un CMS [headless Kentico Cloud](http://bit.ly/kc-home) rapide. Elle répond à **toutes** les exigences de l'outil d'audit Lighthouse de Google.

Si vous êtes intéressé par l'intégration des vérifications Lighthouse dans votre écosystème d'intégration continue, n'hésitez pas à me contacter via [Twitter](http://bit.ly/twitter-freecodecamp) !