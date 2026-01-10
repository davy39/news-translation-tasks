---
title: 'The Robotic Influencers of our Future: Experimenting With a Minecraft-playing,
  Twitch-streaming Robot'
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2019-10-01T21:26:15.000Z'
originalURL: https://freecodecamp.org/news/the-robotic-influencers-of-our-future-a-minecraft-playing-twitch-streaming-robot
coverImage: https://www.freecodecamp.org/news/content/images/2019/10/twitchrobot.png
tags:
- name: gaming
  slug: gaming
- name: minecraft
  slug: minecraft
- name: robotics
  slug: robotics
- name: streaming
  slug: streaming
- name: Twitch
  slug: twitch
seo_title: null
seo_desc: 'By Minja Axelsson

  In this article, I''ll discuss how we reached young audiences by combining robotics
  with e-sports.

  What on Earth?

  Ever heard of anything like it before? Me neither. The robot was created as part
  of Futurice’s project with Yle, the na...'
---

By Minja Axelsson

In this article, I'll discuss how we reached young audiences by combining robotics with e-sports.

## What on Earth?

Ever heard of anything like it before? Me neither. The robot was created as part of [Futurice](https://www.futurice.com/)’s project with [Yle](https://yle.fi/), the national broadcast company of Finland. 

Yle produces content for TV, radio, and the web. It has a broad reach of older audiences, but has had trouble reaching younger ones. The goal of this project was to use new technology to reach young audiences — specifically teenagers.

Yle’s content has traditionally been non-participatory: the performers perform, and the audience watches. However, younger audiences generally view content that is more participatory, such as YouTube videos or streams. 

We wanted to create participatory content — the performer should interact with their audience. Yle’s journalists specialized in teenage audiences pointed out that gaming and e-sports are popular content. We realized that gaming was the perfect context for this: the audience could play together with the performer. We wanted to explore what an entertainer, or even influencer of the future could look like. So why not create a streaming robot gamer?

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_QW08nV9GgKS589PJ.png)
_Yle’s journalists and Futurice’s roboticists coming up with the idea of a robot gamer_

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_XdFOgvs4DhZVaHnW.png)
_First drafts_

## What Was This Robot Like?

We chose two games for the robot to play: Flappy Bird and Minecraft.

Flappy Bird was a cult game that had a brief period of extreme popularity in 2014. We chose Flappy Bird because the mechanisms of the game are simple, and allowed for the game to be played with machine learning. We wanted to try a [neuroevolution algorithm](https://xviniette.github.io/FlappyLearning/), which evolved new birds into the game based on which birds did best in the previous generation. This way we could see how the audience reacted when a computer was playing the game.

We chose Minecraft for its communal features, which allow interaction between players. Players can co-operate or fight each other, trade with each other, and chat with each other. They can “grief” each other — i.e. be a nuisance. Players can also mine materials, and turn them into items, or even build cities. They can store precious things, farm the land, herd animals, and fight monsters. 

Minecraft also has a material called redstone, which players can use to build logic. Effectively, players can build an entire computer inside of Minecraft. Poetic, eh?

For playing Minecraft, we decided that a human should control the robot. The game is complicated, and having authentic interactions with other players would require a human on the other end.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_zNxCX_zKJ3ikRM-y.png)
_Flappy Bird and the robot_

Our team of Yle’s journalists and Futurice roboticists defined some clear advantages for using a robot in this context:

* A robot is tireless — it can play forever, and provide content 24/7. It’s an ideal streamer.
* A robot can be gender neutral. Gamers and gaming audiences are typically male, but a gender neutral robot could potentially attract more diverse audiences.
* A robot can reflect gamers’ behaviour, stirring emotions. Gaming culture is often aggressive. The robot could be aggressive in turn, making gamers reflect on their own behaviour.
* A robot can interact within the game and chat simultaneously. Humans are limited to one output, a robot can have several.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/1_-eTZqndK5kdFckQ5-lXpMg.jpeg)
_Testing our streaming equipment and having problems with interference from the robot’s face screen._

We decided on a six hour gaming session, alternating between Minecraft and Flappy Bird. To nail down the user experience for the session, we defined guidelines for our design of the robot:

* Experimental user experience — the user should be able to explore within the interaction with the robot.
* Streamers are usually strong characters. The robot is a character with a strong personality.
* The robot can cause “WTF?” reactions in players. We wanted the experience to be memorable, rather than bland.
* The culture and space of online gaming is unique, and should be designed for.

