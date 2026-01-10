---
title: Comment concevoir une bulle de chat similaire à iMessage dans React Native
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2021-03-24T18:50:46.000Z'
originalURL: https://freecodecamp.org/news/design-imessage-like-chat-bubble-react-native
coverImage: https://www.freecodecamp.org/news/content/images/2021/03/feature_image_freecodecamp-3.jpg
tags:
- name: app development
  slug: app-development
- name: Chat
  slug: chat
- name: JavaScript
  slug: javascript
- name: React Native
  slug: react-native
- name: UI Design
  slug: ui-design
seo_title: Comment concevoir une bulle de chat similaire à iMessage dans React Native
seo_desc: "By Prajwal Kulkarni\nWhether you're an Apple fan or not, you'll likely\
  \ agree that Apple sure does have a groundbreaking UI. And iMessage is definitely\
  \ an important part of that design. \nThe curved arrow is something that I have\
  \ always really liked and..."
---

Par Prajwal Kulkarni

Que vous soyez un fan d'Apple ou non, vous serez probablement d'accord pour dire qu'Apple a une interface utilisateur révolutionnaire. Et iMessage en est définitivement une partie importante.

La flèche courbée est quelque chose que j'ai toujours vraiment aimé et que j'ai voulu reproduire depuis longtemps.

Après beaucoup d'essais et d'erreurs, j'ai enfin trouvé une solution pour créer une version similaire de la bulle de chat d'iMessage. Dans cet article, je vais vous guider à travers les étapes nécessaires pour créer une bulle de chat qui ressemble à celle d'iMessage d'Apple.

Si vous construisez une application de chat ou si vous prévoyez d'afficher des informations sous forme de message, je vous recommande définitivement d'essayer ce style, car il donne à votre application un look cool et professionnel.

### Prérequis

Cet article suppose que vous connaissez les bases de :

* JSX
* React Native
* HTML & CSS

## Qu'est-ce qu'une bulle de chat ?

Une bulle de chat est essentiellement un conteneur qui contient du texte. Les bulles de chat sont principalement utilisées dans les applications de messagerie instantanée pour afficher efficacement les journaux de chat.

La méthode conventionnelle consiste à afficher les messages envoyés du côté droit de l'écran et les messages reçus du côté gauche, avec des couleurs différentes pour différencier les messages envoyés et reçus.

La plupart des applications de messagerie ont une bulle de chat basique qui est un conteneur régulier avec des coins arrondis. Le principal facteur de différenciation entre les autres applications et iMessage est la présence d'une petite flèche courbée ancrant le conteneur de texte, qui ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/freecodecamp-1.jpg)

## Comment créer une bulle de chat qui ressemble à iMessage

Si nous regardons attentivement l'image ci-dessus, nous pouvons voir que la bulle de chat iMessage est une combinaison d'une bulle de chat régulière avec une flèche ajoutée dans le coin.

Le principal défi réside dans le fait de lier la flèche au conteneur de texte.

Avant de plonger directement dans le code, je voudrais que vous sachiez comment cet élément en forme de flèche est créé et ajouté.

Tout d'abord, consultez [ce](https://codepen.io/samuelkraft/pen/Farhl) code, qui montre comment implémenter cette flèche en utilisant HTML & CSS. Voici son extrait de code.

```css
p {
  max-width: 255px;
  word-wrap: break-word;
  margin-bottom: 12px;
  line-height: 24px;
  position: relative;
	padding: 10px 20px;
  border-radius: 25px;
  
  &:before, &:after {
    content: "";
		position: absolute;
    bottom: 0;
    height: 25px;
  }
}

.from-me {
	color: white; 
	background: #0B93F6;
	align-self: flex-end;
		
	&:before {
		right: -7px;
    width: 20px;
    background-color: #0B93F6;
		border-bottom-left-radius: 16px 14px;
	}

	&:after {
		right: -26px;
    width: 26px;
    background-color: white;
		border-bottom-left-radius: 10px;
	}
}
.from-them {
	background: #E5E5EA;
	color: black;
  align-self: flex-start;
		
	&:before {
		left: -7px;
    width: 20px;
    background-color: #E5E5EA;
		border-bottom-right-radius: 16px;
	}

	&:after {
		left: -26px;
    width: 26px;
    background-color: white;
		border-bottom-right-radius: 10px;
	}
}
```

