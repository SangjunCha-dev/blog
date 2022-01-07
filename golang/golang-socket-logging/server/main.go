package main

import (
	"encoding/json"
	"fmt"
	"io"
	"io/ioutil"
	"log"
	"net"
	"time"

	rotatelogs "github.com/lestrrat-go/file-rotatelogs"
)

type Config struct {
	LogPath    string `json:"log_path"`
	LogName    string `json:"log_name`
	ServerPort string `json:"server_port"`
}

var MyConfig Config = Config{}

// 로그 설정
func setLog() {
	con, err := ioutil.ReadFile("./config.json")
	if err != nil {
		log.Print("[error] setLog", err)
	}
	if err := json.Unmarshal(con, &MyConfig); err != nil {
		log.Print("[error] setLog", err)
	}

	rl, _ := rotatelogs.New(
		MyConfig.LogPath+"/log.%Y-%m-%d.log",
		rotatelogs.WithMaxAge(-1),              // 정해진 시간보다 지난 파일 삭제 (-1은 비활성화)
		rotatelogs.WithRotationTime(time.Hour), // 로테이션 반복 주기
		rotatelogs.WithClock(rotatelogs.Local), // 로컬 시간으로 설정
		rotatelogs.WithRotationCount(90),       // 유지되는 파일 개수
	)
	log.SetFlags(log.Ldate | log.Ltime | log.Lmicroseconds)
	log.SetOutput(rl)
}

func loggingServer() {
	l, err := net.Listen("tcp", ":"+MyConfig.ServerPort)
	if err != nil {
		log.Println(err)
	}
	defer l.Close()

	fmt.Println("Logging Server Start Port :", MyConfig.ServerPort)

	for {
		conn, err := l.Accept()
		if err != nil {
			log.Println(err)
			continue
		}
		defer conn.Close()
		go ConnHandler(conn)
	}
}

func ConnHandler(conn net.Conn) {
	recvBuf := make([]byte, 4096)
	for {
		n, err := conn.Read(recvBuf)
		if err != nil {
			if err == io.EOF {
				log.Println(err)
				return
			}
			log.Println(err)
			return
		}
		if 0 < n {
			data := recvBuf[:n]
			log.Println(string(data))

		}
	}
}

func main() {
	setLog()
	loggingServer()
}
