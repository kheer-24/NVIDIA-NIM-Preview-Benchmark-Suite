@echo off
title NVIDIA NIM - Benchmark Runner
echo ========================================================
echo   Running NVIDIA NIM 45 Preview Models Benchmark
echo   Saves progress incrementally to results.json
echo ========================================================
python benchmark.py --resume
pause