Si vous parcourez directement le code, cela peut sembler assez horrible. Alors décomposons-le à un niveau atomique et recollons-le ensuite.

La balise `<p>` inclut des contraintes de style telles que margin-bottom, position, padding, etc. Notez que la largeur maximale utilisée ici est de 255px, ce qui est une valeur statique. Mais nous utiliserons une approche dynamique, car les bulles de chat doivent être réactives sur différentes tailles d'écran.

Les `&:before` et `&:after` dans le style `<p>` définissent deux éléments sans contenu. Ils sont positionnés de manière absolue par rapport à la balise `<p>` (conteneur de texte), et sont placés en bas. Ils ont une hauteur de 25px (la hauteur de la flèche).

En allant plus loin, le style `.from-me` (messages envoyés) définit que le texte soit blanc, le fond bleu (#0b936f), et qu'il soit placé du côté droit de l'écran (align-self: flex-end).

Voici la partie importante – l'extension des `&:before` et `&:after`, qui est l'implémentation réelle de la flèche.

Le `&:before` a une largeur de 20px et est placé à 7 pixels négatifs à droite. Il a un border-bottom-left radius de 16px, ce qui donne l'apparence courbée à la flèche.

De même, le `&:after` a une largeur de 26px et est placé à 26 pixels négatifs à droite. Puisque -7px > -26px, `&:after` est placé du côté droit de l'élément `&:before` et le chevauche partiellement.

Si vous êtes encore confus, ne vous inquiétez pas – référez-vous simplement aux images ci-dessous pour avoir une vision plus claire de ce dont je parle.

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc1.PNG)
_&:before avec fond noir et border-bottom-left-radius_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc2.PNG)
_&:after chevauchant &:before avec fond vert_

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc3.PNG)
_&:after avec fond changé en blanc pour correspondre au fond de l'écran de chat._

