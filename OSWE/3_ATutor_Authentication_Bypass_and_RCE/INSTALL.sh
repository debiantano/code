# https://maximilian-marx.me/posts/atutor-blind-sqli/
sudo apt update
sudo apt upgrade
sudo apt-get install openssh-server
sudo apt install aptitude
sudo aptitude purge `dpkg -l | grep php| awk '{print $2}' |tr "\n" " "`
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo reboot
sudo apt-get install php5.6 libapache2-mod-php5.6 php5.6-mcrypt php5.6-mysql php5.6-gd php5.6-mbstring
sudo apt-get install mysql-server
wget http://downloads.sourceforge.net/project/atutor/ATutor%202/ATutor-2.2.1.tar.gz?r=http%3A%2F%2Fwww.atutor.ca%2Fatutor%2Fdownload.php -O ATutor-2.2.1.tar.gz
tar -zxvf ATutor-2.2.1.tar.gz
sudo mv ATutor /var/www/html/atutor
sudo chown -R www-data: /var/www/html/atutor/
mysql_secure_installation
# -> Set new password for root
# -> Remove anonymous users? Y
# -> Disallow root login remotely? Y
# -> Remove Test DB and access to it? Y
# -> Reload privilege tables now? Y
sudo systemctl restart apache2
sudo nano /etc/mysql/my.cnf
# Add this:
[mysqld]
sql_mode="ONLY_FULL_GROUP_BY,ERROR_FOR_DIVISION_BY_ZERO,NO_AUTO_CREATE_USER,NO_ENGINE_SUBSTITUTION"
# Save and exit
sudo systemctl restart mysql

# Now visit http://localhost/atutor and start the setup
