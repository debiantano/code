<?php
class Book{

    // constructor
    public function __construct(
        public string $author,
        public string $title,
        private int $price,
        private int $stock,
        private int $id)
        {
        echo "Soy una instancia de Book";
        }

        // metodos
        public function getInfo(){
            $info = "<u>$this->title</u>";
            return $info;
        }
}

echo "<b>Instancia de clase</b></br>";

$book1 = new Book("Fedor Dostoivski", "Crimen y castigo", 120, 20, 1);
$book2 = new Book("Ernest Hemingway", "El viejo y el mar", 240, 10, 2);

var_dump($book1);

echo "</br></br><b>Propiedades de la clase Book</b>";
echo "</br>";
echo $book1->author;

echo "</br>";
echo $book1->title;

echo "</br>";
echo "</br><b>Metodo getInfo</b></br>";
echo $book1->getInfo();

?>
