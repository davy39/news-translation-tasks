---
title: Comment créer un composant Marquee avec React
subtitle: ''
author: David Jaja
co_authors: []
series: null
date: '2024-04-09T12:41:24.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-a-marquee-component-with-react
coverImage: https://www.freecodecamp.org/news/content/images/2024/04/Group-297.png
tags:
- name: components
  slug: components
- name: projects
  slug: projects
- name: React
  slug: react
seo_title: Comment créer un composant Marquee avec React
seo_desc: 'When you think of marquees, you often envision the vibrant lights and spinning
  displays at amusement parks, bringing back fond memories of your childhood.

  Similarly in web applications, marquees inject a lively visual sense by effortlessly
  grabbing a...'
---

Lorsque vous pensez aux marquees, vous imaginez souvent les lumières vibrantes et les affichages tournants des parcs d'attractions, rappelant les souvenirs de votre enfance.

De même, dans les applications web, les marquees injectent un sentiment visuel dynamique en attirant facilement l'attention et en infusant vos projets en ligne avec du dynamisme.

Rejoignez-moi pour explorer comment créer un composant marquee engageant dans React. 
Ce guide étape par étape s'adresse à tous, quel que soit le niveau de compétence, nous visons à rendre votre expérience avec React à la fois agréable et utile.

## **Ce que nous allons couvrir :**

