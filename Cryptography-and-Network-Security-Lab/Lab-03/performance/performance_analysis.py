import os
import time
import csv
import psutil
import tracemalloc
import matplotlib.pyplot as plt

from Crypto.Cipher import AES, DES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


# ============================================================
# CONFIGURATION
# ============================================================

REPEAT = 5

INPUT_FILES = {
    "Text": "inputs/sample.txt",
    "Image": "inputs/sample.jpg",
    "Audio": "inputs/sample.wav"
}

# AES-128 key and IV
AES_KEY = get_random_bytes(16)
AES_IV = get_random_bytes(16)

# DES key and IV
DES_KEY = get_random_bytes(8)
DES_IV = get_random_bytes(8)


# ============================================================
# RESULT STORAGE
# ============================================================

results = []


# ============================================================
# FUNCTION TO MEASURE AES
# ============================================================

def measure_aes(data):

    encryption_times = []
    decryption_times = []
    encryption_memory = []
    decryption_memory = []
    encryption_cpu = []
    decryption_cpu = []

    encrypted_data = None

    # --------------------------------------------------------
    # Prepare padded data
    # --------------------------------------------------------

    padded_data = pad(data, AES.block_size)

    # --------------------------------------------------------
    # ENCRYPTION
    # --------------------------------------------------------

    for _ in range(REPEAT):

        tracemalloc.start()

        process = psutil.Process(os.getpid())

        start_cpu = process.cpu_percent(None)

        start_time = time.perf_counter()

        cipher = AES.new(
            AES_KEY,
            AES.MODE_CBC,
            AES_IV
        )

        encrypted_data = cipher.encrypt(padded_data)

        end_time = time.perf_counter()

        end_cpu = process.cpu_percent(None)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        encryption_times.append(
            end_time - start_time
        )

        encryption_memory.append(
            peak / (1024 * 1024)
        )

        encryption_cpu.append(
            end_cpu
        )

    # --------------------------------------------------------
    # DECRYPTION
    # --------------------------------------------------------

    for _ in range(REPEAT):

        tracemalloc.start()

        process = psutil.Process(os.getpid())

        start_time = time.perf_counter()

        cipher = AES.new(
            AES_KEY,
            AES.MODE_CBC,
            AES_IV
        )

        decrypted_data = cipher.decrypt(
            encrypted_data
        )

        decrypted_data = unpad(
            decrypted_data,
            AES.block_size
        )

        end_time = time.perf_counter()

        end_cpu = process.cpu_percent(None)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        decryption_times.append(
            end_time - start_time
        )

        decryption_memory.append(
            peak / (1024 * 1024)
        )

        decryption_cpu.append(
            end_cpu
        )

    # --------------------------------------------------------
    # AVERAGES
    # --------------------------------------------------------

    avg_encryption_time = (
        sum(encryption_times) / REPEAT
    )

    avg_decryption_time = (
        sum(decryption_times) / REPEAT
    )

    avg_encryption_memory = (
        sum(encryption_memory) / REPEAT
    )

    avg_decryption_memory = (
        sum(decryption_memory) / REPEAT
    )

    avg_encryption_cpu = (
        sum(encryption_cpu) / REPEAT
    )

    avg_decryption_cpu = (
        sum(decryption_cpu) / REPEAT
    )

    # --------------------------------------------------------
    # THROUGHPUT
    # --------------------------------------------------------

    data_size_mb = len(data) / (1024 * 1024)

    encryption_throughput = (
        data_size_mb / avg_encryption_time
    )

    decryption_throughput = (
        data_size_mb / avg_decryption_time
    )

    return {
        "enc_time": avg_encryption_time,
        "dec_time": avg_decryption_time,
        "enc_throughput": encryption_throughput,
        "dec_throughput": decryption_throughput,
        "enc_memory": avg_encryption_memory,
        "dec_memory": avg_decryption_memory,
        "enc_cpu": avg_encryption_cpu,
        "dec_cpu": avg_decryption_cpu,
        "encrypted_size": len(encrypted_data)
    }


