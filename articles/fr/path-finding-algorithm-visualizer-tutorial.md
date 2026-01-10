---
title: Comment créer un visualiseur d'algorithme de recherche de chemin avec React
subtitle: ''
author: Houssein Badra
co_authors: []
series: null
date: '2022-11-17T21:07:02.000Z'
originalURL: https://freecodecamp.org/news/path-finding-algorithm-visualizer-tutorial
coverImage: https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--67--1.png
tags:
- name: algorithms
  slug: algorithms
- name: React
  slug: react
seo_title: Comment créer un visualiseur d'algorithme de recherche de chemin avec React
seo_desc: 'Path-finding algorithms are algorithms used to find optimal path between
  two locations. These algorithms are widely used in map applications like Google
  Maps, for example.

  In this tutorial we will be building a path finding algorithm visualizer with ...'
---

Les algorithmes de recherche de chemin sont des algorithmes utilisés pour trouver le chemin optimal entre deux emplacements. Ces algorithmes sont largement utilisés dans les applications de cartographie comme Google Maps, par exemple.

Dans ce tutoriel, nous allons créer un visualiseur d'algorithme de recherche de chemin avec React. Il prendra en charge la recherche en largeur d'abord (BFS), la recherche en profondeur d'abord (DFS), l'ajout de murs et la pondération des nœuds pour les algorithmes de graphes pondérés comme Dijkstra. Cela nous aidera à identifier des caractéristiques comme les rues à fort trafic que vous ne voulez pas emprunter.

