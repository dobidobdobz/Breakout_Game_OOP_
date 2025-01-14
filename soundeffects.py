import pygame


class Sound_effects():

    def __init__(self):
        super().__init__()
        # handles all the sound effects in the game
        pygame.mixer.init()

    def switch_music_on(self):
        # background music
        self.music = pygame.mixer.Sound("music_files/background_music.wav")
        self.music.set_volume(0.4)
        self.music.play(loops=-1, maxtime=0, fade_ms=0)  # Play looped music

    def switch_music_off(self):
        self.music.stop()

    def game_over(self):
        self.game_over_sound = pygame.mixer.Sound("music_files/game-over-arcade.wav")
        self.game_over_sound.set_volume(1)
        self.game_over_sound.play()

    def game_over_won(self):
        self.game_over_won = pygame.mixer.Sound("music_files/win-game.wav")
        self.game_over_won.set_volume(1)
        self.game_over_won.play()

    def block_bounce_sound_effect(self):
        self.block_bounce_sound = pygame.mixer.Sound("music_files/brick_bounce.wav")
        self.block_bounce_sound.set_volume(0.8)
        self.block_bounce_sound.play()

    def paddle_bounce_sound_effect(self):
        self.paddle_bounce_sound = pygame.mixer.Sound("music_files/paddle_hit.wav")
        self.paddle_bounce_sound.set_volume(0.4)
        self.paddle_bounce_sound.play()

    def wall_bounce_sound_effect(self):
        self.wall_bounce_sound = pygame.mixer.Sound("music_files/blast-wave.wav")
        self.wall_bounce_sound.set_volume(0.4)
        self.wall_bounce_sound.play()

    def reset_bleep_sound_effect(self):
        self.reset_sound = pygame.mixer.Sound("music_files/fail.wav")
        self.reset_sound.set_volume(0.4)
        self.reset_sound.play()
