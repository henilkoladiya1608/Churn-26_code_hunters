# Contributing to ChurnZero Analysis

Thank you for your interest in contributing! We welcome contributions from the community.

## How to Contribute

### Reporting Bugs

Before creating a bug report, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and what you expected instead**

### Pull Requests

- Fill in the required template
- Follow the Python styleguides
- Include appropriate test cases
- End all files with a newline

## Development Setup

1. Fork the repository
2. Clone your fork:
   ```bash
   git clone https://github.com/yourusername/ChurnZero-Analysis.git
   cd ChurnZero-Analysis
   ```

3. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   pip install pytest pytest-cov black flake8
   ```

5. Create a feature branch:
   ```bash
   git checkout -b feature/YourFeature
   ```

6. Make your changes and commit:
   ```bash
   git add .
   git commit -m "Add YourFeature"
   ```

7. Push to your fork:
   ```bash
   git push origin feature/YourFeature
   ```

8. Open a Pull Request

## Code Style

### Python Style Guide

We follow [PEP 8](https://pep8.org/) with the following additions:

- Use 4 spaces for indentation
- Maximum line length is 100 characters
- Use type hints where appropriate
- Write descriptive variable and function names

### Formatting

Use `black` for code formatting:
```bash
black churnzero_analysis.py
```

### Linting

Use `flake8` to check your code:
```bash
flake8 churnzero_analysis.py
```

## Testing

- Write tests for new features
- Run tests before submitting a PR:
  ```bash
  pytest
  ```
- Maintain or improve code coverage

## Documentation

- Add docstrings to all functions and classes
- Update README.md if you add new features
- Include examples in your docstrings

## Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

## Additional Notes

### Issue and Pull Request Labels

This project uses the following labels:

- `bug` - Something isn't working
- `enhancement` - New feature or request
- `documentation` - Improvements or additions to documentation
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention is needed

## License

By contributing to ChurnZero Analysis, you agree that your contributions will be licensed under its MIT License.

## Questions?

Feel free to open an issue with the label `question` or contact the project maintainers.

Thank you for contributing! 🎉
