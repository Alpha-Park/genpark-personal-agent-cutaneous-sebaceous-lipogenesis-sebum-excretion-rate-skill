"""
Example usage of Cutaneous Sebaceous Lipogenesis Skill.
Demonstrates balanced eudermic skin vs hyperseborrheic skin in acne vulgaris.
"""

import json
from client import SebaceousLipogenesisClient


def main():
    print("=== Testing Cutaneous Sebaceous Lipogenesis Skill ===")
    client = SebaceousLipogenesisClient()

    # 1. Healthy young adult with balanced eudermic skin (CSL = 145 ug/cm2, SER = 1.15 ug/cm2/h -> Eudermic)
    res_normal = client.evaluate_sebum_kinetics(
        casual_sebum_level_ug_cm2=145.0,
        reaccumulated_sebum_ug_cm2=2.3,
        accumulation_duration_hours=2.0,
        anatomical_site="forehead"
    )
    print("\n[Case 1: Normal Eudermic Skin]")
    print(json.dumps(res_normal, indent=2))

    # 2. Patient with severe seborrhea / active acne vulgaris (CSL = 340 ug/cm2, SER = 2.85 ug/cm2/h -> Severe Seborrhea)
    res_seborrhea = client.evaluate_sebum_kinetics(
        casual_sebum_level_ug_cm2=340.0,
        reaccumulated_sebum_ug_cm2=5.7,
        accumulation_duration_hours=2.0,
        anatomical_site="T-zone"
    )
    print("\n[Case 2: Severe Seborrheic / Hyperseborrhea]")
    print(json.dumps(res_seborrhea, indent=2))

    # Assertions
    assert "Normal" in res_normal["lipid_barrier_classification"]["skin_type"]
    assert "Severe" in res_seborrhea["lipid_barrier_classification"]["skin_type"]
    assert res_seborrhea["sebum_metrics"]["sebum_excretion_rate_ug_cm2_h"] > 2.0
    print("\n[SUCCESS] Cutaneous Sebaceous Lipogenesis tests passed!")


if __name__ == "__main__":
    main()
