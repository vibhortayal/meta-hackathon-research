# Source note — Modal Sandboxes docs

- URL: https://modal.com/docs/guide/sandboxes
- Fetched: 2026-10-27
- Readable: Yes.

Key facts:
- Sandboxes are secure containers for executing untrusted code (e.g., LLM-generated code), created via `Sandbox.create` in the Python/JavaScript/Go SDKs.
- Default maximum lifetime 5 minutes, configurable up to 24 hours via `timeout`; idle timeouts supported; billed at max(request, actual).
- Two runtimes: gVisor (default isolation) and VMs (full Linux kernel; needed for Docker-in-Sandbox, FUSE, nested cgroups). GPU sandboxes only on gVisor.
- Supports custom images, volumes, secrets/environment variables, readiness probes (TCP/exec), filesystem snapshots, named sandboxes (unique per running App, <64 chars), and up to 10 tags per sandbox.
- The event page links "sandboxes" as one of the Modal offerings available alongside the $100 credit.
