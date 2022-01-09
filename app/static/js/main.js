$(document).ready(function (){

    $('.alert').alert()
    setTimeout(function(){
        $('.alert').alert('close')},3000
    )

// page 1
    if (window.location.pathname=='/settings') {
    }

// page 2
    if (window.location.pathname=='/overview') {
    }

})



//////////////////////////////////////////////////////////////////////////////////////
// functions /////////////////////////////////////////////////////////////////////////
//////////////////////////////////////////////////////////////////////////////////////

// user registration and login
    function regSubmit(){
        var reg_email = $('.reg_email').val()
        var reg_first_name = $('.reg_first_name').val()
        var reg_last_name = $('.reg_last_name').val()
        var reg_password = $('.reg_password').val()
        var reg_password2 = $('.reg_password2').val()
        var reg_dob = $('.reg_dob').val()
        $.ajax({
            type: 'GET',
            url: 'register',
            data: {
                "reg_email": reg_email,
                // "reg_first_name": reg_first_name,
                // "reg_last_name": reg_last_name,
                'reg_password': reg_password,
                'reg_password2': reg_password2,
                'reg_dob': reg_dob,
            },
            beforeSend: function(){
                $('.loadingAnim').show()
            },
            complete: function(){
                $('.loadingAnim').hide()
            },
            success: function(data) {
                if (data.message_type == 'success') {
                    hideModal()
                }
                else {
                    $('.reg_password').val('')
                    $('.reg_password2').val('')
                }
                $('.alertCont').append(`
                    <div class="alert alert-${data.message_type} fade show text-center">
                    ${data.message}
                    </div>
                `)
                $('.alert').alert()
                setTimeout(function(){
                    $('.alert').alert('close')},3000
                )
            }
        })
            
    }

// export
    function startExport(){
        var exportDateStart = $('.exportDateStart').val()
        var exportDateEnd = $('.exportDateEnd').val()
        $.ajax({
            type: 'GET',
            url: 'export',
            data: {
                'exportDateStart': exportDateStart,
                'exportDateEnd': exportDateEnd,
            },
            beforeSend: function(){
                $('.loadingAnim').show()
            },
            complete: function(){
                $('.loadingAnim').hide()
            },
            success: function(data) {
                var transaction = JSON.parse(data.transaction)
                var account = JSON.parse(data.account)
                var category = JSON.parse(data.category)
                var csvString = converToCsv(transaction,account,category)
                var blob = new Blob([csvString]);
                if (window.navigator.msSaveOrOpenBlob) 
                    window.navigator.msSaveBlob(blob, `${exportDateStart} to ${exportDateEnd}.csv`);
                else
                {
                    var a = window.document.createElement("a");
                    a.href = window.URL.createObjectURL(blob, {type: "text/plain"});
                    a.download = `${exportDateStart} to ${exportDateEnd}.csv`;
                    document.body.appendChild(a);
                    a.click();
                    document.body.removeChild(a);
                }            
            }
        })
    }

    function converToCsv(transaction,account,category){
        var str = '';
        var line = '';
        for (var index in transaction[0].fields) {
            if (line != '') line += ','
            line += index;
        }
        str += line + '\r\n';

        for (var i = 0; i < transaction.length; i++) {
            var line = '';
            for (var index in transaction[i].fields) {
                if (line != '') line += ','
                if  (index == 'category'){
                    for (var x in category) {
                        if (category[x].pk == transaction[i].fields[index]) {
                            line += category[x].fields.categoryName
                        }
                    }
                }
                else if (index == 'fromAccount' || index == 'toAccount'){
                    for (var x in account) {
                        if (account[x].pk == transaction[i].fields[index]) {
                            line += account[x].fields.accountName
                        }
                    }
                }
                else {
                    line += transaction[i].fields[index];
                }
                if (!transaction[i].fields[index] && transaction[i].fields[index] != '0' ){
                    line += 'N/A'
                }
            }
            str += line + '\r\n';
        }
        return str;
    }



// modal and tab
    function hideModal(){
        $('.modal').hide()
        $('.modal-backdrop').hide()
        $('.editEntryForm').hide()
    }
