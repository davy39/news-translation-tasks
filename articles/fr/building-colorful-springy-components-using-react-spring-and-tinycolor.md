---
title: Création de composants colorés et dynamiques avec React Spring et Tinycolor
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-07-05T15:49:59.000Z'
originalURL: https://freecodecamp.org/news/building-colorful-springy-components-using-react-spring-and-tinycolor
coverImage: https://www.freecodecamp.org/news/content/images/2019/07/philip-veater-AKmdNgzZESM-unsplash-1.jpg
tags:
- name: Accessibility
  slug: accessibility
- name: Design
  slug: design
- name: JavaScript
  slug: javascript
- name: React
  slug: react
- name: UX
  slug: ux
seo_title: Création de composants colorés et dynamiques avec React Spring et Tinycolor
seo_desc: 'By Stephen McLean

  Recently, I decided to build a web application to allow designers and developers
  to generate variants for colors and to check color accessibility. In this post,
  I would like to give you a walkthrough of how I built some of the compo...'
---

Par Stephen McLean

Récemment, j'ai décidé de créer [une application web](https://rainbo.xyz/) pour permettre aux designers et développeurs de générer des variantes de couleurs et de vérifier l'accessibilité des couleurs. Dans cet article, je souhaite vous guider à travers la création de certains des composants que j'ai utilisés dans cette application.

Le code source complet de l'application peut être trouvé à la fin de cet article, ainsi qu'un lien vers une instance Storybook contenant tous les composants décrits.

## Dépendances

Pour m'aider à créer ces composants, j'ai utilisé [Tinycolor](https://github.com/bgrins/TinyColor), une bibliothèque avec une gamme de fonctions utilitaires pour manipuler, transformer et représenter les couleurs.

J'ai également utilisé [React Spring](https://www.react-spring.io/), une bibliothèque basée sur la physique des ressorts qui permet d'ajouter facilement des animations à votre projet.

## Tuile de couleur

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Color-Tile-1.png)
_Designs de tuiles de couleur_

Le composant le plus simple de notre liste, la tuile de couleur servira de bloc de construction pour d'autres composants. La responsabilité de ce composant est d'afficher une couleur, ainsi que son nom et sa valeur HEX.

```javascript
const TILE_SIZES = {
  sm: "2.5rem",
  md: "4rem",
  lg: "6rem"
};

const ColorTile = ({
  color,
  name,
  hideName,
  hideHex,
  size,
  className,
  customTileStyle,
  ...otherProps
}) => {
  const containerClass = cx(styles.container, className);

  const tileClass = cx(styles.tile, {
    "margin-bottom--xxs": !hideName || !hideHex
  });
  const dimension = TILE_SIZES[size];
  const tileStyle = {
    "--color-tile-width": dimension,
    "--color-tile-height": dimension,
    "--color-tile-bg": color,
    "--color-tile-border-color": "transparent",
    ...customTileStyle
  };
  const tile = <div style={tileStyle} className={tileClass} />;

  const nameClass = cx("text--colors-grey-lighten-30", {
    "margin-bottom--xxs": !hideHex
  });

  const hex = useMemo(() => tinycolor(color).toHexString(), [color]);
  return (
    <div className={containerClass} {...otherProps}>
      {tile}
      {!hideName && <small className={nameClass}>{name}</small>}
      {!hideHex && (
        <small className="text--colors-grey-lighten-30">{hex}</small>
      )}
    </div>
  );
};

ColorTile.propTypes = {
  /**
   * Couleur à afficher
   */
  color: PropTypes.string.isRequired,
  /**
   * Nom de la couleur
   */
  name: PropTypes.string,
  /**
   * Masquer le texte du nom si vrai
   */
  hideName: PropTypes.bool,
  /**
   * Masquer l'affichage de la valeur hexadécimale de la couleur si vrai
   */
  hideHex: PropTypes.bool,
  /**
   * Taille de la tuile
   */
  size: PropTypes.oneOf(["sm", "md", "lg"]),
  /**
   * Styles personnalisés à appliquer à l'élément de tuile
   */
  customTileStyle: PropTypes.object
};

ColorTile.defaultProps = {
  size: "md",
  hideName: true,
  hideHex: true,
  customTileStyle: {}
};
```

#### Notes sur l'implémentation

