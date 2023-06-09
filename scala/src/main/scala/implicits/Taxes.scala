package implicits

case class Product(name: String, price: Double, category: String)

trait TaxCalculator {
  def calculateTax(p: Product): Double
}

object TaxRates {

  implicit val franceRate: TaxCalculator = (p: Product) => p.category match {
    case "food" => p.price * 0.055
    case _ => p.price * 0.20
  }

  implicit val germanRate: TaxCalculator = (p: Product) => p.category match {
    case "food" => p.price * 0.07
    case _ => p.price * 0.19
  }

  implicit val englandRate: TaxCalculator = (p: Product) => p.category match {
    case "food" => p.price * 0.0
    case _ => p.price * 0.175
  }

  def calculateTotalPrice(product: Product)(implicit taxCalculator: TaxCalculator): Double = {
    val tax = taxCalculator.calculateTax(product)
    product.price + tax
  }

}

object Taxes extends App {

  import TaxRates.franceRate

  println(TaxRates.calculateTotalPrice(Product("lait", 2, "food")))
  println(TaxRates.calculateTotalPrice(Product("television", 2, "entertainment")))

}