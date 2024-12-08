import pynvml

def get_gpu_usage():
    pynvml.nvmlInit()  # Initialize NVML
    device_count = pynvml.nvmlDeviceGetCount()  # Get number of GPUs
    for i in range(device_count):
        handle = pynvml.nvmlDeviceGetHandleByIndex(i)  # Get handle for GPU
        gpu_name = pynvml.nvmlDeviceGetName(handle)
        mem_info = pynvml.nvmlDeviceGetMemoryInfo(handle)  # Memory usage
        utilization = pynvml.nvmlDeviceGetUtilizationRates(handle)  # GPU usage
        print(f"GPU {i}: {gpu_name}")
        print(f"  Memory: {mem_info.used / 1024**2:.2f} MB / {mem_info.total / 1024**2:.2f} MB")
        print(f"  GPU Utilization: {utilization.gpu}%")
        print(f"  Memory Utilization: {utilization.memory}%")
    pynvml.nvmlShutdown()  # Shutdown NVML

get_gpu_usage()
