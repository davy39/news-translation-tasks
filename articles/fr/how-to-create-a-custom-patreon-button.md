---
title: Comment Créer un Bouton Patreon Personnalisé
subtitle: ''
author: Ahmad Abdolsaheb
co_authors: []
series: null
date: '2022-01-18T15:53:41.000Z'
originalURL: https://freecodecamp.org/news/how-to-create-a-custom-patreon-button
coverImage: https://www.freecodecamp.org/news/content/images/2022/01/Untitled_Artwork.png
tags:
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Comment Créer un Bouton Patreon Personnalisé
seo_desc: 'Patreon is a subscription management system for creators. Although it offers
  a default button snippet, you can create a custom button that includes your preferred
  design and call to action to increase your click through rate.

  In this article you will...'
---

Patreon est un système de gestion d'abonnements pour les créateurs. Bien qu'il propose un extrait de bouton par défaut, vous pouvez créer un bouton personnalisé qui inclut votre design préféré et un appel à l'action pour augmenter votre taux de clics.

Dans cet article, vous apprendrez comment créer un simple bouton de lien Patreon personnalisé qui dirige les utilisateurs vers le flux de paiement de votre niveau préféré.

## Comment Configurer Votre Compte

### Étape 1 :

Pour commencer la configuration, vous aurez besoin d'un compte Patreon. Créez un compte si vous n'en avez pas ou connectez-vous à votre compte.

### Étape 2 :

Visitez le [portail d'enregistrement](https://www.patreon.com/portal/registration/register-clients) de votre compte. Sous **Clients & API Keys**, cliquez sur le bouton **Create Client**.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-63.png)
_Portail d'enregistrement des clients Patreon_

### Étape 3 :

Après avoir cliqué sur le bouton, une fenêtre modale apparaîtra. Remplissez les informations relatives à votre site web et assurez-vous d'entrer un URI complet (y compris la fin /) dans le champ **Redirect URIs**. Ensuite, cliquez sur le bouton **Create Client**.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-60.png)
_Formulaire d'enregistrement des clients Patreon_

### Étape 4 :

Sous **Your existing clients**, vous verrez votre nouveau client. Cliquez sur l'icône de la liste déroulante de votre nouveau client.

Enfin, copiez l'ID du client car vous en aurez besoin dans les prochaines étapes.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/image-64.png)
_Informations sur le client enregistré_

## Le Code pour le Bouton Personnalisé

Ce qui suit est une fonction qui prend un identifiant de compte, un montant ou un niveau préféré (en cents) et un URI de redirection, et retourne un lien vers le flux de paiement de Patreon.

Utilisez la fonction suivante dans votre code, ajoutez un message/log personnalisé et stylisez l'élément <a> pour créer votre bouton de lien souhaité.

```javascript
const PatreonButton = (clientId, amount, redirectURI) => {
  const clientId = `&client_id=${patreonClientId}`;
  const pledgeLevel = `$&min_cents=${amount}`;
  const v2Params = "&scope=identity%20identity[email]";
  const redirectUri = `&redirect_uri=${redirectURI}`;
  const href = `https://www.patreon.com/oauth2/become-patron?response_type=code${pledgeLevel}${clientId}${redirectUri}${v2Params}`;
  return (
    <a
      className="patreon-button link-button"
      data-patreon-widget-type="become-patron-button"
      href={href}
      rel="noreferrer"
      target="_blank"
    >
      /* 
      <svg
        id="patreon-logo"
        viewBox="10 0 2560 356"
        xmlns="http://www.w3.org/2000/svg"
        xmlnsXlink="http://www.w3.org/1999/xlink"
      >
        <g>
          <path d="M1536.54 72.449v76.933h128.24v61.473h-128.24v74.51h128.24v62.921h-206.64V9.529h206.64v62.92h-128.24M2070.82 178.907c0-55.652-37.76-107.434-99.21-107.434-61.95 0-99.21 51.782-99.21 107.434s37.26 107.435 99.21 107.435c61.45 0 99.21-51.783 99.21-107.435zm-278.77 0c0-92.916 66.79-178.093 179.56-178.093 112.26 0 179.05 85.177 179.05 178.093 0 92.916-66.79 178.093-179.05 178.093-112.77 0-179.56-85.177-179.56-178.093zM186.32 131.97c0-31.46-21.299-58.563-54.206-58.563H78.398v117.109h53.716c32.907 0 54.206-27.086 54.206-58.546zM0 9.529h141.788c75.016 0 123.417 56.628 123.417 122.441s-48.401 122.423-123.417 122.423h-63.39v93.893H0V9.529zM492.17 106.314l-41.621 139.382h82.266L492.17 106.314zm73.081 241.972-13.054-41.134H431.69l-13.072 41.134h-83.73L455.882 9.529h72.105l122.442 338.757h-85.178zM782.055 77.277H705.61V9.529h231.793v67.748h-76.951v271.009h-78.397V77.277M2485.08 230.202V9.529h77.91v338.757h-81.78l-121.97-217.78v217.78h-78.4V9.529h81.78l122.46 220.673M1245.68 131.97c0-31.46-21.3-58.563-54.21-58.563h-53.72v117.109h53.72c32.91 0 54.21-27.086 54.21-58.546zM1059.36 9.529h142.29c75 0 123.4 56.628 123.4 122.441 0 47.425-25.17 89.517-67.28 109.369l67.77 106.947h-90.98l-60.03-93.893h-36.78v93.893h-78.39V9.529z" />
        </g>
      </svg> */
    </a>
  );
};

