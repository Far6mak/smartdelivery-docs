@echo off

echo === SMARTDELIVERY API TESTS START === > tests/results.log

python tests/api_tests.py >> tests/results.log

echo === TESTS FINISHED === >> tests/results.log

echo Done! results saved to tests/results.log
pause