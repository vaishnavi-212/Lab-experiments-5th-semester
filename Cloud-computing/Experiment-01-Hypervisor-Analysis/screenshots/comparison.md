# Type-1 vs Type-2 Hypervisor Comparison

## Objective

To study and compare Type-1 and Type-2 hypervisors by running Ubuntu virtual machines and measuring CPU performance using Sysbench.

## Hypervisors Used

| Feature | Type-1: Proxmox VE | Type-2: VMware Workstation |
|---|---|---|
| Hypervisor Type | Type-1 | Type-2 |
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Network | Virtual/Bridged | NAT |
| Benchmark | Sysbench CPU | Sysbench CPU |

## Type-1 Hypervisor — Proxmox VE

Proxmox VE is a Type-1 hypervisor that runs directly on the physical hardware and manages virtual machines.

### Proxmox VM Configuration

- Guest OS: Ubuntu
- CPU: 2 vCPU
- Memory: 2 GB
- Disk: 20 GB
- Hypervisor: Proxmox VE

The Proxmox VM configuration confirms 2 CPU cores, 2048 MB memory, and a 20 GB virtual disk.

## Type-2 Hypervisor — VMware Workstation

VMware Workstation is a Type-2 hypervisor that runs on top of a host operating system and provides virtual machines.

### VMware VM Configuration

- Guest OS: Ubuntu
- CPU: 2 vCPU
- Memory: 4 GB
- Disk: 20 GB
- Network: NAT
- Hypervisor: VMware Workstation

The VMware virtual machine was successfully started with Ubuntu as the guest operating system.

## CPU Benchmark

The CPU performance was measured using Sysbench.

### Benchmark Command

The following command was used:

`sysbench cpu --cpu-max-prime=20000 --threads=2 run`

The benchmark uses a prime number limit of 20000 and two worker threads.

## VMware Workstation Benchmark Result

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

## Proxmox VE Benchmark Result

The Proxmox CPU benchmark result is yet to be recorded.

| Metric | Proxmox VE |
|---|---:|
| Prime Number Limit | 20000 |
| Threads | 2 |
| Total Execution Time | To be measured |
| Total Events | To be measured |
| Events per Second | To be measured |
| Average Latency | To be measured |
| Maximum Latency | To be measured |
| 95th Percentile Latency | To be measured |

## Performance Comparison

| Metric | Type-1: Proxmox VE | Type-2: VMware Workstation |
|---|---:|---:|
| Hypervisor Type | Type-1 | Type-2 |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Threads | 2 | 2 |
| Prime Number Limit | 20000 | 20000 |
| Execution Time | To be measured | 10.0006 s |
| Total Events | To be measured | 24413 |
| Events per Second | To be measured | 2440.88 |
| Average Latency | To be measured | 0.82 ms |

## Observations

1. Proxmox VE provides Type-1 virtualization and runs directly on the physical server hardware.
2. VMware Workstation provides Type-2 virtualization and runs above a host operating system.
3. Both virtual machines use 2 virtual CPU cores and a 20 GB virtual disk.
4. The current Proxmox VM has 2 GB RAM, while the VMware VM has 4 GB RAM.
5. The recorded VMware Sysbench test achieved 2440.88 events per second.
6. The VMware benchmark completed in 10.0006 seconds.
7. A Proxmox Sysbench result is required before making a direct numerical performance comparison.
8. For a controlled comparison, both virtual machines should use identical CPU, memory, disk, guest OS, and benchmark settings.

## Fair Comparison Consideration

The current configurations are not completely identical because the Proxmox VM has 2 GB RAM while the VMware VM has 4 GB RAM.

Therefore, the current results should be treated as experimental observations rather than a controlled performance comparison.

For a fair comparison, both virtual machines should use:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 2 GB |
| Disk | 20 GB |
| Guest OS | Same Ubuntu version |
| Benchmark | Sysbench CPU |
| Threads | 2 |
| Prime Limit | 20000 |

## Conclusion

The experiment demonstrates the difference between Type-1 and Type-2 virtualization.

Proxmox VE operates as a Type-1 hypervisor directly on the physical hardware, whereas VMware Workstation operates as a Type-2 hypervisor on top of a host operating system.

Sysbench provides measurable CPU performance metrics such as execution time, total events, events per second, and latency. A direct performance comparison can be performed after obtaining the Proxmox benchmark using the same workload and equivalent VM configuration.