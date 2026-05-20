import json
import os

def log_enemy():
    print("\n--- R6 Analyst: Log Enemy ---")
    map_name = input("Map: ")
    enemy_name = input("Enemy name: ")
    floor = input("Floor: ")
    position = input("Position (describe it): ")
    weapon = input("Weapon: ")
    playstyle = input("Playstyle (roam / camp-room / camp-other / roam-camp): ")
    breakable_wall = input("Breakable wall behind them? (y/n): ")

    entry = {
        "map": map_name,
        "enemy": enemy_name,
        "floor": floor,
        "position": position,
        "weapon": weapon,
        "playstyle": playstyle,
        "breakable_wall": breakable_wall == "y"
    }

    data_file = os.path.expanduser("~/ian-learns-claude/projects/r6-analyst/data/matches.json")

    if os.path.exists(data_file) and os.path.getsize(data_file) > 0:
        with open(data_file, "r") as f:
            data = json.load(f)
    else:
        data = []

    data.append(entry)

    with open(data_file, "w") as f:
        json.dump(data, f, indent=2)

    print("\nEntry saved.")

log_enemy()
