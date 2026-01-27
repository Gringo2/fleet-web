# Project Structure - Fleet Web

This document outlines the organization of the `src` directory in the Fleet web interface.

## Core Directories

- **`common/`**: Reusable components, utility functions, and hooks.
    - **`components/`**: UI components like Buttons, Dialogs, etc.
    - **`util/`**: Helpers for formatting, API calls (`fetchOrThrow`), and preferences.
- **`store/`**: Redux Toolkit slices and the main store configuration.
- **`map/`**: All map-related logic and components.
    - **`core/`**: Base map view and camera logic.
    - **`main/`**: Specific map layers for the main tracking view.
- **`login/`**: Components for authentication (Login, Register, Password Reset).
- **`main/`**: The primary dashboard view (`MainPage.jsx`) and its sub-components (DeviceList, Toolbars).
- **`reports/`**: Documentation and UI for various tracking reports.
- **`settings/`**: Management pages for Devices, Users, Groups, etc.
- **`other/`**: Miscellaneous pages like Replay, Geofences, and the GPS Emulator.
- **`resources/`**: Static assets, including images and localization files (`l10n`).

## Key Files

- **`index.jsx`**: Application entry point.
- **`App.jsx`**: Main application component with global providers and layout logic.
- **`Navigation.jsx`**: Route definitions using React Router.
- **`SocketController.jsx`**: WebSocket lifecycle management.
- **`ServerProvider.jsx`**: Context provider for server-wide configuration.
