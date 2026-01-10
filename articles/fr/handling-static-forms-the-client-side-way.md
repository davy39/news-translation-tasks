---
title: Comment gérer les formulaires statiques - La méthode côté client
subtitle: ''
author: Bolaji Ayodeji
co_authors: []
series: null
date: '2019-07-21T20:58:47.000Z'
originalURL: https://freecodecamp.org/news/handling-static-forms-the-client-side-way
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/1_NjU8ApeQC0wK4NgIaOjALw.png
tags:
- name: forms
  slug: forms
- name: JAMstack
  slug: jamstack
seo_title: Comment gérer les formulaires statiques - La méthode côté client
seo_desc: 'Forms are interactive elements used to get input from the user for further
  processing. Most times, forms are just used to receive input that requires no processing
  but rather just receiving data, this might be a contact form, RSVP, get a quote
  e.t.c

  ...'
---

Les formulaires sont des éléments interactifs utilisés pour obtenir des entrées de l'utilisateur en vue d'un traitement ultérieur. La plupart du temps, les formulaires sont simplement utilisés pour recevoir des entrées qui ne nécessitent aucun traitement, mais simplement la réception de données, cela peut être un formulaire de contact, une réponse à une invitation, une demande de devis, etc.

Traditionnellement, les formulaires sont gérés avec l'aide d'un serveur (également connu sous le nom de côté serveur), mais cela est plus efficace lorsque vous traitez les données du formulaire, peut-être un formulaire d'inscription d'utilisateur où les données du formulaire sont validées, authentifiées et sauvegardées dans une base de données.

Lorsque vous construisez un formulaire simple où vous ne recevez que des données de l'utilisateur et ne les traitez pas (c'est-à-dire un formulaire de contact), le but est d'obtenir les données du formulaire et de les envoyer à l'email de support de votre entreprise (par exemple, info@..., support@...)

Utiliser un serveur ici n'est pas idéal et est seulement un excès, une méthode très courante de faire cela est via [PHPMailer](https://github.com/PHPMailer/PHPMailer) (la bibliothèque classique d'envoi d'emails pour PHP). PHPMailer est utilisé avec PHP et nécessite beaucoup de configurations serveurs ennuyeuses. Et si vous construisez simplement un site statique ? Il devrait y avoir une manière plus facile de faire cela côté client, non ?

Dans cet article, je vais vous présenter deux méthodes de gestion des données de formulaire côté client dans les sites statiques. Il existe d'autres méthodes, mais j'ai utilisé ces deux-là et les ai considérées comme les meilleures et les plus faciles (pas de sentiments blessés :) ).

PAS de configurations fastidieuses, PAS de serveurs, PAS de choses sérieuses, construisez simplement votre formulaire, faites quelques petits ajustements, l'utilisateur soumet et bingo, cela va directement à votre email désigné. :)

### FORMULAIRE DE DÉMARRAGE

Pour les besoins de cet article, j'ai construit un formulaire de base avec HTML5 et Bootstrap 4, vous pouvez le fork depuis le [Codepen ci-dessous.](https://codepen.io/iambolajiayo/pen/MdGdex)

%[https://codepen.io/iambolajiayo/pen/MdGdex] 

Actuellement, ce formulaire n'utilise aucune des méthodes dont nous allons parler, à la fin de l'article, je fournirai le code complet pour les deux méthodes, vous pourrez alors mettre à jour le formulaire et tester. J'ai ajouté une petite validation, ne vous inquiétez pas pour cela.

Maintenant, commençons !!

### MÉTHODE UN

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-12.png align="left")

