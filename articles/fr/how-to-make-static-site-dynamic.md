---
title: Comment rendre votre site statique dynamique
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-03-23T19:00:00.000Z'
originalURL: https://freecodecamp.org/news/how-to-make-static-site-dynamic
coverImage: https://www.freecodecamp.org/news/content/images/2020/03/article-cover.jpg
tags:
- name: Productivity
  slug: productivity
- name: Web Development
  slug: web-development
seo_title: Comment rendre votre site statique dynamique
seo_desc: 'By Ondrej Polesny

  A static site seems like a good fit for a small and steady project, right? Like
  one that does not require any advanced features or interaction with users. But how
  can you leverage the performance benefits and still have your static ...'
---

Par Ondrej Polesny

Un site statique semble être un bon choix pour un petit projet stable, n'est-ce pas ? Comme un projet qui ne nécessite pas de fonctionnalités avancées ou d'interaction avec les utilisateurs. Mais comment pouvez-vous tirer parti des avantages de performance et avoir toujours un site statique dynamique, personnalisé et interactif ?

Chaque fois que je mentionne un "site statique" à des développeurs qui n'ont pas encore travaillé avec des générateurs de sites statiques, ils les critiquent. Le mot à la mode fonctionne contre moi et ne décrit pas vraiment ce que vous obtenez si vous décidez d'utiliser un générateur de site statique (comme Gatsby ou Gridsome).

Alors, je leur explique comment tout cela fonctionne, y compris les reconstructions automatiques lorsque le contenu ou la mise en œuvre change. Ils ont toujours le même commentaire :

> "C'est bien et tout, mais la pré-génération du site ne fonctionnera pas pour des scénarios dynamiques comme le commerce électronique ou la personnalisation. Ainsi, c'est bon seulement pour les petits projets."

Et ce n'est tout simplement pas vrai. Je vais vous montrer pourquoi.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/site-timeline.png)

Il existe deux façons de rendre un site statique dynamique :

* pendant la pré-génération du site
* par les interactions des utilisateurs sur le site

Je devrais expliquer cela en utilisant un site web réel. Récemment, j'ai été confronté à la tâche de créer un site de mariage. Je sais, il existe des milliers de modèles simples pour cela. Mais travaillant dans l'IT, les gens s'attendent implicitement à ce que le site soit à la pointe de la technologie. Alors j'ai cédé. Je vais leur montrer.

Pour la partie mise en œuvre, j'ai décidé d'utiliser le générateur de site statique Gridsome car je préfère Vue.js à React. J'utiliserai un [CMS headless](http://bit.ly/38aGvfn) pour stocker le contenu et deux fonctions serverless pour gérer l'interaction des utilisateurs.

_Préférez-vous la vidéo ? Regardez la_ [_série Twitch sur YouTube_](http://bit.ly/2TbMo7D)_. Et assurez-vous de_ [_me suivre sur Twitch_](https://twitch.tv/ondrabus) _pour ne pas manquer tous les prochains streams._

## Contenu dynamique pendant la pré-génération du site

J'ai rassemblé toutes les informations que je connais avant de construire le site web. Je sais qui je veux inviter. Je sais quand l'événement a lieu et je sais qui je vais épouser. Tout comme vous savez quels produits vous voulez vendre ou quels services vous voulez offrir sur votre site.

Avec cela en tête, j'ai créé un ensemble de modèles de contenu pour mon site :

* Invité
* Hébergement
* Section
* Élément de la chronologie

Et voici à quoi ils ressemblent dans la conception réelle du site :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/wedding-site-1-.png)

Parce que je connais tous les invités, j'ai utilisé le contenu du CMS headless pour (automatiquement) générer une page séparée pour chaque invité (consultez l'étiquette URL personnalisée sur l'image). En conséquence, au moment de la construction, les composants connaissent le contexte de l'invité. Imaginez les possibilités de personnalisation - je peux même retourner un 404 pour certains de mes parents les moins préférés.

