from memory_game import display, button_a, button_b, sleep, running_time, Image
import random

# ── CONFIG ────────────────────────────────────────────────────────────────────
INITIAL_ROWS     = [1, 2]      # Dino’s normal lanes (rows 2 & 3)
UP_ROWS          = [0, 1]      # Jump lanes  (rows 1 & 2)
DOWN_ROWS        = [2, 3]      # Duck lanes  (rows 3 & 4)
JUMP_DURATION    = 500         # ms to stay in a jump/duck
FRAME_DELAY      = 150         # ms per frame
SPAWN_MIN_FRAMES = 10          # min frames between cacti
SPAWN_MAX_FRAMES = 20          # max frames between cacti
# ─────────────────────────────────────────────────────────────────────────────

def play_game():
    state = "normal"          # "normal" | "up" | "down"
    state_start = 0
    obstacles = []            # list of [x, row]
    next_spawn = random.randint(SPAWN_MIN_FRAMES, SPAWN_MAX_FRAMES)
    score = 0

    while True:
        now = running_time()
        # auto-return to normal after jump/duck
        if state != "normal" and now - state_start >= JUMP_DURATION:
            state = "normal"

        # input: A=jump up, B=duck down
        if button_a.was_pressed() and state == "normal":
            state = "up"
            state_start = now
        if button_b.was_pressed() and state == "normal":
            state = "down"
            state_start = now

        # spawn new cactus
        next_spawn -= 1
        if next_spawn <= 0:
            obstacles.append([4, random.choice(INITIAL_ROWS)])
            next_spawn = random.randint(SPAWN_MIN_FRAMES, SPAWN_MAX_FRAMES)

        # move & cull
        for obs in obstacles:
            obs[0] -= 1
        obstacles = [obs for obs in obstacles if obs[0] >= 0]

        # update score
        score += 1

        # draw frame
        display.clear()
        if state == "up":
            dino_rows = UP_ROWS
        elif state == "down":
            dino_rows = DOWN_ROWS
        else:
            dino_rows = INITIAL_ROWS

        # draw dino
        for y in dino_rows:
            display.set_pixel(0, y, 9)
        # draw cacti
        for x, y in obstacles:
            display.set_pixel(x, y, 5)

        # collision?
        for x, y in obstacles:
            if x == 0 and y in dino_rows:
                return score

        sleep(FRAME_DELAY)


# ── MAIN LOOP ─────────────────────────────────────────────────────────────────
while True:
    sc = play_game()

    # game over
    display.clear()
    display.scroll("Game Over")
    display.scroll("Score:" + str(sc))
    display.show(Image.SAD)

    # A=restart, B=quit
    display.scroll("A=Restart  B=Quit")
    while True:
        if button_a.was_pressed():
            break   # restart
        if button_b.was_pressed():
            display.clear()
            while True:
                sleep(1000)