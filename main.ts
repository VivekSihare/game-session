// Every 3 seconds
// --- Collision: Player hits bomb ---
sprites.onOverlap(SpriteKind.Player, SpriteKind.Enemy, function (sprite2, other2) {
    info.changeLifeBy(-1)
    other2.destroy(effects.fire, 200)
    music.wawawawaa.play()
})
// --- Reset Button ---
controller.B.onEvent(ControllerButtonEvent.Pressed, function () {
    info.setLife(3)
    info.setScore(0)
    info.startCountdown(30)
    player1.setPosition(80, 60)
    game.splash("Game Reset! Try again!")
})
// 30 seconds game
info.onCountdownEnd(function () {
    game.splash("Time's up! Well done!")
    game.over(true, effects.confetti)
})
// --- Pause Menu Button ---
controller.menu.onEvent(ControllerButtonEvent.Pressed, function () {
    game.showLongText("Game paused. Press A to continue!", DialogLayout.Center)
})
// --- Game Over Events ---
info.onLifeZero(function () {
    game.splash("Oh no! You lost all lives!")
    game.over(false, effects.melt)
})
// Every 2 seconds
// --- Collision: Player collects apple ---
sprites.onOverlap(SpriteKind.Player, SpriteKind.Food, function (sprite, other) {
    info.changeScoreBy(1)
    other.destroy(effects.confetti, 200)
    music.baDing.play()
})
let bomb: Sprite = null
let apple: Sprite = null
let player1: Sprite = null
// --- Show Prompt at Start ---
game.showLongText("Welcome! Collect apples and avoid the bombs!", DialogLayout.Center)
// --- Setup Player ---
player1 = sprites.create(img`
    . . f f f f . . 
    . f 2 2 2 2 f . 
    f 2 f f f f 2 f 
    f 2 f . . f 2 f 
    f 2 f f f f 2 f 
    . f 2 2 2 2 f . 
    . . f f f f . . 
    `, SpriteKind.Player)
player1.setPosition(80, 60)
controller.moveSprite(player1, 100, 0)
// Only horizontal movement
// --- Setup Game Info ---
info.setLife(3)
info.setScore(0)
// --- Countdown Timer Game Over ---
info.startCountdown(30)
// --- Spawn Apples (Collectibles) ---
game.onUpdateInterval(2000, function () {
    apple = sprites.create(img`
        . . 5 . . 
        . 5 5 5 . 
        5 5 5 5 5 
        . 5 5 5 . 
        . . 5 . . 
        `, SpriteKind.Food)
    apple.setPosition(randint(10, 150), 0)
    apple.setVelocity(0, 50)
    apple.setFlag(SpriteFlag.AutoDestroy, true)
})
// --- Spawn Bombs (Obstacles) ---
game.onUpdateInterval(3000, function () {
    bomb = sprites.create(img`
        . . 8 . . 
        . 8 8 8 . 
        8 8 8 8 8 
        . 8 8 8 . 
        . . 8 . . 
        `, SpriteKind.Enemy)
    bomb.setPosition(randint(10, 150), 0)
    bomb.setVelocity(0, 70)
    bomb.setFlag(SpriteFlag.AutoDestroy, true)
})
