# Contributing to Image Caption Generator

First off, thank you for considering contributing to Image Caption Generator! 🎉

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check existing issues. When you create a bug report, include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps to reproduce the problem**
- **Provide specific examples**
- **Describe the behavior you observed**
- **Explain which behavior you expected to see**
- **Include screenshots if possible**
- **Include your environment details** (OS, Python version, etc.)

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, include:

- **Use a clear and descriptive title**
- **Provide a detailed description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior** and **explain the behavior you'd like to see**
- **Explain why this enhancement would be useful**

### Pull Requests

1. Fork the repo and create your branch from `main`
2. If you've added code that should be tested, add tests
3. If you've changed APIs, update the documentation
4. Ensure the test suite passes
5. Make sure your code follows the existing style
6. Issue that pull request!

## Development Setup

1. **Fork and clone the repository**
```bash
git clone https://github.com/eosoukaina/image-caption-generator.git
cd image-caption-generator
```

2. **Create a virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install development dependencies**
```bash
pip install -r requirements.txt
pip install pytest black flake8
```

4. **Create a branch**
```bash
git checkout -b feature/your-feature-name
```

## Styleguides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature")
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
- Limit the first line to 72 characters or less
- Reference issues and pull requests liberally after the first line

Examples:
```
feat: Add API endpoint for batch processing
fix: Resolve memory leak in image processing
docs: Update installation instructions
style: Format code with Black
test: Add tests for caption generation
```

### Python Styleguide

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
- Use [Black](https://github.com/psf/black) for code formatting
- Use type hints for function signatures
- Write docstrings for all public functions and classes
- Keep functions focused and small

Example:
```python
def generate_caption(image_path: Path) -> str:
    """
    Generate a caption for an image.
    
    Args:
        image_path: Path to the image file
        
    Returns:
        Generated caption as string
        
    Raises:
        ValueError: If image cannot be processed
    """
    # Implementation
```

### Documentation Styleguide

- Use Markdown for documentation
- Reference functions and classes using backticks: `function_name()`
- Include code examples where appropriate
- Keep line length to 80-100 characters

## Testing

Run the test suite before submitting:

```bash
pytest tests/
```

Run style checks:

```bash
black --check .
flake8 .
```

## Project Structure

When adding new features, maintain the project structure:

```
app.py              # Main application
config.py           # Configuration
wsgi.py            # Production entry point
models/            # Trained models
static/            # Static assets
templates/         # HTML templates
tests/             # Test files
docs/              # Documentation
```

## Areas for Contribution

Here are some areas where contributions would be especially valuable:

### High Priority
- [ ] Add comprehensive unit tests
- [ ] Improve model accuracy
- [ ] Add support for more image formats
- [ ] Implement caching for faster inference
- [ ] Add multi-language caption support

### Medium Priority
- [ ] Create mobile-responsive design improvements
- [ ] Add user authentication
- [ ] Implement image history/gallery
- [ ] Add export functionality (JSON, CSV)
- [ ] Improve error messages

### Low Priority
- [ ] Add dark/light theme toggle
- [ ] Create API rate limiting
- [ ] Add image filters/preprocessing
- [ ] Create video caption support
- [ ] Add social media sharing

## Questions?

Feel free to open an issue with your question or reach out to the maintainers.

## Recognition

Contributors will be recognized in:
- README.md Contributors section
- Release notes
- Project documentation

Thank you for contributing! 🙏
