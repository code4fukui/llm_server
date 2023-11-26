# llm_server

- llm_server provides LLM API by [rinna/youri-7b-gptq](https://huggingface.co/rinna/youri-7b-gptq)

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

## related

- [llm_client](https://github.com/code4fukui/llm_client/)

## reference

- [rinnaの新AI「youri-7b-chat-gptq」の魅力 | ジコログ](https://self-development.info/rinna%E3%81%AE%E6%96%B0ai%E3%80%8Cyouri-7b-chat-gptq%E3%80%8D%E3%81%AE%E9%AD%85%E5%8A%9B/)
- [8GB RTX3060TiでOK、PythonでローカルLLMのCORS対応APIサーバー＆JSクライアント](https://fukuno.jig.jp/4140)
