$def with (content)
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml" lang="zh-CN">
<head>
    <title>$content.title</title>
    <meta charset='utf-8'>
    <link href='https://dn-maxiang.qbox.me/res-min/themes/marxico.css' rel='stylesheet'/>
    <link rel="stylesheet" href="/static/css/base.css"/>
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap.min.css" rel="stylesheet"/>
    <link href="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/css/bootstrap-theme.min.css" rel="stylesheet"/>
    <link href="/static/css/bootstrap-markdown-editor.css" rel="stylesheet"/>
    <script>
        var onload = null;
    </script>
</head>
<body>
    <div id='preview-contents' class='note-content'>
        <div id="wmd-preview" class="preview-content">
            $:content
        </div>
    </div>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js"></script>
    <script src="http://maxcdn.bootstrapcdn.com/bootstrap/3.3.1/js/bootstrap.min.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/ace/1.1.3/ace.js"></script>
    <script src="http://cdnjs.cloudflare.com/ajax/libs/marked/0.3.2/marked.min.js"></script>

    <script src="/static/js/showdown.min.js"></script>
    <script src="/static/js/bootstrap-markdown-editor.js"></script>

    <script>

        jQuery(document).ready(function($$) {

            $$('#editor').markdownEditor({
                preview: true,
                onPreview: function (content, callback) {
                    callback( marked(content) );
                }
            });

        });
        if (onload) {
            onload();
        }
    </script>
</body>
</html>