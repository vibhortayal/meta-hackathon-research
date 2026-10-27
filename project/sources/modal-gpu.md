# Source note — Modal GPU docs ("serverless GPUs" link)

- URL: https://modal.com/docs/guide/gpu
- Fetched: 2026-10-27
- Readable: Yes.

Key facts:
- GPU types selectable via the `gpu` argument: T4, L4, A10, L40S, A100 (40GB/80GB), RTX-PRO-6000, H100, H200, B200, B300; up to 8 GPUs per container on most types.
- Using a GPU requires a valid payment method on file (docs statement; relevant context for using Modal credits in practice — the event page does not state this condition).
- GPU fallback lists supported; multi-GPU training on a single node, multi-node training in private beta.