# ============================================================
# FUNCTION TO MEASURE DES
# ============================================================

def measure_des(data):

    encryption_times = []
    decryption_times = []
    encryption_memory = []
    decryption_memory = []
    encryption_cpu = []
    decryption_cpu = []

    encrypted_data = None

    # --------------------------------------------------------
    # Prepare padded data
    # --------------------------------------------------------

    padded_data = pad(data, DES.block_size)

    # --------------------------------------------------------
    # ENCRYPTION
    # --------------------------------------------------------

    for _ in range(REPEAT):

        tracemalloc.start()

        process = psutil.Process(os.getpid())

        start_time = time.perf_counter()

        cipher = DES.new(
            DES_KEY,
            DES.MODE_CBC,
            DES_IV
        )

        encrypted_data = cipher.encrypt(
            padded_data
        )

        end_time = time.perf_counter()

        end_cpu = process.cpu_percent(None)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        encryption_times.append(
            end_time - start_time
        )

        encryption_memory.append(
            peak / (1024 * 1024)
        )

        encryption_cpu.append(
            end_cpu
        )

    # --------------------------------------------------------
    # DECRYPTION
    # --------------------------------------------------------

    for _ in range(REPEAT):

        tracemalloc.start()

        process = psutil.Process(os.getpid())

        start_time = time.perf_counter()

        cipher = DES.new(
            DES_KEY,
            DES.MODE_CBC,
            DES_IV
        )

        decrypted_data = cipher.decrypt(
            encrypted_data
        )

        decrypted_data = unpad(
            decrypted_data,
            DES.block_size
        )

        end_time = time.perf_counter()

        end_cpu = process.cpu_percent(None)

        current, peak = tracemalloc.get_traced_memory()

        tracemalloc.stop()

        decryption_times.append(
            end_time - start_time
        )

        decryption_memory.append(
            peak / (1024 * 1024)
        )

        decryption_cpu.append(
            end_cpu
        )

    # --------------------------------------------------------
    # AVERAGES
    # --------------------------------------------------------

    avg_encryption_time = (
        sum(encryption_times) / REPEAT
    )

    avg_decryption_time = (
        sum(decryption_times) / REPEAT
    )

    avg_encryption_memory = (
        sum(encryption_memory) / REPEAT
    )

    avg_decryption_memory = (
        sum(decryption_memory) / REPEAT
    )

    avg_encryption_cpu = (
        sum(encryption_cpu) / REPEAT
    )

    avg_decryption_cpu = (
        sum(decryption_cpu) / REPEAT
    )

    # --------------------------------------------------------
    # THROUGHPUT
    # --------------------------------------------------------

    data_size_mb = len(data) / (1024 * 1024)

    encryption_throughput = (
        data_size_mb / avg_encryption_time
    )

    decryption_throughput = (
        data_size_mb / avg_decryption_time
    )

    return {
        "enc_time": avg_encryption_time,
        "dec_time": avg_decryption_time,
        "enc_throughput": encryption_throughput,
        "dec_throughput": decryption_throughput,
        "enc_memory": avg_encryption_memory,
        "dec_memory": avg_decryption_memory,
        "enc_cpu": avg_encryption_cpu,
        "dec_cpu": avg_decryption_cpu,
        "encrypted_size": len(encrypted_data)
    }


# ============================================================
# MAIN PERFORMANCE ANALYSIS
# ============================================================

