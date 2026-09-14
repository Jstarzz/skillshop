# Take My Load integration notes

The current project direction uses a Go controller, Go workers, and a high-throughput Rust HTTP engine. Controller-issued assignments preserve target policy, capacity-aware sharding, ready barriers, synchronized start, cancellation, and failure propagation.

Use coordination simulation before enabling execution on a new topology. Treat the controller's planning ceiling as a safety/planning constraint, not a benchmark result.

For every run, preserve:
- exact controller/worker/engine versions;
- authorized target and plan;
- worker inventory and usable capacity;
- scheduled / started / completed / failed requests;
- backpressure;
- achieved RPS;
- latency/status summary;
- generator CPU/network/socket headroom;
- target-side resource telemetry.

The architecture can target very high aggregate rates, but actual 100k/1M-class claims require benchmark evidence on hardware and networking capable of generating and receiving that traffic.
