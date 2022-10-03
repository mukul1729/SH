using System.Collections;
using System.Collections.Specialized;
static List<T> CopyNames<T>(
		List<T> input, int maxElements)
{
	int actualCount = maxElements;
	List<T> ret = new List<T>(actualCount);
	for (int i = 0; i < actualCount; i++)
		ret.Add(input[i]);
	return ret;
}
static void Main()
{
	List<int> numbers  = new List<int>();
	numbers.Add(10);
	numbers.Add(9);
	numbers.Add(2);
	
	List<int> firstTwo = CopyNames<int>(numbers,2);
	Console.WriteLine(firstTwo);
}
