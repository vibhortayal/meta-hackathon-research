# Staging report — Costco JSON export (owner uploads, 2026-10-27; v2)
TWO files staged. File 2 (the "2014" dump) SUPERSEDES file 1: all 63 file-1
barcodes are inside file 2. File 2 is the canonical staged set.
CORRECTION on range: the file name claims 2014-11-01, but the earliest actual
receipt is 2023-10-25. Costco's digital system holds 3 years here, not 12.
Canonical set: 114 receipts, 2023-10-25 to 2026-10-26; 93 Sales, 21 Refund;
1,226 lines; 569 distinct items; arithmetic 114 of 114; sales $15,823.23;
refunds -$2,336.51; egg whites x35, spinach x30, pasture eggs x25 are the top
repeats; 103 items have 3+ purchases. One receipt carries warehouseCountry
"CN" — an anomaly in the source data, noted, not explained.
File-1 detail below is retained for the record.
Status: STAGED ONLY. Not merged into any dictionary, ledger, or pattern store.
The raw file stays in this folder and OUT of git (full purchase history; the
repo carries this report only).

## Content
- 63 receipts, 2025-01-29 to 2026-10-26 (21 months). 48 Sales, 15 Refund.
- 637 lines, 313 distinct items, 10.1 lines per receipt.
- Stores: Fremont 35, Newark 23, Pentagon City 1, NE San Jose 1, Sunnyvale 2, Lewisville TX 1.
- Sales total: $8,078.28.
- Arithmetic: 63 of 63 — line sums equal subTotal on every receipt, refunds included.
- The 7 spike-1 PDFs are a subset (Pentagon City barcode confirmed present).

## Field map (receipt level)
transactionDate/Time, transactionType (Sales|Refund), transactionBarcode,
warehouse fields, totalItemCount, subTotal, taxes, total, instantSavings,
itemArray[], tenderArray[], couponArray[].
Line level: itemNumber, itemDescription01 (abbreviated, e.g. "ORG BELLAS"),
itemDescription02 (pack/size detail on 501 of 637 lines), unit (signed;
negative on refunds), amount (signed), taxFlag, itemIdentifier.

## Pattern viability (answers critique point 3)
58 items have 3+ purchases; 22 have 5+. Top: egg whites x24, spinach x16,
Greek yogurt x14, pasture eggs x14, blueberries x13, ORG BELLAS x13,
blackberries x12, edamame x11, sourdough x9, cauliflower x9.
Cadence is computable at warehouse scale (weeks). No cold-start problem.

## Returns are a major behavior
15 of 63 transactions are refunds (24%). Largest: -$1,106.14 (2026-04-15).
79 negative lines; refund units are signed too. Returns netting is not a
corner case in this data — it is a quarter of the record.

## Caveat
Descriptions are still codes. Decode is still required, but the problem is
now easier: itemNumber is a stable key, repetition is deep, and
description02 carries size/pack evidence for most lines.
