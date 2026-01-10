---
title: Améliorez les performances de votre site avec le Lazy-Loading et le Code-Splitting
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2018-04-06T06:44:18.000Z'
originalURL: https://freecodecamp.org/news/increase-the-performance-of-your-site-with-lazy-loading-and-code-splitting-87258bbfc89b
coverImage: https://cdn-media-1.freecodecamp.org/images/1*QbeGpWdpFKZLxJsbCFVfjw.jpeg
tags:
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: software development
  slug: software-development
- name: Web Design
  slug: web-design
- name: Web Development
  slug: web-development
seo_title: Améliorez les performances de votre site avec le Lazy-Loading et le Code-Splitting
seo_desc: 'By José M. Pérez

  How to use a High-Order Component to load what is needed, when needed.

  Componentization has marked a before and after in web development. The main advantages
  that are usually mentioned are reusability and modularization. Components a...'
---

Par José M. Pérez

#### Comment utiliser un composant d'ordre supérieur pour charger ce qui est nécessaire, quand c'est nécessaire.

La composantisation a marqué un avant et un après dans le développement web. Les principaux avantages qui sont généralement mentionnés sont la réutilisabilité et la modularisation. Les composants sont des pièces bien définies que nous pouvons utiliser pour construire nos sites, comme des briques de Lego. Il s'avère que cette structure de composants fournit une excellente base pour améliorer les performances de nos sites.

