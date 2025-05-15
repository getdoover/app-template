# Doover Application Template

This repository serves as a template for creating Doover applications.

It provides a structured layout for application code, deployment configurations, simulators, and tests. The template is
designed to simplify the development and deployment of Doover-compatible applications.

The basic structure of the repository is as follows:

## Getting Started

```
doover_config.json  <-- Configuration file for doover
Dockerfile          <-- Dockerfile for building the application image
Pipfile             <-- Python dependencies
Pipfile.lock        <-- Locked dependencies
README.md           <-- This file

application/        <-- Application directory
  application.py    <-- Main application code
  app_config.py     <-- Config schema definition
  app_ui.py         <-- UI code (if applicable)
  app_state.py      <-- State machine (if applicable)

deployment/
  docker-compose.yml <-- Docker Compose file for deployment

simulator/
  app_config.json   <-- Sample configuration for the simulator
  docker-compose.yml <-- Docker Compose file for the simulator
  
tests/
    test_imports.py  <-- Test file for the application
```

The `doover_config.json` file is the doover configuration file for the application.
It defines where the Doover site should find the application code. In our case, this is a fairly straightforward

```json
{
    "deployment_package_dir": "deployment/"
}
```

### Prerequisites

- Docker and Docker Compose installed
- Python 3.11 or later (if running locally)
- Pipenv for managing Python dependencies

### Running Locally

1. Run the application:

```bash
cd simulator && docker copmose up --build
```

## Simulators

The `simulator/` directory contains tools for simulating application behavior. For example:

- `app_config.json`: Sample configuration file for the app.
- `docker-compose.yml`: Defines services for running the application.

You can find a sample simulator in the `simulator/sample/` directory. While it is fairly bare-bones, it shows
positioning of the simulator in the application structure, and how to start the simulator alongside your application.

## Testing

Run the tests using the following command:

```bash
pytest tests/
```

## Deployment

The `deployment/` directory contains deployment configurations, including a `docker-compose.yml` file for orchestrating
services.

## Customization

To create your own Doover application:

1. Modify the application logic in the appropriate directory.
2. Update the simulator and test configurations as needed.
3. Adjust deployment configurations to suit your requirements.
