  /* Submit review when clicking on review buttons */
  $(document).ready(function() {
    $(".console-button-apagar").click(
      function(event) {
        event.stopPropagation()
        var eventRow = $(this).closest("tr.console-row-event")
        var action = $(this).prop("value")
  
        apagarUsuario(eventRow.prop("id"), action).done(
          function() {
            eventRow.hide()
          }
          ).fail(
          function(e) {
              getAlert("danger", "Error! 😞", e.responseJSON.erro)
          }
        )
      }
    );
  });
