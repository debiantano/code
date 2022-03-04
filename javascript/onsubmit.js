<!DOCTYPE html>
<html>
<body>

<p>Este ejemplo usa HTML DOM para asignar un evento "onsubmit" a un elemento de formulario.</p>

<p>Cuando envía el formulario, se activa una función que alerta algún texto.</p>

<form id="myForm" action="/action_page.php">
  Enter name: <input type="text" name="fname">
  <input type="submit" value="Submit">
</form>

<script>
document.getElementById("myForm").onsubmit = function() {myFunction()};

function myFunction() {
  alert("Enviado");
}
</script>

</body>
</html>
