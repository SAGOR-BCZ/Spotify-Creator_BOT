import os, sys
try:
    __import__("main").main.multi_threading()
except Exception as e:
    exit(str(e))
