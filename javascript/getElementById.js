<!DOCTYPE html>
<html>
<body>

<h1>The Document Object</h1>
<h2>The getElementById() Method</h2>

<p id="demo"></p>

<script>
document.getElementById("demo").innerHTML = "Hello World";
</script>

</body>
</html>

//////////////////////////////////////////////////////////////////////////////////////////////////

<!DOCTYPE html>
<html>
<body>

<h1 id="demo">The Document Object</h1>
<h2>The getElementById() Method</h2>

<script>
const myElement = document.getElementById("demo");
myElement.style.color = "blue";
</script>

</body>
</html>
