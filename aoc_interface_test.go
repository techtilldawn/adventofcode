package adventofcode

import (
	"testing"
	"time"
)

func TestFolderPath(t *testing.T) {
	t.Run("Test FolderPath", func(t *testing.T) {
		got := FolderPath(time.Date(2025, 12, 4, 0, 0, 0, 0, time.UTC))
		want := "./2025/04"

		if got != want {
			t.Errorf("FolderPath() = %v; want %v", got, want)
		}
	})
	t.Run("Test DownloadInputUrl", func(t *testing.T) {
		got := DownloadInputUrl(time.Date(2025, 12, 4, 0, 0, 0, 0, time.UTC))
		want := "https://adventofcode.com/2025/day/4/input"

		if got != want {
			t.Errorf("DownloadInputUrl() = %v; want %v", got, want)
		}
	})
}
