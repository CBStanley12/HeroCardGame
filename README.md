# HeroCardGame
Class project to create a simple card game

Goal:
Be the first player to empty their hand.

Setup:
Remove the two of Spades and place it faceup between the two players. This becomes the play pile. Dealer Shuffles the deck and alternately deals both players five cards facedown. The cards that are left become the draw pile. The draw pile is set facedown beside the play pile.

Gameplay:
Non-dealer goes first. Place a card of equal or higher value from their own hand faceup on the two of Spades. This new card is now the top card. Dealer places a card of equal or higher value from their own hand faceup on the top card. If a player cannot play, then that player draws cards from the top of the draw pile until they have five cards in their hand and play passes to the other player.
If both players have five cards in their hands and neither player can play, then a 'Hero' is drawn from the top of the draw pile and placed faceup on the play pile. Heros are drawn until at least one player can play. If both players can play, then the one with the lowest playable card plays first. In case of a draw between the players, another hero is drawn.
Play continues until a player manages to play all five cards without having to draw from the draw pile. This may occur quickly or it may take most of the deck.
If the draw pile is empty and neither player can play, then the game is declared a draw.
