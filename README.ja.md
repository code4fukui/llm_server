# llm_server

`llm_server` は、大規模言語モデル [rinna/youri-7b-chat-gptq](https://huggingface.co/rinna/youri-7b-chat-gptq) 向けのシンプルなFlaskベースのWeb APIを提供します。

サーバーはGETリクエストを待ち受け、モデルが生成したテキスト補完を返します。

## 要件

- Python 3.x
- CUDA対応のNVIDIA GPUが必要です。

## インストール

以下のコマンドはCUDA 11.8環境用です。異なるバージョンのCUDAを使用する場合はURLを調整してください。

```sh
# PyTorchのインストール
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

# AutoGPTQのインストール
pip install auto-gptq --extra-index-url https://huggingface.github.io/autogptq-index/whl/cu118/

# Flaskのインストール
pip install flask
```

## 使用方法

1.  **サーバーの起動:**

    オプションでポート番号を指定できます。デフォルトは `5050` です。

    ```sh
    python3 llm_server.py 5050
    ```

2.  **APIへのリクエスト:**

    `curl` などのクライアントを使用して、`p` クエリパラメータにプロンプトを送信します。

    ```sh
    curl "http://localhost:5050/?p=What%20is%20a%20Large%20Language%20Model%3F"
    ```

## APIエンドポイント

### `GET /`

指定されたプロンプトに対するテキスト補完を返します。

-   **クエリパラメータ:**
    -   `p` (文字列、必須): モデルに送信するプロンプト。
-   **成功時のレスポンス:**
    -   `Content-Type: text/html; charset=utf-8`
    -   レスポンスボディには、モデルが出力した生の文字列が含まれます。

## 関連

-   [llm_client](https://github.com/code4fukui/llm_client/) - このサーバーとやり取りするためのサンプルクライアント。

## ライセンス

MIT License — [LICENSE](LICENSE) を参照してください。
