FROM python:3.11.9-slim
RUN pip install fastapi uvicorn -i https://pypi.tuna.tsinghua.edu.cn/simple/
COPY main.py /app/main.py
WORKDIR /app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
