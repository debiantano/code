<?php 
  require 'classes/db.php';
  require 'classes/phpfix.php';
  require 'classes/post.php';
  require 'classes/comment.php';
?>
<!-- PentesterLab --> 
<html>
  <head>
    <link rel="stylesheet" id="base" href="css/default.css" type="text/css" media="screen" />

    <title><?php echo (isset($site)) ? h($site) :"My Blog" ; ?></title>
  </head>
  <body>
    
  <div id="header">
    <div id="logo">
      <h1><a href="index.php">My Blog</a></h1>
    </div>
    <div id="menu">
      <ul>  
        <li class="active">
            <a href="/"> Home  |</a> 
        </li>
 
        <li>
          <a href="/admin/">Admin</a>
        </li>
        </ul>
      </div>
    </div> 

  </div>

    <div id="page">
      <div id="content">