1. Les lignes 17 et 19 peuvent sembler légèrement étranges si vous n'êtes pas familier avec l'excellente bibliothèque [classnames](https://www.npmjs.com/package/classnames). Basiquement, la bibliothèque classnames permet de concaténer et d'appliquer conditionnellement des classes CSS à vos éléments.
2. À la ligne 36, vous pouvez voir que nous calculons la chaîne HEX de la couleur passée. Puisque nous utilisons la propriété de couleur passée directement dans le CSS, elle peut être dans n'importe quel format de couleur CSS acceptable, pas seulement HEX. Cela pourrait être une chaîne rgba par exemple. C'est là que Tinycolor intervient. Nous pouvons lui donner n'importe lequel de ces formats et il retourne une chaîne HEX bien formatée que nous pouvons afficher avec notre tuile.
3. En restant à la ligne 36, vous avez peut-être également remarqué que la fonction pour calculer la chaîne HEX est enveloppée dans `useMemo`. Cela est dû au fait que nous voulons calculer cette valeur uniquement si la couleur change. Nous pouvons éviter de recalculer si l'une des autres propriétés change, ce qui pourrait causer un nouveau rendu. Je suis encore en train d'apprendre la nouvelle API Hooks, donc cela pourrait ne pas être l'utilisation la plus appropriée de `useMemo` puisque ce n'est probablement pas une opération particulièrement coûteuse, mais je pense que c'était une bonne façon de la gérer quoi qu'il en soit. Vous pouvez en apprendre plus sur la fonction `useMemo` ou les Hooks en général [ici](https://reactjs.org/docs/hooks-reference.html#usememo).

```css
.tile {
  width: var(--color-tile-width);
  height: var(--color-tile-height);
  background-color: var(--color-tile-bg);
  border: 3px solid var(--color-tile-border-color);
  cursor: pointer;
}

.container {
  display: inline-flex;
  flex-direction: column;
  align-items: center;
}
```

#### Notes sur le style

Le style de notre tuile est vraiment simple. Nous avons la tuile elle-même qui prend ses dimensions et sa couleur à partir des variables que nous passons.

Ensuite, nous avons le conteneur qui contient la tuile, le nom de la couleur et la valeur HEX. C'est un simple conteneur flex qui maintient nos éléments alignés.

## Sélecteur de couleur

![Image](https://cdn-media-1.freecodecamp.org/images/1*60aXsgfuTUd0yYPBvhl71w.png)
_Designs de sélecteur de couleur_

Pour notre sélecteur de couleur, nous allons réutiliser le composant Color Tile, ainsi qu'un sélecteur du package [react-color](https://casesandberg.github.io/react-color/).

```javascript
import React, { useState } from "react";
import PropTypes from "prop-types";
import { ChromePicker } from "react-color";

import ColorTile from "../ColorTile/ColorTile";

import styles from "./ColorPicker.module.scss";

const ColorPicker = ({ color, onChange, className, tileClassName }) => {
  const [isPickerOpen, setPickerOpen] = useState(false);

  const onSwatchClick = () => {
    setPickerOpen(!isPickerOpen);
  };

  const onColorChange = color => {
    onChange(color.hex);
  };

  return (
    <div className={className}>
      <ColorTile
        color={color}
        onClick={onSwatchClick}
        hideHex={false}
        size="lg"
        className={tileClassName}
      />

      {isPickerOpen && (
        <div className={styles.popover}>
          <div className={styles.cover} onClick={onSwatchClick} />
          <ChromePicker color={color} onChangeComplete={onColorChange} />
        </div>
      )}
    </div>
  );
};

ColorPicker.propTypes = {
  /**
   * Valeur de couleur actuellement sélectionnée
   */
  color: PropTypes.string,
  /**
   * Fonction de rappel pour lorsque la couleur change
   */
  onChange: PropTypes.func,
  /**
   * Classes personnalisées à appliquer à la tuile de couleur
   */
  tileClassName: PropTypes.string
};

ColorPicker.defaultProps = {
  onChange: () => {}
};

export default ColorPicker;
```

#### Notes sur l'implémentation

Notre sélecteur de couleur est composé d'un `ColorTile` qui montre la couleur actuellement sélectionnée, ainsi que sa valeur HEX, et un `ChromePicker` de la bibliothèque `react-color` qui nous permet effectivement de sélectionner une couleur.

Nous avons un état qui contrôle si le `ChromePicker` est visible ou non, et une fonction de rappel pour informer le composant utilisant notre sélecteur lorsque la couleur change. `react-color` fournit beaucoup d'informations lorsque la couleur change, mais la valeur hexadécimale était suffisante pour mes besoins, comme vous pouvez le voir à la ligne 17.

## Liste de couleurs

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Color-List--1-.png)
_Designs de liste de couleurs_

Notre composant Color List prend une liste de couleurs et les affiche sous forme de liste contenant des tuiles de couleur. Notre Color List est destinée à montrer une couleur de base sous forme de tuile légèrement plus grande, les tuiles restantes représentant les variantes de la base affichées sous forme de tuiles plus petites. Nous permettons également de nommer notre liste, et cela sera utilisé pour afficher le nom de la couleur de base.

Notre Color List apporte également la partie "dynamique" de ce guide. Les tuiles seront animées à l'entrée en utilisant React Spring.

```javascript
const ROW_DIRECTION = "row";
const COL_DIRECTION = "col";
const ALL_DIRECTIONS = [ROW_DIRECTION, COL_DIRECTION];

/**
 * Affiche une liste de couleurs
 */
const ColorPaletteList = ({
  name,
  colors,
  direction,
  onColorClick,
  onColorDoubleClick,
  animationRef,
  getCustomTileStyle,
  renderTileBy,
  ...otherProps
}) => {
  const headingClass = cx("margin-bottom--xs", {
    "text--align-left": direction === ROW_DIRECTION,
    "text--align-center": direction === COL_DIRECTION
  });

  const containerClass = cx({
    [styles.containerCol]: direction === COL_DIRECTION,
    [styles.containerRow]: direction === ROW_DIRECTION
  });

  const tileClass = cx({
    "margin-bottom--xs": direction === COL_DIRECTION,
    "margin-right--xs": direction === ROW_DIRECTION
  });

  const trailMargin =
    direction === COL_DIRECTION ? "marginBottom" : "marginRight";
  const trails = useTrail(colors.length, {
    from: { [trailMargin]: 20, opacity: 0 },
    to: { [trailMargin]: 0, opacity: 1 },
    ref: animationRef
  });

  return (
    <div {...otherProps}>
      <h4 className={headingClass}>{name || ""}</h4>
      <div className={containerClass}>
        {trails.map((trailProps, idx) => {
          const color = colors[idx];
          const onClick = () => onColorClick(color);
          return (
            <animated.div
              key={`animated-tile-${color.name}-${idx}`}
              style={trailProps}
            >
              {renderTileBy(color, tileClass, onClick, false, false)}
            </animated.div>
          );
        })}
      </div>
    </div>
  );
};

ColorPaletteList.propTypes = {
  /**
   * Nom de la liste
   */
  name: PropTypes.string,
  /**
   * La liste des couleurs à afficher
   */
  colors: PropTypes.arrayOf(
    PropTypes.shape({
      color: PropTypes.string,
      name: PropTypes.string,
      isMain: PropTypes.bool
    })
  ).isRequired,
  /**
   * Détermine la disposition des tuiles
   */
  direction: PropTypes.oneOf(ALL_DIRECTIONS),
  /**
   * Rappel pour lorsqu'une couleur dans la liste est cliquée
   */
  onColorClick: PropTypes.func,
  /**
   * Référence utilisée pour s'accrocher à l'animation
   */
  animationRef: PropTypes.object,
  /**
   * Passer des styles personnalisés pour une tuile de couleur particulière
   */
  getCustomTileStyle: PropTypes.func,
  /**
   * Prop de rendu pour rendre la tuile de couleur
   */
  renderTileBy: PropTypes.func
};

ColorPaletteList.defaultProps = {
  direction: COL_DIRECTION,
  onColorClick: () => {},
  onColorDoubleClick: () => {},
  getCustomTileStyle: () => ({}),
  renderTileBy: (color, className, onClick, hideName, hideHex) => (
    <ColorTile
      key={color.name}
      color={color.color}
      name={color.name}
      size={color.isMain ? "lg" : "md"}
      className={className}
      onClick={onClick}
      hideName={hideName}
      hideHex={hideHex}
    />
  )
};
```

#### Notes sur l'implémentation

1. Aux lignes 34-40, vous pouvez voir notre implémentation de React Spring en utilisant `useTrail`. Vous pouvez en lire plus sur les trails [ici](https://www.react-spring.io/docs/hooks/use-trail). Nous animons la marge sur le conteneur de tuiles de couleur et, selon que la liste est alignée en colonne ou en ligne, cela pourrait être la marge à droite ou en bas.
2. À la ligne 39, vous pouvez voir que nous passons une référence à notre animation. Cela nous permet de passer une référence à notre Color List pour retarder l'animation. Cela serait utile si nous voulions déclencher une séquence spécifique d'animations à partir d'un composant parent.

```css
.containerCol {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

.containerRow {
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: wrap;
}
```

## Paire de couleurs

![Image](https://www.freecodecamp.org/news/content/images/2019/07/Accessible-Pair--1-.png)
_Designs de paire de couleurs_

Le composant Color Pair prend deux couleurs et les affiche côte à côte avec des informations d'accessibilité. L'idée est qu'un développeur ou un designer associerait des couleurs pour s'assurer qu'elles fonctionnent ensemble lorsqu'elles sont utilisées comme combinaison arrière-plan/premier plan.

```javascript
const AccessiblePair = ({
  background,
  foreground,
  hideCloseBtn,
  onCloseBtnClick,
  closeBtnIcon,
  ...otherProps
}) => {
  const title = `${background.name}/${foreground.name}`;

  const bgTileStyle = {
    "--tile-color": background.color
  };

  const fgTileStyle = {
    "--tile-color": foreground.color
  };

  const tileContainerClass = cx(styles.tileContainer, "margin-right--sm");
  const titleContainerClass = cx(
    styles.titleContainer,
    "margin-bottom--xxs",
    "text--colors-grey-lighten-30"
  );

  const isAAPass = tinycolor.isReadable(background.color, foreground.color, {
    level: "AA",
    size: "small"
  });
  const isAAAPass = tinycolor.isReadable(background.color, foreground.color, {
    level: "AAA",
    size: "small"
  });

  const aaDisplayText = "WCAG AA";
  const aaaDisplayText = "WCAG AAA";
  const aaPillType = isAAPass ? "success" : "error";
  const aaaPillType = isAAAPass ? "success" : "error";

  const examplePillStyle = {
    "--pill-background": background.color,
    "--pill-color": foreground.color
  };

  return (
    <div {...otherProps}>
      <div className={titleContainerClass}>
        <small className={styles.title}>{title}</small>
        {!hideCloseBtn && (
          <FontAwesomeIcon icon={closeBtnIcon} onClick={onCloseBtnClick} />
        )}
      </div>
      <div className={styles.mainContent}>
        <div className={tileContainerClass}>
          <div style={bgTileStyle} className={styles.tile} />
          <div style={fgTileStyle} className={styles.tile} />
        </div>

        <div className={styles.pillContainer}>
          <Pill type={aaPillType} className="margin-bottom--xxs">
            {aaDisplayText}
          </Pill>
          <Pill type={aaaPillType} className="margin-bottom--xxs">
            {aaaDisplayText}
          </Pill>
          <Pill style={examplePillStyle}>Voici comment le texte apparaîtra</Pill>
        </div>
      </div>
    </div>
  );
};

AccessiblePair.propTypes = {
  /**
   * La couleur de fond
   */
  background: colorShape.isRequired,
  /**
   * La couleur de premier plan
   */
  foreground: colorShape.isRequired,
  /**
   * Définir à vrai pour masquer le bouton de fermeture
   */
  hideCloseBtn: PropTypes.bool,
  /**
   * Rappel pour lorsque le bouton de fermeture est cliqué
   */
  onCloseBtnClick: PropTypes.func,
  /**
   * Icône FontAwesome à utiliser pour le bouton de fermeture
   */
  closeBtnIcon: PropTypes.string
};

AccessiblePair.defaultProps = {
  hideCloseBtn: false,
  onCloseBtnClick: () => {},
  closeBtnIcon: "times"
};
```

#### Notes sur l'implémentation

Comme mentionné, notre composant Color Pair prend une couleur de fond et une couleur de premier plan, et aux lignes 26-33, vous pouvez voir où nous utilisons Tinycolor pour déterminer l'accessibilité de la paire de couleurs.

Nous utilisons un simple composant Pill pour afficher le résultat avec le type de Pill étant déterminé par le résultat. Je n'ai pas montré la source du Pill ici, mais c'est un composant assez standard que vous trouveriez dans n'importe quelle bibliothèque de composants (Bootstrap, Material, etc).

Vous pouvez en apprendre plus sur l'accessibilité et le WCAG [ici](https://www.w3.org/WAI/standards-guidelines/wcag/).

## Conclusion et code source

J'espère que vous avez appris quelque chose de ce guide. Je recommande vivement de regarder les bibliothèques que j'ai mentionnées ici pour votre prochain projet. En particulier, mon application aurait pris beaucoup plus de temps à créer sans l'excellente bibliothèque Tinycolor.

> _Le code source de l'application complète peut être trouvé [ici](https://github.com/stephan-mclean/project-color)._

> _Une instance Storybook avec tous les composants peut être trouvée [ici](https://rainbo-components.netlify.com/)._

Si vous avez des commentaires sur les designs, le code, ou en général, j'adorerais les entendre.

Merci beaucoup d'avoir lu mon article !

_Publié à l'origine [ici](https://medium.com/better-programming/building-colorful-springy-components-using-react-spring-and-tinycolor-1086c6594203)._