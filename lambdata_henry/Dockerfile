## Image to base ours on
FROM debian
## Environment variables to configure things
## Setting shell so pipenv shell works
ENV SHELL=/bin/bash
## Update and install dependencies
RUN apt update && \       --- upgrade all packages u already have
  apt upgrade -y && \       ---  answer "YES" for all questions yes/no
  apt install python3-pip -y && \
  pip3 install pandas && \
  pip3 install -i https://test.pypi.org/simple/ lambdata-henry