🍏 Apple Catch Game – Step-by-Step Guide

⭐ GOAL

- ➡ Move your player
- ➡ Catch apples 🍎
- ➡ Avoid bombs 💣
- ⏱ Stay alive for 30 seconds!

✳️ STEP 1 – Start a New Game

- 1️⃣ Go to arcade.makecode.com
- 2️⃣ Click New Project
- 3️⃣ Name it Apple Catch Game

✳️ STEP 2 – Show a Welcome Message

- Go to Game drawer
- Drag show long text block
- Write: ➤ "Welcome! Catch apples and avoid bombs!"
- Pick CENTER layout
- ✔ This shows the message before game starts

✳️ STEP 3 – Make Your Player

- Go to Sprites
- Drag set mySprite to sprite of…
- Draw a character
- Change its kind to Player
- Place it in the middle:
- set x to 80
- set y to 60

✳️ STEP 4 – Make Player Move

- Grab controller move sprite block
- Connect it under your player block
- Set vx = 100 and vy = 0 (only left/right)
- ✔ Now you can move using arrow keys
- Add Bounce on wall for player kind

✳️ STEP 5 – Add Score and Lives

- Go to Info drawer
- Drag:
- ✔ set life to 3
- ✔ set score to 0

✳️ STEP 6 – Add Countdown Timer

- Go to Info
- Drag:
- ⏱ start countdown 30 seconds
- ✔ This ends the game after 30 seconds

✳️ STEP 7 – Drop Apples Every 2 Seconds 🍎

- Go to Game drawer
- Use on update every 2000 ms
- Inside it, create a sprite 🍎
- Set sprite kind → Food
- Set:
- x = random 10 to 150
- y = 0
- velocity y = 50
- auto destroy = on

✳️ STEP 8 – Drop Bombs Every 3 Seconds 💣

- Repeat the SAME steps
- BUT:
- 🍎 = food
- 💣 = enemy
- Velocity = 70 (faster)

✳️ STEP 9 – Collecting Apples

- Go to Sprites
- Use:
- ➡ On player overlaps food
- Inside:
- ✔ change score by 1
- ✔ Play ding sound
- ✔ Destroy apple

✳️ STEP 10 – Hitting Bombs

- Use:
- ➡ On player overlaps enemy
- Inside:
- ❌ change life by -1
- 🔥 Destroy bomb with fire effect
- 🥺 Play sad sound

✳️ STEP 11 – When Lives Become 0 ❤️

- Go to Info
- Use:
- ➡ on life zero
- Inside:
- 🚫 game over (lose)
- 🎭 Pick melt effect
- 📢 Add a splash message

✳️ STEP 12 – When Countdown Ends ⏱

- Use:
- ➡ on countdown end
- Inside:
- 🎉 game over (win)
- ✨ confetti effect
- 📢 “Time’s up!” message

✳️ STEP 13 – Add RESET Button (B)

- Use:
- ➡ on button B pressed
- Inside:
- 🔄 set life to 3
- 🔄 set score to 0
- 🔄 restart countdown
- ↩ move player to center
- 🎉 show splash “Game Reset!”

✳️ STEP 14 – Add PAUSE Button (MENU)

- Use:
- ➡ on menu button pressed
- Inside:
- 📢 show long text
- “Game paused. Press A to continue”
