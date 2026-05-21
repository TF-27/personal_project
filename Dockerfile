FROM fedora:latest

RUN dnf clean all

RUN dnf update -y
RUN dnf install -y \
    python3 \
    python3-pip \
    python3-devel \
    gcc \
    git \
    pkg-config \
    libX11-devel \
    gtk3-devel \
    gobject-introspection-devel \
    pango-devel \
    cairo-devel \
    gdk-pixbuf2-devel \
    libxkbcommon-devel

RUN pip install --upgrade pip
RUN pip install briefcase

WORKDIR /app

CMD ["/bin/bash"]