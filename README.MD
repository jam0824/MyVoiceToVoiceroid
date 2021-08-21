# はじめに
これは音声認識をして、その認識した言葉をvoiceroidに話させるプログラムです。

（動画 https://twitter.com/mty_mno/status/1428709646458527750 ）

現在は"VOICEROID2 紲星あかり"のみで動作を確認しています。

他のものでも、恐らくは"model_appium"の"TextBox"と書かれている部分（文字を入力するボックスを指定する場所）と"再生"と書かれている部分（音声の再生ボタンの場所）を変更すれば使えるのではないかと思っています。

このプログラムはpythonがインストールされていること、voiceroidがインストールされていることが前提です。

プログラムの説明は以下のブログ記事に記載しています。

https://testerchan.hatenadiary.com/entry/2021/08/21/133238


# 準備
## コードを実行するためには以下のものをインストールしてください
### ■WinAppDriverのインストール
以下から"WinAppDriver"をダウンロードし、ダウンロードしたWindowsApplicationDriver-xxxxx.exeを実行しインストールしてください。
https://github.com/Microsoft/WinAppDriver/releases



### ■chromedriverの配置
以下から"chromedriver"をダウンロードし、コードが置いてあるフォルダの中にchromedriver.exeを入れてください。

chromedriverのバージョンはgoogle chromeのバージョンと同じものをダウンロードしてください。

https://sites.google.com/a/chromium.org/chromedriver/



### ■seleniumのインストール
以下をコマンドプロンプトなどで実行し、インストールしてください。

> `pip install selenium`



### ■appiumのインストール
以下をコマンドプロンプトなどで実行し、インストールしてください。

> `pip install Appium-Python-Client`



## Windowsの開発者モードをオン
windowsの設定を開き、"設定の検索"部分に`開発者向け`と入力し検索してください。

そうすると"開発者向け設定"とありますのでそれを選択してください。

"開発者モード"という部分がありますのでそれを`オン`にしてください。

# コードの変更

## ■index.htmlのおいてあるパスの変更
`exec_realtime_voiceroid.py`の`file:///D:/xampp/htdocs/音声リアルタイムボイスロイド変換/index.html`部分をご自分がコードを置いているところに変更してください。

## ■voiceroidのおいてあるパスの変更
`exec_realtime_voiceroid.py`の`C:\Program Files (x86)\AHS\VOICEROID2\VoiceroidEditor.exe`部分をご自分がvoiceroidを置いているところに変更してください。


# 実行

## 実行前にWinAppDriverとvoiceroidを起動しておいてください
### ■WinAppDriverの起動
コマンドプロンプトを開いて以下を入力してください。もしインストールフォルダを変えていたら替えた場所で入力してください。

> `"C:\Program Files\Windows Application Driver\WinAppDriver.exe"`

以下のように表示されたら成功です。

> Windows Application Driver listening for requests at: http://127.0.0.1:4723/
? Press ENTER to exit.

### ■voiceroidの実行
普通に実行してください。


## コードの実行
コマンドプロンプトでコードがあるフォルダに移動し、以下を入力しコードを実行してください。

> `python exec_realtime_voiceroid.py`

実行するとchromeが立ち上がります。

マイクの許可を求めてくるので許可してください。

後は入力待ち状態になっていますので話しかけてください。

chrome側で音声入力された後にvoiceroidの入力画面に文字が入力され、自動的に再生ボタンが押されて再生します。

再生ボタンが自動敵に押される際はマウスの制御が奪われますのでご注意ください。

終了時は「終了」と話すと終了します。

また1分ほど放置すると勝手に音声認識が終わってしまうのでご注意ください。


# 要素の調べ方と変更方法

voiceroid2以外を使うときは、入力するボックスと、再生ボタンを認識させる必要があるかと思います。（そのまま使えるかもだけど）

## 入力ボックスのAutomationIdの調べ方
voiceroidを起動した後、windowsで"inspect.exe"を検索し起動します。（windowsにデフォルトで入っているアプリです）

inspect.exeを起動した後、voiceroidの入力ボックスをクリックします。

クリックするとinspect.exeの右側に情報が表示されます。

そこの`AutomationId`を確認してください。

そこに記載されている文字列が`TextBox`ならそのまま動きますし、そうでなければ`model_appium.py`の`TextBox`と書かれている部分をAutomationIdに記載されている文字列に変更してください。

## 再生ボタンのNameの調べ方

先ほどと同様inspect.exeで調べます。

再生ボタンを押すとinspect.exeでその場所の情報を表示してくれます。

そのとき、左側のリストに"再生テキスト"という場所があると思うので、それを選択してください。

そこに`Name`という項目がありますからそこを確認してください。

それが`再生`ならそのまま動きますし、そうでなければ`model_appium.py`の`再生`と書かれている部分をNameに記載されている文字列に変更してください。