J'ai effectivement utilisé cela pour afficher des salutations personnalisées et uniquement les éléments de la chronologie pertinents.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/salutation.png)

Si vous construisiez un site de commerce électronique, vous pourriez implémenter une page de produit qui affiche une liste de produits similaires. Vous lieriez probablement également aux services pertinents pour les produits que votre entreprise offre. Vous connaissez tous les détails nécessaires au moment de la construction.

### La modélisation du contenu est la clé pour les sites pré-construits

J'ai identifié trois modèles de contenu pour mon site, mais généralement, il y en a beaucoup plus. Une bonne façon d'aborder la modélisation du contenu est de regarder les wireframes de votre futur site. Il ne s'agit pas seulement de savoir comment mettre les données dans le CMS, vous devez penser à :

* **Comment le contenu va-t-il être affiché et consommé ?**  
Prenons les produits et les catégories par exemple. Dans la plupart des cas, vous les trouverez dans une relation N:N, mais je vise ici le côté mise en œuvre des choses. Pensez à la complexité des requêtes de données. Ajuster les modèles de contenu pour mieux représenter la structure réelle du site peut grandement aider à la mise en œuvre.  
Dans mon exemple, les éléments de la chronologie sont liés aux invités (1:N), ce qui permet une mise en œuvre simple tout en gardant la gestion du contenu directe. Comme réorganiser l'ordre des éléments.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/linked-items.png)

* **Comment le contenu est-il lié à d'autres éléments de contenu ?**  
Quelle est la relation entre les produits, les packs de produits, les catégories, les offres spéciales ou les réductions ? Les réponses à ces questions vous aideront à choisir le bon outil pour connecter les éléments de contenu comme la Taxonomie ou les Éléments liés.
* **Comment le contenu va-t-il être créé ?**  
Les éditeurs comprendront-ils la structure du contenu que vous avez mise en place ? De plus, dans la plupart des cas, ils n'ont pas accès à l'ensemble des projets, mais seulement aux parties qui les concernent. Votre structure permet-elle un niveau de granularité des permissions suffisant ? Vos modèles de contenu sont-ils suffisamment restrictifs pour éviter les problèmes de contenu manquant sur le site en direct ?

Il y a beaucoup plus à dire sur la modélisation du contenu. Si vous êtes intéressé, consultez [cette excellente série sur la modélisation du contenu](https://medium.com/@meandmyrobot/content-modelling-in-kentico-kontent-part-1-f820ad45d98a) écrite par [Michael Kinkaid](https://twitter.com/meandmyrobot).

## Composants dynamiques

Avec les bons modèles de contenu, nous pouvons générer le site statique. En fait, pré-généré est probablement une meilleure étiquette pour cela. Son contenu n'est pas ancien et statique - chaque changement de contenu reconstruira effectivement le site.

Mais que faire si nous devons interagir avec les visiteurs ? Parfois, nous devons obtenir des informations de leur part ou leur montrer un contenu différent en fonction de leurs actions. Dans ces cas, nous pouvons utiliser des composants dynamiques. Ils sont pré-initialisés avec des valeurs pendant la construction du site, mais ils peuvent continuer à interagir avec les systèmes backend en fonction des actions des visiteurs.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/dynamic-form.png)

Sur mon site web, j'ai un formulaire que les invités peuvent utiliser pour confirmer quel type d'hébergement les intéresse. Leur sélection doit être stockée dans le même élément de contenu Invité que j'ai créé initialement dans le CMS headless.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/implementation.png)

Je pourrais communiquer directement avec le CMS depuis le composant sur le site. Cependant, nous parlons ici de JavaScript côté client. Exposer la clé serait un problème de sécurité majeur même si je ne m'attends pas à ce que l'un de mes invités comprenne ce qu'est une clé de sécurité ou comment elle peut être mal utilisée. Donc, l'intermédiaire entre le site statique et le CMS est une fonction serverless.

### Composant réactif sur un site statique

