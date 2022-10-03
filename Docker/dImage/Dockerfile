FROM voidlinux:voidlinux

RUN \
	xbps-install -Suv

COPY dimage /

USER nobody

ENTRYPOINT ["/dimage"]
