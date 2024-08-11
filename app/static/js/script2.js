var faqs_row = 0;
function addfaqs() {
html = '<tr id="faqs-row'  + faqs_row + '">';  
	
html += '<td><input type="text" name="name" value="ABC" style="text-align: center;"></td>';
html += '<td><input type="text" name="name" value="google.co.in" style="text-align: center;"></td>';
html += '<td><input type="text" name="name" value="10,000" style="color: yellow;text-align: center;"></td>';
html += '<td><input type="text" name="name" value="10,000" style="color: green;text-align: center;"></td>';
html += '<td><input type="text" name="name" value="google.co.in"></td>';
html += '<td><input type="text" name="name" value="1,000" style="color: yellow;text-align: center;"></td>'; 
html += '<td><input type="text" name="name" value="1,000" style="color: green;text-align: center;"></td>';	
	
html += '<td style="max-width:34px;"><span class="c-link js-toggleForm">✎</span> <button style="max-width:33px;float: right;" class="badge badge-danger" onclick="$(\'#faqs-row' + faqs_row + '\').remove();"><i class="fa fa-trash"></i></button></td>';

    html += '</tr>';

$('#faqs tbody').append(html);

faqs_row++;
}


