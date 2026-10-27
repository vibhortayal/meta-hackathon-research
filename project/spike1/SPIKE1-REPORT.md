# Spike 1 — receipt decode (v1 prompt, muse-spark-1.3, Standard mode)

Set: 7 real Costco in-warehouse receipt PDFs (owner's, Oct 2026 back to Sep 25).
Golden-set note: 2 of the 7 are RETURN receipts; one item (2051892) is bought on one
receipt and returned on another — the returns requirement is in the data, not hypothetical.

## Scorecard vs SPEC gates
- Line capture: all purchasable items captured on all 7 receipts. Count diffs vs
  "items sold" fully explained: Instant Savings lines decoded as separate lines
  (R5 +2, R7 +1) and one qty-2 line (R2, Uber Eats cards).
- Arithmetic self-check: 7/7 — line sums equal receipt subtotals exactly,
  including both negative return receipts.
- Auto-posted: 45/57 lines (79%) vs 85% gate — near miss; the 12 flagged lines are
  mostly true ambiguity (correct behavior). Savings-line folding + dictionary
  reconciliation are the v2 levers.
- Silently wrong: 0 observed in manual review of all auto lines (gate <=2%).
- Returns: both detected; R6 (NFL women's pajamas -26.99) decoded at 0.95 with
  negative tax/total correct. R4's returned item matches R5's purchase by item no.
- Cost: $0.20 total, ~$0.029/receipt. Reasoning tokens dominate output — v2 uses
  low reasoning_effort for decode.

## Dictionary already forming (same item no. across receipts/stores)
96716 Organic Spinach x3 (prices differ by store: 5.39 / 3.99), 1063232 Egg Whites x3,
1048072 Greek Yogurt x2, 1068080 Pasture Raised Eggs x2, 1178969 Almond Flour x2
(16.99 vs 13.59), 763114 Organic Edamame x2, 9877788 Organic Tofu x2.

## v2 iteration list (eval loop)
1. Fold Instant Savings lines into their parent item as a discount field.
2. Dictionary conflict resolution: 815544 read as "Blueberry Muffins" (0.55) once and
   "Blueberries" (0.75) once — one user answer fixes it forever.
3. True-ambiguity checks working as designed: 32911 "Vanilla" (0.50), 22967 chicken
   thighs (0.70), 121288 "ORG BELLAS" peppers-vs-portabellas (0.65).
4. reasoning_effort=low A/B on the same set; track score + cost trajectory.
