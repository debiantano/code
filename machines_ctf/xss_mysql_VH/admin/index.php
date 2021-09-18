<?php 
  require("../classes/auth.php");
  require("header.php");
  require("../classes/db.php");
  require("../classes/phpfix.php");
  require("../classes/post.php");
  require("../classes/comment.php");

   if(isset($_POST['title'])){
      Post::create();
   }
?>

<div style="padding-left: 300px;">
<table border="1">

<div>
<?php  
  $posts= Post::all();

  foreach ($posts as $post) {
    echo "<tr>";
    echo "<td><a href=\"../post.php?id=".h($post->id)."\">".h($post->title)."</a></td>";
    echo "<td><a href=\"edit.php?id=".h($post->id)."\">edit</a></td>";
    echo "<td><a href=\"del.php?id=".h($post->id)."\">delete</a></td>";
    echo "</tr>";
  }
?>
</table>
<a href="new.php">Write a new post</a>
</div>
</div>
<?php
  require("footer.php");

?>
