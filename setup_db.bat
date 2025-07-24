@echo off
echo Creating PostgreSQL user for Shopping Quest development...
echo.
echo You'll need to enter the postgres user password when prompted.
echo.
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -c "CREATE USER shoppingquest WITH PASSWORD 'quest123';"
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -c "CREATE DATABASE shoppingquest_dev OWNER shoppingquest;"
"C:\Program Files\PostgreSQL\17\bin\psql.exe" -U postgres -c "GRANT ALL PRIVILEGES ON DATABASE shoppingquest_dev TO shoppingquest;"
echo.
echo Done! Use these credentials in pgAdmin:
echo Username: shoppingquest
echo Password: quest123
echo Database: shoppingquest_dev
pause
