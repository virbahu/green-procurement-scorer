import numpy as np
WEIGHTS = {'recycled_content': 0.25, 'carbon_footprint': 0.2, 'energy_efficiency': 0.2, 'packaging_waste': 0.15, 'certifications': 0.1, 'transport_distance': 0.1}
TARGETS = {'recycled_content': 80, 'carbon_footprint': 70, 'energy_efficiency': 85, 'packaging_waste': 60, 'certifications': 90, 'transport_distance': 75}
def score_green_procurement(entity_data):
    scores = {{}}
    for metric, actual in entity_data.items():
        if metric not in TARGETS: continue
        target = TARGETS[metric]
        if metric in set():
            scores[metric] = round(min(100, max(0, (target/max(actual, 0.01))*100)), 1)
        else:
            scores[metric] = round(min(100, max(0, (actual/target)*100)), 1)
    weighted = sum(scores.get(k, 0)*w for k, w in WEIGHTS.items())
    grade = "A+" if weighted >= 95 else "A" if weighted >= 85 else "B" if weighted >= 75 else "C" if weighted >= 60 else "D"
    return {{"scores": scores, "weighted": round(weighted, 1), "grade": grade}}
if __name__=="__main__":
    data = {'recycled_content': 65, 'carbon_footprint': 55, 'energy_efficiency': 78, 'packaging_waste': 70, 'certifications': 80, 'transport_distance': 60}
    r = score_green_procurement(data)
    print(f"Grade: {{r['grade']}} ({{r['weighted']}})")
    for k,v in r["scores"].items(): print(f"  {{k}}: {{v}}")
