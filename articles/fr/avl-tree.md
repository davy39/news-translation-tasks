---
title: Insertion et Rotation dans un Arbre AVL
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2020-01-15T22:10:00.000Z'
originalURL: https://freecodecamp.org/news/avl-tree
coverImage: https://cdn-media-2.freecodecamp.org/w1280/5f9c9dda740569d1a4ca39fa.jpg
tags:
- name: algorithms
  slug: algorithms
- name: binary search
  slug: binary-search
- name: data structures
  slug: data-structures
- name: toothbrush
  slug: toothbrush
- name: Trees
  slug: trees
seo_title: Insertion et Rotation dans un Arbre AVL
seo_desc: An AVL tree is an improved version of the binary search tree (BST) that
  is self-balancing. It was named after its inventors Adelson-Velsky and Landis, and
  was first introduced in 1962, just two years after the design of the binary search
  tree in 1960...
---

Un arbre AVL est une version améliorée de l'arbre binaire de recherche (BST) qui est auto-équilibrant. Il a été nommé d'après ses inventeurs **A**delson-**V**elsky et **L**andis, et a été introduit pour la première fois en 1962, seulement deux ans après la conception de l'arbre binaire de recherche en 1960. L'arbre AVL est considéré comme étant la première structure de données de son type.

Un BST est une structure de données composée de nœuds. Il a les garanties suivantes :

1. Chaque arbre a un nœud racine (en haut).
2. Le nœud racine a zéro ou plusieurs nœuds enfants.
3. Chaque nœud enfant a zéro ou plusieurs nœuds enfants, et ainsi de suite.
4. Chaque nœud a jusqu'à deux enfants.
5. Pour chaque nœud, ses descendants de gauche sont inférieurs au nœud actuel, qui est inférieur aux descendants de droite.

Les arbres AVL ont une garantie supplémentaire :

1. La différence entre la profondeur des sous-arbres droit et gauche ne peut pas être supérieure à un.

Afin de maintenir cette garantie, les implémentations des arbres AVL incluent un algorithme pour rééquilibrer l'arbre lorsque l'ajout d'un élément supplémentaire provoquerait une différence de profondeur entre les arbres droit et gauche supérieure à un.

Les arbres AVL ont un temps d'exécution pire cas pour la recherche, l'insertion et la suppression de O(log n).

### **Rotation à Droite**

