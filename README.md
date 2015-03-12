# Fabhelper

## 概要
fabricでのインストールや設定変更、デプロイの冪等性保証をサポートするfabricラッパー

## 動作確認
動作確認は[Vagrantのbox配布サイト](http://www.vagrantbox.es/)から取得した以下の環境で実施  
+ CentOS6.5.3_x86_64
+ 

## インストール
とりあえずcloneしてパス通せば良いんじゃあ無いかな

## 作成背景
fabricを使う場面が多く、処理の重複が多かったため  
車輪の再発明が好きなんだからしょうがないじゃん

## ディレクトリ構成
```Bash
$ tree

.
├── README.md
├── Vagrantfile
├── fabfile   # 呼び出しサンプル
│   ├── __init__.py   # タスク定義元
│   ├── cron.py
│   ├──  .
│   ├──  .
│   ├──  .
│   ├── yum.py
│   └── fabhelper   # 実体
│   　   ├── __init__.py
│   　   ├── cron.py
│   　   ├──  .
│   　   ├──  .
│   　   ├──  .
│   　   └── yum.py
└── localfiles   # ローカルから転送するファイルサンプル
    └── put_to_directory.sh
```

## タスク一覧
```Bash
$ fab -l                                                                                                                                                                                             master
Available commands:

    all
    git.all
    git.clone
    date.all
    date.now
	 .
	 .
	 .
    yum.update
```

## モジュール概要

### cron
cronの設定を行う  
+ ローカルのshを転送する
+ shをechoで吐き出す

### date
現在時刻を取得する
+ デフォルトフォーマット(yyyy-mm-dd_hh:mm:ss)
+ フォーマット指定

### file
ファイル操作に関するUtil集
+ sedラッパー
+ バックアップと差分出力アノテーション
+ リンク張り替え
+ ファイル存在確認
+ 行存在確認

### git
git操作に関するUtil集
+ clone
+ ブランチ指定clone

### log
サーバ内にログを作成する
+ 成功ログ書き込み
+ 成功ログ読み込み
+ 失敗ログ書き込み
+ 失敗ログ読み込み

### result
色つきでコマンドの結果を出力
+ 正常
+ 異常
+ 冪統制保証のためのガード
+ 各デフォルト色の変更
+ 太字

### service
サービスの有効無効の設定や再起動等のUtil集
+ 自動起動の有効化
+ 自動起動の無効化
+ サービスの起動
+ サービスの停止
+ 自動起動の有効化とサービスの起動
+ 自動起動の無効化とサービスの停止
+ サービスの再起動
+ 設定ファイル再読込

### yum
yum操作に関するUtil集
+ epel, remi, rpm-forge各リポジトリの追加
+ インストール
+ リポジトリ指定インストール
+ アップデート
+ yum-cronの設定
