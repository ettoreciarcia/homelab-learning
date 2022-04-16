FROM golang:1.16-alpine

WORKDIR /app

COPY . /app
RUN go mod download
RUN go build -o /web-server
EXPOSE 4000
CMD ["/web-server"]