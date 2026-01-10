---
title: Comment configurer une passerelle de paiement dans Next.js et React avec Razorpay
  et TailwindCSS
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-12-21T18:16:10.000Z'
originalURL: https://freecodecamp.org/news/integrate-a-payment-gateway-in-next-js-and-react-with-razorpay-and-tailwindcss
coverImage: https://www.freecodecamp.org/news/content/images/2021/12/Blue-and-White-Modern-Corporate-Travel-YouTube-Thumbnail.png
tags:
- name: ecommerce
  slug: ecommerce
- name: Next.js
  slug: nextjs
- name: payments
  slug: payments
- name: React
  slug: react
- name: tailwind
  slug: tailwind
seo_title: Comment configurer une passerelle de paiement dans Next.js et React avec
  Razorpay et TailwindCSS
seo_desc: "By Manu Arora\nIf you have an e-commerce application, a payment gateway\
  \ lets you process payments on your website on the fly. \nWith all the modern payment\
  \ gateway solutions available these days, there are many ways you can integrate\
  \ payments and charg..."
---

Par Manu Arora

Si vous avez une application d'e-commerce, une passerelle de paiement vous permet de traiter les paiements sur votre site web à la volée. 

Avec toutes les solutions de passerelle de paiement modernes disponibles de nos jours, il existe de nombreuses façons d'intégrer les paiements et de facturer vos utilisateurs pour vos produits ou services.  
  
Dans ce tutoriel, nous allons construire une page d'accueil qui permet à l'utilisateur final d'acheter des produits à partir d'une application web. La page ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-20-at-10.54.31-PM.png)

