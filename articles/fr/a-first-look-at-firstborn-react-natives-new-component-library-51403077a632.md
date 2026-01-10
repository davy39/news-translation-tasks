---
title: Un premier regard sur firstBorn, la nouvelle bibliothèque de composants de
  React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-04-16T16:21:13.000Z'
originalURL: https://freecodecamp.org/news/a-first-look-at-firstborn-react-natives-new-component-library-51403077a632
coverImage: https://cdn-media-1.freecodecamp.org/images/1*JtQqp-vPqOOfvcT_V6jkVQ.jpeg
tags:
- name: Design
  slug: design
- name: General Programming
  slug: programming
- name: React Native
  slug: react-native
- name: 'tech '
  slug: tech
- name: UX
  slug: ux
seo_title: Un premier regard sur firstBorn, la nouvelle bibliothèque de composants
  de React Native
seo_desc: 'By Sameeha Rahman

  [first-born](https://github.com/99xt/first-born) is a React Native UI Component
  Framework, which follows the design methodology Atomic Design by Brad Frost.

  Version 1.0.0 was recently published as an npm module on the 1st of April (...'
---

Par Sameeha Rahman

`[first-born](https://github.com/99xt/first-born)` est un Framework de composants UI pour React Native, qui suit la méthodologie de design [Atomic Design par Brad Frost](http://atomicdesign.bradfrost.com/chapter-2/).

La version 1.0.0 a été récemment publiée en tant que [module npm](https://www.npmjs.com/package/@99xt/first-born) le 1er avril (et ce n'est pas une blague...).

Dans cet article, nous allons voir une démonstration des composants existants offerts par `first-born`.

### La méthodologie de design

La méthodologie Atomic Design suit le principe selon lequel les interfaces utilisateur peuvent être décomposées en 5 phases différentes.

Selon cette méthodologie de design, les phases sont décrites comme suit :

* Atomes : Les éléments de base et autonomes, comme le texte, les icônes, les boutons ou les zones de texte.
* Molécules : Une combinaison de différents atomes, qui ensemble ont une meilleure valeur opérationnelle. Par exemple, une zone de texte avec une étiquette de texte pour expliquer le contenu ou afficher une erreur dans les données saisies.
* Organismes : Une combinaison de différentes molécules fonctionnant ensemble pour former des structures complexes. Par exemple, un formulaire composé de nombreuses molécules de zones de texte.
* Modèle : Une combinaison de différents organismes qui forment la base de la page. Cela inclut la mise en page et le contexte de ces organismes.
* Page : Tous les éléments ci-dessus fonctionnant ensemble dans une instance réelle, donne naissance à une page. C'est également la mise en œuvre réelle du modèle.

### Pour commencer

Commençons par créer une nouvelle application React Native en utilisant la CLI :

```
react-native init firstBornExample
```

Une fois créée, accédez au dossier de l'application :

```
cd firstBornExample
```

Pour ajouter `first-born` à l'application, installez-le comme suit :

```
npm i --save @99xt/first-born
```

`first-born` a deux autres dépendances que nous devons installer nous-mêmes.

```
npm i --save create-react-class react-native-vector-icons
```

Nous devrons ensuite suivre [ce guide](https://github.com/oblador/react-native-vector-icons#installation) pour configurer `react-native-vector-icons` pour l'application.

create-react-class n'a pas d'étapes de configuration supplémentaires.

Et nous sommes prêts à partir !

### Utilisation

Pour importer les composants, l'instruction ressemblera à ceci :

```js
import { <nom_du_composant> } from '@99xt/first-born'
```

Le module comprend les composants intégrés suivants :

#### Atomes

[**Texte**](https://github.com/99xt/first-born#text)

L'atome `Text` a un ensemble fixe de tailles. Ces tailles diffèrent selon la plateforme de l'application sous-jacente. Nous pouvons également passer une couleur à cet atome `Text`.

```js
<Text size="h4">exemple first-born</Text>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*7jJPnGkJJZrFZIftUhHF7g.png)
_Texte (Android)_

[**Icône**](https://github.com/99xt/first-born#icon)

L'atome `Icon` est construit sur la classe Ionicons de `react-native-vector-icons`. Ionicons propose deux rendus différents d'une même icône pour Android et iOS. Cette classe rendra l'icône en fonction de la plateforme sous-jacente.

```js
<Icon name="heart" color="red"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*PUTR7NmtSQ56wiYJBb6D3A.png)
_Icône (Android)_

[**Bouton**](https://github.com/99xt/first-born#button)

L'atome `Button` peut être rendu de plusieurs manières. Il n'accepte que les `Textes`, `Icônes` et `Images` comme éléments enfants à afficher. Il existe en 3 tailles différentes, ainsi qu'en 4 étiquettes différentes qui rendront le bouton dans de nombreuses combinaisons.

```js
render() {
    return (
      <View style={styles.container}>
        <Button size="small">
          <Text>Petit</Text>
        </Button>
        <Button >
          <Text>Par défaut</Text>
        </Button>
        <Button size="large">
          <Text>Grand</Text>
        </Button>
        <Button >
          <Icon name="heart" />
          <Text>Par défaut</Text>
        </Button>
        <Button rounded>
          <Icon name="heart" />
          <Text>Arrondi</Text>
        </Button>
        <Button block>
          <Icon name="heart" />
          <Text>Bloc</Text>
        </Button>
        <Button rounded block>
          <Icon name="heart" />
          <Text>{"Arrondi & Bloc"}</Text>
        </Button>
        <Button outline>
          <Icon name="heart" />
          <Text>Contour</Text>
        </Button>
        <Button outline transparent>
          <Icon name="heart" />
          <Text>{"Contour & Transparent"}</Text>
        </Button>
      </View>
    );
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*5L8jA5r6UmDOJlXRHp_M1g.gif)
_Boutons (Android)_

[**Entrée**](https://github.com/99xt/first-born#input)

L'atome `Input` est un `react-native TextInput` stylisé. Il affiche une bordure colorée à l'utilisateur si le TextInput est en focus. La méthode `onChangeText` est obligatoire.

```js
<Input placeholder="Nom" onChangeText={this.handleTextChange} />
...
handleTextChange = (text) => {
  this.setState({ text: text })
}
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*HV4fnn4A_FnBGoYOyDMDbg.gif)
_Entrée (Android)_

Cela prend également en charge l'indication d'une erreur à l'utilisateur. Pour utiliser cette fonctionnalité, nous devons créer une méthode de validation. Cette méthode doit retourner un booléen en fonction de la validité du texte saisi. Un tel scénario est de vérifier si une adresse e-mail suit le format conventionnel. Cette méthode est celle passée dans la propriété `isValid`.

```js
checkInputValidity = (text) => {
  const regex = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
  return regex.test(text);
}
...
<Input placeholder="Email" isValid={this.checkInputValidity} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*N0hTkCyRQ3FKQdx7nDXV3A.gif)
_Validation de l'entrée (Android)_

[**Zone de texte**](https://github.com/99xt/first-born#textarea)

L'atome `TextArea` est un `react-native TextInput` stylisé. Il affiche une bordure colorée à l'utilisateur si le TextInput est en focus. Il augmente également en hauteur avec plus de données saisies.

```js
<TextArea placeholder="Description"/>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*M8YCAvfmqFSIDUSTbasbEA.gif)
_Zone de texte (Android)_

[**Sélecteur**](https://github.com/99xt/first-born#picker)

L'atome `Picker` est un composant `react-native Picker` stylisé. Sur Android, le sélecteur est une liste déroulante qui s'étend à partir du composant `Picker` initial. Sur iOS, cliquer sur le `first-born Picker` ouvrira une modale pour que l'utilisateur choisisse la valeur.

```js
<Picker>
	<Picker.Item value="1" label="1" />
	<Picker.Item value="2" label="2" />
	<Picker.Item value="3" label="3" />
</Picker>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*5e5zk7wIKmZRuzw2Gvy--A.gif)
_Sélecteur (Android)_

[**Sélecteur de date**](https://github.com/99xt/first-born#datepicker)

L'atome `DatePicker` est un composant `react-native View` stylisé, qui ressemble à un `TextInput`. Sur Android, lorsque la `View` est cliquée, elle exécute l'[API](https://facebook.github.io/react-native/docs/datepickerandroid) `[DatePickerAndroid](https://facebook.github.io/react-native/docs/datepickerandroid)`. Sur iOS, cliquer sur la `View` ouvrira une modale pour que l'utilisateur choisisse la date à partir du composant `[DatePickerIOS](https://facebook.github.io/react-native/docs/datepickerios)`.

```js
<DatePicker />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*NNBTVrTRxq-BnhAd5Rwfwg.gif)
_Sélecteur de date (Android)_

#### Molécules

[**FormDatePicker**](https://github.com/99xt/first-born#formdatepicker)

Cette molécule utilise l'atome `DatePicker` et inclut l'atome `Text` comme étiquette. La propriété label de cet élément est obligatoire.

```js
<FormDatePicker label="Date" />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*OfW_Tlb2oBPAN9dIEhnzEg.png)
_FormDatePicker (Android)_

[**FormPicker**](https://github.com/99xt/first-born#formpicker)

Cette molécule utilise l'atome `Picker` et inclut l'atome `Text` comme étiquette. La propriété label de cet élément est obligatoire.

```js
<FormPicker label="Nombre">
	<Picker.Item value="1" label="1" />
	<Picker.Item value="2" label="2" />
	<Picker.Item value="3" label="3" />
</FormPicker>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*E0WRwIPgUlfQM2zAJRe1jQ.png)
_FormPicker (Android)_

Nous pouvons également passer des données sous forme de tableau d'objets, qui ont les clés `value` et `label`. Les données dans les deux clés doivent être de type String.

```js
pickerData = [
	{
		value: "1",
		label: "1"
	},
	{
		value: "2",
		label: "2"
	},
	{
		value: "3",
		label: "3"
	}
];
...
<FormPicker label="Nombre" pickerData={this.pickerData} />
```

[**FormInput**](https://github.com/99xt/first-born#forminput)

Cette molécule utilise l'atome `Input` et inclut l'atome `Text` comme étiquette. La propriété label de cet élément est obligatoire.

```js
<FormInput label="Nom" />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*WkEj7U4QjEMVVnzgKFUpyw.png)
_FormInput (Android)_

[**FormTextArea**](https://github.com/99xt/first-born#formtextarea)

Cette molécule utilise l'atome `TextArea` et inclut l'atome `Text` comme étiquette. La propriété label de cet élément est obligatoire.

```js
<FormTextArea label="Description" />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*FvN6n9CSgREAlyA8dB3BrQ.png)
_FormTextArea (Android)_

[**Carte**](https://github.com/99xt/first-born#card)

La molécule `Card` affiche une `View` avec une image, un titre et une description. Parmi les trois, le titre est obligatoire. Le style de cette molécule diffère selon la plateforme sous-jacente.

```js
<Card title="Titre seul" />
<Card title="Titre" description="Et description" />
<Card title="Titre" description="Description" image={require("./path/to/an/image.png")} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*6-5QCn6M6Z7Hu8YU_iSCKg.png)
_Carte (Android)_

[**Éléments de liste**](https://github.com/99xt/first-born#list-item)

La molécule `ListItem` affiche une `View` avec une image, un titre et une description. Parmi les trois, le titre est obligatoire. Le style de cette molécule diffère selon la plateforme sous-jacente.

```js
<ListItem title="Titre seul" />
<ListItem title="Titre" description="Et description" />
<ListItem title="Titre" description="Description" image={require("./path/to/an/image.png")} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*JbtPBYHdRFd1JrwIBJZTWg.png)
_Éléments de liste (Android)_

[**Notification**](https://github.com/99xt/first-born#notifications)

La molécule `Notification` affiche une bannière en haut de la page. La référence au composant est passée au `NotificationManager`. En invoquant la méthode `showAlert` de ce gestionnaire, nous pouvons envoyer le message à afficher à l'utilisateur.

Ajoutez la `Notification` comme tout dernier élément du parent `View`.

```js
<Notification ref={"alert"} />
```

Nous devons enregistrer cette molécule `Notification` lorsque la page est montée. Cela permet de passer la référence de la `Notification` au gestionnaire.

```js
componentDidMount() {
	NotificationBarManager.registerMessageBar(this.refs.alert);
}
```

Pour nettoyer, nous devons également désenregistrer cette molécule lorsque la page est démontée.

```js
componentWillUnmount() {  
	NotificationBarManager.unregisterMessageBar();
}
```

Pour afficher la barre de `Notification`, exécutez la méthode ci-dessous, en passant le message à afficher.

```js
NotificationBarManager.showAlert({  
	message: 'Votre message d'alerte ici'
});
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*LoyUDfsV7iH8cfNCPBuH7A.gif)
_Notification (Android)_

[**Bouton flottant**](https://github.com/99xt/first-born#floating-action-button)

Cette molécule est équivalente au bouton d'action flottant Android (FAB). Il peut s'agir soit d'une action unique, soit s'étendre pour afficher plusieurs actions.

Si le FAB contient une action unique, nous utilisons la propriété `onPress` pour passer la méthode à exécuter lorsque le bouton est cliqué.

```js
<FloatingButton onPress={this.handleShowNotification} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*luY2QUOdxc21FwdidH9brQ.gif)
_FAB avec une action unique_

Si le FAB doit s'étendre pour afficher plusieurs actions, un tableau d'actions doit être créé. Chaque objet d'action dans le tableau doit contenir au minimum :

1. Un `name` unique
2. Une `icône` ou une `image`
3. Une `position` à partir du haut (commence à 1) lorsque le FAB est étendu
4. Une méthode à exécuter `onPress`

```js
const actions = [
	{
		icon: 'help',
		name: 'bt_accessibility',
		position: 2,
		onPress: () => Alert.alert('Bonjour', 'Accessibilité')
	},
	{
		icon: 'pin',
		name: 'bt_room',
		position: 1,
		onPress: () => Alert.alert('Bonjour', 'Localisation')
	},
	{
		icon: 'videocam',
		name: 'bt_videocam',
		position: 3,
		onPress: () => Alert.alert('Bonjour', 'Vidéo')
	}
];
```

Nous passons ensuite le tableau au `FloatingButton` dans la propriété `actions` :

```js
<FloatingButton actions={this.actions} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*Y-AzQvQtemDwzT43aGpw8Q.gif)
_FAB avec plusieurs actions_

#### Organismes

**Formulaire**

L'organisme `Form` est construit à partir des molécules de formulaire, `FormInput`, `FormPicker`, `FormDatePicker` et `FormTextArea`.

Pour rendre cet organisme, un tableau contenant les détails de chaque champ doit être passé. Les composants enfants sont rendus selon le `type` spécifié dans chaque objet.

La correspondance est la suivante :

1. 'text' — `FormInput`
2. 'textarea' — `FormTextArea`
3. 'date' — `FormDatePicker`
4. 'picker' — `FormPicker`

L'objet de chaque champ ne peut contenir que les propriétés spécifiées pour le type de champ mappé. En termes plus simples, un objet de `type` 'text' ne doit contenir que les propriétés que la molécule `FormInput` accepte.

![Image](https://cdn-media-1.freecodecamp.org/images/1*sY8fbh-jSnI-oar9c1nhKg.png)
_Formulaire (Android)_

[**Liste de cartes**](https://github.com/99xt/first-born#cardlist)

Cet organisme rend actuellement une liste en lecture seule de `Cartes`, soit horizontalement, soit verticalement. Il nécessite un tableau d'objets qui ont les mêmes propriétés qu'une molécule `Carte`.

```js
const listData = [
	{
		title: "Titre 1",
		description: "Description 1",
		image: require("./path/to/an/image.png")
	},
    {
		title: "Titre 2",
		description: "Description 2",
		image: require("./path/to/an/image.png")
	},
    {
		title: "Titre 3",
		description: "Description 3",
		image: require("./path/to/an/image.png")
	}
];
```

Pour rendre la liste, passez le tableau ci-dessus à la propriété data. Ajoutez la propriété booléenne `horizontal`, si nous souhaitons une liste à défilement horizontal.

```js
<CardList data={this.listData} />
<CardList data={this.listData} horizontal />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*rWLDdoHlAizf8n8zIOxJKg.gif)
_Liste de cartes (Android)_

[**Vue de liste**](https://github.com/99xt/first-born#listview)

Cet organisme rend actuellement une liste en lecture seule de `ListItem` verticalement. Il nécessite un tableau d'objets qui ont les mêmes propriétés qu'une molécule `ListItem`. La même liste utilisée pour une `CardList` peut également être utilisée ici.

```js
<ListView data={this.listData} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*U8raFMaggqk5jdbLyCdr-g.gif)
_Vue de liste (Android)_

[**Navigation d'en-tête (NavBar)**](https://github.com/99xt/first-born#navbar)

L'organisme `NavBar` est un en-tête de page qui se rend selon la plateforme sous-jacente. Il est rendu en haut de la page, juste à l'intérieur du composant `View` principal de la page.

Pour former la `NavBar`, les trois éléments enfants (`NavBarRight`, `NavBarLeft` et `NavBarBody`) doivent être inclus pour aligner correctement les éléments.

```js
<NavBar>  
	<NavBarLeft />
		<NavBarBody>
			<Text>Titre</Text>
		</NavBarBody>
	<NavBarRight/>
</NavBar>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*ehUzDGAIWWg3VSVnusCy1A.png)
_NavBar avec titre uniquement (Android)_

Nous pouvons également inclure des boutons dans l'en-tête avec le composant `NavBarButton`. Ce bouton peut être ajouté en tant qu'enfants aux composants `NavBarRight` et `NavBarLeft`.

Le `NavBarButton` peut être utilisé de deux manières :

1. Il a une propriété `type`, qui accepte les valeurs 'back', 'drawer' et 'search'. Cela rend les icônes correspondantes à chaque type par défaut.
2. Nous pouvons créer un bouton personnalisé en incluant soit des `Textes`, des `Icônes` ou des `Images` en tant qu'enfants dans le composant `NavBarButton`.

```js
<NavBar>
	<NavBarLeft >
		<NavBarButton type="drawer" />
	</NavBarLeft>
	<NavBarBody>
		<Text>Titre</Text>
	</NavBarBody>
	<NavBarRight>
		<NavBarButton>
			<Icon name="heart" />
		</NavBarButton>
	</NavBarRight>
</NavBar>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*gVBpFDczPEM84dY7LIvXzA.png)
_NavBar avec boutons (Android)_

[**Navigation de pied de page (TabBar)**](https://github.com/99xt/first-born#tabbar)

L'organisme `TabBar` est un pied de page qui se rend selon la plateforme sous-jacente. Il est rendu tout en bas de la page, juste avant la balise de fermeture du composant `View` principal de la page.

La TabBar contient plusieurs TabItems, selon le nombre de pages dans la navigation par onglets. Un TabItem accepte soit des `Textes`, des `Icônes` ou des `Images` en tant qu'enfants.

```js
<TabBar>
	<TabItem active>
		<Icon name="heart" />
		<Text>Favoris</Text>
	</TabItem>
	<TabItem>
		<Icon name="add" />
		<Text>Ajouter</Text>
	</TabItem>
	<TabItem>
		<Icon name="camera" />
		<Text>Caméra</Text>
	</TabItem>
	<TabItem>
		<Icon name="settings" />
		<Text>Paramètres</Text>
	</TabItem>
</TabBar>
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*5cXDFOxPpwZv9Q7_gGVmKA.png)
_TabBar avec texte uniquement (Android)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*ZvZcBROU_hdmQebebyhnXg.png)
_TabBar avec icônes uniquement (Android)_

![Image](https://cdn-media-1.freecodecamp.org/images/1*tLBwVpzKOTrjoNeuPMrJRA.png)
_TabBar avec icônes et texte (Android)_

[**Navigation par pilules (PillView)**](https://github.com/99xt/first-born#pillbar)

La navigation `PillView` est utilisée pour afficher différentes sections sur une page. Sur Android, elle se rend sous forme de barre d'onglets d'en-tête. Sur iOS, elle se rend sous forme de pilules.

Elle nécessite deux tableaux pour être rendue avec succès. L'un est une liste des scènes qu'elle affichera. Le second est les composants à afficher dans l'en-tête (`PillBar`).

La scène de la pilule ne nécessite qu'une seule clé dans l'objet. Elle est utilisée pour désigner la scène à afficher sur la vue lorsque le `PillItem` correspondant est cliqué.

L'en-tête de la pilule nécessitera au moins l'un des éléments suivants : Texte, Icône ou Image à rendre sur le `PillItem`.

```js
const pillScenes = [
	{ scene: <CardList data={this.listData} /> },
	{ scene: <ListView data={this.listData} /> },
	{ scene: 
		<View style={styles.innerContainer}>
			<Form formElements={this.formElements} />
		</View> 
	}
];
```

```js
const pillHeaders = [
	{
		title: 'Liste de cartes',
		icon: "card"
	},
	{
		title: 'Vue de liste',
		icon: "list"
	},
	{
		title: 'Formulaire',
		icon: "help"
	}
];
```

Nous allons ensuite passer les deux tableaux à l'élément `PillView` comme ceci :

```js
<PillView pillHeaders={this.pillHeaders} pillScenes={this.pillScenes} />
```

![Image](https://cdn-media-1.freecodecamp.org/images/1*R6vKLzsIROI1VyPFuzoC8g.gif)
_PillView (Android)_

Et voici tous les composants que `first-born` a à offrir (pour l'instant...).

Une fois le code un peu mieux assemblé, nous aboutirons à une application similaire à ceci :

![Image](https://cdn-media-1.freecodecamp.org/images/1*vq0yVJovf5m2YC3aKqpM2A.gif)
_Mise en œuvre finale de toutes les fonctionnalités_

Essayez `first-born` et faites-moi savoir comment cela se passe pour vous.

Trouvez le dépôt de démonstration [ici](https://github.com/samsam-026/firstBornExample).

Si vous souhaitez voir comment les éléments de navigation first-born fonctionnent avec des modules de navigation externes, consultez les dépôts suivants ;

React Navigation : [first-born-react-navigation-example](https://github.com/samsam-026/first-born-react-navigation-example)

React Native Router Flux : [first-born-rnrf-example](https://github.com/samsam-026/first-born-rnrf-example)