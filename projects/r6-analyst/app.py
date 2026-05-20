from flask import Flask, request, jsonify, render_template_string
import json
import os
from collections import Counter

app = Flask(__name__)

DATA_FILE = "data/matches.json"

def load_data():
    if os.path.exists(DATA_FILE) and os.path.getsize(DATA_FILE) > 0:
        with open(DATA_FILE) as f:
            return json.load(f)
    return []

def save_data(data):
    os.makedirs("data", exist_ok=True)
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=2)

HTML = """
<!DOCTYPE html>
<html>
<head>
  <title>R6 Analyst</title>
  <style>
    body { background: #1a1a2e; color: #eee; font-family: monospace; max-width: 700px; margin: 40px auto; padding: 20px; }
    h1 { color: #e94560; }
    h2 { color: #0f3460; background: #e94560; padding: 8px; }
    input, select { background: #16213e; color: #eee; border: 1px solid #e94560; padding: 8px; width: 100%; margin: 6px 0; box-sizing: border-box; }
    button { background: #e94560; color: white; border: none; padding: 10px 20px; cursor: pointer; width: 100%; font-size: 16px; margin-top: 10px; }
    .entry { background: #16213e; padding: 10px; margin: 8px 0; border-left: 3px solid #e94560; }
    .stat { margin: 4px 0; }
  </style>
</head>
<body>
  <h1>R6 Analyst</h1>

  <h2>Log Enemy</h2>
  <form id="logForm">
    <input name="map" placeholder="Map" required>
    <input name="enemy" placeholder="Enemy name" required>
    <input name="floor" placeholder="Floor">
    <input name="position" placeholder="Position (describe it)">
    <input name="weapon" placeholder="Weapon">
    <select name="playstyle">
      <option value="roam">Roam</option>
      <option value="camp-room">Camp room</option>
      <option value="camp-other">Camp other</option>
      <option value="roam-camp">Roam + camp</option>
    </select>
    <select name="breakable_wall">
      <option value="y">Breakable wall behind: YES</option>
      <option value="n">Breakable wall behind: NO</option>
    </select>
    <button type="submit">Save Entry</button>
  </form>
  <div id="msg"></div>

  <h2>Analysis</h2>
  <input id="filterName" placeholder="Filter by enemy name (leave blank for all)">
  <button onclick="loadAnalysis()">Analyze</button>
  <div id="analysis"></div>

  <script>
    document.getElementById('logForm').onsubmit = async (e) => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(e.target));
      const res = await fetch('/log', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data)});
      const r = await res.json();
      document.getElementById('msg').innerText = r.message;
      e.target.reset();
    };

    async function loadAnalysis() {
      const name = document.getElementById('filterName').value;
      const res = await fetch('/analyze?enemy=' + encodeURIComponent(name));
      const data = await res.json();
      if (data.error) { document.getElementById('analysis').innerHTML = '<p>' + data.error + '</p>'; return; }
      let html = '<p><b>' + data.count + ' entries</b></p>';
      html += '<div class="entry"><b>Playstyle:</b>' + Object.entries(data.playstyles).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      html += '<div class="entry"><b>Weapons:</b>' + Object.entries(data.weapons).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      html += '<div class="entry"><b>Breakable wall:</b> ' + data.breakable + '/' + data.count + ' times</div>';
      html += '<div class="entry"><b>Maps:</b>' + Object.entries(data.maps).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      document.getElementById('analysis').innerHTML = html;
    }
    loadAnalysis();
  </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML)

@app.route("/log", methods=["POST"])
def log():
    entry = request.json
    entry["breakable_wall"] = entry.get("breakable_wall") == "y"
    data = load_data()
    data.append(entry)
    save_data(data)
    return jsonify({"message": "Entry saved."})

@app.route("/analyze")
def analyze():
    enemy = request.args.get("enemy", "").strip()
    data = load_data()
    if enemy:
        data = [e for e in data if e["enemy"].lower() == enemy.lower()]
    if not data:
        return jsonify({"error": "No entries found."})
    return jsonify({
        "count": len(data),
        "playstyles": dict(Counter(e["playstyle"] for e in data).most_common()),
        "weapons": dict(Counter(e["weapon"] for e in data).most_common()),
        "breakable": sum(1 for e in data if e["breakable_wall"]),
        "maps": dict(Counter(e["map"] for e in data).most_common()),
    })

if __name__ == "__main__":
    app.run(debug=True)
