---
title: Comment configurer le rendu côté serveur dans React avec Rails en utilisant
  Puppeteer
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-02-21T06:00:04.000Z'
originalURL: https://freecodecamp.org/news/server-side-rendering-react-with-rails-using-puppeteer-cf5ec2697e88
coverImage: https://cdn-media-1.freecodecamp.org/images/0*JDwIoDI39Uzjzp5c
tags:
- name: General Programming
  slug: programming
- name: puppeteer
  slug: puppeteer
- name: Rails
  slug: rails
- name: React
  slug: react
- name: 'tech '
  slug: tech
seo_title: Comment configurer le rendu côté serveur dans React avec Rails en utilisant
  Puppeteer
seo_desc: 'By Sitaram Shelke

  This post is co-authored by Hricha Kabir, my colleague at Altizon Systems. She was
  working on this task primarily. I had the chance to learn along the way.


  _Photo by [Unsplash](https://unsplash.com/@rvruggiero?utm_source=medium&utm...'
---

Par Sitaram Shelke

Cet article est co-écrit par [Hricha Kabir](https://in.linkedin.com/in/hrichakabir), ma collègue chez [Altizon Systems](http://www.altizon.com). Elle travaillait principalement sur cette tâche. J'ai eu l'occasion d'apprendre en cours de route.

![Image](https://cdn-media-1.freecodecamp.org/images/SFMTJgWJQqSDFXU-rUJrn4HkgCccugY1GpYh)
_Photo par [Unsplash](https://unsplash.com/@rvruggiero?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title="">Robert V. Ruggiero</a> sur <a href="https://unsplash.com?utm_source=medium&amp;utm_medium=referral" rel="noopener" target="_blank" title=")_

Nous travaillons sur un produit IoT axé sur les industries manufacturières et construisons des rapports d'analyse. La plupart du temps, la conception des rapports et les informations varient en fonction du rôle de l'utilisateur qui va les consulter.

Exemple : Une personne de niveau directeur s'intéresse à un rapport consolidé d'une semaine, tandis qu'un chef de département s'intéresse aux statistiques d'une seule journée et qu'un responsable qualité est attentif aux données de shift. Si nous descendons davantage dans la hiérarchie, le responsable de production sera celui qui souhaite consulter les données de production en direct.

Pour les données en direct, le responsable de production peut ouvrir le tableau de bord en direct et le surveiller, mais l'utilisateur qui souhaite voir un rapport consolidé ne préférera pas se connecter au produit et consulter un rapport. Au lieu de cela, ils préfèrent une communication par email planifiée qui enverra un rapport basé sur une heure planifiée et le répétera indéfiniment jusqu'à ce qu'un utilisateur arrête ce travail planifié.

Ainsi, notre tâche était d'écrire un utilitaire qui envoie périodiquement un rapport particulier à un utilisateur par email sur une base quotidienne ou à une heure planifiée définie. Pour la planification, nous utilisons [Sidekiq](https://sidekiq.org/), mais notre principal défi était : comment exécuter/calculer le rapport côté serveur (sans ouvrir de navigateur) et l'envoyer par email.

Dans tous nos produits, nous utilisons **React** pour le front-end et il effectue le travail lourd de rendu du rapport dans le navigateur. Pour atteindre l'objectif d'attacher le même rapport dans l'email, nous aurions dû concevoir un modèle HTML pour chaque rapport. Cela signifie que nous aurions eu 2 vues de chaque rapport, une écrite en HTML et une autre en ReactJS.

Cela présente les inconvénients suivants :

**1.** La base de code du produit aura un code dupliqué qui viole le principe DRY pour le développement logiciel.

**2.** Augmente le temps de conception d'un rapport, ce qui impacte la livraison du produit.

Nous avons décidé de rechercher d'autres solutions possibles au lieu d'écrire le même code deux fois. Et nous avons rencontré les options suivantes et les avons explorées une par une jusqu'à ce que nous réussissions à atteindre notre objectif.

**1. Capture d'écran :** Imprimer le rapport en utilisant la capture d'écran et l'envoyer en tant que pièce jointe.

**2. Bouton d'impression FrontEnd :** Dans l'interface utilisateur du rapport, ajouter un bouton d'impression qui convertira le composant React en page HTML/PDF.

**3. Gem Ruby :** Il existe une gem Ruby qui peut rendre un composant de rapport côté serveur dans Rails, générer son HTML et l'envoyer en tant que corps d'email.

**4. Rendu côté serveur avec un serveur Node :** Utiliser le rendu côté serveur en utilisant ReactDOMServer et le protocole de navigateur [headless](https://developers.google.com/web/updates/2017/04/headless-chrome) pour rendre HTML et JS et générer un PDF.

Maintenant, nous allons passer en revue les détails de chaque solution.

#### **Capture d'écran :**

C'était la solution la plus simple que nous avions et elle nécessite une entrée utilisateur. Un utilisateur doit être présent avec un système qui effectuera une capture d'écran en tant qu'image et l'attachera à l'email. Mais cela ne s'adapte pas à l'échelle. De plus, que faire si un utilisateur souhaite un rapport à une heure planifiée ou envoyé périodiquement ?

Exemple : Chaque semaine à 20h. Il n'est pas possible pour une personne de faire cela. Cela souffre également de l'incapacité à capturer entièrement une page défilante, nous avons donc dû abandonner cette idée.

#### **Bouton d'impression FrontEnd :**

Après avoir fait quelques recherches, nous avons découvert qu'il existe des extensions de navigateur disponibles qui produisent une image complète d'une page ouverte. Exemple : Full Page Screen Capture dans Chrome. Après avoir ajouté cette extension au navigateur, nous pourrions capturer n'importe quel écran au format image (png/jpg).

Encore une fois, cette solution ne nécessite aucun développement mais souffre de certains des problèmes précédents d'échelle et de planification. En même temps, nous aurions toujours besoin d'un utilisateur connecté au navigateur pour effectuer cette action, ce qui contredit l'objectif de la livraison par email.

#### **RubyGem :**

Nous avons rapidement réalisé que notre solution ne pouvait pas nécessiter d'interaction avec le navigateur. Nous devrions utiliser le [rendu côté serveur](https://alligator.io/react/server-side-rendering/). Nous avons donc commencé à explorer les Ruby Gems qui supportent le rendu côté serveur avec React. Nous avons exploré les Gems suivants

**3.1 [rails_react_stdio](https://github.com/aaronvb/rails_react_stdio) :**

Il est basé sur [react-stdio](https://github.com/ReactTraining/react-stdio) qui supporte le rendu côté serveur indépendamment de la technologie côté serveur. Il agit comme un binaire qui effectuera le travail de rendu des composants React. Pour rendre un composant React côté serveur, nous devons passer le chemin du fichier du composant React et les props si nécessaire. Il retournera une réponse JSON qui contiendra le code HTML du rapport. Ensuite, nous pouvons envoyer le contenu HTML par email.

En interne, cette gem utilise _popen3_ pour exécuter la commande de rendu. Mais cela signifie que le binaire _react-stdio_ doit être présent dans le conteneur Docker où notre application Rails est en cours d'exécution.

Ce n'est pas idéal du point de vue de la maintenabilité et de la reproductibilité. De plus, avoir un contenu HTML volumineux avec des graphiques peut être lent à charger, nous avons donc préféré une pièce jointe PDF. Pourtant, nous avons essayé.

Exemple : Pour rendre un rapport qui a le composant _TestComponent_ et le chemin de fichier _app/assets/javascripts/components/TestComponent.jsx_

Tout d'abord, inclure la gem dans le Gemfile :

```rb
gem 'rails_react_stdio', '~> 0.1.0'
```

Maintenant, à partir du planificateur d'email, appelez la méthode de la gem pour rendre le rapport et obtenir le HTML de la réponse. Ensuite, envoyez cette réponse par email.

```rb
email_body = RailsReactStdio::React.render('app/assets/javascripts/components/TestComponent.jsx', {city: "Pune"})
```

Nous avons essayé d'utiliser la méthode ci-dessus mais sans succès. De plus, le dépôt GitHub n'était pas activement maintenu, et tous ses cas de test échouaient. Nous avons donc décidé d'avancer sans cela.

**3.2 react-rails :**

La communauté ReactJS a construit cette gem. Elle utilise [ExecJS](https://github.com/rails/execjs) pour exécuter l'action de rendu d'un composant React côté serveur. Nous devons simplement passer un drapeau _'prerender': true_.

```js
<%= react_component('Dashboard', {name: 'Example'}, {prerender: true}) %>
```

Ce processus de pré-rendu n'a pas accès à la fenêtre ou au document, il ne charge donc pas JavaScript ou CSS en temps d'exécution. Nous utilisons également JQuery pour quelques choses, donc cela ne fonctionnerait pas non plus.

Il existe une alternative : cette gem a une autre classe pour le rendu côté serveur, _ExecJSRenderer_, qui aide à fournir JavaScript à un composant côté serveur.

La classe _ExecJSRenderer_ a 2 méthodes : _before_render_ et _after_render_, qui donnent accès au JavaScript requis avant et après le rendu du composant. Mais cela nécessiterait beaucoup de changements dans la base de code existante pour supporter le rendu côté serveur, dans chaque contrôleur. En dehors de cela, ExecJS ne fournit pas de sandboxing ainsi que des informations sur les erreurs d'exécution. Nous cherchions toujours quelque chose de mieux.

#### **Rendu côté serveur avec un serveur Node :**

La plupart des gems Ruby que nous avons explorées créaient en interne le serveur Node et rendaient React côté serveur. Au lieu d'utiliser Ruby, nous avons donc décidé d'utiliser directement le serveur Node et d'accomplir cette tâche nous-mêmes.

**4.1 Solution basée sur ReactDOMServer :**

Ici, nous utilisons [ReactDOMServer](https://reactjs.org/docs/react-dom-server.html). C'est la solution préférée pour le rendu côté serveur de l'équipe React. Nous avons créé un serveur Node qui appelle la méthode _renderToString()_ avec un composant React. Il retourne le contenu rendu que nous combinons avec HTML et envoyons par email.

Exemple :

```js
server.get('/', (req, res, next) => {
  /**
  * renderToString() prendra notre application React et la transformera en une chaîne
  * à insérer dans notre fonction de modèle Html.
  */
  console.log('démarré')
  const body = renderToString(<App />);
  const title = 'Rendu côté serveur des composants React';
  var result = Html({ body, title })
}
```

La méthode _renderToString()_ retourne une réponse de chaîne. Nous passons cette réponse à un modèle HTML et envoyons le modèle par email.

Lorsque nous avons testé cela, un email a été reçu comme prévu sauf que toutes les images utilisées dans le rapport étaient cassées. L'email n'a pas pu résoudre le chemin relatif de la source de l'image.

Pour obtenir les images correctes dans l'email, nous devrions soit

* Stocker les images dans S3 et utiliser l'URL de la source dans le rapport : Nous ajouterions maintenant les URL des images S3 dans l'email, et le serveur de messagerie chargerait directement les images depuis le serveur S3. Cela nécessiterait un espace cloud supplémentaire pour stocker les images, et le téléchargement depuis la destination nécessite un autre appel réseau depuis la boîte de réception de l'email.

Ou

* Envoyer le code base64 de l'image dans l'email : Au lieu de l'URL de l'image, nous pouvons envoyer le code base64 d'une image. Bien que cela augmente la charge utile du réseau, de nombreux serveurs de messagerie tels qu'Outlook et Gmail bloquent les images base64.

Nous devrions donc encore faire quelque chose à ce sujet.

**4.2 [Puppeteer](https://github.com/GoogleChrome/puppeteer) :**

Après avoir exploré les méthodes ci-dessus, nous avons découvert le service Puppeteer Headless Chrome. Puppeteer est une bibliothèque NodeJS de l'équipe Google Chrome, utilisée dans les tests de bout en bout. Par défaut, elle utilise le navigateur Chrome/Chromium pour la même chose. Essentiellement, elle simule toutes les actions qu'un utilisateur peut effectuer dans le navigateur. Exemple : Saisie clavier, événements de la souris, soumission de formulaire, etc.

Le résultat d'une requête puppeteer peut être une page HTML, une capture d'écran ou un PDF. Dans le cas de HTML, il rend la page complète côté serveur avec toutes les images, CSS et JavaScript. Ou un utilisateur peut rendre une page côté serveur et, si nécessaire, il peut générer une capture d'écran ou un PDF.

Si nous utilisons cette bibliothèque avec un serveur Node, nous pouvons planifier une tâche dans Sidekiq qui ferait une requête à ce serveur, rendrait un rapport et l'enverrait par email. Puppeteer dispose également d'un ensemble riche d'API qui supportent l'envoi d'en-têtes personnalisés dans la requête, ce qui nous aide à authentifier une requête en arrière-plan.

C'est exactement ce dont nous avions besoin !

**Ainsi, le cycle de vie global de la requête à l'intérieur de Puppeteer devrait ressembler à ceci :**

**1.** Il lance le navigateur

**2.** Crée une page sur le navigateur

**3.** Authentifie avec le serveur de l'application de rapport

**4.** Ouvre l'URL du rapport que l'utilisateur souhaite et retourne le contenu de la page rendue

**5.** En fonction des besoins de l'utilisateur, stocke le HTML de la page rendue ou prend une capture d'écran ou génère un PDF.

Nous pouvons utiliser soit le navigateur par défaut (téléchargé lorsque nous installons Puppeteer), soit nous pouvons spécifier une version spécifique du navigateur. Si nous spécifions une version spécifique du navigateur, nous devrons nous assurer que les API de Puppeteer sont compatibles avec le navigateur donné.

Tout ce qui précède peut être réalisé en suivant les étapes suivantes.

**1. Installer Puppeteer :**

Il télécharge le navigateur Chrome/Chromium par défaut. Donc, si nous voulons lancer le navigateur par défaut et installer Puppeteer :

```bash
npm install puppeteer
```

**2. Servir une requête :**

Construire un serveur qui recevra une requête et implémentera un cycle de vie de requête et retournera le résultat souhaité.

Voici l'extrait de code que nous utilisons pour générer un PDF d'une URL de page donnée.

```js
const puppeteer = require("puppeteer");
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.emulateMedia("screen");
await page.goto('https://www.google.com', {
      timeout: 30 * 1000, 
      waitUntil: "networkidle0"
});
await page.pdf(pdfOptions);
return page;
```

Comme nous l'avons déjà mentionné dans les étapes du cycle de vie ci-dessus, il lance d'abord le navigateur. Ensuite, il crée et ouvre une page dans le navigateur lancé. Ici, avec l'URL, nous avons passé les paramètres _timeout_ et _waitUntil_ qui sont donnés pour les raisons suivantes :

* _timeout_ : Si nous voulons restreindre le temps d'une requête, nous pouvons le passer à la variable timeout
* _waitUntil_ : si networkidle0 est donné, alors la prochaine requête ne sera pas servie tant que la requête actuelle n'est pas terminée.

À la fin, le contenu rendu sera passé à la méthode pdf et elle générera un pdf. Nous pouvons également fournir des options de formatage PDF comme la hauteur de la page, la largeur de la page, les en-têtes, les pieds de page et les marges.

De plus, nous avons appelé page.emulateMedia("screen"); qui applique le CSS à la page. Si nous n'ajoutons pas emulateMedia, notre PDF ne charge pas le CSS.

En dehors de ce que nous avons utilisé, il existe de nombreuses options de configuration différentes avec les API Puppeteer. Visitez la [documentation des API](https://github.com/GoogleChrome/puppeteer/blob/v1.12.2/docs/api.md#) pour plus d'informations.

Si vous avez trouvé cela utile ou si vous avez des suggestions, n'hésitez pas à les écrire dans les commentaires.

C'est tout pour aujourd'hui.