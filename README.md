# serialmonitor_python
SerialPortMonitor written in Python

一方的に送られてくるコマンドを受信するプログラム。
##Usage
### 1.通信相手の接続とCOM番号の確認
コマンドを送信する機械などをPCに接続する。
Windowsの場合、デバイスマネージャなどでCOM番号を確認する。
例えば見たい機器"COM5"である場合はソースコードの"COM3"となっている部分を以下のように書き換え保存する。

sp = serial.Serial("COM5",timeout=10)

### 2.pythonを以下のように実行する。
>python main.py

添付のarduinoを動かした場合は以下の結果が得られる。
>b'HelloSerialMonitor!HelloSerialMonitor!HelloSerialMonitor!HelloSerialMonitor!HelloSerialMonitor!Hello'


##pyserialのインストール
pythonのライブラリ"pyserial"が必要。

pipの場合は以下のようにしてインストールできる
>pip install pyserial

condaの場合は（管理者権限で）以下のようにしてインストールできる
>conda install pyserial

##動作検証環境
python 3.7.0 (Windows)

##プルリクエスト
まだ不慣れですが送っていただけると嬉しいです。