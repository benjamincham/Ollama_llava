# Backend serving llava using llamacpp

## Setup instructions

### 1. Create Conda environment
```
conda create -n llamacpp_llava python=3.9 -y && conda activate llamacpp_llava
```

### 2. Downloade Model files
Refer to [ggml_llava-v1.5-13b/README.md](ggml_llava-v1.5-13b/README.md)

### 3. Install llama-cpp-server package
For detailed information, checkout [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)

###  &emsp;option A: Install with GPU cuBLAS support (perferred)
```
CMAKE_ARGS="-DLLAMA_CUBLAS=on" FORCE_CMAKE=1 pip install llama-cpp-python[server] --upgrade --no-cache-dir
```

###  &emsp;Option B: Install with CPU only
```
CMAKE_ARGS="-DLLAMA_BLAS=ON -DLLAMA_BLAS_VENDOR=OpenBLAS" pip install llama-cpp-python
```

### 4. Start llamacpp to serve llava
Note: if your GPU runs out of memory, consider lowering '--n_gpu_layers' to a lower number (e.g. 1 instead of 10) <br><br>
For information on parameters to start llama_cpp.server, checkout [llama-cpp-python docs](https://llama-cpp-python.readthedocs.io/en/latest/api-reference/)
```
python -m llama_cpp.server --model ./ggml_llava-v1.5-13b/ggml-model-q4_k.gguf --clip_model_path ./ggml_llava-v1.5-13b/mmproj-model-f16.gguf --chat_format llava-1-5 --n_gpu_layers 10 --n_threads 16
```

### 5. Examples to performce inference using llama-cpp-server

###  &emsp;5a: Inference using image file
Refer to [code](example/inference_local_file.py), change the image_path to point to your image
```
python ./example/inference_local_file.py
```

###  &emsp;5b: Inference using image url
Refer to [code](example/inference_remote_url.py)
```
python ./example/inference_remote_url.py
```