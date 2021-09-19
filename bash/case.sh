catn case.sh
#!/bin/bash

echo "What is your preferred programing /scripting lenguage?"
echo "1) bash"
echo "2) python"
echo "3) c++"
echo "4) perl"
echo "I do not know !"

echo -e "Please make a choose: \c"
read choose

case $choose in
        1) echo "You select bash";;
        2) echo "You select python";;
        3) echo "You select c++";;
        4) echo "You select perl";;
        5) exit;;
esac

