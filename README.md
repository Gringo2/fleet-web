# Fleet Web Interface

Modern, responsive web interface for the [Fleet GPS tracking platform](https://www.Fleet.org).

## Overview

Fleet is an open-source server for various GPS tracking devices. This repository contains the official React-based web interface. It provides real-time tracking, historical reports, geofencing, and account management.

For the backend server, please check the [main Fleet repository](https://github.com/Fleet/Fleet).

## Tech Stack

- **Framework**: [React 19](https://react.dev/)
- **Build Tool**: [Vite 7](https://vitejs.dev/)
- **UI Library**: [Material UI 7](https://mui.com/)
- **State Management**: [Redux Toolkit](https://redux-toolkit.js.org/)
- **Map Engine**: [MapLibre GL](https://maplibre.org/)
- **Icons**: [MUI Icons](https://mui.com/material-ui/material-icons/)
- **PWA**: [Vite PWA Plugin](https://vite-pwa-org.netlify.app/)

## Getting Started

### Prerequisites

- Node.js (v18 or newer)
- npm (v9 or newer)

### Installation

```bash
npm install
```

### Development

To start the development server:

```bash
npm run start
```

The app will be available at `http://localhost:3000`. By default, it expects a Fleet backend running at `http://localhost:8082`. You can change this in `vite.config.js`.

### Build

To create a production-ready build:

```bash
npm run build
```

The output will be in the `build` directory.

## Features

- **Real-time Tracking**: Live updates via WebSockets.
- **Reporting**: Comprehensive reports (Trips, Stops, Summary, Chart).
- **Geofencing**: Create and manage circular, polygonal, and polyline geofences.
- **Responsive Design**: Optimized for desktop and mobile devices.
- **Localization**: Support for multiple languages.
- **PWA Integration**: Installable web app with offline capabilities.

## Documentation

- [Project Structure](docs/structure.md)
- [Integration Guide](docs/integration.md) (API & WebSockets)
- [Localization Guide](docs/l10n.md) (Translations & i18n)
- [Deployment Guide](docs/deployment.md) (Docker & Standalone)
- [State Management](docs/state.md) (Redux Store & Data Flow)
- [Map Architecture](docs/map.md) (MapLibre Layers & Components)
- [Backend Documentation](../Fleet/README.md)

## License

[Apache License, Version 2.0](LICENSE.txt)
