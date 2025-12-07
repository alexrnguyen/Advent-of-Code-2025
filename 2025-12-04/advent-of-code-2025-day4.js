const fs = require('fs');

function readLinesFromFile(filePath) 
{
    const content = fs.readFileSync(filePath, 'utf-8');
    const lines = content.split(/\r?\n/); // Split by common line endings
    return lines.map(line => line.split(''));
}

function getAllNeighbors(arr, row, col) 
{
    const neighbours = [];
    const numRows = arr.length;
    const numCols = arr[row] ? arr[row].length : 0;

    for (let dx = -1; dx <= 1; dx++)
    {
        for (let dy = -1; dy <= 1; dy++)   
        {
            if (dx === 0 && dy === 0) 
            {
                continue;
            }

            const newRow = row + dx;
            const newCol = col + dy;

            // Check if the new coordinates are within the array bounds
            if (newRow >= 0 && newRow < numRows && newCol >= 0 && newCol < numCols) 
            {
                neighbours.push(arr[newRow][newCol]);
            }
        }
    }

    return neighbours;
}

function part1(content)
{
    let numAccessibleRolls = 0;
    for (let row = 0; row < content.length; row++)
    {
        for (let col = 0; col < content[row].length; col++)
        {
            if (content[row][col] === '@')
            {
                const neighbours = getAllNeighbors(content, row, col);
                const numAdjacentRolls = neighbours
                    .map(neightbour => neightbour === '@' ? 1 : 0)
                    .reduce((acc, curr) => acc + curr, 0);
                
                if (numAdjacentRolls < 4) 
                {
                    numAccessibleRolls++;
                }
            }
        }
    }

    console.log(`Part 1 Number of accessible rolls: ${numAccessibleRolls}`);
}

function part2(content)
{
    let totalAccessibleRolls = 0;
    let numAccessibleRolls = 0;
    do
    {
        numAccessibleRolls = 0;
        for (let row = 0; row < content.length; row++)
        {
            for (let col = 0; col < content[row].length; col++)
            {
                if (content[row][col] === '@')
                {
                    const neighbours = getAllNeighbors(content, row, col);
                    const numAdjacentRolls = neighbours
                        .map(neightbour => neightbour === '@' ? 1 : 0)
                        .reduce((acc, curr) => acc + curr, 0);
                    
                    if (numAdjacentRolls < 4) 
                    {
                        content[row][col] = "x";
                        numAccessibleRolls++;
                    }
                }
            }
        }
        totalAccessibleRolls += numAccessibleRolls
    } while (numAccessibleRolls > 0)

    console.log(`Part 2 Number of accessible rolls: ${totalAccessibleRolls}`);
}


const content = readLinesFromFile("day4-input.txt");
part1(content);
part2(content);