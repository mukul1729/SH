# We're using a multistage Docker build here in order to allow us to release a self-verifying
# Docker image when built on the official Docker infrastructure.
# They require us to verify the source integrity in some way while making sure that this is a
# reproducible build.
# See https://github.com/docker-library/official-images#image-build
# In order to achieve this, we externally host the rootfs archives and their checksums and then
# just download and verify it in the first stage of this Dockerfile.
# The second stage is for actually configuring the system a little bit.
# Some templating is done in order to allow us to easily build different configurations and to
# allow us to automate the releaes process.
FROM alpine:3.12 AS verify
RUN apk add --no-cache curl bash
SHELL ["/bin/bash", "-c"]
# https://gitlab.archlinux.org/archlinux/archlinux-docker/-/releases/v20220109.0.43549
RUN ROOTFS="$(curl -sOJL -w "%{filename_effective}" "https://gitlab.archlinux.org/archlinux/archlinux-docker/-/package_files/1922/download")" && \
    sha256sum -c <<< "fc32cdef7b007f0fb21320440d52fa8e8351765b071e4a491ce2ef5c11f10139  base-20220109.0.43549.tar.xz" && \
    mkdir /rootfs && \
    tar -C /rootfs --extract --file "${ROOTFS}"

FROM scratch AS root
COPY --from=verify /rootfs/ /

RUN ldconfig

ENV LANG=en_US.UTF-8
CMD ["/usr/bin/bash"]

