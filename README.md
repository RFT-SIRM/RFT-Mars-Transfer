# RFT-Mars-Transfer

Reproducible computational mission-envelope study for a **robotic** high-acceleration Earth–Mars transfer. The repository separates verified RFT mathematical results from classical mechanics and explicitly records unresolved propulsion assumptions.

## Scope

Baseline: 50,000 kg robotic vehicle, 55,000,000 km Earth–Mars distance, symmetric constant +1 g acceleration followed by −1 g deceleration. The same profile is applied on return.

This is **not** a claim of a working fractal drive, validated QPU, flight-ready battery, or experimental payload transport.

## Baseline results

- One-way flight time: ~41.605 h
- Round-trip time: ~83.211 h
- Peak speed: ~734.4 km/s (~0.245% c)
- Thrust at 1 g for 50 t: 490.33 kN
- Peak mechanical power: ~360.1 GW
- Ideal kinetic energy at turnover: ~3.7456 TWh per acceleration leg
- Four powered acceleration/deceleration legs round trip: ~14.97 TWh ideal kinetic-energy sum
- Reference 12 t battery at 1,500 Wh/kg: 18 MWh
- Ideal round-trip kinetic-energy requirement / reference battery: ~832,355×

The energy ratio is an **engineering gap**, not evidence that the RFT layer supplies the missing energy.

## Verification

Run:

```bash
python3 -m pytest -q
python3 src/run_calculations.py
```

CI repeats the tests and calculation generation.

## Evidence boundary

`docs/EVIDENCE_BOUNDARY.md` defines what is mathematical, numerical, architectural, or hypothetical. A future complete Lean 4 verification of the central theorem can be linked here without upgrading the classical propulsion model into an experimental claim.

## IP / legal status

This repository contains a proprietary-license notice and an IP disclosure template. Copyright/license controls use of the published repository contents; it does **not** by itself create a patent monopoly over underlying ideas. Potential patentable subject matter should be reviewed by qualified patent counsel **before public disclosure or further publication**. Public Git history is an evidence record, not a substitute for patent filing.