Pour suivre ce tutoriel, vous devriez avoir une compréhension de base de [BFS](https://www.freecodecamp.org/news/breadth-first-search-a-bfs-graph-traversal-guide-with-3-leetcodeexamples/) et [DFS](https://www.freecodecamp.org/news/dfs-for-your-next-tech-giant-interview/). Au cas où vous auriez besoin de réviser, je laisserai un lien vers une vidéo YouTube expliquant les deux algorithmes.

Vous devriez également avoir une compréhension de base de React.

Voici la [version finale de ce que nous allons construire](https://houssein-algo-visualizer.netlify.app/) et voici [le code source](https://github.com/HousseinBadra/Algo-visualizer.git) sur mon compte GitHub.

Dans ce tutoriel, nous utiliserons Visual Studio Code (mais vous pouvez utiliser n'importe quel éditeur), une invite de commande, un peu de React, ES6 JavaScript, et HTML et CSS.

Alors commençons à coder !

## Installation du projet

Pour ce tutoriel, j'utiliserai Vite, qui est un outil qui vous aide à démarrer des projets bien plus rapidement que npm create-react-app.

Tout d'abord, installez Vite si ce n'est pas déjà fait. Créez un dossier dans un répertoire connu sur votre machine. Ensuite, en utilisant le terminal, naviguez jusqu'à ce répertoire et exécutez ces commandes :

```
$ npm create vite@latest my-app
$ cd my-app
$ npm install
```

Maintenant, à l'intérieur du dossier src, créez un dossier components, un dossier contexts et un dossier utils – et vous avez terminé. Voici une capture d'écran de ce à quoi votre projet devrait ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--68-.png)
_Structure du dossier du projet_

## Comment ajouter Bootstrap

Maintenant, nous devons ajouter Bootstrap à notre projet pour les boutons et les icônes que nous allons ajouter, puisque nous devons nous concentrer sur la partie JavaScript.

Pour ce faire, ajoutez simplement le CDN Bootstrap à la balise head dans votre fichier HTML. Après avoir ajouté ces liens, vous devriez remarquer le changement de police.

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.9.1/font/bootstrap-icons.css">
```

## Comment représenter les cellules

Pour la représentation de la grille et des cellules, je vais construire un tableau à deux dimensions d'objets contenant toutes les propriétés dont nous avons besoin pour représenter une certaine cellule.

Maintenant, dans le dossier utils, créez un fichier startingGrid.js. Ici, vous écrivrez une fonction qui retourne une grille qui est un tableau à deux dimensions d'objets représentant les cellules.

Chaque objet aura ces propriétés : **x**, **y**, **isstarting**, **istarget**, **iswall**, et **weight**.

**x** et **y** représentent les coordonnées de la cellule. **isstarting** est un booléen qui n'est vrai que pour la cellule de départ. **istarget** est similaire, mais pour le nœud cible. **iswall** est un booléen qui n'est vrai que pour les murs. Et **weight** est un entier.

Toutes les cellules normales ont un poids de 1, et les cellules pondérées ont un poids de 5. La fonction devrait ressembler à ceci :

```js
export function getGrid(width,height){
    let grid=[]
    for (let i =0 ; i<height ; i++){
      let local=[]
      for (let j =0 ; j<width ; j++){
          local.push({x:j,y:i,isstart:false,istarget:false,weight:1,
          iswall:false})
          }
      grid.push(local)
      }
    grid[Math.floor(height/2)][Math.floor(width/2)].isstart=true
    grid[height-2][width-2].istarget=true
    return  grid
    }
```

## Comment créer le contexte

Dans React, passer des props de parent à enfant peut devenir ingérable. Pour cette raison, il est préférable de stocker tout notre état dans un seul endroit où l'état sera accessible à tous les éléments. C'est ce qu'est un contexte.

Dans React, nous pouvons créer un contexte avec `createContext` et accéder à toutes ses variables en utilisant le hook `useContext`.

Maintenant, créons un contexte avec tout ce dont nous avons besoin. Lorsque nous survolons une cellule, nous contrôlerons le comportement de l'écouteur d'événements en fonction d'une variable appelée mode. Par exemple, si le mode est `addwalls`, alors survoler une cellule en fait un mur.

Nous utiliserons la même logique pour ajouter des cellules pondérées, et aussi pour définir les cellules de départ et de fin.

La structure que je vais utiliser pour créer le contexte est très simple. Vous pouvez l'utiliser dans tous vos projets, et elle ressemblera à ceci :

```js
import { useContext,createContext } from "react";

const context = createContext()

export const useParams=()=>{
    return useContext(context)
}

export const ParamsProvider = ({children}) => {

      return (<div>
       <context.Provider value={}>
        {children}
       </context.Provider>
      </div>)

}
```

Maintenant, nous allons créer un état pour :

* Le **mode** dans lequel nous nous trouvons, soit en construction de murs, soit en définition de la cellule de départ.
* L'**algorithme** que nous allons exécuter.
* La **grille** que nous égaliserons par défaut à la grille retournée par la fonction que nous avons déjà créée.
* Déterminer si nous sommes en **édition** ou non.
* Pour les coordonnées des nœuds **départ** et **cible**.
* Déterminer que nous voulons **exécuter l'algorithme** et **effacer la grille** lorsqu'ils sont modifiés en utilisant `useEffect` (Un état séparé pour chacun, lorsque nous changeons sa valeur, nous exécutons un useEffect avec un effet secondaire approprié).

Le code ressemblera à ceci :

```js
import { useContext, useState,createContext, useEffect, useRef } from "react";
import { getGrid } from "../utils/startinggrid";

const context = createContext()

export const useParams=()=>{
    return useContext(context)
}

export const ParamsProvider = ({children}) => {

     const [mode,setmode] = useState(null)
     const [algo,setalgo] = useState('')
     const [run,setrun] = useState(false)
     const [grid,setgrid] = useState(getGrid(50,25))
     const [editing,seteditFlag] = useState(false)
     const [res,setres] = useState(false)
     const start=useRef({x:25,y:12})
     const end=useRef({x:48,y:23})
    
     useEffect(()=>{    
      restart()
     },[res])


     function restart(){
      setgrid(getGrid(50,25))
     }


      return (<div>
      <context.Provider value={{mode,
        setmode,
        algo,
        setalgo,
        grid,
        setgrid,
        setres,
        editing,
        seteditFlag,
        start,
        end,
        run,
        setrun,
        res}}>
         {children}
       </context.Provider>
       </div>)

     }

```

Et enfin, nous envelopperons le composant d'application avec le ParamsProvider comme ceci :

```js
import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App'
import './index.css'
import {ParamsProvider} from './context/context'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
      <ParamsProvider>
      <App />
      </ParamsProvider>
  </React.StrictMode>

)
```

Maintenant, pour vous assurer que tout fonctionne, importez le hook personnalisé useParams dans vos composants. Utilisez la console pour vérifier sa valeur de retour. Il devrait retourner un objet avec toutes les variables que nous avons ajoutées au store.

```js
import './App.css'
import {useParams} from './context/context'


function App() {

console.log(useParams())

return ( <div></div>)

}

export default App
```

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--75-.png)

## Comment créer la barre de navigation

Maintenant, il est temps de créer la barre de navigation que nous utiliserons pour contrôler les modes. Tout d'abord, créez un dossier Navbar avec deux fichiers : Navbar.jsx et Navbar.css. Cette structure est très utile, surtout lorsque vous utilisez Sass (donc chaque composant et son CSS peuvent être trouvés dans le même dossier).

La barre de navigation sera composée de six boutons : deux pour définir le mode d'édition du nœud de départ/de fin, deux pour définir le mode de construction de blocs/ajout de cellules pondérées, et deux pour effacer le tableau et exécuter l'algorithme.

Le code ressemblera à ceci :

```js
import React, { useState } from 'react'
import './Navbar.css'
import { useParams } from '../../context/context'


export default function Navbar() {

  // const [algo,setalgo] = useState('')
  const {mode,setmode,algo,setalgo,setres,setrun}=useParams()

  

  return (
    <div className='navbar'>
      <div className='container'>
       <button type="button" className={['btn' ,'btn-primary', mode=='setstart'? 'selected' : ''].join(' ')} onClick={()=>{
        if(mode == 'setstart') setmode(null)
        else {setmode('setstart')}
       }}>
        <i className="bi bi-geo-alt"></i>
       </button>
       <button type="button" className={['btn' ,'btn-primary', mode=='settarget'? 'selected' : ''].join(' ')} onClick={()=>{
        if(mode == 'settarget') setmode(null)
        else {setmode('settarget')}
       }}>
       <i className="bi bi-geo"></i>
       </button>
       <button type="button" className={['btn' ,'btn-primary', mode=='addbricks'? 'selected' : ''].join(' ')} onClick={()=>{
        if(mode == 'addbricks') setmode(null)
        else {setmode('addbricks')}
       }}>
       <i className="bi bi-bricks"></i>
       </button>
       <button type="button" className={['btn' ,'btn-primary', mode=='addweight'? 'selected' : ''].join(' ')} onClick={()=>{
        if(mode == 'addweight') setmode(null)
        else {setmode('addweight')}
       }}>
       <i className="bi bi-virus"></i>
       </button>
       <button type="button" className="btn btn-primary" onClick={()=>{setres((old)=>{ return !old})}}>
       <i className="bi bi-arrow-counterclockwise"></i> 
       </button>
       <button type="button" className="btn btn-primary" onClick={()=>{setrun((old)=>{return !old})}}>
       <i className="bi bi-caret-right"></i> 
       </button>
       <div>
       <select className="form-select" aria-label="Default select example"  value={algo} onChange={(e)=>{
        setalgo(e.target.value)
       }}>
       <option value=''>Choisissez votre algorithme</option>
       <option value="dijkstra">dijkstra</option>
       <option value="BDS">BDS</option>
       <option value="BFS">BFS</option>
</select>
       </div>
      </div>
    </div>
  )
}
```

Chaque bouton définit le mode sur la valeur souhaitée – ou sur null s'il est déjà défini sur le mode du bouton.

Les boutons d'exécution et de redémarrage changent les valeurs des variables de contexte d'état `res` et `run`. Nous utiliserons ceux-ci avec un hook useEffect pour exécuter l'algorithme ou effacer le tableau. L'élément d'entrée `select` est pour sélectionner l'algorithme.

Maintenant, par exemple, si le bouton de mode de construction de blocs est sélectionné, nous voulons que ce bouton ait un style différent des autres boutons. Nous ferons cela en utilisant la classe selected qui sera ajoutée pour le bouton en fonction du mode sélectionné. Le CSS ressemblera à ceci :

```css
.navbar{
    width:100%;  
    height:min(20vh , 100px);
    background:black;
}

.navbar .selected {
    box-shadow: rgb(204, 219, 232) 3px 3px 6px 0px inset, rgba(255, 255, 255,     0.5) -3px -3px 6px 1px inset;
}
```

Voici à quoi l'application va ressembler pour le moment. Pour la tester, vous pouvez vérifier les changements de variables de contexte lors des clics sur les boutons :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--76-.png)
_État actuel de l'application_

## Comment créer la grille

Maintenant, les cellules sont des divs contenues dans une div avec la classe board qui contiendra toutes les cellules. La grille ressemblera à une feuille Excel où chaque cellule a une coordonnée x et y.

Tout d'abord, créez un dossier Grid dans le dossier components. Ensuite, ajoutez deux fichiers : Grid.jsx et Grid.css.

Maintenant, créons la grille. Tout d'abord, nous allons créer une fonction qui prend la grille et retourne un tableau de refs pour chaque cellule.

Lorsque nous exécutons les algorithmes, il y aura beaucoup de changements d'état si nous utilisons un état régulier et l'application plantera. Donc la solution est de créer une ref pour chaque cellule, et lorsque nous rendons les cellules, chacune aura sa ref correspondante. Cela nous permet de manipuler la div sans re-rendre le composant.

Cette approche a un coût, cependant, qui est un comportement inattendu – car ce n'est pas la façon dont React est censé fonctionner. Mais si nous n'utilisons pas cette approche, l'application plantera à cause des re-rendus.

Nous allons créer un état pour sauvegarder le tableau de refs. L'algorithme ressemblera à ceci :

```js
  const {grid,setgrid,editing,seteditFlag,mode,start,end,run,res,algo}  =       useParams()

  const [refarray,mm]=useState(getrefarray(grid))
  
  function getrefarray(grid){
    let array=[]
    grid.forEach((elem)=>{
     elem.forEach((child)=>{
      array.push(useRef())
    })
   })
   return array
   }
```

Tout d'abord, nous allons rendre une div avec la classe `board`. À l'intérieur du board et pour chaque élément de `refarray`, nous allons rendre une div avec une propriété ref (l'élément lui-même) afin que nous puissions y accéder et le modifier sans rendre à nouveau le composant.

Chaque div aura la classe cell et la classe wall si son objet de cellule correspondant dans la grille a la propriété `iswall` égale à true. Nous ajouterons également l'icône correspondante à la cellule en fonction de son objet de cellule.

```js
{refarray.map((elem,index)=> {
        let classList=['cell']

        let yindex=Math.floor(index/50)
        let xindex=index % 50
        let cell=grid[yindex][xindex]

        if (cell.iswall) {
          classList.push('wall')
        }
        
        return <div key={`${index}`} ref={elem}  className={classList.join('         ')} >
         

          {cell.weight > 1 ? <i className="bi bi-virus"></i> : null}
          {cell.isstart ? <i className="bi bi-geo-alt"></i> : null }
          {cell.istarget ? <i className="bi bi-geo"></i> : null }
          
        </div> 
})
```

Voici à quoi la grille va ressembler :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--77-.png)
_Application montrant la grille_

Maintenant, nous devons ajouter trois écouteurs d'événements à chaque cellule. Tout d'abord, nous ajouterons des écouteurs d'événements onMouseDown et onMouseUp – nous les utilisons pour définir la variable de contexte d'édition. Ensuite, nous ajouterons un onMouseOver qui déterminera – en fonction du mode et de ce drapeau d'édition – quelles modifications sont appliquées à la grille.

Nous mettrons à jour la grille comme d'habitude – nous n'utiliserons la méthode ref que lors de l'exécution de l'algorithme. Le code ressemblera à ceci :

```js
return (
    <div className='board'>
      {refarray.map((elem,index)=> {
        let classList=['cell']
        let yindex=Math.floor(index/50)
        let xindex=index % 50
        let cell=grid[yindex][xindex]

        if (cell.iswall) {
          classList.push('wall')
        }
        
        return <div key={`${index}`} ref={elem}  className={classList.join(' ')} 
        onMouseDown={()=>{seteditFlag(true)}} 
        onMouseUp={()=> {seteditFlag(false)}}
        onMouseMove={()=>{
          if (!editing) return
          const current= grid[yindex][xindex]
          if (current.isstart || current.istarget ) return
          switch(mode){
            case 'setstart':
              var newgrid=grid.map((elem)=>{
              return elem.map((elem)=>{
                if (!elem.isstart) return elem
                return {...elem,isstart:false}
              }) 
              })
              newgrid[yindex][xindex]={...newgrid[yindex][xindex],isstart:true,istarget:false,weight:1,iswall:false}
             start.current={x:xindex,y:yindex}
             setgrid(newgrid)
             break;

           case 'settarget':
                var newgrid=grid.map((elem)=>{
                return elem.map((elem)=>{
                  if (!elem.istarget) return elem
                  return {...elem,istarget:false}
                }) 
               })
               newgrid[yindex][xindex]={...newgrid[yindex][xindex],isstart:false,istarget:true,weight:1,iswall:false}
               end.current={x:xindex,y:yindex}
               setgrid(newgrid)
               break;

             case 'addbricks':
                var newgrid=grid.slice()
               newgrid[yindex][xindex]={...newgrid[yindex][xindex],weight:1,iswall:true}
               setgrid(newgrid)
               break;

            case 'addweight':
                var newgrid=grid.slice()
               newgrid[yindex][xindex]={...newgrid[yindex][xindex],weight:5,iswall:false}
               setgrid(newgrid)
               break;
           default:
             return 
            }}}>
         

          {cell.weight > 1 ? <i className="bi bi-virus"></i> : null}
          {cell.isstart ? <i className="bi bi-geo-alt"></i> : null }
          {cell.istarget ? <i className="bi bi-geo"></i> : null }
          
         </div>
      })}
    </div>
  )

```

Si le drapeau d'édition est faux, nous retournerons. Il en va de même si la cellule est une cellule de départ ou une cellule cible – alors nous ne voulons pas les modifier. Sinon, si le mode est égal à `addwalls`, alors nous modifierons la cellule correspondante dans la grille et définirons la propriété `iswall` à true.

De plus, si le mode est égal à `addweight`, nous modifierons la cellule correspondante dans la grille et définirons la propriété weight à 5 au lieu de 1.

Pour le `setstart`, nous créerons une copie de la grille où toutes les cellules ont `isstart` défini à false. Ensuite, nous définirons la cellule correspondante pour la nouvelle cellule de départ à true. Il en va de même pour le mode settarget.

Maintenant, vous devriez être en mesure d'ajouter des murs, des poids et de changer la position du nœud de départ et de fin :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--78-.png)

## Les algorithmes

Nous pouvons trouver le chemin le plus court en utilisant les algorithmes que nous allons implémenter. Chaque algorithme trouve un chemin de manière unique et, selon l'algorithme, la sortie changera.

Commençons par l'algorithme de recherche en largeur d'abord (ou BFS). Nous allons créer une fonction **BFS** qui prend 5 arguments :

* le **graph**
* les coordonnées du point de départ et de fin, **start** et **target**
* **prevmap**, qui est une table de hachage utilisée pour suivre la cellule précédente pour chaque cellule dans la grille lorsque l'algorithme s'exécute
* **hashmap**, qui est une table de hachage que nous utiliserons pour suivre les cellules visitées. Une table de hachage est un objet avec des paires clé-valeur, comme un dictionnaire en Python.

Pour chaque cellule dans le graphique, nous créerons un id x-y qui sera unique. Nous définirons sa valeur à false pour **hashmap** et null pour **prevmap**. Voici comment nous allons les implémenter dans un useEffect plus tard :

```js
  let hashmap={}
  let prevmap={}
  for (let j=0;j<25;j++){
   for (let i=0;i<50;i++){
     hashmap[`${i}-${j}`]=false
     prevmap[`${i}-${j}`]=null
   }
 }
```

Maintenant, nous commencerons avec un tableau avec un élément – les coordonnées du nœud de départ – et un compteur initialisé à zéro. Tant que la longueur du tableau n'est pas nulle, nous retirerons le dernier élément du tableau et incrémenterons le compteur.

Maintenant, en utilisant les coordonnées de l'élément, nous accéderons à sa ref et ajouterons la classe visited avec un délai de transition proportionnel au compteur.

Ensuite, nous accéderons aux siblings de l'élément à partir de la grille et vérifierons s'ils sont visités ou non à partir de **hashmap.** S'ils sont visités, nous les ignorerons, mais s'ils ne sont pas visités, nous les marquerons comme visités et les ajouterons au sommet du tableau. Ensuite, nous marquerons leur valeur dans **prevmap** à l'élément actuel.

Lors du retrait des éléments, si nous arrivons à un élément avec des coordonnées x et y égales à celles de la cible, nous retournerons cet objet avec le compteur actuel.

La recherche en profondeur d'abord est très similaire : avec de petits changements dans l'ordre, nous pouvons supprimer et ajouter des éléments au tableau. [Voici la vidéo YouTube d'Alvin qui explique le sujet de manière utile](https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&ved=2ahUKEwjp_Y66x5T7AhWIH-wKHWcBBpAQwqsBegQICRAB&url=https%3A%2F%2Fwww.youtube.com%2Fwatch%3Fv%3DtWVWeAqZ0WU&usg=AOvVaw1zYTobguFNgtE86akRVrNf).

Enfin, s'il n'y a pas de chemin de a à b – par exemple si a est entouré de murs – nous retournerons null. Cela ne se produira que lorsque le tableau deviendra vide avant de retourner une valeur. Le code ressemblera à ceci :

```js

  function BFS(graph,hashmap,prevmap,start,target){
    let queue=[start]
    let count=0
    hashmap[`${start.x}-${start.y}`]=true
    while (queue.length > 0){
      count+=1
      let c=queue.pop()
      refarray[c.x+c.y*50].current.style['transition-delay']=`${count * 8}ms`
      refarray[c.x+c.y*50].current.classList.add('visited')
      if (c.x == target.x && c.y == target.y) return [c,count]
 
      if(c.x+1 < 50 && !hashmap[`${c.x+1}-${c.y}`] && !graph[c.y][c.x+1].iswall){
        queue.unshift({x:c.x +1,y:c.y})
        prevmap[`${c.x+1}-${c.y}`]={...c}
        hashmap[`${c.x+1}-${c.y}`]=true
      }
      if(c.x-1 >=0 && !hashmap[`${c.x-1}-${c.y}`] && !graph[c.y][c.x-1].iswall){
        queue.unshift({x:c.x -1,y:c.y})
        prevmap[`${c.x-1}-${c.y}`]={...c}
        hashmap[`${c.x-1}-${c.y}`]=true
      }
      if(c.y+1 < 25 && !hashmap[`${c.x}-${c.y+1}`] && !graph[c.y+1][c.x].iswall){
        queue.unshift({x:c.x ,y:c.y+1})
        prevmap[`${c.x}-${c.y+1}`]={...c}
        hashmap[`${c.x}-${c.y+1}`]=true
      }
      if(c.y-1 >=0 && !hashmap[`${c.x}-${c.y-1}`] && !graph[c.y-1][c.x].iswall){
        queue.unshift({x:c.x ,y:c.y-1})
        prevmap[`${c.x}-${c.y-1}`]={...c}
        hashmap[`${c.x}-${c.y-1}`]=true
      }
    }
    return null
  }

  function BDS(graph,hashmap,prevmap,start,target){
    let queue=[start]
    let count=0
    hashmap[`${start.x}-${start.y}`]=true
    while (queue.length > 0){
      count+=1
      let c=queue[0]
      queue.shift()
      refarray[c.x+c.y*50].current.style['transition-delay']=`${count * 8}ms`
      refarray[c.x+c.y*50].current.classList.add('visited')
      if (c.x == target.x && c.y == target.y) return [c,count]
 
      
      
      if(c.y+1 < 25 && !hashmap[`${c.x}-${c.y+1}`] && !graph[c.y+1][c.x].iswall){
        queue.unshift({x:c.x ,y:c.y+1})
        prevmap[`${c.x}-${c.y+1}`]={...c}
        hashmap[`${c.x}-${c.y+1}`]=true
      }
      if(c.x-1 >=0 && !hashmap[`${c.x-1}-${c.y}`] && !graph[c.y][c.x-1].iswall){
        queue.unshift({x:c.x -1,y:c.y})
        prevmap[`${c.x-1}-${c.y}`]={...c}
        hashmap[`${c.x-1}-${c.y}`]=true
      }
      if(c.y-1 >=0 && !hashmap[`${c.x}-${c.y-1}`] && !graph[c.y-1][c.x].iswall){
        queue.unshift({x:c.x ,y:c.y-1})
        prevmap[`${c.x}-${c.y-1}`]={...c}
        hashmap[`${c.x}-${c.y-1}`]=true
      }
      if(c.x+1 < 50 && !hashmap[`${c.x+1}-${c.y}`] && !graph[c.y][c.x+1].iswall){
        queue.unshift({x:c.x +1,y:c.y})
        prevmap[`${c.x+1}-${c.y}`]={...c}
        hashmap[`${c.x+1}-${c.y}`]=true
      }
    }
    return null
  }
```

Nous exécuterons l'algorithme uniquement lorsque le bouton de démarrage dans la barre de navigation est cliqué. Cela changera la valeur de run, donc nous exécuterons un useEffect pour cela avec la variable de contexte run dans son tableau de dépendances.

Nous sauvegarderons la valeur de retour dans une variable **result**. Si le résultat est null, nous ne ferons rien et il n'y aura pas de chemin. Sinon, nous utiliserons les coordonnées de la cible et le prevmap pour obtenir le chemin du point de départ à la cible. Ensuite, nous exécuterons un timeout avec un callback qui ajoutera la classe path et le délai de transition correspondant à chaque cellule.

Voici à quoi le code ressemblera :

```js
 useEffect(()=>{

if (algo == 'BFS'){
  let hashmap={}
  let prevmap={}
  for (let j=0;j<25;j++){
   for (let i=0;i<50;i++){
     hashmap[`${i}-${j}`]=false
     prevmap[`${i}-${j}`]=null
   }
 }
 let result=BFS(grid,hashmap,prevmap,start.current,end.current)
 let path=[]
 if (result !=null){
  let current=result[0]
  while (prevmap[`${current.x}-${current.y}`] != null){
    path.push(current)
    current=prevmap[`${current.x}-${current.y}`]
  }
  setTimeout(()=>{path.reverse().forEach((elem,index)=>{
    refarray[elem.x+elem.y*50].current.style['transition-delay']=`${( index) * 15}ms`
      refarray[elem.x+elem.y*50].current.classList.add('path')
  })},result[1]*9)
  
 }
  
 
}
if (algo == 'BDS'){
  let hashmap={}
  let prevmap={}
  for (let j=0;j<25;j++){
   for (let i=0;i<50;i++){
     hashmap[`${i}-${j}`]=false
     prevmap[`${i}-${j}`]=null
   }
 }
  let result=BDS(grid,hashmap,prevmap,start.current,end.current)
  let path=[]
  if (result !=null){
   let current=result[0]
   while (prevmap[`${current.x}-${current.y}`] != null){
     path.push(current)
     current=prevmap[`${current.x}-${current.y}`]
   }
   setTimeout(()=>{path.reverse().forEach((elem,index)=>{
     refarray[elem.x+elem.y*50].current.style['transition-delay']=`${( index) * 15}ms`
       refarray[elem.x+elem.y*50].current.classList.add('path')
   })},result[1]*9)
   
  }
   
  
 }
 },[run])

```

Maintenant, après avoir appuyé sur le bouton de démarrage, voici le résultat que nous allons obtenir :

![Image](https://www.freecodecamp.org/news/content/images/2022/11/Screenshot--79-.png)

## Comment effacer le tableau

Les effets secondaires de l'exécution de ces algorithmes sont les classes que nous avons ajoutées et la propriété de délai de transition (que nous devons effacer avant d'exécuter à nouveau l'algorithme). C'est ce que nous allons faire pour réinitialiser la grille.

La dernière chose dont nous devons nous soucier est d'effacer le tableau. Cela se produira lorsque le bouton d'effacement dans la barre de navigation sera cliqué, et il changera la valeur de la variable de contexte res.

Donc, le dernier useEffect parcourra chaque ref du refarray et réinitialisera ses classes et son délai de transition. De plus, dans le contexte, il y a un autre useEffect qui régénérera une nouvelle grille (vous pouvez vérifier le code du contexte). Cela ressemblera à ceci :

```js
 useEffect(()=>{
  refarray.forEach((elem)=>{elem.current.style['transition-delay']='0ms'})
  refarray.forEach((elem)=>{elem.current.classList.remove('visited');elem.current.classList.remove('path')})
 },[res])
```

Voici le CSS pour la grille :

```css
.board{
    width:100%;
    height:calc(100vh - min(20vh , 100px));
    background:black;
    display:grid;
    grid-template-rows: repeat(25 , 1fr);
    grid-template-columns: repeat(50 , 1fr);
    gap: 1px;
    
}

.board .cell{
    display:flex;
    justify-content: center;
    align-items: center;
    background: white;
}

.wall {
    background:black !important
}

.visited{
    background:rgb(33, 85, 228) !important;
    transition:all 8ms cubic-bezier(0.075, 0.82, 0.165, 1);
  
}

.path{
    background:rgb(244, 255, 87) !important ;
    transition:all 8ms cubic-bezier(0.075, 0.82, 0.165, 1);

    
}

```

Maintenant, lorsque vous cliquez sur le bouton de redémarrage, le tableau sera de retour à la normale.

## Conclusion

Enfin, dans ce tutoriel, nous avons appris beaucoup de choses sur les algorithmes de recherche de chemin, React, les contextes, les refs, la pensée algorithmique et bien plus encore.

J'espère que vous avez apprécié ce tutoriel autant que j'ai apprécié l'écrire. C'est l'un des nombreux tutoriels que je vais créer pour freeCodeCamp.

Vous trouverez le code de ce projet sur mon [GitHub](https://github.com/housseinbadra) et voici la [version hébergée](https://houssein-algo-visualizer.netlify.app/). Si vous voulez me soutenir, [suivez-moi sur LinkedIn](https://www.linkedin.com/in/houssein-badra-943879214). Cela signifie beaucoup pour moi.