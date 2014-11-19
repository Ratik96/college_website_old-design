$(document).ready(function() { 
    $('#selectorForm').ajaxForm({ 
        dataType:  'json',  
        success:   processJson 
    }); 
});
function processJson(data) { 
    // 'data' is the json object returned from the server 
    $('#namecloud').html('');
    var nc=$('#namecloud');
    
    for(var i=0,maximum=data.length;i<maximum;i+=1){
        nc.append("<a href='"+student_att+data[i].id+"'>"+data[i].name+"</a><br>");
    }
}
