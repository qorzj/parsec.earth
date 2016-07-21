$def with (urlPrefix)
$var title: 系统设置
<div style="width:800px;margin:100px auto">
    <div>
        <form method="post">
            <span>测试链接前缀:</span><br/>
            <input type="text" name="prefix" style="width:400px" value="${urlPrefix}"/>
            <br/><br/>
            <input type="submit" value="修改测试链接前缀"/>
        </form>
        <p>&nbsp;</p><p>&nbsp;</p>
        <p>常用测试前缀:</p>
        <p>https://lightyear.leanapp.cn</p>
        <p>http://localhost:3000</p>
    </div>
</div>