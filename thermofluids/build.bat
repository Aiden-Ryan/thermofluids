@echo off
REM Check current setuptools version
pip show setuptools > setuptools_version.txt
for /F "tokens=2" %%a in ('findstr "Version" setuptools_version.txt') do set setuptools_version=%%a
set required_version=72.1.0

REM Compare setuptools versions and downgrade if necessary
python -c "import sys; from pkg_resources import parse_version; sys.exit(0 if parse_version('%setuptools_version%') <= parse_version('%required_version%') else 1)"
if %errorlevel% neq 0 (
    echo Downgrading setuptools from %setuptools_version% to %required_version%...
    pip install setuptools==%required_version%
)

del setuptools_version.txt
REM Now run setup.py to build the package
python setup.py sdist bdist_wheel
