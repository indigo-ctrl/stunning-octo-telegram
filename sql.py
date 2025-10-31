mysql -u root -p

CREATE DATABASE hobbyhelper_bot CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

CREATE USER 'bot_user'@'localhost' IDENTIFIED BY 'secure_password';

GRANT ALL PRIVILEGES ON hobbyhelper_bot.* TO 'bot_user'@'localhost';

FLUSH PRIVILEGES;

USE hobbyhelper_bot;