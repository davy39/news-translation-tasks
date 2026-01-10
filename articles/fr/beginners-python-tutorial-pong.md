---
title: 'Tutoriel Python pour débutants : Pong'
subtitle: ''
author: Beau Carnes
co_authors: []
series: null
date: '2023-08-23T20:45:10.000Z'
originalURL: https://freecodecamp.org/news/beginners-python-tutorial-pong
coverImage: https://www.freecodecamp.org/news/content/images/2023/08/pong.jpg
tags:
- name: Python
  slug: python
- name: youtube
  slug: youtube
seo_title: 'Tutoriel Python pour débutants : Pong'
seo_desc: 'Pong was one of the first video games. And it also makes a good first (or
  early) Python project when you are learning to code.

  We just published a course on the freeCodeCamp.org YouTube channel that will help
  you improve your Python and Pygame skills...'
---

Pong était l'un des premiers jeux vidéo. Et il constitue également un bon premier (ou précoce) projet Python lorsque vous apprenez à coder.

Nous venons de publier un cours sur la chaîne YouTube freeCodeCamp.org qui vous aidera à améliorer vos compétences en Python et Pygame en vous apprenant à construire le jeu classique pong, mais cette fois avec des fonctionnalités supplémentaires. Ce tutoriel pour débutants est un excellent moyen de commencer à apprendre à créer des jeux engageants avec des mécaniques uniques.

<canvas></canvas>
<script>
// Variables globales
var DIRECTION = {
	IDLE: 0,
	UP: 1,
	DOWN: 2,
	LEFT: 3,
	RIGHT: 4
};

var rounds = [5, 5, 3, 3, 2];
var colors = ['#1abc9c', '#2ecc71', '#3498db', '#e74c3c', '#9b59b6'];

// L'objet ball (Le cube qui rebondit d'avant en arrière)
var Ball = {
	new: function (incrementedSpeed) {
		return {
			width: 18,
			height: 18,
			x: (this.canvas.width / 2) - 9,
			y: (this.canvas.height / 2) - 9,
			moveX: DIRECTION.IDLE,
			moveY: DIRECTION.IDLE,
			speed: incrementedSpeed || 9
		};
	}
};

// L'objet paddle (Les deux lignes qui montent et descendent)
var Paddle = {
	new: function (side) {
		return {
			width: 18,
			height: 70,
			x: side === 'left' ? 150 : this.canvas.width - 150,
			y: (this.canvas.height / 2) - 35,
			score: 0,
			move: DIRECTION.IDLE,
			speed: 10
		};
	}
};

