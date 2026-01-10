---
title: Comment créer un formulaire de contact avec Netlify Forms et Next.js
subtitle: ''
author: Colby Fayock
co_authors: []
series: null
date: '2020-08-26T17:13:13.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-contact-form-with-netlify-forms-and-nextjs
coverImage: https://www.freecodecamp.org/news/content/images/2020/08/netlify-forms.jpg
tags:
- name: Netlify
  slug: netlify
- name: Next.js
  slug: nextjs
- name: React
  slug: react
seo_title: Comment créer un formulaire de contact avec Netlify Forms et Next.js
seo_desc: "If you want someone to be able to contact you or submit information on\
  \ a website, an HTML form is a pretty standard way to achieve that. \nBut accepting\
  \ form submissions usually requires an additional service or complex server-side\
  \ code. How can we ta..."
---

Si vous souhaitez que quelqu'un puisse vous contacter ou soumettre des informations sur un site web, un formulaire HTML est une méthode assez standard pour y parvenir. 

Mais l'acceptation des soumissions de formulaires nécessite généralement un service supplémentaire ou un code côté serveur complexe. Comment pouvons-nous tirer parti de Netlify pour créer facilement de nouveaux formulaires ?

* [Qu'est-ce que Netlify ?](#heading-qu-est-ce-que-netlify)
* [Que allons-nous construire ?](#heading-que-allons-nous-construire)
* [Combien cela coûte-t-il ?](#heading-combien-cela-coute-t-il)
* [Partie 1 : Créer un formulaire de contact avec HTML](#heading-partie-1-creer-un-formulaire-de-contact-avec-html)
* [Partie 2 : Ajouter un formulaire Netlify personnalisé à une application Next.js React](#heading-partie-2-ajouter-un-formulaire-netlify-personnalise-a-une-application-nextjs-react)

%[https://www.youtube.com/watch?v=GLxgxnLTVLE]

## Qu'est-ce que Netlify ?

[Netlify](https://www.netlify.com/) est une plateforme web qui vous permet de déployer facilement de nouveaux projets web avec des flux de travail faciles à configurer. Cela inclut le déploiement d'un site web statique, de fonctions lambda, et comme nous allons en parler ici, de formulaires personnalisés.

Leur service de formulaires fonctionne dans le cadre du pipeline de construction et de déploiement. Lorsque nous incluons un formulaire avec un attribut spécifique à notre page, Netlify reconnaîtra ce formulaire et le configurera pour qu'il fonctionne.

## Que allons-nous construire ?

Nous allons construire un formulaire de contact qui permettra aux gens de vous envoyer un message via votre site web.

Le formulaire lui-même sera assez simple. Comme un formulaire de contact standard, nous demanderons le nom, l'adresse e-mail et un message de quelqu'un.

Nous allons le construire en utilisant du HTML simple pour démontrer comment cela fonctionne, puis le construire avec [Next.js](https://nextjs.org/) pour créer un formulaire dans une application React.

## Combien cela coûte-t-il ?

Les formulaires Netlify sont gratuits pour commencer. Ce niveau gratuit est limité à 100 soumissions de formulaires par site web par mois, donc si vous restez en dessous de ce seuil, cela sera toujours gratuit.

Cela dit, si vous dépassez 100 soumissions de formulaires sur un site particulier, le premier niveau sera de 19 $+ au moment de la rédaction de cet article. Vous pouvez consulter les [derniers plans tarifaires sur le site web de Netlify](https://www.netlify.com/pricing/).

## Partie 1 : Créer un formulaire de contact avec HTML

Pour commencer, nous allons créer un formulaire de base avec du HTML pur. C'est une victoire rapide pour démontrer comment cela fonctionne.

### Étape 1 : Créer un formulaire HTML

Pour notre formulaire, nous pouvons vraiment utiliser ce que nous voulons. Les formulaires de contact peuvent être aussi simples qu'un champ d'adresse e-mail et un champ de message, ou inclure une variété d'options pour aider une entreprise à répondre à des questions spécifiques.

Nous allons commencer par quelque chose de simple. Nous allons créer un formulaire qui demande le nom, l'adresse e-mail et un message de quelqu'un.

Pour commencer, créez un nouveau fichier HTML à la racine de votre projet. Ce fichier HTML doit inclure la structure de base d'un document HTML. À l'intérieur du body, ajoutons notre nouveau formulaire :

```html
<form name="contact" method="POST" data-netlify="true">
    <p>
      <label for="name">Nom</label>
      <input type="text" id="name" name="name" />
    </p>
    <p>
      <label for="email">Email</label>
      <input type="text" id="email" name="email" />
    </p>
    <p>
      <label for="message">Message</label>
      <textarea id="message" name="message"></textarea>
    </p>
    <p>
      <button type="submit">Envoyer</button>
    </p>
  </form>

```

Dans l'extrait ci-dessus, nous :

* Créons un nouveau formulaire
* Le formulaire a un attribut name, une méthode, et un attribut `data-netlify` défini sur `true`
* Créons 3 champs de formulaire avec des labels, chacun identifié avec un attribut name
* Créons un bouton pour soumettre le formulaire

La chose à laquelle nous voulons prêter le plus attention est l'attribut `data-netlify` et le `name` du formulaire. Lorsque Netlify lit le site, il verra ces champs et les utilisera pour transformer votre formulaire en un formulaire actif.

Je vais également ajouter un peu de CSS pour que les labels aient un aspect plus cohérent. Vous pouvez optionnellement ajouter ceci à la balise `<head>` du document :

```html
<style>
  body {
    font-family: sans-serif;
  }
  label {
    display: block;
    margin-bottom: .2em;
  }
</style>

```

Et à ce stade, nous devrions avoir un formulaire de base !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/basic-html-form-1.jpg)
_Formulaire HTML de base_

Vous allez maintenant vouloir mettre ce formulaire sur GitHub ou votre fournisseur Git préféré et nous serons prêts pour l'étape suivante.

[Suivez avec le commit !](https://github.com/colbyfayock/my-html-netlify-form/commit/482a4e14b3c8e10bc9ae29c2f233c3312dd1b89a)

### Étape 2 : Configurer un nouveau formulaire avec Netlify

Une fois notre formulaire poussé vers notre fournisseur Git, nous pouvons maintenant le synchroniser avec Netlify.

Tout d'abord, créez un compte ou utilisez un compte existant avec Netlify et cliquez sur le bouton **Nouveau site depuis Git**.

Ici, sélectionnez le fournisseur Git que vous avez utilisé. J'utilise **GitHub** dans mon exemple.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-connect-git-provider.jpg)
_Connexion d'un fournisseur Git dans Netlify_

Une fois que vous avez sélectionné votre fournisseur Git, il vous demandera d'autoriser l'accès afin que Netlify puisse trouver votre dépôt Git.

Après avoir connecté votre compte avec succès, vous devriez maintenant voir une liste des dépôts auxquels vous avez donné accès. Trouvez le dépôt auquel vous avez ajouté votre formulaire et sélectionnez-le.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/connecting-git-repo-netlify.jpg)
_Connexion d'un dépôt Git à Netlify_

Si vous suivez avec moi, notre formulaire est en HTML pur, ce qui signifie qu'il ne devrait y avoir aucune étape de construction ou aucun répertoire spécial dans lequel il est publié. Mais n'hésitez pas à ajuster ces paramètres si vous avez fait quelque chose de différent.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/configuring-build-steps-netlify.jpg)
_Configuration des étapes de construction dans Netlify_

Maintenant, cliquez sur **Déployer le site**, ce qui ouvrira une nouvelle page dans Netlify et en un rien de temps votre site sera déployé avec succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-site-successfully-deployed.jpg)

Enfin, cliquez sur l'URL en haut du tableau de bord du projet Netlify qui se termine par netlify.app. Une fois chargé, vous verrez votre formulaire !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/html-form-netlify.jpg)

### Étape 3 : Voir les soumissions de formulaires

Maintenant que nous avons notre formulaire, nous voulons finalement voir les réponses.

Pour commencer, ajoutez quelques informations à votre formulaire et cliquez sur soumettre.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-html-form.jpg)
_Test du formulaire HTML_

Une fois que vous avez soumis, vous remarquerez que vous êtes redirigé vers une page Netlify qui indique que le formulaire a été soumis avec succès.

Vous pouvez maintenant retourner à votre tableau de bord de projet Netlify et faire défiler un peu vers le bas où vous pouvez maintenant voir une boîte avec **Soumissions de formulaires récentes** ainsi que votre nouvelle soumission.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-form-submission.jpg)
_Soumission de formulaire Netlify_

## Partie 2 : Ajouter un formulaire Netlify personnalisé à une application Next.js React

Si le formulaire doit vivre seul et ne pas faire partie d'un site plus grand, il y a beaucoup d'avantages à laisser votre formulaire en HTML pur. Mais souvent, nous voulons que notre formulaire de contact fasse partie de notre site web ou de notre application.

Ici, nous allons passer en revue l'ajout d'un formulaire à une application [Next.js](https://nextjs.org/).

_Note : notre démonstration de l'utilisation de Next.js est une application rendue statiquement. Si vous chargez votre formulaire côté client, ce qui signifie que le HTML sous-jacent n'inclut pas le formulaire, consultez les notes en bas de cette page pour plus d'informations sur les solutions._

### Étape 0 : Créer une application Next.js

Pour commencer, nous avons besoin d'une application. Nous allons utiliser Next.js puisque nous pouvons créer une nouvelle application à partir de zéro assez facilement.

Pour ce faire, vous pouvez naviguer vers l'endroit où vous souhaitez créer l'application et exécuter :

```
yarn create next-app [nom-du-projet]
# ou
npx create-next-app [nom-du-projet]

```

Je vais nommer mon projet `my-nextjs-netlify-form`.

Une fois que Next.js a fini d'installer les dépendances, il vous donnera des instructions pour naviguer vers votre répertoire de projet et démarrer votre serveur de développement.

Et après avoir exécuté `yarn dev` ou `npm run dev`, vous devriez être prêt à partir avec votre application Next.js :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/new-nextjs-app-1.jpg)
_Nouvelle application Next.js_

[Suivez avec le commit !](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/6f9fb6966b6c112a3ec934e305f2dd115e9d424e)

### Étape 1 : Ajouter un formulaire HTML à une application Next.js

Notre Étape 1 va ressembler beaucoup à la Partie 1.

À l'intérieur de `pages/index.js`, nous voulons trouver notre wrapper de grille et nous allons l'utiliser pour ajouter notre formulaire.

Trouvez `<div className={styles.grid}>` et remplacez le bloc entier par ce qui suit :

```jsx
<div className={styles.grid}>
  <div className={styles.card}>
    <form name="contact" method="POST" data-netlify="true">
      <p>
        <label htmlFor="name">Nom</label>
        <input type="text" id="name" name="name" />
      </p>
      <p>
        <label htmlFor="email">Email</label>
        <input type="text" id="email" name="email" />
      </p>
      <p>
        <label htmlFor="message">Message</label>
        <textarea id="message" name="message"></textarea>
      </p>
      <p>
        <button type="submit">Envoyer</button>
      </p>
    </form>
  </div>
</div>

```

Voici ce que nous faisons :

* Nous profitons de la grille existante de Next.js
* Nous profitons également de la carte existante dans laquelle nous allons inclure notre formulaire
* À l'intérieur de la carte, nous collons le même formulaire HTML que dans la Partie 1

Si nous rechargeons la page, nous pouvons maintenant voir notre formulaire à l'intérieur d'une carte, comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/08/form-nextjs-react-app.jpg)
_Ajout d'un formulaire à une application Next.js_

Avant de continuer, nous voulons faire 2 choses.

Tout d'abord, parce que nous créons ce formulaire dans une application JavaScript, [Netlify recommande](https://www.netlify.com/blog/2017/07/20/how-to-integrate-netlifys-form-handling-in-a-react-app/#form-handling-with-static-site-generators) que nous ajoutions une entrée cachée avec le nom de notre formulaire.

À l'intérieur de notre formulaire, ajoutez l'entrée suivante en haut de l'élément de formulaire :

```
<input type="hidden" name="form-name" value="contact" />

```

Assurez-vous que la valeur de cette entrée est la même que le nom de votre formulaire.

Deuxièmement, parce que la carte que nous réutilisons est destinée à une liste de liens, Next.js inclut certains effets de survol. Cela rend le formulaire confus à utiliser, alors supprimons-les.

Supprimez ce qui suit de `styles/Home.module.css` :

```
.card:hover,
.card:focus,
.card:active {
  color: #0070f3;
  border-color: #0070f3;
}

```

Pour une étape bonus supplémentaire, je vais mettre à jour le titre de ma page en "Contactez-moi" et supprimer la description. N'hésitez pas à faire ce que vous voulez.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/nextjs-contact-form-title.jpg)
_Mise à jour du titre du formulaire_

Et une fois que vous êtes prêt, comme avant, ajoutez ceci comme un nouveau dépôt à GitHub ou votre fournisseur Git préféré.

[Suivez avec le commit !](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/b9cac11411c6c71ee648c8631c35740735c599b7)

### Étape 2 : Configurer et déployer votre application Next.js sur Netlify

Le déploiement de notre application sur Netlify sera assez similaire, mais avant d'y arriver, nous devons configurer notre application Next.js pour qu'elle puisse être exportée lors de la construction.

Dans notre application Next.js, à l'intérieur du fichier `package.json`, nous voulons mettre à jour le script `build` en :

```json
"build": "next build && next export",

```

Maintenant, lorsque vous exécutez le script `build`, il compilera l'application en HTML, CSS et JS statiques à l'intérieur du répertoire `out`. Cela nous permettra de la déployer sur Netlify. Vous pouvez même l'essayer localement sur votre machine si vous le souhaitez.

Avec ce changement, validez-le et poussez-le vers votre fournisseur Git.

Ensuite, le déploiement de l'application ressemblera principalement à la Partie 1. La seule différence est que, comme nous avons une application Next.js, nous devons ajouter nos étapes de construction.

Pour commencer, nous allons vouloir connecter notre fournisseur Git comme dans la Partie 1.

Une fois que nous arrivons à la page des paramètres de déploiement, nous voulons configurer notre commande de construction et notre répertoire de publication.

Notre **commande de construction** sera `yarn build` ou `npm run build` selon le gestionnaire de paquets que vous avez utilisé et le **répertoire de publication** sera `out`.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-deploy-settings-nextjs-app.jpg)
_Paramètres de déploiement pour une application Next.js statique_

Après cela, cliquez sur **Déployer le site**, et cela démarrera comme avant.

Une fois le déploiement terminé, nous serons prêts à ouvrir l'application.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/successfully-deployed-nextjs-app-netlify.jpg)
_Application Next.js déployée avec succès sur Netlify_

Et une fois que nous avons ouvert notre application, nous pouvons tester notre formulaire en le remplissant et en cliquant sur soumettre.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-nextjs-contact-form.jpg)

Comme avant, nous atterrirons sur une page de succès Netlify. Mais si nous retournons et regardons à l'intérieur de notre tableau de bord Netlify, nous verrons maintenant notre soumission !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/successful-nextjs-form-submission-netlify-form.jpg)
_Soumission de formulaire Next.js réussie sur Netlify_

[Suivez avec le commit !](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/3a4516a706af550a37372a9aa2bbaf54b9d7d691)

### Bonus : Gardez les gens sur votre site web avec un message de succès

Une autre fonctionnalité intéressante avec les formulaires Netlify est qu'elle permet de configurer votre formulaire pour garder les gens sur votre site web en configurant le formulaire directement sur la page.

Vous avez beaucoup d'options ici, que ce soit pour rediriger quelqu'un vers une nouvelle page ou configurer un message sur la page à partir de laquelle il a soumis le formulaire.

Pour cette démonstration, nous allons configurer un paramètre d'URL que nous pouvons détecter pour afficher un message de succès si nous voyons ce paramètre.

Pour ce faire, sur votre formulaire HTML, ajoutez l'attribut suivant :

```
action="/?success=true"

```

Cela indiquera à Netlify que nous voulons rester sur la page d'accueil (puisque nous n'avons qu'une seule page) mais appliquer le paramètre d'URL afin que nous puissions le détecter dans notre application.

Ensuite, nous pouvons utiliser les hooks `useState` et `useEffect` pour voir ce paramètre et mettre à jour la page.

En haut du fichier, importons ces hooks :

```
import { useState, useEffect } from 'react';

```

À l'intérieur de notre composant Home en haut, ajoutons notre état :

```
const [success, setSuccess] = useState(false);

```

Et pour détecter le paramètre d'URL, nous pouvons utiliser le hook `useEffect` :

```jsx
useEffect(() => {
  if ( window.location.search.includes('success=true') ) {
    setSuccess(true);
  }
}, []);

```

_Note : ceci est une manière simple d'atteindre ce résultat pour la démonstration. Si vous avez une application plus compliquée, vous pourriez vouloir nommer le paramètre quelque chose de plus logique et analyser correctement les paramètres d'URL pour la valeur._

Ce que cela fait, c'est que lorsque le composant est rendu, il déclenchera ce hook `useEffect`, vérifiant les paramètres dans l'URL, et recherchant `success=true`. S'il le trouve, il mettra à jour notre variable d'état `success` à `true` !

Ensuite, sous le titre de notre page (`<h1>`), ajoutons l'extrait suivant :

```jsx
{success && (
  <p style={{ color: 'green'}}>
    Formulaire soumis avec succès !
  </p>
)}

```

Ici, nous vérifions si `success` est vrai, et si c'est le cas, nous incluons une ligne de texte qui indique que le formulaire a été soumis avec succès.

Bien que vous ne puissiez pas soumettre votre formulaire localement, vous pouvez tester cela en visitant votre application en cours d'exécution localement avec le paramètre d'URL `?success=true` comme :

```
http://localhost:3000/?success=true

```

![Image](https://www.freecodecamp.org/news/content/images/2020/08/testing-success-message-locally.jpg)
_Test du message de succès localement_

Enfin, vous pouvez pousser ces changements vers votre fournisseur Git et Netlify reconstruira automatiquement votre site.

Et une fois que c'est terminé, vous pouvez soumettre votre formulaire comme avant et voir le message de succès.

![Image](https://www.freecodecamp.org/news/content/images/2020/08/netlify-success-redirect.jpg)
_Redirection réussie du formulaire sur Netlify_

Et voir que notre formulaire est toujours soumis !

![Image](https://www.freecodecamp.org/news/content/images/2020/08/form-submission-success-netlify.jpg)
_Soumission réussie du formulaire sur Netlify_

[Suivez avec le commit !](https://github.com/colbyfayock/my-nextjs-netlify-form/commit/25378cd6b17ad6bb48dc7281220ab48eba74f478)

## Formulaires Netlify et code côté client

Une chose à noter avec la solution de Netlify est que cela ne fonctionne aussi "simplement" que pour les pages HTML statiques. 

Si votre page utilise JavaScript pour gérer le contenu de cette page, comme ne pas ajouter un formulaire avant que la page ne se charge, vous devrez consulter la documentation de Netlify sur la manière de faire fonctionner cela [avec un attribut de formulaire supplémentaire](https://docs.netlify.com/forms/setup/#javascript-forms).

Netlify donne également un exemple sur la manière de [soumettre votre formulaire dynamiquement avec JavaScript](https://docs.netlify.com/forms/setup/#submit-forms-via-ajax) afin que vous puissiez créer une expérience personnalisée dans votre application.

## Que pouvez-vous faire d'autre ?

### Configurer des flux de travail avancés avec d'autres outils

Netlify vous permet de vous intégrer avec d'autres outils pour vous permettre de gérer vos soumissions de formulaires. Notamment, [Netlify fonctionne avec Zapier](https://zapier.com/apps/netlify/integrations), ce qui signifie que vous pouvez accepter les soumissions entrantes et faire ce que vous voulez avec elles.

[https://docs.netlify.com/forms/notifications/](https://docs.netlify.com/forms/notifications/)

### Prévenir le spam avec reCAPTCHA

Le spam est également une réalité. Vous ne voulez pas que votre boîte de réception soit inondée de spam, vous pouvez donc tirer parti du champ Honeypot intégré de Netlify ou ils vous guident pour ajouter reCAPTCHA 2.

[https://docs.netlify.com/forms/spam-filters/](https://docs.netlify.com/forms/spam-filters/)

<div id="colbyfayock-author-card">
  <p style="margin: 0;">
    <a href="https://twitter.com/colbyfayock" style="display: block;">
      <img src="https://res.cloudinary.com/fay/image/upload/w_2000,h_400,c_fill,q_auto,f_auto/w_1020,c_fit,co_rgb:007079,g_north_west,x_635,y_70,l_text:Source%20Sans%20Pro_64_line_spacing_-10_bold:Colby%20Fayock/w_1020,c_fit,co_rgb:383f43,g_west,x_635,y_6,l_text:Source%20Sans%20Pro_44_line_spacing_0_normal:Follow%20me%20for%20more%20JavaScript%252c%20UX%252c%20and%20other%20interesting%20things!/w_1020,c_fit,co_rgb:007079,g_south_west,x_635,y_70,l_text:Source%20Sans%20Pro_40_line_spacing_-10_semibold:colbyfayock.com/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_68,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_145,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_222,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/w_300,c_fit,co_rgb:7c848a,g_north_west,x_1725,y_295,l_text:Source%20Sans%20Pro_40_line_spacing_-10_normal:colbyfayock/v1/social-footer-card" alt="Suivez-moi pour plus de Javascript, UX, et autres choses intéressantes !" style="width:100%;display: block;margin: 0;">
    </a>
  </p>
  <ul style="display:flex;justify-content:center;list-style:none;padding:0;margin: .5em 0 0;font-size: .8em;">
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://twitter.com/colbyfayock" style="text-decoration: none;">? Suivez-moi sur Twitter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://youtube.com/colbyfayock" style="text-decoration: none;">? Abonnez-vous à ma chaîne Youtube</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://www.colbyfayock.com/newsletter/" style="text-decoration: none;">4e83fb Sign Up For My Newsletter</a>
    </li>
    <li style="margin: 0 .6em;padding: 0;">
      <a href="https://github.com/sponsors/colbyfayock" style="text-decoration: none;">? Sponsorisez-moi</a>
    </li>
  </ul>
</div>