```

N'hésitez pas à décommenter l'élément SVG imbriqué et à l'utiliser comme illustration de votre bouton ou à insérer le vôtre. Voici quelques styles pour ajuster votre bouton pour les modes clair et sombre.

```css
a.patreon-button {
  border-radius: 5px;
  background-color: #ff424d;
  min-height: 42px;
  border: none;
  display: grid;
  place-items: center;
}
a.patreon-button svg {
  max-height: 12px;
  fill: white;
}
a.patreon-button:active,
a.patreon-button:active:focus,
a.patreon-button:hover {
  background-color: #e13d47;
}

.dark-palette a.patreon-button {
  background-color: white;
}

.dark-palette a.patreon-button svg {
  fill: #ff424d;
}
.dark-palette a.patreon-button:active,
.dark-palette a.patreon-button:active:focus,
.dark-palette a.patreon-button:hover {
  background-color: #efefef;
}
```

Voilà. Un bouton personnalisé pour diriger les utilisateurs vers le niveau souhaité sur Patreon.

Chez freeCodeCamp, nous avons implémenté le même bouton en utilisant [TypeScript](https://github.com/freeCodeCamp/freeCodeCamp/blob/56a60700b7e999548262e3827b80d09fdf201ad2/client/src/components/Donation/patreon-button.tsx) pour notre [page de dons](https://www.freecodecamp.org/donate/).

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-18-at-9.13.20-AM.png)
_Bouton Patreon personnalisé sur la page de dons de freeCodeCamp_

En cliquant sur le bouton, les utilisateurs connectés à Patreon devraient être dirigés directement vers la page de paiement.

![Image](https://www.freecodecamp.org/news/content/images/2022/01/Screen-Shot-2022-01-18-at-9.09.36-AM.png)
_Page de paiement Patreon_

## Les prochaines étapes

Si vous souhaitez synchroniser votre plateforme avec Patreon, vous pourriez ajouter des métadonnées au bouton et les recevoir via un webhook.

Alternativement, si vous cherchez à créer une intégration complète, il existe une variété d'intégrations open source que vous pourriez utiliser comme modèle. Pour des questions spécifiques, référez-vous à la communauté active des développeurs de Patreon [developer community](https://www.patreondevelopers.com/).

Enfin, si vous avez aimé lire cet article, n'oubliez pas de me suivre sur [twitter](https://twitter.com/abdolsaheb?lang=en) pour plus d'articles et de tutoriels.

Bon codage.