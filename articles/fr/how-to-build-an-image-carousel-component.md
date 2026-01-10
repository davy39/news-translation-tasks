---
title: Comment créer un composant Carousel d'images avec TypeScript et Styled-Components
subtitle: ''
author: Keyur Paralkar
co_authors: []
series: null
date: '2023-06-05T17:28:08.000Z'
originalURL: https://freecodecamp.org/news/how-to-build-an-image-carousel-component
coverImage: https://www.freecodecamp.org/news/content/images/2023/05/sunder-muthukumaran-I4eKHN1KaZ0-unsplash.jpg
tags:
- name: CSS
  slug: css
- name: TypeScript
  slug: typescript
seo_title: Comment créer un composant Carousel d'images avec TypeScript et Styled-Components
seo_desc: 'In recent years, OTT (over-the-top) video streaming platforms have become
  more innovative and convenient to use. In their user interfaces, movies and series
  titles are arranged so that the titles are clearly visible.

  In this tutorial, I’ll guide you ...'
---

Ces dernières années, les plateformes de streaming vidéo OTT (over-the-top) sont devenues plus innovantes et plus pratiques à utiliser. Dans leurs interfaces utilisateur, les titres de films et de séries sont disposés de manière à ce que les titres soient clairement visibles.

Dans ce tutoriel, je vais vous guider à travers le processus de création d'un composant carousel d'images qui ressemble à ceux que vous voyez sur de nombreuses plateformes OTT (pensez à Netflix). 

Nous allons commencer par créer des composants atomiques, tels que `Tags`, `Description`, `Title`, et ainsi de suite, qui afficheront diverses informations sur chaque titre de film. Ensuite, nous assemblerons ces composants via un modèle composé pour créer un composant `Banner` qui affiche chaque titre de film sous la forme d'une image. Enfin, nous utiliserons le composant `HeroBanner` pour construire le composant carousel d'images en utilisant le package `Swiper`. 

À la fin de cet article, vous aurez les connaissances et les compétences nécessaires pour créer un beau et fonctionnel composant carousel d'images qui impressionnera vos utilisateurs. Commençons !

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-97.png)

## Table des matières

