class GameState:

    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    WIN = "win"

    def __init__(self):

        self.current_state = self.MENU

    def change_state(self, state):

        self.current_state = state
