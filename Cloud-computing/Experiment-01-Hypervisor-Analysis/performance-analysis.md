# Hypervisor Performance Analysis

## Objective

To analyze CPU performance in virtual machines using Sysbench and understand the performance metrics produced by the benchmark.

## Benchmark Configuration

The CPU benchmark was executed using:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=2 run
```

| Parameter | Value |
|---|---:|
| Benchmark | CPU |
| Prime Number Limit | 20000 |
| Threads | 2 |
| Default Execution Time | 10 seconds |

The Sysbench CPU workload performs prime-number calculations and reports throughput and latency statistics. :contentReference[oaicite:1]{index=1}

## Performance Metrics

### Execution Time

Execution time represents the total time taken to complete the benchmark workload.

A lower execution time means the workload completed in less time.

### Total Events

Total events represent the number of benchmark operations completed during the test.

### Events Per Second

Events per second represents the benchmark throughput, or the number of events processed per second.

A higher value indicates higher throughput for the tested workload. :contentReference[oaicite:2]{index=2}

### Average Latency

Average latency represents the average time taken to complete an individual benchmark operation.

Lower average latency indicates less delay per operation.

### Maximum Latency

Maximum latency represents the highest observed latency during the benchmark.

It can reveal occasional delays or interruptions during execution.

### 95th Percentile Latency

The 95th percentile latency represents the latency value below which approximately 95% of the recorded operations fall.

Sysbench provides percentile-based latency statistics as part of its benchmark reporting. :contentReference[oaicite:3]{index=3}

## VMware Workstation Results

The CPU benchmark was successfully executed inside the VMware Workstation virtual machine.

| Metric | Result |
|---|---:|
| Prime Number Limit | 20000 |
| Threads | 2 |
| Total Execution Time | 10.0006 s |
| Total Events | 24413 |
| Events Per Second | 2440.88 |
| Minimum Latency | 0.68 ms |
| Average Latency | 0.82 ms |
| Maximum Latency | 45.09 ms |
| 95th Percentile Latency | 0.94 ms |

### Result Analysis

The benchmark completed in approximately 10 seconds and processed 24,413 total events.

The measured throughput was **2440.88 events per second**.

The average latency was **0.82 ms**, while the maximum observed latency was **45.09 ms**. The 95th percentile latency was **0.94 ms**.

The difference between the maximum latency and the 95th percentile indicates that the highest latency was an occasional value rather than the typical latency observed for most operations.

## Proxmox VE Results

The Proxmox virtual machine was configured with:

| Parameter | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 2 GB |
| Disk | 20 GB |
| Guest OS | Ubuntu |

The same Sysbench workload is intended to be executed on the Proxmox virtual machine:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=2 run
```

The Proxmox benchmark values have not yet been recorded.

## Current Performance Data

| Metric | Proxmox VE | VMware Workstation |
|---|---:|---:|
| Execution Time | — | 10.0006 s |
| Total Events | — | 24413 |
| Events Per Second | — | 2440.88 |
| Average Latency | — | 0.82 ms |
| Maximum Latency | — | 45.09 ms |
| 95th Percentile Latency | — | 0.94 ms |

The dash (`—`) indicates that the corresponding measurement has not yet been recorded.

## Factors Affecting the Comparison

The current virtual machines do not have identical configurations.

| Parameter | Proxmox VE | VMware Workstation |
|---|---|---|
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Guest OS | Ubuntu | Ubuntu |
| Benchmark Threads | 2 | 2 |
| Prime Number Limit | 20000 | 20000 |

The VMware VM has twice the allocated memory of the Proxmox VM. In addition, the virtual machines are running on different physical environments.

Therefore, the recorded VMware result should be treated as an individual benchmark result rather than evidence that one hypervisor is faster than the other.

## Controlled Comparison

For a meaningful comparison, the following conditions should be kept equivalent:

- Same Ubuntu version
- Same number of vCPUs
- Same memory allocation
- Same virtual disk configuration
- Same Sysbench version
- Same prime number limit
- Same number of benchmark threads
- Same benchmark duration
- Similar host conditions where possible

After the Proxmox benchmark is recorded under comparable conditions, the results can be compared using execution time, events per second, and latency metrics.

## Conclusion

The Sysbench CPU benchmark provides measurable information about CPU workload throughput and latency inside a virtual machine.

The VMware Workstation VM recorded **2440.88 events per second**, with an average latency of **0.82 ms** and a total execution time of **10.0006 seconds**.

The corresponding Proxmox benchmark has not yet been recorded. Therefore, no numerical performance conclusion between the two hypervisor environments is made at this stage.