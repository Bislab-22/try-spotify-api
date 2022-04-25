# 環境構築について

## pipでインストールする場合（Dockerなし）
リポジトリのルートで以下を実行
``` bash
pip install -r requirements.txt
pip install torch torchvision torchaudio --extra-index-url https://download.pytorch.org/whl/cu113 (pytorchは今のところ使わないがDockerと合わせるために一応入れておく)
```

## dockerでインストール場合
リポジトリのルートで以下を実行
```bash
docker build -t [イメージ名]
docker run -v [現在のパスの絶対パス]:/volumes -p 80:8080 --name [コンテナ名] -d -it [イメージ名]
docker start [コンテナ名]
```
