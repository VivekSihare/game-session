# --- Reset Button ---

def on_b_pressed():
    info.set_life(3)
    info.set_score(0)
    info.start_countdown(30)
    player1.set_position(80, 60)
    game.splash("Game Reset! Try again!")
controller.B.on_event(ControllerButtonEvent.PRESSED, on_b_pressed)

# 30 seconds game

def on_countdown_end():
    game.splash("Time's up! Well done!")
    game.over(True, effects.confetti)
info.on_countdown_end(on_countdown_end)

# --- Pause Menu Button ---

def on_menu_pressed():
    game.show_long_text("Game paused. Press A to continue!", DialogLayout.CENTER)
controller.menu.on_event(ControllerButtonEvent.PRESSED, on_menu_pressed)

# --- Game Over Events ---

def on_life_zero():
    game.splash("Oh no! You lost all lives!")
    game.over(False, effects.melt)
info.on_life_zero(on_life_zero)

# Every 2 seconds
# --- Collision: Player collects apple ---

def on_on_overlap(sprite, other):
    info.change_score_by(1)
    other.destroy(effects.confetti, 200)
    music.ba_ding.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

# Every 3 seconds
# --- Collision: Player hits bomb ---

def on_on_overlap2(sprite2, other2):
    info.change_life_by(-1)
    other2.destroy(effects.fire, 200)
    music.wawawawaa.play()
sprites.on_overlap(SpriteKind.player, SpriteKind.enemy, on_on_overlap2)

bomb: Sprite = None
apple: Sprite = None
player1: Sprite = None
# --- Show Prompt at Start ---
game.show_long_text("Welcome! Collect apples and avoid the bombs!",
    DialogLayout.CENTER)
# --- Setup Player ---
player1 = sprites.create(img("""
        . . f f f f . .
        . f 2 2 2 2 f .
        f 2 f f f f 2 f
        f 2 f . . f 2 f
        f 2 f f f f 2 f
        . f 2 2 2 2 f .
        . . f f f f . .
        """),
    SpriteKind.player)
player1.set_position(80, 60)
controller.move_sprite(player1, 100, 0)
# Only horizontal movement
# --- Setup Game Info ---
info.set_life(3)
info.set_score(0)
# --- Countdown Timer Game Over ---
info.start_countdown(30)
# --- Spawn Apples (Collectibles) ---

def on_update_interval():
    global apple
    apple = sprites.create(img("""
            . . 5 . .
            . 5 5 5 .
            5 5 5 5 5
            . 5 5 5 .
            . . 5 . .
            """),
        SpriteKind.food)
    apple.set_position(randint(10, 150), 0)
    apple.set_velocity(0, 50)
    apple.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(2000, on_update_interval)

# --- Spawn Bombs (Obstacles) ---

def on_update_interval2():
    global bomb
    bomb = sprites.create(img("""
            . . 8 . .
            . 8 8 8 .
            8 8 8 8 8
            . 8 8 8 .
            . . 8 . .
            """),
        SpriteKind.enemy)
    bomb.set_position(randint(10, 150), 0)
    bomb.set_velocity(0, 70)
    bomb.set_flag(SpriteFlag.AUTO_DESTROY, True)
game.on_update_interval(3000, on_update_interval2)
