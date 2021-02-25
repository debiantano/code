<?php
  include("log.class.php");

  class Welcome {
    public function handler($val) {
      echo "Hello " . $val;
    }
  }

  class User {
    private $name;
    private $wel;

    function __construct($name) {
      $this->name = $name;
      $this->wel = new Welcome();
    }

    function __destruct() {
      //echo "bye\n";
      $this->wel->handler($this->name);
    }
  }

?>
