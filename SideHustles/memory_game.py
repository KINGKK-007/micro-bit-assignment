from microbit import *
import random

def generate_path():
    """Generate a continuous random path from a random corner."""
    corners = [(0, 0), (4, 0), (0, 4), (4, 4)]
    start = random.choice(corners)
    path = [start]
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    # Build the path by adding adjacent neighbors
    while True:
        x, y = path[-1]
        neighbors = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if 0 <= nx <= 4 and 0 <= ny <= 4 and (nx, ny) not in path:
                neighbors.append((nx, ny))
        if not neighbors:
            break
        path.append(random.choice(neighbors))
        if len(path) >= 10:  # limit length
            break
    return path

def show_path(path, duration=10000):
    """Display the given path for duration (ms)."""
    display.clear()
    for (x, y) in path:
        display.set_pixel(x, y, 9)  # light up each LED in path
    sleep(duration)
    display.clear()

def run_game():
    """Play one round of the memory path game."""
    path = generate_path()
    start = path[0]
    show_path(path, duration=10000)
    # Prepare user input
    current = start
    user_path = [current]
    display.set_pixel(current[0], current[1], 9)
    last_A_time = 0
    last_B_time = 0
    waiting_A = False
    waiting_B = False

    while len(user_path) < len(path):
        now = running_time()
        # If A was pressed and timeout expired, move left
        if waiting_A and now - last_A_time >= 1000:
            x, y = current
            current = (max(x - 1, 0), y)
            display.clear(); display.set_pixel(current[0], current[1], 9)
            user_path.append(current)
            waiting_A = False
        # If B was pressed and timeout expired, move right
        if waiting_B and now - last_B_time >= 1000:
            x, y = current
            current = (min(x + 1, 4), y)
            display.clear(); display.set_pixel(current[0], current[1], 9)
            user_path.append(current)
            waiting_B = False

        # Detect button A press
        if button_a.is_pressed():
            while button_a.is_pressed():
                sleep(10)  # wait for release to avoid bouncing
            if waiting_A and (running_time() - last_A_time) < 1000:
                # Double A → move up
                x, y = current
                current = (x, max(y - 1, 0))
                display.clear(); display.set_pixel(current[0], current[1], 9)
                user_path.append(current)
                waiting_A = False
            else:
                # Single A (start waiting for possible double)
                last_A_time = running_time()
                waiting_A = True

        # Detect button B press
        if button_b.is_pressed():
            while button_b.is_pressed():
                sleep(10)
            if waiting_B and (running_time() - last_B_time) < 1000:
                # Double B → move down
                x, y = current
                current = (x, min(y + 1, 4))
                display.clear(); display.set_pixel(current[0], current[1], 9)
                user_path.append(current)
                waiting_B = False
            else:
                last_B_time = running_time()
                waiting_B = True

        # A+B pressed together quits game
        if button_a.is_pressed() and button_b.is_pressed():
            display.scroll("Goodbye")
            return False

        sleep(50)

    # Game finished: check win or lose
    if user_path == path:
        display.scroll("You won!")
    else:
        display.scroll("Failed")
    return True

# Main loop: shake to start, A+B to quit
while True:
    if accelerometer.was_gesture("shake"):
        cont = run_game()
        if not cont:
            break
    if button_a.is_pressed() and button_b.is_pressed():
        break
    sleep(100)