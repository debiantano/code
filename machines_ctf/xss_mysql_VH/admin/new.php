<?php
  require("../classes/auth.php");
  require("header.php");
  require("../classes/db.php");
  require("../classes/phpfix.php");
  require("../classes/post.php");
?>

  <form action="index.php" method="POST" enctype="multipart/form-data">
    Title: <input type="text" name="title" /><br/>
    Text: <textarea name="text" cols="80" rows="5">
        </textarea><br/>

    <input type="submit" name="Add" value="Add">

  </form>

<?php
  require("footer.php");

?>
