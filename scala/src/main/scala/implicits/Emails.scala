package implicits

case class Order(id: Int, items: String, total: Int)

trait CurrencyFormatter[T] {
  def format(total: Int): T
}

object Formatters {
  implicit val intFormatter: CurrencyFormatter[Int] = (t: Int) => t
  implicit val doubleFormatter: CurrencyFormatter[Double] = (t: Int) => t.toDouble
  implicit val floatFormatter: CurrencyFormatter[Float] = (t: Int) => t.toFloat
  implicit val stringFormatter: CurrencyFormatter[String] = (t: Int) => t.toString
}

object Emails extends App {

  private def printOrder[T](o: Order)(implicit formater: CurrencyFormatter[T]): Unit = {
    print(s"Id: ${o.id}, items: ${o.items}, total: ${formater.format(o.total)}")
  }


  import Formatters.intFormatter
  printOrder(Order(1, "PS5", 10))
}
