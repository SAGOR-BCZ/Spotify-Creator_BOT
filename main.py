import os, sys
try:
    __import__("main_enc").main.multi_threading()
except Exception as e:
    exit(str(e))
