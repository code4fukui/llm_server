# llm_server

> 日本語のREADMEはこちらです: [README.ja.md](README.ja.md)

`llm_server` provides a simple Flask-based web API for the [rinna/youri-7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq) Large Language Model.

The server listens for GET requests and returns model-generated text completions.

## Requirements

- Python 3.x
- An NVIDIA GPU with CUDA support is required.

## Installation

The following commands are for a CUDA 11.8 environment. Adjust the URLs if you are using a different version of CUDA.

```sh
# Install PyTorch
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# Install AutoGPTQ
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/

# Install Flask
pip install flask
```

## Usage

1.  **Start the server:**

    You can specify an optional port number. The default is `5050`.

    ```sh
    python3 llm_server.py 5050
    ```

2.  **Query the API:**

    Use a client like `curl` to send a prompt to the `p` query parameter.

    ```sh
    curl "http://localhost:5050/?p=What%20is%20a%20Large%20Language%20Model%3F"
    ```

## API Endpoint

### `GET /`

Returns a text completion for a given prompt.

-   **Query Parameter:**
    -   `p` (string, required): The prompt to send to the model.
-   **Success Response:**
    -   `Content-Type: text/html; charset=utf-8`
    -   The response body contains the raw string output from the model.

## Related

-   [llm_client](https://github.com/code4fukui/llm_client/) - A sample client to interact with this server.

## License

MIT License — see [LICENSE](LICENSE).