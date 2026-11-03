---
name: genpark-personal-agent-cutaneous-sebaceous-lipogenesis-sebumetry-skill
version: 1.0.0
description: Calculates Casual Sebum Level (CSL in ug/cm2) and Sebum Excretion Rate (SER in ug/cm2/h) to classify skin surface lipid barrier typing via photometric sebumetry.
authors:
  - GenPark Ecosystem
tags:
  - personal-agent
  - dermatology
  - sebum
  - sebumetry
  - lipogenesis
  - skin-barrier
  - zero-dependency
---

# Cutaneous Sebaceous Lipogenesis Sebumetry Skill

## Mathematical Formulation

Sebum Excretion Rate ($SER$):

$$SER = \frac{S_{\text{accumulated}}}{\Delta t} \quad \left(\frac{\mu\text{g}}{\text{cm}^2 \cdot \text{h}}\right)$$

Where:
- $CSL$ ($\mu\text{g}/\text{cm}^2$): steady-state surface lipid concentration on uncleaned skin.
- $S_{\text{accumulated}}$ ($\mu\text{g}/\text{cm}^2$): lipid re-accumulation following degreasing.
- $\Delta t$ ($\text{hours}$): timed accumulation interval.

## Clinical Skin Lipid Barrier Classification
- **Dry / Alipic**: $CSL < 90 \, \mu\text{g}/\text{cm}^2$ (barrier lipid depletion, TEWL elevation risk)
- **Normal / Balanced Eudermic**: $CSL \in [90, 180) \, \mu\text{g}/\text{cm}^2$, $SER < 1.5 \, \mu\text{g}/(\text{cm}^2 \cdot \text{h})$
- **Oily / Seborrheic**: $CSL \in [180, 280] \, \mu\text{g}/\text{cm}^2$
- **Severe Hyperseborrhea**: $CSL > 280 \, \mu\text{g}/\text{cm}^2$ or $SER > 2.2 \, \mu\text{g}/(\text{cm}^2 \cdot \text{h})$ (acne vulgaris, seborrheic dermatitis vulnerability)
