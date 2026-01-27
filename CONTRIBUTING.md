# Contributing to Traccar Web Interface

Thank you for your interest in contributing to the Traccar web interface!

## Code Style

- We use **ESLint** with the **Airbnb** configuration to maintain code quality.
- Functional components and Hooks are preferred over class components.
- Use **Emotion** for styling (via MUI).
- Ensure all new features are localized in `src/resources/l10n`.

## Development Process

1. **Fork** the repository and create your branch from `master`.
2. **Install** dependencies: `npm install`.
3. **Run** the development server: `npm start`.
4. **Lint** your code: `npm run lint`.
5. **Test** your changes thoroughly against a local or demo Traccar backend.
6. **Submit** a Pull Request with a clear description of the changes.

## Reporting Issues

- Use the GitHub Issues tracker to report bugs.
- Provide clear steps to reproduce the issue.
- Include information about your environment (Browser, OS, Traccar version).

## Pull Request Guidelines

- Keep PRs focused on a single change.
- Ensure the build passes and there are no linting errors.
- Update documentation if necessary.
