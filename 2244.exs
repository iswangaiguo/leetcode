defmodule Solution do
  @spec minimum_rounds(tasks :: [integer]) :: integer
  def minimum_rounds(tasks) do
    map = Enum.frequencies(tasks)
  end
end

map = Solution.minimum_rounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4])
list = Enum.map(map, fn {key, value} -> value end)
Enum.each(list, &IO.puts/1)