Commençons par le composant. J'ai utilisé Vue.js et Gridsome comme SSG, mais le concept de composant dynamique est le même quel que soit le framework utilisé. Le CMS headless que j'ai utilisé ici est [Kontent](http://bit.ly/38aGvfn). Il a un niveau gratuit généreux, mais si vous aimez l'open-source (pour citer mon professeur d'université des systèmes d'exploitation "Je ne fais pas confiance à moins de voir son code") j'ai entendu dire que [Strapi](http://bit.ly/2POJ9Rk) est un bon choix.

#### Implémentation du composant

Au moment de la construction, le composant recevra les données initiales - les données que nous connaissons à ce moment précis. Si Michael a sélectionné l'une des options la semaine dernière et que nous reconstruisons le site aujourd'hui, nous connaissons sa sélection.

```xml
<RsvpAccommodation inviteeId="{GUID}" optionSelected="sleep_in_a_tent" howManyInvited="2" salutation="Michael" />
```

D'un autre côté, s'il n'a pas encore interagi avec le site, la sélection serait vide.

```xml
<RsvpAccommodation inviteeId="{GUID}" optionSelected="" howManyInvited="2" salutation="Michael" />
```

Le composant ressemble à ceci :

```js
<template>
    ...
    <input type="radio" name="option" value="not_interested" id="none" v-model="option" />
    <label for="none">Děkuji, nepotřebuji</label>
    <input type="radio" name="option" value="interested_in_booking_a_room" id="hotel" v-model="option" />
    <label for="hotel">Mám zájem o ubytování v okolí</label>
    <input type="radio" name="option" value="sleep_in_a_tent" id="tent" v-model="option" /><label for="tent">Mám zájem o přespání ve vlastním stanu</label>
    ...
</template>
<script>
export default {
    props: {
        salutation: String,
        inviteeId: String,
        howManyInvited: Number,
	    salutation: String,
        optionSelected: String
    },
    data: function(){
        option: this.optionSelected
    },
    ...
</script>
```

Vue.js surveille les propriétés de données utilisées. Lorsque Michael change sa sélection, l'événement de changement de données est déclenché. Notez que le nom de la propriété dans l'objet watch doit correspondre au nom de la propriété de données.

À ce moment-là, nous devons stocker sa sélection - nous formons les données et faisons une requête asynchrone à la fonction serverless - tout en utilisant le JS côté client.

```js
...
<script>
export default {
    ...
    watch: {
        option: function(newVal, oldVal) {
            let url = `{remote base URL}/action?id=${this.inviteeId}`;
            fetch(url, {
                method: 'POST',
                body: JSON.stringify({
                    option: this.option,
                })
            })
            .then(response => {
                if (response.status !== 200) {
                    alert("Impossible d'enregistrer, veuillez réessayer.");
                }
            });
         }
    }
}
</script>
```

### Implémentation de la fonction serverless

J'ai utilisé Netlify pour construire et déployer la fonction serverless. Si c'est votre première fonction Netlify, n'hésitez pas à consulter ma [vidéo d'introduction](https://youtu.be/0krLcVQjh28?t=623) où je montre comment configurer l'environnement de développement local Netlify.

Le CMS headless dispose de deux API. L'une pour la livraison des données - je l'ai utilisée pour obtenir toutes les données pendant la construction du site - et une autre pour la gestion des données. Dans la fonction serverless, j'ai besoin d'utiliser les deux API, donc j'ai ajouté l'ID du projet et la clé de l'API de gestion au fichier .env à la racine du projet des fonctions Netlify :

```js
KONTENT_PROJECT_ID={project ID}
KONTENT_CM_KEY={management API key}
```

Et il est toujours plus agréable d'utiliser un SDK que de lutter avec des appels d'API REST bruts :

```js
npm i @dotenv --save
npm i @kentico/kontent-delivery --save
npm i @kentico/kontent-management --save
```

Le début de la fonction ressemble à ceci :

```js
require("dotenv").config();
const KontentDelivery = require('@kentico/kontent-delivery')
const KontentManagement = require('@kentico/kontent-management')
```

La fonction est plus ou moins accessible publiquement - son URL est stockée dans le code JS côté client en texte brut - donc nous devons d'abord effectuer quelques vérifications élémentaires. Chaque requête à cette fonction doit contenir un paramètre ID dans la chaîne de requête qui contient un identifiant d'un invité existant. C'est la personne qui a rempli le formulaire. Si l'ID est manquant ou invalide, nous retournons 404.

```js
exports.handler = async (event, context, callback) => {
  const { KONTENT_PROJECT_ID, KONTENT_CM_KEY } = process.env;
  const deliveryClient = new KontentDelivery.DeliveryClient({ projectId: KONTENT_PROJECT_ID });
  let id = event.queryStringParameters.id;
  const invitee = await deliveryClient.items()
                    .type('invitee')
                    .elementsParameter(['accommodation'])
                    .equalsFilter('system.id', id)
                    .toPromise();
  if (invitee.items == null || invitee.items.length == 0)
  {
    return {
      statusCode: 404,
      body: `Invité non trouvé`
    };
}
```

La requête deliveryClient est limitée à un seul élément - `accommodation`. C'est parce que les informations du formulaire ne sont pas stockées dans le modèle _Invité_ mais dans un élément lié de type _Hébergement_.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/nested-type.png)

Le modèle de contenu Hébergement correspond directement au formulaire sur le site web :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/accommodation-map.png)

