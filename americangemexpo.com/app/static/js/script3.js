var faqs_row1 = 0;
function addfaqs() {
html = '<tr id="faqs-row'  + faqs_row1 + '">'; 
	  html += '<td><input type="text" name="name" value="john"></td>';
      html += '<td><input type="text" name="name" value="john"></td>';
      html += '<td><input type="text" name="name" value="john"></td>';
      html += '<td><input type="text" name="name" value="john"></td>';
      html += '<td><input type="text" name="name" value="john"></td> '; 
      html += '<td><span class="c-link1 js-toggleForm1">✎</span> <button style="max-width:33px;float: right;" class="badge badge-danger" onclick="$(\'.faqs-row' + faqs_row1 + '\').remove();"><i class="fa fa-trash"></i></button></td>';
	 

    html += '</tr>';

$('.faqs tbody').append(html);

faqs_row1++;
}


