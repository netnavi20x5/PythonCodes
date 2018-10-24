# PythonCodes
Twitter API Testing

requirements
dependency on tweepy

install tweepy by using 
pip install tweepy

for error (windows 10 Python v3.7) 

issue: For windows 10 x64
...\streaming.py", line 358

The same issue but on Windows10 x64 python3.7 beta, on python3.6 it works fine, so seems like incompatibility with python 3.7?
Apparently async cannot be used as an argument name in Python 3.7
So open streaming.py and replace #async with async_ it fixed the error 

