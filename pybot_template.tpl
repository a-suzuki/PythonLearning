<html>
    <head>
        <meta charset="utf-8" />
        <script type="text/javascript" src="/js/jquery.min.js"></script>
        <script type="text/javascript" src="/js/bootstrap.min.js"></script>
             
        <link rel="stylesheet" href="/css/bootstrap.min.css" />
        <link rel="stylesheet" href="/css/bootstrap-theme.min.css" />
    </head>
    <body>
        <div class="jumbotron">
            <div class="container">
                <h1>pybot Webアプリケーション</h1>
                <form method="post" action="/hello" class="form-inline">
                    <div class="form-group">
                        <label for="inputText">メッセージを入力してください: </label>
                        <input type="text" class="form-control" id=inputText name="input_text">
                        <button type="submit" class="btn btn-primary">送信</button>
                    </div>
                </form>
                <ul>
                    <li>入力メッセージ: {{input_text}}</li>
                    <li>pybotからの応答メッセージ: {{output_text}}</li>
                </ul>
            </div>
        </div>
    </body>
</html>
