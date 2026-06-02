import subprocess

steps = [
    "python3 src/validation/basic_quality_checks.py",
    "python3 src/profiling/profile_dataset.py",
    "python3 src/profiling/anomaly_detection.py",
    "python3 src/drift/drift_detection.py",
]

for step in steps:
    print(f"\nRunning: {step}")
    result = subprocess.run(step, shell=True)

    if result.returncode != 0:
        print(f"Failed: {step}")
        break
else:
    print("\nData Quality pipeline completed successfully.")
