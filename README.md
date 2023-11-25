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

## reference

- [rinnaの新AI「youri-7b-chat-gptq」の魅力 | ジコログ](https://self-development.info/rinna%E3%81%AE%E6%96%B0ai%E3%80%8Cyouri-7b-chat-gptq%E3%80%8D%E3%81%AE%E9%AD%85%E5%8A%9B/)
