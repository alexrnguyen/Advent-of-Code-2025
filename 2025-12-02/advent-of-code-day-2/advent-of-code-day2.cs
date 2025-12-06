namespace Solution
{
    public class Solution
    {
        public long Part1(IEnumerable<string> productIDs)
        {
            long sumOfInvalidIds = 0;

            foreach (string productID in productIDs)
            {
                long firstID = long.Parse(productID.Split('-')[0]);
                long secondID = long.Parse(productID.Split('-')[1]);

                long range = secondID - firstID;

                for (long i = firstID; i <= secondID; i++)
                {
                    string idInRange = i.ToString();

                    if (idInRange.Length % 2 == 0)
                    {
                        int leftPtr = 0;
                        int rightPtr = idInRange.Length / 2;
                        string longestSubstring = "";
                        for (int j = 0; j < idInRange.Length / 2; j++)
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
            return sumOfInvalidIds;
        }
        public static void Main(string[] args)
        {
            Solution solutionInstance = new Solution();
            Console.WriteLine("Enter a file path containing input data: ");
            string filePath = Console.ReadLine();
            string input = File.ReadAllText(filePath);
            IEnumerable<string> productIDs = input.Split(',');
            Console.WriteLine($"Part 1 Result: {solutionInstance.Part1(productIDs)}");
        }
    }
}