# Lab-03: AES and DES Encryption

## Objective

To implement **AES (Advanced Encryption Standard)** and **DES (Data Encryption Standard)** symmetric encryption algorithms in Python using the **PyCryptodome** cryptographic library.

The experiment also performs a performance analysis of AES and DES using different types of input data such as **text, image, and audio**.

---

## Technologies Used

- Python
- PyCryptodome
- AES
- DES
- CBC (Cipher Block Chaining)
- Matplotlib
- CSV

---

# 1. AES Encryption

AES (Advanced Encryption Standard) is a symmetric-key block cipher in which the same secret key is used for encryption and decryption.

## AES Implementation

The AES program:

1. Takes a message dynamically from the user.
2. Generates a random 128-bit AES key.
3. Generates a random Initialization Vector (IV).
4. Pads the message according to the AES block size.
5. Encrypts the message using AES in CBC mode.
6. Displays the encrypted ciphertext.
7. Decrypts the ciphertext using the same key and IV.
8. Displays the original message.

## Run AES

From the `Lab-03` directory:

```bash
python aes.py
```

## AES Flow

```text
User Message
     |
     v
   Padding
     |
     v
AES Encryption
     |
     v
Ciphertext
     |
     v
AES Decryption
     |
     v
Original Message
```

---

# 2. DES Encryption

DES (Data Encryption Standard) is a symmetric-key block cipher in which the same key is used for encryption and decryption.

## DES Implementation

The DES program:

1. Takes a message dynamically from the user.
2. Generates a DES key.
3. Generates an Initialization Vector (IV).
4. Pads the message.
5. Encrypts the message using DES in CBC mode.
6. Displays the encrypted ciphertext.
7. Decrypts the ciphertext.
8. Displays the original message.

## Run DES

From the `Lab-03` directory:

```bash
python des.py
```

## DES Flow

```text
User Message
     |
     v
   Padding
     |
     v
DES Encryption
     |
     v
Ciphertext
     |
     v
DES Decryption
     |
     v
Original Message
```

> **Note:** DES is an older encryption standard and is no longer considered secure for modern applications. It is implemented here for educational and performance comparison purposes.

---

# 3. Performance Analysis

The performance analysis compares AES and DES using different types of input data.

### Input Types

- Text
- Image
- Audio

The input files are stored in:

```text
performance/
└── inputs/
    ├── sample.txt
    ├── sample.jpg
    └── sample.wav
```

---

# 4. Performance Metrics

The following parameters are measured during the experiment.

## Encryption Latency

Time required to encrypt the input data.

```text
Encryption Latency =
Encryption End Time - Encryption Start Time
```

## Decryption Latency

Time required to decrypt the encrypted data.

```text
Decryption Latency =
Decryption End Time - Decryption Start Time
```

## Encryption Throughput

Amount of data encrypted per unit of time.

```text
Encryption Throughput =
Input Size / Encryption Time
```

## Decryption Throughput

Amount of data decrypted per unit of time.

```text
Decryption Throughput =
Input Size / Decryption Time
```

## CPU Usage

Measures CPU utilization during the encryption and decryption operations.

## Memory Usage

Measures memory consumed during the encryption and decryption operations.

## Ciphertext Size

Measures the size of the encrypted output.

## Encryption Overhead

Measures the additional size introduced by encryption.

```text
Overhead =
((Encrypted Size - Original Size) / Original Size) × 100
```

---

# 5. Performance Analysis Program

The performance analysis program is located at:

```text
performance/performance_analysis.py
```

It reads the input files from:

```text
performance/inputs/
```

and stores the generated results in:

```text
performance/results/
```

---

# 6. Running Performance Analysis

From the `Lab-03` directory, first enter the performance directory:

```bash
cd performance
```

Then run:

```bash
python performance_analysis.py
```

Alternatively, if you are already inside the `performance` directory:

```bash
python performance_analysis.py
```

The program processes:

```text
sample.txt
sample.jpg
sample.wav
```

and measures the performance of AES and DES.

---

# 7. Results

The generated results are stored in:

```text
performance/results/
```

The results include:

```text
results/
├── aes_des_performance.csv
├── cpu_usage.png
├── decryption_latency.png
├── decryption_throughput.png
├── encryption_latency.png
├── encryption_throughput.png
└── memory_usage.png
```

### CSV Results

`aes_des_performance.csv` contains the numerical performance measurements for AES and DES.

### Graphs

The generated graphs show comparisons of:

- Encryption latency
- Decryption latency
- Encryption throughput
- Decryption throughput
- CPU usage
- Memory usage

---

# 8. Project Structure

```text
Lab-03/
│
├── README.md
│
├── aes.py
│
├── des.py
│
└── performance/
    │
    ├── performance_analysis.py
    │
    ├── inputs/
    │   ├── sample.txt
    │   ├── sample.jpg
    │   └── sample.wav
    │
    └── results/
        ├── aes_des_performance.csv
        ├── cpu_usage.png
        ├── decryption_latency.png
        ├── decryption_throughput.png
        ├── encryption_latency.png
        ├── encryption_throughput.png
        └── memory_usage.png
```

---

# 9. AES vs DES

| Parameter | AES | DES |
|---|---|---|
| Full Form | Advanced Encryption Standard | Data Encryption Standard |
| Type | Symmetric Block Cipher | Symmetric Block Cipher |
| Key Size Used | 128 bits | 64 bits |
| Effective Key Size | 128 bits | 56 bits |
| Block Size | 128 bits | 64 bits |
| Mode Used | CBC | CBC |
| IV Size | 128 bits | 64 bits |
| Security Status | Modern standard | Deprecated |
| Purpose in this Lab | Encryption and performance analysis | Educational comparison |

---

# 10. Conclusion

AES and DES were implemented in Python using the **PyCryptodome** cryptographic library.

The implementations demonstrate the complete symmetric encryption process:

```text
Plaintext
    |
    v
Encryption
    |
    v
Ciphertext
    |
    v
Decryption
    |
    v
Plaintext
```

A performance analysis was also performed using **text, image, and audio inputs**.

The algorithms were evaluated using:

- Encryption latency
- Decryption latency
- Encryption throughput
- Decryption throughput
- CPU usage
- Memory usage
- Ciphertext size
- Encryption overhead

The generated CSV file and graphs provide the measured performance results for AES and DES.