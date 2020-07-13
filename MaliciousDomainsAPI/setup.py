from setuptools import setup
global authToken, password
def auth(token, pwd):
    authToken=token
    password=pwd
    return(True)

setup(
    API_KEY=authToken,
    pwd=password,
    name='OTXv2',
    version='1.5.10',
    description='AlienVault OTX API',
    author='AlienVault Team',
    author_email='otx@alienvault.com',
    url='https://github.com/AlienVault-Labs/OTX-Python-SDK',
    download_url='https://github.com/AlienVault-Labs/OTX-Python-SDK/tarball/1.5.10',
    py_modules=['OTXv2', 'IndicatorTypes','patch_pulse'],
    install_requires=['requests', 'python-dateutil', 'pytz']
)
