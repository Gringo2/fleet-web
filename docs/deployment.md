# Deployment Guide - Traccar Full Stack

This guide explains how to deploy the Traccar backend and frontend together using Docker.

## 1. Quick Start with Docker Compose

Running Traccar using Docker is the recommended way to get a production-ready setup quickly.

### Prerequisites
- Docker installed
- Docker Compose installed

### Step-by-Step

1.  **Prepare the configuration**:
    Create a `traccar.xml` file with your database and server settings. You can use the `debug.xml` from the backend repo as a template.

2.  **Create a Docker Compose file**:
    Create a `docker-compose.yml` file. You can base it on the official MySQL example in the backend's `docker/compose/traccar-mysql.yaml`.

```yaml
version: '3'
services:
  db:
    image: mysql:8.0
    container_name: traccar-db
    environment:
      - MYSQL_ROOT_PASSWORD=password
      - MYSQL_DATABASE=traccar
    volumes:
      - ./db:/var/lib/mysql

  traccar:
    image: traccar/traccar:latest
    container_name: traccar-server
    ports:
      - "8082:8082"    # Web Interface & API
      - "5000-5150:5000-5150/tcp" # Device Protocols (TCP)
      - "5000-5150:5000-5150/udp" # Device Protocols (UDP)
    volumes:
      - ./traccar.xml:/opt/traccar/conf/traccar.xml:ro
      - ./logs:/opt/traccar/logs
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
2.  Run the JAR: `java -jar target/traccar-server.jar conf/traccar.xml`

### Frontend (Production Build)
1.  Build the frontend: `npm run build`
2.  Copy the contents of the `build` directory to the backend's web root (configured via `web.path` in `traccar.xml`, default is `./modern`).

## 3. Database Selection

Traccar supports multiple databases. Use the following drivers in your configuration:
- **H2**: (Default for testing) `jdbc:h2:./target/database`
- **MySQL**: `jdbc:mysql://[host]:3306/traccar`
- **PostgreSQL**: `jdbc:postgresql://[host]:5432/traccar`

Liquibase will automatically create the necessary tables on the first run.
