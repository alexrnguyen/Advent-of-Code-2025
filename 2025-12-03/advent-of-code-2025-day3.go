package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func readInput(filePath string) []string {
	file, _ := os.Open(filePath)

	defer file.Close()

	scanner := bufio.NewScanner(file)

	var content []string

	for scanner.Scan() {
		line := scanner.Text()
		content = append(content, line)
	}

	return content
}

func part1(content []string) int {
	totalOutputJoltage := 0

	for _, bank := range content {

		bankTable := make([]int, len(bank))
		bankTable[0], _ = strconv.Atoi(string(bank[0]))
		for i := 1; i < len(bank); i++ {
			leftNum := bankTable[0]
			for j := 0; j <= i; j++ {
				rightNum, _ := strconv.Atoi(string(bank[j]))
				joltageCandidate, _ := strconv.Atoi(strconv.Itoa(leftNum) + strconv.Itoa(rightNum))
				if rightNum > leftNum && j < i {
					leftNum = rightNum
				}
				if joltageCandidate > bankTable[i-1] {
					bankTable[i] = joltageCandidate
				} else {
					bankTable[i] = bankTable[i-1]
				}
			}
			totalOutputJoltage += bankTable[len(bank)-1]
		}
	}

	return totalOutputJoltage
}

func main() {
	filePath := "day3-input.txt"
	content := readInput(filePath)
	fmt.Println("Part 1 Total Output Joltage:", part1(content))
}
