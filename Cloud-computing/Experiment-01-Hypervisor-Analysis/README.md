# Hypervisor Analysis

## Overview

This work explores virtualization using two different hypervisor architectures:

- **Type-1 Hypervisor:** Proxmox VE
- **Type-2 Hypervisor:** VMware Workstation
- **Guest Operating System:** Ubuntu

The work focuses on understanding how virtual machines are created, configured, and monitored in different virtualization environments.

## Hypervisors

### Proxmox VE

Proxmox VE is a Type-1 hypervisor platform that runs directly on physical server hardware. It provides a web-based interface for creating and managing virtual machines.

The Ubuntu virtual machine was configured with:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 2 GB |
| Disk | 20 GB |
| Network | VirtIO Bridge |

### VMware Workstation

VMware Workstation is a Type-2 hypervisor that runs on top of a host operating system. It provides a desktop environment for creating and managing virtual machines.

The Ubuntu virtual machine was configured with:

| Resource | Configuration |
|---|---|
| CPU | 2 vCPU |
| Memory | 4 GB |
| Disk | 20 GB |
| Network | NAT |

## System Monitoring

Linux commands were used to inspect the virtual machine environment and verify its allocated resources.

```bash
lscpu
```

Displays processor architecture, CPU count, processor information, and virtualization details.

```bash
free -h
```

Displays memory usage and availability.

```bash
lsblk
```

Displays storage devices, partitions, and mount points.

```bash
uname -a
```

Displays kernel and system information.

```bash
sysbench --version
```

Displays the installed Sysbench version.

## CPU Benchmarking

CPU performance was measured using Sysbench with the following workload:

```bash
sysbench cpu --cpu-max-prime=20000 --threads=2 run
```

The benchmark uses two worker threads and performs CPU-intensive prime number calculations.

The benchmark output provides metrics such as:

- Execution time
- Total events
- Events per second
- Minimum latency
- Average latency
- Maximum latency
- 95th percentile latency

The recorded benchmark results and metric explanations are documented separately in:

`performance-analysis.md`

## Virtualization Comparison

The two virtualization approaches are compared based on:

- Hypervisor architecture
- Virtual machine configuration
- Resource allocation
- Virtual machine management
- CPU benchmarking methodology

The detailed comparison is available in:

`screenshots/comparison.md`

## Screenshots

Screenshots are organized according to the virtualization platform.

### Proxmox VE

Located in:

`screenshots/type1-proxmox/`

The screenshots document the Proxmox environment, virtual machine configuration, Ubuntu console, and system information.

### VMware Workstation

Located in:

`screenshots/type2-vmware/`

The screenshots document the VMware virtual machine configuration, running Ubuntu system, system information, and Sysbench output.

## Repository Structure

```text
Experiment-01-Hypervisor-Analysis/
│
├── README.md
├── performance-analysis.md
│
└── screenshots/
    ├── comparison.md
    │
    ├── type1-proxmox/
    │   ├── 01-proxmox-dashboard.png
    │   ├── 02-proxmox-vm-configuration.png
    │   ├── 03-proxmox-vm-running.png
    │   ├── 04-proxmox-ubuntu-console.png
    │   └── 05-proxmox-system-configuration.png
    │
    └── type2-vmware/
        ├── 01-vmware-vm-configuration.png
        ├── 02-vmware-vm-running.jpeg
        ├── 03-vmware-system-configuration.png
        └── 04-vmware-sysbench-result.jpeg
```

## Summary

This work provides practical exposure to virtualization concepts, virtual machine configuration, resource allocation, Linux system inspection, and CPU benchmarking.

The detailed performance measurements and Type-1 versus Type-2 comparison are maintained separately to keep the documentation organized and focused.