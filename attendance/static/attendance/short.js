for (var student in jsonstr){
var row=document.createElement('tr');
var td_n=document.createElement('td');
var td_l=document.createElement('td');
var td_t=document.createElement('td');
var td_p=document.createElement('td');
td_l.innerHTML=jsonstr[student]['lecture'];
td_t.innerHTML=jsonstr[student]['tutorial'];
td_p.innerHTML=jsonstr[student]['practical'];
td_n.innerHTML=student;
row.appendChild(td_n);
 row.appendChild(td_l);
 row.appendChild(td_t);
 row.appendChild(td_p);
 $('#sorted_table tbody').append(row);
}  
