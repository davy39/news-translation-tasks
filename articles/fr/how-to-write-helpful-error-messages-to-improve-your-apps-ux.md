---
title: Comment écrire des messages d'erreur utiles pour améliorer l'expérience utilisateur
  de votre application
subtitle: ''
author: Andrico Karoulla
co_authors: []
series: null
date: '2021-04-05T22:07:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-write-helpful-error-messages-to-improve-your-apps-ux
coverImage: https://cdn-media-2.freecodecamp.org/w1280/60622fcb9618b008528a924c.jpg
tags:
- name: error handling
  slug: error-handling
- name: JavaScript
  slug: javascript
- name: user experience
  slug: user-experience
- name: ux design
  slug: ux-design
seo_title: Comment écrire des messages d'erreur utiles pour améliorer l'expérience
  utilisateur de votre application
seo_desc: 'Gone are the days of useless and generic error messaging.


  Screenshot taken moments before a rage-quit

  If you''re here, you''re likely concerned with making your user-facing products
  as delightful as possible. And error messaging plays an important rol...'
---

Les jours des messages d'erreur génériques et inutiles sont révolus.

![Un message d'erreur générique affichant : "Oups, quelque chose s'est mal passé. Veuillez réessayer plus tard"](https://www.freecodecamp.org/news/content/images/2021/03/ykhg3yuzq8931--1-.png)
_Capture d'écran prise quelques instants avant un rage-quit_

Si vous êtes ici, vous vous souciez probablement de rendre vos produits destinés aux utilisateurs aussi agréables que possible. Et les messages d'erreur jouent un rôle important dans ce domaine. 

Avoir des messages d'erreur utiles peut grandement contribuer à rendre une situation frustrante pour un utilisateur final aussi agréable que possible.

Cet article est divisé en deux parties. La première construit un contexte autour des messages d'erreur et de leur importance. Cette section devrait être utile, que vous soyez développeur JavaScript ou non.

La deuxième partie est un court guide pour vous aider à commencer à gérer vos propres messages d'erreur.

## **L'état actuel des messages d'erreur**

Dans un monde parfait, les messages d'erreur seraient redondants et les utilisateurs pourraient utiliser tout ce que vous avez construit sans problème. Mais des erreurs se produiront, et vos utilisateurs finaux les rencontreront. 

Ces erreurs peuvent provenir de :

* Échec de validation
* Échecs côté serveur
* Limitation de débit
* Code défectueux
* Actes de dieu

Et lorsque les choses tournent mal, souvent le message d'erreur côté client prend forme de l'une de ces deux manières :

* Erreurs génériques sans information significative, par exemple `Quelque chose s'est mal passé, veuillez réessayer plus tard`
* Messages hyper spécifiques de la trace de la pile envoyée par le serveur, par exemple `Erreur 10x29183 : ligne 26 : erreur de mappage Object -> Int32`

Aucun de ces messages n'est utile pour nos utilisateurs finaux.

Pour nos utilisateurs, l'erreur générique peut créer un sentiment d'impuissance et de frustration. S'ils reçoivent un tel message, ils ne peuvent pas compléter une action et n'ont aucun moyen de savoir pourquoi l'erreur s'est produite et comment (ou si) ils peuvent la résoudre. Cela peut entraîner une perte de confiance de l'utilisateur final, une perte de client, ou un avis négatif.

D'autre part, les messages d'erreur hyper-spécifiques sont une abstraction qui fuit et ne devraient pas être vus par nos utilisateurs finaux.

Tout d'abord, ces types d'erreurs fournissent des informations d'implémentation sur notre logique côté serveur. Est-ce une préoccupation de sécurité ? probablement ? Je ne suis pas un testeur de pénétration.

Deuxièmement, si nous sommes dans le domaine de la création d'expériences utilisateur engageantes, (et pourquoi ne le seriez-vous pas ?) nos messages d'erreur devraient sembler humains et être orientés service. C'est un sentiment partagé dans un certain nombre de ressources que j'ai rencontrées, dont beaucoup sont incluses dans une section de lecture supplémentaire à la fin.

## **Pourquoi devrais-je créer des messages d'erreur sensés ?**

### Pour aider à maintenir la santé mentale des développeurs

Chasser les bugs est difficile, et scanner les logs est fastidieux. Parfois, nous avons du contexte sur pourquoi les choses ont échoué, et d'autres fois non. Si un utilisateur final signale un bug, il est important qu'il puisse nous présenter autant d'informations utiles que possible.

Un rapport d'un utilisateur qui dit :

`Salut, j'utilisais l'application hier soir en mettant à jour mon profil et tout à coup ça a arrêté de fonctionner. L'erreur disait quelque chose sur une erreur de validation, mais je ne sais pas ce que ça signifie`

est beaucoup moins utile que :

`Salut, j'utilisais l'application hier soir en mettant à jour mon profil et tout à coup ça a arrêté de fonctionner. L'erreur disait "Nous avons eu des problèmes pour mettre à jour vos détails. Votre adresse doit être située dans l'UE" mais je vis en Angleterre`

Cela nous fait gagner du temps et réduit les fausses pistes. Un message d'erreur clair et spécifique peut également aider un utilisateur final à comprendre ce qu'il a fait de mal et lui permettre de corriger son erreur.

### Pour aider à maintenir la santé mentale de l'organisation

Les messages d'erreur sensés offrent également des avantages au niveau de l'organisation. Pour ceux qui travaillent dans de grandes entreprises, la copie/les messages peuvent être la responsabilité d'un département entièrement séparé. Plus il y a d'endroits dans le code qui nécessitent des changements de copie, plus il est facile pour la copie de se désynchroniser avec les directives de marque de votre entreprise. 

Inversement, garder tous vos messages d'erreur dans une seule source rend beaucoup plus facile pour ceux qui possèdent la copie d'adhérer à ces directives de marque.

D'autres départements, comme l'équipe de support, peuvent être submergés de tickets de support des utilisateurs. Si vous êtes ingénieur, pourquoi ne pas contacter votre équipe de support pour voir combien de tickets de support pourraient être évités avec des messages d'erreur améliorés. 

Résoudre les problèmes avec votre messagerie lorsqu'un utilisateur remplit incorrectement un formulaire, a des données manquantes ou n'a pas les permissions pour une action spécifique pourrait avoir un impact positif sur la vie de l'équipe de support.

### Pour aider à maintenir la santé mentale des utilisateurs finaux

En fournissant des messages d'erreur sensés, nous espérons ne pas laisser nos utilisateurs finaux se sentir impuissants. 

Comme décrit précédemment, nos messages doivent être _orientés service_. Ils doivent guider notre utilisateur sur la façon de compléter son processus, ou au moins lui faire savoir où il peut aller et obtenir de l'aide si le problème est hors de son contrôle.

Dans le livre de Jon Yablonski, les Lois de l'UX, il décrit un concept psychologique appelé la Règle du pic-final :

> _Les gens jugent une expérience largement basée sur ce qu'ils ont ressenti à son pic et à sa fin plutôt que sur la somme totale ou la moyenne de chaque moment de l'expérience_

Dans le contexte de cet article, si les gens deviennent si frustrés qu'ils quittent votre site en rage, leur souvenir durable de votre application est de la frustration qu'ils ont ressentie à l'utiliser. 

Les messages d'erreur jouent un grand rôle dans la prévention de cela, car ils peuvent agir comme le dernier gardien empêchant un utilisateur qui est simplement bloqué de devenir si frustré qu'il quitte votre application.

Si quelqu'un utilise votre produit à des fins transactionnelles comme acheter un billet d'avion ou faire des achats en ligne, et qu'il est arrêté net dans ses tracks pendant une tâche sans moyen de continuer, la probabilité qu'il quitte votre site pour un autre augmente considérablement. Un autre client perdu.

Bien que cela soit entièrement anecdotique, j'ai souvent quitté des sites en rage parce que je ne savais pas comment compléter un processus - soit rien ne se passait lorsque je cliquais sur un bouton, soit je continuais à recevoir des messages d'erreur vagues. 

Sauf si ces sites/applications sont l'une de ces rares plateformes omniprésentes (comme Google, Instagram, Apple), je ne les ai probablement pas utilisés depuis. Je suis sûr que vous pouvez même vous souvenir d'un moment où cela vous est arrivé. En fait, je vous invite ouvertement à envoyer des images de messages d'erreur horribles via [Twitter](https://twitter.com/andricokaroulla?lang=en)

L'utilisation de messages d'erreur sensés peut aider à atténuer cette frustration si quelque chose ne va pas. Étonnamment, la création d'un message d'erreur utile ne nécessite qu'une poignée de qualités.

## Qu'est-ce qui fait un bon message d'erreur ?

Tiré de [Microcopy: A complete guide](https://www.microcopybook.com/). Un message d'erreur utile doit satisfaire ces qualités :

* Expliquer clairement qu'il y a un problème
* Expliquer quel est le problème
* Si possible, fournir une solution afin que l'utilisateur puisse compléter le processus, ou
* Les orienter vers l'endroit où ils peuvent obtenir de l'aide
* Rendre un scénario frustrant aussi agréable que possible

Cela peut sembler beaucoup à couvrir avec seulement quelques phrases, mais voici quelques exemples de ce que je considère être de bons messages d'erreur :

* Nous avons limité le nombre de fois où vous pouvez réinitialiser votre mot de passe chaque heure. Vous pouvez réessayer plus tard.
* Veuillez vous connecter pour voir ce profil
* Nous n'avons pas pu créer votre profil, seuls les résidents du Royaume-Uni peuvent utiliser notre application.

Il est worth de noter que je ne suis pas un chercheur/designer UX, juste un développeur frontend avec un vif intérêt pour l'UX. Il se peut que mes exemples ci-dessus ne répondent pas aux exigences de votre projet ou organisation. 

Cela dit, si vous êtes un ingénieur frontend, améliorer la messagerie d'erreur de votre organisation constitue une excellente opportunité de monter en compétences et de collaborer avec vos collègues UX.

## Comment puis-je commencer à écrire des messages d'erreur sensés ?

J'ai open-sourcé un outil simple appelé `sane-error-messages`. L'exécution de l'outil générera un tout nouveau dépôt conçu pour héberger vos messages d'erreur par défaut. Vous pouvez ajuster les valeurs par défaut, ajouter ou supprimer des messages, puis les publier pour les consommer dans vos applications destinées aux clients.

`sane-error-messages` fonctionne en agrégeant tous vos messages dans un seul objet JavaScript. La clé est un code d'erreur, et la valeur est un message correspondant. 

Les codes d'erreur doivent être les mêmes codes que vous recevez de votre serveur, tels que `POSTS_NOT_FOUND` ou `CONFLICTING_USER_RECORD`. Votre dépôt de messages d'erreur expose une fonction pour obtenir votre message d'erreur à partir d'un code d'erreur. 

Cette approche a été inspirée par la façon dont des outils comme [Cypress](https://www.freecodecamp.org/news/p/009d4c55-b3e6-4e48-b186-541f5959af8c/*https://github.com/cypress-io/cypress/blob/develop/packages/server/lib/errors.js*) gèrent leurs messages d'erreur.

Tant que votre serveur retourne des codes d'erreur prévisibles, l'implémentation côté serveur n'a pas d'importance. La séquence suivante est juste une façon d'implémenter _`sane-error-messages`_

![Un diagramme de séquence montrant le processus d'affichage d'un message d'erreur sensé.](https://www.freecodecamp.org/news/content/images/2021/03/Screenshot-2021-03-15-at-21.41.28.png)
_Avoir un dépôt séparé devient plus important avec le nombre d'applications destinées aux utilisateurs que vous avez._

En bref :

* L'utilisateur "voit tous les produits"
* Le frontend fait une requête réseau
* La requête réseau échoue et retourne un code d'erreur "USER_NOT FOUND"
* Le frontend demande le message d'erreur correspondant à votre package `error-messages`.
* Le frontend applique toute information contextuelle pertinente
* Le frontend affiche cette information à l'utilisateur final.

Si vous voulez essayer quelque chose de pratique, vous pouvez jouer avec ce [CodeSandbox](https://codesandbox.io/s/amazing-platform-dxtjc?file=/src/App.js). Le CodeSandbox envoie une requête à un serveur mock qui retourne 1 des 12 codes d'erreur aléatoirement. 

Le côté client utilisera le code d'erreur pour récupérer un message d'erreur sensé du dépôt de messages d'erreur. Le côté client affiche ensuite le message d'erreur à l'utilisateur. Si le code n'a pas de message spécifié, le message générique de secours s'affiche (et il est nul).

![Un gif de messages d'erreur pertinents s'affichant sur un bac à sable de code](https://www.freecodecamp.org/news/content/images/2021/03/ezgif.com-gif-maker--2-.gif)
_Quelques messages d'erreur sensés dans la nature_

## Comment configurer vos messages d'erreur

Note : Vous pouvez trouver le [dépôt ici](https://github.com/andrico1234/sane-error-messages#readme). Si vous rencontrez des problèmes pendant le processus de tutoriel, vous pouvez créer un problème GitHub.

Commencez par exécuter

`yarn global add sane-error-message`

puis

`sane-error-messages create <dirName>`

pour échafauder votre projet. Cela créera un tout nouveau module pour vous afin de personnaliser avec vos messages d'erreur par défaut. 

Votre nouveau module utilise `tsdx` sous le capot pour gérer tous les scripts de gestion de module, tels que l'exécution, la construction et les tests.

Vous pouvez en savoir plus sur [tsdx ici](https://www.freecodecamp.org/news/p/009d4c55-b3e6-4e48-b186-541f5959af8c/*https://tsdx.io/*).

En bref, le contenu de votre nouveau package ressemblera à ceci :

```typescript
/* errorCodes.ts: Le fichier qui définit chaque code d'erreur comme */
const USER_NOT_ADMIN = '403_USER_NOT_ADMIN'

/* defaultErrorMessages.ts: Associe chaque code à un message par défaut */
const errorCodes {
  // vos codes et messages vont ici...
  [USER_NOT_ADMIN]: "Nous sommes désolés, seuls les administrateurs ont accès à "
}

/* ErrorMessages.ts: La classe que vous utiliserez pour instancier votre objet de messages d'erreur dans le projet consommateur */
class ErrorMessages {
  // Vous pouvez remplacer les messages par défaut par des messages plus spécifiques
  constructor: (customErrorMessages: Partial<Record<string | number, string>>): ErrorMessages;

  // Passez un code d'erreur pour obtenir votre message personnalisé
  getErrorMessage: (code: string | number, fallbackMessage?: string): string;

  // Vérifie si l'argument est un code d'erreur valide et agit comme un garde pour les valeurs non-ErrorCode
  isErrorCode(code: string | number): boolean;

  // Retourne l'objet errorCodes avec vos messages personnalisés
  messages: Record<ErrorCode, string>
}

type ErrorCode = ValueOf<errorCodes>
```

## Comment consommer vos messages d'erreur

Si vous avez créé un dépôt avec le nom `custom-error-messages` et que vous l'avez publié sur npm, vous pourriez le consommer dans vos applications en faisant ce qui suit :

```typescript
import { ErrorMessages } from 'custom-error-messages';

const customErrorMessages = {
  '400_validation': 'Veuillez entrer les champs de votre formulaire correctement',
};

// Initialisez votre objet errorMessages avec vos messages personnalisés
const errorMessages = new ErrorMessages(customErrorMessages);

function riskyFunction() {
  try {
    // Lance une erreur 
    await boom();
  } catch (err) {
    // Obtenez le code d'erreur que notre serveur a envoyé
    const { code } = err;
		
    // Obtenez le message correspondant au code
    const message = errorMessages.getErrorMessage(code);
    
    // Affichez le message au client
    displayNotification(message);
  }
}
```

Vous pouvez ensuite prendre tous les codes d'erreur que votre serveur retourne et leur appliquer des messages correspondants.

Une fois que vous êtes prêt, vous pouvez publier votre outil sur NPM, puis le consommer à partir de vos applications destinées aux clients.

## **Conclusion**

J'espère que vous avez apprécié apprendre un aspect souvent négligé du développement web. 

J'ai fait beaucoup de lectures pour en apprendre davantage sur les messages d'erreur et j'ai partagé certaines de mes ressources préférées ci-dessous. Certaines sont des livres et d'autres sont des articles courts, mais ils valent tous votre temps.

Vous pouvez également me contacter si une partie du tutoriel n'était pas claire, ou si vous pensez que je peux simplifier les choses. Merci pour votre lecture.

## FAQs

### Pourquoi le serveur ne peut-il pas simplement retourner ces messages ?

Le serveur ne devrait pas être concerné par la logique côté client. Mais si vous avez la chance de travailler avec une API qui donne des codes d'erreur utiles avec chaque requête échouée, alors vous êtes presque arrivé.

### Devrai-je créer une instance de error-messages pour chaque consommateur d'API ?

Pas nécessairement. Parce que ce package peut prendre une liste de messages et de codes par défaut, tant qu'il est synchronisé avec les APIs, vos frontends pourront consommer le même package. 

Dans chaque instance côté client, vous pouvez passer des codes d'erreur supplémentaires, ou remplacer les messages existants pour adapter votre messagerie frontend.

### Je pense que ce package devrait avoir X ou faire Y différemment

Je l'utilise en interne dans mon travail, et c'est un domaine de problème dans lequel je suis très nouveau. J'adorerais entendre vos suggestions ou améliorations pour l'architecture globale ou l'ensemble des fonctionnalités de _`sane-error-messages`._

## **Lectures complémentaires**

**Microcopy: A Complete Guide**  
J'ai mentionné ce livre un peu plus tôt, et c'est l'un de mes préférés lorsqu'il s'agit de rendre mes produits destinés aux utilisateurs beaucoup plus personnalisés.

L'auteure du livre, Kinneret Yifrah, a gracieusement fourni un coupon pour une réduction de 10 %, vous pouvez l'acheter [ici](https://www.microcopybook.com/).

Code de coupon pour l'eBook : andrico-ebook

Code de coupon pour le bundle : andrico-bundle

**Error messaging guidelines: NN Group**  
Un [court article](https://www.nngroup.com/articles/error-message-guidelines/) sur l'importance des messages d'erreur sensés qui partage quelques conseils très utiles sur la façon de créer des messages d'erreur sensés.

En bref :

* Les erreurs doivent être exprimées en langage clair
* Indiquer quel est le problème
* Suggérer une solution

**Error Messages (Design basics): Microsoft**  
Un [article approfondi](https://docs.microsoft.com/en-us/windows/win32/uxguide/mess-error) qui couvre à la fois les directives de conception et les pratiques de messagerie

**Laws of UX**  
Un [court livre](https://www.amazon.co.uk/gp/product/149205531X/ref=as_li_tl?ie=UTF8&camp=1634&creative=6738&creativeASIN=149205531X&linkCode=as2&tag=calistheni02b-21&linkId=3f089ce27d59c4eeb48522be9ac52fb2) qui introduit comment une poignée de concepts psychologiques peuvent être utilisés pour améliorer l'UX de vos produits.