for input_type, file_path in INPUT_FILES.items():

    print("\n========================================")
    print(input_type)
    print("========================================")

    if not os.path.exists(file_path):
        print("File not found:", file_path)
        continue

    # --------------------------------------------------------
    # Read file as binary
    # --------------------------------------------------------

    with open(file_path, "rb") as file:
        data = file.read()

    original_size = len(data)

    print(
        "Original Size:",
        round(original_size / (1024 * 1024), 4),
        "MB"
    )

    # --------------------------------------------------------
    # AES
    # --------------------------------------------------------

    aes_result = measure_aes(data)

    # --------------------------------------------------------
    # DES
    # --------------------------------------------------------

    des_result = measure_des(data)

    # --------------------------------------------------------
    # Calculate overhead
    # --------------------------------------------------------

    aes_overhead = (
        (aes_result["encrypted_size"] - original_size)
        / original_size
    ) * 100

    des_overhead = (
        (des_result["encrypted_size"] - original_size)
        / original_size
    ) * 100

    # --------------------------------------------------------
    # Store results
    # --------------------------------------------------------

    results.append([
        input_type,
        original_size,

        aes_result["enc_time"],
        aes_result["dec_time"],

        aes_result["enc_throughput"],
        aes_result["dec_throughput"],

        aes_result["enc_memory"],
        aes_result["dec_memory"],

        aes_result["enc_cpu"],
        aes_result["dec_cpu"],

        aes_result["encrypted_size"],
        aes_overhead,

        des_result["enc_time"],
        des_result["dec_time"],

        des_result["enc_throughput"],
        des_result["dec_throughput"],

        des_result["enc_memory"],
        des_result["dec_memory"],

        des_result["enc_cpu"],
        des_result["dec_cpu"],

        des_result["encrypted_size"],
        des_overhead
    ])

    # --------------------------------------------------------
    # Display results
    # --------------------------------------------------------

    print("\nAES")
    print("----------------------------------------")

    print(
        "Encryption Latency :",
        round(aes_result["enc_time"], 6),
        "seconds"
    )

    print(
        "Decryption Latency :",
        round(aes_result["dec_time"], 6),
        "seconds"
    )

    print(
        "Encryption Throughput :",
        round(aes_result["enc_throughput"], 2),
        "MB/s"
    )

    print(
        "Decryption Throughput :",
        round(aes_result["dec_throughput"], 2),
        "MB/s"
    )

    print(
        "Encryption Memory :",
        round(aes_result["enc_memory"], 4),
        "MB"
    )

    print(
        "Decryption Memory :",
        round(aes_result["dec_memory"], 4),
        "MB"
    )

    print(
        "Encryption CPU :",
        round(aes_result["enc_cpu"], 2),
        "%"
    )

    print(
        "Decryption CPU :",
        round(aes_result["dec_cpu"], 2),
        "%"
    )

    print(
        "Encrypted Size :",
        round(
            aes_result["encrypted_size"] / (1024 * 1024),
            4
        ),
        "MB"
    )

    print(
        "Overhead :",
        round(aes_overhead, 4),
        "%"
    )

    print("\nDES")
    print("----------------------------------------")

    print(
        "Encryption Latency :",
        round(des_result["enc_time"], 6),
        "seconds"
    )

    print(
        "Decryption Latency :",
        round(des_result["dec_time"], 6),
        "seconds"
    )

    print(
        "Encryption Throughput :",
        round(des_result["enc_throughput"], 2),
        "MB/s"
    )

    print(
        "Decryption Throughput :",
        round(des_result["dec_throughput"], 2),
        "MB/s"
    )

    print(
        "Encryption Memory :",
        round(des_result["enc_memory"], 4),
        "MB"
    )

    print(
        "Decryption Memory :",
        round(des_result["dec_memory"], 4),
        "MB"
    )

    print(
        "Encryption CPU :",
        round(des_result["enc_cpu"], 2),
        "%"
    )

    print(
        "Decryption CPU :",
        round(des_result["dec_cpu"], 2),
        "%"
    )

    print(
        "Encrypted Size :",
        round(
            des_result["encrypted_size"] / (1024 * 1024),
            4
        ),
        "MB"
    )

    print(
        "Overhead :",
        round(des_overhead, 4),
        "%"
    )


