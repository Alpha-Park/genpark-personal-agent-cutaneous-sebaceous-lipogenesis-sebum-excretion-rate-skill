"""
Cutaneous Sebaceous Lipogenesis & Sebumetry Dynamics Client.
Zero-mock pure Python standard library implementation.
Calculates Casual Sebum Level (CSL in ug/cm2), Sebum Excretion Rate (SER in ug/cm2/h),
and skin surface lipid barrier typing via photometric sebumetry.
"""

import math
from typing import Dict, Any, Optional


class SebaceousLipogenesisClient:
    """
    Evaluates sebaceous gland lipogenesis and epidermal lipid barrier kinetics:
    - Casual Sebum Level (CSL in ug/cm2): steady-state sebum on unwashed skin
    - Sebum Excretion Rate (SER in ug/cm2/h): dynamic re-accumulation rate after degreasing
    - Sebumeter photometric transmission calibrated in ug/cm2
    - Clinical skin lipid classification (Alipic, Eudermic, Seborrheic)
    """

    def __init__(self):
        pass

    def evaluate_sebum_kinetics(
        self,
        casual_sebum_level_ug_cm2: float,
        reaccumulated_sebum_ug_cm2: Optional[float] = None,
        accumulation_duration_hours: Optional[float] = 2.0,
        anatomical_site: Optional[str] = "forehead",
        patient_age_years: Optional[int] = 25
    ) -> Dict[str, Any]:
        """
        Calculates sebum excretion parameters.
        casual_sebum_level_ug_cm2: baseline casual sebum level (10.0 to 450.0 ug/cm2).
        reaccumulated_sebum_ug_cm2: post-cleansing lipid accumulation in ug/cm2 (optional).
        accumulation_duration_hours: elapsed time in hours since cleansing (default 2.0h).
        anatomical_site: forehead, T-zone, cheek, chin.
        """
        if casual_sebum_level_ug_cm2 < 0:
            raise ValueError("Casual sebum level cannot be negative.")

        ser_ug_cm2_h = None
        if reaccumulated_sebum_ug_cm2 is not None and accumulation_duration_hours and accumulation_duration_hours > 0:
            if reaccumulated_sebum_ug_cm2 < 0:
                raise ValueError("Reaccumulated sebum cannot be negative.")
            ser_ug_cm2_h = round(reaccumulated_sebum_ug_cm2 / accumulation_duration_hours, 2)

        # Reference thresholds for forehead / T-zone (highest sebaceous density ~400-900 glands/cm2):
        # Alipic / Dry: CSL < 90 ug/cm2 or SER < 15.0 ug/cm2/h
        # Normal / Eudermic: CSL 90 - 200 ug/cm2, SER 15.0 - 55.0 ug/cm2/h
        # Oily / Seborrheic: CSL 200 - 280 ug/cm2, SER 55.0 - 85.0 ug/cm2/h
        # Severe Seborrhea: CSL > 280 ug/cm2 or SER > 85.0 ug/cm2/h
        if casual_sebum_level_ug_cm2 > 280.0 or (ser_ug_cm2_h and ser_ug_cm2_h > 85.0):
            skin_type = "Severe Seborrhea / Hyperseborrheic Skin"
            pathology_risk = "Excessive androgenic sebocyte proliferation; heightened risk for acne vulgaris, Cutibacterium acnes overgrowth, and seborrheic dermatitis."
        elif casual_sebum_level_ug_cm2 >= 200.0 or (ser_ug_cm2_h and ser_ug_cm2_h >= 55.0):
            skin_type = "Oily / Moderate Seborrheic Skin"
            pathology_risk = "Elevated sebum output with follicular dilatation and lipid shine."
        elif casual_sebum_level_ug_cm2 >= 90.0:
            skin_type = "Normal / Balanced Eudermic Skin"
            pathology_risk = "Physiological balance of wax esters, squalene, and triglycerides maintaining stratum corneum acid mantle and water repellency."
        else:
            skin_type = "Dry / Alipic Skin (Sebaceous Hyposecretion)"
            pathology_risk = "Deficient surface lipid film; increased transepidermal water loss vulnerability and xerotic barrier breakdown."

        return {
            "status": "success",
            "sebum_metrics": {
                "casual_sebum_level_ug_cm2": round(casual_sebum_level_ug_cm2, 1),
                "sebum_excretion_rate_ug_cm2_h": ser_ug_cm2_h,
                "accumulation_duration_hours": accumulation_duration_hours if ser_ug_cm2_h else None,
                "anatomical_site": anatomical_site
            },
            "lipid_barrier_classification": {
                "skin_type": skin_type,
                "pathophysiologic_implication": pathology_risk
            }
        }
