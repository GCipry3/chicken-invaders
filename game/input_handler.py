from PySide6.QtCore import Qt

class InputHandler:
    def __init__(self, player):
        self.player = player
        self.key_states = {
            Qt.Key_Left: False,
            Qt.Key_Right: False,
            Qt.Key_Space: False
        }

    def update(self):
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
        if key in self.key_states:
            self.key_states[key] = is_pressed