# ============================================================
# SAVE RESULTS TO CSV
# ============================================================

os.makedirs("results", exist_ok=True)

csv_file = "results/aes_des_performance.csv"

headers = [
    "Input Type",
    "Original Size (bytes)",

    "AES Encryption Latency (s)",
    "AES Decryption Latency (s)",

    "AES Encryption Throughput (MB/s)",
    "AES Decryption Throughput (MB/s)",

    "AES Encryption Memory (MB)",
    "AES Decryption Memory (MB)",

    "AES Encryption CPU (%)",
    "AES Decryption CPU (%)",

    "AES Encrypted Size (bytes)",
    "AES Overhead (%)",

    "DES Encryption Latency (s)",
    "DES Decryption Latency (s)",

    "DES Encryption Throughput (MB/s)",
    "DES Decryption Throughput (MB/s)",

    "DES Encryption Memory (MB)",
    "DES Decryption Memory (MB)",

    "DES Encryption CPU (%)",
    "DES Decryption CPU (%)",

    "DES Encrypted Size (bytes)",
    "DES Overhead (%)"
]


with open(
    csv_file,
    "w",
    newline=""
) as file:

    writer = csv.writer(file)

    writer.writerow(headers)

    writer.writerows(results)


print("\n========================================")
print("Results saved to:")
print(csv_file)
print("========================================")


# ============================================================
# GRAPH 1: ENCRYPTION LATENCY
# ============================================================

input_types = [row[0] for row in results]

aes_enc_latency = [row[2] for row in results]
des_enc_latency = [row[12] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_enc_latency,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_enc_latency,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("Encryption Latency (seconds)")
plt.title("AES vs DES Encryption Latency")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/encryption_latency.png",
    dpi=300
)

plt.show()


# ============================================================
# GRAPH 2: DECRYPTION LATENCY
# ============================================================

aes_dec_latency = [row[3] for row in results]
des_dec_latency = [row[13] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_dec_latency,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_dec_latency,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("Decryption Latency (seconds)")
plt.title("AES vs DES Decryption Latency")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/decryption_latency.png",
    dpi=300
)

plt.show()


# ============================================================
# GRAPH 3: ENCRYPTION THROUGHPUT
# ============================================================

aes_enc_throughput = [row[4] for row in results]
des_enc_throughput = [row[14] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_enc_throughput,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_enc_throughput,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("Encryption Throughput (MB/s)")
plt.title("AES vs DES Encryption Throughput")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/encryption_throughput.png",
    dpi=300
)

plt.show()


# ============================================================
# GRAPH 4: DECRYPTION THROUGHPUT
# ============================================================

aes_dec_throughput = [row[5] for row in results]
des_dec_throughput = [row[15] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_dec_throughput,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_dec_throughput,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("Decryption Throughput (MB/s)")
plt.title("AES vs DES Decryption Throughput")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/decryption_throughput.png",
    dpi=300
)

plt.show()


# ============================================================
# GRAPH 5: MEMORY USAGE
# ============================================================

aes_memory = [row[6] for row in results]
des_memory = [row[17] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_memory,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_memory,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("Memory Usage (MB)")
plt.title("AES vs DES Memory Usage")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/memory_usage.png",
    dpi=300
)

plt.show()


# ============================================================
# GRAPH 6: CPU USAGE
# ============================================================

aes_cpu = [row[8] for row in results]
des_cpu = [row[19] for row in results]

plt.figure(figsize=(8, 5))

plt.plot(
    input_types,
    aes_cpu,
    marker="o",
    label="AES"
)

plt.plot(
    input_types,
    des_cpu,
    marker="o",
    label="DES"
)

plt.xlabel("Input Type")
plt.ylabel("CPU Usage (%)")
plt.title("AES vs DES CPU Usage")
plt.legend()
plt.grid(True)
plt.tight_layout()

plt.savefig(
    "results/cpu_usage.png",
    dpi=300
)

plt.show()