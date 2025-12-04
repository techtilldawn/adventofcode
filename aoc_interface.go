package adventofcode

import (
	"io"
	"net/http"
	"os"
	"strconv"
	"time"
)

func FolderPath(t time.Time) string {
	year := t.Year()
	day := t.Day()
	dayStr := strconv.Itoa(day)
	if day < 10 {
		dayStr = "0" + strconv.Itoa(day)
	}
	return "./" + strconv.Itoa(year) + "/" + dayStr
}

func CreateDirectory(path string) error {
	if err := os.MkdirAll(path, os.ModePerm); err != nil {
		return err
	}
	return nil
}

func CheckDirectoryExists(path string) bool {
	info, err := os.Stat(path)
	if os.IsNotExist(err) {
		return false
	}
	return info.IsDir()
}

func DownloadInputUrl(t time.Time) string {
	baseUrl := "https://adventofcode.com/"
	url := baseUrl + strconv.Itoa(t.Year()) + "/day/" + strconv.Itoa(t.Day()) + "/input"
	return url
}

// rework tomoz me...
func DownloadInputFile(url string) {
	sessionCookie := os.Getenv("AOC_SESSION_COOKIE")
	if sessionCookie == "" {
		panic("AOC_SESSION_COOKIE environment variable not set")
	}

	req, err := http.NewRequest("GET", url, nil)
	if err != nil {
		panic(err)
	}

	req.Header.Add("Cookie", "session="+sessionCookie)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	if resp.StatusCode != http.StatusOK {
		panic("Failed to download input file: " + resp.Status)
	}

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		panic(err)
	}
	file, err := os.Create("input.txt")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	_, err = file.Write(body)
	if err != nil {
		panic(err)
	}
}

func FillCurrentYearAndDay() {
	t := time.Now()
	if t.Month() != time.December {
		return // Only fill during December
	}
	for day := 1; day <= t.Day(); day++ {
		folderToCreate := FolderPath(t)
		if CheckDirectoryExists(folderToCreate) {
			continue
		}
		if err := CreateDirectory(folderToCreate); err != nil {
			panic(err)
		}
	}
}
