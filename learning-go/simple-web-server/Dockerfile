FROM golang:1.16-alpine

WORKDIR /app

COPY . /app
RUN go mod download
ENV PORT=4000
RUN go build -o /web-server
EXPOSE 4000
CMD ["/web-server"]