Nous voulons stocker les données que nous avons obtenues du JS côté client comme un nouvel enregistrement. La mise à jour de l'élément de contenu existant est également une possibilité, mais nous perdrions tout l'historique si les invités changeaient leur sélection à l'avenir.

Tout d'abord, nous notons l'ID de l'élément de contenu _Hébergement_ existant et initialisons le client de gestion de contenu.

```js
let accommodationId = invitee.items[0].accommodation.value[0].system.id;
const client = new KontentManagement.ManagementClient({ projectId: KONTENT_PROJECT_ID, apiKey: KONTENT_CM_KEY });
```

Ensuite, nous devons créer une nouvelle variante linguistique de l'élément de contenu _Hébergement_. Même s'il n'y a qu'une seule langue dans le projet, le contenu est stocké dans un compartiment séparé étiqueté avec ce nom de code de langue. Cela garantit une transition fluide si vous décidez d'ajouter des langues supplémentaires à l'avenir.

```js
await client.createNewVersionOfLanguageVariant()
      .byItemId(accommodationId)
      .byLanguageCodename('default')
      .toPromise();
```

Ce code fait la même chose que si vous cliquez sur "Créer une nouvelle version" dans l'interface utilisateur.

![Image](https://www.freecodecamp.org/news/content/images/2020/03/create-new-version.png)

Ensuite, nous devons remplir la variante avec des données. Les données arrivent sous forme de JSON dans le corps de la requête.

```js
let accommodation = JSON.parse(event.body);
await client.upsertLanguageVariant()
    .byItemId(accommodationId)
    .byLanguageCodename('default')
    .withElements([{
        element: { codename: 'option' },
        value: [{ codename: accommodation.option }]
     }])
    .toPromise();
```

La dernière étape consiste à publier la nouvelle variante :

```js
await client.publishOrScheduleLanguageVariant()
    .byItemId(accommodationId)
    .byLanguageCodename('default')
    .withData()
    .toPromise();
return { statusCode: 200, body: `OK` }
```

#### Problèmes de CORS avec Netlify

Même si vous exécutez les fonctions et le site statique localement, vous rencontrerez un problème de CORS car les deux implémentations sont servies à partir de ports différents. Sur toutes les réponses de la fonction serverless, vous devez retourner l'en-tête "Access-Control-Allow-Origin".

Netlify a un moyen simple de gérer cela globalement via le fichier de configuration `netlify.toml` à la racine du projet des fonctions :

```js
[build]
  Functions = "lambda"
[[headers]]
  for = "/*"
  [headers.values]
    Access-Control-Allow-Origin = "*"
```

#### Anciennes données après l'actualisation de la page

Maintenant, le composant réagit aux actions des visiteurs. Cependant, l'état initial (qui sera également affiché si le visiteur actualise la page) provient toujours de la construction du site statique. Si un visiteur change sa sélection, le changement est enregistré dans le CMS, mais le site n'est pas reconstruit.

Il ne serait pas efficace de reconstruire tout le site après chaque interaction utilisateur. Même si nous le faisions, cela prendrait quelques secondes à minutes jusqu'à ce que la construction et le déploiement soient terminés.

Au lieu de cela, nous faisons une requête asynchrone lorsque le composant est rendu pour la première fois :

```js
<script>
...
    mounted: function () {
        let url = `${baseUrl}/delivery?id=${this.inviteeId}`;
        let response = fetch(`${remote base URL}/delivery?id=${this.inviteeId}`, { method: 'GET', mode: 'cors' })
            .then(response => response.json())
            .then(accommodationObj => {
                this.option = accommodationObj.option;
            });
    },
...
</script>
```

Le composant sera pré-initialisé avec des données pendant la pré-construction du site. Mais une fois le composant créé, il obtiendra des données fraîches du CMS en utilisant une autre fonction serverless. Cette fonction est très similaire à la précédente :

```js
exports.handler = async (event, context, callback) => {
  const { KONTENT_PROJECT_ID } = process.env;
  let id = event.queryStringParameters.id;
  const deliveryClient = new KontentDelivery.DeliveryClient({ projectId: KONTENT_PROJECT_ID });
  const invitee = await deliveryClient.items()
                    .queryConfig({ waitForLoadingNewContent: true })
                    .type('invitee')
                    .elementsParameter(['accommodation', 'option'])
                    .equalsFilter('system.id', id)
                    .toPromise();
  if (invitee.items == null || invitee.items[0] == null)
  {
    return {
      statusCode: 404,
      body: `Invité non trouvé`
    };
  }
  return {
	statusCode: 200,
	body: JSON.stringify({
		option: invitee.items[0].accommodation.value[0].codename
	})
  };
};
```

Dans ce cas, nous devons ajouter une configuration supplémentaire à la requête de données - `waitForLoadingNewContent`. Le contenu provenant du CMS headless est mis en cache et livré via CDN, donc nous pourrions obtenir un contenu obsolète s'il a été modifié au cours des dernières minutes. L'option de configuration garantit que la réponse contiendra toujours des données fraîches.

Ainsi, le processus global d'un composant dynamique sur un site statique ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2020/03/dynamic.png)

## C'est rapide et interactif

Vous voyez, le grand avantage des sites statiques est que toutes les informations disponibles au moment de la construction peuvent être servies sous forme de fichiers statiques, ce qui est rapide et facilement scalable en utilisant un CDN.

Mais ils peuvent également fournir une fonctionnalité dynamique qui peut être livrée via des fonctions serverless - également peu coûteuses et facilement scalables.

Si vous prenez mon site web comme exemple - au lieu de devoir déployer toute l'application dans le cloud, j'ai seulement eu besoin d'héberger un ensemble de petits fichiers statiques et deux minuscules fonctions serverless. Et je suis également en mesure de scaler ces fonctions indépendamment.

Les sites statiques ne sont peut-être pas le choix ultime pour le développement web, mais pour de nombreux projets, ils apportent des avantages en termes de clarté, de performance et de sécurité ainsi que des coûts de maintenance réduits. Quelle est votre expérience ? [Faites-le moi savoir.](http://bit.ly/38kyjt6)

Assurez-vous de consulter également mes [streams Twitch](http://bit.ly/3akWp8l) et ma [chaîne YouTube](http://bit.ly/2TbMo7D) sur le développement web.