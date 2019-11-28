$(function () {

  $(".js-upload-photos").click(function () {
    $("#fileupload").click();
    
  });
  var x = document.getElementById("Lprogress");
  var y = document.getElementById("LDprogress");
  
  document.getElementById("okButton")
  .addEventListener("click", function() {
 
document.getElementById("awecsome").hidden = false;
}, false);

  $("#fileupload").fileupload({
    dataType: 'json',
    sequentialUploads: true,

    start: function (e) {
      document.getElementById("awesome").hidden = false;
       //$("#modal-progress").modal("show");
       
    },

    stop: function (e) {
      document.getElementById("awesome").hidden = true;
     // x.style.display='none';//$("#modal-progress").modal("hide");
    },

    progressall: function (e, data) {
      var progress = parseInt(data.loaded / data.total * 100, 10);
      var strProgress = progress + "%";
      $(".progress-bar").css({"width": strProgress});
      //$(".progress-bar").text(strProgress);
    },
    done: function (e, data) {
      alert("LOL") //
      /*if (data.result.is_valid) {
        $("#gallery tbody").prepend(
          "<tr><td><a href='" + data.result.url + "'>" + data.result.name + "</a></td></tr>"
        )
      }*/
      
    }
  });

});
