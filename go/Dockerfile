FROM golang:alpine as caddy

RUN apk update && apk upgrade && apk add --no-cache git

RUN go get -u github.com/mholt/caddy && \
    go get -u github.com/caddyserver/builds

WORKDIR /go/src/github.com/mholt/caddy/caddy/

RUN go run build.go

RUN cp /go/src/github.com/mholt/caddy/caddy/caddy /go/bin/


FROM alpine:latest

RUN apk update && apk upgrade && apk add --no-cache ca-certificates

COPY --from=caddy /go/bin/caddy /usr/bin/caddy

COPY ./go/Caddyfile.dev /etc/Caddyfile.dev

COPY ./go/Caddyfile.prod /etc/Caddyfile.prod

CMD /usr/bin/caddy --conf=/etc/$CADDY_FILE --agree=true --email=$CADDY_EMAIL
