"""
Configuration management for the Autonomous Strategy Generator
Uses environment variables with sensible defaults
"""

import os
from dataclasses import dataclass
from typing import Dict, List, Optional
from enum import Enum

class MarketType(Enum):
    CRYPTO = "crypto"
    STOCKS = "stocks"
    FOREX = "forex"
    COMMODITIES = "commodities"

class StrategyType(Enum):
    MOMENTUM = "momentum"
    MEAN_REVERSION = "mean_reversion"
    ARBITRAGE = "arbitrage"
    ML_PREDICTIVE = "ml_predictive"

@dataclass
class DatabaseConfig:
    """Firebase configuration"""
    project