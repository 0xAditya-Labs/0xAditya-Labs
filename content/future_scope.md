# Future Scope

## Modular Metrics System
- **Metric Verification Scripts:** We will introduce scripts (e.g., `benchmark.sh` or `fetch_telemetry.py`) similar to those used directly in the project repositories (like SwiftCache or ContextIQ). These scripts will run locally or via GitHub actions to regenerate and verify the latency/QPS metrics.
- **Dynamic README Injection:** Instead of hardcoding metrics in the `README.md`, they will be generated as a JSON artifact (e.g., `metrics.json`) and injected via python scripts to ensure zero manual updates for system metrics.
- **WakaTime Radar Chart:** Integrating a WakaTime-based stats chart to show a dynamic radar of language and domain usage over time, injected into the `~/stats` block.
- **Open Source Contributions Marker:** Tracking major PRs dynamically to populate the `~/open_source` section.
- **Hackathons Log:** Tracking and displaying major hackathon podiums.

This forms a self-updating, high-signal profile structure where every stat is verified and fetched dynamically.