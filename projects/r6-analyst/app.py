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
    body { background: #1a1a2e; color: #eee; font-family: monospace; max-width: 750px; margin: 40px auto; padding: 20px; }
    h1 { color: #e94560; }
    input, select { background: #16213e; color: #eee; border: 1px solid #e94560; padding: 8px; width: 100%; margin: 6px 0; box-sizing: border-box; }
    button { background: #e94560; color: white; border: none; padding: 10px 20px; cursor: pointer; font-size: 14px; margin-top: 6px; }
    button.danger { background: #8b0000; }
    button.secondary { background: #0f3460; }
    .entry { background: #16213e; padding: 10px; margin: 8px 0; border-left: 3px solid #e94560; display: flex; align-items: flex-start; gap: 10px; }
    .entry-content { flex: 1; }
    .stat { margin: 4px 0; }
    .entry-label { font-size: 12px; color: #aaa; }
    input[type="checkbox"] { width: auto; margin-top: 3px; accent-color: #e94560; }
    .tabs { display: flex; gap: 4px; margin-bottom: 20px; }
    .tab { padding: 10px 20px; cursor: pointer; background: #16213e; color: #aaa; border: none; font-family: monospace; font-size: 14px; }
    .tab.active { background: #e94560; color: white; }
    .page { display: none; }
    .page.active { display: block; }
    .player-card { background: #16213e; padding: 12px; margin: 8px 0; border-left: 3px solid #e94560; cursor: pointer; display: flex; justify-content: space-between; align-items: center; }
    .player-card:hover { border-left-color: #fff; }
    .badge { background: #e94560; color: white; padding: 2px 8px; font-size: 12px; }
    .analysis-box { background: #16213e; padding: 12px; margin: 8px 0; border-left: 3px solid #0f3460; }
  </style>
</head>
<body>
  <h1>R6 Analyst</h1>

  <div class="tabs">
    <button class="tab active" onclick="showTab(event,'log')">Log Enemy</button>
    <button class="tab" onclick="showTab(event,'files')">Files</button>
    <button class="tab" onclick="showTab(event,'analysis')">Analysis</button>
  </div>

  <!-- LOG TAB -->
  <div id="tab-log" class="page active">
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
      <button type="submit" style="width:100%">Save Entry</button>
    </form>
    <div id="msg"></div>
  </div>

  <!-- FILES TAB -->
  <div id="tab-files" class="page">
    <p style="color:#aaa">Click a player to analyze them. Check boxes to delete.</p>
    <button class="danger" onclick="deleteSelected()" style="width:100%;margin-bottom:10px">Delete Selected</button>
    <div id="playerList"></div>
  </div>

  <!-- ANALYSIS TAB -->
  <div id="tab-analysis" class="page">
    <p id="analysisBanner" style="color:#e94560;font-weight:bold"></p>
    <input id="filterName" placeholder="Filter by enemy name (leave blank for all)">
    <button onclick="loadAnalysis()" style="width:100%">Analyze</button>
    <div id="analysis"></div>
  </div>

  <script type="text/javascript">
    function showTab(e, name) {
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.getElementById('tab-' + name).classList.add('active');
      e.target.classList.add('active');
      if (name === 'files') loadPlayerList();
      if (name === 'analysis') loadAnalysis();
    }

    document.getElementById('logForm').onsubmit = async (e) => {
      e.preventDefault();
      const data = Object.fromEntries(new FormData(e.target));
      const res = await fetch('/log', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(data)});
      const r = await res.json();
      document.getElementById('msg').innerText = r.message;
      e.target.reset();
    };

    async function loadPlayerList() {
      const res = await fetch('/entries');
      const data = await res.json();
      if (data.length === 0) { document.getElementById('playerList').innerHTML = '<p>No entries yet.</p>'; return; }
      let html = '';
      data.forEach((e, i) => {
        html += '<div class="entry">';
        html += '<input type="checkbox" class="entry-check" value="' + i + '">';
        html += `<div class="entry-content" onclick="analyzePlayer('${e.enemy}')" style="cursor:pointer;flex:1">`;
        html += '<div><b>' + e.enemy + '</b> — ' + e.map + ' (Floor ' + e.floor + ')</div>';
        html += '<div class="entry-label">Weapon: ' + e.weapon + ' | Style: ' + e.playstyle + ' | Breakable: ' + (e.breakable_wall ? 'Yes' : 'No') + '</div>';
        html += '<div class="entry-label" style="color:#e94560">Click to analyze →</div>';
        html += '</div></div>';
      });
      document.getElementById('playerList').innerHTML = html;
    }

    function analyzePlayer(name) {
      document.getElementById('filterName').value = name;
      document.getElementById('analysisBanner').innerText = 'Analyzing: ' + name;
      document.querySelectorAll('.tab').forEach(t => t.classList.remove('active'));
      document.querySelectorAll('.page').forEach(p => p.classList.remove('active'));
      document.getElementById('tab-analysis').classList.add('active');
      document.querySelectorAll('.tab')[2].classList.add('active');
      loadAnalysis();
    }

    async function deleteSelected() {
      const selected = [...document.querySelectorAll('.entry-check:checked')].map(cb => parseInt(cb.value));
      if (selected.length === 0) { alert('Select at least one entry.'); return; }
      if (!confirm('Delete ' + selected.length + ' entry/entries?')) return;
      await fetch('/delete', {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify({indexes: selected})});
      loadPlayerList();
    }

    async function loadAnalysis() {
      const name = document.getElementById('filterName').value;
      const res = await fetch('/analyze?enemy=' + encodeURIComponent(name));
      const data = await res.json();
      if (data.error) { document.getElementById('analysis').innerHTML = '<p>' + data.error + '</p>'; return; }
      let html = '<p><b>' + data.count + ' entries</b></p>';
      html += '<div class="analysis-box"><b>Playstyle:</b>' + Object.entries(data.playstyles).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      html += '<div class="analysis-box"><b>Weapons:</b>' + Object.entries(data.weapons).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      html += '<div class="analysis-box"><b>Breakable wall behind them:</b> ' + data.breakable + '/' + data.count + ' times</div>';
      html += '<div class="analysis-box"><b>Maps:</b>' + Object.entries(data.maps).map(([k,v]) => '<div class="stat">' + k + ': ' + v + 'x</div>').join('') + '</div>';
      document.getElementById('analysis').innerHTML = html;
    }
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

@app.route("/entries")
def entries():
    return jsonify(load_data())

@app.route("/delete", methods=["POST"])
def delete():
    indexes = set(request.json.get("indexes", []))
    data = load_data()
    data = [e for i, e in enumerate(data) if i not in indexes]
    save_data(data)
    return jsonify({"message": "Deleted."})

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
