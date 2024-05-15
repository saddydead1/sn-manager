FROM ubuntu:latest
LABEL authors="saddy"

ENTRYPOINT ["top", "-b"]