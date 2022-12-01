package calories

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
	"testing"
)
import "github.com/stretchr/testify/assert"

func TestWithRealInput(t *testing.T) {
	filename := "./input.txt"
	lines, err := LinesFromFile(filename)
	if err != nil {
		assert.Failf(t, "Could not read from file %s", filename)
	}
	cals, err := mostCalories(lines)
	assert.NoError(t, err)
	assert.Equal(t, 68775, cals)
}

type Elf []int

func mostCalories(lines []string) (int, error) {
	elves, err := parse(lines)
	if err != nil {
		return 0, err
	}
	maxFound := math.MinInt
	for _, elf := range elves {
		cals := countCalories(elf)
		if cals > maxFound {
			maxFound = cals
		}
	}
	return maxFound, nil
}

func countCalories(elf Elf) int {
	tot := 0
	for _, num := range elf {
		tot += num
	}
	return tot
}

func parse(lines []string) ([]Elf, error) {
	elves := []Elf{}
	currentElf := []int{}
	for _, line := range lines {
		if line == "" {
			elves = append(elves, currentElf)
			currentElf = []int{}
			continue
		}
		num, err := strconv.ParseInt(line, 10, 64)
		if err != nil {
			return nil, fmt.Errorf(`Could not parse "%s", giving up on the whole input`, line)
		}
		currentElf = append(currentElf, int(num))
	}
	elves = append(elves, currentElf)
	return elves, nil
}

func LinesFromFile(filename string) ([]string, error) {
	// reading whole file into mem because I know AoC inputs are not that big
	file, err := os.ReadFile(filename)
	if err != nil {
		return nil, err
	}
	lines := strings.Split(string(file), "\n")
	if strings.TrimSpace(lines[len(lines)-1]) == "" {
		return lines[:len(lines)-1], nil
	}
	return lines, nil
}
