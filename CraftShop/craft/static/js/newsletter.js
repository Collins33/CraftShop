$(document).ready(function(){
  $('form.subscription').submit(function(event){
    event.preventDefault()
    form=$('form.subscription')
    //the ajax function
    $.ajax({
      'url':'/ajax/newsletter/',
      'type':'POST',
      'data':form.serialize(),
      'dataType':'json',
      'success':function(data){
        alert(data["success"])
      }
    })
    $('#id_your_name').val('')
   $("#id_email").val('')
  })

})