Based on these guidelines, we created the character IQ_201. IQ_201 is based on aggressive online gamers that are convinced of their own superior intelligence (see [this meme about having an IQ over 200](https://knowyourmeme.com/memes/200-iq)). The robot would be rude and reactive, meant to get a reaction out of adolescents interacting with it.

Before implementation, the team also wanted to take into account some ethical considerations:

* Transparency about how the robot is operated is needed. If this robot was going to be put into production, users should be able to find information on how it works.
* The robot should treat all the players the same. This was also part of the decision to make the robot appear gender neutral. And due to the sometimes angry, hateful, even racist or sexist culture of gaming, we needed to design the robot’s personality carefully. It could be out-there, even rude, but never hateful. We didn’t want any heated gaming moments.
* The robot should be rude, but not too over-the-top.
* The chat needed to be moderated. As stated, gaming culture can be toxic. We wanted to keep a careful eye on both the Minecraft and Twitch chats, to ensure no shenanigans would go on.

To fulfill all these requirements, we selected the [Furhat robot](https://www.furhatrobotics.com/). The Furhat robot had a relatively easy-to-use teleoperation interface, which allowed for the user to input text to be turned into the robot’s speech, as well as perform gestures at the click of a button.

## Flowers and Violence

We had a 6 hour stream, starting at 2pm and ending at 8pm. We alternated between games: 2-3pm was Flappy Bird, 3-5pm Minecraft, 5-6pm Flappy Bird, then 6-8pm Minecraft again. This schedule allowed the robot operators playing Minecraft to have a much-needed break in the middle.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/twitchrobot-1.png)
_Our robot_

In the beginning, a few people joined. Gradually, we gained more and more people. We reached our peak at 4:20 — 49 simultaneous viewers on Twitch. Overall, we had 431 unique viewers. In Minecraft, there were around 30 active players. Considering how minimal our advertising was (one forum post and a few tweets), we were pleasantly surprised by the turnout.

The Minecraft sessions were directed by two robot operators (myself and another Minja). The other Minja played Minecraft, and I operated the robot’s voice and gestures. A third person was answering messages on chat.

%[https://www.youtube.com/watch?v=8kKPoYx7rMs]

Minecraft was overwhelming. The robot’s provocative character provoked teenagers into repeatedly killing it. After fleeing to the mountains to be with the llamas a couple of times and being killed yet again, we modified the robot’s behaviour to be more friendly. We wanted to create more constructive interactions.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_pMMw-X8ZYwIOH_cU.png)
_Two Minjas as robot operators_

Toward the end of the second Minecraft stream, teenagers were cooperating with the robot. They protected it from the few aggressive players that were left, and gave it gifts such as flowers. Some even complimented the robot directly, to make it happy. The players started following the robot, agreeing to cooperate when it initiated building a lighthouse. They also built a house, and captured and named a llama: IQ_201 Junior.

There were two clear factions in the game: some were intent to kill the robot throughout the entire game, and some protected it throughout. Some became more comfortable with the robot as the stream went on, switching sides. Either way, the robot aroused strong emotions. Teenagers sought out genuine interaction with it. No-one ignored the robot, or was bored.

Discussions about how the robot worked were had throughout the stream. No-one asked the robot itself though, maybe out of respect or fear of annoying it. Discussions focused on whether the robot was “real”, i.e. whether it was truly automatic, or a human was operating it. Was it typing with actual physical hands? Or had it “hacked into” the game and was playing via code?

## “I Will Miss You Robot!”

16 people responded to our survey afterward. 80% of players were under 18, most were 13 to 15-year-olds. 80% of players interacted with the robot. This was extremely positive, we succeeded in making a robot that was compelling to users. 75% of players rated the robot as 3 or above, out of 5.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_7k1TlGnl986zyBKQ.png)
_Viewers over time_

We collected comments from the players from the survey, as well as the Minecraft game chat. They are translated from Finnish, and reflect some of the thoughts our players had on the robot.

#### The critical first:

**“It was pretty fun and cool. But it somehow felt like a set-up.” [Referring to the robot possibly having a human operator]**

A lot of players were wondering how the robot actually worked. This comment brings us back to the ethical consideration we talked about earlier: transparency about how the robot was operated. 

Though we intended to be transparent at first, we decided to not inform users of the robot’s teleoperated nature for this first pilot. We made this choice because we wanted to keep the “suspension of disbelief” of the user active, meaning that we wanted the participants to play along with the fact they were talking to a “real robot” (an autonomous robot) (Duffy & Zawieska, 2012). 

The negative response we received regarding the unclarity on the robot’s functioning made it clear to us that if this pilot were extended, it is highly important to be more transparent. It is possible to hold suspension of disbelief and be honest of the robot’s operation simultaneously (we do all know that television shows are not reality, after all).

**“The robot was a bit simple in certain things, and sometimes talked meanly to people, and was condescending. This was a bit anxiety inducing… Was this intentional?”**

Some players felt that the robot’s rude behaviour crossed the boundary into condescending. They wished that the robot would be more considerate in the future. This indicates that even a robot can hurt feelings. In future versions, making IQ_201 more empathic, and less focused on the superiority of robots over humans, could have positive results.

**“The robot looked a bit blue in the face, and its voice was a bit weird.”**

Two teenagers did not enjoy the robot’s appearance and voice. One remarked especially about its blue face, asking why we did not make it “normal colored”. 

This may have been due to the robot falling into the “uncanny valley” for these players. Uncanny valley is a theory developed by robotics researcher Masahiro Mori (Mori et al., 2012). His theory posits that as the appearance of a robot approaches human-likeness, there is a dip when the appearance gets very close. Zombies and corpses fall into this valley. 

To get rid of this effect with our robot, it could be wise to alter the robot’s appearance and voice in future solutions.

![Image](https://www.freecodecamp.org/news/content/images/2019/10/0_g5B15D6hFSmG0bbi.png)
_The Uncanny Valley by Masahiro Mori. Wikimedia commons._

#### And then the positive:

**“It was really interesting gaming with the robot. :) Hopefully in the future we can have this type of event again. :)”**

