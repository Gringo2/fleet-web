# Deployment Guide - Fleet Full Stack

This guide explains how to deploy the Fleet backend and frontend together using Docker.

## 1. Quick Start with Docker Compose

Running Fleet using Docker is the recommended way to get a production-ready setup quickly.

### Prerequisites
- Docker installed
- Docker Compose installed

### Step-by-Step

1.  **Prepare the configuration**:
    Create a `Fleet.xml` file with your database and server settings. You can use the `debug.xml` from the backend repo as a template.

2.  **Create a Docker Compose file**:
    Create a `docker-compose.yml` file. You can base it on the official MySQL example in the backend's `docker/compose/Fleet-mysql.yaml`.

```yaml
version: '3'
services:
  db:
    image: mysql:8.0
    container_name: Fleet-db
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=Fleet
    volumes:
      - ./db:/var/lib/mysql

  Fleet:
    image: Fleet/Fleet:latest
    container_name: Fleet-server
    ports:
      - "8082:8082"    # Web Interface & API
      - "5000-5150:5000-5150/tcp" # Device Protocols (TCP)
      - "5000-5150:5000-5150/udp" # Device Protocols (UDP)
    volumes:
      - ./Fleet.xml:/opt/Fleet/conf/Fleet.xml:ro
      - ./logs:/opt/Fleet/logs
    depends_on:
      - db
```

3.  **Launch the stack**:
```bash
docker-compose up -d
```

The web interface will be available at `http://localhost:8082`.

## 2. Manual Deployment (Standalone)

If you are not using Docker:

### Backend
1.  Build the JAR: `./gradlew assemble`
2.  Run the JAR: `java -jar target/Fleet-server.jar conf/Fleet.xml`

### Frontend (Production Build)
1.  Build the frontend: `npm run build`
2.  Copy the contents of the `build` directory to the backend's web root (configured via `web.path` in `Fleet.xml`, default is `./modern`).

## 3. Database Selection

Fleet supports multiple databases. Use the following drivers in your configuration:
- **H2**: (Default for testing) `jdbc:h2:./target/database`
- **MySQL**: `jdbc:mysql://[host]:3306/Fleet`
- **PostgreSQL**: `jdbc:postgresql://[host]:5432/Fleet`

Liquibase will automatically create the necessary tables on the first run.
