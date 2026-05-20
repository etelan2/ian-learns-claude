import json
import os
from collections import Counter

def analyze(enemy_name=None):
    data_file = os.path.expanduser("~/ian-learns-claude/projects/r6-analyst/data/matches.json")

    if not os.path.exists(data_file) or os.path.getsize(data_file) == 0:
        print("No data yet. Log some enemies first.")
        return

    with open(data_file) as f:
        data = json.load(f)

    if enemy_name:
        data = [e for e in data if e["enemy"].lower() == enemy_name.lower()]

    if not data:
        print(f"No entries found for '{enemy_name}'.")
        return

    print(f"\n--- Analysis ({len(data)} entries) ---")

    playstyles = Counter(e["playstyle"] for e in data)
    print("\nPlaystyle breakdown:")
    for style, count in playstyles.most_common():
        print(f"  {style}: {count}x")

    weapons = Counter(e["weapon"] for e in data)
    print("\nWeapons used:")
    for weapon, count in weapons.most_common():
        print(f"  {weapon}: {count}x")

    breakable = sum(1 for e in data if e["breakable_wall"])
    print(f"\nBreakable wall behind them: {breakable}/{len(data)} times")

    maps = Counter(e["map"] for e in data)
    print("\nMaps played:")
    for map_name, count in maps.most_common():
        print(f"  {map_name}: {count}x")

if __name__ == "__main__":
    name = input("Analyze which enemy? (leave blank for all): ").strip()
    analyze(name if name else None)
