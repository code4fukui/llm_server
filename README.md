# llm_server

llm_server provides a LLM (Large Language Model) API using the [rinna/youri-7b-gptq](https://huggingface.co/rinna/youri-7b-gptq) model.

## Setup

```sh
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/
pip install flask
```

## Usage

Run the server:

```sh
python3 llm_server.py 5050
```

Then access the API at `http://[::]:5050/?p=who`

## Related

- [llm_client](https://github.com/code4fukui/llm_client/)

## License

MIT License