Démo en direct : [Intégrer les paiements](https://integrate-payments.vercel.app)
Code source : [Code source d'Intégrer les paiements](https://github.com/manuarora700/integrate-payments.git)

Certaines des passerelles de paiement populaires disponibles sont :

- [Stripe](https://stripe.com)
- [Gumroad](https://gumroad.com)
- [PayPal](https://paypal.com)
- [Razorpay](https://razorpay.com)

Aujourd'hui, nous allons apprendre à intégrer Razorpay avec une application Next.js (React) et comprendre comment le flux fonctionne réellement.

## **Stack technique**

Pour notre Stack, nous allons utiliser les technologies suivantes :

- [Next.js](https://nextjs.org) - Un Framework pour React qui donne accès aux fonctions serverless et à l'architecture React.
- [TailwindCSS](https://tailwindcss.com) - Un Framework CSS basé sur des utilitaires pour un stylisage facile.
- [Razorpay](https://razorpay.com) - Un système de passerelle de paiement qui permet aux utilisateurs d'accéder aux paiements.
- [Vercel](https://vercel.com) - Pour l'hébergement de notre application Next.js (si elle n'est pas déjà hébergée).
- [Tailwind Master Kit](https://tailwindmasterkit.com) - Pour des composants Tailwind facilement accessibles.

## **Configuration du projet**

Si vous avez déjà un projet, vous pouvez passer directement à la partie intégration de l'article. Sinon, commençons par créer un dépôt Git et héberger notre projet sur Vercel.

### **Comment configurer un dépôt et un site web Next.js**

Tout d'abord, rendez-vous sur [Vercel](https://vercel.com) et créez-vous un compte hobby. (Si vous comptez l'utiliser pour un projet commercial, assurez-vous d'acheter leur forfait. Les comptes Hobby sont uniquement destinés aux tests et à la création d'environnements de test.)

Une fois le compte créé, cliquez sur `New Project`.
![Screenshot-2021-12-21-at-11.56.47-AM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-11.56.47-AM.png)

Ensuite, sélectionnez `Next.js` parmi les options disponibles et créez un dépôt Git sur la plateforme elle-même.
![Screenshot-2021-12-21-at-11.57.31-AM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-11.57.31-AM.png)

Votre site sera déployé en quelques secondes et vous obtiendrez une URL pour le site web en direct.

### **Comment configurer TailwindCSS**

Maintenant que le site web est configuré, vous pouvez aller directement sur [GitHub](https://github.com), cloner le dépôt, pour l'exécuter dans votre environnement local. Pour cela, suivez ces étapes simples :

- Allez sur [GitHub](https://github.com) et trouvez votre dépôt nouvellement créé.
- Cliquez sur la section `code` et copiez l'URL du dépôt.
- Ouvrez votre terminal sur le bureau et écrivez `git clone <nom_du_depot>`. Cela clonera le dépôt dans votre environnement local afin que vous puissiez commencer à travailler.
- Une fois le dépôt cloné/copié dans votre environnement local, ouvrez le projet dans votre éditeur de code préféré (VSCode est le meilleur à mon avis).
- Dans le terminal, ouvrez l'emplacement de l'application et écrivez `npm install`. Cela installera tous les modules node associés.
- Vous pouvez démarrer le serveur de développement local en écrivant `npm run dev`.

Maintenant, le projet est opérationnel dans votre environnement local. Pour accéder à votre site web localement, ouvrez `localhost:3000` dans votre navigateur et vous pourrez voir le site web de base déjà présent.  
  
Configurer Tailwind est très simple. Leur [documentation](https://tailwindcss.com/docs/guides/nextjs) le rend encore plus simple. Consultez leur doc pour plus de références sur TailwindCSS en tant que Framework.  
  
Pour configurer Tailwind sur votre environnement local, suivez les étapes ci-dessous :

- `npm install -D tailwindcss postcss autoprefixer` - Cela installera TailwindCSS ainsi que d'autres dépendances importantes pour la compilation et l'exécution de votre code Tailwind.
- `npx tailwindcss init -p` - Cela initialisera un fichier `tailwind.config.js` qui est simplement un objet pouvant être manipulé selon les besoins de l'utilisateur.
- Dans le fichier `tailwind.config.js`, collez le code ci-dessous qui indique essentiellement à Tailwind de compiler le code présent dans les répertoires `/pages` et `/components`.

```js
module.exports = {
  content: [
    "./pages/**/*.{js,ts,jsx,tsx}",
    "./components/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
- Ouvrez le fichier `globals.css` présent dans le répertoire `/styles` et collez le code suivant. Ces extraits de code importent tout le code de configuration lié à Tailwind :
```css
@tailwind base;
@tailwind components;
@tailwind utilities;
```
- Redémarrez votre site web en quittant le terminal et en écrivant `npm run dev` dans le terminal. Vous êtes maintenant prêt à exploiter la puissance de TailwindCSS.

Maintenant que Tailwind et notre site web sont configurés, passons directement au développement de la page et à l'intégration des paiements.

## **Développement de la page d'accueil**

La page d'accueil que nous allons utiliser est directement tirée du [Tailwind Master Kit](https://tailwindmasterkit.com) qui vous permet d'accéder à des composants construits avec TailwindCSS.

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-12.13.56-PM.png)

Décomposons le code pour mieux le comprendre.

### **Navbar.js**

```js
import React from "react";
export const Navbar = () => {
  return (
    <div className="flex flex-row items-center  justify-between px-20 py-10">
      <div className="flex flex-row items-center">
        <h1 className="font-bold italic text-2xl text-white mr-10">Payments</h1>
        <ul className="flex flex-row space-x-10">
          <li>
            <a
              href="#"
              className="text-gray-400 text-sm tracking-wide font-light"
            >
              Tarification
            </a>
          </li>
          <li>
            <a
              href="#"
              className="text-gray-400 text-sm tracking-wide font-light"
            >
              Produit
            </a>
          </li>
          <li>
            <a
              href="#"
              className="text-gray-400 text-sm tracking-wide font-light"
            >
              Équipe
            </a>
          </li>
          <li>
            <a
              href="#"
              className="text-gray-400 text-sm tracking-wide font-light"
            >
              Ventes
            </a>
          </li>
        </ul>
      </div>
      <div className="flex flex-row space-x-10 items-center">
        <a href="#" className="text-gray-400 text-sm tracking-wide font-light">
          Ventes
        </a>
        <button className="bg-[#272A30] text-gray-300 px-8 text-sm py-2 rounded-md shadow-xl drop-shadow-2xl">
          Se connecter
        </button>
      </div>
    </div>
  );
};

```

Construire la Navbar est simple. C'est un conteneur Flexbox avec des liens et des éléments de liste non ordonnée alignés en ligne (`row`). 

Le bouton, cependant, est intéressant. Il utilise la nouvelle classe d'ombre portée (drop shadow) de TailwindCSS qui projette une ombre en arrière-plan. (Nous pouvons également utiliser des ombres colorées dans les versions 3.0+ de TailwindCSS - c'est plutôt cool.)

### **Hero.js**

```js
const Hero = ({ onClick }) => {
  return (
    <div className="relative z-10 flex flex-col md:flex-row mt-10 items-center  max-w-6xl justify-evenly mx-auto">
      <div className="md:w-1/3 mb-20 md:mb-0 mx-10">
        <h1 className=" text-white font-bold text-5xl mb-10">
          Intégrez{" "}
          <span className="bg-clip-text text-transparent bg-gradient-to-r from-pink-500 to-violet-500">
            les paiements
          </span>{" "}
          en moins de 10 minutes.
        </h1>
        <p className="text-sm text-gray-300 font-light tracking-wide w-[300px] mb-10">
          Apprenez à intégrer une passerelle de paiement avec votre application Next.js et React.
        </p>
        <div className="bg-gradient-to-r from-[#3e4044] to-[#1D2328] p-[1px] rounded-md mb-4">
          <button
            onClick={onClick}
            className="bg-gradient-to-r from-[#2E3137] to-[#1D2328] rounded-md w-full py-4 shadow-xl drop-shadow-2xl text-gray-300 font-bold"
          >
            Acheter maintenant !
          </button>
        </div>
        <div className="bg-gradient-to-r from-[#3e4044] to-[#1D2328] p-[1px] rounded-md">
          <button className="bg-gradient-to-r from-[#1D2328] to-[#1D2328] rounded-md w-full py-4 shadow-sm drop-shadow-sm text-gray-400 font-light">
            Lire le blog
          </button>
        </div>
      </div>
      {/* <div className="w-2/3 bg-white flex-shrink-0  relative"> */}
      <img
        className="w-full md:w-[36rem] h-full"
        alt="paiement stripe de undraw"
        src="/payments.svg"
      />
      {/* </div> */}
    </div>
  );
};
```

La section hero contient notre bouton `Acheter maintenant` qui initialisera les paiements pour nous (nous verrons l'implémentation dans la section suivante).

La mise en page contient deux sections : la `section de gauche` contient tout le texte et la `section de droite` contient une grande image (tirée d'Undraw, un site web d'illustrations gratuit et open source). 

L'action `onClick` sur le bouton est importante car elle est responsable du déclenchement de l'action qui initialisera les paiements. Le `onClick` n'est rien d'autre qu'un `callback` qui appelle la fonction passée en tant que prop au composant.  
  
C'est à peu près tout pour la partie UI. Plongeons dans la section des paiements et comprenons comment configurer un compte développeur sur Razorpay et utiliser leur SDK pour effectuer des paiements sur notre site web.

## Comment configurer un compte Razorpay et récupérer les clés API

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-12.25.43-PM.png)

Pour intégrer les paiements (c'est-à-dire recevoir des paiements sur notre site web), nous avons besoin de deux choses :

1. Un compte Razorpay
2. Un ensemble de clés API qui nous permet d'accéder à leurs services.

Créons un compte et récupérons les clés API.

- Rendez-vous sur [Razorpay](https://razorpay.com) et inscrivez-vous pour un compte.
- Après l'inscription, vous pouvez accéder au [Tableau de bord](https://dashboard.razorpay.com/app/dashboard) où vous trouverez tous les détails nécessaires pour intégrer les paiements.
![Screenshot-2021-12-21-at-12.28.44-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-12.28.44-PM.png)
- Pour l'instant, nous serons en mode Test afin de pouvoir tester nos paiements avant de passer réellement en direct.
- Dans le panneau de gauche, faites défiler jusqu'à `Settings` - Vous y trouverez la section des clés API ainsi que les configurations que vous pouvez apporter à l'interface utilisateur de vos paiements.
![Screenshot-2021-12-21-at-12.30.10-PM](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-12.30.10-PM.png)
- Comme vous le ferez pour la première fois, cliquez sur `Generate API Keys` et le téléchargement commencera automatiquement. Le fichier téléchargé contient la `Razorpay API Key` et le `Razorpay API Secret`.

Vous êtes maintenant prêt avec les clés API et la configuration de la plateforme. Voyons directement comment déclencher l'API Razorpay et effectuer des paiements.

## **Comment intégrer les paiements avec Razorpay**

Pour que nos paiements soient intégrés, nous avons besoin d'un clic sur un bouton qui initialise réellement le module de `checkout` de Razorpay. Pour cela, nous avons déjà un bouton `Acheter maintenant` qui appelle une fonction `onClick` qui n'est rien d'autre qu'un callback. Voyons l'implémentation réelle et comprenons le code qui se cache derrière.

Pour initialiser un paiement, nous devons ajouter le script `checkout` de Razorpay dans notre code. Dans React, nous pouvons simplement le faire en utilisant le code `document.body.appendChild(script)`.

### **initializeRazorpay()**

```js
const initializeRazorpay = () => {
    return new Promise((resolve) => {
      const script = document.createElement("script");
      script.src = "https://checkout.razorpay.com/v1/checkout.js";

      script.onload = () => {
        resolve(true);
      };
      script.onerror = () => {
        resolve(false);
      };

      document.body.appendChild(script);
    });
  };
```

Ici, nous utilisons une promesse pour accomplir cette tâche. Nous faisons cela parce que plus tard, nous allons utiliser `initializeRazorpay()` de telle sorte que chaque fois que `Acheter maintenant` est cliqué, les paiements sont initialisés. Il nous suffit d'attendre (`await`) cette fonction pour créer et ajouter un script dans le DOM.  
  
Voyons la fonction principale qui est responsable de la création et de l'initialisation des paiements sur la page.

### **Fonction makePayment()**

```js
const makePayment = async () => {
    const res = await initializeRazorpay();

    if (!res) {
      alert("Le chargement du SDK Razorpay a échoué");
      return;
    }

    // Faire un appel API à l'API serverless
    const data = await fetch("/api/razorpay", { method: "POST" }).then((t) =>
      t.json()
    );
    console.log(data);
    var options = {
      key: process.env.RAZORPAY_KEY, // Entrez l'ID de clé généré depuis le tableau de bord
      name: "Manu Arora Pvt Ltd",
      currency: data.currency,
      amount: data.amount,
      order_id: data.id,
      description: "Merci pour votre don de test",
      image: "https://manuarora.in/logo.png",
      handler: function (response) {
        // Valider le paiement sur le serveur - utiliser des webhooks est une meilleure idée.
        alert(response.razorpay_payment_id);
        alert(response.razorpay_order_id);
        alert(response.razorpay_signature);
      },
      prefill: {
        name: "Manu Arora",
        email: "manuarorawork@gmail.com",
        contact: "9999999999",
      },
    };

    const paymentObject = new window.Razorpay(options);
    paymentObject.open();
  };
```

La méthode `makePayment()` est responsable de l'initialisation et de l'ouverture de la fenêtre contextuelle (popup) Razorpay.

La fonction `makePayment()` effectue les opérations suivantes :

1. Initialise le script Razorpay Checkout et l'ajoute au body. Cela a été géré par la méthode `initializeRazorpay` comme nous l'avons vu précédemment.
2. Effectue un appel à la fonction serverless `/api/razorpay.js`. (Nous en parlerons dans une minute).
3. Crée un objet qui possède 4 clés importantes :
    1. `currency` - La devise dans laquelle nous voulons que la transaction ait lieu.
    2. `amount` - Le montant de la transaction. Notez qu'il doit s'agir de la plus petite unité monétaire. Par exemple, si vous êtes aux États-Unis, le montant sera en cents.
    3. `order_id` - Celui-ci sera généré par l'API serverless dont nous allons parler dans une minute.
    4. `handler` - Lorsque les paiements réussissent, cette fonction de callback est appelée.

4. Enfin, un `paymentObject` est créé avec les `options` passées en paramètres à la méthode `window.Razorpay`. Ceci est disponible grâce au script `checkout` que nous avons examiné auparavant.

Nous avons examiné la méthode `makePayment()` ci-dessus et vu une ligne de code qui est :
```js
const data = await fetch("/api/razorpay", { method: "POST" }).then((t) =>
      t.json()
    );
```

Mais qu'est-ce que cela signifie ?

Next.js nous permet d'accéder à des fonctions serverless à l'aide des `apis` qui sont disponibles dans le dossier `api` au sein de Next.js.

Les API serverless ne sont rien d'autre que des `fonctions Lambda` qui agissent comme un back-end pour nos applications JAMStack. Ici, nous pouvons écrire notre code lié au back-end facilement sans avoir à créer un back-end séparé.

Ici, nous avons besoin du serverless car l'ID de commande (`order_id`) que nous avons vu dans le code de `makePayments()` est unique et doit être généré au back-end. Non seulement cela, mais le montant (`amount`) et la devise (`currency`) proviennent également du back-end. Ceci afin de s'assurer que personne ne puisse manipuler le montant et la devise et que le portail soit sécurisé pour les paiements.

Jetons un coup d'œil au code de l'API serverless pour mieux le comprendre.

### **/api/razorpay.js**

```js
const Razorpay = require("razorpay");
const shortid = require("shortid");

export default async function handler(req, res) {
  if (req.method === "POST") {
    // Initialiser l'objet razorpay
    const razorpay = new Razorpay({
      key_id: process.env.RAZORPAY_KEY,
      key_secret: process.env.RAZORPAY_SECRET,
    });

    // Créer une commande -> générer l'ID de commande -> L'envoyer au front-end
    const payment_capture = 1;
    const amount = 499;
    const currency = "INR";
    const options = {
      amount: (amount * 100).toString(),
      currency,
      receipt: shortid.generate(),
      payment_capture,
    };

    try {
      const response = await razorpay.orders.create(options);
      res.status(200).json({
        id: response.id,
        currency: response.currency,
        amount: response.amount,
      });
    } catch (err) {
      console.log(err);
      res.status(400).json(err);
    }
  } else {
    // Gérer toute autre méthode HTTP
  }
}

```

Considérez `razorpay.js` comme votre route qui mène à `/api/razorpay`. Chaque fichier que vous créez dans le dossier API devient une route serverless. Tout comme nous créons des API dans le back-end, nous créons des fichiers ici dans le dossier API qui deviennent une route pour nous.  
  
Par exemple : supposons que vous créiez un fichier dans le dossier `/api` nommé `posts.js`. La route deviendra alors `/api/posts`, laquelle peut renvoyer tout ce que vous voulez selon le cas d'utilisation.  
  
Dans notre cas, nous devons faire une requête `POST` à notre back-end qui créera un `order_id` pour nous, ainsi qu'un `amount` et une `currency` qui pourront être renvoyés au front-end pour effectuer les paiements.  
  
Comprenons le flux de cette API.

1. Tout d'abord, nous devons installer le module `razorpay` ainsi que `shortid` pour générer des identifiants uniques courts. Pour ce faire, rendez-vous dans votre terminal et écrivez `npm install razorpay` et `npm install shortid`.
2. Maintenant, pour accéder à une requête `POST`, nous vérifions l'objet de la requête et accédons à la méthode en utilisant l'extrait ci-dessous :

```js
export default async function handler(req, res) {
  if (req.method === "POST") {
    // Initialiser l'objet razorpay
    const razorpay = new Razorpay({
      key_id: process.env.RAZORPAY_KEY,
      key_secret: process.env.RAZORPAY_SECRET,
    });

    // reste du code...
}
```

3.  Ici, `request.method` vérifie la méthode. Si la méthode est `POST`, nous continuons et initialisons l'objet Razorpay.

4.  L'objet Razorpay prend 2 paramètres : `key_id` et `key_secret`. Vous vous souvenez quand nous avons téléchargé les clés depuis le tableau de bord Razorpay ? Utilisons-les.

5.  Ouvrez/créez le fichier `.env` à la racine de votre structure de dossiers et collez le code suivant :

```js
RAZORPAY_KEY=VOTRE_CLE_ICI
RAZORPAY_SECRET=VOTRE_SECRET_ICI
```

Ici, vous pouvez insérer votre clé API et votre secret et vous serez prêt à partir.

Note : Assurez-vous de redémarrer votre serveur de développement – sinon les changements ne seront pas pris en compte.

Une fois l'objet `razorpay` configuré, il prend trois options importantes : `receipt`, `amount` et `currency`.

```js
const payment_capture = 1;
    const amount = 499;
    const currency = "INR";
const options = {
      amount: (amount * 100).toString(),
      currency,
      receipt: shortid.generate(),
    };
```

Notez que le montant et la devise sont déclarés dans notre `back-end` afin qu'il n'y ait aucun moyen pour des attaquants de les falsifier.

Une fois les options configurées, nous pouvons créer des commandes avec la méthode `_razorpay_._orders_.create(options)` de Razorpay.

```js
try {
      const response = await razorpay.orders.create(options);
      res.status(200).json({
        id: response.id,
        currency: response.currency,
        amount: response.amount,
      });
    } catch (err) {
      console.log(err);
      res.status(400).json(err);
    }
```

Ici, nous attendons simplement (`await`) la méthode `create()` fournie par Razorpay. Lorsque la méthode de création réussit, nous obtenons un `id` qui n'est rien d'autre que l'ID de commande (`order_id`) que nous devons fournir au front-end afin de générer des paiements uniques.  
  
Une fois que tout a réussi, nous envoyons une `réponse 200` avec les champs `id`, `currency` et `amount`. C'est tout ce qui est requis par le front-end pour traiter les paiements.

## **Comment effectuer des paiements avec Razorpay**

![Image](https://www.freecodecamp.org/news/content/images/2021/12/Screenshot-2021-12-21-at-1.14.41-PM.png)

Une fois que tout est intégré et en place, nous pouvons commencer à utiliser les méthodes de facturation de Razorpay – diverses options sont disponibles. Avec cela, vous pouvez commencer à facturer vos services et produits en acceptant simplement les paiements sur votre site web.

Toute la fenêtre contextuelle est personnalisable et peut être modifiée directement depuis le portail du tableau de bord de Razorpay.  
  
Puisque vous êtes en mode Test, pour commencer à utiliser leurs services en production, vous devez terminer leur processus d'identification en soumettant vos documents justificatifs et simplement basculer entre le `mode test` et le `mode live`. 

C'est tout ce que vous avez à faire du côté du code pour passer du test au live.

## **Variables d'environnement**

Pour nous assurer que nos modifications sont reflétées sur notre site web de production en direct, nous devons également ajouter les mêmes variables d'environnement que celles ajoutées dans le code sur la plateforme Vercel.  
  
Pour cela :

1. Rendez-vous sur Vercel et ouvrez votre projet.
2. Cliquez sur `settings`.
3. Cliquez sur `environment variables`.
4. Vous aurez 2 champs de saisie - Name et Value.
5. Tout d'abord, entrez `RAZORPAY_KEY` et ajoutez la clé API.
6. Deuxièmement, entrez `RAZORPAY_SECRET` et ajoutez la valeur secrète.
7. Redéployez le site web et vous pourrez effectuer des paiements dans l'environnement en direct également.

## **Démo en direct et code source**

L'intégralité du code source de l'application peut être trouvée [ici](https://github.com/manuarora700/integrate-payments).

La démo en direct du site web est [ici](https://integrate-payments.vercel.app/).


## **Conclusion**

L'intégration des paiements est facile, grâce à l'excellente documentation de Razorpay qui est facile à comprendre.

J'ai aimé coder ce site web et intégrer les paiements. Vous pouvez également voir un extrait du code sur mon site web : [Extraits de code de Manu Arora](https://manuarora.in/snippets)

Si vous avez aimé ce blog, essayez de l'implémenter sur votre propre site web afin de pouvoir atteindre vos utilisateurs finaux et faire des paiements une tâche facile pour vous-même.

Si vous souhaitez donner votre avis, contactez-moi sur mon [compte Twitter](https://twitter.com/mannupaaji) ou visitez mon [site web](https://manuarora.in/)

Merci également au [Tailwind Master Kit](https://tailwindmasterkit.com/) pour la magnifique interface utilisateur de la page d'accueil.  
  
Bon codage ! :)