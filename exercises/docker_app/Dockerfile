FROM golang:alpine

WORKDIR /go/src/app

COPY . /go/src/app

RUN go mod init && \
    go build -o helloworld && \
    go mod tidy

EXPOSE 6111

CMD ["./helloworld"]