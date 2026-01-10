---
title: "Qu'est-ce que le Pr\x0E9-rendu et l'Hydratation en D\x0E9veloppement Web ?\
  \ Une Analyse Approfondie pour les D\x0E9veloppeurs"
subtitle: ''
author: Salvador Villalon Jr
co_authors: []
series: null
date: '2024-10-07T14:21:31.237Z'
originalURL: https://freecodecamp.org/news/what-are-pre-rendering-and-hydration-in-web-dev
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1727985850590/fdb7eb16-52bd-41ec-8e1a-e4fb9068a535.png
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: reactjs
- name: Next.js
  slug: nextjs
- name: hydration
  slug: hydration
- name: pre rendering
  slug: pre-rendering
- name: Web Development
  slug: web-development
- name: Full Stack Development
  slug: full-stack-development
seo_title: "Qu'est-ce que le Pr\x0E9-rendu et l'Hydratation en D\x0E9veloppement Web\
  \ ? Une Analyse Approfondie pour les D\x0E9veloppeurs"
seo_desc: 'Have you ever wondered how Frameworks like Next.js, Gatsby.js, and Remix
  work?

  These frameworks use the concepts of Pre-rendering and Hydration, which represent
  significant advancements in the history of web development.

  These frameworks leverage the...'
---

