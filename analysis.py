"""Reproduce descriptive calculations for the accompanying paper.
IBM annual global average breach cost figures (USD millions); see README for source links.
"""
import csv
from pathlib import Path
p=Path(__file__).with_name('ibm_breach_costs.csv')
with p.open() as f: rows=list(csv.DictReader(f))
values={int(r['year']):float(r['average_cost_usd_millions']) for r in rows}
for y in sorted(values)[1:]:
    print(f'{y}: ${values[y]:.2f}m; YoY {(values[y]/values[y-1]-1)*100:.1f}%')
print('2021–2024 total change:',round((values[2024]/values[2021]-1)*100,2),'%')
for probability in (.05,.10,.20):
    print(f'Illustrative expected annual loss at p={probability:.0%}: ${probability*values[2024]*1e6:,.0f}')
