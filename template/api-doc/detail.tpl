$def with (objId, obj, inputList, urlPrefix)
$var title: ${obj.get('name')}
<div style="width:800px;margin:50px auto">
    <div><a href="/api/list">&lt;&lt;接口列表</a><div>&nbsp;</div></div>
    <div class="row">
        接口名称: <pre>${obj.get('name')}</pre>
    </div>
    <div class="row">
        模块(Module.Class): <pre>${obj.get('module')}</pre>
    </div>
    <div class="row">
        接口URL: <pre>${obj.get('url')}</pre>
    </div>
    <div class="row">
        HTTP Method: <pre>${obj.get('method')}</pre>
    </div>
    <div class="row">
        输入参数: <pre>${obj.get('input')}</pre>
        <div id="testarea" style="display:none">
            <form method="${obj.get('method')}" target="_blank" action="${urlPrefix}${obj.get('url')}" enctype="multipart/form-data">
                $for key,tipe,isMust in inputList:
                    <p>
                        ${key}
                        $if not isMust:
                            <small>(可选)</small>
                        $else:
                            <small>(必填)</small>
                        ($tipe): &nbsp;
                        $if tipe == 'file':
                            <input type="file" name="${key}"/>
                        $else:
                            <textarea rows="1" cols="40" name="${key}"></textarea>
                    </p>
                <br/>
                <input type="submit" value="提交测试"/> &nbsp; &nbsp; &nbsp;
                <a href="/param-code.html" target="_blank">参数类型解释</a>
            </form>
            <hr/>
        </div>
         <div>&nbsp; &nbsp; <a href="javascript:void(0)" onclick="$$('#testarea').toggle()">在线测试</a></div>
    </div>
    <div class="row">
        <div id="mdContent"></div>
        <textarea id="contentText" style="display:none">${obj.get('content')}</textarea>
        <script>
            function onload() {
                var converter = new showdown.Converter();
                $$('#mdContent').html(converter.makeHtml($$('#contentText').html()));
            }
        </script>
    </div>
    <div class="row">
        <br/>
        创建者: ${obj.get('creatorName')}
    </div>
    <div>
        <div>&nbsp;</div>
        <div>
            <a href="/api/edit?id=$objId"><button>进入修改页面</button></a>
        </div>
    </div>
</div>
