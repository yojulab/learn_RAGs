FROM python:3.11

# 기본 도구 설치
RUN apt-get update && apt-get install -y \
    git \
    curl \
    wget \
    sudo \
    sqlite3 \
    && rm -rf /var/lib/apt/lists/*

# 작업 디렉토리 설정
WORKDIR /apps

# Clone the Git repository. Here we dynamically specify the repository name using the variable defined earlier.
RUN git clone -b main https://github.com/yojulab/learn_RAGs learn_RAGs

# Changes the working directory to /app/${REPO_NAME}. This uses the variable to dynamically set the directory path.
WORKDIR /apps/learn_RAGs

RUN python -m pip install --upgrade pip
RUN python -m pip install --no-cache-dir -r ./requirements.txt

# RUN rm -rf .git
