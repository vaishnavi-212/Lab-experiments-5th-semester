# Type-1 vs Type-2 Hypervisor Comparison

## Objective

To compare Type-1 and Type-2 hypervisors based on their architecture, virtual machine configuration, resource allocation, and virtualization environment.

## Hypervisors Compared

| Feature | Type-1: Proxmox VE | Type-2: VMware Workstation |
|---|---|---|
| Hypervisor Type | Type-1 | Type-2 |
| Example | Proxmox VE | VMware Workstation |
| Guest OS | Ubuntu | Ubuntu |
| Host Environment | Runs directly on physical hardware | Runs on a host operating system |
| Management | Web-based interface | Desktop application |
| CPU | 2 vCPU | 2 vCPU |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Network | VirtIO Bridge | NAT |

## Type-1 Hypervisor — Proxmox VE

Proxmox VE provides virtualization directly on physical server hardware.

The virtual machine was configured with:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 2 GB |
| Disk | 20 GB |
| Network | VirtIO Bridge |
| Guest OS | Ubuntu |

The Proxmox environment was accessed through its web-based management interface.

## Type-2 Hypervisor — VMware Workstation

VMware Workstation runs as an application on top of a host operating system and provides an environment for running virtual machines.

The virtual machine was configured with:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 4 GB |
| Disk | 20 GB |
| Network | NAT |
| Guest OS | Ubuntu |

The Ubuntu virtual machine was started through VMware Workstation and accessed through its graphical environment.

## Architecture Comparison

| Aspect | Type-1 Hypervisor | Type-2 Hypervisor |
|---|---|---|
| Runs on | Physical hardware | Host operating system |
| Host OS dependency | No conventional host OS | Requires host OS |
| Example | Proxmox VE | VMware Workstation |
| Management style | Server/web interface | Desktop application |
| Common environment | Servers and virtualization infrastructure | Desktop virtualization and development |

## Resource Comparison

The two virtual machines share the same CPU and disk allocation but have different memory allocations.

| Resource | Proxmox VE | VMware Workstation |
|---|---:|---:|
| vCPU | 2 | 2 |
| Memory | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Guest OS | Ubuntu | Ubuntu |

The difference in memory allocation should be considered when interpreting benchmark results.

## Benchmark Workload

Both environments use the same intended CPU benchmark configuration:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=2 run
```

This provides a consistent workload configuration for CPU performance measurements.

The detailed benchmark measurements are documented separately in:

`../performance-analysis.md`

## Recorded VMware Result

The VMware Workstation benchmark produced:

| Metric | VMware Workstation |
|---|---:|
| Execution Time | 10.0006 s |
| Total Events | 24413 |
| Events Per Second | 2440.88 |
| Average Latency | 0.82 ms |
| Maximum Latency | 45.09 ms |
| 95th Percentile Latency | 0.94 ms |

The corresponding Proxmox benchmark has not yet been recorded.

## Observations

1. Proxmox VE represents a Type-1 virtualization architecture.
2. VMware Workstation represents a Type-2 virtualization architecture.
3. Both virtual machines use 2 vCPUs.
4. Both virtual machines use a 20 GB virtual disk.
5. The Proxmox VM has 2 GB RAM.
6. The VMware VM has 4 GB RAM.
7. The VMware Sysbench benchmark recorded 2440.88 events per second.
8. The VMware benchmark recorded an average latency of 0.82 ms.
9. A corresponding Proxmox benchmark is required for numerical performance comparison.

## Fair Comparison Requirements

A controlled comparison should use equivalent configurations and conditions.

| Parameter | Recommended Configuration |
|---|---|
| Guest OS | Same Ubuntu version |
| CPU | 2 vCPU |
| Memory | Same allocation |
| Disk | 20 GB |
| Sysbench Version | Same version |
| Prime Number Limit | 20000 |
| Threads | 2 |
| Benchmark Duration | Same duration |

The current results should therefore be interpreted as recorded observations rather than a final performance ranking between the two hypervisor types.

## Summary

Proxmox VE and VMware Workstation demonstrate two different approaches to virtualization.

Proxmox VE operates directly on physical server hardware, while VMware Workstation operates through a host operating system.

The comparison covers their architecture, virtual machine configurations, resource allocation, and benchmark setup. A numerical performance comparison can be completed after the Proxmox benchmark is recorded under comparable conditions.