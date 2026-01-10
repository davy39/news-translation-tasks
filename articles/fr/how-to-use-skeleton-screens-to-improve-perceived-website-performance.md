---
title: Comment utiliser les écrans squelettes pour améliorer la performance perçue
  d'un site web
subtitle: ''
author: Timothy Olanrewaju
co_authors: []
series: null
date: '2024-10-23T19:59:15.584Z'
originalURL: https://freecodecamp.org/news/how-to-use-skeleton-screens-to-improve-perceived-website-performance
coverImage: https://cdn.hashnode.com/res/hashnode/image/upload/v1729603651952/5f5f3c38-20e0-41ac-a4a0-7190347b3a59.png
tags:
- name: Frontend Development
  slug: frontend-development
- name: performance
  slug: performance
seo_title: Comment utiliser les écrans squelettes pour améliorer la performance perçue
  d'un site web
seo_desc: 'When you’re building a website, it’s important to make sure that it’s fast.
  People have little to no patience for slow-loading websites. So as developers, we
  need to use all the techniques available to us to speed up our site’s performance.

  And somet...'
---

Lorsque vous construisez un site web, il est important de vous assurer qu'il est rapide. Les gens ont peu ou pas de patience pour les sites web qui chargent lentement. En tant que développeurs, nous devons donc utiliser toutes les techniques disponibles pour accélérer les performances de notre site.

Et parfois, nous devons donner l'impression aux utilisateurs que quelque chose se passe lorsqu'ils attendent le chargement d'une page, afin qu'ils ne renoncent pas et ne quittent pas le site.

