# Manual
1. Docker Command
    - docker run --network host --name python-server -v ~/share:/mnt -d -it --rm -p 8000:8000 python:latest
2. Install Command
    - pip install -r requirements.txt
3. Execute Command
    - uvicorn main:app --reload