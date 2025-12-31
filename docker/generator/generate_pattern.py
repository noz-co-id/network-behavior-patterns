import json
import time
from datetime import datetime
import random

patterns = [
    {
        "pattern_type": "procedure_latency",
        "procedure_class": "legacy_interop",
        "state": "aligned",
        "severity": "low"
    },
    {
        "pattern_type": "state_consistency",
        "procedure_class": "legacy_interop",
        "state": "drift_detected",
        "severity": "medium"
    }
]

output = []

for _ in range(5):
    entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "aggregation_window": "60s",
        "behavior_pattern": random.choice(patterns),
        "confidence": round(random.uniform(0.7, 0.98), 2),
        "source": "synthetic-generator",
        "compliance": {
            "gdpr": "non-personal",
            "3gpp": "procedure-level"
        }
    }
    output.append(entry)
    time.sleep(1)

with open("/output/aggregated-behavior.log.json", "w") as f:
    json.dump(output, f, indent=2)
