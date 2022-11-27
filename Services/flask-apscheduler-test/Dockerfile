# @author : microfat
# @time   : 11/20/22 22:18:29
# @File   : Dockerfile

FROM python:3.11.0-slim
LABEL developer="xiang"
LABEL mail=""
LABEL version="1.0"


# 安装基础环境
RUN sed -i 's/deb.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
    && sed -i 's/security.debian.org/mirrors.tuna.tsinghua.edu.cn/g' /etc/apt/sources.list \
    && apt-get clean \
    && apt-get update \
    # 设置python pip
    && apt-get install --no-install-recommends -y build-essential\
    && pip3 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple --upgrade pip \
    # 设置时区
    && export DEBIAN_FRONTEND=noninteractive \
    && apt-get install --no-install-recommends -y tzdata \
    && rm /etc/localtime \
    && ln -s /usr/share/zoneinfo/Asia/Shanghai /etc/localtime \
    && dpkg-reconfigure -f noninteractive tzdata

COPY . /app
WORKDIR /app

# 安装项目环境
RUN rm -Rf /app/__pycache__ \
    && cat /app/Services/flask-apscheduler-test/requirements.txt | xargs -n 1 -L 1 pip3 --default-timeout=1000 install --no-cache-dir -i https://pypi.tuna.tsinghua.edu.cn/simple \
    #&& python3 /app/setup.py build_ext --inplace \
    && apt-get purge -y --auto-remove gcc make \
    && rm -rf /var/lib/apt/lists/* 

#ENTRYPOINT ["/bin/sh"]
ENTRYPOINT ["supervisord", "-n", "-c", "/app/Services/flask-apscheduler-test/supervisord.conf"]