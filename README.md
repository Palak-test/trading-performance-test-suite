

# Loopa

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)

Loopa is an open source, developer-friendly load testing tool for HTTP and other protocols. Define your tests in regular Python code, run them from the command line or web UI, and scale up to distributed testing across many machines.

## Features

- **Write user test scenarios in plain Python**: Use familiar programming constructs to define user behavior, loops, and conditional logic.
- **Distributed & Scalable**: Easily run load tests distributed over multiple machines, supporting thousands of concurrent users.
- **Web-based UI**: Monitor test progress, throughput, response times, and errors in real time. Change load while the test is running.
- **Extensible & Hackable**: Add custom event handlers, load shapes, and reporting modules. Test any system or protocol by writing your own client.
- **CI/CD Friendly**: Run tests headless for automation and integration.

## Project Structure

```
loopa/                # Core source code (argument parsing, environment, dispatch, clients, events)
examples/             # Example scripts and integrations (basic, docker, grpc, terraform, vagrant, etc.)
docs/                 # Documentation (quickstart, configuration, tasksets, extensions, logging, etc.)
pytest_loopa/         # Test suite
Dockerfile, Makefile, pyproject.toml, package.json, LICENSE, SECURITY.md
```

## Architecture

Loopa is modular and extensible:
- **Argument Parser**: Command-line and environment configuration
- **Environment Manager**: Test settings and variables
- **Dispatcher**: Task execution and user simulation
- **Clients**: HTTP client logic for target systems
- **Event System**: Custom event handling and extensibility
- **Examples & Extensions**: Advanced integrations (Docker, Terraform, Vagrant, gRPC, etc.)

## Getting Started

See [docs/quickstart.rst](docs/quickstart.rst) for installation and usage instructions.

## Documentation

Comprehensive documentation is available in the [docs/](docs/) directory:
- Quickstart
- Configuration
- Tasksets
- Extensions
- Logging
- Running Distributed
- Writing a Loopafile

## Links

- [Documentation](https://github.com/Palak-test/trading-performance-test-suite/tree/master/docs)
- [Security Policy](SECURITY.md)
- [MIT License](LICENSE)

---

Created by pari9p (behlpari4@gmail.com)
