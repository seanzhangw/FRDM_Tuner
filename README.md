# Project Descriptions for Team ar929-kb593-sl2222

## ar929
Sent by other partner.## kb593
We would like to create either a multiplayer or single player game using either an LED strip or an LED panel. In terms of the game, we aren’t completely set on how we want the game to work, but we do want to implement concurrency and focus more on the hardware user interaction.

 

Option 1: Light Racing 

Prototype as a two-player game: One light signal travels randomly along the LED strip. After some starting signal, the two players each send out a light signal from one end of the LED strip via the sensor (the speed, color of the light is also dependent on the data obtained from sensor). The light signal will travel towards the other end. When light A hits the other light B when it has passed the random signal, we declare the winner to be the player that sends light A. We need to add constraints on the start time (otherwise you can do nothing to win the game).

We could add more components and gaming constraints to make this more complex. For example, we can use a laser to touch the sensor to start the light and then run to click a button on the board to stop it before reaching the end.

 

Option 2: Two-Person Light Control

For this option, we took inspiration from the whack-a-mole game and we will use an LED panel for which we randomly simulate LED light colors onto a position on the board at different speeds, depending on the level the players have reached (more difficult for each level). One person will have control of the light color and the other person will have control over the placement/position of the LED (which light on the panel is currently on and needs to be turned off). In order for the LED light to turn off the right color and position must be selected. In terms of how the light colors will be chosen by one player, we will use voice input (MEMS Microphone) for which color from ones we program into the game. As for choosing which position on the LED panel should be turned off, we are not completely sure about the method but our first idea is to use an infrared LED touch panel as a peripheral for players to actually touch the position of the LED that needs to be turned off. ## sl2222

# Feedback
# Project Web-Page

The project web-pages will also be hosted on github in this repo in the "page" branch. You can edit it by switching branches and modifying the files, or by pushing to the branch. Here is a link to a minmal web-page that you can edit and modify: [https://pages.github.coecis.cornell.edu/ece3140-sp2024/ar929-kb593-sl2222](https://pages.github.coecis.cornell.edu/ece3140-sp2024/ar929-kb593-sl2222)
