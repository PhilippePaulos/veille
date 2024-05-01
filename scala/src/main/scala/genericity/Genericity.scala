package genericity

import utils.Display

import scala.annotation.tailrec

object Genericity extends App with Display {

  private def max[T](list: List[T], cmp: (T, T) => Boolean): Option[T] = {

    @tailrec
    def maxRecursive(list: List[T], max: Option[T]): Option[T] = list match {
      case Nil => max
      case head :: tail =>
        val newMax = max.fold(head)(m => if (cmp(head, m)) head else m)
        maxRecursive(tail, Some(newMax))
    }

    maxRecursive(list, None)
  }


  var strings = List("foo", "baro", "baz")
  val longestString = max(strings, (s1: String, s2: String) => s1.length > s2.length)
  println(longestString)
  longestString.foreach(e => f"Max is ${e}")

}
