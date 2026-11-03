# Cutaneous Sebaceous Lipogenesis Sebumetry Personal Agent Skill

[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](LICENSE)
[![Python: 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/)
[![Zero Dependencies](https://img.shields.io/badge/dependencies-zero-brightgreen.svg)]()
[![Model Context Protocol](https://img.shields.io/badge/MCP-Standard%20JSON--RPC-orange.svg)]()
[![Production Ready](https://img.shields.io/badge/status-production--ready-green.svg)]()

Deterministic, zero-mock personal agent micro-skill for calculating Casual Sebum Level ($CSL$ in $\mu\text{g}/\text{cm}^2$) and Sebum Excretion Rate ($SER$ in $\mu\text{g}/(\text{cm}^2 \cdot \text{h})$) using photometric sebumetry to evaluate epidermal lipid barrier health.

## Architecture

```mermaid
flowchart TD
    A[Photometric Sebumeter Tape Sampling] --> B[Measure Steady-State Casual Sebum Level CSL]
    B --> C[Post-Degreasing Sebum Accumulation Over Time]
    C --> D[Compute Sebum Excretion Rate SER = Delta S / Delta t]
    D --> E[Classify Alipic < 90 vs Eudermic vs Hyperseborrheic > 280]
```

## Quickstart

```python
from client import SebaceousLipogenesisClient

client = SebaceousLipogenesisClient()
result = client.evaluate_sebum_kinetics(
    casual_sebum_level_ug_cm2=145.0,
    reaccumulated_sebum_ug_cm2=2.3,
    accumulation_duration_hours=2.0
)
print(result)
```

## License

Apache-2.0
