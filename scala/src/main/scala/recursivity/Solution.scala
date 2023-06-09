package recursivity

import scala.annotation.tailrec

object Solution {

  private val ROMAN_MAP: Map[Char, Int] = Map('I' -> 1, 'V' -> 5, 'X' -> 10, 'L' -> 50, 'C' -> 100, 'D' -> 500, 'M' -> 1000)

  def romanToInt(s: String): Int = {

    @tailrec
    def romanToIntRecursive(listChar: List[Char], sum: Int): Int = listChar match {
      case Nil => sum
      case x :: Nil => sum + ROMAN_MAP(x)
      case x :: y :: tail if ROMAN_MAP(y) > ROMAN_MAP(x) =>
        romanToIntRecursive(tail, sum + ROMAN_MAP(y) - ROMAN_MAP(x))
      case x :: tail => romanToIntRecursive(tail, sum + ROMAN_MAP(x))

    }

    romanToIntRecursive(s.toList, 0)
  }

}

object Main extends App{

  println(Solution.romanToInt("III"))
  println(Solution.romanToInt("LVIII"))
  println(Solution.romanToInt("MCMXCIV"))

}