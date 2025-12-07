package main

import (
	"testing"
)

var latestInput int

func TestCalcRotationOutcome(t *testing.T) {
	t.Run("OneClick", func(t *testing.T) {
		got := CalcRotationOutcome("L68", 50)
		want := 82

		if got != want {
			t.Errorf("got %d; want %d", got, want)
		}
	})
	t.Run("TwoClicks", func(t *testing.T) {
		got := CalcRotationOutcome("L158", 18)
		want := 60

		if got != want {
			t.Errorf("got %d; want %d", got, want)
		}
	})
	t.Run("FourClicks", func(t *testing.T) {
		got := CalcRotationOutcome("R400", 18)
		want := 18

		if got != want {
			t.Errorf("got %d; want %d", got, want)
		}
	})
}