La vitesse de chargement rapide des pages web est importante de nos jours car l'attention des humains diminue. Selon les [statistiques sur l'attention moyenne des humains](https://www.wellbrookrecovery.com/post/average-attention-span), la visite moyenne d'une page dure moins d'une minute, les utilisateurs quittant souvent les pages web en seulement 10 à 20 secondes.

Cela signifie que nous, en tant que développeurs, avons dû trouver des stratégies pour garder les utilisateurs engagés pendant qu'ils attendent que le contenu de leur page web demandée se charge. Et cela a conduit au concept de l'écran squelette.

Dans cet article, nous allons examiner ce que sont les écrans squelettes, leur efficacité à améliorer l'expérience utilisateur et construire notre propre écran squelette !

## **Qu'est-ce qu'un écran squelette ?**

Un écran squelette est comme une esquisse d'une page web qui s'affiche avant que la page finale ne se charge complètement. Il donne un aperçu de la forme et du positionnement des éléments à l'écran (comme le texte, les images et les boutons) qui sont représentés par un espace réservé.

Voici à quoi ressemble un écran squelette de YouTube :

![Exemple d'écran squelette YouTube montrant des espaces réservés](https://cdn.hashnode.com/res/hashnode/image/upload/v1729602784479/b4ffa403-f642-41f0-911b-897f2eebad2b.png align="center")

Lorsque vous visitez un site web qui utilise des écrans squelettes, l'écran squelette apparaît en premier pendant que le contenu est en cours de récupération. Lorsque le contenu est enfin récupéré, il remplace progressivement l'écran squelette jusqu'à ce que l'écran soit entièrement rempli.

C'est ce qui a donné le nom *Écran Squelette* - parce que les os nus, semblables à un squelette, apparaissent en premier avant d'être remplis par le contenu réel.

Les écrans squelettes prennent l'apparence ou la forme des éléments qu'ils sont censés "remplacer" - ce qui signifie que les espaces réservés en forme d'ovale sont remplacés par des éléments en forme d'ovale lors du chargement complet, et ainsi de suite.

L'objectif ultime de l'écran squelettique est de rendre l'attente moins pénible en donnant aux utilisateurs quelque chose sur quoi se concentrer. Cela n'a rien à voir avec le temps de chargement réel, mais tout à voir avec le fait de fournir une distraction pour que le temps d'attente semble plus court. Cela peut également rassurer les utilisateurs que le contenu arrive effectivement. Malin, n'est-ce pas ?

## **La psychologie derrière les écrans squelettes**

Voici où les choses deviennent intéressantes. Vous vous demandez peut-être déjà quelle était la raison derrière une telle invention.

D'après ce que nous avons déjà discuté, vous êtes probablement d'accord pour dire qu'ils concernent tous la "Performance Perçue". Il s'agit moins du temps que les utilisateurs doivent attendre et plus du temps qu'il *semble* qu'ils attendent.

Si vous avez déjà été coincé dans les embouteillages, vous savez qu'il y a une différence de sensation lorsque vous avancez par rapport à lorsque vous êtes immobile. Un trafic en mouvement, même s'il est lent, est meilleur que d'être bloqué dans un embouteillage total.

Il en va de même pour un utilisateur qui visite une page web. Un espace réservé visible et engageant est meilleur que d'être accueilli par un écran blanc en attendant que le contenu final s'affiche.

Avec les écrans squelettes, c'est comme si on disait : "Hey, voici la forme du contenu de la page que vous cherchez, mais s'il vous plaît, faites preuve de patience pendant que nous vous obtenons la vraie chose !"

Cela s'inscrit parfaitement dans l'**Effet Zeigarnik**, un principe psychologique suggérant que nous nous souvenons mieux des tâches inachevées que des tâches terminées. Pensez à cela comme à laisser un puzzle à moitié terminé sur votre table - votre cerveau reste engagé, impatient de voir l'image finale.

De même, lorsque les utilisateurs voient un écran squelette, ils restent mentalement accrochés, anticipant le moment où le contenu se chargera complètement.

## **Écrans squelettes vs Spinners et barres de progression**

Les spinners et les barres de progression peuvent sembler être une alternative viable aux écrans squelettes, mais ont-ils le même effet sur les utilisateurs ? La réponse est - pas tout à fait.

Avec les spinners et les barres de progression, le temps de chargement est quelque peu indécis, et c'est un peu comme regarder une horloge - le temps semble s'écouler plus lentement, car se concentrer sur les aiguilles de l'horloge rend la durée plus longue et plus frustrante.

Les écrans squelettes, en revanche, ajoutent une couche supplémentaire intéressante en fournissant un indice visuel du contenu attendu plutôt que de simplement afficher un indicateur (ce que font les spinners et les barres de progression).

Les interfaces qui utilisent des écrans squelettes font en sorte que l'utilisateur scanne l'écran en pensant des choses comme : "Ce rectangle doit être une image ou une vidéo, et ces blocs semblent être pour le texte". Ils ne laissent pas les utilisateurs inactifs mais gardent leur cerveau et leurs yeux engagés.

## **Un écran squelette n'est-il qu'une illusion visuelle ?**

Oui, les écrans squelettes sont un peu une illusion. Ils n'accélèrent pas les temps de chargement - plutôt, ils donnent simplement l'impression d'être plus rapides.

Mais voici le problème : si ce n'est pas bien fait, ce truc peut se retourner contre vous. Les utilisateurs s'attendent à ce que, une fois qu'ils voient l'écran squelette, le contenu réel doit suivre rapidement. Sinon, la frustration s'installe.

De plus, ajouter du mouvement aux écrans squelettes rend l'effet d'illusion plus efficace en diminuant le temps de durée perçu. Il n'est pas rare de voir des effets de glissement (de gauche à droite) et des effets de pulsation (opacité de fondu - entrée et sortie) utilisés dans les écrans squelettes.

![écran squelette avec mouvement](https://cdn.hashnode.com/res/hashnode/image/upload/v1729603561030/235b53ed-a75d-4eb0-9126-c63174d0c59f.gif align="center")

Enfin, pour de meilleurs résultats, les écrans squelettes doivent être de couleur neutre. Cela est important car cela aide à créer une expérience de chargement fluide et subtile sans distraire ou submerger les utilisateurs.

## Comment construire un écran squelette avec React

Maintenant que vous savez ce qu'est un écran squelette, construisons le nôtre en utilisant React.

### **Étape 1 : Configurer votre projet React**

Si vous êtes nouveau dans React et souhaitez suivre, cliquez sur ce [lien](https://vite.dev/guide/) et suivez les étapes pour créer votre projet React. Lorsque vous avez terminé, revenez ici et continuons à construire.

Si vous avez déjà un projet React que vous souhaitez utiliser, c'est aussi bien.

### **Étape 2 : Installer le package** `react-loading-skeleton`

Ensuite, nous installerons un package appelé **react-loading-skeleton** qui aide à créer de beaux et animés squelettes. Pour installer ce package :

* Naviguez vers votre projet dans votre terminal.

* Si vous utilisez yarn, tapez cette commande `yarn add react-loading-skeleton` ou `npm install react-loading-skeleton` pour les utilisateurs de npm.

### **Étape 3 : Comment gérer les états et les imports de squelettes**

Il y a des variables qui changeront fréquemment dans notre projet, et elles doivent être déclarées. Vous pouvez lire mon article sur la [gestion d'état](https://www.freecodecamp.org/news/react-state-management/) si vous n'êtes pas familier avec le concept.

```javascript
  import { useState } from 'react';
  import Skeleton from 'react-loading-skeleton';
  import 'react-loading-skeleton/dist/skeleton.css';

  const SkeletonScreenComponent = () => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
  }
  export default SkeletonScreenComponent;
```

Dans ce code, nous avons déclaré trois états dans notre **SkeletonScreenComponent** qui sont :

* **data** : responsable du stockage des données récupérées depuis une fausse API REST avec sa valeur initiale définie sur un tableau vide.

* **loading** : pour suivre le chargement des données avec sa valeur initiale définie sur une valeur booléenne **true**.

* **error** : pour stocker tout message d'erreur avec une valeur initiale définie sur **null**.

Nous avons également importé le hook `useState` pour les états ainsi que le composant `Skeleton` et son CSS depuis la bibliothèque `react-loading-skeleton`.

### **Étape 4 : Récupérer les données depuis la fausse API**

Notre petit projet récupérera des données depuis [https://jsonplaceholder.typicode.com/posts](https://jsonplaceholder.typicode.com/posts), qui est une fausse API REST en ligne gratuite.

```javascript
  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
        const response = await fetch('https://jsonplaceholder.typicode.com/posts');
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
        setLoading(false);
    } catch (err) {
      setError('Error fetching data'+ err.message);
      setLoading(false);
    } 
  };
```

Dans le bloc de code ci-dessus :

* Le **hook useEffect** est responsable de la gestion des effets secondaires. Il est parfait pour les besoins de récupération de données, et son tableau de dépendances est défini comme vide (ce qui le fait rendre au montage).

* **fetchData** est une fonction asynchrone qui récupère les données depuis l'**URL**, met à jour l'état **data**, définit l'état **loading** sur false une fois terminé, capture toute erreur et met à jour l'état **error**.

### **Étape 5 : Rendu conditionnel**

L'idée principale de ce projet tourne autour de l'état **loading**. Le composant rend différents contenus en fonction de l'état **loading**.

Si **loading** est vrai :

* Un tableau est créé où chaque élément est un composant Skeleton.

* Le **compteur Skeleton** est défini à 2, pour le titre et le corps du post. Vous pouvez définir le compteur selon le nombre d'espaces réservés que vous souhaitez afficher.

Si le chargement des données est réussi :

* Il parcourt le tableau **data**.

* Il rend le titre et le corps de chaque post.

Si une erreur survient, un message d'erreur est affiché.

```javascript
   if (loading) {
    return (
      <div>
        {Array.from({ length: 15 },(_, index) => (
          <div key={index} style={{  marginTop: '30px'  }}>
            <Skeleton count={2} style={{marginBottom:"5px"}} />
          </div>
        ))}
      </div>
    );
  }

  if (error) {
    return <div>{error}</div>;
  }
  return (
    <div>
      {data.map(({id, title, body}) => (
        <div key={id} style={{ marginBottom: '20px' }}>
          <h3>{title}</h3>
          <p>{body}</p>
        </div>
      ))}
    </div>
  );
```

### **Résultat final**

Voici à quoi ressemble notre écran squelette :

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1729711380366/974d0de9-faf1-4050-90e7-1c982ac72e67.gif align="center")

## **Conclusion**

Les écrans squelettes sont excellents pour créer l'illusion de progression et donner aux utilisateurs l'impression que le site se charge plus rapidement. Mais ils ne corrigent pas à eux seuls les pages à chargement lent. L'astuce consiste à combiner les écrans squelettes avec des techniques d'amélioration des performances telles que le chargement paresseux, la compression d'images et le rendu côté serveur.

Équilibrer la vitesse réelle et la perception de l'utilisateur est vital dans la performance web. Les écrans squelettes ne sont qu'un outil dans votre boîte à outils UX - mais lorsqu'ils sont utilisés correctement, ils peuvent aider à créer une expérience web qui semble rapide, fiable et surtout engageante. Et dans le monde du développement web, où la perception est la réalité, c'est la moitié de la bataille gagnée.

Pour plus de publications et d'articles liés au front-end, vous pouvez me suivre sur [LinkedIn](https://www.linkedin.com/in/timothy-olanrewaju750/) et [X](https://x.com/SmoothTee_DC).

À la prochaine !