# Spike 2 — photo-receipt gate (INTERIM, v1 prompt, muse-spark-1.3 vision, Standard)

Gate (set 2026-10-27): >=90% lines correct on 20 real paper receipts, mixed stores
and lighting, before the build commits. Fallback if failed: PDF + e-receipts only.
Line correct = product identity + amount paid both right.

## Progress: 3 unique receipts, 4 photographs, 8/8 lines correct
- Safeway 2026-07-29, FLAT photo: 3/3 lines, item numbers exact, Green Giant
  expansion right, savings folded (0.99/3.00/3.00), balance 14.98 matched.
- Safeway 2026-07-29, HAND photo (same receipt, thumb occludes left edge): 3/3
  products+prices. Item numbers: 1 exact; 1 partial-honest (visible digits only,
  no invention); 1 flagged CHECK with the CORRECT full number in alternatives.
- Safeway 2026-09-12, DARK car photo: 1/1 line (Alec's Ice Cream PI), prices exact,
  balance 7.99 matched. Item-number digit string likely misread (crossed by shadow;
  ground truth itself uncertain) — product+price unaffected.
- Apni Mandi (independent Indian grocer) 2024-07-03, hand photo: 4/4 lines —
  duplicate Mint lines kept separate (count 4 matches), DEEP peanuts and
  "Mampster Sooji Gol Gappa 290G" read as printed, EMV payment block ignored,
  total 15.36 matched.

## Findings
- Balance/arithmetic check passes on 4/4 photographs.
- Weak dimension = item numbers under occlusion, not products or prices. Behavior
  under occlusion is honest: partial digits, flags, correct answers in alternatives.
- Flavor codes (BR/CH/PI on Alec's Ice Cream) stay unexpanded — correct
  conservatism; the dictionary resolves them from repeat sightings (brand repeats
  across both Safeway receipts already).
- Cost ~$0.015 per photo; latency ~11 s per photo (fine for intake, not in-store).

## Remaining for the gate
17 more unique receipts. The set so far is SHORT receipts (1-4 lines); long
receipts (20+ lines) are the untested hard case. Verdict so far: promising,
not proven.