1. [Comprendre les composants Marquee](#heading-comprendre-les-composants-marquee)
2. [Avantages des Marquees](#heading-avantages-des-marquees)
3. [Planification et conception du composant Marquee](#heading-planification-et-conception-du-composant-marquee)
4. [Comment implémenter le composant Marquee](#heading-comment-implementer-le-composant-marquee)
5. [Comment améliorer le composant Marquee](#heading-comment-ameliorer-le-composant-marquee)
6. [Meilleures pratiques et conseils pour le développement de composants Marquee](https://www.freecodecamp.org/news/p/0148db11-7178-4632-b727-2321d7e96b01/best-practices-and-tips-for-marquee-component-development)
7. [Conclusion](#heading-conclusion)

## Prérequis

* Fondamentaux de HTML et CSS
* Fondamentaux de ES6 JavaScript et React

## Comprendre les composants Marquee

Une marquee représente une section continue de texte ou de contenu visuel (comme des images) qui défile automatiquement dans une direction horizontale.

Bien que l'élément officiel [HTML Marquee](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/marquee) soit obsolète et son utilisation fortement déconseillée, le concept de défilement, d'éléments sans fin pour ajouter du piquant à une page web est toujours très utilisé, et peut être trouvé sur de nombreux sites web modernes.

Cet effet est réalisé grâce aux [animations CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_animations/Using_CSS_animations), offrant un résultat d'animation plus efficace, fluide et léger.

Un exemple visuel d'un composant marquee de [Webflow](https://webflow.com/made-in-webflow/website/ujjo-Rebuild) est montré ci-dessous.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/00-Example-marquee.gif)
_Exemple Webflow_

## Avantages des Marquees

Ils ont de nombreuses utilités telles que :

* **Attirer l'attention** : Les marquees sont excellentes pour attirer l'attention sur un contenu spécifique d'une page web. Qu'il s'agisse d'une offre spéciale, d'une annonce ou d'un contenu mis en avant, une marquee en mouvement attire naturellement l'œil.
* **Appeal visuel** : Ajouter une touche de mouvement à votre site web améliore son attrait visuel. Les marquees peuvent donner vie à une page, la rendant plus dynamique et engageante pour les utilisateurs.
* **Mettre en avant des informations importantes** : Lorsque vous souhaitez souligner des informations critiques comme des nouvelles urgentes, des événements à venir ou des messages urgents, une marquee est un moyen efficace de s'assurer que les utilisateurs ne les manquent pas.
* **Promotion d'événements** : Elles sont particulièrement utiles pour promouvoir des événements ou des activités sensibles au temps. Leur nature de défilement permet d'afficher les détails des événements, les dates et les points forts de manière efficace en termes d'espace.
* **Mises à jour de style ticker** : Pour afficher des mises à jour en temps réel, telles que les prix des actions, les titres de nouvelles ou les flux de médias sociaux, les marquees fournissent un format de style ticker qui maintient l'information en flux continu pour les utilisateurs.
* **Bannières interactives** : Elles peuvent servir de bannières interactives, permettant aux utilisateurs de cliquer sur des éléments spécifiques lorsqu'ils défilent. Cela peut être un moyen créatif de guider les utilisateurs vers différentes sections ou pages de votre site web.
* **Présentations de produits dynamiques** : Les sites web de commerce électronique peuvent bénéficier des marquees en mettant en avant de nouveaux produits ou des articles vedettes de manière visuellement engageante, encourageant les utilisateurs à explorer les offres.
* **Emphase sur les appels à l'action** : Si vous avez des messages spécifiques d'appel à l'action, les utiliser peut leur donner de la proéminence et s'assurer qu'ils ne passent pas inaperçus.
* **Rompre la monotonie** : Dans les longues pages ou le contenu statique, une marquee bien conçue peut rompre la monotonie et ajouter un élément de surprise, rendant l'expérience utilisateur plus intéressante.
* **Polyvalence** : Elles sont polyvalentes et peuvent être personnalisées pour s'adapter à divers styles et thèmes, ce qui en fait un outil flexible pour les concepteurs web cherchant à créer des interfaces utilisateur uniques et mémorables.

## Planification et conception du composant Marquee

Avant de commencer à coder, il est important de planifier et de concevoir votre composant et de prendre en compte des facteurs tels que :

* **Définir le contenu** : Définissez clairement le contenu que vous souhaitez afficher dans le composant. Cela peut inclure du texte, des images ou une combinaison des deux.
* **Vitesse de défilement** : Déterminez la vitesse de défilement souhaitée à utiliser. Pensez au rythme optimal pour la lisibilité et l'attrait visuel.
* **Conception visuelle** : Esquissez ou visualisez comment vous souhaitez qu'elle apparaisse. Décidez des couleurs, des polices et de tout style supplémentaire pour aligner avec votre schéma de conception global.
* **Comportement à la fin du défilement** : Considérez son comportement lorsqu'elle atteint la fin de sa position de défilement. Décidez si elle doit boucler en continu, rebondir ou avoir un état final spécifique.
* **Interaction utilisateur** : Si applicable, planifiez toute interaction utilisateur. Cela pourrait inclure la pause au survol ou permettre aux utilisateurs de cliquer sur des éléments dans la marquee.
* **Conception réactive** : Assurez-vous que votre composant est conçu pour être réactif, s'adaptant de manière transparente à différentes tailles d'écran et appareils.
* **Considérations de test** : Anticipez les défis potentiels ou les ajustements nécessaires pendant la phase de test. Planifiez comment elle se comportera sur divers navigateurs et appareils.
* **Accessibilité** : Gardez à l'esprit l'accessibilité, en vous assurant que les utilisateurs avec différents handicaps peuvent toujours accéder et comprendre le contenu à l'intérieur.

## Comment implémenter le composant Marquee

Pour implémenter le composant, commencez par créer un environnement React avec [Vite](https://vitejs.dev/guide/).

```bash
npm create vite@latest
```

Ensuite, naviguez vers votre répertoire de projet, installez les packages nécessaires et démarrez le serveur de développement.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/01-react-server-after-installation-.png)
_Configuration du serveur de développement_

Ensuite, créez les éléments pour la maquette JSX de votre composant.

```jsx
export default function App() {
  return (
    <div className=" main__container">
      <h1>Ma Marquee</h1>
      <section className=" ">
        <h2>Comportement par défaut</h2>

        <div className="marquee">
          <ul className="marquee__content">
            <div className=" marquee__item">
              <img src={AndroidLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={BehanceLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={GoogleLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={InstagramLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={PaypalLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={SpotifyLogo} alt="" />
            </div>
          </ul>

          <ul aria-hidden="true" className="marquee__content">
            <div className=" marquee__item">
              <img src={AndroidLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={BehanceLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={GoogleLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={InstagramLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={PaypalLogo} alt="" />
            </div>
            <div className=" marquee__item">
              <img src={SpotifyLogo} alt="" />
            </div>
          </ul>
        </div>
      </section>
    </div>
  );
}
```

Cela inclut un en-tête pour le composant, le comportement du composant et les données dans le composant à animer.

Il est important de dupliquer les données dans le composant car elles seront utilisées pour obtenir l'effet de duplication. Cependant, nous masquons la deuxième liste initialement en utilisant la propriété `aria-hidden='true'`.

Pour le rendre plus visuellement attrayant, ajoutez ces styles.

```css
body {
  font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto,
    Oxygen, Ubuntu, Cantarell, "Open Sans", "Helvetica Neue", sans-serif;
  padding: 2rem;
  width: 100%;
  min-height: 100vh;
  font-size: 1rem;
  line-height: 1.5;
}

* { box-sizing: border-box; }

h1 {
  font-size: 2rem;
  font-weight: 600;
  line-height: 1.2;
  margin-block: 2rem 1rem;
  text-align: center;
}

h2 {
  font-size: 1.25rem;
  font-weight: 600;
}

section { margin-block: 3rem; }

.main__container {
  max-width: 1000px;
  margin-inline: auto;
  background: rgb(124, 145, 175);
  padding: 3rem;
}

/* Styles de la marquee */
.marquee {
  --gap: 1rem;
  position: relative;
  display: flex;
  overflow: hidden;
  user-select: none;
  gap: var(--gap);
  border: 2px dashed lightgray;
}

.marquee__content {
  flex-shrink: 0;
  display: flex;
  justify-content: space-around;
  gap: var(--gap);
  min-width: 100%;
}

.marquee__content img {
  max-width: 2rem;
  width: 100%;
  object-fit: contain;
}

.marquee__content > * {
  flex: 0 0 auto;
  color: white;
  background: #e8daef;
  margin: 2px;
  padding: 1rem 2rem;
  border-radius: 0.25rem;
  text-align: center;
}

.marquee__item {
  display: flex;
  justify-content: center;
  align-items: center;
}

ul { padding-left: 0; }
```

Pour l'instant, votre composant devrait ressembler à ceci ;

![Image](https://www.freecodecamp.org/news/content/images/2024/03/02-UI-after-applying-styles.png)
_UI après application des styles_

Pour animer ce composant, commencez par définir des [keyframes CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/@keyframes) personnalisées.

```css
@keyframes scroll {
  from { transform: translateX(0); }
  to { transform: translateX(calc(-100% - var(--gap))); }
}
```

**Note** : L'écart utilisé est le même que celui entre les éléments de la marquee. 
Ensuite, attribuez ces keyframes à une classe.

```css
/* Activer l'animation */
.enable-animation .marquee__content {
  animation: scroll 10s linear infinite;
}
```

Enfin, ajoutez cette classe à votre élément de section.

```jsx
<section className="enable-animation">
```

Et avec cela, votre composant devrait déjà être animé.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/03-Animated-marquee.gif)
_Marquee animée_

## Comment améliorer le composant Marquee

Ce composant va au-delà des animations infinies régulières (comme montré ci-dessus), il possède souvent des fonctionnalités supplémentaires telles que :

* **Pause au survol** : Bien que l'utilisation d'une marquee puisse être bénéfique pour montrer un ensemble de contenu de manière plus dynamique, la vitesse de l'animation ou la position de l'information pertinente pour l'utilisateur peut poser des problèmes, surtout pour les lecteurs lents.

Pour résoudre cela, vous pouvez implémenter une fonctionnalité de pause pour l'arrêter lorsque l'utilisateur passe la souris dessus. Il suffit d'ajouter le code CSS ci-dessous.

```css
/* Pause au survol */
.marquee:hover .marquee__content {
  animation-play-state: paused;
}
```

Et avec cela, elle se met en pause au survol.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/04-Animated-marquee-that-pauses-on-hover.gif)
_Marquee animée qui se met en pause au survol_

* **Inverser au double-clic** : Dans le cas où un utilisateur a dépassé une information importante et souhaite la voir sans attendre que l'animation en boucle la ramène, il est important de fournir un moyen d'y parvenir.

En double-cliquant sur le composant, l'animation se joue dans le sens inverse, montrant l'information que l'utilisateur vient de dépasser. Cette fonctionnalité non seulement favorise l'accessibilité, mais donne également à vos pages web une sensation de réactivité, car elle fournit un moyen plus rapide d'obtenir des informations.

Pour implémenter cela, commencez par créer un état d'animation inverse.

```jsx
 const [reverseAnimation, setReverseAnimation] = useState(false);
```

Ensuite, créez une fonction pour inverser l'état de l'animation.

```jsx
const handleDoubleClick = () => {
    setReverseAnimation((prev) => !prev);
  };
```

Après cela, créez la règle de classe CSS pour inverser l'animation.

```jsx
/* Animation inverse */
.marquee--reverse .marquee__content {
  animation-direction: reverse !important;
}
```

Ensuite, attachez la fonction de gestionnaire au composant.

```jsx
<div className="marquee" onDoubleClick={handleDoubleClick}>
      <ul className="marquee__content">
        <div className=" marquee__item">
          <img src={AndroidLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={BehanceLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={GoogleLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={InstagramLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={PaypalLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={SpotifyLogo} alt="" />
        </div>
      </ul>

      <ul aria-hidden="true" className="marquee__content">
        <div className=" marquee__item">
          <img src={AndroidLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={BehanceLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={GoogleLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={InstagramLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={PaypalLogo} alt="" />
        </div>
        <div className=" marquee__item">
          <img src={SpotifyLogo} alt="" />
        </div>
      </ul>
</div>
```

Enfin, ajoutez conditionnellement la classe inverse au composant qui inverse l'animation au double-clic.

```jsx
 <div className={`marquee ${reverseAnimation && "marquee--reverse"}`} 
      onDoubleClick={handleDoubleClick}>
```

Le double-clic sur le composant donne maintenant ;

![Image](https://www.freecodecamp.org/news/content/images/2024/03/05-Animated-marquee-that-revereses-on-double-click.gif)
_Marquee animée qui s'inverse au double-clic_

* **Pause/Lecture sur clic de la barre d'espace** : Une autre fonctionnalité qui peut être ajoutée pour améliorer l'UX, surtout pour les utilisateurs de clavier, est de mettre en pause ou de lire l'animation en appuyant sur la barre d'espace. Cela imite la fonctionnalité de lecture des vidéos sur le web et aidera à améliorer l'accessibilité pour les utilisateurs.

Pour implémenter cela, commencez par créer un état pour stocker l'état actuel de pause de l'animation.

```jsx
const [isAnimationPaused, setIsAnimationPaused] = useState(false);
```

Ensuite, créez la règle CSS pour l'état de pause.

```jsx
/* Pause de l'animation */
.marquee--paused .marquee__content {
  animation-play-state: paused !important;
}
```

Après cela, créez un effet qui met à jour l'état `isAnimationPaused` chaque fois que la barre d'espace est pressée.

```jsx
 useEffect(() => {
    const handleKeyPress = (event) => {
      if (event.code === "Space") {
     
        setIsAnimationPaused((prev) => !prev);
      }
    };
    document.addEventListener("keydown", handleKeyPress);

   // Fonction de nettoyage lorsque le composant est démonté
    return () => {
      document.removeEventListener("keydown", handleKeyPress);
    };
  }, []);
```

De cette manière, l'état bascule entre vrai et faux en fonction des pressions de l'utilisateur. 
Enfin, ajoutez dynamiquement la classe de pause à votre composant.

```jsx
<div className={`marquee ${reverseAnimation && "marquee--reverse"} ${
       isAnimationPaused && "marquee--paused"}`} onDoubleClick={handleDoubleClick}>
```

Et avec cela, votre composant se met en pause et relance chaque fois que vous appuyez sur la barre d'espace.

![Image](https://www.freecodecamp.org/news/content/images/2024/03/06-Animated-marquee-that-can-be-paused-with-space-bar.gif)
_Marquee animée qui peut être mise en pause avec la barre d'espace_

## Meilleures pratiques et conseils pour le développement de composants Marquee

Certaines des meilleures pratiques à considérer lors de la création de ce composant incluent :

* **Chargement paresseux des images** : Dans le cas où votre marquee contient de nombreuses images de haute qualité qui pourraient être volumineuses, il est essentiel de les optimiser avant de créer le composant. 
Le [chargement paresseux](https://daiveedjay.hashnode.dev/implementing-image-lazy-loading-to-improve-website-performance-using-javascript) retarde le téléchargement des images par le navigateur jusqu'à ce qu'elles soient nécessaires (requises pour être affichées dans la fenêtre d'affichage), réduisant ainsi le temps de chargement global de la page.

Pour y parvenir, ajoutez la propriété `loading='lazy'` à vos images.

```jsx
<ul className="marquee__content">
    <div className=" marquee__item">
      <img src={AndroidLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={BehanceLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={GoogleLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={InstagramLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={PaypalLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={SpotifyLogo} alt="" loading="lazy" />
    </div>
  </ul>

  <ul aria-hidden="true" className="marquee__content">
    <div className=" marquee__item">
      <img src={AndroidLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={BehanceLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={GoogleLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={InstagramLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={PaypalLogo} alt="" loading="lazy" />
    </div>
    <div className=" marquee__item">
      <img src={SpotifyLogo} alt="" loading="lazy" />
    </div>
</ul>
```

* **Vitesse d'animation réfléchie** : Lors de la mise en œuvre de l'animation, il est crucial de trouver un équilibre en termes de vitesse. Le rythme de l'animation doit être visuellement attrayant, captant l'attention de l'utilisateur sans sacrifier la lisibilité ou causer de l'inconfort. 
Cela implique une considération réfléchie de la rapidité avec laquelle le contenu défile à l'écran. 
En prêtant attention à la vitesse de l'animation et en trouvant le bon équilibre, vous améliorez l'expérience utilisateur globale, faisant de la marquee un élément efficace et agréable sur votre site web.
* **Penser aux utilisateurs sensibles au mouvement** : La conception inclusive signifie prendre en compte les besoins et préférences de différents utilisateurs, y compris ceux sensibles au mouvement. Certains utilisateurs peuvent préférer moins de mouvement en raison de conditions telles que les troubles vestibulaires ou simplement pour le confort personnel. 
Pour soutenir ces utilisateurs, vous pouvez utiliser la requête média `prefers-reduced-motion` dans votre composant.

```jsx
/* Pause de l'animation lorsque le mouvement réduit est activé */
@media (prefers-reduced-motion: reduce) {
  .marquee__content {
    animation-play-state: paused !important;
  }
}
```

* **Documentation appropriée** : Fournissez une documentation claire sur la manière dont les utilisateurs peuvent utiliser votre composant efficacement afin qu'ils ne rencontrent pas de difficultés à l'utiliser ou ne manquent pas toutes les fonctionnalités qu'il possède. Envisagez d'utiliser des étiquettes autour du composant ou une fenêtre contextuelle pour transmettre de courtes instructions sur son utilisation.

## Conclusion

Votre guide des composants Marquee React est complet ! De la planification à l'exécution, vous avez plongé dans la création d'éléments de défilement dynamiques pour vos projets web.

Rappelez-vous, ce composant est plus que du mouvement, c'est une histoire interactive. Qu'il s'agisse de partager des informations cruciales, de promouvoir des événements ou d'injecter du dynamisme, votre marquee est un ajout polyvalent à votre boîte à outils.

Mais ce voyage n'est que le début. Ajustez les vitesses, tenez compte des sensibilités et adoptez les meilleures pratiques pour affiner votre marquee. Laissez libre cours à votre créativité, et que vos histoires de défilement laissent une impression durable.

Donnez la priorité à l'expérience utilisateur, expérimentez avec des améliorations et laissez votre développement briller dans le paysage web. Bon défilement !

### **Informations de contact**

Vous souhaitez me contacter ? N'hésitez pas à me contacter sur les plateformes suivantes :

* Twitter : [@jajadavid8](https://twitter.com/JajaDavid8)
* LinkedIn : [David Jaja](https://www.linkedin.com/in/david-jaja-8084251b4/)
* Email : Jajadavidjid@gmail.com