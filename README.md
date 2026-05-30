python -m venv .venv \
.venv\Scripts\activate \
poetry add --group lint flake8 black isort mypy \
flake8 src/
black src/  
isort src/  
mypy src/        