The majority of the teenagers enjoyed playing with the robot, and watching the stream. Their feedback complimented the robot’s sense of humour, and its playing skills. A continuation of the pilot would surely find an interested audience.

**[to the robot] “Some people have trouble with new things. In this case, these players are having trouble with a robot, since you’re new.”**

This player consoled the robot in-game, as other players were giving it a hard time by continuously killing it. This comment was moving: the player felt bad for the robot, and thought the robot might feel bad as well, attempting to change that. This is a clear empathic response toward the robot.

**[to the robot] “I will miss you robot!”**

A few players gave the robot heartfelt goodbyes when it left Minecraft. These players found the robot approachable, and even formed an emotional bond with it. This means we succeeded in creating a compelling character, even during what was only a 6 hour stream. 

For future builds of the robot, the players should be informed how the robot operates. This could help them calibrate an appropriate level of emotional bond to the robot.

## Are Robotic Influencers Our Future?

Players took an active interest in the robot. They approached it, interacted with it, and formed opinions on it. The robot also provoked emotional reactions — both positive and negative. Some participants really loved the robot and wished for more interaction in the future, and some were heavily critical. 

This indicates that robot influencers have the capacity to affect our emotions — whether this capacity will ever reach the level of human entertainers, I do not know. Whether that is desirable, I also do not know.

What positively surprised me was that the young user base of the robot were media literate: they critically examined the robot’s mode of operation. The players had a good idea of what is possible with AI today, and what is not. They were not easily duped.

This makes me hopeful for our future, whether it contains robotic entertainers or not. When viewers remain critical, they can understand that robots are machines with no actual emotional capacity, even if viewers do choose to suspend disbelief. 

Interacting with the robot can be though of as a form of [parasocial interaction](https://en.wikipedia.org/wiki/Parasocial_interaction) for the viewer — where the viewer may feel that their relationship with the robot is close — even though it is not truly reciprocal. This in itself is not necessarily harmful, as long as we are honest about what the relationship truly is. We should understand that robots are putting on a performance to elicit emotions in us — like human entertainers do

[**A video about the project.**](https://areena.yle.fi/1-50168989?source=post_page-----702735f678a8----------------------)

First published on [Towards Data Science.](https://towardsdatascience.com/the-robotic-influencers-of-our-future-a-minecraft-playing-twitch-streaming-robot-702735f678a8)

---

_Duffy, B. R., & Zawieska, K. (2012, September). Suspension of disbelief in social robotics. In 2012 IEEE RO-MAN: The 21st IEEE International Symposium on Robot and Human Interactive Communication (pp. 484–489). IEEE._

_Mori, M., MacDorman, K. F., & Kageki, N. (2012). The uncanny valley: The original essay by Masahiro Mori. IEEE Spectrum, 98–100._

