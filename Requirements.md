# Fetch-Assessment
Python Dependencies:
pandas
matplotlib
seaborn
sqlalchemy
psycopg2
numpy


PostgreSQL & pgAdmin Setup
version: '3.8'
services:
  postgres:
    image: postgres
    container_name: my_postgres
    restart: always
    environment:
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
      POSTGRES_DB: mydatabase
    ports:
      - "5433:5432"  # PostgreSQL is exposed on port 5433 (mapped from Docker's 5432)
    volumes:
      - postgres_data:/var/lib/postgresql/data

  pgadmin:
    image: dpage/pgadmin4
    container_name: my_pgadmin
    restart: always
    environment:
      PGADMIN_DEFAULT_EMAIL: admin@example.com
      PGADMIN_DEFAULT_PASSWORD: admin
    ports:
      - "5055:80"  # pgAdmin is accessible on http://localhost:5055/
    depends_on:
      - postgres

volumes:
  postgres_data:





  
