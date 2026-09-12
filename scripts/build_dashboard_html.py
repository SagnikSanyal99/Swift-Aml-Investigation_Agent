from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))

from src.dashboard import executive_figure, operations_figure, evidence_figure, validation_figure
from src.metrics import verified_kpi_frame

DASH = ROOT / "dashboard" / "index.html"

figures = {
    "executive": executive_figure(),
    "operations": operations_figure(),
    "evidence": evidence_figure(),
    "validation": validation_figure(),
}

cards = []
for _, row in verified_kpi_frame().query("KPI in ['ROC-AUC','PR-AUC','Payment edges','Account nodes','Selected investigations','Canonical evidence records','LLM successful investigations','Ground-truth contamination']").iterrows():
    value = row['Value']
    if isinstance(value, float) and value < 1:
        value = f"{value:.4f}"
    elif isinstance(value, (int, float)):
        value = f"{int(value):,}"
    cards.append(f'<div class="card"><div class="label">{row["KPI"]}</div><div class="value">{value}</div><div class="layer">{row["Layer"]}</div></div>')

plot_sections = []
for key, fig in figures.items():
    div = fig.to_html(full_html=False, include_plotlyjs=False, config={"displaylogo": False, "responsive": True})
    plot_sections.append(f'<section id="{key}" class="panel">{div}</section>')

html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Evidence-Grounded AML Investigation</title>
<script src="https://cdn.plot.ly/plotly-2.35.2.min.js"></script>
<style>
body{{font-family:Inter,Arial,sans-serif;margin:0;background:#f4f6f8;color:#182230}}
.header{{background:#111827;color:white;padding:38px 5vw}}
.header h1{{margin:0 0 8px;font-size:32px}}
.header p{{max-width:1050px;color:#d1d5db;line-height:1.55}}
.container{{max-width:1450px;margin:auto;padding:28px}}
.cards{{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin:0 0 24px}}
.card{{background:white;border-radius:14px;padding:18px;box-shadow:0 3px 12px rgba(0,0,0,.07)}}
.label{{font-size:12px;color:#687386}}
.value{{font-size:27px;font-weight:700;margin-top:8px}}
.layer{{font-size:11px;color:#9aa3b2;margin-top:7px}}
.tabs{{display:flex;flex-wrap:wrap;gap:8px;margin:10px 0 22px}}
button{{border:0;border-radius:9px;padding:10px 14px;background:#e5e7eb;cursor:pointer;font-weight:600}}
button.active{{background:#111827;color:#fff}}
.panel{{display:none;background:white;border-radius:14px;padding:10px;margin-bottom:20px;box-shadow:0 3px 12px rgba(0,0,0,.06)}}
.panel.active{{display:block}}
.disclosure{{background:#eef2ff;border-left:5px solid #6366f1;padding:16px;border-radius:8px;line-height:1.5}}
.footer{{text-align:center;color:#788293;font-size:12px;padding:35px}}
</style>
</head>
<body>
<div class="header">
<h1>Evidence-Grounded AML Investigation for Cross-Border SWIFT Payments</h1>
<p>Interactive presentation dashboard covering payment scale, model results, controlled validation, evidence retrieval, investigation outcomes, and governance.</p>
</div>
<div class="container">
<div class="cards">{''.join(cards)}</div>
<div class="disclosure"><b>Positioning:</b> This is an auditable research-grade prototype using synthetic data. The predictive model is frozen; investigation evidence is separated from model signal; synthetic ground truth is validation-only; the AI investigation layer covers 32 persisted successful investigations.</div>
<div class="tabs">
<button class="tab active" data-target="executive">Executive</button>
<button class="tab" data-target="operations">AML Operations</button>
<button class="tab" data-target="evidence">Evidence</button>
<button class="tab" data-target="validation">Validation</button>
</div>
{''.join(plot_sections)}
</div>
<div class="footer">Generated from persisted verified project results. No model retraining or API calls are performed by this dashboard.</div>
<script>
const tabs=document.querySelectorAll('.tab');
const panels=document.querySelectorAll('.panel');
tabs.forEach(t=>t.addEventListener('click',()=>{{
  tabs.forEach(x=>x.classList.remove('active')); panels.forEach(x=>x.classList.remove('active'));
  t.classList.add('active'); document.getElementById(t.dataset.target).classList.add('active');
  window.dispatchEvent(new Event('resize'));
}}));
document.getElementById('executive').classList.add('active');
</script>
</body>
</html>'''

DASH.write_text(html, encoding='utf-8')
print(f"Wrote {DASH}")
