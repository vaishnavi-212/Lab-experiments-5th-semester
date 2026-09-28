# Experiment 01: Hypervisor Analysis

## Objective

To study and compare Type-1 and Type-2 hypervisors by creating Ubuntu virtual machines, examining their configurations, and analyzing CPU performance using Sysbench.

## Technologies Used

- Proxmox Virtual Environment (Type-1 Hypervisor)
- VMware Workstation (Type-2 Hypervisor)
- Ubuntu Linux
- Sysbench
- Linux System Monitoring Commands

## Introduction

A hypervisor is software that creates and manages virtual machines, allowing multiple operating systems to run on a single physical machine.

Hypervisors are classified into two types:

### Type-1 Hypervisor

A Type-1 hypervisor runs directly on physical hardware without requiring a conventional host operating system.

In this experiment, Proxmox VE was used to create and manage an Ubuntu virtual machine.

### Type-2 Hypervisor

A Type-2 hypervisor runs as an application on top of a host operating system.

In this experiment, VMware Workstation was used to create and run an Ubuntu virtual machine on Windows.

---

## Experimental Setup

| Parameter | Type-1: Proxmox VE | Type-2: VMware Workstation |
|---|---|---|
| Hypervisor | Proxmox VE | VMware Workstation |
| Guest OS | Ubuntu | Ubuntu |
| CPU | 2 vCPU | 2 vCPU |
| RAM | 2 GB | 4 GB |
| Disk | 20 GB | 20 GB |
| Network | VirtIO Bridge | NAT |
| Benchmark Tool | Sysbench | Sysbench |

---

## Experiment Procedure

### Part A: Type-1 Hypervisor

1. Accessed the Proxmox VE web interface.
2. Examined the physical server configuration.
3. Created an Ubuntu virtual machine.
4. Allocated 2 CPU cores, 2 GB RAM, and 20 GB storage.
5. Configured the virtual network interface.
6. Started the virtual machine.
7. Accessed the Ubuntu console.
8. Examined the virtual machine's hardware configuration.

### Part B: Type-2 Hypervisor

1. Installed and launched VMware Workstation.
2. Created a new virtual machine.
3. Selected Ubuntu as the guest operating system.
4. Allocated 2 CPU cores, 4 GB RAM, and 20 GB storage.
5. Configured the network adapter using NAT.
6. Started the Ubuntu virtual machine.
7. Opened the Ubuntu terminal.
8. Examined the virtual machine's hardware configuration.
9. Executed the Sysbench CPU benchmark.
10. Recorded the performance metrics.

---

## System Configuration Commands

The following Linux commands were used to examine the virtual machine configuration.

### CPU Information

```bash
lscpu
```

Displays CPU architecture, processor count, model, and virtualization information.

### Memory Information

```bash
free -h
```

Displays total, used, free, and available memory.

### Storage Information

```bash
lsblk
```

Displays block devices, disk partitions, and mount points.

### Kernel Information

```bash
uname -a
```

Displays Linux kernel and system information.

### Sysbench Version

```bash
sysbench --version
```

Displays the installed Sysbench version.

---

## CPU Performance Benchmark

Sysbench was used to evaluate CPU performance inside the virtual machine.

### Benchmark Command

```bash
sysbench cpu --cpu-max-prime=20000 --threads=2 run
```

### Benchmark Parameters

| Parameter | Value |
|---|---|
| Benchmark | CPU |
| Prime Number Limit | 20000 |
| Threads | 2 |
| Default Test Duration | 10 seconds |

The benchmark performs CPU-intensive prime number calculations and measures the number of operations completed during execution.

---

## Performance Results

### VMware Workstation

| Metric | Result |
|---|---:|
| Total Execution Time | 10.0006 s |
| Total Events | 24413 |
| Events Per Second | 2440.88 |
| Minimum Latency | 0.68 ms |
| Average Latency | 0.82 ms |
| Maximum Latency | 45.09 ms |
| 95th Percentile Latency | 0.94 ms |

### Proxmox VE

The Proxmox CPU benchmark result has not yet been recorded.

A direct numerical performance comparison will be possible after executing the same benchmark on the Proxmox virtual machine.

---

## Screenshots

### Type-1: Proxmox VE

The following screenshots document the Proxmox environment and virtual machine configuration.

| Screenshot | Description |
|---|---|
| 01 | Proxmox dashboard |
| 02 | Virtual machine configuration |
| 03 | Virtual machine running |
| 04 | Ubuntu console |
| 05 | System configuration |

Screenshots are available in:

`screenshots/type1-proxmox/`

### Type-2: VMware Workstation

The following screenshots document the VMware environment and benchmark execution.

| Screenshot | Description |
|---|---|
| 01 | VMware virtual machine configuration |
| 02 | Ubuntu virtual machine running |
| 03 | System configuration |
| 04 | Sysbench CPU benchmark result |

Screenshots are available in:

`screenshots/type2-vmware/`

---

## Performance Analysis

The experiment examines the following performance metrics:

- **Execution Time:** Duration of benchmark execution.
- **Events Per Second:** Number of benchmark operations completed per second.
- **Average Latency:** Average time required to complete an operation.
- **Maximum Latency:** Highest observed operation latency.
- **95th Percentile Latency:** Latency below which 95% of recorded operations fall.

The VMware virtual machine achieved 2440.88 events per second with an average latency of 0.82 ms.

The Proxmox benchmark remains to be measured.

The current virtual machines also have different RAM allocations and run on different physical hosts. Therefore, the available results cannot establish which hypervisor provides greater CPU performance.

For a controlled comparison, equivalent virtual machine configurations and consistent benchmark conditions should be used.

For detailed analysis, refer to [Performance Analysis](performance-analysis.md).

---

## Hypervisor Comparison

| Feature | Type-1 Hypervisor | Type-2 Hypervisor |
|---|---|---|
| Example | Proxmox VE | VMware Workstation |
| Installation | Directly on physical hardware | On a host operating system |
| Host OS Required | No conventional host OS required | Yes |
| Virtual Machine Management | Web-based management interface | Desktop application |
| Typical Usage | Servers and virtualization infrastructure | Desktop virtualization and development |

For detailed comparison, refer to [Hypervisor Comparison](screenshots/comparison.md).

---

## Repository Structure

```text
Experiment-01-Hypervisor-Analysis/
│
├── README.md
│
├── performance-analysis.md
│
└── screenshots/
    │
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

---

## Conclusion

The experiment demonstrated the practical implementation of Type-1 and Type-2 virtualization using Proxmox VE and VMware Workstation.

Ubuntu virtual machines were created and configured in both environments.

System information was examined using Linux commands, and CPU performance was measured using Sysbench in the VMware environment.

The experiment provided practical understanding of hypervisor architecture, virtual machine configuration, resource allocation, and CPU performance measurement.

A complete numerical comparison requires the corresponding Proxmox benchmark results under comparable experimental conditions.