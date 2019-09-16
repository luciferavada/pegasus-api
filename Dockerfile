FROM archlinux/base

ENV PACMAN_PACKAGES="python python-pip git base-devel"

copy ./.requirements /.requirements

RUN pacman --noconfirm -Sy ${PACMAN_PACKAGES} && \
  pip install -r /.requirements

RUN pip install watchgod

COPY ./server /server

CMD python server