var Game = {
	initialize: function () {
		this.canvas = document.querySelector('canvas');
		this.context = this.canvas.getContext('2d');

		this.canvas.width = 1400;
		this.canvas.height = 1000;

		this.canvas.style.width = (this.canvas.width / 2) + 'px';
		this.canvas.style.height = (this.canvas.height / 2) + 'px';

		this.player = Paddle.new.call(this, 'left');
		this.paddle = Paddle.new.call(this, 'right');
		this.ball = Ball.new.call(this);

		this.paddle.speed = 8;
		this.running = this.over = false;
		this.turn = this.paddle;
		this.timer = this.round = 0;
		this.color = '#2c3e50';

		Pong.menu();
		Pong.listen();
	},

	endGameMenu: function (text) {
		// Changer la taille et la couleur de la police du canvas
		Pong.context.font = '50px Courier New';
		Pong.context.fillStyle = this.color;

		// Dessiner le rectangle derrière le texte 'Appuyez sur n'importe quelle touche pour commencer'.
		Pong.context.fillRect(
			Pong.canvas.width / 2 - 350,
			Pong.canvas.height / 2 - 48,
			700,
			100
		);

		// Changer la couleur du canvas;
		Pong.context.fillStyle = '#ffffff';

		// Dessiner le texte du menu de fin de jeu ('Game Over' et 'Winner')
		Pong.context.fillText(text,
			Pong.canvas.width / 2,
			Pong.canvas.height / 2 + 15
		);

		setTimeout(function () {
			Pong = Object.assign({}, Game);
			Pong.initialize();
		}, 3000);
	},

	menu: function () {
		// Dessiner tous les objets Pong dans leur état actuel
		Pong.draw();

		// Changer la taille et la couleur de la police du canvas
		this.context.font = '50px Courier New';
		this.context.fillStyle = this.color;

		// Dessiner le rectangle derrière le texte 'Appuyez sur n'importe quelle touche pour commencer'.
		this.context.fillRect(
			this.canvas.width / 2 - 350,
			this.canvas.height / 2 - 48,
			700,
			100
		);

		// Changer la couleur du canvas;
		this.context.fillStyle = '#ffffff';

		// Dessiner le texte 'appuyez sur n'importe quelle touche pour commencer'
		this.context.fillText('Appuyez sur n\'importe quelle touche pour commencer',
			this.canvas.width / 2,
			this.canvas.height / 2 + 15
		);
	},

	// Mettre à jour tous les objets (déplacer le joueur, la palette, la balle, incrémenter le score, etc.)
	update: function () {
		if (!this.over) {
			// Si la balle entre en collision avec les limites - corriger les coordonnées x et y.
			if (this.ball.x <= 0) Pong._resetTurn.call(this, this.paddle, this.player);
			if (this.ball.x >= this.canvas.width - this.ball.width) Pong._resetTurn.call(this, this.player, this.paddle);
			if (this.ball.y <= 0) this.ball.moveY = DIRECTION.DOWN;
			if (this.ball.y >= this.canvas.height - this.ball.height) this.ball.moveY = DIRECTION.UP;

			// Déplacer le joueur si la valeur player.move a été mise à jour par un événement clavier
			if (this.player.move === DIRECTION.UP) this.player.y -= this.player.speed;
			else if (this.player.move === DIRECTION.DOWN) this.player.y += this.player.speed;

			// Au nouveau service (début de chaque tour) déplacer la balle du côté correct
			// et randomiser la direction pour ajouter un peu de défi.
			if (Pong._turnDelayIsOver.call(this) && this.turn) {
				this.ball.moveX = this.turn === this.player ? DIRECTION.LEFT : DIRECTION.RIGHT;
				this.ball.moveY = [DIRECTION.UP, DIRECTION.DOWN][Math.round(Math.random())];
				this.ball.y = Math.floor(Math.random() * this.canvas.height - 200) + 200;
				this.turn = null;
			}

			// Si le joueur entre en collision avec les limites, mettre à jour les coordonnées x et y.
			if (this.player.y <= 0) this.player.y = 0;
			else if (this.player.y >= (this.canvas.height - this.player.height)) this.player.y = (this.canvas.height - this.player.height);

			// Déplacer la balle dans la direction souhaitée basée sur les valeurs moveY et moveX
			if (this.ball.moveY === DIRECTION.UP) this.ball.y -= (this.ball.speed / 1.5);
			else if (this.ball.moveY === DIRECTION.DOWN) this.ball.y += (this.ball.speed / 1.5);
			if (this.ball.moveX === DIRECTION.LEFT) this.ball.x -= this.ball.speed;
			else if (this.ball.moveX === DIRECTION.RIGHT) this.ball.x += this.ball.speed;

			// Gérer le mouvement de la palette (IA) vers le haut et vers le bas
			if (this.paddle.y > this.ball.y - (this.paddle.height / 2)) {
				if (this.ball.moveX === DIRECTION.RIGHT) this.paddle.y -= this.paddle.speed / 1.5;
				else this.paddle.y -= this.paddle.speed / 4;
			}
			if (this.paddle.y < this.ball.y - (this.paddle.height / 2)) {
				if (this.ball.moveX === DIRECTION.RIGHT) this.paddle.y += this.paddle.speed / 1.5;
				else this.paddle.y += this.paddle.speed / 4;
			}

			// Gérer la collision de la palette (IA) avec le mur
			if (this.paddle.y >= this.canvas.height - this.paddle.height) this.paddle.y = this.canvas.height - this.paddle.height;
			else if (this.paddle.y <= 0) this.paddle.y = 0;

			// Gérer les collisions Joueur-Balle
			if (this.ball.x - this.ball.width <= this.player.x && this.ball.x >= this.player.x - this.player.width) {
				if (this.ball.y <= this.player.y + this.player.height && this.ball.y + this.ball.height >= this.player.y) {
					this.ball.x = (this.player.x + this.ball.width);
					this.ball.moveX = DIRECTION.RIGHT;


				}
			}

			// Gérer la collision palette-balle
			if (this.ball.x - this.ball.width <= this.paddle.x && this.ball.x >= this.paddle.x - this.paddle.width) {
				if (this.ball.y <= this.paddle.y + this.paddle.height && this.ball.y + this.ball.height >= this.paddle.y) {
					this.ball.x = (this.paddle.x - this.ball.width);
					this.ball.moveX = DIRECTION.LEFT;


				}
			}
		}

		// Gérer la transition de fin de manche
		// Vérifier si le joueur a gagné la manche.
		if (this.player.score === rounds[this.round]) {
			// Vérifier s'il reste des manches/niveaux et afficher l'écran de victoire s'il
			// n'y en a pas.
			if (!rounds[this.round + 1]) {
				this.over = true;
				setTimeout(function () { Pong.endGameMenu('Gagnant !'); }, 1000);
			} else {
				// S'il y a une autre manche, réinitialiser toutes les valeurs et incrémenter le numéro de manche.
				this.color = this._generateRoundColor();
				this.player.score = this.paddle.score = 0;
				this.player.speed += 0.5;
				this.paddle.speed += 1;
				this.ball.speed += 1;
				this.round += 1;

			}
		}
		// Vérifier si la palette/IA a gagné la manche.
		else if (this.paddle.score === rounds[this.round]) {
			this.over = true;
			setTimeout(function () { Pong.endGameMenu('Game Over !'); }, 1000);
		}
	},

	// Dessiner les objets sur l'élément canvas
	draw: function () {
		// Effacer le Canvas
		this.context.clearRect(
			0,
			0,
			this.canvas.width,
			this.canvas.height
		);

		// Définir le style de remplissage sur noir
		this.context.fillStyle = this.color;

		// Dessiner l'arrière-plan
		this.context.fillRect(
			0,
			0,
			this.canvas.width,
			this.canvas.height
		);

		// Définir le style de remplissage sur blanc (Pour les palettes et la balle)
		this.context.fillStyle = '#ffffff';

		// Dessiner le Joueur
		this.context.fillRect(
			this.player.x,
			this.player.y,
			this.player.width,
			this.player.height
		);

		// Dessiner la Palette
		this.context.fillRect(
			this.paddle.x,
			this.paddle.y,
			this.paddle.width,
			this.paddle.height
		);

		// Dessiner la Balle
		if (Pong._turnDelayIsOver.call(this)) {
			this.context.fillRect(
				this.ball.x,
				this.ball.y,
				this.ball.width,
				this.ball.height
			);
		}

		// Dessiner le filet (Ligne au milieu)
		this.context.beginPath();
		this.context.setLineDash([7, 15]);
		this.context.moveTo((this.canvas.width / 2), this.canvas.height - 140);
		this.context.lineTo((this.canvas.width / 2), 140);
		this.context.lineWidth = 10;
		this.context.strokeStyle = '#ffffff';
		this.context.stroke();

		// Définir la police par défaut du canvas et l'aligner au centre
		this.context.font = '100px Courier New';
		this.context.textAlign = 'center';

		// Dessiner le score du joueur (gauche)
		this.context.fillText(
			this.player.score.toString(),
			(this.canvas.width / 2) - 300,
			200
		);

		// Dessiner le score de la palette (droite)
		this.context.fillText(
			this.paddle.score.toString(),
			(this.canvas.width / 2) + 300,
			200
		);

		// Changer la taille de la police pour le texte du score central
		this.context.font = '30px Courier New';

		// Dessiner le score gagnant (centre)
		this.context.fillText(
			'Manche ' + (Pong.round + 1),
			(this.canvas.width / 2),
			35
		);

		// Changer la taille de la police pour la valeur du score central
		this.context.font = '40px Courier';

		// Dessiner le numéro de la manche actuelle
		this.context.fillText(
			rounds[Pong.round] ? rounds[Pong.round] : rounds[Pong.round - 1],
			(this.canvas.width / 2),
			100
		);
	},

	loop: function () {
		Pong.update();
		Pong.draw();

		// Si le jeu n'est pas terminé, dessiner la prochaine frame.
		if (!Pong.over) requestAnimationFrame(Pong.loop);
	},

	listen: function () {
		document.addEventListener('keydown', function (key) {
			// Gérer la fonction 'Appuyez sur n'importe quelle touche pour commencer' et démarrer le jeu.
			if (Pong.running === false) {
				Pong.running = true;
				window.requestAnimationFrame(Pong.loop);
			}

			// Gérer les événements des touches flèche haut et w
			if (key.keyCode === 38 || key.keyCode === 87) Pong.player.move = DIRECTION.UP;

			// Gérer les événements des touches flèche bas et s
			if (key.keyCode === 40 || key.keyCode === 83) Pong.player.move = DIRECTION.DOWN;
		});

		// Arrêter le joueur de bouger quand aucune touche n'est pressée.
		document.addEventListener('keyup', function (key) { Pong.player.move = DIRECTION.IDLE; });
	},

	// Réinitialiser l'emplacement de la balle, les tours du joueur et définir un délai avant le début de la prochaine manche.
	_resetTurn: function(victor, loser) {
		this.ball = Ball.new.call(this, this.ball.speed);
		this.turn = loser;
		this.timer = (new Date()).getTime();

		victor.score++;
	
	},

	// Attendre qu'un délai se soit écoulé après chaque tour.
	_turnDelayIsOver: function() {
		return ((new Date()).getTime() - this.timer >= 1000);
	},

	// Sélectionner une couleur aléatoire comme arrière-plan de chaque niveau/manche.
	_generateRoundColor: function () {
		var newColor = colors[Math.floor(Math.random() * colors.length)];
		if (newColor === this.color) return Pong._generateRoundColor();
		return newColor;
	}
};

var Pong = Object.assign({}, Game);
Pong.initialize();
                </script>

_(Appuyez sur les touches fléchées pour jouer. Ce n'est pas la version que vous allez créer.)_

Rohan a créé ce cours et c'est un excellent projet pour débutants. Voici les sections de ce cours :

* Programme du cours
* Pong traditionnel
* Angles créatifs
* Élément smash
* Élément flash
* Clonage de balle
* Clonage de palette
* Élément écran de fin

Regardez le cours complet sur [la chaîne YouTube freeCodeCamp.org](https://youtu.be/tS8F7_X2qB0) (1 heure de visionnage).

%[https://youtu.be/tS8F7_X2qB0]