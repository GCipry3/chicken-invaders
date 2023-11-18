from PySide6.QtCore import Qt
from .player import Player

class InputHandler:
    """
    Handles input events and updates the player's actions accordingly.
    
    Attributes:
        player (Player): The player whose actions are updated.
    """

    def __init__(self, player: Player):
        self.player = player
        self.key_states = {
            Qt.Key_Left: False,
            Qt.Key_Right: False,
            Qt.Key_Space: False
        }

    def update(self):
        """
        Updates the player's actions based on the current key states.
        """
        if self.key_states[Qt.Key_Left]:
            self.player.start_moving_left()
        else:
            self.player.stop_moving_left()

        if self.key_states[Qt.Key_Right]:
            self.player.start_moving_right()
        else:
            self.player.stop_moving_right()

        if self.key_states[Qt.Key_Space]:
            self.player.shoot()

    def handle_key_event(self, key, is_pressed):
        """
        Handles a key event by updating the corresponding key state.
        """
        if key in self.key_states:
            self.key_states[key] = is_pressed
