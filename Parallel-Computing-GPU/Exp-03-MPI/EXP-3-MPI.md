# Experiment 3 - MPI Matrix Multiplication

## Aim

To implement parallel matrix multiplication using MPI (Message Passing Interface) by distributing the computation among multiple processes running across a master and worker nodes.

## Objective

- Configure a multi-node MPI environment.
- Establish communication between the master and worker nodes.
- Verify SSH communication.
- Install and verify OpenMPI.
- Configure an MPI hostfile.
- Test MPI execution across four nodes.
- Implement matrix multiplication using MPI.
- Distribute matrix rows among MPI processes.
- Measure execution time.
- Verify the correctness of the computed matrix.

## System Configuration

| Component | Configuration |
|---|---|
| Operating System | Ubuntu |
| Architecture | ARM64 (aarch64) |
| MPI Implementation | OpenMPI |
| OpenMPI Version | 4.1.6 |
| Compiler | GCC |
| Number of Nodes | 4 |
| MPI Processes | 4 |
| Matrix Size | 4000 × 4000 |
| Programming Language | C |

## MPI Cluster

The MPI cluster consists of one master node and three worker nodes.

```text
                Master
                  |
        -----------------------
        |          |          |
     Worker 1   Worker 2   Worker 3
```

## MPI Architecture

The experiment uses four MPI processes:

```text
Rank 0 → Master
Rank 1 → Worker 1
Rank 2 → Worker 2
Rank 3 → Worker 3
```

The 4000 rows of the matrix are divided among the four MPI processes.

```text
4000 rows
    |
    +-------- 1000 rows → Rank 0
    |
    +-------- 1000 rows → Rank 1
    |
    +-------- 1000 rows → Rank 2
    |
    +-------- 1000 rows → Rank 3
```

Each process performs matrix multiplication for its assigned rows.

## MPI Communication

MPI provides communication between processes running on different nodes.

The experiment uses MPI functions such as:

- `MPI_Init()` - Initializes the MPI environment.
- `MPI_Comm_rank()` - Gets the rank of the current process.
- `MPI_Comm_size()` - Gets the total number of MPI processes.
- `MPI_Send()` - Sends data from one process to another.
- `MPI_Recv()` - Receives data from another process.
- `MPI_Finalize()` - Terminates the MPI environment.

## Matrix Multiplication

Matrix multiplication is performed using:

```text
C = A × B
```

For each element:

```text
C[i][j] = Σ A[i][k] × B[k][j]
```

For this experiment, all elements of matrices `A` and `B` are initialized to `1.0`.

Therefore:

```text
C[i][j] = 4000.00
```

because each result element is the sum of 4000 products of `1.0 × 1.0`.

## Experimental Procedure

### 1. Configure the MPI Cluster

The master and three worker virtual machines were configured for MPI execution.

```text
Master
Worker 1
Worker 2
Worker 3
```

### 2. Configure Hostnames

The nodes were configured as:

```text
master
worker1
worker2
worker3
```

### 3. Verify Network Connectivity

Connectivity between the master and worker nodes was tested using:

```bash
ping -c 4 worker1
ping -c 4 worker2
ping -c 4 worker3
```

All configured worker nodes responded successfully.

### 4. Configure SSH

SSH was enabled on the worker nodes.

The SSH service was verified using:

```bash
sudo systemctl status ssh
```

SSH communication was tested using:

```bash
ssh vaishnavi@worker1 hostname
ssh vaishnavi@worker2 hostname
ssh vaishnavi@worker3 hostname
```

### 5. Verify OpenMPI

OpenMPI was verified using:

```bash
mpirun --version
```

The installed version was:

```text
mpirun (Open MPI) 4.1.6
```

The MPI compiler was verified using:

```bash
mpicc --version
```

### 6. Configure the MPI Hostfile

The hostfile was configured as:

```text
master slots=1
worker1 slots=1
worker2 slots=1
worker3 slots=1
```

### 7. Test Four-Node MPI Execution

MPI execution across all four nodes was verified using:

```bash
mpirun -np 4 --hostfile hosts hostname
```

The output confirmed that the four MPI processes were distributed across:

```text
master
worker1
worker2
worker3
```

### 8. Test MPI Send and Receive

A simple MPI program was used to verify communication between processes.

The master process sends data to a worker using:

```c
MPI_Send()
```

The worker receives the data using:

```c
MPI_Recv()
```

This confirmed that MPI communication between the nodes was functioning correctly.

### 9. Compile the MPI Matrix Multiplication Program

The matrix multiplication program was compiled using:

```bash
mpicc matrix_mpi.c -o matrix_mpi
```

### 10. Execute MPI Matrix Multiplication

The matrix multiplication program was executed using four MPI processes:

```bash
mpirun -np 4 --hostfile hosts ./matrix_mpi
```

The processes divided the matrix rows among themselves and performed the computation in parallel.

## Program Execution

The program initialized matrices of size:

```text
4000 × 4000
```

The MPI processes were distributed as follows:

```text
Rank 0 on master   → computing 1000 rows
Rank 1 on worker1  → computing 1000 rows
Rank 2 on worker2  → computing 1000 rows
Rank 3 on worker3  → computing 1000 rows
```

After computation, the results were collected and verified.

## Result

The final execution produced:

```text
MPI Matrix Multiplication Completed
Matrix Size = 4000 × 4000
Number of MPI Processes = 4
Execution Time = 287.372540 seconds
Verification C[0][0] = 4000.00
```

## Verification

Since every element of matrices `A` and `B` is `1.0`:

```text
C[0][0] = 1×1 + 1×1 + ... + 1×1
```

There are 4000 terms:

```text
C[0][0] = 4000.00
```

Therefore, the result was verified successfully.

## Screenshots

Add your actual screenshot filenames here:

```text
screenshots/
├── 01-cluster-configuration.png
├── 02-vm-config.png
├── 03-hosts-and-ip.png
├── 04-network-connectivity.png
├── 05-ssh-service.png
├── 06-passwordless-ssh.png
├── 07-openmpi-installation.png
├── 08-mpi-hostfile.png
├── 09-four-node-mpi-test.png
├── 10-sendrecv-executable.png
├── 11-sendrecv-result.png
├── 12-mpi-matrix-source.png
├── 13-mpi-executable-workers.png
└── 14-final-mpi-matrix-result.png
```

## Conclusion

The MPI-based matrix multiplication program was successfully implemented and executed using four MPI processes distributed across a master and three worker nodes.

The experiment demonstrated:

- Multi-node MPI configuration.
- Process-based parallelism.
- MPI communication using send and receive operations.
- Distribution of matrix computation among processes.
- Parallel execution across multiple nodes.
- Verification of the matrix multiplication result.

The final verification value was:

```text
C[0][0] = 4000.00
```

with an execution time of:

```text
287.372540 seconds
```

Thus, the MPI environment and parallel matrix multiplication implementation were successfully verified.