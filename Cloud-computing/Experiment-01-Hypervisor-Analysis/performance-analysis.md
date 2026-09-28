# Hypervisor Performance Analysis

## 1. Objective

To analyze the performance of virtual machines running on a Type-1 hypervisor and a Type-2 hypervisor using equivalent workloads and measurable CPU performance metrics.

The experiment uses:

- Type-1 Hypervisor: Proxmox VE
- Type-2 Hypervisor: VMware Workstation
- Guest Operating System: Ubuntu
- Benchmark Tool: Sysbench CPU

---

## 2. Experimental Configuration

| Parameter | Proxmox VE | VMware Workstation |
|---|---|---|
| Hypervisor Type | Type-1 | Type-2 |
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Network | Virtual/Bridged | NAT |
| Benchmark | Sysbench CPU | Sysbench CPU |
| Threads | 2 | 2 |
| Prime Number Limit | 20000 | 20000 |

---

## 3. Benchmark Method

The CPU performance of the virtual machines is measured using Sysbench.

The benchmark command used is:

`sysbench cpu --cpu-max-prime=20000 --threads=2 run`

The benchmark performs CPU-intensive calculations using prime numbers up to the specified limit.

The following metrics are recorded:

- Total execution time
- Total number of events
- Events per second
- Minimum latency
- Average latency
- Maximum latency
- 95th percentile latency

---

## 4. VMware Workstation Results

The recorded VMware Workstation benchmark produced the following results:

| Metric | VMware Workstation |
|---|---:|
| Prime Number Limit | 20000 |
| Threads | 2 |
| Total Execution Time | 10.0006 s |
| Total Events | 24413 |
| Events per Second | 2440.88 |
| Minimum Latency | 0.68 ms |
| Average Latency | 0.82 ms |
| Maximum Latency | 45.09 ms |
| 95th Percentile Latency | 0.94 ms |

The VMware VM completed the CPU benchmark in approximately 10 seconds and processed 24413 events.

---

## 5. Proxmox VE Results

The Proxmox VM was configured with 2 vCPUs, 2 GB RAM, and a 20 GB virtual disk.

The Sysbench CPU benchmark result has not yet been recorded.

| Metric | Proxmox VE |
|---|---:|
| Prime Number Limit | 20000 |
| Threads | 2 |
| Total Execution Time | To be measured |
| Total Events | To be measured |
| Events per Second | To be measured |
| Minimum Latency | To be measured |
| Average Latency | To be measured |
| Maximum Latency | To be measured |
| 95th Percentile Latency | To be measured |

---

## 6. Performance Metrics

### Execution Time

Execution time represents the amount of time required to complete the benchmark workload.

Lower execution time indicates that the workload was completed in less time.

### Events Per Second

Events per second represents the number of benchmark operations completed per second.

Higher events per second indicates greater throughput for the tested workload.

### Average Latency

Average latency represents the average time taken to complete individual benchmark operations.

Lower average latency indicates that operations were completed with less delay.

### Maximum Latency

Maximum latency represents the highest observed response time during the benchmark.

It can indicate occasional delays or interruptions during execution.

---

## 7. Current Comparison

| Metric | Proxmox VE | VMware Workstation |
|---|---:|---:|
| Execution Time | To be measured | 10.0006 s |
| Total Events | To be measured | 24413 |
| Events Per Second | To be measured | 2440.88 |
| Average Latency | To be measured | 0.82 ms |
| Maximum Latency | To be measured | 45.09 ms |

A direct performance conclusion cannot be made until the Proxmox benchmark is performed using the same workload.

---

## 8. Fair Comparison

The current VM configurations are not completely identical.

The Proxmox VM uses 2 GB RAM, while the VMware VM currently uses 4 GB RAM.

Therefore, the current benchmark results should not be treated as a controlled comparison between the two hypervisor types.

For a fair comparison, both virtual machines should use the same:

- Guest operating system
- CPU allocation
- Memory allocation
- Disk configuration
- Sysbench version
- Prime number limit
- Number of benchmark threads

The recommended controlled configuration is:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 2 GB |
| Disk | 20 GB |
| Guest OS | Same Ubuntu version |
| Sysbench workload | CPU |
| Prime Number Limit | 20000 |
| Threads | 2 |

---

## 9. Observations

1. Proxmox VE provides Type-1 virtualization directly on the physical server hardware.
2. VMware Workstation provides Type-2 virtualization on top of the host operating system.
3. Both virtual machines currently use 2 virtual CPU cores and a 20 GB virtual disk.
4. The Proxmox VM has 2 GB RAM, while the VMware VM has 4 GB RAM.
5. The VMware benchmark produced 2440.88 events per second.
6. The VMware benchmark completed in 10.0006 seconds.
7. The VMware average latency was 0.82 ms.
8. The VMware maximum latency was 45.09 ms.
9. A Proxmox benchmark result is required before making a direct numerical comparison.
10. Matching the VM configurations is necessary for a controlled performance comparison.

---

## 10. Conclusion

The experiment demonstrates the practical difference between Type-1 and Type-2 hypervisors.

Proxmox VE provides virtualization directly on the physical hardware, whereas VMware Workstation operates as an application on a host operating system.

Sysbench provides measurable CPU performance metrics including execution time, events per second, and latency.

The current VMware results have been recorded, while the Proxmox benchmark remains to be measured. Once the Proxmox benchmark is performed using the same workload and equivalent VM configuration, the two hypervisor environments can be compared using the recorded performance metrics.