![Image](https://www.freecodecamp.org/news/content/images/2021/03/fcc4.PNG)
_&:before avec fond mis à jour à #0b93f6 pour correspondre à la couleur de la bulle de chat._

Donc, essentiellement, la pointe de la flèche est créée en chevauchant deux éléments dans le coin inférieur de la bulle de chat et en ajustant les couleurs de fond pour correspondre à celles de la bulle de chat et de l'écran de chat.

Plus loin, la traduction de CSS et HTML en JSX est assez simple, car la plupart des choses sont assez directes.

## Comment construire la version React Native

Avant de commencer, je veux noter que cela fonctionne mieux avec FlatList, et je vous recommande de l'utiliser, et non d'autres composants ou fonctions comme map (qui manquait de cohérence sur différents écrans et appareils).

Les trois étapes que nous allons suivre ici sont :

1. Créer une bulle de chat avec une tête de flèche
2. Ajouter des styles à la bulle de chat et à la tête de flèche
3. Intégrer la bulle de chat dans FlatList

Alors, commençons.

Tout d'abord, nous allons créer la bulle de chat avec la tête de flèche, comme ceci :

```
<View style={{
                    backgroundColor: "#0078fe",
                    padding:10,
                    marginLeft: '45%',
                    borderRadius: 5,
                    //marginBottom: 15,
                    marginTop: 5,
                    marginRight: "5%",
                    maxWidth: '50%',
                    alignSelf: 'flex-end',
                    //maxWidth: 500,
                    
                    borderRadius: 20,
                  }} key={index}>
  
                    
                    <Text style={{ fontSize: 16, color: "#fff", }} key={index}>{item.text}</Text>
  
                      <View style={styles.rightArrow}></View>
                      
                      <View style={styles.rightArrowOverlap}></View>
                    
                    
                    
</View>


//Message reçu
      <View style={{
                    backgroundColor: "#dedede",
                    padding:10,
                    borderRadius: 5,
                    marginTop: 5,
                    marginLeft: "5%",
                    maxWidth: '50%',
                    alignSelf: 'flex-start',
                    //maxWidth: 500,
                    //padding: 14,
                    
                    //alignItems:"center",
                    borderRadius: 20,
                  }} key={index}>
  
                    
                      
                      <Text style={{ fontSize: 16, color: "#000",justifyContent:"center" }} key={index}> {item.text}</Text>
                      <View style={styles.leftArrow}>
  
                      </View>
                      <View style={styles.leftArrowOverlap}></View>
                    
                    
                    
                    </View>
             
```

La balise **`<View>`** la plus externe agit comme la balise 'p' en comparaison avec la version HTML. Les deux balises **`<View>`** restantes agissent comme `:before` et `:after`.

Ensuite, nous allons ajouter des styles à la bulle de chat et à la tête de flèche comme ceci :

```
const styles = StyleSheet.create({
rightArrow: {
  position: "absolute",
  backgroundColor: "#0078fe",
  //backgroundColor:"red",
  width: 20,
  height: 25,
  bottom: 0,
  borderBottomLeftRadius: 25,
  right: -10
},

rightArrowOverlap: {
  position: "absolute",
  backgroundColor: "#eeeeee",
  //backgroundColor:"green",
  width: 20,
  height: 35,
  bottom: -6,
  borderBottomLeftRadius: 18,
  right: -20

},

/*Tête de flèche pour les messages reçus*/
leftArrow: {
    position: "absolute",
    backgroundColor: "#dedede",
    //backgroundColor:"red",
    width: 20,
    height: 25,
    bottom: 0,
    borderBottomRightRadius: 25,
    left: -10
},

leftArrowOverlap: {
    position: "absolute",
    backgroundColor: "#eeeeee",
    //backgroundColor:"green",
    width: 20,
    height: 35,
    bottom: -6,
    borderBottomRightRadius: 18,
    left: -20

},
})
```

Ensuite, nous allons l'intégrer dans FlatList :

```
<FlatList
        //inverted
        style={{backgroundColor:"#eeeeee"}}
        data={this.state.chat_log}
        ref={ref => (this.FlatListRef = ref)} // assign the flatlist's ref to your component's FlatListRef...
      
        
        renderItem = {({item,index})=>{

          rowId={index}
         
            if (SENT_MESSAGE) { //change as per your code logic

          
              
                return (
    
                  <View style={{
                    backgroundColor: "#0078fe",
                    padding:10,
                    marginLeft: '45%',
                    borderRadius: 5,
                   
                    marginTop: 5,
                    marginRight: "5%",
                    maxWidth: '50%',
                    alignSelf: 'flex-end',
                    borderRadius: 20,
                  }} key={index}>
  
                    
                    <Text style={{ fontSize: 16, color: "#fff", }} key={index}> {item.text}</Text>
  
                      <View style={styles.rightArrow}>
  
                      </View>
                      <View style={styles.rightArrowOverlap}></View>
                    
                    
                    
                  </View>
                )

              
              
              
            } else {

              
                return (
                  <View style={{
                    backgroundColor: "#dedede",
                    padding:10,
                    borderRadius: 5,
                    marginTop: 5,
                    marginLeft: "5%",
                    maxWidth: '50%',
                    alignSelf: 'flex-start',
                    //maxWidth: 500,
                    //padding: 14,
                    
                    //alignItems:"center",
                    borderRadius: 20,
                  }} key={index}>
  
                    
                      
                      <Text style={{ fontSize: 16, color: "#000",justifyContent:"center" }} key={index}> {item.text}</Text>
                      <View style={styles.leftArrow}>
  
                      </View>
                      <View style={styles.leftArrowOverlap}></View>
                    
                    
                    
                  </View>
                )
              
              
            }
            
          

        }
        
        keyExtractor={(item,index)=>index.toString()}
        />

```

Les valeurs telles que **borderRadius, padding, margin,** et **backgroundColor** sont des valeurs arbitraires et peuvent être modifiées si vous le souhaitez. Alors n'hésitez pas à jouer avec et à faire ces changements pour mieux répondre à vos besoins.

Le résultat du code ci-dessus ressemble à ceci :

![Image](https://www.freecodecamp.org/news/content/images/2021/03/IMG_20210324_160111.jpg)
_Apparence de la bulle de chat, telle que testée sur plusieurs appareils (Android)._

Cela a l'air cool, n'est-ce pas ? ;)

## Conclusion

Félicitations ! Vous avez construit une bulle de chat qui ressemble exactement à celle utilisée par iMessage.

J'espère que vous avez trouvé cet article utile. Si c'est le cas, partagez-le avec vos amis et collègues.

Vous avez encore des questions ? N'hésitez pas à me contacter, et je vous répondrai dès que possible.

Vous pouvez également me rejoindre sur [LinkedIn](https://in.linkedin.com/in/prajwal-kulkarni) / [Instagram](https://instagram.com/prajwalkulkarni_).