![Image](https://www.freecodecamp.org/news/content/images/2020/02/avl_right_rotation.jpg)
_Source : [https://github.com/HebleV/valet_parking/tree/master/images](https://github.com/HebleV/valet_parking/tree/master/images)_

### **Rotation à Gauche**

![Image](https://www.freecodecamp.org/news/content/images/2020/02/avl_left_rotation.jpg)
_Source : [https://github.com/HebleV/valet_parking/tree/master/images](https://github.com/HebleV/valet_parking/tree/master/images)_

### **Processus d'Insertion dans un AVL**

Cela fonctionne de manière similaire à une insertion normale dans un arbre binaire de recherche. Après l'insertion, vous corrigez la propriété AVL en utilisant des rotations à gauche ou à droite.

* S'il y a un déséquilibre dans l'enfant gauche du sous-arbre droit, alors vous effectuez une rotation gauche-droite.
* S'il y a un déséquilibre dans l'enfant gauche du sous-arbre gauche, alors vous effectuez une rotation à droite.
* S'il y a un déséquilibre dans l'enfant droit du sous-arbre droit, alors vous effectuez une rotation à gauche.
* S'il y a un déséquilibre dans l'enfant droit du sous-arbre gauche, alors vous effectuez une rotation droite-gauche.

### Exemple

Voici un exemple d'un arbre AVL en Python :

```py
class node:
	def __init__(self,value=None):
		self.value=value
		self.left_child=None
		self.right_child=None
		self.parent=None # pointeur vers le nœud parent dans l'arbre
		self.height=1 # hauteur du nœud dans l'arbre (distance max. à la feuille) NOUVEAU POUR AVL

class AVLTree:
	def __init__(self):
		self.root=None

	def __repr__(self):
		if self.root==None: return ''
		content='\n' # pour contenir la chaîne finale
		cur_nodes=[self.root] # tous les nœuds au niveau actuel
		cur_height=self.root.height # hauteur des nœuds au niveau actuel
		sep=' '*(2**(cur_height-1)) # séparateur de taille variable entre les éléments
		while True:
			cur_height+=-1 # décrémenter la hauteur actuelle
			if len(cur_nodes)==0: break
			cur_row=' '
			next_row=''
			next_nodes=[]

			if all(n is None for n in cur_nodes):
				break

			for n in cur_nodes:

				if n==None:
					cur_row+='   '+sep
					next_row+='   '+sep
					next_nodes.extend([None,None])
					continue

				if n.value!=None:       
					buf=' '*int((5-len(str(n.value)))/2)
					cur_row+='%s%s%s'%(buf,str(n.value),buf)+sep
				else:
					cur_row+=' '*5+sep

				if n.left_child!=None:  
					next_nodes.append(n.left_child)
					next_row+=' /'+sep
				else:
					next_row+='  '+sep
					next_nodes.append(None)

				if n.right_child!=None: 
					next_nodes.append(n.right_child)
					next_row+='\ '+sep
				else:
					next_row+='  '+sep
					next_nodes.append(None)

			content+=(cur_height*'   '+cur_row+'\n'+cur_height*'   '+next_row+'\n')
			cur_nodes=next_nodes
			sep=' '*int(len(sep)/2) # réduire de moitié la taille du séparateur
		return content

	def insert(self,value):
		if self.root==None:
			self.root=node(value)
		else:
			self._insert(value,self.root)

	def _insert(self,value,cur_node):
		if value<cur_node.value:
			if cur_node.left_child==None:
				cur_node.left_child=node(value)
				cur_node.left_child.parent=cur_node # définir le parent
				self._inspect_insertion(cur_node.left_child)
			else:
				self._insert(value,cur_node.left_child)
		elif value>cur_node.value:
			if cur_node.right_child==None:
				cur_node.right_child=node(value)
				cur_node.right_child.parent=cur_node # définir le parent
				self._inspect_insertion(cur_node.right_child)
			else:
				self._insert(value,cur_node.right_child)
		else:
			print("Valeur déjà dans l'arbre !")

	def print_tree(self):
		if self.root!=None:
			self._print_tree(self.root)

	def _print_tree(self,cur_node):
		if cur_node!=None:
			self._print_tree(cur_node.left_child)
			print ('%s, h=%d'%(str(cur_node.value),cur_node.height))
			self._print_tree(cur_node.right_child)

	def height(self):
		if self.root!=None:
			return self._height(self.root,0)
		else:
			return 0

	def _height(self,cur_node,cur_height):
		if cur_node==None: return cur_height
		left_height=self._height(cur_node.left_child,cur_height+1)
		right_height=self._height(cur_node.right_child,cur_height+1)
		return max(left_height,right_height)

	def find(self,value):
		if self.root!=None:
			return self._find(value,self.root)
		else:
			return None

	def _find(self,value,cur_node):
		if value==cur_node.value:
			return cur_node
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._find(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._find(value,cur_node.right_child)

	def delete_value(self,value):
		return self.delete_node(self.find(value))

	def delete_node(self,node):

		## -----
		# Améliorations depuis la leçon précédente

		# Protéger contre la suppression d'un nœud non trouvé dans l'arbre
		if node==None or self.find(node.value)==None:
			print("Nœud à supprimer non trouvé dans l'arbre !")
			return None 
		## -----

		# retourne le nœud avec la valeur minimale dans l'arbre enraciné au nœud d'entrée
		def min_value_node(n):
			current=n
			while current.left_child!=None:
				current=current.left_child
			return current

		# retourne le nombre d'enfants pour le nœud spécifié
		def num_children(n):
			num_children=0
			if n.left_child!=None: num_children+=1
			if n.right_child!=None: num_children+=1
			return num_children

		# obtenir le parent du nœud à supprimer
		node_parent=node.parent

		# obtenir le nombre d'enfants du nœud à supprimer
		node_children=num_children(node)

		# diviser l'opération en différents cas basés sur la
		# structure de l'arbre et du nœud à supprimer

		# CAS 1 (le nœud n'a pas d'enfants)
		if node_children==0:

			if node_parent!=None:
				# supprimer la référence au nœud du parent
				if node_parent.left_child==node:
					node_parent.left_child=None
				else:
					node_parent.right_child=None
			else:
				self.root=None

		# CAS 2 (le nœud a un seul enfant)
		if node_children==1:

			# obtenir le nœud enfant unique
			if node.left_child!=None:
				child=node.left_child
			else:
				child=node.right_child

			if node_parent!=None:
				# remplacer le nœud à supprimer par son enfant
				if node_parent.left_child==node:
					node_parent.left_child=child
				else:
					node_parent.right_child=child
			else:
				self.root=child

			# corriger le pointeur parent dans le nœud
			child.parent=node_parent

		# CAS 3 (le nœud a deux enfants)
		if node_children==2:

			# obtenir le successeur dans l'ordre du nœud supprimé
			successor=min_value_node(node.right_child)

			# copier la valeur du successeur dans l'ordre vers le nœud contenant
			# précédemment la valeur que nous souhaitions supprimer
			node.value=successor.value

			# supprimer le successeur dans l'ordre maintenant que sa valeur a été
			# copiée dans l'autre nœud
			self.delete_node(successor)

			# quitter la fonction pour ne pas appeler _inspect_deletion deux fois
			return

		if node_parent!=None:
			# corriger la hauteur du parent du nœud actuel
			node_parent.height=1+max(self.get_height(node_parent.left_child),self.get_height(node_parent.right_child))

			# commencer à remonter l'arbre en vérifiant s'il y a
			# des sections qui invalident maintenant les règles d'équilibre AVL
			self._inspect_deletion(node_parent)

	def search(self,value):
		if self.root!=None:
			return self._search(value,self.root)
		else:
			return False

	def _search(self,value,cur_node):
		if value==cur_node.value:
			return True
		elif value<cur_node.value and cur_node.left_child!=None:
			return self._search(value,cur_node.left_child)
		elif value>cur_node.value and cur_node.right_child!=None:
			return self._search(value,cur_node.right_child)
		return False 


	# Fonctions ajoutées pour AVL...

	def _inspect_insertion(self,cur_node,path=[]):
		if cur_node.parent==None: return
		path=[cur_node]+path

		left_height =self.get_height(cur_node.parent.left_child)
		right_height=self.get_height(cur_node.parent.right_child)

		if abs(left_height-right_height)>1:
			path=[cur_node.parent]+path
			self._rebalance_node(path[0],path[1],path[2])
			return

		new_height=1+cur_node.height 
		if new_height>cur_node.parent.height:
			cur_node.parent.height=new_height

		self._inspect_insertion(cur_node.parent,path)

	def _inspect_deletion(self,cur_node):
		if cur_node==None: return

		left_height =self.get_height(cur_node.left_child)
		right_height=self.get_height(cur_node.right_child)

		if abs(left_height-right_height)>1:
			y=self.taller_child(cur_node)
			x=self.taller_child(y)
			self._rebalance_node(cur_node,y,x)

		self._inspect_deletion(cur_node.parent)

	def _rebalance_node(self,z,y,x):
		if y==z.left_child and x==y.left_child:
			self._right_rotate(z)
		elif y==z.left_child and x==y.right_child:
			self._left_rotate(y)
			self._right_rotate(z)
		elif y==z.right_child and x==y.right_child:
			self._left_rotate(z)
		elif y==z.right_child and x==y.left_child:
			self._right_rotate(y)
			self._left_rotate(z)
		else:
			raise Exception('_rebalance_node: configuration des nœuds z,y,x non reconnue !')

	def _right_rotate(self,z):
		sub_root=z.parent 
		y=z.left_child
		t3=y.right_child
		y.right_child=z
		z.parent=y
		z.left_child=t3
		if t3!=None: t3.parent=z
		y.parent=sub_root
		if y.parent==None:
				self.root=y
		else:
			if y.parent.left_child==z:
				y.parent.left_child=y
			else:
				y.parent.right_child=y		
		z.height=1+max(self.get_height(z.left_child),
			self.get_height(z.right_child))
		y.height=1+max(self.get_height(y.left_child),
			self.get_height(y.right_child))

	def _left_rotate(self,z):
		sub_root=z.parent 
		y=z.right_child
		t2=y.left_child
		y.left_child=z
		z.parent=y
		z.right_child=t2
		if t2!=None: t2.parent=z
		y.parent=sub_root
		if y.parent==None: 
			self.root=y
		else:
			if y.parent.left_child==z:
				y.parent.left_child=y
			else:
				y.parent.right_child=y
		z.height=1+max(self.get_height(z.left_child),
			self.get_height(z.right_child))
		y.height=1+max(self.get_height(y.left_child),
			self.get_height(y.right_child))

	def get_height(self,cur_node):
		if cur_node==None: return 0
		return cur_node.height

	def taller_child(self,cur_node):
		left=self.get_height(cur_node.left_child)
		right=self.get_height(cur_node.right_child)
		return cur_node.left_child if left>=right else cur_node.right_child
```

### Plus d'informations sur la recherche binaire :

* [Les bases de la recherche binaire](https://guide.freecodecamp.org/algorithms/search-algorithms/binary-search/)
* [Les arbres binaires de recherche expliqués avec des exemples](https://www.freecodecamp.org/news/binary-search-tree-what-is-it/)
* [Structures de données binaires : introduction aux arbres (et aux tas)](https://www.freecodecamp.org/news/binary-data-structures-an-intro-to-trees-and-heaps-in-javascript-962ab536cb42/)