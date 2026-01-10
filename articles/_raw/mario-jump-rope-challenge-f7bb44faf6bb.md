---
title: MacGyvering the Mario Odyssey Jump-Rope Challenge
subtitle: ''
author: freeCodeCamp
co_authors: []
series: null
date: '2017-11-27T07:18:28.000Z'
originalURL: https://freecodecamp.org/news/mario-jump-rope-challenge-f7bb44faf6bb
coverImage: https://cdn-media-1.freecodecamp.org/images/1*Gch8CVKbhZiqMqD0ZgB6OA.jpeg
tags:
- name: arduino
  slug: arduino
- name: gaming
  slug: gaming
- name: nintendo
  slug: nintendo
- name: General Programming
  slug: programming
- name: technology
  slug: technology
seo_title: null
seo_desc: 'By Antin Harasymiv

  Super Mario Odyssey is quite possibly my favorite Mario game. So much so that I
  went out of my way to complete every last challenge. But one of them gave me more
  trouble than all the others combined: Jump-Rope Genius in the Metro K...'
---

By Antin Harasymiv

[Super Mario Odyssey](https://www.nintendo.com/games/detail/super-mario-odyssey-switch) is quite possibly my favorite Mario game. So much so that I went out of my way to complete every last challenge. But one of them gave me more trouble than all the others combined: _Jump-Rope Genius_ in the Metro Kingdom.

You don’t even need to move. You just need to successfully jump 100 times in succession. But the trick is every five jumps it speeds up until 50, until you’re jumping almost twice a second. Press jump too early and you fail. Press jump too late and you fail. Press jump for too long and… you guessed it, you fail.

After a few dozen or so failed attempts I started joking that I’d just build something to beat it for me… and as the days went by and I still hadn’t finished the challenge my joking turned more serious and I started wondering how to do it.

My first thought was to simply program an Arduino to bridge the connectors for the jump button on a Switch controller, but thankfully I checked the [iFixit teardown](https://www.ifixit.com/Teardown/Nintendo+Switch+Teardown/78263#s156437) first because Nintendo controllers since the Wii use dome switches instead of the conductive rubber pads, which makes that impossible (for some fun reading see the [evolution](https://www.fictiv.com/blog/posts/nintendo-controller-teardown-part-1) of Nintendo controllers over the years).

![Image](https://cdn-media-1.freecodecamp.org/images/1*s7mqVpMJHtFRFflTAETHTQ.jpeg)
_Switch Joy-Con controller_

I was mentally tossing up between buying an older GameCube controller (with adapter) which would be easy to hack, or using a solenoid to physically press a button on a Switch controller, both seemed like viable solutions, but after getting outbid on the first few GameCube controllers selling on eBay I settled on the solenoid route.

After completing 835 of the 836 unique challenges in Mario, I turned all my attention back to the final moon. In order to program something to beat it, first I’d need to measure the timing, so my intention was to record the screen and then count the frames. Before setting up a camera I put a few practice rounds in, and much to my horror, I actually beat the thing legitimately.

![Image](https://cdn-media-1.freecodecamp.org/images/1*oIzx9GmxYY57vJfq0Ewwyw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*kgB2EcsqurjlAm4Ni9DmLQ.jpeg)

Having spent two weeks telling everyone I knew that I was going to program something to beat it (and having most of them scoff) losing the excuse to do so was pretty disappointing.

However being an adult, I realized that I didn’t really need an excuse to waste my time and money (that’s pretty much all we do), so express ordered an Arduino and the necessary components to start my project.

![Image](https://cdn-media-1.freecodecamp.org/images/1*0shSlQ9GLpAK7fVEDPt5Pw.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*JFaR8nH_b25ZIcFEt7w0WA.jpeg)

The first step was to figure out how to use an Arduino, which… was pretty straight forward actually, the online editor and tutorials are super easy, and after programming a few flashing LEDs I felt ready to go. The biggest hurdle was actually finding a USB-B cable because honestly who still uses those?

The second step was to figure out the timing, and I made it impressively difficult for myself. I thought I was being clever by recording from the overhead view, and could use the woman’s foot to align frames, when _her hand touched her foot_ I’d call that a revolution, and I painstakingly went through QuickTime pressing the arrow keys to step a frame at a time and counting _one, two, three… sixty-eight, sixty-nine, seventy_.

![Image](https://cdn-media-1.freecodecamp.org/images/1*78Sfthm-0pj58nvXBZwiIw.png)
_The middle frame shows her hand aligned with foot_

The second and a half step was to realize the jump count was a more reliable measure, and that Final Cut Pro would show me the time and frame count, allowing me to really quickly scrub through the video.

![Image](https://cdn-media-1.freecodecamp.org/images/1*LkMIRmBft5rUN-yusYEV4g.png)
_Final Cut Pro_

Do this 50 times… and put all the results into a spreadsheet and you have the secret to Jump-Rope success. Those last 50 jumps? You need to do one every 0.58 seconds.

![Image](https://cdn-media-1.freecodecamp.org/images/1*PB9TdFtO9Ynh6KDxs479HA.png)
_Measured timings for Mario Jump-Rope challenge_

With timings completed I turned my attention to the electronic half of the problem, and fortunately someone who understands electronics (I definitely do not) had already [shared](https://core-electronics.com.au/tutorials/solenoid-control-with-arduino.html) how to control a solenoid with an Arduino.

For those who don’t know, a solenoid is really just a cylindrical coil of wire which when you run a current through produces a magnetic field. The name is interchangeable with a few things that use solenoids (the coil part) to do something more complex, in this case push a small metal rod. Turn on the power and the rod pushes out, turn it off and the spring moves it back.

![Image](https://cdn-media-1.freecodecamp.org/images/1*Pr51iD0DzPoSdwbPF8OIJQ.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*EjyP9Ed764JVtIijnU53Hw.png)
_Completed circuit_

I wired up a circuit with a simple switch and solenoid, and wrote a program that would loop through and trigger it, progressively shortening the timing as it progressed. Flipping the switch would start the loop, turning it off would reset.

This would enable me to manually run Mario into position and flip the switch to start, and also give me an easy way to retry if I messed up (which I anticipated would be often). After a few hours (and some tips from my brother) I had a working circuit!

At this point I’d basically assumed success, and then reality kicked in (or rather, kicked me). In my naiveté I’d assumed the solenoid would be able to trivially depress a Switch button, the one I [bought](https://www.adafruit.com/product/2776) was a 5V solenoid able to move 3mm and apply 80 grams of force, that seemed like a lot (it’s actually less than a single newton).

I held it against the controller and… nothing. No movement, the button refused the budge. Googling for how much force is needed to press a Switch controller yielded no results, and around my house I had no good tools to measure it with.

So, with no good tools, I went looking for some bad ones.

What about cooking measures? I filled 1/3 of a cup with water and balanced that above a button, no movement. I filled 1/2 of a cup with water and it depressed. So there’s your answer, a Joy-Con button needs somewhere between a third and half a cup of water.

Turning those back into real units, 1 cup = 250 ml and the easy thing about the metric system is that weight is derived from the volume of water. 250 ml is 250 grams, so my Joy-Con needed somewhere between 83 grams and 125 grams to depress.

Suddenly my 80 gram solenoid didn’t seem so underpowered, what if I… overpowered it? I was giving it the 5 volts it asked for, but I had a 9 volt power supply. The magnetic force of a solenoid increases with the voltage (actually it goes up with the square of the voltage) so at 9 volts my solenoid should be applying closer to 250 grams, or as I like to think about it, 1 cup of water!

Step four involved attaching the solenoid to the controller. Given how little thought I had put into planning this part, it was no surprise how inelegant the solution turned out. A few pieces of wood raised it over the other buttons, a few pieces of electrical tape held the wood in place, and a rubber band kept the solenoid in position.

![Image](https://cdn-media-1.freecodecamp.org/images/1*mLSWqLee2C3Zc0Y8X6nwtg.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*L854swGhbWdtOrJPuTAXog.jpeg)

![Image](https://cdn-media-1.freecodecamp.org/images/1*Gch8CVKbhZiqMqD0ZgB6OA.jpeg)

I was finally ready to put it all to the test, I warped to the Metro Kingdom, ran up to the challenge, and prepared myself to bask in the sweet glory of my smug success.

And almost immediately failed… My timing was wrong. I manually tweaked a few of the timings in my code and got Mario closer, closer again, and closer still, until he could pretty reliably get to 86.

At that point instead of randomly tweaking things I recorded it playing and returned to Final Cut Pro to recount frames (this time focusing on how many frames nearer/further the rope was getting per 5 jump segment), and while I was a little off in a few places, as Mario was always getting to 50 the only thing requiring changing was the 50+ timing. I reduced it to a jump every 35.2 frames and tried again.

Success! 261 jumps. This felt like a huge victory, you can see in the video it easily trounced my meagre human effort of 102 jumps. I immediately went and woke my wife and tried to explain how cool it was, and when that failed to get me much adulation, resorted to telling my brother who was much more suitably impressed.

However, it’s a robot, why should 261 be a limit? Why can’t it be perfect? I analyzed the frames again and noticed the rope was catching up to Mario ever so slowly, he needed to go faster!

![Image](https://cdn-media-1.freecodecamp.org/images/1*sFulRlhZB9oPR4iLwzD8vQ.png)
_Jump timings, average was measured, actual is what is in code_

Reducing the timing from a jump every 35.2 frames to one every 35.15 frames (a change of just 0.14%) resulted in a much more successful Mario.

So successful that it was able to play the infuriating Mario Jump-Rope challenge for 35 minutes and 21 seconds before failing… setting a new high score (for me) of 3613.

At first I assumed it failed because my timing was still imperceptibly out, but upon closer inspection of the video it stayed perfectly in sync until it… long pressed! What a human mistake for a computer to make, instead of doing a short quick jump it held the button too long and sent Mario too high, he jumped at the right time but landed late.

In actuality I think it was that the poor solenoid was overheating, earlier in the night while I was playing with timings it had stopped running as well, I think driving it at almost twice the voltage was problematic. In the video you can even see that it pressed a second time during the jump at the correct timing.

As for the code? That was the simplest part. A mere 76 lines of code can play Mario better than me

![Image](https://cdn-media-1.freecodecamp.org/images/1*qxpqBkhYlTgMUgbiAkDihg.png)

For simplicities sake I measured all timings in how many frames between jumps, I could count the frames easily in the video, and then just divide by 60 to turn that into seconds.

The code calculates everything using dead reckoning from the time the challenge started, I assumed imprecisions in triggering any single jump would average out. Every loop the code calculates how many milliseconds should have elapsed before the next jump and if that threshold is met turns on the solenoid; there is a short duration that it keeps the solenoid on before resetting (maybe it needed to be shorter to avoid the long-press).

And that’s it… almost stupidly simple, fittingly so, given the nature of the jumping challenge.

I could try again but at almost 40 minutes per attempt I’m just not interested enough. Also, I’ve since discovered that [someone](https://www.youtube.com/watch?v=hu3HEwc6Pwk) went one step better than me, although in a slightly different direction.

Instead of physically pressing a button on their controller they use a library to simulate being a controller enabling them to trivially send signals. When they ran into the same timing challenge as me (only getting a few hundred jumps before failing — they were using the constant 35.18 for their final jumps) they solved that by programmatically monitoring to the video signal, checking the score region and when it changes do another jump. With this method they can reach the max score of 99,999!

You’d think with all of this that I’d have one of the highest scores in the game… you’d be wrong! Only a week ago I’d probably be in the top 100, but a bug has been discovered in the game that enables anyone to glitch this challenge, for almost no effort you can get unlimited jumps and over 10,000 people have now done so. Maybe if Nintendo patch this and reset the score board I’ll dust my solenoid off again, I feel if you can build something to play the game using only the controller itself then that’s kinda legitimate.

