<?php 
  require("../classes/auth.php");
  require("header.php");
  require("../classes/db.php");
  require("../classes/phpfix.php");
  require("../classes/post.php");
?>

<?php  
  $post = Post::delete((int)($_GET["id"]));
  header("Location: /admin/index.php");
?>
