$def with (lst)
$var title: 接口列表
<div style="width:800px;margin:100px auto">
    $for r in lst:
        <div class="row">
            ${r.get('module')} &nbsp; <a href="/api/detail?id=${r.id}">${r.get('name')}</a>
        </div>
    <div class="row">
        <br/>
        <a href="/api/edit"><button>新增接口</button></a>
    </div>
    <div>
        <br/>
        <a href="/setting">设置</a>
    </div>
</div>