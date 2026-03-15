# llm_server

[llm_server](https://github.com/code4fukui/llm_server)は、[rinna/youri-7b-gptq](https://huggingface.co/rinna/youri-7b-gptq)モデルを使用したLLM(Large Language Model)APIを提供するサーバーです。

## 必要環境
- Python 3.x
- PyTorch
- Auto-GPTQ
- Flask

## 使い方
1. 必要なライブラリをインストールします:
```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
pip install flask
```
2. サーバーを起動します:
```sh
python3 llm_server.py 5050
```
3. ブラウザで `http://[::]:5050/?p=who` にアクセスするとレスポンスが得られます。

## ライセンス
MIT License