Vous ates-vous d9j0 demand9 comment des Frameworks comme [**Next.js**](https://nextjs.org/), [**Gatsby.js**](https://www.gatsbyjs.com/), et [**Remix**](https://remix.run/) fonctionnent ?

Ces frameworks utilisent les concepts de Pr9-rendu et d'Hydratation, qui repr9sentent des avanc9es significatives dans l'histoire du d9veloppement web.

Ces frameworks exploitent ces concepts pour cr9er des chaenes d'outils qui construisent des applications web efficaces. Dans cet article, nous allons discuter du Pr9-rendu et de l'Hydratation et pourquoi ils sont des fonctionnalit9s importantes 0 utiliser lors de la cr9ation d'applications monopage.

Pour comprendre ces concepts, nous devons explorer pourquoi ils ont 9t9 cr99s et quel probl8me ils essaient de r9soudre. Regardons le d9but des applications web.

## Table des Mati8res

1. [Le D9veloppement Web dans le Pass9 : Le Rendu C4t9 Serveur Traditionnel](#heading-le-developpement-web-dans-le-passe-le-rendu-cote-serveur-traditionnel)
    
    * [Les Inconv9nients du Rendu C4t9 Serveur Traditionnel](#heading-les-inconvenients-du-rendu-cote-serveur-traditionnel)
        
2. [Rendu C4t9 Serveur Traditionnel vs. Applications Monopage](#heading-rendu-cote-serveur-traditionnel-vs-applications-monopage)
    
    * [Qu'est-ce qu'une Application Monopage (SPA) ?](#heading-quest-ce-quune-application-monopage-spa)
        
    * [Flux d'une Application Monopage](#heading-flux-dune-application-monopage)
        
3. [Entrer dans un Nouveau Monde avec le Pr9-rendu et l'Hydratation](#heading-entrer-dans-un-nouveau-monde-avec-le-pre-rendu-et-lhydratation)
    
    * [Pourquoi le Pr9-rendu est-il Important ?](#heading-pourquoi-le-pre-rendu-est-il-important)
        
    * [Qu'est-ce que le Rendu C4t9 Serveur ?](#heading-quest-ce-que-le-rendu-cote-serveur)
        
    * [Qu'est-ce que la G9n9ration de Site Statique (SSG) ?](#heading-quest-ce-que-la-generation-de-site-statique)
        
    * [Qu'est-ce que l'Hydratation ?](#heading-quest-ce-que-lhydratation)
        
    * [Qu'est-ce que la R9conciliation ?](#heading-quest-ce-que-la-reconciliation)
        
    * [Le Pr9-rendu et l'Hydratation en Action](#heading-le-pre-rendu-et-lhydratation-en-action)
        
    * [Un Mod8le Mental pour l'Hydratation](#heading-un-modele-mental-pour-lhydratation)
        
    * [Erreurs Potentielles lors de l'Utilisation de Frameworks de Pr9-rendu et d'Hydratation](#heading-erreurs-potentielles-lors-de-lutilisation-de-frameworks-de-pre-rendu-et-dhydratation)
        
4. [Comment cela se rapporte-t-il aux frameworks comme Gatsby.js, Next.js, et Remix ?](#heading-comment-cela-se-rapporte-t-il-aux-frameworks-comme-gatsbyjs-nextjs-et-remix)
    
5. [Allons de l'Avant](#heading-allons-de-lavant)
    
6. [Conclusion](#heading-conclusion)
    

## Le D9veloppement Web dans le Pass9 : Le Rendu C4t9 Serveur Traditionnel

0 l'9poque du rendu c4t9 serveur traditionnel, le rendu et l'interactivit9 9taient s9par9s. Nous utilisions des langages c4t9 serveur comme [**Node.js**](https://nodejs.org/en), [**PHP**](https://www.php.net/), [**Java**](https://www.java.com/en/), et [**Ruby on Rails**](https://rubyonrails.org/).

Dans nos serveurs, nous cr9ions des **vues** en utilisant des langages de templating comme [**JSP**](https://en.wikipedia.org/wiki/Jakarta_Server_Pages) et [**EJS**](https://ejs.co/). Les vues sont des pages HTML, et vous pouviez y injecter du JavaScript ou du Java pour ajouter des fonctionnalit9s, des donn9es dynamiques r9cup9r9es 0 partir de requates de base de donn9es, et des segments interactifs avec des langages comme [**JQuery**](https://jquery.com/).

### Les Inconv9nients du Rendu C4t9 Serveur Traditionnel

1. **Probl8mes de Performance**
    

* Une requate au serveur devait atre effectu9e chaque fois que l'utilisateur demandait une page !
    
    * Cela signifiait qu'il y aurait un rechargement complet de la page.
        
    * Des requates complexes pouvaient r9sulter en des vitesses plus lentes.
        

2. **D9fis de Scalabilit9**
    

* **Port9e Mondiale** : Un **CDN Dynamique** 9tait n9cessaire pour mettre en cache vos fichiers dynamiques. Les CDN sont mieux adapt9s pour le contenu statique, mais des entreprises comme Cloudflare ont cr99 [**Cloudflare-Workers**](https://www.cloudflare.com/products/cloudflare-workers/) pour aider dans le processus.
    
* **Mont9e en Charge des Serveurs** : Si plus d'utilisateurs commen7aient 0 utiliser l'application, il y aurait une augmentation de la demande sur le serveur. Vous auriez peut-atre db investir davantage dans des ressources telles que la mont9e en charge en ajoutant plus de serveurs.
    

3. **Logique Dupliqu9e**
    

* Vous pourriez avoir du code dupliqu9. Par exemple, si vous essayiez de valider des champs de formulaire, vous deviez valider dans le fichier EJS et votre point de terminaison API.
    

Regardons l'extrait de code ci-dessous pour voir un exemple de cette logique dupliqu9e :

**Code en EJS :**

```javascript
<form action='/submit-form' method='POST' id="myForm">
    <label for="email">Email :</label>
    <input type="email" id="email" name="email" />
    <button type="submit">Soumettre</button>
</form>

<script>
    document
        .getElementById('myForm')
        .addEventListener('submit', function (event) {
            const email = document.getElementById('email').value;

            if (!email.includes('@')) {
                alert('Veuillez entrer un email valide.');
                event.preventDefault();
            }
        });
</script>
```

**Code en Express.js :**

```javascript
import express from "express";
const app = express();
const path = require("path");
const port = 3000;

// Pour recevoir les donn9es du formulaire
app.use(
  express.urlencoded({
    extended: true,
  }),
);

// Configuration du moteur de vue. Besoin d'un dossier appel9 views
app.set("views", path.join(__dirname, "views"));
app.set("view engine", "ejs");

app.get("/", (req, res) => {
  // Pour rendre la vue
  res.render("index", { errors: null });
});

app.post("/submit-form", (req, res) => {
  const email = req.body.email;

  if (!email.includes("@")) {
    res.status(400).send("Email invalide.");
    return;
  }
  // Poursuivre le traitement du formulaire
});

app.listen(port, () => {
  console.log(`Sandbox 9coutant sur le port ${port}`);
});
```

Le rendu c4t9 serveur traditionnel avait des inconv9nients significatifs, mais l'introduction des **applications monopage** a marqu9 une nouvelle 8re dans le d9veloppement web.

## Rendu C4t9 Serveur Traditionnel vs. Applications Monopage

### Qu'est-ce qu'une Application Monopage (SPA) ?

> ***Une application monopage (SPA) est une impl9mentation d'application web qui charge un seul document web et met ensuite 0 jour le contenu du corps de ce document unique via des API JavaScript telles que Fetch lorsque diff9rents contenus doivent atre affich9s. Permet aux utilisateurs d'utiliser des sites web sans charger de nouvelles pages compl8tes depuis le serveur. (***[***Source : MDN***](https://developer.mozilla.org/en-US/docs/Glossary/SPA)***)***

Une fa7on populaire d'impl9menter une SPA est d'utiliser React. React vous permet de cr9er des applications rapides et simplifie la mise 0 jour de l'UI plus facilement que les m9thodes de manipulation du DOM.

Il offre plusieurs avantages :

* **Exp9rience Utilisateur Am9lior9e**
    
    * Une SPA charge un seul fichier HTML et met dynamiquement 0 jour le contenu au fur et 0 mesure que l'utilisateur interagit avec lui. Tout cela est fait sans rechargement complet de la page.
        
    * Une SPA peut mettre 0 jour l'9tat de l'UI facilement et fournir un retour instantan9 aux utilisateurs en fonction des actions effectu9es sur l'application.
        
* **Charge Serveur R9duite**
    
    * La plupart du travail est effectu9 par le navigateur. Cela r9duit la charge sur le serveur !
        
* **Meilleure Scalabilit9**
    
    * Le navigateur effectue maintenant la plupart du travail. Nous pouvons maintenant d9ployer des serveurs d9di9s ax9s sur le service de donn9es via des API. Nous pouvons facilement 9voluer horizontalement. Nous avons l'option d'utiliser des serveurs ou des fonctions serverless comme [**AWS lambda**](https://aws.amazon.com/lambda/).
        
    * Une SPA peut atre h9berg9e sur un CDN statique comme [**Netlify**](https://docs.netlify.com/platform/what-is-netlify/).
        

Avec l'ajout de chaenes d'outils comme [**Vite**](https://vitejs.dev/) et [**Create React App**](https://create-react-app.dev/) pour automatiser la configuration d'une application JavaScript moderne, les ing9nieurs n'avaient plus 0 se soucier de la configuration manuelle de Webpack.

Il y a quelques inconv9nients 0 impl9menter des SPA. Le principal est qu'il d9pend du navigateur pour charger tout le JavaScript et le HTML pour nous. Cela signifie que sur les appareils mobiles et pour les personnes avec une connexion internet lente, les utilisateurs peuvent rencontrer des retards dans l'affichage de la page. Examinons le flux pour expliquer cela :

### Flux d'une Application Monopage

> ![Flux d'une Application Monopage React. (Source : Comment NextJS fonctionne REELLEMENT : https://youtu.be/d2yNsZd5PMs?si=RmnywZJEAuurseQm)](https://cdn.hashnode.com/res/hashnode/image/upload/v1725392287290/04dba828-9903-4ca6-bf8e-0c0d875d587b.png?auto=compress,format&format=webp align="left")

Plusieurs 9tapes sont n9cessaires pour que les utilisateurs voient enfin la page HTML.

Tout d'abord, le navigateur r9cup8re le HTML. Ce HTML initial sera vide et incorrect. Pourquoi ? Parce que le contenu provient de JavaScript. Cela signifie qu'il faut du temps au navigateur pour r9cup9rer JavaScript, le charger et l'ex9cuter. Comme le HTML initial est incorrect, les robots d'indexation et les moteurs de recherche ne trouveront pas de contenu pertinent sur le site web et l'ignoreront.

Regardez le GIF ci-dessous. Ici, JavaScript est d9sactiv9 dans les outils de d9veloppement Chrome. Le site web 9choue 0 se charger sans JavaScript. Si JavaScript est activ9 mais que la connexion internet est lente, les utilisateurs peuvent voir une page blanche pendant une p9riode prolong9e.

![Test de l'Application Monopage avec JavaScript D9sactiv9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725392877108/d5a2eb1c-f784-4879-b02f-8c340d405c9c.gif?auto=format,compress&gif-q=60&format=webm align="left")

C'9tait un gros probl8me. Cela a conduit le d9veloppement web 0 9voluer vers **l'8re du pr9-rendu**.

## Entrer dans un Nouveau Monde avec le Pr9-rendu et l'Hydratation

### Pourquoi le Pr9-rendu est-il Important ?

Les gens ont r9alis9 que nous pouvions g9n9rer le HTML 0 l'avance. Il pouvait atre g9n9r9 depuis notre serveur ou au moment de la construction, selon les m9thodes utilis9es.

Le pr9-rendu peut atre effectu9 de deux mani8res - [**Server Side Rendering (SSR)**](https://nextjs.org/docs/pages/building-your-application/rendering/server-side-rendering) ou [**Static Site Generation (SSG)**](https://nextjs.org/docs/pages/building-your-application/rendering/static-site-generation)

### Qu'est-ce que le Rendu C4t9 Serveur ?

Les composants React sont rendus sur le serveur, et le HTML r9sultant est envoy9 au navigateur. Cela peut am9liorer le SEO et les temps de chargement initiaux. **Le processus de rendu se produit 0 chaque requate de page.**

### Qu'est-ce que la G9n9ration de Site Statique (SSG) ?

**Des pages HTML statiques sont g9n9r9es au moment de la construction.** Ces pages peuvent atre servies rapidement sans n9cessiter un serveur pour les rendre 0 la vol9e.

L'une ou l'autre m9thode est b9n9fique ! **Maintenant, le HTML que l'utilisateur re7oit sera correct.** Ils verront une page avec du contenu au lieu d'une page blanche comme vu en utilisant Vite ou Create React App.

Mais il y a un probl8me : le HTML que l'utilisateur re7oit n'est pas interactif. Ils ne peuvent pas cliquer dessus ou soumettre un formulaire. Comment pouvons-nous ajouter de l'interactivit9 0 notre application ? En hydratant correctement 🛰 🌊 !

### Qu'est-ce que l'Hydratation ?

[**Hydratation**](https://react.dev/reference/react-dom/hydrate#hydrating-server-rendered-html) est ce qui ajoute de l'interactivit9 0 notre application. Elle charge le JavaScript qui rend notre application interactive.

> ***Dans React, "l'hydratation" est la fa7on dont React "attache" le HTML existant qui a d9j0 9t9 rendu par React dans un environnement serveur. Pendant l'hydratation, React va tenter d'attacher des 9couteurs d'9v9nements au balisage existant et prendre en charge le rendu de l'application sur le client. (***[***Source : Documentation React***](https://react.dev/reference/react-dom/hydrate#hydrating-server-rendered-html)***)***

Voyons 0 quoi ressemble le flux pour une application qui utilise le pr9-rendu et l'hydratation :

![Flux de pr9-rendu.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725392958385/eaee78cb-736c-4d49-8fb7-c9cb098d3652.png?auto=compress,format&format=webp align="left")

### **Qu'est-ce que la R9conciliation ?**

> ***La r9conciliation est le processus par lequel React d9termine la mani8re la plus efficace de mettre 0 jour l'UI en r9ponse aux changements de donn9es ou de hi9rarchie des composants. (Source :*** [***Quelle est la diff9rence entre le DOM virtuel et le DOM r9el (React) ?***](https://www.educative.io/answers/what-is-the-concept-of-reconciliation-in-react)***)***

La r9conciliation est le processus par lequel React d9termine comment mettre 0 jour l'UI en r9ponse aux changements de donn9es ou de hi9rarchie des composants.

Lorsque les composants sont rendus, un DOM virtuel est cr99. Si des changements d'9tat ou de props se produisent, un nouveau DOM virtuel est cr99. React utilise ensuite son algorithme de diff pour comparer le nouveau DOM virtuel avec le DOM virtuel pr9c9dent afin de v9rifier les changements. C'est la **r9conciliation**.

En fonction des changements trouv9s, **React ne va pas mettre 0 jour l'ensemble de l'UI**. Au lieu de cela, il va **s9lectionner les 9l9ments qui doivent atre mis 0 jour**. Cet [**article**](https://www.educative.io/answers/what-is-the-concept-of-reconciliation-in-react) m'a aid9 0 comprendre la r9conciliation.

### **Le Pr9-rendu et l'Hydratation en Action**

Pendant le flux de pr9-rendu et d'hydratation, l'utilisateur verra d'abord le HTML avec le contenu correct.

Ensuite, l'hydratation entre en jeu et charge JavaScript pour donner de l'interactivit9 0 l'application.

Simulons le processus de ce qui se passe si le processus d'hydratation prend beaucoup de temps (en raison d'une connexion internet lente) ou si l'utilisateur a d9sactiv9 JavaScript.

Voici un gif o9 j'ai d9sactiv9 JavaScript sur mon Portfolio. J'ai cr99 mon portfolio en utilisant [**Gatsby**](https://www.gatsbyjs.com/), un framework de g9n9ration de site statique (il a 9galement des capacit9s de rendu c4t9 serveur) :

![Test du Portfolio avec JavaScript D9sactiv9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725554638438/698fd854-e828-44cd-996a-e01b154803d1.gif?auto=format,compress&gif-q=60&format=webm align="left")

Mame s'il n'y a pas de JavaScript, je peux toujours voir le contenu sur mon portfolio. C'est parce que l'utilisateur a re7u du **HTML pr9-rendu** ! Vous pouvez voir que je ne peux pas cliquer sur les **9l9ments du menu d9roulant ou les boutons** qui disent 0 propos de moi, Projets et Exp9rience. C'est parce que le JavaScript ne s'est pas charg9, donc l'utilisateur ne peut pas interagir avec.

### **Un Mod8le Mental pour l'Hydratation**

[**Josh Comeau**](https://www.joshwcomeau.com/) a cr99 un mod8le mental cool pour l'hydratation. Josh l'appelle le **
bDeux Passes de Rendu.b**

> ***La premi8re passe, au moment de la compilation, produit tout le contenu non personnel statique et laisse des trous o9 le contenu dynamique ira. Ensuite, apr8s que l'application React a 9t9 mont9e sur l'appareil de l'utilisateur, une deuxi8me passe comble toutes les parties dynamiques qui d9pendent de l'9tat du client. (Source :*** [***Les P9rils de l'Hydratation***](https://www.joshwcomeau.com/react/the-perils-of-rehydration/#mental-models-13)***)***

Pour r9sumer :

1. **La Premi8re Passe** : l'utilisateur voit le HTML pr9-rendu. Il contient du contenu statique, mais il manque le contenu dynamique.
    
2. **La Deuxi8me Passe** : JavaScript commence 0 se charger et comble les pi8ces dynamiques manquantes qui d9pendent de l'9tat du client.
    

### **Erreurs Potentielles lors de l'Utilisation de Frameworks de Pr9-rendu et d'Hydratation**

Lors de l'utilisation de frameworks comme Next.js, le serveur retournera du HTML pr9-rendu statique, puis l'hydratation se produira, ce qui chargera JavaScript.

Mais nous devons atre prudents lors de l'utilisation de donn9es dynamiques et de propri9t9s exclusives au client. Par exemple, regardez ce code :

#### Erreur de Donn9es Dynamiques

```javascript
function HydrationErrors() {
  return (
    <>
      <h1>Erreurs d'Hydratation</h1>

      <div>
        <p>Aujourd'hui, la date en millisecondes est {new Date().getTime()}</p>
      </div>
    </>
  );
}
```

Ici, le serveur g9n9rera du HTML avec un horodatage en millisecondes. Par exemple : `1724869161034`. Le processus d'hydratation commence, puis le client charge le HTML. Le temps a pass9 et l'horodatage est diff9rent, il est maintenant `172486193750` ! Ce sc9nario provoque l'erreur suivante :

![Inad9quation du contenu textuel entre le serveur et l'hydratation du client.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725555403697/ebb398ec-cd58-4b9a-aa63-c43a9b511eeb.png?auto=compress,format&format=webp align="left")

Cela se produit parce que la fonction `getTime()` g9n9rera un horodatage diff9rent.

Cela signifie que le serveur et le client g9n8rent du HTML diff9rent. L'onglet R9seau nous montre la r9ponse du serveur. C'est un HTML diff9rent de ce que le client charge.

**La r9ponse du serveur ci-dessous :**

![Diff9rent HTML du serveur g9n9r9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725555472118/d76c7ad0-92ab-4b77-92ea-b3d9d6a3b4fe.png?auto=compress,format&format=webp align="left")

**La r9ponse du client ci-dessous :**

![Diff9rent HTML du client g9n9r9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725555518535/af27855d-d362-44e3-8007-b01fde1d2455.png?auto=compress,format&format=webp align="left")

**Pour corriger l'erreur :**

```javascript
function HydrationErrors() {
  const [date, setDate] = useState<number>();

  useEffect(() => {
    setDate(new Date().getTime());
  }, []);

  return (
    <>
      <h1>Erreurs d'Hydratation</h1>

      <div>
        <p>Aujourd'hui, la date en millisecondes est {date}</p>
      </div>
    </>
  );
}
```

Vous pouvez utiliser le hook `useEffect`. Pourquoi cela fonctionnerait-il ? Parce que le HTML que le serveur et le client rendent contiendra une variable d'9tat `date` vide.

Une fois le composant mont9, le `useEffect` s'active et ajoute les donn9es dynamiques de la variable d'9tat ou vous pouvez utiliser le drapeau `suppressHydrationWarning` et le d9finir sur vrai.

```javascript
  <p suppressHydrationWarning={true}>Aujourd'hui, la date en millisecondes est {date}</p>
```

#### Utilisation des Propri9t9s Exclusives au Client

Rappelez-vous que vous ne pouvez pas utiliser `window` ou `localStorage`. Ils n'existent pas sur le serveur. Prenez l'exemple suivant :

```javascript
function HydrationErrors() {
  return (
    <>
      <div>
        {typeof window !== "undefined" && <p>Cette balise p apparaetra</p>}
      </div>
    </>
  );
}
```

Ici, le serveur retourne un HTML avec une balise `<div>` vide, mais le client charge un HTML qui inclut la balise `<p>`. Cela cr9e une **ERREUR D'HYDRATATION !**

C'est l'erreur que vous obtenez :

![Impossible d'utiliser les propri9t9s c4t9 client erreur d'hydratation.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725555844562/443c435c-308a-4422-b184-b2f321672519.png?auto=compress,format&format=webp align="left")

L'onglet R9seau nous montre la r9ponse du serveur. C'est une balise `<div>` vide.

**La r9ponse du serveur ci-dessous :**

![Diff9rent HTML du serveur g9n9r9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725555958286/aeeaa522-3266-4b60-856d-d0cd3bf4d9c9.png?auto=compress,format&format=webp align="left")

Mais le client charge un HTML qui dit "Cette balise p apparaetra".

**La r9ponse du client ci-dessous :**

![Diff9rent HTML du client g9n9r9.](https://cdn.hashnode.com/res/hashnode/image/upload/v1725556187527/173bf82a-1754-4835-9921-adea0f2e864a.png?auto=compress,format&format=webp align="left")

Cette d9mo a 9t9 inspir9e par [**Deeecode The Web**](https://www.youtube.com/@deeecode) dans [**Pourquoi les ERREURS D'HYDRATATION existent-elles ? Et comment les r9soudre**](https://youtu.be/7UOyuEHYmSE?si=Ql8z5D_pAryvTyFf). Il donne une excellente explication de pourquoi les erreurs d'hydratation se produisent. Je recommande de le regarder !

## Comment cela se rapporte-t-il aux frameworks comme Gatsby.js, Next.js, et Remix ?

Tout ce dont nous avons discut9 est ce sur quoi tous ces frameworks se concentrent.

La g9n9ration de site statique et le rendu c4t9 serveur peuvent atre impl9ment9s en utilisant Gatsby.js, Next.js, et Remix. Ils se concentrent sur la cr9ation d'un HTML pr9-rendu prat 0 atre vu par l'utilisateur, puis initient l'hydratation pour ajouter de l'interactivit9 0 l'application.

Gatsby.js, Next.js, et Remix ne remplacent pas le concept des applications monopage  ils ajoutent au processus. Regardez ce flux :

> ![Flux combin9 de pr9-rendu et d'application monopage. (Source : Comment NextJS fonctionne REELLEMENT)](https://cdn.hashnode.com/res/hashnode/image/upload/v1725556321232/7d8629fd-b528-4cd7-9bc2-7de0bf1ab630.png?auto=compress,format&format=webp align="left")

Cela ajoute au flux actuel de l'application monopage ! Si vous n'aviez pas de pr9-rendu, le processus commence o9 la boete rose commence, avec un HTML incomplet.

## Allons de l'Avant

Cet article est destin9 0 atre une introduction au pr9-rendu et 0 l'hydratation.

Next.js a d'abord impl9ment9 ces concepts avec le [Pages Router](https://nextjs.org/docs/pages). Pages Router 9tait g9nial et a introduit le monde aux fonctions comme `getServerSideProps`, `getStaticPaths`, et `getStaticProps` pour impl9menter la g9n9ration de site statique et le rendu c4t9 serveur.

Ces impl9mentations avaient leurs avantages et inconv9nients. Par exemple, Josh W Comeau a mentionn9 que avec `getServerSideProps` :

> 1. Cette strat9gie ne fonctionne qu'au niveau de la route, pour les composants tout en haut de l'arbre. Nous ne pouvons pas faire cela dans n'importe quel composant.
>     
> 2. Chaque m9ta-framework a invent9 sa propre approche. Next.js a une approche, Gatsby en a une autre, Remix en a une autre encore. Cela n'a pas 9t9 standardis9.
>     
> 3. Tous nos composants React vont *toujours* s'hydrater sur le client, mame lorsqu'il n'est pas n9cessaire pour eux de le faire.
>     
>     [(Source : Comprendre les Composants Serveur React)](https://www.joshwcomeau.com/react/server-components/)
>     

L'9quipe React a vu cela aussi et a cr99 un nouveau paradigme appel9 [React Server Components (RSC)](https://react.dev/reference/rsc/server-components). Pour impl9menter RSC, l'9quipe Vercel a cr99 le [App Router](https://nextjs.org/docs/app). App Router utilise toujours les concepts de pr9-rendu et d'hydratation, mais il n'utilise plus `getStaticProps`, `getStaticPaths`, et `getServerSideProps`. Il utilise RSC et d'autres grandes fonctionnalit9s d'App Router pour impl9menter de meilleures applications web. Je recommande de jeter un 9il 0 App Router lorsque vous en aurez l'occasion.

## Conclusion

Merci d'avoir lu jusqu'ici 😃 !

J'ai beaucoup appris en 9crivant cet article. J'ai commenc9 cette recherche parce que j'ai utilis9 Gatsby pour cr9er mon [**portfolio version 4**](https://salvador-villalon.netlify.app/) et Next.js dans mon travail, mais je ne comprenais pas les concepts derri8re ces frameworks et pourquoi ils avaient 9t9 cr99s.

J'ai cr99 une application web pour d9montrer les sujets abord9s dans l'article.

* Application : [**https://the-nextjs-pagesrouter-guide.vercel.app/**](https://the-nextjs-pagesrouter-guide.vercel.app/)
    
* D9p4t GitHub : [**https://github.com/salvillalon45/the-nextjs-pagesrouter-guide**](https://github.com/salvillalon45/the-nextjs-pagesrouter-guide)
    

Dans le d9p4t GitHub, vous pouvez trouver les extraits de code pour les 9l9ments suivants :

* Une page impl9mentant getStaticProps et getStaticPaths
    
* Une page impl9mentant getStaticProps
    
* Une page impl9mentant getServerSideProps avec une r9cup9ration c4t9 client
    
* Une page pour d9montrer les erreurs d'hydratation
    
* Utilisation du r9pertoire API pour impl9menter nos propres routes API
    

### Ressources

Voici quelques ressources d'apprentissage cl9 que j'ai utilis9es pour 9crire cet article au cas o9 vous souhaiteriez approfondir :

* [**Qu'est-ce que l'Hydratation**](https://youtu.be/R-BKadZWYnQ?si=imNFJL36knSPdF7S)** ?** par Builder
    
* [**Qu'est-ce que l'HYDRATATION REACT exactement ? Et pourquoi est-ce important ?**](https://youtu.be/87i0pejrULw?si=e179x9x2KkaR8AxL) par Deeecode The Web
    
* [**Comment NextJS fonctionne REELLEMENT**](https://youtu.be/d2yNsZd5PMs?si=UZYKHUrajdXQd1y4&t=1) par Theo Browne
    
* [**Next.js - GetServerSideProps vs GetStaticProps**](https://youtu.be/xfX8nVpaycU?si=ZV-r2piDoWhLAKMi) par Morado Web Development