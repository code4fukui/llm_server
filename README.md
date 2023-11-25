# llm_server

## setup

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
```

## run the server

```sh
py llm_server.py 5050
```
http://[::]:5050/?p=who
