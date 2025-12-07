package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

func CalcRotationOutcome(instruction string, start int) int {
	direction := instruction[0:1]
	stepsString := instruction[1:]
	stepsInt, err := strconv.Atoi(stepsString)

	if err != nil {
		return 0
	}

	move := stepsInt
	if direction == "L" {
		move = -stepsInt
	}

	totalDisplacement := start + move

	modulus := 100

	newPosition := (totalDisplacement%modulus + modulus) % modulus

	return newPosition
}

func ReadFileContent(filePath string) (string, error) {
	content, err := os.ReadFile(filePath)
	if err != nil {
		return "", fmt.Errorf("could not read file %s: %w", filePath, err)
	}
	return string(content), nil
}

func main() {
	input, err := ReadFileContent("input.txt")

	if err != nil {
		fmt.Println("Error reading input file:", err)
		return
	}

	position := 50
	instructions := strings.Split(strings.TrimSpace(input), "\n")
	count := 0

	for _, instruction := range instructions {
		newPosition := CalcRotationOutcome(instruction, position)
		position = newPosition
		if position == 0 {
			count++
		}
	}
	fmt.Printf("Final Position: %d, Total Clicks: %d\n", position, count)
}
