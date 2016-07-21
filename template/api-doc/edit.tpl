$def with (objId, obj)
$var title: 新增或修改接口
<div style="width:800px;margin:50px auto">
    <div><a href="/api/list">&lt;&lt;接口列表</a></div>
    $if objId:
        <h3>修改接口</h3>
    $else:
        <h3>新增接口</h3>
    <form method="post" class="form-inline" onSubmit="return onSubmitForm(this)">
        <div class="row">
            <div class="formLeft">接口名称</div>
            <input type="text" class="form-control" name="name" placeholder="例如: 新增或更新店铺" value="${obj.get('name')}"/>
        </div>
        <div class="row">
            <div class="formLeft">模块(Module.Class)</div>
            <input type="text" class="form-control" name="module" placeholder="例如: boss.shop.Save" value="${obj.get('module')}"/>
        </div>
        <div class="row">
            <div class="formLeft">接口URL</div>
            <input type="text" class="form-control" name="url" placeholder="例如: /shop/save" value="${obj.get('url')}"/>
        </div>
        <div class="row">
            <div class="formLeft">HTTP Method</div>
            <input type="text" class="form-control" name="method" placeholder="GET或POST或DELETE" value="${obj.get('method')}"/>
        </div>
        <div class="row">
            <div class="formLeft">输入参数</div>
            <input type="text" class="form-control" name="input" style='width:660px' placeholder="例如: id?, name, address, phone" value="${obj.get('input')}"/>
        </div>
        <div class="row">
            <br/>
            <div class="formLeft">内容(Markdown格式)</div>
            <textarea name="content" id="editor">${obj.get('content')}</textarea>
        </div>
        <div>
            <br/><input type="submit" value="新增或修改"/>
        </div>
    </form>
    <script>
        function onSubmitForm(item) {
            $$.post('/api/save', {
                name:item.name.value,
                module:item.module.value,
                url:item.url.value,
                method:item.method.value,
                input:item.input.value,
                content:$$('#editor').val(),
                $if objId:
                    id: '${objId}',
            }, function(data) {
                if (data.code != 0) {
                    alert(JSON.stringify(data));
                } else {
                    $if objId:
                        window.location.href = '/api/detail?id=$objId';
                    $else:
                        window.location.href = '/api/list';
                }
            });
            return false;
        }
    </script>
</div>
