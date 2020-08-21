var data = {}  
data = $('#login-form').serialize();    
$.ajax({  
    type: 'POST',  
    url: /login/,  
    data: data,  //request Header中默认是Content-Type:application/x-www-form-urlencoded
    dataType: 'json', //# 注意：期望服务器返回的数据类型  
    success: function(data) { //# 这里的data就是json格式的数据  
        return data;
    },  
    error: function(xhr, type) {  
    }  

});