[Formspree](http://formspree.io/) fournit des formulaires HTML fonctionnels via leur plateforme sans PHP ni JavaScript. Envoyez votre formulaire à leur URL et il sera transféré à votre email. Pas de PHP, de JavaScript ou d'inscription requis — parfait pour les sites statiques !

Attendez !, attendez !!, attendez !!! c'est aussi [Open Source](https://github.com/formspree/formspree)

#### GESTION DE FORMULAIRE AVEC FORMSPREE

* Construisez votre formulaire, [nous l'avons déjà fait](https://codepen.io/iambolajiayo/pen/MdGdex?editors=1010)

(Suivez l'étape suivante et mettez à jour ce formulaire pour utiliser cette méthode)

```html
<form action="https://formspree.io/you@email.com" method="POST">
    <input type="hidden" name="_subject" value="Formulaire de Bolaji">                 
    <input type="hidden" name="_next" value="/thanks.html" >
    <input type="text" name="name">
    <input type="email" name="_replyto">
    <input type="text" name="phone">
    <input type="submit" value="Envoyer">
</form>
```

Maintenant, passons en revue les nouvelles choses ajoutées ci-dessus.

* Nous avons changé l'attribut d'action du formulaire en `[https://formspree.io/you@email.com](https://formspree.io/you@email.com)` [remplacez [your@email.com](mailto:your@email.com) par votre propre email.] Cela envoie simplement les données de votre formulaire à formspree puis à votre email. Formspree agit ici comme un tiers.

* J'ai ajouté quelques attributs de nom aux champs de saisie. Cela configure simplement chaque champ afin que nous puissions récupérer les données et les envoyer à formspree.

— Pour l'adresse email, j'ai ajouté un **attribut _replyto** (Cela signifie simplement que vous pourrez répondre rapidement à l'utilisateur qui a initialement soumis le formulaire via email)

— J'ai ajouté un **attribut _subject**. Cette valeur est utilisée pour le sujet de l'email afin que vous puissiez répondre rapidement aux soumissions sans avoir à modifier la ligne de sujet chaque fois.

— J'ai ajouté un **attribut _next**. Par défaut, après avoir soumis un formulaire, l'utilisateur voit la page "Merci" de Formspree. Vous pouvez fournir une URL alternative pour cette page comme suit : `<input type="hidden" name="_next" value="/thanks.html" />`

![Image](https://cdn-media-1.freecodecamp.org/images/1*M2O2tR08URl1I2i5bVGU5Q.png align="left")

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_M2O2tR08URl1I2i5bVGU5Q.png align="left")

*page de succès par défaut de formspree*

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_nLA5m3_yjx4mmmJAmuu8Yg.png align="left")

*page de succès personnalisée que j'ai construite pour un client.*

* Nous avons ajouté un attribut de valeur au bouton d'envoi [**value="Envoyer"**]

C'est notre Thanos, un clic sur ce bouton et votre formulaire est effacé et ses données envoyées à votre email.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_hnEhoz4pSb4pNtzXD0pDpw.png align="left")

C'est tout pour l'utilisation de formspree :) Bien qu'il existe d'autres paramètres de configuration pour plusieurs autres fonctionnalités, vous pouvez vérifier [ici](https://formspree.io/).

#### CHOSES À NOTER !

* Vous n'avez pas besoin de vous inscrire pour utiliser formspree, ajoutez simplement votre attribut d'action et vous êtes prêt à partir. Vous ne vous inscrivez que si vous voulez un [plan payant](https://formspree.io/plans).

* Assurez-vous que votre formulaire a l'attribut `method="POST"`

* Formspree utilise reCAPTCHA pour identifier les soumissions de spam. Après qu'un utilisateur clique sur notre *Thanos*, il devra faire une vérification CAPTCHA. Une manière cool d'arrêter les soumissions de spam.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_0mq3GFJ4_fRWnR5_vX1L5g.png align="left")

* Après cela, le formulaire est envoyé à votre email désigné et la page de succès personnalisée est affichée !

* Formspree ne lit pas vos données de formulaire, ils n'y ont pas accès, ils sont simplement un service de livraison, vous envoyez votre colis scellé à eux, ils le livrent à votre client, cool non ? :)

* Formspree est gratuit pour 50 soumissions par formulaire par mois SEULEMENT ! Besoin de plus, vous pouvez passer à un [plan payant](https://formspree.io/plans).

* Formspree a à la fois des plans gratuits et payants. Les plans payants ont plusieurs autres fonctionnalités comme un tableau de bord d'administration, des soumissions illimitées, une gestion AJAX, etc. Les plans payants et leurs fonctionnalités peuvent être trouvés [ici](https://formspree.io/plans)

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_UZwPE17ZnWZym5qaDkYIwA.png align="left")

Si vous construisez un site basique, vous ne devriez pas vous inquiéter des plans payants, les plans payants sont surtout nécessaires pour les applications et entreprises d'entreprise, le plan gratuit couvrira tous vos besoins. J'utilise cela pour certains projets clients aussi :)

* Les utilisateurs premium de Formspree peuvent soumettre des formulaires via AJAX. Il suffit de définir l'en-tête Accept sur application/json. Si vous utilisez jQuery, cela peut être fait comme suit :

```js
    $.ajax({
        url: "https://formspree.io/FORM_ID",
        method: "POST",
        data: {message: "bonjour !"},
        dataType: "json"
    });
```

Eh bien, c'est pour les utilisateurs payants :)

Si vous n'utilisez pas jQUERY comme moi et que vous en avez marre de la syntaxe AJAX longue par défaut, consultez la [bibliothèque simpleAJAX](https://github.com/BolajiAyodeji/simple-ajax-library), une bibliothèque simple que j'ai construite pour gérer les requêtes HTTP. Comme ceci :

```js
const http = new simpleAJAX;

const data = {
    "name": "Bolaji Ayodeji",
    "email": "hi@bolajiayodeji.com",
    "message": "bonjour"
};
http.post('https://formspree.io/FORM_ID', data,
(err, user) => {
    if(err) {
     console.log(err)
    } else {
     console.log(user);
   }
 });
```

Une étoile me rendrait heureux ! :)

Si vous êtes dans React, [ZEIT](https://zeit.co/) a un guide complet sur l'utilisation de Formspree avec [Create React App](https://zeit.co/guides/deploying-react-forms-using-formspree-with-zeit-now), complet avec des instructions de déploiement. Hautement recommandé !

### MÉTHODE DEUX

![Image](https://www.freecodecamp.org/news/content/images/2020/02/image-13.png align="left")

[Netlify](https://www.netlify.com/) offre la gestion des formulaires pour les sites déployés sur leur plateforme.

#### GESTION DE FORMULAIRE AVEC NETLIFY

* Créez un compte sur Netlify et déployez votre site là-bas.

Veuillez regarder cette vidéo de 14 minutes par [@JamesQuick](https://twitter.com/jamesqquick) ci-dessous si vous ne savez pas ce qu'est Netlify. Découvrez toutes les fonctionnalités géniales de Netlify comme le déploiement continu, les fonctions Lambda, les tests fractionnés, les branches de prévisualisation, et plus encore !

%[https://www.youtube.com/watch?v=qAUX2A-W4Bc] 

* Maintenant que vous avez déployé votre site, créons à nouveau le formulaire

```html
    <form action="/thanks.html" name="formulaire de Bolaji" method="POST" data-netlify="true">
        <input type="text" name="name">
        <input type="email" name="email">
        <input type="text" name="phone">
        <input type="submit">
    </form>
```

Maintenant, passons en revue les nouvelles choses que j'ai ajoutées ci-dessus.

* Netlify est assez simple, vous ajoutez simplement l'attribut netlify `data-netlify="true"` à la balise `<form>`, et vous pouvez commencer à recevoir les soumissions dans le panneau d'administration de votre site Netlify.

* Ici, l'attribut `action` sert de page de succès personnalisée

C'est tout, vos soumissions de formulaire vont directement à votre panneau d'administration Netlify

Paramètres > Build & deploy > Environment > Variables d'environnement

(Regardez la vidéo ci-dessus si vous ne comprenez pas ce que signifie le panneau)

**Choses à noter !**

* Votre site doit être hébergé sur netlify pour utiliser cette méthode

* Vous devez ajouter l'attribut netlify pour que le formulaire fonctionne

* Vous pouvez trouver toutes les soumissions à vos formulaires Netlify dans l'onglet Forms de votre tableau de bord de site. **Paramètres > Forms**

* Netlify a également des plans gratuits et payants

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1__sg2Fo1r5gniCilQjBcMhA.png align="left")

[*https://www.netlify.com/pricing*](https://www.netlify.com/pricing/#features)

* Netlify dispose de plusieurs options de notification intégrées pour les soumissions de formulaires vérifiées, y compris les notifications par email et Slack. **(Uniquement disponible dans les plans payants)**. Vous pouvez les trouver dans **Paramètres > Forms > Notifications de formulaire**.

* Netlify s'intègre également avec [Zapier](https://zapier.com/app/dashboard), vous pouvez donc configurer des déclencheurs qui envoient vos soumissions de formulaires vérifiées à l'une des 500+ applications de leur catalogue.

* Tous les emails de notification sont envoyés depuis `team@netlify.com`, et toute réponse à une notification ira à cette adresse. Si vous souhaitez répondre à un soumissionnaire de formulaire, vous devrez entrer son adresse manuellement.

* Les formulaires Netlify peuvent également recevoir des téléchargements de fichiers via des soumissions de formulaires :).

Pour ce faire, ajoutez une entrée avec `type="file"` à n'importe quel formulaire. Lorsqu'un formulaire est soumis, un lien vers chaque fichier téléchargé sera inclus dans les détails de la soumission du formulaire.

* Netlify est limité à 100 soumissions par mois et 10 Mo de téléchargements par mois pour le plan GRATUIT. Si vous voulez plus, vous devrez passer à un plan supérieur.

![Image](https://www.freecodecamp.org/news/content/images/2019/09/1_XaWaJi_I6eQq06_ogPEHUg.png align="left")

*les soumissions de formulaires dans le panneau d'administration*

Et c'est tout !!

### CODE FINAL DU FORMULAIRE HTML

```html
<!--formspree.html-->

<form action="https://formspree.io/you@email.com" method="POST">
   <input type="hidden" name="_subject" value="Formulaire de Bolaji">                 
   <input type="hidden" name="_next" value="/thanks.html" >
   <div class="form-group">
      <label>Nom :</label>
      <input type="text" class="form-control" id="name" placeholder="Nom">
      <div class="invalid-feedback">
         Le nom doit comporter entre 2 et 20 caractères
      </div>
   </div>
   <div class="form-group">
      <label>Email :</label>
      <input type="text" class="form-control" id="email" placeholder="Adresse email">
      <div class="invalid-feedback">
         Entrez une adresse email valide
      </div>
   </div>
   <div class="form-group">
      <label>Téléphone :</label>
      <input type="text" class="form-control" id="phone" placeholder="Numéro de téléphone">
      <div class="invalid-feedback">
         Entrez un numéro valide
      </div>
   </div>
   <input type="submit" value="Envoyer" class="btn btn-info btn-block">
</form>
```

```html
<!--netlify.html-->

<form action="/thanks.html" name="formulaire de Bolaji" method="POST" data-netlify="true">
   <div class="form-group">
      <label>Nom :</label>
      <input type="text" class="form-control" id="name" placeholder="Nom">
      <div class="invalid-feedback">
         Le nom doit comporter entre 2 et 20 caractères
      </div>
   </div>
   <div class="form-group">
      <label>Email :</label>
      <input type="text" class="form-control" id="email" placeholder="Adresse email">
      <div class="invalid-feedback">
         Entrez une adresse email valide
      </div>
   </div>
   <div class="form-group">
      <label>Téléphone :</label>
      <input type="text" class="form-control" id="phone" placeholder="Numéro de téléphone">
      <div class="invalid-feedback">
         Entrez un numéro valide
      </div>
   </div>
   <input type="submit" value="Envoyer" class="btn btn-info btn-block">
</form>
```

### CONCLUSION

Une chose à noter à propos de Formspree est que la version gratuite laisse votre adresse email exposée aux scrapers et aux bots, vous pourriez donc vouloir configurer une adresse email temporaire jetable pendant que vous l'utilisez. Si vous souhaitez masquer votre adresse email par défaut, vous devrez passer à un plan supérieur.

Voulez-vous une pratique supplémentaire ? Regardez cette vidéo tutorielle ci-dessous par [Brad Traversy](https://medium.com/u/861216ad5921) et apprenez comment ajouter un formulaire de contact ou tout autre type de formulaire à votre site web en utilisant la fonctionnalité de formulaire Netlify, y compris les téléchargements de fichiers et le filtrage de spam. [Guide complet + code pratique]

%[https://www.youtube.com/watch?v=6ElQ689HRcY] 

### Liens utiles

* [netlify.com/docs/form-handling](https://hashnode.com/util/redirect?url=https://www.netlify.com/docs/form-handling/)

* [forestry.io/blog/5-ways-to-handle-forms-on-..](https://hashnode.com/util/redirect?url=https://forestry.io/blog/5-ways-to-handle-forms-on-your-static-site/)

* [gridsome.org/docs/guide-forms](https://hashnode.com/util/redirect?url=https://gridsome.org/docs/guide-forms/)

* [zeit.co/guides/deploying-react-forms-using-..](https://hashnode.com/util/redirect?url=https://zeit.co/guides/deploying-react-forms-using-formspree-with-zeit-now)

* [zeit.co/guides/deploying-statickit-with-zei..](https://hashnode.com/util/redirect?url=https://zeit.co/guides/deploying-statickit-with-zeit-now)

Merci d'avoir lu !