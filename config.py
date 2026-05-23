"""
Configuration file for ChurnZero Analysis Project
"""

import os
from pathlib import Path

# Project root directory
PROJECT_ROOT = Path(__file__).parent
DATA_DIR = PROJECT_ROOT / 'data'
RESULTS_DIR = PROJECT_ROOT / 'results'
MODELS_DIR = RESULTS_DIR / 'models'
FIGURES_DIR = RESULTS_DIR / 'figures'
REPORTS_DIR = RESULTS_DIR / 'reports'

# Create directories if they don't exist
for directory in [DATA_DIR, RESULTS_DIR, MODELS_DIR, FIGURES_DIR, REPORTS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Data configuration
DATA_CONFIG = {
    'path': DATA_DIR / 'churnzero_data.csv',
    'sep': ',',
    'encoding': 'utf-8',
}

# Analysis parameters
ANALYSIS_CONFIG = {
    'test_size': 0.2,
    'random_state': 42,
    'cv_folds': 5,
}

# Model parameters
MODEL_CONFIG = {
    'logistic_regression': {
        'max_iter': 1000,
        'random_state': 42,
    },
    'random_forest': {
        'n_estimators': 100,
        'max_depth': 10,
        'random_state': 42,
    },
    'gradient_boosting': {
        'n_estimators': 100,
        'learning_rate': 0.1,
        'max_depth': 5,
        'random_state': 42,
    },
}

# Visualization configuration
VISUALIZATION_CONFIG = {
    'figsize': (12, 6),
    'dpi': 300,
    'style': 'seaborn-v0_8-whitegrid',
    'colormap': 'viridis',
}

# Logging configuration
LOGGING_CONFIG = {
    'level': 'INFO',
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
}

# Feature configuration
FEATURE_CONFIG = {
    'numeric_features': [],  # Add your numeric features
    'categorical_features': [],  # Add your categorical features
    'target_variable': 'churn',  # Target column name
}
