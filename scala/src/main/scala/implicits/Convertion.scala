package implicits

import utils.Display

trait Converter[T] {
    def convert(s: String): T
}

object Converters {
  implicit val intConverter: Converter[Int] = (s: String) => s.toInt
  implicit val doubleConverter: Converter[Double] = (s: String) => s.toDouble
  implicit val floatConverter: Converter[Float] = (s: String) => s.toFloat
  implicit val stringConvertor: Converter[String] = (s: String) => s
}

object Solution {

  def convert[T](s: String)(implicit converter: Converter[T]): T = {
    converter.convert(s)
  }
}

object Convertion extends App with Display{
  import Converters._

  Solution.convert[Int]("123").show()
}