package calories

import (
	"os"
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
	cals := mostCalories(lines)
	assert.Equal(t, 1000, cals)
}

func mostCalories(lines []string) interface{} {
	return nil
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