* [Prérequis](#heading-prerequisites)
* [Comment construire le composant Banner](#heading-how-to-build-the-banner-component)
* [Comment construire les composants individuels](#heading-how-to-build-the-individual-components)
* [Comment assembler tous les composants avec le modèle composé](#heading-how-to-stitch-all-the-components-together-with-the-compound-pattern)
* [Comment construire le composant Carousel d'images](#heading-how-to-build-the-image-carousel-component)
* [Résumé](#heading-summary)

## Prérequis

Avant de passer aux sections suivantes, assurez-vous d'être à l'aise avec les sujets suivants :

* **CSS** – Une connaissance intermédiaire de CSS est requise pour styliser les petits composants que nous allons créer dans cet article.
* **Styled components** – Vous devez être familiarisé avec ce que sont les styled-components, car nous allons les utiliser pour créer une version d'un composant qui contient du CSS statique/dynamique. Vous pouvez en apprendre davantage sur les styled-components [ici](https://styled-components.com/).
* **Modèle composé** – Nous utiliserons ce modèle pour assembler les composants individuels afin qu'ils puissent être utilisés plus tard de manière pratique. Vous pouvez en lire davantage sur le modèle composé [ici](https://www.patterns.dev/posts/compound-pattern).
* **TypeScript** – Nous utiliserons [TypeScript](https://www.typescriptlang.org/docs/) dans ce tutoriel entier. Il offre une bonne sécurité de type en plus de JavaScript. Avoir quelques connaissances de base à ce sujet sera définitivement fructueux ici.

## Comment construire le composant Banner

Le GIF ci-dessous représente un composant carousel d'images. Si vous ne savez pas ce qu'est un carousel d'images, alors laissez-moi vous donner un bref aperçu.

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-98.png)

Un carousel d'images est un composant qui consiste en des images qui tournent un nombre fixe de fois ou peuvent être tournées à l'aide d'icônes de navigation. 

Dans ce tutoriel, nous allons créer ce composant. Mais avant de nous lancer dans le carousel d'images, nous allons commencer par un composant très basique qui est le composant Banner. 

Le composant Banner va être un composant qui nous aidera à afficher :

- Titre
- Tags
- Description
- Image de fond


Après cela, avec l'aide de [styled-components](https://styled-components.com/) et CSS, nous allons le rendre beau comme nous le voyons sur la plupart des plateformes OTT.

La construction de ce composant implique les étapes suivantes :

1. Construire les composants individuels
2. Assembler tous les composants avec le modèle composé

## Comment construire les composants individuels

![Image](https://www.freecodecamp.org/news/content/images/2023/06/Screenshot-2023-06-03-at-8.33.17-AM.png)

Notre composant banner sera composé de quelques composants plus petits et basiques qui ne peuvent pas être davantage décomposés. Ces composants sont connus sous le nom de [composants atomiques](https://blog.logrocket.com/atomic-design-react-native/). Commençons par construire le composant le plus simple qui est le composant Title :

Tout d'abord, créez un composant fonctionnel comme ci-dessous :

```tsx
const Title = (props: { title: string }) => <div>{props.title}</div>;

```

Nous devons également styliser ce composant. Nous créons un composant div stylisé et le plaçons à l'intérieur du composant Title ci-dessus comme ceci :

```tsx
const StyledTitle = styled.div`
  font-size: 28px;
  font-weight: 600;
  color: white;
`;

const Title = (props: { title: string }) => (
  <StyledTitle>{props.title}</StyledTitle>
);

```

Le prochain composant dans notre ligne est le composant `Tags`. C'est un élément div qui mappe sur la chaîne (tags) et les affiche dans l'élément `span` :

Créez un composant fonctionnel qui accepte un tableau de chaînes comme prop et les affiche dans l'élément span avec une fonction map :

```tsx
const Tags = (props: { tags: string[] }) => {
  return (
    <div>
      {props.tags.map((tag: string, index: number) => (
        <span key={`tag-${tag}-index`}>{tag}</span>
      ))}
    </div>
  );
};

```

Maintenant, créons un composant div stylisé qui agit comme un remplacement pour l'élément div ci-dessus. Nous créons ce composant wrapper pour appliquer des styles aux éléments enfants :

```tsx
const StyledTag = styled.div`
  padding: 0.5rem 0;

  & span {
    margin-right: 0.5rem;
    font-size: 1rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.6);
  }
`;

```

Enfin, nous assemblons ces composants ensemble :

```tsx
const Tags = (props: { tags: string[] }) => {
  return (
    <StyledTag>
      {tags.map((tag: string, index: number) => (
        <span key={`tag-${tag}-index`}>{tag}</span>
      ))}
    </StyledTag>
  );
};

```

De même, nous créons un autre composant appelé le composant `Description`. Il aide à afficher la description du titre du film. C'est aussi un composant fonctionnel qui accepte une prop de description et l'affiche en utilisant un styled-component :

```tsx
const StyledDescription = styled.div`
  text-align: start;
  color: rgba(255, 255, 255, 0.8);
  display: -webkit-box;
  max-width: 50%;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
`;

const Description = (props: { description: string }) => (
  <StyledDescription>{description}</StyledDescription>
);

```

Enfin, nous allons créer le composant `Banner`. Le but de ce composant est d'afficher l'image de fond du titre du film ainsi que les enfants qui lui sont passés. Créons une version très basique de ce composant :

```tsx
const Banner = (props) => {
  return (
    <div
      style={{
        backgroundImage: `url(${props.image})`,
        width: "100%",
        height: "400px",
      }}
    >
      <div>{props.children}</div>
    </div>
  );
};

<Banner image="https://m.media-amazon.com/images/M/MV5BZjRlNDUxZjAtOGQ4OC00OTNlLTgxNmQtYTBmMDgwZmNmNjkxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg">
  <h1 style={{ color: "yellow" }}>Die hard</h1>
</Banner>;

```

Si nous exécutons ce composant, il fait ce que nous attendons de lui, "Afficher une image de fond avec le composant enfant" comme ci-dessous :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-101.png)

Mais le style semble être décalé – nous ne voulons pas que ce composant ait l'air aussi laid. Ce dont nous avons besoin, c'est d'appliquer du CSS pour mettre les choses aux bons endroits aux bonnes positions 😂 (jeu de mots intentionnel). 

Nous voulons que l'affiche du film soit à droite et que tous les composants enfants soient à gauche. Maintenant, créons un composant stylisé pour faire cela :

```tsx
const StyledContainer = styled.div`
  height: 400px;
  width: 100%;
  display: flex;
  background-image: linear-gradient(90deg, rgba(0, 0, 0, 1) 60%, transparent),
    url(${(props) => props.image});
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right;

  & > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding-left: 10px;
  }
`;

const Banner = (props) => {
  return (
    <StyledContainer image={props.image}>
      <div>{props.children}</div>
    </StyledContainer>
  );
};

<Banner image="https://m.media-amazon.com/images/M/MV5BZjRlNDUxZjAtOGQ4OC00OTNlLTgxNmQtYTBmMDgwZmNmNjkxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg">
  <h1 style={{ color: "yellow" }}>Die hard</h1>
</Banner>;

```

Nous avons créé un nouveau composant stylisé appelé `StyledContainer`. Il contient du CSS qui alignera l'image à droite et appliquera un dégradé noir autour du conteneur de sorte que seul le titre du film soit visible. 

Ensuite, dans la section `& > div`, nous nous assurons que tous les composants enfants sont alignés à gauche. Voici à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-103.png)

Youpi ! notre composant Banner est prêt. Testons maintenant ce composant banner avec tous les composants que nous avons créés ci-dessus. Placez les composants `Title`, `Tags` et `Description` à l'intérieur du composant `Banner` comme ci-dessous :

```tsx
<Banner image="https://m.media-amazon.com/images/M/MV5BZjRlNDUxZjAtOGQ4OC00OTNlLTgxNmQtYTBmMDgwZmNmNjkxXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_.jpg">
  <Title title="Die Hard" />
  <Tags tags={["Action", "Thriller"]} />
  <Description description="Le plan du flic du NYPD John McClane de se réconcilier avec sa femme séparée est jeté dans une boucle sérieuse lorsque, quelques minutes après son arrivée à son bureau, tout le bâtiment est pris d'assaut par un groupe de terroristes. Avec peu d'aide de la part du LAPD, McClane, qui fait des blagues, se lance pour sauver les otages et faire tomber les méchants." />
</Banner>;

```

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-104.png)
_C'est ainsi que notre composant Banner apparaîtra._

## Comment assembler tous les composants avec le modèle composé

Nous voulons que notre composant Banner soit facile à utiliser et qu'il soit flexible. Nous pouvons assembler les composants Title, Tags et Description dans le composant Banner à l'aide d'un modèle composé. 

Les composants créés avec ce modèle partagent l'état et la logique entre leurs composants internes. Un exemple d'un tel modèle composé est un [composant Menu fourni par semantic UI.](https://react.semantic-ui.com/collections/menu/#types-basic)

```tsx
<Menu>
  <Menu.Item />
</Menu>;

```

L'avantage d'utiliser un tel modèle est que nous devons simplement importer un composant – dans notre cas, nous importerons simplement le composant Banner. Tous ses composants internes peuvent être utilisés directement comme ci-dessous :

```tsx
<Banner.Title />
<Banner.Tags />
<Banner.Description />
```

Maintenant, commençons à faire de même pour notre composant Banner.

Puisque nous avons tous les composants prêts, je les ai placés dans un seul fichier :

```tsx
import "./styles.css";
import styled from "styled-components";
import React from "react";

export type BannerProps = {
  title: string,
  tags: string[],
  description: string,
  image: string,
};

const StyledTitle = styled.div`
  font-size: 28px;
  font-weight: 600;
  color: white;
`;

const StyledTag = styled.div`
  padding: 0.5rem 0;

  & span {
    margin-right: 0.5rem;
    font-size: 1rem;
    font-weight: 500;
    color: rgba(255, 255, 255, 0.6);
  }
`;

const StyledDescription = styled.div`
  text-align: start;
  color: rgba(255, 255, 255, 0.8);
  display: -webkit-box;
  max-width: 50%;
  -webkit-line-clamp: 4;
  -webkit-box-orient: vertical;
  overflow: hidden;
`;
const Container = styled.div`
  height: 400px;
  width: 100%;
  display: flex;
  background-image: linear-gradient(90deg, rgba(0, 0, 0, 1) 60%, transparent),
    url(${(props: Pick<BannerProps, "image">) => props.image});
  background-size: contain;
  background-repeat: no-repeat;
  background-position: right;

  & > div {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: flex-start;
    padding-left: 10px;
  }
`;

const Title = ({ title }: Pick<BannerProps, "title">) => (
  <StyledTitle>{title}</StyledTitle>
);

const Tags = ({ tags }: Pick<BannerProps, "tags">) => {
  return (
    <StyledTag>
      {tags.map((tag) => (
        <span key={`tag-${tag}`}>{tag}</span>
      ))}
    </StyledTag>
  );
};

const Description = ({ description }: Pick<BannerProps, "description">) => (
  <StyledDescription>{description}</StyledDescription>
);

const Banner = (props: any) => {
  return (
    <Container image={props.image}>
      <div>{props.children}</div>
    </Container>
  );
};

Banner.Title = Title;
Banner.Tags = Tags;
Banner.Description = Description;

export default Banner;

```

Explication rapide du code ci-dessus :

Tout d'abord, nous créons les typages pour le composant Banner appelés BannerProps. Cela ressemble à ceci :

```tsx
export type BannerProps = {
  title: string;
  tags: string[];
  description: string;
  image: string;
};
```

Ensuite, nous plaçons tous les composants atomiques que nous avons créés ici. Nous nous assurons également d'utiliser le type BannerProps dans chaque définition de fonction des composants atomiques, par exemple :

```tsx
const Title = ({ title }: Pick<BannerProps, "title">) => (
  <StyledTitle>{title}</StyledTitle>
);

```

Comme vous pouvez le voir, nous utilisons la fonction utilitaire Pick de TypeScript pour sélectionner uniquement la prop title des props Banner.

Enfin, nous assemblons tous ces composants en créant une nouvelle propriété pour le composant Banner comme ci-dessous et exportons ce composant :

```tsx
Banner.Title = Title;
Banner.Tags = Tags;
Banner.Description = Description;

export default Banner;
```

**NOTE :** Pour les besoins de ce tutoriel, nous utilisons le modèle composé, mais vous pouvez utiliser ces composants atomiques indépendamment. J'ai choisi d'utiliser le modèle composé ici pour vous apprendre à l'utiliser. Vous pouvez l'appliquer dans différents scénarios comme lors de la construction d'un bouton de sélection ou d'un composant de menu.

Bon travail – nous avons enfin assemblé tous nos composants atomiques en un seul composant Banner. Dans la section suivante, nous allons parler de l'utilisation de ce composant.

## Comment construire le composant Carousel d'images

Enfin, nous sommes arrivés au point où nous pouvons construire le composant carousel d'images. Dans cette section, nous allons faire les choses suivantes :

* Construire un composant Banner Tile qui agira comme une seule image à l'intérieur du carousel
* Construire le composant carousel d'images.

Commençons par créer le composant Banner Tile. L'intention de ce composant est d'utiliser le composant `Banner`. 

Tout d'abord, nous allons commencer par créer des données d'exemple que nous pourrons parcourir. Créez un fichier nommé `sampledata.json` et placez le contenu suivant à l'intérieur :

```json
{
  "data": [
    {
      "title": "The Last of Us",
      "genres": ["Drama"],
      "cover_url": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/uKvVjHNqB5VmOrdxqAt2F7J78ED.jpg",
      "description": "Vingt ans après que la civilisation moderne a été détruite, Joel, un survivant endurci, est engagé pour faire passer en contrebande Ellie, une fille de 14 ans, hors d'une zone de quarantaine oppressive. Ce qui commence comme un petit travail devient bientôt un voyage brutal et déchirant, alors qu'ils doivent tous deux traverser les États-Unis et dépendre l'un de l'autre pour survivre."
    },
    {
      "title": "Fight Club",
      "genres": ["Drama", "Thriller", "Comedy"],
      "cover_url": "https://www.themoviedb.org/t/p/w300_and_h450_bestv2/pB8BM7pdSp6B6Ih7QZ4DrQ3PmJK.jpg",
      "description": "Un insomniaque à la bombe à retardement et un vendeur de savon glissant canalisent l'agressivité masculine primordiale en une nouvelle forme de thérapie choquante. Leur concept prend de l'ampleur, avec des clubs de combat souterrains se formant dans chaque ville, jusqu'à ce qu'un excentrique se mette en travers de leur chemin et enflamme une spirale incontrôlable vers l'oubli."
    },
    {
      "title": "Creed III",
      "genres": ["Drama", "Thriller"],
      "cover_url": "https://www.themoviedb.org/t/p/w600_and_h900_bestv2/cvsXj3I9Q2iyyIo95AecSd1tad7.jpg",
      "description": "Après avoir dominé le monde de la boxe, Adonis Creed a prospéré à la fois dans sa carrière et sa vie familiale. Lorsque un ami d'enfance et ancien prodige de la boxe, Damien Anderson, réapparaît après avoir purgé une longue peine de prison, il est impatient de prouver qu'il mérite sa chance sur le ring. L'affrontement entre anciens amis est plus qu'un simple combat. Pour régler ses comptes, Adonis doit mettre son avenir en jeu pour combattre Damien - un combattant qui n'a rien à perdre."
    },
    {
      "title": "Die Hard",
      "genres": ["Action", "Thriller"],
      "cover_url": "https://www.themoviedb.org/t/p/w1280/yFihWxQcmqcaBR31QM6Y8gT6aYV.jpg",
      "description": "Le plan du flic du NYPD John McClane de se réconcilier avec sa femme séparée est jeté dans une boucle sérieuse lorsque, quelques minutes après son arrivée à son bureau, tout le bâtiment est pris d'assaut par un groupe de terroristes. Avec peu d'aide de la part du LAPD, McClane, qui fait des blagues, se lance pour sauver les otages et faire tomber les méchants."
    }
  ]
}
```

**NOTE :** J'ai utilisé [themoviedb.org](http://themoviedb.org/) pour obtenir les données ci-dessus.

Ensuite, créez un fichier nommé `BannerTile.tsx` dans le répertoire `components`. Créez ensuite un composant fonctionnel qui utilise le composant Banner comme ci-dessous :

```tsx
import Banner, { BannerProps } from "./Banner";

export default function BannerTile(props: BannerProps) {
  const { title, image, tags, description } = props;
  return (
    <Banner image={image}>
      <Banner.Title title={title} />
      <Banner.Tags tags={tags} />
      <Banner.Description description={description} />
    </Banner>
  );
}

```

Pour tester ce composant, nous pouvons utiliser `sampledata.json`. Suivez les étapes suivantes pour tester le composant `BannerTile` :

Tout d'abord, nous devons importer les données depuis sampledata.json :

```tsx
const sampleData = require('./sampledata.json');
```

Ensuite, nous parcourons ces données avec la fonction map. Nous nous assurons également d'appeler le composant `BannerTile` sur chacune des données :

```tsx
<div>
  {sampleData.data.map((item: SampleData, index: number) => (
    <BannerTile
      key={`key-${item.title}-${index}`}
      title={item.title}
      tags={item.genres}
      image={item.cover_url}
      description={item.description}
    />
  ))}
</div>;

```

Le résultat après l'exécution de ce code ressemblera à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-121.png)

Pour implémenter le carousel d'images, nous pouvons utiliser un package appelé [Swiper](https://swiperjs.com/get-started). Nous devons simplement placer tous les `BannerTiles` à l'intérieur du composant fourni par le swiper. Maintenant, sans plus tarder, commençons.

Pour installer le package swiper, utilisez la commande suivante :

```shell
npm i swiper

```

Maintenant, créons un nouveau fichier nommé `HeroBanner.tsx`. Ce fichier contiendra le composant `HeroBanner`. Le but de ce composant est de parcourir les données des films et de les afficher via le carousel d'images et le composant `BannerTile`.

Une fois que nous avons installé la bibliothèque swiper, nous pouvons commencer à l'utiliser. Selon la documentation de swiper.js, nous devons importer le CSS fourni par celle-ci :

```tsx
import "swiper/css";
import "swiper/css/navigation";
```

Ensuite, nous devons également importer les composants de swiper.js qui nous aideront à construire le carousel d'images. Importez les composants suivants :

```tsx
import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation } from "swiper";
```

Maintenant, importons également le `BannerTile`, les types associés au Banner, et le `sampleData` depuis le `sampledata.json` :

```tsx
import "swiper/css";
import "swiper/css/navigation";

import { Swiper, SwiperSlide } from "swiper/react";
import { Navigation } from "swiper";

import BannerTile from "./BannerTile";
import { BannerProps } from "./Banner";

const sampleData = require("../utilities/sampledata.json");
```

Les `sampleData` que nous avons importés contiennent uniquement le titre, les genres, l'URL de couverture et la description. C'est le moment idéal pour utiliser le type `BannerProps` afin de filtrer uniquement les types dont nous avons besoin. 

```tsx
type SampleData = Pick<BannerProps, 'title' | 'description'> & {
	genres: string[];
  cover_url: string;
}
```

Maintenant, commençons à construire ce composant. Créez un composant fonctionnel appelé `HeroBanner` et placez le code suivant à l'intérieur :

```tsx
const HeroBanner = () => (
  <Swiper navigation modules={[Navigation]} slidesPerView={1}>
    {sampleData.data.map((item: SampleData, index: number) => (
      <SwiperSlide key={`key-${item.title}-${index}`}>
        <BannerTile
          title={item.title}
          tags={item.genres}
          image={item.cover_url}
          description={item.description}
        />
      </SwiperSlide>
    ))}
  </Swiper>
);
```

Dans le composant HeroBanner, nous faisons les choses suivantes :

* Nous utilisons le composant `Swiper` fourni par la bibliothèque swiper.js qui agit comme un conteneur wrapper autour de toutes les images, c'est-à-dire le composant `BannerTile`. Nous nous sommes assurés qu'il n'y a qu'une seule diapositive par vue.
* En parcourant le `sampleData`, nous nous assurons que chaque composant `BannerTile` est enveloppé par le composant `SwiperSlide`.

Pour en savoir plus sur les composants React de swiper, vous pouvez vous référer à leur [documentation](https://swiperjs.com/react).

Le résultat final ressemblera à quelque chose comme ceci :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-122.png)

Nous avons enfin obtenu ce que nous voulions : un composant carousel d'images qui ressemble et fonctionne comme ceux des plateformes OTT populaires. 

Mais il y a une dernière chose que nous devons faire ici. Nous devons nous assurer que les flèches gauche et droite sont blanches pour qu'elles se détachent. Pour cela, nous utilisons les styled-components :

```tsx
export const StyledSwiper = styled(Swiper)`
  & .swiper-button-next,
  .swiper-button-prev {
    color: white;
  }
`;
```

Maintenant, nous modifions notre composant HeroBanner. Nous remplaçons le composant Swiper par le composant StyledSwiper comme ci-dessous :

```tsx
const HeroBanner = () => (
  <StyledSwiper navigation modules={[Navigation]} slidesPerView={1}>
    {sampleData.data.map((item: SampleData, index: number) => (
      <SwiperSlide key={`key-${item.title}-${index}`}>
        <BannerTile
          title={item.title}
          tags={item.genres}
          image={item.cover_url}
          description={item.description}
        />
      </SwiperSlide>
    ))}
  </StyledSwiper>
);
```

Voici à quoi cela ressemblera :

![Image](https://www.freecodecamp.org/news/content/images/2023/05/image-123.png)
_Cela a l'air bien maintenant_

## Résumé

Voici comment vous pouvez créer un carousel d'images pour les titres de films. Dans ce tutoriel, vous avez appris :

* Comment créer des composants atomiques
* Comment assembler tous les composants avec le modèle composé
* Comment créer un composant BannerTile qui affiche les informations liées à chaque film
* Comment construire un composant carousel d'images avec swiper.js

L'ensemble du code de ce tutoriel peut être trouvé [ici](https://codesandbox.io/s/image-carousel-52hnep?file=/src/App.tsx).

Merci d'avoir lu !

Suivez-moi sur [twitter](https://twitter.com/keurplkar), [github](http://github.com/keyurparalkar), et [linkedIn](https://www.linkedin.com/in/keyur-paralkar-494415107/).