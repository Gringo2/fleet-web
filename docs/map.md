# Map Architecture

The map is the central component of the Traccar web interface. It is built on top of **MapLibre GL JS**, a high-performance WebGL-based vector map library.

## 1. Core Components

- **`MainMap.jsx`**: The container component that initializes the map instance and manages global state subscriptions.
- **`MapView.jsx`**: A wrapper around `MapLibre` that handles view state (zoom, center) and resizing.

## 2. Layers & Features

The map is composed of several functional layers, each managed by a React component that syncs Redux state to the MapLibre instance:

- **`MapPositions.js`**: Renders vehicle markers. It efficiently updates marker positions without full re-renders using MapLibre's `Source` and `Layer` APIs.
- **`MapRoutePath.js`**: Draws the history trail (polyline) when a user selects a device or requests a report.
- **`MapGeofence.js`**: Renders polygon, circle, and line geofences on the map.
- **`MapAccuracy.js`**: Renders a circle around the device indicating GPS accuracy.

## 3. Customization

### Map Styles
Map styles are configured in the `Server` settings or `traccar.xml`. The app supports:
- **XYZ Tiles**: Standard raster tiles (OSM, Google Maps).
- **Vector Styles**: Mapbox/MapLibre GL JSON styles.

### Adding a New Layer
To add a custom layer (e.g., weather radar):
1.  Create a new component (e.g., `MapWeather.js`).
2.  Use the `useMap` hook to get access to the `map` instance.
3.  Add the source and layer in a `useEffect` hook.
4.  Import and render the component inside `MainMap.jsx`.
