# Scripts

[Motomachi](https://motomachi.ryoku.chat/) をビルドするためのスクリプトです。

## 使い方

```
git clone https://github.com/yui87/motomachi-scripts.git make_motomachi
```

```
cd make_motomachi
```

合成に必要なフォントは `setup.sh` の中でダウンロード、展開されます。

```
./setup.sh
```

[FontForge](https://fontforge.org/) をインストールした上で、以下を実行します。

```
fontforge -lang=py -script koruri.py
```
