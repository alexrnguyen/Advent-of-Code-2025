Console.WriteLine("Enter a file path containing input data: ");
string filePath = Console.ReadLine();
string input = File.ReadAllText(filePath);


IEnumerable<string> productIDs = input.Split(',');
long sumOfInvalidIds = 0;

foreach (string productID in productIDs)
{
    long firstID = long.Parse(productID.Split('-')[0]);
    long secondID = long.Parse(productID.Split('-')[1]);

    long range = secondID - firstID;

    for (long i = firstID; i <= secondID; i++)
    {
        string idInRange = i.ToString();

        if (idInRange.Length % 2 == 1)
        {
            continue;
        }
        else
        {
            int leftPtr = 0;
            int rightPtr = idInRange.Length / 2;
            string longestSubstring = "";
            for (int j = 0; j < idInRange.Length/2; j++)
            {
                if (idInRange[leftPtr] == idInRange[rightPtr])
                {
                    longestSubstring += idInRange[j];
                    leftPtr++;
                    rightPtr++;
                }
                else
                {
                    longestSubstring = "";
                    break;
                }
            }

            longestSubstring = string.Concat(Enumerable.Repeat(longestSubstring, 2));

            if (longestSubstring != "")
            {
                sumOfInvalidIds += long.Parse(longestSubstring);
            }
        }
    }

}

Console.WriteLine($"Result: {sumOfInvalidIds}");
return 0;