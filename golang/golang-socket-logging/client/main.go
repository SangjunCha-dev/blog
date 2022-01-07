package main

import (
	"fmt"
	"net"
	"strconv"
	"time"
)

func main() {
	conn, err := net.Dial("tcp", ":8010")
	if nil != err {
		fmt.Println(err)
	}

	cnt := 1
	for {
		msg := "hello world " + strconv.Itoa(cnt)
		conn.Write([]byte(msg))
		fmt.Println(msg)
		time.Sleep(time.Duration(1) * time.Second)
		cnt += 1
	}
}