![Image](https://cdn-media-1.freecodecamp.org/images/1*QbeGpWdpFKZLxJsbCFVfjw.jpeg)
_[Photo par ](https://unsplash.com/photos/sX9_SHIqH4w" rel="noopener" target="_blank" title=")<a href="https://unsplash.com/@marvin_ronsdorf" rel="noopener" target="_blank" title=""></a>Marvin Ronsdorf_

Nous sommes explicites sur nos dépendances, donc nous savons quel code nous devons exécuter pour un composant spécifique. Le lazy-loading et le fractionnement des bundles peuvent avoir un impact énorme sur les performances de la page : moins de code demandé, analysé et exécuté. Et cela ne s'applique pas seulement à JavaScript, mais à tous les types d'actifs.

Je vois de nombreux sites qui pourraient tirer parti de cela. Je voulais montrer quelques techniques de base pour charger le contenu selon les besoins.

L'article utilisera Preact/React, mais les idées peuvent être appliquées à toute autre bibliothèque de composants.

Nous allons aborder plusieurs sujets.

Commençons !

### Modèles de composition

Dans un monde de composants, les composants ne sont pas seulement utilisés pour rendre des pixels réels à l'écran. Ils peuvent également envelopper des fonctionnalités qui sont transmises aux composants enfants.

Cela est généralement réalisé en utilisant des [composants d'ordre supérieur (HOC)](https://reactjs.org/docs/higher-order-components.html). Ces composants reçoivent un autre composant et ajoutent une certaine fonctionnalité, comme un comportement.

Si vous avez utilisé Redux, la fonction `connect` est un HOC qui reçoit votre composant non connecté. Vous pouvez trouver plus d'exemples dans « [React Higher Order Components in depth](https://medium.com/@franleplant/react-higher-order-components-in-depth-cf9032ee6c3e) » par Fran Guijarro.

```
const MyComponent = props => (  <div>    {props.id} - {props.name}  </div>);
```

```
// ...
```

```
const ConnectedComponent = connect(mapStateToProps, mapDispatchToProps)( MyComponent );
```

La fonction en tant que composant enfant (également connue sous le nom de « [Render Callback](https://reactpatterns.com/#render-callback) ») est un autre modèle utilisé dans des scénarios similaires. Il devient assez populaire ces jours-ci. Vous avez peut-être rencontré cela dans [react-media](https://github.com/ReactTraining/react-media) ou [unstated](https://github.com/jamiebuilds/unstated).

Regardez cet exemple tiré de react-media :

```
const MyComponent = () => (  <Media query="(max-width: 599px)">    {matches =>      matches ? (        <p>The document is less than 600px wide.</p>      ) : ( <p>The document is at least 600px wide.</p>      )    }  </Media>);
```

Le composant `Media` appelle ses enfants en passant un argument `matches`. De cette façon, les composants enfants n'ont pas besoin de connaître la requête média. La composantisation rend généralement les tests et la maintenance plus faciles.

### Améliorer les performances de nos sites en chargeant uniquement ce qui est nécessaire

Imaginez une page web typique. Vous pouvez consulter [Website Sameness](https://css-tricks.com/website-sameness/) ou [Web Design Trends: Why Do All Websites Look The Same?](https://www.friday.ie/journal/why-do-all-websites-look-the-same/) pour vous inspirer :) . La page d'exemple que nous allons utiliser contient plusieurs sections ou blocs :

* un en-tête (de nos jours, une grande image héroïque prenant toute la zone au-dessus de la ligne de flottaison)
* une section avec quelques images
* une autre section avec un composant lourd comme une carte
* un pied de page

![Image](https://cdn-media-1.freecodecamp.org/images/0*OwMzSYIliOOuMnAs.png)
_La structure de base d'une page que nous utiliserons comme exemple._

Cela, mappé en composants React, ressemblerait à ceci :

```
const Page = () => {  <div>    <Header />    <Gallery />    <Map />    <Footer />  </div>};
```

Lorsque l'utilisateur visite la page, il est très probable qu'il voie l'en-tête à l'écran. Après tout, c'est le composant le plus haut. Il est moins probable qu'il voie la galerie, la carte et le pied de page à moins qu'il ne fasse défiler.

La plupart du temps, vous incluriez tous les scripts et le CSS nécessaires pour rendre toutes les sections dès que l'utilisateur visite la page. Jusqu'à récemment, il était difficile de définir les dépendances d'un module et de charger ce qui était nécessaire.

Il y a des années, avant ES6, de grandes entreprises ont créé leurs propres solutions pour définir les dépendances et les charger selon les besoins. Yahoo a construit [YUI Loader](https://books.google.com/books?id=E7p-07kNfXYC&pg=PA65&lpg=PA65&dq=yahoo+yui+loader&source=bl&ots=UOcpQHdaRp&sig=AGTHNZvPYXWdU9lkj9klzTEa3ys&hl=en&sa=X&ved=0ahUKEwjn26Wti8PZAhUJDSwKHQOsCbIQ6AEIVDAG#v=onepage&q=yahoo%20yui%20loader&f=false) et Facebook a écrit [Haste, Bootloader et Primer](https://jmperezperez.com/facebook-frontend-javascript/).

Lorsque vous envoyez à l'utilisateur du code qui n'est pas nécessaire, vous gaspillez des ressources de votre côté et du côté de l'utilisateur. Plus de bande passante pour transférer les données, plus de CPU pour les analyser et les exécuter, et plus de mémoire pour les conserver. Et ces actifs voleront les ressources limitées d'autres actifs critiques qui en ont plus urgemment besoin.

Quel est l'intérêt de demander des ressources dont l'utilisateur n'aura pas besoin, comme des images que l'utilisateur n'atteindra pas ? Ou de charger un composant tiers comme une Google Map, avec tous ses actifs supplémentaires nécessaires pour rendre la chose ?

Un rapport de couverture de code, comme [celui fourni par Google Chrome](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage) **ne nous aidera pas beaucoup**. Le code JS sera exécuté et le CSS appliqué aux éléments qui ne sont pas visibles.

![Image](https://cdn-media-1.freecodecamp.org/images/0*aaC71xdnTv1M90uj.png)
_Onglet de couverture de code sur Google Chrome ([source](https://developers.google.com/web/updates/2017/04/devtools-release-notes#coverage" rel="noopener" target="_blank" title="))_

Comme pour tout le reste, **il y a des compromis avec le lazy-loading**. Nous ne voulons pas appliquer le lazy-loading à tout. Voici quelques points à prendre en compte.

* **Ne pas lazy loader au-dessus de la ligne de flottaison**. Dans la plupart des cas, nous voulons que le contenu au-dessus de la ligne de flottaison soit rendu dès que possible. Chaque technique de lazy-loading introduira un délai. Le navigateur doit exécuter le JS qui injecte le HTML dans le document, l'analyser et commencer à demander les actifs référencés.

![Image](https://cdn-media-1.freecodecamp.org/images/0*Og7qV0WrbJC8Thtl.png)

Où placer la ligne de flottaison ? C'est délicat, et cela dépendra du périphérique de l'utilisateur, qui varie considérablement, et de votre mise en page.

* **Lazy loader un peu plus tôt que nécessaire**. Vous voulez éviter de montrer des zones vides à l'utilisateur. Pour cela, vous pouvez charger un actif qui est nécessaire lorsqu'il est suffisamment proche de la zone visible. Par exemple, un utilisateur fait défiler vers le bas et si l'image à charger est, disons, 100px en dessous du bas de la fenêtre, commencez à la demander.

![Image](https://cdn-media-1.freecodecamp.org/images/0*SauGmZ_Equ1vw89o.png)

* **Contenu invisible dans certains scénarios**. Vous devez prendre en compte que le contenu chargé paresseusement ne sera pas affiché dans certaines situations :

1) Si le contenu chargé paresseusement n'a pas été chargé, il n'apparaîtra pas lors de l'impression de la page.

2) La même chose peut se produire lorsque la page est affichée dans des lecteurs RSS qui n'exécutent peut-être pas le JavaScript nécessaire pour charger le contenu.

3) En ce qui concerne le SEO, vous pourriez avoir des problèmes d'indexation du contenu chargé paresseusement sur Google. Au moment de la rédaction de cet article, Googlebot prend en charge IntersectionObserver. Il invoque son rappel avec des changements dans la fenêtre d'affichage au-dessus de la ligne de flottaison. Cependant, **il ne déclenchera pas le rappel pour le contenu en dessous de la ligne de flottaison**. Ainsi, **ce contenu ne sera pas vu ni indexé par Google**. Si votre contenu est important, vous pouvez, par exemple, rendre le texte et charger paresseusement des composants comme des images et d'autres widgets (par exemple, des cartes).

Ici, je rend [une page de test](https://jmperezperez.com/lazy-load/89b6f20e1d79e9fb902242ab84217b12.html) (vous pouvez voir la source [ici](https://github.com/JMPerez/lazy-load/blob/master/text-above-fold.js)) en utilisant les outils Google Webmaster Tools « Fetch as Google ». Googlebot rend le contenu dans la boîte affichée dans la fenêtre, mais pas le contenu en dessous.

### Un petit composant pour détecter quand une zone est visible

J'ai parlé dans le passé du [lazy-loading des images](https://jmperezperez.com/lazy-loading-images). Ce n'est qu'un type d'actif que nous pouvons lazy-loader, mais nous pouvons appliquer la technique à d'autres éléments.

Construisons un composant simple qui détectera quand la section est visible dans la fenêtre. Pour plus de concision, j'utiliserai l'[API Intersection Observer](https://developer.mozilla.org/docs/Web/API/Intersection_Observer_API), une technologie expérimentale avec [un bon support](https://caniuse.com/#search=intersectionobserver).

```
class Observer extends Component {  constructor() {    super();    this.state = { isVisible: false };    this.io = null;    this.container = null;  }  componentDidMount() {    this.io = new IntersectionObserver([entry] => {      this.setState({ isVisible: entry.isIntersecting });    }, {});    this.io.observe(this.container);  }  componentWillUnmount() {    if (this.io) {      this.io.disconnect();    }  }  render() {    return (      // nous créons une div pour obtenir une référence.      // Il est possible d'utiliser findDOMNode() pour éviter      // de créer des éléments supplémentaires, mais findDOMNode est déconseillé      <div        ref={div => {          this.container = div;        }}      >        {Array.isArray(this.props.children)          ? this.props.children.map(child => child(this.state.isVisible))          : this.props.children(this.state.isVisible)}      </div>    );  }}
```

Le composant utilise IntersectionObserver pour détecter que le conteneur intersecte avec la fenêtre (ce qui signifie qu'il est visible). Nous profitons des méthodes de cycle de vie de React pour nettoyer l'IntersectionObserver, [le déconnectant](https://developer.mozilla.org/docs/Web/API/IntersectionObserver/disconnect) lors du démontage.

Ce composant de base pourrait être étendu avec des propriétés supplémentaires passées en tant qu'[options à IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API#Intersection_observer_options), comme des marges ou des seuils. Cela nous permet de détecter les éléments proches mais n'intersectant pas avec la fenêtre. Les options sont définies dans le constructeur et sont en lecture seule. Ainsi, l'ajout de la prise en charge des options signifie que nous devrions réinstancier l'IntersectionObserver avec de nouvelles options lorsqu'elles changent, ajoutant une logique supplémentaire dans `componentWillReceiveProps` que nous n'allons pas couvrir ici.

Maintenant, nous pouvons utiliser ce composant pour lazy loader deux de nos composants, `Gallery` et `Map` :

```
const Page = () => {    <div>        <Header />        <Observer>          {isVisible => <Gallery isVisible />}        </Observer>        <Observer>          {isVisible => <Map isVisible />}        </Observer>        <Footer />    </div>}
```

Dans le code ci-dessus, je transmets simplement la propriété `isVisible` aux composants `Gallery` et `Map` pour qu'ils la gèrent. Alternativement, nous pourrions retourner le composant s'il est visible, ou un élément vide sinon.

Dans tous les cas, **assurez-vous de réserver l'espace pour le composant chargé paresseusement**. Vous ne voulez pas que le contenu saute, donc si vous savez que votre `Map` fait 400px de haut, rendez un conteneur vide de 400px de haut avant que la carte ne soit rendue.

Comment les composants `Map` et `Gallery` utilisent-ils la propriété `isVisible` ? Jetons un coup d'œil à la `Map` :

```
class Map extends Component {  constructor() {    super();    this.state = { initialized: false };    this.map = null;  }
```

```
initializeMap() {    this.setState({ initialized: true });    // loadScript charge un script externe, sa définition n'est pas incluse ici.    loadScript("https://maps.google.com/maps/api/js?key=<your_key>", () => {      const latlng = new google.maps.LatLng(38.34, -0.48);      const myOptions = { zoom: 15, center: latlng };      const map = new google.maps.Map(this.map, myOptions);    });  }
```

```
componentDidMount() {    if (this.props.isVisible) {      this.initializeMap();    }  }
```

```
componentWillReceiveProps(nextProps) {    if (!this.state.initialized && nextProps.isVisible) {      this.initializeMap();    }  }
```

```
render() {    return (      <div        ref={div => {          this.map = div;        }}      />    );  }}
```

Lorsque le conteneur est affiché dans la fenêtre, nous faisons une demande pour injecter le script de Google Map. Une fois chargé, nous créons la carte. C'est un bon exemple de lazy-loading de JavaScript qui n'est pas nécessaire dès le début, et le reste des ressources nécessaires pour afficher la carte.

Le composant a un état pour éviter de réinjecter le script de Google Map.

Jetons un coup d'œil au composant `Gallery` :

```
class Gallery extends Component {  constructor() {    super();    this.state = { hasBeenVisible: false };  }  componentDidMount() {    if (this.props.isVisible) {      this.setState({ hasBeenVisible: true });    }  }  componentWillReceiveProps(nextProps) {    if (!this.state.hasBeenVisible && nextProps.isVisible) {      this.setState({ hasBeenVisible: true });    }  }  render() {    return (      <div>        <h1>Quelques images</h1>        Image 1        {this.state.hasBeenVisible ? (          <img src="http://example.com/image01.jpg" width="300" height="300" />        ) : (          <div className="placeholder" />        )}        Image 2        {this.state.hasBeenVisible ? (          <img src="http://example.com/image02.jpg" width="300" height="300" />        ) : (          <div className="placeholder" />        )}      </div>    );  }}
```

L'exemple ci-dessus définit un autre composant avec état. En fait, nous stockons dans l'état les mêmes informations que nous avons faites avec la `Map`.

Si la galerie est affichée dans la fenêtre et ensuite elle est en dehors de la fenêtre, les images resteront dans le DOM. Dans la plupart des cas, c'est ce que nous voulons lorsque nous travaillons avec des images.

### Composants enfants sans état

Un composant sans état pourrait également être intéressant. Il nous permettrait de décharger les images qui ne sont plus visibles, en affichant à nouveau les placeholders :

```
const Gallery = ({ isVisible }) => (  <div>    <h1>Quelques images</h1>;    Image 1    {isVisible ? (      <img src="http://example.com/image01.jpg" width="300" height="300" />    ) : (      <div className="placeholder" />    )}    Image 2    {isVisible ? (      <img src="http://example.com/image02.jpg" width="300" height="300" />    ) : (      <div className="placeholder" />    )}  </div>);
```

Si vous faites cela, **assurez-vous que les images ont les bons en-têtes de réponse de cache**. Ainsi, les requêtes ultérieures du navigateur atteignent le cache et ne téléchargent pas à nouveau les images.

Si vous vous retrouvez à rendre vos composants chargés paresseusement avec état uniquement pour suivre qu'ils ont été visibles au moins une fois, vous pouvez ajouter cette logique au composant `Observer`. Après tout, `Observer` est déjà avec état et il peut facilement appeler ses enfants avec un argument supplémentaire `hasBeenVisible`.

```
const Page = () => {  ...  <Observer>    {(isVisible, hasBeenVisible) =>      <Gallery hasBeenVisible /> // Gallery peut maintenant être sans état    }  </Observer>  ...}
```

Une autre option est d'avoir une variante du composant `Observer` qui ne passe qu'une propriété comme `hasBeenVisible`. Cela a l'avantage que nous pouvons déconnecter l'IntersectionObserver dès que l'élément est en vue puisque nous ne allons pas changer sa valeur. Nous appellerons ce composant `ObserverOnce` :

```
class ObserverOnce extends Component {  constructor() {    super();    this.state = { hasBeenVisible: false };    this.io = null;    this.container = null;  }  componentDidMount() {    this.io = new IntersectionObserver(entries => {      entries.forEach(entry => {        if (entry.isIntersecting) {          this.setState({ hasBeenVisible: true });          this.io.disconnect();        }      });    }, {});    this.io.observe(this.container);  }  componentWillUnmount() {    if (this.io) {      this.io.disconnect();    }  }  render() {    return (      <div        ref={div => {          this.container = div;        }}      >        {Array.isArray(this.props.children)          ? this.props.children.map(child => child(this.state.hasBeenVisible))          : this.props.children(this.state.hasBeenVisible)}      </div>    );  }}
```

### Plus de cas d'utilisation

Nous avons utilisé le composant `Observer` pour charger des ressources à la demande. Nous pouvons également l'utiliser pour commencer à animer un composant dès qu'un utilisateur le voit.

Voici un exemple tiré du site React Alicante. Il anime certains chiffres de conférence dès que l'utilisateur fait défiler jusqu'à cette section.

Nous pourrions le recréer comme ceci (voir [l'exemple sur Codepen](https://codepen.io/jmperez/pen/LQXjYv)) :

```
class ConferenceData extends Component {  constructor() {    super();    this.state = { progress: 0 };    this.interval = null;    this.animationDuration = 2000;    this.startAnimation = null;  }  componentWillReceiveProps(nextProps) {    if (      !this.props.isVisible &&      nextProps.isVisible &&      this.state.progress !== 1    ) {      this.startAnimation = Date.now();      const tick = () => {        const progress = Math.min(          1,          (Date.now() - this.startAnimation) / this.animationDuration        );        this.setState({ progress: progress });        if (progress < 1) {          requestAnimationFrame(tick);        }      };      tick();    }  }  render() {    return (      <div>        {Math.floor(this.state.progress * 3)} jours         {Math.floor(this.state.progress * 21)} conférences         {Math.floor(this.state.progress * 4)} ateliers         {Math.floor(this.state.progress * 350)} participants      </div>    );  }}
```

Ensuite, nous l'utiliserions exactement comme les autres composants. Cela montre la puissance de l'abstraction de la logique de détection de visibilité en dehors des composants qui en ont besoin.

### Polyfilling IntersectionObserver à la demande

Jusqu'à présent, nous avons utilisé IntersectionObserver pour détecter quand un élément devient visible. Au moment de la rédaction de cet article, certains navigateurs (par exemple, Safari) ne prennent pas en charge cette fonctionnalité, donc l'instanciation de IntersectionObserver échouera.

Une option serait de définir `isVisible` sur `true` lorsque IntersectionObserver n'est pas disponible. Cela, en pratique, désactiverait le lazy-loading. D'une certaine manière, nous considérerions le lazy-loading comme une amélioration progressive :

```
class Observer extends Component {  constructor() {    super();    // isVisible est initialisé à true si le navigateur    // ne prend pas en charge l'API IntersectionObserver    this.state = { isVisible: !(window.IntersectionObserver) };    this.io = null;    this.container = null;  }  componentDidMount() {    // initialiser IntersectionObserver uniquement si pris en charge    if (window.IntersectionObserver) {      this.io = new IntersectionObserver(entries => {        ...      }    }  }}
```

Une autre option, que je préfère, est d'inclure un polyfill comme [le polyfill IntersectionObserver de w3c](https://github.com/w3c/IntersectionObserver/tree/master/polyfill). Ainsi, IntersectionObserver fonctionnera dans tous les navigateurs.

En suivant le sujet du chargement des ressources à la demande, et pour donner l'exemple, nous allons tirer parti du code-splitting pour ne demander le polyfill que si nécessaire. Ainsi, les navigateurs prenant en charge l'API n'ont pas besoin de récupérer le polyfill :

```
class Observer extends Component {  ...  componentDidMount() {    (window.IntersectionObserver      ? Promise.resolve()      : import('intersection-observer')    ).then(() => {      this.io = new window.IntersectionObserver(entries => {        entries.forEach(entry => {          this.setState({ isVisible: entry.isIntersecting });        });      }, {});      this.io.observe(this.container);    });  }  ...}
```

Vous pouvez voir [une démonstration ici](https://react-intersection-observer.stackblitz.io/) (consultez [la source du code](https://stackblitz.com/edit/react-intersection-observer)). Safari fera une demande supplémentaire pour charger le package npm `intersection-observer`, puisqu'il ne prend pas en charge IntersectionObserver.

![Image](https://cdn-media-1.freecodecamp.org/images/0*vNqwYA3I3hEASrCG.png)
_Safari demande le polyfill pour intersection-observer à la demande. Pas besoin de l'envoyer aux navigateurs qui le prennent en charge nativement._

Cela est réalisé grâce au code splitting. Il existe des outils comme [Parcel](https://parceljs.org/code_splitting.html) ou [Webpack](https://webpack.js.org/guides/code-splitting/) qui créeront un bundle pour ce package importé, et la logique nécessaire pour demander le fichier.

### Code Splitting et CSS-in-JS

Jusqu'à présent, nous avons vu comment utiliser un HOC pour détecter qu'un élément est dans la fenêtre. Nous avons également vu comment charger du JavaScript supplémentaire lorsque cela est nécessaire.

Le code-splitting est assez courant et simple à implémenter au niveau des routes. Le navigateur charge des bundles supplémentaires lorsque l'utilisateur navigue sur différentes URL du site. Des outils comme [react-router](https://github.com/ReactTraining/react-router) et [Next.js](https://github.com/zeit/next.js/) ont rendu cela simple à implémenter.

À travers les exemples de cet article, nous avons vu que la même chose peut être réalisée au sein de la même route, en chargeant le code des composants à la demande. Cela est très utile si nous avons des composants qui nécessitent beaucoup de code spécifique, pas seulement du JavaScript.

Un composant pourrait lier d'autres ressources ou même les inclure en ligne. Pensez aux SVG ou aux styles CSS.

Il n'y a pas d'intérêt à demander des styles qui ne seront pas appliqués à un élément. Demander et injecter dynamiquement du CSS provoque un FOUC (Flash of Unstyled Content). Le navigateur affiche les éléments HTML avec le style existant. Une fois les styles supplémentaires injectés, il restyle le contenu. Avec l'avènement des solutions CSS-in-JS (ou JSS), ce n'est plus un problème. Le CSS est intégré dans le composant, et nous obtenons un vrai code splitting pour nos composants. **Avec CSS-in-JS, nous allons plus loin dans le code splitting, en chargeant le CSS à la demande.**

### Implémentations utiles

Dans cet article, j'ai expliqué comment implémenter un composant Observer de base. Il existe des implémentations existantes de composants similaires qui ont été plus testées, prennent en charge plus d'options et fournissent des moyens supplémentaires de s'intégrer dans votre projet.

Je vous recommande définitivement de consulter ces 2 bibliothèques :

### Conclusion

Espérons que j'ai montré comment la composantisation peut rendre le code-splitting et le chargement des ressources à la demande plus faciles que jamais. Définissez les dépendances de votre code et utilisez des bundlers et des outils modernes pour demander les dépendances selon les besoins lorsque l'utilisateur navigue vers de nouveaux chemins ou que de nouveaux composants sont affichés sur la page.

Je tiens à remercier [@alexjoverm](https://twitter.com/alexjoverm), [@aarongarciah](https://twitter.com/aarongarciah) et [@FlavioCorpa](https://twitter.com/FlavioCorpa) pour avoir révisé l'article, recherché des sujets similaires et recommandé des outils pour fournir les exemples sur la page.

Avez-vous vu une faute de frappe ou une information erronée ? Dans ce cas, [envoyez-moi un message](https://twitter.com/jmperezperez).

_Lisez plus de moi sur mon [site web](https://jmperezperez.com).